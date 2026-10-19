# 모의투자 운영 현황

[PC·서버 장애 진단과 복구 방법](https://github.com/BaekJaeYeol/paper-trading-program/blob/main/investment-lab/docs/failure-recovery.md)

이번 실행 복구: {}

완료 봉 확인 주기: 기록 5/20회 · 기록 없는 예정 15회 · 아직 판정 전 6회 · 주의: 예약 시작 지연 또는 실행·저장 누락을 확인하세요.

[주기 판정 기준](https://github.com/BaekJaeYeol/paper-trading-program/blob/main/investment-lab/docs/session-coverage.md)

최근 확인: 2026-10-19T18:52:00.442554+00:00 (UTC)
다음 15분 확인 목표 (세션 실행 중에만 적용): 2026-10-19T19:07:00+00:00 (UTC, 실행 지연 가능)

실제 주문 없음. v1 기존 계좌와 v2 새 계좌의 시작일이 다르므로 수익률을 직접 우열 비교하지 마세요.
v2는 다음 봉 시가에 비용·스프레드·직전 거래량 제한을 적용한 가상 체결입니다. 미체결 잔량은 만료됩니다.

| 종목 | 상태 | 최근 성공 UTC | 마지막 완료 봉 UTC | 이번 새 봉 |
|---|---|---|---|---|
| SPY | updated | 2026-10-19T18:52:00.442554+00:00 | 2026-10-19T18:30:00+00:00 | 1 |
| QQQ | updated | 2026-10-19T18:52:00.442554+00:00 | 2026-10-19T18:30:00+00:00 | 1 |
| IWM | updated | 2026-10-19T18:52:00.442554+00:00 | 2026-10-19T18:30:00+00:00 | 1 |
| DIA | updated | 2026-10-19T18:52:00.442554+00:00 | 2026-10-19T18:30:00+00:00 | 1 |
| MSFT | updated | 2026-10-19T18:52:00.442554+00:00 | 2026-10-19T18:30:00+00:00 | 1 |
| JPM | updated | 2026-10-19T18:52:00.442554+00:00 | 2026-10-19T18:30:00+00:00 | 1 |
| XOM | updated | 2026-10-19T18:52:00.442554+00:00 | 2026-10-19T18:30:00+00:00 | 1 |
| JNJ | updated | 2026-10-19T18:52:00.442554+00:00 | 2026-10-19T18:30:00+00:00 | 1 |
| CAT | updated | 2026-10-19T18:52:00.442554+00:00 | 2026-10-19T18:30:00+00:00 | 1 |
| WMT | updated | 2026-10-19T18:52:00.442554+00:00 | 2026-10-19T18:30:00+00:00 | 1 |

이번 실행 소요: 45.68초
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
| v1 | buy_hold | 9906.46 | -93.54 | buy /  / buy_hold: prior completed bar target 100%; next bar open simulation |
| v1 | trend_8_26 | 9884.78 | -115.22 | buy /  / trend_8_26: prior completed bar target 100%; next bar open simulation |
| v1 | momentum_26 | 9866.27 | -133.73 | buy /  / momentum_26: prior completed bar target 100%; next bar open simulation |
| v1 | breakout_8 | 9873.76 | -126.24 | sell /  / breakout_8: prior completed bar target 0%; next bar open simulation |
| v1 | reversion_12 | 9844.51 | -155.49 | sell /  / reversion_12: prior completed bar target 0%; next bar open simulation |
| v1 | volume_26 | 9790.14 | -209.86 | sell /  / volume_26: prior completed bar target 0%; next bar open simulation |
| v1 | trend_8_26 AND momentum_26 | 9866.27 | -133.73 | buy /  / trend_8_26 AND momentum_26: prior completed bar target 100%; next bar open simulation |
| v1 | trend_8_26 + momentum_26 | 9875.51 | -124.49 | buy /  / trend_8_26 + momentum_26: prior completed bar target 100%; next bar open simulation |
| v1 | trend_8_26 AND breakout_8 | 9970.32 | -29.68 | sell /  / trend_8_26 AND breakout_8: prior completed bar target 0%; next bar open simulation |
| v1 | trend_8_26 + breakout_8 | 9898.95 | -101.05 | buy /  / trend_8_26 + breakout_8: prior completed bar target 50%; next bar open simulation |
| v1 | trend_8_26 AND reversion_12 | 9908.20 | -91.80 | sell /  / trend_8_26 AND reversion_12: prior completed bar target 0%; next bar open simulation |
| v1 | trend_8_26 + reversion_12 | 9864.53 | -135.47 | buy /  / trend_8_26 + reversion_12: prior completed bar target 50%; next bar open simulation |
| v1 | trend_8_26 AND volume_26 | 9836.21 | -163.79 | sell /  / trend_8_26 AND volume_26: prior completed bar target 0%; next bar open simulation |
| v1 | trend_8_26 + volume_26 | 9837.29 | -162.71 | buy /  / trend_8_26 + volume_26: prior completed bar target 50%; next bar open simulation |
| v1 | momentum_26 AND breakout_8 | 9954.13 | -45.87 | sell /  / momentum_26 AND breakout_8: prior completed bar target 0%; next bar open simulation |
| v1 | momentum_26 + breakout_8 | 9869.97 | -130.03 | buy /  / momentum_26 + breakout_8: prior completed bar target 50%; next bar open simulation |
| v1 | momentum_26 AND reversion_12 | 9961.77 | -38.23 | sell /  / momentum_26 AND reversion_12: prior completed bar target 0%; next bar open simulation |
| v1 | momentum_26 + reversion_12 | 9875.01 | -124.99 | buy /  / momentum_26 + reversion_12: prior completed bar target 50%; next bar open simulation |
| v1 | momentum_26 AND volume_26 | 9849.91 | -150.09 | sell /  / momentum_26 AND volume_26: prior completed bar target 0%; next bar open simulation |
| v1 | momentum_26 + volume_26 | 9828.08 | -171.92 | buy /  / momentum_26 + volume_26: prior completed bar target 50%; next bar open simulation |
| v1 | breakout_8 AND reversion_12 | 10000.00 | 0.00 | 대기 /  / 새 신호 대기 |
| v1 | breakout_8 + reversion_12 | 9859.02 | -140.98 | sell /  / breakout_8 + reversion_12: prior completed bar target 0%; next bar open simulation |
| v1 | breakout_8 AND volume_26 | 9954.13 | -45.87 | sell /  / breakout_8 AND volume_26: prior completed bar target 0%; next bar open simulation |
| v1 | breakout_8 + volume_26 | 9831.79 | -168.21 | sell /  / breakout_8 + volume_26: prior completed bar target 0%; next bar open simulation |
| v1 | reversion_12 AND volume_26 | 9899.64 | -100.36 | sell /  / reversion_12 AND volume_26: prior completed bar target 0%; next bar open simulation |
| v1 | reversion_12 + volume_26 | 9817.21 | -182.79 | sell /  / reversion_12 + volume_26: prior completed bar target 0%; next bar open simulation |
| v1 | ema_12_26 | 9868.58 | -131.42 | buy /  / EMA12 > EMA26; 조건 충족; EMA12=766.605, EMA26=766.511 |
| v1 | macd_12_26_9 | 9859.93 | -140.07 | sell /  / MACD > 신호선 그리고 MACD > 0; 조건 미충족; MACD=0.314893, signal9=0.346476 |
| v1 | rsi_14_recovery | 9899.32 | -100.68 | sell /  / 직전 RSI14 < 30, 현재 RSI14 >= 30 (한 봉 목표); 조건 미충족; RSI14=34.3611, previous_RSI14=32.906 |
| v1 | bollinger_20_reentry | 9835.17 | -164.83 | sell /  / 직전 종가 < 직전 하단밴드, 현재 하단밴드 <= 종가 <= SMA20 (한 봉 목표); 조건 미충족; close=763.39, lower20=762.854, SMA20=768.639, previous_lower20=763.636 |
| v1 | donchian_20 | 9960.79 | -39.21 | sell /  / 종가 > 현재 봉을 제외한 직전 20봉 최고가; 조건 미충족; close=769.96, prior_high20=770.3 |
| v1 | atr_14_breakout | 9955.14 | -44.86 | sell /  / 종가 > 직전 종가 + 직전 ATR14 그리고 종가 > EMA26; 조건 미충족; close=766.58, threshold=768.736, prior_ATR14=1.82624, EMA26=765.727 |
| v1 | session_vwap | 9806.83 | -193.17 | sell /  / 종가 > 뉴욕 거래일별 누적 전형가격 VWAP; 조건 미충족; close=768.64, session_VWAP=768.839, session_volume=6.99147e+07 |
| v1 | obv_20 | 9909.51 | -90.49 | sell /  / OBV > OBV의 SMA20 그리고 종가 > EMA26; 조건 미충족; OBV=-1.1153e+07, OBV_SMA20=-7.86173e+06, close=768.275, EMA26=767.362 |
| v1 | stochastic_14_3_recovery | 9801.35 | -198.65 | sell /  / 직전 %K14 < 20에서 %K14가 %D3 상향 돌파 (한 봉 목표); 조건 미충족; K14=27.1506, D3=20.2589, previous_K14=23.6558, previous_D3=22.5002 |
| v1 | mfi_14_recovery | 9955.14 | -44.86 | sell /  / 직전 MFI14 < 20, 현재 MFI14 >= 20 (한 봉 목표); 조건 미충족; MFI14=24.4041, previous_MFI14=24.1984 |
| v1 | adx_14_trend | 9981.96 | -18.04 | sell /  / Wilder ADX14 >= 25 그리고 +DI14 > -DI14; 조건 미충족; ADX14=24.2312, plus_DI14=28.3519, minus_DI14=24.6578 |
| v1 | aroon_25_trend | 9861.30 | -138.70 | sell /  / Aroon25 Up > 70 그리고 Down < 30 (동률이면 최신 극값); 조건 미충족; Aroon_up=68, Aroon_down=20 |
| v1 | cci_20_momentum | 9861.55 | -138.45 | sell /  / CCI20 > 100 (전형가격·평균절대편차); 조건 미충족; CCI20=98.503 |
| v1 | williams_14_recovery | 9773.34 | -226.66 | sell /  / 직전 Williams %R14 < -80, 현재 >= -80 (한 봉 목표); 조건 미충족; Williams_R14=-72.8494, previous_R14=-76.3442 |
| v1 | cmf_20_accumulation | 9890.95 | -109.05 | sell /  / Chaikin Money Flow20 > 0.1; 조건 미충족; CMF20=0.0493062, volume20=8.08389e+07 |
| v1 | chaikin_3_10 | 9864.45 | -135.55 | sell /  / ADL의 EMA3 - EMA10 > 0 그리고 종가 > EMA26; 조건 미충족; Chaikin3_10=-974621, ADL=7.60516e+06, close=768.275, EMA26=767.362 |
| v1 | roc_10_momentum | 9953.42 | -46.58 | sell /  / 10봉 ROC > 1% 그리고 종가 > EMA26; 조건 미충족; ROC10_percent=0.806376, close=769.45, EMA26=767.181 |
| v1 | trix_15_trend | 9820.63 | -179.37 | sell /  / 15봉 삼중 EMA의 1봉 변화율 TRIX > 0 그리고 종가 > EMA26; 조건 미충족; TRIX15_percent=0.00690301, close=767.25, EMA26=767.448 |
| v1 | keltner_20_breakout | 10000.00 | 0.00 | 대기 /  / 새 신호 대기 |
| v1 | opening_range_30m | 9846.77 | -153.23 | sell /  / 뉴욕 09:30·09:45 두 완료 봉 최고가를 10:00 이후 종가가 돌파; 조건 미충족; close=767.51, opening_high=768.06 |
| v2 | cash | 10000.00 | 0.00 | 대기 /  / 새 신호 대기 |
| v2 | buy_hold | 9835.01 | -164.99 | buy / partial / 직전 완료 봉 목표 비중 100%; 다음 봉 시가 가정 |
| v2 | trend_8_26 | 9767.67 | -232.33 | buy / partial / 직전 완료 봉 목표 비중 100%; 다음 봉 시가 가정 |
| v2 | momentum_26 | 9720.12 | -279.88 | buy / partial / 직전 완료 봉 목표 비중 100%; 다음 봉 시가 가정 |
| v2 | breakout_8 | 9471.75 | -528.25 | sell / filled / 직전 완료 봉 목표 비중 0%; 다음 봉 시가 가정 |
| v2 | reversion_12 | 9380.06 | -619.94 | sell / filled / 직전 완료 봉 목표 비중 0%; 다음 봉 시가 가정 |
| v2 | volume_26 | 9235.92 | -764.08 | sell / filled / 직전 완료 봉 목표 비중 0%; 다음 봉 시가 가정 |
| v2 | trend_8_26 AND momentum_26 | 9726.75 | -273.25 | buy / partial / 직전 완료 봉 목표 비중 100%; 다음 봉 시가 가정 |
| v2 | trend_8_26 + momentum_26 | 9743.87 | -256.13 | buy / partial / 직전 완료 봉 목표 비중 100%; 다음 봉 시가 가정 |
| v2 | trend_8_26 AND breakout_8 | 9794.09 | -205.91 | sell / filled / 직전 완료 봉 목표 비중 0%; 다음 봉 시가 가정 |
| v2 | trend_8_26 + breakout_8 | 9638.58 | -361.42 | buy / filled / 직전 완료 봉 목표 비중 50%; 다음 봉 시가 가정 |
| v2 | trend_8_26 AND reversion_12 | 9801.35 | -198.65 | sell / filled / 직전 완료 봉 목표 비중 0%; 다음 봉 시가 가정 |
| v2 | trend_8_26 + reversion_12 | 9571.49 | -428.51 | buy / filled / 직전 완료 봉 목표 비중 50%; 다음 봉 시가 가정 |
| v2 | trend_8_26 AND volume_26 | 9678.83 | -321.17 | sell / filled / 직전 완료 봉 목표 비중 0%; 다음 봉 시가 가정 |
| v2 | trend_8_26 + volume_26 | 9517.75 | -482.25 | buy / filled / 직전 완료 봉 목표 비중 50%; 다음 봉 시가 가정 |
| v2 | momentum_26 AND breakout_8 | 9736.71 | -263.29 | sell / filled / 직전 완료 봉 목표 비중 0%; 다음 봉 시가 가정 |
| v2 | momentum_26 + breakout_8 | 9595.01 | -404.99 | buy / filled / 직전 완료 봉 목표 비중 50%; 다음 봉 시가 가정 |
| v2 | momentum_26 AND reversion_12 | 9923.13 | -76.87 | sell / filled / 직전 완료 봉 목표 비중 0%; 다음 봉 시가 가정 |
| v2 | momentum_26 + reversion_12 | 9588.36 | -411.64 | buy / filled / 직전 완료 봉 목표 비중 50%; 다음 봉 시가 가정 |
| v2 | momentum_26 AND volume_26 | 9762.54 | -237.46 | sell / filled / 직전 완료 봉 목표 비중 0%; 다음 봉 시가 가정 |
| v2 | momentum_26 + volume_26 | 9534.51 | -465.49 | buy / filled / 직전 완료 봉 목표 비중 50%; 다음 봉 시가 가정 |
| v2 | breakout_8 AND reversion_12 | 10000.00 | 0.00 | 대기 /  / 새 신호 대기 |
| v2 | breakout_8 + reversion_12 | 9464.93 | -535.07 | sell / filled / 직전 완료 봉 목표 비중 0%; 다음 봉 시가 가정 |
| v2 | breakout_8 AND volume_26 | 9885.63 | -114.37 | sell / filled / 직전 완료 봉 목표 비중 0%; 다음 봉 시가 가정 |
| v2 | breakout_8 + volume_26 | 9392.04 | -607.96 | sell / filled / 직전 완료 봉 목표 비중 0%; 다음 봉 시가 가정 |
| v2 | reversion_12 AND volume_26 | 9641.69 | -358.31 | sell / filled / 직전 완료 봉 목표 비중 0%; 다음 봉 시가 가정 |
| v2 | reversion_12 + volume_26 | 9385.88 | -614.12 | sell / filled / 직전 완료 봉 목표 비중 0%; 다음 봉 시가 가정 |
| v2 | ema_12_26 | 9865.62 | -134.38 | buy / partial / EMA12 > EMA26; 조건 충족; EMA12=766.605, EMA26=766.511; 직전 완료 봉 목표를 다음 봉 시가에 모의 적용 |
| v2 | macd_12_26_9 | 9855.99 | -144.01 | sell / filled / MACD > 신호선 그리고 MACD > 0; 조건 미충족; MACD=0.314893, signal9=0.346476; 직전 완료 봉 목표를 다음 봉 시가에 모의 적용 |
| v2 | rsi_14_recovery | 9895.36 | -104.64 | sell / filled / 직전 RSI14 < 30, 현재 RSI14 >= 30 (한 봉 목표); 조건 미충족; RSI14=34.3611, previous_RSI14=32.906; 직전 완료 봉 목표를 다음 봉 시가에 모의 적용 |
| v2 | bollinger_20_reentry | 9829.27 | -170.73 | sell / filled / 직전 종가 < 직전 하단밴드, 현재 하단밴드 <= 종가 <= SMA20 (한 봉 목표); 조건 미충족; close=763.39, lower20=762.854, SMA20=768.639, previous_lower20=763.636; 직전 완료 봉 목표를 다음 봉 시가에 모의 적용 |
| v2 | donchian_20 | 9958.80 | -41.20 | sell / filled / 종가 > 현재 봉을 제외한 직전 20봉 최고가; 조건 미충족; close=769.96, prior_high20=770.3; 직전 완료 봉 목표를 다음 봉 시가에 모의 적용 |
| v2 | atr_14_breakout | 9953.15 | -46.85 | sell / filled / 종가 > 직전 종가 + 직전 ATR14 그리고 종가 > EMA26; 조건 미충족; close=766.58, threshold=768.736, prior_ATR14=1.82624, EMA26=765.727; 직전 완료 봉 목표를 다음 봉 시가에 모의 적용 |
| v2 | session_vwap | 9798.99 | -201.01 | sell / filled / 종가 > 뉴욕 거래일별 누적 전형가격 VWAP; 조건 미충족; close=768.64, session_VWAP=768.839, session_volume=6.99147e+07; 직전 완료 봉 목표를 다음 봉 시가에 모의 적용 |
| v2 | obv_20 | 9905.54 | -94.46 | sell / filled / OBV > OBV의 SMA20 그리고 종가 > EMA26; 조건 미충족; OBV=-1.1153e+07, OBV_SMA20=-7.86173e+06, close=768.275, EMA26=767.362; 직전 완료 봉 목표를 다음 봉 시가에 모의 적용 |
| v2 | stochastic_14_3_recovery | 9791.56 | -208.44 | sell / filled / 직전 %K14 < 20에서 %K14가 %D3 상향 돌파 (한 봉 목표); 조건 미충족; K14=27.1506, D3=20.2589, previous_K14=23.6558, previous_D3=22.5002; 직전 완료 봉 목표를 다음 봉 시가에 모의 적용 |
| v2 | mfi_14_recovery | 9953.15 | -46.85 | sell / filled / 직전 MFI14 < 20, 현재 MFI14 >= 20 (한 봉 목표); 조건 미충족; MFI14=24.4041, previous_MFI14=24.1984; 직전 완료 봉 목표를 다음 봉 시가에 모의 적용 |
| v2 | adx_14_trend | 9979.97 | -20.03 | sell / filled / Wilder ADX14 >= 25 그리고 +DI14 > -DI14; 조건 미충족; ADX14=24.2312, plus_DI14=28.3519, minus_DI14=24.6578; 직전 완료 봉 목표를 다음 봉 시가에 모의 적용 |
| v2 | aroon_25_trend | 9857.36 | -142.64 | sell / filled / Aroon25 Up > 70 그리고 Down < 30 (동률이면 최신 극값); 조건 미충족; Aroon_up=68, Aroon_down=20; 직전 완료 봉 목표를 다음 봉 시가에 모의 적용 |
| v2 | cci_20_momentum | 9855.63 | -144.37 | sell / filled / CCI20 > 100 (전형가격·평균절대편차); 조건 미충족; CCI20=98.503; 직전 완료 봉 목표를 다음 봉 시가에 모의 적용 |
| v2 | williams_14_recovery | 9763.57 | -236.43 | sell / filled / 직전 Williams %R14 < -80, 현재 >= -80 (한 봉 목표); 조건 미충족; Williams_R14=-72.8494, previous_R14=-76.3442; 직전 완료 봉 목표를 다음 봉 시가에 모의 적용 |
| v2 | cmf_20_accumulation | 9887.00 | -113.00 | sell / filled / Chaikin Money Flow20 > 0.1; 조건 미충족; CMF20=0.0493062, volume20=8.08389e+07; 직전 완료 봉 목표를 다음 봉 시가에 모의 적용 |
| v2 | chaikin_3_10 | 9858.53 | -141.47 | sell / filled / ADL의 EMA3 - EMA10 > 0 그리고 종가 > EMA26; 조건 미충족; Chaikin3_10=-974621, ADL=7.60516e+06, close=768.275, EMA26=767.362; 직전 완료 봉 목표를 다음 봉 시가에 모의 적용 |
| v2 | roc_10_momentum | 9951.43 | -48.57 | sell / filled / 10봉 ROC > 1% 그리고 종가 > EMA26; 조건 미충족; ROC10_percent=0.806376, close=769.45, EMA26=767.181; 직전 완료 봉 목표를 다음 봉 시가에 모의 적용 |
| v2 | trix_15_trend | 9814.74 | -185.26 | sell / filled / 15봉 삼중 EMA의 1봉 변화율 TRIX > 0 그리고 종가 > EMA26; 조건 미충족; TRIX15_percent=0.00690301, close=767.25, EMA26=767.448; 직전 완료 봉 목표를 다음 봉 시가에 모의 적용 |
| v2 | keltner_20_breakout | 10000.00 | 0.00 | 대기 /  / 새 신호 대기 |
| v2 | opening_range_30m | 9840.86 | -159.14 | sell / filled / 뉴욕 09:30·09:45 두 완료 봉 최고가를 10:00 이후 종가가 돌파; 조건 미충족; close=767.51, opening_high=768.06; 직전 완료 봉 목표를 다음 봉 시가에 모의 적용 |

### 같은 기간의 비용·노출 비교 (사후 연구)

| 전략 | 비용 전 | 비용 후 | 100% 보유 | 같은 평균 노출 보유 | 평균 노출 |
|---|---:|---:|---:|---:|---:|
| cash | 0.00% | 0.00% | -0.11% | -0.00% | 0.00% |
| buy_hold | 0.31% | -0.11% | -0.11% | -0.11% | 100.00% |
| trend_8_26 | 1.47% | -1.89% | -0.11% | -0.06% | 50.52% |
| momentum_26 | -0.46% | -4.55% | -0.11% | -0.05% | 48.95% |
| breakout_8 | -0.22% | -15.65% | -0.11% | -0.02% | 22.25% |
| reversion_12 | -1.55% | -12.84% | -0.11% | -0.03% | 28.80% |
| volume_26 | -1.02% | -10.13% | -0.11% | -0.01% | 8.90% |
| trend_8_26 AND momentum_26 | 0.61% | -3.12% | -0.11% | -0.05% | 43.19% |
| trend_8_26 + momentum_26 | 0.50% | -3.23% | -0.11% | -0.05% | 49.74% |
| trend_8_26 AND breakout_8 | 0.17% | -10.57% | -0.11% | -0.01% | 13.09% |
| trend_8_26 + breakout_8 | 0.62% | -8.84% | -0.11% | -0.04% | 36.39% |
| trend_8_26 AND reversion_12 | -0.14% | -3.84% | -0.11% | -0.01% | 6.54% |
| trend_8_26 + reversion_12 | -0.05% | -7.34% | -0.11% | -0.04% | 39.66% |
| trend_8_26 AND volume_26 | -0.68% | -5.16% | -0.11% | -0.01% | 4.71% |
| trend_8_26 + volume_26 | 0.22% | -6.11% | -0.11% | -0.03% | 29.72% |
| momentum_26 AND breakout_8 | 0.31% | -10.44% | -0.11% | -0.02% | 13.87% |
| momentum_26 + breakout_8 | -0.34% | -10.27% | -0.11% | -0.04% | 35.61% |
| momentum_26 AND reversion_12 | -0.76% | -4.85% | -0.11% | -0.01% | 6.81% |
| momentum_26 + reversion_12 | -1.00% | -8.22% | -0.11% | -0.04% | 38.88% |
| momentum_26 AND volume_26 | -0.40% | -3.69% | -0.11% | -0.00% | 2.88% |
| momentum_26 + volume_26 | -0.74% | -6.22% | -0.11% | -0.03% | 28.93% |
| breakout_8 AND reversion_12 | 0.00% | 0.00% | -0.11% | -0.00% | 0.00% |
| breakout_8 + reversion_12 | -0.89% | -13.73% | -0.11% | -0.03% | 25.53% |
| breakout_8 AND volume_26 | 0.03% | -1.64% | -0.11% | -0.00% | 1.57% |
| breakout_8 + volume_26 | -0.62% | -12.03% | -0.11% | -0.02% | 15.58% |
| reversion_12 AND volume_26 | -0.88% | -4.95% | -0.11% | -0.00% | 3.66% |
| reversion_12 + volume_26 | -1.28% | -11.13% | -0.11% | -0.02% | 18.85% |
| ema_12_26 | -0.31% | -3.60% | -0.11% | -0.06% | 50.79% |
| macd_12_26_9 | 0.30% | -4.23% | -0.11% | -0.03% | 31.41% |
| rsi_14_recovery | -0.53% | -4.22% | -0.11% | -0.00% | 2.36% |
| bollinger_20_reentry | -1.13% | -7.17% | -0.11% | -0.00% | 3.93% |
| donchian_20 | 0.11% | -7.17% | -0.11% | -0.01% | 6.81% |
| atr_14_breakout | 0.38% | -4.55% | -0.11% | -0.00% | 3.66% |
| session_vwap | 2.10% | -7.69% | -0.11% | -0.05% | 47.91% |
| obv_20 | 0.26% | -7.43% | -0.11% | -0.04% | 38.74% |
| stochastic_14_3_recovery | -0.88% | -15.85% | -0.11% | -0.01% | 10.21% |
| mfi_14_recovery | -0.01% | -2.50% | -0.11% | -0.00% | 1.57% |
| adx_14_trend | 0.32% | -3.40% | -0.11% | -0.03% | 28.01% |
| aroon_25_trend | 0.82% | -2.10% | -0.11% | -0.03% | 25.65% |
| cci_20_momentum | -0.04% | -8.10% | -0.11% | -0.02% | 21.99% |
| williams_14_recovery | -0.80% | -11.43% | -0.11% | -0.01% | 7.07% |
| cmf_20_accumulation | 2.29% | -1.50% | -0.11% | -0.05% | 45.29% |
| chaikin_3_10 | 1.85% | -4.77% | -0.11% | -0.04% | 40.05% |
| roc_10_momentum | -0.13% | -0.97% | -0.11% | -0.00% | 1.05% |
| trix_15_trend | -0.28% | -3.57% | -0.11% | -0.04% | 37.17% |
| keltner_20_breakout | 0.09% | -3.62% | -0.11% | -0.01% | 10.73% |
| opening_range_30m | 0.36% | -5.37% | -0.11% | -0.03% | 31.68% |

동일 구간·초기 자금, 종료 시 청산 비용 포함. 노출 맞춤은 사후 설명용이며 v2 실제 계좌 성과가 아닙니다.
[낙폭 분해·비용 영향·전체 구간](SPY/comparison.json)

[v1 전체 기록](SPY/accounts.json) · [v2 전체 기록](SPY/accounts-v2.json)

## QQQ 계좌

| 모델 | 전략 | 평가액 USD | 손익 USD | 최근 매매·이유 |
|---|---|---:|---:|---|
| v1 | cash | 10000.00 | 0.00 | 대기 /  / 새 신호 대기 |
| v1 | buy_hold | 9894.31 | -105.69 | buy /  / buy_hold: prior completed bar target 100%; next bar open simulation |
| v1 | trend_8_26 | 9887.10 | -112.90 | buy /  / trend_8_26: prior completed bar target 100%; next bar open simulation |
| v1 | momentum_26 | 9829.56 | -170.44 | buy /  / momentum_26: prior completed bar target 100%; next bar open simulation |
| v1 | breakout_8 | 9897.90 | -102.10 | sell /  / breakout_8: prior completed bar target 0%; next bar open simulation |
| v1 | reversion_12 | 9859.88 | -140.12 | buy /  / reversion_12: prior completed bar target 100%; next bar open simulation |
| v1 | volume_26 | 9763.59 | -236.41 | sell /  / volume_26: prior completed bar target 0%; next bar open simulation |
| v1 | trend_8_26 AND momentum_26 | 9895.62 | -104.38 | buy /  / trend_8_26 AND momentum_26: prior completed bar target 100%; next bar open simulation |
| v1 | trend_8_26 + momentum_26 | 9878.00 | -122.00 | buy /  / trend_8_26 + momentum_26: prior completed bar target 100%; next bar open simulation |
| v1 | trend_8_26 AND breakout_8 | 9989.91 | -10.09 | sell /  / trend_8_26 AND breakout_8: prior completed bar target 0%; next bar open simulation |
| v1 | trend_8_26 + breakout_8 | 9912.21 | -87.79 | buy /  / trend_8_26 + breakout_8: prior completed bar target 50%; next bar open simulation |
| v1 | trend_8_26 AND reversion_12 | 9922.26 | -77.74 | buy /  / trend_8_26 AND reversion_12: prior completed bar target 100%; next bar open simulation |
| v1 | trend_8_26 + reversion_12 | 9873.62 | -126.38 | buy /  / trend_8_26 + reversion_12: prior completed bar target 100%; next bar open simulation |
| v1 | trend_8_26 AND volume_26 | 9932.72 | -67.28 | sell /  / trend_8_26 AND volume_26: prior completed bar target 0%; next bar open simulation |
| v1 | trend_8_26 + volume_26 | 9825.08 | -174.92 | buy /  / trend_8_26 + volume_26: prior completed bar target 50%; next bar open simulation |
| v1 | momentum_26 AND breakout_8 | 9929.95 | -70.05 | sell /  / momentum_26 AND breakout_8: prior completed bar target 0%; next bar open simulation |
| v1 | momentum_26 + breakout_8 | 9863.64 | -136.36 | buy /  / momentum_26 + breakout_8: prior completed bar target 50%; next bar open simulation |
| v1 | momentum_26 AND reversion_12 | 9922.26 | -77.74 | buy /  / momentum_26 AND reversion_12: prior completed bar target 100%; next bar open simulation |
| v1 | momentum_26 + reversion_12 | 9844.87 | -155.13 | buy /  / momentum_26 + reversion_12: prior completed bar target 100%; next bar open simulation |
| v1 | momentum_26 AND volume_26 | 9912.22 | -87.78 | sell /  / momentum_26 AND volume_26: prior completed bar target 0%; next bar open simulation |
| v1 | momentum_26 + volume_26 | 9816.06 | -183.94 | buy /  / momentum_26 + volume_26: prior completed bar target 50%; next bar open simulation |
| v1 | breakout_8 AND reversion_12 | 10000.00 | 0.00 | 대기 /  / 새 신호 대기 |
| v1 | breakout_8 + reversion_12 | 9878.96 | -121.04 | buy /  / breakout_8 + reversion_12: prior completed bar target 50%; next bar open simulation |
| v1 | breakout_8 AND volume_26 | 9947.15 | -52.85 | sell /  / breakout_8 AND volume_26: prior completed bar target 0%; next bar open simulation |
| v1 | breakout_8 + volume_26 | 9850.15 | -149.85 | sell /  / breakout_8 + volume_26: prior completed bar target 0%; next bar open simulation |
| v1 | reversion_12 AND volume_26 | 9907.31 | -92.69 | sell /  / reversion_12 AND volume_26: prior completed bar target 0%; next bar open simulation |
| v1 | reversion_12 + volume_26 | 9851.00 | -149.00 | buy /  / reversion_12 + volume_26: prior completed bar target 50%; next bar open simulation |
| v1 | ema_12_26 | 9884.88 | -115.12 | buy /  / EMA12 > EMA26; 조건 충족; EMA12=717, EMA26=716.746 |
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
| v1 | williams_14_recovery | 9750.71 | -249.29 | sell /  / 직전 Williams %R14 < -80, 현재 >= -80 (한 봉 목표); 조건 미충족; Williams_R14=-82.7972, previous_R14=-79.0998 |
| v1 | cmf_20_accumulation | 9709.61 | -290.39 | sell /  / Chaikin Money Flow20 > 0.1; 조건 미충족; CMF20=0.0836393, volume20=5.30174e+08 |
| v1 | chaikin_3_10 | 9899.84 | -100.16 | sell /  / ADL의 EMA3 - EMA10 > 0 그리고 종가 > EMA26; 조건 미충족; Chaikin3_10=-495746, ADL=2.16147e+08, close=719.63, EMA26=719.312 |
| v1 | roc_10_momentum | 9990.50 | -9.50 | sell /  / 10봉 ROC > 1% 그리고 종가 > EMA26; 조건 미충족; ROC10_percent=0.483561, close=722.477, EMA26=718.78 |
| v1 | trix_15_trend | 9893.71 | -106.29 | sell /  / 15봉 삼중 EMA의 1봉 변화율 TRIX > 0 그리고 종가 > EMA26; 조건 미충족; TRIX15_percent=0.0209731, close=718.545, EMA26=719.286 |
| v1 | keltner_20_breakout | 9904.16 | -95.84 | sell /  / 종가 > EMA20 + 2 x Wilder ATR14; 조건 미충족; close=723.31, upper_Keltner=723.407, EMA20=718.722, ATR14=2.34265 |
| v1 | opening_range_30m | 9887.22 | -112.78 | sell /  / 뉴욕 09:30·09:45 두 완료 봉 최고가를 10:00 이후 종가가 돌파; 조건 미충족; close=719.99, opening_high=720.22 |
| v2 | cash | 10000.00 | 0.00 | 대기 /  / 새 신호 대기 |
| v2 | buy_hold | 9574.49 | -425.51 | buy / partial / 직전 완료 봉 목표 비중 100%; 다음 봉 시가 가정 |
| v2 | trend_8_26 | 9690.10 | -309.90 | buy / partial / 직전 완료 봉 목표 비중 100%; 다음 봉 시가 가정 |
| v2 | momentum_26 | 9724.21 | -275.79 | buy / partial / 직전 완료 봉 목표 비중 100%; 다음 봉 시가 가정 |
| v2 | breakout_8 | 9565.39 | -434.61 | sell / filled / 직전 완료 봉 목표 비중 0%; 다음 봉 시가 가정 |
| v2 | reversion_12 | 9374.05 | -625.95 | buy / partial / 직전 완료 봉 목표 비중 100%; 다음 봉 시가 가정 |
| v2 | volume_26 | 9565.80 | -434.20 | 중단: 손실 한도 / sell / filled / 직전 완료 봉 목표 비중 0%; 다음 봉 시가 가정 |
| v2 | trend_8_26 AND momentum_26 | 9791.52 | -208.48 | buy / partial / 직전 완료 봉 목표 비중 100%; 다음 봉 시가 가정 |
| v2 | trend_8_26 + momentum_26 | 9727.56 | -272.44 | buy / partial / 직전 완료 봉 목표 비중 100%; 다음 봉 시가 가정 |
| v2 | trend_8_26 AND breakout_8 | 9883.87 | -116.13 | sell / filled / 직전 완료 봉 목표 비중 0%; 다음 봉 시가 가정 |
| v2 | trend_8_26 + breakout_8 | 9647.66 | -352.34 | buy / filled / 직전 완료 봉 목표 비중 50%; 다음 봉 시가 가정 |
| v2 | trend_8_26 AND reversion_12 | 9781.55 | -218.45 | buy / partial / 직전 완료 봉 목표 비중 100%; 다음 봉 시가 가정 |
| v2 | trend_8_26 + reversion_12 | 9530.60 | -469.40 | buy / partial / 직전 완료 봉 목표 비중 100%; 다음 봉 시가 가정 |
| v2 | trend_8_26 AND volume_26 | 9769.99 | -230.01 | sell / filled / 직전 완료 봉 목표 비중 0%; 다음 봉 시가 가정 |
| v2 | trend_8_26 + volume_26 | 9429.00 | -571.00 | buy / filled / 직전 완료 봉 목표 비중 50%; 다음 봉 시가 가정 |
| v2 | momentum_26 AND breakout_8 | 9886.96 | -113.04 | sell / filled / 직전 완료 봉 목표 비중 0%; 다음 봉 시가 가정 |
| v2 | momentum_26 + breakout_8 | 9644.40 | -355.60 | buy / filled / 직전 완료 봉 목표 비중 50%; 다음 봉 시가 가정 |
| v2 | momentum_26 AND reversion_12 | 9919.29 | -80.71 | buy / partial / 직전 완료 봉 목표 비중 100%; 다음 봉 시가 가정 |
| v2 | momentum_26 + reversion_12 | 9567.42 | -432.58 | buy / partial / 직전 완료 봉 목표 비중 100%; 다음 봉 시가 가정 |
| v2 | momentum_26 AND volume_26 | 9845.67 | -154.33 | sell / filled / 직전 완료 봉 목표 비중 0%; 다음 봉 시가 가정 |
| v2 | momentum_26 + volume_26 | 9465.43 | -534.57 | buy / filled / 직전 완료 봉 목표 비중 50%; 다음 봉 시가 가정 |
| v2 | breakout_8 AND reversion_12 | 10000.00 | 0.00 | 대기 /  / 새 신호 대기 |
| v2 | breakout_8 + reversion_12 | 9528.86 | -471.14 | buy / filled / 직전 완료 봉 목표 비중 50%; 다음 봉 시가 가정 |
| v2 | breakout_8 AND volume_26 | 9891.45 | -108.55 | sell / filled / 직전 완료 봉 목표 비중 0%; 다음 봉 시가 가정 |
| v2 | breakout_8 + volume_26 | 9427.43 | -572.57 | sell / filled / 직전 완료 봉 목표 비중 0%; 다음 봉 시가 가정 |
| v2 | reversion_12 AND volume_26 | 9547.64 | -452.36 | 중단: 손실 한도 / sell / filled / 직전 완료 봉 목표 비중 0%; 다음 봉 시가 가정 |
| v2 | reversion_12 + volume_26 | 9332.85 | -667.15 | buy / filled / 직전 완료 봉 목표 비중 50%; 다음 봉 시가 가정 |
| v2 | ema_12_26 | 9881.91 | -118.09 | buy / partial / EMA12 > EMA26; 조건 충족; EMA12=717, EMA26=716.746; 직전 완료 봉 목표를 다음 봉 시가에 모의 적용 |
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
| v2 | williams_14_recovery | 9740.96 | -259.04 | sell / filled / 직전 Williams %R14 < -80, 현재 >= -80 (한 봉 목표); 조건 미충족; Williams_R14=-82.7972, previous_R14=-79.0998; 직전 완료 봉 목표를 다음 봉 시가에 모의 적용 |
| v2 | cmf_20_accumulation | 9699.90 | -300.10 | sell / filled / Chaikin Money Flow20 > 0.1; 조건 미충족; CMF20=0.0836393, volume20=5.30174e+08; 직전 완료 봉 목표를 다음 봉 시가에 모의 적용 |
| v2 | chaikin_3_10 | 9895.89 | -104.11 | sell / filled / ADL의 EMA3 - EMA10 > 0 그리고 종가 > EMA26; 조건 미충족; Chaikin3_10=-495746, ADL=2.16147e+08, close=719.63, EMA26=719.312; 직전 완료 봉 목표를 다음 봉 시가에 모의 적용 |
| v2 | roc_10_momentum | 9988.50 | -11.50 | sell / filled / 10봉 ROC > 1% 그리고 종가 > EMA26; 조건 미충족; ROC10_percent=0.483561, close=722.477, EMA26=718.78; 직전 완료 봉 목표를 다음 봉 시가에 모의 적용 |
| v2 | trix_15_trend | 9891.73 | -108.27 | sell / filled / 15봉 삼중 EMA의 1봉 변화율 TRIX > 0 그리고 종가 > EMA26; 조건 미충족; TRIX15_percent=0.0209731, close=718.545, EMA26=719.286; 직전 완료 봉 목표를 다음 봉 시가에 모의 적용 |
| v2 | keltner_20_breakout | 9900.20 | -99.80 | sell / filled / 종가 > EMA20 + 2 x Wilder ATR14; 조건 미충족; close=723.31, upper_Keltner=723.407, EMA20=718.722, ATR14=2.34265; 직전 완료 봉 목표를 다음 봉 시가에 모의 적용 |
| v2 | opening_range_30m | 9883.27 | -116.73 | sell / filled / 뉴욕 09:30·09:45 두 완료 봉 최고가를 10:00 이후 종가가 돌파; 조건 미충족; close=719.99, opening_high=720.22; 직전 완료 봉 목표를 다음 봉 시가에 모의 적용 |

### 같은 기간의 비용·노출 비교 (사후 연구)

| 전략 | 비용 전 | 비용 후 | 100% 보유 | 같은 평균 노출 보유 | 평균 노출 |
|---|---:|---:|---:|---:|---:|
| cash | 0.00% | 0.00% | -2.98% | -0.00% | 0.00% |
| buy_hold | -2.57% | -2.98% | -2.98% | -2.98% | 100.00% |
| trend_8_26 | 0.38% | -3.35% | -2.98% | -1.37% | 46.07% |
| momentum_26 | -1.22% | -6.47% | -2.98% | -1.23% | 41.36% |
| breakout_8 | -0.79% | -16.13% | -2.98% | -0.56% | 18.85% |
| reversion_12 | -0.38% | -12.91% | -2.98% | -0.89% | 29.84% |
| volume_26 | -1.06% | -14.23% | -2.98% | -0.47% | 15.71% |
| trend_8_26 AND momentum_26 | 0.01% | -4.10% | -2.98% | -1.08% | 36.39% |
| trend_8_26 + momentum_26 | -0.42% | -4.52% | -2.98% | -1.30% | 43.72% |
| trend_8_26 AND breakout_8 | -0.02% | -9.22% | -2.98% | -0.34% | 11.52% |
| trend_8_26 + breakout_8 | -0.20% | -9.40% | -2.98% | -0.97% | 32.47% |
| trend_8_26 AND reversion_12 | -0.08% | -5.39% | -2.98% | -0.21% | 7.07% |
| trend_8_26 + reversion_12 | 0.01% | -7.87% | -2.98% | -1.13% | 37.96% |
| trend_8_26 AND volume_26 | 0.21% | -4.71% | -2.98% | -0.16% | 5.24% |
| trend_8_26 + volume_26 | -0.34% | -8.76% | -2.98% | -0.92% | 30.90% |
| momentum_26 AND breakout_8 | -0.03% | -9.24% | -2.98% | -0.33% | 11.26% |
| momentum_26 + breakout_8 | -1.00% | -11.25% | -2.98% | -0.90% | 30.11% |
| momentum_26 AND reversion_12 | -0.39% | -6.08% | -2.98% | -0.21% | 7.07% |
| momentum_26 + reversion_12 | -0.79% | -9.37% | -2.98% | -1.06% | 35.61% |
| momentum_26 AND volume_26 | -0.04% | -4.56% | -2.98% | -0.12% | 4.19% |
| momentum_26 + volume_26 | -1.14% | -10.06% | -2.98% | -0.85% | 28.54% |
| breakout_8 AND reversion_12 | 0.00% | 0.00% | -2.98% | -0.00% | 0.00% |
| breakout_8 + reversion_12 | -0.58% | -13.64% | -2.98% | -0.72% | 24.35% |
| breakout_8 AND volume_26 | 0.31% | -2.60% | -2.98% | -0.06% | 2.09% |
| breakout_8 + volume_26 | -0.92% | -13.76% | -2.98% | -0.51% | 17.29% |
| reversion_12 AND volume_26 | -1.31% | -8.11% | -2.98% | -0.25% | 8.38% |
| reversion_12 + volume_26 | -0.71% | -12.84% | -2.98% | -0.68% | 22.78% |
| ema_12_26 | 0.67% | -1.42% | -2.98% | -1.15% | 38.74% |
| macd_12_26_9 | 1.23% | -2.52% | -2.98% | -0.69% | 23.04% |
| rsi_14_recovery | -0.83% | -5.71% | -2.98% | -0.09% | 3.14% |
| bollinger_20_reentry | -0.44% | -6.12% | -2.98% | -0.11% | 3.66% |
| donchian_20 | 0.59% | -4.75% | -2.98% | -0.17% | 5.76% |
| atr_14_breakout | 0.11% | -4.01% | -2.98% | -0.09% | 2.88% |
| session_vwap | -0.52% | -11.93% | -2.98% | -1.43% | 47.91% |
| obv_20 | -0.80% | -9.18% | -2.98% | -0.90% | 30.37% |
| stochastic_14_3_recovery | -0.85% | -12.59% | -2.98% | -0.23% | 7.85% |
| mfi_14_recovery | -0.49% | -2.56% | -2.98% | -0.04% | 1.31% |
| adx_14_trend | -0.11% | -3.00% | -2.98% | -0.64% | 21.47% |
| aroon_25_trend | 1.11% | -2.64% | -2.98% | -0.58% | 19.63% |
| cci_20_momentum | -0.25% | -5.55% | -2.98% | -0.51% | 17.28% |
| williams_14_recovery | -1.13% | -12.10% | -2.98% | -0.22% | 7.33% |
| cmf_20_accumulation | -1.35% | -8.92% | -2.98% | -0.90% | 30.37% |
| chaikin_3_10 | -1.93% | -9.45% | -2.98% | -1.10% | 36.91% |
| roc_10_momentum | -0.00% | -1.67% | -2.98% | -0.12% | 4.19% |
| trix_15_trend | 0.26% | -1.41% | -2.98% | -0.94% | 31.68% |
| keltner_20_breakout | -0.89% | -5.76% | -2.98% | -0.24% | 8.12% |
| opening_range_30m | -0.39% | -6.47% | -2.98% | -0.73% | 24.61% |

동일 구간·초기 자금, 종료 시 청산 비용 포함. 노출 맞춤은 사후 설명용이며 v2 실제 계좌 성과가 아닙니다.
[낙폭 분해·비용 영향·전체 구간](QQQ/comparison.json)

[v1 전체 기록](QQQ/accounts.json) · [v2 전체 기록](QQQ/accounts-v2.json)

## IWM 계좌

| 모델 | 전략 | 평가액 USD | 손익 USD | 최근 매매·이유 |
|---|---|---:|---:|---|
| v1 | cash | 10000.00 | 0.00 | 대기 /  / 새 신호 대기 |
| v1 | buy_hold | 9820.65 | -179.35 | buy /  / buy_hold: prior completed bar target 100%; next bar open simulation |
| v1 | trend_8_26 | 9781.45 | -218.55 | buy /  / trend_8_26: prior completed bar target 100%; next bar open simulation |
| v1 | momentum_26 | 9797.34 | -202.66 | buy /  / momentum_26: prior completed bar target 100%; next bar open simulation |
| v1 | breakout_8 | 9788.68 | -211.32 | sell /  / breakout_8: prior completed bar target 0%; next bar open simulation |
| v1 | reversion_12 | 9805.86 | -194.14 | buy /  / reversion_12: prior completed bar target 100%; next bar open simulation |
| v1 | volume_26 | 9862.10 | -137.90 | sell /  / volume_26: prior completed bar target 0%; next bar open simulation |
| v1 | trend_8_26 AND momentum_26 | 9797.34 | -202.66 | buy /  / trend_8_26 AND momentum_26: prior completed bar target 100%; next bar open simulation |
| v1 | trend_8_26 + momentum_26 | 9789.39 | -210.61 | buy /  / trend_8_26 + momentum_26: prior completed bar target 100%; next bar open simulation |
| v1 | trend_8_26 AND breakout_8 | 9896.83 | -103.17 | sell /  / trend_8_26 AND breakout_8: prior completed bar target 0%; next bar open simulation |
| v1 | trend_8_26 + breakout_8 | 9785.03 | -214.97 | buy /  / trend_8_26 + breakout_8: prior completed bar target 50%; next bar open simulation |
| v1 | trend_8_26 AND reversion_12 | 9846.63 | -153.37 | buy /  / trend_8_26 AND reversion_12: prior completed bar target 100%; next bar open simulation |
| v1 | trend_8_26 + reversion_12 | 9793.58 | -206.42 | buy /  / trend_8_26 + reversion_12: prior completed bar target 100%; next bar open simulation |
| v1 | trend_8_26 AND volume_26 | 9935.98 | -64.02 | sell /  / trend_8_26 AND volume_26: prior completed bar target 0%; next bar open simulation |
| v1 | trend_8_26 + volume_26 | 9821.58 | -178.42 | buy /  / trend_8_26 + volume_26: prior completed bar target 50%; next bar open simulation |
| v1 | momentum_26 AND breakout_8 | 9929.38 | -70.62 | sell /  / momentum_26 AND breakout_8: prior completed bar target 0%; next bar open simulation |
| v1 | momentum_26 + breakout_8 | 9812.57 | -187.43 | buy /  / momentum_26 + breakout_8: prior completed bar target 50%; next bar open simulation |
| v1 | momentum_26 AND reversion_12 | 9943.85 | -56.15 | buy /  / momentum_26 AND reversion_12: prior completed bar target 100%; next bar open simulation |
| v1 | momentum_26 + reversion_12 | 9821.14 | -178.86 | buy /  / momentum_26 + reversion_12: prior completed bar target 100%; next bar open simulation |
| v1 | momentum_26 AND volume_26 | 10000.00 | 0.00 | 대기 /  / 새 신호 대기 |
| v1 | momentum_26 + volume_26 | 9829.58 | -170.42 | buy /  / momentum_26 + volume_26: prior completed bar target 50%; next bar open simulation |
| v1 | breakout_8 AND reversion_12 | 10000.00 | 0.00 | 대기 /  / 새 신호 대기 |
| v1 | breakout_8 + reversion_12 | 9797.14 | -202.86 | buy /  / breakout_8 + reversion_12: prior completed bar target 50%; next bar open simulation |
| v1 | breakout_8 AND volume_26 | 9944.66 | -55.34 | sell /  / breakout_8 AND volume_26: prior completed bar target 0%; next bar open simulation |
| v1 | breakout_8 + volume_26 | 9825.26 | -174.74 | sell /  / breakout_8 + volume_26: prior completed bar target 0%; next bar open simulation |
| v1 | reversion_12 AND volume_26 | 9935.98 | -64.02 | sell /  / reversion_12 AND volume_26: prior completed bar target 0%; next bar open simulation |
| v1 | reversion_12 + volume_26 | 9853.55 | -146.45 | buy /  / reversion_12 + volume_26: prior completed bar target 50%; next bar open simulation |
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
| v2 | buy_hold | 9715.64 | -284.36 | buy / partial / 직전 완료 봉 목표 비중 100%; 다음 봉 시가 가정 |
| v2 | trend_8_26 | 9652.77 | -347.23 | buy / partial / 직전 완료 봉 목표 비중 100%; 다음 봉 시가 가정 |
| v2 | momentum_26 | 9667.52 | -332.48 | buy / partial / 직전 완료 봉 목표 비중 100%; 다음 봉 시가 가정 |
| v2 | breakout_8 | 9406.95 | -593.05 | sell / filled / 직전 완료 봉 목표 비중 0%; 다음 봉 시가 가정 |
| v2 | reversion_12 | 9345.07 | -654.93 | buy / partial / 직전 완료 봉 목표 비중 100%; 다음 봉 시가 가정 |
| v2 | volume_26 | 9378.42 | -621.58 | sell / filled / 직전 완료 봉 목표 비중 0%; 다음 봉 시가 가정 |
| v2 | trend_8_26 AND momentum_26 | 9816.56 | -183.44 | buy / partial / 직전 완료 봉 목표 비중 100%; 다음 봉 시가 가정 |
| v2 | trend_8_26 + momentum_26 | 9680.58 | -319.42 | buy / partial / 직전 완료 봉 목표 비중 100%; 다음 봉 시가 가정 |
| v2 | trend_8_26 AND breakout_8 | 9806.54 | -193.46 | sell / filled / 직전 완료 봉 목표 비중 0%; 다음 봉 시가 가정 |
| v2 | trend_8_26 + breakout_8 | 9549.20 | -450.80 | buy / filled / 직전 완료 봉 목표 비중 50%; 다음 봉 시가 가정 |
| v2 | trend_8_26 AND reversion_12 | 9725.41 | -274.59 | buy / partial / 직전 완료 봉 목표 비중 100%; 다음 봉 시가 가정 |
| v2 | trend_8_26 + reversion_12 | 9497.45 | -502.55 | buy / partial / 직전 완료 봉 목표 비중 100%; 다음 봉 시가 가정 |
| v2 | trend_8_26 AND volume_26 | 9797.73 | -202.27 | sell / filled / 직전 완료 봉 목표 비중 0%; 다음 봉 시가 가정 |
| v2 | trend_8_26 + volume_26 | 9534.49 | -465.51 | buy / filled / 직전 완료 봉 목표 비중 50%; 다음 봉 시가 가정 |
| v2 | momentum_26 AND breakout_8 | 9733.71 | -266.29 | sell / filled / 직전 완료 봉 목표 비중 0%; 다음 봉 시가 가정 |
| v2 | momentum_26 + breakout_8 | 9556.36 | -443.64 | buy / filled / 직전 완료 봉 목표 비중 50%; 다음 봉 시가 가정 |
| v2 | momentum_26 AND reversion_12 | 9901.70 | -98.30 | buy / partial / 직전 완료 봉 목표 비중 100%; 다음 봉 시가 가정 |
| v2 | momentum_26 + reversion_12 | 9544.47 | -455.53 | buy / partial / 직전 완료 봉 목표 비중 100%; 다음 봉 시가 가정 |
| v2 | momentum_26 AND volume_26 | 9897.79 | -102.21 | sell / filled / 직전 완료 봉 목표 비중 0%; 다음 봉 시가 가정 |
| v2 | momentum_26 + volume_26 | 9521.57 | -478.43 | buy / filled / 직전 완료 봉 목표 비중 50%; 다음 봉 시가 가정 |
| v2 | breakout_8 AND reversion_12 | 10000.00 | 0.00 | 대기 /  / 새 신호 대기 |
| v2 | breakout_8 + reversion_12 | 9414.90 | -585.10 | buy / filled / 직전 완료 봉 목표 비중 50%; 다음 봉 시가 가정 |
| v2 | breakout_8 AND volume_26 | 9690.16 | -309.84 | sell / filled / 직전 완료 봉 목표 비중 0%; 다음 봉 시가 가정 |
| v2 | breakout_8 + volume_26 | 9412.30 | -587.70 | sell / filled / 직전 완료 봉 목표 비중 0%; 다음 봉 시가 가정 |
| v2 | reversion_12 AND volume_26 | 9676.46 | -323.54 | sell / filled / 직전 완료 봉 목표 비중 0%; 다음 봉 시가 가정 |
| v2 | reversion_12 + volume_26 | 9400.84 | -599.16 | buy / filled / 직전 완료 봉 목표 비중 50%; 다음 봉 시가 가정 |
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
| cash | 0.00% | 0.00% | -3.47% | -0.00% | 0.00% |
| buy_hold | -3.07% | -3.47% | -3.47% | -3.47% | 100.00% |
| trend_8_26 | -1.47% | -5.12% | -3.47% | -1.54% | 43.98% |
| momentum_26 | -2.40% | -7.97% | -3.47% | -1.38% | 39.53% |
| breakout_8 | -0.55% | -13.78% | -3.47% | -0.70% | 19.90% |
| reversion_12 | -2.53% | -15.15% | -3.47% | -1.07% | 30.63% |
| volume_26 | -2.61% | -9.32% | -3.47% | -0.28% | 8.12% |
| trend_8_26 AND momentum_26 | -1.28% | -5.34% | -3.47% | -1.21% | 34.55% |
| trend_8_26 + momentum_26 | -1.93% | -6.16% | -3.47% | -1.46% | 41.76% |
| trend_8_26 AND breakout_8 | -0.38% | -8.02% | -3.47% | -0.40% | 11.52% |
| trend_8_26 + breakout_8 | -1.00% | -9.36% | -3.47% | -1.12% | 31.94% |
| trend_8_26 AND reversion_12 | -0.86% | -5.33% | -3.47% | -0.20% | 5.76% |
| trend_8_26 + reversion_12 | -1.99% | -10.09% | -3.47% | -1.30% | 37.31% |
| trend_8_26 AND volume_26 | -0.98% | -3.85% | -3.47% | -0.09% | 2.62% |
| trend_8_26 + volume_26 | -2.03% | -7.05% | -3.47% | -0.91% | 26.05% |
| momentum_26 AND breakout_8 | -0.21% | -7.48% | -3.47% | -0.36% | 10.21% |
| momentum_26 + breakout_8 | -1.47% | -10.74% | -3.47% | -1.04% | 29.72% |
| momentum_26 AND reversion_12 | 0.03% | -3.68% | -3.47% | -0.13% | 3.66% |
| momentum_26 + reversion_12 | -2.46% | -10.71% | -3.47% | -1.23% | 35.08% |
| momentum_26 AND volume_26 | -0.96% | -2.61% | -3.47% | -0.05% | 1.31% |
| momentum_26 + volume_26 | -2.50% | -8.27% | -3.47% | -0.83% | 23.83% |
| breakout_8 AND reversion_12 | 0.00% | 0.00% | -3.47% | -0.00% | 0.00% |
| breakout_8 + reversion_12 | -1.54% | -13.76% | -3.47% | -0.88% | 25.27% |
| breakout_8 AND volume_26 | -1.46% | -4.31% | -3.47% | -0.08% | 2.36% |
| breakout_8 + volume_26 | -1.58% | -11.40% | -3.47% | -0.49% | 14.01% |
| reversion_12 AND volume_26 | -0.62% | -4.31% | -3.47% | -0.14% | 3.93% |
| reversion_12 + volume_26 | -2.57% | -11.73% | -3.47% | -0.68% | 19.38% |
| ema_12_26 | -0.23% | -2.71% | -3.47% | -1.50% | 42.93% |
| macd_12_26_9 | 1.54% | -0.99% | -3.47% | -0.97% | 27.75% |
| rsi_14_recovery | -0.86% | -6.52% | -3.47% | -0.13% | 3.66% |
| bollinger_20_reentry | -0.31% | -4.81% | -3.47% | -0.10% | 2.88% |
| donchian_20 | -0.20% | -5.10% | -3.47% | -0.19% | 5.50% |
| atr_14_breakout | -1.18% | -7.22% | -3.47% | -0.14% | 3.93% |
| session_vwap | -0.85% | -9.98% | -3.47% | -1.38% | 39.53% |
| obv_20 | 0.29% | -3.43% | -3.47% | -1.33% | 37.96% |
| stochastic_14_3_recovery | -0.91% | -14.45% | -3.47% | -0.32% | 9.16% |
| mfi_14_recovery | 0.24% | -3.88% | -3.47% | -0.09% | 2.62% |
| adx_14_trend | 0.00% | -3.30% | -3.47% | -1.08% | 30.89% |
| aroon_25_trend | -1.71% | -5.36% | -3.47% | -0.73% | 20.94% |
| cci_20_momentum | -2.04% | -8.41% | -3.47% | -0.64% | 18.32% |
| williams_14_recovery | -0.28% | -9.47% | -3.47% | -0.21% | 6.02% |
| cmf_20_accumulation | -1.81% | -7.80% | -3.47% | -0.61% | 17.54% |
| chaikin_3_10 | -1.82% | -7.82% | -3.47% | -1.08% | 30.89% |
| roc_10_momentum | -0.63% | -1.87% | -3.47% | -0.11% | 3.14% |
| trix_15_trend | 0.35% | -2.56% | -3.47% | -1.09% | 31.15% |
| keltner_20_breakout | -0.91% | -4.18% | -3.47% | -0.18% | 5.24% |
| opening_range_30m | 2.57% | -1.23% | -3.47% | -0.74% | 21.20% |

동일 구간·초기 자금, 종료 시 청산 비용 포함. 노출 맞춤은 사후 설명용이며 v2 실제 계좌 성과가 아닙니다.
[낙폭 분해·비용 영향·전체 구간](IWM/comparison.json)

[v1 전체 기록](IWM/accounts.json) · [v2 전체 기록](IWM/accounts-v2.json)

## DIA 계좌

| 모델 | 전략 | 평가액 USD | 손익 USD | 최근 매매·이유 |
|---|---|---:|---:|---|
| v1 | cash | 10000.00 | 0.00 | 대기 /  / 새 신호 대기 |
| v1 | buy_hold | 9917.04 | -82.96 | buy /  / buy_hold: prior completed bar target 100%; next bar open simulation |
| v1 | trend_8_26 | 9875.74 | -124.26 | buy /  / trend_8_26: prior completed bar target 100%; next bar open simulation |
| v1 | momentum_26 | 9856.02 | -143.98 | buy /  / momentum_26: prior completed bar target 100%; next bar open simulation |
| v1 | breakout_8 | 9766.06 | -233.94 | sell /  / breakout_8: prior completed bar target 0%; next bar open simulation |
| v1 | reversion_12 | 9892.53 | -107.47 | sell /  / reversion_12: prior completed bar target 0%; next bar open simulation |
| v1 | volume_26 | 9908.95 | -91.05 | sell /  / volume_26: prior completed bar target 0%; next bar open simulation |
| v1 | trend_8_26 AND momentum_26 | 9856.02 | -143.98 | buy /  / trend_8_26 AND momentum_26: prior completed bar target 100%; next bar open simulation |
| v1 | trend_8_26 + momentum_26 | 9865.88 | -134.12 | buy /  / trend_8_26 + momentum_26: prior completed bar target 100%; next bar open simulation |
| v1 | trend_8_26 AND breakout_8 | 9899.20 | -100.80 | sell /  / trend_8_26 AND breakout_8: prior completed bar target 0%; next bar open simulation |
| v1 | trend_8_26 + breakout_8 | 9840.35 | -159.65 | sell /  / trend_8_26 + breakout_8: prior completed bar target 50%; next bar open simulation |
| v1 | trend_8_26 AND reversion_12 | 9936.00 | -64.00 | sell /  / trend_8_26 AND reversion_12: prior completed bar target 0%; next bar open simulation |
| v1 | trend_8_26 + reversion_12 | 9884.01 | -115.99 | buy /  / trend_8_26 + reversion_12: prior completed bar target 50%; next bar open simulation |
| v1 | trend_8_26 AND volume_26 | 9943.10 | -56.90 | sell /  / trend_8_26 AND volume_26: prior completed bar target 0%; next bar open simulation |
| v1 | trend_8_26 + volume_26 | 9892.23 | -107.77 | buy /  / trend_8_26 + volume_26: prior completed bar target 50%; next bar open simulation |
| v1 | momentum_26 AND breakout_8 | 9899.20 | -100.80 | sell /  / momentum_26 AND breakout_8: prior completed bar target 0%; next bar open simulation |
| v1 | momentum_26 + breakout_8 | 9810.88 | -189.12 | sell /  / momentum_26 + breakout_8: prior completed bar target 50%; next bar open simulation |
| v1 | momentum_26 AND reversion_12 | 9940.78 | -59.22 | sell /  / momentum_26 AND reversion_12: prior completed bar target 0%; next bar open simulation |
| v1 | momentum_26 + reversion_12 | 9874.13 | -125.87 | buy /  / momentum_26 + reversion_12: prior completed bar target 50%; next bar open simulation |
| v1 | momentum_26 AND volume_26 | 9943.10 | -56.90 | sell /  / momentum_26 AND volume_26: prior completed bar target 0%; next bar open simulation |
| v1 | momentum_26 + volume_26 | 9882.35 | -117.65 | buy /  / momentum_26 + volume_26: prior completed bar target 50%; next bar open simulation |
| v1 | breakout_8 AND reversion_12 | 10000.00 | 0.00 | 대기 /  / 새 신호 대기 |
| v1 | breakout_8 + reversion_12 | 9828.95 | -171.05 | sell /  / breakout_8 + reversion_12: prior completed bar target 0%; next bar open simulation |
| v1 | breakout_8 AND volume_26 | 10000.00 | 0.00 | 대기 /  / 새 신호 대기 |
| v1 | breakout_8 + volume_26 | 9837.14 | -162.86 | sell /  / breakout_8 + volume_26: prior completed bar target 0%; next bar open simulation |
| v1 | reversion_12 AND volume_26 | 9965.65 | -34.35 | sell /  / reversion_12 AND volume_26: prior completed bar target 0%; next bar open simulation |
| v1 | reversion_12 + volume_26 | 9920.50 | -79.50 | sell /  / reversion_12 + volume_26: prior completed bar target 0%; next bar open simulation |
| v1 | ema_12_26 | 9876.07 | -123.93 | sell /  / EMA12 > EMA26; 조건 미충족; EMA12=520.874, EMA26=520.918 |
| v1 | macd_12_26_9 | 9941.64 | -58.36 | sell /  / MACD > 신호선 그리고 MACD > 0; 조건 미충족; MACD=1.23542, signal9=1.25143 |
| v1 | rsi_14_recovery | 10000.00 | 0.00 | 대기 /  / 새 신호 대기 |
| v1 | bollinger_20_reentry | 9978.51 | -21.49 | sell /  / 직전 종가 < 직전 하단밴드, 현재 하단밴드 <= 종가 <= SMA20 (한 봉 목표); 조건 미충족; close=519.823, lower20=518.355, SMA20=521.612, previous_lower20=518.548 |
| v1 | donchian_20 | 9895.87 | -104.13 | sell /  / 종가 > 현재 봉을 제외한 직전 20봉 최고가; 조건 미충족; close=520.09, prior_high20=520.519 |
| v1 | atr_14_breakout | 9925.94 | -74.06 | sell /  / 종가 > 직전 종가 + 직전 ATR14 그리고 종가 > EMA26; 조건 미충족; close=519.24, threshold=520.599, prior_ATR14=0.989436, EMA26=519.399 |
| v1 | session_vwap | 9911.18 | -88.82 | buy /  / 종가 > 뉴욕 거래일별 누적 전형가격 VWAP; 조건 충족; close=519.01, session_VWAP=518.623, session_volume=840642 |
| v1 | obv_20 | 9862.52 | -137.48 | buy /  / OBV > OBV의 SMA20 그리고 종가 > EMA26; 조건 충족; OBV=-9.67274e+06, OBV_SMA20=-9.77214e+06, close=519.4, EMA26=519.374 |
| v1 | stochastic_14_3_recovery | 9821.75 | -178.25 | sell /  / 직전 %K14 < 20에서 %K14가 %D3 상향 돌파 (한 봉 목표); 조건 미충족; K14=21.4008, D3=27.0401, previous_K14=46.6025, previous_D3=27.3524 |
| v1 | mfi_14_recovery | 9936.38 | -63.62 | sell /  / 직전 MFI14 < 20, 현재 MFI14 >= 20 (한 봉 목표); 조건 미충족; MFI14=44.8014, previous_MFI14=20.0271 |
| v1 | adx_14_trend | 9882.74 | -117.26 | sell /  / Wilder ADX14 >= 25 그리고 +DI14 > -DI14; 조건 미충족; ADX14=30.2264, plus_DI14=23.4608, minus_DI14=27.9688 |
| v1 | aroon_25_trend | 9886.35 | -113.65 | sell /  / Aroon25 Up > 70 그리고 Down < 30 (동률이면 최신 극값); 조건 미충족; Aroon_up=68, Aroon_down=20 |
| v1 | cci_20_momentum | 9910.36 | -89.64 | sell /  / CCI20 > 100 (전형가격·평균절대편차); 조건 미충족; CCI20=46.8763 |
| v1 | williams_14_recovery | 9855.05 | -144.95 | sell /  / 직전 Williams %R14 < -80, 현재 >= -80 (한 봉 목표); 조건 미충족; Williams_R14=-78.5992, previous_R14=-53.3975 |
| v1 | cmf_20_accumulation | 9832.51 | -167.49 | sell /  / Chaikin Money Flow20 > 0.1; 조건 미충족; CMF20=0.0891944, volume20=1.5657e+06 |
| v1 | chaikin_3_10 | 9864.43 | -135.57 | buy /  / ADL의 EMA3 - EMA10 > 0 그리고 종가 > EMA26; 조건 충족; Chaikin3_10=42268.1, ADL=-1.72367e+07, close=519.4, EMA26=519.374 |
| v1 | roc_10_momentum | 10000.00 | 0.00 | 대기 /  / 새 신호 대기 |
| v1 | trix_15_trend | 9928.27 | -71.73 | sell /  / 15봉 삼중 EMA의 1봉 변화율 TRIX > 0 그리고 종가 > EMA26; 조건 미충족; TRIX15_percent=0.0322153, close=521.26, EMA26=521.365 |
| v1 | keltner_20_breakout | 9940.12 | -59.88 | sell /  / 종가 > EMA20 + 2 x Wilder ATR14; 조건 미충족; close=522.89, upper_Keltner=523.089, EMA20=521.145, ATR14=0.971947 |
| v1 | opening_range_30m | 9859.70 | -140.30 | buy /  / 뉴욕 09:30·09:45 두 완료 봉 최고가를 10:00 이후 종가가 돌파; 조건 충족; close=519.165, opening_high=519.1 |
| v2 | cash | 10000.00 | 0.00 | 대기 /  / 새 신호 대기 |
| v2 | buy_hold | 10039.90 | 39.90 | buy / partial / 직전 완료 봉 목표 비중 100%; 다음 봉 시가 가정 |
| v2 | trend_8_26 | 9809.80 | -190.20 | buy / partial / 직전 완료 봉 목표 비중 100%; 다음 봉 시가 가정 |
| v2 | momentum_26 | 9895.88 | -104.12 | buy / partial / 직전 완료 봉 목표 비중 100%; 다음 봉 시가 가정 |
| v2 | breakout_8 | 9293.42 | -706.58 | sell / filled / 직전 완료 봉 목표 비중 0%; 다음 봉 시가 가정 |
| v2 | reversion_12 | 9589.97 | -410.03 | sell / filled / 직전 완료 봉 목표 비중 0%; 다음 봉 시가 가정 |
| v2 | volume_26 | 9625.87 | -374.13 | sell / filled / 직전 완료 봉 목표 비중 0%; 다음 봉 시가 가정 |
| v2 | trend_8_26 AND momentum_26 | 9891.29 | -108.71 | buy / partial / 직전 완료 봉 목표 비중 100%; 다음 봉 시가 가정 |
| v2 | trend_8_26 + momentum_26 | 9852.81 | -147.19 | buy / partial / 직전 완료 봉 목표 비중 100%; 다음 봉 시가 가정 |
| v2 | trend_8_26 AND breakout_8 | 9585.26 | -414.74 | sell / filled / 직전 완료 봉 목표 비중 0%; 다음 봉 시가 가정 |
| v2 | trend_8_26 + breakout_8 | 9568.20 | -431.80 | sell / filled / 직전 완료 봉 목표 비중 50%; 다음 봉 시가 가정 |
| v2 | trend_8_26 AND reversion_12 | 9746.03 | -253.97 | sell / filled / 직전 완료 봉 목표 비중 0%; 다음 봉 시가 가정 |
| v2 | trend_8_26 + reversion_12 | 9698.89 | -301.11 | buy / filled / 직전 완료 봉 목표 비중 50%; 다음 봉 시가 가정 |
| v2 | trend_8_26 AND volume_26 | 9800.82 | -199.18 | sell / filled / 직전 완료 봉 목표 비중 0%; 다음 봉 시가 가정 |
| v2 | trend_8_26 + volume_26 | 9737.68 | -262.32 | buy / filled / 직전 완료 봉 목표 비중 50%; 다음 봉 시가 가정 |
| v2 | momentum_26 AND breakout_8 | 9574.35 | -425.65 | sell / filled / 직전 완료 봉 목표 비중 0%; 다음 봉 시가 가정 |
| v2 | momentum_26 + breakout_8 | 9589.99 | -410.01 | sell / filled / 직전 완료 봉 목표 비중 50%; 다음 봉 시가 가정 |
| v2 | momentum_26 AND reversion_12 | 9895.03 | -104.97 | sell / filled / 직전 완료 봉 목표 비중 0%; 다음 봉 시가 가정 |
| v2 | momentum_26 + reversion_12 | 9741.41 | -258.59 | buy / filled / 직전 완료 봉 목표 비중 50%; 다음 봉 시가 가정 |
| v2 | momentum_26 AND volume_26 | 9733.77 | -266.23 | sell / filled / 직전 완료 봉 목표 비중 0%; 다음 봉 시가 가정 |
| v2 | momentum_26 + volume_26 | 9800.99 | -199.01 | buy / filled / 직전 완료 봉 목표 비중 50%; 다음 봉 시가 가정 |
| v2 | breakout_8 AND reversion_12 | 10000.00 | 0.00 | 대기 /  / 새 신호 대기 |
| v2 | breakout_8 + reversion_12 | 9439.97 | -560.03 | sell / filled / 직전 완료 봉 목표 비중 0%; 다음 봉 시가 가정 |
| v2 | breakout_8 AND volume_26 | 9796.56 | -203.44 | sell / filled / 직전 완료 봉 목표 비중 0%; 다음 봉 시가 가정 |
| v2 | breakout_8 + volume_26 | 9457.93 | -542.07 | sell / filled / 직전 완료 봉 목표 비중 0%; 다음 봉 시가 가정 |
| v2 | reversion_12 AND volume_26 | 9963.66 | -36.34 | sell / filled / 직전 완료 봉 목표 비중 0%; 다음 봉 시가 가정 |
| v2 | reversion_12 + volume_26 | 9627.77 | -372.23 | sell / filled / 직전 완료 봉 목표 비중 0%; 다음 봉 시가 가정 |
| v2 | ema_12_26 | 9874.10 | -125.90 | sell / filled / EMA12 > EMA26; 조건 미충족; EMA12=520.874, EMA26=520.918; 직전 완료 봉 목표를 다음 봉 시가에 모의 적용 |
| v2 | macd_12_26_9 | 9939.65 | -60.35 | sell / filled / MACD > 신호선 그리고 MACD > 0; 조건 미충족; MACD=1.23542, signal9=1.25143; 직전 완료 봉 목표를 다음 봉 시가에 모의 적용 |
| v2 | rsi_14_recovery | 10000.00 | 0.00 | 대기 /  / 새 신호 대기 |
| v2 | bollinger_20_reentry | 9976.52 | -23.48 | sell / filled / 직전 종가 < 직전 하단밴드, 현재 하단밴드 <= 종가 <= SMA20 (한 봉 목표); 조건 미충족; close=519.823, lower20=518.355, SMA20=521.612, previous_lower20=518.548; 직전 완료 봉 목표를 다음 봉 시가에 모의 적용 |
| v2 | donchian_20 | 9891.91 | -108.09 | sell / filled / 종가 > 현재 봉을 제외한 직전 20봉 최고가; 조건 미충족; close=520.09, prior_high20=520.519; 직전 완료 봉 목표를 다음 봉 시가에 모의 적용 |
| v2 | atr_14_breakout | 9921.97 | -78.03 | sell / filled / 종가 > 직전 종가 + 직전 ATR14 그리고 종가 > EMA26; 조건 미충족; close=519.24, threshold=520.599, prior_ATR14=0.989436, EMA26=519.399; 직전 완료 봉 목표를 다음 봉 시가에 모의 적용 |
| v2 | session_vwap | 9906.23 | -93.77 | buy / partial / 종가 > 뉴욕 거래일별 누적 전형가격 VWAP; 조건 충족; close=519.01, session_VWAP=518.623, session_volume=840642; 직전 완료 봉 목표를 다음 봉 시가에 모의 적용 |
| v2 | obv_20 | 9857.59 | -142.41 | buy / partial / OBV > OBV의 SMA20 그리고 종가 > EMA26; 조건 충족; OBV=-9.67274e+06, OBV_SMA20=-9.77214e+06, close=519.4, EMA26=519.374; 직전 완료 봉 목표를 다음 봉 시가에 모의 적용 |
| v2 | stochastic_14_3_recovery | 9813.90 | -186.10 | sell / filled / 직전 %K14 < 20에서 %K14가 %D3 상향 돌파 (한 봉 목표); 조건 미충족; K14=21.4008, D3=27.0401, previous_K14=46.6025, previous_D3=27.3524; 직전 완료 봉 목표를 다음 봉 시가에 모의 적용 |
| v2 | mfi_14_recovery | 9932.40 | -67.60 | sell / filled / 직전 MFI14 < 20, 현재 MFI14 >= 20 (한 봉 목표); 조건 미충족; MFI14=44.8014, previous_MFI14=20.0271; 직전 완료 봉 목표를 다음 봉 시가에 모의 적용 |
| v2 | adx_14_trend | 9878.79 | -121.21 | sell / filled / Wilder ADX14 >= 25 그리고 +DI14 > -DI14; 조건 미충족; ADX14=30.2264, plus_DI14=23.4608, minus_DI14=27.9688; 직전 완료 봉 목표를 다음 봉 시가에 모의 적용 |
| v2 | aroon_25_trend | 9882.39 | -117.61 | sell / filled / Aroon25 Up > 70 그리고 Down < 30 (동률이면 최신 극값); 조건 미충족; Aroon_up=68, Aroon_down=20; 직전 완료 봉 목표를 다음 봉 시가에 모의 적용 |
| v2 | cci_20_momentum | 9906.40 | -93.60 | sell / filled / CCI20 > 100 (전형가격·평균절대편차); 조건 미충족; CCI20=46.8763; 직전 완료 봉 목표를 다음 봉 시가에 모의 적용 |
| v2 | williams_14_recovery | 9849.14 | -150.86 | sell / filled / 직전 Williams %R14 < -80, 현재 >= -80 (한 봉 목표); 조건 미충족; Williams_R14=-78.5992, previous_R14=-53.3975; 직전 완료 봉 목표를 다음 봉 시가에 모의 적용 |
| v2 | cmf_20_accumulation | 9826.61 | -173.39 | sell / filled / Chaikin Money Flow20 > 0.1; 조건 미충족; CMF20=0.0891944, volume20=1.5657e+06; 직전 완료 봉 목표를 다음 봉 시가에 모의 적용 |
| v2 | chaikin_3_10 | 9859.50 | -140.50 | buy / partial / ADL의 EMA3 - EMA10 > 0 그리고 종가 > EMA26; 조건 충족; Chaikin3_10=42268.1, ADL=-1.72367e+07, close=519.4, EMA26=519.374; 직전 완료 봉 목표를 다음 봉 시가에 모의 적용 |
| v2 | roc_10_momentum | 10000.00 | 0.00 | 대기 /  / 새 신호 대기 |
| v2 | trix_15_trend | 9926.28 | -73.72 | sell / filled / 15봉 삼중 EMA의 1봉 변화율 TRIX > 0 그리고 종가 > EMA26; 조건 미충족; TRIX15_percent=0.0322153, close=521.26, EMA26=521.365; 직전 완료 봉 목표를 다음 봉 시가에 모의 적용 |
| v2 | keltner_20_breakout | 9938.13 | -61.87 | sell / filled / 종가 > EMA20 + 2 x Wilder ATR14; 조건 미충족; close=522.89, upper_Keltner=523.089, EMA20=521.145, ATR14=0.971947; 직전 완료 봉 목표를 다음 봉 시가에 모의 적용 |
| v2 | opening_range_30m | 9852.80 | -147.20 | buy / partial / 뉴욕 09:30·09:45 두 완료 봉 최고가를 10:00 이후 종가가 돌파; 조건 충족; close=519.165, opening_high=519.1; 직전 완료 봉 목표를 다음 봉 시가에 모의 적용 |

### 같은 기간의 비용·노출 비교 (사후 연구)

| 전략 | 비용 전 | 비용 후 | 100% 보유 | 같은 평균 노출 보유 | 평균 노출 |
|---|---:|---:|---:|---:|---:|
| cash | 0.00% | 0.00% | 0.83% | 0.00% | 0.00% |
| buy_hold | 1.26% | 0.83% | 0.83% | 0.83% | 100.00% |
| trend_8_26 | 1.34% | -2.41% | 0.83% | 0.47% | 56.54% |
| momentum_26 | 0.36% | -3.76% | 0.83% | 0.43% | 51.31% |
| breakout_8 | 0.78% | -16.58% | 0.83% | 0.19% | 23.30% |
| reversion_12 | -1.43% | -9.37% | 0.83% | 0.20% | 24.35% |
| volume_26 | -0.74% | -10.26% | 0.83% | 0.08% | 9.95% |
| trend_8_26 AND momentum_26 | 1.48% | -2.70% | 0.83% | 0.38% | 46.07% |
| trend_8_26 + momentum_26 | 0.86% | -3.09% | 0.83% | 0.45% | 53.93% |
| trend_8_26 AND breakout_8 | 1.04% | -10.92% | 0.83% | 0.12% | 14.92% |
| trend_8_26 + breakout_8 | 1.06% | -9.39% | 0.83% | 0.33% | 39.93% |
| trend_8_26 AND reversion_12 | -0.02% | -4.93% | 0.83% | 0.05% | 6.54% |
| trend_8_26 + reversion_12 | -0.05% | -5.77% | 0.83% | 0.34% | 40.45% |
| trend_8_26 AND volume_26 | 0.36% | -4.57% | 0.83% | 0.04% | 4.71% |
| trend_8_26 + volume_26 | 0.30% | -6.23% | 0.83% | 0.28% | 33.25% |
| momentum_26 AND breakout_8 | 0.25% | -11.25% | 0.83% | 0.13% | 15.18% |
| momentum_26 + breakout_8 | 0.58% | -10.21% | 0.83% | 0.31% | 37.31% |
| momentum_26 AND reversion_12 | -0.27% | -3.57% | 0.83% | 0.05% | 5.76% |
| momentum_26 + reversion_12 | -0.53% | -6.03% | 0.83% | 0.31% | 37.83% |
| momentum_26 AND volume_26 | -0.56% | -5.45% | 0.83% | 0.04% | 4.45% |
| momentum_26 + volume_26 | -0.19% | -6.49% | 0.83% | 0.25% | 30.63% |
| breakout_8 AND reversion_12 | 0.00% | 0.00% | 0.83% | 0.00% | 0.00% |
| breakout_8 + reversion_12 | -0.33% | -12.88% | 0.83% | 0.20% | 23.83% |
| breakout_8 AND volume_26 | -0.73% | -3.60% | 0.83% | 0.02% | 2.62% |
| breakout_8 + volume_26 | 0.02% | -12.75% | 0.83% | 0.14% | 16.63% |
| reversion_12 AND volume_26 | -0.01% | -4.53% | 0.83% | 0.03% | 3.40% |
| reversion_12 + volume_26 | -1.08% | -9.63% | 0.83% | 0.14% | 17.15% |
| ema_12_26 | 0.17% | -1.91% | 0.83% | 0.40% | 48.69% |
| macd_12_26_9 | 1.65% | -1.30% | 0.83% | 0.23% | 27.49% |
| rsi_14_recovery | 0.01% | -2.07% | 0.83% | 0.01% | 1.31% |
| bollinger_20_reentry | -0.09% | -5.00% | 0.83% | 0.03% | 3.14% |
| donchian_20 | 0.31% | -6.21% | 0.83% | 0.07% | 8.38% |
| atr_14_breakout | -0.66% | -7.51% | 0.83% | 0.04% | 5.24% |
| session_vwap | 2.28% | -5.16% | 0.83% | 0.41% | 49.21% |
| obv_20 | 0.68% | -7.04% | 0.83% | 0.35% | 41.88% |
| stochastic_14_3_recovery | 0.63% | -12.03% | 0.83% | 0.07% | 8.38% |
| mfi_14_recovery | 0.10% | -3.61% | 0.83% | 0.02% | 2.36% |
| adx_14_trend | 0.20% | -3.52% | 0.83% | 0.27% | 32.46% |
| aroon_25_trend | 0.53% | -2.80% | 0.83% | 0.21% | 25.39% |
| cci_20_momentum | 0.61% | -5.53% | 0.83% | 0.21% | 24.87% |
| williams_14_recovery | 1.08% | -7.06% | 0.83% | 0.04% | 5.24% |
| cmf_20_accumulation | 1.03% | -6.32% | 0.83% | 0.22% | 26.18% |
| chaikin_3_10 | 1.89% | -7.10% | 0.83% | 0.34% | 41.36% |
| roc_10_momentum | 0.15% | -0.27% | 0.83% | 0.01% | 1.31% |
| trix_15_trend | 0.19% | -3.12% | 0.83% | 0.35% | 41.88% |
| keltner_20_breakout | 0.33% | -5.79% | 0.83% | 0.14% | 16.75% |
| opening_range_30m | 1.84% | -3.57% | 0.83% | 0.19% | 22.77% |

동일 구간·초기 자금, 종료 시 청산 비용 포함. 노출 맞춤은 사후 설명용이며 v2 실제 계좌 성과가 아닙니다.
[낙폭 분해·비용 영향·전체 구간](DIA/comparison.json)

[v1 전체 기록](DIA/accounts.json) · [v2 전체 기록](DIA/accounts-v2.json)

## MSFT 계좌

| 모델 | 전략 | 평가액 USD | 손익 USD | 최근 매매·이유 |
|---|---|---:|---:|---|
| v1 | cash | 10000.00 | 0.00 | 대기 /  / 새 신호 대기 |
| v1 | buy_hold | 9854.23 | -145.77 | buy /  / buy_hold: prior completed bar target 100%; next bar open simulation |
| v1 | trend_8_26 | 9836.76 | -163.24 | buy /  / trend_8_26: prior completed bar target 100%; next bar open simulation |
| v1 | momentum_26 | 9807.74 | -192.26 | buy /  / momentum_26: prior completed bar target 100%; next bar open simulation |
| v1 | breakout_8 | 9876.66 | -123.34 | sell /  / breakout_8: prior completed bar target 0%; next bar open simulation |
| v1 | reversion_12 | 9773.75 | -226.25 | sell /  / reversion_12: prior completed bar target 0%; next bar open simulation |
| v1 | volume_26 | 9811.31 | -188.69 | sell /  / volume_26: prior completed bar target 0%; next bar open simulation |
| v1 | trend_8_26 AND momentum_26 | 9822.05 | -177.95 | buy /  / trend_8_26 AND momentum_26: prior completed bar target 100%; next bar open simulation |
| v1 | trend_8_26 + momentum_26 | 9822.25 | -177.75 | buy /  / trend_8_26 + momentum_26: prior completed bar target 100%; next bar open simulation |
| v1 | trend_8_26 AND breakout_8 | 9905.03 | -94.97 | sell /  / trend_8_26 AND breakout_8: prior completed bar target 0%; next bar open simulation |
| v1 | trend_8_26 + breakout_8 | 9876.41 | -123.59 | buy /  / trend_8_26 + breakout_8: prior completed bar target 50%; next bar open simulation |
| v1 | trend_8_26 AND reversion_12 | 9895.34 | -104.66 | sell /  / trend_8_26 AND reversion_12: prior completed bar target 0%; next bar open simulation |
| v1 | trend_8_26 + reversion_12 | 9805.15 | -194.85 | buy /  / trend_8_26 + reversion_12: prior completed bar target 50%; next bar open simulation |
| v1 | trend_8_26 AND volume_26 | 9916.79 | -83.21 | sell /  / trend_8_26 AND volume_26: prior completed bar target 0%; next bar open simulation |
| v1 | trend_8_26 + volume_26 | 9823.97 | -176.03 | buy /  / trend_8_26 + volume_26: prior completed bar target 50%; next bar open simulation |
| v1 | momentum_26 AND breakout_8 | 9905.03 | -94.97 | sell /  / momentum_26 AND breakout_8: prior completed bar target 0%; next bar open simulation |
| v1 | momentum_26 + breakout_8 | 9842.12 | -157.88 | buy /  / momentum_26 + breakout_8: prior completed bar target 50%; next bar open simulation |
| v1 | momentum_26 AND reversion_12 | 9880.92 | -119.08 | sell /  / momentum_26 AND reversion_12: prior completed bar target 0%; next bar open simulation |
| v1 | momentum_26 + reversion_12 | 9790.68 | -209.32 | buy /  / momentum_26 + reversion_12: prior completed bar target 50%; next bar open simulation |
| v1 | momentum_26 AND volume_26 | 9916.79 | -83.21 | sell /  / momentum_26 AND volume_26: prior completed bar target 0%; next bar open simulation |
| v1 | momentum_26 + volume_26 | 9809.48 | -190.52 | buy /  / momentum_26 + volume_26: prior completed bar target 50%; next bar open simulation |
| v1 | breakout_8 AND reversion_12 | 10000.00 | 0.00 | 대기 /  / 새 신호 대기 |
| v1 | breakout_8 + reversion_12 | 9844.65 | -155.35 | sell /  / breakout_8 + reversion_12: prior completed bar target 0%; next bar open simulation |
| v1 | breakout_8 AND volume_26 | 9953.19 | -46.81 | sell /  / breakout_8 AND volume_26: prior completed bar target 0%; next bar open simulation |
| v1 | breakout_8 + volume_26 | 9863.58 | -136.42 | sell /  / breakout_8 + volume_26: prior completed bar target 0%; next bar open simulation |
| v1 | reversion_12 AND volume_26 | 9938.00 | -62.00 | sell /  / reversion_12 AND volume_26: prior completed bar target 0%; next bar open simulation |
| v1 | reversion_12 + volume_26 | 9792.40 | -207.60 | sell /  / reversion_12 + volume_26: prior completed bar target 0%; next bar open simulation |
| v1 | ema_12_26 | 9822.05 | -177.95 | buy /  / EMA12 > EMA26; 조건 충족; EMA12=531.372, EMA26=531.07 |
| v1 | macd_12_26_9 | 9858.20 | -141.80 | buy /  / MACD > 신호선 그리고 MACD > 0; 조건 충족; MACD=0.301143, signal9=-0.952827 |
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
| v1 | cmf_20_accumulation | 9762.54 | -237.46 | buy /  / Chaikin Money Flow20 > 0.1; 조건 충족; CMF20=0.184396, volume20=3.37825e+07 |
| v1 | chaikin_3_10 | 9821.21 | -178.79 | buy /  / ADL의 EMA3 - EMA10 > 0 그리고 종가 > EMA26; 조건 충족; Chaikin3_10=35900, ADL=1.1173e+08, close=533.95, EMA26=532.788 |
| v1 | roc_10_momentum | 9959.43 | -40.57 | sell /  / 10봉 ROC > 1% 그리고 종가 > EMA26; 조건 미충족; ROC10_percent=0.454191, close=534.125, EMA26=532.186 |
| v1 | trix_15_trend | 9872.32 | -127.68 | buy /  / 15봉 삼중 EMA의 1봉 변화율 TRIX > 0 그리고 종가 > EMA26; 조건 충족; TRIX15_percent=0.00435677, close=534.125, EMA26=532.186 |
| v1 | keltner_20_breakout | 9958.78 | -41.22 | sell /  / 종가 > EMA20 + 2 x Wilder ATR14; 조건 미충족; close=533.975, upper_Keltner=534.357, EMA20=530.111, ATR14=2.12332 |
| v1 | opening_range_30m | 9871.67 | -128.33 | buy /  / 뉴욕 09:30·09:45 두 완료 봉 최고가를 10:00 이후 종가가 돌파; 조건 충족; close=534.145, opening_high=532.63 |
| v2 | cash | 10000.00 | 0.00 | 대기 /  / 새 신호 대기 |
| v2 | buy_hold | 9908.00 | -92.00 | buy / partial / 직전 완료 봉 목표 비중 100%; 다음 봉 시가 가정 |
| v2 | trend_8_26 | 9772.38 | -227.62 | buy / partial / 직전 완료 봉 목표 비중 100%; 다음 봉 시가 가정 |
| v2 | momentum_26 | 9853.46 | -146.54 | buy / partial / 직전 완료 봉 목표 비중 100%; 다음 봉 시가 가정 |
| v2 | breakout_8 | 9670.87 | -329.13 | sell / filled / 직전 완료 봉 목표 비중 0%; 다음 봉 시가 가정 |
| v2 | reversion_12 | 9395.36 | -604.64 | sell / filled / 직전 완료 봉 목표 비중 0%; 다음 봉 시가 가정 |
| v2 | volume_26 | 9498.13 | -501.87 | sell / filled / 직전 완료 봉 목표 비중 0%; 다음 봉 시가 가정 |
| v2 | trend_8_26 AND momentum_26 | 9718.86 | -281.14 | buy / partial / 직전 완료 봉 목표 비중 100%; 다음 봉 시가 가정 |
| v2 | trend_8_26 + momentum_26 | 9813.11 | -186.89 | buy / partial / 직전 완료 봉 목표 비중 100%; 다음 봉 시가 가정 |
| v2 | trend_8_26 AND breakout_8 | 9543.92 | -456.08 | sell / filled / 직전 완료 봉 목표 비중 0%; 다음 봉 시가 가정 |
| v2 | trend_8_26 + breakout_8 | 9762.61 | -237.39 | buy / filled / 직전 완료 봉 목표 비중 50%; 다음 봉 시가 가정 |
| v2 | trend_8_26 AND reversion_12 | 9792.57 | -207.43 | sell / filled / 직전 완료 봉 목표 비중 0%; 다음 봉 시가 가정 |
| v2 | trend_8_26 + reversion_12 | 9581.63 | -418.37 | buy / filled / 직전 완료 봉 목표 비중 50%; 다음 봉 시가 가정 |
| v2 | trend_8_26 AND volume_26 | 9861.94 | -138.06 | sell / filled / 직전 완료 봉 목표 비중 0%; 다음 봉 시가 가정 |
| v2 | trend_8_26 + volume_26 | 9654.28 | -345.72 | buy / filled / 직전 완료 봉 목표 비중 50%; 다음 봉 시가 가정 |
| v2 | momentum_26 AND breakout_8 | 9697.48 | -302.52 | sell / filled / 직전 완료 봉 목표 비중 0%; 다음 봉 시가 가정 |
| v2 | momentum_26 + breakout_8 | 9761.79 | -238.21 | buy / filled / 직전 완료 봉 목표 비중 50%; 다음 봉 시가 가정 |
| v2 | momentum_26 AND reversion_12 | 9705.98 | -294.02 | sell / filled / 직전 완료 봉 목표 비중 0%; 다음 봉 시가 가정 |
| v2 | momentum_26 + reversion_12 | 9621.43 | -378.57 | buy / filled / 직전 완료 봉 목표 비중 50%; 다음 봉 시가 가정 |
| v2 | momentum_26 AND volume_26 | 9785.21 | -214.79 | sell / filled / 직전 완료 봉 목표 비중 0%; 다음 봉 시가 가정 |
| v2 | momentum_26 + volume_26 | 9694.39 | -305.61 | buy / filled / 직전 완료 봉 목표 비중 50%; 다음 봉 시가 가정 |
| v2 | breakout_8 AND reversion_12 | 10000.00 | 0.00 | 대기 /  / 새 신호 대기 |
| v2 | breakout_8 + reversion_12 | 9571.93 | -428.07 | sell / filled / 직전 완료 봉 목표 비중 0%; 다음 봉 시가 가정 |
| v2 | breakout_8 AND volume_26 | 9890.09 | -109.91 | sell / filled / 직전 완료 봉 목표 비중 0%; 다음 봉 시가 가정 |
| v2 | breakout_8 + volume_26 | 9624.43 | -375.57 | sell / filled / 직전 완료 봉 목표 비중 0%; 다음 봉 시가 가정 |
| v2 | reversion_12 AND volume_26 | 9699.57 | -300.43 | sell / filled / 직전 완료 봉 목표 비중 0%; 다음 봉 시가 가정 |
| v2 | reversion_12 + volume_26 | 9446.34 | -553.66 | sell / filled / 직전 완료 봉 목표 비중 0%; 다음 봉 시가 가정 |
| v2 | ema_12_26 | 9819.10 | -180.90 | buy / partial / EMA12 > EMA26; 조건 충족; EMA12=531.372, EMA26=531.07; 직전 완료 봉 목표를 다음 봉 시가에 모의 적용 |
| v2 | macd_12_26_9 | 9855.24 | -144.76 | buy / partial / MACD > 신호선 그리고 MACD > 0; 조건 충족; MACD=0.301143, signal9=-0.952827; 직전 완료 봉 목표를 다음 봉 시가에 모의 적용 |
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
| v2 | cmf_20_accumulation | 9759.61 | -240.39 | buy / partial / Chaikin Money Flow20 > 0.1; 조건 충족; CMF20=0.184396, volume20=3.37825e+07; 직전 완료 봉 목표를 다음 봉 시가에 모의 적용 |
| v2 | chaikin_3_10 | 9816.31 | -183.69 | buy / partial / ADL의 EMA3 - EMA10 > 0 그리고 종가 > EMA26; 조건 충족; Chaikin3_10=35900, ADL=1.1173e+08, close=533.95, EMA26=532.788; 직전 완료 봉 목표를 다음 봉 시가에 모의 적용 |
| v2 | roc_10_momentum | 9957.44 | -42.56 | sell / filled / 10봉 ROC > 1% 그리고 종가 > EMA26; 조건 미충족; ROC10_percent=0.454191, close=534.125, EMA26=532.186; 직전 완료 봉 목표를 다음 봉 시가에 모의 적용 |
| v2 | trix_15_trend | 9869.36 | -130.64 | buy / partial / 15봉 삼중 EMA의 1봉 변화율 TRIX > 0 그리고 종가 > EMA26; 조건 충족; TRIX15_percent=0.00435677, close=534.125, EMA26=532.186; 직전 완료 봉 목표를 다음 봉 시가에 모의 적용 |
| v2 | keltner_20_breakout | 9956.78 | -43.22 | sell / filled / 종가 > EMA20 + 2 x Wilder ATR14; 조건 미충족; close=533.975, upper_Keltner=534.357, EMA20=530.111, ATR14=2.12332; 직전 완료 봉 목표를 다음 봉 시가에 모의 적용 |
| v2 | opening_range_30m | 9868.71 | -131.29 | buy / partial / 뉴욕 09:30·09:45 두 완료 봉 최고가를 10:00 이후 종가가 돌파; 조건 충족; close=534.145, opening_high=532.63; 직전 완료 봉 목표를 다음 봉 시가에 모의 적용 |

### 같은 기간의 비용·노출 비교 (사후 연구)

| 전략 | 비용 전 | 비용 후 | 100% 보유 | 같은 평균 노출 보유 | 평균 노출 |
|---|---:|---:|---:|---:|---:|
| cash | 0.00% | 0.00% | 5.33% | 0.00% | 0.00% |
| buy_hold | 5.77% | 5.33% | 5.33% | 5.33% | 100.00% |
| trend_8_26 | 2.57% | -0.82% | 5.33% | 3.04% | 58.12% |
| momentum_26 | 1.72% | -4.09% | 5.33% | 3.17% | 60.47% |
| breakout_8 | 5.93% | -8.55% | 5.33% | 1.04% | 20.16% |
| reversion_12 | -2.85% | -11.80% | 5.33% | 1.26% | 24.35% |
| volume_26 | 1.69% | -7.29% | 5.33% | 0.46% | 8.90% |
| trend_8_26 AND momentum_26 | 0.45% | -5.29% | 5.33% | 2.82% | 53.93% |
| trend_8_26 + momentum_26 | 2.15% | -2.46% | 5.33% | 3.10% | 59.30% |
| trend_8_26 AND breakout_8 | 0.52% | -9.88% | 5.33% | 0.67% | 13.09% |
| trend_8_26 + breakout_8 | 4.25% | -4.16% | 5.33% | 2.03% | 39.14% |
| trend_8_26 AND reversion_12 | -0.05% | -5.36% | 5.33% | 0.33% | 6.54% |
| trend_8_26 + reversion_12 | -0.16% | -6.28% | 5.33% | 2.14% | 41.23% |
| trend_8_26 AND volume_26 | 3.42% | -0.42% | 5.33% | 0.16% | 3.14% |
| trend_8_26 + volume_26 | 2.14% | -3.51% | 5.33% | 1.73% | 33.51% |
| momentum_26 AND breakout_8 | 2.46% | -8.53% | 5.33% | 0.69% | 13.35% |
| momentum_26 + breakout_8 | 3.81% | -5.75% | 5.33% | 2.09% | 40.32% |
| momentum_26 AND reversion_12 | -1.06% | -7.49% | 5.33% | 0.48% | 9.42% |
| momentum_26 + reversion_12 | -0.58% | -7.83% | 5.33% | 2.20% | 42.41% |
| momentum_26 AND volume_26 | 1.77% | -3.23% | 5.33% | 0.20% | 3.93% |
| momentum_26 + volume_26 | 1.71% | -4.71% | 5.33% | 1.80% | 34.69% |
| breakout_8 AND reversion_12 | 0.00% | 0.00% | 5.33% | 0.00% | 0.00% |
| breakout_8 + reversion_12 | 1.46% | -9.43% | 5.33% | 1.15% | 22.26% |
| breakout_8 AND volume_26 | 2.00% | -0.96% | 5.33% | 0.11% | 2.09% |
| breakout_8 + volume_26 | 3.80% | -6.75% | 5.33% | 0.75% | 14.54% |
| reversion_12 AND volume_26 | -2.90% | -6.11% | 5.33% | 0.17% | 3.40% |
| reversion_12 + volume_26 | -0.60% | -9.38% | 5.33% | 0.85% | 16.63% |
| ema_12_26 | 1.68% | -1.68% | 5.33% | 3.15% | 60.21% |
| macd_12_26_9 | 1.21% | -3.76% | 5.33% | 1.79% | 34.55% |
| rsi_14_recovery | -0.06% | -2.13% | 5.33% | 0.07% | 1.31% |
| bollinger_20_reentry | -0.29% | -3.18% | 5.33% | 0.09% | 1.83% |
| donchian_20 | 1.76% | -4.05% | 5.33% | 0.25% | 4.97% |
| atr_14_breakout | 1.45% | -4.74% | 5.33% | 0.21% | 4.19% |
| session_vwap | 6.65% | -1.12% | 5.33% | 2.13% | 41.10% |
| obv_20 | 4.62% | -4.21% | 5.33% | 2.59% | 49.74% |
| stochastic_14_3_recovery | -0.74% | -10.63% | 5.33% | 0.33% | 6.54% |
| mfi_14_recovery | 1.54% | -1.81% | 5.33% | 0.11% | 2.09% |
| adx_14_trend | 3.84% | 1.26% | 5.33% | 2.41% | 46.34% |
| aroon_25_trend | 0.07% | -4.85% | 5.33% | 1.17% | 22.77% |
| cci_20_momentum | 3.27% | -3.44% | 5.33% | 1.17% | 22.77% |
| williams_14_recovery | -0.78% | -9.91% | 5.33% | 0.31% | 6.02% |
| cmf_20_accumulation | 0.68% | -5.07% | 5.33% | 1.67% | 32.20% |
| chaikin_3_10 | 3.74% | -4.21% | 5.33% | 2.38% | 45.81% |
| roc_10_momentum | -0.01% | -4.12% | 5.33% | 0.81% | 15.71% |
| trix_15_trend | 0.58% | -3.56% | 5.33% | 2.51% | 48.17% |
| keltner_20_breakout | 1.11% | -4.26% | 5.33% | 0.70% | 13.61% |
| opening_range_30m | -0.52% | -5.01% | 5.33% | 1.17% | 22.77% |

동일 구간·초기 자금, 종료 시 청산 비용 포함. 노출 맞춤은 사후 설명용이며 v2 실제 계좌 성과가 아닙니다.
[낙폭 분해·비용 영향·전체 구간](MSFT/comparison.json)

[v1 전체 기록](MSFT/accounts.json) · [v2 전체 기록](MSFT/accounts-v2.json)

## JPM 계좌

| 모델 | 전략 | 평가액 USD | 손익 USD | 최근 매매·이유 |
|---|---|---:|---:|---|
| v1 | cash | 10000.00 | 0.00 | 대기 /  / 새 신호 대기 |
| v1 | buy_hold | 9823.93 | -176.07 | buy /  / buy_hold: prior completed bar target 100%; next bar open simulation |
| v1 | trend_8_26 | 9924.04 | -75.96 | sell /  / trend_8_26: prior completed bar target 0%; next bar open simulation |
| v1 | momentum_26 | 9892.69 | -107.31 | sell /  / momentum_26: prior completed bar target 0%; next bar open simulation |
| v1 | breakout_8 | 9829.39 | -170.61 | sell /  / breakout_8: prior completed bar target 0%; next bar open simulation |
| v1 | reversion_12 | 9707.84 | -292.16 | buy /  / reversion_12: prior completed bar target 100%; next bar open simulation |
| v1 | volume_26 | 9975.57 | -24.43 | sell /  / volume_26: prior completed bar target 0%; next bar open simulation |
| v1 | trend_8_26 AND momentum_26 | 9924.04 | -75.96 | sell /  / trend_8_26 AND momentum_26: prior completed bar target 0%; next bar open simulation |
| v1 | trend_8_26 + momentum_26 | 9908.39 | -91.61 | sell /  / trend_8_26 + momentum_26: prior completed bar target 0%; next bar open simulation |
| v1 | trend_8_26 AND breakout_8 | 9915.55 | -84.45 | sell /  / trend_8_26 AND breakout_8: prior completed bar target 0%; next bar open simulation |
| v1 | trend_8_26 + breakout_8 | 9876.66 | -123.34 | sell /  / trend_8_26 + breakout_8: prior completed bar target 0%; next bar open simulation |
| v1 | trend_8_26 AND reversion_12 | 9899.24 | -100.76 | sell /  / trend_8_26 AND reversion_12: prior completed bar target 0%; next bar open simulation |
| v1 | trend_8_26 + reversion_12 | 9815.23 | -184.77 | buy /  / trend_8_26 + reversion_12: prior completed bar target 50%; next bar open simulation |
| v1 | trend_8_26 AND volume_26 | 10035.68 | 35.68 | sell /  / trend_8_26 AND volume_26: prior completed bar target 0%; next bar open simulation |
| v1 | trend_8_26 + volume_26 | 9949.67 | -50.33 | sell /  / trend_8_26 + volume_26: prior completed bar target 0%; next bar open simulation |
| v1 | momentum_26 AND breakout_8 | 9829.39 | -170.61 | sell /  / momentum_26 AND breakout_8: prior completed bar target 0%; next bar open simulation |
| v1 | momentum_26 + breakout_8 | 9861.04 | -138.96 | sell /  / momentum_26 + breakout_8: prior completed bar target 0%; next bar open simulation |
| v1 | momentum_26 AND reversion_12 | 9881.87 | -118.13 | sell /  / momentum_26 AND reversion_12: prior completed bar target 0%; next bar open simulation |
| v1 | momentum_26 + reversion_12 | 9819.36 | -180.64 | buy /  / momentum_26 + reversion_12: prior completed bar target 50%; next bar open simulation |
| v1 | momentum_26 AND volume_26 | 10035.68 | 35.68 | sell /  / momentum_26 AND volume_26: prior completed bar target 0%; next bar open simulation |
| v1 | momentum_26 + volume_26 | 9933.97 | -66.03 | sell /  / momentum_26 + volume_26: prior completed bar target 0%; next bar open simulation |
| v1 | breakout_8 AND reversion_12 | 10000.00 | 0.00 | 대기 /  / 새 신호 대기 |
| v1 | breakout_8 + reversion_12 | 9787.87 | -212.13 | buy /  / breakout_8 + reversion_12: prior completed bar target 50%; next bar open simulation |
| v1 | breakout_8 AND volume_26 | 10035.68 | 35.68 | sell /  / breakout_8 AND volume_26: prior completed bar target 0%; next bar open simulation |
| v1 | breakout_8 + volume_26 | 9902.19 | -97.81 | sell /  / breakout_8 + volume_26: prior completed bar target 0%; next bar open simulation |
| v1 | reversion_12 AND volume_26 | 9940.10 | -59.90 | sell /  / reversion_12 AND volume_26: prior completed bar target 0%; next bar open simulation |
| v1 | reversion_12 + volume_26 | 9840.68 | -159.32 | sell /  / reversion_12 + volume_26: prior completed bar target 50%; next bar open simulation |
| v1 | ema_12_26 | 9888.73 | -111.27 | sell /  / EMA12 > EMA26; 조건 미충족; EMA12=338.579, EMA26=338.665 |
| v1 | macd_12_26_9 | 9973.56 | -26.44 | sell /  / MACD > 신호선 그리고 MACD > 0; 조건 미충족; MACD=1.87003, signal9=1.96381 |
| v1 | rsi_14_recovery | 10000.00 | 0.00 | 대기 /  / 새 신호 대기 |
| v1 | bollinger_20_reentry | 9964.67 | -35.33 | sell /  / 직전 종가 < 직전 하단밴드, 현재 하단밴드 <= 종가 <= SMA20 (한 봉 목표); 조건 미충족; close=336.53, lower20=336.046, SMA20=337.886, previous_lower20=336.231 |
| v1 | donchian_20 | 9872.30 | -127.70 | sell /  / 종가 > 현재 봉을 제외한 직전 20봉 최고가; 조건 미충족; close=343.037, prior_high20=344.4 |
| v1 | atr_14_breakout | 9801.01 | -198.99 | sell /  / 종가 > 직전 종가 + 직전 ATR14 그리고 종가 > EMA26; 조건 미충족; close=337.6, threshold=340.744, prior_ATR14=1.10351, EMA26=338.759 |
| v1 | session_vwap | 9799.54 | -200.46 | sell /  / 종가 > 뉴욕 거래일별 누적 전형가격 VWAP; 조건 미충족; close=337.19, session_VWAP=337.924, session_volume=2.62446e+06 |
| v1 | obv_20 | 10007.55 | 7.55 | sell /  / OBV > OBV의 SMA20 그리고 종가 > EMA26; 조건 미충족; OBV=-1.68091e+07, OBV_SMA20=-1.39645e+07, close=341.625, EMA26=338.807 |
| v1 | stochastic_14_3_recovery | 9798.33 | -201.67 | sell /  / 직전 %K14 < 20에서 %K14가 %D3 상향 돌파 (한 봉 목표); 조건 미충족; K14=9.393, D3=8.15099, previous_K14=14.7764, previous_D3=10.4392 |
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
| v2 | buy_hold | 9988.08 | -11.92 | buy / partial / 직전 완료 봉 목표 비중 100%; 다음 봉 시가 가정 |
| v2 | trend_8_26 | 9931.17 | -68.83 | sell / filled / 직전 완료 봉 목표 비중 0%; 다음 봉 시가 가정 |
| v2 | momentum_26 | 9401.71 | -598.29 | sell / filled / 직전 완료 봉 목표 비중 0%; 다음 봉 시가 가정 |
| v2 | breakout_8 | 9168.97 | -831.03 | sell / filled / 직전 완료 봉 목표 비중 0%; 다음 봉 시가 가정 |
| v2 | reversion_12 | 9685.51 | -314.49 | buy / partial / 직전 완료 봉 목표 비중 100%; 다음 봉 시가 가정 |
| v2 | volume_26 | 9796.81 | -203.19 | sell / filled / 직전 완료 봉 목표 비중 0%; 다음 봉 시가 가정 |
| v2 | trend_8_26 AND momentum_26 | 9890.41 | -109.59 | sell / filled / 직전 완료 봉 목표 비중 0%; 다음 봉 시가 가정 |
| v2 | trend_8_26 + momentum_26 | 9683.69 | -316.31 | sell / filled / 직전 완료 봉 목표 비중 0%; 다음 봉 시가 가정 |
| v2 | trend_8_26 AND breakout_8 | 9287.76 | -712.24 | sell / filled / 직전 완료 봉 목표 비중 0%; 다음 봉 시가 가정 |
| v2 | trend_8_26 + breakout_8 | 9543.58 | -456.42 | sell / filled / 직전 완료 봉 목표 비중 0%; 다음 봉 시가 가정 |
| v2 | trend_8_26 AND reversion_12 | 9877.09 | -122.91 | sell / filled / 직전 완료 봉 목표 비중 0%; 다음 봉 시가 가정 |
| v2 | trend_8_26 + reversion_12 | 9848.94 | -151.06 | buy / filled / 직전 완료 봉 목표 비중 50%; 다음 봉 시가 가정 |
| v2 | trend_8_26 AND volume_26 | 9833.30 | -166.70 | sell / filled / 직전 완료 봉 목표 비중 0%; 다음 봉 시가 가정 |
| v2 | trend_8_26 + volume_26 | 9864.50 | -135.50 | sell / filled / 직전 완료 봉 목표 비중 0%; 다음 봉 시가 가정 |
| v2 | momentum_26 AND breakout_8 | 9150.64 | -849.36 | sell / filled / 직전 완료 봉 목표 비중 0%; 다음 봉 시가 가정 |
| v2 | momentum_26 + breakout_8 | 9305.78 | -694.22 | sell / filled / 직전 완료 봉 목표 비중 0%; 다음 봉 시가 가정 |
| v2 | momentum_26 AND reversion_12 | 9827.31 | -172.69 | sell / filled / 직전 완료 봉 목표 비중 0%; 다음 봉 시가 가정 |
| v2 | momentum_26 + reversion_12 | 9684.33 | -315.67 | buy / filled / 직전 완료 봉 목표 비중 50%; 다음 봉 시가 가정 |
| v2 | momentum_26 AND volume_26 | 9833.30 | -166.70 | sell / filled / 직전 완료 봉 목표 비중 0%; 다음 봉 시가 가정 |
| v2 | momentum_26 + volume_26 | 9659.05 | -340.95 | sell / filled / 직전 완료 봉 목표 비중 0%; 다음 봉 시가 가정 |
| v2 | breakout_8 AND reversion_12 | 10000.00 | 0.00 | 대기 /  / 새 신호 대기 |
| v2 | breakout_8 + reversion_12 | 9483.36 | -516.64 | buy / filled / 직전 완료 봉 목표 비중 50%; 다음 봉 시가 가정 |
| v2 | breakout_8 AND volume_26 | 9926.66 | -73.34 | sell / filled / 직전 완료 봉 목표 비중 0%; 다음 봉 시가 가정 |
| v2 | breakout_8 + volume_26 | 9497.74 | -502.26 | sell / filled / 직전 완료 봉 목표 비중 0%; 다음 봉 시가 가정 |
| v2 | reversion_12 AND volume_26 | 9987.18 | -12.82 | sell / filled / 직전 완료 봉 목표 비중 0%; 다음 봉 시가 가정 |
| v2 | reversion_12 + volume_26 | 9761.64 | -238.36 | sell / filled / 직전 완료 봉 목표 비중 50%; 다음 봉 시가 가정 |
| v2 | ema_12_26 | 9886.75 | -113.25 | sell / filled / EMA12 > EMA26; 조건 미충족; EMA12=338.579, EMA26=338.665; 직전 완료 봉 목표를 다음 봉 시가에 모의 적용 |
| v2 | macd_12_26_9 | 9971.56 | -28.44 | sell / filled / MACD > 신호선 그리고 MACD > 0; 조건 미충족; MACD=1.87003, signal9=1.96381; 직전 완료 봉 목표를 다음 봉 시가에 모의 적용 |
| v2 | rsi_14_recovery | 10000.00 | 0.00 | 대기 /  / 새 신호 대기 |
| v2 | bollinger_20_reentry | 9962.68 | -37.32 | sell / filled / 직전 종가 < 직전 하단밴드, 현재 하단밴드 <= 종가 <= SMA20 (한 봉 목표); 조건 미충족; close=336.53, lower20=336.046, SMA20=337.886, previous_lower20=336.231; 직전 완료 봉 목표를 다음 봉 시가에 모의 적용 |
| v2 | donchian_20 | 9868.35 | -131.65 | sell / filled / 종가 > 현재 봉을 제외한 직전 20봉 최고가; 조건 미충족; close=343.037, prior_high20=344.4; 직전 완료 봉 목표를 다음 봉 시가에 모의 적용 |
| v2 | atr_14_breakout | 9795.13 | -204.87 | sell / filled / 종가 > 직전 종가 + 직전 ATR14 그리고 종가 > EMA26; 조건 미충족; close=337.6, threshold=340.744, prior_ATR14=1.10351, EMA26=338.759; 직전 완료 봉 목표를 다음 봉 시가에 모의 적용 |
| v2 | session_vwap | 9791.71 | -208.29 | sell / filled / 종가 > 뉴욕 거래일별 누적 전형가격 VWAP; 조건 미충족; close=337.19, session_VWAP=337.924, session_volume=2.62446e+06; 직전 완료 봉 목표를 다음 봉 시가에 모의 적용 |
| v2 | obv_20 | 10005.55 | 5.55 | sell / filled / OBV > OBV의 SMA20 그리고 종가 > EMA26; 조건 미충족; OBV=-1.38544e+07, OBV_SMA20=-1.10099e+07, close=341.625, EMA26=338.807; 직전 완료 봉 목표를 다음 봉 시가에 모의 적용 |
| v2 | stochastic_14_3_recovery | 9788.53 | -211.47 | sell / filled / 직전 %K14 < 20에서 %K14가 %D3 상향 돌파 (한 봉 목표); 조건 미충족; K14=9.393, D3=8.15099, previous_K14=14.7764, previous_D3=10.4392; 직전 완료 봉 목표를 다음 봉 시가에 모의 적용 |
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
| cash | 0.00% | 0.00% | -0.81% | -0.00% | 0.00% |
| buy_hold | -0.39% | -0.81% | -0.81% | -0.81% | 100.00% |
| trend_8_26 | 1.16% | -2.59% | -0.81% | -0.42% | 51.57% |
| momentum_26 | -2.37% | -8.33% | -0.81% | -0.39% | 48.43% |
| breakout_8 | -2.94% | -17.60% | -0.81% | -0.16% | 19.37% |
| reversion_12 | 4.50% | -10.54% | -0.81% | -0.22% | 26.44% |
| volume_26 | -0.02% | -6.12% | -0.81% | -0.06% | 6.81% |
| trend_8_26 AND momentum_26 | 1.09% | -3.07% | -0.81% | -0.33% | 40.58% |
| trend_8_26 + momentum_26 | -0.61% | -5.30% | -0.81% | -0.41% | 50.00% |
| trend_8_26 AND breakout_8 | -3.21% | -13.22% | -0.81% | -0.10% | 12.04% |
| trend_8_26 + breakout_8 | -0.89% | -10.21% | -0.81% | -0.29% | 35.48% |
| trend_8_26 AND reversion_12 | 2.66% | -3.61% | -0.81% | -0.06% | 7.33% |
| trend_8_26 + reversion_12 | 2.84% | -6.06% | -0.81% | -0.32% | 39.01% |
| trend_8_26 AND volume_26 | -0.42% | -4.11% | -0.81% | -0.03% | 3.93% |
| trend_8_26 + volume_26 | 0.59% | -4.37% | -0.81% | -0.24% | 29.19% |
| momentum_26 AND breakout_8 | -2.51% | -12.96% | -0.81% | -0.10% | 12.04% |
| momentum_26 + breakout_8 | -2.63% | -12.89% | -0.81% | -0.28% | 33.91% |
| momentum_26 AND reversion_12 | 2.79% | -4.29% | -0.81% | -0.06% | 6.81% |
| momentum_26 + reversion_12 | 1.03% | -7.91% | -0.81% | -0.31% | 37.44% |
| momentum_26 AND volume_26 | 0.21% | -2.70% | -0.81% | -0.02% | 2.88% |
| momentum_26 + volume_26 | -1.18% | -7.03% | -0.81% | -0.23% | 27.62% |
| breakout_8 AND reversion_12 | 0.00% | 0.00% | -0.81% | -0.00% | 0.00% |
| breakout_8 + reversion_12 | 0.73% | -13.06% | -0.81% | -0.19% | 22.92% |
| breakout_8 AND volume_26 | -0.51% | -2.17% | -0.81% | -0.01% | 1.05% |
| breakout_8 + volume_26 | -1.48% | -11.31% | -0.81% | -0.11% | 13.10% |
| reversion_12 AND volume_26 | 1.33% | -2.01% | -0.81% | -0.03% | 3.40% |
| reversion_12 + volume_26 | 2.23% | -7.59% | -0.81% | -0.14% | 16.63% |
| ema_12_26 | 0.72% | -2.20% | -0.81% | -0.41% | 50.00% |
| macd_12_26_9 | 0.83% | -3.32% | -0.81% | -0.25% | 30.89% |
| rsi_14_recovery | 0.21% | -1.88% | -0.81% | -0.01% | 1.31% |
| bollinger_20_reentry | 0.66% | -4.69% | -0.81% | -0.03% | 3.40% |
| donchian_20 | -1.79% | -4.63% | -0.81% | -0.02% | 2.88% |
| atr_14_breakout | -1.59% | -8.37% | -0.81% | -0.04% | 4.71% |
| session_vwap | 1.91% | -7.48% | -0.81% | -0.38% | 46.86% |
| obv_20 | -3.51% | -14.21% | -0.81% | -0.25% | 30.10% |
| stochastic_14_3_recovery | -0.93% | -11.55% | -0.81% | -0.06% | 7.07% |
| mfi_14_recovery | 0.06% | -2.02% | -0.81% | -0.01% | 1.31% |
| adx_14_trend | -2.17% | -4.60% | -0.81% | -0.22% | 26.96% |
| aroon_25_trend | -1.12% | -5.19% | -0.81% | -0.18% | 22.51% |
| cci_20_momentum | -2.26% | -9.76% | -0.81% | -0.12% | 14.92% |
| williams_14_recovery | -1.64% | -11.81% | -0.81% | -0.06% | 6.81% |
| cmf_20_accumulation | -1.74% | -9.66% | -0.81% | -0.23% | 28.53% |
| chaikin_3_10 | 1.37% | -7.19% | -0.81% | -0.27% | 32.98% |
| roc_10_momentum | -0.98% | -3.45% | -0.81% | -0.06% | 7.85% |
| trix_15_trend | -1.25% | -8.83% | -0.81% | -0.29% | 35.08% |
| keltner_20_breakout | -1.19% | -3.65% | -0.81% | -0.03% | 3.93% |
| opening_range_30m | 0.15% | -3.16% | -0.81% | -0.14% | 16.75% |

동일 구간·초기 자금, 종료 시 청산 비용 포함. 노출 맞춤은 사후 설명용이며 v2 실제 계좌 성과가 아닙니다.
[낙폭 분해·비용 영향·전체 구간](JPM/comparison.json)

[v1 전체 기록](JPM/accounts.json) · [v2 전체 기록](JPM/accounts-v2.json)

## XOM 계좌

| 모델 | 전략 | 평가액 USD | 손익 USD | 최근 매매·이유 |
|---|---|---:|---:|---|
| v1 | cash | 10000.00 | 0.00 | 대기 /  / 새 신호 대기 |
| v1 | buy_hold | 10107.02 | 107.02 | buy /  / buy_hold: prior completed bar target 100%; next bar open simulation |
| v1 | trend_8_26 | 10052.15 | 52.15 | buy /  / trend_8_26: prior completed bar target 100%; next bar open simulation |
| v1 | momentum_26 | 10134.87 | 134.87 | buy /  / momentum_26: prior completed bar target 100%; next bar open simulation |
| v1 | breakout_8 | 9752.67 | -247.33 | sell /  / breakout_8: prior completed bar target 0%; next bar open simulation |
| v1 | reversion_12 | 9934.36 | -65.64 | sell /  / reversion_12: prior completed bar target 0%; next bar open simulation |
| v1 | volume_26 | 9889.56 | -110.44 | sell /  / volume_26: prior completed bar target 0%; next bar open simulation |
| v1 | trend_8_26 AND momentum_26 | 10052.15 | 52.15 | buy /  / trend_8_26 AND momentum_26: prior completed bar target 100%; next bar open simulation |
| v1 | trend_8_26 + momentum_26 | 10093.40 | 93.40 | buy /  / trend_8_26 + momentum_26: prior completed bar target 100%; next bar open simulation |
| v1 | trend_8_26 AND breakout_8 | 9829.71 | -170.29 | sell /  / trend_8_26 AND breakout_8: prior completed bar target 0%; next bar open simulation |
| v1 | trend_8_26 + breakout_8 | 9921.17 | -78.83 | sell /  / trend_8_26 + breakout_8: prior completed bar target 50%; next bar open simulation |
| v1 | trend_8_26 AND reversion_12 | 9921.77 | -78.23 | sell /  / trend_8_26 AND reversion_12: prior completed bar target 0%; next bar open simulation |
| v1 | trend_8_26 + reversion_12 | 9992.97 | -7.03 | buy /  / trend_8_26 + reversion_12: prior completed bar target 50%; next bar open simulation |
| v1 | trend_8_26 AND volume_26 | 9985.49 | -14.51 | sell /  / trend_8_26 AND volume_26: prior completed bar target 0%; next bar open simulation |
| v1 | trend_8_26 + volume_26 | 9970.38 | -29.62 | buy /  / trend_8_26 + volume_26: prior completed bar target 50%; next bar open simulation |
| v1 | momentum_26 AND breakout_8 | 9801.24 | -198.76 | sell /  / momentum_26 AND breakout_8: prior completed bar target 0%; next bar open simulation |
| v1 | momentum_26 + breakout_8 | 9942.03 | -57.97 | sell /  / momentum_26 + breakout_8: prior completed bar target 50%; next bar open simulation |
| v1 | momentum_26 AND reversion_12 | 9934.36 | -65.64 | sell /  / momentum_26 AND reversion_12: prior completed bar target 0%; next bar open simulation |
| v1 | momentum_26 + reversion_12 | 10034.00 | 34.00 | buy /  / momentum_26 + reversion_12: prior completed bar target 50%; next bar open simulation |
| v1 | momentum_26 AND volume_26 | 9985.49 | -14.51 | sell /  / momentum_26 AND volume_26: prior completed bar target 0%; next bar open simulation |
| v1 | momentum_26 + volume_26 | 10011.31 | 11.31 | buy /  / momentum_26 + volume_26: prior completed bar target 50%; next bar open simulation |
| v1 | breakout_8 AND reversion_12 | 10000.00 | 0.00 | 대기 /  / 새 신호 대기 |
| v1 | breakout_8 + reversion_12 | 9842.93 | -157.07 | sell /  / breakout_8 + reversion_12: prior completed bar target 0%; next bar open simulation |
| v1 | breakout_8 AND volume_26 | 9950.44 | -49.56 | sell /  / breakout_8 AND volume_26: prior completed bar target 0%; next bar open simulation |
| v1 | breakout_8 + volume_26 | 9820.74 | -179.26 | sell /  / breakout_8 + volume_26: prior completed bar target 0%; next bar open simulation |
| v1 | reversion_12 AND volume_26 | 10000.00 | 0.00 | 대기 /  / 새 신호 대기 |
| v1 | reversion_12 + volume_26 | 9911.86 | -88.14 | sell /  / reversion_12 + volume_26: prior completed bar target 0%; next bar open simulation |
| v1 | ema_12_26 | 10165.48 | 165.48 | buy /  / EMA12 > EMA26; 조건 충족; EMA12=175.145, EMA26=175.141 |
| v1 | macd_12_26_9 | 10093.47 | 93.47 | buy /  / MACD > 신호선 그리고 MACD > 0; 조건 충족; MACD=0.284963, signal9=0.263271 |
| v1 | rsi_14_recovery | 10000.00 | 0.00 | 대기 /  / 새 신호 대기 |
| v1 | bollinger_20_reentry | 9913.52 | -86.48 | sell /  / 직전 종가 < 직전 하단밴드, 현재 하단밴드 <= 종가 <= SMA20 (한 봉 목표); 조건 미충족; close=175.71, lower20=173.907, SMA20=174.743, previous_lower20=173.977 |
| v1 | donchian_20 | 9832.30 | -167.70 | sell /  / 종가 > 현재 봉을 제외한 직전 20봉 최고가; 조건 미충족; close=179.01, prior_high20=179.16 |
| v1 | atr_14_breakout | 9864.96 | -135.04 | sell /  / 종가 > 직전 종가 + 직전 ATR14 그리고 종가 > EMA26; 조건 미충족; close=177.19, threshold=177.748, prior_ATR14=0.663113, EMA26=175.734 |
| v1 | session_vwap | 10029.55 | 29.55 | buy /  / 종가 > 뉴욕 거래일별 누적 전형가격 VWAP; 조건 충족; close=178.12, session_VWAP=178.027, session_volume=4.4806e+06 |
| v1 | obv_20 | 9856.67 | -143.33 | buy /  / OBV > OBV의 SMA20 그리고 종가 > EMA26; 조건 충족; OBV=2.18423e+07, OBV_SMA20=2.18347e+07, close=177.655, EMA26=177.636 |
| v1 | stochastic_14_3_recovery | 9923.93 | -76.07 | sell /  / 직전 %K14 < 20에서 %K14가 %D3 상향 돌파 (한 봉 목표); 조건 미충족; K14=33.4559, D3=21.1148, previous_K14=20.3889, previous_D3=14.0974 |
| v1 | mfi_14_recovery | 10000.00 | 0.00 | 대기 /  / 새 신호 대기 |
| v1 | adx_14_trend | 9999.47 | -0.53 | sell /  / Wilder ADX14 >= 25 그리고 +DI14 > -DI14; 조건 미충족; ADX14=23.8302, plus_DI14=25.6436, minus_DI14=22.6035 |
| v1 | aroon_25_trend | 9929.86 | -70.14 | sell /  / Aroon25 Up > 70 그리고 Down < 30 (동률이면 최신 극값); 조건 미충족; Aroon_up=68, Aroon_down=0 |
| v1 | cci_20_momentum | 9785.01 | -214.99 | sell /  / CCI20 > 100 (전형가격·평균절대편차); 조건 미충족; CCI20=94.6347 |
| v1 | williams_14_recovery | 9838.11 | -161.89 | sell /  / 직전 Williams %R14 < -80, 현재 >= -80 (한 봉 목표); 조건 미충족; Williams_R14=-66.5441, previous_R14=-79.6111 |
| v1 | cmf_20_accumulation | 9967.24 | -32.76 | buy /  / Chaikin Money Flow20 > 0.1; 조건 충족; CMF20=0.158173, volume20=1.12043e+07 |
| v1 | chaikin_3_10 | 9909.84 | -90.16 | buy /  / ADL의 EMA3 - EMA10 > 0 그리고 종가 > EMA26; 조건 충족; Chaikin3_10=45202.2, ADL=2.7734e+07, close=177.655, EMA26=177.636 |
| v1 | roc_10_momentum | 9940.60 | -59.40 | sell /  / 10봉 ROC > 1% 그리고 종가 > EMA26; 조건 미충족; ROC10_percent=0.782107, close=178.47, EMA26=176.891 |
| v1 | trix_15_trend | 10008.22 | 8.22 | buy /  / 15봉 삼중 EMA의 1봉 변화율 TRIX > 0 그리고 종가 > EMA26; 조건 충족; TRIX15_percent=0.0352454, close=177.655, EMA26=177.636 |
| v1 | keltner_20_breakout | 9937.30 | -62.70 | sell /  / 종가 > EMA20 + 2 x Wilder ATR14; 조건 미충족; close=178.845, upper_Keltner=179.079, EMA20=177.884, ATR14=0.597175 |
| v1 | opening_range_30m | 10049.37 | 49.37 | sell /  / 뉴욕 09:30·09:45 두 완료 봉 최고가를 10:00 이후 종가가 돌파; 자료 부족·변동폭 또는 거래량 없음: 대기; close=179.01 |
| v2 | cash | 10000.00 | 0.00 | 대기 /  / 새 신호 대기 |
| v2 | buy_hold | 10429.56 | 429.56 | buy / partial / 직전 완료 봉 목표 비중 100%; 다음 봉 시가 가정 |
| v2 | trend_8_26 | 10145.86 | 145.86 | buy / partial / 직전 완료 봉 목표 비중 100%; 다음 봉 시가 가정 |
| v2 | momentum_26 | 10308.81 | 308.81 | buy / partial / 직전 완료 봉 목표 비중 100%; 다음 봉 시가 가정 |
| v2 | breakout_8 | 9222.01 | -777.99 | sell / filled / 직전 완료 봉 목표 비중 0%; 다음 봉 시가 가정 |
| v2 | reversion_12 | 9748.68 | -251.32 | sell / filled / 직전 완료 봉 목표 비중 0%; 다음 봉 시가 가정 |
| v2 | volume_26 | 9794.70 | -205.30 | sell / filled / 직전 완료 봉 목표 비중 0%; 다음 봉 시가 가정 |
| v2 | trend_8_26 AND momentum_26 | 10153.38 | 153.38 | buy / partial / 직전 완료 봉 목표 비중 100%; 다음 봉 시가 가정 |
| v2 | trend_8_26 + momentum_26 | 10227.02 | 227.02 | buy / partial / 직전 완료 봉 목표 비중 100%; 다음 봉 시가 가정 |
| v2 | trend_8_26 AND breakout_8 | 9281.59 | -718.41 | sell / filled / 직전 완료 봉 목표 비중 0%; 다음 봉 시가 가정 |
| v2 | trend_8_26 + breakout_8 | 9714.06 | -285.94 | sell / filled / 직전 완료 봉 목표 비중 50%; 다음 봉 시가 가정 |
| v2 | trend_8_26 AND reversion_12 | 9760.78 | -239.22 | sell / filled / 직전 완료 봉 목표 비중 0%; 다음 봉 시가 가정 |
| v2 | trend_8_26 + reversion_12 | 9945.26 | -54.74 | buy / filled / 직전 완료 봉 목표 비중 50%; 다음 봉 시가 가정 |
| v2 | trend_8_26 AND volume_26 | 9879.28 | -120.72 | sell / filled / 직전 완료 봉 목표 비중 0%; 다음 봉 시가 가정 |
| v2 | trend_8_26 + volume_26 | 9968.54 | -31.46 | buy / filled / 직전 완료 봉 목표 비중 50%; 다음 봉 시가 가정 |
| v2 | momentum_26 AND breakout_8 | 9269.79 | -730.21 | sell / filled / 직전 완료 봉 목표 비중 0%; 다음 봉 시가 가정 |
| v2 | momentum_26 + breakout_8 | 9750.91 | -249.09 | sell / filled / 직전 완료 봉 목표 비중 50%; 다음 봉 시가 가정 |
| v2 | momentum_26 AND reversion_12 | 9733.85 | -266.15 | sell / filled / 직전 완료 봉 목표 비중 0%; 다음 봉 시가 가정 |
| v2 | momentum_26 + reversion_12 | 10024.84 | 24.84 | buy / filled / 직전 완료 봉 목표 비중 50%; 다음 봉 시가 가정 |
| v2 | momentum_26 AND volume_26 | 9941.52 | -58.48 | sell / filled / 직전 완료 봉 목표 비중 0%; 다음 봉 시가 가정 |
| v2 | momentum_26 + volume_26 | 10069.36 | 69.36 | buy / filled / 직전 완료 봉 목표 비중 50%; 다음 봉 시가 가정 |
| v2 | breakout_8 AND reversion_12 | 10000.00 | 0.00 | 대기 /  / 새 신호 대기 |
| v2 | breakout_8 + reversion_12 | 9481.42 | -518.58 | sell / filled / 직전 완료 봉 목표 비중 0%; 다음 봉 시가 가정 |
| v2 | breakout_8 AND volume_26 | 9918.86 | -81.14 | sell / filled / 직전 완료 봉 목표 비중 0%; 다음 봉 시가 가정 |
| v2 | breakout_8 + volume_26 | 9523.78 | -476.22 | sell / filled / 직전 완료 봉 목표 비중 0%; 다음 봉 시가 가정 |
| v2 | reversion_12 AND volume_26 | 9949.87 | -50.13 | sell / filled / 직전 완료 봉 목표 비중 0%; 다음 봉 시가 가정 |
| v2 | reversion_12 + volume_26 | 9792.16 | -207.84 | sell / filled / 직전 완료 봉 목표 비중 0%; 다음 봉 시가 가정 |
| v2 | ema_12_26 | 10164.46 | 164.46 | buy / partial / EMA12 > EMA26; 조건 충족; EMA12=175.145, EMA26=175.141; 직전 완료 봉 목표를 다음 봉 시가에 모의 적용 |
| v2 | macd_12_26_9 | 10090.44 | 90.44 | buy / partial / MACD > 신호선 그리고 MACD > 0; 조건 충족; MACD=0.284963, signal9=0.263271; 직전 완료 봉 목표를 다음 봉 시가에 모의 적용 |
| v2 | rsi_14_recovery | 10000.00 | 0.00 | 대기 /  / 새 신호 대기 |
| v2 | bollinger_20_reentry | 9911.54 | -88.46 | sell / filled / 직전 종가 < 직전 하단밴드, 현재 하단밴드 <= 종가 <= SMA20 (한 봉 목표); 조건 미충족; close=175.71, lower20=173.907, SMA20=174.743, previous_lower20=173.977; 직전 완료 봉 목표를 다음 봉 시가에 모의 적용 |
| v2 | donchian_20 | 9824.43 | -175.57 | sell / filled / 종가 > 현재 봉을 제외한 직전 20봉 최고가; 조건 미충족; close=179.01, prior_high20=179.16; 직전 완료 봉 목표를 다음 봉 시가에 모의 적용 |
| v2 | atr_14_breakout | 9859.04 | -140.96 | sell / filled / 종가 > 직전 종가 + 직전 ATR14 그리고 종가 > EMA26; 조건 미충족; close=177.19, threshold=177.748, prior_ATR14=0.663113, EMA26=175.734; 직전 완료 봉 목표를 다음 봉 시가에 모의 적용 |
| v2 | session_vwap | 10024.54 | 24.54 | buy / partial / 종가 > 뉴욕 거래일별 누적 전형가격 VWAP; 조건 충족; close=178.12, session_VWAP=178.027, session_volume=4.4806e+06; 직전 완료 봉 목표를 다음 봉 시가에 모의 적용 |
| v2 | obv_20 | 9849.77 | -150.23 | buy / partial / OBV > OBV의 SMA20 그리고 종가 > EMA26; 조건 충족; OBV=2.18423e+07, OBV_SMA20=2.18347e+07, close=177.655, EMA26=177.636; 직전 완료 봉 목표를 다음 봉 시가에 모의 적용 |
| v2 | stochastic_14_3_recovery | 9919.96 | -80.04 | sell / filled / 직전 %K14 < 20에서 %K14가 %D3 상향 돌파 (한 봉 목표); 조건 미충족; K14=33.4559, D3=21.1148, previous_K14=20.3889, previous_D3=14.0974; 직전 완료 봉 목표를 다음 봉 시가에 모의 적용 |
| v2 | mfi_14_recovery | 10000.00 | 0.00 | 대기 /  / 새 신호 대기 |
| v2 | adx_14_trend | 9993.47 | -6.53 | sell / filled / Wilder ADX14 >= 25 그리고 +DI14 > -DI14; 조건 미충족; ADX14=23.8302, plus_DI14=25.6436, minus_DI14=22.6035; 직전 완료 봉 목표를 다음 봉 시가에 모의 적용 |
| v2 | aroon_25_trend | 9927.87 | -72.13 | sell / filled / Aroon25 Up > 70 그리고 Down < 30 (동률이면 최신 극값); 조건 미충족; Aroon_up=68, Aroon_down=0; 직전 완료 봉 목표를 다음 봉 시가에 모의 적용 |
| v2 | cci_20_momentum | 9773.27 | -226.73 | sell / filled / CCI20 > 100 (전형가격·평균절대편차); 조건 미충족; CCI20=94.6347; 직전 완료 봉 목표를 다음 봉 시가에 모의 적용 |
| v2 | williams_14_recovery | 9832.21 | -167.79 | sell / filled / 직전 Williams %R14 < -80, 현재 >= -80 (한 봉 목표); 조건 미충족; Williams_R14=-66.5441, previous_R14=-79.6111; 직전 완료 봉 목표를 다음 봉 시가에 모의 적용 |
| v2 | cmf_20_accumulation | 9966.24 | -33.76 | buy / partial / Chaikin Money Flow20 > 0.1; 조건 충족; CMF20=0.158173, volume20=1.12043e+07; 직전 완료 봉 목표를 다음 봉 시가에 모의 적용 |
| v2 | chaikin_3_10 | 9904.89 | -95.11 | buy / partial / ADL의 EMA3 - EMA10 > 0 그리고 종가 > EMA26; 조건 충족; Chaikin3_10=45202.2, ADL=2.7734e+07, close=177.655, EMA26=177.636; 직전 완료 봉 목표를 다음 봉 시가에 모의 적용 |
| v2 | roc_10_momentum | 9934.64 | -65.36 | sell / filled / 10봉 ROC > 1% 그리고 종가 > EMA26; 조건 미충족; ROC10_percent=0.782107, close=178.47, EMA26=176.891; 직전 완료 봉 목표를 다음 봉 시가에 모의 적용 |
| v2 | trix_15_trend | 10003.22 | 3.22 | buy / partial / 15봉 삼중 EMA의 1봉 변화율 TRIX > 0 그리고 종가 > EMA26; 조건 충족; TRIX15_percent=0.0352454, close=177.655, EMA26=177.636; 직전 완료 봉 목표를 다음 봉 시가에 모의 적용 |
| v2 | keltner_20_breakout | 9931.34 | -68.66 | sell / filled / 종가 > EMA20 + 2 x Wilder ATR14; 조건 미충족; close=178.845, upper_Keltner=179.079, EMA20=177.884, ATR14=0.597175; 직전 완료 봉 목표를 다음 봉 시가에 모의 적용 |
| v2 | opening_range_30m | 10047.36 | 47.36 | sell / filled / 뉴욕 09:30·09:45 두 완료 봉 최고가를 10:00 이후 종가가 돌파; 자료 부족·변동폭 또는 거래량 없음: 대기; close=179.01; 직전 완료 봉 목표를 다음 봉 시가에 모의 적용 |

### 같은 기간의 비용·노출 비교 (사후 연구)

| 전략 | 비용 전 | 비용 후 | 100% 보유 | 같은 평균 노출 보유 | 평균 노출 |
|---|---:|---:|---:|---:|---:|
| cash | 0.00% | 0.00% | 10.59% | 0.00% | 0.00% |
| buy_hold | 11.06% | 10.59% | 10.59% | 10.59% | 100.00% |
| trend_8_26 | 2.81% | -1.83% | 10.59% | 6.93% | 66.49% |
| momentum_26 | 3.48% | -3.65% | 10.59% | 7.61% | 72.77% |
| breakout_8 | -0.54% | -19.38% | 10.59% | 2.81% | 27.49% |
| reversion_12 | 5.32% | -4.78% | 10.59% | 2.17% | 21.20% |
| volume_26 | 3.26% | -3.86% | 10.59% | 0.48% | 4.71% |
| trend_8_26 AND momentum_26 | 1.33% | -3.65% | 10.59% | 6.37% | 61.26% |
| trend_8_26 + momentum_26 | 3.15% | -2.54% | 10.59% | 7.27% | 69.64% |
| trend_8_26 AND breakout_8 | -0.36% | -15.77% | 10.59% | 2.22% | 21.73% |
| trend_8_26 + breakout_8 | 1.14% | -10.65% | 10.59% | 4.86% | 47.00% |
| trend_8_26 AND reversion_12 | 0.37% | -4.96% | 10.59% | 0.90% | 8.90% |
| trend_8_26 + reversion_12 | 4.09% | -3.11% | 10.59% | 4.53% | 43.85% |
| trend_8_26 AND volume_26 | 2.37% | -1.84% | 10.59% | 0.26% | 2.62% |
| trend_8_26 + volume_26 | 3.05% | -2.65% | 10.59% | 3.66% | 35.61% |
| momentum_26 AND breakout_8 | -0.66% | -18.11% | 10.59% | 2.62% | 25.65% |
| momentum_26 + breakout_8 | 1.47% | -11.85% | 10.59% | 5.19% | 50.14% |
| momentum_26 AND reversion_12 | 0.87% | -5.29% | 10.59% | 1.01% | 9.95% |
| momentum_26 + reversion_12 | 4.42% | -3.00% | 10.59% | 4.86% | 46.99% |
| momentum_26 AND volume_26 | 2.15% | -1.64% | 10.59% | 0.24% | 2.36% |
| momentum_26 + volume_26 | 3.39% | -2.53% | 10.59% | 3.99% | 38.75% |
| breakout_8 AND reversion_12 | 0.00% | 0.00% | 10.59% | 0.00% | 0.00% |
| breakout_8 + reversion_12 | 2.36% | -12.21% | 10.59% | 2.49% | 24.36% |
| breakout_8 AND volume_26 | 0.51% | -1.17% | 10.59% | 0.11% | 1.05% |
| breakout_8 + volume_26 | 1.35% | -11.03% | 10.59% | 1.64% | 16.11% |
| reversion_12 AND volume_26 | 1.10% | -1.00% | 10.59% | 0.13% | 1.31% |
| reversion_12 + volume_26 | 4.30% | -3.51% | 10.59% | 1.32% | 12.96% |
| ema_12_26 | 2.92% | -0.06% | 10.59% | 8.04% | 76.70% |
| macd_12_26_9 | 0.38% | -5.35% | 10.59% | 4.37% | 42.41% |
| rsi_14_recovery | -0.15% | -0.57% | 10.59% | 0.03% | 0.26% |
| bollinger_20_reentry | -0.86% | -3.33% | 10.59% | 0.16% | 1.57% |
| donchian_20 | -0.93% | -10.43% | 10.59% | 0.98% | 9.69% |
| atr_14_breakout | 0.47% | -8.01% | 10.59% | 0.58% | 5.76% |
| session_vwap | 2.13% | -9.20% | 10.59% | 7.16% | 68.59% |
| obv_20 | 2.12% | -6.10% | 10.59% | 4.95% | 47.91% |
| stochastic_14_3_recovery | 1.68% | -6.90% | 10.59% | 0.56% | 5.50% |
| mfi_14_recovery | -0.31% | -1.97% | 10.59% | 0.11% | 1.05% |
| adx_14_trend | 3.88% | 0.87% | 10.59% | 4.57% | 44.24% |
| aroon_25_trend | -2.08% | -8.44% | 10.59% | 3.63% | 35.34% |
| cci_20_momentum | 3.56% | -5.18% | 10.59% | 2.95% | 28.80% |
| williams_14_recovery | 0.21% | -5.51% | 10.59% | 0.37% | 3.66% |
| cmf_20_accumulation | 1.13% | -5.44% | 10.59% | 5.56% | 53.66% |
| chaikin_3_10 | 0.60% | -8.28% | 10.59% | 6.18% | 59.42% |
| roc_10_momentum | 0.80% | -5.36% | 10.59% | 1.33% | 13.09% |
| trix_15_trend | 1.31% | -4.87% | 10.59% | 6.82% | 65.45% |
| keltner_20_breakout | 0.18% | -6.72% | 10.59% | 1.76% | 17.28% |
| opening_range_30m | 0.54% | -9.10% | 10.59% | 4.02% | 39.01% |

동일 구간·초기 자금, 종료 시 청산 비용 포함. 노출 맞춤은 사후 설명용이며 v2 실제 계좌 성과가 아닙니다.
[낙폭 분해·비용 영향·전체 구간](XOM/comparison.json)

[v1 전체 기록](XOM/accounts.json) · [v2 전체 기록](XOM/accounts-v2.json)

## JNJ 계좌

| 모델 | 전략 | 평가액 USD | 손익 USD | 최근 매매·이유 |
|---|---|---:|---:|---|
| v1 | cash | 10000.00 | 0.00 | 대기 /  / 새 신호 대기 |
| v1 | buy_hold | 9930.04 | -69.96 | buy /  / buy_hold: prior completed bar target 100%; next bar open simulation |
| v1 | trend_8_26 | 9882.29 | -117.71 | buy /  / trend_8_26: prior completed bar target 100%; next bar open simulation |
| v1 | momentum_26 | 9898.09 | -101.91 | sell /  / momentum_26: prior completed bar target 0%; next bar open simulation |
| v1 | breakout_8 | 9632.82 | -367.18 | sell /  / breakout_8: prior completed bar target 0%; next bar open simulation |
| v1 | reversion_12 | 9891.56 | -108.44 | sell /  / reversion_12: prior completed bar target 0%; next bar open simulation |
| v1 | volume_26 | 9884.71 | -115.29 | sell /  / volume_26: prior completed bar target 0%; next bar open simulation |
| v1 | trend_8_26 AND momentum_26 | 9950.33 | -49.67 | sell /  / trend_8_26 AND momentum_26: prior completed bar target 0%; next bar open simulation |
| v1 | trend_8_26 + momentum_26 | 9890.15 | -109.85 | buy /  / trend_8_26 + momentum_26: prior completed bar target 50%; next bar open simulation |
| v1 | trend_8_26 AND breakout_8 | 9937.40 | -62.60 | sell /  / trend_8_26 AND breakout_8: prior completed bar target 0%; next bar open simulation |
| v1 | trend_8_26 + breakout_8 | 9776.21 | -223.79 | buy /  / trend_8_26 + breakout_8: prior completed bar target 50%; next bar open simulation |
| v1 | trend_8_26 AND reversion_12 | 9992.01 | -7.99 | sell /  / trend_8_26 AND reversion_12: prior completed bar target 0%; next bar open simulation |
| v1 | trend_8_26 + reversion_12 | 9886.84 | -113.16 | buy /  / trend_8_26 + reversion_12: prior completed bar target 50%; next bar open simulation |
| v1 | trend_8_26 AND volume_26 | 9935.63 | -64.37 | sell /  / trend_8_26 AND volume_26: prior completed bar target 0%; next bar open simulation |
| v1 | trend_8_26 + volume_26 | 9883.45 | -116.55 | buy /  / trend_8_26 + volume_26: prior completed bar target 50%; next bar open simulation |
| v1 | momentum_26 AND breakout_8 | 9911.77 | -88.23 | sell /  / momentum_26 AND breakout_8: prior completed bar target 0%; next bar open simulation |
| v1 | momentum_26 + breakout_8 | 9764.45 | -235.55 | sell /  / momentum_26 + breakout_8: prior completed bar target 0%; next bar open simulation |
| v1 | momentum_26 AND reversion_12 | 10000.00 | 0.00 | 대기 /  / 새 신호 대기 |
| v1 | momentum_26 + reversion_12 | 9914.55 | -85.45 | sell /  / momentum_26 + reversion_12: prior completed bar target 0%; next bar open simulation |
| v1 | momentum_26 AND volume_26 | 10000.00 | 0.00 | 대기 /  / 새 신호 대기 |
| v1 | momentum_26 + volume_26 | 9911.13 | -88.87 | sell /  / momentum_26 + volume_26: prior completed bar target 0%; next bar open simulation |
| v1 | breakout_8 AND reversion_12 | 10000.00 | 0.00 | 대기 /  / 새 신호 대기 |
| v1 | breakout_8 + reversion_12 | 9761.18 | -238.82 | sell /  / breakout_8 + reversion_12: prior completed bar target 0%; next bar open simulation |
| v1 | breakout_8 AND volume_26 | 10000.00 | 0.00 | 대기 /  / 새 신호 대기 |
| v1 | breakout_8 + volume_26 | 9757.82 | -242.18 | sell /  / breakout_8 + volume_26: prior completed bar target 0%; next bar open simulation |
| v1 | reversion_12 AND volume_26 | 9974.59 | -25.41 | sell /  / reversion_12 AND volume_26: prior completed bar target 0%; next bar open simulation |
| v1 | reversion_12 + volume_26 | 9907.87 | -92.13 | sell /  / reversion_12 + volume_26: prior completed bar target 0%; next bar open simulation |
| v1 | ema_12_26 | 9781.22 | -218.78 | sell /  / EMA12 > EMA26; 조건 미충족; EMA12=255.193, EMA26=255.284 |
| v1 | macd_12_26_9 | 9756.47 | -243.53 | sell /  / MACD > 신호선 그리고 MACD > 0; 조건 미충족; MACD=-0.0912606, signal9=-0.0161084 |
| v1 | rsi_14_recovery | 9923.04 | -76.96 | sell /  / 직전 RSI14 < 30, 현재 RSI14 >= 30 (한 봉 목표); 조건 미충족; RSI14=40.3665, previous_RSI14=36.2025 |
| v1 | bollinger_20_reentry | 9881.04 | -118.96 | sell /  / 직전 종가 < 직전 하단밴드, 현재 하단밴드 <= 종가 <= SMA20 (한 봉 목표); 조건 미충족; close=251.75, lower20=251.316, SMA20=254.208, previous_lower20=251.691 |
| v1 | donchian_20 | 10000.00 | 0.00 | 대기 /  / 새 신호 대기 |
| v1 | atr_14_breakout | 9883.97 | -116.03 | sell /  / 종가 > 직전 종가 + 직전 ATR14 그리고 종가 > EMA26; 조건 미충족; close=256.72, threshold=258.136, prior_ATR14=1.3158, EMA26=255.146 |
| v1 | session_vwap | 9765.84 | -234.16 | buy /  / 종가 > 뉴욕 거래일별 누적 전형가격 VWAP; 조건 충족; close=252.75, session_VWAP=252.657, session_volume=4.65844e+06 |
| v1 | obv_20 | 9665.44 | -334.56 | buy /  / OBV > OBV의 SMA20 그리고 종가 > EMA26; 조건 충족; OBV=4.74226e+06, OBV_SMA20=3.3149e+06, close=254.07, EMA26=253.729 |
| v1 | stochastic_14_3_recovery | 9862.87 | -137.13 | sell /  / 직전 %K14 < 20에서 %K14가 %D3 상향 돌파 (한 봉 목표); 조건 미충족; K14=28.9392, D3=18.1738, previous_K14=19.7943, previous_D3=12.6561 |
| v1 | mfi_14_recovery | 10000.00 | 0.00 | 대기 /  / 새 신호 대기 |
| v1 | adx_14_trend | 9823.79 | -176.21 | sell /  / Wilder ADX14 >= 25 그리고 +DI14 > -DI14; 조건 미충족; ADX14=24.7842, plus_DI14=27.3963, minus_DI14=19.1477 |
| v1 | aroon_25_trend | 9967.50 | -32.50 | sell /  / Aroon25 Up > 70 그리고 Down < 30 (동률이면 최신 극값); 조건 미충족; Aroon_up=68, Aroon_down=16 |
| v1 | cci_20_momentum | 9935.63 | -64.37 | sell /  / CCI20 > 100 (전형가격·평균절대편차); 조건 미충족; CCI20=62.9489 |
| v1 | williams_14_recovery | 9903.67 | -96.33 | sell /  / 직전 Williams %R14 < -80, 현재 >= -80 (한 봉 목표); 조건 미충족; Williams_R14=-61.3372, previous_R14=-71.0608 |
| v1 | cmf_20_accumulation | 10054.58 | 54.58 | buy /  / Chaikin Money Flow20 > 0.1; 조건 충족; CMF20=0.280188, volume20=5.69706e+06 |
| v1 | chaikin_3_10 | 9884.16 | -115.84 | buy /  / ADL의 EMA3 - EMA10 > 0 그리고 종가 > EMA26; 조건 충족; Chaikin3_10=495361, ADL=4.44077e+06, close=254.07, EMA26=253.729 |
| v1 | roc_10_momentum | 9773.82 | -226.18 | sell /  / 10봉 ROC > 1% 그리고 종가 > EMA26; 조건 미충족; ROC10_percent=0.766776, close=254.29, EMA26=253.836 |
| v1 | trix_15_trend | 9840.00 | -160.00 | sell /  / 15봉 삼중 EMA의 1봉 변화율 TRIX > 0 그리고 종가 > EMA26; 조건 미충족; TRIX15_percent=0.000692295, close=255.155, EMA26=255.356 |
| v1 | keltner_20_breakout | 10000.00 | 0.00 | 대기 /  / 새 신호 대기 |
| v1 | opening_range_30m | 10000.00 | 0.00 | 대기 /  / 새 신호 대기 |
| v2 | cash | 10000.00 | 0.00 | 대기 /  / 새 신호 대기 |
| v2 | buy_hold | 9698.28 | -301.72 | 중단: 손실 한도 / buy / partial / 직전 완료 봉 목표 비중 100%; 다음 봉 시가 가정 |
| v2 | trend_8_26 | 9698.28 | -301.72 | 중단: 손실 한도 / buy / partial / 직전 완료 봉 목표 비중 100%; 다음 봉 시가 가정 |
| v2 | momentum_26 | 9698.28 | -301.72 | 중단: 손실 한도 / buy / partial / 직전 완료 봉 목표 비중 100%; 다음 봉 시가 가정 |
| v2 | breakout_8 | 9343.39 | -656.61 | 중단: 손실 한도 / sell / filled / 직전 완료 봉 목표 비중 0%; 다음 봉 시가 가정 |
| v2 | reversion_12 | 9581.23 | -418.77 | sell / filled / 직전 완료 봉 목표 비중 0%; 다음 봉 시가 가정 |
| v2 | volume_26 | 9672.67 | -327.33 | sell / filled / 직전 완료 봉 목표 비중 0%; 다음 봉 시가 가정 |
| v2 | trend_8_26 AND momentum_26 | 9698.28 | -301.72 | 중단: 손실 한도 / buy / partial / 직전 완료 봉 목표 비중 100%; 다음 봉 시가 가정 |
| v2 | trend_8_26 + momentum_26 | 9698.28 | -301.72 | 중단: 손실 한도 / buy / partial / 직전 완료 봉 목표 비중 100%; 다음 봉 시가 가정 |
| v2 | trend_8_26 AND breakout_8 | 9419.39 | -580.61 | 중단: 손실 한도 / sell / filled / 직전 완료 봉 목표 비중 0%; 다음 봉 시가 가정 |
| v2 | trend_8_26 + breakout_8 | 9348.63 | -651.37 | buy / filled / 직전 완료 봉 목표 비중 50%; 다음 봉 시가 가정 |
| v2 | trend_8_26 AND reversion_12 | 9968.12 | -31.88 | sell / filled / 직전 완료 봉 목표 비중 0%; 다음 봉 시가 가정 |
| v2 | trend_8_26 + reversion_12 | 9732.92 | -267.08 | 중단: 손실 한도 / sell / filled / 직전 완료 봉 목표 비중 0%; 다음 봉 시가 가정 |
| v2 | trend_8_26 AND volume_26 | 9805.21 | -194.79 | sell / filled / 직전 완료 봉 목표 비중 0%; 다음 봉 시가 가정 |
| v2 | trend_8_26 + volume_26 | 9821.91 | -178.09 | 중단: 손실 한도 / buy / filled / 직전 완료 봉 목표 비중 50%; 다음 봉 시가 가정 |
| v2 | momentum_26 AND breakout_8 | 9512.11 | -487.89 | sell / filled / 직전 완료 봉 목표 비중 0%; 다음 봉 시가 가정 |
| v2 | momentum_26 + breakout_8 | 9328.14 | -671.86 | sell / filled / 직전 완료 봉 목표 비중 0%; 다음 봉 시가 가정 |
| v2 | momentum_26 AND reversion_12 | 9938.87 | -61.13 | sell / filled / 직전 완료 봉 목표 비중 0%; 다음 봉 시가 가정 |
| v2 | momentum_26 + reversion_12 | 9732.92 | -267.08 | 중단: 손실 한도 / sell / filled / 직전 완료 봉 목표 비중 0%; 다음 봉 시가 가정 |
| v2 | momentum_26 AND volume_26 | 9920.93 | -79.07 | sell / filled / 직전 완료 봉 목표 비중 0%; 다음 봉 시가 가정 |
| v2 | momentum_26 + volume_26 | 9821.91 | -178.09 | 중단: 손실 한도 / buy / filled / 직전 완료 봉 목표 비중 50%; 다음 봉 시가 가정 |
| v2 | breakout_8 AND reversion_12 | 10000.00 | 0.00 | 대기 /  / 새 신호 대기 |
| v2 | breakout_8 + reversion_12 | 9343.83 | -656.17 | sell / filled / 직전 완료 봉 목표 비중 0%; 다음 봉 시가 가정 |
| v2 | breakout_8 AND volume_26 | 9814.17 | -185.83 | sell / filled / 직전 완료 봉 목표 비중 0%; 다음 봉 시가 가정 |
| v2 | breakout_8 + volume_26 | 9368.55 | -631.45 | sell / filled / 직전 완료 봉 목표 비중 0%; 다음 봉 시가 가정 |
| v2 | reversion_12 AND volume_26 | 9859.15 | -140.85 | sell / filled / 직전 완료 봉 목표 비중 0%; 다음 봉 시가 가정 |
| v2 | reversion_12 + volume_26 | 9667.54 | -332.46 | sell / filled / 직전 완료 봉 목표 비중 0%; 다음 봉 시가 가정 |
| v2 | ema_12_26 | 9777.31 | -222.69 | sell / filled / EMA12 > EMA26; 조건 미충족; EMA12=255.193, EMA26=255.284; 직전 완료 봉 목표를 다음 봉 시가에 모의 적용 |
| v2 | macd_12_26_9 | 9752.57 | -247.43 | sell / filled / MACD > 신호선 그리고 MACD > 0; 조건 미충족; MACD=-0.0912606, signal9=-0.0161084; 직전 완료 봉 목표를 다음 봉 시가에 모의 적용 |
| v2 | rsi_14_recovery | 9919.07 | -80.93 | sell / filled / 직전 RSI14 < 30, 현재 RSI14 >= 30 (한 봉 목표); 조건 미충족; RSI14=40.3665, previous_RSI14=36.2025; 직전 완료 봉 목표를 다음 봉 시가에 모의 적용 |
| v2 | bollinger_20_reentry | 9877.09 | -122.91 | sell / filled / 직전 종가 < 직전 하단밴드, 현재 하단밴드 <= 종가 <= SMA20 (한 봉 목표); 조건 미충족; close=251.75, lower20=251.316, SMA20=254.208, previous_lower20=251.691; 직전 완료 봉 목표를 다음 봉 시가에 모의 적용 |
| v2 | donchian_20 | 10000.00 | 0.00 | 대기 /  / 새 신호 대기 |
| v2 | atr_14_breakout | 9880.02 | -119.98 | sell / filled / 종가 > 직전 종가 + 직전 ATR14 그리고 종가 > EMA26; 조건 미충족; close=256.72, threshold=258.136, prior_ATR14=1.3158, EMA26=255.146; 직전 완료 봉 목표를 다음 봉 시가에 모의 적용 |
| v2 | session_vwap | 9757.06 | -242.94 | buy / partial / 종가 > 뉴욕 거래일별 누적 전형가격 VWAP; 조건 충족; close=252.75, session_VWAP=252.657, session_volume=4.65844e+06; 직전 완료 봉 목표를 다음 봉 시가에 모의 적용 |
| v2 | obv_20 | 9654.81 | -345.19 | buy / partial / OBV > OBV의 SMA20 그리고 종가 > EMA26; 조건 충족; OBV=4.74226e+06, OBV_SMA20=3.3149e+06, close=254.07, EMA26=253.729; 직전 완료 봉 목표를 다음 봉 시가에 모의 적용 |
| v2 | stochastic_14_3_recovery | 9856.96 | -143.04 | sell / filled / 직전 %K14 < 20에서 %K14가 %D3 상향 돌파 (한 봉 목표); 조건 미충족; K14=28.9392, D3=18.1738, previous_K14=19.7943, previous_D3=12.6561; 직전 완료 봉 목표를 다음 봉 시가에 모의 적용 |
| v2 | mfi_14_recovery | 10000.00 | 0.00 | 대기 /  / 새 신호 대기 |
| v2 | adx_14_trend | 9817.90 | -182.10 | sell / filled / Wilder ADX14 >= 25 그리고 +DI14 > -DI14; 조건 미충족; ADX14=24.7842, plus_DI14=27.3963, minus_DI14=19.1477; 직전 완료 봉 목표를 다음 봉 시가에 모의 적용 |
| v2 | aroon_25_trend | 9965.51 | -34.49 | sell / filled / Aroon25 Up > 70 그리고 Down < 30 (동률이면 최신 극값); 조건 미충족; Aroon_up=68, Aroon_down=16; 직전 완료 봉 목표를 다음 봉 시가에 모의 적용 |
| v2 | cci_20_momentum | 9933.64 | -66.36 | sell / filled / CCI20 > 100 (전형가격·평균절대편차); 조건 미충족; CCI20=62.9489; 직전 완료 봉 목표를 다음 봉 시가에 모의 적용 |
| v2 | williams_14_recovery | 9899.71 | -100.29 | sell / filled / 직전 Williams %R14 < -80, 현재 >= -80 (한 봉 목표); 조건 미충족; Williams_R14=-61.3372, previous_R14=-71.0608; 직전 완료 봉 목표를 다음 봉 시가에 모의 적용 |
| v2 | cmf_20_accumulation | 10053.57 | 53.57 | buy / partial / Chaikin Money Flow20 > 0.1; 조건 충족; CMF20=0.280188, volume20=5.69706e+06; 직전 완료 봉 목표를 다음 봉 시가에 모의 적용 |
| v2 | chaikin_3_10 | 9879.22 | -120.78 | buy / partial / ADL의 EMA3 - EMA10 > 0 그리고 종가 > EMA26; 조건 충족; Chaikin3_10=495361, ADL=4.44077e+06, close=254.07, EMA26=253.729; 직전 완료 봉 목표를 다음 봉 시가에 모의 적용 |
| v2 | roc_10_momentum | 9767.96 | -232.04 | sell / filled / 10봉 ROC > 1% 그리고 종가 > EMA26; 조건 미충족; ROC10_percent=0.766776, close=254.29, EMA26=253.836; 직전 완료 봉 목표를 다음 봉 시가에 모의 적용 |
| v2 | trix_15_trend | 9836.06 | -163.94 | sell / filled / 15봉 삼중 EMA의 1봉 변화율 TRIX > 0 그리고 종가 > EMA26; 조건 미충족; TRIX15_percent=0.000692295, close=255.155, EMA26=255.356; 직전 완료 봉 목표를 다음 봉 시가에 모의 적용 |
| v2 | keltner_20_breakout | 10000.00 | 0.00 | 대기 /  / 새 신호 대기 |
| v2 | opening_range_30m | 10000.00 | 0.00 | 대기 /  / 새 신호 대기 |

### 같은 기간의 비용·노출 비교 (사후 연구)

| 전략 | 비용 전 | 비용 후 | 100% 보유 | 같은 평균 노출 보유 | 평균 노출 |
|---|---:|---:|---:|---:|---:|
| cash | 0.00% | 0.00% | -5.48% | -0.00% | 0.00% |
| buy_hold | -5.08% | -5.48% | -5.48% | -5.48% | 100.00% |
| trend_8_26 | 1.30% | -1.22% | -5.48% | -2.47% | 43.98% |
| momentum_26 | 0.22% | -3.09% | -5.48% | -2.41% | 42.93% |
| breakout_8 | -1.24% | -18.25% | -5.48% | -1.14% | 20.16% |
| reversion_12 | -7.36% | -15.18% | -5.48% | -1.74% | 30.89% |
| volume_26 | -1.90% | -8.28% | -5.48% | -0.36% | 6.28% |
| trend_8_26 AND momentum_26 | 1.48% | -1.46% | -5.48% | -2.12% | 37.70% |
| trend_8_26 + momentum_26 | 0.76% | -2.16% | -5.48% | -2.44% | 43.46% |
| trend_8_26 AND breakout_8 | 0.57% | -10.59% | -5.48% | -0.74% | 13.09% |
| trend_8_26 + breakout_8 | 0.05% | -9.93% | -5.48% | -1.81% | 32.07% |
| trend_8_26 AND reversion_12 | 0.87% | -2.05% | -5.48% | -0.30% | 5.24% |
| trend_8_26 + reversion_12 | -3.09% | -8.07% | -5.48% | -2.11% | 37.44% |
| trend_8_26 AND volume_26 | 0.41% | -1.67% | -5.48% | -0.07% | 1.31% |
| trend_8_26 + volume_26 | -0.28% | -4.60% | -5.48% | -1.42% | 25.13% |
| momentum_26 AND breakout_8 | 1.38% | -9.11% | -5.48% | -0.71% | 12.57% |
| momentum_26 + breakout_8 | -0.49% | -10.79% | -5.48% | -1.78% | 31.55% |
| momentum_26 AND reversion_12 | -0.82% | -2.88% | -5.48% | -0.31% | 5.50% |
| momentum_26 + reversion_12 | -3.61% | -8.76% | -5.48% | -2.08% | 36.91% |
| momentum_26 AND volume_26 | 0.14% | -0.70% | -5.48% | -0.03% | 0.52% |
| momentum_26 + volume_26 | -0.82% | -4.91% | -5.48% | -1.39% | 24.61% |
| breakout_8 AND reversion_12 | 0.00% | 0.00% | -5.48% | -0.00% | 0.00% |
| breakout_8 + reversion_12 | -4.33% | -16.21% | -5.48% | -1.44% | 25.53% |
| breakout_8 AND volume_26 | -0.91% | -2.15% | -5.48% | -0.04% | 0.79% |
| breakout_8 + volume_26 | -1.56% | -12.68% | -5.48% | -0.75% | 13.23% |
| reversion_12 AND volume_26 | -1.84% | -4.69% | -5.48% | -0.16% | 2.88% |
| reversion_12 + volume_26 | -4.65% | -11.05% | -5.48% | -1.05% | 18.59% |
| ema_12_26 | -1.34% | -3.39% | -5.48% | -2.14% | 37.96% |
| macd_12_26_9 | 4.01% | 1.42% | -5.48% | -1.41% | 24.87% |
| rsi_14_recovery | -1.66% | -7.67% | -5.48% | -0.22% | 3.93% |
| bollinger_20_reentry | -0.95% | -5.82% | -5.48% | -0.18% | 3.14% |
| donchian_20 | 0.63% | -6.31% | -5.48% | -0.37% | 6.54% |
| atr_14_breakout | 1.19% | -4.59% | -5.48% | -0.25% | 4.45% |
| session_vwap | 1.65% | -5.75% | -5.48% | -2.55% | 45.55% |
| obv_20 | -5.89% | -14.55% | -5.48% | -1.67% | 29.58% |
| stochastic_14_3_recovery | -0.24% | -12.79% | -5.48% | -0.48% | 8.38% |
| mfi_14_recovery | 0.33% | -0.93% | -5.48% | -0.04% | 0.79% |
| adx_14_trend | -2.56% | -7.35% | -5.48% | -1.76% | 31.15% |
| aroon_25_trend | 4.10% | 0.24% | -5.48% | -1.54% | 27.23% |
| cci_20_momentum | 0.59% | -5.56% | -5.48% | -1.13% | 19.90% |
| williams_14_recovery | -1.46% | -9.40% | -5.48% | -0.30% | 5.24% |
| cmf_20_accumulation | 3.32% | -0.51% | -5.48% | -1.48% | 26.18% |
| chaikin_3_10 | -3.28% | -8.04% | -5.48% | -1.74% | 30.89% |
| roc_10_momentum | -2.36% | -8.70% | -5.48% | -0.85% | 14.92% |
| trix_15_trend | -0.23% | -2.31% | -5.48% | -1.63% | 28.80% |
| keltner_20_breakout | 0.65% | -2.68% | -5.48% | -0.52% | 9.16% |
| opening_range_30m | 0.79% | -2.95% | -5.48% | -1.47% | 25.92% |

동일 구간·초기 자금, 종료 시 청산 비용 포함. 노출 맞춤은 사후 설명용이며 v2 실제 계좌 성과가 아닙니다.
[낙폭 분해·비용 영향·전체 구간](JNJ/comparison.json)

[v1 전체 기록](JNJ/accounts.json) · [v2 전체 기록](JNJ/accounts-v2.json)

## CAT 계좌

| 모델 | 전략 | 평가액 USD | 손익 USD | 최근 매매·이유 |
|---|---|---:|---:|---|
| v1 | cash | 10000.00 | 0.00 | 대기 /  / 새 신호 대기 |
| v1 | buy_hold | 9878.38 | -121.62 | buy /  / buy_hold: prior completed bar target 100%; next bar open simulation |
| v1 | trend_8_26 | 9909.54 | -90.46 | sell /  / trend_8_26: prior completed bar target 0%; next bar open simulation |
| v1 | momentum_26 | 9872.70 | -127.30 | sell /  / momentum_26: prior completed bar target 0%; next bar open simulation |
| v1 | breakout_8 | 9790.00 | -210.00 | sell /  / breakout_8: prior completed bar target 0%; next bar open simulation |
| v1 | reversion_12 | 9830.10 | -169.90 | sell /  / reversion_12: prior completed bar target 0%; next bar open simulation |
| v1 | volume_26 | 10000.00 | 0.00 | 대기 /  / 새 신호 대기 |
| v1 | trend_8_26 AND momentum_26 | 9873.91 | -126.09 | sell /  / trend_8_26 AND momentum_26: prior completed bar target 0%; next bar open simulation |
| v1 | trend_8_26 + momentum_26 | 9891.24 | -108.76 | sell /  / trend_8_26 + momentum_26: prior completed bar target 0%; next bar open simulation |
| v1 | trend_8_26 AND breakout_8 | 9850.32 | -149.68 | sell /  / trend_8_26 AND breakout_8: prior completed bar target 0%; next bar open simulation |
| v1 | trend_8_26 + breakout_8 | 9849.76 | -150.24 | sell /  / trend_8_26 + breakout_8: prior completed bar target 0%; next bar open simulation |
| v1 | trend_8_26 AND reversion_12 | 9928.06 | -71.94 | sell /  / trend_8_26 AND reversion_12: prior completed bar target 0%; next bar open simulation |
| v1 | trend_8_26 + reversion_12 | 9890.14 | -109.86 | sell /  / trend_8_26 + reversion_12: prior completed bar target 0%; next bar open simulation |
| v1 | trend_8_26 AND volume_26 | 10000.00 | 0.00 | 대기 /  / 새 신호 대기 |
| v1 | trend_8_26 + volume_26 | 9954.72 | -45.28 | sell /  / trend_8_26 + volume_26: prior completed bar target 0%; next bar open simulation |
| v1 | momentum_26 AND breakout_8 | 9850.32 | -149.68 | sell /  / momentum_26 AND breakout_8: prior completed bar target 0%; next bar open simulation |
| v1 | momentum_26 + breakout_8 | 9831.28 | -168.72 | sell /  / momentum_26 + breakout_8: prior completed bar target 0%; next bar open simulation |
| v1 | momentum_26 AND reversion_12 | 9887.21 | -112.79 | sell /  / momentum_26 AND reversion_12: prior completed bar target 0%; next bar open simulation |
| v1 | momentum_26 + reversion_12 | 9851.97 | -148.03 | sell /  / momentum_26 + reversion_12: prior completed bar target 0%; next bar open simulation |
| v1 | momentum_26 AND volume_26 | 10000.00 | 0.00 | 대기 /  / 새 신호 대기 |
| v1 | momentum_26 + volume_26 | 9936.12 | -63.88 | sell /  / momentum_26 + volume_26: prior completed bar target 0%; next bar open simulation |
| v1 | breakout_8 AND reversion_12 | 10000.00 | 0.00 | 대기 /  / 새 신호 대기 |
| v1 | breakout_8 + reversion_12 | 9810.52 | -189.48 | sell /  / breakout_8 + reversion_12: prior completed bar target 0%; next bar open simulation |
| v1 | breakout_8 AND volume_26 | 10000.00 | 0.00 | 대기 /  / 새 신호 대기 |
| v1 | breakout_8 + volume_26 | 9894.44 | -105.56 | sell /  / breakout_8 + volume_26: prior completed bar target 0%; next bar open simulation |
| v1 | reversion_12 AND volume_26 | 10000.00 | 0.00 | 대기 /  / 새 신호 대기 |
| v1 | reversion_12 + volume_26 | 9915.19 | -84.81 | sell /  / reversion_12 + volume_26: prior completed bar target 0%; next bar open simulation |
| v1 | ema_12_26 | 9862.47 | -137.53 | sell /  / EMA12 > EMA26; 조건 미충족; EMA12=735.622, EMA26=735.711 |
| v1 | macd_12_26_9 | 9904.18 | -95.82 | sell /  / MACD > 신호선 그리고 MACD > 0; 조건 미충족; MACD=0.746548, signal9=0.752293 |
| v1 | rsi_14_recovery | 9986.99 | -13.01 | sell /  / 직전 RSI14 < 30, 현재 RSI14 >= 30 (한 봉 목표); 조건 미충족; RSI14=42.2805, previous_RSI14=38.7468 |
| v1 | bollinger_20_reentry | 9765.13 | -234.87 | sell /  / 직전 종가 < 직전 하단밴드, 현재 하단밴드 <= 종가 <= SMA20 (한 봉 목표); 조건 미충족; close=727.35, lower20=723.447, SMA20=732.513, previous_lower20=723.966 |
| v1 | donchian_20 | 9950.83 | -49.17 | sell /  / 종가 > 현재 봉을 제외한 직전 20봉 최고가; 조건 미충족; close=739.81, prior_high20=742.28 |
| v1 | atr_14_breakout | 9790.00 | -210.00 | sell /  / 종가 > 직전 종가 + 직전 ATR14 그리고 종가 > EMA26; 조건 미충족; close=731.995, threshold=738.753, prior_ATR14=5.19827, EMA26=730.642 |
| v1 | session_vwap | 9628.53 | -371.47 | sell /  / 종가 > 뉴욕 거래일별 누적 전형가격 VWAP; 조건 미충족; close=726.49, session_VWAP=726.913, session_volume=1.42484e+06 |
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
| v2 | buy_hold | 9084.89 | -915.11 | 중단: 손실 한도 / buy / partial / 직전 완료 봉 목표 비중 100%; 다음 봉 시가 가정 |
| v2 | trend_8_26 | 9831.00 | -169.00 | sell / filled / 직전 완료 봉 목표 비중 0%; 다음 봉 시가 가정 |
| v2 | momentum_26 | 9885.12 | -114.88 | sell / filled / 직전 완료 봉 목표 비중 0%; 다음 봉 시가 가정 |
| v2 | breakout_8 | 9610.96 | -389.04 | sell / filled / 직전 완료 봉 목표 비중 0%; 다음 봉 시가 가정 |
| v2 | reversion_12 | 8958.02 | -1041.98 | 중단: 손실 한도 / buy / partial / 직전 완료 봉 목표 비중 100%; 다음 봉 시가 가정 |
| v2 | volume_26 | 9214.21 | -785.79 | 중단: 손실 한도 / buy / partial / 직전 완료 봉 목표 비중 100%; 다음 봉 시가 가정 |
| v2 | trend_8_26 AND momentum_26 | 9914.96 | -85.04 | sell / filled / 직전 완료 봉 목표 비중 0%; 다음 봉 시가 가정 |
| v2 | trend_8_26 + momentum_26 | 9858.16 | -141.84 | sell / filled / 직전 완료 봉 목표 비중 0%; 다음 봉 시가 가정 |
| v2 | trend_8_26 AND breakout_8 | 9765.08 | -234.92 | sell / filled / 직전 완료 봉 목표 비중 0%; 다음 봉 시가 가정 |
| v2 | trend_8_26 + breakout_8 | 9720.80 | -279.20 | sell / filled / 직전 완료 봉 목표 비중 0%; 다음 봉 시가 가정 |
| v2 | trend_8_26 AND reversion_12 | 9738.62 | -261.38 | sell / filled / 직전 완료 봉 목표 비중 0%; 다음 봉 시가 가정 |
| v2 | trend_8_26 + reversion_12 | 9511.82 | -488.18 | sell / filled / 직전 완료 봉 목표 비중 0%; 다음 봉 시가 가정 |
| v2 | trend_8_26 AND volume_26 | 10035.44 | 35.44 | sell / filled / 직전 완료 봉 목표 비중 0%; 다음 봉 시가 가정 |
| v2 | trend_8_26 + volume_26 | 9587.50 | -412.50 | sell / filled / 직전 완료 봉 목표 비중 0%; 다음 봉 시가 가정 |
| v2 | momentum_26 AND breakout_8 | 9824.16 | -175.84 | sell / filled / 직전 완료 봉 목표 비중 0%; 다음 봉 시가 가정 |
| v2 | momentum_26 + breakout_8 | 9747.29 | -252.71 | sell / filled / 직전 완료 봉 목표 비중 0%; 다음 봉 시가 가정 |
| v2 | momentum_26 AND reversion_12 | 9755.55 | -244.45 | sell / filled / 직전 완료 봉 목표 비중 0%; 다음 봉 시가 가정 |
| v2 | momentum_26 + reversion_12 | 9517.90 | -482.10 | sell / filled / 직전 완료 봉 목표 비중 0%; 다음 봉 시가 가정 |
| v2 | momentum_26 AND volume_26 | 10048.78 | 48.78 | sell / filled / 직전 완료 봉 목표 비중 0%; 다음 봉 시가 가정 |
| v2 | momentum_26 + volume_26 | 9633.99 | -366.01 | sell / filled / 직전 완료 봉 목표 비중 0%; 다음 봉 시가 가정 |
| v2 | breakout_8 AND reversion_12 | 10000.00 | 0.00 | 대기 /  / 새 신호 대기 |
| v2 | breakout_8 + reversion_12 | 9610.18 | -389.82 | 중단: 손실 한도 / sell / filled / 직전 완료 봉 목표 비중 0%; 다음 봉 시가 가정 |
| v2 | breakout_8 AND volume_26 | 9998.69 | -1.31 | sell / filled / 직전 완료 봉 목표 비중 0%; 다음 봉 시가 가정 |
| v2 | breakout_8 + volume_26 | 9499.63 | -500.37 | sell / filled / 직전 완료 봉 목표 비중 0%; 다음 봉 시가 가정 |
| v2 | reversion_12 AND volume_26 | 9150.47 | -849.53 | 중단: 손실 한도 / buy / partial / 직전 완료 봉 목표 비중 100%; 다음 봉 시가 가정 |
| v2 | reversion_12 + volume_26 | 9341.20 | -658.80 | 중단: 손실 한도 / sell / filled / 직전 완료 봉 목표 비중 50%; 다음 봉 시가 가정 |
| v2 | ema_12_26 | 9860.50 | -139.50 | sell / filled / EMA12 > EMA26; 조건 미충족; EMA12=735.622, EMA26=735.711; 직전 완료 봉 목표를 다음 봉 시가에 모의 적용 |
| v2 | macd_12_26_9 | 9902.20 | -97.80 | sell / filled / MACD > 신호선 그리고 MACD > 0; 조건 미충족; MACD=0.746548, signal9=0.752293; 직전 완료 봉 목표를 다음 봉 시가에 모의 적용 |
| v2 | rsi_14_recovery | 9984.99 | -15.01 | sell / filled / 직전 RSI14 < 30, 현재 RSI14 >= 30 (한 봉 목표); 조건 미충족; RSI14=42.2805, previous_RSI14=38.7468; 직전 완료 봉 목표를 다음 봉 시가에 모의 적용 |
| v2 | bollinger_20_reentry | 9761.22 | -238.78 | sell / filled / 직전 종가 < 직전 하단밴드, 현재 하단밴드 <= 종가 <= SMA20 (한 봉 목표); 조건 미충족; close=727.35, lower20=723.447, SMA20=732.513, previous_lower20=723.966; 직전 완료 봉 목표를 다음 봉 시가에 모의 적용 |
| v2 | donchian_20 | 9948.84 | -51.16 | sell / filled / 종가 > 현재 봉을 제외한 직전 20봉 최고가; 조건 미충족; close=739.81, prior_high20=742.28; 직전 완료 봉 목표를 다음 봉 시가에 모의 적용 |
| v2 | atr_14_breakout | 9784.13 | -215.87 | sell / filled / 종가 > 직전 종가 + 직전 ATR14 그리고 종가 > EMA26; 조건 미충족; close=731.995, threshold=738.753, prior_ATR14=5.19827, EMA26=730.642; 직전 완료 봉 목표를 다음 봉 시가에 모의 적용 |
| v2 | session_vwap | 9616.98 | -383.02 | sell / filled / 종가 > 뉴욕 거래일별 누적 전형가격 VWAP; 조건 미충족; close=726.49, session_VWAP=726.913, session_volume=1.42484e+06; 직전 완료 봉 목표를 다음 봉 시가에 모의 적용 |
| v2 | obv_20 | 9809.44 | -190.56 | sell / filled / OBV > OBV의 SMA20 그리고 종가 > EMA26; 조건 미충족; OBV=-3.10102e+06, OBV_SMA20=-4.20035e+06, close=734.925, EMA26=736.093; 직전 완료 봉 목표를 다음 봉 시가에 모의 적용 |
| v2 | stochastic_14_3_recovery | 9833.19 | -166.81 | sell / filled / 직전 %K14 < 20에서 %K14가 %D3 상향 돌파 (한 봉 목표); 조건 미충족; K14=70.1066, D3=41.8677, previous_K14=37.4769, previous_D3=26.7366; 직전 완료 봉 목표를 다음 봉 시가에 모의 적용 |
| v2 | mfi_14_recovery | 10054.30 | 54.30 | sell / filled / 직전 MFI14 < 20, 현재 MFI14 >= 20 (한 봉 목표); 조건 미충족; MFI14=34.3275, previous_MFI14=29.4992; 직전 완료 봉 목표를 다음 봉 시가에 모의 적용 |
| v2 | adx_14_trend | 10000.00 | 0.00 | 대기 /  / 새 신호 대기 |
| v2 | aroon_25_trend | 10029.14 | 29.14 | sell / filled / Aroon25 Up > 70 그리고 Down < 30 (동률이면 최신 극값); 조건 미충족; Aroon_up=88, Aroon_down=48; 직전 완료 봉 목표를 다음 봉 시가에 모의 적용 |
| v2 | cci_20_momentum | 10022.77 | 22.77 | sell / filled / CCI20 > 100 (전형가격·평균절대편차); 조건 미충족; CCI20=98.8062; 직전 완료 봉 목표를 다음 봉 시가에 모의 적용 |
| v2 | williams_14_recovery | 9988.83 | -11.17 | sell / filled / 직전 Williams %R14 < -80, 현재 >= -80 (한 봉 목표); 조건 미충족; Williams_R14=-29.8934, previous_R14=-62.5231; 직전 완료 봉 목표를 다음 봉 시가에 모의 적용 |
| v2 | cmf_20_accumulation | 9838.82 | -161.18 | sell / filled / Chaikin Money Flow20 > 0.1; 조건 미충족; CMF20=-0.0799774, volume20=4.73159e+06; 직전 완료 봉 목표를 다음 봉 시가에 모의 적용 |
| v2 | chaikin_3_10 | 9567.72 | -432.28 | 중단: 손실 한도 / buy / partial / ADL의 EMA3 - EMA10 > 0 그리고 종가 > EMA26; 조건 충족; Chaikin3_10=293683, ADL=-4.91156e+06, close=739.58, EMA26=736.187; 직전 완료 봉 목표를 다음 봉 시가에 모의 적용 |
| v2 | roc_10_momentum | 9961.14 | -38.86 | sell / filled / 10봉 ROC > 1% 그리고 종가 > EMA26; 조건 미충족; ROC10_percent=-0.134597, close=734.53, EMA26=735.486; 직전 완료 봉 목표를 다음 봉 시가에 모의 적용 |
| v2 | trix_15_trend | 9577.36 | -422.64 | 중단: 손실 한도 / buy / partial / 15봉 삼중 EMA의 1봉 변화율 TRIX > 0 그리고 종가 > EMA26; 조건 충족; TRIX15_percent=0.0196284, close=739.58, EMA26=736.187; 직전 완료 봉 목표를 다음 봉 시가에 모의 적용 |
| v2 | keltner_20_breakout | 10000.00 | 0.00 | 대기 /  / 새 신호 대기 |
| v2 | opening_range_30m | 10038.70 | 38.70 | sell / filled / 뉴욕 09:30·09:45 두 완료 봉 최고가를 10:00 이후 종가가 돌파; 자료 부족·변동폭 또는 거래량 없음: 대기; close=740.21; 직전 완료 봉 목표를 다음 봉 시가에 모의 적용 |

### 같은 기간의 비용·노출 비교 (사후 연구)

| 전략 | 비용 전 | 비용 후 | 100% 보유 | 같은 평균 노출 보유 | 평균 노출 |
|---|---:|---:|---:|---:|---:|
| cash | 0.00% | 0.00% | -12.17% | -0.00% | 0.00% |
| buy_hold | -11.80% | -12.17% | -12.17% | -12.17% | 100.00% |
| trend_8_26 | -1.27% | -4.93% | -12.17% | -5.59% | 45.03% |
| momentum_26 | -2.55% | -6.56% | -12.17% | -5.56% | 44.76% |
| breakout_8 | -2.74% | -14.61% | -12.17% | -1.77% | 14.14% |
| reversion_12 | -3.79% | -16.94% | -12.17% | -3.50% | 28.01% |
| volume_26 | -3.36% | -9.26% | -12.17% | -0.89% | 7.07% |
| trend_8_26 AND momentum_26 | 0.21% | -2.69% | -12.17% | -4.85% | 39.01% |
| trend_8_26 + momentum_26 | -1.90% | -5.74% | -12.17% | -5.57% | 44.90% |
| trend_8_26 AND breakout_8 | -1.65% | -8.04% | -12.17% | -0.86% | 6.81% |
| trend_8_26 + breakout_8 | -1.98% | -9.69% | -12.17% | -3.69% | 29.59% |
| trend_8_26 AND reversion_12 | 0.56% | -5.98% | -12.17% | -0.79% | 6.28% |
| trend_8_26 + reversion_12 | -2.47% | -10.36% | -12.17% | -4.55% | 36.52% |
| trend_8_26 AND volume_26 | 1.79% | 0.09% | -12.17% | -0.20% | 1.57% |
| trend_8_26 + volume_26 | -2.27% | -6.90% | -12.17% | -3.25% | 26.05% |
| momentum_26 AND breakout_8 | -2.08% | -8.83% | -12.17% | -0.92% | 7.33% |
| momentum_26 + breakout_8 | -2.61% | -10.65% | -12.17% | -3.68% | 29.46% |
| momentum_26 AND reversion_12 | -2.51% | -8.84% | -12.17% | -0.82% | 6.54% |
| momentum_26 + reversion_12 | -3.11% | -11.14% | -12.17% | -4.53% | 36.39% |
| momentum_26 AND volume_26 | 1.50% | 0.22% | -12.17% | -0.13% | 1.05% |
| momentum_26 + volume_26 | -2.90% | -7.50% | -12.17% | -3.24% | 25.92% |
| breakout_8 AND reversion_12 | 0.00% | 0.00% | -12.17% | -0.00% | 0.00% |
| breakout_8 + reversion_12 | -3.21% | -14.87% | -12.17% | -2.64% | 21.08% |
| breakout_8 AND volume_26 | 0.41% | -0.01% | -12.17% | -0.03% | 0.26% |
| breakout_8 + volume_26 | -3.02% | -11.41% | -12.17% | -1.33% | 10.61% |
| reversion_12 AND volume_26 | -1.40% | -5.45% | -12.17% | -0.63% | 4.97% |
| reversion_12 + volume_26 | -3.53% | -12.62% | -12.17% | -2.20% | 17.55% |
| ema_12_26 | -2.07% | -4.10% | -12.17% | -5.36% | 43.19% |
| macd_12_26_9 | 1.55% | -1.40% | -12.17% | -3.33% | 26.70% |
| rsi_14_recovery | -0.69% | -6.36% | -12.17% | -0.46% | 3.66% |
| bollinger_20_reentry | -0.24% | -6.33% | -12.17% | -0.49% | 3.93% |
| donchian_20 | -1.16% | -4.82% | -12.17% | -0.56% | 4.45% |
| atr_14_breakout | -1.81% | -7.81% | -12.17% | -0.53% | 4.19% |
| session_vwap | 0.42% | -11.47% | -12.17% | -5.40% | 43.46% |
| obv_20 | -3.68% | -12.91% | -12.17% | -2.82% | 22.51% |
| stochastic_14_3_recovery | -2.99% | -14.12% | -12.17% | -0.95% | 7.59% |
| mfi_14_recovery | 1.43% | -1.10% | -12.17% | -0.20% | 1.57% |
| adx_14_trend | -2.02% | -4.05% | -12.17% | -1.05% | 8.38% |
| aroon_25_trend | -0.78% | -4.46% | -12.17% | -1.54% | 12.30% |
| cci_20_momentum | -3.92% | -9.02% | -12.17% | -1.77% | 14.14% |
| williams_14_recovery | -0.65% | -10.18% | -12.17% | -0.79% | 6.28% |
| cmf_20_accumulation | -5.07% | -11.61% | -12.17% | -2.00% | 15.97% |
| chaikin_3_10 | -5.60% | -14.65% | -12.17% | -3.82% | 30.63% |
| roc_10_momentum | -1.79% | -7.40% | -12.17% | -1.58% | 12.57% |
| trix_15_trend | -1.21% | -5.67% | -12.17% | -4.21% | 33.77% |
| keltner_20_breakout | -2.87% | -5.29% | -12.17% | -0.33% | 2.62% |
| opening_range_30m | 6.14% | 1.77% | -12.17% | -2.49% | 19.90% |

동일 구간·초기 자금, 종료 시 청산 비용 포함. 노출 맞춤은 사후 설명용이며 v2 실제 계좌 성과가 아닙니다.
[낙폭 분해·비용 영향·전체 구간](CAT/comparison.json)

[v1 전체 기록](CAT/accounts.json) · [v2 전체 기록](CAT/accounts-v2.json)

## WMT 계좌

| 모델 | 전략 | 평가액 USD | 손익 USD | 최근 매매·이유 |
|---|---|---:|---:|---|
| v1 | cash | 10000.00 | 0.00 | 대기 /  / 새 신호 대기 |
| v1 | buy_hold | 10067.04 | 67.04 | buy /  / buy_hold: prior completed bar target 100%; next bar open simulation |
| v1 | trend_8_26 | 9884.03 | -115.97 | buy /  / trend_8_26: prior completed bar target 100%; next bar open simulation |
| v1 | momentum_26 | 9878.47 | -121.53 | buy /  / momentum_26: prior completed bar target 100%; next bar open simulation |
| v1 | breakout_8 | 9791.36 | -208.64 | sell /  / breakout_8: prior completed bar target 0%; next bar open simulation |
| v1 | reversion_12 | 9916.28 | -83.72 | sell /  / reversion_12: prior completed bar target 0%; next bar open simulation |
| v1 | volume_26 | 9915.76 | -84.24 | sell /  / volume_26: prior completed bar target 0%; next bar open simulation |
| v1 | trend_8_26 AND momentum_26 | 9888.82 | -111.18 | buy /  / trend_8_26 AND momentum_26: prior completed bar target 100%; next bar open simulation |
| v1 | trend_8_26 + momentum_26 | 9881.28 | -118.72 | buy /  / trend_8_26 + momentum_26: prior completed bar target 100%; next bar open simulation |
| v1 | trend_8_26 AND breakout_8 | 9917.79 | -82.21 | sell /  / trend_8_26 AND breakout_8: prior completed bar target 0%; next bar open simulation |
| v1 | trend_8_26 + breakout_8 | 9837.50 | -162.50 | sell /  / trend_8_26 + breakout_8: prior completed bar target 50%; next bar open simulation |
| v1 | trend_8_26 AND reversion_12 | 9967.64 | -32.36 | sell /  / trend_8_26 AND reversion_12: prior completed bar target 0%; next bar open simulation |
| v1 | trend_8_26 + reversion_12 | 9919.87 | -80.13 | buy /  / trend_8_26 + reversion_12: prior completed bar target 50%; next bar open simulation |
| v1 | trend_8_26 AND volume_26 | 10000.00 | 0.00 | 대기 /  / 새 신호 대기 |
| v1 | trend_8_26 + volume_26 | 9899.77 | -100.23 | buy /  / trend_8_26 + volume_26: prior completed bar target 50%; next bar open simulation |
| v1 | momentum_26 AND breakout_8 | 9879.45 | -120.55 | sell /  / momentum_26 AND breakout_8: prior completed bar target 0%; next bar open simulation |
| v1 | momentum_26 + breakout_8 | 9894.06 | -105.94 | sell /  / momentum_26 + breakout_8: prior completed bar target 50%; next bar open simulation |
| v1 | momentum_26 AND reversion_12 | 10011.47 | 11.47 | sell /  / momentum_26 AND reversion_12: prior completed bar target 0%; next bar open simulation |
| v1 | momentum_26 + reversion_12 | 9936.88 | -63.12 | buy /  / momentum_26 + reversion_12: prior completed bar target 50%; next bar open simulation |
| v1 | momentum_26 AND volume_26 | 10013.52 | 13.52 | sell /  / momentum_26 AND volume_26: prior completed bar target 0%; next bar open simulation |
| v1 | momentum_26 + volume_26 | 9916.83 | -83.17 | buy /  / momentum_26 + volume_26: prior completed bar target 50%; next bar open simulation |
| v1 | breakout_8 AND reversion_12 | 10000.00 | 0.00 | 대기 /  / 새 신호 대기 |
| v1 | breakout_8 + reversion_12 | 9873.31 | -126.69 | sell /  / breakout_8 + reversion_12: prior completed bar target 0%; next bar open simulation |
| v1 | breakout_8 AND volume_26 | 9913.57 | -86.43 | sell /  / breakout_8 AND volume_26: prior completed bar target 0%; next bar open simulation |
| v1 | breakout_8 + volume_26 | 9853.42 | -146.58 | sell /  / breakout_8 + volume_26: prior completed bar target 0%; next bar open simulation |
| v1 | reversion_12 AND volume_26 | 10000.00 | 0.00 | 대기 /  / 새 신호 대기 |
| v1 | reversion_12 + volume_26 | 9955.79 | -44.21 | sell /  / reversion_12 + volume_26: prior completed bar target 0%; next bar open simulation |
| v1 | ema_12_26 | 9999.84 | -0.16 | buy /  / EMA12 > EMA26; 조건 충족; EMA12=118.628, EMA26=118.619 |
| v1 | macd_12_26_9 | 10012.38 | 12.38 | buy /  / MACD > 신호선 그리고 MACD > 0; 조건 충족; MACD=0.00919902, signal9=-0.00852776 |
| v1 | rsi_14_recovery | 10000.00 | 0.00 | 대기 /  / 새 신호 대기 |
| v1 | bollinger_20_reentry | 10000.00 | 0.00 | 대기 /  / 새 신호 대기 |
| v1 | donchian_20 | 10000.00 | 0.00 | 대기 /  / 새 신호 대기 |
| v1 | atr_14_breakout | 9979.72 | -20.28 | sell /  / 종가 > 직전 종가 + 직전 ATR14 그리고 종가 > EMA26; 조건 미충족; close=119.375, threshold=119.607, prior_ATR14=0.486823, EMA26=118.217 |
| v1 | session_vwap | 9751.17 | -248.83 | buy /  / 종가 > 뉴욕 거래일별 누적 전형가격 VWAP; 조건 충족; close=118.68, session_VWAP=118.618, session_volume=1.15133e+07 |
| v1 | obv_20 | 9880.45 | -119.55 | buy /  / OBV > OBV의 SMA20 그리고 종가 > EMA26; 조건 충족; OBV=2.23382e+07, OBV_SMA20=1.748e+07, close=118.68, EMA26=118.585 |
| v1 | stochastic_14_3_recovery | 9979.72 | -20.28 | sell /  / 직전 %K14 < 20에서 %K14가 %D3 상향 돌파 (한 봉 목표); 조건 미충족; K14=93.8952, D3=60.8222, previous_K14=82.4242, previous_D3=34.5012 |
| v1 | mfi_14_recovery | 10000.00 | 0.00 | 대기 /  / 새 신호 대기 |
| v1 | adx_14_trend | 9991.69 | -8.31 | sell /  / Wilder ADX14 >= 25 그리고 +DI14 > -DI14; 조건 미충족; ADX14=24.5142, plus_DI14=24.7537, minus_DI14=21.6519 |
| v1 | aroon_25_trend | 9973.75 | -26.25 | buy /  / Aroon25 Up > 70 그리고 Down < 30 (동률이면 최신 극값); 조건 충족; Aroon_up=100, Aroon_down=28 |
| v1 | cci_20_momentum | 9928.96 | -71.04 | buy /  / CCI20 > 100 (전형가격·평균절대편차); 조건 충족; CCI20=148.633 |
| v1 | williams_14_recovery | 9979.72 | -20.28 | sell /  / 직전 Williams %R14 < -80, 현재 >= -80 (한 봉 목표); 조건 미충족; Williams_R14=-6.10484, previous_R14=-17.5758 |
| v1 | cmf_20_accumulation | 9909.24 | -90.76 | buy /  / Chaikin Money Flow20 > 0.1; 조건 충족; CMF20=0.112667, volume20=1.57051e+07 |
| v1 | chaikin_3_10 | 9738.91 | -261.09 | buy /  / ADL의 EMA3 - EMA10 > 0 그리고 종가 > EMA26; 조건 충족; Chaikin3_10=395736, ADL=1.91464e+07, close=118.68, EMA26=118.585 |
| v1 | roc_10_momentum | 10000.00 | 0.00 | 대기 /  / 새 신호 대기 |
| v1 | trix_15_trend | 9798.52 | -201.48 | buy /  / 15봉 삼중 EMA의 1봉 변화율 TRIX > 0 그리고 종가 > EMA26; 조건 충족; TRIX15_percent=0.00139768, close=119.24, EMA26=118.719 |
| v1 | keltner_20_breakout | 10000.00 | 0.00 | 대기 /  / 새 신호 대기 |
| v1 | opening_range_30m | 9973.75 | -26.25 | buy /  / 뉴욕 09:30·09:45 두 완료 봉 최고가를 10:00 이후 종가가 돌파; 조건 충족; close=119.24, opening_high=119.14 |
| v2 | cash | 10000.00 | 0.00 | 대기 /  / 새 신호 대기 |
| v2 | buy_hold | 10665.93 | 665.93 | buy / partial / 직전 완료 봉 목표 비중 100%; 다음 봉 시가 가정 |
| v2 | trend_8_26 | 10284.75 | 284.75 | buy / partial / 직전 완료 봉 목표 비중 100%; 다음 봉 시가 가정 |
| v2 | momentum_26 | 10283.83 | 283.83 | buy / partial / 직전 완료 봉 목표 비중 100%; 다음 봉 시가 가정 |
| v2 | breakout_8 | 9746.99 | -253.01 | sell / filled / 직전 완료 봉 목표 비중 0%; 다음 봉 시가 가정 |
| v2 | reversion_12 | 9818.63 | -181.37 | sell / filled / 직전 완료 봉 목표 비중 0%; 다음 봉 시가 가정 |
| v2 | volume_26 | 9875.40 | -124.60 | sell / filled / 직전 완료 봉 목표 비중 0%; 다음 봉 시가 가정 |
| v2 | trend_8_26 AND momentum_26 | 10289.73 | 289.73 | buy / partial / 직전 완료 봉 목표 비중 100%; 다음 봉 시가 가정 |
| v2 | trend_8_26 + momentum_26 | 10284.27 | 284.27 | buy / partial / 직전 완료 봉 목표 비중 100%; 다음 봉 시가 가정 |
| v2 | trend_8_26 AND breakout_8 | 10001.61 | 1.61 | sell / filled / 직전 완료 봉 목표 비중 0%; 다음 봉 시가 가정 |
| v2 | trend_8_26 + breakout_8 | 10012.57 | 12.57 | sell / filled / 직전 완료 봉 목표 비중 50%; 다음 봉 시가 가정 |
| v2 | trend_8_26 AND reversion_12 | 9775.04 | -224.96 | sell / filled / 직전 완료 봉 목표 비중 0%; 다음 봉 시가 가정 |
| v2 | trend_8_26 + reversion_12 | 10071.43 | 71.43 | buy / filled / 직전 완료 봉 목표 비중 50%; 다음 봉 시가 가정 |
| v2 | trend_8_26 AND volume_26 | 9949.23 | -50.77 | sell / filled / 직전 완료 봉 목표 비중 0%; 다음 봉 시가 가정 |
| v2 | trend_8_26 + volume_26 | 10079.31 | 79.31 | buy / filled / 직전 완료 봉 목표 비중 50%; 다음 봉 시가 가정 |
| v2 | momentum_26 AND breakout_8 | 9838.62 | -161.38 | sell / filled / 직전 완료 봉 목표 비중 0%; 다음 봉 시가 가정 |
| v2 | momentum_26 + breakout_8 | 10075.54 | 75.54 | sell / filled / 직전 완료 봉 목표 비중 50%; 다음 봉 시가 가정 |
| v2 | momentum_26 AND reversion_12 | 9838.09 | -161.91 | sell / filled / 직전 완료 봉 목표 비중 0%; 다음 봉 시가 가정 |
| v2 | momentum_26 + reversion_12 | 10134.65 | 134.65 | buy / filled / 직전 완료 봉 목표 비중 50%; 다음 봉 시가 가정 |
| v2 | momentum_26 AND volume_26 | 9925.24 | -74.76 | sell / filled / 직전 완료 봉 목표 비중 0%; 다음 봉 시가 가정 |
| v2 | momentum_26 + volume_26 | 10100.14 | 100.14 | buy / filled / 직전 완료 봉 목표 비중 50%; 다음 봉 시가 가정 |
| v2 | breakout_8 AND reversion_12 | 10000.00 | 0.00 | 대기 /  / 새 신호 대기 |
| v2 | breakout_8 + reversion_12 | 9825.02 | -174.98 | sell / filled / 직전 완료 봉 목표 비중 0%; 다음 봉 시가 가정 |
| v2 | breakout_8 AND volume_26 | 9860.28 | -139.72 | sell / filled / 직전 완료 봉 목표 비중 0%; 다음 봉 시가 가정 |
| v2 | breakout_8 + volume_26 | 9812.40 | -187.60 | sell / filled / 직전 완료 봉 목표 비중 0%; 다음 봉 시가 가정 |
| v2 | reversion_12 AND volume_26 | 10009.78 | 9.78 | sell / filled / 직전 완료 봉 목표 비중 0%; 다음 봉 시가 가정 |
| v2 | reversion_12 + volume_26 | 9888.34 | -111.66 | sell / filled / 직전 완료 봉 목표 비중 0%; 다음 봉 시가 가정 |
| v2 | ema_12_26 | 9996.84 | -3.16 | buy / partial / EMA12 > EMA26; 조건 충족; EMA12=118.628, EMA26=118.619; 직전 완료 봉 목표를 다음 봉 시가에 모의 적용 |
| v2 | macd_12_26_9 | 10011.38 | 11.38 | buy / partial / MACD > 신호선 그리고 MACD > 0; 조건 충족; MACD=0.00919902, signal9=-0.00852776; 직전 완료 봉 목표를 다음 봉 시가에 모의 적용 |
| v2 | rsi_14_recovery | 10000.00 | 0.00 | 대기 /  / 새 신호 대기 |
| v2 | bollinger_20_reentry | 10000.00 | 0.00 | 대기 /  / 새 신호 대기 |
| v2 | donchian_20 | 10000.00 | 0.00 | 대기 /  / 새 신호 대기 |
| v2 | atr_14_breakout | 9977.72 | -22.28 | sell / filled / 종가 > 직전 종가 + 직전 ATR14 그리고 종가 > EMA26; 조건 미충족; close=119.375, threshold=119.607, prior_ATR14=0.486823, EMA26=118.217; 직전 완료 봉 목표를 다음 봉 시가에 모의 적용 |
| v2 | session_vwap | 9740.45 | -259.55 | buy / partial / 종가 > 뉴욕 거래일별 누적 전형가격 VWAP; 조건 충족; close=118.68, session_VWAP=118.618, session_volume=1.15133e+07; 직전 완료 봉 목표를 다음 봉 시가에 모의 적용 |
| v2 | obv_20 | 9873.54 | -126.46 | buy / partial / OBV > OBV의 SMA20 그리고 종가 > EMA26; 조건 충족; OBV=2.23382e+07, OBV_SMA20=1.748e+07, close=118.68, EMA26=118.585; 직전 완료 봉 목표를 다음 봉 시가에 모의 적용 |
| v2 | stochastic_14_3_recovery | 9977.72 | -22.28 | sell / filled / 직전 %K14 < 20에서 %K14가 %D3 상향 돌파 (한 봉 목표); 조건 미충족; K14=93.8952, D3=60.8222, previous_K14=82.4242, previous_D3=34.5012; 직전 완료 봉 목표를 다음 봉 시가에 모의 적용 |
| v2 | mfi_14_recovery | 10000.00 | 0.00 | 대기 /  / 새 신호 대기 |
| v2 | adx_14_trend | 9989.70 | -10.30 | sell / filled / Wilder ADX14 >= 25 그리고 +DI14 > -DI14; 조건 미충족; ADX14=24.5142, plus_DI14=24.7537, minus_DI14=21.6519; 직전 완료 봉 목표를 다음 봉 시가에 모의 적용 |
| v2 | aroon_25_trend | 9972.76 | -27.24 | buy / partial / Aroon25 Up > 70 그리고 Down < 30 (동률이면 최신 극값); 조건 충족; Aroon_up=100, Aroon_down=28; 직전 완료 봉 목표를 다음 봉 시가에 모의 적용 |
| v2 | cci_20_momentum | 9925.98 | -74.02 | buy / partial / CCI20 > 100 (전형가격·평균절대편차); 조건 충족; CCI20=148.633; 직전 완료 봉 목표를 다음 봉 시가에 모의 적용 |
| v2 | williams_14_recovery | 9977.72 | -22.28 | sell / filled / 직전 Williams %R14 < -80, 현재 >= -80 (한 봉 목표); 조건 미충족; Williams_R14=-6.10484, previous_R14=-17.5758; 직전 완료 봉 목표를 다음 봉 시가에 모의 적용 |
| v2 | cmf_20_accumulation | 9904.29 | -95.71 | buy / partial / Chaikin Money Flow20 > 0.1; 조건 충족; CMF20=0.112667, volume20=1.57051e+07; 직전 완료 봉 목표를 다음 봉 시가에 모의 적용 |
| v2 | chaikin_3_10 | 9728.20 | -271.80 | buy / partial / ADL의 EMA3 - EMA10 > 0 그리고 종가 > EMA26; 조건 충족; Chaikin3_10=395736, ADL=1.91464e+07, close=118.68, EMA26=118.585; 직전 완료 봉 목표를 다음 봉 시가에 모의 적용 |
| v2 | roc_10_momentum | 10000.00 | 0.00 | 대기 /  / 새 신호 대기 |
| v2 | trix_15_trend | 9791.67 | -208.33 | buy / partial / 15봉 삼중 EMA의 1봉 변화율 TRIX > 0 그리고 종가 > EMA26; 조건 충족; TRIX15_percent=0.00139768, close=119.24, EMA26=118.719; 직전 완료 봉 목표를 다음 봉 시가에 모의 적용 |
| v2 | keltner_20_breakout | 10000.00 | 0.00 | 대기 /  / 새 신호 대기 |
| v2 | opening_range_30m | 9972.76 | -27.24 | buy / partial / 뉴욕 09:30·09:45 두 완료 봉 최고가를 10:00 이후 종가가 돌파; 조건 충족; close=119.24, opening_high=119.14; 직전 완료 봉 목표를 다음 봉 시가에 모의 적용 |

### 같은 기간의 비용·노출 비교 (사후 연구)

| 전략 | 비용 전 | 비용 후 | 100% 보유 | 같은 평균 노출 보유 | 평균 노출 |
|---|---:|---:|---:|---:|---:|
| cash | 0.00% | 0.00% | 11.54% | 0.00% | 0.00% |
| buy_hold | 12.01% | 11.54% | 11.54% | 11.54% | 100.00% |
| trend_8_26 | 8.26% | 4.69% | 11.54% | 7.55% | 66.23% |
| momentum_26 | 9.78% | 3.95% | 11.54% | 7.64% | 67.02% |
| breakout_8 | 6.72% | -10.16% | 11.54% | 2.97% | 26.44% |
| reversion_12 | 3.63% | -7.09% | 11.54% | 1.94% | 17.28% |
| volume_26 | 0.37% | -5.36% | 11.54% | 0.58% | 5.24% |
| trend_8_26 AND momentum_26 | 8.00% | 3.12% | 11.54% | 6.79% | 59.69% |
| trend_8_26 + momentum_26 | 9.02% | 4.32% | 11.54% | 7.60% | 66.63% |
| trend_8_26 AND breakout_8 | 6.83% | -6.21% | 11.54% | 2.38% | 21.20% |
| trend_8_26 + breakout_8 | 7.50% | -3.01% | 11.54% | 5.25% | 46.34% |
| trend_8_26 AND reversion_12 | 0.27% | -4.66% | 11.54% | 0.73% | 6.54% |
| trend_8_26 + reversion_12 | 5.96% | -0.96% | 11.54% | 4.72% | 41.76% |
| trend_8_26 AND volume_26 | 0.53% | -1.56% | 11.54% | 0.20% | 1.83% |
| trend_8_26 + volume_26 | 4.28% | -0.04% | 11.54% | 4.03% | 35.74% |
| momentum_26 AND breakout_8 | 6.88% | -6.56% | 11.54% | 2.53% | 22.51% |
| momentum_26 + breakout_8 | 8.25% | -2.54% | 11.54% | 5.29% | 46.73% |
| momentum_26 AND reversion_12 | 1.20% | -4.18% | 11.54% | 0.82% | 7.33% |
| momentum_26 + reversion_12 | 6.69% | 0.37% | 11.54% | 4.77% | 42.15% |
| momentum_26 AND volume_26 | 1.86% | -1.91% | 11.54% | 0.29% | 2.62% |
| momentum_26 + volume_26 | 5.00% | -0.60% | 11.54% | 4.08% | 36.13% |
| breakout_8 AND reversion_12 | 0.00% | 0.00% | 11.54% | 0.00% | 0.00% |
| breakout_8 + reversion_12 | 5.19% | -8.06% | 11.54% | 2.45% | 21.87% |
| breakout_8 AND volume_26 | 1.02% | -1.49% | 11.54% | 0.20% | 1.83% |
| breakout_8 + volume_26 | 3.52% | -7.59% | 11.54% | 1.77% | 15.84% |
| reversion_12 AND volume_26 | -0.97% | -3.44% | 11.54% | 0.20% | 1.83% |
| reversion_12 + volume_26 | 1.99% | -5.64% | 11.54% | 1.26% | 11.26% |
| ema_12_26 | 12.02% | 10.62% | 11.54% | 7.83% | 68.59% |
| macd_12_26_9 | 8.31% | 4.73% | 11.54% | 3.84% | 34.03% |
| rsi_14_recovery | -0.68% | -2.74% | 11.54% | 0.15% | 1.31% |
| bollinger_20_reentry | 0.93% | -2.41% | 11.54% | 0.23% | 2.09% |
| donchian_20 | 4.80% | -7.22% | 11.54% | 1.46% | 13.09% |
| atr_14_breakout | -0.61% | -10.14% | 11.54% | 0.82% | 7.33% |
| session_vwap | 8.36% | -2.44% | 11.54% | 6.64% | 58.38% |
| obv_20 | 10.32% | 2.72% | 11.54% | 6.21% | 54.71% |
| stochastic_14_3_recovery | 1.36% | -8.36% | 11.54% | 0.70% | 6.28% |
| mfi_14_recovery | 0.02% | -0.81% | 11.54% | 0.06% | 0.52% |
| adx_14_trend | 8.84% | 6.13% | 11.54% | 5.73% | 50.52% |
| aroon_25_trend | 5.62% | 0.85% | 11.54% | 3.33% | 29.58% |
| cci_20_momentum | 7.36% | -0.87% | 11.54% | 3.60% | 31.94% |
| williams_14_recovery | 0.16% | -7.91% | 11.54% | 0.58% | 5.24% |
| cmf_20_accumulation | 8.57% | -0.17% | 11.54% | 3.99% | 35.34% |
| chaikin_3_10 | 8.51% | 0.19% | 11.54% | 5.76% | 50.79% |
| roc_10_momentum | -0.30% | -5.20% | 11.54% | 1.61% | 14.40% |
| trix_15_trend | 10.89% | 7.67% | 11.54% | 7.13% | 62.57% |
| keltner_20_breakout | 6.84% | 0.74% | 11.54% | 2.94% | 26.18% |
| opening_range_30m | 10.05% | 5.08% | 11.54% | 3.96% | 35.08% |

동일 구간·초기 자금, 종료 시 청산 비용 포함. 노출 맞춤은 사후 설명용이며 v2 실제 계좌 성과가 아닙니다.
[낙폭 분해·비용 영향·전체 구간](WMT/comparison.json)

[v1 전체 기록](WMT/accounts.json) · [v2 전체 기록](WMT/accounts-v2.json)
