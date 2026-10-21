# 모의투자 운영 현황

[PC·서버 장애 진단과 복구 방법](https://github.com/BaekJaeYeol/paper-trading-program/blob/main/investment-lab/docs/failure-recovery.md)

이번 실행 복구: {}

완료 봉 확인 주기: 기록 0/9회 · 기록 없는 예정 9회 · 아직 판정 전 17회 · 주의: 예약 시작 지연 또는 실행·저장 누락을 확인하세요.

[주기 판정 기준](https://github.com/BaekJaeYeol/paper-trading-program/blob/main/investment-lab/docs/session-coverage.md)

최근 확인: 2026-10-21T15:56:48.014467+00:00 (UTC)
다음 15분 확인 목표 (세션 실행 중에만 적용): 2026-10-21T16:07:00+00:00 (UTC, 실행 지연 가능)

실제 주문 없음. v1 기존 계좌와 v2 새 계좌의 시작일이 다르므로 수익률을 직접 우열 비교하지 마세요.
v2는 다음 봉 시가에 비용·스프레드·직전 거래량 제한을 적용한 가상 체결입니다. 미체결 잔량은 만료됩니다.

| 종목 | 상태 | 최근 성공 UTC | 마지막 완료 봉 UTC | 이번 새 봉 |
|---|---|---|---|---|
| SPY | updated | 2026-10-21T15:56:48.014467+00:00 | 2026-10-21T15:30:00+00:00 | 9 |
| QQQ | updated | 2026-10-21T15:56:48.014467+00:00 | 2026-10-21T15:30:00+00:00 | 9 |
| IWM | updated | 2026-10-21T15:56:48.014467+00:00 | 2026-10-21T15:30:00+00:00 | 9 |
| DIA | updated | 2026-10-21T15:56:48.014467+00:00 | 2026-10-21T15:30:00+00:00 | 9 |
| MSFT | updated | 2026-10-21T15:56:48.014467+00:00 | 2026-10-21T15:30:00+00:00 | 9 |
| JPM | updated | 2026-10-21T15:56:48.014467+00:00 | 2026-10-21T15:30:00+00:00 | 9 |
| XOM | updated | 2026-10-21T15:56:48.014467+00:00 | 2026-10-21T15:30:00+00:00 | 9 |
| JNJ | updated | 2026-10-21T15:56:48.014467+00:00 | 2026-10-21T15:30:00+00:00 | 9 |
| CAT | updated | 2026-10-21T15:56:48.014467+00:00 | 2026-10-21T15:30:00+00:00 | 9 |
| WMT | updated | 2026-10-21T15:56:48.014467+00:00 | 2026-10-21T15:30:00+00:00 | 9 |

이번 실행 소요: 49.0초
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
| v1 | buy_hold | 9970.87 | -29.13 | buy /  / buy_hold: prior completed bar target 100%; next bar open simulation |
| v1 | trend_8_26 | 9799.29 | -200.71 | buy /  / trend_8_26: prior completed bar target 100%; next bar open simulation |
| v1 | momentum_26 | 9725.23 | -274.77 | buy /  / momentum_26: prior completed bar target 100%; next bar open simulation |
| v1 | breakout_8 | 9652.43 | -347.57 | buy /  / breakout_8: prior completed bar target 100%; next bar open simulation |
| v1 | reversion_12 | 9722.53 | -277.47 | sell /  / reversion_12: prior completed bar target 0%; next bar open simulation |
| v1 | volume_26 | 9642.64 | -357.36 | sell /  / volume_26: prior completed bar target 0%; next bar open simulation |
| v1 | trend_8_26 AND momentum_26 | 9717.90 | -282.10 | buy /  / trend_8_26 AND momentum_26: prior completed bar target 100%; next bar open simulation |
| v1 | trend_8_26 + momentum_26 | 9762.17 | -237.83 | buy /  / trend_8_26 + momentum_26: prior completed bar target 100%; next bar open simulation |
| v1 | trend_8_26 AND breakout_8 | 9815.68 | -184.32 | buy /  / trend_8_26 AND breakout_8: prior completed bar target 100%; next bar open simulation |
| v1 | trend_8_26 + breakout_8 | 9764.46 | -235.54 | buy /  / trend_8_26 + breakout_8: prior completed bar target 100%; next bar open simulation |
| v1 | trend_8_26 AND reversion_12 | 9793.45 | -206.55 | sell /  / trend_8_26 AND reversion_12: prior completed bar target 0%; next bar open simulation |
| v1 | trend_8_26 + reversion_12 | 9760.67 | -239.33 | sell /  / trend_8_26 + reversion_12: prior completed bar target 50%; next bar open simulation |
| v1 | trend_8_26 AND volume_26 | 9688.02 | -311.98 | sell /  / trend_8_26 AND volume_26: prior completed bar target 0%; next bar open simulation |
| v1 | trend_8_26 + volume_26 | 9720.57 | -279.43 | sell /  / trend_8_26 + volume_26: prior completed bar target 50%; next bar open simulation |
| v1 | momentum_26 AND breakout_8 | 9724.19 | -275.81 | buy /  / momentum_26 AND breakout_8: prior completed bar target 100%; next bar open simulation |
| v1 | momentum_26 + breakout_8 | 9688.75 | -311.25 | buy /  / momentum_26 + breakout_8: prior completed bar target 100%; next bar open simulation |
| v1 | momentum_26 AND reversion_12 | 9794.14 | -205.86 | sell /  / momentum_26 AND reversion_12: prior completed bar target 0%; next bar open simulation |
| v1 | momentum_26 + reversion_12 | 9762.75 | -237.25 | sell /  / momentum_26 + reversion_12: prior completed bar target 50%; next bar open simulation |
| v1 | momentum_26 AND volume_26 | 9701.51 | -298.49 | sell /  / momentum_26 AND volume_26: prior completed bar target 0%; next bar open simulation |
| v1 | momentum_26 + volume_26 | 9683.77 | -316.23 | sell /  / momentum_26 + volume_26: prior completed bar target 50%; next bar open simulation |
| v1 | breakout_8 AND reversion_12 | 10000.00 | 0.00 | 대기 /  / 새 신호 대기 |
| v1 | breakout_8 + reversion_12 | 9687.17 | -312.83 | sell /  / breakout_8 + reversion_12: prior completed bar target 50%; next bar open simulation |
| v1 | breakout_8 AND volume_26 | 9878.80 | -121.20 | sell /  / breakout_8 AND volume_26: prior completed bar target 0%; next bar open simulation |
| v1 | breakout_8 + volume_26 | 9666.67 | -333.33 | sell /  / breakout_8 + volume_26: prior completed bar target 50%; next bar open simulation |
| v1 | reversion_12 AND volume_26 | 9861.02 | -138.98 | sell /  / reversion_12 AND volume_26: prior completed bar target 0%; next bar open simulation |
| v1 | reversion_12 + volume_26 | 9682.37 | -317.63 | sell /  / reversion_12 + volume_26: prior completed bar target 0%; next bar open simulation |
| v1 | ema_12_26 | 9831.00 | -169.00 | buy /  / EMA12 > EMA26; 조건 충족; EMA12=767.528, EMA26=767.458 |
| v1 | macd_12_26_9 | 9795.08 | -204.92 | buy /  / MACD > 신호선 그리고 MACD > 0; 조건 충족; MACD=0.244662, signal9=0.176064 |
| v1 | rsi_14_recovery | 9899.32 | -100.68 | sell /  / 직전 RSI14 < 30, 현재 RSI14 >= 30 (한 봉 목표); 조건 미충족; RSI14=34.3611, previous_RSI14=32.906 |
| v1 | bollinger_20_reentry | 9835.17 | -164.83 | sell /  / 직전 종가 < 직전 하단밴드, 현재 하단밴드 <= 종가 <= SMA20 (한 봉 목표); 조건 미충족; close=763.39, lower20=762.854, SMA20=768.639, previous_lower20=763.636 |
| v1 | donchian_20 | 9913.28 | -86.72 | buy /  / 종가 > 현재 봉을 제외한 직전 20봉 최고가; 조건 충족; close=771.43, prior_high20=771.34 |
| v1 | atr_14_breakout | 9858.15 | -141.85 | sell /  / 종가 > 직전 종가 + 직전 ATR14 그리고 종가 > EMA26; 조건 미충족; close=770.65, threshold=771.314, prior_ATR14=1.1542, EMA26=769.052 |
| v1 | session_vwap | 9726.52 | -273.48 | buy /  / 종가 > 뉴욕 거래일별 누적 전형가격 VWAP; 조건 충족; close=770.23, session_VWAP=770.038, session_volume=6.50217e+06 |
| v1 | obv_20 | 9801.29 | -198.71 | buy /  / OBV > OBV의 SMA20 그리고 종가 > EMA26; 조건 충족; OBV=-4.30721e+07, OBV_SMA20=-5.00094e+07, close=769.37, EMA26=769.056 |
| v1 | stochastic_14_3_recovery | 9694.64 | -305.36 | sell /  / 직전 %K14 < 20에서 %K14가 %D3 상향 돌파 (한 봉 목표); 조건 미충족; K14=53.6357, D3=31.478, previous_K14=28.6364, previous_D3=21.2782 |
| v1 | mfi_14_recovery | 9875.98 | -124.02 | sell /  / 직전 MFI14 < 20, 현재 MFI14 >= 20 (한 봉 목표); 조건 미충족; MFI14=33.0962, previous_MFI14=27.4403 |
| v1 | adx_14_trend | 9981.96 | -18.04 | sell /  / Wilder ADX14 >= 25 그리고 +DI14 > -DI14; 조건 미충족; ADX14=24.2312, plus_DI14=28.3519, minus_DI14=24.6578 |
| v1 | aroon_25_trend | 9861.30 | -138.70 | sell /  / Aroon25 Up > 70 그리고 Down < 30 (동률이면 최신 극값); 조건 미충족; Aroon_up=68, Aroon_down=20 |
| v1 | cci_20_momentum | 9769.35 | -230.65 | buy /  / CCI20 > 100 (전형가격·평균절대편차); 조건 충족; CCI20=100.444 |
| v1 | williams_14_recovery | 9666.94 | -333.06 | sell /  / 직전 Williams %R14 < -80, 현재 >= -80 (한 봉 목표); 조건 미충족; Williams_R14=-46.3643, previous_R14=-71.3636 |
| v1 | cmf_20_accumulation | 9913.16 | -86.84 | buy /  / Chaikin Money Flow20 > 0.1; 조건 충족; CMF20=0.124634, volume20=9.6482e+07 |
| v1 | chaikin_3_10 | 9711.71 | -288.29 | buy /  / ADL의 EMA3 - EMA10 > 0 그리고 종가 > EMA26; 조건 충족; Chaikin3_10=644152, ADL=1.0752e+07, close=769.37, EMA26=769.056 |
| v1 | roc_10_momentum | 9953.42 | -46.58 | sell /  / 10봉 ROC > 1% 그리고 종가 > EMA26; 조건 미충족; ROC10_percent=0.806376, close=769.45, EMA26=767.181 |
| v1 | trix_15_trend | 9635.17 | -364.83 | buy /  / 15봉 삼중 EMA의 1봉 변화율 TRIX > 0 그리고 종가 > EMA26; 조건 충족; TRIX15_percent=0.00337952, close=769.37, EMA26=769.056 |
| v1 | keltner_20_breakout | 9924.71 | -75.29 | sell /  / 종가 > EMA20 + 2 x Wilder ATR14; 조건 미충족; close=768.93, upper_Keltner=771.837, EMA20=768.595, ATR14=1.6209 |
| v1 | opening_range_30m | 9744.89 | -255.11 | buy /  / 뉴욕 09:30·09:45 두 완료 봉 최고가를 10:00 이후 종가가 돌파; 조건 충족; close=771.43, opening_high=771.34 |
| v2 | cash | 10000.00 | 0.00 | 대기 /  / 새 신호 대기 |
| v2 | buy_hold | 9898.95 | -101.05 | buy / partial / 직전 완료 봉 목표 비중 100%; 다음 봉 시가 가정 |
| v2 | trend_8_26 | 9679.32 | -320.68 | buy / partial / 직전 완료 봉 목표 비중 100%; 다음 봉 시가 가정 |
| v2 | momentum_26 | 9575.42 | -424.58 | buy / partial / 직전 완료 봉 목표 비중 100%; 다음 봉 시가 가정 |
| v2 | breakout_8 | 9249.25 | -750.75 | buy / partial / 직전 완료 봉 목표 비중 100%; 다음 봉 시가 가정 |
| v2 | reversion_12 | 9256.42 | -743.58 | sell / filled / 직전 완료 봉 목표 비중 0%; 다음 봉 시가 가정 |
| v2 | volume_26 | 9091.31 | -908.69 | sell / filled / 직전 완료 봉 목표 비중 0%; 다음 봉 시가 가정 |
| v2 | trend_8_26 AND momentum_26 | 9574.73 | -425.27 | buy / partial / 직전 완료 봉 목표 비중 100%; 다음 봉 시가 가정 |
| v2 | trend_8_26 + momentum_26 | 9627.22 | -372.78 | buy / partial / 직전 완료 봉 목표 비중 100%; 다음 봉 시가 가정 |
| v2 | trend_8_26 AND breakout_8 | 9635.44 | -364.56 | buy / partial / 직전 완료 봉 목표 비중 100%; 다음 봉 시가 가정 |
| v2 | trend_8_26 + breakout_8 | 9501.45 | -498.55 | buy / partial / 직전 완료 봉 목표 비중 100%; 다음 봉 시가 가정 |
| v2 | trend_8_26 AND reversion_12 | 9682.03 | -317.97 | sell / filled / 직전 완료 봉 목표 비중 0%; 다음 봉 시가 가정 |
| v2 | trend_8_26 + reversion_12 | 9465.03 | -534.97 | sell / filled / 직전 완료 봉 목표 비중 50%; 다음 봉 시가 가정 |
| v2 | trend_8_26 AND volume_26 | 9527.29 | -472.71 | sell / filled / 직전 완료 봉 목표 비중 0%; 다음 봉 시가 가정 |
| v2 | trend_8_26 + volume_26 | 9400.13 | -599.87 | sell / filled / 직전 완료 봉 목표 비중 50%; 다음 봉 시가 가정 |
| v2 | momentum_26 AND breakout_8 | 9501.33 | -498.67 | buy / partial / 직전 완료 봉 목표 비중 100%; 다음 봉 시가 가정 |
| v2 | momentum_26 + breakout_8 | 9410.83 | -589.17 | buy / partial / 직전 완료 봉 목표 비중 100%; 다음 봉 시가 가정 |
| v2 | momentum_26 AND reversion_12 | 9748.35 | -251.65 | sell / filled / 직전 완료 봉 목표 비중 0%; 다음 봉 시가 가정 |
| v2 | momentum_26 + reversion_12 | 9473.66 | -526.34 | sell / filled / 직전 완료 봉 목표 비중 50%; 다음 봉 시가 가정 |
| v2 | momentum_26 AND volume_26 | 9609.69 | -390.31 | sell / filled / 직전 완료 봉 목표 비중 0%; 다음 봉 시가 가정 |
| v2 | momentum_26 + volume_26 | 9388.86 | -611.14 | sell / filled / 직전 완료 봉 목표 비중 50%; 다음 봉 시가 가정 |
| v2 | breakout_8 AND reversion_12 | 10000.00 | 0.00 | 대기 /  / 새 신호 대기 |
| v2 | breakout_8 + reversion_12 | 9291.10 | -708.90 | sell / filled / 직전 완료 봉 목표 비중 50%; 다음 봉 시가 가정 |
| v2 | breakout_8 AND volume_26 | 9808.87 | -191.13 | sell / filled / 직전 완료 봉 목표 비중 0%; 다음 봉 시가 가정 |
| v2 | breakout_8 + volume_26 | 9227.37 | -772.63 | sell / filled / 직전 완료 봉 목표 비중 50%; 다음 봉 시가 가정 |
| v2 | reversion_12 AND volume_26 | 9602.16 | -397.84 | sell / filled / 직전 완료 봉 목표 비중 0%; 다음 봉 시가 가정 |
| v2 | reversion_12 + volume_26 | 9250.48 | -749.52 | sell / filled / 직전 완료 봉 목표 비중 0%; 다음 봉 시가 가정 |
| v2 | ema_12_26 | 9826.08 | -173.92 | buy / partial / EMA12 > EMA26; 조건 충족; EMA12=767.528, EMA26=767.458; 직전 완료 봉 목표를 다음 봉 시가에 모의 적용 |
| v2 | macd_12_26_9 | 9788.22 | -211.78 | buy / partial / MACD > 신호선 그리고 MACD > 0; 조건 충족; MACD=0.244662, signal9=0.176064; 직전 완료 봉 목표를 다음 봉 시가에 모의 적용 |
| v2 | rsi_14_recovery | 9895.36 | -104.64 | sell / filled / 직전 RSI14 < 30, 현재 RSI14 >= 30 (한 봉 목표); 조건 미충족; RSI14=34.3611, previous_RSI14=32.906; 직전 완료 봉 목표를 다음 봉 시가에 모의 적용 |
| v2 | bollinger_20_reentry | 9829.27 | -170.73 | sell / filled / 직전 종가 < 직전 하단밴드, 현재 하단밴드 <= 종가 <= SMA20 (한 봉 목표); 조건 미충족; close=763.39, lower20=762.854, SMA20=768.639, previous_lower20=763.636; 직전 완료 봉 목표를 다음 봉 시가에 모의 적용 |
| v2 | donchian_20 | 9908.33 | -91.67 | buy / partial / 종가 > 현재 봉을 제외한 직전 20봉 최고가; 조건 충족; close=771.43, prior_high20=771.34; 직전 완료 봉 목표를 다음 봉 시가에 모의 적용 |
| v2 | atr_14_breakout | 9850.26 | -149.74 | sell / filled / 종가 > 직전 종가 + 직전 ATR14 그리고 종가 > EMA26; 조건 미충족; close=770.65, threshold=771.314, prior_ATR14=1.1542, EMA26=769.052; 직전 완료 봉 목표를 다음 봉 시가에 모의 적용 |
| v2 | session_vwap | 9713.88 | -286.12 | buy / partial / 종가 > 뉴욕 거래일별 누적 전형가격 VWAP; 조건 충족; close=770.23, session_VWAP=770.038, session_volume=6.50217e+06; 직전 완료 봉 목표를 다음 봉 시가에 모의 적용 |
| v2 | obv_20 | 9792.47 | -207.53 | buy / partial / OBV > OBV의 SMA20 그리고 종가 > EMA26; 조건 충족; OBV=-4.30721e+07, OBV_SMA20=-5.00094e+07, close=769.37, EMA26=769.056; 직전 완료 봉 목표를 다음 봉 시가에 모의 적용 |
| v2 | stochastic_14_3_recovery | 9677.21 | -322.79 | sell / filled / 직전 %K14 < 20에서 %K14가 %D3 상향 돌파 (한 봉 목표); 조건 미충족; K14=53.6357, D3=31.478, previous_K14=28.6364, previous_D3=21.2782; 직전 완료 봉 목표를 다음 봉 시가에 모의 적용 |
| v2 | mfi_14_recovery | 9870.05 | -129.95 | sell / filled / 직전 MFI14 < 20, 현재 MFI14 >= 20 (한 봉 목표); 조건 미충족; MFI14=33.0962, previous_MFI14=27.4403; 직전 완료 봉 목표를 다음 봉 시가에 모의 적용 |
| v2 | adx_14_trend | 9979.97 | -20.03 | sell / filled / Wilder ADX14 >= 25 그리고 +DI14 > -DI14; 조건 미충족; ADX14=24.2312, plus_DI14=28.3519, minus_DI14=24.6578; 직전 완료 봉 목표를 다음 봉 시가에 모의 적용 |
| v2 | aroon_25_trend | 9857.36 | -142.64 | sell / filled / Aroon25 Up > 70 그리고 Down < 30 (동률이면 최신 극값); 조건 미충족; Aroon_up=68, Aroon_down=20; 직전 완료 봉 목표를 다음 봉 시가에 모의 적용 |
| v2 | cci_20_momentum | 9758.61 | -241.39 | buy / partial / CCI20 > 100 (전형가격·평균절대편차); 조건 충족; CCI20=100.444; 직전 완료 봉 목표를 다음 봉 시가에 모의 적용 |
| v2 | williams_14_recovery | 9649.55 | -350.45 | sell / filled / 직전 Williams %R14 < -80, 현재 >= -80 (한 봉 목표); 조건 미충족; Williams_R14=-46.3643, previous_R14=-71.3636; 직전 완료 봉 목표를 다음 봉 시가에 모의 적용 |
| v2 | cmf_20_accumulation | 9908.21 | -91.79 | buy / partial / Chaikin Money Flow20 > 0.1; 조건 충족; CMF20=0.124634, volume20=9.6482e+07; 직전 완료 봉 목표를 다음 봉 시가에 모의 적용 |
| v2 | chaikin_3_10 | 9699.09 | -300.91 | buy / partial / ADL의 EMA3 - EMA10 > 0 그리고 종가 > EMA26; 조건 충족; Chaikin3_10=644152, ADL=1.0752e+07, close=769.37, EMA26=769.056; 직전 완료 봉 목표를 다음 봉 시가에 모의 적용 |
| v2 | roc_10_momentum | 9951.43 | -48.57 | sell / filled / 10봉 ROC > 1% 그리고 종가 > EMA26; 조건 미충족; ROC10_percent=0.806376, close=769.45, EMA26=767.181; 직전 완료 봉 목표를 다음 봉 시가에 모의 적용 |
| v2 | trix_15_trend | 9620.73 | -379.27 | buy / partial / 15봉 삼중 EMA의 1봉 변화율 TRIX > 0 그리고 종가 > EMA26; 조건 충족; TRIX15_percent=0.00337952, close=769.37, EMA26=769.056; 직전 완료 봉 목표를 다음 봉 시가에 모의 적용 |
| v2 | keltner_20_breakout | 9922.73 | -77.27 | sell / filled / 종가 > EMA20 + 2 x Wilder ATR14; 조건 미충족; close=768.93, upper_Keltner=771.837, EMA20=768.595, ATR14=1.6209; 직전 완료 봉 목표를 다음 봉 시가에 모의 적용 |
| v2 | opening_range_30m | 9734.17 | -265.83 | buy / partial / 뉴욕 09:30·09:45 두 완료 봉 최고가를 10:00 이후 종가가 돌파; 조건 충족; close=771.43, opening_high=771.34; 직전 완료 봉 목표를 다음 봉 시가에 모의 적용 |

### 같은 기간의 비용·노출 비교 (사후 연구)

| 전략 | 비용 전 | 비용 후 | 100% 보유 | 같은 평균 노출 보유 | 평균 노출 |
|---|---:|---:|---:|---:|---:|
| cash | 0.00% | 0.00% | 0.33% | 0.00% | 0.00% |
| buy_hold | 0.75% | 0.33% | 0.33% | 0.33% | 100.00% |
| trend_8_26 | 1.05% | -3.11% | 0.33% | 0.17% | 52.51% |
| momentum_26 | -0.67% | -5.55% | 0.33% | 0.17% | 52.77% |
| breakout_8 | -0.38% | -16.14% | 0.33% | 0.07% | 22.69% |
| reversion_12 | -1.27% | -11.85% | 0.33% | 0.09% | 27.18% |
| volume_26 | -1.25% | -9.96% | 0.33% | 0.03% | 8.97% |
| trend_8_26 AND momentum_26 | 0.23% | -4.70% | 0.33% | 0.15% | 44.59% |
| trend_8_26 + momentum_26 | 0.19% | -4.34% | 0.33% | 0.17% | 52.64% |
| trend_8_26 AND breakout_8 | -0.00% | -10.72% | 0.33% | 0.04% | 13.46% |
| trend_8_26 + breakout_8 | 0.34% | -9.48% | 0.33% | 0.12% | 37.61% |
| trend_8_26 AND reversion_12 | -0.03% | -4.54% | 0.33% | 0.02% | 6.33% |
| trend_8_26 + reversion_12 | -0.11% | -7.40% | 0.33% | 0.13% | 39.85% |
| trend_8_26 AND volume_26 | -0.99% | -5.46% | 0.33% | 0.02% | 5.01% |
| trend_8_26 + volume_26 | -0.10% | -6.60% | 0.33% | 0.10% | 30.74% |
| momentum_26 AND breakout_8 | 0.17% | -11.32% | 0.33% | 0.05% | 15.04% |
| momentum_26 + breakout_8 | -0.52% | -11.00% | 0.33% | 0.12% | 37.74% |
| momentum_26 AND reversion_12 | -0.79% | -6.06% | 0.33% | 0.02% | 7.12% |
| momentum_26 + reversion_12 | -0.97% | -8.19% | 0.33% | 0.13% | 39.98% |
| momentum_26 AND volume_26 | -0.74% | -4.42% | 0.33% | 0.01% | 3.43% |
| momentum_26 + volume_26 | -0.96% | -6.82% | 0.33% | 0.10% | 30.87% |
| breakout_8 AND reversion_12 | 0.00% | 0.00% | 0.33% | 0.00% | 0.00% |
| breakout_8 + reversion_12 | -0.82% | -13.67% | 0.33% | 0.08% | 24.94% |
| breakout_8 AND volume_26 | -0.33% | -2.40% | 0.33% | 0.01% | 1.85% |
| breakout_8 + volume_26 | -0.81% | -12.75% | 0.33% | 0.05% | 15.84% |
| reversion_12 AND volume_26 | -0.87% | -5.34% | 0.33% | 0.01% | 3.96% |
| reversion_12 + volume_26 | -1.26% | -10.73% | 0.33% | 0.06% | 18.08% |
| ema_12_26 | -0.13% | -3.84% | 0.33% | 0.19% | 56.46% |
| macd_12_26_9 | 0.27% | -4.66% | 0.33% | 0.11% | 32.45% |
| rsi_14_recovery | -0.53% | -4.22% | 0.33% | 0.01% | 2.37% |
| bollinger_20_reentry | -1.07% | -6.72% | 0.33% | 0.01% | 3.69% |
| donchian_20 | 0.02% | -7.65% | 0.33% | 0.02% | 6.86% |
| atr_14_breakout | 0.32% | -5.40% | 0.33% | 0.01% | 3.96% |
| session_vwap | 1.83% | -8.32% | 0.33% | 0.15% | 45.38% |
| obv_20 | -0.06% | -8.11% | 0.33% | 0.13% | 39.58% |
| stochastic_14_3_recovery | -0.08% | -14.46% | 0.33% | 0.03% | 9.76% |
| mfi_14_recovery | 0.04% | -2.86% | 0.33% | 0.01% | 1.85% |
| adx_14_trend | 0.57% | -2.34% | 0.33% | 0.08% | 25.33% |
| aroon_25_trend | 0.89% | -1.62% | 0.33% | 0.08% | 24.27% |
| cci_20_momentum | -0.21% | -9.02% | 0.33% | 0.07% | 22.69% |
| williams_14_recovery | -0.26% | -10.95% | 0.33% | 0.02% | 7.12% |
| cmf_20_accumulation | 1.97% | -1.81% | 0.33% | 0.15% | 44.33% |
| chaikin_3_10 | 1.65% | -5.36% | 0.33% | 0.14% | 42.22% |
| roc_10_momentum | -0.13% | -0.97% | 0.33% | 0.00% | 1.06% |
| trix_15_trend | -0.23% | -5.13% | 0.33% | 0.14% | 41.69% |
| keltner_20_breakout | -0.27% | -3.57% | 0.33% | 0.03% | 10.55% |
| opening_range_30m | 0.50% | -5.64% | 0.33% | 0.12% | 36.68% |

동일 구간·초기 자금, 종료 시 청산 비용 포함. 노출 맞춤은 사후 설명용이며 v2 실제 계좌 성과가 아닙니다.
[낙폭 분해·비용 영향·전체 구간](SPY/comparison.json)

[v1 전체 기록](SPY/accounts.json) · [v2 전체 기록](SPY/accounts-v2.json)

## QQQ 계좌

| 모델 | 전략 | 평가액 USD | 손익 USD | 최근 매매·이유 |
|---|---|---:|---:|---|
| v1 | cash | 10000.00 | 0.00 | 대기 /  / 새 신호 대기 |
| v1 | buy_hold | 9986.76 | -13.24 | buy /  / buy_hold: prior completed bar target 100%; next bar open simulation |
| v1 | trend_8_26 | 9865.58 | -134.42 | buy /  / trend_8_26: prior completed bar target 100%; next bar open simulation |
| v1 | momentum_26 | 9549.91 | -450.09 | buy /  / momentum_26: prior completed bar target 100%; next bar open simulation |
| v1 | breakout_8 | 9666.86 | -333.14 | buy /  / breakout_8: prior completed bar target 100%; next bar open simulation |
| v1 | reversion_12 | 9765.33 | -234.67 | sell /  / reversion_12: prior completed bar target 0%; next bar open simulation |
| v1 | volume_26 | 9622.97 | -377.03 | buy /  / volume_26: prior completed bar target 100%; next bar open simulation |
| v1 | trend_8_26 AND momentum_26 | 9918.72 | -81.28 | buy /  / trend_8_26 AND momentum_26: prior completed bar target 100%; next bar open simulation |
| v1 | trend_8_26 + momentum_26 | 9745.43 | -254.57 | buy /  / trend_8_26 + momentum_26: prior completed bar target 100%; next bar open simulation |
| v1 | trend_8_26 AND breakout_8 | 10004.83 | 4.83 | buy /  / trend_8_26 AND breakout_8: prior completed bar target 100%; next bar open simulation |
| v1 | trend_8_26 + breakout_8 | 9804.82 | -195.18 | buy /  / trend_8_26 + breakout_8: prior completed bar target 100%; next bar open simulation |
| v1 | trend_8_26 AND reversion_12 | 9902.56 | -97.44 | sell /  / trend_8_26 AND reversion_12: prior completed bar target 0%; next bar open simulation |
| v1 | trend_8_26 + reversion_12 | 9835.06 | -164.94 | sell /  / trend_8_26 + reversion_12: prior completed bar target 50%; next bar open simulation |
| v1 | trend_8_26 AND volume_26 | 9863.13 | -136.87 | buy /  / trend_8_26 AND volume_26: prior completed bar target 100%; next bar open simulation |
| v1 | trend_8_26 + volume_26 | 9743.45 | -256.55 | buy /  / trend_8_26 + volume_26: prior completed bar target 100%; next bar open simulation |
| v1 | momentum_26 AND breakout_8 | 9698.16 | -301.84 | buy /  / momentum_26 AND breakout_8: prior completed bar target 100%; next bar open simulation |
| v1 | momentum_26 + breakout_8 | 9608.29 | -391.71 | buy /  / momentum_26 + breakout_8: prior completed bar target 100%; next bar open simulation |
| v1 | momentum_26 AND reversion_12 | 9800.84 | -199.16 | sell /  / momentum_26 AND reversion_12: prior completed bar target 0%; next bar open simulation |
| v1 | momentum_26 + reversion_12 | 9695.89 | -304.11 | sell /  / momentum_26 + reversion_12: prior completed bar target 50%; next bar open simulation |
| v1 | momentum_26 AND volume_26 | 9835.55 | -164.45 | buy /  / momentum_26 AND volume_26: prior completed bar target 100%; next bar open simulation |
| v1 | momentum_26 + volume_26 | 9605.51 | -394.49 | buy /  / momentum_26 + volume_26: prior completed bar target 100%; next bar open simulation |
| v1 | breakout_8 AND reversion_12 | 10000.00 | 0.00 | 대기 /  / 새 신호 대기 |
| v1 | breakout_8 + reversion_12 | 9754.98 | -245.02 | sell /  / breakout_8 + reversion_12: prior completed bar target 50%; next bar open simulation |
| v1 | breakout_8 AND volume_26 | 9945.93 | -54.07 | buy /  / breakout_8 AND volume_26: prior completed bar target 100%; next bar open simulation |
| v1 | breakout_8 + volume_26 | 9664.19 | -335.81 | buy /  / breakout_8 + volume_26: prior completed bar target 100%; next bar open simulation |
| v1 | reversion_12 AND volume_26 | 9907.31 | -92.69 | sell /  / reversion_12 AND volume_26: prior completed bar target 0%; next bar open simulation |
| v1 | reversion_12 + volume_26 | 9732.72 | -267.28 | sell /  / reversion_12 + volume_26: prior completed bar target 50%; next bar open simulation |
| v1 | ema_12_26 | 9620.47 | -379.53 | buy /  / EMA12 > EMA26; 조건 충족; EMA12=719.205, EMA26=719.04 |
| v1 | macd_12_26_9 | 9772.20 | -227.80 | buy /  / MACD > 신호선 그리고 MACD > 0; 조건 충족; MACD=0.165076, signal9=-0.134014 |
| v1 | rsi_14_recovery | 9809.40 | -190.60 | sell /  / 직전 RSI14 < 30, 현재 RSI14 >= 30 (한 봉 목표); 조건 미충족; RSI14=50.2063, previous_RSI14=44.1729 |
| v1 | bollinger_20_reentry | 9878.60 | -121.40 | sell /  / 직전 종가 < 직전 하단밴드, 현재 하단밴드 <= 종가 <= SMA20 (한 봉 목표); 조건 미충족; close=718.66, lower20=714.386, SMA20=719.409, previous_lower20=714.271 |
| v1 | donchian_20 | 9949.90 | -50.10 | buy /  / 종가 > 현재 봉을 제외한 직전 20봉 최고가; 조건 충족; close=724.62, prior_high20=723.805 |
| v1 | atr_14_breakout | 9930.01 | -69.99 | sell /  / 종가 > 직전 종가 + 직전 ATR14 그리고 종가 > EMA26; 조건 미충족; close=722.535, threshold=722.712, prior_ATR14=1.8425, EMA26=719.04 |
| v1 | session_vwap | 9727.77 | -272.23 | buy /  / 종가 > 뉴욕 거래일별 누적 전형가격 VWAP; 조건 충족; close=721.81, session_VWAP=721.45, session_volume=2.32267e+07 |
| v1 | obv_20 | 9752.13 | -247.87 | buy /  / OBV > OBV의 SMA20 그리고 종가 > EMA26; 조건 충족; OBV=2.23867e+08, OBV_SMA20=2.10034e+08, close=722.48, EMA26=719.576 |
| v1 | stochastic_14_3_recovery | 9598.51 | -401.49 | sell /  / 직전 %K14 < 20에서 %K14가 %D3 상향 돌파 (한 봉 목표); 조건 미충족; K14=21.6302, D3=18.3878, previous_K14=24.7642, previous_D3=19.9023 |
| v1 | mfi_14_recovery | 9813.56 | -186.44 | sell /  / 직전 MFI14 < 20, 현재 MFI14 >= 20 (한 봉 목표); 조건 미충족; MFI14=30.3876, previous_MFI14=31.1747 |
| v1 | adx_14_trend | 9926.53 | -73.47 | sell /  / Wilder ADX14 >= 25 그리고 +DI14 > -DI14; 조건 미충족; ADX14=23.9831, plus_DI14=26.5781, minus_DI14=24.6326 |
| v1 | aroon_25_trend | 9831.22 | -168.78 | sell /  / Aroon25 Up > 70 그리고 Down < 30 (동률이면 최신 극값); 조건 미충족; Aroon_up=100, Aroon_down=80 |
| v1 | cci_20_momentum | 9930.63 | -69.37 | buy /  / CCI20 > 100 (전형가격·평균절대편차); 조건 충족; CCI20=222.381 |
| v1 | williams_14_recovery | 9689.61 | -310.39 | sell /  / 직전 Williams %R14 < -80, 현재 >= -80 (한 봉 목표); 조건 미충족; Williams_R14=-78.3698, previous_R14=-75.2358 |
| v1 | cmf_20_accumulation | 9580.30 | -419.70 | buy /  / Chaikin Money Flow20 > 0.1; 조건 충족; CMF20=0.185201, volume20=2.07769e+08 |
| v1 | chaikin_3_10 | 9758.98 | -241.02 | buy /  / ADL의 EMA3 - EMA10 > 0 그리고 종가 > EMA26; 조건 충족; Chaikin3_10=659089, ADL=2.27792e+08, close=722.48, EMA26=719.576 |
| v1 | roc_10_momentum | 9983.89 | -16.11 | buy /  / 10봉 ROC > 1% 그리고 종가 > EMA26; 조건 충족; ROC10_percent=1.06205, close=724.74, EMA26=720.545 |
| v1 | trix_15_trend | 9709.36 | -290.64 | buy /  / 15봉 삼중 EMA의 1봉 변화율 TRIX > 0 그리고 종가 > EMA26; 조건 충족; TRIX15_percent=3.24292e-05, close=721.81, EMA26=719.344 |
| v1 | keltner_20_breakout | 9869.95 | -130.05 | sell /  / 종가 > EMA20 + 2 x Wilder ATR14; 조건 미충족; close=724.74, upper_Keltner=724.763, EMA20=720.919, ATR14=1.92215 |
| v1 | opening_range_30m | 9783.33 | -216.67 | buy /  / 뉴욕 09:30·09:45 두 완료 봉 최고가를 10:00 이후 종가가 돌파; 조건 충족; close=723.37, opening_high=723.2 |
| v2 | cash | 10000.00 | 0.00 | 대기 /  / 새 신호 대기 |
| v2 | buy_hold | 9663.94 | -336.06 | buy / partial / 직전 완료 봉 목표 비중 100%; 다음 봉 시가 가정 |
| v2 | trend_8_26 | 9665.14 | -334.86 | buy / partial / 직전 완료 봉 목표 비중 100%; 다음 봉 시가 가정 |
| v2 | momentum_26 | 9440.00 | -560.00 | buy / partial / 직전 완료 봉 목표 비중 100%; 다음 봉 시가 가정 |
| v2 | breakout_8 | 9333.71 | -666.29 | buy / partial / 직전 완료 봉 목표 비중 100%; 다음 봉 시가 가정 |
| v2 | reversion_12 | 9275.81 | -724.19 | sell / filled / 직전 완료 봉 목표 비중 0%; 다음 봉 시가 가정 |
| v2 | volume_26 | 9565.80 | -434.20 | 중단: 손실 한도 / sell / filled / 직전 완료 봉 목표 비중 0%; 다음 봉 시가 가정 |
| v2 | trend_8_26 AND momentum_26 | 9812.42 | -187.58 | buy / partial / 직전 완료 봉 목표 비중 100%; 다음 봉 시가 가정 |
| v2 | trend_8_26 + momentum_26 | 9592.21 | -407.79 | buy / partial / 직전 완료 봉 목표 비중 100%; 다음 봉 시가 가정 |
| v2 | trend_8_26 AND breakout_8 | 9897.64 | -102.36 | buy / partial / 직전 완료 봉 목표 비중 100%; 다음 봉 시가 가정 |
| v2 | trend_8_26 + breakout_8 | 9537.87 | -462.13 | buy / partial / 직전 완료 봉 목표 비중 100%; 다음 봉 시가 가정 |
| v2 | trend_8_26 AND reversion_12 | 9761.15 | -238.85 | sell / filled / 직전 완료 봉 목표 비중 0%; 다음 봉 시가 가정 |
| v2 | trend_8_26 + reversion_12 | 9488.14 | -511.86 | sell / filled / 직전 완료 봉 목표 비중 50%; 다음 봉 시가 가정 |
| v2 | trend_8_26 AND volume_26 | 9696.68 | -303.32 | buy / partial / 직전 완료 봉 목표 비중 100%; 다음 봉 시가 가정 |
| v2 | trend_8_26 + volume_26 | 9345.52 | -654.48 | buy / partial / 직전 완료 봉 목표 비중 100%; 다음 봉 시가 가정 |
| v2 | momentum_26 AND breakout_8 | 9647.49 | -352.51 | buy / partial / 직전 완료 봉 목표 비중 100%; 다음 봉 시가 가정 |
| v2 | momentum_26 + breakout_8 | 9386.74 | -613.26 | buy / partial / 직전 완료 봉 목표 비중 100%; 다음 봉 시가 가정 |
| v2 | momentum_26 AND reversion_12 | 9794.96 | -205.04 | sell / filled / 직전 완료 봉 목표 비중 0%; 다음 봉 시가 가정 |
| v2 | momentum_26 + reversion_12 | 9416.50 | -583.50 | sell / filled / 직전 완료 봉 목표 비중 50%; 다음 봉 시가 가정 |
| v2 | momentum_26 AND volume_26 | 9766.59 | -233.41 | buy / partial / 직전 완료 봉 목표 비중 100%; 다음 봉 시가 가정 |
| v2 | momentum_26 + volume_26 | 9255.44 | -744.56 | buy / partial / 직전 완료 봉 목표 비중 100%; 다음 봉 시가 가정 |
| v2 | breakout_8 AND reversion_12 | 10000.00 | 0.00 | 대기 /  / 새 신호 대기 |
| v2 | breakout_8 + reversion_12 | 9402.67 | -597.33 | sell / filled / 직전 완료 봉 목표 비중 50%; 다음 봉 시가 가정 |
| v2 | breakout_8 AND volume_26 | 9889.25 | -110.75 | buy / partial / 직전 완료 봉 목표 비중 100%; 다음 봉 시가 가정 |
| v2 | breakout_8 + volume_26 | 9242.04 | -757.96 | buy / partial / 직전 완료 봉 목표 비중 100%; 다음 봉 시가 가정 |
| v2 | reversion_12 AND volume_26 | 9547.64 | -452.36 | 중단: 손실 한도 / sell / filled / 직전 완료 봉 목표 비중 0%; 다음 봉 시가 가정 |
| v2 | reversion_12 + volume_26 | 9213.40 | -786.60 | sell / filled / 직전 완료 봉 목표 비중 50%; 다음 봉 시가 가정 |
| v2 | ema_12_26 | 9611.82 | -388.18 | buy / partial / EMA12 > EMA26; 조건 충족; EMA12=719.205, EMA26=719.04; 직전 완료 봉 목표를 다음 봉 시가에 모의 적용 |
| v2 | macd_12_26_9 | 9763.41 | -236.59 | buy / partial / MACD > 신호선 그리고 MACD > 0; 조건 충족; MACD=0.165076, signal9=-0.134014; 직전 완료 봉 목표를 다음 봉 시가에 모의 적용 |
| v2 | rsi_14_recovery | 9801.56 | -198.44 | sell / filled / 직전 RSI14 < 30, 현재 RSI14 >= 30 (한 봉 목표); 조건 미충족; RSI14=50.2063, previous_RSI14=44.1729; 직전 완료 봉 목표를 다음 봉 시가에 모의 적용 |
| v2 | bollinger_20_reentry | 9872.68 | -127.32 | sell / filled / 직전 종가 < 직전 하단밴드, 현재 하단밴드 <= 종가 <= SMA20 (한 봉 목표); 조건 미충족; close=718.66, lower20=714.386, SMA20=719.409, previous_lower20=714.271; 직전 완료 봉 목표를 다음 봉 시가에 모의 적용 |
| v2 | donchian_20 | 9944.92 | -55.08 | buy / partial / 종가 > 현재 봉을 제외한 직전 20봉 최고가; 조건 충족; close=724.62, prior_high20=723.805; 직전 완료 봉 목표를 다음 봉 시가에 모의 적용 |
| v2 | atr_14_breakout | 9924.06 | -75.94 | sell / filled / 종가 > 직전 종가 + 직전 ATR14 그리고 종가 > EMA26; 조건 미충족; close=722.535, threshold=722.712, prior_ATR14=1.8425, EMA26=719.04; 직전 완료 봉 목표를 다음 봉 시가에 모의 적용 |
| v2 | session_vwap | 9713.19 | -286.81 | buy / partial / 종가 > 뉴욕 거래일별 누적 전형가격 VWAP; 조건 충족; close=721.81, session_VWAP=721.45, session_volume=2.32267e+07; 직전 완료 봉 목표를 다음 봉 시가에 모의 적용 |
| v2 | obv_20 | 9741.41 | -258.59 | buy / partial / OBV > OBV의 SMA20 그리고 종가 > EMA26; 조건 충족; OBV=2.23867e+08, OBV_SMA20=2.10034e+08, close=722.48, EMA26=719.576; 직전 완료 봉 목표를 다음 봉 시가에 모의 적용 |
| v2 | stochastic_14_3_recovery | 9694.13 | -305.87 | 중단: 손실 한도 / sell / filled / 직전 %K14 < 20에서 %K14가 %D3 상향 돌파 (한 봉 목표); 조건 미충족; K14=10.576, D3=8.00581, previous_K14=7.39787, previous_D3=7.27486; 직전 완료 봉 목표를 다음 봉 시가에 모의 적용 |
| v2 | mfi_14_recovery | 9809.63 | -190.37 | sell / filled / 직전 MFI14 < 20, 현재 MFI14 >= 20 (한 봉 목표); 조건 미충족; MFI14=30.3876, previous_MFI14=31.1747; 직전 완료 봉 목표를 다음 봉 시가에 모의 적용 |
| v2 | adx_14_trend | 9922.56 | -77.44 | sell / filled / Wilder ADX14 >= 25 그리고 +DI14 > -DI14; 조건 미충족; ADX14=23.9831, plus_DI14=26.5781, minus_DI14=24.6326; 직전 완료 봉 목표를 다음 봉 시가에 모의 적용 |
| v2 | aroon_25_trend | 9825.33 | -174.67 | sell / filled / Aroon25 Up > 70 그리고 Down < 30 (동률이면 최신 극값); 조건 미충족; Aroon_up=100, Aroon_down=80; 직전 완료 봉 목표를 다음 봉 시가에 모의 적용 |
| v2 | cci_20_momentum | 9923.68 | -76.32 | buy / partial / CCI20 > 100 (전형가격·평균절대편차); 조건 충족; CCI20=222.381; 직전 완료 봉 목표를 다음 봉 시가에 모의 적용 |
| v2 | williams_14_recovery | 9672.18 | -327.82 | sell / filled / 직전 Williams %R14 < -80, 현재 >= -80 (한 봉 목표); 조건 미충족; Williams_R14=-78.3698, previous_R14=-75.2358; 직전 완료 봉 목표를 다음 봉 시가에 모의 적용 |
| v2 | cmf_20_accumulation | 9565.94 | -434.06 | buy / partial / Chaikin Money Flow20 > 0.1; 조건 충족; CMF20=0.185201, volume20=2.07769e+08; 직전 완료 봉 목표를 다음 봉 시가에 모의 적용 |
| v2 | chaikin_3_10 | 9748.25 | -251.75 | buy / partial / ADL의 EMA3 - EMA10 > 0 그리고 종가 > EMA26; 조건 충족; Chaikin3_10=659089, ADL=2.27792e+08, close=722.48, EMA26=719.576; 직전 완료 봉 목표를 다음 봉 시가에 모의 적용 |
| v2 | roc_10_momentum | 9980.90 | -19.10 | buy / partial / 10봉 ROC > 1% 그리고 종가 > EMA26; 조건 충족; ROC10_percent=1.06205, close=724.74, EMA26=720.545; 직전 완료 봉 목표를 다음 봉 시가에 모의 적용 |
| v2 | trix_15_trend | 9698.68 | -301.32 | buy / partial / 15봉 삼중 EMA의 1봉 변화율 TRIX > 0 그리고 종가 > EMA26; 조건 충족; TRIX15_percent=3.24292e-05, close=721.81, EMA26=719.344; 직전 완료 봉 목표를 다음 봉 시가에 모의 적용 |
| v2 | keltner_20_breakout | 9864.03 | -135.97 | sell / filled / 종가 > EMA20 + 2 x Wilder ATR14; 조건 미충족; close=724.74, upper_Keltner=724.763, EMA20=720.919, ATR14=1.92215; 직전 완료 봉 목표를 다음 봉 시가에 모의 적용 |
| v2 | opening_range_30m | 9774.53 | -225.47 | buy / partial / 뉴욕 09:30·09:45 두 완료 봉 최고가를 10:00 이후 종가가 돌파; 조건 충족; close=723.37, opening_high=723.2; 직전 완료 봉 목표를 다음 봉 시가에 모의 적용 |

### 같은 기간의 비용·노출 비교 (사후 연구)

| 전략 | 비용 전 | 비용 후 | 100% 보유 | 같은 평균 노출 보유 | 평균 노출 |
|---|---:|---:|---:|---:|---:|
| cash | 0.00% | 0.00% | -2.75% | -0.00% | 0.00% |
| buy_hold | -2.34% | -2.75% | -2.75% | -2.75% | 100.00% |
| trend_8_26 | 0.39% | -3.74% | -2.75% | -1.14% | 41.42% |
| momentum_26 | -2.98% | -9.29% | -2.75% | -1.03% | 37.47% |
| breakout_8 | -1.41% | -16.30% | -2.75% | -0.51% | 18.47% |
| reversion_12 | -0.10% | -12.30% | -2.75% | -0.85% | 30.87% |
| volume_26 | -1.42% | -14.90% | -2.75% | -0.44% | 16.09% |
| trend_8_26 AND momentum_26 | 0.07% | -4.04% | -2.75% | -0.83% | 30.08% |
| trend_8_26 + momentum_26 | -1.31% | -5.96% | -2.75% | -1.09% | 39.45% |
| trend_8_26 AND breakout_8 | 0.37% | -7.32% | -2.75% | -0.29% | 10.55% |
| trend_8_26 + breakout_8 | -0.51% | -9.67% | -2.75% | -0.83% | 29.95% |
| trend_8_26 AND reversion_12 | -0.34% | -4.44% | -2.75% | -0.18% | 6.33% |
| trend_8_26 + reversion_12 | 0.16% | -7.54% | -2.75% | -1.00% | 36.15% |
| trend_8_26 AND volume_26 | 0.20% | -4.73% | -2.75% | -0.14% | 5.01% |
| trend_8_26 + volume_26 | -0.51% | -9.31% | -2.75% | -0.79% | 28.77% |
| momentum_26 AND breakout_8 | -0.49% | -9.28% | -2.75% | -0.31% | 11.35% |
| momentum_26 + breakout_8 | -2.19% | -12.68% | -2.75% | -0.77% | 27.97% |
| momentum_26 AND reversion_12 | -1.28% | -6.13% | -2.75% | -0.18% | 6.60% |
| momentum_26 + reversion_12 | -1.54% | -10.06% | -2.75% | -0.94% | 34.17% |
| momentum_26 AND volume_26 | -0.53% | -4.62% | -2.75% | -0.10% | 3.69% |
| momentum_26 + volume_26 | -2.20% | -11.77% | -2.75% | -0.74% | 26.79% |
| breakout_8 AND reversion_12 | 0.00% | 0.00% | -2.75% | -0.00% | 0.00% |
| breakout_8 + reversion_12 | -0.75% | -13.25% | -2.75% | -0.68% | 24.68% |
| breakout_8 AND volume_26 | 0.28% | -2.21% | -2.75% | -0.06% | 2.11% |
| breakout_8 + volume_26 | -1.41% | -14.18% | -2.75% | -0.48% | 17.29% |
| reversion_12 AND volume_26 | -1.31% | -8.11% | -2.75% | -0.23% | 8.44% |
| reversion_12 + volume_26 | -0.76% | -13.07% | -2.75% | -0.65% | 23.49% |
| ema_12_26 | -1.54% | -4.80% | -2.75% | -1.09% | 39.58% |
| macd_12_26_9 | 0.56% | -3.98% | -2.75% | -0.62% | 22.43% |
| rsi_14_recovery | -0.47% | -5.76% | -2.75% | -0.09% | 3.43% |
| bollinger_20_reentry | -0.08% | -6.18% | -2.75% | -0.11% | 3.96% |
| donchian_20 | 0.59% | -4.76% | -2.75% | -0.16% | 5.80% |
| atr_14_breakout | 0.51% | -3.62% | -2.75% | -0.08% | 2.90% |
| session_vwap | 0.12% | -11.73% | -2.75% | -1.23% | 44.59% |
| obv_20 | -1.17% | -9.89% | -2.75% | -0.71% | 25.86% |
| stochastic_14_3_recovery | 0.18% | -11.68% | -2.75% | -0.22% | 7.92% |
| mfi_14_recovery | -1.23% | -3.69% | -2.75% | -0.04% | 1.58% |
| adx_14_trend | -0.12% | -3.02% | -2.75% | -0.50% | 18.21% |
| aroon_25_trend | 1.18% | -2.16% | -2.75% | -0.43% | 15.57% |
| cci_20_momentum | -0.02% | -5.33% | -2.75% | -0.48% | 17.41% |
| williams_14_recovery | -0.13% | -10.84% | -2.75% | -0.20% | 7.12% |
| cmf_20_accumulation | -1.64% | -9.18% | -2.75% | -0.92% | 33.51% |
| chaikin_3_10 | -2.31% | -10.56% | -2.75% | -0.89% | 32.19% |
| roc_10_momentum | 0.16% | -1.51% | -2.75% | -0.12% | 4.22% |
| trix_15_trend | 0.19% | -3.52% | -2.75% | -0.88% | 31.93% |
| keltner_20_breakout | -0.73% | -4.82% | -2.75% | -0.19% | 6.86% |
| opening_range_30m | -0.10% | -5.80% | -2.75% | -0.83% | 30.08% |

동일 구간·초기 자금, 종료 시 청산 비용 포함. 노출 맞춤은 사후 설명용이며 v2 실제 계좌 성과가 아닙니다.
[낙폭 분해·비용 영향·전체 구간](QQQ/comparison.json)

[v1 전체 기록](QQQ/accounts.json) · [v2 전체 기록](QQQ/accounts-v2.json)

## IWM 계좌

| 모델 | 전략 | 평가액 USD | 손익 USD | 최근 매매·이유 |
|---|---|---:|---:|---|
| v1 | cash | 10000.00 | 0.00 | 대기 /  / 새 신호 대기 |
| v1 | buy_hold | 10026.76 | 26.76 | buy /  / buy_hold: prior completed bar target 100%; next bar open simulation |
| v1 | trend_8_26 | 9831.55 | -168.45 | buy /  / trend_8_26: prior completed bar target 100%; next bar open simulation |
| v1 | momentum_26 | 10002.96 | 2.96 | buy /  / momentum_26: prior completed bar target 100%; next bar open simulation |
| v1 | breakout_8 | 9572.95 | -427.05 | sell /  / breakout_8: prior completed bar target 0%; next bar open simulation |
| v1 | reversion_12 | 9786.62 | -213.38 | sell /  / reversion_12: prior completed bar target 0%; next bar open simulation |
| v1 | volume_26 | 9923.29 | -76.71 | sell /  / volume_26: prior completed bar target 0%; next bar open simulation |
| v1 | trend_8_26 AND momentum_26 | 9847.53 | -152.47 | buy /  / trend_8_26 AND momentum_26: prior completed bar target 100%; next bar open simulation |
| v1 | trend_8_26 + momentum_26 | 9916.95 | -83.05 | buy /  / trend_8_26 + momentum_26: prior completed bar target 100%; next bar open simulation |
| v1 | trend_8_26 AND breakout_8 | 9661.72 | -338.28 | sell /  / trend_8_26 AND breakout_8: prior completed bar target 0%; next bar open simulation |
| v1 | trend_8_26 + breakout_8 | 9701.56 | -298.44 | sell /  / trend_8_26 + breakout_8: prior completed bar target 50%; next bar open simulation |
| v1 | trend_8_26 AND reversion_12 | 9827.31 | -172.69 | sell /  / trend_8_26 AND reversion_12: prior completed bar target 0%; next bar open simulation |
| v1 | trend_8_26 + reversion_12 | 9808.90 | -191.10 | sell /  / trend_8_26 + reversion_12: prior completed bar target 50%; next bar open simulation |
| v1 | trend_8_26 AND volume_26 | 9935.98 | -64.02 | sell /  / trend_8_26 AND volume_26: prior completed bar target 0%; next bar open simulation |
| v1 | trend_8_26 + volume_26 | 9896.93 | -103.07 | sell /  / trend_8_26 + volume_26: prior completed bar target 50%; next bar open simulation |
| v1 | momentum_26 AND breakout_8 | 9710.54 | -289.46 | sell /  / momentum_26 AND breakout_8: prior completed bar target 0%; next bar open simulation |
| v1 | momentum_26 + breakout_8 | 9805.33 | -194.67 | sell /  / momentum_26 + breakout_8: prior completed bar target 50%; next bar open simulation |
| v1 | momentum_26 AND reversion_12 | 9924.34 | -75.66 | sell /  / momentum_26 AND reversion_12: prior completed bar target 0%; next bar open simulation |
| v1 | momentum_26 + reversion_12 | 9913.85 | -86.15 | sell /  / momentum_26 + reversion_12: prior completed bar target 50%; next bar open simulation |
| v1 | momentum_26 AND volume_26 | 10062.05 | 62.05 | sell /  / momentum_26 AND volume_26: prior completed bar target 0%; next bar open simulation |
| v1 | momentum_26 + volume_26 | 9962.88 | -37.12 | sell /  / momentum_26 + volume_26: prior completed bar target 50%; next bar open simulation |
| v1 | breakout_8 AND reversion_12 | 10000.00 | 0.00 | 대기 /  / 새 신호 대기 |
| v1 | breakout_8 + reversion_12 | 9679.06 | -320.94 | sell /  / breakout_8 + reversion_12: prior completed bar target 0%; next bar open simulation |
| v1 | breakout_8 AND volume_26 | 9967.28 | -32.72 | sell /  / breakout_8 AND volume_26: prior completed bar target 0%; next bar open simulation |
| v1 | breakout_8 + volume_26 | 9766.00 | -234.00 | sell /  / breakout_8 + volume_26: prior completed bar target 0%; next bar open simulation |
| v1 | reversion_12 AND volume_26 | 9935.98 | -64.02 | sell /  / reversion_12 AND volume_26: prior completed bar target 0%; next bar open simulation |
| v1 | reversion_12 + volume_26 | 9874.40 | -125.60 | sell /  / reversion_12 + volume_26: prior completed bar target 0%; next bar open simulation |
| v1 | ema_12_26 | 9896.90 | -103.10 | buy /  / EMA12 > EMA26; 조건 충족; EMA12=271.545, EMA26=271.529 |
| v1 | macd_12_26_9 | 9906.42 | -93.58 | sell /  / MACD > 신호선 그리고 MACD > 0; 조건 미충족; MACD=0.978353, signal9=1.01104 |
| v1 | rsi_14_recovery | 9786.95 | -213.05 | sell /  / 직전 RSI14 < 30, 현재 RSI14 >= 30 (한 봉 목표); 조건 미충족; RSI14=46.986, previous_RSI14=37.1649 |
| v1 | bollinger_20_reentry | 9924.03 | -75.97 | sell /  / 직전 종가 < 직전 하단밴드, 현재 하단밴드 <= 종가 <= SMA20 (한 봉 목표); 조건 미충족; close=271.19, lower20=270.018, SMA20=273.224, previous_lower20=270.283 |
| v1 | donchian_20 | 9835.91 | -164.09 | sell /  / 종가 > 현재 봉을 제외한 직전 20봉 최고가; 조건 미충족; close=275.785, prior_high20=276.875 |
| v1 | atr_14_breakout | 9849.82 | -150.18 | sell /  / 종가 > 직전 종가 + 직전 ATR14 그리고 종가 > EMA26; 조건 미충족; close=276.97, threshold=277.417, prior_ATR14=0.596703, EMA26=275.4 |
| v1 | session_vwap | 9807.96 | -192.04 | buy /  / 종가 > 뉴욕 거래일별 누적 전형가격 VWAP; 조건 충족; close=276.94, session_VWAP=276.815, session_volume=5.57282e+06 |
| v1 | obv_20 | 9891.24 | -108.76 | buy /  / OBV > OBV의 SMA20 그리고 종가 > EMA26; 조건 충족; OBV=-3.32696e+07, OBV_SMA20=-3.46228e+07, close=272.6, EMA26=271.529 |
| v1 | stochastic_14_3_recovery | 9665.87 | -334.13 | sell /  / 직전 %K14 < 20에서 %K14가 %D3 상향 돌파 (한 봉 목표); 조건 미충족; K14=72.727, D3=41.2922, previous_K14=34.0903, previous_D3=23.8263 |
| v1 | mfi_14_recovery | 9934.22 | -65.78 | sell /  / 직전 MFI14 < 20, 현재 MFI14 >= 20 (한 봉 목표); 조건 미충족; MFI14=34.131, previous_MFI14=22.0435 |
| v1 | adx_14_trend | 9822.17 | -177.83 | buy /  / Wilder ADX14 >= 25 그리고 +DI14 > -DI14; 조건 충족; ADX14=26.5262, plus_DI14=49.1478, minus_DI14=9.69634 |
| v1 | aroon_25_trend | 9764.31 | -235.69 | buy /  / Aroon25 Up > 70 그리고 Down < 30 (동률이면 최신 극값); 조건 충족; Aroon_up=100, Aroon_down=0 |
| v1 | cci_20_momentum | 9907.78 | -92.22 | sell /  / CCI20 > 100 (전형가격·평균절대편차); 조건 미충족; CCI20=71.4927 |
| v1 | williams_14_recovery | 9833.31 | -166.69 | sell /  / 직전 Williams %R14 < -80, 현재 >= -80 (한 봉 목표); 조건 미충족; Williams_R14=-27.273, previous_R14=-65.9097 |
| v1 | cmf_20_accumulation | 9825.75 | -174.25 | sell /  / Chaikin Money Flow20 > 0.1; 조건 미충족; CMF20=0.0815655, volume20=1.22806e+07 |
| v1 | chaikin_3_10 | 9878.06 | -121.94 | sell /  / ADL의 EMA3 - EMA10 > 0 그리고 종가 > EMA26; 조건 미충족; Chaikin3_10=-108533, ADL=-4.17289e+07, close=276.97, EMA26=275.4 |
| v1 | roc_10_momentum | 9996.39 | -3.61 | sell /  / 10봉 ROC > 1% 그리고 종가 > EMA26; 조건 미충족; ROC10_percent=0.995963, close=275.315, EMA26=273.754 |
| v1 | trix_15_trend | 9978.34 | -21.66 | buy /  / 15봉 삼중 EMA의 1봉 변화율 TRIX > 0 그리고 종가 > EMA26; 조건 충족; TRIX15_percent=0.00296855, close=273.97, EMA26=271.9 |
| v1 | keltner_20_breakout | 9879.23 | -120.77 | sell /  / 종가 > EMA20 + 2 x Wilder ATR14; 조건 미충족; close=276.4, upper_Keltner=277.094, EMA20=275.768, ATR14=0.662947 |
| v1 | opening_range_30m | 9963.15 | -36.85 | sell /  / 뉴욕 09:30·09:45 두 완료 봉 최고가를 10:00 이후 종가가 돌파; 자료 부족·변동폭 또는 거래량 없음: 대기; close=276.82 |
| v2 | cash | 10000.00 | 0.00 | 대기 /  / 새 신호 대기 |
| v2 | buy_hold | 9919.55 | -80.45 | buy / partial / 직전 완료 봉 목표 비중 100%; 다음 봉 시가 가정 |
| v2 | trend_8_26 | 9700.28 | -299.72 | buy / partial / 직전 완료 봉 목표 비중 100%; 다음 봉 시가 가정 |
| v2 | momentum_26 | 9870.41 | -129.59 | buy / partial / 직전 완료 봉 목표 비중 100%; 다음 봉 시가 가정 |
| v2 | breakout_8 | 9188.59 | -811.41 | sell / filled / 직전 완료 봉 목표 비중 0%; 다음 봉 시가 가정 |
| v2 | reversion_12 | 9325.80 | -674.20 | sell / filled / 직전 완료 봉 목표 비중 0%; 다음 봉 시가 가정 |
| v2 | volume_26 | 9434.73 | -565.27 | sell / filled / 직전 완료 봉 목표 비중 0%; 다음 봉 시가 가정 |
| v2 | trend_8_26 AND momentum_26 | 9864.88 | -135.12 | buy / partial / 직전 완료 봉 목표 비중 100%; 다음 봉 시가 가정 |
| v2 | trend_8_26 + momentum_26 | 9805.74 | -194.26 | buy / partial / 직전 완료 봉 목표 비중 100%; 다음 봉 시가 가정 |
| v2 | trend_8_26 AND breakout_8 | 9564.01 | -435.99 | sell / filled / 직전 완료 봉 목표 비중 0%; 다음 봉 시가 가정 |
| v2 | trend_8_26 + breakout_8 | 9461.12 | -538.88 | sell / filled / 직전 완료 봉 목표 비중 50%; 다음 봉 시가 가정 |
| v2 | trend_8_26 AND reversion_12 | 9705.35 | -294.65 | sell / filled / 직전 완료 봉 목표 비중 0%; 다음 봉 시가 가정 |
| v2 | trend_8_26 + reversion_12 | 9510.87 | -489.13 | sell / filled / 직전 완료 봉 목표 비중 50%; 다음 봉 시가 가정 |
| v2 | trend_8_26 AND volume_26 | 9797.73 | -202.27 | sell / filled / 직전 완료 봉 목표 비중 0%; 다음 봉 시가 가정 |
| v2 | trend_8_26 + volume_26 | 9606.66 | -393.34 | sell / filled / 직전 완료 봉 목표 비중 50%; 다음 봉 시가 가정 |
| v2 | momentum_26 AND breakout_8 | 9507.76 | -492.24 | sell / filled / 직전 완료 봉 목표 비중 0%; 다음 봉 시가 가정 |
| v2 | momentum_26 + breakout_8 | 9543.58 | -456.42 | sell / filled / 직전 완료 봉 목표 비중 50%; 다음 봉 시가 가정 |
| v2 | momentum_26 AND reversion_12 | 9881.28 | -118.72 | sell / filled / 직전 완료 봉 목표 비중 0%; 다음 봉 시가 가정 |
| v2 | momentum_26 + reversion_12 | 9634.07 | -365.93 | sell / filled / 직전 완료 봉 목표 비중 50%; 다음 봉 시가 가정 |
| v2 | momentum_26 AND volume_26 | 9957.22 | -42.78 | sell / filled / 직전 완료 봉 목표 비중 0%; 다음 봉 시가 가정 |
| v2 | momentum_26 + volume_26 | 9649.72 | -350.28 | sell / filled / 직전 완료 봉 목표 비중 50%; 다음 봉 시가 가정 |
| v2 | breakout_8 AND reversion_12 | 10000.00 | 0.00 | 대기 /  / 새 신호 대기 |
| v2 | breakout_8 + reversion_12 | 9295.37 | -704.63 | sell / filled / 직전 완료 봉 목표 비중 0%; 다음 봉 시가 가정 |
| v2 | breakout_8 AND volume_26 | 9710.25 | -289.75 | sell / filled / 직전 완료 봉 목표 비중 0%; 다음 봉 시가 가정 |
| v2 | breakout_8 + volume_26 | 9349.91 | -650.09 | sell / filled / 직전 완료 봉 목표 비중 0%; 다음 봉 시가 가정 |
| v2 | reversion_12 AND volume_26 | 9676.46 | -323.54 | sell / filled / 직전 완료 봉 목표 비중 0%; 다음 봉 시가 가정 |
| v2 | reversion_12 + volume_26 | 9419.31 | -580.69 | sell / filled / 직전 완료 봉 목표 비중 0%; 다음 봉 시가 가정 |
| v2 | ema_12_26 | 9891.95 | -108.05 | buy / partial / EMA12 > EMA26; 조건 충족; EMA12=271.545, EMA26=271.529; 직전 완료 봉 목표를 다음 봉 시가에 모의 적용 |
| v2 | macd_12_26_9 | 9900.47 | -99.53 | sell / filled / MACD > 신호선 그리고 MACD > 0; 조건 미충족; MACD=0.978353, signal9=1.01104; 직전 완료 봉 목표를 다음 봉 시가에 모의 적용 |
| v2 | rsi_14_recovery | 9779.12 | -220.88 | sell / filled / 직전 RSI14 < 30, 현재 RSI14 >= 30 (한 봉 목표); 조건 미충족; RSI14=46.986, previous_RSI14=37.1649; 직전 완료 봉 목표를 다음 봉 시가에 모의 적용 |
| v2 | bollinger_20_reentry | 9920.06 | -79.94 | sell / filled / 직전 종가 < 직전 하단밴드, 현재 하단밴드 <= 종가 <= SMA20 (한 봉 목표); 조건 미충족; close=271.19, lower20=270.018, SMA20=273.224, previous_lower20=270.283; 직전 완료 봉 목표를 다음 봉 시가에 모의 적용 |
| v2 | donchian_20 | 9830.01 | -169.99 | sell / filled / 종가 > 현재 봉을 제외한 직전 20봉 최고가; 조건 미충족; close=275.785, prior_high20=276.875; 직전 완료 봉 목표를 다음 봉 시가에 모의 적용 |
| v2 | atr_14_breakout | 9839.97 | -160.03 | sell / filled / 종가 > 직전 종가 + 직전 ATR14 그리고 종가 > EMA26; 조건 미충족; close=276.97, threshold=277.417, prior_ATR14=0.596703, EMA26=275.4; 직전 완료 봉 목표를 다음 봉 시가에 모의 적용 |
| v2 | session_vwap | 9795.22 | -204.78 | buy / partial / 종가 > 뉴욕 거래일별 누적 전형가격 VWAP; 조건 충족; close=276.94, session_VWAP=276.815, session_volume=5.57282e+06; 직전 완료 봉 목표를 다음 봉 시가에 모의 적용 |
| v2 | obv_20 | 9882.34 | -117.66 | buy / partial / OBV > OBV의 SMA20 그리고 종가 > EMA26; 조건 충족; OBV=-2.88653e+07, OBV_SMA20=-3.02185e+07, close=272.6, EMA26=271.529; 직전 완료 봉 목표를 다음 봉 시가에 모의 적용 |
| v2 | stochastic_14_3_recovery | 9650.41 | -349.59 | sell / filled / 직전 %K14 < 20에서 %K14가 %D3 상향 돌파 (한 봉 목표); 조건 미충족; K14=72.727, D3=41.2922, previous_K14=34.0903, previous_D3=23.8263; 직전 완료 봉 목표를 다음 봉 시가에 모의 적용 |
| v2 | mfi_14_recovery | 9930.25 | -69.75 | sell / filled / 직전 MFI14 < 20, 현재 MFI14 >= 20 (한 봉 목표); 조건 미충족; MFI14=34.131, previous_MFI14=22.0435; 직전 완료 봉 목표를 다음 봉 시가에 모의 적용 |
| v2 | adx_14_trend | 9817.26 | -182.74 | buy / partial / Wilder ADX14 >= 25 그리고 +DI14 > -DI14; 조건 충족; ADX14=26.5262, plus_DI14=49.1478, minus_DI14=9.69634; 직전 완료 봉 목표를 다음 봉 시가에 모의 적용 |
| v2 | aroon_25_trend | 9755.53 | -244.47 | buy / partial / Aroon25 Up > 70 그리고 Down < 30 (동률이면 최신 극값); 조건 충족; Aroon_up=100, Aroon_down=0; 직전 완료 봉 목표를 다음 봉 시가에 모의 적용 |
| v2 | cci_20_momentum | 9899.86 | -100.14 | sell / filled / CCI20 > 100 (전형가격·평균절대편차); 조건 미충족; CCI20=71.4927; 직전 완료 봉 목표를 다음 봉 시가에 모의 적용 |
| v2 | williams_14_recovery | 9825.45 | -174.55 | sell / filled / 직전 Williams %R14 < -80, 현재 >= -80 (한 봉 목표); 조건 미충족; Williams_R14=-27.273, previous_R14=-65.9097; 직전 완료 봉 목표를 다음 봉 시가에 모의 적용 |
| v2 | cmf_20_accumulation | 9812.00 | -188.00 | sell / filled / Chaikin Money Flow20 > 0.1; 조건 미충족; CMF20=0.0815655, volume20=1.22806e+07; 직전 완료 봉 목표를 다음 봉 시가에 모의 적용 |
| v2 | chaikin_3_10 | 9868.19 | -131.81 | sell / filled / ADL의 EMA3 - EMA10 > 0 그리고 종가 > EMA26; 조건 미충족; Chaikin3_10=-108533, ADL=-4.17289e+07, close=276.97, EMA26=275.4; 직전 완료 봉 목표를 다음 봉 시가에 모의 적용 |
| v2 | roc_10_momentum | 9994.39 | -5.61 | sell / filled / 10봉 ROC > 1% 그리고 종가 > EMA26; 조건 미충족; ROC10_percent=0.995963, close=275.315, EMA26=273.754; 직전 완료 봉 목표를 다음 봉 시가에 모의 적용 |
| v2 | trix_15_trend | 9975.35 | -24.65 | buy / partial / 15봉 삼중 EMA의 1봉 변화율 TRIX > 0 그리고 종가 > EMA26; 조건 충족; TRIX15_percent=0.00296855, close=273.97, EMA26=271.9; 직전 완료 봉 목표를 다음 봉 시가에 모의 적용 |
| v2 | keltner_20_breakout | 9873.30 | -126.70 | sell / filled / 종가 > EMA20 + 2 x Wilder ATR14; 조건 미충족; close=276.4, upper_Keltner=277.094, EMA20=275.768, ATR14=0.662947; 직전 완료 봉 목표를 다음 봉 시가에 모의 적용 |
| v2 | opening_range_30m | 9959.17 | -40.83 | sell / filled / 뉴욕 09:30·09:45 두 완료 봉 최고가를 10:00 이후 종가가 돌파; 자료 부족·변동폭 또는 거래량 없음: 대기; close=276.82; 직전 완료 봉 목표를 다음 봉 시가에 모의 적용 |

### 같은 기간의 비용·노출 비교 (사후 연구)

| 전략 | 비용 전 | 비용 후 | 100% 보유 | 같은 평균 노출 보유 | 평균 노출 |
|---|---:|---:|---:|---:|---:|
| cash | 0.00% | 0.00% | -1.24% | -0.00% | 0.00% |
| buy_hold | -0.82% | -1.24% | -1.24% | -1.24% | 100.00% |
| trend_8_26 | -0.05% | -3.36% | -1.24% | -0.59% | 47.76% |
| momentum_26 | 0.09% | -5.23% | -1.24% | -0.57% | 46.17% |
| breakout_8 | 0.18% | -13.88% | -1.24% | -0.25% | 20.05% |
| reversion_12 | -2.16% | -13.02% | -1.24% | -0.34% | 27.18% |
| volume_26 | -1.32% | -8.12% | -1.24% | -0.10% | 8.18% |
| trend_8_26 AND momentum_26 | 0.08% | -3.63% | -1.24% | -0.49% | 39.58% |
| trend_8_26 + momentum_26 | 0.02% | -3.89% | -1.24% | -0.58% | 46.97% |
| trend_8_26 AND breakout_8 | -0.03% | -8.47% | -1.24% | -0.16% | 12.66% |
| trend_8_26 + breakout_8 | 0.07% | -8.57% | -1.24% | -0.42% | 33.91% |
| trend_8_26 AND reversion_12 | -0.74% | -4.42% | -1.24% | -0.06% | 5.01% |
| trend_8_26 + reversion_12 | -1.10% | -8.32% | -1.24% | -0.47% | 37.47% |
| trend_8_26 AND volume_26 | -0.68% | -3.16% | -1.24% | -0.03% | 2.11% |
| trend_8_26 + volume_26 | -0.68% | -5.37% | -1.24% | -0.35% | 27.97% |
| momentum_26 AND breakout_8 | 0.41% | -8.45% | -1.24% | -0.15% | 12.40% |
| momentum_26 + breakout_8 | 0.14% | -9.47% | -1.24% | -0.41% | 33.12% |
| momentum_26 AND reversion_12 | 0.02% | -2.88% | -1.24% | -0.04% | 2.90% |
| momentum_26 + reversion_12 | -1.04% | -8.26% | -1.24% | -0.46% | 36.68% |
| momentum_26 AND volume_26 | 0.06% | -2.02% | -1.24% | -0.02% | 1.85% |
| momentum_26 + volume_26 | -0.61% | -6.30% | -1.24% | -0.34% | 27.18% |
| breakout_8 AND reversion_12 | 0.00% | 0.00% | -1.24% | -0.00% | 0.00% |
| breakout_8 + reversion_12 | -0.99% | -12.91% | -1.24% | -0.29% | 23.62% |
| breakout_8 AND volume_26 | -0.54% | -3.42% | -1.24% | -0.03% | 2.11% |
| breakout_8 + volume_26 | -0.57% | -10.67% | -1.24% | -0.18% | 14.12% |
| reversion_12 AND volume_26 | -0.62% | -4.31% | -1.24% | -0.05% | 3.96% |
| reversion_12 + volume_26 | -1.73% | -10.04% | -1.24% | -0.22% | 17.68% |
| ema_12_26 | 1.67% | -1.28% | -1.24% | -0.59% | 47.76% |
| macd_12_26_9 | 2.93% | 0.37% | -1.24% | -0.35% | 28.50% |
| rsi_14_recovery | -0.65% | -5.14% | -1.24% | -0.04% | 2.90% |
| bollinger_20_reentry | -0.24% | -4.35% | -1.24% | -0.03% | 2.64% |
| donchian_20 | -0.29% | -5.59% | -1.24% | -0.08% | 6.33% |
| atr_14_breakout | -0.12% | -6.61% | -1.24% | -0.06% | 4.49% |
| session_vwap | 1.41% | -7.93% | -1.24% | -0.57% | 45.91% |
| obv_20 | 1.61% | -2.57% | -1.24% | -0.53% | 42.74% |
| stochastic_14_3_recovery | -0.42% | -12.58% | -1.24% | -0.10% | 8.18% |
| mfi_14_recovery | 0.36% | -4.17% | -1.24% | -0.04% | 2.90% |
| adx_14_trend | 0.50% | -2.42% | -1.24% | -0.44% | 35.09% |
| aroon_25_trend | -0.82% | -5.30% | -1.24% | -0.27% | 21.64% |
| cci_20_momentum | -0.89% | -7.33% | -1.24% | -0.25% | 19.79% |
| williams_14_recovery | -0.07% | -8.89% | -1.24% | -0.07% | 5.80% |
| cmf_20_accumulation | -0.11% | -6.99% | -1.24% | -0.31% | 24.54% |
| chaikin_3_10 | -0.09% | -5.80% | -1.24% | -0.44% | 35.36% |
| roc_10_momentum | -0.27% | -1.93% | -1.24% | -0.07% | 5.54% |
| trix_15_trend | 1.76% | -1.19% | -1.24% | -0.47% | 37.73% |
| keltner_20_breakout | -0.34% | -4.04% | -1.24% | -0.10% | 7.92% |
| opening_range_30m | 2.93% | -1.30% | -1.24% | -0.34% | 27.44% |

동일 구간·초기 자금, 종료 시 청산 비용 포함. 노출 맞춤은 사후 설명용이며 v2 실제 계좌 성과가 아닙니다.
[낙폭 분해·비용 영향·전체 구간](IWM/comparison.json)

[v1 전체 기록](IWM/accounts.json) · [v2 전체 기록](IWM/accounts-v2.json)

## DIA 계좌

| 모델 | 전략 | 평가액 USD | 손익 USD | 최근 매매·이유 |
|---|---|---:|---:|---|
| v1 | cash | 10000.00 | 0.00 | 대기 /  / 새 신호 대기 |
| v1 | buy_hold | 10032.90 | 32.90 | buy /  / buy_hold: prior completed bar target 100%; next bar open simulation |
| v1 | trend_8_26 | 9999.45 | -0.55 | buy /  / trend_8_26: prior completed bar target 100%; next bar open simulation |
| v1 | momentum_26 | 9832.97 | -167.03 | buy /  / momentum_26: prior completed bar target 100%; next bar open simulation |
| v1 | breakout_8 | 9547.43 | -452.57 | buy /  / breakout_8: prior completed bar target 100%; next bar open simulation |
| v1 | reversion_12 | 9863.03 | -136.97 | sell /  / reversion_12: prior completed bar target 0%; next bar open simulation |
| v1 | volume_26 | 9901.29 | -98.71 | sell /  / volume_26: prior completed bar target 0%; next bar open simulation |
| v1 | trend_8_26 AND momentum_26 | 9888.90 | -111.10 | buy /  / trend_8_26 AND momentum_26: prior completed bar target 100%; next bar open simulation |
| v1 | trend_8_26 + momentum_26 | 9915.92 | -84.08 | buy /  / trend_8_26 + momentum_26: prior completed bar target 100%; next bar open simulation |
| v1 | trend_8_26 AND breakout_8 | 9772.30 | -227.70 | buy /  / trend_8_26 AND breakout_8: prior completed bar target 100%; next bar open simulation |
| v1 | trend_8_26 + breakout_8 | 9810.04 | -189.96 | buy /  / trend_8_26 + breakout_8: prior completed bar target 100%; next bar open simulation |
| v1 | trend_8_26 AND reversion_12 | 9906.37 | -93.63 | sell /  / trend_8_26 AND reversion_12: prior completed bar target 0%; next bar open simulation |
| v1 | trend_8_26 + reversion_12 | 9930.85 | -69.15 | sell /  / trend_8_26 + reversion_12: prior completed bar target 50%; next bar open simulation |
| v1 | trend_8_26 AND volume_26 | 9974.09 | -25.91 | sell /  / trend_8_26 AND volume_26: prior completed bar target 0%; next bar open simulation |
| v1 | trend_8_26 + volume_26 | 9950.08 | -49.92 | sell /  / trend_8_26 + volume_26: prior completed bar target 50%; next bar open simulation |
| v1 | momentum_26 AND breakout_8 | 9677.59 | -322.41 | buy /  / momentum_26 AND breakout_8: prior completed bar target 100%; next bar open simulation |
| v1 | momentum_26 + breakout_8 | 9689.24 | -310.76 | buy /  / momentum_26 + breakout_8: prior completed bar target 100%; next bar open simulation |
| v1 | momentum_26 AND reversion_12 | 9906.39 | -93.61 | sell /  / momentum_26 AND reversion_12: prior completed bar target 0%; next bar open simulation |
| v1 | momentum_26 + reversion_12 | 9887.28 | -112.72 | sell /  / momentum_26 + reversion_12: prior completed bar target 50%; next bar open simulation |
| v1 | momentum_26 AND volume_26 | 9891.01 | -108.99 | sell /  / momentum_26 AND volume_26: prior completed bar target 0%; next bar open simulation |
| v1 | momentum_26 + volume_26 | 9886.74 | -113.26 | sell /  / momentum_26 + volume_26: prior completed bar target 50%; next bar open simulation |
| v1 | breakout_8 AND reversion_12 | 10000.00 | 0.00 | 대기 /  / 새 신호 대기 |
| v1 | breakout_8 + reversion_12 | 9723.21 | -276.79 | buy /  / breakout_8 + reversion_12: prior completed bar target 50%; next bar open simulation |
| v1 | breakout_8 AND volume_26 | 9947.52 | -52.48 | sell /  / breakout_8 AND volume_26: prior completed bar target 0%; next bar open simulation |
| v1 | breakout_8 + volume_26 | 9761.65 | -238.35 | buy /  / breakout_8 + volume_26: prior completed bar target 50%; next bar open simulation |
| v1 | reversion_12 AND volume_26 | 9970.42 | -29.58 | sell /  / reversion_12 AND volume_26: prior completed bar target 0%; next bar open simulation |
| v1 | reversion_12 + volume_26 | 9901.82 | -98.18 | sell /  / reversion_12 + volume_26: prior completed bar target 0%; next bar open simulation |
| v1 | ema_12_26 | 9887.22 | -112.78 | buy /  / EMA12 > EMA26; 조건 충족; EMA12=519.74, EMA26=519.585 |
| v1 | macd_12_26_9 | 9895.59 | -104.41 | sell /  / MACD > 신호선 그리고 MACD > 0; 조건 미충족; MACD=1.09098, signal9=1.12388 |
| v1 | rsi_14_recovery | 10000.00 | 0.00 | 대기 /  / 새 신호 대기 |
| v1 | bollinger_20_reentry | 9978.51 | -21.49 | sell /  / 직전 종가 < 직전 하단밴드, 현재 하단밴드 <= 종가 <= SMA20 (한 봉 목표); 조건 미충족; close=519.823, lower20=518.355, SMA20=521.612, previous_lower20=518.548 |
| v1 | donchian_20 | 9822.00 | -178.00 | sell /  / 종가 > 현재 봉을 제외한 직전 20봉 최고가; 조건 미충족; close=523.68, prior_high20=526.17 |
| v1 | atr_14_breakout | 9804.37 | -195.63 | sell /  / 종가 > 직전 종가 + 직전 ATR14 그리고 종가 > EMA26; 조건 미충족; close=524.62, threshold=525.055, prior_ATR14=0.664902, EMA26=523.373 |
| v1 | session_vwap | 9842.44 | -157.56 | buy /  / 종가 > 뉴욕 거래일별 누적 전형가격 VWAP; 조건 충족; close=525.38, session_VWAP=524.679, session_volume=1.14471e+06 |
| v1 | obv_20 | 9847.98 | -152.02 | buy /  / OBV > OBV의 SMA20 그리고 종가 > EMA26; 조건 충족; OBV=-8.96454e+06, OBV_SMA20=-9.07774e+06, close=523.66, EMA26=523.184 |
| v1 | stochastic_14_3_recovery | 9740.52 | -259.48 | sell /  / 직전 %K14 < 20에서 %K14가 %D3 상향 돌파 (한 봉 목표); 조건 미충족; K14=29.7295, D3=26.3059, previous_K14=30.81, previous_D3=22.4321 |
| v1 | mfi_14_recovery | 9902.01 | -97.99 | sell /  / 직전 MFI14 < 20, 현재 MFI14 >= 20 (한 봉 목표); 조건 미충족; MFI14=29.4378, previous_MFI14=21.6288 |
| v1 | adx_14_trend | 9811.65 | -188.35 | sell /  / Wilder ADX14 >= 25 그리고 +DI14 > -DI14; 조건 미충족; ADX14=24.7281, plus_DI14=33.8838, minus_DI14=22.7145 |
| v1 | aroon_25_trend | 9889.87 | -110.13 | sell /  / Aroon25 Up > 70 그리고 Down < 30 (동률이면 최신 극값); 조건 미충족; Aroon_up=76, Aroon_down=84 |
| v1 | cci_20_momentum | 9845.92 | -154.08 | buy /  / CCI20 > 100 (전형가격·평균절대편차); 조건 충족; CCI20=182.27 |
| v1 | williams_14_recovery | 9773.54 | -226.46 | sell /  / 직전 Williams %R14 < -80, 현재 >= -80 (한 봉 목표); 조건 미충족; Williams_R14=-70.2705, previous_R14=-69.19 |
| v1 | cmf_20_accumulation | 9652.39 | -347.61 | buy /  / Chaikin Money Flow20 > 0.1; 조건 충족; CMF20=0.10038, volume20=2.23022e+06 |
| v1 | chaikin_3_10 | 9855.16 | -144.84 | buy /  / ADL의 EMA3 - EMA10 > 0 그리고 종가 > EMA26; 조건 충족; Chaikin3_10=17236.9, ADL=-1.53967e+07, close=523.66, EMA26=523.184 |
| v1 | roc_10_momentum | 9939.01 | -60.99 | sell /  / 10봉 ROC > 1% 그리고 종가 > EMA26; 조건 미충족; ROC10_percent=0.771645, close=523.68, EMA26=521.367 |
| v1 | trix_15_trend | 9989.02 | -10.98 | buy /  / 15봉 삼중 EMA의 1봉 변화율 TRIX > 0 그리고 종가 > EMA26; 조건 충족; TRIX15_percent=0.000473967, close=521.46, EMA26=519.585 |
| v1 | keltner_20_breakout | 9944.49 | -55.51 | sell /  / 종가 > EMA20 + 2 x Wilder ATR14; 조건 미충족; close=523.68, upper_Keltner=523.985, EMA20=521.785, ATR14=1.10038 |
| v1 | opening_range_30m | 9742.52 | -257.48 | sell /  / 뉴욕 09:30·09:45 두 완료 봉 최고가를 10:00 이후 종가가 돌파; 자료 부족·변동폭 또는 거래량 없음: 대기; close=524.62 |
| v2 | cash | 10000.00 | 0.00 | 대기 /  / 새 신호 대기 |
| v2 | buy_hold | 10157.20 | 157.20 | buy / partial / 직전 완료 봉 목표 비중 100%; 다음 봉 시가 가정 |
| v2 | trend_8_26 | 9930.69 | -69.31 | buy / partial / 직전 완료 봉 목표 비중 100%; 다음 봉 시가 가정 |
| v2 | momentum_26 | 9868.78 | -131.22 | buy / partial / 직전 완료 봉 목표 비중 100%; 다음 봉 시가 가정 |
| v2 | breakout_8 | 9077.20 | -922.80 | buy / partial / 직전 완료 봉 목표 비중 100%; 다음 봉 시가 가정 |
| v2 | reversion_12 | 9557.55 | -442.45 | sell / filled / 직전 완료 봉 목표 비중 0%; 다음 봉 시가 가정 |
| v2 | volume_26 | 9612.66 | -387.34 | sell / filled / 직전 완료 봉 목표 비중 0%; 다음 봉 시가 가정 |
| v2 | trend_8_26 AND momentum_26 | 9920.32 | -79.68 | buy / partial / 직전 완료 봉 목표 비중 100%; 다음 봉 시가 가정 |
| v2 | trend_8_26 + momentum_26 | 9899.82 | -100.18 | buy / partial / 직전 완료 봉 목표 비중 100%; 다음 봉 시가 가정 |
| v2 | trend_8_26 AND breakout_8 | 9455.77 | -544.23 | buy / partial / 직전 완료 봉 목표 비중 100%; 다음 봉 시가 가정 |
| v2 | trend_8_26 + breakout_8 | 9534.44 | -465.56 | buy / partial / 직전 완료 봉 목표 비중 100%; 다음 봉 시가 가정 |
| v2 | trend_8_26 AND reversion_12 | 9713.09 | -286.91 | sell / filled / 직전 완료 봉 목표 비중 0%; 다음 봉 시가 가정 |
| v2 | trend_8_26 + reversion_12 | 9741.92 | -258.08 | sell / filled / 직전 완료 봉 목표 비중 50%; 다음 봉 시가 가정 |
| v2 | trend_8_26 AND volume_26 | 9827.44 | -172.56 | sell / filled / 직전 완료 봉 목표 비중 0%; 다음 봉 시가 가정 |
| v2 | trend_8_26 + volume_26 | 9790.70 | -209.30 | sell / filled / 직전 완료 봉 목표 비중 50%; 다음 봉 시가 가정 |
| v2 | momentum_26 AND breakout_8 | 9351.59 | -648.41 | buy / partial / 직전 완료 봉 목표 비중 100%; 다음 봉 시가 가정 |
| v2 | momentum_26 + breakout_8 | 9464.94 | -535.06 | buy / partial / 직전 완료 봉 목표 비중 100%; 다음 봉 시가 가정 |
| v2 | momentum_26 AND reversion_12 | 9858.83 | -141.17 | sell / filled / 직전 완료 봉 목표 비중 0%; 다음 봉 시가 가정 |
| v2 | momentum_26 + reversion_12 | 9752.42 | -247.58 | sell / filled / 직전 완료 봉 목표 비중 50%; 다음 봉 시가 가정 |
| v2 | momentum_26 AND volume_26 | 9676.97 | -323.03 | sell / filled / 직전 완료 봉 목표 비중 0%; 다음 봉 시가 가정 |
| v2 | momentum_26 + volume_26 | 9801.42 | -198.58 | sell / filled / 직전 완료 봉 목표 비중 50%; 다음 봉 시가 가정 |
| v2 | breakout_8 AND reversion_12 | 10000.00 | 0.00 | 대기 /  / 새 신호 대기 |
| v2 | breakout_8 + reversion_12 | 9333.26 | -666.74 | buy / filled / 직전 완료 봉 목표 비중 50%; 다음 봉 시가 가정 |
| v2 | breakout_8 AND volume_26 | 9741.25 | -258.75 | sell / filled / 직전 완료 봉 목표 비중 0%; 다음 봉 시가 가정 |
| v2 | breakout_8 + volume_26 | 9380.18 | -619.82 | buy / filled / 직전 완료 봉 목표 비중 50%; 다음 봉 시가 가정 |
| v2 | reversion_12 AND volume_26 | 9966.44 | -33.56 | sell / filled / 직전 완료 봉 목표 비중 0%; 다음 봉 시가 가정 |
| v2 | reversion_12 + volume_26 | 9604.84 | -395.16 | sell / filled / 직전 완료 봉 목표 비중 0%; 다음 봉 시가 가정 |
| v2 | ema_12_26 | 9882.28 | -117.72 | buy / partial / EMA12 > EMA26; 조건 충족; EMA12=519.74, EMA26=519.585; 직전 완료 봉 목표를 다음 봉 시가에 모의 적용 |
| v2 | macd_12_26_9 | 9889.66 | -110.34 | sell / filled / MACD > 신호선 그리고 MACD > 0; 조건 미충족; MACD=1.09098, signal9=1.12388; 직전 완료 봉 목표를 다음 봉 시가에 모의 적용 |
| v2 | rsi_14_recovery | 10000.00 | 0.00 | 대기 /  / 새 신호 대기 |
| v2 | bollinger_20_reentry | 9976.52 | -23.48 | sell / filled / 직전 종가 < 직전 하단밴드, 현재 하단밴드 <= 종가 <= SMA20 (한 봉 목표); 조건 미충족; close=519.823, lower20=518.355, SMA20=521.612, previous_lower20=518.548; 직전 완료 봉 목표를 다음 봉 시가에 모의 적용 |
| v2 | donchian_20 | 9814.14 | -185.86 | sell / filled / 종가 > 현재 봉을 제외한 직전 20봉 최고가; 조건 미충족; close=523.68, prior_high20=526.17; 직전 완료 봉 목표를 다음 봉 시가에 모의 적용 |
| v2 | atr_14_breakout | 9794.57 | -205.43 | sell / filled / 종가 > 직전 종가 + 직전 ATR14 그리고 종가 > EMA26; 조건 미충족; close=524.62, threshold=525.055, prior_ATR14=0.664902, EMA26=523.373; 직전 완료 봉 목표를 다음 봉 시가에 모의 적용 |
| v2 | session_vwap | 9831.62 | -168.38 | buy / partial / 종가 > 뉴욕 거래일별 누적 전형가격 VWAP; 조건 충족; close=525.38, session_VWAP=524.679, session_volume=1.14471e+06; 직전 완료 봉 목표를 다음 봉 시가에 모의 적용 |
| v2 | obv_20 | 9839.13 | -160.87 | buy / partial / OBV > OBV의 SMA20 그리고 종가 > EMA26; 조건 충족; OBV=-9.15207e+06, OBV_SMA20=-9.26528e+06, close=523.66, EMA26=523.184; 직전 완료 봉 목표를 다음 봉 시가에 모의 적용 |
| v2 | stochastic_14_3_recovery | 9726.89 | -273.11 | sell / filled / 직전 %K14 < 20에서 %K14가 %D3 상향 돌파 (한 봉 목표); 조건 미충족; K14=29.7295, D3=26.3059, previous_K14=30.81, previous_D3=22.4321; 직전 완료 봉 목표를 다음 봉 시가에 모의 적용 |
| v2 | mfi_14_recovery | 9896.07 | -103.93 | sell / filled / 직전 MFI14 < 20, 현재 MFI14 >= 20 (한 봉 목표); 조건 미충족; MFI14=29.4378, previous_MFI14=21.6288; 직전 완료 봉 목표를 다음 봉 시가에 모의 적용 |
| v2 | adx_14_trend | 9805.77 | -194.23 | sell / filled / Wilder ADX14 >= 25 그리고 +DI14 > -DI14; 조건 미충족; ADX14=24.7281, plus_DI14=33.8838, minus_DI14=22.7145; 직전 완료 봉 목표를 다음 봉 시가에 모의 적용 |
| v2 | aroon_25_trend | 9881.96 | -118.04 | sell / filled / Aroon25 Up > 70 그리고 Down < 30 (동률이면 최신 극값); 조건 미충족; Aroon_up=76, Aroon_down=84; 직전 완료 봉 목표를 다음 봉 시가에 모의 적용 |
| v2 | cci_20_momentum | 9837.06 | -162.94 | buy / partial / CCI20 > 100 (전형가격·평균절대편차); 조건 충족; CCI20=182.27; 직전 완료 봉 목표를 다음 봉 시가에 모의 적용 |
| v2 | williams_14_recovery | 9761.82 | -238.18 | sell / filled / 직전 Williams %R14 < -80, 현재 >= -80 (한 봉 목표); 조건 미충족; Williams_R14=-70.2705, previous_R14=-69.19; 직전 완료 봉 목표를 다음 봉 시가에 모의 적용 |
| v2 | cmf_20_accumulation | 9637.92 | -362.08 | buy / partial / Chaikin Money Flow20 > 0.1; 조건 충족; CMF20=0.10038, volume20=2.23022e+06; 직전 완료 봉 목표를 다음 봉 시가에 모의 적용 |
| v2 | chaikin_3_10 | 9846.30 | -153.70 | buy / partial / ADL의 EMA3 - EMA10 > 0 그리고 종가 > EMA26; 조건 충족; Chaikin3_10=17236.9, ADL=-1.59365e+07, close=523.66, EMA26=523.184; 직전 완료 봉 목표를 다음 봉 시가에 모의 적용 |
| v2 | roc_10_momentum | 9937.03 | -62.97 | sell / filled / 10봉 ROC > 1% 그리고 종가 > EMA26; 조건 미충족; ROC10_percent=0.771645, close=523.68, EMA26=521.367; 직전 완료 봉 목표를 다음 봉 시가에 모의 적용 |
| v2 | trix_15_trend | 9986.02 | -13.98 | buy / partial / 15봉 삼중 EMA의 1봉 변화율 TRIX > 0 그리고 종가 > EMA26; 조건 충족; TRIX15_percent=0.000473967, close=521.46, EMA26=519.585; 직전 완료 봉 목표를 다음 봉 시가에 모의 적용 |
| v2 | keltner_20_breakout | 9940.51 | -59.49 | sell / filled / 종가 > EMA20 + 2 x Wilder ATR14; 조건 미충족; close=523.68, upper_Keltner=523.985, EMA20=521.785, ATR14=1.10038; 직전 완료 봉 목표를 다음 봉 시가에 모의 적용 |
| v2 | opening_range_30m | 9730.84 | -269.16 | sell / filled / 뉴욕 09:30·09:45 두 완료 봉 최고가를 10:00 이후 종가가 돌파; 자료 부족·변동폭 또는 거래량 없음: 대기; close=524.62; 직전 완료 봉 목표를 다음 봉 시가에 모의 적용 |

### 같은 기간의 비용·노출 비교 (사후 연구)

| 전략 | 비용 전 | 비용 후 | 100% 보유 | 같은 평균 노출 보유 | 평균 노출 |
|---|---:|---:|---:|---:|---:|
| cash | 0.00% | 0.00% | 2.47% | 0.00% | 0.00% |
| buy_hold | 2.90% | 2.47% | 2.47% | 2.47% | 100.00% |
| trend_8_26 | 3.24% | -0.59% | 2.47% | 1.52% | 61.74% |
| momentum_26 | 1.30% | -2.87% | 2.47% | 1.40% | 56.99% |
| breakout_8 | 0.31% | -17.31% | 2.47% | 0.60% | 24.27% |
| reversion_12 | -0.49% | -7.74% | 2.47% | 0.52% | 21.11% |
| volume_26 | 0.40% | -9.60% | 2.47% | 0.27% | 10.82% |
| trend_8_26 AND momentum_26 | 2.90% | -1.34% | 2.47% | 1.27% | 51.72% |
| trend_8_26 + momentum_26 | 2.27% | -1.73% | 2.47% | 1.46% | 59.37% |
| trend_8_26 AND breakout_8 | 1.29% | -11.45% | 2.47% | 0.40% | 16.36% |
| trend_8_26 + breakout_8 | 1.77% | -8.76% | 2.47% | 1.06% | 43.01% |
| trend_8_26 AND reversion_12 | 0.42% | -4.12% | 2.47% | 0.16% | 6.33% |
| trend_8_26 + reversion_12 | 1.36% | -4.04% | 2.47% | 1.02% | 41.43% |
| trend_8_26 AND volume_26 | 1.66% | -3.75% | 2.47% | 0.14% | 5.54% |
| trend_8_26 + volume_26 | 1.81% | -5.01% | 2.47% | 0.89% | 36.28% |
| momentum_26 AND breakout_8 | -0.12% | -13.04% | 2.47% | 0.43% | 17.68% |
| momentum_26 + breakout_8 | 0.81% | -10.19% | 2.47% | 1.00% | 40.64% |
| momentum_26 AND reversion_12 | -0.29% | -2.77% | 2.47% | 0.12% | 4.75% |
| momentum_26 + reversion_12 | 0.41% | -4.54% | 2.47% | 0.96% | 39.05% |
| momentum_26 AND volume_26 | 0.11% | -6.00% | 2.47% | 0.14% | 5.80% |
| momentum_26 + volume_26 | 0.86% | -5.71% | 2.47% | 0.83% | 33.91% |
| breakout_8 AND reversion_12 | 0.00% | 0.00% | 2.47% | 0.00% | 0.00% |
| breakout_8 + reversion_12 | -0.09% | -12.30% | 2.47% | 0.56% | 22.70% |
| breakout_8 AND volume_26 | -0.45% | -4.15% | 2.47% | 0.08% | 3.43% |
| breakout_8 + volume_26 | 0.36% | -12.64% | 2.47% | 0.43% | 17.55% |
| reversion_12 AND volume_26 | 0.29% | -4.24% | 2.47% | 0.08% | 3.43% |
| reversion_12 + volume_26 | -0.04% | -8.49% | 2.47% | 0.39% | 15.97% |
| ema_12_26 | 1.08% | -1.43% | 2.47% | 1.40% | 56.73% |
| macd_12_26_9 | 2.25% | -1.13% | 2.47% | 0.74% | 30.08% |
| rsi_14_recovery | 0.16% | -1.09% | 2.47% | 0.02% | 0.79% |
| bollinger_20_reentry | 0.13% | -3.59% | 2.47% | 0.06% | 2.37% |
| donchian_20 | 0.36% | -6.94% | 2.47% | 0.24% | 9.76% |
| atr_14_breakout | -0.69% | -8.30% | 2.47% | 0.15% | 6.07% |
| session_vwap | 3.01% | -4.09% | 2.47% | 1.35% | 54.88% |
| obv_20 | 1.47% | -6.31% | 2.47% | 1.18% | 48.02% |
| stochastic_14_3_recovery | 0.87% | -11.07% | 2.47% | 0.19% | 7.92% |
| mfi_14_recovery | 0.22% | -3.50% | 2.47% | 0.06% | 2.37% |
| adx_14_trend | 0.13% | -3.59% | 2.47% | 0.77% | 31.13% |
| aroon_25_trend | 1.63% | -2.14% | 2.47% | 0.66% | 26.91% |
| cci_20_momentum | 1.06% | -5.51% | 2.47% | 0.64% | 25.86% |
| williams_14_recovery | 1.55% | -5.84% | 2.47% | 0.12% | 4.75% |
| cmf_20_accumulation | 1.05% | -7.87% | 2.47% | 0.84% | 34.04% |
| chaikin_3_10 | 2.61% | -6.84% | 2.47% | 1.22% | 49.60% |
| roc_10_momentum | -0.07% | -0.90% | 2.47% | 0.05% | 2.11% |
| trix_15_trend | 1.21% | -2.14% | 2.47% | 1.25% | 50.92% |
| keltner_20_breakout | 0.78% | -5.77% | 2.47% | 0.45% | 18.47% |
| opening_range_30m | 1.64% | -4.56% | 2.47% | 0.74% | 30.08% |

동일 구간·초기 자금, 종료 시 청산 비용 포함. 노출 맞춤은 사후 설명용이며 v2 실제 계좌 성과가 아닙니다.
[낙폭 분해·비용 영향·전체 구간](DIA/comparison.json)

[v1 전체 기록](DIA/accounts.json) · [v2 전체 기록](DIA/accounts-v2.json)

## MSFT 계좌

| 모델 | 전략 | 평가액 USD | 손익 USD | 최근 매매·이유 |
|---|---|---:|---:|---|
| v1 | cash | 10000.00 | 0.00 | 대기 /  / 새 신호 대기 |
| v1 | buy_hold | 9802.31 | -197.69 | buy /  / buy_hold: prior completed bar target 100%; next bar open simulation |
| v1 | trend_8_26 | 9581.90 | -418.10 | sell /  / trend_8_26: prior completed bar target 0%; next bar open simulation |
| v1 | momentum_26 | 9543.78 | -456.22 | buy /  / momentum_26: prior completed bar target 100%; next bar open simulation |
| v1 | breakout_8 | 9679.79 | -320.21 | sell /  / breakout_8: prior completed bar target 0%; next bar open simulation |
| v1 | reversion_12 | 9552.38 | -447.62 | sell /  / reversion_12: prior completed bar target 0%; next bar open simulation |
| v1 | volume_26 | 9722.84 | -277.16 | sell /  / volume_26: prior completed bar target 0%; next bar open simulation |
| v1 | trend_8_26 AND momentum_26 | 9662.97 | -337.03 | sell /  / trend_8_26 AND momentum_26: prior completed bar target 0%; next bar open simulation |
| v1 | trend_8_26 + momentum_26 | 9601.08 | -398.92 | sell /  / trend_8_26 + momentum_26: prior completed bar target 50%; next bar open simulation |
| v1 | trend_8_26 AND breakout_8 | 9820.11 | -179.89 | sell /  / trend_8_26 AND breakout_8: prior completed bar target 0%; next bar open simulation |
| v1 | trend_8_26 + breakout_8 | 9669.55 | -330.45 | sell /  / trend_8_26 + breakout_8: prior completed bar target 0%; next bar open simulation |
| v1 | trend_8_26 AND reversion_12 | 9627.16 | -372.84 | sell /  / trend_8_26 AND reversion_12: prior completed bar target 0%; next bar open simulation |
| v1 | trend_8_26 + reversion_12 | 9586.21 | -413.79 | sell /  / trend_8_26 + reversion_12: prior completed bar target 0%; next bar open simulation |
| v1 | trend_8_26 AND volume_26 | 9894.93 | -105.07 | sell /  / trend_8_26 AND volume_26: prior completed bar target 0%; next bar open simulation |
| v1 | trend_8_26 + volume_26 | 9652.28 | -347.72 | sell /  / trend_8_26 + volume_26: prior completed bar target 0%; next bar open simulation |
| v1 | momentum_26 AND breakout_8 | 9778.34 | -221.66 | sell /  / momentum_26 AND breakout_8: prior completed bar target 0%; next bar open simulation |
| v1 | momentum_26 + breakout_8 | 9611.79 | -388.21 | sell /  / momentum_26 + breakout_8: prior completed bar target 50%; next bar open simulation |
| v1 | momentum_26 AND reversion_12 | 9649.76 | -350.24 | sell /  / momentum_26 AND reversion_12: prior completed bar target 0%; next bar open simulation |
| v1 | momentum_26 + reversion_12 | 9547.99 | -452.01 | sell /  / momentum_26 + reversion_12: prior completed bar target 50%; next bar open simulation |
| v1 | momentum_26 AND volume_26 | 9830.16 | -169.84 | sell /  / momentum_26 AND volume_26: prior completed bar target 0%; next bar open simulation |
| v1 | momentum_26 + volume_26 | 9633.13 | -366.87 | sell /  / momentum_26 + volume_26: prior completed bar target 50%; next bar open simulation |
| v1 | breakout_8 AND reversion_12 | 10000.00 | 0.00 | 대기 /  / 새 신호 대기 |
| v1 | breakout_8 + reversion_12 | 9635.00 | -365.00 | sell /  / breakout_8 + reversion_12: prior completed bar target 0%; next bar open simulation |
| v1 | breakout_8 AND volume_26 | 9953.19 | -46.81 | sell /  / breakout_8 AND volume_26: prior completed bar target 0%; next bar open simulation |
| v1 | breakout_8 + volume_26 | 9720.53 | -279.47 | sell /  / breakout_8 + volume_26: prior completed bar target 0%; next bar open simulation |
| v1 | reversion_12 AND volume_26 | 9863.28 | -136.72 | sell /  / reversion_12 AND volume_26: prior completed bar target 0%; next bar open simulation |
| v1 | reversion_12 + volume_26 | 9656.47 | -343.53 | sell /  / reversion_12 + volume_26: prior completed bar target 0%; next bar open simulation |
| v1 | ema_12_26 | 9588.87 | -411.13 | sell /  / EMA12 > EMA26; 조건 미충족; EMA12=532.137, EMA26=532.175 |
| v1 | macd_12_26_9 | 9762.31 | -237.69 | sell /  / MACD > 신호선 그리고 MACD > 0; 조건 미충족; MACD=-0.0387557, signal9=-0.0148606 |
| v1 | rsi_14_recovery | 9957.14 | -42.86 | sell /  / 직전 RSI14 < 30, 현재 RSI14 >= 30 (한 봉 목표); 조건 미충족; RSI14=45.5102, previous_RSI14=37.5844 |
| v1 | bollinger_20_reentry | 9813.80 | -186.20 | sell /  / 직전 종가 < 직전 하단밴드, 현재 하단밴드 <= 종가 <= SMA20 (한 봉 목표); 조건 미충족; close=529.335, lower20=528.85, SMA20=531.508, previous_lower20=529.166 |
| v1 | donchian_20 | 9912.16 | -87.84 | sell /  / 종가 > 현재 봉을 제외한 직전 20봉 최고가; 조건 미충족; close=534.52, prior_high20=535.44 |
| v1 | atr_14_breakout | 9915.10 | -84.90 | sell /  / 종가 > 직전 종가 + 직전 ATR14 그리고 종가 > EMA26; 조건 미충족; close=533.975, threshold=536.307, prior_ATR14=2.16203, EMA26=530.521 |
| v1 | session_vwap | 9822.79 | -177.21 | buy /  / 종가 > 뉴욕 거래일별 누적 전형가격 VWAP; 조건 충족; close=530.964, session_VWAP=530.832, session_volume=8.43578e+06 |
| v1 | obv_20 | 9650.01 | -349.99 | buy /  / OBV > OBV의 SMA20 그리고 종가 > EMA26; 조건 충족; OBV=9.04505e+07, OBV_SMA20=9.01119e+07, close=531.15, EMA26=531.118 |
| v1 | stochastic_14_3_recovery | 9789.03 | -210.97 | sell /  / 직전 %K14 < 20에서 %K14가 %D3 상향 돌파 (한 봉 목표); 조건 미충족; K14=60.6262, D3=34.5689, previous_K14=38.87, previous_D3=26.948 |
| v1 | mfi_14_recovery | 9972.58 | -27.42 | sell /  / 직전 MFI14 < 20, 현재 MFI14 >= 20 (한 봉 목표); 조건 미충족; MFI14=53.413, previous_MFI14=44.3372 |
| v1 | adx_14_trend | 9883.62 | -116.38 | sell /  / Wilder ADX14 >= 25 그리고 +DI14 > -DI14; 조건 미충족; ADX14=23.6824, plus_DI14=22.3066, minus_DI14=19.9214 |
| v1 | aroon_25_trend | 9812.47 | -187.53 | sell /  / Aroon25 Up > 70 그리고 Down < 30 (동률이면 최신 극값); 조건 미충족; Aroon_up=68, Aroon_down=20 |
| v1 | cci_20_momentum | 9949.66 | -50.34 | sell /  / CCI20 > 100 (전형가격·평균절대편차); 조건 미충족; CCI20=69.3811 |
| v1 | williams_14_recovery | 9752.02 | -247.98 | sell /  / 직전 Williams %R14 < -80, 현재 >= -80 (한 봉 목표); 조건 미충족; Williams_R14=-49.2857, previous_R14=-77.0479 |
| v1 | cmf_20_accumulation | 9661.91 | -338.09 | buy /  / Chaikin Money Flow20 > 0.1; 조건 충족; CMF20=0.135675, volume20=5.00055e+06 |
| v1 | chaikin_3_10 | 9688.41 | -311.59 | buy /  / ADL의 EMA3 - EMA10 > 0 그리고 종가 > EMA26; 조건 충족; Chaikin3_10=2.08944e+06, ADL=1.17343e+08, close=531.15, EMA26=531.118 |
| v1 | roc_10_momentum | 9959.43 | -40.57 | sell /  / 10봉 ROC > 1% 그리고 종가 > EMA26; 조건 미충족; ROC10_percent=0.454191, close=534.125, EMA26=532.186 |
| v1 | trix_15_trend | 9712.42 | -287.58 | sell /  / 15봉 삼중 EMA의 1봉 변화율 TRIX > 0 그리고 종가 > EMA26; 조건 미충족; TRIX15_percent=0.0172213, close=526.676, EMA26=532.897 |
| v1 | keltner_20_breakout | 9958.78 | -41.22 | sell /  / 종가 > EMA20 + 2 x Wilder ATR14; 조건 미충족; close=533.975, upper_Keltner=534.357, EMA20=530.111, ATR14=2.12332 |
| v1 | opening_range_30m | 9711.79 | -288.21 | sell /  / 뉴욕 09:30·09:45 두 완료 봉 최고가를 10:00 이후 종가가 돌파; 자료 부족·변동폭 또는 거래량 없음: 대기; close=526.676 |
| v2 | cash | 10000.00 | 0.00 | 대기 /  / 새 신호 대기 |
| v2 | buy_hold | 9855.79 | -144.21 | buy / partial / 직전 완료 봉 목표 비중 100%; 다음 봉 시가 가정 |
| v2 | trend_8_26 | 9516.34 | -483.66 | sell / filled / 직전 완료 봉 목표 비중 0%; 다음 봉 시가 가정 |
| v2 | momentum_26 | 9582.52 | -417.48 | buy / partial / 직전 완료 봉 목표 비중 100%; 다음 봉 시가 가정 |
| v2 | breakout_8 | 9468.63 | -531.37 | sell / filled / 직전 완료 봉 목표 비중 0%; 다음 봉 시가 가정 |
| v2 | reversion_12 | 9175.21 | -824.79 | sell / filled / 직전 완료 봉 목표 비중 0%; 다음 봉 시가 가정 |
| v2 | volume_26 | 9406.85 | -593.15 | sell / filled / 직전 완료 봉 목표 비중 0%; 다음 봉 시가 가정 |
| v2 | trend_8_26 AND momentum_26 | 9560.49 | -439.51 | sell / filled / 직전 완료 봉 목표 비중 0%; 다음 봉 시가 가정 |
| v2 | trend_8_26 + momentum_26 | 9589.74 | -410.26 | sell / filled / 직전 완료 봉 목표 비중 50%; 다음 봉 시가 가정 |
| v2 | trend_8_26 AND breakout_8 | 9458.32 | -541.68 | sell / filled / 직전 완료 봉 목표 비중 0%; 다음 봉 시가 가정 |
| v2 | trend_8_26 + breakout_8 | 9552.86 | -447.14 | sell / filled / 직전 완료 봉 목표 비중 0%; 다음 봉 시가 가정 |
| v2 | trend_8_26 AND reversion_12 | 9521.46 | -478.54 | sell / filled / 직전 완료 봉 목표 비중 0%; 다음 봉 시가 가정 |
| v2 | trend_8_26 + reversion_12 | 9363.46 | -636.54 | sell / filled / 직전 완료 봉 목표 비중 0%; 다음 봉 시가 가정 |
| v2 | trend_8_26 AND volume_26 | 9838.23 | -161.77 | sell / filled / 직전 완료 봉 목표 비중 0%; 다음 봉 시가 가정 |
| v2 | trend_8_26 + volume_26 | 9481.28 | -518.72 | sell / filled / 직전 완료 봉 목표 비중 0%; 다음 봉 시가 가정 |
| v2 | momentum_26 AND breakout_8 | 9567.71 | -432.29 | sell / filled / 직전 완료 봉 목표 비중 0%; 다음 봉 시가 가정 |
| v2 | momentum_26 + breakout_8 | 9525.72 | -474.28 | sell / filled / 직전 완료 봉 목표 비중 50%; 다음 봉 시가 가정 |
| v2 | momentum_26 AND reversion_12 | 9475.12 | -524.88 | sell / filled / 직전 완료 봉 목표 비중 0%; 다음 봉 시가 가정 |
| v2 | momentum_26 + reversion_12 | 9376.35 | -623.65 | sell / filled / 직전 완료 봉 목표 비중 50%; 다음 봉 시가 가정 |
| v2 | momentum_26 AND volume_26 | 9695.84 | -304.16 | sell / filled / 직전 완료 봉 목표 비중 0%; 다음 봉 시가 가정 |
| v2 | momentum_26 + volume_26 | 9514.41 | -485.59 | sell / filled / 직전 완료 봉 목표 비중 50%; 다음 봉 시가 가정 |
| v2 | breakout_8 AND reversion_12 | 10000.00 | 0.00 | 대기 /  / 새 신호 대기 |
| v2 | breakout_8 + reversion_12 | 9359.64 | -640.36 | sell / filled / 직전 완료 봉 목표 비중 0%; 다음 봉 시가 가정 |
| v2 | breakout_8 AND volume_26 | 9890.09 | -109.91 | sell / filled / 직전 완료 봉 목표 비중 0%; 다음 봉 시가 가정 |
| v2 | breakout_8 + volume_26 | 9477.25 | -522.75 | sell / filled / 직전 완료 봉 목표 비중 0%; 다음 봉 시가 가정 |
| v2 | reversion_12 AND volume_26 | 9622.80 | -377.20 | sell / filled / 직전 완료 봉 목표 비중 0%; 다음 봉 시가 가정 |
| v2 | reversion_12 + volume_26 | 9309.61 | -690.39 | sell / filled / 직전 완료 봉 목표 비중 0%; 다음 봉 시가 가정 |
| v2 | ema_12_26 | 9583.12 | -416.88 | sell / filled / EMA12 > EMA26; 조건 미충족; EMA12=532.137, EMA26=532.175; 직전 완료 봉 목표를 다음 봉 시가에 모의 적용 |
| v2 | macd_12_26_9 | 9756.46 | -243.54 | sell / filled / MACD > 신호선 그리고 MACD > 0; 조건 미충족; MACD=-0.0387557, signal9=-0.0148606; 직전 완료 봉 목표를 다음 봉 시가에 모의 적용 |
| v2 | rsi_14_recovery | 9951.17 | -48.83 | sell / filled / 직전 RSI14 < 30, 현재 RSI14 >= 30 (한 봉 목표); 조건 미충족; RSI14=45.5102, previous_RSI14=37.5844; 직전 완료 봉 목표를 다음 봉 시가에 모의 적용 |
| v2 | bollinger_20_reentry | 9805.95 | -194.05 | sell / filled / 직전 종가 < 직전 하단밴드, 현재 하단밴드 <= 종가 <= SMA20 (한 봉 목표); 조건 미충족; close=529.335, lower20=528.85, SMA20=531.508, previous_lower20=529.166; 직전 완료 봉 목표를 다음 봉 시가에 모의 적용 |
| v2 | donchian_20 | 9908.19 | -91.81 | sell / filled / 종가 > 현재 봉을 제외한 직전 20봉 최고가; 조건 미충족; close=534.52, prior_high20=535.44; 직전 완료 봉 목표를 다음 봉 시가에 모의 적용 |
| v2 | atr_14_breakout | 9911.14 | -88.86 | sell / filled / 종가 > 직전 종가 + 직전 ATR14 그리고 종가 > EMA26; 조건 미충족; close=533.975, threshold=536.307, prior_ATR14=2.16203, EMA26=530.521; 직전 완료 봉 목표를 다음 봉 시가에 모의 적용 |
| v2 | session_vwap | 9813.96 | -186.04 | buy / partial / 종가 > 뉴욕 거래일별 누적 전형가격 VWAP; 조건 충족; close=530.964, session_VWAP=530.832, session_volume=8.43578e+06; 직전 완료 봉 목표를 다음 봉 시가에 모의 적용 |
| v2 | obv_20 | 9635.55 | -364.45 | buy / partial / OBV > OBV의 SMA20 그리고 종가 > EMA26; 조건 충족; OBV=9.04505e+07, OBV_SMA20=9.01119e+07, close=531.15, EMA26=531.118; 직전 완료 봉 목표를 다음 봉 시가에 모의 적용 |
| v2 | stochastic_14_3_recovery | 9779.25 | -220.75 | sell / filled / 직전 %K14 < 20에서 %K14가 %D3 상향 돌파 (한 봉 목표); 조건 미충족; K14=60.6262, D3=34.5689, previous_K14=38.87, previous_D3=26.948; 직전 완료 봉 목표를 다음 봉 시가에 모의 적용 |
| v2 | mfi_14_recovery | 9968.59 | -31.41 | sell / filled / 직전 MFI14 < 20, 현재 MFI14 >= 20 (한 봉 목표); 조건 미충족; MFI14=53.413, previous_MFI14=44.3372; 직전 완료 봉 목표를 다음 봉 시가에 모의 적용 |
| v2 | adx_14_trend | 9879.67 | -120.33 | sell / filled / Wilder ADX14 >= 25 그리고 +DI14 > -DI14; 조건 미충족; ADX14=23.6824, plus_DI14=22.3066, minus_DI14=19.9214; 직전 완료 봉 목표를 다음 봉 시가에 모의 적용 |
| v2 | aroon_25_trend | 9808.55 | -191.45 | sell / filled / Aroon25 Up > 70 그리고 Down < 30 (동률이면 최신 극값); 조건 미충족; Aroon_up=68, Aroon_down=20; 직전 완료 봉 목표를 다음 봉 시가에 모의 적용 |
| v2 | cci_20_momentum | 9945.68 | -54.32 | sell / filled / CCI20 > 100 (전형가격·평균절대편차); 조건 미충족; CCI20=69.3811; 직전 완료 봉 목표를 다음 봉 시가에 모의 적용 |
| v2 | williams_14_recovery | 9742.27 | -257.73 | sell / filled / 직전 Williams %R14 < -80, 현재 >= -80 (한 봉 목표); 조건 미충족; Williams_R14=-49.2857, previous_R14=-77.0479; 직전 완료 봉 목표를 다음 봉 시가에 모의 적용 |
| v2 | cmf_20_accumulation | 9655.15 | -344.85 | buy / partial / Chaikin Money Flow20 > 0.1; 조건 충족; CMF20=0.135675, volume20=5.00055e+06; 직전 완료 봉 목표를 다음 봉 시가에 모의 적용 |
| v2 | chaikin_3_10 | 9675.82 | -324.18 | buy / partial / ADL의 EMA3 - EMA10 > 0 그리고 종가 > EMA26; 조건 충족; Chaikin3_10=2.08944e+06, ADL=1.17343e+08, close=531.15, EMA26=531.118; 직전 완료 봉 목표를 다음 봉 시가에 모의 적용 |
| v2 | roc_10_momentum | 9957.44 | -42.56 | sell / filled / 10봉 ROC > 1% 그리고 종가 > EMA26; 조건 미충족; ROC10_percent=0.454191, close=534.125, EMA26=532.186; 직전 완료 봉 목표를 다음 봉 시가에 모의 적용 |
| v2 | trix_15_trend | 9708.54 | -291.46 | sell / filled / 15봉 삼중 EMA의 1봉 변화율 TRIX > 0 그리고 종가 > EMA26; 조건 미충족; TRIX15_percent=0.0172213, close=526.676, EMA26=532.897; 직전 완료 봉 목표를 다음 봉 시가에 모의 적용 |
| v2 | keltner_20_breakout | 9956.78 | -43.22 | sell / filled / 종가 > EMA20 + 2 x Wilder ATR14; 조건 미충족; close=533.975, upper_Keltner=534.357, EMA20=530.111, ATR14=2.12332; 직전 완료 봉 목표를 다음 봉 시가에 모의 적용 |
| v2 | opening_range_30m | 9707.90 | -292.10 | sell / filled / 뉴욕 09:30·09:45 두 완료 봉 최고가를 10:00 이후 종가가 돌파; 자료 부족·변동폭 또는 거래량 없음: 대기; close=526.676; 직전 완료 봉 목표를 다음 봉 시가에 모의 적용 |

### 같은 기간의 비용·노출 비교 (사후 연구)

| 전략 | 비용 전 | 비용 후 | 100% 보유 | 같은 평균 노출 보유 | 평균 노출 |
|---|---:|---:|---:|---:|---:|
| cash | 0.00% | 0.00% | 2.12% | 0.00% | 0.00% |
| buy_hold | 2.55% | 2.12% | 2.12% | 2.12% | 100.00% |
| trend_8_26 | -0.82% | -4.50% | 2.12% | 1.19% | 56.99% |
| momentum_26 | -0.52% | -6.60% | 2.12% | 1.20% | 57.26% |
| breakout_8 | 6.28% | -7.86% | 2.12% | 0.40% | 19.26% |
| reversion_12 | -4.69% | -13.83% | 2.12% | 0.54% | 25.86% |
| volume_26 | 0.33% | -8.14% | 2.12% | 0.19% | 8.97% |
| trend_8_26 AND momentum_26 | -1.50% | -6.73% | 2.12% | 1.05% | 50.40% |
| trend_8_26 + momentum_26 | -0.67% | -5.15% | 2.12% | 1.20% | 57.13% |
| trend_8_26 AND breakout_8 | 0.51% | -9.13% | 2.12% | 0.25% | 11.87% |
| trend_8_26 + breakout_8 | 2.69% | -5.40% | 2.12% | 0.80% | 38.13% |
| trend_8_26 AND reversion_12 | -1.80% | -7.80% | 2.12% | 0.15% | 7.39% |
| trend_8_26 + reversion_12 | -2.76% | -8.90% | 2.12% | 0.87% | 41.43% |
| trend_8_26 AND volume_26 | 2.59% | -0.80% | 2.12% | 0.06% | 2.90% |
| trend_8_26 + volume_26 | -0.23% | -5.75% | 2.12% | 0.69% | 32.99% |
| momentum_26 AND breakout_8 | 2.76% | -7.48% | 2.12% | 0.25% | 12.14% |
| momentum_26 + breakout_8 | 2.83% | -6.84% | 2.12% | 0.80% | 38.26% |
| momentum_26 AND reversion_12 | -2.82% | -9.51% | 2.12% | 0.21% | 10.03% |
| momentum_26 + reversion_12 | -2.61% | -10.29% | 2.12% | 0.87% | 41.56% |
| momentum_26 AND volume_26 | 0.81% | -4.14% | 2.12% | 0.08% | 3.96% |
| momentum_26 + volume_26 | -0.08% | -6.98% | 2.12% | 0.69% | 33.12% |
| breakout_8 AND reversion_12 | 0.00% | 0.00% | 2.12% | 0.00% | 0.00% |
| breakout_8 + reversion_12 | 0.67% | -10.14% | 2.12% | 0.47% | 22.57% |
| breakout_8 AND volume_26 | 2.04% | -0.50% | 2.12% | 0.04% | 1.85% |
| breakout_8 + volume_26 | 3.28% | -7.41% | 2.12% | 0.29% | 14.12% |
| reversion_12 AND volume_26 | -2.86% | -6.85% | 2.12% | 0.08% | 3.96% |
| reversion_12 + volume_26 | -2.20% | -10.84% | 2.12% | 0.36% | 17.42% |
| ema_12_26 | -1.46% | -5.11% | 2.12% | 1.22% | 58.31% |
| macd_12_26_9 | -0.41% | -5.30% | 2.12% | 0.68% | 32.45% |
| rsi_14_recovery | 0.31% | -2.19% | 2.12% | 0.03% | 1.58% |
| bollinger_20_reentry | -0.93% | -4.21% | 2.12% | 0.04% | 2.11% |
| donchian_20 | 1.05% | -4.32% | 2.12% | 0.09% | 4.22% |
| atr_14_breakout | 1.36% | -3.62% | 2.12% | 0.07% | 3.43% |
| session_vwap | 5.58% | -2.52% | 2.12% | 0.87% | 41.69% |
| obv_20 | 5.23% | -3.65% | 2.12% | 1.02% | 48.81% |
| stochastic_14_3_recovery | -0.57% | -10.11% | 2.12% | 0.13% | 6.33% |
| mfi_14_recovery | 1.58% | -2.19% | 2.12% | 0.05% | 2.37% |
| adx_14_trend | 3.96% | 1.37% | 2.12% | 0.92% | 44.06% |
| aroon_25_trend | -0.49% | -4.59% | 2.12% | 0.44% | 21.37% |
| cci_20_momentum | 2.56% | -3.70% | 2.12% | 0.42% | 20.32% |
| williams_14_recovery | -1.61% | -10.30% | 2.12% | 0.12% | 5.80% |
| cmf_20_accumulation | 0.48% | -5.66% | 2.12% | 0.77% | 36.68% |
| chaikin_3_10 | 4.13% | -4.26% | 2.12% | 0.98% | 46.70% |
| roc_10_momentum | -0.61% | -4.30% | 2.12% | 0.27% | 13.19% |
| trix_15_trend | -1.14% | -5.20% | 2.12% | 0.95% | 45.38% |
| keltner_20_breakout | 0.49% | -4.45% | 2.12% | 0.24% | 11.61% |
| opening_range_30m | -1.20% | -4.47% | 2.12% | 0.37% | 17.94% |

동일 구간·초기 자금, 종료 시 청산 비용 포함. 노출 맞춤은 사후 설명용이며 v2 실제 계좌 성과가 아닙니다.
[낙폭 분해·비용 영향·전체 구간](MSFT/comparison.json)

[v1 전체 기록](MSFT/accounts.json) · [v2 전체 기록](MSFT/accounts-v2.json)

## JPM 계좌

| 모델 | 전략 | 평가액 USD | 손익 USD | 최근 매매·이유 |
|---|---|---:|---:|---|
| v1 | cash | 10000.00 | 0.00 | 대기 /  / 새 신호 대기 |
| v1 | buy_hold | 9793.74 | -206.26 | buy /  / buy_hold: prior completed bar target 100%; next bar open simulation |
| v1 | trend_8_26 | 9786.16 | -213.84 | sell /  / trend_8_26: prior completed bar target 0%; next bar open simulation |
| v1 | momentum_26 | 9646.55 | -353.45 | sell /  / momentum_26: prior completed bar target 0%; next bar open simulation |
| v1 | breakout_8 | 9759.46 | -240.54 | sell /  / breakout_8: prior completed bar target 0%; next bar open simulation |
| v1 | reversion_12 | 9608.78 | -391.22 | sell /  / reversion_12: prior completed bar target 0%; next bar open simulation |
| v1 | volume_26 | 9854.06 | -145.94 | sell /  / volume_26: prior completed bar target 0%; next bar open simulation |
| v1 | trend_8_26 AND momentum_26 | 9793.49 | -206.51 | sell /  / trend_8_26 AND momentum_26: prior completed bar target 0%; next bar open simulation |
| v1 | trend_8_26 + momentum_26 | 9716.16 | -283.84 | sell /  / trend_8_26 + momentum_26: prior completed bar target 0%; next bar open simulation |
| v1 | trend_8_26 AND breakout_8 | 9915.55 | -84.45 | sell /  / trend_8_26 AND breakout_8: prior completed bar target 0%; next bar open simulation |
| v1 | trend_8_26 + breakout_8 | 9792.38 | -207.62 | sell /  / trend_8_26 + breakout_8: prior completed bar target 0%; next bar open simulation |
| v1 | trend_8_26 AND reversion_12 | 9855.61 | -144.39 | sell /  / trend_8_26 AND reversion_12: prior completed bar target 0%; next bar open simulation |
| v1 | trend_8_26 + reversion_12 | 9696.91 | -303.09 | sell /  / trend_8_26 + reversion_12: prior completed bar target 0%; next bar open simulation |
| v1 | trend_8_26 AND volume_26 | 10035.68 | 35.68 | sell /  / trend_8_26 AND volume_26: prior completed bar target 0%; next bar open simulation |
| v1 | trend_8_26 + volume_26 | 9819.94 | -180.06 | sell /  / trend_8_26 + volume_26: prior completed bar target 0%; next bar open simulation |
| v1 | momentum_26 AND breakout_8 | 9733.77 | -266.23 | sell /  / momentum_26 AND breakout_8: prior completed bar target 0%; next bar open simulation |
| v1 | momentum_26 + breakout_8 | 9702.99 | -297.01 | sell /  / momentum_26 + breakout_8: prior completed bar target 0%; next bar open simulation |
| v1 | momentum_26 AND reversion_12 | 9849.85 | -150.15 | sell /  / momentum_26 AND reversion_12: prior completed bar target 0%; next bar open simulation |
| v1 | momentum_26 + reversion_12 | 9685.49 | -314.51 | sell /  / momentum_26 + reversion_12: prior completed bar target 0%; next bar open simulation |
| v1 | momentum_26 AND volume_26 | 9926.98 | -73.02 | sell /  / momentum_26 AND volume_26: prior completed bar target 0%; next bar open simulation |
| v1 | momentum_26 + volume_26 | 9769.23 | -230.77 | sell /  / momentum_26 + volume_26: prior completed bar target 0%; next bar open simulation |
| v1 | breakout_8 AND reversion_12 | 10000.00 | 0.00 | 대기 /  / 새 신호 대기 |
| v1 | breakout_8 + reversion_12 | 9722.47 | -277.53 | sell /  / breakout_8 + reversion_12: prior completed bar target 0%; next bar open simulation |
| v1 | breakout_8 AND volume_26 | 10022.00 | 22.00 | sell /  / breakout_8 AND volume_26: prior completed bar target 0%; next bar open simulation |
| v1 | breakout_8 + volume_26 | 9806.65 | -193.35 | sell /  / breakout_8 + volume_26: prior completed bar target 0%; next bar open simulation |
| v1 | reversion_12 AND volume_26 | 9940.10 | -59.90 | sell /  / reversion_12 AND volume_26: prior completed bar target 0%; next bar open simulation |
| v1 | reversion_12 + volume_26 | 9769.50 | -230.50 | sell /  / reversion_12 + volume_26: prior completed bar target 0%; next bar open simulation |
| v1 | ema_12_26 | 9755.41 | -244.59 | sell /  / EMA12 > EMA26; 조건 미충족; EMA12=336.517, EMA26=336.551 |
| v1 | macd_12_26_9 | 9839.10 | -160.90 | sell /  / MACD > 신호선 그리고 MACD > 0; 조건 미충족; MACD=-0.0344827, signal9=-0.0504891 |
| v1 | rsi_14_recovery | 9986.37 | -13.63 | sell /  / 직전 RSI14 < 30, 현재 RSI14 >= 30 (한 봉 목표); 조건 미충족; RSI14=61.6663, previous_RSI14=57.046 |
| v1 | bollinger_20_reentry | 9849.78 | -150.22 | sell /  / 직전 종가 < 직전 하단밴드, 현재 하단밴드 <= 종가 <= SMA20 (한 봉 목표); 조건 미충족; close=333.59, lower20=333.09, SMA20=334.751, previous_lower20=333.244 |
| v1 | donchian_20 | 9830.85 | -169.15 | sell /  / 종가 > 현재 봉을 제외한 직전 20봉 최고가; 조건 미충족; close=339.04, prior_high20=339.42 |
| v1 | atr_14_breakout | 9746.56 | -253.44 | sell /  / 종가 > 직전 종가 + 직전 ATR14 그리고 종가 > EMA26; 조건 미충족; close=339.04, threshold=340.465, prior_ATR14=1.34545, EMA26=336.613 |
| v1 | session_vwap | 9727.57 | -272.43 | sell /  / 종가 > 뉴욕 거래일별 누적 전형가격 VWAP; 조건 미충족; close=336.08, session_VWAP=337.149, session_volume=2.04555e+06 |
| v1 | obv_20 | 10007.55 | 7.55 | sell /  / OBV > OBV의 SMA20 그리고 종가 > EMA26; 조건 미충족; OBV=-1.66645e+07, OBV_SMA20=-1.38199e+07, close=341.625, EMA26=338.807 |
| v1 | stochastic_14_3_recovery | 9575.82 | -424.18 | sell /  / 직전 %K14 < 20에서 %K14가 %D3 상향 돌파 (한 봉 목표); 조건 미충족; K14=36.1707, D3=21.3001, previous_K14=19.2613, previous_D3=15.9414 |
| v1 | mfi_14_recovery | 9935.64 | -64.36 | sell /  / 직전 MFI14 < 20, 현재 MFI14 >= 20 (한 봉 목표); 조건 미충족; MFI14=30.2719, previous_MFI14=26.8492 |
| v1 | adx_14_trend | 9726.68 | -273.32 | sell /  / Wilder ADX14 >= 25 그리고 +DI14 > -DI14; 조건 미충족; ADX14=23.9395, plus_DI14=23.2021, minus_DI14=22.594 |
| v1 | aroon_25_trend | 9824.71 | -175.29 | sell /  / Aroon25 Up > 70 그리고 Down < 30 (동률이면 최신 극값); 조건 미충족; Aroon_up=68, Aroon_down=16 |
| v1 | cci_20_momentum | 9950.54 | -49.46 | sell /  / CCI20 > 100 (전형가격·평균절대편차); 조건 미충족; CCI20=28.4392 |
| v1 | williams_14_recovery | 9568.76 | -431.24 | sell /  / 직전 Williams %R14 < -80, 현재 >= -80 (한 봉 목표); 조건 미충족; Williams_R14=-78.9473, previous_R14=-79.2829 |
| v1 | cmf_20_accumulation | 9828.96 | -171.04 | sell /  / Chaikin Money Flow20 > 0.1; 조건 미충족; CMF20=-0.0481318, volume20=2.57468e+06 |
| v1 | chaikin_3_10 | 9837.22 | -162.78 | sell /  / ADL의 EMA3 - EMA10 > 0 그리고 종가 > EMA26; 조건 미충족; Chaikin3_10=7273.89, ADL=-1.2896e+07, close=336.08, EMA26=336.65 |
| v1 | roc_10_momentum | 9836.40 | -163.60 | sell /  / 10봉 ROC > 1% 그리고 종가 > EMA26; 조건 미충족; ROC10_percent=0.964142, close=337.72, EMA26=336.695 |
| v1 | trix_15_trend | 9723.73 | -276.27 | sell /  / 15봉 삼중 EMA의 1봉 변화율 TRIX > 0 그리고 종가 > EMA26; 조건 미충족; TRIX15_percent=0.0135144, close=337.6, EMA26=338.759 |
| v1 | keltner_20_breakout | 9905.24 | -94.76 | sell /  / 종가 > EMA20 + 2 x Wilder ATR14; 조건 미충족; close=339.04, upper_Keltner=339.281, EMA20=336.559, ATR14=1.36146 |
| v1 | opening_range_30m | 9850.26 | -149.74 | sell /  / 뉴욕 09:30·09:45 두 완료 봉 최고가를 10:00 이후 종가가 돌파; 조건 미충족; close=337.72, opening_high=339.035 |
| v2 | cash | 10000.00 | 0.00 | 대기 /  / 새 신호 대기 |
| v2 | buy_hold | 9957.39 | -42.61 | buy / partial / 직전 완료 봉 목표 비중 100%; 다음 봉 시가 가정 |
| v2 | trend_8_26 | 9791.24 | -208.76 | sell / filled / 직전 완료 봉 목표 비중 0%; 다음 봉 시가 가정 |
| v2 | momentum_26 | 9160.46 | -839.54 | sell / filled / 직전 완료 봉 목표 비중 0%; 다음 봉 시가 가정 |
| v2 | breakout_8 | 9100.10 | -899.90 | sell / filled / 직전 완료 봉 목표 비중 0%; 다음 봉 시가 가정 |
| v2 | reversion_12 | 9578.05 | -421.95 | sell / filled / 직전 완료 봉 목표 비중 0%; 다음 봉 시가 가정 |
| v2 | volume_26 | 9673.61 | -326.39 | sell / filled / 직전 완료 봉 목표 비중 0%; 다음 봉 시가 가정 |
| v2 | trend_8_26 AND momentum_26 | 9756.41 | -243.59 | sell / filled / 직전 완료 봉 목표 비중 0%; 다음 봉 시가 가정 |
| v2 | trend_8_26 + momentum_26 | 9491.08 | -508.92 | sell / filled / 직전 완료 봉 목표 비중 0%; 다음 봉 시가 가정 |
| v2 | trend_8_26 AND breakout_8 | 9287.76 | -712.24 | sell / filled / 직전 완료 봉 목표 비중 0%; 다음 봉 시가 가정 |
| v2 | trend_8_26 + breakout_8 | 9460.24 | -539.76 | sell / filled / 직전 완료 봉 목표 비중 0%; 다음 봉 시가 가정 |
| v2 | trend_8_26 AND reversion_12 | 9831.59 | -168.41 | sell / filled / 직전 완료 봉 목표 비중 0%; 다음 봉 시가 가정 |
| v2 | trend_8_26 + reversion_12 | 9724.85 | -275.15 | sell / filled / 직전 완료 봉 목표 비중 0%; 다음 봉 시가 가정 |
| v2 | trend_8_26 AND volume_26 | 9833.30 | -166.70 | sell / filled / 직전 완료 봉 목표 비중 0%; 다음 봉 시가 가정 |
| v2 | trend_8_26 + volume_26 | 9732.95 | -267.05 | sell / filled / 직전 완료 봉 목표 비중 0%; 다음 봉 시가 가정 |
| v2 | momentum_26 AND breakout_8 | 9058.00 | -942.00 | sell / filled / 직전 완료 봉 목표 비중 0%; 다음 봉 시가 가정 |
| v2 | momentum_26 + breakout_8 | 9151.14 | -848.86 | sell / filled / 직전 완료 봉 목표 비중 0%; 다음 봉 시가 가정 |
| v2 | momentum_26 AND reversion_12 | 9793.51 | -206.49 | sell / filled / 직전 완료 봉 목표 비중 0%; 다음 봉 시가 가정 |
| v2 | momentum_26 + reversion_12 | 9546.08 | -453.92 | sell / filled / 직전 완료 봉 목표 비중 0%; 다음 봉 시가 가정 |
| v2 | momentum_26 AND volume_26 | 9724.84 | -275.16 | sell / filled / 직전 완료 봉 목표 비중 0%; 다음 봉 시가 가정 |
| v2 | momentum_26 + volume_26 | 9494.12 | -505.88 | sell / filled / 직전 완료 봉 목표 비중 0%; 다음 봉 시가 가정 |
| v2 | breakout_8 AND reversion_12 | 10000.00 | 0.00 | 대기 /  / 새 신호 대기 |
| v2 | breakout_8 + reversion_12 | 9414.81 | -585.19 | sell / filled / 직전 완료 봉 목표 비중 0%; 다음 봉 시가 가정 |
| v2 | breakout_8 AND volume_26 | 9911.14 | -88.86 | sell / filled / 직전 완료 봉 목표 비중 0%; 다음 봉 시가 가정 |
| v2 | breakout_8 + volume_26 | 9402.34 | -597.66 | sell / filled / 직전 완료 봉 목표 비중 0%; 다음 봉 시가 가정 |
| v2 | reversion_12 AND volume_26 | 9987.18 | -12.82 | sell / filled / 직전 완료 봉 목표 비중 0%; 다음 봉 시가 가정 |
| v2 | reversion_12 + volume_26 | 9686.66 | -313.34 | sell / filled / 직전 완료 봉 목표 비중 0%; 다음 봉 시가 가정 |
| v2 | ema_12_26 | 9751.51 | -248.49 | sell / filled / EMA12 > EMA26; 조건 미충족; EMA12=336.517, EMA26=336.551; 직전 완료 봉 목표를 다음 봉 시가에 모의 적용 |
| v2 | macd_12_26_9 | 9835.16 | -164.84 | sell / filled / MACD > 신호선 그리고 MACD > 0; 조건 미충족; MACD=-0.0344827, signal9=-0.0504891; 직전 완료 봉 목표를 다음 봉 시가에 모의 적용 |
| v2 | rsi_14_recovery | 9984.37 | -15.63 | sell / filled / 직전 RSI14 < 30, 현재 RSI14 >= 30 (한 봉 목표); 조건 미충족; RSI14=61.6663, previous_RSI14=57.046; 직전 완료 봉 목표를 다음 봉 시가에 모의 적용 |
| v2 | bollinger_20_reentry | 9843.87 | -156.13 | sell / filled / 직전 종가 < 직전 하단밴드, 현재 하단밴드 <= 종가 <= SMA20 (한 봉 목표); 조건 미충족; close=333.59, lower20=333.09, SMA20=334.751, previous_lower20=333.244; 직전 완료 봉 목표를 다음 봉 시가에 모의 적용 |
| v2 | donchian_20 | 9824.96 | -175.04 | sell / filled / 종가 > 현재 봉을 제외한 직전 20봉 최고가; 조건 미충족; close=339.04, prior_high20=339.42; 직전 완료 봉 목표를 다음 봉 시가에 모의 적용 |
| v2 | atr_14_breakout | 9736.82 | -263.18 | sell / filled / 종가 > 직전 종가 + 직전 ATR14 그리고 종가 > EMA26; 조건 미충족; close=339.04, threshold=340.465, prior_ATR14=1.34545, EMA26=336.613; 직전 완료 봉 목표를 다음 봉 시가에 모의 적용 |
| v2 | session_vwap | 9717.84 | -282.16 | sell / filled / 종가 > 뉴욕 거래일별 누적 전형가격 VWAP; 조건 미충족; close=336.08, session_VWAP=337.149, session_volume=2.04555e+06; 직전 완료 봉 목표를 다음 봉 시가에 모의 적용 |
| v2 | obv_20 | 10005.55 | 5.55 | sell / filled / OBV > OBV의 SMA20 그리고 종가 > EMA26; 조건 미충족; OBV=-1.38544e+07, OBV_SMA20=-1.10099e+07, close=341.625, EMA26=338.807; 직전 완료 봉 목표를 다음 봉 시가에 모의 적용 |
| v2 | stochastic_14_3_recovery | 9554.77 | -445.23 | sell / filled / 직전 %K14 < 20에서 %K14가 %D3 상향 돌파 (한 봉 목표); 조건 미충족; K14=36.1707, D3=21.3001, previous_K14=19.2613, previous_D3=15.9414; 직전 완료 봉 목표를 다음 봉 시가에 모의 적용 |
| v2 | mfi_14_recovery | 9931.66 | -68.34 | sell / filled / 직전 MFI14 < 20, 현재 MFI14 >= 20 (한 봉 목표); 조건 미충족; MFI14=30.2719, previous_MFI14=26.8492; 직전 완료 봉 목표를 다음 봉 시가에 모의 적용 |
| v2 | adx_14_trend | 9722.79 | -277.21 | sell / filled / Wilder ADX14 >= 25 그리고 +DI14 > -DI14; 조건 미충족; ADX14=23.9395, plus_DI14=23.2021, minus_DI14=22.594; 직전 완료 봉 목표를 다음 봉 시가에 모의 적용 |
| v2 | aroon_25_trend | 9822.74 | -177.26 | sell / filled / Aroon25 Up > 70 그리고 Down < 30 (동률이면 최신 극값); 조건 미충족; Aroon_up=68, Aroon_down=16; 직전 완료 봉 목표를 다음 봉 시가에 모의 적용 |
| v2 | cci_20_momentum | 9946.56 | -53.44 | sell / filled / CCI20 > 100 (전형가격·평균절대편차); 조건 미충족; CCI20=28.4392; 직전 완료 봉 목표를 다음 봉 시가에 모의 적용 |
| v2 | williams_14_recovery | 9549.64 | -450.36 | sell / filled / 직전 Williams %R14 < -80, 현재 >= -80 (한 봉 목표); 조건 미충족; Williams_R14=-78.9473, previous_R14=-79.2829; 직전 완료 봉 목표를 다음 봉 시가에 모의 적용 |
| v2 | cmf_20_accumulation | 9823.06 | -176.94 | sell / filled / Chaikin Money Flow20 > 0.1; 조건 미충족; CMF20=-0.0481318, volume20=2.57468e+06; 직전 완료 봉 목표를 다음 봉 시가에 모의 적용 |
| v2 | chaikin_3_10 | 9831.32 | -168.68 | sell / filled / ADL의 EMA3 - EMA10 > 0 그리고 종가 > EMA26; 조건 미충족; Chaikin3_10=7273.89, ADL=-1.28498e+07, close=336.08, EMA26=336.65; 직전 완료 봉 목표를 다음 봉 시가에 모의 적용 |
| v2 | roc_10_momentum | 9832.47 | -167.53 | sell / filled / 10봉 ROC > 1% 그리고 종가 > EMA26; 조건 미충족; ROC10_percent=0.964142, close=337.72, EMA26=336.695; 직전 완료 봉 목표를 다음 봉 시가에 모의 적용 |
| v2 | trix_15_trend | 9715.96 | -284.04 | sell / filled / 15봉 삼중 EMA의 1봉 변화율 TRIX > 0 그리고 종가 > EMA26; 조건 미충족; TRIX15_percent=0.0135144, close=337.6, EMA26=338.759; 직전 완료 봉 목표를 다음 봉 시가에 모의 적용 |
| v2 | keltner_20_breakout | 9901.28 | -98.72 | sell / filled / 종가 > EMA20 + 2 x Wilder ATR14; 조건 미충족; close=339.04, upper_Keltner=339.281, EMA20=336.559, ATR14=1.36146; 직전 완료 봉 목표를 다음 봉 시가에 모의 적용 |
| v2 | opening_range_30m | 9846.33 | -153.67 | sell / filled / 뉴욕 09:30·09:45 두 완료 봉 최고가를 10:00 이후 종가가 돌파; 조건 미충족; close=337.72, opening_high=339.035; 직전 완료 봉 목표를 다음 봉 시가에 모의 적용 |

### 같은 기간의 비용·노출 비교 (사후 연구)

| 전략 | 비용 전 | 비용 후 | 100% 보유 | 같은 평균 노출 보유 | 평균 노출 |
|---|---:|---:|---:|---:|---:|
| cash | 0.00% | 0.00% | 0.04% | 0.00% | 0.00% |
| buy_hold | 0.47% | 0.04% | 0.04% | 0.04% | 100.00% |
| trend_8_26 | 0.52% | -3.21% | 0.04% | 0.02% | 52.77% |
| momentum_26 | -3.27% | -10.69% | 0.04% | 0.02% | 52.24% |
| breakout_8 | -2.73% | -17.43% | 0.04% | 0.01% | 19.79% |
| reversion_12 | 5.68% | -9.53% | 0.04% | 0.01% | 24.80% |
| volume_26 | -0.40% | -6.87% | 0.04% | 0.00% | 7.12% |
| trend_8_26 AND momentum_26 | 0.56% | -4.38% | 0.04% | 0.02% | 41.42% |
| trend_8_26 + momentum_26 | -1.38% | -6.82% | 0.04% | 0.02% | 52.51% |
| trend_8_26 AND breakout_8 | -3.21% | -13.22% | 0.04% | 0.01% | 12.14% |
| trend_8_26 + breakout_8 | -1.10% | -10.21% | 0.04% | 0.02% | 36.29% |
| trend_8_26 AND reversion_12 | 2.81% | -3.46% | 0.04% | 0.00% | 7.12% |
| trend_8_26 + reversion_12 | 3.09% | -5.84% | 0.04% | 0.02% | 38.79% |
| trend_8_26 AND volume_26 | -0.37% | -3.66% | 0.04% | 0.00% | 3.69% |
| trend_8_26 + volume_26 | 0.08% | -5.05% | 0.04% | 0.01% | 29.95% |
| momentum_26 AND breakout_8 | -2.68% | -13.84% | 0.04% | 0.01% | 12.66% |
| momentum_26 + breakout_8 | -2.97% | -13.92% | 0.04% | 0.02% | 36.02% |
| momentum_26 AND reversion_12 | 2.87% | -4.62% | 0.04% | 0.00% | 7.12% |
| momentum_26 + reversion_12 | 1.13% | -8.20% | 0.04% | 0.02% | 38.53% |
| momentum_26 AND volume_26 | -0.48% | -3.77% | 0.04% | 0.00% | 3.17% |
| momentum_26 + volume_26 | -1.82% | -8.41% | 0.04% | 0.01% | 29.69% |
| breakout_8 AND reversion_12 | 0.00% | 0.00% | 0.04% | 0.00% | 0.00% |
| breakout_8 + reversion_12 | 1.41% | -12.29% | 0.04% | 0.01% | 22.31% |
| breakout_8 AND volume_26 | -0.25% | -2.32% | 0.04% | 0.00% | 1.32% |
| breakout_8 + volume_26 | -1.56% | -11.57% | 0.04% | 0.01% | 13.46% |
| reversion_12 AND volume_26 | 1.38% | -1.56% | 0.04% | 0.00% | 3.17% |
| reversion_12 + volume_26 | 2.61% | -7.05% | 0.04% | 0.01% | 15.97% |
| ema_12_26 | -0.24% | -3.54% | 0.04% | 0.02% | 52.24% |
| macd_12_26_9 | -0.13% | -4.64% | 0.04% | 0.01% | 32.98% |
| rsi_14_recovery | 0.59% | -1.08% | 0.04% | 0.00% | 1.06% |
| bollinger_20_reentry | 0.25% | -3.87% | 0.04% | 0.00% | 2.64% |
| donchian_20 | -1.81% | -5.05% | 0.04% | 0.00% | 3.17% |
| atr_14_breakout | -1.35% | -8.92% | 0.04% | 0.00% | 5.28% |
| session_vwap | 1.67% | -7.69% | 0.04% | 0.02% | 46.97% |
| obv_20 | -3.42% | -13.78% | 0.04% | 0.01% | 30.08% |
| stochastic_14_3_recovery | -0.98% | -11.97% | 0.04% | 0.00% | 7.39% |
| mfi_14_recovery | 0.25% | -1.42% | 0.04% | 0.00% | 1.06% |
| adx_14_trend | -2.43% | -4.85% | 0.04% | 0.01% | 29.82% |
| aroon_25_trend | -0.75% | -4.43% | 0.04% | 0.01% | 21.90% |
| cci_20_momentum | -2.84% | -10.67% | 0.04% | 0.01% | 16.36% |
| williams_14_recovery | -1.32% | -12.27% | 0.04% | 0.00% | 7.39% |
| cmf_20_accumulation | -1.98% | -10.63% | 0.04% | 0.01% | 30.34% |
| chaikin_3_10 | 1.01% | -7.52% | 0.04% | 0.02% | 34.04% |
| roc_10_momentum | -1.36% | -4.22% | 0.04% | 0.00% | 8.44% |
| trix_15_trend | -1.25% | -8.83% | 0.04% | 0.02% | 35.36% |
| keltner_20_breakout | -1.21% | -4.07% | 0.04% | 0.00% | 4.22% |
| opening_range_30m | -0.23% | -3.93% | 0.04% | 0.01% | 17.41% |

동일 구간·초기 자금, 종료 시 청산 비용 포함. 노출 맞춤은 사후 설명용이며 v2 실제 계좌 성과가 아닙니다.
[낙폭 분해·비용 영향·전체 구간](JPM/comparison.json)

[v1 전체 기록](JPM/accounts.json) · [v2 전체 기록](JPM/accounts-v2.json)

## XOM 계좌

| 모델 | 전략 | 평가액 USD | 손익 USD | 최근 매매·이유 |
|---|---|---:|---:|---|
| v1 | cash | 10000.00 | 0.00 | 대기 /  / 새 신호 대기 |
| v1 | buy_hold | 10048.74 | 48.74 | buy /  / buy_hold: prior completed bar target 100%; next bar open simulation |
| v1 | trend_8_26 | 9862.24 | -137.76 | buy /  / trend_8_26: prior completed bar target 100%; next bar open simulation |
| v1 | momentum_26 | 9907.21 | -92.79 | buy /  / momentum_26: prior completed bar target 100%; next bar open simulation |
| v1 | breakout_8 | 9566.22 | -433.78 | sell /  / breakout_8: prior completed bar target 0%; next bar open simulation |
| v1 | reversion_12 | 9683.62 | -316.38 | sell /  / reversion_12: prior completed bar target 0%; next bar open simulation |
| v1 | volume_26 | 9648.38 | -351.62 | sell /  / volume_26: prior completed bar target 0%; next bar open simulation |
| v1 | trend_8_26 AND momentum_26 | 9826.35 | -173.65 | buy /  / trend_8_26 AND momentum_26: prior completed bar target 100%; next bar open simulation |
| v1 | trend_8_26 + momentum_26 | 9884.80 | -115.20 | buy /  / trend_8_26 + momentum_26: prior completed bar target 100%; next bar open simulation |
| v1 | trend_8_26 AND breakout_8 | 9704.96 | -295.04 | sell /  / trend_8_26 AND breakout_8: prior completed bar target 0%; next bar open simulation |
| v1 | trend_8_26 + breakout_8 | 9732.95 | -267.05 | buy /  / trend_8_26 + breakout_8: prior completed bar target 50%; next bar open simulation |
| v1 | trend_8_26 AND reversion_12 | 9677.97 | -322.03 | sell /  / trend_8_26 AND reversion_12: prior completed bar target 0%; next bar open simulation |
| v1 | trend_8_26 + reversion_12 | 9772.46 | -227.54 | buy /  / trend_8_26 + reversion_12: prior completed bar target 50%; next bar open simulation |
| v1 | trend_8_26 AND volume_26 | 9764.30 | -235.70 | sell /  / trend_8_26 AND volume_26: prior completed bar target 0%; next bar open simulation |
| v1 | trend_8_26 + volume_26 | 9754.93 | -245.07 | buy /  / trend_8_26 + volume_26: prior completed bar target 50%; next bar open simulation |
| v1 | momentum_26 AND breakout_8 | 9801.24 | -198.76 | sell /  / momentum_26 AND breakout_8: prior completed bar target 0%; next bar open simulation |
| v1 | momentum_26 + breakout_8 | 9735.46 | -264.54 | buy /  / momentum_26 + breakout_8: prior completed bar target 50%; next bar open simulation |
| v1 | momentum_26 AND reversion_12 | 9766.58 | -233.42 | sell /  / momentum_26 AND reversion_12: prior completed bar target 0%; next bar open simulation |
| v1 | momentum_26 + reversion_12 | 9794.63 | -205.37 | buy /  / momentum_26 + reversion_12: prior completed bar target 50%; next bar open simulation |
| v1 | momentum_26 AND volume_26 | 9985.49 | -14.51 | sell /  / momentum_26 AND volume_26: prior completed bar target 0%; next bar open simulation |
| v1 | momentum_26 + volume_26 | 9776.93 | -223.07 | buy /  / momentum_26 + volume_26: prior completed bar target 50%; next bar open simulation |
| v1 | breakout_8 AND reversion_12 | 10000.00 | 0.00 | 대기 /  / 새 신호 대기 |
| v1 | breakout_8 + reversion_12 | 9643.94 | -356.06 | sell /  / breakout_8 + reversion_12: prior completed bar target 0%; next bar open simulation |
| v1 | breakout_8 AND volume_26 | 9851.05 | -148.95 | sell /  / breakout_8 AND volume_26: prior completed bar target 0%; next bar open simulation |
| v1 | breakout_8 + volume_26 | 9607.03 | -392.97 | sell /  / breakout_8 + volume_26: prior completed bar target 0%; next bar open simulation |
| v1 | reversion_12 AND volume_26 | 9815.22 | -184.78 | sell /  / reversion_12 AND volume_26: prior completed bar target 0%; next bar open simulation |
| v1 | reversion_12 + volume_26 | 9666.08 | -333.92 | sell /  / reversion_12 + volume_26: prior completed bar target 0%; next bar open simulation |
| v1 | ema_12_26 | 9866.65 | -133.35 | buy /  / EMA12 > EMA26; 조건 충족; EMA12=177.271, EMA26=177.221 |
| v1 | macd_12_26_9 | 9955.93 | -44.07 | buy /  / MACD > 신호선 그리고 MACD > 0; 조건 충족; MACD=0.0503325, signal9=-0.0213957 |
| v1 | rsi_14_recovery | 9927.64 | -72.36 | sell /  / 직전 RSI14 < 30, 현재 RSI14 >= 30 (한 봉 목표); 조건 미충족; RSI14=37.639, previous_RSI14=31.1023 |
| v1 | bollinger_20_reentry | 9852.90 | -147.10 | sell /  / 직전 종가 < 직전 하단밴드, 현재 하단밴드 <= 종가 <= SMA20 (한 봉 목표); 조건 미충족; close=175.55, lower20=175.189, SMA20=177.794, previous_lower20=175.528 |
| v1 | donchian_20 | 9739.57 | -260.43 | sell /  / 종가 > 현재 봉을 제외한 직전 20봉 최고가; 조건 미충족; close=176.61, prior_high20=177.952 |
| v1 | atr_14_breakout | 9826.13 | -173.87 | sell /  / 종가 > 직전 종가 + 직전 ATR14 그리고 종가 > EMA26; 조건 미충족; close=177.865, threshold=178.483, prior_ATR14=0.612834, EMA26=177.268 |
| v1 | session_vwap | 9851.29 | -148.71 | sell /  / 종가 > 뉴욕 거래일별 누적 전형가격 VWAP; 조건 미충족; close=177.28, session_VWAP=177.359, session_volume=2.74277e+06 |
| v1 | obv_20 | 9655.48 | -344.52 | sell /  / OBV > OBV의 SMA20 그리고 종가 > EMA26; 조건 미충족; OBV=2.29812e+07, OBV_SMA20=2.29985e+07, close=177.28, EMA26=177.348 |
| v1 | stochastic_14_3_recovery | 9721.31 | -278.69 | sell /  / 직전 %K14 < 20에서 %K14가 %D3 상향 돌파 (한 봉 목표); 조건 미충족; K14=29.2797, D3=21.8586, previous_K14=22.3575, previous_D3=16.0588 |
| v1 | mfi_14_recovery | 10000.00 | 0.00 | 대기 /  / 새 신호 대기 |
| v1 | adx_14_trend | 9999.47 | -0.53 | sell /  / Wilder ADX14 >= 25 그리고 +DI14 > -DI14; 조건 미충족; ADX14=23.8302, plus_DI14=25.6436, minus_DI14=22.6035 |
| v1 | aroon_25_trend | 9727.62 | -272.38 | buy /  / Aroon25 Up > 70 그리고 Down < 30 (동률이면 최신 극값); 조건 충족; Aroon_up=100, Aroon_down=4 |
| v1 | cci_20_momentum | 9599.29 | -400.71 | sell /  / CCI20 > 100 (전형가격·평균절대편차); 조건 미충족; CCI20=74.6634 |
| v1 | williams_14_recovery | 9665.88 | -334.12 | sell /  / 직전 Williams %R14 < -80, 현재 >= -80 (한 봉 목표); 조건 미충족; Williams_R14=-12.0205, previous_R14=-62.6593 |
| v1 | cmf_20_accumulation | 9950.87 | -49.13 | buy /  / Chaikin Money Flow20 > 0.1; 조건 충족; CMF20=0.210618, volume20=5.30029e+06 |
| v1 | chaikin_3_10 | 9761.08 | -238.92 | sell /  / ADL의 EMA3 - EMA10 > 0 그리고 종가 > EMA26; 조건 미충족; Chaikin3_10=16553.2, ADL=2.81181e+07, close=177.28, EMA26=177.348 |
| v1 | roc_10_momentum | 9940.60 | -59.40 | sell /  / 10봉 ROC > 1% 그리고 종가 > EMA26; 조건 미충족; ROC10_percent=0.782107, close=178.47, EMA26=176.891 |
| v1 | trix_15_trend | 9893.71 | -106.29 | sell /  / 15봉 삼중 EMA의 1봉 변화율 TRIX > 0 그리고 종가 > EMA26; 조건 미충족; TRIX15_percent=0.00535723, close=177.28, EMA26=177.348 |
| v1 | keltner_20_breakout | 9937.30 | -62.70 | sell /  / 종가 > EMA20 + 2 x Wilder ATR14; 조건 미충족; close=178.845, upper_Keltner=179.079, EMA20=177.884, ATR14=0.597175 |
| v1 | opening_range_30m | 10049.37 | 49.37 | sell /  / 뉴욕 09:30·09:45 두 완료 봉 최고가를 10:00 이후 종가가 돌파; 자료 부족·변동폭 또는 거래량 없음: 대기; close=179.01 |
| v2 | cash | 10000.00 | 0.00 | 대기 /  / 새 신호 대기 |
| v2 | buy_hold | 10369.42 | 369.42 | buy / partial / 직전 완료 봉 목표 비중 100%; 다음 봉 시가 가정 |
| v2 | trend_8_26 | 9952.19 | -47.81 | buy / partial / 직전 완료 봉 목표 비중 100%; 다음 봉 시가 가정 |
| v2 | momentum_26 | 10073.21 | 73.21 | buy / partial / 직전 완료 봉 목표 비중 100%; 다음 봉 시가 가정 |
| v2 | breakout_8 | 9038.47 | -961.53 | sell / filled / 직전 완료 봉 목표 비중 0%; 다음 봉 시가 가정 |
| v2 | reversion_12 | 9498.83 | -501.17 | sell / filled / 직전 완료 봉 목표 비중 0%; 다음 봉 시가 가정 |
| v2 | volume_26 | 9550.10 | -449.90 | sell / filled / 직전 완료 봉 목표 비중 0%; 다음 봉 시가 가정 |
| v2 | trend_8_26 AND momentum_26 | 9921.34 | -78.66 | buy / partial / 직전 완료 봉 목표 비중 100%; 다음 봉 시가 가정 |
| v2 | trend_8_26 + momentum_26 | 10012.64 | 12.64 | buy / partial / 직전 완료 봉 목표 비중 100%; 다음 봉 시가 가정 |
| v2 | trend_8_26 AND breakout_8 | 9160.13 | -839.87 | sell / filled / 직전 완료 봉 목표 비중 0%; 다음 봉 시가 가정 |
| v2 | trend_8_26 + breakout_8 | 9524.99 | -475.01 | buy / filled / 직전 완료 봉 목표 비중 50%; 다음 봉 시가 가정 |
| v2 | trend_8_26 AND reversion_12 | 9517.12 | -482.88 | sell / filled / 직전 완료 봉 목표 비중 0%; 다음 봉 시가 가정 |
| v2 | trend_8_26 + reversion_12 | 9722.88 | -277.12 | buy / filled / 직전 완료 봉 목표 비중 50%; 다음 봉 시가 가정 |
| v2 | trend_8_26 AND volume_26 | 9656.58 | -343.42 | sell / filled / 직전 완료 봉 목표 비중 0%; 다음 봉 시가 가정 |
| v2 | trend_8_26 + volume_26 | 9749.22 | -250.78 | buy / filled / 직전 완료 봉 목표 비중 50%; 다음 봉 시가 가정 |
| v2 | momentum_26 AND breakout_8 | 9269.79 | -730.21 | sell / filled / 직전 완료 봉 목표 비중 0%; 다음 봉 시가 가정 |
| v2 | momentum_26 + breakout_8 | 9542.57 | -457.43 | buy / filled / 직전 완료 봉 목표 비중 50%; 다음 봉 시가 가정 |
| v2 | momentum_26 AND reversion_12 | 9567.55 | -432.45 | sell / filled / 직전 완료 봉 목표 비중 0%; 다음 봉 시가 가정 |
| v2 | momentum_26 + reversion_12 | 9781.76 | -218.24 | buy / filled / 직전 완료 봉 목표 비중 50%; 다음 봉 시가 가정 |
| v2 | momentum_26 AND volume_26 | 9941.52 | -58.48 | sell / filled / 직전 완료 봉 목표 비중 0%; 다음 봉 시가 가정 |
| v2 | momentum_26 + volume_26 | 9828.69 | -171.31 | buy / filled / 직전 완료 봉 목표 비중 50%; 다음 봉 시가 가정 |
| v2 | breakout_8 AND reversion_12 | 10000.00 | 0.00 | 대기 /  / 새 신호 대기 |
| v2 | breakout_8 + reversion_12 | 9285.08 | -714.92 | sell / filled / 직전 완료 봉 목표 비중 0%; 다음 봉 시가 가정 |
| v2 | breakout_8 AND volume_26 | 9817.82 | -182.18 | sell / filled / 직전 완료 봉 목표 비중 0%; 다음 봉 시가 가정 |
| v2 | breakout_8 + volume_26 | 9310.00 | -690.00 | sell / filled / 직전 완료 봉 목표 비중 0%; 다음 봉 시가 가정 |
| v2 | reversion_12 AND volume_26 | 9760.17 | -239.83 | sell / filled / 직전 완료 봉 목표 비중 0%; 다음 봉 시가 가정 |
| v2 | reversion_12 + volume_26 | 9544.56 | -455.44 | sell / filled / 직전 완료 봉 목표 비중 0%; 다음 봉 시가 가정 |
| v2 | ema_12_26 | 9861.71 | -138.29 | buy / partial / EMA12 > EMA26; 조건 충족; EMA12=177.271, EMA26=177.221; 직전 완료 봉 목표를 다음 봉 시가에 모의 적용 |
| v2 | macd_12_26_9 | 9948.96 | -51.04 | buy / partial / MACD > 신호선 그리고 MACD > 0; 조건 충족; MACD=0.0503325, signal9=-0.0213957; 직전 완료 봉 목표를 다음 봉 시가에 모의 적용 |
| v2 | rsi_14_recovery | 9923.67 | -76.33 | sell / filled / 직전 RSI14 < 30, 현재 RSI14 >= 30 (한 봉 목표); 조건 미충족; RSI14=37.639, previous_RSI14=31.1023; 직전 완료 봉 목표를 다음 봉 시가에 모의 적용 |
| v2 | bollinger_20_reentry | 9848.96 | -151.04 | sell / filled / 직전 종가 < 직전 하단밴드, 현재 하단밴드 <= 종가 <= SMA20 (한 봉 목표); 조건 미충족; close=175.55, lower20=175.189, SMA20=177.794, previous_lower20=175.528; 직전 완료 봉 목표를 다음 봉 시가에 모의 적용 |
| v2 | donchian_20 | 9729.83 | -270.17 | sell / filled / 종가 > 현재 봉을 제외한 직전 20봉 최고가; 조건 미충족; close=176.61, prior_high20=177.952; 직전 완료 봉 목표를 다음 봉 시가에 모의 적용 |
| v2 | atr_14_breakout | 9818.27 | -181.73 | sell / filled / 종가 > 직전 종가 + 직전 ATR14 그리고 종가 > EMA26; 조건 미충족; close=177.865, threshold=178.483, prior_ATR14=0.612834, EMA26=177.268; 직전 완료 봉 목표를 다음 봉 시가에 모의 적용 |
| v2 | session_vwap | 9841.44 | -158.56 | sell / filled / 종가 > 뉴욕 거래일별 누적 전형가격 VWAP; 조건 미충족; close=177.28, session_VWAP=177.359, session_volume=2.74277e+06; 직전 완료 봉 목표를 다음 봉 시가에 모의 적용 |
| v2 | obv_20 | 9640.04 | -359.96 | sell / filled / OBV > OBV의 SMA20 그리고 종가 > EMA26; 조건 미충족; OBV=2.29812e+07, OBV_SMA20=2.29985e+07, close=177.28, EMA26=177.348; 직전 완료 봉 목표를 다음 봉 시가에 모의 적용 |
| v2 | stochastic_14_3_recovery | 9711.59 | -288.41 | sell / filled / 직전 %K14 < 20에서 %K14가 %D3 상향 돌파 (한 봉 목표); 조건 미충족; K14=29.2797, D3=21.8586, previous_K14=22.3575, previous_D3=16.0588; 직전 완료 봉 목표를 다음 봉 시가에 모의 적용 |
| v2 | mfi_14_recovery | 10000.00 | 0.00 | 대기 /  / 새 신호 대기 |
| v2 | adx_14_trend | 9993.47 | -6.53 | sell / filled / Wilder ADX14 >= 25 그리고 +DI14 > -DI14; 조건 미충족; ADX14=23.8302, plus_DI14=25.6436, minus_DI14=22.6035; 직전 완료 봉 목표를 다음 봉 시가에 모의 적용 |
| v2 | aroon_25_trend | 9722.76 | -277.24 | buy / partial / Aroon25 Up > 70 그리고 Down < 30 (동률이면 최신 극값); 조건 충족; Aroon_up=100, Aroon_down=4; 직전 완료 봉 목표를 다음 봉 시가에 모의 적용 |
| v2 | cci_20_momentum | 9582.02 | -417.98 | sell / filled / CCI20 > 100 (전형가격·평균절대편차); 조건 미충족; CCI20=74.6634; 직전 완료 봉 목표를 다음 봉 시가에 모의 적용 |
| v2 | williams_14_recovery | 9654.28 | -345.72 | sell / filled / 직전 Williams %R14 < -80, 현재 >= -80 (한 봉 목표); 조건 미충족; Williams_R14=-12.0205, previous_R14=-62.6593; 직전 완료 봉 목표를 다음 봉 시가에 모의 적용 |
| v2 | cmf_20_accumulation | 9945.90 | -54.10 | buy / partial / Chaikin Money Flow20 > 0.1; 조건 충족; CMF20=0.210618, volume20=5.30029e+06; 직전 완료 봉 목표를 다음 봉 시가에 모의 적용 |
| v2 | chaikin_3_10 | 9749.38 | -250.62 | sell / filled / ADL의 EMA3 - EMA10 > 0 그리고 종가 > EMA26; 조건 미충족; Chaikin3_10=16553.2, ADL=2.81181e+07, close=177.28, EMA26=177.348; 직전 완료 봉 목표를 다음 봉 시가에 모의 적용 |
| v2 | roc_10_momentum | 9934.64 | -65.36 | sell / filled / 10봉 ROC > 1% 그리고 종가 > EMA26; 조건 미충족; ROC10_percent=0.782107, close=178.47, EMA26=176.891; 직전 완료 봉 목표를 다음 봉 시가에 모의 적용 |
| v2 | trix_15_trend | 9885.79 | -114.21 | sell / filled / 15봉 삼중 EMA의 1봉 변화율 TRIX > 0 그리고 종가 > EMA26; 조건 미충족; TRIX15_percent=0.00535723, close=177.28, EMA26=177.348; 직전 완료 봉 목표를 다음 봉 시가에 모의 적용 |
| v2 | keltner_20_breakout | 9931.34 | -68.66 | sell / filled / 종가 > EMA20 + 2 x Wilder ATR14; 조건 미충족; close=178.845, upper_Keltner=179.079, EMA20=177.884, ATR14=0.597175; 직전 완료 봉 목표를 다음 봉 시가에 모의 적용 |
| v2 | opening_range_30m | 10047.36 | 47.36 | sell / filled / 뉴욕 09:30·09:45 두 완료 봉 최고가를 10:00 이후 종가가 돌파; 자료 부족·변동폭 또는 거래량 없음: 대기; close=179.01; 직전 완료 봉 목표를 다음 봉 시가에 모의 적용 |

### 같은 기간의 비용·노출 비교 (사후 연구)

| 전략 | 비용 전 | 비용 후 | 100% 보유 | 같은 평균 노출 보유 | 평균 노출 |
|---|---:|---:|---:|---:|---:|
| cash | 0.00% | 0.00% | 8.04% | 0.00% | 0.00% |
| buy_hold | 8.49% | 8.04% | 8.04% | 8.04% | 100.00% |
| trend_8_26 | 0.78% | -4.17% | 8.04% | 5.43% | 68.34% |
| momentum_26 | 1.32% | -6.06% | 8.04% | 5.62% | 70.71% |
| breakout_8 | -1.21% | -19.24% | 8.04% | 2.08% | 26.65% |
| reversion_12 | 3.37% | -6.54% | 8.04% | 1.69% | 21.64% |
| volume_26 | 1.74% | -6.06% | 8.04% | 0.45% | 5.80% |
| trend_8_26 AND momentum_26 | -0.63% | -6.31% | 8.04% | 4.72% | 59.63% |
| trend_8_26 + momentum_26 | 1.06% | -4.92% | 8.04% | 5.52% | 69.53% |
| trend_8_26 AND breakout_8 | -1.05% | -15.64% | 8.04% | 1.58% | 20.32% |
| trend_8_26 + breakout_8 | -0.19% | -11.64% | 8.04% | 3.74% | 47.50% |
| trend_8_26 AND reversion_12 | -1.31% | -7.34% | 8.04% | 0.82% | 10.55% |
| trend_8_26 + reversion_12 | 2.09% | -5.16% | 8.04% | 3.54% | 44.99% |
| trend_8_26 AND volume_26 | 0.91% | -4.05% | 8.04% | 0.29% | 3.69% |
| trend_8_26 + volume_26 | 1.28% | -4.92% | 8.04% | 2.91% | 37.07% |
| momentum_26 AND breakout_8 | -1.02% | -17.03% | 8.04% | 1.79% | 22.96% |
| momentum_26 + breakout_8 | 0.07% | -12.88% | 8.04% | 3.84% | 48.69% |
| momentum_26 AND reversion_12 | -0.44% | -6.91% | 8.04% | 0.80% | 10.29% |
| momentum_26 + reversion_12 | 2.37% | -5.11% | 8.04% | 3.64% | 46.18% |
| momentum_26 AND volume_26 | 2.15% | -1.64% | 8.04% | 0.18% | 2.37% |
| momentum_26 + volume_26 | 1.55% | -5.07% | 8.04% | 3.00% | 38.26% |
| breakout_8 AND reversion_12 | 0.00% | 0.00% | 8.04% | 0.00% | 0.00% |
| breakout_8 + reversion_12 | 1.07% | -12.76% | 8.04% | 1.89% | 24.15% |
| breakout_8 AND volume_26 | -0.10% | -2.18% | 8.04% | 0.10% | 1.32% |
| breakout_8 + volume_26 | 0.27% | -12.17% | 8.04% | 1.26% | 16.24% |
| reversion_12 AND volume_26 | 0.43% | -2.89% | 8.04% | 0.18% | 2.37% |
| reversion_12 + volume_26 | 2.57% | -5.51% | 8.04% | 1.07% | 13.73% |
| ema_12_26 | 0.21% | -3.51% | 8.04% | 6.16% | 77.31% |
| macd_12_26_9 | -0.68% | -6.74% | 8.04% | 3.26% | 41.42% |
| rsi_14_recovery | -0.08% | -1.33% | 8.04% | 0.06% | 0.79% |
| bollinger_20_reentry | -1.07% | -3.94% | 8.04% | 0.14% | 1.85% |
| donchian_20 | -1.73% | -10.03% | 8.04% | 0.70% | 8.97% |
| atr_14_breakout | 0.55% | -7.55% | 8.04% | 0.43% | 5.54% |
| session_vwap | 0.51% | -9.89% | 8.04% | 5.23% | 65.96% |
| obv_20 | 1.20% | -8.50% | 8.04% | 3.83% | 48.55% |
| stochastic_14_3_recovery | 0.79% | -8.49% | 8.04% | 0.47% | 6.07% |
| mfi_14_recovery | -0.31% | -1.97% | 8.04% | 0.08% | 1.06% |
| adx_14_trend | 3.21% | 0.22% | 8.04% | 3.11% | 39.58% |
| aroon_25_trend | -3.56% | -10.20% | 8.04% | 2.65% | 33.77% |
| cci_20_momentum | 2.18% | -6.84% | 8.04% | 2.14% | 27.44% |
| williams_14_recovery | -0.38% | -6.85% | 8.04% | 0.33% | 4.22% |
| cmf_20_accumulation | 1.12% | -5.45% | 8.04% | 3.97% | 50.40% |
| chaikin_3_10 | 0.80% | -8.10% | 8.04% | 4.72% | 59.63% |
| roc_10_momentum | 0.44% | -4.90% | 8.04% | 0.90% | 11.61% |
| trix_15_trend | 0.22% | -6.29% | 8.04% | 5.08% | 64.12% |
| keltner_20_breakout | 0.54% | -5.20% | 8.04% | 1.23% | 15.83% |
| opening_range_30m | -0.41% | -9.20% | 8.04% | 2.44% | 31.13% |

동일 구간·초기 자금, 종료 시 청산 비용 포함. 노출 맞춤은 사후 설명용이며 v2 실제 계좌 성과가 아닙니다.
[낙폭 분해·비용 영향·전체 구간](XOM/comparison.json)

[v1 전체 기록](XOM/accounts.json) · [v2 전체 기록](XOM/accounts-v2.json)

## JNJ 계좌

| 모델 | 전략 | 평가액 USD | 손익 USD | 최근 매매·이유 |
|---|---|---:|---:|---|
| v1 | cash | 10000.00 | 0.00 | 대기 /  / 새 신호 대기 |
| v1 | buy_hold | 9959.72 | -40.28 | buy /  / buy_hold: prior completed bar target 100%; next bar open simulation |
| v1 | trend_8_26 | 9989.00 | -11.00 | sell /  / trend_8_26: prior completed bar target 0%; next bar open simulation |
| v1 | momentum_26 | 9722.10 | -277.90 | sell /  / momentum_26: prior completed bar target 0%; next bar open simulation |
| v1 | breakout_8 | 9466.25 | -533.75 | sell /  / breakout_8: prior completed bar target 0%; next bar open simulation |
| v1 | reversion_12 | 9747.78 | -252.22 | sell /  / reversion_12: prior completed bar target 0%; next bar open simulation |
| v1 | volume_26 | 9902.45 | -97.55 | sell /  / volume_26: prior completed bar target 0%; next bar open simulation |
| v1 | trend_8_26 AND momentum_26 | 9813.05 | -186.95 | sell /  / trend_8_26 AND momentum_26: prior completed bar target 0%; next bar open simulation |
| v1 | trend_8_26 + momentum_26 | 9854.96 | -145.04 | sell /  / trend_8_26 + momentum_26: prior completed bar target 0%; next bar open simulation |
| v1 | trend_8_26 AND breakout_8 | 9765.55 | -234.45 | sell /  / trend_8_26 AND breakout_8: prior completed bar target 0%; next bar open simulation |
| v1 | trend_8_26 + breakout_8 | 9743.89 | -256.11 | sell /  / trend_8_26 + breakout_8: prior completed bar target 0%; next bar open simulation |
| v1 | trend_8_26 AND reversion_12 | 9930.57 | -69.43 | sell /  / trend_8_26 AND reversion_12: prior completed bar target 0%; next bar open simulation |
| v1 | trend_8_26 + reversion_12 | 9867.78 | -132.22 | sell /  / trend_8_26 + reversion_12: prior completed bar target 0%; next bar open simulation |
| v1 | trend_8_26 AND volume_26 | 9995.12 | -4.88 | sell /  / trend_8_26 AND volume_26: prior completed bar target 0%; next bar open simulation |
| v1 | trend_8_26 + volume_26 | 9945.88 | -54.12 | sell /  / trend_8_26 + volume_26: prior completed bar target 0%; next bar open simulation |
| v1 | momentum_26 AND breakout_8 | 9784.22 | -215.78 | sell /  / momentum_26 AND breakout_8: prior completed bar target 0%; next bar open simulation |
| v1 | momentum_26 + breakout_8 | 9593.22 | -406.78 | sell /  / momentum_26 + breakout_8: prior completed bar target 0%; next bar open simulation |
| v1 | momentum_26 AND reversion_12 | 9938.52 | -61.48 | sell /  / momentum_26 AND reversion_12: prior completed bar target 0%; next bar open simulation |
| v1 | momentum_26 + reversion_12 | 9773.79 | -226.21 | sell /  / momentum_26 + reversion_12: prior completed bar target 0%; next bar open simulation |
| v1 | momentum_26 AND volume_26 | 10000.00 | 0.00 | 대기 /  / 새 신호 대기 |
| v1 | momentum_26 + volume_26 | 9851.20 | -148.80 | sell /  / momentum_26 + volume_26: prior completed bar target 0%; next bar open simulation |
| v1 | breakout_8 AND reversion_12 | 10000.00 | 0.00 | 대기 /  / 새 신호 대기 |
| v1 | breakout_8 + reversion_12 | 9605.72 | -394.28 | sell /  / breakout_8 + reversion_12: prior completed bar target 0%; next bar open simulation |
| v1 | breakout_8 AND volume_26 | 10000.00 | 0.00 | 대기 /  / 새 신호 대기 |
| v1 | breakout_8 + volume_26 | 9701.23 | -298.77 | sell /  / breakout_8 + volume_26: prior completed bar target 0%; next bar open simulation |
| v1 | reversion_12 AND volume_26 | 9933.02 | -66.98 | sell /  / reversion_12 AND volume_26: prior completed bar target 0%; next bar open simulation |
| v1 | reversion_12 + volume_26 | 9844.46 | -155.54 | sell /  / reversion_12 + volume_26: prior completed bar target 0%; next bar open simulation |
| v1 | ema_12_26 | 9770.13 | -229.87 | sell /  / EMA12 > EMA26; 조건 미충족; EMA12=257.771, EMA26=257.934 |
| v1 | macd_12_26_9 | 9887.47 | -112.53 | sell /  / MACD > 신호선 그리고 MACD > 0; 조건 미충족; MACD=1.30676, signal9=1.31668 |
| v1 | rsi_14_recovery | 9923.04 | -76.96 | sell /  / 직전 RSI14 < 30, 현재 RSI14 >= 30 (한 봉 목표); 조건 미충족; RSI14=40.3665, previous_RSI14=36.2025 |
| v1 | bollinger_20_reentry | 9816.96 | -183.04 | sell /  / 직전 종가 < 직전 하단밴드, 현재 하단밴드 <= 종가 <= SMA20 (한 봉 목표); 조건 미충족; close=255.05, lower20=254.819, SMA20=258.099, previous_lower20=255.312 |
| v1 | donchian_20 | 9921.02 | -78.98 | sell /  / 종가 > 현재 봉을 제외한 직전 20봉 최고가; 조건 미충족; close=258.68, prior_high20=260.425 |
| v1 | atr_14_breakout | 9701.58 | -298.42 | sell /  / 종가 > 직전 종가 + 직전 ATR14 그리고 종가 > EMA26; 조건 미충족; close=259.42, threshold=260.032, prior_ATR14=0.777474, EMA26=258.478 |
| v1 | session_vwap | 9675.82 | -324.18 | sell /  / 종가 > 뉴욕 거래일별 누적 전형가격 VWAP; 조건 미충족; close=256.41, session_VWAP=256.783, session_volume=393635 |
| v1 | obv_20 | 9506.00 | -494.00 | sell /  / OBV > OBV의 SMA20 그리고 종가 > EMA26; 조건 미충족; OBV=1.05978e+07, OBV_SMA20=1.06874e+07, close=256.41, EMA26=258.325 |
| v1 | stochastic_14_3_recovery | 9624.87 | -375.13 | buy /  / 직전 %K14 < 20에서 %K14가 %D3 상향 돌파 (한 봉 목표); 조건 충족; K14=14.3541, D3=8.37258, previous_K14=6.77968, previous_D3=8.72126 |
| v1 | mfi_14_recovery | 10000.00 | 0.00 | 대기 /  / 새 신호 대기 |
| v1 | adx_14_trend | 9681.33 | -318.67 | sell /  / Wilder ADX14 >= 25 그리고 +DI14 > -DI14; 조건 미충족; ADX14=33.0847, plus_DI14=22.751, minus_DI14=33.7106 |
| v1 | aroon_25_trend | 9899.46 | -100.54 | sell /  / Aroon25 Up > 70 그리고 Down < 30 (동률이면 최신 극값); 조건 미충족; Aroon_up=68, Aroon_down=44 |
| v1 | cci_20_momentum | 9818.66 | -181.34 | sell /  / CCI20 > 100 (전형가격·평균절대편차); 조건 미충족; CCI20=95.1073 |
| v1 | williams_14_recovery | 9737.89 | -262.11 | sell /  / 직전 Williams %R14 < -80, 현재 >= -80 (한 봉 목표); 조건 미충족; Williams_R14=-27.6062, previous_R14=-37.7293 |
| v1 | cmf_20_accumulation | 10060.68 | 60.68 | sell /  / Chaikin Money Flow20 > 0.1; 조건 미충족; CMF20=-0.0883438, volume20=4.47769e+06 |
| v1 | chaikin_3_10 | 9772.24 | -227.76 | sell /  / ADL의 EMA3 - EMA10 > 0 그리고 종가 > EMA26; 조건 미충족; Chaikin3_10=-71247.4, ADL=5.61269e+06, close=256.41, EMA26=258.325 |
| v1 | roc_10_momentum | 9691.76 | -308.24 | sell /  / 10봉 ROC > 1% 그리고 종가 > EMA26; 조건 미충족; ROC10_percent=-0.503419, close=258.91, EMA26=257.09 |
| v1 | trix_15_trend | 9665.05 | -334.95 | sell /  / 15봉 삼중 EMA의 1봉 변화율 TRIX > 0 그리고 종가 > EMA26; 조건 미충족; TRIX15_percent=0.0421187, close=256.41, EMA26=258.325 |
| v1 | keltner_20_breakout | 9916.04 | -83.96 | sell /  / 종가 > EMA20 + 2 x Wilder ATR14; 조건 미충족; close=258.91, upper_Keltner=259.564, EMA20=257.603, ATR14=0.980686 |
| v1 | opening_range_30m | 10000.00 | 0.00 | 대기 /  / 새 신호 대기 |
| v2 | cash | 10000.00 | 0.00 | 대기 /  / 새 신호 대기 |
| v2 | buy_hold | 9727.27 | -272.73 | 중단: 손실 한도 / buy / partial / 직전 완료 봉 목표 비중 100%; 다음 봉 시가 가정 |
| v2 | trend_8_26 | 9727.27 | -272.73 | 중단: 손실 한도 / buy / partial / 직전 완료 봉 목표 비중 100%; 다음 봉 시가 가정 |
| v2 | momentum_26 | 9727.27 | -272.73 | 중단: 손실 한도 / buy / partial / 직전 완료 봉 목표 비중 100%; 다음 봉 시가 가정 |
| v2 | breakout_8 | 9343.39 | -656.61 | 중단: 손실 한도 / sell / filled / 직전 완료 봉 목표 비중 0%; 다음 봉 시가 가정 |
| v2 | reversion_12 | 9434.41 | -565.59 | sell / filled / 직전 완료 봉 목표 비중 0%; 다음 봉 시가 가정 |
| v2 | volume_26 | 9686.16 | -313.84 | sell / filled / 직전 완료 봉 목표 비중 0%; 다음 봉 시가 가정 |
| v2 | trend_8_26 AND momentum_26 | 9727.27 | -272.73 | 중단: 손실 한도 / buy / partial / 직전 완료 봉 목표 비중 100%; 다음 봉 시가 가정 |
| v2 | trend_8_26 + momentum_26 | 9727.27 | -272.73 | 중단: 손실 한도 / buy / partial / 직전 완료 봉 목표 비중 100%; 다음 봉 시가 가정 |
| v2 | trend_8_26 AND breakout_8 | 9419.39 | -580.61 | 중단: 손실 한도 / sell / filled / 직전 완료 봉 목표 비중 0%; 다음 봉 시가 가정 |
| v2 | trend_8_26 + breakout_8 | 9314.45 | -685.55 | sell / filled / 직전 완료 봉 목표 비중 0%; 다음 봉 시가 가정 |
| v2 | trend_8_26 AND reversion_12 | 9900.89 | -99.11 | sell / filled / 직전 완료 봉 목표 비중 0%; 다음 봉 시가 가정 |
| v2 | trend_8_26 + reversion_12 | 9732.92 | -267.08 | 중단: 손실 한도 / sell / filled / 직전 완료 봉 목표 비중 0%; 다음 봉 시가 가정 |
| v2 | trend_8_26 AND volume_26 | 9861.95 | -138.05 | sell / filled / 직전 완료 봉 목표 비중 0%; 다음 봉 시가 가정 |
| v2 | trend_8_26 + volume_26 | 9836.74 | -163.26 | 중단: 손실 한도 / buy / filled / 직전 완료 봉 목표 비중 50%; 다음 봉 시가 가정 |
| v2 | momentum_26 AND breakout_8 | 9385.94 | -614.06 | sell / filled / 직전 완료 봉 목표 비중 0%; 다음 봉 시가 가정 |
| v2 | momentum_26 + breakout_8 | 9160.89 | -839.11 | sell / filled / 직전 완료 봉 목표 비중 0%; 다음 봉 시가 가정 |
| v2 | momentum_26 AND reversion_12 | 9871.83 | -128.17 | sell / filled / 직전 완료 봉 목표 비중 0%; 다음 봉 시가 가정 |
| v2 | momentum_26 + reversion_12 | 9732.92 | -267.08 | 중단: 손실 한도 / sell / filled / 직전 완료 봉 목표 비중 0%; 다음 봉 시가 가정 |
| v2 | momentum_26 AND volume_26 | 9920.93 | -79.07 | sell / filled / 직전 완료 봉 목표 비중 0%; 다음 봉 시가 가정 |
| v2 | momentum_26 + volume_26 | 9836.74 | -163.26 | 중단: 손실 한도 / buy / filled / 직전 완료 봉 목표 비중 50%; 다음 봉 시가 가정 |
| v2 | breakout_8 AND reversion_12 | 10000.00 | 0.00 | 대기 /  / 새 신호 대기 |
| v2 | breakout_8 + reversion_12 | 9188.57 | -811.43 | sell / filled / 직전 완료 봉 목표 비중 0%; 다음 봉 시가 가정 |
| v2 | breakout_8 AND volume_26 | 9814.17 | -185.83 | sell / filled / 직전 완료 봉 목표 비중 0%; 다음 봉 시가 가정 |
| v2 | breakout_8 + volume_26 | 9310.48 | -689.52 | sell / filled / 직전 완료 봉 목표 비중 0%; 다음 봉 시가 가정 |
| v2 | reversion_12 AND volume_26 | 9816.09 | -183.91 | sell / filled / 직전 완료 봉 목표 비중 0%; 다음 봉 시가 가정 |
| v2 | reversion_12 + volume_26 | 9599.90 | -400.10 | sell / filled / 직전 완료 봉 목표 비중 0%; 다음 봉 시가 가정 |
| v2 | ema_12_26 | 9764.26 | -235.74 | sell / filled / EMA12 > EMA26; 조건 미충족; EMA12=257.771, EMA26=257.934; 직전 완료 봉 목표를 다음 봉 시가에 모의 적용 |
| v2 | macd_12_26_9 | 9881.54 | -118.46 | sell / filled / MACD > 신호선 그리고 MACD > 0; 조건 미충족; MACD=1.30676, signal9=1.31668; 직전 완료 봉 목표를 다음 봉 시가에 모의 적용 |
| v2 | rsi_14_recovery | 9919.07 | -80.93 | sell / filled / 직전 RSI14 < 30, 현재 RSI14 >= 30 (한 봉 목표); 조건 미충족; RSI14=40.3665, previous_RSI14=36.2025; 직전 완료 봉 목표를 다음 봉 시가에 모의 적용 |
| v2 | bollinger_20_reentry | 9811.07 | -188.93 | sell / filled / 직전 종가 < 직전 하단밴드, 현재 하단밴드 <= 종가 <= SMA20 (한 봉 목표); 조건 미충족; close=255.05, lower20=254.819, SMA20=258.099, previous_lower20=255.312; 직전 완료 봉 목표를 다음 봉 시가에 모의 적용 |
| v2 | donchian_20 | 9919.03 | -80.97 | sell / filled / 종가 > 현재 봉을 제외한 직전 20봉 최고가; 조건 미충족; close=258.68, prior_high20=260.425; 직전 완료 봉 목표를 다음 봉 시가에 모의 적용 |
| v2 | atr_14_breakout | 9693.82 | -306.18 | sell / filled / 종가 > 직전 종가 + 직전 ATR14 그리고 종가 > EMA26; 조건 미충족; close=259.42, threshold=260.032, prior_ATR14=0.777474, EMA26=258.478; 직전 완료 봉 목표를 다음 봉 시가에 모의 적용 |
| v2 | session_vwap | 9658.42 | -341.58 | sell / filled / 종가 > 뉴욕 거래일별 누적 전형가격 VWAP; 조건 미충족; close=256.41, session_VWAP=256.783, session_volume=393635; 직전 완료 봉 목표를 다음 봉 시가에 모의 적용 |
| v2 | obv_20 | 9488.91 | -511.09 | sell / filled / OBV > OBV의 SMA20 그리고 종가 > EMA26; 조건 미충족; OBV=1.05978e+07, OBV_SMA20=1.06874e+07, close=256.41, EMA26=258.325; 직전 완료 봉 목표를 다음 봉 시가에 모의 적용 |
| v2 | stochastic_14_3_recovery | 9612.37 | -387.63 | buy / partial / 직전 %K14 < 20에서 %K14가 %D3 상향 돌파 (한 봉 목표); 조건 충족; K14=14.3541, D3=8.37258, previous_K14=6.77968, previous_D3=8.72126; 직전 완료 봉 목표를 다음 봉 시가에 모의 적용 |
| v2 | mfi_14_recovery | 10000.00 | 0.00 | 대기 /  / 새 신호 대기 |
| v2 | adx_14_trend | 9673.58 | -326.42 | sell / filled / Wilder ADX14 >= 25 그리고 +DI14 > -DI14; 조건 미충족; ADX14=33.0847, plus_DI14=22.751, minus_DI14=33.7106; 직전 완료 봉 목표를 다음 봉 시가에 모의 적용 |
| v2 | aroon_25_trend | 9895.50 | -104.50 | sell / filled / Aroon25 Up > 70 그리고 Down < 30 (동률이면 최신 극값); 조건 미충족; Aroon_up=68, Aroon_down=44; 직전 완료 봉 목표를 다음 봉 시가에 모의 적용 |
| v2 | cci_20_momentum | 9812.77 | -187.23 | sell / filled / CCI20 > 100 (전형가격·평균절대편차); 조건 미충족; CCI20=95.1073; 직전 완료 봉 목표를 다음 봉 시가에 모의 적용 |
| v2 | williams_14_recovery | 9730.10 | -269.90 | sell / filled / 직전 Williams %R14 < -80, 현재 >= -80 (한 봉 목표); 조건 미충족; Williams_R14=-27.6062, previous_R14=-37.7293; 직전 완료 봉 목표를 다음 봉 시가에 모의 적용 |
| v2 | cmf_20_accumulation | 10056.66 | 56.66 | sell / filled / Chaikin Money Flow20 > 0.1; 조건 미충족; CMF20=-0.0883438, volume20=4.47769e+06; 직전 완료 봉 목표를 다음 봉 시가에 모의 적용 |
| v2 | chaikin_3_10 | 9764.42 | -235.58 | sell / filled / ADL의 EMA3 - EMA10 > 0 그리고 종가 > EMA26; 조건 미충족; Chaikin3_10=-71247.4, ADL=5.61269e+06, close=256.41, EMA26=258.325; 직전 완료 봉 목표를 다음 봉 시가에 모의 적용 |
| v2 | roc_10_momentum | 9684.01 | -315.99 | sell / filled / 10봉 ROC > 1% 그리고 종가 > EMA26; 조건 미충족; ROC10_percent=-0.503419, close=258.91, EMA26=257.09; 직전 완료 봉 목표를 다음 봉 시가에 모의 적용 |
| v2 | trix_15_trend | 9659.25 | -340.75 | sell / filled / 15봉 삼중 EMA의 1봉 변화율 TRIX > 0 그리고 종가 > EMA26; 조건 미충족; TRIX15_percent=0.0421187, close=256.41, EMA26=258.325; 직전 완료 봉 목표를 다음 봉 시가에 모의 적용 |
| v2 | keltner_20_breakout | 9914.05 | -85.95 | sell / filled / 종가 > EMA20 + 2 x Wilder ATR14; 조건 미충족; close=258.91, upper_Keltner=259.564, EMA20=257.603, ATR14=0.980686; 직전 완료 봉 목표를 다음 봉 시가에 모의 적용 |
| v2 | opening_range_30m | 10000.00 | 0.00 | 대기 /  / 새 신호 대기 |

### 같은 기간의 비용·노출 비교 (사후 연구)

| 전략 | 비용 전 | 비용 후 | 100% 보유 | 같은 평균 노출 보유 | 평균 노출 |
|---|---:|---:|---:|---:|---:|
| cash | 0.00% | 0.00% | -4.65% | -0.00% | 0.00% |
| buy_hold | -4.25% | -4.65% | -4.65% | -4.65% | 100.00% |
| trend_8_26 | 2.60% | 0.47% | -4.65% | -2.28% | 48.02% |
| momentum_26 | -0.86% | -3.74% | -4.65% | -2.21% | 46.44% |
| breakout_8 | -0.94% | -17.66% | -4.65% | -0.96% | 20.05% |
| reversion_12 | -6.87% | -15.09% | -4.65% | -1.53% | 31.93% |
| volume_26 | -0.49% | -7.35% | -4.65% | -0.32% | 6.60% |
| trend_8_26 AND momentum_26 | 0.79% | -1.72% | -4.65% | -1.95% | 40.90% |
| trend_8_26 + momentum_26 | 0.86% | -1.65% | -4.65% | -2.24% | 47.23% |
| trend_8_26 AND breakout_8 | 0.14% | -11.71% | -4.65% | -0.66% | 13.72% |
| trend_8_26 + breakout_8 | 0.84% | -8.83% | -4.65% | -1.63% | 34.04% |
| trend_8_26 AND reversion_12 | 1.37% | -1.98% | -4.65% | -0.28% | 5.80% |
| trend_8_26 + reversion_12 | -2.21% | -7.43% | -4.65% | -1.90% | 39.98% |
| trend_8_26 AND volume_26 | 1.42% | -1.10% | -4.65% | -0.08% | 1.58% |
| trend_8_26 + volume_26 | 1.08% | -3.30% | -4.65% | -1.31% | 27.31% |
| momentum_26 AND breakout_8 | 1.00% | -9.83% | -4.65% | -0.62% | 12.93% |
| momentum_26 + breakout_8 | -0.88% | -10.76% | -4.65% | -1.59% | 33.25% |
| momentum_26 AND reversion_12 | -0.27% | -3.16% | -4.65% | -0.31% | 6.33% |
| momentum_26 + reversion_12 | -3.88% | -9.01% | -4.65% | -1.87% | 39.19% |
| momentum_26 AND volume_26 | 0.14% | -0.70% | -4.65% | -0.03% | 0.53% |
| momentum_26 + volume_26 | -0.64% | -4.55% | -4.65% | -1.27% | 26.52% |
| breakout_8 AND reversion_12 | 0.00% | 0.00% | -4.65% | -0.00% | 0.00% |
| breakout_8 + reversion_12 | -3.93% | -16.03% | -4.65% | -1.25% | 26.00% |
| breakout_8 AND volume_26 | -0.46% | -1.29% | -4.65% | -0.03% | 0.53% |
| breakout_8 + volume_26 | -0.71% | -11.73% | -4.65% | -0.64% | 13.33% |
| reversion_12 AND volume_26 | -1.86% | -5.10% | -4.65% | -0.15% | 3.17% |
| reversion_12 + volume_26 | -3.72% | -10.74% | -4.65% | -0.93% | 19.27% |
| ema_12_26 | -1.05% | -3.51% | -4.65% | -2.23% | 46.97% |
| macd_12_26_9 | 5.83% | 2.76% | -4.65% | -1.41% | 29.55% |
| rsi_14_recovery | -1.35% | -6.20% | -4.65% | -0.15% | 3.17% |
| bollinger_20_reentry | -1.34% | -6.19% | -4.65% | -0.15% | 3.17% |
| donchian_20 | 0.68% | -6.26% | -4.65% | -0.32% | 6.60% |
| atr_14_breakout | 0.24% | -5.88% | -4.65% | -0.23% | 4.75% |
| session_vwap | 3.16% | -5.15% | -4.65% | -2.29% | 48.28% |
| obv_20 | -5.78% | -15.17% | -4.65% | -1.70% | 35.62% |
| stochastic_14_3_recovery | -1.35% | -14.47% | -4.65% | -0.43% | 8.97% |
| mfi_14_recovery | 0.33% | -0.93% | -4.65% | -0.04% | 0.79% |
| adx_14_trend | -3.61% | -8.35% | -4.65% | -1.76% | 36.94% |
| aroon_25_trend | 3.28% | -0.55% | -4.65% | -1.44% | 30.08% |
| cci_20_momentum | 0.58% | -5.17% | -4.65% | -0.95% | 19.79% |
| williams_14_recovery | -2.49% | -9.97% | -4.65% | -0.24% | 5.01% |
| cmf_20_accumulation | 4.00% | -0.27% | -4.65% | -1.66% | 34.83% |
| chaikin_3_10 | -3.43% | -8.18% | -4.65% | -1.80% | 37.73% |
| roc_10_momentum | -2.79% | -9.49% | -4.65% | -0.85% | 17.68% |
| trix_15_trend | -1.61% | -4.06% | -4.65% | -1.71% | 35.88% |
| keltner_20_breakout | 0.20% | -3.52% | -4.65% | -0.57% | 11.87% |
| opening_range_30m | 0.79% | -2.95% | -4.65% | -1.25% | 26.12% |

동일 구간·초기 자금, 종료 시 청산 비용 포함. 노출 맞춤은 사후 설명용이며 v2 실제 계좌 성과가 아닙니다.
[낙폭 분해·비용 영향·전체 구간](JNJ/comparison.json)

[v1 전체 기록](JNJ/accounts.json) · [v2 전체 기록](JNJ/accounts-v2.json)

## CAT 계좌

| 모델 | 전략 | 평가액 USD | 손익 USD | 최근 매매·이유 |
|---|---|---:|---:|---|
| v1 | cash | 10000.00 | 0.00 | 대기 /  / 새 신호 대기 |
| v1 | buy_hold | 9988.46 | -11.54 | buy /  / buy_hold: prior completed bar target 100%; next bar open simulation |
| v1 | trend_8_26 | 9910.89 | -89.11 | buy /  / trend_8_26: prior completed bar target 100%; next bar open simulation |
| v1 | momentum_26 | 9621.00 | -379.00 | buy /  / momentum_26: prior completed bar target 100%; next bar open simulation |
| v1 | breakout_8 | 9566.85 | -433.15 | sell /  / breakout_8: prior completed bar target 0%; next bar open simulation |
| v1 | reversion_12 | 9921.83 | -78.17 | sell /  / reversion_12: prior completed bar target 0%; next bar open simulation |
| v1 | volume_26 | 9916.22 | -83.78 | sell /  / volume_26: prior completed bar target 0%; next bar open simulation |
| v1 | trend_8_26 AND momentum_26 | 9808.05 | -191.95 | buy /  / trend_8_26 AND momentum_26: prior completed bar target 100%; next bar open simulation |
| v1 | trend_8_26 + momentum_26 | 9765.94 | -234.06 | buy /  / trend_8_26 + momentum_26: prior completed bar target 100%; next bar open simulation |
| v1 | trend_8_26 AND breakout_8 | 9770.28 | -229.72 | sell /  / trend_8_26 AND breakout_8: prior completed bar target 0%; next bar open simulation |
| v1 | trend_8_26 + breakout_8 | 9738.42 | -261.58 | sell /  / trend_8_26 + breakout_8: prior completed bar target 50%; next bar open simulation |
| v1 | trend_8_26 AND reversion_12 | 9928.06 | -71.94 | sell /  / trend_8_26 AND reversion_12: prior completed bar target 0%; next bar open simulation |
| v1 | trend_8_26 + reversion_12 | 9957.68 | -42.32 | sell /  / trend_8_26 + reversion_12: prior completed bar target 50%; next bar open simulation |
| v1 | trend_8_26 AND volume_26 | 9965.69 | -34.31 | sell /  / trend_8_26 AND volume_26: prior completed bar target 0%; next bar open simulation |
| v1 | trend_8_26 + volume_26 | 9934.37 | -65.63 | sell /  / trend_8_26 + volume_26: prior completed bar target 50%; next bar open simulation |
| v1 | momentum_26 AND breakout_8 | 9637.91 | -362.09 | sell /  / momentum_26 AND breakout_8: prior completed bar target 0%; next bar open simulation |
| v1 | momentum_26 + breakout_8 | 9593.97 | -406.03 | sell /  / momentum_26 + breakout_8: prior completed bar target 50%; next bar open simulation |
| v1 | momentum_26 AND reversion_12 | 9887.21 | -112.79 | sell /  / momentum_26 AND reversion_12: prior completed bar target 0%; next bar open simulation |
| v1 | momentum_26 + reversion_12 | 9770.89 | -229.11 | sell /  / momentum_26 + reversion_12: prior completed bar target 50%; next bar open simulation |
| v1 | momentum_26 AND volume_26 | 9894.55 | -105.45 | sell /  / momentum_26 AND volume_26: prior completed bar target 0%; next bar open simulation |
| v1 | momentum_26 + volume_26 | 9767.52 | -232.48 | sell /  / momentum_26 + volume_26: prior completed bar target 50%; next bar open simulation |
| v1 | breakout_8 AND reversion_12 | 10000.00 | 0.00 | 대기 /  / 새 신호 대기 |
| v1 | breakout_8 + reversion_12 | 9743.26 | -256.74 | sell /  / breakout_8 + reversion_12: prior completed bar target 0%; next bar open simulation |
| v1 | breakout_8 AND volume_26 | 9894.55 | -105.45 | sell /  / breakout_8 AND volume_26: prior completed bar target 0%; next bar open simulation |
| v1 | breakout_8 + volume_26 | 9739.97 | -260.03 | sell /  / breakout_8 + volume_26: prior completed bar target 0%; next bar open simulation |
| v1 | reversion_12 AND volume_26 | 10046.29 | 46.29 | sell /  / reversion_12 AND volume_26: prior completed bar target 0%; next bar open simulation |
| v1 | reversion_12 + volume_26 | 9919.48 | -80.52 | sell /  / reversion_12 + volume_26: prior completed bar target 0%; next bar open simulation |
| v1 | ema_12_26 | 9938.92 | -61.08 | buy /  / EMA12 > EMA26; 조건 충족; EMA12=726.261, EMA26=726.172 |
| v1 | macd_12_26_9 | 9980.95 | -19.05 | buy /  / MACD > 신호선 그리고 MACD > 0; 조건 충족; MACD=0.0889648, signal9=-0.313692 |
| v1 | rsi_14_recovery | 9999.22 | -0.78 | sell /  / 직전 RSI14 < 30, 현재 RSI14 >= 30 (한 봉 목표); 조건 미충족; RSI14=43.621, previous_RSI14=38.5787 |
| v1 | bollinger_20_reentry | 9777.09 | -222.91 | sell /  / 직전 종가 < 직전 하단밴드, 현재 하단밴드 <= 종가 <= SMA20 (한 봉 목표); 조건 미충족; close=721.16, lower20=716.851, SMA20=725.821, previous_lower20=717.276 |
| v1 | donchian_20 | 9943.28 | -56.72 | sell /  / 종가 > 현재 봉을 제외한 직전 20봉 최고가; 조건 미충족; close=735.35, prior_high20=745 |
| v1 | atr_14_breakout | 9768.31 | -231.69 | sell /  / 종가 > 직전 종가 + 직전 ATR14 그리고 종가 > EMA26; 조건 미충족; close=735.35, threshold=737.263, prior_ATR14=4.10289, EMA26=727.331 |
| v1 | session_vwap | 9605.41 | -394.59 | sell /  / 종가 > 뉴욕 거래일별 누적 전형가격 VWAP; 조건 미충족; close=725.47, session_VWAP=725.577, session_volume=4.43662e+06 |
| v1 | obv_20 | 9880.56 | -119.44 | buy /  / OBV > OBV의 SMA20 그리고 종가 > EMA26; 조건 충족; OBV=-5.0567e+06, OBV_SMA20=-6.30537e+06, close=733.16, EMA26=726.69 |
| v1 | stochastic_14_3_recovery | 9855.08 | -144.92 | sell /  / 직전 %K14 < 20에서 %K14가 %D3 상향 돌파 (한 봉 목표); 조건 미충족; K14=59.6496, D3=39.2535, previous_K14=43.8356, previous_D3=33.8642 |
| v1 | mfi_14_recovery | 10068.63 | 68.63 | sell /  / 직전 MFI14 < 20, 현재 MFI14 >= 20 (한 봉 목표); 조건 미충족; MFI14=32.7313, previous_MFI14=24.1736 |
| v1 | adx_14_trend | 10000.00 | 0.00 | 대기 /  / 새 신호 대기 |
| v1 | aroon_25_trend | 9999.46 | -0.54 | buy /  / Aroon25 Up > 70 그리고 Down < 30 (동률이면 최신 극값); 조건 충족; Aroon_up=76, Aroon_down=28 |
| v1 | cci_20_momentum | 9831.89 | -168.11 | sell /  / CCI20 > 100 (전형가격·평균절대편차); 조건 미충족; CCI20=87.5351 |
| v1 | williams_14_recovery | 10007.06 | 7.06 | sell /  / 직전 Williams %R14 < -80, 현재 >= -80 (한 봉 목표); 조건 미충족; Williams_R14=-40.3504, previous_R14=-56.1644 |
| v1 | cmf_20_accumulation | 9872.23 | -127.77 | sell /  / Chaikin Money Flow20 > 0.1; 조건 미충족; CMF20=0.061511, volume20=3.85936e+06 |
| v1 | chaikin_3_10 | 9680.37 | -319.63 | sell /  / ADL의 EMA3 - EMA10 > 0 그리고 종가 > EMA26; 조건 미충족; Chaikin3_10=50291.9, ADL=-5.10316e+06, close=725.47, EMA26=726.172 |
| v1 | roc_10_momentum | 9928.37 | -71.63 | sell /  / 10봉 ROC > 1% 그리고 종가 > EMA26; 조건 미충족; ROC10_percent=0.969802, close=733.48, EMA26=727.787 |
| v1 | trix_15_trend | 9672.71 | -327.29 | buy /  / 15봉 삼중 EMA의 1봉 변화율 TRIX > 0 그리고 종가 > EMA26; 조건 충족; TRIX15_percent=0.00081134, close=733.16, EMA26=726.69 |
| v1 | keltner_20_breakout | 10000.00 | 0.00 | 대기 /  / 새 신호 대기 |
| v1 | opening_range_30m | 10162.22 | 162.22 | sell /  / 뉴욕 09:30·09:45 두 완료 봉 최고가를 10:00 이후 종가가 돌파; 자료 부족·변동폭 또는 거래량 없음: 대기; close=733.16 |
| v2 | cash | 10000.00 | 0.00 | 대기 /  / 새 신호 대기 |
| v2 | buy_hold | 9186.13 | -813.87 | 중단: 손실 한도 / buy / partial / 직전 완료 봉 목표 비중 100%; 다음 봉 시가 가정 |
| v2 | trend_8_26 | 9829.40 | -170.60 | buy / partial / 직전 완료 봉 목표 비중 100%; 다음 봉 시가 가정 |
| v2 | momentum_26 | 9622.52 | -377.48 | buy / partial / 직전 완료 봉 목표 비중 100%; 다음 봉 시가 가정 |
| v2 | breakout_8 | 9382.51 | -617.49 | sell / filled / 직전 완료 봉 목표 비중 0%; 다음 봉 시가 가정 |
| v2 | reversion_12 | 9057.84 | -942.16 | 중단: 손실 한도 / buy / partial / 직전 완료 봉 목표 비중 100%; 다음 봉 시가 가정 |
| v2 | volume_26 | 9316.89 | -683.11 | 중단: 손실 한도 / buy / partial / 직전 완료 봉 목표 비중 100%; 다음 봉 시가 가정 |
| v2 | trend_8_26 AND momentum_26 | 9843.91 | -156.09 | buy / partial / 직전 완료 봉 목표 비중 100%; 다음 봉 시가 가정 |
| v2 | trend_8_26 + momentum_26 | 9726.46 | -273.54 | buy / partial / 직전 완료 봉 목표 비중 100%; 다음 봉 시가 가정 |
| v2 | trend_8_26 AND breakout_8 | 9681.86 | -318.14 | sell / filled / 직전 완료 봉 목표 비중 0%; 다음 봉 시가 가정 |
| v2 | trend_8_26 + breakout_8 | 9604.66 | -395.34 | sell / filled / 직전 완료 봉 목표 비중 50%; 다음 봉 시가 가정 |
| v2 | trend_8_26 AND reversion_12 | 9738.62 | -261.38 | sell / filled / 직전 완료 봉 목표 비중 0%; 다음 봉 시가 가정 |
| v2 | trend_8_26 + reversion_12 | 9574.36 | -425.64 | sell / filled / 직전 완료 봉 목표 비중 50%; 다음 봉 시가 가정 |
| v2 | trend_8_26 AND volume_26 | 9999.01 | -0.99 | sell / filled / 직전 완료 봉 목표 비중 0%; 다음 봉 시가 가정 |
| v2 | trend_8_26 + volume_26 | 9562.62 | -437.38 | sell / filled / 직전 완료 봉 목표 비중 50%; 다음 봉 시가 가정 |
| v2 | momentum_26 AND breakout_8 | 9602.70 | -397.30 | sell / filled / 직전 완료 봉 목표 비중 0%; 다음 봉 시가 가정 |
| v2 | momentum_26 + breakout_8 | 9502.02 | -497.98 | sell / filled / 직전 완료 봉 목표 비중 50%; 다음 봉 시가 가정 |
| v2 | momentum_26 AND reversion_12 | 9755.55 | -244.45 | sell / filled / 직전 완료 봉 목표 비중 0%; 다음 봉 시가 가정 |
| v2 | momentum_26 + reversion_12 | 9432.48 | -567.52 | sell / filled / 직전 완료 봉 목표 비중 50%; 다음 봉 시가 가정 |
| v2 | momentum_26 AND volume_26 | 9936.85 | -63.15 | sell / filled / 직전 완료 봉 목표 비중 0%; 다음 봉 시가 가정 |
| v2 | momentum_26 + volume_26 | 9460.57 | -539.43 | sell / filled / 직전 완료 봉 목표 비중 50%; 다음 봉 시가 가정 |
| v2 | breakout_8 AND reversion_12 | 10000.00 | 0.00 | 대기 /  / 새 신호 대기 |
| v2 | breakout_8 + reversion_12 | 9610.18 | -389.82 | 중단: 손실 한도 / sell / filled / 직전 완료 봉 목표 비중 0%; 다음 봉 시가 가정 |
| v2 | breakout_8 AND volume_26 | 9887.31 | -112.69 | sell / filled / 직전 완료 봉 목표 비중 0%; 다음 봉 시가 가정 |
| v2 | breakout_8 + volume_26 | 9341.97 | -658.03 | sell / filled / 직전 완료 봉 목표 비중 0%; 다음 봉 시가 가정 |
| v2 | reversion_12 AND volume_26 | 9252.44 | -747.56 | 중단: 손실 한도 / buy / partial / 직전 완료 봉 목표 비중 100%; 다음 봉 시가 가정 |
| v2 | reversion_12 + volume_26 | 9391.66 | -608.34 | 중단: 손실 한도 / sell / filled / 직전 완료 봉 목표 비중 50%; 다음 봉 시가 가정 |
| v2 | ema_12_26 | 9935.94 | -64.06 | buy / partial / EMA12 > EMA26; 조건 충족; EMA12=726.261, EMA26=726.172; 직전 완료 봉 목표를 다음 봉 시가에 모의 적용 |
| v2 | macd_12_26_9 | 9977.96 | -22.04 | buy / partial / MACD > 신호선 그리고 MACD > 0; 조건 충족; MACD=0.0889648, signal9=-0.313692; 직전 완료 봉 목표를 다음 봉 시가에 모의 적용 |
| v2 | rsi_14_recovery | 9995.22 | -4.78 | sell / filled / 직전 RSI14 < 30, 현재 RSI14 >= 30 (한 봉 목표); 조건 미충족; RSI14=43.621, previous_RSI14=38.5787; 직전 완료 봉 목표를 다음 봉 시가에 모의 적용 |
| v2 | bollinger_20_reentry | 9771.22 | -228.78 | sell / filled / 직전 종가 < 직전 하단밴드, 현재 하단밴드 <= 종가 <= SMA20 (한 봉 목표); 조건 미충족; close=721.16, lower20=716.851, SMA20=725.821, previous_lower20=717.276; 직전 완료 봉 목표를 다음 봉 시가에 모의 적용 |
| v2 | donchian_20 | 9939.30 | -60.70 | sell / filled / 종가 > 현재 봉을 제외한 직전 20봉 최고가; 조건 미충족; close=735.35, prior_high20=745; 직전 완료 봉 목표를 다음 봉 시가에 모의 적용 |
| v2 | atr_14_breakout | 9758.55 | -241.45 | sell / filled / 종가 > 직전 종가 + 직전 ATR14 그리고 종가 > EMA26; 조건 미충족; close=735.35, threshold=737.263, prior_ATR14=4.10289, EMA26=727.331; 직전 완료 봉 목표를 다음 봉 시가에 모의 적용 |
| v2 | session_vwap | 9588.13 | -411.87 | sell / filled / 종가 > 뉴욕 거래일별 누적 전형가격 VWAP; 조건 미충족; close=725.47, session_VWAP=725.577, session_volume=4.43662e+06; 직전 완료 봉 목표를 다음 봉 시가에 모의 적용 |
| v2 | obv_20 | 9869.70 | -130.30 | buy / partial / OBV > OBV의 SMA20 그리고 종가 > EMA26; 조건 충족; OBV=-5.0567e+06, OBV_SMA20=-6.30537e+06, close=733.16, EMA26=726.69; 직전 완료 봉 목표를 다음 봉 시가에 모의 적용 |
| v2 | stochastic_14_3_recovery | 9843.26 | -156.74 | sell / filled / 직전 %K14 < 20에서 %K14가 %D3 상향 돌파 (한 봉 목표); 조건 미충족; K14=59.6496, D3=39.2535, previous_K14=43.8356, previous_D3=33.8642; 직전 완료 봉 목표를 다음 봉 시가에 모의 적용 |
| v2 | mfi_14_recovery | 10064.61 | 64.61 | sell / filled / 직전 MFI14 < 20, 현재 MFI14 >= 20 (한 봉 목표); 조건 미충족; MFI14=32.7313, previous_MFI14=24.1736; 직전 완료 봉 목표를 다음 봉 시가에 모의 적용 |
| v2 | adx_14_trend | 10000.00 | 0.00 | 대기 /  / 새 신호 대기 |
| v2 | aroon_25_trend | 9994.47 | -5.53 | buy / partial / Aroon25 Up > 70 그리고 Down < 30 (동률이면 최신 극값); 조건 충족; Aroon_up=76, Aroon_down=28; 직전 완료 봉 목표를 다음 봉 시가에 모의 적용 |
| v2 | cci_20_momentum | 9825.99 | -174.01 | sell / filled / CCI20 > 100 (전형가격·평균절대편차); 조건 미충족; CCI20=87.5351; 직전 완료 봉 목표를 다음 봉 시가에 모의 적용 |
| v2 | williams_14_recovery | 9999.06 | -0.94 | sell / filled / 직전 Williams %R14 < -80, 현재 >= -80 (한 봉 목표); 조건 미충족; Williams_R14=-40.3504, previous_R14=-56.1644; 직전 완료 봉 목표를 다음 봉 시가에 모의 적용 |
| v2 | cmf_20_accumulation | 9864.34 | -135.66 | sell / filled / Chaikin Money Flow20 > 0.1; 조건 미충족; CMF20=0.061511, volume20=3.85936e+06; 직전 완료 봉 목표를 다음 봉 시가에 모의 적용 |
| v2 | chaikin_3_10 | 9674.34 | -325.66 | 중단: 손실 한도 / buy / partial / ADL의 EMA3 - EMA10 > 0 그리고 종가 > EMA26; 조건 충족; Chaikin3_10=293683, ADL=-4.91156e+06, close=739.58, EMA26=736.187; 직전 완료 봉 목표를 다음 봉 시가에 모의 적용 |
| v2 | roc_10_momentum | 9924.40 | -75.60 | sell / filled / 10봉 ROC > 1% 그리고 종가 > EMA26; 조건 미충족; ROC10_percent=0.969802, close=733.48, EMA26=727.787; 직전 완료 봉 목표를 다음 봉 시가에 모의 적용 |
| v2 | trix_15_trend | 9684.08 | -315.92 | 중단: 손실 한도 / buy / partial / 15봉 삼중 EMA의 1봉 변화율 TRIX > 0 그리고 종가 > EMA26; 조건 충족; TRIX15_percent=0.0196284, close=739.58, EMA26=736.187; 직전 완료 봉 목표를 다음 봉 시가에 모의 적용 |
| v2 | keltner_20_breakout | 10000.00 | 0.00 | 대기 /  / 새 신호 대기 |
| v2 | opening_range_30m | 10158.15 | 158.15 | sell / filled / 뉴욕 09:30·09:45 두 완료 봉 최고가를 10:00 이후 종가가 돌파; 자료 부족·변동폭 또는 거래량 없음: 대기; close=733.16; 직전 완료 봉 목표를 다음 봉 시가에 모의 적용 |

### 같은 기간의 비용·노출 비교 (사후 연구)

| 전략 | 비용 전 | 비용 후 | 100% 보유 | 같은 평균 노출 보유 | 평균 노출 |
|---|---:|---:|---:|---:|---:|
| cash | 0.00% | 0.00% | -10.42% | -0.00% | 0.00% |
| buy_hold | -10.05% | -10.42% | -10.42% | -10.42% | 100.00% |
| trend_8_26 | 1.12% | -2.63% | -10.42% | -4.81% | 45.12% |
| momentum_26 | -1.63% | -6.46% | -10.42% | -4.67% | 43.80% |
| breakout_8 | -3.49% | -15.62% | -10.42% | -1.56% | 14.51% |
| reversion_12 | -2.52% | -15.13% | -10.42% | -2.83% | 26.39% |
| volume_26 | -1.22% | -8.80% | -10.42% | -0.91% | 8.44% |
| trend_8_26 AND momentum_26 | 1.73% | -1.63% | -10.42% | -4.06% | 37.99% |
| trend_8_26 + momentum_26 | -0.24% | -4.55% | -10.42% | -4.74% | 44.46% |
| trend_8_26 AND breakout_8 | -2.02% | -8.77% | -10.42% | -0.80% | 7.39% |
| trend_8_26 + breakout_8 | -1.17% | -9.14% | -10.42% | -3.20% | 29.82% |
| trend_8_26 AND reversion_12 | 0.65% | -5.10% | -10.42% | -0.54% | 5.01% |
| trend_8_26 + reversion_12 | -0.63% | -8.29% | -10.42% | -3.82% | 35.76% |
| trend_8_26 AND volume_26 | 2.90% | 1.18% | -10.42% | -0.17% | 1.58% |
| trend_8_26 + volume_26 | 0.01% | -5.34% | -10.42% | -2.87% | 26.78% |
| momentum_26 AND breakout_8 | -2.75% | -10.58% | -10.42% | -0.88% | 8.18% |
| momentum_26 + breakout_8 | -2.52% | -11.13% | -10.42% | -3.13% | 29.16% |
| momentum_26 AND reversion_12 | -3.16% | -8.69% | -10.42% | -0.63% | 5.80% |
| momentum_26 + reversion_12 | -2.01% | -10.69% | -10.42% | -3.75% | 35.10% |
| momentum_26 AND volume_26 | 2.69% | 0.55% | -10.42% | -0.17% | 1.58% |
| momentum_26 + volume_26 | -1.37% | -7.22% | -10.42% | -2.80% | 26.12% |
| breakout_8 AND reversion_12 | 0.00% | 0.00% | -10.42% | -0.00% | 0.00% |
| breakout_8 + reversion_12 | -2.94% | -14.46% | -10.42% | -2.20% | 20.46% |
| breakout_8 AND volume_26 | 0.55% | -1.13% | -10.42% | -0.11% | 1.06% |
| breakout_8 + volume_26 | -2.33% | -11.71% | -10.42% | -1.24% | 11.48% |
| reversion_12 AND volume_26 | -0.54% | -5.03% | -10.42% | -0.57% | 5.28% |
| reversion_12 + volume_26 | -1.83% | -11.63% | -10.42% | -1.88% | 17.42% |
| ema_12_26 | 0.86% | -0.82% | -10.42% | -4.39% | 41.16% |
| macd_12_26_9 | 3.16% | 0.60% | -10.42% | -2.80% | 26.12% |
| rsi_14_recovery | -0.17% | -6.26% | -10.42% | -0.43% | 3.96% |
| bollinger_20_reentry | 0.54% | -5.20% | -10.42% | -0.40% | 3.69% |
| donchian_20 | -0.84% | -4.91% | -10.42% | -0.51% | 4.75% |
| atr_14_breakout | -1.25% | -7.28% | -10.42% | -0.46% | 4.22% |
| session_vwap | 2.48% | -10.03% | -10.42% | -5.08% | 47.76% |
| obv_20 | -1.39% | -10.85% | -10.42% | -2.30% | 21.37% |
| stochastic_14_3_recovery | -1.65% | -11.45% | -10.42% | -0.71% | 6.60% |
| mfi_14_recovery | 1.96% | -1.00% | -10.42% | -0.20% | 1.85% |
| adx_14_trend | -2.02% | -4.05% | -10.42% | -0.91% | 8.44% |
| aroon_25_trend | 0.17% | -3.54% | -10.42% | -1.25% | 11.61% |
| cci_20_momentum | -3.74% | -8.48% | -10.42% | -1.51% | 13.98% |
| williams_14_recovery | 0.89% | -6.85% | -10.42% | -0.54% | 5.01% |
| cmf_20_accumulation | -3.04% | -9.72% | -10.42% | -2.04% | 19.00% |
| chaikin_3_10 | -2.70% | -11.29% | -10.42% | -3.19% | 29.82% |
| roc_10_momentum | -1.64% | -7.25% | -10.42% | -1.39% | 12.93% |
| trix_15_trend | -0.52% | -4.61% | -10.42% | -3.42% | 31.93% |
| keltner_20_breakout | -2.87% | -5.29% | -10.42% | -0.29% | 2.64% |
| opening_range_30m | 7.86% | 2.99% | -10.42% | -2.83% | 26.39% |

동일 구간·초기 자금, 종료 시 청산 비용 포함. 노출 맞춤은 사후 설명용이며 v2 실제 계좌 성과가 아닙니다.
[낙폭 분해·비용 영향·전체 구간](CAT/comparison.json)

[v1 전체 기록](CAT/accounts.json) · [v2 전체 기록](CAT/accounts-v2.json)

## WMT 계좌

| 모델 | 전략 | 평가액 USD | 손익 USD | 최근 매매·이유 |
|---|---|---:|---:|---|
| v1 | cash | 10000.00 | 0.00 | 대기 /  / 새 신호 대기 |
| v1 | buy_hold | 9967.78 | -32.22 | buy /  / buy_hold: prior completed bar target 100%; next bar open simulation |
| v1 | trend_8_26 | 9791.85 | -208.15 | sell /  / trend_8_26: prior completed bar target 0%; next bar open simulation |
| v1 | momentum_26 | 9801.37 | -198.63 | sell /  / momentum_26: prior completed bar target 0%; next bar open simulation |
| v1 | breakout_8 | 9707.18 | -292.82 | buy /  / breakout_8: prior completed bar target 100%; next bar open simulation |
| v1 | reversion_12 | 9634.15 | -365.85 | sell /  / reversion_12: prior completed bar target 0%; next bar open simulation |
| v1 | volume_26 | 9761.42 | -238.58 | sell /  / volume_26: prior completed bar target 0%; next bar open simulation |
| v1 | trend_8_26 AND momentum_26 | 9811.64 | -188.36 | sell /  / trend_8_26 AND momentum_26: prior completed bar target 0%; next bar open simulation |
| v1 | trend_8_26 + momentum_26 | 9796.64 | -203.36 | sell /  / trend_8_26 + momentum_26: prior completed bar target 0%; next bar open simulation |
| v1 | trend_8_26 AND breakout_8 | 9854.29 | -145.71 | sell /  / trend_8_26 AND breakout_8: prior completed bar target 0%; next bar open simulation |
| v1 | trend_8_26 + breakout_8 | 9749.48 | -250.52 | buy /  / trend_8_26 + breakout_8: prior completed bar target 50%; next bar open simulation |
| v1 | trend_8_26 AND reversion_12 | 9798.51 | -201.49 | sell /  / trend_8_26 AND reversion_12: prior completed bar target 0%; next bar open simulation |
| v1 | trend_8_26 + reversion_12 | 9751.83 | -248.17 | sell /  / trend_8_26 + reversion_12: prior completed bar target 0%; next bar open simulation |
| v1 | trend_8_26 AND volume_26 | 9837.96 | -162.04 | sell /  / trend_8_26 AND volume_26: prior completed bar target 0%; next bar open simulation |
| v1 | trend_8_26 + volume_26 | 9776.88 | -223.12 | sell /  / trend_8_26 + volume_26: prior completed bar target 0%; next bar open simulation |
| v1 | momentum_26 AND breakout_8 | 9816.19 | -183.81 | sell /  / momentum_26 AND breakout_8: prior completed bar target 0%; next bar open simulation |
| v1 | momentum_26 + breakout_8 | 9813.07 | -186.93 | buy /  / momentum_26 + breakout_8: prior completed bar target 50%; next bar open simulation |
| v1 | momentum_26 AND reversion_12 | 9935.88 | -64.12 | sell /  / momentum_26 AND reversion_12: prior completed bar target 0%; next bar open simulation |
| v1 | momentum_26 + reversion_12 | 9815.11 | -184.89 | sell /  / momentum_26 + reversion_12: prior completed bar target 0%; next bar open simulation |
| v1 | momentum_26 AND volume_26 | 9905.94 | -94.06 | sell /  / momentum_26 AND volume_26: prior completed bar target 0%; next bar open simulation |
| v1 | momentum_26 + volume_26 | 9820.75 | -179.25 | sell /  / momentum_26 + volume_26: prior completed bar target 0%; next bar open simulation |
| v1 | breakout_8 AND reversion_12 | 10000.00 | 0.00 | 대기 /  / 새 신호 대기 |
| v1 | breakout_8 + reversion_12 | 9709.27 | -290.73 | buy /  / breakout_8 + reversion_12: prior completed bar target 50%; next bar open simulation |
| v1 | breakout_8 AND volume_26 | 9850.09 | -149.91 | sell /  / breakout_8 AND volume_26: prior completed bar target 0%; next bar open simulation |
| v1 | breakout_8 + volume_26 | 9734.33 | -265.67 | buy /  / breakout_8 + volume_26: prior completed bar target 50%; next bar open simulation |
| v1 | reversion_12 AND volume_26 | 9911.53 | -88.47 | sell /  / reversion_12 AND volume_26: prior completed bar target 0%; next bar open simulation |
| v1 | reversion_12 + volume_26 | 9736.41 | -263.59 | sell /  / reversion_12 + volume_26: prior completed bar target 0%; next bar open simulation |
| v1 | ema_12_26 | 9906.58 | -93.42 | sell /  / EMA12 > EMA26; 조건 미충족; EMA12=118.808, EMA26=118.852 |
| v1 | macd_12_26_9 | 9985.46 | -14.54 | sell /  / MACD > 신호선 그리고 MACD > 0; 조건 미충족; MACD=0.122825, signal9=0.127837 |
| v1 | rsi_14_recovery | 9973.19 | -26.81 | sell /  / 직전 RSI14 < 30, 현재 RSI14 >= 30 (한 봉 목표); 조건 미충족; RSI14=46.7246, previous_RSI14=43.1348 |
| v1 | bollinger_20_reentry | 9874.49 | -125.51 | sell /  / 직전 종가 < 직전 하단밴드, 현재 하단밴드 <= 종가 <= SMA20 (한 봉 목표); 조건 미충족; close=117.94, lower20=117.359, SMA20=117.989, previous_lower20=117.365 |
| v1 | donchian_20 | 9935.97 | -64.03 | sell /  / 종가 > 현재 봉을 제외한 직전 20봉 최고가; 조건 미충족; close=119.52, prior_high20=120.5 |
| v1 | atr_14_breakout | 9915.82 | -84.18 | sell /  / 종가 > 직전 종가 + 직전 ATR14 그리고 종가 > EMA26; 조건 미충족; close=119.52, threshold=120.186, prior_ATR14=0.395874, EMA26=118.952 |
| v1 | session_vwap | 9754.41 | -245.59 | buy /  / 종가 > 뉴욕 거래일별 누적 전형가격 VWAP; 조건 충족; close=117.788, session_VWAP=117.467, session_volume=3.21959e+06 |
| v1 | obv_20 | 9857.61 | -142.39 | sell /  / OBV > OBV의 SMA20 그리고 종가 > EMA26; 조건 미충족; OBV=1.5985e+07, OBV_SMA20=1.72435e+07, close=118.945, EMA26=118.951 |
| v1 | stochastic_14_3_recovery | 9535.67 | -464.33 | sell /  / 직전 %K14 < 20에서 %K14가 %D3 상향 돌파 (한 봉 목표); 조건 미충족; K14=41.7922, D3=26.634, previous_K14=28.1734, previous_D3=21.2618 |
| v1 | mfi_14_recovery | 9868.10 | -131.90 | sell /  / 직전 MFI14 < 20, 현재 MFI14 >= 20 (한 봉 목표); 조건 미충족; MFI14=23.7816, previous_MFI14=20.1936 |
| v1 | adx_14_trend | 9991.69 | -8.31 | sell /  / Wilder ADX14 >= 25 그리고 +DI14 > -DI14; 조건 미충족; ADX14=24.5142, plus_DI14=24.7537, minus_DI14=21.6519 |
| v1 | aroon_25_trend | 9947.63 | -52.37 | sell /  / Aroon25 Up > 70 그리고 Down < 30 (동률이면 최신 극값); 조건 미충족; Aroon_up=68, Aroon_down=4 |
| v1 | cci_20_momentum | 9772.81 | -227.19 | sell /  / CCI20 > 100 (전형가격·평균절대편차); 조건 미충족; CCI20=38.8365 |
| v1 | williams_14_recovery | 9640.68 | -359.32 | sell /  / 직전 Williams %R14 < -80, 현재 >= -80 (한 봉 목표); 조건 미충족; Williams_R14=-58.2078, previous_R14=-71.8266 |
| v1 | cmf_20_accumulation | 9801.46 | -198.54 | buy /  / Chaikin Money Flow20 > 0.1; 조건 충족; CMF20=0.126029, volume20=1.02737e+07 |
| v1 | chaikin_3_10 | 9762.96 | -237.04 | sell /  / ADL의 EMA3 - EMA10 > 0 그리고 종가 > EMA26; 조건 미충족; Chaikin3_10=-178256, ADL=1.07945e+07, close=119.52, EMA26=118.952 |
| v1 | roc_10_momentum | 10000.00 | 0.00 | 대기 /  / 새 신호 대기 |
| v1 | trix_15_trend | 9708.65 | -291.35 | sell /  / 15봉 삼중 EMA의 1봉 변화율 TRIX > 0 그리고 종가 > EMA26; 조건 미충족; TRIX15_percent=0.0142754, close=118.77, EMA26=118.947 |
| v1 | keltner_20_breakout | 9935.97 | -64.03 | sell /  / 종가 > EMA20 + 2 x Wilder ATR14; 조건 미충족; close=119.52, upper_Keltner=119.83, EMA20=119.013, ATR14=0.408312 |
| v1 | opening_range_30m | 9908.52 | -91.48 | buy /  / 뉴욕 09:30·09:45 두 완료 봉 최고가를 10:00 이후 종가가 돌파; 조건 충족; close=118, opening_high=117.96 |
| v2 | cash | 10000.00 | 0.00 | 대기 /  / 새 신호 대기 |
| v2 | buy_hold | 10560.77 | 560.77 | buy / partial / 직전 완료 봉 목표 비중 100%; 다음 봉 시가 가정 |
| v2 | trend_8_26 | 10187.81 | 187.81 | sell / filled / 직전 완료 봉 목표 비중 0%; 다음 봉 시가 가정 |
| v2 | momentum_26 | 10200.51 | 200.51 | sell / filled / 직전 완료 봉 목표 비중 0%; 다음 봉 시가 가정 |
| v2 | breakout_8 | 9660.30 | -339.70 | buy / partial / 직전 완료 봉 목표 비중 100%; 다음 봉 시가 가정 |
| v2 | reversion_12 | 9527.83 | -472.17 | sell / filled / 직전 완료 봉 목표 비중 0%; 다음 봉 시가 가정 |
| v2 | volume_26 | 9715.86 | -284.14 | sell / filled / 직전 완료 봉 목표 비중 0%; 다음 봉 시가 가정 |
| v2 | trend_8_26 AND momentum_26 | 10206.36 | 206.36 | sell / filled / 직전 완료 봉 목표 비중 0%; 다음 봉 시가 가정 |
| v2 | trend_8_26 + momentum_26 | 10194.13 | 194.13 | sell / filled / 직전 완료 봉 목표 비중 0%; 다음 봉 시가 가정 |
| v2 | trend_8_26 AND breakout_8 | 9935.59 | -64.41 | sell / filled / 직전 완료 봉 목표 비중 0%; 다음 봉 시가 가정 |
| v2 | trend_8_26 + breakout_8 | 9921.00 | -79.00 | buy / filled / 직전 완료 봉 목표 비중 50%; 다음 봉 시가 가정 |
| v2 | trend_8_26 AND reversion_12 | 9603.42 | -396.58 | sell / filled / 직전 완료 봉 목표 비중 0%; 다음 봉 시가 가정 |
| v2 | trend_8_26 + reversion_12 | 9895.37 | -104.63 | sell / filled / 직전 완료 봉 목표 비중 0%; 다음 봉 시가 가정 |
| v2 | trend_8_26 AND volume_26 | 9784.10 | -215.90 | sell / filled / 직전 완료 봉 목표 비중 0%; 다음 봉 시가 가정 |
| v2 | trend_8_26 + volume_26 | 9950.71 | -49.29 | sell / filled / 직전 완료 봉 목표 비중 0%; 다음 봉 시가 가정 |
| v2 | momentum_26 AND breakout_8 | 9773.67 | -226.33 | sell / filled / 직전 완료 봉 목표 비중 0%; 다음 봉 시가 가정 |
| v2 | momentum_26 + breakout_8 | 9990.05 | -9.95 | buy / filled / 직전 완료 봉 목표 비중 50%; 다음 봉 시가 가정 |
| v2 | momentum_26 AND reversion_12 | 9759.91 | -240.09 | sell / filled / 직전 완료 봉 목표 비중 0%; 다음 봉 시가 가정 |
| v2 | momentum_26 + reversion_12 | 10005.93 | 5.93 | sell / filled / 직전 완료 봉 목표 비중 0%; 다음 봉 시가 가정 |
| v2 | momentum_26 AND volume_26 | 9814.68 | -185.32 | sell / filled / 직전 완료 봉 목표 비중 0%; 다음 봉 시가 가정 |
| v2 | momentum_26 + volume_26 | 9998.77 | -1.23 | sell / filled / 직전 완료 봉 목표 비중 0%; 다음 봉 시가 가정 |
| v2 | breakout_8 AND reversion_12 | 10000.00 | 0.00 | 대기 /  / 새 신호 대기 |
| v2 | breakout_8 + reversion_12 | 9655.48 | -344.52 | buy / filled / 직전 완료 봉 목표 비중 50%; 다음 봉 시가 가정 |
| v2 | breakout_8 AND volume_26 | 9795.19 | -204.81 | sell / filled / 직전 완료 봉 목표 비중 0%; 다음 봉 시가 가정 |
| v2 | breakout_8 + volume_26 | 9689.44 | -310.56 | buy / filled / 직전 완료 봉 목표 비중 50%; 다음 봉 시가 가정 |
| v2 | reversion_12 AND volume_26 | 9917.25 | -82.75 | sell / filled / 직전 완료 봉 목표 비중 0%; 다음 봉 시가 가정 |
| v2 | reversion_12 + volume_26 | 9661.72 | -338.28 | sell / filled / 직전 완료 봉 목표 비중 0%; 다음 봉 시가 가정 |
| v2 | ema_12_26 | 9902.61 | -97.39 | sell / filled / EMA12 > EMA26; 조건 미충족; EMA12=118.808, EMA26=118.852; 직전 완료 봉 목표를 다음 봉 시가에 모의 적용 |
| v2 | macd_12_26_9 | 9981.46 | -18.54 | sell / filled / MACD > 신호선 그리고 MACD > 0; 조건 미충족; MACD=0.122825, signal9=0.127837; 직전 완료 봉 목표를 다음 봉 시가에 모의 적용 |
| v2 | rsi_14_recovery | 9971.19 | -28.81 | sell / filled / 직전 RSI14 < 30, 현재 RSI14 >= 30 (한 봉 목표); 조건 미충족; RSI14=46.7246, previous_RSI14=43.1348; 직전 완료 봉 목표를 다음 봉 시가에 모의 적용 |
| v2 | bollinger_20_reentry | 9868.57 | -131.43 | sell / filled / 직전 종가 < 직전 하단밴드, 현재 하단밴드 <= 종가 <= SMA20 (한 봉 목표); 조건 미충족; close=117.94, lower20=117.359, SMA20=117.989, previous_lower20=117.365; 직전 완료 봉 목표를 다음 봉 시가에 모의 적용 |
| v2 | donchian_20 | 9933.99 | -66.01 | sell / filled / 종가 > 현재 봉을 제외한 직전 20봉 최고가; 조건 미충족; close=119.52, prior_high20=120.5; 직전 완료 봉 목표를 다음 봉 시가에 모의 적용 |
| v2 | atr_14_breakout | 9911.85 | -88.15 | sell / filled / 종가 > 직전 종가 + 직전 ATR14 그리고 종가 > EMA26; 조건 미충족; close=119.52, threshold=120.186, prior_ATR14=0.395874, EMA26=118.952; 직전 완료 봉 목표를 다음 봉 시가에 모의 적용 |
| v2 | session_vwap | 9739.79 | -260.21 | buy / partial / 종가 > 뉴욕 거래일별 누적 전형가격 VWAP; 조건 충족; close=117.788, session_VWAP=117.467, session_volume=3.21959e+06; 직전 완료 봉 목표를 다음 봉 시가에 모의 적용 |
| v2 | obv_20 | 9847.76 | -152.24 | sell / filled / OBV > OBV의 SMA20 그리고 종가 > EMA26; 조건 미충족; OBV=1.6238e+07, OBV_SMA20=1.74966e+07, close=118.945, EMA26=118.951; 직전 완료 봉 목표를 다음 봉 시가에 모의 적용 |
| v2 | stochastic_14_3_recovery | 9671.94 | -328.06 | 중단: 손실 한도 / buy / partial / 직전 %K14 < 20에서 %K14가 %D3 상향 돌파 (한 봉 목표); 조건 충족; K14=25.6758, D3=22.4971, previous_K14=12.8379, previous_D3=25.8704; 직전 완료 봉 목표를 다음 봉 시가에 모의 적용 |
| v2 | mfi_14_recovery | 9862.18 | -137.82 | sell / filled / 직전 MFI14 < 20, 현재 MFI14 >= 20 (한 봉 목표); 조건 미충족; MFI14=23.7816, previous_MFI14=20.1936; 직전 완료 봉 목표를 다음 봉 시가에 모의 적용 |
| v2 | adx_14_trend | 9989.70 | -10.30 | sell / filled / Wilder ADX14 >= 25 그리고 +DI14 > -DI14; 조건 미충족; ADX14=24.5142, plus_DI14=24.7537, minus_DI14=21.6519; 직전 완료 봉 목표를 다음 봉 시가에 모의 적용 |
| v2 | aroon_25_trend | 9943.65 | -56.35 | sell / filled / Aroon25 Up > 70 그리고 Down < 30 (동률이면 최신 극값); 조건 미충족; Aroon_up=68, Aroon_down=4; 직전 완료 봉 목표를 다음 봉 시가에 모의 적용 |
| v2 | cci_20_momentum | 9766.95 | -233.05 | sell / filled / CCI20 > 100 (전형가격·평균절대편차); 조건 미충족; CCI20=38.8365; 직전 완료 봉 목표를 다음 봉 시가에 모의 적용 |
| v2 | williams_14_recovery | 9629.12 | -370.88 | sell / filled / 직전 Williams %R14 < -80, 현재 >= -80 (한 봉 목표); 조건 미충족; Williams_R14=-58.2078, previous_R14=-71.8266; 직전 완료 봉 목표를 다음 봉 시가에 모의 적용 |
| v2 | cmf_20_accumulation | 9790.68 | -209.32 | buy / partial / Chaikin Money Flow20 > 0.1; 조건 충족; CMF20=0.126029, volume20=1.02737e+07; 직전 완료 봉 목표를 다음 봉 시가에 모의 적용 |
| v2 | chaikin_3_10 | 9749.30 | -250.70 | sell / filled / ADL의 EMA3 - EMA10 > 0 그리고 종가 > EMA26; 조건 미충족; Chaikin3_10=-178256, ADL=1.4762e+07, close=119.52, EMA26=118.952; 직전 완료 봉 목표를 다음 봉 시가에 모의 적용 |
| v2 | roc_10_momentum | 10000.00 | 0.00 | 대기 /  / 새 신호 대기 |
| v2 | trix_15_trend | 9697.01 | -302.99 | sell / filled / 15봉 삼중 EMA의 1봉 변화율 TRIX > 0 그리고 종가 > EMA26; 조건 미충족; TRIX15_percent=0.0142754, close=118.77, EMA26=118.947; 직전 완료 봉 목표를 다음 봉 시가에 모의 적용 |
| v2 | keltner_20_breakout | 9933.99 | -66.01 | sell / filled / 종가 > EMA20 + 2 x Wilder ATR14; 조건 미충족; close=119.52, upper_Keltner=119.83, EMA20=119.013, ATR14=0.408312; 직전 완료 봉 목표를 다음 봉 시가에 모의 적용 |
| v2 | opening_range_30m | 9905.55 | -94.45 | buy / partial / 뉴욕 09:30·09:45 두 완료 봉 최고가를 10:00 이후 종가가 돌파; 조건 충족; close=118, opening_high=117.96; 직전 완료 봉 목표를 다음 봉 시가에 모의 적용 |

### 같은 기간의 비용·노출 비교 (사후 연구)

| 전략 | 비용 전 | 비용 후 | 100% 보유 | 같은 평균 노출 보유 | 평균 노출 |
|---|---:|---:|---:|---:|---:|
| cash | 0.00% | 0.00% | 12.00% | 0.00% | 0.00% |
| buy_hold | 12.47% | 12.00% | 12.00% | 12.00% | 100.00% |
| trend_8_26 | 8.93% | 5.77% | 12.00% | 8.01% | 68.07% |
| momentum_26 | 10.44% | 5.02% | 12.00% | 8.27% | 70.18% |
| breakout_8 | 6.09% | -10.31% | 12.00% | 2.93% | 25.59% |
| reversion_12 | 4.25% | -7.32% | 12.00% | 2.08% | 18.21% |
| volume_26 | 1.03% | -5.14% | 12.00% | 0.66% | 5.80% |
| trend_8_26 AND momentum_26 | 8.65% | 4.18% | 12.00% | 7.36% | 62.80% |
| trend_8_26 + momentum_26 | 9.69% | 5.39% | 12.00% | 8.14% | 69.13% |
| trend_8_26 AND breakout_8 | 6.59% | -6.43% | 12.00% | 2.41% | 21.11% |
| trend_8_26 + breakout_8 | 7.51% | -2.60% | 12.00% | 5.44% | 46.84% |
| trend_8_26 AND reversion_12 | 0.33% | -5.40% | 12.00% | 0.72% | 6.33% |
| trend_8_26 + reversion_12 | 6.60% | -0.35% | 12.00% | 5.00% | 43.14% |
| trend_8_26 AND volume_26 | 0.24% | -2.26% | 12.00% | 0.24% | 2.11% |
| trend_8_26 + volume_26 | 4.94% | 0.60% | 12.00% | 4.26% | 36.94% |
| momentum_26 AND breakout_8 | 6.62% | -7.18% | 12.00% | 2.63% | 22.96% |
| momentum_26 + breakout_8 | 8.26% | -2.12% | 12.00% | 5.56% | 47.90% |
| momentum_26 AND reversion_12 | 1.65% | -4.16% | 12.00% | 0.84% | 7.39% |
| momentum_26 + reversion_12 | 7.35% | 1.19% | 12.00% | 5.12% | 44.20% |
| momentum_26 AND volume_26 | 1.64% | -2.54% | 12.00% | 0.33% | 2.90% |
| momentum_26 + volume_26 | 5.67% | 0.24% | 12.00% | 4.39% | 38.00% |
| breakout_8 AND reversion_12 | 0.00% | 0.00% | 12.00% | 0.00% | 0.00% |
| breakout_8 + reversion_12 | 5.20% | -8.05% | 12.00% | 2.50% | 21.91% |
| breakout_8 AND volume_26 | 0.78% | -2.14% | 12.00% | 0.24% | 2.11% |
| breakout_8 + volume_26 | 3.55% | -7.56% | 12.00% | 1.79% | 15.71% |
| reversion_12 AND volume_26 | -0.59% | -3.47% | 12.00% | 0.27% | 2.37% |
| reversion_12 + volume_26 | 2.63% | -5.64% | 12.00% | 1.36% | 12.01% |
| ema_12_26 | 11.20% | 9.81% | 12.00% | 8.62% | 73.09% |
| macd_12_26_9 | 8.67% | 4.64% | 12.00% | 4.20% | 36.41% |
| rsi_14_recovery | -0.12% | -1.78% | 12.00% | 0.12% | 1.06% |
| bollinger_20_reentry | 1.28% | -2.07% | 12.00% | 0.24% | 2.11% |
| donchian_20 | 4.55% | -7.44% | 12.00% | 1.47% | 12.93% |
| atr_14_breakout | -0.90% | -10.40% | 12.00% | 0.84% | 7.39% |
| session_vwap | 9.69% | -0.83% | 12.00% | 6.79% | 58.05% |
| obv_20 | 10.62% | 3.00% | 12.00% | 6.56% | 56.20% |
| stochastic_14_3_recovery | 0.65% | -8.62% | 12.00% | 0.69% | 6.07% |
| mfi_14_recovery | -0.10% | -2.18% | 12.00% | 0.15% | 1.32% |
| adx_14_trend | 8.73% | 6.47% | 12.00% | 5.83% | 50.13% |
| aroon_25_trend | 7.01% | 2.18% | 12.00% | 3.61% | 31.40% |
| cci_20_momentum | 6.31% | -1.85% | 12.00% | 3.64% | 31.66% |
| williams_14_recovery | -0.84% | -9.59% | 12.00% | 0.66% | 5.80% |
| cmf_20_accumulation | 9.51% | 0.26% | 12.00% | 4.26% | 36.94% |
| chaikin_3_10 | 9.85% | 1.42% | 12.00% | 6.02% | 51.72% |
| roc_10_momentum | -0.29% | -4.79% | 12.00% | 1.59% | 13.98% |
| trix_15_trend | 10.97% | 6.86% | 12.00% | 7.65% | 65.17% |
| keltner_20_breakout | 6.59% | 0.08% | 12.00% | 3.06% | 26.65% |
| opening_range_30m | 9.76% | 4.37% | 12.00% | 4.23% | 36.68% |

동일 구간·초기 자금, 종료 시 청산 비용 포함. 노출 맞춤은 사후 설명용이며 v2 실제 계좌 성과가 아닙니다.
[낙폭 분해·비용 영향·전체 구간](WMT/comparison.json)

[v1 전체 기록](WMT/accounts.json) · [v2 전체 기록](WMT/accounts-v2.json)
