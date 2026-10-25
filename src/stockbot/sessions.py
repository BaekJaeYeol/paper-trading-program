"""Calendar/clock-based session diagnostics. Brackets remain regular-hours only."""
from datetime import date,datetime,time,timedelta
from zoneinfo import ZoneInfo
NY=ZoneInfo('America/New_York');KST=ZoneInfo('Asia/Seoul')
LABELS={'regular':'정규장','pre':'프리마켓','post':'애프터마켓','overnight_unverified':'야간 가능 시간 · 권한 미검증','closed':'휴장·주말 대기','early_close_wait':'조기폐장 후 · 시간외 시간 미검증','clock_mismatch':'시장 시계 불일치 · 주문 차단'}

def describe(clock,calendar):
    now=datetime.fromisoformat(clock['timestamp'].replace('Z','+00:00'))
    if now.tzinfo is None:raise ValueError('Timezone required for session clock')
    now=now.astimezone(NY);today=now.date();sessions={}
    for row in calendar:
        day=date.fromisoformat(row['date'])
        if day in sessions:raise ValueError('Duplicate calendar session')
        opening=time.fromisoformat(row['open']);closing=time.fromisoformat(row['close'])
        if opening.tzinfo is not None or closing.tzinfo is not None:raise ValueError('Calendar hours must be local')
        if opening>=closing:raise ValueError('Invalid calendar hours')
        sessions[day]=(datetime.combine(day,opening,NY),datetime.combine(day,closing,NY))
    current=sessions.get(today);code='closed'
    regular=clock.get('is_open') is True
    if regular:
        code='regular' if current and current[0]<=now<current[1] else 'clock_mismatch'
    elif current and current[0]<=now<current[1]:code='clock_mismatch'
    elif current and time(4)<=now.time()<current[0].time():code='pre'
    elif current and current[1]<=now and now.time()<time(20):code='post' if current[1].time()==time(16) else 'early_close_wait'
    elif (now.time()>=time(20) and today+timedelta(days=1) in sessions) or (now.time()<time(4) and current):code='overnight_unverified'
    future=[o for o,c in sessions.values() if o>now]
    return {'code':code,'label':LABELS[code],'new_orders_allowed':code=='regular',
            'reason':'regular_bracket_only' if code=='regular' else 'extended_bracket_unsupported' if code in ('pre','post') else 'session_or_permissions_unverified' if code in ('overnight_unverified','early_close_wait','clock_mismatch') else 'market_closed',
            'observed_ny':now.isoformat(),'next_regular_open_kst':min(future).astimezone(KST).isoformat() if future else None,
            'poll_seconds':300 if code=='regular' else 60,'extended_orders_enabled':False}
