"""Read-only, single manual candidate budget estimate. No executable payload."""
from datetime import datetime, timezone, date
from decimal import Decimal, InvalidOperation, ROUND_CEILING
import re
import time
from zoneinfo import ZoneInfo

BUDGET_KRW = Decimal('10000')
FX_BUFFER = Decimal('0.01')


class PreviewBlocked(ValueError):
    pass


def number(value, *, zero=False):
    if not isinstance(value, str) or not re.fullmatch(r'\d{1,16}(?:\.\d{1,12})?', value):
        raise PreviewBlocked('금액·수량 응답 형식이 올바르지 않습니다.')
    try:
        result = Decimal(value)
    except InvalidOperation:
        raise PreviewBlocked('숫자 입력을 확인하세요.') from None
    if not result.is_finite() or result < 0 or (not zero and result == 0):
        raise PreviewBlocked('금액·수량은 유효한 양수여야 합니다.')
    return result


def inputs(symbol, price, quantity):
    symbol = symbol.strip().upper()
    if not re.fullmatch(r'[A-Z][A-Z0-9.\-]{0,14}', symbol):
        raise PreviewBlocked('미국 주식 티커 한 개를 입력하세요.')
    price, quantity = number(price), number(quantity)
    if price < 1 or price != price.quantize(Decimal('.01')):
        raise PreviewBlocked('이번 미리보기는 1달러 이상, 소수 둘째 자리까지의 지정가만 지원합니다.')
    if quantity != quantity.to_integral_value() or quantity > 10000:
        raise PreviewBlocked('이번 미리보기는 정수 수량 1~10000주만 지원합니다.')
    return symbol, price, quantity


def timestamp(value):
    try:
        result = datetime.fromisoformat(value)
        if result.tzinfo is None:
            raise ValueError()
        return result
    except (TypeError, ValueError):
        raise PreviewBlocked('응답 시각을 확인할 수 없습니다.') from None


def only_symbol(items, symbol):
    if not isinstance(items, list) or len(items) != 1 or items[0].get('symbol') != symbol:
        raise PreviewBlocked('조회 종목이 일치하지 않습니다.')
    return items[0]


def clear_account(snapshot, symbol):
    if snapshot.get('complete') is not True:
        raise PreviewBlocked('불완전한 계좌 조회입니다.')
    if snapshot['open_orders']:
        raise PreviewBlocked('일반 미체결 주문이 있어 예산 미리보기를 차단했습니다. 자동 취소하지 않습니다.')
    for item in snapshot['positions']:
        # Fail closed for missing identity, including holdings unrelated to candidate.
        if not isinstance(item['symbol'], str):
            raise PreviewBlocked('보유종목 확인 실패')
        if item['symbol'].upper() == symbol:
            raise PreviewBlocked('기존 보유종목은 매수 미리보기 대상에서 제외합니다.')


def preview(broker, symbol, price, quantity, *, now=None, monotonic=time.monotonic):
    symbol, price, quantity = inputs(symbol, price, quantity)
    started = monotonic()
    clock = now or (lambda: datetime.now(timezone.utc))

    def check():
        if monotonic() - started > 30:
            raise PreviewBlocked('조회 시간이 30초를 넘어 결과를 폐기했습니다. 다시 조회하세요.')

    def get(path, params=None):
        check()
        result = broker.get(path, params)
        check()
        return result

    def conditions():
        value = get('/api/v1/conditional-orders', {'status': 'OPEN', 'limit': 100})
        if value['hasNext'] is not False or value['nextCursor'] is not None or value['conditionalOrders']:
            raise PreviewBlocked('진행 중 조건주문 또는 불완전한 목록이 있어 차단했습니다. 자동 취소하지 않습니다.')

    check()
    first = broker.account_snapshot()
    check()
    clear_account(first, symbol)
    conditions()
    stock = only_symbol(get('/api/v1/stocks', {'symbols': symbol}), symbol)
    if (stock['currency'] != 'USD' or stock['market'] not in {'NYSE', 'NASDAQ', 'AMEX'}
            or stock['status'] != 'ACTIVE' or stock['securityType'] != 'STOCK'
            or stock['isCommonShare'] is not True):
        raise PreviewBlocked('이번 미리보기는 미국 주요 거래소의 활성 보통주만 지원합니다.')
    quote = only_symbol(get('/api/v1/prices', {'symbols': symbol}), symbol)
    if quote['currency'] != 'USD':
        raise PreviewBlocked('시세 통화 불일치')
    last = number(quote['lastPrice'])
    fx = get('/api/v1/exchange-rate', {'baseCurrency': 'USD', 'quoteCurrency': 'KRW'})
    if fx['baseCurrency'] != 'USD' or fx['quoteCurrency'] != 'KRW':
        raise PreviewBlocked('환율 통화 불일치')
    rate = number(fx['rate'])
    fees = get('/api/v1/commissions')
    cash = get('/api/v1/buying-power', {'currency': 'USD'})
    if cash['currency'] != 'USD':
        raise PreviewBlocked('매수 가능 금액 통화 불일치')
    available = number(cash['cashBuyingPower'], zero=True)
    # Re-read account and conditional orders to detect changes during the estimate.
    second = broker.account_snapshot()
    check()
    if second['account_id'] != first['account_id']:
        raise PreviewBlocked('조회 중 계좌가 변경되었습니다.')
    clear_account(second, symbol)
    conditions()
    moment = clock()
    age = (moment - timestamp(quote['timestamp'])).total_seconds()
    if not 0 <= age <= 60:
        raise PreviewBlocked('현재가가 60초 이상 지연되었거나 미래 시각입니다. 장외·휴장 시 미리보기가 차단될 수 있습니다.')
    if not timestamp(fx['validFrom']) <= moment < timestamp(fx['validUntil']):
        raise PreviewBlocked('환율 유효 시간이 지났습니다.')
    today = moment.astimezone(ZoneInfo('Asia/Seoul')).date()
    applicable = []
    for fee in fees:
        if fee['marketCountry'] != 'US':
            continue
        start = date.fromisoformat(fee['startDate']) if fee.get('startDate') else date.min
        end = date.fromisoformat(fee['endDate']) if fee.get('endDate') else date.max
        if start <= today <= end:
            applicable.append(number(fee['commissionRate'], zero=True))
    if len(applicable) != 1 or applicable[0] > Decimal('.1'):
        raise PreviewBlocked('현재 적용할 미국 주식 수수료율을 확정할 수 없습니다.')
    principal = price * quantity
    fee_usd = (principal * applicable[0]).quantize(Decimal('.01'), rounding=ROUND_CEILING)
    total_usd = principal + fee_usd
    estimate = (total_usd * rate).quantize(Decimal('1'), rounding=ROUND_CEILING)
    buffered = (total_usd * rate * (1 + FX_BUFFER)).quantize(Decimal('1'), rounding=ROUND_CEILING)
    reasons = []
    if buffered > BUDGET_KRW:
        reasons.append('환율 여유분 포함 1만 원 초과')
    if total_usd > available:
        reasons.append('달러 현금 매수 가능 금액 부족 (자동 환전 없음)')
    check()
    return {'symbol': symbol, 'price_usd': str(price), 'quantity': str(quantity),
            'last_price_usd': str(last), 'principal_usd': str(principal),
            'fee_rate': str(applicable[0]), 'fee_usd': str(fee_usd),
            'total_usd': str(total_usd), 'fx_rate': str(rate),
            'estimated_krw': str(estimate), 'buffered_krw': str(buffered),
            'budget_krw': str(BUDGET_KRW), 'within_budget': not reasons,
            'reasons': reasons, 'as_of': moment.isoformat(), 'orders_enabled': False}


def describe(result):
    state = ('예산 검사 통과 · 주문 전송 불가' if result['within_budget'] else '예산 검사 차단')
    return (f"{state}\n{result['symbol']} · 지정가 {result['price_usd']} USD × {result['quantity']}주\n"
            f"참고 현재가 {result['last_price_usd']} USD (체결 가능 호가 아님)\n"
            f"매수금액 {result['principal_usd']} USD + 수수료 추정 {result['fee_usd']} USD\n"
            f"참고 환율 {result['fx_rate']}원/USD · 원화 추정 {result['estimated_krw']}원\n"
            f"환율 여유 1% 포함 {result['buffered_krw']}원 / 한도 10,000원\n"
            + (' · '.join(result['reasons']) + '\n' if result['reasons'] else '')
            + '단일 수동 후보의 매수 비용 추정입니다. 자동 선정·예산 예약·환전·주문은 하지 않습니다.\n'
              '수수료 할인/면제는 보수적으로 미반영하며 매도 비용·세금은 별도입니다.\n'
              '환율은 참고용이며 실제 비용을 보장하지 않습니다. 거래정지·세션·호가·주문 자격은 미검증입니다.')
