# 모의투자 운영 현황

[PC·서버 장애 진단과 복구 방법](https://github.com/BaekJaeYeol/paper-trading-program/blob/main/investment-lab/docs/failure-recovery.md)

이번 실행 복구: {}

완료 봉 확인 주기: 기록 17/24회 · 기록 없는 예정 7회 · 아직 판정 전 2회 · 주의: 예약 시작 지연 또는 실행·저장 누락을 확인하세요.

[주기 판정 기준](https://github.com/BaekJaeYeol/paper-trading-program/blob/main/investment-lab/docs/session-coverage.md)

최근 확인: 2026-10-20T19:52:00.421979+00:00 (UTC)
다음 15분 확인 목표 (세션 실행 중에만 적용): 2026-10-20T20:07:00+00:00 (UTC, 실행 지연 가능)

실제 주문 없음. v1 기존 계좌와 v2 새 계좌의 시작일이 다르므로 수익률을 직접 우열 비교하지 마세요.
v2는 다음 봉 시가에 비용·스프레드·직전 거래량 제한을 적용한 가상 체결입니다. 미체결 잔량은 만료됩니다.

| 종목 | 상태 | 최근 성공 UTC | 마지막 완료 봉 UTC | 이번 새 봉 |
|---|---|---|---|---|
| SPY | updated | 2026-10-20T19:52:00.421979+00:00 | 2026-10-20T19:30:00+00:00 | 1 |
| QQQ | updated | 2026-10-20T19:52:00.421979+00:00 | 2026-10-20T19:30:00+00:00 | 1 |
| IWM | updated | 2026-10-20T19:52:00.421979+00:00 | 2026-10-20T19:30:00+00:00 | 1 |
| DIA | updated | 2026-10-20T19:52:00.421979+00:00 | 2026-10-20T19:30:00+00:00 | 1 |
| MSFT | updated | 2026-10-20T19:52:00.421979+00:00 | 2026-10-20T19:30:00+00:00 | 1 |
| JPM | updated | 2026-10-20T19:52:00.421979+00:00 | 2026-10-20T19:30:00+00:00 | 1 |
| XOM | updated | 2026-10-20T19:52:00.421979+00:00 | 2026-10-20T19:30:00+00:00 | 1 |
| JNJ | updated | 2026-10-20T19:52:00.421979+00:00 | 2026-10-20T19:30:00+00:00 | 1 |
| CAT | updated | 2026-10-20T19:52:00.421979+00:00 | 2026-10-20T19:30:00+00:00 | 1 |
| WMT | updated | 2026-10-20T19:52:00.421979+00:00 | 2026-10-20T19:30:00+00:00 | 1 |

이번 실행 소요: 47.82초
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
| v1 | buy_hold | 9918.34 | -81.66 | buy /  / buy_hold: prior completed bar target 100%; next bar open simulation |
| v1 | trend_8_26 | 9789.54 | -210.46 | sell /  / trend_8_26: prior completed bar target 0%; next bar open simulation |
| v1 | momentum_26 | 9746.62 | -253.38 | buy /  / momentum_26: prior completed bar target 100%; next bar open simulation |
| v1 | breakout_8 | 9707.92 | -292.08 | sell /  / breakout_8: prior completed bar target 0%; next bar open simulation |
| v1 | reversion_12 | 9742.00 | -258.00 | buy /  / reversion_12: prior completed bar target 100%; next bar open simulation |
| v1 | volume_26 | 9642.64 | -357.36 | sell /  / volume_26: prior completed bar target 0%; next bar open simulation |
| v1 | trend_8_26 AND momentum_26 | 9723.48 | -276.52 | sell /  / trend_8_26 AND momentum_26: prior completed bar target 0%; next bar open simulation |
| v1 | trend_8_26 + momentum_26 | 9768.05 | -231.95 | sell /  / trend_8_26 + momentum_26: prior completed bar target 50%; next bar open simulation |
| v1 | trend_8_26 AND breakout_8 | 9814.44 | -185.56 | sell /  / trend_8_26 AND breakout_8: prior completed bar target 0%; next bar open simulation |
| v1 | trend_8_26 + breakout_8 | 9787.60 | -212.40 | sell /  / trend_8_26 + breakout_8: prior completed bar target 0%; next bar open simulation |
| v1 | trend_8_26 AND reversion_12 | 9793.45 | -206.55 | sell /  / trend_8_26 AND reversion_12: prior completed bar target 0%; next bar open simulation |
| v1 | trend_8_26 + reversion_12 | 9765.62 | -234.38 | sell /  / trend_8_26 + reversion_12: prior completed bar target 50%; next bar open simulation |
| v1 | trend_8_26 AND volume_26 | 9688.02 | -311.98 | sell /  / trend_8_26 AND volume_26: prior completed bar target 0%; next bar open simulation |
| v1 | trend_8_26 + volume_26 | 9715.76 | -284.24 | sell /  / trend_8_26 + volume_26: prior completed bar target 0%; next bar open simulation |
| v1 | momentum_26 AND breakout_8 | 9786.94 | -213.06 | sell /  / momentum_26 AND breakout_8: prior completed bar target 0%; next bar open simulation |
| v1 | momentum_26 + breakout_8 | 9727.24 | -272.76 | buy /  / momentum_26 + breakout_8: prior completed bar target 50%; next bar open simulation |
| v1 | momentum_26 AND reversion_12 | 9813.75 | -186.25 | buy /  / momentum_26 AND reversion_12: prior completed bar target 100%; next bar open simulation |
| v1 | momentum_26 + reversion_12 | 9783.26 | -216.74 | buy /  / momentum_26 + reversion_12: prior completed bar target 100%; next bar open simulation |
| v1 | momentum_26 AND volume_26 | 9701.51 | -298.49 | sell /  / momentum_26 AND volume_26: prior completed bar target 0%; next bar open simulation |
| v1 | momentum_26 + volume_26 | 9694.42 | -305.58 | buy /  / momentum_26 + volume_26: prior completed bar target 50%; next bar open simulation |
| v1 | breakout_8 AND reversion_12 | 10000.00 | 0.00 | 대기 /  / 새 신호 대기 |
| v1 | breakout_8 + reversion_12 | 9724.72 | -275.28 | sell /  / breakout_8 + reversion_12: prior completed bar target 50%; next bar open simulation |
| v1 | breakout_8 AND volume_26 | 9878.80 | -121.20 | sell /  / breakout_8 AND volume_26: prior completed bar target 0%; next bar open simulation |
| v1 | breakout_8 + volume_26 | 9694.44 | -305.56 | sell /  / breakout_8 + volume_26: prior completed bar target 0%; next bar open simulation |
| v1 | reversion_12 AND volume_26 | 9861.02 | -138.98 | sell /  / reversion_12 AND volume_26: prior completed bar target 0%; next bar open simulation |
| v1 | reversion_12 + volume_26 | 9692.06 | -307.94 | sell /  / reversion_12 + volume_26: prior completed bar target 50%; next bar open simulation |
| v1 | ema_12_26 | 9779.20 | -220.80 | buy /  / EMA12 > EMA26; 조건 충족; EMA12=767.528, EMA26=767.458 |
| v1 | macd_12_26_9 | 9790.92 | -209.08 | sell /  / MACD > 신호선 그리고 MACD > 0; 조건 미충족; MACD=0.543331, signal9=0.570253 |
| v1 | rsi_14_recovery | 9899.32 | -100.68 | sell /  / 직전 RSI14 < 30, 현재 RSI14 >= 30 (한 봉 목표); 조건 미충족; RSI14=34.3611, previous_RSI14=32.906 |
| v1 | bollinger_20_reentry | 9835.17 | -164.83 | sell /  / 직전 종가 < 직전 하단밴드, 현재 하단밴드 <= 종가 <= SMA20 (한 봉 목표); 조건 미충족; close=763.39, lower20=762.854, SMA20=768.639, previous_lower20=763.636 |
| v1 | donchian_20 | 9918.97 | -81.03 | sell /  / 종가 > 현재 봉을 제외한 직전 20봉 최고가; 조건 미충족; close=771.51, prior_high20=771.74 |
| v1 | atr_14_breakout | 9891.49 | -108.51 | sell /  / 종가 > 직전 종가 + 직전 ATR14 그리고 종가 > EMA26; 조건 미충족; close=771.51, threshold=773.161, prior_ATR14=1.48112, EMA26=768.048 |
| v1 | session_vwap | 9780.02 | -219.98 | sell /  / 종가 > 뉴욕 거래일별 누적 전형가격 VWAP; 조건 미충족; close=768.93, session_VWAP=770.349, session_volume=4.83081e+07 |
| v1 | obv_20 | 9850.84 | -149.16 | sell /  / OBV > OBV의 SMA20 그리고 종가 > EMA26; 조건 미충족; OBV=-3.90101e+07, OBV_SMA20=-4.09907e+07, close=768.14, EMA26=768.933 |
| v1 | stochastic_14_3_recovery | 9699.30 | -300.70 | sell /  / 직전 %K14 < 20에서 %K14가 %D3 상향 돌파 (한 봉 목표); 조건 미충족; K14=23.0363, D3=19.8618, previous_K14=34.7815, previous_D3=23.5295 |
| v1 | mfi_14_recovery | 9875.98 | -124.02 | sell /  / 직전 MFI14 < 20, 현재 MFI14 >= 20 (한 봉 목표); 조건 미충족; MFI14=33.0962, previous_MFI14=27.4403 |
| v1 | adx_14_trend | 9981.96 | -18.04 | sell /  / Wilder ADX14 >= 25 그리고 +DI14 > -DI14; 조건 미충족; ADX14=24.2312, plus_DI14=28.3519, minus_DI14=24.6578 |
| v1 | aroon_25_trend | 9861.30 | -138.70 | sell /  / Aroon25 Up > 70 그리고 Down < 30 (동률이면 최신 극값); 조건 미충족; Aroon_up=68, Aroon_down=20 |
| v1 | cci_20_momentum | 9816.97 | -183.03 | sell /  / CCI20 > 100 (전형가격·평균절대편차); 조건 미충족; CCI20=80.9096 |
| v1 | williams_14_recovery | 9671.57 | -328.43 | sell /  / 직전 Williams %R14 < -80, 현재 >= -80 (한 봉 목표); 조건 미충족; Williams_R14=-76.9637, previous_R14=-65.2185 |
| v1 | cmf_20_accumulation | 9860.93 | -139.07 | buy /  / Chaikin Money Flow20 > 0.1; 조건 충족; CMF20=0.124634, volume20=9.6482e+07 |
| v1 | chaikin_3_10 | 9760.81 | -239.19 | sell /  / ADL의 EMA3 - EMA10 > 0 그리고 종가 > EMA26; 조건 미충족; Chaikin3_10=3.81506e+06, ADL=8.90144e+06, close=768.14, EMA26=768.933 |
| v1 | roc_10_momentum | 9953.42 | -46.58 | sell /  / 10봉 ROC > 1% 그리고 종가 > EMA26; 조건 미충족; ROC10_percent=0.806376, close=769.45, EMA26=767.181 |
| v1 | trix_15_trend | 9683.88 | -316.12 | sell /  / 15봉 삼중 EMA의 1봉 변화율 TRIX > 0 그리고 종가 > EMA26; 조건 미충족; TRIX15_percent=0.00796431, close=768.14, EMA26=768.933 |
| v1 | keltner_20_breakout | 9924.71 | -75.29 | sell /  / 종가 > EMA20 + 2 x Wilder ATR14; 조건 미충족; close=768.93, upper_Keltner=771.837, EMA20=768.595, ATR14=1.6209 |
| v1 | opening_range_30m | 9748.19 | -251.81 | buy /  / 뉴욕 09:30·09:45 두 완료 봉 최고가를 10:00 이후 종가가 돌파; 조건 충족; close=769.1, opening_high=768 |
| v2 | cash | 10000.00 | 0.00 | 대기 /  / 새 신호 대기 |
| v2 | buy_hold | 9846.80 | -153.20 | buy / partial / 직전 완료 봉 목표 비중 100%; 다음 봉 시가 가정 |
| v2 | trend_8_26 | 9670.66 | -329.34 | sell / filled / 직전 완료 봉 목표 비중 0%; 다음 봉 시가 가정 |
| v2 | momentum_26 | 9598.40 | -401.60 | buy / partial / 직전 완료 봉 목표 비중 100%; 다음 봉 시가 가정 |
| v2 | breakout_8 | 9305.21 | -694.79 | sell / filled / 직전 완료 봉 목표 비중 0%; 다음 봉 시가 가정 |
| v2 | reversion_12 | 9275.89 | -724.11 | buy / partial / 직전 완료 봉 목표 비중 100%; 다음 봉 시가 가정 |
| v2 | volume_26 | 9091.31 | -908.69 | sell / filled / 직전 완료 봉 목표 비중 0%; 다음 봉 시가 가정 |
| v2 | trend_8_26 AND momentum_26 | 9581.18 | -418.82 | sell / filled / 직전 완료 봉 목표 비중 0%; 다음 봉 시가 가정 |
| v2 | trend_8_26 + momentum_26 | 9634.47 | -365.53 | sell / filled / 직전 완료 봉 목표 비중 50%; 다음 봉 시가 가정 |
| v2 | trend_8_26 AND breakout_8 | 9635.18 | -364.82 | sell / filled / 직전 완료 봉 목표 비중 0%; 다음 봉 시가 가정 |
| v2 | trend_8_26 + breakout_8 | 9525.87 | -474.13 | sell / filled / 직전 완료 봉 목표 비중 0%; 다음 봉 시가 가정 |
| v2 | trend_8_26 AND reversion_12 | 9682.03 | -317.97 | sell / filled / 직전 완료 봉 목표 비중 0%; 다음 봉 시가 가정 |
| v2 | trend_8_26 + reversion_12 | 9470.78 | -529.22 | sell / filled / 직전 완료 봉 목표 비중 50%; 다음 봉 시가 가정 |
| v2 | trend_8_26 AND volume_26 | 9527.29 | -472.71 | sell / filled / 직전 완료 봉 목표 비중 0%; 다음 봉 시가 가정 |
| v2 | trend_8_26 + volume_26 | 9395.95 | -604.05 | sell / filled / 직전 완료 봉 목표 비중 0%; 다음 봉 시가 가정 |
| v2 | momentum_26 AND breakout_8 | 9565.51 | -434.49 | sell / filled / 직전 완료 봉 목표 비중 0%; 다음 봉 시가 가정 |
| v2 | momentum_26 + breakout_8 | 9450.58 | -549.42 | buy / filled / 직전 완료 봉 목표 비중 50%; 다음 봉 시가 가정 |
| v2 | momentum_26 AND reversion_12 | 9768.85 | -231.15 | buy / partial / 직전 완료 봉 목표 비중 100%; 다음 봉 시가 가정 |
| v2 | momentum_26 + reversion_12 | 9494.99 | -505.01 | buy / partial / 직전 완료 봉 목표 비중 100%; 다음 봉 시가 가정 |
| v2 | momentum_26 AND volume_26 | 9609.69 | -390.31 | sell / filled / 직전 완료 봉 목표 비중 0%; 다음 봉 시가 가정 |
| v2 | momentum_26 + volume_26 | 9400.13 | -599.87 | buy / filled / 직전 완료 봉 목표 비중 50%; 다음 봉 시가 가정 |
| v2 | breakout_8 AND reversion_12 | 10000.00 | 0.00 | 대기 /  / 새 신호 대기 |
| v2 | breakout_8 + reversion_12 | 9328.99 | -671.01 | sell / filled / 직전 완료 봉 목표 비중 50%; 다음 봉 시가 가정 |
| v2 | breakout_8 AND volume_26 | 9808.87 | -191.13 | sell / filled / 직전 완료 봉 목표 비중 0%; 다음 봉 시가 가정 |
| v2 | breakout_8 + volume_26 | 9255.27 | -744.73 | sell / filled / 직전 완료 봉 목표 비중 0%; 다음 봉 시가 가정 |
| v2 | reversion_12 AND volume_26 | 9602.16 | -397.84 | sell / filled / 직전 완료 봉 목표 비중 0%; 다음 봉 시가 가정 |
| v2 | reversion_12 + volume_26 | 9260.20 | -739.80 | sell / filled / 직전 완료 봉 목표 비중 50%; 다음 봉 시가 가정 |
| v2 | ema_12_26 | 9774.32 | -225.68 | buy / partial / EMA12 > EMA26; 조건 충족; EMA12=767.528, EMA26=767.458; 직전 완료 봉 목표를 다음 봉 시가에 모의 적용 |
| v2 | macd_12_26_9 | 9785.04 | -214.96 | sell / filled / MACD > 신호선 그리고 MACD > 0; 조건 미충족; MACD=0.543331, signal9=0.570253; 직전 완료 봉 목표를 다음 봉 시가에 모의 적용 |
| v2 | rsi_14_recovery | 9895.36 | -104.64 | sell / filled / 직전 RSI14 < 30, 현재 RSI14 >= 30 (한 봉 목표); 조건 미충족; RSI14=34.3611, previous_RSI14=32.906; 직전 완료 봉 목표를 다음 봉 시가에 모의 적용 |
| v2 | bollinger_20_reentry | 9829.27 | -170.73 | sell / filled / 직전 종가 < 직전 하단밴드, 현재 하단밴드 <= 종가 <= SMA20 (한 봉 목표); 조건 미충족; close=763.39, lower20=762.854, SMA20=768.639, previous_lower20=763.636; 직전 완료 봉 목표를 다음 봉 시가에 모의 적용 |
| v2 | donchian_20 | 9915.00 | -85.00 | sell / filled / 종가 > 현재 봉을 제외한 직전 20봉 최고가; 조건 미충족; close=771.51, prior_high20=771.74; 직전 완료 봉 목표를 다음 봉 시가에 모의 적용 |
| v2 | atr_14_breakout | 9885.56 | -114.44 | sell / filled / 종가 > 직전 종가 + 직전 ATR14 그리고 종가 > EMA26; 조건 미충족; close=771.51, threshold=773.161, prior_ATR14=1.48112, EMA26=768.048; 직전 완료 봉 목표를 다음 봉 시가에 모의 적용 |
| v2 | session_vwap | 9770.24 | -229.76 | sell / filled / 종가 > 뉴욕 거래일별 누적 전형가격 VWAP; 조건 미충족; close=768.93, session_VWAP=770.349, session_volume=4.83081e+07; 직전 완료 봉 목표를 다음 봉 시가에 모의 적용 |
| v2 | obv_20 | 9844.93 | -155.07 | sell / filled / OBV > OBV의 SMA20 그리고 종가 > EMA26; 조건 미충족; OBV=-3.90101e+07, OBV_SMA20=-4.09907e+07, close=768.14, EMA26=768.933; 직전 완료 봉 목표를 다음 봉 시가에 모의 적용 |
| v2 | stochastic_14_3_recovery | 9683.79 | -316.21 | sell / filled / 직전 %K14 < 20에서 %K14가 %D3 상향 돌파 (한 봉 목표); 조건 미충족; K14=23.0363, D3=19.8618, previous_K14=34.7815, previous_D3=23.5295; 직전 완료 봉 목표를 다음 봉 시가에 모의 적용 |
| v2 | mfi_14_recovery | 9870.05 | -129.95 | sell / filled / 직전 MFI14 < 20, 현재 MFI14 >= 20 (한 봉 목표); 조건 미충족; MFI14=33.0962, previous_MFI14=27.4403; 직전 완료 봉 목표를 다음 봉 시가에 모의 적용 |
| v2 | adx_14_trend | 9979.97 | -20.03 | sell / filled / Wilder ADX14 >= 25 그리고 +DI14 > -DI14; 조건 미충족; ADX14=24.2312, plus_DI14=28.3519, minus_DI14=24.6578; 직전 완료 봉 목표를 다음 봉 시가에 모의 적용 |
| v2 | aroon_25_trend | 9857.36 | -142.64 | sell / filled / Aroon25 Up > 70 그리고 Down < 30 (동률이면 최신 극값); 조건 미충족; Aroon_up=68, Aroon_down=20; 직전 완료 봉 목표를 다음 봉 시가에 모의 적용 |
| v2 | cci_20_momentum | 9809.12 | -190.88 | sell / filled / CCI20 > 100 (전형가격·평균절대편차); 조건 미충족; CCI20=80.9096; 직전 완료 봉 목표를 다음 봉 시가에 모의 적용 |
| v2 | williams_14_recovery | 9656.11 | -343.89 | sell / filled / 직전 Williams %R14 < -80, 현재 >= -80 (한 봉 목표); 조건 미충족; Williams_R14=-76.9637, previous_R14=-65.2185; 직전 완료 봉 목표를 다음 봉 시가에 모의 적용 |
| v2 | cmf_20_accumulation | 9856.00 | -144.00 | buy / partial / Chaikin Money Flow20 > 0.1; 조건 충족; CMF20=0.124634, volume20=9.6482e+07; 직전 완료 봉 목표를 다음 봉 시가에 모의 적용 |
| v2 | chaikin_3_10 | 9751.05 | -248.95 | sell / filled / ADL의 EMA3 - EMA10 > 0 그리고 종가 > EMA26; 조건 미충족; Chaikin3_10=3.81506e+06, ADL=8.90144e+06, close=768.14, EMA26=768.933; 직전 완료 봉 목표를 다음 봉 시가에 모의 적용 |
| v2 | roc_10_momentum | 9951.43 | -48.57 | sell / filled / 10봉 ROC > 1% 그리고 종가 > EMA26; 조건 미충족; ROC10_percent=0.806376, close=769.45, EMA26=767.181; 직전 완료 봉 목표를 다음 봉 시가에 모의 적용 |
| v2 | trix_15_trend | 9672.27 | -327.73 | sell / filled / 15봉 삼중 EMA의 1봉 변화율 TRIX > 0 그리고 종가 > EMA26; 조건 미충족; TRIX15_percent=0.00796431, close=768.14, EMA26=768.933; 직전 완료 봉 목표를 다음 봉 시가에 모의 적용 |
| v2 | keltner_20_breakout | 9922.73 | -77.27 | sell / filled / 종가 > EMA20 + 2 x Wilder ATR14; 조건 미충족; close=768.93, upper_Keltner=771.837, EMA20=768.595, ATR14=1.6209; 직전 완료 봉 목표를 다음 봉 시가에 모의 적용 |
| v2 | opening_range_30m | 9739.43 | -260.57 | buy / partial / 뉴욕 09:30·09:45 두 완료 봉 최고가를 10:00 이후 종가가 돌파; 조건 충족; close=769.1, opening_high=768; 직전 완료 봉 목표를 다음 봉 시가에 모의 적용 |

### 같은 기간의 비용·노출 비교 (사후 연구)

| 전략 | 비용 전 | 비용 후 | 100% 보유 | 같은 평균 노출 보유 | 평균 노출 |
|---|---:|---:|---:|---:|---:|
| cash | 0.00% | 0.00% | -0.43% | -0.00% | 0.00% |
| buy_hold | -0.01% | -0.43% | -0.43% | -0.43% | 100.00% |
| trend_8_26 | 0.51% | -3.21% | -0.43% | -0.23% | 54.57% |
| momentum_26 | -1.08% | -5.54% | -0.43% | -0.23% | 54.31% |
| breakout_8 | -0.61% | -16.68% | -0.43% | -0.09% | 21.93% |
| reversion_12 | -1.34% | -12.29% | -0.43% | -0.12% | 27.94% |
| volume_26 | -1.23% | -10.33% | -0.43% | -0.04% | 9.14% |
| trend_8_26 AND momentum_26 | -0.14% | -4.65% | -0.43% | -0.20% | 47.26% |
| trend_8_26 + momentum_26 | -0.28% | -4.38% | -0.43% | -0.23% | 54.44% |
| trend_8_26 AND breakout_8 | -0.42% | -11.84% | -0.43% | -0.06% | 13.32% |
| trend_8_26 + breakout_8 | -0.05% | -9.82% | -0.43% | -0.16% | 38.26% |
| trend_8_26 AND reversion_12 | -0.10% | -5.01% | -0.43% | -0.03% | 7.31% |
| trend_8_26 + reversion_12 | -0.41% | -7.68% | -0.43% | -0.18% | 41.26% |
| trend_8_26 AND volume_26 | -0.97% | -5.84% | -0.43% | -0.02% | 5.22% |
| trend_8_26 + volume_26 | -0.36% | -6.84% | -0.43% | -0.14% | 31.86% |
| momentum_26 AND breakout_8 | 0.01% | -11.83% | -0.43% | -0.06% | 14.62% |
| momentum_26 + breakout_8 | -0.84% | -11.29% | -0.43% | -0.16% | 38.13% |
| momentum_26 AND reversion_12 | -0.86% | -6.52% | -0.43% | -0.03% | 8.09% |
| momentum_26 + reversion_12 | -1.21% | -8.41% | -0.43% | -0.18% | 41.13% |
| momentum_26 AND volume_26 | -0.72% | -4.80% | -0.43% | -0.02% | 3.66% |
| momentum_26 + volume_26 | -1.15% | -7.00% | -0.43% | -0.14% | 31.73% |
| breakout_8 AND reversion_12 | 0.00% | 0.00% | -0.43% | -0.00% | 0.00% |
| breakout_8 + reversion_12 | -0.97% | -14.17% | -0.43% | -0.11% | 24.94% |
| breakout_8 AND volume_26 | -0.33% | -2.40% | -0.43% | -0.01% | 1.83% |
| breakout_8 + volume_26 | -0.92% | -12.84% | -0.43% | -0.07% | 15.54% |
| reversion_12 AND volume_26 | -0.87% | -5.34% | -0.43% | -0.02% | 3.92% |
| reversion_12 + volume_26 | -1.28% | -11.13% | -0.43% | -0.08% | 18.54% |
| ema_12_26 | -0.89% | -4.56% | -0.43% | -0.24% | 56.92% |
| macd_12_26_9 | -0.08% | -4.99% | -0.43% | -0.14% | 32.64% |
| rsi_14_recovery | -0.53% | -4.22% | -0.43% | -0.01% | 2.35% |
| bollinger_20_reentry | -1.07% | -6.72% | -0.43% | -0.02% | 3.66% |
| donchian_20 | -0.12% | -7.39% | -0.43% | -0.03% | 6.27% |
| atr_14_breakout | 0.26% | -5.07% | -0.43% | -0.02% | 3.66% |
| session_vwap | 1.67% | -8.08% | -0.43% | -0.20% | 45.95% |
| obv_20 | -0.14% | -7.80% | -0.43% | -0.16% | 37.34% |
| stochastic_14_3_recovery | -0.44% | -14.41% | -0.43% | -0.04% | 9.40% |
| mfi_14_recovery | -0.01% | -3.31% | -0.43% | -0.01% | 2.09% |
| adx_14_trend | 0.32% | -3.40% | -0.43% | -0.12% | 27.94% |
| aroon_25_trend | 0.82% | -2.10% | -0.43% | -0.11% | 25.59% |
| cci_20_momentum | -0.39% | -8.80% | -0.43% | -0.09% | 21.67% |
| williams_14_recovery | -0.61% | -10.89% | -0.43% | -0.03% | 6.79% |
| cmf_20_accumulation | 1.49% | -2.68% | -0.43% | -0.18% | 42.56% |
| chaikin_3_10 | 1.47% | -5.12% | -0.43% | -0.17% | 39.95% |
| roc_10_momentum | -0.13% | -0.97% | -0.43% | -0.00% | 1.04% |
| trix_15_trend | -0.55% | -5.04% | -0.43% | -0.18% | 42.82% |
| keltner_20_breakout | -0.26% | -3.96% | -0.43% | -0.05% | 10.70% |
| opening_range_30m | 0.02% | -6.09% | -0.43% | -0.16% | 37.60% |

동일 구간·초기 자금, 종료 시 청산 비용 포함. 노출 맞춤은 사후 설명용이며 v2 실제 계좌 성과가 아닙니다.
[낙폭 분해·비용 영향·전체 구간](SPY/comparison.json)

[v1 전체 기록](SPY/accounts.json) · [v2 전체 기록](SPY/accounts-v2.json)

## QQQ 계좌

| 모델 | 전략 | 평가액 USD | 손익 USD | 최근 매매·이유 |
|---|---|---:|---:|---|
| v1 | cash | 10000.00 | 0.00 | 대기 /  / 새 신호 대기 |
| v1 | buy_hold | 9871.89 | -128.11 | buy /  / buy_hold: prior completed bar target 100%; next bar open simulation |
| v1 | trend_8_26 | 9828.61 | -171.39 | sell /  / trend_8_26: prior completed bar target 0%; next bar open simulation |
| v1 | momentum_26 | 9547.76 | -452.24 | sell /  / momentum_26: prior completed bar target 0%; next bar open simulation |
| v1 | breakout_8 | 9695.44 | -304.56 | sell /  / breakout_8: prior completed bar target 0%; next bar open simulation |
| v1 | reversion_12 | 9741.18 | -258.82 | buy /  / reversion_12: prior completed bar target 100%; next bar open simulation |
| v1 | volume_26 | 9624.14 | -375.86 | sell /  / volume_26: prior completed bar target 0%; next bar open simulation |
| v1 | trend_8_26 AND momentum_26 | 9890.12 | -109.88 | sell /  / trend_8_26 AND momentum_26: prior completed bar target 0%; next bar open simulation |
| v1 | trend_8_26 + momentum_26 | 9706.64 | -293.36 | sell /  / trend_8_26 + momentum_26: prior completed bar target 0%; next bar open simulation |
| v1 | trend_8_26 AND breakout_8 | 9989.91 | -10.09 | sell /  / trend_8_26 AND breakout_8: prior completed bar target 0%; next bar open simulation |
| v1 | trend_8_26 + breakout_8 | 9800.88 | -199.12 | sell /  / trend_8_26 + breakout_8: prior completed bar target 0%; next bar open simulation |
| v1 | trend_8_26 AND reversion_12 | 9902.56 | -97.44 | sell /  / trend_8_26 AND reversion_12: prior completed bar target 0%; next bar open simulation |
| v1 | trend_8_26 + reversion_12 | 9804.47 | -195.53 | sell /  / trend_8_26 + reversion_12: prior completed bar target 50%; next bar open simulation |
| v1 | trend_8_26 AND volume_26 | 9864.33 | -135.67 | sell /  / trend_8_26 AND volume_26: prior completed bar target 0%; next bar open simulation |
| v1 | trend_8_26 + volume_26 | 9725.78 | -274.22 | sell /  / trend_8_26 + volume_26: prior completed bar target 0%; next bar open simulation |
| v1 | momentum_26 AND breakout_8 | 9726.83 | -273.17 | sell /  / momentum_26 AND breakout_8: prior completed bar target 0%; next bar open simulation |
| v1 | momentum_26 + breakout_8 | 9621.37 | -378.63 | sell /  / momentum_26 + breakout_8: prior completed bar target 0%; next bar open simulation |
| v1 | momentum_26 AND reversion_12 | 9800.84 | -199.16 | sell /  / momentum_26 AND reversion_12: prior completed bar target 0%; next bar open simulation |
| v1 | momentum_26 + reversion_12 | 9663.48 | -336.52 | sell /  / momentum_26 + reversion_12: prior completed bar target 50%; next bar open simulation |
| v1 | momentum_26 AND volume_26 | 9836.75 | -163.25 | sell /  / momentum_26 AND volume_26: prior completed bar target 0%; next bar open simulation |
| v1 | momentum_26 + volume_26 | 9605.04 | -394.96 | sell /  / momentum_26 + volume_26: prior completed bar target 0%; next bar open simulation |
| v1 | breakout_8 AND reversion_12 | 10000.00 | 0.00 | 대기 /  / 새 신호 대기 |
| v1 | breakout_8 + reversion_12 | 9737.79 | -262.21 | sell /  / breakout_8 + reversion_12: prior completed bar target 50%; next bar open simulation |
| v1 | breakout_8 AND volume_26 | 9947.15 | -52.85 | sell /  / breakout_8 AND volume_26: prior completed bar target 0%; next bar open simulation |
| v1 | breakout_8 + volume_26 | 9679.03 | -320.97 | sell /  / breakout_8 + volume_26: prior completed bar target 0%; next bar open simulation |
| v1 | reversion_12 AND volume_26 | 9907.31 | -92.69 | sell /  / reversion_12 AND volume_26: prior completed bar target 0%; next bar open simulation |
| v1 | reversion_12 + volume_26 | 9721.26 | -278.74 | sell /  / reversion_12 + volume_26: prior completed bar target 50%; next bar open simulation |
| v1 | ema_12_26 | 9594.71 | -405.29 | sell /  / EMA12 > EMA26; 조건 미충족; EMA12=718.879, EMA26=719.016 |
| v1 | macd_12_26_9 | 9746.03 | -253.97 | sell /  / MACD > 신호선 그리고 MACD > 0; 조건 미충족; MACD=0.0195537, signal9=0.0263977 |
| v1 | rsi_14_recovery | 9809.40 | -190.60 | sell /  / 직전 RSI14 < 30, 현재 RSI14 >= 30 (한 봉 목표); 조건 미충족; RSI14=50.2063, previous_RSI14=44.1729 |
| v1 | bollinger_20_reentry | 9878.60 | -121.40 | sell /  / 직전 종가 < 직전 하단밴드, 현재 하단밴드 <= 종가 <= SMA20 (한 봉 목표); 조건 미충족; close=718.66, lower20=714.386, SMA20=719.409, previous_lower20=714.271 |
| v1 | donchian_20 | 9951.11 | -48.89 | sell /  / 종가 > 현재 봉을 제외한 직전 20봉 최고가; 조건 미충족; close=724.13, prior_high20=724.151 |
| v1 | atr_14_breakout | 9945.80 | -54.20 | sell /  / 종가 > 직전 종가 + 직전 ATR14 그리고 종가 > EMA26; 조건 미충족; close=721.52, threshold=724.646, prior_ATR14=2.53578, EMA26=719.016 |
| v1 | session_vwap | 9757.98 | -242.02 | sell /  / 종가 > 뉴욕 거래일별 누적 전형가격 VWAP; 조건 미충족; close=719.05, session_VWAP=719.729, session_volume=3.45027e+08 |
| v1 | obv_20 | 9724.00 | -276.00 | sell /  / OBV > OBV의 SMA20 그리고 종가 > EMA26; 조건 미충족; OBV=2.65835e+08, OBV_SMA20=2.15387e+08, close=718.98, EMA26=719.158 |
| v1 | stochastic_14_3_recovery | 9575.60 | -424.40 | sell /  / 직전 %K14 < 20에서 %K14가 %D3 상향 돌파 (한 봉 목표); 조건 미충족; K14=26.1736, D3=21.5848, previous_K14=38.2558, previous_D3=23.006 |
| v1 | mfi_14_recovery | 9813.56 | -186.44 | sell /  / 직전 MFI14 < 20, 현재 MFI14 >= 20 (한 봉 목표); 조건 미충족; MFI14=30.3876, previous_MFI14=31.1747 |
| v1 | adx_14_trend | 9926.53 | -73.47 | sell /  / Wilder ADX14 >= 25 그리고 +DI14 > -DI14; 조건 미충족; ADX14=23.9831, plus_DI14=26.5781, minus_DI14=24.6326 |
| v1 | aroon_25_trend | 9875.01 | -124.99 | sell /  / Aroon25 Up > 70 그리고 Down < 30 (동률이면 최신 극값); 조건 미충족; Aroon_up=68, Aroon_down=20 |
| v1 | cci_20_momentum | 9880.19 | -119.81 | sell /  / CCI20 > 100 (전형가격·평균절대편차); 조건 미충족; CCI20=19.2232 |
| v1 | williams_14_recovery | 9666.48 | -333.52 | sell /  / 직전 Williams %R14 < -80, 현재 >= -80 (한 봉 목표); 조건 미충족; Williams_R14=-73.8264, previous_R14=-61.7442 |
| v1 | cmf_20_accumulation | 9581.47 | -418.53 | sell /  / Chaikin Money Flow20 > 0.1; 조건 미충족; CMF20=0.0778093, volume20=4.23002e+08 |
| v1 | chaikin_3_10 | 9730.83 | -269.17 | sell /  / ADL의 EMA3 - EMA10 > 0 그리고 종가 > EMA26; 조건 미충족; Chaikin3_10=-9825.14, ADL=2.60129e+08, close=719.13, EMA26=719.112 |
| v1 | roc_10_momentum | 9990.50 | -9.50 | sell /  / 10봉 ROC > 1% 그리고 종가 > EMA26; 조건 미충족; ROC10_percent=0.483561, close=722.477, EMA26=718.78 |
| v1 | trix_15_trend | 9672.97 | -327.03 | sell /  / 15봉 삼중 EMA의 1봉 변화율 TRIX > 0 그리고 종가 > EMA26; 조건 미충족; TRIX15_percent=0.000611733, close=718.98, EMA26=719.158 |
| v1 | keltner_20_breakout | 9904.16 | -95.84 | sell /  / 종가 > EMA20 + 2 x Wilder ATR14; 조건 미충족; close=723.31, upper_Keltner=723.407, EMA20=718.722, ATR14=2.34265 |
| v1 | opening_range_30m | 9744.58 | -255.42 | buy /  / 뉴욕 09:30·09:45 두 완료 봉 최고가를 10:00 이후 종가가 돌파; 조건 충족; close=718.66, opening_high=716.18 |
| v2 | cash | 10000.00 | 0.00 | 대기 /  / 새 신호 대기 |
| v2 | buy_hold | 9552.79 | -447.21 | buy / partial / 직전 완료 봉 목표 비중 100%; 다음 봉 시가 가정 |
| v2 | trend_8_26 | 9629.88 | -370.12 | sell / filled / 직전 완료 봉 목표 비중 0%; 다음 봉 시가 가정 |
| v2 | momentum_26 | 9440.70 | -559.30 | sell / filled / 직전 완료 봉 목표 비중 0%; 다음 봉 시가 가정 |
| v2 | breakout_8 | 9364.11 | -635.89 | sell / filled / 직전 완료 봉 목표 비중 0%; 다음 봉 시가 가정 |
| v2 | reversion_12 | 9253.80 | -746.20 | buy / partial / 직전 완료 봉 목표 비중 100%; 다음 봉 시가 가정 |
| v2 | volume_26 | 9565.80 | -434.20 | 중단: 손실 한도 / sell / filled / 직전 완료 봉 목표 비중 0%; 다음 봉 시가 가정 |
| v2 | trend_8_26 AND momentum_26 | 9785.10 | -214.90 | sell / filled / 직전 완료 봉 목표 비중 0%; 다음 봉 시가 가정 |
| v2 | trend_8_26 + momentum_26 | 9554.99 | -445.01 | sell / filled / 직전 완료 봉 목표 비중 0%; 다음 봉 시가 가정 |
| v2 | trend_8_26 AND breakout_8 | 9883.87 | -116.13 | sell / filled / 직전 완료 봉 목표 비중 0%; 다음 봉 시가 가정 |
| v2 | trend_8_26 + breakout_8 | 9535.95 | -464.05 | sell / filled / 직전 완료 봉 목표 비중 0%; 다음 봉 시가 가정 |
| v2 | trend_8_26 AND reversion_12 | 9761.15 | -238.85 | sell / filled / 직전 완료 봉 목표 비중 0%; 다음 봉 시가 가정 |
| v2 | trend_8_26 + reversion_12 | 9459.58 | -540.42 | sell / filled / 직전 완료 봉 목표 비중 50%; 다음 봉 시가 가정 |
| v2 | trend_8_26 AND volume_26 | 9698.84 | -301.16 | sell / filled / 직전 완료 봉 목표 비중 0%; 다음 봉 시가 가정 |
| v2 | trend_8_26 + volume_26 | 9329.51 | -670.49 | sell / filled / 직전 완료 봉 목표 비중 0%; 다음 봉 시가 가정 |
| v2 | momentum_26 AND breakout_8 | 9678.91 | -321.09 | sell / filled / 직전 완료 봉 목표 비중 0%; 다음 봉 시가 가정 |
| v2 | momentum_26 + breakout_8 | 9402.35 | -597.65 | sell / filled / 직전 완료 봉 목표 비중 0%; 다음 봉 시가 가정 |
| v2 | momentum_26 AND reversion_12 | 9794.96 | -205.04 | sell / filled / 직전 완료 봉 목표 비중 0%; 다음 봉 시가 가정 |
| v2 | momentum_26 + reversion_12 | 9385.97 | -614.03 | sell / filled / 직전 완료 봉 목표 비중 50%; 다음 봉 시가 가정 |
| v2 | momentum_26 AND volume_26 | 9768.76 | -231.24 | sell / filled / 직전 완료 봉 목표 비중 0%; 다음 봉 시가 가정 |
| v2 | momentum_26 + volume_26 | 9256.85 | -743.15 | sell / filled / 직전 완료 봉 목표 비중 0%; 다음 봉 시가 가정 |
| v2 | breakout_8 AND reversion_12 | 10000.00 | 0.00 | 대기 /  / 새 신호 대기 |
| v2 | breakout_8 + reversion_12 | 9387.04 | -612.96 | sell / filled / 직전 완료 봉 목표 비중 50%; 다음 봉 시가 가정 |
| v2 | breakout_8 AND volume_26 | 9891.45 | -108.55 | sell / filled / 직전 완료 봉 목표 비중 0%; 다음 봉 시가 가정 |
| v2 | breakout_8 + volume_26 | 9258.08 | -741.92 | sell / filled / 직전 완료 봉 목표 비중 0%; 다음 봉 시가 가정 |
| v2 | reversion_12 AND volume_26 | 9547.64 | -452.36 | 중단: 손실 한도 / sell / filled / 직전 완료 봉 목표 비중 0%; 다음 봉 시가 가정 |
| v2 | reversion_12 + volume_26 | 9203.47 | -796.53 | sell / filled / 직전 완료 봉 목표 비중 50%; 다음 봉 시가 가정 |
| v2 | ema_12_26 | 9587.04 | -412.96 | sell / filled / EMA12 > EMA26; 조건 미충족; EMA12=718.879, EMA26=719.016; 직전 완료 봉 목표를 다음 봉 시가에 모의 적용 |
| v2 | macd_12_26_9 | 9738.24 | -261.76 | sell / filled / MACD > 신호선 그리고 MACD > 0; 조건 미충족; MACD=0.0195537, signal9=0.0263977; 직전 완료 봉 목표를 다음 봉 시가에 모의 적용 |
| v2 | rsi_14_recovery | 9801.56 | -198.44 | sell / filled / 직전 RSI14 < 30, 현재 RSI14 >= 30 (한 봉 목표); 조건 미충족; RSI14=50.2063, previous_RSI14=44.1729; 직전 완료 봉 목표를 다음 봉 시가에 모의 적용 |
| v2 | bollinger_20_reentry | 9872.68 | -127.32 | sell / filled / 직전 종가 < 직전 하단밴드, 현재 하단밴드 <= 종가 <= SMA20 (한 봉 목표); 조건 미충족; close=718.66, lower20=714.386, SMA20=719.409, previous_lower20=714.271; 직전 완료 봉 목표를 다음 봉 시가에 모의 적용 |
| v2 | donchian_20 | 9947.13 | -52.87 | sell / filled / 종가 > 현재 봉을 제외한 직전 20봉 최고가; 조건 미충족; close=724.13, prior_high20=724.151; 직전 완료 봉 목표를 다음 봉 시가에 모의 적용 |
| v2 | atr_14_breakout | 9941.83 | -58.17 | sell / filled / 종가 > 직전 종가 + 직전 ATR14 그리고 종가 > EMA26; 조건 미충족; close=721.52, threshold=724.646, prior_ATR14=2.53578, EMA26=719.016; 직전 완료 봉 목표를 다음 봉 시가에 모의 적용 |
| v2 | session_vwap | 9746.27 | -253.73 | sell / filled / 종가 > 뉴욕 거래일별 누적 전형가격 VWAP; 조건 미충족; close=719.05, session_VWAP=719.729, session_volume=3.45027e+08; 직전 완료 봉 목표를 다음 봉 시가에 모의 적용 |
| v2 | obv_20 | 9714.29 | -285.71 | sell / filled / OBV > OBV의 SMA20 그리고 종가 > EMA26; 조건 미충족; OBV=2.65835e+08, OBV_SMA20=2.15387e+08, close=718.98, EMA26=719.158; 직전 완료 봉 목표를 다음 봉 시가에 모의 적용 |
| v2 | stochastic_14_3_recovery | 9694.13 | -305.87 | 중단: 손실 한도 / sell / filled / 직전 %K14 < 20에서 %K14가 %D3 상향 돌파 (한 봉 목표); 조건 미충족; K14=10.576, D3=8.00581, previous_K14=7.39787, previous_D3=7.27486; 직전 완료 봉 목표를 다음 봉 시가에 모의 적용 |
| v2 | mfi_14_recovery | 9809.63 | -190.37 | sell / filled / 직전 MFI14 < 20, 현재 MFI14 >= 20 (한 봉 목표); 조건 미충족; MFI14=30.3876, previous_MFI14=31.1747; 직전 완료 봉 목표를 다음 봉 시가에 모의 적용 |
| v2 | adx_14_trend | 9922.56 | -77.44 | sell / filled / Wilder ADX14 >= 25 그리고 +DI14 > -DI14; 조건 미충족; ADX14=23.9831, plus_DI14=26.5781, minus_DI14=24.6326; 직전 완료 봉 목표를 다음 봉 시가에 모의 적용 |
| v2 | aroon_25_trend | 9871.06 | -128.94 | sell / filled / Aroon25 Up > 70 그리고 Down < 30 (동률이면 최신 극값); 조건 미충족; Aroon_up=68, Aroon_down=20; 직전 완료 봉 목표를 다음 봉 시가에 모의 적용 |
| v2 | cci_20_momentum | 9874.26 | -125.74 | sell / filled / CCI20 > 100 (전형가격·평균절대편차); 조건 미충족; CCI20=19.2232; 직전 완료 봉 목표를 다음 봉 시가에 모의 적용 |
| v2 | williams_14_recovery | 9651.03 | -348.97 | sell / filled / 직전 Williams %R14 < -80, 현재 >= -80 (한 봉 목표); 조건 미충족; Williams_R14=-73.8264, previous_R14=-61.7442; 직전 완료 봉 목표를 다음 봉 시가에 모의 적용 |
| v2 | cmf_20_accumulation | 9568.06 | -431.94 | sell / filled / Chaikin Money Flow20 > 0.1; 조건 미충족; CMF20=0.0778093, volume20=4.23002e+08; 직전 완료 봉 목표를 다음 봉 시가에 모의 적용 |
| v2 | chaikin_3_10 | 9721.11 | -278.89 | sell / filled / ADL의 EMA3 - EMA10 > 0 그리고 종가 > EMA26; 조건 미충족; Chaikin3_10=-9825.14, ADL=2.60129e+08, close=719.13, EMA26=719.112; 직전 완료 봉 목표를 다음 봉 시가에 모의 적용 |
| v2 | roc_10_momentum | 9988.50 | -11.50 | sell / filled / 10봉 ROC > 1% 그리고 종가 > EMA26; 조건 미충족; ROC10_percent=0.483561, close=722.477, EMA26=718.78; 직전 완료 봉 목표를 다음 봉 시가에 모의 적용 |
| v2 | trix_15_trend | 9663.30 | -336.70 | sell / filled / 15봉 삼중 EMA의 1봉 변화율 TRIX > 0 그리고 종가 > EMA26; 조건 미충족; TRIX15_percent=0.000611733, close=718.98, EMA26=719.158; 직전 완료 봉 목표를 다음 봉 시가에 모의 적용 |
| v2 | keltner_20_breakout | 9900.20 | -99.80 | sell / filled / 종가 > EMA20 + 2 x Wilder ATR14; 조건 미충족; close=723.31, upper_Keltner=723.407, EMA20=718.722, ATR14=2.34265; 직전 완료 봉 목표를 다음 봉 시가에 모의 적용 |
| v2 | opening_range_30m | 9737.76 | -262.24 | buy / partial / 뉴욕 09:30·09:45 두 완료 봉 최고가를 10:00 이후 종가가 돌파; 조건 충족; close=718.66, opening_high=716.18; 직전 완료 봉 목표를 다음 봉 시가에 모의 적용 |

### 같은 기간의 비용·노출 비교 (사후 연구)

| 전략 | 비용 전 | 비용 후 | 100% 보유 | 같은 평균 노출 보유 | 평균 노출 |
|---|---:|---:|---:|---:|---:|
| cash | 0.00% | 0.00% | -3.90% | -0.00% | 0.00% |
| buy_hold | -3.49% | -3.90% | -3.90% | -3.90% | 100.00% |
| trend_8_26 | -0.22% | -3.92% | -3.90% | -1.70% | 43.34% |
| momentum_26 | -3.62% | -9.12% | -3.90% | -1.52% | 38.90% |
| breakout_8 | -1.93% | -17.10% | -3.90% | -0.71% | 18.02% |
| reversion_12 | -0.43% | -12.95% | -3.90% | -1.19% | 30.29% |
| volume_26 | -1.61% | -14.70% | -3.90% | -0.60% | 15.40% |
| trend_8_26 AND momentum_26 | -0.45% | -4.14% | -3.90% | -1.27% | 32.38% |
| trend_8_26 + momentum_26 | -1.93% | -6.16% | -3.90% | -1.61% | 41.13% |
| trend_8_26 AND breakout_8 | -0.20% | -8.63% | -3.90% | -0.42% | 10.70% |
| trend_8_26 + breakout_8 | -1.07% | -10.19% | -3.90% | -1.20% | 30.69% |
| trend_8_26 AND reversion_12 | -0.22% | -4.73% | -3.90% | -0.26% | 6.53% |
| trend_8_26 + reversion_12 | -0.31% | -7.98% | -3.90% | -1.44% | 36.82% |
| trend_8_26 AND volume_26 | 0.01% | -4.51% | -3.90% | -0.17% | 4.44% |
| trend_8_26 + volume_26 | -0.91% | -9.29% | -3.90% | -1.15% | 29.38% |
| momentum_26 AND breakout_8 | -1.02% | -10.14% | -3.90% | -0.43% | 10.97% |
| momentum_26 + breakout_8 | -2.77% | -13.02% | -3.90% | -1.11% | 28.47% |
| momentum_26 AND reversion_12 | -1.16% | -6.41% | -3.90% | -0.27% | 6.79% |
| momentum_26 + reversion_12 | -2.03% | -10.50% | -3.90% | -1.35% | 34.60% |
| momentum_26 AND volume_26 | -0.72% | -4.40% | -3.90% | -0.12% | 3.13% |
| momentum_26 + volume_26 | -2.61% | -11.59% | -3.90% | -1.06% | 27.16% |
| breakout_8 AND reversion_12 | 0.00% | 0.00% | -3.90% | -0.00% | 0.00% |
| breakout_8 + reversion_12 | -1.17% | -14.16% | -3.90% | -0.95% | 24.16% |
| breakout_8 AND volume_26 | 0.09% | -1.99% | -3.90% | -0.06% | 1.57% |
| breakout_8 + volume_26 | -1.76% | -14.49% | -3.90% | -0.66% | 16.72% |
| reversion_12 AND volume_26 | -1.31% | -8.11% | -3.90% | -0.33% | 8.36% |
| reversion_12 + volume_26 | -1.01% | -13.29% | -3.90% | -0.90% | 22.85% |
| ema_12_26 | -2.04% | -4.87% | -3.90% | -1.60% | 40.99% |
| macd_12_26_9 | 0.06% | -4.46% | -3.90% | -0.89% | 22.72% |
| rsi_14_recovery | -0.47% | -5.76% | -3.90% | -0.13% | 3.39% |
| bollinger_20_reentry | -0.08% | -6.18% | -3.90% | -0.15% | 3.92% |
| donchian_20 | 0.40% | -4.54% | -3.90% | -0.20% | 5.22% |
| atr_14_breakout | 0.27% | -3.45% | -3.90% | -0.10% | 2.61% |
| session_vwap | -0.32% | -11.75% | -3.90% | -1.80% | 45.95% |
| obv_20 | -1.61% | -10.29% | -3.90% | -1.09% | 27.94% |
| stochastic_14_3_recovery | -0.36% | -12.16% | -3.90% | -0.31% | 7.83% |
| mfi_14_recovery | -1.23% | -3.69% | -3.90% | -0.06% | 1.57% |
| adx_14_trend | -0.11% | -3.00% | -3.90% | -0.84% | 21.41% |
| aroon_25_trend | 1.27% | -2.07% | -3.90% | -0.71% | 18.02% |
| cci_20_momentum | -0.69% | -5.96% | -3.90% | -0.61% | 15.67% |
| williams_14_recovery | -0.68% | -11.32% | -3.90% | -0.28% | 7.05% |
| cmf_20_accumulation | -1.98% | -9.49% | -3.90% | -1.30% | 33.16% |
| chaikin_3_10 | -2.82% | -10.65% | -3.90% | -1.35% | 34.46% |
| roc_10_momentum | 0.02% | -1.23% | -3.90% | -0.15% | 3.92% |
| trix_15_trend | -0.41% | -3.70% | -3.90% | -1.33% | 33.94% |
| keltner_20_breakout | -0.98% | -5.45% | -3.90% | -0.28% | 7.05% |
| opening_range_30m | -1.24% | -8.04% | -3.90% | -1.21% | 30.81% |

동일 구간·초기 자금, 종료 시 청산 비용 포함. 노출 맞춤은 사후 설명용이며 v2 실제 계좌 성과가 아닙니다.
[낙폭 분해·비용 영향·전체 구간](QQQ/comparison.json)

[v1 전체 기록](QQQ/accounts.json) · [v2 전체 기록](QQQ/accounts-v2.json)

## IWM 계좌

| 모델 | 전략 | 평가액 USD | 손익 USD | 최근 매매·이유 |
|---|---|---:|---:|---|
| v1 | cash | 10000.00 | 0.00 | 대기 /  / 새 신호 대기 |
| v1 | buy_hold | 9996.51 | -3.49 | buy /  / buy_hold: prior completed bar target 100%; next bar open simulation |
| v1 | trend_8_26 | 9801.90 | -198.10 | buy /  / trend_8_26: prior completed bar target 100%; next bar open simulation |
| v1 | momentum_26 | 9972.79 | -27.21 | buy /  / momentum_26: prior completed bar target 100%; next bar open simulation |
| v1 | breakout_8 | 9673.06 | -326.94 | sell /  / breakout_8: prior completed bar target 0%; next bar open simulation |
| v1 | reversion_12 | 9786.62 | -213.38 | sell /  / reversion_12: prior completed bar target 0%; next bar open simulation |
| v1 | volume_26 | 9923.29 | -76.71 | sell /  / volume_26: prior completed bar target 0%; next bar open simulation |
| v1 | trend_8_26 AND momentum_26 | 9817.83 | -182.17 | buy /  / trend_8_26 AND momentum_26: prior completed bar target 100%; next bar open simulation |
| v1 | trend_8_26 + momentum_26 | 9887.04 | -112.96 | buy /  / trend_8_26 + momentum_26: prior completed bar target 100%; next bar open simulation |
| v1 | trend_8_26 AND breakout_8 | 9762.76 | -237.24 | sell /  / trend_8_26 AND breakout_8: prior completed bar target 0%; next bar open simulation |
| v1 | trend_8_26 + breakout_8 | 9737.43 | -262.57 | sell /  / trend_8_26 + breakout_8: prior completed bar target 50%; next bar open simulation |
| v1 | trend_8_26 AND reversion_12 | 9827.31 | -172.69 | sell /  / trend_8_26 AND reversion_12: prior completed bar target 0%; next bar open simulation |
| v1 | trend_8_26 + reversion_12 | 9794.12 | -205.88 | sell /  / trend_8_26 + reversion_12: prior completed bar target 50%; next bar open simulation |
| v1 | trend_8_26 AND volume_26 | 9935.98 | -64.02 | sell /  / trend_8_26 AND volume_26: prior completed bar target 0%; next bar open simulation |
| v1 | trend_8_26 + volume_26 | 9882.02 | -117.98 | sell /  / trend_8_26 + volume_26: prior completed bar target 50%; next bar open simulation |
| v1 | momentum_26 AND breakout_8 | 9812.09 | -187.91 | sell /  / momentum_26 AND breakout_8: prior completed bar target 0%; next bar open simulation |
| v1 | momentum_26 + breakout_8 | 9841.58 | -158.42 | sell /  / momentum_26 + breakout_8: prior completed bar target 50%; next bar open simulation |
| v1 | momentum_26 AND reversion_12 | 9924.34 | -75.66 | sell /  / momentum_26 AND reversion_12: prior completed bar target 0%; next bar open simulation |
| v1 | momentum_26 + reversion_12 | 9898.92 | -101.08 | sell /  / momentum_26 + reversion_12: prior completed bar target 50%; next bar open simulation |
| v1 | momentum_26 AND volume_26 | 10062.05 | 62.05 | sell /  / momentum_26 AND volume_26: prior completed bar target 0%; next bar open simulation |
| v1 | momentum_26 + volume_26 | 9947.87 | -52.13 | sell /  / momentum_26 + volume_26: prior completed bar target 50%; next bar open simulation |
| v1 | breakout_8 AND reversion_12 | 10000.00 | 0.00 | 대기 /  / 새 신호 대기 |
| v1 | breakout_8 + reversion_12 | 9729.56 | -270.44 | sell /  / breakout_8 + reversion_12: prior completed bar target 0%; next bar open simulation |
| v1 | breakout_8 AND volume_26 | 9967.28 | -32.72 | sell /  / breakout_8 AND volume_26: prior completed bar target 0%; next bar open simulation |
| v1 | breakout_8 + volume_26 | 9816.95 | -183.05 | sell /  / breakout_8 + volume_26: prior completed bar target 0%; next bar open simulation |
| v1 | reversion_12 AND volume_26 | 9935.98 | -64.02 | sell /  / reversion_12 AND volume_26: prior completed bar target 0%; next bar open simulation |
| v1 | reversion_12 + volume_26 | 9874.40 | -125.60 | sell /  / reversion_12 + volume_26: prior completed bar target 0%; next bar open simulation |
| v1 | ema_12_26 | 9867.04 | -132.96 | buy /  / EMA12 > EMA26; 조건 충족; EMA12=271.545, EMA26=271.529 |
| v1 | macd_12_26_9 | 9906.42 | -93.58 | sell /  / MACD > 신호선 그리고 MACD > 0; 조건 미충족; MACD=0.978353, signal9=1.01104 |
| v1 | rsi_14_recovery | 9786.95 | -213.05 | sell /  / 직전 RSI14 < 30, 현재 RSI14 >= 30 (한 봉 목표); 조건 미충족; RSI14=46.986, previous_RSI14=37.1649 |
| v1 | bollinger_20_reentry | 9924.03 | -75.97 | sell /  / 직전 종가 < 직전 하단밴드, 현재 하단밴드 <= 종가 <= SMA20 (한 봉 목표); 조건 미충족; close=271.19, lower20=270.018, SMA20=273.224, previous_lower20=270.283 |
| v1 | donchian_20 | 9835.91 | -164.09 | sell /  / 종가 > 현재 봉을 제외한 직전 20봉 최고가; 조건 미충족; close=275.785, prior_high20=276.875 |
| v1 | atr_14_breakout | 9883.94 | -116.06 | sell /  / 종가 > 직전 종가 + 직전 ATR14 그리고 종가 > EMA26; 조건 미충족; close=276.33, threshold=276.592, prior_ATR14=0.747363, EMA26=272.499 |
| v1 | session_vwap | 9870.02 | -129.98 | buy /  / 종가 > 뉴욕 거래일별 누적 전형가격 VWAP; 조건 충족; close=272.6, session_VWAP=272.22, session_volume=3.20722e+06 |
| v1 | obv_20 | 9861.40 | -138.60 | buy /  / OBV > OBV의 SMA20 그리고 종가 > EMA26; 조건 충족; OBV=-2.88653e+07, OBV_SMA20=-3.02185e+07, close=272.6, EMA26=271.529 |
| v1 | stochastic_14_3_recovery | 9665.87 | -334.13 | sell /  / 직전 %K14 < 20에서 %K14가 %D3 상향 돌파 (한 봉 목표); 조건 미충족; K14=72.727, D3=41.2922, previous_K14=34.0903, previous_D3=23.8263 |
| v1 | mfi_14_recovery | 9934.22 | -65.78 | sell /  / 직전 MFI14 < 20, 현재 MFI14 >= 20 (한 봉 목표); 조건 미충족; MFI14=34.131, previous_MFI14=22.0435 |
| v1 | adx_14_trend | 9792.55 | -207.45 | buy /  / Wilder ADX14 >= 25 그리고 +DI14 > -DI14; 조건 충족; ADX14=26.5262, plus_DI14=49.1478, minus_DI14=9.69634 |
| v1 | aroon_25_trend | 9784.20 | -215.80 | sell /  / Aroon25 Up > 70 그리고 Down < 30 (동률이면 최신 극값); 조건 미충족; Aroon_up=68, Aroon_down=20 |
| v1 | cci_20_momentum | 9955.08 | -44.92 | sell /  / CCI20 > 100 (전형가격·평균절대편차); 조건 미충족; CCI20=86.224 |
| v1 | williams_14_recovery | 9833.31 | -166.69 | sell /  / 직전 Williams %R14 < -80, 현재 >= -80 (한 봉 목표); 조건 미충족; Williams_R14=-27.273, previous_R14=-65.9097 |
| v1 | cmf_20_accumulation | 9813.96 | -186.04 | buy /  / Chaikin Money Flow20 > 0.1; 조건 충족; CMF20=0.208851, volume20=1.40263e+07 |
| v1 | chaikin_3_10 | 9862.29 | -137.71 | buy /  / ADL의 EMA3 - EMA10 > 0 그리고 종가 > EMA26; 조건 충족; Chaikin3_10=878293, ADL=-4.92877e+07, close=272.6, EMA26=271.529 |
| v1 | roc_10_momentum | 9996.39 | -3.61 | sell /  / 10봉 ROC > 1% 그리고 종가 > EMA26; 조건 미충족; ROC10_percent=0.995963, close=275.315, EMA26=273.754 |
| v1 | trix_15_trend | 9948.24 | -51.76 | buy /  / 15봉 삼중 EMA의 1봉 변화율 TRIX > 0 그리고 종가 > EMA26; 조건 충족; TRIX15_percent=0.00296855, close=273.97, EMA26=271.9 |
| v1 | keltner_20_breakout | 9933.72 | -66.28 | sell /  / 종가 > EMA20 + 2 x Wilder ATR14; 조건 미충족; close=275.315, upper_Keltner=275.695, EMA20=274.153, ATR14=0.771306 |
| v1 | opening_range_30m | 9952.63 | -47.37 | buy /  / 뉴욕 09:30·09:45 두 완료 봉 최고가를 10:00 이후 종가가 돌파; 조건 충족; close=275.845, opening_high=274.33 |
| v2 | cash | 10000.00 | 0.00 | 대기 /  / 새 신호 대기 |
| v2 | buy_hold | 9889.62 | -110.38 | buy / partial / 직전 완료 봉 목표 비중 100%; 다음 봉 시가 가정 |
| v2 | trend_8_26 | 9671.02 | -328.98 | buy / partial / 직전 완료 봉 목표 비중 100%; 다음 봉 시가 가정 |
| v2 | momentum_26 | 9840.64 | -159.36 | buy / partial / 직전 완료 봉 목표 비중 100%; 다음 봉 시가 가정 |
| v2 | breakout_8 | 9288.40 | -711.60 | sell / filled / 직전 완료 봉 목표 비중 0%; 다음 봉 시가 가정 |
| v2 | reversion_12 | 9325.80 | -674.20 | sell / filled / 직전 완료 봉 목표 비중 0%; 다음 봉 시가 가정 |
| v2 | volume_26 | 9434.73 | -565.27 | sell / filled / 직전 완료 봉 목표 비중 0%; 다음 봉 시가 가정 |
| v2 | trend_8_26 AND momentum_26 | 9835.12 | -164.88 | buy / partial / 직전 완료 봉 목표 비중 100%; 다음 봉 시가 가정 |
| v2 | trend_8_26 + momentum_26 | 9776.16 | -223.84 | buy / partial / 직전 완료 봉 목표 비중 100%; 다음 봉 시가 가정 |
| v2 | trend_8_26 AND breakout_8 | 9667.89 | -332.11 | sell / filled / 직전 완료 봉 목표 비중 0%; 다음 봉 시가 가정 |
| v2 | trend_8_26 + breakout_8 | 9498.00 | -502.00 | sell / filled / 직전 완료 봉 목표 비중 50%; 다음 봉 시가 가정 |
| v2 | trend_8_26 AND reversion_12 | 9705.35 | -294.65 | sell / filled / 직전 완료 봉 목표 비중 0%; 다음 봉 시가 가정 |
| v2 | trend_8_26 + reversion_12 | 9496.54 | -503.46 | sell / filled / 직전 완료 봉 목표 비중 50%; 다음 봉 시가 가정 |
| v2 | trend_8_26 AND volume_26 | 9797.73 | -202.27 | sell / filled / 직전 완료 봉 목표 비중 0%; 다음 봉 시가 가정 |
| v2 | trend_8_26 + volume_26 | 9592.19 | -407.81 | sell / filled / 직전 완료 봉 목표 비중 50%; 다음 봉 시가 가정 |
| v2 | momentum_26 AND breakout_8 | 9611.04 | -388.96 | sell / filled / 직전 완료 봉 목표 비중 0%; 다음 봉 시가 가정 |
| v2 | momentum_26 + breakout_8 | 9580.79 | -419.21 | sell / filled / 직전 완료 봉 목표 비중 50%; 다음 봉 시가 가정 |
| v2 | momentum_26 AND reversion_12 | 9881.28 | -118.72 | sell / filled / 직전 완료 봉 목표 비중 0%; 다음 봉 시가 가정 |
| v2 | momentum_26 + reversion_12 | 9619.56 | -380.44 | sell / filled / 직전 완료 봉 목표 비중 50%; 다음 봉 시가 가정 |
| v2 | momentum_26 AND volume_26 | 9957.22 | -42.78 | sell / filled / 직전 완료 봉 목표 비중 0%; 다음 봉 시가 가정 |
| v2 | momentum_26 + volume_26 | 9635.18 | -364.82 | sell / filled / 직전 완료 봉 목표 비중 50%; 다음 봉 시가 가정 |
| v2 | breakout_8 AND reversion_12 | 10000.00 | 0.00 | 대기 /  / 새 신호 대기 |
| v2 | breakout_8 + reversion_12 | 9345.74 | -654.26 | sell / filled / 직전 완료 봉 목표 비중 0%; 다음 봉 시가 가정 |
| v2 | breakout_8 AND volume_26 | 9710.25 | -289.75 | sell / filled / 직전 완료 봉 목표 비중 0%; 다음 봉 시가 가정 |
| v2 | breakout_8 + volume_26 | 9400.58 | -599.42 | sell / filled / 직전 완료 봉 목표 비중 0%; 다음 봉 시가 가정 |
| v2 | reversion_12 AND volume_26 | 9676.46 | -323.54 | sell / filled / 직전 완료 봉 목표 비중 0%; 다음 봉 시가 가정 |
| v2 | reversion_12 + volume_26 | 9419.31 | -580.69 | sell / filled / 직전 완료 봉 목표 비중 0%; 다음 봉 시가 가정 |
| v2 | ema_12_26 | 9862.11 | -137.89 | buy / partial / EMA12 > EMA26; 조건 충족; EMA12=271.545, EMA26=271.529; 직전 완료 봉 목표를 다음 봉 시가에 모의 적용 |
| v2 | macd_12_26_9 | 9900.47 | -99.53 | sell / filled / MACD > 신호선 그리고 MACD > 0; 조건 미충족; MACD=0.978353, signal9=1.01104; 직전 완료 봉 목표를 다음 봉 시가에 모의 적용 |
| v2 | rsi_14_recovery | 9779.12 | -220.88 | sell / filled / 직전 RSI14 < 30, 현재 RSI14 >= 30 (한 봉 목표); 조건 미충족; RSI14=46.986, previous_RSI14=37.1649; 직전 완료 봉 목표를 다음 봉 시가에 모의 적용 |
| v2 | bollinger_20_reentry | 9920.06 | -79.94 | sell / filled / 직전 종가 < 직전 하단밴드, 현재 하단밴드 <= 종가 <= SMA20 (한 봉 목표); 조건 미충족; close=271.19, lower20=270.018, SMA20=273.224, previous_lower20=270.283; 직전 완료 봉 목표를 다음 봉 시가에 모의 적용 |
| v2 | donchian_20 | 9830.01 | -169.99 | sell / filled / 종가 > 현재 봉을 제외한 직전 20봉 최고가; 조건 미충족; close=275.785, prior_high20=276.875; 직전 완료 봉 목표를 다음 봉 시가에 모의 적용 |
| v2 | atr_14_breakout | 9876.04 | -123.96 | sell / filled / 종가 > 직전 종가 + 직전 ATR14 그리고 종가 > EMA26; 조건 미충족; close=276.33, threshold=276.592, prior_ATR14=0.747363, EMA26=272.499; 직전 완료 봉 목표를 다음 봉 시가에 모의 적용 |
| v2 | session_vwap | 9861.14 | -138.86 | buy / partial / 종가 > 뉴욕 거래일별 누적 전형가격 VWAP; 조건 충족; close=272.6, session_VWAP=272.22, session_volume=3.20722e+06; 직전 완료 봉 목표를 다음 봉 시가에 모의 적용 |
| v2 | obv_20 | 9852.53 | -147.47 | buy / partial / OBV > OBV의 SMA20 그리고 종가 > EMA26; 조건 충족; OBV=-2.88653e+07, OBV_SMA20=-3.02185e+07, close=272.6, EMA26=271.529; 직전 완료 봉 목표를 다음 봉 시가에 모의 적용 |
| v2 | stochastic_14_3_recovery | 9650.41 | -349.59 | sell / filled / 직전 %K14 < 20에서 %K14가 %D3 상향 돌파 (한 봉 목표); 조건 미충족; K14=72.727, D3=41.2922, previous_K14=34.0903, previous_D3=23.8263; 직전 완료 봉 목표를 다음 봉 시가에 모의 적용 |
| v2 | mfi_14_recovery | 9930.25 | -69.75 | sell / filled / 직전 MFI14 < 20, 현재 MFI14 >= 20 (한 봉 목표); 조건 미충족; MFI14=34.131, previous_MFI14=22.0435; 직전 완료 봉 목표를 다음 봉 시가에 모의 적용 |
| v2 | adx_14_trend | 9787.65 | -212.35 | buy / partial / Wilder ADX14 >= 25 그리고 +DI14 > -DI14; 조건 충족; ADX14=26.5262, plus_DI14=49.1478, minus_DI14=9.69634; 직전 완료 봉 목표를 다음 봉 시가에 모의 적용 |
| v2 | aroon_25_trend | 9776.38 | -223.62 | sell / filled / Aroon25 Up > 70 그리고 Down < 30 (동률이면 최신 극값); 조건 미충족; Aroon_up=68, Aroon_down=20; 직전 완료 봉 목표를 다음 봉 시가에 모의 적용 |
| v2 | cci_20_momentum | 9949.11 | -50.89 | sell / filled / CCI20 > 100 (전형가격·평균절대편차); 조건 미충족; CCI20=86.224; 직전 완료 봉 목표를 다음 봉 시가에 모의 적용 |
| v2 | williams_14_recovery | 9825.45 | -174.55 | sell / filled / 직전 Williams %R14 < -80, 현재 >= -80 (한 봉 목표); 조건 미충족; Williams_R14=-27.273, previous_R14=-65.9097; 직전 완료 봉 목표를 다음 봉 시가에 모의 적용 |
| v2 | cmf_20_accumulation | 9801.21 | -198.79 | buy / partial / Chaikin Money Flow20 > 0.1; 조건 충족; CMF20=0.208851, volume20=1.40263e+07; 직전 완료 봉 목표를 다음 봉 시가에 모의 적용 |
| v2 | chaikin_3_10 | 9853.42 | -146.58 | buy / partial / ADL의 EMA3 - EMA10 > 0 그리고 종가 > EMA26; 조건 충족; Chaikin3_10=878293, ADL=-4.92877e+07, close=272.6, EMA26=271.529; 직전 완료 봉 목표를 다음 봉 시가에 모의 적용 |
| v2 | roc_10_momentum | 9994.39 | -5.61 | sell / filled / 10봉 ROC > 1% 그리고 종가 > EMA26; 조건 미충족; ROC10_percent=0.995963, close=275.315, EMA26=273.754; 직전 완료 봉 목표를 다음 봉 시가에 모의 적용 |
| v2 | trix_15_trend | 9945.26 | -54.74 | buy / partial / 15봉 삼중 EMA의 1봉 변화율 TRIX > 0 그리고 종가 > EMA26; 조건 충족; TRIX15_percent=0.00296855, close=273.97, EMA26=271.9; 직전 완료 봉 목표를 다음 봉 시가에 모의 적용 |
| v2 | keltner_20_breakout | 9929.75 | -70.25 | sell / filled / 종가 > EMA20 + 2 x Wilder ATR14; 조건 미충족; close=275.315, upper_Keltner=275.695, EMA20=274.153, ATR14=0.771306; 직전 완료 봉 목표를 다음 봉 시가에 모의 적용 |
| v2 | opening_range_30m | 9949.65 | -50.35 | buy / partial / 뉴욕 09:30·09:45 두 완료 봉 최고가를 10:00 이후 종가가 돌파; 조건 충족; close=275.845, opening_high=274.33; 직전 완료 봉 목표를 다음 봉 시가에 모의 적용 |

### 같은 기간의 비용·노출 비교 (사후 연구)

| 전략 | 비용 전 | 비용 후 | 100% 보유 | 같은 평균 노출 보유 | 평균 노출 |
|---|---:|---:|---:|---:|---:|
| cash | 0.00% | 0.00% | -1.91% | -0.00% | 0.00% |
| buy_hold | -1.50% | -1.91% | -1.91% | -1.91% | 100.00% |
| trend_8_26 | -0.76% | -4.44% | -1.91% | -0.93% | 48.04% |
| momentum_26 | -0.60% | -5.88% | -1.91% | -0.90% | 46.74% |
| breakout_8 | 0.32% | -13.39% | -1.91% | -0.38% | 19.58% |
| reversion_12 | -2.15% | -13.73% | -1.91% | -0.53% | 27.68% |
| volume_26 | -1.32% | -8.12% | -1.91% | -0.16% | 8.09% |
| trend_8_26 AND momentum_26 | -0.62% | -4.71% | -1.91% | -0.77% | 39.95% |
| trend_8_26 + momentum_26 | -0.67% | -4.76% | -1.91% | -0.91% | 47.39% |
| trend_8_26 AND breakout_8 | 0.11% | -7.96% | -1.91% | -0.24% | 12.27% |
| trend_8_26 + breakout_8 | -0.21% | -8.83% | -1.91% | -0.65% | 33.82% |
| trend_8_26 AND reversion_12 | -0.74% | -4.82% | -1.91% | -0.11% | 5.48% |
| trend_8_26 + reversion_12 | -1.44% | -9.02% | -1.91% | -0.73% | 37.86% |
| trend_8_26 AND volume_26 | -0.68% | -3.16% | -1.91% | -0.04% | 2.09% |
| trend_8_26 + volume_26 | -1.03% | -5.90% | -1.91% | -0.54% | 28.07% |
| momentum_26 AND breakout_8 | 0.56% | -7.93% | -1.91% | -0.23% | 12.01% |
| momentum_26 + breakout_8 | -0.14% | -9.53% | -1.91% | -0.64% | 33.16% |
| momentum_26 AND reversion_12 | 0.03% | -3.68% | -1.91% | -0.07% | 3.66% |
| momentum_26 + reversion_12 | -1.37% | -8.95% | -1.91% | -0.72% | 37.21% |
| momentum_26 AND volume_26 | 0.06% | -2.02% | -1.91% | -0.04% | 1.83% |
| momentum_26 + volume_26 | -0.95% | -6.62% | -1.91% | -0.53% | 27.42% |
| breakout_8 AND reversion_12 | 0.00% | 0.00% | -1.91% | -0.00% | 0.00% |
| breakout_8 + reversion_12 | -0.91% | -13.03% | -1.91% | -0.46% | 23.64% |
| breakout_8 AND volume_26 | -0.54% | -3.42% | -1.91% | -0.04% | 2.09% |
| breakout_8 + volume_26 | -0.50% | -10.42% | -1.91% | -0.27% | 13.84% |
| reversion_12 AND volume_26 | -0.62% | -4.31% | -1.91% | -0.08% | 3.92% |
| reversion_12 + volume_26 | -1.73% | -10.41% | -1.91% | -0.35% | 17.89% |
| ema_12_26 | 0.97% | -1.95% | -1.91% | -0.93% | 48.30% |
| macd_12_26_9 | 2.56% | -0.41% | -1.91% | -0.59% | 30.55% |
| rsi_14_recovery | -0.65% | -5.14% | -1.91% | -0.06% | 2.87% |
| bollinger_20_reentry | -0.24% | -4.35% | -1.91% | -0.05% | 2.61% |
| donchian_20 | -0.29% | -5.59% | -1.91% | -0.12% | 6.27% |
| atr_14_breakout | -0.16% | -6.65% | -1.91% | -0.09% | 4.44% |
| session_vwap | 0.93% | -7.98% | -1.91% | -0.87% | 45.17% |
| obv_20 | 0.95% | -3.61% | -1.91% | -0.81% | 42.04% |
| stochastic_14_3_recovery | -0.44% | -12.96% | -1.91% | -0.16% | 8.36% |
| mfi_14_recovery | 0.36% | -4.17% | -1.91% | -0.06% | 2.87% |
| adx_14_trend | -0.32% | -4.01% | -1.91% | -0.68% | 34.99% |
| aroon_25_trend | -1.30% | -5.76% | -1.91% | -0.42% | 21.93% |
| cci_20_momentum | -1.11% | -7.54% | -1.91% | -0.36% | 18.80% |
| williams_14_recovery | -0.09% | -9.29% | -1.91% | -0.12% | 6.01% |
| cmf_20_accumulation | -0.43% | -7.29% | -1.91% | -0.46% | 24.02% |
| chaikin_3_10 | -0.88% | -7.32% | -1.91% | -0.70% | 36.03% |
| roc_10_momentum | -0.27% | -1.93% | -1.91% | -0.11% | 5.48% |
| trix_15_trend | 1.08% | -2.26% | -1.91% | -0.71% | 36.81% |
| keltner_20_breakout | -0.20% | -3.49% | -1.91% | -0.14% | 7.31% |
| opening_range_30m | 2.62% | -1.60% | -1.91% | -0.51% | 26.63% |

동일 구간·초기 자금, 종료 시 청산 비용 포함. 노출 맞춤은 사후 설명용이며 v2 실제 계좌 성과가 아닙니다.
[낙폭 분해·비용 영향·전체 구간](IWM/comparison.json)

[v1 전체 기록](IWM/accounts.json) · [v2 전체 기록](IWM/accounts-v2.json)

## DIA 계좌

| 모델 | 전략 | 평가액 USD | 손익 USD | 최근 매매·이유 |
|---|---|---:|---:|---|
| v1 | cash | 10000.00 | 0.00 | 대기 /  / 새 신호 대기 |
| v1 | buy_hold | 9995.11 | -4.89 | buy /  / buy_hold: prior completed bar target 100%; next bar open simulation |
| v1 | trend_8_26 | 9953.48 | -46.52 | buy /  / trend_8_26: prior completed bar target 100%; next bar open simulation |
| v1 | momentum_26 | 9849.74 | -150.26 | buy /  / momentum_26: prior completed bar target 100%; next bar open simulation |
| v1 | breakout_8 | 9655.94 | -344.06 | sell /  / breakout_8: prior completed bar target 0%; next bar open simulation |
| v1 | reversion_12 | 9863.03 | -136.97 | sell /  / reversion_12: prior completed bar target 0%; next bar open simulation |
| v1 | volume_26 | 9939.83 | -60.17 | sell /  / volume_26: prior completed bar target 0%; next bar open simulation |
| v1 | trend_8_26 AND momentum_26 | 9849.74 | -150.26 | buy /  / trend_8_26 AND momentum_26: prior completed bar target 100%; next bar open simulation |
| v1 | trend_8_26 + momentum_26 | 9901.56 | -98.44 | buy /  / trend_8_26 + momentum_26: prior completed bar target 100%; next bar open simulation |
| v1 | trend_8_26 AND breakout_8 | 9787.57 | -212.43 | sell /  / trend_8_26 AND breakout_8: prior completed bar target 0%; next bar open simulation |
| v1 | trend_8_26 + breakout_8 | 9823.24 | -176.76 | sell /  / trend_8_26 + breakout_8: prior completed bar target 50%; next bar open simulation |
| v1 | trend_8_26 AND reversion_12 | 9906.37 | -93.63 | sell /  / trend_8_26 AND reversion_12: prior completed bar target 0%; next bar open simulation |
| v1 | trend_8_26 + reversion_12 | 9908.01 | -91.99 | sell /  / trend_8_26 + reversion_12: prior completed bar target 50%; next bar open simulation |
| v1 | trend_8_26 AND volume_26 | 9974.09 | -25.91 | sell /  / trend_8_26 AND volume_26: prior completed bar target 0%; next bar open simulation |
| v1 | trend_8_26 + volume_26 | 9946.52 | -53.48 | sell /  / trend_8_26 + volume_26: prior completed bar target 50%; next bar open simulation |
| v1 | momentum_26 AND breakout_8 | 9787.57 | -212.43 | sell /  / momentum_26 AND breakout_8: prior completed bar target 0%; next bar open simulation |
| v1 | momentum_26 + breakout_8 | 9752.35 | -247.65 | sell /  / momentum_26 + breakout_8: prior completed bar target 50%; next bar open simulation |
| v1 | momentum_26 AND reversion_12 | 9906.39 | -93.61 | sell /  / momentum_26 AND reversion_12: prior completed bar target 0%; next bar open simulation |
| v1 | momentum_26 + reversion_12 | 9895.72 | -104.28 | sell /  / momentum_26 + reversion_12: prior completed bar target 50%; next bar open simulation |
| v1 | momentum_26 AND volume_26 | 9929.52 | -70.48 | sell /  / momentum_26 AND volume_26: prior completed bar target 0%; next bar open simulation |
| v1 | momentum_26 + volume_26 | 9914.41 | -85.59 | sell /  / momentum_26 + volume_26: prior completed bar target 50%; next bar open simulation |
| v1 | breakout_8 AND reversion_12 | 10000.00 | 0.00 | 대기 /  / 새 신호 대기 |
| v1 | breakout_8 + reversion_12 | 9778.33 | -221.67 | sell /  / breakout_8 + reversion_12: prior completed bar target 0%; next bar open simulation |
| v1 | breakout_8 AND volume_26 | 9986.25 | -13.75 | sell /  / breakout_8 AND volume_26: prior completed bar target 0%; next bar open simulation |
| v1 | breakout_8 + volume_26 | 9836.08 | -163.92 | sell /  / breakout_8 + volume_26: prior completed bar target 0%; next bar open simulation |
| v1 | reversion_12 AND volume_26 | 9970.42 | -29.58 | sell /  / reversion_12 AND volume_26: prior completed bar target 0%; next bar open simulation |
| v1 | reversion_12 + volume_26 | 9921.10 | -78.90 | sell /  / reversion_12 + volume_26: prior completed bar target 0%; next bar open simulation |
| v1 | ema_12_26 | 9849.97 | -150.03 | buy /  / EMA12 > EMA26; 조건 충족; EMA12=519.74, EMA26=519.585 |
| v1 | macd_12_26_9 | 9895.59 | -104.41 | sell /  / MACD > 신호선 그리고 MACD > 0; 조건 미충족; MACD=1.09098, signal9=1.12388 |
| v1 | rsi_14_recovery | 10000.00 | 0.00 | 대기 /  / 새 신호 대기 |
| v1 | bollinger_20_reentry | 9978.51 | -21.49 | sell /  / 직전 종가 < 직전 하단밴드, 현재 하단밴드 <= 종가 <= SMA20 (한 봉 목표); 조건 미충족; close=519.823, lower20=518.355, SMA20=521.612, previous_lower20=518.548 |
| v1 | donchian_20 | 9822.00 | -178.00 | sell /  / 종가 > 현재 봉을 제외한 직전 20봉 최고가; 조건 미충족; close=523.68, prior_high20=526.17 |
| v1 | atr_14_breakout | 9885.70 | -114.30 | sell /  / 종가 > 직전 종가 + 직전 ATR14 그리고 종가 > EMA26; 조건 미충족; close=525.49, threshold=525.841, prior_ATR14=0.980592, EMA26=520.815 |
| v1 | session_vwap | 9860.05 | -139.95 | buy /  / 종가 > 뉴욕 거래일별 누적 전형가격 VWAP; 조건 충족; close=523.58, session_VWAP=523.505, session_volume=2.75313e+06 |
| v1 | obv_20 | 9829.77 | -170.23 | sell /  / OBV > OBV의 SMA20 그리고 종가 > EMA26; 조건 미충족; OBV=-9.39558e+06, OBV_SMA20=-9.334e+06, close=523.33, EMA26=523.033 |
| v1 | stochastic_14_3_recovery | 9781.80 | -218.20 | sell /  / 직전 %K14 < 20에서 %K14가 %D3 상향 돌파 (한 봉 목표); 조건 미충족; K14=29.5271, D3=23.7537, previous_K14=30.7093, previous_D3=24.065 |
| v1 | mfi_14_recovery | 9902.01 | -97.99 | sell /  / 직전 MFI14 < 20, 현재 MFI14 >= 20 (한 봉 목표); 조건 미충족; MFI14=29.4378, previous_MFI14=21.6288 |
| v1 | adx_14_trend | 9811.65 | -188.35 | sell /  / Wilder ADX14 >= 25 그리고 +DI14 > -DI14; 조건 미충족; ADX14=24.7281, plus_DI14=33.8838, minus_DI14=22.7145 |
| v1 | aroon_25_trend | 9928.84 | -71.16 | sell /  / Aroon25 Up > 70 그리고 Down < 30 (동률이면 최신 극값); 조건 미충족; Aroon_up=100, Aroon_down=80 |
| v1 | cci_20_momentum | 9915.48 | -84.52 | sell /  / CCI20 > 100 (전형가격·평균절대편차); 조건 미충족; CCI20=87.8356 |
| v1 | williams_14_recovery | 9814.96 | -185.04 | sell /  / 직전 Williams %R14 < -80, 현재 >= -80 (한 봉 목표); 조건 미충족; Williams_R14=-70.4729, previous_R14=-69.2907 |
| v1 | cmf_20_accumulation | 9746.54 | -253.46 | sell /  / Chaikin Money Flow20 > 0.1; 조건 미충족; CMF20=0.0647408, volume20=1.77993e+06 |
| v1 | chaikin_3_10 | 9836.93 | -163.07 | sell /  / ADL의 EMA3 - EMA10 > 0 그리고 종가 > EMA26; 조건 미충족; Chaikin3_10=-1094.33, ADL=-1.60023e+07, close=523.58, EMA26=523.074 |
| v1 | roc_10_momentum | 9939.01 | -60.99 | sell /  / 10봉 ROC > 1% 그리고 종가 > EMA26; 조건 미충족; ROC10_percent=0.771645, close=523.68, EMA26=521.367 |
| v1 | trix_15_trend | 9951.39 | -48.61 | buy /  / 15봉 삼중 EMA의 1봉 변화율 TRIX > 0 그리고 종가 > EMA26; 조건 충족; TRIX15_percent=0.000473967, close=521.46, EMA26=519.585 |
| v1 | keltner_20_breakout | 9944.49 | -55.51 | sell /  / 종가 > EMA20 + 2 x Wilder ATR14; 조건 미충족; close=523.68, upper_Keltner=523.985, EMA20=521.785, ATR14=1.10038 |
| v1 | opening_range_30m | 9744.73 | -255.27 | buy /  / 뉴욕 09:30·09:45 두 완료 봉 최고가를 10:00 이후 종가가 돌파; 조건 충족; close=523.58, opening_high=523.47 |
| v2 | cash | 10000.00 | 0.00 | 대기 /  / 새 신호 대기 |
| v2 | buy_hold | 10118.93 | 118.93 | buy / partial / 직전 완료 봉 목표 비중 100%; 다음 봉 시가 가정 |
| v2 | trend_8_26 | 9887.02 | -112.98 | buy / partial / 직전 완료 봉 목표 비중 100%; 다음 봉 시가 가정 |
| v2 | momentum_26 | 9887.59 | -112.41 | buy / partial / 직전 완료 봉 목표 비중 100%; 다음 봉 시가 가정 |
| v2 | breakout_8 | 9183.12 | -816.88 | sell / filled / 직전 완료 봉 목표 비중 0%; 다음 봉 시가 가정 |
| v2 | reversion_12 | 9557.55 | -442.45 | sell / filled / 직전 완료 봉 목표 비중 0%; 다음 봉 시가 가정 |
| v2 | volume_26 | 9652.01 | -347.99 | sell / filled / 직전 완료 봉 목표 비중 0%; 다음 봉 시가 가정 |
| v2 | trend_8_26 AND momentum_26 | 9883.00 | -117.00 | buy / partial / 직전 완료 봉 목표 비중 100%; 다음 봉 시가 가정 |
| v2 | trend_8_26 + momentum_26 | 9887.47 | -112.53 | buy / partial / 직전 완료 봉 목표 비중 100%; 다음 봉 시가 가정 |
| v2 | trend_8_26 AND breakout_8 | 9471.49 | -528.51 | sell / filled / 직전 완료 봉 목표 비중 0%; 다음 봉 시가 가정 |
| v2 | trend_8_26 + breakout_8 | 9548.70 | -451.30 | sell / filled / 직전 완료 봉 목표 비중 50%; 다음 봉 시가 가정 |
| v2 | trend_8_26 AND reversion_12 | 9713.09 | -286.91 | sell / filled / 직전 완료 봉 목표 비중 0%; 다음 봉 시가 가정 |
| v2 | trend_8_26 + reversion_12 | 9720.49 | -279.51 | sell / filled / 직전 완료 봉 목표 비중 50%; 다음 봉 시가 가정 |
| v2 | trend_8_26 AND volume_26 | 9827.44 | -172.56 | sell / filled / 직전 완료 봉 목표 비중 0%; 다음 봉 시가 가정 |
| v2 | trend_8_26 + volume_26 | 9789.16 | -210.84 | sell / filled / 직전 완료 봉 목표 비중 50%; 다음 봉 시가 가정 |
| v2 | momentum_26 AND breakout_8 | 9460.71 | -539.29 | sell / filled / 직전 완료 봉 목표 비중 0%; 다음 봉 시가 가정 |
| v2 | momentum_26 + breakout_8 | 9528.97 | -471.03 | sell / filled / 직전 완료 봉 목표 비중 50%; 다음 봉 시가 가정 |
| v2 | momentum_26 AND reversion_12 | 9858.83 | -141.17 | sell / filled / 직전 완료 봉 목표 비중 0%; 다음 봉 시가 가정 |
| v2 | momentum_26 + reversion_12 | 9761.72 | -238.28 | sell / filled / 직전 완료 봉 목표 비중 50%; 다음 봉 시가 가정 |
| v2 | momentum_26 AND volume_26 | 9716.58 | -283.42 | sell / filled / 직전 완료 봉 목표 비중 0%; 다음 봉 시가 가정 |
| v2 | momentum_26 + volume_26 | 9830.82 | -169.18 | sell / filled / 직전 완료 봉 목표 비중 50%; 다음 봉 시가 가정 |
| v2 | breakout_8 AND reversion_12 | 10000.00 | 0.00 | 대기 /  / 새 신호 대기 |
| v2 | breakout_8 + reversion_12 | 9387.58 | -612.42 | sell / filled / 직전 완료 봉 목표 비중 0%; 다음 봉 시가 가정 |
| v2 | breakout_8 AND volume_26 | 9781.13 | -218.87 | sell / filled / 직전 완료 봉 목표 비중 0%; 다음 봉 시가 가정 |
| v2 | breakout_8 + volume_26 | 9454.07 | -545.93 | sell / filled / 직전 완료 봉 목표 비중 0%; 다음 봉 시가 가정 |
| v2 | reversion_12 AND volume_26 | 9966.44 | -33.56 | sell / filled / 직전 완료 봉 목표 비중 0%; 다음 봉 시가 가정 |
| v2 | reversion_12 + volume_26 | 9624.50 | -375.50 | sell / filled / 직전 완료 봉 목표 비중 0%; 다음 봉 시가 가정 |
| v2 | ema_12_26 | 9845.05 | -154.95 | buy / partial / EMA12 > EMA26; 조건 충족; EMA12=519.74, EMA26=519.585; 직전 완료 봉 목표를 다음 봉 시가에 모의 적용 |
| v2 | macd_12_26_9 | 9889.66 | -110.34 | sell / filled / MACD > 신호선 그리고 MACD > 0; 조건 미충족; MACD=1.09098, signal9=1.12388; 직전 완료 봉 목표를 다음 봉 시가에 모의 적용 |
| v2 | rsi_14_recovery | 10000.00 | 0.00 | 대기 /  / 새 신호 대기 |
| v2 | bollinger_20_reentry | 9976.52 | -23.48 | sell / filled / 직전 종가 < 직전 하단밴드, 현재 하단밴드 <= 종가 <= SMA20 (한 봉 목표); 조건 미충족; close=519.823, lower20=518.355, SMA20=521.612, previous_lower20=518.548; 직전 완료 봉 목표를 다음 봉 시가에 모의 적용 |
| v2 | donchian_20 | 9814.14 | -185.86 | sell / filled / 종가 > 현재 봉을 제외한 직전 20봉 최고가; 조건 미충족; close=523.68, prior_high20=526.17; 직전 완료 봉 목표를 다음 봉 시가에 모의 적용 |
| v2 | atr_14_breakout | 9877.79 | -122.21 | sell / filled / 종가 > 직전 종가 + 직전 ATR14 그리고 종가 > EMA26; 조건 미충족; close=525.49, threshold=525.841, prior_ATR14=0.980592, EMA26=520.815; 직전 완료 봉 목표를 다음 봉 시가에 모의 적용 |
| v2 | session_vwap | 9851.18 | -148.82 | buy / partial / 종가 > 뉴욕 거래일별 누적 전형가격 VWAP; 조건 충족; close=523.58, session_VWAP=523.505, session_volume=2.75313e+06; 직전 완료 봉 목표를 다음 봉 시가에 모의 적용 |
| v2 | obv_20 | 9821.91 | -178.09 | sell / filled / OBV > OBV의 SMA20 그리고 종가 > EMA26; 조건 미충족; OBV=-9.39558e+06, OBV_SMA20=-9.334e+06, close=523.33, EMA26=523.033; 직전 완료 봉 목표를 다음 봉 시가에 모의 적용 |
| v2 | stochastic_14_3_recovery | 9770.07 | -229.93 | sell / filled / 직전 %K14 < 20에서 %K14가 %D3 상향 돌파 (한 봉 목표); 조건 미충족; K14=29.5271, D3=23.7537, previous_K14=30.7093, previous_D3=24.065; 직전 완료 봉 목표를 다음 봉 시가에 모의 적용 |
| v2 | mfi_14_recovery | 9896.07 | -103.93 | sell / filled / 직전 MFI14 < 20, 현재 MFI14 >= 20 (한 봉 목표); 조건 미충족; MFI14=29.4378, previous_MFI14=21.6288; 직전 완료 봉 목표를 다음 봉 시가에 모의 적용 |
| v2 | adx_14_trend | 9805.77 | -194.23 | sell / filled / Wilder ADX14 >= 25 그리고 +DI14 > -DI14; 조건 미충족; ADX14=24.7281, plus_DI14=33.8838, minus_DI14=22.7145; 직전 완료 봉 목표를 다음 봉 시가에 모의 적용 |
| v2 | aroon_25_trend | 9922.89 | -77.11 | sell / filled / Aroon25 Up > 70 그리고 Down < 30 (동률이면 최신 극값); 조건 미충족; Aroon_up=100, Aroon_down=80; 직전 완료 봉 목표를 다음 봉 시가에 모의 적용 |
| v2 | cci_20_momentum | 9909.53 | -90.47 | sell / filled / CCI20 > 100 (전형가격·평균절대편차); 조건 미충족; CCI20=87.8356; 직전 완료 봉 목표를 다음 봉 시가에 모의 적용 |
| v2 | williams_14_recovery | 9805.15 | -194.85 | sell / filled / 직전 Williams %R14 < -80, 현재 >= -80 (한 봉 목표); 조건 미충족; Williams_R14=-70.4729, previous_R14=-69.2907; 직전 완료 봉 목표를 다음 봉 시가에 모의 적용 |
| v2 | cmf_20_accumulation | 9734.86 | -265.14 | sell / filled / Chaikin Money Flow20 > 0.1; 조건 미충족; CMF20=0.0647408, volume20=1.77993e+06; 직전 완료 봉 목표를 다음 봉 시가에 모의 적용 |
| v2 | chaikin_3_10 | 9829.07 | -170.93 | sell / filled / ADL의 EMA3 - EMA10 > 0 그리고 종가 > EMA26; 조건 미충족; Chaikin3_10=-1094.33, ADL=-1.60023e+07, close=523.58, EMA26=523.074; 직전 완료 봉 목표를 다음 봉 시가에 모의 적용 |
| v2 | roc_10_momentum | 9937.03 | -62.97 | sell / filled / 10봉 ROC > 1% 그리고 종가 > EMA26; 조건 미충족; ROC10_percent=0.771645, close=523.68, EMA26=521.367; 직전 완료 봉 목표를 다음 봉 시가에 모의 적용 |
| v2 | trix_15_trend | 9948.40 | -51.60 | buy / partial / 15봉 삼중 EMA의 1봉 변화율 TRIX > 0 그리고 종가 > EMA26; 조건 충족; TRIX15_percent=0.000473967, close=521.46, EMA26=519.585; 직전 완료 봉 목표를 다음 봉 시가에 모의 적용 |
| v2 | keltner_20_breakout | 9940.51 | -59.49 | sell / filled / 종가 > EMA20 + 2 x Wilder ATR14; 조건 미충족; close=523.68, upper_Keltner=523.985, EMA20=521.785, ATR14=1.10038; 직전 완료 봉 목표를 다음 봉 시가에 모의 적용 |
| v2 | opening_range_30m | 9734.01 | -265.99 | buy / partial / 뉴욕 09:30·09:45 두 완료 봉 최고가를 10:00 이후 종가가 돌파; 조건 충족; close=523.58, opening_high=523.47; 직전 완료 봉 목표를 다음 봉 시가에 모의 적용 |

### 같은 기간의 비용·노출 비교 (사후 연구)

| 전략 | 비용 전 | 비용 후 | 100% 보유 | 같은 평균 노출 보유 | 평균 노출 |
|---|---:|---:|---:|---:|---:|
| cash | 0.00% | 0.00% | 1.63% | 0.00% | 0.00% |
| buy_hold | 2.06% | 1.63% | 1.63% | 1.63% | 100.00% |
| trend_8_26 | 2.11% | -1.68% | 1.63% | 1.01% | 62.14% |
| momentum_26 | 0.72% | -3.42% | 1.63% | 0.95% | 57.96% |
| breakout_8 | 0.85% | -16.17% | 1.63% | 0.38% | 22.98% |
| reversion_12 | -0.52% | -8.92% | 1.63% | 0.37% | 22.45% |
| volume_26 | 0.39% | -9.23% | 1.63% | 0.17% | 10.44% |
| trend_8_26 AND momentum_26 | 1.84% | -2.35% | 1.63% | 0.86% | 52.74% |
| trend_8_26 + momentum_26 | 1.42% | -2.55% | 1.63% | 0.98% | 60.05% |
| trend_8_26 AND breakout_8 | 1.24% | -11.12% | 1.63% | 0.26% | 15.93% |
| trend_8_26 + breakout_8 | 1.48% | -8.83% | 1.63% | 0.69% | 42.57% |
| trend_8_26 AND reversion_12 | 0.48% | -5.25% | 1.63% | 0.12% | 7.05% |
| trend_8_26 + reversion_12 | 0.79% | -5.18% | 1.63% | 0.69% | 42.30% |
| trend_8_26 AND volume_26 | 1.66% | -3.75% | 1.63% | 0.09% | 5.48% |
| trend_8_26 + volume_26 | 1.25% | -5.34% | 1.63% | 0.59% | 36.30% |
| momentum_26 AND breakout_8 | 0.41% | -11.85% | 1.63% | 0.27% | 16.45% |
| momentum_26 + breakout_8 | 0.79% | -9.83% | 1.63% | 0.66% | 40.48% |
| momentum_26 AND reversion_12 | -0.22% | -3.92% | 1.63% | 0.10% | 6.01% |
| momentum_26 + reversion_12 | 0.10% | -5.23% | 1.63% | 0.66% | 40.21% |
| momentum_26 AND volume_26 | 0.10% | -5.62% | 1.63% | 0.09% | 5.48% |
| momentum_26 + volume_26 | 0.56% | -5.78% | 1.63% | 0.56% | 34.21% |
| breakout_8 AND reversion_12 | 0.00% | 0.00% | 1.63% | 0.00% | 0.00% |
| breakout_8 + reversion_12 | 0.16% | -12.26% | 1.63% | 0.37% | 22.72% |
| breakout_8 AND volume_26 | -0.47% | -3.75% | 1.63% | 0.05% | 3.13% |
| breakout_8 + volume_26 | 0.62% | -11.86% | 1.63% | 0.27% | 16.72% |
| reversion_12 AND volume_26 | 0.29% | -4.24% | 1.63% | 0.06% | 3.39% |
| reversion_12 + volume_26 | -0.06% | -8.89% | 1.63% | 0.27% | 16.45% |
| ema_12_26 | 0.58% | -2.33% | 1.63% | 0.90% | 55.35% |
| macd_12_26_9 | 2.07% | -1.72% | 1.63% | 0.51% | 31.33% |
| rsi_14_recovery | 0.16% | -1.09% | 1.63% | 0.01% | 0.78% |
| bollinger_20_reentry | 0.11% | -4.01% | 1.63% | 0.04% | 2.61% |
| donchian_20 | 0.36% | -6.94% | 1.63% | 0.16% | 9.66% |
| atr_14_breakout | -0.26% | -7.52% | 1.63% | 0.09% | 5.74% |
| session_vwap | 2.58% | -4.89% | 1.63% | 0.88% | 54.05% |
| obv_20 | 0.90% | -6.84% | 1.63% | 0.75% | 45.69% |
| stochastic_14_3_recovery | 0.95% | -11.37% | 1.63% | 0.13% | 8.09% |
| mfi_14_recovery | 0.22% | -3.50% | 1.63% | 0.04% | 2.35% |
| adx_14_trend | -0.05% | -4.16% | 1.63% | 0.53% | 32.38% |
| aroon_25_trend | 1.44% | -2.32% | 1.63% | 0.42% | 25.85% |
| cci_20_momentum | 1.17% | -4.61% | 1.63% | 0.40% | 24.80% |
| williams_14_recovery | 1.54% | -6.64% | 1.63% | 0.09% | 5.22% |
| cmf_20_accumulation | 1.42% | -6.75% | 1.63% | 0.54% | 32.90% |
| chaikin_3_10 | 2.21% | -6.81% | 1.63% | 0.76% | 46.48% |
| roc_10_momentum | -0.07% | -0.90% | 1.63% | 0.03% | 2.09% |
| trix_15_trend | 0.63% | -3.10% | 1.63% | 0.78% | 48.04% |
| keltner_20_breakout | 0.78% | -5.77% | 1.63% | 0.30% | 18.28% |
| opening_range_30m | 1.46% | -4.73% | 1.63% | 0.48% | 29.24% |

동일 구간·초기 자금, 종료 시 청산 비용 포함. 노출 맞춤은 사후 설명용이며 v2 실제 계좌 성과가 아닙니다.
[낙폭 분해·비용 영향·전체 구간](DIA/comparison.json)

[v1 전체 기록](DIA/accounts.json) · [v2 전체 기록](DIA/accounts-v2.json)

## MSFT 계좌

| 모델 | 전략 | 평가액 USD | 손익 USD | 최근 매매·이유 |
|---|---|---:|---:|---|
| v1 | cash | 10000.00 | 0.00 | 대기 /  / 새 신호 대기 |
| v1 | buy_hold | 9793.81 | -206.19 | buy /  / buy_hold: prior completed bar target 100%; next bar open simulation |
| v1 | trend_8_26 | 9611.49 | -388.51 | buy /  / trend_8_26: prior completed bar target 100%; next bar open simulation |
| v1 | momentum_26 | 9607.85 | -392.15 | sell /  / momentum_26: prior completed bar target 0%; next bar open simulation |
| v1 | breakout_8 | 9679.79 | -320.21 | sell /  / breakout_8: prior completed bar target 0%; next bar open simulation |
| v1 | reversion_12 | 9638.08 | -361.92 | buy /  / reversion_12: prior completed bar target 100%; next bar open simulation |
| v1 | volume_26 | 9811.31 | -188.69 | sell /  / volume_26: prior completed bar target 0%; next bar open simulation |
| v1 | trend_8_26 AND momentum_26 | 9662.97 | -337.03 | sell /  / trend_8_26 AND momentum_26: prior completed bar target 0%; next bar open simulation |
| v1 | trend_8_26 + momentum_26 | 9628.87 | -371.13 | buy /  / trend_8_26 + momentum_26: prior completed bar target 50%; next bar open simulation |
| v1 | trend_8_26 AND breakout_8 | 9820.11 | -179.89 | sell /  / trend_8_26 AND breakout_8: prior completed bar target 0%; next bar open simulation |
| v1 | trend_8_26 + breakout_8 | 9684.47 | -315.53 | buy /  / trend_8_26 + breakout_8: prior completed bar target 50%; next bar open simulation |
| v1 | trend_8_26 AND reversion_12 | 9674.21 | -325.79 | buy /  / trend_8_26 AND reversion_12: prior completed bar target 100%; next bar open simulation |
| v1 | trend_8_26 + reversion_12 | 9624.71 | -375.29 | buy /  / trend_8_26 + reversion_12: prior completed bar target 100%; next bar open simulation |
| v1 | trend_8_26 AND volume_26 | 9916.79 | -83.21 | sell /  / trend_8_26 AND volume_26: prior completed bar target 0%; next bar open simulation |
| v1 | trend_8_26 + volume_26 | 9711.08 | -288.92 | buy /  / trend_8_26 + volume_26: prior completed bar target 50%; next bar open simulation |
| v1 | momentum_26 AND breakout_8 | 9778.34 | -221.66 | sell /  / momentum_26 AND breakout_8: prior completed bar target 0%; next bar open simulation |
| v1 | momentum_26 + breakout_8 | 9644.04 | -355.96 | sell /  / momentum_26 + breakout_8: prior completed bar target 0%; next bar open simulation |
| v1 | momentum_26 AND reversion_12 | 9707.47 | -292.53 | sell /  / momentum_26 AND reversion_12: prior completed bar target 0%; next bar open simulation |
| v1 | momentum_26 + reversion_12 | 9622.88 | -377.12 | buy /  / momentum_26 + reversion_12: prior completed bar target 50%; next bar open simulation |
| v1 | momentum_26 AND volume_26 | 9916.79 | -83.21 | sell /  / momentum_26 AND volume_26: prior completed bar target 0%; next bar open simulation |
| v1 | momentum_26 + volume_26 | 9709.27 | -290.73 | sell /  / momentum_26 + volume_26: prior completed bar target 0%; next bar open simulation |
| v1 | breakout_8 AND reversion_12 | 10000.00 | 0.00 | 대기 /  / 새 신호 대기 |
| v1 | breakout_8 + reversion_12 | 9678.14 | -321.86 | buy /  / breakout_8 + reversion_12: prior completed bar target 50%; next bar open simulation |
| v1 | breakout_8 AND volume_26 | 9953.19 | -46.81 | sell /  / breakout_8 AND volume_26: prior completed bar target 0%; next bar open simulation |
| v1 | breakout_8 + volume_26 | 9764.69 | -235.31 | sell /  / breakout_8 + volume_26: prior completed bar target 0%; next bar open simulation |
| v1 | reversion_12 AND volume_26 | 9938.00 | -62.00 | sell /  / reversion_12 AND volume_26: prior completed bar target 0%; next bar open simulation |
| v1 | reversion_12 + volume_26 | 9724.27 | -275.73 | buy /  / reversion_12 + volume_26: prior completed bar target 50%; next bar open simulation |
| v1 | ema_12_26 | 9588.87 | -411.13 | sell /  / EMA12 > EMA26; 조건 미충족; EMA12=532.137, EMA26=532.175 |
| v1 | macd_12_26_9 | 9762.31 | -237.69 | sell /  / MACD > 신호선 그리고 MACD > 0; 조건 미충족; MACD=-0.0387557, signal9=-0.0148606 |
| v1 | rsi_14_recovery | 9957.14 | -42.86 | sell /  / 직전 RSI14 < 30, 현재 RSI14 >= 30 (한 봉 목표); 조건 미충족; RSI14=45.5102, previous_RSI14=37.5844 |
| v1 | bollinger_20_reentry | 9854.81 | -145.19 | sell /  / 직전 종가 < 직전 하단밴드, 현재 하단밴드 <= 종가 <= SMA20 (한 봉 목표); 조건 미충족; close=531.675, lower20=529.239, SMA20=533.058, previous_lower20=529.387 |
| v1 | donchian_20 | 9912.16 | -87.84 | sell /  / 종가 > 현재 봉을 제외한 직전 20봉 최고가; 조건 미충족; close=534.52, prior_high20=535.44 |
| v1 | atr_14_breakout | 9915.10 | -84.90 | sell /  / 종가 > 직전 종가 + 직전 ATR14 그리고 종가 > EMA26; 조건 미충족; close=533.975, threshold=536.307, prior_ATR14=2.16203, EMA26=530.521 |
| v1 | session_vwap | 9833.84 | -166.16 | sell /  / 종가 > 뉴욕 거래일별 누적 전형가격 VWAP; 조건 미충족; close=530.6, session_VWAP=530.833, session_volume=8.14839e+06 |
| v1 | obv_20 | 9685.13 | -314.87 | sell /  / OBV > OBV의 SMA20 그리고 종가 > EMA26; 조건 미충족; OBV=9.18612e+07, OBV_SMA20=9.19297e+07, close=532.21, EMA26=532.291 |
| v1 | stochastic_14_3_recovery | 9789.03 | -210.97 | sell /  / 직전 %K14 < 20에서 %K14가 %D3 상향 돌파 (한 봉 목표); 조건 미충족; K14=60.6262, D3=34.5689, previous_K14=38.87, previous_D3=26.948 |
| v1 | mfi_14_recovery | 9972.58 | -27.42 | sell /  / 직전 MFI14 < 20, 현재 MFI14 >= 20 (한 봉 목표); 조건 미충족; MFI14=53.413, previous_MFI14=44.3372 |
| v1 | adx_14_trend | 9883.62 | -116.38 | sell /  / Wilder ADX14 >= 25 그리고 +DI14 > -DI14; 조건 미충족; ADX14=23.6824, plus_DI14=22.3066, minus_DI14=19.9214 |
| v1 | aroon_25_trend | 9812.47 | -187.53 | sell /  / Aroon25 Up > 70 그리고 Down < 30 (동률이면 최신 극값); 조건 미충족; Aroon_up=68, Aroon_down=20 |
| v1 | cci_20_momentum | 9949.66 | -50.34 | sell /  / CCI20 > 100 (전형가격·평균절대편차); 조건 미충족; CCI20=69.3811 |
| v1 | williams_14_recovery | 9819.22 | -180.78 | sell /  / 직전 Williams %R14 < -80, 현재 >= -80 (한 봉 목표); 조건 미충족; Williams_R14=-39.3738, previous_R14=-61.13 |
| v1 | cmf_20_accumulation | 9672.78 | -327.22 | sell /  / Chaikin Money Flow20 > 0.1; 조건 미충족; CMF20=0.0753291, volume20=4.96995e+06 |
| v1 | chaikin_3_10 | 9723.66 | -276.34 | sell /  / ADL의 EMA3 - EMA10 > 0 그리고 종가 > EMA26; 조건 미충족; Chaikin3_10=121607, ADL=1.11106e+08, close=532.21, EMA26=532.291 |
| v1 | roc_10_momentum | 9959.43 | -40.57 | sell /  / 10봉 ROC > 1% 그리고 종가 > EMA26; 조건 미충족; ROC10_percent=0.454191, close=534.125, EMA26=532.186 |
| v1 | trix_15_trend | 9712.42 | -287.58 | sell /  / 15봉 삼중 EMA의 1봉 변화율 TRIX > 0 그리고 종가 > EMA26; 조건 미충족; TRIX15_percent=0.0172213, close=526.676, EMA26=532.897 |
| v1 | keltner_20_breakout | 9958.78 | -41.22 | sell /  / 종가 > EMA20 + 2 x Wilder ATR14; 조건 미충족; close=533.975, upper_Keltner=534.357, EMA20=530.111, ATR14=2.12332 |
| v1 | opening_range_30m | 9711.79 | -288.21 | sell /  / 뉴욕 09:30·09:45 두 완료 봉 최고가를 10:00 이후 종가가 돌파; 자료 부족·변동폭 또는 거래량 없음: 대기; close=526.676 |
| v2 | cash | 10000.00 | 0.00 | 대기 /  / 새 신호 대기 |
| v2 | buy_hold | 9847.25 | -152.75 | buy / partial / 직전 완료 봉 목표 비중 100%; 다음 봉 시가 가정 |
| v2 | trend_8_26 | 9546.67 | -453.33 | buy / partial / 직전 완료 봉 목표 비중 100%; 다음 봉 시가 가정 |
| v2 | momentum_26 | 9649.74 | -350.26 | sell / filled / 직전 완료 봉 목표 비중 0%; 다음 봉 시가 가정 |
| v2 | breakout_8 | 9468.63 | -531.37 | sell / filled / 직전 완료 봉 목표 비중 0%; 다음 봉 시가 가정 |
| v2 | reversion_12 | 9260.31 | -739.69 | buy / partial / 직전 완료 봉 목표 비중 100%; 다음 봉 시가 가정 |
| v2 | volume_26 | 9498.13 | -501.87 | sell / filled / 직전 완료 봉 목표 비중 0%; 다음 봉 시가 가정 |
| v2 | trend_8_26 AND momentum_26 | 9560.49 | -439.51 | sell / filled / 직전 완료 봉 목표 비중 0%; 다음 봉 시가 가정 |
| v2 | trend_8_26 + momentum_26 | 9618.46 | -381.54 | buy / filled / 직전 완료 봉 목표 비중 50%; 다음 봉 시가 가정 |
| v2 | trend_8_26 AND breakout_8 | 9458.32 | -541.68 | sell / filled / 직전 완료 봉 목표 비중 0%; 다음 봉 시가 가정 |
| v2 | trend_8_26 + breakout_8 | 9568.09 | -431.91 | buy / filled / 직전 완료 봉 목표 비중 50%; 다음 봉 시가 가정 |
| v2 | trend_8_26 AND reversion_12 | 9568.95 | -431.05 | buy / partial / 직전 완료 봉 목표 비중 100%; 다음 봉 시가 가정 |
| v2 | trend_8_26 + reversion_12 | 9402.01 | -597.99 | buy / partial / 직전 완료 봉 목표 비중 100%; 다음 봉 시가 가정 |
| v2 | trend_8_26 AND volume_26 | 9861.94 | -138.06 | sell / filled / 직전 완료 봉 목표 비중 0%; 다음 봉 시가 가정 |
| v2 | trend_8_26 + volume_26 | 9542.39 | -457.61 | buy / filled / 직전 완료 봉 목표 비중 50%; 다음 봉 시가 가정 |
| v2 | momentum_26 AND breakout_8 | 9567.71 | -432.29 | sell / filled / 직전 완료 봉 목표 비중 0%; 다음 봉 시가 가정 |
| v2 | momentum_26 + breakout_8 | 9559.11 | -440.89 | sell / filled / 직전 완료 봉 목표 비중 0%; 다음 봉 시가 가정 |
| v2 | momentum_26 AND reversion_12 | 9533.70 | -466.30 | sell / filled / 직전 완료 봉 목표 비중 0%; 다음 봉 시가 가정 |
| v2 | momentum_26 + reversion_12 | 9452.73 | -547.27 | buy / filled / 직전 완료 봉 목표 비중 50%; 다음 봉 시가 가정 |
| v2 | momentum_26 AND volume_26 | 9785.21 | -214.79 | sell / filled / 직전 완료 봉 목표 비중 0%; 다음 봉 시가 가정 |
| v2 | momentum_26 + volume_26 | 9593.92 | -406.08 | sell / filled / 직전 완료 봉 목표 비중 0%; 다음 봉 시가 가정 |
| v2 | breakout_8 AND reversion_12 | 10000.00 | 0.00 | 대기 /  / 새 신호 대기 |
| v2 | breakout_8 + reversion_12 | 9402.96 | -597.04 | buy / filled / 직전 완료 봉 목표 비중 50%; 다음 봉 시가 가정 |
| v2 | breakout_8 AND volume_26 | 9890.09 | -109.91 | sell / filled / 직전 완료 봉 목표 비중 0%; 다음 봉 시가 가정 |
| v2 | breakout_8 + volume_26 | 9523.17 | -476.83 | sell / filled / 직전 완료 봉 목표 비중 0%; 다음 봉 시가 가정 |
| v2 | reversion_12 AND volume_26 | 9699.57 | -300.43 | sell / filled / 직전 완료 봉 목표 비중 0%; 다음 봉 시가 가정 |
| v2 | reversion_12 + volume_26 | 9378.26 | -621.74 | buy / filled / 직전 완료 봉 목표 비중 50%; 다음 봉 시가 가정 |
| v2 | ema_12_26 | 9583.12 | -416.88 | sell / filled / EMA12 > EMA26; 조건 미충족; EMA12=532.137, EMA26=532.175; 직전 완료 봉 목표를 다음 봉 시가에 모의 적용 |
| v2 | macd_12_26_9 | 9756.46 | -243.54 | sell / filled / MACD > 신호선 그리고 MACD > 0; 조건 미충족; MACD=-0.0387557, signal9=-0.0148606; 직전 완료 봉 목표를 다음 봉 시가에 모의 적용 |
| v2 | rsi_14_recovery | 9951.17 | -48.83 | sell / filled / 직전 RSI14 < 30, 현재 RSI14 >= 30 (한 봉 목표); 조건 미충족; RSI14=45.5102, previous_RSI14=37.5844; 직전 완료 봉 목표를 다음 봉 시가에 모의 적용 |
| v2 | bollinger_20_reentry | 9848.90 | -151.10 | sell / filled / 직전 종가 < 직전 하단밴드, 현재 하단밴드 <= 종가 <= SMA20 (한 봉 목표); 조건 미충족; close=531.675, lower20=529.239, SMA20=533.058, previous_lower20=529.387; 직전 완료 봉 목표를 다음 봉 시가에 모의 적용 |
| v2 | donchian_20 | 9908.19 | -91.81 | sell / filled / 종가 > 현재 봉을 제외한 직전 20봉 최고가; 조건 미충족; close=534.52, prior_high20=535.44; 직전 완료 봉 목표를 다음 봉 시가에 모의 적용 |
| v2 | atr_14_breakout | 9911.14 | -88.86 | sell / filled / 종가 > 직전 종가 + 직전 ATR14 그리고 종가 > EMA26; 조건 미충족; close=533.975, threshold=536.307, prior_ATR14=2.16203, EMA26=530.521; 직전 완료 봉 목표를 다음 봉 시가에 모의 적용 |
| v2 | session_vwap | 9825.97 | -174.03 | sell / filled / 종가 > 뉴욕 거래일별 누적 전형가격 VWAP; 조건 미충족; close=530.6, session_VWAP=530.833, session_volume=8.14839e+06; 직전 완료 봉 목표를 다음 봉 시가에 모의 적용 |
| v2 | obv_20 | 9673.51 | -326.49 | sell / filled / OBV > OBV의 SMA20 그리고 종가 > EMA26; 조건 미충족; OBV=9.18612e+07, OBV_SMA20=9.19297e+07, close=532.21, EMA26=532.291; 직전 완료 봉 목표를 다음 봉 시가에 모의 적용 |
| v2 | stochastic_14_3_recovery | 9779.25 | -220.75 | sell / filled / 직전 %K14 < 20에서 %K14가 %D3 상향 돌파 (한 봉 목표); 조건 미충족; K14=60.6262, D3=34.5689, previous_K14=38.87, previous_D3=26.948; 직전 완료 봉 목표를 다음 봉 시가에 모의 적용 |
| v2 | mfi_14_recovery | 9968.59 | -31.41 | sell / filled / 직전 MFI14 < 20, 현재 MFI14 >= 20 (한 봉 목표); 조건 미충족; MFI14=53.413, previous_MFI14=44.3372; 직전 완료 봉 목표를 다음 봉 시가에 모의 적용 |
| v2 | adx_14_trend | 9879.67 | -120.33 | sell / filled / Wilder ADX14 >= 25 그리고 +DI14 > -DI14; 조건 미충족; ADX14=23.6824, plus_DI14=22.3066, minus_DI14=19.9214; 직전 완료 봉 목표를 다음 봉 시가에 모의 적용 |
| v2 | aroon_25_trend | 9808.55 | -191.45 | sell / filled / Aroon25 Up > 70 그리고 Down < 30 (동률이면 최신 극값); 조건 미충족; Aroon_up=68, Aroon_down=20; 직전 완료 봉 목표를 다음 봉 시가에 모의 적용 |
| v2 | cci_20_momentum | 9945.68 | -54.32 | sell / filled / CCI20 > 100 (전형가격·평균절대편차); 조건 미충족; CCI20=69.3811; 직전 완료 봉 목표를 다음 봉 시가에 모의 적용 |
| v2 | williams_14_recovery | 9811.37 | -188.63 | sell / filled / 직전 Williams %R14 < -80, 현재 >= -80 (한 봉 목표); 조건 미충족; Williams_R14=-39.3738, previous_R14=-61.13; 직전 완료 봉 목표를 다음 봉 시가에 모의 적용 |
| v2 | cmf_20_accumulation | 9666.97 | -333.03 | sell / filled / Chaikin Money Flow20 > 0.1; 조건 미충족; CMF20=0.0753291, volume20=4.96995e+06; 직전 완료 봉 목표를 다음 봉 시가에 모의 적용 |
| v2 | chaikin_3_10 | 9713.94 | -286.06 | sell / filled / ADL의 EMA3 - EMA10 > 0 그리고 종가 > EMA26; 조건 미충족; Chaikin3_10=121607, ADL=1.11106e+08, close=532.21, EMA26=532.291; 직전 완료 봉 목표를 다음 봉 시가에 모의 적용 |
| v2 | roc_10_momentum | 9957.44 | -42.56 | sell / filled / 10봉 ROC > 1% 그리고 종가 > EMA26; 조건 미충족; ROC10_percent=0.454191, close=534.125, EMA26=532.186; 직전 완료 봉 목표를 다음 봉 시가에 모의 적용 |
| v2 | trix_15_trend | 9708.54 | -291.46 | sell / filled / 15봉 삼중 EMA의 1봉 변화율 TRIX > 0 그리고 종가 > EMA26; 조건 미충족; TRIX15_percent=0.0172213, close=526.676, EMA26=532.897; 직전 완료 봉 목표를 다음 봉 시가에 모의 적용 |
| v2 | keltner_20_breakout | 9956.78 | -43.22 | sell / filled / 종가 > EMA20 + 2 x Wilder ATR14; 조건 미충족; close=533.975, upper_Keltner=534.357, EMA20=530.111, ATR14=2.12332; 직전 완료 봉 목표를 다음 봉 시가에 모의 적용 |
| v2 | opening_range_30m | 9707.90 | -292.10 | sell / filled / 뉴욕 09:30·09:45 두 완료 봉 최고가를 10:00 이후 종가가 돌파; 자료 부족·변동폭 또는 거래량 없음: 대기; close=526.676; 직전 완료 봉 목표를 다음 봉 시가에 모의 적용 |

### 같은 기간의 비용·노출 비교 (사후 연구)

| 전략 | 비용 전 | 비용 후 | 100% 보유 | 같은 평균 노출 보유 | 평균 노출 |
|---|---:|---:|---:|---:|---:|
| cash | 0.00% | 0.00% | 2.03% | 0.00% | 0.00% |
| buy_hold | 2.46% | 2.03% | 2.03% | 2.03% | 100.00% |
| trend_8_26 | -0.71% | -4.39% | 2.03% | 1.20% | 59.53% |
| momentum_26 | -0.46% | -5.75% | 2.03% | 1.19% | 59.27% |
| breakout_8 | 6.00% | -8.87% | 2.03% | 0.39% | 19.58% |
| reversion_12 | -4.20% | -13.38% | 2.03% | 0.48% | 24.28% |
| volume_26 | 0.04% | -7.25% | 2.03% | 0.16% | 7.83% |
| trend_8_26 AND momentum_26 | -1.50% | -6.74% | 2.03% | 1.07% | 53.52% |
| trend_8_26 + momentum_26 | -0.58% | -4.86% | 2.03% | 1.19% | 59.40% |
| trend_8_26 AND breakout_8 | 0.24% | -10.13% | 2.03% | 0.24% | 12.27% |
| trend_8_26 + breakout_8 | 2.61% | -5.86% | 2.03% | 0.79% | 39.56% |
| trend_8_26 AND reversion_12 | -1.30% | -7.72% | 2.03% | 0.15% | 7.31% |
| trend_8_26 + reversion_12 | -2.45% | -8.81% | 2.03% | 0.84% | 41.91% |
| trend_8_26 AND volume_26 | 2.40% | -0.56% | 2.03% | 0.05% | 2.61% |
| trend_8_26 + volume_26 | -0.32% | -5.24% | 2.03% | 0.67% | 33.68% |
| momentum_26 AND breakout_8 | 2.49% | -8.50% | 2.03% | 0.25% | 12.53% |
| momentum_26 + breakout_8 | 2.74% | -6.93% | 2.03% | 0.79% | 39.43% |
| momentum_26 AND reversion_12 | -2.41% | -9.14% | 2.03% | 0.19% | 9.66% |
| momentum_26 + reversion_12 | -2.33% | -9.65% | 2.03% | 0.84% | 41.78% |
| momentum_26 AND volume_26 | 0.89% | -3.26% | 2.03% | 0.07% | 3.39% |
| momentum_26 + volume_26 | -0.19% | -6.10% | 2.03% | 0.67% | 33.55% |
| breakout_8 AND reversion_12 | 0.00% | 0.00% | 2.03% | 0.00% | 0.00% |
| breakout_8 + reversion_12 | 0.80% | -10.41% | 2.03% | 0.44% | 21.94% |
| breakout_8 AND volume_26 | 2.04% | -0.50% | 2.03% | 0.04% | 1.83% |
| breakout_8 + volume_26 | 2.99% | -7.48% | 2.03% | 0.27% | 13.71% |
| reversion_12 AND volume_26 | -2.90% | -6.11% | 2.03% | 0.07% | 3.39% |
| reversion_12 + volume_26 | -2.09% | -10.37% | 2.03% | 0.32% | 16.06% |
| ema_12_26 | -1.46% | -5.11% | 2.03% | 1.23% | 61.36% |
| macd_12_26_9 | -0.51% | -5.79% | 2.03% | 0.69% | 34.46% |
| rsi_14_recovery | 0.31% | -2.19% | 2.03% | 0.03% | 1.57% |
| bollinger_20_reentry | -0.92% | -3.79% | 2.03% | 0.04% | 1.83% |
| donchian_20 | 1.05% | -4.32% | 2.03% | 0.08% | 4.18% |
| atr_14_breakout | 1.36% | -3.62% | 2.03% | 0.07% | 3.39% |
| session_vwap | 5.26% | -2.82% | 2.03% | 0.84% | 42.04% |
| obv_20 | 4.98% | -3.07% | 2.03% | 0.96% | 47.78% |
| stochastic_14_3_recovery | -0.50% | -10.42% | 2.03% | 0.13% | 6.53% |
| mfi_14_recovery | 1.58% | -2.19% | 2.03% | 0.05% | 2.35% |
| adx_14_trend | 3.84% | 1.26% | 2.03% | 0.93% | 46.21% |
| aroon_25_trend | -0.45% | -4.95% | 2.03% | 0.44% | 22.19% |
| cci_20_momentum | 2.53% | -4.13% | 2.03% | 0.42% | 20.89% |
| williams_14_recovery | -1.26% | -9.97% | 2.03% | 0.11% | 5.74% |
| cmf_20_accumulation | 0.39% | -5.34% | 2.03% | 0.67% | 33.68% |
| chaikin_3_10 | 3.88% | -3.68% | 2.03% | 0.92% | 45.69% |
| roc_10_momentum | -0.64% | -4.73% | 2.03% | 0.29% | 14.36% |
| trix_15_trend | -1.14% | -5.20% | 2.03% | 0.97% | 48.56% |
| keltner_20_breakout | 0.46% | -4.88% | 2.03% | 0.24% | 12.27% |
| opening_range_30m | -1.20% | -4.47% | 2.03% | 0.43% | 21.41% |

동일 구간·초기 자금, 종료 시 청산 비용 포함. 노출 맞춤은 사후 설명용이며 v2 실제 계좌 성과가 아닙니다.
[낙폭 분해·비용 영향·전체 구간](MSFT/comparison.json)

[v1 전체 기록](MSFT/accounts.json) · [v2 전체 기록](MSFT/accounts-v2.json)

## JPM 계좌

| 모델 | 전략 | 평가액 USD | 손익 USD | 최근 매매·이유 |
|---|---|---:|---:|---|
| v1 | cash | 10000.00 | 0.00 | 대기 /  / 새 신호 대기 |
| v1 | buy_hold | 9842.92 | -157.08 | buy /  / buy_hold: prior completed bar target 100%; next bar open simulation |
| v1 | trend_8_26 | 9786.16 | -213.84 | sell /  / trend_8_26: prior completed bar target 0%; next bar open simulation |
| v1 | momentum_26 | 9678.87 | -321.13 | buy /  / momentum_26: prior completed bar target 100%; next bar open simulation |
| v1 | breakout_8 | 9759.46 | -240.54 | sell /  / breakout_8: prior completed bar target 0%; next bar open simulation |
| v1 | reversion_12 | 9688.80 | -311.20 | sell /  / reversion_12: prior completed bar target 0%; next bar open simulation |
| v1 | volume_26 | 9961.97 | -38.03 | sell /  / volume_26: prior completed bar target 0%; next bar open simulation |
| v1 | trend_8_26 AND momentum_26 | 9793.49 | -206.51 | sell /  / trend_8_26 AND momentum_26: prior completed bar target 0%; next bar open simulation |
| v1 | trend_8_26 + momentum_26 | 9732.32 | -267.68 | sell /  / trend_8_26 + momentum_26: prior completed bar target 50%; next bar open simulation |
| v1 | trend_8_26 AND breakout_8 | 9915.55 | -84.45 | sell /  / trend_8_26 AND breakout_8: prior completed bar target 0%; next bar open simulation |
| v1 | trend_8_26 + breakout_8 | 9792.38 | -207.62 | sell /  / trend_8_26 + breakout_8: prior completed bar target 0%; next bar open simulation |
| v1 | trend_8_26 AND reversion_12 | 9855.61 | -144.39 | sell /  / trend_8_26 AND reversion_12: prior completed bar target 0%; next bar open simulation |
| v1 | trend_8_26 + reversion_12 | 9737.25 | -262.75 | sell /  / trend_8_26 + reversion_12: prior completed bar target 0%; next bar open simulation |
| v1 | trend_8_26 AND volume_26 | 10035.68 | 35.68 | sell /  / trend_8_26 AND volume_26: prior completed bar target 0%; next bar open simulation |
| v1 | trend_8_26 + volume_26 | 9873.52 | -126.48 | sell /  / trend_8_26 + volume_26: prior completed bar target 0%; next bar open simulation |
| v1 | momentum_26 AND breakout_8 | 9733.77 | -266.23 | sell /  / momentum_26 AND breakout_8: prior completed bar target 0%; next bar open simulation |
| v1 | momentum_26 + breakout_8 | 9719.13 | -280.87 | sell /  / momentum_26 + breakout_8: prior completed bar target 50%; next bar open simulation |
| v1 | momentum_26 AND reversion_12 | 9849.85 | -150.15 | sell /  / momentum_26 AND reversion_12: prior completed bar target 0%; next bar open simulation |
| v1 | momentum_26 + reversion_12 | 9722.55 | -277.45 | sell /  / momentum_26 + reversion_12: prior completed bar target 50%; next bar open simulation |
| v1 | momentum_26 AND volume_26 | 10035.68 | 35.68 | sell /  / momentum_26 AND volume_26: prior completed bar target 0%; next bar open simulation |
| v1 | momentum_26 + volume_26 | 9838.95 | -161.05 | sell /  / momentum_26 + volume_26: prior completed bar target 50%; next bar open simulation |
| v1 | breakout_8 AND reversion_12 | 10000.00 | 0.00 | 대기 /  / 새 신호 대기 |
| v1 | breakout_8 + reversion_12 | 9762.92 | -237.08 | sell /  / breakout_8 + reversion_12: prior completed bar target 0%; next bar open simulation |
| v1 | breakout_8 AND volume_26 | 10022.00 | 22.00 | sell /  / breakout_8 AND volume_26: prior completed bar target 0%; next bar open simulation |
| v1 | breakout_8 + volume_26 | 9860.16 | -139.84 | sell /  / breakout_8 + volume_26: prior completed bar target 0%; next bar open simulation |
| v1 | reversion_12 AND volume_26 | 9940.10 | -59.90 | sell /  / reversion_12 AND volume_26: prior completed bar target 0%; next bar open simulation |
| v1 | reversion_12 + volume_26 | 9844.00 | -156.00 | sell /  / reversion_12 + volume_26: prior completed bar target 0%; next bar open simulation |
| v1 | ema_12_26 | 9755.41 | -244.59 | sell /  / EMA12 > EMA26; 조건 미충족; EMA12=336.517, EMA26=336.551 |
| v1 | macd_12_26_9 | 9839.10 | -160.90 | sell /  / MACD > 신호선 그리고 MACD > 0; 조건 미충족; MACD=-0.0344827, signal9=-0.0504891 |
| v1 | rsi_14_recovery | 9986.37 | -13.63 | sell /  / 직전 RSI14 < 30, 현재 RSI14 >= 30 (한 봉 목표); 조건 미충족; RSI14=61.6663, previous_RSI14=57.046 |
| v1 | bollinger_20_reentry | 9964.67 | -35.33 | sell /  / 직전 종가 < 직전 하단밴드, 현재 하단밴드 <= 종가 <= SMA20 (한 봉 목표); 조건 미충족; close=336.53, lower20=336.046, SMA20=337.886, previous_lower20=336.231 |
| v1 | donchian_20 | 9830.85 | -169.15 | sell /  / 종가 > 현재 봉을 제외한 직전 20봉 최고가; 조건 미충족; close=339.04, prior_high20=339.42 |
| v1 | atr_14_breakout | 9746.56 | -253.44 | sell /  / 종가 > 직전 종가 + 직전 ATR14 그리고 종가 > EMA26; 조건 미충족; close=339.04, threshold=340.465, prior_ATR14=1.34545, EMA26=336.613 |
| v1 | session_vwap | 9727.57 | -272.43 | sell /  / 종가 > 뉴욕 거래일별 누적 전형가격 VWAP; 조건 미충족; close=336.08, session_VWAP=337.149, session_volume=2.04555e+06 |
| v1 | obv_20 | 10007.55 | 7.55 | sell /  / OBV > OBV의 SMA20 그리고 종가 > EMA26; 조건 미충족; OBV=-1.60234e+07, OBV_SMA20=-1.31788e+07, close=341.625, EMA26=338.807 |
| v1 | stochastic_14_3_recovery | 9593.34 | -406.66 | sell /  / 직전 %K14 < 20에서 %K14가 %D3 상향 돌파 (한 봉 목표); 조건 미충족; K14=17.3167, D3=17.2112, previous_K14=22.2303, previous_D3=19.0146 |
| v1 | mfi_14_recovery | 9935.64 | -64.36 | sell /  / 직전 MFI14 < 20, 현재 MFI14 >= 20 (한 봉 목표); 조건 미충족; MFI14=30.2719, previous_MFI14=26.8492 |
| v1 | adx_14_trend | 9726.68 | -273.32 | sell /  / Wilder ADX14 >= 25 그리고 +DI14 > -DI14; 조건 미충족; ADX14=23.9395, plus_DI14=23.2021, minus_DI14=22.594 |
| v1 | aroon_25_trend | 9824.71 | -175.29 | sell /  / Aroon25 Up > 70 그리고 Down < 30 (동률이면 최신 극값); 조건 미충족; Aroon_up=68, Aroon_down=16 |
| v1 | cci_20_momentum | 9950.54 | -49.46 | sell /  / CCI20 > 100 (전형가격·평균절대편차); 조건 미충족; CCI20=28.4392 |
| v1 | williams_14_recovery | 9699.76 | -300.24 | buy /  / 직전 Williams %R14 < -80, 현재 >= -80 (한 봉 목표); 조건 충족; Williams_R14=-67.9641, previous_R14=-82.6833 |
| v1 | cmf_20_accumulation | 9828.96 | -171.04 | sell /  / Chaikin Money Flow20 > 0.1; 조건 미충족; CMF20=-0.0481318, volume20=2.57468e+06 |
| v1 | chaikin_3_10 | 9837.22 | -162.78 | sell /  / ADL의 EMA3 - EMA10 > 0 그리고 종가 > EMA26; 조건 미충족; Chaikin3_10=7273.89, ADL=-1.28498e+07, close=336.08, EMA26=336.65 |
| v1 | roc_10_momentum | 9836.40 | -163.60 | sell /  / 10봉 ROC > 1% 그리고 종가 > EMA26; 조건 미충족; ROC10_percent=0.964142, close=337.72, EMA26=336.695 |
| v1 | trix_15_trend | 9723.73 | -276.27 | sell /  / 15봉 삼중 EMA의 1봉 변화율 TRIX > 0 그리고 종가 > EMA26; 조건 미충족; TRIX15_percent=0.0135144, close=337.6, EMA26=338.759 |
| v1 | keltner_20_breakout | 9905.24 | -94.76 | sell /  / 종가 > EMA20 + 2 x Wilder ATR14; 조건 미충족; close=339.04, upper_Keltner=339.281, EMA20=336.559, ATR14=1.36146 |
| v1 | opening_range_30m | 9850.26 | -149.74 | sell /  / 뉴욕 09:30·09:45 두 완료 봉 최고가를 10:00 이후 종가가 돌파; 조건 미충족; close=337.72, opening_high=339.035 |
| v2 | cash | 10000.00 | 0.00 | 대기 /  / 새 신호 대기 |
| v2 | buy_hold | 10007.39 | 7.39 | buy / partial / 직전 완료 봉 목표 비중 100%; 다음 봉 시가 가정 |
| v2 | trend_8_26 | 9791.24 | -208.76 | sell / filled / 직전 완료 봉 목표 비중 0%; 다음 봉 시가 가정 |
| v2 | momentum_26 | 9192.06 | -807.94 | buy / partial / 직전 완료 봉 목표 비중 100%; 다음 봉 시가 가정 |
| v2 | breakout_8 | 9100.10 | -899.90 | sell / filled / 직전 완료 봉 목표 비중 0%; 다음 봉 시가 가정 |
| v2 | reversion_12 | 9661.69 | -338.31 | sell / filled / 직전 완료 봉 목표 비중 0%; 다음 봉 시가 가정 |
| v2 | volume_26 | 9781.50 | -218.50 | sell / filled / 직전 완료 봉 목표 비중 0%; 다음 봉 시가 가정 |
| v2 | trend_8_26 AND momentum_26 | 9756.41 | -243.59 | sell / filled / 직전 완료 봉 목표 비중 0%; 다음 봉 시가 가정 |
| v2 | trend_8_26 + momentum_26 | 9507.34 | -492.66 | sell / filled / 직전 완료 봉 목표 비중 50%; 다음 봉 시가 가정 |
| v2 | trend_8_26 AND breakout_8 | 9287.76 | -712.24 | sell / filled / 직전 완료 봉 목표 비중 0%; 다음 봉 시가 가정 |
| v2 | trend_8_26 + breakout_8 | 9460.24 | -539.76 | sell / filled / 직전 완료 봉 목표 비중 0%; 다음 봉 시가 가정 |
| v2 | trend_8_26 AND reversion_12 | 9831.59 | -168.41 | sell / filled / 직전 완료 봉 목표 비중 0%; 다음 봉 시가 가정 |
| v2 | trend_8_26 + reversion_12 | 9767.26 | -232.74 | sell / filled / 직전 완료 봉 목표 비중 0%; 다음 봉 시가 가정 |
| v2 | trend_8_26 AND volume_26 | 9833.30 | -166.70 | sell / filled / 직전 완료 봉 목표 비중 0%; 다음 봉 시가 가정 |
| v2 | trend_8_26 + volume_26 | 9787.03 | -212.97 | sell / filled / 직전 완료 봉 목표 비중 0%; 다음 봉 시가 가정 |
| v2 | momentum_26 AND breakout_8 | 9058.00 | -942.00 | sell / filled / 직전 완료 봉 목표 비중 0%; 다음 봉 시가 가정 |
| v2 | momentum_26 + breakout_8 | 9166.81 | -833.19 | sell / filled / 직전 완료 봉 목표 비중 50%; 다음 봉 시가 가정 |
| v2 | momentum_26 AND reversion_12 | 9793.51 | -206.49 | sell / filled / 직전 완료 봉 목표 비중 0%; 다음 봉 시가 가정 |
| v2 | momentum_26 + reversion_12 | 9584.04 | -415.96 | sell / filled / 직전 완료 봉 목표 비중 50%; 다음 봉 시가 가정 |
| v2 | momentum_26 AND volume_26 | 9833.30 | -166.70 | sell / filled / 직전 완료 봉 목표 비중 0%; 다음 봉 시가 가정 |
| v2 | momentum_26 + volume_26 | 9563.30 | -436.70 | sell / filled / 직전 완료 봉 목표 비중 50%; 다음 봉 시가 가정 |
| v2 | breakout_8 AND reversion_12 | 10000.00 | 0.00 | 대기 /  / 새 신호 대기 |
| v2 | breakout_8 + reversion_12 | 9455.87 | -544.13 | sell / filled / 직전 완료 봉 목표 비중 0%; 다음 봉 시가 가정 |
| v2 | breakout_8 AND volume_26 | 9911.14 | -88.86 | sell / filled / 직전 완료 봉 목표 비중 0%; 다음 봉 시가 가정 |
| v2 | breakout_8 + volume_26 | 9454.59 | -545.41 | sell / filled / 직전 완료 봉 목표 비중 0%; 다음 봉 시가 가정 |
| v2 | reversion_12 AND volume_26 | 9987.18 | -12.82 | sell / filled / 직전 완료 봉 목표 비중 0%; 다음 봉 시가 가정 |
| v2 | reversion_12 + volume_26 | 9762.48 | -237.52 | sell / filled / 직전 완료 봉 목표 비중 0%; 다음 봉 시가 가정 |
| v2 | ema_12_26 | 9751.51 | -248.49 | sell / filled / EMA12 > EMA26; 조건 미충족; EMA12=336.517, EMA26=336.551; 직전 완료 봉 목표를 다음 봉 시가에 모의 적용 |
| v2 | macd_12_26_9 | 9835.16 | -164.84 | sell / filled / MACD > 신호선 그리고 MACD > 0; 조건 미충족; MACD=-0.0344827, signal9=-0.0504891; 직전 완료 봉 목표를 다음 봉 시가에 모의 적용 |
| v2 | rsi_14_recovery | 9984.37 | -15.63 | sell / filled / 직전 RSI14 < 30, 현재 RSI14 >= 30 (한 봉 목표); 조건 미충족; RSI14=61.6663, previous_RSI14=57.046; 직전 완료 봉 목표를 다음 봉 시가에 모의 적용 |
| v2 | bollinger_20_reentry | 9962.68 | -37.32 | sell / filled / 직전 종가 < 직전 하단밴드, 현재 하단밴드 <= 종가 <= SMA20 (한 봉 목표); 조건 미충족; close=336.53, lower20=336.046, SMA20=337.886, previous_lower20=336.231; 직전 완료 봉 목표를 다음 봉 시가에 모의 적용 |
| v2 | donchian_20 | 9824.96 | -175.04 | sell / filled / 종가 > 현재 봉을 제외한 직전 20봉 최고가; 조건 미충족; close=339.04, prior_high20=339.42; 직전 완료 봉 목표를 다음 봉 시가에 모의 적용 |
| v2 | atr_14_breakout | 9736.82 | -263.18 | sell / filled / 종가 > 직전 종가 + 직전 ATR14 그리고 종가 > EMA26; 조건 미충족; close=339.04, threshold=340.465, prior_ATR14=1.34545, EMA26=336.613; 직전 완료 봉 목표를 다음 봉 시가에 모의 적용 |
| v2 | session_vwap | 9717.84 | -282.16 | sell / filled / 종가 > 뉴욕 거래일별 누적 전형가격 VWAP; 조건 미충족; close=336.08, session_VWAP=337.149, session_volume=2.04555e+06; 직전 완료 봉 목표를 다음 봉 시가에 모의 적용 |
| v2 | obv_20 | 10005.55 | 5.55 | sell / filled / OBV > OBV의 SMA20 그리고 종가 > EMA26; 조건 미충족; OBV=-1.38544e+07, OBV_SMA20=-1.10099e+07, close=341.625, EMA26=338.807; 직전 완료 봉 목표를 다음 봉 시가에 모의 적용 |
| v2 | stochastic_14_3_recovery | 9574.17 | -425.83 | sell / filled / 직전 %K14 < 20에서 %K14가 %D3 상향 돌파 (한 봉 목표); 조건 미충족; K14=17.3167, D3=17.2112, previous_K14=22.2303, previous_D3=19.0146; 직전 완료 봉 목표를 다음 봉 시가에 모의 적용 |
| v2 | mfi_14_recovery | 9931.66 | -68.34 | sell / filled / 직전 MFI14 < 20, 현재 MFI14 >= 20 (한 봉 목표); 조건 미충족; MFI14=30.2719, previous_MFI14=26.8492; 직전 완료 봉 목표를 다음 봉 시가에 모의 적용 |
| v2 | adx_14_trend | 9722.79 | -277.21 | sell / filled / Wilder ADX14 >= 25 그리고 +DI14 > -DI14; 조건 미충족; ADX14=23.9395, plus_DI14=23.2021, minus_DI14=22.594; 직전 완료 봉 목표를 다음 봉 시가에 모의 적용 |
| v2 | aroon_25_trend | 9822.74 | -177.26 | sell / filled / Aroon25 Up > 70 그리고 Down < 30 (동률이면 최신 극값); 조건 미충족; Aroon_up=68, Aroon_down=16; 직전 완료 봉 목표를 다음 봉 시가에 모의 적용 |
| v2 | cci_20_momentum | 9946.56 | -53.44 | sell / filled / CCI20 > 100 (전형가격·평균절대편차); 조건 미충족; CCI20=28.4392; 직전 완료 봉 목표를 다음 봉 시가에 모의 적용 |
| v2 | williams_14_recovery | 9685.23 | -314.77 | buy / partial / 직전 Williams %R14 < -80, 현재 >= -80 (한 봉 목표); 조건 충족; Williams_R14=-67.9641, previous_R14=-82.6833; 직전 완료 봉 목표를 다음 봉 시가에 모의 적용 |
| v2 | cmf_20_accumulation | 9823.06 | -176.94 | sell / filled / Chaikin Money Flow20 > 0.1; 조건 미충족; CMF20=-0.0481318, volume20=2.57468e+06; 직전 완료 봉 목표를 다음 봉 시가에 모의 적용 |
| v2 | chaikin_3_10 | 9831.32 | -168.68 | sell / filled / ADL의 EMA3 - EMA10 > 0 그리고 종가 > EMA26; 조건 미충족; Chaikin3_10=7273.89, ADL=-1.28498e+07, close=336.08, EMA26=336.65; 직전 완료 봉 목표를 다음 봉 시가에 모의 적용 |
| v2 | roc_10_momentum | 9832.47 | -167.53 | sell / filled / 10봉 ROC > 1% 그리고 종가 > EMA26; 조건 미충족; ROC10_percent=0.964142, close=337.72, EMA26=336.695; 직전 완료 봉 목표를 다음 봉 시가에 모의 적용 |
| v2 | trix_15_trend | 9715.96 | -284.04 | sell / filled / 15봉 삼중 EMA의 1봉 변화율 TRIX > 0 그리고 종가 > EMA26; 조건 미충족; TRIX15_percent=0.0135144, close=337.6, EMA26=338.759; 직전 완료 봉 목표를 다음 봉 시가에 모의 적용 |
| v2 | keltner_20_breakout | 9901.28 | -98.72 | sell / filled / 종가 > EMA20 + 2 x Wilder ATR14; 조건 미충족; close=339.04, upper_Keltner=339.281, EMA20=336.559, ATR14=1.36146; 직전 완료 봉 목표를 다음 봉 시가에 모의 적용 |
| v2 | opening_range_30m | 9846.33 | -153.67 | sell / filled / 뉴욕 09:30·09:45 두 완료 봉 최고가를 10:00 이후 종가가 돌파; 조건 미충족; close=337.72, opening_high=339.035; 직전 완료 봉 목표를 다음 봉 시가에 모의 적용 |

### 같은 기간의 비용·노출 비교 (사후 연구)

| 전략 | 비용 전 | 비용 후 | 100% 보유 | 같은 평균 노출 보유 | 평균 노출 |
|---|---:|---:|---:|---:|---:|
| cash | 0.00% | 0.00% | 0.11% | 0.00% | 0.00% |
| buy_hold | 0.53% | 0.11% | 0.11% | 0.11% | 100.00% |
| trend_8_26 | 0.52% | -3.21% | 0.11% | 0.06% | 52.22% |
| momentum_26 | -3.14% | -10.57% | 0.11% | 0.05% | 51.17% |
| breakout_8 | -2.73% | -17.43% | 0.11% | 0.02% | 19.58% |
| reversion_12 | 5.71% | -9.50% | 0.11% | 0.03% | 25.33% |
| volume_26 | 0.29% | -5.83% | 0.11% | 0.01% | 6.79% |
| trend_8_26 AND momentum_26 | 0.56% | -4.38% | 0.11% | 0.04% | 40.99% |
| trend_8_26 + momentum_26 | -1.32% | -6.76% | 0.11% | 0.06% | 51.70% |
| trend_8_26 AND breakout_8 | -3.21% | -13.22% | 0.11% | 0.01% | 12.01% |
| trend_8_26 + breakout_8 | -1.10% | -10.21% | 0.11% | 0.04% | 35.91% |
| trend_8_26 AND reversion_12 | 2.81% | -3.46% | 0.11% | 0.01% | 7.05% |
| trend_8_26 + reversion_12 | 3.11% | -5.82% | 0.11% | 0.04% | 38.78% |
| trend_8_26 AND volume_26 | -0.37% | -3.66% | 0.11% | 0.00% | 3.66% |
| trend_8_26 + volume_26 | 0.42% | -4.52% | 0.11% | 0.03% | 29.51% |
| momentum_26 AND breakout_8 | -2.68% | -13.84% | 0.11% | 0.01% | 12.53% |
| momentum_26 + breakout_8 | -2.91% | -13.87% | 0.11% | 0.04% | 35.39% |
| momentum_26 AND reversion_12 | 2.87% | -4.62% | 0.11% | 0.01% | 7.05% |
| momentum_26 + reversion_12 | 1.22% | -8.32% | 0.11% | 0.04% | 38.26% |
| momentum_26 AND volume_26 | 0.21% | -2.70% | 0.11% | 0.00% | 2.87% |
| momentum_26 + volume_26 | -1.41% | -7.83% | 0.11% | 0.03% | 28.99% |
| breakout_8 AND reversion_12 | 0.00% | 0.00% | 0.11% | 0.00% | 0.00% |
| breakout_8 + reversion_12 | 1.43% | -12.27% | 0.11% | 0.02% | 22.46% |
| breakout_8 AND volume_26 | -0.25% | -2.32% | 0.11% | 0.00% | 1.31% |
| breakout_8 + volume_26 | -1.22% | -11.07% | 0.11% | 0.01% | 13.19% |
| reversion_12 AND volume_26 | 1.38% | -1.56% | 0.11% | 0.00% | 3.13% |
| reversion_12 + volume_26 | 2.98% | -6.71% | 0.11% | 0.02% | 16.06% |
| ema_12_26 | -0.24% | -3.54% | 0.11% | 0.06% | 51.70% |
| macd_12_26_9 | -0.13% | -4.64% | 0.11% | 0.03% | 32.64% |
| rsi_14_recovery | 0.47% | -2.03% | 0.11% | 0.00% | 1.57% |
| bollinger_20_reentry | 0.51% | -3.62% | 0.11% | 0.00% | 2.61% |
| donchian_20 | -1.81% | -5.05% | 0.11% | 0.00% | 3.13% |
| atr_14_breakout | -1.35% | -8.92% | 0.11% | 0.01% | 5.22% |
| session_vwap | 1.67% | -7.69% | 0.11% | 0.05% | 46.48% |
| obv_20 | -3.42% | -13.78% | 0.11% | 0.03% | 29.77% |
| stochastic_14_3_recovery | -1.46% | -13.13% | 0.11% | 0.01% | 7.83% |
| mfi_14_recovery | 0.32% | -2.18% | 0.11% | 0.00% | 1.57% |
| adx_14_trend | -2.43% | -4.85% | 0.11% | 0.03% | 29.50% |
| aroon_25_trend | -0.87% | -4.95% | 0.11% | 0.02% | 21.93% |
| cci_20_momentum | -2.84% | -10.67% | 0.11% | 0.02% | 16.19% |
| williams_14_recovery | -1.22% | -11.81% | 0.11% | 0.01% | 7.05% |
| cmf_20_accumulation | -1.98% | -10.63% | 0.11% | 0.03% | 30.03% |
| chaikin_3_10 | 1.01% | -7.52% | 0.11% | 0.04% | 33.68% |
| roc_10_momentum | -1.36% | -4.22% | 0.11% | 0.01% | 8.36% |
| trix_15_trend | -1.25% | -8.83% | 0.11% | 0.04% | 34.99% |
| keltner_20_breakout | -1.21% | -4.07% | 0.11% | 0.00% | 4.18% |
| opening_range_30m | -0.23% | -3.93% | 0.11% | 0.02% | 17.23% |

동일 구간·초기 자금, 종료 시 청산 비용 포함. 노출 맞춤은 사후 설명용이며 v2 실제 계좌 성과가 아닙니다.
[낙폭 분해·비용 영향·전체 구간](JPM/comparison.json)

[v1 전체 기록](JPM/accounts.json) · [v2 전체 기록](JPM/accounts-v2.json)

## XOM 계좌

| 모델 | 전략 | 평가액 USD | 손익 USD | 최근 매매·이유 |
|---|---|---:|---:|---|
| v1 | cash | 10000.00 | 0.00 | 대기 /  / 새 신호 대기 |
| v1 | buy_hold | 10045.91 | 45.91 | buy /  / buy_hold: prior completed bar target 100%; next bar open simulation |
| v1 | trend_8_26 | 9859.46 | -140.54 | buy /  / trend_8_26: prior completed bar target 100%; next bar open simulation |
| v1 | momentum_26 | 9934.85 | -65.15 | sell /  / momentum_26: prior completed bar target 0%; next bar open simulation |
| v1 | breakout_8 | 9639.65 | -360.35 | buy /  / breakout_8: prior completed bar target 100%; next bar open simulation |
| v1 | reversion_12 | 9657.92 | -342.08 | sell /  / reversion_12: prior completed bar target 0%; next bar open simulation |
| v1 | volume_26 | 9732.23 | -267.77 | sell /  / volume_26: prior completed bar target 0%; next bar open simulation |
| v1 | trend_8_26 AND momentum_26 | 9853.77 | -146.23 | sell /  / trend_8_26 AND momentum_26: prior completed bar target 0%; next bar open simulation |
| v1 | trend_8_26 + momentum_26 | 9897.17 | -102.83 | sell /  / trend_8_26 + momentum_26: prior completed bar target 50%; next bar open simulation |
| v1 | trend_8_26 AND breakout_8 | 9779.44 | -220.56 | buy /  / trend_8_26 AND breakout_8: prior completed bar target 100%; next bar open simulation |
| v1 | trend_8_26 + breakout_8 | 9768.86 | -231.14 | buy /  / trend_8_26 + breakout_8: prior completed bar target 100%; next bar open simulation |
| v1 | trend_8_26 AND reversion_12 | 9652.28 | -347.72 | sell /  / trend_8_26 AND reversion_12: prior completed bar target 0%; next bar open simulation |
| v1 | trend_8_26 + reversion_12 | 9758.11 | -241.89 | sell /  / trend_8_26 + reversion_12: prior completed bar target 50%; next bar open simulation |
| v1 | trend_8_26 AND volume_26 | 9849.16 | -150.84 | sell /  / trend_8_26 AND volume_26: prior completed bar target 0%; next bar open simulation |
| v1 | trend_8_26 + volume_26 | 9795.82 | -204.18 | sell /  / trend_8_26 + volume_26: prior completed bar target 50%; next bar open simulation |
| v1 | momentum_26 AND breakout_8 | 9801.24 | -198.76 | sell /  / momentum_26 AND breakout_8: prior completed bar target 0%; next bar open simulation |
| v1 | momentum_26 + breakout_8 | 9786.34 | -213.66 | buy /  / momentum_26 + breakout_8: prior completed bar target 50%; next bar open simulation |
| v1 | momentum_26 AND reversion_12 | 9766.58 | -233.42 | sell /  / momentum_26 AND reversion_12: prior completed bar target 0%; next bar open simulation |
| v1 | momentum_26 + reversion_12 | 9795.30 | -204.70 | sell /  / momentum_26 + reversion_12: prior completed bar target 0%; next bar open simulation |
| v1 | momentum_26 AND volume_26 | 9985.49 | -14.51 | sell /  / momentum_26 AND volume_26: prior completed bar target 0%; next bar open simulation |
| v1 | momentum_26 + volume_26 | 9833.06 | -166.94 | sell /  / momentum_26 + volume_26: prior completed bar target 0%; next bar open simulation |
| v1 | breakout_8 AND reversion_12 | 10000.00 | 0.00 | 대기 /  / 새 신호 대기 |
| v1 | breakout_8 + reversion_12 | 9648.70 | -351.30 | buy /  / breakout_8 + reversion_12: prior completed bar target 50%; next bar open simulation |
| v1 | breakout_8 AND volume_26 | 9950.44 | -49.56 | sell /  / breakout_8 AND volume_26: prior completed bar target 0%; next bar open simulation |
| v1 | breakout_8 + volume_26 | 9685.64 | -314.36 | buy /  / breakout_8 + volume_26: prior completed bar target 50%; next bar open simulation |
| v1 | reversion_12 AND volume_26 | 9840.91 | -159.09 | sell /  / reversion_12 AND volume_26: prior completed bar target 0%; next bar open simulation |
| v1 | reversion_12 + volume_26 | 9695.08 | -304.92 | sell /  / reversion_12 + volume_26: prior completed bar target 0%; next bar open simulation |
| v1 | ema_12_26 | 9973.99 | -26.01 | sell /  / EMA12 > EMA26; 조건 미충족; EMA12=177.968, EMA26=178.055 |
| v1 | macd_12_26_9 | 10064.24 | 64.24 | sell /  / MACD > 신호선 그리고 MACD > 0; 조건 미충족; MACD=0.288973, signal9=0.30355 |
| v1 | rsi_14_recovery | 9927.64 | -72.36 | sell /  / 직전 RSI14 < 30, 현재 RSI14 >= 30 (한 봉 목표); 조건 미충족; RSI14=37.639, previous_RSI14=31.1023 |
| v1 | bollinger_20_reentry | 9852.90 | -147.10 | sell /  / 직전 종가 < 직전 하단밴드, 현재 하단밴드 <= 종가 <= SMA20 (한 봉 목표); 조건 미충족; close=175.55, lower20=175.189, SMA20=177.794, previous_lower20=175.528 |
| v1 | donchian_20 | 9832.30 | -167.70 | sell /  / 종가 > 현재 봉을 제외한 직전 20봉 최고가; 조건 미충족; close=179.01, prior_high20=179.16 |
| v1 | atr_14_breakout | 9864.96 | -135.04 | sell /  / 종가 > 직전 종가 + 직전 ATR14 그리고 종가 > EMA26; 조건 미충족; close=177.19, threshold=177.748, prior_ATR14=0.663113, EMA26=175.734 |
| v1 | session_vwap | 9998.17 | -1.83 | buy /  / 종가 > 뉴욕 거래일별 누적 전형가격 VWAP; 조건 충족; close=176.885, session_VWAP=176.63, session_volume=5.45281e+06 |
| v1 | obv_20 | 9799.44 | -200.56 | buy /  / OBV > OBV의 SMA20 그리고 종가 > EMA26; 조건 충족; OBV=2.03094e+07, OBV_SMA20=1.963e+07, close=177.36, EMA26=177.099 |
| v1 | stochastic_14_3_recovery | 9721.31 | -278.69 | sell /  / 직전 %K14 < 20에서 %K14가 %D3 상향 돌파 (한 봉 목표); 조건 미충족; K14=29.2797, D3=21.8586, previous_K14=22.3575, previous_D3=16.0588 |
| v1 | mfi_14_recovery | 10000.00 | 0.00 | 대기 /  / 새 신호 대기 |
| v1 | adx_14_trend | 9999.47 | -0.53 | sell /  / Wilder ADX14 >= 25 그리고 +DI14 > -DI14; 조건 미충족; ADX14=23.8302, plus_DI14=25.6436, minus_DI14=22.6035 |
| v1 | aroon_25_trend | 9754.76 | -245.24 | sell /  / Aroon25 Up > 70 그리고 Down < 30 (동률이면 최신 극값); 조건 미충족; Aroon_up=88, Aroon_down=100 |
| v1 | cci_20_momentum | 9743.77 | -256.23 | sell /  / CCI20 > 100 (전형가격·평균절대편차); 조건 미충족; CCI20=96.5349 |
| v1 | williams_14_recovery | 9653.59 | -346.41 | sell /  / 직전 Williams %R14 < -80, 현재 >= -80 (한 봉 목표); 조건 미충족; Williams_R14=-70.7203, previous_R14=-77.6425 |
| v1 | cmf_20_accumulation | 9966.29 | -33.71 | sell /  / Chaikin Money Flow20 > 0.1; 조건 미충족; CMF20=0.0744325, volume20=5.28871e+06 |
| v1 | chaikin_3_10 | 9906.62 | -93.38 | buy /  / ADL의 EMA3 - EMA10 > 0 그리고 종가 > EMA26; 조건 충족; Chaikin3_10=98311.7, ADL=2.44104e+07, close=177.36, EMA26=177.099 |
| v1 | roc_10_momentum | 9940.60 | -59.40 | sell /  / 10봉 ROC > 1% 그리고 종가 > EMA26; 조건 미충족; ROC10_percent=0.782107, close=178.47, EMA26=176.891 |
| v1 | trix_15_trend | 9952.41 | -47.59 | sell /  / 15봉 삼중 EMA의 1봉 변화율 TRIX > 0 그리고 종가 > EMA26; 조건 미충족; TRIX15_percent=0.0212551, close=178.14, EMA26=178.249 |
| v1 | keltner_20_breakout | 9937.30 | -62.70 | sell /  / 종가 > EMA20 + 2 x Wilder ATR14; 조건 미충족; close=178.845, upper_Keltner=179.079, EMA20=177.884, ATR14=0.597175 |
| v1 | opening_range_30m | 10049.37 | 49.37 | sell /  / 뉴욕 09:30·09:45 두 완료 봉 최고가를 10:00 이후 종가가 돌파; 자료 부족·변동폭 또는 거래량 없음: 대기; close=179.01 |
| v2 | cash | 10000.00 | 0.00 | 대기 /  / 새 신호 대기 |
| v2 | buy_hold | 10366.50 | 366.50 | buy / partial / 직전 완료 봉 목표 비중 100%; 다음 봉 시가 가정 |
| v2 | trend_8_26 | 9949.39 | -50.61 | buy / partial / 직전 완료 봉 목표 비중 100%; 다음 봉 시가 가정 |
| v2 | momentum_26 | 10102.33 | 102.33 | sell / filled / 직전 완료 봉 목표 비중 0%; 다음 봉 시가 가정 |
| v2 | breakout_8 | 9108.76 | -891.24 | buy / partial / 직전 완료 봉 목표 비중 100%; 다음 봉 시가 가정 |
| v2 | reversion_12 | 9475.52 | -524.48 | sell / filled / 직전 완료 봉 목표 비중 0%; 다음 봉 시가 가정 |
| v2 | volume_26 | 9635.02 | -364.98 | sell / filled / 직전 완료 봉 목표 비중 0%; 다음 봉 시가 가정 |
| v2 | trend_8_26 AND momentum_26 | 9950.02 | -49.98 | sell / filled / 직전 완료 봉 목표 비중 0%; 다음 봉 시가 가정 |
| v2 | trend_8_26 + momentum_26 | 10025.67 | 25.67 | sell / filled / 직전 완료 봉 목표 비중 50%; 다음 봉 시가 가정 |
| v2 | trend_8_26 AND breakout_8 | 9231.36 | -768.64 | buy / partial / 직전 완료 봉 목표 비중 100%; 다음 봉 시가 가정 |
| v2 | trend_8_26 + breakout_8 | 9560.62 | -439.38 | buy / partial / 직전 완료 봉 목표 비중 100%; 다음 봉 시가 가정 |
| v2 | trend_8_26 AND reversion_12 | 9493.76 | -506.24 | sell / filled / 직전 완료 봉 목표 비중 0%; 다음 봉 시가 가정 |
| v2 | trend_8_26 + reversion_12 | 9709.58 | -290.42 | sell / filled / 직전 완료 봉 목표 비중 50%; 다음 봉 시가 가정 |
| v2 | trend_8_26 AND volume_26 | 9742.44 | -257.56 | sell / filled / 직전 완료 봉 목표 비중 0%; 다음 봉 시가 가정 |
| v2 | trend_8_26 + volume_26 | 9791.07 | -208.93 | sell / filled / 직전 완료 봉 목표 비중 50%; 다음 봉 시가 가정 |
| v2 | momentum_26 AND breakout_8 | 9269.79 | -730.21 | sell / filled / 직전 완료 봉 목표 비중 0%; 다음 봉 시가 가정 |
| v2 | momentum_26 + breakout_8 | 9593.41 | -406.59 | buy / filled / 직전 완료 봉 목표 비중 50%; 다음 봉 시가 가정 |
| v2 | momentum_26 AND reversion_12 | 9567.55 | -432.45 | sell / filled / 직전 완료 봉 목표 비중 0%; 다음 봉 시가 가정 |
| v2 | momentum_26 + reversion_12 | 9783.90 | -216.10 | sell / filled / 직전 완료 봉 목표 비중 0%; 다음 봉 시가 가정 |
| v2 | momentum_26 AND volume_26 | 9941.52 | -58.48 | sell / filled / 직전 완료 봉 목표 비중 0%; 다음 봉 시가 가정 |
| v2 | momentum_26 + volume_26 | 9886.61 | -113.39 | sell / filled / 직전 완료 봉 목표 비중 0%; 다음 봉 시가 가정 |
| v2 | breakout_8 AND reversion_12 | 10000.00 | 0.00 | 대기 /  / 새 신호 대기 |
| v2 | breakout_8 + reversion_12 | 9290.13 | -709.87 | buy / filled / 직전 완료 봉 목표 비중 50%; 다음 봉 시가 가정 |
| v2 | breakout_8 AND volume_26 | 9918.86 | -81.14 | sell / filled / 직전 완료 봉 목표 비중 0%; 다음 봉 시가 가정 |
| v2 | breakout_8 + volume_26 | 9387.59 | -612.41 | buy / filled / 직전 완료 봉 목표 비중 50%; 다음 봉 시가 가정 |
| v2 | reversion_12 AND volume_26 | 9787.67 | -212.33 | sell / filled / 직전 완료 봉 목표 비중 0%; 다음 봉 시가 가정 |
| v2 | reversion_12 + volume_26 | 9575.11 | -424.89 | sell / filled / 직전 완료 봉 목표 비중 0%; 다음 봉 시가 가정 |
| v2 | ema_12_26 | 9971.99 | -28.01 | sell / filled / EMA12 > EMA26; 조건 미충족; EMA12=177.968, EMA26=178.055; 직전 완료 봉 목표를 다음 봉 시가에 모의 적용 |
| v2 | macd_12_26_9 | 10060.21 | 60.21 | sell / filled / MACD > 신호선 그리고 MACD > 0; 조건 미충족; MACD=0.288973, signal9=0.30355; 직전 완료 봉 목표를 다음 봉 시가에 모의 적용 |
| v2 | rsi_14_recovery | 9923.67 | -76.33 | sell / filled / 직전 RSI14 < 30, 현재 RSI14 >= 30 (한 봉 목표); 조건 미충족; RSI14=37.639, previous_RSI14=31.1023; 직전 완료 봉 목표를 다음 봉 시가에 모의 적용 |
| v2 | bollinger_20_reentry | 9848.96 | -151.04 | sell / filled / 직전 종가 < 직전 하단밴드, 현재 하단밴드 <= 종가 <= SMA20 (한 봉 목표); 조건 미충족; close=175.55, lower20=175.189, SMA20=177.794, previous_lower20=175.528; 직전 완료 봉 목표를 다음 봉 시가에 모의 적용 |
| v2 | donchian_20 | 9824.43 | -175.57 | sell / filled / 종가 > 현재 봉을 제외한 직전 20봉 최고가; 조건 미충족; close=179.01, prior_high20=179.16; 직전 완료 봉 목표를 다음 봉 시가에 모의 적용 |
| v2 | atr_14_breakout | 9859.04 | -140.96 | sell / filled / 종가 > 직전 종가 + 직전 ATR14 그리고 종가 > EMA26; 조건 미충족; close=177.19, threshold=177.748, prior_ATR14=0.663113, EMA26=175.734; 직전 완료 봉 목표를 다음 봉 시가에 모의 적용 |
| v2 | session_vwap | 9991.18 | -8.82 | buy / partial / 종가 > 뉴욕 거래일별 누적 전형가격 VWAP; 조건 충족; close=176.885, session_VWAP=176.63, session_volume=5.45281e+06; 직전 완료 봉 목표를 다음 봉 시가에 모의 적용 |
| v2 | obv_20 | 9786.71 | -213.29 | buy / partial / OBV > OBV의 SMA20 그리고 종가 > EMA26; 조건 충족; OBV=2.03094e+07, OBV_SMA20=1.963e+07, close=177.36, EMA26=177.099; 직전 완료 봉 목표를 다음 봉 시가에 모의 적용 |
| v2 | stochastic_14_3_recovery | 9711.59 | -288.41 | sell / filled / 직전 %K14 < 20에서 %K14가 %D3 상향 돌파 (한 봉 목표); 조건 미충족; K14=29.2797, D3=21.8586, previous_K14=22.3575, previous_D3=16.0588; 직전 완료 봉 목표를 다음 봉 시가에 모의 적용 |
| v2 | mfi_14_recovery | 10000.00 | 0.00 | 대기 /  / 새 신호 대기 |
| v2 | adx_14_trend | 9993.47 | -6.53 | sell / filled / Wilder ADX14 >= 25 그리고 +DI14 > -DI14; 조건 미충족; ADX14=23.8302, plus_DI14=25.6436, minus_DI14=22.6035; 직전 완료 봉 목표를 다음 봉 시가에 모의 적용 |
| v2 | aroon_25_trend | 9750.86 | -249.14 | sell / filled / Aroon25 Up > 70 그리고 Down < 30 (동률이면 최신 극값); 조건 미충족; Aroon_up=88, Aroon_down=100; 직전 완료 봉 목표를 다음 봉 시가에 모의 적용 |
| v2 | cci_20_momentum | 9730.14 | -269.86 | sell / filled / CCI20 > 100 (전형가격·평균절대편차); 조건 미충족; CCI20=96.5349; 직전 완료 봉 목표를 다음 봉 시가에 모의 적용 |
| v2 | williams_14_recovery | 9643.94 | -356.06 | sell / filled / 직전 Williams %R14 < -80, 현재 >= -80 (한 봉 목표); 조건 미충족; Williams_R14=-70.7203, previous_R14=-77.6425; 직전 완료 봉 목표를 다음 봉 시가에 모의 적용 |
| v2 | cmf_20_accumulation | 9962.31 | -37.69 | sell / filled / Chaikin Money Flow20 > 0.1; 조건 미충족; CMF20=0.0744325, volume20=5.28871e+06; 직전 완료 봉 목표를 다음 봉 시가에 모의 적용 |
| v2 | chaikin_3_10 | 9897.71 | -102.29 | buy / partial / ADL의 EMA3 - EMA10 > 0 그리고 종가 > EMA26; 조건 충족; Chaikin3_10=98311.7, ADL=2.44104e+07, close=177.36, EMA26=177.099; 직전 완료 봉 목표를 다음 봉 시가에 모의 적용 |
| v2 | roc_10_momentum | 9934.64 | -65.36 | sell / filled / 10봉 ROC > 1% 그리고 종가 > EMA26; 조건 미충족; ROC10_percent=0.782107, close=178.47, EMA26=176.891; 직전 완료 봉 목표를 다음 봉 시가에 모의 적용 |
| v2 | trix_15_trend | 9946.44 | -53.56 | sell / filled / 15봉 삼중 EMA의 1봉 변화율 TRIX > 0 그리고 종가 > EMA26; 조건 미충족; TRIX15_percent=0.0212551, close=178.14, EMA26=178.249; 직전 완료 봉 목표를 다음 봉 시가에 모의 적용 |
| v2 | keltner_20_breakout | 9931.34 | -68.66 | sell / filled / 종가 > EMA20 + 2 x Wilder ATR14; 조건 미충족; close=178.845, upper_Keltner=179.079, EMA20=177.884, ATR14=0.597175; 직전 완료 봉 목표를 다음 봉 시가에 모의 적용 |
| v2 | opening_range_30m | 10047.36 | 47.36 | sell / filled / 뉴욕 09:30·09:45 두 완료 봉 최고가를 10:00 이후 종가가 돌파; 자료 부족·변동폭 또는 거래량 없음: 대기; close=179.01; 직전 완료 봉 목표를 다음 봉 시가에 모의 적용 |

### 같은 기간의 비용·노출 비교 (사후 연구)

| 전략 | 비용 전 | 비용 후 | 100% 보유 | 같은 평균 노출 보유 | 평균 노출 |
|---|---:|---:|---:|---:|---:|
| cash | 0.00% | 0.00% | 8.66% | 0.00% | 0.00% |
| buy_hold | 9.12% | 8.66% | 8.66% | 8.66% | 100.00% |
| trend_8_26 | 1.36% | -3.62% | 8.66% | 5.87% | 68.67% |
| momentum_26 | 2.01% | -5.02% | 8.66% | 6.19% | 72.32% |
| breakout_8 | -0.01% | -19.29% | 8.66% | 2.37% | 28.20% |
| reversion_12 | 2.68% | -6.77% | 8.66% | 1.75% | 20.89% |
| volume_26 | 2.21% | -5.23% | 8.66% | 0.43% | 5.22% |
| trend_8_26 AND momentum_26 | 0.05% | -5.27% | 8.66% | 5.23% | 61.36% |
| trend_8_26 + momentum_26 | 1.69% | -4.12% | 8.66% | 6.03% | 70.50% |
| trend_8_26 AND breakout_8 | 0.15% | -15.69% | 8.66% | 1.84% | 21.93% |
| trend_8_26 + breakout_8 | 0.70% | -11.42% | 8.66% | 4.11% | 48.44% |
| trend_8_26 AND reversion_12 | -1.96% | -7.56% | 8.66% | 0.83% | 9.92% |
| trend_8_26 + reversion_12 | 2.05% | -5.01% | 8.66% | 3.79% | 44.78% |
| trend_8_26 AND volume_26 | 1.38% | -3.20% | 8.66% | 0.26% | 3.13% |
| trend_8_26 + volume_26 | 1.81% | -4.23% | 8.66% | 3.12% | 36.95% |
| momentum_26 AND breakout_8 | -0.39% | -17.55% | 8.66% | 2.10% | 25.07% |
| momentum_26 + breakout_8 | 1.02% | -12.43% | 8.66% | 4.26% | 50.27% |
| momentum_26 AND reversion_12 | -0.44% | -6.91% | 8.66% | 0.85% | 10.18% |
| momentum_26 + reversion_12 | 2.37% | -4.71% | 8.66% | 3.95% | 46.61% |
| momentum_26 AND volume_26 | 2.15% | -1.64% | 8.66% | 0.20% | 2.35% |
| momentum_26 + volume_26 | 2.14% | -4.12% | 8.66% | 3.27% | 38.78% |
| breakout_8 AND reversion_12 | 0.00% | 0.00% | 8.66% | 0.00% | 0.00% |
| breakout_8 + reversion_12 | 1.34% | -13.08% | 8.66% | 2.06% | 24.55% |
| breakout_8 AND volume_26 | 0.51% | -1.17% | 8.66% | 0.09% | 1.04% |
| breakout_8 + volume_26 | 1.10% | -11.81% | 8.66% | 1.40% | 16.72% |
| reversion_12 AND volume_26 | 0.29% | -2.62% | 8.66% | 0.17% | 2.09% |
| reversion_12 + volume_26 | 2.47% | -5.21% | 8.66% | 1.09% | 13.06% |
| ema_12_26 | 1.30% | -1.63% | 8.66% | 6.68% | 77.81% |
| macd_12_26_9 | 0.41% | -5.33% | 8.66% | 3.58% | 42.30% |
| rsi_14_recovery | -0.08% | -1.33% | 8.66% | 0.07% | 0.78% |
| bollinger_20_reentry | -1.07% | -3.94% | 8.66% | 0.15% | 1.83% |
| donchian_20 | -1.08% | -10.19% | 8.66% | 0.78% | 9.40% |
| atr_14_breakout | 0.54% | -7.17% | 8.66% | 0.43% | 5.22% |
| session_vwap | 2.01% | -8.16% | 8.66% | 5.73% | 67.10% |
| obv_20 | 2.71% | -6.74% | 8.66% | 4.23% | 49.87% |
| stochastic_14_3_recovery | 0.79% | -8.49% | 8.66% | 0.50% | 6.01% |
| mfi_14_recovery | -0.31% | -1.97% | 8.66% | 0.09% | 1.04% |
| adx_14_trend | 3.83% | 0.83% | 8.66% | 3.62% | 42.82% |
| aroon_25_trend | -3.46% | -9.74% | 8.66% | 2.90% | 34.46% |
| cci_20_momentum | 3.49% | -5.64% | 8.66% | 2.33% | 27.68% |
| williams_14_recovery | -0.90% | -6.95% | 8.66% | 0.33% | 3.92% |
| cmf_20_accumulation | 0.87% | -5.68% | 8.66% | 4.05% | 47.78% |
| chaikin_3_10 | 1.87% | -6.73% | 8.66% | 5.11% | 60.05% |
| roc_10_momentum | 1.03% | -4.74% | 8.66% | 1.07% | 12.79% |
| trix_15_trend | 1.02% | -5.15% | 8.66% | 5.66% | 66.32% |
| keltner_20_breakout | 0.45% | -6.08% | 8.66% | 1.40% | 16.71% |
| opening_range_30m | -0.22% | -9.03% | 8.66% | 2.86% | 33.94% |

동일 구간·초기 자금, 종료 시 청산 비용 포함. 노출 맞춤은 사후 설명용이며 v2 실제 계좌 성과가 아닙니다.
[낙폭 분해·비용 영향·전체 구간](XOM/comparison.json)

[v1 전체 기록](XOM/accounts.json) · [v2 전체 기록](XOM/accounts-v2.json)

## JNJ 계좌

| 모델 | 전략 | 평가액 USD | 손익 USD | 최근 매매·이유 |
|---|---|---:|---:|---|
| v1 | cash | 10000.00 | 0.00 | 대기 /  / 새 신호 대기 |
| v1 | buy_hold | 10125.91 | 125.91 | buy /  / buy_hold: prior completed bar target 100%; next bar open simulation |
| v1 | trend_8_26 | 10077.23 | 77.23 | buy /  / trend_8_26: prior completed bar target 100%; next bar open simulation |
| v1 | momentum_26 | 9847.74 | -152.26 | buy /  / momentum_26: prior completed bar target 100%; next bar open simulation |
| v1 | breakout_8 | 9466.25 | -533.75 | sell /  / breakout_8: prior completed bar target 0%; next bar open simulation |
| v1 | reversion_12 | 9851.38 | -148.62 | buy /  / reversion_12: prior completed bar target 100%; next bar open simulation |
| v1 | volume_26 | 9943.90 | -56.10 | sell /  / volume_26: prior completed bar target 0%; next bar open simulation |
| v1 | trend_8_26 AND momentum_26 | 9899.72 | -100.28 | buy /  / trend_8_26 AND momentum_26: prior completed bar target 100%; next bar open simulation |
| v1 | trend_8_26 + momentum_26 | 9962.12 | -37.88 | buy /  / trend_8_26 + momentum_26: prior completed bar target 100%; next bar open simulation |
| v1 | trend_8_26 AND breakout_8 | 9765.55 | -234.45 | sell /  / trend_8_26 AND breakout_8: prior completed bar target 0%; next bar open simulation |
| v1 | trend_8_26 + breakout_8 | 9786.75 | -213.25 | buy /  / trend_8_26 + breakout_8: prior completed bar target 50%; next bar open simulation |
| v1 | trend_8_26 AND reversion_12 | 9951.42 | -48.58 | buy /  / trend_8_26 AND reversion_12: prior completed bar target 100%; next bar open simulation |
| v1 | trend_8_26 + reversion_12 | 9963.77 | -36.23 | buy /  / trend_8_26 + reversion_12: prior completed bar target 100%; next bar open simulation |
| v1 | trend_8_26 AND volume_26 | 9995.12 | -4.88 | sell /  / trend_8_26 AND volume_26: prior completed bar target 0%; next bar open simulation |
| v1 | trend_8_26 + volume_26 | 10010.54 | 10.54 | buy /  / trend_8_26 + volume_26: prior completed bar target 50%; next bar open simulation |
| v1 | momentum_26 AND breakout_8 | 9784.22 | -215.78 | sell /  / momentum_26 AND breakout_8: prior completed bar target 0%; next bar open simulation |
| v1 | momentum_26 + breakout_8 | 9654.96 | -345.04 | buy /  / momentum_26 + breakout_8: prior completed bar target 50%; next bar open simulation |
| v1 | momentum_26 AND reversion_12 | 9959.38 | -40.62 | buy /  / momentum_26 AND reversion_12: prior completed bar target 100%; next bar open simulation |
| v1 | momentum_26 + reversion_12 | 9869.13 | -130.87 | buy /  / momentum_26 + reversion_12: prior completed bar target 100%; next bar open simulation |
| v1 | momentum_26 AND volume_26 | 10000.00 | 0.00 | 대기 /  / 새 신호 대기 |
| v1 | momentum_26 + volume_26 | 9935.35 | -64.65 | buy /  / momentum_26 + volume_26: prior completed bar target 50%; next bar open simulation |
| v1 | breakout_8 AND reversion_12 | 10000.00 | 0.00 | 대기 /  / 새 신호 대기 |
| v1 | breakout_8 + reversion_12 | 9656.69 | -343.31 | buy /  / breakout_8 + reversion_12: prior completed bar target 50%; next bar open simulation |
| v1 | breakout_8 AND volume_26 | 10000.00 | 0.00 | 대기 /  / 새 신호 대기 |
| v1 | breakout_8 + volume_26 | 9721.53 | -278.47 | sell /  / breakout_8 + volume_26: prior completed bar target 0%; next bar open simulation |
| v1 | reversion_12 AND volume_26 | 9974.59 | -25.41 | sell /  / reversion_12 AND volume_26: prior completed bar target 0%; next bar open simulation |
| v1 | reversion_12 + volume_26 | 9917.37 | -82.63 | buy /  / reversion_12 + volume_26: prior completed bar target 50%; next bar open simulation |
| v1 | ema_12_26 | 9946.42 | -53.58 | buy /  / EMA12 > EMA26; 조건 충족; EMA12=253.915, EMA26=253.911 |
| v1 | macd_12_26_9 | 9887.47 | -112.53 | sell /  / MACD > 신호선 그리고 MACD > 0; 조건 미충족; MACD=1.30676, signal9=1.31668 |
| v1 | rsi_14_recovery | 9923.04 | -76.96 | sell /  / 직전 RSI14 < 30, 현재 RSI14 >= 30 (한 봉 목표); 조건 미충족; RSI14=40.3665, previous_RSI14=36.2025 |
| v1 | bollinger_20_reentry | 9881.04 | -118.96 | sell /  / 직전 종가 < 직전 하단밴드, 현재 하단밴드 <= 종가 <= SMA20 (한 봉 목표); 조건 미충족; close=251.75, lower20=251.316, SMA20=254.208, previous_lower20=251.691 |
| v1 | donchian_20 | 9921.02 | -78.98 | sell /  / 종가 > 현재 봉을 제외한 직전 20봉 최고가; 조건 미충족; close=258.68, prior_high20=260.425 |
| v1 | atr_14_breakout | 9805.90 | -194.10 | sell /  / 종가 > 직전 종가 + 직전 ATR14 그리고 종가 > EMA26; 조건 미충족; close=258.68, threshold=261.221, prior_ATR14=1.00083, EMA26=254.754 |
| v1 | session_vwap | 9753.99 | -246.01 | sell /  / 종가 > 뉴욕 거래일별 누적 전형가격 VWAP; 조건 미충족; close=258.78, session_VWAP=259.361, session_volume=5.7456e+06 |
| v1 | obv_20 | 9582.81 | -417.19 | sell /  / OBV > OBV의 SMA20 그리고 종가 > EMA26; 조건 미충족; OBV=6.96995e+06, OBV_SMA20=7.15756e+06, close=258.36, EMA26=258.335 |
| v1 | stochastic_14_3_recovery | 9802.06 | -197.94 | sell /  / 직전 %K14 < 20에서 %K14가 %D3 상향 돌파 (한 봉 목표); 조건 미충족; K14=1.94019, D3=16.0903, previous_K14=30.2239, previous_D3=19.4628 |
| v1 | mfi_14_recovery | 10000.00 | 0.00 | 대기 /  / 새 신호 대기 |
| v1 | adx_14_trend | 9806.44 | -193.56 | buy /  / Wilder ADX14 >= 25 그리고 +DI14 > -DI14; 조건 충족; ADX14=27.0884, plus_DI14=47.0278, minus_DI14=11.4099 |
| v1 | aroon_25_trend | 9899.46 | -100.54 | sell /  / Aroon25 Up > 70 그리고 Down < 30 (동률이면 최신 극값); 조건 미충족; Aroon_up=68, Aroon_down=44 |
| v1 | cci_20_momentum | 9818.66 | -181.34 | sell /  / CCI20 > 100 (전형가격·평균절대편차); 조건 미충족; CCI20=95.1073 |
| v1 | williams_14_recovery | 9842.61 | -157.39 | sell /  / 직전 Williams %R14 < -80, 현재 >= -80 (한 봉 목표); 조건 미충족; Williams_R14=-98.0598, previous_R14=-69.7761 |
| v1 | cmf_20_accumulation | 10209.61 | 209.61 | buy /  / Chaikin Money Flow20 > 0.1; 조건 충족; CMF20=0.172643, volume20=5.45882e+06 |
| v1 | chaikin_3_10 | 9898.53 | -101.47 | buy /  / ADL의 EMA3 - EMA10 > 0 그리고 종가 > EMA26; 조건 충족; Chaikin3_10=250777, ADL=4.30146e+06, close=254.04, EMA26=253.978 |
| v1 | roc_10_momentum | 9691.76 | -308.24 | sell /  / 10봉 ROC > 1% 그리고 종가 > EMA26; 조건 미충족; ROC10_percent=-0.503419, close=258.91, EMA26=257.09 |
| v1 | trix_15_trend | 9789.95 | -210.05 | buy /  / 15봉 삼중 EMA의 1봉 변화율 TRIX > 0 그리고 종가 > EMA26; 조건 충족; TRIX15_percent=0.000945132, close=260.22, EMA26=254.44 |
| v1 | keltner_20_breakout | 9916.04 | -83.96 | sell /  / 종가 > EMA20 + 2 x Wilder ATR14; 조건 미충족; close=258.91, upper_Keltner=259.564, EMA20=257.603, ATR14=0.980686 |
| v1 | opening_range_30m | 10000.00 | 0.00 | 대기 /  / 새 신호 대기 |
| v2 | cash | 10000.00 | 0.00 | 대기 /  / 새 신호 대기 |
| v2 | buy_hold | 9889.58 | -110.42 | 중단: 손실 한도 / buy / partial / 직전 완료 봉 목표 비중 100%; 다음 봉 시가 가정 |
| v2 | trend_8_26 | 9889.58 | -110.42 | 중단: 손실 한도 / buy / partial / 직전 완료 봉 목표 비중 100%; 다음 봉 시가 가정 |
| v2 | momentum_26 | 9889.58 | -110.42 | 중단: 손실 한도 / buy / partial / 직전 완료 봉 목표 비중 100%; 다음 봉 시가 가정 |
| v2 | breakout_8 | 9343.39 | -656.61 | 중단: 손실 한도 / sell / filled / 직전 완료 봉 목표 비중 0%; 다음 봉 시가 가정 |
| v2 | reversion_12 | 9537.55 | -462.45 | buy / partial / 직전 완료 봉 목표 비중 100%; 다음 봉 시가 가정 |
| v2 | volume_26 | 9728.64 | -271.36 | sell / filled / 직전 완료 봉 목표 비중 0%; 다음 봉 시가 가정 |
| v2 | trend_8_26 AND momentum_26 | 9889.58 | -110.42 | 중단: 손실 한도 / buy / partial / 직전 완료 봉 목표 비중 100%; 다음 봉 시가 가정 |
| v2 | trend_8_26 + momentum_26 | 9889.58 | -110.42 | 중단: 손실 한도 / buy / partial / 직전 완료 봉 목표 비중 100%; 다음 봉 시가 가정 |
| v2 | trend_8_26 AND breakout_8 | 9419.39 | -580.61 | 중단: 손실 한도 / sell / filled / 직전 완료 봉 목표 비중 0%; 다음 봉 시가 가정 |
| v2 | trend_8_26 + breakout_8 | 9355.89 | -644.11 | buy / filled / 직전 완료 봉 목표 비중 50%; 다음 봉 시가 가정 |
| v2 | trend_8_26 AND reversion_12 | 9922.67 | -77.33 | buy / partial / 직전 완료 봉 목표 비중 100%; 다음 봉 시가 가정 |
| v2 | trend_8_26 + reversion_12 | 9732.92 | -267.08 | 중단: 손실 한도 / sell / filled / 직전 완료 봉 목표 비중 0%; 다음 봉 시가 가정 |
| v2 | trend_8_26 AND volume_26 | 9861.95 | -138.05 | sell / filled / 직전 완료 봉 목표 비중 0%; 다음 봉 시가 가정 |
| v2 | trend_8_26 + volume_26 | 9919.80 | -80.20 | 중단: 손실 한도 / buy / filled / 직전 완료 봉 목표 비중 50%; 다음 봉 시가 가정 |
| v2 | momentum_26 AND breakout_8 | 9385.94 | -614.06 | sell / filled / 직전 완료 봉 목표 비중 0%; 다음 봉 시가 가정 |
| v2 | momentum_26 + breakout_8 | 9220.31 | -779.69 | buy / filled / 직전 완료 봉 목표 비중 50%; 다음 봉 시가 가정 |
| v2 | momentum_26 AND reversion_12 | 9893.55 | -106.45 | buy / partial / 직전 완료 봉 목표 비중 100%; 다음 봉 시가 가정 |
| v2 | momentum_26 + reversion_12 | 9732.92 | -267.08 | 중단: 손실 한도 / sell / filled / 직전 완료 봉 목표 비중 0%; 다음 봉 시가 가정 |
| v2 | momentum_26 AND volume_26 | 9920.93 | -79.07 | sell / filled / 직전 완료 봉 목표 비중 0%; 다음 봉 시가 가정 |
| v2 | momentum_26 + volume_26 | 9919.80 | -80.20 | 중단: 손실 한도 / buy / filled / 직전 완료 봉 목표 비중 50%; 다음 봉 시가 가정 |
| v2 | breakout_8 AND reversion_12 | 10000.00 | 0.00 | 대기 /  / 새 신호 대기 |
| v2 | breakout_8 + reversion_12 | 9238.71 | -761.29 | buy / filled / 직전 완료 봉 목표 비중 50%; 다음 봉 시가 가정 |
| v2 | breakout_8 AND volume_26 | 9814.17 | -185.83 | sell / filled / 직전 완료 봉 목표 비중 0%; 다음 봉 시가 가정 |
| v2 | breakout_8 + volume_26 | 9330.90 | -669.10 | sell / filled / 직전 완료 봉 목표 비중 0%; 다음 봉 시가 가정 |
| v2 | reversion_12 AND volume_26 | 9859.15 | -140.85 | sell / filled / 직전 완료 봉 목표 비중 0%; 다음 봉 시가 가정 |
| v2 | reversion_12 + volume_26 | 9673.42 | -326.58 | buy / filled / 직전 완료 봉 목표 비중 50%; 다음 봉 시가 가정 |
| v2 | ema_12_26 | 9941.45 | -58.55 | buy / partial / EMA12 > EMA26; 조건 충족; EMA12=253.915, EMA26=253.911; 직전 완료 봉 목표를 다음 봉 시가에 모의 적용 |
| v2 | macd_12_26_9 | 9881.54 | -118.46 | sell / filled / MACD > 신호선 그리고 MACD > 0; 조건 미충족; MACD=1.30676, signal9=1.31668; 직전 완료 봉 목표를 다음 봉 시가에 모의 적용 |
| v2 | rsi_14_recovery | 9919.07 | -80.93 | sell / filled / 직전 RSI14 < 30, 현재 RSI14 >= 30 (한 봉 목표); 조건 미충족; RSI14=40.3665, previous_RSI14=36.2025; 직전 완료 봉 목표를 다음 봉 시가에 모의 적용 |
| v2 | bollinger_20_reentry | 9877.09 | -122.91 | sell / filled / 직전 종가 < 직전 하단밴드, 현재 하단밴드 <= 종가 <= SMA20 (한 봉 목표); 조건 미충족; close=251.75, lower20=251.316, SMA20=254.208, previous_lower20=251.691; 직전 완료 봉 목표를 다음 봉 시가에 모의 적용 |
| v2 | donchian_20 | 9919.03 | -80.97 | sell / filled / 종가 > 현재 봉을 제외한 직전 20봉 최고가; 조건 미충족; close=258.68, prior_high20=260.425; 직전 완료 봉 목표를 다음 봉 시가에 모의 적용 |
| v2 | atr_14_breakout | 9800.02 | -199.98 | sell / filled / 종가 > 직전 종가 + 직전 ATR14 그리고 종가 > EMA26; 조건 미충족; close=258.68, threshold=261.221, prior_ATR14=1.00083, EMA26=254.754; 직전 완료 봉 목표를 다음 봉 시가에 모의 적용 |
| v2 | session_vwap | 9738.40 | -261.60 | sell / filled / 종가 > 뉴욕 거래일별 누적 전형가격 VWAP; 조건 미충족; close=258.78, session_VWAP=259.361, session_volume=5.7456e+06; 직전 완료 봉 목표를 다음 봉 시가에 모의 적용 |
| v2 | obv_20 | 9567.49 | -432.51 | sell / filled / OBV > OBV의 SMA20 그리고 종가 > EMA26; 조건 미충족; OBV=6.96995e+06, OBV_SMA20=7.15756e+06, close=258.36, EMA26=258.335; 직전 완료 봉 목표를 다음 봉 시가에 모의 적용 |
| v2 | stochastic_14_3_recovery | 9794.23 | -205.77 | sell / filled / 직전 %K14 < 20에서 %K14가 %D3 상향 돌파 (한 봉 목표); 조건 미충족; K14=1.94019, D3=16.0903, previous_K14=30.2239, previous_D3=19.4628; 직전 완료 봉 목표를 다음 봉 시가에 모의 적용 |
| v2 | mfi_14_recovery | 10000.00 | 0.00 | 대기 /  / 새 신호 대기 |
| v2 | adx_14_trend | 9799.58 | -200.42 | buy / partial / Wilder ADX14 >= 25 그리고 +DI14 > -DI14; 조건 충족; ADX14=27.0884, plus_DI14=47.0278, minus_DI14=11.4099; 직전 완료 봉 목표를 다음 봉 시가에 모의 적용 |
| v2 | aroon_25_trend | 9895.50 | -104.50 | sell / filled / Aroon25 Up > 70 그리고 Down < 30 (동률이면 최신 극값); 조건 미충족; Aroon_up=68, Aroon_down=44; 직전 완료 봉 목표를 다음 봉 시가에 모의 적용 |
| v2 | cci_20_momentum | 9812.77 | -187.23 | sell / filled / CCI20 > 100 (전형가격·평균절대편차); 조건 미충족; CCI20=95.1073; 직전 완료 봉 목표를 다음 봉 시가에 모의 적용 |
| v2 | williams_14_recovery | 9836.70 | -163.30 | sell / filled / 직전 Williams %R14 < -80, 현재 >= -80 (한 봉 목표); 조건 미충족; Williams_R14=-98.0598, previous_R14=-69.7761; 직전 완료 봉 목표를 다음 봉 시가에 모의 적용 |
| v2 | cmf_20_accumulation | 10206.55 | 206.55 | buy / partial / Chaikin Money Flow20 > 0.1; 조건 충족; CMF20=0.172643, volume20=5.45882e+06; 직전 완료 봉 목표를 다음 봉 시가에 모의 적용 |
| v2 | chaikin_3_10 | 9891.60 | -108.40 | buy / partial / ADL의 EMA3 - EMA10 > 0 그리고 종가 > EMA26; 조건 충족; Chaikin3_10=250777, ADL=4.30146e+06, close=254.04, EMA26=253.978; 직전 완료 봉 목표를 다음 봉 시가에 모의 적용 |
| v2 | roc_10_momentum | 9684.01 | -315.99 | sell / filled / 10봉 ROC > 1% 그리고 종가 > EMA26; 조건 미충족; ROC10_percent=-0.503419, close=258.91, EMA26=257.09; 직전 완료 봉 목표를 다음 봉 시가에 모의 적용 |
| v2 | trix_15_trend | 9785.06 | -214.94 | buy / partial / 15봉 삼중 EMA의 1봉 변화율 TRIX > 0 그리고 종가 > EMA26; 조건 충족; TRIX15_percent=0.000945132, close=260.22, EMA26=254.44; 직전 완료 봉 목표를 다음 봉 시가에 모의 적용 |
| v2 | keltner_20_breakout | 9914.05 | -85.95 | sell / filled / 종가 > EMA20 + 2 x Wilder ATR14; 조건 미충족; close=258.91, upper_Keltner=259.564, EMA20=257.603, ATR14=0.980686; 직전 완료 봉 목표를 다음 봉 시가에 모의 적용 |
| v2 | opening_range_30m | 10000.00 | 0.00 | 대기 /  / 새 신호 대기 |

### 같은 기간의 비용·노출 비교 (사후 연구)

| 전략 | 비용 전 | 비용 후 | 100% 보유 | 같은 평균 노출 보유 | 평균 노출 |
|---|---:|---:|---:|---:|---:|
| cash | 0.00% | 0.00% | -3.72% | -0.00% | 0.00% |
| buy_hold | -3.31% | -3.72% | -3.72% | -3.72% | 100.00% |
| trend_8_26 | 2.73% | 0.17% | -3.72% | -1.92% | 50.65% |
| momentum_26 | -0.32% | -4.02% | -3.72% | -1.85% | 48.56% |
| breakout_8 | -1.06% | -18.10% | -3.72% | -0.77% | 20.10% |
| reversion_12 | -6.52% | -14.77% | -3.72% | -1.16% | 30.29% |
| volume_26 | -0.47% | -6.94% | -3.72% | -0.24% | 6.27% |
| trend_8_26 AND momentum_26 | 0.94% | -2.40% | -3.72% | -1.65% | 43.34% |
| trend_8_26 + momentum_26 | 1.20% | -1.94% | -3.72% | -1.89% | 49.61% |
| trend_8_26 AND breakout_8 | 0.02% | -12.19% | -3.72% | -0.53% | 13.84% |
| trend_8_26 + breakout_8 | 0.85% | -9.21% | -3.72% | -1.35% | 35.38% |
| trend_8_26 AND reversion_12 | 1.42% | -2.34% | -3.72% | -0.23% | 6.01% |
| trend_8_26 + reversion_12 | -1.97% | -7.20% | -3.72% | -1.54% | 40.47% |
| trend_8_26 AND volume_26 | 1.42% | -1.10% | -3.72% | -0.06% | 1.57% |
| trend_8_26 + volume_26 | 1.15% | -3.23% | -3.72% | -1.09% | 28.46% |
| momentum_26 AND breakout_8 | 0.88% | -10.31% | -3.72% | -0.50% | 13.05% |
| momentum_26 + breakout_8 | -0.66% | -11.13% | -3.72% | -1.31% | 34.34% |
| momentum_26 AND reversion_12 | -0.23% | -3.53% | -3.72% | -0.25% | 6.53% |
| momentum_26 + reversion_12 | -3.44% | -8.98% | -3.72% | -1.51% | 39.43% |
| momentum_26 AND volume_26 | 0.14% | -0.70% | -3.72% | -0.02% | 0.52% |
| momentum_26 + volume_26 | -0.36% | -4.48% | -3.72% | -1.05% | 27.42% |
| breakout_8 AND reversion_12 | 0.00% | 0.00% | -3.72% | -0.00% | 0.00% |
| breakout_8 + reversion_12 | -3.81% | -16.11% | -3.72% | -0.97% | 25.20% |
| breakout_8 AND volume_26 | -0.46% | -1.29% | -3.72% | -0.02% | 0.52% |
| breakout_8 + volume_26 | -0.76% | -11.78% | -3.72% | -0.51% | 13.19% |
| reversion_12 AND volume_26 | -1.84% | -4.69% | -3.72% | -0.11% | 2.87% |
| reversion_12 + volume_26 | -3.53% | -10.38% | -3.72% | -0.70% | 18.28% |
| ema_12_26 | 0.53% | -1.97% | -3.72% | -1.73% | 45.43% |
| macd_12_26_9 | 5.83% | 2.76% | -3.72% | -1.12% | 29.24% |
| rsi_14_recovery | -1.35% | -6.20% | -3.72% | -0.12% | 3.13% |
| bollinger_20_reentry | -1.10% | -5.56% | -3.72% | -0.11% | 2.87% |
| donchian_20 | 0.68% | -6.26% | -3.72% | -0.25% | 6.53% |
| atr_14_breakout | 0.79% | -5.36% | -3.72% | -0.18% | 4.70% |
| session_vwap | 3.19% | -5.12% | -3.72% | -1.87% | 49.09% |
| obv_20 | -5.75% | -15.15% | -3.72% | -1.40% | 36.55% |
| stochastic_14_3_recovery | -0.53% | -12.67% | -3.72% | -0.31% | 8.09% |
| mfi_14_recovery | 0.33% | -0.93% | -3.72% | -0.03% | 0.78% |
| adx_14_trend | -2.56% | -7.35% | -3.72% | -1.38% | 36.03% |
| aroon_25_trend | 3.28% | -0.55% | -3.72% | -1.14% | 29.77% |
| cci_20_momentum | 0.07% | -6.43% | -3.72% | -0.80% | 20.89% |
| williams_14_recovery | -1.84% | -8.99% | -3.72% | -0.18% | 4.70% |
| cmf_20_accumulation | 5.33% | 1.00% | -3.72% | -1.29% | 33.68% |
| chaikin_3_10 | -2.75% | -7.92% | -3.72% | -1.47% | 38.38% |
| roc_10_momentum | -2.79% | -9.49% | -3.72% | -0.67% | 17.49% |
| trix_15_trend | -0.54% | -3.02% | -3.72% | -1.34% | 34.99% |
| keltner_20_breakout | 0.20% | -3.52% | -3.72% | -0.45% | 11.75% |
| opening_range_30m | 0.79% | -2.95% | -3.72% | -0.99% | 25.85% |

동일 구간·초기 자금, 종료 시 청산 비용 포함. 노출 맞춤은 사후 설명용이며 v2 실제 계좌 성과가 아닙니다.
[낙폭 분해·비용 영향·전체 구간](JNJ/comparison.json)

[v1 전체 기록](JNJ/accounts.json) · [v2 전체 기록](JNJ/accounts-v2.json)

## CAT 계좌

| 모델 | 전략 | 평가액 USD | 손익 USD | 최근 매매·이유 |
|---|---|---:|---:|---|
| v1 | cash | 10000.00 | 0.00 | 대기 /  / 새 신호 대기 |
| v1 | buy_hold | 9869.54 | -130.46 | buy /  / buy_hold: prior completed bar target 100%; next bar open simulation |
| v1 | trend_8_26 | 9792.90 | -207.10 | buy /  / trend_8_26: prior completed bar target 100%; next bar open simulation |
| v1 | momentum_26 | 9640.53 | -359.47 | sell /  / momentum_26: prior completed bar target 0%; next bar open simulation |
| v1 | breakout_8 | 9600.35 | -399.65 | sell /  / breakout_8: prior completed bar target 0%; next bar open simulation |
| v1 | reversion_12 | 9921.83 | -78.17 | sell /  / reversion_12: prior completed bar target 0%; next bar open simulation |
| v1 | volume_26 | 9916.22 | -83.78 | sell /  / volume_26: prior completed bar target 0%; next bar open simulation |
| v1 | trend_8_26 AND momentum_26 | 9827.97 | -172.03 | sell /  / trend_8_26 AND momentum_26: prior completed bar target 0%; next bar open simulation |
| v1 | trend_8_26 + momentum_26 | 9716.59 | -283.41 | sell /  / trend_8_26 + momentum_26: prior completed bar target 50%; next bar open simulation |
| v1 | trend_8_26 AND breakout_8 | 9804.49 | -195.51 | sell /  / trend_8_26 AND breakout_8: prior completed bar target 0%; next bar open simulation |
| v1 | trend_8_26 + breakout_8 | 9696.32 | -303.68 | sell /  / trend_8_26 + breakout_8: prior completed bar target 50%; next bar open simulation |
| v1 | trend_8_26 AND reversion_12 | 9928.06 | -71.94 | sell /  / trend_8_26 AND reversion_12: prior completed bar target 0%; next bar open simulation |
| v1 | trend_8_26 + reversion_12 | 9897.32 | -102.68 | buy /  / trend_8_26 + reversion_12: prior completed bar target 50%; next bar open simulation |
| v1 | trend_8_26 AND volume_26 | 9965.69 | -34.31 | sell /  / trend_8_26 AND volume_26: prior completed bar target 0%; next bar open simulation |
| v1 | trend_8_26 + volume_26 | 9874.16 | -125.84 | sell /  / trend_8_26 + volume_26: prior completed bar target 50%; next bar open simulation |
| v1 | momentum_26 AND breakout_8 | 9671.65 | -328.35 | sell /  / momentum_26 AND breakout_8: prior completed bar target 0%; next bar open simulation |
| v1 | momentum_26 + breakout_8 | 9620.51 | -379.49 | sell /  / momentum_26 + breakout_8: prior completed bar target 0%; next bar open simulation |
| v1 | momentum_26 AND reversion_12 | 9887.21 | -112.79 | sell /  / momentum_26 AND reversion_12: prior completed bar target 0%; next bar open simulation |
| v1 | momentum_26 + reversion_12 | 9780.83 | -219.17 | sell /  / momentum_26 + reversion_12: prior completed bar target 0%; next bar open simulation |
| v1 | momentum_26 AND volume_26 | 9894.55 | -105.45 | sell /  / momentum_26 AND volume_26: prior completed bar target 0%; next bar open simulation |
| v1 | momentum_26 + volume_26 | 9777.45 | -222.55 | sell /  / momentum_26 + volume_26: prior completed bar target 0%; next bar open simulation |
| v1 | breakout_8 AND reversion_12 | 10000.00 | 0.00 | 대기 /  / 새 신호 대기 |
| v1 | breakout_8 + reversion_12 | 9760.29 | -239.71 | sell /  / breakout_8 + reversion_12: prior completed bar target 0%; next bar open simulation |
| v1 | breakout_8 AND volume_26 | 9894.55 | -105.45 | sell /  / breakout_8 AND volume_26: prior completed bar target 0%; next bar open simulation |
| v1 | breakout_8 + volume_26 | 9757.00 | -243.00 | sell /  / breakout_8 + volume_26: prior completed bar target 0%; next bar open simulation |
| v1 | reversion_12 AND volume_26 | 10046.29 | 46.29 | sell /  / reversion_12 AND volume_26: prior completed bar target 0%; next bar open simulation |
| v1 | reversion_12 + volume_26 | 9919.48 | -80.52 | sell /  / reversion_12 + volume_26: prior completed bar target 0%; next bar open simulation |
| v1 | ema_12_26 | 9820.60 | -179.40 | buy /  / EMA12 > EMA26; 조건 충족; EMA12=726.261, EMA26=726.172 |
| v1 | macd_12_26_9 | 9862.13 | -137.87 | buy /  / MACD > 신호선 그리고 MACD > 0; 조건 충족; MACD=0.0889648, signal9=-0.313692 |
| v1 | rsi_14_recovery | 9999.22 | -0.78 | sell /  / 직전 RSI14 < 30, 현재 RSI14 >= 30 (한 봉 목표); 조건 미충족; RSI14=43.621, previous_RSI14=38.5787 |
| v1 | bollinger_20_reentry | 9777.09 | -222.91 | sell /  / 직전 종가 < 직전 하단밴드, 현재 하단밴드 <= 종가 <= SMA20 (한 봉 목표); 조건 미충족; close=721.16, lower20=716.851, SMA20=725.821, previous_lower20=717.276 |
| v1 | donchian_20 | 9950.83 | -49.17 | sell /  / 종가 > 현재 봉을 제외한 직전 20봉 최고가; 조건 미충족; close=739.81, prior_high20=742.28 |
| v1 | atr_14_breakout | 9775.74 | -224.26 | sell /  / 종가 > 직전 종가 + 직전 ATR14 그리고 종가 > EMA26; 조건 미충족; close=732.42, threshold=735.931, prior_ATR14=4.99094, EMA26=726.612 |
| v1 | session_vwap | 9382.16 | -617.84 | buy /  / 종가 > 뉴욕 거래일별 누적 전형가격 VWAP; 조건 충족; close=725.26, session_VWAP=723.918, session_volume=2.02044e+06 |
| v1 | obv_20 | 9647.99 | -352.01 | buy /  / OBV > OBV의 SMA20 그리고 종가 > EMA26; 조건 충족; OBV=-4.78244e+06, OBV_SMA20=-6.34049e+06, close=727.27, EMA26=726.037 |
| v1 | stochastic_14_3_recovery | 9855.08 | -144.92 | sell /  / 직전 %K14 < 20에서 %K14가 %D3 상향 돌파 (한 봉 목표); 조건 미충족; K14=59.6496, D3=39.2535, previous_K14=43.8356, previous_D3=33.8642 |
| v1 | mfi_14_recovery | 10068.63 | 68.63 | sell /  / 직전 MFI14 < 20, 현재 MFI14 >= 20 (한 봉 목표); 조건 미충족; MFI14=32.7313, previous_MFI14=24.1736 |
| v1 | adx_14_trend | 10000.00 | 0.00 | 대기 /  / 새 신호 대기 |
| v1 | aroon_25_trend | 10031.15 | 31.15 | sell /  / Aroon25 Up > 70 그리고 Down < 30 (동률이면 최신 극값); 조건 미충족; Aroon_up=88, Aroon_down=48 |
| v1 | cci_20_momentum | 9890.31 | -109.69 | sell /  / CCI20 > 100 (전형가격·평균절대편차); 조건 미충족; CCI20=20.3547 |
| v1 | williams_14_recovery | 10007.06 | 7.06 | sell /  / 직전 Williams %R14 < -80, 현재 >= -80 (한 봉 목표); 조건 미충족; Williams_R14=-40.3504, previous_R14=-56.1644 |
| v1 | cmf_20_accumulation | 9796.77 | -203.23 | buy /  / Chaikin Money Flow20 > 0.1; 조건 충족; CMF20=0.130083, volume20=2.38752e+06 |
| v1 | chaikin_3_10 | 9455.38 | -544.62 | buy /  / ADL의 EMA3 - EMA10 > 0 그리고 종가 > EMA26; 조건 충족; Chaikin3_10=46276.1, ADL=-5.95779e+06, close=726.047, EMA26=725.791 |
| v1 | roc_10_momentum | 9963.13 | -36.87 | sell /  / 10봉 ROC > 1% 그리고 종가 > EMA26; 조건 미충족; ROC10_percent=-0.134597, close=734.53, EMA26=735.486 |
| v1 | trix_15_trend | 9669.78 | -330.22 | sell /  / 15봉 삼중 EMA의 1봉 변화율 TRIX > 0 그리고 종가 > EMA26; 조건 미충족; TRIX15_percent=0.0186631, close=734.925, EMA26=736.093 |
| v1 | keltner_20_breakout | 10000.00 | 0.00 | 대기 /  / 새 신호 대기 |
| v1 | opening_range_30m | 10084.54 | 84.54 | buy /  / 뉴욕 09:30·09:45 두 완료 봉 최고가를 10:00 이후 종가가 돌파; 조건 충족; close=721.16, opening_high=718.07 |
| v2 | cash | 10000.00 | 0.00 | 대기 /  / 새 신호 대기 |
| v2 | buy_hold | 9076.77 | -923.23 | 중단: 손실 한도 / buy / partial / 직전 완료 봉 목표 비중 100%; 다음 봉 시가 가정 |
| v2 | trend_8_26 | 9712.38 | -287.62 | buy / partial / 직전 완료 봉 목표 비중 100%; 다음 봉 시가 가정 |
| v2 | momentum_26 | 9644.95 | -355.05 | sell / filled / 직전 완료 봉 목표 비중 0%; 다음 봉 시가 가정 |
| v2 | breakout_8 | 9417.25 | -582.75 | sell / filled / 직전 완료 봉 목표 비중 0%; 다음 봉 시가 가정 |
| v2 | reversion_12 | 8950.01 | -1049.99 | 중단: 손실 한도 / buy / partial / 직전 완료 봉 목표 비중 100%; 다음 봉 시가 가정 |
| v2 | volume_26 | 9205.97 | -794.03 | 중단: 손실 한도 / buy / partial / 직전 완료 봉 목표 비중 100%; 다음 봉 시가 가정 |
| v2 | trend_8_26 AND momentum_26 | 9866.86 | -133.14 | sell / filled / 직전 완료 봉 목표 비중 0%; 다음 봉 시가 가정 |
| v2 | trend_8_26 + momentum_26 | 9678.76 | -321.24 | sell / filled / 직전 완료 봉 목표 비중 50%; 다음 봉 시가 가정 |
| v2 | trend_8_26 AND breakout_8 | 9717.70 | -282.30 | sell / filled / 직전 완료 봉 목표 비중 0%; 다음 봉 시가 가정 |
| v2 | trend_8_26 + breakout_8 | 9564.10 | -435.90 | sell / filled / 직전 완료 봉 목표 비중 50%; 다음 봉 시가 가정 |
| v2 | trend_8_26 AND reversion_12 | 9738.62 | -261.38 | sell / filled / 직전 완료 봉 목표 비중 0%; 다음 봉 시가 가정 |
| v2 | trend_8_26 + reversion_12 | 9516.34 | -483.66 | buy / filled / 직전 완료 봉 목표 비중 50%; 다음 봉 시가 가정 |
| v2 | trend_8_26 AND volume_26 | 9999.01 | -0.99 | sell / filled / 직전 완료 봉 목표 비중 0%; 다음 봉 시가 가정 |
| v2 | trend_8_26 + volume_26 | 9504.67 | -495.33 | sell / filled / 직전 완료 봉 목표 비중 50%; 다음 봉 시가 가정 |
| v2 | momentum_26 AND breakout_8 | 9638.26 | -361.74 | sell / filled / 직전 완료 봉 목표 비중 0%; 다음 봉 시가 가정 |
| v2 | momentum_26 + breakout_8 | 9530.69 | -469.31 | sell / filled / 직전 완료 봉 목표 비중 0%; 다음 봉 시가 가정 |
| v2 | momentum_26 AND reversion_12 | 9755.55 | -244.45 | sell / filled / 직전 완료 봉 목표 비중 0%; 다음 봉 시가 가정 |
| v2 | momentum_26 + reversion_12 | 9443.50 | -556.50 | sell / filled / 직전 완료 봉 목표 비중 0%; 다음 봉 시가 가정 |
| v2 | momentum_26 AND volume_26 | 9936.85 | -63.15 | sell / filled / 직전 완료 봉 목표 비중 0%; 다음 봉 시가 가정 |
| v2 | momentum_26 + volume_26 | 9471.62 | -528.38 | sell / filled / 직전 완료 봉 목표 비중 0%; 다음 봉 시가 가정 |
| v2 | breakout_8 AND reversion_12 | 10000.00 | 0.00 | 대기 /  / 새 신호 대기 |
| v2 | breakout_8 + reversion_12 | 9610.18 | -389.82 | 중단: 손실 한도 / sell / filled / 직전 완료 봉 목표 비중 0%; 다음 봉 시가 가정 |
| v2 | breakout_8 AND volume_26 | 9887.31 | -112.69 | sell / filled / 직전 완료 봉 목표 비중 0%; 다음 봉 시가 가정 |
| v2 | breakout_8 + volume_26 | 9359.24 | -640.76 | sell / filled / 직전 완료 봉 목표 비중 0%; 다음 봉 시가 가정 |
| v2 | reversion_12 AND volume_26 | 9142.28 | -857.72 | 중단: 손실 한도 / buy / partial / 직전 완료 봉 목표 비중 100%; 다음 봉 시가 가정 |
| v2 | reversion_12 + volume_26 | 9337.15 | -662.85 | 중단: 손실 한도 / sell / filled / 직전 완료 봉 목표 비중 50%; 다음 봉 시가 가정 |
| v2 | ema_12_26 | 9817.65 | -182.35 | buy / partial / EMA12 > EMA26; 조건 충족; EMA12=726.261, EMA26=726.172; 직전 완료 봉 목표를 다음 봉 시가에 모의 적용 |
| v2 | macd_12_26_9 | 9859.17 | -140.83 | buy / partial / MACD > 신호선 그리고 MACD > 0; 조건 충족; MACD=0.0889648, signal9=-0.313692; 직전 완료 봉 목표를 다음 봉 시가에 모의 적용 |
| v2 | rsi_14_recovery | 9995.22 | -4.78 | sell / filled / 직전 RSI14 < 30, 현재 RSI14 >= 30 (한 봉 목표); 조건 미충족; RSI14=43.621, previous_RSI14=38.5787; 직전 완료 봉 목표를 다음 봉 시가에 모의 적용 |
| v2 | bollinger_20_reentry | 9771.22 | -228.78 | sell / filled / 직전 종가 < 직전 하단밴드, 현재 하단밴드 <= 종가 <= SMA20 (한 봉 목표); 조건 미충족; close=721.16, lower20=716.851, SMA20=725.821, previous_lower20=717.276; 직전 완료 봉 목표를 다음 봉 시가에 모의 적용 |
| v2 | donchian_20 | 9948.84 | -51.16 | sell / filled / 종가 > 현재 봉을 제외한 직전 20봉 최고가; 조건 미충족; close=739.81, prior_high20=742.28; 직전 완료 봉 목표를 다음 봉 시가에 모의 적용 |
| v2 | atr_14_breakout | 9767.92 | -232.08 | sell / filled / 종가 > 직전 종가 + 직전 ATR14 그리고 종가 > EMA26; 조건 미충족; close=732.42, threshold=735.931, prior_ATR14=4.99094, EMA26=726.612; 직전 완료 봉 목표를 다음 봉 시가에 모의 적용 |
| v2 | session_vwap | 9366.22 | -633.78 | buy / partial / 종가 > 뉴욕 거래일별 누적 전형가격 VWAP; 조건 충족; close=725.26, session_VWAP=723.918, session_volume=2.02044e+06; 직전 완료 봉 목표를 다음 봉 시가에 모의 적용 |
| v2 | obv_20 | 9639.31 | -360.69 | buy / partial / OBV > OBV의 SMA20 그리고 종가 > EMA26; 조건 충족; OBV=-4.78244e+06, OBV_SMA20=-6.34049e+06, close=727.27, EMA26=726.037; 직전 완료 봉 목표를 다음 봉 시가에 모의 적용 |
| v2 | stochastic_14_3_recovery | 9843.26 | -156.74 | sell / filled / 직전 %K14 < 20에서 %K14가 %D3 상향 돌파 (한 봉 목표); 조건 미충족; K14=59.6496, D3=39.2535, previous_K14=43.8356, previous_D3=33.8642; 직전 완료 봉 목표를 다음 봉 시가에 모의 적용 |
| v2 | mfi_14_recovery | 10064.61 | 64.61 | sell / filled / 직전 MFI14 < 20, 현재 MFI14 >= 20 (한 봉 목표); 조건 미충족; MFI14=32.7313, previous_MFI14=24.1736; 직전 완료 봉 목표를 다음 봉 시가에 모의 적용 |
| v2 | adx_14_trend | 10000.00 | 0.00 | 대기 /  / 새 신호 대기 |
| v2 | aroon_25_trend | 10029.14 | 29.14 | sell / filled / Aroon25 Up > 70 그리고 Down < 30 (동률이면 최신 극값); 조건 미충족; Aroon_up=88, Aroon_down=48; 직전 완료 봉 목표를 다음 봉 시가에 모의 적용 |
| v2 | cci_20_momentum | 9886.36 | -113.64 | sell / filled / CCI20 > 100 (전형가격·평균절대편차); 조건 미충족; CCI20=20.3547; 직전 완료 봉 목표를 다음 봉 시가에 모의 적용 |
| v2 | williams_14_recovery | 9999.06 | -0.94 | sell / filled / 직전 Williams %R14 < -80, 현재 >= -80 (한 봉 목표); 조건 미충족; Williams_R14=-40.3504, previous_R14=-56.1644; 직전 완료 봉 목표를 다음 봉 시가에 모의 적용 |
| v2 | cmf_20_accumulation | 9789.91 | -210.09 | buy / partial / Chaikin Money Flow20 > 0.1; 조건 충족; CMF20=0.130083, volume20=2.38752e+06; 직전 완료 봉 목표를 다음 봉 시가에 모의 적용 |
| v2 | chaikin_3_10 | 9559.16 | -440.84 | 중단: 손실 한도 / buy / partial / ADL의 EMA3 - EMA10 > 0 그리고 종가 > EMA26; 조건 충족; Chaikin3_10=293683, ADL=-4.91156e+06, close=739.58, EMA26=736.187; 직전 완료 봉 목표를 다음 봉 시가에 모의 적용 |
| v2 | roc_10_momentum | 9961.14 | -38.86 | sell / filled / 10봉 ROC > 1% 그리고 종가 > EMA26; 조건 미충족; ROC10_percent=-0.134597, close=734.53, EMA26=735.486; 직전 완료 봉 목표를 다음 봉 시가에 모의 적용 |
| v2 | trix_15_trend | 9568.79 | -431.21 | 중단: 손실 한도 / buy / partial / 15봉 삼중 EMA의 1봉 변화율 TRIX > 0 그리고 종가 > EMA26; 조건 충족; TRIX15_percent=0.0196284, close=739.58, EMA26=736.187; 직전 완료 봉 목표를 다음 봉 시가에 모의 적용 |
| v2 | keltner_20_breakout | 10000.00 | 0.00 | 대기 /  / 새 신호 대기 |
| v2 | opening_range_30m | 10081.51 | 81.51 | buy / partial / 뉴욕 09:30·09:45 두 완료 봉 최고가를 10:00 이후 종가가 돌파; 조건 충족; close=721.16, opening_high=718.07; 직전 완료 봉 목표를 다음 봉 시가에 모의 적용 |

### 같은 기간의 비용·노출 비교 (사후 연구)

| 전략 | 비용 전 | 비용 후 | 100% 보유 | 같은 평균 노출 보유 | 평균 노출 |
|---|---:|---:|---:|---:|---:|
| cash | 0.00% | 0.00% | -11.29% | -0.00% | 0.00% |
| buy_hold | -10.92% | -11.29% | -11.29% | -11.29% | 100.00% |
| trend_8_26 | -0.08% | -3.79% | -11.29% | -4.84% | 42.04% |
| momentum_26 | -2.45% | -6.85% | -11.29% | -4.81% | 41.78% |
| breakout_8 | -3.71% | -16.17% | -11.29% | -1.70% | 14.62% |
| reversion_12 | -2.20% | -15.57% | -11.29% | -3.11% | 26.89% |
| volume_26 | -1.22% | -8.80% | -11.29% | -0.97% | 8.36% |
| trend_8_26 AND momentum_26 | 1.33% | -1.19% | -11.29% | -4.13% | 35.77% |
| trend_8_26 + momentum_26 | -1.26% | -5.32% | -11.29% | -4.83% | 41.91% |
| trend_8_26 AND breakout_8 | -2.07% | -8.43% | -11.29% | -0.79% | 6.79% |
| trend_8_26 + breakout_8 | -1.88% | -9.98% | -11.29% | -3.28% | 28.33% |
| trend_8_26 AND reversion_12 | 0.65% | -5.10% | -11.29% | -0.58% | 4.96% |
| trend_8_26 + reversion_12 | -1.08% | -9.08% | -11.29% | -3.98% | 34.47% |
| trend_8_26 AND volume_26 | 2.90% | 1.18% | -11.29% | -0.18% | 1.57% |
| trend_8_26 + volume_26 | -0.60% | -5.91% | -11.29% | -2.92% | 25.20% |
| momentum_26 AND breakout_8 | -2.80% | -10.25% | -11.29% | -0.88% | 7.57% |
| momentum_26 + breakout_8 | -3.04% | -11.61% | -11.29% | -3.26% | 28.20% |
| momentum_26 AND reversion_12 | -3.16% | -8.69% | -11.29% | -0.67% | 5.74% |
| momentum_26 + reversion_12 | -2.26% | -10.73% | -11.29% | -3.97% | 34.34% |
| momentum_26 AND volume_26 | 2.69% | 0.55% | -11.29% | -0.18% | 1.57% |
| momentum_26 + volume_26 | -1.78% | -7.41% | -11.29% | -2.90% | 25.07% |
| breakout_8 AND reversion_12 | 0.00% | 0.00% | -11.29% | -0.00% | 0.00% |
| breakout_8 + reversion_12 | -2.90% | -14.96% | -11.29% | -2.41% | 20.77% |
| breakout_8 AND volume_26 | 0.55% | -1.13% | -11.29% | -0.12% | 1.04% |
| breakout_8 + volume_26 | -2.44% | -11.99% | -11.29% | -1.34% | 11.49% |
| reversion_12 AND volume_26 | -0.54% | -5.03% | -11.29% | -0.61% | 5.22% |
| reversion_12 + volume_26 | -1.67% | -11.86% | -11.29% | -2.05% | 17.63% |
| ema_12_26 | -0.34% | -2.00% | -11.29% | -4.40% | 38.12% |
| macd_12_26_9 | 1.93% | -0.60% | -11.29% | -2.69% | 23.24% |
| rsi_14_recovery | -0.17% | -6.26% | -11.29% | -0.46% | 3.92% |
| bollinger_20_reentry | 0.54% | -5.20% | -11.29% | -0.43% | 3.66% |
| donchian_20 | -1.16% | -4.82% | -11.29% | -0.52% | 4.44% |
| atr_14_breakout | -1.46% | -7.48% | -11.29% | -0.49% | 4.18% |
| session_vwap | -0.31% | -12.85% | -11.29% | -5.49% | 47.78% |
| obv_20 | -4.30% | -13.48% | -11.29% | -2.27% | 19.58% |
| stochastic_14_3_recovery | -2.13% | -12.62% | -11.29% | -0.82% | 7.05% |
| mfi_14_recovery | 1.96% | -1.00% | -11.29% | -0.21% | 1.83% |
| adx_14_trend | -2.02% | -4.05% | -11.29% | -0.97% | 8.36% |
| aroon_25_trend | -0.11% | -3.01% | -11.29% | -1.19% | 10.18% |
| cci_20_momentum | -3.56% | -7.91% | -11.29% | -1.49% | 12.79% |
| williams_14_recovery | 0.45% | -8.03% | -11.29% | -0.64% | 5.48% |
| cmf_20_accumulation | -3.98% | -10.59% | -11.29% | -2.12% | 18.28% |
| chaikin_3_10 | -5.30% | -14.02% | -11.29% | -3.41% | 29.50% |
| roc_10_momentum | -1.68% | -6.91% | -11.29% | -1.43% | 12.27% |
| trix_15_trend | -0.75% | -4.43% | -11.29% | -3.41% | 29.50% |
| keltner_20_breakout | -2.87% | -5.29% | -11.29% | -0.30% | 2.61% |
| opening_range_30m | 6.82% | 1.99% | -11.29% | -2.96% | 25.59% |

동일 구간·초기 자금, 종료 시 청산 비용 포함. 노출 맞춤은 사후 설명용이며 v2 실제 계좌 성과가 아닙니다.
[낙폭 분해·비용 영향·전체 구간](CAT/comparison.json)

[v1 전체 기록](CAT/accounts.json) · [v2 전체 기록](CAT/accounts-v2.json)

## WMT 계좌

| 모델 | 전략 | 평가액 USD | 손익 USD | 최근 매매·이유 |
|---|---|---:|---:|---|
| v1 | cash | 10000.00 | 0.00 | 대기 /  / 새 신호 대기 |
| v1 | buy_hold | 9971.16 | -28.84 | buy /  / buy_hold: prior completed bar target 100%; next bar open simulation |
| v1 | trend_8_26 | 9791.85 | -208.15 | sell /  / trend_8_26: prior completed bar target 0%; next bar open simulation |
| v1 | momentum_26 | 9801.37 | -198.63 | sell /  / momentum_26: prior completed bar target 0%; next bar open simulation |
| v1 | breakout_8 | 9728.67 | -271.33 | sell /  / breakout_8: prior completed bar target 0%; next bar open simulation |
| v1 | reversion_12 | 9674.76 | -325.24 | buy /  / reversion_12: prior completed bar target 100%; next bar open simulation |
| v1 | volume_26 | 9755.08 | -244.92 | sell /  / volume_26: prior completed bar target 0%; next bar open simulation |
| v1 | trend_8_26 AND momentum_26 | 9811.64 | -188.36 | sell /  / trend_8_26 AND momentum_26: prior completed bar target 0%; next bar open simulation |
| v1 | trend_8_26 + momentum_26 | 9796.64 | -203.36 | sell /  / trend_8_26 + momentum_26: prior completed bar target 0%; next bar open simulation |
| v1 | trend_8_26 AND breakout_8 | 9854.29 | -145.71 | sell /  / trend_8_26 AND breakout_8: prior completed bar target 0%; next bar open simulation |
| v1 | trend_8_26 + breakout_8 | 9760.28 | -239.72 | sell /  / trend_8_26 + breakout_8: prior completed bar target 0%; next bar open simulation |
| v1 | trend_8_26 AND reversion_12 | 9798.51 | -201.49 | sell /  / trend_8_26 AND reversion_12: prior completed bar target 0%; next bar open simulation |
| v1 | trend_8_26 + reversion_12 | 9772.29 | -227.71 | buy /  / trend_8_26 + reversion_12: prior completed bar target 50%; next bar open simulation |
| v1 | trend_8_26 AND volume_26 | 9837.96 | -162.04 | sell /  / trend_8_26 AND volume_26: prior completed bar target 0%; next bar open simulation |
| v1 | trend_8_26 + volume_26 | 9773.64 | -226.36 | sell /  / trend_8_26 + volume_26: prior completed bar target 0%; next bar open simulation |
| v1 | momentum_26 AND breakout_8 | 9816.19 | -183.81 | sell /  / momentum_26 AND breakout_8: prior completed bar target 0%; next bar open simulation |
| v1 | momentum_26 + breakout_8 | 9823.93 | -176.07 | sell /  / momentum_26 + breakout_8: prior completed bar target 0%; next bar open simulation |
| v1 | momentum_26 AND reversion_12 | 9935.88 | -64.12 | sell /  / momentum_26 AND reversion_12: prior completed bar target 0%; next bar open simulation |
| v1 | momentum_26 + reversion_12 | 9835.70 | -164.30 | buy /  / momentum_26 + reversion_12: prior completed bar target 50%; next bar open simulation |
| v1 | momentum_26 AND volume_26 | 9905.94 | -94.06 | sell /  / momentum_26 AND volume_26: prior completed bar target 0%; next bar open simulation |
| v1 | momentum_26 + volume_26 | 9817.50 | -182.50 | sell /  / momentum_26 + volume_26: prior completed bar target 0%; next bar open simulation |
| v1 | breakout_8 AND reversion_12 | 10000.00 | 0.00 | 대기 /  / 새 신호 대기 |
| v1 | breakout_8 + reversion_12 | 9740.42 | -259.58 | buy /  / breakout_8 + reversion_12: prior completed bar target 50%; next bar open simulation |
| v1 | breakout_8 AND volume_26 | 9850.09 | -149.91 | sell /  / breakout_8 AND volume_26: prior completed bar target 0%; next bar open simulation |
| v1 | breakout_8 + volume_26 | 9741.88 | -258.12 | sell /  / breakout_8 + volume_26: prior completed bar target 0%; next bar open simulation |
| v1 | reversion_12 AND volume_26 | 9905.10 | -94.90 | sell /  / reversion_12 AND volume_26: prior completed bar target 0%; next bar open simulation |
| v1 | reversion_12 + volume_26 | 9753.68 | -246.32 | buy /  / reversion_12 + volume_26: prior completed bar target 50%; next bar open simulation |
| v1 | ema_12_26 | 9906.58 | -93.42 | sell /  / EMA12 > EMA26; 조건 미충족; EMA12=118.808, EMA26=118.852 |
| v1 | macd_12_26_9 | 9985.46 | -14.54 | sell /  / MACD > 신호선 그리고 MACD > 0; 조건 미충족; MACD=0.122825, signal9=0.127837 |
| v1 | rsi_14_recovery | 10000.00 | 0.00 | 대기 /  / 새 신호 대기 |
| v1 | bollinger_20_reentry | 9901.04 | -98.96 | sell /  / 직전 종가 < 직전 하단밴드, 현재 하단밴드 <= 종가 <= SMA20 (한 봉 목표); 조건 미충족; close=118.132, lower20=117.91, SMA20=118.808, previous_lower20=118.006 |
| v1 | donchian_20 | 9935.97 | -64.03 | sell /  / 종가 > 현재 봉을 제외한 직전 20봉 최고가; 조건 미충족; close=119.52, prior_high20=120.5 |
| v1 | atr_14_breakout | 9915.82 | -84.18 | sell /  / 종가 > 직전 종가 + 직전 ATR14 그리고 종가 > EMA26; 조건 미충족; close=119.52, threshold=120.186, prior_ATR14=0.395874, EMA26=118.952 |
| v1 | session_vwap | 9838.24 | -161.76 | sell /  / 종가 > 뉴욕 거래일별 누적 전형가격 VWAP; 조건 미충족; close=118.71, session_VWAP=118.72, session_volume=1.73369e+07 |
| v1 | obv_20 | 9857.61 | -142.39 | sell /  / OBV > OBV의 SMA20 그리고 종가 > EMA26; 조건 미충족; OBV=1.6238e+07, OBV_SMA20=1.74966e+07, close=118.945, EMA26=118.951 |
| v1 | stochastic_14_3_recovery | 9661.47 | -338.53 | sell /  / 직전 %K14 < 20에서 %K14가 %D3 상향 돌파 (한 봉 목표); 조건 미충족; K14=9.9362, D3=16.15, previous_K14=25.6758, previous_D3=22.4971 |
| v1 | mfi_14_recovery | 9953.35 | -46.65 | sell /  / 직전 MFI14 < 20, 현재 MFI14 >= 20 (한 봉 목표); 조건 미충족; MFI14=30.6648, previous_MFI14=20.4345 |
| v1 | adx_14_trend | 9991.69 | -8.31 | sell /  / Wilder ADX14 >= 25 그리고 +DI14 > -DI14; 조건 미충족; ADX14=24.5142, plus_DI14=24.7537, minus_DI14=21.6519 |
| v1 | aroon_25_trend | 9947.63 | -52.37 | sell /  / Aroon25 Up > 70 그리고 Down < 30 (동률이면 최신 극값); 조건 미충족; Aroon_up=68, Aroon_down=4 |
| v1 | cci_20_momentum | 9772.81 | -227.19 | sell /  / CCI20 > 100 (전형가격·평균절대편차); 조건 미충족; CCI20=38.8365 |
| v1 | williams_14_recovery | 9767.87 | -232.13 | sell /  / 직전 Williams %R14 < -80, 현재 >= -80 (한 봉 목표); 조건 미충족; Williams_R14=-90.0638, previous_R14=-74.3242 |
| v1 | cmf_20_accumulation | 9898.70 | -101.30 | sell /  / Chaikin Money Flow20 > 0.1; 조건 미충족; CMF20=0.0888031, volume20=1.50234e+07 |
| v1 | chaikin_3_10 | 9762.96 | -237.04 | sell /  / ADL의 EMA3 - EMA10 > 0 그리고 종가 > EMA26; 조건 미충족; Chaikin3_10=-178256, ADL=1.4762e+07, close=119.52, EMA26=118.952 |
| v1 | roc_10_momentum | 10000.00 | 0.00 | 대기 /  / 새 신호 대기 |
| v1 | trix_15_trend | 9708.65 | -291.35 | sell /  / 15봉 삼중 EMA의 1봉 변화율 TRIX > 0 그리고 종가 > EMA26; 조건 미충족; TRIX15_percent=0.0142754, close=118.77, EMA26=118.947 |
| v1 | keltner_20_breakout | 9935.97 | -64.03 | sell /  / 종가 > EMA20 + 2 x Wilder ATR14; 조건 미충족; close=119.52, upper_Keltner=119.83, EMA20=119.013, ATR14=0.408312 |
| v1 | opening_range_30m | 9927.51 | -72.49 | sell /  / 뉴욕 09:30·09:45 두 완료 봉 최고가를 10:00 이후 종가가 돌파; 조건 미충족; close=118.85, opening_high=119.14 |
| v2 | cash | 10000.00 | 0.00 | 대기 /  / 새 신호 대기 |
| v2 | buy_hold | 10564.35 | 564.35 | buy / partial / 직전 완료 봉 목표 비중 100%; 다음 봉 시가 가정 |
| v2 | trend_8_26 | 10187.81 | 187.81 | sell / filled / 직전 완료 봉 목표 비중 0%; 다음 봉 시가 가정 |
| v2 | momentum_26 | 10200.51 | 200.51 | sell / filled / 직전 완료 봉 목표 비중 0%; 다음 봉 시가 가정 |
| v2 | breakout_8 | 9682.65 | -317.35 | sell / filled / 직전 완료 봉 목표 비중 0%; 다음 봉 시가 가정 |
| v2 | reversion_12 | 9568.95 | -431.05 | buy / partial / 직전 완료 봉 목표 비중 100%; 다음 봉 시가 가정 |
| v2 | volume_26 | 9711.50 | -288.50 | sell / filled / 직전 완료 봉 목표 비중 0%; 다음 봉 시가 가정 |
| v2 | trend_8_26 AND momentum_26 | 10206.36 | 206.36 | sell / filled / 직전 완료 봉 목표 비중 0%; 다음 봉 시가 가정 |
| v2 | trend_8_26 + momentum_26 | 10194.13 | 194.13 | sell / filled / 직전 완료 봉 목표 비중 0%; 다음 봉 시가 가정 |
| v2 | trend_8_26 AND breakout_8 | 9935.59 | -64.41 | sell / filled / 직전 완료 봉 목표 비중 0%; 다음 봉 시가 가정 |
| v2 | trend_8_26 + breakout_8 | 9932.48 | -67.52 | sell / filled / 직전 완료 봉 목표 비중 0%; 다음 봉 시가 가정 |
| v2 | trend_8_26 AND reversion_12 | 9603.42 | -396.58 | sell / filled / 직전 완료 봉 목표 비중 0%; 다음 봉 시가 가정 |
| v2 | trend_8_26 + reversion_12 | 9916.63 | -83.37 | buy / filled / 직전 완료 봉 목표 비중 50%; 다음 봉 시가 가정 |
| v2 | trend_8_26 AND volume_26 | 9784.10 | -215.90 | sell / filled / 직전 완료 봉 목표 비중 0%; 다음 봉 시가 가정 |
| v2 | trend_8_26 + volume_26 | 9948.42 | -51.58 | sell / filled / 직전 완료 봉 목표 비중 0%; 다음 봉 시가 가정 |
| v2 | momentum_26 AND breakout_8 | 9773.67 | -226.33 | sell / filled / 직전 완료 봉 목표 비중 0%; 다음 봉 시가 가정 |
| v2 | momentum_26 + breakout_8 | 10001.62 | 1.62 | sell / filled / 직전 완료 봉 목표 비중 0%; 다음 봉 시가 가정 |
| v2 | momentum_26 AND reversion_12 | 9759.91 | -240.09 | sell / filled / 직전 완료 봉 목표 비중 0%; 다음 봉 시가 가정 |
| v2 | momentum_26 + reversion_12 | 10027.43 | 27.43 | buy / filled / 직전 완료 봉 목표 비중 50%; 다음 봉 시가 가정 |
| v2 | momentum_26 AND volume_26 | 9814.68 | -185.32 | sell / filled / 직전 완료 봉 목표 비중 0%; 다음 봉 시가 가정 |
| v2 | momentum_26 + volume_26 | 9996.47 | -3.53 | sell / filled / 직전 완료 봉 목표 비중 0%; 다음 봉 시가 가정 |
| v2 | breakout_8 AND reversion_12 | 10000.00 | 0.00 | 대기 /  / 새 신호 대기 |
| v2 | breakout_8 + reversion_12 | 9687.44 | -312.56 | buy / filled / 직전 완료 봉 목표 비중 50%; 다음 봉 시가 가정 |
| v2 | breakout_8 AND volume_26 | 9795.19 | -204.81 | sell / filled / 직전 완료 봉 목표 비중 0%; 다음 봉 시가 가정 |
| v2 | breakout_8 + volume_26 | 9698.42 | -301.58 | sell / filled / 직전 완료 봉 목표 비중 0%; 다음 봉 시가 가정 |
| v2 | reversion_12 AND volume_26 | 9912.80 | -87.20 | sell / filled / 직전 완료 봉 목표 비중 0%; 다음 봉 시가 가정 |
| v2 | reversion_12 + volume_26 | 9680.33 | -319.67 | buy / filled / 직전 완료 봉 목표 비중 50%; 다음 봉 시가 가정 |
| v2 | ema_12_26 | 9902.61 | -97.39 | sell / filled / EMA12 > EMA26; 조건 미충족; EMA12=118.808, EMA26=118.852; 직전 완료 봉 목표를 다음 봉 시가에 모의 적용 |
| v2 | macd_12_26_9 | 9981.46 | -18.54 | sell / filled / MACD > 신호선 그리고 MACD > 0; 조건 미충족; MACD=0.122825, signal9=0.127837; 직전 완료 봉 목표를 다음 봉 시가에 모의 적용 |
| v2 | rsi_14_recovery | 10000.00 | 0.00 | 대기 /  / 새 신호 대기 |
| v2 | bollinger_20_reentry | 9897.08 | -102.92 | sell / filled / 직전 종가 < 직전 하단밴드, 현재 하단밴드 <= 종가 <= SMA20 (한 봉 목표); 조건 미충족; close=118.132, lower20=117.91, SMA20=118.808, previous_lower20=118.006; 직전 완료 봉 목표를 다음 봉 시가에 모의 적용 |
| v2 | donchian_20 | 9933.99 | -66.01 | sell / filled / 종가 > 현재 봉을 제외한 직전 20봉 최고가; 조건 미충족; close=119.52, prior_high20=120.5; 직전 완료 봉 목표를 다음 봉 시가에 모의 적용 |
| v2 | atr_14_breakout | 9911.85 | -88.15 | sell / filled / 종가 > 직전 종가 + 직전 ATR14 그리고 종가 > EMA26; 조건 미충족; close=119.52, threshold=120.186, prior_ATR14=0.395874, EMA26=118.952; 직전 완료 봉 목표를 다음 봉 시가에 모의 적용 |
| v2 | session_vwap | 9826.44 | -173.56 | sell / filled / 종가 > 뉴욕 거래일별 누적 전형가격 VWAP; 조건 미충족; close=118.71, session_VWAP=118.72, session_volume=1.73369e+07; 직전 완료 봉 목표를 다음 봉 시가에 모의 적용 |
| v2 | obv_20 | 9847.76 | -152.24 | sell / filled / OBV > OBV의 SMA20 그리고 종가 > EMA26; 조건 미충족; OBV=1.6238e+07, OBV_SMA20=1.74966e+07, close=118.945, EMA26=118.951; 직전 완료 봉 목표를 다음 봉 시가에 모의 적용 |
| v2 | stochastic_14_3_recovery | 9675.22 | -324.78 | 중단: 손실 한도 / buy / partial / 직전 %K14 < 20에서 %K14가 %D3 상향 돌파 (한 봉 목표); 조건 충족; K14=25.6758, D3=22.4971, previous_K14=12.8379, previous_D3=25.8704; 직전 완료 봉 목표를 다음 봉 시가에 모의 적용 |
| v2 | mfi_14_recovery | 9951.36 | -48.64 | sell / filled / 직전 MFI14 < 20, 현재 MFI14 >= 20 (한 봉 목표); 조건 미충족; MFI14=30.6648, previous_MFI14=20.4345; 직전 완료 봉 목표를 다음 봉 시가에 모의 적용 |
| v2 | adx_14_trend | 9989.70 | -10.30 | sell / filled / Wilder ADX14 >= 25 그리고 +DI14 > -DI14; 조건 미충족; ADX14=24.5142, plus_DI14=24.7537, minus_DI14=21.6519; 직전 완료 봉 목표를 다음 봉 시가에 모의 적용 |
| v2 | aroon_25_trend | 9943.65 | -56.35 | sell / filled / Aroon25 Up > 70 그리고 Down < 30 (동률이면 최신 극값); 조건 미충족; Aroon_up=68, Aroon_down=4; 직전 완료 봉 목표를 다음 봉 시가에 모의 적용 |
| v2 | cci_20_momentum | 9766.95 | -233.05 | sell / filled / CCI20 > 100 (전형가격·평균절대편차); 조건 미충족; CCI20=38.8365; 직전 완료 봉 목표를 다음 봉 시가에 모의 적용 |
| v2 | williams_14_recovery | 9758.11 | -241.89 | sell / filled / 직전 Williams %R14 < -80, 현재 >= -80 (한 봉 목표); 조건 미충족; Williams_R14=-90.0638, previous_R14=-74.3242; 직전 완료 봉 목표를 다음 봉 시가에 모의 적용 |
| v2 | cmf_20_accumulation | 9890.78 | -109.22 | sell / filled / Chaikin Money Flow20 > 0.1; 조건 미충족; CMF20=0.0888031, volume20=1.50234e+07; 직전 완료 봉 목표를 다음 봉 시가에 모의 적용 |
| v2 | chaikin_3_10 | 9749.30 | -250.70 | sell / filled / ADL의 EMA3 - EMA10 > 0 그리고 종가 > EMA26; 조건 미충족; Chaikin3_10=-178256, ADL=1.4762e+07, close=119.52, EMA26=118.952; 직전 완료 봉 목표를 다음 봉 시가에 모의 적용 |
| v2 | roc_10_momentum | 10000.00 | 0.00 | 대기 /  / 새 신호 대기 |
| v2 | trix_15_trend | 9697.01 | -302.99 | sell / filled / 15봉 삼중 EMA의 1봉 변화율 TRIX > 0 그리고 종가 > EMA26; 조건 미충족; TRIX15_percent=0.0142754, close=118.77, EMA26=118.947; 직전 완료 봉 목표를 다음 봉 시가에 모의 적용 |
| v2 | keltner_20_breakout | 9933.99 | -66.01 | sell / filled / 종가 > EMA20 + 2 x Wilder ATR14; 조건 미충족; close=119.52, upper_Keltner=119.83, EMA20=119.013, ATR14=0.408312; 직전 완료 봉 목표를 다음 봉 시가에 모의 적용 |
| v2 | opening_range_30m | 9925.52 | -74.48 | sell / filled / 뉴욕 09:30·09:45 두 완료 봉 최고가를 10:00 이후 종가가 돌파; 조건 미충족; close=118.85, opening_high=119.14; 직전 완료 봉 목표를 다음 봉 시가에 모의 적용 |

### 같은 기간의 비용·노출 비교 (사후 연구)

| 전략 | 비용 전 | 비용 후 | 100% 보유 | 같은 평균 노출 보유 | 평균 노출 |
|---|---:|---:|---:|---:|---:|
| cash | 0.00% | 0.00% | 11.04% | 0.00% | 0.00% |
| buy_hold | 11.51% | 11.04% | 11.04% | 11.04% | 100.00% |
| trend_8_26 | 8.48% | 4.90% | 11.04% | 7.35% | 67.62% |
| momentum_26 | 10.00% | 4.15% | 11.04% | 7.58% | 69.71% |
| breakout_8 | 6.12% | -9.92% | 11.04% | 2.67% | 25.07% |
| reversion_12 | 4.06% | -8.64% | 11.04% | 1.94% | 18.28% |
| volume_26 | 0.56% | -5.18% | 11.04% | 0.55% | 5.22% |
| trend_8_26 AND momentum_26 | 8.21% | 3.32% | 11.04% | 6.76% | 62.40% |
| trend_8_26 + momentum_26 | 9.24% | 4.53% | 11.04% | 7.47% | 68.67% |
| trend_8_26 AND breakout_8 | 6.59% | -6.43% | 11.04% | 2.22% | 20.89% |
| trend_8_26 + breakout_8 | 7.31% | -2.78% | 11.04% | 4.98% | 46.35% |
| trend_8_26 AND reversion_12 | -0.07% | -6.17% | 11.04% | 0.69% | 6.53% |
| trend_8_26 + reversion_12 | 6.29% | -1.47% | 11.04% | 4.61% | 42.96% |
| trend_8_26 AND volume_26 | 0.24% | -2.26% | 11.04% | 0.22% | 2.09% |
| trend_8_26 + volume_26 | 4.48% | 0.16% | 11.04% | 3.90% | 36.43% |
| momentum_26 AND breakout_8 | 6.62% | -7.18% | 11.04% | 2.41% | 22.72% |
| momentum_26 + breakout_8 | 8.05% | -2.31% | 11.04% | 5.10% | 47.39% |
| momentum_26 AND reversion_12 | 1.23% | -4.95% | 11.04% | 0.80% | 7.57% |
| momentum_26 + reversion_12 | 7.03% | 0.05% | 11.04% | 4.73% | 44.00% |
| momentum_26 AND volume_26 | 1.64% | -2.54% | 11.04% | 0.30% | 2.87% |
| momentum_26 + volume_26 | 5.21% | -0.19% | 11.04% | 4.01% | 37.47% |
| breakout_8 AND reversion_12 | 0.00% | 0.00% | 11.04% | 0.00% | 0.00% |
| breakout_8 + reversion_12 | 5.11% | -8.51% | 11.04% | 2.30% | 21.68% |
| breakout_8 AND volume_26 | 0.78% | -2.14% | 11.04% | 0.22% | 2.09% |
| breakout_8 + volume_26 | 3.32% | -7.38% | 11.04% | 1.60% | 15.15% |
| reversion_12 AND volume_26 | -1.05% | -3.51% | 11.04% | 0.19% | 1.83% |
| reversion_12 + volume_26 | 2.30% | -6.34% | 11.04% | 1.24% | 11.75% |
| ema_12_26 | 11.20% | 9.81% | 11.04% | 7.88% | 72.32% |
| macd_12_26_9 | 8.67% | 4.64% | 11.04% | 3.85% | 36.03% |
| rsi_14_recovery | -0.25% | -1.50% | 11.04% | 0.08% | 0.78% |
| bollinger_20_reentry | 1.21% | -2.13% | 11.04% | 0.22% | 2.09% |
| donchian_20 | 4.55% | -7.44% | 11.04% | 1.35% | 12.79% |
| atr_14_breakout | -0.90% | -10.40% | 11.04% | 0.77% | 7.31% |
| session_vwap | 9.97% | 0.26% | 11.04% | 6.04% | 55.87% |
| obv_20 | 10.62% | 3.00% | 11.04% | 6.01% | 55.61% |
| stochastic_14_3_recovery | 0.90% | -9.54% | 11.04% | 0.72% | 6.79% |
| mfi_14_recovery | -0.04% | -1.29% | 11.04% | 0.08% | 0.78% |
| adx_14_trend | 8.73% | 6.47% | 11.04% | 5.34% | 49.61% |
| aroon_25_trend | 6.58% | 1.34% | 11.04% | 3.34% | 31.33% |
| cci_20_momentum | 6.31% | -1.85% | 11.04% | 3.34% | 31.33% |
| williams_14_recovery | -0.16% | -8.97% | 11.04% | 0.61% | 5.74% |
| cmf_20_accumulation | 9.93% | 1.50% | 11.04% | 3.77% | 35.25% |
| chaikin_3_10 | 9.85% | 1.42% | 11.04% | 5.52% | 51.17% |
| roc_10_momentum | -0.29% | -4.79% | 11.04% | 1.46% | 13.84% |
| trix_15_trend | 10.97% | 6.86% | 11.04% | 7.00% | 64.49% |
| keltner_20_breakout | 6.59% | 0.08% | 11.04% | 2.81% | 26.37% |
| opening_range_30m | 9.76% | 4.80% | 11.04% | 3.83% | 35.77% |

동일 구간·초기 자금, 종료 시 청산 비용 포함. 노출 맞춤은 사후 설명용이며 v2 실제 계좌 성과가 아닙니다.
[낙폭 분해·비용 영향·전체 구간](WMT/comparison.json)

[v1 전체 기록](WMT/accounts.json) · [v2 전체 기록](WMT/accounts-v2.json)
