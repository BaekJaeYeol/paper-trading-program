# 모의투자 운영 현황

[PC·서버 장애 진단과 복구 방법](https://github.com/BaekJaeYeol/paper-trading-program/blob/main/investment-lab/docs/failure-recovery.md)

이번 실행 복구: {}

완료 봉 확인 주기: 기록 13/21회 · 기록 없는 예정 8회 · 아직 판정 전 5회 · 주의: 예약 시작 지연 또는 실행·저장 누락을 확인하세요.

[주기 판정 기준](https://github.com/BaekJaeYeol/paper-trading-program/blob/main/investment-lab/docs/session-coverage.md)

최근 확인: 2026-10-23T19:07:00.360384+00:00 (UTC)
다음 15분 확인 목표 (세션 실행 중에만 적용): 2026-10-23T19:22:00+00:00 (UTC, 실행 지연 가능)

실제 주문 없음. v1 기존 계좌와 v2 새 계좌의 시작일이 다르므로 수익률을 직접 우열 비교하지 마세요.
v2는 다음 봉 시가에 비용·스프레드·직전 거래량 제한을 적용한 가상 체결입니다. 미체결 잔량은 만료됩니다.

| 종목 | 상태 | 최근 성공 UTC | 마지막 완료 봉 UTC | 이번 새 봉 |
|---|---|---|---|---|
| SPY | updated | 2026-10-23T19:07:00.360384+00:00 | 2026-10-23T18:45:00+00:00 | 1 |
| QQQ | updated | 2026-10-23T19:07:00.360384+00:00 | 2026-10-23T18:45:00+00:00 | 1 |
| IWM | updated | 2026-10-23T19:07:00.360384+00:00 | 2026-10-23T18:45:00+00:00 | 1 |
| DIA | updated | 2026-10-23T19:07:00.360384+00:00 | 2026-10-23T18:45:00+00:00 | 1 |
| MSFT | updated | 2026-10-23T19:07:00.360384+00:00 | 2026-10-23T18:45:00+00:00 | 1 |
| JPM | updated | 2026-10-23T19:07:00.360384+00:00 | 2026-10-23T18:45:00+00:00 | 1 |
| XOM | updated | 2026-10-23T19:07:00.360384+00:00 | 2026-10-23T18:45:00+00:00 | 1 |
| JNJ | updated | 2026-10-23T19:07:00.360384+00:00 | 2026-10-23T18:45:00+00:00 | 1 |
| CAT | updated | 2026-10-23T19:07:00.360384+00:00 | 2026-10-23T18:45:00+00:00 | 1 |
| WMT | updated | 2026-10-23T19:07:00.360384+00:00 | 2026-10-23T18:45:00+00:00 | 1 |

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
| v1 | buy_hold | 9817.15 | -182.85 | buy /  / buy_hold: prior completed bar target 100%; next bar open simulation |
| v1 | trend_8_26 | 9657.97 | -342.03 | sell /  / trend_8_26: prior completed bar target 0%; next bar open simulation |
| v1 | momentum_26 | 9631.54 | -368.46 | sell /  / momentum_26: prior completed bar target 0%; next bar open simulation |
| v1 | breakout_8 | 9427.76 | -572.24 | sell /  / breakout_8: prior completed bar target 0%; next bar open simulation |
| v1 | reversion_12 | 9454.44 | -545.56 | sell /  / reversion_12: prior completed bar target 0%; next bar open simulation |
| v1 | volume_26 | 9298.73 | -701.27 | buy /  / volume_26: prior completed bar target 100%; next bar open simulation |
| v1 | trend_8_26 AND momentum_26 | 9624.28 | -375.72 | sell /  / trend_8_26 AND momentum_26: prior completed bar target 0%; next bar open simulation |
| v1 | trend_8_26 + momentum_26 | 9644.71 | -355.29 | sell /  / trend_8_26 + momentum_26: prior completed bar target 0%; next bar open simulation |
| v1 | trend_8_26 AND breakout_8 | 9730.71 | -269.29 | sell /  / trend_8_26 AND breakout_8: prior completed bar target 0%; next bar open simulation |
| v1 | trend_8_26 + breakout_8 | 9580.32 | -419.68 | sell /  / trend_8_26 + breakout_8: prior completed bar target 0%; next bar open simulation |
| v1 | trend_8_26 AND reversion_12 | 9736.23 | -263.77 | sell /  / trend_8_26 AND reversion_12: prior completed bar target 0%; next bar open simulation |
| v1 | trend_8_26 + reversion_12 | 9574.56 | -425.44 | sell /  / trend_8_26 + reversion_12: prior completed bar target 0%; next bar open simulation |
| v1 | trend_8_26 AND volume_26 | 9605.36 | -394.64 | sell /  / trend_8_26 AND volume_26: prior completed bar target 0%; next bar open simulation |
| v1 | trend_8_26 + volume_26 | 9476.45 | -523.55 | buy /  / trend_8_26 + volume_26: prior completed bar target 50%; next bar open simulation |
| v1 | momentum_26 AND breakout_8 | 9640.01 | -359.99 | sell /  / momentum_26 AND breakout_8: prior completed bar target 0%; next bar open simulation |
| v1 | momentum_26 + breakout_8 | 9529.11 | -470.89 | sell /  / momentum_26 + breakout_8: prior completed bar target 0%; next bar open simulation |
| v1 | momentum_26 AND reversion_12 | 9769.70 | -230.30 | sell /  / momentum_26 AND reversion_12: prior completed bar target 0%; next bar open simulation |
| v1 | momentum_26 + reversion_12 | 9599.82 | -400.18 | sell /  / momentum_26 + reversion_12: prior completed bar target 0%; next bar open simulation |
| v1 | momentum_26 AND volume_26 | 9618.73 | -381.27 | sell /  / momentum_26 AND volume_26: prior completed bar target 0%; next bar open simulation |
| v1 | momentum_26 + volume_26 | 9463.48 | -536.52 | buy /  / momentum_26 + volume_26: prior completed bar target 50%; next bar open simulation |
| v1 | breakout_8 AND reversion_12 | 10000.00 | 0.00 | 대기 /  / 새 신호 대기 |
| v1 | breakout_8 + reversion_12 | 9478.47 | -521.53 | sell /  / breakout_8 + reversion_12: prior completed bar target 0%; next bar open simulation |
| v1 | breakout_8 AND volume_26 | 9807.14 | -192.86 | sell /  / breakout_8 AND volume_26: prior completed bar target 0%; next bar open simulation |
| v1 | breakout_8 + volume_26 | 9400.19 | -599.81 | buy /  / breakout_8 + volume_26: prior completed bar target 50%; next bar open simulation |
| v1 | reversion_12 AND volume_26 | 9811.81 | -188.19 | sell /  / reversion_12 AND volume_26: prior completed bar target 0%; next bar open simulation |
| v1 | reversion_12 + volume_26 | 9470.14 | -529.86 | buy /  / reversion_12 + volume_26: prior completed bar target 50%; next bar open simulation |
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
| v2 | buy_hold | 9746.34 | -253.66 | buy / partial / 직전 완료 봉 목표 비중 100%; 다음 봉 시가 가정 |
| v2 | trend_8_26 | 9536.87 | -463.13 | sell / filled / 직전 완료 봉 목표 비중 0%; 다음 봉 시가 가정 |
| v2 | momentum_26 | 9482.22 | -517.78 | sell / filled / 직전 완료 봉 목표 비중 0%; 다음 봉 시가 가정 |
| v2 | breakout_8 | 9024.03 | -975.97 | sell / filled / 직전 완료 봉 목표 비중 0%; 다음 봉 시가 가정 |
| v2 | reversion_12 | 9001.86 | -998.14 | 중단: 손실 한도 / buy / partial / 직전 완료 봉 목표 비중 100%; 다음 봉 시가 가정 |
| v2 | volume_26 | 8959.26 | -1040.74 | 중단: 손실 한도 / buy / partial / 직전 완료 봉 목표 비중 100%; 다음 봉 시가 가정 |
| v2 | trend_8_26 AND momentum_26 | 9481.53 | -518.47 | sell / filled / 직전 완료 봉 목표 비중 0%; 다음 봉 시가 가정 |
| v2 | trend_8_26 + momentum_26 | 9509.48 | -490.52 | sell / filled / 직전 완료 봉 목표 비중 0%; 다음 봉 시가 가정 |
| v2 | trend_8_26 AND breakout_8 | 9547.25 | -452.75 | sell / filled / 직전 완료 봉 목표 비중 0%; 다음 봉 시가 가정 |
| v2 | trend_8_26 + breakout_8 | 9315.73 | -684.27 | sell / filled / 직전 완료 봉 목표 비중 0%; 다음 봉 시가 가정 |
| v2 | trend_8_26 AND reversion_12 | 9621.61 | -378.39 | sell / filled / 직전 완료 봉 목표 비중 0%; 다음 봉 시가 가정 |
| v2 | trend_8_26 + reversion_12 | 9278.51 | -721.49 | sell / filled / 직전 완료 봉 목표 비중 0%; 다음 봉 시가 가정 |
| v2 | trend_8_26 AND volume_26 | 9442.22 | -557.78 | sell / filled / 직전 완료 봉 목표 비중 0%; 다음 봉 시가 가정 |
| v2 | trend_8_26 + volume_26 | 9153.96 | -846.04 | buy / filled / 직전 완료 봉 목표 비중 50%; 다음 봉 시가 가정 |
| v2 | momentum_26 AND breakout_8 | 9414.38 | -585.62 | sell / filled / 직전 완료 봉 목표 비중 0%; 다음 봉 시가 가정 |
| v2 | momentum_26 + breakout_8 | 9250.22 | -749.78 | sell / filled / 직전 완료 봉 목표 비중 0%; 다음 봉 시가 가정 |
| v2 | momentum_26 AND reversion_12 | 9722.08 | -277.92 | sell / filled / 직전 완료 봉 목표 비중 0%; 다음 봉 시가 가정 |
| v2 | momentum_26 + reversion_12 | 9310.42 | -689.58 | sell / filled / 직전 완료 봉 목표 비중 0%; 다음 봉 시가 가정 |
| v2 | momentum_26 AND volume_26 | 9523.88 | -476.12 | sell / filled / 직전 완료 봉 목표 비중 0%; 다음 봉 시가 가정 |
| v2 | momentum_26 + volume_26 | 9166.09 | -833.91 | buy / filled / 직전 완료 봉 목표 비중 50%; 다음 봉 시가 가정 |
| v2 | breakout_8 AND reversion_12 | 10000.00 | 0.00 | 대기 /  / 새 신호 대기 |
| v2 | breakout_8 + reversion_12 | 9082.29 | -917.71 | sell / filled / 직전 완료 봉 목표 비중 0%; 다음 봉 시가 가정 |
| v2 | breakout_8 AND volume_26 | 9733.81 | -266.19 | sell / filled / 직전 완료 봉 목표 비중 0%; 다음 봉 시가 가정 |
| v2 | breakout_8 + volume_26 | 8990.64 | -1009.36 | 중단: 손실 한도 / sell / filled / 직전 완료 봉 목표 비중 0%; 다음 봉 시가 가정 |
| v2 | reversion_12 AND volume_26 | 9552.33 | -447.67 | sell / filled / 직전 완료 봉 목표 비중 0%; 다음 봉 시가 가정 |
| v2 | reversion_12 + volume_26 | 9038.20 | -961.80 | buy / filled / 직전 완료 봉 목표 비중 50%; 다음 봉 시가 가정 |
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
| cash | 0.00% | 0.00% | -1.88% | -0.00% | 0.00% |
| buy_hold | -1.47% | -1.88% | -1.88% | -1.88% | 100.00% |
| trend_8_26 | -0.61% | -4.29% | -1.88% | -0.93% | 49.35% |
| momentum_26 | -1.29% | -5.35% | -1.88% | -0.90% | 48.04% |
| breakout_8 | -0.27% | -16.40% | -1.88% | -0.43% | 22.72% |
| reversion_12 | -1.03% | -12.38% | -1.88% | -0.54% | 28.72% |
| volume_26 | -1.18% | -12.51% | -1.88% | -0.20% | 10.70% |
| trend_8_26 AND momentum_26 | -0.50% | -4.59% | -1.88% | -0.79% | 42.04% |
| trend_8_26 + momentum_26 | -0.95% | -4.82% | -1.88% | -0.92% | 48.70% |
| trend_8_26 AND breakout_8 | 0.27% | -10.48% | -1.88% | -0.28% | 14.62% |
| trend_8_26 + breakout_8 | -0.44% | -10.18% | -1.88% | -0.68% | 36.04% |
| trend_8_26 AND reversion_12 | 0.20% | -4.32% | -1.88% | -0.12% | 6.27% |
| trend_8_26 + reversion_12 | -0.81% | -8.05% | -1.88% | -0.73% | 39.04% |
| trend_8_26 AND volume_26 | -1.05% | -6.30% | -1.88% | -0.10% | 5.48% |
| trend_8_26 + volume_26 | -0.89% | -8.50% | -1.88% | -0.57% | 30.03% |
| momentum_26 AND breakout_8 | 0.27% | -10.85% | -1.88% | -0.29% | 15.40% |
| momentum_26 + breakout_8 | -0.78% | -11.05% | -1.88% | -0.67% | 35.39% |
| momentum_26 AND reversion_12 | -0.39% | -4.89% | -1.88% | -0.11% | 6.01% |
| momentum_26 + reversion_12 | -1.16% | -8.17% | -1.88% | -0.72% | 38.39% |
| momentum_26 AND volume_26 | -0.79% | -5.27% | -1.88% | -0.07% | 3.92% |
| momentum_26 + volume_26 | -1.23% | -8.24% | -1.88% | -0.55% | 29.38% |
| breakout_8 AND reversion_12 | 0.00% | 0.00% | -1.88% | -0.00% | 0.00% |
| breakout_8 + reversion_12 | -0.65% | -13.71% | -1.88% | -0.48% | 25.73% |
| breakout_8 AND volume_26 | -0.26% | -3.15% | -1.88% | -0.04% | 2.35% |
| breakout_8 + volume_26 | -0.73% | -13.95% | -1.88% | -0.31% | 16.72% |
| reversion_12 AND volume_26 | -0.97% | -5.05% | -1.88% | -0.07% | 3.66% |
| reversion_12 + volume_26 | -1.10% | -11.34% | -1.88% | -0.37% | 19.72% |
| ema_12_26 | -1.47% | -4.73% | -1.88% | -0.96% | 50.91% |
| macd_12_26_9 | -0.36% | -4.86% | -1.88% | -0.59% | 31.59% |
| rsi_14_recovery | -0.42% | -3.71% | -1.88% | -0.04% | 2.09% |
| bollinger_20_reentry | -0.89% | -6.94% | -1.88% | -0.07% | 3.92% |
| donchian_20 | 0.22% | -7.85% | -1.88% | -0.14% | 7.31% |
| atr_14_breakout | 0.45% | -4.89% | -1.88% | -0.07% | 3.66% |
| session_vwap | -0.68% | -11.33% | -1.88% | -0.90% | 48.04% |
| obv_20 | -1.20% | -9.92% | -1.88% | -0.66% | 34.99% |
| stochastic_14_3_recovery | 0.64% | -14.20% | -1.88% | -0.19% | 9.92% |
| mfi_14_recovery | 0.11% | -2.79% | -1.88% | -0.03% | 1.83% |
| adx_14_trend | 1.03% | -0.65% | -1.88% | -0.41% | 21.93% |
| aroon_25_trend | 0.13% | -2.36% | -1.88% | -0.44% | 23.24% |
| cci_20_momentum | 0.19% | -7.49% | -1.88% | -0.40% | 21.15% |
| williams_14_recovery | 0.50% | -11.77% | -1.88% | -0.15% | 8.09% |
| cmf_20_accumulation | 0.36% | -4.58% | -1.88% | -0.93% | 49.35% |
| chaikin_3_10 | -0.17% | -7.44% | -1.88% | -0.72% | 38.12% |
| roc_10_momentum | -0.07% | -0.49% | -1.88% | -0.00% | 0.26% |
| trix_15_trend | -1.32% | -6.56% | -1.88% | -0.72% | 38.38% |
| keltner_20_breakout | 0.19% | -3.93% | -1.88% | -0.20% | 10.70% |
| opening_range_30m | -0.27% | -6.36% | -1.88% | -0.82% | 43.34% |

동일 구간·초기 자금, 종료 시 청산 비용 포함. 노출 맞춤은 사후 설명용이며 v2 실제 계좌 성과가 아닙니다.
[낙폭 분해·비용 영향·전체 구간](SPY/comparison.json)

[v1 전체 기록](SPY/accounts.json) · [v2 전체 기록](SPY/accounts-v2.json)

## QQQ 계좌

| 모델 | 전략 | 평가액 USD | 손익 USD | 최근 매매·이유 |
|---|---|---:|---:|---|
| v1 | cash | 10000.00 | 0.00 | 대기 /  / 새 신호 대기 |
| v1 | buy_hold | 9699.32 | -300.68 | buy /  / buy_hold: prior completed bar target 100%; next bar open simulation |
| v1 | trend_8_26 | 9617.69 | -382.31 | sell /  / trend_8_26: prior completed bar target 0%; next bar open simulation |
| v1 | momentum_26 | 9252.85 | -747.15 | buy /  / momentum_26: prior completed bar target 100%; next bar open simulation |
| v1 | breakout_8 | 9463.64 | -536.36 | sell /  / breakout_8: prior completed bar target 0%; next bar open simulation |
| v1 | reversion_12 | 9464.61 | -535.39 | buy /  / reversion_12: prior completed bar target 100%; next bar open simulation |
| v1 | volume_26 | 9446.81 | -553.19 | sell /  / volume_26: prior completed bar target 0%; next bar open simulation |
| v1 | trend_8_26 AND momentum_26 | 9594.04 | -405.96 | sell /  / trend_8_26 AND momentum_26: prior completed bar target 0%; next bar open simulation |
| v1 | trend_8_26 + momentum_26 | 9471.38 | -528.62 | sell /  / trend_8_26 + momentum_26: prior completed bar target 50%; next bar open simulation |
| v1 | trend_8_26 AND breakout_8 | 9893.81 | -106.19 | sell /  / trend_8_26 AND breakout_8: prior completed bar target 0%; next bar open simulation |
| v1 | trend_8_26 + breakout_8 | 9597.94 | -402.06 | sell /  / trend_8_26 + breakout_8: prior completed bar target 0%; next bar open simulation |
| v1 | trend_8_26 AND reversion_12 | 9856.40 | -143.60 | sell /  / trend_8_26 AND reversion_12: prior completed bar target 0%; next bar open simulation |
| v1 | trend_8_26 + reversion_12 | 9598.41 | -401.59 | buy /  / trend_8_26 + reversion_12: prior completed bar target 50%; next bar open simulation |
| v1 | trend_8_26 AND volume_26 | 9771.73 | -228.27 | sell /  / trend_8_26 AND volume_26: prior completed bar target 0%; next bar open simulation |
| v1 | trend_8_26 + volume_26 | 9531.96 | -468.04 | sell /  / trend_8_26 + volume_26: prior completed bar target 0%; next bar open simulation |
| v1 | momentum_26 AND breakout_8 | 9644.64 | -355.36 | sell /  / momentum_26 AND breakout_8: prior completed bar target 0%; next bar open simulation |
| v1 | momentum_26 + breakout_8 | 9376.62 | -623.38 | buy /  / momentum_26 + breakout_8: prior completed bar target 50%; next bar open simulation |
| v1 | momentum_26 AND reversion_12 | 9761.29 | -238.71 | buy /  / momentum_26 AND reversion_12: prior completed bar target 100%; next bar open simulation |
| v1 | momentum_26 + reversion_12 | 9433.51 | -566.49 | buy /  / momentum_26 + reversion_12: prior completed bar target 100%; next bar open simulation |
| v1 | momentum_26 AND volume_26 | 9789.69 | -210.31 | sell /  / momentum_26 AND volume_26: prior completed bar target 0%; next bar open simulation |
| v1 | momentum_26 + volume_26 | 9368.10 | -631.90 | buy /  / momentum_26 + volume_26: prior completed bar target 50%; next bar open simulation |
| v1 | breakout_8 AND reversion_12 | 10000.00 | 0.00 | 대기 /  / 새 신호 대기 |
| v1 | breakout_8 + reversion_12 | 9501.89 | -498.11 | buy /  / breakout_8 + reversion_12: prior completed bar target 50%; next bar open simulation |
| v1 | breakout_8 AND volume_26 | 9873.64 | -126.36 | sell /  / breakout_8 AND volume_26: prior completed bar target 0%; next bar open simulation |
| v1 | breakout_8 + volume_26 | 9531.07 | -468.93 | sell /  / breakout_8 + volume_26: prior completed bar target 0%; next bar open simulation |
| v1 | reversion_12 AND volume_26 | 9791.68 | -208.32 | sell /  / reversion_12 AND volume_26: prior completed bar target 0%; next bar open simulation |
| v1 | reversion_12 + volume_26 | 9493.42 | -506.58 | buy /  / reversion_12 + volume_26: prior completed bar target 50%; next bar open simulation |
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
| v2 | buy_hold | 9385.79 | -614.21 | 중단: 손실 한도 / buy / partial / 직전 완료 봉 목표 비중 100%; 다음 봉 시가 가정 |
| v2 | trend_8_26 | 9419.46 | -580.54 | sell / filled / 직전 완료 봉 목표 비중 0%; 다음 봉 시가 가정 |
| v2 | momentum_26 | 9140.87 | -859.13 | buy / partial / 직전 완료 봉 목표 비중 100%; 다음 봉 시가 가정 |
| v2 | breakout_8 | 9129.27 | -870.73 | sell / filled / 직전 완료 봉 목표 비중 0%; 다음 봉 시가 가정 |
| v2 | reversion_12 | 8978.49 | -1021.51 | 중단: 손실 한도 / buy / partial / 직전 완료 봉 목표 비중 100%; 다음 봉 시가 가정 |
| v2 | volume_26 | 9565.80 | -434.20 | 중단: 손실 한도 / sell / filled / 직전 완료 봉 목표 비중 0%; 다음 봉 시가 가정 |
| v2 | trend_8_26 AND momentum_26 | 9484.57 | -515.43 | sell / filled / 직전 완료 봉 목표 비중 0%; 다음 봉 시가 가정 |
| v2 | trend_8_26 + momentum_26 | 9318.28 | -681.72 | sell / filled / 직전 완료 봉 목표 비중 50%; 다음 봉 시가 가정 |
| v2 | trend_8_26 AND breakout_8 | 9782.92 | -217.08 | sell / filled / 직전 완료 봉 목표 비중 0%; 다음 봉 시가 가정 |
| v2 | trend_8_26 + breakout_8 | 9331.95 | -668.05 | sell / filled / 직전 완료 봉 목표 비중 0%; 다음 봉 시가 가정 |
| v2 | trend_8_26 AND reversion_12 | 9711.76 | -288.24 | sell / filled / 직전 완료 봉 목표 비중 0%; 다음 봉 시가 가정 |
| v2 | trend_8_26 + reversion_12 | 9254.27 | -745.73 | buy / filled / 직전 완료 봉 목표 비중 50%; 다음 봉 시가 가정 |
| v2 | trend_8_26 AND volume_26 | 9602.02 | -397.98 | sell / filled / 직전 완료 봉 목표 비중 0%; 다음 봉 시가 가정 |
| v2 | trend_8_26 + volume_26 | 9135.34 | -864.66 | sell / filled / 직전 완료 봉 목표 비중 0%; 다음 봉 시가 가정 |
| v2 | momentum_26 AND breakout_8 | 9591.37 | -408.63 | sell / filled / 직전 완료 봉 목표 비중 0%; 다음 봉 시가 가정 |
| v2 | momentum_26 + breakout_8 | 9154.44 | -845.56 | buy / filled / 직전 완료 봉 목표 비중 50%; 다음 봉 시가 가정 |
| v2 | momentum_26 AND reversion_12 | 9752.51 | -247.49 | buy / partial / 직전 완료 봉 목표 비중 100%; 다음 봉 시가 가정 |
| v2 | momentum_26 + reversion_12 | 9154.79 | -845.21 | buy / partial / 직전 완료 봉 목표 비중 100%; 다음 봉 시가 가정 |
| v2 | momentum_26 AND volume_26 | 9718.13 | -281.87 | sell / filled / 직전 완료 봉 목표 비중 0%; 다음 봉 시가 가정 |
| v2 | momentum_26 + volume_26 | 9018.10 | -981.90 | buy / filled / 직전 완료 봉 목표 비중 50%; 다음 봉 시가 가정 |
| v2 | breakout_8 AND reversion_12 | 10000.00 | 0.00 | 대기 /  / 새 신호 대기 |
| v2 | breakout_8 + reversion_12 | 9148.62 | -851.38 | buy / filled / 직전 완료 봉 목표 비중 50%; 다음 봉 시가 가정 |
| v2 | breakout_8 AND volume_26 | 9814.43 | -185.57 | sell / filled / 직전 완료 봉 목표 비중 0%; 다음 봉 시가 가정 |
| v2 | breakout_8 + volume_26 | 9107.44 | -892.56 | sell / filled / 직전 완료 봉 목표 비중 0%; 다음 봉 시가 가정 |
| v2 | reversion_12 AND volume_26 | 9547.64 | -452.36 | 중단: 손실 한도 / sell / filled / 직전 완료 봉 목표 비중 0%; 다음 봉 시가 가정 |
| v2 | reversion_12 + volume_26 | 8986.78 | -1013.22 | 중단: 손실 한도 / buy / filled / 직전 완료 봉 목표 비중 50%; 다음 봉 시가 가정 |
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
| cash | 0.00% | 0.00% | -6.67% | -0.00% | 0.00% |
| buy_hold | -6.27% | -6.67% | -6.67% | -6.67% | 100.00% |
| trend_8_26 | -2.45% | -6.07% | -6.67% | -2.72% | 40.21% |
| momentum_26 | -4.50% | -10.33% | -6.67% | -2.27% | 33.42% |
| breakout_8 | -2.12% | -16.91% | -6.67% | -1.25% | 18.28% |
| reversion_12 | -0.47% | -13.35% | -6.67% | -2.25% | 33.16% |
| volume_26 | -0.60% | -15.62% | -6.67% | -1.26% | 18.54% |
| trend_8_26 AND momentum_26 | -1.30% | -5.36% | -6.67% | -1.92% | 28.20% |
| trend_8_26 + momentum_26 | -3.47% | -7.64% | -6.67% | -2.50% | 36.82% |
| trend_8_26 AND breakout_8 | 0.08% | -7.98% | -6.67% | -0.75% | 10.97% |
| trend_8_26 + breakout_8 | -2.28% | -10.91% | -6.67% | -1.99% | 29.25% |
| trend_8_26 AND reversion_12 | -0.24% | -3.94% | -6.67% | -0.43% | 6.27% |
| trend_8_26 + reversion_12 | -1.45% | -9.03% | -6.67% | -2.49% | 36.69% |
| trend_8_26 AND volume_26 | 0.17% | -5.15% | -6.67% | -0.41% | 6.01% |
| trend_8_26 + volume_26 | -1.52% | -10.98% | -6.67% | -2.00% | 29.38% |
| momentum_26 AND breakout_8 | -0.42% | -8.06% | -6.67% | -0.70% | 10.18% |
| momentum_26 + breakout_8 | -3.31% | -13.32% | -6.67% | -1.76% | 25.85% |
| momentum_26 AND reversion_12 | -1.19% | -5.26% | -6.67% | -0.39% | 5.74% |
| momentum_26 + reversion_12 | -2.49% | -10.74% | -6.67% | -2.26% | 33.30% |
| momentum_26 AND volume_26 | -0.37% | -4.07% | -6.67% | -0.25% | 3.66% |
| momentum_26 + volume_26 | -2.56% | -12.65% | -6.67% | -1.77% | 25.99% |
| breakout_8 AND reversion_12 | 0.00% | 0.00% | -6.67% | -0.00% | 0.00% |
| breakout_8 + reversion_12 | -1.29% | -14.08% | -6.67% | -1.75% | 25.73% |
| breakout_8 AND volume_26 | 0.15% | -2.75% | -6.67% | -0.18% | 2.61% |
| breakout_8 + volume_26 | -1.36% | -14.50% | -6.67% | -1.25% | 18.42% |
| reversion_12 AND volume_26 | -1.12% | -8.70% | -6.67% | -0.61% | 8.88% |
| reversion_12 + volume_26 | -0.53% | -13.96% | -6.67% | -1.76% | 25.86% |
| ema_12_26 | -3.97% | -6.75% | -6.67% | -2.16% | 31.85% |
| macd_12_26_9 | -0.54% | -4.63% | -6.67% | -1.37% | 20.10% |
| rsi_14_recovery | -0.50% | -6.97% | -6.67% | -0.29% | 4.18% |
| bollinger_20_reentry | -0.05% | -5.76% | -6.67% | -0.25% | 3.66% |
| donchian_20 | 0.55% | -4.39% | -6.67% | -0.36% | 5.22% |
| atr_14_breakout | 0.52% | -3.21% | -6.67% | -0.18% | 2.61% |
| session_vwap | -3.12% | -14.59% | -6.67% | -3.18% | 47.00% |
| obv_20 | -4.37% | -13.18% | -6.67% | -1.40% | 20.63% |
| stochastic_14_3_recovery | 0.14% | -12.82% | -6.67% | -0.59% | 8.62% |
| mfi_14_recovery | -1.13% | -3.99% | -6.67% | -0.13% | 1.83% |
| adx_14_trend | 0.42% | -2.08% | -6.67% | -1.30% | 19.06% |
| aroon_25_trend | 0.17% | -2.73% | -6.67% | -0.98% | 14.36% |
| cci_20_momentum | 0.37% | -4.56% | -6.67% | -1.19% | 17.49% |
| williams_14_recovery | -0.24% | -12.05% | -6.67% | -0.54% | 7.83% |
| cmf_20_accumulation | -3.18% | -10.60% | -6.67% | -2.20% | 32.38% |
| chaikin_3_10 | -5.49% | -13.83% | -6.67% | -1.72% | 25.33% |
| roc_10_momentum | 0.41% | -0.43% | -6.67% | -0.20% | 2.87% |
| trix_15_trend | -2.85% | -6.46% | -6.67% | -1.78% | 26.11% |
| keltner_20_breakout | -0.36% | -4.46% | -6.67% | -0.46% | 6.79% |
| opening_range_30m | -2.08% | -7.67% | -6.67% | -2.51% | 37.08% |

동일 구간·초기 자금, 종료 시 청산 비용 포함. 노출 맞춤은 사후 설명용이며 v2 실제 계좌 성과가 아닙니다.
[낙폭 분해·비용 영향·전체 구간](QQQ/comparison.json)

[v1 전체 기록](QQQ/accounts.json) · [v2 전체 기록](QQQ/accounts-v2.json)

## IWM 계좌

| 모델 | 전략 | 평가액 USD | 손익 USD | 최근 매매·이유 |
|---|---|---:|---:|---|
| v1 | cash | 10000.00 | 0.00 | 대기 /  / 새 신호 대기 |
| v1 | buy_hold | 9988.00 | -12.00 | buy /  / buy_hold: prior completed bar target 100%; next bar open simulation |
| v1 | trend_8_26 | 9661.23 | -338.77 | buy /  / trend_8_26: prior completed bar target 100%; next bar open simulation |
| v1 | momentum_26 | 9607.76 | -392.24 | sell /  / momentum_26: prior completed bar target 0%; next bar open simulation |
| v1 | breakout_8 | 9221.05 | -778.95 | sell /  / breakout_8: prior completed bar target 0%; next bar open simulation |
| v1 | reversion_12 | 9713.04 | -286.96 | sell /  / reversion_12: prior completed bar target 0%; next bar open simulation |
| v1 | volume_26 | 9851.14 | -148.86 | sell /  / volume_26: prior completed bar target 0%; next bar open simulation |
| v1 | trend_8_26 AND momentum_26 | 9608.92 | -391.08 | sell /  / trend_8_26 AND momentum_26: prior completed bar target 0%; next bar open simulation |
| v1 | trend_8_26 + momentum_26 | 9653.86 | -346.14 | sell /  / trend_8_26 + momentum_26: prior completed bar target 50%; next bar open simulation |
| v1 | trend_8_26 AND breakout_8 | 9404.46 | -595.54 | sell /  / trend_8_26 AND breakout_8: prior completed bar target 0%; next bar open simulation |
| v1 | trend_8_26 + breakout_8 | 9438.76 | -561.24 | buy /  / trend_8_26 + breakout_8: prior completed bar target 50%; next bar open simulation |
| v1 | trend_8_26 AND reversion_12 | 9755.06 | -244.94 | sell /  / trend_8_26 AND reversion_12: prior completed bar target 0%; next bar open simulation |
| v1 | trend_8_26 + reversion_12 | 9686.85 | -313.15 | buy /  / trend_8_26 + reversion_12: prior completed bar target 50%; next bar open simulation |
| v1 | trend_8_26 AND volume_26 | 9893.73 | -106.27 | sell /  / trend_8_26 AND volume_26: prior completed bar target 0%; next bar open simulation |
| v1 | trend_8_26 + volume_26 | 9775.06 | -224.94 | buy /  / trend_8_26 + volume_26: prior completed bar target 50%; next bar open simulation |
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
| v1 | ema_12_26 | 9660.09 | -339.91 | sell /  / EMA12 > EMA26; 조건 미충족; EMA12=275.689, EMA26=275.69 |
| v1 | macd_12_26_9 | 9749.85 | -250.15 | sell /  / MACD > 신호선 그리고 MACD > 0; 조건 미충족; MACD=-0.00119186, signal9=-0.0266722 |
| v1 | rsi_14_recovery | 9786.95 | -213.05 | sell /  / 직전 RSI14 < 30, 현재 RSI14 >= 30 (한 봉 목표); 조건 미충족; RSI14=46.986, previous_RSI14=37.1649 |
| v1 | bollinger_20_reentry | 9762.11 | -237.89 | sell /  / 직전 종가 < 직전 하단밴드, 현재 하단밴드 <= 종가 <= SMA20 (한 봉 목표); 조건 미충족; close=275.725, lower20=274.173, SMA20=275.605, previous_lower20=274.15 |
| v1 | donchian_20 | 9835.91 | -164.09 | sell /  / 종가 > 현재 봉을 제외한 직전 20봉 최고가; 조건 미충족; close=275.785, prior_high20=276.875 |
| v1 | atr_14_breakout | 9685.22 | -314.78 | sell /  / 종가 > 직전 종가 + 직전 ATR14 그리고 종가 > EMA26; 조건 미충족; close=274.63, threshold=277.369, prior_ATR14=0.659199, EMA26=275.963 |
| v1 | session_vwap | 9247.31 | -752.69 | buy /  / 종가 > 뉴욕 거래일별 누적 전형가격 VWAP; 조건 충족; close=275.03, session_VWAP=274.45, session_volume=6.20261e+06 |
| v1 | obv_20 | 9624.91 | -375.09 | sell /  / OBV > OBV의 SMA20 그리고 종가 > EMA26; 조건 미충족; OBV=-2.65101e+07, OBV_SMA20=-2.63464e+07, close=274.63, EMA26=275.963 |
| v1 | stochastic_14_3_recovery | 9613.95 | -386.05 | sell /  / 직전 %K14 < 20에서 %K14가 %D3 상향 돌파 (한 봉 목표); 조건 미충족; K14=68.0001, D3=43.5239, previous_K14=48.1428, previous_D3=23.7507 |
| v1 | mfi_14_recovery | 9934.22 | -65.78 | sell /  / 직전 MFI14 < 20, 현재 MFI14 >= 20 (한 봉 목표); 조건 미충족; MFI14=34.131, previous_MFI14=22.0435 |
| v1 | adx_14_trend | 9726.05 | -273.95 | sell /  / Wilder ADX14 >= 25 그리고 +DI14 > -DI14; 조건 미충족; ADX14=27.8461, plus_DI14=25.882, minus_DI14=28.4558 |
| v1 | aroon_25_trend | 9745.85 | -254.15 | sell /  / Aroon25 Up > 70 그리고 Down < 30 (동률이면 최신 극값); 조건 미충족; Aroon_up=68, Aroon_down=4 |
| v1 | cci_20_momentum | 9722.50 | -277.50 | sell /  / CCI20 > 100 (전형가격·평균절대편차); 조건 미충족; CCI20=-314.625 |
| v1 | williams_14_recovery | 9742.36 | -257.64 | sell /  / 직전 Williams %R14 < -80, 현재 >= -80 (한 봉 목표); 조건 미충족; Williams_R14=-31.9999, previous_R14=-51.8572 |
| v1 | cmf_20_accumulation | 9665.18 | -334.82 | buy /  / Chaikin Money Flow20 > 0.1; 조건 충족; CMF20=0.23674, volume20=1.30084e+07 |
| v1 | chaikin_3_10 | 9340.54 | -659.46 | sell /  / ADL의 EMA3 - EMA10 > 0 그리고 종가 > EMA26; 조건 미충족; Chaikin3_10=105567, ADL=-2.68677e+07, close=275.63, EMA26=275.69 |
| v1 | roc_10_momentum | 9996.39 | -3.61 | sell /  / 10봉 ROC > 1% 그리고 종가 > EMA26; 조건 미충족; ROC10_percent=0.995963, close=275.315, EMA26=273.754 |
| v1 | trix_15_trend | 9811.92 | -188.08 | sell /  / 15봉 삼중 EMA의 1봉 변화율 TRIX > 0 그리고 종가 > EMA26; 조건 미충족; TRIX15_percent=0.00744142, close=276.06, EMA26=276.447 |
| v1 | keltner_20_breakout | 9879.23 | -120.77 | sell /  / 종가 > EMA20 + 2 x Wilder ATR14; 조건 미충족; close=276.4, upper_Keltner=277.094, EMA20=275.768, ATR14=0.662947 |
| v1 | opening_range_30m | 9944.34 | -55.66 | buy /  / 뉴욕 09:30·09:45 두 완료 봉 최고가를 10:00 이후 종가가 돌파; 조건 충족; close=275.725, opening_high=275.24 |
| v2 | cash | 10000.00 | 0.00 | 대기 /  / 새 신호 대기 |
| v2 | buy_hold | 9881.20 | -118.80 | buy / partial / 직전 완료 봉 목표 비중 100%; 다음 봉 시가 가정 |
| v2 | trend_8_26 | 9528.41 | -471.59 | buy / partial / 직전 완료 봉 목표 비중 100%; 다음 봉 시가 가정 |
| v2 | momentum_26 | 9466.24 | -533.76 | sell / filled / 직전 완료 봉 목표 비중 0%; 다음 봉 시가 가정 |
| v2 | breakout_8 | 8992.16 | -1007.84 | 중단: 손실 한도 / buy / partial / 직전 완료 봉 목표 비중 100%; 다음 봉 시가 가정 |
| v2 | reversion_12 | 9246.43 | -753.57 | sell / filled / 직전 완료 봉 목표 비중 0%; 다음 봉 시가 가정 |
| v2 | volume_26 | 9360.51 | -639.49 | sell / filled / 직전 완료 봉 목표 비중 0%; 다음 봉 시가 가정 |
| v2 | trend_8_26 AND momentum_26 | 9617.18 | -382.82 | sell / filled / 직전 완료 봉 목표 비중 0%; 다음 봉 시가 가정 |
| v2 | trend_8_26 + momentum_26 | 9537.48 | -462.52 | sell / filled / 직전 완료 봉 목표 비중 50%; 다음 봉 시가 가정 |
| v2 | trend_8_26 AND breakout_8 | 9300.05 | -699.95 | sell / filled / 직전 완료 봉 목표 비중 0%; 다음 봉 시가 가정 |
| v2 | trend_8_26 + breakout_8 | 9196.55 | -803.45 | buy / filled / 직전 완료 봉 목표 비중 50%; 다음 봉 시가 가정 |
| v2 | trend_8_26 AND reversion_12 | 9630.14 | -369.86 | sell / filled / 직전 완료 봉 목표 비중 0%; 다음 봉 시가 가정 |
| v2 | trend_8_26 + reversion_12 | 9385.94 | -614.06 | buy / filled / 직전 완료 봉 목표 비중 50%; 다음 봉 시가 가정 |
| v2 | trend_8_26 AND volume_26 | 9752.17 | -247.83 | sell / filled / 직전 완료 봉 목표 비중 0%; 다음 봉 시가 가정 |
| v2 | trend_8_26 + volume_26 | 9483.62 | -516.38 | buy / filled / 직전 완료 봉 목표 비중 50%; 다음 봉 시가 가정 |
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
| v2 | ema_12_26 | 9648.50 | -351.50 | sell / filled / EMA12 > EMA26; 조건 미충족; EMA12=275.689, EMA26=275.69; 직전 완료 봉 목표를 다음 봉 시가에 모의 적용 |
| v2 | macd_12_26_9 | 9738.16 | -261.84 | sell / filled / MACD > 신호선 그리고 MACD > 0; 조건 미충족; MACD=-0.00119186, signal9=-0.0266722; 직전 완료 봉 목표를 다음 봉 시가에 모의 적용 |
| v2 | rsi_14_recovery | 9779.12 | -220.88 | sell / filled / 직전 RSI14 < 30, 현재 RSI14 >= 30 (한 봉 목표); 조건 미충족; RSI14=46.986, previous_RSI14=37.1649; 직전 완료 봉 목표를 다음 봉 시가에 모의 적용 |
| v2 | bollinger_20_reentry | 9750.40 | -249.60 | sell / filled / 직전 종가 < 직전 하단밴드, 현재 하단밴드 <= 종가 <= SMA20 (한 봉 목표); 조건 미충족; close=275.725, lower20=274.173, SMA20=275.605, previous_lower20=274.15; 직전 완료 봉 목표를 다음 봉 시가에 모의 적용 |
| v2 | donchian_20 | 9830.01 | -169.99 | sell / filled / 종가 > 현재 봉을 제외한 직전 20봉 최고가; 조건 미충족; close=275.785, prior_high20=276.875; 직전 완료 봉 목표를 다음 봉 시가에 모의 적용 |
| v2 | atr_14_breakout | 9669.74 | -330.26 | sell / filled / 종가 > 직전 종가 + 직전 ATR14 그리고 종가 > EMA26; 조건 미충족; close=274.63, threshold=277.369, prior_ATR14=0.659199, EMA26=275.963; 직전 완료 봉 목표를 다음 봉 시가에 모의 적용 |
| v2 | session_vwap | 9215.00 | -785.00 | buy / partial / 종가 > 뉴욕 거래일별 누적 전형가격 VWAP; 조건 충족; close=275.03, session_VWAP=274.45, session_volume=6.20261e+06; 직전 완료 봉 목표를 다음 봉 시가에 모의 적용 |
| v2 | obv_20 | 9607.61 | -392.39 | sell / filled / OBV > OBV의 SMA20 그리고 종가 > EMA26; 조건 미충족; OBV=-2.65101e+07, OBV_SMA20=-2.63464e+07, close=274.63, EMA26=275.963; 직전 완료 봉 목표를 다음 봉 시가에 모의 적용 |
| v2 | stochastic_14_3_recovery | 9594.74 | -405.26 | sell / filled / 직전 %K14 < 20에서 %K14가 %D3 상향 돌파 (한 봉 목표); 조건 미충족; K14=68.0001, D3=43.5239, previous_K14=48.1428, previous_D3=23.7507; 직전 완료 봉 목표를 다음 봉 시가에 모의 적용 |
| v2 | mfi_14_recovery | 9930.25 | -69.75 | sell / filled / 직전 MFI14 < 20, 현재 MFI14 >= 20 (한 봉 목표); 조건 미충족; MFI14=34.131, previous_MFI14=22.0435; 직전 완료 봉 목표를 다음 봉 시가에 모의 적용 |
| v2 | adx_14_trend | 9718.27 | -281.73 | sell / filled / Wilder ADX14 >= 25 그리고 +DI14 > -DI14; 조건 미충족; ADX14=27.8461, plus_DI14=25.882, minus_DI14=28.4558; 직전 완료 봉 목표를 다음 봉 시가에 모의 적용 |
| v2 | aroon_25_trend | 9736.11 | -263.89 | sell / filled / Aroon25 Up > 70 그리고 Down < 30 (동률이면 최신 극값); 조건 미충족; Aroon_up=68, Aroon_down=4; 직전 완료 봉 목표를 다음 봉 시가에 모의 적용 |
| v2 | cci_20_momentum | 9708.90 | -291.10 | sell / filled / CCI20 > 100 (전형가격·평균절대편차); 조건 미충족; CCI20=-314.625; 직전 완료 봉 목표를 다음 봉 시가에 모의 적용 |
| v2 | williams_14_recovery | 9726.79 | -273.21 | sell / filled / 직전 Williams %R14 < -80, 현재 >= -80 (한 봉 목표); 조건 미충족; Williams_R14=-31.9999, previous_R14=-51.8572; 직전 완료 봉 목표를 다음 봉 시가에 모의 적용 |
| v2 | cmf_20_accumulation | 9646.84 | -353.16 | buy / partial / Chaikin Money Flow20 > 0.1; 조건 충족; CMF20=0.23674, volume20=1.30084e+07; 직전 완료 봉 목표를 다음 봉 시가에 모의 적용 |
| v2 | chaikin_3_10 | 9312.56 | -687.44 | sell / filled / ADL의 EMA3 - EMA10 > 0 그리고 종가 > EMA26; 조건 미충족; Chaikin3_10=105567, ADL=-2.68677e+07, close=275.63, EMA26=275.69; 직전 완료 봉 목표를 다음 봉 시가에 모의 적용 |
| v2 | roc_10_momentum | 9994.39 | -5.61 | sell / filled / 10봉 ROC > 1% 그리고 종가 > EMA26; 조건 미충족; ROC10_percent=0.995963, close=275.315, EMA26=273.754; 직전 완료 봉 목표를 다음 봉 시가에 모의 적용 |
| v2 | trix_15_trend | 9804.07 | -195.93 | sell / filled / 15봉 삼중 EMA의 1봉 변화율 TRIX > 0 그리고 종가 > EMA26; 조건 미충족; TRIX15_percent=0.00744142, close=276.06, EMA26=276.447; 직전 완료 봉 목표를 다음 봉 시가에 모의 적용 |
| v2 | keltner_20_breakout | 9873.30 | -126.70 | sell / filled / 종가 > EMA20 + 2 x Wilder ATR14; 조건 미충족; close=276.4, upper_Keltner=277.094, EMA20=275.768, ATR14=0.662947; 직전 완료 봉 목표를 다음 봉 시가에 모의 적용 |
| v2 | opening_range_30m | 9939.37 | -60.63 | buy / partial / 뉴욕 09:30·09:45 두 완료 봉 최고가를 10:00 이후 종가가 돌파; 조건 충족; close=275.725, opening_high=275.24; 직전 완료 봉 목표를 다음 봉 시가에 모의 적용 |

### 같은 기간의 비용·노출 비교 (사후 연구)

| 전략 | 비용 전 | 비용 후 | 100% 보유 | 같은 평균 노출 보유 | 평균 노출 |
|---|---:|---:|---:|---:|---:|
| cash | 0.00% | 0.00% | -2.69% | -0.00% | 0.00% |
| buy_hold | -2.28% | -2.69% | -2.69% | -2.69% | 100.00% |
| trend_8_26 | -1.58% | -5.23% | -2.69% | -1.27% | 46.74% |
| momentum_26 | 0.72% | -5.83% | -2.69% | -1.15% | 42.04% |
| breakout_8 | -1.25% | -16.17% | -2.69% | -0.53% | 19.32% |
| reversion_12 | -1.54% | -12.46% | -2.69% | -0.73% | 26.63% |
| volume_26 | 0.06% | -7.22% | -2.69% | -0.24% | 8.62% |
| trend_8_26 AND momentum_26 | 0.12% | -4.00% | -2.69% | -0.98% | 36.03% |
| trend_8_26 + momentum_26 | -0.44% | -4.93% | -2.69% | -1.21% | 44.39% |
| trend_8_26 AND breakout_8 | -0.64% | -9.79% | -2.69% | -0.34% | 12.27% |
| trend_8_26 + breakout_8 | -1.41% | -10.68% | -2.69% | -0.90% | 33.03% |
| trend_8_26 AND reversion_12 | -0.94% | -4.61% | -2.69% | -0.15% | 5.48% |
| trend_8_26 + reversion_12 | -1.55% | -8.93% | -2.69% | -1.00% | 36.69% |
| trend_8_26 AND volume_26 | -0.31% | -3.61% | -2.69% | -0.08% | 2.87% |
| trend_8_26 + volume_26 | -0.76% | -5.84% | -2.69% | -0.76% | 27.68% |
| momentum_26 AND breakout_8 | 0.08% | -9.51% | -2.69% | -0.33% | 12.01% |
| momentum_26 + breakout_8 | -0.27% | -10.78% | -2.69% | -0.84% | 30.69% |
| momentum_26 AND reversion_12 | -0.35% | -2.42% | -2.69% | -0.06% | 2.35% |
| momentum_26 + reversion_12 | -0.41% | -7.87% | -2.69% | -0.94% | 34.34% |
| momentum_26 AND volume_26 | 0.43% | -2.48% | -2.69% | -0.06% | 2.35% |
| momentum_26 + volume_26 | 0.39% | -5.94% | -2.69% | -0.69% | 25.33% |
| breakout_8 AND reversion_12 | 0.00% | 0.00% | -2.69% | -0.00% | 0.00% |
| breakout_8 + reversion_12 | -1.39% | -13.62% | -2.69% | -0.63% | 22.99% |
| breakout_8 AND volume_26 | -0.63% | -3.91% | -2.69% | -0.06% | 2.35% |
| breakout_8 + volume_26 | -0.59% | -11.44% | -2.69% | -0.38% | 13.98% |
| reversion_12 AND volume_26 | 0.75% | -3.80% | -2.69% | -0.10% | 3.66% |
| reversion_12 + volume_26 | -0.74% | -9.32% | -2.69% | -0.48% | 17.63% |
| ema_12_26 | -0.17% | -3.87% | -2.69% | -1.18% | 43.08% |
| macd_12_26_9 | 1.91% | -1.45% | -2.69% | -0.65% | 23.76% |
| rsi_14_recovery | -0.88% | -4.95% | -2.69% | -0.07% | 2.61% |
| bollinger_20_reentry | -0.28% | -5.58% | -2.69% | -0.09% | 3.39% |
| donchian_20 | -0.07% | -4.58% | -2.69% | -0.15% | 5.48% |
| atr_14_breakout | -0.74% | -7.58% | -2.69% | -0.13% | 4.70% |
| session_vwap | -1.55% | -13.93% | -2.69% | -1.39% | 50.91% |
| obv_20 | -0.22% | -5.53% | -2.69% | -1.07% | 39.16% |
| stochastic_14_3_recovery | -0.64% | -12.40% | -2.69% | -0.22% | 7.83% |
| mfi_14_recovery | 0.20% | -3.92% | -2.69% | -0.07% | 2.61% |
| adx_14_trend | 0.33% | -2.17% | -2.69% | -0.83% | 30.29% |
| aroon_25_trend | -0.41% | -4.11% | -2.69% | -0.47% | 17.23% |
| cci_20_momentum | -0.93% | -7.76% | -2.69% | -0.51% | 18.54% |
| williams_14_recovery | 0.07% | -9.15% | -2.69% | -0.17% | 6.01% |
| cmf_20_accumulation | 0.06% | -6.83% | -2.69% | -0.80% | 29.24% |
| chaikin_3_10 | -1.44% | -10.14% | -2.69% | -0.98% | 36.03% |
| roc_10_momentum | 0.32% | -0.52% | -2.69% | -0.10% | 3.66% |
| trix_15_trend | 0.63% | -2.69% | -2.69% | -0.89% | 32.64% |
| keltner_20_breakout | 0.21% | -2.69% | -2.69% | -0.16% | 5.74% |
| opening_range_30m | 1.53% | -2.65% | -2.69% | -0.75% | 27.42% |

동일 구간·초기 자금, 종료 시 청산 비용 포함. 노출 맞춤은 사후 설명용이며 v2 실제 계좌 성과가 아닙니다.
[낙폭 분해·비용 영향·전체 구간](IWM/comparison.json)

[v1 전체 기록](IWM/accounts.json) · [v2 전체 기록](IWM/accounts-v2.json)

## DIA 계좌

| 모델 | 전략 | 평가액 USD | 손익 USD | 최근 매매·이유 |
|---|---|---:|---:|---|
| v1 | cash | 10000.00 | 0.00 | 대기 /  / 새 신호 대기 |
| v1 | buy_hold | 9963.42 | -36.58 | buy /  / buy_hold: prior completed bar target 100%; next bar open simulation |
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
| v1 | cmf_20_accumulation | 9348.82 | -651.18 | buy /  / Chaikin Money Flow20 > 0.1; 조건 충족; CMF20=0.115503, volume20=1.66288e+06 |
| v1 | chaikin_3_10 | 9611.06 | -388.94 | sell /  / ADL의 EMA3 - EMA10 > 0 그리고 종가 > EMA26; 조건 미충족; Chaikin3_10=70160.2, ADL=-1.15315e+07, close=522.39, EMA26=526.494 |
| v1 | roc_10_momentum | 9939.01 | -60.99 | sell /  / 10봉 ROC > 1% 그리고 종가 > EMA26; 조건 미충족; ROC10_percent=0.771645, close=523.68, EMA26=521.367 |
| v1 | trix_15_trend | 9741.60 | -258.40 | sell /  / 15봉 삼중 EMA의 1봉 변화율 TRIX > 0 그리고 종가 > EMA26; 조건 미충족; TRIX15_percent=0.0047414, close=522.39, EMA26=526.494 |
| v1 | keltner_20_breakout | 9826.82 | -173.18 | sell /  / 종가 > EMA20 + 2 x Wilder ATR14; 조건 미충족; close=526.34, upper_Keltner=527.991, EMA20=526.293, ATR14=0.848911 |
| v1 | opening_range_30m | 9536.25 | -463.75 | sell /  / 뉴욕 09:30·09:45 두 완료 봉 최고가를 10:00 이후 종가가 돌파; 자료 부족·변동폭 또는 거래량 없음: 대기; close=522.39 |
| v2 | cash | 10000.00 | 0.00 | 대기 /  / 새 신호 대기 |
| v2 | buy_hold | 10086.86 | 86.86 | buy / partial / 직전 완료 봉 목표 비중 100%; 다음 봉 시가 가정 |
| v2 | trend_8_26 | 9784.94 | -215.06 | sell / filled / 직전 완료 봉 목표 비중 0%; 다음 봉 시가 가정 |
| v2 | momentum_26 | 9699.02 | -300.98 | sell / filled / 직전 완료 봉 목표 비중 0%; 다음 봉 시가 가정 |
| v2 | breakout_8 | 8928.08 | -1071.92 | 중단: 손실 한도 / buy / partial / 직전 완료 봉 목표 비중 100%; 다음 봉 시가 가정 |
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
| v2 | cmf_20_accumulation | 9325.48 | -674.52 | buy / partial / Chaikin Money Flow20 > 0.1; 조건 충족; CMF20=0.115503, volume20=1.66288e+06; 직전 완료 봉 목표를 다음 봉 시가에 모의 적용 |
| v2 | chaikin_3_10 | 9595.70 | -404.30 | sell / filled / ADL의 EMA3 - EMA10 > 0 그리고 종가 > EMA26; 조건 미충족; Chaikin3_10=70160.2, ADL=-1.15315e+07, close=522.39, EMA26=526.494; 직전 완료 봉 목표를 다음 봉 시가에 모의 적용 |
| v2 | roc_10_momentum | 9937.03 | -62.97 | sell / filled / 10봉 ROC > 1% 그리고 종가 > EMA26; 조건 미충족; ROC10_percent=0.771645, close=523.68, EMA26=521.367; 직전 완료 봉 목표를 다음 봉 시가에 모의 적용 |
| v2 | trix_15_trend | 9731.86 | -268.14 | sell / filled / 15봉 삼중 EMA의 1봉 변화율 TRIX > 0 그리고 종가 > EMA26; 조건 미충족; TRIX15_percent=0.0047414, close=522.39, EMA26=526.494; 직전 완료 봉 목표를 다음 봉 시가에 모의 적용 |
| v2 | keltner_20_breakout | 9817.00 | -183.00 | sell / filled / 종가 > EMA20 + 2 x Wilder ATR14; 조건 미충족; close=526.34, upper_Keltner=527.991, EMA20=526.293, ATR14=0.848911; 직전 완료 봉 목표를 다음 봉 시가에 모의 적용 |
| v2 | opening_range_30m | 9517.20 | -482.80 | sell / filled / 뉴욕 09:30·09:45 두 완료 봉 최고가를 10:00 이후 종가가 돌파; 자료 부족·변동폭 또는 거래량 없음: 대기; close=522.39; 직전 완료 봉 목표를 다음 봉 시가에 모의 적용 |

### 같은 기간의 비용·노출 비교 (사후 연구)

| 전략 | 비용 전 | 비용 후 | 100% 보유 | 같은 평균 노출 보유 | 평균 노출 |
|---|---:|---:|---:|---:|---:|
| cash | 0.00% | 0.00% | 1.98% | 0.00% | 0.00% |
| buy_hold | 2.41% | 1.98% | 1.98% | 1.98% | 100.00% |
| trend_8_26 | 2.35% | -1.45% | 1.98% | 1.22% | 62.14% |
| momentum_26 | 1.43% | -3.15% | 1.98% | 1.17% | 59.53% |
| breakout_8 | 0.31% | -16.61% | 1.98% | 0.50% | 25.33% |
| reversion_12 | 0.84% | -7.29% | 1.98% | 0.37% | 19.06% |
| volume_26 | 1.74% | -7.24% | 1.98% | 0.19% | 9.66% |
| trend_8_26 AND momentum_26 | 2.82% | -2.23% | 1.98% | 1.04% | 52.74% |
| trend_8_26 + momentum_26 | 1.89% | -2.30% | 1.98% | 1.20% | 60.84% |
| trend_8_26 AND breakout_8 | 1.39% | -10.99% | 1.98% | 0.35% | 18.02% |
| trend_8_26 + breakout_8 | 1.33% | -8.58% | 1.98% | 0.86% | 43.74% |
| trend_8_26 AND reversion_12 | 0.81% | -4.55% | 1.98% | 0.14% | 7.05% |
| trend_8_26 + reversion_12 | 1.59% | -4.22% | 1.98% | 0.80% | 40.60% |
| trend_8_26 AND volume_26 | 2.07% | -3.35% | 1.98% | 0.11% | 5.48% |
| trend_8_26 + volume_26 | 2.05% | -4.19% | 1.98% | 0.70% | 35.90% |
| momentum_26 AND breakout_8 | 0.60% | -12.79% | 1.98% | 0.40% | 20.37% |
| momentum_26 + breakout_8 | 0.88% | -10.13% | 1.98% | 0.83% | 42.44% |
| momentum_26 AND reversion_12 | 0.10% | -3.21% | 1.98% | 0.11% | 5.48% |
| momentum_26 + reversion_12 | 1.14% | -4.45% | 1.98% | 0.77% | 39.30% |
| momentum_26 AND volume_26 | 0.52% | -5.62% | 1.98% | 0.11% | 5.74% |
| momentum_26 + volume_26 | 1.59% | -4.62% | 1.98% | 0.68% | 34.60% |
| breakout_8 AND reversion_12 | 0.00% | 0.00% | 1.98% | 0.00% | 0.00% |
| breakout_8 + reversion_12 | 0.58% | -11.72% | 1.98% | 0.43% | 22.20% |
| breakout_8 AND volume_26 | 0.28% | -3.44% | 1.98% | 0.07% | 3.39% |
| breakout_8 + volume_26 | 1.03% | -11.13% | 1.98% | 0.34% | 17.50% |
| reversion_12 AND volume_26 | 1.21% | -2.13% | 1.98% | 0.05% | 2.35% |
| reversion_12 + volume_26 | 1.29% | -6.88% | 1.98% | 0.28% | 14.37% |
| ema_12_26 | 1.22% | -0.88% | 1.98% | 1.19% | 60.57% |
| macd_12_26_9 | 2.44% | -1.77% | 1.98% | 0.62% | 31.85% |
| rsi_14_recovery | 0.39% | -0.86% | 1.98% | 0.02% | 0.78% |
| bollinger_20_reentry | 0.60% | -2.72% | 1.98% | 0.04% | 2.09% |
| donchian_20 | 0.32% | -7.76% | 1.98% | 0.21% | 10.97% |
| atr_14_breakout | -0.20% | -8.63% | 1.98% | 0.13% | 6.53% |
| session_vwap | 1.22% | -6.54% | 1.98% | 1.25% | 63.45% |
| obv_20 | 1.83% | -5.58% | 1.98% | 0.89% | 45.17% |
| stochastic_14_3_recovery | 1.62% | -9.28% | 1.98% | 0.14% | 7.05% |
| mfi_14_recovery | 0.37% | -2.95% | 1.98% | 0.04% | 2.09% |
| adx_14_trend | 0.37% | -3.35% | 1.98% | 0.64% | 32.64% |
| aroon_25_trend | 1.75% | -2.02% | 1.98% | 0.54% | 27.42% |
| cci_20_momentum | 2.05% | -4.58% | 1.98% | 0.55% | 27.94% |
| williams_14_recovery | 1.56% | -6.23% | 1.98% | 0.10% | 4.96% |
| cmf_20_accumulation | -0.03% | -9.23% | 1.98% | 0.91% | 46.48% |
| chaikin_3_10 | 1.04% | -8.26% | 1.98% | 1.01% | 51.44% |
| roc_10_momentum | -0.07% | -0.90% | 1.98% | 0.04% | 2.09% |
| trix_15_trend | 0.80% | -2.94% | 1.98% | 1.07% | 54.31% |
| keltner_20_breakout | 1.05% | -6.31% | 1.98% | 0.39% | 19.84% |
| opening_range_30m | 1.10% | -6.66% | 1.98% | 0.64% | 32.64% |

동일 구간·초기 자금, 종료 시 청산 비용 포함. 노출 맞춤은 사후 설명용이며 v2 실제 계좌 성과가 아닙니다.
[낙폭 분해·비용 영향·전체 구간](DIA/comparison.json)

[v1 전체 기록](DIA/accounts.json) · [v2 전체 기록](DIA/accounts-v2.json)

## MSFT 계좌

| 모델 | 전략 | 평가액 USD | 손익 USD | 최근 매매·이유 |
|---|---|---:|---:|---|
| v1 | cash | 10000.00 | 0.00 | 대기 /  / 새 신호 대기 |
| v1 | buy_hold | 9666.00 | -334.00 | buy /  / buy_hold: prior completed bar target 100%; next bar open simulation |
| v1 | trend_8_26 | 9404.15 | -595.85 | buy /  / trend_8_26: prior completed bar target 100%; next bar open simulation |
| v1 | momentum_26 | 9195.45 | -804.55 | buy /  / momentum_26: prior completed bar target 100%; next bar open simulation |
| v1 | breakout_8 | 9454.11 | -545.89 | sell /  / breakout_8: prior completed bar target 0%; next bar open simulation |
| v1 | reversion_12 | 9238.90 | -761.10 | buy /  / reversion_12: prior completed bar target 100%; next bar open simulation |
| v1 | volume_26 | 9589.18 | -410.82 | buy /  / volume_26: prior completed bar target 100%; next bar open simulation |
| v1 | trend_8_26 AND momentum_26 | 9332.99 | -667.01 | buy /  / trend_8_26 AND momentum_26: prior completed bar target 100%; next bar open simulation |
| v1 | trend_8_26 + momentum_26 | 9336.50 | -663.50 | buy /  / trend_8_26 + momentum_26: prior completed bar target 100%; next bar open simulation |
| v1 | trend_8_26 AND breakout_8 | 9678.51 | -321.49 | sell /  / trend_8_26 AND breakout_8: prior completed bar target 0%; next bar open simulation |
| v1 | trend_8_26 + breakout_8 | 9467.05 | -532.95 | buy /  / trend_8_26 + breakout_8: prior completed bar target 50%; next bar open simulation |
| v1 | trend_8_26 AND reversion_12 | 9471.71 | -528.29 | buy /  / trend_8_26 AND reversion_12: prior completed bar target 100%; next bar open simulation |
| v1 | trend_8_26 + reversion_12 | 9339.71 | -660.29 | buy /  / trend_8_26 + reversion_12: prior completed bar target 100%; next bar open simulation |
| v1 | trend_8_26 AND volume_26 | 9767.47 | -232.53 | buy /  / trend_8_26 AND volume_26: prior completed bar target 100%; next bar open simulation |
| v1 | trend_8_26 + volume_26 | 9496.30 | -503.70 | buy /  / trend_8_26 + volume_26: prior completed bar target 100%; next bar open simulation |
| v1 | momentum_26 AND breakout_8 | 9642.25 | -357.75 | sell /  / momentum_26 AND breakout_8: prior completed bar target 0%; next bar open simulation |
| v1 | momentum_26 + breakout_8 | 9342.67 | -657.33 | buy /  / momentum_26 + breakout_8: prior completed bar target 50%; next bar open simulation |
| v1 | momentum_26 AND reversion_12 | 9601.47 | -398.53 | buy /  / momentum_26 AND reversion_12: prior completed bar target 100%; next bar open simulation |
| v1 | momentum_26 + reversion_12 | 9272.45 | -727.55 | buy /  / momentum_26 + reversion_12: prior completed bar target 100%; next bar open simulation |
| v1 | momentum_26 AND volume_26 | 9814.83 | -185.17 | buy /  / momentum_26 AND volume_26: prior completed bar target 100%; next bar open simulation |
| v1 | momentum_26 + volume_26 | 9428.05 | -571.95 | buy /  / momentum_26 + volume_26: prior completed bar target 100%; next bar open simulation |
| v1 | breakout_8 AND reversion_12 | 10000.00 | 0.00 | 대기 /  / 새 신호 대기 |
| v1 | breakout_8 + reversion_12 | 9383.14 | -616.86 | buy /  / breakout_8 + reversion_12: prior completed bar target 50%; next bar open simulation |
| v1 | breakout_8 AND volume_26 | 9953.19 | -46.81 | sell /  / breakout_8 AND volume_26: prior completed bar target 0%; next bar open simulation |
| v1 | breakout_8 + volume_26 | 9559.35 | -440.65 | buy /  / breakout_8 + volume_26: prior completed bar target 50%; next bar open simulation |
| v1 | reversion_12 AND volume_26 | 9755.16 | -244.84 | buy /  / reversion_12 AND volume_26: prior completed bar target 100%; next bar open simulation |
| v1 | reversion_12 + volume_26 | 9431.17 | -568.83 | buy /  / reversion_12 + volume_26: prior completed bar target 100%; next bar open simulation |
| v1 | ema_12_26 | 9448.58 | -551.42 | buy /  / EMA12 > EMA26; 조건 충족; EMA12=524.345, EMA26=524.284 |
| v1 | macd_12_26_9 | 9560.58 | -439.42 | buy /  / MACD > 신호선 그리고 MACD > 0; 조건 충족; MACD=0.0602049, signal9=-0.410679 |
| v1 | rsi_14_recovery | 9839.66 | -160.34 | sell /  / 직전 RSI14 < 30, 현재 RSI14 >= 30 (한 봉 목표); 조건 미충족; RSI14=49.0008, previous_RSI14=38.029 |
| v1 | bollinger_20_reentry | 9745.81 | -254.19 | sell /  / 직전 종가 < 직전 하단밴드, 현재 하단밴드 <= 종가 <= SMA20 (한 봉 목표); 조건 미충족; close=523.535, lower20=518.78, SMA20=523.154, previous_lower20=518.792 |
| v1 | donchian_20 | 9912.16 | -87.84 | sell /  / 종가 > 현재 봉을 제외한 직전 20봉 최고가; 조건 미충족; close=534.52, prior_high20=535.44 |
| v1 | atr_14_breakout | 9915.10 | -84.90 | sell /  / 종가 > 직전 종가 + 직전 ATR14 그리고 종가 > EMA26; 조건 미충족; close=533.975, threshold=536.307, prior_ATR14=2.16203, EMA26=530.521 |
| v1 | session_vwap | 9625.80 | -374.20 | buy /  / 종가 > 뉴욕 거래일별 누적 전형가격 VWAP; 조건 충족; close=520.51, session_VWAP=518.805, session_volume=2.29852e+06 |
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
| v1 | opening_range_30m | 9596.89 | -403.11 | buy /  / 뉴욕 09:30·09:45 두 완료 봉 최고가를 10:00 이후 종가가 돌파; 조건 충족; close=523.535, opening_high=522.36 |
| v2 | cash | 10000.00 | 0.00 | 대기 /  / 새 신호 대기 |
| v2 | buy_hold | 9718.74 | -281.26 | buy / partial / 직전 완료 봉 목표 비중 100%; 다음 봉 시가 가정 |
| v2 | trend_8_26 | 9337.00 | -663.00 | buy / partial / 직전 완료 봉 목표 비중 100%; 다음 봉 시가 가정 |
| v2 | momentum_26 | 9219.86 | -780.14 | buy / partial / 직전 완료 봉 목표 비중 100%; 다음 봉 시가 가정 |
| v2 | breakout_8 | 9238.63 | -761.37 | sell / filled / 직전 완료 봉 목표 비중 0%; 다음 봉 시가 가정 |
| v2 | reversion_12 | 9018.07 | -981.93 | 중단: 손실 한도 / buy / partial / 직전 완료 봉 목표 비중 100%; 다음 봉 시가 가정 |
| v2 | volume_26 | 9269.18 | -730.82 | buy / partial / 직전 완료 봉 목표 비중 100%; 다음 봉 시가 가정 |
| v2 | trend_8_26 AND momentum_26 | 9222.02 | -777.98 | buy / partial / 직전 완료 봉 목표 비중 100%; 다음 봉 시가 가정 |
| v2 | trend_8_26 + momentum_26 | 9317.55 | -682.45 | buy / partial / 직전 완료 봉 목표 비중 100%; 다음 봉 시가 가정 |
| v2 | trend_8_26 AND breakout_8 | 9318.21 | -681.79 | sell / filled / 직전 완료 봉 목표 비중 0%; 다음 봉 시가 가정 |
| v2 | trend_8_26 + breakout_8 | 9346.72 | -653.28 | buy / filled / 직전 완료 봉 목표 비중 50%; 다음 봉 시가 가정 |
| v2 | trend_8_26 AND reversion_12 | 9361.17 | -638.83 | buy / partial / 직전 완료 봉 목표 비중 100%; 다음 봉 시가 가정 |
| v2 | trend_8_26 + reversion_12 | 9115.38 | -884.62 | buy / partial / 직전 완료 봉 목표 비중 100%; 다음 봉 시가 가정 |
| v2 | trend_8_26 AND volume_26 | 9706.65 | -293.35 | buy / partial / 직전 완료 봉 목표 비중 100%; 다음 봉 시가 가정 |
| v2 | trend_8_26 + volume_26 | 9322.46 | -677.54 | buy / partial / 직전 완료 봉 목표 비중 100%; 다음 봉 시가 가정 |
| v2 | momentum_26 AND breakout_8 | 9430.77 | -569.23 | sell / filled / 직전 완료 봉 목표 비중 0%; 다음 봉 시가 가정 |
| v2 | momentum_26 + breakout_8 | 9248.81 | -751.19 | buy / filled / 직전 완료 봉 목표 비중 50%; 다음 봉 시가 가정 |
| v2 | momentum_26 AND reversion_12 | 9424.88 | -575.12 | buy / partial / 직전 완료 봉 목표 비중 100%; 다음 봉 시가 가정 |
| v2 | momentum_26 + reversion_12 | 9096.19 | -903.81 | buy / partial / 직전 완료 봉 목표 비중 100%; 다음 봉 시가 가정 |
| v2 | momentum_26 AND volume_26 | 9679.76 | -320.24 | buy / partial / 직전 완료 봉 목표 비중 100%; 다음 봉 시가 가정 |
| v2 | momentum_26 + volume_26 | 9302.99 | -697.01 | buy / partial / 직전 완료 봉 목표 비중 100%; 다음 봉 시가 가정 |
| v2 | breakout_8 AND reversion_12 | 10000.00 | 0.00 | 대기 /  / 새 신호 대기 |
| v2 | breakout_8 + reversion_12 | 9105.39 | -894.61 | buy / filled / 직전 완료 봉 목표 비중 50%; 다음 봉 시가 가정 |
| v2 | breakout_8 AND volume_26 | 9890.09 | -109.91 | sell / filled / 직전 완료 봉 목표 비중 0%; 다음 봉 시가 가정 |
| v2 | breakout_8 + volume_26 | 9312.17 | -687.83 | buy / filled / 직전 완료 봉 목표 비중 50%; 다음 봉 시가 가정 |
| v2 | reversion_12 AND volume_26 | 9512.56 | -487.44 | buy / partial / 직전 완료 봉 목표 비중 100%; 다음 봉 시가 가정 |
| v2 | reversion_12 + volume_26 | 9082.39 | -917.61 | buy / partial / 직전 완료 봉 목표 비중 100%; 다음 봉 시가 가정 |
| v2 | ema_12_26 | 9440.08 | -559.92 | buy / partial / EMA12 > EMA26; 조건 충족; EMA12=524.345, EMA26=524.284; 직전 완료 봉 목표를 다음 봉 시가에 모의 적용 |
| v2 | macd_12_26_9 | 9550.07 | -449.93 | buy / partial / MACD > 신호선 그리고 MACD > 0; 조건 충족; MACD=0.0602049, signal9=-0.410679; 직전 완료 봉 목표를 다음 봉 시가에 모의 적용 |
| v2 | rsi_14_recovery | 9825.89 | -174.11 | sell / filled / 직전 RSI14 < 30, 현재 RSI14 >= 30 (한 봉 목표); 조건 미충족; RSI14=49.0008, previous_RSI14=38.029; 직전 완료 봉 목표를 다음 봉 시가에 모의 적용 |
| v2 | bollinger_20_reentry | 9732.18 | -267.82 | sell / filled / 직전 종가 < 직전 하단밴드, 현재 하단밴드 <= 종가 <= SMA20 (한 봉 목표); 조건 미충족; close=523.535, lower20=518.78, SMA20=523.154, previous_lower20=518.792; 직전 완료 봉 목표를 다음 봉 시가에 모의 적용 |
| v2 | donchian_20 | 9908.19 | -91.81 | sell / filled / 종가 > 현재 봉을 제외한 직전 20봉 최고가; 조건 미충족; close=534.52, prior_high20=535.44; 직전 완료 봉 목표를 다음 봉 시가에 모의 적용 |
| v2 | atr_14_breakout | 9911.14 | -88.86 | sell / filled / 종가 > 직전 종가 + 직전 ATR14 그리고 종가 > EMA26; 조건 미충족; close=533.975, threshold=536.307, prior_ATR14=2.16203, EMA26=530.521; 직전 완료 봉 목표를 다음 봉 시가에 모의 적용 |
| v2 | session_vwap | 9609.46 | -390.54 | buy / partial / 종가 > 뉴욕 거래일별 누적 전형가격 VWAP; 조건 충족; close=520.51, session_VWAP=518.805, session_volume=2.29852e+06; 직전 완료 봉 목표를 다음 봉 시가에 모의 적용 |
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
| v2 | opening_range_30m | 9588.26 | -411.74 | buy / partial / 뉴욕 09:30·09:45 두 완료 봉 최고가를 10:00 이후 종가가 돌파; 조건 충족; close=523.535, opening_high=522.36; 직전 완료 봉 목표를 다음 봉 시가에 모의 적용 |

### 같은 기간의 비용·노출 비교 (사후 연구)

| 전략 | 비용 전 | 비용 후 | 100% 보유 | 같은 평균 노출 보유 | 평균 노출 |
|---|---:|---:|---:|---:|---:|
| cash | 0.00% | 0.00% | -0.79% | -0.00% | 0.00% |
| buy_hold | -0.37% | -0.79% | -0.79% | -0.79% | 100.00% |
| trend_8_26 | -2.88% | -6.48% | -0.79% | -0.45% | 56.92% |
| momentum_26 | -2.19% | -9.31% | -0.79% | -0.43% | 54.83% |
| breakout_8 | 3.75% | -10.06% | -0.79% | -0.15% | 18.80% |
| reversion_12 | -5.53% | -14.94% | -0.79% | -0.21% | 26.63% |
| volume_26 | -0.45% | -9.62% | -0.79% | -0.07% | 8.88% |
| trend_8_26 AND momentum_26 | -2.39% | -8.74% | -0.79% | -0.39% | 49.61% |
| trend_8_26 + momentum_26 | -2.53% | -7.51% | -0.79% | -0.44% | 55.88% |
| trend_8_26 AND breakout_8 | -1.14% | -10.62% | -0.79% | -0.09% | 11.23% |
| trend_8_26 + breakout_8 | 0.39% | -7.70% | -0.79% | -0.30% | 37.86% |
| trend_8_26 AND reversion_12 | -2.25% | -8.60% | -0.79% | -0.06% | 7.57% |
| trend_8_26 + reversion_12 | -4.20% | -10.63% | -0.79% | -0.33% | 41.78% |
| trend_8_26 AND volume_26 | 0.71% | -3.03% | -0.79% | -0.02% | 2.87% |
| trend_8_26 + volume_26 | -1.66% | -7.68% | -0.79% | -0.26% | 32.90% |
| momentum_26 AND breakout_8 | -0.01% | -9.98% | -0.79% | -0.09% | 12.01% |
| momentum_26 + breakout_8 | 0.75% | -9.30% | -0.79% | -0.29% | 36.82% |
| momentum_26 AND reversion_12 | -2.95% | -8.88% | -0.79% | -0.07% | 8.36% |
| momentum_26 + reversion_12 | -3.86% | -11.62% | -0.79% | -0.32% | 40.74% |
| momentum_26 AND volume_26 | -0.29% | -4.39% | -0.79% | -0.02% | 3.13% |
| momentum_26 + volume_26 | -1.31% | -8.70% | -0.79% | -0.25% | 31.86% |
| breakout_8 AND reversion_12 | 0.00% | 0.00% | -0.79% | -0.00% | 0.00% |
| breakout_8 + reversion_12 | -0.98% | -11.80% | -0.79% | -0.18% | 22.72% |
| breakout_8 AND volume_26 | 0.08% | -1.59% | -0.79% | -0.01% | 1.31% |
| breakout_8 + volume_26 | 1.64% | -9.08% | -0.79% | -0.11% | 13.85% |
| reversion_12 AND volume_26 | -2.48% | -6.89% | -0.79% | -0.03% | 4.18% |
| reversion_12 + volume_26 | -3.01% | -12.14% | -0.79% | -0.14% | 17.76% |
| ema_12_26 | -2.53% | -5.75% | -0.79% | -0.44% | 55.61% |
| macd_12_26_9 | -2.60% | -7.77% | -0.79% | -0.26% | 33.16% |
| rsi_14_recovery | 0.73% | -3.42% | -0.79% | -0.02% | 2.61% |
| bollinger_20_reentry | -0.23% | -4.34% | -0.79% | -0.02% | 2.61% |
| donchian_20 | -0.08% | -4.60% | -0.79% | -0.03% | 3.39% |
| atr_14_breakout | 0.48% | -3.25% | -0.79% | -0.02% | 2.35% |
| session_vwap | 4.21% | -4.58% | -0.79% | -0.40% | 51.44% |
| obv_20 | 3.00% | -4.90% | -0.79% | -0.38% | 48.83% |
| stochastic_14_3_recovery | -0.05% | -9.25% | -0.79% | -0.05% | 6.01% |
| mfi_14_recovery | 1.71% | -2.47% | -0.79% | -0.02% | 2.61% |
| adx_14_trend | 4.03% | 1.87% | -0.79% | -0.34% | 43.34% |
| aroon_25_trend | -1.30% | -5.75% | -0.79% | -0.17% | 21.93% |
| cci_20_momentum | 2.09% | -4.14% | -0.79% | -0.16% | 19.84% |
| williams_14_recovery | -0.66% | -9.04% | -0.79% | -0.04% | 5.48% |
| cmf_20_accumulation | -0.28% | -7.15% | -0.79% | -0.34% | 43.60% |
| chaikin_3_10 | 1.40% | -6.77% | -0.79% | -0.39% | 49.09% |
| roc_10_momentum | 0.40% | -3.73% | -0.79% | -0.10% | 12.79% |
| trix_15_trend | -0.08% | -3.79% | -0.79% | -0.34% | 42.82% |
| keltner_20_breakout | -0.31% | -5.21% | -0.79% | -0.08% | 10.70% |
| opening_range_30m | -1.11% | -5.18% | -0.79% | -0.20% | 25.59% |

동일 구간·초기 자금, 종료 시 청산 비용 포함. 노출 맞춤은 사후 설명용이며 v2 실제 계좌 성과가 아닙니다.
[낙폭 분해·비용 영향·전체 구간](MSFT/comparison.json)

[v1 전체 기록](MSFT/accounts.json) · [v2 전체 기록](MSFT/accounts-v2.json)

## JPM 계좌

| 모델 | 전략 | 평가액 USD | 손익 USD | 최근 매매·이유 |
|---|---|---:|---:|---|
| v1 | cash | 10000.00 | 0.00 | 대기 /  / 새 신호 대기 |
| v1 | buy_hold | 9744.42 | -255.58 | buy /  / buy_hold: prior completed bar target 100%; next bar open simulation |
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
| v1 | cmf_20_accumulation | 9634.29 | -365.71 | buy /  / Chaikin Money Flow20 > 0.1; 조건 충족; CMF20=0.115539, volume20=2.04147e+06 |
| v1 | chaikin_3_10 | 9553.87 | -446.13 | sell /  / ADL의 EMA3 - EMA10 > 0 그리고 종가 > EMA26; 조건 미충족; Chaikin3_10=268702, ADL=-8.90187e+06, close=332.6, EMA26=334.725 |
| v1 | roc_10_momentum | 9836.40 | -163.60 | sell /  / 10봉 ROC > 1% 그리고 종가 > EMA26; 조건 미충족; ROC10_percent=0.964142, close=337.72, EMA26=336.695 |
| v1 | trix_15_trend | 9614.50 | -385.50 | sell /  / 15봉 삼중 EMA의 1봉 변화율 TRIX > 0 그리고 종가 > EMA26; 조건 미충족; TRIX15_percent=0.00517218, close=332.6, EMA26=334.725 |
| v1 | keltner_20_breakout | 9905.24 | -94.76 | sell /  / 종가 > EMA20 + 2 x Wilder ATR14; 조건 미충족; close=339.04, upper_Keltner=339.281, EMA20=336.559, ATR14=1.36146 |
| v1 | opening_range_30m | 9795.03 | -204.97 | sell /  / 뉴욕 09:30·09:45 두 완료 봉 최고가를 10:00 이후 종가가 돌파; 자료 부족·변동폭 또는 거래량 없음: 대기; close=332.6 |
| v2 | cash | 10000.00 | 0.00 | 대기 /  / 새 신호 대기 |
| v2 | buy_hold | 9907.24 | -92.76 | buy / partial / 직전 완료 봉 목표 비중 100%; 다음 봉 시가 가정 |
| v2 | trend_8_26 | 9573.52 | -426.48 | sell / filled / 직전 완료 봉 목표 비중 0%; 다음 봉 시가 가정 |
| v2 | momentum_26 | 9055.84 | -944.16 | 중단: 손실 한도 / buy / partial / 직전 완료 봉 목표 비중 100%; 다음 봉 시가 가정 |
| v2 | breakout_8 | 8925.87 | -1074.13 | 중단: 손실 한도 / buy / partial / 직전 완료 봉 목표 비중 100%; 다음 봉 시가 가정 |
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
| v2 | momentum_26 AND breakout_8 | 8878.40 | -1121.60 | 중단: 손실 한도 / buy / partial / 직전 완료 봉 목표 비중 100%; 다음 봉 시가 가정 |
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
| v2 | cmf_20_accumulation | 9623.70 | -376.30 | buy / partial / Chaikin Money Flow20 > 0.1; 조건 충족; CMF20=0.115539, volume20=2.04147e+06; 직전 완료 봉 목표를 다음 봉 시가에 모의 적용 |
| v2 | chaikin_3_10 | 9536.68 | -463.32 | sell / filled / ADL의 EMA3 - EMA10 > 0 그리고 종가 > EMA26; 조건 미충족; Chaikin3_10=268702, ADL=-8.90187e+06, close=332.6, EMA26=334.725; 직전 완료 봉 목표를 다음 봉 시가에 모의 적용 |
| v2 | roc_10_momentum | 9832.47 | -167.53 | sell / filled / 10봉 ROC > 1% 그리고 종가 > EMA26; 조건 미충족; ROC10_percent=0.964142, close=337.72, EMA26=336.695; 직전 완료 봉 목표를 다음 봉 시가에 모의 적용 |
| v2 | trix_15_trend | 9604.89 | -395.11 | sell / filled / 15봉 삼중 EMA의 1봉 변화율 TRIX > 0 그리고 종가 > EMA26; 조건 미충족; TRIX15_percent=0.00517218, close=332.6, EMA26=334.725; 직전 완료 봉 목표를 다음 봉 시가에 모의 적용 |
| v2 | keltner_20_breakout | 9901.28 | -98.72 | sell / filled / 종가 > EMA20 + 2 x Wilder ATR14; 조건 미충족; close=339.04, upper_Keltner=339.281, EMA20=336.559, ATR14=1.36146; 직전 완료 봉 목표를 다음 봉 시가에 모의 적용 |
| v2 | opening_range_30m | 9789.16 | -210.84 | sell / filled / 뉴욕 09:30·09:45 두 완료 봉 최고가를 10:00 이후 종가가 돌파; 자료 부족·변동폭 또는 거래량 없음: 대기; close=332.6; 직전 완료 봉 목표를 다음 봉 시가에 모의 적용 |

### 같은 기간의 비용·노출 비교 (사후 연구)

| 전략 | 비용 전 | 비용 후 | 100% 보유 | 같은 평균 노출 보유 | 평균 노출 |
|---|---:|---:|---:|---:|---:|
| cash | 0.00% | 0.00% | -0.55% | -0.00% | 0.00% |
| buy_hold | -0.13% | -0.55% | -0.55% | -0.55% | 100.00% |
| trend_8_26 | -0.60% | -4.68% | -0.55% | -0.30% | 53.52% |
| momentum_26 | -4.62% | -13.76% | -0.55% | -0.29% | 52.74% |
| breakout_8 | -3.66% | -18.90% | -0.55% | -0.10% | 18.54% |
| reversion_12 | 6.10% | -8.40% | -0.55% | -0.13% | 24.28% |
| volume_26 | 1.66% | -4.54% | -0.55% | -0.03% | 6.27% |
| trend_8_26 AND momentum_26 | -0.41% | -6.49% | -0.55% | -0.23% | 41.25% |
| trend_8_26 + momentum_26 | -2.62% | -9.14% | -0.55% | -0.29% | 53.14% |
| trend_8_26 AND breakout_8 | -3.16% | -13.54% | -0.55% | -0.06% | 11.49% |
| trend_8_26 + breakout_8 | -2.12% | -11.51% | -0.55% | -0.20% | 36.04% |
| trend_8_26 AND reversion_12 | 1.24% | -4.95% | -0.55% | -0.04% | 7.83% |
| trend_8_26 + reversion_12 | 2.72% | -6.17% | -0.55% | -0.21% | 38.91% |
| trend_8_26 AND volume_26 | 0.99% | -2.35% | -0.55% | -0.02% | 3.92% |
| trend_8_26 + volume_26 | 0.55% | -4.61% | -0.55% | -0.16% | 29.90% |
| momentum_26 AND breakout_8 | -3.71% | -15.46% | -0.55% | -0.07% | 12.53% |
| momentum_26 + breakout_8 | -4.11% | -16.18% | -0.55% | -0.20% | 35.65% |
| momentum_26 AND reversion_12 | 1.94% | -4.68% | -0.55% | -0.04% | 6.53% |
| momentum_26 + reversion_12 | 0.63% | -8.66% | -0.55% | -0.21% | 38.52% |
| momentum_26 AND volume_26 | -0.68% | -3.96% | -0.55% | -0.02% | 3.13% |
| momentum_26 + volume_26 | -1.50% | -8.69% | -0.55% | -0.16% | 29.51% |
| breakout_8 AND reversion_12 | 0.00% | 0.00% | -0.55% | -0.00% | 0.00% |
| breakout_8 + reversion_12 | 1.12% | -12.53% | -0.55% | -0.12% | 21.42% |
| breakout_8 AND volume_26 | 0.94% | -1.16% | -0.55% | -0.01% | 1.31% |
| breakout_8 + volume_26 | -1.02% | -11.08% | -0.55% | -0.07% | 12.41% |
| reversion_12 AND volume_26 | 1.89% | -1.06% | -0.55% | -0.01% | 2.35% |
| reversion_12 + volume_26 | 3.87% | -5.51% | -0.55% | -0.08% | 15.28% |
| ema_12_26 | -1.85% | -5.89% | -0.55% | -0.28% | 50.13% |
| macd_12_26_9 | -1.79% | -7.01% | -0.55% | -0.18% | 32.11% |
| rsi_14_recovery | 0.40% | -0.86% | -0.55% | -0.00% | 0.78% |
| bollinger_20_reentry | 1.01% | -3.15% | -0.55% | -0.01% | 2.61% |
| donchian_20 | -2.16% | -5.78% | -0.55% | -0.02% | 3.13% |
| atr_14_breakout | -1.11% | -9.08% | -0.55% | -0.03% | 5.48% |
| session_vwap | -0.03% | -10.75% | -0.55% | -0.28% | 50.91% |
| obv_20 | -3.83% | -15.93% | -0.55% | -0.16% | 28.20% |
| stochastic_14_3_recovery | 0.40% | -9.99% | -0.55% | -0.04% | 6.79% |
| mfi_14_recovery | 0.12% | -1.13% | -0.55% | -0.00% | 0.78% |
| adx_14_trend | -2.34% | -4.37% | -0.55% | -0.14% | 24.80% |
| aroon_25_trend | -1.01% | -4.68% | -0.55% | -0.10% | 18.02% |
| cci_20_momentum | -3.21% | -11.38% | -0.55% | -0.09% | 16.45% |
| williams_14_recovery | -0.13% | -9.71% | -0.55% | -0.03% | 6.27% |
| cmf_20_accumulation | -2.68% | -10.14% | -0.55% | -0.20% | 36.81% |
| chaikin_3_10 | 1.13% | -8.18% | -0.55% | -0.19% | 33.68% |
| roc_10_momentum | -1.40% | -3.86% | -0.55% | -0.04% | 6.53% |
| trix_15_trend | -0.93% | -7.75% | -0.55% | -0.19% | 34.99% |
| keltner_20_breakout | -0.35% | -2.83% | -0.55% | -0.02% | 3.92% |
| opening_range_30m | -0.69% | -4.38% | -0.55% | -0.09% | 16.97% |

동일 구간·초기 자금, 종료 시 청산 비용 포함. 노출 맞춤은 사후 설명용이며 v2 실제 계좌 성과가 아닙니다.
[낙폭 분해·비용 영향·전체 구간](JPM/comparison.json)

[v1 전체 기록](JPM/accounts.json) · [v2 전체 기록](JPM/accounts-v2.json)

## XOM 계좌

| 모델 | 전략 | 평가액 USD | 손익 USD | 최근 매매·이유 |
|---|---|---:|---:|---|
| v1 | cash | 10000.00 | 0.00 | 대기 /  / 새 신호 대기 |
| v1 | buy_hold | 10337.71 | 337.71 | buy /  / buy_hold: prior completed bar target 100%; next bar open simulation |
| v1 | trend_8_26 | 9986.50 | -13.50 | buy /  / trend_8_26: prior completed bar target 100%; next bar open simulation |
| v1 | momentum_26 | 9980.22 | -19.78 | buy /  / momentum_26: prior completed bar target 100%; next bar open simulation |
| v1 | breakout_8 | 9481.80 | -518.20 | sell /  / breakout_8: prior completed bar target 0%; next bar open simulation |
| v1 | reversion_12 | 9517.47 | -482.53 | sell /  / reversion_12: prior completed bar target 0%; next bar open simulation |
| v1 | volume_26 | 9554.35 | -445.65 | sell /  / volume_26: prior completed bar target 0%; next bar open simulation |
| v1 | trend_8_26 AND momentum_26 | 9848.16 | -151.84 | buy /  / trend_8_26 AND momentum_26: prior completed bar target 100%; next bar open simulation |
| v1 | trend_8_26 + momentum_26 | 9983.63 | -16.37 | buy /  / trend_8_26 + momentum_26: prior completed bar target 100%; next bar open simulation |
| v1 | trend_8_26 AND breakout_8 | 9693.28 | -306.72 | sell /  / trend_8_26 AND breakout_8: prior completed bar target 0%; next bar open simulation |
| v1 | trend_8_26 + breakout_8 | 9770.54 | -229.46 | sell /  / trend_8_26 + breakout_8: prior completed bar target 50%; next bar open simulation |
| v1 | trend_8_26 AND reversion_12 | 9545.50 | -454.50 | sell /  / trend_8_26 AND reversion_12: prior completed bar target 0%; next bar open simulation |
| v1 | trend_8_26 + reversion_12 | 9749.29 | -250.71 | sell /  / trend_8_26 + reversion_12: prior completed bar target 50%; next bar open simulation |
| v1 | trend_8_26 AND volume_26 | 9669.14 | -330.86 | sell /  / trend_8_26 AND volume_26: prior completed bar target 0%; next bar open simulation |
| v1 | trend_8_26 + volume_26 | 9768.54 | -231.46 | sell /  / trend_8_26 + volume_26: prior completed bar target 50%; next bar open simulation |
| v1 | momentum_26 AND breakout_8 | 9813.21 | -186.79 | sell /  / momentum_26 AND breakout_8: prior completed bar target 0%; next bar open simulation |
| v1 | momentum_26 + breakout_8 | 9728.21 | -271.79 | sell /  / momentum_26 + breakout_8: prior completed bar target 50%; next bar open simulation |
| v1 | momentum_26 AND reversion_12 | 9642.75 | -357.25 | sell /  / momentum_26 AND reversion_12: prior completed bar target 0%; next bar open simulation |
| v1 | momentum_26 + reversion_12 | 9746.10 | -253.90 | sell /  / momentum_26 + reversion_12: prior completed bar target 50%; next bar open simulation |
| v1 | momentum_26 AND volume_26 | 9888.17 | -111.83 | sell /  / momentum_26 AND volume_26: prior completed bar target 0%; next bar open simulation |
| v1 | momentum_26 + volume_26 | 9765.15 | -234.85 | sell /  / momentum_26 + volume_26: prior completed bar target 50%; next bar open simulation |
| v1 | breakout_8 AND reversion_12 | 10000.00 | 0.00 | 대기 /  / 새 신호 대기 |
| v1 | breakout_8 + reversion_12 | 9518.57 | -481.43 | sell /  / breakout_8 + reversion_12: prior completed bar target 0%; next bar open simulation |
| v1 | breakout_8 AND volume_26 | 9896.24 | -103.76 | sell /  / breakout_8 AND volume_26: prior completed bar target 0%; next bar open simulation |
| v1 | breakout_8 + volume_26 | 9517.91 | -482.09 | sell /  / breakout_8 + volume_26: prior completed bar target 0%; next bar open simulation |
| v1 | reversion_12 AND volume_26 | 9794.27 | -205.73 | sell /  / reversion_12 AND volume_26: prior completed bar target 0%; next bar open simulation |
| v1 | reversion_12 + volume_26 | 9536.04 | -463.96 | sell /  / reversion_12 + volume_26: prior completed bar target 0%; next bar open simulation |
| v1 | ema_12_26 | 10055.17 | 55.17 | buy /  / EMA12 > EMA26; 조건 충족; EMA12=176.974, EMA26=176.95 |
| v1 | macd_12_26_9 | 10047.23 | 47.23 | sell /  / MACD > 신호선 그리고 MACD > 0; 조건 미충족; MACD=1.35319, signal9=1.41024 |
| v1 | rsi_14_recovery | 9927.64 | -72.36 | sell /  / 직전 RSI14 < 30, 현재 RSI14 >= 30 (한 봉 목표); 조건 미충족; RSI14=37.639, previous_RSI14=31.1023 |
| v1 | bollinger_20_reentry | 9694.21 | -305.79 | sell /  / 직전 종가 < 직전 하단밴드, 현재 하단밴드 <= 종가 <= SMA20 (한 봉 목표); 조건 미충족; close=175.53, lower20=174.782, SMA20=177.101, previous_lower20=174.994 |
| v1 | donchian_20 | 9754.38 | -245.62 | sell /  / 종가 > 현재 봉을 제외한 직전 20봉 최고가; 조건 미충족; close=183.28, prior_high20=183.3 |
| v1 | atr_14_breakout | 9789.04 | -210.96 | sell /  / 종가 > 직전 종가 + 직전 ATR14 그리고 종가 > EMA26; 조건 미충족; close=181.355, threshold=182.652, prior_ATR14=0.727068, EMA26=178.133 |
| v1 | session_vwap | 9986.26 | -13.74 | buy /  / 종가 > 뉴욕 거래일별 누적 전형가격 VWAP; 조건 충족; close=182.5, session_VWAP=182.493, session_volume=1.26203e+07 |
| v1 | obv_20 | 9558.42 | -441.58 | buy /  / OBV > OBV의 SMA20 그리고 종가 > EMA26; 조건 충족; OBV=2.26159e+07, OBV_SMA20=2.18428e+07, close=176.86, EMA26=176.75 |
| v1 | stochastic_14_3_recovery | 9636.26 | -363.74 | sell /  / 직전 %K14 < 20에서 %K14가 %D3 상향 돌파 (한 봉 목표); 조건 미충족; K14=11.8836, D3=5.65987, previous_K14=4.66302, previous_D3=2.02546 |
| v1 | mfi_14_recovery | 10000.00 | 0.00 | 대기 /  / 새 신호 대기 |
| v1 | adx_14_trend | 10058.74 | 58.74 | buy /  / Wilder ADX14 >= 25 그리고 +DI14 > -DI14; 조건 충족; ADX14=26.2258, plus_DI14=52.4409, minus_DI14=10.4732 |
| v1 | aroon_25_trend | 9626.27 | -373.73 | sell /  / Aroon25 Up > 70 그리고 Down < 30 (동률이면 최신 극값); 조건 미충족; Aroon_up=68, Aroon_down=4 |
| v1 | cci_20_momentum | 9460.38 | -539.62 | sell /  / CCI20 > 100 (전형가격·평균절대편차); 조건 미충족; CCI20=95.1299 |
| v1 | williams_14_recovery | 9633.99 | -366.01 | buy /  / 직전 Williams %R14 < -80, 현재 >= -80 (한 봉 목표); 조건 충족; Williams_R14=-73.5295, previous_R14=-86.1764 |
| v1 | cmf_20_accumulation | 9955.27 | -44.73 | buy /  / Chaikin Money Flow20 > 0.1; 조건 충족; CMF20=0.202217, volume20=4.5047e+06 |
| v1 | chaikin_3_10 | 9917.26 | -82.74 | buy /  / ADL의 EMA3 - EMA10 > 0 그리고 종가 > EMA26; 조건 충족; Chaikin3_10=152048, ADL=2.84951e+07, close=176.86, EMA26=176.75 |
| v1 | roc_10_momentum | 9912.41 | -87.59 | sell /  / 10봉 ROC > 1% 그리고 종가 > EMA26; 조건 미충족; ROC10_percent=0.733814, close=183.26, EMA26=180.514 |
| v1 | trix_15_trend | 10005.06 | 5.06 | buy /  / 15봉 삼중 EMA의 1봉 변화율 TRIX > 0 그리고 종가 > EMA26; 조건 충족; TRIX15_percent=0.00288954, close=177.71, EMA26=177.21 |
| v1 | keltner_20_breakout | 9898.00 | -102.00 | sell /  / 종가 > EMA20 + 2 x Wilder ATR14; 조건 미충족; close=182.29, upper_Keltner=182.66, EMA20=181.48, ATR14=0.590087 |
| v1 | opening_range_30m | 9987.90 | -12.10 | buy /  / 뉴욕 09:30·09:45 두 완료 봉 최고가를 10:00 이후 종가가 돌파; 조건 충족; close=182.19, opening_high=181.96 |
| v2 | cash | 10000.00 | 0.00 | 대기 /  / 새 신호 대기 |
| v2 | buy_hold | 10667.61 | 667.61 | buy / partial / 직전 완료 봉 목표 비중 100%; 다음 봉 시가 가정 |
| v2 | trend_8_26 | 10073.56 | 73.56 | buy / partial / 직전 완료 봉 목표 비중 100%; 다음 봉 시가 가정 |
| v2 | momentum_26 | 10145.42 | 145.42 | buy / partial / 직전 완료 봉 목표 비중 100%; 다음 봉 시가 가정 |
| v2 | breakout_8 | 8988.95 | -1011.05 | 중단: 손실 한도 / sell / filled / 직전 완료 봉 목표 비중 0%; 다음 봉 시가 가정 |
| v2 | reversion_12 | 9330.25 | -669.75 | sell / filled / 직전 완료 봉 목표 비중 0%; 다음 봉 시가 가정 |
| v2 | volume_26 | 9451.35 | -548.65 | sell / filled / 직전 완료 봉 목표 비중 0%; 다음 봉 시가 가정 |
| v2 | trend_8_26 AND momentum_26 | 9939.38 | -60.62 | buy / partial / 직전 완료 봉 목표 비중 100%; 다음 봉 시가 가정 |
| v2 | trend_8_26 + momentum_26 | 10109.72 | 109.72 | buy / partial / 직전 완료 봉 목표 비중 100%; 다음 봉 시가 가정 |
| v2 | trend_8_26 AND breakout_8 | 9139.97 | -860.03 | sell / filled / 직전 완료 봉 목표 비중 0%; 다음 봉 시가 가정 |
| v2 | trend_8_26 + breakout_8 | 9554.12 | -445.88 | sell / filled / 직전 완료 봉 목표 비중 50%; 다음 봉 시가 가정 |
| v2 | trend_8_26 AND reversion_12 | 9381.23 | -618.77 | sell / filled / 직전 완료 봉 목표 비중 0%; 다음 봉 시가 가정 |
| v2 | trend_8_26 + reversion_12 | 9694.95 | -305.05 | sell / filled / 직전 완료 봉 목표 비중 50%; 다음 봉 시가 가정 |
| v2 | trend_8_26 AND volume_26 | 9556.73 | -443.27 | sell / filled / 직전 완료 봉 목표 비중 0%; 다음 봉 시가 가정 |
| v2 | trend_8_26 + volume_26 | 9757.93 | -242.07 | sell / filled / 직전 완료 봉 목표 비중 50%; 다음 봉 시가 가정 |
| v2 | momentum_26 AND breakout_8 | 9273.68 | -726.32 | sell / filled / 직전 완료 봉 목표 비중 0%; 다음 봉 시가 가정 |
| v2 | momentum_26 + breakout_8 | 9527.83 | -472.17 | sell / filled / 직전 완료 봉 목표 비중 50%; 다음 봉 시가 가정 |
| v2 | momentum_26 AND reversion_12 | 9440.57 | -559.43 | sell / filled / 직전 완료 봉 목표 비중 0%; 다음 봉 시가 가정 |
| v2 | momentum_26 + reversion_12 | 9729.38 | -270.62 | sell / filled / 직전 완료 봉 목표 비중 50%; 다음 봉 시가 가정 |
| v2 | momentum_26 AND volume_26 | 9838.73 | -161.27 | sell / filled / 직전 완료 봉 목표 비중 0%; 다음 봉 시가 가정 |
| v2 | momentum_26 + volume_26 | 9812.91 | -187.09 | sell / filled / 직전 완료 봉 목표 비중 50%; 다음 봉 시가 가정 |
| v2 | breakout_8 AND reversion_12 | 10000.00 | 0.00 | 대기 /  / 새 신호 대기 |
| v2 | breakout_8 + reversion_12 | 9155.19 | -844.81 | sell / filled / 직전 완료 봉 목표 비중 0%; 다음 봉 시가 가정 |
| v2 | breakout_8 AND volume_26 | 9860.88 | -139.12 | sell / filled / 직전 완료 봉 목표 비중 0%; 다음 봉 시가 가정 |
| v2 | breakout_8 + volume_26 | 9214.41 | -785.59 | sell / filled / 직전 완료 봉 목표 비중 0%; 다음 봉 시가 가정 |
| v2 | reversion_12 AND volume_26 | 9737.38 | -262.62 | sell / filled / 직전 완료 봉 목표 비중 0%; 다음 봉 시가 가정 |
| v2 | reversion_12 + volume_26 | 9410.50 | -589.50 | sell / filled / 직전 완료 봉 목표 비중 0%; 다음 봉 시가 가정 |
| v2 | ema_12_26 | 10048.13 | 48.13 | buy / partial / EMA12 > EMA26; 조건 충족; EMA12=176.974, EMA26=176.95; 직전 완료 봉 목표를 다음 봉 시가에 모의 적용 |
| v2 | macd_12_26_9 | 10035.18 | 35.18 | sell / filled / MACD > 신호선 그리고 MACD > 0; 조건 미충족; MACD=1.35319, signal9=1.41024; 직전 완료 봉 목표를 다음 봉 시가에 모의 적용 |
| v2 | rsi_14_recovery | 9923.67 | -76.33 | sell / filled / 직전 RSI14 < 30, 현재 RSI14 >= 30 (한 봉 목표); 조건 미충족; RSI14=37.639, previous_RSI14=31.1023; 직전 완료 봉 목표를 다음 봉 시가에 모의 적용 |
| v2 | bollinger_20_reentry | 9684.52 | -315.48 | sell / filled / 직전 종가 < 직전 하단밴드, 현재 하단밴드 <= 종가 <= SMA20 (한 봉 목표); 조건 미충족; close=175.53, lower20=174.782, SMA20=177.101, previous_lower20=174.994; 직전 완료 봉 목표를 다음 봉 시가에 모의 적용 |
| v2 | donchian_20 | 9738.78 | -261.22 | sell / filled / 종가 > 현재 봉을 제외한 직전 20봉 최고가; 조건 미충족; close=183.28, prior_high20=183.3; 직전 완료 봉 목표를 다음 봉 시가에 모의 적용 |
| v2 | atr_14_breakout | 9777.30 | -222.70 | sell / filled / 종가 > 직전 종가 + 직전 ATR14 그리고 종가 > EMA26; 조건 미충족; close=181.355, threshold=182.652, prior_ATR14=0.727068, EMA26=178.133; 직전 완료 봉 목표를 다음 봉 시가에 모의 적용 |
| v2 | session_vwap | 9967.31 | -32.69 | buy / partial / 종가 > 뉴욕 거래일별 누적 전형가격 VWAP; 조건 충족; close=182.5, session_VWAP=182.493, session_volume=1.26203e+07; 직전 완료 봉 목표를 다음 봉 시가에 모의 적용 |
| v2 | obv_20 | 9502.46 | -497.54 | 중단: 손실 한도 / sell / filled / OBV > OBV의 SMA20 그리고 종가 > EMA26; 조건 미충족; OBV=2.24329e+07, OBV_SMA20=2.30895e+07, close=177.005, EMA26=177.393; 직전 완료 봉 목표를 다음 봉 시가에 모의 적용 |
| v2 | stochastic_14_3_recovery | 9622.78 | -377.22 | sell / filled / 직전 %K14 < 20에서 %K14가 %D3 상향 돌파 (한 봉 목표); 조건 미충족; K14=11.8836, D3=5.65987, previous_K14=4.66302, previous_D3=2.02546; 직전 완료 봉 목표를 다음 봉 시가에 모의 적용 |
| v2 | mfi_14_recovery | 10000.00 | 0.00 | 대기 /  / 새 신호 대기 |
| v2 | adx_14_trend | 10051.70 | 51.70 | buy / partial / Wilder ADX14 >= 25 그리고 +DI14 > -DI14; 조건 충족; ADX14=26.2258, plus_DI14=52.4409, minus_DI14=10.4732; 직전 완료 봉 목표를 다음 봉 시가에 모의 적용 |
| v2 | aroon_25_trend | 9616.65 | -383.35 | sell / filled / Aroon25 Up > 70 그리고 Down < 30 (동률이면 최신 극값); 조건 미충족; Aroon_up=68, Aroon_down=4; 직전 완료 봉 목표를 다음 봉 시가에 모의 적용 |
| v2 | cci_20_momentum | 9435.81 | -564.19 | sell / filled / CCI20 > 100 (전형가격·평균절대편차); 조건 미충족; CCI20=95.1299; 직전 완료 봉 목표를 다음 봉 시가에 모의 적용 |
| v2 | williams_14_recovery | 9619.55 | -380.45 | buy / partial / 직전 Williams %R14 < -80, 현재 >= -80 (한 봉 목표); 조건 충족; Williams_R14=-73.5295, previous_R14=-86.1764; 직전 완료 봉 목표를 다음 봉 시가에 모의 적용 |
| v2 | cmf_20_accumulation | 9942.34 | -57.66 | buy / partial / Chaikin Money Flow20 > 0.1; 조건 충족; CMF20=0.202217, volume20=4.5047e+06; 직전 완료 봉 목표를 다음 봉 시가에 모의 적용 |
| v2 | chaikin_3_10 | 9900.42 | -99.58 | buy / partial / ADL의 EMA3 - EMA10 > 0 그리고 종가 > EMA26; 조건 충족; Chaikin3_10=152048, ADL=2.87515e+07, close=176.86, EMA26=176.75; 직전 완료 봉 목표를 다음 봉 시가에 모의 적용 |
| v2 | roc_10_momentum | 9900.52 | -99.48 | sell / filled / 10봉 ROC > 1% 그리고 종가 > EMA26; 조건 미충족; ROC10_percent=0.733814, close=183.26, EMA26=180.514; 직전 완료 봉 목표를 다음 봉 시가에 모의 적용 |
| v2 | trix_15_trend | 9992.06 | -7.94 | buy / partial / 15봉 삼중 EMA의 1봉 변화율 TRIX > 0 그리고 종가 > EMA26; 조건 충족; TRIX15_percent=0.00288954, close=177.71, EMA26=177.21; 직전 완료 봉 목표를 다음 봉 시가에 모의 적용 |
| v2 | keltner_20_breakout | 9888.11 | -111.89 | sell / filled / 종가 > EMA20 + 2 x Wilder ATR14; 조건 미충족; close=182.29, upper_Keltner=182.66, EMA20=181.48, ATR14=0.590087; 직전 완료 봉 목표를 다음 봉 시가에 모의 적용 |
| v2 | opening_range_30m | 9982.91 | -17.09 | buy / partial / 뉴욕 09:30·09:45 두 완료 봉 최고가를 10:00 이후 종가가 돌파; 조건 충족; close=182.19, opening_high=181.96; 직전 완료 봉 목표를 다음 봉 시가에 모의 적용 |

### 같은 기간의 비용·노출 비교 (사후 연구)

| 전략 | 비용 전 | 비용 후 | 100% 보유 | 같은 평균 노출 보유 | 평균 노출 |
|---|---:|---:|---:|---:|---:|
| cash | 0.00% | 0.00% | 11.79% | 0.00% | 0.00% |
| buy_hold | 12.26% | 11.79% | 11.79% | 11.79% | 100.00% |
| trend_8_26 | 5.93% | 2.00% | 11.79% | 8.23% | 71.02% |
| momentum_26 | 5.74% | 0.96% | 11.79% | 8.04% | 69.45% |
| breakout_8 | 1.60% | -15.90% | 11.79% | 3.07% | 27.15% |
| reversion_12 | 1.19% | -8.51% | 11.79% | 2.41% | 21.41% |
| volume_26 | 1.18% | -6.19% | 11.79% | 0.61% | 5.48% |
| trend_8_26 AND momentum_26 | 4.06% | -0.64% | 11.79% | 7.10% | 61.62% |
| trend_8_26 + momentum_26 | 5.84% | 1.48% | 11.79% | 8.14% | 70.24% |
| trend_8_26 AND breakout_8 | 1.72% | -12.55% | 11.79% | 2.41% | 21.41% |
| trend_8_26 + breakout_8 | 3.76% | -6.78% | 11.79% | 5.62% | 49.09% |
| trend_8_26 AND reversion_12 | -1.71% | -7.32% | 11.79% | 1.17% | 10.44% |
| trend_8_26 + reversion_12 | 3.56% | -3.20% | 11.79% | 5.28% | 46.22% |
| trend_8_26 AND volume_26 | 0.50% | -4.44% | 11.79% | 0.41% | 3.66% |
| trend_8_26 + volume_26 | 3.55% | -1.97% | 11.79% | 4.35% | 38.25% |
| momentum_26 AND breakout_8 | 1.67% | -12.60% | 11.79% | 2.50% | 22.19% |
| momentum_26 + breakout_8 | 3.67% | -7.84% | 11.79% | 5.52% | 48.31% |
| momentum_26 AND reversion_12 | 0.09% | -7.20% | 11.79% | 1.20% | 10.70% |
| momentum_26 + reversion_12 | 3.46% | -3.49% | 11.79% | 5.19% | 45.44% |
| momentum_26 AND volume_26 | 1.74% | -2.03% | 11.79% | 0.26% | 2.35% |
| momentum_26 + volume_26 | 3.46% | -2.06% | 11.79% | 4.26% | 37.47% |
| breakout_8 AND reversion_12 | 0.00% | 0.00% | 11.79% | 0.00% | 0.00% |
| breakout_8 + reversion_12 | 1.41% | -11.92% | 11.79% | 2.74% | 24.29% |
| breakout_8 AND volume_26 | 0.76% | -1.75% | 11.79% | 0.17% | 1.57% |
| breakout_8 + volume_26 | 1.40% | -10.62% | 11.79% | 1.83% | 16.33% |
| reversion_12 AND volume_26 | -0.04% | -3.35% | 11.79% | 0.26% | 2.35% |
| reversion_12 + volume_26 | 1.20% | -6.77% | 11.79% | 1.51% | 13.45% |
| ema_12_26 | 5.56% | 2.50% | 11.79% | 8.80% | 75.72% |
| macd_12_26_9 | 3.85% | -2.08% | 11.79% | 4.82% | 42.30% |
| rsi_14_recovery | 0.07% | -0.76% | 11.79% | 0.06% | 0.52% |
| bollinger_20_reentry | -1.49% | -4.34% | 11.79% | 0.20% | 1.83% |
| donchian_20 | 0.04% | -8.41% | 11.79% | 1.17% | 10.44% |
| atr_14_breakout | 0.86% | -7.27% | 11.79% | 0.64% | 5.74% |
| session_vwap | 6.05% | -5.32% | 11.79% | 7.38% | 63.97% |
| obv_20 | 3.33% | -6.97% | 11.79% | 5.80% | 50.65% |
| stochastic_14_3_recovery | 0.20% | -9.02% | 11.79% | 0.67% | 6.01% |
| mfi_14_recovery | -0.31% | -1.97% | 11.79% | 0.12% | 1.04% |
| adx_14_trend | 4.15% | 1.13% | 11.79% | 4.94% | 43.34% |
| aroon_25_trend | -1.71% | -8.10% | 11.79% | 3.88% | 34.20% |
| cci_20_momentum | 2.35% | -7.47% | 11.79% | 3.34% | 29.50% |
| williams_14_recovery | -0.96% | -7.00% | 11.79% | 0.44% | 3.92% |
| cmf_20_accumulation | 4.16% | -2.20% | 11.79% | 5.99% | 52.22% |
| chaikin_3_10 | 6.41% | -2.57% | 11.79% | 7.07% | 61.36% |
| roc_10_momentum | 1.32% | -4.87% | 11.79% | 1.70% | 15.14% |
| trix_15_trend | 5.00% | -1.00% | 11.79% | 7.13% | 61.88% |
| keltner_20_breakout | 0.94% | -5.62% | 11.79% | 2.23% | 19.84% |
| opening_range_30m | 0.36% | -6.55% | 11.79% | 3.25% | 28.72% |

동일 구간·초기 자금, 종료 시 청산 비용 포함. 노출 맞춤은 사후 설명용이며 v2 실제 계좌 성과가 아닙니다.
[낙폭 분해·비용 영향·전체 구간](XOM/comparison.json)

[v1 전체 기록](XOM/accounts.json) · [v2 전체 기록](XOM/accounts-v2.json)

## JNJ 계좌

| 모델 | 전략 | 평가액 USD | 손익 USD | 최근 매매·이유 |
|---|---|---:|---:|---|
| v1 | cash | 10000.00 | 0.00 | 대기 /  / 새 신호 대기 |
| v1 | buy_hold | 10296.40 | 296.40 | buy /  / buy_hold: prior completed bar target 100%; next bar open simulation |
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
| v2 | buy_hold | 10056.09 | 56.09 | 중단: 손실 한도 / buy / partial / 직전 완료 봉 목표 비중 100%; 다음 봉 시가 가정 |
| v2 | trend_8_26 | 10056.09 | 56.09 | 중단: 손실 한도 / buy / partial / 직전 완료 봉 목표 비중 100%; 다음 봉 시가 가정 |
| v2 | momentum_26 | 10056.09 | 56.09 | 중단: 손실 한도 / buy / partial / 직전 완료 봉 목표 비중 100%; 다음 봉 시가 가정 |
| v2 | breakout_8 | 9343.39 | -656.61 | 중단: 손실 한도 / sell / filled / 직전 완료 봉 목표 비중 0%; 다음 봉 시가 가정 |
| v2 | reversion_12 | 9295.90 | -704.10 | sell / filled / 직전 완료 봉 목표 비중 0%; 다음 봉 시가 가정 |
| v2 | volume_26 | 9819.31 | -180.69 | sell / filled / 직전 완료 봉 목표 비중 0%; 다음 봉 시가 가정 |
| v2 | trend_8_26 AND momentum_26 | 10056.09 | 56.09 | 중단: 손실 한도 / buy / partial / 직전 완료 봉 목표 비중 100%; 다음 봉 시가 가정 |
| v2 | trend_8_26 + momentum_26 | 10056.09 | 56.09 | 중단: 손실 한도 / buy / partial / 직전 완료 봉 목표 비중 100%; 다음 봉 시가 가정 |
| v2 | trend_8_26 AND breakout_8 | 9419.39 | -580.61 | 중단: 손실 한도 / sell / filled / 직전 완료 봉 목표 비중 0%; 다음 봉 시가 가정 |
| v2 | trend_8_26 + breakout_8 | 9384.04 | -615.96 | sell / filled / 직전 완료 봉 목표 비중 0%; 다음 봉 시가 가정 |
| v2 | trend_8_26 AND reversion_12 | 9775.94 | -224.06 | sell / filled / 직전 완료 봉 목표 비중 0%; 다음 봉 시가 가정 |
| v2 | trend_8_26 + reversion_12 | 9732.92 | -267.08 | 중단: 손실 한도 / sell / filled / 직전 완료 봉 목표 비중 0%; 다음 봉 시가 가정 |
| v2 | trend_8_26 AND volume_26 | 9997.51 | -2.49 | sell / filled / 직전 완료 봉 목표 비중 0%; 다음 봉 시가 가정 |
| v2 | trend_8_26 + volume_26 | 10005.00 | 5.00 | 중단: 손실 한도 / buy / filled / 직전 완료 봉 목표 비중 50%; 다음 봉 시가 가정 |
| v2 | momentum_26 AND breakout_8 | 9297.50 | -702.50 | sell / filled / 직전 완료 봉 목표 비중 0%; 다음 봉 시가 가정 |
| v2 | momentum_26 + breakout_8 | 9093.87 | -906.13 | sell / filled / 직전 완료 봉 목표 비중 0%; 다음 봉 시가 가정 |
| v2 | momentum_26 AND reversion_12 | 9637.84 | -362.16 | sell / filled / 직전 완료 봉 목표 비중 0%; 다음 봉 시가 가정 |
| v2 | momentum_26 + reversion_12 | 9732.92 | -267.08 | 중단: 손실 한도 / sell / filled / 직전 완료 봉 목표 비중 0%; 다음 봉 시가 가정 |
| v2 | momentum_26 AND volume_26 | 9920.93 | -79.07 | sell / filled / 직전 완료 봉 목표 비중 0%; 다음 봉 시가 가정 |
| v2 | momentum_26 + volume_26 | 10005.00 | 5.00 | 중단: 손실 한도 / buy / filled / 직전 완료 봉 목표 비중 50%; 다음 봉 시가 가정 |
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
| cash | 0.00% | 0.00% | 3.13% | 0.00% | 0.00% |
| buy_hold | 3.56% | 3.13% | 3.13% | 3.13% | 100.00% |
| trend_8_26 | 5.22% | 2.61% | 3.13% | 1.74% | 55.87% |
| momentum_26 | -0.46% | -4.56% | 3.13% | 1.67% | 53.52% |
| breakout_8 | 2.39% | -17.70% | 3.13% | 0.79% | 25.33% |
| reversion_12 | -4.63% | -11.57% | 3.13% | 0.68% | 21.93% |
| volume_26 | 3.01% | -2.88% | 3.13% | 0.15% | 4.96% |
| trend_8_26 AND momentum_26 | 1.18% | -1.75% | 3.13% | 1.48% | 47.52% |
| trend_8_26 + momentum_26 | 2.35% | -0.83% | 3.13% | 1.71% | 54.70% |
| trend_8_26 AND breakout_8 | 3.61% | -10.93% | 3.13% | 0.58% | 18.54% |
| trend_8_26 + breakout_8 | 3.83% | -7.89% | 3.13% | 1.26% | 40.61% |
| trend_8_26 AND reversion_12 | 0.52% | -3.21% | 3.13% | 0.20% | 6.53% |
| trend_8_26 + reversion_12 | 0.22% | -4.53% | 3.13% | 1.21% | 38.91% |
| trend_8_26 AND volume_26 | 3.25% | 0.26% | 3.13% | 0.06% | 2.09% |
| trend_8_26 + volume_26 | 4.15% | 0.05% | 3.13% | 0.95% | 30.42% |
| momentum_26 AND breakout_8 | 2.60% | -10.68% | 3.13% | 0.52% | 16.71% |
| momentum_26 + breakout_8 | 0.99% | -11.16% | 3.13% | 1.23% | 39.43% |
| momentum_26 AND reversion_12 | -1.40% | -5.46% | 3.13% | 0.23% | 7.31% |
| momentum_26 + reversion_12 | -2.54% | -7.54% | 3.13% | 1.17% | 37.73% |
| momentum_26 AND volume_26 | 0.14% | -0.70% | 3.13% | 0.02% | 0.52% |
| momentum_26 + volume_26 | 1.30% | -2.48% | 3.13% | 0.91% | 29.25% |
| breakout_8 AND reversion_12 | 0.00% | 0.00% | 3.13% | 0.00% | 0.00% |
| breakout_8 + reversion_12 | -1.16% | -14.33% | 3.13% | 0.74% | 23.64% |
| breakout_8 AND volume_26 | 1.33% | 0.06% | 3.13% | 0.03% | 1.04% |
| breakout_8 + volume_26 | 2.71% | -9.65% | 3.13% | 0.47% | 15.15% |
| reversion_12 AND volume_26 | -0.88% | -2.53% | 3.13% | 0.05% | 1.57% |
| reversion_12 + volume_26 | -0.87% | -6.93% | 3.13% | 0.42% | 13.45% |
| ema_12_26 | -0.07% | -2.97% | 3.13% | 1.72% | 55.09% |
| macd_12_26_9 | 9.10% | 5.49% | 3.13% | 1.08% | 34.73% |
| rsi_14_recovery | 0.09% | -2.40% | 3.13% | 0.05% | 1.57% |
| bollinger_20_reentry | -1.07% | -4.74% | 3.13% | 0.07% | 2.35% |
| donchian_20 | 2.07% | -7.72% | 3.13% | 0.31% | 9.92% |
| atr_14_breakout | 1.15% | -6.61% | 3.13% | 0.19% | 6.01% |
| session_vwap | 6.71% | -1.47% | 3.13% | 1.79% | 57.44% |
| obv_20 | -2.58% | -12.66% | 3.13% | 1.33% | 42.56% |
| stochastic_14_3_recovery | -0.56% | -10.09% | 3.13% | 0.19% | 6.27% |
| mfi_14_recovery | 0.80% | -1.30% | 3.13% | 0.04% | 1.31% |
| adx_14_trend | -3.32% | -8.45% | 3.13% | 1.33% | 42.82% |
| aroon_25_trend | 4.48% | 0.18% | 3.13% | 1.16% | 37.34% |
| cci_20_momentum | 4.61% | -2.19% | 3.13% | 0.77% | 24.80% |
| williams_14_recovery | -0.58% | -5.46% | 3.13% | 0.10% | 3.13% |
| cmf_20_accumulation | 6.29% | 1.49% | 3.13% | 1.31% | 42.04% |
| chaikin_3_10 | 0.06% | -5.26% | 3.13% | 1.42% | 45.43% |
| roc_10_momentum | -0.56% | -8.19% | 3.13% | 0.70% | 22.45% |
| trix_15_trend | -1.21% | -4.08% | 3.13% | 1.31% | 42.04% |
| keltner_20_breakout | 1.76% | -2.43% | 3.13% | 0.57% | 18.28% |
| opening_range_30m | 0.92% | -3.23% | 3.13% | 0.99% | 31.85% |

동일 구간·초기 자금, 종료 시 청산 비용 포함. 노출 맞춤은 사후 설명용이며 v2 실제 계좌 성과가 아닙니다.
[낙폭 분해·비용 영향·전체 구간](JNJ/comparison.json)

[v1 전체 기록](JNJ/accounts.json) · [v2 전체 기록](JNJ/accounts-v2.json)

## CAT 계좌

| 모델 | 전략 | 평가액 USD | 손익 USD | 최근 매매·이유 |
|---|---|---:|---:|---|
| v1 | cash | 10000.00 | 0.00 | 대기 /  / 새 신호 대기 |
| v1 | buy_hold | 9356.79 | -643.21 | buy /  / buy_hold: prior completed bar target 100%; next bar open simulation |
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
| v1 | session_vwap | 8780.99 | -1219.01 | sell /  / 종가 > 뉴욕 거래일별 누적 전형가격 VWAP; 조건 미충족; close=687.345, session_VWAP=687.387, session_volume=2.45301e+06 |
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
| v2 | buy_hold | 8605.20 | -1394.80 | 중단: 손실 한도 / buy / partial / 직전 완료 봉 목표 비중 100%; 다음 봉 시가 가정 |
| v2 | trend_8_26 | 9207.79 | -792.21 | 중단: 손실 한도 / buy / partial / 직전 완료 봉 목표 비중 100%; 다음 봉 시가 가정 |
| v2 | momentum_26 | 9013.99 | -986.01 | 중단: 손실 한도 / buy / partial / 직전 완료 봉 목표 비중 100%; 다음 봉 시가 가정 |
| v2 | breakout_8 | 9125.42 | -874.58 | sell / filled / 직전 완료 봉 목표 비중 0%; 다음 봉 시가 가정 |
| v2 | reversion_12 | 8485.03 | -1514.97 | 중단: 손실 한도 / buy / partial / 직전 완료 봉 목표 비중 100%; 다음 봉 시가 가정 |
| v2 | volume_26 | 8727.69 | -1272.31 | 중단: 손실 한도 / buy / partial / 직전 완료 봉 목표 비중 100%; 다음 봉 시가 가정 |
| v2 | trend_8_26 AND momentum_26 | 9221.38 | -778.62 | 중단: 손실 한도 / buy / partial / 직전 완료 봉 목표 비중 100%; 다음 봉 시가 가정 |
| v2 | trend_8_26 + momentum_26 | 9111.36 | -888.64 | 중단: 손실 한도 / buy / partial / 직전 완료 봉 목표 비중 100%; 다음 봉 시가 가정 |
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
| v2 | reversion_12 AND volume_26 | 8667.31 | -1332.69 | 중단: 손실 한도 / buy / partial / 직전 완료 봉 목표 비중 100%; 다음 봉 시가 가정 |
| v2 | reversion_12 + volume_26 | 9102.12 | -897.88 | 중단: 손실 한도 / sell / filled / 직전 완료 봉 목표 비중 50%; 다음 봉 시가 가정 |
| v2 | ema_12_26 | 9307.59 | -692.41 | 중단: 손실 한도 / buy / partial / EMA12 > EMA26; 조건 충족; EMA12=726.261, EMA26=726.172; 직전 완료 봉 목표를 다음 봉 시가에 모의 적용 |
| v2 | macd_12_26_9 | 9984.52 | -15.48 | sell / filled / MACD > 신호선 그리고 MACD > 0; 조건 미충족; MACD=2.92675, signal9=3.02629; 직전 완료 봉 목표를 다음 봉 시가에 모의 적용 |
| v2 | rsi_14_recovery | 9858.74 | -141.26 | sell / filled / 직전 RSI14 < 30, 현재 RSI14 >= 30 (한 봉 목표); 조건 미충족; RSI14=34.2237, previous_RSI14=36.7431; 직전 완료 봉 목표를 다음 봉 시가에 모의 적용 |
| v2 | bollinger_20_reentry | 9601.72 | -398.28 | sell / filled / 직전 종가 < 직전 하단밴드, 현재 하단밴드 <= 종가 <= SMA20 (한 봉 목표); 조건 미충족; close=688.16, lower20=683.118, SMA20=697.519, previous_lower20=684.291; 직전 완료 봉 목표를 다음 봉 시가에 모의 적용 |
| v2 | donchian_20 | 9939.30 | -60.70 | sell / filled / 종가 > 현재 봉을 제외한 직전 20봉 최고가; 조건 미충족; close=735.35, prior_high20=745; 직전 완료 봉 목표를 다음 봉 시가에 모의 적용 |
| v2 | atr_14_breakout | 9758.55 | -241.45 | sell / filled / 종가 > 직전 종가 + 직전 ATR14 그리고 종가 > EMA26; 조건 미충족; close=735.35, threshold=737.263, prior_ATR14=4.10289, EMA26=727.331; 직전 완료 봉 목표를 다음 봉 시가에 모의 적용 |
| v2 | session_vwap | 8962.83 | -1037.17 | 중단: 손실 한도 / buy / partial / 종가 > 뉴욕 거래일별 누적 전형가격 VWAP; 조건 충족; close=734.98, session_VWAP=734.093, session_volume=764353; 직전 완료 봉 목표를 다음 봉 시가에 모의 적용 |
| v2 | obv_20 | 9245.54 | -754.46 | 중단: 손실 한도 / buy / partial / OBV > OBV의 SMA20 그리고 종가 > EMA26; 조건 충족; OBV=-5.0567e+06, OBV_SMA20=-6.30537e+06, close=733.16, EMA26=726.69; 직전 완료 봉 목표를 다음 봉 시가에 모의 적용 |
| v2 | stochastic_14_3_recovery | 9619.94 | -380.06 | sell / filled / 직전 %K14 < 20에서 %K14가 %D3 상향 돌파 (한 봉 목표); 조건 미충족; K14=24.7265, D3=31.6073, previous_K14=51.7944, previous_D3=39.927; 직전 완료 봉 목표를 다음 봉 시가에 모의 적용 |
| v2 | mfi_14_recovery | 9986.21 | -13.79 | sell / filled / 직전 MFI14 < 20, 현재 MFI14 >= 20 (한 봉 목표); 조건 미충족; MFI14=41.7007, previous_MFI14=39.2559; 직전 완료 봉 목표를 다음 봉 시가에 모의 적용 |
| v2 | adx_14_trend | 9325.50 | -674.50 | 중단: 손실 한도 / buy / partial / Wilder ADX14 >= 25 그리고 +DI14 > -DI14; 조건 충족; ADX14=25.4031, plus_DI14=35.2628, minus_DI14=13.9603; 직전 완료 봉 목표를 다음 봉 시가에 모의 적용 |
| v2 | aroon_25_trend | 9973.62 | -26.38 | sell / filled / Aroon25 Up > 70 그리고 Down < 30 (동률이면 최신 극값); 조건 미충족; Aroon_up=68, Aroon_down=20; 직전 완료 봉 목표를 다음 봉 시가에 모의 적용 |
| v2 | cci_20_momentum | 9854.97 | -145.03 | sell / filled / CCI20 > 100 (전형가격·평균절대편차); 조건 미충족; CCI20=99.2123; 직전 완료 봉 목표를 다음 봉 시가에 모의 적용 |
| v2 | williams_14_recovery | 9660.65 | -339.35 | sell / filled / 직전 Williams %R14 < -80, 현재 >= -80 (한 봉 목표); 조건 미충족; Williams_R14=-75.2735, previous_R14=-48.2056; 직전 완료 봉 목표를 다음 봉 시가에 모의 적용 |
| v2 | cmf_20_accumulation | 9166.83 | -833.17 | 중단: 손실 한도 / buy / partial / Chaikin Money Flow20 > 0.1; 조건 충족; CMF20=0.145111, volume20=965726; 직전 완료 봉 목표를 다음 봉 시가에 모의 적용 |
| v2 | chaikin_3_10 | 9062.53 | -937.47 | 중단: 손실 한도 / buy / partial / ADL의 EMA3 - EMA10 > 0 그리고 종가 > EMA26; 조건 충족; Chaikin3_10=293683, ADL=-4.91156e+06, close=739.58, EMA26=736.187; 직전 완료 봉 목표를 다음 봉 시가에 모의 적용 |
| v2 | roc_10_momentum | 9888.81 | -111.19 | sell / filled / 10봉 ROC > 1% 그리고 종가 > EMA26; 조건 미충족; ROC10_percent=0.883016, close=741.47, EMA26=734.681; 직전 완료 봉 목표를 다음 봉 시가에 모의 적용 |
| v2 | trix_15_trend | 9071.66 | -928.34 | 중단: 손실 한도 / buy / partial / 15봉 삼중 EMA의 1봉 변화율 TRIX > 0 그리고 종가 > EMA26; 조건 충족; TRIX15_percent=0.0196284, close=739.58, EMA26=736.187; 직전 완료 봉 목표를 다음 봉 시가에 모의 적용 |
| v2 | keltner_20_breakout | 10000.00 | 0.00 | 대기 /  / 새 신호 대기 |
| v2 | opening_range_30m | 10158.15 | 158.15 | sell / filled / 뉴욕 09:30·09:45 두 완료 봉 최고가를 10:00 이후 종가가 돌파; 자료 부족·변동폭 또는 거래량 없음: 대기; close=733.16; 직전 완료 봉 목표를 다음 봉 시가에 모의 적용 |

### 같은 기간의 비용·노출 비교 (사후 연구)

| 전략 | 비용 전 | 비용 후 | 100% 보유 | 같은 평균 노출 보유 | 평균 노출 |
|---|---:|---:|---:|---:|---:|
| cash | 0.00% | 0.00% | -18.38% | -0.00% | 0.00% |
| buy_hold | -18.04% | -18.38% | -18.38% | -18.38% | 100.00% |
| trend_8_26 | -2.45% | -5.67% | -18.38% | -7.47% | 38.38% |
| momentum_26 | -5.96% | -9.83% | -18.38% | -7.08% | 36.29% |
| breakout_8 | -1.90% | -14.23% | -18.38% | -3.06% | 15.40% |
| reversion_12 | -3.77% | -16.57% | -18.38% | -5.44% | 27.68% |
| volume_26 | -3.30% | -11.47% | -18.38% | -1.72% | 8.62% |
| trend_8_26 AND momentum_26 | -1.86% | -4.71% | -18.38% | -6.14% | 31.33% |
| trend_8_26 + momentum_26 | -4.20% | -7.76% | -18.38% | -7.27% | 37.34% |
| trend_8_26 AND breakout_8 | 0.84% | -5.31% | -18.38% | -1.62% | 8.09% |
| trend_8_26 + breakout_8 | -2.14% | -9.84% | -18.38% | -5.29% | 26.90% |
| trend_8_26 AND reversion_12 | 2.91% | -2.56% | -18.38% | -1.00% | 4.96% |
| trend_8_26 + reversion_12 | -3.04% | -10.32% | -18.38% | -6.46% | 33.03% |
| trend_8_26 AND volume_26 | 2.90% | 1.18% | -18.38% | -0.32% | 1.57% |
| trend_8_26 + volume_26 | -2.83% | -8.21% | -18.38% | -4.64% | 23.50% |
| momentum_26 AND breakout_8 | 0.09% | -6.80% | -18.38% | -1.67% | 8.36% |
| momentum_26 + breakout_8 | -3.92% | -12.04% | -18.38% | -5.09% | 25.85% |
| momentum_26 AND reversion_12 | -0.98% | -6.25% | -18.38% | -1.15% | 5.74% |
| momentum_26 + reversion_12 | -4.82% | -13.06% | -18.38% | -6.26% | 31.99% |
| momentum_26 AND volume_26 | 2.69% | 0.55% | -18.38% | -0.32% | 1.57% |
| momentum_26 + volume_26 | -4.60% | -10.25% | -18.38% | -4.43% | 22.46% |
| breakout_8 AND reversion_12 | 0.00% | 0.00% | -18.38% | -0.00% | 0.00% |
| breakout_8 + reversion_12 | -2.78% | -14.50% | -18.38% | -4.26% | 21.55% |
| breakout_8 AND volume_26 | 0.55% | -1.13% | -18.38% | -0.21% | 1.04% |
| breakout_8 + volume_26 | -2.57% | -12.30% | -18.38% | -2.40% | 12.02% |
| reversion_12 AND volume_26 | -2.64% | -7.81% | -18.38% | -1.10% | 5.48% |
| reversion_12 + volume_26 | -3.50% | -13.68% | -18.38% | -3.60% | 18.15% |
| ema_12_26 | -4.32% | -5.92% | -18.38% | -6.63% | 33.94% |
| macd_12_26_9 | 0.73% | -1.36% | -18.38% | -4.18% | 21.15% |
| rsi_14_recovery | -0.08% | -6.58% | -18.38% | -0.84% | 4.18% |
| bollinger_20_reentry | -0.84% | -6.50% | -18.38% | -0.73% | 3.66% |
| donchian_20 | 1.25% | -1.69% | -18.38% | -0.63% | 3.13% |
| atr_14_breakout | 1.29% | -2.88% | -18.38% | -0.58% | 2.87% |
| session_vwap | -5.08% | -16.31% | -18.38% | -8.83% | 45.69% |
| obv_20 | -3.87% | -11.62% | -18.38% | -3.83% | 19.32% |
| stochastic_14_3_recovery | -2.02% | -13.25% | -18.38% | -1.52% | 7.57% |
| mfi_14_recovery | 1.79% | -1.16% | -18.38% | -0.37% | 1.83% |
| adx_14_trend | -3.70% | -5.70% | -18.38% | -1.20% | 6.01% |
| aroon_25_trend | 1.10% | -1.83% | -18.38% | -1.62% | 8.09% |
| cci_20_momentum | -1.74% | -6.17% | -18.38% | -2.55% | 12.79% |
| williams_14_recovery | -2.07% | -10.34% | -18.38% | -1.10% | 5.48% |
| cmf_20_accumulation | -4.44% | -10.28% | -18.38% | -3.16% | 15.93% |
| chaikin_3_10 | -6.00% | -13.57% | -18.38% | -5.04% | 25.59% |
| roc_10_momentum | -0.09% | -5.40% | -18.38% | -1.88% | 9.40% |
| trix_15_trend | -3.86% | -7.43% | -18.38% | -5.19% | 26.37% |
| keltner_20_breakout | 0.38% | -0.46% | -18.38% | -0.26% | 1.31% |
| opening_range_30m | 3.63% | -0.21% | -18.38% | -4.23% | 21.41% |

동일 구간·초기 자금, 종료 시 청산 비용 포함. 노출 맞춤은 사후 설명용이며 v2 실제 계좌 성과가 아닙니다.
[낙폭 분해·비용 영향·전체 구간](CAT/comparison.json)

[v1 전체 기록](CAT/accounts.json) · [v2 전체 기록](CAT/accounts-v2.json)

## WMT 계좌

| 모델 | 전략 | 평가액 USD | 손익 USD | 최근 매매·이유 |
|---|---|---:|---:|---|
| v1 | cash | 10000.00 | 0.00 | 대기 /  / 새 신호 대기 |
| v1 | buy_hold | 10071.68 | 71.68 | buy /  / buy_hold: prior completed bar target 100%; next bar open simulation |
| v1 | trend_8_26 | 9779.58 | -220.42 | sell /  / trend_8_26: prior completed bar target 0%; next bar open simulation |
| v1 | momentum_26 | 9832.09 | -167.91 | sell /  / momentum_26: prior completed bar target 0%; next bar open simulation |
| v1 | breakout_8 | 9342.19 | -657.81 | sell /  / breakout_8: prior completed bar target 0%; next bar open simulation |
| v1 | reversion_12 | 9434.65 | -565.35 | buy /  / reversion_12: prior completed bar target 100%; next bar open simulation |
| v1 | volume_26 | 9775.35 | -224.65 | sell /  / volume_26: prior completed bar target 0%; next bar open simulation |
| v1 | trend_8_26 AND momentum_26 | 9861.19 | -138.81 | sell /  / trend_8_26 AND momentum_26: prior completed bar target 0%; next bar open simulation |
| v1 | trend_8_26 + momentum_26 | 9805.82 | -194.18 | sell /  / trend_8_26 + momentum_26: prior completed bar target 0%; next bar open simulation |
| v1 | trend_8_26 AND breakout_8 | 9602.19 | -397.81 | sell /  / trend_8_26 AND breakout_8: prior completed bar target 0%; next bar open simulation |
| v1 | trend_8_26 + breakout_8 | 9577.78 | -422.22 | sell /  / trend_8_26 + breakout_8: prior completed bar target 0%; next bar open simulation |
| v1 | trend_8_26 AND reversion_12 | 9683.74 | -316.26 | sell /  / trend_8_26 AND reversion_12: prior completed bar target 0%; next bar open simulation |
| v1 | trend_8_26 + reversion_12 | 9644.13 | -355.87 | sell /  / trend_8_26 + reversion_12: prior completed bar target 50%; next bar open simulation |
| v1 | trend_8_26 AND volume_26 | 9837.96 | -162.04 | sell /  / trend_8_26 AND volume_26: prior completed bar target 0%; next bar open simulation |
| v1 | trend_8_26 + volume_26 | 9777.89 | -222.11 | sell /  / trend_8_26 + volume_26: prior completed bar target 0%; next bar open simulation |
| v1 | momentum_26 AND breakout_8 | 9514.44 | -485.56 | sell /  / momentum_26 AND breakout_8: prior completed bar target 0%; next bar open simulation |
| v1 | momentum_26 + breakout_8 | 9642.15 | -357.85 | sell /  / momentum_26 + breakout_8: prior completed bar target 0%; next bar open simulation |
| v1 | momentum_26 AND reversion_12 | 9877.29 | -122.71 | sell /  / momentum_26 AND reversion_12: prior completed bar target 0%; next bar open simulation |
| v1 | momentum_26 + reversion_12 | 9728.00 | -272.00 | sell /  / momentum_26 + reversion_12: prior completed bar target 50%; next bar open simulation |
| v1 | momentum_26 AND volume_26 | 9853.50 | -146.50 | sell /  / momentum_26 AND volume_26: prior completed bar target 0%; next bar open simulation |
| v1 | momentum_26 + volume_26 | 9843.34 | -156.66 | sell /  / momentum_26 + volume_26: prior completed bar target 0%; next bar open simulation |
| v1 | breakout_8 AND reversion_12 | 10000.00 | 0.00 | 대기 /  / 새 신호 대기 |
| v1 | breakout_8 + reversion_12 | 9425.70 | -574.30 | sell /  / breakout_8 + reversion_12: prior completed bar target 50%; next bar open simulation |
| v1 | breakout_8 AND volume_26 | 9797.95 | -202.05 | sell /  / breakout_8 AND volume_26: prior completed bar target 0%; next bar open simulation |
| v1 | breakout_8 + volume_26 | 9556.59 | -443.41 | sell /  / breakout_8 + volume_26: prior completed bar target 0%; next bar open simulation |
| v1 | reversion_12 AND volume_26 | 9911.53 | -88.47 | sell /  / reversion_12 AND volume_26: prior completed bar target 0%; next bar open simulation |
| v1 | reversion_12 + volume_26 | 9661.35 | -338.65 | sell /  / reversion_12 + volume_26: prior completed bar target 50%; next bar open simulation |
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
| v1 | williams_14_recovery | 9645.18 | -354.82 | sell /  / 직전 Williams %R14 < -80, 현재 >= -80 (한 봉 목표); 조건 미충족; Williams_R14=-87.6038, previous_R14=-75.207 |
| v1 | cmf_20_accumulation | 9737.44 | -262.56 | sell /  / Chaikin Money Flow20 > 0.1; 조건 미충족; CMF20=0.0930543, volume20=1.6661e+07 |
| v1 | chaikin_3_10 | 9709.84 | -290.16 | sell /  / ADL의 EMA3 - EMA10 > 0 그리고 종가 > EMA26; 조건 미충족; Chaikin3_10=76755.7, ADL=1.33628e+07, close=120.04, EMA26=120.151 |
| v1 | roc_10_momentum | 10091.95 | 91.95 | sell /  / 10봉 ROC > 1% 그리고 종가 > EMA26; 조건 미충족; ROC10_percent=0.710203, close=120.535, EMA26=119.283 |
| v1 | trix_15_trend | 9640.97 | -359.03 | sell /  / 15봉 삼중 EMA의 1봉 변화율 TRIX > 0 그리고 종가 > EMA26; 조건 미충족; TRIX15_percent=0.0327766, close=119.98, EMA26=120.094 |
| v1 | keltner_20_breakout | 9879.35 | -120.65 | sell /  / 종가 > EMA20 + 2 x Wilder ATR14; 조건 미충족; close=121.08, upper_Keltner=121.15, EMA20=120.322, ATR14=0.414113 |
| v1 | opening_range_30m | 9860.78 | -139.22 | sell /  / 뉴욕 09:30·09:45 두 완료 봉 최고가를 10:00 이후 종가가 돌파; 자료 부족·변동폭 또는 거래량 없음: 대기; close=121.08 |
| v2 | cash | 10000.00 | 0.00 | 대기 /  / 새 신호 대기 |
| v2 | buy_hold | 10670.85 | 670.85 | buy / partial / 직전 완료 봉 목표 비중 100%; 다음 봉 시가 가정 |
| v2 | trend_8_26 | 10170.98 | 170.98 | sell / filled / 직전 완료 봉 목표 비중 0%; 다음 봉 시가 가정 |
| v2 | momentum_26 | 10228.38 | 228.38 | sell / filled / 직전 완료 봉 목표 비중 0%; 다음 봉 시가 가정 |
| v2 | breakout_8 | 9296.17 | -703.83 | 중단: 손실 한도 / sell / filled / 직전 완료 봉 목표 비중 0%; 다음 봉 시가 가정 |
| v2 | reversion_12 | 9324.01 | -675.99 | buy / partial / 직전 완료 봉 목표 비중 100%; 다음 봉 시가 가정 |
| v2 | volume_26 | 9727.78 | -272.22 | sell / filled / 직전 완료 봉 목표 비중 0%; 다음 봉 시가 가정 |
| v2 | trend_8_26 AND momentum_26 | 10255.85 | 255.85 | sell / filled / 직전 완료 봉 목표 비중 0%; 다음 봉 시가 가정 |
| v2 | trend_8_26 + momentum_26 | 10199.60 | 199.60 | sell / filled / 직전 완료 봉 목표 비중 0%; 다음 봉 시가 가정 |
| v2 | trend_8_26 AND breakout_8 | 9667.87 | -332.13 | sell / filled / 직전 완료 봉 목표 비중 0%; 다음 봉 시가 가정 |
| v2 | trend_8_26 + breakout_8 | 9736.05 | -263.95 | sell / filled / 직전 완료 봉 목표 비중 0%; 다음 봉 시가 가정 |
| v2 | trend_8_26 AND reversion_12 | 9487.14 | -512.86 | sell / filled / 직전 완료 봉 목표 비중 0%; 다음 봉 시가 가정 |
| v2 | trend_8_26 + reversion_12 | 9780.69 | -219.31 | sell / filled / 직전 완료 봉 목표 비중 50%; 다음 봉 시가 가정 |
| v2 | trend_8_26 AND volume_26 | 9784.10 | -215.90 | sell / filled / 직전 완료 봉 목표 비중 0%; 다음 봉 시가 가정 |
| v2 | trend_8_26 + volume_26 | 9948.73 | -51.27 | sell / filled / 직전 완료 봉 목표 비중 0%; 다음 봉 시가 가정 |
| v2 | momentum_26 AND breakout_8 | 9475.14 | -524.86 | 중단: 손실 한도 / sell / filled / 직전 완료 봉 목표 비중 0%; 다음 봉 시가 가정 |
| v2 | momentum_26 + breakout_8 | 9804.78 | -195.22 | sell / filled / 직전 완료 봉 목표 비중 0%; 다음 봉 시가 가정 |
| v2 | momentum_26 AND reversion_12 | 9700.42 | -299.58 | sell / filled / 직전 완료 봉 목표 비중 0%; 다음 봉 시가 가정 |
| v2 | momentum_26 + reversion_12 | 9911.65 | -88.35 | sell / filled / 직전 완료 봉 목표 비중 50%; 다음 봉 시가 가정 |
| v2 | momentum_26 AND volume_26 | 9760.78 | -239.22 | sell / filled / 직전 완료 봉 목표 비중 0%; 다음 봉 시가 가정 |
| v2 | momentum_26 + volume_26 | 10018.75 | 18.75 | sell / filled / 직전 완료 봉 목표 비중 0%; 다음 봉 시가 가정 |
| v2 | breakout_8 AND reversion_12 | 10000.00 | 0.00 | 대기 /  / 새 신호 대기 |
| v2 | breakout_8 + reversion_12 | 9361.27 | -638.73 | sell / filled / 직전 완료 봉 목표 비중 50%; 다음 봉 시가 가정 |
| v2 | breakout_8 AND volume_26 | 9741.39 | -258.61 | sell / filled / 직전 완료 봉 목표 비중 0%; 다음 봉 시가 가정 |
| v2 | breakout_8 + volume_26 | 9502.52 | -497.48 | sell / filled / 직전 완료 봉 목표 비중 0%; 다음 봉 시가 가정 |
| v2 | reversion_12 AND volume_26 | 9917.25 | -82.75 | sell / filled / 직전 완료 봉 목표 비중 0%; 다음 봉 시가 가정 |
| v2 | reversion_12 + volume_26 | 9583.87 | -416.13 | sell / filled / 직전 완료 봉 목표 비중 50%; 다음 봉 시가 가정 |
| v2 | ema_12_26 | 9966.01 | -33.99 | sell / filled / EMA12 > EMA26; 조건 미충족; EMA12=120.013, EMA26=120.022; 직전 완료 봉 목표를 다음 봉 시가에 모의 적용 |
| v2 | macd_12_26_9 | 10115.01 | 115.01 | sell / filled / MACD > 신호선 그리고 MACD > 0; 조건 미충족; MACD=0.563738, signal9=0.568978; 직전 완료 봉 목표를 다음 봉 시가에 모의 적용 |
| v2 | rsi_14_recovery | 9971.19 | -28.81 | sell / filled / 직전 RSI14 < 30, 현재 RSI14 >= 30 (한 봉 목표); 조건 미충족; RSI14=46.7246, previous_RSI14=43.1348; 직전 완료 봉 목표를 다음 봉 시가에 모의 적용 |
| v2 | bollinger_20_reentry | 9930.34 | -69.66 | sell / filled / 직전 종가 < 직전 하단밴드, 현재 하단밴드 <= 종가 <= SMA20 (한 봉 목표); 조건 미충족; close=120.035, lower20=119.686, SMA20=120.446, previous_lower20=119.732; 직전 완료 봉 목표를 다음 봉 시가에 모의 적용 |
| v2 | donchian_20 | 9630.34 | -369.66 | sell / filled / 종가 > 현재 봉을 제외한 직전 20봉 최고가; 조건 미충족; close=121.08, prior_high20=121.18; 직전 완료 봉 목표를 다음 봉 시가에 모의 적용 |
| v2 | atr_14_breakout | 9801.98 | -198.02 | sell / filled / 종가 > 직전 종가 + 직전 ATR14 그리고 종가 > EMA26; 조건 미충족; close=120.03, threshold=120.128, prior_ATR14=0.443028, EMA26=118.335; 직전 완료 봉 목표를 다음 봉 시가에 모의 적용 |
| v2 | session_vwap | 9660.42 | -339.58 | sell / filled / 종가 > 뉴욕 거래일별 누적 전형가격 VWAP; 조건 미충족; close=121.08, session_VWAP=121.52, session_volume=1.65503e+06; 직전 완료 봉 목표를 다음 봉 시가에 모의 적용 |
| v2 | obv_20 | 9880.47 | -119.53 | sell / filled / OBV > OBV의 SMA20 그리고 종가 > EMA26; 조건 미충족; OBV=1.93315e+07, OBV_SMA20=1.9255e+07, close=119.98, EMA26=120.094; 직전 완료 봉 목표를 다음 봉 시가에 모의 적용 |
| v2 | stochastic_14_3_recovery | 9772.76 | -227.24 | 중단: 손실 한도 / buy / partial / 직전 %K14 < 20에서 %K14가 %D3 상향 돌파 (한 봉 목표); 조건 충족; K14=25.6758, D3=22.4971, previous_K14=12.8379, previous_D3=25.8704; 직전 완료 봉 목표를 다음 봉 시가에 모의 적용 |
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
| cash | 0.00% | 0.00% | 14.43% | 0.00% | 0.00% |
| buy_hold | 14.91% | 14.43% | 14.43% | 14.43% | 100.00% |
| trend_8_26 | 10.14% | 6.50% | 14.43% | 10.28% | 73.11% |
| momentum_26 | 13.96% | 9.27% | 14.43% | 10.87% | 77.02% |
| breakout_8 | 6.46% | -11.87% | 14.43% | 3.76% | 27.94% |
| reversion_12 | 2.54% | -7.68% | 14.43% | 2.44% | 18.28% |
| volume_26 | 2.67% | -2.38% | 14.43% | 0.65% | 4.96% |
| trend_8_26 AND momentum_26 | 11.05% | 7.39% | 14.43% | 9.57% | 68.41% |
| trend_8_26 + momentum_26 | 12.03% | 7.88% | 14.43% | 10.57% | 75.07% |
| trend_8_26 AND breakout_8 | 6.87% | -8.51% | 14.43% | 3.19% | 23.76% |
| trend_8_26 + breakout_8 | 8.30% | -2.91% | 14.43% | 6.95% | 50.53% |
| trend_8_26 AND reversion_12 | -0.82% | -6.48% | 14.43% | 0.97% | 7.31% |
| trend_8_26 + reversion_12 | 6.31% | -0.42% | 14.43% | 6.26% | 45.70% |
| trend_8_26 AND volume_26 | 0.13% | -1.95% | 14.43% | 0.24% | 1.83% |
| trend_8_26 + volume_26 | 6.38% | 2.19% | 14.43% | 5.31% | 39.04% |
| momentum_26 AND breakout_8 | 6.71% | -10.17% | 14.43% | 3.51% | 26.11% |
| momentum_26 + breakout_8 | 10.17% | -1.23% | 14.43% | 7.24% | 52.49% |
| momentum_26 AND reversion_12 | 1.67% | -3.74% | 14.43% | 1.04% | 7.83% |
| momentum_26 + reversion_12 | 8.14% | 1.94% | 14.43% | 6.54% | 47.65% |
| momentum_26 AND volume_26 | 1.72% | -2.05% | 14.43% | 0.34% | 2.61% |
| momentum_26 + volume_26 | 8.21% | 3.73% | 14.43% | 5.59% | 40.99% |
| breakout_8 AND reversion_12 | 0.00% | 0.00% | 14.43% | 0.00% | 0.00% |
| breakout_8 + reversion_12 | 4.51% | -9.23% | 14.43% | 3.10% | 23.12% |
| breakout_8 AND volume_26 | 0.69% | -2.22% | 14.43% | 0.27% | 2.09% |
| breakout_8 + volume_26 | 4.58% | -7.04% | 14.43% | 2.19% | 16.46% |
| reversion_12 AND volume_26 | 0.43% | -0.83% | 14.43% | 0.14% | 1.04% |
| reversion_12 + volume_26 | 2.61% | -4.27% | 14.43% | 1.54% | 11.62% |
| ema_12_26 | 12.38% | 10.51% | 14.43% | 11.62% | 81.98% |
| macd_12_26_9 | 10.59% | 6.04% | 14.43% | 5.55% | 40.73% |
| rsi_14_recovery | 0.20% | -0.64% | 14.43% | 0.07% | 0.52% |
| bollinger_20_reentry | 1.82% | -0.72% | 14.43% | 0.21% | 1.57% |
| donchian_20 | 4.01% | -9.83% | 14.43% | 1.95% | 14.62% |
| atr_14_breakout | -0.01% | -9.97% | 14.43% | 1.00% | 7.57% |
| session_vwap | 11.69% | 1.40% | 14.43% | 8.41% | 60.57% |
| obv_20 | 12.22% | 4.48% | 14.43% | 8.76% | 62.92% |
| stochastic_14_3_recovery | -0.07% | -8.50% | 14.43% | 0.72% | 5.48% |
| mfi_14_recovery | 1.30% | -0.39% | 14.43% | 0.14% | 1.04% |
| adx_14_trend | 9.95% | 7.22% | 14.43% | 8.22% | 59.27% |
| aroon_25_trend | 8.13% | 2.81% | 14.43% | 4.60% | 33.94% |
| cci_20_momentum | 6.82% | -3.01% | 14.43% | 4.89% | 36.03% |
| williams_14_recovery | 0.63% | -6.30% | 14.43% | 0.58% | 4.44% |
| cmf_20_accumulation | 9.26% | 0.88% | 14.43% | 6.07% | 44.39% |
| chaikin_3_10 | 10.62% | 1.28% | 14.43% | 8.07% | 58.22% |
| roc_10_momentum | 1.03% | -3.94% | 14.43% | 2.26% | 16.97% |
| trix_15_trend | 11.09% | 6.07% | 14.43% | 10.00% | 71.28% |
| keltner_20_breakout | 7.26% | -0.55% | 14.43% | 4.13% | 30.55% |
| opening_range_30m | 11.01% | 4.67% | 14.43% | 5.81% | 42.56% |

동일 구간·초기 자금, 종료 시 청산 비용 포함. 노출 맞춤은 사후 설명용이며 v2 실제 계좌 성과가 아닙니다.
[낙폭 분해·비용 영향·전체 구간](WMT/comparison.json)

[v1 전체 기록](WMT/accounts.json) · [v2 전체 기록](WMT/accounts-v2.json)
