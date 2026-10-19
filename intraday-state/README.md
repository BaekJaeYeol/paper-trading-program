# 모의투자 운영 현황

[PC·서버 장애 진단과 복구 방법](https://github.com/BaekJaeYeol/paper-trading-program/blob/main/investment-lab/docs/failure-recovery.md)

이번 실행 복구: {}

완료 봉 확인 주기: 기록 0/15회 · 기록 없는 예정 15회 · 아직 판정 전 11회 · 주의: 예약 시작 지연 또는 실행·저장 누락을 확인하세요.

[주기 판정 기준](https://github.com/BaekJaeYeol/paper-trading-program/blob/main/investment-lab/docs/session-coverage.md)

최근 확인: 2026-10-19T17:27:44.133897+00:00 (UTC)
다음 15분 확인 목표 (세션 실행 중에만 적용): 2026-10-19T17:37:00+00:00 (UTC, 실행 지연 가능)

실제 주문 없음. v1 기존 계좌와 v2 새 계좌의 시작일이 다르므로 수익률을 직접 우열 비교하지 마세요.
v2는 다음 봉 시가에 비용·스프레드·직전 거래량 제한을 적용한 가상 체결입니다. 미체결 잔량은 만료됩니다.

| 종목 | 상태 | 최근 성공 UTC | 마지막 완료 봉 UTC | 이번 새 봉 |
|---|---|---|---|---|
| SPY | updated | 2026-10-19T17:27:44.133897+00:00 | 2026-10-19T17:00:00+00:00 | 15 |
| QQQ | updated | 2026-10-19T17:27:44.133897+00:00 | 2026-10-19T17:00:00+00:00 | 15 |
| IWM | updated | 2026-10-19T17:27:44.133897+00:00 | 2026-10-19T17:00:00+00:00 | 15 |
| DIA | updated | 2026-10-19T17:27:44.133897+00:00 | 2026-10-19T17:00:00+00:00 | 15 |
| MSFT | updated | 2026-10-19T17:27:44.133897+00:00 | 2026-10-19T17:00:00+00:00 | 15 |
| JPM | updated | 2026-10-19T17:27:44.133897+00:00 | 2026-10-19T17:00:00+00:00 | 15 |
| XOM | updated | 2026-10-19T17:27:44.133897+00:00 | 2026-10-19T17:00:00+00:00 | 15 |
| JNJ | updated | 2026-10-19T17:27:44.133897+00:00 | 2026-10-19T17:00:00+00:00 | 15 |
| CAT | updated | 2026-10-19T17:27:44.133897+00:00 | 2026-10-19T17:00:00+00:00 | 15 |
| WMT | updated | 2026-10-19T17:27:44.133897+00:00 | 2026-10-19T17:00:00+00:00 | 15 |

이번 실행 소요: 47.0초
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
| v1 | buy_hold | 9905.56 | -94.44 | buy /  / buy_hold: prior completed bar target 100%; next bar open simulation |
| v1 | trend_8_26 | 9883.88 | -116.12 | buy /  / trend_8_26: prior completed bar target 100%; next bar open simulation |
| v1 | momentum_26 | 9865.37 | -134.63 | buy /  / momentum_26: prior completed bar target 100%; next bar open simulation |
| v1 | breakout_8 | 9873.76 | -126.24 | sell /  / breakout_8: prior completed bar target 0%; next bar open simulation |
| v1 | reversion_12 | 9862.04 | -137.96 | buy /  / reversion_12: prior completed bar target 100%; next bar open simulation |
| v1 | volume_26 | 9790.14 | -209.86 | sell /  / volume_26: prior completed bar target 0%; next bar open simulation |
| v1 | trend_8_26 AND momentum_26 | 9865.37 | -134.63 | buy /  / trend_8_26 AND momentum_26: prior completed bar target 100%; next bar open simulation |
| v1 | trend_8_26 + momentum_26 | 9874.61 | -125.39 | buy /  / trend_8_26 + momentum_26: prior completed bar target 100%; next bar open simulation |
| v1 | trend_8_26 AND breakout_8 | 9970.32 | -29.68 | sell /  / trend_8_26 AND breakout_8: prior completed bar target 0%; next bar open simulation |
| v1 | trend_8_26 + breakout_8 | 9898.50 | -101.50 | buy /  / trend_8_26 + breakout_8: prior completed bar target 50%; next bar open simulation |
| v1 | trend_8_26 AND reversion_12 | 9925.85 | -74.15 | buy /  / trend_8_26 AND reversion_12: prior completed bar target 100%; next bar open simulation |
| v1 | trend_8_26 + reversion_12 | 9872.86 | -127.14 | buy /  / trend_8_26 + reversion_12: prior completed bar target 100%; next bar open simulation |
| v1 | trend_8_26 AND volume_26 | 9836.21 | -163.79 | sell /  / trend_8_26 AND volume_26: prior completed bar target 0%; next bar open simulation |
| v1 | trend_8_26 + volume_26 | 9836.84 | -163.16 | sell /  / trend_8_26 + volume_26: prior completed bar target 50%; next bar open simulation |
| v1 | momentum_26 AND breakout_8 | 9954.13 | -45.87 | sell /  / momentum_26 AND breakout_8: prior completed bar target 0%; next bar open simulation |
| v1 | momentum_26 + breakout_8 | 9869.53 | -130.47 | buy /  / momentum_26 + breakout_8: prior completed bar target 50%; next bar open simulation |
| v1 | momentum_26 AND reversion_12 | 9979.51 | -20.49 | buy /  / momentum_26 AND reversion_12: prior completed bar target 100%; next bar open simulation |
| v1 | momentum_26 + reversion_12 | 9883.36 | -116.64 | buy /  / momentum_26 + reversion_12: prior completed bar target 100%; next bar open simulation |
| v1 | momentum_26 AND volume_26 | 9849.91 | -150.09 | sell /  / momentum_26 AND volume_26: prior completed bar target 0%; next bar open simulation |
| v1 | momentum_26 + volume_26 | 9827.64 | -172.36 | sell /  / momentum_26 + volume_26: prior completed bar target 50%; next bar open simulation |
| v1 | breakout_8 AND reversion_12 | 10000.00 | 0.00 | 대기 /  / 새 신호 대기 |
| v1 | breakout_8 + reversion_12 | 9867.80 | -132.20 | buy /  / breakout_8 + reversion_12: prior completed bar target 50%; next bar open simulation |
| v1 | breakout_8 AND volume_26 | 9954.13 | -45.87 | sell /  / breakout_8 AND volume_26: prior completed bar target 0%; next bar open simulation |
| v1 | breakout_8 + volume_26 | 9831.79 | -168.21 | sell /  / breakout_8 + volume_26: prior completed bar target 0%; next bar open simulation |
| v1 | reversion_12 AND volume_26 | 9899.64 | -100.36 | sell /  / reversion_12 AND volume_26: prior completed bar target 0%; next bar open simulation |
| v1 | reversion_12 + volume_26 | 9825.96 | -174.04 | buy /  / reversion_12 + volume_26: prior completed bar target 50%; next bar open simulation |
| v1 | ema_12_26 | 9867.68 | -132.32 | buy /  / EMA12 > EMA26; 조건 충족; EMA12=766.605, EMA26=766.511 |
| v1 | macd_12_26_9 | 9881.42 | -118.58 | buy /  / MACD > 신호선 그리고 MACD > 0; 조건 충족; MACD=0.0937072, signal9=-0.695283 |
| v1 | rsi_14_recovery | 9899.32 | -100.68 | sell /  / 직전 RSI14 < 30, 현재 RSI14 >= 30 (한 봉 목표); 조건 미충족; RSI14=34.3611, previous_RSI14=32.906 |
| v1 | bollinger_20_reentry | 9835.17 | -164.83 | sell /  / 직전 종가 < 직전 하단밴드, 현재 하단밴드 <= 종가 <= SMA20 (한 봉 목표); 조건 미충족; close=763.39, lower20=762.854, SMA20=768.639, previous_lower20=763.636 |
| v1 | donchian_20 | 9960.79 | -39.21 | sell /  / 종가 > 현재 봉을 제외한 직전 20봉 최고가; 조건 미충족; close=769.96, prior_high20=770.3 |
| v1 | atr_14_breakout | 9955.14 | -44.86 | sell /  / 종가 > 직전 종가 + 직전 ATR14 그리고 종가 > EMA26; 조건 미충족; close=766.58, threshold=768.736, prior_ATR14=1.82624, EMA26=765.727 |
| v1 | session_vwap | 9806.83 | -193.17 | sell /  / 종가 > 뉴욕 거래일별 누적 전형가격 VWAP; 조건 미충족; close=768.64, session_VWAP=768.839, session_volume=6.99147e+07 |
| v1 | obv_20 | 9909.51 | -90.49 | sell /  / OBV > OBV의 SMA20 그리고 종가 > EMA26; 조건 미충족; OBV=-1.1153e+07, OBV_SMA20=-7.86173e+06, close=768.275, EMA26=767.362 |
| v1 | stochastic_14_3_recovery | 9839.35 | -160.65 | sell /  / 직전 %K14 < 20에서 %K14가 %D3 상향 돌파 (한 봉 목표); 조건 미충족; K14=84.501, D3=47.2592, previous_K14=38.478, previous_D3=30.1887 |
| v1 | mfi_14_recovery | 9955.14 | -44.86 | sell /  / 직전 MFI14 < 20, 현재 MFI14 >= 20 (한 봉 목표); 조건 미충족; MFI14=24.4041, previous_MFI14=24.1984 |
| v1 | adx_14_trend | 9981.96 | -18.04 | sell /  / Wilder ADX14 >= 25 그리고 +DI14 > -DI14; 조건 미충족; ADX14=24.2312, plus_DI14=28.3519, minus_DI14=24.6578 |
| v1 | aroon_25_trend | 9902.37 | -97.63 | sell /  / Aroon25 Up > 70 그리고 Down < 30 (동률이면 최신 극값); 조건 미충족; Aroon_up=72, Aroon_down=100 |
| v1 | cci_20_momentum | 9861.55 | -138.45 | sell /  / CCI20 > 100 (전형가격·평균절대편차); 조건 미충족; CCI20=98.503 |
| v1 | williams_14_recovery | 9811.23 | -188.77 | sell /  / 직전 Williams %R14 < -80, 현재 >= -80 (한 봉 목표); 조건 미충족; Williams_R14=-15.499, previous_R14=-61.522 |
| v1 | cmf_20_accumulation | 9890.95 | -109.05 | sell /  / Chaikin Money Flow20 > 0.1; 조건 미충족; CMF20=0.0493062, volume20=8.08389e+07 |
| v1 | chaikin_3_10 | 9864.45 | -135.55 | sell /  / ADL의 EMA3 - EMA10 > 0 그리고 종가 > EMA26; 조건 미충족; Chaikin3_10=-974621, ADL=7.60516e+06, close=768.275, EMA26=767.362 |
| v1 | roc_10_momentum | 9953.42 | -46.58 | sell /  / 10봉 ROC > 1% 그리고 종가 > EMA26; 조건 미충족; ROC10_percent=0.806376, close=769.45, EMA26=767.181 |
| v1 | trix_15_trend | 9886.18 | -113.82 | buy /  / 15봉 삼중 EMA의 1봉 변화율 TRIX > 0 그리고 종가 > EMA26; 조건 충족; TRIX15_percent=0.00164165, close=768.275, EMA26=767.362 |
| v1 | keltner_20_breakout | 10000.00 | 0.00 | 대기 /  / 새 신호 대기 |
| v1 | opening_range_30m | 9846.77 | -153.23 | sell /  / 뉴욕 09:30·09:45 두 완료 봉 최고가를 10:00 이후 종가가 돌파; 조건 미충족; close=767.51, opening_high=768.06 |
| v2 | cash | 10000.00 | 0.00 | 대기 /  / 새 신호 대기 |
| v2 | buy_hold | 9834.11 | -165.89 | buy / partial / 직전 완료 봉 목표 비중 100%; 다음 봉 시가 가정 |
| v2 | trend_8_26 | 9766.78 | -233.22 | buy / partial / 직전 완료 봉 목표 비중 100%; 다음 봉 시가 가정 |
| v2 | momentum_26 | 9719.23 | -280.77 | buy / partial / 직전 완료 봉 목표 비중 100%; 다음 봉 시가 가정 |
| v2 | breakout_8 | 9471.75 | -528.25 | sell / filled / 직전 완료 봉 목표 비중 0%; 다음 봉 시가 가정 |
| v2 | reversion_12 | 9397.70 | -602.30 | buy / partial / 직전 완료 봉 목표 비중 100%; 다음 봉 시가 가정 |
| v2 | volume_26 | 9235.92 | -764.08 | sell / filled / 직전 완료 봉 목표 비중 0%; 다음 봉 시가 가정 |
| v2 | trend_8_26 AND momentum_26 | 9725.86 | -274.14 | buy / partial / 직전 완료 봉 목표 비중 100%; 다음 봉 시가 가정 |
| v2 | trend_8_26 + momentum_26 | 9742.98 | -257.02 | buy / partial / 직전 완료 봉 목표 비중 100%; 다음 봉 시가 가정 |
| v2 | trend_8_26 AND breakout_8 | 9794.09 | -205.91 | sell / filled / 직전 완료 봉 목표 비중 0%; 다음 봉 시가 가정 |
| v2 | trend_8_26 + breakout_8 | 9638.15 | -361.85 | buy / filled / 직전 완료 봉 목표 비중 50%; 다음 봉 시가 가정 |
| v2 | trend_8_26 AND reversion_12 | 9819.79 | -180.21 | buy / partial / 직전 완료 봉 목표 비중 100%; 다음 봉 시가 가정 |
| v2 | trend_8_26 + reversion_12 | 9580.06 | -419.94 | buy / partial / 직전 완료 봉 목표 비중 100%; 다음 봉 시가 가정 |
| v2 | trend_8_26 AND volume_26 | 9678.83 | -321.17 | sell / filled / 직전 완료 봉 목표 비중 0%; 다음 봉 시가 가정 |
| v2 | trend_8_26 + volume_26 | 9517.33 | -482.67 | sell / filled / 직전 완료 봉 목표 비중 50%; 다음 봉 시가 가정 |
| v2 | momentum_26 AND breakout_8 | 9736.71 | -263.29 | sell / filled / 직전 완료 봉 목표 비중 0%; 다음 봉 시가 가정 |
| v2 | momentum_26 + breakout_8 | 9594.58 | -405.42 | buy / filled / 직전 완료 봉 목표 비중 50%; 다음 봉 시가 가정 |
| v2 | momentum_26 AND reversion_12 | 9941.80 | -58.20 | buy / partial / 직전 완료 봉 목표 비중 100%; 다음 봉 시가 가정 |
| v2 | momentum_26 + reversion_12 | 9596.94 | -403.06 | buy / partial / 직전 완료 봉 목표 비중 100%; 다음 봉 시가 가정 |
| v2 | momentum_26 AND volume_26 | 9762.54 | -237.46 | sell / filled / 직전 완료 봉 목표 비중 0%; 다음 봉 시가 가정 |
| v2 | momentum_26 + volume_26 | 9534.08 | -465.92 | sell / filled / 직전 완료 봉 목표 비중 50%; 다음 봉 시가 가정 |
| v2 | breakout_8 AND reversion_12 | 10000.00 | 0.00 | 대기 /  / 새 신호 대기 |
| v2 | breakout_8 + reversion_12 | 9473.84 | -526.16 | buy / filled / 직전 완료 봉 목표 비중 50%; 다음 봉 시가 가정 |
| v2 | breakout_8 AND volume_26 | 9885.63 | -114.37 | sell / filled / 직전 완료 봉 목표 비중 0%; 다음 봉 시가 가정 |
| v2 | breakout_8 + volume_26 | 9392.04 | -607.96 | sell / filled / 직전 완료 봉 목표 비중 0%; 다음 봉 시가 가정 |
| v2 | reversion_12 AND volume_26 | 9641.69 | -358.31 | sell / filled / 직전 완료 봉 목표 비중 0%; 다음 봉 시가 가정 |
| v2 | reversion_12 + volume_26 | 9394.71 | -605.29 | buy / filled / 직전 완료 봉 목표 비중 50%; 다음 봉 시가 가정 |
| v2 | ema_12_26 | 9864.72 | -135.28 | buy / partial / EMA12 > EMA26; 조건 충족; EMA12=766.605, EMA26=766.511; 직전 완료 봉 목표를 다음 봉 시가에 모의 적용 |
| v2 | macd_12_26_9 | 9878.45 | -121.55 | buy / partial / MACD > 신호선 그리고 MACD > 0; 조건 충족; MACD=0.0937072, signal9=-0.695283; 직전 완료 봉 목표를 다음 봉 시가에 모의 적용 |
| v2 | rsi_14_recovery | 9895.36 | -104.64 | sell / filled / 직전 RSI14 < 30, 현재 RSI14 >= 30 (한 봉 목표); 조건 미충족; RSI14=34.3611, previous_RSI14=32.906; 직전 완료 봉 목표를 다음 봉 시가에 모의 적용 |
| v2 | bollinger_20_reentry | 9829.27 | -170.73 | sell / filled / 직전 종가 < 직전 하단밴드, 현재 하단밴드 <= 종가 <= SMA20 (한 봉 목표); 조건 미충족; close=763.39, lower20=762.854, SMA20=768.639, previous_lower20=763.636; 직전 완료 봉 목표를 다음 봉 시가에 모의 적용 |
| v2 | donchian_20 | 9958.80 | -41.20 | sell / filled / 종가 > 현재 봉을 제외한 직전 20봉 최고가; 조건 미충족; close=769.96, prior_high20=770.3; 직전 완료 봉 목표를 다음 봉 시가에 모의 적용 |
| v2 | atr_14_breakout | 9953.15 | -46.85 | sell / filled / 종가 > 직전 종가 + 직전 ATR14 그리고 종가 > EMA26; 조건 미충족; close=766.58, threshold=768.736, prior_ATR14=1.82624, EMA26=765.727; 직전 완료 봉 목표를 다음 봉 시가에 모의 적용 |
| v2 | session_vwap | 9798.99 | -201.01 | sell / filled / 종가 > 뉴욕 거래일별 누적 전형가격 VWAP; 조건 미충족; close=768.64, session_VWAP=768.839, session_volume=6.99147e+07; 직전 완료 봉 목표를 다음 봉 시가에 모의 적용 |
| v2 | obv_20 | 9905.54 | -94.46 | sell / filled / OBV > OBV의 SMA20 그리고 종가 > EMA26; 조건 미충족; OBV=-1.1153e+07, OBV_SMA20=-7.86173e+06, close=768.275, EMA26=767.362; 직전 완료 봉 목표를 다음 봉 시가에 모의 적용 |
| v2 | stochastic_14_3_recovery | 9831.49 | -168.51 | sell / filled / 직전 %K14 < 20에서 %K14가 %D3 상향 돌파 (한 봉 목표); 조건 미충족; K14=84.501, D3=47.2592, previous_K14=38.478, previous_D3=30.1887; 직전 완료 봉 목표를 다음 봉 시가에 모의 적용 |
| v2 | mfi_14_recovery | 9953.15 | -46.85 | sell / filled / 직전 MFI14 < 20, 현재 MFI14 >= 20 (한 봉 목표); 조건 미충족; MFI14=24.4041, previous_MFI14=24.1984; 직전 완료 봉 목표를 다음 봉 시가에 모의 적용 |
| v2 | adx_14_trend | 9979.97 | -20.03 | sell / filled / Wilder ADX14 >= 25 그리고 +DI14 > -DI14; 조건 미충족; ADX14=24.2312, plus_DI14=28.3519, minus_DI14=24.6578; 직전 완료 봉 목표를 다음 봉 시가에 모의 적용 |
| v2 | aroon_25_trend | 9900.39 | -99.61 | sell / filled / Aroon25 Up > 70 그리고 Down < 30 (동률이면 최신 극값); 조건 미충족; Aroon_up=72, Aroon_down=100; 직전 완료 봉 목표를 다음 봉 시가에 모의 적용 |
| v2 | cci_20_momentum | 9855.63 | -144.37 | sell / filled / CCI20 > 100 (전형가격·평균절대편차); 조건 미충족; CCI20=98.503; 직전 완료 봉 목표를 다음 봉 시가에 모의 적용 |
| v2 | williams_14_recovery | 9803.39 | -196.61 | sell / filled / 직전 Williams %R14 < -80, 현재 >= -80 (한 봉 목표); 조건 미충족; Williams_R14=-15.499, previous_R14=-61.522; 직전 완료 봉 목표를 다음 봉 시가에 모의 적용 |
| v2 | cmf_20_accumulation | 9887.00 | -113.00 | sell / filled / Chaikin Money Flow20 > 0.1; 조건 미충족; CMF20=0.0493062, volume20=8.08389e+07; 직전 완료 봉 목표를 다음 봉 시가에 모의 적용 |
| v2 | chaikin_3_10 | 9858.53 | -141.47 | sell / filled / ADL의 EMA3 - EMA10 > 0 그리고 종가 > EMA26; 조건 미충족; Chaikin3_10=-974621, ADL=7.60516e+06, close=768.275, EMA26=767.362; 직전 완료 봉 목표를 다음 봉 시가에 모의 적용 |
| v2 | roc_10_momentum | 9951.43 | -48.57 | sell / filled / 10봉 ROC > 1% 그리고 종가 > EMA26; 조건 미충족; ROC10_percent=0.806376, close=769.45, EMA26=767.181; 직전 완료 봉 목표를 다음 봉 시가에 모의 적용 |
| v2 | trix_15_trend | 9883.21 | -116.79 | buy / partial / 15봉 삼중 EMA의 1봉 변화율 TRIX > 0 그리고 종가 > EMA26; 조건 충족; TRIX15_percent=0.00164165, close=768.275, EMA26=767.362; 직전 완료 봉 목표를 다음 봉 시가에 모의 적용 |
| v2 | keltner_20_breakout | 10000.00 | 0.00 | 대기 /  / 새 신호 대기 |
| v2 | opening_range_30m | 9840.86 | -159.14 | sell / filled / 뉴욕 09:30·09:45 두 완료 봉 최고가를 10:00 이후 종가가 돌파; 조건 미충족; close=767.51, opening_high=768.06; 직전 완료 봉 목표를 다음 봉 시가에 모의 적용 |

### 같은 기간의 비용·노출 비교 (사후 연구)

| 전략 | 비용 전 | 비용 후 | 100% 보유 | 같은 평균 노출 보유 | 평균 노출 |
|---|---:|---:|---:|---:|---:|
| cash | 0.00% | 0.00% | -0.23% | -0.00% | 0.00% |
| buy_hold | 0.19% | -0.23% | -0.23% | -0.23% | 100.00% |
| trend_8_26 | 1.46% | -1.90% | -0.23% | -0.11% | 49.08% |
| momentum_26 | -0.46% | -4.56% | -0.23% | -0.11% | 47.51% |
| breakout_8 | -0.22% | -15.65% | -0.23% | -0.05% | 22.31% |
| reversion_12 | -1.68% | -12.96% | -0.23% | -0.07% | 29.40% |
| volume_26 | -1.12% | -10.60% | -0.23% | -0.02% | 9.71% |
| trend_8_26 AND momentum_26 | 0.60% | -3.13% | -0.23% | -0.09% | 41.73% |
| trend_8_26 + momentum_26 | 0.49% | -3.24% | -0.23% | -0.11% | 48.30% |
| trend_8_26 AND breakout_8 | 0.17% | -10.57% | -0.23% | -0.03% | 13.12% |
| trend_8_26 + breakout_8 | 0.62% | -8.84% | -0.23% | -0.08% | 35.70% |
| trend_8_26 AND reversion_12 | -0.16% | -3.86% | -0.23% | -0.01% | 5.77% |
| trend_8_26 + reversion_12 | -0.12% | -7.41% | -0.23% | -0.09% | 39.24% |
| trend_8_26 AND volume_26 | -0.68% | -5.16% | -0.23% | -0.01% | 4.72% |
| trend_8_26 + volume_26 | 0.16% | -6.35% | -0.23% | -0.07% | 29.40% |
| momentum_26 AND breakout_8 | 0.31% | -10.44% | -0.23% | -0.03% | 13.91% |
| momentum_26 + breakout_8 | -0.34% | -10.28% | -0.23% | -0.08% | 34.91% |
| momentum_26 AND reversion_12 | -0.79% | -4.87% | -0.23% | -0.01% | 6.04% |
| momentum_26 + reversion_12 | -1.07% | -8.29% | -0.23% | -0.09% | 38.46% |
| momentum_26 AND volume_26 | -0.40% | -3.69% | -0.23% | -0.01% | 2.89% |
| momentum_26 + volume_26 | -0.79% | -6.46% | -0.23% | -0.06% | 28.61% |
| breakout_8 AND reversion_12 | 0.00% | 0.00% | -0.23% | -0.00% | 0.00% |
| breakout_8 + reversion_12 | -0.95% | -13.79% | -0.23% | -0.06% | 25.86% |
| breakout_8 AND volume_26 | 0.03% | -1.64% | -0.23% | -0.00% | 1.57% |
| breakout_8 + volume_26 | -0.67% | -12.25% | -0.23% | -0.04% | 16.02% |
| reversion_12 AND volume_26 | -0.97% | -5.44% | -0.23% | -0.01% | 4.46% |
| reversion_12 + volume_26 | -1.40% | -11.42% | -0.23% | -0.04% | 19.56% |
| ema_12_26 | -0.32% | -3.61% | -0.23% | -0.11% | 49.34% |
| macd_12_26_9 | 0.31% | -4.22% | -0.23% | -0.07% | 30.97% |
| rsi_14_recovery | -0.53% | -4.22% | -0.23% | -0.01% | 2.36% |
| bollinger_20_reentry | -1.13% | -7.17% | -0.23% | -0.01% | 3.94% |
| donchian_20 | 0.11% | -7.17% | -0.23% | -0.02% | 6.82% |
| atr_14_breakout | 0.38% | -4.55% | -0.23% | -0.01% | 3.67% |
| session_vwap | 2.10% | -7.69% | -0.23% | -0.11% | 48.03% |
| obv_20 | 0.26% | -7.43% | -0.23% | -0.09% | 38.85% |
| stochastic_14_3_recovery | -1.11% | -16.05% | -0.23% | -0.02% | 10.24% |
| mfi_14_recovery | -0.06% | -2.96% | -0.23% | -0.00% | 1.84% |
| adx_14_trend | 0.32% | -3.40% | -0.23% | -0.06% | 28.08% |
| aroon_25_trend | 0.84% | -1.67% | -0.23% | -0.06% | 25.20% |
| cci_20_momentum | -0.04% | -8.10% | -0.23% | -0.05% | 22.05% |
| williams_14_recovery | -0.81% | -11.07% | -0.23% | -0.02% | 6.82% |
| cmf_20_accumulation | 2.07% | -2.13% | -0.23% | -0.10% | 45.67% |
| chaikin_3_10 | 1.85% | -4.77% | -0.23% | -0.09% | 40.16% |
| roc_10_momentum | -0.13% | -0.97% | -0.23% | -0.00% | 1.05% |
| trix_15_trend | -0.21% | -3.10% | -0.23% | -0.08% | 36.48% |
| keltner_20_breakout | 0.09% | -3.62% | -0.23% | -0.02% | 10.76% |
| opening_range_30m | 0.36% | -5.37% | -0.23% | -0.07% | 31.76% |

동일 구간·초기 자금, 종료 시 청산 비용 포함. 노출 맞춤은 사후 설명용이며 v2 실제 계좌 성과가 아닙니다.
[낙폭 분해·비용 영향·전체 구간](SPY/comparison.json)

[v1 전체 기록](SPY/accounts.json) · [v2 전체 기록](SPY/accounts-v2.json)

## QQQ 계좌

| 모델 | 전략 | 평가액 USD | 손익 USD | 최근 매매·이유 |
|---|---|---:|---:|---|
| v1 | cash | 10000.00 | 0.00 | 대기 /  / 새 신호 대기 |
| v1 | buy_hold | 9903.78 | -96.22 | buy /  / buy_hold: prior completed bar target 100%; next bar open simulation |
| v1 | trend_8_26 | 9896.56 | -103.44 | buy /  / trend_8_26: prior completed bar target 100%; next bar open simulation |
| v1 | momentum_26 | 9838.97 | -161.03 | buy /  / momentum_26: prior completed bar target 100%; next bar open simulation |
| v1 | breakout_8 | 9897.90 | -102.10 | sell /  / breakout_8: prior completed bar target 0%; next bar open simulation |
| v1 | reversion_12 | 9869.32 | -130.68 | buy /  / reversion_12: prior completed bar target 100%; next bar open simulation |
| v1 | volume_26 | 9763.59 | -236.41 | sell /  / volume_26: prior completed bar target 0%; next bar open simulation |
| v1 | trend_8_26 AND momentum_26 | 9905.09 | -94.91 | buy /  / trend_8_26 AND momentum_26: prior completed bar target 100%; next bar open simulation |
| v1 | trend_8_26 + momentum_26 | 9887.45 | -112.55 | buy /  / trend_8_26 + momentum_26: prior completed bar target 100%; next bar open simulation |
| v1 | trend_8_26 AND breakout_8 | 9989.91 | -10.09 | sell /  / trend_8_26 AND breakout_8: prior completed bar target 0%; next bar open simulation |
| v1 | trend_8_26 + breakout_8 | 9916.97 | -83.03 | buy /  / trend_8_26 + breakout_8: prior completed bar target 50%; next bar open simulation |
| v1 | trend_8_26 AND reversion_12 | 9931.76 | -68.24 | buy /  / trend_8_26 AND reversion_12: prior completed bar target 100%; next bar open simulation |
| v1 | trend_8_26 + reversion_12 | 9883.07 | -116.93 | buy /  / trend_8_26 + reversion_12: prior completed bar target 100%; next bar open simulation |
| v1 | trend_8_26 AND volume_26 | 9932.72 | -67.28 | sell /  / trend_8_26 AND volume_26: prior completed bar target 0%; next bar open simulation |
| v1 | trend_8_26 + volume_26 | 9829.79 | -170.21 | buy /  / trend_8_26 + volume_26: prior completed bar target 50%; next bar open simulation |
| v1 | momentum_26 AND breakout_8 | 9929.95 | -70.05 | sell /  / momentum_26 AND breakout_8: prior completed bar target 0%; next bar open simulation |
| v1 | momentum_26 + breakout_8 | 9868.37 | -131.63 | buy /  / momentum_26 + breakout_8: prior completed bar target 50%; next bar open simulation |
| v1 | momentum_26 AND reversion_12 | 9931.76 | -68.24 | buy /  / momentum_26 AND reversion_12: prior completed bar target 100%; next bar open simulation |
| v1 | momentum_26 + reversion_12 | 9854.29 | -145.71 | buy /  / momentum_26 + reversion_12: prior completed bar target 100%; next bar open simulation |
| v1 | momentum_26 AND volume_26 | 9912.22 | -87.78 | sell /  / momentum_26 AND volume_26: prior completed bar target 0%; next bar open simulation |
| v1 | momentum_26 + volume_26 | 9820.77 | -179.23 | buy /  / momentum_26 + volume_26: prior completed bar target 50%; next bar open simulation |
| v1 | breakout_8 AND reversion_12 | 10000.00 | 0.00 | 대기 /  / 새 신호 대기 |
| v1 | breakout_8 + reversion_12 | 9883.71 | -116.29 | buy /  / breakout_8 + reversion_12: prior completed bar target 50%; next bar open simulation |
| v1 | breakout_8 AND volume_26 | 9947.15 | -52.85 | sell /  / breakout_8 AND volume_26: prior completed bar target 0%; next bar open simulation |
| v1 | breakout_8 + volume_26 | 9850.15 | -149.85 | sell /  / breakout_8 + volume_26: prior completed bar target 0%; next bar open simulation |
| v1 | reversion_12 AND volume_26 | 9907.31 | -92.69 | sell /  / reversion_12 AND volume_26: prior completed bar target 0%; next bar open simulation |
| v1 | reversion_12 + volume_26 | 9855.73 | -144.27 | buy /  / reversion_12 + volume_26: prior completed bar target 50%; next bar open simulation |
| v1 | ema_12_26 | 9894.34 | -105.66 | buy /  / EMA12 > EMA26; 조건 충족; EMA12=717, EMA26=716.746 |
| v1 | macd_12_26_9 | 9894.34 | -105.66 | buy /  / MACD > 신호선 그리고 MACD > 0; 조건 충족; MACD=0.254284, signal9=-1.34399 |
| v1 | rsi_14_recovery | 9813.02 | -186.98 | sell /  / 직전 RSI14 < 30, 현재 RSI14 >= 30 (한 봉 목표); 조건 미충족; RSI14=58.2718, previous_RSI14=33.2263 |
| v1 | bollinger_20_reentry | 9882.24 | -117.76 | sell /  / 직전 종가 < 직전 하단밴드, 현재 하단밴드 <= 종가 <= SMA20 (한 봉 목표); 조건 미충족; close=716.64, lower20=715.793, SMA20=723.132, previous_lower20=716.805 |
| v1 | donchian_20 | 9951.11 | -48.89 | sell /  / 종가 > 현재 봉을 제외한 직전 20봉 최고가; 조건 미충족; close=724.13, prior_high20=724.151 |
| v1 | atr_14_breakout | 9945.53 | -54.47 | sell /  / 종가 > 직전 종가 + 직전 ATR14 그리고 종가 > EMA26; 조건 미충족; close=717.88, threshold=721.828, prior_ATR14=2.82823, EMA26=715.308 |
| v1 | session_vwap | 9802.73 | -197.27 | sell /  / 종가 > 뉴욕 거래일별 누적 전형가격 VWAP; 조건 미충족; close=721.515, session_VWAP=722.066, session_volume=4.49868e+08 |
| v1 | obv_20 | 9923.79 | -76.21 | buy /  / OBV > OBV의 SMA20 그리고 종가 > EMA26; 조건 충족; OBV=-1.30207e+07, OBV_SMA20=-3.93901e+07, close=719, EMA26=715.102 |
| v1 | stochastic_14_3_recovery | 9659.03 | -340.97 | sell /  / 직전 %K14 < 20에서 %K14가 %D3 상향 돌파 (한 봉 목표); 조건 미충족; K14=90.6084, D3=42.9821, previous_K14=27.5933, previous_D3=23.7441 |
| v1 | mfi_14_recovery | 9927.15 | -72.85 | sell /  / 직전 MFI14 < 20, 현재 MFI14 >= 20 (한 봉 목표); 조건 미충족; MFI14=58.7386, previous_MFI14=43.5194 |
| v1 | adx_14_trend | 9926.53 | -73.47 | sell /  / Wilder ADX14 >= 25 그리고 +DI14 > -DI14; 조건 미충족; ADX14=23.9831, plus_DI14=26.5781, minus_DI14=24.6326 |
| v1 | aroon_25_trend | 9922.86 | -77.14 | sell /  / Aroon25 Up > 70 그리고 Down < 30 (동률이면 최신 극값); 조건 미충족; Aroon_up=80, Aroon_down=92 |
| v1 | cci_20_momentum | 9950.47 | -49.53 | sell /  / CCI20 > 100 (전형가격·평균절대편차); 조건 미충족; CCI20=97.528 |
| v1 | williams_14_recovery | 9793.99 | -206.01 | sell /  / 직전 Williams %R14 < -80, 현재 >= -80 (한 봉 목표); 조건 미충족; Williams_R14=-9.39162, previous_R14=-72.4067 |
| v1 | cmf_20_accumulation | 9733.09 | -266.91 | buy /  / Chaikin Money Flow20 > 0.1; 조건 충족; CMF20=0.210229, volume20=2.88359e+08 |
| v1 | chaikin_3_10 | 9923.79 | -76.21 | buy /  / ADL의 EMA3 - EMA10 > 0 그리고 종가 > EMA26; 조건 충족; Chaikin3_10=1.42733e+07, ADL=1.66683e+08, close=719, EMA26=715.102 |
| v1 | roc_10_momentum | 9990.50 | -9.50 | sell /  / 10봉 ROC > 1% 그리고 종가 > EMA26; 조건 미충족; ROC10_percent=0.483561, close=722.477, EMA26=718.78 |
| v1 | trix_15_trend | 9933.37 | -66.63 | buy /  / 15봉 삼중 EMA의 1봉 변화율 TRIX > 0 그리고 종가 > EMA26; 조건 충족; TRIX15_percent=0.000507984, close=723.31, EMA26=718.484 |
| v1 | keltner_20_breakout | 9904.16 | -95.84 | sell /  / 종가 > EMA20 + 2 x Wilder ATR14; 조건 미충족; close=723.31, upper_Keltner=723.407, EMA20=718.722, ATR14=2.34265 |
| v1 | opening_range_30m | 9887.22 | -112.78 | sell /  / 뉴욕 09:30·09:45 두 완료 봉 최고가를 10:00 이후 종가가 돌파; 조건 미충족; close=719.99, opening_high=720.22 |
| v2 | cash | 10000.00 | 0.00 | 대기 /  / 새 신호 대기 |
| v2 | buy_hold | 9583.65 | -416.35 | buy / partial / 직전 완료 봉 목표 비중 100%; 다음 봉 시가 가정 |
| v2 | trend_8_26 | 9699.38 | -300.62 | buy / partial / 직전 완료 봉 목표 비중 100%; 다음 봉 시가 가정 |
| v2 | momentum_26 | 9733.52 | -266.48 | buy / partial / 직전 완료 봉 목표 비중 100%; 다음 봉 시가 가정 |
| v2 | breakout_8 | 9565.39 | -434.61 | sell / filled / 직전 완료 봉 목표 비중 0%; 다음 봉 시가 가정 |
| v2 | reversion_12 | 9383.03 | -616.97 | buy / partial / 직전 완료 봉 목표 비중 100%; 다음 봉 시가 가정 |
| v2 | volume_26 | 9565.80 | -434.20 | 중단: 손실 한도 / sell / filled / 직전 완료 봉 목표 비중 0%; 다음 봉 시가 가정 |
| v2 | trend_8_26 AND momentum_26 | 9800.89 | -199.11 | buy / partial / 직전 완료 봉 목표 비중 100%; 다음 봉 시가 가정 |
| v2 | trend_8_26 + momentum_26 | 9736.87 | -263.13 | buy / partial / 직전 완료 봉 목표 비중 100%; 다음 봉 시가 가정 |
| v2 | trend_8_26 AND breakout_8 | 9883.87 | -116.13 | sell / filled / 직전 완료 봉 목표 비중 0%; 다음 봉 시가 가정 |
| v2 | trend_8_26 + breakout_8 | 9652.28 | -347.72 | buy / filled / 직전 완료 봉 목표 비중 50%; 다음 봉 시가 가정 |
| v2 | trend_8_26 AND reversion_12 | 9790.91 | -209.09 | buy / partial / 직전 완료 봉 목표 비중 100%; 다음 봉 시가 가정 |
| v2 | trend_8_26 + reversion_12 | 9539.72 | -460.28 | buy / partial / 직전 완료 봉 목표 비중 100%; 다음 봉 시가 가정 |
| v2 | trend_8_26 AND volume_26 | 9769.99 | -230.01 | sell / filled / 직전 완료 봉 목표 비중 0%; 다음 봉 시가 가정 |
| v2 | trend_8_26 + volume_26 | 9433.53 | -566.47 | buy / filled / 직전 완료 봉 목표 비중 50%; 다음 봉 시가 가정 |
| v2 | momentum_26 AND breakout_8 | 9886.96 | -113.04 | sell / filled / 직전 완료 봉 목표 비중 0%; 다음 봉 시가 가정 |
| v2 | momentum_26 + breakout_8 | 9649.02 | -350.98 | buy / filled / 직전 완료 봉 목표 비중 50%; 다음 봉 시가 가정 |
| v2 | momentum_26 AND reversion_12 | 9928.78 | -71.22 | buy / partial / 직전 완료 봉 목표 비중 100%; 다음 봉 시가 가정 |
| v2 | momentum_26 + reversion_12 | 9576.58 | -423.42 | buy / partial / 직전 완료 봉 목표 비중 100%; 다음 봉 시가 가정 |
| v2 | momentum_26 AND volume_26 | 9845.67 | -154.33 | sell / filled / 직전 완료 봉 목표 비중 0%; 다음 봉 시가 가정 |
| v2 | momentum_26 + volume_26 | 9469.97 | -530.03 | buy / filled / 직전 완료 봉 목표 비중 50%; 다음 봉 시가 가정 |
| v2 | breakout_8 AND reversion_12 | 10000.00 | 0.00 | 대기 /  / 새 신호 대기 |
| v2 | breakout_8 + reversion_12 | 9533.44 | -466.56 | buy / filled / 직전 완료 봉 목표 비중 50%; 다음 봉 시가 가정 |
| v2 | breakout_8 AND volume_26 | 9891.45 | -108.55 | sell / filled / 직전 완료 봉 목표 비중 0%; 다음 봉 시가 가정 |
| v2 | breakout_8 + volume_26 | 9427.43 | -572.57 | sell / filled / 직전 완료 봉 목표 비중 0%; 다음 봉 시가 가정 |
| v2 | reversion_12 AND volume_26 | 9547.64 | -452.36 | 중단: 손실 한도 / sell / filled / 직전 완료 봉 목표 비중 0%; 다음 봉 시가 가정 |
| v2 | reversion_12 + volume_26 | 9337.33 | -662.67 | buy / filled / 직전 완료 봉 목표 비중 50%; 다음 봉 시가 가정 |
| v2 | ema_12_26 | 9891.37 | -108.63 | buy / partial / EMA12 > EMA26; 조건 충족; EMA12=717, EMA26=716.746; 직전 완료 봉 목표를 다음 봉 시가에 모의 적용 |
| v2 | macd_12_26_9 | 9891.37 | -108.63 | buy / partial / MACD > 신호선 그리고 MACD > 0; 조건 충족; MACD=0.254284, signal9=-1.34399; 직전 완료 봉 목표를 다음 봉 시가에 모의 적용 |
| v2 | rsi_14_recovery | 9807.13 | -192.87 | sell / filled / 직전 RSI14 < 30, 현재 RSI14 >= 30 (한 봉 목표); 조건 미충족; RSI14=58.2718, previous_RSI14=33.2263; 직전 완료 봉 목표를 다음 봉 시가에 모의 적용 |
| v2 | bollinger_20_reentry | 9878.29 | -121.71 | sell / filled / 직전 종가 < 직전 하단밴드, 현재 하단밴드 <= 종가 <= SMA20 (한 봉 목표); 조건 미충족; close=716.64, lower20=715.793, SMA20=723.132, previous_lower20=716.805; 직전 완료 봉 목표를 다음 봉 시가에 모의 적용 |
| v2 | donchian_20 | 9947.13 | -52.87 | sell / filled / 종가 > 현재 봉을 제외한 직전 20봉 최고가; 조건 미충족; close=724.13, prior_high20=724.151; 직전 완료 봉 목표를 다음 봉 시가에 모의 적용 |
| v2 | atr_14_breakout | 9943.55 | -56.45 | sell / filled / 종가 > 직전 종가 + 직전 ATR14 그리고 종가 > EMA26; 조건 미충족; close=717.88, threshold=721.828, prior_ATR14=2.82823, EMA26=715.308; 직전 완료 봉 목표를 다음 봉 시가에 모의 적용 |
| v2 | session_vwap | 9794.89 | -205.11 | sell / filled / 종가 > 뉴욕 거래일별 누적 전형가격 VWAP; 조건 미충족; close=721.515, session_VWAP=722.066, session_volume=4.49868e+08; 직전 완료 봉 목표를 다음 봉 시가에 모의 적용 |
| v2 | obv_20 | 9920.81 | -79.19 | buy / partial / OBV > OBV의 SMA20 그리고 종가 > EMA26; 조건 충족; OBV=-1.30207e+07, OBV_SMA20=-3.93901e+07, close=719, EMA26=715.102; 직전 완료 봉 목표를 다음 봉 시가에 모의 적용 |
| v2 | stochastic_14_3_recovery | 9694.13 | -305.87 | 중단: 손실 한도 / sell / filled / 직전 %K14 < 20에서 %K14가 %D3 상향 돌파 (한 봉 목표); 조건 미충족; K14=10.576, D3=8.00581, previous_K14=7.39787, previous_D3=7.27486; 직전 완료 봉 목표를 다음 봉 시가에 모의 적용 |
| v2 | mfi_14_recovery | 9925.16 | -74.84 | sell / filled / 직전 MFI14 < 20, 현재 MFI14 >= 20 (한 봉 목표); 조건 미충족; MFI14=58.7386, previous_MFI14=43.5194; 직전 완료 봉 목표를 다음 봉 시가에 모의 적용 |
| v2 | adx_14_trend | 9922.56 | -77.44 | sell / filled / Wilder ADX14 >= 25 그리고 +DI14 > -DI14; 조건 미충족; ADX14=23.9831, plus_DI14=26.5781, minus_DI14=24.6326; 직전 완료 봉 목표를 다음 봉 시가에 모의 적용 |
| v2 | aroon_25_trend | 9920.88 | -79.12 | sell / filled / Aroon25 Up > 70 그리고 Down < 30 (동률이면 최신 극값); 조건 미충족; Aroon_up=80, Aroon_down=92; 직전 완료 봉 목표를 다음 봉 시가에 모의 적용 |
| v2 | cci_20_momentum | 9946.49 | -53.51 | sell / filled / CCI20 > 100 (전형가격·평균절대편차); 조건 미충족; CCI20=97.528; 직전 완료 봉 목표를 다음 봉 시가에 모의 적용 |
| v2 | williams_14_recovery | 9786.16 | -213.84 | sell / filled / 직전 Williams %R14 < -80, 현재 >= -80 (한 봉 목표); 조건 미충족; Williams_R14=-9.39162, previous_R14=-72.4067; 직전 완료 봉 목표를 다음 봉 시가에 모의 적용 |
| v2 | cmf_20_accumulation | 9724.33 | -275.67 | buy / partial / Chaikin Money Flow20 > 0.1; 조건 충족; CMF20=0.210229, volume20=2.88359e+08; 직전 완료 봉 목표를 다음 봉 시가에 모의 적용 |
| v2 | chaikin_3_10 | 9920.81 | -79.19 | buy / partial / ADL의 EMA3 - EMA10 > 0 그리고 종가 > EMA26; 조건 충족; Chaikin3_10=1.42733e+07, ADL=1.66683e+08, close=719, EMA26=715.102; 직전 완료 봉 목표를 다음 봉 시가에 모의 적용 |
| v2 | roc_10_momentum | 9988.50 | -11.50 | sell / filled / 10봉 ROC > 1% 그리고 종가 > EMA26; 조건 미충족; ROC10_percent=0.483561, close=722.477, EMA26=718.78; 직전 완료 봉 목표를 다음 봉 시가에 모의 적용 |
| v2 | trix_15_trend | 9932.38 | -67.62 | buy / partial / 15봉 삼중 EMA의 1봉 변화율 TRIX > 0 그리고 종가 > EMA26; 조건 충족; TRIX15_percent=0.000507984, close=723.31, EMA26=718.484; 직전 완료 봉 목표를 다음 봉 시가에 모의 적용 |
| v2 | keltner_20_breakout | 9900.20 | -99.80 | sell / filled / 종가 > EMA20 + 2 x Wilder ATR14; 조건 미충족; close=723.31, upper_Keltner=723.407, EMA20=718.722, ATR14=2.34265; 직전 완료 봉 목표를 다음 봉 시가에 모의 적용 |
| v2 | opening_range_30m | 9883.27 | -116.73 | sell / filled / 뉴욕 09:30·09:45 두 완료 봉 최고가를 10:00 이후 종가가 돌파; 조건 미충족; close=719.99, opening_high=720.22; 직전 완료 봉 목표를 다음 봉 시가에 모의 적용 |

### 같은 기간의 비용·노출 비교 (사후 연구)

| 전략 | 비용 전 | 비용 후 | 100% 보유 | 같은 평균 노출 보유 | 평균 노출 |
|---|---:|---:|---:|---:|---:|
| cash | 0.00% | 0.00% | -2.77% | -0.00% | 0.00% |
| buy_hold | -2.36% | -2.77% | -2.77% | -2.77% | 100.00% |
| trend_8_26 | 0.60% | -3.13% | -2.77% | -1.27% | 45.93% |
| momentum_26 | -1.13% | -6.38% | -2.77% | -1.10% | 39.90% |
| breakout_8 | -0.79% | -16.13% | -2.77% | -0.52% | 18.90% |
| reversion_12 | -0.22% | -13.13% | -2.77% | -0.81% | 29.40% |
| volume_26 | -1.51% | -14.98% | -2.77% | -0.44% | 16.01% |
| trend_8_26 AND momentum_26 | 0.11% | -4.01% | -2.77% | -0.96% | 34.91% |
| trend_8_26 + momentum_26 | -0.26% | -4.37% | -2.77% | -1.18% | 42.92% |
| trend_8_26 AND breakout_8 | -0.02% | -9.22% | -2.77% | -0.32% | 11.55% |
| trend_8_26 + breakout_8 | -0.09% | -9.30% | -2.77% | -0.89% | 32.42% |
| trend_8_26 AND reversion_12 | 0.08% | -5.63% | -2.77% | -0.18% | 6.56% |
| trend_8_26 + reversion_12 | 0.20% | -7.89% | -2.77% | -1.04% | 37.67% |
| trend_8_26 AND volume_26 | -0.24% | -5.54% | -2.77% | -0.15% | 5.51% |
| trend_8_26 + volume_26 | -0.45% | -9.06% | -2.77% | -0.85% | 30.98% |
| momentum_26 AND breakout_8 | -0.03% | -9.24% | -2.77% | -0.31% | 11.29% |
| momentum_26 + breakout_8 | -0.95% | -11.21% | -2.77% | -0.81% | 29.40% |
| momentum_26 AND reversion_12 | -0.29% | -5.99% | -2.77% | -0.15% | 5.51% |
| momentum_26 + reversion_12 | -0.67% | -9.45% | -2.77% | -0.96% | 34.65% |
| momentum_26 AND volume_26 | -0.04% | -4.56% | -2.77% | -0.12% | 4.20% |
| momentum_26 + volume_26 | -1.32% | -10.41% | -2.77% | -0.77% | 27.96% |
| breakout_8 AND reversion_12 | 0.00% | 0.00% | -2.77% | -0.00% | 0.00% |
| breakout_8 + reversion_12 | -0.49% | -13.76% | -2.77% | -0.67% | 24.16% |
| breakout_8 AND volume_26 | 0.31% | -2.60% | -2.77% | -0.06% | 2.10% |
| breakout_8 + volume_26 | -1.15% | -14.13% | -2.77% | -0.48% | 17.46% |
| reversion_12 AND volume_26 | -1.76% | -8.92% | -2.77% | -0.24% | 8.66% |
| reversion_12 + volume_26 | -0.86% | -13.34% | -2.77% | -0.63% | 22.71% |
| ema_12_26 | 0.76% | -1.33% | -2.77% | -1.03% | 37.27% |
| macd_12_26_9 | 1.32% | -2.44% | -2.77% | -0.62% | 22.57% |
| rsi_14_recovery | -0.83% | -5.71% | -2.77% | -0.09% | 3.15% |
| bollinger_20_reentry | -0.44% | -6.12% | -2.77% | -0.10% | 3.67% |
| donchian_20 | 0.59% | -4.75% | -2.77% | -0.16% | 5.77% |
| atr_14_breakout | 0.11% | -4.01% | -2.77% | -0.08% | 2.89% |
| session_vwap | -0.59% | -12.36% | -2.77% | -1.35% | 48.82% |
| obv_20 | -0.72% | -9.10% | -2.77% | -0.82% | 29.92% |
| stochastic_14_3_recovery | -0.79% | -12.90% | -2.77% | -0.22% | 8.14% |
| mfi_14_recovery | -0.49% | -2.56% | -2.77% | -0.04% | 1.31% |
| adx_14_trend | -0.11% | -3.00% | -2.77% | -0.59% | 21.52% |
| aroon_25_trend | 1.40% | -1.95% | -2.77% | -0.54% | 19.69% |
| cci_20_momentum | -0.25% | -5.55% | -2.77% | -0.48% | 17.32% |
| williams_14_recovery | -1.02% | -12.01% | -2.77% | -0.20% | 7.35% |
| cmf_20_accumulation | -1.18% | -8.76% | -2.77% | -0.85% | 30.97% |
| chaikin_3_10 | -1.89% | -9.42% | -2.77% | -1.01% | 36.75% |
| roc_10_momentum | -0.00% | -1.67% | -2.77% | -0.12% | 4.20% |
| trix_15_trend | 0.46% | -1.21% | -2.77% | -0.84% | 30.45% |
| keltner_20_breakout | -0.89% | -5.76% | -2.77% | -0.22% | 8.14% |
| opening_range_30m | -0.39% | -6.47% | -2.77% | -0.68% | 24.67% |

동일 구간·초기 자금, 종료 시 청산 비용 포함. 노출 맞춤은 사후 설명용이며 v2 실제 계좌 성과가 아닙니다.
[낙폭 분해·비용 영향·전체 구간](QQQ/comparison.json)

[v1 전체 기록](QQQ/accounts.json) · [v2 전체 기록](QQQ/accounts-v2.json)

## IWM 계좌

| 모델 | 전략 | 평가액 USD | 손익 USD | 최근 매매·이유 |
|---|---|---:|---:|---|
| v1 | cash | 10000.00 | 0.00 | 대기 /  / 새 신호 대기 |
| v1 | buy_hold | 9825.72 | -174.28 | buy /  / buy_hold: prior completed bar target 100%; next bar open simulation |
| v1 | trend_8_26 | 9786.50 | -213.50 | buy /  / trend_8_26: prior completed bar target 100%; next bar open simulation |
| v1 | momentum_26 | 9802.40 | -197.60 | buy /  / momentum_26: prior completed bar target 100%; next bar open simulation |
| v1 | breakout_8 | 9788.68 | -211.32 | sell /  / breakout_8: prior completed bar target 0%; next bar open simulation |
| v1 | reversion_12 | 9861.22 | -138.78 | sell /  / reversion_12: prior completed bar target 0%; next bar open simulation |
| v1 | volume_26 | 9862.10 | -137.90 | sell /  / volume_26: prior completed bar target 0%; next bar open simulation |
| v1 | trend_8_26 AND momentum_26 | 9802.40 | -197.60 | buy /  / trend_8_26 AND momentum_26: prior completed bar target 100%; next bar open simulation |
| v1 | trend_8_26 + momentum_26 | 9794.44 | -205.56 | buy /  / trend_8_26 + momentum_26: prior completed bar target 100%; next bar open simulation |
| v1 | trend_8_26 AND breakout_8 | 9896.83 | -103.17 | sell /  / trend_8_26 AND breakout_8: prior completed bar target 0%; next bar open simulation |
| v1 | trend_8_26 + breakout_8 | 9787.57 | -212.43 | buy /  / trend_8_26 + breakout_8: prior completed bar target 50%; next bar open simulation |
| v1 | trend_8_26 AND reversion_12 | 9902.23 | -97.77 | sell /  / trend_8_26 AND reversion_12: prior completed bar target 0%; next bar open simulation |
| v1 | trend_8_26 + reversion_12 | 9823.71 | -176.29 | buy /  / trend_8_26 + reversion_12: prior completed bar target 50%; next bar open simulation |
| v1 | trend_8_26 AND volume_26 | 9935.98 | -64.02 | sell /  / trend_8_26 AND volume_26: prior completed bar target 0%; next bar open simulation |
| v1 | trend_8_26 + volume_26 | 9824.14 | -175.86 | buy /  / trend_8_26 + volume_26: prior completed bar target 50%; next bar open simulation |
| v1 | momentum_26 AND breakout_8 | 9929.38 | -70.62 | sell /  / momentum_26 AND breakout_8: prior completed bar target 0%; next bar open simulation |
| v1 | momentum_26 + breakout_8 | 9815.12 | -184.88 | sell /  / momentum_26 + breakout_8: prior completed bar target 50%; next bar open simulation |
| v1 | momentum_26 AND reversion_12 | 10000.00 | 0.00 | 대기 /  / 새 신호 대기 |
| v1 | momentum_26 + reversion_12 | 9851.35 | -148.65 | sell /  / momentum_26 + reversion_12: prior completed bar target 50%; next bar open simulation |
| v1 | momentum_26 AND volume_26 | 10000.00 | 0.00 | 대기 /  / 새 신호 대기 |
| v1 | momentum_26 + volume_26 | 9832.13 | -167.87 | sell /  / momentum_26 + volume_26: prior completed bar target 50%; next bar open simulation |
| v1 | breakout_8 AND reversion_12 | 10000.00 | 0.00 | 대기 /  / 새 신호 대기 |
| v1 | breakout_8 + reversion_12 | 9824.81 | -175.19 | sell /  / breakout_8 + reversion_12: prior completed bar target 0%; next bar open simulation |
| v1 | breakout_8 AND volume_26 | 9944.66 | -55.34 | sell /  / breakout_8 AND volume_26: prior completed bar target 0%; next bar open simulation |
| v1 | breakout_8 + volume_26 | 9825.26 | -174.74 | sell /  / breakout_8 + volume_26: prior completed bar target 0%; next bar open simulation |
| v1 | reversion_12 AND volume_26 | 9935.98 | -64.02 | sell /  / reversion_12 AND volume_26: prior completed bar target 0%; next bar open simulation |
| v1 | reversion_12 + volume_26 | 9881.38 | -118.62 | sell /  / reversion_12 + volume_26: prior completed bar target 0%; next bar open simulation |
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
| v1 | aroon_25_trend | 9862.11 | -137.89 | sell /  / Aroon25 Up > 70 그리고 Down < 30 (동률이면 최신 극값); 조건 미충족; Aroon_up=68, Aroon_down=100 |
| v1 | cci_20_momentum | 9879.55 | -120.45 | sell /  / CCI20 > 100 (전형가격·평균절대편차); 조건 미충족; CCI20=81.8699 |
| v1 | williams_14_recovery | 9903.90 | -96.10 | sell /  / 직전 Williams %R14 < -80, 현재 >= -80 (한 봉 목표); 조건 미충족; Williams_R14=-48.0732, previous_R14=-69.6736 |
| v1 | cmf_20_accumulation | 9799.11 | -200.89 | sell /  / Chaikin Money Flow20 > 0.1; 조건 미충족; CMF20=0.0512251, volume20=2.08469e+07 |
| v1 | chaikin_3_10 | 9805.17 | -194.83 | sell /  / ADL의 EMA3 - EMA10 > 0 그리고 종가 > EMA26; 조건 미충족; Chaikin3_10=-9609.69, ADL=-6.08839e+07, close=271.41, EMA26=271.689 |
| v1 | roc_10_momentum | 10000.00 | 0.00 | 대기 /  / 새 신호 대기 |
| v1 | trix_15_trend | 9895.73 | -104.27 | sell /  / 15봉 삼중 EMA의 1봉 변화율 TRIX > 0 그리고 종가 > EMA26; 조건 미충족; TRIX15_percent=0.0257204, close=273.74, EMA26=273.991 |
| v1 | keltner_20_breakout | 9937.31 | -62.69 | sell /  / 종가 > EMA20 + 2 x Wilder ATR14; 조건 미충족; close=274.88, upper_Keltner=275.161, EMA20=274.044, ATR14=0.558498 |
| v1 | opening_range_30m | 9968.03 | -31.97 | sell /  / 뉴욕 09:30·09:45 두 완료 봉 최고가를 10:00 이후 종가가 돌파; 자료 부족·변동폭 또는 거래량 없음: 대기; close=275.73 |
| v2 | cash | 10000.00 | 0.00 | 대기 /  / 새 신호 대기 |
| v2 | buy_hold | 9720.66 | -279.34 | buy / partial / 직전 완료 봉 목표 비중 100%; 다음 봉 시가 가정 |
| v2 | trend_8_26 | 9657.75 | -342.25 | buy / partial / 직전 완료 봉 목표 비중 100%; 다음 봉 시가 가정 |
| v2 | momentum_26 | 9672.51 | -327.49 | buy / partial / 직전 완료 봉 목표 비중 100%; 다음 봉 시가 가정 |
| v2 | breakout_8 | 9406.95 | -593.05 | sell / filled / 직전 완료 봉 목표 비중 0%; 다음 봉 시가 가정 |
| v2 | reversion_12 | 9400.65 | -599.35 | sell / filled / 직전 완료 봉 목표 비중 0%; 다음 봉 시가 가정 |
| v2 | volume_26 | 9378.42 | -621.58 | sell / filled / 직전 완료 봉 목표 비중 0%; 다음 봉 시가 가정 |
| v2 | trend_8_26 AND momentum_26 | 9821.63 | -178.37 | buy / partial / 직전 완료 봉 목표 비중 100%; 다음 봉 시가 가정 |
| v2 | trend_8_26 + momentum_26 | 9685.58 | -314.42 | buy / partial / 직전 완료 봉 목표 비중 100%; 다음 봉 시가 가정 |
| v2 | trend_8_26 AND breakout_8 | 9806.54 | -193.46 | sell / filled / 직전 완료 봉 목표 비중 0%; 다음 봉 시가 가정 |
| v2 | trend_8_26 + breakout_8 | 9551.68 | -448.32 | buy / filled / 직전 완료 봉 목표 비중 50%; 다음 봉 시가 가정 |
| v2 | trend_8_26 AND reversion_12 | 9783.25 | -216.75 | sell / filled / 직전 완료 봉 목표 비중 0%; 다음 봉 시가 가정 |
| v2 | trend_8_26 + reversion_12 | 9528.09 | -471.91 | buy / filled / 직전 완료 봉 목표 비중 50%; 다음 봉 시가 가정 |
| v2 | trend_8_26 AND volume_26 | 9797.73 | -202.27 | sell / filled / 직전 완료 봉 목표 비중 0%; 다음 봉 시가 가정 |
| v2 | trend_8_26 + volume_26 | 9536.97 | -463.03 | buy / filled / 직전 완료 봉 목표 비중 50%; 다음 봉 시가 가정 |
| v2 | momentum_26 AND breakout_8 | 9733.71 | -266.29 | sell / filled / 직전 완료 봉 목표 비중 0%; 다음 봉 시가 가정 |
| v2 | momentum_26 + breakout_8 | 9558.84 | -441.16 | sell / filled / 직전 완료 봉 목표 비중 50%; 다음 봉 시가 가정 |
| v2 | momentum_26 AND reversion_12 | 9960.59 | -39.41 | sell / filled / 직전 완료 봉 목표 비중 0%; 다음 봉 시가 가정 |
| v2 | momentum_26 + reversion_12 | 9575.27 | -424.73 | sell / filled / 직전 완료 봉 목표 비중 50%; 다음 봉 시가 가정 |
| v2 | momentum_26 AND volume_26 | 9897.79 | -102.21 | sell / filled / 직전 완료 봉 목표 비중 0%; 다음 봉 시가 가정 |
| v2 | momentum_26 + volume_26 | 9524.04 | -475.96 | sell / filled / 직전 완료 봉 목표 비중 50%; 다음 봉 시가 가정 |
| v2 | breakout_8 AND reversion_12 | 10000.00 | 0.00 | 대기 /  / 새 신호 대기 |
| v2 | breakout_8 + reversion_12 | 9442.90 | -557.10 | sell / filled / 직전 완료 봉 목표 비중 0%; 다음 봉 시가 가정 |
| v2 | breakout_8 AND volume_26 | 9690.16 | -309.84 | sell / filled / 직전 완료 봉 목표 비중 0%; 다음 봉 시가 가정 |
| v2 | breakout_8 + volume_26 | 9412.30 | -587.70 | sell / filled / 직전 완료 봉 목표 비중 0%; 다음 봉 시가 가정 |
| v2 | reversion_12 AND volume_26 | 9676.46 | -323.54 | sell / filled / 직전 완료 봉 목표 비중 0%; 다음 봉 시가 가정 |
| v2 | reversion_12 + volume_26 | 9428.81 | -571.19 | sell / filled / 직전 완료 봉 목표 비중 0%; 다음 봉 시가 가정 |
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
| v2 | aroon_25_trend | 9860.14 | -139.86 | sell / filled / Aroon25 Up > 70 그리고 Down < 30 (동률이면 최신 극값); 조건 미충족; Aroon_up=68, Aroon_down=100; 직전 완료 봉 목표를 다음 봉 시가에 모의 적용 |
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
| cash | 0.00% | 0.00% | -3.63% | -0.00% | 0.00% |
| buy_hold | -3.22% | -3.63% | -3.63% | -3.63% | 100.00% |
| trend_8_26 | -1.63% | -5.28% | -3.63% | -1.60% | 43.83% |
| momentum_26 | -2.63% | -8.58% | -3.63% | -1.40% | 38.32% |
| breakout_8 | -0.55% | -13.78% | -3.63% | -0.73% | 19.95% |
| reversion_12 | -2.43% | -14.70% | -3.63% | -1.10% | 30.18% |
| volume_26 | -2.82% | -9.90% | -3.63% | -0.32% | 8.66% |
| trend_8_26 AND momentum_26 | -1.51% | -5.96% | -3.63% | -1.22% | 33.33% |
| trend_8_26 + momentum_26 | -2.13% | -6.55% | -3.63% | -1.50% | 41.08% |
| trend_8_26 AND breakout_8 | -0.38% | -8.02% | -3.63% | -0.42% | 11.55% |
| trend_8_26 + breakout_8 | -1.08% | -9.44% | -3.63% | -1.17% | 31.90% |
| trend_8_26 AND reversion_12 | -0.76% | -4.84% | -3.63% | -0.19% | 5.25% |
| trend_8_26 + reversion_12 | -2.02% | -9.93% | -3.63% | -1.35% | 37.01% |
| trend_8_26 AND volume_26 | -1.20% | -4.47% | -3.63% | -0.12% | 3.15% |
| trend_8_26 + volume_26 | -2.22% | -7.43% | -3.63% | -0.96% | 26.25% |
| momentum_26 AND breakout_8 | -0.21% | -7.48% | -3.63% | -0.38% | 10.24% |
| momentum_26 + breakout_8 | -1.59% | -11.03% | -3.63% | -1.07% | 29.14% |
| momentum_26 AND reversion_12 | -0.01% | -2.90% | -3.63% | -0.09% | 2.36% |
| momentum_26 + reversion_12 | -2.53% | -10.40% | -3.63% | -1.25% | 34.26% |
| momentum_26 AND volume_26 | -1.25% | -3.30% | -3.63% | -0.06% | 1.57% |
| momentum_26 + volume_26 | -2.73% | -8.86% | -3.63% | -0.86% | 23.49% |
| breakout_8 AND reversion_12 | 0.00% | 0.00% | -3.63% | -0.00% | 0.00% |
| breakout_8 + reversion_12 | -1.49% | -13.53% | -3.63% | -0.92% | 25.07% |
| breakout_8 AND volume_26 | -1.46% | -4.31% | -3.63% | -0.09% | 2.36% |
| breakout_8 + volume_26 | -1.69% | -11.68% | -3.63% | -0.52% | 14.31% |
| reversion_12 AND volume_26 | -0.55% | -4.64% | -3.63% | -0.15% | 4.20% |
| reversion_12 + volume_26 | -2.62% | -11.60% | -3.63% | -0.71% | 19.43% |
| ema_12_26 | -0.23% | -2.71% | -3.63% | -1.57% | 43.04% |
| macd_12_26_9 | 1.54% | -0.99% | -3.63% | -1.02% | 27.82% |
| rsi_14_recovery | -0.86% | -6.52% | -3.63% | -0.13% | 3.67% |
| bollinger_20_reentry | -0.31% | -4.81% | -3.63% | -0.11% | 2.89% |
| donchian_20 | -0.20% | -5.10% | -3.63% | -0.20% | 5.51% |
| atr_14_breakout | -1.18% | -7.22% | -3.63% | -0.14% | 3.94% |
| session_vwap | -0.87% | -10.37% | -3.63% | -1.47% | 40.16% |
| obv_20 | 0.29% | -3.43% | -3.63% | -1.39% | 38.06% |
| stochastic_14_3_recovery | -1.20% | -15.06% | -3.63% | -0.35% | 9.45% |
| mfi_14_recovery | 0.24% | -3.88% | -3.63% | -0.10% | 2.62% |
| adx_14_trend | 0.00% | -3.30% | -3.63% | -1.13% | 30.97% |
| aroon_25_trend | -1.70% | -4.95% | -3.63% | -0.75% | 20.47% |
| cci_20_momentum | -2.04% | -8.41% | -3.63% | -0.67% | 18.37% |
| williams_14_recovery | -0.58% | -10.11% | -3.63% | -0.23% | 6.30% |
| cmf_20_accumulation | -1.81% | -7.80% | -3.63% | -0.64% | 17.59% |
| chaikin_3_10 | -1.82% | -7.82% | -3.63% | -1.13% | 30.97% |
| roc_10_momentum | -0.63% | -1.87% | -3.63% | -0.12% | 3.15% |
| trix_15_trend | 0.35% | -2.56% | -3.63% | -1.14% | 31.23% |
| keltner_20_breakout | -0.91% | -4.18% | -3.63% | -0.19% | 5.25% |
| opening_range_30m | 2.57% | -1.23% | -3.63% | -0.78% | 21.26% |

동일 구간·초기 자금, 종료 시 청산 비용 포함. 노출 맞춤은 사후 설명용이며 v2 실제 계좌 성과가 아닙니다.
[낙폭 분해·비용 영향·전체 구간](IWM/comparison.json)

[v1 전체 기록](IWM/accounts.json) · [v2 전체 기록](IWM/accounts-v2.json)

## DIA 계좌

| 모델 | 전략 | 평가액 USD | 손익 USD | 최근 매매·이유 |
|---|---|---:|---:|---|
| v1 | cash | 10000.00 | 0.00 | 대기 /  / 새 신호 대기 |
| v1 | buy_hold | 9906.93 | -93.07 | buy /  / buy_hold: prior completed bar target 100%; next bar open simulation |
| v1 | trend_8_26 | 9865.67 | -134.33 | buy /  / trend_8_26: prior completed bar target 100%; next bar open simulation |
| v1 | momentum_26 | 9909.03 | -90.97 | sell /  / momentum_26: prior completed bar target 0%; next bar open simulation |
| v1 | breakout_8 | 9806.43 | -193.57 | sell /  / breakout_8: prior completed bar target 0%; next bar open simulation |
| v1 | reversion_12 | 9892.53 | -107.47 | sell /  / reversion_12: prior completed bar target 0%; next bar open simulation |
| v1 | volume_26 | 9908.95 | -91.05 | sell /  / volume_26: prior completed bar target 0%; next bar open simulation |
| v1 | trend_8_26 AND momentum_26 | 9909.03 | -90.97 | sell /  / trend_8_26 AND momentum_26: prior completed bar target 0%; next bar open simulation |
| v1 | trend_8_26 + momentum_26 | 9887.30 | -112.70 | buy /  / trend_8_26 + momentum_26: prior completed bar target 50%; next bar open simulation |
| v1 | trend_8_26 AND breakout_8 | 9940.12 | -59.88 | sell /  / trend_8_26 AND breakout_8: prior completed bar target 0%; next bar open simulation |
| v1 | trend_8_26 + breakout_8 | 9855.63 | -144.37 | buy /  / trend_8_26 + breakout_8: prior completed bar target 50%; next bar open simulation |
| v1 | trend_8_26 AND reversion_12 | 9936.00 | -64.00 | sell /  / trend_8_26 AND reversion_12: prior completed bar target 0%; next bar open simulation |
| v1 | trend_8_26 + reversion_12 | 9878.98 | -121.02 | buy /  / trend_8_26 + reversion_12: prior completed bar target 50%; next bar open simulation |
| v1 | trend_8_26 AND volume_26 | 9943.10 | -56.90 | sell /  / trend_8_26 AND volume_26: prior completed bar target 0%; next bar open simulation |
| v1 | trend_8_26 + volume_26 | 9887.19 | -112.81 | buy /  / trend_8_26 + volume_26: prior completed bar target 50%; next bar open simulation |
| v1 | momentum_26 AND breakout_8 | 9940.12 | -59.88 | sell /  / momentum_26 AND breakout_8: prior completed bar target 0%; next bar open simulation |
| v1 | momentum_26 + breakout_8 | 9857.54 | -142.46 | sell /  / momentum_26 + breakout_8: prior completed bar target 0%; next bar open simulation |
| v1 | momentum_26 AND reversion_12 | 9940.78 | -59.22 | sell /  / momentum_26 AND reversion_12: prior completed bar target 0%; next bar open simulation |
| v1 | momentum_26 + reversion_12 | 9900.69 | -99.31 | sell /  / momentum_26 + reversion_12: prior completed bar target 0%; next bar open simulation |
| v1 | momentum_26 AND volume_26 | 9943.10 | -56.90 | sell /  / momentum_26 AND volume_26: prior completed bar target 0%; next bar open simulation |
| v1 | momentum_26 + volume_26 | 9908.93 | -91.07 | sell /  / momentum_26 + volume_26: prior completed bar target 0%; next bar open simulation |
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
| v1 | session_vwap | 9901.07 | -98.93 | buy /  / 종가 > 뉴욕 거래일별 누적 전형가격 VWAP; 조건 충족; close=519.01, session_VWAP=518.623, session_volume=840642 |
| v1 | obv_20 | 9880.35 | -119.65 | sell /  / OBV > OBV의 SMA20 그리고 종가 > EMA26; 조건 미충족; OBV=-9.70764e+06, OBV_SMA20=-9.69418e+06, close=520.09, EMA26=519.448 |
| v1 | stochastic_14_3_recovery | 9821.75 | -178.25 | sell /  / 직전 %K14 < 20에서 %K14가 %D3 상향 돌파 (한 봉 목표); 조건 미충족; K14=21.4008, D3=27.0401, previous_K14=46.6025, previous_D3=27.3524 |
| v1 | mfi_14_recovery | 9936.38 | -63.62 | sell /  / 직전 MFI14 < 20, 현재 MFI14 >= 20 (한 봉 목표); 조건 미충족; MFI14=44.8014, previous_MFI14=20.0271 |
| v1 | adx_14_trend | 9882.74 | -117.26 | sell /  / Wilder ADX14 >= 25 그리고 +DI14 > -DI14; 조건 미충족; ADX14=30.2264, plus_DI14=23.4608, minus_DI14=27.9688 |
| v1 | aroon_25_trend | 9903.86 | -96.14 | buy /  / Aroon25 Up > 70 그리고 Down < 30 (동률이면 최신 극값); 조건 충족; Aroon_up=76, Aroon_down=28 |
| v1 | cci_20_momentum | 9910.36 | -89.64 | sell /  / CCI20 > 100 (전형가격·평균절대편차); 조건 미충족; CCI20=46.8763 |
| v1 | williams_14_recovery | 9855.05 | -144.95 | sell /  / 직전 Williams %R14 < -80, 현재 >= -80 (한 봉 목표); 조건 미충족; Williams_R14=-78.5992, previous_R14=-53.3975 |
| v1 | cmf_20_accumulation | 9889.11 | -110.89 | buy /  / Chaikin Money Flow20 > 0.1; 조건 충족; CMF20=0.211244, volume20=2.96677e+06 |
| v1 | chaikin_3_10 | 9882.27 | -117.73 | sell /  / ADL의 EMA3 - EMA10 > 0 그리고 종가 > EMA26; 조건 미충족; Chaikin3_10=16638.1, ADL=-1.73546e+07, close=519.25, EMA26=519.462 |
| v1 | roc_10_momentum | 10000.00 | 0.00 | 대기 /  / 새 신호 대기 |
| v1 | trix_15_trend | 9928.27 | -71.73 | sell /  / 15봉 삼중 EMA의 1봉 변화율 TRIX > 0 그리고 종가 > EMA26; 조건 미충족; TRIX15_percent=0.0322153, close=521.26, EMA26=521.365 |
| v1 | keltner_20_breakout | 9940.12 | -59.88 | sell /  / 종가 > EMA20 + 2 x Wilder ATR14; 조건 미충족; close=522.89, upper_Keltner=523.089, EMA20=521.145, ATR14=0.971947 |
| v1 | opening_range_30m | 9891.98 | -108.02 | buy /  / 뉴욕 09:30·09:45 두 완료 봉 최고가를 10:00 이후 종가가 돌파; 조건 충족; close=519.48, opening_high=519.1 |
| v2 | cash | 10000.00 | 0.00 | 대기 /  / 새 신호 대기 |
| v2 | buy_hold | 10029.66 | 29.66 | buy / partial / 직전 완료 봉 목표 비중 100%; 다음 봉 시가 가정 |
| v2 | trend_8_26 | 9799.80 | -200.20 | buy / partial / 직전 완료 봉 목표 비중 100%; 다음 봉 시가 가정 |
| v2 | momentum_26 | 9952.08 | -47.92 | sell / filled / 직전 완료 봉 목표 비중 0%; 다음 봉 시가 가정 |
| v2 | breakout_8 | 9333.71 | -666.29 | sell / filled / 직전 완료 봉 목표 비중 0%; 다음 봉 시가 가정 |
| v2 | reversion_12 | 9589.97 | -410.03 | sell / filled / 직전 완료 봉 목표 비중 0%; 다음 봉 시가 가정 |
| v2 | volume_26 | 9625.87 | -374.13 | sell / filled / 직전 완료 봉 목표 비중 0%; 다음 봉 시가 가정 |
| v2 | trend_8_26 AND momentum_26 | 9947.46 | -52.54 | sell / filled / 직전 완료 봉 목표 비중 0%; 다음 봉 시가 가정 |
| v2 | trend_8_26 + momentum_26 | 9875.68 | -124.32 | buy / filled / 직전 완료 봉 목표 비중 50%; 다음 봉 시가 가정 |
| v2 | trend_8_26 AND breakout_8 | 9626.81 | -373.19 | sell / filled / 직전 완료 봉 목표 비중 0%; 다음 봉 시가 가정 |
| v2 | trend_8_26 + breakout_8 | 9584.02 | -415.98 | buy / filled / 직전 완료 봉 목표 비중 50%; 다음 봉 시가 가정 |
| v2 | trend_8_26 AND reversion_12 | 9746.03 | -253.97 | sell / filled / 직전 완료 봉 목표 비중 0%; 다음 봉 시가 가정 |
| v2 | trend_8_26 + reversion_12 | 9693.95 | -306.05 | buy / filled / 직전 완료 봉 목표 비중 50%; 다음 봉 시가 가정 |
| v2 | trend_8_26 AND volume_26 | 9800.82 | -199.18 | sell / filled / 직전 완료 봉 목표 비중 0%; 다음 봉 시가 가정 |
| v2 | trend_8_26 + volume_26 | 9732.72 | -267.28 | buy / filled / 직전 완료 봉 목표 비중 50%; 다음 봉 시가 가정 |
| v2 | momentum_26 AND breakout_8 | 9615.85 | -384.15 | sell / filled / 직전 완료 봉 목표 비중 0%; 다음 봉 시가 가정 |
| v2 | momentum_26 + breakout_8 | 9638.01 | -361.99 | sell / filled / 직전 완료 봉 목표 비중 0%; 다음 봉 시가 가정 |
| v2 | momentum_26 AND reversion_12 | 9895.03 | -104.97 | sell / filled / 직전 완료 봉 목표 비중 0%; 다음 봉 시가 가정 |
| v2 | momentum_26 + reversion_12 | 9769.08 | -230.92 | sell / filled / 직전 완료 봉 목표 비중 0%; 다음 봉 시가 가정 |
| v2 | momentum_26 AND volume_26 | 9733.77 | -266.23 | sell / filled / 직전 완료 봉 목표 비중 0%; 다음 봉 시가 가정 |
| v2 | momentum_26 + volume_26 | 9828.84 | -171.16 | sell / filled / 직전 완료 봉 목표 비중 0%; 다음 봉 시가 가정 |
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
| v2 | session_vwap | 9896.12 | -103.88 | buy / partial / 종가 > 뉴욕 거래일별 누적 전형가격 VWAP; 조건 충족; close=519.01, session_VWAP=518.623, session_volume=840642; 직전 완료 봉 목표를 다음 봉 시가에 모의 적용 |
| v2 | obv_20 | 9876.40 | -123.60 | sell / filled / OBV > OBV의 SMA20 그리고 종가 > EMA26; 조건 미충족; OBV=-9.70764e+06, OBV_SMA20=-9.69418e+06, close=520.09, EMA26=519.448; 직전 완료 봉 목표를 다음 봉 시가에 모의 적용 |
| v2 | stochastic_14_3_recovery | 9813.90 | -186.10 | sell / filled / 직전 %K14 < 20에서 %K14가 %D3 상향 돌파 (한 봉 목표); 조건 미충족; K14=21.4008, D3=27.0401, previous_K14=46.6025, previous_D3=27.3524; 직전 완료 봉 목표를 다음 봉 시가에 모의 적용 |
| v2 | mfi_14_recovery | 9932.40 | -67.60 | sell / filled / 직전 MFI14 < 20, 현재 MFI14 >= 20 (한 봉 목표); 조건 미충족; MFI14=44.8014, previous_MFI14=20.0271; 직전 완료 봉 목표를 다음 봉 시가에 모의 적용 |
| v2 | adx_14_trend | 9878.79 | -121.21 | sell / filled / Wilder ADX14 >= 25 그리고 +DI14 > -DI14; 조건 미충족; ADX14=30.2264, plus_DI14=23.4608, minus_DI14=27.9688; 직전 완료 봉 목표를 다음 봉 시가에 모의 적용 |
| v2 | aroon_25_trend | 9900.89 | -99.11 | buy / partial / Aroon25 Up > 70 그리고 Down < 30 (동률이면 최신 극값); 조건 충족; Aroon_up=76, Aroon_down=28; 직전 완료 봉 목표를 다음 봉 시가에 모의 적용 |
| v2 | cci_20_momentum | 9906.40 | -93.60 | sell / filled / CCI20 > 100 (전형가격·평균절대편차); 조건 미충족; CCI20=46.8763; 직전 완료 봉 목표를 다음 봉 시가에 모의 적용 |
| v2 | williams_14_recovery | 9849.14 | -150.86 | sell / filled / 직전 Williams %R14 < -80, 현재 >= -80 (한 봉 목표); 조건 미충족; Williams_R14=-78.5992, previous_R14=-53.3975; 직전 완료 봉 목표를 다음 봉 시가에 모의 적용 |
| v2 | cmf_20_accumulation | 9886.15 | -113.85 | buy / partial / Chaikin Money Flow20 > 0.1; 조건 충족; CMF20=0.211244, volume20=2.96677e+06; 직전 완료 봉 목표를 다음 봉 시가에 모의 적용 |
| v2 | chaikin_3_10 | 9878.32 | -121.68 | sell / filled / ADL의 EMA3 - EMA10 > 0 그리고 종가 > EMA26; 조건 미충족; Chaikin3_10=16638.1, ADL=-1.73546e+07, close=519.25, EMA26=519.462; 직전 완료 봉 목표를 다음 봉 시가에 모의 적용 |
| v2 | roc_10_momentum | 10000.00 | 0.00 | 대기 /  / 새 신호 대기 |
| v2 | trix_15_trend | 9926.28 | -73.72 | sell / filled / 15봉 삼중 EMA의 1봉 변화율 TRIX > 0 그리고 종가 > EMA26; 조건 미충족; TRIX15_percent=0.0322153, close=521.26, EMA26=521.365; 직전 완료 봉 목표를 다음 봉 시가에 모의 적용 |
| v2 | keltner_20_breakout | 9938.13 | -61.87 | sell / filled / 종가 > EMA20 + 2 x Wilder ATR14; 조건 미충족; close=522.89, upper_Keltner=523.089, EMA20=521.145, ATR14=0.971947; 직전 완료 봉 목표를 다음 봉 시가에 모의 적용 |
| v2 | opening_range_30m | 9887.03 | -112.97 | buy / partial / 뉴욕 09:30·09:45 두 완료 봉 최고가를 10:00 이후 종가가 돌파; 조건 충족; close=519.48, opening_high=519.1; 직전 완료 봉 목표를 다음 봉 시가에 모의 적용 |

### 같은 기간의 비용·노출 비교 (사후 연구)

| 전략 | 비용 전 | 비용 후 | 100% 보유 | 같은 평균 노출 보유 | 평균 노출 |
|---|---:|---:|---:|---:|---:|
| cash | 0.00% | 0.00% | 0.51% | 0.00% | 0.00% |
| buy_hold | 0.93% | 0.51% | 0.51% | 0.51% | 100.00% |
| trend_8_26 | 1.24% | -2.51% | 0.51% | 0.28% | 55.12% |
| momentum_26 | 0.30% | -3.01% | 0.51% | 0.25% | 50.13% |
| breakout_8 | 0.79% | -16.21% | 0.51% | 0.12% | 23.10% |
| reversion_12 | -1.64% | -9.57% | 0.51% | 0.13% | 25.72% |
| volume_26 | -0.92% | -10.79% | 0.51% | 0.05% | 10.50% |
| trend_8_26 AND momentum_26 | 1.41% | -1.94% | 0.51% | 0.23% | 44.88% |
| trend_8_26 + momentum_26 | 0.77% | -2.76% | 0.51% | 0.27% | 52.63% |
| trend_8_26 AND breakout_8 | 1.06% | -10.53% | 0.51% | 0.07% | 14.70% |
| trend_8_26 + breakout_8 | 1.02% | -9.24% | 0.51% | 0.20% | 39.11% |
| trend_8_26 AND reversion_12 | -0.02% | -4.93% | 0.51% | 0.03% | 6.56% |
| trend_8_26 + reversion_12 | -0.21% | -5.92% | 0.51% | 0.21% | 40.42% |
| trend_8_26 AND volume_26 | 0.36% | -4.57% | 0.51% | 0.02% | 4.72% |
| trend_8_26 + volume_26 | 0.16% | -6.56% | 0.51% | 0.17% | 32.81% |
| momentum_26 AND breakout_8 | 0.26% | -10.87% | 0.51% | 0.08% | 14.96% |
| momentum_26 + breakout_8 | 0.55% | -9.67% | 0.51% | 0.19% | 36.62% |
| momentum_26 AND reversion_12 | -0.27% | -3.57% | 0.51% | 0.03% | 5.77% |
| momentum_26 + reversion_12 | -0.67% | -5.76% | 0.51% | 0.19% | 37.93% |
| momentum_26 AND volume_26 | -0.56% | -5.45% | 0.51% | 0.02% | 4.46% |
| momentum_26 + volume_26 | -0.31% | -6.40% | 0.51% | 0.15% | 30.32% |
| breakout_8 AND reversion_12 | 0.00% | 0.00% | 0.51% | 0.00% | 0.00% |
| breakout_8 + reversion_12 | -0.43% | -12.78% | 0.51% | 0.12% | 24.42% |
| breakout_8 AND volume_26 | -0.73% | -3.60% | 0.51% | 0.01% | 2.62% |
| breakout_8 + volume_26 | -0.06% | -12.82% | 0.51% | 0.09% | 16.81% |
| reversion_12 AND volume_26 | -0.19% | -5.09% | 0.51% | 0.02% | 3.94% |
| reversion_12 + volume_26 | -1.28% | -10.00% | 0.51% | 0.09% | 18.12% |
| ema_12_26 | 0.17% | -1.91% | 0.51% | 0.25% | 48.82% |
| macd_12_26_9 | 1.65% | -1.30% | 0.51% | 0.14% | 27.56% |
| rsi_14_recovery | 0.01% | -2.07% | 0.51% | 0.01% | 1.31% |
| bollinger_20_reentry | -0.09% | -5.00% | 0.51% | 0.02% | 3.15% |
| donchian_20 | 0.31% | -6.21% | 0.51% | 0.04% | 8.40% |
| atr_14_breakout | -0.66% | -7.51% | 0.51% | 0.03% | 5.25% |
| session_vwap | 2.07% | -5.76% | 0.51% | 0.24% | 48.03% |
| obv_20 | 0.66% | -6.67% | 0.51% | 0.21% | 41.21% |
| stochastic_14_3_recovery | 0.56% | -12.45% | 0.51% | 0.04% | 8.66% |
| mfi_14_recovery | 0.10% | -3.61% | 0.51% | 0.01% | 2.36% |
| adx_14_trend | 0.20% | -3.52% | 0.51% | 0.17% | 32.55% |
| aroon_25_trend | 0.50% | -2.82% | 0.51% | 0.13% | 25.20% |
| cci_20_momentum | 0.61% | -5.53% | 0.51% | 0.13% | 24.93% |
| williams_14_recovery | 0.97% | -7.55% | 0.51% | 0.03% | 5.51% |
| cmf_20_accumulation | 0.88% | -6.07% | 0.51% | 0.13% | 26.25% |
| chaikin_3_10 | 1.87% | -6.73% | 0.51% | 0.21% | 40.68% |
| roc_10_momentum | 0.15% | -0.27% | 0.51% | 0.01% | 1.31% |
| trix_15_trend | 0.19% | -3.12% | 0.51% | 0.21% | 41.99% |
| keltner_20_breakout | 0.33% | -5.79% | 0.51% | 0.09% | 16.80% |
| opening_range_30m | 1.77% | -3.24% | 0.51% | 0.11% | 21.52% |

동일 구간·초기 자금, 종료 시 청산 비용 포함. 노출 맞춤은 사후 설명용이며 v2 실제 계좌 성과가 아닙니다.
[낙폭 분해·비용 영향·전체 구간](DIA/comparison.json)

[v1 전체 기록](DIA/accounts.json) · [v2 전체 기록](DIA/accounts-v2.json)

## MSFT 계좌

| 모델 | 전략 | 평가액 USD | 손익 USD | 최근 매매·이유 |
|---|---|---:|---:|---|
| v1 | cash | 10000.00 | 0.00 | 대기 /  / 새 신호 대기 |
| v1 | buy_hold | 9840.03 | -159.97 | buy /  / buy_hold: prior completed bar target 100%; next bar open simulation |
| v1 | trend_8_26 | 9822.58 | -177.42 | buy /  / trend_8_26: prior completed bar target 100%; next bar open simulation |
| v1 | momentum_26 | 9793.60 | -206.40 | buy /  / momentum_26: prior completed bar target 100%; next bar open simulation |
| v1 | breakout_8 | 9876.66 | -123.34 | sell /  / breakout_8: prior completed bar target 0%; next bar open simulation |
| v1 | reversion_12 | 9784.80 | -215.20 | buy /  / reversion_12: prior completed bar target 100%; next bar open simulation |
| v1 | volume_26 | 9811.31 | -188.69 | sell /  / volume_26: prior completed bar target 0%; next bar open simulation |
| v1 | trend_8_26 AND momentum_26 | 9807.89 | -192.11 | buy /  / trend_8_26 AND momentum_26: prior completed bar target 100%; next bar open simulation |
| v1 | trend_8_26 + momentum_26 | 9808.10 | -191.90 | buy /  / trend_8_26 + momentum_26: prior completed bar target 100%; next bar open simulation |
| v1 | trend_8_26 AND breakout_8 | 9905.03 | -94.97 | sell /  / trend_8_26 AND breakout_8: prior completed bar target 0%; next bar open simulation |
| v1 | trend_8_26 + breakout_8 | 9869.30 | -130.70 | buy /  / trend_8_26 + breakout_8: prior completed bar target 50%; next bar open simulation |
| v1 | trend_8_26 AND reversion_12 | 9906.53 | -93.47 | buy /  / trend_8_26 AND reversion_12: prior completed bar target 100%; next bar open simulation |
| v1 | trend_8_26 + reversion_12 | 9803.63 | -196.37 | buy /  / trend_8_26 + reversion_12: prior completed bar target 100%; next bar open simulation |
| v1 | trend_8_26 AND volume_26 | 9916.79 | -83.21 | sell /  / trend_8_26 AND volume_26: prior completed bar target 0%; next bar open simulation |
| v1 | trend_8_26 + volume_26 | 9816.90 | -183.10 | buy /  / trend_8_26 + volume_26: prior completed bar target 50%; next bar open simulation |
| v1 | momentum_26 AND breakout_8 | 9905.03 | -94.97 | sell /  / momentum_26 AND breakout_8: prior completed bar target 0%; next bar open simulation |
| v1 | momentum_26 + breakout_8 | 9835.03 | -164.97 | buy /  / momentum_26 + breakout_8: prior completed bar target 50%; next bar open simulation |
| v1 | momentum_26 AND reversion_12 | 9892.09 | -107.91 | buy /  / momentum_26 AND reversion_12: prior completed bar target 100%; next bar open simulation |
| v1 | momentum_26 + reversion_12 | 9789.16 | -210.84 | buy /  / momentum_26 + reversion_12: prior completed bar target 100%; next bar open simulation |
| v1 | momentum_26 AND volume_26 | 9916.79 | -83.21 | sell /  / momentum_26 AND volume_26: prior completed bar target 0%; next bar open simulation |
| v1 | momentum_26 + volume_26 | 9802.41 | -197.59 | buy /  / momentum_26 + volume_26: prior completed bar target 50%; next bar open simulation |
| v1 | breakout_8 AND reversion_12 | 10000.00 | 0.00 | 대기 /  / 새 신호 대기 |
| v1 | breakout_8 + reversion_12 | 9850.22 | -149.78 | buy /  / breakout_8 + reversion_12: prior completed bar target 50%; next bar open simulation |
| v1 | breakout_8 AND volume_26 | 9953.19 | -46.81 | sell /  / breakout_8 AND volume_26: prior completed bar target 0%; next bar open simulation |
| v1 | breakout_8 + volume_26 | 9863.58 | -136.42 | sell /  / breakout_8 + volume_26: prior completed bar target 0%; next bar open simulation |
| v1 | reversion_12 AND volume_26 | 9938.00 | -62.00 | sell /  / reversion_12 AND volume_26: prior completed bar target 0%; next bar open simulation |
| v1 | reversion_12 + volume_26 | 9797.95 | -202.05 | buy /  / reversion_12 + volume_26: prior completed bar target 50%; next bar open simulation |
| v1 | ema_12_26 | 9807.89 | -192.11 | buy /  / EMA12 > EMA26; 조건 충족; EMA12=531.372, EMA26=531.07 |
| v1 | macd_12_26_9 | 9843.99 | -156.01 | buy /  / MACD > 신호선 그리고 MACD > 0; 조건 충족; MACD=0.301143, signal9=-0.952827 |
| v1 | rsi_14_recovery | 9960.54 | -39.46 | sell /  / 직전 RSI14 < 30, 현재 RSI14 >= 30 (한 봉 목표); 조건 미충족; RSI14=56.2522, previous_RSI14=46.6115 |
| v1 | bollinger_20_reentry | 9885.00 | -115.00 | sell /  / 직전 종가 < 직전 하단밴드, 현재 하단밴드 <= 종가 <= SMA20 (한 봉 목표); 조건 미충족; close=529.125, lower20=527.516, SMA20=535.918, previous_lower20=528.497 |
| v1 | donchian_20 | 9912.16 | -87.84 | sell /  / 종가 > 현재 봉을 제외한 직전 20봉 최고가; 조건 미충족; close=534.52, prior_high20=535.44 |
| v1 | atr_14_breakout | 9915.10 | -84.90 | sell /  / 종가 > 직전 종가 + 직전 ATR14 그리고 종가 > EMA26; 조건 미충족; close=533.975, threshold=536.307, prior_ATR14=2.16203, EMA26=530.521 |
| v1 | session_vwap | 9894.65 | -105.35 | sell /  / 종가 > 뉴욕 거래일별 누적 전형가격 VWAP; 조건 미충족; close=534.125, session_VWAP=534.159, session_volume=2.7999e+07 |
| v1 | obv_20 | 9798.38 | -201.62 | sell /  / OBV > OBV의 SMA20 그리고 종가 > EMA26; 조건 미충족; OBV=1.07848e+08, OBV_SMA20=1.07988e+08, close=533.345, EMA26=532.447 |
| v1 | stochastic_14_3_recovery | 9792.37 | -207.63 | sell /  / 직전 %K14 < 20에서 %K14가 %D3 상향 돌파 (한 봉 목표); 조건 미충족; K14=25.4855, D3=14.0848, previous_K14=10.0077, previous_D3=7.52857 |
| v1 | mfi_14_recovery | 10009.36 | 9.36 | sell /  / 직전 MFI14 < 20, 현재 MFI14 >= 20 (한 봉 목표); 조건 미충족; MFI14=25.2915, previous_MFI14=22.266 |
| v1 | adx_14_trend | 9902.31 | -97.69 | buy /  / Wilder ADX14 >= 25 그리고 +DI14 > -DI14; 조건 충족; ADX14=40.5315, plus_DI14=26.6727, minus_DI14=23.8299 |
| v1 | aroon_25_trend | 9823.56 | -176.44 | buy /  / Aroon25 Up > 70 그리고 Down < 30 (동률이면 최신 극값); 조건 충족; Aroon_up=92, Aroon_down=28 |
| v1 | cci_20_momentum | 10012.15 | 12.15 | sell /  / CCI20 > 100 (전형가격·평균절대편차); 조건 미충족; CCI20=86.441 |
| v1 | williams_14_recovery | 9822.57 | -177.43 | sell /  / 직전 Williams %R14 < -80, 현재 >= -80 (한 봉 목표); 조건 미충족; Williams_R14=-78.4506, previous_R14=-77.7733 |
| v1 | cmf_20_accumulation | 9748.47 | -251.53 | buy /  / Chaikin Money Flow20 > 0.1; 조건 충족; CMF20=0.184396, volume20=3.37825e+07 |
| v1 | chaikin_3_10 | 9834.97 | -165.03 | sell /  / ADL의 EMA3 - EMA10 > 0 그리고 종가 > EMA26; 조건 미충족; Chaikin3_10=-39308.5, ADL=1.1146e+08, close=533.345, EMA26=532.447 |
| v1 | roc_10_momentum | 9959.43 | -40.57 | sell /  / 10봉 ROC > 1% 그리고 종가 > EMA26; 조건 미충족; ROC10_percent=0.454191, close=534.125, EMA26=532.186 |
| v1 | trix_15_trend | 9858.09 | -141.91 | buy /  / 15봉 삼중 EMA의 1봉 변화율 TRIX > 0 그리고 종가 > EMA26; 조건 충족; TRIX15_percent=0.00435677, close=534.125, EMA26=532.186 |
| v1 | keltner_20_breakout | 9958.78 | -41.22 | sell /  / 종가 > EMA20 + 2 x Wilder ATR14; 조건 미충족; close=533.975, upper_Keltner=534.357, EMA20=530.111, ATR14=2.12332 |
| v1 | opening_range_30m | 9857.44 | -142.56 | buy /  / 뉴욕 09:30·09:45 두 완료 봉 최고가를 10:00 이후 종가가 돌파; 조건 충족; close=534.145, opening_high=532.63 |
| v2 | cash | 10000.00 | 0.00 | 대기 /  / 새 신호 대기 |
| v2 | buy_hold | 9893.72 | -106.28 | buy / partial / 직전 완료 봉 목표 비중 100%; 다음 봉 시가 가정 |
| v2 | trend_8_26 | 9758.30 | -241.70 | buy / partial / 직전 완료 봉 목표 비중 100%; 다음 봉 시가 가정 |
| v2 | momentum_26 | 9839.26 | -160.74 | buy / partial / 직전 완료 봉 목표 비중 100%; 다음 봉 시가 가정 |
| v2 | breakout_8 | 9670.87 | -329.13 | sell / filled / 직전 완료 봉 목표 비중 0%; 다음 봉 시가 가정 |
| v2 | reversion_12 | 9406.92 | -593.08 | buy / partial / 직전 완료 봉 목표 비중 100%; 다음 봉 시가 가정 |
| v2 | volume_26 | 9498.13 | -501.87 | sell / filled / 직전 완료 봉 목표 비중 0%; 다음 봉 시가 가정 |
| v2 | trend_8_26 AND momentum_26 | 9704.85 | -295.15 | buy / partial / 직전 완료 봉 목표 비중 100%; 다음 봉 시가 가정 |
| v2 | trend_8_26 + momentum_26 | 9798.97 | -201.03 | buy / partial / 직전 완료 봉 목표 비중 100%; 다음 봉 시가 가정 |
| v2 | trend_8_26 AND breakout_8 | 9543.92 | -456.08 | sell / filled / 직전 완료 봉 목표 비중 0%; 다음 봉 시가 가정 |
| v2 | trend_8_26 + breakout_8 | 9755.58 | -244.42 | buy / filled / 직전 완료 봉 목표 비중 50%; 다음 봉 시가 가정 |
| v2 | trend_8_26 AND reversion_12 | 9804.62 | -195.38 | buy / partial / 직전 완료 봉 목표 비중 100%; 다음 봉 시가 가정 |
| v2 | trend_8_26 + reversion_12 | 9580.62 | -419.38 | buy / partial / 직전 완료 봉 목표 비중 100%; 다음 봉 시가 가정 |
| v2 | trend_8_26 AND volume_26 | 9861.94 | -138.06 | sell / filled / 직전 완료 봉 목표 비중 0%; 다음 봉 시가 가정 |
| v2 | trend_8_26 + volume_26 | 9647.33 | -352.67 | buy / filled / 직전 완료 봉 목표 비중 50%; 다음 봉 시가 가정 |
| v2 | momentum_26 AND breakout_8 | 9697.48 | -302.52 | sell / filled / 직전 완료 봉 목표 비중 0%; 다음 봉 시가 가정 |
| v2 | momentum_26 + breakout_8 | 9754.76 | -245.24 | buy / filled / 직전 완료 봉 목표 비중 50%; 다음 봉 시가 가정 |
| v2 | momentum_26 AND reversion_12 | 9717.93 | -282.07 | buy / partial / 직전 완료 봉 목표 비중 100%; 다음 봉 시가 가정 |
| v2 | momentum_26 + reversion_12 | 9620.41 | -379.59 | buy / partial / 직전 완료 봉 목표 비중 100%; 다음 봉 시가 가정 |
| v2 | momentum_26 AND volume_26 | 9785.21 | -214.79 | sell / filled / 직전 완료 봉 목표 비중 0%; 다음 봉 시가 가정 |
| v2 | momentum_26 + volume_26 | 9687.41 | -312.59 | buy / filled / 직전 완료 봉 목표 비중 50%; 다음 봉 시가 가정 |
| v2 | breakout_8 AND reversion_12 | 10000.00 | 0.00 | 대기 /  / 새 신호 대기 |
| v2 | breakout_8 + reversion_12 | 9577.83 | -422.17 | buy / filled / 직전 완료 봉 목표 비중 50%; 다음 봉 시가 가정 |
| v2 | breakout_8 AND volume_26 | 9890.09 | -109.91 | sell / filled / 직전 완료 봉 목표 비중 0%; 다음 봉 시가 가정 |
| v2 | breakout_8 + volume_26 | 9624.43 | -375.57 | sell / filled / 직전 완료 봉 목표 비중 0%; 다음 봉 시가 가정 |
| v2 | reversion_12 AND volume_26 | 9699.57 | -300.43 | sell / filled / 직전 완료 봉 목표 비중 0%; 다음 봉 시가 가정 |
| v2 | reversion_12 + volume_26 | 9452.16 | -547.84 | buy / filled / 직전 완료 봉 목표 비중 50%; 다음 봉 시가 가정 |
| v2 | ema_12_26 | 9804.95 | -195.05 | buy / partial / EMA12 > EMA26; 조건 충족; EMA12=531.372, EMA26=531.07; 직전 완료 봉 목표를 다음 봉 시가에 모의 적용 |
| v2 | macd_12_26_9 | 9841.04 | -158.96 | buy / partial / MACD > 신호선 그리고 MACD > 0; 조건 충족; MACD=0.301143, signal9=-0.952827; 직전 완료 봉 목표를 다음 봉 시가에 모의 적용 |
| v2 | rsi_14_recovery | 9956.56 | -43.44 | sell / filled / 직전 RSI14 < 30, 현재 RSI14 >= 30 (한 봉 목표); 조건 미충족; RSI14=56.2522, previous_RSI14=46.6115; 직전 완료 봉 목표를 다음 봉 시가에 모의 적용 |
| v2 | bollinger_20_reentry | 9881.05 | -118.95 | sell / filled / 직전 종가 < 직전 하단밴드, 현재 하단밴드 <= 종가 <= SMA20 (한 봉 목표); 조건 미충족; close=529.125, lower20=527.516, SMA20=535.918, previous_lower20=528.497; 직전 완료 봉 목표를 다음 봉 시가에 모의 적용 |
| v2 | donchian_20 | 9908.19 | -91.81 | sell / filled / 종가 > 현재 봉을 제외한 직전 20봉 최고가; 조건 미충족; close=534.52, prior_high20=535.44; 직전 완료 봉 목표를 다음 봉 시가에 모의 적용 |
| v2 | atr_14_breakout | 9911.14 | -88.86 | sell / filled / 종가 > 직전 종가 + 직전 ATR14 그리고 종가 > EMA26; 조건 미충족; close=533.975, threshold=536.307, prior_ATR14=2.16203, EMA26=530.521; 직전 완료 봉 목표를 다음 봉 시가에 모의 적용 |
| v2 | session_vwap | 9890.69 | -109.31 | sell / filled / 종가 > 뉴욕 거래일별 누적 전형가격 VWAP; 조건 미충족; close=534.125, session_VWAP=534.159, session_volume=2.7999e+07; 직전 완료 봉 목표를 다음 봉 시가에 모의 적용 |
| v2 | obv_20 | 9792.50 | -207.50 | sell / filled / OBV > OBV의 SMA20 그리고 종가 > EMA26; 조건 미충족; OBV=1.07848e+08, OBV_SMA20=1.07988e+08, close=533.345, EMA26=532.447; 직전 완료 봉 목표를 다음 봉 시가에 모의 적용 |
| v2 | stochastic_14_3_recovery | 9784.54 | -215.46 | sell / filled / 직전 %K14 < 20에서 %K14가 %D3 상향 돌파 (한 봉 목표); 조건 미충족; K14=25.4855, D3=14.0848, previous_K14=10.0077, previous_D3=7.52857; 직전 완료 봉 목표를 다음 봉 시가에 모의 적용 |
| v2 | mfi_14_recovery | 10007.36 | 7.36 | sell / filled / 직전 MFI14 < 20, 현재 MFI14 >= 20 (한 봉 목표); 조건 미충족; MFI14=25.2915, previous_MFI14=22.266; 직전 완료 봉 목표를 다음 봉 시가에 모의 적용 |
| v2 | adx_14_trend | 9899.34 | -100.66 | buy / partial / Wilder ADX14 >= 25 그리고 +DI14 > -DI14; 조건 충족; ADX14=40.5315, plus_DI14=26.6727, minus_DI14=23.8299; 직전 완료 봉 목표를 다음 봉 시가에 모의 적용 |
| v2 | aroon_25_trend | 9820.62 | -179.38 | buy / partial / Aroon25 Up > 70 그리고 Down < 30 (동률이면 최신 극값); 조건 충족; Aroon_up=92, Aroon_down=28; 직전 완료 봉 목표를 다음 봉 시가에 모의 적용 |
| v2 | cci_20_momentum | 10010.15 | 10.15 | sell / filled / CCI20 > 100 (전형가격·평균절대편차); 조건 미충족; CCI20=86.441; 직전 완료 봉 목표를 다음 봉 시가에 모의 적용 |
| v2 | williams_14_recovery | 9816.68 | -183.32 | sell / filled / 직전 Williams %R14 < -80, 현재 >= -80 (한 봉 목표); 조건 미충족; Williams_R14=-78.4506, previous_R14=-77.7733; 직전 완료 봉 목표를 다음 봉 시가에 모의 적용 |
| v2 | cmf_20_accumulation | 9745.54 | -254.46 | buy / partial / Chaikin Money Flow20 > 0.1; 조건 충족; CMF20=0.184396, volume20=3.37825e+07; 직전 완료 봉 목표를 다음 봉 시가에 모의 적용 |
| v2 | chaikin_3_10 | 9831.04 | -168.96 | sell / filled / ADL의 EMA3 - EMA10 > 0 그리고 종가 > EMA26; 조건 미충족; Chaikin3_10=-39308.5, ADL=1.1146e+08, close=533.345, EMA26=532.447; 직전 완료 봉 목표를 다음 봉 시가에 모의 적용 |
| v2 | roc_10_momentum | 9957.44 | -42.56 | sell / filled / 10봉 ROC > 1% 그리고 종가 > EMA26; 조건 미충족; ROC10_percent=0.454191, close=534.125, EMA26=532.186; 직전 완료 봉 목표를 다음 봉 시가에 모의 적용 |
| v2 | trix_15_trend | 9855.13 | -144.87 | buy / partial / 15봉 삼중 EMA의 1봉 변화율 TRIX > 0 그리고 종가 > EMA26; 조건 충족; TRIX15_percent=0.00435677, close=534.125, EMA26=532.186; 직전 완료 봉 목표를 다음 봉 시가에 모의 적용 |
| v2 | keltner_20_breakout | 9956.78 | -43.22 | sell / filled / 종가 > EMA20 + 2 x Wilder ATR14; 조건 미충족; close=533.975, upper_Keltner=534.357, EMA20=530.111, ATR14=2.12332; 직전 완료 봉 목표를 다음 봉 시가에 모의 적용 |
| v2 | opening_range_30m | 9854.49 | -145.51 | buy / partial / 뉴욕 09:30·09:45 두 완료 봉 최고가를 10:00 이후 종가가 돌파; 조건 충족; close=534.145, opening_high=532.63; 직전 완료 봉 목표를 다음 봉 시가에 모의 적용 |

### 같은 기간의 비용·노출 비교 (사후 연구)

| 전략 | 비용 전 | 비용 후 | 100% 보유 | 같은 평균 노출 보유 | 평균 노출 |
|---|---:|---:|---:|---:|---:|
| cash | 0.00% | 0.00% | 4.03% | 0.00% | 0.00% |
| buy_hold | 4.46% | 4.03% | 4.03% | 4.03% | 100.00% |
| trend_8_26 | 0.94% | -2.80% | 4.03% | 2.28% | 57.48% |
| momentum_26 | 1.57% | -4.23% | 4.03% | 2.35% | 59.06% |
| breakout_8 | 5.93% | -8.55% | 4.03% | 0.79% | 20.21% |
| reversion_12 | -4.00% | -12.84% | 4.03% | 0.99% | 25.20% |
| volume_26 | 1.69% | -7.29% | 4.03% | 0.35% | 8.92% |
| trend_8_26 AND momentum_26 | 0.30% | -5.42% | 4.03% | 2.08% | 52.49% |
| trend_8_26 + momentum_26 | 1.26% | -3.51% | 4.03% | 2.32% | 58.27% |
| trend_8_26 AND breakout_8 | 0.52% | -9.88% | 4.03% | 0.51% | 13.12% |
| trend_8_26 + breakout_8 | 3.42% | -5.12% | 4.03% | 1.53% | 38.85% |
| trend_8_26 AND reversion_12 | -1.58% | -7.20% | 4.03% | 0.27% | 6.82% |
| trend_8_26 + reversion_12 | -1.54% | -7.77% | 4.03% | 1.63% | 41.34% |
| trend_8_26 AND volume_26 | 3.42% | -0.42% | 4.03% | 0.12% | 3.15% |
| trend_8_26 + volume_26 | 1.33% | -4.47% | 4.03% | 1.31% | 33.21% |
| momentum_26 AND breakout_8 | 2.46% | -8.53% | 4.03% | 0.52% | 13.39% |
| momentum_26 + breakout_8 | 3.74% | -5.82% | 4.03% | 1.57% | 39.64% |
| momentum_26 AND reversion_12 | -1.15% | -7.57% | 4.03% | 0.35% | 8.92% |
| momentum_26 + reversion_12 | -1.23% | -8.45% | 4.03% | 1.67% | 42.13% |
| momentum_26 AND volume_26 | 1.77% | -3.23% | 4.03% | 0.15% | 3.94% |
| momentum_26 + volume_26 | 1.64% | -4.78% | 4.03% | 1.34% | 33.99% |
| breakout_8 AND reversion_12 | 0.00% | 0.00% | 4.03% | 0.00% | 0.00% |
| breakout_8 + reversion_12 | 0.86% | -9.97% | 4.03% | 0.89% | 22.71% |
| breakout_8 AND volume_26 | 2.00% | -0.96% | 4.03% | 0.08% | 2.10% |
| breakout_8 + volume_26 | 3.80% | -6.75% | 4.03% | 0.57% | 14.57% |
| reversion_12 AND volume_26 | -2.90% | -6.11% | 4.03% | 0.13% | 3.41% |
| reversion_12 + volume_26 | -1.19% | -9.92% | 4.03% | 0.67% | 17.07% |
| ema_12_26 | 1.53% | -1.82% | 4.03% | 2.34% | 58.79% |
| macd_12_26_9 | 1.06% | -3.90% | 4.03% | 1.30% | 33.07% |
| rsi_14_recovery | -0.06% | -2.13% | 4.03% | 0.05% | 1.31% |
| bollinger_20_reentry | -0.29% | -3.18% | 4.03% | 0.07% | 1.84% |
| donchian_20 | 1.76% | -4.05% | 4.03% | 0.19% | 4.99% |
| atr_14_breakout | 1.45% | -4.74% | 4.03% | 0.16% | 4.20% |
| session_vwap | 5.11% | -2.95% | 4.03% | 1.66% | 41.99% |
| obv_20 | 4.53% | -3.89% | 4.03% | 1.95% | 49.34% |
| stochastic_14_3_recovery | -0.50% | -10.80% | 4.03% | 0.27% | 6.82% |
| mfi_14_recovery | 1.54% | -1.81% | 4.03% | 0.08% | 2.10% |
| adx_14_trend | 3.83% | 1.25% | 4.03% | 1.84% | 46.46% |
| aroon_25_trend | -0.01% | -4.93% | 4.03% | 0.88% | 22.31% |
| cci_20_momentum | 3.27% | -3.44% | 4.03% | 0.90% | 22.83% |
| williams_14_recovery | -0.78% | -9.91% | 4.03% | 0.24% | 6.04% |
| cmf_20_accumulation | 0.53% | -5.21% | 4.03% | 1.21% | 30.71% |
| chaikin_3_10 | 3.68% | -3.87% | 4.03% | 1.79% | 45.14% |
| roc_10_momentum | -0.01% | -4.12% | 4.03% | 0.62% | 15.75% |
| trix_15_trend | 0.43% | -3.70% | 4.03% | 1.85% | 46.72% |
| keltner_20_breakout | 1.11% | -4.26% | 4.03% | 0.53% | 13.65% |
| opening_range_30m | -2.09% | -6.91% | 4.03% | 0.87% | 22.05% |

동일 구간·초기 자금, 종료 시 청산 비용 포함. 노출 맞춤은 사후 설명용이며 v2 실제 계좌 성과가 아닙니다.
[낙폭 분해·비용 영향·전체 구간](MSFT/comparison.json)

[v1 전체 기록](MSFT/accounts.json) · [v2 전체 기록](MSFT/accounts-v2.json)

## JPM 계좌

| 모델 | 전략 | 평가액 USD | 손익 USD | 최근 매매·이유 |
|---|---|---:|---:|---|
| v1 | cash | 10000.00 | 0.00 | 대기 /  / 새 신호 대기 |
| v1 | buy_hold | 9873.45 | -126.55 | buy /  / buy_hold: prior completed bar target 100%; next bar open simulation |
| v1 | trend_8_26 | 9924.04 | -75.96 | sell /  / trend_8_26: prior completed bar target 0%; next bar open simulation |
| v1 | momentum_26 | 9892.69 | -107.31 | sell /  / momentum_26: prior completed bar target 0%; next bar open simulation |
| v1 | breakout_8 | 9829.39 | -170.61 | sell /  / breakout_8: prior completed bar target 0%; next bar open simulation |
| v1 | reversion_12 | 9803.96 | -196.04 | sell /  / reversion_12: prior completed bar target 0%; next bar open simulation |
| v1 | volume_26 | 10020.63 | 20.63 | sell /  / volume_26: prior completed bar target 0%; next bar open simulation |
| v1 | trend_8_26 AND momentum_26 | 9924.04 | -75.96 | sell /  / trend_8_26 AND momentum_26: prior completed bar target 0%; next bar open simulation |
| v1 | trend_8_26 + momentum_26 | 9908.39 | -91.61 | sell /  / trend_8_26 + momentum_26: prior completed bar target 0%; next bar open simulation |
| v1 | trend_8_26 AND breakout_8 | 9915.55 | -84.45 | sell /  / trend_8_26 AND breakout_8: prior completed bar target 0%; next bar open simulation |
| v1 | trend_8_26 + breakout_8 | 9876.66 | -123.34 | sell /  / trend_8_26 + breakout_8: prior completed bar target 0%; next bar open simulation |
| v1 | trend_8_26 AND reversion_12 | 9899.24 | -100.76 | sell /  / trend_8_26 AND reversion_12: prior completed bar target 0%; next bar open simulation |
| v1 | trend_8_26 + reversion_12 | 9863.74 | -136.26 | sell /  / trend_8_26 + reversion_12: prior completed bar target 0%; next bar open simulation |
| v1 | trend_8_26 AND volume_26 | 10035.68 | 35.68 | sell /  / trend_8_26 AND volume_26: prior completed bar target 0%; next bar open simulation |
| v1 | trend_8_26 + volume_26 | 9972.14 | -27.86 | sell /  / trend_8_26 + volume_26: prior completed bar target 0%; next bar open simulation |
| v1 | momentum_26 AND breakout_8 | 9829.39 | -170.61 | sell /  / momentum_26 AND breakout_8: prior completed bar target 0%; next bar open simulation |
| v1 | momentum_26 + breakout_8 | 9861.04 | -138.96 | sell /  / momentum_26 + breakout_8: prior completed bar target 0%; next bar open simulation |
| v1 | momentum_26 AND reversion_12 | 9881.87 | -118.13 | sell /  / momentum_26 AND reversion_12: prior completed bar target 0%; next bar open simulation |
| v1 | momentum_26 + reversion_12 | 9867.90 | -132.10 | sell /  / momentum_26 + reversion_12: prior completed bar target 0%; next bar open simulation |
| v1 | momentum_26 AND volume_26 | 10035.68 | 35.68 | sell /  / momentum_26 AND volume_26: prior completed bar target 0%; next bar open simulation |
| v1 | momentum_26 + volume_26 | 9956.40 | -43.60 | sell /  / momentum_26 + volume_26: prior completed bar target 0%; next bar open simulation |
| v1 | breakout_8 AND reversion_12 | 10000.00 | 0.00 | 대기 /  / 새 신호 대기 |
| v1 | breakout_8 + reversion_12 | 9836.25 | -163.75 | sell /  / breakout_8 + reversion_12: prior completed bar target 0%; next bar open simulation |
| v1 | breakout_8 AND volume_26 | 10035.68 | 35.68 | sell /  / breakout_8 AND volume_26: prior completed bar target 0%; next bar open simulation |
| v1 | breakout_8 + volume_26 | 9924.55 | -75.45 | sell /  / breakout_8 + volume_26: prior completed bar target 0%; next bar open simulation |
| v1 | reversion_12 AND volume_26 | 9985.00 | -15.00 | sell /  / reversion_12 AND volume_26: prior completed bar target 0%; next bar open simulation |
| v1 | reversion_12 + volume_26 | 9911.63 | -88.37 | sell /  / reversion_12 + volume_26: prior completed bar target 0%; next bar open simulation |
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
| v1 | williams_14_recovery | 9852.65 | -147.35 | buy /  / 직전 Williams %R14 < -80, 현재 >= -80 (한 봉 목표); 조건 충족; Williams_R14=-77.2645, previous_R14=-81.1593 |
| v1 | cmf_20_accumulation | 9932.16 | -67.84 | sell /  / Chaikin Money Flow20 > 0.1; 조건 미충족; CMF20=-0.14511, volume20=9.3038e+06 |
| v1 | chaikin_3_10 | 9920.58 | -79.42 | sell /  / ADL의 EMA3 - EMA10 > 0 그리고 종가 > EMA26; 조건 미충족; Chaikin3_10=55836.7, ADL=-1.05866e+07, close=337.6, EMA26=338.759 |
| v1 | roc_10_momentum | 9913.84 | -86.16 | sell /  / 10봉 ROC > 1% 그리고 종가 > EMA26; 조건 미충족; ROC10_percent=-0.490038, close=340.901, EMA26=338.962 |
| v1 | trix_15_trend | 9723.73 | -276.27 | sell /  / 15봉 삼중 EMA의 1봉 변화율 TRIX > 0 그리고 종가 > EMA26; 조건 미충족; TRIX15_percent=0.0135144, close=337.6, EMA26=338.759 |
| v1 | keltner_20_breakout | 9946.99 | -53.01 | sell /  / 종가 > EMA20 + 2 x Wilder ATR14; 조건 미충족; close=342, upper_Keltner=342.276, EMA20=339.397, ATR14=1.43933 |
| v1 | opening_range_30m | 9927.81 | -72.19 | sell /  / 뉴욕 09:30·09:45 두 완료 봉 최고가를 10:00 이후 종가가 돌파; 조건 미충족; close=343.037, opening_high=343.75 |
| v2 | cash | 10000.00 | 0.00 | 대기 /  / 새 신호 대기 |
| v2 | buy_hold | 10038.44 | 38.44 | buy / partial / 직전 완료 봉 목표 비중 100%; 다음 봉 시가 가정 |
| v2 | trend_8_26 | 9931.17 | -68.83 | sell / filled / 직전 완료 봉 목표 비중 0%; 다음 봉 시가 가정 |
| v2 | momentum_26 | 9401.71 | -598.29 | sell / filled / 직전 완료 봉 목표 비중 0%; 다음 봉 시가 가정 |
| v2 | breakout_8 | 9168.97 | -831.03 | sell / filled / 직전 완료 봉 목표 비중 0%; 다음 봉 시가 가정 |
| v2 | reversion_12 | 9784.34 | -215.66 | sell / filled / 직전 완료 봉 목표 비중 0%; 다음 봉 시가 가정 |
| v2 | volume_26 | 9843.04 | -156.96 | sell / filled / 직전 완료 봉 목표 비중 0%; 다음 봉 시가 가정 |
| v2 | trend_8_26 AND momentum_26 | 9890.41 | -109.59 | sell / filled / 직전 완료 봉 목표 비중 0%; 다음 봉 시가 가정 |
| v2 | trend_8_26 + momentum_26 | 9683.69 | -316.31 | sell / filled / 직전 완료 봉 목표 비중 0%; 다음 봉 시가 가정 |
| v2 | trend_8_26 AND breakout_8 | 9287.76 | -712.24 | sell / filled / 직전 완료 봉 목표 비중 0%; 다음 봉 시가 가정 |
| v2 | trend_8_26 + breakout_8 | 9543.58 | -456.42 | sell / filled / 직전 완료 봉 목표 비중 0%; 다음 봉 시가 가정 |
| v2 | trend_8_26 AND reversion_12 | 9877.09 | -122.91 | sell / filled / 직전 완료 봉 목표 비중 0%; 다음 봉 시가 가정 |
| v2 | trend_8_26 + reversion_12 | 9899.11 | -100.89 | sell / filled / 직전 완료 봉 목표 비중 0%; 다음 봉 시가 가정 |
| v2 | trend_8_26 AND volume_26 | 9833.30 | -166.70 | sell / filled / 직전 완료 봉 목표 비중 0%; 다음 봉 시가 가정 |
| v2 | trend_8_26 + volume_26 | 9887.76 | -112.24 | sell / filled / 직전 완료 봉 목표 비중 0%; 다음 봉 시가 가정 |
| v2 | momentum_26 AND breakout_8 | 9150.64 | -849.36 | sell / filled / 직전 완료 봉 목표 비중 0%; 다음 봉 시가 가정 |
| v2 | momentum_26 + breakout_8 | 9305.78 | -694.22 | sell / filled / 직전 완료 봉 목표 비중 0%; 다음 봉 시가 가정 |
| v2 | momentum_26 AND reversion_12 | 9827.31 | -172.69 | sell / filled / 직전 완료 봉 목표 비중 0%; 다음 봉 시가 가정 |
| v2 | momentum_26 + reversion_12 | 9733.66 | -266.34 | sell / filled / 직전 완료 봉 목표 비중 0%; 다음 봉 시가 가정 |
| v2 | momentum_26 AND volume_26 | 9833.30 | -166.70 | sell / filled / 직전 완료 봉 목표 비중 0%; 다음 봉 시가 가정 |
| v2 | momentum_26 + volume_26 | 9681.83 | -318.17 | sell / filled / 직전 완료 봉 목표 비중 0%; 다음 봉 시가 가정 |
| v2 | breakout_8 AND reversion_12 | 10000.00 | 0.00 | 대기 /  / 새 신호 대기 |
| v2 | breakout_8 + reversion_12 | 9531.67 | -468.33 | sell / filled / 직전 완료 봉 목표 비중 0%; 다음 봉 시가 가정 |
| v2 | breakout_8 AND volume_26 | 9926.66 | -73.34 | sell / filled / 직전 완료 봉 목표 비중 0%; 다음 봉 시가 가정 |
| v2 | breakout_8 + volume_26 | 9520.14 | -479.86 | sell / filled / 직전 완료 봉 목표 비중 0%; 다음 봉 시가 가정 |
| v2 | reversion_12 AND volume_26 | 10034.30 | 34.30 | sell / filled / 직전 완료 봉 목표 비중 0%; 다음 봉 시가 가정 |
| v2 | reversion_12 + volume_26 | 9834.48 | -165.52 | sell / filled / 직전 완료 봉 목표 비중 0%; 다음 봉 시가 가정 |
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
| v2 | williams_14_recovery | 9845.76 | -154.24 | buy / partial / 직전 Williams %R14 < -80, 현재 >= -80 (한 봉 목표); 조건 충족; Williams_R14=-77.2645, previous_R14=-81.1593; 직전 완료 봉 목표를 다음 봉 시가에 모의 적용 |
| v2 | cmf_20_accumulation | 9930.17 | -69.83 | sell / filled / Chaikin Money Flow20 > 0.1; 조건 미충족; CMF20=-0.14511, volume20=9.3038e+06; 직전 완료 봉 목표를 다음 봉 시가에 모의 적용 |
| v2 | chaikin_3_10 | 9916.62 | -83.38 | sell / filled / ADL의 EMA3 - EMA10 > 0 그리고 종가 > EMA26; 조건 미충족; Chaikin3_10=55836.7, ADL=-1.05866e+07, close=337.6, EMA26=338.759; 직전 완료 봉 목표를 다음 봉 시가에 모의 적용 |
| v2 | roc_10_momentum | 9911.86 | -88.14 | sell / filled / 10봉 ROC > 1% 그리고 종가 > EMA26; 조건 미충족; ROC10_percent=-0.490038, close=340.901, EMA26=338.962; 직전 완료 봉 목표를 다음 봉 시가에 모의 적용 |
| v2 | trix_15_trend | 9715.96 | -284.04 | sell / filled / 15봉 삼중 EMA의 1봉 변화율 TRIX > 0 그리고 종가 > EMA26; 조건 미충족; TRIX15_percent=0.0135144, close=337.6, EMA26=338.759; 직전 완료 봉 목표를 다음 봉 시가에 모의 적용 |
| v2 | keltner_20_breakout | 9945.00 | -55.00 | sell / filled / 종가 > EMA20 + 2 x Wilder ATR14; 조건 미충족; close=342, upper_Keltner=342.276, EMA20=339.397, ATR14=1.43933; 직전 완료 봉 목표를 다음 봉 시가에 모의 적용 |
| v2 | opening_range_30m | 9925.82 | -74.18 | sell / filled / 뉴욕 09:30·09:45 두 완료 봉 최고가를 10:00 이후 종가가 돌파; 조건 미충족; close=343.037, opening_high=343.75; 직전 완료 봉 목표를 다음 봉 시가에 모의 적용 |

### 같은 기간의 비용·노출 비교 (사후 연구)

| 전략 | 비용 전 | 비용 후 | 100% 보유 | 같은 평균 노출 보유 | 평균 노출 |
|---|---:|---:|---:|---:|---:|
| cash | 0.00% | 0.00% | -0.47% | -0.00% | 0.00% |
| buy_hold | -0.05% | -0.47% | -0.47% | -0.47% | 100.00% |
| trend_8_26 | 1.16% | -2.59% | -0.47% | -0.24% | 51.71% |
| momentum_26 | -2.37% | -8.33% | -0.47% | -0.23% | 48.56% |
| breakout_8 | -3.63% | -18.53% | -0.47% | -0.09% | 19.69% |
| reversion_12 | 5.56% | -9.64% | -0.47% | -0.12% | 25.98% |
| volume_26 | 0.31% | -5.82% | -0.47% | -0.03% | 6.82% |
| trend_8_26 AND momentum_26 | 1.09% | -3.07% | -0.47% | -0.19% | 40.68% |
| trend_8_26 + momentum_26 | -0.61% | -5.30% | -0.47% | -0.24% | 50.13% |
| trend_8_26 AND breakout_8 | -3.21% | -13.22% | -0.47% | -0.06% | 12.07% |
| trend_8_26 + breakout_8 | -1.24% | -10.72% | -0.47% | -0.17% | 35.70% |
| trend_8_26 AND reversion_12 | 2.66% | -3.61% | -0.47% | -0.03% | 7.35% |
| trend_8_26 + reversion_12 | 3.36% | -5.59% | -0.47% | -0.18% | 38.85% |
| trend_8_26 AND volume_26 | -0.42% | -4.11% | -0.47% | -0.02% | 3.94% |
| trend_8_26 + volume_26 | 0.75% | -4.21% | -0.47% | -0.14% | 29.27% |
| momentum_26 AND breakout_8 | -2.51% | -12.96% | -0.47% | -0.06% | 12.07% |
| momentum_26 + breakout_8 | -2.98% | -13.38% | -0.47% | -0.16% | 34.13% |
| momentum_26 AND reversion_12 | 2.79% | -4.29% | -0.47% | -0.03% | 6.82% |
| momentum_26 + reversion_12 | 1.54% | -7.44% | -0.47% | -0.18% | 37.28% |
| momentum_26 AND volume_26 | 0.21% | -2.70% | -0.47% | -0.01% | 2.89% |
| momentum_26 + volume_26 | -1.02% | -6.88% | -0.47% | -0.13% | 27.69% |
| breakout_8 AND reversion_12 | 0.00% | 0.00% | -0.47% | -0.00% | 0.00% |
| breakout_8 + reversion_12 | 0.88% | -12.74% | -0.47% | -0.11% | 22.84% |
| breakout_8 AND volume_26 | -0.51% | -2.17% | -0.47% | -0.00% | 1.05% |
| breakout_8 + volume_26 | -1.67% | -11.48% | -0.47% | -0.06% | 13.26% |
| reversion_12 AND volume_26 | 1.66% | -1.70% | -0.47% | -0.02% | 3.41% |
| reversion_12 + volume_26 | 2.91% | -6.97% | -0.47% | -0.08% | 16.41% |
| ema_12_26 | 0.72% | -2.20% | -0.47% | -0.24% | 50.13% |
| macd_12_26_9 | 0.83% | -3.32% | -0.47% | -0.15% | 30.97% |
| rsi_14_recovery | 0.14% | -2.35% | -0.47% | -0.01% | 1.57% |
| bollinger_20_reentry | 0.66% | -4.69% | -0.47% | -0.02% | 3.41% |
| donchian_20 | -1.79% | -4.63% | -0.47% | -0.01% | 2.89% |
| atr_14_breakout | -1.59% | -8.37% | -0.47% | -0.02% | 4.72% |
| session_vwap | 1.19% | -8.52% | -0.47% | -0.22% | 47.24% |
| obv_20 | -3.51% | -14.21% | -0.47% | -0.14% | 30.18% |
| stochastic_14_3_recovery | -1.63% | -12.54% | -0.47% | -0.03% | 7.35% |
| mfi_14_recovery | 0.06% | -2.02% | -0.47% | -0.01% | 1.31% |
| adx_14_trend | -2.86% | -5.68% | -0.47% | -0.13% | 27.30% |
| aroon_25_trend | -1.12% | -5.19% | -0.47% | -0.11% | 22.57% |
| cci_20_momentum | -2.26% | -9.76% | -0.47% | -0.07% | 14.96% |
| williams_14_recovery | -2.41% | -13.24% | -0.47% | -0.03% | 7.35% |
| cmf_20_accumulation | -1.74% | -9.66% | -0.47% | -0.14% | 28.61% |
| chaikin_3_10 | 1.37% | -7.19% | -0.47% | -0.16% | 33.07% |
| roc_10_momentum | -0.98% | -3.45% | -0.47% | -0.04% | 7.87% |
| trix_15_trend | -1.25% | -8.83% | -0.47% | -0.17% | 35.17% |
| keltner_20_breakout | -1.19% | -3.65% | -0.47% | -0.02% | 3.94% |
| opening_range_30m | 0.15% | -3.16% | -0.47% | -0.08% | 16.80% |

동일 구간·초기 자금, 종료 시 청산 비용 포함. 노출 맞춤은 사후 설명용이며 v2 실제 계좌 성과가 아닙니다.
[낙폭 분해·비용 영향·전체 구간](JPM/comparison.json)

[v1 전체 기록](JPM/accounts.json) · [v2 전체 기록](JPM/accounts-v2.json)

## XOM 계좌

| 모델 | 전략 | 평가액 USD | 손익 USD | 최근 매매·이유 |
|---|---|---:|---:|---|
| v1 | cash | 10000.00 | 0.00 | 대기 /  / 새 신호 대기 |
| v1 | buy_hold | 10086.91 | 86.91 | buy /  / buy_hold: prior completed bar target 100%; next bar open simulation |
| v1 | trend_8_26 | 10074.20 | 74.20 | sell /  / trend_8_26: prior completed bar target 0%; next bar open simulation |
| v1 | momentum_26 | 10114.70 | 114.70 | buy /  / momentum_26: prior completed bar target 100%; next bar open simulation |
| v1 | breakout_8 | 9759.89 | -240.11 | buy /  / breakout_8: prior completed bar target 100%; next bar open simulation |
| v1 | reversion_12 | 9934.36 | -65.64 | sell /  / reversion_12: prior completed bar target 0%; next bar open simulation |
| v1 | volume_26 | 9889.56 | -110.44 | sell /  / volume_26: prior completed bar target 0%; next bar open simulation |
| v1 | trend_8_26 AND momentum_26 | 10074.20 | 74.20 | sell /  / trend_8_26 AND momentum_26: prior completed bar target 0%; next bar open simulation |
| v1 | trend_8_26 + momentum_26 | 10094.40 | 94.40 | sell /  / trend_8_26 + momentum_26: prior completed bar target 50%; next bar open simulation |
| v1 | trend_8_26 AND breakout_8 | 9878.22 | -121.78 | sell /  / trend_8_26 AND breakout_8: prior completed bar target 0%; next bar open simulation |
| v1 | trend_8_26 + breakout_8 | 9935.71 | -64.29 | sell /  / trend_8_26 + breakout_8: prior completed bar target 50%; next bar open simulation |
| v1 | trend_8_26 AND reversion_12 | 9921.77 | -78.23 | sell /  / trend_8_26 AND reversion_12: prior completed bar target 0%; next bar open simulation |
| v1 | trend_8_26 + reversion_12 | 10003.95 | 3.95 | sell /  / trend_8_26 + reversion_12: prior completed bar target 0%; next bar open simulation |
| v1 | trend_8_26 AND volume_26 | 9985.49 | -14.51 | sell /  / trend_8_26 AND volume_26: prior completed bar target 0%; next bar open simulation |
| v1 | trend_8_26 + volume_26 | 9981.34 | -18.66 | sell /  / trend_8_26 + volume_26: prior completed bar target 0%; next bar open simulation |
| v1 | momentum_26 AND breakout_8 | 9808.50 | -191.50 | buy /  / momentum_26 AND breakout_8: prior completed bar target 100%; next bar open simulation |
| v1 | momentum_26 + breakout_8 | 9935.80 | -64.20 | buy /  / momentum_26 + breakout_8: prior completed bar target 100%; next bar open simulation |
| v1 | momentum_26 AND reversion_12 | 9934.36 | -65.64 | sell /  / momentum_26 AND reversion_12: prior completed bar target 0%; next bar open simulation |
| v1 | momentum_26 + reversion_12 | 10024.04 | 24.04 | sell /  / momentum_26 + reversion_12: prior completed bar target 50%; next bar open simulation |
| v1 | momentum_26 AND volume_26 | 9985.49 | -14.51 | sell /  / momentum_26 AND volume_26: prior completed bar target 0%; next bar open simulation |
| v1 | momentum_26 + volume_26 | 10001.37 | 1.37 | sell /  / momentum_26 + volume_26: prior completed bar target 50%; next bar open simulation |
| v1 | breakout_8 AND reversion_12 | 10000.00 | 0.00 | 대기 /  / 새 신호 대기 |
| v1 | breakout_8 + reversion_12 | 9846.57 | -153.43 | sell /  / breakout_8 + reversion_12: prior completed bar target 50%; next bar open simulation |
| v1 | breakout_8 AND volume_26 | 9950.44 | -49.56 | sell /  / breakout_8 AND volume_26: prior completed bar target 0%; next bar open simulation |
| v1 | breakout_8 + volume_26 | 9824.37 | -175.63 | sell /  / breakout_8 + volume_26: prior completed bar target 50%; next bar open simulation |
| v1 | reversion_12 AND volume_26 | 10000.00 | 0.00 | 대기 /  / 새 신호 대기 |
| v1 | reversion_12 + volume_26 | 9911.86 | -88.14 | sell /  / reversion_12 + volume_26: prior completed bar target 0%; next bar open simulation |
| v1 | ema_12_26 | 10145.25 | 145.25 | buy /  / EMA12 > EMA26; 조건 충족; EMA12=175.145, EMA26=175.141 |
| v1 | macd_12_26_9 | 10115.61 | 115.61 | sell /  / MACD > 신호선 그리고 MACD > 0; 조건 미충족; MACD=0.723601, signal9=0.751787 |
| v1 | rsi_14_recovery | 10000.00 | 0.00 | 대기 /  / 새 신호 대기 |
| v1 | bollinger_20_reentry | 9913.52 | -86.48 | sell /  / 직전 종가 < 직전 하단밴드, 현재 하단밴드 <= 종가 <= SMA20 (한 봉 목표); 조건 미충족; close=175.71, lower20=173.907, SMA20=174.743, previous_lower20=173.977 |
| v1 | donchian_20 | 9832.30 | -167.70 | sell /  / 종가 > 현재 봉을 제외한 직전 20봉 최고가; 조건 미충족; close=179.01, prior_high20=179.16 |
| v1 | atr_14_breakout | 9864.96 | -135.04 | sell /  / 종가 > 직전 종가 + 직전 ATR14 그리고 종가 > EMA26; 조건 미충족; close=177.19, threshold=177.748, prior_ATR14=0.663113, EMA26=175.734 |
| v1 | session_vwap | 10009.60 | 9.60 | buy /  / 종가 > 뉴욕 거래일별 누적 전형가격 VWAP; 조건 충족; close=178.12, session_VWAP=178.027, session_volume=4.4806e+06 |
| v1 | obv_20 | 9837.06 | -162.94 | buy /  / OBV > OBV의 SMA20 그리고 종가 > EMA26; 조건 충족; OBV=2.18423e+07, OBV_SMA20=2.18347e+07, close=177.655, EMA26=177.636 |
| v1 | stochastic_14_3_recovery | 9923.93 | -76.07 | sell /  / 직전 %K14 < 20에서 %K14가 %D3 상향 돌파 (한 봉 목표); 조건 미충족; K14=33.4559, D3=21.1148, previous_K14=20.3889, previous_D3=14.0974 |
| v1 | mfi_14_recovery | 10000.00 | 0.00 | 대기 /  / 새 신호 대기 |
| v1 | adx_14_trend | 9999.47 | -0.53 | sell /  / Wilder ADX14 >= 25 그리고 +DI14 > -DI14; 조건 미충족; ADX14=23.8302, plus_DI14=25.6436, minus_DI14=22.6035 |
| v1 | aroon_25_trend | 9929.86 | -70.14 | sell /  / Aroon25 Up > 70 그리고 Down < 30 (동률이면 최신 극값); 조건 미충족; Aroon_up=68, Aroon_down=0 |
| v1 | cci_20_momentum | 9842.10 | -157.90 | sell /  / CCI20 > 100 (전형가격·평균절대편차); 조건 미충족; CCI20=67.3071 |
| v1 | williams_14_recovery | 9838.11 | -161.89 | sell /  / 직전 Williams %R14 < -80, 현재 >= -80 (한 봉 목표); 조건 미충족; Williams_R14=-66.5441, previous_R14=-79.6111 |
| v1 | cmf_20_accumulation | 9947.41 | -52.59 | buy /  / Chaikin Money Flow20 > 0.1; 조건 충족; CMF20=0.158173, volume20=1.12043e+07 |
| v1 | chaikin_3_10 | 9890.13 | -109.87 | buy /  / ADL의 EMA3 - EMA10 > 0 그리고 종가 > EMA26; 조건 충족; Chaikin3_10=45202.2, ADL=2.7734e+07, close=177.655, EMA26=177.636 |
| v1 | roc_10_momentum | 9940.60 | -59.40 | sell /  / 10봉 ROC > 1% 그리고 종가 > EMA26; 조건 미충족; ROC10_percent=0.782107, close=178.47, EMA26=176.891 |
| v1 | trix_15_trend | 9988.31 | -11.69 | buy /  / 15봉 삼중 EMA의 1봉 변화율 TRIX > 0 그리고 종가 > EMA26; 조건 충족; TRIX15_percent=0.0352454, close=177.655, EMA26=177.636 |
| v1 | keltner_20_breakout | 9937.30 | -62.70 | sell /  / 종가 > EMA20 + 2 x Wilder ATR14; 조건 미충족; close=178.845, upper_Keltner=179.079, EMA20=177.884, ATR14=0.597175 |
| v1 | opening_range_30m | 10049.37 | 49.37 | sell /  / 뉴욕 09:30·09:45 두 완료 봉 최고가를 10:00 이후 종가가 돌파; 자료 부족·변동폭 또는 거래량 없음: 대기; close=179.01 |
| v2 | cash | 10000.00 | 0.00 | 대기 /  / 새 신호 대기 |
| v2 | buy_hold | 10408.81 | 408.81 | buy / partial / 직전 완료 봉 목표 비중 100%; 다음 봉 시가 가정 |
| v2 | trend_8_26 | 10169.14 | 169.14 | sell / filled / 직전 완료 봉 목표 비중 0%; 다음 봉 시가 가정 |
| v2 | momentum_26 | 10288.30 | 288.30 | buy / partial / 직전 완료 봉 목표 비중 100%; 다음 봉 시가 가정 |
| v2 | breakout_8 | 9229.76 | -770.24 | buy / partial / 직전 완료 봉 목표 비중 100%; 다음 봉 시가 가정 |
| v2 | reversion_12 | 9748.68 | -251.32 | sell / filled / 직전 완료 봉 목표 비중 0%; 다음 봉 시가 가정 |
| v2 | volume_26 | 9794.70 | -205.30 | sell / filled / 직전 완료 봉 목표 비중 0%; 다음 봉 시가 가정 |
| v2 | trend_8_26 AND momentum_26 | 10176.68 | 176.68 | sell / filled / 직전 완료 봉 목표 비중 0%; 다음 봉 시가 가정 |
| v2 | trend_8_26 + momentum_26 | 10228.54 | 228.54 | sell / filled / 직전 완료 봉 목표 비중 50%; 다음 봉 시가 가정 |
| v2 | trend_8_26 AND breakout_8 | 9329.27 | -670.73 | sell / filled / 직전 완료 봉 목표 비중 0%; 다음 봉 시가 가정 |
| v2 | trend_8_26 + breakout_8 | 9729.27 | -270.73 | sell / filled / 직전 완료 봉 목표 비중 50%; 다음 봉 시가 가정 |
| v2 | trend_8_26 AND reversion_12 | 9760.78 | -239.22 | sell / filled / 직전 완료 봉 목표 비중 0%; 다음 봉 시가 가정 |
| v2 | trend_8_26 + reversion_12 | 9956.69 | -43.31 | sell / filled / 직전 완료 봉 목표 비중 0%; 다음 봉 시가 가정 |
| v2 | trend_8_26 AND volume_26 | 9879.28 | -120.72 | sell / filled / 직전 완료 봉 목표 비중 0%; 다음 봉 시가 가정 |
| v2 | trend_8_26 + volume_26 | 9980.00 | -20.00 | sell / filled / 직전 완료 봉 목표 비중 0%; 다음 봉 시가 가정 |
| v2 | momentum_26 AND breakout_8 | 9277.59 | -722.41 | buy / partial / 직전 완료 봉 목표 비중 100%; 다음 봉 시가 가정 |
| v2 | momentum_26 + breakout_8 | 9745.29 | -254.71 | buy / partial / 직전 완료 봉 목표 비중 100%; 다음 봉 시가 가정 |
| v2 | momentum_26 AND reversion_12 | 9733.85 | -266.15 | sell / filled / 직전 완료 봉 목표 비중 0%; 다음 봉 시가 가정 |
| v2 | momentum_26 + reversion_12 | 10014.88 | 14.88 | sell / filled / 직전 완료 봉 목표 비중 50%; 다음 봉 시가 가정 |
| v2 | momentum_26 AND volume_26 | 9941.52 | -58.48 | sell / filled / 직전 완료 봉 목표 비중 0%; 다음 봉 시가 가정 |
| v2 | momentum_26 + volume_26 | 10059.36 | 59.36 | sell / filled / 직전 완료 봉 목표 비중 50%; 다음 봉 시가 가정 |
| v2 | breakout_8 AND reversion_12 | 10000.00 | 0.00 | 대기 /  / 새 신호 대기 |
| v2 | breakout_8 + reversion_12 | 9485.41 | -514.59 | sell / filled / 직전 완료 봉 목표 비중 50%; 다음 봉 시가 가정 |
| v2 | breakout_8 AND volume_26 | 9918.86 | -81.14 | sell / filled / 직전 완료 봉 목표 비중 0%; 다음 봉 시가 가정 |
| v2 | breakout_8 + volume_26 | 9527.78 | -472.22 | sell / filled / 직전 완료 봉 목표 비중 50%; 다음 봉 시가 가정 |
| v2 | reversion_12 AND volume_26 | 9949.87 | -50.13 | sell / filled / 직전 완료 봉 목표 비중 0%; 다음 봉 시가 가정 |
| v2 | reversion_12 + volume_26 | 9792.16 | -207.84 | sell / filled / 직전 완료 봉 목표 비중 0%; 다음 봉 시가 가정 |
| v2 | ema_12_26 | 10144.24 | 144.24 | buy / partial / EMA12 > EMA26; 조건 충족; EMA12=175.145, EMA26=175.141; 직전 완료 봉 목표를 다음 봉 시가에 모의 적용 |
| v2 | macd_12_26_9 | 10113.59 | 113.59 | sell / filled / MACD > 신호선 그리고 MACD > 0; 조건 미충족; MACD=0.723601, signal9=0.751787; 직전 완료 봉 목표를 다음 봉 시가에 모의 적용 |
| v2 | rsi_14_recovery | 10000.00 | 0.00 | 대기 /  / 새 신호 대기 |
| v2 | bollinger_20_reentry | 9911.54 | -88.46 | sell / filled / 직전 종가 < 직전 하단밴드, 현재 하단밴드 <= 종가 <= SMA20 (한 봉 목표); 조건 미충족; close=175.71, lower20=173.907, SMA20=174.743, previous_lower20=173.977; 직전 완료 봉 목표를 다음 봉 시가에 모의 적용 |
| v2 | donchian_20 | 9824.43 | -175.57 | sell / filled / 종가 > 현재 봉을 제외한 직전 20봉 최고가; 조건 미충족; close=179.01, prior_high20=179.16; 직전 완료 봉 목표를 다음 봉 시가에 모의 적용 |
| v2 | atr_14_breakout | 9859.04 | -140.96 | sell / filled / 종가 > 직전 종가 + 직전 ATR14 그리고 종가 > EMA26; 조건 미충족; close=177.19, threshold=177.748, prior_ATR14=0.663113, EMA26=175.734; 직전 완료 봉 목표를 다음 봉 시가에 모의 적용 |
| v2 | session_vwap | 10004.60 | 4.60 | buy / partial / 종가 > 뉴욕 거래일별 누적 전형가격 VWAP; 조건 충족; close=178.12, session_VWAP=178.027, session_volume=4.4806e+06; 직전 완료 봉 목표를 다음 봉 시가에 모의 적용 |
| v2 | obv_20 | 9830.18 | -169.82 | buy / partial / OBV > OBV의 SMA20 그리고 종가 > EMA26; 조건 충족; OBV=2.18423e+07, OBV_SMA20=2.18347e+07, close=177.655, EMA26=177.636; 직전 완료 봉 목표를 다음 봉 시가에 모의 적용 |
| v2 | stochastic_14_3_recovery | 9919.96 | -80.04 | sell / filled / 직전 %K14 < 20에서 %K14가 %D3 상향 돌파 (한 봉 목표); 조건 미충족; K14=33.4559, D3=21.1148, previous_K14=20.3889, previous_D3=14.0974; 직전 완료 봉 목표를 다음 봉 시가에 모의 적용 |
| v2 | mfi_14_recovery | 10000.00 | 0.00 | 대기 /  / 새 신호 대기 |
| v2 | adx_14_trend | 9993.47 | -6.53 | sell / filled / Wilder ADX14 >= 25 그리고 +DI14 > -DI14; 조건 미충족; ADX14=23.8302, plus_DI14=25.6436, minus_DI14=22.6035; 직전 완료 봉 목표를 다음 봉 시가에 모의 적용 |
| v2 | aroon_25_trend | 9927.87 | -72.13 | sell / filled / Aroon25 Up > 70 그리고 Down < 30 (동률이면 최신 극값); 조건 미충족; Aroon_up=68, Aroon_down=0; 직전 완료 봉 목표를 다음 봉 시가에 모의 적용 |
| v2 | cci_20_momentum | 9832.27 | -167.73 | sell / filled / CCI20 > 100 (전형가격·평균절대편차); 조건 미충족; CCI20=67.3071; 직전 완료 봉 목표를 다음 봉 시가에 모의 적용 |
| v2 | williams_14_recovery | 9832.21 | -167.79 | sell / filled / 직전 Williams %R14 < -80, 현재 >= -80 (한 봉 목표); 조건 미충족; Williams_R14=-66.5441, previous_R14=-79.6111; 직전 완료 봉 목표를 다음 봉 시가에 모의 적용 |
| v2 | cmf_20_accumulation | 9946.41 | -53.59 | buy / partial / Chaikin Money Flow20 > 0.1; 조건 충족; CMF20=0.158173, volume20=1.12043e+07; 직전 완료 봉 목표를 다음 봉 시가에 모의 적용 |
| v2 | chaikin_3_10 | 9885.19 | -114.81 | buy / partial / ADL의 EMA3 - EMA10 > 0 그리고 종가 > EMA26; 조건 충족; Chaikin3_10=45202.2, ADL=2.7734e+07, close=177.655, EMA26=177.636; 직전 완료 봉 목표를 다음 봉 시가에 모의 적용 |
| v2 | roc_10_momentum | 9934.64 | -65.36 | sell / filled / 10봉 ROC > 1% 그리고 종가 > EMA26; 조건 미충족; ROC10_percent=0.782107, close=178.47, EMA26=176.891; 직전 완료 봉 목표를 다음 봉 시가에 모의 적용 |
| v2 | trix_15_trend | 9983.31 | -16.69 | buy / partial / 15봉 삼중 EMA의 1봉 변화율 TRIX > 0 그리고 종가 > EMA26; 조건 충족; TRIX15_percent=0.0352454, close=177.655, EMA26=177.636; 직전 완료 봉 목표를 다음 봉 시가에 모의 적용 |
| v2 | keltner_20_breakout | 9931.34 | -68.66 | sell / filled / 종가 > EMA20 + 2 x Wilder ATR14; 조건 미충족; close=178.845, upper_Keltner=179.079, EMA20=177.884, ATR14=0.597175; 직전 완료 봉 목표를 다음 봉 시가에 모의 적용 |
| v2 | opening_range_30m | 10047.36 | 47.36 | sell / filled / 뉴욕 09:30·09:45 두 완료 봉 최고가를 10:00 이후 종가가 돌파; 자료 부족·변동폭 또는 거래량 없음: 대기; close=179.01; 직전 완료 봉 목표를 다음 봉 시가에 모의 적용 |

### 같은 기간의 비용·노출 비교 (사후 연구)

| 전략 | 비용 전 | 비용 후 | 100% 보유 | 같은 평균 노출 보유 | 평균 노출 |
|---|---:|---:|---:|---:|---:|
| cash | 0.00% | 0.00% | 9.70% | 0.00% | 0.00% |
| buy_hold | 10.16% | 9.70% | 9.70% | 9.70% | 100.00% |
| trend_8_26 | 2.83% | -1.40% | 9.70% | 6.31% | 65.88% |
| momentum_26 | 2.42% | -5.04% | 9.70% | 6.93% | 72.18% |
| breakout_8 | -2.15% | -21.02% | 9.70% | 2.50% | 26.51% |
| reversion_12 | 5.55% | -4.57% | 9.70% | 2.05% | 21.78% |
| volume_26 | 3.26% | -3.86% | 9.70% | 0.44% | 4.72% |
| trend_8_26 AND momentum_26 | 1.35% | -3.22% | 9.70% | 5.79% | 60.63% |
| trend_8_26 + momentum_26 | 2.64% | -3.02% | 9.70% | 6.62% | 69.03% |
| trend_8_26 AND breakout_8 | -0.27% | -15.34% | 9.70% | 2.00% | 21.26% |
| trend_8_26 + breakout_8 | 0.33% | -11.36% | 9.70% | 4.39% | 46.20% |
| trend_8_26 AND reversion_12 | 0.37% | -4.96% | 9.70% | 0.84% | 8.92% |
| trend_8_26 + reversion_12 | 4.21% | -2.79% | 9.70% | 4.16% | 43.84% |
| trend_8_26 AND volume_26 | 2.37% | -1.84% | 9.70% | 0.25% | 2.62% |
| trend_8_26 + volume_26 | 3.06% | -2.43% | 9.70% | 3.34% | 35.30% |
| momentum_26 AND breakout_8 | -2.26% | -19.77% | 9.70% | 2.32% | 24.67% |
| momentum_26 + breakout_8 | 0.13% | -13.38% | 9.70% | 4.69% | 49.35% |
| momentum_26 AND reversion_12 | 0.87% | -5.29% | 9.70% | 0.93% | 9.97% |
| momentum_26 + reversion_12 | 4.00% | -3.39% | 9.70% | 4.47% | 46.99% |
| momentum_26 AND volume_26 | 2.15% | -1.64% | 9.70% | 0.22% | 2.36% |
| momentum_26 + volume_26 | 2.86% | -3.24% | 9.70% | 3.64% | 38.46% |
| breakout_8 AND reversion_12 | 0.00% | 0.00% | 9.70% | 0.00% | 0.00% |
| breakout_8 + reversion_12 | 1.65% | -13.00% | 9.70% | 2.28% | 24.16% |
| breakout_8 AND volume_26 | 0.51% | -1.17% | 9.70% | 0.10% | 1.05% |
| breakout_8 + volume_26 | 0.53% | -11.94% | 9.70% | 1.47% | 15.63% |
| reversion_12 AND volume_26 | 1.10% | -1.00% | 9.70% | 0.12% | 1.31% |
| reversion_12 + volume_26 | 4.41% | -3.41% | 9.70% | 1.24% | 13.26% |
| ema_12_26 | 1.87% | -1.50% | 9.70% | 7.32% | 76.12% |
| macd_12_26_9 | 0.40% | -4.93% | 9.70% | 3.96% | 41.73% |
| rsi_14_recovery | -0.15% | -0.57% | 9.70% | 0.02% | 0.26% |
| bollinger_20_reentry | -0.87% | -3.75% | 9.70% | 0.17% | 1.84% |
| donchian_20 | -0.93% | -10.43% | 9.70% | 0.91% | 9.71% |
| atr_14_breakout | -1.03% | -9.76% | 9.70% | 0.56% | 6.04% |
| session_vwap | 0.86% | -10.33% | 9.70% | 6.54% | 68.24% |
| obv_20 | 1.92% | -6.29% | 9.70% | 4.41% | 46.46% |
| stochastic_14_3_recovery | 1.68% | -6.90% | 9.70% | 0.52% | 5.51% |
| mfi_14_recovery | -0.31% | -1.97% | 9.70% | 0.10% | 1.05% |
| adx_14_trend | 3.88% | 0.87% | 9.70% | 4.21% | 44.36% |
| aroon_25_trend | -2.08% | -8.44% | 9.70% | 3.35% | 35.43% |
| cci_20_momentum | 3.75% | -4.61% | 9.70% | 2.70% | 28.61% |
| williams_14_recovery | 0.21% | -5.51% | 9.70% | 0.34% | 3.67% |
| cmf_20_accumulation | 0.91% | -5.65% | 9.70% | 5.00% | 52.49% |
| chaikin_3_10 | -0.87% | -10.00% | 9.70% | 5.59% | 58.53% |
| roc_10_momentum | 0.80% | -5.36% | 9.70% | 1.23% | 13.12% |
| trix_15_trend | -0.17% | -6.66% | 9.70% | 6.18% | 64.57% |
| keltner_20_breakout | 0.18% | -6.72% | 9.70% | 1.63% | 17.32% |
| opening_range_30m | 0.54% | -9.10% | 9.70% | 3.71% | 39.11% |

동일 구간·초기 자금, 종료 시 청산 비용 포함. 노출 맞춤은 사후 설명용이며 v2 실제 계좌 성과가 아닙니다.
[낙폭 분해·비용 영향·전체 구간](XOM/comparison.json)

[v1 전체 기록](XOM/accounts.json) · [v2 전체 기록](XOM/accounts-v2.json)

## JNJ 계좌

| 모델 | 전략 | 평가액 USD | 손익 USD | 최근 매매·이유 |
|---|---|---:|---:|---|
| v1 | cash | 10000.00 | 0.00 | 대기 /  / 새 신호 대기 |
| v1 | buy_hold | 9913.24 | -86.76 | buy /  / buy_hold: prior completed bar target 100%; next bar open simulation |
| v1 | trend_8_26 | 9903.43 | -96.57 | sell /  / trend_8_26: prior completed bar target 0%; next bar open simulation |
| v1 | momentum_26 | 9898.09 | -101.91 | sell /  / momentum_26: prior completed bar target 0%; next bar open simulation |
| v1 | breakout_8 | 9685.66 | -314.34 | buy /  / breakout_8: prior completed bar target 100%; next bar open simulation |
| v1 | reversion_12 | 9891.56 | -108.44 | sell /  / reversion_12: prior completed bar target 0%; next bar open simulation |
| v1 | volume_26 | 9884.71 | -115.29 | sell /  / volume_26: prior completed bar target 0%; next bar open simulation |
| v1 | trend_8_26 AND momentum_26 | 9950.33 | -49.67 | sell /  / trend_8_26 AND momentum_26: prior completed bar target 0%; next bar open simulation |
| v1 | trend_8_26 + momentum_26 | 9900.74 | -99.26 | sell /  / trend_8_26 + momentum_26: prior completed bar target 0%; next bar open simulation |
| v1 | trend_8_26 AND breakout_8 | 9937.40 | -62.60 | sell /  / trend_8_26 AND breakout_8: prior completed bar target 0%; next bar open simulation |
| v1 | trend_8_26 + breakout_8 | 9793.89 | -206.11 | buy /  / trend_8_26 + breakout_8: prior completed bar target 50%; next bar open simulation |
| v1 | trend_8_26 AND reversion_12 | 9992.01 | -7.99 | sell /  / trend_8_26 AND reversion_12: prior completed bar target 0%; next bar open simulation |
| v1 | trend_8_26 + reversion_12 | 9897.42 | -102.58 | sell /  / trend_8_26 + reversion_12: prior completed bar target 0%; next bar open simulation |
| v1 | trend_8_26 AND volume_26 | 9935.63 | -64.37 | sell /  / trend_8_26 AND volume_26: prior completed bar target 0%; next bar open simulation |
| v1 | trend_8_26 + volume_26 | 9894.03 | -105.97 | sell /  / trend_8_26 + volume_26: prior completed bar target 0%; next bar open simulation |
| v1 | momentum_26 AND breakout_8 | 9911.77 | -88.23 | sell /  / momentum_26 AND breakout_8: prior completed bar target 0%; next bar open simulation |
| v1 | momentum_26 + breakout_8 | 9791.22 | -208.78 | buy /  / momentum_26 + breakout_8: prior completed bar target 50%; next bar open simulation |
| v1 | momentum_26 AND reversion_12 | 10000.00 | 0.00 | 대기 /  / 새 신호 대기 |
| v1 | momentum_26 + reversion_12 | 9914.55 | -85.45 | sell /  / momentum_26 + reversion_12: prior completed bar target 0%; next bar open simulation |
| v1 | momentum_26 AND volume_26 | 10000.00 | 0.00 | 대기 /  / 새 신호 대기 |
| v1 | momentum_26 + volume_26 | 9911.13 | -88.87 | sell /  / momentum_26 + volume_26: prior completed bar target 0%; next bar open simulation |
| v1 | breakout_8 AND reversion_12 | 10000.00 | 0.00 | 대기 /  / 새 신호 대기 |
| v1 | breakout_8 + reversion_12 | 9787.95 | -212.05 | buy /  / breakout_8 + reversion_12: prior completed bar target 50%; next bar open simulation |
| v1 | breakout_8 AND volume_26 | 10000.00 | 0.00 | 대기 /  / 새 신호 대기 |
| v1 | breakout_8 + volume_26 | 9784.57 | -215.43 | buy /  / breakout_8 + volume_26: prior completed bar target 50%; next bar open simulation |
| v1 | reversion_12 AND volume_26 | 9974.59 | -25.41 | sell /  / reversion_12 AND volume_26: prior completed bar target 0%; next bar open simulation |
| v1 | reversion_12 + volume_26 | 9907.87 | -92.13 | sell /  / reversion_12 + volume_26: prior completed bar target 0%; next bar open simulation |
| v1 | ema_12_26 | 9781.22 | -218.78 | sell /  / EMA12 > EMA26; 조건 미충족; EMA12=255.193, EMA26=255.284 |
| v1 | macd_12_26_9 | 9756.47 | -243.53 | sell /  / MACD > 신호선 그리고 MACD > 0; 조건 미충족; MACD=-0.0912606, signal9=-0.0161084 |
| v1 | rsi_14_recovery | 9923.04 | -76.96 | sell /  / 직전 RSI14 < 30, 현재 RSI14 >= 30 (한 봉 목표); 조건 미충족; RSI14=40.3665, previous_RSI14=36.2025 |
| v1 | bollinger_20_reentry | 9881.04 | -118.96 | sell /  / 직전 종가 < 직전 하단밴드, 현재 하단밴드 <= 종가 <= SMA20 (한 봉 목표); 조건 미충족; close=251.75, lower20=251.316, SMA20=254.208, previous_lower20=251.691 |
| v1 | donchian_20 | 10000.00 | 0.00 | 대기 /  / 새 신호 대기 |
| v1 | atr_14_breakout | 9883.97 | -116.03 | sell /  / 종가 > 직전 종가 + 직전 ATR14 그리고 종가 > EMA26; 조건 미충족; close=256.72, threshold=258.136, prior_ATR14=1.3158, EMA26=255.146 |
| v1 | session_vwap | 9749.32 | -250.68 | buy /  / 종가 > 뉴욕 거래일별 누적 전형가격 VWAP; 조건 충족; close=252.75, session_VWAP=252.657, session_volume=4.65844e+06 |
| v1 | obv_20 | 9719.39 | -280.61 | sell /  / OBV > OBV의 SMA20 그리고 종가 > EMA26; 조건 미충족; OBV=3.09392e+06, OBV_SMA20=3.55727e+06, close=255.6, EMA26=255.387 |
| v1 | stochastic_14_3_recovery | 9862.87 | -137.13 | sell /  / 직전 %K14 < 20에서 %K14가 %D3 상향 돌파 (한 봉 목표); 조건 미충족; K14=28.9392, D3=18.1738, previous_K14=19.7943, previous_D3=12.6561 |
| v1 | mfi_14_recovery | 10000.00 | 0.00 | 대기 /  / 새 신호 대기 |
| v1 | adx_14_trend | 9823.79 | -176.21 | sell /  / Wilder ADX14 >= 25 그리고 +DI14 > -DI14; 조건 미충족; ADX14=24.7842, plus_DI14=27.3963, minus_DI14=19.1477 |
| v1 | aroon_25_trend | 9967.50 | -32.50 | sell /  / Aroon25 Up > 70 그리고 Down < 30 (동률이면 최신 극값); 조건 미충족; Aroon_up=68, Aroon_down=16 |
| v1 | cci_20_momentum | 9935.63 | -64.37 | sell /  / CCI20 > 100 (전형가격·평균절대편차); 조건 미충족; CCI20=62.9489 |
| v1 | williams_14_recovery | 9903.67 | -96.33 | sell /  / 직전 Williams %R14 < -80, 현재 >= -80 (한 봉 목표); 조건 미충족; Williams_R14=-61.3372, previous_R14=-71.0608 |
| v1 | cmf_20_accumulation | 10037.57 | 37.57 | buy /  / Chaikin Money Flow20 > 0.1; 조건 충족; CMF20=0.280188, volume20=5.69706e+06 |
| v1 | chaikin_3_10 | 9939.33 | -60.67 | sell /  / ADL의 EMA3 - EMA10 > 0 그리고 종가 > EMA26; 조건 미충족; Chaikin3_10=-18930.6, ADL=2.43796e+06, close=253.995, EMA26=255.284 |
| v1 | roc_10_momentum | 9816.66 | -183.34 | sell /  / 10봉 ROC > 1% 그리고 종가 > EMA26; 조건 미충족; ROC10_percent=-0.398319, close=255.08, EMA26=255.591 |
| v1 | trix_15_trend | 9840.00 | -160.00 | sell /  / 15봉 삼중 EMA의 1봉 변화율 TRIX > 0 그리고 종가 > EMA26; 조건 미충족; TRIX15_percent=0.000692295, close=255.155, EMA26=255.356 |
| v1 | keltner_20_breakout | 10000.00 | 0.00 | 대기 /  / 새 신호 대기 |
| v1 | opening_range_30m | 10000.00 | 0.00 | 대기 /  / 새 신호 대기 |
| v2 | cash | 10000.00 | 0.00 | 대기 /  / 새 신호 대기 |
| v2 | buy_hold | 9681.87 | -318.13 | 중단: 손실 한도 / buy / partial / 직전 완료 봉 목표 비중 100%; 다음 봉 시가 가정 |
| v2 | trend_8_26 | 9681.87 | -318.13 | 중단: 손실 한도 / buy / partial / 직전 완료 봉 목표 비중 100%; 다음 봉 시가 가정 |
| v2 | momentum_26 | 9681.87 | -318.13 | 중단: 손실 한도 / buy / partial / 직전 완료 봉 목표 비중 100%; 다음 봉 시가 가정 |
| v2 | breakout_8 | 9343.39 | -656.61 | 중단: 손실 한도 / sell / filled / 직전 완료 봉 목표 비중 0%; 다음 봉 시가 가정 |
| v2 | reversion_12 | 9581.23 | -418.77 | sell / filled / 직전 완료 봉 목표 비중 0%; 다음 봉 시가 가정 |
| v2 | volume_26 | 9672.67 | -327.33 | sell / filled / 직전 완료 봉 목표 비중 0%; 다음 봉 시가 가정 |
| v2 | trend_8_26 AND momentum_26 | 9681.87 | -318.13 | 중단: 손실 한도 / buy / partial / 직전 완료 봉 목표 비중 100%; 다음 봉 시가 가정 |
| v2 | trend_8_26 + momentum_26 | 9681.87 | -318.13 | 중단: 손실 한도 / buy / partial / 직전 완료 봉 목표 비중 100%; 다음 봉 시가 가정 |
| v2 | trend_8_26 AND breakout_8 | 9419.39 | -580.61 | 중단: 손실 한도 / sell / filled / 직전 완료 봉 목표 비중 0%; 다음 봉 시가 가정 |
| v2 | trend_8_26 + breakout_8 | 9366.48 | -633.52 | buy / filled / 직전 완료 봉 목표 비중 50%; 다음 봉 시가 가정 |
| v2 | trend_8_26 AND reversion_12 | 9968.12 | -31.88 | sell / filled / 직전 완료 봉 목표 비중 0%; 다음 봉 시가 가정 |
| v2 | trend_8_26 + reversion_12 | 9732.92 | -267.08 | 중단: 손실 한도 / sell / filled / 직전 완료 봉 목표 비중 0%; 다음 봉 시가 가정 |
| v2 | trend_8_26 AND volume_26 | 9805.21 | -194.79 | sell / filled / 직전 완료 봉 목표 비중 0%; 다음 봉 시가 가정 |
| v2 | trend_8_26 + volume_26 | 9813.52 | -186.48 | 중단: 손실 한도 / buy / filled / 직전 완료 봉 목표 비중 50%; 다음 봉 시가 가정 |
| v2 | momentum_26 AND breakout_8 | 9512.11 | -487.89 | sell / filled / 직전 완료 봉 목표 비중 0%; 다음 봉 시가 가정 |
| v2 | momentum_26 + breakout_8 | 9355.12 | -644.88 | buy / filled / 직전 완료 봉 목표 비중 50%; 다음 봉 시가 가정 |
| v2 | momentum_26 AND reversion_12 | 9938.87 | -61.13 | sell / filled / 직전 완료 봉 목표 비중 0%; 다음 봉 시가 가정 |
| v2 | momentum_26 + reversion_12 | 9732.92 | -267.08 | 중단: 손실 한도 / sell / filled / 직전 완료 봉 목표 비중 0%; 다음 봉 시가 가정 |
| v2 | momentum_26 AND volume_26 | 9920.93 | -79.07 | sell / filled / 직전 완료 봉 목표 비중 0%; 다음 봉 시가 가정 |
| v2 | momentum_26 + volume_26 | 9813.52 | -186.48 | 중단: 손실 한도 / buy / filled / 직전 완료 봉 목표 비중 50%; 다음 봉 시가 가정 |
| v2 | breakout_8 AND reversion_12 | 10000.00 | 0.00 | 대기 /  / 새 신호 대기 |
| v2 | breakout_8 + reversion_12 | 9370.86 | -629.14 | buy / filled / 직전 완료 봉 목표 비중 50%; 다음 봉 시가 가정 |
| v2 | breakout_8 AND volume_26 | 9814.17 | -185.83 | sell / filled / 직전 완료 봉 목표 비중 0%; 다음 봉 시가 가정 |
| v2 | breakout_8 + volume_26 | 9395.65 | -604.35 | buy / filled / 직전 완료 봉 목표 비중 50%; 다음 봉 시가 가정 |
| v2 | reversion_12 AND volume_26 | 9859.15 | -140.85 | sell / filled / 직전 완료 봉 목표 비중 0%; 다음 봉 시가 가정 |
| v2 | reversion_12 + volume_26 | 9667.54 | -332.46 | sell / filled / 직전 완료 봉 목표 비중 0%; 다음 봉 시가 가정 |
| v2 | ema_12_26 | 9777.31 | -222.69 | sell / filled / EMA12 > EMA26; 조건 미충족; EMA12=255.193, EMA26=255.284; 직전 완료 봉 목표를 다음 봉 시가에 모의 적용 |
| v2 | macd_12_26_9 | 9752.57 | -247.43 | sell / filled / MACD > 신호선 그리고 MACD > 0; 조건 미충족; MACD=-0.0912606, signal9=-0.0161084; 직전 완료 봉 목표를 다음 봉 시가에 모의 적용 |
| v2 | rsi_14_recovery | 9919.07 | -80.93 | sell / filled / 직전 RSI14 < 30, 현재 RSI14 >= 30 (한 봉 목표); 조건 미충족; RSI14=40.3665, previous_RSI14=36.2025; 직전 완료 봉 목표를 다음 봉 시가에 모의 적용 |
| v2 | bollinger_20_reentry | 9877.09 | -122.91 | sell / filled / 직전 종가 < 직전 하단밴드, 현재 하단밴드 <= 종가 <= SMA20 (한 봉 목표); 조건 미충족; close=251.75, lower20=251.316, SMA20=254.208, previous_lower20=251.691; 직전 완료 봉 목표를 다음 봉 시가에 모의 적용 |
| v2 | donchian_20 | 10000.00 | 0.00 | 대기 /  / 새 신호 대기 |
| v2 | atr_14_breakout | 9880.02 | -119.98 | sell / filled / 종가 > 직전 종가 + 직전 ATR14 그리고 종가 > EMA26; 조건 미충족; close=256.72, threshold=258.136, prior_ATR14=1.3158, EMA26=255.146; 직전 완료 봉 목표를 다음 봉 시가에 모의 적용 |
| v2 | session_vwap | 9740.55 | -259.45 | buy / partial / 종가 > 뉴욕 거래일별 누적 전형가격 VWAP; 조건 충족; close=252.75, session_VWAP=252.657, session_volume=4.65844e+06; 직전 완료 봉 목표를 다음 봉 시가에 모의 적용 |
| v2 | obv_20 | 9711.62 | -288.38 | sell / filled / OBV > OBV의 SMA20 그리고 종가 > EMA26; 조건 미충족; OBV=3.09392e+06, OBV_SMA20=3.55727e+06, close=255.6, EMA26=255.387; 직전 완료 봉 목표를 다음 봉 시가에 모의 적용 |
| v2 | stochastic_14_3_recovery | 9856.96 | -143.04 | sell / filled / 직전 %K14 < 20에서 %K14가 %D3 상향 돌파 (한 봉 목표); 조건 미충족; K14=28.9392, D3=18.1738, previous_K14=19.7943, previous_D3=12.6561; 직전 완료 봉 목표를 다음 봉 시가에 모의 적용 |
| v2 | mfi_14_recovery | 10000.00 | 0.00 | 대기 /  / 새 신호 대기 |
| v2 | adx_14_trend | 9817.90 | -182.10 | sell / filled / Wilder ADX14 >= 25 그리고 +DI14 > -DI14; 조건 미충족; ADX14=24.7842, plus_DI14=27.3963, minus_DI14=19.1477; 직전 완료 봉 목표를 다음 봉 시가에 모의 적용 |
| v2 | aroon_25_trend | 9965.51 | -34.49 | sell / filled / Aroon25 Up > 70 그리고 Down < 30 (동률이면 최신 극값); 조건 미충족; Aroon_up=68, Aroon_down=16; 직전 완료 봉 목표를 다음 봉 시가에 모의 적용 |
| v2 | cci_20_momentum | 9933.64 | -66.36 | sell / filled / CCI20 > 100 (전형가격·평균절대편차); 조건 미충족; CCI20=62.9489; 직전 완료 봉 목표를 다음 봉 시가에 모의 적용 |
| v2 | williams_14_recovery | 9899.71 | -100.29 | sell / filled / 직전 Williams %R14 < -80, 현재 >= -80 (한 봉 목표); 조건 미충족; Williams_R14=-61.3372, previous_R14=-71.0608; 직전 완료 봉 목표를 다음 봉 시가에 모의 적용 |
| v2 | cmf_20_accumulation | 10036.57 | 36.57 | buy / partial / Chaikin Money Flow20 > 0.1; 조건 충족; CMF20=0.280188, volume20=5.69706e+06; 직전 완료 봉 목표를 다음 봉 시가에 모의 적용 |
| v2 | chaikin_3_10 | 9937.34 | -62.66 | sell / filled / ADL의 EMA3 - EMA10 > 0 그리고 종가 > EMA26; 조건 미충족; Chaikin3_10=-18930.6, ADL=2.43796e+06, close=253.995, EMA26=255.284; 직전 완료 봉 목표를 다음 봉 시가에 모의 적용 |
| v2 | roc_10_momentum | 9812.74 | -187.26 | sell / filled / 10봉 ROC > 1% 그리고 종가 > EMA26; 조건 미충족; ROC10_percent=-0.398319, close=255.08, EMA26=255.591; 직전 완료 봉 목표를 다음 봉 시가에 모의 적용 |
| v2 | trix_15_trend | 9836.06 | -163.94 | sell / filled / 15봉 삼중 EMA의 1봉 변화율 TRIX > 0 그리고 종가 > EMA26; 조건 미충족; TRIX15_percent=0.000692295, close=255.155, EMA26=255.356; 직전 완료 봉 목표를 다음 봉 시가에 모의 적용 |
| v2 | keltner_20_breakout | 10000.00 | 0.00 | 대기 /  / 새 신호 대기 |
| v2 | opening_range_30m | 10000.00 | 0.00 | 대기 /  / 새 신호 대기 |

### 같은 기간의 비용·노출 비교 (사후 연구)

| 전략 | 비용 전 | 비용 후 | 100% 보유 | 같은 평균 노출 보유 | 평균 노출 |
|---|---:|---:|---:|---:|---:|
| cash | 0.00% | 0.00% | -7.05% | -0.00% | 0.00% |
| buy_hold | -6.66% | -7.05% | -7.05% | -7.05% | 100.00% |
| trend_8_26 | 1.32% | -0.79% | -7.05% | -3.19% | 43.83% |
| momentum_26 | -0.31% | -4.01% | -7.05% | -3.19% | 43.83% |
| breakout_8 | -1.29% | -17.95% | -7.05% | -1.41% | 19.16% |
| reversion_12 | -8.19% | -16.29% | -7.05% | -2.32% | 31.76% |
| volume_26 | -1.41% | -8.20% | -7.05% | -0.49% | 6.56% |
| trend_8_26 AND momentum_26 | 1.48% | -1.46% | -7.05% | -2.76% | 37.80% |
| trend_8_26 + momentum_26 | 0.51% | -2.41% | -7.05% | -3.19% | 43.83% |
| trend_8_26 AND breakout_8 | 0.57% | -10.59% | -7.05% | -0.97% | 13.12% |
| trend_8_26 + breakout_8 | 0.03% | -9.76% | -7.05% | -2.31% | 31.50% |
| trend_8_26 AND reversion_12 | 0.87% | -2.05% | -7.05% | -0.39% | 5.25% |
| trend_8_26 + reversion_12 | -3.52% | -8.48% | -7.05% | -2.76% | 37.80% |
| trend_8_26 AND volume_26 | 0.41% | -1.67% | -7.05% | -0.10% | 1.31% |
| trend_8_26 + volume_26 | -0.02% | -4.35% | -7.05% | -1.85% | 25.20% |
| momentum_26 AND breakout_8 | 1.38% | -9.11% | -7.05% | -0.93% | 12.60% |
| momentum_26 + breakout_8 | -0.78% | -11.05% | -7.05% | -2.31% | 31.50% |
| momentum_26 AND reversion_12 | -0.75% | -3.22% | -7.05% | -0.43% | 5.77% |
| momentum_26 + reversion_12 | -4.30% | -9.60% | -7.05% | -2.76% | 37.80% |
| momentum_26 AND volume_26 | 0.65% | -0.61% | -7.05% | -0.06% | 0.79% |
| momentum_26 + volume_26 | -0.83% | -5.32% | -7.05% | -1.85% | 25.20% |
| breakout_8 AND reversion_12 | 0.00% | 0.00% | -7.05% | -0.00% | 0.00% |
| breakout_8 + reversion_12 | -4.78% | -16.60% | -7.05% | -1.87% | 25.47% |
| breakout_8 AND volume_26 | -0.91% | -2.15% | -7.05% | -0.06% | 0.79% |
| breakout_8 + volume_26 | -1.34% | -12.48% | -7.05% | -0.95% | 12.87% |
| reversion_12 AND volume_26 | -1.84% | -4.69% | -7.05% | -0.21% | 2.89% |
| reversion_12 + volume_26 | -4.84% | -11.41% | -7.05% | -1.41% | 19.16% |
| ema_12_26 | -1.86% | -4.30% | -7.05% | -2.83% | 38.85% |
| macd_12_26_9 | 4.01% | 1.42% | -7.05% | -1.83% | 24.93% |
| rsi_14_recovery | -1.66% | -7.67% | -7.05% | -0.29% | 3.94% |
| bollinger_20_reentry | -0.95% | -5.82% | -7.05% | -0.23% | 3.15% |
| donchian_20 | 0.63% | -6.31% | -7.05% | -0.49% | 6.56% |
| atr_14_breakout | 1.19% | -4.59% | -7.05% | -0.33% | 4.46% |
| session_vwap | 1.16% | -6.60% | -7.05% | -3.22% | 44.36% |
| obv_20 | -6.96% | -15.17% | -7.05% | -2.10% | 28.61% |
| stochastic_14_3_recovery | -1.34% | -14.11% | -7.05% | -0.64% | 8.66% |
| mfi_14_recovery | 0.33% | -0.93% | -7.05% | -0.06% | 0.79% |
| adx_14_trend | -2.56% | -7.35% | -7.05% | -2.29% | 31.23% |
| aroon_25_trend | 4.10% | 0.24% | -7.05% | -2.00% | 27.30% |
| cci_20_momentum | 0.59% | -5.56% | -7.05% | -1.47% | 19.95% |
| williams_14_recovery | -1.77% | -10.06% | -7.05% | -0.41% | 5.51% |
| cmf_20_accumulation | 3.14% | -0.68% | -7.05% | -1.81% | 24.67% |
| chaikin_3_10 | -3.32% | -7.30% | -7.05% | -2.17% | 29.66% |
| roc_10_momentum | -2.32% | -8.29% | -7.05% | -1.09% | 14.70% |
| trix_15_trend | -1.33% | -3.78% | -7.05% | -2.14% | 29.13% |
| keltner_20_breakout | 0.65% | -2.68% | -7.05% | -0.68% | 9.19% |
| opening_range_30m | 0.79% | -2.95% | -7.05% | -1.91% | 25.98% |

동일 구간·초기 자금, 종료 시 청산 비용 포함. 노출 맞춤은 사후 설명용이며 v2 실제 계좌 성과가 아닙니다.
[낙폭 분해·비용 영향·전체 구간](JNJ/comparison.json)

[v1 전체 기록](JNJ/accounts.json) · [v2 전체 기록](JNJ/accounts-v2.json)

## CAT 계좌

| 모델 | 전략 | 평가액 USD | 손익 USD | 최근 매매·이유 |
|---|---|---:|---:|---|
| v1 | cash | 10000.00 | 0.00 | 대기 /  / 새 신호 대기 |
| v1 | buy_hold | 9868.05 | -131.95 | buy /  / buy_hold: prior completed bar target 100%; next bar open simulation |
| v1 | trend_8_26 | 9953.84 | -46.16 | sell /  / trend_8_26: prior completed bar target 0%; next bar open simulation |
| v1 | momentum_26 | 9872.70 | -127.30 | sell /  / momentum_26: prior completed bar target 0%; next bar open simulation |
| v1 | breakout_8 | 9790.00 | -210.00 | sell /  / breakout_8: prior completed bar target 0%; next bar open simulation |
| v1 | reversion_12 | 9820.78 | -179.22 | sell /  / reversion_12: prior completed bar target 0%; next bar open simulation |
| v1 | volume_26 | 10000.00 | 0.00 | 대기 /  / 새 신호 대기 |
| v1 | trend_8_26 AND momentum_26 | 9873.91 | -126.09 | sell /  / trend_8_26 AND momentum_26: prior completed bar target 0%; next bar open simulation |
| v1 | trend_8_26 + momentum_26 | 9913.34 | -86.66 | sell /  / trend_8_26 + momentum_26: prior completed bar target 0%; next bar open simulation |
| v1 | trend_8_26 AND breakout_8 | 9850.32 | -149.68 | sell /  / trend_8_26 AND breakout_8: prior completed bar target 0%; next bar open simulation |
| v1 | trend_8_26 + breakout_8 | 9871.78 | -128.22 | sell /  / trend_8_26 + breakout_8: prior completed bar target 0%; next bar open simulation |
| v1 | trend_8_26 AND reversion_12 | 9928.06 | -71.94 | sell /  / trend_8_26 AND reversion_12: prior completed bar target 0%; next bar open simulation |
| v1 | trend_8_26 + reversion_12 | 9907.56 | -92.44 | sell /  / trend_8_26 + reversion_12: prior completed bar target 0%; next bar open simulation |
| v1 | trend_8_26 AND volume_26 | 10000.00 | 0.00 | 대기 /  / 새 신호 대기 |
| v1 | trend_8_26 + volume_26 | 9976.97 | -23.03 | sell /  / trend_8_26 + volume_26: prior completed bar target 0%; next bar open simulation |
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
| v1 | session_vwap | 9702.21 | -297.79 | buy /  / 종가 > 뉴욕 거래일별 누적 전형가격 VWAP; 조건 충족; close=726.52, session_VWAP=725.436, session_volume=782457 |
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
| v2 | buy_hold | 9075.39 | -924.61 | 중단: 손실 한도 / buy / partial / 직전 완료 봉 목표 비중 100%; 다음 봉 시가 가정 |
| v2 | trend_8_26 | 9876.93 | -123.07 | sell / filled / 직전 완료 봉 목표 비중 0%; 다음 봉 시가 가정 |
| v2 | momentum_26 | 9885.12 | -114.88 | sell / filled / 직전 완료 봉 목표 비중 0%; 다음 봉 시가 가정 |
| v2 | breakout_8 | 9610.96 | -389.04 | sell / filled / 직전 완료 봉 목표 비중 0%; 다음 봉 시가 가정 |
| v2 | reversion_12 | 8948.65 | -1051.35 | 중단: 손실 한도 / buy / partial / 직전 완료 봉 목표 비중 100%; 다음 봉 시가 가정 |
| v2 | volume_26 | 9204.57 | -795.43 | 중단: 손실 한도 / buy / partial / 직전 완료 봉 목표 비중 100%; 다음 봉 시가 가정 |
| v2 | trend_8_26 AND momentum_26 | 9914.96 | -85.04 | sell / filled / 직전 완료 봉 목표 비중 0%; 다음 봉 시가 가정 |
| v2 | trend_8_26 + momentum_26 | 9881.18 | -118.82 | sell / filled / 직전 완료 봉 목표 비중 0%; 다음 봉 시가 가정 |
| v2 | trend_8_26 AND breakout_8 | 9765.08 | -234.92 | sell / filled / 직전 완료 봉 목표 비중 0%; 다음 봉 시가 가정 |
| v2 | trend_8_26 + breakout_8 | 9743.50 | -256.50 | sell / filled / 직전 완료 봉 목표 비중 0%; 다음 봉 시가 가정 |
| v2 | trend_8_26 AND reversion_12 | 9738.62 | -261.38 | sell / filled / 직전 완료 봉 목표 비중 0%; 다음 봉 시가 가정 |
| v2 | trend_8_26 + reversion_12 | 9530.49 | -469.51 | sell / filled / 직전 완료 봉 목표 비중 0%; 다음 봉 시가 가정 |
| v2 | trend_8_26 AND volume_26 | 10035.44 | 35.44 | sell / filled / 직전 완료 봉 목표 비중 0%; 다음 봉 시가 가정 |
| v2 | trend_8_26 + volume_26 | 9609.89 | -390.11 | sell / filled / 직전 완료 봉 목표 비중 0%; 다음 봉 시가 가정 |
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
| v2 | reversion_12 AND volume_26 | 9140.90 | -859.10 | 중단: 손실 한도 / buy / partial / 직전 완료 봉 목표 비중 100%; 다음 봉 시가 가정 |
| v2 | reversion_12 + volume_26 | 9336.47 | -663.53 | 중단: 손실 한도 / sell / filled / 직전 완료 봉 목표 비중 50%; 다음 봉 시가 가정 |
| v2 | ema_12_26 | 9860.50 | -139.50 | sell / filled / EMA12 > EMA26; 조건 미충족; EMA12=735.622, EMA26=735.711; 직전 완료 봉 목표를 다음 봉 시가에 모의 적용 |
| v2 | macd_12_26_9 | 9902.20 | -97.80 | sell / filled / MACD > 신호선 그리고 MACD > 0; 조건 미충족; MACD=0.746548, signal9=0.752293; 직전 완료 봉 목표를 다음 봉 시가에 모의 적용 |
| v2 | rsi_14_recovery | 9984.99 | -15.01 | sell / filled / 직전 RSI14 < 30, 현재 RSI14 >= 30 (한 봉 목표); 조건 미충족; RSI14=42.2805, previous_RSI14=38.7468; 직전 완료 봉 목표를 다음 봉 시가에 모의 적용 |
| v2 | bollinger_20_reentry | 9761.22 | -238.78 | sell / filled / 직전 종가 < 직전 하단밴드, 현재 하단밴드 <= 종가 <= SMA20 (한 봉 목표); 조건 미충족; close=727.35, lower20=723.447, SMA20=732.513, previous_lower20=723.966; 직전 완료 봉 목표를 다음 봉 시가에 모의 적용 |
| v2 | donchian_20 | 9948.84 | -51.16 | sell / filled / 종가 > 현재 봉을 제외한 직전 20봉 최고가; 조건 미충족; close=739.81, prior_high20=742.28; 직전 완료 봉 목표를 다음 봉 시가에 모의 적용 |
| v2 | atr_14_breakout | 9784.13 | -215.87 | sell / filled / 종가 > 직전 종가 + 직전 ATR14 그리고 종가 > EMA26; 조건 미충족; close=731.995, threshold=738.753, prior_ATR14=5.19827, EMA26=730.642; 직전 완료 봉 목표를 다음 봉 시가에 모의 적용 |
| v2 | session_vwap | 9693.48 | -306.52 | buy / partial / 종가 > 뉴욕 거래일별 누적 전형가격 VWAP; 조건 충족; close=726.52, session_VWAP=725.436, session_volume=782457; 직전 완료 봉 목표를 다음 봉 시가에 모의 적용 |
| v2 | obv_20 | 9809.44 | -190.56 | sell / filled / OBV > OBV의 SMA20 그리고 종가 > EMA26; 조건 미충족; OBV=-3.10102e+06, OBV_SMA20=-4.20035e+06, close=734.925, EMA26=736.093; 직전 완료 봉 목표를 다음 봉 시가에 모의 적용 |
| v2 | stochastic_14_3_recovery | 9833.19 | -166.81 | sell / filled / 직전 %K14 < 20에서 %K14가 %D3 상향 돌파 (한 봉 목표); 조건 미충족; K14=70.1066, D3=41.8677, previous_K14=37.4769, previous_D3=26.7366; 직전 완료 봉 목표를 다음 봉 시가에 모의 적용 |
| v2 | mfi_14_recovery | 10054.30 | 54.30 | sell / filled / 직전 MFI14 < 20, 현재 MFI14 >= 20 (한 봉 목표); 조건 미충족; MFI14=34.3275, previous_MFI14=29.4992; 직전 완료 봉 목표를 다음 봉 시가에 모의 적용 |
| v2 | adx_14_trend | 10000.00 | 0.00 | 대기 /  / 새 신호 대기 |
| v2 | aroon_25_trend | 10029.14 | 29.14 | sell / filled / Aroon25 Up > 70 그리고 Down < 30 (동률이면 최신 극값); 조건 미충족; Aroon_up=88, Aroon_down=48; 직전 완료 봉 목표를 다음 봉 시가에 모의 적용 |
| v2 | cci_20_momentum | 10022.77 | 22.77 | sell / filled / CCI20 > 100 (전형가격·평균절대편차); 조건 미충족; CCI20=98.8062; 직전 완료 봉 목표를 다음 봉 시가에 모의 적용 |
| v2 | williams_14_recovery | 9988.83 | -11.17 | sell / filled / 직전 Williams %R14 < -80, 현재 >= -80 (한 봉 목표); 조건 미충족; Williams_R14=-29.8934, previous_R14=-62.5231; 직전 완료 봉 목표를 다음 봉 시가에 모의 적용 |
| v2 | cmf_20_accumulation | 9838.82 | -161.18 | sell / filled / Chaikin Money Flow20 > 0.1; 조건 미충족; CMF20=-0.0799774, volume20=4.73159e+06; 직전 완료 봉 목표를 다음 봉 시가에 모의 적용 |
| v2 | chaikin_3_10 | 9557.71 | -442.29 | 중단: 손실 한도 / buy / partial / ADL의 EMA3 - EMA10 > 0 그리고 종가 > EMA26; 조건 충족; Chaikin3_10=293683, ADL=-4.91156e+06, close=739.58, EMA26=736.187; 직전 완료 봉 목표를 다음 봉 시가에 모의 적용 |
| v2 | roc_10_momentum | 9961.14 | -38.86 | sell / filled / 10봉 ROC > 1% 그리고 종가 > EMA26; 조건 미충족; ROC10_percent=-0.134597, close=734.53, EMA26=735.486; 직전 완료 봉 목표를 다음 봉 시가에 모의 적용 |
| v2 | trix_15_trend | 9567.34 | -432.66 | 중단: 손실 한도 / buy / partial / 15봉 삼중 EMA의 1봉 변화율 TRIX > 0 그리고 종가 > EMA26; 조건 충족; TRIX15_percent=0.0196284, close=739.58, EMA26=736.187; 직전 완료 봉 목표를 다음 봉 시가에 모의 적용 |
| v2 | keltner_20_breakout | 10000.00 | 0.00 | 대기 /  / 새 신호 대기 |
| v2 | opening_range_30m | 10038.70 | 38.70 | sell / filled / 뉴욕 09:30·09:45 두 완료 봉 최고가를 10:00 이후 종가가 돌파; 자료 부족·변동폭 또는 거래량 없음: 대기; close=740.21; 직전 완료 봉 목표를 다음 봉 시가에 모의 적용 |

### 같은 기간의 비용·노출 비교 (사후 연구)

| 전략 | 비용 전 | 비용 후 | 100% 보유 | 같은 평균 노출 보유 | 평균 노출 |
|---|---:|---:|---:|---:|---:|
| cash | 0.00% | 0.00% | -11.60% | -0.00% | 0.00% |
| buy_hold | -11.22% | -11.60% | -11.60% | -11.60% | 100.00% |
| trend_8_26 | -0.47% | -3.76% | -11.60% | -5.43% | 46.19% |
| momentum_26 | -2.96% | -7.35% | -11.60% | -5.37% | 45.67% |
| breakout_8 | -2.78% | -15.01% | -11.60% | -1.71% | 14.44% |
| reversion_12 | -3.25% | -16.48% | -11.60% | -3.32% | 28.08% |
| volume_26 | -3.22% | -9.51% | -11.60% | -0.90% | 7.61% |
| trend_8_26 AND momentum_26 | -0.21% | -3.51% | -11.60% | -4.70% | 39.90% |
| trend_8_26 + momentum_26 | -1.71% | -5.56% | -11.60% | -5.40% | 45.93% |
| trend_8_26 AND breakout_8 | -1.69% | -8.46% | -11.60% | -0.84% | 7.09% |
| trend_8_26 + breakout_8 | -1.60% | -9.35% | -11.60% | -3.58% | 30.32% |
| trend_8_26 AND reversion_12 | 1.62% | -5.39% | -11.60% | -0.81% | 6.82% |
| trend_8_26 + reversion_12 | -1.81% | -9.56% | -11.60% | -4.38% | 37.14% |
| trend_8_26 AND volume_26 | 1.93% | -0.18% | -11.60% | -0.25% | 2.10% |
| trend_8_26 + volume_26 | -1.80% | -6.46% | -11.60% | -3.18% | 26.91% |
| momentum_26 AND breakout_8 | -2.12% | -9.25% | -11.60% | -0.90% | 7.61% |
| momentum_26 + breakout_8 | -2.83% | -11.23% | -11.60% | -3.55% | 30.06% |
| momentum_26 AND reversion_12 | -2.46% | -9.18% | -11.60% | -0.81% | 6.82% |
| momentum_26 + reversion_12 | -3.05% | -11.27% | -11.60% | -4.35% | 36.88% |
| momentum_26 AND volume_26 | 1.45% | -0.24% | -11.60% | -0.16% | 1.31% |
| momentum_26 + volume_26 | -3.03% | -8.02% | -11.60% | -3.15% | 26.64% |
| breakout_8 AND reversion_12 | 0.00% | 0.00% | -11.60% | -0.00% | 0.00% |
| breakout_8 + reversion_12 | -2.96% | -14.83% | -11.60% | -2.52% | 21.27% |
| breakout_8 AND volume_26 | 0.37% | -0.47% | -11.60% | -0.06% | 0.52% |
| breakout_8 + volume_26 | -2.97% | -11.73% | -11.60% | -1.31% | 11.03% |
| reversion_12 AND volume_26 | -1.40% | -5.45% | -11.60% | -0.59% | 4.99% |
| reversion_12 + volume_26 | -3.19% | -12.31% | -11.60% | -2.11% | 17.85% |
| ema_12_26 | -1.32% | -3.37% | -11.60% | -5.25% | 44.62% |
| macd_12_26_9 | 1.07% | -1.86% | -11.60% | -3.22% | 27.30% |
| rsi_14_recovery | -0.69% | -6.36% | -11.60% | -0.44% | 3.67% |
| bollinger_20_reentry | -0.24% | -6.33% | -11.60% | -0.47% | 3.94% |
| donchian_20 | -1.20% | -5.26% | -11.60% | -0.56% | 4.72% |
| atr_14_breakout | -1.85% | -8.23% | -11.60% | -0.53% | 4.46% |
| session_vwap | 0.29% | -11.58% | -11.60% | -5.19% | 44.09% |
| obv_20 | -4.13% | -13.32% | -11.60% | -2.73% | 23.10% |
| stochastic_14_3_recovery | -2.81% | -14.32% | -11.60% | -0.93% | 7.87% |
| mfi_14_recovery | 1.43% | -1.10% | -11.60% | -0.19% | 1.57% |
| adx_14_trend | -2.02% | -4.05% | -11.60% | -1.00% | 8.40% |
| aroon_25_trend | -1.25% | -4.91% | -11.60% | -1.52% | 12.86% |
| cci_20_momentum | -4.37% | -9.45% | -11.60% | -1.74% | 14.70% |
| williams_14_recovery | -0.47% | -10.39% | -11.60% | -0.78% | 6.56% |
| cmf_20_accumulation | -5.52% | -12.03% | -11.60% | -1.96% | 16.54% |
| chaikin_3_10 | -6.04% | -15.05% | -11.60% | -3.69% | 31.23% |
| roc_10_momentum | -1.79% | -7.40% | -11.60% | -1.49% | 12.60% |
| trix_15_trend | -1.68% | -6.12% | -11.60% | -4.06% | 34.38% |
| keltner_20_breakout | -2.87% | -5.29% | -11.60% | -0.31% | 2.62% |
| opening_range_30m | 6.14% | 1.77% | -11.60% | -2.36% | 19.95% |

동일 구간·초기 자금, 종료 시 청산 비용 포함. 노출 맞춤은 사후 설명용이며 v2 실제 계좌 성과가 아닙니다.
[낙폭 분해·비용 영향·전체 구간](CAT/comparison.json)

[v1 전체 기록](CAT/accounts.json) · [v2 전체 기록](CAT/accounts-v2.json)

## WMT 계좌

| 모델 | 전략 | 평가액 USD | 손익 USD | 최근 매매·이유 |
|---|---|---:|---:|---|
| v1 | cash | 10000.00 | 0.00 | 대기 /  / 새 신호 대기 |
| v1 | buy_hold | 10026.91 | 26.91 | buy /  / buy_hold: prior completed bar target 100%; next bar open simulation |
| v1 | trend_8_26 | 9895.09 | -104.91 | sell /  / trend_8_26: prior completed bar target 0%; next bar open simulation |
| v1 | momentum_26 | 9901.81 | -98.19 | buy /  / momentum_26: prior completed bar target 100%; next bar open simulation |
| v1 | breakout_8 | 9819.29 | -180.71 | buy /  / breakout_8: prior completed bar target 100%; next bar open simulation |
| v1 | reversion_12 | 9916.28 | -83.72 | sell /  / reversion_12: prior completed bar target 0%; next bar open simulation |
| v1 | volume_26 | 9915.76 | -84.24 | sell /  / volume_26: prior completed bar target 0%; next bar open simulation |
| v1 | trend_8_26 AND momentum_26 | 9899.88 | -100.12 | sell /  / trend_8_26 AND momentum_26: prior completed bar target 0%; next bar open simulation |
| v1 | trend_8_26 + momentum_26 | 9898.48 | -101.52 | sell /  / trend_8_26 + momentum_26: prior completed bar target 50%; next bar open simulation |
| v1 | trend_8_26 AND breakout_8 | 9950.02 | -49.98 | sell /  / trend_8_26 AND breakout_8: prior completed bar target 0%; next bar open simulation |
| v1 | trend_8_26 + breakout_8 | 9857.02 | -142.98 | sell /  / trend_8_26 + breakout_8: prior completed bar target 50%; next bar open simulation |
| v1 | trend_8_26 AND reversion_12 | 9967.64 | -32.36 | sell /  / trend_8_26 AND reversion_12: prior completed bar target 0%; next bar open simulation |
| v1 | trend_8_26 + reversion_12 | 9925.44 | -74.56 | sell /  / trend_8_26 + reversion_12: prior completed bar target 0%; next bar open simulation |
| v1 | trend_8_26 AND volume_26 | 10000.00 | 0.00 | 대기 /  / 새 신호 대기 |
| v1 | trend_8_26 + volume_26 | 9905.33 | -94.67 | sell /  / trend_8_26 + volume_26: prior completed bar target 0%; next bar open simulation |
| v1 | momentum_26 AND breakout_8 | 9930.99 | -69.01 | buy /  / momentum_26 AND breakout_8: prior completed bar target 100%; next bar open simulation |
| v1 | momentum_26 + breakout_8 | 9900.04 | -99.96 | buy /  / momentum_26 + breakout_8: prior completed bar target 100%; next bar open simulation |
| v1 | momentum_26 AND reversion_12 | 10011.47 | 11.47 | sell /  / momentum_26 AND reversion_12: prior completed bar target 0%; next bar open simulation |
| v1 | momentum_26 + reversion_12 | 9948.64 | -51.36 | sell /  / momentum_26 + reversion_12: prior completed bar target 50%; next bar open simulation |
| v1 | momentum_26 AND volume_26 | 10013.52 | 13.52 | sell /  / momentum_26 AND volume_26: prior completed bar target 0%; next bar open simulation |
| v1 | momentum_26 + volume_26 | 9928.57 | -71.43 | sell /  / momentum_26 + volume_26: prior completed bar target 50%; next bar open simulation |
| v1 | breakout_8 AND reversion_12 | 10000.00 | 0.00 | 대기 /  / 새 신호 대기 |
| v1 | breakout_8 + reversion_12 | 9887.40 | -112.60 | sell /  / breakout_8 + reversion_12: prior completed bar target 50%; next bar open simulation |
| v1 | breakout_8 AND volume_26 | 9913.57 | -86.43 | sell /  / breakout_8 AND volume_26: prior completed bar target 0%; next bar open simulation |
| v1 | breakout_8 + volume_26 | 9867.47 | -132.53 | sell /  / breakout_8 + volume_26: prior completed bar target 50%; next bar open simulation |
| v1 | reversion_12 AND volume_26 | 10000.00 | 0.00 | 대기 /  / 새 신호 대기 |
| v1 | reversion_12 + volume_26 | 9955.79 | -44.21 | sell /  / reversion_12 + volume_26: prior completed bar target 0%; next bar open simulation |
| v1 | ema_12_26 | 9987.48 | -12.52 | sell /  / EMA12 > EMA26; 조건 미충족; EMA12=118.639, EMA26=118.64 |
| v1 | macd_12_26_9 | 10000.00 | 0.00 | 대기 /  / 새 신호 대기 |
| v1 | rsi_14_recovery | 10000.00 | 0.00 | 대기 /  / 새 신호 대기 |
| v1 | bollinger_20_reentry | 10000.00 | 0.00 | 대기 /  / 새 신호 대기 |
| v1 | donchian_20 | 10000.00 | 0.00 | 대기 /  / 새 신호 대기 |
| v1 | atr_14_breakout | 9979.72 | -20.28 | sell /  / 종가 > 직전 종가 + 직전 ATR14 그리고 종가 > EMA26; 조건 미충족; close=119.375, threshold=119.607, prior_ATR14=0.486823, EMA26=118.217 |
| v1 | session_vwap | 9712.30 | -287.70 | buy /  / 종가 > 뉴욕 거래일별 누적 전형가격 VWAP; 조건 충족; close=118.68, session_VWAP=118.618, session_volume=1.15133e+07 |
| v1 | obv_20 | 9841.07 | -158.93 | buy /  / OBV > OBV의 SMA20 그리고 종가 > EMA26; 조건 충족; OBV=2.23382e+07, OBV_SMA20=1.748e+07, close=118.68, EMA26=118.585 |
| v1 | stochastic_14_3_recovery | 9979.72 | -20.28 | sell /  / 직전 %K14 < 20에서 %K14가 %D3 상향 돌파 (한 봉 목표); 조건 미충족; K14=93.8952, D3=60.8222, previous_K14=82.4242, previous_D3=34.5012 |
| v1 | mfi_14_recovery | 10000.00 | 0.00 | 대기 /  / 새 신호 대기 |
| v1 | adx_14_trend | 9991.69 | -8.31 | sell /  / Wilder ADX14 >= 25 그리고 +DI14 > -DI14; 조건 미충족; ADX14=24.5142, plus_DI14=24.7537, minus_DI14=21.6519 |
| v1 | aroon_25_trend | 10000.00 | 0.00 | 대기 /  / 새 신호 대기 |
| v1 | cci_20_momentum | 9932.96 | -67.04 | sell /  / CCI20 > 100 (전형가격·평균절대편차); 조건 미충족; CCI20=99.1325 |
| v1 | williams_14_recovery | 9979.72 | -20.28 | sell /  / 직전 Williams %R14 < -80, 현재 >= -80 (한 봉 목표); 조건 미충족; Williams_R14=-6.10484, previous_R14=-17.5758 |
| v1 | cmf_20_accumulation | 9869.74 | -130.26 | buy /  / Chaikin Money Flow20 > 0.1; 조건 충족; CMF20=0.112667, volume20=1.57051e+07 |
| v1 | chaikin_3_10 | 9700.09 | -299.91 | buy /  / ADL의 EMA3 - EMA10 > 0 그리고 종가 > EMA26; 조건 충족; Chaikin3_10=395736, ADL=1.91464e+07, close=118.68, EMA26=118.585 |
| v1 | roc_10_momentum | 10000.00 | 0.00 | 대기 /  / 새 신호 대기 |
| v1 | trix_15_trend | 9824.31 | -175.69 | sell /  / 15봉 삼중 EMA의 1봉 변화율 TRIX > 0 그리고 종가 > EMA26; 조건 미충족; TRIX15_percent=0.00969478, close=118.67, EMA26=118.682 |
| v1 | keltner_20_breakout | 10000.00 | 0.00 | 대기 /  / 새 신호 대기 |
| v1 | opening_range_30m | 10000.00 | 0.00 | 대기 /  / 새 신호 대기 |
| v2 | cash | 10000.00 | 0.00 | 대기 /  / 새 신호 대기 |
| v2 | buy_hold | 10623.42 | 623.42 | buy / partial / 직전 완료 봉 목표 비중 100%; 다음 봉 시가 가정 |
| v2 | trend_8_26 | 10297.28 | 297.28 | sell / filled / 직전 완료 봉 목표 비중 0%; 다음 봉 시가 가정 |
| v2 | momentum_26 | 10310.20 | 310.20 | buy / partial / 직전 완료 봉 목표 비중 100%; 다음 봉 시가 가정 |
| v2 | breakout_8 | 9777.73 | -222.27 | buy / partial / 직전 완료 봉 목표 비중 100%; 다음 봉 시가 가정 |
| v2 | reversion_12 | 9818.63 | -181.37 | sell / filled / 직전 완료 봉 목표 비중 0%; 다음 봉 시가 가정 |
| v2 | volume_26 | 9875.40 | -124.60 | sell / filled / 직전 완료 봉 목표 비중 0%; 다음 봉 시가 가정 |
| v2 | trend_8_26 AND momentum_26 | 10302.26 | 302.26 | sell / filled / 직전 완료 봉 목표 비중 0%; 다음 봉 시가 가정 |
| v2 | trend_8_26 + momentum_26 | 10303.71 | 303.71 | sell / filled / 직전 완료 봉 목표 비중 50%; 다음 봉 시가 가정 |
| v2 | trend_8_26 AND breakout_8 | 10036.12 | 36.12 | sell / filled / 직전 완료 봉 목표 비중 0%; 다음 봉 시가 가정 |
| v2 | trend_8_26 + breakout_8 | 10034.45 | 34.45 | sell / filled / 직전 완료 봉 목표 비중 50%; 다음 봉 시가 가정 |
| v2 | trend_8_26 AND reversion_12 | 9775.04 | -224.96 | sell / filled / 직전 완료 봉 목표 비중 0%; 다음 봉 시가 가정 |
| v2 | trend_8_26 + reversion_12 | 10077.59 | 77.59 | sell / filled / 직전 완료 봉 목표 비중 0%; 다음 봉 시가 가정 |
| v2 | trend_8_26 AND volume_26 | 9949.23 | -50.77 | sell / filled / 직전 완료 봉 목표 비중 0%; 다음 봉 시가 가정 |
| v2 | trend_8_26 + volume_26 | 10085.48 | 85.48 | sell / filled / 직전 완료 봉 목표 비중 0%; 다음 봉 시가 가정 |
| v2 | momentum_26 AND breakout_8 | 9892.91 | -107.09 | buy / partial / 직전 완료 봉 목표 비중 100%; 다음 봉 시가 가정 |
| v2 | momentum_26 + breakout_8 | 10083.15 | 83.15 | buy / partial / 직전 완료 봉 목표 비중 100%; 다음 봉 시가 가정 |
| v2 | momentum_26 AND reversion_12 | 9838.09 | -161.91 | sell / filled / 직전 완료 봉 목표 비중 0%; 다음 봉 시가 가정 |
| v2 | momentum_26 + reversion_12 | 10147.66 | 147.66 | sell / filled / 직전 완료 봉 목표 비중 50%; 다음 봉 시가 가정 |
| v2 | momentum_26 AND volume_26 | 9925.24 | -74.76 | sell / filled / 직전 완료 봉 목표 비중 0%; 다음 봉 시가 가정 |
| v2 | momentum_26 + volume_26 | 10113.11 | 113.11 | sell / filled / 직전 완료 봉 목표 비중 50%; 다음 봉 시가 가정 |
| v2 | breakout_8 AND reversion_12 | 10000.00 | 0.00 | 대기 /  / 새 신호 대기 |
| v2 | breakout_8 + reversion_12 | 9840.51 | -159.49 | sell / filled / 직전 완료 봉 목표 비중 50%; 다음 봉 시가 가정 |
| v2 | breakout_8 AND volume_26 | 9860.28 | -139.72 | sell / filled / 직전 완료 봉 목표 비중 0%; 다음 봉 시가 가정 |
| v2 | breakout_8 + volume_26 | 9827.87 | -172.13 | sell / filled / 직전 완료 봉 목표 비중 50%; 다음 봉 시가 가정 |
| v2 | reversion_12 AND volume_26 | 10009.78 | 9.78 | sell / filled / 직전 완료 봉 목표 비중 0%; 다음 봉 시가 가정 |
| v2 | reversion_12 + volume_26 | 9888.34 | -111.66 | sell / filled / 직전 완료 봉 목표 비중 0%; 다음 봉 시가 가정 |
| v2 | ema_12_26 | 9985.48 | -14.52 | sell / filled / EMA12 > EMA26; 조건 미충족; EMA12=118.639, EMA26=118.64; 직전 완료 봉 목표를 다음 봉 시가에 모의 적용 |
| v2 | macd_12_26_9 | 10000.00 | 0.00 | 대기 /  / 새 신호 대기 |
| v2 | rsi_14_recovery | 10000.00 | 0.00 | 대기 /  / 새 신호 대기 |
| v2 | bollinger_20_reentry | 10000.00 | 0.00 | 대기 /  / 새 신호 대기 |
| v2 | donchian_20 | 10000.00 | 0.00 | 대기 /  / 새 신호 대기 |
| v2 | atr_14_breakout | 9977.72 | -22.28 | sell / filled / 종가 > 직전 종가 + 직전 ATR14 그리고 종가 > EMA26; 조건 미충족; close=119.375, threshold=119.607, prior_ATR14=0.486823, EMA26=118.217; 직전 완료 봉 목표를 다음 봉 시가에 모의 적용 |
| v2 | session_vwap | 9701.62 | -298.38 | buy / partial / 종가 > 뉴욕 거래일별 누적 전형가격 VWAP; 조건 충족; close=118.68, session_VWAP=118.618, session_volume=1.15133e+07; 직전 완료 봉 목표를 다음 봉 시가에 모의 적용 |
| v2 | obv_20 | 9834.18 | -165.82 | buy / partial / OBV > OBV의 SMA20 그리고 종가 > EMA26; 조건 충족; OBV=2.23382e+07, OBV_SMA20=1.748e+07, close=118.68, EMA26=118.585; 직전 완료 봉 목표를 다음 봉 시가에 모의 적용 |
| v2 | stochastic_14_3_recovery | 9977.72 | -22.28 | sell / filled / 직전 %K14 < 20에서 %K14가 %D3 상향 돌파 (한 봉 목표); 조건 미충족; K14=93.8952, D3=60.8222, previous_K14=82.4242, previous_D3=34.5012; 직전 완료 봉 목표를 다음 봉 시가에 모의 적용 |
| v2 | mfi_14_recovery | 10000.00 | 0.00 | 대기 /  / 새 신호 대기 |
| v2 | adx_14_trend | 9989.70 | -10.30 | sell / filled / Wilder ADX14 >= 25 그리고 +DI14 > -DI14; 조건 미충족; ADX14=24.5142, plus_DI14=24.7537, minus_DI14=21.6519; 직전 완료 봉 목표를 다음 봉 시가에 모의 적용 |
| v2 | aroon_25_trend | 10000.00 | 0.00 | 대기 /  / 새 신호 대기 |
| v2 | cci_20_momentum | 9930.98 | -69.02 | sell / filled / CCI20 > 100 (전형가격·평균절대편차); 조건 미충족; CCI20=99.1325; 직전 완료 봉 목표를 다음 봉 시가에 모의 적용 |
| v2 | williams_14_recovery | 9977.72 | -22.28 | sell / filled / 직전 Williams %R14 < -80, 현재 >= -80 (한 봉 목표); 조건 미충족; Williams_R14=-6.10484, previous_R14=-17.5758; 직전 완료 봉 목표를 다음 봉 시가에 모의 적용 |
| v2 | cmf_20_accumulation | 9864.81 | -135.19 | buy / partial / Chaikin Money Flow20 > 0.1; 조건 충족; CMF20=0.112667, volume20=1.57051e+07; 직전 완료 봉 목표를 다음 봉 시가에 모의 적용 |
| v2 | chaikin_3_10 | 9689.43 | -310.57 | buy / partial / ADL의 EMA3 - EMA10 > 0 그리고 종가 > EMA26; 조건 충족; Chaikin3_10=395736, ADL=1.91464e+07, close=118.68, EMA26=118.585; 직전 완료 봉 목표를 다음 봉 시가에 모의 적용 |
| v2 | roc_10_momentum | 10000.00 | 0.00 | 대기 /  / 새 신호 대기 |
| v2 | trix_15_trend | 9818.42 | -181.58 | sell / filled / 15봉 삼중 EMA의 1봉 변화율 TRIX > 0 그리고 종가 > EMA26; 조건 미충족; TRIX15_percent=0.00969478, close=118.67, EMA26=118.682; 직전 완료 봉 목표를 다음 봉 시가에 모의 적용 |
| v2 | keltner_20_breakout | 10000.00 | 0.00 | 대기 /  / 새 신호 대기 |
| v2 | opening_range_30m | 10000.00 | 0.00 | 대기 /  / 새 신호 대기 |

### 같은 기간의 비용·노출 비교 (사후 연구)

| 전략 | 비용 전 | 비용 후 | 100% 보유 | 같은 평균 노출 보유 | 평균 노출 |
|---|---:|---:|---:|---:|---:|
| cash | 0.00% | 0.00% | 8.63% | 0.00% | 0.00% |
| buy_hold | 9.08% | 8.63% | 8.63% | 8.63% | 100.00% |
| trend_8_26 | 8.17% | 5.03% | 8.63% | 5.64% | 65.62% |
| momentum_26 | 6.67% | 1.00% | 8.63% | 5.75% | 66.93% |
| breakout_8 | 5.01% | -11.60% | 8.63% | 2.20% | 25.72% |
| reversion_12 | 4.11% | -6.66% | 8.63% | 1.53% | 17.85% |
| volume_26 | -0.63% | -6.30% | 8.63% | 0.52% | 6.04% |
| trend_8_26 AND momentum_26 | 7.90% | 3.46% | 8.63% | 5.07% | 59.06% |
| trend_8_26 + momentum_26 | 7.42% | 3.00% | 8.63% | 5.70% | 66.28% |
| trend_8_26 AND breakout_8 | 6.75% | -5.88% | 8.63% | 1.77% | 20.73% |
| trend_8_26 + breakout_8 | 6.59% | -3.63% | 8.63% | 3.92% | 45.68% |
| trend_8_26 AND reversion_12 | 0.27% | -4.66% | 8.63% | 0.56% | 6.56% |
| trend_8_26 + reversion_12 | 6.16% | -0.56% | 8.63% | 3.58% | 41.74% |
| trend_8_26 AND volume_26 | 0.53% | -1.56% | 8.63% | 0.16% | 1.84% |
| trend_8_26 + volume_26 | 3.71% | -0.37% | 8.63% | 3.07% | 35.83% |
| momentum_26 AND breakout_8 | 5.42% | -7.84% | 8.63% | 1.91% | 22.31% |
| momentum_26 + breakout_8 | 5.85% | -4.90% | 8.63% | 3.97% | 46.33% |
| momentum_26 AND reversion_12 | 1.20% | -4.18% | 8.63% | 0.63% | 7.35% |
| momentum_26 + reversion_12 | 5.42% | -0.62% | 8.63% | 3.63% | 42.39% |
| momentum_26 AND volume_26 | 0.38% | -3.75% | 8.63% | 0.25% | 2.89% |
| momentum_26 + volume_26 | 2.99% | -2.50% | 8.63% | 3.13% | 36.49% |
| breakout_8 AND reversion_12 | 0.00% | 0.00% | 8.63% | 0.00% | 0.00% |
| breakout_8 + reversion_12 | 4.59% | -8.58% | 8.63% | 1.86% | 21.79% |
| breakout_8 AND volume_26 | 1.02% | -1.49% | 8.63% | 0.16% | 1.84% |
| breakout_8 + volume_26 | 2.18% | -8.59% | 8.63% | 1.36% | 15.89% |
| reversion_12 AND volume_26 | -0.51% | -2.99% | 8.63% | 0.20% | 2.36% |
| reversion_12 + volume_26 | 1.72% | -5.89% | 8.63% | 1.02% | 11.95% |
| ema_12_26 | 8.67% | 7.31% | 8.63% | 5.87% | 68.24% |
| macd_12_26_9 | 7.96% | 4.83% | 8.63% | 2.81% | 32.81% |
| rsi_14_recovery | -0.68% | -2.74% | 8.63% | 0.11% | 1.31% |
| bollinger_20_reentry | 0.93% | -2.41% | 8.63% | 0.18% | 2.10% |
| donchian_20 | 4.80% | -7.22% | 8.63% | 1.12% | 13.12% |
| atr_14_breakout | -0.61% | -10.14% | 8.63% | 0.63% | 7.35% |
| session_vwap | 6.59% | -4.43% | 8.63% | 4.94% | 57.48% |
| obv_20 | 8.47% | 0.57% | 8.63% | 4.60% | 53.54% |
| stochastic_14_3_recovery | 1.36% | -8.36% | 8.63% | 0.54% | 6.30% |
| mfi_14_recovery | 0.02% | -0.81% | 8.63% | 0.04% | 0.52% |
| adx_14_trend | 8.84% | 6.13% | 8.63% | 4.35% | 50.66% |
| aroon_25_trend | 5.69% | 1.34% | 8.63% | 2.49% | 29.13% |
| cci_20_momentum | 7.19% | -0.62% | 8.63% | 2.65% | 30.97% |
| williams_14_recovery | 0.16% | -7.91% | 8.63% | 0.45% | 5.25% |
| cmf_20_accumulation | 8.14% | -0.57% | 8.63% | 2.90% | 33.86% |
| chaikin_3_10 | 5.19% | -3.29% | 8.63% | 4.30% | 50.13% |
| roc_10_momentum | -0.30% | -5.20% | 8.63% | 1.23% | 14.44% |
| trix_15_trend | 7.99% | 4.86% | 8.63% | 5.41% | 62.99% |
| keltner_20_breakout | 6.84% | 0.74% | 8.63% | 2.25% | 26.25% |
| opening_range_30m | 10.12% | 5.59% | 8.63% | 2.97% | 34.65% |

동일 구간·초기 자금, 종료 시 청산 비용 포함. 노출 맞춤은 사후 설명용이며 v2 실제 계좌 성과가 아닙니다.
[낙폭 분해·비용 영향·전체 구간](WMT/comparison.json)

[v1 전체 기록](WMT/accounts.json) · [v2 전체 기록](WMT/accounts-v2.json)
