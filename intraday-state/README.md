# 모의투자 운영 현황

[PC·서버 장애 진단과 복구 방법](https://github.com/BaekJaeYeol/paper-trading-program/blob/main/investment-lab/docs/failure-recovery.md)

이번 실행 복구: {}

완료 봉 확인 주기: 기록 1/9회 · 기록 없는 예정 8회 · 아직 판정 전 17회 · 주의: 예약 시작 지연 또는 실행·저장 누락을 확인하세요.

[주기 판정 기준](https://github.com/BaekJaeYeol/paper-trading-program/blob/main/investment-lab/docs/session-coverage.md)

최근 확인: 2026-10-23T16:07:00.400844+00:00 (UTC)
다음 15분 확인 목표 (세션 실행 중에만 적용): 2026-10-23T16:22:00+00:00 (UTC, 실행 지연 가능)

실제 주문 없음. v1 기존 계좌와 v2 새 계좌의 시작일이 다르므로 수익률을 직접 우열 비교하지 마세요.
v2는 다음 봉 시가에 비용·스프레드·직전 거래량 제한을 적용한 가상 체결입니다. 미체결 잔량은 만료됩니다.

| 종목 | 상태 | 최근 성공 UTC | 마지막 완료 봉 UTC | 이번 새 봉 |
|---|---|---|---|---|
| SPY | updated | 2026-10-23T16:07:00.400844+00:00 | 2026-10-23T15:45:00+00:00 | 1 |
| QQQ | updated | 2026-10-23T16:07:00.400844+00:00 | 2026-10-23T15:45:00+00:00 | 1 |
| IWM | updated | 2026-10-23T16:07:00.400844+00:00 | 2026-10-23T15:45:00+00:00 | 1 |
| DIA | updated | 2026-10-23T16:07:00.400844+00:00 | 2026-10-23T15:45:00+00:00 | 1 |
| MSFT | updated | 2026-10-23T16:07:00.400844+00:00 | 2026-10-23T15:45:00+00:00 | 1 |
| JPM | updated | 2026-10-23T16:07:00.400844+00:00 | 2026-10-23T15:45:00+00:00 | 1 |
| XOM | updated | 2026-10-23T16:07:00.400844+00:00 | 2026-10-23T15:45:00+00:00 | 1 |
| JNJ | updated | 2026-10-23T16:07:00.400844+00:00 | 2026-10-23T15:45:00+00:00 | 1 |
| CAT | updated | 2026-10-23T16:07:00.400844+00:00 | 2026-10-23T15:45:00+00:00 | 1 |
| WMT | updated | 2026-10-23T16:07:00.400844+00:00 | 2026-10-23T15:45:00+00:00 | 1 |

이번 실행 소요: 50.47초
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
| v1 | buy_hold | 9848.45 | -151.55 | buy /  / buy_hold: prior completed bar target 100%; next bar open simulation |
| v1 | trend_8_26 | 9711.09 | -288.91 | sell /  / trend_8_26: prior completed bar target 0%; next bar open simulation |
| v1 | momentum_26 | 9631.54 | -368.46 | sell /  / momentum_26: prior completed bar target 0%; next bar open simulation |
| v1 | breakout_8 | 9473.86 | -526.14 | sell /  / breakout_8: prior completed bar target 0%; next bar open simulation |
| v1 | reversion_12 | 9483.61 | -516.39 | sell /  / reversion_12: prior completed bar target 0%; next bar open simulation |
| v1 | volume_26 | 9358.66 | -641.34 | sell /  / volume_26: prior completed bar target 0%; next bar open simulation |
| v1 | trend_8_26 AND momentum_26 | 9624.28 | -375.72 | sell /  / trend_8_26 AND momentum_26: prior completed bar target 0%; next bar open simulation |
| v1 | trend_8_26 + momentum_26 | 9671.22 | -328.78 | sell /  / trend_8_26 + momentum_26: prior completed bar target 0%; next bar open simulation |
| v1 | trend_8_26 AND breakout_8 | 9730.71 | -269.29 | sell /  / trend_8_26 AND breakout_8: prior completed bar target 0%; next bar open simulation |
| v1 | trend_8_26 + breakout_8 | 9630.12 | -369.88 | sell /  / trend_8_26 + breakout_8: prior completed bar target 0%; next bar open simulation |
| v1 | trend_8_26 AND reversion_12 | 9736.23 | -263.77 | sell /  / trend_8_26 AND reversion_12: prior completed bar target 0%; next bar open simulation |
| v1 | trend_8_26 + reversion_12 | 9596.47 | -403.53 | sell /  / trend_8_26 + reversion_12: prior completed bar target 0%; next bar open simulation |
| v1 | trend_8_26 AND volume_26 | 9605.36 | -394.64 | sell /  / trend_8_26 AND volume_26: prior completed bar target 0%; next bar open simulation |
| v1 | trend_8_26 + volume_26 | 9533.09 | -466.91 | sell /  / trend_8_26 + volume_26: prior completed bar target 0%; next bar open simulation |
| v1 | momentum_26 AND breakout_8 | 9640.01 | -359.99 | sell /  / momentum_26 AND breakout_8: prior completed bar target 0%; next bar open simulation |
| v1 | momentum_26 + breakout_8 | 9552.40 | -447.60 | sell /  / momentum_26 + breakout_8: prior completed bar target 0%; next bar open simulation |
| v1 | momentum_26 AND reversion_12 | 9769.70 | -230.30 | sell /  / momentum_26 AND reversion_12: prior completed bar target 0%; next bar open simulation |
| v1 | momentum_26 + reversion_12 | 9614.64 | -385.36 | sell /  / momentum_26 + reversion_12: prior completed bar target 0%; next bar open simulation |
| v1 | momentum_26 AND volume_26 | 9618.73 | -381.27 | sell /  / momentum_26 AND volume_26: prior completed bar target 0%; next bar open simulation |
| v1 | momentum_26 + volume_26 | 9493.96 | -506.04 | sell /  / momentum_26 + volume_26: prior completed bar target 0%; next bar open simulation |
| v1 | breakout_8 AND reversion_12 | 10000.00 | 0.00 | 대기 /  / 새 신호 대기 |
| v1 | breakout_8 + reversion_12 | 9516.31 | -483.69 | sell /  / breakout_8 + reversion_12: prior completed bar target 0%; next bar open simulation |
| v1 | breakout_8 AND volume_26 | 9807.14 | -192.86 | sell /  / breakout_8 AND volume_26: prior completed bar target 0%; next bar open simulation |
| v1 | breakout_8 + volume_26 | 9453.51 | -546.49 | sell /  / breakout_8 + volume_26: prior completed bar target 0%; next bar open simulation |
| v1 | reversion_12 AND volume_26 | 9811.81 | -188.19 | sell /  / reversion_12 AND volume_26: prior completed bar target 0%; next bar open simulation |
| v1 | reversion_12 + volume_26 | 9496.28 | -503.72 | sell /  / reversion_12 + volume_26: prior completed bar target 0%; next bar open simulation |
| v1 | ema_12_26 | 9742.51 | -257.49 | sell /  / EMA12 > EMA26; 조건 미충족; EMA12=771.277, EMA26=771.539 |
| v1 | macd_12_26_9 | 9769.55 | -230.45 | sell /  / MACD > 신호선 그리고 MACD > 0; 조건 미충족; MACD=1.03945, signal9=1.12358 |
| v1 | rsi_14_recovery | 9805.98 | -194.02 | sell /  / 직전 RSI14 < 30, 현재 RSI14 >= 30 (한 봉 목표); 조건 미충족; RSI14=38.7389, previous_RSI14=37.2051 |
| v1 | bollinger_20_reentry | 9716.86 | -283.14 | sell /  / 직전 종가 < 직전 하단밴드, 현재 하단밴드 <= 종가 <= SMA20 (한 봉 목표); 조건 미충족; close=762.88, lower20=759.962, SMA20=762.264, previous_lower20=759.738 |
| v1 | donchian_20 | 9818.08 | -181.92 | sell /  / 종가 > 현재 봉을 제외한 직전 20봉 최고가; 조건 미충족; close=774.19, prior_high20=774.44 |
| v1 | atr_14_breakout | 9816.89 | -183.11 | sell /  / 종가 > 직전 종가 + 직전 ATR14 그리고 종가 > EMA26; 조건 미충족; close=773.07, threshold=774.291, prior_ATR14=1.05565, EMA26=772.249 |
| v1 | session_vwap | 9429.63 | -570.37 | buy /  / 종가 > 뉴욕 거래일별 누적 전형가격 VWAP; 조건 충족; close=761.64, session_VWAP=760.614, session_volume=1.67272e+07 |
| v1 | obv_20 | 9597.93 | -402.07 | sell /  / OBV > OBV의 SMA20 그리고 종가 > EMA26; 조건 미충족; OBV=-588094, OBV_SMA20=-9.96088e+06, close=766.62, EMA26=771.893 |
| v1 | stochastic_14_3_recovery | 9461.72 | -538.28 | sell /  / 직전 %K14 < 20에서 %K14가 %D3 상향 돌파 (한 봉 목표); 조건 미충족; K14=78.2126, D3=50.4634, previous_K14=55.1135, previous_D3=31.7922 |
| v1 | mfi_14_recovery | 9810.25 | -189.75 | sell /  / 직전 MFI14 < 20, 현재 MFI14 >= 20 (한 봉 목표); 조건 미충족; MFI14=24.2496, previous_MFI14=22.3876 |
| v1 | adx_14_trend | 9981.96 | -18.04 | sell /  / Wilder ADX14 >= 25 그리고 +DI14 > -DI14; 조건 미충족; ADX14=24.2312, plus_DI14=28.3519, minus_DI14=24.6578 |
| v1 | aroon_25_trend | 9728.66 | -271.34 | sell /  / Aroon25 Up > 70 그리고 Down < 30 (동률이면 최신 극값); 조건 미충족; Aroon_up=72, Aroon_down=100 |
| v1 | cci_20_momentum | 9766.23 | -233.77 | sell /  / CCI20 > 100 (전형가격·평균절대편차); 조건 미충족; CCI20=97.3932 |
| v1 | williams_14_recovery | 9410.56 | -589.44 | sell /  / 직전 Williams %R14 < -80, 현재 >= -80 (한 봉 목표); 조건 미충족; Williams_R14=-21.7874, previous_R14=-44.8865 |
| v1 | cmf_20_accumulation | 9670.75 | -329.25 | buy /  / Chaikin Money Flow20 > 0.1; 조건 충족; CMF20=0.264253, volume20=5.65809e+07 |
| v1 | chaikin_3_10 | 9565.38 | -434.62 | sell /  / ADL의 EMA3 - EMA10 > 0 그리고 종가 > EMA26; 조건 미충족; Chaikin3_10=1.08024e+06, ADL=4.14098e+07, close=766.62, EMA26=771.893 |
| v1 | roc_10_momentum | 9953.42 | -46.58 | sell /  / 10봉 ROC > 1% 그리고 종가 > EMA26; 조건 미충족; ROC10_percent=0.806376, close=769.45, EMA26=767.181 |
| v1 | trix_15_trend | 9489.99 | -510.01 | sell /  / 15봉 삼중 EMA의 1봉 변화율 TRIX > 0 그리고 종가 > EMA26; 조건 미충족; TRIX15_percent=0.0154379, close=766.62, EMA26=771.893 |
| v1 | keltner_20_breakout | 9810.90 | -189.10 | sell /  / 종가 > EMA20 + 2 x Wilder ATR14; 조건 미충족; close=774.19, upper_Keltner=774.31, EMA20=772.615, ATR14=0.847257 |
| v1 | opening_range_30m | 9649.63 | -350.37 | buy /  / 뉴욕 09:30·09:45 두 완료 봉 최고가를 10:00 이후 종가가 돌파; 조건 충족; close=761.64, opening_high=761.2 |
| v2 | cash | 10000.00 | 0.00 | 대기 /  / 새 신호 대기 |
| v2 | buy_hold | 9777.41 | -222.59 | buy / partial / 직전 완료 봉 목표 비중 100%; 다음 봉 시가 가정 |
| v2 | trend_8_26 | 9591.24 | -408.76 | sell / filled / 직전 완료 봉 목표 비중 0%; 다음 봉 시가 가정 |
| v2 | momentum_26 | 9482.22 | -517.78 | sell / filled / 직전 완료 봉 목표 비중 0%; 다음 봉 시가 가정 |
| v2 | breakout_8 | 9069.97 | -930.03 | sell / filled / 직전 완료 봉 목표 비중 0%; 다음 봉 시가 가정 |
| v2 | reversion_12 | 9019.94 | -980.06 | sell / filled / 직전 완료 봉 목표 비중 0%; 다음 봉 시가 가정 |
| v2 | volume_26 | 8987.83 | -1012.17 | 중단: 손실 한도 / buy / partial / 직전 완료 봉 목표 비중 100%; 다음 봉 시가 가정 |
| v2 | trend_8_26 AND momentum_26 | 9481.53 | -518.47 | sell / filled / 직전 완료 봉 목표 비중 0%; 다음 봉 시가 가정 |
| v2 | trend_8_26 + momentum_26 | 9536.57 | -463.43 | sell / filled / 직전 완료 봉 목표 비중 0%; 다음 봉 시가 가정 |
| v2 | trend_8_26 AND breakout_8 | 9547.25 | -452.75 | sell / filled / 직전 완료 봉 목표 비중 0%; 다음 봉 시가 가정 |
| v2 | trend_8_26 + breakout_8 | 9366.04 | -633.96 | sell / filled / 직전 완료 봉 목표 비중 0%; 다음 봉 시가 가정 |
| v2 | trend_8_26 AND reversion_12 | 9621.61 | -378.39 | sell / filled / 직전 완료 봉 목표 비중 0%; 다음 봉 시가 가정 |
| v2 | trend_8_26 + reversion_12 | 9300.68 | -699.32 | sell / filled / 직전 완료 봉 목표 비중 0%; 다음 봉 시가 가정 |
| v2 | trend_8_26 AND volume_26 | 9442.22 | -557.78 | sell / filled / 직전 완료 봉 목표 비중 0%; 다음 봉 시가 가정 |
| v2 | trend_8_26 + volume_26 | 9210.98 | -789.02 | sell / filled / 직전 완료 봉 목표 비중 0%; 다음 봉 시가 가정 |
| v2 | momentum_26 AND breakout_8 | 9414.38 | -585.62 | sell / filled / 직전 완료 봉 목표 비중 0%; 다음 봉 시가 가정 |
| v2 | momentum_26 + breakout_8 | 9273.75 | -726.25 | sell / filled / 직전 완료 봉 목표 비중 0%; 다음 봉 시가 가정 |
| v2 | momentum_26 AND reversion_12 | 9722.08 | -277.92 | sell / filled / 직전 완료 봉 목표 비중 0%; 다음 봉 시가 가정 |
| v2 | momentum_26 + reversion_12 | 9325.73 | -674.27 | sell / filled / 직전 완료 봉 목표 비중 0%; 다음 봉 시가 가정 |
| v2 | momentum_26 AND volume_26 | 9523.88 | -476.12 | sell / filled / 직전 완료 봉 목표 비중 0%; 다음 봉 시가 가정 |
| v2 | momentum_26 + volume_26 | 9197.00 | -803.00 | sell / filled / 직전 완료 봉 목표 비중 0%; 다음 봉 시가 가정 |
| v2 | breakout_8 AND reversion_12 | 10000.00 | 0.00 | 대기 /  / 새 신호 대기 |
| v2 | breakout_8 + reversion_12 | 9120.37 | -879.63 | sell / filled / 직전 완료 봉 목표 비중 0%; 다음 봉 시가 가정 |
| v2 | breakout_8 AND volume_26 | 9733.81 | -266.19 | sell / filled / 직전 완료 봉 목표 비중 0%; 다음 봉 시가 가정 |
| v2 | breakout_8 + volume_26 | 9013.51 | -986.49 | sell / filled / 직전 완료 봉 목표 비중 0%; 다음 봉 시가 가정 |
| v2 | reversion_12 AND volume_26 | 9552.33 | -447.67 | sell / filled / 직전 완료 봉 목표 비중 0%; 다음 봉 시가 가정 |
| v2 | reversion_12 + volume_26 | 9064.51 | -935.49 | sell / filled / 직전 완료 봉 목표 비중 0%; 다음 봉 시가 가정 |
| v2 | ema_12_26 | 9736.67 | -263.33 | sell / filled / EMA12 > EMA26; 조건 미충족; EMA12=771.277, EMA26=771.539; 직전 완료 봉 목표를 다음 봉 시가에 모의 적용 |
| v2 | macd_12_26_9 | 9761.73 | -238.27 | sell / filled / MACD > 신호선 그리고 MACD > 0; 조건 미충족; MACD=1.03945, signal9=1.12358; 직전 완료 봉 목표를 다음 봉 시가에 모의 적용 |
| v2 | rsi_14_recovery | 9798.14 | -201.86 | sell / filled / 직전 RSI14 < 30, 현재 RSI14 >= 30 (한 봉 목표); 조건 미충족; RSI14=38.7389, previous_RSI14=37.2051; 직전 완료 봉 목표를 다음 봉 시가에 모의 적용 |
| v2 | bollinger_20_reentry | 9705.21 | -294.79 | sell / filled / 직전 종가 < 직전 하단밴드, 현재 하단밴드 <= 종가 <= SMA20 (한 봉 목표); 조건 미충족; close=762.88, lower20=759.962, SMA20=762.264, previous_lower20=759.738; 직전 완료 봉 목표를 다음 봉 시가에 모의 적용 |
| v2 | donchian_20 | 9808.27 | -191.73 | sell / filled / 종가 > 현재 봉을 제외한 직전 20봉 최고가; 조건 미충족; close=774.19, prior_high20=774.44; 직전 완료 봉 목표를 다음 봉 시가에 모의 적용 |
| v2 | atr_14_breakout | 9807.08 | -192.92 | sell / filled / 종가 > 직전 종가 + 직전 ATR14 그리고 종가 > EMA26; 조건 미충족; close=773.07, threshold=774.291, prior_ATR14=1.05565, EMA26=772.249; 직전 완료 봉 목표를 다음 봉 시가에 모의 적용 |
| v2 | session_vwap | 9407.97 | -592.03 | buy / partial / 종가 > 뉴욕 거래일별 누적 전형가격 VWAP; 조건 충족; close=761.64, session_VWAP=760.614, session_volume=1.67272e+07; 직전 완료 봉 목표를 다음 봉 시가에 모의 적용 |
| v2 | obv_20 | 9584.50 | -415.50 | sell / filled / OBV > OBV의 SMA20 그리고 종가 > EMA26; 조건 미충족; OBV=-949325, OBV_SMA20=-1.03221e+07, close=766.62, EMA26=771.893; 직전 완료 봉 목표를 다음 봉 시가에 모의 적용 |
| v2 | stochastic_14_3_recovery | 9431.49 | -568.51 | sell / filled / 직전 %K14 < 20에서 %K14가 %D3 상향 돌파 (한 봉 목표); 조건 미충족; K14=78.2126, D3=50.4634, previous_K14=55.1135, previous_D3=31.7922; 직전 완료 봉 목표를 다음 봉 시가에 모의 적용 |
| v2 | mfi_14_recovery | 9800.44 | -199.56 | sell / filled / 직전 MFI14 < 20, 현재 MFI14 >= 20 (한 봉 목표); 조건 미충족; MFI14=24.2496, previous_MFI14=22.3876; 직전 완료 봉 목표를 다음 봉 시가에 모의 적용 |
| v2 | adx_14_trend | 9979.97 | -20.03 | sell / filled / Wilder ADX14 >= 25 그리고 +DI14 > -DI14; 조건 미충족; ADX14=24.2312, plus_DI14=28.3519, minus_DI14=24.6578; 직전 완료 봉 목표를 다음 봉 시가에 모의 적용 |
| v2 | aroon_25_trend | 9722.82 | -277.18 | sell / filled / Aroon25 Up > 70 그리고 Down < 30 (동률이면 최신 극값); 조건 미충족; Aroon_up=72, Aroon_down=100; 직전 완료 봉 목표를 다음 봉 시가에 모의 적용 |
| v2 | cci_20_momentum | 9754.52 | -245.48 | sell / filled / CCI20 > 100 (전형가격·평균절대편차); 조건 미충족; CCI20=97.3932; 직전 완료 봉 목표를 다음 봉 시가에 모의 적용 |
| v2 | williams_14_recovery | 9378.62 | -621.38 | sell / filled / 직전 Williams %R14 < -80, 현재 >= -80 (한 봉 목표); 조건 미충족; Williams_R14=-21.7874, previous_R14=-44.8865; 직전 완료 봉 목표를 다음 봉 시가에 모의 적용 |
| v2 | cmf_20_accumulation | 9660.12 | -339.88 | buy / partial / Chaikin Money Flow20 > 0.1; 조건 충족; CMF20=0.264253, volume20=5.65809e+07; 직전 완료 봉 목표를 다음 봉 시가에 모의 적용 |
| v2 | chaikin_3_10 | 9550.09 | -449.91 | sell / filled / ADL의 EMA3 - EMA10 > 0 그리고 종가 > EMA26; 조건 미충족; Chaikin3_10=1.08024e+06, ADL=4.99714e+07, close=766.62, EMA26=771.893; 직전 완료 봉 목표를 다음 봉 시가에 모의 적용 |
| v2 | roc_10_momentum | 9951.43 | -48.57 | sell / filled / 10봉 ROC > 1% 그리고 종가 > EMA26; 조건 미충족; ROC10_percent=0.806376, close=769.45, EMA26=767.181; 직전 완료 봉 목표를 다음 봉 시가에 모의 적용 |
| v2 | trix_15_trend | 9472.93 | -527.07 | sell / filled / 15봉 삼중 EMA의 1봉 변화율 TRIX > 0 그리고 종가 > EMA26; 조건 미충족; TRIX15_percent=0.0154379, close=766.62, EMA26=771.893; 직전 완료 봉 목표를 다음 봉 시가에 모의 적용 |
| v2 | keltner_20_breakout | 9803.05 | -196.95 | sell / filled / 종가 > EMA20 + 2 x Wilder ATR14; 조건 미충족; close=774.19, upper_Keltner=774.31, EMA20=772.615, ATR14=0.847257; 직전 완료 봉 목표를 다음 봉 시가에 모의 적용 |
| v2 | opening_range_30m | 9637.09 | -362.91 | buy / partial / 뉴욕 09:30·09:45 두 완료 봉 최고가를 10:00 이후 종가가 돌파; 조건 충족; close=761.64, opening_high=761.2; 직전 완료 봉 목표를 다음 봉 시가에 모의 적용 |

### 같은 기간의 비용·노출 비교 (사후 연구)

| 전략 | 비용 전 | 비용 후 | 100% 보유 | 같은 평균 노출 보유 | 평균 노출 |
|---|---:|---:|---:|---:|---:|
| cash | 0.00% | 0.00% | -1.18% | -0.00% | 0.00% |
| buy_hold | -0.77% | -1.18% | -1.18% | -1.18% | 100.00% |
| trend_8_26 | -0.27% | -3.97% | -1.18% | -0.59% | 50.00% |
| momentum_26 | -0.91% | -5.38% | -1.18% | -0.60% | 50.53% |
| breakout_8 | 0.15% | -15.69% | -1.18% | -0.28% | 23.95% |
| reversion_12 | -1.12% | -12.09% | -1.18% | -0.33% | 28.16% |
| volume_26 | -1.14% | -11.74% | -1.18% | -0.12% | 10.26% |
| trend_8_26 AND momentum_26 | -0.31% | -4.81% | -1.18% | -0.51% | 43.42% |
| trend_8_26 + momentum_26 | -0.59% | -4.68% | -1.18% | -0.59% | 50.27% |
| trend_8_26 AND breakout_8 | 0.43% | -10.33% | -1.18% | -0.18% | 15.00% |
| trend_8_26 + breakout_8 | -0.06% | -9.64% | -1.18% | -0.44% | 36.98% |
| trend_8_26 AND reversion_12 | 0.20% | -4.32% | -1.18% | -0.07% | 6.32% |
| trend_8_26 + reversion_12 | -0.69% | -7.93% | -1.18% | -0.46% | 39.08% |
| trend_8_26 AND volume_26 | -1.05% | -6.30% | -1.18% | -0.07% | 5.53% |
| trend_8_26 + volume_26 | -0.70% | -7.94% | -1.18% | -0.36% | 30.14% |
| momentum_26 AND breakout_8 | 0.60% | -10.93% | -1.18% | -0.20% | 16.58% |
| momentum_26 + breakout_8 | -0.38% | -10.69% | -1.18% | -0.44% | 37.24% |
| momentum_26 AND reversion_12 | -0.39% | -4.89% | -1.18% | -0.07% | 6.05% |
| momentum_26 + reversion_12 | -1.01% | -8.04% | -1.18% | -0.47% | 39.35% |
| momentum_26 AND volume_26 | -0.79% | -5.27% | -1.18% | -0.05% | 3.95% |
| momentum_26 + volume_26 | -1.02% | -7.85% | -1.18% | -0.36% | 30.40% |
| breakout_8 AND reversion_12 | 0.00% | 0.00% | -1.18% | -0.00% | 0.00% |
| breakout_8 + reversion_12 | -0.49% | -13.20% | -1.18% | -0.31% | 26.06% |
| breakout_8 AND volume_26 | -0.26% | -3.15% | -1.18% | -0.03% | 2.37% |
| breakout_8 + volume_26 | -0.50% | -13.20% | -1.18% | -0.20% | 17.11% |
| reversion_12 AND volume_26 | -0.97% | -5.05% | -1.18% | -0.04% | 3.68% |
| reversion_12 + volume_26 | -1.13% | -10.99% | -1.18% | -0.23% | 19.22% |
| ema_12_26 | -1.09% | -4.36% | -1.18% | -0.63% | 53.68% |
| macd_12_26_9 | -0.36% | -4.86% | -1.18% | -0.38% | 31.84% |
| rsi_14_recovery | -0.42% | -3.71% | -1.18% | -0.02% | 2.11% |
| bollinger_20_reentry | -0.89% | -6.94% | -1.18% | -0.05% | 3.95% |
| donchian_20 | 0.22% | -7.85% | -1.18% | -0.09% | 7.37% |
| atr_14_breakout | 0.45% | -4.89% | -1.18% | -0.04% | 3.68% |
| session_vwap | -0.30% | -10.99% | -1.18% | -0.57% | 47.89% |
| obv_20 | -0.82% | -9.57% | -1.18% | -0.44% | 37.63% |
| stochastic_14_3_recovery | 0.64% | -14.20% | -1.18% | -0.12% | 10.00% |
| mfi_14_recovery | 0.11% | -2.79% | -1.18% | -0.02% | 1.84% |
| adx_14_trend | 1.03% | -0.65% | -1.18% | -0.26% | 22.11% |
| aroon_25_trend | 0.13% | -2.36% | -1.18% | -0.28% | 23.42% |
| cci_20_momentum | 0.49% | -7.22% | -1.18% | -0.26% | 22.11% |
| williams_14_recovery | 0.50% | -11.77% | -1.18% | -0.10% | 8.16% |
| cmf_20_accumulation | 1.09% | -3.88% | -1.18% | -0.58% | 49.21% |
| chaikin_3_10 | 0.30% | -6.61% | -1.18% | -0.48% | 40.53% |
| roc_10_momentum | -0.07% | -0.49% | -1.18% | -0.00% | 0.26% |
| trix_15_trend | -0.93% | -6.20% | -1.18% | -0.49% | 41.05% |
| keltner_20_breakout | 0.19% | -3.93% | -1.18% | -0.13% | 10.79% |
| opening_range_30m | 0.06% | -6.05% | -1.18% | -0.50% | 42.37% |

동일 구간·초기 자금, 종료 시 청산 비용 포함. 노출 맞춤은 사후 설명용이며 v2 실제 계좌 성과가 아닙니다.
[낙폭 분해·비용 영향·전체 구간](SPY/comparison.json)

[v1 전체 기록](SPY/accounts.json) · [v2 전체 기록](SPY/accounts-v2.json)

## QQQ 계좌

| 모델 | 전략 | 평가액 USD | 손익 USD | 최근 매매·이유 |
|---|---|---:|---:|---|
| v1 | cash | 10000.00 | 0.00 | 대기 /  / 새 신호 대기 |
| v1 | buy_hold | 9747.12 | -252.88 | buy /  / buy_hold: prior completed bar target 100%; next bar open simulation |
| v1 | trend_8_26 | 9681.36 | -318.64 | buy /  / trend_8_26: prior completed bar target 100%; next bar open simulation |
| v1 | momentum_26 | 9342.16 | -657.84 | sell /  / momentum_26: prior completed bar target 0%; next bar open simulation |
| v1 | breakout_8 | 9517.02 | -482.98 | sell /  / breakout_8: prior completed bar target 0%; next bar open simulation |
| v1 | reversion_12 | 9514.59 | -485.41 | sell /  / reversion_12: prior completed bar target 0%; next bar open simulation |
| v1 | volume_26 | 9492.12 | -507.88 | buy /  / volume_26: prior completed bar target 100%; next bar open simulation |
| v1 | trend_8_26 AND momentum_26 | 9702.95 | -297.05 | sell /  / trend_8_26 AND momentum_26: prior completed bar target 0%; next bar open simulation |
| v1 | trend_8_26 + momentum_26 | 9548.43 | -451.57 | sell /  / trend_8_26 + momentum_26: prior completed bar target 50%; next bar open simulation |
| v1 | trend_8_26 AND breakout_8 | 9949.62 | -50.38 | sell /  / trend_8_26 AND breakout_8: prior completed bar target 0%; next bar open simulation |
| v1 | trend_8_26 + breakout_8 | 9656.78 | -343.22 | buy /  / trend_8_26 + breakout_8: prior completed bar target 50%; next bar open simulation |
| v1 | trend_8_26 AND reversion_12 | 9885.50 | -114.50 | sell /  / trend_8_26 AND reversion_12: prior completed bar target 0%; next bar open simulation |
| v1 | trend_8_26 + reversion_12 | 9636.26 | -363.74 | buy /  / trend_8_26 + reversion_12: prior completed bar target 50%; next bar open simulation |
| v1 | trend_8_26 AND volume_26 | 9818.60 | -181.40 | buy /  / trend_8_26 AND volume_26: prior completed bar target 100%; next bar open simulation |
| v1 | trend_8_26 + volume_26 | 9586.38 | -413.62 | buy /  / trend_8_26 + volume_26: prior completed bar target 100%; next bar open simulation |
| v1 | momentum_26 AND breakout_8 | 9644.64 | -355.36 | sell /  / momentum_26 AND breakout_8: prior completed bar target 0%; next bar open simulation |
| v1 | momentum_26 + breakout_8 | 9448.35 | -551.65 | sell /  / momentum_26 + breakout_8: prior completed bar target 0%; next bar open simulation |
| v1 | momentum_26 AND reversion_12 | 9783.95 | -216.05 | sell /  / momentum_26 AND reversion_12: prior completed bar target 0%; next bar open simulation |
| v1 | momentum_26 + reversion_12 | 9484.98 | -515.02 | sell /  / momentum_26 + reversion_12: prior completed bar target 0%; next bar open simulation |
| v1 | momentum_26 AND volume_26 | 9789.69 | -210.31 | sell /  / momentum_26 AND volume_26: prior completed bar target 0%; next bar open simulation |
| v1 | momentum_26 + volume_26 | 9435.81 | -564.19 | buy /  / momentum_26 + volume_26: prior completed bar target 50%; next bar open simulation |
| v1 | breakout_8 AND reversion_12 | 10000.00 | 0.00 | 대기 /  / 새 신호 대기 |
| v1 | breakout_8 + reversion_12 | 9553.82 | -446.18 | sell /  / breakout_8 + reversion_12: prior completed bar target 0%; next bar open simulation |
| v1 | breakout_8 AND volume_26 | 9929.33 | -70.67 | sell /  / breakout_8 AND volume_26: prior completed bar target 0%; next bar open simulation |
| v1 | breakout_8 + volume_26 | 9580.79 | -419.21 | buy /  / breakout_8 + volume_26: prior completed bar target 50%; next bar open simulation |
| v1 | reversion_12 AND volume_26 | 9791.68 | -208.32 | sell /  / reversion_12 AND volume_26: prior completed bar target 0%; next bar open simulation |
| v1 | reversion_12 + volume_26 | 9541.30 | -458.70 | buy /  / reversion_12 + volume_26: prior completed bar target 50%; next bar open simulation |
| v1 | ema_12_26 | 9439.49 | -560.51 | sell /  / EMA12 > EMA26; 조건 미충족; EMA12=723.809, EMA26=723.847 |
| v1 | macd_12_26_9 | 9765.43 | -234.57 | sell /  / MACD > 신호선 그리고 MACD > 0; 조건 미충족; MACD=1.7811, signal9=1.82319 |
| v1 | rsi_14_recovery | 9689.26 | -310.74 | sell /  / 직전 RSI14 < 30, 현재 RSI14 >= 30 (한 봉 목표); 조건 미충족; RSI14=36.3006, previous_RSI14=36.7413 |
| v1 | bollinger_20_reentry | 9823.48 | -176.52 | sell /  / 직전 종가 < 직전 하단밴드, 현재 하단밴드 <= 종가 <= SMA20 (한 봉 목표); 조건 미충족; close=706.995, lower20=705.434, SMA20=720.761, previous_lower20=707.596 |
| v1 | donchian_20 | 9889.14 | -110.86 | sell /  / 종가 > 현재 봉을 제외한 직전 20봉 최고가; 조건 미충족; close=726.885, prior_high20=727.77 |
| v1 | atr_14_breakout | 9856.25 | -143.75 | sell /  / 종가 > 직전 종가 + 직전 ATR14 그리고 종가 > EMA26; 조건 미충족; close=708.502, threshold=710.044, prior_ATR14=2.19397, EMA26=707.552 |
| v1 | session_vwap | 9423.67 | -576.33 | buy /  / 종가 > 뉴욕 거래일별 누적 전형가격 VWAP; 조건 충족; close=704.41, session_VWAP=703.356, session_volume=4.32363e+06 |
| v1 | obv_20 | 9451.27 | -548.73 | sell /  / OBV > OBV의 SMA20 그리고 종가 > EMA26; 조건 미충족; OBV=3.90948e+08, OBV_SMA20=4.41854e+08, close=707.03, EMA26=707.514 |
| v1 | stochastic_14_3_recovery | 9359.39 | -640.61 | sell /  / 직전 %K14 < 20에서 %K14가 %D3 상향 돌파 (한 봉 목표); 조건 미충족; K14=55.2721, D3=32.1738, previous_K14=36.3025, previous_D3=23.7941 |
| v1 | mfi_14_recovery | 9740.78 | -259.22 | sell /  / 직전 MFI14 < 20, 현재 MFI14 >= 20 (한 봉 목표); 조건 미충족; MFI14=27.2489, previous_MFI14=20.9918 |
| v1 | adx_14_trend | 9825.33 | -174.67 | sell /  / Wilder ADX14 >= 25 그리고 +DI14 > -DI14; 조건 미충족; ADX14=23.847, plus_DI14=27.825, minus_DI14=26.997 |
| v1 | aroon_25_trend | 9774.48 | -225.52 | sell /  / Aroon25 Up > 70 그리고 Down < 30 (동률이면 최신 극값); 조건 미충족; Aroon_up=68, Aroon_down=4 |
| v1 | cci_20_momentum | 9843.10 | -156.90 | buy /  / CCI20 > 100 (전형가격·평균절대편차); 조건 충족; CCI20=174.954 |
| v1 | williams_14_recovery | 9486.47 | -513.53 | sell /  / 직전 Williams %R14 < -80, 현재 >= -80 (한 봉 목표); 조건 미충족; Williams_R14=-44.7279, previous_R14=-63.6975 |
| v1 | cmf_20_accumulation | 9372.38 | -627.62 | sell /  / Chaikin Money Flow20 > 0.1; 조건 미충족; CMF20=0.0746924, volume20=2.59371e+08 |
| v1 | chaikin_3_10 | 9465.92 | -534.08 | sell /  / ADL의 EMA3 - EMA10 > 0 그리고 종가 > EMA26; 조건 미충족; Chaikin3_10=1.07496e+06, ADL=4.19762e+08, close=707.03, EMA26=707.514 |
| v1 | roc_10_momentum | 9961.33 | -38.67 | sell /  / 10봉 ROC > 1% 그리고 종가 > EMA26; 조건 미충족; ROC10_percent=0.681109, close=725.78, EMA26=721.667 |
| v1 | trix_15_trend | 9467.11 | -532.89 | sell /  / 15봉 삼중 EMA의 1봉 변화율 TRIX > 0 그리고 종가 > EMA26; 조건 미충족; TRIX15_percent=0.0245938, close=713.775, EMA26=723.847 |
| v1 | keltner_20_breakout | 9782.40 | -217.60 | sell /  / 종가 > EMA20 + 2 x Wilder ATR14; 조건 미충족; close=726.815, upper_Keltner=727.39, EMA20=724.295, ATR14=1.54727 |
| v1 | opening_range_30m | 9588.91 | -411.09 | buy /  / 뉴욕 09:30·09:45 두 완료 봉 최고가를 10:00 이후 종가가 돌파; 조건 충족; close=707.85, opening_high=705.64 |
| v2 | cash | 10000.00 | 0.00 | 대기 /  / 새 신호 대기 |
| v2 | buy_hold | 9432.05 | -567.95 | 중단: 손실 한도 / buy / partial / 직전 완료 봉 목표 비중 100%; 다음 봉 시가 가정 |
| v2 | trend_8_26 | 9482.77 | -517.23 | buy / partial / 직전 완료 봉 목표 비중 100%; 다음 봉 시가 가정 |
| v2 | momentum_26 | 9231.87 | -768.13 | sell / filled / 직전 완료 봉 목표 비중 0%; 다음 봉 시가 가정 |
| v2 | breakout_8 | 9182.60 | -817.40 | sell / filled / 직전 완료 봉 목표 비중 0%; 다음 봉 시가 가정 |
| v2 | reversion_12 | 9028.60 | -971.40 | sell / filled / 직전 완료 봉 목표 비중 0%; 다음 봉 시가 가정 |
| v2 | volume_26 | 9565.80 | -434.20 | 중단: 손실 한도 / sell / filled / 직전 완료 봉 목표 비중 0%; 다음 봉 시가 가정 |
| v2 | trend_8_26 AND momentum_26 | 9596.08 | -403.92 | sell / filled / 직전 완료 봉 목표 비중 0%; 다음 봉 시가 가정 |
| v2 | trend_8_26 + momentum_26 | 9395.96 | -604.04 | sell / filled / 직전 완료 봉 목표 비중 50%; 다음 봉 시가 가정 |
| v2 | trend_8_26 AND breakout_8 | 9840.07 | -159.93 | sell / filled / 직전 완료 봉 목표 비중 0%; 다음 봉 시가 가정 |
| v2 | trend_8_26 + breakout_8 | 9390.57 | -609.43 | buy / filled / 직전 완료 봉 목표 비중 50%; 다음 봉 시가 가정 |
| v2 | trend_8_26 AND reversion_12 | 9742.38 | -257.62 | sell / filled / 직전 완료 봉 목표 비중 0%; 다음 봉 시가 가정 |
| v2 | trend_8_26 + reversion_12 | 9291.69 | -708.31 | buy / filled / 직전 완료 봉 목표 비중 50%; 다음 봉 시가 가정 |
| v2 | trend_8_26 AND volume_26 | 9649.04 | -350.96 | buy / partial / 직전 완료 봉 목표 비중 100%; 다음 봉 시가 가정 |
| v2 | trend_8_26 + volume_26 | 9188.42 | -811.58 | buy / partial / 직전 완료 봉 목표 비중 100%; 다음 봉 시가 가정 |
| v2 | momentum_26 AND breakout_8 | 9591.37 | -408.63 | sell / filled / 직전 완료 봉 목표 비중 0%; 다음 봉 시가 가정 |
| v2 | momentum_26 + breakout_8 | 9226.79 | -773.21 | sell / filled / 직전 완료 봉 목표 비중 0%; 다음 봉 시가 가정 |
| v2 | momentum_26 AND reversion_12 | 9776.12 | -223.88 | sell / filled / 직전 완료 봉 목표 비중 0%; 다음 봉 시가 가정 |
| v2 | momentum_26 + reversion_12 | 9206.59 | -793.41 | sell / filled / 직전 완료 봉 목표 비중 0%; 다음 봉 시가 가정 |
| v2 | momentum_26 AND volume_26 | 9718.13 | -281.87 | sell / filled / 직전 완료 봉 목표 비중 0%; 다음 봉 시가 가정 |
| v2 | momentum_26 + volume_26 | 9085.10 | -914.90 | buy / filled / 직전 완료 봉 목표 비중 50%; 다음 봉 시가 가정 |
| v2 | breakout_8 AND reversion_12 | 10000.00 | 0.00 | 대기 /  / 새 신호 대기 |
| v2 | breakout_8 + reversion_12 | 9200.93 | -799.07 | sell / filled / 직전 완료 봉 목표 비중 0%; 다음 봉 시가 가정 |
| v2 | breakout_8 AND volume_26 | 9871.76 | -128.24 | sell / filled / 직전 완료 봉 목표 비중 0%; 다음 봉 시가 가정 |
| v2 | breakout_8 + volume_26 | 9156.31 | -843.69 | buy / filled / 직전 완료 봉 목표 비중 50%; 다음 봉 시가 가정 |
| v2 | reversion_12 AND volume_26 | 9547.64 | -452.36 | 중단: 손실 한도 / sell / filled / 직전 완료 봉 목표 비중 0%; 다음 봉 시가 가정 |
| v2 | reversion_12 + volume_26 | 9022.24 | -977.76 | buy / filled / 직전 완료 봉 목표 비중 50%; 다음 봉 시가 가정 |
| v2 | ema_12_26 | 9430.06 | -569.94 | sell / filled / EMA12 > EMA26; 조건 미충족; EMA12=723.809, EMA26=723.847; 직전 완료 봉 목표를 다음 봉 시가에 모의 적용 |
| v2 | macd_12_26_9 | 9755.67 | -244.33 | sell / filled / MACD > 신호선 그리고 MACD > 0; 조건 미충족; MACD=1.7811, signal9=1.82319; 직전 완료 봉 목표를 다음 봉 시가에 모의 적용 |
| v2 | rsi_14_recovery | 9675.71 | -324.29 | sell / filled / 직전 RSI14 < 30, 현재 RSI14 >= 30 (한 봉 목표); 조건 미충족; RSI14=36.3006, previous_RSI14=36.7413; 직전 완료 봉 목표를 다음 봉 시가에 모의 적용 |
| v2 | bollinger_20_reentry | 9815.62 | -184.38 | sell / filled / 직전 종가 < 직전 하단밴드, 현재 하단밴드 <= 종가 <= SMA20 (한 봉 목표); 조건 미충족; close=706.995, lower20=705.434, SMA20=720.761, previous_lower20=707.596; 직전 완료 봉 목표를 다음 봉 시가에 모의 적용 |
| v2 | donchian_20 | 9881.23 | -118.77 | sell / filled / 종가 > 현재 봉을 제외한 직전 20봉 최고가; 조건 미충족; close=726.885, prior_high20=727.77; 직전 완료 봉 목표를 다음 봉 시가에 모의 적용 |
| v2 | atr_14_breakout | 9846.40 | -153.60 | sell / filled / 종가 > 직전 종가 + 직전 ATR14 그리고 종가 > EMA26; 조건 미충족; close=708.502, threshold=710.044, prior_ATR14=2.19397, EMA26=707.552; 직전 완료 봉 목표를 다음 봉 시가에 모의 적용 |
| v2 | session_vwap | 9403.90 | -596.10 | buy / partial / 종가 > 뉴욕 거래일별 누적 전형가격 VWAP; 조건 충족; close=704.41, session_VWAP=703.356, session_volume=4.32363e+06; 직전 완료 봉 목표를 다음 봉 시가에 모의 적용 |
| v2 | obv_20 | 9436.16 | -563.84 | sell / filled / OBV > OBV의 SMA20 그리고 종가 > EMA26; 조건 미충족; OBV=3.90948e+08, OBV_SMA20=4.41854e+08, close=707.03, EMA26=707.514; 직전 완료 봉 목표를 다음 봉 시가에 모의 적용 |
| v2 | stochastic_14_3_recovery | 9694.13 | -305.87 | 중단: 손실 한도 / sell / filled / 직전 %K14 < 20에서 %K14가 %D3 상향 돌파 (한 봉 목표); 조건 미충족; K14=10.576, D3=8.00581, previous_K14=7.39787, previous_D3=7.27486; 직전 완료 봉 목표를 다음 봉 시가에 모의 적용 |
| v2 | mfi_14_recovery | 9732.99 | -267.01 | sell / filled / 직전 MFI14 < 20, 현재 MFI14 >= 20 (한 봉 목표); 조건 미충족; MFI14=27.2489, previous_MFI14=20.9918; 직전 완료 봉 목표를 다음 봉 시가에 모의 적용 |
| v2 | adx_14_trend | 9817.47 | -182.53 | sell / filled / Wilder ADX14 >= 25 그리고 +DI14 > -DI14; 조건 미충족; ADX14=23.847, plus_DI14=27.825, minus_DI14=26.997; 직전 완료 봉 목표를 다음 봉 시가에 모의 적용 |
| v2 | aroon_25_trend | 9766.66 | -233.34 | sell / filled / Aroon25 Up > 70 그리고 Down < 30 (동률이면 최신 극값); 조건 미충족; Aroon_up=68, Aroon_down=4; 직전 완료 봉 목표를 다음 봉 시가에 모의 적용 |
| v2 | cci_20_momentum | 9832.28 | -167.72 | buy / partial / CCI20 > 100 (전형가격·평균절대편차); 조건 충족; CCI20=174.954; 직전 완료 봉 목표를 다음 봉 시가에 모의 적용 |
| v2 | williams_14_recovery | 9459.95 | -540.05 | sell / filled / 직전 Williams %R14 < -80, 현재 >= -80 (한 봉 목표); 조건 미충족; Williams_R14=-44.7279, previous_R14=-63.6975; 직전 완료 봉 목표를 다음 봉 시가에 모의 적용 |
| v2 | cmf_20_accumulation | 9355.52 | -644.48 | sell / filled / Chaikin Money Flow20 > 0.1; 조건 미충족; CMF20=0.0746924, volume20=2.59371e+08; 직전 완료 봉 목표를 다음 봉 시가에 모의 적용 |
| v2 | chaikin_3_10 | 9450.79 | -549.21 | sell / filled / ADL의 EMA3 - EMA10 > 0 그리고 종가 > EMA26; 조건 미충족; Chaikin3_10=1.07496e+06, ADL=4.19762e+08, close=707.03, EMA26=707.514; 직전 완료 봉 목표를 다음 봉 시가에 모의 적용 |
| v2 | roc_10_momentum | 9957.34 | -42.66 | sell / filled / 10봉 ROC > 1% 그리고 종가 > EMA26; 조건 미충족; ROC10_percent=0.681109, close=725.78, EMA26=721.667; 직전 완료 봉 목표를 다음 봉 시가에 모의 적용 |
| v2 | trix_15_trend | 9453.87 | -546.13 | sell / filled / 15봉 삼중 EMA의 1봉 변화율 TRIX > 0 그리고 종가 > EMA26; 조건 미충족; TRIX15_percent=0.0245938, close=713.775, EMA26=723.847; 직전 완료 봉 목표를 다음 봉 시가에 모의 적용 |
| v2 | keltner_20_breakout | 9772.62 | -227.38 | sell / filled / 종가 > EMA20 + 2 x Wilder ATR14; 조건 미충족; close=726.815, upper_Keltner=727.39, EMA20=724.295, ATR14=1.54727; 직전 완료 봉 목표를 다음 봉 시가에 모의 적용 |
| v2 | opening_range_30m | 9578.37 | -421.63 | buy / partial / 뉴욕 09:30·09:45 두 완료 봉 최고가를 10:00 이후 종가가 돌파; 조건 충족; close=707.85, opening_high=705.64; 직전 완료 봉 목표를 다음 봉 시가에 모의 적용 |

### 같은 기간의 비용·노출 비교 (사후 연구)

| 전략 | 비용 전 | 비용 후 | 100% 보유 | 같은 평균 노출 보유 | 평균 노출 |
|---|---:|---:|---:|---:|---:|
| cash | 0.00% | 0.00% | -5.77% | -0.00% | 0.00% |
| buy_hold | -5.37% | -5.77% | -5.77% | -5.77% | 100.00% |
| trend_8_26 | -1.98% | -6.01% | -5.77% | -2.23% | 38.16% |
| momentum_26 | -3.78% | -9.27% | -5.77% | -2.01% | 34.47% |
| breakout_8 | -2.08% | -17.22% | -5.77% | -1.11% | 18.95% |
| reversion_12 | -0.54% | -12.68% | -5.77% | -1.89% | 32.37% |
| volume_26 | -0.32% | -15.38% | -5.77% | -1.06% | 18.16% |
| trend_8_26 AND momentum_26 | -0.95% | -4.62% | -5.77% | -1.63% | 27.89% |
| trend_8_26 + momentum_26 | -2.88% | -7.07% | -5.77% | -2.12% | 36.32% |
| trend_8_26 AND breakout_8 | 0.25% | -7.44% | -5.77% | -0.63% | 10.79% |
| trend_8_26 + breakout_8 | -2.02% | -11.05% | -5.77% | -1.67% | 28.56% |
| trend_8_26 AND reversion_12 | -0.34% | -3.63% | -5.77% | -0.32% | 5.53% |
| trend_8_26 + reversion_12 | -1.25% | -8.84% | -5.77% | -2.06% | 35.27% |
| trend_8_26 AND volume_26 | 0.45% | -4.89% | -5.77% | -0.32% | 5.53% |
| trend_8_26 + volume_26 | -1.15% | -10.82% | -5.77% | -1.65% | 28.16% |
| momentum_26 AND breakout_8 | -0.53% | -8.93% | -5.77% | -0.65% | 11.05% |
| momentum_26 + breakout_8 | -2.92% | -12.97% | -5.77% | -1.56% | 26.72% |
| momentum_26 AND reversion_12 | -1.16% | -4.83% | -5.77% | -0.32% | 5.53% |
| momentum_26 + reversion_12 | -2.16% | -10.06% | -5.77% | -1.95% | 33.43% |
| momentum_26 AND volume_26 | -0.37% | -4.07% | -5.77% | -0.22% | 3.68% |
| momentum_26 + volume_26 | -2.06% | -12.02% | -5.77% | -1.54% | 26.32% |
| breakout_8 AND reversion_12 | 0.00% | 0.00% | -5.77% | -0.00% | 0.00% |
| breakout_8 + reversion_12 | -1.30% | -13.91% | -5.77% | -1.50% | 25.67% |
| breakout_8 AND volume_26 | 0.32% | -2.18% | -5.77% | -0.14% | 2.37% |
| breakout_8 + volume_26 | -1.20% | -14.54% | -5.77% | -1.09% | 18.56% |
| reversion_12 AND volume_26 | -1.12% | -8.70% | -5.77% | -0.53% | 8.95% |
| reversion_12 + volume_26 | -0.42% | -13.51% | -5.77% | -1.48% | 25.27% |
| ema_12_26 | -3.52% | -6.31% | -5.77% | -2.01% | 34.47% |
| macd_12_26_9 | -0.46% | -4.55% | -5.77% | -1.20% | 20.53% |
| rsi_14_recovery | -0.50% | -6.97% | -5.77% | -0.25% | 4.21% |
| bollinger_20_reentry | -0.05% | -5.76% | -5.77% | -0.22% | 3.68% |
| donchian_20 | 0.40% | -4.93% | -5.77% | -0.32% | 5.53% |
| atr_14_breakout | 0.37% | -3.75% | -5.77% | -0.17% | 2.89% |
| session_vwap | -2.83% | -14.33% | -5.77% | -2.73% | 46.84% |
| obv_20 | -3.77% | -12.26% | -5.77% | -1.34% | 22.89% |
| stochastic_14_3_recovery | 0.14% | -12.82% | -5.77% | -0.51% | 8.68% |
| mfi_14_recovery | -1.13% | -3.99% | -5.77% | -0.11% | 1.84% |
| adx_14_trend | 0.42% | -2.08% | -5.77% | -1.13% | 19.21% |
| aroon_25_trend | 0.17% | -2.73% | -5.77% | -0.85% | 14.47% |
| cci_20_momentum | 0.59% | -4.36% | -5.77% | -1.03% | 17.63% |
| williams_14_recovery | -0.17% | -11.61% | -5.77% | -0.45% | 7.63% |
| cmf_20_accumulation | -2.56% | -9.66% | -5.77% | -2.03% | 34.74% |
| chaikin_3_10 | -4.89% | -12.92% | -5.77% | -1.62% | 27.63% |
| roc_10_momentum | 0.41% | -0.43% | -5.77% | -0.17% | 2.89% |
| trix_15_trend | -2.40% | -6.02% | -5.77% | -1.68% | 28.68% |
| keltner_20_breakout | -0.51% | -5.00% | -5.77% | -0.42% | 7.11% |
| opening_range_30m | -1.46% | -6.70% | -5.77% | -2.05% | 35.00% |

동일 구간·초기 자금, 종료 시 청산 비용 포함. 노출 맞춤은 사후 설명용이며 v2 실제 계좌 성과가 아닙니다.
[낙폭 분해·비용 영향·전체 구간](QQQ/comparison.json)

[v1 전체 기록](QQQ/accounts.json) · [v2 전체 기록](QQQ/accounts-v2.json)

## IWM 계좌

| 모델 | 전략 | 평가액 USD | 손익 USD | 최근 매매·이유 |
|---|---|---:|---:|---|
| v1 | cash | 10000.00 | 0.00 | 대기 /  / 새 신호 대기 |
| v1 | buy_hold | 10003.76 | 3.76 | buy /  / buy_hold: prior completed bar target 100%; next bar open simulation |
| v1 | trend_8_26 | 9680.21 | -319.79 | sell /  / trend_8_26: prior completed bar target 0%; next bar open simulation |
| v1 | momentum_26 | 9717.25 | -282.75 | buy /  / momentum_26: prior completed bar target 100%; next bar open simulation |
| v1 | breakout_8 | 9262.03 | -737.97 | sell /  / breakout_8: prior completed bar target 0%; next bar open simulation |
| v1 | reversion_12 | 9713.04 | -286.96 | sell /  / reversion_12: prior completed bar target 0%; next bar open simulation |
| v1 | volume_26 | 9851.14 | -148.86 | sell /  / volume_26: prior completed bar target 0%; next bar open simulation |
| v1 | trend_8_26 AND momentum_26 | 9699.16 | -300.84 | sell /  / trend_8_26 AND momentum_26: prior completed bar target 0%; next bar open simulation |
| v1 | trend_8_26 + momentum_26 | 9718.23 | -281.77 | buy /  / trend_8_26 + momentum_26: prior completed bar target 50%; next bar open simulation |
| v1 | trend_8_26 AND breakout_8 | 9404.46 | -595.54 | sell /  / trend_8_26 AND breakout_8: prior completed bar target 0%; next bar open simulation |
| v1 | trend_8_26 + breakout_8 | 9469.06 | -530.94 | sell /  / trend_8_26 + breakout_8: prior completed bar target 0%; next bar open simulation |
| v1 | trend_8_26 AND reversion_12 | 9755.06 | -244.94 | sell /  / trend_8_26 AND reversion_12: prior completed bar target 0%; next bar open simulation |
| v1 | trend_8_26 + reversion_12 | 9696.40 | -303.60 | sell /  / trend_8_26 + reversion_12: prior completed bar target 0%; next bar open simulation |
| v1 | trend_8_26 AND volume_26 | 9893.73 | -106.27 | sell /  / trend_8_26 AND volume_26: prior completed bar target 0%; next bar open simulation |
| v1 | trend_8_26 + volume_26 | 9784.70 | -215.30 | sell /  / trend_8_26 + volume_26: prior completed bar target 0%; next bar open simulation |
| v1 | momentum_26 AND breakout_8 | 9478.36 | -521.64 | sell /  / momentum_26 AND breakout_8: prior completed bar target 0%; next bar open simulation |
| v1 | momentum_26 + breakout_8 | 9506.05 | -493.95 | buy /  / momentum_26 + breakout_8: prior completed bar target 50%; next bar open simulation |
| v1 | momentum_26 AND reversion_12 | 9876.67 | -123.33 | sell /  / momentum_26 AND reversion_12: prior completed bar target 0%; next bar open simulation |
| v1 | momentum_26 + reversion_12 | 9812.56 | -187.44 | buy /  / momentum_26 + reversion_12: prior completed bar target 50%; next bar open simulation |
| v1 | momentum_26 AND volume_26 | 9928.27 | -71.73 | sell /  / momentum_26 AND volume_26: prior completed bar target 0%; next bar open simulation |
| v1 | momentum_26 + volume_26 | 9823.08 | -176.92 | buy /  / momentum_26 + volume_26: prior completed bar target 50%; next bar open simulation |
| v1 | breakout_8 AND reversion_12 | 10000.00 | 0.00 | 대기 /  / 새 신호 대기 |
| v1 | breakout_8 + reversion_12 | 9522.63 | -477.37 | sell /  / breakout_8 + reversion_12: prior completed bar target 0%; next bar open simulation |
| v1 | breakout_8 AND volume_26 | 9918.46 | -81.54 | sell /  / breakout_8 AND volume_26: prior completed bar target 0%; next bar open simulation |
| v1 | breakout_8 + volume_26 | 9571.11 | -428.89 | sell /  / breakout_8 + volume_26: prior completed bar target 0%; next bar open simulation |
| v1 | reversion_12 AND volume_26 | 9912.42 | -87.58 | sell /  / reversion_12 AND volume_26: prior completed bar target 0%; next bar open simulation |
| v1 | reversion_12 + volume_26 | 9821.00 | -179.00 | sell /  / reversion_12 + volume_26: prior completed bar target 0%; next bar open simulation |
| v1 | ema_12_26 | 9767.13 | -232.87 | sell /  / EMA12 > EMA26; 조건 미충족; EMA12=275.878, EMA26=275.963 |
| v1 | macd_12_26_9 | 9857.89 | -142.11 | sell /  / MACD > 신호선 그리고 MACD > 0; 조건 미충족; MACD=-0.0844159, signal9=-0.0555294 |
| v1 | rsi_14_recovery | 9786.95 | -213.05 | sell /  / 직전 RSI14 < 30, 현재 RSI14 >= 30 (한 봉 목표); 조건 미충족; RSI14=46.986, previous_RSI14=37.1649 |
| v1 | bollinger_20_reentry | 9762.11 | -237.89 | sell /  / 직전 종가 < 직전 하단밴드, 현재 하단밴드 <= 종가 <= SMA20 (한 봉 목표); 조건 미충족; close=275.725, lower20=274.173, SMA20=275.605, previous_lower20=274.15 |
| v1 | donchian_20 | 9835.91 | -164.09 | sell /  / 종가 > 현재 봉을 제외한 직전 20봉 최고가; 조건 미충족; close=275.785, prior_high20=276.875 |
| v1 | atr_14_breakout | 9685.22 | -314.78 | sell /  / 종가 > 직전 종가 + 직전 ATR14 그리고 종가 > EMA26; 조건 미충족; close=274.63, threshold=277.369, prior_ATR14=0.659199, EMA26=275.963 |
| v1 | session_vwap | 9261.90 | -738.10 | buy /  / 종가 > 뉴욕 거래일별 누적 전형가격 VWAP; 조건 충족; close=275.03, session_VWAP=274.45, session_volume=6.20261e+06 |
| v1 | obv_20 | 9624.91 | -375.09 | sell /  / OBV > OBV의 SMA20 그리고 종가 > EMA26; 조건 미충족; OBV=-2.65101e+07, OBV_SMA20=-2.63464e+07, close=274.63, EMA26=275.963 |
| v1 | stochastic_14_3_recovery | 9613.95 | -386.05 | sell /  / 직전 %K14 < 20에서 %K14가 %D3 상향 돌파 (한 봉 목표); 조건 미충족; K14=68.0001, D3=43.5239, previous_K14=48.1428, previous_D3=23.7507 |
| v1 | mfi_14_recovery | 9934.22 | -65.78 | sell /  / 직전 MFI14 < 20, 현재 MFI14 >= 20 (한 봉 목표); 조건 미충족; MFI14=34.131, previous_MFI14=22.0435 |
| v1 | adx_14_trend | 9726.05 | -273.95 | sell /  / Wilder ADX14 >= 25 그리고 +DI14 > -DI14; 조건 미충족; ADX14=27.8461, plus_DI14=25.882, minus_DI14=28.4558 |
| v1 | aroon_25_trend | 9745.85 | -254.15 | sell /  / Aroon25 Up > 70 그리고 Down < 30 (동률이면 최신 극값); 조건 미충족; Aroon_up=68, Aroon_down=4 |
| v1 | cci_20_momentum | 9722.50 | -277.50 | sell /  / CCI20 > 100 (전형가격·평균절대편차); 조건 미충족; CCI20=-314.625 |
| v1 | williams_14_recovery | 9742.36 | -257.64 | sell /  / 직전 Williams %R14 < -80, 현재 >= -80 (한 봉 목표); 조건 미충족; Williams_R14=-31.9999, previous_R14=-51.8572 |
| v1 | cmf_20_accumulation | 9680.43 | -319.57 | buy /  / Chaikin Money Flow20 > 0.1; 조건 충족; CMF20=0.23674, volume20=1.30084e+07 |
| v1 | chaikin_3_10 | 9419.10 | -580.90 | buy /  / ADL의 EMA3 - EMA10 > 0 그리고 종가 > EMA26; 조건 충족; Chaikin3_10=1.00567e+06, ADL=-2.66275e+07, close=275.85, EMA26=275.595 |
| v1 | roc_10_momentum | 9996.39 | -3.61 | sell /  / 10봉 ROC > 1% 그리고 종가 > EMA26; 조건 미충족; ROC10_percent=0.995963, close=275.315, EMA26=273.754 |
| v1 | trix_15_trend | 9811.92 | -188.08 | sell /  / 15봉 삼중 EMA의 1봉 변화율 TRIX > 0 그리고 종가 > EMA26; 조건 미충족; TRIX15_percent=0.00744142, close=276.06, EMA26=276.447 |
| v1 | keltner_20_breakout | 9879.23 | -120.77 | sell /  / 종가 > EMA20 + 2 x Wilder ATR14; 조건 미충족; close=276.4, upper_Keltner=277.094, EMA20=275.768, ATR14=0.662947 |
| v1 | opening_range_30m | 9960.03 | -39.97 | buy /  / 뉴욕 09:30·09:45 두 완료 봉 최고가를 10:00 이후 종가가 돌파; 조건 충족; close=275.725, opening_high=275.24 |
| v2 | cash | 10000.00 | 0.00 | 대기 /  / 새 신호 대기 |
| v2 | buy_hold | 9896.79 | -103.21 | buy / partial / 직전 완료 봉 목표 비중 100%; 다음 봉 시가 가정 |
| v2 | trend_8_26 | 9548.09 | -451.91 | sell / filled / 직전 완료 봉 목표 비중 0%; 다음 봉 시가 가정 |
| v2 | momentum_26 | 9578.90 | -421.10 | buy / partial / 직전 완료 봉 목표 비중 100%; 다음 봉 시가 가정 |
| v2 | breakout_8 | 9006.34 | -993.66 | 중단: 손실 한도 / buy / partial / 직전 완료 봉 목표 비중 100%; 다음 봉 시가 가정 |
| v2 | reversion_12 | 9246.43 | -753.57 | sell / filled / 직전 완료 봉 목표 비중 0%; 다음 봉 시가 가정 |
| v2 | volume_26 | 9360.51 | -639.49 | sell / filled / 직전 완료 봉 목표 비중 0%; 다음 봉 시가 가정 |
| v2 | trend_8_26 AND momentum_26 | 9711.39 | -288.61 | sell / filled / 직전 완료 봉 목표 비중 0%; 다음 봉 시가 가정 |
| v2 | trend_8_26 + momentum_26 | 9603.96 | -396.04 | buy / filled / 직전 완료 봉 목표 비중 50%; 다음 봉 시가 가정 |
| v2 | trend_8_26 AND breakout_8 | 9300.05 | -699.95 | sell / filled / 직전 완료 봉 목표 비중 0%; 다음 봉 시가 가정 |
| v2 | trend_8_26 + breakout_8 | 9227.46 | -772.54 | sell / filled / 직전 완료 봉 목표 비중 0%; 다음 봉 시가 가정 |
| v2 | trend_8_26 AND reversion_12 | 9630.14 | -369.86 | sell / filled / 직전 완료 봉 목표 비중 0%; 다음 봉 시가 가정 |
| v2 | trend_8_26 + reversion_12 | 9395.66 | -604.34 | sell / filled / 직전 완료 봉 목표 비중 0%; 다음 봉 시가 가정 |
| v2 | trend_8_26 AND volume_26 | 9752.17 | -247.83 | sell / filled / 직전 완료 봉 목표 비중 0%; 다음 봉 시가 가정 |
| v2 | trend_8_26 + volume_26 | 9493.44 | -506.56 | sell / filled / 직전 완료 봉 목표 비중 0%; 다음 봉 시가 가정 |
| v2 | momentum_26 AND breakout_8 | 9271.16 | -728.84 | sell / filled / 직전 완료 봉 목표 비중 0%; 다음 봉 시가 가정 |
| v2 | momentum_26 + breakout_8 | 9242.11 | -757.89 | buy / filled / 직전 완료 봉 목표 비중 50%; 다음 봉 시가 가정 |
| v2 | momentum_26 AND reversion_12 | 9831.84 | -168.16 | sell / filled / 직전 완료 봉 목표 비중 0%; 다음 봉 시가 가정 |
| v2 | momentum_26 + reversion_12 | 9529.91 | -470.09 | buy / filled / 직전 완료 봉 목표 비중 50%; 다음 봉 시가 가정 |
| v2 | momentum_26 AND volume_26 | 9818.94 | -181.06 | sell / filled / 직전 완료 봉 목표 비중 0%; 다음 봉 시가 가정 |
| v2 | momentum_26 + volume_26 | 9508.60 | -491.40 | buy / filled / 직전 완료 봉 목표 비중 50%; 다음 봉 시가 가정 |
| v2 | breakout_8 AND reversion_12 | 10000.00 | 0.00 | 대기 /  / 새 신호 대기 |
| v2 | breakout_8 + reversion_12 | 9136.90 | -863.10 | sell / filled / 직전 완료 봉 목표 비중 0%; 다음 봉 시가 가정 |
| v2 | breakout_8 AND volume_26 | 9660.76 | -339.24 | sell / filled / 직전 완료 봉 목표 비중 0%; 다음 봉 시가 가정 |
| v2 | breakout_8 + volume_26 | 9155.07 | -844.93 | sell / filled / 직전 완료 봉 목표 비중 0%; 다음 봉 시가 가정 |
| v2 | reversion_12 AND volume_26 | 9647.72 | -352.28 | sell / filled / 직전 완료 봉 목표 비중 0%; 다음 봉 시가 가정 |
| v2 | reversion_12 + volume_26 | 9361.82 | -638.18 | sell / filled / 직전 완료 봉 목표 비중 0%; 다음 봉 시가 가정 |
| v2 | ema_12_26 | 9759.32 | -240.68 | sell / filled / EMA12 > EMA26; 조건 미충족; EMA12=275.878, EMA26=275.963; 직전 완료 봉 목표를 다음 봉 시가에 모의 적용 |
| v2 | macd_12_26_9 | 9850.01 | -149.99 | sell / filled / MACD > 신호선 그리고 MACD > 0; 조건 미충족; MACD=-0.0844159, signal9=-0.0555294; 직전 완료 봉 목표를 다음 봉 시가에 모의 적용 |
| v2 | rsi_14_recovery | 9779.12 | -220.88 | sell / filled / 직전 RSI14 < 30, 현재 RSI14 >= 30 (한 봉 목표); 조건 미충족; RSI14=46.986, previous_RSI14=37.1649; 직전 완료 봉 목표를 다음 봉 시가에 모의 적용 |
| v2 | bollinger_20_reentry | 9750.40 | -249.60 | sell / filled / 직전 종가 < 직전 하단밴드, 현재 하단밴드 <= 종가 <= SMA20 (한 봉 목표); 조건 미충족; close=275.725, lower20=274.173, SMA20=275.605, previous_lower20=274.15; 직전 완료 봉 목표를 다음 봉 시가에 모의 적용 |
| v2 | donchian_20 | 9830.01 | -169.99 | sell / filled / 종가 > 현재 봉을 제외한 직전 20봉 최고가; 조건 미충족; close=275.785, prior_high20=276.875; 직전 완료 봉 목표를 다음 봉 시가에 모의 적용 |
| v2 | atr_14_breakout | 9669.74 | -330.26 | sell / filled / 종가 > 직전 종가 + 직전 ATR14 그리고 종가 > EMA26; 조건 미충족; close=274.63, threshold=277.369, prior_ATR14=0.659199, EMA26=275.963; 직전 완료 봉 목표를 다음 봉 시가에 모의 적용 |
| v2 | session_vwap | 9229.54 | -770.46 | buy / partial / 종가 > 뉴욕 거래일별 누적 전형가격 VWAP; 조건 충족; close=275.03, session_VWAP=274.45, session_volume=6.20261e+06; 직전 완료 봉 목표를 다음 봉 시가에 모의 적용 |
| v2 | obv_20 | 9607.61 | -392.39 | sell / filled / OBV > OBV의 SMA20 그리고 종가 > EMA26; 조건 미충족; OBV=-2.65101e+07, OBV_SMA20=-2.63464e+07, close=274.63, EMA26=275.963; 직전 완료 봉 목표를 다음 봉 시가에 모의 적용 |
| v2 | stochastic_14_3_recovery | 9594.74 | -405.26 | sell / filled / 직전 %K14 < 20에서 %K14가 %D3 상향 돌파 (한 봉 목표); 조건 미충족; K14=68.0001, D3=43.5239, previous_K14=48.1428, previous_D3=23.7507; 직전 완료 봉 목표를 다음 봉 시가에 모의 적용 |
| v2 | mfi_14_recovery | 9930.25 | -69.75 | sell / filled / 직전 MFI14 < 20, 현재 MFI14 >= 20 (한 봉 목표); 조건 미충족; MFI14=34.131, previous_MFI14=22.0435; 직전 완료 봉 목표를 다음 봉 시가에 모의 적용 |
| v2 | adx_14_trend | 9718.27 | -281.73 | sell / filled / Wilder ADX14 >= 25 그리고 +DI14 > -DI14; 조건 미충족; ADX14=27.8461, plus_DI14=25.882, minus_DI14=28.4558; 직전 완료 봉 목표를 다음 봉 시가에 모의 적용 |
| v2 | aroon_25_trend | 9736.11 | -263.89 | sell / filled / Aroon25 Up > 70 그리고 Down < 30 (동률이면 최신 극값); 조건 미충족; Aroon_up=68, Aroon_down=4; 직전 완료 봉 목표를 다음 봉 시가에 모의 적용 |
| v2 | cci_20_momentum | 9708.90 | -291.10 | sell / filled / CCI20 > 100 (전형가격·평균절대편차); 조건 미충족; CCI20=-314.625; 직전 완료 봉 목표를 다음 봉 시가에 모의 적용 |
| v2 | williams_14_recovery | 9726.79 | -273.21 | sell / filled / 직전 Williams %R14 < -80, 현재 >= -80 (한 봉 목표); 조건 미충족; Williams_R14=-31.9999, previous_R14=-51.8572; 직전 완료 봉 목표를 다음 봉 시가에 모의 적용 |
| v2 | cmf_20_accumulation | 9662.05 | -337.95 | buy / partial / Chaikin Money Flow20 > 0.1; 조건 충족; CMF20=0.23674, volume20=1.30084e+07; 직전 완료 봉 목표를 다음 봉 시가에 모의 적용 |
| v2 | chaikin_3_10 | 9393.70 | -606.30 | buy / partial / ADL의 EMA3 - EMA10 > 0 그리고 종가 > EMA26; 조건 충족; Chaikin3_10=1.00567e+06, ADL=-2.66275e+07, close=275.85, EMA26=275.595; 직전 완료 봉 목표를 다음 봉 시가에 모의 적용 |
| v2 | roc_10_momentum | 9994.39 | -5.61 | sell / filled / 10봉 ROC > 1% 그리고 종가 > EMA26; 조건 미충족; ROC10_percent=0.995963, close=275.315, EMA26=273.754; 직전 완료 봉 목표를 다음 봉 시가에 모의 적용 |
| v2 | trix_15_trend | 9804.07 | -195.93 | sell / filled / 15봉 삼중 EMA의 1봉 변화율 TRIX > 0 그리고 종가 > EMA26; 조건 미충족; TRIX15_percent=0.00744142, close=276.06, EMA26=276.447; 직전 완료 봉 목표를 다음 봉 시가에 모의 적용 |
| v2 | keltner_20_breakout | 9873.30 | -126.70 | sell / filled / 종가 > EMA20 + 2 x Wilder ATR14; 조건 미충족; close=276.4, upper_Keltner=277.094, EMA20=275.768, ATR14=0.662947; 직전 완료 봉 목표를 다음 봉 시가에 모의 적용 |
| v2 | opening_range_30m | 9955.05 | -44.95 | buy / partial / 뉴욕 09:30·09:45 두 완료 봉 최고가를 10:00 이후 종가가 돌파; 조건 충족; close=275.725, opening_high=275.24; 직전 완료 봉 목표를 다음 봉 시가에 모의 적용 |

### 같은 기간의 비용·노출 비교 (사후 연구)

| 전략 | 비용 전 | 비용 후 | 100% 보유 | 같은 평균 노출 보유 | 평균 노출 |
|---|---:|---:|---:|---:|---:|
| cash | 0.00% | 0.00% | -2.27% | -0.00% | 0.00% |
| buy_hold | -1.86% | -2.27% | -2.27% | -2.27% | 100.00% |
| trend_8_26 | -1.56% | -5.21% | -2.27% | -1.04% | 45.26% |
| momentum_26 | 0.53% | -5.61% | -2.27% | -1.00% | 43.68% |
| breakout_8 | -1.21% | -15.78% | -2.27% | -0.44% | 19.21% |
| reversion_12 | -0.95% | -12.31% | -2.27% | -0.63% | 27.37% |
| volume_26 | -0.45% | -8.08% | -2.27% | -0.21% | 8.95% |
| trend_8_26 AND momentum_26 | 0.28% | -3.44% | -2.27% | -0.84% | 36.58% |
| trend_8_26 + momentum_26 | -0.51% | -4.81% | -2.27% | -1.02% | 44.48% |
| trend_8_26 AND breakout_8 | -0.64% | -9.79% | -2.27% | -0.29% | 12.37% |
| trend_8_26 + breakout_8 | -1.38% | -10.46% | -2.27% | -0.74% | 32.24% |
| trend_8_26 AND reversion_12 | -0.94% | -4.61% | -2.27% | -0.13% | 5.53% |
| trend_8_26 + reversion_12 | -1.25% | -8.84% | -2.27% | -0.83% | 36.32% |
| trend_8_26 AND volume_26 | -0.31% | -3.61% | -2.27% | -0.07% | 2.89% |
| trend_8_26 + volume_26 | -1.00% | -6.27% | -2.27% | -0.62% | 27.11% |
| momentum_26 AND breakout_8 | 0.08% | -9.51% | -2.27% | -0.28% | 12.11% |
| momentum_26 + breakout_8 | -0.34% | -10.65% | -2.27% | -0.72% | 31.45% |
| momentum_26 AND reversion_12 | -0.35% | -2.42% | -2.27% | -0.05% | 2.37% |
| momentum_26 + reversion_12 | -0.20% | -7.49% | -2.27% | -0.82% | 35.53% |
| momentum_26 AND volume_26 | -0.08% | -3.38% | -2.27% | -0.06% | 2.63% |
| momentum_26 + volume_26 | 0.05% | -6.27% | -2.27% | -0.61% | 26.32% |
| breakout_8 AND reversion_12 | 0.00% | 0.00% | -2.27% | -0.00% | 0.00% |
| breakout_8 + reversion_12 | -1.07% | -13.17% | -2.27% | -0.54% | 23.30% |
| breakout_8 AND volume_26 | -0.63% | -3.91% | -2.27% | -0.05% | 2.37% |
| breakout_8 + volume_26 | -0.83% | -11.65% | -2.27% | -0.33% | 14.09% |
| reversion_12 AND volume_26 | 0.75% | -3.80% | -2.27% | -0.09% | 3.68% |
| reversion_12 + volume_26 | -0.69% | -9.47% | -2.27% | -0.42% | 18.16% |
| ema_12_26 | 0.41% | -2.50% | -2.27% | -1.03% | 45.00% |
| macd_12_26_9 | 2.22% | -0.32% | -2.27% | -0.53% | 23.16% |
| rsi_14_recovery | -0.88% | -4.95% | -2.27% | -0.06% | 2.63% |
| bollinger_20_reentry | -0.28% | -5.58% | -2.27% | -0.08% | 3.42% |
| donchian_20 | -0.07% | -4.58% | -2.27% | -0.13% | 5.53% |
| atr_14_breakout | -0.74% | -7.58% | -2.27% | -0.11% | 4.74% |
| session_vwap | -1.40% | -13.80% | -2.27% | -1.10% | 48.16% |
| obv_20 | -0.22% | -5.53% | -2.27% | -0.91% | 39.47% |
| stochastic_14_3_recovery | -0.09% | -12.29% | -2.27% | -0.19% | 8.16% |
| mfi_14_recovery | 0.20% | -3.92% | -2.27% | -0.06% | 2.63% |
| adx_14_trend | 0.33% | -2.17% | -2.27% | -0.70% | 30.53% |
| aroon_25_trend | -0.41% | -4.11% | -2.27% | -0.40% | 17.37% |
| cci_20_momentum | -0.93% | -7.76% | -2.27% | -0.43% | 18.68% |
| williams_14_recovery | 0.62% | -9.02% | -2.27% | -0.15% | 6.32% |
| cmf_20_accumulation | 0.22% | -6.69% | -2.27% | -0.61% | 26.32% |
| chaikin_3_10 | -1.58% | -10.27% | -2.27% | -0.83% | 36.05% |
| roc_10_momentum | 0.32% | -0.52% | -2.27% | -0.09% | 3.68% |
| trix_15_trend | 0.32% | -3.40% | -2.27% | -0.80% | 34.74% |
| keltner_20_breakout | 0.21% | -2.69% | -2.27% | -0.13% | 5.79% |
| opening_range_30m | 1.69% | -2.50% | -2.27% | -0.56% | 24.47% |

동일 구간·초기 자금, 종료 시 청산 비용 포함. 노출 맞춤은 사후 설명용이며 v2 실제 계좌 성과가 아닙니다.
[낙폭 분해·비용 영향·전체 구간](IWM/comparison.json)

[v1 전체 기록](IWM/accounts.json) · [v2 전체 기록](IWM/accounts-v2.json)

## DIA 계좌

| 모델 | 전략 | 평가액 USD | 손익 USD | 최근 매매·이유 |
|---|---|---:|---:|---|
| v1 | cash | 10000.00 | 0.00 | 대기 /  / 새 신호 대기 |
| v1 | buy_hold | 9984.61 | -15.39 | buy /  / buy_hold: prior completed bar target 100%; next bar open simulation |
| v1 | trend_8_26 | 9855.65 | -144.35 | sell /  / trend_8_26: prior completed bar target 0%; next bar open simulation |
| v1 | momentum_26 | 9668.66 | -331.34 | sell /  / momentum_26: prior completed bar target 0%; next bar open simulation |
| v1 | breakout_8 | 9293.36 | -706.64 | sell /  / breakout_8: prior completed bar target 0%; next bar open simulation |
| v1 | reversion_12 | 9792.90 | -207.10 | sell /  / reversion_12: prior completed bar target 0%; next bar open simulation |
| v1 | volume_26 | 9754.48 | -245.52 | sell /  / volume_26: prior completed bar target 0%; next bar open simulation |
| v1 | trend_8_26 AND momentum_26 | 9665.55 | -334.45 | sell /  / trend_8_26 AND momentum_26: prior completed bar target 0%; next bar open simulation |
| v1 | trend_8_26 + momentum_26 | 9761.79 | -238.21 | sell /  / trend_8_26 + momentum_26: prior completed bar target 0%; next bar open simulation |
| v1 | trend_8_26 AND breakout_8 | 9561.79 | -438.21 | sell /  / trend_8_26 AND breakout_8: prior completed bar target 0%; next bar open simulation |
| v1 | trend_8_26 + breakout_8 | 9628.01 | -371.99 | sell /  / trend_8_26 + breakout_8: prior completed bar target 0%; next bar open simulation |
| v1 | trend_8_26 AND reversion_12 | 9865.72 | -134.28 | sell /  / trend_8_26 AND reversion_12: prior completed bar target 0%; next bar open simulation |
| v1 | trend_8_26 + reversion_12 | 9843.68 | -156.32 | sell /  / trend_8_26 + reversion_12: prior completed bar target 0%; next bar open simulation |
| v1 | trend_8_26 AND volume_26 | 9839.32 | -160.68 | sell /  / trend_8_26 AND volume_26: prior completed bar target 0%; next bar open simulation |
| v1 | trend_8_26 + volume_26 | 9804.74 | -195.26 | sell /  / trend_8_26 + volume_26: prior completed bar target 0%; next bar open simulation |
| v1 | momentum_26 AND breakout_8 | 9420.05 | -579.95 | sell /  / momentum_26 AND breakout_8: prior completed bar target 0%; next bar open simulation |
| v1 | momentum_26 + breakout_8 | 9479.27 | -520.73 | sell /  / momentum_26 + breakout_8: prior completed bar target 0%; next bar open simulation |
| v1 | momentum_26 AND reversion_12 | 9865.74 | -134.26 | sell /  / momentum_26 AND reversion_12: prior completed bar target 0%; next bar open simulation |
| v1 | momentum_26 + reversion_12 | 9788.90 | -211.10 | sell /  / momentum_26 + reversion_12: prior completed bar target 0%; next bar open simulation |
| v1 | momentum_26 AND volume_26 | 9757.36 | -242.64 | sell /  / momentum_26 AND volume_26: prior completed bar target 0%; next bar open simulation |
| v1 | momentum_26 + volume_26 | 9730.80 | -269.20 | sell /  / momentum_26 + volume_26: prior completed bar target 0%; next bar open simulation |
| v1 | breakout_8 AND reversion_12 | 10000.00 | 0.00 | 대기 /  / 새 신호 대기 |
| v1 | breakout_8 + reversion_12 | 9577.80 | -422.20 | sell /  / breakout_8 + reversion_12: prior completed bar target 0%; next bar open simulation |
| v1 | breakout_8 AND volume_26 | 9876.84 | -123.16 | sell /  / breakout_8 AND volume_26: prior completed bar target 0%; next bar open simulation |
| v1 | breakout_8 + volume_26 | 9559.16 | -440.84 | sell /  / breakout_8 + volume_26: prior completed bar target 0%; next bar open simulation |
| v1 | reversion_12 AND volume_26 | 9917.39 | -82.61 | sell /  / reversion_12 AND volume_26: prior completed bar target 0%; next bar open simulation |
| v1 | reversion_12 + volume_26 | 9812.68 | -187.32 | sell /  / reversion_12 + volume_26: prior completed bar target 0%; next bar open simulation |
| v1 | ema_12_26 | 9803.63 | -196.37 | sell /  / EMA12 > EMA26; 조건 미충족; EMA12=526.379, EMA26=526.494 |
| v1 | macd_12_26_9 | 9752.67 | -247.33 | sell /  / MACD > 신호선 그리고 MACD > 0; 조건 미충족; MACD=-0.115547, signal9=0.181673 |
| v1 | rsi_14_recovery | 9985.10 | -14.90 | sell /  / 직전 RSI14 < 30, 현재 RSI14 >= 30 (한 봉 목표); 조건 미충족; RSI14=40.1529, previous_RSI14=32.5751 |
| v1 | bollinger_20_reentry | 9925.00 | -75.00 | sell /  / 직전 종가 < 직전 하단밴드, 현재 하단밴드 <= 종가 <= SMA20 (한 봉 목표); 조건 미충족; close=522.815, lower20=520.55, SMA20=525.436, previous_lower20=520.821 |
| v1 | donchian_20 | 9675.11 | -324.89 | sell /  / 종가 > 현재 봉을 제외한 직전 20봉 최고가; 조건 미충족; close=526.71, prior_high20=528.45 |
| v1 | atr_14_breakout | 9709.35 | -290.65 | sell /  / 종가 > 직전 종가 + 직전 ATR14 그리고 종가 > EMA26; 조건 미충족; close=527.625, threshold=528.531, prior_ATR14=1.00085, EMA26=526.218 |
| v1 | session_vwap | 9617.24 | -382.76 | buy /  / 종가 > 뉴욕 거래일별 누적 전형가격 VWAP; 조건 충족; close=522.815, session_VWAP=521.917, session_volume=1.59529e+06 |
| v1 | obv_20 | 9727.80 | -272.20 | sell /  / OBV > OBV의 SMA20 그리고 종가 > EMA26; 조건 미충족; OBV=-6.66951e+06, OBV_SMA20=-6.32674e+06, close=522.39, EMA26=526.494 |
| v1 | stochastic_14_3_recovery | 9688.29 | -311.71 | sell /  / 직전 %K14 < 20에서 %K14가 %D3 상향 돌파 (한 봉 목표); 조건 미충족; K14=35.6623, D3=20.5547, previous_K14=19.3192, previous_D3=8.7863 |
| v1 | mfi_14_recovery | 9902.01 | -97.99 | sell /  / 직전 MFI14 < 20, 현재 MFI14 >= 20 (한 봉 목표); 조건 미충족; MFI14=29.4378, previous_MFI14=21.6288 |
| v1 | adx_14_trend | 9711.49 | -288.51 | sell /  / Wilder ADX14 >= 25 그리고 +DI14 > -DI14; 조건 미충족; ADX14=28.0997, plus_DI14=30.0206, minus_DI14=36.1913 |
| v1 | aroon_25_trend | 9820.69 | -179.31 | sell /  / Aroon25 Up > 70 그리고 Down < 30 (동률이면 최신 극값); 조건 미충족; Aroon_up=72, Aroon_down=92 |
| v1 | cci_20_momentum | 9709.75 | -290.25 | sell /  / CCI20 > 100 (전형가격·평균절대편차); 조건 미충족; CCI20=-498.183 |
| v1 | williams_14_recovery | 9697.88 | -302.12 | sell /  / 직전 Williams %R14 < -80, 현재 >= -80 (한 봉 목표); 조건 미충족; Williams_R14=-68.4085, previous_R14=-64.3377 |
| v1 | cmf_20_accumulation | 9400.30 | -599.70 | buy /  / Chaikin Money Flow20 > 0.1; 조건 충족; CMF20=0.140077, volume20=2.63627e+06 |
| v1 | chaikin_3_10 | 9611.06 | -388.94 | sell /  / ADL의 EMA3 - EMA10 > 0 그리고 종가 > EMA26; 조건 미충족; Chaikin3_10=70160.2, ADL=-1.15315e+07, close=522.39, EMA26=526.494 |
| v1 | roc_10_momentum | 9939.01 | -60.99 | sell /  / 10봉 ROC > 1% 그리고 종가 > EMA26; 조건 미충족; ROC10_percent=0.771645, close=523.68, EMA26=521.367 |
| v1 | trix_15_trend | 9741.60 | -258.40 | sell /  / 15봉 삼중 EMA의 1봉 변화율 TRIX > 0 그리고 종가 > EMA26; 조건 미충족; TRIX15_percent=0.0047414, close=522.39, EMA26=526.494 |
| v1 | keltner_20_breakout | 9826.82 | -173.18 | sell /  / 종가 > EMA20 + 2 x Wilder ATR14; 조건 미충족; close=526.34, upper_Keltner=527.991, EMA20=526.293, ATR14=0.848911 |
| v1 | opening_range_30m | 9536.25 | -463.75 | sell /  / 뉴욕 09:30·09:45 두 완료 봉 최고가를 10:00 이후 종가가 돌파; 자료 부족·변동폭 또는 거래량 없음: 대기; close=522.39 |
| v2 | cash | 10000.00 | 0.00 | 대기 /  / 새 신호 대기 |
| v2 | buy_hold | 10108.31 | 108.31 | buy / partial / 직전 완료 봉 목표 비중 100%; 다음 봉 시가 가정 |
| v2 | trend_8_26 | 9784.94 | -215.06 | sell / filled / 직전 완료 봉 목표 비중 0%; 다음 봉 시가 가정 |
| v2 | momentum_26 | 9699.02 | -300.98 | sell / filled / 직전 완료 봉 목표 비중 0%; 다음 봉 시가 가정 |
| v2 | breakout_8 | 8947.06 | -1052.94 | 중단: 손실 한도 / buy / partial / 직전 완료 봉 목표 비중 100%; 다음 봉 시가 가정 |
| v2 | reversion_12 | 9483.90 | -516.10 | sell / filled / 직전 완료 봉 목표 비중 0%; 다음 봉 시가 가정 |
| v2 | volume_26 | 9462.56 | -537.44 | sell / filled / 직전 완료 봉 목표 비중 0%; 다음 봉 시가 가정 |
| v2 | trend_8_26 AND momentum_26 | 9689.46 | -310.54 | sell / filled / 직전 완료 봉 목표 비중 0%; 다음 봉 시가 가정 |
| v2 | trend_8_26 + momentum_26 | 9742.04 | -257.96 | sell / filled / 직전 완료 봉 목표 비중 0%; 다음 봉 시가 가정 |
| v2 | trend_8_26 AND breakout_8 | 9241.90 | -758.10 | sell / filled / 직전 완료 봉 목표 비중 0%; 다음 봉 시가 가정 |
| v2 | trend_8_26 + breakout_8 | 9350.97 | -649.03 | sell / filled / 직전 완료 봉 목표 비중 0%; 다음 봉 시가 가정 |
| v2 | trend_8_26 AND reversion_12 | 9669.36 | -330.64 | sell / filled / 직전 완료 봉 목표 비중 0%; 다음 봉 시가 가정 |
| v2 | trend_8_26 + reversion_12 | 9653.02 | -346.98 | sell / filled / 직전 완료 봉 목표 비중 0%; 다음 봉 시가 가정 |
| v2 | trend_8_26 AND volume_26 | 9688.83 | -311.17 | sell / filled / 직전 완료 봉 목표 비중 0%; 다음 봉 시가 가정 |
| v2 | trend_8_26 + volume_26 | 9642.37 | -357.63 | sell / filled / 직전 완료 봉 목표 비중 0%; 다음 봉 시가 가정 |
| v2 | momentum_26 AND breakout_8 | 9090.90 | -909.10 | sell / filled / 직전 완료 봉 목표 비중 0%; 다음 봉 시가 가정 |
| v2 | momentum_26 + breakout_8 | 9251.50 | -748.50 | sell / filled / 직전 완료 봉 목표 비중 0%; 다음 봉 시가 가정 |
| v2 | momentum_26 AND reversion_12 | 9814.45 | -185.55 | sell / filled / 직전 완료 봉 목표 비중 0%; 다음 봉 시가 가정 |
| v2 | momentum_26 + reversion_12 | 9651.03 | -348.97 | sell / filled / 직전 완료 봉 목표 비중 0%; 다음 봉 시가 가정 |
| v2 | momentum_26 AND volume_26 | 9540.48 | -459.52 | sell / filled / 직전 완료 봉 목표 비중 0%; 다음 봉 시가 가정 |
| v2 | momentum_26 + volume_26 | 9640.55 | -359.45 | sell / filled / 직전 완료 봉 목표 비중 0%; 다음 봉 시가 가정 |
| v2 | breakout_8 AND reversion_12 | 10000.00 | 0.00 | 대기 /  / 새 신호 대기 |
| v2 | breakout_8 + reversion_12 | 9185.85 | -814.15 | sell / filled / 직전 완료 봉 목표 비중 0%; 다음 봉 시가 가정 |
| v2 | breakout_8 AND volume_26 | 9668.17 | -331.83 | sell / filled / 직전 완료 봉 목표 비중 0%; 다음 봉 시가 가정 |
| v2 | breakout_8 + volume_26 | 9175.95 | -824.05 | sell / filled / 직전 완료 봉 목표 비중 0%; 다음 봉 시가 가정 |
| v2 | reversion_12 AND volume_26 | 9909.46 | -90.54 | sell / filled / 직전 완료 봉 목표 비중 0%; 다음 봉 시가 가정 |
| v2 | reversion_12 + volume_26 | 9512.65 | -487.35 | sell / filled / 직전 완료 봉 목표 비중 0%; 다음 봉 시가 가정 |
| v2 | ema_12_26 | 9797.75 | -202.25 | sell / filled / EMA12 > EMA26; 조건 미충족; EMA12=526.379, EMA26=526.494; 직전 완료 봉 목표를 다음 봉 시가에 모의 적용 |
| v2 | macd_12_26_9 | 9740.97 | -259.03 | sell / filled / MACD > 신호선 그리고 MACD > 0; 조건 미충족; MACD=-0.115547, signal9=0.181673; 직전 완료 봉 목표를 다음 봉 시가에 모의 적용 |
| v2 | rsi_14_recovery | 9983.11 | -16.89 | sell / filled / 직전 RSI14 < 30, 현재 RSI14 >= 30 (한 봉 목표); 조건 미충족; RSI14=40.1529, previous_RSI14=32.5751; 직전 완료 봉 목표를 다음 봉 시가에 모의 적용 |
| v2 | bollinger_20_reentry | 9919.05 | -80.95 | sell / filled / 직전 종가 < 직전 하단밴드, 현재 하단밴드 <= 종가 <= SMA20 (한 봉 목표); 조건 미충족; close=522.815, lower20=520.55, SMA20=525.436, previous_lower20=520.821; 직전 완료 봉 목표를 다음 봉 시가에 모의 적용 |
| v2 | donchian_20 | 9661.57 | -338.43 | sell / filled / 종가 > 현재 봉을 제외한 직전 20봉 최고가; 조건 미충족; close=526.71, prior_high20=528.45; 직전 완료 봉 목표를 다음 봉 시가에 모의 적용 |
| v2 | atr_14_breakout | 9693.83 | -306.17 | sell / filled / 종가 > 직전 종가 + 직전 ATR14 그리고 종가 > EMA26; 조건 미충족; close=527.625, threshold=528.531, prior_ATR14=1.00085, EMA26=526.218; 직전 완료 봉 목표를 다음 봉 시가에 모의 적용 |
| v2 | session_vwap | 9600.90 | -399.10 | buy / partial / 종가 > 뉴욕 거래일별 누적 전형가격 VWAP; 조건 충족; close=522.815, session_VWAP=521.917, session_volume=1.59529e+06; 직전 완료 봉 목표를 다음 봉 시가에 모의 적용 |
| v2 | obv_20 | 9712.25 | -287.75 | sell / filled / OBV > OBV의 SMA20 그리고 종가 > EMA26; 조건 미충족; OBV=-6.66951e+06, OBV_SMA20=-6.32674e+06, close=522.39, EMA26=526.494; 직전 완료 봉 목표를 다음 봉 시가에 모의 적용 |
| v2 | stochastic_14_3_recovery | 9670.86 | -329.14 | sell / filled / 직전 %K14 < 20에서 %K14가 %D3 상향 돌파 (한 봉 목표); 조건 미충족; K14=35.6623, D3=20.5547, previous_K14=19.3192, previous_D3=8.7863; 직전 완료 봉 목표를 다음 봉 시가에 모의 적용 |
| v2 | mfi_14_recovery | 9896.07 | -103.93 | sell / filled / 직전 MFI14 < 20, 현재 MFI14 >= 20 (한 봉 목표); 조건 미충족; MFI14=29.4378, previous_MFI14=21.6288; 직전 완료 봉 목표를 다음 봉 시가에 모의 적용 |
| v2 | adx_14_trend | 9701.78 | -298.22 | sell / filled / Wilder ADX14 >= 25 그리고 +DI14 > -DI14; 조건 미충족; ADX14=28.0997, plus_DI14=30.0206, minus_DI14=36.1913; 직전 완료 봉 목표를 다음 봉 시가에 모의 적용 |
| v2 | aroon_25_trend | 9810.88 | -189.12 | sell / filled / Aroon25 Up > 70 그리고 Down < 30 (동률이면 최신 극값); 조건 미충족; Aroon_up=72, Aroon_down=92; 직전 완료 봉 목표를 다음 봉 시가에 모의 적용 |
| v2 | cci_20_momentum | 9694.23 | -305.77 | sell / filled / CCI20 > 100 (전형가격·평균절대편차); 조건 미충족; CCI20=-498.183; 직전 완료 봉 목표를 다음 봉 시가에 모의 적용 |
| v2 | williams_14_recovery | 9682.38 | -317.62 | sell / filled / 직전 Williams %R14 < -80, 현재 >= -80 (한 봉 목표); 조건 미충족; Williams_R14=-68.4085, previous_R14=-64.3377; 직전 완료 봉 목표를 다음 봉 시가에 모의 적용 |
| v2 | cmf_20_accumulation | 9378.71 | -621.29 | buy / partial / Chaikin Money Flow20 > 0.1; 조건 충족; CMF20=0.140077, volume20=2.63627e+06; 직전 완료 봉 목표를 다음 봉 시가에 모의 적용 |
| v2 | chaikin_3_10 | 9595.70 | -404.30 | sell / filled / ADL의 EMA3 - EMA10 > 0 그리고 종가 > EMA26; 조건 미충족; Chaikin3_10=70160.2, ADL=-1.15315e+07, close=522.39, EMA26=526.494; 직전 완료 봉 목표를 다음 봉 시가에 모의 적용 |
| v2 | roc_10_momentum | 9937.03 | -62.97 | sell / filled / 10봉 ROC > 1% 그리고 종가 > EMA26; 조건 미충족; ROC10_percent=0.771645, close=523.68, EMA26=521.367; 직전 완료 봉 목표를 다음 봉 시가에 모의 적용 |
| v2 | trix_15_trend | 9731.86 | -268.14 | sell / filled / 15봉 삼중 EMA의 1봉 변화율 TRIX > 0 그리고 종가 > EMA26; 조건 미충족; TRIX15_percent=0.0047414, close=522.39, EMA26=526.494; 직전 완료 봉 목표를 다음 봉 시가에 모의 적용 |
| v2 | keltner_20_breakout | 9817.00 | -183.00 | sell / filled / 종가 > EMA20 + 2 x Wilder ATR14; 조건 미충족; close=526.34, upper_Keltner=527.991, EMA20=526.293, ATR14=0.848911; 직전 완료 봉 목표를 다음 봉 시가에 모의 적용 |
| v2 | opening_range_30m | 9517.20 | -482.80 | sell / filled / 뉴욕 09:30·09:45 두 완료 봉 최고가를 10:00 이후 종가가 돌파; 자료 부족·변동폭 또는 거래량 없음: 대기; close=522.39; 직전 완료 봉 목표를 다음 봉 시가에 모의 적용 |

### 같은 기간의 비용·노출 비교 (사후 연구)

| 전략 | 비용 전 | 비용 후 | 100% 보유 | 같은 평균 노출 보유 | 평균 노출 |
|---|---:|---:|---:|---:|---:|
| cash | 0.00% | 0.00% | 2.03% | 0.00% | 0.00% |
| buy_hold | 2.46% | 2.03% | 2.03% | 2.03% | 100.00% |
| trend_8_26 | 1.92% | -2.28% | 2.03% | 1.31% | 64.47% |
| momentum_26 | 1.00% | -3.96% | 2.03% | 1.25% | 61.84% |
| breakout_8 | -0.10% | -17.65% | 2.03% | 0.52% | 26.05% |
| reversion_12 | 1.02% | -7.12% | 2.03% | 0.39% | 19.21% |
| volume_26 | 1.35% | -8.37% | 2.03% | 0.21% | 10.53% |
| trend_8_26 AND momentum_26 | 2.39% | -3.05% | 2.03% | 1.11% | 55.00% |
| trend_8_26 + momentum_26 | 1.46% | -3.12% | 2.03% | 1.28% | 63.16% |
| trend_8_26 AND breakout_8 | 0.97% | -12.10% | 2.03% | 0.38% | 18.68% |
| trend_8_26 + breakout_8 | 0.91% | -9.54% | 2.03% | 0.91% | 45.27% |
| trend_8_26 AND reversion_12 | 0.81% | -4.55% | 2.03% | 0.14% | 7.11% |
| trend_8_26 + reversion_12 | 1.47% | -4.34% | 2.03% | 0.84% | 41.85% |
| trend_8_26 AND volume_26 | 1.68% | -4.53% | 2.03% | 0.12% | 6.05% |
| trend_8_26 + volume_26 | 1.64% | -5.18% | 2.03% | 0.76% | 37.50% |
| momentum_26 AND breakout_8 | 0.18% | -13.88% | 2.03% | 0.42% | 21.05% |
| momentum_26 + breakout_8 | 0.46% | -11.07% | 2.03% | 0.89% | 43.95% |
| momentum_26 AND reversion_12 | 0.10% | -3.21% | 2.03% | 0.11% | 5.53% |
| momentum_26 + reversion_12 | 1.02% | -4.56% | 2.03% | 0.82% | 40.53% |
| momentum_26 AND volume_26 | 0.13% | -6.77% | 2.03% | 0.13% | 6.32% |
| momentum_26 + volume_26 | 1.18% | -5.60% | 2.03% | 0.73% | 36.19% |
| breakout_8 AND reversion_12 | 0.00% | 0.00% | 2.03% | 0.00% | 0.00% |
| breakout_8 + reversion_12 | 0.46% | -12.00% | 2.03% | 0.46% | 22.64% |
| breakout_8 AND volume_26 | -0.11% | -4.22% | 2.03% | 0.07% | 3.68% |
| breakout_8 + volume_26 | 0.62% | -12.22% | 2.03% | 0.37% | 18.30% |
| reversion_12 AND volume_26 | 1.21% | -2.55% | 2.03% | 0.05% | 2.63% |
| reversion_12 + volume_26 | 1.18% | -7.37% | 2.03% | 0.30% | 14.87% |
| ema_12_26 | 0.79% | -1.71% | 2.03% | 1.28% | 63.16% |
| macd_12_26_9 | 2.44% | -1.77% | 2.03% | 0.65% | 32.11% |
| rsi_14_recovery | 0.39% | -0.86% | 2.03% | 0.02% | 0.79% |
| bollinger_20_reentry | 0.60% | -2.72% | 2.03% | 0.04% | 2.11% |
| donchian_20 | 0.32% | -7.76% | 2.03% | 0.22% | 11.05% |
| atr_14_breakout | -0.20% | -8.63% | 2.03% | 0.13% | 6.58% |
| session_vwap | 1.15% | -6.61% | 2.03% | 1.26% | 62.37% |
| obv_20 | 1.40% | -6.77% | 2.03% | 0.95% | 47.11% |
| stochastic_14_3_recovery | 1.62% | -9.28% | 2.03% | 0.14% | 7.11% |
| mfi_14_recovery | 0.37% | -2.95% | 2.03% | 0.04% | 2.11% |
| adx_14_trend | 0.37% | -3.35% | 2.03% | 0.66% | 32.89% |
| aroon_25_trend | 1.75% | -2.02% | 2.03% | 0.56% | 27.63% |
| cci_20_momentum | 1.65% | -5.35% | 2.03% | 0.57% | 28.42% |
| williams_14_recovery | 1.56% | -6.23% | 2.03% | 0.10% | 5.00% |
| cmf_20_accumulation | 0.20% | -9.03% | 2.03% | 0.89% | 44.21% |
| chaikin_3_10 | 1.11% | -8.59% | 2.03% | 1.07% | 53.16% |
| roc_10_momentum | -0.07% | -0.90% | 2.03% | 0.04% | 2.11% |
| trix_15_trend | 0.38% | -3.75% | 2.03% | 1.14% | 56.58% |
| keltner_20_breakout | 1.05% | -6.31% | 2.03% | 0.40% | 20.00% |
| opening_range_30m | 1.10% | -6.66% | 2.03% | 0.66% | 32.89% |

동일 구간·초기 자금, 종료 시 청산 비용 포함. 노출 맞춤은 사후 설명용이며 v2 실제 계좌 성과가 아닙니다.
[낙폭 분해·비용 영향·전체 구간](DIA/comparison.json)

[v1 전체 기록](DIA/accounts.json) · [v2 전체 기록](DIA/accounts-v2.json)

## MSFT 계좌

| 모델 | 전략 | 평가액 USD | 손익 USD | 최근 매매·이유 |
|---|---|---:|---:|---|
| v1 | cash | 10000.00 | 0.00 | 대기 /  / 새 신호 대기 |
| v1 | buy_hold | 9686.47 | -313.53 | buy /  / buy_hold: prior completed bar target 100%; next bar open simulation |
| v1 | trend_8_26 | 9424.07 | -575.93 | buy /  / trend_8_26: prior completed bar target 100%; next bar open simulation |
| v1 | momentum_26 | 9279.92 | -720.08 | buy /  / momentum_26: prior completed bar target 100%; next bar open simulation |
| v1 | breakout_8 | 9454.11 | -545.89 | sell /  / breakout_8: prior completed bar target 0%; next bar open simulation |
| v1 | reversion_12 | 9285.36 | -714.64 | sell /  / reversion_12: prior completed bar target 0%; next bar open simulation |
| v1 | volume_26 | 9623.19 | -376.81 | sell /  / volume_26: prior completed bar target 0%; next bar open simulation |
| v1 | trend_8_26 AND momentum_26 | 9418.73 | -581.27 | buy /  / trend_8_26 AND momentum_26: prior completed bar target 100%; next bar open simulation |
| v1 | trend_8_26 + momentum_26 | 9389.19 | -610.81 | buy /  / trend_8_26 + momentum_26: prior completed bar target 100%; next bar open simulation |
| v1 | trend_8_26 AND breakout_8 | 9678.51 | -321.49 | sell /  / trend_8_26 AND breakout_8: prior completed bar target 0%; next bar open simulation |
| v1 | trend_8_26 + breakout_8 | 9477.12 | -522.88 | buy /  / trend_8_26 + breakout_8: prior completed bar target 50%; next bar open simulation |
| v1 | trend_8_26 AND reversion_12 | 9519.35 | -480.65 | sell /  / trend_8_26 AND reversion_12: prior completed bar target 0%; next bar open simulation |
| v1 | trend_8_26 + reversion_12 | 9373.11 | -626.89 | buy /  / trend_8_26 + reversion_12: prior completed bar target 50%; next bar open simulation |
| v1 | trend_8_26 AND volume_26 | 9802.11 | -197.89 | sell /  / trend_8_26 AND volume_26: prior completed bar target 0%; next bar open simulation |
| v1 | trend_8_26 + volume_26 | 9523.22 | -476.78 | buy /  / trend_8_26 + volume_26: prior completed bar target 50%; next bar open simulation |
| v1 | momentum_26 AND breakout_8 | 9642.25 | -357.75 | sell /  / momentum_26 AND breakout_8: prior completed bar target 0%; next bar open simulation |
| v1 | momentum_26 + breakout_8 | 9385.53 | -614.47 | sell /  / momentum_26 + breakout_8: prior completed bar target 50%; next bar open simulation |
| v1 | momentum_26 AND reversion_12 | 9649.76 | -350.24 | sell /  / momentum_26 AND reversion_12: prior completed bar target 0%; next bar open simulation |
| v1 | momentum_26 + reversion_12 | 9338.38 | -661.62 | sell /  / momentum_26 + reversion_12: prior completed bar target 50%; next bar open simulation |
| v1 | momentum_26 AND volume_26 | 9830.16 | -169.84 | sell /  / momentum_26 AND volume_26: prior completed bar target 0%; next bar open simulation |
| v1 | momentum_26 + volume_26 | 9469.13 | -530.87 | sell /  / momentum_26 + volume_26: prior completed bar target 50%; next bar open simulation |
| v1 | breakout_8 AND reversion_12 | 10000.00 | 0.00 | 대기 /  / 새 신호 대기 |
| v1 | breakout_8 + reversion_12 | 9406.74 | -593.26 | sell /  / breakout_8 + reversion_12: prior completed bar target 0%; next bar open simulation |
| v1 | breakout_8 AND volume_26 | 9953.19 | -46.81 | sell /  / breakout_8 AND volume_26: prior completed bar target 0%; next bar open simulation |
| v1 | breakout_8 + volume_26 | 9576.31 | -423.69 | sell /  / breakout_8 + volume_26: prior completed bar target 0%; next bar open simulation |
| v1 | reversion_12 AND volume_26 | 9770.39 | -229.61 | sell /  / reversion_12 AND volume_26: prior completed bar target 0%; next bar open simulation |
| v1 | reversion_12 + volume_26 | 9471.64 | -528.36 | sell /  / reversion_12 + volume_26: prior completed bar target 0%; next bar open simulation |
| v1 | ema_12_26 | 9491.42 | -508.58 | sell /  / EMA12 > EMA26; 조건 미충족; EMA12=531.766, EMA26=531.788 |
| v1 | macd_12_26_9 | 9603.93 | -396.07 | sell /  / MACD > 신호선 그리고 MACD > 0; 조건 미충족; MACD=-0.0222122, signal9=0.149678 |
| v1 | rsi_14_recovery | 9839.66 | -160.34 | sell /  / 직전 RSI14 < 30, 현재 RSI14 >= 30 (한 봉 목표); 조건 미충족; RSI14=49.0008, previous_RSI14=38.029 |
| v1 | bollinger_20_reentry | 9745.81 | -254.19 | sell /  / 직전 종가 < 직전 하단밴드, 현재 하단밴드 <= 종가 <= SMA20 (한 봉 목표); 조건 미충족; close=523.535, lower20=518.78, SMA20=523.154, previous_lower20=518.792 |
| v1 | donchian_20 | 9912.16 | -87.84 | sell /  / 종가 > 현재 봉을 제외한 직전 20봉 최고가; 조건 미충족; close=534.52, prior_high20=535.44 |
| v1 | atr_14_breakout | 9915.10 | -84.90 | sell /  / 종가 > 직전 종가 + 직전 ATR14 그리고 종가 > EMA26; 조건 미충족; close=533.975, threshold=536.307, prior_ATR14=2.16203, EMA26=530.521 |
| v1 | session_vwap | 9646.19 | -353.81 | buy /  / 종가 > 뉴욕 거래일별 누적 전형가격 VWAP; 조건 충족; close=520.51, session_VWAP=518.805, session_volume=2.29852e+06 |
| v1 | obv_20 | 9512.03 | -487.97 | buy /  / OBV > OBV의 SMA20 그리고 종가 > EMA26; 조건 충족; OBV=4.32468e+07, OBV_SMA20=4.25563e+07, close=525.435, EMA26=523.774 |
| v1 | stochastic_14_3_recovery | 9641.51 | -358.49 | sell /  / 직전 %K14 < 20에서 %K14가 %D3 상향 돌파 (한 봉 목표); 조건 미충족; K14=18.1724, D3=16.7161, previous_K14=21.0531, previous_D3=14.2045 |
| v1 | mfi_14_recovery | 9880.73 | -119.27 | sell /  / 직전 MFI14 < 20, 현재 MFI14 >= 20 (한 봉 목표); 조건 미충족; MFI14=28.323, previous_MFI14=32.1727 |
| v1 | adx_14_trend | 9883.62 | -116.38 | sell /  / Wilder ADX14 >= 25 그리고 +DI14 > -DI14; 조건 미충족; ADX14=23.6824, plus_DI14=22.3066, minus_DI14=19.9214 |
| v1 | aroon_25_trend | 9616.60 | -383.40 | sell /  / Aroon25 Up > 70 그리고 Down < 30 (동률이면 최신 극값); 조건 미충족; Aroon_up=96, Aroon_down=100 |
| v1 | cci_20_momentum | 9870.62 | -129.38 | sell /  / CCI20 > 100 (전형가격·평균절대편차); 조건 미충족; CCI20=99.2896 |
| v1 | williams_14_recovery | 9621.94 | -378.06 | sell /  / 직전 Williams %R14 < -80, 현재 >= -80 (한 봉 목표); 조건 미충족; Williams_R14=-12.9449, previous_R14=-50.616 |
| v1 | cmf_20_accumulation | 9606.90 | -393.10 | buy /  / Chaikin Money Flow20 > 0.1; 조건 충족; CMF20=0.197107, volume20=1.18305e+07 |
| v1 | chaikin_3_10 | 9549.88 | -450.12 | buy /  / ADL의 EMA3 - EMA10 > 0 그리고 종가 > EMA26; 조건 충족; Chaikin3_10=722764, ADL=9.67933e+07, close=525.435, EMA26=523.774 |
| v1 | roc_10_momentum | 9959.43 | -40.57 | sell /  / 10봉 ROC > 1% 그리고 종가 > EMA26; 조건 미충족; ROC10_percent=0.454191, close=534.125, EMA26=532.186 |
| v1 | trix_15_trend | 9557.09 | -442.91 | sell /  / 15봉 삼중 EMA의 1봉 변화율 TRIX > 0 그리고 종가 > EMA26; 조건 미충족; TRIX15_percent=0.00481299, close=529.54, EMA26=531.788 |
| v1 | keltner_20_breakout | 9958.78 | -41.22 | sell /  / 종가 > EMA20 + 2 x Wilder ATR14; 조건 미충족; close=533.975, upper_Keltner=534.357, EMA20=530.111, ATR14=2.12332 |
| v1 | opening_range_30m | 9617.22 | -382.78 | buy /  / 뉴욕 09:30·09:45 두 완료 봉 최고가를 10:00 이후 종가가 돌파; 조건 충족; close=523.535, opening_high=522.36 |
| v2 | cash | 10000.00 | 0.00 | 대기 /  / 새 신호 대기 |
| v2 | buy_hold | 9739.33 | -260.67 | buy / partial / 직전 완료 봉 목표 비중 100%; 다음 봉 시가 가정 |
| v2 | trend_8_26 | 9356.78 | -643.22 | buy / partial / 직전 완료 봉 목표 비중 100%; 다음 봉 시가 가정 |
| v2 | momentum_26 | 9308.28 | -691.72 | buy / partial / 직전 완료 봉 목표 비중 100%; 다음 봉 시가 가정 |
| v2 | breakout_8 | 9238.63 | -761.37 | sell / filled / 직전 완료 봉 목표 비중 0%; 다음 봉 시가 가정 |
| v2 | reversion_12 | 9037.17 | -962.83 | 중단: 손실 한도 / buy / partial / 직전 완료 봉 목표 비중 100%; 다음 봉 시가 가정 |
| v2 | volume_26 | 9304.84 | -695.16 | sell / filled / 직전 완료 봉 목표 비중 0%; 다음 봉 시가 가정 |
| v2 | trend_8_26 AND momentum_26 | 9310.46 | -689.54 | buy / partial / 직전 완료 봉 목표 비중 100%; 다음 봉 시가 가정 |
| v2 | trend_8_26 + momentum_26 | 9372.01 | -627.99 | buy / partial / 직전 완료 봉 목표 비중 100%; 다음 봉 시가 가정 |
| v2 | trend_8_26 AND breakout_8 | 9318.21 | -681.79 | sell / filled / 직전 완료 봉 목표 비중 0%; 다음 봉 시가 가정 |
| v2 | trend_8_26 + breakout_8 | 9356.67 | -643.33 | buy / filled / 직전 완료 봉 목표 비중 50%; 다음 봉 시가 가정 |
| v2 | trend_8_26 AND reversion_12 | 9411.07 | -588.93 | sell / filled / 직전 완료 봉 목표 비중 0%; 다음 봉 시가 가정 |
| v2 | trend_8_26 + reversion_12 | 9149.35 | -850.65 | buy / filled / 직전 완료 봉 목표 비중 50%; 다음 봉 시가 가정 |
| v2 | trend_8_26 AND volume_26 | 9743.99 | -256.01 | sell / filled / 직전 완료 봉 목표 비중 0%; 다음 봉 시가 가정 |
| v2 | trend_8_26 + volume_26 | 9350.29 | -649.71 | buy / filled / 직전 완료 봉 목표 비중 50%; 다음 봉 시가 가정 |
| v2 | momentum_26 AND breakout_8 | 9430.77 | -569.23 | sell / filled / 직전 완료 봉 목표 비중 0%; 다음 봉 시가 가정 |
| v2 | momentum_26 + breakout_8 | 9293.11 | -706.89 | sell / filled / 직전 완료 봉 목표 비중 50%; 다음 봉 시가 가정 |
| v2 | momentum_26 AND reversion_12 | 9475.12 | -524.88 | sell / filled / 직전 완료 봉 목표 비중 0%; 다음 봉 시가 가정 |
| v2 | momentum_26 + reversion_12 | 9164.08 | -835.92 | sell / filled / 직전 완료 봉 목표 비중 50%; 다음 봉 시가 가정 |
| v2 | momentum_26 AND volume_26 | 9695.84 | -304.16 | sell / filled / 직전 완료 봉 목표 비중 0%; 다음 봉 시가 가정 |
| v2 | momentum_26 + volume_26 | 9345.86 | -654.14 | sell / filled / 직전 완료 봉 목표 비중 50%; 다음 봉 시가 가정 |
| v2 | breakout_8 AND reversion_12 | 10000.00 | 0.00 | 대기 /  / 새 신호 대기 |
| v2 | breakout_8 + reversion_12 | 9129.66 | -870.34 | sell / filled / 직전 완료 봉 목표 비중 0%; 다음 봉 시가 가정 |
| v2 | breakout_8 AND volume_26 | 9890.09 | -109.91 | sell / filled / 직전 완료 봉 목표 비중 0%; 다음 봉 시가 가정 |
| v2 | breakout_8 + volume_26 | 9330.09 | -669.91 | sell / filled / 직전 완료 봉 목표 비중 0%; 다음 봉 시가 가정 |
| v2 | reversion_12 AND volume_26 | 9528.36 | -471.64 | sell / filled / 직전 완료 봉 목표 비중 0%; 다음 봉 시가 가정 |
| v2 | reversion_12 + volume_26 | 9124.11 | -875.89 | sell / filled / 직전 완료 봉 목표 비중 0%; 다음 봉 시가 가정 |
| v2 | ema_12_26 | 9483.83 | -516.17 | sell / filled / EMA12 > EMA26; 조건 미충족; EMA12=531.766, EMA26=531.788; 직전 완료 봉 목표를 다음 봉 시가에 모의 적용 |
| v2 | macd_12_26_9 | 9594.34 | -405.66 | sell / filled / MACD > 신호선 그리고 MACD > 0; 조건 미충족; MACD=-0.0222122, signal9=0.149678; 직전 완료 봉 목표를 다음 봉 시가에 모의 적용 |
| v2 | rsi_14_recovery | 9825.89 | -174.11 | sell / filled / 직전 RSI14 < 30, 현재 RSI14 >= 30 (한 봉 목표); 조건 미충족; RSI14=49.0008, previous_RSI14=38.029; 직전 완료 봉 목표를 다음 봉 시가에 모의 적용 |
| v2 | bollinger_20_reentry | 9732.18 | -267.82 | sell / filled / 직전 종가 < 직전 하단밴드, 현재 하단밴드 <= 종가 <= SMA20 (한 봉 목표); 조건 미충족; close=523.535, lower20=518.78, SMA20=523.154, previous_lower20=518.792; 직전 완료 봉 목표를 다음 봉 시가에 모의 적용 |
| v2 | donchian_20 | 9908.19 | -91.81 | sell / filled / 종가 > 현재 봉을 제외한 직전 20봉 최고가; 조건 미충족; close=534.52, prior_high20=535.44; 직전 완료 봉 목표를 다음 봉 시가에 모의 적용 |
| v2 | atr_14_breakout | 9911.14 | -88.86 | sell / filled / 종가 > 직전 종가 + 직전 ATR14 그리고 종가 > EMA26; 조건 미충족; close=533.975, threshold=536.307, prior_ATR14=2.16203, EMA26=530.521; 직전 완료 봉 목표를 다음 봉 시가에 모의 적용 |
| v2 | session_vwap | 9629.81 | -370.19 | buy / partial / 종가 > 뉴욕 거래일별 누적 전형가격 VWAP; 조건 충족; close=520.51, session_VWAP=518.805, session_volume=2.29852e+06; 직전 완료 봉 목표를 다음 봉 시가에 모의 적용 |
| v2 | obv_20 | 9493.98 | -506.02 | buy / partial / OBV > OBV의 SMA20 그리고 종가 > EMA26; 조건 충족; OBV=4.32468e+07, OBV_SMA20=4.25563e+07, close=525.435, EMA26=523.774; 직전 완료 봉 목표를 다음 봉 시가에 모의 적용 |
| v2 | stochastic_14_3_recovery | 9622.24 | -377.76 | sell / filled / 직전 %K14 < 20에서 %K14가 %D3 상향 돌파 (한 봉 목표); 조건 미충족; K14=18.1724, D3=16.7161, previous_K14=21.0531, previous_D3=14.2045; 직전 완료 봉 목표를 다음 봉 시가에 모의 적용 |
| v2 | mfi_14_recovery | 9872.83 | -127.17 | sell / filled / 직전 MFI14 < 20, 현재 MFI14 >= 20 (한 봉 목표); 조건 미충족; MFI14=28.323, previous_MFI14=32.1727; 직전 완료 봉 목표를 다음 봉 시가에 모의 적용 |
| v2 | adx_14_trend | 9879.67 | -120.33 | sell / filled / Wilder ADX14 >= 25 그리고 +DI14 > -DI14; 조건 미충족; ADX14=23.6824, plus_DI14=22.3066, minus_DI14=19.9214; 직전 완료 봉 목표를 다음 봉 시가에 모의 적용 |
| v2 | aroon_25_trend | 9608.91 | -391.09 | sell / filled / Aroon25 Up > 70 그리고 Down < 30 (동률이면 최신 극값); 조건 미충족; Aroon_up=96, Aroon_down=100; 직전 완료 봉 목표를 다음 봉 시가에 모의 적용 |
| v2 | cci_20_momentum | 9862.73 | -137.27 | sell / filled / CCI20 > 100 (전형가격·평균절대편차); 조건 미충족; CCI20=99.2896; 직전 완료 봉 목표를 다음 봉 시가에 모의 적용 |
| v2 | williams_14_recovery | 9602.71 | -397.29 | sell / filled / 직전 Williams %R14 < -80, 현재 >= -80 (한 봉 목표); 조건 미충족; Williams_R14=-12.9449, previous_R14=-50.616; 직전 완료 봉 목표를 다음 봉 시가에 모의 적용 |
| v2 | cmf_20_accumulation | 9596.33 | -403.67 | buy / partial / Chaikin Money Flow20 > 0.1; 조건 충족; CMF20=0.197107, volume20=1.18305e+07; 직전 완료 봉 목표를 다음 봉 시가에 모의 적용 |
| v2 | chaikin_3_10 | 9533.66 | -466.34 | buy / partial / ADL의 EMA3 - EMA10 > 0 그리고 종가 > EMA26; 조건 충족; Chaikin3_10=722764, ADL=9.67933e+07, close=525.435, EMA26=523.774; 직전 완료 봉 목표를 다음 봉 시가에 모의 적용 |
| v2 | roc_10_momentum | 9957.44 | -42.56 | sell / filled / 10봉 ROC > 1% 그리고 종가 > EMA26; 조건 미충족; ROC10_percent=0.454191, close=534.125, EMA26=532.186; 직전 완료 봉 목표를 다음 봉 시가에 모의 적용 |
| v2 | trix_15_trend | 9549.45 | -450.55 | sell / filled / 15봉 삼중 EMA의 1봉 변화율 TRIX > 0 그리고 종가 > EMA26; 조건 미충족; TRIX15_percent=0.00481299, close=529.54, EMA26=531.788; 직전 완료 봉 목표를 다음 봉 시가에 모의 적용 |
| v2 | keltner_20_breakout | 9956.78 | -43.22 | sell / filled / 종가 > EMA20 + 2 x Wilder ATR14; 조건 미충족; close=533.975, upper_Keltner=534.357, EMA20=530.111, ATR14=2.12332; 직전 완료 봉 목표를 다음 봉 시가에 모의 적용 |
| v2 | opening_range_30m | 9608.57 | -391.43 | buy / partial / 뉴욕 09:30·09:45 두 완료 봉 최고가를 10:00 이후 종가가 돌파; 조건 충족; close=523.535, opening_high=522.36; 직전 완료 봉 목표를 다음 봉 시가에 모의 적용 |

### 같은 기간의 비용·노출 비교 (사후 연구)

| 전략 | 비용 전 | 비용 후 | 100% 보유 | 같은 평균 노출 보유 | 평균 노출 |
|---|---:|---:|---:|---:|---:|
| cash | 0.00% | 0.00% | 1.50% | 0.00% | 0.00% |
| buy_hold | 1.92% | 1.50% | 1.50% | 1.50% | 100.00% |
| trend_8_26 | -1.89% | -5.53% | 1.50% | 0.81% | 55.00% |
| momentum_26 | -0.06% | -6.56% | 1.50% | 0.80% | 54.21% |
| breakout_8 | 6.10% | -8.79% | 1.50% | 0.29% | 20.00% |
| reversion_12 | -5.62% | -14.31% | 1.50% | 0.38% | 26.32% |
| volume_26 | 1.20% | -7.73% | 1.50% | 0.13% | 8.68% |
| trend_8_26 AND momentum_26 | -1.50% | -7.12% | 1.50% | 0.72% | 48.68% |
| trend_8_26 + momentum_26 | -0.98% | -5.64% | 1.50% | 0.81% | 54.61% |
| trend_8_26 AND breakout_8 | -0.07% | -10.03% | 1.50% | 0.17% | 11.84% |
| trend_8_26 + breakout_8 | 2.04% | -6.58% | 1.50% | 0.55% | 37.51% |
| trend_8_26 AND reversion_12 | -2.35% | -7.92% | 1.50% | 0.10% | 7.11% |
| trend_8_26 + reversion_12 | -3.75% | -9.84% | 1.50% | 0.60% | 40.66% |
| trend_8_26 AND volume_26 | 2.38% | -1.01% | 1.50% | 0.04% | 2.63% |
| trend_8_26 + volume_26 | -0.35% | -6.25% | 1.50% | 0.47% | 31.85% |
| momentum_26 AND breakout_8 | 2.32% | -8.26% | 1.50% | 0.19% | 12.89% |
| momentum_26 + breakout_8 | 2.98% | -7.29% | 1.50% | 0.54% | 37.11% |
| momentum_26 AND reversion_12 | -3.05% | -8.20% | 1.50% | 0.11% | 7.89% |
| momentum_26 + reversion_12 | -2.86% | -9.95% | 1.50% | 0.59% | 40.27% |
| momentum_26 AND volume_26 | 1.56% | -2.61% | 1.50% | 0.05% | 3.16% |
| momentum_26 + volume_26 | 0.58% | -6.56% | 1.50% | 0.46% | 31.45% |
| breakout_8 AND reversion_12 | 0.00% | 0.00% | 1.50% | 0.00% | 0.00% |
| breakout_8 + reversion_12 | 0.09% | -10.85% | 1.50% | 0.34% | 23.17% |
| breakout_8 AND volume_26 | 1.98% | -0.14% | 1.50% | 0.02% | 1.58% |
| breakout_8 + volume_26 | 3.63% | -7.49% | 1.50% | 0.21% | 14.35% |
| reversion_12 AND volume_26 | -2.53% | -6.53% | 1.50% | 0.06% | 3.95% |
| reversion_12 + volume_26 | -2.26% | -10.90% | 1.50% | 0.26% | 17.51% |
| ema_12_26 | -1.50% | -4.35% | 1.50% | 0.81% | 54.74% |
| macd_12_26_9 | -1.57% | -6.41% | 1.50% | 0.47% | 32.11% |
| rsi_14_recovery | 0.73% | -3.42% | 1.50% | 0.04% | 2.63% |
| bollinger_20_reentry | -0.23% | -4.34% | 1.50% | 0.04% | 2.63% |
| donchian_20 | 0.99% | -3.97% | 1.50% | 0.06% | 3.95% |
| atr_14_breakout | 1.57% | -2.61% | 1.50% | 0.04% | 2.89% |
| session_vwap | 5.56% | -3.75% | 1.50% | 0.72% | 49.21% |
| obv_20 | 5.18% | -3.70% | 1.50% | 0.74% | 50.26% |
| stochastic_14_3_recovery | -0.05% | -9.25% | 1.50% | 0.09% | 6.05% |
| mfi_14_recovery | 1.71% | -2.47% | 1.50% | 0.04% | 2.63% |
| adx_14_trend | 4.03% | 1.87% | 1.50% | 0.64% | 43.68% |
| aroon_25_trend | -1.57% | -6.01% | 1.50% | 0.33% | 22.37% |
| cci_20_momentum | 2.91% | -3.38% | 1.50% | 0.30% | 20.79% |
| williams_14_recovery | -0.66% | -9.04% | 1.50% | 0.08% | 5.53% |
| cmf_20_accumulation | 0.71% | -6.23% | 1.50% | 0.65% | 44.21% |
| chaikin_3_10 | 3.67% | -4.68% | 1.50% | 0.74% | 50.00% |
| roc_10_momentum | -0.61% | -4.30% | 1.50% | 0.19% | 13.16% |
| trix_15_trend | -1.16% | -4.83% | 1.50% | 0.64% | 43.68% |
| keltner_20_breakout | 0.49% | -4.45% | 1.50% | 0.17% | 11.58% |
| opening_range_30m | -0.90% | -4.98% | 1.50% | 0.33% | 22.63% |

동일 구간·초기 자금, 종료 시 청산 비용 포함. 노출 맞춤은 사후 설명용이며 v2 실제 계좌 성과가 아닙니다.
[낙폭 분해·비용 영향·전체 구간](MSFT/comparison.json)

[v1 전체 기록](MSFT/accounts.json) · [v2 전체 기록](MSFT/accounts-v2.json)

## JPM 계좌

| 모델 | 전략 | 평가액 USD | 손익 USD | 최근 매매·이유 |
|---|---|---:|---:|---|
| v1 | cash | 10000.00 | 0.00 | 대기 /  / 새 신호 대기 |
| v1 | buy_hold | 9749.85 | -250.15 | buy /  / buy_hold: prior completed bar target 100%; next bar open simulation |
| v1 | trend_8_26 | 9572.38 | -427.62 | sell /  / trend_8_26: prior completed bar target 0%; next bar open simulation |
| v1 | momentum_26 | 9183.69 | -816.31 | sell /  / momentum_26: prior completed bar target 0%; next bar open simulation |
| v1 | breakout_8 | 9416.54 | -583.46 | sell /  / breakout_8: prior completed bar target 0%; next bar open simulation |
| v1 | reversion_12 | 9506.50 | -493.50 | sell /  / reversion_12: prior completed bar target 0%; next bar open simulation |
| v1 | volume_26 | 9846.15 | -153.85 | sell /  / volume_26: prior completed bar target 0%; next bar open simulation |
| v1 | trend_8_26 AND momentum_26 | 9441.00 | -559.00 | sell /  / trend_8_26 AND momentum_26: prior completed bar target 0%; next bar open simulation |
| v1 | trend_8_26 + momentum_26 | 9376.17 | -623.83 | sell /  / trend_8_26 + momentum_26: prior completed bar target 0%; next bar open simulation |
| v1 | trend_8_26 AND breakout_8 | 9638.65 | -361.35 | sell /  / trend_8_26 AND breakout_8: prior completed bar target 0%; next bar open simulation |
| v1 | trend_8_26 + breakout_8 | 9532.23 | -467.77 | sell /  / trend_8_26 + breakout_8: prior completed bar target 0%; next bar open simulation |
| v1 | trend_8_26 AND reversion_12 | 9687.22 | -312.78 | sell /  / trend_8_26 AND reversion_12: prior completed bar target 0%; next bar open simulation |
| v1 | trend_8_26 + reversion_12 | 9539.24 | -460.76 | sell /  / trend_8_26 + reversion_12: prior completed bar target 0%; next bar open simulation |
| v1 | trend_8_26 AND volume_26 | 10027.62 | 27.62 | sell /  / trend_8_26 AND volume_26: prior completed bar target 0%; next bar open simulation |
| v1 | trend_8_26 + volume_26 | 9708.16 | -291.84 | sell /  / trend_8_26 + volume_26: prior completed bar target 0%; next bar open simulation |
| v1 | momentum_26 AND breakout_8 | 9431.18 | -568.82 | sell /  / momentum_26 AND breakout_8: prior completed bar target 0%; next bar open simulation |
| v1 | momentum_26 + breakout_8 | 9299.50 | -700.50 | sell /  / momentum_26 + breakout_8: prior completed bar target 0%; next bar open simulation |
| v1 | momentum_26 AND reversion_12 | 9788.16 | -211.84 | sell /  / momentum_26 AND reversion_12: prior completed bar target 0%; next bar open simulation |
| v1 | momentum_26 + reversion_12 | 9456.31 | -543.69 | sell /  / momentum_26 + reversion_12: prior completed bar target 0%; next bar open simulation |
| v1 | momentum_26 AND volume_26 | 9871.31 | -128.69 | sell /  / momentum_26 AND volume_26: prior completed bar target 0%; next bar open simulation |
| v1 | momentum_26 + volume_26 | 9547.21 | -452.79 | sell /  / momentum_26 + volume_26: prior completed bar target 0%; next bar open simulation |
| v1 | breakout_8 AND reversion_12 | 10000.00 | 0.00 | 대기 /  / 새 신호 대기 |
| v1 | breakout_8 + reversion_12 | 9518.11 | -481.89 | sell /  / breakout_8 + reversion_12: prior completed bar target 0%; next bar open simulation |
| v1 | breakout_8 AND volume_26 | 9998.31 | -1.69 | sell /  / breakout_8 AND volume_26: prior completed bar target 0%; next bar open simulation |
| v1 | breakout_8 + volume_26 | 9648.21 | -351.79 | sell /  / breakout_8 + volume_26: prior completed bar target 0%; next bar open simulation |
| v1 | reversion_12 AND volume_26 | 9881.36 | -118.64 | sell /  / reversion_12 AND volume_26: prior completed bar target 0%; next bar open simulation |
| v1 | reversion_12 + volume_26 | 9713.44 | -286.56 | sell /  / reversion_12 + volume_26: prior completed bar target 0%; next bar open simulation |
| v1 | ema_12_26 | 9456.51 | -543.49 | sell /  / EMA12 > EMA26; 조건 미충족; EMA12=334.326, EMA26=334.511 |
| v1 | macd_12_26_9 | 9556.03 | -443.97 | sell /  / MACD > 신호선 그리고 MACD > 0; 조건 미충족; MACD=0.0530109, signal9=0.111707 |
| v1 | rsi_14_recovery | 9986.37 | -13.63 | sell /  / 직전 RSI14 < 30, 현재 RSI14 >= 30 (한 봉 목표); 조건 미충족; RSI14=61.6663, previous_RSI14=57.046 |
| v1 | bollinger_20_reentry | 9835.47 | -164.53 | sell /  / 직전 종가 < 직전 하단밴드, 현재 하단밴드 <= 종가 <= SMA20 (한 봉 목표); 조건 미충족; close=332.25, lower20=330.876, SMA20=334.012, previous_lower20=331.095 |
| v1 | donchian_20 | 9663.29 | -336.71 | sell /  / 종가 > 현재 봉을 제외한 직전 20봉 최고가; 조건 미충족; close=332.6, prior_high20=336.61 |
| v1 | atr_14_breakout | 9637.39 | -362.61 | sell /  / 종가 > 직전 종가 + 직전 ATR14 그리고 종가 > EMA26; 조건 미충족; close=332.6, threshold=337.371, prior_ATR14=0.861165, EMA26=334.725 |
| v1 | session_vwap | 9463.99 | -536.01 | buy /  / 종가 > 뉴욕 거래일별 누적 전형가격 VWAP; 조건 충족; close=332.25, session_VWAP=332.014, session_volume=1.2537e+06 |
| v1 | obv_20 | 9551.60 | -448.40 | sell /  / OBV > OBV의 SMA20 그리고 종가 > EMA26; 조건 미충족; OBV=-1.95307e+07, OBV_SMA20=-1.97351e+07, close=332.6, EMA26=334.725 |
| v1 | stochastic_14_3_recovery | 9561.90 | -438.10 | sell /  / 직전 %K14 < 20에서 %K14가 %D3 상향 돌파 (한 봉 목표); 조건 미충족; K14=29.7908, D3=19.2166, previous_K14=15.9424, previous_D3=14.3857 |
| v1 | mfi_14_recovery | 9935.64 | -64.36 | sell /  / 직전 MFI14 < 20, 현재 MFI14 >= 20 (한 봉 목표); 조건 미충족; MFI14=30.2719, previous_MFI14=26.8492 |
| v1 | adx_14_trend | 9726.68 | -273.32 | sell /  / Wilder ADX14 >= 25 그리고 +DI14 > -DI14; 조건 미충족; ADX14=23.9395, plus_DI14=23.2021, minus_DI14=22.594 |
| v1 | aroon_25_trend | 9769.62 | -230.38 | sell /  / Aroon25 Up > 70 그리고 Down < 30 (동률이면 최신 극값); 조건 미충족; Aroon_up=96, Aroon_down=100 |
| v1 | cci_20_momentum | 9681.01 | -318.99 | sell /  / CCI20 > 100 (전형가격·평균절대편차); 조건 미충족; CCI20=-280.713 |
| v1 | williams_14_recovery | 9533.71 | -466.29 | sell /  / 직전 Williams %R14 < -80, 현재 >= -80 (한 봉 목표); 조건 미충족; Williams_R14=-66.1834, previous_R14=-70.2092 |
| v1 | cmf_20_accumulation | 9670.72 | -329.28 | buy /  / Chaikin Money Flow20 > 0.1; 조건 충족; CMF20=0.106552, volume20=1.86088e+06 |
| v1 | chaikin_3_10 | 9553.87 | -446.13 | sell /  / ADL의 EMA3 - EMA10 > 0 그리고 종가 > EMA26; 조건 미충족; Chaikin3_10=268702, ADL=-8.90187e+06, close=332.6, EMA26=334.725 |
| v1 | roc_10_momentum | 9836.40 | -163.60 | sell /  / 10봉 ROC > 1% 그리고 종가 > EMA26; 조건 미충족; ROC10_percent=0.964142, close=337.72, EMA26=336.695 |
| v1 | trix_15_trend | 9614.50 | -385.50 | sell /  / 15봉 삼중 EMA의 1봉 변화율 TRIX > 0 그리고 종가 > EMA26; 조건 미충족; TRIX15_percent=0.00517218, close=332.6, EMA26=334.725 |
| v1 | keltner_20_breakout | 9905.24 | -94.76 | sell /  / 종가 > EMA20 + 2 x Wilder ATR14; 조건 미충족; close=339.04, upper_Keltner=339.281, EMA20=336.559, ATR14=1.36146 |
| v1 | opening_range_30m | 9795.03 | -204.97 | sell /  / 뉴욕 09:30·09:45 두 완료 봉 최고가를 10:00 이후 종가가 돌파; 자료 부족·변동폭 또는 거래량 없음: 대기; close=332.6 |
| v2 | cash | 10000.00 | 0.00 | 대기 /  / 새 신호 대기 |
| v2 | buy_hold | 9912.76 | -87.24 | buy / partial / 직전 완료 봉 목표 비중 100%; 다음 봉 시가 가정 |
| v2 | trend_8_26 | 9573.52 | -426.48 | sell / filled / 직전 완료 봉 목표 비중 0%; 다음 봉 시가 가정 |
| v2 | momentum_26 | 9060.89 | -939.11 | 중단: 손실 한도 / buy / partial / 직전 완료 봉 목표 비중 100%; 다음 봉 시가 가정 |
| v2 | breakout_8 | 8930.84 | -1069.16 | 중단: 손실 한도 / buy / partial / 직전 완료 봉 목표 비중 100%; 다음 봉 시가 가정 |
| v2 | reversion_12 | 9470.41 | -529.59 | sell / filled / 직전 완료 봉 목표 비중 0%; 다음 봉 시가 가정 |
| v2 | volume_26 | 9661.98 | -338.02 | sell / filled / 직전 완료 봉 목표 비중 0%; 다음 봉 시가 가정 |
| v2 | trend_8_26 AND momentum_26 | 9395.85 | -604.15 | sell / filled / 직전 완료 봉 목표 비중 0%; 다음 봉 시가 가정 |
| v2 | trend_8_26 + momentum_26 | 9150.71 | -849.29 | sell / filled / 직전 완료 봉 목표 비중 0%; 다음 봉 시가 가정 |
| v2 | trend_8_26 AND breakout_8 | 9019.37 | -980.63 | sell / filled / 직전 완료 봉 목표 비중 0%; 다음 봉 시가 가정 |
| v2 | trend_8_26 + breakout_8 | 9201.55 | -798.45 | sell / filled / 직전 완료 봉 목표 비중 0%; 다음 봉 시가 가정 |
| v2 | trend_8_26 AND reversion_12 | 9657.80 | -342.20 | sell / filled / 직전 완료 봉 목표 비중 0%; 다음 봉 시가 가정 |
| v2 | trend_8_26 + reversion_12 | 9561.93 | -438.07 | sell / filled / 직전 완료 봉 목표 비중 0%; 다음 봉 시가 가정 |
| v2 | trend_8_26 AND volume_26 | 9821.47 | -178.53 | sell / filled / 직전 완료 봉 목표 비중 0%; 다음 봉 시가 가정 |
| v2 | trend_8_26 + volume_26 | 9618.29 | -381.71 | sell / filled / 직전 완료 봉 목표 비중 0%; 다음 봉 시가 가정 |
| v2 | momentum_26 AND breakout_8 | 8883.35 | -1116.65 | 중단: 손실 한도 / buy / partial / 직전 완료 봉 목표 비중 100%; 다음 봉 시가 가정 |
| v2 | momentum_26 + breakout_8 | 8995.36 | -1004.64 | 중단: 손실 한도 / sell / filled / 직전 완료 봉 목표 비중 0%; 다음 봉 시가 가정 |
| v2 | momentum_26 AND reversion_12 | 9730.22 | -269.78 | sell / filled / 직전 완료 봉 목표 비중 0%; 다음 봉 시가 가정 |
| v2 | momentum_26 + reversion_12 | 9313.65 | -686.35 | sell / filled / 직전 완료 봉 목표 비중 0%; 다음 봉 시가 가정 |
| v2 | momentum_26 AND volume_26 | 9668.38 | -331.62 | sell / filled / 직전 완료 봉 목표 비중 0%; 다음 봉 시가 가정 |
| v2 | momentum_26 + volume_26 | 9270.91 | -729.09 | sell / filled / 직전 완료 봉 목표 비중 0%; 다음 봉 시가 가정 |
| v2 | breakout_8 AND reversion_12 | 10000.00 | 0.00 | 대기 /  / 새 신호 대기 |
| v2 | breakout_8 + reversion_12 | 9208.60 | -791.40 | sell / filled / 직전 완료 봉 목표 비중 0%; 다음 봉 시가 가정 |
| v2 | breakout_8 AND volume_26 | 9883.76 | -116.24 | sell / filled / 직전 완료 봉 목표 비중 0%; 다음 봉 시가 가정 |
| v2 | breakout_8 + volume_26 | 9243.03 | -756.97 | sell / filled / 직전 완료 봉 목표 비중 0%; 다음 봉 시가 가정 |
| v2 | reversion_12 AND volume_26 | 9926.17 | -73.83 | sell / filled / 직전 완료 봉 목표 비중 0%; 다음 봉 시가 가정 |
| v2 | reversion_12 + volume_26 | 9626.24 | -373.76 | sell / filled / 직전 완료 봉 목표 비중 0%; 다음 봉 시가 가정 |
| v2 | ema_12_26 | 9447.06 | -552.94 | sell / filled / EMA12 > EMA26; 조건 미충족; EMA12=334.326, EMA26=334.511; 직전 완료 봉 목표를 다음 봉 시가에 모의 적용 |
| v2 | macd_12_26_9 | 9546.47 | -453.53 | sell / filled / MACD > 신호선 그리고 MACD > 0; 조건 미충족; MACD=0.0530109, signal9=0.111707; 직전 완료 봉 목표를 다음 봉 시가에 모의 적용 |
| v2 | rsi_14_recovery | 9984.37 | -15.63 | sell / filled / 직전 RSI14 < 30, 현재 RSI14 >= 30 (한 봉 목표); 조건 미충족; RSI14=61.6663, previous_RSI14=57.046; 직전 완료 봉 목표를 다음 봉 시가에 모의 적용 |
| v2 | bollinger_20_reentry | 9825.64 | -174.36 | sell / filled / 직전 종가 < 직전 하단밴드, 현재 하단밴드 <= 종가 <= SMA20 (한 봉 목표); 조건 미충족; close=332.25, lower20=330.876, SMA20=334.012, previous_lower20=331.095; 직전 완료 봉 목표를 다음 봉 시가에 모의 적용 |
| v2 | donchian_20 | 9653.63 | -346.37 | sell / filled / 종가 > 현재 봉을 제외한 직전 20봉 최고가; 조건 미충족; close=332.6, prior_high20=336.61; 직전 완료 봉 목표를 다음 봉 시가에 모의 적용 |
| v2 | atr_14_breakout | 9621.98 | -378.02 | sell / filled / 종가 > 직전 종가 + 직전 ATR14 그리고 종가 > EMA26; 조건 미충족; close=332.6, threshold=337.371, prior_ATR14=0.861165, EMA26=334.725; 직전 완료 봉 목표를 다음 봉 시가에 모의 적용 |
| v2 | session_vwap | 9446.03 | -553.97 | buy / partial / 종가 > 뉴욕 거래일별 누적 전형가격 VWAP; 조건 충족; close=332.25, session_VWAP=332.014, session_volume=1.2537e+06; 직전 완료 봉 목표를 다음 봉 시가에 모의 적용 |
| v2 | obv_20 | 9532.52 | -467.48 | sell / filled / OBV > OBV의 SMA20 그리고 종가 > EMA26; 조건 미충족; OBV=-1.95307e+07, OBV_SMA20=-1.97351e+07, close=332.6, EMA26=334.725; 직전 완료 봉 목표를 다음 봉 시가에 모의 적용 |
| v2 | stochastic_14_3_recovery | 9537.08 | -462.92 | sell / filled / 직전 %K14 < 20에서 %K14가 %D3 상향 돌파 (한 봉 목표); 조건 미충족; K14=29.7908, D3=19.2166, previous_K14=15.9424, previous_D3=14.3857; 직전 완료 봉 목표를 다음 봉 시가에 모의 적용 |
| v2 | mfi_14_recovery | 9931.66 | -68.34 | sell / filled / 직전 MFI14 < 20, 현재 MFI14 >= 20 (한 봉 목표); 조건 미충족; MFI14=30.2719, previous_MFI14=26.8492; 직전 완료 봉 목표를 다음 봉 시가에 모의 적용 |
| v2 | adx_14_trend | 9722.79 | -277.21 | sell / filled / Wilder ADX14 >= 25 그리고 +DI14 > -DI14; 조건 미충족; ADX14=23.9395, plus_DI14=23.2021, minus_DI14=22.594; 직전 완료 봉 목표를 다음 봉 시가에 모의 적용 |
| v2 | aroon_25_trend | 9765.71 | -234.29 | sell / filled / Aroon25 Up > 70 그리고 Down < 30 (동률이면 최신 극값); 조건 미충족; Aroon_up=96, Aroon_down=100; 직전 완료 봉 목표를 다음 봉 시가에 모의 적용 |
| v2 | cci_20_momentum | 9671.34 | -328.66 | sell / filled / CCI20 > 100 (전형가격·평균절대편차); 조건 미충족; CCI20=-280.713; 직전 완료 봉 목표를 다음 봉 시가에 모의 적용 |
| v2 | williams_14_recovery | 9510.86 | -489.14 | sell / filled / 직전 Williams %R14 < -80, 현재 >= -80 (한 봉 목표); 조건 미충족; Williams_R14=-66.1834, previous_R14=-70.2092; 직전 완료 봉 목표를 다음 봉 시가에 모의 적용 |
| v2 | cmf_20_accumulation | 9662.02 | -337.98 | buy / partial / Chaikin Money Flow20 > 0.1; 조건 충족; CMF20=0.106552, volume20=1.86088e+06; 직전 완료 봉 목표를 다음 봉 시가에 모의 적용 |
| v2 | chaikin_3_10 | 9536.68 | -463.32 | sell / filled / ADL의 EMA3 - EMA10 > 0 그리고 종가 > EMA26; 조건 미충족; Chaikin3_10=268702, ADL=-8.90187e+06, close=332.6, EMA26=334.725; 직전 완료 봉 목표를 다음 봉 시가에 모의 적용 |
| v2 | roc_10_momentum | 9832.47 | -167.53 | sell / filled / 10봉 ROC > 1% 그리고 종가 > EMA26; 조건 미충족; ROC10_percent=0.964142, close=337.72, EMA26=336.695; 직전 완료 봉 목표를 다음 봉 시가에 모의 적용 |
| v2 | trix_15_trend | 9604.89 | -395.11 | sell / filled / 15봉 삼중 EMA의 1봉 변화율 TRIX > 0 그리고 종가 > EMA26; 조건 미충족; TRIX15_percent=0.00517218, close=332.6, EMA26=334.725; 직전 완료 봉 목표를 다음 봉 시가에 모의 적용 |
| v2 | keltner_20_breakout | 9901.28 | -98.72 | sell / filled / 종가 > EMA20 + 2 x Wilder ATR14; 조건 미충족; close=339.04, upper_Keltner=339.281, EMA20=336.559, ATR14=1.36146; 직전 완료 봉 목표를 다음 봉 시가에 모의 적용 |
| v2 | opening_range_30m | 9789.16 | -210.84 | sell / filled / 뉴욕 09:30·09:45 두 완료 봉 최고가를 10:00 이후 종가가 돌파; 자료 부족·변동폭 또는 거래량 없음: 대기; close=332.6; 직전 완료 봉 목표를 다음 봉 시가에 모의 적용 |

### 같은 기간의 비용·노출 비교 (사후 연구)

| 전략 | 비용 전 | 비용 후 | 100% 보유 | 같은 평균 노출 보유 | 평균 노출 |
|---|---:|---:|---:|---:|---:|
| cash | 0.00% | 0.00% | -0.18% | -0.00% | 0.00% |
| buy_hold | 0.24% | -0.18% | -0.18% | -0.18% | 100.00% |
| trend_8_26 | -0.61% | -4.70% | -0.18% | -0.10% | 55.00% |
| momentum_26 | -4.62% | -13.76% | -0.18% | -0.10% | 53.16% |
| breakout_8 | -3.77% | -19.33% | -0.18% | -0.04% | 19.47% |
| reversion_12 | 6.42% | -8.13% | -0.18% | -0.04% | 24.21% |
| volume_26 | 0.98% | -5.58% | -0.18% | -0.01% | 6.84% |
| trend_8_26 AND momentum_26 | -0.41% | -6.49% | -0.18% | -0.08% | 41.58% |
| trend_8_26 + momentum_26 | -2.62% | -9.15% | -0.18% | -0.10% | 54.08% |
| trend_8_26 AND breakout_8 | -3.52% | -14.23% | -0.18% | -0.02% | 12.11% |
| trend_8_26 + breakout_8 | -2.18% | -11.75% | -0.18% | -0.07% | 37.24% |
| trend_8_26 AND reversion_12 | 1.62% | -4.98% | -0.18% | -0.01% | 8.16% |
| trend_8_26 + reversion_12 | 2.87% | -6.04% | -0.18% | -0.07% | 39.61% |
| trend_8_26 AND volume_26 | 0.31% | -3.41% | -0.18% | -0.01% | 4.47% |
| trend_8_26 + volume_26 | 0.20% | -5.13% | -0.18% | -0.06% | 30.92% |
| momentum_26 AND breakout_8 | -3.71% | -15.46% | -0.18% | -0.02% | 12.63% |
| momentum_26 + breakout_8 | -4.17% | -16.40% | -0.18% | -0.07% | 36.32% |
| momentum_26 AND reversion_12 | 1.94% | -4.68% | -0.18% | -0.01% | 6.58% |
| momentum_26 + reversion_12 | 0.78% | -8.53% | -0.18% | -0.07% | 38.69% |
| momentum_26 AND volume_26 | -0.68% | -3.96% | -0.18% | -0.01% | 3.16% |
| momentum_26 + volume_26 | -1.83% | -9.19% | -0.18% | -0.06% | 30.00% |
| breakout_8 AND reversion_12 | 0.00% | 0.00% | -0.18% | -0.00% | 0.00% |
| breakout_8 + reversion_12 | 1.22% | -12.64% | -0.18% | -0.04% | 21.85% |
| breakout_8 AND volume_26 | 0.27% | -2.22% | -0.18% | -0.00% | 1.58% |
| breakout_8 + volume_26 | -1.41% | -11.80% | -0.18% | -0.02% | 13.16% |
| reversion_12 AND volume_26 | 1.89% | -1.06% | -0.18% | -0.00% | 2.37% |
| reversion_12 + volume_26 | 3.68% | -5.68% | -0.18% | -0.03% | 15.53% |
| ema_12_26 | -1.79% | -5.83% | -0.18% | -0.10% | 51.84% |
| macd_12_26_9 | -1.73% | -6.95% | -0.18% | -0.06% | 33.68% |
| rsi_14_recovery | 0.40% | -0.86% | -0.18% | -0.00% | 0.79% |
| bollinger_20_reentry | 1.01% | -3.15% | -0.18% | -0.00% | 2.63% |
| donchian_20 | -2.16% | -5.78% | -0.18% | -0.01% | 3.16% |
| atr_14_breakout | -1.11% | -9.08% | -0.18% | -0.01% | 5.53% |
| session_vwap | -0.26% | -10.95% | -0.18% | -0.10% | 51.58% |
| obv_20 | -3.99% | -16.42% | -0.18% | -0.06% | 30.00% |
| stochastic_14_3_recovery | 0.18% | -9.80% | -0.18% | -0.01% | 6.58% |
| mfi_14_recovery | 0.12% | -1.13% | -0.18% | -0.00% | 0.79% |
| adx_14_trend | -2.34% | -4.37% | -0.18% | -0.05% | 25.00% |
| aroon_25_trend | -0.64% | -4.32% | -0.18% | -0.03% | 18.42% |
| cci_20_momentum | -3.50% | -12.02% | -0.18% | -0.03% | 17.37% |
| williams_14_recovery | -0.35% | -9.52% | -0.18% | -0.01% | 6.05% |
| cmf_20_accumulation | -2.41% | -10.27% | -0.18% | -0.06% | 35.00% |
| chaikin_3_10 | 0.96% | -8.72% | -0.18% | -0.07% | 35.53% |
| roc_10_momentum | -1.40% | -3.86% | -0.18% | -0.01% | 6.58% |
| trix_15_trend | -0.93% | -7.75% | -0.18% | -0.06% | 35.26% |
| keltner_20_breakout | -0.35% | -2.83% | -0.18% | -0.01% | 3.95% |
| opening_range_30m | -0.69% | -4.38% | -0.18% | -0.03% | 17.11% |

동일 구간·초기 자금, 종료 시 청산 비용 포함. 노출 맞춤은 사후 설명용이며 v2 실제 계좌 성과가 아닙니다.
[낙폭 분해·비용 영향·전체 구간](JPM/comparison.json)

[v1 전체 기록](JPM/accounts.json) · [v2 전체 기록](JPM/accounts-v2.json)

## XOM 계좌

| 모델 | 전략 | 평가액 USD | 손익 USD | 최근 매매·이유 |
|---|---|---:|---:|---|
| v1 | cash | 10000.00 | 0.00 | 대기 /  / 새 신호 대기 |
| v1 | buy_hold | 10350.99 | 350.99 | buy /  / buy_hold: prior completed bar target 100%; next bar open simulation |
| v1 | trend_8_26 | 9999.33 | -0.67 | buy /  / trend_8_26: prior completed bar target 100%; next bar open simulation |
| v1 | momentum_26 | 9993.05 | -6.95 | buy /  / momentum_26: prior completed bar target 100%; next bar open simulation |
| v1 | breakout_8 | 9481.80 | -518.20 | sell /  / breakout_8: prior completed bar target 0%; next bar open simulation |
| v1 | reversion_12 | 9541.48 | -458.52 | sell /  / reversion_12: prior completed bar target 0%; next bar open simulation |
| v1 | volume_26 | 9554.35 | -445.65 | sell /  / volume_26: prior completed bar target 0%; next bar open simulation |
| v1 | trend_8_26 AND momentum_26 | 9860.82 | -139.18 | buy /  / trend_8_26 AND momentum_26: prior completed bar target 100%; next bar open simulation |
| v1 | trend_8_26 + momentum_26 | 9996.46 | -3.54 | buy /  / trend_8_26 + momentum_26: prior completed bar target 100%; next bar open simulation |
| v1 | trend_8_26 AND breakout_8 | 9693.28 | -306.72 | sell /  / trend_8_26 AND breakout_8: prior completed bar target 0%; next bar open simulation |
| v1 | trend_8_26 + breakout_8 | 9776.86 | -223.14 | sell /  / trend_8_26 + breakout_8: prior completed bar target 50%; next bar open simulation |
| v1 | trend_8_26 AND reversion_12 | 9569.59 | -430.41 | sell /  / trend_8_26 AND reversion_12: prior completed bar target 0%; next bar open simulation |
| v1 | trend_8_26 + reversion_12 | 9767.88 | -232.12 | buy /  / trend_8_26 + reversion_12: prior completed bar target 50%; next bar open simulation |
| v1 | trend_8_26 AND volume_26 | 9669.14 | -330.86 | sell /  / trend_8_26 AND volume_26: prior completed bar target 0%; next bar open simulation |
| v1 | trend_8_26 + volume_26 | 9774.86 | -225.14 | buy /  / trend_8_26 + volume_26: prior completed bar target 50%; next bar open simulation |
| v1 | momentum_26 AND breakout_8 | 9813.21 | -186.79 | sell /  / momentum_26 AND breakout_8: prior completed bar target 0%; next bar open simulation |
| v1 | momentum_26 + breakout_8 | 9734.50 | -265.50 | sell /  / momentum_26 + breakout_8: prior completed bar target 50%; next bar open simulation |
| v1 | momentum_26 AND reversion_12 | 9667.08 | -332.92 | sell /  / momentum_26 AND reversion_12: prior completed bar target 0%; next bar open simulation |
| v1 | momentum_26 + reversion_12 | 9764.68 | -235.32 | buy /  / momentum_26 + reversion_12: prior completed bar target 50%; next bar open simulation |
| v1 | momentum_26 AND volume_26 | 9888.17 | -111.83 | sell /  / momentum_26 AND volume_26: prior completed bar target 0%; next bar open simulation |
| v1 | momentum_26 + volume_26 | 9771.46 | -228.54 | buy /  / momentum_26 + volume_26: prior completed bar target 50%; next bar open simulation |
| v1 | breakout_8 AND reversion_12 | 10000.00 | 0.00 | 대기 /  / 새 신호 대기 |
| v1 | breakout_8 + reversion_12 | 9530.60 | -469.40 | sell /  / breakout_8 + reversion_12: prior completed bar target 0%; next bar open simulation |
| v1 | breakout_8 AND volume_26 | 9896.24 | -103.76 | sell /  / breakout_8 AND volume_26: prior completed bar target 0%; next bar open simulation |
| v1 | breakout_8 + volume_26 | 9517.91 | -482.09 | sell /  / breakout_8 + volume_26: prior completed bar target 0%; next bar open simulation |
| v1 | reversion_12 AND volume_26 | 9794.27 | -205.73 | sell /  / reversion_12 AND volume_26: prior completed bar target 0%; next bar open simulation |
| v1 | reversion_12 + volume_26 | 9548.09 | -451.91 | sell /  / reversion_12 + volume_26: prior completed bar target 0%; next bar open simulation |
| v1 | ema_12_26 | 10068.09 | 68.09 | buy /  / EMA12 > EMA26; 조건 충족; EMA12=176.974, EMA26=176.95 |
| v1 | macd_12_26_9 | 10108.49 | 108.49 | buy /  / MACD > 신호선 그리고 MACD > 0; 조건 충족; MACD=0.0238028, signal9=-0.152108 |
| v1 | rsi_14_recovery | 9927.64 | -72.36 | sell /  / 직전 RSI14 < 30, 현재 RSI14 >= 30 (한 봉 목표); 조건 미충족; RSI14=37.639, previous_RSI14=31.1023 |
| v1 | bollinger_20_reentry | 9694.21 | -305.79 | sell /  / 직전 종가 < 직전 하단밴드, 현재 하단밴드 <= 종가 <= SMA20 (한 봉 목표); 조건 미충족; close=175.53, lower20=174.782, SMA20=177.101, previous_lower20=174.994 |
| v1 | donchian_20 | 9754.38 | -245.62 | sell /  / 종가 > 현재 봉을 제외한 직전 20봉 최고가; 조건 미충족; close=183.28, prior_high20=183.3 |
| v1 | atr_14_breakout | 9789.04 | -210.96 | sell /  / 종가 > 직전 종가 + 직전 ATR14 그리고 종가 > EMA26; 조건 미충족; close=181.355, threshold=182.652, prior_ATR14=0.727068, EMA26=178.133 |
| v1 | session_vwap | 10111.26 | 111.26 | buy /  / 종가 > 뉴욕 거래일별 누적 전형가격 VWAP; 조건 충족; close=176.86, session_VWAP=176.627, session_volume=3.72585e+06 |
| v1 | obv_20 | 9570.70 | -429.30 | buy /  / OBV > OBV의 SMA20 그리고 종가 > EMA26; 조건 충족; OBV=2.26159e+07, OBV_SMA20=2.18428e+07, close=176.86, EMA26=176.75 |
| v1 | stochastic_14_3_recovery | 9636.26 | -363.74 | sell /  / 직전 %K14 < 20에서 %K14가 %D3 상향 돌파 (한 봉 목표); 조건 미충족; K14=11.8836, D3=5.65987, previous_K14=4.66302, previous_D3=2.02546 |
| v1 | mfi_14_recovery | 10000.00 | 0.00 | 대기 /  / 새 신호 대기 |
| v1 | adx_14_trend | 10071.66 | 71.66 | buy /  / Wilder ADX14 >= 25 그리고 +DI14 > -DI14; 조건 충족; ADX14=26.2258, plus_DI14=52.4409, minus_DI14=10.4732 |
| v1 | aroon_25_trend | 9683.38 | -316.62 | buy /  / Aroon25 Up > 70 그리고 Down < 30 (동률이면 최신 극값); 조건 충족; Aroon_up=100, Aroon_down=28 |
| v1 | cci_20_momentum | 9479.59 | -520.41 | buy /  / CCI20 > 100 (전형가격·평균절대편차); 조건 충족; CCI20=263.413 |
| v1 | williams_14_recovery | 9643.01 | -356.99 | sell /  / 직전 Williams %R14 < -80, 현재 >= -80 (한 봉 목표); 조건 미충족; Williams_R14=-68.9948, previous_R14=-74.4719 |
| v1 | cmf_20_accumulation | 9968.06 | -31.94 | buy /  / Chaikin Money Flow20 > 0.1; 조건 충족; CMF20=0.202217, volume20=4.5047e+06 |
| v1 | chaikin_3_10 | 9930.01 | -69.99 | buy /  / ADL의 EMA3 - EMA10 > 0 그리고 종가 > EMA26; 조건 충족; Chaikin3_10=152048, ADL=2.84951e+07, close=176.86, EMA26=176.75 |
| v1 | roc_10_momentum | 9920.07 | -79.93 | buy /  / 10봉 ROC > 1% 그리고 종가 > EMA26; 조건 충족; ROC10_percent=2.14562, close=180.905, EMA26=177.551 |
| v1 | trix_15_trend | 10017.91 | 17.91 | buy /  / 15봉 삼중 EMA의 1봉 변화율 TRIX > 0 그리고 종가 > EMA26; 조건 충족; TRIX15_percent=0.00288954, close=177.71, EMA26=177.21 |
| v1 | keltner_20_breakout | 9958.36 | -41.64 | buy /  / 종가 > EMA20 + 2 x Wilder ATR14; 조건 충족; close=180.905, upper_Keltner=179.045, EMA20=177.683, ATR14=0.680695 |
| v1 | opening_range_30m | 10000.73 | 0.73 | buy /  / 뉴욕 09:30·09:45 두 완료 봉 최고가를 10:00 이후 종가가 돌파; 조건 충족; close=182.19, opening_high=181.96 |
| v2 | cash | 10000.00 | 0.00 | 대기 /  / 새 신호 대기 |
| v2 | buy_hold | 10681.32 | 681.32 | buy / partial / 직전 완료 봉 목표 비중 100%; 다음 봉 시가 가정 |
| v2 | trend_8_26 | 10086.50 | 86.50 | buy / partial / 직전 완료 봉 목표 비중 100%; 다음 봉 시가 가정 |
| v2 | momentum_26 | 10158.46 | 158.46 | buy / partial / 직전 완료 봉 목표 비중 100%; 다음 봉 시가 가정 |
| v2 | breakout_8 | 8988.95 | -1011.05 | 중단: 손실 한도 / sell / filled / 직전 완료 봉 목표 비중 0%; 다음 봉 시가 가정 |
| v2 | reversion_12 | 9355.66 | -644.34 | sell / filled / 직전 완료 봉 목표 비중 0%; 다음 봉 시가 가정 |
| v2 | volume_26 | 9451.35 | -548.65 | sell / filled / 직전 완료 봉 목표 비중 0%; 다음 봉 시가 가정 |
| v2 | trend_8_26 AND momentum_26 | 9952.16 | -47.84 | buy / partial / 직전 완료 봉 목표 비중 100%; 다음 봉 시가 가정 |
| v2 | trend_8_26 + momentum_26 | 10122.71 | 122.71 | buy / partial / 직전 완료 봉 목표 비중 100%; 다음 봉 시가 가정 |
| v2 | trend_8_26 AND breakout_8 | 9139.97 | -860.03 | sell / filled / 직전 완료 봉 목표 비중 0%; 다음 봉 시가 가정 |
| v2 | trend_8_26 + breakout_8 | 9560.31 | -439.69 | sell / filled / 직전 완료 봉 목표 비중 50%; 다음 봉 시가 가정 |
| v2 | trend_8_26 AND reversion_12 | 9406.78 | -593.22 | sell / filled / 직전 완료 봉 목표 비중 0%; 다음 봉 시가 가정 |
| v2 | trend_8_26 + reversion_12 | 9714.41 | -285.59 | buy / filled / 직전 완료 봉 목표 비중 50%; 다음 봉 시가 가정 |
| v2 | trend_8_26 AND volume_26 | 9556.73 | -443.27 | sell / filled / 직전 완료 봉 목표 비중 0%; 다음 봉 시가 가정 |
| v2 | trend_8_26 + volume_26 | 9764.24 | -235.76 | buy / filled / 직전 완료 봉 목표 비중 50%; 다음 봉 시가 가정 |
| v2 | momentum_26 AND breakout_8 | 9273.68 | -726.32 | sell / filled / 직전 완료 봉 목표 비중 0%; 다음 봉 시가 가정 |
| v2 | momentum_26 + breakout_8 | 9533.99 | -466.01 | sell / filled / 직전 완료 봉 목표 비중 50%; 다음 봉 시가 가정 |
| v2 | momentum_26 AND reversion_12 | 9466.29 | -533.71 | sell / filled / 직전 완료 봉 목표 비중 0%; 다음 봉 시가 가정 |
| v2 | momentum_26 + reversion_12 | 9748.90 | -251.10 | buy / filled / 직전 완료 봉 목표 비중 50%; 다음 봉 시가 가정 |
| v2 | momentum_26 AND volume_26 | 9838.73 | -161.27 | sell / filled / 직전 완료 봉 목표 비중 0%; 다음 봉 시가 가정 |
| v2 | momentum_26 + volume_26 | 9819.26 | -180.74 | buy / filled / 직전 완료 봉 목표 비중 50%; 다음 봉 시가 가정 |
| v2 | breakout_8 AND reversion_12 | 10000.00 | 0.00 | 대기 /  / 새 신호 대기 |
| v2 | breakout_8 + reversion_12 | 9167.68 | -832.32 | sell / filled / 직전 완료 봉 목표 비중 0%; 다음 봉 시가 가정 |
| v2 | breakout_8 AND volume_26 | 9860.88 | -139.12 | sell / filled / 직전 완료 봉 목표 비중 0%; 다음 봉 시가 가정 |
| v2 | breakout_8 + volume_26 | 9214.41 | -785.59 | sell / filled / 직전 완료 봉 목표 비중 0%; 다음 봉 시가 가정 |
| v2 | reversion_12 AND volume_26 | 9737.38 | -262.62 | sell / filled / 직전 완료 봉 목표 비중 0%; 다음 봉 시가 가정 |
| v2 | reversion_12 + volume_26 | 9423.33 | -576.67 | sell / filled / 직전 완료 봉 목표 비중 0%; 다음 봉 시가 가정 |
| v2 | ema_12_26 | 10061.04 | 61.04 | buy / partial / EMA12 > EMA26; 조건 충족; EMA12=176.974, EMA26=176.95; 직전 완료 봉 목표를 다음 봉 시가에 모의 적용 |
| v2 | macd_12_26_9 | 10097.38 | 97.38 | buy / partial / MACD > 신호선 그리고 MACD > 0; 조건 충족; MACD=0.0238028, signal9=-0.152108; 직전 완료 봉 목표를 다음 봉 시가에 모의 적용 |
| v2 | rsi_14_recovery | 9923.67 | -76.33 | sell / filled / 직전 RSI14 < 30, 현재 RSI14 >= 30 (한 봉 목표); 조건 미충족; RSI14=37.639, previous_RSI14=31.1023; 직전 완료 봉 목표를 다음 봉 시가에 모의 적용 |
| v2 | bollinger_20_reentry | 9684.52 | -315.48 | sell / filled / 직전 종가 < 직전 하단밴드, 현재 하단밴드 <= 종가 <= SMA20 (한 봉 목표); 조건 미충족; close=175.53, lower20=174.782, SMA20=177.101, previous_lower20=174.994; 직전 완료 봉 목표를 다음 봉 시가에 모의 적용 |
| v2 | donchian_20 | 9738.78 | -261.22 | sell / filled / 종가 > 현재 봉을 제외한 직전 20봉 최고가; 조건 미충족; close=183.28, prior_high20=183.3; 직전 완료 봉 목표를 다음 봉 시가에 모의 적용 |
| v2 | atr_14_breakout | 9777.30 | -222.70 | sell / filled / 종가 > 직전 종가 + 직전 ATR14 그리고 종가 > EMA26; 조건 미충족; close=181.355, threshold=182.652, prior_ATR14=0.727068, EMA26=178.133; 직전 완료 봉 목표를 다음 봉 시가에 모의 적용 |
| v2 | session_vwap | 10096.11 | 96.11 | buy / partial / 종가 > 뉴욕 거래일별 누적 전형가격 VWAP; 조건 충족; close=176.86, session_VWAP=176.627, session_volume=3.72585e+06; 직전 완료 봉 목표를 다음 봉 시가에 모의 적용 |
| v2 | obv_20 | 9502.46 | -497.54 | 중단: 손실 한도 / sell / filled / OBV > OBV의 SMA20 그리고 종가 > EMA26; 조건 미충족; OBV=2.24329e+07, OBV_SMA20=2.30895e+07, close=177.005, EMA26=177.393; 직전 완료 봉 목표를 다음 봉 시가에 모의 적용 |
| v2 | stochastic_14_3_recovery | 9622.78 | -377.22 | sell / filled / 직전 %K14 < 20에서 %K14가 %D3 상향 돌파 (한 봉 목표); 조건 미충족; K14=11.8836, D3=5.65987, previous_K14=4.66302, previous_D3=2.02546; 직전 완료 봉 목표를 다음 봉 시가에 모의 적용 |
| v2 | mfi_14_recovery | 10000.00 | 0.00 | 대기 /  / 새 신호 대기 |
| v2 | adx_14_trend | 10064.62 | 64.62 | buy / partial / Wilder ADX14 >= 25 그리고 +DI14 > -DI14; 조건 충족; ADX14=26.2258, plus_DI14=52.4409, minus_DI14=10.4732; 직전 완료 봉 목표를 다음 봉 시가에 모의 적용 |
| v2 | aroon_25_trend | 9674.67 | -325.33 | buy / partial / Aroon25 Up > 70 그리고 Down < 30 (동률이면 최신 극값); 조건 충족; Aroon_up=100, Aroon_down=28; 직전 완료 봉 목표를 다음 봉 시가에 모의 적용 |
| v2 | cci_20_momentum | 9455.92 | -544.08 | buy / partial / CCI20 > 100 (전형가격·평균절대편차); 조건 충족; CCI20=263.413; 직전 완료 봉 목표를 다음 봉 시가에 모의 적용 |
| v2 | williams_14_recovery | 9629.52 | -370.48 | sell / filled / 직전 Williams %R14 < -80, 현재 >= -80 (한 봉 목표); 조건 미충족; Williams_R14=-68.9948, previous_R14=-74.4719; 직전 완료 봉 목표를 다음 봉 시가에 모의 적용 |
| v2 | cmf_20_accumulation | 9955.11 | -44.89 | buy / partial / Chaikin Money Flow20 > 0.1; 조건 충족; CMF20=0.202217, volume20=4.5047e+06; 직전 완료 봉 목표를 다음 봉 시가에 모의 적용 |
| v2 | chaikin_3_10 | 9913.14 | -86.86 | buy / partial / ADL의 EMA3 - EMA10 > 0 그리고 종가 > EMA26; 조건 충족; Chaikin3_10=152048, ADL=2.87515e+07, close=176.86, EMA26=176.75; 직전 완료 봉 목표를 다음 봉 시가에 모의 적용 |
| v2 | roc_10_momentum | 9909.16 | -90.84 | buy / partial / 10봉 ROC > 1% 그리고 종가 > EMA26; 조건 충족; ROC10_percent=2.14562, close=180.905, EMA26=177.551; 직전 완료 봉 목표를 다음 봉 시가에 모의 적용 |
| v2 | trix_15_trend | 10004.90 | 4.90 | buy / partial / 15봉 삼중 EMA의 1봉 변화율 TRIX > 0 그리고 종가 > EMA26; 조건 충족; TRIX15_percent=0.00288954, close=177.71, EMA26=177.21; 직전 완료 봉 목표를 다음 봉 시가에 모의 적용 |
| v2 | keltner_20_breakout | 9949.40 | -50.60 | buy / partial / 종가 > EMA20 + 2 x Wilder ATR14; 조건 충족; close=180.905, upper_Keltner=179.045, EMA20=177.683, ATR14=0.680695; 직전 완료 봉 목표를 다음 봉 시가에 모의 적용 |
| v2 | opening_range_30m | 9995.74 | -4.26 | buy / partial / 뉴욕 09:30·09:45 두 완료 봉 최고가를 10:00 이후 종가가 돌파; 조건 충족; close=182.19, opening_high=181.96; 직전 완료 봉 목표를 다음 봉 시가에 모의 적용 |

### 같은 기간의 비용·노출 비교 (사후 연구)

| 전략 | 비용 전 | 비용 후 | 100% 보유 | 같은 평균 노출 보유 | 평균 노출 |
|---|---:|---:|---:|---:|---:|
| cash | 0.00% | 0.00% | 11.08% | 0.00% | 0.00% |
| buy_hold | 11.55% | 11.08% | 11.08% | 11.08% | 100.00% |
| trend_8_26 | 5.25% | 0.92% | 11.08% | 7.73% | 70.79% |
| momentum_26 | 4.36% | -0.77% | 11.08% | 7.50% | 68.68% |
| breakout_8 | 1.47% | -16.36% | 11.08% | 2.96% | 27.63% |
| reversion_12 | 1.72% | -7.65% | 11.08% | 2.25% | 21.05% |
| volume_26 | -0.06% | -7.73% | 11.08% | 0.61% | 5.79% |
| trend_8_26 AND momentum_26 | 2.71% | -2.34% | 11.08% | 6.61% | 60.79% |
| trend_8_26 + momentum_26 | 4.82% | 0.29% | 11.08% | 7.61% | 69.74% |
| trend_8_26 AND breakout_8 | 1.59% | -13.03% | 11.08% | 2.33% | 21.84% |
| trend_8_26 + breakout_8 | 3.37% | -7.53% | 11.08% | 5.32% | 49.22% |
| trend_8_26 AND reversion_12 | -1.19% | -6.84% | 11.08% | 1.06% | 10.00% |
| trend_8_26 + reversion_12 | 3.50% | -3.25% | 11.08% | 4.96% | 45.93% |
| trend_8_26 AND volume_26 | -0.73% | -6.00% | 11.08% | 0.42% | 3.95% |
| trend_8_26 + volume_26 | 2.58% | -3.29% | 11.08% | 4.12% | 38.29% |
| momentum_26 AND breakout_8 | 1.54% | -13.08% | 11.08% | 2.42% | 22.63% |
| momentum_26 + breakout_8 | 2.93% | -8.88% | 11.08% | 5.20% | 48.17% |
| momentum_26 AND reversion_12 | -0.06% | -6.95% | 11.08% | 1.03% | 9.74% |
| momentum_26 + reversion_12 | 3.06% | -3.66% | 11.08% | 4.84% | 44.87% |
| momentum_26 AND volume_26 | 0.50% | -3.64% | 11.08% | 0.28% | 2.63% |
| momentum_26 + volume_26 | 2.15% | -3.70% | 11.08% | 4.00% | 37.24% |
| breakout_8 AND reversion_12 | 0.00% | 0.00% | 11.08% | 0.00% | 0.00% |
| breakout_8 + reversion_12 | 1.61% | -11.74% | 11.08% | 2.60% | 24.35% |
| breakout_8 AND volume_26 | 0.76% | -1.75% | 11.08% | 0.17% | 1.58% |
| breakout_8 + volume_26 | 0.71% | -11.59% | 11.08% | 1.78% | 16.72% |
| reversion_12 AND volume_26 | -0.04% | -3.35% | 11.08% | 0.25% | 2.37% |
| reversion_12 + volume_26 | 0.84% | -6.91% | 11.08% | 1.43% | 13.43% |
| ema_12_26 | 4.19% | 0.74% | 11.08% | 8.21% | 75.00% |
| macd_12_26_9 | 2.79% | -3.49% | 11.08% | 4.65% | 43.16% |
| rsi_14_recovery | -0.08% | -1.33% | 11.08% | 0.08% | 0.79% |
| bollinger_20_reentry | -1.64% | -4.89% | 11.08% | 0.22% | 2.11% |
| donchian_20 | -0.09% | -8.91% | 11.08% | 1.14% | 10.79% |
| atr_14_breakout | 0.86% | -7.27% | 11.08% | 0.61% | 5.79% |
| session_vwap | 4.84% | -6.00% | 11.08% | 7.05% | 64.74% |
| obv_20 | 3.25% | -7.43% | 11.08% | 5.35% | 49.47% |
| stochastic_14_3_recovery | 0.05% | -9.54% | 11.08% | 0.67% | 6.32% |
| mfi_14_recovery | -0.31% | -1.97% | 11.08% | 0.11% | 1.05% |
| adx_14_trend | 4.28% | 1.26% | 11.08% | 4.36% | 40.53% |
| aroon_25_trend | -2.73% | -9.44% | 11.08% | 3.70% | 34.47% |
| cci_20_momentum | 2.22% | -7.97% | 11.08% | 3.21% | 30.00% |
| williams_14_recovery | -1.21% | -7.24% | 11.08% | 0.42% | 3.95% |
| cmf_20_accumulation | 4.23% | -2.95% | 11.08% | 5.41% | 50.00% |
| chaikin_3_10 | 5.03% | -4.24% | 11.08% | 6.58% | 60.53% |
| roc_10_momentum | 1.20% | -4.98% | 11.08% | 1.57% | 14.74% |
| trix_15_trend | 3.63% | -2.70% | 11.08% | 6.64% | 61.05% |
| keltner_20_breakout | 1.36% | -5.23% | 11.08% | 1.99% | 18.68% |
| opening_range_30m | 0.22% | -7.08% | 11.08% | 2.90% | 27.11% |

동일 구간·초기 자금, 종료 시 청산 비용 포함. 노출 맞춤은 사후 설명용이며 v2 실제 계좌 성과가 아닙니다.
[낙폭 분해·비용 영향·전체 구간](XOM/comparison.json)

[v1 전체 기록](XOM/accounts.json) · [v2 전체 기록](XOM/accounts-v2.json)

## JNJ 계좌

| 모델 | 전략 | 평가액 USD | 손익 USD | 최근 매매·이유 |
|---|---|---:|---:|---|
| v1 | cash | 10000.00 | 0.00 | 대기 /  / 새 신호 대기 |
| v1 | buy_hold | 10271.21 | 271.21 | buy /  / buy_hold: prior completed bar target 100%; next bar open simulation |
| v1 | trend_8_26 | 10203.47 | 203.47 | sell /  / trend_8_26: prior completed bar target 0%; next bar open simulation |
| v1 | momentum_26 | 9644.97 | -355.03 | sell /  / momentum_26: prior completed bar target 0%; next bar open simulation |
| v1 | breakout_8 | 9474.03 | -525.97 | sell /  / breakout_8: prior completed bar target 0%; next bar open simulation |
| v1 | reversion_12 | 9629.25 | -370.75 | sell /  / reversion_12: prior completed bar target 0%; next bar open simulation |
| v1 | volume_26 | 10040.58 | 40.58 | sell /  / volume_26: prior completed bar target 0%; next bar open simulation |
| v1 | trend_8_26 AND momentum_26 | 9811.53 | -188.47 | sell /  / trend_8_26 AND momentum_26: prior completed bar target 0%; next bar open simulation |
| v1 | trend_8_26 + momentum_26 | 9940.65 | -59.35 | sell /  / trend_8_26 + momentum_26: prior completed bar target 0%; next bar open simulation |
| v1 | trend_8_26 AND breakout_8 | 9864.21 | -135.79 | sell /  / trend_8_26 AND breakout_8: prior completed bar target 0%; next bar open simulation |
| v1 | trend_8_26 + breakout_8 | 9852.28 | -147.72 | sell /  / trend_8_26 + breakout_8: prior completed bar target 0%; next bar open simulation |
| v1 | trend_8_26 AND reversion_12 | 9807.21 | -192.79 | sell /  / trend_8_26 AND reversion_12: prior completed bar target 0%; next bar open simulation |
| v1 | trend_8_26 + reversion_12 | 9912.48 | -87.52 | sell /  / trend_8_26 + reversion_12: prior completed bar target 0%; next bar open simulation |
| v1 | trend_8_26 AND volume_26 | 10134.54 | 134.54 | sell /  / trend_8_26 AND volume_26: prior completed bar target 0%; next bar open simulation |
| v1 | trend_8_26 + volume_26 | 10122.01 | 122.01 | sell /  / trend_8_26 + volume_26: prior completed bar target 0%; next bar open simulation |
| v1 | momentum_26 AND breakout_8 | 9703.66 | -296.34 | sell /  / momentum_26 AND breakout_8: prior completed bar target 0%; next bar open simulation |
| v1 | momentum_26 + breakout_8 | 9559.48 | -440.52 | sell /  / momentum_26 + breakout_8: prior completed bar target 0%; next bar open simulation |
| v1 | momentum_26 AND reversion_12 | 9708.77 | -291.23 | sell /  / momentum_26 AND reversion_12: prior completed bar target 0%; next bar open simulation |
| v1 | momentum_26 + reversion_12 | 9675.68 | -324.32 | sell /  / momentum_26 + reversion_12: prior completed bar target 0%; next bar open simulation |
| v1 | momentum_26 AND volume_26 | 10000.00 | 0.00 | 대기 /  / 새 신호 대기 |
| v1 | momentum_26 + volume_26 | 9900.29 | -99.71 | sell /  / momentum_26 + volume_26: prior completed bar target 0%; next bar open simulation |
| v1 | breakout_8 AND reversion_12 | 10000.00 | 0.00 | 대기 /  / 새 신호 대기 |
| v1 | breakout_8 + reversion_12 | 9551.13 | -448.87 | sell /  / breakout_8 + reversion_12: prior completed bar target 0%; next bar open simulation |
| v1 | breakout_8 AND volume_26 | 10139.49 | 139.49 | sell /  / breakout_8 AND volume_26: prior completed bar target 0%; next bar open simulation |
| v1 | breakout_8 + volume_26 | 9772.62 | -227.38 | sell /  / breakout_8 + volume_26: prior completed bar target 0%; next bar open simulation |
| v1 | reversion_12 AND volume_26 | 9933.02 | -66.98 | sell /  / reversion_12 AND volume_26: prior completed bar target 0%; next bar open simulation |
| v1 | reversion_12 + volume_26 | 9852.61 | -147.39 | sell /  / reversion_12 + volume_26: prior completed bar target 0%; next bar open simulation |
| v1 | ema_12_26 | 9827.67 | -172.33 | sell /  / EMA12 > EMA26; 조건 미충족; EMA12=264.816, EMA26=264.953 |
| v1 | macd_12_26_9 | 10152.66 | 152.66 | sell /  / MACD > 신호선 그리고 MACD > 0; 조건 미충족; MACD=2.48372, signal9=2.49952 |
| v1 | rsi_14_recovery | 9923.04 | -76.96 | sell /  / 직전 RSI14 < 30, 현재 RSI14 >= 30 (한 봉 목표); 조건 미충족; RSI14=40.3665, previous_RSI14=36.2025 |
| v1 | bollinger_20_reentry | 9778.51 | -221.49 | sell /  / 직전 종가 < 직전 하단밴드, 현재 하단밴드 <= 종가 <= SMA20 (한 봉 목표); 조건 미충족; close=263.43, lower20=262.644, SMA20=266.981, previous_lower20=263.145 |
| v1 | donchian_20 | 9779.77 | -220.23 | sell /  / 종가 > 현재 봉을 제외한 직전 20봉 최고가; 조건 미충족; close=268.59, prior_high20=269.55 |
| v1 | atr_14_breakout | 9634.41 | -365.59 | sell /  / 종가 > 직전 종가 + 직전 ATR14 그리고 종가 > EMA26; 조건 미충족; close=269.05, threshold=269.858, prior_ATR14=0.907979, EMA26=264.623 |
| v1 | session_vwap | 9933.23 | -66.77 | sell /  / 종가 > 뉴욕 거래일별 누적 전형가격 VWAP; 조건 미충족; close=263.8, session_VWAP=264.478, session_volume=329302 |
| v1 | obv_20 | 9789.37 | -210.63 | sell /  / OBV > OBV의 SMA20 그리고 종가 > EMA26; 조건 미충족; OBV=2.01573e+07, OBV_SMA20=2.06236e+07, close=267.68, EMA26=266.081 |
| v1 | stochastic_14_3_recovery | 9436.30 | -563.70 | sell /  / 직전 %K14 < 20에서 %K14가 %D3 상향 돌파 (한 봉 목표); 조건 미충족; K14=12.1046, D3=12.4715, previous_K14=15.1307, previous_D3=13.9387 |
| v1 | mfi_14_recovery | 9931.49 | -68.51 | sell /  / 직전 MFI14 < 20, 현재 MFI14 >= 20 (한 봉 목표); 조건 미충족; MFI14=35.8262, previous_MFI14=31.0222 |
| v1 | adx_14_trend | 9672.00 | -328.00 | sell /  / Wilder ADX14 >= 25 그리고 +DI14 > -DI14; 조건 미충족; ADX14=53.7666, plus_DI14=23.1641, minus_DI14=36.2315 |
| v1 | aroon_25_trend | 9974.61 | -25.39 | sell /  / Aroon25 Up > 70 그리고 Down < 30 (동률이면 최신 극값); 조건 미충족; Aroon_up=76, Aroon_down=100 |
| v1 | cci_20_momentum | 10131.21 | 131.21 | sell /  / CCI20 > 100 (전형가격·평균절대편차); 조건 미충족; CCI20=91.7877 |
| v1 | williams_14_recovery | 9706.89 | -293.11 | sell /  / 직전 Williams %R14 < -80, 현재 >= -80 (한 봉 목표); 조건 미충족; Williams_R14=-66.5072, previous_R14=-71.4835 |
| v1 | cmf_20_accumulation | 10240.33 | 240.33 | sell /  / Chaikin Money Flow20 > 0.1; 조건 미충족; CMF20=-0.188785, volume20=4.96784e+06 |
| v1 | chaikin_3_10 | 10085.51 | 85.51 | sell /  / ADL의 EMA3 - EMA10 > 0 그리고 종가 > EMA26; 조건 미충족; Chaikin3_10=-220136, ADL=1.31662e+07, close=267.68, EMA26=266.081 |
| v1 | roc_10_momentum | 9834.72 | -165.28 | sell /  / 10봉 ROC > 1% 그리고 종가 > EMA26; 조건 미충족; ROC10_percent=0.555956, close=268.59, EMA26=264.916 |
| v1 | trix_15_trend | 9665.47 | -334.53 | sell /  / 15봉 삼중 EMA의 1봉 변화율 TRIX > 0 그리고 종가 > EMA26; 조건 미충족; TRIX15_percent=0.123572, close=263.8, EMA26=265.912 |
| v1 | keltner_20_breakout | 10029.96 | 29.96 | sell /  / 종가 > EMA20 + 2 x Wilder ATR14; 조건 미충족; close=267.68, upper_Keltner=268.805, EMA20=266.948, ATR14=0.92845 |
| v1 | opening_range_30m | 9973.31 | -26.69 | sell /  / 뉴욕 09:30·09:45 두 완료 봉 최고가를 10:00 이후 종가가 돌파; 자료 부족·변동폭 또는 거래량 없음: 대기; close=263.8 |
| v2 | cash | 10000.00 | 0.00 | 대기 /  / 새 신호 대기 |
| v2 | buy_hold | 10031.48 | 31.48 | 중단: 손실 한도 / buy / partial / 직전 완료 봉 목표 비중 100%; 다음 봉 시가 가정 |
| v2 | trend_8_26 | 10031.48 | 31.48 | 중단: 손실 한도 / buy / partial / 직전 완료 봉 목표 비중 100%; 다음 봉 시가 가정 |
| v2 | momentum_26 | 10031.48 | 31.48 | 중단: 손실 한도 / buy / partial / 직전 완료 봉 목표 비중 100%; 다음 봉 시가 가정 |
| v2 | breakout_8 | 9343.39 | -656.61 | 중단: 손실 한도 / sell / filled / 직전 완료 봉 목표 비중 0%; 다음 봉 시가 가정 |
| v2 | reversion_12 | 9317.82 | -682.18 | sell / filled / 직전 완료 봉 목표 비중 0%; 다음 봉 시가 가정 |
| v2 | volume_26 | 9819.31 | -180.69 | sell / filled / 직전 완료 봉 목표 비중 0%; 다음 봉 시가 가정 |
| v2 | trend_8_26 AND momentum_26 | 10031.48 | 31.48 | 중단: 손실 한도 / buy / partial / 직전 완료 봉 목표 비중 100%; 다음 봉 시가 가정 |
| v2 | trend_8_26 + momentum_26 | 10031.48 | 31.48 | 중단: 손실 한도 / buy / partial / 직전 완료 봉 목표 비중 100%; 다음 봉 시가 가정 |
| v2 | trend_8_26 AND breakout_8 | 9419.39 | -580.61 | 중단: 손실 한도 / sell / filled / 직전 완료 봉 목표 비중 0%; 다음 봉 시가 가정 |
| v2 | trend_8_26 + breakout_8 | 9409.59 | -590.41 | sell / filled / 직전 완료 봉 목표 비중 0%; 다음 봉 시가 가정 |
| v2 | trend_8_26 AND reversion_12 | 9775.94 | -224.06 | sell / filled / 직전 완료 봉 목표 비중 0%; 다음 봉 시가 가정 |
| v2 | trend_8_26 + reversion_12 | 9732.92 | -267.08 | 중단: 손실 한도 / sell / filled / 직전 완료 봉 목표 비중 0%; 다음 봉 시가 가정 |
| v2 | trend_8_26 AND volume_26 | 9997.51 | -2.49 | sell / filled / 직전 완료 봉 목표 비중 0%; 다음 봉 시가 가정 |
| v2 | trend_8_26 + volume_26 | 9992.41 | -7.59 | 중단: 손실 한도 / buy / filled / 직전 완료 봉 목표 비중 50%; 다음 봉 시가 가정 |
| v2 | momentum_26 AND breakout_8 | 9297.50 | -702.50 | sell / filled / 직전 완료 봉 목표 비중 0%; 다음 봉 시가 가정 |
| v2 | momentum_26 + breakout_8 | 9118.64 | -881.36 | sell / filled / 직전 완료 봉 목표 비중 0%; 다음 봉 시가 가정 |
| v2 | momentum_26 AND reversion_12 | 9637.84 | -362.16 | sell / filled / 직전 완료 봉 목표 비중 0%; 다음 봉 시가 가정 |
| v2 | momentum_26 + reversion_12 | 9732.92 | -267.08 | 중단: 손실 한도 / sell / filled / 직전 완료 봉 목표 비중 0%; 다음 봉 시가 가정 |
| v2 | momentum_26 AND volume_26 | 9920.93 | -79.07 | sell / filled / 직전 완료 봉 목표 비중 0%; 다음 봉 시가 가정 |
| v2 | momentum_26 + volume_26 | 9992.41 | -7.59 | 중단: 손실 한도 / buy / filled / 직전 완료 봉 목표 비중 50%; 다음 봉 시가 가정 |
| v2 | breakout_8 AND reversion_12 | 10000.00 | 0.00 | 대기 /  / 새 신호 대기 |
| v2 | breakout_8 + reversion_12 | 9128.10 | -871.90 | sell / filled / 직전 완료 봉 목표 비중 0%; 다음 봉 시가 가정 |
| v2 | breakout_8 AND volume_26 | 9949.08 | -50.92 | sell / filled / 직전 완료 봉 목표 비중 0%; 다음 봉 시가 가정 |
| v2 | breakout_8 + volume_26 | 9370.54 | -629.46 | sell / filled / 직전 완료 봉 목표 비중 0%; 다음 봉 시가 가정 |
| v2 | reversion_12 AND volume_26 | 9816.09 | -183.91 | sell / filled / 직전 완료 봉 목표 비중 0%; 다음 봉 시가 가정 |
| v2 | reversion_12 + volume_26 | 9605.91 | -394.09 | sell / filled / 직전 완료 봉 목표 비중 0%; 다음 봉 시가 가정 |
| v2 | ema_12_26 | 9819.81 | -180.19 | sell / filled / EMA12 > EMA26; 조건 미충족; EMA12=264.816, EMA26=264.953; 직전 완료 봉 목표를 다음 봉 시가에 모의 적용 |
| v2 | macd_12_26_9 | 10144.54 | 144.54 | sell / filled / MACD > 신호선 그리고 MACD > 0; 조건 미충족; MACD=2.48372, signal9=2.49952; 직전 완료 봉 목표를 다음 봉 시가에 모의 적용 |
| v2 | rsi_14_recovery | 9919.07 | -80.93 | sell / filled / 직전 RSI14 < 30, 현재 RSI14 >= 30 (한 봉 목표); 조건 미충족; RSI14=40.3665, previous_RSI14=36.2025; 직전 완료 봉 목표를 다음 봉 시가에 모의 적용 |
| v2 | bollinger_20_reentry | 9770.69 | -229.31 | sell / filled / 직전 종가 < 직전 하단밴드, 현재 하단밴드 <= 종가 <= SMA20 (한 봉 목표); 조건 미충족; close=263.43, lower20=262.644, SMA20=266.981, previous_lower20=263.145; 직전 완료 봉 목표를 다음 봉 시가에 모의 적용 |
| v2 | donchian_20 | 9764.13 | -235.87 | sell / filled / 종가 > 현재 봉을 제외한 직전 20봉 최고가; 조건 미충족; close=268.59, prior_high20=269.55; 직전 완료 봉 목표를 다음 봉 시가에 모의 적용 |
| v2 | atr_14_breakout | 9619.01 | -380.99 | sell / filled / 종가 > 직전 종가 + 직전 ATR14 그리고 종가 > EMA26; 조건 미충족; close=269.05, threshold=269.858, prior_ATR14=0.907979, EMA26=264.623; 직전 완료 봉 목표를 다음 봉 시가에 모의 적용 |
| v2 | session_vwap | 9913.38 | -86.62 | sell / filled / 종가 > 뉴욕 거래일별 누적 전형가격 VWAP; 조건 미충족; close=263.8, session_VWAP=264.478, session_volume=329302; 직전 완료 봉 목표를 다음 봉 시가에 모의 적용 |
| v2 | obv_20 | 9769.81 | -230.19 | sell / filled / OBV > OBV의 SMA20 그리고 종가 > EMA26; 조건 미충족; OBV=2.01573e+07, OBV_SMA20=2.06236e+07, close=267.68, EMA26=266.081; 직전 완료 봉 목표를 다음 봉 시가에 모의 적용 |
| v2 | stochastic_14_3_recovery | 9415.56 | -584.44 | sell / filled / 직전 %K14 < 20에서 %K14가 %D3 상향 돌파 (한 봉 목표); 조건 미충족; K14=12.1046, D3=12.4715, previous_K14=15.1307, previous_D3=13.9387; 직전 완료 봉 목표를 다음 봉 시가에 모의 적용 |
| v2 | mfi_14_recovery | 9925.53 | -74.47 | sell / filled / 직전 MFI14 < 20, 현재 MFI14 >= 20 (한 봉 목표); 조건 미충족; MFI14=35.8262, previous_MFI14=31.0222; 직전 완료 봉 목표를 다음 봉 시가에 모의 적용 |
| v2 | adx_14_trend | 9662.33 | -337.67 | sell / filled / Wilder ADX14 >= 25 그리고 +DI14 > -DI14; 조건 미충족; ADX14=53.7666, plus_DI14=23.1641, minus_DI14=36.2315; 직전 완료 봉 목표를 다음 봉 시가에 모의 적용 |
| v2 | aroon_25_trend | 9968.63 | -31.37 | sell / filled / Aroon25 Up > 70 그리고 Down < 30 (동률이면 최신 극값); 조건 미충족; Aroon_up=76, Aroon_down=100; 직전 완료 봉 목표를 다음 봉 시가에 모의 적용 |
| v2 | cci_20_momentum | 10121.08 | 121.08 | sell / filled / CCI20 > 100 (전형가격·평균절대편차); 조건 미충족; CCI20=91.7877; 직전 완료 봉 목표를 다음 봉 시가에 모의 적용 |
| v2 | williams_14_recovery | 9697.19 | -302.81 | sell / filled / 직전 Williams %R14 < -80, 현재 >= -80 (한 봉 목표); 조건 미충족; Williams_R14=-66.5072, previous_R14=-71.4835; 직전 완료 봉 목표를 다음 봉 시가에 모의 적용 |
| v2 | cmf_20_accumulation | 10234.18 | 234.18 | sell / filled / Chaikin Money Flow20 > 0.1; 조건 미충족; CMF20=-0.188785, volume20=4.96784e+06; 직전 완료 봉 목표를 다음 봉 시가에 모의 적용 |
| v2 | chaikin_3_10 | 10075.43 | 75.43 | sell / filled / ADL의 EMA3 - EMA10 > 0 그리고 종가 > EMA26; 조건 미충족; Chaikin3_10=-220136, ADL=1.31662e+07, close=267.68, EMA26=266.081; 직전 완료 봉 목표를 다음 봉 시가에 모의 적용 |
| v2 | roc_10_momentum | 9822.93 | -177.07 | sell / filled / 10봉 ROC > 1% 그리고 종가 > EMA26; 조건 미충족; ROC10_percent=0.555956, close=268.59, EMA26=264.916; 직전 완료 봉 목표를 다음 봉 시가에 모의 적용 |
| v2 | trix_15_trend | 9657.74 | -342.26 | sell / filled / 15봉 삼중 EMA의 1봉 변화율 TRIX > 0 그리고 종가 > EMA26; 조건 미충족; TRIX15_percent=0.123572, close=263.8, EMA26=265.912; 직전 완료 봉 목표를 다음 봉 시가에 모의 적용 |
| v2 | keltner_20_breakout | 10025.95 | 25.95 | sell / filled / 종가 > EMA20 + 2 x Wilder ATR14; 조건 미충족; close=267.68, upper_Keltner=268.805, EMA20=266.948, ATR14=0.92845; 직전 완료 봉 목표를 다음 봉 시가에 모의 적용 |
| v2 | opening_range_30m | 9971.31 | -28.69 | sell / filled / 뉴욕 09:30·09:45 두 완료 봉 최고가를 10:00 이후 종가가 돌파; 자료 부족·변동폭 또는 거래량 없음: 대기; close=263.8; 직전 완료 봉 목표를 다음 봉 시가에 모의 적용 |

### 같은 기간의 비용·노출 비교 (사후 연구)

| 전략 | 비용 전 | 비용 후 | 100% 보유 | 같은 평균 노출 보유 | 평균 노출 |
|---|---:|---:|---:|---:|---:|
| cash | 0.00% | 0.00% | 2.49% | 0.00% | 0.00% |
| buy_hold | 2.92% | 2.49% | 2.49% | 2.49% | 100.00% |
| trend_8_26 | 5.22% | 2.61% | 2.49% | 1.40% | 56.32% |
| momentum_26 | -0.46% | -4.56% | 2.49% | 1.34% | 53.95% |
| breakout_8 | 2.52% | -17.25% | 2.49% | 0.63% | 25.26% |
| reversion_12 | -4.44% | -11.77% | 2.49% | 0.58% | 23.42% |
| volume_26 | 2.79% | -3.49% | 2.49% | 0.14% | 5.79% |
| trend_8_26 AND momentum_26 | 1.18% | -1.75% | 2.49% | 1.19% | 47.89% |
| trend_8_26 + momentum_26 | 2.35% | -0.83% | 2.49% | 1.37% | 55.13% |
| trend_8_26 AND breakout_8 | 3.61% | -10.93% | 2.49% | 0.46% | 18.68% |
| trend_8_26 + breakout_8 | 3.90% | -7.63% | 2.49% | 1.01% | 40.80% |
| trend_8_26 AND reversion_12 | 0.52% | -3.21% | 2.49% | 0.16% | 6.58% |
| trend_8_26 + reversion_12 | 0.32% | -4.64% | 2.49% | 0.99% | 39.87% |
| trend_8_26 AND volume_26 | 3.25% | 0.26% | 2.49% | 0.05% | 2.11% |
| trend_8_26 + volume_26 | 4.04% | -0.26% | 2.49% | 0.77% | 31.06% |
| momentum_26 AND breakout_8 | 2.60% | -10.68% | 2.49% | 0.42% | 16.84% |
| momentum_26 + breakout_8 | 1.05% | -10.92% | 2.49% | 0.98% | 39.61% |
| momentum_26 AND reversion_12 | -1.40% | -5.46% | 2.49% | 0.18% | 7.37% |
| momentum_26 + reversion_12 | -2.44% | -7.64% | 2.49% | 0.96% | 38.69% |
| momentum_26 AND volume_26 | 0.14% | -0.70% | 2.49% | 0.01% | 0.53% |
| momentum_26 + volume_26 | 1.19% | -2.79% | 2.49% | 0.74% | 29.87% |
| breakout_8 AND reversion_12 | 0.00% | 0.00% | 2.49% | 0.00% | 0.00% |
| breakout_8 + reversion_12 | -1.00% | -14.20% | 2.49% | 0.60% | 24.35% |
| breakout_8 AND volume_26 | 1.33% | 0.06% | 2.49% | 0.03% | 1.05% |
| breakout_8 + volume_26 | 2.66% | -9.69% | 2.49% | 0.39% | 15.53% |
| reversion_12 AND volume_26 | -0.42% | -2.49% | 2.49% | 0.05% | 1.84% |
| reversion_12 + volume_26 | -0.87% | -7.13% | 2.49% | 0.36% | 14.61% |
| ema_12_26 | -0.07% | -2.97% | 2.49% | 1.38% | 55.53% |
| macd_12_26_9 | 9.10% | 5.49% | 2.49% | 0.87% | 35.00% |
| rsi_14_recovery | -0.94% | -4.21% | 2.49% | 0.05% | 2.11% |
| bollinger_20_reentry | -1.15% | -5.22% | 2.49% | 0.07% | 2.63% |
| donchian_20 | 2.07% | -7.72% | 2.49% | 0.25% | 10.00% |
| atr_14_breakout | 1.15% | -6.61% | 2.49% | 0.15% | 6.05% |
| session_vwap | 6.62% | -1.55% | 2.49% | 1.44% | 58.16% |
| obv_20 | -2.58% | -12.66% | 2.49% | 1.06% | 42.89% |
| stochastic_14_3_recovery | -0.87% | -11.13% | 2.49% | 0.17% | 6.84% |
| mfi_14_recovery | 0.80% | -1.30% | 2.49% | 0.03% | 1.32% |
| adx_14_trend | -3.32% | -8.45% | 2.49% | 1.07% | 43.16% |
| aroon_25_trend | 4.48% | 0.18% | 2.49% | 0.93% | 37.63% |
| cci_20_momentum | 4.61% | -2.19% | 2.49% | 0.62% | 25.00% |
| williams_14_recovery | -1.73% | -6.96% | 2.49% | 0.08% | 3.42% |
| cmf_20_accumulation | 6.29% | 1.49% | 2.49% | 1.05% | 42.37% |
| chaikin_3_10 | 0.06% | -5.26% | 2.49% | 1.14% | 45.79% |
| roc_10_momentum | -0.56% | -8.19% | 2.49% | 0.56% | 22.63% |
| trix_15_trend | -1.21% | -4.08% | 2.49% | 1.05% | 42.37% |
| keltner_20_breakout | 1.76% | -2.43% | 2.49% | 0.46% | 18.42% |
| opening_range_30m | 0.92% | -3.23% | 2.49% | 0.80% | 32.11% |

동일 구간·초기 자금, 종료 시 청산 비용 포함. 노출 맞춤은 사후 설명용이며 v2 실제 계좌 성과가 아닙니다.
[낙폭 분해·비용 영향·전체 구간](JNJ/comparison.json)

[v1 전체 기록](JNJ/accounts.json) · [v2 전체 기록](JNJ/accounts-v2.json)

## CAT 계좌

| 모델 | 전략 | 평가액 USD | 손익 USD | 최근 매매·이유 |
|---|---|---:|---:|---|
| v1 | cash | 10000.00 | 0.00 | 대기 /  / 새 신호 대기 |
| v1 | buy_hold | 9406.66 | -593.34 | buy /  / buy_hold: prior completed bar target 100%; next bar open simulation |
| v1 | trend_8_26 | 9570.52 | -429.48 | sell /  / trend_8_26: prior completed bar target 0%; next bar open simulation |
| v1 | momentum_26 | 9290.58 | -709.42 | sell /  / momentum_26: prior completed bar target 0%; next bar open simulation |
| v1 | breakout_8 | 9396.16 | -603.84 | sell /  / breakout_8: prior completed bar target 0%; next bar open simulation |
| v1 | reversion_12 | 9658.88 | -341.12 | sell /  / reversion_12: prior completed bar target 0%; next bar open simulation |
| v1 | volume_26 | 9611.34 | -388.66 | sell /  / volume_26: prior completed bar target 0%; next bar open simulation |
| v1 | trend_8_26 AND momentum_26 | 9471.21 | -528.79 | sell /  / trend_8_26 AND momentum_26: prior completed bar target 0%; next bar open simulation |
| v1 | trend_8_26 + momentum_26 | 9430.55 | -569.45 | sell /  / trend_8_26 + momentum_26: prior completed bar target 0%; next bar open simulation |
| v1 | trend_8_26 AND breakout_8 | 9747.92 | -252.08 | sell /  / trend_8_26 AND breakout_8: prior completed bar target 0%; next bar open simulation |
| v1 | trend_8_26 + breakout_8 | 9484.90 | -515.10 | sell /  / trend_8_26 + breakout_8: prior completed bar target 0%; next bar open simulation |
| v1 | trend_8_26 AND reversion_12 | 9919.62 | -80.38 | sell /  / trend_8_26 AND reversion_12: prior completed bar target 0%; next bar open simulation |
| v1 | trend_8_26 + reversion_12 | 9674.91 | -325.09 | sell /  / trend_8_26 + reversion_12: prior completed bar target 0%; next bar open simulation |
| v1 | trend_8_26 AND volume_26 | 9965.69 | -34.31 | sell /  / trend_8_26 AND volume_26: prior completed bar target 0%; next bar open simulation |
| v1 | trend_8_26 + volume_26 | 9631.20 | -368.80 | sell /  / trend_8_26 + volume_26: prior completed bar target 0%; next bar open simulation |
| v1 | momentum_26 AND breakout_8 | 9615.85 | -384.15 | sell /  / momentum_26 AND breakout_8: prior completed bar target 0%; next bar open simulation |
| v1 | momentum_26 + breakout_8 | 9344.21 | -655.79 | sell /  / momentum_26 + breakout_8: prior completed bar target 0%; next bar open simulation |
| v1 | momentum_26 AND reversion_12 | 9878.81 | -121.19 | sell /  / momentum_26 AND reversion_12: prior completed bar target 0%; next bar open simulation |
| v1 | momentum_26 + reversion_12 | 9493.43 | -506.57 | sell /  / momentum_26 + reversion_12: prior completed bar target 0%; next bar open simulation |
| v1 | momentum_26 AND volume_26 | 9894.55 | -105.45 | sell /  / momentum_26 AND volume_26: prior completed bar target 0%; next bar open simulation |
| v1 | momentum_26 + volume_26 | 9469.44 | -530.56 | sell /  / momentum_26 + volume_26: prior completed bar target 0%; next bar open simulation |
| v1 | breakout_8 AND reversion_12 | 10000.00 | 0.00 | 대기 /  / 새 신호 대기 |
| v1 | breakout_8 + reversion_12 | 9546.36 | -453.64 | sell /  / breakout_8 + reversion_12: prior completed bar target 0%; next bar open simulation |
| v1 | breakout_8 AND volume_26 | 9894.55 | -105.45 | sell /  / breakout_8 AND volume_26: prior completed bar target 0%; next bar open simulation |
| v1 | breakout_8 + volume_26 | 9503.34 | -496.66 | sell /  / breakout_8 + volume_26: prior completed bar target 0%; next bar open simulation |
| v1 | reversion_12 AND volume_26 | 9737.41 | -262.59 | sell /  / reversion_12 AND volume_26: prior completed bar target 0%; next bar open simulation |
| v1 | reversion_12 + volume_26 | 9635.55 | -364.45 | sell /  / reversion_12 + volume_26: prior completed bar target 0%; next bar open simulation |
| v1 | ema_12_26 | 9597.59 | -402.41 | sell /  / EMA12 > EMA26; 조건 미충족; EMA12=734.57, EMA26=734.673 |
| v1 | macd_12_26_9 | 9988.51 | -11.49 | sell /  / MACD > 신호선 그리고 MACD > 0; 조건 미충족; MACD=2.92675, signal9=3.02629 |
| v1 | rsi_14_recovery | 9866.63 | -133.37 | sell /  / 직전 RSI14 < 30, 현재 RSI14 >= 30 (한 봉 목표); 조건 미충족; RSI14=34.2237, previous_RSI14=36.7431 |
| v1 | bollinger_20_reentry | 9611.32 | -388.68 | sell /  / 직전 종가 < 직전 하단밴드, 현재 하단밴드 <= 종가 <= SMA20 (한 봉 목표); 조건 미충족; close=688.16, lower20=683.118, SMA20=697.519, previous_lower20=684.291 |
| v1 | donchian_20 | 9943.28 | -56.72 | sell /  / 종가 > 현재 봉을 제외한 직전 20봉 최고가; 조건 미충족; close=735.35, prior_high20=745 |
| v1 | atr_14_breakout | 9768.31 | -231.69 | sell /  / 종가 > 직전 종가 + 직전 ATR14 그리고 종가 > EMA26; 조건 미충족; close=735.35, threshold=737.263, prior_ATR14=4.10289, EMA26=727.331 |
| v1 | session_vwap | 8986.70 | -1013.30 | sell /  / 종가 > 뉴욕 거래일별 누적 전형가격 VWAP; 조건 미충족; close=685.97, session_VWAP=687.049, session_volume=1.75061e+06 |
| v1 | obv_20 | 9541.23 | -458.77 | sell /  / OBV > OBV의 SMA20 그리고 종가 > EMA26; 조건 미충족; OBV=-5.63582e+06, OBV_SMA20=-5.55612e+06, close=711.18, EMA26=734.673 |
| v1 | stochastic_14_3_recovery | 9787.27 | -212.73 | sell /  / 직전 %K14 < 20에서 %K14가 %D3 상향 돌파 (한 봉 목표); 조건 미충족; K14=38.9983, D3=20.3743, previous_K14=12.2487, previous_D3=12.0951 |
| v1 | mfi_14_recovery | 9992.21 | -7.79 | sell /  / 직전 MFI14 < 20, 현재 MFI14 >= 20 (한 봉 목표); 조건 미충족; MFI14=41.7007, previous_MFI14=39.2559 |
| v1 | adx_14_trend | 9614.13 | -385.87 | sell /  / Wilder ADX14 >= 25 그리고 +DI14 > -DI14; 조건 미충족; ADX14=37.6898, plus_DI14=16.8278, minus_DI14=52.0976 |
| v1 | aroon_25_trend | 9979.61 | -20.39 | sell /  / Aroon25 Up > 70 그리고 Down < 30 (동률이면 최신 극값); 조건 미충족; Aroon_up=68, Aroon_down=20 |
| v1 | cci_20_momentum | 9862.85 | -137.15 | sell /  / CCI20 > 100 (전형가격·평균절대편차); 조건 미충족; CCI20=99.2123 |
| v1 | williams_14_recovery | 9822.79 | -177.21 | sell /  / 직전 Williams %R14 < -80, 현재 >= -80 (한 봉 목표); 조건 미충족; Williams_R14=-72.124, previous_R14=-61.0017 |
| v1 | cmf_20_accumulation | 9458.11 | -541.89 | sell /  / Chaikin Money Flow20 > 0.1; 조건 미충족; CMF20=0.0105743, volume20=1.36134e+06 |
| v1 | chaikin_3_10 | 9240.53 | -759.47 | sell /  / ADL의 EMA3 - EMA10 > 0 그리고 종가 > EMA26; 조건 미충족; Chaikin3_10=-27551.7, ADL=-5.27692e+06, close=711.18, EMA26=734.673 |
| v1 | roc_10_momentum | 9896.73 | -103.27 | sell /  / 10봉 ROC > 1% 그리고 종가 > EMA26; 조건 미충족; ROC10_percent=0.883016, close=741.47, EMA26=734.681 |
| v1 | trix_15_trend | 9340.52 | -659.48 | sell /  / 15봉 삼중 EMA의 1봉 변화율 TRIX > 0 그리고 종가 > EMA26; 조건 미충족; TRIX15_percent=0.0460682, close=711.18, EMA26=734.673 |
| v1 | keltner_20_breakout | 10000.00 | 0.00 | 대기 /  / 새 신호 대기 |
| v1 | opening_range_30m | 10162.22 | 162.22 | sell /  / 뉴욕 09:30·09:45 두 완료 봉 최고가를 10:00 이후 종가가 돌파; 자료 부족·변동폭 또는 거래량 없음: 대기; close=733.16 |
| v2 | cash | 10000.00 | 0.00 | 대기 /  / 새 신호 대기 |
| v2 | buy_hold | 8651.07 | -1348.93 | 중단: 손실 한도 / buy / partial / 직전 완료 봉 목표 비중 100%; 다음 봉 시가 가정 |
| v2 | trend_8_26 | 9256.87 | -743.13 | 중단: 손실 한도 / buy / partial / 직전 완료 봉 목표 비중 100%; 다음 봉 시가 가정 |
| v2 | momentum_26 | 9062.04 | -937.96 | 중단: 손실 한도 / buy / partial / 직전 완료 봉 목표 비중 100%; 다음 봉 시가 가정 |
| v2 | breakout_8 | 9207.74 | -792.26 | sell / filled / 직전 완료 봉 목표 비중 0%; 다음 봉 시가 가정 |
| v2 | reversion_12 | 8530.25 | -1469.75 | 중단: 손실 한도 / buy / partial / 직전 완료 봉 목표 비중 100%; 다음 봉 시가 가정 |
| v2 | volume_26 | 8774.21 | -1225.79 | 중단: 손실 한도 / buy / partial / 직전 완료 봉 목표 비중 100%; 다음 봉 시가 가정 |
| v2 | trend_8_26 AND momentum_26 | 9270.53 | -729.47 | 중단: 손실 한도 / buy / partial / 직전 완료 봉 목표 비중 100%; 다음 봉 시가 가정 |
| v2 | trend_8_26 + momentum_26 | 9159.93 | -840.07 | 중단: 손실 한도 / buy / partial / 직전 완료 봉 목표 비중 100%; 다음 봉 시가 가정 |
| v2 | trend_8_26 AND breakout_8 | 9655.84 | -344.16 | sell / filled / 직전 완료 봉 목표 비중 0%; 다음 봉 시가 가정 |
| v2 | trend_8_26 + breakout_8 | 9350.40 | -649.60 | sell / filled / 직전 완료 봉 목표 비중 0%; 다음 봉 시가 가정 |
| v2 | trend_8_26 AND reversion_12 | 9728.39 | -271.61 | sell / filled / 직전 완료 봉 목표 비중 0%; 다음 봉 시가 가정 |
| v2 | trend_8_26 + reversion_12 | 9309.67 | -690.33 | 중단: 손실 한도 / sell / filled / 직전 완료 봉 목표 비중 0%; 다음 봉 시가 가정 |
| v2 | trend_8_26 AND volume_26 | 9999.01 | -0.99 | sell / filled / 직전 완료 봉 목표 비중 0%; 다음 봉 시가 가정 |
| v2 | trend_8_26 + volume_26 | 9303.04 | -696.96 | 중단: 손실 한도 / sell / filled / 직전 완료 봉 목표 비중 0%; 다음 봉 시가 가정 |
| v2 | momentum_26 AND breakout_8 | 9576.90 | -423.10 | sell / filled / 직전 완료 봉 목표 비중 0%; 다음 봉 시가 가정 |
| v2 | momentum_26 + breakout_8 | 9250.48 | -749.52 | sell / filled / 직전 완료 봉 목표 비중 0%; 다음 봉 시가 가정 |
| v2 | momentum_26 AND reversion_12 | 9745.30 | -254.70 | sell / filled / 직전 완료 봉 목표 비중 0%; 다음 봉 시가 가정 |
| v2 | momentum_26 + reversion_12 | 9171.71 | -828.29 | 중단: 손실 한도 / sell / filled / 직전 완료 봉 목표 비중 0%; 다음 봉 시가 가정 |
| v2 | momentum_26 AND volume_26 | 9936.85 | -63.15 | sell / filled / 직전 완료 봉 목표 비중 0%; 다음 봉 시가 가정 |
| v2 | momentum_26 + volume_26 | 9203.76 | -796.24 | 중단: 손실 한도 / sell / filled / 직전 완료 봉 목표 비중 0%; 다음 봉 시가 가정 |
| v2 | breakout_8 AND reversion_12 | 10000.00 | 0.00 | 대기 /  / 새 신호 대기 |
| v2 | breakout_8 + reversion_12 | 9610.18 | -389.82 | 중단: 손실 한도 / sell / filled / 직전 완료 봉 목표 비중 0%; 다음 봉 시가 가정 |
| v2 | breakout_8 AND volume_26 | 9887.31 | -112.69 | sell / filled / 직전 완료 봉 목표 비중 0%; 다음 봉 시가 가정 |
| v2 | breakout_8 + volume_26 | 9107.70 | -892.30 | sell / filled / 직전 완료 봉 목표 비중 0%; 다음 봉 시가 가정 |
| v2 | reversion_12 AND volume_26 | 8713.51 | -1286.49 | 중단: 손실 한도 / buy / partial / 직전 완료 봉 목표 비중 100%; 다음 봉 시가 가정 |
| v2 | reversion_12 + volume_26 | 9124.98 | -875.02 | 중단: 손실 한도 / sell / filled / 직전 완료 봉 목표 비중 50%; 다음 봉 시가 가정 |
| v2 | ema_12_26 | 9357.21 | -642.79 | 중단: 손실 한도 / buy / partial / EMA12 > EMA26; 조건 충족; EMA12=726.261, EMA26=726.172; 직전 완료 봉 목표를 다음 봉 시가에 모의 적용 |
| v2 | macd_12_26_9 | 9984.52 | -15.48 | sell / filled / MACD > 신호선 그리고 MACD > 0; 조건 미충족; MACD=2.92675, signal9=3.02629; 직전 완료 봉 목표를 다음 봉 시가에 모의 적용 |
| v2 | rsi_14_recovery | 9858.74 | -141.26 | sell / filled / 직전 RSI14 < 30, 현재 RSI14 >= 30 (한 봉 목표); 조건 미충족; RSI14=34.2237, previous_RSI14=36.7431; 직전 완료 봉 목표를 다음 봉 시가에 모의 적용 |
| v2 | bollinger_20_reentry | 9601.72 | -398.28 | sell / filled / 직전 종가 < 직전 하단밴드, 현재 하단밴드 <= 종가 <= SMA20 (한 봉 목표); 조건 미충족; close=688.16, lower20=683.118, SMA20=697.519, previous_lower20=684.291; 직전 완료 봉 목표를 다음 봉 시가에 모의 적용 |
| v2 | donchian_20 | 9939.30 | -60.70 | sell / filled / 종가 > 현재 봉을 제외한 직전 20봉 최고가; 조건 미충족; close=735.35, prior_high20=745; 직전 완료 봉 목표를 다음 봉 시가에 모의 적용 |
| v2 | atr_14_breakout | 9758.55 | -241.45 | sell / filled / 종가 > 직전 종가 + 직전 ATR14 그리고 종가 > EMA26; 조건 미충족; close=735.35, threshold=737.263, prior_ATR14=4.10289, EMA26=727.331; 직전 완료 봉 목표를 다음 봉 시가에 모의 적용 |
| v2 | session_vwap | 9010.60 | -989.40 | 중단: 손실 한도 / buy / partial / 종가 > 뉴욕 거래일별 누적 전형가격 VWAP; 조건 충족; close=734.98, session_VWAP=734.093, session_volume=764353; 직전 완료 봉 목표를 다음 봉 시가에 모의 적용 |
| v2 | obv_20 | 9294.83 | -705.17 | 중단: 손실 한도 / buy / partial / OBV > OBV의 SMA20 그리고 종가 > EMA26; 조건 충족; OBV=-5.0567e+06, OBV_SMA20=-6.30537e+06, close=733.16, EMA26=726.69; 직전 완료 봉 목표를 다음 봉 시가에 모의 적용 |
| v2 | stochastic_14_3_recovery | 9767.72 | -232.28 | sell / filled / 직전 %K14 < 20에서 %K14가 %D3 상향 돌파 (한 봉 목표); 조건 미충족; K14=38.9983, D3=20.3743, previous_K14=12.2487, previous_D3=12.0951; 직전 완료 봉 목표를 다음 봉 시가에 모의 적용 |
| v2 | mfi_14_recovery | 9986.21 | -13.79 | sell / filled / 직전 MFI14 < 20, 현재 MFI14 >= 20 (한 봉 목표); 조건 미충족; MFI14=41.7007, previous_MFI14=39.2559; 직전 완료 봉 목표를 다음 봉 시가에 모의 적용 |
| v2 | adx_14_trend | 9375.21 | -624.79 | 중단: 손실 한도 / buy / partial / Wilder ADX14 >= 25 그리고 +DI14 > -DI14; 조건 충족; ADX14=25.4031, plus_DI14=35.2628, minus_DI14=13.9603; 직전 완료 봉 목표를 다음 봉 시가에 모의 적용 |
| v2 | aroon_25_trend | 9973.62 | -26.38 | sell / filled / Aroon25 Up > 70 그리고 Down < 30 (동률이면 최신 극값); 조건 미충족; Aroon_up=68, Aroon_down=20; 직전 완료 봉 목표를 다음 봉 시가에 모의 적용 |
| v2 | cci_20_momentum | 9854.97 | -145.03 | sell / filled / CCI20 > 100 (전형가격·평균절대편차); 조건 미충족; CCI20=99.2123; 직전 완료 봉 목표를 다음 봉 시가에 모의 적용 |
| v2 | williams_14_recovery | 9809.05 | -190.95 | sell / filled / 직전 Williams %R14 < -80, 현재 >= -80 (한 봉 목표); 조건 미충족; Williams_R14=-72.124, previous_R14=-61.0017; 직전 완료 봉 목표를 다음 봉 시가에 모의 적용 |
| v2 | cmf_20_accumulation | 9215.69 | -784.31 | 중단: 손실 한도 / buy / partial / Chaikin Money Flow20 > 0.1; 조건 충족; CMF20=0.145111, volume20=965726; 직전 완료 봉 목표를 다음 봉 시가에 모의 적용 |
| v2 | chaikin_3_10 | 9110.84 | -889.16 | 중단: 손실 한도 / buy / partial / ADL의 EMA3 - EMA10 > 0 그리고 종가 > EMA26; 조건 충족; Chaikin3_10=293683, ADL=-4.91156e+06, close=739.58, EMA26=736.187; 직전 완료 봉 목표를 다음 봉 시가에 모의 적용 |
| v2 | roc_10_momentum | 9888.81 | -111.19 | sell / filled / 10봉 ROC > 1% 그리고 종가 > EMA26; 조건 미충족; ROC10_percent=0.883016, close=741.47, EMA26=734.681; 직전 완료 봉 목표를 다음 봉 시가에 모의 적용 |
| v2 | trix_15_trend | 9120.02 | -879.98 | 중단: 손실 한도 / buy / partial / 15봉 삼중 EMA의 1봉 변화율 TRIX > 0 그리고 종가 > EMA26; 조건 충족; TRIX15_percent=0.0196284, close=739.58, EMA26=736.187; 직전 완료 봉 목표를 다음 봉 시가에 모의 적용 |
| v2 | keltner_20_breakout | 10000.00 | 0.00 | 대기 /  / 새 신호 대기 |
| v2 | opening_range_30m | 10158.15 | 158.15 | sell / filled / 뉴욕 09:30·09:45 두 완료 봉 최고가를 10:00 이후 종가가 돌파; 자료 부족·변동폭 또는 거래량 없음: 대기; close=733.16; 직전 완료 봉 목표를 다음 봉 시가에 모의 적용 |

### 같은 기간의 비용·노출 비교 (사후 연구)

| 전략 | 비용 전 | 비용 후 | 100% 보유 | 같은 평균 노출 보유 | 평균 노출 |
|---|---:|---:|---:|---:|---:|
| cash | 0.00% | 0.00% | -18.73% | -0.00% | 0.00% |
| buy_hold | -18.39% | -18.73% | -18.73% | -18.73% | 100.00% |
| trend_8_26 | -4.99% | -8.52% | -18.73% | -8.04% | 40.53% |
| momentum_26 | -8.41% | -12.55% | -18.73% | -7.64% | 38.42% |
| breakout_8 | -1.43% | -13.46% | -18.73% | -3.10% | 15.26% |
| reversion_12 | -4.26% | -17.35% | -18.73% | -5.70% | 28.42% |
| volume_26 | -2.81% | -11.38% | -18.73% | -1.83% | 8.95% |
| trend_8_26 AND momentum_26 | -4.42% | -7.58% | -18.73% | -6.67% | 33.42% |
| trend_8_26 + momentum_26 | -6.70% | -10.54% | -18.73% | -7.84% | 39.48% |
| trend_8_26 AND breakout_8 | 0.84% | -5.31% | -18.73% | -1.67% | 8.16% |
| trend_8_26 + breakout_8 | -3.19% | -10.81% | -18.73% | -5.60% | 27.90% |
| trend_8_26 AND reversion_12 | 0.96% | -5.20% | -18.73% | -1.13% | 5.53% |
| trend_8_26 + reversion_12 | -4.55% | -12.09% | -18.73% | -6.88% | 34.48% |
| trend_8_26 AND volume_26 | 2.90% | 1.18% | -18.73% | -0.33% | 1.58% |
| trend_8_26 + volume_26 | -3.85% | -9.36% | -18.73% | -4.98% | 24.74% |
| momentum_26 AND breakout_8 | 0.09% | -6.80% | -18.73% | -1.72% | 8.42% |
| momentum_26 + breakout_8 | -4.95% | -12.98% | -18.73% | -5.40% | 26.85% |
| momentum_26 AND reversion_12 | -2.85% | -8.78% | -18.73% | -1.29% | 6.32% |
| momentum_26 + reversion_12 | -6.31% | -14.78% | -18.73% | -6.68% | 33.43% |
| momentum_26 AND volume_26 | 2.69% | 0.55% | -18.73% | -0.33% | 1.58% |
| momentum_26 + volume_26 | -5.60% | -11.39% | -18.73% | -4.78% | 23.69% |
| breakout_8 AND reversion_12 | 0.00% | 0.00% | -18.73% | -0.00% | 0.00% |
| breakout_8 + reversion_12 | -2.79% | -14.51% | -18.73% | -4.41% | 21.85% |
| breakout_8 AND volume_26 | 0.55% | -1.13% | -18.73% | -0.22% | 1.05% |
| breakout_8 + volume_26 | -2.09% | -11.86% | -18.73% | -2.47% | 12.11% |
| reversion_12 AND volume_26 | -2.14% | -7.73% | -18.73% | -1.19% | 5.79% |
| reversion_12 + volume_26 | -3.49% | -14.04% | -18.73% | -3.79% | 18.69% |
| ema_12_26 | -5.24% | -6.82% | -18.73% | -7.28% | 36.58% |
| macd_12_26_9 | 0.73% | -1.36% | -18.73% | -4.31% | 21.32% |
| rsi_14_recovery | -0.08% | -6.58% | -18.73% | -0.86% | 4.21% |
| bollinger_20_reentry | -0.84% | -6.50% | -18.73% | -0.76% | 3.68% |
| donchian_20 | 1.25% | -1.69% | -18.73% | -0.65% | 3.16% |
| atr_14_breakout | 1.29% | -2.88% | -18.73% | -0.60% | 2.89% |
| session_vwap | -3.60% | -14.65% | -18.73% | -9.04% | 45.79% |
| obv_20 | -4.43% | -12.50% | -18.73% | -4.25% | 21.05% |
| stochastic_14_3_recovery | -0.19% | -11.26% | -18.73% | -1.51% | 7.37% |
| mfi_14_recovery | 1.79% | -1.16% | -18.73% | -0.38% | 1.84% |
| adx_14_trend | -6.21% | -8.54% | -18.73% | -1.62% | 7.89% |
| aroon_25_trend | 1.10% | -1.83% | -18.73% | -1.67% | 8.16% |
| cci_20_momentum | -1.74% | -6.17% | -18.73% | -2.63% | 12.89% |
| williams_14_recovery | -0.24% | -8.28% | -18.73% | -1.08% | 5.26% |
| cmf_20_accumulation | -5.05% | -11.59% | -18.73% | -3.52% | 17.37% |
| chaikin_3_10 | -6.55% | -14.44% | -18.73% | -5.50% | 27.37% |
| roc_10_momentum | -0.09% | -5.40% | -18.73% | -1.94% | 9.47% |
| trix_15_trend | -6.37% | -10.22% | -18.73% | -5.70% | 28.42% |
| keltner_20_breakout | 0.38% | -0.46% | -18.73% | -0.27% | 1.32% |
| opening_range_30m | 3.63% | -0.21% | -18.73% | -4.36% | 21.58% |

동일 구간·초기 자금, 종료 시 청산 비용 포함. 노출 맞춤은 사후 설명용이며 v2 실제 계좌 성과가 아닙니다.
[낙폭 분해·비용 영향·전체 구간](CAT/comparison.json)

[v1 전체 기록](CAT/accounts.json) · [v2 전체 기록](CAT/accounts-v2.json)

## WMT 계좌

| 모델 | 전략 | 평가액 USD | 손익 USD | 최근 매매·이유 |
|---|---|---:|---:|---|
| v1 | cash | 10000.00 | 0.00 | 대기 /  / 새 신호 대기 |
| v1 | buy_hold | 10135.04 | 135.04 | buy /  / buy_hold: prior completed bar target 100%; next bar open simulation |
| v1 | trend_8_26 | 9779.58 | -220.42 | sell /  / trend_8_26: prior completed bar target 0%; next bar open simulation |
| v1 | momentum_26 | 9910.26 | -89.74 | buy /  / momentum_26: prior completed bar target 100%; next bar open simulation |
| v1 | breakout_8 | 9342.19 | -657.81 | sell /  / breakout_8: prior completed bar target 0%; next bar open simulation |
| v1 | reversion_12 | 9517.26 | -482.74 | sell /  / reversion_12: prior completed bar target 0%; next bar open simulation |
| v1 | volume_26 | 9775.35 | -224.65 | sell /  / volume_26: prior completed bar target 0%; next bar open simulation |
| v1 | trend_8_26 AND momentum_26 | 9861.19 | -138.81 | sell /  / trend_8_26 AND momentum_26: prior completed bar target 0%; next bar open simulation |
| v1 | trend_8_26 + momentum_26 | 9844.73 | -155.27 | buy /  / trend_8_26 + momentum_26: prior completed bar target 50%; next bar open simulation |
| v1 | trend_8_26 AND breakout_8 | 9602.19 | -397.81 | sell /  / trend_8_26 AND breakout_8: prior completed bar target 0%; next bar open simulation |
| v1 | trend_8_26 + breakout_8 | 9577.78 | -422.22 | sell /  / trend_8_26 + breakout_8: prior completed bar target 0%; next bar open simulation |
| v1 | trend_8_26 AND reversion_12 | 9683.74 | -316.26 | sell /  / trend_8_26 AND reversion_12: prior completed bar target 0%; next bar open simulation |
| v1 | trend_8_26 + reversion_12 | 9686.31 | -313.69 | sell /  / trend_8_26 + reversion_12: prior completed bar target 0%; next bar open simulation |
| v1 | trend_8_26 AND volume_26 | 9837.96 | -162.04 | sell /  / trend_8_26 AND volume_26: prior completed bar target 0%; next bar open simulation |
| v1 | trend_8_26 + volume_26 | 9777.89 | -222.11 | sell /  / trend_8_26 + volume_26: prior completed bar target 0%; next bar open simulation |
| v1 | momentum_26 AND breakout_8 | 9514.44 | -485.56 | sell /  / momentum_26 AND breakout_8: prior completed bar target 0%; next bar open simulation |
| v1 | momentum_26 + breakout_8 | 9680.41 | -319.59 | buy /  / momentum_26 + breakout_8: prior completed bar target 50%; next bar open simulation |
| v1 | momentum_26 AND reversion_12 | 9877.29 | -122.71 | sell /  / momentum_26 AND reversion_12: prior completed bar target 0%; next bar open simulation |
| v1 | momentum_26 + reversion_12 | 9809.31 | -190.69 | buy /  / momentum_26 + reversion_12: prior completed bar target 50%; next bar open simulation |
| v1 | momentum_26 AND volume_26 | 9853.50 | -146.50 | sell /  / momentum_26 AND volume_26: prior completed bar target 0%; next bar open simulation |
| v1 | momentum_26 + volume_26 | 9882.40 | -117.60 | buy /  / momentum_26 + volume_26: prior completed bar target 50%; next bar open simulation |
| v1 | breakout_8 AND reversion_12 | 10000.00 | 0.00 | 대기 /  / 새 신호 대기 |
| v1 | breakout_8 + reversion_12 | 9466.92 | -533.08 | sell /  / breakout_8 + reversion_12: prior completed bar target 0%; next bar open simulation |
| v1 | breakout_8 AND volume_26 | 9797.95 | -202.05 | sell /  / breakout_8 AND volume_26: prior completed bar target 0%; next bar open simulation |
| v1 | breakout_8 + volume_26 | 9556.59 | -443.41 | sell /  / breakout_8 + volume_26: prior completed bar target 0%; next bar open simulation |
| v1 | reversion_12 AND volume_26 | 9911.53 | -88.47 | sell /  / reversion_12 AND volume_26: prior completed bar target 0%; next bar open simulation |
| v1 | reversion_12 + volume_26 | 9703.61 | -296.39 | sell /  / reversion_12 + volume_26: prior completed bar target 0%; next bar open simulation |
| v1 | ema_12_26 | 10014.50 | 14.50 | buy /  / EMA12 > EMA26; 조건 충족; EMA12=117.957, EMA26=117.935 |
| v1 | macd_12_26_9 | 10121.08 | 121.08 | sell /  / MACD > 신호선 그리고 MACD > 0; 조건 미충족; MACD=0.563738, signal9=0.568978 |
| v1 | rsi_14_recovery | 9973.19 | -26.81 | sell /  / 직전 RSI14 < 30, 현재 RSI14 >= 30 (한 봉 목표); 조건 미충족; RSI14=46.7246, previous_RSI14=43.1348 |
| v1 | bollinger_20_reentry | 9940.27 | -59.73 | sell /  / 직전 종가 < 직전 하단밴드, 현재 하단밴드 <= 종가 <= SMA20 (한 봉 목표); 조건 미충족; close=120.035, lower20=119.686, SMA20=120.446, previous_lower20=119.732 |
| v1 | donchian_20 | 9643.84 | -356.16 | sell /  / 종가 > 현재 봉을 제외한 직전 20봉 최고가; 조건 미충족; close=121.08, prior_high20=121.18 |
| v1 | atr_14_breakout | 9811.78 | -188.22 | sell /  / 종가 > 직전 종가 + 직전 ATR14 그리고 종가 > EMA26; 조건 미충족; close=120.03, threshold=120.128, prior_ATR14=0.443028, EMA26=118.335 |
| v1 | session_vwap | 9681.70 | -318.30 | sell /  / 종가 > 뉴욕 거래일별 누적 전형가격 VWAP; 조건 미충족; close=121.08, session_VWAP=121.52, session_volume=1.65503e+06 |
| v1 | obv_20 | 9913.72 | -86.28 | buy /  / OBV > OBV의 SMA20 그리고 종가 > EMA26; 조건 충족; OBV=2.01069e+07, OBV_SMA20=1.89444e+07, close=120.205, EMA26=120.099 |
| v1 | stochastic_14_3_recovery | 9430.26 | -569.74 | sell /  / 직전 %K14 < 20에서 %K14가 %D3 상향 돌파 (한 봉 목표); 조건 미충족; K14=19.0069, D3=12.557, previous_K14=16.4382, previous_D3=8.94508 |
| v1 | mfi_14_recovery | 9969.08 | -30.92 | sell /  / 직전 MFI14 < 20, 현재 MFI14 >= 20 (한 봉 목표); 조건 미충족; MFI14=57.3162, previous_MFI14=36.5877 |
| v1 | adx_14_trend | 10102.70 | 102.70 | buy /  / Wilder ADX14 >= 25 그리고 +DI14 > -DI14; 조건 충족; ADX14=32.9742, plus_DI14=41.4463, minus_DI14=15.2475 |
| v1 | aroon_25_trend | 9893.25 | -106.75 | sell /  / Aroon25 Up > 70 그리고 Down < 30 (동률이면 최신 극값); 조건 미충족; Aroon_up=80, Aroon_down=96 |
| v1 | cci_20_momentum | 9664.17 | -335.83 | sell /  / CCI20 > 100 (전형가격·평균절대편차); 조건 미충족; CCI20=-31.8509 |
| v1 | williams_14_recovery | 9696.42 | -303.58 | sell /  / 직전 Williams %R14 < -80, 현재 >= -80 (한 봉 목표); 조건 미충족; Williams_R14=-77.0548, previous_R14=-75.1713 |
| v1 | cmf_20_accumulation | 9737.44 | -262.56 | sell /  / Chaikin Money Flow20 > 0.1; 조건 미충족; CMF20=0.0930543, volume20=1.6661e+07 |
| v1 | chaikin_3_10 | 9709.84 | -290.16 | sell /  / ADL의 EMA3 - EMA10 > 0 그리고 종가 > EMA26; 조건 미충족; Chaikin3_10=76755.7, ADL=1.33628e+07, close=120.04, EMA26=120.151 |
| v1 | roc_10_momentum | 10091.95 | 91.95 | sell /  / 10봉 ROC > 1% 그리고 종가 > EMA26; 조건 미충족; ROC10_percent=0.710203, close=120.535, EMA26=119.283 |
| v1 | trix_15_trend | 9659.88 | -340.12 | buy /  / 15봉 삼중 EMA의 1봉 변화율 TRIX > 0 그리고 종가 > EMA26; 조건 충족; TRIX15_percent=0.0420898, close=120.205, EMA26=120.099 |
| v1 | keltner_20_breakout | 9879.35 | -120.65 | sell /  / 종가 > EMA20 + 2 x Wilder ATR14; 조건 미충족; close=121.08, upper_Keltner=121.15, EMA20=120.322, ATR14=0.414113 |
| v1 | opening_range_30m | 9860.78 | -139.22 | sell /  / 뉴욕 09:30·09:45 두 완료 봉 최고가를 10:00 이후 종가가 돌파; 자료 부족·변동폭 또는 거래량 없음: 대기; close=121.08 |
| v2 | cash | 10000.00 | 0.00 | 대기 /  / 새 신호 대기 |
| v2 | buy_hold | 10737.98 | 737.98 | buy / partial / 직전 완료 봉 목표 비중 100%; 다음 봉 시가 가정 |
| v2 | trend_8_26 | 10170.98 | 170.98 | sell / filled / 직전 완료 봉 목표 비중 0%; 다음 봉 시가 가정 |
| v2 | momentum_26 | 10312.80 | 312.80 | buy / partial / 직전 완료 봉 목표 비중 100%; 다음 봉 시가 가정 |
| v2 | breakout_8 | 9296.17 | -703.83 | 중단: 손실 한도 / sell / filled / 직전 완료 봉 목표 비중 0%; 다음 봉 시가 가정 |
| v2 | reversion_12 | 9408.47 | -591.53 | sell / filled / 직전 완료 봉 목표 비중 0%; 다음 봉 시가 가정 |
| v2 | volume_26 | 9727.78 | -272.22 | sell / filled / 직전 완료 봉 목표 비중 0%; 다음 봉 시가 가정 |
| v2 | trend_8_26 AND momentum_26 | 10255.85 | 255.85 | sell / filled / 직전 완료 봉 목표 비중 0%; 다음 봉 시가 가정 |
| v2 | trend_8_26 + momentum_26 | 10241.61 | 241.61 | buy / filled / 직전 완료 봉 목표 비중 50%; 다음 봉 시가 가정 |
| v2 | trend_8_26 AND breakout_8 | 9667.87 | -332.13 | sell / filled / 직전 완료 봉 목표 비중 0%; 다음 봉 시가 가정 |
| v2 | trend_8_26 + breakout_8 | 9736.05 | -263.95 | sell / filled / 직전 완료 봉 목표 비중 0%; 다음 봉 시가 가정 |
| v2 | trend_8_26 AND reversion_12 | 9487.14 | -512.86 | sell / filled / 직전 완료 봉 목표 비중 0%; 다음 봉 시가 가정 |
| v2 | trend_8_26 + reversion_12 | 9824.94 | -175.06 | sell / filled / 직전 완료 봉 목표 비중 0%; 다음 봉 시가 가정 |
| v2 | trend_8_26 AND volume_26 | 9784.10 | -215.90 | sell / filled / 직전 완료 봉 목표 비중 0%; 다음 봉 시가 가정 |
| v2 | trend_8_26 + volume_26 | 9948.73 | -51.27 | sell / filled / 직전 완료 봉 목표 비중 0%; 다음 봉 시가 가정 |
| v2 | momentum_26 AND breakout_8 | 9475.14 | -524.86 | 중단: 손실 한도 / sell / filled / 직전 완료 봉 목표 비중 0%; 다음 봉 시가 가정 |
| v2 | momentum_26 + breakout_8 | 9845.16 | -154.84 | buy / filled / 직전 완료 봉 목표 비중 50%; 다음 봉 시가 가정 |
| v2 | momentum_26 AND reversion_12 | 9700.42 | -299.58 | sell / filled / 직전 완료 봉 목표 비중 0%; 다음 봉 시가 가정 |
| v2 | momentum_26 + reversion_12 | 9997.50 | -2.50 | buy / filled / 직전 완료 봉 목표 비중 50%; 다음 봉 시가 가정 |
| v2 | momentum_26 AND volume_26 | 9760.78 | -239.22 | sell / filled / 직전 완료 봉 목표 비중 0%; 다음 봉 시가 가정 |
| v2 | momentum_26 + volume_26 | 10060.01 | 60.01 | buy / filled / 직전 완료 봉 목표 비중 50%; 다음 봉 시가 가정 |
| v2 | breakout_8 AND reversion_12 | 10000.00 | 0.00 | 대기 /  / 새 신호 대기 |
| v2 | breakout_8 + reversion_12 | 9403.63 | -596.37 | sell / filled / 직전 완료 봉 목표 비중 0%; 다음 봉 시가 가정 |
| v2 | breakout_8 AND volume_26 | 9741.39 | -258.61 | sell / filled / 직전 완료 봉 목표 비중 0%; 다음 봉 시가 가정 |
| v2 | breakout_8 + volume_26 | 9502.52 | -497.48 | sell / filled / 직전 완료 봉 목표 비중 0%; 다음 봉 시가 가정 |
| v2 | reversion_12 AND volume_26 | 9917.25 | -82.75 | sell / filled / 직전 완료 봉 목표 비중 0%; 다음 봉 시가 가정 |
| v2 | reversion_12 + volume_26 | 9627.24 | -372.76 | sell / filled / 직전 완료 봉 목표 비중 0%; 다음 봉 시가 가정 |
| v2 | ema_12_26 | 10009.49 | 9.49 | buy / partial / EMA12 > EMA26; 조건 충족; EMA12=117.957, EMA26=117.935; 직전 완료 봉 목표를 다음 봉 시가에 모의 적용 |
| v2 | macd_12_26_9 | 10115.01 | 115.01 | sell / filled / MACD > 신호선 그리고 MACD > 0; 조건 미충족; MACD=0.563738, signal9=0.568978; 직전 완료 봉 목표를 다음 봉 시가에 모의 적용 |
| v2 | rsi_14_recovery | 9971.19 | -28.81 | sell / filled / 직전 RSI14 < 30, 현재 RSI14 >= 30 (한 봉 목표); 조건 미충족; RSI14=46.7246, previous_RSI14=43.1348; 직전 완료 봉 목표를 다음 봉 시가에 모의 적용 |
| v2 | bollinger_20_reentry | 9930.34 | -69.66 | sell / filled / 직전 종가 < 직전 하단밴드, 현재 하단밴드 <= 종가 <= SMA20 (한 봉 목표); 조건 미충족; close=120.035, lower20=119.686, SMA20=120.446, previous_lower20=119.732; 직전 완료 봉 목표를 다음 봉 시가에 모의 적용 |
| v2 | donchian_20 | 9630.34 | -369.66 | sell / filled / 종가 > 현재 봉을 제외한 직전 20봉 최고가; 조건 미충족; close=121.08, prior_high20=121.18; 직전 완료 봉 목표를 다음 봉 시가에 모의 적용 |
| v2 | atr_14_breakout | 9801.98 | -198.02 | sell / filled / 종가 > 직전 종가 + 직전 ATR14 그리고 종가 > EMA26; 조건 미충족; close=120.03, threshold=120.128, prior_ATR14=0.443028, EMA26=118.335; 직전 완료 봉 목표를 다음 봉 시가에 모의 적용 |
| v2 | session_vwap | 9660.42 | -339.58 | sell / filled / 종가 > 뉴욕 거래일별 누적 전형가격 VWAP; 조건 미충족; close=121.08, session_VWAP=121.52, session_volume=1.65503e+06; 직전 완료 봉 목표를 다음 봉 시가에 모의 적용 |
| v2 | obv_20 | 9900.84 | -99.16 | buy / partial / OBV > OBV의 SMA20 그리고 종가 > EMA26; 조건 충족; OBV=2.01069e+07, OBV_SMA20=1.89444e+07, close=120.205, EMA26=120.099; 직전 완료 봉 목표를 다음 봉 시가에 모의 적용 |
| v2 | stochastic_14_3_recovery | 9834.23 | -165.77 | 중단: 손실 한도 / buy / partial / 직전 %K14 < 20에서 %K14가 %D3 상향 돌파 (한 봉 목표); 조건 충족; K14=25.6758, D3=22.4971, previous_K14=12.8379, previous_D3=25.8704; 직전 완료 봉 목표를 다음 봉 시가에 모의 적용 |
| v2 | mfi_14_recovery | 9961.11 | -38.89 | sell / filled / 직전 MFI14 < 20, 현재 MFI14 >= 20 (한 봉 목표); 조건 미충족; MFI14=57.3162, previous_MFI14=36.5877; 직전 완료 봉 목표를 다음 봉 시가에 모의 적용 |
| v2 | adx_14_trend | 10099.67 | 99.67 | buy / partial / Wilder ADX14 >= 25 그리고 +DI14 > -DI14; 조건 충족; ADX14=32.9742, plus_DI14=41.4463, minus_DI14=15.2475; 직전 완료 봉 목표를 다음 봉 시가에 모의 적용 |
| v2 | aroon_25_trend | 9885.34 | -114.66 | sell / filled / Aroon25 Up > 70 그리고 Down < 30 (동률이면 최신 극값); 조건 미충족; Aroon_up=80, Aroon_down=96; 직전 완료 봉 목표를 다음 봉 시가에 모의 적용 |
| v2 | cci_20_momentum | 9650.65 | -349.35 | sell / filled / CCI20 > 100 (전형가격·평균절대편차); 조건 미충족; CCI20=-31.8509; 직전 완료 봉 목표를 다음 봉 시가에 모의 적용 |
| v2 | williams_14_recovery | 9680.92 | -319.08 | sell / filled / 직전 Williams %R14 < -80, 현재 >= -80 (한 봉 목표); 조건 미충족; Williams_R14=-77.0548, previous_R14=-75.1713; 직전 완료 봉 목표를 다음 봉 시가에 모의 적용 |
| v2 | cmf_20_accumulation | 9723.82 | -276.18 | sell / filled / Chaikin Money Flow20 > 0.1; 조건 미충족; CMF20=0.0930543, volume20=1.6661e+07; 직전 완료 봉 목표를 다음 봉 시가에 모의 적용 |
| v2 | chaikin_3_10 | 9690.44 | -309.56 | sell / filled / ADL의 EMA3 - EMA10 > 0 그리고 종가 > EMA26; 조건 미충족; Chaikin3_10=76755.7, ADL=1.33628e+07, close=120.04, EMA26=120.151; 직전 완료 봉 목표를 다음 봉 시가에 모의 적용 |
| v2 | roc_10_momentum | 10089.93 | 89.93 | sell / filled / 10봉 ROC > 1% 그리고 종가 > EMA26; 조건 미충족; ROC10_percent=0.710203, close=120.535, EMA26=119.283; 직전 완료 봉 목표를 다음 봉 시가에 모의 적용 |
| v2 | trix_15_trend | 9645.40 | -354.60 | buy / partial / 15봉 삼중 EMA의 1봉 변화율 TRIX > 0 그리고 종가 > EMA26; 조건 충족; TRIX15_percent=0.0420898, close=120.205, EMA26=120.099; 직전 완료 봉 목표를 다음 봉 시가에 모의 적용 |
| v2 | keltner_20_breakout | 9871.45 | -128.55 | sell / filled / 종가 > EMA20 + 2 x Wilder ATR14; 조건 미충족; close=121.08, upper_Keltner=121.15, EMA20=120.322, ATR14=0.414113; 직전 완료 봉 목표를 다음 봉 시가에 모의 적용 |
| v2 | opening_range_30m | 9850.92 | -149.08 | sell / filled / 뉴욕 09:30·09:45 두 완료 봉 최고가를 10:00 이후 종가가 돌파; 자료 부족·변동폭 또는 거래량 없음: 대기; close=121.08; 직전 완료 봉 목표를 다음 봉 시가에 모의 적용 |

### 같은 기간의 비용·노출 비교 (사후 연구)

| 전략 | 비용 전 | 비용 후 | 100% 보유 | 같은 평균 노출 보유 | 평균 노출 |
|---|---:|---:|---:|---:|---:|
| cash | 0.00% | 0.00% | 14.78% | 0.00% | 0.00% |
| buy_hold | 15.27% | 14.78% | 14.78% | 14.78% | 100.00% |
| trend_8_26 | 10.14% | 6.50% | 14.78% | 10.64% | 73.68% |
| momentum_26 | 14.18% | 9.94% | 14.78% | 11.21% | 77.37% |
| breakout_8 | 6.41% | -12.28% | 14.78% | 3.94% | 28.42% |
| reversion_12 | 2.87% | -6.99% | 14.78% | 2.42% | 17.63% |
| volume_26 | 2.41% | -3.03% | 14.78% | 0.75% | 5.53% |
| trend_8_26 AND momentum_26 | 11.05% | 7.39% | 14.78% | 9.91% | 68.95% |
| trend_8_26 + momentum_26 | 12.14% | 8.21% | 14.78% | 10.92% | 75.53% |
| trend_8_26 AND breakout_8 | 6.87% | -8.51% | 14.78% | 3.31% | 23.95% |
| trend_8_26 + breakout_8 | 8.27% | -3.13% | 14.78% | 7.23% | 51.06% |
| trend_8_26 AND reversion_12 | -0.82% | -6.48% | 14.78% | 1.00% | 7.37% |
| trend_8_26 + reversion_12 | 6.49% | -0.04% | 14.78% | 6.43% | 45.66% |
| trend_8_26 AND volume_26 | 0.13% | -1.95% | 14.78% | 0.25% | 1.84% |
| trend_8_26 + volume_26 | 6.24% | 1.85% | 14.78% | 5.55% | 39.61% |
| momentum_26 AND breakout_8 | 6.71% | -10.17% | 14.78% | 3.65% | 26.32% |
| momentum_26 + breakout_8 | 10.24% | -1.16% | 14.78% | 7.50% | 52.90% |
| momentum_26 AND reversion_12 | 1.67% | -3.74% | 14.78% | 1.08% | 7.89% |
| momentum_26 + reversion_12 | 8.42% | 2.63% | 14.78% | 6.70% | 47.50% |
| momentum_26 AND volume_26 | 1.72% | -2.05% | 14.78% | 0.36% | 2.63% |
| momentum_26 + volume_26 | 8.18% | 3.70% | 14.78% | 5.82% | 41.45% |
| breakout_8 AND reversion_12 | 0.00% | 0.00% | 14.78% | 0.00% | 0.00% |
| breakout_8 + reversion_12 | 4.66% | -8.91% | 14.78% | 3.18% | 23.04% |
| breakout_8 AND volume_26 | 0.64% | -2.68% | 14.78% | 0.32% | 2.37% |
| breakout_8 + volume_26 | 4.42% | -7.57% | 14.78% | 2.33% | 16.98% |
| reversion_12 AND volume_26 | 0.22% | -1.44% | 14.78% | 0.18% | 1.32% |
| reversion_12 + volume_26 | 2.65% | -4.23% | 14.78% | 1.58% | 11.58% |
| ema_12_26 | 12.64% | 10.76% | 14.78% | 11.86% | 81.58% |
| macd_12_26_9 | 10.59% | 6.04% | 14.78% | 5.76% | 41.05% |
| rsi_14_recovery | 0.20% | -0.64% | 14.78% | 0.07% | 0.53% |
| bollinger_20_reentry | 1.82% | -0.72% | 14.78% | 0.21% | 1.58% |
| donchian_20 | 4.01% | -9.83% | 14.78% | 2.02% | 14.74% |
| atr_14_breakout | -0.01% | -9.97% | 14.78% | 1.04% | 7.63% |
| session_vwap | 11.63% | 0.93% | 14.78% | 8.76% | 61.32% |
| obv_20 | 12.16% | 3.99% | 14.78% | 9.12% | 63.68% |
| stochastic_14_3_recovery | -0.29% | -8.32% | 14.78% | 0.72% | 5.26% |
| mfi_14_recovery | 1.30% | -0.39% | 14.78% | 0.14% | 1.05% |
| adx_14_trend | 10.15% | 7.41% | 14.78% | 8.44% | 59.21% |
| aroon_25_trend | 8.13% | 2.81% | 14.78% | 4.77% | 34.21% |
| cci_20_momentum | 6.82% | -3.01% | 14.78% | 5.07% | 36.32% |
| williams_14_recovery | 0.94% | -6.02% | 14.78% | 0.61% | 4.47% |
| cmf_20_accumulation | 9.32% | 0.09% | 14.78% | 6.37% | 45.26% |
| chaikin_3_10 | 10.57% | 0.81% | 14.78% | 8.40% | 58.95% |
| roc_10_momentum | 1.03% | -3.94% | 14.78% | 2.35% | 17.11% |
| trix_15_trend | 11.08% | 6.07% | 14.78% | 10.36% | 71.84% |
| keltner_20_breakout | 7.26% | -0.55% | 14.78% | 4.28% | 30.79% |
| opening_range_30m | 11.01% | 4.67% | 14.78% | 6.03% | 42.89% |

동일 구간·초기 자금, 종료 시 청산 비용 포함. 노출 맞춤은 사후 설명용이며 v2 실제 계좌 성과가 아닙니다.
[낙폭 분해·비용 영향·전체 구간](WMT/comparison.json)

[v1 전체 기록](WMT/accounts.json) · [v2 전체 기록](WMT/accounts-v2.json)
