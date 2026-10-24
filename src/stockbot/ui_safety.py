"""Display and resume checks for the existing paper-only engine."""
from contextlib import closing
from datetime import datetime,timezone
from decimal import Decimal
from pathlib import Path
import sqlite3

ORDER_STATES={'new':'접수','accepted':'접수','pending_new':'접수 대기','partially_filled':'부분 체결','filled':'체결 완료','pending_cancel':'취소 요청 중','canceled':'취소 완료','rejected':'거부','expired':'만료','done_for_day':'당일 종료','pending_replace':'정정 요청 중','replaced':'정정 완료','accepted_for_bidding':'접수','stopped':'중지','suspended':'일시 중지','calculated':'정산 중'}

def order_row(order):
    qty=Decimal(str(order.get('qty','')));filled=Decimal(str(order.get('filled_qty','')))
    if not qty.is_finite() or not filled.is_finite() or not 0<=filled<=qty or qty<=0:raise ValueError('Invalid order quantity')
    status=ORDER_STATES.get(order.get('status'),'미확인 · 증권사 확인 필요')
    return [order.get('symbol',''),{'buy':'매수','sell':'매도'}.get(order.get('side'),'미확인'),str(qty),str(filled),str(qty-filled),order.get('limit_price') or '—',status]

def unresolved_attempts(directory):
    path=Path(directory)/'orders.sqlite'
    if not path.exists():return []
    with closing(sqlite3.connect(path.resolve().as_uri()+'?mode=ro',uri=True,timeout=5)) as db:
        if not db.execute("SELECT 1 FROM sqlite_master WHERE type='table' AND name='attempts'").fetchone():return []
        return [r[0] for r in db.execute("SELECT id FROM attempts WHERE status IN ('pending','unknown')")]

def resume_snapshot(c,broker,reader):
    from .paper_journal import reconcile_snapshot
    data=reconcile_snapshot(c,broker,reader)
    if data['reconciliation']['unresolved']:raise RuntimeError('Unresolved orders require broker reconciliation')
    if not data.get('can_trade'):raise ValueError('Account unavailable')
    for order in data['orders']:
        order_row(order)
        if order.get('status') not in ORDER_STATES:raise ValueError('Unknown broker order status')
    return data
