"""Ten fixed, long/cash research rules using completed OHLCV bars only.

Indicators use SMA-seeded EMA and Wilder RSI/ATR. No optimization or ranking.
Recovery rules are one-bar target pulses, not latched trade instructions.
"""
import datetime as dt
import math
import statistics
from zoneinfo import ZoneInfo

NY = ZoneInfo('America/New_York')
NAMES = ('ema_12_26', 'macd_12_26_9', 'rsi_14_recovery',
         'bollinger_20_reentry', 'donchian_20', 'atr_14_breakout',
         'session_vwap', 'obv_20', 'stochastic_14_3_recovery', 'mfi_14_recovery')


def ema(values, period):
    result = [None] * len(values)
    if len(values) >= period:
        result[period-1] = statistics.mean(values[:period])
        alpha = 2 / (period+1)
        for i in range(period, len(values)):
            result[i] = alpha*values[i] + (1-alpha)*result[i-1]
    return result


def ratio_index(positive, negative):
    if positive == negative == 0:
        return 50.
    return 100. if negative == 0 else 100 - 100/(1+positive/negative)


def extended_analysis(rows):
    signals = {name: [] for name in NAMES}
    evidence = {name: [] for name in NAMES}
    if not rows:
        return signals, evidence
    close = [r[4] for r in rows]
    fast, slow = ema(close, 12), ema(close, 26)
    macd = [fast[i]-slow[i] if slow[i] is not None else None for i in range(len(rows))]
    macd_signal = [None]*25 + ema(macd[25:], 9) if len(rows) >= 26 else [None]*len(rows)
    gains, losses, tr, positive, negative, obv = [], [], [], [], [], []
    rsi, mfi, atr, kvalues = [], [], [], []
    gain_avg = loss_avg = atr_avg = None
    session = None
    weighted = volume = 0.
    for i, row in enumerate(rows):
        stamp, opening, high, low, c, v = row
        day = dt.datetime.fromisoformat(stamp).astimezone(NY).date()
        if day != session:
            session, weighted, volume = day, 0., 0.
        typical = (high+low+c)/3
        weighted += typical*v
        volume += v
        vwap = weighted/volume if volume > 0 else None
        delta = c-close[i-1] if i else 0.
        gains.append(max(delta, 0.)); losses.append(max(-delta, 0.))
        tr.append(max(high-low, abs(high-close[i-1]), abs(low-close[i-1])) if i else high-low)
        previous_typical = sum(rows[i-1][j] for j in (2, 3, 4))/3 if i else typical
        positive.append(typical*v if typical > previous_typical else 0.)
        negative.append(typical*v if typical < previous_typical else 0.)
        obv.append((obv[-1] if i else 0.) + (v if delta > 0 else -v if delta < 0 else 0.))
        if i == 14:
            gain_avg, loss_avg, atr_avg = (statistics.mean(x[1:15]) for x in (gains, losses, tr))
        elif i > 14:
            gain_avg = (gain_avg*13+gains[i])/14
            loss_avg = (loss_avg*13+losses[i])/14
            atr_avg = (atr_avg*13+tr[i])/14
        rsi.append(ratio_index(gain_avg, loss_avg) if i >= 14 else None)
        atr.append(atr_avg)
        mfi.append(ratio_index(sum(positive[i-13:i+1]), sum(negative[i-13:i+1])) if i >= 14 else None)
        highest = max(r[2] for r in rows[max(0, i-13):i+1])
        lowest = min(r[3] for r in rows[max(0, i-13):i+1])
        kvalues.append(100*(c-lowest)/(highest-lowest) if i >= 13 and highest > lowest else None)

        def add(name, condition, rule, metrics, ready):
            # Warm-up is per indicator; unavailable/degenerate inputs always wait.
            target = float(bool(condition)) if ready else 0.
            values = {key: value for key, value in metrics.items() if value is not None}
            if any(not math.isfinite(value) for value in values.values()):
                raise ValueError('지표 계산에 유한하지 않은 값이 있습니다: '+name)
            detail = ', '.join(f'{key}={value:.6g}' for key, value in values.items())
            reason = f'{rule}; '+('자료 부족·변동폭 또는 거래량 없음: 대기' if not ready else '조건 충족' if target else '조건 미충족')
            signals[name].append(target)
            evidence[name].append(dict(signal_bar=stamp, target=target, rule=rule,
                                       indicators=values, reason=reason+'; '+detail))

        add('ema_12_26', slow[i] is not None and fast[i] > slow[i],
            'EMA12 > EMA26', {'EMA12':fast[i], 'EMA26':slow[i]}, i >= 25)
        add('macd_12_26_9', macd_signal[i] is not None and macd[i] > macd_signal[i] and macd[i] > 0,
            'MACD > 신호선 그리고 MACD > 0', {'MACD':macd[i], 'signal9':macd_signal[i]}, i >= 33)
        add('rsi_14_recovery', i >= 15 and rsi[i-1] < 30 <= rsi[i],
            '직전 RSI14 < 30, 현재 RSI14 >= 30 (한 봉 목표)',
            {'RSI14':rsi[i], 'previous_RSI14':rsi[i-1] if i else None}, i >= 15 and gain_avg+loss_avg > 0)
        mean = statistics.mean(close[max(0, i-19):i+1])
        sd = statistics.pstdev(close[max(0, i-19):i+1])
        lower = mean-2*sd
        previous_lower = statistics.mean(close[i-20:i])-2*statistics.pstdev(close[i-20:i]) if i >= 20 else None
        add('bollinger_20_reentry', i >= 20 and close[i-1] < previous_lower and lower <= c <= mean,
            '직전 종가 < 직전 하단밴드, 현재 하단밴드 <= 종가 <= SMA20 (한 봉 목표)',
            {'close':c, 'lower20':lower, 'SMA20':mean, 'previous_lower20':previous_lower}, i >= 20 and sd > 0)
        prior_high = max(r[2] for r in rows[max(0, i-20):i]) if i else None
        add('donchian_20', i >= 20 and c > prior_high,
            '종가 > 현재 봉을 제외한 직전 20봉 최고가', {'close':c, 'prior_high20':prior_high}, i >= 20)
        prior_atr = atr[i-1] if i else None
        threshold = close[i-1]+prior_atr if prior_atr is not None else None
        add('atr_14_breakout', i >= 25 and c > threshold and c > slow[i],
            '종가 > 직전 종가 + 직전 ATR14 그리고 종가 > EMA26',
            {'close':c, 'threshold':threshold, 'prior_ATR14':prior_atr, 'EMA26':slow[i]}, i >= 25 and prior_atr > 0)
        add('session_vwap', vwap is not None and c > vwap,
            '종가 > 뉴욕 거래일별 누적 전형가격 VWAP', {'close':c, 'session_VWAP':vwap, 'session_volume':volume}, volume > 0)
        obv_mean = statistics.mean(obv[max(0, i-19):i+1])
        add('obv_20', i >= 25 and obv[i] > obv_mean and c > slow[i],
            'OBV > OBV의 SMA20 그리고 종가 > EMA26',
            {'OBV':obv[i], 'OBV_SMA20':obv_mean, 'close':c, 'EMA26':slow[i]}, i >= 25 and sum(r[5] for r in rows[i-19:i+1]) > 0)
        kval = kvalues[i]
        prev_k = kvalues[i-1] if i else None
        dval = statistics.mean(kvalues[i-2:i+1]) if i >= 15 and all(x is not None for x in kvalues[i-2:i+1]) else None
        prev_d = statistics.mean(kvalues[i-3:i]) if i >= 16 and all(x is not None for x in kvalues[i-3:i]) else None
        ready = all(x is not None for x in (kval, prev_k, dval, prev_d))
        add('stochastic_14_3_recovery', ready and prev_k < 20 and prev_k <= prev_d and kval > dval,
            '직전 %K14 < 20에서 %K14가 %D3 상향 돌파 (한 봉 목표)',
            {'K14':kval, 'D3':dval, 'previous_K14':prev_k, 'previous_D3':prev_d}, ready)
        add('mfi_14_recovery', i >= 15 and mfi[i-1] < 20 <= mfi[i],
            '직전 MFI14 < 20, 현재 MFI14 >= 20 (한 봉 목표)',
            {'MFI14':mfi[i], 'previous_MFI14':mfi[i-1] if i else None}, i >= 15 and sum(positive[i-13:i+1])+sum(negative[i-13:i+1]) > 0)
    return signals, evidence
