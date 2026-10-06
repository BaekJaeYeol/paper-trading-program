"""Durable execution coordinator. Broker adapters must satisfy this contract.

Not wired to the legacy Alpaca CLI or to Toss live accounts yet.
"""
from contextlib import closing
from dataclasses import dataclass
from decimal import Decimal
import json
from pathlib import Path
import sqlite3
from typing import Protocol

TERMINAL = {'filled', 'canceled', 'rejected', 'expired'}
STATES = TERMINAL | {'accepted', 'partially_filled', 'pending_cancel'}

@dataclass(frozen=True)
class Order:
    client_id: str
    broker_id: str
    symbol: str
    quantity: Decimal
    filled: Decimal
    status: str

    def validate(self):
        if not self.client_id or not self.broker_id or not self.symbol:
            raise ValueError('Missing order identity')
        if not self.quantity.is_finite() or not self.filled.is_finite():
            raise ValueError('Non-finite quantity')
        if not 0 <= self.filled <= self.quantity or self.quantity <= 0:
            raise ValueError('Invalid filled quantity')
        if self.status not in STATES:
            raise ValueError('Unsupported broker status')
        if self.status == 'filled' and self.filled != self.quantity:
            raise ValueError('Filled order has remaining quantity')

class Broker(Protocol):
    def find_order(self, client_id: str) -> Order | None: ...
    def submit(self, request: dict, client_id: str) -> Order: ...
    def account_snapshot(self) -> dict: ...
    def cancel(self, broker_id: str) -> None: ...

class Coordinator:
    def __init__(self, directory, broker: Broker):
        self.root = Path(directory)
        self.root.mkdir(parents=True, exist_ok=True)
        self.broker = broker
        self.ready = False
        with self.connect() as db:
            db.executescript('''
                CREATE TABLE IF NOT EXISTS intents (
                    client_id TEXT PRIMARY KEY, payload TEXT NOT NULL,
                    state TEXT NOT NULL, broker_id TEXT,
                    filled TEXT NOT NULL DEFAULT '0');
                CREATE TABLE IF NOT EXISTS snapshots (
                    id INTEGER PRIMARY KEY AUTOINCREMENT, payload TEXT NOT NULL);
            ''')

    def connect(self):
        # SQLite context managers commit/rollback but do NOT close connections.
        return closing(sqlite3.connect(self.root/'execution.sqlite', timeout=30))

    def intent(self, client_id):
        with self.connect() as db:
            return db.execute('SELECT payload,state,broker_id,filled FROM intents WHERE client_id=?', (client_id,)).fetchone()

    def record(self, order):
        order.validate()
        with self.connect() as db:
            db.execute('BEGIN IMMEDIATE')
            row = db.execute('SELECT payload,filled,broker_id,state FROM intents WHERE client_id=?', (order.client_id,)).fetchone()
            if row is None:
                raise ValueError('Unknown local order')
            payload = json.loads(row[0])
            if order.symbol != payload['symbol'] or order.quantity != Decimal(str(payload['qty'])):
                raise ValueError('Broker/local order mismatch')
            if row[2] is not None and row[2] != order.broker_id:
                raise ValueError('Broker identity changed')
            if order.filled < Decimal(row[1]):
                raise ValueError('Cumulative fills decreased; reconciliation required')
            if row[3] in TERMINAL and order.status != row[3]:
                raise ValueError('Terminal order changed; reconciliation required')
            db.execute('UPDATE intents SET state=?,broker_id=?,filled=? WHERE client_id=?',
                       (order.status,order.broker_id,str(order.filled),order.client_id))
            db.commit()

    def synchronize(self):
        """Read broker positions/balance authoritatively; never derive them from intents."""
        self.ready = False
        with self.connect() as db:
            ids = [r[0] for r in db.execute('SELECT client_id FROM intents WHERE state NOT IN (?,?,?,?)', tuple(sorted(TERMINAL)))]
        unresolved = []
        for cid in ids:
            order = self.broker.find_order(cid)
            if order is None:
                # Absence is NOT proof that a timed-out submission never reached broker.
                unresolved.append(cid)
            else:
                self.record(order)
        snapshot = self.broker.account_snapshot()
        if not snapshot.get('complete') or not isinstance(snapshot.get('positions'),list) or not isinstance(snapshot.get('open_orders'),list):
            raise ValueError('Incomplete broker snapshot')
        if not snapshot.get('account_id') or not snapshot.get('as_of'):
            raise ValueError('Snapshot missing identity/time')
        # Adapter must validate freshness, pagination, currency and balances.
        with self.connect() as db:
            db.execute('INSERT INTO snapshots(payload) VALUES (?)',(json.dumps(snapshot),))
            db.commit()
        self.ready = not unresolved and not (self.root/'STOP').exists()
        return {'ready':self.ready,'unresolved':unresolved,'snapshot':snapshot}

    def submit(self, client_id, request):
        if not self.ready or (self.root/'STOP').exists():
            raise RuntimeError('Synchronize successfully and clear STOP before entry')
        payload = json.dumps(request,sort_keys=True)
        quantity = Decimal(str(request['qty']))
        if not request.get('symbol') or not quantity.is_finite() or quantity <= 0:
            raise ValueError('Invalid request')
        with self.connect() as db:
            db.execute('BEGIN IMMEDIATE')
            old = db.execute('SELECT payload FROM intents WHERE client_id=?',(client_id,)).fetchone()
            if old:
                if old[0] != payload:
                    raise ValueError('Client ID reused with different request')
                return self.intent(client_id)
            db.execute("INSERT INTO intents(client_id,payload,state) VALUES (?,?,'unknown')",(client_id,payload))
            db.commit()
        # One atomic intent reservation, no retry of POST even on timeout.
        try:
            order = self.broker.submit(request,client_id)
            if order.client_id != client_id:
                raise ValueError('Submission returned different client ID')
            self.record(order)
        except Exception:
            self.ready = False
            raise RuntimeError('Submission uncertain; run synchronize, never blindly resend') from None
        return self.intent(client_id)

    def halt(self, cancel_bot_orders=False):
        (self.root/'STOP').touch()
        self.ready = False
        results = []
        if cancel_bot_orders:
            with self.connect() as db:
                rows = db.execute('SELECT client_id,broker_id FROM intents WHERE state NOT IN (?,?,?,?)',tuple(sorted(TERMINAL))).fetchall()
            for cid,bid in rows:
                if not bid:
                    results.append({'client_id':cid,'status':'unknown_requires_reconcile'})
                    continue
                try:
                    self.broker.cancel(bid)
                    results.append({'client_id':cid,'status':'cancel_requested'})
                except Exception:
                    results.append({'client_id':cid,'status':'cancel_uncertain'})
        # Cancellation acknowledgement is not final cancellation. Poll to reconcile.
        return results
