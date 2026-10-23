# 모의투자 운영 현황

[PC·서버 장애 진단과 복구 방법](https://github.com/BaekJaeYeol/paper-trading-program/blob/main/investment-lab/docs/failure-recovery.md)

이번 실행 복구: {}

완료 봉 확인 주기: 기록 11/19회 · 기록 없는 예정 8회 · 아직 판정 전 7회 · 주의: 예약 시작 지연 또는 실행·저장 누락을 확인하세요.

[주기 판정 기준](https://github.com/BaekJaeYeol/paper-trading-program/blob/main/investment-lab/docs/session-coverage.md)

최근 확인: 2026-10-23T18:37:00.345172+00:00 (UTC)
다음 15분 확인 목표 (세션 실행 중에만 적용): 2026-10-23T18:52:00+00:00 (UTC, 실행 지연 가능)

실제 주문 없음. v1 기존 계좌와 v2 새 계좌의 시작일이 다르므로 수익률을 직접 우열 비교하지 마세요.
v2는 다음 봉 시가에 비용·스프레드·직전 거래량 제한을 적용한 가상 체결입니다. 미체결 잔량은 만료됩니다.

| 종목 | 상태 | 최근 성공 UTC | 마지막 완료 봉 UTC | 이번 새 봉 |
|---|---|---|---|---|
| SPY | updated | 2026-10-23T18:37:00.345172+00:00 | 2026-10-23T18:15:00+00:00 | 1 |
| QQQ | updated | 2026-10-23T18:37:00.345172+00:00 | 2026-10-23T18:15:00+00:00 | 1 |
| IWM | updated | 2026-10-23T18:37:00.345172+00:00 | 2026-10-23T18:15:00+00:00 | 1 |
| DIA | updated | 2026-10-23T18:37:00.345172+00:00 | 2026-10-23T18:15:00+00:00 | 1 |
| MSFT | updated | 2026-10-23T18:37:00.345172+00:00 | 2026-10-23T18:15:00+00:00 | 1 |
| JPM | updated | 2026-10-23T18:37:00.345172+00:00 | 2026-10-23T18:15:00+00:00 | 1 |
| XOM | updated | 2026-10-23T18:37:00.345172+00:00 | 2026-10-23T18:15:00+00:00 | 1 |
| JNJ | updated | 2026-10-23T18:37:00.345172+00:00 | 2026-10-23T18:15:00+00:00 | 1 |
| CAT | updated | 2026-10-23T18:37:00.345172+00:00 | 2026-10-23T18:15:00+00:00 | 1 |
| WMT | updated | 2026-10-23T18:37:00.345172+00:00 | 2026-10-23T18:15:00+00:00 | 1 |

이번 실행 소요: 51.28초
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
| v1 | buy_hold | 9820.76 | -179.24 | buy /  / buy_hold: prior completed bar target 100%; next bar open simulation |
| v1 | trend_8_26 | 9657.97 | -342.03 | sell /  / trend_8_26: prior completed bar target 0%; next bar open simulation |
| v1 | momentum_26 | 9631.54 | -368.46 | sell /  / momentum_26: prior completed bar target 0%; next bar open simulation |
| v1 | breakout_8 | 9427.76 | -572.24 | sell /  / breakout_8: prior completed bar target 0%; next bar open simulation |
| v1 | reversion_12 | 9454.44 | -545.56 | sell /  / reversion_12: prior completed bar target 0%; next bar open simulation |
| v1 | volume_26 | 9315.07 | -684.93 | sell /  / volume_26: prior completed bar target 0%; next bar open simulation |
| v1 | trend_8_26 AND momentum_26 | 9624.28 | -375.72 | sell /  / trend_8_26 AND momentum_26: prior completed bar target 0%; next bar open simulation |
| v1 | trend_8_26 + momentum_26 | 9644.71 | -355.29 | sell /  / trend_8_26 + momentum_26: prior completed bar target 0%; next bar open simulation |
| v1 | trend_8_26 AND breakout_8 | 9730.71 | -269.29 | sell /  / trend_8_26 AND breakout_8: prior completed bar target 0%; next bar open simulation |
| v1 | trend_8_26 + breakout_8 | 9580.32 | -419.68 | sell /  / trend_8_26 + breakout_8: prior completed bar target 0%; next bar open simulation |
| v1 | trend_8_26 AND reversion_12 | 9736.23 | -263.77 | sell /  / trend_8_26 AND reversion_12: prior completed bar target 0%; next bar open simulation |
| v1 | trend_8_26 + reversion_12 | 9574.56 | -425.44 | sell /  / trend_8_26 + reversion_12: prior completed bar target 0%; next bar open simulation |
| v1 | trend_8_26 AND volume_26 | 9605.36 | -394.64 | sell /  / trend_8_26 AND volume_26: prior completed bar target 0%; next bar open simulation |
| v1 | trend_8_26 + volume_26 | 9484.78 | -515.22 | sell /  / trend_8_26 + volume_26: prior completed bar target 0%; next bar open simulation |
| v1 | momentum_26 AND breakout_8 | 9640.01 | -359.99 | sell /  / momentum_26 AND breakout_8: prior completed bar target 0%; next bar open simulation |
| v1 | momentum_26 + breakout_8 | 9529.11 | -470.89 | sell /  / momentum_26 + breakout_8: prior completed bar target 0%; next bar open simulation |
| v1 | momentum_26 AND reversion_12 | 9769.70 | -230.30 | sell /  / momentum_26 AND reversion_12: prior completed bar target 0%; next bar open simulation |
| v1 | momentum_26 + reversion_12 | 9599.82 | -400.18 | sell /  / momentum_26 + reversion_12: prior completed bar target 0%; next bar open simulation |
| v1 | momentum_26 AND volume_26 | 9618.73 | -381.27 | sell /  / momentum_26 AND volume_26: prior completed bar target 0%; next bar open simulation |
| v1 | momentum_26 + volume_26 | 9471.81 | -528.19 | sell /  / momentum_26 + volume_26: prior completed bar target 0%; next bar open simulation |
| v1 | breakout_8 AND reversion_12 | 10000.00 | 0.00 | 대기 /  / 새 신호 대기 |
| v1 | breakout_8 + reversion_12 | 9478.47 | -521.53 | sell /  / breakout_8 + reversion_12: prior completed bar target 0%; next bar open simulation |
| v1 | breakout_8 AND volume_26 | 9807.14 | -192.86 | sell /  / breakout_8 AND volume_26: prior completed bar target 0%; next bar open simulation |
| v1 | breakout_8 + volume_26 | 9408.46 | -591.54 | sell /  / breakout_8 + volume_26: prior completed bar target 0%; next bar open simulation |
| v1 | reversion_12 AND volume_26 | 9811.81 | -188.19 | sell /  / reversion_12 AND volume_26: prior completed bar target 0%; next bar open simulation |
| v1 | reversion_12 + volume_26 | 9478.47 | -521.53 | sell /  / reversion_12 + volume_26: prior completed bar target 0%; next bar open simulation |
| v1 | ema_12_26 | 9742.51 | -257.49 | sell /  / EMA12 > EMA26; 조건 미충족; EMA12=771.277, EMA26=771.539 |
| v1 | macd_12_26_9 | 9769.55 | -230.45 | sell /  / MACD > 신호선 그리고 MACD > 0; 조건 미충족; MACD=1.03945, signal9=1.12358 |
| v1 | rsi_14_recovery | 9805.98 | -194.02 | sell /  / 직전 RSI14 < 30, 현재 RSI14 >= 30 (한 봉 목표); 조건 미충족; RSI14=38.7389, previous_RSI14=37.2051 |
| v1 | bollinger_20_reentry | 9716.86 | -283.14 | sell /  / 직전 종가 < 직전 하단밴드, 현재 하단밴드 <= 종가 <= SMA20 (한 봉 목표); 조건 미충족; close=762.88, lower20=759.962, SMA20=762.264, previous_lower20=759.738 |
| v1 | donchian_20 | 9818.08 | -181.92 | sell /  / 종가 > 현재 봉을 제외한 직전 20봉 최고가; 조건 미충족; close=774.19, prior_high20=774.44 |
| v1 | atr_14_breakout | 9816.89 | -183.11 | sell /  / 종가 > 직전 종가 + 직전 ATR14 그리고 종가 > EMA26; 조건 미충족; close=773.07, threshold=774.291, prior_ATR14=1.05565, EMA26=772.249 |
| v1 | session_vwap | 9390.31 | -609.69 | sell /  / 종가 > 뉴욕 거래일별 누적 전형가격 VWAP; 조건 미충족; close=761.36, session_VWAP=761.482, session_volume=3.37356e+07 |
| v1 | obv_20 | 9597.93 | -402.07 | sell /  / OBV > OBV의 SMA20 그리고 종가 > EMA26; 조건 미충족; OBV=-588094, OBV_SMA20=-9.96088e+06, close=766.62, EMA26=771.893 |
| v1 | stochastic_14_3_recovery | 9461.72 | -538.28 | sell /  / 직전 %K14 < 20에서 %K14가 %D3 상향 돌파 (한 봉 목표); 조건 미충족; K14=78.2126, D3=50.4634, previous_K14=55.1135, previous_D3=31.7922 |
| v1 | mfi_14_recovery | 9810.25 | -189.75 | sell /  / 직전 MFI14 < 20, 현재 MFI14 >= 20 (한 봉 목표); 조건 미충족; MFI14=24.2496, previous_MFI14=22.3876 |
| v1 | adx_14_trend | 9981.96 | -18.04 | sell /  / Wilder ADX14 >= 25 그리고 +DI14 > -DI14; 조건 미충족; ADX14=24.2312, plus_DI14=28.3519, minus_DI14=24.6578 |
| v1 | aroon_25_trend | 9728.66 | -271.34 | sell /  / Aroon25 Up > 70 그리고 Down < 30 (동률이면 최신 극값); 조건 미충족; Aroon_up=72, Aroon_down=100 |
| v1 | cci_20_momentum | 9766.23 | -233.77 | sell /  / CCI20 > 100 (전형가격·평균절대편차); 조건 미충족; CCI20=97.3932 |
| v1 | williams_14_recovery | 9410.56 | -589.44 | sell /  / 직전 Williams %R14 < -80, 현재 >= -80 (한 봉 목표); 조건 미충족; Williams_R14=-21.7874, previous_R14=-44.8865 |
| v1 | cmf_20_accumulation | 9643.56 | -356.44 | buy /  / Chaikin Money Flow20 > 0.1; 조건 충족; CMF20=0.264253, volume20=5.65809e+07 |
| v1 | chaikin_3_10 | 9518.83 | -481.17 | sell /  / ADL의 EMA3 - EMA10 > 0 그리고 종가 > EMA26; 조건 미충족; Chaikin3_10=2.35994e+06, ADL=6.37828e+07, close=762.39, EMA26=762.974 |
| v1 | roc_10_momentum | 9953.42 | -46.58 | sell /  / 10봉 ROC > 1% 그리고 종가 > EMA26; 조건 미충족; ROC10_percent=0.806376, close=769.45, EMA26=767.181 |
| v1 | trix_15_trend | 9489.99 | -510.01 | sell /  / 15봉 삼중 EMA의 1봉 변화율 TRIX > 0 그리고 종가 > EMA26; 조건 미충족; TRIX15_percent=0.0154379, close=766.62, EMA26=771.893 |
| v1 | keltner_20_breakout | 9810.90 | -189.10 | sell /  / 종가 > EMA20 + 2 x Wilder ATR14; 조건 미충족; close=774.19, upper_Keltner=774.31, EMA20=772.615, ATR14=0.847257 |
| v1 | opening_range_30m | 9598.85 | -401.15 | sell /  / 뉴욕 09:30·09:45 두 완료 봉 최고가를 10:00 이후 종가가 돌파; 조건 미충족; close=760.59, opening_high=761.2 |
| v2 | cash | 10000.00 | 0.00 | 대기 /  / 새 신호 대기 |
| v2 | buy_hold | 9749.93 | -250.07 | buy / partial / 직전 완료 봉 목표 비중 100%; 다음 봉 시가 가정 |
| v2 | trend_8_26 | 9536.87 | -463.13 | sell / filled / 직전 완료 봉 목표 비중 0%; 다음 봉 시가 가정 |
| v2 | momentum_26 | 9482.22 | -517.78 | sell / filled / 직전 완료 봉 목표 비중 0%; 다음 봉 시가 가정 |
| v2 | breakout_8 | 9024.03 | -975.97 | sell / filled / 직전 완료 봉 목표 비중 0%; 다음 봉 시가 가정 |
| v2 | reversion_12 | 9005.17 | -994.83 | 중단: 손실 한도 / buy / partial / 직전 완료 봉 목표 비중 100%; 다음 봉 시가 가정 |
| v2 | volume_26 | 8962.56 | -1037.44 | 중단: 손실 한도 / buy / partial / 직전 완료 봉 목표 비중 100%; 다음 봉 시가 가정 |
| v2 | trend_8_26 AND momentum_26 | 9481.53 | -518.47 | sell / filled / 직전 완료 봉 목표 비중 0%; 다음 봉 시가 가정 |
| v2 | trend_8_26 + momentum_26 | 9509.48 | -490.52 | sell / filled / 직전 완료 봉 목표 비중 0%; 다음 봉 시가 가정 |
| v2 | trend_8_26 AND breakout_8 | 9547.25 | -452.75 | sell / filled / 직전 완료 봉 목표 비중 0%; 다음 봉 시가 가정 |
| v2 | trend_8_26 + breakout_8 | 9315.73 | -684.27 | sell / filled / 직전 완료 봉 목표 비중 0%; 다음 봉 시가 가정 |
| v2 | trend_8_26 AND reversion_12 | 9621.61 | -378.39 | sell / filled / 직전 완료 봉 목표 비중 0%; 다음 봉 시가 가정 |
| v2 | trend_8_26 + reversion_12 | 9278.51 | -721.49 | sell / filled / 직전 완료 봉 목표 비중 0%; 다음 봉 시가 가정 |
| v2 | trend_8_26 AND volume_26 | 9442.22 | -557.78 | sell / filled / 직전 완료 봉 목표 비중 0%; 다음 봉 시가 가정 |
| v2 | trend_8_26 + volume_26 | 9162.47 | -837.53 | sell / filled / 직전 완료 봉 목표 비중 0%; 다음 봉 시가 가정 |
| v2 | momentum_26 AND breakout_8 | 9414.38 | -585.62 | sell / filled / 직전 완료 봉 목표 비중 0%; 다음 봉 시가 가정 |
| v2 | momentum_26 + breakout_8 | 9250.22 | -749.78 | sell / filled / 직전 완료 봉 목표 비중 0%; 다음 봉 시가 가정 |
| v2 | momentum_26 AND reversion_12 | 9722.08 | -277.92 | sell / filled / 직전 완료 봉 목표 비중 0%; 다음 봉 시가 가정 |
| v2 | momentum_26 + reversion_12 | 9310.42 | -689.58 | sell / filled / 직전 완료 봉 목표 비중 0%; 다음 봉 시가 가정 |
| v2 | momentum_26 AND volume_26 | 9523.88 | -476.12 | sell / filled / 직전 완료 봉 목표 비중 0%; 다음 봉 시가 가정 |
| v2 | momentum_26 + volume_26 | 9174.62 | -825.38 | sell / filled / 직전 완료 봉 목표 비중 0%; 다음 봉 시가 가정 |
| v2 | breakout_8 AND reversion_12 | 10000.00 | 0.00 | 대기 /  / 새 신호 대기 |
| v2 | breakout_8 + reversion_12 | 9082.29 | -917.71 | sell / filled / 직전 완료 봉 목표 비중 0%; 다음 봉 시가 가정 |
| v2 | breakout_8 AND volume_26 | 9733.81 | -266.19 | sell / filled / 직전 완료 봉 목표 비중 0%; 다음 봉 시가 가정 |
| v2 | breakout_8 + volume_26 | 8990.64 | -1009.36 | 중단: 손실 한도 / sell / filled / 직전 완료 봉 목표 비중 0%; 다음 봉 시가 가정 |
| v2 | reversion_12 AND volume_26 | 9552.33 | -447.67 | sell / filled / 직전 완료 봉 목표 비중 0%; 다음 봉 시가 가정 |
| v2 | reversion_12 + volume_26 | 9046.60 | -953.40 | sell / filled / 직전 완료 봉 목표 비중 0%; 다음 봉 시가 가정 |
| v2 | ema_12_26 | 9736.67 | -263.33 | sell / filled / EMA12 > EMA26; 조건 미충족; EMA12=771.277, EMA26=771.539; 직전 완료 봉 목표를 다음 봉 시가에 모의 적용 |
| v2 | macd_12_26_9 | 9761.73 | -238.27 | sell / filled / MACD > 신호선 그리고 MACD > 0; 조건 미충족; MACD=1.03945, signal9=1.12358; 직전 완료 봉 목표를 다음 봉 시가에 모의 적용 |
| v2 | rsi_14_recovery | 9798.14 | -201.86 | sell / filled / 직전 RSI14 < 30, 현재 RSI14 >= 30 (한 봉 목표); 조건 미충족; RSI14=38.7389, previous_RSI14=37.2051; 직전 완료 봉 목표를 다음 봉 시가에 모의 적용 |
| v2 | bollinger_20_reentry | 9705.21 | -294.79 | sell / filled / 직전 종가 < 직전 하단밴드, 현재 하단밴드 <= 종가 <= SMA20 (한 봉 목표); 조건 미충족; close=762.88, lower20=759.962, SMA20=762.264, previous_lower20=759.738; 직전 완료 봉 목표를 다음 봉 시가에 모의 적용 |
| v2 | donchian_20 | 9808.27 | -191.73 | sell / filled / 종가 > 현재 봉을 제외한 직전 20봉 최고가; 조건 미충족; close=774.19, prior_high20=774.44; 직전 완료 봉 목표를 다음 봉 시가에 모의 적용 |
| v2 | atr_14_breakout | 9807.08 | -192.92 | sell / filled / 종가 > 직전 종가 + 직전 ATR14 그리고 종가 > EMA26; 조건 미충족; close=773.07, threshold=774.291, prior_ATR14=1.05565, EMA26=772.249; 직전 완료 봉 목표를 다음 봉 시가에 모의 적용 |
| v2 | session_vwap | 9367.80 | -632.20 | sell / filled / 종가 > 뉴욕 거래일별 누적 전형가격 VWAP; 조건 미충족; close=761.36, session_VWAP=761.482, session_volume=3.37356e+07; 직전 완료 봉 목표를 다음 봉 시가에 모의 적용 |
| v2 | obv_20 | 9584.50 | -415.50 | sell / filled / OBV > OBV의 SMA20 그리고 종가 > EMA26; 조건 미충족; OBV=-949325, OBV_SMA20=-1.03221e+07, close=766.62, EMA26=771.893; 직전 완료 봉 목표를 다음 봉 시가에 모의 적용 |
| v2 | stochastic_14_3_recovery | 9431.49 | -568.51 | sell / filled / 직전 %K14 < 20에서 %K14가 %D3 상향 돌파 (한 봉 목표); 조건 미충족; K14=78.2126, D3=50.4634, previous_K14=55.1135, previous_D3=31.7922; 직전 완료 봉 목표를 다음 봉 시가에 모의 적용 |
| v2 | mfi_14_recovery | 9800.44 | -199.56 | sell / filled / 직전 MFI14 < 20, 현재 MFI14 >= 20 (한 봉 목표); 조건 미충족; MFI14=24.2496, previous_MFI14=22.3876; 직전 완료 봉 목표를 다음 봉 시가에 모의 적용 |
| v2 | adx_14_trend | 9979.97 | -20.03 | sell / filled / Wilder ADX14 >= 25 그리고 +DI14 > -DI14; 조건 미충족; ADX14=24.2312, plus_DI14=28.3519, minus_DI14=24.6578; 직전 완료 봉 목표를 다음 봉 시가에 모의 적용 |
| v2 | aroon_25_trend | 9722.82 | -277.18 | sell / filled / Aroon25 Up > 70 그리고 Down < 30 (동률이면 최신 극값); 조건 미충족; Aroon_up=72, Aroon_down=100; 직전 완료 봉 목표를 다음 봉 시가에 모의 적용 |
| v2 | cci_20_momentum | 9754.52 | -245.48 | sell / filled / CCI20 > 100 (전형가격·평균절대편차); 조건 미충족; CCI20=97.3932; 직전 완료 봉 목표를 다음 봉 시가에 모의 적용 |
| v2 | williams_14_recovery | 9378.62 | -621.38 | sell / filled / 직전 Williams %R14 < -80, 현재 >= -80 (한 봉 목표); 조건 미충족; Williams_R14=-21.7874, previous_R14=-44.8865; 직전 완료 봉 목표를 다음 봉 시가에 모의 적용 |
| v2 | cmf_20_accumulation | 9632.96 | -367.04 | buy / partial / Chaikin Money Flow20 > 0.1; 조건 충족; CMF20=0.264253, volume20=5.65809e+07; 직전 완료 봉 목표를 다음 봉 시가에 모의 적용 |
| v2 | chaikin_3_10 | 9501.71 | -498.29 | sell / filled / ADL의 EMA3 - EMA10 > 0 그리고 종가 > EMA26; 조건 미충족; Chaikin3_10=2.35994e+06, ADL=6.37828e+07, close=762.39, EMA26=762.974; 직전 완료 봉 목표를 다음 봉 시가에 모의 적용 |
| v2 | roc_10_momentum | 9951.43 | -48.57 | sell / filled / 10봉 ROC > 1% 그리고 종가 > EMA26; 조건 미충족; ROC10_percent=0.806376, close=769.45, EMA26=767.181; 직전 완료 봉 목표를 다음 봉 시가에 모의 적용 |
| v2 | trix_15_trend | 9472.93 | -527.07 | sell / filled / 15봉 삼중 EMA의 1봉 변화율 TRIX > 0 그리고 종가 > EMA26; 조건 미충족; TRIX15_percent=0.0154379, close=766.62, EMA26=771.893; 직전 완료 봉 목표를 다음 봉 시가에 모의 적용 |
| v2 | keltner_20_breakout | 9803.05 | -196.95 | sell / filled / 종가 > EMA20 + 2 x Wilder ATR14; 조건 미충족; close=774.19, upper_Keltner=774.31, EMA20=772.615, ATR14=0.847257; 직전 완료 봉 목표를 다음 봉 시가에 모의 적용 |
| v2 | opening_range_30m | 9585.42 | -414.58 | sell / filled / 뉴욕 09:30·09:45 두 완료 봉 최고가를 10:00 이후 종가가 돌파; 조건 미충족; close=760.59, opening_high=761.2; 직전 완료 봉 목표를 다음 봉 시가에 모의 적용 |

### 같은 기간의 비용·노출 비교 (사후 연구)

| 전략 | 비용 전 | 비용 후 | 100% 보유 | 같은 평균 노출 보유 | 평균 노출 |
|---|---:|---:|---:|---:|---:|
| cash | 0.00% | 0.00% | -1.68% | -0.00% | 0.00% |
| buy_hold | -1.27% | -1.68% | -1.68% | -1.68% | 100.00% |
| trend_8_26 | -0.44% | -4.14% | -1.68% | -0.84% | 49.74% |
| momentum_26 | -1.13% | -5.19% | -1.68% | -0.82% | 48.43% |
| breakout_8 | -0.11% | -16.26% | -1.68% | -0.39% | 23.04% |
| reversion_12 | -1.03% | -12.38% | -1.68% | -0.48% | 28.80% |
| volume_26 | -1.21% | -12.17% | -1.68% | -0.18% | 10.47% |
| trend_8_26 AND momentum_26 | -0.33% | -4.43% | -1.68% | -0.71% | 42.41% |
| trend_8_26 + momentum_26 | -0.79% | -4.67% | -1.68% | -0.83% | 49.09% |
| trend_8_26 AND breakout_8 | 0.43% | -10.33% | -1.68% | -0.25% | 14.92% |
| trend_8_26 + breakout_8 | -0.27% | -10.03% | -1.68% | -0.61% | 36.39% |
| trend_8_26 AND reversion_12 | 0.20% | -4.32% | -1.68% | -0.11% | 6.28% |
| trend_8_26 + reversion_12 | -0.73% | -7.97% | -1.68% | -0.66% | 39.27% |
| trend_8_26 AND volume_26 | -1.05% | -6.30% | -1.68% | -0.09% | 5.50% |
| trend_8_26 + volume_26 | -0.82% | -8.25% | -1.68% | -0.51% | 30.11% |
| momentum_26 AND breakout_8 | 0.43% | -10.71% | -1.68% | -0.26% | 15.71% |
| momentum_26 + breakout_8 | -0.62% | -10.90% | -1.68% | -0.60% | 35.74% |
| momentum_26 AND reversion_12 | -0.39% | -4.89% | -1.68% | -0.10% | 6.02% |
| momentum_26 + reversion_12 | -1.08% | -8.10% | -1.68% | -0.65% | 38.62% |
| momentum_26 AND volume_26 | -0.79% | -5.27% | -1.68% | -0.07% | 3.93% |
| momentum_26 + volume_26 | -1.16% | -7.98% | -1.68% | -0.50% | 29.45% |
| breakout_8 AND reversion_12 | 0.00% | 0.00% | -1.68% | -0.00% | 0.00% |
| breakout_8 + reversion_12 | -0.57% | -13.64% | -1.68% | -0.44% | 25.93% |
| breakout_8 AND volume_26 | -0.26% | -3.15% | -1.68% | -0.04% | 2.36% |
| breakout_8 + volume_26 | -0.66% | -13.71% | -1.68% | -0.28% | 16.76% |
| reversion_12 AND volume_26 | -0.97% | -5.05% | -1.68% | -0.06% | 3.66% |
| reversion_12 + volume_26 | -1.12% | -11.17% | -1.68% | -0.33% | 19.64% |
| ema_12_26 | -1.31% | -4.57% | -1.68% | -0.86% | 51.31% |
| macd_12_26_9 | -0.36% | -4.86% | -1.68% | -0.53% | 31.68% |
| rsi_14_recovery | -0.42% | -3.71% | -1.68% | -0.04% | 2.09% |
| bollinger_20_reentry | -0.89% | -6.94% | -1.68% | -0.07% | 3.93% |
| donchian_20 | 0.22% | -7.85% | -1.68% | -0.12% | 7.33% |
| atr_14_breakout | 0.45% | -4.89% | -1.68% | -0.06% | 3.66% |
| session_vwap | -0.52% | -11.19% | -1.68% | -0.82% | 48.43% |
| obv_20 | -1.04% | -9.78% | -1.68% | -0.59% | 35.34% |
| stochastic_14_3_recovery | 0.64% | -14.20% | -1.68% | -0.17% | 9.95% |
| mfi_14_recovery | 0.11% | -2.79% | -1.68% | -0.03% | 1.83% |
| adx_14_trend | 1.03% | -0.65% | -1.68% | -0.37% | 21.99% |
| aroon_25_trend | 0.13% | -2.36% | -1.68% | -0.39% | 23.30% |
| cci_20_momentum | 0.36% | -7.34% | -1.68% | -0.36% | 21.47% |
| williams_14_recovery | 0.50% | -11.77% | -1.68% | -0.14% | 8.12% |
| cmf_20_accumulation | 0.58% | -4.36% | -1.68% | -0.83% | 49.48% |
| chaikin_3_10 | -0.01% | -7.29% | -1.68% | -0.65% | 38.48% |
| roc_10_momentum | -0.07% | -0.49% | -1.68% | -0.00% | 0.26% |
| trix_15_trend | -1.16% | -6.41% | -1.68% | -0.65% | 38.74% |
| keltner_20_breakout | 0.19% | -3.93% | -1.68% | -0.18% | 10.73% |
| opening_range_30m | -0.27% | -6.36% | -1.68% | -0.73% | 43.46% |

동일 구간·초기 자금, 종료 시 청산 비용 포함. 노출 맞춤은 사후 설명용이며 v2 실제 계좌 성과가 아닙니다.
[낙폭 분해·비용 영향·전체 구간](SPY/comparison.json)

[v1 전체 기록](SPY/accounts.json) · [v2 전체 기록](SPY/accounts-v2.json)

## QQQ 계좌

| 모델 | 전략 | 평가액 USD | 손익 USD | 최근 매매·이유 |
|---|---|---:|---:|---|
| v1 | cash | 10000.00 | 0.00 | 대기 /  / 새 신호 대기 |
| v1 | buy_hold | 9710.39 | -289.61 | buy /  / buy_hold: prior completed bar target 100%; next bar open simulation |
| v1 | trend_8_26 | 9644.88 | -355.12 | buy /  / trend_8_26: prior completed bar target 100%; next bar open simulation |
| v1 | momentum_26 | 9263.41 | -736.59 | buy /  / momentum_26: prior completed bar target 100%; next bar open simulation |
| v1 | breakout_8 | 9463.64 | -536.36 | sell /  / breakout_8: prior completed bar target 0%; next bar open simulation |
| v1 | reversion_12 | 9486.58 | -513.42 | sell /  / reversion_12: prior completed bar target 0%; next bar open simulation |
| v1 | volume_26 | 9446.81 | -553.19 | sell /  / volume_26: prior completed bar target 0%; next bar open simulation |
| v1 | trend_8_26 AND momentum_26 | 9621.16 | -378.84 | buy /  / trend_8_26 AND momentum_26: prior completed bar target 100%; next bar open simulation |
| v1 | trend_8_26 + momentum_26 | 9490.17 | -509.83 | buy /  / trend_8_26 + momentum_26: prior completed bar target 100%; next bar open simulation |
| v1 | trend_8_26 AND breakout_8 | 9893.81 | -106.19 | sell /  / trend_8_26 AND breakout_8: prior completed bar target 0%; next bar open simulation |
| v1 | trend_8_26 + breakout_8 | 9611.49 | -388.51 | buy /  / trend_8_26 + breakout_8: prior completed bar target 50%; next bar open simulation |
| v1 | trend_8_26 AND reversion_12 | 9856.40 | -143.60 | sell /  / trend_8_26 AND reversion_12: prior completed bar target 0%; next bar open simulation |
| v1 | trend_8_26 + reversion_12 | 9603.89 | -396.11 | sell /  / trend_8_26 + reversion_12: prior completed bar target 50%; next bar open simulation |
| v1 | trend_8_26 AND volume_26 | 9771.73 | -228.27 | sell /  / trend_8_26 AND volume_26: prior completed bar target 0%; next bar open simulation |
| v1 | trend_8_26 + volume_26 | 9545.42 | -454.58 | buy /  / trend_8_26 + volume_26: prior completed bar target 50%; next bar open simulation |
| v1 | momentum_26 AND breakout_8 | 9644.64 | -355.36 | sell /  / momentum_26 AND breakout_8: prior completed bar target 0%; next bar open simulation |
| v1 | momentum_26 + breakout_8 | 9381.97 | -618.03 | sell /  / momentum_26 + breakout_8: prior completed bar target 50%; next bar open simulation |
| v1 | momentum_26 AND reversion_12 | 9783.95 | -216.05 | sell /  / momentum_26 AND reversion_12: prior completed bar target 0%; next bar open simulation |
| v1 | momentum_26 + reversion_12 | 9449.84 | -550.16 | buy /  / momentum_26 + reversion_12: prior completed bar target 50%; next bar open simulation |
| v1 | momentum_26 AND volume_26 | 9789.69 | -210.31 | sell /  / momentum_26 AND volume_26: prior completed bar target 0%; next bar open simulation |
| v1 | momentum_26 + volume_26 | 9373.45 | -626.55 | sell /  / momentum_26 + volume_26: prior completed bar target 50%; next bar open simulation |
| v1 | breakout_8 AND reversion_12 | 10000.00 | 0.00 | 대기 /  / 새 신호 대기 |
| v1 | breakout_8 + reversion_12 | 9512.92 | -487.08 | sell /  / breakout_8 + reversion_12: prior completed bar target 0%; next bar open simulation |
| v1 | breakout_8 AND volume_26 | 9873.64 | -126.36 | sell /  / breakout_8 AND volume_26: prior completed bar target 0%; next bar open simulation |
| v1 | breakout_8 + volume_26 | 9531.07 | -468.93 | sell /  / breakout_8 + volume_26: prior completed bar target 0%; next bar open simulation |
| v1 | reversion_12 AND volume_26 | 9791.68 | -208.32 | sell /  / reversion_12 AND volume_26: prior completed bar target 0%; next bar open simulation |
| v1 | reversion_12 + volume_26 | 9504.44 | -495.56 | sell /  / reversion_12 + volume_26: prior completed bar target 0%; next bar open simulation |
| v1 | ema_12_26 | 9439.49 | -560.51 | sell /  / EMA12 > EMA26; 조건 미충족; EMA12=723.809, EMA26=723.847 |
| v1 | macd_12_26_9 | 9765.43 | -234.57 | sell /  / MACD > 신호선 그리고 MACD > 0; 조건 미충족; MACD=1.7811, signal9=1.82319 |
| v1 | rsi_14_recovery | 9689.26 | -310.74 | sell /  / 직전 RSI14 < 30, 현재 RSI14 >= 30 (한 봉 목표); 조건 미충족; RSI14=36.3006, previous_RSI14=36.7413 |
| v1 | bollinger_20_reentry | 9823.48 | -176.52 | sell /  / 직전 종가 < 직전 하단밴드, 현재 하단밴드 <= 종가 <= SMA20 (한 봉 목표); 조건 미충족; close=706.995, lower20=705.434, SMA20=720.761, previous_lower20=707.596 |
| v1 | donchian_20 | 9889.14 | -110.86 | sell /  / 종가 > 현재 봉을 제외한 직전 20봉 최고가; 조건 미충족; close=726.885, prior_high20=727.77 |
| v1 | atr_14_breakout | 9856.25 | -143.75 | sell /  / 종가 > 직전 종가 + 직전 ATR14 그리고 종가 > EMA26; 조건 미충족; close=708.502, threshold=710.044, prior_ATR14=2.19397, EMA26=707.552 |
| v1 | session_vwap | 9325.66 | -674.34 | sell /  / 종가 > 뉴욕 거래일별 누적 전형가격 VWAP; 조건 미충족; close=706.325, session_VWAP=707.155, session_volume=3.86762e+08 |
| v1 | obv_20 | 9398.26 | -601.74 | sell /  / OBV > OBV의 SMA20 그리고 종가 > EMA26; 조건 미충족; OBV=3.57362e+08, OBV_SMA20=4.32094e+08, close=707.37, EMA26=707.558 |
| v1 | stochastic_14_3_recovery | 9359.39 | -640.61 | sell /  / 직전 %K14 < 20에서 %K14가 %D3 상향 돌파 (한 봉 목표); 조건 미충족; K14=55.2721, D3=32.1738, previous_K14=36.3025, previous_D3=23.7941 |
| v1 | mfi_14_recovery | 9740.78 | -259.22 | sell /  / 직전 MFI14 < 20, 현재 MFI14 >= 20 (한 봉 목표); 조건 미충족; MFI14=27.2489, previous_MFI14=20.9918 |
| v1 | adx_14_trend | 9825.33 | -174.67 | sell /  / Wilder ADX14 >= 25 그리고 +DI14 > -DI14; 조건 미충족; ADX14=23.847, plus_DI14=27.825, minus_DI14=26.997 |
| v1 | aroon_25_trend | 9774.48 | -225.52 | sell /  / Aroon25 Up > 70 그리고 Down < 30 (동률이면 최신 극값); 조건 미충족; Aroon_up=68, Aroon_down=4 |
| v1 | cci_20_momentum | 9796.12 | -203.88 | sell /  / CCI20 > 100 (전형가격·평균절대편차); 조건 미충족; CCI20=61.134 |
| v1 | williams_14_recovery | 9486.47 | -513.53 | sell /  / 직전 Williams %R14 < -80, 현재 >= -80 (한 봉 목표); 조건 미충족; Williams_R14=-44.7279, previous_R14=-63.6975 |
| v1 | cmf_20_accumulation | 9319.81 | -680.19 | sell /  / Chaikin Money Flow20 > 0.1; 조건 미충족; CMF20=-0.0457086, volume20=4.3889e+08 |
| v1 | chaikin_3_10 | 9412.83 | -587.17 | sell /  / ADL의 EMA3 - EMA10 > 0 그리고 종가 > EMA26; 조건 미충족; Chaikin3_10=-1.63534e+07, ADL=3.82635e+08, close=707.37, EMA26=707.558 |
| v1 | roc_10_momentum | 9961.33 | -38.67 | sell /  / 10봉 ROC > 1% 그리고 종가 > EMA26; 조건 미충족; ROC10_percent=0.681109, close=725.78, EMA26=721.667 |
| v1 | trix_15_trend | 9467.11 | -532.89 | sell /  / 15봉 삼중 EMA의 1봉 변화율 TRIX > 0 그리고 종가 > EMA26; 조건 미충족; TRIX15_percent=0.0245938, close=713.775, EMA26=723.847 |
| v1 | keltner_20_breakout | 9782.40 | -217.60 | sell /  / 종가 > EMA20 + 2 x Wilder ATR14; 조건 미충족; close=726.815, upper_Keltner=727.39, EMA20=724.295, ATR14=1.54727 |
| v1 | opening_range_30m | 9498.71 | -501.29 | buy /  / 뉴욕 09:30·09:45 두 완료 봉 최고가를 10:00 이후 종가가 돌파; 조건 충족; close=706.42, opening_high=705.64 |
| v2 | cash | 10000.00 | 0.00 | 대기 /  / 새 신호 대기 |
| v2 | buy_hold | 9396.51 | -603.49 | 중단: 손실 한도 / buy / partial / 직전 완료 봉 목표 비중 100%; 다음 봉 시가 가정 |
| v2 | trend_8_26 | 9447.04 | -552.96 | buy / partial / 직전 완료 봉 목표 비중 100%; 다음 봉 시가 가정 |
| v2 | momentum_26 | 9151.31 | -848.69 | buy / partial / 직전 완료 봉 목표 비중 100%; 다음 봉 시가 가정 |
| v2 | breakout_8 | 9129.27 | -870.73 | sell / filled / 직전 완료 봉 목표 비중 0%; 다음 봉 시가 가정 |
| v2 | reversion_12 | 9000.22 | -999.78 | sell / filled / 직전 완료 봉 목표 비중 0%; 다음 봉 시가 가정 |
| v2 | volume_26 | 9565.80 | -434.20 | 중단: 손실 한도 / sell / filled / 직전 완료 봉 목표 비중 0%; 다음 봉 시가 가정 |
| v2 | trend_8_26 AND momentum_26 | 9512.33 | -487.67 | buy / partial / 직전 완료 봉 목표 비중 100%; 다음 봉 시가 가정 |
| v2 | trend_8_26 + momentum_26 | 9337.23 | -662.77 | buy / partial / 직전 완료 봉 목표 비중 100%; 다음 봉 시가 가정 |
| v2 | trend_8_26 AND breakout_8 | 9782.92 | -217.08 | sell / filled / 직전 완료 봉 목표 비중 0%; 다음 봉 시가 가정 |
| v2 | trend_8_26 + breakout_8 | 9345.59 | -654.41 | buy / filled / 직전 완료 봉 목표 비중 50%; 다음 봉 시가 가정 |
| v2 | trend_8_26 AND reversion_12 | 9711.76 | -288.24 | sell / filled / 직전 완료 봉 목표 비중 0%; 다음 봉 시가 가정 |
| v2 | trend_8_26 + reversion_12 | 9259.55 | -740.45 | sell / filled / 직전 완료 봉 목표 비중 50%; 다음 봉 시가 가정 |
| v2 | trend_8_26 AND volume_26 | 9602.02 | -397.98 | sell / filled / 직전 완료 봉 목표 비중 0%; 다음 봉 시가 가정 |
| v2 | trend_8_26 + volume_26 | 9148.70 | -851.30 | buy / filled / 직전 완료 봉 목표 비중 50%; 다음 봉 시가 가정 |
| v2 | momentum_26 AND breakout_8 | 9591.37 | -408.63 | sell / filled / 직전 완료 봉 목표 비중 0%; 다음 봉 시가 가정 |
| v2 | momentum_26 + breakout_8 | 9159.67 | -840.33 | sell / filled / 직전 완료 봉 목표 비중 50%; 다음 봉 시가 가정 |
| v2 | momentum_26 AND reversion_12 | 9776.12 | -223.88 | sell / filled / 직전 완료 봉 목표 비중 0%; 다음 봉 시가 가정 |
| v2 | momentum_26 + reversion_12 | 9171.10 | -828.90 | buy / filled / 직전 완료 봉 목표 비중 50%; 다음 봉 시가 가정 |
| v2 | momentum_26 AND volume_26 | 9718.13 | -281.87 | sell / filled / 직전 완료 봉 목표 비중 0%; 다음 봉 시가 가정 |
| v2 | momentum_26 + volume_26 | 9023.25 | -976.75 | sell / filled / 직전 완료 봉 목표 비중 50%; 다음 봉 시가 가정 |
| v2 | breakout_8 AND reversion_12 | 10000.00 | 0.00 | 대기 /  / 새 신호 대기 |
| v2 | breakout_8 + reversion_12 | 9159.71 | -840.29 | sell / filled / 직전 완료 봉 목표 비중 0%; 다음 봉 시가 가정 |
| v2 | breakout_8 AND volume_26 | 9814.43 | -185.57 | sell / filled / 직전 완료 봉 목표 비중 0%; 다음 봉 시가 가정 |
| v2 | breakout_8 + volume_26 | 9107.44 | -892.56 | sell / filled / 직전 완료 봉 목표 비중 0%; 다음 봉 시가 가정 |
| v2 | reversion_12 AND volume_26 | 9547.64 | -452.36 | 중단: 손실 한도 / sell / filled / 직전 완료 봉 목표 비중 0%; 다음 봉 시가 가정 |
| v2 | reversion_12 + volume_26 | 8991.91 | -1008.09 | 중단: 손실 한도 / buy / filled / 직전 완료 봉 목표 비중 50%; 다음 봉 시가 가정 |
| v2 | ema_12_26 | 9430.06 | -569.94 | sell / filled / EMA12 > EMA26; 조건 미충족; EMA12=723.809, EMA26=723.847; 직전 완료 봉 목표를 다음 봉 시가에 모의 적용 |
| v2 | macd_12_26_9 | 9755.67 | -244.33 | sell / filled / MACD > 신호선 그리고 MACD > 0; 조건 미충족; MACD=1.7811, signal9=1.82319; 직전 완료 봉 목표를 다음 봉 시가에 모의 적용 |
| v2 | rsi_14_recovery | 9675.71 | -324.29 | sell / filled / 직전 RSI14 < 30, 현재 RSI14 >= 30 (한 봉 목표); 조건 미충족; RSI14=36.3006, previous_RSI14=36.7413; 직전 완료 봉 목표를 다음 봉 시가에 모의 적용 |
| v2 | bollinger_20_reentry | 9815.62 | -184.38 | sell / filled / 직전 종가 < 직전 하단밴드, 현재 하단밴드 <= 종가 <= SMA20 (한 봉 목표); 조건 미충족; close=706.995, lower20=705.434, SMA20=720.761, previous_lower20=707.596; 직전 완료 봉 목표를 다음 봉 시가에 모의 적용 |
| v2 | donchian_20 | 9881.23 | -118.77 | sell / filled / 종가 > 현재 봉을 제외한 직전 20봉 최고가; 조건 미충족; close=726.885, prior_high20=727.77; 직전 완료 봉 목표를 다음 봉 시가에 모의 적용 |
| v2 | atr_14_breakout | 9846.40 | -153.60 | sell / filled / 종가 > 직전 종가 + 직전 ATR14 그리고 종가 > EMA26; 조건 미충족; close=708.502, threshold=710.044, prior_ATR14=2.19397, EMA26=707.552; 직전 완료 봉 목표를 다음 봉 시가에 모의 적용 |
| v2 | session_vwap | 9303.31 | -696.69 | sell / filled / 종가 > 뉴욕 거래일별 누적 전형가격 VWAP; 조건 미충족; close=706.325, session_VWAP=707.155, session_volume=3.86762e+08; 직전 완료 봉 목표를 다음 봉 시가에 모의 적용 |
| v2 | obv_20 | 9381.36 | -618.64 | sell / filled / OBV > OBV의 SMA20 그리고 종가 > EMA26; 조건 미충족; OBV=3.57362e+08, OBV_SMA20=4.32094e+08, close=707.37, EMA26=707.558; 직전 완료 봉 목표를 다음 봉 시가에 모의 적용 |
| v2 | stochastic_14_3_recovery | 9694.13 | -305.87 | 중단: 손실 한도 / sell / filled / 직전 %K14 < 20에서 %K14가 %D3 상향 돌파 (한 봉 목표); 조건 미충족; K14=10.576, D3=8.00581, previous_K14=7.39787, previous_D3=7.27486; 직전 완료 봉 목표를 다음 봉 시가에 모의 적용 |
| v2 | mfi_14_recovery | 9732.99 | -267.01 | sell / filled / 직전 MFI14 < 20, 현재 MFI14 >= 20 (한 봉 목표); 조건 미충족; MFI14=27.2489, previous_MFI14=20.9918; 직전 완료 봉 목표를 다음 봉 시가에 모의 적용 |
| v2 | adx_14_trend | 9817.47 | -182.53 | sell / filled / Wilder ADX14 >= 25 그리고 +DI14 > -DI14; 조건 미충족; ADX14=23.847, plus_DI14=27.825, minus_DI14=26.997; 직전 완료 봉 목표를 다음 봉 시가에 모의 적용 |
| v2 | aroon_25_trend | 9766.66 | -233.34 | sell / filled / Aroon25 Up > 70 그리고 Down < 30 (동률이면 최신 극값); 조건 미충족; Aroon_up=68, Aroon_down=4; 직전 완료 봉 목표를 다음 봉 시가에 모의 적용 |
| v2 | cci_20_momentum | 9784.37 | -215.63 | sell / filled / CCI20 > 100 (전형가격·평균절대편차); 조건 미충족; CCI20=61.134; 직전 완료 봉 목표를 다음 봉 시가에 모의 적용 |
| v2 | williams_14_recovery | 9459.95 | -540.05 | sell / filled / 직전 Williams %R14 < -80, 현재 >= -80 (한 봉 목표); 조건 미충족; Williams_R14=-44.7279, previous_R14=-63.6975; 직전 완료 봉 목표를 다음 봉 시가에 모의 적용 |
| v2 | cmf_20_accumulation | 9301.19 | -698.81 | sell / filled / Chaikin Money Flow20 > 0.1; 조건 미충족; CMF20=-0.0457086, volume20=4.3889e+08; 직전 완료 봉 목표를 다음 봉 시가에 모의 적용 |
| v2 | chaikin_3_10 | 9395.90 | -604.10 | sell / filled / ADL의 EMA3 - EMA10 > 0 그리고 종가 > EMA26; 조건 미충족; Chaikin3_10=-1.63534e+07, ADL=3.82635e+08, close=707.37, EMA26=707.558; 직전 완료 봉 목표를 다음 봉 시가에 모의 적용 |
| v2 | roc_10_momentum | 9957.34 | -42.66 | sell / filled / 10봉 ROC > 1% 그리고 종가 > EMA26; 조건 미충족; ROC10_percent=0.681109, close=725.78, EMA26=721.667; 직전 완료 봉 목표를 다음 봉 시가에 모의 적용 |
| v2 | trix_15_trend | 9453.87 | -546.13 | sell / filled / 15봉 삼중 EMA의 1봉 변화율 TRIX > 0 그리고 종가 > EMA26; 조건 미충족; TRIX15_percent=0.0245938, close=713.775, EMA26=723.847; 직전 완료 봉 목표를 다음 봉 시가에 모의 적용 |
| v2 | keltner_20_breakout | 9772.62 | -227.38 | sell / filled / 종가 > EMA20 + 2 x Wilder ATR14; 조건 미충족; close=726.815, upper_Keltner=727.39, EMA20=724.295, ATR14=1.54727; 직전 완료 봉 목표를 다음 봉 시가에 모의 적용 |
| v2 | opening_range_30m | 9486.37 | -513.63 | buy / partial / 뉴욕 09:30·09:45 두 완료 봉 최고가를 10:00 이후 종가가 돌파; 조건 충족; close=706.42, opening_high=705.64; 직전 완료 봉 목표를 다음 봉 시가에 모의 적용 |

### 같은 기간의 비용·노출 비교 (사후 연구)

| 전략 | 비용 전 | 비용 후 | 100% 보유 | 같은 평균 노출 보유 | 평균 노출 |
|---|---:|---:|---:|---:|---:|
| cash | 0.00% | 0.00% | -6.49% | -0.00% | 0.00% |
| buy_hold | -6.09% | -6.49% | -6.49% | -6.49% | 100.00% |
| trend_8_26 | -2.37% | -5.99% | -6.49% | -2.64% | 40.05% |
| momentum_26 | -4.39% | -10.23% | -6.49% | -2.18% | 32.98% |
| breakout_8 | -2.12% | -16.91% | -6.49% | -1.21% | 18.32% |
| reversion_12 | -0.44% | -12.96% | -6.49% | -2.18% | 32.98% |
| volume_26 | -0.60% | -15.62% | -6.49% | -1.23% | 18.59% |
| trend_8_26 AND momentum_26 | -1.22% | -5.28% | -6.49% | -1.85% | 28.01% |
| trend_8_26 + momentum_26 | -3.38% | -7.55% | -6.49% | -2.41% | 36.52% |
| trend_8_26 AND breakout_8 | 0.08% | -7.98% | -6.49% | -0.73% | 10.99% |
| trend_8_26 + breakout_8 | -2.24% | -10.87% | -6.49% | -1.93% | 29.19% |
| trend_8_26 AND reversion_12 | -0.24% | -3.94% | -6.49% | -0.42% | 6.28% |
| trend_8_26 + reversion_12 | -1.39% | -8.97% | -6.49% | -2.41% | 36.52% |
| trend_8_26 AND volume_26 | 0.17% | -5.15% | -6.49% | -0.40% | 6.02% |
| trend_8_26 + volume_26 | -1.48% | -10.94% | -6.49% | -1.94% | 29.33% |
| momentum_26 AND breakout_8 | -0.42% | -8.06% | -6.49% | -0.68% | 10.21% |
| momentum_26 + breakout_8 | -3.26% | -13.27% | -6.49% | -1.70% | 25.66% |
| momentum_26 AND reversion_12 | -1.16% | -4.83% | -6.49% | -0.37% | 5.50% |
| momentum_26 + reversion_12 | -2.42% | -10.48% | -6.49% | -2.18% | 32.99% |
| momentum_26 AND volume_26 | -0.37% | -4.07% | -6.49% | -0.24% | 3.66% |
| momentum_26 + volume_26 | -2.50% | -12.60% | -6.49% | -1.70% | 25.79% |
| breakout_8 AND reversion_12 | 0.00% | 0.00% | -6.49% | -0.00% | 0.00% |
| breakout_8 + reversion_12 | -1.27% | -13.89% | -6.49% | -1.70% | 25.66% |
| breakout_8 AND volume_26 | 0.15% | -2.75% | -6.49% | -0.17% | 2.62% |
| breakout_8 + volume_26 | -1.36% | -14.50% | -6.49% | -1.22% | 18.46% |
| reversion_12 AND volume_26 | -1.12% | -8.70% | -6.49% | -0.59% | 8.90% |
| reversion_12 + volume_26 | -0.51% | -13.76% | -6.49% | -1.71% | 25.79% |
| ema_12_26 | -3.89% | -6.68% | -6.49% | -2.13% | 32.20% |
| macd_12_26_9 | -0.46% | -4.55% | -6.49% | -1.35% | 20.42% |
| rsi_14_recovery | -0.50% | -6.97% | -6.49% | -0.28% | 4.19% |
| bollinger_20_reentry | -0.05% | -5.76% | -6.49% | -0.24% | 3.66% |
| donchian_20 | 0.55% | -4.39% | -6.49% | -0.35% | 5.24% |
| atr_14_breakout | 0.52% | -3.21% | -6.49% | -0.17% | 2.62% |
| session_vwap | -3.12% | -14.59% | -6.49% | -3.10% | 47.12% |
| obv_20 | -4.30% | -13.11% | -6.49% | -1.39% | 20.94% |
| stochastic_14_3_recovery | 0.14% | -12.82% | -6.49% | -0.57% | 8.64% |
| mfi_14_recovery | -1.13% | -3.99% | -6.49% | -0.12% | 1.83% |
| adx_14_trend | 0.42% | -2.08% | -6.49% | -1.27% | 19.11% |
| aroon_25_trend | 0.17% | -2.73% | -6.49% | -0.95% | 14.40% |
| cci_20_momentum | 0.45% | -4.48% | -6.49% | -1.18% | 17.80% |
| williams_14_recovery | -0.17% | -11.61% | -6.49% | -0.50% | 7.59% |
| cmf_20_accumulation | -3.10% | -10.53% | -6.49% | -2.16% | 32.72% |
| chaikin_3_10 | -5.41% | -13.76% | -6.49% | -1.70% | 25.65% |
| roc_10_momentum | 0.41% | -0.43% | -6.49% | -0.19% | 2.88% |
| trix_15_trend | -2.78% | -6.38% | -6.49% | -1.75% | 26.44% |
| keltner_20_breakout | -0.36% | -4.46% | -6.49% | -0.45% | 6.81% |
| opening_range_30m | -2.00% | -7.60% | -6.49% | -2.43% | 36.91% |

동일 구간·초기 자금, 종료 시 청산 비용 포함. 노출 맞춤은 사후 설명용이며 v2 실제 계좌 성과가 아닙니다.
[낙폭 분해·비용 영향·전체 구간](QQQ/comparison.json)

[v1 전체 기록](QQQ/accounts.json) · [v2 전체 기록](QQQ/accounts-v2.json)

## IWM 계좌

| 모델 | 전략 | 평가액 USD | 손익 USD | 최근 매매·이유 |
|---|---|---:|---:|---|
| v1 | cash | 10000.00 | 0.00 | 대기 /  / 새 신호 대기 |
| v1 | buy_hold | 9992.35 | -7.65 | buy /  / buy_hold: prior completed bar target 100%; next bar open simulation |
| v1 | trend_8_26 | 9665.43 | -334.57 | buy /  / trend_8_26: prior completed bar target 100%; next bar open simulation |
| v1 | momentum_26 | 9627.43 | -372.57 | buy /  / momentum_26: prior completed bar target 100%; next bar open simulation |
| v1 | breakout_8 | 9221.05 | -778.95 | sell /  / breakout_8: prior completed bar target 0%; next bar open simulation |
| v1 | reversion_12 | 9713.04 | -286.96 | sell /  / reversion_12: prior completed bar target 0%; next bar open simulation |
| v1 | volume_26 | 9851.14 | -148.86 | sell /  / volume_26: prior completed bar target 0%; next bar open simulation |
| v1 | trend_8_26 AND momentum_26 | 9628.58 | -371.42 | buy /  / trend_8_26 AND momentum_26: prior completed bar target 100%; next bar open simulation |
| v1 | trend_8_26 + momentum_26 | 9665.84 | -334.16 | buy /  / trend_8_26 + momentum_26: prior completed bar target 100%; next bar open simulation |
| v1 | trend_8_26 AND breakout_8 | 9404.46 | -595.54 | sell /  / trend_8_26 AND breakout_8: prior completed bar target 0%; next bar open simulation |
| v1 | trend_8_26 + breakout_8 | 9440.82 | -559.18 | buy /  / trend_8_26 + breakout_8: prior completed bar target 50%; next bar open simulation |
| v1 | trend_8_26 AND reversion_12 | 9755.06 | -244.94 | sell /  / trend_8_26 AND reversion_12: prior completed bar target 0%; next bar open simulation |
| v1 | trend_8_26 + reversion_12 | 9688.96 | -311.04 | buy /  / trend_8_26 + reversion_12: prior completed bar target 50%; next bar open simulation |
| v1 | trend_8_26 AND volume_26 | 9893.73 | -106.27 | sell /  / trend_8_26 AND volume_26: prior completed bar target 0%; next bar open simulation |
| v1 | trend_8_26 + volume_26 | 9777.20 | -222.80 | buy /  / trend_8_26 + volume_26: prior completed bar target 50%; next bar open simulation |
| v1 | momentum_26 AND breakout_8 | 9478.36 | -521.64 | sell /  / momentum_26 AND breakout_8: prior completed bar target 0%; next bar open simulation |
| v1 | momentum_26 + breakout_8 | 9459.92 | -540.08 | buy /  / momentum_26 + breakout_8: prior completed bar target 50%; next bar open simulation |
| v1 | momentum_26 AND reversion_12 | 9876.67 | -123.33 | sell /  / momentum_26 AND reversion_12: prior completed bar target 0%; next bar open simulation |
| v1 | momentum_26 + reversion_12 | 9767.07 | -232.93 | buy /  / momentum_26 + reversion_12: prior completed bar target 50%; next bar open simulation |
| v1 | momentum_26 AND volume_26 | 9928.27 | -71.73 | sell /  / momentum_26 AND volume_26: prior completed bar target 0%; next bar open simulation |
| v1 | momentum_26 + volume_26 | 9777.54 | -222.46 | buy /  / momentum_26 + volume_26: prior completed bar target 50%; next bar open simulation |
| v1 | breakout_8 AND reversion_12 | 10000.00 | 0.00 | 대기 /  / 새 신호 대기 |
| v1 | breakout_8 + reversion_12 | 9501.52 | -498.48 | sell /  / breakout_8 + reversion_12: prior completed bar target 0%; next bar open simulation |
| v1 | breakout_8 AND volume_26 | 9918.46 | -81.54 | sell /  / breakout_8 AND volume_26: prior completed bar target 0%; next bar open simulation |
| v1 | breakout_8 + volume_26 | 9549.89 | -450.11 | sell /  / breakout_8 + volume_26: prior completed bar target 0%; next bar open simulation |
| v1 | reversion_12 AND volume_26 | 9912.42 | -87.58 | sell /  / reversion_12 AND volume_26: prior completed bar target 0%; next bar open simulation |
| v1 | reversion_12 + volume_26 | 9821.00 | -179.00 | sell /  / reversion_12 + volume_26: prior completed bar target 0%; next bar open simulation |
| v1 | ema_12_26 | 9706.47 | -293.53 | sell /  / EMA12 > EMA26; 조건 미충족; EMA12=275.679, EMA26=275.693 |
| v1 | macd_12_26_9 | 9796.67 | -203.33 | sell /  / MACD > 신호선 그리고 MACD > 0; 조건 미충족; MACD=-0.0140484, signal9=-0.0720113 |
| v1 | rsi_14_recovery | 9786.95 | -213.05 | sell /  / 직전 RSI14 < 30, 현재 RSI14 >= 30 (한 봉 목표); 조건 미충족; RSI14=46.986, previous_RSI14=37.1649 |
| v1 | bollinger_20_reentry | 9762.11 | -237.89 | sell /  / 직전 종가 < 직전 하단밴드, 현재 하단밴드 <= 종가 <= SMA20 (한 봉 목표); 조건 미충족; close=275.725, lower20=274.173, SMA20=275.605, previous_lower20=274.15 |
| v1 | donchian_20 | 9835.91 | -164.09 | sell /  / 종가 > 현재 봉을 제외한 직전 20봉 최고가; 조건 미충족; close=275.785, prior_high20=276.875 |
| v1 | atr_14_breakout | 9685.22 | -314.78 | sell /  / 종가 > 직전 종가 + 직전 ATR14 그리고 종가 > EMA26; 조건 미충족; close=274.63, threshold=277.369, prior_ATR14=0.659199, EMA26=275.963 |
| v1 | session_vwap | 9251.34 | -748.66 | buy /  / 종가 > 뉴욕 거래일별 누적 전형가격 VWAP; 조건 충족; close=275.03, session_VWAP=274.45, session_volume=6.20261e+06 |
| v1 | obv_20 | 9624.91 | -375.09 | sell /  / OBV > OBV의 SMA20 그리고 종가 > EMA26; 조건 미충족; OBV=-2.65101e+07, OBV_SMA20=-2.63464e+07, close=274.63, EMA26=275.963 |
| v1 | stochastic_14_3_recovery | 9613.95 | -386.05 | sell /  / 직전 %K14 < 20에서 %K14가 %D3 상향 돌파 (한 봉 목표); 조건 미충족; K14=68.0001, D3=43.5239, previous_K14=48.1428, previous_D3=23.7507 |
| v1 | mfi_14_recovery | 9934.22 | -65.78 | sell /  / 직전 MFI14 < 20, 현재 MFI14 >= 20 (한 봉 목표); 조건 미충족; MFI14=34.131, previous_MFI14=22.0435 |
| v1 | adx_14_trend | 9726.05 | -273.95 | sell /  / Wilder ADX14 >= 25 그리고 +DI14 > -DI14; 조건 미충족; ADX14=27.8461, plus_DI14=25.882, minus_DI14=28.4558 |
| v1 | aroon_25_trend | 9745.85 | -254.15 | sell /  / Aroon25 Up > 70 그리고 Down < 30 (동률이면 최신 극값); 조건 미충족; Aroon_up=68, Aroon_down=4 |
| v1 | cci_20_momentum | 9722.50 | -277.50 | sell /  / CCI20 > 100 (전형가격·평균절대편차); 조건 미충족; CCI20=-314.625 |
| v1 | williams_14_recovery | 9742.36 | -257.64 | sell /  / 직전 Williams %R14 < -80, 현재 >= -80 (한 봉 목표); 조건 미충족; Williams_R14=-31.9999, previous_R14=-51.8572 |
| v1 | cmf_20_accumulation | 9669.39 | -330.61 | buy /  / Chaikin Money Flow20 > 0.1; 조건 충족; CMF20=0.23674, volume20=1.30084e+07 |
| v1 | chaikin_3_10 | 9367.06 | -632.94 | buy /  / ADL의 EMA3 - EMA10 > 0 그리고 종가 > EMA26; 조건 충족; Chaikin3_10=2029.77, ADL=-2.70969e+07, close=275.78, EMA26=275.675 |
| v1 | roc_10_momentum | 9996.39 | -3.61 | sell /  / 10봉 ROC > 1% 그리고 종가 > EMA26; 조건 미충족; ROC10_percent=0.995963, close=275.315, EMA26=273.754 |
| v1 | trix_15_trend | 9811.92 | -188.08 | sell /  / 15봉 삼중 EMA의 1봉 변화율 TRIX > 0 그리고 종가 > EMA26; 조건 미충족; TRIX15_percent=0.00744142, close=276.06, EMA26=276.447 |
| v1 | keltner_20_breakout | 9879.23 | -120.77 | sell /  / 종가 > EMA20 + 2 x Wilder ATR14; 조건 미충족; close=276.4, upper_Keltner=277.094, EMA20=275.768, ATR14=0.662947 |
| v1 | opening_range_30m | 9948.67 | -51.33 | buy /  / 뉴욕 09:30·09:45 두 완료 봉 최고가를 10:00 이후 종가가 돌파; 조건 충족; close=275.725, opening_high=275.24 |
| v2 | cash | 10000.00 | 0.00 | 대기 /  / 새 신호 대기 |
| v2 | buy_hold | 9885.50 | -114.50 | buy / partial / 직전 완료 봉 목표 비중 100%; 다음 봉 시가 가정 |
| v2 | trend_8_26 | 9532.56 | -467.44 | buy / partial / 직전 완료 봉 목표 비중 100%; 다음 봉 시가 가정 |
| v2 | momentum_26 | 9486.56 | -513.44 | buy / partial / 직전 완료 봉 목표 비중 100%; 다음 봉 시가 가정 |
| v2 | breakout_8 | 8996.07 | -1003.93 | 중단: 손실 한도 / buy / partial / 직전 완료 봉 목표 비중 100%; 다음 봉 시가 가정 |
| v2 | reversion_12 | 9246.43 | -753.57 | sell / filled / 직전 완료 봉 목표 비중 0%; 다음 봉 시가 가정 |
| v2 | volume_26 | 9360.51 | -639.49 | sell / filled / 직전 완료 봉 목표 비중 0%; 다음 봉 시가 가정 |
| v2 | trend_8_26 AND momentum_26 | 9637.83 | -362.17 | buy / partial / 직전 완료 봉 목표 비중 100%; 다음 봉 시가 가정 |
| v2 | trend_8_26 + momentum_26 | 9549.79 | -450.21 | buy / partial / 직전 완료 봉 목표 비중 100%; 다음 봉 시가 가정 |
| v2 | trend_8_26 AND breakout_8 | 9300.05 | -699.95 | sell / filled / 직전 완료 봉 목표 비중 0%; 다음 봉 시가 가정 |
| v2 | trend_8_26 + breakout_8 | 9198.56 | -801.44 | buy / filled / 직전 완료 봉 목표 비중 50%; 다음 봉 시가 가정 |
| v2 | trend_8_26 AND reversion_12 | 9630.14 | -369.86 | sell / filled / 직전 완료 봉 목표 비중 0%; 다음 봉 시가 가정 |
| v2 | trend_8_26 + reversion_12 | 9387.98 | -612.02 | buy / filled / 직전 완료 봉 목표 비중 50%; 다음 봉 시가 가정 |
| v2 | trend_8_26 AND volume_26 | 9752.17 | -247.83 | sell / filled / 직전 완료 봉 목표 비중 0%; 다음 봉 시가 가정 |
| v2 | trend_8_26 + volume_26 | 9485.68 | -514.32 | buy / filled / 직전 완료 봉 목표 비중 50%; 다음 봉 시가 가정 |
| v2 | momentum_26 AND breakout_8 | 9271.16 | -728.84 | sell / filled / 직전 완료 봉 목표 비중 0%; 다음 봉 시가 가정 |
| v2 | momentum_26 + breakout_8 | 9195.43 | -804.57 | buy / filled / 직전 완료 봉 목표 비중 50%; 다음 봉 시가 가정 |
| v2 | momentum_26 AND reversion_12 | 9831.84 | -168.16 | sell / filled / 직전 완료 봉 목표 비중 0%; 다음 봉 시가 가정 |
| v2 | momentum_26 + reversion_12 | 9483.83 | -516.17 | buy / filled / 직전 완료 봉 목표 비중 50%; 다음 봉 시가 가정 |
| v2 | momentum_26 AND volume_26 | 9818.94 | -181.06 | sell / filled / 직전 완료 봉 목표 비중 0%; 다음 봉 시가 가정 |
| v2 | momentum_26 + volume_26 | 9462.63 | -537.37 | buy / filled / 직전 완료 봉 목표 비중 50%; 다음 봉 시가 가정 |
| v2 | breakout_8 AND reversion_12 | 10000.00 | 0.00 | 대기 /  / 새 신호 대기 |
| v2 | breakout_8 + reversion_12 | 9115.73 | -884.27 | sell / filled / 직전 완료 봉 목표 비중 0%; 다음 봉 시가 가정 |
| v2 | breakout_8 AND volume_26 | 9660.76 | -339.24 | sell / filled / 직전 완료 봉 목표 비중 0%; 다음 봉 시가 가정 |
| v2 | breakout_8 + volume_26 | 9133.86 | -866.14 | sell / filled / 직전 완료 봉 목표 비중 0%; 다음 봉 시가 가정 |
| v2 | reversion_12 AND volume_26 | 9647.72 | -352.28 | sell / filled / 직전 완료 봉 목표 비중 0%; 다음 봉 시가 가정 |
| v2 | reversion_12 + volume_26 | 9361.82 | -638.18 | sell / filled / 직전 완료 봉 목표 비중 0%; 다음 봉 시가 가정 |
| v2 | ema_12_26 | 9696.77 | -303.23 | sell / filled / EMA12 > EMA26; 조건 미충족; EMA12=275.679, EMA26=275.693; 직전 완료 봉 목표를 다음 봉 시가에 모의 적용 |
| v2 | macd_12_26_9 | 9786.88 | -213.12 | sell / filled / MACD > 신호선 그리고 MACD > 0; 조건 미충족; MACD=-0.0140484, signal9=-0.0720113; 직전 완료 봉 목표를 다음 봉 시가에 모의 적용 |
| v2 | rsi_14_recovery | 9779.12 | -220.88 | sell / filled / 직전 RSI14 < 30, 현재 RSI14 >= 30 (한 봉 목표); 조건 미충족; RSI14=46.986, previous_RSI14=37.1649; 직전 완료 봉 목표를 다음 봉 시가에 모의 적용 |
| v2 | bollinger_20_reentry | 9750.40 | -249.60 | sell / filled / 직전 종가 < 직전 하단밴드, 현재 하단밴드 <= 종가 <= SMA20 (한 봉 목표); 조건 미충족; close=275.725, lower20=274.173, SMA20=275.605, previous_lower20=274.15; 직전 완료 봉 목표를 다음 봉 시가에 모의 적용 |
| v2 | donchian_20 | 9830.01 | -169.99 | sell / filled / 종가 > 현재 봉을 제외한 직전 20봉 최고가; 조건 미충족; close=275.785, prior_high20=276.875; 직전 완료 봉 목표를 다음 봉 시가에 모의 적용 |
| v2 | atr_14_breakout | 9669.74 | -330.26 | sell / filled / 종가 > 직전 종가 + 직전 ATR14 그리고 종가 > EMA26; 조건 미충족; close=274.63, threshold=277.369, prior_ATR14=0.659199, EMA26=275.963; 직전 완료 봉 목표를 다음 봉 시가에 모의 적용 |
| v2 | session_vwap | 9219.02 | -780.98 | buy / partial / 종가 > 뉴욕 거래일별 누적 전형가격 VWAP; 조건 충족; close=275.03, session_VWAP=274.45, session_volume=6.20261e+06; 직전 완료 봉 목표를 다음 봉 시가에 모의 적용 |
| v2 | obv_20 | 9607.61 | -392.39 | sell / filled / OBV > OBV의 SMA20 그리고 종가 > EMA26; 조건 미충족; OBV=-2.65101e+07, OBV_SMA20=-2.63464e+07, close=274.63, EMA26=275.963; 직전 완료 봉 목표를 다음 봉 시가에 모의 적용 |
| v2 | stochastic_14_3_recovery | 9594.74 | -405.26 | sell / filled / 직전 %K14 < 20에서 %K14가 %D3 상향 돌파 (한 봉 목표); 조건 미충족; K14=68.0001, D3=43.5239, previous_K14=48.1428, previous_D3=23.7507; 직전 완료 봉 목표를 다음 봉 시가에 모의 적용 |
| v2 | mfi_14_recovery | 9930.25 | -69.75 | sell / filled / 직전 MFI14 < 20, 현재 MFI14 >= 20 (한 봉 목표); 조건 미충족; MFI14=34.131, previous_MFI14=22.0435; 직전 완료 봉 목표를 다음 봉 시가에 모의 적용 |
| v2 | adx_14_trend | 9718.27 | -281.73 | sell / filled / Wilder ADX14 >= 25 그리고 +DI14 > -DI14; 조건 미충족; ADX14=27.8461, plus_DI14=25.882, minus_DI14=28.4558; 직전 완료 봉 목표를 다음 봉 시가에 모의 적용 |
| v2 | aroon_25_trend | 9736.11 | -263.89 | sell / filled / Aroon25 Up > 70 그리고 Down < 30 (동률이면 최신 극값); 조건 미충족; Aroon_up=68, Aroon_down=4; 직전 완료 봉 목표를 다음 봉 시가에 모의 적용 |
| v2 | cci_20_momentum | 9708.90 | -291.10 | sell / filled / CCI20 > 100 (전형가격·평균절대편차); 조건 미충족; CCI20=-314.625; 직전 완료 봉 목표를 다음 봉 시가에 모의 적용 |
| v2 | williams_14_recovery | 9726.79 | -273.21 | sell / filled / 직전 Williams %R14 < -80, 현재 >= -80 (한 봉 목표); 조건 미충족; Williams_R14=-31.9999, previous_R14=-51.8572; 직전 완료 봉 목표를 다음 봉 시가에 모의 적용 |
| v2 | cmf_20_accumulation | 9651.03 | -348.97 | buy / partial / Chaikin Money Flow20 > 0.1; 조건 충족; CMF20=0.23674, volume20=1.30084e+07; 직전 완료 봉 목표를 다음 봉 시가에 모의 적용 |
| v2 | chaikin_3_10 | 9339.93 | -660.07 | buy / partial / ADL의 EMA3 - EMA10 > 0 그리고 종가 > EMA26; 조건 충족; Chaikin3_10=2029.77, ADL=-2.70969e+07, close=275.78, EMA26=275.675; 직전 완료 봉 목표를 다음 봉 시가에 모의 적용 |
| v2 | roc_10_momentum | 9994.39 | -5.61 | sell / filled / 10봉 ROC > 1% 그리고 종가 > EMA26; 조건 미충족; ROC10_percent=0.995963, close=275.315, EMA26=273.754; 직전 완료 봉 목표를 다음 봉 시가에 모의 적용 |
| v2 | trix_15_trend | 9804.07 | -195.93 | sell / filled / 15봉 삼중 EMA의 1봉 변화율 TRIX > 0 그리고 종가 > EMA26; 조건 미충족; TRIX15_percent=0.00744142, close=276.06, EMA26=276.447; 직전 완료 봉 목표를 다음 봉 시가에 모의 적용 |
| v2 | keltner_20_breakout | 9873.30 | -126.70 | sell / filled / 종가 > EMA20 + 2 x Wilder ATR14; 조건 미충족; close=276.4, upper_Keltner=277.094, EMA20=275.768, ATR14=0.662947; 직전 완료 봉 목표를 다음 봉 시가에 모의 적용 |
| v2 | opening_range_30m | 9943.69 | -56.31 | buy / partial / 뉴욕 09:30·09:45 두 완료 봉 최고가를 10:00 이후 종가가 돌파; 조건 충족; close=275.725, opening_high=275.24; 직전 완료 봉 목표를 다음 봉 시가에 모의 적용 |

### 같은 기간의 비용·노출 비교 (사후 연구)

| 전략 | 비용 전 | 비용 후 | 100% 보유 | 같은 평균 노출 보유 | 평균 노출 |
|---|---:|---:|---:|---:|---:|
| cash | 0.00% | 0.00% | -2.11% | -0.00% | 0.00% |
| buy_hold | -1.70% | -2.11% | -2.11% | -2.11% | 100.00% |
| trend_8_26 | -1.54% | -5.19% | -2.11% | -0.99% | 46.34% |
| momentum_26 | 0.72% | -5.83% | -2.11% | -0.90% | 42.15% |
| breakout_8 | -1.25% | -16.17% | -2.11% | -0.41% | 19.37% |
| reversion_12 | -0.99% | -12.34% | -2.11% | -0.58% | 26.96% |
| volume_26 | 0.06% | -7.22% | -2.11% | -0.19% | 8.64% |
| trend_8_26 AND momentum_26 | 0.13% | -3.99% | -2.11% | -0.77% | 36.13% |
| trend_8_26 + momentum_26 | -0.41% | -4.91% | -2.11% | -0.94% | 44.24% |
| trend_8_26 AND breakout_8 | -0.64% | -9.79% | -2.11% | -0.26% | 12.30% |
| trend_8_26 + breakout_8 | -1.39% | -10.66% | -2.11% | -0.70% | 32.86% |
| trend_8_26 AND reversion_12 | -0.94% | -4.61% | -2.11% | -0.12% | 5.50% |
| trend_8_26 + reversion_12 | -1.26% | -8.84% | -2.11% | -0.78% | 36.65% |
| trend_8_26 AND volume_26 | -0.31% | -3.61% | -2.11% | -0.06% | 2.88% |
| trend_8_26 + volume_26 | -0.73% | -5.82% | -2.11% | -0.59% | 27.49% |
| momentum_26 AND breakout_8 | 0.08% | -9.51% | -2.11% | -0.26% | 12.04% |
| momentum_26 + breakout_8 | -0.27% | -10.78% | -2.11% | -0.66% | 30.77% |
| momentum_26 AND reversion_12 | -0.35% | -2.42% | -2.11% | -0.05% | 2.36% |
| momentum_26 + reversion_12 | -0.13% | -7.80% | -2.11% | -0.74% | 34.56% |
| momentum_26 AND volume_26 | 0.43% | -2.48% | -2.11% | -0.05% | 2.36% |
| momentum_26 + volume_26 | 0.40% | -5.94% | -2.11% | -0.54% | 25.40% |
| breakout_8 AND reversion_12 | 0.00% | 0.00% | -2.11% | -0.00% | 0.00% |
| breakout_8 + reversion_12 | -1.11% | -13.38% | -2.11% | -0.50% | 23.18% |
| breakout_8 AND volume_26 | -0.63% | -3.91% | -2.11% | -0.05% | 2.36% |
| breakout_8 + volume_26 | -0.59% | -11.44% | -2.11% | -0.30% | 14.01% |
| reversion_12 AND volume_26 | 0.75% | -3.80% | -2.11% | -0.08% | 3.66% |
| reversion_12 + volume_26 | -0.46% | -9.25% | -2.11% | -0.38% | 17.81% |
| ema_12_26 | 0.47% | -2.85% | -2.11% | -0.92% | 43.19% |
| macd_12_26_9 | 1.99% | -0.96% | -2.11% | -0.50% | 23.56% |
| rsi_14_recovery | -0.88% | -4.95% | -2.11% | -0.06% | 2.62% |
| bollinger_20_reentry | -0.28% | -5.58% | -2.11% | -0.07% | 3.40% |
| donchian_20 | -0.07% | -4.58% | -2.11% | -0.12% | 5.50% |
| atr_14_breakout | -0.74% | -7.58% | -2.11% | -0.10% | 4.71% |
| session_vwap | -1.51% | -13.89% | -2.11% | -1.07% | 50.52% |
| obv_20 | -0.22% | -5.53% | -2.11% | -0.84% | 39.27% |
| stochastic_14_3_recovery | -0.09% | -12.29% | -2.11% | -0.17% | 8.12% |
| mfi_14_recovery | 0.20% | -3.92% | -2.11% | -0.06% | 2.62% |
| adx_14_trend | 0.33% | -2.17% | -2.11% | -0.65% | 30.37% |
| aroon_25_trend | -0.41% | -4.11% | -2.11% | -0.37% | 17.28% |
| cci_20_momentum | -0.93% | -7.76% | -2.11% | -0.40% | 18.59% |
| williams_14_recovery | 0.62% | -9.02% | -2.11% | -0.13% | 6.28% |
| cmf_20_accumulation | 0.10% | -6.79% | -2.11% | -0.61% | 28.80% |
| chaikin_3_10 | -1.36% | -10.06% | -2.11% | -0.76% | 35.86% |
| roc_10_momentum | 0.32% | -0.52% | -2.11% | -0.08% | 3.66% |
| trix_15_trend | 0.63% | -2.69% | -2.11% | -0.70% | 32.72% |
| keltner_20_breakout | 0.21% | -2.69% | -2.11% | -0.12% | 5.76% |
| opening_range_30m | 1.57% | -2.61% | -2.11% | -0.58% | 26.96% |

동일 구간·초기 자금, 종료 시 청산 비용 포함. 노출 맞춤은 사후 설명용이며 v2 실제 계좌 성과가 아닙니다.
[낙폭 분해·비용 영향·전체 구간](IWM/comparison.json)

[v1 전체 기록](IWM/accounts.json) · [v2 전체 기록](IWM/accounts-v2.json)

## DIA 계좌

| 모델 | 전략 | 평가액 USD | 손익 USD | 최근 매매·이유 |
|---|---|---:|---:|---|
| v1 | cash | 10000.00 | 0.00 | 대기 /  / 새 신호 대기 |
| v1 | buy_hold | 9968.77 | -31.23 | buy /  / buy_hold: prior completed bar target 100%; next bar open simulation |
| v1 | trend_8_26 | 9855.65 | -144.35 | sell /  / trend_8_26: prior completed bar target 0%; next bar open simulation |
| v1 | momentum_26 | 9668.66 | -331.34 | sell /  / momentum_26: prior completed bar target 0%; next bar open simulation |
| v1 | breakout_8 | 9293.36 | -706.64 | sell /  / breakout_8: prior completed bar target 0%; next bar open simulation |
| v1 | reversion_12 | 9761.85 | -238.15 | sell /  / reversion_12: prior completed bar target 0%; next bar open simulation |
| v1 | volume_26 | 9754.48 | -245.52 | sell /  / volume_26: prior completed bar target 0%; next bar open simulation |
| v1 | trend_8_26 AND momentum_26 | 9665.55 | -334.45 | sell /  / trend_8_26 AND momentum_26: prior completed bar target 0%; next bar open simulation |
| v1 | trend_8_26 + momentum_26 | 9761.79 | -238.21 | sell /  / trend_8_26 + momentum_26: prior completed bar target 0%; next bar open simulation |
| v1 | trend_8_26 AND breakout_8 | 9561.79 | -438.21 | sell /  / trend_8_26 AND breakout_8: prior completed bar target 0%; next bar open simulation |
| v1 | trend_8_26 + breakout_8 | 9628.01 | -371.99 | sell /  / trend_8_26 + breakout_8: prior completed bar target 0%; next bar open simulation |
| v1 | trend_8_26 AND reversion_12 | 9865.72 | -134.28 | sell /  / trend_8_26 AND reversion_12: prior completed bar target 0%; next bar open simulation |
| v1 | trend_8_26 + reversion_12 | 9828.04 | -171.96 | sell /  / trend_8_26 + reversion_12: prior completed bar target 0%; next bar open simulation |
| v1 | trend_8_26 AND volume_26 | 9839.32 | -160.68 | sell /  / trend_8_26 AND volume_26: prior completed bar target 0%; next bar open simulation |
| v1 | trend_8_26 + volume_26 | 9804.74 | -195.26 | sell /  / trend_8_26 + volume_26: prior completed bar target 0%; next bar open simulation |
| v1 | momentum_26 AND breakout_8 | 9420.05 | -579.95 | sell /  / momentum_26 AND breakout_8: prior completed bar target 0%; next bar open simulation |
| v1 | momentum_26 + breakout_8 | 9479.27 | -520.73 | sell /  / momentum_26 + breakout_8: prior completed bar target 0%; next bar open simulation |
| v1 | momentum_26 AND reversion_12 | 9865.74 | -134.26 | sell /  / momentum_26 AND reversion_12: prior completed bar target 0%; next bar open simulation |
| v1 | momentum_26 + reversion_12 | 9773.35 | -226.65 | sell /  / momentum_26 + reversion_12: prior completed bar target 0%; next bar open simulation |
| v1 | momentum_26 AND volume_26 | 9757.36 | -242.64 | sell /  / momentum_26 AND volume_26: prior completed bar target 0%; next bar open simulation |
| v1 | momentum_26 + volume_26 | 9730.80 | -269.20 | sell /  / momentum_26 + volume_26: prior completed bar target 0%; next bar open simulation |
| v1 | breakout_8 AND reversion_12 | 10000.00 | 0.00 | 대기 /  / 새 신호 대기 |
| v1 | breakout_8 + reversion_12 | 9562.58 | -437.42 | sell /  / breakout_8 + reversion_12: prior completed bar target 0%; next bar open simulation |
| v1 | breakout_8 AND volume_26 | 9876.84 | -123.16 | sell /  / breakout_8 AND volume_26: prior completed bar target 0%; next bar open simulation |
| v1 | breakout_8 + volume_26 | 9559.16 | -440.84 | sell /  / breakout_8 + volume_26: prior completed bar target 0%; next bar open simulation |
| v1 | reversion_12 AND volume_26 | 9917.39 | -82.61 | sell /  / reversion_12 AND volume_26: prior completed bar target 0%; next bar open simulation |
| v1 | reversion_12 + volume_26 | 9797.09 | -202.91 | sell /  / reversion_12 + volume_26: prior completed bar target 0%; next bar open simulation |
| v1 | ema_12_26 | 9803.63 | -196.37 | sell /  / EMA12 > EMA26; 조건 미충족; EMA12=526.379, EMA26=526.494 |
| v1 | macd_12_26_9 | 9752.67 | -247.33 | sell /  / MACD > 신호선 그리고 MACD > 0; 조건 미충족; MACD=-0.115547, signal9=0.181673 |
| v1 | rsi_14_recovery | 9985.10 | -14.90 | sell /  / 직전 RSI14 < 30, 현재 RSI14 >= 30 (한 봉 목표); 조건 미충족; RSI14=40.1529, previous_RSI14=32.5751 |
| v1 | bollinger_20_reentry | 9925.00 | -75.00 | sell /  / 직전 종가 < 직전 하단밴드, 현재 하단밴드 <= 종가 <= SMA20 (한 봉 목표); 조건 미충족; close=522.815, lower20=520.55, SMA20=525.436, previous_lower20=520.821 |
| v1 | donchian_20 | 9675.11 | -324.89 | sell /  / 종가 > 현재 봉을 제외한 직전 20봉 최고가; 조건 미충족; close=526.71, prior_high20=528.45 |
| v1 | atr_14_breakout | 9709.35 | -290.65 | sell /  / 종가 > 직전 종가 + 직전 ATR14 그리고 종가 > EMA26; 조건 미충족; close=527.625, threshold=528.531, prior_ATR14=1.00085, EMA26=526.218 |
| v1 | session_vwap | 9556.14 | -443.86 | buy /  / 종가 > 뉴욕 거래일별 누적 전형가격 VWAP; 조건 충족; close=522.17, session_VWAP=522.11, session_volume=2.27683e+06 |
| v1 | obv_20 | 9727.80 | -272.20 | sell /  / OBV > OBV의 SMA20 그리고 종가 > EMA26; 조건 미충족; OBV=-6.66951e+06, OBV_SMA20=-6.32674e+06, close=522.39, EMA26=526.494 |
| v1 | stochastic_14_3_recovery | 9688.29 | -311.71 | sell /  / 직전 %K14 < 20에서 %K14가 %D3 상향 돌파 (한 봉 목표); 조건 미충족; K14=35.6623, D3=20.5547, previous_K14=19.3192, previous_D3=8.7863 |
| v1 | mfi_14_recovery | 9902.01 | -97.99 | sell /  / 직전 MFI14 < 20, 현재 MFI14 >= 20 (한 봉 목표); 조건 미충족; MFI14=29.4378, previous_MFI14=21.6288 |
| v1 | adx_14_trend | 9711.49 | -288.51 | sell /  / Wilder ADX14 >= 25 그리고 +DI14 > -DI14; 조건 미충족; ADX14=28.0997, plus_DI14=30.0206, minus_DI14=36.1913 |
| v1 | aroon_25_trend | 9820.69 | -179.31 | sell /  / Aroon25 Up > 70 그리고 Down < 30 (동률이면 최신 극값); 조건 미충족; Aroon_up=72, Aroon_down=92 |
| v1 | cci_20_momentum | 9709.75 | -290.25 | sell /  / CCI20 > 100 (전형가격·평균절대편차); 조건 미충족; CCI20=-498.183 |
| v1 | williams_14_recovery | 9697.88 | -302.12 | sell /  / 직전 Williams %R14 < -80, 현재 >= -80 (한 봉 목표); 조건 미충족; Williams_R14=-68.4085, previous_R14=-64.3377 |
| v1 | cmf_20_accumulation | 9385.39 | -614.61 | buy /  / Chaikin Money Flow20 > 0.1; 조건 충족; CMF20=0.140077, volume20=2.63627e+06 |
| v1 | chaikin_3_10 | 9611.06 | -388.94 | sell /  / ADL의 EMA3 - EMA10 > 0 그리고 종가 > EMA26; 조건 미충족; Chaikin3_10=70160.2, ADL=-1.15315e+07, close=522.39, EMA26=526.494 |
| v1 | roc_10_momentum | 9939.01 | -60.99 | sell /  / 10봉 ROC > 1% 그리고 종가 > EMA26; 조건 미충족; ROC10_percent=0.771645, close=523.68, EMA26=521.367 |
| v1 | trix_15_trend | 9741.60 | -258.40 | sell /  / 15봉 삼중 EMA의 1봉 변화율 TRIX > 0 그리고 종가 > EMA26; 조건 미충족; TRIX15_percent=0.0047414, close=522.39, EMA26=526.494 |
| v1 | keltner_20_breakout | 9826.82 | -173.18 | sell /  / 종가 > EMA20 + 2 x Wilder ATR14; 조건 미충족; close=526.34, upper_Keltner=527.991, EMA20=526.293, ATR14=0.848911 |
| v1 | opening_range_30m | 9536.25 | -463.75 | sell /  / 뉴욕 09:30·09:45 두 완료 봉 최고가를 10:00 이후 종가가 돌파; 자료 부족·변동폭 또는 거래량 없음: 대기; close=522.39 |
| v2 | cash | 10000.00 | 0.00 | 대기 /  / 새 신호 대기 |
| v2 | buy_hold | 10092.27 | 92.27 | buy / partial / 직전 완료 봉 목표 비중 100%; 다음 봉 시가 가정 |
| v2 | trend_8_26 | 9784.94 | -215.06 | sell / filled / 직전 완료 봉 목표 비중 0%; 다음 봉 시가 가정 |
| v2 | momentum_26 | 9699.02 | -300.98 | sell / filled / 직전 완료 봉 목표 비중 0%; 다음 봉 시가 가정 |
| v2 | breakout_8 | 8932.87 | -1067.13 | 중단: 손실 한도 / buy / partial / 직전 완료 봉 목표 비중 100%; 다음 봉 시가 가정 |
| v2 | reversion_12 | 9451.93 | -548.07 | sell / filled / 직전 완료 봉 목표 비중 0%; 다음 봉 시가 가정 |
| v2 | volume_26 | 9462.56 | -537.44 | sell / filled / 직전 완료 봉 목표 비중 0%; 다음 봉 시가 가정 |
| v2 | trend_8_26 AND momentum_26 | 9689.46 | -310.54 | sell / filled / 직전 완료 봉 목표 비중 0%; 다음 봉 시가 가정 |
| v2 | trend_8_26 + momentum_26 | 9742.04 | -257.96 | sell / filled / 직전 완료 봉 목표 비중 0%; 다음 봉 시가 가정 |
| v2 | trend_8_26 AND breakout_8 | 9241.90 | -758.10 | sell / filled / 직전 완료 봉 목표 비중 0%; 다음 봉 시가 가정 |
| v2 | trend_8_26 + breakout_8 | 9350.97 | -649.03 | sell / filled / 직전 완료 봉 목표 비중 0%; 다음 봉 시가 가정 |
| v2 | trend_8_26 AND reversion_12 | 9669.36 | -330.64 | sell / filled / 직전 완료 봉 목표 비중 0%; 다음 봉 시가 가정 |
| v2 | trend_8_26 + reversion_12 | 9636.71 | -363.29 | sell / filled / 직전 완료 봉 목표 비중 0%; 다음 봉 시가 가정 |
| v2 | trend_8_26 AND volume_26 | 9688.83 | -311.17 | sell / filled / 직전 완료 봉 목표 비중 0%; 다음 봉 시가 가정 |
| v2 | trend_8_26 + volume_26 | 9642.37 | -357.63 | sell / filled / 직전 완료 봉 목표 비중 0%; 다음 봉 시가 가정 |
| v2 | momentum_26 AND breakout_8 | 9090.90 | -909.10 | sell / filled / 직전 완료 봉 목표 비중 0%; 다음 봉 시가 가정 |
| v2 | momentum_26 + breakout_8 | 9251.50 | -748.50 | sell / filled / 직전 완료 봉 목표 비중 0%; 다음 봉 시가 가정 |
| v2 | momentum_26 AND reversion_12 | 9814.45 | -185.55 | sell / filled / 직전 완료 봉 목표 비중 0%; 다음 봉 시가 가정 |
| v2 | momentum_26 + reversion_12 | 9634.73 | -365.27 | sell / filled / 직전 완료 봉 목표 비중 0%; 다음 봉 시가 가정 |
| v2 | momentum_26 AND volume_26 | 9540.48 | -459.52 | sell / filled / 직전 완료 봉 목표 비중 0%; 다음 봉 시가 가정 |
| v2 | momentum_26 + volume_26 | 9640.55 | -359.45 | sell / filled / 직전 완료 봉 목표 비중 0%; 다음 봉 시가 가정 |
| v2 | breakout_8 AND reversion_12 | 10000.00 | 0.00 | 대기 /  / 새 신호 대기 |
| v2 | breakout_8 + reversion_12 | 9170.34 | -829.66 | sell / filled / 직전 완료 봉 목표 비중 0%; 다음 봉 시가 가정 |
| v2 | breakout_8 AND volume_26 | 9668.17 | -331.83 | sell / filled / 직전 완료 봉 목표 비중 0%; 다음 봉 시가 가정 |
| v2 | breakout_8 + volume_26 | 9175.95 | -824.05 | sell / filled / 직전 완료 봉 목표 비중 0%; 다음 봉 시가 가정 |
| v2 | reversion_12 AND volume_26 | 9909.46 | -90.54 | sell / filled / 직전 완료 봉 목표 비중 0%; 다음 봉 시가 가정 |
| v2 | reversion_12 + volume_26 | 9496.59 | -503.41 | sell / filled / 직전 완료 봉 목표 비중 0%; 다음 봉 시가 가정 |
| v2 | ema_12_26 | 9797.75 | -202.25 | sell / filled / EMA12 > EMA26; 조건 미충족; EMA12=526.379, EMA26=526.494; 직전 완료 봉 목표를 다음 봉 시가에 모의 적용 |
| v2 | macd_12_26_9 | 9740.97 | -259.03 | sell / filled / MACD > 신호선 그리고 MACD > 0; 조건 미충족; MACD=-0.115547, signal9=0.181673; 직전 완료 봉 목표를 다음 봉 시가에 모의 적용 |
| v2 | rsi_14_recovery | 9983.11 | -16.89 | sell / filled / 직전 RSI14 < 30, 현재 RSI14 >= 30 (한 봉 목표); 조건 미충족; RSI14=40.1529, previous_RSI14=32.5751; 직전 완료 봉 목표를 다음 봉 시가에 모의 적용 |
| v2 | bollinger_20_reentry | 9919.05 | -80.95 | sell / filled / 직전 종가 < 직전 하단밴드, 현재 하단밴드 <= 종가 <= SMA20 (한 봉 목표); 조건 미충족; close=522.815, lower20=520.55, SMA20=525.436, previous_lower20=520.821; 직전 완료 봉 목표를 다음 봉 시가에 모의 적용 |
| v2 | donchian_20 | 9661.57 | -338.43 | sell / filled / 종가 > 현재 봉을 제외한 직전 20봉 최고가; 조건 미충족; close=526.71, prior_high20=528.45; 직전 완료 봉 목표를 다음 봉 시가에 모의 적용 |
| v2 | atr_14_breakout | 9693.83 | -306.17 | sell / filled / 종가 > 직전 종가 + 직전 ATR14 그리고 종가 > EMA26; 조건 미충족; close=527.625, threshold=528.531, prior_ATR14=1.00085, EMA26=526.218; 직전 완료 봉 목표를 다음 봉 시가에 모의 적용 |
| v2 | session_vwap | 9538.00 | -462.00 | buy / partial / 종가 > 뉴욕 거래일별 누적 전형가격 VWAP; 조건 충족; close=522.17, session_VWAP=522.11, session_volume=2.27683e+06; 직전 완료 봉 목표를 다음 봉 시가에 모의 적용 |
| v2 | obv_20 | 9712.25 | -287.75 | sell / filled / OBV > OBV의 SMA20 그리고 종가 > EMA26; 조건 미충족; OBV=-6.66951e+06, OBV_SMA20=-6.32674e+06, close=522.39, EMA26=526.494; 직전 완료 봉 목표를 다음 봉 시가에 모의 적용 |
| v2 | stochastic_14_3_recovery | 9670.86 | -329.14 | sell / filled / 직전 %K14 < 20에서 %K14가 %D3 상향 돌파 (한 봉 목표); 조건 미충족; K14=35.6623, D3=20.5547, previous_K14=19.3192, previous_D3=8.7863; 직전 완료 봉 목표를 다음 봉 시가에 모의 적용 |
| v2 | mfi_14_recovery | 9896.07 | -103.93 | sell / filled / 직전 MFI14 < 20, 현재 MFI14 >= 20 (한 봉 목표); 조건 미충족; MFI14=29.4378, previous_MFI14=21.6288; 직전 완료 봉 목표를 다음 봉 시가에 모의 적용 |
| v2 | adx_14_trend | 9701.78 | -298.22 | sell / filled / Wilder ADX14 >= 25 그리고 +DI14 > -DI14; 조건 미충족; ADX14=28.0997, plus_DI14=30.0206, minus_DI14=36.1913; 직전 완료 봉 목표를 다음 봉 시가에 모의 적용 |
| v2 | aroon_25_trend | 9810.88 | -189.12 | sell / filled / Aroon25 Up > 70 그리고 Down < 30 (동률이면 최신 극값); 조건 미충족; Aroon_up=72, Aroon_down=92; 직전 완료 봉 목표를 다음 봉 시가에 모의 적용 |
| v2 | cci_20_momentum | 9694.23 | -305.77 | sell / filled / CCI20 > 100 (전형가격·평균절대편차); 조건 미충족; CCI20=-498.183; 직전 완료 봉 목표를 다음 봉 시가에 모의 적용 |
| v2 | williams_14_recovery | 9682.38 | -317.62 | sell / filled / 직전 Williams %R14 < -80, 현재 >= -80 (한 봉 목표); 조건 미충족; Williams_R14=-68.4085, previous_R14=-64.3377; 직전 완료 봉 목표를 다음 봉 시가에 모의 적용 |
| v2 | cmf_20_accumulation | 9363.83 | -636.17 | buy / partial / Chaikin Money Flow20 > 0.1; 조건 충족; CMF20=0.140077, volume20=2.63627e+06; 직전 완료 봉 목표를 다음 봉 시가에 모의 적용 |
| v2 | chaikin_3_10 | 9595.70 | -404.30 | sell / filled / ADL의 EMA3 - EMA10 > 0 그리고 종가 > EMA26; 조건 미충족; Chaikin3_10=70160.2, ADL=-1.15315e+07, close=522.39, EMA26=526.494; 직전 완료 봉 목표를 다음 봉 시가에 모의 적용 |
| v2 | roc_10_momentum | 9937.03 | -62.97 | sell / filled / 10봉 ROC > 1% 그리고 종가 > EMA26; 조건 미충족; ROC10_percent=0.771645, close=523.68, EMA26=521.367; 직전 완료 봉 목표를 다음 봉 시가에 모의 적용 |
| v2 | trix_15_trend | 9731.86 | -268.14 | sell / filled / 15봉 삼중 EMA의 1봉 변화율 TRIX > 0 그리고 종가 > EMA26; 조건 미충족; TRIX15_percent=0.0047414, close=522.39, EMA26=526.494; 직전 완료 봉 목표를 다음 봉 시가에 모의 적용 |
| v2 | keltner_20_breakout | 9817.00 | -183.00 | sell / filled / 종가 > EMA20 + 2 x Wilder ATR14; 조건 미충족; close=526.34, upper_Keltner=527.991, EMA20=526.293, ATR14=0.848911; 직전 완료 봉 목표를 다음 봉 시가에 모의 적용 |
| v2 | opening_range_30m | 9517.20 | -482.80 | sell / filled / 뉴욕 09:30·09:45 두 완료 봉 최고가를 10:00 이후 종가가 돌파; 자료 부족·변동폭 또는 거래량 없음: 대기; close=522.39; 직전 완료 봉 목표를 다음 봉 시가에 모의 적용 |

### 같은 기간의 비용·노출 비교 (사후 연구)

| 전략 | 비용 전 | 비용 후 | 100% 보유 | 같은 평균 노출 보유 | 평균 노출 |
|---|---:|---:|---:|---:|---:|
| cash | 0.00% | 0.00% | 2.31% | 0.00% | 0.00% |
| buy_hold | 2.74% | 2.31% | 2.31% | 2.31% | 100.00% |
| trend_8_26 | 2.35% | -1.45% | 2.31% | 1.43% | 62.30% |
| momentum_26 | 1.43% | -3.15% | 2.31% | 1.37% | 59.69% |
| breakout_8 | 0.31% | -16.61% | 2.31% | 0.58% | 25.39% |
| reversion_12 | 1.10% | -7.43% | 2.31% | 0.44% | 19.37% |
| volume_26 | 1.74% | -7.24% | 2.31% | 0.22% | 9.69% |
| trend_8_26 AND momentum_26 | 2.82% | -2.23% | 2.31% | 1.21% | 52.88% |
| trend_8_26 + momentum_26 | 1.89% | -2.30% | 2.31% | 1.40% | 61.00% |
| trend_8_26 AND breakout_8 | 1.39% | -10.99% | 2.31% | 0.41% | 18.06% |
| trend_8_26 + breakout_8 | 1.33% | -8.58% | 2.31% | 1.00% | 43.85% |
| trend_8_26 AND reversion_12 | 0.81% | -4.55% | 2.31% | 0.16% | 7.07% |
| trend_8_26 + reversion_12 | 1.73% | -4.29% | 2.31% | 0.93% | 40.84% |
| trend_8_26 AND volume_26 | 2.07% | -3.35% | 2.31% | 0.12% | 5.50% |
| trend_8_26 + volume_26 | 2.05% | -4.19% | 2.31% | 0.82% | 36.00% |
| momentum_26 AND breakout_8 | 0.60% | -12.79% | 2.31% | 0.46% | 20.42% |
| momentum_26 + breakout_8 | 0.88% | -10.13% | 2.31% | 0.97% | 42.55% |
| momentum_26 AND reversion_12 | 0.10% | -3.21% | 2.31% | 0.12% | 5.50% |
| momentum_26 + reversion_12 | 1.28% | -4.52% | 2.31% | 0.90% | 39.53% |
| momentum_26 AND volume_26 | 0.52% | -5.62% | 2.31% | 0.13% | 5.76% |
| momentum_26 + volume_26 | 1.59% | -4.62% | 2.31% | 0.79% | 34.69% |
| breakout_8 AND reversion_12 | 0.00% | 0.00% | 2.31% | 0.00% | 0.00% |
| breakout_8 + reversion_12 | 0.71% | -11.78% | 2.31% | 0.51% | 22.39% |
| breakout_8 AND volume_26 | 0.28% | -3.44% | 2.31% | 0.08% | 3.40% |
| breakout_8 + volume_26 | 1.03% | -11.13% | 2.31% | 0.40% | 17.55% |
| reversion_12 AND volume_26 | 1.21% | -2.13% | 2.31% | 0.05% | 2.36% |
| reversion_12 + volume_26 | 1.43% | -6.95% | 2.31% | 0.33% | 14.53% |
| ema_12_26 | 1.22% | -0.88% | 2.31% | 1.39% | 60.73% |
| macd_12_26_9 | 2.44% | -1.77% | 2.31% | 0.73% | 31.94% |
| rsi_14_recovery | 0.39% | -0.86% | 2.31% | 0.02% | 0.79% |
| bollinger_20_reentry | 0.60% | -2.72% | 2.31% | 0.05% | 2.09% |
| donchian_20 | 0.32% | -7.76% | 2.31% | 0.25% | 10.99% |
| atr_14_breakout | -0.20% | -8.63% | 2.31% | 0.15% | 6.54% |
| session_vwap | 1.30% | -6.47% | 2.31% | 1.45% | 63.35% |
| obv_20 | 1.83% | -5.58% | 2.31% | 1.03% | 45.29% |
| stochastic_14_3_recovery | 1.62% | -9.28% | 2.31% | 0.16% | 7.07% |
| mfi_14_recovery | 0.37% | -2.95% | 2.31% | 0.05% | 2.09% |
| adx_14_trend | 0.37% | -3.35% | 2.31% | 0.75% | 32.72% |
| aroon_25_trend | 1.75% | -2.02% | 2.31% | 0.63% | 27.49% |
| cci_20_momentum | 2.05% | -4.58% | 2.31% | 0.64% | 28.01% |
| williams_14_recovery | 1.56% | -6.23% | 2.31% | 0.11% | 4.97% |
| cmf_20_accumulation | -0.04% | -8.86% | 2.31% | 1.06% | 46.34% |
| chaikin_3_10 | 1.04% | -8.26% | 2.31% | 1.18% | 51.57% |
| roc_10_momentum | -0.07% | -0.90% | 2.31% | 0.05% | 2.09% |
| trix_15_trend | 0.80% | -2.94% | 2.31% | 1.25% | 54.45% |
| keltner_20_breakout | 1.05% | -6.31% | 2.31% | 0.45% | 19.90% |
| opening_range_30m | 1.10% | -6.66% | 2.31% | 0.75% | 32.72% |

동일 구간·초기 자금, 종료 시 청산 비용 포함. 노출 맞춤은 사후 설명용이며 v2 실제 계좌 성과가 아닙니다.
[낙폭 분해·비용 영향·전체 구간](DIA/comparison.json)

[v1 전체 기록](DIA/accounts.json) · [v2 전체 기록](DIA/accounts-v2.json)

## MSFT 계좌

| 모델 | 전략 | 평가액 USD | 손익 USD | 최근 매매·이유 |
|---|---|---:|---:|---|
| v1 | cash | 10000.00 | 0.00 | 대기 /  / 새 신호 대기 |
| v1 | buy_hold | 9670.98 | -329.02 | buy /  / buy_hold: prior completed bar target 100%; next bar open simulation |
| v1 | trend_8_26 | 9408.99 | -591.01 | buy /  / trend_8_26: prior completed bar target 100%; next bar open simulation |
| v1 | momentum_26 | 9200.18 | -799.82 | buy /  / momentum_26: prior completed bar target 100%; next bar open simulation |
| v1 | breakout_8 | 9454.11 | -545.89 | sell /  / breakout_8: prior completed bar target 0%; next bar open simulation |
| v1 | reversion_12 | 9253.32 | -746.68 | sell /  / reversion_12: prior completed bar target 0%; next bar open simulation |
| v1 | volume_26 | 9604.15 | -395.85 | sell /  / volume_26: prior completed bar target 0%; next bar open simulation |
| v1 | trend_8_26 AND momentum_26 | 9337.80 | -662.20 | buy /  / trend_8_26 AND momentum_26: prior completed bar target 100%; next bar open simulation |
| v1 | trend_8_26 + momentum_26 | 9341.31 | -658.69 | buy /  / trend_8_26 + momentum_26: prior completed bar target 100%; next bar open simulation |
| v1 | trend_8_26 AND breakout_8 | 9678.51 | -321.49 | sell /  / trend_8_26 AND breakout_8: prior completed bar target 0%; next bar open simulation |
| v1 | trend_8_26 + breakout_8 | 9469.49 | -530.51 | buy /  / trend_8_26 + breakout_8: prior completed bar target 50%; next bar open simulation |
| v1 | trend_8_26 AND reversion_12 | 9486.50 | -513.50 | sell /  / trend_8_26 AND reversion_12: prior completed bar target 0%; next bar open simulation |
| v1 | trend_8_26 + reversion_12 | 9349.41 | -650.59 | sell /  / trend_8_26 + reversion_12: prior completed bar target 50%; next bar open simulation |
| v1 | trend_8_26 AND volume_26 | 9782.72 | -217.28 | sell /  / trend_8_26 AND volume_26: prior completed bar target 0%; next bar open simulation |
| v1 | trend_8_26 + volume_26 | 9506.16 | -493.84 | buy /  / trend_8_26 + volume_26: prior completed bar target 50%; next bar open simulation |
| v1 | momentum_26 AND breakout_8 | 9642.25 | -357.75 | sell /  / momentum_26 AND breakout_8: prior completed bar target 0%; next bar open simulation |
| v1 | momentum_26 + breakout_8 | 9345.08 | -654.92 | buy /  / momentum_26 + breakout_8: prior completed bar target 50%; next bar open simulation |
| v1 | momentum_26 AND reversion_12 | 9616.46 | -383.54 | sell /  / momentum_26 AND reversion_12: prior completed bar target 0%; next bar open simulation |
| v1 | momentum_26 + reversion_12 | 9282.08 | -717.92 | sell /  / momentum_26 + reversion_12: prior completed bar target 50%; next bar open simulation |
| v1 | momentum_26 AND volume_26 | 9830.16 | -169.84 | sell /  / momentum_26 AND volume_26: prior completed bar target 0%; next bar open simulation |
| v1 | momentum_26 + volume_26 | 9437.84 | -562.16 | buy /  / momentum_26 + volume_26: prior completed bar target 50%; next bar open simulation |
| v1 | breakout_8 AND reversion_12 | 10000.00 | 0.00 | 대기 /  / 새 신호 대기 |
| v1 | breakout_8 + reversion_12 | 9390.48 | -609.52 | sell /  / breakout_8 + reversion_12: prior completed bar target 0%; next bar open simulation |
| v1 | breakout_8 AND volume_26 | 9953.19 | -46.81 | sell /  / breakout_8 AND volume_26: prior completed bar target 0%; next bar open simulation |
| v1 | breakout_8 + volume_26 | 9566.82 | -433.18 | sell /  / breakout_8 + volume_26: prior completed bar target 0%; next bar open simulation |
| v1 | reversion_12 AND volume_26 | 9770.39 | -229.61 | sell /  / reversion_12 AND volume_26: prior completed bar target 0%; next bar open simulation |
| v1 | reversion_12 + volume_26 | 9445.90 | -554.10 | sell /  / reversion_12 + volume_26: prior completed bar target 0%; next bar open simulation |
| v1 | ema_12_26 | 9453.45 | -546.55 | buy /  / EMA12 > EMA26; 조건 충족; EMA12=524.345, EMA26=524.284 |
| v1 | macd_12_26_9 | 9565.51 | -434.49 | buy /  / MACD > 신호선 그리고 MACD > 0; 조건 충족; MACD=0.0602049, signal9=-0.410679 |
| v1 | rsi_14_recovery | 9839.66 | -160.34 | sell /  / 직전 RSI14 < 30, 현재 RSI14 >= 30 (한 봉 목표); 조건 미충족; RSI14=49.0008, previous_RSI14=38.029 |
| v1 | bollinger_20_reentry | 9745.81 | -254.19 | sell /  / 직전 종가 < 직전 하단밴드, 현재 하단밴드 <= 종가 <= SMA20 (한 봉 목표); 조건 미충족; close=523.535, lower20=518.78, SMA20=523.154, previous_lower20=518.792 |
| v1 | donchian_20 | 9912.16 | -87.84 | sell /  / 종가 > 현재 봉을 제외한 직전 20봉 최고가; 조건 미충족; close=534.52, prior_high20=535.44 |
| v1 | atr_14_breakout | 9915.10 | -84.90 | sell /  / 종가 > 직전 종가 + 직전 ATR14 그리고 종가 > EMA26; 조건 미충족; close=533.975, threshold=536.307, prior_ATR14=2.16203, EMA26=530.521 |
| v1 | session_vwap | 9630.76 | -369.24 | buy /  / 종가 > 뉴욕 거래일별 누적 전형가격 VWAP; 조건 충족; close=520.51, session_VWAP=518.805, session_volume=2.29852e+06 |
| v1 | obv_20 | 9475.03 | -524.97 | sell /  / OBV > OBV의 SMA20 그리고 종가 > EMA26; 조건 미충족; OBV=3.70404e+07, OBV_SMA20=4.23196e+07, close=524.11, EMA26=524.113 |
| v1 | stochastic_14_3_recovery | 9641.51 | -358.49 | sell /  / 직전 %K14 < 20에서 %K14가 %D3 상향 돌파 (한 봉 목표); 조건 미충족; K14=18.1724, D3=16.7161, previous_K14=21.0531, previous_D3=14.2045 |
| v1 | mfi_14_recovery | 9880.73 | -119.27 | sell /  / 직전 MFI14 < 20, 현재 MFI14 >= 20 (한 봉 목표); 조건 미충족; MFI14=28.323, previous_MFI14=32.1727 |
| v1 | adx_14_trend | 9883.62 | -116.38 | sell /  / Wilder ADX14 >= 25 그리고 +DI14 > -DI14; 조건 미충족; ADX14=23.6824, plus_DI14=22.3066, minus_DI14=19.9214 |
| v1 | aroon_25_trend | 9616.60 | -383.40 | sell /  / Aroon25 Up > 70 그리고 Down < 30 (동률이면 최신 극값); 조건 미충족; Aroon_up=96, Aroon_down=100 |
| v1 | cci_20_momentum | 9870.62 | -129.38 | sell /  / CCI20 > 100 (전형가격·평균절대편차); 조건 미충족; CCI20=99.2896 |
| v1 | williams_14_recovery | 9621.94 | -378.06 | sell /  / 직전 Williams %R14 < -80, 현재 >= -80 (한 봉 목표); 조건 미충족; Williams_R14=-12.9449, previous_R14=-50.616 |
| v1 | cmf_20_accumulation | 9569.53 | -430.47 | sell /  / Chaikin Money Flow20 > 0.1; 조건 미충족; CMF20=-0.143516, volume20=1.68966e+07 |
| v1 | chaikin_3_10 | 9512.73 | -487.27 | sell /  / ADL의 EMA3 - EMA10 > 0 그리고 종가 > EMA26; 조건 미충족; Chaikin3_10=-1.26329e+06, ADL=9.19087e+07, close=524.11, EMA26=524.113 |
| v1 | roc_10_momentum | 9912.67 | -87.33 | sell /  / 10봉 ROC > 1% 그리고 종가 > EMA26; 조건 미충족; ROC10_percent=0.691625, close=524.11, EMA26=524.113 |
| v1 | trix_15_trend | 9557.09 | -442.91 | sell /  / 15봉 삼중 EMA의 1봉 변화율 TRIX > 0 그리고 종가 > EMA26; 조건 미충족; TRIX15_percent=0.00481299, close=529.54, EMA26=531.788 |
| v1 | keltner_20_breakout | 9958.78 | -41.22 | sell /  / 종가 > EMA20 + 2 x Wilder ATR14; 조건 미충족; close=533.975, upper_Keltner=534.357, EMA20=530.111, ATR14=2.12332 |
| v1 | opening_range_30m | 9601.84 | -398.16 | buy /  / 뉴욕 09:30·09:45 두 완료 봉 최고가를 10:00 이후 종가가 돌파; 조건 충족; close=523.535, opening_high=522.36 |
| v2 | cash | 10000.00 | 0.00 | 대기 /  / 새 신호 대기 |
| v2 | buy_hold | 9723.75 | -276.25 | buy / partial / 직전 완료 봉 목표 비중 100%; 다음 봉 시가 가정 |
| v2 | trend_8_26 | 9341.81 | -658.19 | buy / partial / 직전 완료 봉 목표 비중 100%; 다음 봉 시가 가정 |
| v2 | momentum_26 | 9224.61 | -775.39 | buy / partial / 직전 완료 봉 목표 비중 100%; 다음 봉 시가 가정 |
| v2 | breakout_8 | 9238.63 | -761.37 | sell / filled / 직전 완료 봉 목표 비중 0%; 다음 봉 시가 가정 |
| v2 | reversion_12 | 9022.72 | -977.28 | 중단: 손실 한도 / buy / partial / 직전 완료 봉 목표 비중 100%; 다음 봉 시가 가정 |
| v2 | volume_26 | 9284.58 | -715.42 | sell / filled / 직전 완료 봉 목표 비중 0%; 다음 봉 시가 가정 |
| v2 | trend_8_26 AND momentum_26 | 9226.77 | -773.23 | buy / partial / 직전 완료 봉 목표 비중 100%; 다음 봉 시가 가정 |
| v2 | trend_8_26 + momentum_26 | 9322.35 | -677.65 | buy / partial / 직전 완료 봉 목표 비중 100%; 다음 봉 시가 가정 |
| v2 | trend_8_26 AND breakout_8 | 9318.21 | -681.79 | sell / filled / 직전 완료 봉 목표 비중 0%; 다음 봉 시가 가정 |
| v2 | trend_8_26 + breakout_8 | 9349.14 | -650.86 | buy / filled / 직전 완료 봉 목표 비중 50%; 다음 봉 시가 가정 |
| v2 | trend_8_26 AND reversion_12 | 9376.72 | -623.28 | sell / filled / 직전 완료 봉 목표 비중 0%; 다음 봉 시가 가정 |
| v2 | trend_8_26 + reversion_12 | 9125.30 | -874.70 | sell / filled / 직전 완료 봉 목표 비중 50%; 다음 봉 시가 가정 |
| v2 | trend_8_26 AND volume_26 | 9722.77 | -277.23 | sell / filled / 직전 완료 봉 목표 비중 0%; 다음 봉 시가 가정 |
| v2 | trend_8_26 + volume_26 | 9332.60 | -667.40 | buy / filled / 직전 완료 봉 목표 비중 50%; 다음 봉 시가 가정 |
| v2 | momentum_26 AND breakout_8 | 9430.77 | -569.23 | sell / filled / 직전 완료 봉 목표 비중 0%; 다음 봉 시가 가정 |
| v2 | momentum_26 + breakout_8 | 9251.19 | -748.81 | buy / filled / 직전 완료 봉 목표 비중 50%; 다음 봉 시가 가정 |
| v2 | momentum_26 AND reversion_12 | 9440.54 | -559.46 | sell / filled / 직전 완료 봉 목표 비중 0%; 다음 봉 시가 가정 |
| v2 | momentum_26 + reversion_12 | 9106.08 | -893.92 | sell / filled / 직전 완료 봉 목표 비중 50%; 다음 봉 시가 가정 |
| v2 | momentum_26 AND volume_26 | 9695.84 | -304.16 | sell / filled / 직전 완료 봉 목표 비중 0%; 다음 봉 시가 가정 |
| v2 | momentum_26 + volume_26 | 9313.12 | -686.88 | buy / filled / 직전 완료 봉 목표 비중 50%; 다음 봉 시가 가정 |
| v2 | breakout_8 AND reversion_12 | 10000.00 | 0.00 | 대기 /  / 새 신호 대기 |
| v2 | breakout_8 + reversion_12 | 9112.97 | -887.03 | sell / filled / 직전 완료 봉 목표 비중 0%; 다음 봉 시가 가정 |
| v2 | breakout_8 AND volume_26 | 9890.09 | -109.91 | sell / filled / 직전 완료 봉 목표 비중 0%; 다음 봉 시가 가정 |
| v2 | breakout_8 + volume_26 | 9319.91 | -680.09 | sell / filled / 직전 완료 봉 목표 비중 0%; 다음 봉 시가 가정 |
| v2 | reversion_12 AND volume_26 | 9528.36 | -471.64 | sell / filled / 직전 완료 봉 목표 비중 0%; 다음 봉 시가 가정 |
| v2 | reversion_12 + volume_26 | 9097.48 | -902.52 | sell / filled / 직전 완료 봉 목표 비중 0%; 다음 봉 시가 가정 |
| v2 | ema_12_26 | 9444.94 | -555.06 | buy / partial / EMA12 > EMA26; 조건 충족; EMA12=524.345, EMA26=524.284; 직전 완료 봉 목표를 다음 봉 시가에 모의 적용 |
| v2 | macd_12_26_9 | 9554.99 | -445.01 | buy / partial / MACD > 신호선 그리고 MACD > 0; 조건 충족; MACD=0.0602049, signal9=-0.410679; 직전 완료 봉 목표를 다음 봉 시가에 모의 적용 |
| v2 | rsi_14_recovery | 9825.89 | -174.11 | sell / filled / 직전 RSI14 < 30, 현재 RSI14 >= 30 (한 봉 목표); 조건 미충족; RSI14=49.0008, previous_RSI14=38.029; 직전 완료 봉 목표를 다음 봉 시가에 모의 적용 |
| v2 | bollinger_20_reentry | 9732.18 | -267.82 | sell / filled / 직전 종가 < 직전 하단밴드, 현재 하단밴드 <= 종가 <= SMA20 (한 봉 목표); 조건 미충족; close=523.535, lower20=518.78, SMA20=523.154, previous_lower20=518.792; 직전 완료 봉 목표를 다음 봉 시가에 모의 적용 |
| v2 | donchian_20 | 9908.19 | -91.81 | sell / filled / 종가 > 현재 봉을 제외한 직전 20봉 최고가; 조건 미충족; close=534.52, prior_high20=535.44; 직전 완료 봉 목표를 다음 봉 시가에 모의 적용 |
| v2 | atr_14_breakout | 9911.14 | -88.86 | sell / filled / 종가 > 직전 종가 + 직전 ATR14 그리고 종가 > EMA26; 조건 미충족; close=533.975, threshold=536.307, prior_ATR14=2.16203, EMA26=530.521; 직전 완료 봉 목표를 다음 봉 시가에 모의 적용 |
| v2 | session_vwap | 9614.41 | -385.59 | buy / partial / 종가 > 뉴욕 거래일별 누적 전형가격 VWAP; 조건 충족; close=520.51, session_VWAP=518.805, session_volume=2.29852e+06; 직전 완료 봉 목표를 다음 봉 시가에 모의 적용 |
| v2 | obv_20 | 9456.10 | -543.90 | sell / filled / OBV > OBV의 SMA20 그리고 종가 > EMA26; 조건 미충족; OBV=3.70404e+07, OBV_SMA20=4.23196e+07, close=524.11, EMA26=524.113; 직전 완료 봉 목표를 다음 봉 시가에 모의 적용 |
| v2 | stochastic_14_3_recovery | 9622.24 | -377.76 | sell / filled / 직전 %K14 < 20에서 %K14가 %D3 상향 돌파 (한 봉 목표); 조건 미충족; K14=18.1724, D3=16.7161, previous_K14=21.0531, previous_D3=14.2045; 직전 완료 봉 목표를 다음 봉 시가에 모의 적용 |
| v2 | mfi_14_recovery | 9872.83 | -127.17 | sell / filled / 직전 MFI14 < 20, 현재 MFI14 >= 20 (한 봉 목표); 조건 미충족; MFI14=28.323, previous_MFI14=32.1727; 직전 완료 봉 목표를 다음 봉 시가에 모의 적용 |
| v2 | adx_14_trend | 9879.67 | -120.33 | sell / filled / Wilder ADX14 >= 25 그리고 +DI14 > -DI14; 조건 미충족; ADX14=23.6824, plus_DI14=22.3066, minus_DI14=19.9214; 직전 완료 봉 목표를 다음 봉 시가에 모의 적용 |
| v2 | aroon_25_trend | 9608.91 | -391.09 | sell / filled / Aroon25 Up > 70 그리고 Down < 30 (동률이면 최신 극값); 조건 미충족; Aroon_up=96, Aroon_down=100; 직전 완료 봉 목표를 다음 봉 시가에 모의 적용 |
| v2 | cci_20_momentum | 9862.73 | -137.27 | sell / filled / CCI20 > 100 (전형가격·평균절대편차); 조건 미충족; CCI20=99.2896; 직전 완료 봉 목표를 다음 봉 시가에 모의 적용 |
| v2 | williams_14_recovery | 9602.71 | -397.29 | sell / filled / 직전 Williams %R14 < -80, 현재 >= -80 (한 봉 목표); 조건 미충족; Williams_R14=-12.9449, previous_R14=-50.616; 직전 완료 봉 목표를 다음 봉 시가에 모의 적용 |
| v2 | cmf_20_accumulation | 9558.05 | -441.95 | sell / filled / Chaikin Money Flow20 > 0.1; 조건 미충족; CMF20=-0.143516, volume20=1.68966e+07; 직전 완료 봉 목표를 다음 봉 시가에 모의 적용 |
| v2 | chaikin_3_10 | 9495.62 | -504.38 | sell / filled / ADL의 EMA3 - EMA10 > 0 그리고 종가 > EMA26; 조건 미충족; Chaikin3_10=-1.26329e+06, ADL=9.19087e+07, close=524.11, EMA26=524.113; 직전 완료 봉 목표를 다음 봉 시가에 모의 적용 |
| v2 | roc_10_momentum | 9908.71 | -91.29 | sell / filled / 10봉 ROC > 1% 그리고 종가 > EMA26; 조건 미충족; ROC10_percent=0.691625, close=524.11, EMA26=524.113; 직전 완료 봉 목표를 다음 봉 시가에 모의 적용 |
| v2 | trix_15_trend | 9549.45 | -450.55 | sell / filled / 15봉 삼중 EMA의 1봉 변화율 TRIX > 0 그리고 종가 > EMA26; 조건 미충족; TRIX15_percent=0.00481299, close=529.54, EMA26=531.788; 직전 완료 봉 목표를 다음 봉 시가에 모의 적용 |
| v2 | keltner_20_breakout | 9956.78 | -43.22 | sell / filled / 종가 > EMA20 + 2 x Wilder ATR14; 조건 미충족; close=533.975, upper_Keltner=534.357, EMA20=530.111, ATR14=2.12332; 직전 완료 봉 목표를 다음 봉 시가에 모의 적용 |
| v2 | opening_range_30m | 9593.20 | -406.80 | buy / partial / 뉴욕 09:30·09:45 두 완료 봉 최고가를 10:00 이후 종가가 돌파; 조건 충족; close=523.535, opening_high=522.36; 직전 완료 봉 목표를 다음 봉 시가에 모의 적용 |

### 같은 기간의 비용·노출 비교 (사후 연구)

| 전략 | 비용 전 | 비용 후 | 100% 보유 | 같은 평균 노출 보유 | 평균 노출 |
|---|---:|---:|---:|---:|---:|
| cash | 0.00% | 0.00% | -1.01% | -0.00% | 0.00% |
| buy_hold | -0.60% | -1.01% | -1.01% | -1.01% | 100.00% |
| trend_8_26 | -3.09% | -6.69% | -1.01% | -0.57% | 56.81% |
| momentum_26 | -2.40% | -9.51% | -1.01% | -0.55% | 54.71% |
| breakout_8 | 3.75% | -10.06% | -1.01% | -0.19% | 18.85% |
| reversion_12 | -5.57% | -14.62% | -1.01% | -0.27% | 26.44% |
| volume_26 | -0.49% | -9.28% | -1.01% | -0.09% | 8.64% |
| trend_8_26 AND momentum_26 | -2.61% | -8.94% | -1.01% | -0.50% | 49.48% |
| trend_8_26 + momentum_26 | -2.75% | -7.72% | -1.01% | -0.56% | 55.76% |
| trend_8_26 AND breakout_8 | -1.14% | -10.62% | -1.01% | -0.11% | 11.26% |
| trend_8_26 + breakout_8 | 0.28% | -7.81% | -1.01% | -0.38% | 37.83% |
| trend_8_26 AND reversion_12 | -2.30% | -8.26% | -1.01% | -0.07% | 7.33% |
| trend_8_26 + reversion_12 | -4.33% | -10.56% | -1.01% | -0.42% | 41.63% |
| trend_8_26 AND volume_26 | 0.67% | -2.66% | -1.01% | -0.03% | 2.62% |
| trend_8_26 + volume_26 | -1.79% | -7.61% | -1.01% | -0.33% | 32.73% |
| momentum_26 AND breakout_8 | -0.01% | -9.98% | -1.01% | -0.12% | 12.04% |
| momentum_26 + breakout_8 | 0.64% | -9.40% | -1.01% | -0.37% | 36.79% |
| momentum_26 AND reversion_12 | -2.99% | -8.53% | -1.01% | -0.08% | 8.12% |
| momentum_26 + reversion_12 | -3.99% | -11.55% | -1.01% | -0.41% | 40.58% |
| momentum_26 AND volume_26 | -0.33% | -4.03% | -1.01% | -0.03% | 2.88% |
| momentum_26 + volume_26 | -1.44% | -8.63% | -1.01% | -0.32% | 31.68% |
| breakout_8 AND reversion_12 | 0.00% | 0.00% | -1.01% | -0.00% | 0.00% |
| breakout_8 + reversion_12 | -1.00% | -11.64% | -1.01% | -0.23% | 22.65% |
| breakout_8 AND volume_26 | 0.08% | -1.59% | -1.01% | -0.01% | 1.31% |
| breakout_8 + volume_26 | 1.61% | -8.91% | -1.01% | -0.14% | 13.75% |
| reversion_12 AND volume_26 | -2.53% | -6.53% | -1.01% | -0.04% | 3.93% |
| reversion_12 + volume_26 | -3.05% | -11.81% | -1.01% | -0.18% | 17.54% |
| ema_12_26 | -2.75% | -5.96% | -1.01% | -0.56% | 55.50% |
| macd_12_26_9 | -2.82% | -7.98% | -1.01% | -0.33% | 32.98% |
| rsi_14_recovery | 0.73% | -3.42% | -1.01% | -0.03% | 2.62% |
| bollinger_20_reentry | -0.23% | -4.34% | -1.01% | -0.03% | 2.62% |
| donchian_20 | -0.08% | -4.60% | -1.01% | -0.03% | 3.40% |
| atr_14_breakout | 0.48% | -3.25% | -1.01% | -0.02% | 2.36% |
| session_vwap | 4.27% | -4.53% | -1.01% | -0.52% | 51.05% |
| obv_20 | 2.72% | -5.16% | -1.01% | -0.50% | 49.21% |
| stochastic_14_3_recovery | -0.05% | -9.25% | -1.01% | -0.06% | 6.02% |
| mfi_14_recovery | 1.71% | -2.47% | -1.01% | -0.03% | 2.62% |
| adx_14_trend | 4.03% | 1.87% | -1.01% | -0.44% | 43.46% |
| aroon_25_trend | -1.57% | -6.01% | -1.01% | -0.22% | 22.25% |
| cci_20_momentum | 1.81% | -4.41% | -1.01% | -0.20% | 20.16% |
| williams_14_recovery | -0.66% | -9.04% | -1.01% | -0.06% | 5.50% |
| cmf_20_accumulation | -0.55% | -7.41% | -1.01% | -0.44% | 43.98% |
| chaikin_3_10 | 1.12% | -7.03% | -1.01% | -0.50% | 49.48% |
| roc_10_momentum | 0.13% | -3.99% | -1.01% | -0.13% | 13.09% |
| trix_15_trend | -0.36% | -4.05% | -1.01% | -0.44% | 43.19% |
| keltner_20_breakout | -0.58% | -5.47% | -1.01% | -0.11% | 10.99% |
| opening_range_30m | -1.06% | -5.13% | -1.01% | -0.25% | 25.13% |

동일 구간·초기 자금, 종료 시 청산 비용 포함. 노출 맞춤은 사후 설명용이며 v2 실제 계좌 성과가 아닙니다.
[낙폭 분해·비용 영향·전체 구간](MSFT/comparison.json)

[v1 전체 기록](MSFT/accounts.json) · [v2 전체 기록](MSFT/accounts-v2.json)

## JPM 계좌

| 모델 | 전략 | 평가액 USD | 손익 USD | 최근 매매·이유 |
|---|---|---:|---:|---|
| v1 | cash | 10000.00 | 0.00 | 대기 /  / 새 신호 대기 |
| v1 | buy_hold | 9754.54 | -245.46 | buy /  / buy_hold: prior completed bar target 100%; next bar open simulation |
| v1 | trend_8_26 | 9572.38 | -427.62 | sell /  / trend_8_26: prior completed bar target 0%; next bar open simulation |
| v1 | momentum_26 | 9183.69 | -816.31 | sell /  / momentum_26: prior completed bar target 0%; next bar open simulation |
| v1 | breakout_8 | 9398.30 | -601.70 | buy /  / breakout_8: prior completed bar target 100%; next bar open simulation |
| v1 | reversion_12 | 9476.27 | -523.73 | sell /  / reversion_12: prior completed bar target 0%; next bar open simulation |
| v1 | volume_26 | 9846.15 | -153.85 | sell /  / volume_26: prior completed bar target 0%; next bar open simulation |
| v1 | trend_8_26 AND momentum_26 | 9441.00 | -559.00 | sell /  / trend_8_26 AND momentum_26: prior completed bar target 0%; next bar open simulation |
| v1 | trend_8_26 + momentum_26 | 9376.17 | -623.83 | sell /  / trend_8_26 + momentum_26: prior completed bar target 0%; next bar open simulation |
| v1 | trend_8_26 AND breakout_8 | 9638.65 | -361.35 | sell /  / trend_8_26 AND breakout_8: prior completed bar target 0%; next bar open simulation |
| v1 | trend_8_26 + breakout_8 | 9522.98 | -477.02 | buy /  / trend_8_26 + breakout_8: prior completed bar target 50%; next bar open simulation |
| v1 | trend_8_26 AND reversion_12 | 9687.22 | -312.78 | sell /  / trend_8_26 AND reversion_12: prior completed bar target 0%; next bar open simulation |
| v1 | trend_8_26 + reversion_12 | 9524.04 | -475.96 | sell /  / trend_8_26 + reversion_12: prior completed bar target 0%; next bar open simulation |
| v1 | trend_8_26 AND volume_26 | 10027.62 | 27.62 | sell /  / trend_8_26 AND volume_26: prior completed bar target 0%; next bar open simulation |
| v1 | trend_8_26 + volume_26 | 9708.16 | -291.84 | sell /  / trend_8_26 + volume_26: prior completed bar target 0%; next bar open simulation |
| v1 | momentum_26 AND breakout_8 | 9431.18 | -568.82 | sell /  / momentum_26 AND breakout_8: prior completed bar target 0%; next bar open simulation |
| v1 | momentum_26 + breakout_8 | 9290.48 | -709.52 | buy /  / momentum_26 + breakout_8: prior completed bar target 50%; next bar open simulation |
| v1 | momentum_26 AND reversion_12 | 9788.16 | -211.84 | sell /  / momentum_26 AND reversion_12: prior completed bar target 0%; next bar open simulation |
| v1 | momentum_26 + reversion_12 | 9441.24 | -558.76 | sell /  / momentum_26 + reversion_12: prior completed bar target 0%; next bar open simulation |
| v1 | momentum_26 AND volume_26 | 9871.31 | -128.69 | sell /  / momentum_26 AND volume_26: prior completed bar target 0%; next bar open simulation |
| v1 | momentum_26 + volume_26 | 9547.21 | -452.79 | sell /  / momentum_26 + volume_26: prior completed bar target 0%; next bar open simulation |
| v1 | breakout_8 AND reversion_12 | 10000.00 | 0.00 | 대기 /  / 새 신호 대기 |
| v1 | breakout_8 + reversion_12 | 9493.72 | -506.28 | buy /  / breakout_8 + reversion_12: prior completed bar target 50%; next bar open simulation |
| v1 | breakout_8 AND volume_26 | 9998.31 | -1.69 | sell /  / breakout_8 AND volume_26: prior completed bar target 0%; next bar open simulation |
| v1 | breakout_8 + volume_26 | 9638.85 | -361.15 | buy /  / breakout_8 + volume_26: prior completed bar target 50%; next bar open simulation |
| v1 | reversion_12 AND volume_26 | 9881.36 | -118.64 | sell /  / reversion_12 AND volume_26: prior completed bar target 0%; next bar open simulation |
| v1 | reversion_12 + volume_26 | 9697.96 | -302.04 | sell /  / reversion_12 + volume_26: prior completed bar target 0%; next bar open simulation |
| v1 | ema_12_26 | 9456.51 | -543.49 | sell /  / EMA12 > EMA26; 조건 미충족; EMA12=334.326, EMA26=334.511 |
| v1 | macd_12_26_9 | 9556.03 | -443.97 | sell /  / MACD > 신호선 그리고 MACD > 0; 조건 미충족; MACD=0.0530109, signal9=0.111707 |
| v1 | rsi_14_recovery | 9986.37 | -13.63 | sell /  / 직전 RSI14 < 30, 현재 RSI14 >= 30 (한 봉 목표); 조건 미충족; RSI14=61.6663, previous_RSI14=57.046 |
| v1 | bollinger_20_reentry | 9835.47 | -164.53 | sell /  / 직전 종가 < 직전 하단밴드, 현재 하단밴드 <= 종가 <= SMA20 (한 봉 목표); 조건 미충족; close=332.25, lower20=330.876, SMA20=334.012, previous_lower20=331.095 |
| v1 | donchian_20 | 9663.29 | -336.71 | sell /  / 종가 > 현재 봉을 제외한 직전 20봉 최고가; 조건 미충족; close=332.6, prior_high20=336.61 |
| v1 | atr_14_breakout | 9637.39 | -362.61 | sell /  / 종가 > 직전 종가 + 직전 ATR14 그리고 종가 > EMA26; 조건 미충족; close=332.6, threshold=337.371, prior_ATR14=0.861165, EMA26=334.725 |
| v1 | session_vwap | 9428.20 | -571.80 | buy /  / 종가 > 뉴욕 거래일별 누적 전형가격 VWAP; 조건 충족; close=332.145, session_VWAP=331.988, session_volume=2.34495e+06 |
| v1 | obv_20 | 9551.60 | -448.40 | sell /  / OBV > OBV의 SMA20 그리고 종가 > EMA26; 조건 미충족; OBV=-1.95307e+07, OBV_SMA20=-1.97351e+07, close=332.6, EMA26=334.725 |
| v1 | stochastic_14_3_recovery | 9544.29 | -455.71 | sell /  / 직전 %K14 < 20에서 %K14가 %D3 상향 돌파 (한 봉 목표); 조건 미충족; K14=45.6055, D3=25.3586, previous_K14=22.8521, previous_D3=15.2809 |
| v1 | mfi_14_recovery | 9935.64 | -64.36 | sell /  / 직전 MFI14 < 20, 현재 MFI14 >= 20 (한 봉 목표); 조건 미충족; MFI14=30.2719, previous_MFI14=26.8492 |
| v1 | adx_14_trend | 9726.68 | -273.32 | sell /  / Wilder ADX14 >= 25 그리고 +DI14 > -DI14; 조건 미충족; ADX14=23.9395, plus_DI14=23.2021, minus_DI14=22.594 |
| v1 | aroon_25_trend | 9769.62 | -230.38 | sell /  / Aroon25 Up > 70 그리고 Down < 30 (동률이면 최신 극값); 조건 미충족; Aroon_up=96, Aroon_down=100 |
| v1 | cci_20_momentum | 9681.01 | -318.99 | sell /  / CCI20 > 100 (전형가격·평균절대편차); 조건 미충족; CCI20=-280.713 |
| v1 | williams_14_recovery | 9516.15 | -483.85 | sell /  / 직전 Williams %R14 < -80, 현재 >= -80 (한 봉 목표); 조건 미충족; Williams_R14=-54.3945, previous_R14=-77.1479 |
| v1 | cmf_20_accumulation | 9675.38 | -324.62 | buy /  / Chaikin Money Flow20 > 0.1; 조건 충족; CMF20=0.106552, volume20=1.86088e+06 |
| v1 | chaikin_3_10 | 9553.87 | -446.13 | sell /  / ADL의 EMA3 - EMA10 > 0 그리고 종가 > EMA26; 조건 미충족; Chaikin3_10=268702, ADL=-8.90187e+06, close=332.6, EMA26=334.725 |
| v1 | roc_10_momentum | 9836.40 | -163.60 | sell /  / 10봉 ROC > 1% 그리고 종가 > EMA26; 조건 미충족; ROC10_percent=0.964142, close=337.72, EMA26=336.695 |
| v1 | trix_15_trend | 9614.50 | -385.50 | sell /  / 15봉 삼중 EMA의 1봉 변화율 TRIX > 0 그리고 종가 > EMA26; 조건 미충족; TRIX15_percent=0.00517218, close=332.6, EMA26=334.725 |
| v1 | keltner_20_breakout | 9905.24 | -94.76 | sell /  / 종가 > EMA20 + 2 x Wilder ATR14; 조건 미충족; close=339.04, upper_Keltner=339.281, EMA20=336.559, ATR14=1.36146 |
| v1 | opening_range_30m | 9795.03 | -204.97 | sell /  / 뉴욕 09:30·09:45 두 완료 봉 최고가를 10:00 이후 종가가 돌파; 자료 부족·변동폭 또는 거래량 없음: 대기; close=332.6 |
| v2 | cash | 10000.00 | 0.00 | 대기 /  / 새 신호 대기 |
| v2 | buy_hold | 9917.54 | -82.46 | buy / partial / 직전 완료 봉 목표 비중 100%; 다음 봉 시가 가정 |
| v2 | trend_8_26 | 9573.52 | -426.48 | sell / filled / 직전 완료 봉 목표 비중 0%; 다음 봉 시가 가정 |
| v2 | momentum_26 | 9065.26 | -934.74 | 중단: 손실 한도 / buy / partial / 직전 완료 봉 목표 비중 100%; 다음 봉 시가 가정 |
| v2 | breakout_8 | 8935.14 | -1064.86 | 중단: 손실 한도 / buy / partial / 직전 완료 봉 목표 비중 100%; 다음 봉 시가 가정 |
| v2 | reversion_12 | 9438.41 | -561.59 | sell / filled / 직전 완료 봉 목표 비중 0%; 다음 봉 시가 가정 |
| v2 | volume_26 | 9661.98 | -338.02 | sell / filled / 직전 완료 봉 목표 비중 0%; 다음 봉 시가 가정 |
| v2 | trend_8_26 AND momentum_26 | 9395.85 | -604.15 | sell / filled / 직전 완료 봉 목표 비중 0%; 다음 봉 시가 가정 |
| v2 | trend_8_26 + momentum_26 | 9150.71 | -849.29 | sell / filled / 직전 완료 봉 목표 비중 0%; 다음 봉 시가 가정 |
| v2 | trend_8_26 AND breakout_8 | 9019.37 | -980.63 | sell / filled / 직전 완료 봉 목표 비중 0%; 다음 봉 시가 가정 |
| v2 | trend_8_26 + breakout_8 | 9192.16 | -807.84 | buy / filled / 직전 완료 봉 목표 비중 50%; 다음 봉 시가 가정 |
| v2 | trend_8_26 AND reversion_12 | 9657.80 | -342.20 | sell / filled / 직전 완료 봉 목표 비중 0%; 다음 봉 시가 가정 |
| v2 | trend_8_26 + reversion_12 | 9545.74 | -454.26 | sell / filled / 직전 완료 봉 목표 비중 0%; 다음 봉 시가 가정 |
| v2 | trend_8_26 AND volume_26 | 9821.47 | -178.53 | sell / filled / 직전 완료 봉 목표 비중 0%; 다음 봉 시가 가정 |
| v2 | trend_8_26 + volume_26 | 9618.29 | -381.71 | sell / filled / 직전 완료 봉 목표 비중 0%; 다음 봉 시가 가정 |
| v2 | momentum_26 AND breakout_8 | 8887.63 | -1112.37 | 중단: 손실 한도 / buy / partial / 직전 완료 봉 목표 비중 100%; 다음 봉 시가 가정 |
| v2 | momentum_26 + breakout_8 | 8995.36 | -1004.64 | 중단: 손실 한도 / sell / filled / 직전 완료 봉 목표 비중 0%; 다음 봉 시가 가정 |
| v2 | momentum_26 AND reversion_12 | 9730.22 | -269.78 | sell / filled / 직전 완료 봉 목표 비중 0%; 다음 봉 시가 가정 |
| v2 | momentum_26 + reversion_12 | 9297.88 | -702.12 | sell / filled / 직전 완료 봉 목표 비중 0%; 다음 봉 시가 가정 |
| v2 | momentum_26 AND volume_26 | 9668.38 | -331.62 | sell / filled / 직전 완료 봉 목표 비중 0%; 다음 봉 시가 가정 |
| v2 | momentum_26 + volume_26 | 9270.91 | -729.09 | sell / filled / 직전 완료 봉 목표 비중 0%; 다음 봉 시가 가정 |
| v2 | breakout_8 AND reversion_12 | 10000.00 | 0.00 | 대기 /  / 새 신호 대기 |
| v2 | breakout_8 + reversion_12 | 9183.62 | -816.38 | buy / filled / 직전 완료 봉 목표 비중 50%; 다음 봉 시가 가정 |
| v2 | breakout_8 AND volume_26 | 9883.76 | -116.24 | sell / filled / 직전 완료 봉 목표 비중 0%; 다음 봉 시가 가정 |
| v2 | breakout_8 + volume_26 | 9233.59 | -766.41 | buy / filled / 직전 완료 봉 목표 비중 50%; 다음 봉 시가 가정 |
| v2 | reversion_12 AND volume_26 | 9926.17 | -73.83 | sell / filled / 직전 완료 봉 목표 비중 0%; 다음 봉 시가 가정 |
| v2 | reversion_12 + volume_26 | 9609.94 | -390.06 | sell / filled / 직전 완료 봉 목표 비중 0%; 다음 봉 시가 가정 |
| v2 | ema_12_26 | 9447.06 | -552.94 | sell / filled / EMA12 > EMA26; 조건 미충족; EMA12=334.326, EMA26=334.511; 직전 완료 봉 목표를 다음 봉 시가에 모의 적용 |
| v2 | macd_12_26_9 | 9546.47 | -453.53 | sell / filled / MACD > 신호선 그리고 MACD > 0; 조건 미충족; MACD=0.0530109, signal9=0.111707; 직전 완료 봉 목표를 다음 봉 시가에 모의 적용 |
| v2 | rsi_14_recovery | 9984.37 | -15.63 | sell / filled / 직전 RSI14 < 30, 현재 RSI14 >= 30 (한 봉 목표); 조건 미충족; RSI14=61.6663, previous_RSI14=57.046; 직전 완료 봉 목표를 다음 봉 시가에 모의 적용 |
| v2 | bollinger_20_reentry | 9825.64 | -174.36 | sell / filled / 직전 종가 < 직전 하단밴드, 현재 하단밴드 <= 종가 <= SMA20 (한 봉 목표); 조건 미충족; close=332.25, lower20=330.876, SMA20=334.012, previous_lower20=331.095; 직전 완료 봉 목표를 다음 봉 시가에 모의 적용 |
| v2 | donchian_20 | 9653.63 | -346.37 | sell / filled / 종가 > 현재 봉을 제외한 직전 20봉 최고가; 조건 미충족; close=332.6, prior_high20=336.61; 직전 완료 봉 목표를 다음 봉 시가에 모의 적용 |
| v2 | atr_14_breakout | 9621.98 | -378.02 | sell / filled / 종가 > 직전 종가 + 직전 ATR14 그리고 종가 > EMA26; 조건 미충족; close=332.6, threshold=337.371, prior_ATR14=0.861165, EMA26=334.725; 직전 완료 봉 목표를 다음 봉 시가에 모의 적용 |
| v2 | session_vwap | 9408.42 | -591.58 | buy / partial / 종가 > 뉴욕 거래일별 누적 전형가격 VWAP; 조건 충족; close=332.145, session_VWAP=331.988, session_volume=2.34495e+06; 직전 완료 봉 목표를 다음 봉 시가에 모의 적용 |
| v2 | obv_20 | 9532.52 | -467.48 | sell / filled / OBV > OBV의 SMA20 그리고 종가 > EMA26; 조건 미충족; OBV=-1.95307e+07, OBV_SMA20=-1.97351e+07, close=332.6, EMA26=334.725; 직전 완료 봉 목표를 다음 봉 시가에 모의 적용 |
| v2 | stochastic_14_3_recovery | 9517.60 | -482.40 | sell / filled / 직전 %K14 < 20에서 %K14가 %D3 상향 돌파 (한 봉 목표); 조건 미충족; K14=45.6055, D3=25.3586, previous_K14=22.8521, previous_D3=15.2809; 직전 완료 봉 목표를 다음 봉 시가에 모의 적용 |
| v2 | mfi_14_recovery | 9931.66 | -68.34 | sell / filled / 직전 MFI14 < 20, 현재 MFI14 >= 20 (한 봉 목표); 조건 미충족; MFI14=30.2719, previous_MFI14=26.8492; 직전 완료 봉 목표를 다음 봉 시가에 모의 적용 |
| v2 | adx_14_trend | 9722.79 | -277.21 | sell / filled / Wilder ADX14 >= 25 그리고 +DI14 > -DI14; 조건 미충족; ADX14=23.9395, plus_DI14=23.2021, minus_DI14=22.594; 직전 완료 봉 목표를 다음 봉 시가에 모의 적용 |
| v2 | aroon_25_trend | 9765.71 | -234.29 | sell / filled / Aroon25 Up > 70 그리고 Down < 30 (동률이면 최신 극값); 조건 미충족; Aroon_up=96, Aroon_down=100; 직전 완료 봉 목표를 다음 봉 시가에 모의 적용 |
| v2 | cci_20_momentum | 9671.34 | -328.66 | sell / filled / CCI20 > 100 (전형가격·평균절대편차); 조건 미충족; CCI20=-280.713; 직전 완료 봉 목표를 다음 봉 시가에 모의 적용 |
| v2 | williams_14_recovery | 9491.44 | -508.56 | sell / filled / 직전 Williams %R14 < -80, 현재 >= -80 (한 봉 목표); 조건 미충족; Williams_R14=-54.3945, previous_R14=-77.1479; 직전 완료 봉 목표를 다음 봉 시가에 모의 적용 |
| v2 | cmf_20_accumulation | 9666.68 | -333.32 | buy / partial / Chaikin Money Flow20 > 0.1; 조건 충족; CMF20=0.106552, volume20=1.86088e+06; 직전 완료 봉 목표를 다음 봉 시가에 모의 적용 |
| v2 | chaikin_3_10 | 9536.68 | -463.32 | sell / filled / ADL의 EMA3 - EMA10 > 0 그리고 종가 > EMA26; 조건 미충족; Chaikin3_10=268702, ADL=-8.90187e+06, close=332.6, EMA26=334.725; 직전 완료 봉 목표를 다음 봉 시가에 모의 적용 |
| v2 | roc_10_momentum | 9832.47 | -167.53 | sell / filled / 10봉 ROC > 1% 그리고 종가 > EMA26; 조건 미충족; ROC10_percent=0.964142, close=337.72, EMA26=336.695; 직전 완료 봉 목표를 다음 봉 시가에 모의 적용 |
| v2 | trix_15_trend | 9604.89 | -395.11 | sell / filled / 15봉 삼중 EMA의 1봉 변화율 TRIX > 0 그리고 종가 > EMA26; 조건 미충족; TRIX15_percent=0.00517218, close=332.6, EMA26=334.725; 직전 완료 봉 목표를 다음 봉 시가에 모의 적용 |
| v2 | keltner_20_breakout | 9901.28 | -98.72 | sell / filled / 종가 > EMA20 + 2 x Wilder ATR14; 조건 미충족; close=339.04, upper_Keltner=339.281, EMA20=336.559, ATR14=1.36146; 직전 완료 봉 목표를 다음 봉 시가에 모의 적용 |
| v2 | opening_range_30m | 9789.16 | -210.84 | sell / filled / 뉴욕 09:30·09:45 두 완료 봉 최고가를 10:00 이후 종가가 돌파; 자료 부족·변동폭 또는 거래량 없음: 대기; close=332.6; 직전 완료 봉 목표를 다음 봉 시가에 모의 적용 |

### 같은 기간의 비용·노출 비교 (사후 연구)

| 전략 | 비용 전 | 비용 후 | 100% 보유 | 같은 평균 노출 보유 | 평균 노출 |
|---|---:|---:|---:|---:|---:|
| cash | 0.00% | 0.00% | -0.07% | -0.00% | 0.00% |
| buy_hold | 0.35% | -0.07% | -0.07% | -0.07% | 100.00% |
| trend_8_26 | -0.22% | -4.32% | -0.07% | -0.04% | 53.93% |
| momentum_26 | -4.62% | -13.76% | -0.07% | -0.04% | 52.88% |
| breakout_8 | -3.57% | -18.82% | -0.07% | -0.01% | 18.32% |
| reversion_12 | 6.51% | -8.44% | -0.07% | -0.02% | 24.61% |
| volume_26 | 1.66% | -4.54% | -0.07% | -0.00% | 6.28% |
| trend_8_26 AND momentum_26 | -0.41% | -6.49% | -0.07% | -0.03% | 41.36% |
| trend_8_26 + momentum_26 | -2.43% | -8.97% | -0.07% | -0.04% | 53.41% |
| trend_8_26 AND breakout_8 | -3.16% | -13.54% | -0.07% | -0.01% | 11.52% |
| trend_8_26 + breakout_8 | -1.89% | -11.30% | -0.07% | -0.03% | 36.13% |
| trend_8_26 AND reversion_12 | 1.62% | -4.98% | -0.07% | -0.01% | 8.12% |
| trend_8_26 + reversion_12 | 3.11% | -6.01% | -0.07% | -0.03% | 39.27% |
| trend_8_26 AND volume_26 | 0.99% | -2.35% | -0.07% | -0.00% | 3.93% |
| trend_8_26 + volume_26 | 0.74% | -4.43% | -0.07% | -0.02% | 30.11% |
| momentum_26 AND breakout_8 | -3.71% | -15.46% | -0.07% | -0.01% | 12.57% |
| momentum_26 + breakout_8 | -4.07% | -16.14% | -0.07% | -0.02% | 35.61% |
| momentum_26 AND reversion_12 | 1.94% | -4.68% | -0.07% | -0.00% | 6.54% |
| momentum_26 + reversion_12 | 0.82% | -8.68% | -0.07% | -0.03% | 38.75% |
| momentum_26 AND volume_26 | -0.68% | -3.96% | -0.07% | -0.00% | 3.14% |
| momentum_26 + volume_26 | -1.50% | -8.69% | -0.07% | -0.02% | 29.59% |
| breakout_8 AND reversion_12 | 0.00% | 0.00% | -0.07% | -0.00% | 0.00% |
| breakout_8 + reversion_12 | 1.37% | -12.51% | -0.07% | -0.02% | 21.48% |
| breakout_8 AND volume_26 | 0.94% | -1.16% | -0.07% | -0.00% | 1.31% |
| breakout_8 + volume_26 | -0.97% | -11.04% | -0.07% | -0.01% | 12.31% |
| reversion_12 AND volume_26 | 1.89% | -1.06% | -0.07% | -0.00% | 2.36% |
| reversion_12 + volume_26 | 4.07% | -5.53% | -0.07% | -0.01% | 15.45% |
| ema_12_26 | -1.48% | -5.53% | -0.07% | -0.04% | 50.52% |
| macd_12_26_9 | -1.42% | -6.66% | -0.07% | -0.02% | 32.46% |
| rsi_14_recovery | 0.40% | -0.86% | -0.07% | -0.00% | 0.79% |
| bollinger_20_reentry | 1.01% | -3.15% | -0.07% | -0.00% | 2.62% |
| donchian_20 | -2.16% | -5.78% | -0.07% | -0.00% | 3.14% |
| atr_14_breakout | -1.11% | -9.08% | -0.07% | -0.00% | 5.50% |
| session_vwap | 0.07% | -10.66% | -0.07% | -0.04% | 50.79% |
| obv_20 | -3.83% | -15.93% | -0.07% | -0.02% | 28.27% |
| stochastic_14_3_recovery | 0.40% | -9.99% | -0.07% | -0.00% | 6.81% |
| mfi_14_recovery | 0.12% | -1.13% | -0.07% | -0.00% | 0.79% |
| adx_14_trend | -2.34% | -4.37% | -0.07% | -0.02% | 24.87% |
| aroon_25_trend | -0.64% | -4.32% | -0.07% | -0.01% | 18.32% |
| cci_20_momentum | -3.21% | -11.38% | -0.07% | -0.01% | 16.49% |
| williams_14_recovery | -0.13% | -9.71% | -0.07% | -0.00% | 6.28% |
| cmf_20_accumulation | -2.65% | -9.74% | -0.07% | -0.03% | 36.65% |
| chaikin_3_10 | 1.13% | -8.18% | -0.07% | -0.02% | 33.77% |
| roc_10_momentum | -1.40% | -3.86% | -0.07% | -0.00% | 6.54% |
| trix_15_trend | -0.93% | -7.75% | -0.07% | -0.02% | 35.08% |
| keltner_20_breakout | -0.35% | -2.83% | -0.07% | -0.00% | 3.93% |
| opening_range_30m | -0.69% | -4.38% | -0.07% | -0.01% | 17.02% |

동일 구간·초기 자금, 종료 시 청산 비용 포함. 노출 맞춤은 사후 설명용이며 v2 실제 계좌 성과가 아닙니다.
[낙폭 분해·비용 영향·전체 구간](JPM/comparison.json)

[v1 전체 기록](JPM/accounts.json) · [v2 전체 기록](JPM/accounts-v2.json)

## XOM 계좌

| 모델 | 전략 | 평가액 USD | 손익 USD | 최근 매매·이유 |
|---|---|---:|---:|---|
| v1 | cash | 10000.00 | 0.00 | 대기 /  / 새 신호 대기 |
| v1 | buy_hold | 10308.01 | 308.01 | buy /  / buy_hold: prior completed bar target 100%; next bar open simulation |
| v1 | trend_8_26 | 9957.82 | -42.18 | buy /  / trend_8_26: prior completed bar target 100%; next bar open simulation |
| v1 | momentum_26 | 9951.56 | -48.44 | buy /  / momentum_26: prior completed bar target 100%; next bar open simulation |
| v1 | breakout_8 | 9481.80 | -518.20 | sell /  / breakout_8: prior completed bar target 0%; next bar open simulation |
| v1 | reversion_12 | 9517.47 | -482.53 | sell /  / reversion_12: prior completed bar target 0%; next bar open simulation |
| v1 | volume_26 | 9554.35 | -445.65 | sell /  / volume_26: prior completed bar target 0%; next bar open simulation |
| v1 | trend_8_26 AND momentum_26 | 9819.87 | -180.13 | buy /  / trend_8_26 AND momentum_26: prior completed bar target 100%; next bar open simulation |
| v1 | trend_8_26 + momentum_26 | 9954.96 | -45.04 | buy /  / trend_8_26 + momentum_26: prior completed bar target 100%; next bar open simulation |
| v1 | trend_8_26 AND breakout_8 | 9693.28 | -306.72 | sell /  / trend_8_26 AND breakout_8: prior completed bar target 0%; next bar open simulation |
| v1 | trend_8_26 + breakout_8 | 9756.51 | -243.49 | sell /  / trend_8_26 + breakout_8: prior completed bar target 50%; next bar open simulation |
| v1 | trend_8_26 AND reversion_12 | 9545.50 | -454.50 | sell /  / trend_8_26 AND reversion_12: prior completed bar target 0%; next bar open simulation |
| v1 | trend_8_26 + reversion_12 | 9735.28 | -264.72 | sell /  / trend_8_26 + reversion_12: prior completed bar target 50%; next bar open simulation |
| v1 | trend_8_26 AND volume_26 | 9669.14 | -330.86 | sell /  / trend_8_26 AND volume_26: prior completed bar target 0%; next bar open simulation |
| v1 | trend_8_26 + volume_26 | 9754.51 | -245.49 | sell /  / trend_8_26 + volume_26: prior completed bar target 50%; next bar open simulation |
| v1 | momentum_26 AND breakout_8 | 9813.21 | -186.79 | sell /  / momentum_26 AND breakout_8: prior completed bar target 0%; next bar open simulation |
| v1 | momentum_26 + breakout_8 | 9714.24 | -285.76 | sell /  / momentum_26 + breakout_8: prior completed bar target 50%; next bar open simulation |
| v1 | momentum_26 AND reversion_12 | 9642.75 | -357.25 | sell /  / momentum_26 AND reversion_12: prior completed bar target 0%; next bar open simulation |
| v1 | momentum_26 + reversion_12 | 9732.10 | -267.90 | sell /  / momentum_26 + reversion_12: prior completed bar target 50%; next bar open simulation |
| v1 | momentum_26 AND volume_26 | 9888.17 | -111.83 | sell /  / momentum_26 AND volume_26: prior completed bar target 0%; next bar open simulation |
| v1 | momentum_26 + volume_26 | 9751.12 | -248.88 | sell /  / momentum_26 + volume_26: prior completed bar target 50%; next bar open simulation |
| v1 | breakout_8 AND reversion_12 | 10000.00 | 0.00 | 대기 /  / 새 신호 대기 |
| v1 | breakout_8 + reversion_12 | 9518.57 | -481.43 | sell /  / breakout_8 + reversion_12: prior completed bar target 0%; next bar open simulation |
| v1 | breakout_8 AND volume_26 | 9896.24 | -103.76 | sell /  / breakout_8 AND volume_26: prior completed bar target 0%; next bar open simulation |
| v1 | breakout_8 + volume_26 | 9517.91 | -482.09 | sell /  / breakout_8 + volume_26: prior completed bar target 0%; next bar open simulation |
| v1 | reversion_12 AND volume_26 | 9794.27 | -205.73 | sell /  / reversion_12 AND volume_26: prior completed bar target 0%; next bar open simulation |
| v1 | reversion_12 + volume_26 | 9536.04 | -463.96 | sell /  / reversion_12 + volume_26: prior completed bar target 0%; next bar open simulation |
| v1 | ema_12_26 | 10026.29 | 26.29 | buy /  / EMA12 > EMA26; 조건 충족; EMA12=176.974, EMA26=176.95 |
| v1 | macd_12_26_9 | 10047.23 | 47.23 | sell /  / MACD > 신호선 그리고 MACD > 0; 조건 미충족; MACD=1.35319, signal9=1.41024 |
| v1 | rsi_14_recovery | 9927.64 | -72.36 | sell /  / 직전 RSI14 < 30, 현재 RSI14 >= 30 (한 봉 목표); 조건 미충족; RSI14=37.639, previous_RSI14=31.1023 |
| v1 | bollinger_20_reentry | 9694.21 | -305.79 | sell /  / 직전 종가 < 직전 하단밴드, 현재 하단밴드 <= 종가 <= SMA20 (한 봉 목표); 조건 미충족; close=175.53, lower20=174.782, SMA20=177.101, previous_lower20=174.994 |
| v1 | donchian_20 | 9754.38 | -245.62 | sell /  / 종가 > 현재 봉을 제외한 직전 20봉 최고가; 조건 미충족; close=183.28, prior_high20=183.3 |
| v1 | atr_14_breakout | 9789.04 | -210.96 | sell /  / 종가 > 직전 종가 + 직전 ATR14 그리고 종가 > EMA26; 조건 미충족; close=181.355, threshold=182.652, prior_ATR14=0.727068, EMA26=178.133 |
| v1 | session_vwap | 10014.25 | 14.25 | buy /  / 종가 > 뉴욕 거래일별 누적 전형가격 VWAP; 조건 충족; close=182.56, session_VWAP=182.496, session_volume=1.22728e+07 |
| v1 | obv_20 | 9530.96 | -469.04 | buy /  / OBV > OBV의 SMA20 그리고 종가 > EMA26; 조건 충족; OBV=2.26159e+07, OBV_SMA20=2.18428e+07, close=176.86, EMA26=176.75 |
| v1 | stochastic_14_3_recovery | 9636.26 | -363.74 | sell /  / 직전 %K14 < 20에서 %K14가 %D3 상향 돌파 (한 봉 목표); 조건 미충족; K14=11.8836, D3=5.65987, previous_K14=4.66302, previous_D3=2.02546 |
| v1 | mfi_14_recovery | 10000.00 | 0.00 | 대기 /  / 새 신호 대기 |
| v1 | adx_14_trend | 10029.85 | 29.85 | buy /  / Wilder ADX14 >= 25 그리고 +DI14 > -DI14; 조건 충족; ADX14=26.2258, plus_DI14=52.4409, minus_DI14=10.4732 |
| v1 | aroon_25_trend | 9626.27 | -373.73 | sell /  / Aroon25 Up > 70 그리고 Down < 30 (동률이면 최신 극값); 조건 미충족; Aroon_up=68, Aroon_down=4 |
| v1 | cci_20_momentum | 9460.38 | -539.62 | sell /  / CCI20 > 100 (전형가격·평균절대편차); 조건 미충족; CCI20=95.1299 |
| v1 | williams_14_recovery | 9643.01 | -356.99 | sell /  / 직전 Williams %R14 < -80, 현재 >= -80 (한 봉 목표); 조건 미충족; Williams_R14=-68.9948, previous_R14=-74.4719 |
| v1 | cmf_20_accumulation | 9926.68 | -73.32 | buy /  / Chaikin Money Flow20 > 0.1; 조건 충족; CMF20=0.202217, volume20=4.5047e+06 |
| v1 | chaikin_3_10 | 9888.78 | -111.22 | buy /  / ADL의 EMA3 - EMA10 > 0 그리고 종가 > EMA26; 조건 충족; Chaikin3_10=152048, ADL=2.84951e+07, close=176.86, EMA26=176.75 |
| v1 | roc_10_momentum | 9912.41 | -87.59 | sell /  / 10봉 ROC > 1% 그리고 종가 > EMA26; 조건 미충족; ROC10_percent=0.733814, close=183.26, EMA26=180.514 |
| v1 | trix_15_trend | 9976.32 | -23.68 | buy /  / 15봉 삼중 EMA의 1봉 변화율 TRIX > 0 그리고 종가 > EMA26; 조건 충족; TRIX15_percent=0.00288954, close=177.71, EMA26=177.21 |
| v1 | keltner_20_breakout | 9898.00 | -102.00 | sell /  / 종가 > EMA20 + 2 x Wilder ATR14; 조건 미충족; close=182.29, upper_Keltner=182.66, EMA20=181.48, ATR14=0.590087 |
| v1 | opening_range_30m | 9959.21 | -40.79 | buy /  / 뉴욕 09:30·09:45 두 완료 봉 최고가를 10:00 이후 종가가 돌파; 조건 충족; close=182.19, opening_high=181.96 |
| v2 | cash | 10000.00 | 0.00 | 대기 /  / 새 신호 대기 |
| v2 | buy_hold | 10636.97 | 636.97 | buy / partial / 직전 완료 봉 목표 비중 100%; 다음 봉 시가 가정 |
| v2 | trend_8_26 | 10044.62 | 44.62 | buy / partial / 직전 완료 봉 목표 비중 100%; 다음 봉 시가 가정 |
| v2 | momentum_26 | 10116.28 | 116.28 | buy / partial / 직전 완료 봉 목표 비중 100%; 다음 봉 시가 가정 |
| v2 | breakout_8 | 8988.95 | -1011.05 | 중단: 손실 한도 / sell / filled / 직전 완료 봉 목표 비중 0%; 다음 봉 시가 가정 |
| v2 | reversion_12 | 9330.25 | -669.75 | sell / filled / 직전 완료 봉 목표 비중 0%; 다음 봉 시가 가정 |
| v2 | volume_26 | 9451.35 | -548.65 | sell / filled / 직전 완료 봉 목표 비중 0%; 다음 봉 시가 가정 |
| v2 | trend_8_26 AND momentum_26 | 9910.83 | -89.17 | buy / partial / 직전 완료 봉 목표 비중 100%; 다음 봉 시가 가정 |
| v2 | trend_8_26 + momentum_26 | 10080.68 | 80.68 | buy / partial / 직전 완료 봉 목표 비중 100%; 다음 봉 시가 가정 |
| v2 | trend_8_26 AND breakout_8 | 9139.97 | -860.03 | sell / filled / 직전 완료 봉 목표 비중 0%; 다음 봉 시가 가정 |
| v2 | trend_8_26 + breakout_8 | 9540.40 | -459.60 | sell / filled / 직전 완료 봉 목표 비중 50%; 다음 봉 시가 가정 |
| v2 | trend_8_26 AND reversion_12 | 9381.23 | -618.77 | sell / filled / 직전 완료 봉 목표 비중 0%; 다음 봉 시가 가정 |
| v2 | trend_8_26 + reversion_12 | 9681.03 | -318.97 | sell / filled / 직전 완료 봉 목표 비중 50%; 다음 봉 시가 가정 |
| v2 | trend_8_26 AND volume_26 | 9556.73 | -443.27 | sell / filled / 직전 완료 봉 목표 비중 0%; 다음 봉 시가 가정 |
| v2 | trend_8_26 + volume_26 | 9743.91 | -256.09 | sell / filled / 직전 완료 봉 목표 비중 50%; 다음 봉 시가 가정 |
| v2 | momentum_26 AND breakout_8 | 9273.68 | -726.32 | sell / filled / 직전 완료 봉 목표 비중 0%; 다음 봉 시가 가정 |
| v2 | momentum_26 + breakout_8 | 9514.15 | -485.85 | sell / filled / 직전 완료 봉 목표 비중 50%; 다음 봉 시가 가정 |
| v2 | momentum_26 AND reversion_12 | 9440.57 | -559.43 | sell / filled / 직전 완료 봉 목표 비중 0%; 다음 봉 시가 가정 |
| v2 | momentum_26 + reversion_12 | 9715.40 | -284.60 | sell / filled / 직전 완료 봉 목표 비중 50%; 다음 봉 시가 가정 |
| v2 | momentum_26 AND volume_26 | 9838.73 | -161.27 | sell / filled / 직전 완료 봉 목표 비중 0%; 다음 봉 시가 가정 |
| v2 | momentum_26 + volume_26 | 9798.82 | -201.18 | sell / filled / 직전 완료 봉 목표 비중 50%; 다음 봉 시가 가정 |
| v2 | breakout_8 AND reversion_12 | 10000.00 | 0.00 | 대기 /  / 새 신호 대기 |
| v2 | breakout_8 + reversion_12 | 9155.19 | -844.81 | sell / filled / 직전 완료 봉 목표 비중 0%; 다음 봉 시가 가정 |
| v2 | breakout_8 AND volume_26 | 9860.88 | -139.12 | sell / filled / 직전 완료 봉 목표 비중 0%; 다음 봉 시가 가정 |
| v2 | breakout_8 + volume_26 | 9214.41 | -785.59 | sell / filled / 직전 완료 봉 목표 비중 0%; 다음 봉 시가 가정 |
| v2 | reversion_12 AND volume_26 | 9737.38 | -262.62 | sell / filled / 직전 완료 봉 목표 비중 0%; 다음 봉 시가 가정 |
| v2 | reversion_12 + volume_26 | 9410.50 | -589.50 | sell / filled / 직전 완료 봉 목표 비중 0%; 다음 봉 시가 가정 |
| v2 | ema_12_26 | 10019.27 | 19.27 | buy / partial / EMA12 > EMA26; 조건 충족; EMA12=176.974, EMA26=176.95; 직전 완료 봉 목표를 다음 봉 시가에 모의 적용 |
| v2 | macd_12_26_9 | 10035.18 | 35.18 | sell / filled / MACD > 신호선 그리고 MACD > 0; 조건 미충족; MACD=1.35319, signal9=1.41024; 직전 완료 봉 목표를 다음 봉 시가에 모의 적용 |
| v2 | rsi_14_recovery | 9923.67 | -76.33 | sell / filled / 직전 RSI14 < 30, 현재 RSI14 >= 30 (한 봉 목표); 조건 미충족; RSI14=37.639, previous_RSI14=31.1023; 직전 완료 봉 목표를 다음 봉 시가에 모의 적용 |
| v2 | bollinger_20_reentry | 9684.52 | -315.48 | sell / filled / 직전 종가 < 직전 하단밴드, 현재 하단밴드 <= 종가 <= SMA20 (한 봉 목표); 조건 미충족; close=175.53, lower20=174.782, SMA20=177.101, previous_lower20=174.994; 직전 완료 봉 목표를 다음 봉 시가에 모의 적용 |
| v2 | donchian_20 | 9738.78 | -261.22 | sell / filled / 종가 > 현재 봉을 제외한 직전 20봉 최고가; 조건 미충족; close=183.28, prior_high20=183.3; 직전 완료 봉 목표를 다음 봉 시가에 모의 적용 |
| v2 | atr_14_breakout | 9777.30 | -222.70 | sell / filled / 종가 > 직전 종가 + 직전 ATR14 그리고 종가 > EMA26; 조건 미충족; close=181.355, threshold=182.652, prior_ATR14=0.727068, EMA26=178.133; 직전 완료 봉 목표를 다음 봉 시가에 모의 적용 |
| v2 | session_vwap | 9997.24 | -2.76 | buy / partial / 종가 > 뉴욕 거래일별 누적 전형가격 VWAP; 조건 충족; close=182.56, session_VWAP=182.496, session_volume=1.22728e+07; 직전 완료 봉 목표를 다음 봉 시가에 모의 적용 |
| v2 | obv_20 | 9502.46 | -497.54 | 중단: 손실 한도 / sell / filled / OBV > OBV의 SMA20 그리고 종가 > EMA26; 조건 미충족; OBV=2.24329e+07, OBV_SMA20=2.30895e+07, close=177.005, EMA26=177.393; 직전 완료 봉 목표를 다음 봉 시가에 모의 적용 |
| v2 | stochastic_14_3_recovery | 9622.78 | -377.22 | sell / filled / 직전 %K14 < 20에서 %K14가 %D3 상향 돌파 (한 봉 목표); 조건 미충족; K14=11.8836, D3=5.65987, previous_K14=4.66302, previous_D3=2.02546; 직전 완료 봉 목표를 다음 봉 시가에 모의 적용 |
| v2 | mfi_14_recovery | 10000.00 | 0.00 | 대기 /  / 새 신호 대기 |
| v2 | adx_14_trend | 10022.83 | 22.83 | buy / partial / Wilder ADX14 >= 25 그리고 +DI14 > -DI14; 조건 충족; ADX14=26.2258, plus_DI14=52.4409, minus_DI14=10.4732; 직전 완료 봉 목표를 다음 봉 시가에 모의 적용 |
| v2 | aroon_25_trend | 9616.65 | -383.35 | sell / filled / Aroon25 Up > 70 그리고 Down < 30 (동률이면 최신 극값); 조건 미충족; Aroon_up=68, Aroon_down=4; 직전 완료 봉 목표를 다음 봉 시가에 모의 적용 |
| v2 | cci_20_momentum | 9435.81 | -564.19 | sell / filled / CCI20 > 100 (전형가격·평균절대편차); 조건 미충족; CCI20=95.1299; 직전 완료 봉 목표를 다음 봉 시가에 모의 적용 |
| v2 | williams_14_recovery | 9629.52 | -370.48 | sell / filled / 직전 Williams %R14 < -80, 현재 >= -80 (한 봉 목표); 조건 미충족; Williams_R14=-68.9948, previous_R14=-74.4719; 직전 완료 봉 목표를 다음 봉 시가에 모의 적용 |
| v2 | cmf_20_accumulation | 9913.78 | -86.22 | buy / partial / Chaikin Money Flow20 > 0.1; 조건 충족; CMF20=0.202217, volume20=4.5047e+06; 직전 완료 봉 목표를 다음 봉 시가에 모의 적용 |
| v2 | chaikin_3_10 | 9871.98 | -128.02 | buy / partial / ADL의 EMA3 - EMA10 > 0 그리고 종가 > EMA26; 조건 충족; Chaikin3_10=152048, ADL=2.87515e+07, close=176.86, EMA26=176.75; 직전 완료 봉 목표를 다음 봉 시가에 모의 적용 |
| v2 | roc_10_momentum | 9900.52 | -99.48 | sell / filled / 10봉 ROC > 1% 그리고 종가 > EMA26; 조건 미충족; ROC10_percent=0.733814, close=183.26, EMA26=180.514; 직전 완료 봉 목표를 다음 봉 시가에 모의 적용 |
| v2 | trix_15_trend | 9963.36 | -36.64 | buy / partial / 15봉 삼중 EMA의 1봉 변화율 TRIX > 0 그리고 종가 > EMA26; 조건 충족; TRIX15_percent=0.00288954, close=177.71, EMA26=177.21; 직전 완료 봉 목표를 다음 봉 시가에 모의 적용 |
| v2 | keltner_20_breakout | 9888.11 | -111.89 | sell / filled / 종가 > EMA20 + 2 x Wilder ATR14; 조건 미충족; close=182.29, upper_Keltner=182.66, EMA20=181.48, ATR14=0.590087; 직전 완료 봉 목표를 다음 봉 시가에 모의 적용 |
| v2 | opening_range_30m | 9954.23 | -45.77 | buy / partial / 뉴욕 09:30·09:45 두 완료 봉 최고가를 10:00 이후 종가가 돌파; 조건 충족; close=182.19, opening_high=181.96; 직전 완료 봉 목표를 다음 봉 시가에 모의 적용 |

### 같은 기간의 비용·노출 비교 (사후 연구)

| 전략 | 비용 전 | 비용 후 | 100% 보유 | 같은 평균 노출 보유 | 평균 노출 |
|---|---:|---:|---:|---:|---:|
| cash | 0.00% | 0.00% | 11.30% | 0.00% | 0.00% |
| buy_hold | 11.77% | 11.30% | 11.30% | 11.30% | 100.00% |
| trend_8_26 | 5.46% | 1.12% | 11.30% | 7.88% | 70.94% |
| momentum_26 | 5.43% | 0.67% | 11.30% | 7.67% | 69.11% |
| breakout_8 | 1.60% | -15.90% | 11.30% | 2.95% | 27.23% |
| reversion_12 | 1.03% | -8.65% | 11.30% | 2.35% | 21.73% |
| volume_26 | 1.18% | -6.19% | 11.30% | 0.59% | 5.50% |
| trend_8_26 AND momentum_26 | 3.76% | -0.92% | 11.30% | 6.77% | 61.26% |
| trend_8_26 + momentum_26 | 5.46% | 1.12% | 11.30% | 7.78% | 70.03% |
| trend_8_26 AND breakout_8 | 1.72% | -12.55% | 11.30% | 2.32% | 21.47% |
| trend_8_26 + breakout_8 | 3.53% | -7.18% | 11.30% | 5.39% | 49.09% |
| trend_8_26 AND reversion_12 | -1.86% | -7.85% | 11.30% | 1.15% | 10.73% |
| trend_8_26 + reversion_12 | 3.25% | -3.69% | 11.30% | 5.08% | 46.34% |
| trend_8_26 AND volume_26 | 0.50% | -4.44% | 11.30% | 0.39% | 3.66% |
| trend_8_26 + volume_26 | 3.32% | -2.40% | 11.30% | 4.17% | 38.22% |
| momentum_26 AND breakout_8 | 1.67% | -12.60% | 11.30% | 2.40% | 22.25% |
| momentum_26 + breakout_8 | 3.52% | -7.97% | 11.30% | 5.28% | 48.17% |
| momentum_26 AND reversion_12 | 0.09% | -7.20% | 11.30% | 1.15% | 10.73% |
| momentum_26 + reversion_12 | 3.24% | -3.70% | 11.30% | 4.97% | 45.42% |
| momentum_26 AND volume_26 | 1.74% | -2.03% | 11.30% | 0.25% | 2.36% |
| momentum_26 + volume_26 | 3.31% | -2.20% | 11.30% | 4.07% | 37.31% |
| breakout_8 AND reversion_12 | 0.00% | 0.00% | 11.30% | 0.00% | 0.00% |
| breakout_8 + reversion_12 | 1.34% | -11.98% | 11.30% | 2.65% | 24.49% |
| breakout_8 AND volume_26 | 0.76% | -1.75% | 11.30% | 0.17% | 1.57% |
| breakout_8 + volume_26 | 1.40% | -10.62% | 11.30% | 1.76% | 16.37% |
| reversion_12 AND volume_26 | -0.04% | -3.35% | 11.30% | 0.25% | 2.36% |
| reversion_12 + volume_26 | 1.12% | -6.84% | 11.30% | 1.46% | 13.62% |
| ema_12_26 | 5.25% | 2.21% | 11.30% | 8.40% | 75.39% |
| macd_12_26_9 | 3.85% | -2.08% | 11.30% | 4.64% | 42.41% |
| rsi_14_recovery | -0.08% | -1.33% | 11.30% | 0.08% | 0.79% |
| bollinger_20_reentry | -1.64% | -4.89% | 11.30% | 0.22% | 2.09% |
| donchian_20 | 0.04% | -8.41% | 11.30% | 1.12% | 10.47% |
| atr_14_breakout | 0.86% | -7.27% | 11.30% | 0.62% | 5.76% |
| session_vwap | 5.76% | -5.18% | 11.30% | 7.10% | 64.14% |
| obv_20 | 3.03% | -7.24% | 11.30% | 5.52% | 50.26% |
| stochastic_14_3_recovery | 0.05% | -9.54% | 11.30% | 0.67% | 6.28% |
| mfi_14_recovery | -0.31% | -1.97% | 11.30% | 0.11% | 1.05% |
| adx_14_trend | 3.85% | 0.84% | 11.30% | 4.70% | 42.93% |
| aroon_25_trend | -1.71% | -8.10% | 11.30% | 3.73% | 34.29% |
| cci_20_momentum | 2.35% | -7.47% | 11.30% | 3.21% | 29.58% |
| williams_14_recovery | -1.21% | -7.24% | 11.30% | 0.42% | 3.93% |
| cmf_20_accumulation | 3.86% | -2.48% | 11.30% | 5.70% | 51.83% |
| chaikin_3_10 | 6.10% | -2.85% | 11.30% | 6.74% | 60.99% |
| roc_10_momentum | 1.32% | -4.87% | 11.30% | 1.63% | 15.18% |
| trix_15_trend | 4.70% | -1.28% | 11.30% | 6.80% | 61.52% |
| keltner_20_breakout | 0.94% | -5.62% | 11.30% | 2.15% | 19.90% |
| opening_range_30m | 0.08% | -6.82% | 11.30% | 3.07% | 28.27% |

동일 구간·초기 자금, 종료 시 청산 비용 포함. 노출 맞춤은 사후 설명용이며 v2 실제 계좌 성과가 아닙니다.
[낙폭 분해·비용 영향·전체 구간](XOM/comparison.json)

[v1 전체 기록](XOM/accounts.json) · [v2 전체 기록](XOM/accounts-v2.json)

## JNJ 계좌

| 모델 | 전략 | 평가액 USD | 손익 USD | 최근 매매·이유 |
|---|---|---:|---:|---|
| v1 | cash | 10000.00 | 0.00 | 대기 /  / 새 신호 대기 |
| v1 | buy_hold | 10281.17 | 281.17 | buy /  / buy_hold: prior completed bar target 100%; next bar open simulation |
| v1 | trend_8_26 | 10203.47 | 203.47 | sell /  / trend_8_26: prior completed bar target 0%; next bar open simulation |
| v1 | momentum_26 | 9644.97 | -355.03 | sell /  / momentum_26: prior completed bar target 0%; next bar open simulation |
| v1 | breakout_8 | 9424.57 | -575.43 | sell /  / breakout_8: prior completed bar target 0%; next bar open simulation |
| v1 | reversion_12 | 9608.51 | -391.49 | sell /  / reversion_12: prior completed bar target 0%; next bar open simulation |
| v1 | volume_26 | 10040.58 | 40.58 | sell /  / volume_26: prior completed bar target 0%; next bar open simulation |
| v1 | trend_8_26 AND momentum_26 | 9811.53 | -188.47 | sell /  / trend_8_26 AND momentum_26: prior completed bar target 0%; next bar open simulation |
| v1 | trend_8_26 + momentum_26 | 9940.65 | -59.35 | sell /  / trend_8_26 + momentum_26: prior completed bar target 0%; next bar open simulation |
| v1 | trend_8_26 AND breakout_8 | 9864.21 | -135.79 | sell /  / trend_8_26 AND breakout_8: prior completed bar target 0%; next bar open simulation |
| v1 | trend_8_26 + breakout_8 | 9826.50 | -173.50 | sell /  / trend_8_26 + breakout_8: prior completed bar target 0%; next bar open simulation |
| v1 | trend_8_26 AND reversion_12 | 9807.21 | -192.79 | sell /  / trend_8_26 AND reversion_12: prior completed bar target 0%; next bar open simulation |
| v1 | trend_8_26 + reversion_12 | 9901.79 | -98.21 | sell /  / trend_8_26 + reversion_12: prior completed bar target 0%; next bar open simulation |
| v1 | trend_8_26 AND volume_26 | 10134.54 | 134.54 | sell /  / trend_8_26 AND volume_26: prior completed bar target 0%; next bar open simulation |
| v1 | trend_8_26 + volume_26 | 10122.01 | 122.01 | sell /  / trend_8_26 + volume_26: prior completed bar target 0%; next bar open simulation |
| v1 | momentum_26 AND breakout_8 | 9703.66 | -296.34 | sell /  / momentum_26 AND breakout_8: prior completed bar target 0%; next bar open simulation |
| v1 | momentum_26 + breakout_8 | 9534.48 | -465.52 | sell /  / momentum_26 + breakout_8: prior completed bar target 0%; next bar open simulation |
| v1 | momentum_26 AND reversion_12 | 9708.77 | -291.23 | sell /  / momentum_26 AND reversion_12: prior completed bar target 0%; next bar open simulation |
| v1 | momentum_26 + reversion_12 | 9665.24 | -334.76 | sell /  / momentum_26 + reversion_12: prior completed bar target 0%; next bar open simulation |
| v1 | momentum_26 AND volume_26 | 10000.00 | 0.00 | 대기 /  / 새 신호 대기 |
| v1 | momentum_26 + volume_26 | 9900.29 | -99.71 | sell /  / momentum_26 + volume_26: prior completed bar target 0%; next bar open simulation |
| v1 | breakout_8 AND reversion_12 | 10000.00 | 0.00 | 대기 /  / 새 신호 대기 |
| v1 | breakout_8 + reversion_12 | 9515.86 | -484.14 | sell /  / breakout_8 + reversion_12: prior completed bar target 0%; next bar open simulation |
| v1 | breakout_8 AND volume_26 | 10139.49 | 139.49 | sell /  / breakout_8 AND volume_26: prior completed bar target 0%; next bar open simulation |
| v1 | breakout_8 + volume_26 | 9747.06 | -252.94 | sell /  / breakout_8 + volume_26: prior completed bar target 0%; next bar open simulation |
| v1 | reversion_12 AND volume_26 | 9933.02 | -66.98 | sell /  / reversion_12 AND volume_26: prior completed bar target 0%; next bar open simulation |
| v1 | reversion_12 + volume_26 | 9841.98 | -158.02 | sell /  / reversion_12 + volume_26: prior completed bar target 0%; next bar open simulation |
| v1 | ema_12_26 | 9827.67 | -172.33 | sell /  / EMA12 > EMA26; 조건 미충족; EMA12=264.816, EMA26=264.953 |
| v1 | macd_12_26_9 | 10152.66 | 152.66 | sell /  / MACD > 신호선 그리고 MACD > 0; 조건 미충족; MACD=2.48372, signal9=2.49952 |
| v1 | rsi_14_recovery | 9923.04 | -76.96 | sell /  / 직전 RSI14 < 30, 현재 RSI14 >= 30 (한 봉 목표); 조건 미충족; RSI14=40.3665, previous_RSI14=36.2025 |
| v1 | bollinger_20_reentry | 9778.51 | -221.49 | sell /  / 직전 종가 < 직전 하단밴드, 현재 하단밴드 <= 종가 <= SMA20 (한 봉 목표); 조건 미충족; close=263.43, lower20=262.644, SMA20=266.981, previous_lower20=263.145 |
| v1 | donchian_20 | 9779.77 | -220.23 | sell /  / 종가 > 현재 봉을 제외한 직전 20봉 최고가; 조건 미충족; close=268.59, prior_high20=269.55 |
| v1 | atr_14_breakout | 9634.41 | -365.59 | sell /  / 종가 > 직전 종가 + 직전 ATR14 그리고 종가 > EMA26; 조건 미충족; close=269.05, threshold=269.858, prior_ATR14=0.907979, EMA26=264.623 |
| v1 | session_vwap | 9933.23 | -66.77 | sell /  / 종가 > 뉴욕 거래일별 누적 전형가격 VWAP; 조건 미충족; close=263.8, session_VWAP=264.478, session_volume=329302 |
| v1 | obv_20 | 9789.37 | -210.63 | sell /  / OBV > OBV의 SMA20 그리고 종가 > EMA26; 조건 미충족; OBV=2.01573e+07, OBV_SMA20=2.06236e+07, close=267.68, EMA26=266.081 |
| v1 | stochastic_14_3_recovery | 9415.97 | -584.03 | sell /  / 직전 %K14 < 20에서 %K14가 %D3 상향 돌파 (한 봉 목표); 조건 미충족; K14=13.4247, D3=7.95839, previous_K14=6.19489, previous_D3=6.11994 |
| v1 | mfi_14_recovery | 9931.49 | -68.51 | sell /  / 직전 MFI14 < 20, 현재 MFI14 >= 20 (한 봉 목표); 조건 미충족; MFI14=35.8262, previous_MFI14=31.0222 |
| v1 | adx_14_trend | 9672.00 | -328.00 | sell /  / Wilder ADX14 >= 25 그리고 +DI14 > -DI14; 조건 미충족; ADX14=53.7666, plus_DI14=23.1641, minus_DI14=36.2315 |
| v1 | aroon_25_trend | 9974.61 | -25.39 | sell /  / Aroon25 Up > 70 그리고 Down < 30 (동률이면 최신 극값); 조건 미충족; Aroon_up=76, Aroon_down=100 |
| v1 | cci_20_momentum | 10131.21 | 131.21 | sell /  / CCI20 > 100 (전형가격·평균절대편차); 조건 미충족; CCI20=91.7877 |
| v1 | williams_14_recovery | 9681.74 | -318.26 | sell /  / 직전 Williams %R14 < -80, 현재 >= -80 (한 봉 목표); 조건 미충족; Williams_R14=-48.9017, previous_R14=-71.9776 |
| v1 | cmf_20_accumulation | 10240.33 | 240.33 | sell /  / Chaikin Money Flow20 > 0.1; 조건 미충족; CMF20=-0.188785, volume20=4.96784e+06 |
| v1 | chaikin_3_10 | 10085.51 | 85.51 | sell /  / ADL의 EMA3 - EMA10 > 0 그리고 종가 > EMA26; 조건 미충족; Chaikin3_10=-220136, ADL=1.31662e+07, close=267.68, EMA26=266.081 |
| v1 | roc_10_momentum | 9834.72 | -165.28 | sell /  / 10봉 ROC > 1% 그리고 종가 > EMA26; 조건 미충족; ROC10_percent=0.555956, close=268.59, EMA26=264.916 |
| v1 | trix_15_trend | 9665.47 | -334.53 | sell /  / 15봉 삼중 EMA의 1봉 변화율 TRIX > 0 그리고 종가 > EMA26; 조건 미충족; TRIX15_percent=0.123572, close=263.8, EMA26=265.912 |
| v1 | keltner_20_breakout | 10029.96 | 29.96 | sell /  / 종가 > EMA20 + 2 x Wilder ATR14; 조건 미충족; close=267.68, upper_Keltner=268.805, EMA20=266.948, ATR14=0.92845 |
| v1 | opening_range_30m | 9973.31 | -26.69 | sell /  / 뉴욕 09:30·09:45 두 완료 봉 최고가를 10:00 이후 종가가 돌파; 자료 부족·변동폭 또는 거래량 없음: 대기; close=263.8 |
| v2 | cash | 10000.00 | 0.00 | 대기 /  / 새 신호 대기 |
| v2 | buy_hold | 10041.21 | 41.21 | 중단: 손실 한도 / buy / partial / 직전 완료 봉 목표 비중 100%; 다음 봉 시가 가정 |
| v2 | trend_8_26 | 10041.21 | 41.21 | 중단: 손실 한도 / buy / partial / 직전 완료 봉 목표 비중 100%; 다음 봉 시가 가정 |
| v2 | momentum_26 | 10041.21 | 41.21 | 중단: 손실 한도 / buy / partial / 직전 완료 봉 목표 비중 100%; 다음 봉 시가 가정 |
| v2 | breakout_8 | 9343.39 | -656.61 | 중단: 손실 한도 / sell / filled / 직전 완료 봉 목표 비중 0%; 다음 봉 시가 가정 |
| v2 | reversion_12 | 9295.90 | -704.10 | sell / filled / 직전 완료 봉 목표 비중 0%; 다음 봉 시가 가정 |
| v2 | volume_26 | 9819.31 | -180.69 | sell / filled / 직전 완료 봉 목표 비중 0%; 다음 봉 시가 가정 |
| v2 | trend_8_26 AND momentum_26 | 10041.21 | 41.21 | 중단: 손실 한도 / buy / partial / 직전 완료 봉 목표 비중 100%; 다음 봉 시가 가정 |
| v2 | trend_8_26 + momentum_26 | 10041.21 | 41.21 | 중단: 손실 한도 / buy / partial / 직전 완료 봉 목표 비중 100%; 다음 봉 시가 가정 |
| v2 | trend_8_26 AND breakout_8 | 9419.39 | -580.61 | 중단: 손실 한도 / sell / filled / 직전 완료 봉 목표 비중 0%; 다음 봉 시가 가정 |
| v2 | trend_8_26 + breakout_8 | 9384.04 | -615.96 | sell / filled / 직전 완료 봉 목표 비중 0%; 다음 봉 시가 가정 |
| v2 | trend_8_26 AND reversion_12 | 9775.94 | -224.06 | sell / filled / 직전 완료 봉 목표 비중 0%; 다음 봉 시가 가정 |
| v2 | trend_8_26 + reversion_12 | 9732.92 | -267.08 | 중단: 손실 한도 / sell / filled / 직전 완료 봉 목표 비중 0%; 다음 봉 시가 가정 |
| v2 | trend_8_26 AND volume_26 | 9997.51 | -2.49 | sell / filled / 직전 완료 봉 목표 비중 0%; 다음 봉 시가 가정 |
| v2 | trend_8_26 + volume_26 | 9997.39 | -2.61 | 중단: 손실 한도 / buy / filled / 직전 완료 봉 목표 비중 50%; 다음 봉 시가 가정 |
| v2 | momentum_26 AND breakout_8 | 9297.50 | -702.50 | sell / filled / 직전 완료 봉 목표 비중 0%; 다음 봉 시가 가정 |
| v2 | momentum_26 + breakout_8 | 9093.87 | -906.13 | sell / filled / 직전 완료 봉 목표 비중 0%; 다음 봉 시가 가정 |
| v2 | momentum_26 AND reversion_12 | 9637.84 | -362.16 | sell / filled / 직전 완료 봉 목표 비중 0%; 다음 봉 시가 가정 |
| v2 | momentum_26 + reversion_12 | 9732.92 | -267.08 | 중단: 손실 한도 / sell / filled / 직전 완료 봉 목표 비중 0%; 다음 봉 시가 가정 |
| v2 | momentum_26 AND volume_26 | 9920.93 | -79.07 | sell / filled / 직전 완료 봉 목표 비중 0%; 다음 봉 시가 가정 |
| v2 | momentum_26 + volume_26 | 9997.39 | -2.61 | 중단: 손실 한도 / buy / filled / 직전 완료 봉 목표 비중 50%; 다음 봉 시가 가정 |
| v2 | breakout_8 AND reversion_12 | 10000.00 | 0.00 | 대기 /  / 새 신호 대기 |
| v2 | breakout_8 + reversion_12 | 9092.57 | -907.43 | sell / filled / 직전 완료 봉 목표 비중 0%; 다음 봉 시가 가정 |
| v2 | breakout_8 AND volume_26 | 9949.08 | -50.92 | sell / filled / 직전 완료 봉 목표 비중 0%; 다음 봉 시가 가정 |
| v2 | breakout_8 + volume_26 | 9345.10 | -654.90 | sell / filled / 직전 완료 봉 목표 비중 0%; 다음 봉 시가 가정 |
| v2 | reversion_12 AND volume_26 | 9816.09 | -183.91 | sell / filled / 직전 완료 봉 목표 비중 0%; 다음 봉 시가 가정 |
| v2 | reversion_12 + volume_26 | 9594.59 | -405.41 | sell / filled / 직전 완료 봉 목표 비중 0%; 다음 봉 시가 가정 |
| v2 | ema_12_26 | 9819.81 | -180.19 | sell / filled / EMA12 > EMA26; 조건 미충족; EMA12=264.816, EMA26=264.953; 직전 완료 봉 목표를 다음 봉 시가에 모의 적용 |
| v2 | macd_12_26_9 | 10144.54 | 144.54 | sell / filled / MACD > 신호선 그리고 MACD > 0; 조건 미충족; MACD=2.48372, signal9=2.49952; 직전 완료 봉 목표를 다음 봉 시가에 모의 적용 |
| v2 | rsi_14_recovery | 9919.07 | -80.93 | sell / filled / 직전 RSI14 < 30, 현재 RSI14 >= 30 (한 봉 목표); 조건 미충족; RSI14=40.3665, previous_RSI14=36.2025; 직전 완료 봉 목표를 다음 봉 시가에 모의 적용 |
| v2 | bollinger_20_reentry | 9770.69 | -229.31 | sell / filled / 직전 종가 < 직전 하단밴드, 현재 하단밴드 <= 종가 <= SMA20 (한 봉 목표); 조건 미충족; close=263.43, lower20=262.644, SMA20=266.981, previous_lower20=263.145; 직전 완료 봉 목표를 다음 봉 시가에 모의 적용 |
| v2 | donchian_20 | 9764.13 | -235.87 | sell / filled / 종가 > 현재 봉을 제외한 직전 20봉 최고가; 조건 미충족; close=268.59, prior_high20=269.55; 직전 완료 봉 목표를 다음 봉 시가에 모의 적용 |
| v2 | atr_14_breakout | 9619.01 | -380.99 | sell / filled / 종가 > 직전 종가 + 직전 ATR14 그리고 종가 > EMA26; 조건 미충족; close=269.05, threshold=269.858, prior_ATR14=0.907979, EMA26=264.623; 직전 완료 봉 목표를 다음 봉 시가에 모의 적용 |
| v2 | session_vwap | 9913.38 | -86.62 | sell / filled / 종가 > 뉴욕 거래일별 누적 전형가격 VWAP; 조건 미충족; close=263.8, session_VWAP=264.478, session_volume=329302; 직전 완료 봉 목표를 다음 봉 시가에 모의 적용 |
| v2 | obv_20 | 9769.81 | -230.19 | sell / filled / OBV > OBV의 SMA20 그리고 종가 > EMA26; 조건 미충족; OBV=2.01573e+07, OBV_SMA20=2.06236e+07, close=267.68, EMA26=266.081; 직전 완료 봉 목표를 다음 봉 시가에 모의 적용 |
| v2 | stochastic_14_3_recovery | 9393.40 | -606.60 | sell / filled / 직전 %K14 < 20에서 %K14가 %D3 상향 돌파 (한 봉 목표); 조건 미충족; K14=13.4247, D3=7.95839, previous_K14=6.19489, previous_D3=6.11994; 직전 완료 봉 목표를 다음 봉 시가에 모의 적용 |
| v2 | mfi_14_recovery | 9925.53 | -74.47 | sell / filled / 직전 MFI14 < 20, 현재 MFI14 >= 20 (한 봉 목표); 조건 미충족; MFI14=35.8262, previous_MFI14=31.0222; 직전 완료 봉 목표를 다음 봉 시가에 모의 적용 |
| v2 | adx_14_trend | 9662.33 | -337.67 | sell / filled / Wilder ADX14 >= 25 그리고 +DI14 > -DI14; 조건 미충족; ADX14=53.7666, plus_DI14=23.1641, minus_DI14=36.2315; 직전 완료 봉 목표를 다음 봉 시가에 모의 적용 |
| v2 | aroon_25_trend | 9968.63 | -31.37 | sell / filled / Aroon25 Up > 70 그리고 Down < 30 (동률이면 최신 극값); 조건 미충족; Aroon_up=76, Aroon_down=100; 직전 완료 봉 목표를 다음 봉 시가에 모의 적용 |
| v2 | cci_20_momentum | 10121.08 | 121.08 | sell / filled / CCI20 > 100 (전형가격·평균절대편차); 조건 미충족; CCI20=91.7877; 직전 완료 봉 목표를 다음 봉 시가에 모의 적용 |
| v2 | williams_14_recovery | 9670.13 | -329.87 | sell / filled / 직전 Williams %R14 < -80, 현재 >= -80 (한 봉 목표); 조건 미충족; Williams_R14=-48.9017, previous_R14=-71.9776; 직전 완료 봉 목표를 다음 봉 시가에 모의 적용 |
| v2 | cmf_20_accumulation | 10234.18 | 234.18 | sell / filled / Chaikin Money Flow20 > 0.1; 조건 미충족; CMF20=-0.188785, volume20=4.96784e+06; 직전 완료 봉 목표를 다음 봉 시가에 모의 적용 |
| v2 | chaikin_3_10 | 10075.43 | 75.43 | sell / filled / ADL의 EMA3 - EMA10 > 0 그리고 종가 > EMA26; 조건 미충족; Chaikin3_10=-220136, ADL=1.31662e+07, close=267.68, EMA26=266.081; 직전 완료 봉 목표를 다음 봉 시가에 모의 적용 |
| v2 | roc_10_momentum | 9822.93 | -177.07 | sell / filled / 10봉 ROC > 1% 그리고 종가 > EMA26; 조건 미충족; ROC10_percent=0.555956, close=268.59, EMA26=264.916; 직전 완료 봉 목표를 다음 봉 시가에 모의 적용 |
| v2 | trix_15_trend | 9657.74 | -342.26 | sell / filled / 15봉 삼중 EMA의 1봉 변화율 TRIX > 0 그리고 종가 > EMA26; 조건 미충족; TRIX15_percent=0.123572, close=263.8, EMA26=265.912; 직전 완료 봉 목표를 다음 봉 시가에 모의 적용 |
| v2 | keltner_20_breakout | 10025.95 | 25.95 | sell / filled / 종가 > EMA20 + 2 x Wilder ATR14; 조건 미충족; close=267.68, upper_Keltner=268.805, EMA20=266.948, ATR14=0.92845; 직전 완료 봉 목표를 다음 봉 시가에 모의 적용 |
| v2 | opening_range_30m | 9971.31 | -28.69 | sell / filled / 뉴욕 09:30·09:45 두 완료 봉 최고가를 10:00 이후 종가가 돌파; 자료 부족·변동폭 또는 거래량 없음: 대기; close=263.8; 직전 완료 봉 목표를 다음 봉 시가에 모의 적용 |

### 같은 기간의 비용·노출 비교 (사후 연구)

| 전략 | 비용 전 | 비용 후 | 100% 보유 | 같은 평균 노출 보유 | 평균 노출 |
|---|---:|---:|---:|---:|---:|
| cash | 0.00% | 0.00% | 2.89% | 0.00% | 0.00% |
| buy_hold | 3.32% | 2.89% | 2.89% | 2.89% | 100.00% |
| trend_8_26 | 5.22% | 2.61% | 2.89% | 1.61% | 56.02% |
| momentum_26 | -0.46% | -4.56% | 2.89% | 1.54% | 53.66% |
| breakout_8 | 2.39% | -17.70% | 2.89% | 0.73% | 25.39% |
| reversion_12 | -4.63% | -11.57% | 2.89% | 0.63% | 21.99% |
| volume_26 | 3.01% | -2.88% | 2.89% | 0.14% | 4.97% |
| trend_8_26 AND momentum_26 | 1.18% | -1.75% | 2.89% | 1.37% | 47.64% |
| trend_8_26 + momentum_26 | 2.35% | -0.83% | 2.89% | 1.58% | 54.84% |
| trend_8_26 AND breakout_8 | 3.61% | -10.93% | 2.89% | 0.53% | 18.59% |
| trend_8_26 + breakout_8 | 3.83% | -7.89% | 2.89% | 1.17% | 40.71% |
| trend_8_26 AND reversion_12 | 0.52% | -3.21% | 2.89% | 0.19% | 6.54% |
| trend_8_26 + reversion_12 | 0.22% | -4.53% | 2.89% | 1.12% | 39.01% |
| trend_8_26 AND volume_26 | 3.25% | 0.26% | 2.89% | 0.06% | 2.09% |
| trend_8_26 + volume_26 | 4.15% | 0.05% | 2.89% | 0.88% | 30.50% |
| momentum_26 AND breakout_8 | 2.60% | -10.68% | 2.89% | 0.48% | 16.75% |
| momentum_26 + breakout_8 | 0.99% | -11.16% | 2.89% | 1.14% | 39.54% |
| momentum_26 AND reversion_12 | -1.40% | -5.46% | 2.89% | 0.21% | 7.33% |
| momentum_26 + reversion_12 | -2.54% | -7.54% | 2.89% | 1.09% | 37.83% |
| momentum_26 AND volume_26 | 0.14% | -0.70% | 2.89% | 0.02% | 0.52% |
| momentum_26 + volume_26 | 1.30% | -2.48% | 2.89% | 0.84% | 29.32% |
| breakout_8 AND reversion_12 | 0.00% | 0.00% | 2.89% | 0.00% | 0.00% |
| breakout_8 + reversion_12 | -1.16% | -14.33% | 2.89% | 0.68% | 23.70% |
| breakout_8 AND volume_26 | 1.33% | 0.06% | 2.89% | 0.03% | 1.05% |
| breakout_8 + volume_26 | 2.71% | -9.65% | 2.89% | 0.44% | 15.19% |
| reversion_12 AND volume_26 | -0.88% | -2.53% | 2.89% | 0.05% | 1.57% |
| reversion_12 + volume_26 | -0.87% | -6.93% | 2.89% | 0.39% | 13.49% |
| ema_12_26 | -0.07% | -2.97% | 2.89% | 1.59% | 55.24% |
| macd_12_26_9 | 9.10% | 5.49% | 2.89% | 1.00% | 34.82% |
| rsi_14_recovery | 0.00% | -2.89% | 2.89% | 0.05% | 1.83% |
| bollinger_20_reentry | -1.15% | -5.22% | 2.89% | 0.08% | 2.62% |
| donchian_20 | 2.07% | -7.72% | 2.89% | 0.29% | 9.95% |
| atr_14_breakout | 1.15% | -6.61% | 2.89% | 0.17% | 6.02% |
| session_vwap | 6.62% | -1.55% | 2.89% | 1.67% | 57.85% |
| obv_20 | -2.58% | -12.66% | 2.89% | 1.23% | 42.67% |
| stochastic_14_3_recovery | -0.64% | -10.55% | 2.89% | 0.19% | 6.54% |
| mfi_14_recovery | 0.80% | -1.30% | 2.89% | 0.04% | 1.31% |
| adx_14_trend | -3.32% | -8.45% | 2.89% | 1.24% | 42.93% |
| aroon_25_trend | 4.48% | 0.18% | 2.89% | 1.08% | 37.43% |
| cci_20_momentum | 4.61% | -2.19% | 2.89% | 0.71% | 24.87% |
| williams_14_recovery | -0.66% | -5.94% | 2.89% | 0.10% | 3.40% |
| cmf_20_accumulation | 6.29% | 1.49% | 2.89% | 1.21% | 42.15% |
| chaikin_3_10 | 0.06% | -5.26% | 2.89% | 1.31% | 45.55% |
| roc_10_momentum | -0.56% | -8.19% | 2.89% | 0.65% | 22.51% |
| trix_15_trend | -1.21% | -4.08% | 2.89% | 1.21% | 42.15% |
| keltner_20_breakout | 1.76% | -2.43% | 2.89% | 0.53% | 18.32% |
| opening_range_30m | 0.92% | -3.23% | 2.89% | 0.92% | 31.94% |

동일 구간·초기 자금, 종료 시 청산 비용 포함. 노출 맞춤은 사후 설명용이며 v2 실제 계좌 성과가 아닙니다.
[낙폭 분해·비용 영향·전체 구간](JNJ/comparison.json)

[v1 전체 기록](JNJ/accounts.json) · [v2 전체 기록](JNJ/accounts-v2.json)

## CAT 계좌

| 모델 | 전략 | 평가액 USD | 손익 USD | 최근 매매·이유 |
|---|---|---:|---:|---|
| v1 | cash | 10000.00 | 0.00 | 대기 /  / 새 신호 대기 |
| v1 | buy_hold | 9364.67 | -635.33 | buy /  / buy_hold: prior completed bar target 100%; next bar open simulation |
| v1 | trend_8_26 | 9570.52 | -429.48 | sell /  / trend_8_26: prior completed bar target 0%; next bar open simulation |
| v1 | momentum_26 | 9290.58 | -709.42 | sell /  / momentum_26: prior completed bar target 0%; next bar open simulation |
| v1 | breakout_8 | 9314.02 | -685.98 | sell /  / breakout_8: prior completed bar target 0%; next bar open simulation |
| v1 | reversion_12 | 9648.22 | -351.78 | sell /  / reversion_12: prior completed bar target 0%; next bar open simulation |
| v1 | volume_26 | 9611.34 | -388.66 | sell /  / volume_26: prior completed bar target 0%; next bar open simulation |
| v1 | trend_8_26 AND momentum_26 | 9471.21 | -528.79 | sell /  / trend_8_26 AND momentum_26: prior completed bar target 0%; next bar open simulation |
| v1 | trend_8_26 + momentum_26 | 9430.55 | -569.45 | sell /  / trend_8_26 + momentum_26: prior completed bar target 0%; next bar open simulation |
| v1 | trend_8_26 AND breakout_8 | 9747.92 | -252.08 | sell /  / trend_8_26 AND breakout_8: prior completed bar target 0%; next bar open simulation |
| v1 | trend_8_26 + breakout_8 | 9443.36 | -556.64 | sell /  / trend_8_26 + breakout_8: prior completed bar target 0%; next bar open simulation |
| v1 | trend_8_26 AND reversion_12 | 9919.62 | -80.38 | sell /  / trend_8_26 AND reversion_12: prior completed bar target 0%; next bar open simulation |
| v1 | trend_8_26 + reversion_12 | 9669.55 | -330.45 | sell /  / trend_8_26 + reversion_12: prior completed bar target 0%; next bar open simulation |
| v1 | trend_8_26 AND volume_26 | 9965.69 | -34.31 | sell /  / trend_8_26 AND volume_26: prior completed bar target 0%; next bar open simulation |
| v1 | trend_8_26 + volume_26 | 9631.20 | -368.80 | sell /  / trend_8_26 + volume_26: prior completed bar target 0%; next bar open simulation |
| v1 | momentum_26 AND breakout_8 | 9615.85 | -384.15 | sell /  / momentum_26 AND breakout_8: prior completed bar target 0%; next bar open simulation |
| v1 | momentum_26 + breakout_8 | 9303.28 | -696.72 | sell /  / momentum_26 + breakout_8: prior completed bar target 0%; next bar open simulation |
| v1 | momentum_26 AND reversion_12 | 9878.81 | -121.19 | sell /  / momentum_26 AND reversion_12: prior completed bar target 0%; next bar open simulation |
| v1 | momentum_26 + reversion_12 | 9488.17 | -511.83 | sell /  / momentum_26 + reversion_12: prior completed bar target 0%; next bar open simulation |
| v1 | momentum_26 AND volume_26 | 9894.55 | -105.45 | sell /  / momentum_26 AND volume_26: prior completed bar target 0%; next bar open simulation |
| v1 | momentum_26 + volume_26 | 9469.44 | -530.56 | sell /  / momentum_26 + volume_26: prior completed bar target 0%; next bar open simulation |
| v1 | breakout_8 AND reversion_12 | 10000.00 | 0.00 | 대기 /  / 새 신호 대기 |
| v1 | breakout_8 + reversion_12 | 9499.29 | -500.71 | sell /  / breakout_8 + reversion_12: prior completed bar target 0%; next bar open simulation |
| v1 | breakout_8 AND volume_26 | 9894.55 | -105.45 | sell /  / breakout_8 AND volume_26: prior completed bar target 0%; next bar open simulation |
| v1 | breakout_8 + volume_26 | 9461.72 | -538.28 | sell /  / breakout_8 + volume_26: prior completed bar target 0%; next bar open simulation |
| v1 | reversion_12 AND volume_26 | 9737.41 | -262.59 | sell /  / reversion_12 AND volume_26: prior completed bar target 0%; next bar open simulation |
| v1 | reversion_12 + volume_26 | 9630.21 | -369.79 | sell /  / reversion_12 + volume_26: prior completed bar target 0%; next bar open simulation |
| v1 | ema_12_26 | 9597.59 | -402.41 | sell /  / EMA12 > EMA26; 조건 미충족; EMA12=734.57, EMA26=734.673 |
| v1 | macd_12_26_9 | 9988.51 | -11.49 | sell /  / MACD > 신호선 그리고 MACD > 0; 조건 미충족; MACD=2.92675, signal9=3.02629 |
| v1 | rsi_14_recovery | 9866.63 | -133.37 | sell /  / 직전 RSI14 < 30, 현재 RSI14 >= 30 (한 봉 목표); 조건 미충족; RSI14=34.2237, previous_RSI14=36.7431 |
| v1 | bollinger_20_reentry | 9611.32 | -388.68 | sell /  / 직전 종가 < 직전 하단밴드, 현재 하단밴드 <= 종가 <= SMA20 (한 봉 목표); 조건 미충족; close=688.16, lower20=683.118, SMA20=697.519, previous_lower20=684.291 |
| v1 | donchian_20 | 9943.28 | -56.72 | sell /  / 종가 > 현재 봉을 제외한 직전 20봉 최고가; 조건 미충족; close=735.35, prior_high20=745 |
| v1 | atr_14_breakout | 9768.31 | -231.69 | sell /  / 종가 > 직전 종가 + 직전 ATR14 그리고 종가 > EMA26; 조건 미충족; close=735.35, threshold=737.263, prior_ATR14=4.10289, EMA26=727.331 |
| v1 | session_vwap | 8834.40 | -1165.60 | sell /  / 종가 > 뉴욕 거래일별 누적 전형가격 VWAP; 조건 미충족; close=687.03, session_VWAP=687.348, session_volume=2.31562e+06 |
| v1 | obv_20 | 9541.23 | -458.77 | sell /  / OBV > OBV의 SMA20 그리고 종가 > EMA26; 조건 미충족; OBV=-5.63582e+06, OBV_SMA20=-5.55612e+06, close=711.18, EMA26=734.673 |
| v1 | stochastic_14_3_recovery | 9701.71 | -298.29 | sell /  / 직전 %K14 < 20에서 %K14가 %D3 상향 돌파 (한 봉 목표); 조건 미충족; K14=31.4561, D3=31.5097, previous_K14=44.0064, previous_D3=30.7053 |
| v1 | mfi_14_recovery | 9992.21 | -7.79 | sell /  / 직전 MFI14 < 20, 현재 MFI14 >= 20 (한 봉 목표); 조건 미충족; MFI14=41.7007, previous_MFI14=39.2559 |
| v1 | adx_14_trend | 9614.13 | -385.87 | sell /  / Wilder ADX14 >= 25 그리고 +DI14 > -DI14; 조건 미충족; ADX14=37.6898, plus_DI14=16.8278, minus_DI14=52.0976 |
| v1 | aroon_25_trend | 9979.61 | -20.39 | sell /  / Aroon25 Up > 70 그리고 Down < 30 (동률이면 최신 극값); 조건 미충족; Aroon_up=68, Aroon_down=20 |
| v1 | cci_20_momentum | 9862.85 | -137.15 | sell /  / CCI20 > 100 (전형가격·평균절대편차); 조건 미충족; CCI20=99.2123 |
| v1 | williams_14_recovery | 9736.92 | -263.08 | sell /  / 직전 Williams %R14 < -80, 현재 >= -80 (한 봉 목표); 조건 미충족; Williams_R14=-68.5439, previous_R14=-55.9936 |
| v1 | cmf_20_accumulation | 9458.11 | -541.89 | sell /  / Chaikin Money Flow20 > 0.1; 조건 미충족; CMF20=0.0105743, volume20=1.36134e+06 |
| v1 | chaikin_3_10 | 9240.53 | -759.47 | sell /  / ADL의 EMA3 - EMA10 > 0 그리고 종가 > EMA26; 조건 미충족; Chaikin3_10=-27551.7, ADL=-5.27692e+06, close=711.18, EMA26=734.673 |
| v1 | roc_10_momentum | 9896.73 | -103.27 | sell /  / 10봉 ROC > 1% 그리고 종가 > EMA26; 조건 미충족; ROC10_percent=0.883016, close=741.47, EMA26=734.681 |
| v1 | trix_15_trend | 9340.52 | -659.48 | sell /  / 15봉 삼중 EMA의 1봉 변화율 TRIX > 0 그리고 종가 > EMA26; 조건 미충족; TRIX15_percent=0.0460682, close=711.18, EMA26=734.673 |
| v1 | keltner_20_breakout | 10000.00 | 0.00 | 대기 /  / 새 신호 대기 |
| v1 | opening_range_30m | 10162.22 | 162.22 | sell /  / 뉴욕 09:30·09:45 두 완료 봉 최고가를 10:00 이후 종가가 돌파; 자료 부족·변동폭 또는 거래량 없음: 대기; close=733.16 |
| v2 | cash | 10000.00 | 0.00 | 대기 /  / 새 신호 대기 |
| v2 | buy_hold | 8612.45 | -1387.55 | 중단: 손실 한도 / buy / partial / 직전 완료 봉 목표 비중 100%; 다음 봉 시가 가정 |
| v2 | trend_8_26 | 9215.55 | -784.45 | 중단: 손실 한도 / buy / partial / 직전 완료 봉 목표 비중 100%; 다음 봉 시가 가정 |
| v2 | momentum_26 | 9021.58 | -978.42 | 중단: 손실 한도 / buy / partial / 직전 완료 봉 목표 비중 100%; 다음 봉 시가 가정 |
| v2 | breakout_8 | 9125.42 | -874.58 | sell / filled / 직전 완료 봉 목표 비중 0%; 다음 봉 시가 가정 |
| v2 | reversion_12 | 8492.17 | -1507.83 | 중단: 손실 한도 / buy / partial / 직전 완료 봉 목표 비중 100%; 다음 봉 시가 가정 |
| v2 | volume_26 | 8735.04 | -1264.96 | 중단: 손실 한도 / buy / partial / 직전 완료 봉 목표 비중 100%; 다음 봉 시가 가정 |
| v2 | trend_8_26 AND momentum_26 | 9229.15 | -770.85 | 중단: 손실 한도 / buy / partial / 직전 완료 봉 목표 비중 100%; 다음 봉 시가 가정 |
| v2 | trend_8_26 + momentum_26 | 9119.04 | -880.96 | 중단: 손실 한도 / buy / partial / 직전 완료 봉 목표 비중 100%; 다음 봉 시가 가정 |
| v2 | trend_8_26 AND breakout_8 | 9655.84 | -344.16 | sell / filled / 직전 완료 봉 목표 비중 0%; 다음 봉 시가 가정 |
| v2 | trend_8_26 + breakout_8 | 9308.52 | -691.48 | sell / filled / 직전 완료 봉 목표 비중 0%; 다음 봉 시가 가정 |
| v2 | trend_8_26 AND reversion_12 | 9728.39 | -271.61 | sell / filled / 직전 완료 봉 목표 비중 0%; 다음 봉 시가 가정 |
| v2 | trend_8_26 + reversion_12 | 9309.67 | -690.33 | 중단: 손실 한도 / sell / filled / 직전 완료 봉 목표 비중 0%; 다음 봉 시가 가정 |
| v2 | trend_8_26 AND volume_26 | 9999.01 | -0.99 | sell / filled / 직전 완료 봉 목표 비중 0%; 다음 봉 시가 가정 |
| v2 | trend_8_26 + volume_26 | 9303.04 | -696.96 | 중단: 손실 한도 / sell / filled / 직전 완료 봉 목표 비중 0%; 다음 봉 시가 가정 |
| v2 | momentum_26 AND breakout_8 | 9576.90 | -423.10 | sell / filled / 직전 완료 봉 목표 비중 0%; 다음 봉 시가 가정 |
| v2 | momentum_26 + breakout_8 | 9209.04 | -790.96 | sell / filled / 직전 완료 봉 목표 비중 0%; 다음 봉 시가 가정 |
| v2 | momentum_26 AND reversion_12 | 9745.30 | -254.70 | sell / filled / 직전 완료 봉 목표 비중 0%; 다음 봉 시가 가정 |
| v2 | momentum_26 + reversion_12 | 9171.71 | -828.29 | 중단: 손실 한도 / sell / filled / 직전 완료 봉 목표 비중 0%; 다음 봉 시가 가정 |
| v2 | momentum_26 AND volume_26 | 9936.85 | -63.15 | sell / filled / 직전 완료 봉 목표 비중 0%; 다음 봉 시가 가정 |
| v2 | momentum_26 + volume_26 | 9203.76 | -796.24 | 중단: 손실 한도 / sell / filled / 직전 완료 봉 목표 비중 0%; 다음 봉 시가 가정 |
| v2 | breakout_8 AND reversion_12 | 10000.00 | 0.00 | 대기 /  / 새 신호 대기 |
| v2 | breakout_8 + reversion_12 | 9610.18 | -389.82 | 중단: 손실 한도 / sell / filled / 직전 완료 봉 목표 비중 0%; 다음 봉 시가 가정 |
| v2 | breakout_8 AND volume_26 | 9887.31 | -112.69 | sell / filled / 직전 완료 봉 목표 비중 0%; 다음 봉 시가 가정 |
| v2 | breakout_8 + volume_26 | 9066.90 | -933.10 | sell / filled / 직전 완료 봉 목표 비중 0%; 다음 봉 시가 가정 |
| v2 | reversion_12 AND volume_26 | 8674.62 | -1325.38 | 중단: 손실 한도 / buy / partial / 직전 완료 봉 목표 비중 100%; 다음 봉 시가 가정 |
| v2 | reversion_12 + volume_26 | 9105.73 | -894.27 | 중단: 손실 한도 / sell / filled / 직전 완료 봉 목표 비중 50%; 다음 봉 시가 가정 |
| v2 | ema_12_26 | 9315.44 | -684.56 | 중단: 손실 한도 / buy / partial / EMA12 > EMA26; 조건 충족; EMA12=726.261, EMA26=726.172; 직전 완료 봉 목표를 다음 봉 시가에 모의 적용 |
| v2 | macd_12_26_9 | 9984.52 | -15.48 | sell / filled / MACD > 신호선 그리고 MACD > 0; 조건 미충족; MACD=2.92675, signal9=3.02629; 직전 완료 봉 목표를 다음 봉 시가에 모의 적용 |
| v2 | rsi_14_recovery | 9858.74 | -141.26 | sell / filled / 직전 RSI14 < 30, 현재 RSI14 >= 30 (한 봉 목표); 조건 미충족; RSI14=34.2237, previous_RSI14=36.7431; 직전 완료 봉 목표를 다음 봉 시가에 모의 적용 |
| v2 | bollinger_20_reentry | 9601.72 | -398.28 | sell / filled / 직전 종가 < 직전 하단밴드, 현재 하단밴드 <= 종가 <= SMA20 (한 봉 목표); 조건 미충족; close=688.16, lower20=683.118, SMA20=697.519, previous_lower20=684.291; 직전 완료 봉 목표를 다음 봉 시가에 모의 적용 |
| v2 | donchian_20 | 9939.30 | -60.70 | sell / filled / 종가 > 현재 봉을 제외한 직전 20봉 최고가; 조건 미충족; close=735.35, prior_high20=745; 직전 완료 봉 목표를 다음 봉 시가에 모의 적용 |
| v2 | atr_14_breakout | 9758.55 | -241.45 | sell / filled / 종가 > 직전 종가 + 직전 ATR14 그리고 종가 > EMA26; 조건 미충족; close=735.35, threshold=737.263, prior_ATR14=4.10289, EMA26=727.331; 직전 완료 봉 목표를 다음 봉 시가에 모의 적용 |
| v2 | session_vwap | 8970.38 | -1029.62 | 중단: 손실 한도 / buy / partial / 종가 > 뉴욕 거래일별 누적 전형가격 VWAP; 조건 충족; close=734.98, session_VWAP=734.093, session_volume=764353; 직전 완료 봉 목표를 다음 봉 시가에 모의 적용 |
| v2 | obv_20 | 9253.33 | -746.67 | 중단: 손실 한도 / buy / partial / OBV > OBV의 SMA20 그리고 종가 > EMA26; 조건 충족; OBV=-5.0567e+06, OBV_SMA20=-6.30537e+06, close=733.16, EMA26=726.69; 직전 완료 봉 목표를 다음 봉 시가에 모의 적용 |
| v2 | stochastic_14_3_recovery | 9680.39 | -319.61 | sell / filled / 직전 %K14 < 20에서 %K14가 %D3 상향 돌파 (한 봉 목표); 조건 미충족; K14=31.4561, D3=31.5097, previous_K14=44.0064, previous_D3=30.7053; 직전 완료 봉 목표를 다음 봉 시가에 모의 적용 |
| v2 | mfi_14_recovery | 9986.21 | -13.79 | sell / filled / 직전 MFI14 < 20, 현재 MFI14 >= 20 (한 봉 목표); 조건 미충족; MFI14=41.7007, previous_MFI14=39.2559; 직전 완료 봉 목표를 다음 봉 시가에 모의 적용 |
| v2 | adx_14_trend | 9333.36 | -666.64 | 중단: 손실 한도 / buy / partial / Wilder ADX14 >= 25 그리고 +DI14 > -DI14; 조건 충족; ADX14=25.4031, plus_DI14=35.2628, minus_DI14=13.9603; 직전 완료 봉 목표를 다음 봉 시가에 모의 적용 |
| v2 | aroon_25_trend | 9973.62 | -26.38 | sell / filled / Aroon25 Up > 70 그리고 Down < 30 (동률이면 최신 극값); 조건 미충족; Aroon_up=68, Aroon_down=20; 직전 완료 봉 목표를 다음 봉 시가에 모의 적용 |
| v2 | cci_20_momentum | 9854.97 | -145.03 | sell / filled / CCI20 > 100 (전형가격·평균절대편차); 조건 미충족; CCI20=99.2123; 직전 완료 봉 목표를 다음 봉 시가에 모의 적용 |
| v2 | williams_14_recovery | 9721.35 | -278.65 | sell / filled / 직전 Williams %R14 < -80, 현재 >= -80 (한 봉 목표); 조건 미충족; Williams_R14=-68.5439, previous_R14=-55.9936; 직전 완료 봉 목표를 다음 봉 시가에 모의 적용 |
| v2 | cmf_20_accumulation | 9174.55 | -825.45 | 중단: 손실 한도 / buy / partial / Chaikin Money Flow20 > 0.1; 조건 충족; CMF20=0.145111, volume20=965726; 직전 완료 봉 목표를 다음 봉 시가에 모의 적용 |
| v2 | chaikin_3_10 | 9070.17 | -929.83 | 중단: 손실 한도 / buy / partial / ADL의 EMA3 - EMA10 > 0 그리고 종가 > EMA26; 조건 충족; Chaikin3_10=293683, ADL=-4.91156e+06, close=739.58, EMA26=736.187; 직전 완료 봉 목표를 다음 봉 시가에 모의 적용 |
| v2 | roc_10_momentum | 9888.81 | -111.19 | sell / filled / 10봉 ROC > 1% 그리고 종가 > EMA26; 조건 미충족; ROC10_percent=0.883016, close=741.47, EMA26=734.681; 직전 완료 봉 목표를 다음 봉 시가에 모의 적용 |
| v2 | trix_15_trend | 9079.31 | -920.69 | 중단: 손실 한도 / buy / partial / 15봉 삼중 EMA의 1봉 변화율 TRIX > 0 그리고 종가 > EMA26; 조건 충족; TRIX15_percent=0.0196284, close=739.58, EMA26=736.187; 직전 완료 봉 목표를 다음 봉 시가에 모의 적용 |
| v2 | keltner_20_breakout | 10000.00 | 0.00 | 대기 /  / 새 신호 대기 |
| v2 | opening_range_30m | 10158.15 | 158.15 | sell / filled / 뉴욕 09:30·09:45 두 완료 봉 최고가를 10:00 이후 종가가 돌파; 자료 부족·변동폭 또는 거래량 없음: 대기; close=733.16; 직전 완료 봉 목표를 다음 봉 시가에 모의 적용 |

### 같은 기간의 비용·노출 비교 (사후 연구)

| 전략 | 비용 전 | 비용 후 | 100% 보유 | 같은 평균 노출 보유 | 평균 노출 |
|---|---:|---:|---:|---:|---:|
| cash | 0.00% | 0.00% | -17.35% | -0.00% | 0.00% |
| buy_hold | -17.00% | -17.35% | -17.35% | -17.35% | 100.00% |
| trend_8_26 | -2.45% | -5.67% | -17.35% | -7.02% | 38.48% |
| momentum_26 | -5.96% | -9.83% | -17.35% | -6.65% | 36.39% |
| breakout_8 | -1.90% | -14.23% | -17.35% | -2.87% | 15.45% |
| reversion_12 | -2.64% | -15.95% | -17.35% | -5.15% | 28.01% |
| volume_26 | -3.30% | -11.47% | -17.35% | -1.61% | 8.64% |
| trend_8_26 AND momentum_26 | -1.86% | -4.71% | -17.35% | -5.76% | 31.41% |
| trend_8_26 + momentum_26 | -4.20% | -7.76% | -17.35% | -6.83% | 37.44% |
| trend_8_26 AND breakout_8 | 0.84% | -5.31% | -17.35% | -1.52% | 8.12% |
| trend_8_26 + breakout_8 | -2.14% | -9.84% | -17.35% | -4.96% | 26.97% |
| trend_8_26 AND reversion_12 | 2.91% | -2.56% | -17.35% | -0.93% | 4.97% |
| trend_8_26 + reversion_12 | -2.47% | -9.98% | -17.35% | -6.09% | 33.25% |
| trend_8_26 AND volume_26 | 2.90% | 1.18% | -17.35% | -0.29% | 1.57% |
| trend_8_26 + volume_26 | -2.83% | -8.21% | -17.35% | -4.35% | 23.56% |
| momentum_26 AND breakout_8 | 0.09% | -6.80% | -17.35% | -1.56% | 8.38% |
| momentum_26 + breakout_8 | -3.92% | -12.04% | -17.35% | -4.77% | 25.92% |
| momentum_26 AND reversion_12 | -0.98% | -6.25% | -17.35% | -1.08% | 5.76% |
| momentum_26 + reversion_12 | -4.26% | -12.74% | -17.35% | -5.90% | 32.20% |
| momentum_26 AND volume_26 | 2.69% | 0.55% | -17.35% | -0.29% | 1.57% |
| momentum_26 + volume_26 | -4.60% | -10.25% | -17.35% | -4.16% | 22.52% |
| breakout_8 AND reversion_12 | 0.00% | 0.00% | -17.35% | -0.00% | 0.00% |
| breakout_8 + reversion_12 | -2.21% | -14.18% | -17.35% | -4.02% | 21.74% |
| breakout_8 AND volume_26 | 0.55% | -1.13% | -17.35% | -0.20% | 1.05% |
| breakout_8 + volume_26 | -2.57% | -12.30% | -17.35% | -2.24% | 12.05% |
| reversion_12 AND volume_26 | -2.64% | -7.81% | -17.35% | -1.03% | 5.50% |
| reversion_12 + volume_26 | -2.93% | -13.36% | -17.35% | -3.40% | 18.33% |
| ema_12_26 | -3.20% | -4.81% | -17.35% | -6.27% | 34.29% |
| macd_12_26_9 | 0.73% | -1.36% | -17.35% | -3.92% | 21.20% |
| rsi_14_recovery | -0.08% | -6.58% | -17.35% | -0.78% | 4.19% |
| bollinger_20_reentry | -0.84% | -6.50% | -17.35% | -0.69% | 3.66% |
| donchian_20 | 1.25% | -1.69% | -17.35% | -0.59% | 3.14% |
| atr_14_breakout | 1.29% | -2.88% | -17.35% | -0.54% | 2.88% |
| session_vwap | -3.76% | -14.80% | -17.35% | -8.30% | 45.81% |
| obv_20 | -3.87% | -11.62% | -17.35% | -3.59% | 19.37% |
| stochastic_14_3_recovery | -0.66% | -12.05% | -17.35% | -1.42% | 7.59% |
| mfi_14_recovery | 1.79% | -1.16% | -17.35% | -0.34% | 1.83% |
| adx_14_trend | -3.70% | -5.70% | -17.35% | -1.13% | 6.02% |
| aroon_25_trend | 1.10% | -1.83% | -17.35% | -1.52% | 8.12% |
| cci_20_momentum | -1.74% | -6.17% | -17.35% | -2.39% | 12.83% |
| williams_14_recovery | -0.72% | -9.10% | -17.35% | -1.03% | 5.50% |
| cmf_20_accumulation | -4.44% | -10.28% | -17.35% | -2.96% | 15.97% |
| chaikin_3_10 | -6.00% | -13.57% | -17.35% | -4.73% | 25.65% |
| roc_10_momentum | -0.09% | -5.40% | -17.35% | -1.76% | 9.42% |
| trix_15_trend | -3.86% | -7.43% | -17.35% | -4.87% | 26.44% |
| keltner_20_breakout | 0.38% | -0.46% | -17.35% | -0.25% | 1.31% |
| opening_range_30m | 3.63% | -0.21% | -17.35% | -3.97% | 21.47% |

동일 구간·초기 자금, 종료 시 청산 비용 포함. 노출 맞춤은 사후 설명용이며 v2 실제 계좌 성과가 아닙니다.
[낙폭 분해·비용 영향·전체 구간](CAT/comparison.json)

[v1 전체 기록](CAT/accounts.json) · [v2 전체 기록](CAT/accounts-v2.json)

## WMT 계좌

| 모델 | 전략 | 평가액 USD | 손익 USD | 최근 매매·이유 |
|---|---|---:|---:|---|
| v1 | cash | 10000.00 | 0.00 | 대기 /  / 새 신호 대기 |
| v1 | buy_hold | 10075.06 | 75.06 | buy /  / buy_hold: prior completed bar target 100%; next bar open simulation |
| v1 | trend_8_26 | 9779.58 | -220.42 | sell /  / trend_8_26: prior completed bar target 0%; next bar open simulation |
| v1 | momentum_26 | 9832.09 | -167.91 | sell /  / momentum_26: prior completed bar target 0%; next bar open simulation |
| v1 | breakout_8 | 9342.19 | -657.81 | sell /  / breakout_8: prior completed bar target 0%; next bar open simulation |
| v1 | reversion_12 | 9456.70 | -543.30 | sell /  / reversion_12: prior completed bar target 0%; next bar open simulation |
| v1 | volume_26 | 9775.35 | -224.65 | sell /  / volume_26: prior completed bar target 0%; next bar open simulation |
| v1 | trend_8_26 AND momentum_26 | 9861.19 | -138.81 | sell /  / trend_8_26 AND momentum_26: prior completed bar target 0%; next bar open simulation |
| v1 | trend_8_26 + momentum_26 | 9805.82 | -194.18 | sell /  / trend_8_26 + momentum_26: prior completed bar target 0%; next bar open simulation |
| v1 | trend_8_26 AND breakout_8 | 9602.19 | -397.81 | sell /  / trend_8_26 AND breakout_8: prior completed bar target 0%; next bar open simulation |
| v1 | trend_8_26 + breakout_8 | 9577.78 | -422.22 | sell /  / trend_8_26 + breakout_8: prior completed bar target 0%; next bar open simulation |
| v1 | trend_8_26 AND reversion_12 | 9683.74 | -316.26 | sell /  / trend_8_26 AND reversion_12: prior completed bar target 0%; next bar open simulation |
| v1 | trend_8_26 + reversion_12 | 9655.42 | -344.58 | sell /  / trend_8_26 + reversion_12: prior completed bar target 0%; next bar open simulation |
| v1 | trend_8_26 AND volume_26 | 9837.96 | -162.04 | sell /  / trend_8_26 AND volume_26: prior completed bar target 0%; next bar open simulation |
| v1 | trend_8_26 + volume_26 | 9777.89 | -222.11 | sell /  / trend_8_26 + volume_26: prior completed bar target 0%; next bar open simulation |
| v1 | momentum_26 AND breakout_8 | 9514.44 | -485.56 | sell /  / momentum_26 AND breakout_8: prior completed bar target 0%; next bar open simulation |
| v1 | momentum_26 + breakout_8 | 9642.15 | -357.85 | sell /  / momentum_26 + breakout_8: prior completed bar target 0%; next bar open simulation |
| v1 | momentum_26 AND reversion_12 | 9877.29 | -122.71 | sell /  / momentum_26 AND reversion_12: prior completed bar target 0%; next bar open simulation |
| v1 | momentum_26 + reversion_12 | 9739.38 | -260.62 | sell /  / momentum_26 + reversion_12: prior completed bar target 0%; next bar open simulation |
| v1 | momentum_26 AND volume_26 | 9853.50 | -146.50 | sell /  / momentum_26 AND volume_26: prior completed bar target 0%; next bar open simulation |
| v1 | momentum_26 + volume_26 | 9843.34 | -156.66 | sell /  / momentum_26 + volume_26: prior completed bar target 0%; next bar open simulation |
| v1 | breakout_8 AND reversion_12 | 10000.00 | 0.00 | 대기 /  / 새 신호 대기 |
| v1 | breakout_8 + reversion_12 | 9436.73 | -563.27 | sell /  / breakout_8 + reversion_12: prior completed bar target 0%; next bar open simulation |
| v1 | breakout_8 AND volume_26 | 9797.95 | -202.05 | sell /  / breakout_8 AND volume_26: prior completed bar target 0%; next bar open simulation |
| v1 | breakout_8 + volume_26 | 9556.59 | -443.41 | sell /  / breakout_8 + volume_26: prior completed bar target 0%; next bar open simulation |
| v1 | reversion_12 AND volume_26 | 9911.53 | -88.47 | sell /  / reversion_12 AND volume_26: prior completed bar target 0%; next bar open simulation |
| v1 | reversion_12 + volume_26 | 9672.66 | -327.34 | sell /  / reversion_12 + volume_26: prior completed bar target 0%; next bar open simulation |
| v1 | ema_12_26 | 9971.99 | -28.01 | sell /  / EMA12 > EMA26; 조건 미충족; EMA12=120.013, EMA26=120.022 |
| v1 | macd_12_26_9 | 10121.08 | 121.08 | sell /  / MACD > 신호선 그리고 MACD > 0; 조건 미충족; MACD=0.563738, signal9=0.568978 |
| v1 | rsi_14_recovery | 9973.19 | -26.81 | sell /  / 직전 RSI14 < 30, 현재 RSI14 >= 30 (한 봉 목표); 조건 미충족; RSI14=46.7246, previous_RSI14=43.1348 |
| v1 | bollinger_20_reentry | 9940.27 | -59.73 | sell /  / 직전 종가 < 직전 하단밴드, 현재 하단밴드 <= 종가 <= SMA20 (한 봉 목표); 조건 미충족; close=120.035, lower20=119.686, SMA20=120.446, previous_lower20=119.732 |
| v1 | donchian_20 | 9643.84 | -356.16 | sell /  / 종가 > 현재 봉을 제외한 직전 20봉 최고가; 조건 미충족; close=121.08, prior_high20=121.18 |
| v1 | atr_14_breakout | 9811.78 | -188.22 | sell /  / 종가 > 직전 종가 + 직전 ATR14 그리고 종가 > EMA26; 조건 미충족; close=120.03, threshold=120.128, prior_ATR14=0.443028, EMA26=118.335 |
| v1 | session_vwap | 9681.70 | -318.30 | sell /  / 종가 > 뉴욕 거래일별 누적 전형가격 VWAP; 조건 미충족; close=121.08, session_VWAP=121.52, session_volume=1.65503e+06 |
| v1 | obv_20 | 9894.31 | -105.69 | sell /  / OBV > OBV의 SMA20 그리고 종가 > EMA26; 조건 미충족; OBV=1.93315e+07, OBV_SMA20=1.9255e+07, close=119.98, EMA26=120.094 |
| v1 | stochastic_14_3_recovery | 9413.90 | -586.10 | sell /  / 직전 %K14 < 20에서 %K14가 %D3 상향 돌파 (한 봉 목표); 조건 미충족; K14=24.793, D3=9.99746, previous_K14=3.30586, previous_D3=3.22212 |
| v1 | mfi_14_recovery | 9969.08 | -30.92 | sell /  / 직전 MFI14 < 20, 현재 MFI14 >= 20 (한 봉 목표); 조건 미충족; MFI14=57.3162, previous_MFI14=36.5877 |
| v1 | adx_14_trend | 10064.02 | 64.02 | sell /  / Wilder ADX14 >= 25 그리고 +DI14 > -DI14; 조건 미충족; ADX14=30.1427, plus_DI14=25.9007, minus_DI14=26.0063 |
| v1 | aroon_25_trend | 9893.25 | -106.75 | sell /  / Aroon25 Up > 70 그리고 Down < 30 (동률이면 최신 극값); 조건 미충족; Aroon_up=80, Aroon_down=96 |
| v1 | cci_20_momentum | 9664.17 | -335.83 | sell /  / CCI20 > 100 (전형가격·평균절대편차); 조건 미충족; CCI20=-31.8509 |
| v1 | williams_14_recovery | 9664.50 | -335.50 | buy /  / 직전 Williams %R14 < -80, 현재 >= -80 (한 봉 목표); 조건 충족; Williams_R14=-75.207, previous_R14=-96.6941 |
| v1 | cmf_20_accumulation | 9737.44 | -262.56 | sell /  / Chaikin Money Flow20 > 0.1; 조건 미충족; CMF20=0.0930543, volume20=1.6661e+07 |
| v1 | chaikin_3_10 | 9709.84 | -290.16 | sell /  / ADL의 EMA3 - EMA10 > 0 그리고 종가 > EMA26; 조건 미충족; Chaikin3_10=76755.7, ADL=1.33628e+07, close=120.04, EMA26=120.151 |
| v1 | roc_10_momentum | 10091.95 | 91.95 | sell /  / 10봉 ROC > 1% 그리고 종가 > EMA26; 조건 미충족; ROC10_percent=0.710203, close=120.535, EMA26=119.283 |
| v1 | trix_15_trend | 9640.97 | -359.03 | sell /  / 15봉 삼중 EMA의 1봉 변화율 TRIX > 0 그리고 종가 > EMA26; 조건 미충족; TRIX15_percent=0.0327766, close=119.98, EMA26=120.094 |
| v1 | keltner_20_breakout | 9879.35 | -120.65 | sell /  / 종가 > EMA20 + 2 x Wilder ATR14; 조건 미충족; close=121.08, upper_Keltner=121.15, EMA20=120.322, ATR14=0.414113 |
| v1 | opening_range_30m | 9860.78 | -139.22 | sell /  / 뉴욕 09:30·09:45 두 완료 봉 최고가를 10:00 이후 종가가 돌파; 자료 부족·변동폭 또는 거래량 없음: 대기; close=121.08 |
| v2 | cash | 10000.00 | 0.00 | 대기 /  / 새 신호 대기 |
| v2 | buy_hold | 10674.43 | 674.43 | buy / partial / 직전 완료 봉 목표 비중 100%; 다음 봉 시가 가정 |
| v2 | trend_8_26 | 10170.98 | 170.98 | sell / filled / 직전 완료 봉 목표 비중 0%; 다음 봉 시가 가정 |
| v2 | momentum_26 | 10228.38 | 228.38 | sell / filled / 직전 완료 봉 목표 비중 0%; 다음 봉 시가 가정 |
| v2 | breakout_8 | 9296.17 | -703.83 | 중단: 손실 한도 / sell / filled / 직전 완료 봉 목표 비중 0%; 다음 봉 시가 가정 |
| v2 | reversion_12 | 9346.73 | -653.27 | sell / filled / 직전 완료 봉 목표 비중 0%; 다음 봉 시가 가정 |
| v2 | volume_26 | 9727.78 | -272.22 | sell / filled / 직전 완료 봉 목표 비중 0%; 다음 봉 시가 가정 |
| v2 | trend_8_26 AND momentum_26 | 10255.85 | 255.85 | sell / filled / 직전 완료 봉 목표 비중 0%; 다음 봉 시가 가정 |
| v2 | trend_8_26 + momentum_26 | 10199.60 | 199.60 | sell / filled / 직전 완료 봉 목표 비중 0%; 다음 봉 시가 가정 |
| v2 | trend_8_26 AND breakout_8 | 9667.87 | -332.13 | sell / filled / 직전 완료 봉 목표 비중 0%; 다음 봉 시가 가정 |
| v2 | trend_8_26 + breakout_8 | 9736.05 | -263.95 | sell / filled / 직전 완료 봉 목표 비중 0%; 다음 봉 시가 가정 |
| v2 | trend_8_26 AND reversion_12 | 9487.14 | -512.86 | sell / filled / 직전 완료 봉 목표 비중 0%; 다음 봉 시가 가정 |
| v2 | trend_8_26 + reversion_12 | 9792.62 | -207.38 | sell / filled / 직전 완료 봉 목표 비중 0%; 다음 봉 시가 가정 |
| v2 | trend_8_26 AND volume_26 | 9784.10 | -215.90 | sell / filled / 직전 완료 봉 목표 비중 0%; 다음 봉 시가 가정 |
| v2 | trend_8_26 + volume_26 | 9948.73 | -51.27 | sell / filled / 직전 완료 봉 목표 비중 0%; 다음 봉 시가 가정 |
| v2 | momentum_26 AND breakout_8 | 9475.14 | -524.86 | 중단: 손실 한도 / sell / filled / 직전 완료 봉 목표 비중 0%; 다음 봉 시가 가정 |
| v2 | momentum_26 + breakout_8 | 9804.78 | -195.22 | sell / filled / 직전 완료 봉 목표 비중 0%; 다음 봉 시가 가정 |
| v2 | momentum_26 AND reversion_12 | 9700.42 | -299.58 | sell / filled / 직전 완료 봉 목표 비중 0%; 다음 봉 시가 가정 |
| v2 | momentum_26 + reversion_12 | 9923.75 | -76.25 | sell / filled / 직전 완료 봉 목표 비중 0%; 다음 봉 시가 가정 |
| v2 | momentum_26 AND volume_26 | 9760.78 | -239.22 | sell / filled / 직전 완료 봉 목표 비중 0%; 다음 봉 시가 가정 |
| v2 | momentum_26 + volume_26 | 10018.75 | 18.75 | sell / filled / 직전 완료 봉 목표 비중 0%; 다음 봉 시가 가정 |
| v2 | breakout_8 AND reversion_12 | 10000.00 | 0.00 | 대기 /  / 새 신호 대기 |
| v2 | breakout_8 + reversion_12 | 9372.70 | -627.30 | sell / filled / 직전 완료 봉 목표 비중 0%; 다음 봉 시가 가정 |
| v2 | breakout_8 AND volume_26 | 9741.39 | -258.61 | sell / filled / 직전 완료 봉 목표 비중 0%; 다음 봉 시가 가정 |
| v2 | breakout_8 + volume_26 | 9502.52 | -497.48 | sell / filled / 직전 완료 봉 목표 비중 0%; 다음 봉 시가 가정 |
| v2 | reversion_12 AND volume_26 | 9917.25 | -82.75 | sell / filled / 직전 완료 봉 목표 비중 0%; 다음 봉 시가 가정 |
| v2 | reversion_12 + volume_26 | 9595.57 | -404.43 | sell / filled / 직전 완료 봉 목표 비중 0%; 다음 봉 시가 가정 |
| v2 | ema_12_26 | 9966.01 | -33.99 | sell / filled / EMA12 > EMA26; 조건 미충족; EMA12=120.013, EMA26=120.022; 직전 완료 봉 목표를 다음 봉 시가에 모의 적용 |
| v2 | macd_12_26_9 | 10115.01 | 115.01 | sell / filled / MACD > 신호선 그리고 MACD > 0; 조건 미충족; MACD=0.563738, signal9=0.568978; 직전 완료 봉 목표를 다음 봉 시가에 모의 적용 |
| v2 | rsi_14_recovery | 9971.19 | -28.81 | sell / filled / 직전 RSI14 < 30, 현재 RSI14 >= 30 (한 봉 목표); 조건 미충족; RSI14=46.7246, previous_RSI14=43.1348; 직전 완료 봉 목표를 다음 봉 시가에 모의 적용 |
| v2 | bollinger_20_reentry | 9930.34 | -69.66 | sell / filled / 직전 종가 < 직전 하단밴드, 현재 하단밴드 <= 종가 <= SMA20 (한 봉 목표); 조건 미충족; close=120.035, lower20=119.686, SMA20=120.446, previous_lower20=119.732; 직전 완료 봉 목표를 다음 봉 시가에 모의 적용 |
| v2 | donchian_20 | 9630.34 | -369.66 | sell / filled / 종가 > 현재 봉을 제외한 직전 20봉 최고가; 조건 미충족; close=121.08, prior_high20=121.18; 직전 완료 봉 목표를 다음 봉 시가에 모의 적용 |
| v2 | atr_14_breakout | 9801.98 | -198.02 | sell / filled / 종가 > 직전 종가 + 직전 ATR14 그리고 종가 > EMA26; 조건 미충족; close=120.03, threshold=120.128, prior_ATR14=0.443028, EMA26=118.335; 직전 완료 봉 목표를 다음 봉 시가에 모의 적용 |
| v2 | session_vwap | 9660.42 | -339.58 | sell / filled / 종가 > 뉴욕 거래일별 누적 전형가격 VWAP; 조건 미충족; close=121.08, session_VWAP=121.52, session_volume=1.65503e+06; 직전 완료 봉 목표를 다음 봉 시가에 모의 적용 |
| v2 | obv_20 | 9880.47 | -119.53 | sell / filled / OBV > OBV의 SMA20 그리고 종가 > EMA26; 조건 미충족; OBV=1.93315e+07, OBV_SMA20=1.9255e+07, close=119.98, EMA26=120.094; 직전 완료 봉 목표를 다음 봉 시가에 모의 적용 |
| v2 | stochastic_14_3_recovery | 9776.03 | -223.97 | 중단: 손실 한도 / buy / partial / 직전 %K14 < 20에서 %K14가 %D3 상향 돌파 (한 봉 목표); 조건 충족; K14=25.6758, D3=22.4971, previous_K14=12.8379, previous_D3=25.8704; 직전 완료 봉 목표를 다음 봉 시가에 모의 적용 |
| v2 | mfi_14_recovery | 9961.11 | -38.89 | sell / filled / 직전 MFI14 < 20, 현재 MFI14 >= 20 (한 봉 목표); 조건 미충족; MFI14=57.3162, previous_MFI14=36.5877; 직전 완료 봉 목표를 다음 봉 시가에 모의 적용 |
| v2 | adx_14_trend | 10059.99 | 59.99 | sell / filled / Wilder ADX14 >= 25 그리고 +DI14 > -DI14; 조건 미충족; ADX14=30.1427, plus_DI14=25.9007, minus_DI14=26.0063; 직전 완료 봉 목표를 다음 봉 시가에 모의 적용 |
| v2 | aroon_25_trend | 9885.34 | -114.66 | sell / filled / Aroon25 Up > 70 그리고 Down < 30 (동률이면 최신 극값); 조건 미충족; Aroon_up=80, Aroon_down=96; 직전 완료 봉 목표를 다음 봉 시가에 모의 적용 |
| v2 | cci_20_momentum | 9650.65 | -349.35 | sell / filled / CCI20 > 100 (전형가격·평균절대편차); 조건 미충족; CCI20=-31.8509; 직전 완료 봉 목표를 다음 봉 시가에 모의 적용 |
| v2 | williams_14_recovery | 9648.08 | -351.92 | buy / partial / 직전 Williams %R14 < -80, 현재 >= -80 (한 봉 목표); 조건 충족; Williams_R14=-75.207, previous_R14=-96.6941; 직전 완료 봉 목표를 다음 봉 시가에 모의 적용 |
| v2 | cmf_20_accumulation | 9723.82 | -276.18 | sell / filled / Chaikin Money Flow20 > 0.1; 조건 미충족; CMF20=0.0930543, volume20=1.6661e+07; 직전 완료 봉 목표를 다음 봉 시가에 모의 적용 |
| v2 | chaikin_3_10 | 9690.44 | -309.56 | sell / filled / ADL의 EMA3 - EMA10 > 0 그리고 종가 > EMA26; 조건 미충족; Chaikin3_10=76755.7, ADL=1.33628e+07, close=120.04, EMA26=120.151; 직전 완료 봉 목표를 다음 봉 시가에 모의 적용 |
| v2 | roc_10_momentum | 10089.93 | 89.93 | sell / filled / 10봉 ROC > 1% 그리고 종가 > EMA26; 조건 미충족; ROC10_percent=0.710203, close=120.535, EMA26=119.283; 직전 완료 봉 목표를 다음 봉 시가에 모의 적용 |
| v2 | trix_15_trend | 9625.56 | -374.44 | sell / filled / 15봉 삼중 EMA의 1봉 변화율 TRIX > 0 그리고 종가 > EMA26; 조건 미충족; TRIX15_percent=0.0327766, close=119.98, EMA26=120.094; 직전 완료 봉 목표를 다음 봉 시가에 모의 적용 |
| v2 | keltner_20_breakout | 9871.45 | -128.55 | sell / filled / 종가 > EMA20 + 2 x Wilder ATR14; 조건 미충족; close=121.08, upper_Keltner=121.15, EMA20=120.322, ATR14=0.414113; 직전 완료 봉 목표를 다음 봉 시가에 모의 적용 |
| v2 | opening_range_30m | 9850.92 | -149.08 | sell / filled / 뉴욕 09:30·09:45 두 완료 봉 최고가를 10:00 이후 종가가 돌파; 자료 부족·변동폭 또는 거래량 없음: 대기; close=121.08; 직전 완료 봉 목표를 다음 봉 시가에 모의 적용 |

### 같은 기간의 비용·노출 비교 (사후 연구)

| 전략 | 비용 전 | 비용 후 | 100% 보유 | 같은 평균 노출 보유 | 평균 노출 |
|---|---:|---:|---:|---:|---:|
| cash | 0.00% | 0.00% | 14.67% | 0.00% | 0.00% |
| buy_hold | 15.15% | 14.67% | 14.67% | 14.67% | 100.00% |
| trend_8_26 | 10.14% | 6.50% | 14.67% | 10.47% | 73.30% |
| momentum_26 | 13.96% | 9.27% | 14.67% | 11.08% | 77.23% |
| breakout_8 | 6.46% | -11.87% | 14.67% | 3.83% | 28.01% |
| reversion_12 | 2.75% | -7.10% | 14.67% | 2.45% | 18.06% |
| volume_26 | 2.67% | -2.38% | 14.67% | 0.67% | 4.97% |
| trend_8_26 AND momentum_26 | 11.05% | 7.39% | 14.67% | 9.76% | 68.59% |
| trend_8_26 + momentum_26 | 12.03% | 7.88% | 14.67% | 10.78% | 75.26% |
| trend_8_26 AND breakout_8 | 6.87% | -8.51% | 14.67% | 3.25% | 23.82% |
| trend_8_26 + breakout_8 | 8.30% | -2.91% | 14.67% | 7.08% | 50.66% |
| trend_8_26 AND reversion_12 | -0.82% | -6.48% | 14.67% | 0.98% | 7.33% |
| trend_8_26 + reversion_12 | 6.42% | -0.10% | 14.67% | 6.36% | 45.68% |
| trend_8_26 AND volume_26 | 0.13% | -1.95% | 14.67% | 0.24% | 1.83% |
| trend_8_26 + volume_26 | 6.38% | 2.19% | 14.67% | 5.41% | 39.14% |
| momentum_26 AND breakout_8 | 6.71% | -10.17% | 14.67% | 3.58% | 26.18% |
| momentum_26 + breakout_8 | 10.17% | -1.23% | 14.67% | 7.37% | 52.62% |
| momentum_26 AND reversion_12 | 1.67% | -3.74% | 14.67% | 1.05% | 7.85% |
| momentum_26 + reversion_12 | 8.25% | 2.26% | 14.67% | 6.64% | 47.65% |
| momentum_26 AND volume_26 | 1.72% | -2.05% | 14.67% | 0.35% | 2.62% |
| momentum_26 + volume_26 | 8.21% | 3.73% | 14.67% | 5.69% | 41.10% |
| breakout_8 AND reversion_12 | 0.00% | 0.00% | 14.67% | 0.00% | 0.00% |
| breakout_8 + reversion_12 | 4.62% | -8.94% | 14.67% | 3.14% | 23.05% |
| breakout_8 AND volume_26 | 0.69% | -2.22% | 14.67% | 0.28% | 2.09% |
| breakout_8 + volume_26 | 4.58% | -7.04% | 14.67% | 2.23% | 16.50% |
| reversion_12 AND volume_26 | 0.43% | -0.83% | 14.67% | 0.14% | 1.05% |
| reversion_12 + volume_26 | 2.72% | -3.97% | 14.67% | 1.55% | 11.52% |
| ema_12_26 | 12.38% | 10.51% | 14.67% | 11.85% | 82.20% |
| macd_12_26_9 | 10.59% | 6.04% | 14.67% | 5.66% | 40.84% |
| rsi_14_recovery | 0.20% | -0.64% | 14.67% | 0.07% | 0.52% |
| bollinger_20_reentry | 1.82% | -0.72% | 14.67% | 0.21% | 1.57% |
| donchian_20 | 4.01% | -9.83% | 14.67% | 1.98% | 14.66% |
| atr_14_breakout | -0.01% | -9.97% | 14.67% | 1.02% | 7.59% |
| session_vwap | 11.69% | 1.40% | 14.67% | 8.57% | 60.73% |
| obv_20 | 12.22% | 4.48% | 14.67% | 8.93% | 63.09% |
| stochastic_14_3_recovery | -0.07% | -8.50% | 14.67% | 0.74% | 5.50% |
| mfi_14_recovery | 1.30% | -0.39% | 14.67% | 0.14% | 1.05% |
| adx_14_trend | 9.95% | 7.22% | 14.67% | 8.38% | 59.42% |
| aroon_25_trend | 8.13% | 2.81% | 14.67% | 4.68% | 34.03% |
| cci_20_momentum | 6.82% | -3.01% | 14.67% | 4.98% | 36.13% |
| williams_14_recovery | 0.81% | -6.53% | 14.67% | 0.63% | 4.71% |
| cmf_20_accumulation | 9.26% | 0.88% | 14.67% | 6.19% | 44.50% |
| chaikin_3_10 | 10.62% | 1.28% | 14.67% | 8.22% | 58.38% |
| roc_10_momentum | 1.03% | -3.94% | 14.67% | 2.30% | 17.02% |
| trix_15_trend | 11.09% | 6.07% | 14.67% | 10.19% | 71.47% |
| keltner_20_breakout | 7.26% | -0.55% | 14.67% | 4.20% | 30.63% |
| opening_range_30m | 11.01% | 4.67% | 14.67% | 5.92% | 42.67% |

동일 구간·초기 자금, 종료 시 청산 비용 포함. 노출 맞춤은 사후 설명용이며 v2 실제 계좌 성과가 아닙니다.
[낙폭 분해·비용 영향·전체 구간](WMT/comparison.json)

[v1 전체 기록](WMT/accounts.json) · [v2 전체 기록](WMT/accounts-v2.json)
