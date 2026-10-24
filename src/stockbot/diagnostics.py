"""Aggregate, allowlisted paper diagnostics; no IDs, symbols, raw values or logs."""
import json
import os
import tempfile
from datetime import datetime
from zoneinfo import ZoneInfo
from .review_cases import GUIDANCE

def count(value):
    return value if type(value) is int and 0<=value<=1000000000 else None

def build(snapshot,*,age_seconds,read_failed,stopped,running):
    age=count(age_seconds)
    reconciliation=snapshot.get('reconciliation',{})
    inventory=snapshot.get('inventory',{})
    cases=snapshot.get('review',{}).get('cases',[])
    reasons=[]
    for code,(title,action) in GUIDANCE.items():
        matches=[c for c in cases if c.get('code')==code]
        if matches:reasons.append({'code':code,'title':title,'active_in_displayed_cases':sum(c.get('active') is True for c in matches),'displayed_cases':len(matches),'next_action':action})
    return {'schema':'paper-diagnostics-v1','generated_at':datetime.now(ZoneInfo('Asia/Seoul')).isoformat(),
            'scope':'cached_paper_reconciliation_aggregates','live_orders_enabled':False,
            'read_failed_since_snapshot':bool(read_failed),'snapshot_age_seconds':age,
            'stale':bool(read_failed) or age is None or age>=60,
            'stop_requested':bool(stopped),'automatic_paper_running':bool(running),
            'reconciliation':{k:count(reconciliation.get(k)) for k in ('checked','unresolved','legacy','elapsed_seconds')},
            'inventory':{'ready_at_snapshot':inventory.get('ready') is True,'displayed_symbols':len(inventory.get('rows',[])),
                         'mismatched_displayed_symbols':sum(r.get('matched') is not True for r in inventory.get('rows',[]))},
            'review':{'active_total':count(snapshot.get('review',{}).get('blocking')),'display_limit':200,'reasons':reasons},
            'limitations':['상세 목록은 최대 200건이며 전체 주문 수가 아닙니다.',
                          '캐시된 모의계좌 진단 요약입니다. 실시간 주문 승인이나 재개 근거가 아닙니다.',
                          'API 키·계좌·주문 ID·종목·금액·원문·로그·파일 경로는 포함하지 않습니다.']}

def write_report(path,report):
    """Atomic JSON replacement; caller chooses a report-only destination."""
    path=os.fspath(path);parent=os.path.dirname(os.path.abspath(path))
    temporary=None
    try:
        with tempfile.NamedTemporaryFile(mode='w',encoding='utf-8',dir=parent,prefix='.paper-report-',suffix='.tmp',delete=False) as f:
            temporary=f.name
            json.dump(report,f,ensure_ascii=False,indent=2,allow_nan=False)
            f.write('\n');f.flush();os.fsync(f.fileno())
        os.replace(temporary,path);temporary=None
    finally:
        if temporary is not None:os.unlink(temporary)
