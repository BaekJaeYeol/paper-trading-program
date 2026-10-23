# 모의투자 운영 현황

[PC·서버 장애 진단과 복구 방법](https://github.com/BaekJaeYeol/paper-trading-program/blob/main/investment-lab/docs/failure-recovery.md)

이번 실행 복구: {}

완료 봉 확인 주기: 기록 14/22회 · 기록 없는 예정 8회 · 아직 판정 전 4회 · 주의: 예약 시작 지연 또는 실행·저장 누락을 확인하세요.

[주기 판정 기준](https://github.com/BaekJaeYeol/paper-trading-program/blob/main/investment-lab/docs/session-coverage.md)

최근 확인: 2026-10-23T19:22:00.351664+00:00 (UTC)
다음 15분 확인 목표 (세션 실행 중에만 적용): 2026-10-23T19:37:00+00:00 (UTC, 실행 지연 가능)

실제 주문 없음. v1 기존 계좌와 v2 새 계좌의 시작일이 다르므로 수익률을 직접 우열 비교하지 마세요.
v2는 다음 봉 시가에 비용·스프레드·직전 거래량 제한을 적용한 가상 체결입니다. 미체결 잔량은 만료됩니다.

| 종목 | 상태 | 최근 성공 UTC | 마지막 완료 봉 UTC | 이번 새 봉 |
|---|---|---|---|---|
| SPY | updated | 2026-10-23T19:22:00.351664+00:00 | 2026-10-23T19:00:00+00:00 | 1 |
| QQQ | updated | 2026-10-23T19:22:00.351664+00:00 | 2026-10-23T19:00:00+00:00 | 1 |
| IWM | updated | 2026-10-23T19:22:00.351664+00:00 | 2026-10-23T19:00:00+00:00 | 1 |
| DIA | updated | 2026-10-23T19:22:00.351664+00:00 | 2026-10-23T19:00:00+00:00 | 1 |
| MSFT | updated | 2026-10-23T19:22:00.351664+00:00 | 2026-10-23T19:00:00+00:00 | 1 |
| JPM | updated | 2026-10-23T19:22:00.351664+00:00 | 2026-10-23T19:00:00+00:00 | 1 |
| XOM | updated | 2026-10-23T19:22:00.351664+00:00 | 2026-10-23T19:00:00+00:00 | 1 |
| JNJ | updated | 2026-10-23T19:22:00.351664+00:00 | 2026-10-23T19:00:00+00:00 | 1 |
| CAT | updated | 2026-10-23T19:22:00.351664+00:00 | 2026-10-23T19:00:00+00:00 | 1 |
| WMT | updated | 2026-10-23T19:22:00.351664+00:00 | 2026-10-23T19:00:00+00:00 | 1 |

이번 실행 소요: 51.17초
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
| v1 | buy_hold | 9817.53 | -182.47 | buy /  / buy_hold: prior completed bar target 100%; next bar open simulation |
| v1 | trend_8_26 | 9657.97 | -342.03 | sell /  / trend_8_26: prior completed bar target 0%; next bar open simulation |
| v1 | momentum_26 | 9631.54 | -368.46 | sell /  / momentum_26: prior completed bar target 0%; next bar open simulation |
| v1 | breakout_8 | 9427.76 | -572.24 | sell /  / breakout_8: prior completed bar target 0%; next bar open simulation |
| v1 | reversion_12 | 9454.44 | -545.56 | sell /  / reversion_12: prior completed bar target 0%; next bar open simulation |
| v1 | volume_26 | 9279.89 | -720.11 | sell /  / volume_26: prior completed bar target 0%; next bar open simulation |
| v1 | trend_8_26 AND momentum_26 | 9624.28 | -375.72 | sell /  / trend_8_26 AND momentum_26: prior completed bar target 0%; next bar open simulation |
| v1 | trend_8_26 + momentum_26 | 9644.71 | -355.29 | sell /  / trend_8_26 + momentum_26: prior completed bar target 0%; next bar open simulation |
| v1 | trend_8_26 AND breakout_8 | 9730.71 | -269.29 | sell /  / trend_8_26 AND breakout_8: prior completed bar target 0%; next bar open simulation |
| v1 | trend_8_26 + breakout_8 | 9580.32 | -419.68 | sell /  / trend_8_26 + breakout_8: prior completed bar target 0%; next bar open simulation |
| v1 | trend_8_26 AND reversion_12 | 9736.23 | -263.77 | sell /  / trend_8_26 AND reversion_12: prior completed bar target 0%; next bar open simulation |
| v1 | trend_8_26 + reversion_12 | 9574.56 | -425.44 | sell /  / trend_8_26 + reversion_12: prior completed bar target 0%; next bar open simulation |
| v1 | trend_8_26 AND volume_26 | 9605.36 | -394.64 | sell /  / trend_8_26 AND volume_26: prior completed bar target 0%; next bar open simulation |
| v1 | trend_8_26 + volume_26 | 9466.84 | -533.16 | sell /  / trend_8_26 + volume_26: prior completed bar target 0%; next bar open simulation |
| v1 | momentum_26 AND breakout_8 | 9640.01 | -359.99 | sell /  / momentum_26 AND breakout_8: prior completed bar target 0%; next bar open simulation |
| v1 | momentum_26 + breakout_8 | 9529.11 | -470.89 | sell /  / momentum_26 + breakout_8: prior completed bar target 0%; next bar open simulation |
| v1 | momentum_26 AND reversion_12 | 9769.70 | -230.30 | sell /  / momentum_26 AND reversion_12: prior completed bar target 0%; next bar open simulation |
| v1 | momentum_26 + reversion_12 | 9599.82 | -400.18 | sell /  / momentum_26 + reversion_12: prior completed bar target 0%; next bar open simulation |
| v1 | momentum_26 AND volume_26 | 9618.73 | -381.27 | sell /  / momentum_26 AND volume_26: prior completed bar target 0%; next bar open simulation |
| v1 | momentum_26 + volume_26 | 9453.89 | -546.11 | sell /  / momentum_26 + volume_26: prior completed bar target 0%; next bar open simulation |
| v1 | breakout_8 AND reversion_12 | 10000.00 | 0.00 | 대기 /  / 새 신호 대기 |
| v1 | breakout_8 + reversion_12 | 9478.47 | -521.53 | sell /  / breakout_8 + reversion_12: prior completed bar target 0%; next bar open simulation |
| v1 | breakout_8 AND volume_26 | 9807.14 | -192.86 | sell /  / breakout_8 AND volume_26: prior completed bar target 0%; next bar open simulation |
| v1 | breakout_8 + volume_26 | 9390.66 | -609.34 | sell /  / breakout_8 + volume_26: prior completed bar target 0%; next bar open simulation |
| v1 | reversion_12 AND volume_26 | 9811.81 | -188.19 | sell /  / reversion_12 AND volume_26: prior completed bar target 0%; next bar open simulation |
| v1 | reversion_12 + volume_26 | 9460.54 | -539.46 | sell /  / reversion_12 + volume_26: prior completed bar target 0%; next bar open simulation |
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
| v1 | cmf_20_accumulation | 9618.40 | -381.60 | sell /  / Chaikin Money Flow20 > 0.1; 조건 미충족; CMF20=0.0788449, volume20=7.16991e+07 |
| v1 | chaikin_3_10 | 9518.83 | -481.17 | sell /  / ADL의 EMA3 - EMA10 > 0 그리고 종가 > EMA26; 조건 미충족; Chaikin3_10=2.35994e+06, ADL=6.37828e+07, close=762.39, EMA26=762.974 |
| v1 | roc_10_momentum | 9953.42 | -46.58 | sell /  / 10봉 ROC > 1% 그리고 종가 > EMA26; 조건 미충족; ROC10_percent=0.806376, close=769.45, EMA26=767.181 |
| v1 | trix_15_trend | 9489.99 | -510.01 | sell /  / 15봉 삼중 EMA의 1봉 변화율 TRIX > 0 그리고 종가 > EMA26; 조건 미충족; TRIX15_percent=0.0154379, close=766.62, EMA26=771.893 |
| v1 | keltner_20_breakout | 9810.90 | -189.10 | sell /  / 종가 > EMA20 + 2 x Wilder ATR14; 조건 미충족; close=774.19, upper_Keltner=774.31, EMA20=772.615, ATR14=0.847257 |
| v1 | opening_range_30m | 9598.85 | -401.15 | sell /  / 뉴욕 09:30·09:45 두 완료 봉 최고가를 10:00 이후 종가가 돌파; 조건 미충족; close=760.59, opening_high=761.2 |
| v2 | cash | 10000.00 | 0.00 | 대기 /  / 새 신호 대기 |
| v2 | buy_hold | 9746.72 | -253.28 | buy / partial / 직전 완료 봉 목표 비중 100%; 다음 봉 시가 가정 |
| v2 | trend_8_26 | 9536.87 | -463.13 | sell / filled / 직전 완료 봉 목표 비중 0%; 다음 봉 시가 가정 |
| v2 | momentum_26 | 9482.22 | -517.78 | sell / filled / 직전 완료 봉 목표 비중 0%; 다음 봉 시가 가정 |
| v2 | breakout_8 | 9024.03 | -975.97 | sell / filled / 직전 완료 봉 목표 비중 0%; 다음 봉 시가 가정 |
| v2 | reversion_12 | 9002.21 | -997.79 | 중단: 손실 한도 / buy / partial / 직전 완료 봉 목표 비중 100%; 다음 봉 시가 가정 |
| v2 | volume_26 | 8959.62 | -1040.38 | 중단: 손실 한도 / buy / partial / 직전 완료 봉 목표 비중 100%; 다음 봉 시가 가정 |
| v2 | trend_8_26 AND momentum_26 | 9481.53 | -518.47 | sell / filled / 직전 완료 봉 목표 비중 0%; 다음 봉 시가 가정 |
| v2 | trend_8_26 + momentum_26 | 9509.48 | -490.52 | sell / filled / 직전 완료 봉 목표 비중 0%; 다음 봉 시가 가정 |
| v2 | trend_8_26 AND breakout_8 | 9547.25 | -452.75 | sell / filled / 직전 완료 봉 목표 비중 0%; 다음 봉 시가 가정 |
| v2 | trend_8_26 + breakout_8 | 9315.73 | -684.27 | sell / filled / 직전 완료 봉 목표 비중 0%; 다음 봉 시가 가정 |
| v2 | trend_8_26 AND reversion_12 | 9621.61 | -378.39 | sell / filled / 직전 완료 봉 목표 비중 0%; 다음 봉 시가 가정 |
| v2 | trend_8_26 + reversion_12 | 9278.51 | -721.49 | sell / filled / 직전 완료 봉 목표 비중 0%; 다음 봉 시가 가정 |
| v2 | trend_8_26 AND volume_26 | 9442.22 | -557.78 | sell / filled / 직전 완료 봉 목표 비중 0%; 다음 봉 시가 가정 |
| v2 | trend_8_26 + volume_26 | 9144.22 | -855.78 | sell / filled / 직전 완료 봉 목표 비중 0%; 다음 봉 시가 가정 |
| v2 | momentum_26 AND breakout_8 | 9414.38 | -585.62 | sell / filled / 직전 완료 봉 목표 비중 0%; 다음 봉 시가 가정 |
| v2 | momentum_26 + breakout_8 | 9250.22 | -749.78 | sell / filled / 직전 완료 봉 목표 비중 0%; 다음 봉 시가 가정 |
| v2 | momentum_26 AND reversion_12 | 9722.08 | -277.92 | sell / filled / 직전 완료 봉 목표 비중 0%; 다음 봉 시가 가정 |
| v2 | momentum_26 + reversion_12 | 9310.42 | -689.58 | sell / filled / 직전 완료 봉 목표 비중 0%; 다음 봉 시가 가정 |
| v2 | momentum_26 AND volume_26 | 9523.88 | -476.12 | sell / filled / 직전 완료 봉 목표 비중 0%; 다음 봉 시가 가정 |
| v2 | momentum_26 + volume_26 | 9156.34 | -843.66 | sell / filled / 직전 완료 봉 목표 비중 0%; 다음 봉 시가 가정 |
| v2 | breakout_8 AND reversion_12 | 10000.00 | 0.00 | 대기 /  / 새 신호 대기 |
| v2 | breakout_8 + reversion_12 | 9082.29 | -917.71 | sell / filled / 직전 완료 봉 목표 비중 0%; 다음 봉 시가 가정 |
| v2 | breakout_8 AND volume_26 | 9733.81 | -266.19 | sell / filled / 직전 완료 봉 목표 비중 0%; 다음 봉 시가 가정 |
| v2 | breakout_8 + volume_26 | 8990.64 | -1009.36 | 중단: 손실 한도 / sell / filled / 직전 완료 봉 목표 비중 0%; 다음 봉 시가 가정 |
| v2 | reversion_12 AND volume_26 | 9552.33 | -447.67 | sell / filled / 직전 완료 봉 목표 비중 0%; 다음 봉 시가 가정 |
| v2 | reversion_12 + volume_26 | 9028.58 | -971.42 | sell / filled / 직전 완료 봉 목표 비중 0%; 다음 봉 시가 가정 |
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
| v2 | cmf_20_accumulation | 9606.87 | -393.13 | sell / filled / Chaikin Money Flow20 > 0.1; 조건 미충족; CMF20=0.0788449, volume20=7.16991e+07; 직전 완료 봉 목표를 다음 봉 시가에 모의 적용 |
| v2 | chaikin_3_10 | 9501.71 | -498.29 | sell / filled / ADL의 EMA3 - EMA10 > 0 그리고 종가 > EMA26; 조건 미충족; Chaikin3_10=2.35994e+06, ADL=6.37828e+07, close=762.39, EMA26=762.974; 직전 완료 봉 목표를 다음 봉 시가에 모의 적용 |
| v2 | roc_10_momentum | 9951.43 | -48.57 | sell / filled / 10봉 ROC > 1% 그리고 종가 > EMA26; 조건 미충족; ROC10_percent=0.806376, close=769.45, EMA26=767.181; 직전 완료 봉 목표를 다음 봉 시가에 모의 적용 |
| v2 | trix_15_trend | 9472.93 | -527.07 | sell / filled / 15봉 삼중 EMA의 1봉 변화율 TRIX > 0 그리고 종가 > EMA26; 조건 미충족; TRIX15_percent=0.0154379, close=766.62, EMA26=771.893; 직전 완료 봉 목표를 다음 봉 시가에 모의 적용 |
| v2 | keltner_20_breakout | 9803.05 | -196.95 | sell / filled / 종가 > EMA20 + 2 x Wilder ATR14; 조건 미충족; close=774.19, upper_Keltner=774.31, EMA20=772.615, ATR14=0.847257; 직전 완료 봉 목표를 다음 봉 시가에 모의 적용 |
| v2 | opening_range_30m | 9585.42 | -414.58 | sell / filled / 뉴욕 09:30·09:45 두 완료 봉 최고가를 10:00 이후 종가가 돌파; 조건 미충족; close=760.59, opening_high=761.2; 직전 완료 봉 목표를 다음 봉 시가에 모의 적용 |

### 같은 기간의 비용·노출 비교 (사후 연구)

| 전략 | 비용 전 | 비용 후 | 100% 보유 | 같은 평균 노출 보유 | 평균 노출 |
|---|---:|---:|---:|---:|---:|
| cash | 0.00% | 0.00% | -1.97% | -0.00% | 0.00% |
| buy_hold | -1.56% | -1.97% | -1.97% | -1.97% | 100.00% |
| trend_8_26 | -0.70% | -4.39% | -1.97% | -0.97% | 49.09% |
| momentum_26 | -1.38% | -5.44% | -1.97% | -0.94% | 47.78% |
| breakout_8 | -0.37% | -16.48% | -1.97% | -0.44% | 22.45% |
| reversion_12 | -1.03% | -12.38% | -1.97% | -0.57% | 28.72% |
| volume_26 | -1.18% | -12.52% | -1.97% | -0.21% | 10.70% |
| trend_8_26 AND momentum_26 | -0.59% | -4.68% | -1.97% | -0.82% | 41.78% |
| trend_8_26 + momentum_26 | -1.04% | -4.91% | -1.97% | -0.96% | 48.44% |
| trend_8_26 AND breakout_8 | 0.17% | -10.56% | -1.97% | -0.28% | 14.36% |
| trend_8_26 + breakout_8 | -0.53% | -10.26% | -1.97% | -0.71% | 35.78% |
| trend_8_26 AND reversion_12 | 0.20% | -4.32% | -1.97% | -0.12% | 6.27% |
| trend_8_26 + reversion_12 | -0.86% | -8.09% | -1.97% | -0.77% | 38.91% |
| trend_8_26 AND volume_26 | -1.05% | -6.30% | -1.97% | -0.11% | 5.48% |
| trend_8_26 + volume_26 | -0.94% | -8.55% | -1.97% | -0.59% | 29.90% |
| momentum_26 AND breakout_8 | 0.17% | -10.94% | -1.97% | -0.30% | 15.14% |
| momentum_26 + breakout_8 | -0.87% | -11.13% | -1.97% | -0.69% | 35.12% |
| momentum_26 AND reversion_12 | -0.39% | -4.89% | -1.97% | -0.12% | 6.01% |
| momentum_26 + reversion_12 | -1.20% | -8.22% | -1.97% | -0.75% | 38.26% |
| momentum_26 AND volume_26 | -0.79% | -5.27% | -1.97% | -0.08% | 3.92% |
| momentum_26 + volume_26 | -1.28% | -8.28% | -1.97% | -0.58% | 29.25% |
| breakout_8 AND reversion_12 | 0.00% | 0.00% | -1.97% | -0.00% | 0.00% |
| breakout_8 + reversion_12 | -0.70% | -13.75% | -1.97% | -0.51% | 25.60% |
| breakout_8 AND volume_26 | -0.26% | -3.15% | -1.97% | -0.05% | 2.35% |
| breakout_8 + volume_26 | -0.78% | -13.99% | -1.97% | -0.33% | 16.59% |
| reversion_12 AND volume_26 | -0.97% | -5.05% | -1.97% | -0.07% | 3.66% |
| reversion_12 + volume_26 | -1.11% | -11.35% | -1.97% | -0.39% | 19.72% |
| ema_12_26 | -1.57% | -4.82% | -1.97% | -1.00% | 50.65% |
| macd_12_26_9 | -0.46% | -4.95% | -1.97% | -0.62% | 31.33% |
| rsi_14_recovery | -0.42% | -3.71% | -1.97% | -0.04% | 2.09% |
| bollinger_20_reentry | -0.89% | -6.94% | -1.97% | -0.08% | 3.92% |
| donchian_20 | 0.12% | -7.94% | -1.97% | -0.14% | 7.05% |
| atr_14_breakout | 0.35% | -4.58% | -1.97% | -0.07% | 3.39% |
| session_vwap | -0.78% | -11.42% | -1.97% | -0.94% | 47.78% |
| obv_20 | -1.30% | -10.01% | -1.97% | -0.69% | 34.73% |
| stochastic_14_3_recovery | 0.64% | -14.20% | -1.97% | -0.20% | 9.92% |
| mfi_14_recovery | 0.11% | -2.79% | -1.97% | -0.04% | 1.83% |
| adx_14_trend | 1.03% | -0.65% | -1.97% | -0.43% | 21.93% |
| aroon_25_trend | 0.13% | -2.36% | -1.97% | -0.46% | 23.24% |
| cci_20_momentum | 0.10% | -7.58% | -1.97% | -0.41% | 20.89% |
| williams_14_recovery | 0.50% | -11.77% | -1.97% | -0.16% | 8.09% |
| cmf_20_accumulation | 0.26% | -4.67% | -1.97% | -0.97% | 49.09% |
| chaikin_3_10 | -0.27% | -7.53% | -1.97% | -0.75% | 37.86% |
| roc_10_momentum | -0.07% | -0.49% | -1.97% | -0.01% | 0.26% |
| trix_15_trend | -1.41% | -6.65% | -1.97% | -0.75% | 38.12% |
| keltner_20_breakout | 0.10% | -4.02% | -1.97% | -0.21% | 10.44% |
| opening_range_30m | -0.36% | -6.45% | -1.97% | -0.85% | 43.08% |

동일 구간·초기 자금, 종료 시 청산 비용 포함. 노출 맞춤은 사후 설명용이며 v2 실제 계좌 성과가 아닙니다.
[낙폭 분해·비용 영향·전체 구간](SPY/comparison.json)

[v1 전체 기록](SPY/accounts.json) · [v2 전체 기록](SPY/accounts-v2.json)

## QQQ 계좌

| 모델 | 전략 | 평가액 USD | 손익 USD | 최근 매매·이유 |
|---|---|---:|---:|---|
| v1 | cash | 10000.00 | 0.00 | 대기 /  / 새 신호 대기 |
| v1 | buy_hold | 9697.18 | -302.82 | buy /  / buy_hold: prior completed bar target 100%; next bar open simulation |
| v1 | trend_8_26 | 9617.69 | -382.31 | sell /  / trend_8_26: prior completed bar target 0%; next bar open simulation |
| v1 | momentum_26 | 9250.81 | -749.19 | buy /  / momentum_26: prior completed bar target 100%; next bar open simulation |
| v1 | breakout_8 | 9463.64 | -536.36 | sell /  / breakout_8: prior completed bar target 0%; next bar open simulation |
| v1 | reversion_12 | 9462.53 | -537.47 | buy /  / reversion_12: prior completed bar target 100%; next bar open simulation |
| v1 | volume_26 | 9446.81 | -553.19 | sell /  / volume_26: prior completed bar target 0%; next bar open simulation |
| v1 | trend_8_26 AND momentum_26 | 9594.04 | -405.96 | sell /  / trend_8_26 AND momentum_26: prior completed bar target 0%; next bar open simulation |
| v1 | trend_8_26 + momentum_26 | 9470.33 | -529.67 | sell /  / trend_8_26 + momentum_26: prior completed bar target 50%; next bar open simulation |
| v1 | trend_8_26 AND breakout_8 | 9893.81 | -106.19 | sell /  / trend_8_26 AND breakout_8: prior completed bar target 0%; next bar open simulation |
| v1 | trend_8_26 + breakout_8 | 9597.94 | -402.06 | sell /  / trend_8_26 + breakout_8: prior completed bar target 0%; next bar open simulation |
| v1 | trend_8_26 AND reversion_12 | 9856.40 | -143.60 | sell /  / trend_8_26 AND reversion_12: prior completed bar target 0%; next bar open simulation |
| v1 | trend_8_26 + reversion_12 | 9597.36 | -402.64 | buy /  / trend_8_26 + reversion_12: prior completed bar target 50%; next bar open simulation |
| v1 | trend_8_26 AND volume_26 | 9771.73 | -228.27 | sell /  / trend_8_26 AND volume_26: prior completed bar target 0%; next bar open simulation |
| v1 | trend_8_26 + volume_26 | 9531.96 | -468.04 | sell /  / trend_8_26 + volume_26: prior completed bar target 0%; next bar open simulation |
| v1 | momentum_26 AND breakout_8 | 9644.64 | -355.36 | sell /  / momentum_26 AND breakout_8: prior completed bar target 0%; next bar open simulation |
| v1 | momentum_26 + breakout_8 | 9375.58 | -624.42 | buy /  / momentum_26 + breakout_8: prior completed bar target 50%; next bar open simulation |
| v1 | momentum_26 AND reversion_12 | 9759.15 | -240.85 | buy /  / momentum_26 AND reversion_12: prior completed bar target 100%; next bar open simulation |
| v1 | momentum_26 + reversion_12 | 9431.44 | -568.56 | buy /  / momentum_26 + reversion_12: prior completed bar target 100%; next bar open simulation |
| v1 | momentum_26 AND volume_26 | 9789.69 | -210.31 | sell /  / momentum_26 AND volume_26: prior completed bar target 0%; next bar open simulation |
| v1 | momentum_26 + volume_26 | 9367.07 | -632.93 | buy /  / momentum_26 + volume_26: prior completed bar target 50%; next bar open simulation |
| v1 | breakout_8 AND reversion_12 | 10000.00 | 0.00 | 대기 /  / 새 신호 대기 |
| v1 | breakout_8 + reversion_12 | 9500.83 | -499.17 | sell /  / breakout_8 + reversion_12: prior completed bar target 50%; next bar open simulation |
| v1 | breakout_8 AND volume_26 | 9873.64 | -126.36 | sell /  / breakout_8 AND volume_26: prior completed bar target 0%; next bar open simulation |
| v1 | breakout_8 + volume_26 | 9531.07 | -468.93 | sell /  / breakout_8 + volume_26: prior completed bar target 0%; next bar open simulation |
| v1 | reversion_12 AND volume_26 | 9791.68 | -208.32 | sell /  / reversion_12 AND volume_26: prior completed bar target 0%; next bar open simulation |
| v1 | reversion_12 + volume_26 | 9492.36 | -507.64 | sell /  / reversion_12 + volume_26: prior completed bar target 50%; next bar open simulation |
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
| v1 | williams_14_recovery | 9441.24 | -558.76 | sell /  / 직전 Williams %R14 < -80, 현재 >= -80 (한 봉 목표); 조건 미충족; Williams_R14=-87.0884, previous_R14=-74.1768 |
| v1 | cmf_20_accumulation | 9319.81 | -680.19 | sell /  / Chaikin Money Flow20 > 0.1; 조건 미충족; CMF20=-0.0457086, volume20=4.3889e+08 |
| v1 | chaikin_3_10 | 9412.83 | -587.17 | sell /  / ADL의 EMA3 - EMA10 > 0 그리고 종가 > EMA26; 조건 미충족; Chaikin3_10=-1.63534e+07, ADL=3.82635e+08, close=707.37, EMA26=707.558 |
| v1 | roc_10_momentum | 9961.33 | -38.67 | sell /  / 10봉 ROC > 1% 그리고 종가 > EMA26; 조건 미충족; ROC10_percent=0.681109, close=725.78, EMA26=721.667 |
| v1 | trix_15_trend | 9467.11 | -532.89 | sell /  / 15봉 삼중 EMA의 1봉 변화율 TRIX > 0 그리고 종가 > EMA26; 조건 미충족; TRIX15_percent=0.0245938, close=713.775, EMA26=723.847 |
| v1 | keltner_20_breakout | 9782.40 | -217.60 | sell /  / 종가 > EMA20 + 2 x Wilder ATR14; 조건 미충족; close=726.815, upper_Keltner=727.39, EMA20=724.295, ATR14=1.54727 |
| v1 | opening_range_30m | 9471.93 | -528.07 | sell /  / 뉴욕 09:30·09:45 두 완료 봉 최고가를 10:00 이후 종가가 돌파; 조건 미충족; close=705.37, opening_high=705.64 |
| v2 | cash | 10000.00 | 0.00 | 대기 /  / 새 신호 대기 |
| v2 | buy_hold | 9383.73 | -616.27 | 중단: 손실 한도 / buy / partial / 직전 완료 봉 목표 비중 100%; 다음 봉 시가 가정 |
| v2 | trend_8_26 | 9419.46 | -580.54 | sell / filled / 직전 완료 봉 목표 비중 0%; 다음 봉 시가 가정 |
| v2 | momentum_26 | 9138.86 | -861.14 | buy / partial / 직전 완료 봉 목표 비중 100%; 다음 봉 시가 가정 |
| v2 | breakout_8 | 9129.27 | -870.73 | sell / filled / 직전 완료 봉 목표 비중 0%; 다음 봉 시가 가정 |
| v2 | reversion_12 | 8976.51 | -1023.49 | 중단: 손실 한도 / buy / partial / 직전 완료 봉 목표 비중 100%; 다음 봉 시가 가정 |
| v2 | volume_26 | 9565.80 | -434.20 | 중단: 손실 한도 / sell / filled / 직전 완료 봉 목표 비중 0%; 다음 봉 시가 가정 |
| v2 | trend_8_26 AND momentum_26 | 9484.57 | -515.43 | sell / filled / 직전 완료 봉 목표 비중 0%; 다음 봉 시가 가정 |
| v2 | trend_8_26 + momentum_26 | 9317.25 | -682.75 | sell / filled / 직전 완료 봉 목표 비중 50%; 다음 봉 시가 가정 |
| v2 | trend_8_26 AND breakout_8 | 9782.92 | -217.08 | sell / filled / 직전 완료 봉 목표 비중 0%; 다음 봉 시가 가정 |
| v2 | trend_8_26 + breakout_8 | 9331.95 | -668.05 | sell / filled / 직전 완료 봉 목표 비중 0%; 다음 봉 시가 가정 |
| v2 | trend_8_26 AND reversion_12 | 9711.76 | -288.24 | sell / filled / 직전 완료 봉 목표 비중 0%; 다음 봉 시가 가정 |
| v2 | trend_8_26 + reversion_12 | 9253.25 | -746.75 | buy / filled / 직전 완료 봉 목표 비중 50%; 다음 봉 시가 가정 |
| v2 | trend_8_26 AND volume_26 | 9602.02 | -397.98 | sell / filled / 직전 완료 봉 목표 비중 0%; 다음 봉 시가 가정 |
| v2 | trend_8_26 + volume_26 | 9135.34 | -864.66 | sell / filled / 직전 완료 봉 목표 비중 0%; 다음 봉 시가 가정 |
| v2 | momentum_26 AND breakout_8 | 9591.37 | -408.63 | sell / filled / 직전 완료 봉 목표 비중 0%; 다음 봉 시가 가정 |
| v2 | momentum_26 + breakout_8 | 9153.43 | -846.57 | buy / filled / 직전 완료 봉 목표 비중 50%; 다음 봉 시가 가정 |
| v2 | momentum_26 AND reversion_12 | 9750.37 | -249.63 | buy / partial / 직전 완료 봉 목표 비중 100%; 다음 봉 시가 가정 |
| v2 | momentum_26 + reversion_12 | 9152.78 | -847.22 | buy / partial / 직전 완료 봉 목표 비중 100%; 다음 봉 시가 가정 |
| v2 | momentum_26 AND volume_26 | 9718.13 | -281.87 | sell / filled / 직전 완료 봉 목표 비중 0%; 다음 봉 시가 가정 |
| v2 | momentum_26 + volume_26 | 9017.10 | -982.90 | buy / filled / 직전 완료 봉 목표 비중 50%; 다음 봉 시가 가정 |
| v2 | breakout_8 AND reversion_12 | 10000.00 | 0.00 | 대기 /  / 새 신호 대기 |
| v2 | breakout_8 + reversion_12 | 9147.61 | -852.39 | sell / filled / 직전 완료 봉 목표 비중 50%; 다음 봉 시가 가정 |
| v2 | breakout_8 AND volume_26 | 9814.43 | -185.57 | sell / filled / 직전 완료 봉 목표 비중 0%; 다음 봉 시가 가정 |
| v2 | breakout_8 + volume_26 | 9107.44 | -892.56 | sell / filled / 직전 완료 봉 목표 비중 0%; 다음 봉 시가 가정 |
| v2 | reversion_12 AND volume_26 | 9547.64 | -452.36 | 중단: 손실 한도 / sell / filled / 직전 완료 봉 목표 비중 0%; 다음 봉 시가 가정 |
| v2 | reversion_12 + volume_26 | 8985.79 | -1014.21 | 중단: 손실 한도 / buy / filled / 직전 완료 봉 목표 비중 50%; 다음 봉 시가 가정 |
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
| v2 | williams_14_recovery | 9412.96 | -587.04 | sell / filled / 직전 Williams %R14 < -80, 현재 >= -80 (한 봉 목표); 조건 미충족; Williams_R14=-87.0884, previous_R14=-74.1768; 직전 완료 봉 목표를 다음 봉 시가에 모의 적용 |
| v2 | cmf_20_accumulation | 9301.19 | -698.81 | sell / filled / Chaikin Money Flow20 > 0.1; 조건 미충족; CMF20=-0.0457086, volume20=4.3889e+08; 직전 완료 봉 목표를 다음 봉 시가에 모의 적용 |
| v2 | chaikin_3_10 | 9395.90 | -604.10 | sell / filled / ADL의 EMA3 - EMA10 > 0 그리고 종가 > EMA26; 조건 미충족; Chaikin3_10=-1.63534e+07, ADL=3.82635e+08, close=707.37, EMA26=707.558; 직전 완료 봉 목표를 다음 봉 시가에 모의 적용 |
| v2 | roc_10_momentum | 9957.34 | -42.66 | sell / filled / 10봉 ROC > 1% 그리고 종가 > EMA26; 조건 미충족; ROC10_percent=0.681109, close=725.78, EMA26=721.667; 직전 완료 봉 목표를 다음 봉 시가에 모의 적용 |
| v2 | trix_15_trend | 9453.87 | -546.13 | sell / filled / 15봉 삼중 EMA의 1봉 변화율 TRIX > 0 그리고 종가 > EMA26; 조건 미충족; TRIX15_percent=0.0245938, close=713.775, EMA26=723.847; 직전 완료 봉 목표를 다음 봉 시가에 모의 적용 |
| v2 | keltner_20_breakout | 9772.62 | -227.38 | sell / filled / 종가 > EMA20 + 2 x Wilder ATR14; 조건 미충족; close=726.815, upper_Keltner=727.39, EMA20=724.295, ATR14=1.54727; 직전 완료 봉 목표를 다음 봉 시가에 모의 적용 |
| v2 | opening_range_30m | 9458.68 | -541.32 | sell / filled / 뉴욕 09:30·09:45 두 완료 봉 최고가를 10:00 이후 종가가 돌파; 조건 미충족; close=705.37, opening_high=705.64; 직전 완료 봉 목표를 다음 봉 시가에 모의 적용 |

### 같은 기간의 비용·노출 비교 (사후 연구)

| 전략 | 비용 전 | 비용 후 | 100% 보유 | 같은 평균 노출 보유 | 평균 노출 |
|---|---:|---:|---:|---:|---:|
| cash | 0.00% | 0.00% | -6.85% | -0.00% | 0.00% |
| buy_hold | -6.46% | -6.85% | -6.85% | -6.85% | 100.00% |
| trend_8_26 | -2.62% | -6.23% | -6.85% | -2.78% | 39.95% |
| momentum_26 | -4.52% | -10.35% | -6.85% | -2.35% | 33.68% |
| breakout_8 | -2.12% | -16.91% | -6.85% | -1.28% | 18.28% |
| reversion_12 | -0.49% | -13.37% | -6.85% | -2.33% | 33.42% |
| volume_26 | -0.60% | -15.62% | -6.85% | -1.30% | 18.54% |
| trend_8_26 AND momentum_26 | -1.30% | -5.36% | -6.85% | -1.97% | 28.20% |
| trend_8_26 + momentum_26 | -3.57% | -7.73% | -6.85% | -2.57% | 36.82% |
| trend_8_26 AND breakout_8 | 0.08% | -7.98% | -6.85% | -0.77% | 10.97% |
| trend_8_26 + breakout_8 | -2.36% | -10.99% | -6.85% | -2.04% | 29.12% |
| trend_8_26 AND reversion_12 | -0.24% | -3.94% | -6.85% | -0.44% | 6.27% |
| trend_8_26 + reversion_12 | -1.55% | -9.12% | -6.85% | -2.56% | 36.69% |
| trend_8_26 AND volume_26 | 0.17% | -5.15% | -6.85% | -0.42% | 6.01% |
| trend_8_26 + volume_26 | -1.61% | -11.05% | -6.85% | -2.04% | 29.25% |
| momentum_26 AND breakout_8 | -0.42% | -8.06% | -6.85% | -0.72% | 10.18% |
| momentum_26 + breakout_8 | -3.32% | -13.33% | -6.85% | -1.82% | 25.99% |
| momentum_26 AND reversion_12 | -1.21% | -5.28% | -6.85% | -0.42% | 6.01% |
| momentum_26 + reversion_12 | -2.51% | -10.76% | -6.85% | -2.34% | 33.56% |
| momentum_26 AND volume_26 | -0.37% | -4.07% | -6.85% | -0.26% | 3.66% |
| momentum_26 + volume_26 | -2.57% | -12.66% | -6.85% | -1.83% | 26.12% |
| breakout_8 AND reversion_12 | 0.00% | 0.00% | -6.85% | -0.00% | 0.00% |
| breakout_8 + reversion_12 | -1.30% | -14.09% | -6.85% | -1.81% | 25.86% |
| breakout_8 AND volume_26 | 0.15% | -2.75% | -6.85% | -0.18% | 2.61% |
| breakout_8 + volume_26 | -1.36% | -14.50% | -6.85% | -1.29% | 18.42% |
| reversion_12 AND volume_26 | -1.12% | -8.70% | -6.85% | -0.62% | 8.88% |
| reversion_12 + volume_26 | -0.54% | -13.97% | -6.85% | -1.82% | 25.99% |
| ema_12_26 | -4.14% | -6.91% | -6.85% | -2.21% | 31.59% |
| macd_12_26_9 | -0.71% | -4.80% | -6.85% | -1.39% | 19.84% |
| rsi_14_recovery | -0.50% | -6.97% | -6.85% | -0.29% | 4.18% |
| bollinger_20_reentry | -0.05% | -5.76% | -6.85% | -0.26% | 3.66% |
| donchian_20 | 0.55% | -4.39% | -6.85% | -0.37% | 5.22% |
| atr_14_breakout | 0.52% | -3.21% | -6.85% | -0.18% | 2.61% |
| session_vwap | -3.29% | -14.74% | -6.85% | -3.25% | 46.74% |
| obv_20 | -4.54% | -13.33% | -6.85% | -1.43% | 20.37% |
| stochastic_14_3_recovery | 0.14% | -12.82% | -6.85% | -0.61% | 8.62% |
| mfi_14_recovery | -1.13% | -3.99% | -6.85% | -0.13% | 1.83% |
| adx_14_trend | 0.42% | -2.08% | -6.85% | -1.34% | 19.06% |
| aroon_25_trend | 0.17% | -2.73% | -6.85% | -1.01% | 14.36% |
| cci_20_momentum | 0.20% | -4.73% | -6.85% | -1.21% | 17.23% |
| williams_14_recovery | -0.24% | -12.05% | -6.85% | -0.55% | 7.83% |
| cmf_20_accumulation | -3.35% | -10.76% | -6.85% | -2.24% | 32.11% |
| chaikin_3_10 | -5.65% | -13.98% | -6.85% | -1.75% | 25.07% |
| roc_10_momentum | 0.41% | -0.43% | -6.85% | -0.20% | 2.87% |
| trix_15_trend | -3.02% | -6.62% | -6.85% | -1.81% | 25.85% |
| keltner_20_breakout | -0.36% | -4.46% | -6.85% | -0.48% | 6.79% |
| opening_range_30m | -2.08% | -7.67% | -6.85% | -2.59% | 37.08% |

동일 구간·초기 자금, 종료 시 청산 비용 포함. 노출 맞춤은 사후 설명용이며 v2 실제 계좌 성과가 아닙니다.
[낙폭 분해·비용 영향·전체 구간](QQQ/comparison.json)

[v1 전체 기록](QQQ/accounts.json) · [v2 전체 기록](QQQ/accounts-v2.json)

## IWM 계좌

| 모델 | 전략 | 평가액 USD | 손익 USD | 최근 매매·이유 |
|---|---|---:|---:|---|
| v1 | cash | 10000.00 | 0.00 | 대기 /  / 새 신호 대기 |
| v1 | buy_hold | 9986.55 | -13.45 | buy /  / buy_hold: prior completed bar target 100%; next bar open simulation |
| v1 | trend_8_26 | 9659.83 | -340.17 | buy /  / trend_8_26: prior completed bar target 100%; next bar open simulation |
| v1 | momentum_26 | 9607.76 | -392.24 | sell /  / momentum_26: prior completed bar target 0%; next bar open simulation |
| v1 | breakout_8 | 9221.05 | -778.95 | sell /  / breakout_8: prior completed bar target 0%; next bar open simulation |
| v1 | reversion_12 | 9713.04 | -286.96 | sell /  / reversion_12: prior completed bar target 0%; next bar open simulation |
| v1 | volume_26 | 9851.14 | -148.86 | sell /  / volume_26: prior completed bar target 0%; next bar open simulation |
| v1 | trend_8_26 AND momentum_26 | 9608.92 | -391.08 | sell /  / trend_8_26 AND momentum_26: prior completed bar target 0%; next bar open simulation |
| v1 | trend_8_26 + momentum_26 | 9653.16 | -346.84 | sell /  / trend_8_26 + momentum_26: prior completed bar target 50%; next bar open simulation |
| v1 | trend_8_26 AND breakout_8 | 9404.46 | -595.54 | sell /  / trend_8_26 AND breakout_8: prior completed bar target 0%; next bar open simulation |
| v1 | trend_8_26 + breakout_8 | 9438.08 | -561.92 | sell /  / trend_8_26 + breakout_8: prior completed bar target 50%; next bar open simulation |
| v1 | trend_8_26 AND reversion_12 | 9755.06 | -244.94 | sell /  / trend_8_26 AND reversion_12: prior completed bar target 0%; next bar open simulation |
| v1 | trend_8_26 + reversion_12 | 9686.15 | -313.85 | sell /  / trend_8_26 + reversion_12: prior completed bar target 50%; next bar open simulation |
| v1 | trend_8_26 AND volume_26 | 9893.73 | -106.27 | sell /  / trend_8_26 AND volume_26: prior completed bar target 0%; next bar open simulation |
| v1 | trend_8_26 + volume_26 | 9774.35 | -225.65 | sell /  / trend_8_26 + volume_26: prior completed bar target 50%; next bar open simulation |
| v1 | momentum_26 AND breakout_8 | 9478.36 | -521.64 | sell /  / momentum_26 AND breakout_8: prior completed bar target 0%; next bar open simulation |
| v1 | momentum_26 + breakout_8 | 9450.25 | -549.75 | sell /  / momentum_26 + breakout_8: prior completed bar target 0%; next bar open simulation |
| v1 | momentum_26 AND reversion_12 | 9876.67 | -123.33 | sell /  / momentum_26 AND reversion_12: prior completed bar target 0%; next bar open simulation |
| v1 | momentum_26 + reversion_12 | 9757.09 | -242.91 | sell /  / momentum_26 + reversion_12: prior completed bar target 0%; next bar open simulation |
| v1 | momentum_26 AND volume_26 | 9928.27 | -71.73 | sell /  / momentum_26 AND volume_26: prior completed bar target 0%; next bar open simulation |
| v1 | momentum_26 + volume_26 | 9767.55 | -232.45 | sell /  / momentum_26 + volume_26: prior completed bar target 0%; next bar open simulation |
| v1 | breakout_8 AND reversion_12 | 10000.00 | 0.00 | 대기 /  / 새 신호 대기 |
| v1 | breakout_8 + reversion_12 | 9501.52 | -498.48 | sell /  / breakout_8 + reversion_12: prior completed bar target 0%; next bar open simulation |
| v1 | breakout_8 AND volume_26 | 9918.46 | -81.54 | sell /  / breakout_8 AND volume_26: prior completed bar target 0%; next bar open simulation |
| v1 | breakout_8 + volume_26 | 9549.89 | -450.11 | sell /  / breakout_8 + volume_26: prior completed bar target 0%; next bar open simulation |
| v1 | reversion_12 AND volume_26 | 9912.42 | -87.58 | sell /  / reversion_12 AND volume_26: prior completed bar target 0%; next bar open simulation |
| v1 | reversion_12 + volume_26 | 9821.00 | -179.00 | sell /  / reversion_12 + volume_26: prior completed bar target 0%; next bar open simulation |
| v1 | ema_12_26 | 9639.40 | -360.60 | buy /  / EMA12 > EMA26; 조건 충족; EMA12=275.697, EMA26=275.694 |
| v1 | macd_12_26_9 | 9728.97 | -271.03 | buy /  / MACD > 신호선 그리고 MACD > 0; 조건 충족; MACD=0.00298871, signal9=-0.02074 |
| v1 | rsi_14_recovery | 9786.95 | -213.05 | sell /  / 직전 RSI14 < 30, 현재 RSI14 >= 30 (한 봉 목표); 조건 미충족; RSI14=46.986, previous_RSI14=37.1649 |
| v1 | bollinger_20_reentry | 9762.11 | -237.89 | sell /  / 직전 종가 < 직전 하단밴드, 현재 하단밴드 <= 종가 <= SMA20 (한 봉 목표); 조건 미충족; close=275.725, lower20=274.173, SMA20=275.605, previous_lower20=274.15 |
| v1 | donchian_20 | 9835.91 | -164.09 | sell /  / 종가 > 현재 봉을 제외한 직전 20봉 최고가; 조건 미충족; close=275.785, prior_high20=276.875 |
| v1 | atr_14_breakout | 9685.22 | -314.78 | sell /  / 종가 > 직전 종가 + 직전 ATR14 그리고 종가 > EMA26; 조건 미충족; close=274.63, threshold=277.369, prior_ATR14=0.659199, EMA26=275.963 |
| v1 | session_vwap | 9245.97 | -754.03 | buy /  / 종가 > 뉴욕 거래일별 누적 전형가격 VWAP; 조건 충족; close=275.03, session_VWAP=274.45, session_volume=6.20261e+06 |
| v1 | obv_20 | 9624.91 | -375.09 | sell /  / OBV > OBV의 SMA20 그리고 종가 > EMA26; 조건 미충족; OBV=-2.65101e+07, OBV_SMA20=-2.63464e+07, close=274.63, EMA26=275.963 |
| v1 | stochastic_14_3_recovery | 9613.95 | -386.05 | sell /  / 직전 %K14 < 20에서 %K14가 %D3 상향 돌파 (한 봉 목표); 조건 미충족; K14=68.0001, D3=43.5239, previous_K14=48.1428, previous_D3=23.7507 |
| v1 | mfi_14_recovery | 9934.22 | -65.78 | sell /  / 직전 MFI14 < 20, 현재 MFI14 >= 20 (한 봉 목표); 조건 미충족; MFI14=34.131, previous_MFI14=22.0435 |
| v1 | adx_14_trend | 9726.05 | -273.95 | sell /  / Wilder ADX14 >= 25 그리고 +DI14 > -DI14; 조건 미충족; ADX14=27.8461, plus_DI14=25.882, minus_DI14=28.4558 |
| v1 | aroon_25_trend | 9745.85 | -254.15 | sell /  / Aroon25 Up > 70 그리고 Down < 30 (동률이면 최신 극값); 조건 미충족; Aroon_up=68, Aroon_down=4 |
| v1 | cci_20_momentum | 9722.50 | -277.50 | sell /  / CCI20 > 100 (전형가격·평균절대편차); 조건 미충족; CCI20=-314.625 |
| v1 | williams_14_recovery | 9742.36 | -257.64 | sell /  / 직전 Williams %R14 < -80, 현재 >= -80 (한 봉 목표); 조건 미충족; Williams_R14=-31.9999, previous_R14=-51.8572 |
| v1 | cmf_20_accumulation | 9645.86 | -354.14 | sell /  / Chaikin Money Flow20 > 0.1; 조건 미충족; CMF20=0.083871, volume20=1.01663e+07 |
| v1 | chaikin_3_10 | 9320.53 | -679.47 | buy /  / ADL의 EMA3 - EMA10 > 0 그리고 종가 > EMA26; 조건 충족; Chaikin3_10=141136, ADL=-2.67081e+07, close=275.74, EMA26=275.694 |
| v1 | roc_10_momentum | 9996.39 | -3.61 | sell /  / 10봉 ROC > 1% 그리고 종가 > EMA26; 조건 미충족; ROC10_percent=0.995963, close=275.315, EMA26=273.754 |
| v1 | trix_15_trend | 9811.92 | -188.08 | sell /  / 15봉 삼중 EMA의 1봉 변화율 TRIX > 0 그리고 종가 > EMA26; 조건 미충족; TRIX15_percent=0.00744142, close=276.06, EMA26=276.447 |
| v1 | keltner_20_breakout | 9879.23 | -120.77 | sell /  / 종가 > EMA20 + 2 x Wilder ATR14; 조건 미충족; close=276.4, upper_Keltner=277.094, EMA20=275.768, ATR14=0.662947 |
| v1 | opening_range_30m | 9942.90 | -57.10 | buy /  / 뉴욕 09:30·09:45 두 완료 봉 최고가를 10:00 이후 종가가 돌파; 조건 충족; close=275.725, opening_high=275.24 |
| v2 | cash | 10000.00 | 0.00 | 대기 /  / 새 신호 대기 |
| v2 | buy_hold | 9879.77 | -120.23 | buy / partial / 직전 완료 봉 목표 비중 100%; 다음 봉 시가 가정 |
| v2 | trend_8_26 | 9527.03 | -472.97 | buy / partial / 직전 완료 봉 목표 비중 100%; 다음 봉 시가 가정 |
| v2 | momentum_26 | 9466.24 | -533.76 | sell / filled / 직전 완료 봉 목표 비중 0%; 다음 봉 시가 가정 |
| v2 | breakout_8 | 8990.85 | -1009.15 | 중단: 손실 한도 / buy / partial / 직전 완료 봉 목표 비중 100%; 다음 봉 시가 가정 |
| v2 | reversion_12 | 9246.43 | -753.57 | sell / filled / 직전 완료 봉 목표 비중 0%; 다음 봉 시가 가정 |
| v2 | volume_26 | 9360.51 | -639.49 | sell / filled / 직전 완료 봉 목표 비중 0%; 다음 봉 시가 가정 |
| v2 | trend_8_26 AND momentum_26 | 9617.18 | -382.82 | sell / filled / 직전 완료 봉 목표 비중 0%; 다음 봉 시가 가정 |
| v2 | trend_8_26 + momentum_26 | 9536.79 | -463.21 | sell / filled / 직전 완료 봉 목표 비중 50%; 다음 봉 시가 가정 |
| v2 | trend_8_26 AND breakout_8 | 9300.05 | -699.95 | sell / filled / 직전 완료 봉 목표 비중 0%; 다음 봉 시가 가정 |
| v2 | trend_8_26 + breakout_8 | 9195.88 | -804.12 | sell / filled / 직전 완료 봉 목표 비중 50%; 다음 봉 시가 가정 |
| v2 | trend_8_26 AND reversion_12 | 9630.14 | -369.86 | sell / filled / 직전 완료 봉 목표 비중 0%; 다음 봉 시가 가정 |
| v2 | trend_8_26 + reversion_12 | 9385.26 | -614.74 | sell / filled / 직전 완료 봉 목표 비중 50%; 다음 봉 시가 가정 |
| v2 | trend_8_26 AND volume_26 | 9752.17 | -247.83 | sell / filled / 직전 완료 봉 목표 비중 0%; 다음 봉 시가 가정 |
| v2 | trend_8_26 + volume_26 | 9482.93 | -517.07 | sell / filled / 직전 완료 봉 목표 비중 50%; 다음 봉 시가 가정 |
| v2 | momentum_26 AND breakout_8 | 9271.16 | -728.84 | sell / filled / 직전 완료 봉 목표 비중 0%; 다음 봉 시가 가정 |
| v2 | momentum_26 + breakout_8 | 9185.57 | -814.43 | sell / filled / 직전 완료 봉 목표 비중 0%; 다음 봉 시가 가정 |
| v2 | momentum_26 AND reversion_12 | 9831.84 | -168.16 | sell / filled / 직전 완료 봉 목표 비중 0%; 다음 봉 시가 가정 |
| v2 | momentum_26 + reversion_12 | 9473.66 | -526.34 | sell / filled / 직전 완료 봉 목표 비중 0%; 다음 봉 시가 가정 |
| v2 | momentum_26 AND volume_26 | 9818.94 | -181.06 | sell / filled / 직전 완료 봉 목표 비중 0%; 다음 봉 시가 가정 |
| v2 | momentum_26 + volume_26 | 9452.48 | -547.52 | sell / filled / 직전 완료 봉 목표 비중 0%; 다음 봉 시가 가정 |
| v2 | breakout_8 AND reversion_12 | 10000.00 | 0.00 | 대기 /  / 새 신호 대기 |
| v2 | breakout_8 + reversion_12 | 9115.73 | -884.27 | sell / filled / 직전 완료 봉 목표 비중 0%; 다음 봉 시가 가정 |
| v2 | breakout_8 AND volume_26 | 9660.76 | -339.24 | sell / filled / 직전 완료 봉 목표 비중 0%; 다음 봉 시가 가정 |
| v2 | breakout_8 + volume_26 | 9133.86 | -866.14 | sell / filled / 직전 완료 봉 목표 비중 0%; 다음 봉 시가 가정 |
| v2 | reversion_12 AND volume_26 | 9647.72 | -352.28 | sell / filled / 직전 완료 봉 목표 비중 0%; 다음 봉 시가 가정 |
| v2 | reversion_12 + volume_26 | 9361.82 | -638.18 | sell / filled / 직전 완료 봉 목표 비중 0%; 다음 봉 시가 가정 |
| v2 | ema_12_26 | 9626.87 | -373.13 | buy / partial / EMA12 > EMA26; 조건 충족; EMA12=275.697, EMA26=275.694; 직전 완료 봉 목표를 다음 봉 시가에 모의 적용 |
| v2 | macd_12_26_9 | 9716.33 | -283.67 | buy / partial / MACD > 신호선 그리고 MACD > 0; 조건 충족; MACD=0.00298871, signal9=-0.02074; 직전 완료 봉 목표를 다음 봉 시가에 모의 적용 |
| v2 | rsi_14_recovery | 9779.12 | -220.88 | sell / filled / 직전 RSI14 < 30, 현재 RSI14 >= 30 (한 봉 목표); 조건 미충족; RSI14=46.986, previous_RSI14=37.1649; 직전 완료 봉 목표를 다음 봉 시가에 모의 적용 |
| v2 | bollinger_20_reentry | 9750.40 | -249.60 | sell / filled / 직전 종가 < 직전 하단밴드, 현재 하단밴드 <= 종가 <= SMA20 (한 봉 목표); 조건 미충족; close=275.725, lower20=274.173, SMA20=275.605, previous_lower20=274.15; 직전 완료 봉 목표를 다음 봉 시가에 모의 적용 |
| v2 | donchian_20 | 9830.01 | -169.99 | sell / filled / 종가 > 현재 봉을 제외한 직전 20봉 최고가; 조건 미충족; close=275.785, prior_high20=276.875; 직전 완료 봉 목표를 다음 봉 시가에 모의 적용 |
| v2 | atr_14_breakout | 9669.74 | -330.26 | sell / filled / 종가 > 직전 종가 + 직전 ATR14 그리고 종가 > EMA26; 조건 미충족; close=274.63, threshold=277.369, prior_ATR14=0.659199, EMA26=275.963; 직전 완료 봉 목표를 다음 봉 시가에 모의 적용 |
| v2 | session_vwap | 9213.67 | -786.33 | buy / partial / 종가 > 뉴욕 거래일별 누적 전형가격 VWAP; 조건 충족; close=275.03, session_VWAP=274.45, session_volume=6.20261e+06; 직전 완료 봉 목표를 다음 봉 시가에 모의 적용 |
| v2 | obv_20 | 9607.61 | -392.39 | sell / filled / OBV > OBV의 SMA20 그리고 종가 > EMA26; 조건 미충족; OBV=-2.65101e+07, OBV_SMA20=-2.63464e+07, close=274.63, EMA26=275.963; 직전 완료 봉 목표를 다음 봉 시가에 모의 적용 |
| v2 | stochastic_14_3_recovery | 9594.74 | -405.26 | sell / filled / 직전 %K14 < 20에서 %K14가 %D3 상향 돌파 (한 봉 목표); 조건 미충족; K14=68.0001, D3=43.5239, previous_K14=48.1428, previous_D3=23.7507; 직전 완료 봉 목표를 다음 봉 시가에 모의 적용 |
| v2 | mfi_14_recovery | 9930.25 | -69.75 | sell / filled / 직전 MFI14 < 20, 현재 MFI14 >= 20 (한 봉 목표); 조건 미충족; MFI14=34.131, previous_MFI14=22.0435; 직전 완료 봉 목표를 다음 봉 시가에 모의 적용 |
| v2 | adx_14_trend | 9718.27 | -281.73 | sell / filled / Wilder ADX14 >= 25 그리고 +DI14 > -DI14; 조건 미충족; ADX14=27.8461, plus_DI14=25.882, minus_DI14=28.4558; 직전 완료 봉 목표를 다음 봉 시가에 모의 적용 |
| v2 | aroon_25_trend | 9736.11 | -263.89 | sell / filled / Aroon25 Up > 70 그리고 Down < 30 (동률이면 최신 극값); 조건 미충족; Aroon_up=68, Aroon_down=4; 직전 완료 봉 목표를 다음 봉 시가에 모의 적용 |
| v2 | cci_20_momentum | 9708.90 | -291.10 | sell / filled / CCI20 > 100 (전형가격·평균절대편차); 조건 미충족; CCI20=-314.625; 직전 완료 봉 목표를 다음 봉 시가에 모의 적용 |
| v2 | williams_14_recovery | 9726.79 | -273.21 | sell / filled / 직전 Williams %R14 < -80, 현재 >= -80 (한 봉 목표); 조건 미충족; Williams_R14=-31.9999, previous_R14=-51.8572; 직전 완료 봉 목표를 다음 봉 시가에 모의 적용 |
| v2 | cmf_20_accumulation | 9626.59 | -373.41 | sell / filled / Chaikin Money Flow20 > 0.1; 조건 미충족; CMF20=0.083871, volume20=1.01663e+07; 직전 완료 봉 목표를 다음 봉 시가에 모의 적용 |
| v2 | chaikin_3_10 | 9291.69 | -708.31 | buy / partial / ADL의 EMA3 - EMA10 > 0 그리고 종가 > EMA26; 조건 충족; Chaikin3_10=141136, ADL=-2.67081e+07, close=275.74, EMA26=275.694; 직전 완료 봉 목표를 다음 봉 시가에 모의 적용 |
| v2 | roc_10_momentum | 9994.39 | -5.61 | sell / filled / 10봉 ROC > 1% 그리고 종가 > EMA26; 조건 미충족; ROC10_percent=0.995963, close=275.315, EMA26=273.754; 직전 완료 봉 목표를 다음 봉 시가에 모의 적용 |
| v2 | trix_15_trend | 9804.07 | -195.93 | sell / filled / 15봉 삼중 EMA의 1봉 변화율 TRIX > 0 그리고 종가 > EMA26; 조건 미충족; TRIX15_percent=0.00744142, close=276.06, EMA26=276.447; 직전 완료 봉 목표를 다음 봉 시가에 모의 적용 |
| v2 | keltner_20_breakout | 9873.30 | -126.70 | sell / filled / 종가 > EMA20 + 2 x Wilder ATR14; 조건 미충족; close=276.4, upper_Keltner=277.094, EMA20=275.768, ATR14=0.662947; 직전 완료 봉 목표를 다음 봉 시가에 모의 적용 |
| v2 | opening_range_30m | 9937.93 | -62.07 | buy / partial / 뉴욕 09:30·09:45 두 완료 봉 최고가를 10:00 이후 종가가 돌파; 조건 충족; close=275.725, opening_high=275.24; 직전 완료 봉 목표를 다음 봉 시가에 모의 적용 |

### 같은 기간의 비용·노출 비교 (사후 연구)

| 전략 | 비용 전 | 비용 후 | 100% 보유 | 같은 평균 노출 보유 | 평균 노출 |
|---|---:|---:|---:|---:|---:|
| cash | 0.00% | 0.00% | -2.72% | -0.00% | 0.00% |
| buy_hold | -2.31% | -2.72% | -2.72% | -2.72% | 100.00% |
| trend_8_26 | -1.60% | -5.25% | -2.72% | -1.29% | 47.00% |
| momentum_26 | 0.72% | -5.83% | -2.72% | -1.16% | 42.04% |
| breakout_8 | -1.26% | -16.18% | -2.72% | -0.53% | 19.06% |
| reversion_12 | -1.54% | -12.46% | -2.72% | -0.74% | 26.63% |
| volume_26 | 0.06% | -7.22% | -2.72% | -0.24% | 8.62% |
| trend_8_26 AND momentum_26 | 0.12% | -4.00% | -2.72% | -0.99% | 36.03% |
| trend_8_26 + momentum_26 | -0.44% | -4.94% | -2.72% | -1.22% | 44.52% |
| trend_8_26 AND breakout_8 | -0.64% | -9.79% | -2.72% | -0.34% | 12.27% |
| trend_8_26 + breakout_8 | -1.42% | -10.69% | -2.72% | -0.91% | 33.03% |
| trend_8_26 AND reversion_12 | -0.94% | -4.61% | -2.72% | -0.15% | 5.48% |
| trend_8_26 + reversion_12 | -1.56% | -8.93% | -2.72% | -1.01% | 36.82% |
| trend_8_26 AND volume_26 | -0.31% | -3.61% | -2.72% | -0.08% | 2.87% |
| trend_8_26 + volume_26 | -0.76% | -5.85% | -2.72% | -0.77% | 27.81% |
| momentum_26 AND breakout_8 | 0.08% | -9.51% | -2.72% | -0.33% | 12.01% |
| momentum_26 + breakout_8 | -0.27% | -10.78% | -2.72% | -0.84% | 30.55% |
| momentum_26 AND reversion_12 | -0.35% | -2.42% | -2.72% | -0.07% | 2.35% |
| momentum_26 + reversion_12 | -0.41% | -7.87% | -2.72% | -0.95% | 34.34% |
| momentum_26 AND volume_26 | 0.43% | -2.48% | -2.72% | -0.07% | 2.35% |
| momentum_26 + volume_26 | 0.39% | -5.94% | -2.72% | -0.70% | 25.33% |
| breakout_8 AND reversion_12 | 0.00% | 0.00% | -2.72% | -0.00% | 0.00% |
| breakout_8 + reversion_12 | -1.39% | -13.63% | -2.72% | -0.63% | 22.85% |
| breakout_8 AND volume_26 | -0.63% | -3.91% | -2.72% | -0.07% | 2.35% |
| breakout_8 + volume_26 | -0.60% | -11.45% | -2.72% | -0.38% | 13.84% |
| reversion_12 AND volume_26 | 0.75% | -3.80% | -2.72% | -0.10% | 3.66% |
| reversion_12 + volume_26 | -0.74% | -9.32% | -2.72% | -0.49% | 17.63% |
| ema_12_26 | -0.19% | -4.30% | -2.72% | -1.19% | 43.08% |
| macd_12_26_9 | 1.90% | -1.88% | -2.72% | -0.66% | 24.02% |
| rsi_14_recovery | -0.88% | -4.95% | -2.72% | -0.07% | 2.61% |
| bollinger_20_reentry | -0.28% | -5.58% | -2.72% | -0.09% | 3.39% |
| donchian_20 | -0.08% | -4.19% | -2.72% | -0.14% | 5.22% |
| atr_14_breakout | -0.75% | -7.20% | -2.72% | -0.12% | 4.44% |
| session_vwap | -1.57% | -13.95% | -2.72% | -1.40% | 50.91% |
| obv_20 | -0.22% | -5.53% | -2.72% | -1.08% | 39.16% |
| stochastic_14_3_recovery | -0.64% | -12.40% | -2.72% | -0.22% | 7.83% |
| mfi_14_recovery | 0.20% | -3.92% | -2.72% | -0.07% | 2.61% |
| adx_14_trend | 0.33% | -2.17% | -2.72% | -0.84% | 30.29% |
| aroon_25_trend | -0.41% | -4.11% | -2.72% | -0.48% | 17.23% |
| cci_20_momentum | -0.93% | -7.76% | -2.72% | -0.51% | 18.54% |
| williams_14_recovery | 0.07% | -9.15% | -2.72% | -0.17% | 6.01% |
| cmf_20_accumulation | 0.06% | -6.83% | -2.72% | -0.81% | 29.24% |
| chaikin_3_10 | -1.45% | -10.53% | -2.72% | -1.00% | 36.29% |
| roc_10_momentum | 0.32% | -0.52% | -2.72% | -0.10% | 3.66% |
| trix_15_trend | 0.63% | -2.70% | -2.72% | -0.89% | 32.38% |
| keltner_20_breakout | 0.21% | -2.69% | -2.72% | -0.16% | 5.74% |
| opening_range_30m | 1.50% | -2.67% | -2.72% | -0.76% | 27.42% |

동일 구간·초기 자금, 종료 시 청산 비용 포함. 노출 맞춤은 사후 설명용이며 v2 실제 계좌 성과가 아닙니다.
[낙폭 분해·비용 영향·전체 구간](IWM/comparison.json)

[v1 전체 기록](IWM/accounts.json) · [v2 전체 기록](IWM/accounts-v2.json)

## DIA 계좌

| 모델 | 전략 | 평가액 USD | 손익 USD | 최근 매매·이유 |
|---|---|---:|---:|---|
| v1 | cash | 10000.00 | 0.00 | 대기 /  / 새 신호 대기 |
| v1 | buy_hold | 9962.09 | -37.91 | buy /  / buy_hold: prior completed bar target 100%; next bar open simulation |
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
| v1 | session_vwap | 9529.36 | -470.64 | sell /  / 종가 > 뉴욕 거래일별 누적 전형가격 VWAP; 조건 미충족; close=521.935, session_VWAP=522.11, session_volume=2.33157e+06 |
| v1 | obv_20 | 9727.80 | -272.20 | sell /  / OBV > OBV의 SMA20 그리고 종가 > EMA26; 조건 미충족; OBV=-6.66951e+06, OBV_SMA20=-6.32674e+06, close=522.39, EMA26=526.494 |
| v1 | stochastic_14_3_recovery | 9688.29 | -311.71 | sell /  / 직전 %K14 < 20에서 %K14가 %D3 상향 돌파 (한 봉 목표); 조건 미충족; K14=35.6623, D3=20.5547, previous_K14=19.3192, previous_D3=8.7863 |
| v1 | mfi_14_recovery | 9902.01 | -97.99 | sell /  / 직전 MFI14 < 20, 현재 MFI14 >= 20 (한 봉 목표); 조건 미충족; MFI14=29.4378, previous_MFI14=21.6288 |
| v1 | adx_14_trend | 9711.49 | -288.51 | sell /  / Wilder ADX14 >= 25 그리고 +DI14 > -DI14; 조건 미충족; ADX14=28.0997, plus_DI14=30.0206, minus_DI14=36.1913 |
| v1 | aroon_25_trend | 9820.69 | -179.31 | sell /  / Aroon25 Up > 70 그리고 Down < 30 (동률이면 최신 극값); 조건 미충족; Aroon_up=72, Aroon_down=92 |
| v1 | cci_20_momentum | 9709.75 | -290.25 | sell /  / CCI20 > 100 (전형가격·평균절대편차); 조건 미충족; CCI20=-498.183 |
| v1 | williams_14_recovery | 9697.88 | -302.12 | sell /  / 직전 Williams %R14 < -80, 현재 >= -80 (한 봉 목표); 조건 미충족; Williams_R14=-68.4085, previous_R14=-64.3377 |
| v1 | cmf_20_accumulation | 9330.93 | -669.07 | sell /  / Chaikin Money Flow20 > 0.1; 조건 미충족; CMF20=0.0668366, volume20=1.54371e+06 |
| v1 | chaikin_3_10 | 9611.06 | -388.94 | sell /  / ADL의 EMA3 - EMA10 > 0 그리고 종가 > EMA26; 조건 미충족; Chaikin3_10=70160.2, ADL=-1.15315e+07, close=522.39, EMA26=526.494 |
| v1 | roc_10_momentum | 9939.01 | -60.99 | sell /  / 10봉 ROC > 1% 그리고 종가 > EMA26; 조건 미충족; ROC10_percent=0.771645, close=523.68, EMA26=521.367 |
| v1 | trix_15_trend | 9741.60 | -258.40 | sell /  / 15봉 삼중 EMA의 1봉 변화율 TRIX > 0 그리고 종가 > EMA26; 조건 미충족; TRIX15_percent=0.0047414, close=522.39, EMA26=526.494 |
| v1 | keltner_20_breakout | 9826.82 | -173.18 | sell /  / 종가 > EMA20 + 2 x Wilder ATR14; 조건 미충족; close=526.34, upper_Keltner=527.991, EMA20=526.293, ATR14=0.848911 |
| v1 | opening_range_30m | 9536.25 | -463.75 | sell /  / 뉴욕 09:30·09:45 두 완료 봉 최고가를 10:00 이후 종가가 돌파; 자료 부족·변동폭 또는 거래량 없음: 대기; close=522.39 |
| v2 | cash | 10000.00 | 0.00 | 대기 /  / 새 신호 대기 |
| v2 | buy_hold | 10085.51 | 85.51 | buy / partial / 직전 완료 봉 목표 비중 100%; 다음 봉 시가 가정 |
| v2 | trend_8_26 | 9784.94 | -215.06 | sell / filled / 직전 완료 봉 목표 비중 0%; 다음 봉 시가 가정 |
| v2 | momentum_26 | 9699.02 | -300.98 | sell / filled / 직전 완료 봉 목표 비중 0%; 다음 봉 시가 가정 |
| v2 | breakout_8 | 8926.88 | -1073.12 | 중단: 손실 한도 / buy / partial / 직전 완료 봉 목표 비중 100%; 다음 봉 시가 가정 |
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
| v2 | session_vwap | 9510.32 | -489.68 | 중단: 손실 한도 / sell / filled / 종가 > 뉴욕 거래일별 누적 전형가격 VWAP; 조건 미충족; close=521.935, session_VWAP=522.11, session_volume=2.33157e+06; 직전 완료 봉 목표를 다음 봉 시가에 모의 적용 |
| v2 | obv_20 | 9712.25 | -287.75 | sell / filled / OBV > OBV의 SMA20 그리고 종가 > EMA26; 조건 미충족; OBV=-6.66951e+06, OBV_SMA20=-6.32674e+06, close=522.39, EMA26=526.494; 직전 완료 봉 목표를 다음 봉 시가에 모의 적용 |
| v2 | stochastic_14_3_recovery | 9670.86 | -329.14 | sell / filled / 직전 %K14 < 20에서 %K14가 %D3 상향 돌파 (한 봉 목표); 조건 미충족; K14=35.6623, D3=20.5547, previous_K14=19.3192, previous_D3=8.7863; 직전 완료 봉 목표를 다음 봉 시가에 모의 적용 |
| v2 | mfi_14_recovery | 9896.07 | -103.93 | sell / filled / 직전 MFI14 < 20, 현재 MFI14 >= 20 (한 봉 목표); 조건 미충족; MFI14=29.4378, previous_MFI14=21.6288; 직전 완료 봉 목표를 다음 봉 시가에 모의 적용 |
| v2 | adx_14_trend | 9701.78 | -298.22 | sell / filled / Wilder ADX14 >= 25 그리고 +DI14 > -DI14; 조건 미충족; ADX14=28.0997, plus_DI14=30.0206, minus_DI14=36.1913; 직전 완료 봉 목표를 다음 봉 시가에 모의 적용 |
| v2 | aroon_25_trend | 9810.88 | -189.12 | sell / filled / Aroon25 Up > 70 그리고 Down < 30 (동률이면 최신 극값); 조건 미충족; Aroon_up=72, Aroon_down=92; 직전 완료 봉 목표를 다음 봉 시가에 모의 적용 |
| v2 | cci_20_momentum | 9694.23 | -305.77 | sell / filled / CCI20 > 100 (전형가격·평균절대편차); 조건 미충족; CCI20=-498.183; 직전 완료 봉 목표를 다음 봉 시가에 모의 적용 |
| v2 | williams_14_recovery | 9682.38 | -317.62 | sell / filled / 직전 Williams %R14 < -80, 현재 >= -80 (한 봉 목표); 조건 미충족; Williams_R14=-68.4085, previous_R14=-64.3377; 직전 완료 봉 목표를 다음 봉 시가에 모의 적용 |
| v2 | cmf_20_accumulation | 9306.70 | -693.30 | sell / filled / Chaikin Money Flow20 > 0.1; 조건 미충족; CMF20=0.0668366, volume20=1.54371e+06; 직전 완료 봉 목표를 다음 봉 시가에 모의 적용 |
| v2 | chaikin_3_10 | 9595.70 | -404.30 | sell / filled / ADL의 EMA3 - EMA10 > 0 그리고 종가 > EMA26; 조건 미충족; Chaikin3_10=70160.2, ADL=-1.15315e+07, close=522.39, EMA26=526.494; 직전 완료 봉 목표를 다음 봉 시가에 모의 적용 |
| v2 | roc_10_momentum | 9937.03 | -62.97 | sell / filled / 10봉 ROC > 1% 그리고 종가 > EMA26; 조건 미충족; ROC10_percent=0.771645, close=523.68, EMA26=521.367; 직전 완료 봉 목표를 다음 봉 시가에 모의 적용 |
| v2 | trix_15_trend | 9731.86 | -268.14 | sell / filled / 15봉 삼중 EMA의 1봉 변화율 TRIX > 0 그리고 종가 > EMA26; 조건 미충족; TRIX15_percent=0.0047414, close=522.39, EMA26=526.494; 직전 완료 봉 목표를 다음 봉 시가에 모의 적용 |
| v2 | keltner_20_breakout | 9817.00 | -183.00 | sell / filled / 종가 > EMA20 + 2 x Wilder ATR14; 조건 미충족; close=526.34, upper_Keltner=527.991, EMA20=526.293, ATR14=0.848911; 직전 완료 봉 목표를 다음 봉 시가에 모의 적용 |
| v2 | opening_range_30m | 9517.20 | -482.80 | sell / filled / 뉴욕 09:30·09:45 두 완료 봉 최고가를 10:00 이후 종가가 돌파; 자료 부족·변동폭 또는 거래량 없음: 대기; close=522.39; 직전 완료 봉 목표를 다음 봉 시가에 모의 적용 |

### 같은 기간의 비용·노출 비교 (사후 연구)

| 전략 | 비용 전 | 비용 후 | 100% 보유 | 같은 평균 노출 보유 | 평균 노출 |
|---|---:|---:|---:|---:|---:|
| cash | 0.00% | 0.00% | 1.86% | 0.00% | 0.00% |
| buy_hold | 2.29% | 1.86% | 1.86% | 1.86% | 100.00% |
| trend_8_26 | 2.35% | -1.45% | 1.86% | 1.15% | 62.14% |
| momentum_26 | 1.43% | -3.15% | 1.86% | 1.10% | 59.53% |
| breakout_8 | 0.31% | -16.61% | 1.86% | 0.47% | 25.33% |
| reversion_12 | 0.84% | -7.29% | 1.86% | 0.35% | 19.06% |
| volume_26 | 1.74% | -7.24% | 1.86% | 0.18% | 9.66% |
| trend_8_26 AND momentum_26 | 2.82% | -2.23% | 1.86% | 0.97% | 52.74% |
| trend_8_26 + momentum_26 | 1.89% | -2.30% | 1.86% | 1.12% | 60.84% |
| trend_8_26 AND breakout_8 | 1.39% | -10.99% | 1.86% | 0.33% | 18.02% |
| trend_8_26 + breakout_8 | 1.33% | -8.58% | 1.86% | 0.81% | 43.74% |
| trend_8_26 AND reversion_12 | 0.81% | -4.55% | 1.86% | 0.13% | 7.05% |
| trend_8_26 + reversion_12 | 1.59% | -4.22% | 1.86% | 0.75% | 40.60% |
| trend_8_26 AND volume_26 | 2.07% | -3.35% | 1.86% | 0.10% | 5.48% |
| trend_8_26 + volume_26 | 2.05% | -4.19% | 1.86% | 0.66% | 35.90% |
| momentum_26 AND breakout_8 | 0.60% | -12.79% | 1.86% | 0.37% | 20.37% |
| momentum_26 + breakout_8 | 0.88% | -10.13% | 1.86% | 0.78% | 42.44% |
| momentum_26 AND reversion_12 | 0.10% | -3.21% | 1.86% | 0.10% | 5.48% |
| momentum_26 + reversion_12 | 1.14% | -4.45% | 1.86% | 0.72% | 39.30% |
| momentum_26 AND volume_26 | 0.52% | -5.62% | 1.86% | 0.11% | 5.74% |
| momentum_26 + volume_26 | 1.59% | -4.62% | 1.86% | 0.64% | 34.60% |
| breakout_8 AND reversion_12 | 0.00% | 0.00% | 1.86% | 0.00% | 0.00% |
| breakout_8 + reversion_12 | 0.58% | -11.72% | 1.86% | 0.41% | 22.20% |
| breakout_8 AND volume_26 | 0.28% | -3.44% | 1.86% | 0.06% | 3.39% |
| breakout_8 + volume_26 | 1.03% | -11.13% | 1.86% | 0.32% | 17.50% |
| reversion_12 AND volume_26 | 1.21% | -2.13% | 1.86% | 0.04% | 2.35% |
| reversion_12 + volume_26 | 1.29% | -6.88% | 1.86% | 0.26% | 14.37% |
| ema_12_26 | 1.22% | -0.88% | 1.86% | 1.12% | 60.57% |
| macd_12_26_9 | 2.44% | -1.77% | 1.86% | 0.59% | 31.85% |
| rsi_14_recovery | 0.39% | -0.86% | 1.86% | 0.01% | 0.78% |
| bollinger_20_reentry | 0.50% | -2.41% | 1.86% | 0.03% | 1.83% |
| donchian_20 | 0.32% | -7.76% | 1.86% | 0.20% | 10.97% |
| atr_14_breakout | -0.20% | -8.63% | 1.86% | 0.12% | 6.53% |
| session_vwap | 1.12% | -6.64% | 1.86% | 1.17% | 63.19% |
| obv_20 | 1.83% | -5.58% | 1.86% | 0.83% | 45.17% |
| stochastic_14_3_recovery | 1.51% | -8.99% | 1.86% | 0.12% | 6.79% |
| mfi_14_recovery | 0.37% | -2.95% | 1.86% | 0.04% | 2.09% |
| adx_14_trend | 0.37% | -3.35% | 1.86% | 0.60% | 32.64% |
| aroon_25_trend | 1.75% | -2.02% | 1.86% | 0.50% | 27.42% |
| cci_20_momentum | 2.05% | -4.58% | 1.86% | 0.51% | 27.94% |
| williams_14_recovery | 1.45% | -5.93% | 1.86% | 0.09% | 4.70% |
| cmf_20_accumulation | -0.02% | -9.23% | 1.86% | 0.86% | 46.48% |
| chaikin_3_10 | 1.04% | -8.26% | 1.86% | 0.95% | 51.44% |
| roc_10_momentum | -0.07% | -0.90% | 1.86% | 0.04% | 2.09% |
| trix_15_trend | 0.80% | -2.94% | 1.86% | 1.00% | 54.31% |
| keltner_20_breakout | 1.05% | -6.31% | 1.86% | 0.36% | 19.84% |
| opening_range_30m | 1.10% | -6.66% | 1.86% | 0.60% | 32.64% |

동일 구간·초기 자금, 종료 시 청산 비용 포함. 노출 맞춤은 사후 설명용이며 v2 실제 계좌 성과가 아닙니다.
[낙폭 분해·비용 영향·전체 구간](DIA/comparison.json)

[v1 전체 기록](DIA/accounts.json) · [v2 전체 기록](DIA/accounts-v2.json)

## MSFT 계좌

| 모델 | 전략 | 평가액 USD | 손익 USD | 최근 매매·이유 |
|---|---|---:|---:|---|
| v1 | cash | 10000.00 | 0.00 | 대기 /  / 새 신호 대기 |
| v1 | buy_hold | 9659.08 | -340.92 | buy /  / buy_hold: prior completed bar target 100%; next bar open simulation |
| v1 | trend_8_26 | 9397.42 | -602.58 | buy /  / trend_8_26: prior completed bar target 100%; next bar open simulation |
| v1 | momentum_26 | 9188.87 | -811.13 | buy /  / momentum_26: prior completed bar target 100%; next bar open simulation |
| v1 | breakout_8 | 9454.11 | -545.89 | sell /  / breakout_8: prior completed bar target 0%; next bar open simulation |
| v1 | reversion_12 | 9232.29 | -767.71 | buy /  / reversion_12: prior completed bar target 100%; next bar open simulation |
| v1 | volume_26 | 9570.29 | -429.71 | sell /  / volume_26: prior completed bar target 0%; next bar open simulation |
| v1 | trend_8_26 AND momentum_26 | 9326.31 | -673.69 | buy /  / trend_8_26 AND momentum_26: prior completed bar target 100%; next bar open simulation |
| v1 | trend_8_26 + momentum_26 | 9329.82 | -670.18 | buy /  / trend_8_26 + momentum_26: prior completed bar target 100%; next bar open simulation |
| v1 | trend_8_26 AND breakout_8 | 9678.51 | -321.49 | sell /  / trend_8_26 AND breakout_8: prior completed bar target 0%; next bar open simulation |
| v1 | trend_8_26 + breakout_8 | 9463.66 | -536.34 | sell /  / trend_8_26 + breakout_8: prior completed bar target 50%; next bar open simulation |
| v1 | trend_8_26 AND reversion_12 | 9464.94 | -535.06 | buy /  / trend_8_26 AND reversion_12: prior completed bar target 100%; next bar open simulation |
| v1 | trend_8_26 + reversion_12 | 9333.03 | -666.97 | buy /  / trend_8_26 + reversion_12: prior completed bar target 100%; next bar open simulation |
| v1 | trend_8_26 AND volume_26 | 9748.22 | -251.78 | sell /  / trend_8_26 AND volume_26: prior completed bar target 0%; next bar open simulation |
| v1 | trend_8_26 + volume_26 | 9483.54 | -516.46 | sell /  / trend_8_26 + volume_26: prior completed bar target 50%; next bar open simulation |
| v1 | momentum_26 AND breakout_8 | 9642.25 | -357.75 | sell /  / momentum_26 AND breakout_8: prior completed bar target 0%; next bar open simulation |
| v1 | momentum_26 + breakout_8 | 9339.32 | -660.68 | sell /  / momentum_26 + breakout_8: prior completed bar target 50%; next bar open simulation |
| v1 | momentum_26 AND reversion_12 | 9594.60 | -405.40 | buy /  / momentum_26 AND reversion_12: prior completed bar target 100%; next bar open simulation |
| v1 | momentum_26 + reversion_12 | 9265.81 | -734.19 | buy /  / momentum_26 + reversion_12: prior completed bar target 100%; next bar open simulation |
| v1 | momentum_26 AND volume_26 | 9795.49 | -204.51 | sell /  / momentum_26 AND volume_26: prior completed bar target 0%; next bar open simulation |
| v1 | momentum_26 + volume_26 | 9415.39 | -584.61 | sell /  / momentum_26 + volume_26: prior completed bar target 50%; next bar open simulation |
| v1 | breakout_8 AND reversion_12 | 10000.00 | 0.00 | 대기 /  / 새 신호 대기 |
| v1 | breakout_8 + reversion_12 | 9379.77 | -620.23 | sell /  / breakout_8 + reversion_12: prior completed bar target 50%; next bar open simulation |
| v1 | breakout_8 AND volume_26 | 9953.19 | -46.81 | sell /  / breakout_8 AND volume_26: prior completed bar target 0%; next bar open simulation |
| v1 | breakout_8 + volume_26 | 9549.92 | -450.08 | sell /  / breakout_8 + volume_26: prior completed bar target 0%; next bar open simulation |
| v1 | reversion_12 AND volume_26 | 9735.94 | -264.06 | sell /  / reversion_12 AND volume_26: prior completed bar target 0%; next bar open simulation |
| v1 | reversion_12 + volume_26 | 9418.51 | -581.49 | sell /  / reversion_12 + volume_26: prior completed bar target 50%; next bar open simulation |
| v1 | ema_12_26 | 9429.96 | -570.04 | sell /  / EMA12 > EMA26; 조건 미충족; EMA12=524.285, EMA26=524.3 |
| v1 | macd_12_26_9 | 9541.74 | -458.26 | sell /  / MACD > 신호선 그리고 MACD > 0; 조건 미충족; MACD=-0.0156477, signal9=-0.0308572 |
| v1 | rsi_14_recovery | 9839.66 | -160.34 | sell /  / 직전 RSI14 < 30, 현재 RSI14 >= 30 (한 봉 목표); 조건 미충족; RSI14=49.0008, previous_RSI14=38.029 |
| v1 | bollinger_20_reentry | 9745.81 | -254.19 | sell /  / 직전 종가 < 직전 하단밴드, 현재 하단밴드 <= 종가 <= SMA20 (한 봉 목표); 조건 미충족; close=523.535, lower20=518.78, SMA20=523.154, previous_lower20=518.792 |
| v1 | donchian_20 | 9912.16 | -87.84 | sell /  / 종가 > 현재 봉을 제외한 직전 20봉 최고가; 조건 미충족; close=534.52, prior_high20=535.44 |
| v1 | atr_14_breakout | 9915.10 | -84.90 | sell /  / 종가 > 직전 종가 + 직전 ATR14 그리고 종가 > EMA26; 조건 미충족; close=533.975, threshold=536.307, prior_ATR14=2.16203, EMA26=530.521 |
| v1 | session_vwap | 9618.92 | -381.08 | buy /  / 종가 > 뉴욕 거래일별 누적 전형가격 VWAP; 조건 충족; close=520.51, session_VWAP=518.805, session_volume=2.29852e+06 |
| v1 | obv_20 | 9475.03 | -524.97 | sell /  / OBV > OBV의 SMA20 그리고 종가 > EMA26; 조건 미충족; OBV=3.70404e+07, OBV_SMA20=4.23196e+07, close=524.11, EMA26=524.113 |
| v1 | stochastic_14_3_recovery | 9615.09 | -384.91 | buy /  / 직전 %K14 < 20에서 %K14가 %D3 상향 돌파 (한 봉 목표); 조건 충족; K14=31.3505, D3=19.3908, previous_K14=4.74854, previous_D3=24.4258 |
| v1 | mfi_14_recovery | 9880.73 | -119.27 | sell /  / 직전 MFI14 < 20, 현재 MFI14 >= 20 (한 봉 목표); 조건 미충족; MFI14=28.323, previous_MFI14=32.1727 |
| v1 | adx_14_trend | 9883.62 | -116.38 | sell /  / Wilder ADX14 >= 25 그리고 +DI14 > -DI14; 조건 미충족; ADX14=23.6824, plus_DI14=22.3066, minus_DI14=19.9214 |
| v1 | aroon_25_trend | 9616.60 | -383.40 | sell /  / Aroon25 Up > 70 그리고 Down < 30 (동률이면 최신 극값); 조건 미충족; Aroon_up=96, Aroon_down=100 |
| v1 | cci_20_momentum | 9870.62 | -129.38 | sell /  / CCI20 > 100 (전형가격·평균절대편차); 조건 미충족; CCI20=99.2896 |
| v1 | williams_14_recovery | 9595.57 | -404.43 | buy /  / 직전 Williams %R14 < -80, 현재 >= -80 (한 봉 목표); 조건 충족; Williams_R14=-68.6495, previous_R14=-95.2515 |
| v1 | cmf_20_accumulation | 9569.53 | -430.47 | sell /  / Chaikin Money Flow20 > 0.1; 조건 미충족; CMF20=-0.143516, volume20=1.68966e+07 |
| v1 | chaikin_3_10 | 9512.73 | -487.27 | sell /  / ADL의 EMA3 - EMA10 > 0 그리고 종가 > EMA26; 조건 미충족; Chaikin3_10=-1.26329e+06, ADL=9.19087e+07, close=524.11, EMA26=524.113 |
| v1 | roc_10_momentum | 9912.67 | -87.33 | sell /  / 10봉 ROC > 1% 그리고 종가 > EMA26; 조건 미충족; ROC10_percent=0.691625, close=524.11, EMA26=524.113 |
| v1 | trix_15_trend | 9557.09 | -442.91 | sell /  / 15봉 삼중 EMA의 1봉 변화율 TRIX > 0 그리고 종가 > EMA26; 조건 미충족; TRIX15_percent=0.00481299, close=529.54, EMA26=531.788 |
| v1 | keltner_20_breakout | 9958.78 | -41.22 | sell /  / 종가 > EMA20 + 2 x Wilder ATR14; 조건 미충족; close=533.975, upper_Keltner=534.357, EMA20=530.111, ATR14=2.12332 |
| v1 | opening_range_30m | 9590.02 | -409.98 | buy /  / 뉴욕 09:30·09:45 두 완료 봉 최고가를 10:00 이후 종가가 돌파; 조건 충족; close=523.535, opening_high=522.36 |
| v2 | cash | 10000.00 | 0.00 | 대기 /  / 새 신호 대기 |
| v2 | buy_hold | 9711.78 | -288.22 | buy / partial / 직전 완료 봉 목표 비중 100%; 다음 봉 시가 가정 |
| v2 | trend_8_26 | 9330.32 | -669.68 | buy / partial / 직전 완료 봉 목표 비중 100%; 다음 봉 시가 가정 |
| v2 | momentum_26 | 9213.26 | -786.74 | buy / partial / 직전 완료 봉 목표 비중 100%; 다음 봉 시가 가정 |
| v2 | breakout_8 | 9238.63 | -761.37 | sell / filled / 직전 완료 봉 목표 비중 0%; 다음 봉 시가 가정 |
| v2 | reversion_12 | 9011.62 | -988.38 | 중단: 손실 한도 / buy / partial / 직전 완료 봉 목표 비중 100%; 다음 봉 시가 가정 |
| v2 | volume_26 | 9249.99 | -750.01 | sell / filled / 직전 완료 봉 목표 비중 0%; 다음 봉 시가 가정 |
| v2 | trend_8_26 AND momentum_26 | 9215.42 | -784.58 | buy / partial / 직전 완료 봉 목표 비중 100%; 다음 봉 시가 가정 |
| v2 | trend_8_26 + momentum_26 | 9310.88 | -689.12 | buy / partial / 직전 완료 봉 목표 비중 100%; 다음 봉 시가 가정 |
| v2 | trend_8_26 AND breakout_8 | 9318.21 | -681.79 | sell / filled / 직전 완료 봉 목표 비중 0%; 다음 봉 시가 가정 |
| v2 | trend_8_26 + breakout_8 | 9343.38 | -656.62 | sell / filled / 직전 완료 봉 목표 비중 50%; 다음 봉 시가 가정 |
| v2 | trend_8_26 AND reversion_12 | 9354.47 | -645.53 | buy / partial / 직전 완료 봉 목표 비중 100%; 다음 봉 시가 가정 |
| v2 | trend_8_26 + reversion_12 | 9108.86 | -891.14 | buy / partial / 직전 완료 봉 목표 비중 100%; 다음 봉 시가 가정 |
| v2 | trend_8_26 AND volume_26 | 9686.55 | -313.45 | sell / filled / 직전 완료 봉 목표 비중 0%; 다음 봉 시가 가정 |
| v2 | trend_8_26 + volume_26 | 9309.47 | -690.53 | sell / filled / 직전 완료 봉 목표 비중 50%; 다음 봉 시가 가정 |
| v2 | momentum_26 AND breakout_8 | 9430.77 | -569.23 | sell / filled / 직전 완료 봉 목표 비중 0%; 다음 봉 시가 가정 |
| v2 | momentum_26 + breakout_8 | 9245.50 | -754.50 | sell / filled / 직전 완료 봉 목표 비중 50%; 다음 봉 시가 가정 |
| v2 | momentum_26 AND reversion_12 | 9418.14 | -581.86 | buy / partial / 직전 완료 봉 목표 비중 100%; 다음 봉 시가 가정 |
| v2 | momentum_26 + reversion_12 | 9089.68 | -910.32 | buy / partial / 직전 완료 봉 목표 비중 100%; 다음 봉 시가 가정 |
| v2 | momentum_26 AND volume_26 | 9659.72 | -340.28 | sell / filled / 직전 완료 봉 목표 비중 0%; 다음 봉 시가 가정 |
| v2 | momentum_26 + volume_26 | 9290.04 | -709.96 | sell / filled / 직전 완료 봉 목표 비중 50%; 다음 봉 시가 가정 |
| v2 | breakout_8 AND reversion_12 | 10000.00 | 0.00 | 대기 /  / 새 신호 대기 |
| v2 | breakout_8 + reversion_12 | 9102.12 | -897.88 | sell / filled / 직전 완료 봉 목표 비중 50%; 다음 봉 시가 가정 |
| v2 | breakout_8 AND volume_26 | 9890.09 | -109.91 | sell / filled / 직전 완료 봉 목표 비중 0%; 다음 봉 시가 가정 |
| v2 | breakout_8 + volume_26 | 9302.52 | -697.48 | sell / filled / 직전 완료 봉 목표 비중 0%; 다음 봉 시가 가정 |
| v2 | reversion_12 AND volume_26 | 9492.87 | -507.13 | sell / filled / 직전 완료 봉 목표 비중 0%; 다음 봉 시가 가정 |
| v2 | reversion_12 + volume_26 | 9069.74 | -930.26 | sell / filled / 직전 완료 봉 목표 비중 50%; 다음 봉 시가 가정 |
| v2 | ema_12_26 | 9420.53 | -579.47 | sell / filled / EMA12 > EMA26; 조건 미충족; EMA12=524.285, EMA26=524.3; 직전 완료 봉 목표를 다음 봉 시가에 모의 적용 |
| v2 | macd_12_26_9 | 9530.30 | -469.70 | sell / filled / MACD > 신호선 그리고 MACD > 0; 조건 미충족; MACD=-0.0156477, signal9=-0.0308572; 직전 완료 봉 목표를 다음 봉 시가에 모의 적용 |
| v2 | rsi_14_recovery | 9825.89 | -174.11 | sell / filled / 직전 RSI14 < 30, 현재 RSI14 >= 30 (한 봉 목표); 조건 미충족; RSI14=49.0008, previous_RSI14=38.029; 직전 완료 봉 목표를 다음 봉 시가에 모의 적용 |
| v2 | bollinger_20_reentry | 9732.18 | -267.82 | sell / filled / 직전 종가 < 직전 하단밴드, 현재 하단밴드 <= 종가 <= SMA20 (한 봉 목표); 조건 미충족; close=523.535, lower20=518.78, SMA20=523.154, previous_lower20=518.792; 직전 완료 봉 목표를 다음 봉 시가에 모의 적용 |
| v2 | donchian_20 | 9908.19 | -91.81 | sell / filled / 종가 > 현재 봉을 제외한 직전 20봉 최고가; 조건 미충족; close=534.52, prior_high20=535.44; 직전 완료 봉 목표를 다음 봉 시가에 모의 적용 |
| v2 | atr_14_breakout | 9911.14 | -88.86 | sell / filled / 종가 > 직전 종가 + 직전 ATR14 그리고 종가 > EMA26; 조건 미충족; close=533.975, threshold=536.307, prior_ATR14=2.16203, EMA26=530.521; 직전 완료 봉 목표를 다음 봉 시가에 모의 적용 |
| v2 | session_vwap | 9602.58 | -397.42 | buy / partial / 종가 > 뉴욕 거래일별 누적 전형가격 VWAP; 조건 충족; close=520.51, session_VWAP=518.805, session_volume=2.29852e+06; 직전 완료 봉 목표를 다음 봉 시가에 모의 적용 |
| v2 | obv_20 | 9456.10 | -543.90 | sell / filled / OBV > OBV의 SMA20 그리고 종가 > EMA26; 조건 미충족; OBV=3.70404e+07, OBV_SMA20=4.23196e+07, close=524.11, EMA26=524.113; 직전 완료 봉 목표를 다음 봉 시가에 모의 적용 |
| v2 | stochastic_14_3_recovery | 9594.92 | -405.08 | buy / partial / 직전 %K14 < 20에서 %K14가 %D3 상향 돌파 (한 봉 목표); 조건 충족; K14=31.3505, D3=19.3908, previous_K14=4.74854, previous_D3=24.4258; 직전 완료 봉 목표를 다음 봉 시가에 모의 적용 |
| v2 | mfi_14_recovery | 9872.83 | -127.17 | sell / filled / 직전 MFI14 < 20, 현재 MFI14 >= 20 (한 봉 목표); 조건 미충족; MFI14=28.323, previous_MFI14=32.1727; 직전 완료 봉 목표를 다음 봉 시가에 모의 적용 |
| v2 | adx_14_trend | 9879.67 | -120.33 | sell / filled / Wilder ADX14 >= 25 그리고 +DI14 > -DI14; 조건 미충족; ADX14=23.6824, plus_DI14=22.3066, minus_DI14=19.9214; 직전 완료 봉 목표를 다음 봉 시가에 모의 적용 |
| v2 | aroon_25_trend | 9608.91 | -391.09 | sell / filled / Aroon25 Up > 70 그리고 Down < 30 (동률이면 최신 극값); 조건 미충족; Aroon_up=96, Aroon_down=100; 직전 완료 봉 목표를 다음 봉 시가에 모의 적용 |
| v2 | cci_20_momentum | 9862.73 | -137.27 | sell / filled / CCI20 > 100 (전형가격·평균절대편차); 조건 미충족; CCI20=99.2896; 직전 완료 봉 목표를 다음 봉 시가에 모의 적용 |
| v2 | williams_14_recovery | 9575.45 | -424.55 | buy / partial / 직전 Williams %R14 < -80, 현재 >= -80 (한 봉 목표); 조건 충족; Williams_R14=-68.6495, previous_R14=-95.2515; 직전 완료 봉 목표를 다음 봉 시가에 모의 적용 |
| v2 | cmf_20_accumulation | 9558.05 | -441.95 | sell / filled / Chaikin Money Flow20 > 0.1; 조건 미충족; CMF20=-0.143516, volume20=1.68966e+07; 직전 완료 봉 목표를 다음 봉 시가에 모의 적용 |
| v2 | chaikin_3_10 | 9495.62 | -504.38 | sell / filled / ADL의 EMA3 - EMA10 > 0 그리고 종가 > EMA26; 조건 미충족; Chaikin3_10=-1.26329e+06, ADL=9.19087e+07, close=524.11, EMA26=524.113; 직전 완료 봉 목표를 다음 봉 시가에 모의 적용 |
| v2 | roc_10_momentum | 9908.71 | -91.29 | sell / filled / 10봉 ROC > 1% 그리고 종가 > EMA26; 조건 미충족; ROC10_percent=0.691625, close=524.11, EMA26=524.113; 직전 완료 봉 목표를 다음 봉 시가에 모의 적용 |
| v2 | trix_15_trend | 9549.45 | -450.55 | sell / filled / 15봉 삼중 EMA의 1봉 변화율 TRIX > 0 그리고 종가 > EMA26; 조건 미충족; TRIX15_percent=0.00481299, close=529.54, EMA26=531.788; 직전 완료 봉 목표를 다음 봉 시가에 모의 적용 |
| v2 | keltner_20_breakout | 9956.78 | -43.22 | sell / filled / 종가 > EMA20 + 2 x Wilder ATR14; 조건 미충족; close=533.975, upper_Keltner=534.357, EMA20=530.111, ATR14=2.12332; 직전 완료 봉 목표를 다음 봉 시가에 모의 적용 |
| v2 | opening_range_30m | 9581.40 | -418.60 | buy / partial / 뉴욕 09:30·09:45 두 완료 봉 최고가를 10:00 이후 종가가 돌파; 조건 충족; close=523.535, opening_high=522.36; 직전 완료 봉 목표를 다음 봉 시가에 모의 적용 |

### 같은 기간의 비용·노출 비교 (사후 연구)

| 전략 | 비용 전 | 비용 후 | 100% 보유 | 같은 평균 노출 보유 | 평균 노출 |
|---|---:|---:|---:|---:|---:|
| cash | 0.00% | 0.00% | -1.06% | -0.00% | 0.00% |
| buy_hold | -0.65% | -1.06% | -1.06% | -1.06% | 100.00% |
| trend_8_26 | -3.14% | -6.74% | -1.06% | -0.60% | 56.92% |
| momentum_26 | -2.45% | -9.56% | -1.06% | -0.58% | 54.83% |
| breakout_8 | 3.75% | -10.06% | -1.06% | -0.20% | 18.80% |
| reversion_12 | -5.59% | -15.00% | -1.06% | -0.28% | 26.89% |
| volume_26 | -0.45% | -9.61% | -1.06% | -0.09% | 8.88% |
| trend_8_26 AND momentum_26 | -2.66% | -8.99% | -1.06% | -0.52% | 49.61% |
| trend_8_26 + momentum_26 | -2.79% | -7.77% | -1.06% | -0.59% | 55.88% |
| trend_8_26 AND breakout_8 | -1.14% | -10.62% | -1.06% | -0.12% | 11.23% |
| trend_8_26 + breakout_8 | 0.26% | -7.83% | -1.06% | -0.40% | 37.86% |
| trend_8_26 AND reversion_12 | -2.32% | -8.67% | -1.06% | -0.08% | 7.83% |
| trend_8_26 + reversion_12 | -4.36% | -10.78% | -1.06% | -0.44% | 41.91% |
| trend_8_26 AND volume_26 | 0.71% | -3.02% | -1.06% | -0.03% | 2.87% |
| trend_8_26 + volume_26 | -1.79% | -7.80% | -1.06% | -0.35% | 32.90% |
| momentum_26 AND breakout_8 | -0.01% | -9.98% | -1.06% | -0.13% | 12.01% |
| momentum_26 + breakout_8 | 0.61% | -9.42% | -1.06% | -0.39% | 36.82% |
| momentum_26 AND reversion_12 | -3.02% | -8.94% | -1.06% | -0.09% | 8.62% |
| momentum_26 + reversion_12 | -4.02% | -11.77% | -1.06% | -0.43% | 40.87% |
| momentum_26 AND volume_26 | -0.29% | -4.39% | -1.06% | -0.03% | 3.13% |
| momentum_26 + volume_26 | -1.44% | -8.82% | -1.06% | -0.34% | 31.86% |
| breakout_8 AND reversion_12 | 0.00% | 0.00% | -1.06% | -0.00% | 0.00% |
| breakout_8 + reversion_12 | -1.02% | -11.83% | -1.06% | -0.24% | 22.85% |
| breakout_8 AND volume_26 | 0.08% | -1.59% | -1.06% | -0.01% | 1.31% |
| breakout_8 + volume_26 | 1.64% | -9.08% | -1.06% | -0.15% | 13.85% |
| reversion_12 AND volume_26 | -2.48% | -6.88% | -1.06% | -0.04% | 4.18% |
| reversion_12 + volume_26 | -3.05% | -12.17% | -1.06% | -0.19% | 17.89% |
| ema_12_26 | -2.72% | -5.94% | -1.06% | -0.59% | 55.35% |
| macd_12_26_9 | -2.79% | -7.96% | -1.06% | -0.35% | 32.90% |
| rsi_14_recovery | 0.73% | -3.42% | -1.06% | -0.03% | 2.61% |
| bollinger_20_reentry | -0.23% | -4.34% | -1.06% | -0.03% | 2.61% |
| donchian_20 | -0.08% | -4.60% | -1.06% | -0.04% | 3.39% |
| atr_14_breakout | 0.48% | -3.25% | -1.06% | -0.02% | 2.35% |
| session_vwap | 4.14% | -4.65% | -1.06% | -0.55% | 51.70% |
| obv_20 | 2.79% | -5.09% | -1.06% | -0.51% | 48.56% |
| stochastic_14_3_recovery | -0.12% | -9.70% | -1.06% | -0.07% | 6.27% |
| mfi_14_recovery | 1.71% | -2.47% | -1.06% | -0.03% | 2.61% |
| adx_14_trend | 4.03% | 1.87% | -1.06% | -0.46% | 43.34% |
| aroon_25_trend | -1.50% | -5.94% | -1.06% | -0.23% | 21.67% |
| cci_20_momentum | 1.88% | -4.34% | -1.06% | -0.21% | 19.58% |
| williams_14_recovery | -0.73% | -9.49% | -1.06% | -0.06% | 5.74% |
| cmf_20_accumulation | -0.48% | -7.34% | -1.06% | -0.46% | 43.34% |
| chaikin_3_10 | 1.19% | -6.96% | -1.06% | -0.52% | 48.83% |
| roc_10_momentum | 0.20% | -3.92% | -1.06% | -0.13% | 12.53% |
| trix_15_trend | -0.28% | -3.98% | -1.06% | -0.45% | 42.56% |
| keltner_20_breakout | -0.51% | -5.40% | -1.06% | -0.11% | 10.44% |
| opening_range_30m | -1.18% | -5.25% | -1.06% | -0.27% | 25.85% |

동일 구간·초기 자금, 종료 시 청산 비용 포함. 노출 맞춤은 사후 설명용이며 v2 실제 계좌 성과가 아닙니다.
[낙폭 분해·비용 영향·전체 구간](MSFT/comparison.json)

[v1 전체 기록](MSFT/accounts.json) · [v2 전체 기록](MSFT/accounts-v2.json)

## JPM 계좌

| 모델 | 전략 | 평가액 USD | 손익 USD | 최근 매매·이유 |
|---|---|---:|---:|---|
| v1 | cash | 10000.00 | 0.00 | 대기 /  / 새 신호 대기 |
| v1 | buy_hold | 9754.84 | -245.16 | buy /  / buy_hold: prior completed bar target 100%; next bar open simulation |
| v1 | trend_8_26 | 9572.38 | -427.62 | sell /  / trend_8_26: prior completed bar target 0%; next bar open simulation |
| v1 | momentum_26 | 9183.69 | -816.31 | sell /  / momentum_26: prior completed bar target 0%; next bar open simulation |
| v1 | breakout_8 | 9370.48 | -629.52 | sell /  / breakout_8: prior completed bar target 0%; next bar open simulation |
| v1 | reversion_12 | 9476.27 | -523.73 | sell /  / reversion_12: prior completed bar target 0%; next bar open simulation |
| v1 | volume_26 | 9846.15 | -153.85 | sell /  / volume_26: prior completed bar target 0%; next bar open simulation |
| v1 | trend_8_26 AND momentum_26 | 9441.00 | -559.00 | sell /  / trend_8_26 AND momentum_26: prior completed bar target 0%; next bar open simulation |
| v1 | trend_8_26 + momentum_26 | 9376.17 | -623.83 | sell /  / trend_8_26 + momentum_26: prior completed bar target 0%; next bar open simulation |
| v1 | trend_8_26 AND breakout_8 | 9638.65 | -361.35 | sell /  / trend_8_26 AND breakout_8: prior completed bar target 0%; next bar open simulation |
| v1 | trend_8_26 + breakout_8 | 9508.88 | -491.12 | sell /  / trend_8_26 + breakout_8: prior completed bar target 0%; next bar open simulation |
| v1 | trend_8_26 AND reversion_12 | 9687.22 | -312.78 | sell /  / trend_8_26 AND reversion_12: prior completed bar target 0%; next bar open simulation |
| v1 | trend_8_26 + reversion_12 | 9524.04 | -475.96 | sell /  / trend_8_26 + reversion_12: prior completed bar target 0%; next bar open simulation |
| v1 | trend_8_26 AND volume_26 | 10027.62 | 27.62 | sell /  / trend_8_26 AND volume_26: prior completed bar target 0%; next bar open simulation |
| v1 | trend_8_26 + volume_26 | 9708.16 | -291.84 | sell /  / trend_8_26 + volume_26: prior completed bar target 0%; next bar open simulation |
| v1 | momentum_26 AND breakout_8 | 9431.18 | -568.82 | sell /  / momentum_26 AND breakout_8: prior completed bar target 0%; next bar open simulation |
| v1 | momentum_26 + breakout_8 | 9276.72 | -723.28 | sell /  / momentum_26 + breakout_8: prior completed bar target 0%; next bar open simulation |
| v1 | momentum_26 AND reversion_12 | 9788.16 | -211.84 | sell /  / momentum_26 AND reversion_12: prior completed bar target 0%; next bar open simulation |
| v1 | momentum_26 + reversion_12 | 9441.24 | -558.76 | sell /  / momentum_26 + reversion_12: prior completed bar target 0%; next bar open simulation |
| v1 | momentum_26 AND volume_26 | 9871.31 | -128.69 | sell /  / momentum_26 AND volume_26: prior completed bar target 0%; next bar open simulation |
| v1 | momentum_26 + volume_26 | 9547.21 | -452.79 | sell /  / momentum_26 + volume_26: prior completed bar target 0%; next bar open simulation |
| v1 | breakout_8 AND reversion_12 | 10000.00 | 0.00 | 대기 /  / 새 신호 대기 |
| v1 | breakout_8 + reversion_12 | 9479.66 | -520.34 | sell /  / breakout_8 + reversion_12: prior completed bar target 0%; next bar open simulation |
| v1 | breakout_8 AND volume_26 | 9998.31 | -1.69 | sell /  / breakout_8 AND volume_26: prior completed bar target 0%; next bar open simulation |
| v1 | breakout_8 + volume_26 | 9624.57 | -375.43 | sell /  / breakout_8 + volume_26: prior completed bar target 0%; next bar open simulation |
| v1 | reversion_12 AND volume_26 | 9881.36 | -118.64 | sell /  / reversion_12 AND volume_26: prior completed bar target 0%; next bar open simulation |
| v1 | reversion_12 + volume_26 | 9697.96 | -302.04 | sell /  / reversion_12 + volume_26: prior completed bar target 0%; next bar open simulation |
| v1 | ema_12_26 | 9456.51 | -543.49 | sell /  / EMA12 > EMA26; 조건 미충족; EMA12=334.326, EMA26=334.511 |
| v1 | macd_12_26_9 | 9556.03 | -443.97 | sell /  / MACD > 신호선 그리고 MACD > 0; 조건 미충족; MACD=0.0530109, signal9=0.111707 |
| v1 | rsi_14_recovery | 9986.37 | -13.63 | sell /  / 직전 RSI14 < 30, 현재 RSI14 >= 30 (한 봉 목표); 조건 미충족; RSI14=61.6663, previous_RSI14=57.046 |
| v1 | bollinger_20_reentry | 9835.47 | -164.53 | sell /  / 직전 종가 < 직전 하단밴드, 현재 하단밴드 <= 종가 <= SMA20 (한 봉 목표); 조건 미충족; close=332.25, lower20=330.876, SMA20=334.012, previous_lower20=331.095 |
| v1 | donchian_20 | 9663.29 | -336.71 | sell /  / 종가 > 현재 봉을 제외한 직전 20봉 최고가; 조건 미충족; close=332.6, prior_high20=336.61 |
| v1 | atr_14_breakout | 9637.39 | -362.61 | sell /  / 종가 > 직전 종가 + 직전 ATR14 그리고 종가 > EMA26; 조건 미충족; close=332.6, threshold=337.371, prior_ATR14=0.861165, EMA26=334.725 |
| v1 | session_vwap | 9400.29 | -599.71 | sell /  / 종가 > 뉴욕 거래일별 누적 전형가격 VWAP; 조건 미충족; close=331.89, session_VWAP=331.994, session_volume=2.46536e+06 |
| v1 | obv_20 | 9551.60 | -448.40 | sell /  / OBV > OBV의 SMA20 그리고 종가 > EMA26; 조건 미충족; OBV=-1.95307e+07, OBV_SMA20=-1.97351e+07, close=332.6, EMA26=334.725 |
| v1 | stochastic_14_3_recovery | 9544.29 | -455.71 | sell /  / 직전 %K14 < 20에서 %K14가 %D3 상향 돌파 (한 봉 목표); 조건 미충족; K14=45.6055, D3=25.3586, previous_K14=22.8521, previous_D3=15.2809 |
| v1 | mfi_14_recovery | 9935.64 | -64.36 | sell /  / 직전 MFI14 < 20, 현재 MFI14 >= 20 (한 봉 목표); 조건 미충족; MFI14=30.2719, previous_MFI14=26.8492 |
| v1 | adx_14_trend | 9726.68 | -273.32 | sell /  / Wilder ADX14 >= 25 그리고 +DI14 > -DI14; 조건 미충족; ADX14=23.9395, plus_DI14=23.2021, minus_DI14=22.594 |
| v1 | aroon_25_trend | 9769.62 | -230.38 | sell /  / Aroon25 Up > 70 그리고 Down < 30 (동률이면 최신 극값); 조건 미충족; Aroon_up=96, Aroon_down=100 |
| v1 | cci_20_momentum | 9681.01 | -318.99 | sell /  / CCI20 > 100 (전형가격·평균절대편차); 조건 미충족; CCI20=-280.713 |
| v1 | williams_14_recovery | 9516.15 | -483.85 | sell /  / 직전 Williams %R14 < -80, 현재 >= -80 (한 봉 목표); 조건 미충족; Williams_R14=-54.3945, previous_R14=-77.1479 |
| v1 | cmf_20_accumulation | 9644.59 | -355.41 | buy /  / Chaikin Money Flow20 > 0.1; 조건 충족; CMF20=0.115539, volume20=2.04147e+06 |
| v1 | chaikin_3_10 | 9553.87 | -446.13 | sell /  / ADL의 EMA3 - EMA10 > 0 그리고 종가 > EMA26; 조건 미충족; Chaikin3_10=268702, ADL=-8.90187e+06, close=332.6, EMA26=334.725 |
| v1 | roc_10_momentum | 9836.40 | -163.60 | sell /  / 10봉 ROC > 1% 그리고 종가 > EMA26; 조건 미충족; ROC10_percent=0.964142, close=337.72, EMA26=336.695 |
| v1 | trix_15_trend | 9614.50 | -385.50 | sell /  / 15봉 삼중 EMA의 1봉 변화율 TRIX > 0 그리고 종가 > EMA26; 조건 미충족; TRIX15_percent=0.00517218, close=332.6, EMA26=334.725 |
| v1 | keltner_20_breakout | 9905.24 | -94.76 | sell /  / 종가 > EMA20 + 2 x Wilder ATR14; 조건 미충족; close=339.04, upper_Keltner=339.281, EMA20=336.559, ATR14=1.36146 |
| v1 | opening_range_30m | 9795.03 | -204.97 | sell /  / 뉴욕 09:30·09:45 두 완료 봉 최고가를 10:00 이후 종가가 돌파; 자료 부족·변동폭 또는 거래량 없음: 대기; close=332.6 |
| v2 | cash | 10000.00 | 0.00 | 대기 /  / 새 신호 대기 |
| v2 | buy_hold | 9917.84 | -82.16 | buy / partial / 직전 완료 봉 목표 비중 100%; 다음 봉 시가 가정 |
| v2 | trend_8_26 | 9573.52 | -426.48 | sell / filled / 직전 완료 봉 목표 비중 0%; 다음 봉 시가 가정 |
| v2 | momentum_26 | 9065.53 | -934.47 | 중단: 손실 한도 / buy / partial / 직전 완료 봉 목표 비중 100%; 다음 봉 시가 가정 |
| v2 | breakout_8 | 8935.41 | -1064.59 | 중단: 손실 한도 / buy / partial / 직전 완료 봉 목표 비중 100%; 다음 봉 시가 가정 |
| v2 | reversion_12 | 9438.41 | -561.59 | sell / filled / 직전 완료 봉 목표 비중 0%; 다음 봉 시가 가정 |
| v2 | volume_26 | 9661.98 | -338.02 | sell / filled / 직전 완료 봉 목표 비중 0%; 다음 봉 시가 가정 |
| v2 | trend_8_26 AND momentum_26 | 9395.85 | -604.15 | sell / filled / 직전 완료 봉 목표 비중 0%; 다음 봉 시가 가정 |
| v2 | trend_8_26 + momentum_26 | 9150.71 | -849.29 | sell / filled / 직전 완료 봉 목표 비중 0%; 다음 봉 시가 가정 |
| v2 | trend_8_26 AND breakout_8 | 9019.37 | -980.63 | sell / filled / 직전 완료 봉 목표 비중 0%; 다음 봉 시가 가정 |
| v2 | trend_8_26 + breakout_8 | 9178.08 | -821.92 | sell / filled / 직전 완료 봉 목표 비중 0%; 다음 봉 시가 가정 |
| v2 | trend_8_26 AND reversion_12 | 9657.80 | -342.20 | sell / filled / 직전 완료 봉 목표 비중 0%; 다음 봉 시가 가정 |
| v2 | trend_8_26 + reversion_12 | 9545.74 | -454.26 | sell / filled / 직전 완료 봉 목표 비중 0%; 다음 봉 시가 가정 |
| v2 | trend_8_26 AND volume_26 | 9821.47 | -178.53 | sell / filled / 직전 완료 봉 목표 비중 0%; 다음 봉 시가 가정 |
| v2 | trend_8_26 + volume_26 | 9618.29 | -381.71 | sell / filled / 직전 완료 봉 목표 비중 0%; 다음 봉 시가 가정 |
| v2 | momentum_26 AND breakout_8 | 8887.90 | -1112.10 | 중단: 손실 한도 / buy / partial / 직전 완료 봉 목표 비중 100%; 다음 봉 시가 가정 |
| v2 | momentum_26 + breakout_8 | 8995.36 | -1004.64 | 중단: 손실 한도 / sell / filled / 직전 완료 봉 목표 비중 0%; 다음 봉 시가 가정 |
| v2 | momentum_26 AND reversion_12 | 9730.22 | -269.78 | sell / filled / 직전 완료 봉 목표 비중 0%; 다음 봉 시가 가정 |
| v2 | momentum_26 + reversion_12 | 9297.88 | -702.12 | sell / filled / 직전 완료 봉 목표 비중 0%; 다음 봉 시가 가정 |
| v2 | momentum_26 AND volume_26 | 9668.38 | -331.62 | sell / filled / 직전 완료 봉 목표 비중 0%; 다음 봉 시가 가정 |
| v2 | momentum_26 + volume_26 | 9270.91 | -729.09 | sell / filled / 직전 완료 봉 목표 비중 0%; 다음 봉 시가 가정 |
| v2 | breakout_8 AND reversion_12 | 10000.00 | 0.00 | 대기 /  / 새 신호 대기 |
| v2 | breakout_8 + reversion_12 | 9169.56 | -830.44 | sell / filled / 직전 완료 봉 목표 비중 0%; 다음 봉 시가 가정 |
| v2 | breakout_8 AND volume_26 | 9883.76 | -116.24 | sell / filled / 직전 완료 봉 목표 비중 0%; 다음 봉 시가 가정 |
| v2 | breakout_8 + volume_26 | 9219.46 | -780.54 | sell / filled / 직전 완료 봉 목표 비중 0%; 다음 봉 시가 가정 |
| v2 | reversion_12 AND volume_26 | 9926.17 | -73.83 | sell / filled / 직전 완료 봉 목표 비중 0%; 다음 봉 시가 가정 |
| v2 | reversion_12 + volume_26 | 9609.94 | -390.06 | sell / filled / 직전 완료 봉 목표 비중 0%; 다음 봉 시가 가정 |
| v2 | ema_12_26 | 9447.06 | -552.94 | sell / filled / EMA12 > EMA26; 조건 미충족; EMA12=334.326, EMA26=334.511; 직전 완료 봉 목표를 다음 봉 시가에 모의 적용 |
| v2 | macd_12_26_9 | 9546.47 | -453.53 | sell / filled / MACD > 신호선 그리고 MACD > 0; 조건 미충족; MACD=0.0530109, signal9=0.111707; 직전 완료 봉 목표를 다음 봉 시가에 모의 적용 |
| v2 | rsi_14_recovery | 9984.37 | -15.63 | sell / filled / 직전 RSI14 < 30, 현재 RSI14 >= 30 (한 봉 목표); 조건 미충족; RSI14=61.6663, previous_RSI14=57.046; 직전 완료 봉 목표를 다음 봉 시가에 모의 적용 |
| v2 | bollinger_20_reentry | 9825.64 | -174.36 | sell / filled / 직전 종가 < 직전 하단밴드, 현재 하단밴드 <= 종가 <= SMA20 (한 봉 목표); 조건 미충족; close=332.25, lower20=330.876, SMA20=334.012, previous_lower20=331.095; 직전 완료 봉 목표를 다음 봉 시가에 모의 적용 |
| v2 | donchian_20 | 9653.63 | -346.37 | sell / filled / 종가 > 현재 봉을 제외한 직전 20봉 최고가; 조건 미충족; close=332.6, prior_high20=336.61; 직전 완료 봉 목표를 다음 봉 시가에 모의 적용 |
| v2 | atr_14_breakout | 9621.98 | -378.02 | sell / filled / 종가 > 직전 종가 + 직전 ATR14 그리고 종가 > EMA26; 조건 미충족; close=332.6, threshold=337.371, prior_ATR14=0.861165, EMA26=334.725; 직전 완료 봉 목표를 다음 봉 시가에 모의 적용 |
| v2 | session_vwap | 9379.63 | -620.37 | sell / filled / 종가 > 뉴욕 거래일별 누적 전형가격 VWAP; 조건 미충족; close=331.89, session_VWAP=331.994, session_volume=2.46536e+06; 직전 완료 봉 목표를 다음 봉 시가에 모의 적용 |
| v2 | obv_20 | 9532.52 | -467.48 | sell / filled / OBV > OBV의 SMA20 그리고 종가 > EMA26; 조건 미충족; OBV=-1.95307e+07, OBV_SMA20=-1.97351e+07, close=332.6, EMA26=334.725; 직전 완료 봉 목표를 다음 봉 시가에 모의 적용 |
| v2 | stochastic_14_3_recovery | 9517.60 | -482.40 | sell / filled / 직전 %K14 < 20에서 %K14가 %D3 상향 돌파 (한 봉 목표); 조건 미충족; K14=45.6055, D3=25.3586, previous_K14=22.8521, previous_D3=15.2809; 직전 완료 봉 목표를 다음 봉 시가에 모의 적용 |
| v2 | mfi_14_recovery | 9931.66 | -68.34 | sell / filled / 직전 MFI14 < 20, 현재 MFI14 >= 20 (한 봉 목표); 조건 미충족; MFI14=30.2719, previous_MFI14=26.8492; 직전 완료 봉 목표를 다음 봉 시가에 모의 적용 |
| v2 | adx_14_trend | 9722.79 | -277.21 | sell / filled / Wilder ADX14 >= 25 그리고 +DI14 > -DI14; 조건 미충족; ADX14=23.9395, plus_DI14=23.2021, minus_DI14=22.594; 직전 완료 봉 목표를 다음 봉 시가에 모의 적용 |
| v2 | aroon_25_trend | 9765.71 | -234.29 | sell / filled / Aroon25 Up > 70 그리고 Down < 30 (동률이면 최신 극값); 조건 미충족; Aroon_up=96, Aroon_down=100; 직전 완료 봉 목표를 다음 봉 시가에 모의 적용 |
| v2 | cci_20_momentum | 9671.34 | -328.66 | sell / filled / CCI20 > 100 (전형가격·평균절대편차); 조건 미충족; CCI20=-280.713; 직전 완료 봉 목표를 다음 봉 시가에 모의 적용 |
| v2 | williams_14_recovery | 9491.44 | -508.56 | sell / filled / 직전 Williams %R14 < -80, 현재 >= -80 (한 봉 목표); 조건 미충족; Williams_R14=-54.3945, previous_R14=-77.1479; 직전 완료 봉 목표를 다음 봉 시가에 모의 적용 |
| v2 | cmf_20_accumulation | 9633.99 | -366.01 | buy / partial / Chaikin Money Flow20 > 0.1; 조건 충족; CMF20=0.115539, volume20=2.04147e+06; 직전 완료 봉 목표를 다음 봉 시가에 모의 적용 |
| v2 | chaikin_3_10 | 9536.68 | -463.32 | sell / filled / ADL의 EMA3 - EMA10 > 0 그리고 종가 > EMA26; 조건 미충족; Chaikin3_10=268702, ADL=-8.90187e+06, close=332.6, EMA26=334.725; 직전 완료 봉 목표를 다음 봉 시가에 모의 적용 |
| v2 | roc_10_momentum | 9832.47 | -167.53 | sell / filled / 10봉 ROC > 1% 그리고 종가 > EMA26; 조건 미충족; ROC10_percent=0.964142, close=337.72, EMA26=336.695; 직전 완료 봉 목표를 다음 봉 시가에 모의 적용 |
| v2 | trix_15_trend | 9604.89 | -395.11 | sell / filled / 15봉 삼중 EMA의 1봉 변화율 TRIX > 0 그리고 종가 > EMA26; 조건 미충족; TRIX15_percent=0.00517218, close=332.6, EMA26=334.725; 직전 완료 봉 목표를 다음 봉 시가에 모의 적용 |
| v2 | keltner_20_breakout | 9901.28 | -98.72 | sell / filled / 종가 > EMA20 + 2 x Wilder ATR14; 조건 미충족; close=339.04, upper_Keltner=339.281, EMA20=336.559, ATR14=1.36146; 직전 완료 봉 목표를 다음 봉 시가에 모의 적용 |
| v2 | opening_range_30m | 9789.16 | -210.84 | sell / filled / 뉴욕 09:30·09:45 두 완료 봉 최고가를 10:00 이후 종가가 돌파; 자료 부족·변동폭 또는 거래량 없음: 대기; close=332.6; 직전 완료 봉 목표를 다음 봉 시가에 모의 적용 |

### 같은 기간의 비용·노출 비교 (사후 연구)

| 전략 | 비용 전 | 비용 후 | 100% 보유 | 같은 평균 노출 보유 | 평균 노출 |
|---|---:|---:|---:|---:|---:|
| cash | 0.00% | 0.00% | -0.63% | -0.00% | 0.00% |
| buy_hold | -0.22% | -0.63% | -0.63% | -0.63% | 100.00% |
| trend_8_26 | -0.78% | -4.87% | -0.63% | -0.34% | 53.26% |
| momentum_26 | -4.62% | -13.76% | -0.63% | -0.33% | 52.74% |
| breakout_8 | -3.66% | -18.90% | -0.63% | -0.12% | 18.54% |
| reversion_12 | 6.10% | -8.40% | -0.63% | -0.15% | 24.28% |
| volume_26 | 1.66% | -4.54% | -0.63% | -0.04% | 6.27% |
| trend_8_26 AND momentum_26 | -0.41% | -6.49% | -0.63% | -0.26% | 41.25% |
| trend_8_26 + momentum_26 | -2.71% | -9.23% | -0.63% | -0.34% | 53.01% |
| trend_8_26 AND breakout_8 | -3.16% | -13.54% | -0.63% | -0.07% | 11.49% |
| trend_8_26 + breakout_8 | -2.21% | -11.59% | -0.63% | -0.23% | 35.91% |
| trend_8_26 AND reversion_12 | 1.24% | -4.95% | -0.63% | -0.05% | 7.83% |
| trend_8_26 + reversion_12 | 2.62% | -6.26% | -0.63% | -0.25% | 38.78% |
| trend_8_26 AND volume_26 | 0.99% | -2.35% | -0.63% | -0.02% | 3.92% |
| trend_8_26 + volume_26 | 0.45% | -4.70% | -0.63% | -0.19% | 29.77% |
| momentum_26 AND breakout_8 | -3.71% | -15.46% | -0.63% | -0.08% | 12.53% |
| momentum_26 + breakout_8 | -4.11% | -16.18% | -0.63% | -0.23% | 35.65% |
| momentum_26 AND reversion_12 | 1.94% | -4.68% | -0.63% | -0.04% | 6.53% |
| momentum_26 + reversion_12 | 0.63% | -8.66% | -0.63% | -0.24% | 38.52% |
| momentum_26 AND volume_26 | -0.68% | -3.96% | -0.63% | -0.02% | 3.13% |
| momentum_26 + volume_26 | -1.50% | -8.69% | -0.63% | -0.19% | 29.51% |
| breakout_8 AND reversion_12 | 0.00% | 0.00% | -0.63% | -0.00% | 0.00% |
| breakout_8 + reversion_12 | 1.12% | -12.53% | -0.63% | -0.14% | 21.42% |
| breakout_8 AND volume_26 | 0.94% | -1.16% | -0.63% | -0.01% | 1.31% |
| breakout_8 + volume_26 | -1.02% | -11.08% | -0.63% | -0.08% | 12.41% |
| reversion_12 AND volume_26 | 1.89% | -1.06% | -0.63% | -0.01% | 2.35% |
| reversion_12 + volume_26 | 3.87% | -5.51% | -0.63% | -0.10% | 15.28% |
| ema_12_26 | -2.04% | -6.07% | -0.63% | -0.32% | 49.87% |
| macd_12_26_9 | -1.98% | -7.19% | -0.63% | -0.20% | 31.85% |
| rsi_14_recovery | 0.40% | -0.86% | -0.63% | -0.00% | 0.78% |
| bollinger_20_reentry | 1.01% | -3.15% | -0.63% | -0.02% | 2.61% |
| donchian_20 | -2.16% | -5.78% | -0.63% | -0.02% | 3.13% |
| atr_14_breakout | -1.29% | -8.87% | -0.63% | -0.03% | 5.22% |
| session_vwap | -0.22% | -10.91% | -0.63% | -0.32% | 50.65% |
| obv_20 | -4.01% | -16.08% | -0.63% | -0.18% | 27.94% |
| stochastic_14_3_recovery | 0.21% | -9.78% | -0.63% | -0.04% | 6.53% |
| mfi_14_recovery | 0.12% | -1.13% | -0.63% | -0.00% | 0.78% |
| adx_14_trend | -2.34% | -4.37% | -0.63% | -0.16% | 24.80% |
| aroon_25_trend | -1.20% | -4.86% | -0.63% | -0.11% | 17.75% |
| cci_20_momentum | -3.21% | -11.38% | -0.63% | -0.10% | 16.45% |
| williams_14_recovery | -0.32% | -9.50% | -0.63% | -0.04% | 6.01% |
| cmf_20_accumulation | -2.57% | -10.04% | -0.63% | -0.24% | 37.08% |
| chaikin_3_10 | 1.13% | -8.18% | -0.63% | -0.21% | 33.68% |
| roc_10_momentum | -1.40% | -3.86% | -0.63% | -0.04% | 6.53% |
| trix_15_trend | -1.12% | -7.93% | -0.63% | -0.22% | 34.73% |
| keltner_20_breakout | -0.35% | -2.83% | -0.63% | -0.02% | 3.92% |
| opening_range_30m | -0.69% | -4.38% | -0.63% | -0.11% | 16.97% |

동일 구간·초기 자금, 종료 시 청산 비용 포함. 노출 맞춤은 사후 설명용이며 v2 실제 계좌 성과가 아닙니다.
[낙폭 분해·비용 영향·전체 구간](JPM/comparison.json)

[v1 전체 기록](JPM/accounts.json) · [v2 전체 기록](JPM/accounts-v2.json)

## XOM 계좌

| 모델 | 전략 | 평가액 USD | 손익 USD | 최근 매매·이유 |
|---|---|---:|---:|---|
| v1 | cash | 10000.00 | 0.00 | 대기 /  / 새 신호 대기 |
| v1 | buy_hold | 10349.58 | 349.58 | buy /  / buy_hold: prior completed bar target 100%; next bar open simulation |
| v1 | trend_8_26 | 9997.97 | -2.03 | buy /  / trend_8_26: prior completed bar target 100%; next bar open simulation |
| v1 | momentum_26 | 9991.68 | -8.32 | buy /  / momentum_26: prior completed bar target 100%; next bar open simulation |
| v1 | breakout_8 | 9470.37 | -529.63 | buy /  / breakout_8: prior completed bar target 100%; next bar open simulation |
| v1 | reversion_12 | 9517.47 | -482.53 | sell /  / reversion_12: prior completed bar target 0%; next bar open simulation |
| v1 | volume_26 | 9554.35 | -445.65 | sell /  / volume_26: prior completed bar target 0%; next bar open simulation |
| v1 | trend_8_26 AND momentum_26 | 9859.47 | -140.53 | buy /  / trend_8_26 AND momentum_26: prior completed bar target 100%; next bar open simulation |
| v1 | trend_8_26 + momentum_26 | 9995.10 | -4.90 | buy /  / trend_8_26 + momentum_26: prior completed bar target 100%; next bar open simulation |
| v1 | trend_8_26 AND breakout_8 | 9681.59 | -318.41 | buy /  / trend_8_26 AND breakout_8: prior completed bar target 100%; next bar open simulation |
| v1 | trend_8_26 + breakout_8 | 9770.27 | -229.73 | buy /  / trend_8_26 + breakout_8: prior completed bar target 100%; next bar open simulation |
| v1 | trend_8_26 AND reversion_12 | 9545.50 | -454.50 | sell /  / trend_8_26 AND reversion_12: prior completed bar target 0%; next bar open simulation |
| v1 | trend_8_26 + reversion_12 | 9754.88 | -245.12 | sell /  / trend_8_26 + reversion_12: prior completed bar target 50%; next bar open simulation |
| v1 | trend_8_26 AND volume_26 | 9669.14 | -330.86 | sell /  / trend_8_26 AND volume_26: prior completed bar target 0%; next bar open simulation |
| v1 | trend_8_26 + volume_26 | 9774.14 | -225.86 | sell /  / trend_8_26 + volume_26: prior completed bar target 50%; next bar open simulation |
| v1 | momentum_26 AND breakout_8 | 9801.37 | -198.63 | buy /  / momentum_26 AND breakout_8: prior completed bar target 100%; next bar open simulation |
| v1 | momentum_26 + breakout_8 | 9727.94 | -272.06 | buy /  / momentum_26 + breakout_8: prior completed bar target 100%; next bar open simulation |
| v1 | momentum_26 AND reversion_12 | 9642.75 | -357.25 | sell /  / momentum_26 AND reversion_12: prior completed bar target 0%; next bar open simulation |
| v1 | momentum_26 + reversion_12 | 9751.69 | -248.31 | sell /  / momentum_26 + reversion_12: prior completed bar target 50%; next bar open simulation |
| v1 | momentum_26 AND volume_26 | 9888.17 | -111.83 | sell /  / momentum_26 AND volume_26: prior completed bar target 0%; next bar open simulation |
| v1 | momentum_26 + volume_26 | 9770.74 | -229.26 | sell /  / momentum_26 + volume_26: prior completed bar target 50%; next bar open simulation |
| v1 | breakout_8 AND reversion_12 | 10000.00 | 0.00 | 대기 /  / 새 신호 대기 |
| v1 | breakout_8 + reversion_12 | 9512.82 | -487.18 | buy /  / breakout_8 + reversion_12: prior completed bar target 50%; next bar open simulation |
| v1 | breakout_8 AND volume_26 | 9896.24 | -103.76 | sell /  / breakout_8 AND volume_26: prior completed bar target 0%; next bar open simulation |
| v1 | breakout_8 + volume_26 | 9512.16 | -487.84 | buy /  / breakout_8 + volume_26: prior completed bar target 50%; next bar open simulation |
| v1 | reversion_12 AND volume_26 | 9794.27 | -205.73 | sell /  / reversion_12 AND volume_26: prior completed bar target 0%; next bar open simulation |
| v1 | reversion_12 + volume_26 | 9536.04 | -463.96 | sell /  / reversion_12 + volume_26: prior completed bar target 0%; next bar open simulation |
| v1 | ema_12_26 | 10066.71 | 66.71 | buy /  / EMA12 > EMA26; 조건 충족; EMA12=176.974, EMA26=176.95 |
| v1 | macd_12_26_9 | 10047.23 | 47.23 | sell /  / MACD > 신호선 그리고 MACD > 0; 조건 미충족; MACD=1.35319, signal9=1.41024 |
| v1 | rsi_14_recovery | 9927.64 | -72.36 | sell /  / 직전 RSI14 < 30, 현재 RSI14 >= 30 (한 봉 목표); 조건 미충족; RSI14=37.639, previous_RSI14=31.1023 |
| v1 | bollinger_20_reentry | 9694.21 | -305.79 | sell /  / 직전 종가 < 직전 하단밴드, 현재 하단밴드 <= 종가 <= SMA20 (한 봉 목표); 조건 미충족; close=175.53, lower20=174.782, SMA20=177.101, previous_lower20=174.994 |
| v1 | donchian_20 | 9754.38 | -245.62 | sell /  / 종가 > 현재 봉을 제외한 직전 20봉 최고가; 조건 미충족; close=183.28, prior_high20=183.3 |
| v1 | atr_14_breakout | 9789.04 | -210.96 | sell /  / 종가 > 직전 종가 + 직전 ATR14 그리고 종가 > EMA26; 조건 미충족; close=181.355, threshold=182.652, prior_ATR14=0.727068, EMA26=178.133 |
| v1 | session_vwap | 9997.73 | -2.27 | buy /  / 종가 > 뉴욕 거래일별 누적 전형가격 VWAP; 조건 충족; close=182.5, session_VWAP=182.493, session_volume=1.26203e+07 |
| v1 | obv_20 | 9569.39 | -430.61 | buy /  / OBV > OBV의 SMA20 그리고 종가 > EMA26; 조건 충족; OBV=2.26159e+07, OBV_SMA20=2.18428e+07, close=176.86, EMA26=176.75 |
| v1 | stochastic_14_3_recovery | 9636.26 | -363.74 | sell /  / 직전 %K14 < 20에서 %K14가 %D3 상향 돌파 (한 봉 목표); 조건 미충족; K14=11.8836, D3=5.65987, previous_K14=4.66302, previous_D3=2.02546 |
| v1 | mfi_14_recovery | 10000.00 | 0.00 | 대기 /  / 새 신호 대기 |
| v1 | adx_14_trend | 10070.29 | 70.29 | buy /  / Wilder ADX14 >= 25 그리고 +DI14 > -DI14; 조건 충족; ADX14=26.2258, plus_DI14=52.4409, minus_DI14=10.4732 |
| v1 | aroon_25_trend | 9626.27 | -373.73 | sell /  / Aroon25 Up > 70 그리고 Down < 30 (동률이면 최신 극값); 조건 미충족; Aroon_up=68, Aroon_down=4 |
| v1 | cci_20_momentum | 9460.38 | -539.62 | sell /  / CCI20 > 100 (전형가격·평균절대편차); 조건 미충족; CCI20=95.1299 |
| v1 | williams_14_recovery | 9618.15 | -381.85 | sell /  / 직전 Williams %R14 < -80, 현재 >= -80 (한 봉 목표); 조건 미충족; Williams_R14=-55.2881, previous_R14=-73.5295 |
| v1 | cmf_20_accumulation | 9966.70 | -33.30 | buy /  / Chaikin Money Flow20 > 0.1; 조건 충족; CMF20=0.202217, volume20=4.5047e+06 |
| v1 | chaikin_3_10 | 9928.65 | -71.35 | buy /  / ADL의 EMA3 - EMA10 > 0 그리고 종가 > EMA26; 조건 충족; Chaikin3_10=152048, ADL=2.84951e+07, close=176.86, EMA26=176.75 |
| v1 | roc_10_momentum | 9912.41 | -87.59 | sell /  / 10봉 ROC > 1% 그리고 종가 > EMA26; 조건 미충족; ROC10_percent=0.733814, close=183.26, EMA26=180.514 |
| v1 | trix_15_trend | 10016.54 | 16.54 | buy /  / 15봉 삼중 EMA의 1봉 변화율 TRIX > 0 그리고 종가 > EMA26; 조건 충족; TRIX15_percent=0.00288954, close=177.71, EMA26=177.21 |
| v1 | keltner_20_breakout | 9898.00 | -102.00 | sell /  / 종가 > EMA20 + 2 x Wilder ATR14; 조건 미충족; close=182.29, upper_Keltner=182.66, EMA20=181.48, ATR14=0.590087 |
| v1 | opening_range_30m | 9999.37 | -0.63 | buy /  / 뉴욕 09:30·09:45 두 완료 봉 최고가를 10:00 이후 종가가 돌파; 조건 충족; close=182.19, opening_high=181.96 |
| v2 | cash | 10000.00 | 0.00 | 대기 /  / 새 신호 대기 |
| v2 | buy_hold | 10679.86 | 679.86 | buy / partial / 직전 완료 봉 목표 비중 100%; 다음 봉 시가 가정 |
| v2 | trend_8_26 | 10085.12 | 85.12 | buy / partial / 직전 완료 봉 목표 비중 100%; 다음 봉 시가 가정 |
| v2 | momentum_26 | 10157.07 | 157.07 | buy / partial / 직전 완료 봉 목표 비중 100%; 다음 봉 시가 가정 |
| v2 | breakout_8 | 8988.95 | -1011.05 | 중단: 손실 한도 / sell / filled / 직전 완료 봉 목표 비중 0%; 다음 봉 시가 가정 |
| v2 | reversion_12 | 9330.25 | -669.75 | sell / filled / 직전 완료 봉 목표 비중 0%; 다음 봉 시가 가정 |
| v2 | volume_26 | 9451.35 | -548.65 | sell / filled / 직전 완료 봉 목표 비중 0%; 다음 봉 시가 가정 |
| v2 | trend_8_26 AND momentum_26 | 9950.80 | -49.20 | buy / partial / 직전 완료 봉 목표 비중 100%; 다음 봉 시가 가정 |
| v2 | trend_8_26 + momentum_26 | 10121.33 | 121.33 | buy / partial / 직전 완료 봉 목표 비중 100%; 다음 봉 시가 가정 |
| v2 | trend_8_26 AND breakout_8 | 9128.04 | -871.96 | buy / partial / 직전 완료 봉 목표 비중 100%; 다음 봉 시가 가정 |
| v2 | trend_8_26 + breakout_8 | 9553.38 | -446.62 | buy / partial / 직전 완료 봉 목표 비중 100%; 다음 봉 시가 가정 |
| v2 | trend_8_26 AND reversion_12 | 9381.23 | -618.77 | sell / filled / 직전 완료 봉 목표 비중 0%; 다음 봉 시가 가정 |
| v2 | trend_8_26 + reversion_12 | 9700.51 | -299.49 | sell / filled / 직전 완료 봉 목표 비중 50%; 다음 봉 시가 가정 |
| v2 | trend_8_26 AND volume_26 | 9556.73 | -443.27 | sell / filled / 직전 완료 봉 목표 비중 0%; 다음 봉 시가 가정 |
| v2 | trend_8_26 + volume_26 | 9763.52 | -236.48 | sell / filled / 직전 완료 봉 목표 비중 50%; 다음 봉 시가 가정 |
| v2 | momentum_26 AND breakout_8 | 9261.58 | -738.42 | buy / partial / 직전 완료 봉 목표 비중 100%; 다음 봉 시가 가정 |
| v2 | momentum_26 + breakout_8 | 9527.09 | -472.91 | buy / partial / 직전 완료 봉 목표 비중 100%; 다음 봉 시가 가정 |
| v2 | momentum_26 AND reversion_12 | 9440.57 | -559.43 | sell / filled / 직전 완료 봉 목표 비중 0%; 다음 봉 시가 가정 |
| v2 | momentum_26 + reversion_12 | 9734.95 | -265.05 | sell / filled / 직전 완료 봉 목표 비중 50%; 다음 봉 시가 가정 |
| v2 | momentum_26 AND volume_26 | 9838.73 | -161.27 | sell / filled / 직전 완료 봉 목표 비중 0%; 다음 봉 시가 가정 |
| v2 | momentum_26 + volume_26 | 9818.53 | -181.47 | sell / filled / 직전 완료 봉 목표 비중 50%; 다음 봉 시가 가정 |
| v2 | breakout_8 AND reversion_12 | 10000.00 | 0.00 | 대기 /  / 새 신호 대기 |
| v2 | breakout_8 + reversion_12 | 9149.20 | -850.80 | buy / filled / 직전 완료 봉 목표 비중 50%; 다음 봉 시가 가정 |
| v2 | breakout_8 AND volume_26 | 9860.88 | -139.12 | sell / filled / 직전 완료 봉 목표 비중 0%; 다음 봉 시가 가정 |
| v2 | breakout_8 + volume_26 | 9208.38 | -791.62 | buy / filled / 직전 완료 봉 목표 비중 50%; 다음 봉 시가 가정 |
| v2 | reversion_12 AND volume_26 | 9737.38 | -262.62 | sell / filled / 직전 완료 봉 목표 비중 0%; 다음 봉 시가 가정 |
| v2 | reversion_12 + volume_26 | 9410.50 | -589.50 | sell / filled / 직전 완료 봉 목표 비중 0%; 다음 봉 시가 가정 |
| v2 | ema_12_26 | 10059.67 | 59.67 | buy / partial / EMA12 > EMA26; 조건 충족; EMA12=176.974, EMA26=176.95; 직전 완료 봉 목표를 다음 봉 시가에 모의 적용 |
| v2 | macd_12_26_9 | 10035.18 | 35.18 | sell / filled / MACD > 신호선 그리고 MACD > 0; 조건 미충족; MACD=1.35319, signal9=1.41024; 직전 완료 봉 목표를 다음 봉 시가에 모의 적용 |
| v2 | rsi_14_recovery | 9923.67 | -76.33 | sell / filled / 직전 RSI14 < 30, 현재 RSI14 >= 30 (한 봉 목표); 조건 미충족; RSI14=37.639, previous_RSI14=31.1023; 직전 완료 봉 목표를 다음 봉 시가에 모의 적용 |
| v2 | bollinger_20_reentry | 9684.52 | -315.48 | sell / filled / 직전 종가 < 직전 하단밴드, 현재 하단밴드 <= 종가 <= SMA20 (한 봉 목표); 조건 미충족; close=175.53, lower20=174.782, SMA20=177.101, previous_lower20=174.994; 직전 완료 봉 목표를 다음 봉 시가에 모의 적용 |
| v2 | donchian_20 | 9738.78 | -261.22 | sell / filled / 종가 > 현재 봉을 제외한 직전 20봉 최고가; 조건 미충족; close=183.28, prior_high20=183.3; 직전 완료 봉 목표를 다음 봉 시가에 모의 적용 |
| v2 | atr_14_breakout | 9777.30 | -222.70 | sell / filled / 종가 > 직전 종가 + 직전 ATR14 그리고 종가 > EMA26; 조건 미충족; close=181.355, threshold=182.652, prior_ATR14=0.727068, EMA26=178.133; 직전 완료 봉 목표를 다음 봉 시가에 모의 적용 |
| v2 | session_vwap | 9978.75 | -21.25 | buy / partial / 종가 > 뉴욕 거래일별 누적 전형가격 VWAP; 조건 충족; close=182.5, session_VWAP=182.493, session_volume=1.26203e+07; 직전 완료 봉 목표를 다음 봉 시가에 모의 적용 |
| v2 | obv_20 | 9502.46 | -497.54 | 중단: 손실 한도 / sell / filled / OBV > OBV의 SMA20 그리고 종가 > EMA26; 조건 미충족; OBV=2.24329e+07, OBV_SMA20=2.30895e+07, close=177.005, EMA26=177.393; 직전 완료 봉 목표를 다음 봉 시가에 모의 적용 |
| v2 | stochastic_14_3_recovery | 9622.78 | -377.22 | sell / filled / 직전 %K14 < 20에서 %K14가 %D3 상향 돌파 (한 봉 목표); 조건 미충족; K14=11.8836, D3=5.65987, previous_K14=4.66302, previous_D3=2.02546; 직전 완료 봉 목표를 다음 봉 시가에 모의 적용 |
| v2 | mfi_14_recovery | 10000.00 | 0.00 | 대기 /  / 새 신호 대기 |
| v2 | adx_14_trend | 10063.24 | 63.24 | buy / partial / Wilder ADX14 >= 25 그리고 +DI14 > -DI14; 조건 충족; ADX14=26.2258, plus_DI14=52.4409, minus_DI14=10.4732; 직전 완료 봉 목표를 다음 봉 시가에 모의 적용 |
| v2 | aroon_25_trend | 9616.65 | -383.35 | sell / filled / Aroon25 Up > 70 그리고 Down < 30 (동률이면 최신 극값); 조건 미충족; Aroon_up=68, Aroon_down=4; 직전 완료 봉 목표를 다음 봉 시가에 모의 적용 |
| v2 | cci_20_momentum | 9435.81 | -564.19 | sell / filled / CCI20 > 100 (전형가격·평균절대편차); 조건 미충족; CCI20=95.1299; 직전 완료 봉 목표를 다음 봉 시가에 모의 적용 |
| v2 | williams_14_recovery | 9602.77 | -397.23 | sell / filled / 직전 Williams %R14 < -80, 현재 >= -80 (한 봉 목표); 조건 미충족; Williams_R14=-55.2881, previous_R14=-73.5295; 직전 완료 봉 목표를 다음 봉 시가에 모의 적용 |
| v2 | cmf_20_accumulation | 9953.75 | -46.25 | buy / partial / Chaikin Money Flow20 > 0.1; 조건 충족; CMF20=0.202217, volume20=4.5047e+06; 직전 완료 봉 목표를 다음 봉 시가에 모의 적용 |
| v2 | chaikin_3_10 | 9911.79 | -88.21 | buy / partial / ADL의 EMA3 - EMA10 > 0 그리고 종가 > EMA26; 조건 충족; Chaikin3_10=152048, ADL=2.87515e+07, close=176.86, EMA26=176.75; 직전 완료 봉 목표를 다음 봉 시가에 모의 적용 |
| v2 | roc_10_momentum | 9900.52 | -99.48 | sell / filled / 10봉 ROC > 1% 그리고 종가 > EMA26; 조건 미충족; ROC10_percent=0.733814, close=183.26, EMA26=180.514; 직전 완료 봉 목표를 다음 봉 시가에 모의 적용 |
| v2 | trix_15_trend | 10003.53 | 3.53 | buy / partial / 15봉 삼중 EMA의 1봉 변화율 TRIX > 0 그리고 종가 > EMA26; 조건 충족; TRIX15_percent=0.00288954, close=177.71, EMA26=177.21; 직전 완료 봉 목표를 다음 봉 시가에 모의 적용 |
| v2 | keltner_20_breakout | 9888.11 | -111.89 | sell / filled / 종가 > EMA20 + 2 x Wilder ATR14; 조건 미충족; close=182.29, upper_Keltner=182.66, EMA20=181.48, ATR14=0.590087; 직전 완료 봉 목표를 다음 봉 시가에 모의 적용 |
| v2 | opening_range_30m | 9994.37 | -5.63 | buy / partial / 뉴욕 09:30·09:45 두 완료 봉 최고가를 10:00 이후 종가가 돌파; 조건 충족; close=182.19, opening_high=181.96; 직전 완료 봉 목표를 다음 봉 시가에 모의 적용 |

### 같은 기간의 비용·노출 비교 (사후 연구)

| 전략 | 비용 전 | 비용 후 | 100% 보유 | 같은 평균 노출 보유 | 평균 노출 |
|---|---:|---:|---:|---:|---:|
| cash | 0.00% | 0.00% | 11.83% | 0.00% | 0.00% |
| buy_hold | 12.30% | 11.83% | 11.83% | 11.83% | 100.00% |
| trend_8_26 | 6.05% | 2.11% | 11.83% | 8.29% | 71.28% |
| momentum_26 | 5.77% | 0.99% | 11.83% | 8.07% | 69.45% |
| breakout_8 | 1.68% | -16.18% | 11.83% | 3.11% | 27.42% |
| reversion_12 | 1.10% | -8.21% | 11.83% | 2.39% | 21.15% |
| volume_26 | 1.18% | -6.19% | 11.83% | 0.61% | 5.48% |
| trend_8_26 AND momentum_26 | 4.18% | -0.52% | 11.83% | 7.15% | 61.88% |
| trend_8_26 + momentum_26 | 5.92% | 1.56% | 11.83% | 8.18% | 70.37% |
| trend_8_26 AND breakout_8 | 1.80% | -12.85% | 11.83% | 2.45% | 21.67% |
| trend_8_26 + breakout_8 | 3.86% | -6.89% | 11.83% | 5.66% | 49.35% |
| trend_8_26 AND reversion_12 | -1.71% | -7.32% | 11.83% | 1.17% | 10.44% |
| trend_8_26 + reversion_12 | 3.57% | -2.98% | 11.83% | 5.29% | 46.22% |
| trend_8_26 AND volume_26 | 0.50% | -4.44% | 11.83% | 0.41% | 3.66% |
| trend_8_26 + volume_26 | 3.61% | -1.92% | 11.83% | 4.38% | 38.38% |
| momentum_26 AND breakout_8 | 1.75% | -12.90% | 11.83% | 2.54% | 22.45% |
| momentum_26 + breakout_8 | 3.72% | -7.98% | 11.83% | 5.56% | 48.44% |
| momentum_26 AND reversion_12 | -0.00% | -6.89% | 11.83% | 1.17% | 10.44% |
| momentum_26 + reversion_12 | 3.43% | -3.31% | 11.83% | 5.19% | 45.30% |
| momentum_26 AND volume_26 | 1.74% | -2.03% | 11.83% | 0.26% | 2.35% |
| momentum_26 + volume_26 | 3.47% | -2.05% | 11.83% | 4.27% | 37.47% |
| breakout_8 AND reversion_12 | 0.00% | 0.00% | 11.83% | 0.00% | 0.00% |
| breakout_8 + reversion_12 | 1.41% | -11.92% | 11.83% | 2.75% | 24.29% |
| breakout_8 AND volume_26 | 0.76% | -1.75% | 11.83% | 0.17% | 1.57% |
| breakout_8 + volume_26 | 1.44% | -10.77% | 11.83% | 1.85% | 16.46% |
| reversion_12 AND volume_26 | -0.04% | -3.35% | 11.83% | 0.26% | 2.35% |
| reversion_12 + volume_26 | 1.15% | -6.62% | 11.83% | 1.50% | 13.32% |
| ema_12_26 | 5.68% | 2.62% | 11.83% | 8.86% | 75.98% |
| macd_12_26_9 | 3.85% | -2.08% | 11.83% | 4.83% | 42.30% |
| rsi_14_recovery | 0.07% | -0.76% | 11.83% | 0.06% | 0.52% |
| bollinger_20_reentry | -1.49% | -4.34% | 11.83% | 0.20% | 1.83% |
| donchian_20 | 0.04% | -8.41% | 11.83% | 1.17% | 10.44% |
| atr_14_breakout | 0.86% | -7.27% | 11.83% | 0.64% | 5.74% |
| session_vwap | 6.08% | -5.29% | 11.83% | 7.41% | 63.97% |
| obv_20 | 3.45% | -6.86% | 11.83% | 5.85% | 50.91% |
| stochastic_14_3_recovery | 0.20% | -9.02% | 11.83% | 0.67% | 6.01% |
| mfi_14_recovery | -0.31% | -1.97% | 11.83% | 0.12% | 1.04% |
| adx_14_trend | 4.27% | 1.25% | 11.83% | 4.99% | 43.60% |
| aroon_25_trend | -1.71% | -8.10% | 11.83% | 3.89% | 34.20% |
| cci_20_momentum | 2.35% | -7.47% | 11.83% | 3.35% | 29.50% |
| williams_14_recovery | -0.92% | -6.97% | 11.83% | 0.44% | 3.92% |
| cmf_20_accumulation | 4.28% | -2.09% | 11.83% | 6.03% | 52.48% |
| chaikin_3_10 | 6.53% | -2.46% | 11.83% | 7.12% | 61.62% |
| roc_10_momentum | 1.32% | -4.87% | 11.83% | 1.70% | 15.14% |
| trix_15_trend | 5.12% | -0.89% | 11.83% | 7.19% | 62.14% |
| keltner_20_breakout | 0.94% | -5.62% | 11.83% | 2.24% | 19.84% |
| opening_range_30m | 0.48% | -6.44% | 11.83% | 3.29% | 28.98% |

동일 구간·초기 자금, 종료 시 청산 비용 포함. 노출 맞춤은 사후 설명용이며 v2 실제 계좌 성과가 아닙니다.
[낙폭 분해·비용 영향·전체 구간](XOM/comparison.json)

[v1 전체 기록](XOM/accounts.json) · [v2 전체 기록](XOM/accounts-v2.json)

## JNJ 계좌

| 모델 | 전략 | 평가액 USD | 손익 USD | 최근 매매·이유 |
|---|---|---:|---:|---|
| v1 | cash | 10000.00 | 0.00 | 대기 /  / 새 신호 대기 |
| v1 | buy_hold | 10298.16 | 298.16 | buy /  / buy_hold: prior completed bar target 100%; next bar open simulation |
| v1 | trend_8_26 | 10203.47 | 203.47 | sell /  / trend_8_26: prior completed bar target 0%; next bar open simulation |
| v1 | momentum_26 | 9644.97 | -355.03 | sell /  / momentum_26: prior completed bar target 0%; next bar open simulation |
| v1 | breakout_8 | 9408.78 | -591.22 | buy /  / breakout_8: prior completed bar target 100%; next bar open simulation |
| v1 | reversion_12 | 9608.51 | -391.49 | sell /  / reversion_12: prior completed bar target 0%; next bar open simulation |
| v1 | volume_26 | 10040.58 | 40.58 | sell /  / volume_26: prior completed bar target 0%; next bar open simulation |
| v1 | trend_8_26 AND momentum_26 | 9811.53 | -188.47 | sell /  / trend_8_26 AND momentum_26: prior completed bar target 0%; next bar open simulation |
| v1 | trend_8_26 + momentum_26 | 9940.65 | -59.35 | sell /  / trend_8_26 + momentum_26: prior completed bar target 0%; next bar open simulation |
| v1 | trend_8_26 AND breakout_8 | 9864.21 | -135.79 | sell /  / trend_8_26 AND breakout_8: prior completed bar target 0%; next bar open simulation |
| v1 | trend_8_26 + breakout_8 | 9818.26 | -181.74 | buy /  / trend_8_26 + breakout_8: prior completed bar target 50%; next bar open simulation |
| v1 | trend_8_26 AND reversion_12 | 9807.21 | -192.79 | sell /  / trend_8_26 AND reversion_12: prior completed bar target 0%; next bar open simulation |
| v1 | trend_8_26 + reversion_12 | 9901.79 | -98.21 | sell /  / trend_8_26 + reversion_12: prior completed bar target 0%; next bar open simulation |
| v1 | trend_8_26 AND volume_26 | 10134.54 | 134.54 | sell /  / trend_8_26 AND volume_26: prior completed bar target 0%; next bar open simulation |
| v1 | trend_8_26 + volume_26 | 10122.01 | 122.01 | sell /  / trend_8_26 + volume_26: prior completed bar target 0%; next bar open simulation |
| v1 | momentum_26 AND breakout_8 | 9703.66 | -296.34 | sell /  / momentum_26 AND breakout_8: prior completed bar target 0%; next bar open simulation |
| v1 | momentum_26 + breakout_8 | 9526.48 | -473.52 | buy /  / momentum_26 + breakout_8: prior completed bar target 50%; next bar open simulation |
| v1 | momentum_26 AND reversion_12 | 9708.77 | -291.23 | sell /  / momentum_26 AND reversion_12: prior completed bar target 0%; next bar open simulation |
| v1 | momentum_26 + reversion_12 | 9665.24 | -334.76 | sell /  / momentum_26 + reversion_12: prior completed bar target 0%; next bar open simulation |
| v1 | momentum_26 AND volume_26 | 10000.00 | 0.00 | 대기 /  / 새 신호 대기 |
| v1 | momentum_26 + volume_26 | 9900.29 | -99.71 | sell /  / momentum_26 + volume_26: prior completed bar target 0%; next bar open simulation |
| v1 | breakout_8 AND reversion_12 | 10000.00 | 0.00 | 대기 /  / 새 신호 대기 |
| v1 | breakout_8 + reversion_12 | 9507.88 | -492.12 | buy /  / breakout_8 + reversion_12: prior completed bar target 50%; next bar open simulation |
| v1 | breakout_8 AND volume_26 | 10139.49 | 139.49 | sell /  / breakout_8 AND volume_26: prior completed bar target 0%; next bar open simulation |
| v1 | breakout_8 + volume_26 | 9738.88 | -261.12 | buy /  / breakout_8 + volume_26: prior completed bar target 50%; next bar open simulation |
| v1 | reversion_12 AND volume_26 | 9933.02 | -66.98 | sell /  / reversion_12 AND volume_26: prior completed bar target 0%; next bar open simulation |
| v1 | reversion_12 + volume_26 | 9841.98 | -158.02 | sell /  / reversion_12 + volume_26: prior completed bar target 0%; next bar open simulation |
| v1 | ema_12_26 | 9827.67 | -172.33 | sell /  / EMA12 > EMA26; 조건 미충족; EMA12=264.816, EMA26=264.953 |
| v1 | macd_12_26_9 | 10152.66 | 152.66 | sell /  / MACD > 신호선 그리고 MACD > 0; 조건 미충족; MACD=2.48372, signal9=2.49952 |
| v1 | rsi_14_recovery | 9923.04 | -76.96 | sell /  / 직전 RSI14 < 30, 현재 RSI14 >= 30 (한 봉 목표); 조건 미충족; RSI14=40.3665, previous_RSI14=36.2025 |
| v1 | bollinger_20_reentry | 9778.51 | -221.49 | sell /  / 직전 종가 < 직전 하단밴드, 현재 하단밴드 <= 종가 <= SMA20 (한 봉 목표); 조건 미충족; close=263.43, lower20=262.644, SMA20=266.981, previous_lower20=263.145 |
| v1 | donchian_20 | 9779.77 | -220.23 | sell /  / 종가 > 현재 봉을 제외한 직전 20봉 최고가; 조건 미충족; close=268.59, prior_high20=269.55 |
| v1 | atr_14_breakout | 9634.41 | -365.59 | sell /  / 종가 > 직전 종가 + 직전 ATR14 그리고 종가 > EMA26; 조건 미충족; close=269.05, threshold=269.858, prior_ATR14=0.907979, EMA26=264.623 |
| v1 | session_vwap | 9916.59 | -83.41 | buy /  / 종가 > 뉴욕 거래일별 누적 전형가격 VWAP; 조건 충족; close=263.62, session_VWAP=263.396, session_volume=3.37048e+06 |
| v1 | obv_20 | 9789.37 | -210.63 | sell /  / OBV > OBV의 SMA20 그리고 종가 > EMA26; 조건 미충족; OBV=2.01573e+07, OBV_SMA20=2.06236e+07, close=267.68, EMA26=266.081 |
| v1 | stochastic_14_3_recovery | 9415.97 | -584.03 | sell /  / 직전 %K14 < 20에서 %K14가 %D3 상향 돌파 (한 봉 목표); 조건 미충족; K14=13.4247, D3=7.95839, previous_K14=6.19489, previous_D3=6.11994 |
| v1 | mfi_14_recovery | 9931.49 | -68.51 | sell /  / 직전 MFI14 < 20, 현재 MFI14 >= 20 (한 봉 목표); 조건 미충족; MFI14=35.8262, previous_MFI14=31.0222 |
| v1 | adx_14_trend | 9672.00 | -328.00 | sell /  / Wilder ADX14 >= 25 그리고 +DI14 > -DI14; 조건 미충족; ADX14=53.7666, plus_DI14=23.1641, minus_DI14=36.2315 |
| v1 | aroon_25_trend | 9974.61 | -25.39 | sell /  / Aroon25 Up > 70 그리고 Down < 30 (동률이면 최신 극값); 조건 미충족; Aroon_up=76, Aroon_down=100 |
| v1 | cci_20_momentum | 10114.24 | 114.24 | buy /  / CCI20 > 100 (전형가격·평균절대편차); 조건 충족; CCI20=105.231 |
| v1 | williams_14_recovery | 9681.74 | -318.26 | sell /  / 직전 Williams %R14 < -80, 현재 >= -80 (한 봉 목표); 조건 미충족; Williams_R14=-48.9017, previous_R14=-71.9776 |
| v1 | cmf_20_accumulation | 10240.33 | 240.33 | sell /  / Chaikin Money Flow20 > 0.1; 조건 미충족; CMF20=-0.188785, volume20=4.96784e+06 |
| v1 | chaikin_3_10 | 10085.51 | 85.51 | sell /  / ADL의 EMA3 - EMA10 > 0 그리고 종가 > EMA26; 조건 미충족; Chaikin3_10=-220136, ADL=1.31662e+07, close=267.68, EMA26=266.081 |
| v1 | roc_10_momentum | 9834.72 | -165.28 | sell /  / 10봉 ROC > 1% 그리고 종가 > EMA26; 조건 미충족; ROC10_percent=0.555956, close=268.59, EMA26=264.916 |
| v1 | trix_15_trend | 9665.47 | -334.53 | sell /  / 15봉 삼중 EMA의 1봉 변화율 TRIX > 0 그리고 종가 > EMA26; 조건 미충족; TRIX15_percent=0.123572, close=263.8, EMA26=265.912 |
| v1 | keltner_20_breakout | 10029.96 | 29.96 | sell /  / 종가 > EMA20 + 2 x Wilder ATR14; 조건 미충족; close=267.68, upper_Keltner=268.805, EMA20=266.948, ATR14=0.92845 |
| v1 | opening_range_30m | 9973.31 | -26.69 | sell /  / 뉴욕 09:30·09:45 두 완료 봉 최고가를 10:00 이후 종가가 돌파; 자료 부족·변동폭 또는 거래량 없음: 대기; close=263.8 |
| v2 | cash | 10000.00 | 0.00 | 대기 /  / 새 신호 대기 |
| v2 | buy_hold | 10057.80 | 57.80 | 중단: 손실 한도 / buy / partial / 직전 완료 봉 목표 비중 100%; 다음 봉 시가 가정 |
| v2 | trend_8_26 | 10057.80 | 57.80 | 중단: 손실 한도 / buy / partial / 직전 완료 봉 목표 비중 100%; 다음 봉 시가 가정 |
| v2 | momentum_26 | 10057.80 | 57.80 | 중단: 손실 한도 / buy / partial / 직전 완료 봉 목표 비중 100%; 다음 봉 시가 가정 |
| v2 | breakout_8 | 9343.39 | -656.61 | 중단: 손실 한도 / sell / filled / 직전 완료 봉 목표 비중 0%; 다음 봉 시가 가정 |
| v2 | reversion_12 | 9295.90 | -704.10 | sell / filled / 직전 완료 봉 목표 비중 0%; 다음 봉 시가 가정 |
| v2 | volume_26 | 9819.31 | -180.69 | sell / filled / 직전 완료 봉 목표 비중 0%; 다음 봉 시가 가정 |
| v2 | trend_8_26 AND momentum_26 | 10057.80 | 57.80 | 중단: 손실 한도 / buy / partial / 직전 완료 봉 목표 비중 100%; 다음 봉 시가 가정 |
| v2 | trend_8_26 + momentum_26 | 10057.80 | 57.80 | 중단: 손실 한도 / buy / partial / 직전 완료 봉 목표 비중 100%; 다음 봉 시가 가정 |
| v2 | trend_8_26 AND breakout_8 | 9419.39 | -580.61 | 중단: 손실 한도 / sell / filled / 직전 완료 봉 목표 비중 0%; 다음 봉 시가 가정 |
| v2 | trend_8_26 + breakout_8 | 9375.69 | -624.31 | buy / filled / 직전 완료 봉 목표 비중 50%; 다음 봉 시가 가정 |
| v2 | trend_8_26 AND reversion_12 | 9775.94 | -224.06 | sell / filled / 직전 완료 봉 목표 비중 0%; 다음 봉 시가 가정 |
| v2 | trend_8_26 + reversion_12 | 9732.92 | -267.08 | 중단: 손실 한도 / sell / filled / 직전 완료 봉 목표 비중 0%; 다음 봉 시가 가정 |
| v2 | trend_8_26 AND volume_26 | 9997.51 | -2.49 | sell / filled / 직전 완료 봉 목표 비중 0%; 다음 봉 시가 가정 |
| v2 | trend_8_26 + volume_26 | 10005.88 | 5.88 | 중단: 손실 한도 / buy / filled / 직전 완료 봉 목표 비중 50%; 다음 봉 시가 가정 |
| v2 | momentum_26 AND breakout_8 | 9297.50 | -702.50 | sell / filled / 직전 완료 봉 목표 비중 0%; 다음 봉 시가 가정 |
| v2 | momentum_26 + breakout_8 | 9085.79 | -914.21 | buy / filled / 직전 완료 봉 목표 비중 50%; 다음 봉 시가 가정 |
| v2 | momentum_26 AND reversion_12 | 9637.84 | -362.16 | sell / filled / 직전 완료 봉 목표 비중 0%; 다음 봉 시가 가정 |
| v2 | momentum_26 + reversion_12 | 9732.92 | -267.08 | 중단: 손실 한도 / sell / filled / 직전 완료 봉 목표 비중 0%; 다음 봉 시가 가정 |
| v2 | momentum_26 AND volume_26 | 9920.93 | -79.07 | sell / filled / 직전 완료 봉 목표 비중 0%; 다음 봉 시가 가정 |
| v2 | momentum_26 + volume_26 | 10005.88 | 5.88 | 중단: 손실 한도 / buy / filled / 직전 완료 봉 목표 비중 50%; 다음 봉 시가 가정 |
| v2 | breakout_8 AND reversion_12 | 10000.00 | 0.00 | 대기 /  / 새 신호 대기 |
| v2 | breakout_8 + reversion_12 | 9084.49 | -915.51 | buy / filled / 직전 완료 봉 목표 비중 50%; 다음 봉 시가 가정 |
| v2 | breakout_8 AND volume_26 | 9949.08 | -50.92 | sell / filled / 직전 완료 봉 목표 비중 0%; 다음 봉 시가 가정 |
| v2 | breakout_8 + volume_26 | 9336.79 | -663.21 | buy / filled / 직전 완료 봉 목표 비중 50%; 다음 봉 시가 가정 |
| v2 | reversion_12 AND volume_26 | 9816.09 | -183.91 | sell / filled / 직전 완료 봉 목표 비중 0%; 다음 봉 시가 가정 |
| v2 | reversion_12 + volume_26 | 9594.59 | -405.41 | sell / filled / 직전 완료 봉 목표 비중 0%; 다음 봉 시가 가정 |
| v2 | ema_12_26 | 9819.81 | -180.19 | sell / filled / EMA12 > EMA26; 조건 미충족; EMA12=264.816, EMA26=264.953; 직전 완료 봉 목표를 다음 봉 시가에 모의 적용 |
| v2 | macd_12_26_9 | 10144.54 | 144.54 | sell / filled / MACD > 신호선 그리고 MACD > 0; 조건 미충족; MACD=2.48372, signal9=2.49952; 직전 완료 봉 목표를 다음 봉 시가에 모의 적용 |
| v2 | rsi_14_recovery | 9919.07 | -80.93 | sell / filled / 직전 RSI14 < 30, 현재 RSI14 >= 30 (한 봉 목표); 조건 미충족; RSI14=40.3665, previous_RSI14=36.2025; 직전 완료 봉 목표를 다음 봉 시가에 모의 적용 |
| v2 | bollinger_20_reentry | 9770.69 | -229.31 | sell / filled / 직전 종가 < 직전 하단밴드, 현재 하단밴드 <= 종가 <= SMA20 (한 봉 목표); 조건 미충족; close=263.43, lower20=262.644, SMA20=266.981, previous_lower20=263.145; 직전 완료 봉 목표를 다음 봉 시가에 모의 적용 |
| v2 | donchian_20 | 9764.13 | -235.87 | sell / filled / 종가 > 현재 봉을 제외한 직전 20봉 최고가; 조건 미충족; close=268.59, prior_high20=269.55; 직전 완료 봉 목표를 다음 봉 시가에 모의 적용 |
| v2 | atr_14_breakout | 9619.01 | -380.99 | sell / filled / 종가 > 직전 종가 + 직전 ATR14 그리고 종가 > EMA26; 조건 미충족; close=269.05, threshold=269.858, prior_ATR14=0.907979, EMA26=264.623; 직전 완료 봉 목표를 다음 봉 시가에 모의 적용 |
| v2 | session_vwap | 9895.79 | -104.21 | buy / partial / 종가 > 뉴욕 거래일별 누적 전형가격 VWAP; 조건 충족; close=263.62, session_VWAP=263.396, session_volume=3.37048e+06; 직전 완료 봉 목표를 다음 봉 시가에 모의 적용 |
| v2 | obv_20 | 9769.81 | -230.19 | sell / filled / OBV > OBV의 SMA20 그리고 종가 > EMA26; 조건 미충족; OBV=2.01573e+07, OBV_SMA20=2.06236e+07, close=267.68, EMA26=266.081; 직전 완료 봉 목표를 다음 봉 시가에 모의 적용 |
| v2 | stochastic_14_3_recovery | 9393.40 | -606.60 | sell / filled / 직전 %K14 < 20에서 %K14가 %D3 상향 돌파 (한 봉 목표); 조건 미충족; K14=13.4247, D3=7.95839, previous_K14=6.19489, previous_D3=6.11994; 직전 완료 봉 목표를 다음 봉 시가에 모의 적용 |
| v2 | mfi_14_recovery | 9925.53 | -74.47 | sell / filled / 직전 MFI14 < 20, 현재 MFI14 >= 20 (한 봉 목표); 조건 미충족; MFI14=35.8262, previous_MFI14=31.0222; 직전 완료 봉 목표를 다음 봉 시가에 모의 적용 |
| v2 | adx_14_trend | 9662.33 | -337.67 | sell / filled / Wilder ADX14 >= 25 그리고 +DI14 > -DI14; 조건 미충족; ADX14=53.7666, plus_DI14=23.1641, minus_DI14=36.2315; 직전 완료 봉 목표를 다음 봉 시가에 모의 적용 |
| v2 | aroon_25_trend | 9968.63 | -31.37 | sell / filled / Aroon25 Up > 70 그리고 Down < 30 (동률이면 최신 극값); 조건 미충족; Aroon_up=76, Aroon_down=100; 직전 완료 봉 목표를 다음 봉 시가에 모의 적용 |
| v2 | cci_20_momentum | 10103.12 | 103.12 | buy / partial / CCI20 > 100 (전형가격·평균절대편차); 조건 충족; CCI20=105.231; 직전 완료 봉 목표를 다음 봉 시가에 모의 적용 |
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
| cash | 0.00% | 0.00% | 3.49% | 0.00% | 0.00% |
| buy_hold | 3.92% | 3.49% | 3.49% | 3.49% | 100.00% |
| trend_8_26 | 5.22% | 2.61% | 3.49% | 1.94% | 55.87% |
| momentum_26 | -0.46% | -4.56% | 3.49% | 1.86% | 53.52% |
| breakout_8 | 2.42% | -18.02% | 3.49% | 0.89% | 25.59% |
| reversion_12 | -4.63% | -11.57% | 3.49% | 0.76% | 21.93% |
| volume_26 | 3.01% | -2.88% | 3.49% | 0.17% | 4.96% |
| trend_8_26 AND momentum_26 | 1.18% | -1.75% | 3.49% | 1.65% | 47.52% |
| trend_8_26 + momentum_26 | 2.35% | -0.83% | 3.49% | 1.90% | 54.70% |
| trend_8_26 AND breakout_8 | 3.61% | -10.93% | 3.49% | 0.64% | 18.54% |
| trend_8_26 + breakout_8 | 3.85% | -8.06% | 3.49% | 1.41% | 40.74% |
| trend_8_26 AND reversion_12 | 0.52% | -3.21% | 3.49% | 0.23% | 6.53% |
| trend_8_26 + reversion_12 | 0.22% | -4.53% | 3.49% | 1.35% | 38.91% |
| trend_8_26 AND volume_26 | 3.25% | 0.26% | 3.49% | 0.07% | 2.09% |
| trend_8_26 + volume_26 | 4.15% | 0.05% | 3.49% | 1.05% | 30.42% |
| momentum_26 AND breakout_8 | 2.60% | -10.68% | 3.49% | 0.58% | 16.71% |
| momentum_26 + breakout_8 | 1.00% | -11.33% | 3.49% | 1.37% | 39.56% |
| momentum_26 AND reversion_12 | -1.40% | -5.46% | 3.49% | 0.25% | 7.31% |
| momentum_26 + reversion_12 | -2.54% | -7.54% | 3.49% | 1.31% | 37.73% |
| momentum_26 AND volume_26 | 0.14% | -0.70% | 3.49% | 0.02% | 0.52% |
| momentum_26 + volume_26 | 1.30% | -2.48% | 3.49% | 1.01% | 29.25% |
| breakout_8 AND reversion_12 | 0.00% | 0.00% | 3.49% | 0.00% | 0.00% |
| breakout_8 + reversion_12 | -1.14% | -14.50% | 3.49% | 0.82% | 23.77% |
| breakout_8 AND volume_26 | 1.33% | 0.06% | 3.49% | 0.04% | 1.04% |
| breakout_8 + volume_26 | 2.72% | -9.83% | 3.49% | 0.53% | 15.28% |
| reversion_12 AND volume_26 | -0.88% | -2.53% | 3.49% | 0.05% | 1.57% |
| reversion_12 + volume_26 | -0.87% | -6.93% | 3.49% | 0.46% | 13.45% |
| ema_12_26 | -0.07% | -2.97% | 3.49% | 1.91% | 55.09% |
| macd_12_26_9 | 9.10% | 5.49% | 3.49% | 1.20% | 34.73% |
| rsi_14_recovery | 0.09% | -2.40% | 3.49% | 0.05% | 1.57% |
| bollinger_20_reentry | -1.07% | -4.74% | 3.49% | 0.08% | 2.35% |
| donchian_20 | 2.07% | -7.72% | 3.49% | 0.34% | 9.92% |
| atr_14_breakout | 1.15% | -6.61% | 3.49% | 0.21% | 6.01% |
| session_vwap | 7.10% | -1.11% | 3.49% | 1.99% | 57.44% |
| obv_20 | -2.58% | -12.66% | 3.49% | 1.48% | 42.56% |
| stochastic_14_3_recovery | -0.56% | -10.09% | 3.49% | 0.22% | 6.27% |
| mfi_14_recovery | 0.80% | -1.30% | 3.49% | 0.05% | 1.31% |
| adx_14_trend | -3.32% | -8.45% | 3.49% | 1.48% | 42.82% |
| aroon_25_trend | 4.48% | 0.18% | 3.49% | 1.29% | 37.34% |
| cci_20_momentum | 4.65% | -2.57% | 3.49% | 0.87% | 25.07% |
| williams_14_recovery | -0.58% | -5.46% | 3.49% | 0.11% | 3.13% |
| cmf_20_accumulation | 6.29% | 1.49% | 3.49% | 1.46% | 42.04% |
| chaikin_3_10 | 0.06% | -5.26% | 3.49% | 1.58% | 45.43% |
| roc_10_momentum | -0.56% | -8.19% | 3.49% | 0.78% | 22.45% |
| trix_15_trend | -1.21% | -4.08% | 3.49% | 1.46% | 42.04% |
| keltner_20_breakout | 1.76% | -2.43% | 3.49% | 0.63% | 18.28% |
| opening_range_30m | 0.92% | -3.23% | 3.49% | 1.10% | 31.85% |

동일 구간·초기 자금, 종료 시 청산 비용 포함. 노출 맞춤은 사후 설명용이며 v2 실제 계좌 성과가 아닙니다.
[낙폭 분해·비용 영향·전체 구간](JNJ/comparison.json)

[v1 전체 기록](JNJ/accounts.json) · [v2 전체 기록](JNJ/accounts-v2.json)

## CAT 계좌

| 모델 | 전략 | 평가액 USD | 손익 USD | 최근 매매·이유 |
|---|---|---:|---:|---|
| v1 | cash | 10000.00 | 0.00 | 대기 /  / 새 신호 대기 |
| v1 | buy_hold | 9358.76 | -641.24 | buy /  / buy_hold: prior completed bar target 100%; next bar open simulation |
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
| v1 | session_vwap | 8763.01 | -1236.99 | buy /  / 종가 > 뉴욕 거래일별 누적 전형가격 VWAP; 조건 충족; close=688.5, session_VWAP=687.404, session_volume=2.51127e+06 |
| v1 | obv_20 | 9541.23 | -458.77 | sell /  / OBV > OBV의 SMA20 그리고 종가 > EMA26; 조건 미충족; OBV=-5.63582e+06, OBV_SMA20=-5.55612e+06, close=711.18, EMA26=734.673 |
| v1 | stochastic_14_3_recovery | 9643.06 | -356.94 | sell /  / 직전 %K14 < 20에서 %K14가 %D3 상향 돌파 (한 봉 목표); 조건 미충족; K14=24.7265, D3=31.6073, previous_K14=51.7944, previous_D3=39.927 |
| v1 | mfi_14_recovery | 9992.21 | -7.79 | sell /  / 직전 MFI14 < 20, 현재 MFI14 >= 20 (한 봉 목표); 조건 미충족; MFI14=41.7007, previous_MFI14=39.2559 |
| v1 | adx_14_trend | 9614.13 | -385.87 | sell /  / Wilder ADX14 >= 25 그리고 +DI14 > -DI14; 조건 미충족; ADX14=37.6898, plus_DI14=16.8278, minus_DI14=52.0976 |
| v1 | aroon_25_trend | 9979.61 | -20.39 | sell /  / Aroon25 Up > 70 그리고 Down < 30 (동률이면 최신 극값); 조건 미충족; Aroon_up=68, Aroon_down=20 |
| v1 | cci_20_momentum | 9862.85 | -137.15 | sell /  / CCI20 > 100 (전형가격·평균절대편차); 조건 미충족; CCI20=99.2123 |
| v1 | williams_14_recovery | 9678.05 | -321.95 | sell /  / 직전 Williams %R14 < -80, 현재 >= -80 (한 봉 목표); 조건 미충족; Williams_R14=-75.2735, previous_R14=-48.2056 |
| v1 | cmf_20_accumulation | 9458.11 | -541.89 | sell /  / Chaikin Money Flow20 > 0.1; 조건 미충족; CMF20=0.0105743, volume20=1.36134e+06 |
| v1 | chaikin_3_10 | 9240.53 | -759.47 | sell /  / ADL의 EMA3 - EMA10 > 0 그리고 종가 > EMA26; 조건 미충족; Chaikin3_10=-27551.7, ADL=-5.27692e+06, close=711.18, EMA26=734.673 |
| v1 | roc_10_momentum | 9896.73 | -103.27 | sell /  / 10봉 ROC > 1% 그리고 종가 > EMA26; 조건 미충족; ROC10_percent=0.883016, close=741.47, EMA26=734.681 |
| v1 | trix_15_trend | 9340.52 | -659.48 | sell /  / 15봉 삼중 EMA의 1봉 변화율 TRIX > 0 그리고 종가 > EMA26; 조건 미충족; TRIX15_percent=0.0460682, close=711.18, EMA26=734.673 |
| v1 | keltner_20_breakout | 10000.00 | 0.00 | 대기 /  / 새 신호 대기 |
| v1 | opening_range_30m | 10162.22 | 162.22 | sell /  / 뉴욕 09:30·09:45 두 완료 봉 최고가를 10:00 이후 종가가 돌파; 자료 부족·변동폭 또는 거래량 없음: 대기; close=733.16 |
| v2 | cash | 10000.00 | 0.00 | 대기 /  / 새 신호 대기 |
| v2 | buy_hold | 8607.01 | -1392.99 | 중단: 손실 한도 / buy / partial / 직전 완료 봉 목표 비중 100%; 다음 봉 시가 가정 |
| v2 | trend_8_26 | 9209.73 | -790.27 | 중단: 손실 한도 / buy / partial / 직전 완료 봉 목표 비중 100%; 다음 봉 시가 가정 |
| v2 | momentum_26 | 9015.89 | -984.11 | 중단: 손실 한도 / buy / partial / 직전 완료 봉 목표 비중 100%; 다음 봉 시가 가정 |
| v2 | breakout_8 | 9125.42 | -874.58 | sell / filled / 직전 완료 봉 목표 비중 0%; 다음 봉 시가 가정 |
| v2 | reversion_12 | 8486.81 | -1513.19 | 중단: 손실 한도 / buy / partial / 직전 완료 봉 목표 비중 100%; 다음 봉 시가 가정 |
| v2 | volume_26 | 8729.53 | -1270.47 | 중단: 손실 한도 / buy / partial / 직전 완료 봉 목표 비중 100%; 다음 봉 시가 가정 |
| v2 | trend_8_26 AND momentum_26 | 9223.32 | -776.68 | 중단: 손실 한도 / buy / partial / 직전 완료 봉 목표 비중 100%; 다음 봉 시가 가정 |
| v2 | trend_8_26 + momentum_26 | 9113.28 | -886.72 | 중단: 손실 한도 / buy / partial / 직전 완료 봉 목표 비중 100%; 다음 봉 시가 가정 |
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
| v2 | reversion_12 AND volume_26 | 8669.14 | -1330.86 | 중단: 손실 한도 / buy / partial / 직전 완료 봉 목표 비중 100%; 다음 봉 시가 가정 |
| v2 | reversion_12 + volume_26 | 9103.02 | -896.98 | 중단: 손실 한도 / sell / filled / 직전 완료 봉 목표 비중 50%; 다음 봉 시가 가정 |
| v2 | ema_12_26 | 9309.56 | -690.44 | 중단: 손실 한도 / buy / partial / EMA12 > EMA26; 조건 충족; EMA12=726.261, EMA26=726.172; 직전 완료 봉 목표를 다음 봉 시가에 모의 적용 |
| v2 | macd_12_26_9 | 9984.52 | -15.48 | sell / filled / MACD > 신호선 그리고 MACD > 0; 조건 미충족; MACD=2.92675, signal9=3.02629; 직전 완료 봉 목표를 다음 봉 시가에 모의 적용 |
| v2 | rsi_14_recovery | 9858.74 | -141.26 | sell / filled / 직전 RSI14 < 30, 현재 RSI14 >= 30 (한 봉 목표); 조건 미충족; RSI14=34.2237, previous_RSI14=36.7431; 직전 완료 봉 목표를 다음 봉 시가에 모의 적용 |
| v2 | bollinger_20_reentry | 9601.72 | -398.28 | sell / filled / 직전 종가 < 직전 하단밴드, 현재 하단밴드 <= 종가 <= SMA20 (한 봉 목표); 조건 미충족; close=688.16, lower20=683.118, SMA20=697.519, previous_lower20=684.291; 직전 완료 봉 목표를 다음 봉 시가에 모의 적용 |
| v2 | donchian_20 | 9939.30 | -60.70 | sell / filled / 종가 > 현재 봉을 제외한 직전 20봉 최고가; 조건 미충족; close=735.35, prior_high20=745; 직전 완료 봉 목표를 다음 봉 시가에 모의 적용 |
| v2 | atr_14_breakout | 9758.55 | -241.45 | sell / filled / 종가 > 직전 종가 + 직전 ATR14 그리고 종가 > EMA26; 조건 미충족; close=735.35, threshold=737.263, prior_ATR14=4.10289, EMA26=727.331; 직전 완료 봉 목표를 다음 봉 시가에 모의 적용 |
| v2 | session_vwap | 8964.72 | -1035.28 | 중단: 손실 한도 / buy / partial / 종가 > 뉴욕 거래일별 누적 전형가격 VWAP; 조건 충족; close=734.98, session_VWAP=734.093, session_volume=764353; 직전 완료 봉 목표를 다음 봉 시가에 모의 적용 |
| v2 | obv_20 | 9247.49 | -752.51 | 중단: 손실 한도 / buy / partial / OBV > OBV의 SMA20 그리고 종가 > EMA26; 조건 충족; OBV=-5.0567e+06, OBV_SMA20=-6.30537e+06, close=733.16, EMA26=726.69; 직전 완료 봉 목표를 다음 봉 시가에 모의 적용 |
| v2 | stochastic_14_3_recovery | 9619.94 | -380.06 | sell / filled / 직전 %K14 < 20에서 %K14가 %D3 상향 돌파 (한 봉 목표); 조건 미충족; K14=24.7265, D3=31.6073, previous_K14=51.7944, previous_D3=39.927; 직전 완료 봉 목표를 다음 봉 시가에 모의 적용 |
| v2 | mfi_14_recovery | 9986.21 | -13.79 | sell / filled / 직전 MFI14 < 20, 현재 MFI14 >= 20 (한 봉 목표); 조건 미충족; MFI14=41.7007, previous_MFI14=39.2559; 직전 완료 봉 목표를 다음 봉 시가에 모의 적용 |
| v2 | adx_14_trend | 9327.47 | -672.53 | 중단: 손실 한도 / buy / partial / Wilder ADX14 >= 25 그리고 +DI14 > -DI14; 조건 충족; ADX14=25.4031, plus_DI14=35.2628, minus_DI14=13.9603; 직전 완료 봉 목표를 다음 봉 시가에 모의 적용 |
| v2 | aroon_25_trend | 9973.62 | -26.38 | sell / filled / Aroon25 Up > 70 그리고 Down < 30 (동률이면 최신 극값); 조건 미충족; Aroon_up=68, Aroon_down=20; 직전 완료 봉 목표를 다음 봉 시가에 모의 적용 |
| v2 | cci_20_momentum | 9854.97 | -145.03 | sell / filled / CCI20 > 100 (전형가격·평균절대편차); 조건 미충족; CCI20=99.2123; 직전 완료 봉 목표를 다음 봉 시가에 모의 적용 |
| v2 | williams_14_recovery | 9660.65 | -339.35 | sell / filled / 직전 Williams %R14 < -80, 현재 >= -80 (한 봉 목표); 조건 미충족; Williams_R14=-75.2735, previous_R14=-48.2056; 직전 완료 봉 목표를 다음 봉 시가에 모의 적용 |
| v2 | cmf_20_accumulation | 9168.76 | -831.24 | 중단: 손실 한도 / buy / partial / Chaikin Money Flow20 > 0.1; 조건 충족; CMF20=0.145111, volume20=965726; 직전 완료 봉 목표를 다음 봉 시가에 모의 적용 |
| v2 | chaikin_3_10 | 9064.44 | -935.56 | 중단: 손실 한도 / buy / partial / ADL의 EMA3 - EMA10 > 0 그리고 종가 > EMA26; 조건 충족; Chaikin3_10=293683, ADL=-4.91156e+06, close=739.58, EMA26=736.187; 직전 완료 봉 목표를 다음 봉 시가에 모의 적용 |
| v2 | roc_10_momentum | 9888.81 | -111.19 | sell / filled / 10봉 ROC > 1% 그리고 종가 > EMA26; 조건 미충족; ROC10_percent=0.883016, close=741.47, EMA26=734.681; 직전 완료 봉 목표를 다음 봉 시가에 모의 적용 |
| v2 | trix_15_trend | 9073.58 | -926.42 | 중단: 손실 한도 / buy / partial / 15봉 삼중 EMA의 1봉 변화율 TRIX > 0 그리고 종가 > EMA26; 조건 충족; TRIX15_percent=0.0196284, close=739.58, EMA26=736.187; 직전 완료 봉 목표를 다음 봉 시가에 모의 적용 |
| v2 | keltner_20_breakout | 10000.00 | 0.00 | 대기 /  / 새 신호 대기 |
| v2 | opening_range_30m | 10158.15 | 158.15 | sell / filled / 뉴욕 09:30·09:45 두 완료 봉 최고가를 10:00 이후 종가가 돌파; 자료 부족·변동폭 또는 거래량 없음: 대기; close=733.16; 직전 완료 봉 목표를 다음 봉 시가에 모의 적용 |

### 같은 기간의 비용·노출 비교 (사후 연구)

| 전략 | 비용 전 | 비용 후 | 100% 보유 | 같은 평균 노출 보유 | 평균 노출 |
|---|---:|---:|---:|---:|---:|
| cash | 0.00% | 0.00% | -18.96% | -0.00% | 0.00% |
| buy_hold | -18.62% | -18.96% | -18.96% | -18.96% | 100.00% |
| trend_8_26 | -2.45% | -5.67% | -18.96% | -7.74% | 38.38% |
| momentum_26 | -5.96% | -9.83% | -18.96% | -7.34% | 36.29% |
| breakout_8 | -1.90% | -14.23% | -18.96% | -3.18% | 15.40% |
| reversion_12 | -3.77% | -16.57% | -18.96% | -5.64% | 27.68% |
| volume_26 | -3.30% | -11.47% | -18.96% | -1.79% | 8.62% |
| trend_8_26 AND momentum_26 | -1.86% | -4.71% | -18.96% | -6.36% | 31.33% |
| trend_8_26 + momentum_26 | -4.20% | -7.76% | -18.96% | -7.54% | 37.34% |
| trend_8_26 AND breakout_8 | 0.84% | -5.31% | -18.96% | -1.68% | 8.09% |
| trend_8_26 + breakout_8 | -2.14% | -9.84% | -18.96% | -5.49% | 26.90% |
| trend_8_26 AND reversion_12 | 2.91% | -2.56% | -18.96% | -1.03% | 4.96% |
| trend_8_26 + reversion_12 | -3.04% | -10.32% | -18.96% | -6.70% | 33.03% |
| trend_8_26 AND volume_26 | 2.90% | 1.18% | -18.96% | -0.33% | 1.57% |
| trend_8_26 + volume_26 | -2.83% | -8.21% | -18.96% | -4.81% | 23.50% |
| momentum_26 AND breakout_8 | 0.09% | -6.80% | -18.96% | -1.74% | 8.36% |
| momentum_26 + breakout_8 | -3.92% | -12.04% | -18.96% | -5.28% | 25.85% |
| momentum_26 AND reversion_12 | -0.98% | -6.25% | -18.96% | -1.20% | 5.74% |
| momentum_26 + reversion_12 | -4.82% | -13.06% | -18.96% | -6.49% | 31.99% |
| momentum_26 AND volume_26 | 2.69% | 0.55% | -18.96% | -0.33% | 1.57% |
| momentum_26 + volume_26 | -4.60% | -10.25% | -18.96% | -4.60% | 22.46% |
| breakout_8 AND reversion_12 | 0.00% | 0.00% | -18.96% | -0.00% | 0.00% |
| breakout_8 + reversion_12 | -2.78% | -14.50% | -18.96% | -4.42% | 21.55% |
| breakout_8 AND volume_26 | 0.55% | -1.13% | -18.96% | -0.22% | 1.04% |
| breakout_8 + volume_26 | -2.57% | -12.30% | -18.96% | -2.49% | 12.02% |
| reversion_12 AND volume_26 | -2.64% | -7.81% | -18.96% | -1.14% | 5.48% |
| reversion_12 + volume_26 | -3.50% | -13.68% | -18.96% | -3.74% | 18.15% |
| ema_12_26 | -5.03% | -6.61% | -18.96% | -6.83% | 33.68% |
| macd_12_26_9 | 0.73% | -1.36% | -18.96% | -4.34% | 21.15% |
| rsi_14_recovery | -0.08% | -6.58% | -18.96% | -0.87% | 4.18% |
| bollinger_20_reentry | -1.57% | -6.80% | -18.96% | -0.71% | 3.39% |
| donchian_20 | 1.25% | -1.69% | -18.96% | -0.65% | 3.13% |
| atr_14_breakout | 1.29% | -2.88% | -18.96% | -0.60% | 2.87% |
| session_vwap | -5.78% | -17.28% | -18.96% | -9.15% | 45.69% |
| obv_20 | -3.87% | -11.62% | -18.96% | -3.97% | 19.32% |
| stochastic_14_3_recovery | -2.02% | -13.25% | -18.96% | -1.58% | 7.57% |
| mfi_14_recovery | 1.04% | -1.47% | -18.96% | -0.33% | 1.57% |
| adx_14_trend | -3.70% | -5.70% | -18.96% | -1.25% | 6.01% |
| aroon_25_trend | 1.10% | -1.83% | -18.96% | -1.68% | 8.09% |
| cci_20_momentum | -1.74% | -6.17% | -18.96% | -2.65% | 12.79% |
| williams_14_recovery | -2.07% | -10.34% | -18.96% | -1.14% | 5.48% |
| cmf_20_accumulation | -4.44% | -10.28% | -18.96% | -3.29% | 15.93% |
| chaikin_3_10 | -6.00% | -13.57% | -18.96% | -5.23% | 25.59% |
| roc_10_momentum | -0.09% | -5.40% | -18.96% | -1.95% | 9.40% |
| trix_15_trend | -3.86% | -7.43% | -18.96% | -5.38% | 26.37% |
| keltner_20_breakout | 0.38% | -0.46% | -18.96% | -0.27% | 1.31% |
| opening_range_30m | 3.63% | -0.21% | -18.96% | -4.39% | 21.41% |

동일 구간·초기 자금, 종료 시 청산 비용 포함. 노출 맞춤은 사후 설명용이며 v2 실제 계좌 성과가 아닙니다.
[낙폭 분해·비용 영향·전체 구간](CAT/comparison.json)

[v1 전체 기록](CAT/accounts.json) · [v2 전체 기록](CAT/accounts-v2.json)

## WMT 계좌

| 모델 | 전략 | 평가액 USD | 손익 USD | 최근 매매·이유 |
|---|---|---:|---:|---|
| v1 | cash | 10000.00 | 0.00 | 대기 /  / 새 신호 대기 |
| v1 | buy_hold | 10086.89 | 86.89 | buy /  / buy_hold: prior completed bar target 100%; next bar open simulation |
| v1 | trend_8_26 | 9779.58 | -220.42 | sell /  / trend_8_26: prior completed bar target 0%; next bar open simulation |
| v1 | momentum_26 | 9832.09 | -167.91 | sell /  / momentum_26: prior completed bar target 0%; next bar open simulation |
| v1 | breakout_8 | 9342.19 | -657.81 | sell /  / breakout_8: prior completed bar target 0%; next bar open simulation |
| v1 | reversion_12 | 9417.37 | -582.63 | sell /  / reversion_12: prior completed bar target 0%; next bar open simulation |
| v1 | volume_26 | 9775.35 | -224.65 | sell /  / volume_26: prior completed bar target 0%; next bar open simulation |
| v1 | trend_8_26 AND momentum_26 | 9861.19 | -138.81 | sell /  / trend_8_26 AND momentum_26: prior completed bar target 0%; next bar open simulation |
| v1 | trend_8_26 + momentum_26 | 9805.82 | -194.18 | sell /  / trend_8_26 + momentum_26: prior completed bar target 0%; next bar open simulation |
| v1 | trend_8_26 AND breakout_8 | 9602.19 | -397.81 | sell /  / trend_8_26 AND breakout_8: prior completed bar target 0%; next bar open simulation |
| v1 | trend_8_26 + breakout_8 | 9577.78 | -422.22 | sell /  / trend_8_26 + breakout_8: prior completed bar target 0%; next bar open simulation |
| v1 | trend_8_26 AND reversion_12 | 9683.74 | -316.26 | sell /  / trend_8_26 AND reversion_12: prior completed bar target 0%; next bar open simulation |
| v1 | trend_8_26 + reversion_12 | 9635.30 | -364.70 | sell /  / trend_8_26 + reversion_12: prior completed bar target 0%; next bar open simulation |
| v1 | trend_8_26 AND volume_26 | 9837.96 | -162.04 | sell /  / trend_8_26 AND volume_26: prior completed bar target 0%; next bar open simulation |
| v1 | trend_8_26 + volume_26 | 9777.89 | -222.11 | sell /  / trend_8_26 + volume_26: prior completed bar target 0%; next bar open simulation |
| v1 | momentum_26 AND breakout_8 | 9514.44 | -485.56 | sell /  / momentum_26 AND breakout_8: prior completed bar target 0%; next bar open simulation |
| v1 | momentum_26 + breakout_8 | 9642.15 | -357.85 | sell /  / momentum_26 + breakout_8: prior completed bar target 0%; next bar open simulation |
| v1 | momentum_26 AND reversion_12 | 9877.29 | -122.71 | sell /  / momentum_26 AND reversion_12: prior completed bar target 0%; next bar open simulation |
| v1 | momentum_26 + reversion_12 | 9719.09 | -280.91 | sell /  / momentum_26 + reversion_12: prior completed bar target 0%; next bar open simulation |
| v1 | momentum_26 AND volume_26 | 9853.50 | -146.50 | sell /  / momentum_26 AND volume_26: prior completed bar target 0%; next bar open simulation |
| v1 | momentum_26 + volume_26 | 9843.34 | -156.66 | sell /  / momentum_26 + volume_26: prior completed bar target 0%; next bar open simulation |
| v1 | breakout_8 AND reversion_12 | 10000.00 | 0.00 | 대기 /  / 새 신호 대기 |
| v1 | breakout_8 + reversion_12 | 9417.06 | -582.94 | sell /  / breakout_8 + reversion_12: prior completed bar target 0%; next bar open simulation |
| v1 | breakout_8 AND volume_26 | 9797.95 | -202.05 | sell /  / breakout_8 AND volume_26: prior completed bar target 0%; next bar open simulation |
| v1 | breakout_8 + volume_26 | 9556.59 | -443.41 | sell /  / breakout_8 + volume_26: prior completed bar target 0%; next bar open simulation |
| v1 | reversion_12 AND volume_26 | 9911.53 | -88.47 | sell /  / reversion_12 AND volume_26: prior completed bar target 0%; next bar open simulation |
| v1 | reversion_12 + volume_26 | 9652.50 | -347.50 | sell /  / reversion_12 + volume_26: prior completed bar target 0%; next bar open simulation |
| v1 | ema_12_26 | 9971.99 | -28.01 | sell /  / EMA12 > EMA26; 조건 미충족; EMA12=120.013, EMA26=120.022 |
| v1 | macd_12_26_9 | 10121.08 | 121.08 | sell /  / MACD > 신호선 그리고 MACD > 0; 조건 미충족; MACD=0.563738, signal9=0.568978 |
| v1 | rsi_14_recovery | 9973.19 | -26.81 | sell /  / 직전 RSI14 < 30, 현재 RSI14 >= 30 (한 봉 목표); 조건 미충족; RSI14=46.7246, previous_RSI14=43.1348 |
| v1 | bollinger_20_reentry | 9940.27 | -59.73 | sell /  / 직전 종가 < 직전 하단밴드, 현재 하단밴드 <= 종가 <= SMA20 (한 봉 목표); 조건 미충족; close=120.035, lower20=119.686, SMA20=120.446, previous_lower20=119.732 |
| v1 | donchian_20 | 9643.84 | -356.16 | sell /  / 종가 > 현재 봉을 제외한 직전 20봉 최고가; 조건 미충족; close=121.08, prior_high20=121.18 |
| v1 | atr_14_breakout | 9811.78 | -188.22 | sell /  / 종가 > 직전 종가 + 직전 ATR14 그리고 종가 > EMA26; 조건 미충족; close=120.03, threshold=120.128, prior_ATR14=0.443028, EMA26=118.335 |
| v1 | session_vwap | 9681.70 | -318.30 | sell /  / 종가 > 뉴욕 거래일별 누적 전형가격 VWAP; 조건 미충족; close=121.08, session_VWAP=121.52, session_volume=1.65503e+06 |
| v1 | obv_20 | 9894.31 | -105.69 | sell /  / OBV > OBV의 SMA20 그리고 종가 > EMA26; 조건 미충족; OBV=1.93315e+07, OBV_SMA20=1.9255e+07, close=119.98, EMA26=120.094 |
| v1 | stochastic_14_3_recovery | 9407.71 | -592.29 | buy /  / 직전 %K14 < 20에서 %K14가 %D3 상향 돌파 (한 봉 목표); 조건 충족; K14=9.64918, D3=8.72575, previous_K14=4.13186, previous_D3=13.7737 |
| v1 | mfi_14_recovery | 9969.08 | -30.92 | sell /  / 직전 MFI14 < 20, 현재 MFI14 >= 20 (한 봉 목표); 조건 미충족; MFI14=57.3162, previous_MFI14=36.5877 |
| v1 | adx_14_trend | 10064.02 | 64.02 | sell /  / Wilder ADX14 >= 25 그리고 +DI14 > -DI14; 조건 미충족; ADX14=30.1427, plus_DI14=25.9007, minus_DI14=26.0063 |
| v1 | aroon_25_trend | 9893.25 | -106.75 | sell /  / Aroon25 Up > 70 그리고 Down < 30 (동률이면 최신 극값); 조건 미충족; Aroon_up=80, Aroon_down=96 |
| v1 | cci_20_momentum | 9664.17 | -335.83 | sell /  / CCI20 > 100 (전형가격·평균절대편차); 조건 미충족; CCI20=-31.8509 |
| v1 | williams_14_recovery | 9645.18 | -354.82 | sell /  / 직전 Williams %R14 < -80, 현재 >= -80 (한 봉 목표); 조건 미충족; Williams_R14=-87.6038, previous_R14=-75.207 |
| v1 | cmf_20_accumulation | 9737.44 | -262.56 | sell /  / Chaikin Money Flow20 > 0.1; 조건 미충족; CMF20=0.0930543, volume20=1.6661e+07 |
| v1 | chaikin_3_10 | 9709.84 | -290.16 | sell /  / ADL의 EMA3 - EMA10 > 0 그리고 종가 > EMA26; 조건 미충족; Chaikin3_10=76755.7, ADL=1.33628e+07, close=120.04, EMA26=120.151 |
| v1 | roc_10_momentum | 10091.95 | 91.95 | sell /  / 10봉 ROC > 1% 그리고 종가 > EMA26; 조건 미충족; ROC10_percent=0.710203, close=120.535, EMA26=119.283 |
| v1 | trix_15_trend | 9640.97 | -359.03 | sell /  / 15봉 삼중 EMA의 1봉 변화율 TRIX > 0 그리고 종가 > EMA26; 조건 미충족; TRIX15_percent=0.0327766, close=119.98, EMA26=120.094 |
| v1 | keltner_20_breakout | 9879.35 | -120.65 | sell /  / 종가 > EMA20 + 2 x Wilder ATR14; 조건 미충족; close=121.08, upper_Keltner=121.15, EMA20=120.322, ATR14=0.414113 |
| v1 | opening_range_30m | 9860.78 | -139.22 | sell /  / 뉴욕 09:30·09:45 두 완료 봉 최고가를 10:00 이후 종가가 돌파; 자료 부족·변동폭 또는 거래량 없음: 대기; close=121.08 |
| v2 | cash | 10000.00 | 0.00 | 대기 /  / 새 신호 대기 |
| v2 | buy_hold | 10686.96 | 686.96 | buy / partial / 직전 완료 봉 목표 비중 100%; 다음 봉 시가 가정 |
| v2 | trend_8_26 | 10170.98 | 170.98 | sell / filled / 직전 완료 봉 목표 비중 0%; 다음 봉 시가 가정 |
| v2 | momentum_26 | 10228.38 | 228.38 | sell / filled / 직전 완료 봉 목표 비중 0%; 다음 봉 시가 가정 |
| v2 | breakout_8 | 9296.17 | -703.83 | 중단: 손실 한도 / sell / filled / 직전 완료 봉 목표 비중 0%; 다음 봉 시가 가정 |
| v2 | reversion_12 | 9306.00 | -694.00 | sell / filled / 직전 완료 봉 목표 비중 0%; 다음 봉 시가 가정 |
| v2 | volume_26 | 9727.78 | -272.22 | sell / filled / 직전 완료 봉 목표 비중 0%; 다음 봉 시가 가정 |
| v2 | trend_8_26 AND momentum_26 | 10255.85 | 255.85 | sell / filled / 직전 완료 봉 목표 비중 0%; 다음 봉 시가 가정 |
| v2 | trend_8_26 + momentum_26 | 10199.60 | 199.60 | sell / filled / 직전 완료 봉 목표 비중 0%; 다음 봉 시가 가정 |
| v2 | trend_8_26 AND breakout_8 | 9667.87 | -332.13 | sell / filled / 직전 완료 봉 목표 비중 0%; 다음 봉 시가 가정 |
| v2 | trend_8_26 + breakout_8 | 9736.05 | -263.95 | sell / filled / 직전 완료 봉 목표 비중 0%; 다음 봉 시가 가정 |
| v2 | trend_8_26 AND reversion_12 | 9487.14 | -512.86 | sell / filled / 직전 완료 봉 목표 비중 0%; 다음 봉 시가 가정 |
| v2 | trend_8_26 + reversion_12 | 9771.24 | -228.76 | sell / filled / 직전 완료 봉 목표 비중 0%; 다음 봉 시가 가정 |
| v2 | trend_8_26 AND volume_26 | 9784.10 | -215.90 | sell / filled / 직전 완료 봉 목표 비중 0%; 다음 봉 시가 가정 |
| v2 | trend_8_26 + volume_26 | 9948.73 | -51.27 | sell / filled / 직전 완료 봉 목표 비중 0%; 다음 봉 시가 가정 |
| v2 | momentum_26 AND breakout_8 | 9475.14 | -524.86 | 중단: 손실 한도 / sell / filled / 직전 완료 봉 목표 비중 0%; 다음 봉 시가 가정 |
| v2 | momentum_26 + breakout_8 | 9804.78 | -195.22 | sell / filled / 직전 완료 봉 목표 비중 0%; 다음 봉 시가 가정 |
| v2 | momentum_26 AND reversion_12 | 9700.42 | -299.58 | sell / filled / 직전 완료 봉 목표 비중 0%; 다음 봉 시가 가정 |
| v2 | momentum_26 + reversion_12 | 9902.07 | -97.93 | sell / filled / 직전 완료 봉 목표 비중 0%; 다음 봉 시가 가정 |
| v2 | momentum_26 AND volume_26 | 9760.78 | -239.22 | sell / filled / 직전 완료 봉 목표 비중 0%; 다음 봉 시가 가정 |
| v2 | momentum_26 + volume_26 | 10018.75 | 18.75 | sell / filled / 직전 완료 봉 목표 비중 0%; 다음 봉 시가 가정 |
| v2 | breakout_8 AND reversion_12 | 10000.00 | 0.00 | 대기 /  / 새 신호 대기 |
| v2 | breakout_8 + reversion_12 | 9352.23 | -647.77 | sell / filled / 직전 완료 봉 목표 비중 0%; 다음 봉 시가 가정 |
| v2 | breakout_8 AND volume_26 | 9741.39 | -258.61 | sell / filled / 직전 완료 봉 목표 비중 0%; 다음 봉 시가 가정 |
| v2 | breakout_8 + volume_26 | 9502.52 | -497.48 | sell / filled / 직전 완료 봉 목표 비중 0%; 다음 봉 시가 가정 |
| v2 | reversion_12 AND volume_26 | 9917.25 | -82.75 | sell / filled / 직전 완료 봉 목표 비중 0%; 다음 봉 시가 가정 |
| v2 | reversion_12 + volume_26 | 9574.62 | -425.38 | sell / filled / 직전 완료 봉 목표 비중 0%; 다음 봉 시가 가정 |
| v2 | ema_12_26 | 9966.01 | -33.99 | sell / filled / EMA12 > EMA26; 조건 미충족; EMA12=120.013, EMA26=120.022; 직전 완료 봉 목표를 다음 봉 시가에 모의 적용 |
| v2 | macd_12_26_9 | 10115.01 | 115.01 | sell / filled / MACD > 신호선 그리고 MACD > 0; 조건 미충족; MACD=0.563738, signal9=0.568978; 직전 완료 봉 목표를 다음 봉 시가에 모의 적용 |
| v2 | rsi_14_recovery | 9971.19 | -28.81 | sell / filled / 직전 RSI14 < 30, 현재 RSI14 >= 30 (한 봉 목표); 조건 미충족; RSI14=46.7246, previous_RSI14=43.1348; 직전 완료 봉 목표를 다음 봉 시가에 모의 적용 |
| v2 | bollinger_20_reentry | 9930.34 | -69.66 | sell / filled / 직전 종가 < 직전 하단밴드, 현재 하단밴드 <= 종가 <= SMA20 (한 봉 목표); 조건 미충족; close=120.035, lower20=119.686, SMA20=120.446, previous_lower20=119.732; 직전 완료 봉 목표를 다음 봉 시가에 모의 적용 |
| v2 | donchian_20 | 9630.34 | -369.66 | sell / filled / 종가 > 현재 봉을 제외한 직전 20봉 최고가; 조건 미충족; close=121.08, prior_high20=121.18; 직전 완료 봉 목표를 다음 봉 시가에 모의 적용 |
| v2 | atr_14_breakout | 9801.98 | -198.02 | sell / filled / 종가 > 직전 종가 + 직전 ATR14 그리고 종가 > EMA26; 조건 미충족; close=120.03, threshold=120.128, prior_ATR14=0.443028, EMA26=118.335; 직전 완료 봉 목표를 다음 봉 시가에 모의 적용 |
| v2 | session_vwap | 9660.42 | -339.58 | sell / filled / 종가 > 뉴욕 거래일별 누적 전형가격 VWAP; 조건 미충족; close=121.08, session_VWAP=121.52, session_volume=1.65503e+06; 직전 완료 봉 목표를 다음 봉 시가에 모의 적용 |
| v2 | obv_20 | 9880.47 | -119.53 | sell / filled / OBV > OBV의 SMA20 그리고 종가 > EMA26; 조건 미충족; OBV=1.93315e+07, OBV_SMA20=1.9255e+07, close=119.98, EMA26=120.094; 직전 완료 봉 목표를 다음 봉 시가에 모의 적용 |
| v2 | stochastic_14_3_recovery | 9787.51 | -212.49 | 중단: 손실 한도 / buy / partial / 직전 %K14 < 20에서 %K14가 %D3 상향 돌파 (한 봉 목표); 조건 충족; K14=25.6758, D3=22.4971, previous_K14=12.8379, previous_D3=25.8704; 직전 완료 봉 목표를 다음 봉 시가에 모의 적용 |
| v2 | mfi_14_recovery | 9961.11 | -38.89 | sell / filled / 직전 MFI14 < 20, 현재 MFI14 >= 20 (한 봉 목표); 조건 미충족; MFI14=57.3162, previous_MFI14=36.5877; 직전 완료 봉 목표를 다음 봉 시가에 모의 적용 |
| v2 | adx_14_trend | 10059.99 | 59.99 | sell / filled / Wilder ADX14 >= 25 그리고 +DI14 > -DI14; 조건 미충족; ADX14=30.1427, plus_DI14=25.9007, minus_DI14=26.0063; 직전 완료 봉 목표를 다음 봉 시가에 모의 적용 |
| v2 | aroon_25_trend | 9885.34 | -114.66 | sell / filled / Aroon25 Up > 70 그리고 Down < 30 (동률이면 최신 극값); 조건 미충족; Aroon_up=80, Aroon_down=96; 직전 완료 봉 목표를 다음 봉 시가에 모의 적용 |
| v2 | cci_20_momentum | 9650.65 | -349.35 | sell / filled / CCI20 > 100 (전형가격·평균절대편차); 조건 미충족; CCI20=-31.8509; 직전 완료 봉 목표를 다음 봉 시가에 모의 적용 |
| v2 | williams_14_recovery | 9627.83 | -372.17 | sell / filled / 직전 Williams %R14 < -80, 현재 >= -80 (한 봉 목표); 조건 미충족; Williams_R14=-87.6038, previous_R14=-75.207; 직전 완료 봉 목표를 다음 봉 시가에 모의 적용 |
| v2 | cmf_20_accumulation | 9723.82 | -276.18 | sell / filled / Chaikin Money Flow20 > 0.1; 조건 미충족; CMF20=0.0930543, volume20=1.6661e+07; 직전 완료 봉 목표를 다음 봉 시가에 모의 적용 |
| v2 | chaikin_3_10 | 9690.44 | -309.56 | sell / filled / ADL의 EMA3 - EMA10 > 0 그리고 종가 > EMA26; 조건 미충족; Chaikin3_10=76755.7, ADL=1.33628e+07, close=120.04, EMA26=120.151; 직전 완료 봉 목표를 다음 봉 시가에 모의 적용 |
| v2 | roc_10_momentum | 10089.93 | 89.93 | sell / filled / 10봉 ROC > 1% 그리고 종가 > EMA26; 조건 미충족; ROC10_percent=0.710203, close=120.535, EMA26=119.283; 직전 완료 봉 목표를 다음 봉 시가에 모의 적용 |
| v2 | trix_15_trend | 9625.56 | -374.44 | sell / filled / 15봉 삼중 EMA의 1봉 변화율 TRIX > 0 그리고 종가 > EMA26; 조건 미충족; TRIX15_percent=0.0327766, close=119.98, EMA26=120.094; 직전 완료 봉 목표를 다음 봉 시가에 모의 적용 |
| v2 | keltner_20_breakout | 9871.45 | -128.55 | sell / filled / 종가 > EMA20 + 2 x Wilder ATR14; 조건 미충족; close=121.08, upper_Keltner=121.15, EMA20=120.322, ATR14=0.414113; 직전 완료 봉 목표를 다음 봉 시가에 모의 적용 |
| v2 | opening_range_30m | 9850.92 | -149.08 | sell / filled / 뉴욕 09:30·09:45 두 완료 봉 최고가를 10:00 이후 종가가 돌파; 자료 부족·변동폭 또는 거래량 없음: 대기; close=121.08; 직전 완료 봉 목표를 다음 봉 시가에 모의 적용 |

### 같은 기간의 비용·노출 비교 (사후 연구)

| 전략 | 비용 전 | 비용 후 | 100% 보유 | 같은 평균 노출 보유 | 평균 노출 |
|---|---:|---:|---:|---:|---:|
| cash | 0.00% | 0.00% | 14.14% | 0.00% | 0.00% |
| buy_hold | 14.62% | 14.14% | 14.14% | 14.14% | 100.00% |
| trend_8_26 | 10.14% | 6.50% | 14.14% | 10.09% | 73.11% |
| momentum_26 | 13.96% | 9.27% | 14.14% | 10.66% | 77.02% |
| breakout_8 | 6.46% | -11.87% | 14.14% | 3.70% | 27.94% |
| reversion_12 | 2.14% | -7.65% | 14.14% | 2.36% | 18.02% |
| volume_26 | 2.67% | -2.38% | 14.14% | 0.64% | 4.96% |
| trend_8_26 AND momentum_26 | 11.05% | 7.39% | 14.14% | 9.40% | 68.41% |
| trend_8_26 + momentum_26 | 12.03% | 7.88% | 14.14% | 10.38% | 75.07% |
| trend_8_26 AND breakout_8 | 6.87% | -8.51% | 14.14% | 3.13% | 23.76% |
| trend_8_26 + breakout_8 | 8.30% | -2.91% | 14.14% | 6.83% | 50.53% |
| trend_8_26 AND reversion_12 | -0.82% | -6.48% | 14.14% | 0.95% | 7.31% |
| trend_8_26 + reversion_12 | 6.11% | -0.40% | 14.14% | 6.13% | 45.57% |
| trend_8_26 AND volume_26 | 0.13% | -1.95% | 14.14% | 0.24% | 1.83% |
| trend_8_26 + volume_26 | 6.38% | 2.19% | 14.14% | 5.22% | 39.04% |
| momentum_26 AND breakout_8 | 6.71% | -10.17% | 14.14% | 3.45% | 26.11% |
| momentum_26 + breakout_8 | 10.17% | -1.23% | 14.14% | 7.11% | 52.49% |
| momentum_26 AND reversion_12 | 1.67% | -3.74% | 14.14% | 1.02% | 7.83% |
| momentum_26 + reversion_12 | 7.93% | 1.95% | 14.14% | 6.41% | 47.52% |
| momentum_26 AND volume_26 | 1.72% | -2.05% | 14.14% | 0.34% | 2.61% |
| momentum_26 + volume_26 | 8.21% | 3.73% | 14.14% | 5.49% | 40.99% |
| breakout_8 AND reversion_12 | 0.00% | 0.00% | 14.14% | 0.00% | 0.00% |
| breakout_8 + reversion_12 | 4.31% | -9.21% | 14.14% | 3.03% | 22.99% |
| breakout_8 AND volume_26 | 0.69% | -2.22% | 14.14% | 0.27% | 2.09% |
| breakout_8 + volume_26 | 4.58% | -7.04% | 14.14% | 2.16% | 16.46% |
| reversion_12 AND volume_26 | 0.43% | -0.83% | 14.14% | 0.14% | 1.04% |
| reversion_12 + volume_26 | 2.42% | -4.25% | 14.14% | 1.50% | 11.49% |
| ema_12_26 | 12.38% | 10.51% | 14.14% | 11.40% | 81.98% |
| macd_12_26_9 | 10.59% | 6.04% | 14.14% | 5.46% | 40.73% |
| rsi_14_recovery | 0.20% | -0.64% | 14.14% | 0.07% | 0.52% |
| bollinger_20_reentry | 1.41% | -0.70% | 14.14% | 0.17% | 1.31% |
| donchian_20 | 4.01% | -9.83% | 14.14% | 1.91% | 14.62% |
| atr_14_breakout | -0.01% | -9.97% | 14.14% | 0.98% | 7.57% |
| session_vwap | 11.24% | 1.00% | 14.14% | 8.22% | 60.31% |
| obv_20 | 12.22% | 4.48% | 14.14% | 8.60% | 62.92% |
| stochastic_14_3_recovery | 0.07% | -8.76% | 14.14% | 0.75% | 5.74% |
| mfi_14_recovery | 1.30% | -0.39% | 14.14% | 0.14% | 1.04% |
| adx_14_trend | 9.95% | 7.22% | 14.14% | 8.07% | 59.27% |
| aroon_25_trend | 8.13% | 2.81% | 14.14% | 4.52% | 33.94% |
| cci_20_momentum | 6.82% | -3.01% | 14.14% | 4.81% | 36.03% |
| williams_14_recovery | 0.63% | -6.30% | 14.14% | 0.58% | 4.44% |
| cmf_20_accumulation | 9.26% | 0.88% | 14.14% | 5.97% | 44.39% |
| chaikin_3_10 | 10.62% | 1.28% | 14.14% | 7.92% | 58.22% |
| roc_10_momentum | 1.03% | -3.94% | 14.14% | 2.23% | 16.97% |
| trix_15_trend | 11.09% | 6.07% | 14.14% | 9.82% | 71.28% |
| keltner_20_breakout | 7.26% | -0.55% | 14.14% | 4.05% | 30.55% |
| opening_range_30m | 11.01% | 4.67% | 14.14% | 5.71% | 42.56% |

동일 구간·초기 자금, 종료 시 청산 비용 포함. 노출 맞춤은 사후 설명용이며 v2 실제 계좌 성과가 아닙니다.
[낙폭 분해·비용 영향·전체 구간](WMT/comparison.json)

[v1 전체 기록](WMT/accounts.json) · [v2 전체 기록](WMT/accounts-v2.json)
