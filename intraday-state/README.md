# 모의투자 운영 현황

[PC·서버 장애 진단과 복구 방법](https://github.com/BaekJaeYeol/paper-trading-program/blob/main/investment-lab/docs/failure-recovery.md)

이번 실행 복구: {}

완료 봉 확인 주기: 기록 0/15회 · 기록 없는 예정 15회 · 아직 판정 전 11회 · 주의: 예약 시작 지연 또는 실행·저장 누락을 확인하세요.

[주기 판정 기준](https://github.com/BaekJaeYeol/paper-trading-program/blob/main/investment-lab/docs/session-coverage.md)

최근 확인: 2026-10-19T17:37:00.417860+00:00 (UTC)
다음 15분 확인 목표 (세션 실행 중에만 적용): 2026-10-19T17:52:00+00:00 (UTC, 실행 지연 가능)

실제 주문 없음. v1 기존 계좌와 v2 새 계좌의 시작일이 다르므로 수익률을 직접 우열 비교하지 마세요.
v2는 다음 봉 시가에 비용·스프레드·직전 거래량 제한을 적용한 가상 체결입니다. 미체결 잔량은 만료됩니다.

| 종목 | 상태 | 최근 성공 UTC | 마지막 완료 봉 UTC | 이번 새 봉 |
|---|---|---|---|---|
| SPY | updated | 2026-10-19T17:37:00.417860+00:00 | 2026-10-19T17:15:00+00:00 | 1 |
| QQQ | updated | 2026-10-19T17:37:00.417860+00:00 | 2026-10-19T17:15:00+00:00 | 1 |
| IWM | updated | 2026-10-19T17:37:00.417860+00:00 | 2026-10-19T17:15:00+00:00 | 1 |
| DIA | updated | 2026-10-19T17:37:00.417860+00:00 | 2026-10-19T17:15:00+00:00 | 1 |
| MSFT | updated | 2026-10-19T17:37:00.417860+00:00 | 2026-10-19T17:15:00+00:00 | 1 |
| JPM | updated | 2026-10-19T17:37:00.417860+00:00 | 2026-10-19T17:15:00+00:00 | 1 |
| XOM | updated | 2026-10-19T17:37:00.417860+00:00 | 2026-10-19T17:15:00+00:00 | 1 |
| JNJ | updated | 2026-10-19T17:37:00.417860+00:00 | 2026-10-19T17:15:00+00:00 | 1 |
| CAT | updated | 2026-10-19T17:37:00.417860+00:00 | 2026-10-19T17:15:00+00:00 | 1 |
| WMT | updated | 2026-10-19T17:37:00.417860+00:00 | 2026-10-19T17:15:00+00:00 | 1 |

이번 실행 소요: 45.66초
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
| v1 | buy_hold | 9904.58 | -95.42 | buy /  / buy_hold: prior completed bar target 100%; next bar open simulation |
| v1 | trend_8_26 | 9882.90 | -117.10 | buy /  / trend_8_26: prior completed bar target 100%; next bar open simulation |
| v1 | momentum_26 | 9864.40 | -135.60 | buy /  / momentum_26: prior completed bar target 100%; next bar open simulation |
| v1 | breakout_8 | 9873.76 | -126.24 | sell /  / breakout_8: prior completed bar target 0%; next bar open simulation |
| v1 | reversion_12 | 9861.07 | -138.93 | buy /  / reversion_12: prior completed bar target 100%; next bar open simulation |
| v1 | volume_26 | 9790.14 | -209.86 | sell /  / volume_26: prior completed bar target 0%; next bar open simulation |
| v1 | trend_8_26 AND momentum_26 | 9864.40 | -135.60 | buy /  / trend_8_26 AND momentum_26: prior completed bar target 100%; next bar open simulation |
| v1 | trend_8_26 + momentum_26 | 9873.64 | -126.36 | buy /  / trend_8_26 + momentum_26: prior completed bar target 100%; next bar open simulation |
| v1 | trend_8_26 AND breakout_8 | 9970.32 | -29.68 | sell /  / trend_8_26 AND breakout_8: prior completed bar target 0%; next bar open simulation |
| v1 | trend_8_26 + breakout_8 | 9898.01 | -101.99 | buy /  / trend_8_26 + breakout_8: prior completed bar target 50%; next bar open simulation |
| v1 | trend_8_26 AND reversion_12 | 9924.87 | -75.13 | buy /  / trend_8_26 AND reversion_12: prior completed bar target 100%; next bar open simulation |
| v1 | trend_8_26 + reversion_12 | 9871.89 | -128.11 | buy /  / trend_8_26 + reversion_12: prior completed bar target 100%; next bar open simulation |
| v1 | trend_8_26 AND volume_26 | 9836.21 | -163.79 | sell /  / trend_8_26 AND volume_26: prior completed bar target 0%; next bar open simulation |
| v1 | trend_8_26 + volume_26 | 9836.36 | -163.64 | buy /  / trend_8_26 + volume_26: prior completed bar target 50%; next bar open simulation |
| v1 | momentum_26 AND breakout_8 | 9954.13 | -45.87 | sell /  / momentum_26 AND breakout_8: prior completed bar target 0%; next bar open simulation |
| v1 | momentum_26 + breakout_8 | 9869.04 | -130.96 | buy /  / momentum_26 + breakout_8: prior completed bar target 50%; next bar open simulation |
| v1 | momentum_26 AND reversion_12 | 9978.53 | -21.47 | buy /  / momentum_26 AND reversion_12: prior completed bar target 100%; next bar open simulation |
| v1 | momentum_26 + reversion_12 | 9882.39 | -117.61 | buy /  / momentum_26 + reversion_12: prior completed bar target 100%; next bar open simulation |
| v1 | momentum_26 AND volume_26 | 9849.91 | -150.09 | sell /  / momentum_26 AND volume_26: prior completed bar target 0%; next bar open simulation |
| v1 | momentum_26 + volume_26 | 9827.16 | -172.84 | buy /  / momentum_26 + volume_26: prior completed bar target 50%; next bar open simulation |
| v1 | breakout_8 AND reversion_12 | 10000.00 | 0.00 | 대기 /  / 새 신호 대기 |
| v1 | breakout_8 + reversion_12 | 9867.30 | -132.70 | sell /  / breakout_8 + reversion_12: prior completed bar target 50%; next bar open simulation |
| v1 | breakout_8 AND volume_26 | 9954.13 | -45.87 | sell /  / breakout_8 AND volume_26: prior completed bar target 0%; next bar open simulation |
| v1 | breakout_8 + volume_26 | 9831.79 | -168.21 | sell /  / breakout_8 + volume_26: prior completed bar target 0%; next bar open simulation |
| v1 | reversion_12 AND volume_26 | 9899.64 | -100.36 | sell /  / reversion_12 AND volume_26: prior completed bar target 0%; next bar open simulation |
| v1 | reversion_12 + volume_26 | 9825.46 | -174.54 | sell /  / reversion_12 + volume_26: prior completed bar target 50%; next bar open simulation |
| v1 | ema_12_26 | 9866.71 | -133.29 | buy /  / EMA12 > EMA26; 조건 충족; EMA12=766.605, EMA26=766.511 |
| v1 | macd_12_26_9 | 9880.44 | -119.56 | buy /  / MACD > 신호선 그리고 MACD > 0; 조건 충족; MACD=0.0937072, signal9=-0.695283 |
| v1 | rsi_14_recovery | 9899.32 | -100.68 | sell /  / 직전 RSI14 < 30, 현재 RSI14 >= 30 (한 봉 목표); 조건 미충족; RSI14=34.3611, previous_RSI14=32.906 |
| v1 | bollinger_20_reentry | 9835.17 | -164.83 | sell /  / 직전 종가 < 직전 하단밴드, 현재 하단밴드 <= 종가 <= SMA20 (한 봉 목표); 조건 미충족; close=763.39, lower20=762.854, SMA20=768.639, previous_lower20=763.636 |
| v1 | donchian_20 | 9960.79 | -39.21 | sell /  / 종가 > 현재 봉을 제외한 직전 20봉 최고가; 조건 미충족; close=769.96, prior_high20=770.3 |
| v1 | atr_14_breakout | 9955.14 | -44.86 | sell /  / 종가 > 직전 종가 + 직전 ATR14 그리고 종가 > EMA26; 조건 미충족; close=766.58, threshold=768.736, prior_ATR14=1.82624, EMA26=765.727 |
| v1 | session_vwap | 9806.83 | -193.17 | sell /  / 종가 > 뉴욕 거래일별 누적 전형가격 VWAP; 조건 미충족; close=768.64, session_VWAP=768.839, session_volume=6.99147e+07 |
| v1 | obv_20 | 9909.51 | -90.49 | sell /  / OBV > OBV의 SMA20 그리고 종가 > EMA26; 조건 미충족; OBV=-1.1153e+07, OBV_SMA20=-7.86173e+06, close=768.275, EMA26=767.362 |
| v1 | stochastic_14_3_recovery | 9839.35 | -160.65 | sell /  / 직전 %K14 < 20에서 %K14가 %D3 상향 돌파 (한 봉 목표); 조건 미충족; K14=84.501, D3=47.2592, previous_K14=38.478, previous_D3=30.1887 |
| v1 | mfi_14_recovery | 9955.14 | -44.86 | sell /  / 직전 MFI14 < 20, 현재 MFI14 >= 20 (한 봉 목표); 조건 미충족; MFI14=24.4041, previous_MFI14=24.1984 |
| v1 | adx_14_trend | 9981.96 | -18.04 | sell /  / Wilder ADX14 >= 25 그리고 +DI14 > -DI14; 조건 미충족; ADX14=24.2312, plus_DI14=28.3519, minus_DI14=24.6578 |
| v1 | aroon_25_trend | 9881.82 | -118.18 | buy /  / Aroon25 Up > 70 그리고 Down < 30 (동률이면 최신 극값); 조건 충족; Aroon_up=76, Aroon_down=28 |
| v1 | cci_20_momentum | 9861.55 | -138.45 | sell /  / CCI20 > 100 (전형가격·평균절대편차); 조건 미충족; CCI20=98.503 |
| v1 | williams_14_recovery | 9811.23 | -188.77 | sell /  / 직전 Williams %R14 < -80, 현재 >= -80 (한 봉 목표); 조건 미충족; Williams_R14=-15.499, previous_R14=-61.522 |
| v1 | cmf_20_accumulation | 9890.95 | -109.05 | sell /  / Chaikin Money Flow20 > 0.1; 조건 미충족; CMF20=0.0493062, volume20=8.08389e+07 |
| v1 | chaikin_3_10 | 9864.45 | -135.55 | sell /  / ADL의 EMA3 - EMA10 > 0 그리고 종가 > EMA26; 조건 미충족; Chaikin3_10=-974621, ADL=7.60516e+06, close=768.275, EMA26=767.362 |
| v1 | roc_10_momentum | 9953.42 | -46.58 | sell /  / 10봉 ROC > 1% 그리고 종가 > EMA26; 조건 미충족; ROC10_percent=0.806376, close=769.45, EMA26=767.181 |
| v1 | trix_15_trend | 9885.20 | -114.80 | buy /  / 15봉 삼중 EMA의 1봉 변화율 TRIX > 0 그리고 종가 > EMA26; 조건 충족; TRIX15_percent=0.00164165, close=768.275, EMA26=767.362 |
| v1 | keltner_20_breakout | 10000.00 | 0.00 | 대기 /  / 새 신호 대기 |
| v1 | opening_range_30m | 9846.77 | -153.23 | sell /  / 뉴욕 09:30·09:45 두 완료 봉 최고가를 10:00 이후 종가가 돌파; 조건 미충족; close=767.51, opening_high=768.06 |
| v2 | cash | 10000.00 | 0.00 | 대기 /  / 새 신호 대기 |
| v2 | buy_hold | 9833.14 | -166.86 | buy / partial / 직전 완료 봉 목표 비중 100%; 다음 봉 시가 가정 |
| v2 | trend_8_26 | 9765.82 | -234.18 | buy / partial / 직전 완료 봉 목표 비중 100%; 다음 봉 시가 가정 |
| v2 | momentum_26 | 9718.28 | -281.72 | buy / partial / 직전 완료 봉 목표 비중 100%; 다음 봉 시가 가정 |
| v2 | breakout_8 | 9471.75 | -528.25 | sell / filled / 직전 완료 봉 목표 비중 0%; 다음 봉 시가 가정 |
| v2 | reversion_12 | 9396.78 | -603.22 | buy / partial / 직전 완료 봉 목표 비중 100%; 다음 봉 시가 가정 |
| v2 | volume_26 | 9235.92 | -764.08 | sell / filled / 직전 완료 봉 목표 비중 0%; 다음 봉 시가 가정 |
| v2 | trend_8_26 AND momentum_26 | 9724.90 | -275.10 | buy / partial / 직전 완료 봉 목표 비중 100%; 다음 봉 시가 가정 |
| v2 | trend_8_26 + momentum_26 | 9742.02 | -257.98 | buy / partial / 직전 완료 봉 목표 비중 100%; 다음 봉 시가 가정 |
| v2 | trend_8_26 AND breakout_8 | 9794.09 | -205.91 | sell / filled / 직전 완료 봉 목표 비중 0%; 다음 봉 시가 가정 |
| v2 | trend_8_26 + breakout_8 | 9637.67 | -362.33 | buy / filled / 직전 완료 봉 목표 비중 50%; 다음 봉 시가 가정 |
| v2 | trend_8_26 AND reversion_12 | 9818.82 | -181.18 | buy / partial / 직전 완료 봉 목표 비중 100%; 다음 봉 시가 가정 |
| v2 | trend_8_26 + reversion_12 | 9579.12 | -420.88 | buy / partial / 직전 완료 봉 목표 비중 100%; 다음 봉 시가 가정 |
| v2 | trend_8_26 AND volume_26 | 9678.83 | -321.17 | sell / filled / 직전 완료 봉 목표 비중 0%; 다음 봉 시가 가정 |
| v2 | trend_8_26 + volume_26 | 9516.86 | -483.14 | buy / filled / 직전 완료 봉 목표 비중 50%; 다음 봉 시가 가정 |
| v2 | momentum_26 AND breakout_8 | 9736.71 | -263.29 | sell / filled / 직전 완료 봉 목표 비중 0%; 다음 봉 시가 가정 |
| v2 | momentum_26 + breakout_8 | 9594.11 | -405.89 | buy / filled / 직전 완료 봉 목표 비중 50%; 다음 봉 시가 가정 |
| v2 | momentum_26 AND reversion_12 | 9940.82 | -59.18 | buy / partial / 직전 완료 봉 목표 비중 100%; 다음 봉 시가 가정 |
| v2 | momentum_26 + reversion_12 | 9596.00 | -404.00 | buy / partial / 직전 완료 봉 목표 비중 100%; 다음 봉 시가 가정 |
| v2 | momentum_26 AND volume_26 | 9762.54 | -237.46 | sell / filled / 직전 완료 봉 목표 비중 0%; 다음 봉 시가 가정 |
| v2 | momentum_26 + volume_26 | 9533.61 | -466.39 | buy / filled / 직전 완료 봉 목표 비중 50%; 다음 봉 시가 가정 |
| v2 | breakout_8 AND reversion_12 | 10000.00 | 0.00 | 대기 /  / 새 신호 대기 |
| v2 | breakout_8 + reversion_12 | 9473.36 | -526.64 | sell / filled / 직전 완료 봉 목표 비중 50%; 다음 봉 시가 가정 |
| v2 | breakout_8 AND volume_26 | 9885.63 | -114.37 | sell / filled / 직전 완료 봉 목표 비중 0%; 다음 봉 시가 가정 |
| v2 | breakout_8 + volume_26 | 9392.04 | -607.96 | sell / filled / 직전 완료 봉 목표 비중 0%; 다음 봉 시가 가정 |
| v2 | reversion_12 AND volume_26 | 9641.69 | -358.31 | sell / filled / 직전 완료 봉 목표 비중 0%; 다음 봉 시가 가정 |
| v2 | reversion_12 + volume_26 | 9394.24 | -605.76 | sell / filled / 직전 완료 봉 목표 비중 50%; 다음 봉 시가 가정 |
| v2 | ema_12_26 | 9863.75 | -136.25 | buy / partial / EMA12 > EMA26; 조건 충족; EMA12=766.605, EMA26=766.511; 직전 완료 봉 목표를 다음 봉 시가에 모의 적용 |
| v2 | macd_12_26_9 | 9877.48 | -122.52 | buy / partial / MACD > 신호선 그리고 MACD > 0; 조건 충족; MACD=0.0937072, signal9=-0.695283; 직전 완료 봉 목표를 다음 봉 시가에 모의 적용 |
| v2 | rsi_14_recovery | 9895.36 | -104.64 | sell / filled / 직전 RSI14 < 30, 현재 RSI14 >= 30 (한 봉 목표); 조건 미충족; RSI14=34.3611, previous_RSI14=32.906; 직전 완료 봉 목표를 다음 봉 시가에 모의 적용 |
| v2 | bollinger_20_reentry | 9829.27 | -170.73 | sell / filled / 직전 종가 < 직전 하단밴드, 현재 하단밴드 <= 종가 <= SMA20 (한 봉 목표); 조건 미충족; close=763.39, lower20=762.854, SMA20=768.639, previous_lower20=763.636; 직전 완료 봉 목표를 다음 봉 시가에 모의 적용 |
| v2 | donchian_20 | 9958.80 | -41.20 | sell / filled / 종가 > 현재 봉을 제외한 직전 20봉 최고가; 조건 미충족; close=769.96, prior_high20=770.3; 직전 완료 봉 목표를 다음 봉 시가에 모의 적용 |
| v2 | atr_14_breakout | 9953.15 | -46.85 | sell / filled / 종가 > 직전 종가 + 직전 ATR14 그리고 종가 > EMA26; 조건 미충족; close=766.58, threshold=768.736, prior_ATR14=1.82624, EMA26=765.727; 직전 완료 봉 목표를 다음 봉 시가에 모의 적용 |
| v2 | session_vwap | 9798.99 | -201.01 | sell / filled / 종가 > 뉴욕 거래일별 누적 전형가격 VWAP; 조건 미충족; close=768.64, session_VWAP=768.839, session_volume=6.99147e+07; 직전 완료 봉 목표를 다음 봉 시가에 모의 적용 |
| v2 | obv_20 | 9905.54 | -94.46 | sell / filled / OBV > OBV의 SMA20 그리고 종가 > EMA26; 조건 미충족; OBV=-1.1153e+07, OBV_SMA20=-7.86173e+06, close=768.275, EMA26=767.362; 직전 완료 봉 목표를 다음 봉 시가에 모의 적용 |
| v2 | stochastic_14_3_recovery | 9831.49 | -168.51 | sell / filled / 직전 %K14 < 20에서 %K14가 %D3 상향 돌파 (한 봉 목표); 조건 미충족; K14=84.501, D3=47.2592, previous_K14=38.478, previous_D3=30.1887; 직전 완료 봉 목표를 다음 봉 시가에 모의 적용 |
| v2 | mfi_14_recovery | 9953.15 | -46.85 | sell / filled / 직전 MFI14 < 20, 현재 MFI14 >= 20 (한 봉 목표); 조건 미충족; MFI14=24.4041, previous_MFI14=24.1984; 직전 완료 봉 목표를 다음 봉 시가에 모의 적용 |
| v2 | adx_14_trend | 9979.97 | -20.03 | sell / filled / Wilder ADX14 >= 25 그리고 +DI14 > -DI14; 조건 미충족; ADX14=24.2312, plus_DI14=28.3519, minus_DI14=24.6578; 직전 완료 봉 목표를 다음 봉 시가에 모의 적용 |
| v2 | aroon_25_trend | 9878.85 | -121.15 | buy / partial / Aroon25 Up > 70 그리고 Down < 30 (동률이면 최신 극값); 조건 충족; Aroon_up=76, Aroon_down=28; 직전 완료 봉 목표를 다음 봉 시가에 모의 적용 |
| v2 | cci_20_momentum | 9855.63 | -144.37 | sell / filled / CCI20 > 100 (전형가격·평균절대편차); 조건 미충족; CCI20=98.503; 직전 완료 봉 목표를 다음 봉 시가에 모의 적용 |
| v2 | williams_14_recovery | 9803.39 | -196.61 | sell / filled / 직전 Williams %R14 < -80, 현재 >= -80 (한 봉 목표); 조건 미충족; Williams_R14=-15.499, previous_R14=-61.522; 직전 완료 봉 목표를 다음 봉 시가에 모의 적용 |
| v2 | cmf_20_accumulation | 9887.00 | -113.00 | sell / filled / Chaikin Money Flow20 > 0.1; 조건 미충족; CMF20=0.0493062, volume20=8.08389e+07; 직전 완료 봉 목표를 다음 봉 시가에 모의 적용 |
| v2 | chaikin_3_10 | 9858.53 | -141.47 | sell / filled / ADL의 EMA3 - EMA10 > 0 그리고 종가 > EMA26; 조건 미충족; Chaikin3_10=-974621, ADL=7.60516e+06, close=768.275, EMA26=767.362; 직전 완료 봉 목표를 다음 봉 시가에 모의 적용 |
| v2 | roc_10_momentum | 9951.43 | -48.57 | sell / filled / 10봉 ROC > 1% 그리고 종가 > EMA26; 조건 미충족; ROC10_percent=0.806376, close=769.45, EMA26=767.181; 직전 완료 봉 목표를 다음 봉 시가에 모의 적용 |
| v2 | trix_15_trend | 9882.24 | -117.76 | buy / partial / 15봉 삼중 EMA의 1봉 변화율 TRIX > 0 그리고 종가 > EMA26; 조건 충족; TRIX15_percent=0.00164165, close=768.275, EMA26=767.362; 직전 완료 봉 목표를 다음 봉 시가에 모의 적용 |
| v2 | keltner_20_breakout | 10000.00 | 0.00 | 대기 /  / 새 신호 대기 |
| v2 | opening_range_30m | 9840.86 | -159.14 | sell / filled / 뉴욕 09:30·09:45 두 완료 봉 최고가를 10:00 이후 종가가 돌파; 조건 미충족; close=767.51, opening_high=768.06; 직전 완료 봉 목표를 다음 봉 시가에 모의 적용 |

### 같은 기간의 비용·노출 비교 (사후 연구)

| 전략 | 비용 전 | 비용 후 | 100% 보유 | 같은 평균 노출 보유 | 평균 노출 |
|---|---:|---:|---:|---:|---:|
| cash | 0.00% | 0.00% | -0.16% | -0.00% | 0.00% |
| buy_hold | 0.26% | -0.16% | -0.16% | -0.16% | 100.00% |
| trend_8_26 | 1.45% | -1.91% | -0.16% | -0.08% | 49.34% |
| momentum_26 | -0.47% | -4.57% | -0.16% | -0.08% | 47.77% |
| breakout_8 | -0.22% | -15.65% | -0.16% | -0.04% | 22.31% |
| reversion_12 | -1.62% | -12.90% | -0.16% | -0.05% | 29.40% |
| volume_26 | -1.12% | -10.60% | -0.16% | -0.02% | 9.71% |
| trend_8_26 AND momentum_26 | 0.59% | -3.14% | -0.16% | -0.07% | 41.99% |
| trend_8_26 + momentum_26 | 0.48% | -3.25% | -0.16% | -0.08% | 48.56% |
| trend_8_26 AND breakout_8 | 0.17% | -10.57% | -0.16% | -0.02% | 13.12% |
| trend_8_26 + breakout_8 | 0.61% | -8.85% | -0.16% | -0.06% | 35.83% |
| trend_8_26 AND reversion_12 | -0.17% | -3.87% | -0.16% | -0.01% | 6.04% |
| trend_8_26 + reversion_12 | -0.09% | -7.38% | -0.16% | -0.06% | 39.37% |
| trend_8_26 AND volume_26 | -0.68% | -5.16% | -0.16% | -0.01% | 4.72% |
| trend_8_26 + volume_26 | 0.16% | -6.36% | -0.16% | -0.05% | 29.53% |
| momentum_26 AND breakout_8 | 0.31% | -10.44% | -0.16% | -0.02% | 13.91% |
| momentum_26 + breakout_8 | -0.34% | -10.28% | -0.16% | -0.06% | 35.05% |
| momentum_26 AND reversion_12 | -0.80% | -4.88% | -0.16% | -0.01% | 6.30% |
| momentum_26 + reversion_12 | -1.05% | -8.26% | -0.16% | -0.06% | 38.59% |
| momentum_26 AND volume_26 | -0.40% | -3.69% | -0.16% | -0.00% | 2.89% |
| momentum_26 + volume_26 | -0.79% | -6.47% | -0.16% | -0.05% | 28.74% |
| breakout_8 AND reversion_12 | 0.00% | 0.00% | -0.16% | -0.00% | 0.00% |
| breakout_8 + reversion_12 | -0.92% | -13.76% | -0.16% | -0.04% | 25.86% |
| breakout_8 AND volume_26 | 0.03% | -1.64% | -0.16% | -0.00% | 1.57% |
| breakout_8 + volume_26 | -0.67% | -12.25% | -0.16% | -0.03% | 16.02% |
| reversion_12 AND volume_26 | -0.97% | -5.44% | -0.16% | -0.01% | 4.46% |
| reversion_12 + volume_26 | -1.37% | -11.39% | -0.16% | -0.03% | 19.56% |
| ema_12_26 | -0.33% | -3.62% | -0.16% | -0.08% | 49.61% |
| macd_12_26_9 | 0.30% | -4.23% | -0.16% | -0.05% | 31.23% |
| rsi_14_recovery | -0.53% | -4.22% | -0.16% | -0.00% | 2.36% |
| bollinger_20_reentry | -1.13% | -7.17% | -0.16% | -0.01% | 3.94% |
| donchian_20 | 0.11% | -7.17% | -0.16% | -0.01% | 6.82% |
| atr_14_breakout | 0.38% | -4.55% | -0.16% | -0.01% | 3.67% |
| session_vwap | 2.10% | -7.69% | -0.16% | -0.08% | 48.03% |
| obv_20 | 0.26% | -7.43% | -0.16% | -0.06% | 38.85% |
| stochastic_14_3_recovery | -1.11% | -16.05% | -0.16% | -0.02% | 10.24% |
| mfi_14_recovery | -0.06% | -2.96% | -0.16% | -0.00% | 1.84% |
| adx_14_trend | 0.32% | -3.40% | -0.16% | -0.05% | 28.08% |
| aroon_25_trend | 0.83% | -2.09% | -0.16% | -0.04% | 25.46% |
| cci_20_momentum | -0.04% | -8.10% | -0.16% | -0.04% | 22.05% |
| williams_14_recovery | -0.81% | -11.07% | -0.16% | -0.01% | 6.82% |
| cmf_20_accumulation | 2.07% | -2.13% | -0.16% | -0.08% | 45.67% |
| chaikin_3_10 | 1.85% | -4.77% | -0.16% | -0.07% | 40.16% |
| roc_10_momentum | -0.13% | -0.97% | -0.16% | -0.00% | 1.05% |
| trix_15_trend | -0.22% | -3.11% | -0.16% | -0.06% | 36.75% |
| keltner_20_breakout | 0.09% | -3.62% | -0.16% | -0.02% | 10.76% |
| opening_range_30m | 0.36% | -5.37% | -0.16% | -0.05% | 31.76% |

동일 구간·초기 자금, 종료 시 청산 비용 포함. 노출 맞춤은 사후 설명용이며 v2 실제 계좌 성과가 아닙니다.
[낙폭 분해·비용 영향·전체 구간](SPY/comparison.json)

[v1 전체 기록](SPY/accounts.json) · [v2 전체 기록](SPY/accounts-v2.json)

## QQQ 계좌

| 모델 | 전략 | 평가액 USD | 손익 USD | 최근 매매·이유 |
|---|---|---:|---:|---|
| v1 | cash | 10000.00 | 0.00 | 대기 /  / 새 신호 대기 |
| v1 | buy_hold | 9899.54 | -100.46 | buy /  / buy_hold: prior completed bar target 100%; next bar open simulation |
| v1 | trend_8_26 | 9892.32 | -107.68 | buy /  / trend_8_26: prior completed bar target 100%; next bar open simulation |
| v1 | momentum_26 | 9834.76 | -165.24 | buy /  / momentum_26: prior completed bar target 100%; next bar open simulation |
| v1 | breakout_8 | 9897.90 | -102.10 | sell /  / breakout_8: prior completed bar target 0%; next bar open simulation |
| v1 | reversion_12 | 9865.09 | -134.91 | buy /  / reversion_12: prior completed bar target 100%; next bar open simulation |
| v1 | volume_26 | 9763.59 | -236.41 | sell /  / volume_26: prior completed bar target 0%; next bar open simulation |
| v1 | trend_8_26 AND momentum_26 | 9900.85 | -99.15 | buy /  / trend_8_26 AND momentum_26: prior completed bar target 100%; next bar open simulation |
| v1 | trend_8_26 + momentum_26 | 9883.21 | -116.79 | buy /  / trend_8_26 + momentum_26: prior completed bar target 100%; next bar open simulation |
| v1 | trend_8_26 AND breakout_8 | 9989.91 | -10.09 | sell /  / trend_8_26 AND breakout_8: prior completed bar target 0%; next bar open simulation |
| v1 | trend_8_26 + breakout_8 | 9914.84 | -85.16 | buy /  / trend_8_26 + breakout_8: prior completed bar target 50%; next bar open simulation |
| v1 | trend_8_26 AND reversion_12 | 9927.50 | -72.50 | buy /  / trend_8_26 AND reversion_12: prior completed bar target 100%; next bar open simulation |
| v1 | trend_8_26 + reversion_12 | 9878.84 | -121.16 | buy /  / trend_8_26 + reversion_12: prior completed bar target 100%; next bar open simulation |
| v1 | trend_8_26 AND volume_26 | 9932.72 | -67.28 | sell /  / trend_8_26 AND volume_26: prior completed bar target 0%; next bar open simulation |
| v1 | trend_8_26 + volume_26 | 9827.68 | -172.32 | buy /  / trend_8_26 + volume_26: prior completed bar target 50%; next bar open simulation |
| v1 | momentum_26 AND breakout_8 | 9929.95 | -70.05 | sell /  / momentum_26 AND breakout_8: prior completed bar target 0%; next bar open simulation |
| v1 | momentum_26 + breakout_8 | 9866.25 | -133.75 | buy /  / momentum_26 + breakout_8: prior completed bar target 50%; next bar open simulation |
| v1 | momentum_26 AND reversion_12 | 9927.50 | -72.50 | buy /  / momentum_26 AND reversion_12: prior completed bar target 100%; next bar open simulation |
| v1 | momentum_26 + reversion_12 | 9850.07 | -149.93 | buy /  / momentum_26 + reversion_12: prior completed bar target 100%; next bar open simulation |
| v1 | momentum_26 AND volume_26 | 9912.22 | -87.78 | sell /  / momentum_26 AND volume_26: prior completed bar target 0%; next bar open simulation |
| v1 | momentum_26 + volume_26 | 9818.66 | -181.34 | buy /  / momentum_26 + volume_26: prior completed bar target 50%; next bar open simulation |
| v1 | breakout_8 AND reversion_12 | 10000.00 | 0.00 | 대기 /  / 새 신호 대기 |
| v1 | breakout_8 + reversion_12 | 9881.58 | -118.42 | sell /  / breakout_8 + reversion_12: prior completed bar target 50%; next bar open simulation |
| v1 | breakout_8 AND volume_26 | 9947.15 | -52.85 | sell /  / breakout_8 AND volume_26: prior completed bar target 0%; next bar open simulation |
| v1 | breakout_8 + volume_26 | 9850.15 | -149.85 | sell /  / breakout_8 + volume_26: prior completed bar target 0%; next bar open simulation |
| v1 | reversion_12 AND volume_26 | 9907.31 | -92.69 | sell /  / reversion_12 AND volume_26: prior completed bar target 0%; next bar open simulation |
| v1 | reversion_12 + volume_26 | 9853.61 | -146.39 | sell /  / reversion_12 + volume_26: prior completed bar target 50%; next bar open simulation |
| v1 | ema_12_26 | 9890.10 | -109.90 | buy /  / EMA12 > EMA26; 조건 충족; EMA12=717, EMA26=716.746 |
| v1 | macd_12_26_9 | 9890.10 | -109.90 | buy /  / MACD > 신호선 그리고 MACD > 0; 조건 충족; MACD=0.254284, signal9=-1.34399 |
| v1 | rsi_14_recovery | 9813.02 | -186.98 | sell /  / 직전 RSI14 < 30, 현재 RSI14 >= 30 (한 봉 목표); 조건 미충족; RSI14=58.2718, previous_RSI14=33.2263 |
| v1 | bollinger_20_reentry | 9882.24 | -117.76 | sell /  / 직전 종가 < 직전 하단밴드, 현재 하단밴드 <= 종가 <= SMA20 (한 봉 목표); 조건 미충족; close=716.64, lower20=715.793, SMA20=723.132, previous_lower20=716.805 |
| v1 | donchian_20 | 9951.11 | -48.89 | sell /  / 종가 > 현재 봉을 제외한 직전 20봉 최고가; 조건 미충족; close=724.13, prior_high20=724.151 |
| v1 | atr_14_breakout | 9945.53 | -54.47 | sell /  / 종가 > 직전 종가 + 직전 ATR14 그리고 종가 > EMA26; 조건 미충족; close=717.88, threshold=721.828, prior_ATR14=2.82823, EMA26=715.308 |
| v1 | session_vwap | 9802.73 | -197.27 | sell /  / 종가 > 뉴욕 거래일별 누적 전형가격 VWAP; 조건 미충족; close=721.515, session_VWAP=722.066, session_volume=4.49868e+08 |
| v1 | obv_20 | 9919.54 | -80.46 | buy /  / OBV > OBV의 SMA20 그리고 종가 > EMA26; 조건 충족; OBV=-1.30207e+07, OBV_SMA20=-3.93901e+07, close=719, EMA26=715.102 |
| v1 | stochastic_14_3_recovery | 9659.03 | -340.97 | sell /  / 직전 %K14 < 20에서 %K14가 %D3 상향 돌파 (한 봉 목표); 조건 미충족; K14=90.6084, D3=42.9821, previous_K14=27.5933, previous_D3=23.7441 |
| v1 | mfi_14_recovery | 9927.15 | -72.85 | sell /  / 직전 MFI14 < 20, 현재 MFI14 >= 20 (한 봉 목표); 조건 미충족; MFI14=58.7386, previous_MFI14=43.5194 |
| v1 | adx_14_trend | 9926.53 | -73.47 | sell /  / Wilder ADX14 >= 25 그리고 +DI14 > -DI14; 조건 미충족; ADX14=23.9831, plus_DI14=26.5781, minus_DI14=24.6326 |
| v1 | aroon_25_trend | 9899.33 | -100.67 | buy /  / Aroon25 Up > 70 그리고 Down < 30 (동률이면 최신 극값); 조건 충족; Aroon_up=76, Aroon_down=28 |
| v1 | cci_20_momentum | 9950.47 | -49.53 | sell /  / CCI20 > 100 (전형가격·평균절대편차); 조건 미충족; CCI20=97.528 |
| v1 | williams_14_recovery | 9793.99 | -206.01 | sell /  / 직전 Williams %R14 < -80, 현재 >= -80 (한 봉 목표); 조건 미충족; Williams_R14=-9.39162, previous_R14=-72.4067 |
| v1 | cmf_20_accumulation | 9728.92 | -271.08 | buy /  / Chaikin Money Flow20 > 0.1; 조건 충족; CMF20=0.210229, volume20=2.88359e+08 |
| v1 | chaikin_3_10 | 9919.54 | -80.46 | buy /  / ADL의 EMA3 - EMA10 > 0 그리고 종가 > EMA26; 조건 충족; Chaikin3_10=1.42733e+07, ADL=1.66683e+08, close=719, EMA26=715.102 |
| v1 | roc_10_momentum | 9990.50 | -9.50 | sell /  / 10봉 ROC > 1% 그리고 종가 > EMA26; 조건 미충족; ROC10_percent=0.483561, close=722.477, EMA26=718.78 |
| v1 | trix_15_trend | 9929.12 | -70.88 | buy /  / 15봉 삼중 EMA의 1봉 변화율 TRIX > 0 그리고 종가 > EMA26; 조건 충족; TRIX15_percent=0.000507984, close=723.31, EMA26=718.484 |
| v1 | keltner_20_breakout | 9904.16 | -95.84 | sell /  / 종가 > EMA20 + 2 x Wilder ATR14; 조건 미충족; close=723.31, upper_Keltner=723.407, EMA20=718.722, ATR14=2.34265 |
| v1 | opening_range_30m | 9887.22 | -112.78 | sell /  / 뉴욕 09:30·09:45 두 완료 봉 최고가를 10:00 이후 종가가 돌파; 조건 미충족; close=719.99, opening_high=720.22 |
| v2 | cash | 10000.00 | 0.00 | 대기 /  / 새 신호 대기 |
| v2 | buy_hold | 9579.55 | -420.45 | buy / partial / 직전 완료 봉 목표 비중 100%; 다음 봉 시가 가정 |
| v2 | trend_8_26 | 9695.22 | -304.78 | buy / partial / 직전 완료 봉 목표 비중 100%; 다음 봉 시가 가정 |
| v2 | momentum_26 | 9729.35 | -270.65 | buy / partial / 직전 완료 봉 목표 비중 100%; 다음 봉 시가 가정 |
| v2 | breakout_8 | 9565.39 | -434.61 | sell / filled / 직전 완료 봉 목표 비중 0%; 다음 봉 시가 가정 |
| v2 | reversion_12 | 9379.01 | -620.99 | buy / partial / 직전 완료 봉 목표 비중 100%; 다음 봉 시가 가정 |
| v2 | volume_26 | 9565.80 | -434.20 | 중단: 손실 한도 / sell / filled / 직전 완료 봉 목표 비중 0%; 다음 봉 시가 가정 |
| v2 | trend_8_26 AND momentum_26 | 9796.70 | -203.30 | buy / partial / 직전 완료 봉 목표 비중 100%; 다음 봉 시가 가정 |
| v2 | trend_8_26 + momentum_26 | 9732.70 | -267.30 | buy / partial / 직전 완료 봉 목표 비중 100%; 다음 봉 시가 가정 |
| v2 | trend_8_26 AND breakout_8 | 9883.87 | -116.13 | sell / filled / 직전 완료 봉 목표 비중 0%; 다음 봉 시가 가정 |
| v2 | trend_8_26 + breakout_8 | 9650.22 | -349.78 | buy / filled / 직전 완료 봉 목표 비중 50%; 다음 봉 시가 가정 |
| v2 | trend_8_26 AND reversion_12 | 9786.72 | -213.28 | buy / partial / 직전 완료 봉 목표 비중 100%; 다음 봉 시가 가정 |
| v2 | trend_8_26 + reversion_12 | 9535.64 | -464.36 | buy / partial / 직전 완료 봉 목표 비중 100%; 다음 봉 시가 가정 |
| v2 | trend_8_26 AND volume_26 | 9769.99 | -230.01 | sell / filled / 직전 완료 봉 목표 비중 0%; 다음 봉 시가 가정 |
| v2 | trend_8_26 + volume_26 | 9431.50 | -568.50 | buy / filled / 직전 완료 봉 목표 비중 50%; 다음 봉 시가 가정 |
| v2 | momentum_26 AND breakout_8 | 9886.96 | -113.04 | sell / filled / 직전 완료 봉 목표 비중 0%; 다음 봉 시가 가정 |
| v2 | momentum_26 + breakout_8 | 9646.95 | -353.05 | buy / filled / 직전 완료 봉 목표 비중 50%; 다음 봉 시가 가정 |
| v2 | momentum_26 AND reversion_12 | 9924.53 | -75.47 | buy / partial / 직전 완료 봉 목표 비중 100%; 다음 봉 시가 가정 |
| v2 | momentum_26 + reversion_12 | 9572.47 | -427.53 | buy / partial / 직전 완료 봉 목표 비중 100%; 다음 봉 시가 가정 |
| v2 | momentum_26 AND volume_26 | 9845.67 | -154.33 | sell / filled / 직전 완료 봉 목표 비중 0%; 다음 봉 시가 가정 |
| v2 | momentum_26 + volume_26 | 9467.94 | -532.06 | buy / filled / 직전 완료 봉 목표 비중 50%; 다음 봉 시가 가정 |
| v2 | breakout_8 AND reversion_12 | 10000.00 | 0.00 | 대기 /  / 새 신호 대기 |
| v2 | breakout_8 + reversion_12 | 9531.39 | -468.61 | sell / filled / 직전 완료 봉 목표 비중 50%; 다음 봉 시가 가정 |
| v2 | breakout_8 AND volume_26 | 9891.45 | -108.55 | sell / filled / 직전 완료 봉 목표 비중 0%; 다음 봉 시가 가정 |
| v2 | breakout_8 + volume_26 | 9427.43 | -572.57 | sell / filled / 직전 완료 봉 목표 비중 0%; 다음 봉 시가 가정 |
| v2 | reversion_12 AND volume_26 | 9547.64 | -452.36 | 중단: 손실 한도 / sell / filled / 직전 완료 봉 목표 비중 0%; 다음 봉 시가 가정 |
| v2 | reversion_12 + volume_26 | 9335.32 | -664.68 | sell / filled / 직전 완료 봉 목표 비중 50%; 다음 봉 시가 가정 |
| v2 | ema_12_26 | 9887.14 | -112.86 | buy / partial / EMA12 > EMA26; 조건 충족; EMA12=717, EMA26=716.746; 직전 완료 봉 목표를 다음 봉 시가에 모의 적용 |
| v2 | macd_12_26_9 | 9887.14 | -112.86 | buy / partial / MACD > 신호선 그리고 MACD > 0; 조건 충족; MACD=0.254284, signal9=-1.34399; 직전 완료 봉 목표를 다음 봉 시가에 모의 적용 |
| v2 | rsi_14_recovery | 9807.13 | -192.87 | sell / filled / 직전 RSI14 < 30, 현재 RSI14 >= 30 (한 봉 목표); 조건 미충족; RSI14=58.2718, previous_RSI14=33.2263; 직전 완료 봉 목표를 다음 봉 시가에 모의 적용 |
| v2 | bollinger_20_reentry | 9878.29 | -121.71 | sell / filled / 직전 종가 < 직전 하단밴드, 현재 하단밴드 <= 종가 <= SMA20 (한 봉 목표); 조건 미충족; close=716.64, lower20=715.793, SMA20=723.132, previous_lower20=716.805; 직전 완료 봉 목표를 다음 봉 시가에 모의 적용 |
| v2 | donchian_20 | 9947.13 | -52.87 | sell / filled / 종가 > 현재 봉을 제외한 직전 20봉 최고가; 조건 미충족; close=724.13, prior_high20=724.151; 직전 완료 봉 목표를 다음 봉 시가에 모의 적용 |
| v2 | atr_14_breakout | 9943.55 | -56.45 | sell / filled / 종가 > 직전 종가 + 직전 ATR14 그리고 종가 > EMA26; 조건 미충족; close=717.88, threshold=721.828, prior_ATR14=2.82823, EMA26=715.308; 직전 완료 봉 목표를 다음 봉 시가에 모의 적용 |
| v2 | session_vwap | 9794.89 | -205.11 | sell / filled / 종가 > 뉴욕 거래일별 누적 전형가격 VWAP; 조건 미충족; close=721.515, session_VWAP=722.066, session_volume=4.49868e+08; 직전 완료 봉 목표를 다음 봉 시가에 모의 적용 |
| v2 | obv_20 | 9916.56 | -83.44 | buy / partial / OBV > OBV의 SMA20 그리고 종가 > EMA26; 조건 충족; OBV=-1.30207e+07, OBV_SMA20=-3.93901e+07, close=719, EMA26=715.102; 직전 완료 봉 목표를 다음 봉 시가에 모의 적용 |
| v2 | stochastic_14_3_recovery | 9694.13 | -305.87 | 중단: 손실 한도 / sell / filled / 직전 %K14 < 20에서 %K14가 %D3 상향 돌파 (한 봉 목표); 조건 미충족; K14=10.576, D3=8.00581, previous_K14=7.39787, previous_D3=7.27486; 직전 완료 봉 목표를 다음 봉 시가에 모의 적용 |
| v2 | mfi_14_recovery | 9925.16 | -74.84 | sell / filled / 직전 MFI14 < 20, 현재 MFI14 >= 20 (한 봉 목표); 조건 미충족; MFI14=58.7386, previous_MFI14=43.5194; 직전 완료 봉 목표를 다음 봉 시가에 모의 적용 |
| v2 | adx_14_trend | 9922.56 | -77.44 | sell / filled / Wilder ADX14 >= 25 그리고 +DI14 > -DI14; 조건 미충족; ADX14=23.9831, plus_DI14=26.5781, minus_DI14=24.6326; 직전 완료 봉 목표를 다음 봉 시가에 모의 적용 |
| v2 | aroon_25_trend | 9896.36 | -103.64 | buy / partial / Aroon25 Up > 70 그리고 Down < 30 (동률이면 최신 극값); 조건 충족; Aroon_up=76, Aroon_down=28; 직전 완료 봉 목표를 다음 봉 시가에 모의 적용 |
| v2 | cci_20_momentum | 9946.49 | -53.51 | sell / filled / CCI20 > 100 (전형가격·평균절대편차); 조건 미충족; CCI20=97.528; 직전 완료 봉 목표를 다음 봉 시가에 모의 적용 |
| v2 | williams_14_recovery | 9786.16 | -213.84 | sell / filled / 직전 Williams %R14 < -80, 현재 >= -80 (한 봉 목표); 조건 미충족; Williams_R14=-9.39162, previous_R14=-72.4067; 직전 완료 봉 목표를 다음 봉 시가에 모의 적용 |
| v2 | cmf_20_accumulation | 9720.17 | -279.83 | buy / partial / Chaikin Money Flow20 > 0.1; 조건 충족; CMF20=0.210229, volume20=2.88359e+08; 직전 완료 봉 목표를 다음 봉 시가에 모의 적용 |
| v2 | chaikin_3_10 | 9916.56 | -83.44 | buy / partial / ADL의 EMA3 - EMA10 > 0 그리고 종가 > EMA26; 조건 충족; Chaikin3_10=1.42733e+07, ADL=1.66683e+08, close=719, EMA26=715.102; 직전 완료 봉 목표를 다음 봉 시가에 모의 적용 |
| v2 | roc_10_momentum | 9988.50 | -11.50 | sell / filled / 10봉 ROC > 1% 그리고 종가 > EMA26; 조건 미충족; ROC10_percent=0.483561, close=722.477, EMA26=718.78; 직전 완료 봉 목표를 다음 봉 시가에 모의 적용 |
| v2 | trix_15_trend | 9928.13 | -71.87 | buy / partial / 15봉 삼중 EMA의 1봉 변화율 TRIX > 0 그리고 종가 > EMA26; 조건 충족; TRIX15_percent=0.000507984, close=723.31, EMA26=718.484; 직전 완료 봉 목표를 다음 봉 시가에 모의 적용 |
| v2 | keltner_20_breakout | 9900.20 | -99.80 | sell / filled / 종가 > EMA20 + 2 x Wilder ATR14; 조건 미충족; close=723.31, upper_Keltner=723.407, EMA20=718.722, ATR14=2.34265; 직전 완료 봉 목표를 다음 봉 시가에 모의 적용 |
| v2 | opening_range_30m | 9883.27 | -116.73 | sell / filled / 뉴욕 09:30·09:45 두 완료 봉 최고가를 10:00 이후 종가가 돌파; 조건 미충족; close=719.99, opening_high=720.22; 직전 완료 봉 목표를 다음 봉 시가에 모의 적용 |

### 같은 기간의 비용·노출 비교 (사후 연구)

| 전략 | 비용 전 | 비용 후 | 100% 보유 | 같은 평균 노출 보유 | 평균 노출 |
|---|---:|---:|---:|---:|---:|
| cash | 0.00% | 0.00% | -2.69% | -0.00% | 0.00% |
| buy_hold | -2.28% | -2.69% | -2.69% | -2.69% | 100.00% |
| trend_8_26 | 0.68% | -3.06% | -2.69% | -1.23% | 45.93% |
| momentum_26 | -1.17% | -6.42% | -2.69% | -1.08% | 40.16% |
| breakout_8 | -0.79% | -16.13% | -2.69% | -0.51% | 18.90% |
| reversion_12 | -0.14% | -13.07% | -2.69% | -0.79% | 29.40% |
| volume_26 | -1.51% | -14.98% | -2.69% | -0.43% | 16.01% |
| trend_8_26 AND momentum_26 | 0.06% | -4.05% | -2.69% | -0.94% | 35.17% |
| trend_8_26 + momentum_26 | -0.24% | -4.35% | -2.69% | -1.15% | 43.05% |
| trend_8_26 AND breakout_8 | -0.02% | -9.22% | -2.69% | -0.31% | 11.55% |
| trend_8_26 + breakout_8 | -0.05% | -9.26% | -2.69% | -0.87% | 32.42% |
| trend_8_26 AND reversion_12 | 0.16% | -5.56% | -2.69% | -0.18% | 6.56% |
| trend_8_26 + reversion_12 | 0.28% | -7.82% | -2.69% | -1.01% | 37.67% |
| trend_8_26 AND volume_26 | -0.24% | -5.54% | -2.69% | -0.15% | 5.51% |
| trend_8_26 + volume_26 | -0.42% | -9.02% | -2.69% | -0.83% | 30.98% |
| momentum_26 AND breakout_8 | -0.03% | -9.24% | -2.69% | -0.30% | 11.29% |
| momentum_26 + breakout_8 | -0.98% | -11.22% | -2.69% | -0.79% | 29.53% |
| momentum_26 AND reversion_12 | -0.34% | -6.03% | -2.69% | -0.15% | 5.77% |
| momentum_26 + reversion_12 | -0.65% | -9.43% | -2.69% | -0.93% | 34.78% |
| momentum_26 AND volume_26 | -0.04% | -4.56% | -2.69% | -0.11% | 4.20% |
| momentum_26 + volume_26 | -1.34% | -10.43% | -2.69% | -0.75% | 28.09% |
| breakout_8 AND reversion_12 | 0.00% | 0.00% | -2.69% | -0.00% | 0.00% |
| breakout_8 + reversion_12 | -0.46% | -13.72% | -2.69% | -0.65% | 24.16% |
| breakout_8 AND volume_26 | 0.31% | -2.60% | -2.69% | -0.06% | 2.10% |
| breakout_8 + volume_26 | -1.15% | -14.13% | -2.69% | -0.47% | 17.46% |
| reversion_12 AND volume_26 | -1.76% | -8.92% | -2.69% | -0.23% | 8.66% |
| reversion_12 + volume_26 | -0.82% | -13.30% | -2.69% | -0.61% | 22.71% |
| ema_12_26 | 0.72% | -1.37% | -2.69% | -1.01% | 37.53% |
| macd_12_26_9 | 1.28% | -2.48% | -2.69% | -0.61% | 22.83% |
| rsi_14_recovery | -0.83% | -5.71% | -2.69% | -0.08% | 3.15% |
| bollinger_20_reentry | -0.44% | -6.12% | -2.69% | -0.10% | 3.67% |
| donchian_20 | 0.59% | -4.75% | -2.69% | -0.15% | 5.77% |
| atr_14_breakout | 0.11% | -4.01% | -2.69% | -0.08% | 2.89% |
| session_vwap | -0.47% | -12.25% | -2.69% | -1.30% | 48.56% |
| obv_20 | -0.76% | -9.14% | -2.69% | -0.81% | 30.18% |
| stochastic_14_3_recovery | -0.79% | -12.90% | -2.69% | -0.22% | 8.14% |
| mfi_14_recovery | -0.49% | -2.56% | -2.69% | -0.04% | 1.31% |
| adx_14_trend | -0.11% | -3.00% | -2.69% | -0.58% | 21.52% |
| aroon_25_trend | 1.36% | -2.40% | -2.69% | -0.53% | 19.95% |
| cci_20_momentum | -0.25% | -5.55% | -2.69% | -0.46% | 17.32% |
| williams_14_recovery | -1.02% | -12.01% | -2.69% | -0.20% | 7.35% |
| cmf_20_accumulation | -1.11% | -8.69% | -2.69% | -0.83% | 30.97% |
| chaikin_3_10 | -1.93% | -9.45% | -2.69% | -0.99% | 37.01% |
| roc_10_momentum | -0.00% | -1.67% | -2.69% | -0.11% | 4.20% |
| trix_15_trend | 0.42% | -1.25% | -2.69% | -0.82% | 30.71% |
| keltner_20_breakout | -0.89% | -5.76% | -2.69% | -0.22% | 8.14% |
| opening_range_30m | -0.39% | -6.47% | -2.69% | -0.66% | 24.67% |

동일 구간·초기 자금, 종료 시 청산 비용 포함. 노출 맞춤은 사후 설명용이며 v2 실제 계좌 성과가 아닙니다.
[낙폭 분해·비용 영향·전체 구간](QQQ/comparison.json)

[v1 전체 기록](QQQ/accounts.json) · [v2 전체 기록](QQQ/accounts-v2.json)

## IWM 계좌

| 모델 | 전략 | 평가액 USD | 손익 USD | 최근 매매·이유 |
|---|---|---:|---:|---|
| v1 | cash | 10000.00 | 0.00 | 대기 /  / 새 신호 대기 |
| v1 | buy_hold | 9833.15 | -166.85 | buy /  / buy_hold: prior completed bar target 100%; next bar open simulation |
| v1 | trend_8_26 | 9793.89 | -206.11 | buy /  / trend_8_26: prior completed bar target 100%; next bar open simulation |
| v1 | momentum_26 | 9809.81 | -190.19 | buy /  / momentum_26: prior completed bar target 100%; next bar open simulation |
| v1 | breakout_8 | 9788.68 | -211.32 | sell /  / breakout_8: prior completed bar target 0%; next bar open simulation |
| v1 | reversion_12 | 9849.33 | -150.67 | buy /  / reversion_12: prior completed bar target 100%; next bar open simulation |
| v1 | volume_26 | 9862.10 | -137.90 | sell /  / volume_26: prior completed bar target 0%; next bar open simulation |
| v1 | trend_8_26 AND momentum_26 | 9809.81 | -190.19 | buy /  / trend_8_26 AND momentum_26: prior completed bar target 100%; next bar open simulation |
| v1 | trend_8_26 + momentum_26 | 9801.84 | -198.16 | buy /  / trend_8_26 + momentum_26: prior completed bar target 100%; next bar open simulation |
| v1 | trend_8_26 AND breakout_8 | 9896.83 | -103.17 | sell /  / trend_8_26 AND breakout_8: prior completed bar target 0%; next bar open simulation |
| v1 | trend_8_26 + breakout_8 | 9791.27 | -208.73 | buy /  / trend_8_26 + breakout_8: prior completed bar target 50%; next bar open simulation |
| v1 | trend_8_26 AND reversion_12 | 9890.29 | -109.71 | buy /  / trend_8_26 AND reversion_12: prior completed bar target 100%; next bar open simulation |
| v1 | trend_8_26 + reversion_12 | 9821.49 | -178.51 | buy /  / trend_8_26 + reversion_12: prior completed bar target 100%; next bar open simulation |
| v1 | trend_8_26 AND volume_26 | 9935.98 | -64.02 | sell /  / trend_8_26 AND volume_26: prior completed bar target 0%; next bar open simulation |
| v1 | trend_8_26 + volume_26 | 9827.84 | -172.16 | buy /  / trend_8_26 + volume_26: prior completed bar target 50%; next bar open simulation |
| v1 | momentum_26 AND breakout_8 | 9929.38 | -70.62 | sell /  / momentum_26 AND breakout_8: prior completed bar target 0%; next bar open simulation |
| v1 | momentum_26 + breakout_8 | 9818.82 | -181.18 | buy /  / momentum_26 + breakout_8: prior completed bar target 50%; next bar open simulation |
| v1 | momentum_26 AND reversion_12 | 9987.94 | -12.06 | buy /  / momentum_26 AND reversion_12: prior completed bar target 100%; next bar open simulation |
| v1 | momentum_26 + reversion_12 | 9849.13 | -150.87 | buy /  / momentum_26 + reversion_12: prior completed bar target 100%; next bar open simulation |
| v1 | momentum_26 AND volume_26 | 10000.00 | 0.00 | 대기 /  / 새 신호 대기 |
| v1 | momentum_26 + volume_26 | 9835.85 | -164.15 | buy /  / momentum_26 + volume_26: prior completed bar target 50%; next bar open simulation |
| v1 | breakout_8 AND reversion_12 | 10000.00 | 0.00 | 대기 /  / 새 신호 대기 |
| v1 | breakout_8 + reversion_12 | 9818.87 | -181.13 | buy /  / breakout_8 + reversion_12: prior completed bar target 50%; next bar open simulation |
| v1 | breakout_8 AND volume_26 | 9944.66 | -55.34 | sell /  / breakout_8 AND volume_26: prior completed bar target 0%; next bar open simulation |
| v1 | breakout_8 + volume_26 | 9825.26 | -174.74 | sell /  / breakout_8 + volume_26: prior completed bar target 0%; next bar open simulation |
| v1 | reversion_12 AND volume_26 | 9935.98 | -64.02 | sell /  / reversion_12 AND volume_26: prior completed bar target 0%; next bar open simulation |
| v1 | reversion_12 + volume_26 | 9875.41 | -124.59 | buy /  / reversion_12 + volume_26: prior completed bar target 50%; next bar open simulation |
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
| v1 | aroon_25_trend | 9850.22 | -149.78 | buy /  / Aroon25 Up > 70 그리고 Down < 30 (동률이면 최신 극값); 조건 충족; Aroon_up=76, Aroon_down=28 |
| v1 | cci_20_momentum | 9879.55 | -120.45 | sell /  / CCI20 > 100 (전형가격·평균절대편차); 조건 미충족; CCI20=81.8699 |
| v1 | williams_14_recovery | 9903.90 | -96.10 | sell /  / 직전 Williams %R14 < -80, 현재 >= -80 (한 봉 목표); 조건 미충족; Williams_R14=-48.0732, previous_R14=-69.6736 |
| v1 | cmf_20_accumulation | 9799.11 | -200.89 | sell /  / Chaikin Money Flow20 > 0.1; 조건 미충족; CMF20=0.0512251, volume20=2.08469e+07 |
| v1 | chaikin_3_10 | 9805.17 | -194.83 | sell /  / ADL의 EMA3 - EMA10 > 0 그리고 종가 > EMA26; 조건 미충족; Chaikin3_10=-9609.69, ADL=-6.08839e+07, close=271.41, EMA26=271.689 |
| v1 | roc_10_momentum | 10000.00 | 0.00 | 대기 /  / 새 신호 대기 |
| v1 | trix_15_trend | 9895.73 | -104.27 | sell /  / 15봉 삼중 EMA의 1봉 변화율 TRIX > 0 그리고 종가 > EMA26; 조건 미충족; TRIX15_percent=0.0257204, close=273.74, EMA26=273.991 |
| v1 | keltner_20_breakout | 9937.31 | -62.69 | sell /  / 종가 > EMA20 + 2 x Wilder ATR14; 조건 미충족; close=274.88, upper_Keltner=275.161, EMA20=274.044, ATR14=0.558498 |
| v1 | opening_range_30m | 9968.03 | -31.97 | sell /  / 뉴욕 09:30·09:45 두 완료 봉 최고가를 10:00 이후 종가가 돌파; 자료 부족·변동폭 또는 거래량 없음: 대기; close=275.73 |
| v2 | cash | 10000.00 | 0.00 | 대기 /  / 새 신호 대기 |
| v2 | buy_hold | 9728.01 | -271.99 | buy / partial / 직전 완료 봉 목표 비중 100%; 다음 봉 시가 가정 |
| v2 | trend_8_26 | 9665.05 | -334.95 | buy / partial / 직전 완료 봉 목표 비중 100%; 다음 봉 시가 가정 |
| v2 | momentum_26 | 9679.82 | -320.18 | buy / partial / 직전 완료 봉 목표 비중 100%; 다음 봉 시가 가정 |
| v2 | breakout_8 | 9406.95 | -593.05 | sell / filled / 직전 완료 봉 목표 비중 0%; 다음 봉 시가 가정 |
| v2 | reversion_12 | 9388.38 | -611.62 | buy / partial / 직전 완료 봉 목표 비중 100%; 다음 봉 시가 가정 |
| v2 | volume_26 | 9378.42 | -621.58 | sell / filled / 직전 완료 봉 목표 비중 0%; 다음 봉 시가 가정 |
| v2 | trend_8_26 AND momentum_26 | 9829.05 | -170.95 | buy / partial / 직전 완료 봉 목표 비중 100%; 다음 봉 시가 가정 |
| v2 | trend_8_26 + momentum_26 | 9692.89 | -307.11 | buy / partial / 직전 완료 봉 목표 비중 100%; 다음 봉 시가 가정 |
| v2 | trend_8_26 AND breakout_8 | 9806.54 | -193.46 | sell / filled / 직전 완료 봉 목표 비중 0%; 다음 봉 시가 가정 |
| v2 | trend_8_26 + breakout_8 | 9555.29 | -444.71 | buy / filled / 직전 완료 봉 목표 비중 50%; 다음 봉 시가 가정 |
| v2 | trend_8_26 AND reversion_12 | 9770.48 | -229.52 | buy / partial / 직전 완료 봉 목표 비중 100%; 다음 봉 시가 가정 |
| v2 | trend_8_26 + reversion_12 | 9525.47 | -474.53 | buy / partial / 직전 완료 봉 목표 비중 100%; 다음 봉 시가 가정 |
| v2 | trend_8_26 AND volume_26 | 9797.73 | -202.27 | sell / filled / 직전 완료 봉 목표 비중 0%; 다음 봉 시가 가정 |
| v2 | trend_8_26 + volume_26 | 9540.57 | -459.43 | buy / filled / 직전 완료 봉 목표 비중 50%; 다음 봉 시가 가정 |
| v2 | momentum_26 AND breakout_8 | 9733.71 | -266.29 | sell / filled / 직전 완료 봉 목표 비중 0%; 다음 봉 시가 가정 |
| v2 | momentum_26 + breakout_8 | 9562.45 | -437.55 | buy / filled / 직전 완료 봉 목표 비중 50%; 다음 봉 시가 가정 |
| v2 | momentum_26 AND reversion_12 | 9947.59 | -52.41 | buy / partial / 직전 완료 봉 목표 비중 100%; 다음 봉 시가 가정 |
| v2 | momentum_26 + reversion_12 | 9572.63 | -427.37 | buy / partial / 직전 완료 봉 목표 비중 100%; 다음 봉 시가 가정 |
| v2 | momentum_26 AND volume_26 | 9897.79 | -102.21 | sell / filled / 직전 완료 봉 목표 비중 0%; 다음 봉 시가 가정 |
| v2 | momentum_26 + volume_26 | 9527.64 | -472.36 | buy / filled / 직전 완료 봉 목표 비중 50%; 다음 봉 시가 가정 |
| v2 | breakout_8 AND reversion_12 | 10000.00 | 0.00 | 대기 /  / 새 신호 대기 |
| v2 | breakout_8 + reversion_12 | 9436.73 | -563.27 | buy / filled / 직전 완료 봉 목표 비중 50%; 다음 봉 시가 가정 |
| v2 | breakout_8 AND volume_26 | 9690.16 | -309.84 | sell / filled / 직전 완료 봉 목표 비중 0%; 다음 봉 시가 가정 |
| v2 | breakout_8 + volume_26 | 9412.30 | -587.70 | sell / filled / 직전 완료 봉 목표 비중 0%; 다음 봉 시가 가정 |
| v2 | reversion_12 AND volume_26 | 9676.46 | -323.54 | sell / filled / 직전 완료 봉 목표 비중 0%; 다음 봉 시가 가정 |
| v2 | reversion_12 + volume_26 | 9422.64 | -577.36 | buy / filled / 직전 완료 봉 목표 비중 50%; 다음 봉 시가 가정 |
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
| v2 | aroon_25_trend | 9847.27 | -152.73 | buy / partial / Aroon25 Up > 70 그리고 Down < 30 (동률이면 최신 극값); 조건 충족; Aroon_up=76, Aroon_down=28; 직전 완료 봉 목표를 다음 봉 시가에 모의 적용 |
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
| cash | 0.00% | 0.00% | -3.50% | -0.00% | 0.00% |
| buy_hold | -3.09% | -3.50% | -3.50% | -3.50% | 100.00% |
| trend_8_26 | -1.50% | -5.15% | -3.50% | -1.54% | 43.83% |
| momentum_26 | -2.56% | -8.51% | -3.50% | -1.36% | 38.58% |
| breakout_8 | -0.55% | -13.78% | -3.50% | -0.70% | 19.95% |
| reversion_12 | -2.36% | -14.99% | -3.50% | -1.07% | 30.45% |
| volume_26 | -2.82% | -9.90% | -3.50% | -0.31% | 8.66% |
| trend_8_26 AND momentum_26 | -1.44% | -5.89% | -3.50% | -1.18% | 33.60% |
| trend_8_26 + momentum_26 | -2.02% | -6.45% | -3.50% | -1.45% | 41.21% |
| trend_8_26 AND breakout_8 | -0.38% | -8.02% | -3.50% | -0.41% | 11.55% |
| trend_8_26 + breakout_8 | -1.01% | -9.38% | -3.50% | -1.12% | 31.90% |
| trend_8_26 AND reversion_12 | -0.68% | -5.16% | -3.50% | -0.19% | 5.51% |
| trend_8_26 + reversion_12 | -1.92% | -10.02% | -3.50% | -1.31% | 37.14% |
| trend_8_26 AND volume_26 | -1.20% | -4.47% | -3.50% | -0.11% | 3.15% |
| trend_8_26 + volume_26 | -2.15% | -7.36% | -3.50% | -0.93% | 26.25% |
| momentum_26 AND breakout_8 | -0.21% | -7.48% | -3.50% | -0.36% | 10.24% |
| momentum_26 + breakout_8 | -1.55% | -11.00% | -3.50% | -1.03% | 29.27% |
| momentum_26 AND reversion_12 | 0.07% | -3.24% | -3.50% | -0.09% | 2.62% |
| momentum_26 + reversion_12 | -2.45% | -10.51% | -3.50% | -1.22% | 34.52% |
| momentum_26 AND volume_26 | -1.25% | -3.30% | -3.50% | -0.06% | 1.57% |
| momentum_26 + volume_26 | -2.69% | -8.83% | -3.50% | -0.83% | 23.63% |
| breakout_8 AND reversion_12 | 0.00% | 0.00% | -3.50% | -0.00% | 0.00% |
| breakout_8 + reversion_12 | -1.45% | -13.68% | -3.50% | -0.89% | 25.21% |
| breakout_8 AND volume_26 | -1.46% | -4.31% | -3.50% | -0.08% | 2.36% |
| breakout_8 + volume_26 | -1.69% | -11.68% | -3.50% | -0.51% | 14.31% |
| reversion_12 AND volume_26 | -0.55% | -4.64% | -3.50% | -0.15% | 4.20% |
| reversion_12 + volume_26 | -2.59% | -11.75% | -3.50% | -0.69% | 19.56% |
| ema_12_26 | -0.23% | -2.71% | -3.50% | -1.52% | 43.04% |
| macd_12_26_9 | 1.54% | -0.99% | -3.50% | -0.98% | 27.82% |
| rsi_14_recovery | -0.86% | -6.52% | -3.50% | -0.13% | 3.67% |
| bollinger_20_reentry | -0.31% | -4.81% | -3.50% | -0.10% | 2.89% |
| donchian_20 | -0.20% | -5.10% | -3.50% | -0.19% | 5.51% |
| atr_14_breakout | -1.18% | -7.22% | -3.50% | -0.14% | 3.94% |
| session_vwap | -0.81% | -10.32% | -3.50% | -1.41% | 39.90% |
| obv_20 | 0.29% | -3.43% | -3.50% | -1.34% | 38.06% |
| stochastic_14_3_recovery | -1.20% | -15.06% | -3.50% | -0.33% | 9.45% |
| mfi_14_recovery | 0.24% | -3.88% | -3.50% | -0.09% | 2.62% |
| adx_14_trend | 0.00% | -3.30% | -3.50% | -1.09% | 30.97% |
| aroon_25_trend | -1.62% | -5.27% | -3.50% | -0.73% | 20.73% |
| cci_20_momentum | -2.04% | -8.41% | -3.50% | -0.65% | 18.37% |
| williams_14_recovery | -0.58% | -10.11% | -3.50% | -0.22% | 6.30% |
| cmf_20_accumulation | -1.81% | -7.80% | -3.50% | -0.62% | 17.59% |
| chaikin_3_10 | -1.82% | -7.82% | -3.50% | -1.09% | 30.97% |
| roc_10_momentum | -0.63% | -1.87% | -3.50% | -0.11% | 3.15% |
| trix_15_trend | 0.35% | -2.56% | -3.50% | -1.10% | 31.23% |
| keltner_20_breakout | -0.91% | -4.18% | -3.50% | -0.19% | 5.25% |
| opening_range_30m | 2.57% | -1.23% | -3.50% | -0.75% | 21.26% |

동일 구간·초기 자금, 종료 시 청산 비용 포함. 노출 맞춤은 사후 설명용이며 v2 실제 계좌 성과가 아닙니다.
[낙폭 분해·비용 영향·전체 구간](IWM/comparison.json)

[v1 전체 기록](IWM/accounts.json) · [v2 전체 기록](IWM/accounts-v2.json)

## DIA 계좌

| 모델 | 전략 | 평가액 USD | 손익 USD | 최근 매매·이유 |
|---|---|---:|---:|---|
| v1 | cash | 10000.00 | 0.00 | 대기 /  / 새 신호 대기 |
| v1 | buy_hold | 9909.31 | -90.69 | buy /  / buy_hold: prior completed bar target 100%; next bar open simulation |
| v1 | trend_8_26 | 9868.05 | -131.95 | buy /  / trend_8_26: prior completed bar target 100%; next bar open simulation |
| v1 | momentum_26 | 9892.19 | -107.81 | buy /  / momentum_26: prior completed bar target 100%; next bar open simulation |
| v1 | breakout_8 | 9806.43 | -193.57 | sell /  / breakout_8: prior completed bar target 0%; next bar open simulation |
| v1 | reversion_12 | 9892.53 | -107.47 | sell /  / reversion_12: prior completed bar target 0%; next bar open simulation |
| v1 | volume_26 | 9908.95 | -91.05 | sell /  / volume_26: prior completed bar target 0%; next bar open simulation |
| v1 | trend_8_26 AND momentum_26 | 9892.19 | -107.81 | buy /  / trend_8_26 AND momentum_26: prior completed bar target 100%; next bar open simulation |
| v1 | trend_8_26 + momentum_26 | 9880.09 | -119.91 | buy /  / trend_8_26 + momentum_26: prior completed bar target 100%; next bar open simulation |
| v1 | trend_8_26 AND breakout_8 | 9940.12 | -59.88 | sell /  / trend_8_26 AND breakout_8: prior completed bar target 0%; next bar open simulation |
| v1 | trend_8_26 + breakout_8 | 9856.81 | -143.19 | buy /  / trend_8_26 + breakout_8: prior completed bar target 50%; next bar open simulation |
| v1 | trend_8_26 AND reversion_12 | 9936.00 | -64.00 | sell /  / trend_8_26 AND reversion_12: prior completed bar target 0%; next bar open simulation |
| v1 | trend_8_26 + reversion_12 | 9880.17 | -119.83 | buy /  / trend_8_26 + reversion_12: prior completed bar target 50%; next bar open simulation |
| v1 | trend_8_26 AND volume_26 | 9943.10 | -56.90 | sell /  / trend_8_26 AND volume_26: prior completed bar target 0%; next bar open simulation |
| v1 | trend_8_26 + volume_26 | 9888.38 | -111.62 | buy /  / trend_8_26 + volume_26: prior completed bar target 50%; next bar open simulation |
| v1 | momentum_26 AND breakout_8 | 9940.12 | -59.88 | sell /  / momentum_26 AND breakout_8: prior completed bar target 0%; next bar open simulation |
| v1 | momentum_26 + breakout_8 | 9849.15 | -150.85 | buy /  / momentum_26 + breakout_8: prior completed bar target 50%; next bar open simulation |
| v1 | momentum_26 AND reversion_12 | 9940.78 | -59.22 | sell /  / momentum_26 AND reversion_12: prior completed bar target 0%; next bar open simulation |
| v1 | momentum_26 + reversion_12 | 9892.26 | -107.74 | buy /  / momentum_26 + reversion_12: prior completed bar target 50%; next bar open simulation |
| v1 | momentum_26 AND volume_26 | 9943.10 | -56.90 | sell /  / momentum_26 AND volume_26: prior completed bar target 0%; next bar open simulation |
| v1 | momentum_26 + volume_26 | 9900.49 | -99.51 | buy /  / momentum_26 + volume_26: prior completed bar target 50%; next bar open simulation |
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
| v1 | session_vwap | 9903.46 | -96.54 | buy /  / 종가 > 뉴욕 거래일별 누적 전형가격 VWAP; 조건 충족; close=519.01, session_VWAP=518.623, session_volume=840642 |
| v1 | obv_20 | 9880.35 | -119.65 | sell /  / OBV > OBV의 SMA20 그리고 종가 > EMA26; 조건 미충족; OBV=-9.70764e+06, OBV_SMA20=-9.69418e+06, close=520.09, EMA26=519.448 |
| v1 | stochastic_14_3_recovery | 9821.75 | -178.25 | sell /  / 직전 %K14 < 20에서 %K14가 %D3 상향 돌파 (한 봉 목표); 조건 미충족; K14=21.4008, D3=27.0401, previous_K14=46.6025, previous_D3=27.3524 |
| v1 | mfi_14_recovery | 9936.38 | -63.62 | sell /  / 직전 MFI14 < 20, 현재 MFI14 >= 20 (한 봉 목표); 조건 미충족; MFI14=44.8014, previous_MFI14=20.0271 |
| v1 | adx_14_trend | 9882.74 | -117.26 | sell /  / Wilder ADX14 >= 25 그리고 +DI14 > -DI14; 조건 미충족; ADX14=30.2264, plus_DI14=23.4608, minus_DI14=27.9688 |
| v1 | aroon_25_trend | 9906.25 | -93.75 | buy /  / Aroon25 Up > 70 그리고 Down < 30 (동률이면 최신 극값); 조건 충족; Aroon_up=76, Aroon_down=28 |
| v1 | cci_20_momentum | 9910.36 | -89.64 | sell /  / CCI20 > 100 (전형가격·평균절대편차); 조건 미충족; CCI20=46.8763 |
| v1 | williams_14_recovery | 9855.05 | -144.95 | sell /  / 직전 Williams %R14 < -80, 현재 >= -80 (한 봉 목표); 조건 미충족; Williams_R14=-78.5992, previous_R14=-53.3975 |
| v1 | cmf_20_accumulation | 9891.50 | -108.50 | buy /  / Chaikin Money Flow20 > 0.1; 조건 충족; CMF20=0.211244, volume20=2.96677e+06 |
| v1 | chaikin_3_10 | 9882.27 | -117.73 | sell /  / ADL의 EMA3 - EMA10 > 0 그리고 종가 > EMA26; 조건 미충족; Chaikin3_10=16638.1, ADL=-1.73546e+07, close=519.25, EMA26=519.462 |
| v1 | roc_10_momentum | 10000.00 | 0.00 | 대기 /  / 새 신호 대기 |
| v1 | trix_15_trend | 9928.27 | -71.73 | sell /  / 15봉 삼중 EMA의 1봉 변화율 TRIX > 0 그리고 종가 > EMA26; 조건 미충족; TRIX15_percent=0.0322153, close=521.26, EMA26=521.365 |
| v1 | keltner_20_breakout | 9940.12 | -59.88 | sell /  / 종가 > EMA20 + 2 x Wilder ATR14; 조건 미충족; close=522.89, upper_Keltner=523.089, EMA20=521.145, ATR14=0.971947 |
| v1 | opening_range_30m | 9871.63 | -128.37 | sell /  / 뉴욕 09:30·09:45 두 완료 봉 최고가를 10:00 이후 종가가 돌파; 조건 미충족; close=519.04, opening_high=519.1 |
| v2 | cash | 10000.00 | 0.00 | 대기 /  / 새 신호 대기 |
| v2 | buy_hold | 10032.08 | 32.08 | buy / partial / 직전 완료 봉 목표 비중 100%; 다음 봉 시가 가정 |
| v2 | trend_8_26 | 9802.16 | -197.84 | buy / partial / 직전 완료 봉 목표 비중 100%; 다음 봉 시가 가정 |
| v2 | momentum_26 | 9934.18 | -65.82 | buy / partial / 직전 완료 봉 목표 비중 100%; 다음 봉 시가 가정 |
| v2 | breakout_8 | 9333.71 | -666.29 | sell / filled / 직전 완료 봉 목표 비중 0%; 다음 봉 시가 가정 |
| v2 | reversion_12 | 9589.97 | -410.03 | sell / filled / 직전 완료 봉 목표 비중 0%; 다음 봉 시가 가정 |
| v2 | volume_26 | 9625.87 | -374.13 | sell / filled / 직전 완료 봉 목표 비중 0%; 다음 봉 시가 가정 |
| v2 | trend_8_26 AND momentum_26 | 9929.57 | -70.43 | buy / partial / 직전 완료 봉 목표 비중 100%; 다음 봉 시가 가정 |
| v2 | trend_8_26 + momentum_26 | 9867.99 | -132.01 | buy / partial / 직전 완료 봉 목표 비중 100%; 다음 봉 시가 가정 |
| v2 | trend_8_26 AND breakout_8 | 9626.81 | -373.19 | sell / filled / 직전 완료 봉 목표 비중 0%; 다음 봉 시가 가정 |
| v2 | trend_8_26 + breakout_8 | 9585.17 | -414.83 | buy / filled / 직전 완료 봉 목표 비중 50%; 다음 봉 시가 가정 |
| v2 | trend_8_26 AND reversion_12 | 9746.03 | -253.97 | sell / filled / 직전 완료 봉 목표 비중 0%; 다음 봉 시가 가정 |
| v2 | trend_8_26 + reversion_12 | 9695.12 | -304.88 | buy / filled / 직전 완료 봉 목표 비중 50%; 다음 봉 시가 가정 |
| v2 | trend_8_26 AND volume_26 | 9800.82 | -199.18 | sell / filled / 직전 완료 봉 목표 비중 0%; 다음 봉 시가 가정 |
| v2 | trend_8_26 + volume_26 | 9733.89 | -266.11 | buy / filled / 직전 완료 봉 목표 비중 50%; 다음 봉 시가 가정 |
| v2 | momentum_26 AND breakout_8 | 9615.85 | -384.15 | sell / filled / 직전 완료 봉 목표 비중 0%; 다음 봉 시가 가정 |
| v2 | momentum_26 + breakout_8 | 9629.33 | -370.67 | buy / filled / 직전 완료 봉 목표 비중 50%; 다음 봉 시가 가정 |
| v2 | momentum_26 AND reversion_12 | 9895.03 | -104.97 | sell / filled / 직전 완료 봉 목표 비중 0%; 다음 봉 시가 가정 |
| v2 | momentum_26 + reversion_12 | 9760.28 | -239.72 | buy / filled / 직전 완료 봉 목표 비중 50%; 다음 봉 시가 가정 |
| v2 | momentum_26 AND volume_26 | 9733.77 | -266.23 | sell / filled / 직전 완료 봉 목표 비중 0%; 다음 봉 시가 가정 |
| v2 | momentum_26 + volume_26 | 9819.98 | -180.02 | buy / filled / 직전 완료 봉 목표 비중 50%; 다음 봉 시가 가정 |
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
| v2 | session_vwap | 9898.51 | -101.49 | buy / partial / 종가 > 뉴욕 거래일별 누적 전형가격 VWAP; 조건 충족; close=519.01, session_VWAP=518.623, session_volume=840642; 직전 완료 봉 목표를 다음 봉 시가에 모의 적용 |
| v2 | obv_20 | 9876.40 | -123.60 | sell / filled / OBV > OBV의 SMA20 그리고 종가 > EMA26; 조건 미충족; OBV=-9.70764e+06, OBV_SMA20=-9.69418e+06, close=520.09, EMA26=519.448; 직전 완료 봉 목표를 다음 봉 시가에 모의 적용 |
| v2 | stochastic_14_3_recovery | 9813.90 | -186.10 | sell / filled / 직전 %K14 < 20에서 %K14가 %D3 상향 돌파 (한 봉 목표); 조건 미충족; K14=21.4008, D3=27.0401, previous_K14=46.6025, previous_D3=27.3524; 직전 완료 봉 목표를 다음 봉 시가에 모의 적용 |
| v2 | mfi_14_recovery | 9932.40 | -67.60 | sell / filled / 직전 MFI14 < 20, 현재 MFI14 >= 20 (한 봉 목표); 조건 미충족; MFI14=44.8014, previous_MFI14=20.0271; 직전 완료 봉 목표를 다음 봉 시가에 모의 적용 |
| v2 | adx_14_trend | 9878.79 | -121.21 | sell / filled / Wilder ADX14 >= 25 그리고 +DI14 > -DI14; 조건 미충족; ADX14=30.2264, plus_DI14=23.4608, minus_DI14=27.9688; 직전 완료 봉 목표를 다음 봉 시가에 모의 적용 |
| v2 | aroon_25_trend | 9903.28 | -96.72 | buy / partial / Aroon25 Up > 70 그리고 Down < 30 (동률이면 최신 극값); 조건 충족; Aroon_up=76, Aroon_down=28; 직전 완료 봉 목표를 다음 봉 시가에 모의 적용 |
| v2 | cci_20_momentum | 9906.40 | -93.60 | sell / filled / CCI20 > 100 (전형가격·평균절대편차); 조건 미충족; CCI20=46.8763; 직전 완료 봉 목표를 다음 봉 시가에 모의 적용 |
| v2 | williams_14_recovery | 9849.14 | -150.86 | sell / filled / 직전 Williams %R14 < -80, 현재 >= -80 (한 봉 목표); 조건 미충족; Williams_R14=-78.5992, previous_R14=-53.3975; 직전 완료 봉 목표를 다음 봉 시가에 모의 적용 |
| v2 | cmf_20_accumulation | 9888.53 | -111.47 | buy / partial / Chaikin Money Flow20 > 0.1; 조건 충족; CMF20=0.211244, volume20=2.96677e+06; 직전 완료 봉 목표를 다음 봉 시가에 모의 적용 |
| v2 | chaikin_3_10 | 9878.32 | -121.68 | sell / filled / ADL의 EMA3 - EMA10 > 0 그리고 종가 > EMA26; 조건 미충족; Chaikin3_10=16638.1, ADL=-1.73546e+07, close=519.25, EMA26=519.462; 직전 완료 봉 목표를 다음 봉 시가에 모의 적용 |
| v2 | roc_10_momentum | 10000.00 | 0.00 | 대기 /  / 새 신호 대기 |
| v2 | trix_15_trend | 9926.28 | -73.72 | sell / filled / 15봉 삼중 EMA의 1봉 변화율 TRIX > 0 그리고 종가 > EMA26; 조건 미충족; TRIX15_percent=0.0322153, close=521.26, EMA26=521.365; 직전 완료 봉 목표를 다음 봉 시가에 모의 적용 |
| v2 | keltner_20_breakout | 9938.13 | -61.87 | sell / filled / 종가 > EMA20 + 2 x Wilder ATR14; 조건 미충족; close=522.89, upper_Keltner=523.089, EMA20=521.145, ATR14=0.971947; 직전 완료 봉 목표를 다음 봉 시가에 모의 적용 |
| v2 | opening_range_30m | 9865.71 | -134.29 | sell / filled / 뉴욕 09:30·09:45 두 완료 봉 최고가를 10:00 이후 종가가 돌파; 조건 미충족; close=519.04, opening_high=519.1; 직전 완료 봉 목표를 다음 봉 시가에 모의 적용 |

### 같은 기간의 비용·노출 비교 (사후 연구)

| 전략 | 비용 전 | 비용 후 | 100% 보유 | 같은 평균 노출 보유 | 평균 노출 |
|---|---:|---:|---:|---:|---:|
| cash | 0.00% | 0.00% | 0.55% | 0.00% | 0.00% |
| buy_hold | 0.97% | 0.55% | 0.55% | 0.55% | 100.00% |
| trend_8_26 | 1.27% | -2.49% | 0.55% | 0.30% | 55.38% |
| momentum_26 | 0.33% | -3.39% | 0.55% | 0.28% | 50.39% |
| breakout_8 | 0.79% | -16.21% | 0.55% | 0.13% | 23.10% |
| reversion_12 | -1.63% | -9.55% | 0.55% | 0.14% | 25.46% |
| volume_26 | -0.92% | -10.79% | 0.55% | 0.06% | 10.50% |
| trend_8_26 AND momentum_26 | 1.44% | -2.32% | 0.55% | 0.25% | 45.14% |
| trend_8_26 + momentum_26 | 0.80% | -2.94% | 0.55% | 0.29% | 52.89% |
| trend_8_26 AND breakout_8 | 1.06% | -10.53% | 0.55% | 0.08% | 14.70% |
| trend_8_26 + breakout_8 | 1.03% | -9.23% | 0.55% | 0.22% | 39.25% |
| trend_8_26 AND reversion_12 | -0.02% | -4.93% | 0.55% | 0.04% | 6.56% |
| trend_8_26 + reversion_12 | -0.19% | -5.90% | 0.55% | 0.22% | 40.42% |
| trend_8_26 AND volume_26 | 0.36% | -4.57% | 0.55% | 0.03% | 4.72% |
| trend_8_26 + volume_26 | 0.17% | -6.54% | 0.55% | 0.18% | 32.94% |
| momentum_26 AND breakout_8 | 0.26% | -10.87% | 0.55% | 0.08% | 14.96% |
| momentum_26 + breakout_8 | 0.57% | -9.84% | 0.55% | 0.20% | 36.75% |
| momentum_26 AND reversion_12 | -0.27% | -3.57% | 0.55% | 0.03% | 5.77% |
| momentum_26 + reversion_12 | -0.65% | -5.94% | 0.55% | 0.21% | 37.93% |
| momentum_26 AND volume_26 | -0.56% | -5.45% | 0.55% | 0.02% | 4.46% |
| momentum_26 + volume_26 | -0.29% | -6.58% | 0.55% | 0.17% | 30.45% |
| breakout_8 AND reversion_12 | 0.00% | 0.00% | 0.55% | 0.00% | 0.00% |
| breakout_8 + reversion_12 | -0.42% | -12.78% | 0.55% | 0.13% | 24.29% |
| breakout_8 AND volume_26 | -0.73% | -3.60% | 0.55% | 0.01% | 2.62% |
| breakout_8 + volume_26 | -0.06% | -12.82% | 0.55% | 0.09% | 16.81% |
| reversion_12 AND volume_26 | -0.19% | -5.09% | 0.55% | 0.02% | 3.94% |
| reversion_12 + volume_26 | -1.27% | -9.99% | 0.55% | 0.10% | 17.98% |
| ema_12_26 | 0.17% | -1.91% | 0.55% | 0.27% | 48.82% |
| macd_12_26_9 | 1.65% | -1.30% | 0.55% | 0.15% | 27.56% |
| rsi_14_recovery | 0.01% | -2.07% | 0.55% | 0.01% | 1.31% |
| bollinger_20_reentry | -0.09% | -5.00% | 0.55% | 0.02% | 3.15% |
| donchian_20 | 0.31% | -6.21% | 0.55% | 0.05% | 8.40% |
| atr_14_breakout | -0.66% | -7.51% | 0.55% | 0.03% | 5.25% |
| session_vwap | 2.09% | -5.74% | 0.55% | 0.27% | 48.29% |
| obv_20 | 0.66% | -6.67% | 0.55% | 0.23% | 41.21% |
| stochastic_14_3_recovery | 0.56% | -12.45% | 0.55% | 0.05% | 8.66% |
| mfi_14_recovery | 0.10% | -3.61% | 0.55% | 0.01% | 2.36% |
| adx_14_trend | 0.20% | -3.52% | 0.55% | 0.18% | 32.55% |
| aroon_25_trend | 0.53% | -2.80% | 0.55% | 0.14% | 25.46% |
| cci_20_momentum | 0.61% | -5.53% | 0.55% | 0.14% | 24.93% |
| williams_14_recovery | 0.97% | -7.55% | 0.55% | 0.03% | 5.51% |
| cmf_20_accumulation | 0.90% | -6.05% | 0.55% | 0.15% | 26.51% |
| chaikin_3_10 | 1.87% | -6.73% | 0.55% | 0.22% | 40.68% |
| roc_10_momentum | 0.15% | -0.27% | 0.55% | 0.01% | 1.31% |
| trix_15_trend | 0.19% | -3.12% | 0.55% | 0.23% | 41.99% |
| keltner_20_breakout | 0.33% | -5.79% | 0.55% | 0.09% | 16.80% |
| opening_range_30m | 1.76% | -3.24% | 0.55% | 0.12% | 21.52% |

동일 구간·초기 자금, 종료 시 청산 비용 포함. 노출 맞춤은 사후 설명용이며 v2 실제 계좌 성과가 아닙니다.
[낙폭 분해·비용 영향·전체 구간](DIA/comparison.json)

[v1 전체 기록](DIA/accounts.json) · [v2 전체 기록](DIA/accounts-v2.json)

## MSFT 계좌

| 모델 | 전략 | 평가액 USD | 손익 USD | 최근 매매·이유 |
|---|---|---:|---:|---|
| v1 | cash | 10000.00 | 0.00 | 대기 /  / 새 신호 대기 |
| v1 | buy_hold | 9840.11 | -159.89 | buy /  / buy_hold: prior completed bar target 100%; next bar open simulation |
| v1 | trend_8_26 | 9822.66 | -177.34 | buy /  / trend_8_26: prior completed bar target 100%; next bar open simulation |
| v1 | momentum_26 | 9793.68 | -206.32 | buy /  / momentum_26: prior completed bar target 100%; next bar open simulation |
| v1 | breakout_8 | 9876.66 | -123.34 | sell /  / breakout_8: prior completed bar target 0%; next bar open simulation |
| v1 | reversion_12 | 9784.88 | -215.12 | buy /  / reversion_12: prior completed bar target 100%; next bar open simulation |
| v1 | volume_26 | 9811.31 | -188.69 | sell /  / volume_26: prior completed bar target 0%; next bar open simulation |
| v1 | trend_8_26 AND momentum_26 | 9807.97 | -192.03 | buy /  / trend_8_26 AND momentum_26: prior completed bar target 100%; next bar open simulation |
| v1 | trend_8_26 + momentum_26 | 9808.18 | -191.82 | buy /  / trend_8_26 + momentum_26: prior completed bar target 100%; next bar open simulation |
| v1 | trend_8_26 AND breakout_8 | 9905.03 | -94.97 | sell /  / trend_8_26 AND breakout_8: prior completed bar target 0%; next bar open simulation |
| v1 | trend_8_26 + breakout_8 | 9869.34 | -130.66 | sell /  / trend_8_26 + breakout_8: prior completed bar target 50%; next bar open simulation |
| v1 | trend_8_26 AND reversion_12 | 9906.61 | -93.39 | buy /  / trend_8_26 AND reversion_12: prior completed bar target 100%; next bar open simulation |
| v1 | trend_8_26 + reversion_12 | 9803.71 | -196.29 | buy /  / trend_8_26 + reversion_12: prior completed bar target 100%; next bar open simulation |
| v1 | trend_8_26 AND volume_26 | 9916.79 | -83.21 | sell /  / trend_8_26 AND volume_26: prior completed bar target 0%; next bar open simulation |
| v1 | trend_8_26 + volume_26 | 9816.94 | -183.06 | sell /  / trend_8_26 + volume_26: prior completed bar target 50%; next bar open simulation |
| v1 | momentum_26 AND breakout_8 | 9905.03 | -94.97 | sell /  / momentum_26 AND breakout_8: prior completed bar target 0%; next bar open simulation |
| v1 | momentum_26 + breakout_8 | 9835.07 | -164.93 | sell /  / momentum_26 + breakout_8: prior completed bar target 50%; next bar open simulation |
| v1 | momentum_26 AND reversion_12 | 9892.17 | -107.83 | buy /  / momentum_26 AND reversion_12: prior completed bar target 100%; next bar open simulation |
| v1 | momentum_26 + reversion_12 | 9789.24 | -210.76 | buy /  / momentum_26 + reversion_12: prior completed bar target 100%; next bar open simulation |
| v1 | momentum_26 AND volume_26 | 9916.79 | -83.21 | sell /  / momentum_26 AND volume_26: prior completed bar target 0%; next bar open simulation |
| v1 | momentum_26 + volume_26 | 9802.45 | -197.55 | sell /  / momentum_26 + volume_26: prior completed bar target 50%; next bar open simulation |
| v1 | breakout_8 AND reversion_12 | 10000.00 | 0.00 | 대기 /  / 새 신호 대기 |
| v1 | breakout_8 + reversion_12 | 9850.25 | -149.75 | sell /  / breakout_8 + reversion_12: prior completed bar target 50%; next bar open simulation |
| v1 | breakout_8 AND volume_26 | 9953.19 | -46.81 | sell /  / breakout_8 AND volume_26: prior completed bar target 0%; next bar open simulation |
| v1 | breakout_8 + volume_26 | 9863.58 | -136.42 | sell /  / breakout_8 + volume_26: prior completed bar target 0%; next bar open simulation |
| v1 | reversion_12 AND volume_26 | 9938.00 | -62.00 | sell /  / reversion_12 AND volume_26: prior completed bar target 0%; next bar open simulation |
| v1 | reversion_12 + volume_26 | 9797.97 | -202.03 | sell /  / reversion_12 + volume_26: prior completed bar target 50%; next bar open simulation |
| v1 | ema_12_26 | 9807.97 | -192.03 | buy /  / EMA12 > EMA26; 조건 충족; EMA12=531.372, EMA26=531.07 |
| v1 | macd_12_26_9 | 9844.07 | -155.93 | buy /  / MACD > 신호선 그리고 MACD > 0; 조건 충족; MACD=0.301143, signal9=-0.952827 |
| v1 | rsi_14_recovery | 9960.54 | -39.46 | sell /  / 직전 RSI14 < 30, 현재 RSI14 >= 30 (한 봉 목표); 조건 미충족; RSI14=56.2522, previous_RSI14=46.6115 |
| v1 | bollinger_20_reentry | 9885.00 | -115.00 | sell /  / 직전 종가 < 직전 하단밴드, 현재 하단밴드 <= 종가 <= SMA20 (한 봉 목표); 조건 미충족; close=529.125, lower20=527.516, SMA20=535.918, previous_lower20=528.497 |
| v1 | donchian_20 | 9912.16 | -87.84 | sell /  / 종가 > 현재 봉을 제외한 직전 20봉 최고가; 조건 미충족; close=534.52, prior_high20=535.44 |
| v1 | atr_14_breakout | 9915.10 | -84.90 | sell /  / 종가 > 직전 종가 + 직전 ATR14 그리고 종가 > EMA26; 조건 미충족; close=533.975, threshold=536.307, prior_ATR14=2.16203, EMA26=530.521 |
| v1 | session_vwap | 9894.65 | -105.35 | sell /  / 종가 > 뉴욕 거래일별 누적 전형가격 VWAP; 조건 미충족; close=534.125, session_VWAP=534.159, session_volume=2.7999e+07 |
| v1 | obv_20 | 9798.38 | -201.62 | sell /  / OBV > OBV의 SMA20 그리고 종가 > EMA26; 조건 미충족; OBV=1.07848e+08, OBV_SMA20=1.07988e+08, close=533.345, EMA26=532.447 |
| v1 | stochastic_14_3_recovery | 9792.37 | -207.63 | sell /  / 직전 %K14 < 20에서 %K14가 %D3 상향 돌파 (한 봉 목표); 조건 미충족; K14=25.4855, D3=14.0848, previous_K14=10.0077, previous_D3=7.52857 |
| v1 | mfi_14_recovery | 10009.36 | 9.36 | sell /  / 직전 MFI14 < 20, 현재 MFI14 >= 20 (한 봉 목표); 조건 미충족; MFI14=25.2915, previous_MFI14=22.266 |
| v1 | adx_14_trend | 9883.62 | -116.38 | sell /  / Wilder ADX14 >= 25 그리고 +DI14 > -DI14; 조건 미충족; ADX14=23.6824, plus_DI14=22.3066, minus_DI14=19.9214 |
| v1 | aroon_25_trend | 9823.64 | -176.36 | buy /  / Aroon25 Up > 70 그리고 Down < 30 (동률이면 최신 극값); 조건 충족; Aroon_up=92, Aroon_down=28 |
| v1 | cci_20_momentum | 10012.15 | 12.15 | sell /  / CCI20 > 100 (전형가격·평균절대편차); 조건 미충족; CCI20=86.441 |
| v1 | williams_14_recovery | 9822.57 | -177.43 | sell /  / 직전 Williams %R14 < -80, 현재 >= -80 (한 봉 목표); 조건 미충족; Williams_R14=-78.4506, previous_R14=-77.7733 |
| v1 | cmf_20_accumulation | 9748.54 | -251.46 | buy /  / Chaikin Money Flow20 > 0.1; 조건 충족; CMF20=0.184396, volume20=3.37825e+07 |
| v1 | chaikin_3_10 | 9834.97 | -165.03 | sell /  / ADL의 EMA3 - EMA10 > 0 그리고 종가 > EMA26; 조건 미충족; Chaikin3_10=-39308.5, ADL=1.1146e+08, close=533.345, EMA26=532.447 |
| v1 | roc_10_momentum | 9959.43 | -40.57 | sell /  / 10봉 ROC > 1% 그리고 종가 > EMA26; 조건 미충족; ROC10_percent=0.454191, close=534.125, EMA26=532.186 |
| v1 | trix_15_trend | 9858.17 | -141.83 | buy /  / 15봉 삼중 EMA의 1봉 변화율 TRIX > 0 그리고 종가 > EMA26; 조건 충족; TRIX15_percent=0.00435677, close=534.125, EMA26=532.186 |
| v1 | keltner_20_breakout | 9958.78 | -41.22 | sell /  / 종가 > EMA20 + 2 x Wilder ATR14; 조건 미충족; close=533.975, upper_Keltner=534.357, EMA20=530.111, ATR14=2.12332 |
| v1 | opening_range_30m | 9857.52 | -142.48 | buy /  / 뉴욕 09:30·09:45 두 완료 봉 최고가를 10:00 이후 종가가 돌파; 조건 충족; close=534.145, opening_high=532.63 |
| v2 | cash | 10000.00 | 0.00 | 대기 /  / 새 신호 대기 |
| v2 | buy_hold | 9893.80 | -106.20 | buy / partial / 직전 완료 봉 목표 비중 100%; 다음 봉 시가 가정 |
| v2 | trend_8_26 | 9758.38 | -241.62 | buy / partial / 직전 완료 봉 목표 비중 100%; 다음 봉 시가 가정 |
| v2 | momentum_26 | 9839.34 | -160.66 | buy / partial / 직전 완료 봉 목표 비중 100%; 다음 봉 시가 가정 |
| v2 | breakout_8 | 9670.87 | -329.13 | sell / filled / 직전 완료 봉 목표 비중 0%; 다음 봉 시가 가정 |
| v2 | reversion_12 | 9407.00 | -593.00 | buy / partial / 직전 완료 봉 목표 비중 100%; 다음 봉 시가 가정 |
| v2 | volume_26 | 9498.13 | -501.87 | sell / filled / 직전 완료 봉 목표 비중 0%; 다음 봉 시가 가정 |
| v2 | trend_8_26 AND momentum_26 | 9704.93 | -295.07 | buy / partial / 직전 완료 봉 목표 비중 100%; 다음 봉 시가 가정 |
| v2 | trend_8_26 + momentum_26 | 9799.05 | -200.95 | buy / partial / 직전 완료 봉 목표 비중 100%; 다음 봉 시가 가정 |
| v2 | trend_8_26 AND breakout_8 | 9543.92 | -456.08 | sell / filled / 직전 완료 봉 목표 비중 0%; 다음 봉 시가 가정 |
| v2 | trend_8_26 + breakout_8 | 9755.61 | -244.39 | sell / filled / 직전 완료 봉 목표 비중 50%; 다음 봉 시가 가정 |
| v2 | trend_8_26 AND reversion_12 | 9804.70 | -195.30 | buy / partial / 직전 완료 봉 목표 비중 100%; 다음 봉 시가 가정 |
| v2 | trend_8_26 + reversion_12 | 9580.70 | -419.30 | buy / partial / 직전 완료 봉 목표 비중 100%; 다음 봉 시가 가정 |
| v2 | trend_8_26 AND volume_26 | 9861.94 | -138.06 | sell / filled / 직전 완료 봉 목표 비중 0%; 다음 봉 시가 가정 |
| v2 | trend_8_26 + volume_26 | 9647.37 | -352.63 | sell / filled / 직전 완료 봉 목표 비중 50%; 다음 봉 시가 가정 |
| v2 | momentum_26 AND breakout_8 | 9697.48 | -302.52 | sell / filled / 직전 완료 봉 목표 비중 0%; 다음 봉 시가 가정 |
| v2 | momentum_26 + breakout_8 | 9754.80 | -245.20 | sell / filled / 직전 완료 봉 목표 비중 50%; 다음 봉 시가 가정 |
| v2 | momentum_26 AND reversion_12 | 9718.01 | -281.99 | buy / partial / 직전 완료 봉 목표 비중 100%; 다음 봉 시가 가정 |
| v2 | momentum_26 + reversion_12 | 9620.49 | -379.51 | buy / partial / 직전 완료 봉 목표 비중 100%; 다음 봉 시가 가정 |
| v2 | momentum_26 AND volume_26 | 9785.21 | -214.79 | sell / filled / 직전 완료 봉 목표 비중 0%; 다음 봉 시가 가정 |
| v2 | momentum_26 + volume_26 | 9687.45 | -312.55 | sell / filled / 직전 완료 봉 목표 비중 50%; 다음 봉 시가 가정 |
| v2 | breakout_8 AND reversion_12 | 10000.00 | 0.00 | 대기 /  / 새 신호 대기 |
| v2 | breakout_8 + reversion_12 | 9577.86 | -422.14 | sell / filled / 직전 완료 봉 목표 비중 50%; 다음 봉 시가 가정 |
| v2 | breakout_8 AND volume_26 | 9890.09 | -109.91 | sell / filled / 직전 완료 봉 목표 비중 0%; 다음 봉 시가 가정 |
| v2 | breakout_8 + volume_26 | 9624.43 | -375.57 | sell / filled / 직전 완료 봉 목표 비중 0%; 다음 봉 시가 가정 |
| v2 | reversion_12 AND volume_26 | 9699.57 | -300.43 | sell / filled / 직전 완료 봉 목표 비중 0%; 다음 봉 시가 가정 |
| v2 | reversion_12 + volume_26 | 9452.19 | -547.81 | sell / filled / 직전 완료 봉 목표 비중 50%; 다음 봉 시가 가정 |
| v2 | ema_12_26 | 9805.03 | -194.97 | buy / partial / EMA12 > EMA26; 조건 충족; EMA12=531.372, EMA26=531.07; 직전 완료 봉 목표를 다음 봉 시가에 모의 적용 |
| v2 | macd_12_26_9 | 9841.12 | -158.88 | buy / partial / MACD > 신호선 그리고 MACD > 0; 조건 충족; MACD=0.301143, signal9=-0.952827; 직전 완료 봉 목표를 다음 봉 시가에 모의 적용 |
| v2 | rsi_14_recovery | 9956.56 | -43.44 | sell / filled / 직전 RSI14 < 30, 현재 RSI14 >= 30 (한 봉 목표); 조건 미충족; RSI14=56.2522, previous_RSI14=46.6115; 직전 완료 봉 목표를 다음 봉 시가에 모의 적용 |
| v2 | bollinger_20_reentry | 9881.05 | -118.95 | sell / filled / 직전 종가 < 직전 하단밴드, 현재 하단밴드 <= 종가 <= SMA20 (한 봉 목표); 조건 미충족; close=529.125, lower20=527.516, SMA20=535.918, previous_lower20=528.497; 직전 완료 봉 목표를 다음 봉 시가에 모의 적용 |
| v2 | donchian_20 | 9908.19 | -91.81 | sell / filled / 종가 > 현재 봉을 제외한 직전 20봉 최고가; 조건 미충족; close=534.52, prior_high20=535.44; 직전 완료 봉 목표를 다음 봉 시가에 모의 적용 |
| v2 | atr_14_breakout | 9911.14 | -88.86 | sell / filled / 종가 > 직전 종가 + 직전 ATR14 그리고 종가 > EMA26; 조건 미충족; close=533.975, threshold=536.307, prior_ATR14=2.16203, EMA26=530.521; 직전 완료 봉 목표를 다음 봉 시가에 모의 적용 |
| v2 | session_vwap | 9890.69 | -109.31 | sell / filled / 종가 > 뉴욕 거래일별 누적 전형가격 VWAP; 조건 미충족; close=534.125, session_VWAP=534.159, session_volume=2.7999e+07; 직전 완료 봉 목표를 다음 봉 시가에 모의 적용 |
| v2 | obv_20 | 9792.50 | -207.50 | sell / filled / OBV > OBV의 SMA20 그리고 종가 > EMA26; 조건 미충족; OBV=1.07848e+08, OBV_SMA20=1.07988e+08, close=533.345, EMA26=532.447; 직전 완료 봉 목표를 다음 봉 시가에 모의 적용 |
| v2 | stochastic_14_3_recovery | 9784.54 | -215.46 | sell / filled / 직전 %K14 < 20에서 %K14가 %D3 상향 돌파 (한 봉 목표); 조건 미충족; K14=25.4855, D3=14.0848, previous_K14=10.0077, previous_D3=7.52857; 직전 완료 봉 목표를 다음 봉 시가에 모의 적용 |
| v2 | mfi_14_recovery | 10007.36 | 7.36 | sell / filled / 직전 MFI14 < 20, 현재 MFI14 >= 20 (한 봉 목표); 조건 미충족; MFI14=25.2915, previous_MFI14=22.266; 직전 완료 봉 목표를 다음 봉 시가에 모의 적용 |
| v2 | adx_14_trend | 9879.67 | -120.33 | sell / filled / Wilder ADX14 >= 25 그리고 +DI14 > -DI14; 조건 미충족; ADX14=23.6824, plus_DI14=22.3066, minus_DI14=19.9214; 직전 완료 봉 목표를 다음 봉 시가에 모의 적용 |
| v2 | aroon_25_trend | 9820.70 | -179.30 | buy / partial / Aroon25 Up > 70 그리고 Down < 30 (동률이면 최신 극값); 조건 충족; Aroon_up=92, Aroon_down=28; 직전 완료 봉 목표를 다음 봉 시가에 모의 적용 |
| v2 | cci_20_momentum | 10010.15 | 10.15 | sell / filled / CCI20 > 100 (전형가격·평균절대편차); 조건 미충족; CCI20=86.441; 직전 완료 봉 목표를 다음 봉 시가에 모의 적용 |
| v2 | williams_14_recovery | 9816.68 | -183.32 | sell / filled / 직전 Williams %R14 < -80, 현재 >= -80 (한 봉 목표); 조건 미충족; Williams_R14=-78.4506, previous_R14=-77.7733; 직전 완료 봉 목표를 다음 봉 시가에 모의 적용 |
| v2 | cmf_20_accumulation | 9745.62 | -254.38 | buy / partial / Chaikin Money Flow20 > 0.1; 조건 충족; CMF20=0.184396, volume20=3.37825e+07; 직전 완료 봉 목표를 다음 봉 시가에 모의 적용 |
| v2 | chaikin_3_10 | 9831.04 | -168.96 | sell / filled / ADL의 EMA3 - EMA10 > 0 그리고 종가 > EMA26; 조건 미충족; Chaikin3_10=-39308.5, ADL=1.1146e+08, close=533.345, EMA26=532.447; 직전 완료 봉 목표를 다음 봉 시가에 모의 적용 |
| v2 | roc_10_momentum | 9957.44 | -42.56 | sell / filled / 10봉 ROC > 1% 그리고 종가 > EMA26; 조건 미충족; ROC10_percent=0.454191, close=534.125, EMA26=532.186; 직전 완료 봉 목표를 다음 봉 시가에 모의 적용 |
| v2 | trix_15_trend | 9855.21 | -144.79 | buy / partial / 15봉 삼중 EMA의 1봉 변화율 TRIX > 0 그리고 종가 > EMA26; 조건 충족; TRIX15_percent=0.00435677, close=534.125, EMA26=532.186; 직전 완료 봉 목표를 다음 봉 시가에 모의 적용 |
| v2 | keltner_20_breakout | 9956.78 | -43.22 | sell / filled / 종가 > EMA20 + 2 x Wilder ATR14; 조건 미충족; close=533.975, upper_Keltner=534.357, EMA20=530.111, ATR14=2.12332; 직전 완료 봉 목표를 다음 봉 시가에 모의 적용 |
| v2 | opening_range_30m | 9854.57 | -145.43 | buy / partial / 뉴욕 09:30·09:45 두 완료 봉 최고가를 10:00 이후 종가가 돌파; 조건 충족; close=534.145, opening_high=532.63; 직전 완료 봉 목표를 다음 봉 시가에 모의 적용 |

### 같은 기간의 비용·노출 비교 (사후 연구)

| 전략 | 비용 전 | 비용 후 | 100% 보유 | 같은 평균 노출 보유 | 평균 노출 |
|---|---:|---:|---:|---:|---:|
| cash | 0.00% | 0.00% | 4.36% | 0.00% | 0.00% |
| buy_hold | 4.80% | 4.36% | 4.36% | 4.36% | 100.00% |
| trend_8_26 | 1.26% | -2.49% | 4.36% | 2.47% | 57.48% |
| momentum_26 | 1.57% | -4.23% | 4.36% | 2.55% | 59.32% |
| breakout_8 | 5.93% | -8.55% | 4.36% | 0.86% | 20.21% |
| reversion_12 | -3.70% | -12.56% | 4.36% | 1.07% | 25.20% |
| volume_26 | 1.69% | -7.29% | 4.36% | 0.38% | 8.92% |
| trend_8_26 AND momentum_26 | 0.30% | -5.42% | 4.36% | 2.26% | 52.76% |
| trend_8_26 + momentum_26 | 1.43% | -3.35% | 4.36% | 2.51% | 58.40% |
| trend_8_26 AND breakout_8 | 0.52% | -9.88% | 4.36% | 0.55% | 13.12% |
| trend_8_26 + breakout_8 | 3.59% | -4.97% | 4.36% | 1.66% | 38.85% |
| trend_8_26 AND reversion_12 | -1.26% | -6.90% | 4.36% | 0.29% | 6.82% |
| trend_8_26 + reversion_12 | -1.23% | -7.47% | 4.36% | 1.76% | 41.34% |
| trend_8_26 AND volume_26 | 3.42% | -0.42% | 4.36% | 0.13% | 3.15% |
| trend_8_26 + volume_26 | 1.49% | -4.32% | 4.36% | 1.41% | 33.21% |
| momentum_26 AND breakout_8 | 2.46% | -8.53% | 4.36% | 0.57% | 13.39% |
| momentum_26 + breakout_8 | 3.74% | -5.82% | 4.36% | 1.70% | 39.77% |
| momentum_26 AND reversion_12 | -1.15% | -7.57% | 4.36% | 0.39% | 9.19% |
| momentum_26 + reversion_12 | -1.08% | -8.30% | 4.36% | 1.80% | 42.26% |
| momentum_26 AND volume_26 | 1.77% | -3.23% | 4.36% | 0.17% | 3.94% |
| momentum_26 + volume_26 | 1.64% | -4.78% | 4.36% | 1.45% | 34.12% |
| breakout_8 AND reversion_12 | 0.00% | 0.00% | 4.36% | 0.00% | 0.00% |
| breakout_8 + reversion_12 | 1.02% | -9.83% | 4.36% | 0.96% | 22.71% |
| breakout_8 AND volume_26 | 2.00% | -0.96% | 4.36% | 0.09% | 2.10% |
| breakout_8 + volume_26 | 3.80% | -6.75% | 4.36% | 0.62% | 14.57% |
| reversion_12 AND volume_26 | -2.90% | -6.11% | 4.36% | 0.14% | 3.41% |
| reversion_12 + volume_26 | -1.03% | -9.78% | 4.36% | 0.72% | 17.07% |
| ema_12_26 | 1.53% | -1.82% | 4.36% | 2.54% | 59.06% |
| macd_12_26_9 | 1.06% | -3.90% | 4.36% | 1.42% | 33.33% |
| rsi_14_recovery | -0.06% | -2.13% | 4.36% | 0.06% | 1.31% |
| bollinger_20_reentry | -0.29% | -3.18% | 4.36% | 0.08% | 1.84% |
| donchian_20 | 1.76% | -4.05% | 4.36% | 0.21% | 4.99% |
| atr_14_breakout | 1.45% | -4.74% | 4.36% | 0.18% | 4.20% |
| session_vwap | 5.44% | -2.65% | 4.36% | 1.78% | 41.73% |
| obv_20 | 4.53% | -3.89% | 4.36% | 2.11% | 49.34% |
| stochastic_14_3_recovery | -0.50% | -10.80% | 4.36% | 0.29% | 6.82% |
| mfi_14_recovery | 1.54% | -1.81% | 4.36% | 0.09% | 2.10% |
| adx_14_trend | 3.84% | 1.26% | 4.36% | 1.99% | 46.46% |
| aroon_25_trend | -0.01% | -4.93% | 4.36% | 0.96% | 22.57% |
| cci_20_momentum | 3.27% | -3.44% | 4.36% | 0.97% | 22.83% |
| williams_14_recovery | -0.78% | -9.91% | 4.36% | 0.25% | 6.04% |
| cmf_20_accumulation | 0.54% | -5.21% | 4.36% | 1.32% | 30.97% |
| chaikin_3_10 | 3.68% | -3.87% | 4.36% | 1.93% | 45.14% |
| roc_10_momentum | -0.01% | -4.12% | 4.36% | 0.67% | 15.75% |
| trix_15_trend | 0.43% | -3.70% | 4.36% | 2.01% | 46.98% |
| keltner_20_breakout | 1.11% | -4.26% | 4.36% | 0.58% | 13.65% |
| opening_range_30m | -1.78% | -6.61% | 4.36% | 0.93% | 22.05% |

동일 구간·초기 자금, 종료 시 청산 비용 포함. 노출 맞춤은 사후 설명용이며 v2 실제 계좌 성과가 아닙니다.
[낙폭 분해·비용 영향·전체 구간](MSFT/comparison.json)

[v1 전체 기록](MSFT/accounts.json) · [v2 전체 기록](MSFT/accounts-v2.json)

## JPM 계좌

| 모델 | 전략 | 평가액 USD | 손익 USD | 최근 매매·이유 |
|---|---|---:|---:|---|
| v1 | cash | 10000.00 | 0.00 | 대기 /  / 새 신호 대기 |
| v1 | buy_hold | 9876.83 | -123.17 | buy /  / buy_hold: prior completed bar target 100%; next bar open simulation |
| v1 | trend_8_26 | 9924.04 | -75.96 | sell /  / trend_8_26: prior completed bar target 0%; next bar open simulation |
| v1 | momentum_26 | 9892.69 | -107.31 | sell /  / momentum_26: prior completed bar target 0%; next bar open simulation |
| v1 | breakout_8 | 9829.39 | -170.61 | sell /  / breakout_8: prior completed bar target 0%; next bar open simulation |
| v1 | reversion_12 | 9786.86 | -213.14 | buy /  / reversion_12: prior completed bar target 100%; next bar open simulation |
| v1 | volume_26 | 10020.63 | 20.63 | sell /  / volume_26: prior completed bar target 0%; next bar open simulation |
| v1 | trend_8_26 AND momentum_26 | 9924.04 | -75.96 | sell /  / trend_8_26 AND momentum_26: prior completed bar target 0%; next bar open simulation |
| v1 | trend_8_26 + momentum_26 | 9908.39 | -91.61 | sell /  / trend_8_26 + momentum_26: prior completed bar target 0%; next bar open simulation |
| v1 | trend_8_26 AND breakout_8 | 9915.55 | -84.45 | sell /  / trend_8_26 AND breakout_8: prior completed bar target 0%; next bar open simulation |
| v1 | trend_8_26 + breakout_8 | 9876.66 | -123.34 | sell /  / trend_8_26 + breakout_8: prior completed bar target 0%; next bar open simulation |
| v1 | trend_8_26 AND reversion_12 | 9899.24 | -100.76 | sell /  / trend_8_26 AND reversion_12: prior completed bar target 0%; next bar open simulation |
| v1 | trend_8_26 + reversion_12 | 9855.12 | -144.88 | buy /  / trend_8_26 + reversion_12: prior completed bar target 50%; next bar open simulation |
| v1 | trend_8_26 AND volume_26 | 10035.68 | 35.68 | sell /  / trend_8_26 AND volume_26: prior completed bar target 0%; next bar open simulation |
| v1 | trend_8_26 + volume_26 | 9972.14 | -27.86 | sell /  / trend_8_26 + volume_26: prior completed bar target 0%; next bar open simulation |
| v1 | momentum_26 AND breakout_8 | 9829.39 | -170.61 | sell /  / momentum_26 AND breakout_8: prior completed bar target 0%; next bar open simulation |
| v1 | momentum_26 + breakout_8 | 9861.04 | -138.96 | sell /  / momentum_26 + breakout_8: prior completed bar target 0%; next bar open simulation |
| v1 | momentum_26 AND reversion_12 | 9881.87 | -118.13 | sell /  / momentum_26 AND reversion_12: prior completed bar target 0%; next bar open simulation |
| v1 | momentum_26 + reversion_12 | 9859.27 | -140.73 | buy /  / momentum_26 + reversion_12: prior completed bar target 50%; next bar open simulation |
| v1 | momentum_26 AND volume_26 | 10035.68 | 35.68 | sell /  / momentum_26 AND volume_26: prior completed bar target 0%; next bar open simulation |
| v1 | momentum_26 + volume_26 | 9956.40 | -43.60 | sell /  / momentum_26 + volume_26: prior completed bar target 0%; next bar open simulation |
| v1 | breakout_8 AND reversion_12 | 10000.00 | 0.00 | 대기 /  / 새 신호 대기 |
| v1 | breakout_8 + reversion_12 | 9827.65 | -172.35 | buy /  / breakout_8 + reversion_12: prior completed bar target 50%; next bar open simulation |
| v1 | breakout_8 AND volume_26 | 10035.68 | 35.68 | sell /  / breakout_8 AND volume_26: prior completed bar target 0%; next bar open simulation |
| v1 | breakout_8 + volume_26 | 9924.55 | -75.45 | sell /  / breakout_8 + volume_26: prior completed bar target 0%; next bar open simulation |
| v1 | reversion_12 AND volume_26 | 9985.00 | -15.00 | sell /  / reversion_12 AND volume_26: prior completed bar target 0%; next bar open simulation |
| v1 | reversion_12 + volume_26 | 9902.97 | -97.03 | buy /  / reversion_12 + volume_26: prior completed bar target 50%; next bar open simulation |
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
| v2 | buy_hold | 10041.87 | 41.87 | buy / partial / 직전 완료 봉 목표 비중 100%; 다음 봉 시가 가정 |
| v2 | trend_8_26 | 9931.17 | -68.83 | sell / filled / 직전 완료 봉 목표 비중 0%; 다음 봉 시가 가정 |
| v2 | momentum_26 | 9401.71 | -598.29 | sell / filled / 직전 완료 봉 목표 비중 0%; 다음 봉 시가 가정 |
| v2 | breakout_8 | 9168.97 | -831.03 | sell / filled / 직전 완료 봉 목표 비중 0%; 다음 봉 시가 가정 |
| v2 | reversion_12 | 9766.30 | -233.70 | buy / partial / 직전 완료 봉 목표 비중 100%; 다음 봉 시가 가정 |
| v2 | volume_26 | 9843.04 | -156.96 | sell / filled / 직전 완료 봉 목표 비중 0%; 다음 봉 시가 가정 |
| v2 | trend_8_26 AND momentum_26 | 9890.41 | -109.59 | sell / filled / 직전 완료 봉 목표 비중 0%; 다음 봉 시가 가정 |
| v2 | trend_8_26 + momentum_26 | 9683.69 | -316.31 | sell / filled / 직전 완료 봉 목표 비중 0%; 다음 봉 시가 가정 |
| v2 | trend_8_26 AND breakout_8 | 9287.76 | -712.24 | sell / filled / 직전 완료 봉 목표 비중 0%; 다음 봉 시가 가정 |
| v2 | trend_8_26 + breakout_8 | 9543.58 | -456.42 | sell / filled / 직전 완료 봉 목표 비중 0%; 다음 봉 시가 가정 |
| v2 | trend_8_26 AND reversion_12 | 9877.09 | -122.91 | sell / filled / 직전 완료 봉 목표 비중 0%; 다음 봉 시가 가정 |
| v2 | trend_8_26 + reversion_12 | 9889.96 | -110.04 | buy / filled / 직전 완료 봉 목표 비중 50%; 다음 봉 시가 가정 |
| v2 | trend_8_26 AND volume_26 | 9833.30 | -166.70 | sell / filled / 직전 완료 봉 목표 비중 0%; 다음 봉 시가 가정 |
| v2 | trend_8_26 + volume_26 | 9887.76 | -112.24 | sell / filled / 직전 완료 봉 목표 비중 0%; 다음 봉 시가 가정 |
| v2 | momentum_26 AND breakout_8 | 9150.64 | -849.36 | sell / filled / 직전 완료 봉 목표 비중 0%; 다음 봉 시가 가정 |
| v2 | momentum_26 + breakout_8 | 9305.78 | -694.22 | sell / filled / 직전 완료 봉 목표 비중 0%; 다음 봉 시가 가정 |
| v2 | momentum_26 AND reversion_12 | 9827.31 | -172.69 | sell / filled / 직전 완료 봉 목표 비중 0%; 다음 봉 시가 가정 |
| v2 | momentum_26 + reversion_12 | 9724.66 | -275.34 | buy / filled / 직전 완료 봉 목표 비중 50%; 다음 봉 시가 가정 |
| v2 | momentum_26 AND volume_26 | 9833.30 | -166.70 | sell / filled / 직전 완료 봉 목표 비중 0%; 다음 봉 시가 가정 |
| v2 | momentum_26 + volume_26 | 9681.83 | -318.17 | sell / filled / 직전 완료 봉 목표 비중 0%; 다음 봉 시가 가정 |
| v2 | breakout_8 AND reversion_12 | 10000.00 | 0.00 | 대기 /  / 새 신호 대기 |
| v2 | breakout_8 + reversion_12 | 9522.86 | -477.14 | buy / filled / 직전 완료 봉 목표 비중 50%; 다음 봉 시가 가정 |
| v2 | breakout_8 AND volume_26 | 9926.66 | -73.34 | sell / filled / 직전 완료 봉 목표 비중 0%; 다음 봉 시가 가정 |
| v2 | breakout_8 + volume_26 | 9520.14 | -479.86 | sell / filled / 직전 완료 봉 목표 비중 0%; 다음 봉 시가 가정 |
| v2 | reversion_12 AND volume_26 | 10034.30 | 34.30 | sell / filled / 직전 완료 봉 목표 비중 0%; 다음 봉 시가 가정 |
| v2 | reversion_12 + volume_26 | 9825.39 | -174.61 | buy / filled / 직전 완료 봉 목표 비중 50%; 다음 봉 시가 가정 |
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
| cash | 0.00% | 0.00% | -0.66% | -0.00% | 0.00% |
| buy_hold | -0.24% | -0.66% | -0.66% | -0.66% | 100.00% |
| trend_8_26 | 1.16% | -2.59% | -0.66% | -0.35% | 51.71% |
| momentum_26 | -2.37% | -8.33% | -0.66% | -0.32% | 48.56% |
| breakout_8 | -3.63% | -18.53% | -0.66% | -0.13% | 19.69% |
| reversion_12 | 5.34% | -9.82% | -0.66% | -0.17% | 25.98% |
| volume_26 | 0.31% | -5.82% | -0.66% | -0.05% | 6.82% |
| trend_8_26 AND momentum_26 | 1.09% | -3.07% | -0.66% | -0.27% | 40.68% |
| trend_8_26 + momentum_26 | -0.61% | -5.30% | -0.66% | -0.33% | 50.13% |
| trend_8_26 AND breakout_8 | -3.21% | -13.22% | -0.66% | -0.08% | 12.07% |
| trend_8_26 + breakout_8 | -1.24% | -10.72% | -0.66% | -0.24% | 35.70% |
| trend_8_26 AND reversion_12 | 2.66% | -3.61% | -0.66% | -0.05% | 7.35% |
| trend_8_26 + reversion_12 | 3.25% | -5.69% | -0.66% | -0.26% | 38.85% |
| trend_8_26 AND volume_26 | -0.42% | -4.11% | -0.66% | -0.03% | 3.94% |
| trend_8_26 + volume_26 | 0.75% | -4.21% | -0.66% | -0.20% | 29.27% |
| momentum_26 AND breakout_8 | -2.51% | -12.96% | -0.66% | -0.08% | 12.07% |
| momentum_26 + breakout_8 | -2.98% | -13.38% | -0.66% | -0.23% | 34.13% |
| momentum_26 AND reversion_12 | 2.79% | -4.29% | -0.66% | -0.05% | 6.82% |
| momentum_26 + reversion_12 | 1.44% | -7.54% | -0.66% | -0.25% | 37.28% |
| momentum_26 AND volume_26 | 0.21% | -2.70% | -0.66% | -0.02% | 2.89% |
| momentum_26 + volume_26 | -1.02% | -6.88% | -0.66% | -0.19% | 27.69% |
| breakout_8 AND reversion_12 | 0.00% | 0.00% | -0.66% | -0.00% | 0.00% |
| breakout_8 + reversion_12 | 0.78% | -12.83% | -0.66% | -0.15% | 22.84% |
| breakout_8 AND volume_26 | -0.51% | -2.17% | -0.66% | -0.01% | 1.05% |
| breakout_8 + volume_26 | -1.67% | -11.48% | -0.66% | -0.09% | 13.26% |
| reversion_12 AND volume_26 | 1.66% | -1.70% | -0.66% | -0.02% | 3.41% |
| reversion_12 + volume_26 | 2.80% | -7.07% | -0.66% | -0.11% | 16.41% |
| ema_12_26 | 0.72% | -2.20% | -0.66% | -0.33% | 50.13% |
| macd_12_26_9 | 0.83% | -3.32% | -0.66% | -0.21% | 30.97% |
| rsi_14_recovery | 0.14% | -2.35% | -0.66% | -0.01% | 1.57% |
| bollinger_20_reentry | 0.66% | -4.69% | -0.66% | -0.02% | 3.41% |
| donchian_20 | -1.79% | -4.63% | -0.66% | -0.02% | 2.89% |
| atr_14_breakout | -1.59% | -8.37% | -0.66% | -0.03% | 4.72% |
| session_vwap | 1.19% | -8.52% | -0.66% | -0.32% | 47.24% |
| obv_20 | -3.51% | -14.21% | -0.66% | -0.20% | 30.18% |
| stochastic_14_3_recovery | -1.63% | -12.54% | -0.66% | -0.05% | 7.35% |
| mfi_14_recovery | 0.06% | -2.02% | -0.66% | -0.01% | 1.31% |
| adx_14_trend | -2.86% | -5.68% | -0.66% | -0.18% | 27.30% |
| aroon_25_trend | -1.12% | -5.19% | -0.66% | -0.15% | 22.57% |
| cci_20_momentum | -2.26% | -9.76% | -0.66% | -0.10% | 14.96% |
| williams_14_recovery | -2.40% | -13.23% | -0.66% | -0.05% | 7.35% |
| cmf_20_accumulation | -1.74% | -9.66% | -0.66% | -0.19% | 28.61% |
| chaikin_3_10 | 1.37% | -7.19% | -0.66% | -0.22% | 33.07% |
| roc_10_momentum | -0.98% | -3.45% | -0.66% | -0.05% | 7.87% |
| trix_15_trend | -1.25% | -8.83% | -0.66% | -0.24% | 35.17% |
| keltner_20_breakout | -1.19% | -3.65% | -0.66% | -0.03% | 3.94% |
| opening_range_30m | 0.15% | -3.16% | -0.66% | -0.11% | 16.80% |

동일 구간·초기 자금, 종료 시 청산 비용 포함. 노출 맞춤은 사후 설명용이며 v2 실제 계좌 성과가 아닙니다.
[낙폭 분해·비용 영향·전체 구간](JPM/comparison.json)

[v1 전체 기록](JPM/accounts.json) · [v2 전체 기록](JPM/accounts-v2.json)

## XOM 계좌

| 모델 | 전략 | 평가액 USD | 손익 USD | 최근 매매·이유 |
|---|---|---:|---:|---|
| v1 | cash | 10000.00 | 0.00 | 대기 /  / 새 신호 대기 |
| v1 | buy_hold | 10092.84 | 92.84 | buy /  / buy_hold: prior completed bar target 100%; next bar open simulation |
| v1 | trend_8_26 | 10074.20 | 74.20 | sell /  / trend_8_26: prior completed bar target 0%; next bar open simulation |
| v1 | momentum_26 | 10120.66 | 120.66 | buy /  / momentum_26: prior completed bar target 100%; next bar open simulation |
| v1 | breakout_8 | 9765.64 | -234.36 | buy /  / breakout_8: prior completed bar target 100%; next bar open simulation |
| v1 | reversion_12 | 9934.36 | -65.64 | sell /  / reversion_12: prior completed bar target 0%; next bar open simulation |
| v1 | volume_26 | 9889.56 | -110.44 | sell /  / volume_26: prior completed bar target 0%; next bar open simulation |
| v1 | trend_8_26 AND momentum_26 | 10074.20 | 74.20 | sell /  / trend_8_26 AND momentum_26: prior completed bar target 0%; next bar open simulation |
| v1 | trend_8_26 + momentum_26 | 10097.37 | 97.37 | sell /  / trend_8_26 + momentum_26: prior completed bar target 50%; next bar open simulation |
| v1 | trend_8_26 AND breakout_8 | 9878.22 | -121.78 | sell /  / trend_8_26 AND breakout_8: prior completed bar target 0%; next bar open simulation |
| v1 | trend_8_26 + breakout_8 | 9938.63 | -61.37 | sell /  / trend_8_26 + breakout_8: prior completed bar target 50%; next bar open simulation |
| v1 | trend_8_26 AND reversion_12 | 9921.77 | -78.23 | sell /  / trend_8_26 AND reversion_12: prior completed bar target 0%; next bar open simulation |
| v1 | trend_8_26 + reversion_12 | 10003.95 | 3.95 | sell /  / trend_8_26 + reversion_12: prior completed bar target 0%; next bar open simulation |
| v1 | trend_8_26 AND volume_26 | 9985.49 | -14.51 | sell /  / trend_8_26 AND volume_26: prior completed bar target 0%; next bar open simulation |
| v1 | trend_8_26 + volume_26 | 9981.34 | -18.66 | sell /  / trend_8_26 + volume_26: prior completed bar target 0%; next bar open simulation |
| v1 | momentum_26 AND breakout_8 | 9814.28 | -185.72 | buy /  / momentum_26 AND breakout_8: prior completed bar target 100%; next bar open simulation |
| v1 | momentum_26 + breakout_8 | 9941.65 | -58.35 | buy /  / momentum_26 + breakout_8: prior completed bar target 100%; next bar open simulation |
| v1 | momentum_26 AND reversion_12 | 9934.36 | -65.64 | sell /  / momentum_26 AND reversion_12: prior completed bar target 0%; next bar open simulation |
| v1 | momentum_26 + reversion_12 | 10026.98 | 26.98 | sell /  / momentum_26 + reversion_12: prior completed bar target 50%; next bar open simulation |
| v1 | momentum_26 AND volume_26 | 9985.49 | -14.51 | sell /  / momentum_26 AND volume_26: prior completed bar target 0%; next bar open simulation |
| v1 | momentum_26 + volume_26 | 10004.30 | 4.30 | sell /  / momentum_26 + volume_26: prior completed bar target 50%; next bar open simulation |
| v1 | breakout_8 AND reversion_12 | 10000.00 | 0.00 | 대기 /  / 새 신호 대기 |
| v1 | breakout_8 + reversion_12 | 9849.46 | -150.54 | sell /  / breakout_8 + reversion_12: prior completed bar target 50%; next bar open simulation |
| v1 | breakout_8 AND volume_26 | 9950.44 | -49.56 | sell /  / breakout_8 AND volume_26: prior completed bar target 0%; next bar open simulation |
| v1 | breakout_8 + volume_26 | 9827.26 | -172.74 | sell /  / breakout_8 + volume_26: prior completed bar target 50%; next bar open simulation |
| v1 | reversion_12 AND volume_26 | 10000.00 | 0.00 | 대기 /  / 새 신호 대기 |
| v1 | reversion_12 + volume_26 | 9911.86 | -88.14 | sell /  / reversion_12 + volume_26: prior completed bar target 0%; next bar open simulation |
| v1 | ema_12_26 | 10151.23 | 151.23 | buy /  / EMA12 > EMA26; 조건 충족; EMA12=175.145, EMA26=175.141 |
| v1 | macd_12_26_9 | 10115.61 | 115.61 | sell /  / MACD > 신호선 그리고 MACD > 0; 조건 미충족; MACD=0.723601, signal9=0.751787 |
| v1 | rsi_14_recovery | 10000.00 | 0.00 | 대기 /  / 새 신호 대기 |
| v1 | bollinger_20_reentry | 9913.52 | -86.48 | sell /  / 직전 종가 < 직전 하단밴드, 현재 하단밴드 <= 종가 <= SMA20 (한 봉 목표); 조건 미충족; close=175.71, lower20=173.907, SMA20=174.743, previous_lower20=173.977 |
| v1 | donchian_20 | 9832.30 | -167.70 | sell /  / 종가 > 현재 봉을 제외한 직전 20봉 최고가; 조건 미충족; close=179.01, prior_high20=179.16 |
| v1 | atr_14_breakout | 9864.96 | -135.04 | sell /  / 종가 > 직전 종가 + 직전 ATR14 그리고 종가 > EMA26; 조건 미충족; close=177.19, threshold=177.748, prior_ATR14=0.663113, EMA26=175.734 |
| v1 | session_vwap | 10015.49 | 15.49 | buy /  / 종가 > 뉴욕 거래일별 누적 전형가격 VWAP; 조건 충족; close=178.12, session_VWAP=178.027, session_volume=4.4806e+06 |
| v1 | obv_20 | 9842.85 | -157.15 | buy /  / OBV > OBV의 SMA20 그리고 종가 > EMA26; 조건 충족; OBV=2.18423e+07, OBV_SMA20=2.18347e+07, close=177.655, EMA26=177.636 |
| v1 | stochastic_14_3_recovery | 9923.93 | -76.07 | sell /  / 직전 %K14 < 20에서 %K14가 %D3 상향 돌파 (한 봉 목표); 조건 미충족; K14=33.4559, D3=21.1148, previous_K14=20.3889, previous_D3=14.0974 |
| v1 | mfi_14_recovery | 10000.00 | 0.00 | 대기 /  / 새 신호 대기 |
| v1 | adx_14_trend | 9999.47 | -0.53 | sell /  / Wilder ADX14 >= 25 그리고 +DI14 > -DI14; 조건 미충족; ADX14=23.8302, plus_DI14=25.6436, minus_DI14=22.6035 |
| v1 | aroon_25_trend | 9929.86 | -70.14 | sell /  / Aroon25 Up > 70 그리고 Down < 30 (동률이면 최신 극값); 조건 미충족; Aroon_up=68, Aroon_down=0 |
| v1 | cci_20_momentum | 9842.10 | -157.90 | sell /  / CCI20 > 100 (전형가격·평균절대편차); 조건 미충족; CCI20=67.3071 |
| v1 | williams_14_recovery | 9838.11 | -161.89 | sell /  / 직전 Williams %R14 < -80, 현재 >= -80 (한 봉 목표); 조건 미충족; Williams_R14=-66.5441, previous_R14=-79.6111 |
| v1 | cmf_20_accumulation | 9953.26 | -46.74 | buy /  / Chaikin Money Flow20 > 0.1; 조건 충족; CMF20=0.158173, volume20=1.12043e+07 |
| v1 | chaikin_3_10 | 9895.95 | -104.05 | buy /  / ADL의 EMA3 - EMA10 > 0 그리고 종가 > EMA26; 조건 충족; Chaikin3_10=45202.2, ADL=2.7734e+07, close=177.655, EMA26=177.636 |
| v1 | roc_10_momentum | 9940.60 | -59.40 | sell /  / 10봉 ROC > 1% 그리고 종가 > EMA26; 조건 미충족; ROC10_percent=0.782107, close=178.47, EMA26=176.891 |
| v1 | trix_15_trend | 9994.19 | -5.81 | buy /  / 15봉 삼중 EMA의 1봉 변화율 TRIX > 0 그리고 종가 > EMA26; 조건 충족; TRIX15_percent=0.0352454, close=177.655, EMA26=177.636 |
| v1 | keltner_20_breakout | 9937.30 | -62.70 | sell /  / 종가 > EMA20 + 2 x Wilder ATR14; 조건 미충족; close=178.845, upper_Keltner=179.079, EMA20=177.884, ATR14=0.597175 |
| v1 | opening_range_30m | 10049.37 | 49.37 | sell /  / 뉴욕 09:30·09:45 두 완료 봉 최고가를 10:00 이후 종가가 돌파; 자료 부족·변동폭 또는 거래량 없음: 대기; close=179.01 |
| v2 | cash | 10000.00 | 0.00 | 대기 /  / 새 신호 대기 |
| v2 | buy_hold | 10414.93 | 414.93 | buy / partial / 직전 완료 봉 목표 비중 100%; 다음 봉 시가 가정 |
| v2 | trend_8_26 | 10169.14 | 169.14 | sell / filled / 직전 완료 봉 목표 비중 0%; 다음 봉 시가 가정 |
| v2 | momentum_26 | 10294.35 | 294.35 | buy / partial / 직전 완료 봉 목표 비중 100%; 다음 봉 시가 가정 |
| v2 | breakout_8 | 9235.19 | -764.81 | buy / partial / 직전 완료 봉 목표 비중 100%; 다음 봉 시가 가정 |
| v2 | reversion_12 | 9748.68 | -251.32 | sell / filled / 직전 완료 봉 목표 비중 0%; 다음 봉 시가 가정 |
| v2 | volume_26 | 9794.70 | -205.30 | sell / filled / 직전 완료 봉 목표 비중 0%; 다음 봉 시가 가정 |
| v2 | trend_8_26 AND momentum_26 | 10176.68 | 176.68 | sell / filled / 직전 완료 봉 목표 비중 0%; 다음 봉 시가 가정 |
| v2 | trend_8_26 + momentum_26 | 10231.55 | 231.55 | sell / filled / 직전 완료 봉 목표 비중 50%; 다음 봉 시가 가정 |
| v2 | trend_8_26 AND breakout_8 | 9329.27 | -670.73 | sell / filled / 직전 완료 봉 목표 비중 0%; 다음 봉 시가 가정 |
| v2 | trend_8_26 + breakout_8 | 9732.12 | -267.88 | sell / filled / 직전 완료 봉 목표 비중 50%; 다음 봉 시가 가정 |
| v2 | trend_8_26 AND reversion_12 | 9760.78 | -239.22 | sell / filled / 직전 완료 봉 목표 비중 0%; 다음 봉 시가 가정 |
| v2 | trend_8_26 + reversion_12 | 9956.69 | -43.31 | sell / filled / 직전 완료 봉 목표 비중 0%; 다음 봉 시가 가정 |
| v2 | trend_8_26 AND volume_26 | 9879.28 | -120.72 | sell / filled / 직전 완료 봉 목표 비중 0%; 다음 봉 시가 가정 |
| v2 | trend_8_26 + volume_26 | 9980.00 | -20.00 | sell / filled / 직전 완료 봉 목표 비중 0%; 다음 봉 시가 가정 |
| v2 | momentum_26 AND breakout_8 | 9283.05 | -716.95 | buy / partial / 직전 완료 봉 목표 비중 100%; 다음 봉 시가 가정 |
| v2 | momentum_26 + breakout_8 | 9751.03 | -248.97 | buy / partial / 직전 완료 봉 목표 비중 100%; 다음 봉 시가 가정 |
| v2 | momentum_26 AND reversion_12 | 9733.85 | -266.15 | sell / filled / 직전 완료 봉 목표 비중 0%; 다음 봉 시가 가정 |
| v2 | momentum_26 + reversion_12 | 10017.83 | 17.83 | sell / filled / 직전 완료 봉 목표 비중 50%; 다음 봉 시가 가정 |
| v2 | momentum_26 AND volume_26 | 9941.52 | -58.48 | sell / filled / 직전 완료 봉 목표 비중 0%; 다음 봉 시가 가정 |
| v2 | momentum_26 + volume_26 | 10062.32 | 62.32 | sell / filled / 직전 완료 봉 목표 비중 50%; 다음 봉 시가 가정 |
| v2 | breakout_8 AND reversion_12 | 10000.00 | 0.00 | 대기 /  / 새 신호 대기 |
| v2 | breakout_8 + reversion_12 | 9488.19 | -511.81 | sell / filled / 직전 완료 봉 목표 비중 50%; 다음 봉 시가 가정 |
| v2 | breakout_8 AND volume_26 | 9918.86 | -81.14 | sell / filled / 직전 완료 봉 목표 비중 0%; 다음 봉 시가 가정 |
| v2 | breakout_8 + volume_26 | 9530.58 | -469.42 | sell / filled / 직전 완료 봉 목표 비중 50%; 다음 봉 시가 가정 |
| v2 | reversion_12 AND volume_26 | 9949.87 | -50.13 | sell / filled / 직전 완료 봉 목표 비중 0%; 다음 봉 시가 가정 |
| v2 | reversion_12 + volume_26 | 9792.16 | -207.84 | sell / filled / 직전 완료 봉 목표 비중 0%; 다음 봉 시가 가정 |
| v2 | ema_12_26 | 10150.21 | 150.21 | buy / partial / EMA12 > EMA26; 조건 충족; EMA12=175.145, EMA26=175.141; 직전 완료 봉 목표를 다음 봉 시가에 모의 적용 |
| v2 | macd_12_26_9 | 10113.59 | 113.59 | sell / filled / MACD > 신호선 그리고 MACD > 0; 조건 미충족; MACD=0.723601, signal9=0.751787; 직전 완료 봉 목표를 다음 봉 시가에 모의 적용 |
| v2 | rsi_14_recovery | 10000.00 | 0.00 | 대기 /  / 새 신호 대기 |
| v2 | bollinger_20_reentry | 9911.54 | -88.46 | sell / filled / 직전 종가 < 직전 하단밴드, 현재 하단밴드 <= 종가 <= SMA20 (한 봉 목표); 조건 미충족; close=175.71, lower20=173.907, SMA20=174.743, previous_lower20=173.977; 직전 완료 봉 목표를 다음 봉 시가에 모의 적용 |
| v2 | donchian_20 | 9824.43 | -175.57 | sell / filled / 종가 > 현재 봉을 제외한 직전 20봉 최고가; 조건 미충족; close=179.01, prior_high20=179.16; 직전 완료 봉 목표를 다음 봉 시가에 모의 적용 |
| v2 | atr_14_breakout | 9859.04 | -140.96 | sell / filled / 종가 > 직전 종가 + 직전 ATR14 그리고 종가 > EMA26; 조건 미충족; close=177.19, threshold=177.748, prior_ATR14=0.663113, EMA26=175.734; 직전 완료 봉 목표를 다음 봉 시가에 모의 적용 |
| v2 | session_vwap | 10010.48 | 10.48 | buy / partial / 종가 > 뉴욕 거래일별 누적 전형가격 VWAP; 조건 충족; close=178.12, session_VWAP=178.027, session_volume=4.4806e+06; 직전 완료 봉 목표를 다음 봉 시가에 모의 적용 |
| v2 | obv_20 | 9835.96 | -164.04 | buy / partial / OBV > OBV의 SMA20 그리고 종가 > EMA26; 조건 충족; OBV=2.18423e+07, OBV_SMA20=2.18347e+07, close=177.655, EMA26=177.636; 직전 완료 봉 목표를 다음 봉 시가에 모의 적용 |
| v2 | stochastic_14_3_recovery | 9919.96 | -80.04 | sell / filled / 직전 %K14 < 20에서 %K14가 %D3 상향 돌파 (한 봉 목표); 조건 미충족; K14=33.4559, D3=21.1148, previous_K14=20.3889, previous_D3=14.0974; 직전 완료 봉 목표를 다음 봉 시가에 모의 적용 |
| v2 | mfi_14_recovery | 10000.00 | 0.00 | 대기 /  / 새 신호 대기 |
| v2 | adx_14_trend | 9993.47 | -6.53 | sell / filled / Wilder ADX14 >= 25 그리고 +DI14 > -DI14; 조건 미충족; ADX14=23.8302, plus_DI14=25.6436, minus_DI14=22.6035; 직전 완료 봉 목표를 다음 봉 시가에 모의 적용 |
| v2 | aroon_25_trend | 9927.87 | -72.13 | sell / filled / Aroon25 Up > 70 그리고 Down < 30 (동률이면 최신 극값); 조건 미충족; Aroon_up=68, Aroon_down=0; 직전 완료 봉 목표를 다음 봉 시가에 모의 적용 |
| v2 | cci_20_momentum | 9832.27 | -167.73 | sell / filled / CCI20 > 100 (전형가격·평균절대편차); 조건 미충족; CCI20=67.3071; 직전 완료 봉 목표를 다음 봉 시가에 모의 적용 |
| v2 | williams_14_recovery | 9832.21 | -167.79 | sell / filled / 직전 Williams %R14 < -80, 현재 >= -80 (한 봉 목표); 조건 미충족; Williams_R14=-66.5441, previous_R14=-79.6111; 직전 완료 봉 목표를 다음 봉 시가에 모의 적용 |
| v2 | cmf_20_accumulation | 9952.27 | -47.73 | buy / partial / Chaikin Money Flow20 > 0.1; 조건 충족; CMF20=0.158173, volume20=1.12043e+07; 직전 완료 봉 목표를 다음 봉 시가에 모의 적용 |
| v2 | chaikin_3_10 | 9891.00 | -109.00 | buy / partial / ADL의 EMA3 - EMA10 > 0 그리고 종가 > EMA26; 조건 충족; Chaikin3_10=45202.2, ADL=2.7734e+07, close=177.655, EMA26=177.636; 직전 완료 봉 목표를 다음 봉 시가에 모의 적용 |
| v2 | roc_10_momentum | 9934.64 | -65.36 | sell / filled / 10봉 ROC > 1% 그리고 종가 > EMA26; 조건 미충족; ROC10_percent=0.782107, close=178.47, EMA26=176.891; 직전 완료 봉 목표를 다음 봉 시가에 모의 적용 |
| v2 | trix_15_trend | 9989.19 | -10.81 | buy / partial / 15봉 삼중 EMA의 1봉 변화율 TRIX > 0 그리고 종가 > EMA26; 조건 충족; TRIX15_percent=0.0352454, close=177.655, EMA26=177.636; 직전 완료 봉 목표를 다음 봉 시가에 모의 적용 |
| v2 | keltner_20_breakout | 9931.34 | -68.66 | sell / filled / 종가 > EMA20 + 2 x Wilder ATR14; 조건 미충족; close=178.845, upper_Keltner=179.079, EMA20=177.884, ATR14=0.597175; 직전 완료 봉 목표를 다음 봉 시가에 모의 적용 |
| v2 | opening_range_30m | 10047.36 | 47.36 | sell / filled / 뉴욕 09:30·09:45 두 완료 봉 최고가를 10:00 이후 종가가 돌파; 자료 부족·변동폭 또는 거래량 없음: 대기; close=179.01; 직전 완료 봉 목표를 다음 봉 시가에 모의 적용 |

### 같은 기간의 비용·노출 비교 (사후 연구)

| 전략 | 비용 전 | 비용 후 | 100% 보유 | 같은 평균 노출 보유 | 평균 노출 |
|---|---:|---:|---:|---:|---:|
| cash | 0.00% | 0.00% | 9.28% | 0.00% | 0.00% |
| buy_hold | 9.74% | 9.28% | 9.28% | 9.28% | 100.00% |
| trend_8_26 | 2.83% | -1.40% | 9.28% | 6.04% | 65.88% |
| momentum_26 | 2.03% | -5.40% | 9.28% | 6.63% | 72.18% |
| breakout_8 | -2.09% | -20.97% | 9.28% | 2.42% | 26.77% |
| reversion_12 | 5.55% | -4.57% | 9.28% | 1.97% | 21.78% |
| volume_26 | 3.26% | -3.86% | 9.28% | 0.42% | 4.72% |
| trend_8_26 AND momentum_26 | 1.35% | -3.22% | 9.28% | 5.55% | 60.63% |
| trend_8_26 + momentum_26 | 2.44% | -3.21% | 9.28% | 6.34% | 69.03% |
| trend_8_26 AND breakout_8 | -0.27% | -15.34% | 9.28% | 1.92% | 21.26% |
| trend_8_26 + breakout_8 | 0.36% | -11.34% | 9.28% | 4.22% | 46.33% |
| trend_8_26 AND reversion_12 | 0.37% | -4.96% | 9.28% | 0.80% | 8.92% |
| trend_8_26 + reversion_12 | 4.21% | -2.79% | 9.28% | 3.99% | 43.84% |
| trend_8_26 AND volume_26 | 2.37% | -1.84% | 9.28% | 0.24% | 2.62% |
| trend_8_26 + volume_26 | 3.06% | -2.43% | 9.28% | 3.20% | 35.30% |
| momentum_26 AND breakout_8 | -2.21% | -19.73% | 9.28% | 2.25% | 24.93% |
| momentum_26 + breakout_8 | -0.03% | -13.52% | 9.28% | 4.51% | 49.48% |
| momentum_26 AND reversion_12 | 0.87% | -5.29% | 9.28% | 0.90% | 9.97% |
| momentum_26 + reversion_12 | 3.80% | -3.58% | 9.28% | 4.28% | 46.99% |
| momentum_26 AND volume_26 | 2.15% | -1.64% | 9.28% | 0.21% | 2.36% |
| momentum_26 + volume_26 | 2.66% | -3.42% | 9.28% | 3.49% | 38.46% |
| breakout_8 AND reversion_12 | 0.00% | 0.00% | 9.28% | 0.00% | 0.00% |
| breakout_8 + reversion_12 | 1.68% | -12.98% | 9.28% | 2.20% | 24.29% |
| breakout_8 AND volume_26 | 0.51% | -1.17% | 9.28% | 0.09% | 1.05% |
| breakout_8 + volume_26 | 0.56% | -11.91% | 9.28% | 1.42% | 15.76% |
| reversion_12 AND volume_26 | 1.10% | -1.00% | 9.28% | 0.12% | 1.31% |
| reversion_12 + volume_26 | 4.41% | -3.41% | 9.28% | 1.19% | 13.26% |
| ema_12_26 | 1.48% | -1.88% | 9.28% | 7.01% | 76.12% |
| macd_12_26_9 | 0.40% | -4.93% | 9.28% | 3.80% | 41.73% |
| rsi_14_recovery | -0.15% | -0.57% | 9.28% | 0.02% | 0.26% |
| bollinger_20_reentry | -0.87% | -3.75% | 9.28% | 0.16% | 1.84% |
| donchian_20 | -0.93% | -10.43% | 9.28% | 0.87% | 9.71% |
| atr_14_breakout | -1.03% | -9.76% | 9.28% | 0.54% | 6.04% |
| session_vwap | 0.92% | -10.28% | 9.28% | 6.29% | 68.50% |
| obv_20 | 1.98% | -6.24% | 9.28% | 4.26% | 46.72% |
| stochastic_14_3_recovery | 1.68% | -6.90% | 9.28% | 0.49% | 5.51% |
| mfi_14_recovery | -0.31% | -1.97% | 9.28% | 0.09% | 1.05% |
| adx_14_trend | 3.88% | 0.87% | 9.28% | 4.04% | 44.36% |
| aroon_25_trend | -2.08% | -8.44% | 9.28% | 3.22% | 35.43% |
| cci_20_momentum | 3.75% | -4.61% | 9.28% | 2.59% | 28.61% |
| williams_14_recovery | 0.21% | -5.51% | 9.28% | 0.33% | 3.67% |
| cmf_20_accumulation | 0.97% | -5.59% | 9.28% | 4.82% | 52.76% |
| chaikin_3_10 | -0.81% | -9.95% | 9.28% | 5.38% | 58.79% |
| roc_10_momentum | 0.80% | -5.36% | 9.28% | 1.18% | 13.12% |
| trix_15_trend | -0.11% | -6.60% | 9.28% | 5.94% | 64.83% |
| keltner_20_breakout | 0.18% | -6.72% | 9.28% | 1.56% | 17.32% |
| opening_range_30m | 0.54% | -9.10% | 9.28% | 3.55% | 39.11% |

동일 구간·초기 자금, 종료 시 청산 비용 포함. 노출 맞춤은 사후 설명용이며 v2 실제 계좌 성과가 아닙니다.
[낙폭 분해·비용 영향·전체 구간](XOM/comparison.json)

[v1 전체 기록](XOM/accounts.json) · [v2 전체 기록](XOM/accounts-v2.json)

## JNJ 계좌

| 모델 | 전략 | 평가액 USD | 손익 USD | 최근 매매·이유 |
|---|---|---:|---:|---|
| v1 | cash | 10000.00 | 0.00 | 대기 /  / 새 신호 대기 |
| v1 | buy_hold | 9908.16 | -91.84 | buy /  / buy_hold: prior completed bar target 100%; next bar open simulation |
| v1 | trend_8_26 | 9903.43 | -96.57 | sell /  / trend_8_26: prior completed bar target 0%; next bar open simulation |
| v1 | momentum_26 | 9898.09 | -101.91 | sell /  / momentum_26: prior completed bar target 0%; next bar open simulation |
| v1 | breakout_8 | 9680.70 | -319.30 | buy /  / breakout_8: prior completed bar target 100%; next bar open simulation |
| v1 | reversion_12 | 9891.56 | -108.44 | sell /  / reversion_12: prior completed bar target 0%; next bar open simulation |
| v1 | volume_26 | 9884.71 | -115.29 | sell /  / volume_26: prior completed bar target 0%; next bar open simulation |
| v1 | trend_8_26 AND momentum_26 | 9950.33 | -49.67 | sell /  / trend_8_26 AND momentum_26: prior completed bar target 0%; next bar open simulation |
| v1 | trend_8_26 + momentum_26 | 9900.74 | -99.26 | sell /  / trend_8_26 + momentum_26: prior completed bar target 0%; next bar open simulation |
| v1 | trend_8_26 AND breakout_8 | 9937.40 | -62.60 | sell /  / trend_8_26 AND breakout_8: prior completed bar target 0%; next bar open simulation |
| v1 | trend_8_26 + breakout_8 | 9791.37 | -208.63 | sell /  / trend_8_26 + breakout_8: prior completed bar target 50%; next bar open simulation |
| v1 | trend_8_26 AND reversion_12 | 9992.01 | -7.99 | sell /  / trend_8_26 AND reversion_12: prior completed bar target 0%; next bar open simulation |
| v1 | trend_8_26 + reversion_12 | 9897.42 | -102.58 | sell /  / trend_8_26 + reversion_12: prior completed bar target 0%; next bar open simulation |
| v1 | trend_8_26 AND volume_26 | 9935.63 | -64.37 | sell /  / trend_8_26 AND volume_26: prior completed bar target 0%; next bar open simulation |
| v1 | trend_8_26 + volume_26 | 9894.03 | -105.97 | sell /  / trend_8_26 + volume_26: prior completed bar target 0%; next bar open simulation |
| v1 | momentum_26 AND breakout_8 | 9911.77 | -88.23 | sell /  / momentum_26 AND breakout_8: prior completed bar target 0%; next bar open simulation |
| v1 | momentum_26 + breakout_8 | 9788.70 | -211.30 | sell /  / momentum_26 + breakout_8: prior completed bar target 50%; next bar open simulation |
| v1 | momentum_26 AND reversion_12 | 10000.00 | 0.00 | 대기 /  / 새 신호 대기 |
| v1 | momentum_26 + reversion_12 | 9914.55 | -85.45 | sell /  / momentum_26 + reversion_12: prior completed bar target 0%; next bar open simulation |
| v1 | momentum_26 AND volume_26 | 10000.00 | 0.00 | 대기 /  / 새 신호 대기 |
| v1 | momentum_26 + volume_26 | 9911.13 | -88.87 | sell /  / momentum_26 + volume_26: prior completed bar target 0%; next bar open simulation |
| v1 | breakout_8 AND reversion_12 | 10000.00 | 0.00 | 대기 /  / 새 신호 대기 |
| v1 | breakout_8 + reversion_12 | 9785.43 | -214.57 | sell /  / breakout_8 + reversion_12: prior completed bar target 50%; next bar open simulation |
| v1 | breakout_8 AND volume_26 | 10000.00 | 0.00 | 대기 /  / 새 신호 대기 |
| v1 | breakout_8 + volume_26 | 9782.05 | -217.95 | sell /  / breakout_8 + volume_26: prior completed bar target 50%; next bar open simulation |
| v1 | reversion_12 AND volume_26 | 9974.59 | -25.41 | sell /  / reversion_12 AND volume_26: prior completed bar target 0%; next bar open simulation |
| v1 | reversion_12 + volume_26 | 9907.87 | -92.13 | sell /  / reversion_12 + volume_26: prior completed bar target 0%; next bar open simulation |
| v1 | ema_12_26 | 9781.22 | -218.78 | sell /  / EMA12 > EMA26; 조건 미충족; EMA12=255.193, EMA26=255.284 |
| v1 | macd_12_26_9 | 9756.47 | -243.53 | sell /  / MACD > 신호선 그리고 MACD > 0; 조건 미충족; MACD=-0.0912606, signal9=-0.0161084 |
| v1 | rsi_14_recovery | 9923.04 | -76.96 | sell /  / 직전 RSI14 < 30, 현재 RSI14 >= 30 (한 봉 목표); 조건 미충족; RSI14=40.3665, previous_RSI14=36.2025 |
| v1 | bollinger_20_reentry | 9881.04 | -118.96 | sell /  / 직전 종가 < 직전 하단밴드, 현재 하단밴드 <= 종가 <= SMA20 (한 봉 목표); 조건 미충족; close=251.75, lower20=251.316, SMA20=254.208, previous_lower20=251.691 |
| v1 | donchian_20 | 10000.00 | 0.00 | 대기 /  / 새 신호 대기 |
| v1 | atr_14_breakout | 9883.97 | -116.03 | sell /  / 종가 > 직전 종가 + 직전 ATR14 그리고 종가 > EMA26; 조건 미충족; close=256.72, threshold=258.136, prior_ATR14=1.3158, EMA26=255.146 |
| v1 | session_vwap | 9744.33 | -255.67 | buy /  / 종가 > 뉴욕 거래일별 누적 전형가격 VWAP; 조건 충족; close=252.75, session_VWAP=252.657, session_volume=4.65844e+06 |
| v1 | obv_20 | 9695.40 | -304.60 | buy /  / OBV > OBV의 SMA20 그리고 종가 > EMA26; 조건 충족; OBV=4.77296e+06, OBV_SMA20=3.20496e+06, close=253.81, EMA26=253.704 |
| v1 | stochastic_14_3_recovery | 9862.87 | -137.13 | sell /  / 직전 %K14 < 20에서 %K14가 %D3 상향 돌파 (한 봉 목표); 조건 미충족; K14=28.9392, D3=18.1738, previous_K14=19.7943, previous_D3=12.6561 |
| v1 | mfi_14_recovery | 10000.00 | 0.00 | 대기 /  / 새 신호 대기 |
| v1 | adx_14_trend | 9823.79 | -176.21 | sell /  / Wilder ADX14 >= 25 그리고 +DI14 > -DI14; 조건 미충족; ADX14=24.7842, plus_DI14=27.3963, minus_DI14=19.1477 |
| v1 | aroon_25_trend | 9967.50 | -32.50 | sell /  / Aroon25 Up > 70 그리고 Down < 30 (동률이면 최신 극값); 조건 미충족; Aroon_up=68, Aroon_down=16 |
| v1 | cci_20_momentum | 9935.63 | -64.37 | sell /  / CCI20 > 100 (전형가격·평균절대편차); 조건 미충족; CCI20=62.9489 |
| v1 | williams_14_recovery | 9903.67 | -96.33 | sell /  / 직전 Williams %R14 < -80, 현재 >= -80 (한 봉 목표); 조건 미충족; Williams_R14=-61.3372, previous_R14=-71.0608 |
| v1 | cmf_20_accumulation | 10032.43 | 32.43 | buy /  / Chaikin Money Flow20 > 0.1; 조건 충족; CMF20=0.280188, volume20=5.69706e+06 |
| v1 | chaikin_3_10 | 9914.79 | -85.21 | buy /  / ADL의 EMA3 - EMA10 > 0 그리고 종가 > EMA26; 조건 충족; Chaikin3_10=616829, ADL=4.33018e+06, close=253.81, EMA26=253.704 |
| v1 | roc_10_momentum | 9816.66 | -183.34 | sell /  / 10봉 ROC > 1% 그리고 종가 > EMA26; 조건 미충족; ROC10_percent=-0.398319, close=255.08, EMA26=255.591 |
| v1 | trix_15_trend | 9840.00 | -160.00 | sell /  / 15봉 삼중 EMA의 1봉 변화율 TRIX > 0 그리고 종가 > EMA26; 조건 미충족; TRIX15_percent=0.000692295, close=255.155, EMA26=255.356 |
| v1 | keltner_20_breakout | 10000.00 | 0.00 | 대기 /  / 새 신호 대기 |
| v1 | opening_range_30m | 10000.00 | 0.00 | 대기 /  / 새 신호 대기 |
| v2 | cash | 10000.00 | 0.00 | 대기 /  / 새 신호 대기 |
| v2 | buy_hold | 9676.92 | -323.08 | 중단: 손실 한도 / buy / partial / 직전 완료 봉 목표 비중 100%; 다음 봉 시가 가정 |
| v2 | trend_8_26 | 9676.92 | -323.08 | 중단: 손실 한도 / buy / partial / 직전 완료 봉 목표 비중 100%; 다음 봉 시가 가정 |
| v2 | momentum_26 | 9676.92 | -323.08 | 중단: 손실 한도 / buy / partial / 직전 완료 봉 목표 비중 100%; 다음 봉 시가 가정 |
| v2 | breakout_8 | 9343.39 | -656.61 | 중단: 손실 한도 / sell / filled / 직전 완료 봉 목표 비중 0%; 다음 봉 시가 가정 |
| v2 | reversion_12 | 9581.23 | -418.77 | sell / filled / 직전 완료 봉 목표 비중 0%; 다음 봉 시가 가정 |
| v2 | volume_26 | 9672.67 | -327.33 | sell / filled / 직전 완료 봉 목표 비중 0%; 다음 봉 시가 가정 |
| v2 | trend_8_26 AND momentum_26 | 9676.92 | -323.08 | 중단: 손실 한도 / buy / partial / 직전 완료 봉 목표 비중 100%; 다음 봉 시가 가정 |
| v2 | trend_8_26 + momentum_26 | 9676.92 | -323.08 | 중단: 손실 한도 / buy / partial / 직전 완료 봉 목표 비중 100%; 다음 봉 시가 가정 |
| v2 | trend_8_26 AND breakout_8 | 9419.39 | -580.61 | 중단: 손실 한도 / sell / filled / 직전 완료 봉 목표 비중 0%; 다음 봉 시가 가정 |
| v2 | trend_8_26 + breakout_8 | 9364.06 | -635.94 | sell / filled / 직전 완료 봉 목표 비중 50%; 다음 봉 시가 가정 |
| v2 | trend_8_26 AND reversion_12 | 9968.12 | -31.88 | sell / filled / 직전 완료 봉 목표 비중 0%; 다음 봉 시가 가정 |
| v2 | trend_8_26 + reversion_12 | 9732.92 | -267.08 | 중단: 손실 한도 / sell / filled / 직전 완료 봉 목표 비중 0%; 다음 봉 시가 가정 |
| v2 | trend_8_26 AND volume_26 | 9805.21 | -194.79 | sell / filled / 직전 완료 봉 목표 비중 0%; 다음 봉 시가 가정 |
| v2 | trend_8_26 + volume_26 | 9810.98 | -189.02 | 중단: 손실 한도 / buy / filled / 직전 완료 봉 목표 비중 50%; 다음 봉 시가 가정 |
| v2 | momentum_26 AND breakout_8 | 9512.11 | -487.89 | sell / filled / 직전 완료 봉 목표 비중 0%; 다음 봉 시가 가정 |
| v2 | momentum_26 + breakout_8 | 9352.71 | -647.29 | sell / filled / 직전 완료 봉 목표 비중 50%; 다음 봉 시가 가정 |
| v2 | momentum_26 AND reversion_12 | 9938.87 | -61.13 | sell / filled / 직전 완료 봉 목표 비중 0%; 다음 봉 시가 가정 |
| v2 | momentum_26 + reversion_12 | 9732.92 | -267.08 | 중단: 손실 한도 / sell / filled / 직전 완료 봉 목표 비중 0%; 다음 봉 시가 가정 |
| v2 | momentum_26 AND volume_26 | 9920.93 | -79.07 | sell / filled / 직전 완료 봉 목표 비중 0%; 다음 봉 시가 가정 |
| v2 | momentum_26 + volume_26 | 9810.98 | -189.02 | 중단: 손실 한도 / buy / filled / 직전 완료 봉 목표 비중 50%; 다음 봉 시가 가정 |
| v2 | breakout_8 AND reversion_12 | 10000.00 | 0.00 | 대기 /  / 새 신호 대기 |
| v2 | breakout_8 + reversion_12 | 9368.45 | -631.55 | sell / filled / 직전 완료 봉 목표 비중 50%; 다음 봉 시가 가정 |
| v2 | breakout_8 AND volume_26 | 9814.17 | -185.83 | sell / filled / 직전 완료 봉 목표 비중 0%; 다음 봉 시가 가정 |
| v2 | breakout_8 + volume_26 | 9393.23 | -606.77 | sell / filled / 직전 완료 봉 목표 비중 50%; 다음 봉 시가 가정 |
| v2 | reversion_12 AND volume_26 | 9859.15 | -140.85 | sell / filled / 직전 완료 봉 목표 비중 0%; 다음 봉 시가 가정 |
| v2 | reversion_12 + volume_26 | 9667.54 | -332.46 | sell / filled / 직전 완료 봉 목표 비중 0%; 다음 봉 시가 가정 |
| v2 | ema_12_26 | 9777.31 | -222.69 | sell / filled / EMA12 > EMA26; 조건 미충족; EMA12=255.193, EMA26=255.284; 직전 완료 봉 목표를 다음 봉 시가에 모의 적용 |
| v2 | macd_12_26_9 | 9752.57 | -247.43 | sell / filled / MACD > 신호선 그리고 MACD > 0; 조건 미충족; MACD=-0.0912606, signal9=-0.0161084; 직전 완료 봉 목표를 다음 봉 시가에 모의 적용 |
| v2 | rsi_14_recovery | 9919.07 | -80.93 | sell / filled / 직전 RSI14 < 30, 현재 RSI14 >= 30 (한 봉 목표); 조건 미충족; RSI14=40.3665, previous_RSI14=36.2025; 직전 완료 봉 목표를 다음 봉 시가에 모의 적용 |
| v2 | bollinger_20_reentry | 9877.09 | -122.91 | sell / filled / 직전 종가 < 직전 하단밴드, 현재 하단밴드 <= 종가 <= SMA20 (한 봉 목표); 조건 미충족; close=251.75, lower20=251.316, SMA20=254.208, previous_lower20=251.691; 직전 완료 봉 목표를 다음 봉 시가에 모의 적용 |
| v2 | donchian_20 | 10000.00 | 0.00 | 대기 /  / 새 신호 대기 |
| v2 | atr_14_breakout | 9880.02 | -119.98 | sell / filled / 종가 > 직전 종가 + 직전 ATR14 그리고 종가 > EMA26; 조건 미충족; close=256.72, threshold=258.136, prior_ATR14=1.3158, EMA26=255.146; 직전 완료 봉 목표를 다음 봉 시가에 모의 적용 |
| v2 | session_vwap | 9735.57 | -264.43 | buy / partial / 종가 > 뉴욕 거래일별 누적 전형가격 VWAP; 조건 충족; close=252.75, session_VWAP=252.657, session_volume=4.65844e+06; 직전 완료 봉 목표를 다음 봉 시가에 모의 적용 |
| v2 | obv_20 | 9686.67 | -313.33 | buy / partial / OBV > OBV의 SMA20 그리고 종가 > EMA26; 조건 충족; OBV=4.77296e+06, OBV_SMA20=3.20496e+06, close=253.81, EMA26=253.704; 직전 완료 봉 목표를 다음 봉 시가에 모의 적용 |
| v2 | stochastic_14_3_recovery | 9856.96 | -143.04 | sell / filled / 직전 %K14 < 20에서 %K14가 %D3 상향 돌파 (한 봉 목표); 조건 미충족; K14=28.9392, D3=18.1738, previous_K14=19.7943, previous_D3=12.6561; 직전 완료 봉 목표를 다음 봉 시가에 모의 적용 |
| v2 | mfi_14_recovery | 10000.00 | 0.00 | 대기 /  / 새 신호 대기 |
| v2 | adx_14_trend | 9817.90 | -182.10 | sell / filled / Wilder ADX14 >= 25 그리고 +DI14 > -DI14; 조건 미충족; ADX14=24.7842, plus_DI14=27.3963, minus_DI14=19.1477; 직전 완료 봉 목표를 다음 봉 시가에 모의 적용 |
| v2 | aroon_25_trend | 9965.51 | -34.49 | sell / filled / Aroon25 Up > 70 그리고 Down < 30 (동률이면 최신 극값); 조건 미충족; Aroon_up=68, Aroon_down=16; 직전 완료 봉 목표를 다음 봉 시가에 모의 적용 |
| v2 | cci_20_momentum | 9933.64 | -66.36 | sell / filled / CCI20 > 100 (전형가격·평균절대편차); 조건 미충족; CCI20=62.9489; 직전 완료 봉 목표를 다음 봉 시가에 모의 적용 |
| v2 | williams_14_recovery | 9899.71 | -100.29 | sell / filled / 직전 Williams %R14 < -80, 현재 >= -80 (한 봉 목표); 조건 미충족; Williams_R14=-61.3372, previous_R14=-71.0608; 직전 완료 봉 목표를 다음 봉 시가에 모의 적용 |
| v2 | cmf_20_accumulation | 10031.43 | 31.43 | buy / partial / Chaikin Money Flow20 > 0.1; 조건 충족; CMF20=0.280188, volume20=5.69706e+06; 직전 완료 봉 목표를 다음 봉 시가에 모의 적용 |
| v2 | chaikin_3_10 | 9911.82 | -88.18 | buy / partial / ADL의 EMA3 - EMA10 > 0 그리고 종가 > EMA26; 조건 충족; Chaikin3_10=616829, ADL=4.33018e+06, close=253.81, EMA26=253.704; 직전 완료 봉 목표를 다음 봉 시가에 모의 적용 |
| v2 | roc_10_momentum | 9812.74 | -187.26 | sell / filled / 10봉 ROC > 1% 그리고 종가 > EMA26; 조건 미충족; ROC10_percent=-0.398319, close=255.08, EMA26=255.591; 직전 완료 봉 목표를 다음 봉 시가에 모의 적용 |
| v2 | trix_15_trend | 9836.06 | -163.94 | sell / filled / 15봉 삼중 EMA의 1봉 변화율 TRIX > 0 그리고 종가 > EMA26; 조건 미충족; TRIX15_percent=0.000692295, close=255.155, EMA26=255.356; 직전 완료 봉 목표를 다음 봉 시가에 모의 적용 |
| v2 | keltner_20_breakout | 10000.00 | 0.00 | 대기 /  / 새 신호 대기 |
| v2 | opening_range_30m | 10000.00 | 0.00 | 대기 /  / 새 신호 대기 |

### 같은 기간의 비용·노출 비교 (사후 연구)

| 전략 | 비용 전 | 비용 후 | 100% 보유 | 같은 평균 노출 보유 | 평균 노출 |
|---|---:|---:|---:|---:|---:|
| cash | 0.00% | 0.00% | -7.16% | -0.00% | 0.00% |
| buy_hold | -6.77% | -7.16% | -7.16% | -7.16% | 100.00% |
| trend_8_26 | 1.32% | -0.79% | -7.16% | -3.24% | 43.83% |
| momentum_26 | -0.38% | -4.08% | -7.16% | -3.22% | 43.57% |
| breakout_8 | -1.34% | -17.99% | -7.16% | -1.46% | 19.42% |
| reversion_12 | -8.25% | -16.00% | -7.16% | -2.34% | 31.50% |
| volume_26 | -1.41% | -8.20% | -7.16% | -0.50% | 6.56% |
| trend_8_26 AND momentum_26 | 1.48% | -1.46% | -7.16% | -2.80% | 37.80% |
| trend_8_26 + momentum_26 | 0.47% | -2.44% | -7.16% | -3.23% | 43.70% |
| trend_8_26 AND breakout_8 | 0.57% | -10.59% | -7.16% | -0.99% | 13.12% |
| trend_8_26 + breakout_8 | 0.00% | -9.78% | -7.16% | -2.35% | 31.63% |
| trend_8_26 AND reversion_12 | 0.87% | -2.05% | -7.16% | -0.40% | 5.25% |
| trend_8_26 + reversion_12 | -3.55% | -8.32% | -7.16% | -2.79% | 37.67% |
| trend_8_26 AND volume_26 | 0.41% | -1.67% | -7.16% | -0.10% | 1.31% |
| trend_8_26 + volume_26 | -0.02% | -4.35% | -7.16% | -1.88% | 25.20% |
| momentum_26 AND breakout_8 | 1.38% | -9.11% | -7.16% | -0.95% | 12.60% |
| momentum_26 + breakout_8 | -0.84% | -11.10% | -7.16% | -2.34% | 31.50% |
| momentum_26 AND reversion_12 | -0.82% | -2.88% | -7.16% | -0.42% | 5.51% |
| momentum_26 + reversion_12 | -4.37% | -9.47% | -7.16% | -2.78% | 37.54% |
| momentum_26 AND volume_26 | 0.65% | -0.61% | -7.16% | -0.06% | 0.79% |
| momentum_26 + volume_26 | -0.86% | -5.36% | -7.16% | -1.87% | 25.07% |
| breakout_8 AND reversion_12 | 0.00% | 0.00% | -7.16% | -0.00% | 0.00% |
| breakout_8 + reversion_12 | -4.84% | -16.48% | -7.16% | -1.90% | 25.47% |
| breakout_8 AND volume_26 | -0.91% | -2.15% | -7.16% | -0.06% | 0.79% |
| breakout_8 + volume_26 | -1.36% | -12.50% | -7.16% | -0.98% | 13.00% |
| reversion_12 AND volume_26 | -1.84% | -4.69% | -7.16% | -0.22% | 2.89% |
| reversion_12 + volume_26 | -4.87% | -11.26% | -7.16% | -1.43% | 19.03% |
| ema_12_26 | -1.92% | -4.37% | -7.16% | -2.86% | 38.58% |
| macd_12_26_9 | 4.01% | 1.42% | -7.16% | -1.86% | 24.93% |
| rsi_14_recovery | -1.66% | -7.67% | -7.16% | -0.30% | 3.94% |
| bollinger_20_reentry | -0.95% | -5.82% | -7.16% | -0.24% | 3.15% |
| donchian_20 | 0.63% | -6.31% | -7.16% | -0.50% | 6.56% |
| atr_14_breakout | 1.19% | -4.59% | -7.16% | -0.34% | 4.46% |
| session_vwap | 1.11% | -6.64% | -7.16% | -3.30% | 44.62% |
| obv_20 | -7.01% | -15.57% | -7.16% | -2.15% | 28.87% |
| stochastic_14_3_recovery | -1.34% | -14.11% | -7.16% | -0.65% | 8.66% |
| mfi_14_recovery | 0.33% | -0.93% | -7.16% | -0.06% | 0.79% |
| adx_14_trend | -2.56% | -7.35% | -7.16% | -2.32% | 31.23% |
| aroon_25_trend | 4.10% | 0.24% | -7.16% | -2.04% | 27.30% |
| cci_20_momentum | 0.59% | -5.56% | -7.16% | -1.49% | 19.95% |
| williams_14_recovery | -1.77% | -10.06% | -7.16% | -0.42% | 5.51% |
| cmf_20_accumulation | 3.09% | -0.73% | -7.16% | -1.86% | 24.93% |
| chaikin_3_10 | -3.37% | -7.73% | -7.16% | -2.23% | 29.92% |
| roc_10_momentum | -2.32% | -8.29% | -7.16% | -1.10% | 14.70% |
| trix_15_trend | -1.33% | -3.78% | -7.16% | -2.17% | 29.13% |
| keltner_20_breakout | 0.65% | -2.68% | -7.16% | -0.69% | 9.19% |
| opening_range_30m | 0.79% | -2.95% | -7.16% | -1.94% | 25.98% |

동일 구간·초기 자금, 종료 시 청산 비용 포함. 노출 맞춤은 사후 설명용이며 v2 실제 계좌 성과가 아닙니다.
[낙폭 분해·비용 영향·전체 구간](JNJ/comparison.json)

[v1 전체 기록](JNJ/accounts.json) · [v2 전체 기록](JNJ/accounts-v2.json)

## CAT 계좌

| 모델 | 전략 | 평가액 USD | 손익 USD | 최근 매매·이유 |
|---|---|---:|---:|---|
| v1 | cash | 10000.00 | 0.00 | 대기 /  / 새 신호 대기 |
| v1 | buy_hold | 9865.33 | -134.67 | buy /  / buy_hold: prior completed bar target 100%; next bar open simulation |
| v1 | trend_8_26 | 9928.77 | -71.23 | buy /  / trend_8_26: prior completed bar target 100%; next bar open simulation |
| v1 | momentum_26 | 9872.70 | -127.30 | sell /  / momentum_26: prior completed bar target 0%; next bar open simulation |
| v1 | breakout_8 | 9790.00 | -210.00 | sell /  / breakout_8: prior completed bar target 0%; next bar open simulation |
| v1 | reversion_12 | 9820.78 | -179.22 | sell /  / reversion_12: prior completed bar target 0%; next bar open simulation |
| v1 | volume_26 | 10000.00 | 0.00 | 대기 /  / 새 신호 대기 |
| v1 | trend_8_26 AND momentum_26 | 9873.91 | -126.09 | sell /  / trend_8_26 AND momentum_26: prior completed bar target 0%; next bar open simulation |
| v1 | trend_8_26 + momentum_26 | 9900.83 | -99.17 | buy /  / trend_8_26 + momentum_26: prior completed bar target 50%; next bar open simulation |
| v1 | trend_8_26 AND breakout_8 | 9850.32 | -149.68 | sell /  / trend_8_26 AND breakout_8: prior completed bar target 0%; next bar open simulation |
| v1 | trend_8_26 + breakout_8 | 9859.32 | -140.68 | buy /  / trend_8_26 + breakout_8: prior completed bar target 50%; next bar open simulation |
| v1 | trend_8_26 AND reversion_12 | 9928.06 | -71.94 | sell /  / trend_8_26 AND reversion_12: prior completed bar target 0%; next bar open simulation |
| v1 | trend_8_26 + reversion_12 | 9895.06 | -104.94 | buy /  / trend_8_26 + reversion_12: prior completed bar target 50%; next bar open simulation |
| v1 | trend_8_26 AND volume_26 | 10000.00 | 0.00 | 대기 /  / 새 신호 대기 |
| v1 | trend_8_26 + volume_26 | 9964.38 | -35.62 | buy /  / trend_8_26 + volume_26: prior completed bar target 50%; next bar open simulation |
| v1 | momentum_26 AND breakout_8 | 9850.32 | -149.68 | sell /  / momentum_26 AND breakout_8: prior completed bar target 0%; next bar open simulation |
| v1 | momentum_26 + breakout_8 | 9831.28 | -168.72 | sell /  / momentum_26 + breakout_8: prior completed bar target 0%; next bar open simulation |
| v1 | momentum_26 AND reversion_12 | 9887.21 | -112.79 | sell /  / momentum_26 AND reversion_12: prior completed bar target 0%; next bar open simulation |
| v1 | momentum_26 + reversion_12 | 9847.31 | -152.69 | sell /  / momentum_26 + reversion_12: prior completed bar target 0%; next bar open simulation |
| v1 | momentum_26 AND volume_26 | 10000.00 | 0.00 | 대기 /  / 새 신호 대기 |
| v1 | momentum_26 + volume_26 | 9936.12 | -63.88 | sell /  / momentum_26 + volume_26: prior completed bar target 0%; next bar open simulation |
| v1 | breakout_8 AND reversion_12 | 10000.00 | 0.00 | 대기 /  / 새 신호 대기 |
| v1 | breakout_8 + reversion_12 | 9805.88 | -194.12 | sell /  / breakout_8 + reversion_12: prior completed bar target 0%; next bar open simulation |
| v1 | breakout_8 AND volume_26 | 10000.00 | 0.00 | 대기 /  / 새 신호 대기 |
| v1 | breakout_8 + volume_26 | 9894.44 | -105.56 | sell /  / breakout_8 + volume_26: prior completed bar target 0%; next bar open simulation |
| v1 | reversion_12 AND volume_26 | 10000.00 | 0.00 | 대기 /  / 새 신호 대기 |
| v1 | reversion_12 + volume_26 | 9910.50 | -89.50 | sell /  / reversion_12 + volume_26: prior completed bar target 0%; next bar open simulation |
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
| v2 | buy_hold | 9072.89 | -927.11 | 중단: 손실 한도 / buy / partial / 직전 완료 봉 목표 비중 100%; 다음 봉 시가 가정 |
| v2 | trend_8_26 | 9851.07 | -148.93 | buy / partial / 직전 완료 봉 목표 비중 100%; 다음 봉 시가 가정 |
| v2 | momentum_26 | 9885.12 | -114.88 | sell / filled / 직전 완료 봉 목표 비중 0%; 다음 봉 시가 가정 |
| v2 | breakout_8 | 9610.96 | -389.04 | sell / filled / 직전 완료 봉 목표 비중 0%; 다음 봉 시가 가정 |
| v2 | reversion_12 | 8946.19 | -1053.81 | 중단: 손실 한도 / buy / partial / 직전 완료 봉 목표 비중 100%; 다음 봉 시가 가정 |
| v2 | volume_26 | 9202.04 | -797.96 | 중단: 손실 한도 / buy / partial / 직전 완료 봉 목표 비중 100%; 다음 봉 시가 가정 |
| v2 | trend_8_26 AND momentum_26 | 9914.96 | -85.04 | sell / filled / 직전 완료 봉 목표 비중 0%; 다음 봉 시가 가정 |
| v2 | trend_8_26 + momentum_26 | 9868.22 | -131.78 | buy / filled / 직전 완료 봉 목표 비중 50%; 다음 봉 시가 가정 |
| v2 | trend_8_26 AND breakout_8 | 9765.08 | -234.92 | sell / filled / 직전 완료 봉 목표 비중 0%; 다음 봉 시가 가정 |
| v2 | trend_8_26 + breakout_8 | 9730.72 | -269.28 | buy / filled / 직전 완료 봉 목표 비중 50%; 다음 봉 시가 가정 |
| v2 | trend_8_26 AND reversion_12 | 9738.62 | -261.38 | sell / filled / 직전 완료 봉 목표 비중 0%; 다음 봉 시가 가정 |
| v2 | trend_8_26 + reversion_12 | 9517.98 | -482.02 | buy / filled / 직전 완료 봉 목표 비중 50%; 다음 봉 시가 가정 |
| v2 | trend_8_26 AND volume_26 | 10035.44 | 35.44 | sell / filled / 직전 완료 봉 목표 비중 0%; 다음 봉 시가 가정 |
| v2 | trend_8_26 + volume_26 | 9597.29 | -402.71 | buy / filled / 직전 완료 봉 목표 비중 50%; 다음 봉 시가 가정 |
| v2 | momentum_26 AND breakout_8 | 9824.16 | -175.84 | sell / filled / 직전 완료 봉 목표 비중 0%; 다음 봉 시가 가정 |
| v2 | momentum_26 + breakout_8 | 9747.29 | -252.71 | sell / filled / 직전 완료 봉 목표 비중 0%; 다음 봉 시가 가정 |
| v2 | momentum_26 AND reversion_12 | 9755.55 | -244.45 | sell / filled / 직전 완료 봉 목표 비중 0%; 다음 봉 시가 가정 |
| v2 | momentum_26 + reversion_12 | 9514.36 | -485.64 | sell / filled / 직전 완료 봉 목표 비중 0%; 다음 봉 시가 가정 |
| v2 | momentum_26 AND volume_26 | 10048.78 | 48.78 | sell / filled / 직전 완료 봉 목표 비중 0%; 다음 봉 시가 가정 |
| v2 | momentum_26 + volume_26 | 9633.99 | -366.01 | sell / filled / 직전 완료 봉 목표 비중 0%; 다음 봉 시가 가정 |
| v2 | breakout_8 AND reversion_12 | 10000.00 | 0.00 | 대기 /  / 새 신호 대기 |
| v2 | breakout_8 + reversion_12 | 9610.18 | -389.82 | 중단: 손실 한도 / sell / filled / 직전 완료 봉 목표 비중 0%; 다음 봉 시가 가정 |
| v2 | breakout_8 AND volume_26 | 9998.69 | -1.31 | sell / filled / 직전 완료 봉 목표 비중 0%; 다음 봉 시가 가정 |
| v2 | breakout_8 + volume_26 | 9499.63 | -500.37 | sell / filled / 직전 완료 봉 목표 비중 0%; 다음 봉 시가 가정 |
| v2 | reversion_12 AND volume_26 | 9138.38 | -861.62 | 중단: 손실 한도 / buy / partial / 직전 완료 봉 목표 비중 100%; 다음 봉 시가 가정 |
| v2 | reversion_12 + volume_26 | 9335.22 | -664.78 | 중단: 손실 한도 / sell / filled / 직전 완료 봉 목표 비중 50%; 다음 봉 시가 가정 |
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
| v2 | chaikin_3_10 | 9555.08 | -444.92 | 중단: 손실 한도 / buy / partial / ADL의 EMA3 - EMA10 > 0 그리고 종가 > EMA26; 조건 충족; Chaikin3_10=293683, ADL=-4.91156e+06, close=739.58, EMA26=736.187; 직전 완료 봉 목표를 다음 봉 시가에 모의 적용 |
| v2 | roc_10_momentum | 9961.14 | -38.86 | sell / filled / 10봉 ROC > 1% 그리고 종가 > EMA26; 조건 미충족; ROC10_percent=-0.134597, close=734.53, EMA26=735.486; 직전 완료 봉 목표를 다음 봉 시가에 모의 적용 |
| v2 | trix_15_trend | 9564.71 | -435.29 | 중단: 손실 한도 / buy / partial / 15봉 삼중 EMA의 1봉 변화율 TRIX > 0 그리고 종가 > EMA26; 조건 충족; TRIX15_percent=0.0196284, close=739.58, EMA26=736.187; 직전 완료 봉 목표를 다음 봉 시가에 모의 적용 |
| v2 | keltner_20_breakout | 10000.00 | 0.00 | 대기 /  / 새 신호 대기 |
| v2 | opening_range_30m | 10038.70 | 38.70 | sell / filled / 뉴욕 09:30·09:45 두 완료 봉 최고가를 10:00 이후 종가가 돌파; 자료 부족·변동폭 또는 거래량 없음: 대기; close=740.21; 직전 완료 봉 목표를 다음 봉 시가에 모의 적용 |

### 같은 기간의 비용·노출 비교 (사후 연구)

| 전략 | 비용 전 | 비용 후 | 100% 보유 | 같은 평균 노출 보유 | 평균 노출 |
|---|---:|---:|---:|---:|---:|
| cash | 0.00% | 0.00% | -11.66% | -0.00% | 0.00% |
| buy_hold | -11.29% | -11.66% | -11.66% | -11.66% | 100.00% |
| trend_8_26 | -0.58% | -4.26% | -11.66% | -5.47% | 46.19% |
| momentum_26 | -3.01% | -7.00% | -11.66% | -5.37% | 45.41% |
| breakout_8 | -2.78% | -15.01% | -11.66% | -1.72% | 14.44% |
| reversion_12 | -3.30% | -16.52% | -11.66% | -3.31% | 27.82% |
| volume_26 | -3.22% | -9.51% | -11.66% | -0.91% | 7.61% |
| trend_8_26 AND momentum_26 | -0.26% | -3.15% | -11.66% | -4.70% | 39.63% |
| trend_8_26 + momentum_26 | -1.79% | -5.63% | -11.66% | -5.42% | 45.80% |
| trend_8_26 AND breakout_8 | -1.69% | -8.46% | -11.66% | -0.85% | 7.09% |
| trend_8_26 + breakout_8 | -1.65% | -9.58% | -11.66% | -3.60% | 30.32% |
| trend_8_26 AND reversion_12 | 1.56% | -5.43% | -11.66% | -0.78% | 6.56% |
| trend_8_26 + reversion_12 | -1.88% | -9.82% | -11.66% | -4.39% | 37.01% |
| trend_8_26 AND volume_26 | 1.93% | -0.18% | -11.66% | -0.25% | 2.10% |
| trend_8_26 + volume_26 | -1.85% | -6.70% | -11.66% | -3.20% | 26.91% |
| momentum_26 AND breakout_8 | -2.12% | -9.25% | -11.66% | -0.91% | 7.61% |
| momentum_26 + breakout_8 | -2.86% | -11.07% | -11.66% | -3.56% | 29.93% |
| momentum_26 AND reversion_12 | -2.51% | -8.84% | -11.66% | -0.78% | 6.56% |
| momentum_26 + reversion_12 | -3.10% | -11.12% | -11.66% | -4.34% | 36.62% |
| momentum_26 AND volume_26 | 1.45% | -0.24% | -11.66% | -0.16% | 1.31% |
| momentum_26 + volume_26 | -3.06% | -7.85% | -11.66% | -3.15% | 26.51% |
| breakout_8 AND reversion_12 | 0.00% | 0.00% | -11.66% | -0.00% | 0.00% |
| breakout_8 + reversion_12 | -2.98% | -14.86% | -11.66% | -2.52% | 21.14% |
| breakout_8 AND volume_26 | 0.37% | -0.47% | -11.66% | -0.06% | 0.52% |
| breakout_8 + volume_26 | -2.97% | -11.73% | -11.66% | -1.32% | 11.03% |
| reversion_12 AND volume_26 | -1.40% | -5.45% | -11.66% | -0.60% | 4.99% |
| reversion_12 + volume_26 | -3.22% | -12.33% | -11.66% | -2.11% | 17.72% |
| ema_12_26 | -1.37% | -3.42% | -11.66% | -5.25% | 44.36% |
| macd_12_26_9 | 1.07% | -1.86% | -11.66% | -3.25% | 27.30% |
| rsi_14_recovery | -0.69% | -6.36% | -11.66% | -0.44% | 3.67% |
| bollinger_20_reentry | -0.24% | -6.33% | -11.66% | -0.47% | 3.94% |
| donchian_20 | -1.20% | -5.26% | -11.66% | -0.56% | 4.72% |
| atr_14_breakout | -1.85% | -8.23% | -11.66% | -0.53% | 4.46% |
| session_vwap | 0.31% | -11.56% | -11.66% | -5.22% | 44.09% |
| obv_20 | -4.13% | -13.32% | -11.66% | -2.75% | 23.10% |
| stochastic_14_3_recovery | -2.81% | -14.32% | -11.66% | -0.94% | 7.87% |
| mfi_14_recovery | 1.43% | -1.10% | -11.66% | -0.19% | 1.57% |
| adx_14_trend | -2.02% | -4.05% | -11.66% | -1.00% | 8.40% |
| aroon_25_trend | -1.25% | -4.91% | -11.66% | -1.53% | 12.86% |
| cci_20_momentum | -4.37% | -9.45% | -11.66% | -1.75% | 14.70% |
| williams_14_recovery | -0.47% | -10.39% | -11.66% | -0.78% | 6.56% |
| cmf_20_accumulation | -5.52% | -12.03% | -11.66% | -1.97% | 16.54% |
| chaikin_3_10 | -6.04% | -15.05% | -11.66% | -3.71% | 31.23% |
| roc_10_momentum | -1.79% | -7.40% | -11.66% | -1.50% | 12.60% |
| trix_15_trend | -1.68% | -6.12% | -11.66% | -4.08% | 34.38% |
| keltner_20_breakout | -2.87% | -5.29% | -11.66% | -0.31% | 2.62% |
| opening_range_30m | 6.14% | 1.77% | -11.66% | -2.38% | 19.95% |

동일 구간·초기 자금, 종료 시 청산 비용 포함. 노출 맞춤은 사후 설명용이며 v2 실제 계좌 성과가 아닙니다.
[낙폭 분해·비용 영향·전체 구간](CAT/comparison.json)

[v1 전체 기록](CAT/accounts.json) · [v2 전체 기록](CAT/accounts-v2.json)

## WMT 계좌

| 모델 | 전략 | 평가액 USD | 손익 USD | 최근 매매·이유 |
|---|---|---:|---:|---|
| v1 | cash | 10000.00 | 0.00 | 대기 /  / 새 신호 대기 |
| v1 | buy_hold | 10034.52 | 34.52 | buy /  / buy_hold: prior completed bar target 100%; next bar open simulation |
| v1 | trend_8_26 | 9895.09 | -104.91 | sell /  / trend_8_26: prior completed bar target 0%; next bar open simulation |
| v1 | momentum_26 | 9909.32 | -90.68 | buy /  / momentum_26: prior completed bar target 100%; next bar open simulation |
| v1 | breakout_8 | 9800.08 | -199.92 | sell /  / breakout_8: prior completed bar target 0%; next bar open simulation |
| v1 | reversion_12 | 9916.28 | -83.72 | sell /  / reversion_12: prior completed bar target 0%; next bar open simulation |
| v1 | volume_26 | 9915.76 | -84.24 | sell /  / volume_26: prior completed bar target 0%; next bar open simulation |
| v1 | trend_8_26 AND momentum_26 | 9899.88 | -100.12 | sell /  / trend_8_26 AND momentum_26: prior completed bar target 0%; next bar open simulation |
| v1 | trend_8_26 + momentum_26 | 9902.23 | -97.77 | buy /  / trend_8_26 + momentum_26: prior completed bar target 50%; next bar open simulation |
| v1 | trend_8_26 AND breakout_8 | 9950.02 | -49.98 | sell /  / trend_8_26 AND breakout_8: prior completed bar target 0%; next bar open simulation |
| v1 | trend_8_26 + breakout_8 | 9847.38 | -152.62 | sell /  / trend_8_26 + breakout_8: prior completed bar target 0%; next bar open simulation |
| v1 | trend_8_26 AND reversion_12 | 9967.64 | -32.36 | sell /  / trend_8_26 AND reversion_12: prior completed bar target 0%; next bar open simulation |
| v1 | trend_8_26 + reversion_12 | 9925.44 | -74.56 | sell /  / trend_8_26 + reversion_12: prior completed bar target 0%; next bar open simulation |
| v1 | trend_8_26 AND volume_26 | 10000.00 | 0.00 | 대기 /  / 새 신호 대기 |
| v1 | trend_8_26 + volume_26 | 9905.33 | -94.67 | sell /  / trend_8_26 + volume_26: prior completed bar target 0%; next bar open simulation |
| v1 | momentum_26 AND breakout_8 | 9911.55 | -88.45 | sell /  / momentum_26 AND breakout_8: prior completed bar target 0%; next bar open simulation |
| v1 | momentum_26 + breakout_8 | 9894.11 | -105.89 | sell /  / momentum_26 + breakout_8: prior completed bar target 50%; next bar open simulation |
| v1 | momentum_26 AND reversion_12 | 10011.47 | 11.47 | sell /  / momentum_26 AND reversion_12: prior completed bar target 0%; next bar open simulation |
| v1 | momentum_26 + reversion_12 | 9952.41 | -47.59 | buy /  / momentum_26 + reversion_12: prior completed bar target 50%; next bar open simulation |
| v1 | momentum_26 AND volume_26 | 10013.52 | 13.52 | sell /  / momentum_26 AND volume_26: prior completed bar target 0%; next bar open simulation |
| v1 | momentum_26 + volume_26 | 9932.33 | -67.67 | buy /  / momentum_26 + volume_26: prior completed bar target 50%; next bar open simulation |
| v1 | breakout_8 AND reversion_12 | 10000.00 | 0.00 | 대기 /  / 새 신호 대기 |
| v1 | breakout_8 + reversion_12 | 9877.73 | -122.27 | sell /  / breakout_8 + reversion_12: prior completed bar target 0%; next bar open simulation |
| v1 | breakout_8 AND volume_26 | 9913.57 | -86.43 | sell /  / breakout_8 AND volume_26: prior completed bar target 0%; next bar open simulation |
| v1 | breakout_8 + volume_26 | 9857.82 | -142.18 | sell /  / breakout_8 + volume_26: prior completed bar target 0%; next bar open simulation |
| v1 | reversion_12 AND volume_26 | 10000.00 | 0.00 | 대기 /  / 새 신호 대기 |
| v1 | reversion_12 + volume_26 | 9955.79 | -44.21 | sell /  / reversion_12 + volume_26: prior completed bar target 0%; next bar open simulation |
| v1 | ema_12_26 | 9987.48 | -12.52 | sell /  / EMA12 > EMA26; 조건 미충족; EMA12=118.639, EMA26=118.64 |
| v1 | macd_12_26_9 | 10000.00 | 0.00 | 대기 /  / 새 신호 대기 |
| v1 | rsi_14_recovery | 10000.00 | 0.00 | 대기 /  / 새 신호 대기 |
| v1 | bollinger_20_reentry | 10000.00 | 0.00 | 대기 /  / 새 신호 대기 |
| v1 | donchian_20 | 10000.00 | 0.00 | 대기 /  / 새 신호 대기 |
| v1 | atr_14_breakout | 9979.72 | -20.28 | sell /  / 종가 > 직전 종가 + 직전 ATR14 그리고 종가 > EMA26; 조건 미충족; close=119.375, threshold=119.607, prior_ATR14=0.486823, EMA26=118.217 |
| v1 | session_vwap | 9719.67 | -280.33 | buy /  / 종가 > 뉴욕 거래일별 누적 전형가격 VWAP; 조건 충족; close=118.68, session_VWAP=118.618, session_volume=1.15133e+07 |
| v1 | obv_20 | 9848.53 | -151.47 | buy /  / OBV > OBV의 SMA20 그리고 종가 > EMA26; 조건 충족; OBV=2.23382e+07, OBV_SMA20=1.748e+07, close=118.68, EMA26=118.585 |
| v1 | stochastic_14_3_recovery | 9979.72 | -20.28 | sell /  / 직전 %K14 < 20에서 %K14가 %D3 상향 돌파 (한 봉 목표); 조건 미충족; K14=93.8952, D3=60.8222, previous_K14=82.4242, previous_D3=34.5012 |
| v1 | mfi_14_recovery | 10000.00 | 0.00 | 대기 /  / 새 신호 대기 |
| v1 | adx_14_trend | 9991.69 | -8.31 | sell /  / Wilder ADX14 >= 25 그리고 +DI14 > -DI14; 조건 미충족; ADX14=24.5142, plus_DI14=24.7537, minus_DI14=21.6519 |
| v1 | aroon_25_trend | 10000.00 | 0.00 | 대기 /  / 새 신호 대기 |
| v1 | cci_20_momentum | 9932.96 | -67.04 | sell /  / CCI20 > 100 (전형가격·평균절대편차); 조건 미충족; CCI20=99.1325 |
| v1 | williams_14_recovery | 9979.72 | -20.28 | sell /  / 직전 Williams %R14 < -80, 현재 >= -80 (한 봉 목표); 조건 미충족; Williams_R14=-6.10484, previous_R14=-17.5758 |
| v1 | cmf_20_accumulation | 9877.23 | -122.77 | buy /  / Chaikin Money Flow20 > 0.1; 조건 충족; CMF20=0.112667, volume20=1.57051e+07 |
| v1 | chaikin_3_10 | 9707.45 | -292.55 | buy /  / ADL의 EMA3 - EMA10 > 0 그리고 종가 > EMA26; 조건 충족; Chaikin3_10=395736, ADL=1.91464e+07, close=118.68, EMA26=118.585 |
| v1 | roc_10_momentum | 10000.00 | 0.00 | 대기 /  / 새 신호 대기 |
| v1 | trix_15_trend | 9824.31 | -175.69 | sell /  / 15봉 삼중 EMA의 1봉 변화율 TRIX > 0 그리고 종가 > EMA26; 조건 미충족; TRIX15_percent=0.00969478, close=118.67, EMA26=118.682 |
| v1 | keltner_20_breakout | 10000.00 | 0.00 | 대기 /  / 새 신호 대기 |
| v1 | opening_range_30m | 10000.00 | 0.00 | 대기 /  / 새 신호 대기 |
| v2 | cash | 10000.00 | 0.00 | 대기 /  / 새 신호 대기 |
| v2 | buy_hold | 10631.47 | 631.47 | buy / partial / 직전 완료 봉 목표 비중 100%; 다음 봉 시가 가정 |
| v2 | trend_8_26 | 10297.28 | 297.28 | sell / filled / 직전 완료 봉 목표 비중 0%; 다음 봉 시가 가정 |
| v2 | momentum_26 | 10318.01 | 318.01 | buy / partial / 직전 완료 봉 목표 비중 100%; 다음 봉 시가 가정 |
| v2 | breakout_8 | 9757.62 | -242.38 | sell / filled / 직전 완료 봉 목표 비중 0%; 다음 봉 시가 가정 |
| v2 | reversion_12 | 9818.63 | -181.37 | sell / filled / 직전 완료 봉 목표 비중 0%; 다음 봉 시가 가정 |
| v2 | volume_26 | 9875.40 | -124.60 | sell / filled / 직전 완료 봉 목표 비중 0%; 다음 봉 시가 가정 |
| v2 | trend_8_26 AND momentum_26 | 10302.26 | 302.26 | sell / filled / 직전 완료 봉 목표 비중 0%; 다음 봉 시가 가정 |
| v2 | trend_8_26 + momentum_26 | 10307.61 | 307.61 | buy / filled / 직전 완료 봉 목표 비중 50%; 다음 봉 시가 가정 |
| v2 | trend_8_26 AND breakout_8 | 10036.12 | 36.12 | sell / filled / 직전 완료 봉 목표 비중 0%; 다음 봉 시가 가정 |
| v2 | trend_8_26 + breakout_8 | 10024.13 | 24.13 | sell / filled / 직전 완료 봉 목표 비중 0%; 다음 봉 시가 가정 |
| v2 | trend_8_26 AND reversion_12 | 9775.04 | -224.96 | sell / filled / 직전 완료 봉 목표 비중 0%; 다음 봉 시가 가정 |
| v2 | trend_8_26 + reversion_12 | 10077.59 | 77.59 | sell / filled / 직전 완료 봉 목표 비중 0%; 다음 봉 시가 가정 |
| v2 | trend_8_26 AND volume_26 | 9949.23 | -50.77 | sell / filled / 직전 완료 봉 목표 비중 0%; 다음 봉 시가 가정 |
| v2 | trend_8_26 + volume_26 | 10085.48 | 85.48 | sell / filled / 직전 완료 봉 목표 비중 0%; 다음 봉 시가 가정 |
| v2 | momentum_26 AND breakout_8 | 9872.56 | -127.44 | sell / filled / 직전 완료 봉 목표 비중 0%; 다음 봉 시가 가정 |
| v2 | momentum_26 + breakout_8 | 10076.60 | 76.60 | sell / filled / 직전 완료 봉 목표 비중 50%; 다음 봉 시가 가정 |
| v2 | momentum_26 AND reversion_12 | 9838.09 | -161.91 | sell / filled / 직전 완료 봉 목표 비중 0%; 다음 봉 시가 가정 |
| v2 | momentum_26 + reversion_12 | 10151.51 | 151.51 | buy / filled / 직전 완료 봉 목표 비중 50%; 다음 봉 시가 가정 |
| v2 | momentum_26 AND volume_26 | 9925.24 | -74.76 | sell / filled / 직전 완료 봉 목표 비중 0%; 다음 봉 시가 가정 |
| v2 | momentum_26 + volume_26 | 10116.94 | 116.94 | buy / filled / 직전 완료 봉 목표 비중 50%; 다음 봉 시가 가정 |
| v2 | breakout_8 AND reversion_12 | 10000.00 | 0.00 | 대기 /  / 새 신호 대기 |
| v2 | breakout_8 + reversion_12 | 9830.40 | -169.60 | sell / filled / 직전 완료 봉 목표 비중 0%; 다음 봉 시가 가정 |
| v2 | breakout_8 AND volume_26 | 9860.28 | -139.72 | sell / filled / 직전 완료 봉 목표 비중 0%; 다음 봉 시가 가정 |
| v2 | breakout_8 + volume_26 | 9817.77 | -182.23 | sell / filled / 직전 완료 봉 목표 비중 0%; 다음 봉 시가 가정 |
| v2 | reversion_12 AND volume_26 | 10009.78 | 9.78 | sell / filled / 직전 완료 봉 목표 비중 0%; 다음 봉 시가 가정 |
| v2 | reversion_12 + volume_26 | 9888.34 | -111.66 | sell / filled / 직전 완료 봉 목표 비중 0%; 다음 봉 시가 가정 |
| v2 | ema_12_26 | 9985.48 | -14.52 | sell / filled / EMA12 > EMA26; 조건 미충족; EMA12=118.639, EMA26=118.64; 직전 완료 봉 목표를 다음 봉 시가에 모의 적용 |
| v2 | macd_12_26_9 | 10000.00 | 0.00 | 대기 /  / 새 신호 대기 |
| v2 | rsi_14_recovery | 10000.00 | 0.00 | 대기 /  / 새 신호 대기 |
| v2 | bollinger_20_reentry | 10000.00 | 0.00 | 대기 /  / 새 신호 대기 |
| v2 | donchian_20 | 10000.00 | 0.00 | 대기 /  / 새 신호 대기 |
| v2 | atr_14_breakout | 9977.72 | -22.28 | sell / filled / 종가 > 직전 종가 + 직전 ATR14 그리고 종가 > EMA26; 조건 미충족; close=119.375, threshold=119.607, prior_ATR14=0.486823, EMA26=118.217; 직전 완료 봉 목표를 다음 봉 시가에 모의 적용 |
| v2 | session_vwap | 9708.98 | -291.02 | buy / partial / 종가 > 뉴욕 거래일별 누적 전형가격 VWAP; 조건 충족; close=118.68, session_VWAP=118.618, session_volume=1.15133e+07; 직전 완료 봉 목표를 다음 봉 시가에 모의 적용 |
| v2 | obv_20 | 9841.64 | -158.36 | buy / partial / OBV > OBV의 SMA20 그리고 종가 > EMA26; 조건 충족; OBV=2.23382e+07, OBV_SMA20=1.748e+07, close=118.68, EMA26=118.585; 직전 완료 봉 목표를 다음 봉 시가에 모의 적용 |
| v2 | stochastic_14_3_recovery | 9977.72 | -22.28 | sell / filled / 직전 %K14 < 20에서 %K14가 %D3 상향 돌파 (한 봉 목표); 조건 미충족; K14=93.8952, D3=60.8222, previous_K14=82.4242, previous_D3=34.5012; 직전 완료 봉 목표를 다음 봉 시가에 모의 적용 |
| v2 | mfi_14_recovery | 10000.00 | 0.00 | 대기 /  / 새 신호 대기 |
| v2 | adx_14_trend | 9989.70 | -10.30 | sell / filled / Wilder ADX14 >= 25 그리고 +DI14 > -DI14; 조건 미충족; ADX14=24.5142, plus_DI14=24.7537, minus_DI14=21.6519; 직전 완료 봉 목표를 다음 봉 시가에 모의 적용 |
| v2 | aroon_25_trend | 10000.00 | 0.00 | 대기 /  / 새 신호 대기 |
| v2 | cci_20_momentum | 9930.98 | -69.02 | sell / filled / CCI20 > 100 (전형가격·평균절대편차); 조건 미충족; CCI20=99.1325; 직전 완료 봉 목표를 다음 봉 시가에 모의 적용 |
| v2 | williams_14_recovery | 9977.72 | -22.28 | sell / filled / 직전 Williams %R14 < -80, 현재 >= -80 (한 봉 목표); 조건 미충족; Williams_R14=-6.10484, previous_R14=-17.5758; 직전 완료 봉 목표를 다음 봉 시가에 모의 적용 |
| v2 | cmf_20_accumulation | 9872.29 | -127.71 | buy / partial / Chaikin Money Flow20 > 0.1; 조건 충족; CMF20=0.112667, volume20=1.57051e+07; 직전 완료 봉 목표를 다음 봉 시가에 모의 적용 |
| v2 | chaikin_3_10 | 9696.78 | -303.22 | buy / partial / ADL의 EMA3 - EMA10 > 0 그리고 종가 > EMA26; 조건 충족; Chaikin3_10=395736, ADL=1.91464e+07, close=118.68, EMA26=118.585; 직전 완료 봉 목표를 다음 봉 시가에 모의 적용 |
| v2 | roc_10_momentum | 10000.00 | 0.00 | 대기 /  / 새 신호 대기 |
| v2 | trix_15_trend | 9818.42 | -181.58 | sell / filled / 15봉 삼중 EMA의 1봉 변화율 TRIX > 0 그리고 종가 > EMA26; 조건 미충족; TRIX15_percent=0.00969478, close=118.67, EMA26=118.682; 직전 완료 봉 목표를 다음 봉 시가에 모의 적용 |
| v2 | keltner_20_breakout | 10000.00 | 0.00 | 대기 /  / 새 신호 대기 |
| v2 | opening_range_30m | 10000.00 | 0.00 | 대기 /  / 새 신호 대기 |

### 같은 기간의 비용·노출 비교 (사후 연구)

| 전략 | 비용 전 | 비용 후 | 100% 보유 | 같은 평균 노출 보유 | 평균 노출 |
|---|---:|---:|---:|---:|---:|
| cash | 0.00% | 0.00% | 8.65% | 0.00% | 0.00% |
| buy_hold | 9.11% | 8.65% | 8.65% | 8.65% | 100.00% |
| trend_8_26 | 8.17% | 5.03% | 8.65% | 5.66% | 65.62% |
| momentum_26 | 6.69% | 1.02% | 8.65% | 5.77% | 66.93% |
| breakout_8 | 5.02% | -11.59% | 8.65% | 2.21% | 25.72% |
| reversion_12 | 4.11% | -6.66% | 8.65% | 1.53% | 17.85% |
| volume_26 | -0.63% | -6.30% | 8.65% | 0.52% | 6.04% |
| trend_8_26 AND momentum_26 | 7.90% | 3.46% | 8.65% | 5.09% | 59.06% |
| trend_8_26 + momentum_26 | 7.44% | 3.01% | 8.65% | 5.71% | 66.28% |
| trend_8_26 AND breakout_8 | 6.75% | -5.88% | 8.65% | 1.78% | 20.73% |
| trend_8_26 + breakout_8 | 6.60% | -3.63% | 8.65% | 3.93% | 45.68% |
| trend_8_26 AND reversion_12 | 0.27% | -4.66% | 8.65% | 0.56% | 6.56% |
| trend_8_26 + reversion_12 | 6.16% | -0.56% | 8.65% | 3.59% | 41.74% |
| trend_8_26 AND volume_26 | 0.53% | -1.56% | 8.65% | 0.16% | 1.84% |
| trend_8_26 + volume_26 | 3.71% | -0.37% | 8.65% | 3.08% | 35.83% |
| momentum_26 AND breakout_8 | 5.42% | -7.84% | 8.65% | 1.91% | 22.31% |
| momentum_26 + breakout_8 | 5.87% | -4.89% | 8.65% | 3.99% | 46.33% |
| momentum_26 AND reversion_12 | 1.20% | -4.18% | 8.65% | 0.63% | 7.35% |
| momentum_26 + reversion_12 | 5.43% | -0.61% | 8.65% | 3.65% | 42.39% |
| momentum_26 AND volume_26 | 0.38% | -3.75% | 8.65% | 0.25% | 2.89% |
| momentum_26 + volume_26 | 3.00% | -2.49% | 8.65% | 3.14% | 36.49% |
| breakout_8 AND reversion_12 | 0.00% | 0.00% | 8.65% | 0.00% | 0.00% |
| breakout_8 + reversion_12 | 4.59% | -8.58% | 8.65% | 1.87% | 21.79% |
| breakout_8 AND volume_26 | 1.02% | -1.49% | 8.65% | 0.16% | 1.84% |
| breakout_8 + volume_26 | 2.18% | -8.59% | 8.65% | 1.36% | 15.89% |
| reversion_12 AND volume_26 | -0.51% | -2.99% | 8.65% | 0.20% | 2.36% |
| reversion_12 + volume_26 | 1.72% | -5.89% | 8.65% | 1.02% | 11.95% |
| ema_12_26 | 8.61% | 7.25% | 8.65% | 5.86% | 67.98% |
| macd_12_26_9 | 7.96% | 4.83% | 8.65% | 2.82% | 32.81% |
| rsi_14_recovery | -0.68% | -2.74% | 8.65% | 0.11% | 1.31% |
| bollinger_20_reentry | 0.93% | -2.41% | 8.65% | 0.18% | 2.10% |
| donchian_20 | 4.80% | -7.22% | 8.65% | 1.12% | 13.12% |
| atr_14_breakout | -0.61% | -10.14% | 8.65% | 0.63% | 7.35% |
| session_vwap | 6.61% | -4.41% | 8.65% | 4.95% | 57.48% |
| obv_20 | 8.55% | 0.64% | 8.65% | 4.63% | 53.81% |
| stochastic_14_3_recovery | 1.36% | -8.36% | 8.65% | 0.54% | 6.30% |
| mfi_14_recovery | 0.02% | -0.81% | 8.65% | 0.04% | 0.52% |
| adx_14_trend | 8.84% | 6.13% | 8.65% | 4.36% | 50.66% |
| aroon_25_trend | 5.69% | 1.34% | 8.65% | 2.50% | 29.13% |
| cci_20_momentum | 7.19% | -0.62% | 8.65% | 2.66% | 30.97% |
| williams_14_recovery | 0.16% | -7.91% | 8.65% | 0.45% | 5.25% |
| cmf_20_accumulation | 8.22% | -0.50% | 8.65% | 2.93% | 34.12% |
| chaikin_3_10 | 5.21% | -3.27% | 8.65% | 4.31% | 50.13% |
| roc_10_momentum | -0.30% | -5.20% | 8.65% | 1.24% | 14.44% |
| trix_15_trend | 7.93% | 4.80% | 8.65% | 5.41% | 62.73% |
| keltner_20_breakout | 6.84% | 0.74% | 8.65% | 2.25% | 26.25% |
| opening_range_30m | 10.12% | 5.59% | 8.65% | 2.98% | 34.65% |

동일 구간·초기 자금, 종료 시 청산 비용 포함. 노출 맞춤은 사후 설명용이며 v2 실제 계좌 성과가 아닙니다.
[낙폭 분해·비용 영향·전체 구간](WMT/comparison.json)

[v1 전체 기록](WMT/accounts.json) · [v2 전체 기록](WMT/accounts-v2.json)
