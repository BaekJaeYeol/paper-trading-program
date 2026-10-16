"""Twenty fixed, long/cash research rules using completed OHLCV bars only.

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
MORE_NAMES = ('adx_14_trend', 'aroon_25_trend', 'cci_20_momentum',
              'williams_14_recovery', 'cmf_20_accumulation', 'chaikin_3_10',
              'roc_10_momentum', 'trix_15_trend', 'keltner_20_breakout',
              'opening_range_30m')
NAMES += MORE_NAMES


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
    middle = ema(close, 20)
    first_ema = ema(close, 15)
    second_ema = [None]*14+ema(first_ema[14:],15) if len(rows)>=15 else [None]*len(rows)
    third_ema = [None]*28+ema(second_ema[28:],15) if len(rows)>=29 else [None]*len(rows)
    flows, adl = [], []
    for row in rows:
        flow=(2*row[4]-row[2]-row[3])/(row[2]-row[3])*row[5] if row[2]>row[3] else 0.
        flows.append(flow)
        adl.append((adl[-1] if adl else 0.)+flow)
    adl_fast, adl_slow = ema(adl,3), ema(adl,10)
    macd = [fast[i]-slow[i] if slow[i] is not None else None for i in range(len(rows))]
    macd_signal = [None]*25 + ema(macd[25:], 9) if len(rows) >= 26 else [None]*len(rows)
    gains, losses, tr, positive, negative, obv = [], [], [], [], [], []
    rsi, mfi, atr, kvalues = [], [], [], []
    gain_avg = loss_avg = atr_avg = None
    plus_dm, minus_dm, dx = [], [], []
    plus_avg = minus_avg = adx = None
    opening_rows = []
    session = None
    weighted = volume = 0.
    for i, row in enumerate(rows):
        stamp, opening, high, low, c, v = row
        local = dt.datetime.fromisoformat(stamp).astimezone(NY)
        day = local.date()
        if day != session:
            session, weighted, volume = day, 0., 0.
            opening_rows = []
        minute=local.hour*60+local.minute
        if minute in (570,585):
            opening_rows.append((minute,high))
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

        up=high-rows[i-1][2] if i else 0.
        down=rows[i-1][3]-low if i else 0.
        plus_dm.append(up if up>down and up>0 else 0.)
        minus_dm.append(down if down>up and down>0 else 0.)
        if i==14:
            plus_avg=statistics.mean(plus_dm[1:15])
            minus_avg=statistics.mean(minus_dm[1:15])
        elif i>14:
            plus_avg=(plus_avg*13+plus_dm[i])/14
            minus_avg=(minus_avg*13+minus_dm[i])/14
        plus_di=100*plus_avg/atr_avg if i>=14 and atr_avg>0 else 0.
        minus_di=100*minus_avg/atr_avg if i>=14 and atr_avg>0 else 0.
        dx.append(100*abs(plus_di-minus_di)/(plus_di+minus_di) if plus_di+minus_di>0 else 0.)
        if i==27:
            adx=statistics.mean(dx[14:28])
        elif i>27:
            adx=(adx*13+dx[i])/14
        add('adx_14_trend', i>=27 and adx>=25 and plus_di>minus_di,
            'Wilder ADX14 >= 25 그리고 +DI14 > -DI14',
            {'ADX14':adx,'plus_DI14':plus_di,'minus_DI14':minus_di}, i>=27 and atr_avg>0)

        aroon_up=aroon_down=None
        if i>=25:
            window=rows[i-25:i+1]
            hi_index=max(range(26),key=lambda j:(window[j][2],j))
            lo_index=min(range(26),key=lambda j:(window[j][3],-j))
            aroon_up=100*hi_index/25
            aroon_down=100*lo_index/25
        add('aroon_25_trend', i>=25 and aroon_up>70 and aroon_down<30,
            'Aroon25 Up > 70 그리고 Down < 30 (동률이면 최신 극값)',
            {'Aroon_up':aroon_up,'Aroon_down':aroon_down},i>=25)

        typical_window=[sum(r[j] for j in (2,3,4))/3 for r in rows[max(0,i-19):i+1]]
        typical_mean=statistics.mean(typical_window)
        deviation=statistics.mean(abs(p-typical_mean) for p in typical_window)
        cci=(typical-typical_mean)/(.015*deviation) if deviation>0 else None
        add('cci_20_momentum',cci is not None and cci>100,
            'CCI20 > 100 (전형가격·평균절대편차)',{'CCI20':cci},i>=19 and deviation>0)

        williams=kval-100 if kval is not None else None
        prior_williams=prev_k-100 if prev_k is not None else None
        add('williams_14_recovery',williams is not None and prior_williams is not None and prior_williams< -80<=williams,
            '직전 Williams %R14 < -80, 현재 >= -80 (한 봉 목표)',
            {'Williams_R14':williams,'previous_R14':prior_williams},i>=14 and williams is not None and prior_williams is not None)

        recent_volume=sum(r[5] for r in rows[max(0,i-19):i+1])
        cmf=sum(flows[max(0,i-19):i+1])/recent_volume if recent_volume>0 else None
        add('cmf_20_accumulation',cmf is not None and cmf>.1,
            'Chaikin Money Flow20 > 0.1',{'CMF20':cmf,'volume20':recent_volume},i>=19 and recent_volume>0)
        chaikin=adl_fast[i]-adl_slow[i] if adl_slow[i] is not None else None
        add('chaikin_3_10',i>=25 and chaikin>0 and c>slow[i],
            'ADL의 EMA3 - EMA10 > 0 그리고 종가 > EMA26',
            {'Chaikin3_10':chaikin,'ADL':adl[i],'close':c,'EMA26':slow[i]},i>=25 and recent_volume>0)

        roc=100*(c/close[i-10]-1) if i>=10 else None
        add('roc_10_momentum',i>=25 and roc>1 and c>slow[i],
            '10봉 ROC > 1% 그리고 종가 > EMA26',{'ROC10_percent':roc,'close':c,'EMA26':slow[i]},i>=25)
        trix=100*(third_ema[i]/third_ema[i-1]-1) if i>=43 else None
        add('trix_15_trend',i>=43 and trix>0 and c>slow[i],
            '15봉 삼중 EMA의 1봉 변화율 TRIX > 0 그리고 종가 > EMA26',
            {'TRIX15_percent':trix,'close':c,'EMA26':slow[i]},i>=43)

        upper=middle[i]+2*atr_avg if i>=19 else None
        add('keltner_20_breakout',upper is not None and c>upper,
            '종가 > EMA20 + 2 x Wilder ATR14',
            {'close':c,'upper_Keltner':upper,'EMA20':middle[i],'ATR14':atr_avg},i>=19 and atr_avg>0)
        complete_opening=[entry[0] for entry in opening_rows]==[570,585]
        opening_high=max(entry[1] for entry in opening_rows) if complete_opening else None
        add('opening_range_30m',complete_opening and 600<=minute<960 and c>opening_high,
            '뉴욕 09:30·09:45 두 완료 봉 최고가를 10:00 이후 종가가 돌파',
            {'close':c,'opening_high':opening_high},complete_opening and 600<=minute<960)
    return signals, evidence
