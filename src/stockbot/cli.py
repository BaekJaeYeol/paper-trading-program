from contextlib import closing
import argparse
import csv
import json
import logging
import math
import re
import sqlite3
import time
from datetime import date, datetime, timedelta, timezone
from pathlib import Path
from zoneinfo import ZoneInfo
from .broker import AlpacaPaper
from .cadence import Cadence
from .power import SleepGuard
from .core import Bar, signal, size, backtest
from .strategies import LABELS,decision
from .ui_safety import unresolved_attempts
from .brackets import enforce_entry
from .paper_journal import initialize,bind_account,fingerprint,intent,submitted,submission_uncertain,ReconciliationTimeout

NY = ZoneInfo("America/New_York")

def load_config(path):
    c = json.loads(Path(path).read_text())
    for key in ("max_position_fraction","max_daily_loss","stop_loss","take_profit","max_gap","max_spread"):
        if not 0 < c[key] < 1:
            raise ValueError(f"Invalid {key}")
    if not c["symbols"] or len(set(c["symbols"])) != len(c["symbols"]) or any(not re.fullmatch(r"[A-Z][A-Z0-9.]{0,9}", s) for s in c["symbols"]):
        raise ValueError("Invalid symbols")
    if c["max_positions"] < 1 or c["volume_ratio"] <= 0 or c["max_quote_age_seconds"] <= 0:
        raise ValueError("Invalid limits")
    c.setdefault('entry_strategy','baseline')
    if c['entry_strategy'] not in LABELS:raise ValueError('Invalid entry strategy')
    return c

def read_csv(path):
    with open(path, newline="") as f:
        return [Bar(date.fromisoformat(r["date"]), *(float(r[k]) for k in ("open","high","low","close","volume"))) for r in csv.DictReader(f)]

def now_parse(value):
    return datetime.fromisoformat(value.replace("Z","+00:00"))

def _halted(c, root):
    return (root/'STOP').exists() or bool(c.get('_stop_event') and c['_stop_event'].is_set())

def _cycle(c, execute=False, broker=None):
    root = Path(c["state_dir"])
    root.mkdir(parents=True, exist_ok=True)
    if _halted(c,root):
        return {"status":"halted"}
    if execute and unresolved_attempts(root):
        raise RuntimeError("Unresolved orders block new submissions; reconcile in broker dashboard")
    b = broker or AlpacaPaper()
    clock = b.request("/v2/clock")
    now = now_parse(clock["timestamp"])
    if not clock["is_open"]:
        return {"status":"market_closed"}
    today = now.astimezone(NY).date()
    calendar = b.request("/v2/calendar", {"start":(today-timedelta(days=14)).isoformat(),"end":(today-timedelta(days=1)).isoformat()})
    if not calendar:
        raise ValueError("Missing previous trading session")
    session = date.fromisoformat(calendar[-1]["date"])
    account = b.request("/v2/account")
    if account.get("trading_blocked") or account.get("account_blocked") or account.get("status") != "ACTIVE":
        raise ValueError("Account unavailable")
    equity, bp, last = (float(account[k]) for k in ("equity","buying_power","last_equity"))
    if not all(math.isfinite(x) and x > 0 for x in (equity,bp,last)):
        raise ValueError("Invalid account values")
    if equity <= last*(1-c["max_daily_loss"]):
        return {"status":"daily_loss_limit"}
    positions = b.request("/v2/positions")
    # Refuse to operate alongside positions not managed by this long-only bot.
    if any(float(p["qty"]) < 0 for p in positions):
        raise ValueError("Short position detected")
    orders = b.request("/v2/orders", {"status":"open","limit":500,"nested":"false"})
    if len(orders) >= 500:
        raise ValueError("Order snapshot may be truncated")
    occupied = {p["symbol"] for p in positions} | {o["symbol"] for o in orders}
    # Conservative reserve: subtract open buy notional even if broker BP already reserves it.
    reserve = sum(float(o["qty"])*float(o.get("limit_price") or 0) for o in orders if o["side"] == "buy")
    if any(o["side"] == "buy" and not o.get("limit_price") for o in orders):
        raise ValueError("Unpriced pending buy; cannot bound exposure")
    bp = max(0,bp-reserve)
    result = []
    strategy=c.get('entry_strategy','baseline')
    if strategy not in LABELS:raise ValueError('Invalid entry strategy')
    excluded={}
    with closing(sqlite3.connect(root/"orders.sqlite", timeout=30)) as db:
        initialize(db)
        # Serialize all bot processes across decision and submission, including unknown results.
        db.execute("BEGIN IMMEDIATE")
        if execute:bind_account(db,fingerprint(account))
        for symbol in c["symbols"]:
            if symbol in occupied or len(occupied) >= c["max_positions"]:
                continue
            rows = b.bars(symbol, (session-timedelta(days=180)).isoformat(), today.isoformat(), c["feed"])
            bars = [Bar(now_parse(r["t"]).astimezone(NY).date(),r["o"],r["h"],r["l"],r["c"],r["v"]) for r in rows if now_parse(r["t"]).astimezone(NY).date() <= session]
            if not bars or bars[-1].day != session:
                continue
            s = signal(bars,c["volume_ratio"],c["max_return"])
            if not s:
                continue
            check=decision(bars,strategy)
            if not check['allowed']:
                excluded[check['reason']]=excluded.get(check['reason'],0)+1
                continue
            s['entry_filter']=check
            q = b.quote(symbol,c["feed"])
            age = (now-now_parse(q["t"])).total_seconds()
            bid, ask = float(q["bp"]),float(q["ap"])
            if not all(math.isfinite(x) and x > 0 for x in (bid,ask)) or ask < bid or not 0 <= age <= c["max_quote_age_seconds"]:
                continue
            if (ask-bid)/ask > c["max_spread"] or abs(ask/s["close"]-1) > c["max_gap"]:
                continue
            limit = round(ask,2)
            qty = size(equity,bp,limit,c["max_position_fraction"])
            if qty < 1:
                continue
            cid = f"sb-v1-{symbol}-{session.isoformat()}"
            stop = round(s["close"]*(1-c["stop_loss"]),2)
            target = round(s["close"]*(1+c["take_profit"]),2)
            if not 0 < stop < limit < target:
                continue
            body = {"symbol":symbol,"qty":str(qty),"side":"buy","type":"limit","limit_price":str(limit),"time_in_force":"day","order_class":"bracket","client_order_id":cid,"take_profit":{"limit_price":str(target)},"stop_loss":{"stop_price":str(stop)}}
            if db.execute("SELECT 1 FROM attempts WHERE id=?",(cid,)).fetchone():
                continue
            if execute:
                if _halted(c,root):
                    break
                # Commit intent BEFORE network I/O: crashes/timeouts never trigger blind resubmission.
                enforce_entry(db,positions)
                intent(db,cid,body)
                db.commit()
                db.execute("BEGIN IMMEDIATE")
                try:
                    response=b.request("/v2/orders",body=body)
                    submitted(db,cid,response)
                except Exception:
                    submission_uncertain(db,cid)
                    db.commit()
                    raise RuntimeError(f"Submission uncertain for {cid}; reconcile in broker dashboard") from None
            result.append({"signal":s,"order":body,"submitted":execute})
            occupied.add(symbol)
            bp -= qty*limit
        db.commit()
    return {"status":"ok","orders":result,"entry_filter":{"strategy":strategy,"excluded":excluded}}

def cycle(c, execute=False, broker=None):
    root = Path(c["state_dir"])
    root.mkdir(parents=True, exist_ok=True)
    lock = root / "cycle.lock"
    try:
        lock.mkdir()
    except FileExistsError:
        raise RuntimeError("Another cycle is active or stale cycle.lock exists; inspect before removing") from None
    try:
        return _cycle(c, execute, broker)
    finally:
        lock.rmdir()


def stop_requested(c):
    return bool(c.get('state_dir')) and (Path(c['state_dir'])/'STOP').is_file()

def wait_for_run(c,delay):
    deadline=time.monotonic()+delay
    while True:
        if stop_requested(c):raise SystemExit('STOP active; automatic run stopped')
        remaining=deadline-time.monotonic()
        if remaining<=0:return
        time.sleep(min(5,remaining))


def main():
    ap = argparse.ArgumentParser()
    ap.add_argument("command", choices=["demo","backtest","scan","paper","run","reconcile","research"])
    ap.add_argument("--config",default="config.json")
    ap.add_argument("--csv",default="examples/demo.csv")
    ap.add_argument("--interval",type=int,default=300)
    ap.add_argument("--execute-paper",action="store_true")
    ap.add_argument('--fee-bps',type=float,default=10.)
    ap.add_argument('--slippage-bps',type=float,default=10.)
    ap.add_argument('--sell-tax-bps',type=float,default=0.)
    ap.add_argument('--capital',type=float,default=10000.)
    args = ap.parse_args()
    logging.basicConfig(level=logging.INFO,format="%(asctime)s %(levelname)s %(message)s")
    c = load_config(args.config)
    if args.command in ("demo","backtest"):
        bars = read_csv(args.csv)
        # Validate ordering even when no signals are evaluated.
        if any(a.day >= b.day for a,b in zip(bars,bars[1:])):
            raise ValueError("CSV must be sorted with unique dates")
        print(json.dumps(backtest(bars,c),indent=2))
        return
    if args.command=='research':
        if args.execute_paper:ap.error('research never accepts --execute-paper')
        from .research import compare
        print(json.dumps(compare(read_csv(args.csv),c,cash=args.capital,fee=args.fee_bps/10000,slippage=args.slippage_bps/10000,sell_tax=args.sell_tax_bps/10000),ensure_ascii=False,indent=2,allow_nan=False))
        return
    if args.command=='reconcile':
        if args.execute_paper:ap.error('reconcile never accepts --execute-paper')
        from .paper_journal import reconcile_snapshot,account_snapshot
        print(json.dumps(reconcile_snapshot(c,AlpacaPaper(),account_snapshot),ensure_ascii=False,indent=2))
        return
    if args.command in ("paper","run") and not args.execute_paper:
        ap.error("paper/run requires --execute-paper (simulated orders only)")
    if args.interval < 30:
        ap.error("interval must be >= 30 seconds")
    guard=SleepGuard() if args.command=='run' else None
    try:
        if guard and stop_requested(c):raise SystemExit('STOP active; automatic run stopped')
        if guard and not guard.acquire():raise SystemExit('Windows sleep request failed; automatic run blocked')
        cadence=Cadence(args.interval,time.monotonic())
        while True:
            if args.command=='run' and stop_requested(c):raise SystemExit('STOP active; automatic run stopped')
            if not cadence.claim(time.monotonic()):
                wait_for_run(c,cadence.delay(time.monotonic()));continue
            try:
                if args.command in ('paper','run'):
                    from .paper_journal import reconcile_snapshot,account_snapshot
                    b=AlpacaPaper();snapshot=reconcile_snapshot(c,b,account_snapshot)
                    if snapshot['reconciliation']['unresolved'] or not snapshot['inventory']['ready']:raise SystemExit('Reconciliation blocked entry; inspect orders/holdings before restarting')
                    result=cycle(c,True,b)
                else:result=cycle(c,False)
                print(json.dumps(result,indent=2),flush=True)
            except ReconciliationTimeout:
                raise SystemExit('Full reconciliation timed out; inspect account/orders and restart explicitly') from None
            except Exception as exc:
                logging.error("Cycle stopped: %s",exc)
                if args.command != "run":
                    raise SystemExit(1) from None
            if args.command != "run":
                return
            cadence.complete(time.monotonic())
            delay=cadence.delay(time.monotonic())
            logging.info('Next cycle in %.1f seconds; skipped slots: %d',delay,cadence.skipped)
            wait_for_run(c,delay)
    finally:
        if guard and not guard.release():logging.warning('Sleep request release failed; inspect Windows power state')

if __name__ == "__main__":
    main()
