"""Check every expected regular-session bar, including overnight boundaries."""
import datetime as dt
from zoneinfo import ZoneInfo

NY=ZoneInfo('America/New_York')

def validate_continuity(rows,anchor,session_bounds):
    times={dt.datetime.fromisoformat(row[0]).timestamp() for row in rows}
    first=dt.datetime.fromisoformat(anchor)
    last=dt.datetime.fromisoformat(rows[-1][0])
    if first.timestamp() not in times:
        raise ValueError('운영 기준 봉 누락: 계좌 보존')
    if last<first:
        raise ValueError('운영 기준보다 오래된 데이터: 계좌 보존')
    day=first.astimezone(NY).date()
    end_day=last.astimezone(NY).date()
    while day<=end_day:
        bounds=session_bounds(day)
        if bounds:
            opening,closing=bounds
            stamp=opening
            while stamp+900<=closing and stamp<=last.timestamp():
                if stamp>=first.timestamp() and stamp not in times:
                    missing=dt.datetime.fromtimestamp(stamp,dt.timezone.utc).isoformat()
                    raise ValueError('거래일 경계 포함 정규장 봉 누락: '+missing+'; 계좌 보존')
                stamp+=900
        day+=dt.timedelta(days=1)
