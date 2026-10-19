# 모의투자 운영 현황

[PC·서버 장애 진단과 복구 방법](https://github.com/BaekJaeYeol/paper-trading-program/blob/main/investment-lab/docs/failure-recovery.md)

이번 실행 복구: {}

완료 봉 확인 주기: 기록 3/18회 · 기록 없는 예정 15회 · 아직 판정 전 8회 · 주의: 예약 시작 지연 또는 실행·저장 누락을 확인하세요.

[주기 판정 기준](https://github.com/BaekJaeYeol/paper-trading-program/blob/main/investment-lab/docs/session-coverage.md)

최근 확인: 2026-10-19T18:22:00.448986+00:00 (UTC)
다음 15분 확인 목표 (세션 실행 중에만 적용): 2026-10-19T18:37:00+00:00 (UTC, 실행 지연 가능)

실제 주문 없음. v1 기존 계좌와 v2 새 계좌의 시작일이 다르므로 수익률을 직접 우열 비교하지 마세요.
v2는 다음 봉 시가에 비용·스프레드·직전 거래량 제한을 적용한 가상 체결입니다. 미체결 잔량은 만료됩니다.

| 종목 | 상태 | 최근 성공 UTC | 마지막 완료 봉 UTC | 이번 새 봉 |
|---|---|---|---|---|
| SPY | updated | 2026-10-19T18:22:00.448986+00:00 | 2026-10-19T18:00:00+00:00 | 1 |
| QQQ | updated | 2026-10-19T18:22:00.448986+00:00 | 2026-10-19T18:00:00+00:00 | 1 |
| IWM | updated | 2026-10-19T18:22:00.448986+00:00 | 2026-10-19T18:00:00+00:00 | 1 |
| DIA | updated | 2026-10-19T18:22:00.448986+00:00 | 2026-10-19T18:00:00+00:00 | 1 |
| MSFT | updated | 2026-10-19T18:22:00.448986+00:00 | 2026-10-19T18:00:00+00:00 | 1 |
| JPM | updated | 2026-10-19T18:22:00.448986+00:00 | 2026-10-19T18:00:00+00:00 | 1 |
| XOM | updated | 2026-10-19T18:22:00.448986+00:00 | 2026-10-19T18:00:00+00:00 | 1 |
| JNJ | updated | 2026-10-19T18:22:00.448986+00:00 | 2026-10-19T18:00:00+00:00 | 1 |
| CAT | updated | 2026-10-19T18:22:00.448986+00:00 | 2026-10-19T18:00:00+00:00 | 1 |
| WMT | updated | 2026-10-19T18:22:00.448986+00:00 | 2026-10-19T18:00:00+00:00 | 1 |

이번 실행 소요: 45.98초
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
| v1 | buy_hold | 9909.17 | -90.83 | buy /  / buy_hold: prior completed bar target 100%; next bar open simulation |
| v1 | trend_8_26 | 9887.48 | -112.52 | buy /  / trend_8_26: prior completed bar target 100%; next bar open simulation |
| v1 | momentum_26 | 9868.97 | -131.03 | buy /  / momentum_26: prior completed bar target 100%; next bar open simulation |
| v1 | breakout_8 | 9873.76 | -126.24 | sell /  / breakout_8: prior completed bar target 0%; next bar open simulation |
| v1 | reversion_12 | 9844.51 | -155.49 | sell /  / reversion_12: prior completed bar target 0%; next bar open simulation |
| v1 | volume_26 | 9790.14 | -209.86 | sell /  / volume_26: prior completed bar target 0%; next bar open simulation |
| v1 | trend_8_26 AND momentum_26 | 9868.97 | -131.03 | buy /  / trend_8_26 AND momentum_26: prior completed bar target 100%; next bar open simulation |
| v1 | trend_8_26 + momentum_26 | 9878.22 | -121.78 | buy /  / trend_8_26 + momentum_26: prior completed bar target 100%; next bar open simulation |
| v1 | trend_8_26 AND breakout_8 | 9970.32 | -29.68 | sell /  / trend_8_26 AND breakout_8: prior completed bar target 0%; next bar open simulation |
| v1 | trend_8_26 + breakout_8 | 9900.30 | -99.70 | sell /  / trend_8_26 + breakout_8: prior completed bar target 50%; next bar open simulation |
| v1 | trend_8_26 AND reversion_12 | 9908.20 | -91.80 | sell /  / trend_8_26 AND reversion_12: prior completed bar target 0%; next bar open simulation |
| v1 | trend_8_26 + reversion_12 | 9865.89 | -134.11 | sell /  / trend_8_26 + reversion_12: prior completed bar target 50%; next bar open simulation |
| v1 | trend_8_26 AND volume_26 | 9836.21 | -163.79 | sell /  / trend_8_26 AND volume_26: prior completed bar target 0%; next bar open simulation |
| v1 | trend_8_26 + volume_26 | 9838.63 | -161.37 | sell /  / trend_8_26 + volume_26: prior completed bar target 50%; next bar open simulation |
| v1 | momentum_26 AND breakout_8 | 9954.13 | -45.87 | sell /  / momentum_26 AND breakout_8: prior completed bar target 0%; next bar open simulation |
| v1 | momentum_26 + breakout_8 | 9871.33 | -128.67 | sell /  / momentum_26 + breakout_8: prior completed bar target 50%; next bar open simulation |
| v1 | momentum_26 AND reversion_12 | 9961.77 | -38.23 | sell /  / momentum_26 AND reversion_12: prior completed bar target 0%; next bar open simulation |
| v1 | momentum_26 + reversion_12 | 9876.38 | -123.62 | sell /  / momentum_26 + reversion_12: prior completed bar target 50%; next bar open simulation |
| v1 | momentum_26 AND volume_26 | 9849.91 | -150.09 | sell /  / momentum_26 AND volume_26: prior completed bar target 0%; next bar open simulation |
| v1 | momentum_26 + volume_26 | 9829.43 | -170.57 | sell /  / momentum_26 + volume_26: prior completed bar target 50%; next bar open simulation |
| v1 | breakout_8 AND reversion_12 | 10000.00 | 0.00 | 대기 /  / 새 신호 대기 |
| v1 | breakout_8 + reversion_12 | 9859.02 | -140.98 | sell /  / breakout_8 + reversion_12: prior completed bar target 0%; next bar open simulation |
| v1 | breakout_8 AND volume_26 | 9954.13 | -45.87 | sell /  / breakout_8 AND volume_26: prior completed bar target 0%; next bar open simulation |
| v1 | breakout_8 + volume_26 | 9831.79 | -168.21 | sell /  / breakout_8 + volume_26: prior completed bar target 0%; next bar open simulation |
| v1 | reversion_12 AND volume_26 | 9899.64 | -100.36 | sell /  / reversion_12 AND volume_26: prior completed bar target 0%; next bar open simulation |
| v1 | reversion_12 + volume_26 | 9817.21 | -182.79 | sell /  / reversion_12 + volume_26: prior completed bar target 0%; next bar open simulation |
| v1 | ema_12_26 | 9871.28 | -128.72 | buy /  / EMA12 > EMA26; 조건 충족; EMA12=766.605, EMA26=766.511 |
| v1 | macd_12_26_9 | 9859.93 | -140.07 | sell /  / MACD > 신호선 그리고 MACD > 0; 조건 미충족; MACD=0.314893, signal9=0.346476 |
| v1 | rsi_14_recovery | 9899.32 | -100.68 | sell /  / 직전 RSI14 < 30, 현재 RSI14 >= 30 (한 봉 목표); 조건 미충족; RSI14=34.3611, previous_RSI14=32.906 |
| v1 | bollinger_20_reentry | 9835.17 | -164.83 | sell /  / 직전 종가 < 직전 하단밴드, 현재 하단밴드 <= 종가 <= SMA20 (한 봉 목표); 조건 미충족; close=763.39, lower20=762.854, SMA20=768.639, previous_lower20=763.636 |
| v1 | donchian_20 | 9960.79 | -39.21 | sell /  / 종가 > 현재 봉을 제외한 직전 20봉 최고가; 조건 미충족; close=769.96, prior_high20=770.3 |
| v1 | atr_14_breakout | 9955.14 | -44.86 | sell /  / 종가 > 직전 종가 + 직전 ATR14 그리고 종가 > EMA26; 조건 미충족; close=766.58, threshold=768.736, prior_ATR14=1.82624, EMA26=765.727 |
| v1 | session_vwap | 9806.83 | -193.17 | sell /  / 종가 > 뉴욕 거래일별 누적 전형가격 VWAP; 조건 미충족; close=768.64, session_VWAP=768.839, session_volume=6.99147e+07 |
| v1 | obv_20 | 9909.51 | -90.49 | sell /  / OBV > OBV의 SMA20 그리고 종가 > EMA26; 조건 미충족; OBV=-1.1153e+07, OBV_SMA20=-7.86173e+06, close=768.275, EMA26=767.362 |
| v1 | stochastic_14_3_recovery | 9821.11 | -178.89 | buy /  / 직전 %K14 < 20에서 %K14가 %D3 상향 돌파 (한 봉 목표); 조건 충족; K14=23.6558, D3=22.5002, previous_K14=9.97019, previous_D3=26.4496 |
| v1 | mfi_14_recovery | 9955.14 | -44.86 | sell /  / 직전 MFI14 < 20, 현재 MFI14 >= 20 (한 봉 목표); 조건 미충족; MFI14=24.4041, previous_MFI14=24.1984 |
| v1 | adx_14_trend | 9981.96 | -18.04 | sell /  / Wilder ADX14 >= 25 그리고 +DI14 > -DI14; 조건 미충족; ADX14=24.2312, plus_DI14=28.3519, minus_DI14=24.6578 |
| v1 | aroon_25_trend | 9861.30 | -138.70 | sell /  / Aroon25 Up > 70 그리고 Down < 30 (동률이면 최신 극값); 조건 미충족; Aroon_up=68, Aroon_down=20 |
| v1 | cci_20_momentum | 9861.55 | -138.45 | sell /  / CCI20 > 100 (전형가격·평균절대편차); 조건 미충족; CCI20=98.503 |
| v1 | williams_14_recovery | 9793.04 | -206.96 | buy /  / 직전 Williams %R14 < -80, 현재 >= -80 (한 봉 목표); 조건 충족; Williams_R14=-76.3442, previous_R14=-90.0298 |
| v1 | cmf_20_accumulation | 9890.95 | -109.05 | sell /  / Chaikin Money Flow20 > 0.1; 조건 미충족; CMF20=0.0493062, volume20=8.08389e+07 |
| v1 | chaikin_3_10 | 9864.45 | -135.55 | sell /  / ADL의 EMA3 - EMA10 > 0 그리고 종가 > EMA26; 조건 미충족; Chaikin3_10=-974621, ADL=7.60516e+06, close=768.275, EMA26=767.362 |
| v1 | roc_10_momentum | 9953.42 | -46.58 | sell /  / 10봉 ROC > 1% 그리고 종가 > EMA26; 조건 미충족; ROC10_percent=0.806376, close=769.45, EMA26=767.181 |
| v1 | trix_15_trend | 9846.97 | -153.03 | buy /  / 15봉 삼중 EMA의 1봉 변화율 TRIX > 0 그리고 종가 > EMA26; 조건 충족; TRIX15_percent=0.00716671, close=767.62, EMA26=767.441 |
| v1 | keltner_20_breakout | 10000.00 | 0.00 | 대기 /  / 새 신호 대기 |
| v1 | opening_range_30m | 9846.77 | -153.23 | sell /  / 뉴욕 09:30·09:45 두 완료 봉 최고가를 10:00 이후 종가가 돌파; 조건 미충족; close=767.51, opening_high=768.06 |
| v2 | cash | 10000.00 | 0.00 | 대기 /  / 새 신호 대기 |
| v2 | buy_hold | 9837.70 | -162.30 | buy / partial / 직전 완료 봉 목표 비중 100%; 다음 봉 시가 가정 |
| v2 | trend_8_26 | 9770.35 | -229.65 | buy / partial / 직전 완료 봉 목표 비중 100%; 다음 봉 시가 가정 |
| v2 | momentum_26 | 9722.78 | -277.22 | buy / partial / 직전 완료 봉 목표 비중 100%; 다음 봉 시가 가정 |
| v2 | breakout_8 | 9471.75 | -528.25 | sell / filled / 직전 완료 봉 목표 비중 0%; 다음 봉 시가 가정 |
| v2 | reversion_12 | 9380.06 | -619.94 | sell / filled / 직전 완료 봉 목표 비중 0%; 다음 봉 시가 가정 |
| v2 | volume_26 | 9235.92 | -764.08 | sell / filled / 직전 완료 봉 목표 비중 0%; 다음 봉 시가 가정 |
| v2 | trend_8_26 AND momentum_26 | 9729.41 | -270.59 | buy / partial / 직전 완료 봉 목표 비중 100%; 다음 봉 시가 가정 |
| v2 | trend_8_26 + momentum_26 | 9746.54 | -253.46 | buy / partial / 직전 완료 봉 목표 비중 100%; 다음 봉 시가 가정 |
| v2 | trend_8_26 AND breakout_8 | 9794.09 | -205.91 | sell / filled / 직전 완료 봉 목표 비중 0%; 다음 봉 시가 가정 |
| v2 | trend_8_26 + breakout_8 | 9639.90 | -360.10 | sell / filled / 직전 완료 봉 목표 비중 50%; 다음 봉 시가 가정 |
| v2 | trend_8_26 AND reversion_12 | 9801.35 | -198.65 | sell / filled / 직전 완료 봉 목표 비중 0%; 다음 봉 시가 가정 |
| v2 | trend_8_26 + reversion_12 | 9572.82 | -427.18 | sell / filled / 직전 완료 봉 목표 비중 50%; 다음 봉 시가 가정 |
| v2 | trend_8_26 AND volume_26 | 9678.83 | -321.17 | sell / filled / 직전 완료 봉 목표 비중 0%; 다음 봉 시가 가정 |
| v2 | trend_8_26 + volume_26 | 9519.06 | -480.94 | sell / filled / 직전 완료 봉 목표 비중 50%; 다음 봉 시가 가정 |
| v2 | momentum_26 AND breakout_8 | 9736.71 | -263.29 | sell / filled / 직전 완료 봉 목표 비중 0%; 다음 봉 시가 가정 |
| v2 | momentum_26 + breakout_8 | 9596.33 | -403.67 | sell / filled / 직전 완료 봉 목표 비중 50%; 다음 봉 시가 가정 |
| v2 | momentum_26 AND reversion_12 | 9923.13 | -76.87 | sell / filled / 직전 완료 봉 목표 비중 0%; 다음 봉 시가 가정 |
| v2 | momentum_26 + reversion_12 | 9589.68 | -410.32 | sell / filled / 직전 완료 봉 목표 비중 50%; 다음 봉 시가 가정 |
| v2 | momentum_26 AND volume_26 | 9762.54 | -237.46 | sell / filled / 직전 완료 봉 목표 비중 0%; 다음 봉 시가 가정 |
| v2 | momentum_26 + volume_26 | 9535.81 | -464.19 | sell / filled / 직전 완료 봉 목표 비중 50%; 다음 봉 시가 가정 |
| v2 | breakout_8 AND reversion_12 | 10000.00 | 0.00 | 대기 /  / 새 신호 대기 |
| v2 | breakout_8 + reversion_12 | 9464.93 | -535.07 | sell / filled / 직전 완료 봉 목표 비중 0%; 다음 봉 시가 가정 |
| v2 | breakout_8 AND volume_26 | 9885.63 | -114.37 | sell / filled / 직전 완료 봉 목표 비중 0%; 다음 봉 시가 가정 |
| v2 | breakout_8 + volume_26 | 9392.04 | -607.96 | sell / filled / 직전 완료 봉 목표 비중 0%; 다음 봉 시가 가정 |
| v2 | reversion_12 AND volume_26 | 9641.69 | -358.31 | sell / filled / 직전 완료 봉 목표 비중 0%; 다음 봉 시가 가정 |
| v2 | reversion_12 + volume_26 | 9385.88 | -614.12 | sell / filled / 직전 완료 봉 목표 비중 0%; 다음 봉 시가 가정 |
| v2 | ema_12_26 | 9868.32 | -131.68 | buy / partial / EMA12 > EMA26; 조건 충족; EMA12=766.605, EMA26=766.511; 직전 완료 봉 목표를 다음 봉 시가에 모의 적용 |
| v2 | macd_12_26_9 | 9855.99 | -144.01 | sell / filled / MACD > 신호선 그리고 MACD > 0; 조건 미충족; MACD=0.314893, signal9=0.346476; 직전 완료 봉 목표를 다음 봉 시가에 모의 적용 |
| v2 | rsi_14_recovery | 9895.36 | -104.64 | sell / filled / 직전 RSI14 < 30, 현재 RSI14 >= 30 (한 봉 목표); 조건 미충족; RSI14=34.3611, previous_RSI14=32.906; 직전 완료 봉 목표를 다음 봉 시가에 모의 적용 |
| v2 | bollinger_20_reentry | 9829.27 | -170.73 | sell / filled / 직전 종가 < 직전 하단밴드, 현재 하단밴드 <= 종가 <= SMA20 (한 봉 목표); 조건 미충족; close=763.39, lower20=762.854, SMA20=768.639, previous_lower20=763.636; 직전 완료 봉 목표를 다음 봉 시가에 모의 적용 |
| v2 | donchian_20 | 9958.80 | -41.20 | sell / filled / 종가 > 현재 봉을 제외한 직전 20봉 최고가; 조건 미충족; close=769.96, prior_high20=770.3; 직전 완료 봉 목표를 다음 봉 시가에 모의 적용 |
| v2 | atr_14_breakout | 9953.15 | -46.85 | sell / filled / 종가 > 직전 종가 + 직전 ATR14 그리고 종가 > EMA26; 조건 미충족; close=766.58, threshold=768.736, prior_ATR14=1.82624, EMA26=765.727; 직전 완료 봉 목표를 다음 봉 시가에 모의 적용 |
| v2 | session_vwap | 9798.99 | -201.01 | sell / filled / 종가 > 뉴욕 거래일별 누적 전형가격 VWAP; 조건 미충족; close=768.64, session_VWAP=768.839, session_volume=6.99147e+07; 직전 완료 봉 목표를 다음 봉 시가에 모의 적용 |
| v2 | obv_20 | 9905.54 | -94.46 | sell / filled / OBV > OBV의 SMA20 그리고 종가 > EMA26; 조건 미충족; OBV=-1.1153e+07, OBV_SMA20=-7.86173e+06, close=768.275, EMA26=767.362; 직전 완료 봉 목표를 다음 봉 시가에 모의 적용 |
| v2 | stochastic_14_3_recovery | 9812.28 | -187.72 | buy / partial / 직전 %K14 < 20에서 %K14가 %D3 상향 돌파 (한 봉 목표); 조건 충족; K14=23.6558, D3=22.5002, previous_K14=9.97019, previous_D3=26.4496; 직전 완료 봉 목표를 다음 봉 시가에 모의 적용 |
| v2 | mfi_14_recovery | 9953.15 | -46.85 | sell / filled / 직전 MFI14 < 20, 현재 MFI14 >= 20 (한 봉 목표); 조건 미충족; MFI14=24.4041, previous_MFI14=24.1984; 직전 완료 봉 목표를 다음 봉 시가에 모의 적용 |
| v2 | adx_14_trend | 9979.97 | -20.03 | sell / filled / Wilder ADX14 >= 25 그리고 +DI14 > -DI14; 조건 미충족; ADX14=24.2312, plus_DI14=28.3519, minus_DI14=24.6578; 직전 완료 봉 목표를 다음 봉 시가에 모의 적용 |
| v2 | aroon_25_trend | 9857.36 | -142.64 | sell / filled / Aroon25 Up > 70 그리고 Down < 30 (동률이면 최신 극값); 조건 미충족; Aroon_up=68, Aroon_down=20; 직전 완료 봉 목표를 다음 봉 시가에 모의 적용 |
| v2 | cci_20_momentum | 9855.63 | -144.37 | sell / filled / CCI20 > 100 (전형가격·평균절대편차); 조건 미충족; CCI20=98.503; 직전 완료 봉 목표를 다음 봉 시가에 모의 적용 |
| v2 | williams_14_recovery | 9784.23 | -215.77 | buy / partial / 직전 Williams %R14 < -80, 현재 >= -80 (한 봉 목표); 조건 충족; Williams_R14=-76.3442, previous_R14=-90.0298; 직전 완료 봉 목표를 다음 봉 시가에 모의 적용 |
| v2 | cmf_20_accumulation | 9887.00 | -113.00 | sell / filled / Chaikin Money Flow20 > 0.1; 조건 미충족; CMF20=0.0493062, volume20=8.08389e+07; 직전 완료 봉 목표를 다음 봉 시가에 모의 적용 |
| v2 | chaikin_3_10 | 9858.53 | -141.47 | sell / filled / ADL의 EMA3 - EMA10 > 0 그리고 종가 > EMA26; 조건 미충족; Chaikin3_10=-974621, ADL=7.60516e+06, close=768.275, EMA26=767.362; 직전 완료 봉 목표를 다음 봉 시가에 모의 적용 |
| v2 | roc_10_momentum | 9951.43 | -48.57 | sell / filled / 10봉 ROC > 1% 그리고 종가 > EMA26; 조건 미충족; ROC10_percent=0.806376, close=769.45, EMA26=767.181; 직전 완료 봉 목표를 다음 봉 시가에 모의 적용 |
| v2 | trix_15_trend | 9842.05 | -157.95 | buy / partial / 15봉 삼중 EMA의 1봉 변화율 TRIX > 0 그리고 종가 > EMA26; 조건 충족; TRIX15_percent=0.00716671, close=767.62, EMA26=767.441; 직전 완료 봉 목표를 다음 봉 시가에 모의 적용 |
| v2 | keltner_20_breakout | 10000.00 | 0.00 | 대기 /  / 새 신호 대기 |
| v2 | opening_range_30m | 9840.86 | -159.14 | sell / filled / 뉴욕 09:30·09:45 두 완료 봉 최고가를 10:00 이후 종가가 돌파; 조건 미충족; close=767.51, opening_high=768.06; 직전 완료 봉 목표를 다음 봉 시가에 모의 적용 |

### 같은 기간의 비용·노출 비교 (사후 연구)

| 전략 | 비용 전 | 비용 후 | 100% 보유 | 같은 평균 노출 보유 | 평균 노출 |
|---|---:|---:|---:|---:|---:|
| cash | 0.00% | 0.00% | -0.08% | -0.00% | 0.00% |
| buy_hold | 0.34% | -0.08% | -0.08% | -0.08% | 100.00% |
| trend_8_26 | 1.49% | -1.86% | -0.08% | -0.04% | 50.00% |
| momentum_26 | -0.43% | -4.52% | -0.08% | -0.04% | 48.43% |
| breakout_8 | -0.22% | -15.65% | -0.08% | -0.02% | 22.25% |
| reversion_12 | -1.55% | -12.84% | -0.08% | -0.02% | 29.32% |
| volume_26 | -1.07% | -10.56% | -0.08% | -0.01% | 9.16% |
| trend_8_26 AND momentum_26 | 0.64% | -3.09% | -0.08% | -0.03% | 42.67% |
| trend_8_26 + momentum_26 | 0.53% | -3.20% | -0.08% | -0.04% | 49.22% |
| trend_8_26 AND breakout_8 | 0.17% | -10.57% | -0.08% | -0.01% | 13.09% |
| trend_8_26 + breakout_8 | 0.64% | -8.83% | -0.08% | -0.03% | 36.13% |
| trend_8_26 AND reversion_12 | -0.14% | -3.84% | -0.08% | -0.00% | 6.54% |
| trend_8_26 + reversion_12 | -0.03% | -7.33% | -0.08% | -0.03% | 39.66% |
| trend_8_26 AND volume_26 | -0.68% | -5.16% | -0.08% | -0.00% | 4.71% |
| trend_8_26 + volume_26 | 0.20% | -6.32% | -0.08% | -0.02% | 29.59% |
| momentum_26 AND breakout_8 | 0.31% | -10.44% | -0.08% | -0.01% | 13.87% |
| momentum_26 + breakout_8 | -0.32% | -10.26% | -0.08% | -0.03% | 35.35% |
| momentum_26 AND reversion_12 | -0.76% | -4.85% | -0.08% | -0.01% | 6.81% |
| momentum_26 + reversion_12 | -0.99% | -8.21% | -0.08% | -0.03% | 38.88% |
| momentum_26 AND volume_26 | -0.40% | -3.69% | -0.08% | -0.00% | 2.88% |
| momentum_26 + volume_26 | -0.75% | -6.43% | -0.08% | -0.02% | 28.80% |
| breakout_8 AND reversion_12 | 0.00% | 0.00% | -0.08% | -0.00% | 0.00% |
| breakout_8 + reversion_12 | -0.88% | -13.73% | -0.08% | -0.02% | 25.79% |
| breakout_8 AND volume_26 | 0.03% | -1.64% | -0.08% | -0.00% | 1.57% |
| breakout_8 + volume_26 | -0.65% | -12.23% | -0.08% | -0.01% | 15.71% |
| reversion_12 AND volume_26 | -0.93% | -5.40% | -0.08% | -0.00% | 3.93% |
| reversion_12 + volume_26 | -1.31% | -11.34% | -0.08% | -0.01% | 19.25% |
| ema_12_26 | -0.28% | -3.58% | -0.08% | -0.04% | 50.26% |
| macd_12_26_9 | 0.30% | -4.23% | -0.08% | -0.02% | 31.41% |
| rsi_14_recovery | -0.53% | -4.22% | -0.08% | -0.00% | 2.36% |
| bollinger_20_reentry | -1.13% | -7.17% | -0.08% | -0.00% | 3.93% |
| donchian_20 | 0.11% | -7.17% | -0.08% | -0.01% | 6.81% |
| atr_14_breakout | 0.38% | -4.55% | -0.08% | -0.00% | 3.66% |
| session_vwap | 2.10% | -7.69% | -0.08% | -0.04% | 47.91% |
| obv_20 | 0.26% | -7.43% | -0.08% | -0.03% | 38.74% |
| stochastic_14_3_recovery | -0.88% | -15.85% | -0.08% | -0.01% | 10.21% |
| mfi_14_recovery | -0.06% | -2.96% | -0.08% | -0.00% | 1.83% |
| adx_14_trend | 0.32% | -3.40% | -0.08% | -0.02% | 28.01% |
| aroon_25_trend | 0.82% | -2.10% | -0.08% | -0.02% | 25.65% |
| cci_20_momentum | -0.04% | -8.10% | -0.08% | -0.02% | 21.99% |
| williams_14_recovery | -0.79% | -11.43% | -0.08% | -0.01% | 7.07% |
| cmf_20_accumulation | 2.29% | -1.50% | -0.08% | -0.03% | 45.29% |
| chaikin_3_10 | 1.85% | -4.77% | -0.08% | -0.03% | 40.05% |
| roc_10_momentum | -0.13% | -0.97% | -0.08% | -0.00% | 1.05% |
| trix_15_trend | -0.21% | -3.50% | -0.08% | -0.03% | 36.91% |
| keltner_20_breakout | 0.09% | -3.62% | -0.08% | -0.01% | 10.73% |
| opening_range_30m | 0.36% | -5.37% | -0.08% | -0.02% | 31.68% |

동일 구간·초기 자금, 종료 시 청산 비용 포함. 노출 맞춤은 사후 설명용이며 v2 실제 계좌 성과가 아닙니다.
[낙폭 분해·비용 영향·전체 구간](SPY/comparison.json)

[v1 전체 기록](SPY/accounts.json) · [v2 전체 기록](SPY/accounts-v2.json)

## QQQ 계좌

| 모델 | 전략 | 평가액 USD | 손익 USD | 최근 매매·이유 |
|---|---|---:|---:|---|
| v1 | cash | 10000.00 | 0.00 | 대기 /  / 새 신호 대기 |
| v1 | buy_hold | 9896.38 | -103.62 | buy /  / buy_hold: prior completed bar target 100%; next bar open simulation |
| v1 | trend_8_26 | 9889.16 | -110.84 | buy /  / trend_8_26: prior completed bar target 100%; next bar open simulation |
| v1 | momentum_26 | 9831.61 | -168.39 | buy /  / momentum_26: prior completed bar target 100%; next bar open simulation |
| v1 | breakout_8 | 9897.90 | -102.10 | sell /  / breakout_8: prior completed bar target 0%; next bar open simulation |
| v1 | reversion_12 | 9861.94 | -138.06 | buy /  / reversion_12: prior completed bar target 100%; next bar open simulation |
| v1 | volume_26 | 9763.59 | -236.41 | sell /  / volume_26: prior completed bar target 0%; next bar open simulation |
| v1 | trend_8_26 AND momentum_26 | 9897.69 | -102.31 | buy /  / trend_8_26 AND momentum_26: prior completed bar target 100%; next bar open simulation |
| v1 | trend_8_26 + momentum_26 | 9880.06 | -119.94 | buy /  / trend_8_26 + momentum_26: prior completed bar target 100%; next bar open simulation |
| v1 | trend_8_26 AND breakout_8 | 9989.91 | -10.09 | sell /  / trend_8_26 AND breakout_8: prior completed bar target 0%; next bar open simulation |
| v1 | trend_8_26 + breakout_8 | 9913.25 | -86.75 | sell /  / trend_8_26 + breakout_8: prior completed bar target 50%; next bar open simulation |
| v1 | trend_8_26 AND reversion_12 | 9924.33 | -75.67 | buy /  / trend_8_26 AND reversion_12: prior completed bar target 100%; next bar open simulation |
| v1 | trend_8_26 + reversion_12 | 9875.68 | -124.32 | buy /  / trend_8_26 + reversion_12: prior completed bar target 100%; next bar open simulation |
| v1 | trend_8_26 AND volume_26 | 9932.72 | -67.28 | sell /  / trend_8_26 AND volume_26: prior completed bar target 0%; next bar open simulation |
| v1 | trend_8_26 + volume_26 | 9826.11 | -173.89 | sell /  / trend_8_26 + volume_26: prior completed bar target 50%; next bar open simulation |
| v1 | momentum_26 AND breakout_8 | 9929.95 | -70.05 | sell /  / momentum_26 AND breakout_8: prior completed bar target 0%; next bar open simulation |
| v1 | momentum_26 + breakout_8 | 9864.67 | -135.33 | sell /  / momentum_26 + breakout_8: prior completed bar target 50%; next bar open simulation |
| v1 | momentum_26 AND reversion_12 | 9924.33 | -75.67 | buy /  / momentum_26 AND reversion_12: prior completed bar target 100%; next bar open simulation |
| v1 | momentum_26 + reversion_12 | 9846.92 | -153.08 | buy /  / momentum_26 + reversion_12: prior completed bar target 100%; next bar open simulation |
| v1 | momentum_26 AND volume_26 | 9912.22 | -87.78 | sell /  / momentum_26 AND volume_26: prior completed bar target 0%; next bar open simulation |
| v1 | momentum_26 + volume_26 | 9817.09 | -182.91 | sell /  / momentum_26 + volume_26: prior completed bar target 50%; next bar open simulation |
| v1 | breakout_8 AND reversion_12 | 10000.00 | 0.00 | 대기 /  / 새 신호 대기 |
| v1 | breakout_8 + reversion_12 | 9880.00 | -120.00 | sell /  / breakout_8 + reversion_12: prior completed bar target 50%; next bar open simulation |
| v1 | breakout_8 AND volume_26 | 9947.15 | -52.85 | sell /  / breakout_8 AND volume_26: prior completed bar target 0%; next bar open simulation |
| v1 | breakout_8 + volume_26 | 9850.15 | -149.85 | sell /  / breakout_8 + volume_26: prior completed bar target 0%; next bar open simulation |
| v1 | reversion_12 AND volume_26 | 9907.31 | -92.69 | sell /  / reversion_12 AND volume_26: prior completed bar target 0%; next bar open simulation |
| v1 | reversion_12 + volume_26 | 9852.03 | -147.97 | sell /  / reversion_12 + volume_26: prior completed bar target 50%; next bar open simulation |
| v1 | ema_12_26 | 9886.94 | -113.06 | buy /  / EMA12 > EMA26; 조건 충족; EMA12=717, EMA26=716.746 |
| v1 | macd_12_26_9 | 9865.80 | -134.20 | sell /  / MACD > 신호선 그리고 MACD > 0; 조건 미충족; MACD=0.926099, signal9=1.03237 |
| v1 | rsi_14_recovery | 9813.02 | -186.98 | sell /  / 직전 RSI14 < 30, 현재 RSI14 >= 30 (한 봉 목표); 조건 미충족; RSI14=58.2718, previous_RSI14=33.2263 |
| v1 | bollinger_20_reentry | 9882.24 | -117.76 | sell /  / 직전 종가 < 직전 하단밴드, 현재 하단밴드 <= 종가 <= SMA20 (한 봉 목표); 조건 미충족; close=716.64, lower20=715.793, SMA20=723.132, previous_lower20=716.805 |
| v1 | donchian_20 | 9951.11 | -48.89 | sell /  / 종가 > 현재 봉을 제외한 직전 20봉 최고가; 조건 미충족; close=724.13, prior_high20=724.151 |
| v1 | atr_14_breakout | 9945.53 | -54.47 | sell /  / 종가 > 직전 종가 + 직전 ATR14 그리고 종가 > EMA26; 조건 미충족; close=717.88, threshold=721.828, prior_ATR14=2.82823, EMA26=715.308 |
| v1 | session_vwap | 9802.73 | -197.27 | sell /  / 종가 > 뉴욕 거래일별 누적 전형가격 VWAP; 조건 미충족; close=721.515, session_VWAP=722.066, session_volume=4.49868e+08 |
| v1 | obv_20 | 9895.17 | -104.83 | sell /  / OBV > OBV의 SMA20 그리고 종가 > EMA26; 조건 미충족; OBV=3.95079e+07, OBV_SMA20=5.9237e+07, close=719.38, EMA26=719.317 |
| v1 | stochastic_14_3_recovery | 9659.03 | -340.97 | sell /  / 직전 %K14 < 20에서 %K14가 %D3 상향 돌파 (한 봉 목표); 조건 미충족; K14=90.6084, D3=42.9821, previous_K14=27.5933, previous_D3=23.7441 |
| v1 | mfi_14_recovery | 9927.15 | -72.85 | sell /  / 직전 MFI14 < 20, 현재 MFI14 >= 20 (한 봉 목표); 조건 미충족; MFI14=58.7386, previous_MFI14=43.5194 |
| v1 | adx_14_trend | 9926.53 | -73.47 | sell /  / Wilder ADX14 >= 25 그리고 +DI14 > -DI14; 조건 미충족; ADX14=23.9831, plus_DI14=26.5781, minus_DI14=24.6326 |
| v1 | aroon_25_trend | 9875.01 | -124.99 | sell /  / Aroon25 Up > 70 그리고 Down < 30 (동률이면 최신 극값); 조건 미충족; Aroon_up=68, Aroon_down=20 |
| v1 | cci_20_momentum | 9950.47 | -49.53 | sell /  / CCI20 > 100 (전형가격·평균절대편차); 조건 미충족; CCI20=97.528 |
| v1 | williams_14_recovery | 9771.17 | -228.83 | buy /  / 직전 Williams %R14 < -80, 현재 >= -80 (한 봉 목표); 조건 충족; Williams_R14=-79.0998, previous_R14=-93.4903 |
| v1 | cmf_20_accumulation | 9709.61 | -290.39 | sell /  / Chaikin Money Flow20 > 0.1; 조건 미충족; CMF20=0.0836393, volume20=5.30174e+08 |
| v1 | chaikin_3_10 | 9899.84 | -100.16 | sell /  / ADL의 EMA3 - EMA10 > 0 그리고 종가 > EMA26; 조건 미충족; Chaikin3_10=-495746, ADL=2.16147e+08, close=719.63, EMA26=719.312 |
| v1 | roc_10_momentum | 9990.50 | -9.50 | sell /  / 10봉 ROC > 1% 그리고 종가 > EMA26; 조건 미충족; ROC10_percent=0.483561, close=722.477, EMA26=718.78 |
| v1 | trix_15_trend | 9925.94 | -74.06 | buy /  / 15봉 삼중 EMA의 1봉 변화율 TRIX > 0 그리고 종가 > EMA26; 조건 충족; TRIX15_percent=0.000507984, close=723.31, EMA26=718.484 |
| v1 | keltner_20_breakout | 9904.16 | -95.84 | sell /  / 종가 > EMA20 + 2 x Wilder ATR14; 조건 미충족; close=723.31, upper_Keltner=723.407, EMA20=718.722, ATR14=2.34265 |
| v1 | opening_range_30m | 9887.22 | -112.78 | sell /  / 뉴욕 09:30·09:45 두 완료 봉 최고가를 10:00 이후 종가가 돌파; 조건 미충족; close=719.99, opening_high=720.22 |
| v2 | cash | 10000.00 | 0.00 | 대기 /  / 새 신호 대기 |
| v2 | buy_hold | 9576.49 | -423.51 | buy / partial / 직전 완료 봉 목표 비중 100%; 다음 봉 시가 가정 |
| v2 | trend_8_26 | 9692.12 | -307.88 | buy / partial / 직전 완료 봉 목표 비중 100%; 다음 봉 시가 가정 |
| v2 | momentum_26 | 9726.24 | -273.76 | buy / partial / 직전 완료 봉 목표 비중 100%; 다음 봉 시가 가정 |
| v2 | breakout_8 | 9565.39 | -434.61 | sell / filled / 직전 완료 봉 목표 비중 0%; 다음 봉 시가 가정 |
| v2 | reversion_12 | 9376.01 | -623.99 | buy / partial / 직전 완료 봉 목표 비중 100%; 다음 봉 시가 가정 |
| v2 | volume_26 | 9565.80 | -434.20 | 중단: 손실 한도 / sell / filled / 직전 완료 봉 목표 비중 0%; 다음 봉 시가 가정 |
| v2 | trend_8_26 AND momentum_26 | 9793.56 | -206.44 | buy / partial / 직전 완료 봉 목표 비중 100%; 다음 봉 시가 가정 |
| v2 | trend_8_26 + momentum_26 | 9729.59 | -270.41 | buy / partial / 직전 완료 봉 목표 비중 100%; 다음 봉 시가 가정 |
| v2 | trend_8_26 AND breakout_8 | 9883.87 | -116.13 | sell / filled / 직전 완료 봉 목표 비중 0%; 다음 봉 시가 가정 |
| v2 | trend_8_26 + breakout_8 | 9648.67 | -351.33 | sell / filled / 직전 완료 봉 목표 비중 50%; 다음 봉 시가 가정 |
| v2 | trend_8_26 AND reversion_12 | 9783.59 | -216.41 | buy / partial / 직전 완료 봉 목표 비중 100%; 다음 봉 시가 가정 |
| v2 | trend_8_26 + reversion_12 | 9532.59 | -467.41 | buy / partial / 직전 완료 봉 목표 비중 100%; 다음 봉 시가 가정 |
| v2 | trend_8_26 AND volume_26 | 9769.99 | -230.01 | sell / filled / 직전 완료 봉 목표 비중 0%; 다음 봉 시가 가정 |
| v2 | trend_8_26 + volume_26 | 9429.99 | -570.01 | sell / filled / 직전 완료 봉 목표 비중 50%; 다음 봉 시가 가정 |
| v2 | momentum_26 AND breakout_8 | 9886.96 | -113.04 | sell / filled / 직전 완료 봉 목표 비중 0%; 다음 봉 시가 가정 |
| v2 | momentum_26 + breakout_8 | 9645.41 | -354.59 | sell / filled / 직전 완료 봉 목표 비중 50%; 다음 봉 시가 가정 |
| v2 | momentum_26 AND reversion_12 | 9921.35 | -78.65 | buy / partial / 직전 완료 봉 목표 비중 100%; 다음 봉 시가 가정 |
| v2 | momentum_26 + reversion_12 | 9569.42 | -430.58 | buy / partial / 직전 완료 봉 목표 비중 100%; 다음 봉 시가 가정 |
| v2 | momentum_26 AND volume_26 | 9845.67 | -154.33 | sell / filled / 직전 완료 봉 목표 비중 0%; 다음 봉 시가 가정 |
| v2 | momentum_26 + volume_26 | 9466.42 | -533.58 | sell / filled / 직전 완료 봉 목표 비중 50%; 다음 봉 시가 가정 |
| v2 | breakout_8 AND reversion_12 | 10000.00 | 0.00 | 대기 /  / 새 신호 대기 |
| v2 | breakout_8 + reversion_12 | 9529.86 | -470.14 | sell / filled / 직전 완료 봉 목표 비중 50%; 다음 봉 시가 가정 |
| v2 | breakout_8 AND volume_26 | 9891.45 | -108.55 | sell / filled / 직전 완료 봉 목표 비중 0%; 다음 봉 시가 가정 |
| v2 | breakout_8 + volume_26 | 9427.43 | -572.57 | sell / filled / 직전 완료 봉 목표 비중 0%; 다음 봉 시가 가정 |
| v2 | reversion_12 AND volume_26 | 9547.64 | -452.36 | 중단: 손실 한도 / sell / filled / 직전 완료 봉 목표 비중 0%; 다음 봉 시가 가정 |
| v2 | reversion_12 + volume_26 | 9333.82 | -666.18 | sell / filled / 직전 완료 봉 목표 비중 50%; 다음 봉 시가 가정 |
| v2 | ema_12_26 | 9883.98 | -116.02 | buy / partial / EMA12 > EMA26; 조건 충족; EMA12=717, EMA26=716.746; 직전 완료 봉 목표를 다음 봉 시가에 모의 적용 |
| v2 | macd_12_26_9 | 9861.86 | -138.14 | sell / filled / MACD > 신호선 그리고 MACD > 0; 조건 미충족; MACD=0.926099, signal9=1.03237; 직전 완료 봉 목표를 다음 봉 시가에 모의 적용 |
| v2 | rsi_14_recovery | 9807.13 | -192.87 | sell / filled / 직전 RSI14 < 30, 현재 RSI14 >= 30 (한 봉 목표); 조건 미충족; RSI14=58.2718, previous_RSI14=33.2263; 직전 완료 봉 목표를 다음 봉 시가에 모의 적용 |
| v2 | bollinger_20_reentry | 9878.29 | -121.71 | sell / filled / 직전 종가 < 직전 하단밴드, 현재 하단밴드 <= 종가 <= SMA20 (한 봉 목표); 조건 미충족; close=716.64, lower20=715.793, SMA20=723.132, previous_lower20=716.805; 직전 완료 봉 목표를 다음 봉 시가에 모의 적용 |
| v2 | donchian_20 | 9947.13 | -52.87 | sell / filled / 종가 > 현재 봉을 제외한 직전 20봉 최고가; 조건 미충족; close=724.13, prior_high20=724.151; 직전 완료 봉 목표를 다음 봉 시가에 모의 적용 |
| v2 | atr_14_breakout | 9943.55 | -56.45 | sell / filled / 종가 > 직전 종가 + 직전 ATR14 그리고 종가 > EMA26; 조건 미충족; close=717.88, threshold=721.828, prior_ATR14=2.82823, EMA26=715.308; 직전 완료 봉 목표를 다음 봉 시가에 모의 적용 |
| v2 | session_vwap | 9794.89 | -205.11 | sell / filled / 종가 > 뉴욕 거래일별 누적 전형가격 VWAP; 조건 미충족; close=721.515, session_VWAP=722.066, session_volume=4.49868e+08; 직전 완료 봉 목표를 다음 봉 시가에 모의 적용 |
| v2 | obv_20 | 9891.21 | -108.79 | sell / filled / OBV > OBV의 SMA20 그리고 종가 > EMA26; 조건 미충족; OBV=3.95079e+07, OBV_SMA20=5.9237e+07, close=719.38, EMA26=719.317; 직전 완료 봉 목표를 다음 봉 시가에 모의 적용 |
| v2 | stochastic_14_3_recovery | 9694.13 | -305.87 | 중단: 손실 한도 / sell / filled / 직전 %K14 < 20에서 %K14가 %D3 상향 돌파 (한 봉 목표); 조건 미충족; K14=10.576, D3=8.00581, previous_K14=7.39787, previous_D3=7.27486; 직전 완료 봉 목표를 다음 봉 시가에 모의 적용 |
| v2 | mfi_14_recovery | 9925.16 | -74.84 | sell / filled / 직전 MFI14 < 20, 현재 MFI14 >= 20 (한 봉 목표); 조건 미충족; MFI14=58.7386, previous_MFI14=43.5194; 직전 완료 봉 목표를 다음 봉 시가에 모의 적용 |
| v2 | adx_14_trend | 9922.56 | -77.44 | sell / filled / Wilder ADX14 >= 25 그리고 +DI14 > -DI14; 조건 미충족; ADX14=23.9831, plus_DI14=26.5781, minus_DI14=24.6326; 직전 완료 봉 목표를 다음 봉 시가에 모의 적용 |
| v2 | aroon_25_trend | 9871.06 | -128.94 | sell / filled / Aroon25 Up > 70 그리고 Down < 30 (동률이면 최신 극값); 조건 미충족; Aroon_up=68, Aroon_down=20; 직전 완료 봉 목표를 다음 봉 시가에 모의 적용 |
| v2 | cci_20_momentum | 9946.49 | -53.51 | sell / filled / CCI20 > 100 (전형가격·평균절대편차); 조건 미충족; CCI20=97.528; 직전 완료 봉 목표를 다음 봉 시가에 모의 적용 |
| v2 | williams_14_recovery | 9762.38 | -237.62 | buy / partial / 직전 Williams %R14 < -80, 현재 >= -80 (한 봉 목표); 조건 충족; Williams_R14=-79.0998, previous_R14=-93.4903; 직전 완료 봉 목표를 다음 봉 시가에 모의 적용 |
| v2 | cmf_20_accumulation | 9699.90 | -300.10 | sell / filled / Chaikin Money Flow20 > 0.1; 조건 미충족; CMF20=0.0836393, volume20=5.30174e+08; 직전 완료 봉 목표를 다음 봉 시가에 모의 적용 |
| v2 | chaikin_3_10 | 9895.89 | -104.11 | sell / filled / ADL의 EMA3 - EMA10 > 0 그리고 종가 > EMA26; 조건 미충족; Chaikin3_10=-495746, ADL=2.16147e+08, close=719.63, EMA26=719.312; 직전 완료 봉 목표를 다음 봉 시가에 모의 적용 |
| v2 | roc_10_momentum | 9988.50 | -11.50 | sell / filled / 10봉 ROC > 1% 그리고 종가 > EMA26; 조건 미충족; ROC10_percent=0.483561, close=722.477, EMA26=718.78; 직전 완료 봉 목표를 다음 봉 시가에 모의 적용 |
| v2 | trix_15_trend | 9924.95 | -75.05 | buy / partial / 15봉 삼중 EMA의 1봉 변화율 TRIX > 0 그리고 종가 > EMA26; 조건 충족; TRIX15_percent=0.000507984, close=723.31, EMA26=718.484; 직전 완료 봉 목표를 다음 봉 시가에 모의 적용 |
| v2 | keltner_20_breakout | 9900.20 | -99.80 | sell / filled / 종가 > EMA20 + 2 x Wilder ATR14; 조건 미충족; close=723.31, upper_Keltner=723.407, EMA20=718.722, ATR14=2.34265; 직전 완료 봉 목표를 다음 봉 시가에 모의 적용 |
| v2 | opening_range_30m | 9883.27 | -116.73 | sell / filled / 뉴욕 09:30·09:45 두 완료 봉 최고가를 10:00 이후 종가가 돌파; 조건 미충족; close=719.99, opening_high=720.22; 직전 완료 봉 목표를 다음 봉 시가에 모의 적용 |

### 같은 기간의 비용·노출 비교 (사후 연구)

| 전략 | 비용 전 | 비용 후 | 100% 보유 | 같은 평균 노출 보유 | 평균 노출 |
|---|---:|---:|---:|---:|---:|
| cash | 0.00% | 0.00% | -2.77% | -0.00% | 0.00% |
| buy_hold | -2.36% | -2.77% | -2.77% | -2.77% | 100.00% |
| trend_8_26 | 0.60% | -3.13% | -2.77% | -1.27% | 46.07% |
| momentum_26 | -1.20% | -6.45% | -2.77% | -1.13% | 40.84% |
| breakout_8 | -0.79% | -16.13% | -2.77% | -0.52% | 18.85% |
| reversion_12 | -0.22% | -13.14% | -2.77% | -0.82% | 29.58% |
| volume_26 | -1.06% | -14.23% | -2.77% | -0.43% | 15.71% |
| trend_8_26 AND momentum_26 | 0.03% | -4.08% | -2.77% | -0.99% | 35.86% |
| trend_8_26 + momentum_26 | -0.30% | -4.40% | -2.77% | -1.20% | 43.46% |
| trend_8_26 AND breakout_8 | -0.02% | -9.22% | -2.77% | -0.32% | 11.52% |
| trend_8_26 + breakout_8 | -0.09% | -9.30% | -2.77% | -0.90% | 32.47% |
| trend_8_26 AND reversion_12 | 0.08% | -5.63% | -2.77% | -0.19% | 6.81% |
| trend_8_26 + reversion_12 | 0.20% | -7.89% | -2.77% | -1.04% | 37.83% |
| trend_8_26 AND volume_26 | 0.21% | -4.71% | -2.77% | -0.14% | 5.24% |
| trend_8_26 + volume_26 | -0.23% | -8.66% | -2.77% | -0.85% | 30.90% |
| momentum_26 AND breakout_8 | -0.03% | -9.24% | -2.77% | -0.31% | 11.26% |
| momentum_26 + breakout_8 | -0.99% | -11.24% | -2.77% | -0.82% | 29.85% |
| momentum_26 AND reversion_12 | -0.37% | -6.06% | -2.77% | -0.18% | 6.54% |
| momentum_26 + reversion_12 | -0.70% | -9.48% | -2.77% | -0.97% | 35.21% |
| momentum_26 AND volume_26 | -0.04% | -4.56% | -2.77% | -0.12% | 4.19% |
| momentum_26 + volume_26 | -1.13% | -10.05% | -2.77% | -0.78% | 28.28% |
| breakout_8 AND reversion_12 | 0.00% | 0.00% | -2.77% | -0.00% | 0.00% |
| breakout_8 + reversion_12 | -0.50% | -13.76% | -2.77% | -0.67% | 24.22% |
| breakout_8 AND volume_26 | 0.31% | -2.60% | -2.77% | -0.06% | 2.09% |
| breakout_8 + volume_26 | -0.92% | -13.76% | -2.77% | -0.48% | 17.29% |
| reversion_12 AND volume_26 | -1.31% | -8.11% | -2.77% | -0.23% | 8.38% |
| reversion_12 + volume_26 | -0.63% | -12.96% | -2.77% | -0.62% | 22.65% |
| ema_12_26 | 0.69% | -1.40% | -2.77% | -1.05% | 38.22% |
| macd_12_26_9 | 1.23% | -2.52% | -2.77% | -0.64% | 23.04% |
| rsi_14_recovery | -0.83% | -5.71% | -2.77% | -0.09% | 3.14% |
| bollinger_20_reentry | -0.44% | -6.12% | -2.77% | -0.10% | 3.66% |
| donchian_20 | 0.59% | -4.75% | -2.77% | -0.16% | 5.76% |
| atr_14_breakout | 0.11% | -4.01% | -2.77% | -0.08% | 2.88% |
| session_vwap | -0.52% | -11.93% | -2.77% | -1.32% | 47.91% |
| obv_20 | -0.80% | -9.18% | -2.77% | -0.84% | 30.37% |
| stochastic_14_3_recovery | -0.79% | -12.90% | -2.77% | -0.22% | 8.12% |
| mfi_14_recovery | -0.49% | -2.56% | -2.77% | -0.04% | 1.31% |
| adx_14_trend | -0.11% | -3.00% | -2.77% | -0.59% | 21.47% |
| aroon_25_trend | 1.31% | -2.45% | -2.77% | -0.56% | 20.16% |
| cci_20_momentum | -0.25% | -5.55% | -2.77% | -0.48% | 17.28% |
| williams_14_recovery | -1.06% | -12.40% | -2.77% | -0.21% | 7.59% |
| cmf_20_accumulation | -1.15% | -8.73% | -2.77% | -0.85% | 30.89% |
| chaikin_3_10 | -1.93% | -9.45% | -2.77% | -1.02% | 36.91% |
| roc_10_momentum | -0.00% | -1.67% | -2.77% | -0.12% | 4.19% |
| trix_15_trend | 0.39% | -1.29% | -2.77% | -0.87% | 31.41% |
| keltner_20_breakout | -0.89% | -5.76% | -2.77% | -0.22% | 8.12% |
| opening_range_30m | -0.39% | -6.47% | -2.77% | -0.68% | 24.61% |

동일 구간·초기 자금, 종료 시 청산 비용 포함. 노출 맞춤은 사후 설명용이며 v2 실제 계좌 성과가 아닙니다.
[낙폭 분해·비용 영향·전체 구간](QQQ/comparison.json)

[v1 전체 기록](QQQ/accounts.json) · [v2 전체 기록](QQQ/accounts-v2.json)

## IWM 계좌

| 모델 | 전략 | 평가액 USD | 손익 USD | 최근 매매·이유 |
|---|---|---:|---:|---|
| v1 | cash | 10000.00 | 0.00 | 대기 /  / 새 신호 대기 |
| v1 | buy_hold | 9822.28 | -177.72 | buy /  / buy_hold: prior completed bar target 100%; next bar open simulation |
| v1 | trend_8_26 | 9783.07 | -216.93 | buy /  / trend_8_26: prior completed bar target 100%; next bar open simulation |
| v1 | momentum_26 | 9798.97 | -201.03 | buy /  / momentum_26: prior completed bar target 100%; next bar open simulation |
| v1 | breakout_8 | 9788.68 | -211.32 | sell /  / breakout_8: prior completed bar target 0%; next bar open simulation |
| v1 | reversion_12 | 9807.48 | -192.52 | buy /  / reversion_12: prior completed bar target 100%; next bar open simulation |
| v1 | volume_26 | 9862.10 | -137.90 | sell /  / volume_26: prior completed bar target 0%; next bar open simulation |
| v1 | trend_8_26 AND momentum_26 | 9798.97 | -201.03 | buy /  / trend_8_26 AND momentum_26: prior completed bar target 100%; next bar open simulation |
| v1 | trend_8_26 + momentum_26 | 9791.01 | -208.99 | buy /  / trend_8_26 + momentum_26: prior completed bar target 100%; next bar open simulation |
| v1 | trend_8_26 AND breakout_8 | 9896.83 | -103.17 | sell /  / trend_8_26 AND breakout_8: prior completed bar target 0%; next bar open simulation |
| v1 | trend_8_26 + breakout_8 | 9785.85 | -214.15 | sell /  / trend_8_26 + breakout_8: prior completed bar target 50%; next bar open simulation |
| v1 | trend_8_26 AND reversion_12 | 9848.27 | -151.73 | buy /  / trend_8_26 AND reversion_12: prior completed bar target 100%; next bar open simulation |
| v1 | trend_8_26 + reversion_12 | 9795.20 | -204.80 | buy /  / trend_8_26 + reversion_12: prior completed bar target 100%; next bar open simulation |
| v1 | trend_8_26 AND volume_26 | 9935.98 | -64.02 | sell /  / trend_8_26 AND volume_26: prior completed bar target 0%; next bar open simulation |
| v1 | trend_8_26 + volume_26 | 9822.40 | -177.60 | sell /  / trend_8_26 + volume_26: prior completed bar target 50%; next bar open simulation |
| v1 | momentum_26 AND breakout_8 | 9929.38 | -70.62 | sell /  / momentum_26 AND breakout_8: prior completed bar target 0%; next bar open simulation |
| v1 | momentum_26 + breakout_8 | 9813.39 | -186.61 | sell /  / momentum_26 + breakout_8: prior completed bar target 50%; next bar open simulation |
| v1 | momentum_26 AND reversion_12 | 9945.51 | -54.49 | buy /  / momentum_26 AND reversion_12: prior completed bar target 100%; next bar open simulation |
| v1 | momentum_26 + reversion_12 | 9822.77 | -177.23 | buy /  / momentum_26 + reversion_12: prior completed bar target 100%; next bar open simulation |
| v1 | momentum_26 AND volume_26 | 10000.00 | 0.00 | 대기 /  / 새 신호 대기 |
| v1 | momentum_26 + volume_26 | 9830.40 | -169.60 | sell /  / momentum_26 + volume_26: prior completed bar target 50%; next bar open simulation |
| v1 | breakout_8 AND reversion_12 | 10000.00 | 0.00 | 대기 /  / 새 신호 대기 |
| v1 | breakout_8 + reversion_12 | 9797.96 | -202.04 | sell /  / breakout_8 + reversion_12: prior completed bar target 50%; next bar open simulation |
| v1 | breakout_8 AND volume_26 | 9944.66 | -55.34 | sell /  / breakout_8 AND volume_26: prior completed bar target 0%; next bar open simulation |
| v1 | breakout_8 + volume_26 | 9825.26 | -174.74 | sell /  / breakout_8 + volume_26: prior completed bar target 0%; next bar open simulation |
| v1 | reversion_12 AND volume_26 | 9935.98 | -64.02 | sell /  / reversion_12 AND volume_26: prior completed bar target 0%; next bar open simulation |
| v1 | reversion_12 + volume_26 | 9854.38 | -145.62 | sell /  / reversion_12 + volume_26: prior completed bar target 50%; next bar open simulation |
| v1 | ema_12_26 | 9765.70 | -234.30 | sell /  / EMA12 > EMA26; 조건 미충족; EMA12=271.688, EMA26=271.689 |
| v1 | macd_12_26_9 | 9843.57 | -156.43 | sell /  / MACD > 신호선 그리고 MACD > 0; 조건 미충족; MACD=-0.000914046, signal9=-0.103888 |
| v1 | rsi_14_recovery | 9786.95 | -213.05 | sell /  / 직전 RSI14 < 30, 현재 RSI14 >= 30 (한 봉 목표); 조건 미충족; RSI14=46.986, previous_RSI14=37.1649 |
| v1 | bollinger_20_reentry | 9924.03 | -75.97 | sell /  / 직전 종가 < 직전 하단밴드, 현재 하단밴드 <= 종가 <= SMA20 (한 봉 목표); 조건 미충족; close=271.19, lower20=270.018, SMA20=273.224, previous_lower20=270.283 |
| v1 | donchian_20 | 9929.38 | -70.62 | sell /  / 종가 > 현재 봉을 제외한 직전 20봉 최고가; 조건 미충족; close=274.88, prior_high20=275.91 |
| v1 | atr_14_breakout | 9896.46 | -103.54 | sell /  / 종가 > 직전 종가 + 직전 ATR14 그리고 종가 > EMA26; 조건 미충족; close=272.33, threshold=272.867, prior_ATR14=0.716592, EMA26=271.567 |
| v1 | session_vwap | 9812.86 | -187.14 | sell /  / 종가 > 뉴욕 거래일별 누적 전형가격 VWAP; 조건 미충족; close=271.41, session_VWAP=271.719, session_volume=1.03316e+07 |
| v1 | obv_20 | 9804.29 | -195.71 | sell /  / OBV > OBV의 SMA20 그리고 종가 > EMA26; 조건 미충족; OBV=-4.38074e+07, OBV_SMA20=-4.40508e+07, close=271.41, EMA26=271.689 |
| v1 | stochastic_14_3_recovery | 9729.51 | -270.49 | sell /  / 직전 %K14 < 20에서 %K14가 %D3 상향 돌파 (한 봉 목표); 조건 미충족; K14=51.9268, D3=28.8672, previous_K14=30.3264, previous_D3=23.1523 |
| v1 | mfi_14_recovery | 9962.66 | -37.34 | sell /  / 직전 MFI14 < 20, 현재 MFI14 >= 20 (한 봉 목표); 조건 미충족; MFI14=33.2861, previous_MFI14=27.7983 |
| v1 | adx_14_trend | 9840.05 | -159.95 | sell /  / Wilder ADX14 >= 25 그리고 +DI14 > -DI14; 조건 미충족; ADX14=23.881, plus_DI14=25.6616, minus_DI14=25.2483 |
| v1 | aroon_25_trend | 9822.02 | -177.98 | sell /  / Aroon25 Up > 70 그리고 Down < 30 (동률이면 최신 극값); 조건 미충족; Aroon_up=68, Aroon_down=20 |
| v1 | cci_20_momentum | 9879.55 | -120.45 | sell /  / CCI20 > 100 (전형가격·평균절대편차); 조건 미충족; CCI20=81.8699 |
| v1 | williams_14_recovery | 9903.90 | -96.10 | sell /  / 직전 Williams %R14 < -80, 현재 >= -80 (한 봉 목표); 조건 미충족; Williams_R14=-48.0732, previous_R14=-69.6736 |
| v1 | cmf_20_accumulation | 9799.11 | -200.89 | sell /  / Chaikin Money Flow20 > 0.1; 조건 미충족; CMF20=0.0512251, volume20=2.08469e+07 |
| v1 | chaikin_3_10 | 9805.17 | -194.83 | sell /  / ADL의 EMA3 - EMA10 > 0 그리고 종가 > EMA26; 조건 미충족; Chaikin3_10=-9609.69, ADL=-6.08839e+07, close=271.41, EMA26=271.689 |
| v1 | roc_10_momentum | 10000.00 | 0.00 | 대기 /  / 새 신호 대기 |
| v1 | trix_15_trend | 9895.73 | -104.27 | sell /  / 15봉 삼중 EMA의 1봉 변화율 TRIX > 0 그리고 종가 > EMA26; 조건 미충족; TRIX15_percent=0.0257204, close=273.74, EMA26=273.991 |
| v1 | keltner_20_breakout | 9937.31 | -62.69 | sell /  / 종가 > EMA20 + 2 x Wilder ATR14; 조건 미충족; close=274.88, upper_Keltner=275.161, EMA20=274.044, ATR14=0.558498 |
| v1 | opening_range_30m | 9968.03 | -31.97 | sell /  / 뉴욕 09:30·09:45 두 완료 봉 최고가를 10:00 이후 종가가 돌파; 자료 부족·변동폭 또는 거래량 없음: 대기; close=275.73 |
| v2 | cash | 10000.00 | 0.00 | 대기 /  / 새 신호 대기 |
| v2 | buy_hold | 9717.26 | -282.74 | buy / partial / 직전 완료 봉 목표 비중 100%; 다음 봉 시가 가정 |
| v2 | trend_8_26 | 9654.37 | -345.63 | buy / partial / 직전 완료 봉 목표 비중 100%; 다음 봉 시가 가정 |
| v2 | momentum_26 | 9669.12 | -330.88 | buy / partial / 직전 완료 봉 목표 비중 100%; 다음 봉 시가 가정 |
| v2 | breakout_8 | 9406.95 | -593.05 | sell / filled / 직전 완료 봉 목표 비중 0%; 다음 봉 시가 가정 |
| v2 | reversion_12 | 9346.62 | -653.38 | buy / partial / 직전 완료 봉 목표 비중 100%; 다음 봉 시가 가정 |
| v2 | volume_26 | 9378.42 | -621.58 | sell / filled / 직전 완료 봉 목표 비중 0%; 다음 봉 시가 가정 |
| v2 | trend_8_26 AND momentum_26 | 9818.19 | -181.81 | buy / partial / 직전 완료 봉 목표 비중 100%; 다음 봉 시가 가정 |
| v2 | trend_8_26 + momentum_26 | 9682.18 | -317.82 | buy / partial / 직전 완료 봉 목표 비중 100%; 다음 봉 시가 가정 |
| v2 | trend_8_26 AND breakout_8 | 9806.54 | -193.46 | sell / filled / 직전 완료 봉 목표 비중 0%; 다음 봉 시가 가정 |
| v2 | trend_8_26 + breakout_8 | 9550.00 | -450.00 | sell / filled / 직전 완료 봉 목표 비중 50%; 다음 봉 시가 가정 |
| v2 | trend_8_26 AND reversion_12 | 9727.02 | -272.98 | buy / partial / 직전 완료 봉 목표 비중 100%; 다음 봉 시가 가정 |
| v2 | trend_8_26 + reversion_12 | 9499.02 | -500.98 | buy / partial / 직전 완료 봉 목표 비중 100%; 다음 봉 시가 가정 |
| v2 | trend_8_26 AND volume_26 | 9797.73 | -202.27 | sell / filled / 직전 완료 봉 목표 비중 0%; 다음 봉 시가 가정 |
| v2 | trend_8_26 + volume_26 | 9535.29 | -464.71 | sell / filled / 직전 완료 봉 목표 비중 50%; 다음 봉 시가 가정 |
| v2 | momentum_26 AND breakout_8 | 9733.71 | -266.29 | sell / filled / 직전 완료 봉 목표 비중 0%; 다음 봉 시가 가정 |
| v2 | momentum_26 + breakout_8 | 9557.16 | -442.84 | sell / filled / 직전 완료 봉 목표 비중 50%; 다음 봉 시가 가정 |
| v2 | momentum_26 AND reversion_12 | 9903.34 | -96.66 | buy / partial / 직전 완료 봉 목표 비중 100%; 다음 봉 시가 가정 |
| v2 | momentum_26 + reversion_12 | 9546.05 | -453.95 | buy / partial / 직전 완료 봉 목표 비중 100%; 다음 봉 시가 가정 |
| v2 | momentum_26 AND volume_26 | 9897.79 | -102.21 | sell / filled / 직전 완료 봉 목표 비중 0%; 다음 봉 시가 가정 |
| v2 | momentum_26 + volume_26 | 9522.37 | -477.63 | sell / filled / 직전 완료 봉 목표 비중 50%; 다음 봉 시가 가정 |
| v2 | breakout_8 AND reversion_12 | 10000.00 | 0.00 | 대기 /  / 새 신호 대기 |
| v2 | breakout_8 + reversion_12 | 9415.68 | -584.32 | sell / filled / 직전 완료 봉 목표 비중 50%; 다음 봉 시가 가정 |
| v2 | breakout_8 AND volume_26 | 9690.16 | -309.84 | sell / filled / 직전 완료 봉 목표 비중 0%; 다음 봉 시가 가정 |
| v2 | breakout_8 + volume_26 | 9412.30 | -587.70 | sell / filled / 직전 완료 봉 목표 비중 0%; 다음 봉 시가 가정 |
| v2 | reversion_12 AND volume_26 | 9676.46 | -323.54 | sell / filled / 직전 완료 봉 목표 비중 0%; 다음 봉 시가 가정 |
| v2 | reversion_12 + volume_26 | 9401.63 | -598.37 | sell / filled / 직전 완료 봉 목표 비중 50%; 다음 봉 시가 가정 |
| v2 | ema_12_26 | 9761.79 | -238.21 | sell / filled / EMA12 > EMA26; 조건 미충족; EMA12=271.688, EMA26=271.689; 직전 완료 봉 목표를 다음 봉 시가에 모의 적용 |
| v2 | macd_12_26_9 | 9839.63 | -160.37 | sell / filled / MACD > 신호선 그리고 MACD > 0; 조건 미충족; MACD=-0.000914046, signal9=-0.103888; 직전 완료 봉 목표를 다음 봉 시가에 모의 적용 |
| v2 | rsi_14_recovery | 9779.12 | -220.88 | sell / filled / 직전 RSI14 < 30, 현재 RSI14 >= 30 (한 봉 목표); 조건 미충족; RSI14=46.986, previous_RSI14=37.1649; 직전 완료 봉 목표를 다음 봉 시가에 모의 적용 |
| v2 | bollinger_20_reentry | 9920.06 | -79.94 | sell / filled / 직전 종가 < 직전 하단밴드, 현재 하단밴드 <= 종가 <= SMA20 (한 봉 목표); 조건 미충족; close=271.19, lower20=270.018, SMA20=273.224, previous_lower20=270.283; 직전 완료 봉 목표를 다음 봉 시가에 모의 적용 |
| v2 | donchian_20 | 9927.39 | -72.61 | sell / filled / 종가 > 현재 봉을 제외한 직전 20봉 최고가; 조건 미충족; close=274.88, prior_high20=275.91; 직전 완료 봉 목표를 다음 봉 시가에 모의 적용 |
| v2 | atr_14_breakout | 9892.50 | -107.50 | sell / filled / 종가 > 직전 종가 + 직전 ATR14 그리고 종가 > EMA26; 조건 미충족; close=272.33, threshold=272.867, prior_ATR14=0.716592, EMA26=271.567; 직전 완료 봉 목표를 다음 봉 시가에 모의 적용 |
| v2 | session_vwap | 9806.97 | -193.03 | sell / filled / 종가 > 뉴욕 거래일별 누적 전형가격 VWAP; 조건 미충족; close=271.41, session_VWAP=271.719, session_volume=1.03316e+07; 직전 완료 봉 목표를 다음 봉 시가에 모의 적용 |
| v2 | obv_20 | 9798.41 | -201.59 | sell / filled / OBV > OBV의 SMA20 그리고 종가 > EMA26; 조건 미충족; OBV=-4.38074e+07, OBV_SMA20=-4.40508e+07, close=271.41, EMA26=271.689; 직전 완료 봉 목표를 다음 봉 시가에 모의 적용 |
| v2 | stochastic_14_3_recovery | 9717.85 | -282.15 | sell / filled / 직전 %K14 < 20에서 %K14가 %D3 상향 돌파 (한 봉 목표); 조건 미충족; K14=51.9268, D3=28.8672, previous_K14=30.3264, previous_D3=23.1523; 직전 완료 봉 목표를 다음 봉 시가에 모의 적용 |
| v2 | mfi_14_recovery | 9960.66 | -39.34 | sell / filled / 직전 MFI14 < 20, 현재 MFI14 >= 20 (한 봉 목표); 조건 미충족; MFI14=33.2861, previous_MFI14=27.7983; 직전 완료 봉 목표를 다음 봉 시가에 모의 적용 |
| v2 | adx_14_trend | 9836.12 | -163.88 | sell / filled / Wilder ADX14 >= 25 그리고 +DI14 > -DI14; 조건 미충족; ADX14=23.881, plus_DI14=25.6616, minus_DI14=25.2483; 직전 완료 봉 목표를 다음 봉 시가에 모의 적용 |
| v2 | aroon_25_trend | 9818.09 | -181.91 | sell / filled / Aroon25 Up > 70 그리고 Down < 30 (동률이면 최신 극값); 조건 미충족; Aroon_up=68, Aroon_down=20; 직전 완료 봉 목표를 다음 봉 시가에 모의 적용 |
| v2 | cci_20_momentum | 9875.60 | -124.40 | sell / filled / CCI20 > 100 (전형가격·평균절대편차); 조건 미충족; CCI20=81.8699; 직전 완료 봉 목표를 다음 봉 시가에 모의 적용 |
| v2 | williams_14_recovery | 9899.94 | -100.06 | sell / filled / 직전 Williams %R14 < -80, 현재 >= -80 (한 봉 목표); 조건 미충족; Williams_R14=-48.0732, previous_R14=-69.6736; 직전 완료 봉 목표를 다음 봉 시가에 모의 적용 |
| v2 | cmf_20_accumulation | 9791.28 | -208.72 | sell / filled / Chaikin Money Flow20 > 0.1; 조건 미충족; CMF20=0.0512251, volume20=2.08469e+07; 직전 완료 봉 목표를 다음 봉 시가에 모의 적용 |
| v2 | chaikin_3_10 | 9799.29 | -200.71 | sell / filled / ADL의 EMA3 - EMA10 > 0 그리고 종가 > EMA26; 조건 미충족; Chaikin3_10=-9609.69, ADL=-6.08839e+07, close=271.41, EMA26=271.689; 직전 완료 봉 목표를 다음 봉 시가에 모의 적용 |
| v2 | roc_10_momentum | 10000.00 | 0.00 | 대기 /  / 새 신호 대기 |
| v2 | trix_15_trend | 9893.75 | -106.25 | sell / filled / 15봉 삼중 EMA의 1봉 변화율 TRIX > 0 그리고 종가 > EMA26; 조건 미충족; TRIX15_percent=0.0257204, close=273.74, EMA26=273.991; 직전 완료 봉 목표를 다음 봉 시가에 모의 적용 |
| v2 | keltner_20_breakout | 9935.32 | -64.68 | sell / filled / 종가 > EMA20 + 2 x Wilder ATR14; 조건 미충족; close=274.88, upper_Keltner=275.161, EMA20=274.044, ATR14=0.558498; 직전 완료 봉 목표를 다음 봉 시가에 모의 적용 |
| v2 | opening_range_30m | 9966.04 | -33.96 | sell / filled / 뉴욕 09:30·09:45 두 완료 봉 최고가를 10:00 이후 종가가 돌파; 자료 부족·변동폭 또는 거래량 없음: 대기; close=275.73; 직전 완료 봉 목표를 다음 봉 시가에 모의 적용 |

### 같은 기간의 비용·노출 비교 (사후 연구)

| 전략 | 비용 전 | 비용 후 | 100% 보유 | 같은 평균 노출 보유 | 평균 노출 |
|---|---:|---:|---:|---:|---:|
| cash | 0.00% | 0.00% | -3.72% | -0.00% | 0.00% |
| buy_hold | -3.31% | -3.72% | -3.72% | -3.72% | 100.00% |
| trend_8_26 | -1.72% | -5.36% | -3.72% | -1.65% | 43.98% |
| momentum_26 | -2.67% | -8.61% | -3.72% | -1.47% | 39.27% |
| breakout_8 | -0.55% | -13.78% | -3.72% | -0.75% | 19.90% |
| reversion_12 | -2.49% | -15.11% | -3.72% | -1.14% | 30.37% |
| volume_26 | -2.89% | -9.96% | -3.72% | -0.32% | 8.38% |
| trend_8_26 AND momentum_26 | -1.55% | -5.99% | -3.72% | -1.29% | 34.29% |
| trend_8_26 + momentum_26 | -2.19% | -6.60% | -3.72% | -1.56% | 41.63% |
| trend_8_26 AND breakout_8 | -0.38% | -8.02% | -3.72% | -0.43% | 11.52% |
| trend_8_26 + breakout_8 | -1.13% | -9.48% | -3.72% | -1.20% | 31.94% |
| trend_8_26 AND reversion_12 | -0.82% | -5.30% | -3.72% | -0.21% | 5.50% |
| trend_8_26 + reversion_12 | -2.10% | -10.19% | -3.72% | -1.39% | 37.18% |
| trend_8_26 AND volume_26 | -1.27% | -4.53% | -3.72% | -0.11% | 2.88% |
| trend_8_26 + volume_26 | -2.30% | -7.50% | -3.72% | -0.98% | 26.18% |
| momentum_26 AND breakout_8 | -0.21% | -7.48% | -3.72% | -0.38% | 10.21% |
| momentum_26 + breakout_8 | -1.61% | -11.05% | -3.72% | -1.11% | 29.59% |
| momentum_26 AND reversion_12 | 0.05% | -3.67% | -3.72% | -0.12% | 3.14% |
| momentum_26 + reversion_12 | -2.57% | -10.81% | -3.72% | -1.30% | 34.82% |
| momentum_26 AND volume_26 | -1.25% | -3.30% | -3.72% | -0.06% | 1.57% |
| momentum_26 + volume_26 | -2.78% | -8.91% | -3.72% | -0.89% | 23.83% |
| breakout_8 AND reversion_12 | 0.00% | 0.00% | -3.72% | -0.00% | 0.00% |
| breakout_8 + reversion_12 | -1.52% | -13.74% | -3.72% | -0.94% | 25.14% |
| breakout_8 AND volume_26 | -1.46% | -4.31% | -3.72% | -0.09% | 2.36% |
| breakout_8 + volume_26 | -1.72% | -11.71% | -3.72% | -0.53% | 14.14% |
| reversion_12 AND volume_26 | -0.62% | -4.31% | -3.72% | -0.15% | 3.93% |
| reversion_12 + volume_26 | -2.69% | -11.85% | -3.72% | -0.73% | 19.38% |
| ema_12_26 | -0.23% | -2.71% | -3.72% | -1.61% | 42.93% |
| macd_12_26_9 | 1.54% | -0.99% | -3.72% | -1.04% | 27.75% |
| rsi_14_recovery | -0.86% | -6.52% | -3.72% | -0.14% | 3.66% |
| bollinger_20_reentry | -0.31% | -4.81% | -3.72% | -0.11% | 2.88% |
| donchian_20 | -0.20% | -5.10% | -3.72% | -0.21% | 5.50% |
| atr_14_breakout | -1.18% | -7.22% | -3.72% | -0.15% | 3.93% |
| session_vwap | -0.85% | -9.98% | -3.72% | -1.48% | 39.53% |
| obv_20 | 0.29% | -3.43% | -3.72% | -1.42% | 37.96% |
| stochastic_14_3_recovery | -1.20% | -15.06% | -3.72% | -0.35% | 9.42% |
| mfi_14_recovery | 0.24% | -3.88% | -3.72% | -0.10% | 2.62% |
| adx_14_trend | 0.00% | -3.30% | -3.72% | -1.16% | 30.89% |
| aroon_25_trend | -1.71% | -5.36% | -3.72% | -0.79% | 20.94% |
| cci_20_momentum | -2.04% | -8.41% | -3.72% | -0.69% | 18.32% |
| williams_14_recovery | -0.58% | -10.11% | -3.72% | -0.24% | 6.28% |
| cmf_20_accumulation | -1.81% | -7.80% | -3.72% | -0.66% | 17.54% |
| chaikin_3_10 | -1.82% | -7.82% | -3.72% | -1.16% | 30.89% |
| roc_10_momentum | -0.63% | -1.87% | -3.72% | -0.12% | 3.14% |
| trix_15_trend | 0.35% | -2.56% | -3.72% | -1.17% | 31.15% |
| keltner_20_breakout | -0.91% | -4.18% | -3.72% | -0.20% | 5.24% |
| opening_range_30m | 2.57% | -1.23% | -3.72% | -0.80% | 21.20% |

동일 구간·초기 자금, 종료 시 청산 비용 포함. 노출 맞춤은 사후 설명용이며 v2 실제 계좌 성과가 아닙니다.
[낙폭 분해·비용 영향·전체 구간](IWM/comparison.json)

[v1 전체 기록](IWM/accounts.json) · [v2 전체 기록](IWM/accounts-v2.json)

## DIA 계좌

| 모델 | 전략 | 평가액 USD | 손익 USD | 최근 매매·이유 |
|---|---|---:|---:|---|
| v1 | cash | 10000.00 | 0.00 | 대기 /  / 새 신호 대기 |
| v1 | buy_hold | 9919.43 | -80.57 | buy /  / buy_hold: prior completed bar target 100%; next bar open simulation |
| v1 | trend_8_26 | 9878.12 | -121.88 | buy /  / trend_8_26: prior completed bar target 100%; next bar open simulation |
| v1 | momentum_26 | 9858.40 | -141.60 | buy /  / momentum_26: prior completed bar target 100%; next bar open simulation |
| v1 | breakout_8 | 9806.43 | -193.57 | sell /  / breakout_8: prior completed bar target 0%; next bar open simulation |
| v1 | reversion_12 | 9892.53 | -107.47 | sell /  / reversion_12: prior completed bar target 0%; next bar open simulation |
| v1 | volume_26 | 9908.95 | -91.05 | sell /  / volume_26: prior completed bar target 0%; next bar open simulation |
| v1 | trend_8_26 AND momentum_26 | 9858.40 | -141.60 | buy /  / trend_8_26 AND momentum_26: prior completed bar target 100%; next bar open simulation |
| v1 | trend_8_26 + momentum_26 | 9868.25 | -131.75 | buy /  / trend_8_26 + momentum_26: prior completed bar target 100%; next bar open simulation |
| v1 | trend_8_26 AND breakout_8 | 9940.12 | -59.88 | sell /  / trend_8_26 AND breakout_8: prior completed bar target 0%; next bar open simulation |
| v1 | trend_8_26 + breakout_8 | 9861.84 | -138.16 | sell /  / trend_8_26 + breakout_8: prior completed bar target 50%; next bar open simulation |
| v1 | trend_8_26 AND reversion_12 | 9936.00 | -64.00 | sell /  / trend_8_26 AND reversion_12: prior completed bar target 0%; next bar open simulation |
| v1 | trend_8_26 + reversion_12 | 9885.20 | -114.80 | sell /  / trend_8_26 + reversion_12: prior completed bar target 50%; next bar open simulation |
| v1 | trend_8_26 AND volume_26 | 9943.10 | -56.90 | sell /  / trend_8_26 AND volume_26: prior completed bar target 0%; next bar open simulation |
| v1 | trend_8_26 + volume_26 | 9893.42 | -106.58 | sell /  / trend_8_26 + volume_26: prior completed bar target 50%; next bar open simulation |
| v1 | momentum_26 AND breakout_8 | 9940.12 | -59.88 | sell /  / momentum_26 AND breakout_8: prior completed bar target 0%; next bar open simulation |
| v1 | momentum_26 + breakout_8 | 9832.29 | -167.71 | buy /  / momentum_26 + breakout_8: prior completed bar target 50%; next bar open simulation |
| v1 | momentum_26 AND reversion_12 | 9940.78 | -59.22 | sell /  / momentum_26 AND reversion_12: prior completed bar target 0%; next bar open simulation |
| v1 | momentum_26 + reversion_12 | 9875.33 | -124.67 | buy /  / momentum_26 + reversion_12: prior completed bar target 50%; next bar open simulation |
| v1 | momentum_26 AND volume_26 | 9943.10 | -56.90 | sell /  / momentum_26 AND volume_26: prior completed bar target 0%; next bar open simulation |
| v1 | momentum_26 + volume_26 | 9883.55 | -116.45 | buy /  / momentum_26 + volume_26: prior completed bar target 50%; next bar open simulation |
| v1 | breakout_8 AND reversion_12 | 10000.00 | 0.00 | 대기 /  / 새 신호 대기 |
| v1 | breakout_8 + reversion_12 | 9849.27 | -150.73 | sell /  / breakout_8 + reversion_12: prior completed bar target 0%; next bar open simulation |
| v1 | breakout_8 AND volume_26 | 10000.00 | 0.00 | 대기 /  / 새 신호 대기 |
| v1 | breakout_8 + volume_26 | 9857.47 | -142.53 | sell /  / breakout_8 + volume_26: prior completed bar target 0%; next bar open simulation |
| v1 | reversion_12 AND volume_26 | 9965.65 | -34.35 | sell /  / reversion_12 AND volume_26: prior completed bar target 0%; next bar open simulation |
| v1 | reversion_12 + volume_26 | 9920.50 | -79.50 | sell /  / reversion_12 + volume_26: prior completed bar target 0%; next bar open simulation |
| v1 | ema_12_26 | 9876.07 | -123.93 | sell /  / EMA12 > EMA26; 조건 미충족; EMA12=520.874, EMA26=520.918 |
| v1 | macd_12_26_9 | 9941.64 | -58.36 | sell /  / MACD > 신호선 그리고 MACD > 0; 조건 미충족; MACD=1.23542, signal9=1.25143 |
| v1 | rsi_14_recovery | 10000.00 | 0.00 | 대기 /  / 새 신호 대기 |
| v1 | bollinger_20_reentry | 9978.51 | -21.49 | sell /  / 직전 종가 < 직전 하단밴드, 현재 하단밴드 <= 종가 <= SMA20 (한 봉 목표); 조건 미충족; close=519.823, lower20=518.355, SMA20=521.612, previous_lower20=518.548 |
| v1 | donchian_20 | 9895.87 | -104.13 | sell /  / 종가 > 현재 봉을 제외한 직전 20봉 최고가; 조건 미충족; close=520.09, prior_high20=520.519 |
| v1 | atr_14_breakout | 9925.94 | -74.06 | sell /  / 종가 > 직전 종가 + 직전 ATR14 그리고 종가 > EMA26; 조건 미충족; close=519.24, threshold=520.599, prior_ATR14=0.989436, EMA26=519.399 |
| v1 | session_vwap | 9913.57 | -86.43 | buy /  / 종가 > 뉴욕 거래일별 누적 전형가격 VWAP; 조건 충족; close=519.01, session_VWAP=518.623, session_volume=840642 |
| v1 | obv_20 | 9864.89 | -135.11 | buy /  / OBV > OBV의 SMA20 그리고 종가 > EMA26; 조건 충족; OBV=-9.67274e+06, OBV_SMA20=-9.77214e+06, close=519.4, EMA26=519.374 |
| v1 | stochastic_14_3_recovery | 9821.75 | -178.25 | sell /  / 직전 %K14 < 20에서 %K14가 %D3 상향 돌파 (한 봉 목표); 조건 미충족; K14=21.4008, D3=27.0401, previous_K14=46.6025, previous_D3=27.3524 |
| v1 | mfi_14_recovery | 9936.38 | -63.62 | sell /  / 직전 MFI14 < 20, 현재 MFI14 >= 20 (한 봉 목표); 조건 미충족; MFI14=44.8014, previous_MFI14=20.0271 |
| v1 | adx_14_trend | 9882.74 | -117.26 | sell /  / Wilder ADX14 >= 25 그리고 +DI14 > -DI14; 조건 미충족; ADX14=30.2264, plus_DI14=23.4608, minus_DI14=27.9688 |
| v1 | aroon_25_trend | 9886.35 | -113.65 | sell /  / Aroon25 Up > 70 그리고 Down < 30 (동률이면 최신 극값); 조건 미충족; Aroon_up=68, Aroon_down=20 |
| v1 | cci_20_momentum | 9910.36 | -89.64 | sell /  / CCI20 > 100 (전형가격·평균절대편차); 조건 미충족; CCI20=46.8763 |
| v1 | williams_14_recovery | 9855.05 | -144.95 | sell /  / 직전 Williams %R14 < -80, 현재 >= -80 (한 봉 목표); 조건 미충족; Williams_R14=-78.5992, previous_R14=-53.3975 |
| v1 | cmf_20_accumulation | 9873.15 | -126.85 | sell /  / Chaikin Money Flow20 > 0.1; 조건 미충족; CMF20=0.0708768, volume20=2.29062e+06 |
| v1 | chaikin_3_10 | 9866.81 | -133.19 | buy /  / ADL의 EMA3 - EMA10 > 0 그리고 종가 > EMA26; 조건 충족; Chaikin3_10=42268.1, ADL=-1.72367e+07, close=519.4, EMA26=519.374 |
| v1 | roc_10_momentum | 10000.00 | 0.00 | 대기 /  / 새 신호 대기 |
| v1 | trix_15_trend | 9928.27 | -71.73 | sell /  / 15봉 삼중 EMA의 1봉 변화율 TRIX > 0 그리고 종가 > EMA26; 조건 미충족; TRIX15_percent=0.0322153, close=521.26, EMA26=521.365 |
| v1 | keltner_20_breakout | 9940.12 | -59.88 | sell /  / 종가 > EMA20 + 2 x Wilder ATR14; 조건 미충족; close=522.89, upper_Keltner=523.089, EMA20=521.145, ATR14=0.971947 |
| v1 | opening_range_30m | 9862.07 | -137.93 | buy /  / 뉴욕 09:30·09:45 두 완료 봉 최고가를 10:00 이후 종가가 돌파; 조건 충족; close=519.165, opening_high=519.1 |
| v2 | cash | 10000.00 | 0.00 | 대기 /  / 새 신호 대기 |
| v2 | buy_hold | 10042.32 | 42.32 | buy / partial / 직전 완료 봉 목표 비중 100%; 다음 봉 시가 가정 |
| v2 | trend_8_26 | 9812.16 | -187.84 | buy / partial / 직전 완료 봉 목표 비중 100%; 다음 봉 시가 가정 |
| v2 | momentum_26 | 9898.26 | -101.74 | buy / partial / 직전 완료 봉 목표 비중 100%; 다음 봉 시가 가정 |
| v2 | breakout_8 | 9333.71 | -666.29 | sell / filled / 직전 완료 봉 목표 비중 0%; 다음 봉 시가 가정 |
| v2 | reversion_12 | 9589.97 | -410.03 | sell / filled / 직전 완료 봉 목표 비중 0%; 다음 봉 시가 가정 |
| v2 | volume_26 | 9625.87 | -374.13 | sell / filled / 직전 완료 봉 목표 비중 0%; 다음 봉 시가 가정 |
| v2 | trend_8_26 AND momentum_26 | 9893.67 | -106.33 | buy / partial / 직전 완료 봉 목표 비중 100%; 다음 봉 시가 가정 |
| v2 | trend_8_26 + momentum_26 | 9855.18 | -144.82 | buy / partial / 직전 완료 봉 목표 비중 100%; 다음 봉 시가 가정 |
| v2 | trend_8_26 AND breakout_8 | 9626.81 | -373.19 | sell / filled / 직전 완료 봉 목표 비중 0%; 다음 봉 시가 가정 |
| v2 | trend_8_26 + breakout_8 | 9590.06 | -409.94 | sell / filled / 직전 완료 봉 목표 비중 50%; 다음 봉 시가 가정 |
| v2 | trend_8_26 AND reversion_12 | 9746.03 | -253.97 | sell / filled / 직전 완료 봉 목표 비중 0%; 다음 봉 시가 가정 |
| v2 | trend_8_26 + reversion_12 | 9700.06 | -299.94 | sell / filled / 직전 완료 봉 목표 비중 50%; 다음 봉 시가 가정 |
| v2 | trend_8_26 AND volume_26 | 9800.82 | -199.18 | sell / filled / 직전 완료 봉 목표 비중 0%; 다음 봉 시가 가정 |
| v2 | trend_8_26 + volume_26 | 9738.85 | -261.15 | sell / filled / 직전 완료 봉 목표 비중 50%; 다음 봉 시가 가정 |
| v2 | momentum_26 AND breakout_8 | 9615.85 | -384.15 | sell / filled / 직전 완료 봉 목표 비중 0%; 다음 봉 시가 가정 |
| v2 | momentum_26 + breakout_8 | 9611.88 | -388.12 | buy / filled / 직전 완료 봉 목표 비중 50%; 다음 봉 시가 가정 |
| v2 | momentum_26 AND reversion_12 | 9895.03 | -104.97 | sell / filled / 직전 완료 봉 목표 비중 0%; 다음 봉 시가 가정 |
| v2 | momentum_26 + reversion_12 | 9742.59 | -257.41 | buy / filled / 직전 완료 봉 목표 비중 50%; 다음 봉 시가 가정 |
| v2 | momentum_26 AND volume_26 | 9733.77 | -266.23 | sell / filled / 직전 완료 봉 목표 비중 0%; 다음 봉 시가 가정 |
| v2 | momentum_26 + volume_26 | 9802.19 | -197.81 | buy / filled / 직전 완료 봉 목표 비중 50%; 다음 봉 시가 가정 |
| v2 | breakout_8 AND reversion_12 | 10000.00 | 0.00 | 대기 /  / 새 신호 대기 |
| v2 | breakout_8 + reversion_12 | 9460.42 | -539.58 | sell / filled / 직전 완료 봉 목표 비중 0%; 다음 봉 시가 가정 |
| v2 | breakout_8 AND volume_26 | 9796.56 | -203.44 | sell / filled / 직전 완료 봉 목표 비중 0%; 다음 봉 시가 가정 |
| v2 | breakout_8 + volume_26 | 9478.43 | -521.57 | sell / filled / 직전 완료 봉 목표 비중 0%; 다음 봉 시가 가정 |
| v2 | reversion_12 AND volume_26 | 9963.66 | -36.34 | sell / filled / 직전 완료 봉 목표 비중 0%; 다음 봉 시가 가정 |
| v2 | reversion_12 + volume_26 | 9627.77 | -372.23 | sell / filled / 직전 완료 봉 목표 비중 0%; 다음 봉 시가 가정 |
| v2 | ema_12_26 | 9874.10 | -125.90 | sell / filled / EMA12 > EMA26; 조건 미충족; EMA12=520.874, EMA26=520.918; 직전 완료 봉 목표를 다음 봉 시가에 모의 적용 |
| v2 | macd_12_26_9 | 9939.65 | -60.35 | sell / filled / MACD > 신호선 그리고 MACD > 0; 조건 미충족; MACD=1.23542, signal9=1.25143; 직전 완료 봉 목표를 다음 봉 시가에 모의 적용 |
| v2 | rsi_14_recovery | 10000.00 | 0.00 | 대기 /  / 새 신호 대기 |
| v2 | bollinger_20_reentry | 9976.52 | -23.48 | sell / filled / 직전 종가 < 직전 하단밴드, 현재 하단밴드 <= 종가 <= SMA20 (한 봉 목표); 조건 미충족; close=519.823, lower20=518.355, SMA20=521.612, previous_lower20=518.548; 직전 완료 봉 목표를 다음 봉 시가에 모의 적용 |
| v2 | donchian_20 | 9891.91 | -108.09 | sell / filled / 종가 > 현재 봉을 제외한 직전 20봉 최고가; 조건 미충족; close=520.09, prior_high20=520.519; 직전 완료 봉 목표를 다음 봉 시가에 모의 적용 |
| v2 | atr_14_breakout | 9921.97 | -78.03 | sell / filled / 종가 > 직전 종가 + 직전 ATR14 그리고 종가 > EMA26; 조건 미충족; close=519.24, threshold=520.599, prior_ATR14=0.989436, EMA26=519.399; 직전 완료 봉 목표를 다음 봉 시가에 모의 적용 |
| v2 | session_vwap | 9908.61 | -91.39 | buy / partial / 종가 > 뉴욕 거래일별 누적 전형가격 VWAP; 조건 충족; close=519.01, session_VWAP=518.623, session_volume=840642; 직전 완료 봉 목표를 다음 봉 시가에 모의 적용 |
| v2 | obv_20 | 9859.96 | -140.04 | buy / partial / OBV > OBV의 SMA20 그리고 종가 > EMA26; 조건 충족; OBV=-9.67274e+06, OBV_SMA20=-9.77214e+06, close=519.4, EMA26=519.374; 직전 완료 봉 목표를 다음 봉 시가에 모의 적용 |
| v2 | stochastic_14_3_recovery | 9813.90 | -186.10 | sell / filled / 직전 %K14 < 20에서 %K14가 %D3 상향 돌파 (한 봉 목표); 조건 미충족; K14=21.4008, D3=27.0401, previous_K14=46.6025, previous_D3=27.3524; 직전 완료 봉 목표를 다음 봉 시가에 모의 적용 |
| v2 | mfi_14_recovery | 9932.40 | -67.60 | sell / filled / 직전 MFI14 < 20, 현재 MFI14 >= 20 (한 봉 목표); 조건 미충족; MFI14=44.8014, previous_MFI14=20.0271; 직전 완료 봉 목표를 다음 봉 시가에 모의 적용 |
| v2 | adx_14_trend | 9878.79 | -121.21 | sell / filled / Wilder ADX14 >= 25 그리고 +DI14 > -DI14; 조건 미충족; ADX14=30.2264, plus_DI14=23.4608, minus_DI14=27.9688; 직전 완료 봉 목표를 다음 봉 시가에 모의 적용 |
| v2 | aroon_25_trend | 9882.39 | -117.61 | sell / filled / Aroon25 Up > 70 그리고 Down < 30 (동률이면 최신 극값); 조건 미충족; Aroon_up=68, Aroon_down=20; 직전 완료 봉 목표를 다음 봉 시가에 모의 적용 |
| v2 | cci_20_momentum | 9906.40 | -93.60 | sell / filled / CCI20 > 100 (전형가격·평균절대편차); 조건 미충족; CCI20=46.8763; 직전 완료 봉 목표를 다음 봉 시가에 모의 적용 |
| v2 | williams_14_recovery | 9849.14 | -150.86 | sell / filled / 직전 Williams %R14 < -80, 현재 >= -80 (한 봉 목표); 조건 미충족; Williams_R14=-78.5992, previous_R14=-53.3975; 직전 완료 봉 목표를 다음 봉 시가에 모의 적용 |
| v2 | cmf_20_accumulation | 9869.20 | -130.80 | sell / filled / Chaikin Money Flow20 > 0.1; 조건 미충족; CMF20=0.0708768, volume20=2.29062e+06; 직전 완료 봉 목표를 다음 봉 시가에 모의 적용 |
| v2 | chaikin_3_10 | 9861.87 | -138.13 | buy / partial / ADL의 EMA3 - EMA10 > 0 그리고 종가 > EMA26; 조건 충족; Chaikin3_10=42268.1, ADL=-1.72367e+07, close=519.4, EMA26=519.374; 직전 완료 봉 목표를 다음 봉 시가에 모의 적용 |
| v2 | roc_10_momentum | 10000.00 | 0.00 | 대기 /  / 새 신호 대기 |
| v2 | trix_15_trend | 9926.28 | -73.72 | sell / filled / 15봉 삼중 EMA의 1봉 변화율 TRIX > 0 그리고 종가 > EMA26; 조건 미충족; TRIX15_percent=0.0322153, close=521.26, EMA26=521.365; 직전 완료 봉 목표를 다음 봉 시가에 모의 적용 |
| v2 | keltner_20_breakout | 9938.13 | -61.87 | sell / filled / 종가 > EMA20 + 2 x Wilder ATR14; 조건 미충족; close=522.89, upper_Keltner=523.089, EMA20=521.145, ATR14=0.971947; 직전 완료 봉 목표를 다음 봉 시가에 모의 적용 |
| v2 | opening_range_30m | 9855.17 | -144.83 | buy / partial / 뉴욕 09:30·09:45 두 완료 봉 최고가를 10:00 이후 종가가 돌파; 조건 충족; close=519.165, opening_high=519.1; 직전 완료 봉 목표를 다음 봉 시가에 모의 적용 |

### 같은 기간의 비용·노출 비교 (사후 연구)

| 전략 | 비용 전 | 비용 후 | 100% 보유 | 같은 평균 노출 보유 | 평균 노출 |
|---|---:|---:|---:|---:|---:|
| cash | 0.00% | 0.00% | 0.79% | 0.00% | 0.00% |
| buy_hold | 1.21% | 0.79% | 0.79% | 0.79% | 100.00% |
| trend_8_26 | 1.37% | -2.39% | 0.79% | 0.44% | 56.02% |
| momentum_26 | 0.39% | -3.74% | 0.79% | 0.40% | 50.79% |
| breakout_8 | 0.79% | -16.21% | 0.79% | 0.18% | 23.04% |
| reversion_12 | -1.49% | -9.43% | 0.79% | 0.20% | 24.87% |
| volume_26 | -0.85% | -10.74% | 0.79% | 0.08% | 10.21% |
| trend_8_26 AND momentum_26 | 1.50% | -2.67% | 0.79% | 0.36% | 45.55% |
| trend_8_26 + momentum_26 | 0.88% | -3.07% | 0.79% | 0.42% | 53.41% |
| trend_8_26 AND breakout_8 | 1.06% | -10.53% | 0.79% | 0.12% | 14.66% |
| trend_8_26 + breakout_8 | 1.08% | -9.19% | 0.79% | 0.31% | 39.54% |
| trend_8_26 AND reversion_12 | -0.02% | -4.93% | 0.79% | 0.05% | 6.54% |
| trend_8_26 + reversion_12 | -0.07% | -5.79% | 0.79% | 0.32% | 40.45% |
| trend_8_26 AND volume_26 | 0.36% | -4.57% | 0.79% | 0.04% | 4.71% |
| trend_8_26 + volume_26 | 0.25% | -6.47% | 0.79% | 0.26% | 33.12% |
| momentum_26 AND breakout_8 | 0.26% | -10.87% | 0.79% | 0.12% | 14.92% |
| momentum_26 + breakout_8 | 0.60% | -10.00% | 0.79% | 0.29% | 36.92% |
| momentum_26 AND reversion_12 | -0.27% | -3.57% | 0.79% | 0.05% | 5.76% |
| momentum_26 + reversion_12 | -0.55% | -6.04% | 0.79% | 0.30% | 37.83% |
| momentum_26 AND volume_26 | -0.56% | -5.45% | 0.79% | 0.04% | 4.45% |
| momentum_26 + volume_26 | -0.23% | -6.72% | 0.79% | 0.24% | 30.50% |
| breakout_8 AND reversion_12 | 0.00% | 0.00% | 0.79% | 0.00% | 0.00% |
| breakout_8 + reversion_12 | -0.35% | -12.72% | 0.79% | 0.19% | 23.96% |
| breakout_8 AND volume_26 | -0.73% | -3.60% | 0.79% | 0.02% | 2.62% |
| breakout_8 + volume_26 | -0.03% | -12.80% | 0.79% | 0.13% | 16.63% |
| reversion_12 AND volume_26 | -0.12% | -5.03% | 0.79% | 0.03% | 3.66% |
| reversion_12 + volume_26 | -1.17% | -9.90% | 0.79% | 0.14% | 17.54% |
| ema_12_26 | 0.17% | -1.91% | 0.79% | 0.38% | 48.69% |
| macd_12_26_9 | 1.65% | -1.30% | 0.79% | 0.22% | 27.49% |
| rsi_14_recovery | 0.01% | -2.07% | 0.79% | 0.01% | 1.31% |
| bollinger_20_reentry | -0.09% | -5.00% | 0.79% | 0.02% | 3.14% |
| donchian_20 | 0.31% | -6.21% | 0.79% | 0.07% | 8.38% |
| atr_14_breakout | -0.66% | -7.51% | 0.79% | 0.04% | 5.24% |
| session_vwap | 2.20% | -5.64% | 0.79% | 0.39% | 48.95% |
| obv_20 | 0.71% | -7.02% | 0.79% | 0.33% | 41.36% |
| stochastic_14_3_recovery | 0.63% | -12.03% | 0.79% | 0.07% | 8.38% |
| mfi_14_recovery | 0.10% | -3.61% | 0.79% | 0.02% | 2.36% |
| adx_14_trend | 0.20% | -3.52% | 0.79% | 0.26% | 32.46% |
| aroon_25_trend | 0.53% | -2.80% | 0.79% | 0.20% | 25.39% |
| cci_20_momentum | 0.61% | -5.53% | 0.79% | 0.20% | 24.87% |
| williams_14_recovery | 0.97% | -7.55% | 0.79% | 0.04% | 5.50% |
| cmf_20_accumulation | 0.98% | -5.98% | 0.79% | 0.21% | 26.44% |
| chaikin_3_10 | 1.92% | -7.08% | 0.79% | 0.32% | 40.84% |
| roc_10_momentum | 0.15% | -0.27% | 0.79% | 0.01% | 1.31% |
| trix_15_trend | 0.19% | -3.12% | 0.79% | 0.33% | 41.88% |
| keltner_20_breakout | 0.33% | -5.79% | 0.79% | 0.13% | 16.75% |
| opening_range_30m | 1.87% | -3.55% | 0.79% | 0.18% | 22.25% |

동일 구간·초기 자금, 종료 시 청산 비용 포함. 노출 맞춤은 사후 설명용이며 v2 실제 계좌 성과가 아닙니다.
[낙폭 분해·비용 영향·전체 구간](DIA/comparison.json)

[v1 전체 기록](DIA/accounts.json) · [v2 전체 기록](DIA/accounts-v2.json)

## MSFT 계좌

| 모델 | 전략 | 평가액 USD | 손익 USD | 최근 매매·이유 |
|---|---|---:|---:|---|
| v1 | cash | 10000.00 | 0.00 | 대기 /  / 새 신호 대기 |
| v1 | buy_hold | 9850.27 | -149.73 | buy /  / buy_hold: prior completed bar target 100%; next bar open simulation |
| v1 | trend_8_26 | 9832.80 | -167.20 | buy /  / trend_8_26: prior completed bar target 100%; next bar open simulation |
| v1 | momentum_26 | 9803.79 | -196.21 | buy /  / momentum_26: prior completed bar target 100%; next bar open simulation |
| v1 | breakout_8 | 9876.66 | -123.34 | sell /  / breakout_8: prior completed bar target 0%; next bar open simulation |
| v1 | reversion_12 | 9773.75 | -226.25 | sell /  / reversion_12: prior completed bar target 0%; next bar open simulation |
| v1 | volume_26 | 9811.31 | -188.69 | sell /  / volume_26: prior completed bar target 0%; next bar open simulation |
| v1 | trend_8_26 AND momentum_26 | 9818.10 | -181.90 | buy /  / trend_8_26 AND momentum_26: prior completed bar target 100%; next bar open simulation |
| v1 | trend_8_26 + momentum_26 | 9818.30 | -181.70 | buy /  / trend_8_26 + momentum_26: prior completed bar target 100%; next bar open simulation |
| v1 | trend_8_26 AND breakout_8 | 9905.03 | -94.97 | sell /  / trend_8_26 AND breakout_8: prior completed bar target 0%; next bar open simulation |
| v1 | trend_8_26 + breakout_8 | 9874.43 | -125.57 | buy /  / trend_8_26 + breakout_8: prior completed bar target 50%; next bar open simulation |
| v1 | trend_8_26 AND reversion_12 | 9895.34 | -104.66 | sell /  / trend_8_26 AND reversion_12: prior completed bar target 0%; next bar open simulation |
| v1 | trend_8_26 + reversion_12 | 9803.18 | -196.82 | sell /  / trend_8_26 + reversion_12: prior completed bar target 50%; next bar open simulation |
| v1 | trend_8_26 AND volume_26 | 9916.79 | -83.21 | sell /  / trend_8_26 AND volume_26: prior completed bar target 0%; next bar open simulation |
| v1 | trend_8_26 + volume_26 | 9822.00 | -178.00 | buy /  / trend_8_26 + volume_26: prior completed bar target 50%; next bar open simulation |
| v1 | momentum_26 AND breakout_8 | 9905.03 | -94.97 | sell /  / momentum_26 AND breakout_8: prior completed bar target 0%; next bar open simulation |
| v1 | momentum_26 + breakout_8 | 9840.14 | -159.86 | buy /  / momentum_26 + breakout_8: prior completed bar target 50%; next bar open simulation |
| v1 | momentum_26 AND reversion_12 | 9880.92 | -119.08 | sell /  / momentum_26 AND reversion_12: prior completed bar target 0%; next bar open simulation |
| v1 | momentum_26 + reversion_12 | 9788.72 | -211.28 | sell /  / momentum_26 + reversion_12: prior completed bar target 50%; next bar open simulation |
| v1 | momentum_26 AND volume_26 | 9916.79 | -83.21 | sell /  / momentum_26 AND volume_26: prior completed bar target 0%; next bar open simulation |
| v1 | momentum_26 + volume_26 | 9807.51 | -192.49 | buy /  / momentum_26 + volume_26: prior completed bar target 50%; next bar open simulation |
| v1 | breakout_8 AND reversion_12 | 10000.00 | 0.00 | 대기 /  / 새 신호 대기 |
| v1 | breakout_8 + reversion_12 | 9844.65 | -155.35 | sell /  / breakout_8 + reversion_12: prior completed bar target 0%; next bar open simulation |
| v1 | breakout_8 AND volume_26 | 9953.19 | -46.81 | sell /  / breakout_8 AND volume_26: prior completed bar target 0%; next bar open simulation |
| v1 | breakout_8 + volume_26 | 9863.58 | -136.42 | sell /  / breakout_8 + volume_26: prior completed bar target 0%; next bar open simulation |
| v1 | reversion_12 AND volume_26 | 9938.00 | -62.00 | sell /  / reversion_12 AND volume_26: prior completed bar target 0%; next bar open simulation |
| v1 | reversion_12 + volume_26 | 9792.40 | -207.60 | sell /  / reversion_12 + volume_26: prior completed bar target 0%; next bar open simulation |
| v1 | ema_12_26 | 9818.10 | -181.90 | buy /  / EMA12 > EMA26; 조건 충족; EMA12=531.372, EMA26=531.07 |
| v1 | macd_12_26_9 | 9854.23 | -145.77 | buy /  / MACD > 신호선 그리고 MACD > 0; 조건 충족; MACD=0.301143, signal9=-0.952827 |
| v1 | rsi_14_recovery | 9960.54 | -39.46 | sell /  / 직전 RSI14 < 30, 현재 RSI14 >= 30 (한 봉 목표); 조건 미충족; RSI14=56.2522, previous_RSI14=46.6115 |
| v1 | bollinger_20_reentry | 9885.00 | -115.00 | sell /  / 직전 종가 < 직전 하단밴드, 현재 하단밴드 <= 종가 <= SMA20 (한 봉 목표); 조건 미충족; close=529.125, lower20=527.516, SMA20=535.918, previous_lower20=528.497 |
| v1 | donchian_20 | 9912.16 | -87.84 | sell /  / 종가 > 현재 봉을 제외한 직전 20봉 최고가; 조건 미충족; close=534.52, prior_high20=535.44 |
| v1 | atr_14_breakout | 9915.10 | -84.90 | sell /  / 종가 > 직전 종가 + 직전 ATR14 그리고 종가 > EMA26; 조건 미충족; close=533.975, threshold=536.307, prior_ATR14=2.16203, EMA26=530.521 |
| v1 | session_vwap | 9894.65 | -105.35 | sell /  / 종가 > 뉴욕 거래일별 누적 전형가격 VWAP; 조건 미충족; close=534.125, session_VWAP=534.159, session_volume=2.7999e+07 |
| v1 | obv_20 | 9767.68 | -232.32 | sell /  / OBV > OBV의 SMA20 그리고 종가 > EMA26; 조건 미충족; OBV=1.08325e+08, OBV_SMA20=1.08557e+08, close=533.95, EMA26=532.788 |
| v1 | stochastic_14_3_recovery | 9792.37 | -207.63 | sell /  / 직전 %K14 < 20에서 %K14가 %D3 상향 돌파 (한 봉 목표); 조건 미충족; K14=25.4855, D3=14.0848, previous_K14=10.0077, previous_D3=7.52857 |
| v1 | mfi_14_recovery | 10009.36 | 9.36 | sell /  / 직전 MFI14 < 20, 현재 MFI14 >= 20 (한 봉 목표); 조건 미충족; MFI14=25.2915, previous_MFI14=22.266 |
| v1 | adx_14_trend | 9883.62 | -116.38 | sell /  / Wilder ADX14 >= 25 그리고 +DI14 > -DI14; 조건 미충족; ADX14=23.6824, plus_DI14=22.3066, minus_DI14=19.9214 |
| v1 | aroon_25_trend | 9812.47 | -187.53 | sell /  / Aroon25 Up > 70 그리고 Down < 30 (동률이면 최신 극값); 조건 미충족; Aroon_up=68, Aroon_down=20 |
| v1 | cci_20_momentum | 10012.15 | 12.15 | sell /  / CCI20 > 100 (전형가격·평균절대편차); 조건 미충족; CCI20=86.441 |
| v1 | williams_14_recovery | 9822.57 | -177.43 | sell /  / 직전 Williams %R14 < -80, 현재 >= -80 (한 봉 목표); 조건 미충족; Williams_R14=-78.4506, previous_R14=-77.7733 |
| v1 | cmf_20_accumulation | 9758.61 | -241.39 | buy /  / Chaikin Money Flow20 > 0.1; 조건 충족; CMF20=0.184396, volume20=3.37825e+07 |
| v1 | chaikin_3_10 | 9817.26 | -182.74 | buy /  / ADL의 EMA3 - EMA10 > 0 그리고 종가 > EMA26; 조건 충족; Chaikin3_10=35900, ADL=1.1173e+08, close=533.95, EMA26=532.788 |
| v1 | roc_10_momentum | 9959.43 | -40.57 | sell /  / 10봉 ROC > 1% 그리고 종가 > EMA26; 조건 미충족; ROC10_percent=0.454191, close=534.125, EMA26=532.186 |
| v1 | trix_15_trend | 9868.35 | -131.65 | buy /  / 15봉 삼중 EMA의 1봉 변화율 TRIX > 0 그리고 종가 > EMA26; 조건 충족; TRIX15_percent=0.00435677, close=534.125, EMA26=532.186 |
| v1 | keltner_20_breakout | 9958.78 | -41.22 | sell /  / 종가 > EMA20 + 2 x Wilder ATR14; 조건 미충족; close=533.975, upper_Keltner=534.357, EMA20=530.111, ATR14=2.12332 |
| v1 | opening_range_30m | 9867.70 | -132.30 | buy /  / 뉴욕 09:30·09:45 두 완료 봉 최고가를 10:00 이후 종가가 돌파; 조건 충족; close=534.145, opening_high=532.63 |
| v2 | cash | 10000.00 | 0.00 | 대기 /  / 새 신호 대기 |
| v2 | buy_hold | 9904.01 | -95.99 | buy / partial / 직전 완료 봉 목표 비중 100%; 다음 봉 시가 가정 |
| v2 | trend_8_26 | 9768.45 | -231.55 | buy / partial / 직전 완료 봉 목표 비중 100%; 다음 봉 시가 가정 |
| v2 | momentum_26 | 9849.50 | -150.50 | buy / partial / 직전 완료 봉 목표 비중 100%; 다음 봉 시가 가정 |
| v2 | breakout_8 | 9670.87 | -329.13 | sell / filled / 직전 완료 봉 목표 비중 0%; 다음 봉 시가 가정 |
| v2 | reversion_12 | 9395.36 | -604.64 | sell / filled / 직전 완료 봉 목표 비중 0%; 다음 봉 시가 가정 |
| v2 | volume_26 | 9498.13 | -501.87 | sell / filled / 직전 완료 봉 목표 비중 0%; 다음 봉 시가 가정 |
| v2 | trend_8_26 AND momentum_26 | 9714.95 | -285.05 | buy / partial / 직전 완료 봉 목표 비중 100%; 다음 봉 시가 가정 |
| v2 | trend_8_26 + momentum_26 | 9809.16 | -190.84 | buy / partial / 직전 완료 봉 목표 비중 100%; 다음 봉 시가 가정 |
| v2 | trend_8_26 AND breakout_8 | 9543.92 | -456.08 | sell / filled / 직전 완료 봉 목표 비중 0%; 다음 봉 시가 가정 |
| v2 | trend_8_26 + breakout_8 | 9760.64 | -239.36 | buy / filled / 직전 완료 봉 목표 비중 50%; 다음 봉 시가 가정 |
| v2 | trend_8_26 AND reversion_12 | 9792.57 | -207.43 | sell / filled / 직전 완료 봉 목표 비중 0%; 다음 봉 시가 가정 |
| v2 | trend_8_26 + reversion_12 | 9579.71 | -420.29 | sell / filled / 직전 완료 봉 목표 비중 50%; 다음 봉 시가 가정 |
| v2 | trend_8_26 AND volume_26 | 9861.94 | -138.06 | sell / filled / 직전 완료 봉 목표 비중 0%; 다음 봉 시가 가정 |
| v2 | trend_8_26 + volume_26 | 9652.34 | -347.66 | buy / filled / 직전 완료 봉 목표 비중 50%; 다음 봉 시가 가정 |
| v2 | momentum_26 AND breakout_8 | 9697.48 | -302.52 | sell / filled / 직전 완료 봉 목표 비중 0%; 다음 봉 시가 가정 |
| v2 | momentum_26 + breakout_8 | 9759.83 | -240.17 | buy / filled / 직전 완료 봉 목표 비중 50%; 다음 봉 시가 가정 |
| v2 | momentum_26 AND reversion_12 | 9705.98 | -294.02 | sell / filled / 직전 완료 봉 목표 비중 0%; 다음 봉 시가 가정 |
| v2 | momentum_26 + reversion_12 | 9619.49 | -380.51 | sell / filled / 직전 완료 봉 목표 비중 50%; 다음 봉 시가 가정 |
| v2 | momentum_26 AND volume_26 | 9785.21 | -214.79 | sell / filled / 직전 완료 봉 목표 비중 0%; 다음 봉 시가 가정 |
| v2 | momentum_26 + volume_26 | 9692.44 | -307.56 | buy / filled / 직전 완료 봉 목표 비중 50%; 다음 봉 시가 가정 |
| v2 | breakout_8 AND reversion_12 | 10000.00 | 0.00 | 대기 /  / 새 신호 대기 |
| v2 | breakout_8 + reversion_12 | 9571.93 | -428.07 | sell / filled / 직전 완료 봉 목표 비중 0%; 다음 봉 시가 가정 |
| v2 | breakout_8 AND volume_26 | 9890.09 | -109.91 | sell / filled / 직전 완료 봉 목표 비중 0%; 다음 봉 시가 가정 |
| v2 | breakout_8 + volume_26 | 9624.43 | -375.57 | sell / filled / 직전 완료 봉 목표 비중 0%; 다음 봉 시가 가정 |
| v2 | reversion_12 AND volume_26 | 9699.57 | -300.43 | sell / filled / 직전 완료 봉 목표 비중 0%; 다음 봉 시가 가정 |
| v2 | reversion_12 + volume_26 | 9446.34 | -553.66 | sell / filled / 직전 완료 봉 목표 비중 0%; 다음 봉 시가 가정 |
| v2 | ema_12_26 | 9815.15 | -184.85 | buy / partial / EMA12 > EMA26; 조건 충족; EMA12=531.372, EMA26=531.07; 직전 완료 봉 목표를 다음 봉 시가에 모의 적용 |
| v2 | macd_12_26_9 | 9851.28 | -148.72 | buy / partial / MACD > 신호선 그리고 MACD > 0; 조건 충족; MACD=0.301143, signal9=-0.952827; 직전 완료 봉 목표를 다음 봉 시가에 모의 적용 |
| v2 | rsi_14_recovery | 9956.56 | -43.44 | sell / filled / 직전 RSI14 < 30, 현재 RSI14 >= 30 (한 봉 목표); 조건 미충족; RSI14=56.2522, previous_RSI14=46.6115; 직전 완료 봉 목표를 다음 봉 시가에 모의 적용 |
| v2 | bollinger_20_reentry | 9881.05 | -118.95 | sell / filled / 직전 종가 < 직전 하단밴드, 현재 하단밴드 <= 종가 <= SMA20 (한 봉 목표); 조건 미충족; close=529.125, lower20=527.516, SMA20=535.918, previous_lower20=528.497; 직전 완료 봉 목표를 다음 봉 시가에 모의 적용 |
| v2 | donchian_20 | 9908.19 | -91.81 | sell / filled / 종가 > 현재 봉을 제외한 직전 20봉 최고가; 조건 미충족; close=534.52, prior_high20=535.44; 직전 완료 봉 목표를 다음 봉 시가에 모의 적용 |
| v2 | atr_14_breakout | 9911.14 | -88.86 | sell / filled / 종가 > 직전 종가 + 직전 ATR14 그리고 종가 > EMA26; 조건 미충족; close=533.975, threshold=536.307, prior_ATR14=2.16203, EMA26=530.521; 직전 완료 봉 목표를 다음 봉 시가에 모의 적용 |
| v2 | session_vwap | 9890.69 | -109.31 | sell / filled / 종가 > 뉴욕 거래일별 누적 전형가격 VWAP; 조건 미충족; close=534.125, session_VWAP=534.159, session_volume=2.7999e+07; 직전 완료 봉 목표를 다음 봉 시가에 모의 적용 |
| v2 | obv_20 | 9759.87 | -240.13 | sell / filled / OBV > OBV의 SMA20 그리고 종가 > EMA26; 조건 미충족; OBV=1.08325e+08, OBV_SMA20=1.08557e+08, close=533.95, EMA26=532.788; 직전 완료 봉 목표를 다음 봉 시가에 모의 적용 |
| v2 | stochastic_14_3_recovery | 9784.54 | -215.46 | sell / filled / 직전 %K14 < 20에서 %K14가 %D3 상향 돌파 (한 봉 목표); 조건 미충족; K14=25.4855, D3=14.0848, previous_K14=10.0077, previous_D3=7.52857; 직전 완료 봉 목표를 다음 봉 시가에 모의 적용 |
| v2 | mfi_14_recovery | 10007.36 | 7.36 | sell / filled / 직전 MFI14 < 20, 현재 MFI14 >= 20 (한 봉 목표); 조건 미충족; MFI14=25.2915, previous_MFI14=22.266; 직전 완료 봉 목표를 다음 봉 시가에 모의 적용 |
| v2 | adx_14_trend | 9879.67 | -120.33 | sell / filled / Wilder ADX14 >= 25 그리고 +DI14 > -DI14; 조건 미충족; ADX14=23.6824, plus_DI14=22.3066, minus_DI14=19.9214; 직전 완료 봉 목표를 다음 봉 시가에 모의 적용 |
| v2 | aroon_25_trend | 9808.55 | -191.45 | sell / filled / Aroon25 Up > 70 그리고 Down < 30 (동률이면 최신 극값); 조건 미충족; Aroon_up=68, Aroon_down=20; 직전 완료 봉 목표를 다음 봉 시가에 모의 적용 |
| v2 | cci_20_momentum | 10010.15 | 10.15 | sell / filled / CCI20 > 100 (전형가격·평균절대편차); 조건 미충족; CCI20=86.441; 직전 완료 봉 목표를 다음 봉 시가에 모의 적용 |
| v2 | williams_14_recovery | 9816.68 | -183.32 | sell / filled / 직전 Williams %R14 < -80, 현재 >= -80 (한 봉 목표); 조건 미충족; Williams_R14=-78.4506, previous_R14=-77.7733; 직전 완료 봉 목표를 다음 봉 시가에 모의 적용 |
| v2 | cmf_20_accumulation | 9755.68 | -244.32 | buy / partial / Chaikin Money Flow20 > 0.1; 조건 충족; CMF20=0.184396, volume20=3.37825e+07; 직전 완료 봉 목표를 다음 봉 시가에 모의 적용 |
| v2 | chaikin_3_10 | 9812.36 | -187.64 | buy / partial / ADL의 EMA3 - EMA10 > 0 그리고 종가 > EMA26; 조건 충족; Chaikin3_10=35900, ADL=1.1173e+08, close=533.95, EMA26=532.788; 직전 완료 봉 목표를 다음 봉 시가에 모의 적용 |
| v2 | roc_10_momentum | 9957.44 | -42.56 | sell / filled / 10봉 ROC > 1% 그리고 종가 > EMA26; 조건 미충족; ROC10_percent=0.454191, close=534.125, EMA26=532.186; 직전 완료 봉 목표를 다음 봉 시가에 모의 적용 |
| v2 | trix_15_trend | 9865.39 | -134.61 | buy / partial / 15봉 삼중 EMA의 1봉 변화율 TRIX > 0 그리고 종가 > EMA26; 조건 충족; TRIX15_percent=0.00435677, close=534.125, EMA26=532.186; 직전 완료 봉 목표를 다음 봉 시가에 모의 적용 |
| v2 | keltner_20_breakout | 9956.78 | -43.22 | sell / filled / 종가 > EMA20 + 2 x Wilder ATR14; 조건 미충족; close=533.975, upper_Keltner=534.357, EMA20=530.111, ATR14=2.12332; 직전 완료 봉 목표를 다음 봉 시가에 모의 적용 |
| v2 | opening_range_30m | 9864.74 | -135.26 | buy / partial / 뉴욕 09:30·09:45 두 완료 봉 최고가를 10:00 이후 종가가 돌파; 조건 충족; close=534.145, opening_high=532.63; 직전 완료 봉 목표를 다음 봉 시가에 모의 적용 |

### 같은 기간의 비용·노출 비교 (사후 연구)

| 전략 | 비용 전 | 비용 후 | 100% 보유 | 같은 평균 노출 보유 | 평균 노출 |
|---|---:|---:|---:|---:|---:|
| cash | 0.00% | 0.00% | 5.66% | 0.00% | 0.00% |
| buy_hold | 6.10% | 5.66% | 5.66% | 5.66% | 100.00% |
| trend_8_26 | 2.53% | -0.86% | 5.66% | 3.19% | 57.59% |
| momentum_26 | 1.67% | -4.13% | 5.66% | 3.33% | 59.95% |
| breakout_8 | 5.93% | -8.55% | 5.66% | 1.10% | 20.16% |
| reversion_12 | -2.51% | -11.49% | 5.66% | 1.36% | 24.87% |
| volume_26 | 1.69% | -7.29% | 5.66% | 0.48% | 8.90% |
| trend_8_26 AND momentum_26 | 0.41% | -5.33% | 5.66% | 2.96% | 53.40% |
| trend_8_26 + momentum_26 | 2.11% | -2.50% | 5.66% | 3.26% | 58.77% |
| trend_8_26 AND breakout_8 | 0.52% | -9.88% | 5.66% | 0.71% | 13.09% |
| trend_8_26 + breakout_8 | 4.23% | -4.18% | 5.66% | 2.14% | 38.88% |
| trend_8_26 AND reversion_12 | -0.05% | -5.36% | 5.66% | 0.35% | 6.54% |
| trend_8_26 + reversion_12 | -0.01% | -6.13% | 5.66% | 2.27% | 41.23% |
| trend_8_26 AND volume_26 | 3.42% | -0.42% | 5.66% | 0.17% | 3.14% |
| trend_8_26 + volume_26 | 2.12% | -3.53% | 5.66% | 1.82% | 33.25% |
| momentum_26 AND breakout_8 | 2.46% | -8.53% | 5.66% | 0.73% | 13.35% |
| momentum_26 + breakout_8 | 3.79% | -5.77% | 5.66% | 2.20% | 40.06% |
| momentum_26 AND reversion_12 | -1.06% | -7.49% | 5.66% | 0.51% | 9.42% |
| momentum_26 + reversion_12 | -0.42% | -7.69% | 5.66% | 2.33% | 42.41% |
| momentum_26 AND volume_26 | 1.77% | -3.23% | 5.66% | 0.21% | 3.93% |
| momentum_26 + volume_26 | 1.69% | -4.73% | 5.66% | 1.89% | 34.43% |
| breakout_8 AND reversion_12 | 0.00% | 0.00% | 5.66% | 0.00% | 0.00% |
| breakout_8 + reversion_12 | 1.64% | -9.28% | 5.66% | 1.23% | 22.52% |
| breakout_8 AND volume_26 | 2.00% | -0.96% | 5.66% | 0.11% | 2.09% |
| breakout_8 + volume_26 | 3.80% | -6.75% | 5.66% | 0.79% | 14.54% |
| reversion_12 AND volume_26 | -2.90% | -6.11% | 5.66% | 0.18% | 3.40% |
| reversion_12 + volume_26 | -0.42% | -9.22% | 5.66% | 0.92% | 16.89% |
| ema_12_26 | 1.64% | -1.72% | 5.66% | 3.31% | 59.69% |
| macd_12_26_9 | 1.17% | -3.80% | 5.66% | 1.87% | 34.03% |
| rsi_14_recovery | -0.06% | -2.13% | 5.66% | 0.07% | 1.31% |
| bollinger_20_reentry | -0.29% | -3.18% | 5.66% | 0.10% | 1.83% |
| donchian_20 | 1.76% | -4.05% | 5.66% | 0.27% | 4.97% |
| atr_14_breakout | 1.45% | -4.74% | 5.66% | 0.23% | 4.19% |
| session_vwap | 6.65% | -1.12% | 5.66% | 2.26% | 41.10% |
| obv_20 | 4.62% | -4.21% | 5.66% | 2.75% | 49.74% |
| stochastic_14_3_recovery | -0.50% | -10.80% | 5.66% | 0.37% | 6.81% |
| mfi_14_recovery | 1.54% | -1.81% | 5.66% | 0.11% | 2.09% |
| adx_14_trend | 3.84% | 1.26% | 5.66% | 2.56% | 46.34% |
| aroon_25_trend | 0.07% | -4.85% | 5.66% | 1.24% | 22.77% |
| cci_20_momentum | 3.27% | -3.44% | 5.66% | 1.24% | 22.77% |
| williams_14_recovery | -0.78% | -9.91% | 5.66% | 0.33% | 6.02% |
| cmf_20_accumulation | 0.64% | -5.11% | 5.66% | 1.74% | 31.68% |
| chaikin_3_10 | 3.70% | -4.25% | 5.66% | 2.50% | 45.29% |
| roc_10_momentum | -0.01% | -4.12% | 5.66% | 0.85% | 15.71% |
| trix_15_trend | 0.54% | -3.60% | 5.66% | 2.63% | 47.64% |
| keltner_20_breakout | 1.11% | -4.26% | 5.66% | 0.74% | 13.61% |
| opening_range_30m | -0.56% | -5.05% | 5.66% | 1.21% | 22.25% |

동일 구간·초기 자금, 종료 시 청산 비용 포함. 노출 맞춤은 사후 설명용이며 v2 실제 계좌 성과가 아닙니다.
[낙폭 분해·비용 영향·전체 구간](MSFT/comparison.json)

[v1 전체 기록](MSFT/accounts.json) · [v2 전체 기록](MSFT/accounts-v2.json)

## JPM 계좌

| 모델 | 전략 | 평가액 USD | 손익 USD | 최근 매매·이유 |
|---|---|---:|---:|---|
| v1 | cash | 10000.00 | 0.00 | 대기 /  / 새 신호 대기 |
| v1 | buy_hold | 9836.46 | -163.54 | buy /  / buy_hold: prior completed bar target 100%; next bar open simulation |
| v1 | trend_8_26 | 9924.04 | -75.96 | sell /  / trend_8_26: prior completed bar target 0%; next bar open simulation |
| v1 | momentum_26 | 9892.69 | -107.31 | sell /  / momentum_26: prior completed bar target 0%; next bar open simulation |
| v1 | breakout_8 | 9829.39 | -170.61 | sell /  / breakout_8: prior completed bar target 0%; next bar open simulation |
| v1 | reversion_12 | 9720.22 | -279.78 | buy /  / reversion_12: prior completed bar target 100%; next bar open simulation |
| v1 | volume_26 | 9994.65 | -5.35 | buy /  / volume_26: prior completed bar target 100%; next bar open simulation |
| v1 | trend_8_26 AND momentum_26 | 9924.04 | -75.96 | sell /  / trend_8_26 AND momentum_26: prior completed bar target 0%; next bar open simulation |
| v1 | trend_8_26 + momentum_26 | 9908.39 | -91.61 | sell /  / trend_8_26 + momentum_26: prior completed bar target 0%; next bar open simulation |
| v1 | trend_8_26 AND breakout_8 | 9915.55 | -84.45 | sell /  / trend_8_26 AND breakout_8: prior completed bar target 0%; next bar open simulation |
| v1 | trend_8_26 + breakout_8 | 9876.66 | -123.34 | sell /  / trend_8_26 + breakout_8: prior completed bar target 0%; next bar open simulation |
| v1 | trend_8_26 AND reversion_12 | 9899.24 | -100.76 | sell /  / trend_8_26 AND reversion_12: prior completed bar target 0%; next bar open simulation |
| v1 | trend_8_26 + reversion_12 | 9821.49 | -178.51 | buy /  / trend_8_26 + reversion_12: prior completed bar target 50%; next bar open simulation |
| v1 | trend_8_26 AND volume_26 | 10035.68 | 35.68 | sell /  / trend_8_26 AND volume_26: prior completed bar target 0%; next bar open simulation |
| v1 | trend_8_26 + volume_26 | 9959.19 | -40.81 | buy /  / trend_8_26 + volume_26: prior completed bar target 50%; next bar open simulation |
| v1 | momentum_26 AND breakout_8 | 9829.39 | -170.61 | sell /  / momentum_26 AND breakout_8: prior completed bar target 0%; next bar open simulation |
| v1 | momentum_26 + breakout_8 | 9861.04 | -138.96 | sell /  / momentum_26 + breakout_8: prior completed bar target 0%; next bar open simulation |
| v1 | momentum_26 AND reversion_12 | 9881.87 | -118.13 | sell /  / momentum_26 AND reversion_12: prior completed bar target 0%; next bar open simulation |
| v1 | momentum_26 + reversion_12 | 9825.62 | -174.38 | buy /  / momentum_26 + reversion_12: prior completed bar target 50%; next bar open simulation |
| v1 | momentum_26 AND volume_26 | 10035.68 | 35.68 | sell /  / momentum_26 AND volume_26: prior completed bar target 0%; next bar open simulation |
| v1 | momentum_26 + volume_26 | 9943.47 | -56.53 | buy /  / momentum_26 + volume_26: prior completed bar target 50%; next bar open simulation |
| v1 | breakout_8 AND reversion_12 | 10000.00 | 0.00 | 대기 /  / 새 신호 대기 |
| v1 | breakout_8 + reversion_12 | 9794.11 | -205.89 | buy /  / breakout_8 + reversion_12: prior completed bar target 50%; next bar open simulation |
| v1 | breakout_8 AND volume_26 | 10035.68 | 35.68 | sell /  / breakout_8 AND volume_26: prior completed bar target 0%; next bar open simulation |
| v1 | breakout_8 + volume_26 | 9911.66 | -88.34 | buy /  / breakout_8 + volume_26: prior completed bar target 50%; next bar open simulation |
| v1 | reversion_12 AND volume_26 | 9959.12 | -40.88 | buy /  / reversion_12 AND volume_26: prior completed bar target 100%; next bar open simulation |
| v1 | reversion_12 + volume_26 | 9856.38 | -143.62 | buy /  / reversion_12 + volume_26: prior completed bar target 100%; next bar open simulation |
| v1 | ema_12_26 | 9888.73 | -111.27 | sell /  / EMA12 > EMA26; 조건 미충족; EMA12=338.579, EMA26=338.665 |
| v1 | macd_12_26_9 | 9973.56 | -26.44 | sell /  / MACD > 신호선 그리고 MACD > 0; 조건 미충족; MACD=1.87003, signal9=1.96381 |
| v1 | rsi_14_recovery | 10000.00 | 0.00 | 대기 /  / 새 신호 대기 |
| v1 | bollinger_20_reentry | 9964.67 | -35.33 | sell /  / 직전 종가 < 직전 하단밴드, 현재 하단밴드 <= 종가 <= SMA20 (한 봉 목표); 조건 미충족; close=336.53, lower20=336.046, SMA20=337.886, previous_lower20=336.231 |
| v1 | donchian_20 | 9872.30 | -127.70 | sell /  / 종가 > 현재 봉을 제외한 직전 20봉 최고가; 조건 미충족; close=343.037, prior_high20=344.4 |
| v1 | atr_14_breakout | 9801.01 | -198.99 | sell /  / 종가 > 직전 종가 + 직전 ATR14 그리고 종가 > EMA26; 조건 미충족; close=337.6, threshold=340.744, prior_ATR14=1.10351, EMA26=338.759 |
| v1 | session_vwap | 9799.54 | -200.46 | sell /  / 종가 > 뉴욕 거래일별 누적 전형가격 VWAP; 조건 미충족; close=337.19, session_VWAP=337.924, session_volume=2.62446e+06 |
| v1 | obv_20 | 10007.55 | 7.55 | sell /  / OBV > OBV의 SMA20 그리고 종가 > EMA26; 조건 미충족; OBV=-1.68091e+07, OBV_SMA20=-1.39645e+07, close=341.625, EMA26=338.807 |
| v1 | stochastic_14_3_recovery | 9845.39 | -154.61 | sell /  / 직전 %K14 < 20에서 %K14가 %D3 상향 돌파 (한 봉 목표); 조건 미충족; K14=18.8407, D3=11.3622, previous_K14=11.051, previous_D3=10.6752 |
| v1 | mfi_14_recovery | 9949.20 | -50.80 | sell /  / 직전 MFI14 < 20, 현재 MFI14 >= 20 (한 봉 목표); 조건 미충족; MFI14=27.7885, previous_MFI14=28.8811 |
| v1 | adx_14_trend | 9806.96 | -193.04 | sell /  / Wilder ADX14 >= 25 그리고 +DI14 > -DI14; 조건 미충족; ADX14=30.1815, plus_DI14=27.5695, minus_DI14=29.9812 |
| v1 | aroon_25_trend | 9824.71 | -175.29 | sell /  / Aroon25 Up > 70 그리고 Down < 30 (동률이면 최신 극값); 조건 미충족; Aroon_up=68, Aroon_down=16 |
| v1 | cci_20_momentum | 10050.62 | 50.62 | sell /  / CCI20 > 100 (전형가격·평균절대편차); 조건 미충족; CCI20=93.5627 |
| v1 | williams_14_recovery | 9833.83 | -166.17 | sell /  / 직전 Williams %R14 < -80, 현재 >= -80 (한 봉 목표); 조건 미충족; Williams_R14=-75.4596, previous_R14=-77.2645 |
| v1 | cmf_20_accumulation | 9932.16 | -67.84 | sell /  / Chaikin Money Flow20 > 0.1; 조건 미충족; CMF20=-0.14511, volume20=9.3038e+06 |
| v1 | chaikin_3_10 | 9920.58 | -79.42 | sell /  / ADL의 EMA3 - EMA10 > 0 그리고 종가 > EMA26; 조건 미충족; Chaikin3_10=55836.7, ADL=-1.05866e+07, close=337.6, EMA26=338.759 |
| v1 | roc_10_momentum | 9913.84 | -86.16 | sell /  / 10봉 ROC > 1% 그리고 종가 > EMA26; 조건 미충족; ROC10_percent=-0.490038, close=340.901, EMA26=338.962 |
| v1 | trix_15_trend | 9723.73 | -276.27 | sell /  / 15봉 삼중 EMA의 1봉 변화율 TRIX > 0 그리고 종가 > EMA26; 조건 미충족; TRIX15_percent=0.0135144, close=337.6, EMA26=338.759 |
| v1 | keltner_20_breakout | 9946.99 | -53.01 | sell /  / 종가 > EMA20 + 2 x Wilder ATR14; 조건 미충족; close=342, upper_Keltner=342.276, EMA20=339.397, ATR14=1.43933 |
| v1 | opening_range_30m | 9927.81 | -72.19 | sell /  / 뉴욕 09:30·09:45 두 완료 봉 최고가를 10:00 이후 종가가 돌파; 조건 미충족; close=343.037, opening_high=343.75 |
| v2 | cash | 10000.00 | 0.00 | 대기 /  / 새 신호 대기 |
| v2 | buy_hold | 10000.82 | 0.82 | buy / partial / 직전 완료 봉 목표 비중 100%; 다음 봉 시가 가정 |
| v2 | trend_8_26 | 9931.17 | -68.83 | sell / filled / 직전 완료 봉 목표 비중 0%; 다음 봉 시가 가정 |
| v2 | momentum_26 | 9401.71 | -598.29 | sell / filled / 직전 완료 봉 목표 비중 0%; 다음 봉 시가 가정 |
| v2 | breakout_8 | 9168.97 | -831.03 | sell / filled / 직전 완료 봉 목표 비중 0%; 다음 봉 시가 가정 |
| v2 | reversion_12 | 9697.87 | -302.13 | buy / partial / 직전 완료 봉 목표 비중 100%; 다음 봉 시가 가정 |
| v2 | volume_26 | 9816.54 | -183.46 | buy / partial / 직전 완료 봉 목표 비중 100%; 다음 봉 시가 가정 |
| v2 | trend_8_26 AND momentum_26 | 9890.41 | -109.59 | sell / filled / 직전 완료 봉 목표 비중 0%; 다음 봉 시가 가정 |
| v2 | trend_8_26 + momentum_26 | 9683.69 | -316.31 | sell / filled / 직전 완료 봉 목표 비중 0%; 다음 봉 시가 가정 |
| v2 | trend_8_26 AND breakout_8 | 9287.76 | -712.24 | sell / filled / 직전 완료 봉 목표 비중 0%; 다음 봉 시가 가정 |
| v2 | trend_8_26 + breakout_8 | 9543.58 | -456.42 | sell / filled / 직전 완료 봉 목표 비중 0%; 다음 봉 시가 가정 |
| v2 | trend_8_26 AND reversion_12 | 9877.09 | -122.91 | sell / filled / 직전 완료 봉 목표 비중 0%; 다음 봉 시가 가정 |
| v2 | trend_8_26 + reversion_12 | 9855.22 | -144.78 | buy / filled / 직전 완료 봉 목표 비중 50%; 다음 봉 시가 가정 |
| v2 | trend_8_26 AND volume_26 | 9833.30 | -166.70 | sell / filled / 직전 완료 봉 목표 비중 0%; 다음 봉 시가 가정 |
| v2 | trend_8_26 + volume_26 | 9874.42 | -125.58 | buy / filled / 직전 완료 봉 목표 비중 50%; 다음 봉 시가 가정 |
| v2 | momentum_26 AND breakout_8 | 9150.64 | -849.36 | sell / filled / 직전 완료 봉 목표 비중 0%; 다음 봉 시가 가정 |
| v2 | momentum_26 + breakout_8 | 9305.78 | -694.22 | sell / filled / 직전 완료 봉 목표 비중 0%; 다음 봉 시가 가정 |
| v2 | momentum_26 AND reversion_12 | 9827.31 | -172.69 | sell / filled / 직전 완료 봉 목표 비중 0%; 다음 봉 시가 가정 |
| v2 | momentum_26 + reversion_12 | 9690.51 | -309.49 | buy / filled / 직전 완료 봉 목표 비중 50%; 다음 봉 시가 가정 |
| v2 | momentum_26 AND volume_26 | 9833.30 | -166.70 | sell / filled / 직전 완료 봉 목표 비중 0%; 다음 봉 시가 가정 |
| v2 | momentum_26 + volume_26 | 9668.77 | -331.23 | buy / filled / 직전 완료 봉 목표 비중 50%; 다음 봉 시가 가정 |
| v2 | breakout_8 AND reversion_12 | 10000.00 | 0.00 | 대기 /  / 새 신호 대기 |
| v2 | breakout_8 + reversion_12 | 9489.41 | -510.59 | buy / filled / 직전 완료 봉 목표 비중 50%; 다음 봉 시가 가정 |
| v2 | breakout_8 AND volume_26 | 9926.66 | -73.34 | sell / filled / 직전 완료 봉 목표 비중 0%; 다음 봉 시가 가정 |
| v2 | breakout_8 + volume_26 | 9507.30 | -492.70 | buy / filled / 직전 완료 봉 목표 비중 50%; 다음 봉 시가 가정 |
| v2 | reversion_12 AND volume_26 | 10007.29 | 7.29 | buy / partial / 직전 완료 봉 목표 비중 100%; 다음 봉 시가 가정 |
| v2 | reversion_12 + volume_26 | 9777.70 | -222.30 | buy / partial / 직전 완료 봉 목표 비중 100%; 다음 봉 시가 가정 |
| v2 | ema_12_26 | 9886.75 | -113.25 | sell / filled / EMA12 > EMA26; 조건 미충족; EMA12=338.579, EMA26=338.665; 직전 완료 봉 목표를 다음 봉 시가에 모의 적용 |
| v2 | macd_12_26_9 | 9971.56 | -28.44 | sell / filled / MACD > 신호선 그리고 MACD > 0; 조건 미충족; MACD=1.87003, signal9=1.96381; 직전 완료 봉 목표를 다음 봉 시가에 모의 적용 |
| v2 | rsi_14_recovery | 10000.00 | 0.00 | 대기 /  / 새 신호 대기 |
| v2 | bollinger_20_reentry | 9962.68 | -37.32 | sell / filled / 직전 종가 < 직전 하단밴드, 현재 하단밴드 <= 종가 <= SMA20 (한 봉 목표); 조건 미충족; close=336.53, lower20=336.046, SMA20=337.886, previous_lower20=336.231; 직전 완료 봉 목표를 다음 봉 시가에 모의 적용 |
| v2 | donchian_20 | 9868.35 | -131.65 | sell / filled / 종가 > 현재 봉을 제외한 직전 20봉 최고가; 조건 미충족; close=343.037, prior_high20=344.4; 직전 완료 봉 목표를 다음 봉 시가에 모의 적용 |
| v2 | atr_14_breakout | 9795.13 | -204.87 | sell / filled / 종가 > 직전 종가 + 직전 ATR14 그리고 종가 > EMA26; 조건 미충족; close=337.6, threshold=340.744, prior_ATR14=1.10351, EMA26=338.759; 직전 완료 봉 목표를 다음 봉 시가에 모의 적용 |
| v2 | session_vwap | 9791.71 | -208.29 | sell / filled / 종가 > 뉴욕 거래일별 누적 전형가격 VWAP; 조건 미충족; close=337.19, session_VWAP=337.924, session_volume=2.62446e+06; 직전 완료 봉 목표를 다음 봉 시가에 모의 적용 |
| v2 | obv_20 | 10005.55 | 5.55 | sell / filled / OBV > OBV의 SMA20 그리고 종가 > EMA26; 조건 미충족; OBV=-1.38544e+07, OBV_SMA20=-1.10099e+07, close=341.625, EMA26=338.807; 직전 완료 봉 목표를 다음 봉 시가에 모의 적용 |
| v2 | stochastic_14_3_recovery | 9837.51 | -162.49 | sell / filled / 직전 %K14 < 20에서 %K14가 %D3 상향 돌파 (한 봉 목표); 조건 미충족; K14=18.8407, D3=11.3622, previous_K14=11.051, previous_D3=10.6752; 직전 완료 봉 목표를 다음 봉 시가에 모의 적용 |
| v2 | mfi_14_recovery | 9947.21 | -52.79 | sell / filled / 직전 MFI14 < 20, 현재 MFI14 >= 20 (한 봉 목표); 조건 미충족; MFI14=27.7885, previous_MFI14=28.8811; 직전 완료 봉 목표를 다음 봉 시가에 모의 적용 |
| v2 | adx_14_trend | 9805.00 | -195.00 | sell / filled / Wilder ADX14 >= 25 그리고 +DI14 > -DI14; 조건 미충족; ADX14=30.1815, plus_DI14=27.5695, minus_DI14=29.9812; 직전 완료 봉 목표를 다음 봉 시가에 모의 적용 |
| v2 | aroon_25_trend | 9822.74 | -177.26 | sell / filled / Aroon25 Up > 70 그리고 Down < 30 (동률이면 최신 극값); 조건 미충족; Aroon_up=68, Aroon_down=16; 직전 완료 봉 목표를 다음 봉 시가에 모의 적용 |
| v2 | cci_20_momentum | 10048.61 | 48.61 | sell / filled / CCI20 > 100 (전형가격·평균절대편차); 조건 미충족; CCI20=93.5627; 직전 완료 봉 목표를 다음 봉 시가에 모의 적용 |
| v2 | williams_14_recovery | 9825.97 | -174.03 | sell / filled / 직전 Williams %R14 < -80, 현재 >= -80 (한 봉 목표); 조건 미충족; Williams_R14=-75.4596, previous_R14=-77.2645; 직전 완료 봉 목표를 다음 봉 시가에 모의 적용 |
| v2 | cmf_20_accumulation | 9930.17 | -69.83 | sell / filled / Chaikin Money Flow20 > 0.1; 조건 미충족; CMF20=-0.14511, volume20=9.3038e+06; 직전 완료 봉 목표를 다음 봉 시가에 모의 적용 |
| v2 | chaikin_3_10 | 9916.62 | -83.38 | sell / filled / ADL의 EMA3 - EMA10 > 0 그리고 종가 > EMA26; 조건 미충족; Chaikin3_10=55836.7, ADL=-1.05866e+07, close=337.6, EMA26=338.759; 직전 완료 봉 목표를 다음 봉 시가에 모의 적용 |
| v2 | roc_10_momentum | 9911.86 | -88.14 | sell / filled / 10봉 ROC > 1% 그리고 종가 > EMA26; 조건 미충족; ROC10_percent=-0.490038, close=340.901, EMA26=338.962; 직전 완료 봉 목표를 다음 봉 시가에 모의 적용 |
| v2 | trix_15_trend | 9715.96 | -284.04 | sell / filled / 15봉 삼중 EMA의 1봉 변화율 TRIX > 0 그리고 종가 > EMA26; 조건 미충족; TRIX15_percent=0.0135144, close=337.6, EMA26=338.759; 직전 완료 봉 목표를 다음 봉 시가에 모의 적용 |
| v2 | keltner_20_breakout | 9945.00 | -55.00 | sell / filled / 종가 > EMA20 + 2 x Wilder ATR14; 조건 미충족; close=342, upper_Keltner=342.276, EMA20=339.397, ATR14=1.43933; 직전 완료 봉 목표를 다음 봉 시가에 모의 적용 |
| v2 | opening_range_30m | 9925.82 | -74.18 | sell / filled / 뉴욕 09:30·09:45 두 완료 봉 최고가를 10:00 이후 종가가 돌파; 조건 미충족; close=343.037, opening_high=343.75; 직전 완료 봉 목표를 다음 봉 시가에 모의 적용 |

### 같은 기간의 비용·노출 비교 (사후 연구)

| 전략 | 비용 전 | 비용 후 | 100% 보유 | 같은 평균 노출 보유 | 평균 노출 |
|---|---:|---:|---:|---:|---:|
| cash | 0.00% | 0.00% | -1.27% | -0.00% | 0.00% |
| buy_hold | -0.86% | -1.27% | -1.27% | -1.27% | 100.00% |
| trend_8_26 | 1.16% | -2.59% | -1.27% | -0.66% | 51.57% |
| momentum_26 | -2.37% | -8.33% | -1.27% | -0.62% | 48.43% |
| breakout_8 | -3.63% | -18.53% | -1.27% | -0.25% | 19.63% |
| reversion_12 | 4.76% | -10.32% | -1.27% | -0.34% | 26.18% |
| volume_26 | -0.03% | -6.13% | -1.27% | -0.09% | 6.81% |
| trend_8_26 AND momentum_26 | 1.09% | -3.07% | -1.27% | -0.52% | 40.58% |
| trend_8_26 + momentum_26 | -0.61% | -5.30% | -1.27% | -0.64% | 50.00% |
| trend_8_26 AND breakout_8 | -3.21% | -13.22% | -1.27% | -0.16% | 12.04% |
| trend_8_26 + breakout_8 | -1.24% | -10.72% | -1.27% | -0.46% | 35.61% |
| trend_8_26 AND reversion_12 | 2.66% | -3.61% | -1.27% | -0.09% | 7.33% |
| trend_8_26 + reversion_12 | 2.96% | -5.95% | -1.27% | -0.50% | 38.88% |
| trend_8_26 AND volume_26 | -0.42% | -4.11% | -1.27% | -0.05% | 3.93% |
| trend_8_26 + volume_26 | 0.58% | -4.37% | -1.27% | -0.38% | 29.19% |
| momentum_26 AND breakout_8 | -2.51% | -12.96% | -1.27% | -0.16% | 12.04% |
| momentum_26 + breakout_8 | -2.98% | -13.38% | -1.27% | -0.44% | 34.04% |
| momentum_26 AND reversion_12 | 2.79% | -4.29% | -1.27% | -0.09% | 6.81% |
| momentum_26 + reversion_12 | 1.15% | -7.80% | -1.27% | -0.48% | 37.31% |
| momentum_26 AND volume_26 | 0.21% | -2.70% | -1.27% | -0.04% | 2.88% |
| momentum_26 + volume_26 | -1.18% | -7.04% | -1.27% | -0.36% | 27.62% |
| breakout_8 AND reversion_12 | 0.00% | 0.00% | -1.27% | -0.00% | 0.00% |
| breakout_8 + reversion_12 | 0.50% | -13.26% | -1.27% | -0.29% | 22.92% |
| breakout_8 AND volume_26 | -0.51% | -2.17% | -1.27% | -0.01% | 1.05% |
| breakout_8 + volume_26 | -1.83% | -11.81% | -1.27% | -0.17% | 13.23% |
| reversion_12 AND volume_26 | 1.32% | -2.02% | -1.27% | -0.04% | 3.40% |
| reversion_12 + volume_26 | 2.35% | -7.48% | -1.27% | -0.21% | 16.50% |
| ema_12_26 | 0.72% | -2.20% | -1.27% | -0.64% | 50.00% |
| macd_12_26_9 | 0.83% | -3.32% | -1.27% | -0.40% | 30.89% |
| rsi_14_recovery | 0.21% | -1.88% | -1.27% | -0.02% | 1.31% |
| bollinger_20_reentry | 0.66% | -4.69% | -1.27% | -0.04% | 3.40% |
| donchian_20 | -1.79% | -4.63% | -1.27% | -0.04% | 2.88% |
| atr_14_breakout | -1.59% | -8.37% | -1.27% | -0.06% | 4.71% |
| session_vwap | 1.19% | -8.52% | -1.27% | -0.60% | 47.12% |
| obv_20 | -3.51% | -14.21% | -1.27% | -0.39% | 30.10% |
| stochastic_14_3_recovery | -1.56% | -12.11% | -1.27% | -0.09% | 7.07% |
| mfi_14_recovery | 0.06% | -2.02% | -1.27% | -0.02% | 1.31% |
| adx_14_trend | -2.86% | -5.68% | -1.27% | -0.35% | 27.23% |
| aroon_25_trend | -1.12% | -5.19% | -1.27% | -0.29% | 22.51% |
| cci_20_momentum | -2.26% | -9.76% | -1.27% | -0.19% | 14.92% |
| williams_14_recovery | -2.34% | -12.81% | -1.27% | -0.09% | 7.07% |
| cmf_20_accumulation | -1.74% | -9.66% | -1.27% | -0.37% | 28.53% |
| chaikin_3_10 | 1.37% | -7.19% | -1.27% | -0.42% | 32.98% |
| roc_10_momentum | -0.98% | -3.45% | -1.27% | -0.10% | 7.85% |
| trix_15_trend | -1.25% | -8.83% | -1.27% | -0.45% | 35.08% |
| keltner_20_breakout | -1.19% | -3.65% | -1.27% | -0.05% | 3.93% |
| opening_range_30m | 0.15% | -3.16% | -1.27% | -0.22% | 16.75% |

동일 구간·초기 자금, 종료 시 청산 비용 포함. 노출 맞춤은 사후 설명용이며 v2 실제 계좌 성과가 아닙니다.
[낙폭 분해·비용 영향·전체 구간](JPM/comparison.json)

[v1 전체 기록](JPM/accounts.json) · [v2 전체 기록](JPM/accounts-v2.json)

## XOM 계좌

| 모델 | 전략 | 평가액 USD | 손익 USD | 최근 매매·이유 |
|---|---|---:|---:|---|
| v1 | cash | 10000.00 | 0.00 | 대기 /  / 새 신호 대기 |
| v1 | buy_hold | 10117.73 | 117.73 | buy /  / buy_hold: prior completed bar target 100%; next bar open simulation |
| v1 | trend_8_26 | 10062.80 | 62.80 | buy /  / trend_8_26: prior completed bar target 100%; next bar open simulation |
| v1 | momentum_26 | 10145.61 | 145.61 | buy /  / momentum_26: prior completed bar target 100%; next bar open simulation |
| v1 | breakout_8 | 9789.71 | -210.29 | buy /  / breakout_8: prior completed bar target 100%; next bar open simulation |
| v1 | reversion_12 | 9934.36 | -65.64 | sell /  / reversion_12: prior completed bar target 0%; next bar open simulation |
| v1 | volume_26 | 9889.56 | -110.44 | sell /  / volume_26: prior completed bar target 0%; next bar open simulation |
| v1 | trend_8_26 AND momentum_26 | 10062.80 | 62.80 | buy /  / trend_8_26 AND momentum_26: prior completed bar target 100%; next bar open simulation |
| v1 | trend_8_26 + momentum_26 | 10104.09 | 104.09 | buy /  / trend_8_26 + momentum_26: prior completed bar target 100%; next bar open simulation |
| v1 | trend_8_26 AND breakout_8 | 9867.04 | -132.96 | buy /  / trend_8_26 AND breakout_8: prior completed bar target 100%; next bar open simulation |
| v1 | trend_8_26 + breakout_8 | 9945.25 | -54.75 | buy /  / trend_8_26 + breakout_8: prior completed bar target 100%; next bar open simulation |
| v1 | trend_8_26 AND reversion_12 | 9921.77 | -78.23 | sell /  / trend_8_26 AND reversion_12: prior completed bar target 0%; next bar open simulation |
| v1 | trend_8_26 + reversion_12 | 9998.28 | -1.72 | buy /  / trend_8_26 + reversion_12: prior completed bar target 50%; next bar open simulation |
| v1 | trend_8_26 AND volume_26 | 9985.49 | -14.51 | sell /  / trend_8_26 AND volume_26: prior completed bar target 0%; next bar open simulation |
| v1 | trend_8_26 + volume_26 | 9975.68 | -24.32 | buy /  / trend_8_26 + volume_26: prior completed bar target 50%; next bar open simulation |
| v1 | momentum_26 AND breakout_8 | 9838.47 | -161.53 | buy /  / momentum_26 AND breakout_8: prior completed bar target 100%; next bar open simulation |
| v1 | momentum_26 + breakout_8 | 9966.16 | -33.84 | buy /  / momentum_26 + breakout_8: prior completed bar target 100%; next bar open simulation |
| v1 | momentum_26 AND reversion_12 | 9934.36 | -65.64 | sell /  / momentum_26 AND reversion_12: prior completed bar target 0%; next bar open simulation |
| v1 | momentum_26 + reversion_12 | 10039.32 | 39.32 | sell /  / momentum_26 + reversion_12: prior completed bar target 50%; next bar open simulation |
| v1 | momentum_26 AND volume_26 | 9985.49 | -14.51 | sell /  / momentum_26 AND volume_26: prior completed bar target 0%; next bar open simulation |
| v1 | momentum_26 + volume_26 | 10016.62 | 16.62 | sell /  / momentum_26 + volume_26: prior completed bar target 50%; next bar open simulation |
| v1 | breakout_8 AND reversion_12 | 10000.00 | 0.00 | 대기 /  / 새 신호 대기 |
| v1 | breakout_8 + reversion_12 | 9861.59 | -138.41 | sell /  / breakout_8 + reversion_12: prior completed bar target 50%; next bar open simulation |
| v1 | breakout_8 AND volume_26 | 9950.44 | -49.56 | sell /  / breakout_8 AND volume_26: prior completed bar target 0%; next bar open simulation |
| v1 | breakout_8 + volume_26 | 9839.36 | -160.64 | sell /  / breakout_8 + volume_26: prior completed bar target 50%; next bar open simulation |
| v1 | reversion_12 AND volume_26 | 10000.00 | 0.00 | 대기 /  / 새 신호 대기 |
| v1 | reversion_12 + volume_26 | 9911.86 | -88.14 | sell /  / reversion_12 + volume_26: prior completed bar target 0%; next bar open simulation |
| v1 | ema_12_26 | 10176.25 | 176.25 | buy /  / EMA12 > EMA26; 조건 충족; EMA12=175.145, EMA26=175.141 |
| v1 | macd_12_26_9 | 10104.16 | 104.16 | buy /  / MACD > 신호선 그리고 MACD > 0; 조건 충족; MACD=0.284963, signal9=0.263271 |
| v1 | rsi_14_recovery | 10000.00 | 0.00 | 대기 /  / 새 신호 대기 |
| v1 | bollinger_20_reentry | 9913.52 | -86.48 | sell /  / 직전 종가 < 직전 하단밴드, 현재 하단밴드 <= 종가 <= SMA20 (한 봉 목표); 조건 미충족; close=175.71, lower20=173.907, SMA20=174.743, previous_lower20=173.977 |
| v1 | donchian_20 | 9832.30 | -167.70 | sell /  / 종가 > 현재 봉을 제외한 직전 20봉 최고가; 조건 미충족; close=179.01, prior_high20=179.16 |
| v1 | atr_14_breakout | 9864.96 | -135.04 | sell /  / 종가 > 직전 종가 + 직전 ATR14 그리고 종가 > EMA26; 조건 미충족; close=177.19, threshold=177.748, prior_ATR14=0.663113, EMA26=175.734 |
| v1 | session_vwap | 10040.18 | 40.18 | buy /  / 종가 > 뉴욕 거래일별 누적 전형가격 VWAP; 조건 충족; close=178.12, session_VWAP=178.027, session_volume=4.4806e+06 |
| v1 | obv_20 | 9867.12 | -132.88 | buy /  / OBV > OBV의 SMA20 그리고 종가 > EMA26; 조건 충족; OBV=2.18423e+07, OBV_SMA20=2.18347e+07, close=177.655, EMA26=177.636 |
| v1 | stochastic_14_3_recovery | 9923.93 | -76.07 | sell /  / 직전 %K14 < 20에서 %K14가 %D3 상향 돌파 (한 봉 목표); 조건 미충족; K14=33.4559, D3=21.1148, previous_K14=20.3889, previous_D3=14.0974 |
| v1 | mfi_14_recovery | 10000.00 | 0.00 | 대기 /  / 새 신호 대기 |
| v1 | adx_14_trend | 9999.47 | -0.53 | sell /  / Wilder ADX14 >= 25 그리고 +DI14 > -DI14; 조건 미충족; ADX14=23.8302, plus_DI14=25.6436, minus_DI14=22.6035 |
| v1 | aroon_25_trend | 9929.86 | -70.14 | sell /  / Aroon25 Up > 70 그리고 Down < 30 (동률이면 최신 극값); 조건 미충족; Aroon_up=68, Aroon_down=0 |
| v1 | cci_20_momentum | 9842.10 | -157.90 | sell /  / CCI20 > 100 (전형가격·평균절대편차); 조건 미충족; CCI20=67.3071 |
| v1 | williams_14_recovery | 9838.11 | -161.89 | sell /  / 직전 Williams %R14 < -80, 현재 >= -80 (한 봉 목표); 조건 미충족; Williams_R14=-66.5441, previous_R14=-79.6111 |
| v1 | cmf_20_accumulation | 9977.80 | -22.20 | buy /  / Chaikin Money Flow20 > 0.1; 조건 충족; CMF20=0.158173, volume20=1.12043e+07 |
| v1 | chaikin_3_10 | 9920.35 | -79.65 | buy /  / ADL의 EMA3 - EMA10 > 0 그리고 종가 > EMA26; 조건 충족; Chaikin3_10=45202.2, ADL=2.7734e+07, close=177.655, EMA26=177.636 |
| v1 | roc_10_momentum | 9940.60 | -59.40 | sell /  / 10봉 ROC > 1% 그리고 종가 > EMA26; 조건 미충족; ROC10_percent=0.782107, close=178.47, EMA26=176.891 |
| v1 | trix_15_trend | 10018.82 | 18.82 | buy /  / 15봉 삼중 EMA의 1봉 변화율 TRIX > 0 그리고 종가 > EMA26; 조건 충족; TRIX15_percent=0.0352454, close=177.655, EMA26=177.636 |
| v1 | keltner_20_breakout | 9937.30 | -62.70 | sell /  / 종가 > EMA20 + 2 x Wilder ATR14; 조건 미충족; close=178.845, upper_Keltner=179.079, EMA20=177.884, ATR14=0.597175 |
| v1 | opening_range_30m | 10049.37 | 49.37 | sell /  / 뉴욕 09:30·09:45 두 완료 봉 최고가를 10:00 이후 종가가 돌파; 자료 부족·변동폭 또는 거래량 없음: 대기; close=179.01 |
| v2 | cash | 10000.00 | 0.00 | 대기 /  / 새 신호 대기 |
| v2 | buy_hold | 10440.61 | 440.61 | buy / partial / 직전 완료 봉 목표 비중 100%; 다음 봉 시가 가정 |
| v2 | trend_8_26 | 10156.61 | 156.61 | buy / partial / 직전 완료 봉 목표 비중 100%; 다음 봉 시가 가정 |
| v2 | momentum_26 | 10319.73 | 319.73 | buy / partial / 직전 완료 봉 목표 비중 100%; 다음 봉 시가 가정 |
| v2 | breakout_8 | 9257.96 | -742.04 | buy / partial / 직전 완료 봉 목표 비중 100%; 다음 봉 시가 가정 |
| v2 | reversion_12 | 9748.68 | -251.32 | sell / filled / 직전 완료 봉 목표 비중 0%; 다음 봉 시가 가정 |
| v2 | volume_26 | 9794.70 | -205.30 | sell / filled / 직전 완료 봉 목표 비중 0%; 다음 봉 시가 가정 |
| v2 | trend_8_26 AND momentum_26 | 10164.14 | 164.14 | buy / partial / 직전 완료 봉 목표 비중 100%; 다음 봉 시가 가정 |
| v2 | trend_8_26 + momentum_26 | 10237.85 | 237.85 | buy / partial / 직전 완료 봉 목표 비중 100%; 다음 봉 시가 가정 |
| v2 | trend_8_26 AND breakout_8 | 9317.78 | -682.22 | buy / partial / 직전 완료 봉 목표 비중 100%; 다음 봉 시가 가정 |
| v2 | trend_8_26 + breakout_8 | 9738.12 | -261.88 | buy / partial / 직전 완료 봉 목표 비중 100%; 다음 봉 시가 가정 |
| v2 | trend_8_26 AND reversion_12 | 9760.78 | -239.22 | sell / filled / 직전 완료 봉 목표 비중 0%; 다음 봉 시가 가정 |
| v2 | trend_8_26 + reversion_12 | 9950.55 | -49.45 | buy / filled / 직전 완료 봉 목표 비중 50%; 다음 봉 시가 가정 |
| v2 | trend_8_26 AND volume_26 | 9879.28 | -120.72 | sell / filled / 직전 완료 봉 목표 비중 0%; 다음 봉 시가 가정 |
| v2 | trend_8_26 + volume_26 | 9973.84 | -26.16 | buy / filled / 직전 완료 봉 목표 비중 50%; 다음 봉 시가 가정 |
| v2 | momentum_26 AND breakout_8 | 9305.93 | -694.07 | buy / partial / 직전 완료 봉 목표 비중 100%; 다음 봉 시가 가정 |
| v2 | momentum_26 + breakout_8 | 9775.07 | -224.93 | buy / partial / 직전 완료 봉 목표 비중 100%; 다음 봉 시가 가정 |
| v2 | momentum_26 AND reversion_12 | 9733.85 | -266.15 | sell / filled / 직전 완료 봉 목표 비중 0%; 다음 봉 시가 가정 |
| v2 | momentum_26 + reversion_12 | 10030.16 | 30.16 | sell / filled / 직전 완료 봉 목표 비중 50%; 다음 봉 시가 가정 |
| v2 | momentum_26 AND volume_26 | 9941.52 | -58.48 | sell / filled / 직전 완료 봉 목표 비중 0%; 다음 봉 시가 가정 |
| v2 | momentum_26 + volume_26 | 10074.70 | 74.70 | sell / filled / 직전 완료 봉 목표 비중 50%; 다음 봉 시가 가정 |
| v2 | breakout_8 AND reversion_12 | 10000.00 | 0.00 | 대기 /  / 새 신호 대기 |
| v2 | breakout_8 + reversion_12 | 9499.88 | -500.12 | sell / filled / 직전 완료 봉 목표 비중 50%; 다음 봉 시가 가정 |
| v2 | breakout_8 AND volume_26 | 9918.86 | -81.14 | sell / filled / 직전 완료 봉 목표 비중 0%; 다음 봉 시가 가정 |
| v2 | breakout_8 + volume_26 | 9542.31 | -457.69 | sell / filled / 직전 완료 봉 목표 비중 50%; 다음 봉 시가 가정 |
| v2 | reversion_12 AND volume_26 | 9949.87 | -50.13 | sell / filled / 직전 완료 봉 목표 비중 0%; 다음 봉 시가 가정 |
| v2 | reversion_12 + volume_26 | 9792.16 | -207.84 | sell / filled / 직전 완료 봉 목표 비중 0%; 다음 봉 시가 가정 |
| v2 | ema_12_26 | 10175.24 | 175.24 | buy / partial / EMA12 > EMA26; 조건 충족; EMA12=175.145, EMA26=175.141; 직전 완료 봉 목표를 다음 봉 시가에 모의 적용 |
| v2 | macd_12_26_9 | 10101.13 | 101.13 | buy / partial / MACD > 신호선 그리고 MACD > 0; 조건 충족; MACD=0.284963, signal9=0.263271; 직전 완료 봉 목표를 다음 봉 시가에 모의 적용 |
| v2 | rsi_14_recovery | 10000.00 | 0.00 | 대기 /  / 새 신호 대기 |
| v2 | bollinger_20_reentry | 9911.54 | -88.46 | sell / filled / 직전 종가 < 직전 하단밴드, 현재 하단밴드 <= 종가 <= SMA20 (한 봉 목표); 조건 미충족; close=175.71, lower20=173.907, SMA20=174.743, previous_lower20=173.977; 직전 완료 봉 목표를 다음 봉 시가에 모의 적용 |
| v2 | donchian_20 | 9824.43 | -175.57 | sell / filled / 종가 > 현재 봉을 제외한 직전 20봉 최고가; 조건 미충족; close=179.01, prior_high20=179.16; 직전 완료 봉 목표를 다음 봉 시가에 모의 적용 |
| v2 | atr_14_breakout | 9859.04 | -140.96 | sell / filled / 종가 > 직전 종가 + 직전 ATR14 그리고 종가 > EMA26; 조건 미충족; close=177.19, threshold=177.748, prior_ATR14=0.663113, EMA26=175.734; 직전 완료 봉 목표를 다음 봉 시가에 모의 적용 |
| v2 | session_vwap | 10035.16 | 35.16 | buy / partial / 종가 > 뉴욕 거래일별 누적 전형가격 VWAP; 조건 충족; close=178.12, session_VWAP=178.027, session_volume=4.4806e+06; 직전 완료 봉 목표를 다음 봉 시가에 모의 적용 |
| v2 | obv_20 | 9860.21 | -139.79 | buy / partial / OBV > OBV의 SMA20 그리고 종가 > EMA26; 조건 충족; OBV=2.18423e+07, OBV_SMA20=2.18347e+07, close=177.655, EMA26=177.636; 직전 완료 봉 목표를 다음 봉 시가에 모의 적용 |
| v2 | stochastic_14_3_recovery | 9919.96 | -80.04 | sell / filled / 직전 %K14 < 20에서 %K14가 %D3 상향 돌파 (한 봉 목표); 조건 미충족; K14=33.4559, D3=21.1148, previous_K14=20.3889, previous_D3=14.0974; 직전 완료 봉 목표를 다음 봉 시가에 모의 적용 |
| v2 | mfi_14_recovery | 10000.00 | 0.00 | 대기 /  / 새 신호 대기 |
| v2 | adx_14_trend | 9993.47 | -6.53 | sell / filled / Wilder ADX14 >= 25 그리고 +DI14 > -DI14; 조건 미충족; ADX14=23.8302, plus_DI14=25.6436, minus_DI14=22.6035; 직전 완료 봉 목표를 다음 봉 시가에 모의 적용 |
| v2 | aroon_25_trend | 9927.87 | -72.13 | sell / filled / Aroon25 Up > 70 그리고 Down < 30 (동률이면 최신 극값); 조건 미충족; Aroon_up=68, Aroon_down=0; 직전 완료 봉 목표를 다음 봉 시가에 모의 적용 |
| v2 | cci_20_momentum | 9832.27 | -167.73 | sell / filled / CCI20 > 100 (전형가격·평균절대편차); 조건 미충족; CCI20=67.3071; 직전 완료 봉 목표를 다음 봉 시가에 모의 적용 |
| v2 | williams_14_recovery | 9832.21 | -167.79 | sell / filled / 직전 Williams %R14 < -80, 현재 >= -80 (한 봉 목표); 조건 미충족; Williams_R14=-66.5441, previous_R14=-79.6111; 직전 완료 봉 목표를 다음 봉 시가에 모의 적용 |
| v2 | cmf_20_accumulation | 9976.80 | -23.20 | buy / partial / Chaikin Money Flow20 > 0.1; 조건 충족; CMF20=0.158173, volume20=1.12043e+07; 직전 완료 봉 목표를 다음 봉 시가에 모의 적용 |
| v2 | chaikin_3_10 | 9915.39 | -84.61 | buy / partial / ADL의 EMA3 - EMA10 > 0 그리고 종가 > EMA26; 조건 충족; Chaikin3_10=45202.2, ADL=2.7734e+07, close=177.655, EMA26=177.636; 직전 완료 봉 목표를 다음 봉 시가에 모의 적용 |
| v2 | roc_10_momentum | 9934.64 | -65.36 | sell / filled / 10봉 ROC > 1% 그리고 종가 > EMA26; 조건 미충족; ROC10_percent=0.782107, close=178.47, EMA26=176.891; 직전 완료 봉 목표를 다음 봉 시가에 모의 적용 |
| v2 | trix_15_trend | 10013.82 | 13.82 | buy / partial / 15봉 삼중 EMA의 1봉 변화율 TRIX > 0 그리고 종가 > EMA26; 조건 충족; TRIX15_percent=0.0352454, close=177.655, EMA26=177.636; 직전 완료 봉 목표를 다음 봉 시가에 모의 적용 |
| v2 | keltner_20_breakout | 9931.34 | -68.66 | sell / filled / 종가 > EMA20 + 2 x Wilder ATR14; 조건 미충족; close=178.845, upper_Keltner=179.079, EMA20=177.884, ATR14=0.597175; 직전 완료 봉 목표를 다음 봉 시가에 모의 적용 |
| v2 | opening_range_30m | 10047.36 | 47.36 | sell / filled / 뉴욕 09:30·09:45 두 완료 봉 최고가를 10:00 이후 종가가 돌파; 자료 부족·변동폭 또는 거래량 없음: 대기; close=179.01; 직전 완료 봉 목표를 다음 봉 시가에 모의 적용 |

### 같은 기간의 비용·노출 비교 (사후 연구)

| 전략 | 비용 전 | 비용 후 | 100% 보유 | 같은 평균 노출 보유 | 평균 노출 |
|---|---:|---:|---:|---:|---:|
| cash | 0.00% | 0.00% | 10.95% | 0.00% | 0.00% |
| buy_hold | 11.42% | 10.95% | 10.95% | 10.95% | 100.00% |
| trend_8_26 | 2.92% | -1.72% | 10.95% | 7.11% | 65.97% |
| momentum_26 | 3.59% | -3.55% | 10.95% | 7.81% | 72.25% |
| breakout_8 | -0.36% | -19.24% | 10.95% | 2.88% | 27.23% |
| reversion_12 | 5.55% | -4.57% | 10.95% | 2.29% | 21.73% |
| volume_26 | 3.26% | -3.86% | 10.95% | 0.49% | 4.71% |
| trend_8_26 AND momentum_26 | 1.44% | -3.54% | 10.95% | 6.53% | 60.73% |
| trend_8_26 + momentum_26 | 3.26% | -2.43% | 10.95% | 7.46% | 69.11% |
| trend_8_26 AND breakout_8 | -0.18% | -15.62% | 10.95% | 2.26% | 21.47% |
| trend_8_26 + breakout_8 | 1.29% | -10.52% | 10.95% | 4.98% | 46.60% |
| trend_8_26 AND reversion_12 | 0.37% | -4.96% | 10.95% | 0.93% | 8.90% |
| trend_8_26 + reversion_12 | 4.26% | -2.95% | 10.95% | 4.68% | 43.85% |
| trend_8_26 AND volume_26 | 2.37% | -1.84% | 10.95% | 0.27% | 2.62% |
| trend_8_26 + volume_26 | 3.11% | -2.60% | 10.95% | 3.75% | 35.34% |
| momentum_26 AND breakout_8 | -0.48% | -17.97% | 10.95% | 2.68% | 25.39% |
| momentum_26 + breakout_8 | 1.62% | -11.72% | 10.95% | 5.32% | 49.75% |
| momentum_26 AND reversion_12 | 0.87% | -5.29% | 10.95% | 1.04% | 9.95% |
| momentum_26 + reversion_12 | 4.59% | -2.84% | 10.95% | 5.02% | 46.99% |
| momentum_26 AND volume_26 | 2.15% | -1.64% | 10.95% | 0.25% | 2.36% |
| momentum_26 + volume_26 | 3.45% | -2.48% | 10.95% | 4.09% | 38.49% |
| breakout_8 AND reversion_12 | 0.00% | 0.00% | 10.95% | 0.00% | 0.00% |
| breakout_8 + reversion_12 | 2.57% | -12.03% | 10.95% | 2.59% | 24.49% |
| breakout_8 AND volume_26 | 0.51% | -1.17% | 10.95% | 0.11% | 1.05% |
| breakout_8 + volume_26 | 1.44% | -10.95% | 10.95% | 1.68% | 15.98% |
| reversion_12 AND volume_26 | 1.10% | -1.00% | 10.95% | 0.14% | 1.31% |
| reversion_12 + volume_26 | 4.41% | -3.41% | 10.95% | 1.39% | 13.22% |
| ema_12_26 | 3.03% | 0.05% | 10.95% | 8.25% | 76.18% |
| macd_12_26_9 | 0.49% | -5.25% | 10.95% | 4.46% | 41.88% |
| rsi_14_recovery | -0.15% | -0.57% | 10.95% | 0.03% | 0.26% |
| bollinger_20_reentry | -0.87% | -3.75% | 10.95% | 0.19% | 1.83% |
| donchian_20 | -0.93% | -10.43% | 10.95% | 1.02% | 9.69% |
| atr_14_breakout | 0.47% | -8.01% | 10.95% | 0.60% | 5.76% |
| session_vwap | 2.47% | -8.90% | 10.95% | 7.40% | 68.59% |
| obv_20 | 2.23% | -6.00% | 10.95% | 5.06% | 47.38% |
| stochastic_14_3_recovery | 1.68% | -6.90% | 10.95% | 0.58% | 5.50% |
| mfi_14_recovery | -0.31% | -1.97% | 10.95% | 0.11% | 1.05% |
| adx_14_trend | 3.88% | 0.87% | 10.95% | 4.72% | 44.24% |
| aroon_25_trend | -2.08% | -8.44% | 10.95% | 3.75% | 35.34% |
| cci_20_momentum | 3.75% | -4.61% | 10.95% | 3.02% | 28.53% |
| williams_14_recovery | 0.21% | -5.51% | 10.95% | 0.38% | 3.66% |
| cmf_20_accumulation | 1.22% | -5.36% | 10.95% | 5.72% | 53.40% |
| chaikin_3_10 | 0.71% | -8.18% | 10.95% | 6.33% | 58.90% |
| roc_10_momentum | 0.80% | -5.36% | 10.95% | 1.37% | 13.09% |
| trix_15_trend | 1.42% | -4.77% | 10.95% | 6.99% | 64.92% |
| keltner_20_breakout | 0.18% | -6.72% | 10.95% | 1.82% | 17.28% |
| opening_range_30m | 0.54% | -9.10% | 10.95% | 4.15% | 39.01% |

동일 구간·초기 자금, 종료 시 청산 비용 포함. 노출 맞춤은 사후 설명용이며 v2 실제 계좌 성과가 아닙니다.
[낙폭 분해·비용 영향·전체 구간](XOM/comparison.json)

[v1 전체 기록](XOM/accounts.json) · [v2 전체 기록](XOM/accounts-v2.json)

## JNJ 계좌

| 모델 | 전략 | 평가액 USD | 손익 USD | 최근 매매·이유 |
|---|---|---:|---:|---|
| v1 | cash | 10000.00 | 0.00 | 대기 /  / 새 신호 대기 |
| v1 | buy_hold | 9932.97 | -67.03 | buy /  / buy_hold: prior completed bar target 100%; next bar open simulation |
| v1 | trend_8_26 | 9903.43 | -96.57 | sell /  / trend_8_26: prior completed bar target 0%; next bar open simulation |
| v1 | momentum_26 | 9898.09 | -101.91 | sell /  / momentum_26: prior completed bar target 0%; next bar open simulation |
| v1 | breakout_8 | 9653.64 | -346.36 | buy /  / breakout_8: prior completed bar target 100%; next bar open simulation |
| v1 | reversion_12 | 9891.56 | -108.44 | sell /  / reversion_12: prior completed bar target 0%; next bar open simulation |
| v1 | volume_26 | 9884.71 | -115.29 | sell /  / volume_26: prior completed bar target 0%; next bar open simulation |
| v1 | trend_8_26 AND momentum_26 | 9950.33 | -49.67 | sell /  / trend_8_26 AND momentum_26: prior completed bar target 0%; next bar open simulation |
| v1 | trend_8_26 + momentum_26 | 9900.74 | -99.26 | sell /  / trend_8_26 + momentum_26: prior completed bar target 0%; next bar open simulation |
| v1 | trend_8_26 AND breakout_8 | 9937.40 | -62.60 | sell /  / trend_8_26 AND breakout_8: prior completed bar target 0%; next bar open simulation |
| v1 | trend_8_26 + breakout_8 | 9777.66 | -222.34 | sell /  / trend_8_26 + breakout_8: prior completed bar target 50%; next bar open simulation |
| v1 | trend_8_26 AND reversion_12 | 9992.01 | -7.99 | sell /  / trend_8_26 AND reversion_12: prior completed bar target 0%; next bar open simulation |
| v1 | trend_8_26 + reversion_12 | 9897.42 | -102.58 | sell /  / trend_8_26 + reversion_12: prior completed bar target 0%; next bar open simulation |
| v1 | trend_8_26 AND volume_26 | 9935.63 | -64.37 | sell /  / trend_8_26 AND volume_26: prior completed bar target 0%; next bar open simulation |
| v1 | trend_8_26 + volume_26 | 9894.03 | -105.97 | sell /  / trend_8_26 + volume_26: prior completed bar target 0%; next bar open simulation |
| v1 | momentum_26 AND breakout_8 | 9911.77 | -88.23 | sell /  / momentum_26 AND breakout_8: prior completed bar target 0%; next bar open simulation |
| v1 | momentum_26 + breakout_8 | 9774.99 | -225.01 | sell /  / momentum_26 + breakout_8: prior completed bar target 50%; next bar open simulation |
| v1 | momentum_26 AND reversion_12 | 10000.00 | 0.00 | 대기 /  / 새 신호 대기 |
| v1 | momentum_26 + reversion_12 | 9914.55 | -85.45 | sell /  / momentum_26 + reversion_12: prior completed bar target 0%; next bar open simulation |
| v1 | momentum_26 AND volume_26 | 10000.00 | 0.00 | 대기 /  / 새 신호 대기 |
| v1 | momentum_26 + volume_26 | 9911.13 | -88.87 | sell /  / momentum_26 + volume_26: prior completed bar target 0%; next bar open simulation |
| v1 | breakout_8 AND reversion_12 | 10000.00 | 0.00 | 대기 /  / 새 신호 대기 |
| v1 | breakout_8 + reversion_12 | 9771.72 | -228.28 | sell /  / breakout_8 + reversion_12: prior completed bar target 50%; next bar open simulation |
| v1 | breakout_8 AND volume_26 | 10000.00 | 0.00 | 대기 /  / 새 신호 대기 |
| v1 | breakout_8 + volume_26 | 9768.35 | -231.65 | sell /  / breakout_8 + volume_26: prior completed bar target 50%; next bar open simulation |
| v1 | reversion_12 AND volume_26 | 9974.59 | -25.41 | sell /  / reversion_12 AND volume_26: prior completed bar target 0%; next bar open simulation |
| v1 | reversion_12 + volume_26 | 9907.87 | -92.13 | sell /  / reversion_12 + volume_26: prior completed bar target 0%; next bar open simulation |
| v1 | ema_12_26 | 9781.22 | -218.78 | sell /  / EMA12 > EMA26; 조건 미충족; EMA12=255.193, EMA26=255.284 |
| v1 | macd_12_26_9 | 9756.47 | -243.53 | sell /  / MACD > 신호선 그리고 MACD > 0; 조건 미충족; MACD=-0.0912606, signal9=-0.0161084 |
| v1 | rsi_14_recovery | 9923.04 | -76.96 | sell /  / 직전 RSI14 < 30, 현재 RSI14 >= 30 (한 봉 목표); 조건 미충족; RSI14=40.3665, previous_RSI14=36.2025 |
| v1 | bollinger_20_reentry | 9881.04 | -118.96 | sell /  / 직전 종가 < 직전 하단밴드, 현재 하단밴드 <= 종가 <= SMA20 (한 봉 목표); 조건 미충족; close=251.75, lower20=251.316, SMA20=254.208, previous_lower20=251.691 |
| v1 | donchian_20 | 10000.00 | 0.00 | 대기 /  / 새 신호 대기 |
| v1 | atr_14_breakout | 9883.97 | -116.03 | sell /  / 종가 > 직전 종가 + 직전 ATR14 그리고 종가 > EMA26; 조건 미충족; close=256.72, threshold=258.136, prior_ATR14=1.3158, EMA26=255.146 |
| v1 | session_vwap | 9768.72 | -231.28 | buy /  / 종가 > 뉴욕 거래일별 누적 전형가격 VWAP; 조건 충족; close=252.75, session_VWAP=252.657, session_volume=4.65844e+06 |
| v1 | obv_20 | 9668.29 | -331.71 | buy /  / OBV > OBV의 SMA20 그리고 종가 > EMA26; 조건 충족; OBV=4.74226e+06, OBV_SMA20=3.3149e+06, close=254.07, EMA26=253.729 |
| v1 | stochastic_14_3_recovery | 9862.87 | -137.13 | sell /  / 직전 %K14 < 20에서 %K14가 %D3 상향 돌파 (한 봉 목표); 조건 미충족; K14=28.9392, D3=18.1738, previous_K14=19.7943, previous_D3=12.6561 |
| v1 | mfi_14_recovery | 10000.00 | 0.00 | 대기 /  / 새 신호 대기 |
| v1 | adx_14_trend | 9823.79 | -176.21 | sell /  / Wilder ADX14 >= 25 그리고 +DI14 > -DI14; 조건 미충족; ADX14=24.7842, plus_DI14=27.3963, minus_DI14=19.1477 |
| v1 | aroon_25_trend | 9967.50 | -32.50 | sell /  / Aroon25 Up > 70 그리고 Down < 30 (동률이면 최신 극값); 조건 미충족; Aroon_up=68, Aroon_down=16 |
| v1 | cci_20_momentum | 9935.63 | -64.37 | sell /  / CCI20 > 100 (전형가격·평균절대편차); 조건 미충족; CCI20=62.9489 |
| v1 | williams_14_recovery | 9903.67 | -96.33 | sell /  / 직전 Williams %R14 < -80, 현재 >= -80 (한 봉 목표); 조건 미충족; Williams_R14=-61.3372, previous_R14=-71.0608 |
| v1 | cmf_20_accumulation | 10057.54 | 57.54 | buy /  / Chaikin Money Flow20 > 0.1; 조건 충족; CMF20=0.280188, volume20=5.69706e+06 |
| v1 | chaikin_3_10 | 9887.07 | -112.93 | buy /  / ADL의 EMA3 - EMA10 > 0 그리고 종가 > EMA26; 조건 충족; Chaikin3_10=495361, ADL=4.44077e+06, close=254.07, EMA26=253.729 |
| v1 | roc_10_momentum | 9816.66 | -183.34 | sell /  / 10봉 ROC > 1% 그리고 종가 > EMA26; 조건 미충족; ROC10_percent=-0.398319, close=255.08, EMA26=255.591 |
| v1 | trix_15_trend | 9840.00 | -160.00 | sell /  / 15봉 삼중 EMA의 1봉 변화율 TRIX > 0 그리고 종가 > EMA26; 조건 미충족; TRIX15_percent=0.000692295, close=255.155, EMA26=255.356 |
| v1 | keltner_20_breakout | 10000.00 | 0.00 | 대기 /  / 새 신호 대기 |
| v1 | opening_range_30m | 10000.00 | 0.00 | 대기 /  / 새 신호 대기 |
| v2 | cash | 10000.00 | 0.00 | 대기 /  / 새 신호 대기 |
| v2 | buy_hold | 9701.14 | -298.86 | 중단: 손실 한도 / buy / partial / 직전 완료 봉 목표 비중 100%; 다음 봉 시가 가정 |
| v2 | trend_8_26 | 9701.14 | -298.86 | 중단: 손실 한도 / buy / partial / 직전 완료 봉 목표 비중 100%; 다음 봉 시가 가정 |
| v2 | momentum_26 | 9701.14 | -298.86 | 중단: 손실 한도 / buy / partial / 직전 완료 봉 목표 비중 100%; 다음 봉 시가 가정 |
| v2 | breakout_8 | 9343.39 | -656.61 | 중단: 손실 한도 / sell / filled / 직전 완료 봉 목표 비중 0%; 다음 봉 시가 가정 |
| v2 | reversion_12 | 9581.23 | -418.77 | sell / filled / 직전 완료 봉 목표 비중 0%; 다음 봉 시가 가정 |
| v2 | volume_26 | 9672.67 | -327.33 | sell / filled / 직전 완료 봉 목표 비중 0%; 다음 봉 시가 가정 |
| v2 | trend_8_26 AND momentum_26 | 9701.14 | -298.86 | 중단: 손실 한도 / buy / partial / 직전 완료 봉 목표 비중 100%; 다음 봉 시가 가정 |
| v2 | trend_8_26 + momentum_26 | 9701.14 | -298.86 | 중단: 손실 한도 / buy / partial / 직전 완료 봉 목표 비중 100%; 다음 봉 시가 가정 |
| v2 | trend_8_26 AND breakout_8 | 9419.39 | -580.61 | 중단: 손실 한도 / sell / filled / 직전 완료 봉 목표 비중 0%; 다음 봉 시가 가정 |
| v2 | trend_8_26 + breakout_8 | 9350.01 | -649.99 | sell / filled / 직전 완료 봉 목표 비중 50%; 다음 봉 시가 가정 |
| v2 | trend_8_26 AND reversion_12 | 9968.12 | -31.88 | sell / filled / 직전 완료 봉 목표 비중 0%; 다음 봉 시가 가정 |
| v2 | trend_8_26 + reversion_12 | 9732.92 | -267.08 | 중단: 손실 한도 / sell / filled / 직전 완료 봉 목표 비중 0%; 다음 봉 시가 가정 |
| v2 | trend_8_26 AND volume_26 | 9805.21 | -194.79 | sell / filled / 직전 완료 봉 목표 비중 0%; 다음 봉 시가 가정 |
| v2 | trend_8_26 + volume_26 | 9823.37 | -176.63 | 중단: 손실 한도 / buy / filled / 직전 완료 봉 목표 비중 50%; 다음 봉 시가 가정 |
| v2 | momentum_26 AND breakout_8 | 9512.11 | -487.89 | sell / filled / 직전 완료 봉 목표 비중 0%; 다음 봉 시가 가정 |
| v2 | momentum_26 + breakout_8 | 9338.68 | -661.32 | sell / filled / 직전 완료 봉 목표 비중 50%; 다음 봉 시가 가정 |
| v2 | momentum_26 AND reversion_12 | 9938.87 | -61.13 | sell / filled / 직전 완료 봉 목표 비중 0%; 다음 봉 시가 가정 |
| v2 | momentum_26 + reversion_12 | 9732.92 | -267.08 | 중단: 손실 한도 / sell / filled / 직전 완료 봉 목표 비중 0%; 다음 봉 시가 가정 |
| v2 | momentum_26 AND volume_26 | 9920.93 | -79.07 | sell / filled / 직전 완료 봉 목표 비중 0%; 다음 봉 시가 가정 |
| v2 | momentum_26 + volume_26 | 9823.37 | -176.63 | 중단: 손실 한도 / buy / filled / 직전 완료 봉 목표 비중 50%; 다음 봉 시가 가정 |
| v2 | breakout_8 AND reversion_12 | 10000.00 | 0.00 | 대기 /  / 새 신호 대기 |
| v2 | breakout_8 + reversion_12 | 9354.39 | -645.61 | sell / filled / 직전 완료 봉 목표 비중 50%; 다음 봉 시가 가정 |
| v2 | breakout_8 AND volume_26 | 9814.17 | -185.83 | sell / filled / 직전 완료 봉 목표 비중 0%; 다음 봉 시가 가정 |
| v2 | breakout_8 + volume_26 | 9379.13 | -620.87 | sell / filled / 직전 완료 봉 목표 비중 50%; 다음 봉 시가 가정 |
| v2 | reversion_12 AND volume_26 | 9859.15 | -140.85 | sell / filled / 직전 완료 봉 목표 비중 0%; 다음 봉 시가 가정 |
| v2 | reversion_12 + volume_26 | 9667.54 | -332.46 | sell / filled / 직전 완료 봉 목표 비중 0%; 다음 봉 시가 가정 |
| v2 | ema_12_26 | 9777.31 | -222.69 | sell / filled / EMA12 > EMA26; 조건 미충족; EMA12=255.193, EMA26=255.284; 직전 완료 봉 목표를 다음 봉 시가에 모의 적용 |
| v2 | macd_12_26_9 | 9752.57 | -247.43 | sell / filled / MACD > 신호선 그리고 MACD > 0; 조건 미충족; MACD=-0.0912606, signal9=-0.0161084; 직전 완료 봉 목표를 다음 봉 시가에 모의 적용 |
| v2 | rsi_14_recovery | 9919.07 | -80.93 | sell / filled / 직전 RSI14 < 30, 현재 RSI14 >= 30 (한 봉 목표); 조건 미충족; RSI14=40.3665, previous_RSI14=36.2025; 직전 완료 봉 목표를 다음 봉 시가에 모의 적용 |
| v2 | bollinger_20_reentry | 9877.09 | -122.91 | sell / filled / 직전 종가 < 직전 하단밴드, 현재 하단밴드 <= 종가 <= SMA20 (한 봉 목표); 조건 미충족; close=251.75, lower20=251.316, SMA20=254.208, previous_lower20=251.691; 직전 완료 봉 목표를 다음 봉 시가에 모의 적용 |
| v2 | donchian_20 | 10000.00 | 0.00 | 대기 /  / 새 신호 대기 |
| v2 | atr_14_breakout | 9880.02 | -119.98 | sell / filled / 종가 > 직전 종가 + 직전 ATR14 그리고 종가 > EMA26; 조건 미충족; close=256.72, threshold=258.136, prior_ATR14=1.3158, EMA26=255.146; 직전 완료 봉 목표를 다음 봉 시가에 모의 적용 |
| v2 | session_vwap | 9759.94 | -240.06 | buy / partial / 종가 > 뉴욕 거래일별 누적 전형가격 VWAP; 조건 충족; close=252.75, session_VWAP=252.657, session_volume=4.65844e+06; 직전 완료 봉 목표를 다음 봉 시가에 모의 적용 |
| v2 | obv_20 | 9657.66 | -342.34 | buy / partial / OBV > OBV의 SMA20 그리고 종가 > EMA26; 조건 충족; OBV=4.74226e+06, OBV_SMA20=3.3149e+06, close=254.07, EMA26=253.729; 직전 완료 봉 목표를 다음 봉 시가에 모의 적용 |
| v2 | stochastic_14_3_recovery | 9856.96 | -143.04 | sell / filled / 직전 %K14 < 20에서 %K14가 %D3 상향 돌파 (한 봉 목표); 조건 미충족; K14=28.9392, D3=18.1738, previous_K14=19.7943, previous_D3=12.6561; 직전 완료 봉 목표를 다음 봉 시가에 모의 적용 |
| v2 | mfi_14_recovery | 10000.00 | 0.00 | 대기 /  / 새 신호 대기 |
| v2 | adx_14_trend | 9817.90 | -182.10 | sell / filled / Wilder ADX14 >= 25 그리고 +DI14 > -DI14; 조건 미충족; ADX14=24.7842, plus_DI14=27.3963, minus_DI14=19.1477; 직전 완료 봉 목표를 다음 봉 시가에 모의 적용 |
| v2 | aroon_25_trend | 9965.51 | -34.49 | sell / filled / Aroon25 Up > 70 그리고 Down < 30 (동률이면 최신 극값); 조건 미충족; Aroon_up=68, Aroon_down=16; 직전 완료 봉 목표를 다음 봉 시가에 모의 적용 |
| v2 | cci_20_momentum | 9933.64 | -66.36 | sell / filled / CCI20 > 100 (전형가격·평균절대편차); 조건 미충족; CCI20=62.9489; 직전 완료 봉 목표를 다음 봉 시가에 모의 적용 |
| v2 | williams_14_recovery | 9899.71 | -100.29 | sell / filled / 직전 Williams %R14 < -80, 현재 >= -80 (한 봉 목표); 조건 미충족; Williams_R14=-61.3372, previous_R14=-71.0608; 직전 완료 봉 목표를 다음 봉 시가에 모의 적용 |
| v2 | cmf_20_accumulation | 10056.54 | 56.54 | buy / partial / Chaikin Money Flow20 > 0.1; 조건 충족; CMF20=0.280188, volume20=5.69706e+06; 직전 완료 봉 목표를 다음 봉 시가에 모의 적용 |
| v2 | chaikin_3_10 | 9882.13 | -117.87 | buy / partial / ADL의 EMA3 - EMA10 > 0 그리고 종가 > EMA26; 조건 충족; Chaikin3_10=495361, ADL=4.44077e+06, close=254.07, EMA26=253.729; 직전 완료 봉 목표를 다음 봉 시가에 모의 적용 |
| v2 | roc_10_momentum | 9812.74 | -187.26 | sell / filled / 10봉 ROC > 1% 그리고 종가 > EMA26; 조건 미충족; ROC10_percent=-0.398319, close=255.08, EMA26=255.591; 직전 완료 봉 목표를 다음 봉 시가에 모의 적용 |
| v2 | trix_15_trend | 9836.06 | -163.94 | sell / filled / 15봉 삼중 EMA의 1봉 변화율 TRIX > 0 그리고 종가 > EMA26; 조건 미충족; TRIX15_percent=0.000692295, close=255.155, EMA26=255.356; 직전 완료 봉 목표를 다음 봉 시가에 모의 적용 |
| v2 | keltner_20_breakout | 10000.00 | 0.00 | 대기 /  / 새 신호 대기 |
| v2 | opening_range_30m | 10000.00 | 0.00 | 대기 /  / 새 신호 대기 |

### 같은 기간의 비용·노출 비교 (사후 연구)

| 전략 | 비용 전 | 비용 후 | 100% 보유 | 같은 평균 노출 보유 | 평균 노출 |
|---|---:|---:|---:|---:|---:|
| cash | 0.00% | 0.00% | -6.37% | -0.00% | 0.00% |
| buy_hold | -5.97% | -6.37% | -6.37% | -6.37% | 100.00% |
| trend_8_26 | 1.32% | -0.79% | -6.37% | -2.86% | 43.72% |
| momentum_26 | 0.22% | -3.09% | -6.37% | -2.81% | 42.93% |
| breakout_8 | -1.23% | -18.24% | -6.37% | -1.32% | 19.90% |
| reversion_12 | -8.25% | -16.00% | -6.37% | -2.07% | 31.41% |
| volume_26 | -1.90% | -8.28% | -6.37% | -0.42% | 6.28% |
| trend_8_26 AND momentum_26 | 1.48% | -1.46% | -6.37% | -2.48% | 37.70% |
| trend_8_26 + momentum_26 | 0.77% | -1.95% | -6.37% | -2.84% | 43.33% |
| trend_8_26 AND breakout_8 | 0.57% | -10.59% | -6.37% | -0.87% | 13.09% |
| trend_8_26 + breakout_8 | 0.06% | -9.91% | -6.37% | -2.10% | 31.81% |
| trend_8_26 AND reversion_12 | 0.87% | -2.05% | -6.37% | -0.35% | 5.24% |
| trend_8_26 + reversion_12 | -3.55% | -8.32% | -6.37% | -2.47% | 37.57% |
| trend_8_26 AND volume_26 | 0.41% | -1.67% | -6.37% | -0.09% | 1.31% |
| trend_8_26 + volume_26 | -0.27% | -4.39% | -6.37% | -1.65% | 25.00% |
| momentum_26 AND breakout_8 | 1.38% | -9.11% | -6.37% | -0.84% | 12.57% |
| momentum_26 + breakout_8 | -0.48% | -10.78% | -6.37% | -2.07% | 31.42% |
| momentum_26 AND reversion_12 | -0.82% | -2.88% | -6.37% | -0.37% | 5.50% |
| momentum_26 + reversion_12 | -4.08% | -9.20% | -6.37% | -2.44% | 37.18% |
| momentum_26 AND volume_26 | 0.14% | -0.70% | -6.37% | -0.04% | 0.52% |
| momentum_26 + volume_26 | -0.82% | -4.91% | -6.37% | -1.63% | 24.61% |
| breakout_8 AND reversion_12 | 0.00% | 0.00% | -6.37% | -0.00% | 0.00% |
| breakout_8 + reversion_12 | -4.78% | -16.60% | -6.37% | -1.70% | 25.66% |
| breakout_8 AND volume_26 | -0.91% | -2.15% | -6.37% | -0.05% | 0.79% |
| breakout_8 + volume_26 | -1.56% | -12.67% | -6.37% | -0.87% | 13.10% |
| reversion_12 AND volume_26 | -1.84% | -4.69% | -6.37% | -0.19% | 2.88% |
| reversion_12 + volume_26 | -5.12% | -11.48% | -6.37% | -1.25% | 18.85% |
| ema_12_26 | -1.34% | -3.39% | -6.37% | -2.49% | 37.96% |
| macd_12_26_9 | 4.01% | 1.42% | -6.37% | -1.65% | 24.87% |
| rsi_14_recovery | -1.66% | -7.67% | -6.37% | -0.26% | 3.93% |
| bollinger_20_reentry | -0.95% | -5.82% | -6.37% | -0.21% | 3.14% |
| donchian_20 | 0.63% | -6.31% | -6.37% | -0.44% | 6.54% |
| atr_14_breakout | 1.19% | -4.59% | -6.37% | -0.30% | 4.45% |
| session_vwap | 1.37% | -6.41% | -6.37% | -2.97% | 45.29% |
| obv_20 | -5.86% | -14.53% | -6.37% | -1.92% | 29.06% |
| stochastic_14_3_recovery | -0.24% | -12.79% | -6.37% | -0.56% | 8.38% |
| mfi_14_recovery | 0.33% | -0.93% | -6.37% | -0.05% | 0.79% |
| adx_14_trend | -2.56% | -7.35% | -6.37% | -2.05% | 31.15% |
| aroon_25_trend | 4.10% | 0.24% | -6.37% | -1.80% | 27.23% |
| cci_20_momentum | 0.59% | -5.56% | -6.37% | -1.32% | 19.90% |
| williams_14_recovery | -1.77% | -10.06% | -6.37% | -0.37% | 5.50% |
| cmf_20_accumulation | 3.35% | -0.48% | -6.37% | -1.70% | 25.65% |
| chaikin_3_10 | -3.25% | -8.01% | -6.37% | -2.00% | 30.37% |
| roc_10_momentum | -2.32% | -8.29% | -6.37% | -0.98% | 14.66% |
| trix_15_trend | -0.23% | -2.31% | -6.37% | -1.90% | 28.80% |
| keltner_20_breakout | 0.65% | -2.68% | -6.37% | -0.61% | 9.16% |
| opening_range_30m | 0.79% | -2.95% | -6.37% | -1.71% | 25.92% |

동일 구간·초기 자금, 종료 시 청산 비용 포함. 노출 맞춤은 사후 설명용이며 v2 실제 계좌 성과가 아닙니다.
[낙폭 분해·비용 영향·전체 구간](JNJ/comparison.json)

[v1 전체 기록](JNJ/accounts.json) · [v2 전체 기록](JNJ/accounts-v2.json)

## CAT 계좌

| 모델 | 전략 | 평가액 USD | 손익 USD | 최근 매매·이유 |
|---|---|---:|---:|---|
| v1 | cash | 10000.00 | 0.00 | 대기 /  / 새 신호 대기 |
| v1 | buy_hold | 9899.30 | -100.70 | buy /  / buy_hold: prior completed bar target 100%; next bar open simulation |
| v1 | trend_8_26 | 9909.54 | -90.46 | sell /  / trend_8_26: prior completed bar target 0%; next bar open simulation |
| v1 | momentum_26 | 9872.70 | -127.30 | sell /  / momentum_26: prior completed bar target 0%; next bar open simulation |
| v1 | breakout_8 | 9790.00 | -210.00 | sell /  / breakout_8: prior completed bar target 0%; next bar open simulation |
| v1 | reversion_12 | 9852.23 | -147.77 | buy /  / reversion_12: prior completed bar target 100%; next bar open simulation |
| v1 | volume_26 | 10000.00 | 0.00 | 대기 /  / 새 신호 대기 |
| v1 | trend_8_26 AND momentum_26 | 9873.91 | -126.09 | sell /  / trend_8_26 AND momentum_26: prior completed bar target 0%; next bar open simulation |
| v1 | trend_8_26 + momentum_26 | 9891.24 | -108.76 | sell /  / trend_8_26 + momentum_26: prior completed bar target 0%; next bar open simulation |
| v1 | trend_8_26 AND breakout_8 | 9850.32 | -149.68 | sell /  / trend_8_26 AND breakout_8: prior completed bar target 0%; next bar open simulation |
| v1 | trend_8_26 + breakout_8 | 9849.76 | -150.24 | sell /  / trend_8_26 + breakout_8: prior completed bar target 0%; next bar open simulation |
| v1 | trend_8_26 AND reversion_12 | 9928.06 | -71.94 | sell /  / trend_8_26 AND reversion_12: prior completed bar target 0%; next bar open simulation |
| v1 | trend_8_26 + reversion_12 | 9901.29 | -98.71 | sell /  / trend_8_26 + reversion_12: prior completed bar target 50%; next bar open simulation |
| v1 | trend_8_26 AND volume_26 | 10000.00 | 0.00 | 대기 /  / 새 신호 대기 |
| v1 | trend_8_26 + volume_26 | 9954.72 | -45.28 | sell /  / trend_8_26 + volume_26: prior completed bar target 0%; next bar open simulation |
| v1 | momentum_26 AND breakout_8 | 9850.32 | -149.68 | sell /  / momentum_26 AND breakout_8: prior completed bar target 0%; next bar open simulation |
| v1 | momentum_26 + breakout_8 | 9831.28 | -168.72 | sell /  / momentum_26 + breakout_8: prior completed bar target 0%; next bar open simulation |
| v1 | momentum_26 AND reversion_12 | 9887.21 | -112.79 | sell /  / momentum_26 AND reversion_12: prior completed bar target 0%; next bar open simulation |
| v1 | momentum_26 + reversion_12 | 9863.07 | -136.93 | sell /  / momentum_26 + reversion_12: prior completed bar target 50%; next bar open simulation |
| v1 | momentum_26 AND volume_26 | 10000.00 | 0.00 | 대기 /  / 새 신호 대기 |
| v1 | momentum_26 + volume_26 | 9936.12 | -63.88 | sell /  / momentum_26 + volume_26: prior completed bar target 0%; next bar open simulation |
| v1 | breakout_8 AND reversion_12 | 10000.00 | 0.00 | 대기 /  / 새 신호 대기 |
| v1 | breakout_8 + reversion_12 | 9821.57 | -178.43 | sell /  / breakout_8 + reversion_12: prior completed bar target 50%; next bar open simulation |
| v1 | breakout_8 AND volume_26 | 10000.00 | 0.00 | 대기 /  / 새 신호 대기 |
| v1 | breakout_8 + volume_26 | 9894.44 | -105.56 | sell /  / breakout_8 + volume_26: prior completed bar target 0%; next bar open simulation |
| v1 | reversion_12 AND volume_26 | 10000.00 | 0.00 | 대기 /  / 새 신호 대기 |
| v1 | reversion_12 + volume_26 | 9926.36 | -73.64 | sell /  / reversion_12 + volume_26: prior completed bar target 50%; next bar open simulation |
| v1 | ema_12_26 | 9862.47 | -137.53 | sell /  / EMA12 > EMA26; 조건 미충족; EMA12=735.622, EMA26=735.711 |
| v1 | macd_12_26_9 | 9904.18 | -95.82 | sell /  / MACD > 신호선 그리고 MACD > 0; 조건 미충족; MACD=0.746548, signal9=0.752293 |
| v1 | rsi_14_recovery | 9986.99 | -13.01 | sell /  / 직전 RSI14 < 30, 현재 RSI14 >= 30 (한 봉 목표); 조건 미충족; RSI14=42.2805, previous_RSI14=38.7468 |
| v1 | bollinger_20_reentry | 9765.13 | -234.87 | sell /  / 직전 종가 < 직전 하단밴드, 현재 하단밴드 <= 종가 <= SMA20 (한 봉 목표); 조건 미충족; close=727.35, lower20=723.447, SMA20=732.513, previous_lower20=723.966 |
| v1 | donchian_20 | 9950.83 | -49.17 | sell /  / 종가 > 현재 봉을 제외한 직전 20봉 최고가; 조건 미충족; close=739.81, prior_high20=742.28 |
| v1 | atr_14_breakout | 9790.00 | -210.00 | sell /  / 종가 > 직전 종가 + 직전 ATR14 그리고 종가 > EMA26; 조건 미충족; close=731.995, threshold=738.753, prior_ATR14=5.19827, EMA26=730.642 |
| v1 | session_vwap | 9685.21 | -314.79 | sell /  / 종가 > 뉴욕 거래일별 누적 전형가격 VWAP; 조건 미충족; close=726.12, session_VWAP=727.101, session_volume=1.19038e+06 |
| v1 | obv_20 | 9815.32 | -184.68 | sell /  / OBV > OBV의 SMA20 그리고 종가 > EMA26; 조건 미충족; OBV=-2.86269e+06, OBV_SMA20=-3.96202e+06, close=734.925, EMA26=736.093 |
| v1 | stochastic_14_3_recovery | 9843.02 | -156.98 | sell /  / 직전 %K14 < 20에서 %K14가 %D3 상향 돌파 (한 봉 목표); 조건 미충족; K14=70.1066, D3=41.8677, previous_K14=37.4769, previous_D3=26.7366 |
| v1 | mfi_14_recovery | 10056.32 | 56.32 | sell /  / 직전 MFI14 < 20, 현재 MFI14 >= 20 (한 봉 목표); 조건 미충족; MFI14=34.3275, previous_MFI14=29.4992 |
| v1 | adx_14_trend | 10000.00 | 0.00 | 대기 /  / 새 신호 대기 |
| v1 | aroon_25_trend | 10031.15 | 31.15 | sell /  / Aroon25 Up > 70 그리고 Down < 30 (동률이면 최신 극값); 조건 미충족; Aroon_up=88, Aroon_down=48 |
| v1 | cci_20_momentum | 10024.78 | 24.78 | sell /  / CCI20 > 100 (전형가격·평균절대편차); 조건 미충족; CCI20=98.8062 |
| v1 | williams_14_recovery | 9994.82 | -5.18 | sell /  / 직전 Williams %R14 < -80, 현재 >= -80 (한 봉 목표); 조건 미충족; Williams_R14=-29.8934, previous_R14=-62.5231 |
| v1 | cmf_20_accumulation | 9842.76 | -157.24 | sell /  / Chaikin Money Flow20 > 0.1; 조건 미충족; CMF20=-0.0799774, volume20=4.73159e+06 |
| v1 | chaikin_3_10 | 9578.60 | -421.40 | sell /  / ADL의 EMA3 - EMA10 > 0 그리고 종가 > EMA26; 조건 미충족; Chaikin3_10=17534.4, ADL=-6.11189e+06, close=730.415, EMA26=730.797 |
| v1 | roc_10_momentum | 9963.13 | -36.87 | sell /  / 10봉 ROC > 1% 그리고 종가 > EMA26; 조건 미충족; ROC10_percent=-0.134597, close=734.53, EMA26=735.486 |
| v1 | trix_15_trend | 9669.78 | -330.22 | sell /  / 15봉 삼중 EMA의 1봉 변화율 TRIX > 0 그리고 종가 > EMA26; 조건 미충족; TRIX15_percent=0.0186631, close=734.925, EMA26=736.093 |
| v1 | keltner_20_breakout | 10000.00 | 0.00 | 대기 /  / 새 신호 대기 |
| v1 | opening_range_30m | 10040.71 | 40.71 | sell /  / 뉴욕 09:30·09:45 두 완료 봉 최고가를 10:00 이후 종가가 돌파; 자료 부족·변동폭 또는 거래량 없음: 대기; close=740.21 |
| v2 | cash | 10000.00 | 0.00 | 대기 /  / 새 신호 대기 |
| v2 | buy_hold | 9104.14 | -895.86 | 중단: 손실 한도 / buy / partial / 직전 완료 봉 목표 비중 100%; 다음 봉 시가 가정 |
| v2 | trend_8_26 | 9831.00 | -169.00 | sell / filled / 직전 완료 봉 목표 비중 0%; 다음 봉 시가 가정 |
| v2 | momentum_26 | 9885.12 | -114.88 | sell / filled / 직전 완료 봉 목표 비중 0%; 다음 봉 시가 가정 |
| v2 | breakout_8 | 9610.96 | -389.04 | sell / filled / 직전 완료 봉 목표 비중 0%; 다음 봉 시가 가정 |
| v2 | reversion_12 | 8977.00 | -1023.00 | 중단: 손실 한도 / buy / partial / 직전 완료 봉 목표 비중 100%; 다음 봉 시가 가정 |
| v2 | volume_26 | 9233.73 | -766.27 | 중단: 손실 한도 / buy / partial / 직전 완료 봉 목표 비중 100%; 다음 봉 시가 가정 |
| v2 | trend_8_26 AND momentum_26 | 9914.96 | -85.04 | sell / filled / 직전 완료 봉 목표 비중 0%; 다음 봉 시가 가정 |
| v2 | trend_8_26 + momentum_26 | 9858.16 | -141.84 | sell / filled / 직전 완료 봉 목표 비중 0%; 다음 봉 시가 가정 |
| v2 | trend_8_26 AND breakout_8 | 9765.08 | -234.92 | sell / filled / 직전 완료 봉 목표 비중 0%; 다음 봉 시가 가정 |
| v2 | trend_8_26 + breakout_8 | 9720.80 | -279.20 | sell / filled / 직전 완료 봉 목표 비중 0%; 다음 봉 시가 가정 |
| v2 | trend_8_26 AND reversion_12 | 9738.62 | -261.38 | sell / filled / 직전 완료 봉 목표 비중 0%; 다음 봉 시가 가정 |
| v2 | trend_8_26 + reversion_12 | 9523.02 | -476.98 | sell / filled / 직전 완료 봉 목표 비중 50%; 다음 봉 시가 가정 |
| v2 | trend_8_26 AND volume_26 | 10035.44 | 35.44 | sell / filled / 직전 완료 봉 목표 비중 0%; 다음 봉 시가 가정 |
| v2 | trend_8_26 + volume_26 | 9587.50 | -412.50 | sell / filled / 직전 완료 봉 목표 비중 0%; 다음 봉 시가 가정 |
| v2 | momentum_26 AND breakout_8 | 9824.16 | -175.84 | sell / filled / 직전 완료 봉 목표 비중 0%; 다음 봉 시가 가정 |
| v2 | momentum_26 + breakout_8 | 9747.29 | -252.71 | sell / filled / 직전 완료 봉 목표 비중 0%; 다음 봉 시가 가정 |
| v2 | momentum_26 AND reversion_12 | 9755.55 | -244.45 | sell / filled / 직전 완료 봉 목표 비중 0%; 다음 봉 시가 가정 |
| v2 | momentum_26 + reversion_12 | 9529.11 | -470.89 | sell / filled / 직전 완료 봉 목표 비중 50%; 다음 봉 시가 가정 |
| v2 | momentum_26 AND volume_26 | 10048.78 | 48.78 | sell / filled / 직전 완료 봉 목표 비중 0%; 다음 봉 시가 가정 |
| v2 | momentum_26 + volume_26 | 9633.99 | -366.01 | sell / filled / 직전 완료 봉 목표 비중 0%; 다음 봉 시가 가정 |
| v2 | breakout_8 AND reversion_12 | 10000.00 | 0.00 | 대기 /  / 새 신호 대기 |
| v2 | breakout_8 + reversion_12 | 9610.18 | -389.82 | 중단: 손실 한도 / sell / filled / 직전 완료 봉 목표 비중 0%; 다음 봉 시가 가정 |
| v2 | breakout_8 AND volume_26 | 9998.69 | -1.31 | sell / filled / 직전 완료 봉 목표 비중 0%; 다음 봉 시가 가정 |
| v2 | breakout_8 + volume_26 | 9499.63 | -500.37 | sell / filled / 직전 완료 봉 목표 비중 0%; 다음 봉 시가 가정 |
| v2 | reversion_12 AND volume_26 | 9169.85 | -830.15 | 중단: 손실 한도 / buy / partial / 직전 완료 봉 목표 비중 100%; 다음 봉 시가 가정 |
| v2 | reversion_12 + volume_26 | 9350.80 | -649.20 | 중단: 손실 한도 / sell / filled / 직전 완료 봉 목표 비중 50%; 다음 봉 시가 가정 |
| v2 | ema_12_26 | 9860.50 | -139.50 | sell / filled / EMA12 > EMA26; 조건 미충족; EMA12=735.622, EMA26=735.711; 직전 완료 봉 목표를 다음 봉 시가에 모의 적용 |
| v2 | macd_12_26_9 | 9902.20 | -97.80 | sell / filled / MACD > 신호선 그리고 MACD > 0; 조건 미충족; MACD=0.746548, signal9=0.752293; 직전 완료 봉 목표를 다음 봉 시가에 모의 적용 |
| v2 | rsi_14_recovery | 9984.99 | -15.01 | sell / filled / 직전 RSI14 < 30, 현재 RSI14 >= 30 (한 봉 목표); 조건 미충족; RSI14=42.2805, previous_RSI14=38.7468; 직전 완료 봉 목표를 다음 봉 시가에 모의 적용 |
| v2 | bollinger_20_reentry | 9761.22 | -238.78 | sell / filled / 직전 종가 < 직전 하단밴드, 현재 하단밴드 <= 종가 <= SMA20 (한 봉 목표); 조건 미충족; close=727.35, lower20=723.447, SMA20=732.513, previous_lower20=723.966; 직전 완료 봉 목표를 다음 봉 시가에 모의 적용 |
| v2 | donchian_20 | 9948.84 | -51.16 | sell / filled / 종가 > 현재 봉을 제외한 직전 20봉 최고가; 조건 미충족; close=739.81, prior_high20=742.28; 직전 완료 봉 목표를 다음 봉 시가에 모의 적용 |
| v2 | atr_14_breakout | 9784.13 | -215.87 | sell / filled / 종가 > 직전 종가 + 직전 ATR14 그리고 종가 > EMA26; 조건 미충족; close=731.995, threshold=738.753, prior_ATR14=5.19827, EMA26=730.642; 직전 완료 봉 목표를 다음 봉 시가에 모의 적용 |
| v2 | session_vwap | 9675.53 | -324.47 | sell / filled / 종가 > 뉴욕 거래일별 누적 전형가격 VWAP; 조건 미충족; close=726.12, session_VWAP=727.101, session_volume=1.19038e+06; 직전 완료 봉 목표를 다음 봉 시가에 모의 적용 |
| v2 | obv_20 | 9809.44 | -190.56 | sell / filled / OBV > OBV의 SMA20 그리고 종가 > EMA26; 조건 미충족; OBV=-3.10102e+06, OBV_SMA20=-4.20035e+06, close=734.925, EMA26=736.093; 직전 완료 봉 목표를 다음 봉 시가에 모의 적용 |
| v2 | stochastic_14_3_recovery | 9833.19 | -166.81 | sell / filled / 직전 %K14 < 20에서 %K14가 %D3 상향 돌파 (한 봉 목표); 조건 미충족; K14=70.1066, D3=41.8677, previous_K14=37.4769, previous_D3=26.7366; 직전 완료 봉 목표를 다음 봉 시가에 모의 적용 |
| v2 | mfi_14_recovery | 10054.30 | 54.30 | sell / filled / 직전 MFI14 < 20, 현재 MFI14 >= 20 (한 봉 목표); 조건 미충족; MFI14=34.3275, previous_MFI14=29.4992; 직전 완료 봉 목표를 다음 봉 시가에 모의 적용 |
| v2 | adx_14_trend | 10000.00 | 0.00 | 대기 /  / 새 신호 대기 |
| v2 | aroon_25_trend | 10029.14 | 29.14 | sell / filled / Aroon25 Up > 70 그리고 Down < 30 (동률이면 최신 극값); 조건 미충족; Aroon_up=88, Aroon_down=48; 직전 완료 봉 목표를 다음 봉 시가에 모의 적용 |
| v2 | cci_20_momentum | 10022.77 | 22.77 | sell / filled / CCI20 > 100 (전형가격·평균절대편차); 조건 미충족; CCI20=98.8062; 직전 완료 봉 목표를 다음 봉 시가에 모의 적용 |
| v2 | williams_14_recovery | 9988.83 | -11.17 | sell / filled / 직전 Williams %R14 < -80, 현재 >= -80 (한 봉 목표); 조건 미충족; Williams_R14=-29.8934, previous_R14=-62.5231; 직전 완료 봉 목표를 다음 봉 시가에 모의 적용 |
| v2 | cmf_20_accumulation | 9838.82 | -161.18 | sell / filled / Chaikin Money Flow20 > 0.1; 조건 미충족; CMF20=-0.0799774, volume20=4.73159e+06; 직전 완료 봉 목표를 다음 봉 시가에 모의 적용 |
| v2 | chaikin_3_10 | 9587.99 | -412.01 | 중단: 손실 한도 / buy / partial / ADL의 EMA3 - EMA10 > 0 그리고 종가 > EMA26; 조건 충족; Chaikin3_10=293683, ADL=-4.91156e+06, close=739.58, EMA26=736.187; 직전 완료 봉 목표를 다음 봉 시가에 모의 적용 |
| v2 | roc_10_momentum | 9961.14 | -38.86 | sell / filled / 10봉 ROC > 1% 그리고 종가 > EMA26; 조건 미충족; ROC10_percent=-0.134597, close=734.53, EMA26=735.486; 직전 완료 봉 목표를 다음 봉 시가에 모의 적용 |
| v2 | trix_15_trend | 9597.65 | -402.35 | 중단: 손실 한도 / buy / partial / 15봉 삼중 EMA의 1봉 변화율 TRIX > 0 그리고 종가 > EMA26; 조건 충족; TRIX15_percent=0.0196284, close=739.58, EMA26=736.187; 직전 완료 봉 목표를 다음 봉 시가에 모의 적용 |
| v2 | keltner_20_breakout | 10000.00 | 0.00 | 대기 /  / 새 신호 대기 |
| v2 | opening_range_30m | 10038.70 | 38.70 | sell / filled / 뉴욕 09:30·09:45 두 완료 봉 최고가를 10:00 이후 종가가 돌파; 자료 부족·변동폭 또는 거래량 없음: 대기; close=740.21; 직전 완료 봉 목표를 다음 봉 시가에 모의 적용 |

### 같은 기간의 비용·노출 비교 (사후 연구)

| 전략 | 비용 전 | 비용 후 | 100% 보유 | 같은 평균 노출 보유 | 평균 노출 |
|---|---:|---:|---:|---:|---:|
| cash | 0.00% | 0.00% | -12.40% | -0.00% | 0.00% |
| buy_hold | -12.03% | -12.40% | -12.40% | -12.40% | 100.00% |
| trend_8_26 | -1.74% | -5.38% | -12.40% | -5.77% | 45.55% |
| momentum_26 | -3.01% | -7.00% | -12.40% | -5.74% | 45.29% |
| breakout_8 | -2.78% | -15.01% | -12.40% | -1.85% | 14.40% |
| reversion_12 | -3.76% | -16.92% | -12.40% | -3.57% | 28.01% |
| volume_26 | -3.40% | -9.68% | -12.40% | -0.94% | 7.33% |
| trend_8_26 AND momentum_26 | -0.26% | -3.15% | -12.40% | -5.02% | 39.53% |
| trend_8_26 + momentum_26 | -2.36% | -6.19% | -12.40% | -5.76% | 45.42% |
| trend_8_26 AND breakout_8 | -1.69% | -8.46% | -12.40% | -0.91% | 7.07% |
| trend_8_26 + breakout_8 | -2.23% | -10.11% | -12.40% | -3.82% | 29.98% |
| trend_8_26 AND reversion_12 | 0.56% | -5.98% | -12.40% | -0.81% | 6.28% |
| trend_8_26 + reversion_12 | -2.69% | -10.56% | -12.40% | -4.68% | 36.79% |
| trend_8_26 AND volume_26 | 1.75% | -0.37% | -12.40% | -0.24% | 1.83% |
| trend_8_26 + volume_26 | -2.52% | -7.34% | -12.40% | -3.38% | 26.44% |
| momentum_26 AND breakout_8 | -2.12% | -9.25% | -12.40% | -0.98% | 7.59% |
| momentum_26 + breakout_8 | -2.86% | -11.07% | -12.40% | -3.81% | 29.85% |
| momentum_26 AND reversion_12 | -2.51% | -8.84% | -12.40% | -0.84% | 6.54% |
| momentum_26 + reversion_12 | -3.33% | -11.34% | -12.40% | -4.66% | 36.65% |
| momentum_26 AND volume_26 | 1.45% | -0.24% | -12.40% | -0.17% | 1.31% |
| momentum_26 + volume_26 | -3.15% | -7.94% | -12.40% | -3.36% | 26.31% |
| breakout_8 AND reversion_12 | 0.00% | 0.00% | -12.40% | -0.00% | 0.00% |
| breakout_8 + reversion_12 | -3.21% | -15.06% | -12.40% | -2.71% | 21.21% |
| breakout_8 AND volume_26 | 0.37% | -0.47% | -12.40% | -0.07% | 0.52% |
| breakout_8 + volume_26 | -3.06% | -11.81% | -12.40% | -1.40% | 10.87% |
| reversion_12 AND volume_26 | -1.40% | -5.45% | -12.40% | -0.64% | 4.97% |
| reversion_12 + volume_26 | -3.54% | -12.81% | -12.40% | -2.26% | 17.68% |
| ema_12_26 | -2.53% | -4.56% | -12.40% | -5.54% | 43.72% |
| macd_12_26_9 | 1.07% | -1.86% | -12.40% | -3.47% | 27.23% |
| rsi_14_recovery | -0.69% | -6.36% | -12.40% | -0.47% | 3.66% |
| bollinger_20_reentry | -0.24% | -6.33% | -12.40% | -0.51% | 3.93% |
| donchian_20 | -1.20% | -5.26% | -12.40% | -0.61% | 4.71% |
| atr_14_breakout | -1.85% | -8.23% | -12.40% | -0.57% | 4.45% |
| session_vwap | 0.13% | -11.73% | -12.40% | -5.54% | 43.72% |
| obv_20 | -4.13% | -13.32% | -12.40% | -2.94% | 23.04% |
| stochastic_14_3_recovery | -2.99% | -14.12% | -12.40% | -0.98% | 7.59% |
| mfi_14_recovery | 1.43% | -1.10% | -12.40% | -0.20% | 1.57% |
| adx_14_trend | -2.02% | -4.05% | -12.40% | -1.08% | 8.38% |
| aroon_25_trend | -1.25% | -4.91% | -12.40% | -1.65% | 12.83% |
| cci_20_momentum | -4.37% | -9.45% | -12.40% | -1.88% | 14.66% |
| williams_14_recovery | -0.65% | -10.18% | -12.40% | -0.81% | 6.28% |
| cmf_20_accumulation | -5.52% | -12.03% | -12.40% | -2.11% | 16.49% |
| chaikin_3_10 | -6.04% | -15.05% | -12.40% | -3.97% | 31.15% |
| roc_10_momentum | -1.79% | -7.40% | -12.40% | -1.61% | 12.57% |
| trix_15_trend | -1.68% | -6.12% | -12.40% | -4.36% | 34.29% |
| keltner_20_breakout | -2.87% | -5.29% | -12.40% | -0.34% | 2.62% |
| opening_range_30m | 6.14% | 1.77% | -12.40% | -2.55% | 19.90% |

동일 구간·초기 자금, 종료 시 청산 비용 포함. 노출 맞춤은 사후 설명용이며 v2 실제 계좌 성과가 아닙니다.
[낙폭 분해·비용 영향·전체 구간](CAT/comparison.json)

[v1 전체 기록](CAT/accounts.json) · [v2 전체 기록](CAT/accounts-v2.json)

## WMT 계좌

| 모델 | 전략 | 평가액 USD | 손익 USD | 최근 매매·이유 |
|---|---|---:|---:|---|
| v1 | cash | 10000.00 | 0.00 | 대기 /  / 새 신호 대기 |
| v1 | buy_hold | 10072.53 | 72.53 | buy /  / buy_hold: prior completed bar target 100%; next bar open simulation |
| v1 | trend_8_26 | 9889.42 | -110.58 | buy /  / trend_8_26: prior completed bar target 100%; next bar open simulation |
| v1 | momentum_26 | 9883.85 | -116.15 | buy /  / momentum_26: prior completed bar target 100%; next bar open simulation |
| v1 | breakout_8 | 9817.56 | -182.44 | buy /  / breakout_8: prior completed bar target 100%; next bar open simulation |
| v1 | reversion_12 | 9916.28 | -83.72 | sell /  / reversion_12: prior completed bar target 0%; next bar open simulation |
| v1 | volume_26 | 9915.76 | -84.24 | sell /  / volume_26: prior completed bar target 0%; next bar open simulation |
| v1 | trend_8_26 AND momentum_26 | 9894.21 | -105.79 | buy /  / trend_8_26 AND momentum_26: prior completed bar target 100%; next bar open simulation |
| v1 | trend_8_26 + momentum_26 | 9886.67 | -113.33 | buy /  / trend_8_26 + momentum_26: prior completed bar target 100%; next bar open simulation |
| v1 | trend_8_26 AND breakout_8 | 9944.33 | -55.67 | buy /  / trend_8_26 AND breakout_8: prior completed bar target 100%; next bar open simulation |
| v1 | trend_8_26 + breakout_8 | 9853.33 | -146.67 | buy /  / trend_8_26 + breakout_8: prior completed bar target 100%; next bar open simulation |
| v1 | trend_8_26 AND reversion_12 | 9967.64 | -32.36 | sell /  / trend_8_26 AND reversion_12: prior completed bar target 0%; next bar open simulation |
| v1 | trend_8_26 + reversion_12 | 9922.59 | -77.41 | buy /  / trend_8_26 + reversion_12: prior completed bar target 50%; next bar open simulation |
| v1 | trend_8_26 AND volume_26 | 10000.00 | 0.00 | 대기 /  / 새 신호 대기 |
| v1 | trend_8_26 + volume_26 | 9902.49 | -97.51 | buy /  / trend_8_26 + volume_26: prior completed bar target 50%; next bar open simulation |
| v1 | momentum_26 AND breakout_8 | 9905.88 | -94.12 | buy /  / momentum_26 AND breakout_8: prior completed bar target 100%; next bar open simulation |
| v1 | momentum_26 + breakout_8 | 9909.99 | -90.01 | buy /  / momentum_26 + breakout_8: prior completed bar target 100%; next bar open simulation |
| v1 | momentum_26 AND reversion_12 | 10011.47 | 11.47 | sell /  / momentum_26 AND reversion_12: prior completed bar target 0%; next bar open simulation |
| v1 | momentum_26 + reversion_12 | 9939.61 | -60.39 | buy /  / momentum_26 + reversion_12: prior completed bar target 50%; next bar open simulation |
| v1 | momentum_26 AND volume_26 | 10013.52 | 13.52 | sell /  / momentum_26 AND volume_26: prior completed bar target 0%; next bar open simulation |
| v1 | momentum_26 + volume_26 | 9919.55 | -80.45 | buy /  / momentum_26 + volume_26: prior completed bar target 50%; next bar open simulation |
| v1 | breakout_8 AND reversion_12 | 10000.00 | 0.00 | 대기 /  / 새 신호 대기 |
| v1 | breakout_8 + reversion_12 | 9886.51 | -113.49 | sell /  / breakout_8 + reversion_12: prior completed bar target 50%; next bar open simulation |
| v1 | breakout_8 AND volume_26 | 9913.57 | -86.43 | sell /  / breakout_8 AND volume_26: prior completed bar target 0%; next bar open simulation |
| v1 | breakout_8 + volume_26 | 9866.59 | -133.41 | sell /  / breakout_8 + volume_26: prior completed bar target 50%; next bar open simulation |
| v1 | reversion_12 AND volume_26 | 10000.00 | 0.00 | 대기 /  / 새 신호 대기 |
| v1 | reversion_12 + volume_26 | 9955.79 | -44.21 | sell /  / reversion_12 + volume_26: prior completed bar target 0%; next bar open simulation |
| v1 | ema_12_26 | 10005.29 | 5.29 | buy /  / EMA12 > EMA26; 조건 충족; EMA12=118.628, EMA26=118.619 |
| v1 | macd_12_26_9 | 10017.84 | 17.84 | buy /  / MACD > 신호선 그리고 MACD > 0; 조건 충족; MACD=0.00919902, signal9=-0.00852776 |
| v1 | rsi_14_recovery | 10000.00 | 0.00 | 대기 /  / 새 신호 대기 |
| v1 | bollinger_20_reentry | 10000.00 | 0.00 | 대기 /  / 새 신호 대기 |
| v1 | donchian_20 | 10000.00 | 0.00 | 대기 /  / 새 신호 대기 |
| v1 | atr_14_breakout | 9979.72 | -20.28 | sell /  / 종가 > 직전 종가 + 직전 ATR14 그리고 종가 > EMA26; 조건 미충족; close=119.375, threshold=119.607, prior_ATR14=0.486823, EMA26=118.217 |
| v1 | session_vwap | 9756.49 | -243.51 | buy /  / 종가 > 뉴욕 거래일별 누적 전형가격 VWAP; 조건 충족; close=118.68, session_VWAP=118.618, session_volume=1.15133e+07 |
| v1 | obv_20 | 9885.84 | -114.16 | buy /  / OBV > OBV의 SMA20 그리고 종가 > EMA26; 조건 충족; OBV=2.23382e+07, OBV_SMA20=1.748e+07, close=118.68, EMA26=118.585 |
| v1 | stochastic_14_3_recovery | 9979.72 | -20.28 | sell /  / 직전 %K14 < 20에서 %K14가 %D3 상향 돌파 (한 봉 목표); 조건 미충족; K14=93.8952, D3=60.8222, previous_K14=82.4242, previous_D3=34.5012 |
| v1 | mfi_14_recovery | 10000.00 | 0.00 | 대기 /  / 새 신호 대기 |
| v1 | adx_14_trend | 9991.69 | -8.31 | sell /  / Wilder ADX14 >= 25 그리고 +DI14 > -DI14; 조건 미충족; ADX14=24.5142, plus_DI14=24.7537, minus_DI14=21.6519 |
| v1 | aroon_25_trend | 10000.00 | 0.00 | 대기 /  / 새 신호 대기 |
| v1 | cci_20_momentum | 9934.37 | -65.63 | buy /  / CCI20 > 100 (전형가격·평균절대편차); 조건 충족; CCI20=148.633 |
| v1 | williams_14_recovery | 9979.72 | -20.28 | sell /  / 직전 Williams %R14 < -80, 현재 >= -80 (한 봉 목표); 조건 미충족; Williams_R14=-6.10484, previous_R14=-17.5758 |
| v1 | cmf_20_accumulation | 9914.64 | -85.36 | buy /  / Chaikin Money Flow20 > 0.1; 조건 충족; CMF20=0.112667, volume20=1.57051e+07 |
| v1 | chaikin_3_10 | 9744.22 | -255.78 | buy /  / ADL의 EMA3 - EMA10 > 0 그리고 종가 > EMA26; 조건 충족; Chaikin3_10=395736, ADL=1.91464e+07, close=118.68, EMA26=118.585 |
| v1 | roc_10_momentum | 10000.00 | 0.00 | 대기 /  / 새 신호 대기 |
| v1 | trix_15_trend | 9824.31 | -175.69 | sell /  / 15봉 삼중 EMA의 1봉 변화율 TRIX > 0 그리고 종가 > EMA26; 조건 미충족; TRIX15_percent=0.00969478, close=118.67, EMA26=118.682 |
| v1 | keltner_20_breakout | 10000.00 | 0.00 | 대기 /  / 새 신호 대기 |
| v1 | opening_range_30m | 10000.00 | 0.00 | 대기 /  / 새 신호 대기 |
| v2 | cash | 10000.00 | 0.00 | 대기 /  / 새 신호 대기 |
| v2 | buy_hold | 10671.75 | 671.75 | buy / partial / 직전 완료 봉 목표 비중 100%; 다음 봉 시가 가정 |
| v2 | trend_8_26 | 10290.36 | 290.36 | buy / partial / 직전 완료 봉 목표 비중 100%; 다음 봉 시가 가정 |
| v2 | momentum_26 | 10289.44 | 289.44 | buy / partial / 직전 완료 봉 목표 비중 100%; 다음 봉 시가 가정 |
| v2 | breakout_8 | 9774.05 | -225.95 | buy / partial / 직전 완료 봉 목표 비중 100%; 다음 봉 시가 가정 |
| v2 | reversion_12 | 9818.63 | -181.37 | sell / filled / 직전 완료 봉 목표 비중 0%; 다음 봉 시가 가정 |
| v2 | volume_26 | 9875.40 | -124.60 | sell / filled / 직전 완료 봉 목표 비중 0%; 다음 봉 시가 가정 |
| v2 | trend_8_26 AND momentum_26 | 10295.34 | 295.34 | buy / partial / 직전 완료 봉 목표 비중 100%; 다음 봉 시가 가정 |
| v2 | trend_8_26 + momentum_26 | 10289.87 | 289.87 | buy / partial / 직전 완료 봉 목표 비중 100%; 다음 봉 시가 가정 |
| v2 | trend_8_26 AND breakout_8 | 10029.38 | 29.38 | buy / partial / 직전 완료 봉 목표 비중 100%; 다음 봉 시가 가정 |
| v2 | trend_8_26 + breakout_8 | 10029.18 | 29.18 | buy / partial / 직전 완료 봉 목표 비중 100%; 다음 봉 시가 가정 |
| v2 | trend_8_26 AND reversion_12 | 9775.04 | -224.96 | sell / filled / 직전 완료 봉 목표 비중 0%; 다음 봉 시가 가정 |
| v2 | trend_8_26 + reversion_12 | 10074.19 | 74.19 | buy / filled / 직전 완료 봉 목표 비중 50%; 다음 봉 시가 가정 |
| v2 | trend_8_26 AND volume_26 | 9949.23 | -50.77 | sell / filled / 직전 완료 봉 목표 비중 0%; 다음 봉 시가 가정 |
| v2 | trend_8_26 + volume_26 | 10082.08 | 82.08 | buy / filled / 직전 완료 봉 목표 비중 50%; 다음 봉 시가 가정 |
| v2 | momentum_26 AND breakout_8 | 9865.93 | -134.07 | buy / partial / 직전 완료 봉 목표 비중 100%; 다음 봉 시가 가정 |
| v2 | momentum_26 + breakout_8 | 10092.26 | 92.26 | buy / partial / 직전 완료 봉 목표 비중 100%; 다음 봉 시가 가정 |
| v2 | momentum_26 AND reversion_12 | 9838.09 | -161.91 | sell / filled / 직전 완료 봉 목표 비중 0%; 다음 봉 시가 가정 |
| v2 | momentum_26 + reversion_12 | 10137.43 | 137.43 | buy / filled / 직전 완료 봉 목표 비중 50%; 다음 봉 시가 가정 |
| v2 | momentum_26 AND volume_26 | 9925.24 | -74.76 | sell / filled / 직전 완료 봉 목표 비중 0%; 다음 봉 시가 가정 |
| v2 | momentum_26 + volume_26 | 10102.91 | 102.91 | buy / filled / 직전 완료 봉 목표 비중 50%; 다음 봉 시가 가정 |
| v2 | breakout_8 AND reversion_12 | 10000.00 | 0.00 | 대기 /  / 새 신호 대기 |
| v2 | breakout_8 + reversion_12 | 9838.64 | -161.36 | sell / filled / 직전 완료 봉 목표 비중 50%; 다음 봉 시가 가정 |
| v2 | breakout_8 AND volume_26 | 9860.28 | -139.72 | sell / filled / 직전 완료 봉 목표 비중 0%; 다음 봉 시가 가정 |
| v2 | breakout_8 + volume_26 | 9826.01 | -173.99 | sell / filled / 직전 완료 봉 목표 비중 50%; 다음 봉 시가 가정 |
| v2 | reversion_12 AND volume_26 | 10009.78 | 9.78 | sell / filled / 직전 완료 봉 목표 비중 0%; 다음 봉 시가 가정 |
| v2 | reversion_12 + volume_26 | 9888.34 | -111.66 | sell / filled / 직전 완료 봉 목표 비중 0%; 다음 봉 시가 가정 |
| v2 | ema_12_26 | 10002.29 | 2.29 | buy / partial / EMA12 > EMA26; 조건 충족; EMA12=118.628, EMA26=118.619; 직전 완료 봉 목표를 다음 봉 시가에 모의 적용 |
| v2 | macd_12_26_9 | 10016.84 | 16.84 | buy / partial / MACD > 신호선 그리고 MACD > 0; 조건 충족; MACD=0.00919902, signal9=-0.00852776; 직전 완료 봉 목표를 다음 봉 시가에 모의 적용 |
| v2 | rsi_14_recovery | 10000.00 | 0.00 | 대기 /  / 새 신호 대기 |
| v2 | bollinger_20_reentry | 10000.00 | 0.00 | 대기 /  / 새 신호 대기 |
| v2 | donchian_20 | 10000.00 | 0.00 | 대기 /  / 새 신호 대기 |
| v2 | atr_14_breakout | 9977.72 | -22.28 | sell / filled / 종가 > 직전 종가 + 직전 ATR14 그리고 종가 > EMA26; 조건 미충족; close=119.375, threshold=119.607, prior_ATR14=0.486823, EMA26=118.217; 직전 완료 봉 목표를 다음 봉 시가에 모의 적용 |
| v2 | session_vwap | 9745.76 | -254.24 | buy / partial / 종가 > 뉴욕 거래일별 누적 전형가격 VWAP; 조건 충족; close=118.68, session_VWAP=118.618, session_volume=1.15133e+07; 직전 완료 봉 목표를 다음 봉 시가에 모의 적용 |
| v2 | obv_20 | 9878.92 | -121.08 | buy / partial / OBV > OBV의 SMA20 그리고 종가 > EMA26; 조건 충족; OBV=2.23382e+07, OBV_SMA20=1.748e+07, close=118.68, EMA26=118.585; 직전 완료 봉 목표를 다음 봉 시가에 모의 적용 |
| v2 | stochastic_14_3_recovery | 9977.72 | -22.28 | sell / filled / 직전 %K14 < 20에서 %K14가 %D3 상향 돌파 (한 봉 목표); 조건 미충족; K14=93.8952, D3=60.8222, previous_K14=82.4242, previous_D3=34.5012; 직전 완료 봉 목표를 다음 봉 시가에 모의 적용 |
| v2 | mfi_14_recovery | 10000.00 | 0.00 | 대기 /  / 새 신호 대기 |
| v2 | adx_14_trend | 9989.70 | -10.30 | sell / filled / Wilder ADX14 >= 25 그리고 +DI14 > -DI14; 조건 미충족; ADX14=24.5142, plus_DI14=24.7537, minus_DI14=21.6519; 직전 완료 봉 목표를 다음 봉 시가에 모의 적용 |
| v2 | aroon_25_trend | 10000.00 | 0.00 | 대기 /  / 새 신호 대기 |
| v2 | cci_20_momentum | 9931.39 | -68.61 | buy / partial / CCI20 > 100 (전형가격·평균절대편차); 조건 충족; CCI20=148.633; 직전 완료 봉 목표를 다음 봉 시가에 모의 적용 |
| v2 | williams_14_recovery | 9977.72 | -22.28 | sell / filled / 직전 Williams %R14 < -80, 현재 >= -80 (한 봉 목표); 조건 미충족; Williams_R14=-6.10484, previous_R14=-17.5758; 직전 완료 봉 목표를 다음 봉 시가에 모의 적용 |
| v2 | cmf_20_accumulation | 9909.69 | -90.31 | buy / partial / Chaikin Money Flow20 > 0.1; 조건 충족; CMF20=0.112667, volume20=1.57051e+07; 직전 완료 봉 목표를 다음 봉 시가에 모의 적용 |
| v2 | chaikin_3_10 | 9733.51 | -266.49 | buy / partial / ADL의 EMA3 - EMA10 > 0 그리고 종가 > EMA26; 조건 충족; Chaikin3_10=395736, ADL=1.91464e+07, close=118.68, EMA26=118.585; 직전 완료 봉 목표를 다음 봉 시가에 모의 적용 |
| v2 | roc_10_momentum | 10000.00 | 0.00 | 대기 /  / 새 신호 대기 |
| v2 | trix_15_trend | 9818.42 | -181.58 | sell / filled / 15봉 삼중 EMA의 1봉 변화율 TRIX > 0 그리고 종가 > EMA26; 조건 미충족; TRIX15_percent=0.00969478, close=118.67, EMA26=118.682; 직전 완료 봉 목표를 다음 봉 시가에 모의 적용 |
| v2 | keltner_20_breakout | 10000.00 | 0.00 | 대기 /  / 새 신호 대기 |
| v2 | opening_range_30m | 10000.00 | 0.00 | 대기 /  / 새 신호 대기 |

### 같은 기간의 비용·노출 비교 (사후 연구)

| 전략 | 비용 전 | 비용 후 | 100% 보유 | 같은 평균 노출 보유 | 평균 노출 |
|---|---:|---:|---:|---:|---:|
| cash | 0.00% | 0.00% | 12.12% | 0.00% | 0.00% |
| buy_hold | 12.59% | 12.12% | 12.12% | 12.12% | 100.00% |
| trend_8_26 | 8.32% | 4.74% | 12.12% | 7.86% | 65.71% |
| momentum_26 | 9.84% | 4.00% | 12.12% | 7.96% | 66.49% |
| breakout_8 | 6.79% | -10.10% | 12.12% | 3.08% | 26.18% |
| reversion_12 | 4.11% | -6.66% | 12.12% | 2.09% | 17.80% |
| volume_26 | 0.84% | -4.92% | 12.12% | 0.67% | 5.76% |
| trend_8_26 AND momentum_26 | 8.05% | 3.18% | 12.12% | 7.06% | 59.16% |
| trend_8_26 + momentum_26 | 9.08% | 4.37% | 12.12% | 7.91% | 66.10% |
| trend_8_26 AND breakout_8 | 6.91% | -6.15% | 12.12% | 2.46% | 20.94% |
| trend_8_26 + breakout_8 | 7.57% | -2.95% | 12.12% | 5.45% | 45.95% |
| trend_8_26 AND reversion_12 | 0.27% | -4.66% | 12.12% | 0.76% | 6.54% |
| trend_8_26 + reversion_12 | 6.23% | -0.70% | 12.12% | 4.95% | 41.76% |
| trend_8_26 AND volume_26 | 0.53% | -1.56% | 12.12% | 0.21% | 1.83% |
| trend_8_26 + volume_26 | 4.55% | 0.23% | 12.12% | 4.22% | 35.74% |
| momentum_26 AND breakout_8 | 6.95% | -6.50% | 12.12% | 2.62% | 22.25% |
| momentum_26 + breakout_8 | 8.32% | -2.48% | 12.12% | 5.50% | 46.34% |
| momentum_26 AND reversion_12 | 1.20% | -4.18% | 12.12% | 0.86% | 7.33% |
| momentum_26 + reversion_12 | 6.97% | 0.63% | 12.12% | 4.99% | 42.15% |
| momentum_26 AND volume_26 | 1.86% | -1.91% | 12.12% | 0.31% | 2.62% |
| momentum_26 + volume_26 | 5.28% | -0.34% | 12.12% | 4.27% | 36.13% |
| breakout_8 AND reversion_12 | 0.00% | 0.00% | 12.12% | 0.00% | 0.00% |
| breakout_8 + reversion_12 | 5.47% | -7.81% | 12.12% | 2.59% | 22.00% |
| breakout_8 AND volume_26 | 1.02% | -1.49% | 12.12% | 0.21% | 1.83% |
| breakout_8 + volume_26 | 3.80% | -7.34% | 12.12% | 1.87% | 15.98% |
| reversion_12 AND volume_26 | -0.51% | -2.99% | 12.12% | 0.27% | 2.36% |
| reversion_12 + volume_26 | 2.47% | -5.20% | 12.12% | 1.38% | 11.78% |
| ema_12_26 | 12.08% | 10.68% | 12.12% | 8.15% | 68.06% |
| macd_12_26_9 | 8.37% | 4.79% | 12.12% | 3.96% | 33.51% |
| rsi_14_recovery | -0.68% | -2.74% | 12.12% | 0.15% | 1.31% |
| bollinger_20_reentry | 0.93% | -2.41% | 12.12% | 0.24% | 2.09% |
| donchian_20 | 4.80% | -7.22% | 12.12% | 1.53% | 13.09% |
| atr_14_breakout | -0.61% | -10.14% | 12.12% | 0.86% | 7.33% |
| session_vwap | 8.42% | -2.39% | 12.12% | 6.90% | 57.85% |
| obv_20 | 10.38% | 2.78% | 12.12% | 6.45% | 54.19% |
| stochastic_14_3_recovery | 1.36% | -8.36% | 12.12% | 0.73% | 6.28% |
| mfi_14_recovery | 0.02% | -0.81% | 12.12% | 0.06% | 0.52% |
| adx_14_trend | 8.84% | 6.13% | 12.12% | 6.01% | 50.52% |
| aroon_25_trend | 5.69% | 1.34% | 12.12% | 3.43% | 29.06% |
| cci_20_momentum | 7.42% | -0.82% | 12.12% | 3.71% | 31.41% |
| williams_14_recovery | 0.16% | -7.91% | 12.12% | 0.61% | 5.24% |
| cmf_20_accumulation | 8.63% | -0.12% | 12.12% | 4.11% | 34.82% |
| chaikin_3_10 | 8.57% | 0.24% | 12.12% | 5.98% | 50.26% |
| roc_10_momentum | -0.30% | -5.20% | 12.12% | 1.69% | 14.40% |
| trix_15_trend | 10.96% | 8.20% | 12.12% | 7.41% | 62.04% |
| keltner_20_breakout | 6.84% | 0.74% | 12.12% | 3.08% | 26.18% |
| opening_range_30m | 10.12% | 5.59% | 12.12% | 4.08% | 34.55% |

동일 구간·초기 자금, 종료 시 청산 비용 포함. 노출 맞춤은 사후 설명용이며 v2 실제 계좌 성과가 아닙니다.
[낙폭 분해·비용 영향·전체 구간](WMT/comparison.json)

[v1 전체 기록](WMT/accounts.json) · [v2 전체 기록](WMT/accounts-v2.json)
