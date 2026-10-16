"""Bounded intraday session, with a durable checkpoint after every cycle."""
import argparse
import datetime as dt
import json
import subprocess
import time
from pathlib import Path
from state_recovery import state_lock

SYMBOLS=['SPY','QQQ','IWM','DIA','MSFT','JPM','XOM','JNJ','CAT','WMT']

def next_poll(now):
    return ((int(now)-420)//900+1)*900+420

def git(repo,*args):
    return subprocess.run(['git',*args],cwd=repo,check=True,text=True,capture_output=True,timeout=90).stdout

def refresh(repo):
    for attempt in range(3):
        try:
            git(repo,'pull','--rebase','origin','paper-hourly-state')
            return
        except (subprocess.CalledProcessError,subprocess.TimeoutExpired):
            # Never retry an unresolved rebase or merge conflict.
            base=Path(repo)/'.git'
            if any((base/name).exists() for name in ('rebase-merge','rebase-apply','MERGE_HEAD')) or attempt==2:
                raise
            time.sleep(2*(attempt+1))

def publish(repo):
    git(repo,'add','intraday-state')
    # Root ignore rules intentionally exclude GUI databases; persist only the
    # credential-free research checkpoints needed by the next runner.
    if any((Path(repo)/'intraday-state').glob('**/accounts/*.sqlite')):
        git(repo,'add','--force','--',':(glob)intraday-state/**/accounts/*.sqlite')
    code=subprocess.run(['git','diff','--cached','--quiet'],cwd=repo).returncode
    if code not in (0,1):raise RuntimeError('저장 변경 검사 실패')
    if code==1:
        git(repo,'commit','-m','기록: 장중 세션 15분 갱신·계좌·운영 상태 저장')
    # A previous failed push may have left an unpushed commit despite a clean tree.
    for attempt in range(3):
        refresh(repo)
        try:
            git(repo,'push','origin','HEAD:paper-hourly-state')
            return
        except (subprocess.CalledProcessError,subprocess.TimeoutExpired):
            # A lost push response can still mean success; refresh before retry.
            if attempt==2:raise

def run_session(tick,persist,refresh_state,bounds,max_seconds=19800,once=False,
                clock=time.time,sleep=time.sleep,stopped=lambda:False):
    deadline=clock()+max_seconds
    cycles=0
    last_code=0
    while clock()<deadline:
        refresh_state()
        now=clock()
        window=bounds(now)
        if not once and (window is None or now<window[0]-12600 or now>window[1]+1800):
            break
        result=tick()
        cycles+=1
        last_code=int(any(info['status']=='error' for info in result['symbols'].values()))
        persist()
        if once or stopped():break
        # Align to wall-clock slots, independent of collection duration.
        due=next_poll(clock())
        while clock()<min(due,deadline):
            sleep(min(60,min(due,deadline)-clock()))
            refresh_state()
            if stopped():
                tick()
                persist()
                return last_code,cycles
    return last_code,cycles

def main():
    parser=argparse.ArgumentParser()
    parser.add_argument('--repo',required=True)
    parser.add_argument('--once',action='store_true')
    parser.add_argument('--max-seconds',type=int,default=19800)
    args=parser.parse_args()
    if not 1<=args.max_seconds<=19800:parser.error('세션은 최대 5시간 30분입니다')
    from intraday import tick,NY
    from reliability import session_bounds
    repo=Path(args.repo).resolve()
    state=repo/'intraday-state'
    def bounds(now):
        return session_bounds(dt.datetime.fromtimestamp(now,NY).date())
    with state_lock(repo):
        code,cycles=run_session(lambda:tick(state,symbols=SYMBOLS),lambda:publish(repo),
                                lambda:refresh(repo),bounds,max_seconds=args.max_seconds,once=args.once,
                                stopped=lambda:(state/'emergency-stop.json').exists())
    print(json.dumps(dict(mode='once' if args.once else 'warm-session',cycles=cycles,exit_code=code)))
    return code

if __name__=='__main__':raise SystemExit(main())
