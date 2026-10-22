# 모의투자 운영 현황

[PC·서버 장애 진단과 복구 방법](https://github.com/BaekJaeYeol/paper-trading-program/blob/main/investment-lab/docs/failure-recovery.md)

이번 실행 복구: {}

완료 봉 확인 주기: 기록 9/17회 · 기록 없는 예정 8회 · 아직 판정 전 9회 · 주의: 예약 시작 지연 또는 실행·저장 누락을 확인하세요.

[주기 판정 기준](https://github.com/BaekJaeYeol/paper-trading-program/blob/main/investment-lab/docs/session-coverage.md)

최근 확인: 2026-10-22T18:07:00.571850+00:00 (UTC)
다음 15분 확인 목표 (세션 실행 중에만 적용): 2026-10-22T18:22:00+00:00 (UTC, 실행 지연 가능)

실제 주문 없음. v1 기존 계좌와 v2 새 계좌의 시작일이 다르므로 수익률을 직접 우열 비교하지 마세요.
v2는 다음 봉 시가에 비용·스프레드·직전 거래량 제한을 적용한 가상 체결입니다. 미체결 잔량은 만료됩니다.

| 종목 | 상태 | 최근 성공 UTC | 마지막 완료 봉 UTC | 이번 새 봉 |
|---|---|---|---|---|
| SPY | updated | 2026-10-22T18:07:00.571850+00:00 | 2026-10-22T17:45:00+00:00 | 1 |
| QQQ | updated | 2026-10-22T18:07:00.571850+00:00 | 2026-10-22T17:45:00+00:00 | 1 |
| IWM | updated | 2026-10-22T18:07:00.571850+00:00 | 2026-10-22T17:45:00+00:00 | 1 |
| DIA | updated | 2026-10-22T18:07:00.571850+00:00 | 2026-10-22T17:45:00+00:00 | 1 |
| MSFT | updated | 2026-10-22T18:07:00.571850+00:00 | 2026-10-22T17:45:00+00:00 | 1 |
| JPM | updated | 2026-10-22T18:07:00.571850+00:00 | 2026-10-22T17:45:00+00:00 | 1 |
| XOM | updated | 2026-10-22T18:07:00.571850+00:00 | 2026-10-22T17:45:00+00:00 | 1 |
| JNJ | updated | 2026-10-22T18:07:00.571850+00:00 | 2026-10-22T17:45:00+00:00 | 1 |
| CAT | updated | 2026-10-22T18:07:00.571850+00:00 | 2026-10-22T17:45:00+00:00 | 1 |
| WMT | updated | 2026-10-22T18:07:00.571850+00:00 | 2026-10-22T17:45:00+00:00 | 1 |

이번 실행 소요: 38.23초
[최근 200회 운영·복구 이력](operations-history.json)

| 종목 | 연속 오류 | 복구 |
|---|---:|---|
| SPY | 0 | - |
| QQQ | 0 | - |
| IWM | 0 | - |
| DIA | 0 | - |
| MSFT | 0 | - |
| JPM | 0 | - |
| XOM | 0 | - |
| JNJ | 0 | - |
| CAT | 0 | - |
| WMT | 0 | - |

[공정 비교·복구 검증 설명](https://github.com/BaekJaeYeol/paper-trading-program/blob/main/investment-lab/docs/comparison-orders.md)

v2 신규 주문 제한: 일중 손실 3%, 최고 평가액 대비 낙폭 10%. 중단은 지속되며 자동 청산하지 않습니다. v1은 원래 비교용 계좌로 유지합니다.

## SPY 계좌

| 모델 | 전략 | 평가액 USD | 손익 USD | 최근 매매·이유 |
|---|---|---:|---:|---|
| v1 | cash | 10000.00 | 0.00 | 대기 /  / 새 신호 대기 |
| v1 | buy_hold | 9844.38 | -155.62 | buy /  / buy_hold: prior completed bar target 100%; next bar open simulation |
| v1 | trend_8_26 | 9711.09 | -288.91 | sell /  / trend_8_26: prior completed bar target 0%; next bar open simulation |
| v1 | momentum_26 | 9631.54 | -368.46 | sell /  / momentum_26: prior completed bar target 0%; next bar open simulation |
| v1 | breakout_8 | 9503.28 | -496.72 | sell /  / breakout_8: prior completed bar target 0%; next bar open simulation |
| v1 | reversion_12 | 9619.35 | -380.65 | sell /  / reversion_12: prior completed bar target 0%; next bar open simulation |
| v1 | volume_26 | 9438.20 | -561.80 | sell /  / volume_26: prior completed bar target 0%; next bar open simulation |
| v1 | trend_8_26 AND momentum_26 | 9624.28 | -375.72 | sell /  / trend_8_26 AND momentum_26: prior completed bar target 0%; next bar open simulation |
| v1 | trend_8_26 + momentum_26 | 9671.22 | -328.78 | sell /  / trend_8_26 + momentum_26: prior completed bar target 0%; next bar open simulation |
| v1 | trend_8_26 AND breakout_8 | 9730.71 | -269.29 | sell /  / trend_8_26 AND breakout_8: prior completed bar target 0%; next bar open simulation |
| v1 | trend_8_26 + breakout_8 | 9645.08 | -354.92 | sell /  / trend_8_26 + breakout_8: prior completed bar target 0%; next bar open simulation |
| v1 | trend_8_26 AND reversion_12 | 9736.23 | -263.77 | sell /  / trend_8_26 AND reversion_12: prior completed bar target 0%; next bar open simulation |
| v1 | trend_8_26 + reversion_12 | 9664.97 | -335.03 | sell /  / trend_8_26 + reversion_12: prior completed bar target 0%; next bar open simulation |
| v1 | trend_8_26 AND volume_26 | 9605.36 | -394.64 | sell /  / trend_8_26 AND volume_26: prior completed bar target 0%; next bar open simulation |
| v1 | trend_8_26 + volume_26 | 9573.57 | -426.43 | sell /  / trend_8_26 + volume_26: prior completed bar target 0%; next bar open simulation |
| v1 | momentum_26 AND breakout_8 | 9640.01 | -359.99 | sell /  / momentum_26 AND breakout_8: prior completed bar target 0%; next bar open simulation |
| v1 | momentum_26 + breakout_8 | 9567.24 | -432.76 | sell /  / momentum_26 + breakout_8: prior completed bar target 0%; next bar open simulation |
| v1 | momentum_26 AND reversion_12 | 9769.70 | -230.30 | sell /  / momentum_26 AND reversion_12: prior completed bar target 0%; next bar open simulation |
| v1 | momentum_26 + reversion_12 | 9683.27 | -316.73 | sell /  / momentum_26 + reversion_12: prior completed bar target 0%; next bar open simulation |
| v1 | momentum_26 AND volume_26 | 9618.73 | -381.27 | sell /  / momentum_26 AND volume_26: prior completed bar target 0%; next bar open simulation |
| v1 | momentum_26 + volume_26 | 9534.28 | -465.72 | sell /  / momentum_26 + volume_26: prior completed bar target 0%; next bar open simulation |
| v1 | breakout_8 AND reversion_12 | 10000.00 | 0.00 | 대기 /  / 새 신호 대기 |
| v1 | breakout_8 + reversion_12 | 9560.78 | -439.22 | sell /  / breakout_8 + reversion_12: prior completed bar target 0%; next bar open simulation |
| v1 | breakout_8 AND volume_26 | 9837.59 | -162.41 | sell /  / breakout_8 AND volume_26: prior completed bar target 0%; next bar open simulation |
| v1 | breakout_8 + volume_26 | 9508.37 | -491.63 | sell /  / breakout_8 + volume_26: prior completed bar target 0%; next bar open simulation |
| v1 | reversion_12 AND volume_26 | 9811.81 | -188.19 | sell /  / reversion_12 AND volume_26: prior completed bar target 0%; next bar open simulation |
| v1 | reversion_12 + volume_26 | 9547.19 | -452.81 | sell /  / reversion_12 + volume_26: prior completed bar target 0%; next bar open simulation |
| v1 | ema_12_26 | 9742.51 | -257.49 | sell /  / EMA12 > EMA26; 조건 미충족; EMA12=771.277, EMA26=771.539 |
| v1 | macd_12_26_9 | 9769.55 | -230.45 | sell /  / MACD > 신호선 그리고 MACD > 0; 조건 미충족; MACD=1.03945, signal9=1.12358 |
| v1 | rsi_14_recovery | 9805.98 | -194.02 | sell /  / 직전 RSI14 < 30, 현재 RSI14 >= 30 (한 봉 목표); 조건 미충족; RSI14=38.7389, previous_RSI14=37.2051 |
| v1 | bollinger_20_reentry | 9787.44 | -212.56 | sell /  / 직전 종가 < 직전 하단밴드, 현재 하단밴드 <= 종가 <= SMA20 (한 봉 목표); 조건 미충족; close=762.71, lower20=761.42, SMA20=770.302, previous_lower20=762.585 |
| v1 | donchian_20 | 9818.08 | -181.92 | sell /  / 종가 > 현재 봉을 제외한 직전 20봉 최고가; 조건 미충족; close=774.19, prior_high20=774.44 |
| v1 | atr_14_breakout | 9816.89 | -183.11 | sell /  / 종가 > 직전 종가 + 직전 ATR14 그리고 종가 > EMA26; 조건 미충족; close=773.07, threshold=774.291, prior_ATR14=1.05565, EMA26=772.249 |
| v1 | session_vwap | 9464.46 | -535.54 | sell /  / 종가 > 뉴욕 거래일별 누적 전형가격 VWAP; 조건 미충족; close=763.06, session_VWAP=764.207, session_volume=6.24478e+07 |
| v1 | obv_20 | 9597.93 | -402.07 | sell /  / OBV > OBV의 SMA20 그리고 종가 > EMA26; 조건 미충족; OBV=-949325, OBV_SMA20=-1.03221e+07, close=766.62, EMA26=771.893 |
| v1 | stochastic_14_3_recovery | 9539.39 | -460.61 | sell /  / 직전 %K14 < 20에서 %K14가 %D3 상향 돌파 (한 봉 목표); 조건 미충족; K14=38.1327, D3=23.7925, previous_K14=21.3012, previous_D3=20.8261 |
| v1 | mfi_14_recovery | 9810.25 | -189.75 | sell /  / 직전 MFI14 < 20, 현재 MFI14 >= 20 (한 봉 목표); 조건 미충족; MFI14=24.2496, previous_MFI14=22.3876 |
| v1 | adx_14_trend | 9981.96 | -18.04 | sell /  / Wilder ADX14 >= 25 그리고 +DI14 > -DI14; 조건 미충족; ADX14=24.2312, plus_DI14=28.3519, minus_DI14=24.6578 |
| v1 | aroon_25_trend | 9728.66 | -271.34 | sell /  / Aroon25 Up > 70 그리고 Down < 30 (동률이면 최신 극값); 조건 미충족; Aroon_up=72, Aroon_down=100 |
| v1 | cci_20_momentum | 9766.23 | -233.77 | sell /  / CCI20 > 100 (전형가격·평균절대편차); 조건 미충족; CCI20=97.3932 |
| v1 | williams_14_recovery | 9529.21 | -470.79 | sell /  / 직전 Williams %R14 < -80, 현재 >= -80 (한 봉 목표); 조건 미충족; Williams_R14=-61.8673, previous_R14=-78.6988 |
| v1 | cmf_20_accumulation | 9690.93 | -309.07 | sell /  / Chaikin Money Flow20 > 0.1; 조건 미충족; CMF20=0.0473512, volume20=7.32623e+07 |
| v1 | chaikin_3_10 | 9565.38 | -434.62 | sell /  / ADL의 EMA3 - EMA10 > 0 그리고 종가 > EMA26; 조건 미충족; Chaikin3_10=1.08024e+06, ADL=4.99714e+07, close=766.62, EMA26=771.893 |
| v1 | roc_10_momentum | 9953.42 | -46.58 | sell /  / 10봉 ROC > 1% 그리고 종가 > EMA26; 조건 미충족; ROC10_percent=0.806376, close=769.45, EMA26=767.181 |
| v1 | trix_15_trend | 9489.99 | -510.01 | sell /  / 15봉 삼중 EMA의 1봉 변화율 TRIX > 0 그리고 종가 > EMA26; 조건 미충족; TRIX15_percent=0.0154379, close=766.62, EMA26=771.893 |
| v1 | keltner_20_breakout | 9810.90 | -189.10 | sell /  / 종가 > EMA20 + 2 x Wilder ATR14; 조건 미충족; close=774.19, upper_Keltner=774.31, EMA20=772.615, ATR14=0.847257 |
| v1 | opening_range_30m | 9651.00 | -349.00 | sell /  / 뉴욕 09:30·09:45 두 완료 봉 최고가를 10:00 이후 종가가 돌파; 자료 부족·변동폭 또는 거래량 없음: 대기; close=766.62 |
| v2 | cash | 10000.00 | 0.00 | 대기 /  / 새 신호 대기 |
| v2 | buy_hold | 9773.37 | -226.63 | buy / partial / 직전 완료 봉 목표 비중 100%; 다음 봉 시가 가정 |
| v2 | trend_8_26 | 9591.24 | -408.76 | sell / filled / 직전 완료 봉 목표 비중 0%; 다음 봉 시가 가정 |
| v2 | momentum_26 | 9482.22 | -517.78 | sell / filled / 직전 완료 봉 목표 비중 0%; 다음 봉 시가 가정 |
| v2 | breakout_8 | 9099.96 | -900.04 | sell / filled / 직전 완료 봉 목표 비중 0%; 다음 봉 시가 가정 |
| v2 | reversion_12 | 9154.53 | -845.47 | sell / filled / 직전 완료 봉 목표 비중 0%; 다음 봉 시가 가정 |
| v2 | volume_26 | 8984.12 | -1015.88 | 중단: 손실 한도 / buy / partial / 직전 완료 봉 목표 비중 100%; 다음 봉 시가 가정 |
| v2 | trend_8_26 AND momentum_26 | 9481.53 | -518.47 | sell / filled / 직전 완료 봉 목표 비중 0%; 다음 봉 시가 가정 |
| v2 | trend_8_26 + momentum_26 | 9536.57 | -463.43 | sell / filled / 직전 완료 봉 목표 비중 0%; 다음 봉 시가 가정 |
| v2 | trend_8_26 AND breakout_8 | 9547.25 | -452.75 | sell / filled / 직전 완료 봉 목표 비중 0%; 다음 봉 시가 가정 |
| v2 | trend_8_26 + breakout_8 | 9381.53 | -618.47 | sell / filled / 직전 완료 봉 목표 비중 0%; 다음 봉 시가 가정 |
| v2 | trend_8_26 AND reversion_12 | 9621.61 | -378.39 | sell / filled / 직전 완료 봉 목표 비중 0%; 다음 봉 시가 가정 |
| v2 | trend_8_26 + reversion_12 | 9369.89 | -630.11 | sell / filled / 직전 완료 봉 목표 비중 0%; 다음 봉 시가 가정 |
| v2 | trend_8_26 AND volume_26 | 9442.22 | -557.78 | sell / filled / 직전 완료 봉 목표 비중 0%; 다음 봉 시가 가정 |
| v2 | trend_8_26 + volume_26 | 9252.87 | -747.13 | sell / filled / 직전 완료 봉 목표 비중 0%; 다음 봉 시가 가정 |
| v2 | momentum_26 AND breakout_8 | 9414.38 | -585.62 | sell / filled / 직전 완료 봉 목표 비중 0%; 다음 봉 시가 가정 |
| v2 | momentum_26 + breakout_8 | 9289.09 | -710.91 | sell / filled / 직전 완료 봉 목표 비중 0%; 다음 봉 시가 가정 |
| v2 | momentum_26 AND reversion_12 | 9722.08 | -277.92 | sell / filled / 직전 완료 봉 목표 비중 0%; 다음 봉 시가 가정 |
| v2 | momentum_26 + reversion_12 | 9395.12 | -604.88 | sell / filled / 직전 완료 봉 목표 비중 0%; 다음 봉 시가 가정 |
| v2 | momentum_26 AND volume_26 | 9523.88 | -476.12 | sell / filled / 직전 완료 봉 목표 비중 0%; 다음 봉 시가 가정 |
| v2 | momentum_26 + volume_26 | 9238.83 | -761.17 | sell / filled / 직전 완료 봉 목표 비중 0%; 다음 봉 시가 가정 |
| v2 | breakout_8 AND reversion_12 | 10000.00 | 0.00 | 대기 /  / 새 신호 대기 |
| v2 | breakout_8 + reversion_12 | 9164.83 | -835.17 | sell / filled / 직전 완료 봉 목표 비중 0%; 다음 봉 시가 가정 |
| v2 | breakout_8 AND volume_26 | 9765.99 | -234.01 | sell / filled / 직전 완료 봉 목표 비중 0%; 다음 봉 시가 가정 |
| v2 | breakout_8 + volume_26 | 9069.44 | -930.56 | sell / filled / 직전 완료 봉 목표 비중 0%; 다음 봉 시가 가정 |
| v2 | reversion_12 AND volume_26 | 9552.33 | -447.67 | sell / filled / 직전 완료 봉 목표 비중 0%; 다음 봉 시가 가정 |
| v2 | reversion_12 + volume_26 | 9115.84 | -884.16 | sell / filled / 직전 완료 봉 목표 비중 0%; 다음 봉 시가 가정 |
| v2 | ema_12_26 | 9736.67 | -263.33 | sell / filled / EMA12 > EMA26; 조건 미충족; EMA12=771.277, EMA26=771.539; 직전 완료 봉 목표를 다음 봉 시가에 모의 적용 |
| v2 | macd_12_26_9 | 9761.73 | -238.27 | sell / filled / MACD > 신호선 그리고 MACD > 0; 조건 미충족; MACD=1.03945, signal9=1.12358; 직전 완료 봉 목표를 다음 봉 시가에 모의 적용 |
| v2 | rsi_14_recovery | 9798.14 | -201.86 | sell / filled / 직전 RSI14 < 30, 현재 RSI14 >= 30 (한 봉 목표); 조건 미충족; RSI14=38.7389, previous_RSI14=37.2051; 직전 완료 봉 목표를 다음 봉 시가에 모의 적용 |
| v2 | bollinger_20_reentry | 9779.61 | -220.39 | sell / filled / 직전 종가 < 직전 하단밴드, 현재 하단밴드 <= 종가 <= SMA20 (한 봉 목표); 조건 미충족; close=762.71, lower20=761.42, SMA20=770.302, previous_lower20=762.585; 직전 완료 봉 목표를 다음 봉 시가에 모의 적용 |
| v2 | donchian_20 | 9808.27 | -191.73 | sell / filled / 종가 > 현재 봉을 제외한 직전 20봉 최고가; 조건 미충족; close=774.19, prior_high20=774.44; 직전 완료 봉 목표를 다음 봉 시가에 모의 적용 |
| v2 | atr_14_breakout | 9807.08 | -192.92 | sell / filled / 종가 > 직전 종가 + 직전 ATR14 그리고 종가 > EMA26; 조건 미충족; close=773.07, threshold=774.291, prior_ATR14=1.05565, EMA26=772.249; 직전 완료 봉 목표를 다음 봉 시가에 모의 적용 |
| v2 | session_vwap | 9445.55 | -554.45 | sell / filled / 종가 > 뉴욕 거래일별 누적 전형가격 VWAP; 조건 미충족; close=763.06, session_VWAP=764.207, session_volume=6.24478e+07; 직전 완료 봉 목표를 다음 봉 시가에 모의 적용 |
| v2 | obv_20 | 9584.50 | -415.50 | sell / filled / OBV > OBV의 SMA20 그리고 종가 > EMA26; 조건 미충족; OBV=-949325, OBV_SMA20=-1.03221e+07, close=766.62, EMA26=771.893; 직전 완료 봉 목표를 다음 봉 시가에 모의 적용 |
| v2 | stochastic_14_3_recovery | 9514.62 | -485.38 | sell / filled / 직전 %K14 < 20에서 %K14가 %D3 상향 돌파 (한 봉 목표); 조건 미충족; K14=38.1327, D3=23.7925, previous_K14=21.3012, previous_D3=20.8261; 직전 완료 봉 목표를 다음 봉 시가에 모의 적용 |
| v2 | mfi_14_recovery | 9800.44 | -199.56 | sell / filled / 직전 MFI14 < 20, 현재 MFI14 >= 20 (한 봉 목표); 조건 미충족; MFI14=24.2496, previous_MFI14=22.3876; 직전 완료 봉 목표를 다음 봉 시가에 모의 적용 |
| v2 | adx_14_trend | 9979.97 | -20.03 | sell / filled / Wilder ADX14 >= 25 그리고 +DI14 > -DI14; 조건 미충족; ADX14=24.2312, plus_DI14=28.3519, minus_DI14=24.6578; 직전 완료 봉 목표를 다음 봉 시가에 모의 적용 |
| v2 | aroon_25_trend | 9722.82 | -277.18 | sell / filled / Aroon25 Up > 70 그리고 Down < 30 (동률이면 최신 극값); 조건 미충족; Aroon_up=72, Aroon_down=100; 직전 완료 봉 목표를 다음 봉 시가에 모의 적용 |
| v2 | cci_20_momentum | 9754.52 | -245.48 | sell / filled / CCI20 > 100 (전형가격·평균절대편차); 조건 미충족; CCI20=97.3932; 직전 완료 봉 목표를 다음 봉 시가에 모의 적용 |
| v2 | williams_14_recovery | 9504.47 | -495.53 | sell / filled / 직전 Williams %R14 < -80, 현재 >= -80 (한 봉 목표); 조건 미충족; Williams_R14=-61.8673, previous_R14=-78.6988; 직전 완료 봉 목표를 다음 봉 시가에 모의 적용 |
| v2 | cmf_20_accumulation | 9681.24 | -318.76 | sell / filled / Chaikin Money Flow20 > 0.1; 조건 미충족; CMF20=0.0473512, volume20=7.32623e+07; 직전 완료 봉 목표를 다음 봉 시가에 모의 적용 |
| v2 | chaikin_3_10 | 9550.09 | -449.91 | sell / filled / ADL의 EMA3 - EMA10 > 0 그리고 종가 > EMA26; 조건 미충족; Chaikin3_10=1.08024e+06, ADL=4.99714e+07, close=766.62, EMA26=771.893; 직전 완료 봉 목표를 다음 봉 시가에 모의 적용 |
| v2 | roc_10_momentum | 9951.43 | -48.57 | sell / filled / 10봉 ROC > 1% 그리고 종가 > EMA26; 조건 미충족; ROC10_percent=0.806376, close=769.45, EMA26=767.181; 직전 완료 봉 목표를 다음 봉 시가에 모의 적용 |
| v2 | trix_15_trend | 9472.93 | -527.07 | sell / filled / 15봉 삼중 EMA의 1봉 변화율 TRIX > 0 그리고 종가 > EMA26; 조건 미충족; TRIX15_percent=0.0154379, close=766.62, EMA26=771.893; 직전 완료 봉 목표를 다음 봉 시가에 모의 적용 |
| v2 | keltner_20_breakout | 9803.05 | -196.95 | sell / filled / 종가 > EMA20 + 2 x Wilder ATR14; 조건 미충족; close=774.19, upper_Keltner=774.31, EMA20=772.615, ATR14=0.847257; 직전 완료 봉 목표를 다음 봉 시가에 모의 적용 |
| v2 | opening_range_30m | 9639.43 | -360.57 | sell / filled / 뉴욕 09:30·09:45 두 완료 봉 최고가를 10:00 이후 종가가 돌파; 자료 부족·변동폭 또는 거래량 없음: 대기; close=766.62; 직전 완료 봉 목표를 다음 봉 시가에 모의 적용 |

### 같은 기간의 비용·노출 비교 (사후 연구)

| 전략 | 비용 전 | 비용 후 | 100% 보유 | 같은 평균 노출 보유 | 평균 노출 |
|---|---:|---:|---:|---:|---:|
| cash | 0.00% | 0.00% | -1.43% | -0.00% | 0.00% |
| buy_hold | -1.02% | -1.43% | -1.43% | -1.43% | 100.00% |
| trend_8_26 | -0.48% | -4.17% | -1.43% | -0.79% | 54.97% |
| momentum_26 | -1.12% | -5.58% | -1.43% | -0.80% | 55.50% |
| breakout_8 | -0.24% | -16.38% | -1.43% | -0.35% | 24.35% |
| reversion_12 | -0.90% | -11.15% | -1.43% | -0.37% | 25.65% |
| volume_26 | -1.49% | -10.93% | -1.43% | -0.14% | 9.42% |
| trend_8_26 AND momentum_26 | -0.52% | -5.01% | -1.43% | -0.69% | 48.43% |
| trend_8_26 + momentum_26 | -0.80% | -4.88% | -1.43% | -0.79% | 55.24% |
| trend_8_26 AND breakout_8 | 0.13% | -11.35% | -1.43% | -0.23% | 15.71% |
| trend_8_26 + breakout_8 | -0.36% | -10.10% | -1.43% | -0.57% | 39.67% |
| trend_8_26 AND reversion_12 | 0.21% | -4.72% | -1.43% | -0.09% | 6.54% |
| trend_8_26 + reversion_12 | -0.68% | -7.54% | -1.43% | -0.58% | 40.32% |
| trend_8_26 AND volume_26 | -1.05% | -6.30% | -1.43% | -0.08% | 5.50% |
| trend_8_26 + volume_26 | -0.98% | -7.62% | -1.43% | -0.46% | 32.20% |
| momentum_26 AND breakout_8 | 0.30% | -11.95% | -1.43% | -0.25% | 17.28% |
| momentum_26 + breakout_8 | -0.68% | -11.14% | -1.43% | -0.57% | 39.93% |
| momentum_26 AND reversion_12 | -0.39% | -5.28% | -1.43% | -0.09% | 6.28% |
| momentum_26 + reversion_12 | -1.00% | -7.64% | -1.43% | -0.58% | 40.58% |
| momentum_26 AND volume_26 | -0.79% | -5.27% | -1.43% | -0.06% | 3.93% |
| momentum_26 + volume_26 | -1.30% | -7.53% | -1.43% | -0.47% | 32.46% |
| breakout_8 AND reversion_12 | 0.00% | 0.00% | -1.43% | -0.00% | 0.00% |
| breakout_8 + reversion_12 | -0.57% | -13.45% | -1.43% | -0.36% | 25.01% |
| breakout_8 AND volume_26 | -0.35% | -2.83% | -1.43% | -0.03% | 2.09% |
| breakout_8 + volume_26 | -0.87% | -13.16% | -1.43% | -0.24% | 16.89% |
| reversion_12 AND volume_26 | -0.97% | -5.05% | -1.43% | -0.05% | 3.66% |
| reversion_12 + volume_26 | -1.19% | -10.67% | -1.43% | -0.25% | 17.55% |
| ema_12_26 | -1.30% | -4.56% | -1.43% | -0.84% | 58.64% |
| macd_12_26_9 | -0.57% | -5.46% | -1.43% | -0.50% | 34.82% |
| rsi_14_recovery | -0.42% | -3.71% | -1.43% | -0.03% | 2.09% |
| bollinger_20_reentry | -0.96% | -6.22% | -1.43% | -0.05% | 3.40% |
| donchian_20 | 0.06% | -8.39% | -1.43% | -0.11% | 7.59% |
| atr_14_breakout | 0.29% | -5.44% | -1.43% | -0.06% | 3.93% |
| session_vwap | -0.59% | -11.25% | -1.43% | -0.67% | 46.86% |
| obv_20 | -1.15% | -9.87% | -1.43% | -0.60% | 41.88% |
| stochastic_14_3_recovery | 0.26% | -13.45% | -1.43% | -0.13% | 9.16% |
| mfi_14_recovery | 0.11% | -2.79% | -1.43% | -0.03% | 1.83% |
| adx_14_trend | 0.74% | -1.35% | -1.43% | -0.34% | 23.82% |
| aroon_25_trend | -0.07% | -2.97% | -1.43% | -0.38% | 26.70% |
| cci_20_momentum | 0.07% | -7.99% | -1.43% | -0.34% | 23.56% |
| williams_14_recovery | 0.15% | -10.59% | -1.43% | -0.10% | 7.07% |
| cmf_20_accumulation | 0.68% | -3.86% | -1.43% | -0.71% | 49.74% |
| chaikin_3_10 | -0.07% | -6.95% | -1.43% | -0.65% | 45.29% |
| roc_10_momentum | -0.13% | -0.97% | -1.43% | -0.02% | 1.05% |
| trix_15_trend | -1.14% | -6.39% | -1.43% | -0.65% | 45.55% |
| keltner_20_breakout | -0.22% | -4.73% | -1.43% | -0.18% | 12.30% |
| opening_range_30m | -0.27% | -6.36% | -1.43% | -0.59% | 41.10% |

동일 구간·초기 자금, 종료 시 청산 비용 포함. 노출 맞춤은 사후 설명용이며 v2 실제 계좌 성과가 아닙니다.
[낙폭 분해·비용 영향·전체 구간](SPY/comparison.json)

[v1 전체 기록](SPY/accounts.json) · [v2 전체 기록](SPY/accounts-v2.json)

## QQQ 계좌

| 모델 | 전략 | 평가액 USD | 손익 USD | 최근 매매·이유 |
|---|---|---:|---:|---|
| v1 | cash | 10000.00 | 0.00 | 대기 /  / 새 신호 대기 |
| v1 | buy_hold | 9697.05 | -302.95 | buy /  / buy_hold: prior completed bar target 100%; next bar open simulation |
| v1 | trend_8_26 | 9679.99 | -320.01 | sell /  / trend_8_26: prior completed bar target 0%; next bar open simulation |
| v1 | momentum_26 | 9370.26 | -629.74 | sell /  / momentum_26: prior completed bar target 0%; next bar open simulation |
| v1 | breakout_8 | 9613.51 | -386.49 | sell /  / breakout_8: prior completed bar target 0%; next bar open simulation |
| v1 | reversion_12 | 9595.77 | -404.23 | sell /  / reversion_12: prior completed bar target 0%; next bar open simulation |
| v1 | volume_26 | 9583.68 | -416.32 | sell /  / volume_26: prior completed bar target 0%; next bar open simulation |
| v1 | trend_8_26 AND momentum_26 | 9732.14 | -267.86 | sell /  / trend_8_26 AND momentum_26: prior completed bar target 0%; next bar open simulation |
| v1 | trend_8_26 + momentum_26 | 9562.10 | -437.90 | sell /  / trend_8_26 + momentum_26: prior completed bar target 0%; next bar open simulation |
| v1 | trend_8_26 AND breakout_8 | 9949.62 | -50.38 | sell /  / trend_8_26 AND breakout_8: prior completed bar target 0%; next bar open simulation |
| v1 | trend_8_26 + breakout_8 | 9685.58 | -314.42 | sell /  / trend_8_26 + breakout_8: prior completed bar target 0%; next bar open simulation |
| v1 | trend_8_26 AND reversion_12 | 9885.50 | -114.50 | sell /  / trend_8_26 AND reversion_12: prior completed bar target 0%; next bar open simulation |
| v1 | trend_8_26 + reversion_12 | 9676.68 | -323.32 | sell /  / trend_8_26 + reversion_12: prior completed bar target 0%; next bar open simulation |
| v1 | trend_8_26 AND volume_26 | 9846.67 | -153.33 | sell /  / trend_8_26 AND volume_26: prior completed bar target 0%; next bar open simulation |
| v1 | trend_8_26 + volume_26 | 9631.84 | -368.16 | sell /  / trend_8_26 + volume_26: prior completed bar target 0%; next bar open simulation |
| v1 | momentum_26 AND breakout_8 | 9644.64 | -355.36 | sell /  / momentum_26 AND breakout_8: prior completed bar target 0%; next bar open simulation |
| v1 | momentum_26 + breakout_8 | 9491.44 | -508.56 | sell /  / momentum_26 + breakout_8: prior completed bar target 0%; next bar open simulation |
| v1 | momentum_26 AND reversion_12 | 9783.95 | -216.05 | sell /  / momentum_26 AND reversion_12: prior completed bar target 0%; next bar open simulation |
| v1 | momentum_26 + reversion_12 | 9539.75 | -460.25 | sell /  / momentum_26 + reversion_12: prior completed bar target 0%; next bar open simulation |
| v1 | momentum_26 AND volume_26 | 9819.14 | -180.86 | sell /  / momentum_26 AND volume_26: prior completed bar target 0%; next bar open simulation |
| v1 | momentum_26 + volume_26 | 9495.49 | -504.51 | sell /  / momentum_26 + volume_26: prior completed bar target 0%; next bar open simulation |
| v1 | breakout_8 AND reversion_12 | 10000.00 | 0.00 | 대기 /  / 새 신호 대기 |
| v1 | breakout_8 + reversion_12 | 9643.08 | -356.92 | sell /  / breakout_8 + reversion_12: prior completed bar target 0%; next bar open simulation |
| v1 | breakout_8 AND volume_26 | 9929.33 | -70.67 | sell /  / breakout_8 AND volume_26: prior completed bar target 0%; next bar open simulation |
| v1 | breakout_8 + volume_26 | 9617.74 | -382.26 | sell /  / breakout_8 + volume_26: prior completed bar target 0%; next bar open simulation |
| v1 | reversion_12 AND volume_26 | 9860.10 | -139.90 | sell /  / reversion_12 AND volume_26: prior completed bar target 0%; next bar open simulation |
| v1 | reversion_12 + volume_26 | 9628.05 | -371.95 | sell /  / reversion_12 + volume_26: prior completed bar target 0%; next bar open simulation |
| v1 | ema_12_26 | 9439.49 | -560.51 | sell /  / EMA12 > EMA26; 조건 미충족; EMA12=723.809, EMA26=723.847 |
| v1 | macd_12_26_9 | 9765.43 | -234.57 | sell /  / MACD > 신호선 그리고 MACD > 0; 조건 미충족; MACD=1.7811, signal9=1.82319 |
| v1 | rsi_14_recovery | 9764.60 | -235.40 | sell /  / 직전 RSI14 < 30, 현재 RSI14 >= 30 (한 봉 목표); 조건 미충족; RSI14=30.4228, previous_RSI14=31.111 |
| v1 | bollinger_20_reentry | 9823.48 | -176.52 | sell /  / 직전 종가 < 직전 하단밴드, 현재 하단밴드 <= 종가 <= SMA20 (한 봉 목표); 조건 미충족; close=706.995, lower20=705.434, SMA20=720.761, previous_lower20=707.596 |
| v1 | donchian_20 | 9889.14 | -110.86 | sell /  / 종가 > 현재 봉을 제외한 직전 20봉 최고가; 조건 미충족; close=726.885, prior_high20=727.77 |
| v1 | atr_14_breakout | 9887.37 | -112.63 | sell /  / 종가 > 직전 종가 + 직전 ATR14 그리고 종가 > EMA26; 조건 미충족; close=725.79, threshold=727.527, prior_ATR14=1.49237, EMA26=724.609 |
| v1 | session_vwap | 9387.48 | -612.52 | sell /  / 종가 > 뉴욕 거래일별 누적 전형가격 VWAP; 조건 미충족; close=706.51, session_VWAP=708.65, session_volume=2.91223e+08 |
| v1 | obv_20 | 9508.81 | -491.19 | sell /  / OBV > OBV의 SMA20 그리고 종가 > EMA26; 조건 미충족; OBV=4.39726e+08, OBV_SMA20=4.50483e+08, close=713.775, EMA26=723.847 |
| v1 | stochastic_14_3_recovery | 9410.19 | -589.81 | buy /  / 직전 %K14 < 20에서 %K14가 %D3 상향 돌파 (한 봉 목표); 조건 충족; K14=26.561, D3=18.5101, previous_K14=15.4197, previous_D3=17.0473 |
| v1 | mfi_14_recovery | 9813.56 | -186.44 | sell /  / 직전 MFI14 < 20, 현재 MFI14 >= 20 (한 봉 목표); 조건 미충족; MFI14=30.3876, previous_MFI14=31.1747 |
| v1 | adx_14_trend | 9825.33 | -174.67 | sell /  / Wilder ADX14 >= 25 그리고 +DI14 > -DI14; 조건 미충족; ADX14=23.847, plus_DI14=27.825, minus_DI14=26.997 |
| v1 | aroon_25_trend | 9774.48 | -225.52 | sell /  / Aroon25 Up > 70 그리고 Down < 30 (동률이면 최신 극값); 조건 미충족; Aroon_up=68, Aroon_down=4 |
| v1 | cci_20_momentum | 9862.10 | -137.90 | sell /  / CCI20 > 100 (전형가격·평균절대편차); 조건 미충족; CCI20=80.102 |
| v1 | williams_14_recovery | 9583.73 | -416.27 | buy /  / 직전 Williams %R14 < -80, 현재 >= -80 (한 봉 목표); 조건 충족; Williams_R14=-73.439, previous_R14=-84.5803 |
| v1 | cmf_20_accumulation | 9379.66 | -620.34 | sell /  / Chaikin Money Flow20 > 0.1; 조건 미충족; CMF20=0.025426, volume20=1.62711e+08 |
| v1 | chaikin_3_10 | 9515.49 | -484.51 | sell /  / ADL의 EMA3 - EMA10 > 0 그리고 종가 > EMA26; 조건 미충족; Chaikin3_10=7.32608e+06, ADL=3.89342e+08, close=713.775, EMA26=723.847 |
| v1 | roc_10_momentum | 9961.33 | -38.67 | sell /  / 10봉 ROC > 1% 그리고 종가 > EMA26; 조건 미충족; ROC10_percent=0.681109, close=725.78, EMA26=721.667 |
| v1 | trix_15_trend | 9467.11 | -532.89 | sell /  / 15봉 삼중 EMA의 1봉 변화율 TRIX > 0 그리고 종가 > EMA26; 조건 미충족; TRIX15_percent=0.0245938, close=713.775, EMA26=723.847 |
| v1 | keltner_20_breakout | 9782.40 | -217.60 | sell /  / 종가 > EMA20 + 2 x Wilder ATR14; 조건 미충족; close=726.815, upper_Keltner=727.39, EMA20=724.295, ATR14=1.54727 |
| v1 | opening_range_30m | 9599.28 | -400.72 | sell /  / 뉴욕 09:30·09:45 두 완료 봉 최고가를 10:00 이후 종가가 돌파; 자료 부족·변동폭 또는 거래량 없음: 대기; close=713.775 |
| v2 | cash | 10000.00 | 0.00 | 대기 /  / 새 신호 대기 |
| v2 | buy_hold | 9383.60 | -616.40 | buy / partial / 직전 완료 봉 목표 비중 100%; 다음 봉 시가 가정 |
| v2 | trend_8_26 | 9482.37 | -517.63 | sell / filled / 직전 완료 봉 목표 비중 0%; 다음 봉 시가 가정 |
| v2 | momentum_26 | 9261.49 | -738.51 | sell / filled / 직전 완료 봉 목표 비중 0%; 다음 봉 시가 가정 |
| v2 | breakout_8 | 9279.42 | -720.58 | sell / filled / 직전 완료 봉 목표 비중 0%; 다음 봉 시가 가정 |
| v2 | reversion_12 | 9109.28 | -890.72 | sell / filled / 직전 완료 봉 목표 비중 0%; 다음 봉 시가 가정 |
| v2 | volume_26 | 9565.80 | -434.20 | 중단: 손실 한도 / sell / filled / 직전 완료 봉 목표 비중 0%; 다음 봉 시가 가정 |
| v2 | trend_8_26 AND momentum_26 | 9626.87 | -373.13 | sell / filled / 직전 완료 봉 목표 비중 0%; 다음 봉 시가 가정 |
| v2 | trend_8_26 + momentum_26 | 9410.82 | -589.18 | sell / filled / 직전 완료 봉 목표 비중 0%; 다음 봉 시가 가정 |
| v2 | trend_8_26 AND breakout_8 | 9840.07 | -159.93 | sell / filled / 직전 완료 봉 목표 비중 0%; 다음 봉 시가 가정 |
| v2 | trend_8_26 + breakout_8 | 9419.99 | -580.01 | sell / filled / 직전 완료 봉 목표 비중 0%; 다음 봉 시가 가정 |
| v2 | trend_8_26 AND reversion_12 | 9742.38 | -257.62 | sell / filled / 직전 완료 봉 목표 비중 0%; 다음 봉 시가 가정 |
| v2 | trend_8_26 + reversion_12 | 9333.00 | -667.00 | sell / filled / 직전 완료 봉 목표 비중 0%; 다음 봉 시가 가정 |
| v2 | trend_8_26 AND volume_26 | 9679.53 | -320.47 | sell / filled / 직전 완료 봉 목표 비중 0%; 다음 봉 시가 가정 |
| v2 | trend_8_26 + volume_26 | 9236.62 | -763.38 | sell / filled / 직전 완료 봉 목표 비중 0%; 다음 봉 시가 가정 |
| v2 | momentum_26 AND breakout_8 | 9591.37 | -408.63 | sell / filled / 직전 완료 봉 목표 비중 0%; 다음 봉 시가 가정 |
| v2 | momentum_26 + breakout_8 | 9270.73 | -729.27 | sell / filled / 직전 완료 봉 목표 비중 0%; 다음 봉 시가 가정 |
| v2 | momentum_26 AND reversion_12 | 9776.12 | -223.88 | sell / filled / 직전 완료 봉 목표 비중 0%; 다음 봉 시가 가정 |
| v2 | momentum_26 + reversion_12 | 9262.53 | -737.47 | sell / filled / 직전 완료 봉 목표 비중 0%; 다음 봉 시가 가정 |
| v2 | momentum_26 AND volume_26 | 9749.31 | -250.69 | sell / filled / 직전 완료 봉 목표 비중 0%; 다음 봉 시가 가정 |
| v2 | momentum_26 + volume_26 | 9147.59 | -852.41 | sell / filled / 직전 완료 봉 목표 비중 0%; 다음 봉 시가 가정 |
| v2 | breakout_8 AND reversion_12 | 10000.00 | 0.00 | 대기 /  / 새 신호 대기 |
| v2 | breakout_8 + reversion_12 | 9290.62 | -709.38 | sell / filled / 직전 완료 봉 목표 비중 0%; 다음 봉 시가 가정 |
| v2 | breakout_8 AND volume_26 | 9871.76 | -128.24 | sell / filled / 직전 완료 봉 목표 비중 0%; 다음 봉 시가 가정 |
| v2 | breakout_8 + volume_26 | 9194.86 | -805.14 | sell / filled / 직전 완료 봉 목표 비중 0%; 다음 봉 시가 가정 |
| v2 | reversion_12 AND volume_26 | 9547.64 | -452.36 | 중단: 손실 한도 / sell / filled / 직전 완료 봉 목표 비중 0%; 다음 봉 시가 가정 |
| v2 | reversion_12 + volume_26 | 9110.20 | -889.80 | sell / filled / 직전 완료 봉 목표 비중 0%; 다음 봉 시가 가정 |
| v2 | ema_12_26 | 9430.06 | -569.94 | sell / filled / EMA12 > EMA26; 조건 미충족; EMA12=723.809, EMA26=723.847; 직전 완료 봉 목표를 다음 봉 시가에 모의 적용 |
| v2 | macd_12_26_9 | 9755.67 | -244.33 | sell / filled / MACD > 신호선 그리고 MACD > 0; 조건 미충족; MACD=1.7811, signal9=1.82319; 직전 완료 봉 목표를 다음 봉 시가에 모의 적용 |
| v2 | rsi_14_recovery | 9754.84 | -245.16 | sell / filled / 직전 RSI14 < 30, 현재 RSI14 >= 30 (한 봉 목표); 조건 미충족; RSI14=30.4228, previous_RSI14=31.111; 직전 완료 봉 목표를 다음 봉 시가에 모의 적용 |
| v2 | bollinger_20_reentry | 9815.62 | -184.38 | sell / filled / 직전 종가 < 직전 하단밴드, 현재 하단밴드 <= 종가 <= SMA20 (한 봉 목표); 조건 미충족; close=706.995, lower20=705.434, SMA20=720.761, previous_lower20=707.596; 직전 완료 봉 목표를 다음 봉 시가에 모의 적용 |
| v2 | donchian_20 | 9881.23 | -118.77 | sell / filled / 종가 > 현재 봉을 제외한 직전 20봉 최고가; 조건 미충족; close=726.885, prior_high20=727.77; 직전 완료 봉 목표를 다음 봉 시가에 모의 적용 |
| v2 | atr_14_breakout | 9879.47 | -120.53 | sell / filled / 종가 > 직전 종가 + 직전 ATR14 그리고 종가 > EMA26; 조건 미충족; close=725.79, threshold=727.527, prior_ATR14=1.49237, EMA26=724.609; 직전 완료 봉 목표를 다음 봉 시가에 모의 적용 |
| v2 | session_vwap | 9368.73 | -631.27 | sell / filled / 종가 > 뉴욕 거래일별 누적 전형가격 VWAP; 조건 미충족; close=706.51, session_VWAP=708.65, session_volume=2.91223e+08; 직전 완료 봉 목표를 다음 봉 시가에 모의 적용 |
| v2 | obv_20 | 9495.51 | -504.49 | sell / filled / OBV > OBV의 SMA20 그리고 종가 > EMA26; 조건 미충족; OBV=4.39726e+08, OBV_SMA20=4.50483e+08, close=713.775, EMA26=723.847; 직전 완료 봉 목표를 다음 봉 시가에 모의 적용 |
| v2 | stochastic_14_3_recovery | 9694.13 | -305.87 | 중단: 손실 한도 / sell / filled / 직전 %K14 < 20에서 %K14가 %D3 상향 돌파 (한 봉 목표); 조건 미충족; K14=10.576, D3=8.00581, previous_K14=7.39787, previous_D3=7.27486; 직전 완료 봉 목표를 다음 봉 시가에 모의 적용 |
| v2 | mfi_14_recovery | 9809.63 | -190.37 | sell / filled / 직전 MFI14 < 20, 현재 MFI14 >= 20 (한 봉 목표); 조건 미충족; MFI14=30.3876, previous_MFI14=31.1747; 직전 완료 봉 목표를 다음 봉 시가에 모의 적용 |
| v2 | adx_14_trend | 9817.47 | -182.53 | sell / filled / Wilder ADX14 >= 25 그리고 +DI14 > -DI14; 조건 미충족; ADX14=23.847, plus_DI14=27.825, minus_DI14=26.997; 직전 완료 봉 목표를 다음 봉 시가에 모의 적용 |
| v2 | aroon_25_trend | 9766.66 | -233.34 | sell / filled / Aroon25 Up > 70 그리고 Down < 30 (동률이면 최신 극값); 조건 미충족; Aroon_up=68, Aroon_down=4; 직전 완료 봉 목표를 다음 봉 시가에 모의 적용 |
| v2 | cci_20_momentum | 9852.25 | -147.75 | sell / filled / CCI20 > 100 (전형가격·평균절대편차); 조건 미충족; CCI20=80.102; 직전 완료 봉 목표를 다음 봉 시가에 모의 적용 |
| v2 | williams_14_recovery | 9561.71 | -438.29 | buy / partial / 직전 Williams %R14 < -80, 현재 >= -80 (한 봉 목표); 조건 충족; Williams_R14=-73.439, previous_R14=-84.5803; 직전 완료 봉 목표를 다음 봉 시가에 모의 적용 |
| v2 | cmf_20_accumulation | 9364.67 | -635.33 | sell / filled / Chaikin Money Flow20 > 0.1; 조건 미충족; CMF20=0.025426, volume20=1.62711e+08; 직전 완료 봉 목표를 다음 봉 시가에 모의 적용 |
| v2 | chaikin_3_10 | 9502.18 | -497.82 | sell / filled / ADL의 EMA3 - EMA10 > 0 그리고 종가 > EMA26; 조건 미충족; Chaikin3_10=7.32608e+06, ADL=3.89342e+08, close=713.775, EMA26=723.847; 직전 완료 봉 목표를 다음 봉 시가에 모의 적용 |
| v2 | roc_10_momentum | 9957.34 | -42.66 | sell / filled / 10봉 ROC > 1% 그리고 종가 > EMA26; 조건 미충족; ROC10_percent=0.681109, close=725.78, EMA26=721.667; 직전 완료 봉 목표를 다음 봉 시가에 모의 적용 |
| v2 | trix_15_trend | 9453.87 | -546.13 | sell / filled / 15봉 삼중 EMA의 1봉 변화율 TRIX > 0 그리고 종가 > EMA26; 조건 미충족; TRIX15_percent=0.0245938, close=713.775, EMA26=723.847; 직전 완료 봉 목표를 다음 봉 시가에 모의 적용 |
| v2 | keltner_20_breakout | 9772.62 | -227.38 | sell / filled / 종가 > EMA20 + 2 x Wilder ATR14; 조건 미충족; close=726.815, upper_Keltner=727.39, EMA20=724.295, ATR14=1.54727; 직전 완료 봉 목표를 다음 봉 시가에 모의 적용 |
| v2 | opening_range_30m | 9589.69 | -410.31 | sell / filled / 뉴욕 09:30·09:45 두 완료 봉 최고가를 10:00 이후 종가가 돌파; 자료 부족·변동폭 또는 거래량 없음: 대기; close=713.775; 직전 완료 봉 목표를 다음 봉 시가에 모의 적용 |

### 같은 기간의 비용·노출 비교 (사후 연구)

| 전략 | 비용 전 | 비용 후 | 100% 보유 | 같은 평균 노출 보유 | 평균 노출 |
|---|---:|---:|---:|---:|---:|
| cash | 0.00% | 0.00% | -6.57% | -0.00% | 0.00% |
| buy_hold | -6.18% | -6.57% | -6.57% | -6.57% | 100.00% |
| trend_8_26 | -2.52% | -6.14% | -6.57% | -2.82% | 42.41% |
| momentum_26 | -4.20% | -9.29% | -6.57% | -2.61% | 39.27% |
| breakout_8 | -1.70% | -16.55% | -6.57% | -1.26% | 18.85% |
| reversion_12 | -0.37% | -12.54% | -6.57% | -2.09% | 31.41% |
| volume_26 | -1.07% | -14.59% | -6.57% | -1.14% | 17.02% |
| trend_8_26 AND momentum_26 | -1.38% | -4.64% | -6.57% | -2.18% | 32.72% |
| trend_8_26 + momentum_26 | -3.36% | -7.14% | -6.57% | -2.72% | 40.84% |
| trend_8_26 AND breakout_8 | 0.42% | -7.67% | -6.57% | -0.79% | 11.78% |
| trend_8_26 + breakout_8 | -2.10% | -10.94% | -6.57% | -2.04% | 30.63% |
| trend_8_26 AND reversion_12 | -0.22% | -4.33% | -6.57% | -0.44% | 6.54% |
| trend_8_26 + reversion_12 | -1.44% | -8.82% | -6.57% | -2.46% | 36.92% |
| trend_8_26 AND volume_26 | 0.23% | -4.70% | -6.57% | -0.35% | 5.24% |
| trend_8_26 + volume_26 | -1.79% | -10.47% | -6.57% | -1.98% | 29.72% |
| momentum_26 AND breakout_8 | -0.36% | -9.16% | -6.57% | -0.81% | 12.04% |
| momentum_26 + breakout_8 | -2.95% | -12.81% | -6.57% | -1.94% | 29.06% |
| momentum_26 AND reversion_12 | -1.04% | -5.51% | -6.57% | -0.44% | 6.54% |
| momentum_26 + reversion_12 | -2.29% | -9.99% | -6.57% | -2.35% | 35.35% |
| momentum_26 AND volume_26 | -0.38% | -4.08% | -6.57% | -0.25% | 3.66% |
| momentum_26 + volume_26 | -2.64% | -11.61% | -6.57% | -1.88% | 28.15% |
| breakout_8 AND reversion_12 | 0.00% | 0.00% | -6.57% | -0.00% | 0.00% |
| breakout_8 + reversion_12 | -1.03% | -13.49% | -6.57% | -1.68% | 25.14% |
| breakout_8 AND volume_26 | 0.32% | -2.18% | -6.57% | -0.16% | 2.36% |
| breakout_8 + volume_26 | -1.38% | -14.15% | -6.57% | -1.20% | 17.94% |
| reversion_12 AND volume_26 | -1.22% | -8.03% | -6.57% | -0.56% | 8.38% |
| reversion_12 + volume_26 | -0.71% | -13.03% | -6.57% | -1.62% | 24.22% |
| ema_12_26 | -3.84% | -6.63% | -6.57% | -2.63% | 39.53% |
| macd_12_26_9 | -0.56% | -5.05% | -6.57% | -1.55% | 23.30% |
| rsi_14_recovery | -0.53% | -6.21% | -6.57% | -0.25% | 3.66% |
| bollinger_20_reentry | -0.05% | -5.76% | -6.57% | -0.25% | 3.66% |
| donchian_20 | 0.58% | -5.17% | -6.57% | -0.44% | 6.54% |
| atr_14_breakout | 0.32% | -3.81% | -6.57% | -0.19% | 2.88% |
| session_vwap | -3.33% | -14.78% | -6.57% | -3.04% | 45.81% |
| obv_20 | -3.99% | -12.09% | -6.57% | -1.83% | 27.49% |
| stochastic_14_3_recovery | -0.31% | -12.85% | -6.57% | -0.56% | 8.38% |
| mfi_14_recovery | -1.19% | -3.24% | -6.57% | -0.09% | 1.31% |
| adx_14_trend | -0.10% | -3.00% | -6.57% | -1.33% | 19.90% |
| aroon_25_trend | -0.13% | -3.43% | -6.57% | -1.15% | 17.28% |
| cci_20_momentum | 0.26% | -4.67% | -6.57% | -1.21% | 18.06% |
| williams_14_recovery | -0.14% | -11.22% | -6.57% | -0.49% | 7.33% |
| cmf_20_accumulation | -3.30% | -9.96% | -6.57% | -2.47% | 37.17% |
| chaikin_3_10 | -5.18% | -12.82% | -6.57% | -2.13% | 31.94% |
| roc_10_momentum | 0.13% | -1.54% | -6.57% | -0.32% | 4.71% |
| trix_15_trend | -2.73% | -6.34% | -6.57% | -2.25% | 33.77% |
| keltner_20_breakout | -0.82% | -5.70% | -6.57% | -0.58% | 8.64% |
| opening_range_30m | -1.73% | -6.95% | -6.57% | -2.28% | 34.29% |

동일 구간·초기 자금, 종료 시 청산 비용 포함. 노출 맞춤은 사후 설명용이며 v2 실제 계좌 성과가 아닙니다.
[낙폭 분해·비용 영향·전체 구간](QQQ/comparison.json)

[v1 전체 기록](QQQ/accounts.json) · [v2 전체 기록](QQQ/accounts-v2.json)

## IWM 계좌

| 모델 | 전략 | 평가액 USD | 손익 USD | 최근 매매·이유 |
|---|---|---:|---:|---|
| v1 | cash | 10000.00 | 0.00 | 대기 /  / 새 신호 대기 |
| v1 | buy_hold | 9991.98 | -8.02 | buy /  / buy_hold: prior completed bar target 100%; next bar open simulation |
| v1 | trend_8_26 | 9801.27 | -198.73 | sell /  / trend_8_26: prior completed bar target 0%; next bar open simulation |
| v1 | momentum_26 | 9795.94 | -204.06 | sell /  / momentum_26: prior completed bar target 0%; next bar open simulation |
| v1 | breakout_8 | 9349.32 | -650.68 | sell /  / breakout_8: prior completed bar target 0%; next bar open simulation |
| v1 | reversion_12 | 9736.37 | -263.63 | sell /  / reversion_12: prior completed bar target 0%; next bar open simulation |
| v1 | volume_26 | 9885.16 | -114.84 | sell /  / volume_26: prior completed bar target 0%; next bar open simulation |
| v1 | trend_8_26 AND momentum_26 | 9746.90 | -253.10 | sell /  / trend_8_26 AND momentum_26: prior completed bar target 0%; next bar open simulation |
| v1 | trend_8_26 + momentum_26 | 9798.73 | -201.27 | sell /  / trend_8_26 + momentum_26: prior completed bar target 0%; next bar open simulation |
| v1 | trend_8_26 AND breakout_8 | 9504.10 | -495.90 | sell /  / trend_8_26 AND breakout_8: prior completed bar target 0%; next bar open simulation |
| v1 | trend_8_26 + breakout_8 | 9572.84 | -427.16 | sell /  / trend_8_26 + breakout_8: prior completed bar target 0%; next bar open simulation |
| v1 | trend_8_26 AND reversion_12 | 9811.31 | -188.69 | sell /  / trend_8_26 AND reversion_12: prior completed bar target 0%; next bar open simulation |
| v1 | trend_8_26 + reversion_12 | 9768.56 | -231.44 | sell /  / trend_8_26 + reversion_12: prior completed bar target 0%; next bar open simulation |
| v1 | trend_8_26 AND volume_26 | 9927.90 | -72.10 | sell /  / trend_8_26 AND volume_26: prior completed bar target 0%; next bar open simulation |
| v1 | trend_8_26 + volume_26 | 9862.68 | -137.32 | sell /  / trend_8_26 + volume_26: prior completed bar target 0%; next bar open simulation |
| v1 | momentum_26 AND breakout_8 | 9552.12 | -447.88 | sell /  / momentum_26 AND breakout_8: prior completed bar target 0%; next bar open simulation |
| v1 | momentum_26 + breakout_8 | 9589.36 | -410.64 | sell /  / momentum_26 + breakout_8: prior completed bar target 0%; next bar open simulation |
| v1 | momentum_26 AND reversion_12 | 9876.67 | -123.33 | sell /  / momentum_26 AND reversion_12: prior completed bar target 0%; next bar open simulation |
| v1 | momentum_26 + reversion_12 | 9844.41 | -155.59 | sell /  / momentum_26 + reversion_12: prior completed bar target 0%; next bar open simulation |
| v1 | momentum_26 AND volume_26 | 9977.14 | -22.86 | sell /  / momentum_26 AND volume_26: prior completed bar target 0%; next bar open simulation |
| v1 | momentum_26 + volume_26 | 9879.83 | -120.17 | sell /  / momentum_26 + volume_26: prior completed bar target 0%; next bar open simulation |
| v1 | breakout_8 AND reversion_12 | 10000.00 | 0.00 | 대기 /  / 새 신호 대기 |
| v1 | breakout_8 + reversion_12 | 9559.78 | -440.22 | sell /  / breakout_8 + reversion_12: prior completed bar target 0%; next bar open simulation |
| v1 | breakout_8 AND volume_26 | 9967.28 | -32.72 | sell /  / breakout_8 AND volume_26: prior completed bar target 0%; next bar open simulation |
| v1 | breakout_8 + volume_26 | 9632.70 | -367.30 | sell /  / breakout_8 + volume_26: prior completed bar target 0%; next bar open simulation |
| v1 | reversion_12 AND volume_26 | 9937.60 | -62.40 | sell /  / reversion_12 AND volume_26: prior completed bar target 0%; next bar open simulation |
| v1 | reversion_12 + volume_26 | 9849.76 | -150.24 | sell /  / reversion_12 + volume_26: prior completed bar target 0%; next bar open simulation |
| v1 | ema_12_26 | 9815.21 | -184.79 | sell /  / EMA12 > EMA26; 조건 미충족; EMA12=276.256, EMA26=276.345 |
| v1 | macd_12_26_9 | 9906.42 | -93.58 | sell /  / MACD > 신호선 그리고 MACD > 0; 조건 미충족; MACD=0.978353, signal9=1.01104 |
| v1 | rsi_14_recovery | 9786.95 | -213.05 | sell /  / 직전 RSI14 < 30, 현재 RSI14 >= 30 (한 봉 목표); 조건 미충족; RSI14=46.986, previous_RSI14=37.1649 |
| v1 | bollinger_20_reentry | 9848.19 | -151.81 | sell /  / 직전 종가 < 직전 하단밴드, 현재 하단밴드 <= 종가 <= SMA20 (한 봉 목표); 조건 미충족; close=275.52, lower20=275.107, SMA20=276.469, previous_lower20=275.234 |
| v1 | donchian_20 | 9835.91 | -164.09 | sell /  / 종가 > 현재 봉을 제외한 직전 20봉 최고가; 조건 미충족; close=275.785, prior_high20=276.875 |
| v1 | atr_14_breakout | 9732.89 | -267.11 | sell /  / 종가 > 직전 종가 + 직전 ATR14 그리고 종가 > EMA26; 조건 미충족; close=276.06, threshold=277.643, prior_ATR14=0.662564, EMA26=276.447 |
| v1 | session_vwap | 9463.39 | -536.61 | buy /  / 종가 > 뉴욕 거래일별 누적 전형가격 VWAP; 조건 충족; close=275.85, session_VWAP=275.841, session_volume=1.504e+07 |
| v1 | obv_20 | 9715.63 | -284.37 | sell /  / OBV > OBV의 SMA20 그리고 종가 > EMA26; 조건 미충족; OBV=-1.90717e+07, OBV_SMA20=-1.99835e+07, close=275.747, EMA26=276.073 |
| v1 | stochastic_14_3_recovery | 9629.03 | -370.97 | sell /  / 직전 %K14 < 20에서 %K14가 %D3 상향 돌파 (한 봉 목표); 조건 미충족; K14=39.2924, D3=31.5748, previous_K14=36.5078, previous_D3=30.3985 |
| v1 | mfi_14_recovery | 9934.22 | -65.78 | sell /  / 직전 MFI14 < 20, 현재 MFI14 >= 20 (한 봉 목표); 조건 미충족; MFI14=34.131, previous_MFI14=22.0435 |
| v1 | adx_14_trend | 9726.05 | -273.95 | sell /  / Wilder ADX14 >= 25 그리고 +DI14 > -DI14; 조건 미충족; ADX14=27.8461, plus_DI14=25.882, minus_DI14=28.4558 |
| v1 | aroon_25_trend | 9745.85 | -254.15 | sell /  / Aroon25 Up > 70 그리고 Down < 30 (동률이면 최신 극값); 조건 미충족; Aroon_up=68, Aroon_down=4 |
| v1 | cci_20_momentum | 9825.51 | -174.49 | sell /  / CCI20 > 100 (전형가격·평균절대편차); 조건 미충족; CCI20=-152.101 |
| v1 | williams_14_recovery | 9757.64 | -242.36 | sell /  / 직전 Williams %R14 < -80, 현재 >= -80 (한 봉 목표); 조건 미충족; Williams_R14=-60.7076, previous_R14=-63.4922 |
| v1 | cmf_20_accumulation | 9709.11 | -290.89 | sell /  / Chaikin Money Flow20 > 0.1; 조건 미충족; CMF20=0.0178538, volume20=1.46976e+07 |
| v1 | chaikin_3_10 | 9562.84 | -437.16 | sell /  / ADL의 EMA3 - EMA10 > 0 그리고 종가 > EMA26; 조건 미충족; Chaikin3_10=145817, ADL=-3.25884e+07, close=275.747, EMA26=276.073 |
| v1 | roc_10_momentum | 9996.39 | -3.61 | sell /  / 10봉 ROC > 1% 그리고 종가 > EMA26; 조건 미충족; ROC10_percent=0.995963, close=275.315, EMA26=273.754 |
| v1 | trix_15_trend | 9811.92 | -188.08 | sell /  / 15봉 삼중 EMA의 1봉 변화율 TRIX > 0 그리고 종가 > EMA26; 조건 미충족; TRIX15_percent=0.00744142, close=276.06, EMA26=276.447 |
| v1 | keltner_20_breakout | 9879.23 | -120.77 | sell /  / 종가 > EMA20 + 2 x Wilder ATR14; 조건 미충족; close=276.4, upper_Keltner=277.094, EMA20=275.768, ATR14=0.662947 |
| v1 | opening_range_30m | 9963.15 | -36.85 | sell /  / 뉴욕 09:30·09:45 두 완료 봉 최고가를 10:00 이후 종가가 돌파; 자료 부족·변동폭 또는 거래량 없음: 대기; close=276.82 |
| v2 | cash | 10000.00 | 0.00 | 대기 /  / 새 신호 대기 |
| v2 | buy_hold | 9885.14 | -114.86 | buy / partial / 직전 완료 봉 목표 비중 100%; 다음 봉 시가 가정 |
| v2 | trend_8_26 | 9669.43 | -330.57 | sell / filled / 직전 완료 봉 목표 비중 0%; 다음 봉 시가 가정 |
| v2 | momentum_26 | 9661.30 | -338.70 | sell / filled / 직전 완료 봉 목표 비중 0%; 다음 봉 시가 가정 |
| v2 | breakout_8 | 8995.74 | -1004.26 | 중단: 손실 한도 / buy / partial / 직전 완료 봉 목표 비중 100%; 다음 봉 시가 가정 |
| v2 | reversion_12 | 9270.49 | -729.51 | sell / filled / 직전 완료 봉 목표 비중 0%; 다음 봉 시가 가정 |
| v2 | volume_26 | 9394.71 | -605.29 | sell / filled / 직전 완료 봉 목표 비중 0%; 다음 봉 시가 가정 |
| v2 | trend_8_26 AND momentum_26 | 9761.14 | -238.86 | sell / filled / 직전 완료 봉 목표 비중 0%; 다음 봉 시가 가정 |
| v2 | trend_8_26 + momentum_26 | 9685.93 | -314.07 | sell / filled / 직전 완료 봉 목표 비중 0%; 다음 봉 시가 가정 |
| v2 | trend_8_26 AND breakout_8 | 9402.34 | -597.66 | sell / filled / 직전 완료 봉 목표 비중 0%; 다음 봉 시가 가정 |
| v2 | trend_8_26 + breakout_8 | 9331.39 | -668.61 | sell / filled / 직전 완료 봉 목표 비중 0%; 다음 봉 시가 가정 |
| v2 | trend_8_26 AND reversion_12 | 9687.61 | -312.39 | sell / filled / 직전 완료 봉 목표 비중 0%; 다음 봉 시가 가정 |
| v2 | trend_8_26 + reversion_12 | 9467.49 | -532.51 | sell / filled / 직전 완료 봉 목표 비중 0%; 다음 봉 시가 가정 |
| v2 | trend_8_26 AND volume_26 | 9787.80 | -212.20 | sell / filled / 직전 완료 봉 목표 비중 0%; 다음 봉 시가 가정 |
| v2 | trend_8_26 + volume_26 | 9571.02 | -428.98 | sell / filled / 직전 완료 봉 목표 비중 0%; 다음 봉 시가 가정 |
| v2 | momentum_26 AND breakout_8 | 9347.05 | -652.95 | sell / filled / 직전 완료 봉 목표 비중 0%; 다음 봉 시가 가정 |
| v2 | momentum_26 + breakout_8 | 9327.31 | -672.69 | sell / filled / 직전 완료 봉 목표 비중 0%; 다음 봉 시가 가정 |
| v2 | momentum_26 AND reversion_12 | 9831.84 | -168.16 | sell / filled / 직전 완료 봉 목표 비중 0%; 다음 봉 시가 가정 |
| v2 | momentum_26 + reversion_12 | 9563.23 | -436.77 | sell / filled / 직전 완료 봉 목표 비중 0%; 다음 봉 시가 가정 |
| v2 | momentum_26 AND volume_26 | 9869.24 | -130.76 | sell / filled / 직전 완료 봉 목표 비중 0%; 다음 봉 시가 가정 |
| v2 | momentum_26 + volume_26 | 9566.89 | -433.11 | sell / filled / 직전 완료 봉 목표 비중 0%; 다음 봉 시가 가정 |
| v2 | breakout_8 AND reversion_12 | 10000.00 | 0.00 | 대기 /  / 새 신호 대기 |
| v2 | breakout_8 + reversion_12 | 9174.38 | -825.62 | sell / filled / 직전 완료 봉 목표 비중 0%; 다음 봉 시가 가정 |
| v2 | breakout_8 AND volume_26 | 9710.25 | -289.75 | sell / filled / 직전 완료 봉 목표 비중 0%; 다음 봉 시가 가정 |
| v2 | breakout_8 + volume_26 | 9216.75 | -783.25 | sell / filled / 직전 완료 봉 목표 비중 0%; 다음 봉 시가 가정 |
| v2 | reversion_12 AND volume_26 | 9674.16 | -325.84 | sell / filled / 직전 완료 봉 목표 비중 0%; 다음 봉 시가 가정 |
| v2 | reversion_12 + volume_26 | 9391.11 | -608.89 | sell / filled / 직전 완료 봉 목표 비중 0%; 다음 봉 시가 가정 |
| v2 | ema_12_26 | 9809.32 | -190.68 | sell / filled / EMA12 > EMA26; 조건 미충족; EMA12=276.256, EMA26=276.345; 직전 완료 봉 목표를 다음 봉 시가에 모의 적용 |
| v2 | macd_12_26_9 | 9900.47 | -99.53 | sell / filled / MACD > 신호선 그리고 MACD > 0; 조건 미충족; MACD=0.978353, signal9=1.01104; 직전 완료 봉 목표를 다음 봉 시가에 모의 적용 |
| v2 | rsi_14_recovery | 9779.12 | -220.88 | sell / filled / 직전 RSI14 < 30, 현재 RSI14 >= 30 (한 봉 목표); 조건 미충족; RSI14=46.986, previous_RSI14=37.1649; 직전 완료 봉 목표를 다음 봉 시가에 모의 적용 |
| v2 | bollinger_20_reentry | 9840.32 | -159.68 | sell / filled / 직전 종가 < 직전 하단밴드, 현재 하단밴드 <= 종가 <= SMA20 (한 봉 목표); 조건 미충족; close=275.52, lower20=275.107, SMA20=276.469, previous_lower20=275.234; 직전 완료 봉 목표를 다음 봉 시가에 모의 적용 |
| v2 | donchian_20 | 9830.01 | -169.99 | sell / filled / 종가 > 현재 봉을 제외한 직전 20봉 최고가; 조건 미충족; close=275.785, prior_high20=276.875; 직전 완료 봉 목표를 다음 봉 시가에 모의 적용 |
| v2 | atr_14_breakout | 9719.27 | -280.73 | sell / filled / 종가 > 직전 종가 + 직전 ATR14 그리고 종가 > EMA26; 조건 미충족; close=276.06, threshold=277.643, prior_ATR14=0.662564, EMA26=276.447; 직전 완료 봉 목표를 다음 봉 시가에 모의 적용 |
| v2 | session_vwap | 9437.87 | -562.13 | buy / partial / 종가 > 뉴욕 거래일별 누적 전형가격 VWAP; 조건 충족; close=275.85, session_VWAP=275.841, session_volume=1.504e+07; 직전 완료 봉 목표를 다음 봉 시가에 모의 적용 |
| v2 | obv_20 | 9702.04 | -297.96 | sell / filled / OBV > OBV의 SMA20 그리고 종가 > EMA26; 조건 미충족; OBV=-1.90717e+07, OBV_SMA20=-1.99835e+07, close=275.747, EMA26=276.073; 직전 완료 봉 목표를 다음 봉 시가에 모의 적용 |
| v2 | stochastic_14_3_recovery | 9611.71 | -388.29 | sell / filled / 직전 %K14 < 20에서 %K14가 %D3 상향 돌파 (한 봉 목표); 조건 미충족; K14=39.2924, D3=31.5748, previous_K14=36.5078, previous_D3=30.3985; 직전 완료 봉 목표를 다음 봉 시가에 모의 적용 |
| v2 | mfi_14_recovery | 9930.25 | -69.75 | sell / filled / 직전 MFI14 < 20, 현재 MFI14 >= 20 (한 봉 목표); 조건 미충족; MFI14=34.131, previous_MFI14=22.0435; 직전 완료 봉 목표를 다음 봉 시가에 모의 적용 |
| v2 | adx_14_trend | 9718.27 | -281.73 | sell / filled / Wilder ADX14 >= 25 그리고 +DI14 > -DI14; 조건 미충족; ADX14=27.8461, plus_DI14=25.882, minus_DI14=28.4558; 직전 완료 봉 목표를 다음 봉 시가에 모의 적용 |
| v2 | aroon_25_trend | 9736.11 | -263.89 | sell / filled / Aroon25 Up > 70 그리고 Down < 30 (동률이면 최신 극값); 조건 미충족; Aroon_up=68, Aroon_down=4; 직전 완료 봉 목표를 다음 봉 시가에 모의 적용 |
| v2 | cci_20_momentum | 9815.69 | -184.31 | sell / filled / CCI20 > 100 (전형가격·평균절대편차); 조건 미충족; CCI20=-152.101; 직전 완료 봉 목표를 다음 봉 시가에 모의 적용 |
| v2 | williams_14_recovery | 9743.99 | -256.01 | sell / filled / 직전 Williams %R14 < -80, 현재 >= -80 (한 봉 목표); 조건 미충족; Williams_R14=-60.7076, previous_R14=-63.4922; 직전 완료 봉 목표를 다음 봉 시가에 모의 적용 |
| v2 | cmf_20_accumulation | 9691.65 | -308.35 | sell / filled / Chaikin Money Flow20 > 0.1; 조건 미충족; CMF20=0.0178538, volume20=1.46976e+07; 직전 완료 봉 목표를 다음 봉 시가에 모의 적용 |
| v2 | chaikin_3_10 | 9543.74 | -456.26 | sell / filled / ADL의 EMA3 - EMA10 > 0 그리고 종가 > EMA26; 조건 미충족; Chaikin3_10=145817, ADL=-3.25884e+07, close=275.747, EMA26=276.073; 직전 완료 봉 목표를 다음 봉 시가에 모의 적용 |
| v2 | roc_10_momentum | 9994.39 | -5.61 | sell / filled / 10봉 ROC > 1% 그리고 종가 > EMA26; 조건 미충족; ROC10_percent=0.995963, close=275.315, EMA26=273.754; 직전 완료 봉 목표를 다음 봉 시가에 모의 적용 |
| v2 | trix_15_trend | 9804.07 | -195.93 | sell / filled / 15봉 삼중 EMA의 1봉 변화율 TRIX > 0 그리고 종가 > EMA26; 조건 미충족; TRIX15_percent=0.00744142, close=276.06, EMA26=276.447; 직전 완료 봉 목표를 다음 봉 시가에 모의 적용 |
| v2 | keltner_20_breakout | 9873.30 | -126.70 | sell / filled / 종가 > EMA20 + 2 x Wilder ATR14; 조건 미충족; close=276.4, upper_Keltner=277.094, EMA20=275.768, ATR14=0.662947; 직전 완료 봉 목표를 다음 봉 시가에 모의 적용 |
| v2 | opening_range_30m | 9959.17 | -40.83 | sell / filled / 뉴욕 09:30·09:45 두 완료 봉 최고가를 10:00 이후 종가가 돌파; 자료 부족·변동폭 또는 거래량 없음: 대기; close=276.82; 직전 완료 봉 목표를 다음 봉 시가에 모의 적용 |

### 같은 기간의 비용·노출 비교 (사후 연구)

| 전략 | 비용 전 | 비용 후 | 100% 보유 | 같은 평균 노출 보유 | 평균 노출 |
|---|---:|---:|---:|---:|---:|
| cash | 0.00% | 0.00% | -2.70% | -0.00% | 0.00% |
| buy_hold | -2.30% | -2.70% | -2.70% | -2.70% | 100.00% |
| trend_8_26 | -1.05% | -4.32% | -2.70% | -1.34% | 48.95% |
| momentum_26 | 0.01% | -4.91% | -2.70% | -1.29% | 47.12% |
| breakout_8 | -0.92% | -15.54% | -2.70% | -0.55% | 19.90% |
| reversion_12 | -0.85% | -12.59% | -2.70% | -0.73% | 26.70% |
| volume_26 | -0.50% | -7.75% | -2.70% | -0.23% | 8.38% |
| trend_8_26 AND momentum_26 | 0.05% | -3.26% | -2.70% | -1.13% | 41.36% |
| trend_8_26 + momentum_26 | -0.52% | -4.21% | -2.70% | -1.31% | 48.04% |
| trend_8_26 AND breakout_8 | -0.23% | -9.42% | -2.70% | -0.37% | 13.35% |
| trend_8_26 + breakout_8 | -0.98% | -9.91% | -2.70% | -0.94% | 34.43% |
| trend_8_26 AND reversion_12 | -0.50% | -4.60% | -2.70% | -0.15% | 5.50% |
| trend_8_26 + reversion_12 | -0.94% | -8.56% | -2.70% | -1.04% | 37.83% |
| trend_8_26 AND volume_26 | -0.37% | -3.25% | -2.70% | -0.07% | 2.36% |
| trend_8_26 + volume_26 | -0.77% | -5.66% | -2.70% | -0.79% | 28.67% |
| momentum_26 AND breakout_8 | 0.22% | -9.39% | -2.70% | -0.36% | 13.09% |
| momentum_26 + breakout_8 | -0.45% | -10.19% | -2.70% | -0.92% | 33.51% |
| momentum_26 AND reversion_12 | -0.09% | -2.98% | -2.70% | -0.08% | 2.88% |
| momentum_26 + reversion_12 | -0.41% | -7.49% | -2.70% | -1.01% | 36.92% |
| momentum_26 AND volume_26 | 0.01% | -2.89% | -2.70% | -0.07% | 2.36% |
| momentum_26 + volume_26 | -0.24% | -5.75% | -2.70% | -0.76% | 27.75% |
| breakout_8 AND reversion_12 | 0.00% | 0.00% | -2.70% | -0.00% | 0.00% |
| breakout_8 + reversion_12 | -0.88% | -13.36% | -2.70% | -0.64% | 23.31% |
| breakout_8 AND volume_26 | -0.54% | -3.42% | -2.70% | -0.06% | 2.09% |
| breakout_8 + volume_26 | -0.71% | -11.36% | -2.70% | -0.39% | 14.14% |
| reversion_12 AND volume_26 | 0.60% | -3.54% | -2.70% | -0.09% | 3.40% |
| reversion_12 + volume_26 | -0.67% | -9.45% | -2.70% | -0.48% | 17.55% |
| ema_12_26 | 0.17% | -2.32% | -2.70% | -1.36% | 49.74% |
| macd_12_26_9 | 2.01% | -0.53% | -2.70% | -0.71% | 25.65% |
| rsi_14_recovery | -0.88% | -4.95% | -2.70% | -0.07% | 2.62% |
| bollinger_20_reentry | -0.20% | -4.70% | -2.70% | -0.08% | 2.88% |
| donchian_20 | -0.04% | -4.96% | -2.70% | -0.16% | 5.76% |
| atr_14_breakout | -0.63% | -7.48% | -2.70% | -0.13% | 4.71% |
| session_vwap | -1.31% | -13.00% | -2.70% | -1.26% | 46.07% |
| obv_20 | -0.41% | -5.31% | -2.70% | -1.20% | 43.72% |
| stochastic_14_3_recovery | -0.30% | -12.47% | -2.70% | -0.22% | 8.12% |
| mfi_14_recovery | 0.20% | -3.92% | -2.70% | -0.07% | 2.62% |
| adx_14_trend | -0.12% | -3.02% | -2.70% | -0.94% | 34.29% |
| aroon_25_trend | -0.68% | -4.77% | -2.70% | -0.57% | 20.68% |
| cci_20_momentum | -0.99% | -7.42% | -2.70% | -0.54% | 19.63% |
| williams_14_recovery | 0.41% | -9.22% | -2.70% | -0.17% | 6.28% |
| cmf_20_accumulation | 0.32% | -6.20% | -2.70% | -0.63% | 23.04% |
| chaikin_3_10 | -1.47% | -8.64% | -2.70% | -0.94% | 34.29% |
| roc_10_momentum | -0.02% | -1.27% | -2.70% | -0.14% | 4.97% |
| trix_15_trend | -0.01% | -3.72% | -2.70% | -1.09% | 39.79% |
| keltner_20_breakout | -0.10% | -3.40% | -2.70% | -0.20% | 7.33% |
| opening_range_30m | 1.53% | -2.64% | -2.70% | -0.65% | 23.56% |

동일 구간·초기 자금, 종료 시 청산 비용 포함. 노출 맞춤은 사후 설명용이며 v2 실제 계좌 성과가 아닙니다.
[낙폭 분해·비용 영향·전체 구간](IWM/comparison.json)

[v1 전체 기록](IWM/accounts.json) · [v2 전체 기록](IWM/accounts-v2.json)

## DIA 계좌

| 모델 | 전략 | 평가액 USD | 손익 USD | 최근 매매·이유 |
|---|---|---:|---:|---|
| v1 | cash | 10000.00 | 0.00 | 대기 /  / 새 신호 대기 |
| v1 | buy_hold | 10056.38 | 56.38 | buy /  / buy_hold: prior completed bar target 100%; next bar open simulation |
| v1 | trend_8_26 | 9962.94 | -37.06 | buy /  / trend_8_26: prior completed bar target 100%; next bar open simulation |
| v1 | momentum_26 | 9806.20 | -193.80 | buy /  / momentum_26: prior completed bar target 100%; next bar open simulation |
| v1 | breakout_8 | 9378.75 | -621.25 | sell /  / breakout_8: prior completed bar target 0%; next bar open simulation |
| v1 | reversion_12 | 9822.56 | -177.44 | sell /  / reversion_12: prior completed bar target 0%; next bar open simulation |
| v1 | volume_26 | 9816.03 | -183.97 | sell /  / volume_26: prior completed bar target 0%; next bar open simulation |
| v1 | trend_8_26 AND momentum_26 | 9803.04 | -196.96 | buy /  / trend_8_26 AND momentum_26: prior completed bar target 100%; next bar open simulation |
| v1 | trend_8_26 + momentum_26 | 9884.34 | -115.66 | buy /  / trend_8_26 + momentum_26: prior completed bar target 100%; next bar open simulation |
| v1 | trend_8_26 AND breakout_8 | 9649.65 | -350.35 | sell /  / trend_8_26 AND breakout_8: prior completed bar target 0%; next bar open simulation |
| v1 | trend_8_26 + breakout_8 | 9724.62 | -275.38 | sell /  / trend_8_26 + breakout_8: prior completed bar target 50%; next bar open simulation |
| v1 | trend_8_26 AND reversion_12 | 9865.72 | -134.28 | sell /  / trend_8_26 AND reversion_12: prior completed bar target 0%; next bar open simulation |
| v1 | trend_8_26 + reversion_12 | 9892.28 | -107.72 | sell /  / trend_8_26 + reversion_12: prior completed bar target 50%; next bar open simulation |
| v1 | trend_8_26 AND volume_26 | 9888.21 | -111.79 | sell /  / trend_8_26 AND volume_26: prior completed bar target 0%; next bar open simulation |
| v1 | trend_8_26 + volume_26 | 9889.00 | -111.00 | sell /  / trend_8_26 + volume_26: prior completed bar target 50%; next bar open simulation |
| v1 | momentum_26 AND breakout_8 | 9506.61 | -493.39 | sell /  / momentum_26 AND breakout_8: prior completed bar target 0%; next bar open simulation |
| v1 | momentum_26 + breakout_8 | 9590.20 | -409.80 | sell /  / momentum_26 + breakout_8: prior completed bar target 50%; next bar open simulation |
| v1 | momentum_26 AND reversion_12 | 9865.74 | -134.26 | sell /  / momentum_26 AND reversion_12: prior completed bar target 0%; next bar open simulation |
| v1 | momentum_26 + reversion_12 | 9853.46 | -146.54 | sell /  / momentum_26 + reversion_12: prior completed bar target 50%; next bar open simulation |
| v1 | momentum_26 AND volume_26 | 9805.85 | -194.15 | sell /  / momentum_26 AND volume_26: prior completed bar target 0%; next bar open simulation |
| v1 | momentum_26 + volume_26 | 9830.62 | -169.38 | sell /  / momentum_26 + volume_26: prior completed bar target 50%; next bar open simulation |
| v1 | breakout_8 AND reversion_12 | 10000.00 | 0.00 | 대기 /  / 새 신호 대기 |
| v1 | breakout_8 + reversion_12 | 9617.07 | -382.93 | sell /  / breakout_8 + reversion_12: prior completed bar target 0%; next bar open simulation |
| v1 | breakout_8 AND volume_26 | 9925.92 | -74.08 | sell /  / breakout_8 AND volume_26: prior completed bar target 0%; next bar open simulation |
| v1 | breakout_8 + volume_26 | 9633.26 | -366.74 | sell /  / breakout_8 + volume_26: prior completed bar target 0%; next bar open simulation |
| v1 | reversion_12 AND volume_26 | 9970.42 | -29.58 | sell /  / reversion_12 AND volume_26: prior completed bar target 0%; next bar open simulation |
| v1 | reversion_12 + volume_26 | 9858.49 | -141.51 | sell /  / reversion_12 + volume_26: prior completed bar target 0%; next bar open simulation |
| v1 | ema_12_26 | 9910.35 | -89.65 | buy /  / EMA12 > EMA26; 조건 충족; EMA12=519.74, EMA26=519.585 |
| v1 | macd_12_26_9 | 9801.13 | -198.87 | sell /  / MACD > 신호선 그리고 MACD > 0; 조건 미충족; MACD=0.355602, signal9=0.37454 |
| v1 | rsi_14_recovery | 10000.00 | 0.00 | 대기 /  / 새 신호 대기 |
| v1 | bollinger_20_reentry | 9939.81 | -60.19 | sell /  / 직전 종가 < 직전 하단밴드, 현재 하단밴드 <= 종가 <= SMA20 (한 봉 목표); 조건 미충족; close=525.81, lower20=524.898, SMA20=526.51, previous_lower20=524.945 |
| v1 | donchian_20 | 9675.11 | -324.89 | sell /  / 종가 > 현재 봉을 제외한 직전 20봉 최고가; 조건 미충족; close=526.71, prior_high20=528.45 |
| v1 | atr_14_breakout | 9709.35 | -290.65 | sell /  / 종가 > 직전 종가 + 직전 ATR14 그리고 종가 > EMA26; 조건 미충족; close=527.625, threshold=528.531, prior_ATR14=1.00085, EMA26=526.218 |
| v1 | session_vwap | 9799.30 | -200.70 | buy /  / 종가 > 뉴욕 거래일별 누적 전형가격 VWAP; 조건 충족; close=526.37, session_VWAP=526.232, session_volume=1.64733e+06 |
| v1 | obv_20 | 9851.67 | -148.33 | sell /  / OBV > OBV의 SMA20 그리고 종가 > EMA26; 조건 미충족; OBV=-5.81025e+06, OBV_SMA20=-5.32802e+06, close=526.941, EMA26=526.147 |
| v1 | stochastic_14_3_recovery | 9702.74 | -297.26 | sell /  / 직전 %K14 < 20에서 %K14가 %D3 상향 돌파 (한 봉 목표); 조건 미충족; K14=43.4299, D3=31.8109, previous_K14=42.0016, previous_D3=18.964 |
| v1 | mfi_14_recovery | 9902.01 | -97.99 | sell /  / 직전 MFI14 < 20, 현재 MFI14 >= 20 (한 봉 목표); 조건 미충족; MFI14=29.4378, previous_MFI14=21.6288 |
| v1 | adx_14_trend | 9711.49 | -288.51 | sell /  / Wilder ADX14 >= 25 그리고 +DI14 > -DI14; 조건 미충족; ADX14=28.0997, plus_DI14=30.0206, minus_DI14=36.1913 |
| v1 | aroon_25_trend | 9820.69 | -179.31 | sell /  / Aroon25 Up > 70 그리고 Down < 30 (동률이면 최신 극값); 조건 미충족; Aroon_up=72, Aroon_down=92 |
| v1 | cci_20_momentum | 9758.00 | -242.00 | sell /  / CCI20 > 100 (전형가격·평균절대편차); 조건 미충족; CCI20=65.0571 |
| v1 | williams_14_recovery | 9735.64 | -264.36 | sell /  / 직전 Williams %R14 < -80, 현재 >= -80 (한 봉 목표); 조건 미충족; Williams_R14=-56.5701, previous_R14=-57.9984 |
| v1 | cmf_20_accumulation | 9581.29 | -418.71 | buy /  / Chaikin Money Flow20 > 0.1; 조건 충족; CMF20=0.162227, volume20=1.04086e+06 |
| v1 | chaikin_3_10 | 9762.41 | -237.59 | buy /  / ADL의 EMA3 - EMA10 > 0 그리고 종가 > EMA26; 조건 충족; Chaikin3_10=80194.1, ADL=-1.15132e+07, close=527.11, EMA26=526.511 |
| v1 | roc_10_momentum | 9939.01 | -60.99 | sell /  / 10봉 ROC > 1% 그리고 종가 > EMA26; 조건 미충족; ROC10_percent=0.771645, close=523.68, EMA26=521.367 |
| v1 | trix_15_trend | 9895.01 | -104.99 | buy /  / 15봉 삼중 EMA의 1봉 변화율 TRIX > 0 그리고 종가 > EMA26; 조건 충족; TRIX15_percent=0.00948861, close=527.11, EMA26=526.511 |
| v1 | keltner_20_breakout | 9826.82 | -173.18 | sell /  / 종가 > EMA20 + 2 x Wilder ATR14; 조건 미충족; close=526.34, upper_Keltner=527.991, EMA20=526.293, ATR14=0.848911 |
| v1 | opening_range_30m | 9583.64 | -416.36 | sell /  / 뉴욕 09:30·09:45 두 완료 봉 최고가를 10:00 이후 종가가 돌파; 조건 미충족; close=526.71, opening_high=527.34 |
| v2 | cash | 10000.00 | 0.00 | 대기 /  / 새 신호 대기 |
| v2 | buy_hold | 10180.96 | 180.96 | buy / partial / 직전 완료 봉 목표 비중 100%; 다음 봉 시가 가정 |
| v2 | trend_8_26 | 9892.46 | -107.54 | buy / partial / 직전 완료 봉 목표 비중 100%; 다음 봉 시가 가정 |
| v2 | momentum_26 | 9839.95 | -160.05 | buy / partial / 직전 완료 봉 목표 비중 100%; 다음 봉 시가 가정 |
| v2 | breakout_8 | 9011.37 | -988.63 | 중단: 손실 한도 / buy / partial / 직전 완료 봉 목표 비중 100%; 다음 봉 시가 가정 |
| v2 | reversion_12 | 9514.52 | -485.48 | sell / filled / 직전 완료 봉 목표 비중 0%; 다음 봉 시가 가정 |
| v2 | volume_26 | 9526.08 | -473.92 | sell / filled / 직전 완료 봉 목표 비중 0%; 다음 봉 시가 가정 |
| v2 | trend_8_26 AND momentum_26 | 9830.25 | -169.75 | buy / partial / 직전 완료 봉 목표 비중 100%; 다음 봉 시가 가정 |
| v2 | trend_8_26 + momentum_26 | 9866.32 | -133.68 | buy / partial / 직전 완료 봉 목표 비중 100%; 다음 봉 시가 가정 |
| v2 | trend_8_26 AND breakout_8 | 9330.55 | -669.45 | sell / filled / 직전 완료 봉 목표 비중 0%; 다음 봉 시가 가정 |
| v2 | trend_8_26 + breakout_8 | 9447.17 | -552.83 | sell / filled / 직전 완료 봉 목표 비중 50%; 다음 봉 시가 가정 |
| v2 | trend_8_26 AND reversion_12 | 9669.36 | -330.64 | sell / filled / 직전 완료 봉 목표 비중 0%; 다음 봉 시가 가정 |
| v2 | trend_8_26 + reversion_12 | 9701.16 | -298.84 | sell / filled / 직전 완료 봉 목표 비중 50%; 다음 봉 시가 가정 |
| v2 | trend_8_26 AND volume_26 | 9738.93 | -261.07 | sell / filled / 직전 완료 봉 목표 비중 0%; 다음 봉 시가 가정 |
| v2 | trend_8_26 + volume_26 | 9727.67 | -272.33 | sell / filled / 직전 완료 봉 목표 비중 50%; 다음 봉 시가 가정 |
| v2 | momentum_26 AND breakout_8 | 9178.11 | -821.89 | sell / filled / 직전 완료 봉 목표 비중 0%; 다음 봉 시가 가정 |
| v2 | momentum_26 + breakout_8 | 9363.04 | -636.96 | sell / filled / 직전 완료 봉 목표 비중 50%; 다음 봉 시가 가정 |
| v2 | momentum_26 AND reversion_12 | 9814.45 | -185.55 | sell / filled / 직전 완료 봉 목표 비중 0%; 다음 봉 시가 가정 |
| v2 | momentum_26 + reversion_12 | 9716.14 | -283.86 | sell / filled / 직전 완료 봉 목표 비중 50%; 다음 봉 시가 가정 |
| v2 | momentum_26 AND volume_26 | 9589.81 | -410.19 | sell / filled / 직전 완료 봉 목표 비중 0%; 다음 봉 시가 가정 |
| v2 | momentum_26 + volume_26 | 9742.86 | -257.14 | sell / filled / 직전 완료 봉 목표 비중 50%; 다음 봉 시가 가정 |
| v2 | breakout_8 AND reversion_12 | 10000.00 | 0.00 | 대기 /  / 새 신호 대기 |
| v2 | breakout_8 + reversion_12 | 9225.36 | -774.64 | sell / filled / 직전 완료 봉 목표 비중 0%; 다음 봉 시가 가정 |
| v2 | breakout_8 AND volume_26 | 9718.15 | -281.85 | sell / filled / 직전 완료 봉 목표 비중 0%; 다음 봉 시가 가정 |
| v2 | breakout_8 + volume_26 | 9250.79 | -749.21 | sell / filled / 직전 완료 봉 목표 비중 0%; 다음 봉 시가 가정 |
| v2 | reversion_12 AND volume_26 | 9966.44 | -33.56 | sell / filled / 직전 완료 봉 목표 비중 0%; 다음 봉 시가 가정 |
| v2 | reversion_12 + volume_26 | 9559.93 | -440.07 | sell / filled / 직전 완료 봉 목표 비중 0%; 다음 봉 시가 가정 |
| v2 | ema_12_26 | 9905.40 | -94.60 | buy / partial / EMA12 > EMA26; 조건 충족; EMA12=519.74, EMA26=519.585; 직전 완료 봉 목표를 다음 봉 시가에 모의 적용 |
| v2 | macd_12_26_9 | 9791.33 | -208.67 | sell / filled / MACD > 신호선 그리고 MACD > 0; 조건 미충족; MACD=0.355602, signal9=0.37454; 직전 완료 봉 목표를 다음 봉 시가에 모의 적용 |
| v2 | rsi_14_recovery | 10000.00 | 0.00 | 대기 /  / 새 신호 대기 |
| v2 | bollinger_20_reentry | 9935.84 | -64.16 | sell / filled / 직전 종가 < 직전 하단밴드, 현재 하단밴드 <= 종가 <= SMA20 (한 봉 목표); 조건 미충족; close=525.81, lower20=524.898, SMA20=526.51, previous_lower20=524.945; 직전 완료 봉 목표를 다음 봉 시가에 모의 적용 |
| v2 | donchian_20 | 9661.57 | -338.43 | sell / filled / 종가 > 현재 봉을 제외한 직전 20봉 최고가; 조건 미충족; close=526.71, prior_high20=528.45; 직전 완료 봉 목표를 다음 봉 시가에 모의 적용 |
| v2 | atr_14_breakout | 9693.83 | -306.17 | sell / filled / 종가 > 직전 종가 + 직전 ATR14 그리고 종가 > EMA26; 조건 미충족; close=527.625, threshold=528.531, prior_ATR14=1.00085, EMA26=526.218; 직전 완료 봉 목표를 다음 봉 시가에 모의 적용 |
| v2 | session_vwap | 9786.57 | -213.43 | buy / partial / 종가 > 뉴욕 거래일별 누적 전형가격 VWAP; 조건 충족; close=526.37, session_VWAP=526.232, session_volume=1.64733e+06; 직전 완료 봉 목표를 다음 봉 시가에 모의 적용 |
| v2 | obv_20 | 9841.82 | -158.18 | sell / filled / OBV > OBV의 SMA20 그리고 종가 > EMA26; 조건 미충족; OBV=-5.81025e+06, OBV_SMA20=-5.32802e+06, close=526.941, EMA26=526.147; 직전 완료 봉 목표를 다음 봉 시가에 모의 적용 |
| v2 | stochastic_14_3_recovery | 9687.23 | -312.77 | sell / filled / 직전 %K14 < 20에서 %K14가 %D3 상향 돌파 (한 봉 목표); 조건 미충족; K14=43.4299, D3=31.8109, previous_K14=42.0016, previous_D3=18.964; 직전 완료 봉 목표를 다음 봉 시가에 모의 적용 |
| v2 | mfi_14_recovery | 9896.07 | -103.93 | sell / filled / 직전 MFI14 < 20, 현재 MFI14 >= 20 (한 봉 목표); 조건 미충족; MFI14=29.4378, previous_MFI14=21.6288; 직전 완료 봉 목표를 다음 봉 시가에 모의 적용 |
| v2 | adx_14_trend | 9701.78 | -298.22 | sell / filled / Wilder ADX14 >= 25 그리고 +DI14 > -DI14; 조건 미충족; ADX14=28.0997, plus_DI14=30.0206, minus_DI14=36.1913; 직전 완료 봉 목표를 다음 봉 시가에 모의 적용 |
| v2 | aroon_25_trend | 9810.88 | -189.12 | sell / filled / Aroon25 Up > 70 그리고 Down < 30 (동률이면 최신 극값); 조건 미충족; Aroon_up=72, Aroon_down=92; 직전 완료 봉 목표를 다음 봉 시가에 모의 적용 |
| v2 | cci_20_momentum | 9744.35 | -255.65 | sell / filled / CCI20 > 100 (전형가격·평균절대편차); 조건 미충족; CCI20=65.0571; 직전 완료 봉 목표를 다음 봉 시가에 모의 적용 |
| v2 | williams_14_recovery | 9722.02 | -277.98 | sell / filled / 직전 Williams %R14 < -80, 현재 >= -80 (한 봉 목표); 조건 미충족; Williams_R14=-56.5701, previous_R14=-57.9984; 직전 완료 봉 목표를 다음 봉 시가에 모의 적용 |
| v2 | cmf_20_accumulation | 9563.11 | -436.89 | buy / partial / Chaikin Money Flow20 > 0.1; 조건 충족; CMF20=0.162227, volume20=1.04086e+06; 직전 완료 봉 목표를 다음 봉 시가에 모의 적용 |
| v2 | chaikin_3_10 | 9749.73 | -250.27 | buy / partial / ADL의 EMA3 - EMA10 > 0 그리고 종가 > EMA26; 조건 충족; Chaikin3_10=80194.1, ADL=-1.15132e+07, close=527.11, EMA26=526.511; 직전 완료 봉 목표를 다음 봉 시가에 모의 적용 |
| v2 | roc_10_momentum | 9937.03 | -62.97 | sell / filled / 10봉 ROC > 1% 그리고 종가 > EMA26; 조건 미충족; ROC10_percent=0.771645, close=523.68, EMA26=521.367; 직전 완료 봉 목표를 다음 봉 시가에 모의 적용 |
| v2 | trix_15_trend | 9888.09 | -111.91 | buy / partial / 15봉 삼중 EMA의 1봉 변화율 TRIX > 0 그리고 종가 > EMA26; 조건 충족; TRIX15_percent=0.00948861, close=527.11, EMA26=526.511; 직전 완료 봉 목표를 다음 봉 시가에 모의 적용 |
| v2 | keltner_20_breakout | 9817.00 | -183.00 | sell / filled / 종가 > EMA20 + 2 x Wilder ATR14; 조건 미충족; close=526.34, upper_Keltner=527.991, EMA20=526.293, ATR14=0.848911; 직전 완료 봉 목표를 다음 봉 시가에 모의 적용 |
| v2 | opening_range_30m | 9566.41 | -433.59 | sell / filled / 뉴욕 09:30·09:45 두 완료 봉 최고가를 10:00 이후 종가가 돌파; 조건 미충족; close=526.71, opening_high=527.34; 직전 완료 봉 목표를 다음 봉 시가에 모의 적용 |

### 같은 기간의 비용·노출 비교 (사후 연구)

| 전략 | 비용 전 | 비용 후 | 100% 보유 | 같은 평균 노출 보유 | 평균 노출 |
|---|---:|---:|---:|---:|---:|
| cash | 0.00% | 0.00% | 2.37% | 0.00% | 0.00% |
| buy_hold | 2.80% | 2.37% | 2.37% | 2.37% | 100.00% |
| trend_8_26 | 2.42% | -1.79% | 2.37% | 1.58% | 67.02% |
| momentum_26 | 1.43% | -3.15% | 2.37% | 1.54% | 65.45% |
| breakout_8 | -0.38% | -18.23% | 2.37% | 0.62% | 26.18% |
| reversion_12 | 0.92% | -6.82% | 2.37% | 0.42% | 17.80% |
| volume_26 | 0.99% | -8.31% | 2.37% | 0.24% | 10.21% |
| trend_8_26 AND momentum_26 | 2.82% | -2.23% | 2.37% | 1.38% | 58.64% |
| trend_8_26 + momentum_26 | 1.93% | -2.47% | 2.37% | 1.56% | 66.23% |
| trend_8_26 AND breakout_8 | 0.69% | -12.71% | 2.37% | 0.44% | 18.85% |
| trend_8_26 + breakout_8 | 1.01% | -9.63% | 2.37% | 1.10% | 46.60% |
| trend_8_26 AND reversion_12 | 0.81% | -4.55% | 2.37% | 0.17% | 7.07% |
| trend_8_26 + reversion_12 | 1.67% | -4.15% | 2.37% | 1.00% | 42.41% |
| trend_8_26 AND volume_26 | 1.59% | -4.61% | 2.37% | 0.15% | 6.28% |
| trend_8_26 + volume_26 | 1.70% | -4.92% | 2.37% | 0.91% | 38.62% |
| momentum_26 AND breakout_8 | -0.10% | -14.48% | 2.37% | 0.50% | 21.20% |
| momentum_26 + breakout_8 | 0.53% | -11.00% | 2.37% | 1.08% | 45.82% |
| momentum_26 AND reversion_12 | 0.10% | -3.21% | 2.37% | 0.13% | 5.50% |
| momentum_26 + reversion_12 | 1.18% | -4.21% | 2.37% | 0.98% | 41.63% |
| momentum_26 AND volume_26 | 0.04% | -6.85% | 2.37% | 0.15% | 6.54% |
| momentum_26 + volume_26 | 1.21% | -5.17% | 2.37% | 0.89% | 37.83% |
| breakout_8 AND reversion_12 | 0.00% | 0.00% | 2.37% | 0.00% | 0.00% |
| breakout_8 + reversion_12 | 0.27% | -12.36% | 2.37% | 0.52% | 22.00% |
| breakout_8 AND volume_26 | -0.27% | -4.37% | 2.37% | 0.09% | 3.66% |
| breakout_8 + volume_26 | 0.30% | -12.50% | 2.37% | 0.43% | 18.20% |
| reversion_12 AND volume_26 | 0.94% | -1.99% | 2.37% | 0.05% | 2.09% |
| reversion_12 + volume_26 | 0.95% | -7.19% | 2.37% | 0.33% | 14.01% |
| ema_12_26 | 1.32% | -1.20% | 2.37% | 1.54% | 65.45% |
| macd_12_26_9 | 2.09% | -2.11% | 2.37% | 0.81% | 34.29% |
| rsi_14_recovery | 0.14% | -0.69% | 2.37% | 0.01% | 0.52% |
| bollinger_20_reentry | 0.35% | -2.56% | 2.37% | 0.04% | 1.83% |
| donchian_20 | 0.06% | -8.39% | 2.37% | 0.26% | 11.26% |
| atr_14_breakout | -0.46% | -9.25% | 2.37% | 0.16% | 6.81% |
| session_vwap | 1.95% | -5.47% | 2.37% | 1.39% | 58.90% |
| obv_20 | 0.96% | -6.39% | 2.37% | 1.19% | 50.52% |
| stochastic_14_3_recovery | 1.36% | -9.12% | 2.37% | 0.16% | 6.81% |
| mfi_14_recovery | 0.37% | -2.95% | 2.37% | 0.05% | 2.09% |
| adx_14_trend | -0.02% | -4.14% | 2.37% | 0.79% | 33.51% |
| aroon_25_trend | 1.33% | -2.84% | 2.37% | 0.70% | 29.84% |
| cci_20_momentum | 1.15% | -5.82% | 2.37% | 0.70% | 29.58% |
| williams_14_recovery | 1.55% | -5.85% | 2.37% | 0.11% | 4.71% |
| cmf_20_accumulation | 1.11% | -8.58% | 2.37% | 0.98% | 41.62% |
| chaikin_3_10 | 1.58% | -8.16% | 2.37% | 1.31% | 55.76% |
| roc_10_momentum | -0.07% | -0.90% | 2.37% | 0.05% | 2.09% |
| trix_15_trend | 1.06% | -3.10% | 2.37% | 1.38% | 58.38% |
| keltner_20_breakout | 0.79% | -6.94% | 2.37% | 0.47% | 20.16% |
| opening_range_30m | 1.19% | -6.18% | 2.37% | 0.76% | 32.46% |

동일 구간·초기 자금, 종료 시 청산 비용 포함. 노출 맞춤은 사후 설명용이며 v2 실제 계좌 성과가 아닙니다.
[낙폭 분해·비용 영향·전체 구간](DIA/comparison.json)

[v1 전체 기록](DIA/accounts.json) · [v2 전체 기록](DIA/accounts-v2.json)

## MSFT 계좌

| 모델 | 전략 | 평가액 USD | 손익 USD | 최근 매매·이유 |
|---|---|---:|---:|---|
| v1 | cash | 10000.00 | 0.00 | 대기 /  / 새 신호 대기 |
| v1 | buy_hold | 9658.90 | -341.10 | buy /  / buy_hold: prior completed bar target 100%; next bar open simulation |
| v1 | trend_8_26 | 9433.22 | -566.78 | sell /  / trend_8_26: prior completed bar target 0%; next bar open simulation |
| v1 | momentum_26 | 9297.87 | -702.13 | sell /  / momentum_26: prior completed bar target 0%; next bar open simulation |
| v1 | breakout_8 | 9511.89 | -488.11 | sell /  / breakout_8: prior completed bar target 0%; next bar open simulation |
| v1 | reversion_12 | 9407.10 | -592.90 | buy /  / reversion_12: prior completed bar target 100%; next bar open simulation |
| v1 | volume_26 | 9623.19 | -376.81 | sell /  / volume_26: prior completed bar target 0%; next bar open simulation |
| v1 | trend_8_26 AND momentum_26 | 9427.87 | -572.13 | sell /  / trend_8_26 AND momentum_26: prior completed bar target 0%; next bar open simulation |
| v1 | trend_8_26 + momentum_26 | 9402.84 | -597.16 | sell /  / trend_8_26 + momentum_26: prior completed bar target 0%; next bar open simulation |
| v1 | trend_8_26 AND breakout_8 | 9678.51 | -321.49 | sell /  / trend_8_26 AND breakout_8: prior completed bar target 0%; next bar open simulation |
| v1 | trend_8_26 + breakout_8 | 9510.67 | -489.33 | sell /  / trend_8_26 + breakout_8: prior completed bar target 0%; next bar open simulation |
| v1 | trend_8_26 AND reversion_12 | 9519.35 | -480.65 | sell /  / trend_8_26 AND reversion_12: prior completed bar target 0%; next bar open simulation |
| v1 | trend_8_26 + reversion_12 | 9438.88 | -561.12 | sell /  / trend_8_26 + reversion_12: prior completed bar target 50%; next bar open simulation |
| v1 | trend_8_26 AND volume_26 | 9802.11 | -197.89 | sell /  / trend_8_26 AND volume_26: prior completed bar target 0%; next bar open simulation |
| v1 | trend_8_26 + volume_26 | 9527.85 | -472.15 | sell /  / trend_8_26 + volume_26: prior completed bar target 0%; next bar open simulation |
| v1 | momentum_26 AND breakout_8 | 9642.25 | -357.75 | sell /  / momentum_26 AND breakout_8: prior completed bar target 0%; next bar open simulation |
| v1 | momentum_26 + breakout_8 | 9423.30 | -576.70 | sell /  / momentum_26 + breakout_8: prior completed bar target 0%; next bar open simulation |
| v1 | momentum_26 AND reversion_12 | 9649.76 | -350.24 | sell /  / momentum_26 AND reversion_12: prior completed bar target 0%; next bar open simulation |
| v1 | momentum_26 + reversion_12 | 9408.45 | -591.55 | sell /  / momentum_26 + reversion_12: prior completed bar target 50%; next bar open simulation |
| v1 | momentum_26 AND volume_26 | 9830.16 | -169.84 | sell /  / momentum_26 AND volume_26: prior completed bar target 0%; next bar open simulation |
| v1 | momentum_26 + volume_26 | 9478.30 | -521.70 | sell /  / momentum_26 + volume_26: prior completed bar target 0%; next bar open simulation |
| v1 | breakout_8 AND reversion_12 | 10000.00 | 0.00 | 대기 /  / 새 신호 대기 |
| v1 | breakout_8 + reversion_12 | 9497.04 | -502.96 | sell /  / breakout_8 + reversion_12: prior completed bar target 50%; next bar open simulation |
| v1 | breakout_8 AND volume_26 | 9953.19 | -46.81 | sell /  / breakout_8 AND volume_26: prior completed bar target 0%; next bar open simulation |
| v1 | breakout_8 + volume_26 | 9605.54 | -394.46 | sell /  / breakout_8 + volume_26: prior completed bar target 0%; next bar open simulation |
| v1 | reversion_12 AND volume_26 | 9770.39 | -229.61 | sell /  / reversion_12 AND volume_26: prior completed bar target 0%; next bar open simulation |
| v1 | reversion_12 + volume_26 | 9533.47 | -466.53 | sell /  / reversion_12 + volume_26: prior completed bar target 50%; next bar open simulation |
| v1 | ema_12_26 | 9491.42 | -508.58 | sell /  / EMA12 > EMA26; 조건 미충족; EMA12=531.766, EMA26=531.788 |
| v1 | macd_12_26_9 | 9603.93 | -396.07 | sell /  / MACD > 신호선 그리고 MACD > 0; 조건 미충족; MACD=-0.0222122, signal9=0.149678 |
| v1 | rsi_14_recovery | 9932.10 | -67.90 | sell /  / 직전 RSI14 < 30, 현재 RSI14 >= 30 (한 봉 목표); 조건 미충족; RSI14=39.2066, previous_RSI14=35.1952 |
| v1 | bollinger_20_reentry | 9789.12 | -210.88 | sell /  / 직전 종가 < 직전 하단밴드, 현재 하단밴드 <= 종가 <= SMA20 (한 봉 목표); 조건 미충족; close=526.675, lower20=523.276, SMA20=530.073, previous_lower20=523.675 |
| v1 | donchian_20 | 9912.16 | -87.84 | sell /  / 종가 > 현재 봉을 제외한 직전 20봉 최고가; 조건 미충족; close=534.52, prior_high20=535.44 |
| v1 | atr_14_breakout | 9915.10 | -84.90 | sell /  / 종가 > 직전 종가 + 직전 ATR14 그리고 종가 > EMA26; 조건 미충족; close=533.975, threshold=536.307, prior_ATR14=2.16203, EMA26=530.521 |
| v1 | session_vwap | 9580.74 | -419.26 | sell /  / 종가 > 뉴욕 거래일별 누적 전형가격 VWAP; 조건 미충족; close=524.28, session_VWAP=524.818, session_volume=2.2268e+07 |
| v1 | obv_20 | 9537.51 | -462.49 | sell /  / OBV > OBV의 SMA20 그리고 종가 > EMA26; 조건 미충족; OBV=5.91823e+07, OBV_SMA20=5.93103e+07, close=529.54, EMA26=531.788 |
| v1 | stochastic_14_3_recovery | 9731.13 | -268.87 | sell /  / 직전 %K14 < 20에서 %K14가 %D3 상향 돌파 (한 봉 목표); 조건 미충족; K14=35.5998, D3=27.8717, previous_K14=31.4616, previous_D3=23.8817 |
| v1 | mfi_14_recovery | 9972.58 | -27.42 | sell /  / 직전 MFI14 < 20, 현재 MFI14 >= 20 (한 봉 목표); 조건 미충족; MFI14=53.413, previous_MFI14=44.3372 |
| v1 | adx_14_trend | 9883.62 | -116.38 | sell /  / Wilder ADX14 >= 25 그리고 +DI14 > -DI14; 조건 미충족; ADX14=23.6824, plus_DI14=22.3066, minus_DI14=19.9214 |
| v1 | aroon_25_trend | 9616.60 | -383.40 | sell /  / Aroon25 Up > 70 그리고 Down < 30 (동률이면 최신 극값); 조건 미충족; Aroon_up=96, Aroon_down=100 |
| v1 | cci_20_momentum | 9912.64 | -87.36 | sell /  / CCI20 > 100 (전형가격·평균절대편차); 조건 미충족; CCI20=96.8192 |
| v1 | williams_14_recovery | 9670.32 | -329.68 | sell /  / 직전 Williams %R14 < -80, 현재 >= -80 (한 봉 목표); 조건 미충족; Williams_R14=-64.4002, previous_R14=-68.5384 |
| v1 | cmf_20_accumulation | 9579.01 | -420.99 | sell /  / Chaikin Money Flow20 > 0.1; 조건 미충족; CMF20=-0.038027, volume20=2.32417e+07 |
| v1 | chaikin_3_10 | 9575.46 | -424.54 | sell /  / ADL의 EMA3 - EMA10 > 0 그리고 종가 > EMA26; 조건 미충족; Chaikin3_10=-50549, ADL=1.1482e+08, close=529.54, EMA26=531.788 |
| v1 | roc_10_momentum | 9959.43 | -40.57 | sell /  / 10봉 ROC > 1% 그리고 종가 > EMA26; 조건 미충족; ROC10_percent=0.454191, close=534.125, EMA26=532.186 |
| v1 | trix_15_trend | 9557.09 | -442.91 | sell /  / 15봉 삼중 EMA의 1봉 변화율 TRIX > 0 그리고 종가 > EMA26; 조건 미충족; TRIX15_percent=0.00481299, close=529.54, EMA26=531.788 |
| v1 | keltner_20_breakout | 9958.78 | -41.22 | sell /  / 종가 > EMA20 + 2 x Wilder ATR14; 조건 미충족; close=533.975, upper_Keltner=534.357, EMA20=530.111, ATR14=2.12332 |
| v1 | opening_range_30m | 9589.30 | -410.70 | sell /  / 뉴욕 09:30·09:45 두 완료 봉 최고가를 10:00 이후 종가가 돌파; 자료 부족·변동폭 또는 거래량 없음: 대기; close=529.54 |
| v2 | cash | 10000.00 | 0.00 | 대기 /  / 새 신호 대기 |
| v2 | buy_hold | 9711.60 | -288.40 | buy / partial / 직전 완료 봉 목표 비중 100%; 다음 봉 시가 가정 |
| v2 | trend_8_26 | 9366.79 | -633.21 | sell / filled / 직전 완료 봉 목표 비중 0%; 다음 봉 시가 가정 |
| v2 | momentum_26 | 9327.21 | -672.79 | sell / filled / 직전 완료 봉 목표 비중 0%; 다음 봉 시가 가정 |
| v2 | breakout_8 | 9298.81 | -701.19 | sell / filled / 직전 완료 봉 목표 비중 0%; 다음 봉 시가 가정 |
| v2 | reversion_12 | 9031.15 | -968.85 | buy / partial / 직전 완료 봉 목표 비중 100%; 다음 봉 시가 가정 |
| v2 | volume_26 | 9304.84 | -695.16 | sell / filled / 직전 완료 봉 목표 비중 0%; 다음 봉 시가 가정 |
| v2 | trend_8_26 AND momentum_26 | 9320.43 | -679.57 | sell / filled / 직전 완료 봉 목표 비중 0%; 다음 봉 시가 가정 |
| v2 | trend_8_26 + momentum_26 | 9386.57 | -613.43 | sell / filled / 직전 완료 봉 목표 비중 0%; 다음 봉 시가 가정 |
| v2 | trend_8_26 AND breakout_8 | 9318.21 | -681.79 | sell / filled / 직전 완료 봉 목표 비중 0%; 다음 봉 시가 가정 |
| v2 | trend_8_26 + breakout_8 | 9392.14 | -607.86 | sell / filled / 직전 완료 봉 목표 비중 0%; 다음 봉 시가 가정 |
| v2 | trend_8_26 AND reversion_12 | 9411.07 | -588.93 | sell / filled / 직전 완료 봉 목표 비중 0%; 다음 봉 시가 가정 |
| v2 | trend_8_26 + reversion_12 | 9216.32 | -783.68 | sell / filled / 직전 완료 봉 목표 비중 50%; 다음 봉 시가 가정 |
| v2 | trend_8_26 AND volume_26 | 9743.99 | -256.01 | sell / filled / 직전 완료 봉 목표 비중 0%; 다음 봉 시가 가정 |
| v2 | trend_8_26 + volume_26 | 9355.31 | -644.69 | sell / filled / 직전 완료 봉 목표 비중 0%; 다음 봉 시가 가정 |
| v2 | momentum_26 AND breakout_8 | 9430.77 | -569.23 | sell / filled / 직전 완료 봉 목표 비중 0%; 다음 봉 시가 가정 |
| v2 | momentum_26 + breakout_8 | 9332.85 | -667.15 | sell / filled / 직전 완료 봉 목표 비중 0%; 다음 봉 시가 가정 |
| v2 | momentum_26 AND reversion_12 | 9475.12 | -524.88 | sell / filled / 직전 완료 봉 목표 비중 0%; 다음 봉 시가 가정 |
| v2 | momentum_26 + reversion_12 | 9235.61 | -764.39 | sell / filled / 직전 완료 봉 목표 비중 50%; 다음 봉 시가 가정 |
| v2 | momentum_26 AND volume_26 | 9695.84 | -304.16 | sell / filled / 직전 완료 봉 목표 비중 0%; 다음 봉 시가 가정 |
| v2 | momentum_26 + volume_26 | 9355.39 | -644.61 | sell / filled / 직전 완료 봉 목표 비중 0%; 다음 봉 시가 가정 |
| v2 | breakout_8 AND reversion_12 | 10000.00 | 0.00 | 대기 /  / 새 신호 대기 |
| v2 | breakout_8 + reversion_12 | 9221.46 | -778.54 | sell / filled / 직전 완료 봉 목표 비중 50%; 다음 봉 시가 가정 |
| v2 | breakout_8 AND volume_26 | 9890.09 | -109.91 | sell / filled / 직전 완료 봉 목표 비중 0%; 다음 봉 시가 가정 |
| v2 | breakout_8 + volume_26 | 9360.45 | -639.55 | sell / filled / 직전 완료 봉 목표 비중 0%; 다음 봉 시가 가정 |
| v2 | reversion_12 AND volume_26 | 9528.36 | -471.64 | sell / filled / 직전 완료 봉 목표 비중 0%; 다음 봉 시가 가정 |
| v2 | reversion_12 + volume_26 | 9185.96 | -814.04 | sell / filled / 직전 완료 봉 목표 비중 50%; 다음 봉 시가 가정 |
| v2 | ema_12_26 | 9483.83 | -516.17 | sell / filled / EMA12 > EMA26; 조건 미충족; EMA12=531.766, EMA26=531.788; 직전 완료 봉 목표를 다음 봉 시가에 모의 적용 |
| v2 | macd_12_26_9 | 9594.34 | -405.66 | sell / filled / MACD > 신호선 그리고 MACD > 0; 조건 미충족; MACD=-0.0222122, signal9=0.149678; 직전 완료 봉 목표를 다음 봉 시가에 모의 적용 |
| v2 | rsi_14_recovery | 9924.16 | -75.84 | sell / filled / 직전 RSI14 < 30, 현재 RSI14 >= 30 (한 봉 목표); 조건 미충족; RSI14=39.2066, previous_RSI14=35.1952; 직전 완료 봉 목표를 다음 봉 시가에 모의 적용 |
| v2 | bollinger_20_reentry | 9779.33 | -220.67 | sell / filled / 직전 종가 < 직전 하단밴드, 현재 하단밴드 <= 종가 <= SMA20 (한 봉 목표); 조건 미충족; close=526.675, lower20=523.276, SMA20=530.073, previous_lower20=523.675; 직전 완료 봉 목표를 다음 봉 시가에 모의 적용 |
| v2 | donchian_20 | 9908.19 | -91.81 | sell / filled / 종가 > 현재 봉을 제외한 직전 20봉 최고가; 조건 미충족; close=534.52, prior_high20=535.44; 직전 완료 봉 목표를 다음 봉 시가에 모의 적용 |
| v2 | atr_14_breakout | 9911.14 | -88.86 | sell / filled / 종가 > 직전 종가 + 직전 ATR14 그리고 종가 > EMA26; 조건 미충족; close=533.975, threshold=536.307, prior_ATR14=2.16203, EMA26=530.521; 직전 완료 봉 목표를 다음 봉 시가에 모의 적용 |
| v2 | session_vwap | 9565.42 | -434.58 | sell / filled / 종가 > 뉴욕 거래일별 누적 전형가격 VWAP; 조건 미충족; close=524.28, session_VWAP=524.818, session_volume=2.2268e+07; 직전 완료 봉 목표를 다음 봉 시가에 모의 적용 |
| v2 | obv_20 | 9520.36 | -479.64 | sell / filled / OBV > OBV의 SMA20 그리고 종가 > EMA26; 조건 미충족; OBV=5.91823e+07, OBV_SMA20=5.93103e+07, close=529.54, EMA26=531.788; 직전 완료 봉 목표를 다음 봉 시가에 모의 적용 |
| v2 | stochastic_14_3_recovery | 9715.58 | -284.42 | sell / filled / 직전 %K14 < 20에서 %K14가 %D3 상향 돌파 (한 봉 목표); 조건 미충족; K14=35.5998, D3=27.8717, previous_K14=31.4616, previous_D3=23.8817; 직전 완료 봉 목표를 다음 봉 시가에 모의 적용 |
| v2 | mfi_14_recovery | 9968.59 | -31.41 | sell / filled / 직전 MFI14 < 20, 현재 MFI14 >= 20 (한 봉 목표); 조건 미충족; MFI14=53.413, previous_MFI14=44.3372; 직전 완료 봉 목표를 다음 봉 시가에 모의 적용 |
| v2 | adx_14_trend | 9879.67 | -120.33 | sell / filled / Wilder ADX14 >= 25 그리고 +DI14 > -DI14; 조건 미충족; ADX14=23.6824, plus_DI14=22.3066, minus_DI14=19.9214; 직전 완료 봉 목표를 다음 봉 시가에 모의 적용 |
| v2 | aroon_25_trend | 9608.91 | -391.09 | sell / filled / Aroon25 Up > 70 그리고 Down < 30 (동률이면 최신 극값); 조건 미충족; Aroon_up=96, Aroon_down=100; 직전 완료 봉 목표를 다음 봉 시가에 모의 적용 |
| v2 | cci_20_momentum | 9906.70 | -93.30 | sell / filled / CCI20 > 100 (전형가격·평균절대편차); 조건 미충족; CCI20=96.8192; 직전 완료 봉 목표를 다음 봉 시가에 모의 적용 |
| v2 | williams_14_recovery | 9654.86 | -345.14 | sell / filled / 직전 Williams %R14 < -80, 현재 >= -80 (한 봉 목표); 조건 미충족; Williams_R14=-64.4002, previous_R14=-68.5384; 직전 완료 봉 목표를 다음 봉 시가에 모의 적용 |
| v2 | cmf_20_accumulation | 9569.43 | -430.57 | sell / filled / Chaikin Money Flow20 > 0.1; 조건 미충족; CMF20=-0.038027, volume20=2.32417e+07; 직전 완료 봉 목표를 다음 봉 시가에 모의 적용 |
| v2 | chaikin_3_10 | 9560.15 | -439.85 | sell / filled / ADL의 EMA3 - EMA10 > 0 그리고 종가 > EMA26; 조건 미충족; Chaikin3_10=-50549, ADL=1.1482e+08, close=529.54, EMA26=531.788; 직전 완료 봉 목표를 다음 봉 시가에 모의 적용 |
| v2 | roc_10_momentum | 9957.44 | -42.56 | sell / filled / 10봉 ROC > 1% 그리고 종가 > EMA26; 조건 미충족; ROC10_percent=0.454191, close=534.125, EMA26=532.186; 직전 완료 봉 목표를 다음 봉 시가에 모의 적용 |
| v2 | trix_15_trend | 9549.45 | -450.55 | sell / filled / 15봉 삼중 EMA의 1봉 변화율 TRIX > 0 그리고 종가 > EMA26; 조건 미충족; TRIX15_percent=0.00481299, close=529.54, EMA26=531.788; 직전 완료 봉 목표를 다음 봉 시가에 모의 적용 |
| v2 | keltner_20_breakout | 9956.78 | -43.22 | sell / filled / 종가 > EMA20 + 2 x Wilder ATR14; 조건 미충족; close=533.975, upper_Keltner=534.357, EMA20=530.111, ATR14=2.12332; 직전 완료 봉 목표를 다음 봉 시가에 모의 적용 |
| v2 | opening_range_30m | 9581.64 | -418.36 | sell / filled / 뉴욕 09:30·09:45 두 완료 봉 최고가를 10:00 이후 종가가 돌파; 자료 부족·변동폭 또는 거래량 없음: 대기; close=529.54; 직전 완료 봉 목표를 다음 봉 시가에 모의 적용 |

### 같은 기간의 비용·노출 비교 (사후 연구)

| 전략 | 비용 전 | 비용 후 | 100% 보유 | 같은 평균 노출 보유 | 평균 노출 |
|---|---:|---:|---:|---:|---:|
| cash | 0.00% | 0.00% | 0.45% | 0.00% | 0.00% |
| buy_hold | 0.88% | 0.45% | 0.45% | 0.45% | 100.00% |
| trend_8_26 | -2.92% | -6.52% | 0.45% | 0.26% | 57.59% |
| momentum_26 | -1.02% | -8.23% | 0.45% | 0.26% | 56.81% |
| breakout_8 | 5.86% | -8.61% | 0.45% | 0.09% | 20.16% |
| reversion_12 | -5.50% | -14.56% | 0.45% | 0.11% | 25.39% |
| volume_26 | 0.86% | -8.43% | 0.45% | 0.04% | 9.16% |
| trend_8_26 AND momentum_26 | -2.66% | -8.98% | 0.45% | 0.23% | 50.52% |
| trend_8_26 + momentum_26 | -1.97% | -6.98% | 0.45% | 0.26% | 57.20% |
| trend_8_26 AND breakout_8 | -0.15% | -10.48% | 0.45% | 0.06% | 12.57% |
| trend_8_26 + breakout_8 | 1.39% | -6.98% | 0.45% | 0.17% | 38.88% |
| trend_8_26 AND reversion_12 | -2.62% | -8.95% | 0.45% | 0.03% | 7.59% |
| trend_8_26 + reversion_12 | -4.20% | -10.26% | 0.45% | 0.19% | 41.50% |
| trend_8_26 AND volume_26 | 2.03% | -1.75% | 0.45% | 0.01% | 3.14% |
| trend_8_26 + volume_26 | -1.04% | -7.09% | 0.45% | 0.15% | 33.38% |
| momentum_26 AND breakout_8 | 2.14% | -8.81% | 0.45% | 0.06% | 13.09% |
| momentum_26 + breakout_8 | 2.37% | -7.84% | 0.45% | 0.17% | 38.49% |
| momentum_26 AND reversion_12 | -3.22% | -9.51% | 0.45% | 0.04% | 9.16% |
| momentum_26 + reversion_12 | -3.27% | -10.89% | 0.45% | 0.18% | 41.10% |
| momentum_26 AND volume_26 | 1.17% | -3.40% | 0.45% | 0.02% | 3.40% |
| momentum_26 + volume_26 | -0.07% | -7.75% | 0.45% | 0.15% | 32.99% |
| breakout_8 AND reversion_12 | 0.00% | 0.00% | 0.45% | 0.00% | 0.00% |
| breakout_8 + reversion_12 | 0.04% | -10.71% | 0.45% | 0.10% | 22.78% |
| breakout_8 AND volume_26 | 2.04% | -0.50% | 0.45% | 0.01% | 1.83% |
| breakout_8 + volume_26 | 3.34% | -7.75% | 0.45% | 0.07% | 14.67% |
| reversion_12 AND volume_26 | -2.90% | -7.29% | 0.45% | 0.02% | 4.19% |
| reversion_12 + volume_26 | -2.36% | -11.36% | 0.45% | 0.08% | 17.28% |
| ema_12_26 | -2.02% | -5.26% | 0.45% | 0.26% | 56.81% |
| macd_12_26_9 | -1.89% | -7.10% | 0.45% | 0.15% | 33.77% |
| rsi_14_recovery | 0.46% | -2.45% | 0.45% | 0.01% | 1.83% |
| bollinger_20_reentry | -0.59% | -3.87% | 0.45% | 0.01% | 2.09% |
| donchian_20 | 1.05% | -4.32% | 0.45% | 0.02% | 4.19% |
| atr_14_breakout | 1.62% | -2.97% | 0.45% | 0.01% | 3.14% |
| session_vwap | 4.64% | -4.20% | 0.45% | 0.21% | 46.86% |
| obv_20 | 4.83% | -4.02% | 0.45% | 0.23% | 50.52% |
| stochastic_14_3_recovery | -0.02% | -9.61% | 0.45% | 0.03% | 6.28% |
| mfi_14_recovery | 1.84% | -1.53% | 0.45% | 0.01% | 2.09% |
| adx_14_trend | 4.03% | 1.87% | 0.45% | 0.20% | 43.46% |
| aroon_25_trend | -1.70% | -6.53% | 0.45% | 0.10% | 23.04% |
| cci_20_momentum | 2.85% | -3.43% | 0.45% | 0.09% | 20.94% |
| williams_14_recovery | -1.14% | -9.87% | 0.45% | 0.03% | 5.76% |
| cmf_20_accumulation | 0.22% | -6.30% | 0.45% | 0.19% | 42.15% |
| chaikin_3_10 | 3.75% | -4.21% | 0.45% | 0.22% | 48.69% |
| roc_10_momentum | -0.61% | -4.30% | 0.45% | 0.06% | 13.09% |
| trix_15_trend | -1.48% | -5.53% | 0.45% | 0.20% | 44.24% |
| keltner_20_breakout | 0.49% | -4.45% | 0.45% | 0.05% | 11.52% |
| opening_range_30m | -1.39% | -5.05% | 0.45% | 0.09% | 20.68% |

동일 구간·초기 자금, 종료 시 청산 비용 포함. 노출 맞춤은 사후 설명용이며 v2 실제 계좌 성과가 아닙니다.
[낙폭 분해·비용 영향·전체 구간](MSFT/comparison.json)

[v1 전체 기록](MSFT/accounts.json) · [v2 전체 기록](MSFT/accounts-v2.json)

## JPM 계좌

| 모델 | 전략 | 평가액 USD | 손익 USD | 최근 매매·이유 |
|---|---|---:|---:|---|
| v1 | cash | 10000.00 | 0.00 | 대기 /  / 새 신호 대기 |
| v1 | buy_hold | 9824.72 | -175.28 | buy /  / buy_hold: prior completed bar target 100%; next bar open simulation |
| v1 | trend_8_26 | 9685.05 | -314.95 | buy /  / trend_8_26: prior completed bar target 100%; next bar open simulation |
| v1 | momentum_26 | 9372.05 | -627.95 | buy /  / momentum_26: prior completed bar target 100%; next bar open simulation |
| v1 | breakout_8 | 9582.11 | -417.89 | sell /  / breakout_8: prior completed bar target 0%; next bar open simulation |
| v1 | reversion_12 | 9549.62 | -450.38 | sell /  / reversion_12: prior completed bar target 0%; next bar open simulation |
| v1 | volume_26 | 9920.77 | -79.23 | sell /  / volume_26: prior completed bar target 0%; next bar open simulation |
| v1 | trend_8_26 AND momentum_26 | 9566.53 | -433.47 | buy /  / trend_8_26 AND momentum_26: prior completed bar target 100%; next bar open simulation |
| v1 | trend_8_26 + momentum_26 | 9527.38 | -472.62 | buy /  / trend_8_26 + momentum_26: prior completed bar target 100%; next bar open simulation |
| v1 | trend_8_26 AND breakout_8 | 9808.13 | -191.87 | sell /  / trend_8_26 AND breakout_8: prior completed bar target 0%; next bar open simulation |
| v1 | trend_8_26 + breakout_8 | 9672.07 | -327.93 | sell /  / trend_8_26 + breakout_8: prior completed bar target 50%; next bar open simulation |
| v1 | trend_8_26 AND reversion_12 | 9757.16 | -242.84 | sell /  / trend_8_26 AND reversion_12: prior completed bar target 0%; next bar open simulation |
| v1 | trend_8_26 + reversion_12 | 9616.95 | -383.05 | sell /  / trend_8_26 + reversion_12: prior completed bar target 50%; next bar open simulation |
| v1 | trend_8_26 AND volume_26 | 10103.61 | 103.61 | sell /  / trend_8_26 AND volume_26: prior completed bar target 0%; next bar open simulation |
| v1 | trend_8_26 + volume_26 | 9802.03 | -197.97 | sell /  / trend_8_26 + volume_26: prior completed bar target 50%; next bar open simulation |
| v1 | momentum_26 AND breakout_8 | 9597.01 | -402.99 | sell /  / momentum_26 AND breakout_8: prior completed bar target 0%; next bar open simulation |
| v1 | momentum_26 + breakout_8 | 9476.61 | -523.39 | sell /  / momentum_26 + breakout_8: prior completed bar target 50%; next bar open simulation |
| v1 | momentum_26 AND reversion_12 | 9788.16 | -211.84 | sell /  / momentum_26 AND reversion_12: prior completed bar target 0%; next bar open simulation |
| v1 | momentum_26 + reversion_12 | 9555.33 | -444.67 | sell /  / momentum_26 + reversion_12: prior completed bar target 50%; next bar open simulation |
| v1 | momentum_26 AND volume_26 | 9926.98 | -73.02 | sell /  / momentum_26 AND volume_26: prior completed bar target 0%; next bar open simulation |
| v1 | momentum_26 + volume_26 | 9681.09 | -318.91 | sell /  / momentum_26 + volume_26: prior completed bar target 50%; next bar open simulation |
| v1 | breakout_8 AND reversion_12 | 10000.00 | 0.00 | 대기 /  / 새 신호 대기 |
| v1 | breakout_8 + reversion_12 | 9604.00 | -396.00 | sell /  / breakout_8 + reversion_12: prior completed bar target 0%; next bar open simulation |
| v1 | breakout_8 AND volume_26 | 10054.69 | 54.69 | sell /  / breakout_8 AND volume_26: prior completed bar target 0%; next bar open simulation |
| v1 | breakout_8 + volume_26 | 9769.49 | -230.51 | sell /  / breakout_8 + volume_26: prior completed bar target 0%; next bar open simulation |
| v1 | reversion_12 AND volume_26 | 9940.10 | -59.90 | sell /  / reversion_12 AND volume_26: prior completed bar target 0%; next bar open simulation |
| v1 | reversion_12 + volume_26 | 9772.29 | -227.71 | sell /  / reversion_12 + volume_26: prior completed bar target 0%; next bar open simulation |
| v1 | ema_12_26 | 9555.69 | -444.31 | buy /  / EMA12 > EMA26; 조건 충족; EMA12=334.525, EMA26=334.523 |
| v1 | macd_12_26_9 | 9637.66 | -362.34 | buy /  / MACD > 신호선 그리고 MACD > 0; 조건 충족; MACD=0.00168375, signal9=-0.0492443 |
| v1 | rsi_14_recovery | 9986.37 | -13.63 | sell /  / 직전 RSI14 < 30, 현재 RSI14 >= 30 (한 봉 목표); 조건 미충족; RSI14=61.6663, previous_RSI14=57.046 |
| v1 | bollinger_20_reentry | 9848.44 | -151.56 | sell /  / 직전 종가 < 직전 하단밴드, 현재 하단밴드 <= 종가 <= SMA20 (한 봉 목표); 조건 미충족; close=334.49, lower20=332.961, SMA20=334.508, previous_lower20=332.957 |
| v1 | donchian_20 | 9792.78 | -207.22 | sell /  / 종가 > 현재 봉을 제외한 직전 20봉 최고가; 조건 미충족; close=335.915, prior_high20=336.169 |
| v1 | atr_14_breakout | 9691.73 | -308.27 | sell /  / 종가 > 직전 종가 + 직전 ATR14 그리고 종가 > EMA26; 조건 미충족; close=335.21, threshold=335.598, prior_ATR14=1.10843, EMA26=334.445 |
| v1 | session_vwap | 9569.85 | -430.15 | buy /  / 종가 > 뉴욕 거래일별 누적 전형가격 VWAP; 조건 충족; close=334.909, session_VWAP=334.399, session_volume=2.0782e+06 |
| v1 | obv_20 | 9737.13 | -262.87 | buy /  / OBV > OBV의 SMA20 그리고 종가 > EMA26; 조건 충족; OBV=-2.01293e+07, OBV_SMA20=-2.02067e+07, close=334.909, EMA26=334.523 |
| v1 | stochastic_14_3_recovery | 9574.52 | -425.48 | sell /  / 직전 %K14 < 20에서 %K14가 %D3 상향 돌파 (한 봉 목표); 조건 미충족; K14=53.9297, D3=28.1336, previous_K14=24.5463, previous_D3=18.2988 |
| v1 | mfi_14_recovery | 9935.64 | -64.36 | sell /  / 직전 MFI14 < 20, 현재 MFI14 >= 20 (한 봉 목표); 조건 미충족; MFI14=30.2719, previous_MFI14=26.8492 |
| v1 | adx_14_trend | 9726.68 | -273.32 | sell /  / Wilder ADX14 >= 25 그리고 +DI14 > -DI14; 조건 미충족; ADX14=23.9395, plus_DI14=23.2021, minus_DI14=22.594 |
| v1 | aroon_25_trend | 9824.71 | -175.29 | sell /  / Aroon25 Up > 70 그리고 Down < 30 (동률이면 최신 극값); 조건 미충족; Aroon_up=68, Aroon_down=16 |
| v1 | cci_20_momentum | 9810.74 | -189.26 | sell /  / CCI20 > 100 (전형가격·평균절대편차); 조건 미충족; CCI20=57.5465 |
| v1 | williams_14_recovery | 9567.46 | -432.54 | sell /  / 직전 Williams %R14 < -80, 현재 >= -80 (한 봉 목표); 조건 미충족; Williams_R14=-46.0703, previous_R14=-75.4537 |
| v1 | cmf_20_accumulation | 9797.76 | -202.24 | buy /  / Chaikin Money Flow20 > 0.1; 조건 충족; CMF20=0.131084, volume20=2.22061e+06 |
| v1 | chaikin_3_10 | 9684.95 | -315.05 | buy /  / ADL의 EMA3 - EMA10 > 0 그리고 종가 > EMA26; 조건 충족; Chaikin3_10=31581, ADL=-9.75237e+06, close=334.909, EMA26=334.523 |
| v1 | roc_10_momentum | 9836.40 | -163.60 | sell /  / 10봉 ROC > 1% 그리고 종가 > EMA26; 조건 미충족; ROC10_percent=0.964142, close=337.72, EMA26=336.695 |
| v1 | trix_15_trend | 9723.73 | -276.27 | sell /  / 15봉 삼중 EMA의 1봉 변화율 TRIX > 0 그리고 종가 > EMA26; 조건 미충족; TRIX15_percent=0.0135144, close=337.6, EMA26=338.759 |
| v1 | keltner_20_breakout | 9905.24 | -94.76 | sell /  / 종가 > EMA20 + 2 x Wilder ATR14; 조건 미충족; close=339.04, upper_Keltner=339.281, EMA20=336.559, ATR14=1.36146 |
| v1 | opening_range_30m | 9850.26 | -149.74 | sell /  / 뉴욕 09:30·09:45 두 완료 봉 최고가를 10:00 이후 종가가 돌파; 조건 미충족; close=337.72, opening_high=339.035 |
| v2 | cash | 10000.00 | 0.00 | 대기 /  / 새 신호 대기 |
| v2 | buy_hold | 9988.88 | -11.12 | buy / partial / 직전 완료 봉 목표 비중 100%; 다음 봉 시가 가정 |
| v2 | trend_8_26 | 9687.17 | -312.83 | buy / partial / 직전 완료 봉 목표 비중 100%; 다음 봉 시가 가정 |
| v2 | momentum_26 | 9130.47 | -869.53 | 중단: 손실 한도 / buy / partial / 직전 완료 봉 목표 비중 100%; 다음 봉 시가 가정 |
| v2 | breakout_8 | 8999.42 | -1000.58 | 중단: 손실 한도 / buy / partial / 직전 완료 봉 목표 비중 100%; 다음 봉 시가 가정 |
| v2 | reversion_12 | 9515.28 | -484.72 | sell / filled / 직전 완료 봉 목표 비중 0%; 다음 봉 시가 가정 |
| v2 | volume_26 | 9737.15 | -262.85 | sell / filled / 직전 완료 봉 목표 비중 0%; 다음 봉 시가 가정 |
| v2 | trend_8_26 AND momentum_26 | 9523.64 | -476.36 | buy / partial / 직전 완료 봉 목표 비중 100%; 다음 봉 시가 가정 |
| v2 | trend_8_26 + momentum_26 | 9301.08 | -698.92 | buy / partial / 직전 완료 봉 목표 비중 100%; 다음 봉 시가 가정 |
| v2 | trend_8_26 AND breakout_8 | 9181.63 | -818.37 | sell / filled / 직전 완료 봉 목표 비중 0%; 다음 봉 시가 가정 |
| v2 | trend_8_26 + breakout_8 | 9338.87 | -661.13 | sell / filled / 직전 완료 봉 목표 비중 50%; 다음 봉 시가 가정 |
| v2 | trend_8_26 AND reversion_12 | 9729.48 | -270.52 | sell / filled / 직전 완료 봉 목표 비중 0%; 다음 봉 시가 가정 |
| v2 | trend_8_26 + reversion_12 | 9641.28 | -358.72 | sell / filled / 직전 완료 봉 목표 비중 50%; 다음 봉 시가 가정 |
| v2 | trend_8_26 AND volume_26 | 9897.88 | -102.12 | sell / filled / 직전 완료 봉 목표 비중 0%; 다음 봉 시가 가정 |
| v2 | trend_8_26 + volume_26 | 9712.76 | -287.24 | sell / filled / 직전 완료 봉 목표 비중 50%; 다음 봉 시가 가정 |
| v2 | momentum_26 AND breakout_8 | 8951.57 | -1048.43 | 중단: 손실 한도 / buy / partial / 직전 완료 봉 목표 비중 100%; 다음 봉 시가 가정 |
| v2 | momentum_26 + breakout_8 | 8995.36 | -1004.64 | 중단: 손실 한도 / sell / filled / 직전 완료 봉 목표 비중 0%; 다음 봉 시가 가정 |
| v2 | momentum_26 AND reversion_12 | 9730.22 | -269.78 | sell / filled / 직전 완료 봉 목표 비중 0%; 다음 봉 시가 가정 |
| v2 | momentum_26 + reversion_12 | 9413.54 | -586.46 | sell / filled / 직전 완료 봉 목표 비중 50%; 다음 봉 시가 가정 |
| v2 | momentum_26 AND volume_26 | 9724.84 | -275.16 | sell / filled / 직전 완료 봉 목표 비중 0%; 다음 봉 시가 가정 |
| v2 | momentum_26 + volume_26 | 9404.22 | -595.78 | sell / filled / 직전 완료 봉 목표 비중 50%; 다음 봉 시가 가정 |
| v2 | breakout_8 AND reversion_12 | 10000.00 | 0.00 | 대기 /  / 새 신호 대기 |
| v2 | breakout_8 + reversion_12 | 9293.56 | -706.44 | sell / filled / 직전 완료 봉 목표 비중 0%; 다음 봉 시가 가정 |
| v2 | breakout_8 AND volume_26 | 9941.48 | -58.52 | sell / filled / 직전 완료 봉 목표 비중 0%; 다음 봉 시가 가정 |
| v2 | breakout_8 + volume_26 | 9362.03 | -637.97 | sell / filled / 직전 완료 봉 목표 비중 0%; 다음 봉 시가 가정 |
| v2 | reversion_12 AND volume_26 | 9987.18 | -12.82 | sell / filled / 직전 완료 봉 목표 비중 0%; 다음 봉 시가 가정 |
| v2 | reversion_12 + volume_26 | 9686.50 | -313.50 | sell / filled / 직전 완료 봉 목표 비중 0%; 다음 봉 시가 가정 |
| v2 | ema_12_26 | 9547.10 | -452.90 | buy / partial / EMA12 > EMA26; 조건 충족; EMA12=334.525, EMA26=334.523; 직전 완료 봉 목표를 다음 봉 시가에 모의 적용 |
| v2 | macd_12_26_9 | 9629.00 | -371.00 | buy / partial / MACD > 신호선 그리고 MACD > 0; 조건 충족; MACD=0.00168375, signal9=-0.0492443; 직전 완료 봉 목표를 다음 봉 시가에 모의 적용 |
| v2 | rsi_14_recovery | 9984.37 | -15.63 | sell / filled / 직전 RSI14 < 30, 현재 RSI14 >= 30 (한 봉 목표); 조건 미충족; RSI14=61.6663, previous_RSI14=57.046; 직전 완료 봉 목표를 다음 봉 시가에 모의 적용 |
| v2 | bollinger_20_reentry | 9840.57 | -159.43 | sell / filled / 직전 종가 < 직전 하단밴드, 현재 하단밴드 <= 종가 <= SMA20 (한 봉 목표); 조건 미충족; close=334.49, lower20=332.961, SMA20=334.508, previous_lower20=332.957; 직전 완료 봉 목표를 다음 봉 시가에 모의 적용 |
| v2 | donchian_20 | 9784.95 | -215.05 | sell / filled / 종가 > 현재 봉을 제외한 직전 20봉 최고가; 조건 미충족; close=335.915, prior_high20=336.169; 직전 완료 봉 목표를 다음 봉 시가에 모의 적용 |
| v2 | atr_14_breakout | 9678.18 | -321.82 | sell / filled / 종가 > 직전 종가 + 직전 ATR14 그리고 종가 > EMA26; 조건 미충족; close=335.21, threshold=335.598, prior_ATR14=1.10843, EMA26=334.445; 직전 완료 봉 목표를 다음 봉 시가에 모의 적용 |
| v2 | session_vwap | 9553.60 | -446.40 | buy / partial / 종가 > 뉴욕 거래일별 누적 전형가격 VWAP; 조건 충족; close=334.909, session_VWAP=334.399, session_volume=2.0782e+06; 직전 완료 봉 목표를 다음 봉 시가에 모의 적용 |
| v2 | obv_20 | 9722.54 | -277.46 | buy / partial / OBV > OBV의 SMA20 그리고 종가 > EMA26; 조건 충족; OBV=-2.01293e+07, OBV_SMA20=-2.02067e+07, close=334.909, EMA26=334.523; 직전 완료 봉 목표를 다음 봉 시가에 모의 적용 |
| v2 | stochastic_14_3_recovery | 9551.56 | -448.44 | sell / filled / 직전 %K14 < 20에서 %K14가 %D3 상향 돌파 (한 봉 목표); 조건 미충족; K14=53.9297, D3=28.1336, previous_K14=24.5463, previous_D3=18.2988; 직전 완료 봉 목표를 다음 봉 시가에 모의 적용 |
| v2 | mfi_14_recovery | 9931.66 | -68.34 | sell / filled / 직전 MFI14 < 20, 현재 MFI14 >= 20 (한 봉 목표); 조건 미충족; MFI14=30.2719, previous_MFI14=26.8492; 직전 완료 봉 목표를 다음 봉 시가에 모의 적용 |
| v2 | adx_14_trend | 9722.79 | -277.21 | sell / filled / Wilder ADX14 >= 25 그리고 +DI14 > -DI14; 조건 미충족; ADX14=23.9395, plus_DI14=23.2021, minus_DI14=22.594; 직전 완료 봉 목표를 다음 봉 시가에 모의 적용 |
| v2 | aroon_25_trend | 9822.74 | -177.26 | sell / filled / Aroon25 Up > 70 그리고 Down < 30 (동률이면 최신 극값); 조건 미충족; Aroon_up=68, Aroon_down=16; 직전 완료 봉 목표를 다음 봉 시가에 모의 적용 |
| v2 | cci_20_momentum | 9802.89 | -197.11 | sell / filled / CCI20 > 100 (전형가격·평균절대편차); 조건 미충족; CCI20=57.5465; 직전 완료 봉 목표를 다음 봉 시가에 모의 적용 |
| v2 | williams_14_recovery | 9546.43 | -453.57 | sell / filled / 직전 Williams %R14 < -80, 현재 >= -80 (한 봉 목표); 조건 미충족; Williams_R14=-46.0703, previous_R14=-75.4537; 직전 완료 봉 목표를 다음 봉 시가에 모의 적용 |
| v2 | cmf_20_accumulation | 9790.91 | -209.09 | buy / partial / Chaikin Money Flow20 > 0.1; 조건 충족; CMF20=0.131084, volume20=2.22061e+06; 직전 완료 봉 목표를 다음 봉 시가에 모의 적용 |
| v2 | chaikin_3_10 | 9670.43 | -329.57 | buy / partial / ADL의 EMA3 - EMA10 > 0 그리고 종가 > EMA26; 조건 충족; Chaikin3_10=31581, ADL=-9.75237e+06, close=334.909, EMA26=334.523; 직전 완료 봉 목표를 다음 봉 시가에 모의 적용 |
| v2 | roc_10_momentum | 9832.47 | -167.53 | sell / filled / 10봉 ROC > 1% 그리고 종가 > EMA26; 조건 미충족; ROC10_percent=0.964142, close=337.72, EMA26=336.695; 직전 완료 봉 목표를 다음 봉 시가에 모의 적용 |
| v2 | trix_15_trend | 9715.96 | -284.04 | sell / filled / 15봉 삼중 EMA의 1봉 변화율 TRIX > 0 그리고 종가 > EMA26; 조건 미충족; TRIX15_percent=0.0135144, close=337.6, EMA26=338.759; 직전 완료 봉 목표를 다음 봉 시가에 모의 적용 |
| v2 | keltner_20_breakout | 9901.28 | -98.72 | sell / filled / 종가 > EMA20 + 2 x Wilder ATR14; 조건 미충족; close=339.04, upper_Keltner=339.281, EMA20=336.559, ATR14=1.36146; 직전 완료 봉 목표를 다음 봉 시가에 모의 적용 |
| v2 | opening_range_30m | 9846.33 | -153.67 | sell / filled / 뉴욕 09:30·09:45 두 완료 봉 최고가를 10:00 이후 종가가 돌파; 조건 미충족; close=337.72, opening_high=339.035; 직전 완료 봉 목표를 다음 봉 시가에 모의 적용 |

### 같은 기간의 비용·노출 비교 (사후 연구)

| 전략 | 비용 전 | 비용 후 | 100% 보유 | 같은 평균 노출 보유 | 평균 노출 |
|---|---:|---:|---:|---:|---:|
| cash | 0.00% | 0.00% | -0.23% | -0.00% | 0.00% |
| buy_hold | 0.19% | -0.23% | -0.23% | -0.23% | 100.00% |
| trend_8_26 | -0.55% | -5.04% | -0.23% | -0.13% | 54.19% |
| momentum_26 | -4.51% | -13.31% | -0.23% | -0.12% | 53.93% |
| breakout_8 | -3.62% | -18.86% | -0.23% | -0.04% | 19.37% |
| reversion_12 | 7.20% | -8.23% | -0.23% | -0.05% | 23.56% |
| volume_26 | 1.38% | -5.21% | -0.23% | -0.02% | 6.54% |
| trend_8_26 AND momentum_26 | -0.59% | -6.66% | -0.23% | -0.10% | 41.62% |
| trend_8_26 + momentum_26 | -2.54% | -9.07% | -0.23% | -0.13% | 54.06% |
| trend_8_26 AND breakout_8 | -3.41% | -13.77% | -0.23% | -0.03% | 11.78% |
| trend_8_26 + breakout_8 | -2.08% | -11.66% | -0.23% | -0.09% | 36.79% |
| trend_8_26 AND reversion_12 | 2.60% | -4.47% | -0.23% | -0.02% | 8.12% |
| trend_8_26 + reversion_12 | 3.27% | -6.06% | -0.23% | -0.09% | 38.88% |
| trend_8_26 AND volume_26 | 0.71% | -3.03% | -0.23% | -0.01% | 4.19% |
| trend_8_26 + volume_26 | 0.43% | -5.12% | -0.23% | -0.07% | 30.37% |
| momentum_26 AND breakout_8 | -3.60% | -15.01% | -0.23% | -0.03% | 12.30% |
| momentum_26 + breakout_8 | -4.04% | -15.94% | -0.23% | -0.08% | 36.66% |
| momentum_26 AND reversion_12 | 2.63% | -5.24% | -0.23% | -0.02% | 7.33% |
| momentum_26 + reversion_12 | 1.20% | -8.53% | -0.23% | -0.09% | 38.75% |
| momentum_26 AND volume_26 | -0.48% | -3.77% | -0.23% | -0.01% | 3.14% |
| momentum_26 + volume_26 | -1.58% | -8.77% | -0.23% | -0.07% | 30.24% |
| breakout_8 AND reversion_12 | 0.00% | 0.00% | -0.23% | -0.00% | 0.00% |
| breakout_8 + reversion_12 | 1.67% | -12.43% | -0.23% | -0.05% | 21.48% |
| breakout_8 AND volume_26 | 0.48% | -2.02% | -0.23% | -0.00% | 1.57% |
| breakout_8 + volume_26 | -1.14% | -11.37% | -0.23% | -0.03% | 12.96% |
| reversion_12 AND volume_26 | 2.09% | -0.45% | -0.23% | -0.00% | 2.09% |
| reversion_12 + volume_26 | 4.26% | -5.55% | -0.23% | -0.03% | 15.06% |
| ema_12_26 | -1.82% | -6.26% | -0.23% | -0.12% | 51.57% |
| macd_12_26_9 | -1.72% | -7.33% | -0.23% | -0.08% | 32.46% |
| rsi_14_recovery | 0.40% | -0.86% | -0.23% | -0.00% | 0.79% |
| bollinger_20_reentry | 0.62% | -3.52% | -0.23% | -0.01% | 2.62% |
| donchian_20 | -2.06% | -5.69% | -0.23% | -0.01% | 3.14% |
| atr_14_breakout | -1.02% | -9.00% | -0.23% | -0.01% | 5.50% |
| session_vwap | -0.37% | -11.05% | -0.23% | -0.11% | 48.43% |
| obv_20 | -4.52% | -17.22% | -0.23% | -0.07% | 29.84% |
| stochastic_14_3_recovery | -0.15% | -10.48% | -0.23% | -0.02% | 6.81% |
| mfi_14_recovery | 0.12% | -1.13% | -0.23% | -0.00% | 0.79% |
| adx_14_trend | -2.96% | -5.38% | -0.23% | -0.06% | 26.18% |
| aroon_25_trend | -1.37% | -5.03% | -0.23% | -0.05% | 20.42% |
| cci_20_momentum | -3.44% | -11.96% | -0.23% | -0.04% | 17.02% |
| williams_14_recovery | -0.60% | -10.88% | -0.23% | -0.02% | 6.81% |
| cmf_20_accumulation | -2.69% | -11.65% | -0.23% | -0.08% | 35.08% |
| chaikin_3_10 | 0.25% | -10.12% | -0.23% | -0.08% | 34.55% |
| roc_10_momentum | -1.40% | -3.86% | -0.23% | -0.02% | 6.54% |
| trix_15_trend | -1.66% | -9.20% | -0.23% | -0.08% | 34.29% |
| keltner_20_breakout | -1.21% | -4.07% | -0.23% | -0.01% | 4.19% |
| opening_range_30m | -0.49% | -4.19% | -0.23% | -0.04% | 17.02% |

동일 구간·초기 자금, 종료 시 청산 비용 포함. 노출 맞춤은 사후 설명용이며 v2 실제 계좌 성과가 아닙니다.
[낙폭 분해·비용 영향·전체 구간](JPM/comparison.json)

[v1 전체 기록](JPM/accounts.json) · [v2 전체 기록](JPM/accounts-v2.json)

## XOM 계좌

| 모델 | 전략 | 평가액 USD | 손익 USD | 최근 매매·이유 |
|---|---|---:|---:|---|
| v1 | cash | 10000.00 | 0.00 | 대기 /  / 새 신호 대기 |
| v1 | buy_hold | 10029.79 | 29.79 | buy /  / buy_hold: prior completed bar target 100%; next bar open simulation |
| v1 | trend_8_26 | 9707.62 | -292.38 | sell /  / trend_8_26: prior completed bar target 0%; next bar open simulation |
| v1 | momentum_26 | 9812.01 | -187.99 | sell /  / momentum_26: prior completed bar target 0%; next bar open simulation |
| v1 | breakout_8 | 9456.91 | -543.09 | sell /  / breakout_8: prior completed bar target 0%; next bar open simulation |
| v1 | reversion_12 | 9541.48 | -458.52 | sell /  / reversion_12: prior completed bar target 0%; next bar open simulation |
| v1 | volume_26 | 9510.72 | -489.28 | sell /  / volume_26: prior completed bar target 0%; next bar open simulation |
| v1 | trend_8_26 AND momentum_26 | 9682.17 | -317.83 | sell /  / trend_8_26 AND momentum_26: prior completed bar target 0%; next bar open simulation |
| v1 | trend_8_26 + momentum_26 | 9759.82 | -240.18 | sell /  / trend_8_26 + momentum_26: prior completed bar target 0%; next bar open simulation |
| v1 | trend_8_26 AND breakout_8 | 9628.70 | -371.30 | sell /  / trend_8_26 AND breakout_8: prior completed bar target 0%; next bar open simulation |
| v1 | trend_8_26 + breakout_8 | 9601.16 | -398.84 | sell /  / trend_8_26 + breakout_8: prior completed bar target 0%; next bar open simulation |
| v1 | trend_8_26 AND reversion_12 | 9569.59 | -430.41 | sell /  / trend_8_26 AND reversion_12: prior completed bar target 0%; next bar open simulation |
| v1 | trend_8_26 + reversion_12 | 9624.28 | -375.72 | sell /  / trend_8_26 + reversion_12: prior completed bar target 0%; next bar open simulation |
| v1 | trend_8_26 AND volume_26 | 9624.99 | -375.01 | sell /  / trend_8_26 AND volume_26: prior completed bar target 0%; next bar open simulation |
| v1 | trend_8_26 + volume_26 | 9609.08 | -390.92 | sell /  / trend_8_26 + volume_26: prior completed bar target 0%; next bar open simulation |
| v1 | momentum_26 AND breakout_8 | 9724.23 | -275.77 | sell /  / momentum_26 AND breakout_8: prior completed bar target 0%; next bar open simulation |
| v1 | momentum_26 + breakout_8 | 9633.26 | -366.74 | sell /  / momentum_26 + breakout_8: prior completed bar target 0%; next bar open simulation |
| v1 | momentum_26 AND reversion_12 | 9667.08 | -332.92 | sell /  / momentum_26 AND reversion_12: prior completed bar target 0%; next bar open simulation |
| v1 | momentum_26 + reversion_12 | 9675.78 | -324.22 | sell /  / momentum_26 + reversion_12: prior completed bar target 0%; next bar open simulation |
| v1 | momentum_26 AND volume_26 | 9843.02 | -156.98 | sell /  / momentum_26 AND volume_26: prior completed bar target 0%; next bar open simulation |
| v1 | momentum_26 + volume_26 | 9660.41 | -339.59 | sell /  / momentum_26 + volume_26: prior completed bar target 0%; next bar open simulation |
| v1 | breakout_8 AND reversion_12 | 10000.00 | 0.00 | 대기 /  / 새 신호 대기 |
| v1 | breakout_8 + reversion_12 | 9518.03 | -481.97 | sell /  / breakout_8 + reversion_12: prior completed bar target 0%; next bar open simulation |
| v1 | breakout_8 AND volume_26 | 9851.05 | -148.95 | sell /  / breakout_8 AND volume_26: prior completed bar target 0%; next bar open simulation |
| v1 | breakout_8 + volume_26 | 9483.68 | -516.32 | sell /  / breakout_8 + volume_26: prior completed bar target 0%; next bar open simulation |
| v1 | reversion_12 AND volume_26 | 9794.27 | -205.73 | sell /  / reversion_12 AND volume_26: prior completed bar target 0%; next bar open simulation |
| v1 | reversion_12 + volume_26 | 9526.20 | -473.80 | sell /  / reversion_12 + volume_26: prior completed bar target 0%; next bar open simulation |
| v1 | ema_12_26 | 9780.43 | -219.57 | sell /  / EMA12 > EMA26; 조건 미충족; EMA12=177.479, EMA26=177.559 |
| v1 | macd_12_26_9 | 9819.68 | -180.32 | sell /  / MACD > 신호선 그리고 MACD > 0; 조건 미충족; MACD=0.15005, signal9=0.18271 |
| v1 | rsi_14_recovery | 9927.64 | -72.36 | sell /  / 직전 RSI14 < 30, 현재 RSI14 >= 30 (한 봉 목표); 조건 미충족; RSI14=37.639, previous_RSI14=31.1023 |
| v1 | bollinger_20_reentry | 9694.21 | -305.79 | sell /  / 직전 종가 < 직전 하단밴드, 현재 하단밴드 <= 종가 <= SMA20 (한 봉 목표); 조건 미충족; close=175.53, lower20=174.782, SMA20=177.101, previous_lower20=174.994 |
| v1 | donchian_20 | 9665.93 | -334.07 | sell /  / 종가 > 현재 봉을 제외한 직전 20봉 최고가; 조건 미충족; close=178.045, prior_high20=179.205 |
| v1 | atr_14_breakout | 9803.61 | -196.39 | sell /  / 종가 > 직전 종가 + 직전 ATR14 그리고 종가 > EMA26; 조건 미충족; close=178.95, threshold=179.19, prior_ATR14=0.519565, EMA26=177.678 |
| v1 | session_vwap | 9797.51 | -202.49 | buy /  / 종가 > 뉴욕 거래일별 누적 전형가격 VWAP; 조건 충족; close=176.86, session_VWAP=176.627, session_volume=3.72585e+06 |
| v1 | obv_20 | 9273.72 | -726.28 | buy /  / OBV > OBV의 SMA20 그리고 종가 > EMA26; 조건 충족; OBV=2.23431e+07, OBV_SMA20=2.157e+07, close=176.86, EMA26=176.75 |
| v1 | stochastic_14_3_recovery | 9636.26 | -363.74 | sell /  / 직전 %K14 < 20에서 %K14가 %D3 상향 돌파 (한 봉 목표); 조건 미충족; K14=11.8836, D3=5.65987, previous_K14=4.66302, previous_D3=2.02546 |
| v1 | mfi_14_recovery | 10000.00 | 0.00 | 대기 /  / 새 신호 대기 |
| v1 | adx_14_trend | 9999.47 | -0.53 | sell /  / Wilder ADX14 >= 25 그리고 +DI14 > -DI14; 조건 미충족; ADX14=23.8302, plus_DI14=25.6436, minus_DI14=22.6035 |
| v1 | aroon_25_trend | 9589.85 | -410.15 | sell /  / Aroon25 Up > 70 그리고 Down < 30 (동률이면 최신 극값); 조건 미충족; Aroon_up=96, Aroon_down=40 |
| v1 | cci_20_momentum | 9418.76 | -581.24 | sell /  / CCI20 > 100 (전형가격·평균절대편차); 조건 미충족; CCI20=-36.6043 |
| v1 | williams_14_recovery | 9643.01 | -356.99 | sell /  / 직전 Williams %R14 < -80, 현재 >= -80 (한 봉 목표); 조건 미충족; Williams_R14=-68.9948, previous_R14=-74.4719 |
| v1 | cmf_20_accumulation | 9710.54 | -289.46 | sell /  / Chaikin Money Flow20 > 0.1; 조건 미충족; CMF20=0.0640816, volume20=6.12929e+06 |
| v1 | chaikin_3_10 | 9621.87 | -378.13 | buy /  / ADL의 EMA3 - EMA10 > 0 그리고 종가 > EMA26; 조건 충족; Chaikin3_10=152048, ADL=2.87515e+07, close=176.86, EMA26=176.75 |
| v1 | roc_10_momentum | 9848.63 | -151.37 | sell /  / 10봉 ROC > 1% 그리고 종가 > EMA26; 조건 미충족; ROC10_percent=0.417363, close=178.045, EMA26=177.705 |
| v1 | trix_15_trend | 9744.30 | -255.70 | sell /  / 15봉 삼중 EMA의 1봉 변화율 TRIX > 0 그리고 종가 > EMA26; 조건 미충족; TRIX15_percent=0.0153444, close=177.148, EMA26=177.751 |
| v1 | keltner_20_breakout | 9862.17 | -137.83 | sell /  / 종가 > EMA20 + 2 x Wilder ATR14; 조건 미충족; close=178.045, upper_Keltner=178.914, EMA20=177.784, ATR14=0.564804 |
| v1 | opening_range_30m | 9973.39 | -26.61 | sell /  / 뉴욕 09:30·09:45 두 완료 봉 최고가를 10:00 이후 종가가 돌파; 조건 미충족; close=178.045, opening_high=178.105 |
| v2 | cash | 10000.00 | 0.00 | 대기 /  / 새 신호 대기 |
| v2 | buy_hold | 10349.87 | 349.87 | buy / partial / 직전 완료 봉 목표 비중 100%; 다음 봉 시가 가정 |
| v2 | trend_8_26 | 9793.22 | -206.78 | sell / filled / 직전 완료 봉 목표 비중 0%; 다음 봉 시가 가정 |
| v2 | momentum_26 | 9975.42 | -24.58 | sell / filled / 직전 완료 봉 목표 비중 0%; 다음 봉 시가 가정 |
| v2 | breakout_8 | 8988.95 | -1011.05 | 중단: 손실 한도 / sell / filled / 직전 완료 봉 목표 비중 0%; 다음 봉 시가 가정 |
| v2 | reversion_12 | 9355.66 | -644.34 | sell / filled / 직전 완료 봉 목표 비중 0%; 다음 봉 시가 가정 |
| v2 | volume_26 | 9410.08 | -589.92 | sell / filled / 직전 완료 봉 목표 비중 0%; 다음 봉 시가 가정 |
| v2 | trend_8_26 AND momentum_26 | 9772.84 | -227.16 | sell / filled / 직전 완료 봉 목표 비중 0%; 다음 봉 시가 가정 |
| v2 | trend_8_26 + momentum_26 | 9884.07 | -115.93 | sell / filled / 직전 완료 봉 목표 비중 0%; 다음 봉 시가 가정 |
| v2 | trend_8_26 AND breakout_8 | 9084.52 | -915.48 | sell / filled / 직전 완료 봉 목표 비중 0%; 다음 봉 시가 가정 |
| v2 | trend_8_26 + breakout_8 | 9391.78 | -608.22 | sell / filled / 직전 완료 봉 목표 비중 0%; 다음 봉 시가 가정 |
| v2 | trend_8_26 AND reversion_12 | 9406.78 | -593.22 | sell / filled / 직전 완료 봉 목표 비중 0%; 다음 봉 시가 가정 |
| v2 | trend_8_26 + reversion_12 | 9572.09 | -427.91 | sell / filled / 직전 완료 봉 목표 비중 0%; 다음 봉 시가 가정 |
| v2 | trend_8_26 AND volume_26 | 9514.99 | -485.01 | sell / filled / 직전 완료 봉 목표 비중 0%; 다음 봉 시가 가정 |
| v2 | trend_8_26 + volume_26 | 9600.09 | -399.91 | sell / filled / 직전 완료 봉 목표 비중 0%; 다음 봉 시가 가정 |
| v2 | momentum_26 AND breakout_8 | 9193.28 | -806.72 | sell / filled / 직전 완료 봉 목표 비중 0%; 다음 봉 시가 가정 |
| v2 | momentum_26 + breakout_8 | 9439.09 | -560.91 | sell / filled / 직전 완료 봉 목표 비중 0%; 다음 봉 시가 가정 |
| v2 | momentum_26 AND reversion_12 | 9466.29 | -533.71 | sell / filled / 직전 완료 봉 목표 비중 0%; 다음 봉 시가 가정 |
| v2 | momentum_26 + reversion_12 | 9660.63 | -339.37 | sell / filled / 직전 완료 봉 목표 비중 0%; 다음 봉 시가 가정 |
| v2 | momentum_26 AND volume_26 | 9795.76 | -204.24 | sell / filled / 직전 완료 봉 목표 비중 0%; 다음 봉 시가 가정 |
| v2 | momentum_26 + volume_26 | 9709.12 | -290.88 | sell / filled / 직전 완료 봉 목표 비중 0%; 다음 봉 시가 가정 |
| v2 | breakout_8 AND reversion_12 | 10000.00 | 0.00 | 대기 /  / 새 신호 대기 |
| v2 | breakout_8 + reversion_12 | 9159.26 | -840.74 | sell / filled / 직전 완료 봉 목표 비중 0%; 다음 봉 시가 가정 |
| v2 | breakout_8 AND volume_26 | 9817.82 | -182.18 | sell / filled / 직전 완료 봉 목표 비중 0%; 다음 봉 시가 가정 |
| v2 | breakout_8 + volume_26 | 9185.86 | -814.14 | sell / filled / 직전 완료 봉 목표 비중 0%; 다음 봉 시가 가정 |
| v2 | reversion_12 AND volume_26 | 9737.38 | -262.62 | sell / filled / 직전 완료 봉 목표 비중 0%; 다음 봉 시가 가정 |
| v2 | reversion_12 + volume_26 | 9402.67 | -597.33 | sell / filled / 직전 완료 봉 목표 비중 0%; 다음 봉 시가 가정 |
| v2 | ema_12_26 | 9774.56 | -225.44 | sell / filled / EMA12 > EMA26; 조건 미충족; EMA12=177.479, EMA26=177.559; 직전 완료 봉 목표를 다음 봉 시가에 모의 적용 |
| v2 | macd_12_26_9 | 9809.86 | -190.14 | sell / filled / MACD > 신호선 그리고 MACD > 0; 조건 미충족; MACD=0.15005, signal9=0.18271; 직전 완료 봉 목표를 다음 봉 시가에 모의 적용 |
| v2 | rsi_14_recovery | 9923.67 | -76.33 | sell / filled / 직전 RSI14 < 30, 현재 RSI14 >= 30 (한 봉 목표); 조건 미충족; RSI14=37.639, previous_RSI14=31.1023; 직전 완료 봉 목표를 다음 봉 시가에 모의 적용 |
| v2 | bollinger_20_reentry | 9684.52 | -315.48 | sell / filled / 직전 종가 < 직전 하단밴드, 현재 하단밴드 <= 종가 <= SMA20 (한 봉 목표); 조건 미충족; close=175.53, lower20=174.782, SMA20=177.101, previous_lower20=174.994; 직전 완료 봉 목표를 다음 봉 시가에 모의 적용 |
| v2 | donchian_20 | 9654.34 | -345.66 | sell / filled / 종가 > 현재 봉을 제외한 직전 20봉 최고가; 조건 미충족; close=178.045, prior_high20=179.205; 직전 완료 봉 목표를 다음 봉 시가에 모의 적용 |
| v2 | atr_14_breakout | 9793.82 | -206.18 | sell / filled / 종가 > 직전 종가 + 직전 ATR14 그리고 종가 > EMA26; 조건 미충족; close=178.95, threshold=179.19, prior_ATR14=0.519565, EMA26=177.678; 직전 완료 봉 목표를 다음 봉 시가에 모의 적용 |
| v2 | session_vwap | 9782.82 | -217.18 | buy / partial / 종가 > 뉴욕 거래일별 누적 전형가격 VWAP; 조건 충족; close=176.86, session_VWAP=176.627, session_volume=3.72585e+06; 직전 완료 봉 목표를 다음 봉 시가에 모의 적용 |
| v2 | obv_20 | 9502.46 | -497.54 | 중단: 손실 한도 / sell / filled / OBV > OBV의 SMA20 그리고 종가 > EMA26; 조건 미충족; OBV=2.24329e+07, OBV_SMA20=2.30895e+07, close=177.005, EMA26=177.393; 직전 완료 봉 목표를 다음 봉 시가에 모의 적용 |
| v2 | stochastic_14_3_recovery | 9622.78 | -377.22 | sell / filled / 직전 %K14 < 20에서 %K14가 %D3 상향 돌파 (한 봉 목표); 조건 미충족; K14=11.8836, D3=5.65987, previous_K14=4.66302, previous_D3=2.02546; 직전 완료 봉 목표를 다음 봉 시가에 모의 적용 |
| v2 | mfi_14_recovery | 10000.00 | 0.00 | 대기 /  / 새 신호 대기 |
| v2 | adx_14_trend | 9993.47 | -6.53 | sell / filled / Wilder ADX14 >= 25 그리고 +DI14 > -DI14; 조건 미충족; ADX14=23.8302, plus_DI14=25.6436, minus_DI14=22.6035; 직전 완료 봉 목표를 다음 봉 시가에 모의 적용 |
| v2 | aroon_25_trend | 9582.18 | -417.82 | sell / filled / Aroon25 Up > 70 그리고 Down < 30 (동률이면 최신 극값); 조건 미충족; Aroon_up=96, Aroon_down=40; 직전 완료 봉 목표를 다음 봉 시가에 모의 적용 |
| v2 | cci_20_momentum | 9398.06 | -601.94 | sell / filled / CCI20 > 100 (전형가격·평균절대편차); 조건 미충족; CCI20=-36.6043; 직전 완료 봉 목표를 다음 봉 시가에 모의 적용 |
| v2 | williams_14_recovery | 9629.52 | -370.48 | sell / filled / 직전 Williams %R14 < -80, 현재 >= -80 (한 봉 목표); 조건 미충족; Williams_R14=-68.9948, previous_R14=-74.4719; 직전 완료 봉 목표를 다음 봉 시가에 모의 적용 |
| v2 | cmf_20_accumulation | 9698.90 | -301.10 | sell / filled / Chaikin Money Flow20 > 0.1; 조건 미충족; CMF20=0.0640816, volume20=6.12929e+06; 직전 완료 봉 목표를 다음 봉 시가에 모의 적용 |
| v2 | chaikin_3_10 | 9605.53 | -394.47 | buy / partial / ADL의 EMA3 - EMA10 > 0 그리고 종가 > EMA26; 조건 충족; Chaikin3_10=152048, ADL=2.87515e+07, close=176.86, EMA26=176.75; 직전 완료 봉 목표를 다음 봉 시가에 모의 적용 |
| v2 | roc_10_momentum | 9840.76 | -159.24 | sell / filled / 10봉 ROC > 1% 그리고 종가 > EMA26; 조건 미충족; ROC10_percent=0.417363, close=178.045, EMA26=177.705; 직전 완료 봉 목표를 다음 봉 시가에 모의 적용 |
| v2 | trix_15_trend | 9732.61 | -267.39 | sell / filled / 15봉 삼중 EMA의 1봉 변화율 TRIX > 0 그리고 종가 > EMA26; 조건 미충족; TRIX15_percent=0.0153444, close=177.148, EMA26=177.751; 직전 완료 봉 목표를 다음 봉 시가에 모의 적용 |
| v2 | keltner_20_breakout | 9854.29 | -145.71 | sell / filled / 종가 > EMA20 + 2 x Wilder ATR14; 조건 미충족; close=178.045, upper_Keltner=178.914, EMA20=177.784, ATR14=0.564804; 직전 완료 봉 목표를 다음 봉 시가에 모의 적용 |
| v2 | opening_range_30m | 9969.40 | -30.60 | sell / filled / 뉴욕 09:30·09:45 두 완료 봉 최고가를 10:00 이후 종가가 돌파; 조건 미충족; close=178.045, opening_high=178.105; 직전 완료 봉 목표를 다음 봉 시가에 모의 적용 |

### 같은 기간의 비용·노출 비교 (사후 연구)

| 전략 | 비용 전 | 비용 후 | 100% 보유 | 같은 평균 노출 보유 | 평균 노출 |
|---|---:|---:|---:|---:|---:|
| cash | 0.00% | 0.00% | 8.94% | 0.00% | 0.00% |
| buy_hold | 9.40% | 8.94% | 8.94% | 8.94% | 100.00% |
| trend_8_26 | 2.37% | -1.84% | 8.94% | 6.07% | 69.11% |
| momentum_26 | 2.56% | -2.89% | 8.94% | 6.14% | 69.90% |
| breakout_8 | -0.74% | -18.52% | 8.94% | 2.27% | 26.44% |
| reversion_12 | 2.50% | -7.33% | 8.94% | 1.86% | 21.73% |
| volume_26 | 0.43% | -7.66% | 8.94% | 0.51% | 6.02% |
| trend_8_26 AND momentum_26 | 0.65% | -4.29% | 8.94% | 5.31% | 60.73% |
| trend_8_26 + momentum_26 | 2.48% | -2.15% | 8.94% | 6.11% | 69.51% |
| trend_8_26 AND breakout_8 | -0.60% | -15.27% | 8.94% | 1.77% | 20.68% |
| trend_8_26 + breakout_8 | 0.83% | -10.17% | 8.94% | 4.15% | 47.78% |
| trend_8_26 AND reversion_12 | -0.82% | -6.87% | 8.94% | 0.87% | 10.21% |
| trend_8_26 + reversion_12 | 2.47% | -4.42% | 8.94% | 3.94% | 45.42% |
| trend_8_26 AND volume_26 | -0.39% | -5.68% | 8.94% | 0.33% | 3.93% |
| trend_8_26 + volume_26 | 1.42% | -4.59% | 8.94% | 3.24% | 37.57% |
| momentum_26 AND breakout_8 | -0.52% | -15.90% | 8.94% | 1.93% | 22.51% |
| momentum_26 + breakout_8 | 0.93% | -11.02% | 8.94% | 4.18% | 48.18% |
| momentum_26 AND reversion_12 | -0.06% | -6.95% | 8.94% | 0.82% | 9.69% |
| momentum_26 + reversion_12 | 2.56% | -4.13% | 8.94% | 3.97% | 45.82% |
| momentum_26 AND volume_26 | 0.84% | -3.31% | 8.94% | 0.22% | 2.62% |
| momentum_26 + volume_26 | 1.52% | -4.30% | 8.94% | 3.28% | 37.96% |
| breakout_8 AND reversion_12 | 0.00% | 0.00% | 8.94% | 0.00% | 0.00% |
| breakout_8 + reversion_12 | 0.89% | -12.74% | 8.94% | 2.06% | 24.09% |
| breakout_8 AND volume_26 | -0.10% | -2.18% | 8.94% | 0.11% | 1.31% |
| breakout_8 + volume_26 | -0.14% | -12.53% | 8.94% | 1.39% | 16.24% |
| reversion_12 AND volume_26 | -0.04% | -3.35% | 8.94% | 0.20% | 2.36% |
| reversion_12 + volume_26 | 1.48% | -6.71% | 8.94% | 1.18% | 13.88% |
| ema_12_26 | 1.19% | -2.16% | 8.94% | 6.53% | 74.08% |
| macd_12_26_9 | -0.17% | -6.26% | 8.94% | 3.67% | 42.41% |
| rsi_14_recovery | -0.08% | -1.33% | 8.94% | 0.07% | 0.79% |
| bollinger_20_reentry | -1.53% | -5.18% | 8.94% | 0.20% | 2.36% |
| donchian_20 | -2.09% | -10.73% | 8.94% | 0.80% | 9.42% |
| atr_14_breakout | 0.61% | -7.11% | 8.94% | 0.44% | 5.24% |
| session_vwap | 2.04% | -8.90% | 8.94% | 5.62% | 64.14% |
| obv_20 | 0.49% | -10.29% | 8.94% | 4.25% | 48.95% |
| stochastic_14_3_recovery | 0.05% | -9.54% | 8.94% | 0.53% | 6.28% |
| mfi_14_recovery | -0.31% | -1.97% | 8.94% | 0.09% | 1.05% |
| adx_14_trend | 3.33% | 0.76% | 8.94% | 3.32% | 38.48% |
| aroon_25_trend | -2.74% | -9.45% | 8.94% | 2.79% | 32.46% |
| cci_20_momentum | 1.06% | -8.63% | 8.94% | 2.43% | 28.27% |
| williams_14_recovery | -1.21% | -7.24% | 8.94% | 0.33% | 3.93% |
| cmf_20_accumulation | 2.56% | -4.10% | 8.94% | 4.46% | 51.31% |
| chaikin_3_10 | 2.22% | -7.20% | 8.94% | 5.24% | 59.95% |
| roc_10_momentum | -0.09% | -5.80% | 8.94% | 1.00% | 11.78% |
| trix_15_trend | 0.94% | -5.62% | 8.94% | 5.36% | 61.26% |
| keltner_20_breakout | 0.18% | -5.94% | 8.94% | 1.38% | 16.23% |
| opening_range_30m | 0.89% | -6.85% | 8.94% | 2.31% | 26.96% |

동일 구간·초기 자금, 종료 시 청산 비용 포함. 노출 맞춤은 사후 설명용이며 v2 실제 계좌 성과가 아닙니다.
[낙폭 분해·비용 영향·전체 구간](XOM/comparison.json)

[v1 전체 기록](XOM/accounts.json) · [v2 전체 기록](XOM/accounts-v2.json)

## JNJ 계좌

| 모델 | 전략 | 평가액 USD | 손익 USD | 최근 매매·이유 |
|---|---|---:|---:|---|
| v1 | cash | 10000.00 | 0.00 | 대기 /  / 새 신호 대기 |
| v1 | buy_hold | 10469.03 | 469.03 | buy /  / buy_hold: prior completed bar target 100%; next bar open simulation |
| v1 | trend_8_26 | 10397.30 | 397.30 | buy /  / trend_8_26: prior completed bar target 100%; next bar open simulation |
| v1 | momentum_26 | 9935.79 | -64.21 | buy /  / momentum_26: prior completed bar target 100%; next bar open simulation |
| v1 | breakout_8 | 9592.60 | -407.40 | buy /  / breakout_8: prior completed bar target 100%; next bar open simulation |
| v1 | reversion_12 | 9747.78 | -252.22 | sell /  / reversion_12: prior completed bar target 0%; next bar open simulation |
| v1 | volume_26 | 10040.58 | 40.58 | sell /  / volume_26: prior completed bar target 0%; next bar open simulation |
| v1 | trend_8_26 AND momentum_26 | 10028.73 | 28.73 | buy /  / trend_8_26 AND momentum_26: prior completed bar target 100%; next bar open simulation |
| v1 | trend_8_26 + momentum_26 | 10164.43 | 164.43 | buy /  / trend_8_26 + momentum_26: prior completed bar target 100%; next bar open simulation |
| v1 | trend_8_26 AND breakout_8 | 9987.66 | -12.34 | buy /  / trend_8_26 AND breakout_8: prior completed bar target 100%; next bar open simulation |
| v1 | trend_8_26 + breakout_8 | 10007.22 | 7.22 | buy /  / trend_8_26 + breakout_8: prior completed bar target 100%; next bar open simulation |
| v1 | trend_8_26 AND reversion_12 | 9930.57 | -69.43 | sell /  / trend_8_26 AND reversion_12: prior completed bar target 0%; next bar open simulation |
| v1 | trend_8_26 + reversion_12 | 10067.51 | 67.51 | sell /  / trend_8_26 + reversion_12: prior completed bar target 50%; next bar open simulation |
| v1 | trend_8_26 AND volume_26 | 10134.54 | 134.54 | sell /  / trend_8_26 AND volume_26: prior completed bar target 0%; next bar open simulation |
| v1 | trend_8_26 + volume_26 | 10217.59 | 217.59 | sell /  / trend_8_26 + volume_26: prior completed bar target 50%; next bar open simulation |
| v1 | momentum_26 AND breakout_8 | 9825.10 | -174.90 | buy /  / momentum_26 AND breakout_8: prior completed bar target 100%; next bar open simulation |
| v1 | momentum_26 + breakout_8 | 9762.82 | -237.18 | buy /  / momentum_26 + breakout_8: prior completed bar target 100%; next bar open simulation |
| v1 | momentum_26 AND reversion_12 | 9938.52 | -61.48 | sell /  / momentum_26 AND reversion_12: prior completed bar target 0%; next bar open simulation |
| v1 | momentum_26 + reversion_12 | 9880.57 | -119.43 | sell /  / momentum_26 + reversion_12: prior completed bar target 50%; next bar open simulation |
| v1 | momentum_26 AND volume_26 | 10000.00 | 0.00 | 대기 /  / 새 신호 대기 |
| v1 | momentum_26 + volume_26 | 10048.32 | 48.32 | sell /  / momentum_26 + volume_26: prior completed bar target 50%; next bar open simulation |
| v1 | breakout_8 AND reversion_12 | 10000.00 | 0.00 | 대기 /  / 새 신호 대기 |
| v1 | breakout_8 + reversion_12 | 9669.71 | -330.29 | sell /  / breakout_8 + reversion_12: prior completed bar target 50%; next bar open simulation |
| v1 | breakout_8 AND volume_26 | 10139.49 | 139.49 | sell /  / breakout_8 AND volume_26: prior completed bar target 0%; next bar open simulation |
| v1 | breakout_8 + volume_26 | 9833.60 | -166.40 | sell /  / breakout_8 + volume_26: prior completed bar target 50%; next bar open simulation |
| v1 | reversion_12 AND volume_26 | 9933.02 | -66.98 | sell /  / reversion_12 AND volume_26: prior completed bar target 0%; next bar open simulation |
| v1 | reversion_12 + volume_26 | 9913.08 | -86.92 | sell /  / reversion_12 + volume_26: prior completed bar target 0%; next bar open simulation |
| v1 | ema_12_26 | 10031.30 | 31.30 | buy /  / EMA12 > EMA26; 조건 충족; EMA12=256.701, EMA26=256.629 |
| v1 | macd_12_26_9 | 10151.79 | 151.79 | buy /  / MACD > 신호선 그리고 MACD > 0; 조건 충족; MACD=0.0724674, signal9=-0.175801 |
| v1 | rsi_14_recovery | 9923.04 | -76.96 | sell /  / 직전 RSI14 < 30, 현재 RSI14 >= 30 (한 봉 목표); 조건 미충족; RSI14=40.3665, previous_RSI14=36.2025 |
| v1 | bollinger_20_reentry | 9816.96 | -183.04 | sell /  / 직전 종가 < 직전 하단밴드, 현재 하단밴드 <= 종가 <= SMA20 (한 봉 목표); 조건 미충족; close=255.05, lower20=254.819, SMA20=258.099, previous_lower20=255.312 |
| v1 | donchian_20 | 9849.44 | -150.56 | buy /  / 종가 > 현재 봉을 제외한 직전 20봉 최고가; 조건 충족; close=268.11, prior_high20=267.799 |
| v1 | atr_14_breakout | 9670.87 | -329.13 | sell /  / 종가 > 직전 종가 + 직전 ATR14 그리고 종가 > EMA26; 조건 미충족; close=267.475, threshold=268.093, prior_ATR14=0.987507, EMA26=261.689 |
| v1 | session_vwap | 10109.27 | 109.27 | buy /  / 종가 > 뉴욕 거래일별 누적 전형가격 VWAP; 조건 충족; close=256.05, session_VWAP=255.552, session_volume=3.26826e+06 |
| v1 | obv_20 | 9890.90 | -109.10 | buy /  / OBV > OBV의 SMA20 그리고 종가 > EMA26; 조건 충족; OBV=8.73204e+06, OBV_SMA20=8.54861e+06, close=257.085, EMA26=256.499 |
| v1 | stochastic_14_3_recovery | 9576.18 | -423.82 | sell /  / 직전 %K14 < 20에서 %K14가 %D3 상향 돌파 (한 봉 목표); 조건 미충족; K14=33.4928, D3=23.2217, previous_K14=28.5165, previous_D3=14.8644 |
| v1 | mfi_14_recovery | 9931.49 | -68.51 | sell /  / 직전 MFI14 < 20, 현재 MFI14 >= 20 (한 봉 목표); 조건 미충족; MFI14=35.8262, previous_MFI14=31.0222 |
| v1 | adx_14_trend | 9843.41 | -156.59 | buy /  / Wilder ADX14 >= 25 그리고 +DI14 > -DI14; 조건 충족; ADX14=27.0686, plus_DI14=50.9231, minus_DI14=9.79199 |
| v1 | aroon_25_trend | 10164.09 | 164.09 | buy /  / Aroon25 Up > 70 그리고 Down < 30 (동률이면 최신 극값); 조건 충족; Aroon_up=100, Aroon_down=24 |
| v1 | cci_20_momentum | 10185.26 | 185.26 | sell /  / CCI20 > 100 (전형가격·평균절대편차); 조건 미충족; CCI20=97.4316 |
| v1 | williams_14_recovery | 9706.89 | -293.11 | sell /  / 직전 Williams %R14 < -80, 현재 >= -80 (한 봉 목표); 조건 미충족; Williams_R14=-66.5072, previous_R14=-71.4835 |
| v1 | cmf_20_accumulation | 10467.02 | 467.02 | buy /  / Chaikin Money Flow20 > 0.1; 조건 충족; CMF20=0.396629, volume20=6.26242e+06 |
| v1 | chaikin_3_10 | 10190.11 | 190.11 | buy /  / ADL의 EMA3 - EMA10 > 0 그리고 종가 > EMA26; 조건 충족; Chaikin3_10=8814.88, ADL=5.01916e+06, close=256.505, EMA26=256.405 |
| v1 | roc_10_momentum | 9904.78 | -95.22 | buy /  / 10봉 ROC > 1% 그리고 종가 > EMA26; 조건 충족; ROC10_percent=2.2132, close=261.63, EMA26=256.999 |
| v1 | trix_15_trend | 9836.76 | -163.24 | buy /  / 15봉 삼중 EMA의 1봉 변화율 TRIX > 0 그리고 종가 > EMA26; 조건 충족; TRIX15_percent=0.00204174, close=262.76, EMA26=257.426 |
| v1 | keltner_20_breakout | 10133.99 | 133.99 | buy /  / 종가 > EMA20 + 2 x Wilder ATR14; 조건 충족; close=261.63, upper_Keltner=258.85, EMA20=257.085, ATR14=0.882261 |
| v1 | opening_range_30m | 10150.06 | 150.06 | buy /  / 뉴욕 09:30·09:45 두 완료 봉 최고가를 10:00 이후 종가가 돌파; 조건 충족; close=263.54, opening_high=263.19 |
| v2 | cash | 10000.00 | 0.00 | 대기 /  / 새 신호 대기 |
| v2 | buy_hold | 10224.69 | 224.69 | 중단: 손실 한도 / buy / partial / 직전 완료 봉 목표 비중 100%; 다음 봉 시가 가정 |
| v2 | trend_8_26 | 10224.69 | 224.69 | 중단: 손실 한도 / buy / partial / 직전 완료 봉 목표 비중 100%; 다음 봉 시가 가정 |
| v2 | momentum_26 | 10224.69 | 224.69 | 중단: 손실 한도 / buy / partial / 직전 완료 봉 목표 비중 100%; 다음 봉 시가 가정 |
| v2 | breakout_8 | 9343.39 | -656.61 | 중단: 손실 한도 / sell / filled / 직전 완료 봉 목표 비중 0%; 다음 봉 시가 가정 |
| v2 | reversion_12 | 9434.41 | -565.59 | sell / filled / 직전 완료 봉 목표 비중 0%; 다음 봉 시가 가정 |
| v2 | volume_26 | 9819.31 | -180.69 | sell / filled / 직전 완료 봉 목표 비중 0%; 다음 봉 시가 가정 |
| v2 | trend_8_26 AND momentum_26 | 10224.69 | 224.69 | 중단: 손실 한도 / buy / partial / 직전 완료 봉 목표 비중 100%; 다음 봉 시가 가정 |
| v2 | trend_8_26 + momentum_26 | 10224.69 | 224.69 | 중단: 손실 한도 / buy / partial / 직전 완료 봉 목표 비중 100%; 다음 봉 시가 가정 |
| v2 | trend_8_26 AND breakout_8 | 9419.39 | -580.61 | 중단: 손실 한도 / sell / filled / 직전 완료 봉 목표 비중 0%; 다음 봉 시가 가정 |
| v2 | trend_8_26 + breakout_8 | 9560.45 | -439.55 | buy / partial / 직전 완료 봉 목표 비중 100%; 다음 봉 시가 가정 |
| v2 | trend_8_26 AND reversion_12 | 9900.89 | -99.11 | sell / filled / 직전 완료 봉 목표 비중 0%; 다음 봉 시가 가정 |
| v2 | trend_8_26 + reversion_12 | 9732.92 | -267.08 | 중단: 손실 한도 / sell / filled / 직전 완료 봉 목표 비중 0%; 다음 봉 시가 가정 |
| v2 | trend_8_26 AND volume_26 | 9997.51 | -2.49 | sell / filled / 직전 완료 봉 목표 비중 0%; 다음 봉 시가 가정 |
| v2 | trend_8_26 + volume_26 | 10091.27 | 91.27 | 중단: 손실 한도 / buy / filled / 직전 완료 봉 목표 비중 50%; 다음 봉 시가 가정 |
| v2 | momentum_26 AND breakout_8 | 9418.57 | -581.43 | buy / partial / 직전 완료 봉 목표 비중 100%; 다음 봉 시가 가정 |
| v2 | momentum_26 + breakout_8 | 9317.26 | -682.74 | buy / partial / 직전 완료 봉 목표 비중 100%; 다음 봉 시가 가정 |
| v2 | momentum_26 AND reversion_12 | 9871.83 | -128.17 | sell / filled / 직전 완료 봉 목표 비중 0%; 다음 봉 시가 가정 |
| v2 | momentum_26 + reversion_12 | 9732.92 | -267.08 | 중단: 손실 한도 / sell / filled / 직전 완료 봉 목표 비중 0%; 다음 봉 시가 가정 |
| v2 | momentum_26 AND volume_26 | 9920.93 | -79.07 | sell / filled / 직전 완료 봉 목표 비중 0%; 다음 봉 시가 가정 |
| v2 | momentum_26 + volume_26 | 10091.27 | 91.27 | 중단: 손실 한도 / buy / filled / 직전 완료 봉 목표 비중 50%; 다음 봉 시가 가정 |
| v2 | breakout_8 AND reversion_12 | 10000.00 | 0.00 | 대기 /  / 새 신호 대기 |
| v2 | breakout_8 + reversion_12 | 9244.67 | -755.33 | sell / filled / 직전 완료 봉 목표 비중 50%; 다음 봉 시가 가정 |
| v2 | breakout_8 AND volume_26 | 9949.08 | -50.92 | sell / filled / 직전 완료 봉 목표 비중 0%; 다음 봉 시가 가정 |
| v2 | breakout_8 + volume_26 | 9431.38 | -568.62 | sell / filled / 직전 완료 봉 목표 비중 50%; 다음 봉 시가 가정 |
| v2 | reversion_12 AND volume_26 | 9816.09 | -183.91 | sell / filled / 직전 완료 봉 목표 비중 0%; 다음 봉 시가 가정 |
| v2 | reversion_12 + volume_26 | 9665.84 | -334.16 | sell / filled / 직전 완료 봉 목표 비중 0%; 다음 봉 시가 가정 |
| v2 | ema_12_26 | 10024.28 | 24.28 | buy / partial / EMA12 > EMA26; 조건 충족; EMA12=256.701, EMA26=256.629; 직전 완료 봉 목표를 다음 봉 시가에 모의 적용 |
| v2 | macd_12_26_9 | 10144.68 | 144.68 | buy / partial / MACD > 신호선 그리고 MACD > 0; 조건 충족; MACD=0.0724674, signal9=-0.175801; 직전 완료 봉 목표를 다음 봉 시가에 모의 적용 |
| v2 | rsi_14_recovery | 9919.07 | -80.93 | sell / filled / 직전 RSI14 < 30, 현재 RSI14 >= 30 (한 봉 목표); 조건 미충족; RSI14=40.3665, previous_RSI14=36.2025; 직전 완료 봉 목표를 다음 봉 시가에 모의 적용 |
| v2 | bollinger_20_reentry | 9811.07 | -188.93 | sell / filled / 직전 종가 < 직전 하단밴드, 현재 하단밴드 <= 종가 <= SMA20 (한 봉 목표); 조건 미충족; close=255.05, lower20=254.819, SMA20=258.099, previous_lower20=255.312; 직전 완료 봉 목표를 다음 봉 시가에 모의 적용 |
| v2 | donchian_20 | 9836.64 | -163.36 | buy / partial / 종가 > 현재 봉을 제외한 직전 20봉 최고가; 조건 충족; close=268.11, prior_high20=267.799; 직전 완료 봉 목표를 다음 봉 시가에 모의 적용 |
| v2 | atr_14_breakout | 9657.34 | -342.66 | sell / filled / 종가 > 직전 종가 + 직전 ATR14 그리고 종가 > EMA26; 조건 미충족; close=267.475, threshold=268.093, prior_ATR14=0.987507, EMA26=261.689; 직전 완료 봉 목표를 다음 봉 시가에 모의 적용 |
| v2 | session_vwap | 10090.08 | 90.08 | buy / partial / 종가 > 뉴욕 거래일별 누적 전형가격 VWAP; 조건 충족; close=256.05, session_VWAP=255.552, session_volume=3.26826e+06; 직전 완료 봉 목표를 다음 봉 시가에 모의 적용 |
| v2 | obv_20 | 9872.13 | -127.87 | buy / partial / OBV > OBV의 SMA20 그리고 종가 > EMA26; 조건 충족; OBV=8.59102e+06, OBV_SMA20=8.40759e+06, close=257.085, EMA26=256.499; 직전 완료 봉 목표를 다음 봉 시가에 모의 적용 |
| v2 | stochastic_14_3_recovery | 9560.87 | -439.13 | sell / filled / 직전 %K14 < 20에서 %K14가 %D3 상향 돌파 (한 봉 목표); 조건 미충족; K14=33.4928, D3=23.2217, previous_K14=28.5165, previous_D3=14.8644; 직전 완료 봉 목표를 다음 봉 시가에 모의 적용 |
| v2 | mfi_14_recovery | 9925.53 | -74.47 | sell / filled / 직전 MFI14 < 20, 현재 MFI14 >= 20 (한 봉 목표); 조건 미충족; MFI14=35.8262, previous_MFI14=31.0222; 직전 완료 봉 목표를 다음 봉 시가에 모의 적용 |
| v2 | adx_14_trend | 9834.55 | -165.45 | buy / partial / Wilder ADX14 >= 25 그리고 +DI14 > -DI14; 조건 충족; ADX14=27.0686, plus_DI14=50.9231, minus_DI14=9.79199; 직전 완료 봉 목표를 다음 봉 시가에 모의 적용 |
| v2 | aroon_25_trend | 10159.01 | 159.01 | buy / partial / Aroon25 Up > 70 그리고 Down < 30 (동률이면 최신 극값); 조건 충족; Aroon_up=100, Aroon_down=24; 직전 완료 봉 목표를 다음 봉 시가에 모의 적용 |
| v2 | cci_20_momentum | 10177.12 | 177.12 | sell / filled / CCI20 > 100 (전형가격·평균절대편차); 조건 미충족; CCI20=97.4316; 직전 완료 봉 목표를 다음 봉 시가에 모의 적용 |
| v2 | williams_14_recovery | 9697.19 | -302.81 | sell / filled / 직전 Williams %R14 < -80, 현재 >= -80 (한 봉 목표); 조건 미충족; Williams_R14=-66.5072, previous_R14=-71.4835; 직전 완료 봉 목표를 다음 봉 시가에 모의 적용 |
| v2 | cmf_20_accumulation | 10461.79 | 461.79 | buy / partial / Chaikin Money Flow20 > 0.1; 조건 충족; CMF20=0.396629, volume20=6.26242e+06; 직전 완료 봉 목표를 다음 봉 시가에 모의 적용 |
| v2 | chaikin_3_10 | 10180.94 | 180.94 | buy / partial / ADL의 EMA3 - EMA10 > 0 그리고 종가 > EMA26; 조건 충족; Chaikin3_10=8814.88, ADL=4.70768e+06, close=256.505, EMA26=256.405; 직전 완료 봉 목표를 다음 봉 시가에 모의 적용 |
| v2 | roc_10_momentum | 9895.87 | -104.13 | buy / partial / 10봉 ROC > 1% 그리고 종가 > EMA26; 조건 충족; ROC10_percent=2.2132, close=261.63, EMA26=256.999; 직전 완료 봉 목표를 다음 봉 시가에 모의 적용 |
| v2 | trix_15_trend | 9829.88 | -170.12 | buy / partial / 15봉 삼중 EMA의 1봉 변화율 TRIX > 0 그리고 종가 > EMA26; 조건 충족; TRIX15_percent=0.00204174, close=262.76, EMA26=257.426; 직전 완료 봉 목표를 다음 봉 시가에 모의 적용 |
| v2 | keltner_20_breakout | 10130.95 | 130.95 | buy / partial / 종가 > EMA20 + 2 x Wilder ATR14; 조건 충족; close=261.63, upper_Keltner=258.85, EMA20=257.085, ATR14=0.882261; 직전 완료 봉 목표를 다음 봉 시가에 모의 적용 |
| v2 | opening_range_30m | 10149.04 | 149.04 | buy / partial / 뉴욕 09:30·09:45 두 완료 봉 최고가를 10:00 이후 종가가 돌파; 조건 충족; close=263.54, opening_high=263.19; 직전 완료 봉 목표를 다음 봉 시가에 모의 적용 |

### 같은 기간의 비용·노출 비교 (사후 연구)

| 전략 | 비용 전 | 비용 후 | 100% 보유 | 같은 평균 노출 보유 | 평균 노출 |
|---|---:|---:|---:|---:|---:|
| cash | 0.00% | 0.00% | 2.91% | 0.00% | 0.00% |
| buy_hold | 3.34% | 2.91% | 2.91% | 2.91% | 100.00% |
| trend_8_26 | 7.01% | 4.35% | 2.91% | 1.55% | 53.14% |
| momentum_26 | 1.52% | -1.84% | 2.91% | 1.48% | 50.52% |
| breakout_8 | 2.77% | -16.35% | 2.91% | 0.71% | 24.35% |
| reversion_12 | -4.65% | -12.34% | 2.91% | 0.76% | 25.92% |
| volume_26 | 1.99% | -4.64% | 2.91% | 0.18% | 6.02% |
| trend_8_26 AND momentum_26 | 3.21% | 0.22% | 2.91% | 1.32% | 45.03% |
| trend_8_26 + momentum_26 | 4.24% | 1.21% | 2.91% | 1.52% | 51.83% |
| trend_8_26 AND breakout_8 | 3.86% | -9.96% | 2.91% | 0.52% | 17.80% |
| trend_8_26 + breakout_8 | 4.90% | -6.35% | 2.91% | 1.14% | 38.75% |
| trend_8_26 AND reversion_12 | 1.37% | -1.98% | 2.91% | 0.17% | 5.76% |
| trend_8_26 + reversion_12 | 1.05% | -4.15% | 2.91% | 1.16% | 39.53% |
| trend_8_26 AND volume_26 | 3.25% | 0.26% | 2.91% | 0.06% | 2.09% |
| trend_8_26 + volume_26 | 4.51% | -0.02% | 2.91% | 0.87% | 29.58% |
| momentum_26 AND breakout_8 | 2.85% | -9.70% | 2.91% | 0.47% | 15.97% |
| momentum_26 + breakout_8 | 2.17% | -9.17% | 2.91% | 1.10% | 37.44% |
| momentum_26 AND reversion_12 | -0.27% | -3.16% | 2.91% | 0.18% | 6.28% |
| momentum_26 + reversion_12 | -1.59% | -6.64% | 2.91% | 1.12% | 38.22% |
| momentum_26 AND volume_26 | 0.14% | -0.70% | 2.91% | 0.02% | 0.52% |
| momentum_26 + volume_26 | 1.79% | -2.01% | 2.91% | 0.83% | 28.27% |
| breakout_8 AND reversion_12 | 0.00% | 0.00% | 2.91% | 0.00% | 0.00% |
| breakout_8 + reversion_12 | -0.99% | -14.01% | 2.91% | 0.74% | 25.14% |
| breakout_8 AND volume_26 | 1.33% | 0.06% | 2.91% | 0.03% | 1.05% |
| breakout_8 + volume_26 | 2.39% | -9.74% | 2.91% | 0.45% | 15.19% |
| reversion_12 AND volume_26 | -1.19% | -3.65% | 2.91% | 0.06% | 2.09% |
| reversion_12 + volume_26 | -1.37% | -7.99% | 2.91% | 0.47% | 15.97% |
| ema_12_26 | 1.80% | -1.15% | 2.91% | 1.50% | 51.31% |
| macd_12_26_9 | 8.87% | 5.27% | 2.91% | 1.00% | 34.03% |
| rsi_14_recovery | -1.09% | -5.16% | 2.91% | 0.08% | 2.62% |
| bollinger_20_reentry | -1.28% | -5.34% | 2.91% | 0.08% | 2.62% |
| donchian_20 | 2.18% | -7.23% | 2.91% | 0.28% | 9.42% |
| atr_14_breakout | 1.13% | -6.24% | 2.91% | 0.17% | 5.76% |
| session_vwap | 8.09% | -0.62% | 2.91% | 1.64% | 56.02% |
| obv_20 | -1.76% | -11.93% | 2.91% | 1.19% | 40.58% |
| stochastic_14_3_recovery | -0.70% | -11.35% | 2.91% | 0.21% | 7.07% |
| mfi_14_recovery | 0.80% | -1.30% | 2.91% | 0.04% | 1.31% |
| adx_14_trend | -1.80% | -7.02% | 2.91% | 1.19% | 40.58% |
| aroon_25_trend | 6.25% | 1.88% | 2.91% | 1.01% | 34.55% |
| cci_20_momentum | 4.75% | -1.65% | 2.91% | 0.71% | 24.35% |
| williams_14_recovery | -2.20% | -8.94% | 2.91% | 0.13% | 4.45% |
| cmf_20_accumulation | 8.42% | 3.53% | 2.91% | 1.16% | 39.53% |
| chaikin_3_10 | 0.90% | -4.47% | 2.91% | 1.27% | 43.46% |
| roc_10_momentum | -0.46% | -7.70% | 2.91% | 0.65% | 21.99% |
| trix_15_trend | 0.34% | -2.57% | 2.91% | 1.17% | 39.79% |
| keltner_20_breakout | 2.61% | -1.61% | 2.91% | 0.48% | 16.23% |
| opening_range_30m | 2.51% | -1.71% | 2.91% | 0.87% | 29.58% |

동일 구간·초기 자금, 종료 시 청산 비용 포함. 노출 맞춤은 사후 설명용이며 v2 실제 계좌 성과가 아닙니다.
[낙폭 분해·비용 영향·전체 구간](JNJ/comparison.json)

[v1 전체 기록](JNJ/accounts.json) · [v2 전체 기록](JNJ/accounts-v2.json)

## CAT 계좌

| 모델 | 전략 | 평가액 USD | 손익 USD | 최근 매매·이유 |
|---|---|---:|---:|---|
| v1 | cash | 10000.00 | 0.00 | 대기 /  / 새 신호 대기 |
| v1 | buy_hold | 9529.11 | -470.89 | buy /  / buy_hold: prior completed bar target 100%; next bar open simulation |
| v1 | trend_8_26 | 9570.52 | -429.48 | sell /  / trend_8_26: prior completed bar target 0%; next bar open simulation |
| v1 | momentum_26 | 9290.58 | -709.42 | sell /  / momentum_26: prior completed bar target 0%; next bar open simulation |
| v1 | breakout_8 | 9544.96 | -455.04 | sell /  / breakout_8: prior completed bar target 0%; next bar open simulation |
| v1 | reversion_12 | 9689.85 | -310.15 | sell /  / reversion_12: prior completed bar target 0%; next bar open simulation |
| v1 | volume_26 | 9683.18 | -316.82 | sell /  / volume_26: prior completed bar target 0%; next bar open simulation |
| v1 | trend_8_26 AND momentum_26 | 9471.21 | -528.79 | sell /  / trend_8_26 AND momentum_26: prior completed bar target 0%; next bar open simulation |
| v1 | trend_8_26 + momentum_26 | 9430.55 | -569.45 | sell /  / trend_8_26 + momentum_26: prior completed bar target 0%; next bar open simulation |
| v1 | trend_8_26 AND breakout_8 | 9747.92 | -252.08 | sell /  / trend_8_26 AND breakout_8: prior completed bar target 0%; next bar open simulation |
| v1 | trend_8_26 + breakout_8 | 9559.68 | -440.32 | sell /  / trend_8_26 + breakout_8: prior completed bar target 0%; next bar open simulation |
| v1 | trend_8_26 AND reversion_12 | 9919.62 | -80.38 | sell /  / trend_8_26 AND reversion_12: prior completed bar target 0%; next bar open simulation |
| v1 | trend_8_26 + reversion_12 | 9690.38 | -309.62 | sell /  / trend_8_26 + reversion_12: prior completed bar target 0%; next bar open simulation |
| v1 | trend_8_26 AND volume_26 | 9965.69 | -34.31 | sell /  / trend_8_26 AND volume_26: prior completed bar target 0%; next bar open simulation |
| v1 | trend_8_26 + volume_26 | 9667.13 | -332.87 | sell /  / trend_8_26 + volume_26: prior completed bar target 0%; next bar open simulation |
| v1 | momentum_26 AND breakout_8 | 9615.85 | -384.15 | sell /  / momentum_26 AND breakout_8: prior completed bar target 0%; next bar open simulation |
| v1 | momentum_26 + breakout_8 | 9417.88 | -582.12 | sell /  / momentum_26 + breakout_8: prior completed bar target 0%; next bar open simulation |
| v1 | momentum_26 AND reversion_12 | 9878.81 | -121.19 | sell /  / momentum_26 AND reversion_12: prior completed bar target 0%; next bar open simulation |
| v1 | momentum_26 + reversion_12 | 9508.61 | -491.39 | sell /  / momentum_26 + reversion_12: prior completed bar target 0%; next bar open simulation |
| v1 | momentum_26 AND volume_26 | 9894.55 | -105.45 | sell /  / momentum_26 AND volume_26: prior completed bar target 0%; next bar open simulation |
| v1 | momentum_26 + volume_26 | 9504.77 | -495.23 | sell /  / momentum_26 + volume_26: prior completed bar target 0%; next bar open simulation |
| v1 | breakout_8 AND reversion_12 | 10000.00 | 0.00 | 대기 /  / 새 신호 대기 |
| v1 | breakout_8 + reversion_12 | 9617.78 | -382.22 | sell /  / breakout_8 + reversion_12: prior completed bar target 0%; next bar open simulation |
| v1 | breakout_8 AND volume_26 | 9894.55 | -105.45 | sell /  / breakout_8 AND volume_26: prior completed bar target 0%; next bar open simulation |
| v1 | breakout_8 + volume_26 | 9614.01 | -385.99 | sell /  / breakout_8 + volume_26: prior completed bar target 0%; next bar open simulation |
| v1 | reversion_12 AND volume_26 | 9810.19 | -189.81 | sell /  / reversion_12 AND volume_26: prior completed bar target 0%; next bar open simulation |
| v1 | reversion_12 + volume_26 | 9686.95 | -313.05 | sell /  / reversion_12 + volume_26: prior completed bar target 0%; next bar open simulation |
| v1 | ema_12_26 | 9597.59 | -402.41 | sell /  / EMA12 > EMA26; 조건 미충족; EMA12=734.57, EMA26=734.673 |
| v1 | macd_12_26_9 | 9988.51 | -11.49 | sell /  / MACD > 신호선 그리고 MACD > 0; 조건 미충족; MACD=2.92675, signal9=3.02629 |
| v1 | rsi_14_recovery | 9950.97 | -49.03 | sell /  / 직전 RSI14 < 30, 현재 RSI14 >= 30 (한 봉 목표); 조건 미충족; RSI14=34.1484, previous_RSI14=34.3526 |
| v1 | bollinger_20_reentry | 9693.48 | -306.52 | sell /  / 직전 종가 < 직전 하단밴드, 현재 하단밴드 <= 종가 <= SMA20 (한 봉 목표); 조건 미충족; close=698.04, lower20=693.892, SMA20=727.609, previous_lower20=698.501 |
| v1 | donchian_20 | 9943.28 | -56.72 | sell /  / 종가 > 현재 봉을 제외한 직전 20봉 최고가; 조건 미충족; close=735.35, prior_high20=745 |
| v1 | atr_14_breakout | 9768.31 | -231.69 | sell /  / 종가 > 직전 종가 + 직전 ATR14 그리고 종가 > EMA26; 조건 미충족; close=735.35, threshold=737.263, prior_ATR14=4.10289, EMA26=727.331 |
| v1 | session_vwap | 9184.29 | -815.71 | sell /  / 종가 > 뉴욕 거래일별 누적 전형가격 VWAP; 조건 미충족; close=702.21, session_VWAP=704.334, session_volume=2.86686e+06 |
| v1 | obv_20 | 9541.23 | -458.77 | sell /  / OBV > OBV의 SMA20 그리고 종가 > EMA26; 조건 미충족; OBV=-4.81948e+06, OBV_SMA20=-4.73979e+06, close=711.18, EMA26=734.673 |
| v1 | stochastic_14_3_recovery | 9732.70 | -267.30 | sell /  / 직전 %K14 < 20에서 %K14가 %D3 상향 돌파 (한 봉 목표); 조건 미충족; K14=32.2335, D3=26.0241, previous_K14=30.5872, previous_D3=22.2626 |
| v1 | mfi_14_recovery | 10068.63 | 68.63 | sell /  / 직전 MFI14 < 20, 현재 MFI14 >= 20 (한 봉 목표); 조건 미충족; MFI14=32.7313, previous_MFI14=24.1736 |
| v1 | adx_14_trend | 9614.13 | -385.87 | sell /  / Wilder ADX14 >= 25 그리고 +DI14 > -DI14; 조건 미충족; ADX14=37.6898, plus_DI14=16.8278, minus_DI14=52.0976 |
| v1 | aroon_25_trend | 9979.61 | -20.39 | sell /  / Aroon25 Up > 70 그리고 Down < 30 (동률이면 최신 극값); 조건 미충족; Aroon_up=68, Aroon_down=20 |
| v1 | cci_20_momentum | 9862.85 | -137.15 | sell /  / CCI20 > 100 (전형가격·평균절대편차); 조건 미충족; CCI20=99.2123 |
| v1 | williams_14_recovery | 9906.75 | -93.25 | sell /  / 직전 Williams %R14 < -80, 현재 >= -80 (한 봉 목표); 조건 미충족; Williams_R14=-67.7665, previous_R14=-69.4128 |
| v1 | cmf_20_accumulation | 9458.11 | -541.89 | sell /  / Chaikin Money Flow20 > 0.1; 조건 미충족; CMF20=0.0105743, volume20=1.36134e+06 |
| v1 | chaikin_3_10 | 9240.53 | -759.47 | sell /  / ADL의 EMA3 - EMA10 > 0 그리고 종가 > EMA26; 조건 미충족; Chaikin3_10=-27551.7, ADL=-5.11151e+06, close=711.18, EMA26=734.673 |
| v1 | roc_10_momentum | 9896.73 | -103.27 | sell /  / 10봉 ROC > 1% 그리고 종가 > EMA26; 조건 미충족; ROC10_percent=0.883016, close=741.47, EMA26=734.681 |
| v1 | trix_15_trend | 9340.52 | -659.48 | sell /  / 15봉 삼중 EMA의 1봉 변화율 TRIX > 0 그리고 종가 > EMA26; 조건 미충족; TRIX15_percent=0.0460682, close=711.18, EMA26=734.673 |
| v1 | keltner_20_breakout | 10000.00 | 0.00 | 대기 /  / 새 신호 대기 |
| v1 | opening_range_30m | 10162.22 | 162.22 | sell /  / 뉴욕 09:30·09:45 두 완료 봉 최고가를 10:00 이후 종가가 돌파; 자료 부족·변동폭 또는 거래량 없음: 대기; close=733.16 |
| v2 | cash | 10000.00 | 0.00 | 대기 /  / 새 신호 대기 |
| v2 | buy_hold | 8763.68 | -1236.32 | 중단: 손실 한도 / buy / partial / 직전 완료 봉 목표 비중 100%; 다음 봉 시가 가정 |
| v2 | trend_8_26 | 9377.37 | -622.63 | 중단: 손실 한도 / buy / partial / 직전 완료 봉 목표 비중 100%; 다음 봉 시가 가정 |
| v2 | momentum_26 | 9180.00 | -820.00 | 중단: 손실 한도 / buy / partial / 직전 완료 봉 목표 비중 100%; 다음 봉 시가 가정 |
| v2 | breakout_8 | 9357.29 | -642.71 | sell / filled / 직전 완료 봉 목표 비중 0%; 다음 봉 시가 가정 |
| v2 | reversion_12 | 8641.29 | -1358.71 | 중단: 손실 한도 / buy / partial / 직전 완료 봉 목표 비중 100%; 다음 봉 시가 가정 |
| v2 | volume_26 | 8888.42 | -1111.58 | 중단: 손실 한도 / buy / partial / 직전 완료 봉 목표 비중 100%; 다음 봉 시가 가정 |
| v2 | trend_8_26 AND momentum_26 | 9391.21 | -608.79 | 중단: 손실 한도 / buy / partial / 직전 완료 봉 목표 비중 100%; 다음 봉 시가 가정 |
| v2 | trend_8_26 + momentum_26 | 9279.16 | -720.84 | 중단: 손실 한도 / buy / partial / 직전 완료 봉 목표 비중 100%; 다음 봉 시가 가정 |
| v2 | trend_8_26 AND breakout_8 | 9655.84 | -344.16 | sell / filled / 직전 완료 봉 목표 비중 0%; 다음 봉 시가 가정 |
| v2 | trend_8_26 + breakout_8 | 9426.02 | -573.98 | sell / filled / 직전 완료 봉 목표 비중 0%; 다음 봉 시가 가정 |
| v2 | trend_8_26 AND reversion_12 | 9728.39 | -271.61 | sell / filled / 직전 완료 봉 목표 비중 0%; 다음 봉 시가 가정 |
| v2 | trend_8_26 + reversion_12 | 9315.94 | -684.06 | sell / filled / 직전 완료 봉 목표 비중 0%; 다음 봉 시가 가정 |
| v2 | trend_8_26 AND volume_26 | 9999.01 | -0.99 | sell / filled / 직전 완료 봉 목표 비중 0%; 다음 봉 시가 가정 |
| v2 | trend_8_26 + volume_26 | 9303.04 | -696.96 | 중단: 손실 한도 / sell / filled / 직전 완료 봉 목표 비중 0%; 다음 봉 시가 가정 |
| v2 | momentum_26 AND breakout_8 | 9576.90 | -423.10 | sell / filled / 직전 완료 봉 목표 비중 0%; 다음 봉 시가 가정 |
| v2 | momentum_26 + breakout_8 | 9325.28 | -674.72 | sell / filled / 직전 완료 봉 목표 비중 0%; 다음 봉 시가 가정 |
| v2 | momentum_26 AND reversion_12 | 9745.30 | -254.70 | sell / filled / 직전 완료 봉 목표 비중 0%; 다음 봉 시가 가정 |
| v2 | momentum_26 + reversion_12 | 9177.89 | -822.11 | sell / filled / 직전 완료 봉 목표 비중 0%; 다음 봉 시가 가정 |
| v2 | momentum_26 AND volume_26 | 9936.85 | -63.15 | sell / filled / 직전 완료 봉 목표 비중 0%; 다음 봉 시가 가정 |
| v2 | momentum_26 + volume_26 | 9203.76 | -796.24 | 중단: 손실 한도 / sell / filled / 직전 완료 봉 목표 비중 0%; 다음 봉 시가 가정 |
| v2 | breakout_8 AND reversion_12 | 10000.00 | 0.00 | 대기 /  / 새 신호 대기 |
| v2 | breakout_8 + reversion_12 | 9610.18 | -389.82 | 중단: 손실 한도 / sell / filled / 직전 완료 봉 목표 비중 0%; 다음 봉 시가 가정 |
| v2 | breakout_8 AND volume_26 | 9887.31 | -112.69 | sell / filled / 직전 완료 봉 목표 비중 0%; 다음 봉 시가 가정 |
| v2 | breakout_8 + volume_26 | 9216.53 | -783.47 | sell / filled / 직전 완료 봉 목표 비중 0%; 다음 봉 시가 가정 |
| v2 | reversion_12 AND volume_26 | 8826.94 | -1173.06 | 중단: 손실 한도 / buy / partial / 직전 완료 봉 목표 비중 100%; 다음 봉 시가 가정 |
| v2 | reversion_12 + volume_26 | 9181.11 | -818.89 | 중단: 손실 한도 / sell / filled / 직전 완료 봉 목표 비중 50%; 다음 봉 시가 가정 |
| v2 | ema_12_26 | 9479.01 | -520.99 | 중단: 손실 한도 / buy / partial / EMA12 > EMA26; 조건 충족; EMA12=726.261, EMA26=726.172; 직전 완료 봉 목표를 다음 봉 시가에 모의 적용 |
| v2 | macd_12_26_9 | 9984.52 | -15.48 | sell / filled / MACD > 신호선 그리고 MACD > 0; 조건 미충족; MACD=2.92675, signal9=3.02629; 직전 완료 봉 목표를 다음 봉 시가에 모의 적용 |
| v2 | rsi_14_recovery | 9945.00 | -55.00 | sell / filled / 직전 RSI14 < 30, 현재 RSI14 >= 30 (한 봉 목표); 조건 미충족; RSI14=34.1484, previous_RSI14=34.3526; 직전 완료 봉 목표를 다음 봉 시가에 모의 적용 |
| v2 | bollinger_20_reentry | 9685.73 | -314.27 | sell / filled / 직전 종가 < 직전 하단밴드, 현재 하단밴드 <= 종가 <= SMA20 (한 봉 목표); 조건 미충족; close=698.04, lower20=693.892, SMA20=727.609, previous_lower20=698.501; 직전 완료 봉 목표를 다음 봉 시가에 모의 적용 |
| v2 | donchian_20 | 9939.30 | -60.70 | sell / filled / 종가 > 현재 봉을 제외한 직전 20봉 최고가; 조건 미충족; close=735.35, prior_high20=745; 직전 완료 봉 목표를 다음 봉 시가에 모의 적용 |
| v2 | atr_14_breakout | 9758.55 | -241.45 | sell / filled / 종가 > 직전 종가 + 직전 ATR14 그리고 종가 > EMA26; 조건 미충족; close=735.35, threshold=737.263, prior_ATR14=4.10289, EMA26=727.331; 직전 완료 봉 목표를 다음 봉 시가에 모의 적용 |
| v2 | session_vwap | 9127.89 | -872.11 | 중단: 손실 한도 / buy / partial / 종가 > 뉴욕 거래일별 누적 전형가격 VWAP; 조건 충족; close=734.98, session_VWAP=734.093, session_volume=764353; 직전 완료 봉 목표를 다음 봉 시가에 모의 적용 |
| v2 | obv_20 | 9415.82 | -584.18 | 중단: 손실 한도 / buy / partial / OBV > OBV의 SMA20 그리고 종가 > EMA26; 조건 충족; OBV=-5.0567e+06, OBV_SMA20=-6.30537e+06, close=733.16, EMA26=726.69; 직전 완료 봉 목표를 다음 봉 시가에 모의 적용 |
| v2 | stochastic_14_3_recovery | 9715.20 | -284.80 | sell / filled / 직전 %K14 < 20에서 %K14가 %D3 상향 돌파 (한 봉 목표); 조건 미충족; K14=32.2335, D3=26.0241, previous_K14=30.5872, previous_D3=22.2626; 직전 완료 봉 목표를 다음 봉 시가에 모의 적용 |
| v2 | mfi_14_recovery | 10064.61 | 64.61 | sell / filled / 직전 MFI14 < 20, 현재 MFI14 >= 20 (한 봉 목표); 조건 미충족; MFI14=32.7313, previous_MFI14=24.1736; 직전 완료 봉 목표를 다음 봉 시가에 모의 적용 |
| v2 | adx_14_trend | 9497.25 | -502.75 | 중단: 손실 한도 / buy / partial / Wilder ADX14 >= 25 그리고 +DI14 > -DI14; 조건 충족; ADX14=25.4031, plus_DI14=35.2628, minus_DI14=13.9603; 직전 완료 봉 목표를 다음 봉 시가에 모의 적용 |
| v2 | aroon_25_trend | 9973.62 | -26.38 | sell / filled / Aroon25 Up > 70 그리고 Down < 30 (동률이면 최신 극값); 조건 미충족; Aroon_up=68, Aroon_down=20; 직전 완료 봉 목표를 다음 봉 시가에 모의 적용 |
| v2 | cci_20_momentum | 9854.97 | -145.03 | sell / filled / CCI20 > 100 (전형가격·평균절대편차); 조건 미충족; CCI20=99.2123; 직전 완료 봉 목표를 다음 봉 시가에 모의 적용 |
| v2 | williams_14_recovery | 9894.87 | -105.13 | sell / filled / 직전 Williams %R14 < -80, 현재 >= -80 (한 봉 목표); 조건 미충족; Williams_R14=-67.7665, previous_R14=-69.4128; 직전 완료 봉 목표를 다음 봉 시가에 모의 적용 |
| v2 | cmf_20_accumulation | 9335.65 | -664.35 | 중단: 손실 한도 / buy / partial / Chaikin Money Flow20 > 0.1; 조건 충족; CMF20=0.145111, volume20=965726; 직전 완료 봉 목표를 다음 봉 시가에 모의 적용 |
| v2 | chaikin_3_10 | 9229.44 | -770.56 | 중단: 손실 한도 / buy / partial / ADL의 EMA3 - EMA10 > 0 그리고 종가 > EMA26; 조건 충족; Chaikin3_10=293683, ADL=-4.91156e+06, close=739.58, EMA26=736.187; 직전 완료 봉 목표를 다음 봉 시가에 모의 적용 |
| v2 | roc_10_momentum | 9888.81 | -111.19 | sell / filled / 10봉 ROC > 1% 그리고 종가 > EMA26; 조건 미충족; ROC10_percent=0.883016, close=741.47, EMA26=734.681; 직전 완료 봉 목표를 다음 봉 시가에 모의 적용 |
| v2 | trix_15_trend | 9238.74 | -761.26 | 중단: 손실 한도 / buy / partial / 15봉 삼중 EMA의 1봉 변화율 TRIX > 0 그리고 종가 > EMA26; 조건 충족; TRIX15_percent=0.0196284, close=739.58, EMA26=736.187; 직전 완료 봉 목표를 다음 봉 시가에 모의 적용 |
| v2 | keltner_20_breakout | 10000.00 | 0.00 | 대기 /  / 새 신호 대기 |
| v2 | opening_range_30m | 10158.15 | 158.15 | sell / filled / 뉴욕 09:30·09:45 두 완료 봉 최고가를 10:00 이후 종가가 돌파; 자료 부족·변동폭 또는 거래량 없음: 대기; close=733.16; 직전 완료 봉 목표를 다음 봉 시가에 모의 적용 |

### 같은 기간의 비용·노출 비교 (사후 연구)

| 전략 | 비용 전 | 비용 후 | 100% 보유 | 같은 평균 노출 보유 | 평균 노출 |
|---|---:|---:|---:|---:|---:|
| cash | 0.00% | 0.00% | -16.96% | -0.00% | 0.00% |
| buy_hold | -16.61% | -16.96% | -16.96% | -16.96% | 100.00% |
| trend_8_26 | -4.17% | -7.72% | -16.96% | -8.06% | 45.55% |
| momentum_26 | -7.62% | -11.79% | -16.96% | -7.70% | 43.46% |
| breakout_8 | -2.56% | -14.45% | -16.96% | -2.75% | 15.18% |
| reversion_12 | -4.72% | -17.05% | -16.96% | -4.84% | 26.96% |
| volume_26 | -2.47% | -10.70% | -16.96% | -1.57% | 8.64% |
| trend_8_26 AND momentum_26 | -3.59% | -6.78% | -16.96% | -6.85% | 38.48% |
| trend_8_26 + momentum_26 | -5.88% | -9.76% | -16.96% | -7.88% | 44.50% |
| trend_8_26 AND breakout_8 | -1.08% | -7.90% | -16.96% | -1.57% | 8.64% |
| trend_8_26 + breakout_8 | -3.32% | -10.93% | -16.96% | -5.44% | 30.37% |
| trend_8_26 AND reversion_12 | 0.96% | -5.20% | -16.96% | -1.00% | 5.50% |
| trend_8_26 + reversion_12 | -4.36% | -11.54% | -16.96% | -6.46% | 36.26% |
| trend_8_26 AND volume_26 | 2.90% | 1.18% | -16.96% | -0.29% | 1.57% |
| trend_8_26 + volume_26 | -3.25% | -8.61% | -16.96% | -4.86% | 27.10% |
| momentum_26 AND breakout_8 | -1.82% | -9.35% | -16.96% | -1.62% | 8.90% |
| momentum_26 + breakout_8 | -5.08% | -13.10% | -16.96% | -5.26% | 29.32% |
| momentum_26 AND reversion_12 | -2.85% | -8.78% | -16.96% | -1.15% | 6.28% |
| momentum_26 + reversion_12 | -6.12% | -14.25% | -16.96% | -6.28% | 35.22% |
| momentum_26 AND volume_26 | 2.69% | 0.55% | -16.96% | -0.29% | 1.57% |
| momentum_26 + volume_26 | -5.02% | -10.65% | -16.96% | -4.68% | 26.05% |
| breakout_8 AND reversion_12 | 0.00% | 0.00% | -16.96% | -0.00% | 0.00% |
| breakout_8 + reversion_12 | -3.58% | -15.03% | -16.96% | -3.80% | 21.08% |
| breakout_8 AND volume_26 | 0.55% | -1.13% | -16.96% | -0.19% | 1.05% |
| breakout_8 + volume_26 | -2.48% | -12.03% | -16.96% | -2.16% | 11.92% |
| reversion_12 AND volume_26 | -1.80% | -7.02% | -16.96% | -1.00% | 5.50% |
| reversion_12 + volume_26 | -3.56% | -13.56% | -16.96% | -3.22% | 17.81% |
| ema_12_26 | -4.42% | -6.01% | -16.96% | -7.39% | 41.62% |
| macd_12_26_9 | 1.32% | -1.20% | -16.96% | -4.56% | 25.39% |
| rsi_14_recovery | 0.37% | -5.76% | -16.96% | -0.72% | 3.93% |
| bollinger_20_reentry | -0.39% | -5.68% | -16.96% | -0.62% | 3.40% |
| donchian_20 | -0.65% | -3.93% | -16.96% | -0.62% | 3.40% |
| atr_14_breakout | -1.18% | -6.04% | -16.96% | -0.62% | 3.40% |
| session_vwap | -2.92% | -14.77% | -16.96% | -8.33% | 47.12% |
| obv_20 | -6.15% | -14.44% | -16.96% | -4.15% | 23.04% |
| stochastic_14_3_recovery | -1.14% | -11.74% | -16.96% | -1.29% | 7.07% |
| mfi_14_recovery | 2.16% | -0.38% | -16.96% | -0.29% | 1.57% |
| adx_14_trend | -5.42% | -7.77% | -16.96% | -2.28% | 12.57% |
| aroon_25_trend | -0.20% | -3.50% | -16.96% | -1.90% | 10.47% |
| cci_20_momentum | -3.28% | -8.04% | -16.96% | -2.66% | 14.66% |
| williams_14_recovery | 0.21% | -7.48% | -16.96% | -0.91% | 4.97% |
| cmf_20_accumulation | -6.74% | -13.53% | -16.96% | -3.55% | 19.63% |
| chaikin_3_10 | -7.94% | -16.07% | -16.96% | -5.67% | 31.68% |
| roc_10_momentum | -1.46% | -7.08% | -16.96% | -2.19% | 12.04% |
| trix_15_trend | -5.56% | -9.44% | -16.96% | -5.99% | 33.51% |
| keltner_20_breakout | -2.06% | -3.70% | -16.96% | -0.34% | 1.83% |
| opening_range_30m | 5.64% | 1.29% | -16.96% | -3.92% | 21.73% |

동일 구간·초기 자금, 종료 시 청산 비용 포함. 노출 맞춤은 사후 설명용이며 v2 실제 계좌 성과가 아닙니다.
[낙폭 분해·비용 영향·전체 구간](CAT/comparison.json)

[v1 전체 기록](CAT/accounts.json) · [v2 전체 기록](CAT/accounts-v2.json)

## WMT 계좌

| 모델 | 전략 | 평가액 USD | 손익 USD | 최근 매매·이유 |
|---|---|---:|---:|---|
| v1 | cash | 10000.00 | 0.00 | 대기 /  / 새 신호 대기 |
| v1 | buy_hold | 10167.98 | 167.98 | buy /  / buy_hold: prior completed bar target 100%; next bar open simulation |
| v1 | trend_8_26 | 9826.11 | -173.89 | buy /  / trend_8_26: prior completed bar target 100%; next bar open simulation |
| v1 | momentum_26 | 9942.48 | -57.52 | buy /  / momentum_26: prior completed bar target 100%; next bar open simulation |
| v1 | breakout_8 | 9407.15 | -592.85 | sell /  / breakout_8: prior completed bar target 0%; next bar open simulation |
| v1 | reversion_12 | 9573.71 | -426.29 | sell /  / reversion_12: prior completed bar target 0%; next bar open simulation |
| v1 | volume_26 | 9775.35 | -224.65 | sell /  / volume_26: prior completed bar target 0%; next bar open simulation |
| v1 | trend_8_26 AND momentum_26 | 9908.11 | -91.89 | buy /  / trend_8_26 AND momentum_26: prior completed bar target 100%; next bar open simulation |
| v1 | trend_8_26 + momentum_26 | 9884.15 | -115.85 | buy /  / trend_8_26 + momentum_26: prior completed bar target 100%; next bar open simulation |
| v1 | trend_8_26 AND breakout_8 | 9668.96 | -331.04 | sell /  / trend_8_26 AND breakout_8: prior completed bar target 0%; next bar open simulation |
| v1 | trend_8_26 + breakout_8 | 9633.82 | -366.18 | sell /  / trend_8_26 + breakout_8: prior completed bar target 50%; next bar open simulation |
| v1 | trend_8_26 AND reversion_12 | 9741.18 | -258.82 | sell /  / trend_8_26 AND reversion_12: prior completed bar target 0%; next bar open simulation |
| v1 | trend_8_26 + reversion_12 | 9738.10 | -261.90 | buy /  / trend_8_26 + reversion_12: prior completed bar target 50%; next bar open simulation |
| v1 | trend_8_26 AND volume_26 | 9837.96 | -162.04 | sell /  / trend_8_26 AND volume_26: prior completed bar target 0%; next bar open simulation |
| v1 | trend_8_26 + volume_26 | 9801.15 | -198.85 | buy /  / trend_8_26 + volume_26: prior completed bar target 50%; next bar open simulation |
| v1 | momentum_26 AND breakout_8 | 9580.59 | -419.41 | sell /  / momentum_26 AND breakout_8: prior completed bar target 0%; next bar open simulation |
| v1 | momentum_26 + breakout_8 | 9729.75 | -270.25 | sell /  / momentum_26 + breakout_8: prior completed bar target 50%; next bar open simulation |
| v1 | momentum_26 AND reversion_12 | 9935.88 | -64.12 | sell /  / momentum_26 AND reversion_12: prior completed bar target 0%; next bar open simulation |
| v1 | momentum_26 + reversion_12 | 9854.36 | -145.64 | buy /  / momentum_26 + reversion_12: prior completed bar target 50%; next bar open simulation |
| v1 | momentum_26 AND volume_26 | 9853.50 | -146.50 | sell /  / momentum_26 AND volume_26: prior completed bar target 0%; next bar open simulation |
| v1 | momentum_26 + volume_26 | 9898.48 | -101.52 | buy /  / momentum_26 + volume_26: prior completed bar target 50%; next bar open simulation |
| v1 | breakout_8 AND reversion_12 | 10000.00 | 0.00 | 대기 /  / 새 신호 대기 |
| v1 | breakout_8 + reversion_12 | 9527.89 | -472.11 | sell /  / breakout_8 + reversion_12: prior completed bar target 0%; next bar open simulation |
| v1 | breakout_8 AND volume_26 | 9797.95 | -202.05 | sell /  / breakout_8 AND volume_26: prior completed bar target 0%; next bar open simulation |
| v1 | breakout_8 + volume_26 | 9589.72 | -410.28 | sell /  / breakout_8 + volume_26: prior completed bar target 0%; next bar open simulation |
| v1 | reversion_12 AND volume_26 | 9911.53 | -88.47 | sell /  / reversion_12 AND volume_26: prior completed bar target 0%; next bar open simulation |
| v1 | reversion_12 + volume_26 | 9732.36 | -267.64 | sell /  / reversion_12 + volume_26: prior completed bar target 0%; next bar open simulation |
| v1 | ema_12_26 | 10047.05 | 47.05 | buy /  / EMA12 > EMA26; 조건 충족; EMA12=117.957, EMA26=117.935 |
| v1 | macd_12_26_9 | 10127.05 | 127.05 | buy /  / MACD > 신호선 그리고 MACD > 0; 조건 충족; MACD=0.0217894, signal9=-0.0690006 |
| v1 | rsi_14_recovery | 9973.19 | -26.81 | sell /  / 직전 RSI14 < 30, 현재 RSI14 >= 30 (한 봉 목표); 조건 미충족; RSI14=46.7246, previous_RSI14=43.1348 |
| v1 | bollinger_20_reentry | 9975.54 | -24.46 | sell /  / 직전 종가 < 직전 하단밴드, 현재 하단밴드 <= 종가 <= SMA20 (한 봉 목표); 조건 미충족; close=117.73, lower20=117.465, SMA20=117.829, previous_lower20=117.475 |
| v1 | donchian_20 | 9764.74 | -235.26 | sell /  / 종가 > 현재 봉을 제외한 직전 20봉 최고가; 조건 미충족; close=120.365, prior_high20=120.495 |
| v1 | atr_14_breakout | 9811.78 | -188.22 | sell /  / 종가 > 직전 종가 + 직전 ATR14 그리고 종가 > EMA26; 조건 미충족; close=120.03, threshold=120.128, prior_ATR14=0.443028, EMA26=118.335 |
| v1 | session_vwap | 9642.61 | -357.39 | buy /  / 종가 > 뉴욕 거래일별 누적 전형가격 VWAP; 조건 충족; close=118.96, session_VWAP=118.576, session_volume=4.484e+06 |
| v1 | obv_20 | 9999.53 | -0.47 | buy /  / OBV > OBV의 SMA20 그리고 종가 > EMA26; 조건 충족; OBV=1.42093e+07, OBV_SMA20=1.04391e+07, close=118.41, EMA26=117.87 |
| v1 | stochastic_14_3_recovery | 9463.72 | -536.28 | sell /  / 직전 %K14 < 20에서 %K14가 %D3 상향 돌파 (한 봉 목표); 조건 미충족; K14=38.3112, D3=17.7755, previous_K14=8.66597, previous_D3=7.09962 |
| v1 | mfi_14_recovery | 9969.08 | -30.92 | sell /  / 직전 MFI14 < 20, 현재 MFI14 >= 20 (한 봉 목표); 조건 미충족; MFI14=57.3162, previous_MFI14=36.5877 |
| v1 | adx_14_trend | 10135.54 | 135.54 | buy /  / Wilder ADX14 >= 25 그리고 +DI14 > -DI14; 조건 충족; ADX14=32.9742, plus_DI14=41.4463, minus_DI14=15.2475 |
| v1 | aroon_25_trend | 9944.88 | -55.12 | buy /  / Aroon25 Up > 70 그리고 Down < 30 (동률이면 최신 극값); 조건 충족; Aroon_up=88, Aroon_down=28 |
| v1 | cci_20_momentum | 9804.61 | -195.39 | sell /  / CCI20 > 100 (전형가격·평균절대편차); 조건 미충족; CCI20=84.7671 |
| v1 | williams_14_recovery | 9739.33 | -260.67 | sell /  / 직전 Williams %R14 < -80, 현재 >= -80 (한 봉 목표); 조건 미충족; Williams_R14=-50.649, previous_R14=-61.6888 |
| v1 | cmf_20_accumulation | 9765.06 | -234.94 | buy /  / Chaikin Money Flow20 > 0.1; 조건 충족; CMF20=0.134813, volume20=1.25189e+07 |
| v1 | chaikin_3_10 | 9756.04 | -243.96 | buy /  / ADL의 EMA3 - EMA10 > 0 그리고 종가 > EMA26; 조건 충족; Chaikin3_10=239030, ADL=8.86177e+06, close=118.96, EMA26=118.011 |
| v1 | roc_10_momentum | 10091.95 | 91.95 | sell /  / 10봉 ROC > 1% 그리고 종가 > EMA26; 조건 미충족; ROC10_percent=0.710203, close=120.535, EMA26=119.283 |
| v1 | trix_15_trend | 9743.50 | -256.50 | buy /  / 15봉 삼중 EMA의 1봉 변화율 TRIX > 0 그리고 종가 > EMA26; 조건 충족; TRIX15_percent=0.00531527, close=119.685, EMA26=118.199 |
| v1 | keltner_20_breakout | 10003.21 | 3.21 | sell /  / 종가 > EMA20 + 2 x Wilder ATR14; 조건 미충족; close=120.245, upper_Keltner=120.371, EMA20=119.575, ATR14=0.397892 |
| v1 | opening_range_30m | 9820.97 | -179.03 | buy /  / 뉴욕 09:30·09:45 두 완료 봉 최고가를 10:00 이후 종가가 돌파; 조건 충족; close=119.685, opening_high=119.42 |
| v2 | cash | 10000.00 | 0.00 | 대기 /  / 새 신호 대기 |
| v2 | buy_hold | 10772.88 | 772.88 | buy / partial / 직전 완료 봉 목표 비중 100%; 다음 봉 시가 가정 |
| v2 | trend_8_26 | 10220.39 | 220.39 | buy / partial / 직전 완료 봉 목표 비중 100%; 다음 봉 시가 가정 |
| v2 | momentum_26 | 10346.33 | 346.33 | buy / partial / 직전 완료 봉 목표 비중 100%; 다음 봉 시가 가정 |
| v2 | breakout_8 | 9347.68 | -652.32 | sell / filled / 직전 완료 봉 목표 비중 0%; 다음 봉 시가 가정 |
| v2 | reversion_12 | 9466.17 | -533.83 | sell / filled / 직전 완료 봉 목표 비중 0%; 다음 봉 시가 가정 |
| v2 | volume_26 | 9727.78 | -272.22 | sell / filled / 직전 완료 봉 목표 비중 0%; 다음 봉 시가 가정 |
| v2 | trend_8_26 AND momentum_26 | 10305.68 | 305.68 | buy / partial / 직전 완료 봉 목표 비중 100%; 다음 봉 시가 가정 |
| v2 | trend_8_26 + momentum_26 | 10283.13 | 283.13 | buy / partial / 직전 완료 봉 목표 비중 100%; 다음 봉 시가 가정 |
| v2 | trend_8_26 AND breakout_8 | 9738.98 | -261.02 | sell / filled / 직전 완료 봉 목표 비중 0%; 다음 봉 시가 가정 |
| v2 | trend_8_26 + breakout_8 | 9795.46 | -204.54 | sell / filled / 직전 완료 봉 목표 비중 50%; 다음 봉 시가 가정 |
| v2 | trend_8_26 AND reversion_12 | 9545.32 | -454.68 | sell / filled / 직전 완료 봉 목표 비중 0%; 다음 봉 시가 가정 |
| v2 | trend_8_26 + reversion_12 | 9878.96 | -121.04 | buy / filled / 직전 완료 봉 목표 비중 50%; 다음 봉 시가 가정 |
| v2 | trend_8_26 AND volume_26 | 9784.10 | -215.90 | sell / filled / 직전 완료 봉 목표 비중 0%; 다음 봉 시가 가정 |
| v2 | trend_8_26 + volume_26 | 9972.90 | -27.10 | buy / filled / 직전 완료 봉 목표 비중 50%; 다음 봉 시가 가정 |
| v2 | momentum_26 AND breakout_8 | 9527.65 | -472.35 | sell / filled / 직전 완료 봉 목표 비중 0%; 다음 봉 시가 가정 |
| v2 | momentum_26 + breakout_8 | 9897.32 | -102.68 | sell / filled / 직전 완료 봉 목표 비중 50%; 다음 봉 시가 가정 |
| v2 | momentum_26 AND reversion_12 | 9759.91 | -240.09 | sell / filled / 직전 완료 봉 목표 비중 0%; 다음 봉 시가 가정 |
| v2 | momentum_26 + reversion_12 | 10044.43 | 44.43 | buy / filled / 직전 완료 봉 목표 비중 50%; 다음 봉 시가 가정 |
| v2 | momentum_26 AND volume_26 | 9760.78 | -239.22 | sell / filled / 직전 완료 봉 목표 비중 0%; 다음 봉 시가 가정 |
| v2 | momentum_26 + volume_26 | 10076.39 | 76.39 | buy / filled / 직전 완료 봉 목표 비중 50%; 다음 봉 시가 가정 |
| v2 | breakout_8 AND reversion_12 | 10000.00 | 0.00 | 대기 /  / 새 신호 대기 |
| v2 | breakout_8 + reversion_12 | 9467.03 | -532.97 | sell / filled / 직전 완료 봉 목표 비중 0%; 다음 봉 시가 가정 |
| v2 | breakout_8 AND volume_26 | 9741.39 | -258.61 | sell / filled / 직전 완료 봉 목표 비중 0%; 다음 봉 시가 가정 |
| v2 | breakout_8 + volume_26 | 9537.37 | -462.63 | sell / filled / 직전 완료 봉 목표 비중 0%; 다음 봉 시가 가정 |
| v2 | reversion_12 AND volume_26 | 9917.25 | -82.75 | sell / filled / 직전 완료 봉 목표 비중 0%; 다음 봉 시가 가정 |
| v2 | reversion_12 + volume_26 | 9656.74 | -343.26 | sell / filled / 직전 완료 봉 목표 비중 0%; 다음 봉 시가 가정 |
| v2 | ema_12_26 | 10042.03 | 42.03 | buy / partial / EMA12 > EMA26; 조건 충족; EMA12=117.957, EMA26=117.935; 직전 완료 봉 목표를 다음 봉 시가에 모의 적용 |
| v2 | macd_12_26_9 | 10121.99 | 121.99 | buy / partial / MACD > 신호선 그리고 MACD > 0; 조건 충족; MACD=0.0217894, signal9=-0.0690006; 직전 완료 봉 목표를 다음 봉 시가에 모의 적용 |
| v2 | rsi_14_recovery | 9971.19 | -28.81 | sell / filled / 직전 RSI14 < 30, 현재 RSI14 >= 30 (한 봉 목표); 조건 미충족; RSI14=46.7246, previous_RSI14=43.1348; 직전 완료 봉 목표를 다음 봉 시가에 모의 적용 |
| v2 | bollinger_20_reentry | 9967.56 | -32.44 | sell / filled / 직전 종가 < 직전 하단밴드, 현재 하단밴드 <= 종가 <= SMA20 (한 봉 목표); 조건 미충족; close=117.73, lower20=117.465, SMA20=117.829, previous_lower20=117.475; 직전 완료 봉 목표를 다음 봉 시가에 모의 적용 |
| v2 | donchian_20 | 9754.98 | -245.02 | sell / filled / 종가 > 현재 봉을 제외한 직전 20봉 최고가; 조건 미충족; close=120.365, prior_high20=120.495; 직전 완료 봉 목표를 다음 봉 시가에 모의 적용 |
| v2 | atr_14_breakout | 9801.98 | -198.02 | sell / filled / 종가 > 직전 종가 + 직전 ATR14 그리고 종가 > EMA26; 조건 미충족; close=120.03, threshold=120.128, prior_ATR14=0.443028, EMA26=118.335; 직전 완료 봉 목표를 다음 봉 시가에 모의 적용 |
| v2 | session_vwap | 9622.38 | -377.62 | buy / partial / 종가 > 뉴욕 거래일별 누적 전형가격 VWAP; 조건 충족; close=118.96, session_VWAP=118.576, session_volume=4.484e+06; 직전 완료 봉 목표를 다음 봉 시가에 모의 적용 |
| v2 | obv_20 | 9988.54 | -11.46 | buy / partial / OBV > OBV의 SMA20 그리고 종가 > EMA26; 조건 충족; OBV=1.42093e+07, OBV_SMA20=1.04391e+07, close=118.41, EMA26=117.87; 직전 완료 봉 목표를 다음 봉 시가에 모의 적용 |
| v2 | stochastic_14_3_recovery | 9866.20 | -133.80 | 중단: 손실 한도 / buy / partial / 직전 %K14 < 20에서 %K14가 %D3 상향 돌파 (한 봉 목표); 조건 충족; K14=25.6758, D3=22.4971, previous_K14=12.8379, previous_D3=25.8704; 직전 완료 봉 목표를 다음 봉 시가에 모의 적용 |
| v2 | mfi_14_recovery | 9961.11 | -38.89 | sell / filled / 직전 MFI14 < 20, 현재 MFI14 >= 20 (한 봉 목표); 조건 미충족; MFI14=57.3162, previous_MFI14=36.5877; 직전 완료 봉 목표를 다음 봉 시가에 모의 적용 |
| v2 | adx_14_trend | 10132.50 | 132.50 | buy / partial / Wilder ADX14 >= 25 그리고 +DI14 > -DI14; 조건 충족; ADX14=32.9742, plus_DI14=41.4463, minus_DI14=15.2475; 직전 완료 봉 목표를 다음 봉 시가에 모의 적용 |
| v2 | aroon_25_trend | 9937.92 | -62.08 | buy / partial / Aroon25 Up > 70 그리고 Down < 30 (동률이면 최신 극값); 조건 충족; Aroon_up=88, Aroon_down=28; 직전 완료 봉 목표를 다음 봉 시가에 모의 적용 |
| v2 | cci_20_momentum | 9794.81 | -205.19 | sell / filled / CCI20 > 100 (전형가격·평균절대편차); 조건 미충족; CCI20=84.7671; 직전 완료 봉 목표를 다음 봉 시가에 모의 적용 |
| v2 | williams_14_recovery | 9725.71 | -274.29 | sell / filled / 직전 Williams %R14 < -80, 현재 >= -80 (한 봉 목표); 조건 미충족; Williams_R14=-50.649, previous_R14=-61.6888; 직전 완료 봉 목표를 다음 봉 시가에 모의 적용 |
| v2 | cmf_20_accumulation | 9752.37 | -247.63 | buy / partial / Chaikin Money Flow20 > 0.1; 조건 충족; CMF20=0.134813, volume20=1.25189e+07; 직전 완료 봉 목표를 다음 봉 시가에 모의 적용 |
| v2 | chaikin_3_10 | 9737.52 | -262.48 | buy / partial / ADL의 EMA3 - EMA10 > 0 그리고 종가 > EMA26; 조건 충족; Chaikin3_10=239030, ADL=8.86177e+06, close=118.96, EMA26=118.011; 직전 완료 봉 목표를 다음 봉 시가에 모의 적용 |
| v2 | roc_10_momentum | 10089.93 | 89.93 | sell / filled / 10봉 ROC > 1% 그리고 종가 > EMA26; 조건 미충족; ROC10_percent=0.710203, close=120.535, EMA26=119.283; 직전 완료 봉 목표를 다음 봉 시가에 모의 적용 |
| v2 | trix_15_trend | 9730.84 | -269.16 | buy / partial / 15봉 삼중 EMA의 1봉 변화율 TRIX > 0 그리고 종가 > EMA26; 조건 충족; TRIX15_percent=0.00531527, close=119.685, EMA26=118.199; 직전 완료 봉 목표를 다음 봉 시가에 모의 적용 |
| v2 | keltner_20_breakout | 9999.21 | -0.79 | sell / filled / 종가 > EMA20 + 2 x Wilder ATR14; 조건 미충족; close=120.245, upper_Keltner=120.371, EMA20=119.575, ATR14=0.397892; 직전 완료 봉 목표를 다음 봉 시가에 모의 적용 |
| v2 | opening_range_30m | 9812.14 | -187.86 | buy / partial / 뉴욕 09:30·09:45 두 완료 봉 최고가를 10:00 이후 종가가 돌파; 조건 충족; close=119.685, opening_high=119.42; 직전 완료 봉 목표를 다음 봉 시가에 모의 적용 |

### 같은 기간의 비용·노출 비교 (사후 연구)

| 전략 | 비용 전 | 비용 후 | 100% 보유 | 같은 평균 노출 보유 | 평균 노출 |
|---|---:|---:|---:|---:|---:|
| cash | 0.00% | 0.00% | 14.24% | 0.00% | 0.00% |
| buy_hold | 14.73% | 14.24% | 14.24% | 14.24% | 100.00% |
| trend_8_26 | 9.80% | 5.73% | 14.24% | 9.74% | 69.90% |
| momentum_26 | 13.05% | 7.95% | 14.24% | 10.24% | 73.30% |
| breakout_8 | 6.30% | -11.64% | 14.24% | 3.68% | 27.23% |
| reversion_12 | 3.39% | -7.31% | 14.24% | 2.39% | 17.80% |
| volume_26 | 2.19% | -4.05% | 14.24% | 0.80% | 6.02% |
| trend_8_26 AND momentum_26 | 10.72% | 6.61% | 14.24% | 9.05% | 65.18% |
| trend_8_26 + momentum_26 | 11.42% | 6.83% | 14.24% | 9.99% | 71.60% |
| trend_8_26 AND breakout_8 | 6.76% | -7.84% | 14.24% | 3.07% | 22.77% |
| trend_8_26 + breakout_8 | 8.05% | -3.13% | 14.24% | 6.66% | 48.57% |
| trend_8_26 AND reversion_12 | -0.52% | -6.20% | 14.24% | 0.87% | 6.54% |
| trend_8_26 + reversion_12 | 6.59% | -0.37% | 14.24% | 6.00% | 43.85% |
| trend_8_26 AND volume_26 | 0.24% | -2.26% | 14.24% | 0.28% | 2.09% |
| trend_8_26 + volume_26 | 5.97% | 1.16% | 14.24% | 5.17% | 37.96% |
| momentum_26 AND breakout_8 | 6.59% | -9.51% | 14.24% | 3.39% | 25.13% |
| momentum_26 + breakout_8 | 9.64% | -1.70% | 14.24% | 6.91% | 50.27% |
| momentum_26 AND reversion_12 | 1.65% | -4.16% | 14.24% | 0.98% | 7.33% |
| momentum_26 + reversion_12 | 8.16% | 1.95% | 14.24% | 6.24% | 45.55% |
| momentum_26 AND volume_26 | 1.51% | -3.07% | 14.24% | 0.42% | 3.14% |
| momentum_26 + volume_26 | 7.53% | 2.22% | 14.24% | 5.41% | 39.66% |
| breakout_8 AND reversion_12 | 0.00% | 0.00% | 14.24% | 0.00% | 0.00% |
| breakout_8 + reversion_12 | 4.86% | -8.73% | 14.24% | 3.03% | 22.52% |
| breakout_8 AND volume_26 | 0.64% | -2.68% | 14.24% | 0.31% | 2.36% |
| breakout_8 + volume_26 | 4.25% | -7.72% | 14.24% | 2.23% | 16.63% |
| reversion_12 AND volume_26 | 0.01% | -2.48% | 14.24% | 0.24% | 1.83% |
| reversion_12 + volume_26 | 2.80% | -4.90% | 14.24% | 1.59% | 11.92% |
| ema_12_26 | 13.00% | 11.12% | 14.24% | 10.70% | 76.44% |
| macd_12_26_9 | 10.43% | 5.89% | 14.24% | 5.46% | 40.05% |
| rsi_14_recovery | 0.20% | -0.64% | 14.24% | 0.07% | 0.52% |
| bollinger_20_reentry | 2.08% | -0.46% | 14.24% | 0.21% | 1.57% |
| donchian_20 | 4.47% | -8.66% | 14.24% | 1.86% | 13.87% |
| atr_14_breakout | -0.69% | -10.96% | 14.24% | 1.05% | 7.85% |
| session_vwap | 9.74% | -1.61% | 14.24% | 8.18% | 59.16% |
| obv_20 | 12.68% | 4.91% | 14.24% | 8.26% | 59.69% |
| stochastic_14_3_recovery | 0.13% | -8.71% | 14.24% | 0.77% | 5.76% |
| mfi_14_recovery | 1.30% | -0.39% | 14.24% | 0.14% | 1.05% |
| adx_14_trend | 10.51% | 7.76% | 14.24% | 7.47% | 54.19% |
| aroon_25_trend | 7.50% | 1.79% | 14.24% | 4.22% | 31.15% |
| cci_20_momentum | 7.51% | -1.57% | 14.24% | 4.73% | 34.82% |
| williams_14_recovery | 0.89% | -7.63% | 14.24% | 0.73% | 5.50% |
| cmf_20_accumulation | 9.41% | 0.17% | 14.24% | 5.76% | 42.15% |
| chaikin_3_10 | 10.87% | 1.09% | 14.24% | 7.65% | 55.50% |
| roc_10_momentum | 1.03% | -3.94% | 14.24% | 2.28% | 17.02% |
| trix_15_trend | 11.60% | 7.01% | 14.24% | 9.43% | 67.80% |
| keltner_20_breakout | 7.74% | 0.74% | 14.24% | 4.04% | 29.84% |
| opening_range_30m | 10.34% | 4.04% | 14.24% | 5.50% | 40.31% |

동일 구간·초기 자금, 종료 시 청산 비용 포함. 노출 맞춤은 사후 설명용이며 v2 실제 계좌 성과가 아닙니다.
[낙폭 분해·비용 영향·전체 구간](WMT/comparison.json)

[v1 전체 기록](WMT/accounts.json) · [v2 전체 기록](WMT/accounts-v2.json)
