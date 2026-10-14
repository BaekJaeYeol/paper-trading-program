"""Keep accepted historical bars immutable; report small provider revisions."""
import json
from pathlib import Path

def reconcile_bars(previous, incoming, max_revision=.005, protected_since=None):
    saved={row[0]:row for row in previous}
    result=[];revisions=[]
    for row in incoming:
        old=saved.get(row[0])
        if old is not None and list(old)!=list(row):
            change=max(abs(row[i]/old[i]-1) for i in (1,2,3,4))
            if change>max_revision and (protected_since is None or row[0]>=protected_since):
                raise ValueError(f'과거 봉 큰 가격 수정: {row[0]} 최대 {change:.2%}; 계좌 보존')
            revisions.append(dict(bar=row[0],stored_close=old[4],received_close=row[4],max_price_change=change,volume_changed=old[5]!=row[5],action='기존 확정 봉 유지'))
        result.append(tuple(old) if old is not None else tuple(row))
    return result,revisions
