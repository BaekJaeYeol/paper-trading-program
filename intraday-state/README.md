# 모의투자 운영 현황

[PC·서버 장애 진단과 복구 방법](https://github.com/BaekJaeYeol/paper-trading-program/blob/main/investment-lab/docs/failure-recovery.md)

이번 실행 복구: {}

완료 봉 확인 주기: 기록 5/12회 · 기록 없는 예정 7회 · 아직 판정 전 14회 · 주의: 예약 시작 지연 또는 실행·저장 누락을 확인하세요.

[주기 판정 기준](https://github.com/BaekJaeYeol/paper-trading-program/blob/main/investment-lab/docs/session-coverage.md)

최근 확인: 2026-10-20T16:52:00.440060+00:00 (UTC)
다음 15분 확인 목표 (세션 실행 중에만 적용): 2026-10-20T17:07:00+00:00 (UTC, 실행 지연 가능)

실제 주문 없음. v1 기존 계좌와 v2 새 계좌의 시작일이 다르므로 수익률을 직접 우열 비교하지 마세요.
v2는 다음 봉 시가에 비용·스프레드·직전 거래량 제한을 적용한 가상 체결입니다. 미체결 잔량은 만료됩니다.

| 종목 | 상태 | 최근 성공 UTC | 마지막 완료 봉 UTC | 이번 새 봉 |
|---|---|---|---|---|
| SPY | updated | 2026-10-20T16:52:00.440060+00:00 | 2026-10-20T16:30:00+00:00 | 1 |
| QQQ | updated | 2026-10-20T16:52:00.440060+00:00 | 2026-10-20T16:30:00+00:00 | 1 |
| IWM | updated | 2026-10-20T16:52:00.440060+00:00 | 2026-10-20T16:30:00+00:00 | 1 |
| DIA | updated | 2026-10-20T16:52:00.440060+00:00 | 2026-10-20T16:30:00+00:00 | 1 |
| MSFT | updated | 2026-10-20T16:52:00.440060+00:00 | 2026-10-20T16:30:00+00:00 | 1 |
| JPM | updated | 2026-10-20T16:52:00.440060+00:00 | 2026-10-20T16:30:00+00:00 | 1 |
| XOM | updated | 2026-10-20T16:52:00.440060+00:00 | 2026-10-20T16:30:00+00:00 | 1 |
| JNJ | updated | 2026-10-20T16:52:00.440060+00:00 | 2026-10-20T16:30:00+00:00 | 1 |
| CAT | updated | 2026-10-20T16:52:00.440060+00:00 | 2026-10-20T16:30:00+00:00 | 1 |
| WMT | updated | 2026-10-20T16:52:00.440060+00:00 | 2026-10-20T16:30:00+00:00 | 1 |

이번 실행 소요: 46.93초
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
| v1 | buy_hold | 9929.82 | -70.18 | buy /  / buy_hold: prior completed bar target 100%; next bar open simulation |
| v1 | trend_8_26 | 9824.98 | -175.02 | buy /  / trend_8_26: prior completed bar target 100%; next bar open simulation |
| v1 | momentum_26 | 9757.91 | -242.09 | buy /  / momentum_26: prior completed bar target 100%; next bar open simulation |
| v1 | breakout_8 | 9752.40 | -247.60 | sell /  / breakout_8: prior completed bar target 0%; next bar open simulation |
| v1 | reversion_12 | 9831.96 | -168.04 | sell /  / reversion_12: prior completed bar target 0%; next bar open simulation |
| v1 | volume_26 | 9718.44 | -281.56 | sell /  / volume_26: prior completed bar target 0%; next bar open simulation |
| v1 | trend_8_26 AND momentum_26 | 9758.69 | -241.31 | buy /  / trend_8_26 AND momentum_26: prior completed bar target 100%; next bar open simulation |
| v1 | trend_8_26 + momentum_26 | 9791.38 | -208.62 | buy /  / trend_8_26 + momentum_26: prior completed bar target 100%; next bar open simulation |
| v1 | trend_8_26 AND breakout_8 | 9859.41 | -140.59 | sell /  / trend_8_26 AND breakout_8: prior completed bar target 0%; next bar open simulation |
| v1 | trend_8_26 + breakout_8 | 9827.74 | -172.26 | buy /  / trend_8_26 + breakout_8: prior completed bar target 50%; next bar open simulation |
| v1 | trend_8_26 AND reversion_12 | 9908.20 | -91.80 | sell /  / trend_8_26 AND reversion_12: prior completed bar target 0%; next bar open simulation |
| v1 | trend_8_26 + reversion_12 | 9828.33 | -171.67 | buy /  / trend_8_26 + reversion_12: prior completed bar target 50%; next bar open simulation |
| v1 | trend_8_26 AND volume_26 | 9764.18 | -235.82 | sell /  / trend_8_26 AND volume_26: prior completed bar target 0%; next bar open simulation |
| v1 | trend_8_26 + volume_26 | 9771.50 | -228.50 | buy /  / trend_8_26 + volume_26: prior completed bar target 50%; next bar open simulation |
| v1 | momentum_26 AND breakout_8 | 9831.79 | -168.21 | sell /  / momentum_26 AND breakout_8: prior completed bar target 0%; next bar open simulation |
| v1 | momentum_26 + breakout_8 | 9755.15 | -244.85 | buy /  / momentum_26 + breakout_8: prior completed bar target 50%; next bar open simulation |
| v1 | momentum_26 AND reversion_12 | 9904.38 | -95.62 | sell /  / momentum_26 AND reversion_12: prior completed bar target 0%; next bar open simulation |
| v1 | momentum_26 + reversion_12 | 9834.01 | -165.99 | buy /  / momentum_26 + reversion_12: prior completed bar target 50%; next bar open simulation |
| v1 | momentum_26 AND volume_26 | 9777.78 | -222.22 | sell /  / momentum_26 AND volume_26: prior completed bar target 0%; next bar open simulation |
| v1 | momentum_26 + volume_26 | 9738.08 | -261.92 | buy /  / momentum_26 + volume_26: prior completed bar target 50%; next bar open simulation |
| v1 | breakout_8 AND reversion_12 | 10000.00 | 0.00 | 대기 /  / 새 신호 대기 |
| v1 | breakout_8 + reversion_12 | 9791.96 | -208.04 | sell /  / breakout_8 + reversion_12: prior completed bar target 0%; next bar open simulation |
| v1 | breakout_8 AND volume_26 | 9878.80 | -121.20 | sell /  / breakout_8 AND volume_26: prior completed bar target 0%; next bar open simulation |
| v1 | breakout_8 + volume_26 | 9754.80 | -245.20 | sell /  / breakout_8 + volume_26: prior completed bar target 0%; next bar open simulation |
| v1 | reversion_12 AND volume_26 | 9899.64 | -100.36 | sell /  / reversion_12 AND volume_26: prior completed bar target 0%; next bar open simulation |
| v1 | reversion_12 + volume_26 | 9774.97 | -225.03 | sell /  / reversion_12 + volume_26: prior completed bar target 0%; next bar open simulation |
| v1 | ema_12_26 | 9790.53 | -209.47 | buy /  / EMA12 > EMA26; 조건 충족; EMA12=767.528, EMA26=767.458 |
| v1 | macd_12_26_9 | 9810.78 | -189.22 | buy /  / MACD > 신호선 그리고 MACD > 0; 조건 충족; MACD=0.396374, signal9=0.142666 |
| v1 | rsi_14_recovery | 9899.32 | -100.68 | sell /  / 직전 RSI14 < 30, 현재 RSI14 >= 30 (한 봉 목표); 조건 미충족; RSI14=34.3611, previous_RSI14=32.906 |
| v1 | bollinger_20_reentry | 9835.17 | -164.83 | sell /  / 직전 종가 < 직전 하단밴드, 현재 하단밴드 <= 종가 <= SMA20 (한 봉 목표); 조건 미충족; close=763.39, lower20=762.854, SMA20=768.639, previous_lower20=763.636 |
| v1 | donchian_20 | 9918.97 | -81.03 | sell /  / 종가 > 현재 봉을 제외한 직전 20봉 최고가; 조건 미충족; close=771.51, prior_high20=771.74 |
| v1 | atr_14_breakout | 9891.49 | -108.51 | sell /  / 종가 > 직전 종가 + 직전 ATR14 그리고 종가 > EMA26; 조건 미충족; close=771.51, threshold=773.161, prior_ATR14=1.48112, EMA26=768.048 |
| v1 | session_vwap | 9780.02 | -219.98 | sell /  / 종가 > 뉴욕 거래일별 누적 전형가격 VWAP; 조건 미충족; close=768.93, session_VWAP=770.349, session_volume=4.83081e+07 |
| v1 | obv_20 | 9909.51 | -90.49 | sell /  / OBV > OBV의 SMA20 그리고 종가 > EMA26; 조건 미충족; OBV=-2.19172e+07, OBV_SMA20=-1.86259e+07, close=768.275, EMA26=767.362 |
| v1 | stochastic_14_3_recovery | 9741.21 | -258.79 | sell /  / 직전 %K14 < 20에서 %K14가 %D3 상향 돌파 (한 봉 목표); 조건 미충족; K14=98.0782, D3=62.6231, previous_K14=85.5659, previous_D3=35.3943 |
| v1 | mfi_14_recovery | 9875.98 | -124.02 | sell /  / 직전 MFI14 < 20, 현재 MFI14 >= 20 (한 봉 목표); 조건 미충족; MFI14=33.0962, previous_MFI14=27.4403 |
| v1 | adx_14_trend | 9981.96 | -18.04 | sell /  / Wilder ADX14 >= 25 그리고 +DI14 > -DI14; 조건 미충족; ADX14=24.2312, plus_DI14=28.3519, minus_DI14=24.6578 |
| v1 | aroon_25_trend | 9861.30 | -138.70 | sell /  / Aroon25 Up > 70 그리고 Down < 30 (동률이면 최신 극값); 조건 미충족; Aroon_up=68, Aroon_down=20 |
| v1 | cci_20_momentum | 9816.97 | -183.03 | sell /  / CCI20 > 100 (전형가격·평균절대편차); 조건 미충족; CCI20=80.9096 |
| v1 | williams_14_recovery | 9713.37 | -286.63 | sell /  / 직전 Williams %R14 < -80, 현재 >= -80 (한 봉 목표); 조건 미충족; Williams_R14=-1.92177, previous_R14=-14.4341 |
| v1 | cmf_20_accumulation | 9890.95 | -109.05 | sell /  / Chaikin Money Flow20 > 0.1; 조건 미충족; CMF20=0.0493062, volume20=8.08389e+07 |
| v1 | chaikin_3_10 | 9846.41 | -153.59 | buy /  / ADL의 EMA3 - EMA10 > 0 그리고 종가 > EMA26; 조건 충족; Chaikin3_10=68101.1, ADL=-2.27944e+06, close=769.2, EMA26=768.702 |
| v1 | roc_10_momentum | 9953.42 | -46.58 | sell /  / 10봉 ROC > 1% 그리고 종가 > EMA26; 조건 미충족; ROC10_percent=0.806376, close=769.45, EMA26=767.181 |
| v1 | trix_15_trend | 9758.28 | -241.72 | buy /  / 15봉 삼중 EMA의 1봉 변화율 TRIX > 0 그리고 종가 > EMA26; 조건 충족; TRIX15_percent=0.0030347, close=767.955, EMA26=767.326 |
| v1 | keltner_20_breakout | 9924.71 | -75.29 | sell /  / 종가 > EMA20 + 2 x Wilder ATR14; 조건 미충족; close=768.93, upper_Keltner=771.837, EMA20=768.595, ATR14=1.6209 |
| v1 | opening_range_30m | 9759.48 | -240.52 | buy /  / 뉴욕 09:30·09:45 두 완료 봉 최고가를 10:00 이후 종가가 돌파; 조건 충족; close=769.1, opening_high=768 |
| v2 | cash | 10000.00 | 0.00 | 대기 /  / 새 신호 대기 |
| v2 | buy_hold | 9858.20 | -141.80 | buy / partial / 직전 완료 봉 목표 비중 100%; 다음 봉 시가 가정 |
| v2 | trend_8_26 | 9706.64 | -293.36 | buy / partial / 직전 완료 봉 목표 비중 100%; 다음 봉 시가 가정 |
| v2 | momentum_26 | 9609.52 | -390.48 | buy / partial / 직전 완료 봉 목표 비중 100%; 다음 봉 시가 가정 |
| v2 | breakout_8 | 9349.72 | -650.28 | sell / filled / 직전 완료 봉 목표 비중 0%; 다음 봉 시가 가정 |
| v2 | reversion_12 | 9366.23 | -633.77 | sell / filled / 직전 완료 봉 목표 비중 0%; 다음 봉 시가 가정 |
| v2 | volume_26 | 9166.45 | -833.55 | sell / filled / 직전 완료 봉 목표 비중 0%; 다음 봉 시가 가정 |
| v2 | trend_8_26 AND momentum_26 | 9616.83 | -383.17 | buy / partial / 직전 완료 봉 목표 비중 100%; 다음 봉 시가 가정 |
| v2 | trend_8_26 + momentum_26 | 9657.96 | -342.04 | buy / partial / 직전 완료 봉 목표 비중 100%; 다음 봉 시가 가정 |
| v2 | trend_8_26 AND breakout_8 | 9681.27 | -318.73 | sell / filled / 직전 완료 봉 목표 비중 0%; 다음 봉 시가 가정 |
| v2 | trend_8_26 + breakout_8 | 9566.38 | -433.62 | buy / filled / 직전 완료 봉 목표 비중 50%; 다음 봉 시가 가정 |
| v2 | trend_8_26 AND reversion_12 | 9801.35 | -198.65 | sell / filled / 직전 완료 봉 목표 비중 0%; 다음 봉 시가 가정 |
| v2 | trend_8_26 + reversion_12 | 9534.46 | -465.54 | buy / filled / 직전 완료 봉 목표 비중 50%; 다음 봉 시가 가정 |
| v2 | trend_8_26 AND volume_26 | 9606.04 | -393.96 | sell / filled / 직전 완료 봉 목표 비중 0%; 다음 봉 시가 가정 |
| v2 | trend_8_26 + volume_26 | 9452.21 | -547.79 | buy / filled / 직전 완료 봉 목표 비중 50%; 다음 봉 시가 가정 |
| v2 | momentum_26 AND breakout_8 | 9611.27 | -388.73 | sell / filled / 직전 완료 봉 목표 비중 0%; 다음 봉 시가 가정 |
| v2 | momentum_26 + breakout_8 | 9478.65 | -521.35 | buy / filled / 직전 완료 봉 목표 비중 50%; 다음 봉 시가 가정 |
| v2 | momentum_26 AND reversion_12 | 9864.00 | -136.00 | sell / filled / 직전 완료 봉 목표 비중 0%; 다음 봉 시가 가정 |
| v2 | momentum_26 + reversion_12 | 9546.63 | -453.37 | buy / filled / 직전 완료 봉 목표 비중 50%; 다음 봉 시가 가정 |
| v2 | momentum_26 AND volume_26 | 9689.11 | -310.89 | sell / filled / 직전 완료 봉 목표 비중 0%; 다음 봉 시가 가정 |
| v2 | momentum_26 + volume_26 | 9444.35 | -555.65 | buy / filled / 직전 완료 봉 목표 비중 50%; 다음 봉 시가 가정 |
| v2 | breakout_8 AND reversion_12 | 10000.00 | 0.00 | 대기 /  / 새 신호 대기 |
| v2 | breakout_8 + reversion_12 | 9396.79 | -603.21 | sell / filled / 직전 완료 봉 목표 비중 0%; 다음 봉 시가 가정 |
| v2 | breakout_8 AND volume_26 | 9808.87 | -191.13 | sell / filled / 직전 완료 봉 목표 비중 0%; 다음 봉 시가 가정 |
| v2 | breakout_8 + volume_26 | 9315.70 | -684.30 | sell / filled / 직전 완료 봉 목표 비중 0%; 다음 봉 시가 가정 |
| v2 | reversion_12 AND volume_26 | 9641.69 | -358.31 | sell / filled / 직전 완료 봉 목표 비중 0%; 다음 봉 시가 가정 |
| v2 | reversion_12 + volume_26 | 9343.62 | -656.38 | sell / filled / 직전 완료 봉 목표 비중 0%; 다음 봉 시가 가정 |
| v2 | ema_12_26 | 9785.64 | -214.36 | buy / partial / EMA12 > EMA26; 조건 충족; EMA12=767.528, EMA26=767.458; 직전 완료 봉 목표를 다음 봉 시가에 모의 적용 |
| v2 | macd_12_26_9 | 9805.88 | -194.12 | buy / partial / MACD > 신호선 그리고 MACD > 0; 조건 충족; MACD=0.396374, signal9=0.142666; 직전 완료 봉 목표를 다음 봉 시가에 모의 적용 |
| v2 | rsi_14_recovery | 9895.36 | -104.64 | sell / filled / 직전 RSI14 < 30, 현재 RSI14 >= 30 (한 봉 목표); 조건 미충족; RSI14=34.3611, previous_RSI14=32.906; 직전 완료 봉 목표를 다음 봉 시가에 모의 적용 |
| v2 | bollinger_20_reentry | 9829.27 | -170.73 | sell / filled / 직전 종가 < 직전 하단밴드, 현재 하단밴드 <= 종가 <= SMA20 (한 봉 목표); 조건 미충족; close=763.39, lower20=762.854, SMA20=768.639, previous_lower20=763.636; 직전 완료 봉 목표를 다음 봉 시가에 모의 적용 |
| v2 | donchian_20 | 9915.00 | -85.00 | sell / filled / 종가 > 현재 봉을 제외한 직전 20봉 최고가; 조건 미충족; close=771.51, prior_high20=771.74; 직전 완료 봉 목표를 다음 봉 시가에 모의 적용 |
| v2 | atr_14_breakout | 9885.56 | -114.44 | sell / filled / 종가 > 직전 종가 + 직전 ATR14 그리고 종가 > EMA26; 조건 미충족; close=771.51, threshold=773.161, prior_ATR14=1.48112, EMA26=768.048; 직전 완료 봉 목표를 다음 봉 시가에 모의 적용 |
| v2 | session_vwap | 9770.24 | -229.76 | sell / filled / 종가 > 뉴욕 거래일별 누적 전형가격 VWAP; 조건 미충족; close=768.93, session_VWAP=770.349, session_volume=4.83081e+07; 직전 완료 봉 목표를 다음 봉 시가에 모의 적용 |
| v2 | obv_20 | 9905.54 | -94.46 | sell / filled / OBV > OBV의 SMA20 그리고 종가 > EMA26; 조건 미충족; OBV=-1.1153e+07, OBV_SMA20=-7.86173e+06, close=768.275, EMA26=767.362; 직전 완료 봉 목표를 다음 봉 시가에 모의 적용 |
| v2 | stochastic_14_3_recovery | 9727.58 | -272.42 | sell / filled / 직전 %K14 < 20에서 %K14가 %D3 상향 돌파 (한 봉 목표); 조건 미충족; K14=98.0782, D3=62.6231, previous_K14=85.5659, previous_D3=35.3943; 직전 완료 봉 목표를 다음 봉 시가에 모의 적용 |
| v2 | mfi_14_recovery | 9870.05 | -129.95 | sell / filled / 직전 MFI14 < 20, 현재 MFI14 >= 20 (한 봉 목표); 조건 미충족; MFI14=33.0962, previous_MFI14=27.4403; 직전 완료 봉 목표를 다음 봉 시가에 모의 적용 |
| v2 | adx_14_trend | 9979.97 | -20.03 | sell / filled / Wilder ADX14 >= 25 그리고 +DI14 > -DI14; 조건 미충족; ADX14=24.2312, plus_DI14=28.3519, minus_DI14=24.6578; 직전 완료 봉 목표를 다음 봉 시가에 모의 적용 |
| v2 | aroon_25_trend | 9857.36 | -142.64 | sell / filled / Aroon25 Up > 70 그리고 Down < 30 (동률이면 최신 극값); 조건 미충족; Aroon_up=68, Aroon_down=20; 직전 완료 봉 목표를 다음 봉 시가에 모의 적용 |
| v2 | cci_20_momentum | 9809.12 | -190.88 | sell / filled / CCI20 > 100 (전형가격·평균절대편차); 조건 미충족; CCI20=80.9096; 직전 완료 봉 목표를 다음 봉 시가에 모의 적용 |
| v2 | williams_14_recovery | 9699.78 | -300.22 | sell / filled / 직전 Williams %R14 < -80, 현재 >= -80 (한 봉 목표); 조건 미충족; Williams_R14=-1.92177, previous_R14=-14.4341; 직전 완료 봉 목표를 다음 봉 시가에 모의 적용 |
| v2 | cmf_20_accumulation | 9887.00 | -113.00 | sell / filled / Chaikin Money Flow20 > 0.1; 조건 미충족; CMF20=0.0493062, volume20=8.08389e+07; 직전 완료 봉 목표를 다음 봉 시가에 모의 적용 |
| v2 | chaikin_3_10 | 9839.52 | -160.48 | buy / partial / ADL의 EMA3 - EMA10 > 0 그리고 종가 > EMA26; 조건 충족; Chaikin3_10=68101.1, ADL=-2.27944e+06, close=769.2, EMA26=768.702; 직전 완료 봉 목표를 다음 봉 시가에 모의 적용 |
| v2 | roc_10_momentum | 9951.43 | -48.57 | sell / filled / 10봉 ROC > 1% 그리고 종가 > EMA26; 조건 미충족; ROC10_percent=0.806376, close=769.45, EMA26=767.181; 직전 완료 봉 목표를 다음 봉 시가에 모의 적용 |
| v2 | trix_15_trend | 9749.50 | -250.50 | buy / partial / 15봉 삼중 EMA의 1봉 변화율 TRIX > 0 그리고 종가 > EMA26; 조건 충족; TRIX15_percent=0.0030347, close=767.955, EMA26=767.326; 직전 완료 봉 목표를 다음 봉 시가에 모의 적용 |
| v2 | keltner_20_breakout | 9922.73 | -77.27 | sell / filled / 종가 > EMA20 + 2 x Wilder ATR14; 조건 미충족; close=768.93, upper_Keltner=771.837, EMA20=768.595, ATR14=1.6209; 직전 완료 봉 목표를 다음 봉 시가에 모의 적용 |
| v2 | opening_range_30m | 9750.70 | -249.30 | buy / partial / 뉴욕 09:30·09:45 두 완료 봉 최고가를 10:00 이후 종가가 돌파; 조건 충족; close=769.1, opening_high=768; 직전 완료 봉 목표를 다음 봉 시가에 모의 적용 |

### 같은 기간의 비용·노출 비교 (사후 연구)

| 전략 | 비용 전 | 비용 후 | 100% 보유 | 같은 평균 노출 보유 | 평균 노출 |
|---|---:|---:|---:|---:|---:|
| cash | 0.00% | 0.00% | 0.23% | 0.00% | 0.00% |
| buy_hold | 0.65% | 0.23% | 0.23% | 0.23% | 100.00% |
| trend_8_26 | 1.26% | -2.50% | 0.23% | 0.12% | 53.95% |
| momentum_26 | -0.67% | -5.15% | 0.23% | 0.12% | 52.89% |
| breakout_8 | -0.34% | -16.46% | 0.23% | 0.05% | 22.63% |
| reversion_12 | -1.42% | -11.25% | 0.23% | 0.06% | 27.11% |
| volume_26 | -1.27% | -10.36% | 0.23% | 0.02% | 9.21% |
| trend_8_26 AND momentum_26 | 0.31% | -4.21% | 0.23% | 0.10% | 46.05% |
| trend_8_26 + momentum_26 | 0.29% | -3.83% | 0.23% | 0.12% | 53.42% |
| trend_8_26 AND breakout_8 | -0.15% | -11.60% | 0.23% | 0.03% | 13.95% |
| trend_8_26 + breakout_8 | 0.46% | -9.37% | 0.23% | 0.09% | 38.30% |
| trend_8_26 AND reversion_12 | -0.14% | -3.84% | 0.23% | 0.01% | 6.58% |
| trend_8_26 + reversion_12 | -0.09% | -6.79% | 0.23% | 0.09% | 40.53% |
| trend_8_26 AND volume_26 | -1.01% | -5.87% | 0.23% | 0.01% | 5.26% |
| trend_8_26 + volume_26 | -0.01% | -6.52% | 0.23% | 0.07% | 31.58% |
| momentum_26 AND breakout_8 | 0.28% | -11.60% | 0.23% | 0.03% | 15.26% |
| momentum_26 + breakout_8 | -0.50% | -10.98% | 0.23% | 0.09% | 37.77% |
| momentum_26 AND reversion_12 | -0.94% | -5.41% | 0.23% | 0.02% | 7.11% |
| momentum_26 + reversion_12 | -1.04% | -7.68% | 0.23% | 0.09% | 40.00% |
| momentum_26 AND volume_26 | -0.73% | -4.41% | 0.23% | 0.01% | 3.42% |
| momentum_26 + volume_26 | -0.96% | -6.63% | 0.23% | 0.07% | 31.06% |
| breakout_8 AND reversion_12 | 0.00% | 0.00% | 0.23% | 0.00% | 0.00% |
| breakout_8 + reversion_12 | -0.88% | -13.54% | 0.23% | 0.06% | 24.88% |
| breakout_8 AND volume_26 | -0.33% | -2.40% | 0.23% | 0.00% | 1.84% |
| breakout_8 + volume_26 | -0.80% | -12.37% | 0.23% | 0.04% | 15.93% |
| reversion_12 AND volume_26 | -0.88% | -4.95% | 0.23% | 0.01% | 3.68% |
| reversion_12 + volume_26 | -1.34% | -10.62% | 0.23% | 0.04% | 18.16% |
| ema_12_26 | -0.70% | -4.38% | 0.23% | 0.13% | 55.26% |
| macd_12_26_9 | -0.01% | -4.92% | 0.23% | 0.08% | 33.95% |
| rsi_14_recovery | -0.53% | -4.22% | 0.23% | 0.01% | 2.37% |
| bollinger_20_reentry | -1.07% | -6.72% | 0.23% | 0.01% | 3.68% |
| donchian_20 | 0.09% | -7.58% | 0.23% | 0.02% | 7.11% |
| atr_14_breakout | 0.54% | -5.20% | 0.23% | 0.01% | 4.21% |
| session_vwap | 2.14% | -8.04% | 0.23% | 0.11% | 48.42% |
| obv_20 | 0.32% | -7.37% | 0.23% | 0.09% | 38.42% |
| stochastic_14_3_recovery | -0.40% | -14.02% | 0.23% | 0.02% | 9.21% |
| mfi_14_recovery | -0.01% | -3.31% | 0.23% | 0.00% | 2.11% |
| adx_14_trend | 0.32% | -3.40% | 0.23% | 0.06% | 28.16% |
| aroon_25_trend | 0.82% | -2.10% | 0.23% | 0.06% | 25.79% |
| cci_20_momentum | -0.10% | -8.53% | 0.23% | 0.05% | 23.16% |
| williams_14_recovery | -0.58% | -10.49% | 0.23% | 0.01% | 6.58% |
| cmf_20_accumulation | 2.15% | -1.64% | 0.23% | 0.10% | 43.95% |
| chaikin_3_10 | 1.93% | -5.09% | 0.23% | 0.09% | 40.00% |
| roc_10_momentum | -0.13% | -0.97% | 0.23% | 0.00% | 1.05% |
| trix_15_trend | -0.31% | -4.41% | 0.23% | 0.09% | 41.58% |
| keltner_20_breakout | -0.26% | -4.36% | 0.23% | 0.03% | 11.58% |
| opening_range_30m | 0.07% | -6.43% | 0.23% | 0.08% | 35.00% |

동일 구간·초기 자금, 종료 시 청산 비용 포함. 노출 맞춤은 사후 설명용이며 v2 실제 계좌 성과가 아닙니다.
[낙폭 분해·비용 영향·전체 구간](SPY/comparison.json)

[v1 전체 기록](SPY/accounts.json) · [v2 전체 기록](SPY/accounts-v2.json)

## QQQ 계좌

| 모델 | 전략 | 평가액 USD | 손익 USD | 최근 매매·이유 |
|---|---|---:|---:|---|
| v1 | cash | 10000.00 | 0.00 | 대기 /  / 새 신호 대기 |
| v1 | buy_hold | 9893.80 | -106.20 | buy /  / buy_hold: prior completed bar target 100%; next bar open simulation |
| v1 | trend_8_26 | 9862.73 | -137.27 | buy /  / trend_8_26: prior completed bar target 100%; next bar open simulation |
| v1 | momentum_26 | 9617.56 | -382.44 | sell /  / momentum_26: prior completed bar target 0%; next bar open simulation |
| v1 | breakout_8 | 9742.42 | -257.58 | sell /  / breakout_8: prior completed bar target 0%; next bar open simulation |
| v1 | reversion_12 | 9812.67 | -187.33 | sell /  / reversion_12: prior completed bar target 0%; next bar open simulation |
| v1 | volume_26 | 9624.14 | -375.86 | sell /  / volume_26: prior completed bar target 0%; next bar open simulation |
| v1 | trend_8_26 AND momentum_26 | 9890.12 | -109.88 | sell /  / trend_8_26 AND momentum_26: prior completed bar target 0%; next bar open simulation |
| v1 | trend_8_26 + momentum_26 | 9758.94 | -241.06 | buy /  / trend_8_26 + momentum_26: prior completed bar target 50%; next bar open simulation |
| v1 | trend_8_26 AND breakout_8 | 9989.91 | -10.09 | sell /  / trend_8_26 AND breakout_8: prior completed bar target 0%; next bar open simulation |
| v1 | trend_8_26 + breakout_8 | 9841.64 | -158.36 | buy /  / trend_8_26 + breakout_8: prior completed bar target 50%; next bar open simulation |
| v1 | trend_8_26 AND reversion_12 | 9902.56 | -97.44 | sell /  / trend_8_26 AND reversion_12: prior completed bar target 0%; next bar open simulation |
| v1 | trend_8_26 + reversion_12 | 9837.80 | -162.20 | buy /  / trend_8_26 + reversion_12: prior completed bar target 50%; next bar open simulation |
| v1 | trend_8_26 AND volume_26 | 9864.33 | -135.67 | sell /  / trend_8_26 AND volume_26: prior completed bar target 0%; next bar open simulation |
| v1 | trend_8_26 + volume_26 | 9742.64 | -257.36 | sell /  / trend_8_26 + volume_26: prior completed bar target 50%; next bar open simulation |
| v1 | momentum_26 AND breakout_8 | 9773.97 | -226.03 | sell /  / momentum_26 AND breakout_8: prior completed bar target 0%; next bar open simulation |
| v1 | momentum_26 + breakout_8 | 9679.84 | -320.16 | sell /  / momentum_26 + breakout_8: prior completed bar target 0%; next bar open simulation |
| v1 | momentum_26 AND reversion_12 | 9800.84 | -199.16 | sell /  / momentum_26 AND reversion_12: prior completed bar target 0%; next bar open simulation |
| v1 | momentum_26 + reversion_12 | 9714.89 | -285.11 | sell /  / momentum_26 + reversion_12: prior completed bar target 0%; next bar open simulation |
| v1 | momentum_26 AND volume_26 | 9836.75 | -163.25 | sell /  / momentum_26 AND volume_26: prior completed bar target 0%; next bar open simulation |
| v1 | momentum_26 + volume_26 | 9640.09 | -359.91 | sell /  / momentum_26 + volume_26: prior completed bar target 0%; next bar open simulation |
| v1 | breakout_8 AND reversion_12 | 10000.00 | 0.00 | 대기 /  / 새 신호 대기 |
| v1 | breakout_8 + reversion_12 | 9797.19 | -202.81 | sell /  / breakout_8 + reversion_12: prior completed bar target 0%; next bar open simulation |
| v1 | breakout_8 AND volume_26 | 9947.15 | -52.85 | sell /  / breakout_8 AND volume_26: prior completed bar target 0%; next bar open simulation |
| v1 | breakout_8 + volume_26 | 9702.47 | -297.53 | sell /  / breakout_8 + volume_26: prior completed bar target 0%; next bar open simulation |
| v1 | reversion_12 AND volume_26 | 9907.31 | -92.69 | sell /  / reversion_12 AND volume_26: prior completed bar target 0%; next bar open simulation |
| v1 | reversion_12 + volume_26 | 9756.93 | -243.07 | sell /  / reversion_12 + volume_26: prior completed bar target 0%; next bar open simulation |
| v1 | ema_12_26 | 9696.67 | -303.33 | buy /  / EMA12 > EMA26; 조건 충족; EMA12=719.103, EMA26=719.016 |
| v1 | macd_12_26_9 | 9793.26 | -206.74 | sell /  / MACD > 신호선 그리고 MACD > 0; 조건 미충족; MACD=0.112193, signal9=0.128925 |
| v1 | rsi_14_recovery | 9809.40 | -190.60 | sell /  / 직전 RSI14 < 30, 현재 RSI14 >= 30 (한 봉 목표); 조건 미충족; RSI14=50.2063, previous_RSI14=44.1729 |
| v1 | bollinger_20_reentry | 9878.60 | -121.40 | sell /  / 직전 종가 < 직전 하단밴드, 현재 하단밴드 <= 종가 <= SMA20 (한 봉 목표); 조건 미충족; close=718.66, lower20=714.386, SMA20=719.409, previous_lower20=714.271 |
| v1 | donchian_20 | 9951.11 | -48.89 | sell /  / 종가 > 현재 봉을 제외한 직전 20봉 최고가; 조건 미충족; close=724.13, prior_high20=724.151 |
| v1 | atr_14_breakout | 9945.80 | -54.20 | sell /  / 종가 > 직전 종가 + 직전 ATR14 그리고 종가 > EMA26; 조건 미충족; close=721.52, threshold=724.646, prior_ATR14=2.53578, EMA26=719.016 |
| v1 | session_vwap | 9757.98 | -242.02 | sell /  / 종가 > 뉴욕 거래일별 누적 전형가격 VWAP; 조건 미충족; close=719.05, session_VWAP=719.729, session_volume=3.45027e+08 |
| v1 | obv_20 | 9767.73 | -232.27 | sell /  / OBV > OBV의 SMA20 그리고 종가 > EMA26; 조건 미충족; OBV=2.65783e+08, OBV_SMA20=1.24648e+08, close=719.05, EMA26=719.237 |
| v1 | stochastic_14_3_recovery | 9618.80 | -381.20 | sell /  / 직전 %K14 < 20에서 %K14가 %D3 상향 돌파 (한 봉 목표); 조건 미충족; K14=76.4321, D3=43.007, previous_K14=52.497, previous_D3=21.4564 |
| v1 | mfi_14_recovery | 9813.56 | -186.44 | sell /  / 직전 MFI14 < 20, 현재 MFI14 >= 20 (한 봉 목표); 조건 미충족; MFI14=30.3876, previous_MFI14=31.1747 |
| v1 | adx_14_trend | 9926.53 | -73.47 | sell /  / Wilder ADX14 >= 25 그리고 +DI14 > -DI14; 조건 미충족; ADX14=23.9831, plus_DI14=26.5781, minus_DI14=24.6326 |
| v1 | aroon_25_trend | 9875.01 | -124.99 | sell /  / Aroon25 Up > 70 그리고 Down < 30 (동률이면 최신 극값); 조건 미충족; Aroon_up=68, Aroon_down=20 |
| v1 | cci_20_momentum | 9880.19 | -119.81 | sell /  / CCI20 > 100 (전형가격·평균절대편차); 조건 미충족; CCI20=19.2232 |
| v1 | williams_14_recovery | 9710.09 | -289.91 | sell /  / 직전 Williams %R14 < -80, 현재 >= -80 (한 봉 목표); 조건 미충족; Williams_R14=-23.5679, previous_R14=-47.503 |
| v1 | cmf_20_accumulation | 9617.28 | -382.72 | buy /  / Chaikin Money Flow20 > 0.1; 조건 충족; CMF20=0.152804, volume20=3.24878e+08 |
| v1 | chaikin_3_10 | 9772.35 | -227.65 | sell /  / ADL의 EMA3 - EMA10 > 0 그리고 종가 > EMA26; 조건 미충족; Chaikin3_10=2.03031e+07, ADL=2.77046e+08, close=719.05, EMA26=719.237 |
| v1 | roc_10_momentum | 9990.50 | -9.50 | sell /  / 10봉 ROC > 1% 그리고 종가 > EMA26; 조건 미충족; ROC10_percent=0.483561, close=722.477, EMA26=718.78 |
| v1 | trix_15_trend | 9716.47 | -283.53 | sell /  / 15봉 삼중 EMA의 1봉 변화율 TRIX > 0 그리고 종가 > EMA26; 조건 미충족; TRIX15_percent=0.00323587, close=719.05, EMA26=719.237 |
| v1 | keltner_20_breakout | 9904.16 | -95.84 | sell /  / 종가 > EMA20 + 2 x Wilder ATR14; 조건 미충족; close=723.31, upper_Keltner=723.407, EMA20=718.722, ATR14=2.34265 |
| v1 | opening_range_30m | 9766.21 | -233.79 | buy /  / 뉴욕 09:30·09:45 두 완료 봉 최고가를 10:00 이후 종가가 돌파; 조건 충족; close=718.66, opening_high=716.18 |
| v2 | cash | 10000.00 | 0.00 | 대기 /  / 새 신호 대기 |
| v2 | buy_hold | 9574.00 | -426.00 | buy / partial / 직전 완료 봉 목표 비중 100%; 다음 봉 시가 가정 |
| v2 | trend_8_26 | 9664.29 | -335.71 | buy / partial / 직전 완료 봉 목표 비중 100%; 다음 봉 시가 가정 |
| v2 | momentum_26 | 9511.63 | -488.37 | sell / filled / 직전 완료 봉 목표 비중 0%; 다음 봉 시가 가정 |
| v2 | breakout_8 | 9411.37 | -588.63 | sell / filled / 직전 완료 봉 목표 비중 0%; 다음 봉 시가 가정 |
| v2 | reversion_12 | 9326.37 | -673.63 | sell / filled / 직전 완료 봉 목표 비중 0%; 다음 봉 시가 가정 |
| v2 | volume_26 | 9565.80 | -434.20 | 중단: 손실 한도 / sell / filled / 직전 완료 봉 목표 비중 0%; 다음 봉 시가 가정 |
| v2 | trend_8_26 AND momentum_26 | 9785.10 | -214.90 | sell / filled / 직전 완료 봉 목표 비중 0%; 다음 봉 시가 가정 |
| v2 | trend_8_26 + momentum_26 | 9607.92 | -392.08 | buy / filled / 직전 완료 봉 목표 비중 50%; 다음 봉 시가 가정 |
| v2 | trend_8_26 AND breakout_8 | 9883.87 | -116.13 | sell / filled / 직전 완료 봉 목표 비중 0%; 다음 봉 시가 가정 |
| v2 | trend_8_26 + breakout_8 | 9577.05 | -422.95 | buy / filled / 직전 완료 봉 목표 비중 50%; 다음 봉 시가 가정 |
| v2 | trend_8_26 AND reversion_12 | 9761.15 | -238.85 | sell / filled / 직전 완료 봉 목표 비중 0%; 다음 봉 시가 가정 |
| v2 | trend_8_26 + reversion_12 | 9493.64 | -506.36 | buy / filled / 직전 완료 봉 목표 비중 50%; 다음 봉 시가 가정 |
| v2 | trend_8_26 AND volume_26 | 9698.84 | -301.16 | sell / filled / 직전 완료 봉 목표 비중 0%; 다음 봉 시가 가정 |
| v2 | trend_8_26 + volume_26 | 9346.15 | -653.85 | sell / filled / 직전 완료 봉 목표 비중 50%; 다음 봉 시가 가정 |
| v2 | momentum_26 AND breakout_8 | 9727.76 | -272.24 | sell / filled / 직전 완료 봉 목표 비중 0%; 다음 봉 시가 가정 |
| v2 | momentum_26 + breakout_8 | 9461.38 | -538.62 | sell / filled / 직전 완료 봉 목표 비중 0%; 다음 봉 시가 가정 |
| v2 | momentum_26 AND reversion_12 | 9794.96 | -205.04 | sell / filled / 직전 완료 봉 목표 비중 0%; 다음 봉 시가 가정 |
| v2 | momentum_26 + reversion_12 | 9438.27 | -561.73 | sell / filled / 직전 완료 봉 목표 비중 0%; 다음 봉 시가 가정 |
| v2 | momentum_26 AND volume_26 | 9768.76 | -231.24 | sell / filled / 직전 완료 봉 목표 비중 0%; 다음 봉 시가 가정 |
| v2 | momentum_26 + volume_26 | 9291.55 | -708.45 | sell / filled / 직전 완료 봉 목표 비중 0%; 다음 봉 시가 가정 |
| v2 | breakout_8 AND reversion_12 | 10000.00 | 0.00 | 대기 /  / 새 신호 대기 |
| v2 | breakout_8 + reversion_12 | 9447.62 | -552.38 | sell / filled / 직전 완료 봉 목표 비중 0%; 다음 봉 시가 가정 |
| v2 | breakout_8 AND volume_26 | 9891.45 | -108.55 | sell / filled / 직전 완료 봉 목표 비중 0%; 다음 봉 시가 가정 |
| v2 | breakout_8 + volume_26 | 9281.43 | -718.57 | sell / filled / 직전 완료 봉 목표 비중 0%; 다음 봉 시가 가정 |
| v2 | reversion_12 AND volume_26 | 9547.64 | -452.36 | 중단: 손실 한도 / sell / filled / 직전 완료 봉 목표 비중 0%; 다음 봉 시가 가정 |
| v2 | reversion_12 + volume_26 | 9239.56 | -760.44 | sell / filled / 직전 완료 봉 목표 비중 0%; 다음 봉 시가 가정 |
| v2 | ema_12_26 | 9691.82 | -308.18 | buy / partial / EMA12 > EMA26; 조건 충족; EMA12=719.103, EMA26=719.016; 직전 완료 봉 목표를 다음 봉 시가에 모의 적용 |
| v2 | macd_12_26_9 | 9787.38 | -212.62 | sell / filled / MACD > 신호선 그리고 MACD > 0; 조건 미충족; MACD=0.112193, signal9=0.128925; 직전 완료 봉 목표를 다음 봉 시가에 모의 적용 |
| v2 | rsi_14_recovery | 9801.56 | -198.44 | sell / filled / 직전 RSI14 < 30, 현재 RSI14 >= 30 (한 봉 목표); 조건 미충족; RSI14=50.2063, previous_RSI14=44.1729; 직전 완료 봉 목표를 다음 봉 시가에 모의 적용 |
| v2 | bollinger_20_reentry | 9872.68 | -127.32 | sell / filled / 직전 종가 < 직전 하단밴드, 현재 하단밴드 <= 종가 <= SMA20 (한 봉 목표); 조건 미충족; close=718.66, lower20=714.386, SMA20=719.409, previous_lower20=714.271; 직전 완료 봉 목표를 다음 봉 시가에 모의 적용 |
| v2 | donchian_20 | 9947.13 | -52.87 | sell / filled / 종가 > 현재 봉을 제외한 직전 20봉 최고가; 조건 미충족; close=724.13, prior_high20=724.151; 직전 완료 봉 목표를 다음 봉 시가에 모의 적용 |
| v2 | atr_14_breakout | 9941.83 | -58.17 | sell / filled / 종가 > 직전 종가 + 직전 ATR14 그리고 종가 > EMA26; 조건 미충족; close=721.52, threshold=724.646, prior_ATR14=2.53578, EMA26=719.016; 직전 완료 봉 목표를 다음 봉 시가에 모의 적용 |
| v2 | session_vwap | 9746.27 | -253.73 | sell / filled / 종가 > 뉴욕 거래일별 누적 전형가격 VWAP; 조건 미충족; close=719.05, session_VWAP=719.729, session_volume=3.45027e+08; 직전 완료 봉 목표를 다음 봉 시가에 모의 적용 |
| v2 | obv_20 | 9759.92 | -240.08 | sell / filled / OBV > OBV의 SMA20 그리고 종가 > EMA26; 조건 미충족; OBV=2.65783e+08, OBV_SMA20=1.24648e+08, close=719.05, EMA26=719.237; 직전 완료 봉 목표를 다음 봉 시가에 모의 적용 |
| v2 | stochastic_14_3_recovery | 9694.13 | -305.87 | 중단: 손실 한도 / sell / filled / 직전 %K14 < 20에서 %K14가 %D3 상향 돌파 (한 봉 목표); 조건 미충족; K14=10.576, D3=8.00581, previous_K14=7.39787, previous_D3=7.27486; 직전 완료 봉 목표를 다음 봉 시가에 모의 적용 |
| v2 | mfi_14_recovery | 9809.63 | -190.37 | sell / filled / 직전 MFI14 < 20, 현재 MFI14 >= 20 (한 봉 목표); 조건 미충족; MFI14=30.3876, previous_MFI14=31.1747; 직전 완료 봉 목표를 다음 봉 시가에 모의 적용 |
| v2 | adx_14_trend | 9922.56 | -77.44 | sell / filled / Wilder ADX14 >= 25 그리고 +DI14 > -DI14; 조건 미충족; ADX14=23.9831, plus_DI14=26.5781, minus_DI14=24.6326; 직전 완료 봉 목표를 다음 봉 시가에 모의 적용 |
| v2 | aroon_25_trend | 9871.06 | -128.94 | sell / filled / Aroon25 Up > 70 그리고 Down < 30 (동률이면 최신 극값); 조건 미충족; Aroon_up=68, Aroon_down=20; 직전 완료 봉 목표를 다음 봉 시가에 모의 적용 |
| v2 | cci_20_momentum | 9874.26 | -125.74 | sell / filled / CCI20 > 100 (전형가격·평균절대편차); 조건 미충족; CCI20=19.2232; 직전 완료 봉 목표를 다음 봉 시가에 모의 적용 |
| v2 | williams_14_recovery | 9696.51 | -303.49 | sell / filled / 직전 Williams %R14 < -80, 현재 >= -80 (한 봉 목표); 조건 미충족; Williams_R14=-23.5679, previous_R14=-47.503; 직전 완료 봉 목표를 다음 봉 시가에 모의 적용 |
| v2 | cmf_20_accumulation | 9604.79 | -395.21 | buy / partial / Chaikin Money Flow20 > 0.1; 조건 충족; CMF20=0.152804, volume20=3.24878e+08; 직전 완료 봉 목표를 다음 봉 시가에 모의 적용 |
| v2 | chaikin_3_10 | 9764.53 | -235.47 | sell / filled / ADL의 EMA3 - EMA10 > 0 그리고 종가 > EMA26; 조건 미충족; Chaikin3_10=2.03031e+07, ADL=2.77046e+08, close=719.05, EMA26=719.237; 직전 완료 봉 목표를 다음 봉 시가에 모의 적용 |
| v2 | roc_10_momentum | 9988.50 | -11.50 | sell / filled / 10봉 ROC > 1% 그리고 종가 > EMA26; 조건 미충족; ROC10_percent=0.483561, close=722.477, EMA26=718.78; 직전 완료 봉 목표를 다음 봉 시가에 모의 적용 |
| v2 | trix_15_trend | 9708.70 | -291.30 | sell / filled / 15봉 삼중 EMA의 1봉 변화율 TRIX > 0 그리고 종가 > EMA26; 조건 미충족; TRIX15_percent=0.00323587, close=719.05, EMA26=719.237; 직전 완료 봉 목표를 다음 봉 시가에 모의 적용 |
| v2 | keltner_20_breakout | 9900.20 | -99.80 | sell / filled / 종가 > EMA20 + 2 x Wilder ATR14; 조건 미충족; close=723.31, upper_Keltner=723.407, EMA20=718.722, ATR14=2.34265; 직전 완료 봉 목표를 다음 봉 시가에 모의 적용 |
| v2 | opening_range_30m | 9759.38 | -240.62 | buy / partial / 뉴욕 09:30·09:45 두 완료 봉 최고가를 10:00 이후 종가가 돌파; 조건 충족; close=718.66, opening_high=716.18; 직전 완료 봉 목표를 다음 봉 시가에 모의 적용 |

### 같은 기간의 비용·노출 비교 (사후 연구)

| 전략 | 비용 전 | 비용 후 | 100% 보유 | 같은 평균 노출 보유 | 평균 노출 |
|---|---:|---:|---:|---:|---:|
| cash | 0.00% | 0.00% | -2.97% | -0.00% | 0.00% |
| buy_hold | -2.56% | -2.97% | -2.97% | -2.97% | 100.00% |
| trend_8_26 | 0.67% | -3.06% | -2.97% | -1.36% | 45.79% |
| momentum_26 | -2.58% | -7.76% | -2.97% | -1.22% | 41.05% |
| breakout_8 | -1.66% | -16.87% | -2.97% | -0.55% | 18.42% |
| reversion_12 | -0.70% | -12.09% | -2.97% | -0.87% | 29.21% |
| volume_26 | -1.17% | -14.68% | -2.97% | -0.48% | 16.05% |
| trend_8_26 AND momentum_26 | 0.29% | -3.43% | -2.97% | -1.04% | 35.00% |
| trend_8_26 + momentum_26 | -0.96% | -5.04% | -2.97% | -1.29% | 43.42% |
| trend_8_26 AND breakout_8 | -0.01% | -8.84% | -2.97% | -0.34% | 11.32% |
| trend_8_26 + breakout_8 | -0.49% | -9.66% | -2.97% | -0.95% | 32.11% |
| trend_8_26 AND reversion_12 | -0.22% | -4.73% | -2.97% | -0.19% | 6.58% |
| trend_8_26 + reversion_12 | -0.00% | -7.30% | -2.97% | -1.11% | 37.50% |
| trend_8_26 AND volume_26 | 0.45% | -4.49% | -2.97% | -0.15% | 5.00% |
| trend_8_26 + volume_26 | -0.25% | -8.87% | -2.97% | -0.92% | 30.93% |
| momentum_26 AND breakout_8 | -0.75% | -9.89% | -2.97% | -0.34% | 11.32% |
| momentum_26 + breakout_8 | -2.12% | -12.25% | -2.97% | -0.88% | 29.74% |
| momentum_26 AND reversion_12 | -1.16% | -6.41% | -2.97% | -0.20% | 6.84% |
| momentum_26 + reversion_12 | -1.64% | -9.57% | -2.97% | -1.04% | 35.14% |
| momentum_26 AND volume_26 | -0.28% | -4.38% | -2.97% | -0.11% | 3.68% |
| momentum_26 + volume_26 | -1.87% | -10.92% | -2.97% | -0.85% | 28.56% |
| breakout_8 AND reversion_12 | 0.00% | 0.00% | -2.97% | -0.00% | 0.00% |
| breakout_8 + reversion_12 | -1.17% | -13.62% | -2.97% | -0.71% | 23.82% |
| breakout_8 AND volume_26 | 0.32% | -2.18% | -2.97% | -0.05% | 1.84% |
| breakout_8 + volume_26 | -1.41% | -14.36% | -2.97% | -0.51% | 17.25% |
| reversion_12 AND volume_26 | -1.31% | -8.11% | -2.97% | -0.25% | 8.42% |
| reversion_12 + volume_26 | -0.93% | -12.85% | -2.97% | -0.67% | 22.64% |
| ema_12_26 | -0.85% | -3.32% | -2.97% | -1.26% | 42.63% |
| macd_12_26_9 | 0.89% | -3.26% | -2.97% | -0.74% | 25.00% |
| rsi_14_recovery | -0.47% | -5.76% | -2.97% | -0.10% | 3.42% |
| bollinger_20_reentry | -0.08% | -6.18% | -2.97% | -0.12% | 3.95% |
| donchian_20 | 0.59% | -4.75% | -2.97% | -0.17% | 5.79% |
| atr_14_breakout | 0.47% | -3.67% | -2.97% | -0.09% | 3.16% |
| session_vwap | -0.15% | -11.97% | -2.97% | -1.43% | 48.16% |
| obv_20 | -1.18% | -9.90% | -2.97% | -0.87% | 29.21% |
| stochastic_14_3_recovery | -0.31% | -11.75% | -2.97% | -0.23% | 7.63% |
| mfi_14_recovery | -1.23% | -3.69% | -2.97% | -0.05% | 1.58% |
| adx_14_trend | -0.11% | -3.00% | -2.97% | -0.64% | 21.58% |
| aroon_25_trend | 1.27% | -2.07% | -2.97% | -0.54% | 18.16% |
| cci_20_momentum | -0.45% | -5.74% | -2.97% | -0.51% | 17.11% |
| williams_14_recovery | -0.63% | -10.91% | -2.97% | -0.20% | 6.84% |
| cmf_20_accumulation | -1.84% | -9.75% | -2.97% | -0.93% | 31.32% |
| chaikin_3_10 | -2.63% | -10.48% | -2.97% | -1.08% | 36.32% |
| roc_10_momentum | -0.00% | -1.67% | -2.97% | -0.12% | 4.21% |
| trix_15_trend | -0.35% | -3.23% | -2.97% | -1.01% | 34.21% |
| keltner_20_breakout | -0.89% | -5.76% | -2.97% | -0.24% | 8.16% |
| opening_range_30m | -1.02% | -7.84% | -2.97% | -0.83% | 27.89% |

동일 구간·초기 자금, 종료 시 청산 비용 포함. 노출 맞춤은 사후 설명용이며 v2 실제 계좌 성과가 아닙니다.
[낙폭 분해·비용 영향·전체 구간](QQQ/comparison.json)

[v1 전체 기록](QQQ/accounts.json) · [v2 전체 기록](QQQ/accounts-v2.json)

## IWM 계좌

| 모델 | 전략 | 평가액 USD | 손익 USD | 최근 매매·이유 |
|---|---|---:|---:|---|
| v1 | cash | 10000.00 | 0.00 | 대기 /  / 새 신호 대기 |
| v1 | buy_hold | 9986.01 | -13.99 | buy /  / buy_hold: prior completed bar target 100%; next bar open simulation |
| v1 | trend_8_26 | 9791.60 | -208.40 | buy /  / trend_8_26: prior completed bar target 100%; next bar open simulation |
| v1 | momentum_26 | 9962.31 | -37.69 | buy /  / momentum_26: prior completed bar target 100%; next bar open simulation |
| v1 | breakout_8 | 9713.59 | -286.41 | sell /  / breakout_8: prior completed bar target 0%; next bar open simulation |
| v1 | reversion_12 | 9786.62 | -213.38 | sell /  / reversion_12: prior completed bar target 0%; next bar open simulation |
| v1 | volume_26 | 9923.29 | -76.71 | sell /  / volume_26: prior completed bar target 0%; next bar open simulation |
| v1 | trend_8_26 AND momentum_26 | 9807.51 | -192.49 | buy /  / trend_8_26 AND momentum_26: prior completed bar target 100%; next bar open simulation |
| v1 | trend_8_26 + momentum_26 | 9876.65 | -123.35 | buy /  / trend_8_26 + momentum_26: prior completed bar target 100%; next bar open simulation |
| v1 | trend_8_26 AND breakout_8 | 9803.67 | -196.33 | sell /  / trend_8_26 AND breakout_8: prior completed bar target 0%; next bar open simulation |
| v1 | trend_8_26 + breakout_8 | 9752.70 | -247.30 | sell /  / trend_8_26 + breakout_8: prior completed bar target 50%; next bar open simulation |
| v1 | trend_8_26 AND reversion_12 | 9827.31 | -172.69 | sell /  / trend_8_26 AND reversion_12: prior completed bar target 0%; next bar open simulation |
| v1 | trend_8_26 + reversion_12 | 9789.01 | -210.99 | sell /  / trend_8_26 + reversion_12: prior completed bar target 50%; next bar open simulation |
| v1 | trend_8_26 AND volume_26 | 9935.98 | -64.02 | sell /  / trend_8_26 AND volume_26: prior completed bar target 0%; next bar open simulation |
| v1 | trend_8_26 + volume_26 | 9876.86 | -123.14 | sell /  / trend_8_26 + volume_26: prior completed bar target 50%; next bar open simulation |
| v1 | momentum_26 AND breakout_8 | 9853.20 | -146.80 | sell /  / momentum_26 AND breakout_8: prior completed bar target 0%; next bar open simulation |
| v1 | momentum_26 + breakout_8 | 9857.01 | -142.99 | sell /  / momentum_26 + breakout_8: prior completed bar target 50%; next bar open simulation |
| v1 | momentum_26 AND reversion_12 | 9924.34 | -75.66 | sell /  / momentum_26 AND reversion_12: prior completed bar target 0%; next bar open simulation |
| v1 | momentum_26 + reversion_12 | 9893.75 | -106.25 | sell /  / momentum_26 + reversion_12: prior completed bar target 50%; next bar open simulation |
| v1 | momentum_26 AND volume_26 | 10062.05 | 62.05 | sell /  / momentum_26 AND volume_26: prior completed bar target 0%; next bar open simulation |
| v1 | momentum_26 + volume_26 | 9942.68 | -57.32 | sell /  / momentum_26 + volume_26: prior completed bar target 50%; next bar open simulation |
| v1 | breakout_8 AND reversion_12 | 10000.00 | 0.00 | 대기 /  / 새 신호 대기 |
| v1 | breakout_8 + reversion_12 | 9749.93 | -250.07 | sell /  / breakout_8 + reversion_12: prior completed bar target 0%; next bar open simulation |
| v1 | breakout_8 AND volume_26 | 9967.28 | -32.72 | sell /  / breakout_8 AND volume_26: prior completed bar target 0%; next bar open simulation |
| v1 | breakout_8 + volume_26 | 9837.51 | -162.49 | sell /  / breakout_8 + volume_26: prior completed bar target 0%; next bar open simulation |
| v1 | reversion_12 AND volume_26 | 9935.98 | -64.02 | sell /  / reversion_12 AND volume_26: prior completed bar target 0%; next bar open simulation |
| v1 | reversion_12 + volume_26 | 9874.40 | -125.60 | sell /  / reversion_12 + volume_26: prior completed bar target 0%; next bar open simulation |
| v1 | ema_12_26 | 9856.67 | -143.33 | buy /  / EMA12 > EMA26; 조건 충족; EMA12=271.545, EMA26=271.529 |
| v1 | macd_12_26_9 | 9935.27 | -64.73 | buy /  / MACD > 신호선 그리고 MACD > 0; 조건 충족; MACD=0.0161944, signal9=-0.0860005 |
| v1 | rsi_14_recovery | 9786.95 | -213.05 | sell /  / 직전 RSI14 < 30, 현재 RSI14 >= 30 (한 봉 목표); 조건 미충족; RSI14=46.986, previous_RSI14=37.1649 |
| v1 | bollinger_20_reentry | 9924.03 | -75.97 | sell /  / 직전 종가 < 직전 하단밴드, 현재 하단밴드 <= 종가 <= SMA20 (한 봉 목표); 조건 미충족; close=271.19, lower20=270.018, SMA20=273.224, previous_lower20=270.283 |
| v1 | donchian_20 | 9835.91 | -164.09 | sell /  / 종가 > 현재 봉을 제외한 직전 20봉 최고가; 조건 미충족; close=275.785, prior_high20=276.875 |
| v1 | atr_14_breakout | 9883.94 | -116.06 | sell /  / 종가 > 직전 종가 + 직전 ATR14 그리고 종가 > EMA26; 조건 미충족; close=276.33, threshold=276.592, prior_ATR14=0.747363, EMA26=272.499 |
| v1 | session_vwap | 9859.65 | -140.35 | buy /  / 종가 > 뉴욕 거래일별 누적 전형가격 VWAP; 조건 충족; close=272.6, session_VWAP=272.22, session_volume=3.20722e+06 |
| v1 | obv_20 | 9851.04 | -148.96 | buy /  / OBV > OBV의 SMA20 그리고 종가 > EMA26; 조건 충족; OBV=-2.88653e+07, OBV_SMA20=-3.02185e+07, close=272.6, EMA26=271.529 |
| v1 | stochastic_14_3_recovery | 9665.87 | -334.13 | sell /  / 직전 %K14 < 20에서 %K14가 %D3 상향 돌파 (한 봉 목표); 조건 미충족; K14=72.727, D3=41.2922, previous_K14=34.0903, previous_D3=23.8263 |
| v1 | mfi_14_recovery | 9934.22 | -65.78 | sell /  / 직전 MFI14 < 20, 현재 MFI14 >= 20 (한 봉 목표); 조건 미충족; MFI14=34.131, previous_MFI14=22.0435 |
| v1 | adx_14_trend | 9782.25 | -217.75 | buy /  / Wilder ADX14 >= 25 그리고 +DI14 > -DI14; 조건 충족; ADX14=26.5262, plus_DI14=49.1478, minus_DI14=9.69634 |
| v1 | aroon_25_trend | 9832.16 | -167.84 | sell /  / Aroon25 Up > 70 그리고 Down < 30 (동률이면 최신 극값); 조건 미충족; Aroon_up=100, Aroon_down=68 |
| v1 | cci_20_momentum | 9955.08 | -44.92 | sell /  / CCI20 > 100 (전형가격·평균절대편차); 조건 미충족; CCI20=86.224 |
| v1 | williams_14_recovery | 9833.31 | -166.69 | sell /  / 직전 Williams %R14 < -80, 현재 >= -80 (한 봉 목표); 조건 미충족; Williams_R14=-27.273, previous_R14=-65.9097 |
| v1 | cmf_20_accumulation | 9803.64 | -196.36 | buy /  / Chaikin Money Flow20 > 0.1; 조건 충족; CMF20=0.208851, volume20=1.40263e+07 |
| v1 | chaikin_3_10 | 9851.93 | -148.07 | buy /  / ADL의 EMA3 - EMA10 > 0 그리고 종가 > EMA26; 조건 충족; Chaikin3_10=878293, ADL=-4.92877e+07, close=272.6, EMA26=271.529 |
| v1 | roc_10_momentum | 9996.39 | -3.61 | sell /  / 10봉 ROC > 1% 그리고 종가 > EMA26; 조건 미충족; ROC10_percent=0.995963, close=275.315, EMA26=273.754 |
| v1 | trix_15_trend | 9937.79 | -62.21 | buy /  / 15봉 삼중 EMA의 1봉 변화율 TRIX > 0 그리고 종가 > EMA26; 조건 충족; TRIX15_percent=0.00296855, close=273.97, EMA26=271.9 |
| v1 | keltner_20_breakout | 9933.72 | -66.28 | sell /  / 종가 > EMA20 + 2 x Wilder ATR14; 조건 미충족; close=275.315, upper_Keltner=275.695, EMA20=274.153, ATR14=0.771306 |
| v1 | opening_range_30m | 9942.18 | -57.82 | buy /  / 뉴욕 09:30·09:45 두 완료 봉 최고가를 10:00 이후 종가가 돌파; 조건 충족; close=275.845, opening_high=274.33 |
| v2 | cash | 10000.00 | 0.00 | 대기 /  / 새 신호 대기 |
| v2 | buy_hold | 9879.23 | -120.77 | buy / partial / 직전 완료 봉 목표 비중 100%; 다음 봉 시가 가정 |
| v2 | trend_8_26 | 9660.85 | -339.15 | buy / partial / 직전 완료 봉 목표 비중 100%; 다음 봉 시가 가정 |
| v2 | momentum_26 | 9830.29 | -169.71 | buy / partial / 직전 완료 봉 목표 비중 100%; 다음 봉 시가 가정 |
| v2 | breakout_8 | 9329.18 | -670.82 | sell / filled / 직전 완료 봉 목표 비중 0%; 다음 봉 시가 가정 |
| v2 | reversion_12 | 9325.80 | -674.20 | sell / filled / 직전 완료 봉 목표 비중 0%; 다음 봉 시가 가정 |
| v2 | volume_26 | 9434.73 | -565.27 | sell / filled / 직전 완료 봉 목표 비중 0%; 다음 봉 시가 가정 |
| v2 | trend_8_26 AND momentum_26 | 9824.78 | -175.22 | buy / partial / 직전 완료 봉 목표 비중 100%; 다음 봉 시가 가정 |
| v2 | trend_8_26 + momentum_26 | 9765.89 | -234.11 | buy / partial / 직전 완료 봉 목표 비중 100%; 다음 봉 시가 가정 |
| v2 | trend_8_26 AND breakout_8 | 9710.34 | -289.66 | sell / filled / 직전 완료 봉 목표 비중 0%; 다음 봉 시가 가정 |
| v2 | trend_8_26 + breakout_8 | 9513.84 | -486.16 | sell / filled / 직전 완료 봉 목표 비중 50%; 다음 봉 시가 가정 |
| v2 | trend_8_26 AND reversion_12 | 9705.35 | -294.65 | sell / filled / 직전 완료 봉 목표 비중 0%; 다음 봉 시가 가정 |
| v2 | trend_8_26 + reversion_12 | 9491.59 | -508.41 | sell / filled / 직전 완료 봉 목표 비중 50%; 다음 봉 시가 가정 |
| v2 | trend_8_26 AND volume_26 | 9797.73 | -202.27 | sell / filled / 직전 완료 봉 목표 비중 0%; 다음 봉 시가 가정 |
| v2 | trend_8_26 + volume_26 | 9587.19 | -412.81 | sell / filled / 직전 완료 봉 목표 비중 50%; 다음 봉 시가 가정 |
| v2 | momentum_26 AND breakout_8 | 9653.24 | -346.76 | sell / filled / 직전 완료 봉 목표 비중 0%; 다음 봉 시가 가정 |
| v2 | momentum_26 + breakout_8 | 9596.77 | -403.23 | sell / filled / 직전 완료 봉 목표 비중 50%; 다음 봉 시가 가정 |
| v2 | momentum_26 AND reversion_12 | 9881.28 | -118.72 | sell / filled / 직전 완료 봉 목표 비중 0%; 다음 봉 시가 가정 |
| v2 | momentum_26 + reversion_12 | 9614.55 | -385.45 | sell / filled / 직전 완료 봉 목표 비중 50%; 다음 봉 시가 가정 |
| v2 | momentum_26 AND volume_26 | 9957.22 | -42.78 | sell / filled / 직전 완료 봉 목표 비중 0%; 다음 봉 시가 가정 |
| v2 | momentum_26 + volume_26 | 9630.16 | -369.84 | sell / filled / 직전 완료 봉 목표 비중 50%; 다음 봉 시가 가정 |
| v2 | breakout_8 AND reversion_12 | 10000.00 | 0.00 | 대기 /  / 새 신호 대기 |
| v2 | breakout_8 + reversion_12 | 9366.25 | -633.75 | sell / filled / 직전 완료 봉 목표 비중 0%; 다음 봉 시가 가정 |
| v2 | breakout_8 AND volume_26 | 9710.25 | -289.75 | sell / filled / 직전 완료 봉 목표 비중 0%; 다음 봉 시가 가정 |
| v2 | breakout_8 + volume_26 | 9421.20 | -578.80 | sell / filled / 직전 완료 봉 목표 비중 0%; 다음 봉 시가 가정 |
| v2 | reversion_12 AND volume_26 | 9676.46 | -323.54 | sell / filled / 직전 완료 봉 목표 비중 0%; 다음 봉 시가 가정 |
| v2 | reversion_12 + volume_26 | 9419.31 | -580.69 | sell / filled / 직전 완료 봉 목표 비중 0%; 다음 봉 시가 가정 |
| v2 | ema_12_26 | 9851.75 | -148.25 | buy / partial / EMA12 > EMA26; 조건 충족; EMA12=271.545, EMA26=271.529; 직전 완료 봉 목표를 다음 봉 시가에 모의 적용 |
| v2 | macd_12_26_9 | 9930.30 | -69.70 | buy / partial / MACD > 신호선 그리고 MACD > 0; 조건 충족; MACD=0.0161944, signal9=-0.0860005; 직전 완료 봉 목표를 다음 봉 시가에 모의 적용 |
| v2 | rsi_14_recovery | 9779.12 | -220.88 | sell / filled / 직전 RSI14 < 30, 현재 RSI14 >= 30 (한 봉 목표); 조건 미충족; RSI14=46.986, previous_RSI14=37.1649; 직전 완료 봉 목표를 다음 봉 시가에 모의 적용 |
| v2 | bollinger_20_reentry | 9920.06 | -79.94 | sell / filled / 직전 종가 < 직전 하단밴드, 현재 하단밴드 <= 종가 <= SMA20 (한 봉 목표); 조건 미충족; close=271.19, lower20=270.018, SMA20=273.224, previous_lower20=270.283; 직전 완료 봉 목표를 다음 봉 시가에 모의 적용 |
| v2 | donchian_20 | 9830.01 | -169.99 | sell / filled / 종가 > 현재 봉을 제외한 직전 20봉 최고가; 조건 미충족; close=275.785, prior_high20=276.875; 직전 완료 봉 목표를 다음 봉 시가에 모의 적용 |
| v2 | atr_14_breakout | 9876.04 | -123.96 | sell / filled / 종가 > 직전 종가 + 직전 ATR14 그리고 종가 > EMA26; 조건 미충족; close=276.33, threshold=276.592, prior_ATR14=0.747363, EMA26=272.499; 직전 완료 봉 목표를 다음 봉 시가에 모의 적용 |
| v2 | session_vwap | 9850.78 | -149.22 | buy / partial / 종가 > 뉴욕 거래일별 누적 전형가격 VWAP; 조건 충족; close=272.6, session_VWAP=272.22, session_volume=3.20722e+06; 직전 완료 봉 목표를 다음 봉 시가에 모의 적용 |
| v2 | obv_20 | 9842.18 | -157.82 | buy / partial / OBV > OBV의 SMA20 그리고 종가 > EMA26; 조건 충족; OBV=-2.88653e+07, OBV_SMA20=-3.02185e+07, close=272.6, EMA26=271.529; 직전 완료 봉 목표를 다음 봉 시가에 모의 적용 |
| v2 | stochastic_14_3_recovery | 9650.41 | -349.59 | sell / filled / 직전 %K14 < 20에서 %K14가 %D3 상향 돌파 (한 봉 목표); 조건 미충족; K14=72.727, D3=41.2922, previous_K14=34.0903, previous_D3=23.8263; 직전 완료 봉 목표를 다음 봉 시가에 모의 적용 |
| v2 | mfi_14_recovery | 9930.25 | -69.75 | sell / filled / 직전 MFI14 < 20, 현재 MFI14 >= 20 (한 봉 목표); 조건 미충족; MFI14=34.131, previous_MFI14=22.0435; 직전 완료 봉 목표를 다음 봉 시가에 모의 적용 |
| v2 | adx_14_trend | 9777.37 | -222.63 | buy / partial / Wilder ADX14 >= 25 그리고 +DI14 > -DI14; 조건 충족; ADX14=26.5262, plus_DI14=49.1478, minus_DI14=9.69634; 직전 완료 봉 목표를 다음 봉 시가에 모의 적용 |
| v2 | aroon_25_trend | 9826.26 | -173.74 | sell / filled / Aroon25 Up > 70 그리고 Down < 30 (동률이면 최신 극값); 조건 미충족; Aroon_up=100, Aroon_down=68; 직전 완료 봉 목표를 다음 봉 시가에 모의 적용 |
| v2 | cci_20_momentum | 9949.11 | -50.89 | sell / filled / CCI20 > 100 (전형가격·평균절대편차); 조건 미충족; CCI20=86.224; 직전 완료 봉 목표를 다음 봉 시가에 모의 적용 |
| v2 | williams_14_recovery | 9825.45 | -174.55 | sell / filled / 직전 Williams %R14 < -80, 현재 >= -80 (한 봉 목표); 조건 미충족; Williams_R14=-27.273, previous_R14=-65.9097; 직전 완료 봉 목표를 다음 봉 시가에 모의 적용 |
| v2 | cmf_20_accumulation | 9790.91 | -209.09 | buy / partial / Chaikin Money Flow20 > 0.1; 조건 충족; CMF20=0.208851, volume20=1.40263e+07; 직전 완료 봉 목표를 다음 봉 시가에 모의 적용 |
| v2 | chaikin_3_10 | 9843.07 | -156.93 | buy / partial / ADL의 EMA3 - EMA10 > 0 그리고 종가 > EMA26; 조건 충족; Chaikin3_10=878293, ADL=-4.92877e+07, close=272.6, EMA26=271.529; 직전 완료 봉 목표를 다음 봉 시가에 모의 적용 |
| v2 | roc_10_momentum | 9994.39 | -5.61 | sell / filled / 10봉 ROC > 1% 그리고 종가 > EMA26; 조건 미충족; ROC10_percent=0.995963, close=275.315, EMA26=273.754; 직전 완료 봉 목표를 다음 봉 시가에 모의 적용 |
| v2 | trix_15_trend | 9934.81 | -65.19 | buy / partial / 15봉 삼중 EMA의 1봉 변화율 TRIX > 0 그리고 종가 > EMA26; 조건 충족; TRIX15_percent=0.00296855, close=273.97, EMA26=271.9; 직전 완료 봉 목표를 다음 봉 시가에 모의 적용 |
| v2 | keltner_20_breakout | 9929.75 | -70.25 | sell / filled / 종가 > EMA20 + 2 x Wilder ATR14; 조건 미충족; close=275.315, upper_Keltner=275.695, EMA20=274.153, ATR14=0.771306; 직전 완료 봉 목표를 다음 봉 시가에 모의 적용 |
| v2 | opening_range_30m | 9939.19 | -60.81 | buy / partial / 뉴욕 09:30·09:45 두 완료 봉 최고가를 10:00 이후 종가가 돌파; 조건 충족; close=275.845, opening_high=274.33; 직전 완료 봉 목표를 다음 봉 시가에 모의 적용 |

### 같은 기간의 비용·노출 비교 (사후 연구)

| 전략 | 비용 전 | 비용 후 | 100% 보유 | 같은 평균 노출 보유 | 평균 노출 |
|---|---:|---:|---:|---:|---:|
| cash | 0.00% | 0.00% | -1.50% | -0.00% | 0.00% |
| buy_hold | -1.08% | -1.50% | -1.50% | -1.50% | 100.00% |
| trend_8_26 | -0.86% | -4.53% | -1.50% | -0.70% | 46.84% |
| momentum_26 | -0.76% | -6.42% | -1.50% | -0.67% | 44.47% |
| breakout_8 | -0.31% | -14.66% | -1.50% | -0.31% | 20.53% |
| reversion_12 | -2.15% | -13.73% | -1.50% | -0.42% | 27.89% |
| volume_26 | -1.61% | -8.78% | -1.50% | -0.13% | 8.68% |
| trend_8_26 AND momentum_26 | -0.78% | -5.26% | -1.50% | -0.57% | 37.63% |
| trend_8_26 + momentum_26 | -0.80% | -5.08% | -1.50% | -0.69% | 45.66% |
| trend_8_26 AND breakout_8 | -0.53% | -8.92% | -1.50% | -0.19% | 12.63% |
| trend_8_26 + breakout_8 | -0.57% | -9.55% | -1.50% | -0.51% | 33.69% |
| trend_8_26 AND reversion_12 | -0.74% | -4.82% | -1.50% | -0.08% | 5.53% |
| trend_8_26 + reversion_12 | -1.49% | -9.06% | -1.50% | -0.56% | 37.37% |
| trend_8_26 AND volume_26 | -0.98% | -3.85% | -1.50% | -0.04% | 2.63% |
| trend_8_26 + volume_26 | -1.22% | -6.29% | -1.50% | -0.42% | 27.77% |
| momentum_26 AND breakout_8 | 0.22% | -8.24% | -1.50% | -0.18% | 11.84% |
| momentum_26 + breakout_8 | -0.53% | -10.45% | -1.50% | -0.49% | 32.51% |
| momentum_26 AND reversion_12 | 0.03% | -3.68% | -1.50% | -0.06% | 3.68% |
| momentum_26 + reversion_12 | -1.44% | -9.21% | -1.50% | -0.54% | 36.19% |
| momentum_26 AND volume_26 | 0.06% | -2.02% | -1.50% | -0.03% | 1.84% |
| momentum_26 + volume_26 | -1.18% | -7.22% | -1.50% | -0.40% | 26.58% |
| breakout_8 AND reversion_12 | 0.00% | 0.00% | -1.50% | -0.00% | 0.00% |
| breakout_8 + reversion_12 | -1.23% | -13.66% | -1.50% | -0.36% | 24.22% |
| breakout_8 AND volume_26 | -0.84% | -4.11% | -1.50% | -0.04% | 2.63% |
| breakout_8 + volume_26 | -0.96% | -11.40% | -1.50% | -0.22% | 14.61% |
| reversion_12 AND volume_26 | -0.62% | -4.31% | -1.50% | -0.06% | 3.95% |
| reversion_12 + volume_26 | -1.87% | -10.73% | -1.50% | -0.28% | 18.30% |
| ema_12_26 | 0.90% | -2.02% | -1.50% | -0.70% | 46.32% |
| macd_12_26_9 | 2.69% | -0.29% | -1.50% | -0.47% | 31.05% |
| rsi_14_recovery | -0.65% | -5.14% | -1.50% | -0.04% | 2.89% |
| bollinger_20_reentry | -0.24% | -4.35% | -1.50% | -0.04% | 2.63% |
| donchian_20 | -0.34% | -6.04% | -1.50% | -0.10% | 6.58% |
| atr_14_breakout | -0.52% | -7.37% | -1.50% | -0.07% | 4.74% |
| session_vwap | 0.22% | -9.77% | -1.50% | -0.65% | 43.16% |
| obv_20 | 1.38% | -3.20% | -1.50% | -0.62% | 41.58% |
| stochastic_14_3_recovery | -0.44% | -12.96% | -1.50% | -0.13% | 8.42% |
| mfi_14_recovery | 0.36% | -4.17% | -1.50% | -0.04% | 2.89% |
| adx_14_trend | -0.39% | -4.08% | -1.50% | -0.49% | 32.89% |
| aroon_25_trend | -1.21% | -5.28% | -1.50% | -0.32% | 21.58% |
| cci_20_momentum | -0.89% | -7.72% | -1.50% | -0.31% | 20.79% |
| williams_14_recovery | -0.09% | -9.29% | -1.50% | -0.09% | 6.05% |
| cmf_20_accumulation | -0.78% | -8.00% | -1.50% | -0.32% | 21.32% |
| chaikin_3_10 | -0.76% | -7.60% | -1.50% | -0.52% | 34.47% |
| roc_10_momentum | -0.27% | -1.93% | -1.50% | -0.08% | 5.53% |
| trix_15_trend | 0.98% | -2.36% | -1.50% | -0.51% | 33.95% |
| keltner_20_breakout | -0.55% | -4.24% | -1.50% | -0.12% | 7.63% |
| opening_range_30m | 2.51% | -1.71% | -1.50% | -0.36% | 23.68% |

동일 구간·초기 자금, 종료 시 청산 비용 포함. 노출 맞춤은 사후 설명용이며 v2 실제 계좌 성과가 아닙니다.
[낙폭 분해·비용 영향·전체 구간](IWM/comparison.json)

[v1 전체 기록](IWM/accounts.json) · [v2 전체 기록](IWM/accounts-v2.json)

## DIA 계좌

| 모델 | 전략 | 평가액 USD | 손익 USD | 최근 매매·이유 |
|---|---|---:|---:|---|
| v1 | cash | 10000.00 | 0.00 | 대기 /  / 새 신호 대기 |
| v1 | buy_hold | 10000.64 | 0.64 | buy /  / buy_hold: prior completed bar target 100%; next bar open simulation |
| v1 | trend_8_26 | 9959.00 | -41.00 | buy /  / trend_8_26: prior completed bar target 100%; next bar open simulation |
| v1 | momentum_26 | 9855.20 | -144.80 | buy /  / momentum_26: prior completed bar target 100%; next bar open simulation |
| v1 | breakout_8 | 9693.16 | -306.84 | sell /  / breakout_8: prior completed bar target 0%; next bar open simulation |
| v1 | reversion_12 | 9897.27 | -102.73 | sell /  / reversion_12: prior completed bar target 0%; next bar open simulation |
| v1 | volume_26 | 9939.83 | -60.17 | sell /  / volume_26: prior completed bar target 0%; next bar open simulation |
| v1 | trend_8_26 AND momentum_26 | 9855.20 | -144.80 | buy /  / trend_8_26 AND momentum_26: prior completed bar target 100%; next bar open simulation |
| v1 | trend_8_26 + momentum_26 | 9907.05 | -92.95 | buy /  / trend_8_26 + momentum_26: prior completed bar target 100%; next bar open simulation |
| v1 | trend_8_26 AND breakout_8 | 9825.30 | -174.70 | sell /  / trend_8_26 AND breakout_8: prior completed bar target 0%; next bar open simulation |
| v1 | trend_8_26 + breakout_8 | 9844.89 | -155.11 | buy /  / trend_8_26 + breakout_8: prior completed bar target 50%; next bar open simulation |
| v1 | trend_8_26 AND reversion_12 | 9940.76 | -59.24 | sell /  / trend_8_26 AND reversion_12: prior completed bar target 0%; next bar open simulation |
| v1 | trend_8_26 + reversion_12 | 9927.96 | -72.04 | buy /  / trend_8_26 + reversion_12: prior completed bar target 50%; next bar open simulation |
| v1 | trend_8_26 AND volume_26 | 9974.09 | -25.91 | sell /  / trend_8_26 AND volume_26: prior completed bar target 0%; next bar open simulation |
| v1 | trend_8_26 + volume_26 | 9949.30 | -50.70 | buy /  / trend_8_26 + volume_26: prior completed bar target 50%; next bar open simulation |
| v1 | momentum_26 AND breakout_8 | 9825.30 | -174.70 | sell /  / momentum_26 AND breakout_8: prior completed bar target 0%; next bar open simulation |
| v1 | momentum_26 + breakout_8 | 9773.84 | -226.16 | buy /  / momentum_26 + breakout_8: prior completed bar target 50%; next bar open simulation |
| v1 | momentum_26 AND reversion_12 | 9940.78 | -59.22 | sell /  / momentum_26 AND reversion_12: prior completed bar target 0%; next bar open simulation |
| v1 | momentum_26 + reversion_12 | 9915.64 | -84.36 | buy /  / momentum_26 + reversion_12: prior completed bar target 50%; next bar open simulation |
| v1 | momentum_26 AND volume_26 | 9929.52 | -70.48 | sell /  / momentum_26 AND volume_26: prior completed bar target 0%; next bar open simulation |
| v1 | momentum_26 + volume_26 | 9917.17 | -82.83 | buy /  / momentum_26 + volume_26: prior completed bar target 50%; next bar open simulation |
| v1 | breakout_8 AND reversion_12 | 10000.00 | 0.00 | 대기 /  / 새 신호 대기 |
| v1 | breakout_8 + reversion_12 | 9814.18 | -185.82 | sell /  / breakout_8 + reversion_12: prior completed bar target 0%; next bar open simulation |
| v1 | breakout_8 AND volume_26 | 9986.25 | -13.75 | sell /  / breakout_8 AND volume_26: prior completed bar target 0%; next bar open simulation |
| v1 | breakout_8 + volume_26 | 9855.04 | -144.96 | sell /  / breakout_8 + volume_26: prior completed bar target 0%; next bar open simulation |
| v1 | reversion_12 AND volume_26 | 9970.42 | -29.58 | sell /  / reversion_12 AND volume_26: prior completed bar target 0%; next bar open simulation |
| v1 | reversion_12 + volume_26 | 9938.32 | -61.68 | sell /  / reversion_12 + volume_26: prior completed bar target 0%; next bar open simulation |
| v1 | ema_12_26 | 9855.43 | -144.57 | buy /  / EMA12 > EMA26; 조건 충족; EMA12=519.74, EMA26=519.585 |
| v1 | macd_12_26_9 | 9920.86 | -79.14 | buy /  / MACD > 신호선 그리고 MACD > 0; 조건 충족; MACD=0.154226, signal9=0.0227958 |
| v1 | rsi_14_recovery | 10000.00 | 0.00 | 대기 /  / 새 신호 대기 |
| v1 | bollinger_20_reentry | 9978.51 | -21.49 | sell /  / 직전 종가 < 직전 하단밴드, 현재 하단밴드 <= 종가 <= SMA20 (한 봉 목표); 조건 미충족; close=519.823, lower20=518.355, SMA20=521.612, previous_lower20=518.548 |
| v1 | donchian_20 | 9822.00 | -178.00 | sell /  / 종가 > 현재 봉을 제외한 직전 20봉 최고가; 조건 미충족; close=523.68, prior_high20=526.17 |
| v1 | atr_14_breakout | 9885.70 | -114.30 | sell /  / 종가 > 직전 종가 + 직전 ATR14 그리고 종가 > EMA26; 조건 미충족; close=525.49, threshold=525.841, prior_ATR14=0.980592, EMA26=520.815 |
| v1 | session_vwap | 9910.35 | -89.65 | buy /  / 종가 > 뉴욕 거래일별 누적 전형가격 VWAP; 조건 충족; close=521.46, session_VWAP=520.55, session_volume=446463 |
| v1 | obv_20 | 9861.69 | -138.31 | buy /  / OBV > OBV의 SMA20 그리고 종가 > EMA26; 조건 충족; OBV=-9.86891e+06, OBV_SMA20=-1.0028e+07, close=521.46, EMA26=519.585 |
| v1 | stochastic_14_3_recovery | 9821.00 | -179.00 | sell /  / 직전 %K14 < 20에서 %K14가 %D3 상향 돌파 (한 봉 목표); 조건 미충족; K14=100, D3=70.5235, previous_K14=91.7443, previous_D3=57.9113 |
| v1 | mfi_14_recovery | 9936.38 | -63.62 | sell /  / 직전 MFI14 < 20, 현재 MFI14 >= 20 (한 봉 목표); 조건 미충족; MFI14=44.8014, previous_MFI14=20.0271 |
| v1 | adx_14_trend | 9811.65 | -188.35 | sell /  / Wilder ADX14 >= 25 그리고 +DI14 > -DI14; 조건 미충족; ADX14=24.7281, plus_DI14=33.8838, minus_DI14=22.7145 |
| v1 | aroon_25_trend | 9928.84 | -71.16 | sell /  / Aroon25 Up > 70 그리고 Down < 30 (동률이면 최신 극값); 조건 미충족; Aroon_up=100, Aroon_down=80 |
| v1 | cci_20_momentum | 9915.48 | -84.52 | sell /  / CCI20 > 100 (전형가격·평균절대편차); 조건 미충족; CCI20=87.8356 |
| v1 | williams_14_recovery | 9854.30 | -145.70 | sell /  / 직전 Williams %R14 < -80, 현재 >= -80 (한 봉 목표); 조건 미충족; Williams_R14=0, previous_R14=-8.25572 |
| v1 | cmf_20_accumulation | 9811.95 | -188.05 | buy /  / Chaikin Money Flow20 > 0.1; 조건 충족; CMF20=0.237356, volume20=1.61808e+06 |
| v1 | chaikin_3_10 | 9863.60 | -136.40 | buy /  / ADL의 EMA3 - EMA10 > 0 그리고 종가 > EMA26; 조건 충족; Chaikin3_10=78733.3, ADL=-1.64223e+07, close=521.46, EMA26=519.585 |
| v1 | roc_10_momentum | 9939.01 | -60.99 | sell /  / 10봉 ROC > 1% 그리고 종가 > EMA26; 조건 미충족; ROC10_percent=0.771645, close=523.68, EMA26=521.367 |
| v1 | trix_15_trend | 9956.90 | -43.10 | buy /  / 15봉 삼중 EMA의 1봉 변화율 TRIX > 0 그리고 종가 > EMA26; 조건 충족; TRIX15_percent=0.000473967, close=521.46, EMA26=519.585 |
| v1 | keltner_20_breakout | 9944.49 | -55.51 | sell /  / 종가 > EMA20 + 2 x Wilder ATR14; 조건 미충족; close=523.68, upper_Keltner=523.985, EMA20=521.785, ATR14=1.10038 |
| v1 | opening_range_30m | 9794.44 | -205.56 | buy /  / 뉴욕 09:30·09:45 두 완료 봉 최고가를 10:00 이후 종가가 돌파; 조건 충족; close=524.86, opening_high=523.47 |
| v2 | cash | 10000.00 | 0.00 | 대기 /  / 새 신호 대기 |
| v2 | buy_hold | 10124.54 | 124.54 | buy / partial / 직전 완료 봉 목표 비중 100%; 다음 봉 시가 가정 |
| v2 | trend_8_26 | 9892.50 | -107.50 | buy / partial / 직전 완료 봉 목표 비중 100%; 다음 봉 시가 가정 |
| v2 | momentum_26 | 9893.07 | -106.93 | buy / partial / 직전 완료 봉 목표 비중 100%; 다음 봉 시가 가정 |
| v2 | breakout_8 | 9220.36 | -779.64 | sell / filled / 직전 완료 봉 목표 비중 0%; 다음 봉 시가 가정 |
| v2 | reversion_12 | 9592.64 | -407.36 | sell / filled / 직전 완료 봉 목표 비중 0%; 다음 봉 시가 가정 |
| v2 | volume_26 | 9652.01 | -347.99 | sell / filled / 직전 완료 봉 목표 비중 0%; 다음 봉 시가 가정 |
| v2 | trend_8_26 AND momentum_26 | 9888.48 | -111.52 | buy / partial / 직전 완료 봉 목표 비중 100%; 다음 봉 시가 가정 |
| v2 | trend_8_26 + momentum_26 | 9892.94 | -107.06 | buy / partial / 직전 완료 봉 목표 비중 100%; 다음 봉 시가 가정 |
| v2 | trend_8_26 AND breakout_8 | 9509.90 | -490.10 | sell / filled / 직전 완료 봉 목표 비중 0%; 다음 봉 시가 가정 |
| v2 | trend_8_26 + breakout_8 | 9570.70 | -429.30 | buy / filled / 직전 완료 봉 목표 비중 50%; 다음 봉 시가 가정 |
| v2 | trend_8_26 AND reversion_12 | 9748.75 | -251.25 | sell / filled / 직전 완료 봉 목표 비중 0%; 다음 봉 시가 가정 |
| v2 | trend_8_26 + reversion_12 | 9741.04 | -258.96 | buy / filled / 직전 완료 봉 목표 비중 50%; 다음 봉 시가 가정 |
| v2 | trend_8_26 AND volume_26 | 9827.44 | -172.56 | sell / filled / 직전 완료 봉 목표 비중 0%; 다음 봉 시가 가정 |
| v2 | trend_8_26 + volume_26 | 9791.89 | -208.11 | buy / filled / 직전 완료 봉 목표 비중 50%; 다음 봉 시가 가정 |
| v2 | momentum_26 AND breakout_8 | 9499.07 | -500.93 | sell / filled / 직전 완료 봉 목표 비중 0%; 다음 봉 시가 가정 |
| v2 | momentum_26 + breakout_8 | 9550.92 | -449.08 | buy / filled / 직전 완료 봉 목표 비중 50%; 다음 봉 시가 가정 |
| v2 | momentum_26 AND reversion_12 | 9895.03 | -104.97 | sell / filled / 직전 완료 봉 목표 비중 0%; 다음 봉 시가 가정 |
| v2 | momentum_26 + reversion_12 | 9782.36 | -217.64 | buy / filled / 직전 완료 봉 목표 비중 50%; 다음 봉 시가 가정 |
| v2 | momentum_26 AND volume_26 | 9716.58 | -283.42 | sell / filled / 직전 완료 봉 목표 비중 0%; 다음 봉 시가 가정 |
| v2 | momentum_26 + volume_26 | 9833.56 | -166.44 | buy / filled / 직전 완료 봉 목표 비중 50%; 다음 봉 시가 가정 |
| v2 | breakout_8 AND reversion_12 | 10000.00 | 0.00 | 대기 /  / 새 신호 대기 |
| v2 | breakout_8 + reversion_12 | 9423.89 | -576.11 | sell / filled / 직전 완료 봉 목표 비중 0%; 다음 봉 시가 가정 |
| v2 | breakout_8 AND volume_26 | 9781.13 | -218.87 | sell / filled / 직전 완료 봉 목표 비중 0%; 다음 봉 시가 가정 |
| v2 | breakout_8 + volume_26 | 9473.24 | -526.76 | sell / filled / 직전 완료 봉 목표 비중 0%; 다음 봉 시가 가정 |
| v2 | reversion_12 AND volume_26 | 9966.44 | -33.56 | sell / filled / 직전 완료 봉 목표 비중 0%; 다음 봉 시가 가정 |
| v2 | reversion_12 + volume_26 | 9642.17 | -357.83 | sell / filled / 직전 완료 봉 목표 비중 0%; 다음 봉 시가 가정 |
| v2 | ema_12_26 | 9850.50 | -149.50 | buy / partial / EMA12 > EMA26; 조건 충족; EMA12=519.74, EMA26=519.585; 직전 완료 봉 목표를 다음 봉 시가에 모의 적용 |
| v2 | macd_12_26_9 | 9915.90 | -84.10 | buy / partial / MACD > 신호선 그리고 MACD > 0; 조건 충족; MACD=0.154226, signal9=0.0227958; 직전 완료 봉 목표를 다음 봉 시가에 모의 적용 |
| v2 | rsi_14_recovery | 10000.00 | 0.00 | 대기 /  / 새 신호 대기 |
| v2 | bollinger_20_reentry | 9976.52 | -23.48 | sell / filled / 직전 종가 < 직전 하단밴드, 현재 하단밴드 <= 종가 <= SMA20 (한 봉 목표); 조건 미충족; close=519.823, lower20=518.355, SMA20=521.612, previous_lower20=518.548; 직전 완료 봉 목표를 다음 봉 시가에 모의 적용 |
| v2 | donchian_20 | 9814.14 | -185.86 | sell / filled / 종가 > 현재 봉을 제외한 직전 20봉 최고가; 조건 미충족; close=523.68, prior_high20=526.17; 직전 완료 봉 목표를 다음 봉 시가에 모의 적용 |
| v2 | atr_14_breakout | 9877.79 | -122.21 | sell / filled / 종가 > 직전 종가 + 직전 ATR14 그리고 종가 > EMA26; 조건 미충족; close=525.49, threshold=525.841, prior_ATR14=0.980592, EMA26=520.815; 직전 완료 봉 목표를 다음 봉 시가에 모의 적용 |
| v2 | session_vwap | 9903.42 | -96.58 | buy / partial / 종가 > 뉴욕 거래일별 누적 전형가격 VWAP; 조건 충족; close=521.46, session_VWAP=520.55, session_volume=446463; 직전 완료 봉 목표를 다음 봉 시가에 모의 적용 |
| v2 | obv_20 | 9854.79 | -145.21 | buy / partial / OBV > OBV의 SMA20 그리고 종가 > EMA26; 조건 충족; OBV=-9.86891e+06, OBV_SMA20=-1.0028e+07, close=521.46, EMA26=519.585; 직전 완료 봉 목표를 다음 봉 시가에 모의 적용 |
| v2 | stochastic_14_3_recovery | 9811.19 | -188.81 | sell / filled / 직전 %K14 < 20에서 %K14가 %D3 상향 돌파 (한 봉 목표); 조건 미충족; K14=100, D3=70.5235, previous_K14=91.7443, previous_D3=57.9113; 직전 완료 봉 목표를 다음 봉 시가에 모의 적용 |
| v2 | mfi_14_recovery | 9932.40 | -67.60 | sell / filled / 직전 MFI14 < 20, 현재 MFI14 >= 20 (한 봉 목표); 조건 미충족; MFI14=44.8014, previous_MFI14=20.0271; 직전 완료 봉 목표를 다음 봉 시가에 모의 적용 |
| v2 | adx_14_trend | 9805.77 | -194.23 | sell / filled / Wilder ADX14 >= 25 그리고 +DI14 > -DI14; 조건 미충족; ADX14=24.7281, plus_DI14=33.8838, minus_DI14=22.7145; 직전 완료 봉 목표를 다음 봉 시가에 모의 적용 |
| v2 | aroon_25_trend | 9922.89 | -77.11 | sell / filled / Aroon25 Up > 70 그리고 Down < 30 (동률이면 최신 극값); 조건 미충족; Aroon_up=100, Aroon_down=80; 직전 완료 봉 목표를 다음 봉 시가에 모의 적용 |
| v2 | cci_20_momentum | 9909.53 | -90.47 | sell / filled / CCI20 > 100 (전형가격·평균절대편차); 조건 미충족; CCI20=87.8356; 직전 완료 봉 목표를 다음 봉 시가에 모의 적용 |
| v2 | williams_14_recovery | 9846.42 | -153.58 | sell / filled / 직전 Williams %R14 < -80, 현재 >= -80 (한 봉 목표); 조건 미충족; Williams_R14=0, previous_R14=-8.25572; 직전 완료 봉 목표를 다음 봉 시가에 모의 적용 |
| v2 | cmf_20_accumulation | 9803.13 | -196.87 | buy / partial / Chaikin Money Flow20 > 0.1; 조건 충족; CMF20=0.237356, volume20=1.61808e+06; 직전 완료 봉 목표를 다음 봉 시가에 모의 적용 |
| v2 | chaikin_3_10 | 9856.70 | -143.30 | buy / partial / ADL의 EMA3 - EMA10 > 0 그리고 종가 > EMA26; 조건 충족; Chaikin3_10=78733.3, ADL=-1.64223e+07, close=521.46, EMA26=519.585; 직전 완료 봉 목표를 다음 봉 시가에 모의 적용 |
| v2 | roc_10_momentum | 9937.03 | -62.97 | sell / filled / 10봉 ROC > 1% 그리고 종가 > EMA26; 조건 미충족; ROC10_percent=0.771645, close=523.68, EMA26=521.367; 직전 완료 봉 목표를 다음 봉 시가에 모의 적용 |
| v2 | trix_15_trend | 9953.92 | -46.08 | buy / partial / 15봉 삼중 EMA의 1봉 변화율 TRIX > 0 그리고 종가 > EMA26; 조건 충족; TRIX15_percent=0.000473967, close=521.46, EMA26=519.585; 직전 완료 봉 목표를 다음 봉 시가에 모의 적용 |
| v2 | keltner_20_breakout | 9940.51 | -59.49 | sell / filled / 종가 > EMA20 + 2 x Wilder ATR14; 조건 미충족; close=523.68, upper_Keltner=523.985, EMA20=521.785, ATR14=1.10038; 직전 완료 봉 목표를 다음 봉 시가에 모의 적용 |
| v2 | opening_range_30m | 9785.63 | -214.37 | buy / partial / 뉴욕 09:30·09:45 두 완료 봉 최고가를 10:00 이후 종가가 돌파; 조건 충족; close=524.86, opening_high=523.47; 직전 완료 봉 목표를 다음 봉 시가에 모의 적용 |

### 같은 기간의 비용·노출 비교 (사후 연구)

| 전략 | 비용 전 | 비용 후 | 100% 보유 | 같은 평균 노출 보유 | 평균 노출 |
|---|---:|---:|---:|---:|---:|
| cash | 0.00% | 0.00% | 1.75% | 0.00% | 0.00% |
| buy_hold | 2.18% | 1.75% | 1.75% | 1.75% | 100.00% |
| trend_8_26 | 2.20% | -1.59% | 1.75% | 1.08% | 61.58% |
| momentum_26 | 0.76% | -3.79% | 1.75% | 0.98% | 56.05% |
| breakout_8 | 0.73% | -16.62% | 1.75% | 0.41% | 23.68% |
| reversion_12 | -0.58% | -8.59% | 1.75% | 0.39% | 22.37% |
| volume_26 | 0.22% | -9.77% | 1.75% | 0.19% | 11.05% |
| trend_8_26 AND momentum_26 | 1.87% | -2.73% | 1.75% | 0.89% | 50.79% |
| trend_8_26 + momentum_26 | 1.48% | -2.70% | 1.75% | 1.03% | 58.82% |
| trend_8_26 AND breakout_8 | 1.09% | -11.62% | 1.75% | 0.29% | 16.32% |
| trend_8_26 + breakout_8 | 1.46% | -9.04% | 1.75% | 0.75% | 42.64% |
| trend_8_26 AND reversion_12 | 0.43% | -4.91% | 1.75% | 0.12% | 6.84% |
| trend_8_26 + reversion_12 | 0.81% | -4.96% | 1.75% | 0.73% | 41.98% |
| trend_8_26 AND volume_26 | 1.48% | -4.32% | 1.75% | 0.11% | 6.05% |
| trend_8_26 + volume_26 | 1.21% | -5.58% | 1.75% | 0.63% | 36.32% |
| momentum_26 AND breakout_8 | 0.30% | -11.95% | 1.75% | 0.29% | 16.58% |
| momentum_26 + breakout_8 | 0.75% | -10.25% | 1.75% | 0.70% | 39.88% |
| momentum_26 AND reversion_12 | -0.27% | -3.57% | 1.75% | 0.10% | 5.79% |
| momentum_26 + reversion_12 | 0.09% | -5.24% | 1.75% | 0.69% | 39.21% |
| momentum_26 AND volume_26 | 0.10% | -5.62% | 1.75% | 0.10% | 5.53% |
| momentum_26 + volume_26 | 0.49% | -6.05% | 1.75% | 0.59% | 33.56% |
| breakout_8 AND reversion_12 | 0.00% | 0.00% | 1.75% | 0.00% | 0.00% |
| breakout_8 + reversion_12 | 0.08% | -12.34% | 1.75% | 0.40% | 23.04% |
| breakout_8 AND volume_26 | -0.47% | -3.75% | 1.75% | 0.06% | 3.16% |
| breakout_8 + volume_26 | 0.48% | -12.17% | 1.75% | 0.30% | 17.38% |
| reversion_12 AND volume_26 | 0.29% | -4.24% | 1.75% | 0.06% | 3.42% |
| reversion_12 + volume_26 | -0.18% | -9.00% | 1.75% | 0.29% | 16.72% |
| ema_12_26 | 0.56% | -2.35% | 1.75% | 0.93% | 53.42% |
| macd_12_26_9 | 2.05% | -1.74% | 1.75% | 0.56% | 32.11% |
| rsi_14_recovery | 0.16% | -1.09% | 1.75% | 0.01% | 0.79% |
| bollinger_20_reentry | 0.11% | -4.01% | 1.75% | 0.05% | 2.63% |
| donchian_20 | 0.36% | -6.94% | 1.75% | 0.17% | 9.74% |
| atr_14_breakout | -0.26% | -7.52% | 1.75% | 0.10% | 5.79% |
| session_vwap | 2.50% | -5.36% | 1.75% | 0.92% | 52.89% |
| obv_20 | 1.07% | -7.07% | 1.75% | 0.81% | 46.05% |
| stochastic_14_3_recovery | 0.95% | -11.00% | 1.75% | 0.14% | 7.89% |
| mfi_14_recovery | 0.16% | -3.15% | 1.75% | 0.04% | 2.11% |
| adx_14_trend | -0.13% | -4.23% | 1.75% | 0.58% | 33.42% |
| aroon_25_trend | 1.36% | -2.40% | 1.75% | 0.47% | 26.84% |
| cci_20_momentum | 1.05% | -5.51% | 1.75% | 0.46% | 26.58% |
| williams_14_recovery | 1.54% | -6.25% | 1.75% | 0.09% | 5.00% |
| cmf_20_accumulation | 1.49% | -6.29% | 1.75% | 0.53% | 30.53% |
| chaikin_3_10 | 2.28% | -7.14% | 1.75% | 0.80% | 45.53% |
| roc_10_momentum | -0.07% | -0.90% | 1.75% | 0.04% | 2.11% |
| trix_15_trend | 0.68% | -3.05% | 1.75% | 0.79% | 45.26% |
| keltner_20_breakout | 0.78% | -5.77% | 1.75% | 0.32% | 18.42% |
| opening_range_30m | 1.57% | -4.23% | 1.75% | 0.46% | 26.58% |

동일 구간·초기 자금, 종료 시 청산 비용 포함. 노출 맞춤은 사후 설명용이며 v2 실제 계좌 성과가 아닙니다.
[낙폭 분해·비용 영향·전체 구간](DIA/comparison.json)

[v1 전체 기록](DIA/accounts.json) · [v2 전체 기록](DIA/accounts-v2.json)

## MSFT 계좌

| 모델 | 전략 | 평가액 USD | 손익 USD | 최근 매매·이유 |
|---|---|---:|---:|---|
| v1 | cash | 10000.00 | 0.00 | 대기 /  / 새 신호 대기 |
| v1 | buy_hold | 9810.06 | -189.94 | buy /  / buy_hold: prior completed bar target 100%; next bar open simulation |
| v1 | trend_8_26 | 9677.44 | -322.56 | sell /  / trend_8_26: prior completed bar target 0%; next bar open simulation |
| v1 | momentum_26 | 9648.89 | -351.11 | sell /  / momentum_26: prior completed bar target 0%; next bar open simulation |
| v1 | breakout_8 | 9726.83 | -273.17 | buy /  / breakout_8: prior completed bar target 100%; next bar open simulation |
| v1 | reversion_12 | 9685.33 | -314.67 | sell /  / reversion_12: prior completed bar target 0%; next bar open simulation |
| v1 | volume_26 | 9811.31 | -188.69 | sell /  / volume_26: prior completed bar target 0%; next bar open simulation |
| v1 | trend_8_26 AND momentum_26 | 9662.97 | -337.03 | sell /  / trend_8_26 AND momentum_26: prior completed bar target 0%; next bar open simulation |
| v1 | trend_8_26 + momentum_26 | 9663.17 | -336.83 | sell /  / trend_8_26 + momentum_26: prior completed bar target 0%; next bar open simulation |
| v1 | trend_8_26 AND breakout_8 | 9820.11 | -179.89 | sell /  / trend_8_26 AND breakout_8: prior completed bar target 0%; next bar open simulation |
| v1 | trend_8_26 + breakout_8 | 9721.81 | -278.19 | buy /  / trend_8_26 + breakout_8: prior completed bar target 50%; next bar open simulation |
| v1 | trend_8_26 AND reversion_12 | 9721.64 | -278.36 | sell /  / trend_8_26 AND reversion_12: prior completed bar target 0%; next bar open simulation |
| v1 | trend_8_26 + reversion_12 | 9681.35 | -318.65 | sell /  / trend_8_26 + reversion_12: prior completed bar target 0%; next bar open simulation |
| v1 | trend_8_26 AND volume_26 | 9916.79 | -83.21 | sell /  / trend_8_26 AND volume_26: prior completed bar target 0%; next bar open simulation |
| v1 | trend_8_26 + volume_26 | 9744.38 | -255.62 | sell /  / trend_8_26 + volume_26: prior completed bar target 0%; next bar open simulation |
| v1 | momentum_26 AND breakout_8 | 9820.11 | -179.89 | sell /  / momentum_26 AND breakout_8: prior completed bar target 0%; next bar open simulation |
| v1 | momentum_26 + breakout_8 | 9688.05 | -311.95 | buy /  / momentum_26 + breakout_8: prior completed bar target 50%; next bar open simulation |
| v1 | momentum_26 AND reversion_12 | 9707.47 | -292.53 | sell /  / momentum_26 AND reversion_12: prior completed bar target 0%; next bar open simulation |
| v1 | momentum_26 + reversion_12 | 9667.06 | -332.94 | sell /  / momentum_26 + reversion_12: prior completed bar target 0%; next bar open simulation |
| v1 | momentum_26 AND volume_26 | 9916.79 | -83.21 | sell /  / momentum_26 AND volume_26: prior completed bar target 0%; next bar open simulation |
| v1 | momentum_26 + volume_26 | 9730.00 | -270.00 | sell /  / momentum_26 + volume_26: prior completed bar target 0%; next bar open simulation |
| v1 | breakout_8 AND reversion_12 | 10000.00 | 0.00 | 대기 /  / 새 신호 대기 |
| v1 | breakout_8 + reversion_12 | 9725.42 | -274.58 | buy /  / breakout_8 + reversion_12: prior completed bar target 50%; next bar open simulation |
| v1 | breakout_8 AND volume_26 | 9953.19 | -46.81 | sell /  / breakout_8 AND volume_26: prior completed bar target 0%; next bar open simulation |
| v1 | breakout_8 + volume_26 | 9788.40 | -211.60 | buy /  / breakout_8 + volume_26: prior completed bar target 50%; next bar open simulation |
| v1 | reversion_12 AND volume_26 | 9938.00 | -62.00 | sell /  / reversion_12 AND volume_26: prior completed bar target 0%; next bar open simulation |
| v1 | reversion_12 + volume_26 | 9748.10 | -251.90 | sell /  / reversion_12 + volume_26: prior completed bar target 0%; next bar open simulation |
| v1 | ema_12_26 | 9662.97 | -337.03 | sell /  / EMA12 > EMA26; 조건 미충족; EMA12=532.823, EMA26=532.897 |
| v1 | macd_12_26_9 | 9837.76 | -162.24 | sell /  / MACD > 신호선 그리고 MACD > 0; 조건 미충족; MACD=0.667719, signal9=0.675659 |
| v1 | rsi_14_recovery | 9957.14 | -42.86 | sell /  / 직전 RSI14 < 30, 현재 RSI14 >= 30 (한 봉 목표); 조건 미충족; RSI14=45.5102, previous_RSI14=37.5844 |
| v1 | bollinger_20_reentry | 9854.81 | -145.19 | sell /  / 직전 종가 < 직전 하단밴드, 현재 하단밴드 <= 종가 <= SMA20 (한 봉 목표); 조건 미충족; close=531.675, lower20=529.239, SMA20=533.058, previous_lower20=529.387 |
| v1 | donchian_20 | 9912.16 | -87.84 | sell /  / 종가 > 현재 봉을 제외한 직전 20봉 최고가; 조건 미충족; close=534.52, prior_high20=535.44 |
| v1 | atr_14_breakout | 9915.10 | -84.90 | sell /  / 종가 > 직전 종가 + 직전 ATR14 그리고 종가 > EMA26; 조건 미충족; close=533.975, threshold=536.307, prior_ATR14=2.16203, EMA26=530.521 |
| v1 | session_vwap | 9877.03 | -122.97 | buy /  / 종가 > 뉴욕 거래일별 누적 전형가격 VWAP; 조건 충족; close=529.315, session_VWAP=528.789, session_volume=2.32763e+06 |
| v1 | obv_20 | 9767.68 | -232.32 | sell /  / OBV > OBV의 SMA20 그리고 종가 > EMA26; 조건 미충족; OBV=9.27348e+07, OBV_SMA20=9.29669e+07, close=533.95, EMA26=532.788 |
| v1 | stochastic_14_3_recovery | 9789.03 | -210.97 | sell /  / 직전 %K14 < 20에서 %K14가 %D3 상향 돌파 (한 봉 목표); 조건 미충족; K14=60.6262, D3=34.5689, previous_K14=38.87, previous_D3=26.948 |
| v1 | mfi_14_recovery | 9972.58 | -27.42 | sell /  / 직전 MFI14 < 20, 현재 MFI14 >= 20 (한 봉 목표); 조건 미충족; MFI14=53.413, previous_MFI14=44.3372 |
| v1 | adx_14_trend | 9883.62 | -116.38 | sell /  / Wilder ADX14 >= 25 그리고 +DI14 > -DI14; 조건 미충족; ADX14=23.6824, plus_DI14=22.3066, minus_DI14=19.9214 |
| v1 | aroon_25_trend | 9812.47 | -187.53 | sell /  / Aroon25 Up > 70 그리고 Down < 30 (동률이면 최신 극값); 조건 미충족; Aroon_up=68, Aroon_down=20 |
| v1 | cci_20_momentum | 10012.15 | 12.15 | sell /  / CCI20 > 100 (전형가격·평균절대편차); 조건 미충족; CCI20=86.441 |
| v1 | williams_14_recovery | 9819.22 | -180.78 | sell /  / 직전 Williams %R14 < -80, 현재 >= -80 (한 봉 목표); 조건 미충족; Williams_R14=-39.3738, previous_R14=-61.13 |
| v1 | cmf_20_accumulation | 9741.38 | -258.62 | sell /  / Chaikin Money Flow20 > 0.1; 조건 미충족; CMF20=0.0660116, volume20=2.44678e+07 |
| v1 | chaikin_3_10 | 9777.77 | -222.23 | buy /  / ADL의 EMA3 - EMA10 > 0 그리고 종가 > EMA26; 조건 충족; Chaikin3_10=255579, ADL=1.10838e+08, close=532.15, EMA26=531.97 |
| v1 | roc_10_momentum | 9959.43 | -40.57 | sell /  / 10봉 ROC > 1% 그리고 종가 > EMA26; 조건 미충족; ROC10_percent=0.454191, close=534.125, EMA26=532.186 |
| v1 | trix_15_trend | 9712.42 | -287.58 | sell /  / 15봉 삼중 EMA의 1봉 변화율 TRIX > 0 그리고 종가 > EMA26; 조건 미충족; TRIX15_percent=0.0172213, close=526.676, EMA26=532.897 |
| v1 | keltner_20_breakout | 9958.78 | -41.22 | sell /  / 종가 > EMA20 + 2 x Wilder ATR14; 조건 미충족; close=533.975, upper_Keltner=534.357, EMA20=530.111, ATR14=2.12332 |
| v1 | opening_range_30m | 9711.79 | -288.21 | sell /  / 뉴욕 09:30·09:45 두 완료 봉 최고가를 10:00 이후 종가가 돌파; 자료 부족·변동폭 또는 거래량 없음: 대기; close=526.676 |
| v2 | cash | 10000.00 | 0.00 | 대기 /  / 새 신호 대기 |
| v2 | buy_hold | 9863.58 | -136.42 | buy / partial / 직전 완료 봉 목표 비중 100%; 다음 봉 시가 가정 |
| v2 | trend_8_26 | 9613.14 | -386.86 | sell / filled / 직전 완료 봉 목표 비중 0%; 다음 봉 시가 가정 |
| v2 | momentum_26 | 9692.90 | -307.10 | sell / filled / 직전 완료 봉 목표 비중 0%; 다음 봉 시가 가정 |
| v2 | breakout_8 | 9517.50 | -482.50 | buy / partial / 직전 완료 봉 목표 비중 100%; 다음 봉 시가 가정 |
| v2 | reversion_12 | 9308.50 | -691.50 | sell / filled / 직전 완료 봉 목표 비중 0%; 다음 봉 시가 가정 |
| v2 | volume_26 | 9498.13 | -501.87 | sell / filled / 직전 완료 봉 목표 비중 0%; 다음 봉 시가 가정 |
| v2 | trend_8_26 AND momentum_26 | 9560.49 | -439.51 | sell / filled / 직전 완료 봉 목표 비중 0%; 다음 봉 시가 가정 |
| v2 | trend_8_26 + momentum_26 | 9653.21 | -346.79 | sell / filled / 직전 완료 봉 목표 비중 0%; 다음 봉 시가 가정 |
| v2 | trend_8_26 AND breakout_8 | 9458.32 | -541.68 | sell / filled / 직전 완료 봉 목표 비중 0%; 다음 봉 시가 가정 |
| v2 | trend_8_26 + breakout_8 | 9605.94 | -394.06 | buy / filled / 직전 완료 봉 목표 비중 50%; 다음 봉 시가 가정 |
| v2 | trend_8_26 AND reversion_12 | 9618.75 | -381.25 | sell / filled / 직전 완료 봉 목표 비중 0%; 다음 봉 시가 가정 |
| v2 | trend_8_26 + reversion_12 | 9459.23 | -540.77 | sell / filled / 직전 완료 봉 목표 비중 0%; 다음 봉 시가 가정 |
| v2 | trend_8_26 AND volume_26 | 9861.94 | -138.06 | sell / filled / 직전 완료 봉 목표 비중 0%; 다음 봉 시가 가정 |
| v2 | trend_8_26 + volume_26 | 9575.59 | -424.41 | sell / filled / 직전 완료 봉 목표 비중 0%; 다음 봉 시가 가정 |
| v2 | momentum_26 AND breakout_8 | 9610.50 | -389.50 | sell / filled / 직전 완료 봉 목표 비중 0%; 다음 봉 시가 가정 |
| v2 | momentum_26 + breakout_8 | 9605.14 | -394.86 | buy / filled / 직전 완료 봉 목표 비중 50%; 다음 봉 시가 가정 |
| v2 | momentum_26 AND reversion_12 | 9533.70 | -466.30 | sell / filled / 직전 완료 봉 목표 비중 0%; 다음 봉 시가 가정 |
| v2 | momentum_26 + reversion_12 | 9498.52 | -501.48 | sell / filled / 직전 완료 봉 목표 비중 0%; 다음 봉 시가 가정 |
| v2 | momentum_26 AND volume_26 | 9785.21 | -214.79 | sell / filled / 직전 완료 봉 목표 비중 0%; 다음 봉 시가 가정 |
| v2 | momentum_26 + volume_26 | 9615.37 | -384.63 | sell / filled / 직전 완료 봉 목표 비중 0%; 다음 봉 시가 가정 |
| v2 | breakout_8 AND reversion_12 | 10000.00 | 0.00 | 대기 /  / 새 신호 대기 |
| v2 | breakout_8 + reversion_12 | 9451.74 | -548.26 | buy / filled / 직전 완료 봉 목표 비중 50%; 다음 봉 시가 가정 |
| v2 | breakout_8 AND volume_26 | 9890.09 | -109.91 | sell / filled / 직전 완료 봉 목표 비중 0%; 다음 봉 시가 가정 |
| v2 | breakout_8 + volume_26 | 9547.73 | -452.27 | buy / filled / 직전 완료 봉 목표 비중 50%; 다음 봉 시가 가정 |
| v2 | reversion_12 AND volume_26 | 9699.57 | -300.43 | sell / filled / 직전 완료 봉 목표 비중 0%; 다음 봉 시가 가정 |
| v2 | reversion_12 + volume_26 | 9402.66 | -597.34 | sell / filled / 직전 완료 봉 목표 비중 0%; 다음 봉 시가 가정 |
| v2 | ema_12_26 | 9659.11 | -340.89 | sell / filled / EMA12 > EMA26; 조건 미충족; EMA12=532.823, EMA26=532.897; 직전 완료 봉 목표를 다음 봉 시가에 모의 적용 |
| v2 | macd_12_26_9 | 9833.82 | -166.18 | sell / filled / MACD > 신호선 그리고 MACD > 0; 조건 미충족; MACD=0.667719, signal9=0.675659; 직전 완료 봉 목표를 다음 봉 시가에 모의 적용 |
| v2 | rsi_14_recovery | 9951.17 | -48.83 | sell / filled / 직전 RSI14 < 30, 현재 RSI14 >= 30 (한 봉 목표); 조건 미충족; RSI14=45.5102, previous_RSI14=37.5844; 직전 완료 봉 목표를 다음 봉 시가에 모의 적용 |
| v2 | bollinger_20_reentry | 9848.90 | -151.10 | sell / filled / 직전 종가 < 직전 하단밴드, 현재 하단밴드 <= 종가 <= SMA20 (한 봉 목표); 조건 미충족; close=531.675, lower20=529.239, SMA20=533.058, previous_lower20=529.387; 직전 완료 봉 목표를 다음 봉 시가에 모의 적용 |
| v2 | donchian_20 | 9908.19 | -91.81 | sell / filled / 종가 > 현재 봉을 제외한 직전 20봉 최고가; 조건 미충족; close=534.52, prior_high20=535.44; 직전 완료 봉 목표를 다음 봉 시가에 모의 적용 |
| v2 | atr_14_breakout | 9911.14 | -88.86 | sell / filled / 종가 > 직전 종가 + 직전 ATR14 그리고 종가 > EMA26; 조건 미충족; close=533.975, threshold=536.307, prior_ATR14=2.16203, EMA26=530.521; 직전 완료 봉 목표를 다음 봉 시가에 모의 적용 |
| v2 | session_vwap | 9870.12 | -129.88 | buy / partial / 종가 > 뉴욕 거래일별 누적 전형가격 VWAP; 조건 충족; close=529.315, session_VWAP=528.789, session_volume=2.32763e+06; 직전 완료 봉 목표를 다음 봉 시가에 모의 적용 |
| v2 | obv_20 | 9759.87 | -240.13 | sell / filled / OBV > OBV의 SMA20 그리고 종가 > EMA26; 조건 미충족; OBV=1.08325e+08, OBV_SMA20=1.08557e+08, close=533.95, EMA26=532.788; 직전 완료 봉 목표를 다음 봉 시가에 모의 적용 |
| v2 | stochastic_14_3_recovery | 9779.25 | -220.75 | sell / filled / 직전 %K14 < 20에서 %K14가 %D3 상향 돌파 (한 봉 목표); 조건 미충족; K14=60.6262, D3=34.5689, previous_K14=38.87, previous_D3=26.948; 직전 완료 봉 목표를 다음 봉 시가에 모의 적용 |
| v2 | mfi_14_recovery | 9968.59 | -31.41 | sell / filled / 직전 MFI14 < 20, 현재 MFI14 >= 20 (한 봉 목표); 조건 미충족; MFI14=53.413, previous_MFI14=44.3372; 직전 완료 봉 목표를 다음 봉 시가에 모의 적용 |
| v2 | adx_14_trend | 9879.67 | -120.33 | sell / filled / Wilder ADX14 >= 25 그리고 +DI14 > -DI14; 조건 미충족; ADX14=23.6824, plus_DI14=22.3066, minus_DI14=19.9214; 직전 완료 봉 목표를 다음 봉 시가에 모의 적용 |
| v2 | aroon_25_trend | 9808.55 | -191.45 | sell / filled / Aroon25 Up > 70 그리고 Down < 30 (동률이면 최신 극값); 조건 미충족; Aroon_up=68, Aroon_down=20; 직전 완료 봉 목표를 다음 봉 시가에 모의 적용 |
| v2 | cci_20_momentum | 10010.15 | 10.15 | sell / filled / CCI20 > 100 (전형가격·평균절대편차); 조건 미충족; CCI20=86.441; 직전 완료 봉 목표를 다음 봉 시가에 모의 적용 |
| v2 | williams_14_recovery | 9811.37 | -188.63 | sell / filled / 직전 Williams %R14 < -80, 현재 >= -80 (한 봉 목표); 조건 미충족; Williams_R14=-39.3738, previous_R14=-61.13; 직전 완료 봉 목표를 다음 봉 시가에 모의 적용 |
| v2 | cmf_20_accumulation | 9737.48 | -262.52 | sell / filled / Chaikin Money Flow20 > 0.1; 조건 미충족; CMF20=0.0660116, volume20=2.44678e+07; 직전 완료 봉 목표를 다음 봉 시가에 모의 적용 |
| v2 | chaikin_3_10 | 9770.93 | -229.07 | buy / partial / ADL의 EMA3 - EMA10 > 0 그리고 종가 > EMA26; 조건 충족; Chaikin3_10=255579, ADL=1.10838e+08, close=532.15, EMA26=531.97; 직전 완료 봉 목표를 다음 봉 시가에 모의 적용 |
| v2 | roc_10_momentum | 9957.44 | -42.56 | sell / filled / 10봉 ROC > 1% 그리고 종가 > EMA26; 조건 미충족; ROC10_percent=0.454191, close=534.125, EMA26=532.186; 직전 완료 봉 목표를 다음 봉 시가에 모의 적용 |
| v2 | trix_15_trend | 9708.54 | -291.46 | sell / filled / 15봉 삼중 EMA의 1봉 변화율 TRIX > 0 그리고 종가 > EMA26; 조건 미충족; TRIX15_percent=0.0172213, close=526.676, EMA26=532.897; 직전 완료 봉 목표를 다음 봉 시가에 모의 적용 |
| v2 | keltner_20_breakout | 9956.78 | -43.22 | sell / filled / 종가 > EMA20 + 2 x Wilder ATR14; 조건 미충족; close=533.975, upper_Keltner=534.357, EMA20=530.111, ATR14=2.12332; 직전 완료 봉 목표를 다음 봉 시가에 모의 적용 |
| v2 | opening_range_30m | 9707.90 | -292.10 | sell / filled / 뉴욕 09:30·09:45 두 완료 봉 최고가를 10:00 이후 종가가 돌파; 자료 부족·변동폭 또는 거래량 없음: 대기; close=526.676; 직전 완료 봉 목표를 다음 봉 시가에 모의 적용 |

### 같은 기간의 비용·노출 비교 (사후 연구)

| 전략 | 비용 전 | 비용 후 | 100% 보유 | 같은 평균 노출 보유 | 평균 노출 |
|---|---:|---:|---:|---:|---:|
| cash | 0.00% | 0.00% | 3.70% | 0.00% | 0.00% |
| buy_hold | 4.14% | 3.70% | 3.70% | 3.70% | 100.00% |
| trend_8_26 | 1.11% | -2.23% | 3.70% | 2.19% | 60.00% |
| momentum_26 | 0.23% | -5.10% | 3.70% | 2.25% | 61.58% |
| breakout_8 | 6.11% | -9.16% | 3.70% | 0.74% | 20.53% |
| reversion_12 | -4.30% | -12.75% | 3.70% | 0.86% | 23.95% |
| volume_26 | 1.03% | -7.11% | 3.70% | 0.30% | 8.42% |
| trend_8_26 AND momentum_26 | -0.98% | -6.64% | 3.70% | 2.03% | 55.79% |
| trend_8_26 + momentum_26 | 0.67% | -3.66% | 3.70% | 2.22% | 60.79% |
| trend_8_26 AND breakout_8 | 0.46% | -10.69% | 3.70% | 0.49% | 13.68% |
| trend_8_26 + breakout_8 | 3.60% | -5.16% | 3.70% | 1.46% | 40.27% |
| trend_8_26 AND reversion_12 | -1.41% | -7.04% | 3.70% | 0.25% | 6.84% |
| trend_8_26 + reversion_12 | -1.62% | -7.45% | 3.70% | 1.52% | 41.98% |
| trend_8_26 AND volume_26 | 3.42% | -0.42% | 3.70% | 0.11% | 3.16% |
| trend_8_26 + volume_26 | 1.08% | -4.10% | 3.70% | 1.24% | 34.21% |
| momentum_26 AND breakout_8 | 2.74% | -8.66% | 3.70% | 0.49% | 13.68% |
| momentum_26 + breakout_8 | 3.14% | -6.76% | 3.70% | 1.49% | 41.06% |
| momentum_26 AND reversion_12 | -2.41% | -9.14% | 3.70% | 0.35% | 9.74% |
| momentum_26 + reversion_12 | -2.04% | -9.01% | 3.70% | 1.55% | 42.77% |
| momentum_26 AND volume_26 | 1.07% | -3.49% | 3.70% | 0.13% | 3.68% |
| momentum_26 + volume_26 | 0.65% | -5.31% | 3.70% | 1.27% | 35.00% |
| breakout_8 AND reversion_12 | 0.00% | 0.00% | 3.70% | 0.00% | 0.00% |
| breakout_8 + reversion_12 | 0.79% | -10.22% | 3.70% | 0.80% | 22.24% |
| breakout_8 AND volume_26 | 2.04% | -0.50% | 3.70% | 0.07% | 1.84% |
| breakout_8 + volume_26 | 3.55% | -7.17% | 3.70% | 0.52% | 14.48% |
| reversion_12 AND volume_26 | -2.90% | -6.11% | 3.70% | 0.12% | 3.42% |
| reversion_12 + volume_26 | -1.66% | -9.97% | 3.70% | 0.58% | 16.19% |
| ema_12_26 | 0.23% | -3.08% | 3.70% | 2.27% | 62.11% |
| macd_12_26_9 | 1.20% | -3.77% | 3.70% | 1.27% | 35.00% |
| rsi_14_recovery | 0.31% | -2.19% | 3.70% | 0.06% | 1.58% |
| bollinger_20_reentry | -0.92% | -3.79% | 3.70% | 0.07% | 1.84% |
| donchian_20 | 1.76% | -4.05% | 3.70% | 0.18% | 5.00% |
| atr_14_breakout | 1.72% | -3.69% | 3.70% | 0.13% | 3.68% |
| session_vwap | 7.07% | -1.15% | 3.70% | 1.52% | 41.84% |
| obv_20 | 5.54% | -2.56% | 3.70% | 1.77% | 48.68% |
| stochastic_14_3_recovery | -0.50% | -10.42% | 3.70% | 0.24% | 6.58% |
| mfi_14_recovery | 1.58% | -2.19% | 3.70% | 0.08% | 2.37% |
| adx_14_trend | 3.84% | 1.26% | 3.70% | 1.69% | 46.58% |
| aroon_25_trend | 0.07% | -4.85% | 3.70% | 0.83% | 22.89% |
| cci_20_momentum | 3.31% | -3.40% | 3.70% | 0.82% | 22.63% |
| williams_14_recovery | -1.26% | -9.97% | 3.70% | 0.21% | 5.79% |
| cmf_20_accumulation | 0.70% | -4.65% | 3.70% | 1.19% | 32.89% |
| chaikin_3_10 | 4.33% | -3.67% | 3.70% | 1.68% | 46.32% |
| roc_10_momentum | -0.01% | -4.12% | 3.70% | 0.57% | 15.79% |
| trix_15_trend | -0.85% | -4.93% | 3.70% | 1.82% | 50.00% |
| keltner_20_breakout | 1.11% | -4.26% | 3.70% | 0.49% | 13.68% |
| opening_range_30m | -1.07% | -4.74% | 3.70% | 0.83% | 23.16% |

동일 구간·초기 자금, 종료 시 청산 비용 포함. 노출 맞춤은 사후 설명용이며 v2 실제 계좌 성과가 아닙니다.
[낙폭 분해·비용 영향·전체 구간](MSFT/comparison.json)

[v1 전체 기록](MSFT/accounts.json) · [v2 전체 기록](MSFT/accounts-v2.json)

## JPM 계좌

| 모델 | 전략 | 평가액 USD | 손익 USD | 최근 매매·이유 |
|---|---|---:|---:|---|
| v1 | cash | 10000.00 | 0.00 | 대기 /  / 새 신호 대기 |
| v1 | buy_hold | 9852.75 | -147.25 | buy /  / buy_hold: prior completed bar target 100%; next bar open simulation |
| v1 | trend_8_26 | 9804.45 | -195.55 | buy /  / trend_8_26: prior completed bar target 100%; next bar open simulation |
| v1 | momentum_26 | 9706.33 | -293.67 | sell /  / momentum_26: prior completed bar target 0%; next bar open simulation |
| v1 | breakout_8 | 9759.46 | -240.54 | sell /  / breakout_8: prior completed bar target 0%; next bar open simulation |
| v1 | reversion_12 | 9738.47 | -261.53 | buy /  / reversion_12: prior completed bar target 100%; next bar open simulation |
| v1 | volume_26 | 9961.97 | -38.03 | sell /  / volume_26: prior completed bar target 0%; next bar open simulation |
| v1 | trend_8_26 AND momentum_26 | 9793.49 | -206.51 | sell /  / trend_8_26 AND momentum_26: prior completed bar target 0%; next bar open simulation |
| v1 | trend_8_26 + momentum_26 | 9755.27 | -244.73 | sell /  / trend_8_26 + momentum_26: prior completed bar target 50%; next bar open simulation |
| v1 | trend_8_26 AND breakout_8 | 9915.55 | -84.45 | sell /  / trend_8_26 AND breakout_8: prior completed bar target 0%; next bar open simulation |
| v1 | trend_8_26 + breakout_8 | 9801.53 | -198.47 | buy /  / trend_8_26 + breakout_8: prior completed bar target 50%; next bar open simulation |
| v1 | trend_8_26 AND reversion_12 | 9874.03 | -125.97 | buy /  / trend_8_26 AND reversion_12: prior completed bar target 100%; next bar open simulation |
| v1 | trend_8_26 + reversion_12 | 9771.31 | -228.69 | buy /  / trend_8_26 + reversion_12: prior completed bar target 100%; next bar open simulation |
| v1 | trend_8_26 AND volume_26 | 10035.68 | 35.68 | sell /  / trend_8_26 AND volume_26: prior completed bar target 0%; next bar open simulation |
| v1 | trend_8_26 + volume_26 | 9882.75 | -117.25 | buy /  / trend_8_26 + volume_26: prior completed bar target 50%; next bar open simulation |
| v1 | momentum_26 AND breakout_8 | 9733.77 | -266.23 | sell /  / momentum_26 AND breakout_8: prior completed bar target 0%; next bar open simulation |
| v1 | momentum_26 + breakout_8 | 9732.95 | -267.05 | sell /  / momentum_26 + breakout_8: prior completed bar target 0%; next bar open simulation |
| v1 | momentum_26 AND reversion_12 | 9881.87 | -118.13 | sell /  / momentum_26 AND reversion_12: prior completed bar target 0%; next bar open simulation |
| v1 | momentum_26 + reversion_12 | 9761.29 | -238.71 | sell /  / momentum_26 + reversion_12: prior completed bar target 50%; next bar open simulation |
| v1 | momentum_26 AND volume_26 | 10035.68 | 35.68 | sell /  / momentum_26 AND volume_26: prior completed bar target 0%; next bar open simulation |
| v1 | momentum_26 + volume_26 | 9852.93 | -147.07 | sell /  / momentum_26 + volume_26: prior completed bar target 0%; next bar open simulation |
| v1 | breakout_8 AND reversion_12 | 10000.00 | 0.00 | 대기 /  / 새 신호 대기 |
| v1 | breakout_8 + reversion_12 | 9787.94 | -212.06 | buy /  / breakout_8 + reversion_12: prior completed bar target 50%; next bar open simulation |
| v1 | breakout_8 AND volume_26 | 10022.00 | 22.00 | sell /  / breakout_8 AND volume_26: prior completed bar target 0%; next bar open simulation |
| v1 | breakout_8 + volume_26 | 9860.16 | -139.84 | sell /  / breakout_8 + volume_26: prior completed bar target 0%; next bar open simulation |
| v1 | reversion_12 AND volume_26 | 9940.10 | -59.90 | sell /  / reversion_12 AND volume_26: prior completed bar target 0%; next bar open simulation |
| v1 | reversion_12 + volume_26 | 9869.23 | -130.77 | buy /  / reversion_12 + volume_26: prior completed bar target 50%; next bar open simulation |
| v1 | ema_12_26 | 9755.41 | -244.59 | sell /  / EMA12 > EMA26; 조건 미충족; EMA12=336.517, EMA26=336.551 |
| v1 | macd_12_26_9 | 9839.10 | -160.90 | sell /  / MACD > 신호선 그리고 MACD > 0; 조건 미충족; MACD=-0.0344827, signal9=-0.0504891 |
| v1 | rsi_14_recovery | 9986.37 | -13.63 | sell /  / 직전 RSI14 < 30, 현재 RSI14 >= 30 (한 봉 목표); 조건 미충족; RSI14=61.6663, previous_RSI14=57.046 |
| v1 | bollinger_20_reentry | 9964.67 | -35.33 | sell /  / 직전 종가 < 직전 하단밴드, 현재 하단밴드 <= 종가 <= SMA20 (한 봉 목표); 조건 미충족; close=336.53, lower20=336.046, SMA20=337.886, previous_lower20=336.231 |
| v1 | donchian_20 | 9830.85 | -169.15 | sell /  / 종가 > 현재 봉을 제외한 직전 20봉 최고가; 조건 미충족; close=339.04, prior_high20=339.42 |
| v1 | atr_14_breakout | 9746.56 | -253.44 | sell /  / 종가 > 직전 종가 + 직전 ATR14 그리고 종가 > EMA26; 조건 미충족; close=339.04, threshold=340.465, prior_ATR14=1.34545, EMA26=336.613 |
| v1 | session_vwap | 9727.57 | -272.43 | sell /  / 종가 > 뉴욕 거래일별 누적 전형가격 VWAP; 조건 미충족; close=336.08, session_VWAP=337.149, session_volume=2.04555e+06 |
| v1 | obv_20 | 10007.55 | 7.55 | sell /  / OBV > OBV의 SMA20 그리고 종가 > EMA26; 조건 미충족; OBV=-1.60234e+07, OBV_SMA20=-1.31788e+07, close=341.625, EMA26=338.807 |
| v1 | stochastic_14_3_recovery | 9718.50 | -281.50 | sell /  / 직전 %K14 < 20에서 %K14가 %D3 상향 돌파 (한 봉 목표); 조건 미충족; K14=11.111, D3=10.514, previous_K14=15.4166, previous_D3=10.08 |
| v1 | mfi_14_recovery | 9935.64 | -64.36 | sell /  / 직전 MFI14 < 20, 현재 MFI14 >= 20 (한 봉 목표); 조건 미충족; MFI14=30.2719, previous_MFI14=26.8492 |
| v1 | adx_14_trend | 9726.68 | -273.32 | sell /  / Wilder ADX14 >= 25 그리고 +DI14 > -DI14; 조건 미충족; ADX14=23.9395, plus_DI14=23.2021, minus_DI14=22.594 |
| v1 | aroon_25_trend | 9824.71 | -175.29 | sell /  / Aroon25 Up > 70 그리고 Down < 30 (동률이면 최신 극값); 조건 미충족; Aroon_up=68, Aroon_down=16 |
| v1 | cci_20_momentum | 9950.54 | -49.46 | sell /  / CCI20 > 100 (전형가격·평균절대편차); 조건 미충족; CCI20=28.4392 |
| v1 | williams_14_recovery | 9820.43 | -179.57 | sell /  / 직전 Williams %R14 < -80, 현재 >= -80 (한 봉 목표); 조건 미충족; Williams_R14=-13.9552, previous_R14=-4.5732 |
| v1 | cmf_20_accumulation | 9906.86 | -93.14 | buy /  / Chaikin Money Flow20 > 0.1; 조건 충족; CMF20=0.104274, volume20=4.03831e+06 |
| v1 | chaikin_3_10 | 9837.22 | -162.78 | sell /  / ADL의 EMA3 - EMA10 > 0 그리고 종가 > EMA26; 조건 미충족; Chaikin3_10=7273.89, ADL=-1.28498e+07, close=336.08, EMA26=336.65 |
| v1 | roc_10_momentum | 9836.40 | -163.60 | sell /  / 10봉 ROC > 1% 그리고 종가 > EMA26; 조건 미충족; ROC10_percent=0.964142, close=337.72, EMA26=336.695 |
| v1 | trix_15_trend | 9723.73 | -276.27 | sell /  / 15봉 삼중 EMA의 1봉 변화율 TRIX > 0 그리고 종가 > EMA26; 조건 미충족; TRIX15_percent=0.0135144, close=337.6, EMA26=338.759 |
| v1 | keltner_20_breakout | 9905.24 | -94.76 | sell /  / 종가 > EMA20 + 2 x Wilder ATR14; 조건 미충족; close=339.04, upper_Keltner=339.281, EMA20=336.559, ATR14=1.36146 |
| v1 | opening_range_30m | 9850.26 | -149.74 | sell /  / 뉴욕 09:30·09:45 두 완료 봉 최고가를 10:00 이후 종가가 돌파; 조건 미충족; close=337.72, opening_high=339.035 |
| v2 | cash | 10000.00 | 0.00 | 대기 /  / 새 신호 대기 |
| v2 | buy_hold | 10017.39 | 17.39 | buy / partial / 직전 완료 봉 목표 비중 100%; 다음 봉 시가 가정 |
| v2 | trend_8_26 | 9810.51 | -189.49 | buy / partial / 직전 완료 봉 목표 비중 100%; 다음 봉 시가 가정 |
| v2 | momentum_26 | 9219.07 | -780.93 | sell / filled / 직전 완료 봉 목표 비중 0%; 다음 봉 시가 가정 |
| v2 | breakout_8 | 9100.10 | -899.90 | sell / filled / 직전 완료 봉 목표 비중 0%; 다음 봉 시가 가정 |
| v2 | reversion_12 | 9714.12 | -285.88 | buy / partial / 직전 완료 봉 목표 비중 100%; 다음 봉 시가 가정 |
| v2 | volume_26 | 9781.50 | -218.50 | sell / filled / 직전 완료 봉 목표 비중 0%; 다음 봉 시가 가정 |
| v2 | trend_8_26 AND momentum_26 | 9756.41 | -243.59 | sell / filled / 직전 완료 봉 목표 비중 0%; 다음 봉 시가 가정 |
| v2 | trend_8_26 + momentum_26 | 9530.72 | -469.28 | sell / filled / 직전 완료 봉 목표 비중 50%; 다음 봉 시가 가정 |
| v2 | trend_8_26 AND breakout_8 | 9287.76 | -712.24 | sell / filled / 직전 완료 봉 목표 비중 0%; 다음 봉 시가 가정 |
| v2 | trend_8_26 + breakout_8 | 9469.56 | -530.44 | buy / filled / 직전 완료 봉 목표 비중 50%; 다음 봉 시가 가정 |
| v2 | trend_8_26 AND reversion_12 | 9850.94 | -149.06 | buy / partial / 직전 완료 봉 목표 비중 100%; 다음 봉 시가 가정 |
| v2 | trend_8_26 + reversion_12 | 9803.39 | -196.61 | buy / partial / 직전 완료 봉 목표 비중 100%; 다음 봉 시가 가정 |
| v2 | trend_8_26 AND volume_26 | 9833.30 | -166.70 | sell / filled / 직전 완료 봉 목표 비중 0%; 다음 봉 시가 가정 |
| v2 | trend_8_26 + volume_26 | 9796.67 | -203.33 | buy / filled / 직전 완료 봉 목표 비중 50%; 다음 봉 시가 가정 |
| v2 | momentum_26 AND breakout_8 | 9058.00 | -942.00 | sell / filled / 직전 완료 봉 목표 비중 0%; 다음 봉 시가 가정 |
| v2 | momentum_26 + breakout_8 | 9180.31 | -819.69 | sell / filled / 직전 완료 봉 목표 비중 0%; 다음 봉 시가 가정 |
| v2 | momentum_26 AND reversion_12 | 9827.31 | -172.69 | sell / filled / 직전 완료 봉 목표 비중 0%; 다음 봉 시가 가정 |
| v2 | momentum_26 + reversion_12 | 9624.17 | -375.83 | sell / filled / 직전 완료 봉 목표 비중 50%; 다음 봉 시가 가정 |
| v2 | momentum_26 AND volume_26 | 9833.30 | -166.70 | sell / filled / 직전 완료 봉 목표 비중 0%; 다음 봉 시가 가정 |
| v2 | momentum_26 + volume_26 | 9577.38 | -422.62 | sell / filled / 직전 완료 봉 목표 비중 0%; 다음 봉 시가 가정 |
| v2 | breakout_8 AND reversion_12 | 10000.00 | 0.00 | 대기 /  / 새 신호 대기 |
| v2 | breakout_8 + reversion_12 | 9481.53 | -518.47 | buy / filled / 직전 완료 봉 목표 비중 50%; 다음 봉 시가 가정 |
| v2 | breakout_8 AND volume_26 | 9911.14 | -88.86 | sell / filled / 직전 완료 봉 목표 비중 0%; 다음 봉 시가 가정 |
| v2 | breakout_8 + volume_26 | 9454.59 | -545.41 | sell / filled / 직전 완료 봉 목표 비중 0%; 다음 봉 시가 가정 |
| v2 | reversion_12 AND volume_26 | 9987.18 | -12.82 | sell / filled / 직전 완료 봉 목표 비중 0%; 다음 봉 시가 가정 |
| v2 | reversion_12 + volume_26 | 9788.97 | -211.03 | buy / filled / 직전 완료 봉 목표 비중 50%; 다음 봉 시가 가정 |
| v2 | ema_12_26 | 9751.51 | -248.49 | sell / filled / EMA12 > EMA26; 조건 미충족; EMA12=336.517, EMA26=336.551; 직전 완료 봉 목표를 다음 봉 시가에 모의 적용 |
| v2 | macd_12_26_9 | 9835.16 | -164.84 | sell / filled / MACD > 신호선 그리고 MACD > 0; 조건 미충족; MACD=-0.0344827, signal9=-0.0504891; 직전 완료 봉 목표를 다음 봉 시가에 모의 적용 |
| v2 | rsi_14_recovery | 9984.37 | -15.63 | sell / filled / 직전 RSI14 < 30, 현재 RSI14 >= 30 (한 봉 목표); 조건 미충족; RSI14=61.6663, previous_RSI14=57.046; 직전 완료 봉 목표를 다음 봉 시가에 모의 적용 |
| v2 | bollinger_20_reentry | 9962.68 | -37.32 | sell / filled / 직전 종가 < 직전 하단밴드, 현재 하단밴드 <= 종가 <= SMA20 (한 봉 목표); 조건 미충족; close=336.53, lower20=336.046, SMA20=337.886, previous_lower20=336.231; 직전 완료 봉 목표를 다음 봉 시가에 모의 적용 |
| v2 | donchian_20 | 9824.96 | -175.04 | sell / filled / 종가 > 현재 봉을 제외한 직전 20봉 최고가; 조건 미충족; close=339.04, prior_high20=339.42; 직전 완료 봉 목표를 다음 봉 시가에 모의 적용 |
| v2 | atr_14_breakout | 9736.82 | -263.18 | sell / filled / 종가 > 직전 종가 + 직전 ATR14 그리고 종가 > EMA26; 조건 미충족; close=339.04, threshold=340.465, prior_ATR14=1.34545, EMA26=336.613; 직전 완료 봉 목표를 다음 봉 시가에 모의 적용 |
| v2 | session_vwap | 9717.84 | -282.16 | sell / filled / 종가 > 뉴욕 거래일별 누적 전형가격 VWAP; 조건 미충족; close=336.08, session_VWAP=337.149, session_volume=2.04555e+06; 직전 완료 봉 목표를 다음 봉 시가에 모의 적용 |
| v2 | obv_20 | 10005.55 | 5.55 | sell / filled / OBV > OBV의 SMA20 그리고 종가 > EMA26; 조건 미충족; OBV=-1.38544e+07, OBV_SMA20=-1.10099e+07, close=341.625, EMA26=338.807; 직전 완료 봉 목표를 다음 봉 시가에 모의 적용 |
| v2 | stochastic_14_3_recovery | 9704.91 | -295.09 | sell / filled / 직전 %K14 < 20에서 %K14가 %D3 상향 돌파 (한 봉 목표); 조건 미충족; K14=11.111, D3=10.514, previous_K14=15.4166, previous_D3=10.08; 직전 완료 봉 목표를 다음 봉 시가에 모의 적용 |
| v2 | mfi_14_recovery | 9931.66 | -68.34 | sell / filled / 직전 MFI14 < 20, 현재 MFI14 >= 20 (한 봉 목표); 조건 미충족; MFI14=30.2719, previous_MFI14=26.8492; 직전 완료 봉 목표를 다음 봉 시가에 모의 적용 |
| v2 | adx_14_trend | 9722.79 | -277.21 | sell / filled / Wilder ADX14 >= 25 그리고 +DI14 > -DI14; 조건 미충족; ADX14=23.9395, plus_DI14=23.2021, minus_DI14=22.594; 직전 완료 봉 목표를 다음 봉 시가에 모의 적용 |
| v2 | aroon_25_trend | 9822.74 | -177.26 | sell / filled / Aroon25 Up > 70 그리고 Down < 30 (동률이면 최신 극값); 조건 미충족; Aroon_up=68, Aroon_down=16; 직전 완료 봉 목표를 다음 봉 시가에 모의 적용 |
| v2 | cci_20_momentum | 9946.56 | -53.44 | sell / filled / CCI20 > 100 (전형가격·평균절대편차); 조건 미충족; CCI20=28.4392; 직전 완료 봉 목표를 다음 봉 시가에 모의 적용 |
| v2 | williams_14_recovery | 9810.61 | -189.39 | sell / filled / 직전 Williams %R14 < -80, 현재 >= -80 (한 봉 목표); 조건 미충족; Williams_R14=-13.9552, previous_R14=-4.5732; 직전 완료 봉 목표를 다음 봉 시가에 모의 적용 |
| v2 | cmf_20_accumulation | 9903.89 | -96.11 | buy / partial / Chaikin Money Flow20 > 0.1; 조건 충족; CMF20=0.104274, volume20=4.03831e+06; 직전 완료 봉 목표를 다음 봉 시가에 모의 적용 |
| v2 | chaikin_3_10 | 9831.32 | -168.68 | sell / filled / ADL의 EMA3 - EMA10 > 0 그리고 종가 > EMA26; 조건 미충족; Chaikin3_10=7273.89, ADL=-1.28498e+07, close=336.08, EMA26=336.65; 직전 완료 봉 목표를 다음 봉 시가에 모의 적용 |
| v2 | roc_10_momentum | 9832.47 | -167.53 | sell / filled / 10봉 ROC > 1% 그리고 종가 > EMA26; 조건 미충족; ROC10_percent=0.964142, close=337.72, EMA26=336.695; 직전 완료 봉 목표를 다음 봉 시가에 모의 적용 |
| v2 | trix_15_trend | 9715.96 | -284.04 | sell / filled / 15봉 삼중 EMA의 1봉 변화율 TRIX > 0 그리고 종가 > EMA26; 조건 미충족; TRIX15_percent=0.0135144, close=337.6, EMA26=338.759; 직전 완료 봉 목표를 다음 봉 시가에 모의 적용 |
| v2 | keltner_20_breakout | 9901.28 | -98.72 | sell / filled / 종가 > EMA20 + 2 x Wilder ATR14; 조건 미충족; close=339.04, upper_Keltner=339.281, EMA20=336.559, ATR14=1.36146; 직전 완료 봉 목표를 다음 봉 시가에 모의 적용 |
| v2 | opening_range_30m | 9846.33 | -153.67 | sell / filled / 뉴욕 09:30·09:45 두 완료 봉 최고가를 10:00 이후 종가가 돌파; 조건 미충족; close=337.72, opening_high=339.035; 직전 완료 봉 목표를 다음 봉 시가에 모의 적용 |

### 같은 기간의 비용·노출 비교 (사후 연구)

| 전략 | 비용 전 | 비용 후 | 100% 보유 | 같은 평균 노출 보유 | 평균 노출 |
|---|---:|---:|---:|---:|---:|
| cash | 0.00% | 0.00% | -0.38% | -0.00% | 0.00% |
| buy_hold | 0.04% | -0.38% | -0.38% | -0.38% | 100.00% |
| trend_8_26 | 0.14% | -3.98% | -0.38% | -0.21% | 53.95% |
| momentum_26 | -3.06% | -10.12% | -0.38% | -0.19% | 49.74% |
| breakout_8 | -2.73% | -17.43% | -0.38% | -0.08% | 19.74% |
| reversion_12 | 5.18% | -9.58% | -0.38% | -0.10% | 26.05% |
| volume_26 | 0.25% | -6.27% | -0.38% | -0.03% | 7.11% |
| trend_8_26 AND momentum_26 | 0.56% | -4.38% | -0.38% | -0.16% | 41.32% |
| trend_8_26 + momentum_26 | -1.46% | -6.90% | -0.38% | -0.20% | 51.85% |
| trend_8_26 AND breakout_8 | -3.21% | -13.22% | -0.38% | -0.05% | 12.11% |
| trend_8_26 + breakout_8 | -1.29% | -10.57% | -0.38% | -0.14% | 36.85% |
| trend_8_26 AND reversion_12 | 2.61% | -4.06% | -0.38% | -0.03% | 7.63% |
| trend_8_26 + reversion_12 | 2.65% | -6.23% | -0.38% | -0.15% | 40.01% |
| trend_8_26 AND volume_26 | -0.42% | -4.11% | -0.38% | -0.02% | 3.95% |
| trend_8_26 + volume_26 | 0.21% | -5.12% | -0.38% | -0.12% | 30.53% |
| momentum_26 AND breakout_8 | -2.68% | -13.84% | -0.38% | -0.05% | 12.63% |
| momentum_26 + breakout_8 | -2.87% | -13.65% | -0.38% | -0.13% | 34.74% |
| momentum_26 AND reversion_12 | 2.79% | -4.29% | -0.38% | -0.03% | 6.84% |
| momentum_26 + reversion_12 | 1.00% | -8.13% | -0.38% | -0.15% | 37.90% |
| momentum_26 AND volume_26 | 0.21% | -2.70% | -0.38% | -0.01% | 2.89% |
| momentum_26 + volume_26 | -1.39% | -7.82% | -0.38% | -0.11% | 28.43% |
| breakout_8 AND reversion_12 | 0.00% | 0.00% | -0.38% | -0.00% | 0.00% |
| breakout_8 + reversion_12 | 1.17% | -12.31% | -0.38% | -0.09% | 22.90% |
| breakout_8 AND volume_26 | -0.25% | -2.32% | -0.38% | -0.01% | 1.32% |
| breakout_8 + volume_26 | -1.24% | -11.28% | -0.38% | -0.05% | 13.43% |
| reversion_12 AND volume_26 | 1.33% | -2.01% | -0.38% | -0.01% | 3.42% |
| reversion_12 + volume_26 | 2.70% | -6.97% | -0.38% | -0.06% | 16.58% |
| ema_12_26 | -0.24% | -3.54% | -0.38% | -0.20% | 52.11% |
| macd_12_26_9 | -0.13% | -4.64% | -0.38% | -0.13% | 32.89% |
| rsi_14_recovery | 0.47% | -2.03% | -0.38% | -0.01% | 1.58% |
| bollinger_20_reentry | 0.51% | -3.62% | -0.38% | -0.01% | 2.63% |
| donchian_20 | -1.81% | -5.05% | -0.38% | -0.01% | 3.16% |
| atr_14_breakout | -1.35% | -8.92% | -0.38% | -0.02% | 5.26% |
| session_vwap | 1.57% | -8.17% | -0.38% | -0.18% | 47.11% |
| obv_20 | -3.42% | -13.78% | -0.38% | -0.12% | 30.00% |
| stochastic_14_3_recovery | -1.37% | -11.94% | -0.38% | -0.03% | 7.11% |
| mfi_14_recovery | 0.32% | -2.18% | -0.38% | -0.01% | 1.58% |
| adx_14_trend | -2.43% | -4.85% | -0.38% | -0.11% | 29.74% |
| aroon_25_trend | -1.12% | -5.19% | -0.38% | -0.09% | 22.63% |
| cci_20_momentum | -2.84% | -10.67% | -0.38% | -0.06% | 16.32% |
| williams_14_recovery | -0.99% | -10.48% | -0.38% | -0.02% | 6.32% |
| cmf_20_accumulation | -1.80% | -10.09% | -0.38% | -0.11% | 28.95% |
| chaikin_3_10 | 1.01% | -7.52% | -0.38% | -0.13% | 33.95% |
| roc_10_momentum | -1.36% | -4.22% | -0.38% | -0.03% | 8.42% |
| trix_15_trend | -1.25% | -8.83% | -0.38% | -0.14% | 35.26% |
| keltner_20_breakout | -1.21% | -4.07% | -0.38% | -0.02% | 4.21% |
| opening_range_30m | -0.23% | -3.93% | -0.38% | -0.07% | 17.37% |

동일 구간·초기 자금, 종료 시 청산 비용 포함. 노출 맞춤은 사후 설명용이며 v2 실제 계좌 성과가 아닙니다.
[낙폭 분해·비용 영향·전체 구간](JPM/comparison.json)

[v1 전체 기록](JPM/accounts.json) · [v2 전체 기록](JPM/accounts-v2.json)

## XOM 계좌

| 모델 | 전략 | 평가액 USD | 손익 USD | 최근 매매·이유 |
|---|---|---:|---:|---|
| v1 | cash | 10000.00 | 0.00 | 대기 /  / 새 신호 대기 |
| v1 | buy_hold | 10002.65 | 2.65 | buy /  / buy_hold: prior completed bar target 100%; next bar open simulation |
| v1 | trend_8_26 | 9862.79 | -137.21 | sell /  / trend_8_26: prior completed bar target 0%; next bar open simulation |
| v1 | momentum_26 | 9934.85 | -65.15 | sell /  / momentum_26: prior completed bar target 0%; next bar open simulation |
| v1 | breakout_8 | 9746.97 | -253.03 | buy /  / breakout_8: prior completed bar target 100%; next bar open simulation |
| v1 | reversion_12 | 9657.92 | -342.08 | sell /  / reversion_12: prior completed bar target 0%; next bar open simulation |
| v1 | volume_26 | 9732.23 | -267.77 | sell /  / volume_26: prior completed bar target 0%; next bar open simulation |
| v1 | trend_8_26 AND momentum_26 | 9853.77 | -146.23 | sell /  / trend_8_26 AND momentum_26: prior completed bar target 0%; next bar open simulation |
| v1 | trend_8_26 + momentum_26 | 9898.87 | -101.13 | sell /  / trend_8_26 + momentum_26: prior completed bar target 0%; next bar open simulation |
| v1 | trend_8_26 AND breakout_8 | 9829.71 | -170.29 | sell /  / trend_8_26 AND breakout_8: prior completed bar target 0%; next bar open simulation |
| v1 | trend_8_26 + breakout_8 | 9824.76 | -175.24 | buy /  / trend_8_26 + breakout_8: prior completed bar target 50%; next bar open simulation |
| v1 | trend_8_26 AND reversion_12 | 9652.28 | -347.72 | sell /  / trend_8_26 AND reversion_12: prior completed bar target 0%; next bar open simulation |
| v1 | trend_8_26 + reversion_12 | 9759.79 | -240.21 | sell /  / trend_8_26 + reversion_12: prior completed bar target 0%; next bar open simulation |
| v1 | trend_8_26 AND volume_26 | 9849.16 | -150.84 | sell /  / trend_8_26 AND volume_26: prior completed bar target 0%; next bar open simulation |
| v1 | trend_8_26 + volume_26 | 9797.51 | -202.49 | sell /  / trend_8_26 + volume_26: prior completed bar target 0%; next bar open simulation |
| v1 | momentum_26 AND breakout_8 | 9801.24 | -198.76 | sell /  / momentum_26 AND breakout_8: prior completed bar target 0%; next bar open simulation |
| v1 | momentum_26 + breakout_8 | 9840.72 | -159.28 | buy /  / momentum_26 + breakout_8: prior completed bar target 50%; next bar open simulation |
| v1 | momentum_26 AND reversion_12 | 9766.58 | -233.42 | sell /  / momentum_26 AND reversion_12: prior completed bar target 0%; next bar open simulation |
| v1 | momentum_26 + reversion_12 | 9795.30 | -204.70 | sell /  / momentum_26 + reversion_12: prior completed bar target 0%; next bar open simulation |
| v1 | momentum_26 AND volume_26 | 9985.49 | -14.51 | sell /  / momentum_26 AND volume_26: prior completed bar target 0%; next bar open simulation |
| v1 | momentum_26 + volume_26 | 9833.06 | -166.94 | sell /  / momentum_26 + volume_26: prior completed bar target 0%; next bar open simulation |
| v1 | breakout_8 AND reversion_12 | 10000.00 | 0.00 | 대기 /  / 새 신호 대기 |
| v1 | breakout_8 + reversion_12 | 9702.32 | -297.68 | buy /  / breakout_8 + reversion_12: prior completed bar target 50%; next bar open simulation |
| v1 | breakout_8 AND volume_26 | 9950.44 | -49.56 | sell /  / breakout_8 AND volume_26: prior completed bar target 0%; next bar open simulation |
| v1 | breakout_8 + volume_26 | 9739.46 | -260.54 | buy /  / breakout_8 + volume_26: prior completed bar target 50%; next bar open simulation |
| v1 | reversion_12 AND volume_26 | 9840.91 | -159.09 | sell /  / reversion_12 AND volume_26: prior completed bar target 0%; next bar open simulation |
| v1 | reversion_12 + volume_26 | 9695.08 | -304.92 | sell /  / reversion_12 + volume_26: prior completed bar target 0%; next bar open simulation |
| v1 | ema_12_26 | 9973.99 | -26.01 | sell /  / EMA12 > EMA26; 조건 미충족; EMA12=177.968, EMA26=178.055 |
| v1 | macd_12_26_9 | 10064.24 | 64.24 | sell /  / MACD > 신호선 그리고 MACD > 0; 조건 미충족; MACD=0.288973, signal9=0.30355 |
| v1 | rsi_14_recovery | 9927.64 | -72.36 | sell /  / 직전 RSI14 < 30, 현재 RSI14 >= 30 (한 봉 목표); 조건 미충족; RSI14=37.639, previous_RSI14=31.1023 |
| v1 | bollinger_20_reentry | 9852.90 | -147.10 | sell /  / 직전 종가 < 직전 하단밴드, 현재 하단밴드 <= 종가 <= SMA20 (한 봉 목표); 조건 미충족; close=175.55, lower20=175.189, SMA20=177.794, previous_lower20=175.528 |
| v1 | donchian_20 | 9832.30 | -167.70 | sell /  / 종가 > 현재 봉을 제외한 직전 20봉 최고가; 조건 미충족; close=179.01, prior_high20=179.16 |
| v1 | atr_14_breakout | 9864.96 | -135.04 | sell /  / 종가 > 직전 종가 + 직전 ATR14 그리고 종가 > EMA26; 조건 미충족; close=177.19, threshold=177.748, prior_ATR14=0.663113, EMA26=175.734 |
| v1 | session_vwap | 9973.63 | -26.37 | sell /  / 종가 > 뉴욕 거래일별 누적 전형가격 VWAP; 조건 미충족; close=178.14, session_VWAP=178.717, session_volume=890333 |
| v1 | obv_20 | 9901.33 | -98.67 | sell /  / OBV > OBV의 SMA20 그리고 종가 > EMA26; 조건 미충족; OBV=1.97825e+07, OBV_SMA20=1.99344e+07, close=178.275, EMA26=178.258 |
| v1 | stochastic_14_3_recovery | 9721.31 | -278.69 | sell /  / 직전 %K14 < 20에서 %K14가 %D3 상향 돌파 (한 봉 목표); 조건 미충족; K14=29.2797, D3=21.8586, previous_K14=22.3575, previous_D3=16.0588 |
| v1 | mfi_14_recovery | 10000.00 | 0.00 | 대기 /  / 새 신호 대기 |
| v1 | adx_14_trend | 9999.47 | -0.53 | sell /  / Wilder ADX14 >= 25 그리고 +DI14 > -DI14; 조건 미충족; ADX14=23.8302, plus_DI14=25.6436, minus_DI14=22.6035 |
| v1 | aroon_25_trend | 9754.76 | -245.24 | sell /  / Aroon25 Up > 70 그리고 Down < 30 (동률이면 최신 극값); 조건 미충족; Aroon_up=88, Aroon_down=100 |
| v1 | cci_20_momentum | 9743.77 | -256.23 | sell /  / CCI20 > 100 (전형가격·평균절대편차); 조건 미충족; CCI20=96.5349 |
| v1 | williams_14_recovery | 9653.59 | -346.41 | sell /  / 직전 Williams %R14 < -80, 현재 >= -80 (한 봉 목표); 조건 미충족; Williams_R14=-70.7203, previous_R14=-77.6425 |
| v1 | cmf_20_accumulation | 9966.29 | -33.71 | sell /  / Chaikin Money Flow20 > 0.1; 조건 미충족; CMF20=0.0744325, volume20=5.28871e+06 |
| v1 | chaikin_3_10 | 9954.74 | -45.26 | sell /  / ADL의 EMA3 - EMA10 > 0 그리고 종가 > EMA26; 조건 미충족; Chaikin3_10=-7287.74, ADL=2.55494e+07, close=178.275, EMA26=178.258 |
| v1 | roc_10_momentum | 9940.60 | -59.40 | sell /  / 10봉 ROC > 1% 그리고 종가 > EMA26; 조건 미충족; ROC10_percent=0.782107, close=178.47, EMA26=176.891 |
| v1 | trix_15_trend | 9952.41 | -47.59 | sell /  / 15봉 삼중 EMA의 1봉 변화율 TRIX > 0 그리고 종가 > EMA26; 조건 미충족; TRIX15_percent=0.0212551, close=178.14, EMA26=178.249 |
| v1 | keltner_20_breakout | 9937.30 | -62.70 | sell /  / 종가 > EMA20 + 2 x Wilder ATR14; 조건 미충족; close=178.845, upper_Keltner=179.079, EMA20=177.884, ATR14=0.597175 |
| v1 | opening_range_30m | 10049.37 | 49.37 | sell /  / 뉴욕 09:30·09:45 두 완료 봉 최고가를 10:00 이후 종가가 돌파; 자료 부족·변동폭 또는 거래량 없음: 대기; close=179.01 |
| v2 | cash | 10000.00 | 0.00 | 대기 /  / 새 신호 대기 |
| v2 | buy_hold | 10321.86 | 321.86 | buy / partial / 직전 완료 봉 목표 비중 100%; 다음 봉 시가 가정 |
| v2 | trend_8_26 | 9953.74 | -46.26 | sell / filled / 직전 완료 봉 목표 비중 0%; 다음 봉 시가 가정 |
| v2 | momentum_26 | 10102.33 | 102.33 | sell / filled / 직전 완료 봉 목표 비중 0%; 다음 봉 시가 가정 |
| v2 | breakout_8 | 9215.70 | -784.30 | buy / partial / 직전 완료 봉 목표 비중 100%; 다음 봉 시가 가정 |
| v2 | reversion_12 | 9475.52 | -524.48 | sell / filled / 직전 완료 봉 목표 비중 0%; 다음 봉 시가 가정 |
| v2 | volume_26 | 9635.02 | -364.98 | sell / filled / 직전 완료 봉 목표 비중 0%; 다음 봉 시가 가정 |
| v2 | trend_8_26 AND momentum_26 | 9950.02 | -49.98 | sell / filled / 직전 완료 봉 목표 비중 0%; 다음 봉 시가 가정 |
| v2 | trend_8_26 + momentum_26 | 10027.90 | 27.90 | sell / filled / 직전 완료 봉 목표 비중 0%; 다음 봉 시가 가정 |
| v2 | trend_8_26 AND breakout_8 | 9281.59 | -718.41 | sell / filled / 직전 완료 봉 목표 비중 0%; 다음 봉 시가 가정 |
| v2 | trend_8_26 + breakout_8 | 9618.69 | -381.31 | buy / filled / 직전 완료 봉 목표 비중 50%; 다음 봉 시가 가정 |
| v2 | trend_8_26 AND reversion_12 | 9493.76 | -506.24 | sell / filled / 직전 완료 봉 목표 비중 0%; 다음 봉 시가 가정 |
| v2 | trend_8_26 + reversion_12 | 9711.74 | -288.26 | sell / filled / 직전 완료 봉 목표 비중 0%; 다음 봉 시가 가정 |
| v2 | trend_8_26 AND volume_26 | 9742.44 | -257.56 | sell / filled / 직전 완료 봉 목표 비중 0%; 다음 봉 시가 가정 |
| v2 | trend_8_26 + volume_26 | 9793.25 | -206.75 | sell / filled / 직전 완료 봉 목표 비중 0%; 다음 봉 시가 가정 |
| v2 | momentum_26 AND breakout_8 | 9269.79 | -730.21 | sell / filled / 직전 완료 봉 목표 비중 0%; 다음 봉 시가 가정 |
| v2 | momentum_26 + breakout_8 | 9649.62 | -350.38 | buy / filled / 직전 완료 봉 목표 비중 50%; 다음 봉 시가 가정 |
| v2 | momentum_26 AND reversion_12 | 9567.55 | -432.45 | sell / filled / 직전 완료 봉 목표 비중 0%; 다음 봉 시가 가정 |
| v2 | momentum_26 + reversion_12 | 9783.90 | -216.10 | sell / filled / 직전 완료 봉 목표 비중 0%; 다음 봉 시가 가정 |
| v2 | momentum_26 AND volume_26 | 9941.52 | -58.48 | sell / filled / 직전 완료 봉 목표 비중 0%; 다음 봉 시가 가정 |
| v2 | momentum_26 + volume_26 | 9886.61 | -113.39 | sell / filled / 직전 완료 봉 목표 비중 0%; 다음 봉 시가 가정 |
| v2 | breakout_8 AND reversion_12 | 10000.00 | 0.00 | 대기 /  / 새 신호 대기 |
| v2 | breakout_8 + reversion_12 | 9344.57 | -655.43 | buy / filled / 직전 완료 봉 목표 비중 50%; 다음 봉 시가 가정 |
| v2 | breakout_8 AND volume_26 | 9918.86 | -81.14 | sell / filled / 직전 완료 봉 목표 비중 0%; 다음 봉 시가 가정 |
| v2 | breakout_8 + volume_26 | 9442.60 | -557.40 | buy / filled / 직전 완료 봉 목표 비중 50%; 다음 봉 시가 가정 |
| v2 | reversion_12 AND volume_26 | 9787.67 | -212.33 | sell / filled / 직전 완료 봉 목표 비중 0%; 다음 봉 시가 가정 |
| v2 | reversion_12 + volume_26 | 9575.11 | -424.89 | sell / filled / 직전 완료 봉 목표 비중 0%; 다음 봉 시가 가정 |
| v2 | ema_12_26 | 9971.99 | -28.01 | sell / filled / EMA12 > EMA26; 조건 미충족; EMA12=177.968, EMA26=178.055; 직전 완료 봉 목표를 다음 봉 시가에 모의 적용 |
| v2 | macd_12_26_9 | 10060.21 | 60.21 | sell / filled / MACD > 신호선 그리고 MACD > 0; 조건 미충족; MACD=0.288973, signal9=0.30355; 직전 완료 봉 목표를 다음 봉 시가에 모의 적용 |
| v2 | rsi_14_recovery | 9923.67 | -76.33 | sell / filled / 직전 RSI14 < 30, 현재 RSI14 >= 30 (한 봉 목표); 조건 미충족; RSI14=37.639, previous_RSI14=31.1023; 직전 완료 봉 목표를 다음 봉 시가에 모의 적용 |
| v2 | bollinger_20_reentry | 9848.96 | -151.04 | sell / filled / 직전 종가 < 직전 하단밴드, 현재 하단밴드 <= 종가 <= SMA20 (한 봉 목표); 조건 미충족; close=175.55, lower20=175.189, SMA20=177.794, previous_lower20=175.528; 직전 완료 봉 목표를 다음 봉 시가에 모의 적용 |
| v2 | donchian_20 | 9824.43 | -175.57 | sell / filled / 종가 > 현재 봉을 제외한 직전 20봉 최고가; 조건 미충족; close=179.01, prior_high20=179.16; 직전 완료 봉 목표를 다음 봉 시가에 모의 적용 |
| v2 | atr_14_breakout | 9859.04 | -140.96 | sell / filled / 종가 > 직전 종가 + 직전 ATR14 그리고 종가 > EMA26; 조건 미충족; close=177.19, threshold=177.748, prior_ATR14=0.663113, EMA26=175.734; 직전 완료 봉 목표를 다음 봉 시가에 모의 적용 |
| v2 | session_vwap | 9967.65 | -32.35 | sell / filled / 종가 > 뉴욕 거래일별 누적 전형가격 VWAP; 조건 미충족; close=178.14, session_VWAP=178.717, session_volume=890333; 직전 완료 봉 목표를 다음 봉 시가에 모의 적용 |
| v2 | obv_20 | 9893.41 | -106.59 | sell / filled / OBV > OBV의 SMA20 그리고 종가 > EMA26; 조건 미충족; OBV=1.97825e+07, OBV_SMA20=1.99344e+07, close=178.275, EMA26=178.258; 직전 완료 봉 목표를 다음 봉 시가에 모의 적용 |
| v2 | stochastic_14_3_recovery | 9711.59 | -288.41 | sell / filled / 직전 %K14 < 20에서 %K14가 %D3 상향 돌파 (한 봉 목표); 조건 미충족; K14=29.2797, D3=21.8586, previous_K14=22.3575, previous_D3=16.0588; 직전 완료 봉 목표를 다음 봉 시가에 모의 적용 |
| v2 | mfi_14_recovery | 10000.00 | 0.00 | 대기 /  / 새 신호 대기 |
| v2 | adx_14_trend | 9993.47 | -6.53 | sell / filled / Wilder ADX14 >= 25 그리고 +DI14 > -DI14; 조건 미충족; ADX14=23.8302, plus_DI14=25.6436, minus_DI14=22.6035; 직전 완료 봉 목표를 다음 봉 시가에 모의 적용 |
| v2 | aroon_25_trend | 9750.86 | -249.14 | sell / filled / Aroon25 Up > 70 그리고 Down < 30 (동률이면 최신 극값); 조건 미충족; Aroon_up=88, Aroon_down=100; 직전 완료 봉 목표를 다음 봉 시가에 모의 적용 |
| v2 | cci_20_momentum | 9730.14 | -269.86 | sell / filled / CCI20 > 100 (전형가격·평균절대편차); 조건 미충족; CCI20=96.5349; 직전 완료 봉 목표를 다음 봉 시가에 모의 적용 |
| v2 | williams_14_recovery | 9643.94 | -356.06 | sell / filled / 직전 Williams %R14 < -80, 현재 >= -80 (한 봉 목표); 조건 미충족; Williams_R14=-70.7203, previous_R14=-77.6425; 직전 완료 봉 목표를 다음 봉 시가에 모의 적용 |
| v2 | cmf_20_accumulation | 9962.31 | -37.69 | sell / filled / Chaikin Money Flow20 > 0.1; 조건 미충족; CMF20=0.0744325, volume20=5.28871e+06; 직전 완료 봉 목표를 다음 봉 시가에 모의 적용 |
| v2 | chaikin_3_10 | 9948.77 | -51.23 | sell / filled / ADL의 EMA3 - EMA10 > 0 그리고 종가 > EMA26; 조건 미충족; Chaikin3_10=-7287.74, ADL=2.55494e+07, close=178.275, EMA26=178.258; 직전 완료 봉 목표를 다음 봉 시가에 모의 적용 |
| v2 | roc_10_momentum | 9934.64 | -65.36 | sell / filled / 10봉 ROC > 1% 그리고 종가 > EMA26; 조건 미충족; ROC10_percent=0.782107, close=178.47, EMA26=176.891; 직전 완료 봉 목표를 다음 봉 시가에 모의 적용 |
| v2 | trix_15_trend | 9946.44 | -53.56 | sell / filled / 15봉 삼중 EMA의 1봉 변화율 TRIX > 0 그리고 종가 > EMA26; 조건 미충족; TRIX15_percent=0.0212551, close=178.14, EMA26=178.249; 직전 완료 봉 목표를 다음 봉 시가에 모의 적용 |
| v2 | keltner_20_breakout | 9931.34 | -68.66 | sell / filled / 종가 > EMA20 + 2 x Wilder ATR14; 조건 미충족; close=178.845, upper_Keltner=179.079, EMA20=177.884, ATR14=0.597175; 직전 완료 봉 목표를 다음 봉 시가에 모의 적용 |
| v2 | opening_range_30m | 10047.36 | 47.36 | sell / filled / 뉴욕 09:30·09:45 두 완료 봉 최고가를 10:00 이후 종가가 돌파; 자료 부족·변동폭 또는 거래량 없음: 대기; close=179.01; 직전 완료 봉 목표를 다음 봉 시가에 모의 적용 |

### 같은 기간의 비용·노출 비교 (사후 연구)

| 전략 | 비용 전 | 비용 후 | 100% 보유 | 같은 평균 노출 보유 | 평균 노출 |
|---|---:|---:|---:|---:|---:|
| cash | 0.00% | 0.00% | 9.46% | 0.00% | 0.00% |
| buy_hold | 9.92% | 9.46% | 9.46% | 9.46% | 100.00% |
| trend_8_26 | 1.08% | -3.49% | 9.46% | 6.45% | 69.21% |
| momentum_26 | 2.06% | -4.98% | 9.46% | 6.93% | 74.21% |
| breakout_8 | -0.37% | -18.91% | 9.46% | 2.50% | 27.37% |
| reversion_12 | 2.95% | -6.92% | 9.46% | 1.94% | 21.32% |
| volume_26 | 2.43% | -5.43% | 9.46% | 0.50% | 5.53% |
| trend_8_26 AND momentum_26 | -0.07% | -5.38% | 9.46% | 5.84% | 62.89% |
| trend_8_26 + momentum_26 | 1.57% | -4.03% | 9.46% | 6.69% | 71.71% |
| trend_8_26 AND breakout_8 | -0.36% | -15.77% | 9.46% | 1.99% | 21.84% |
| trend_8_26 + breakout_8 | 0.37% | -11.14% | 9.46% | 4.45% | 48.30% |
| trend_8_26 AND reversion_12 | -1.96% | -7.56% | 9.46% | 0.90% | 10.00% |
| trend_8_26 + reversion_12 | 2.04% | -5.02% | 9.46% | 4.17% | 45.27% |
| trend_8_26 AND volume_26 | 1.38% | -3.20% | 9.46% | 0.28% | 3.16% |
| trend_8_26 + volume_26 | 1.77% | -4.26% | 9.46% | 3.42% | 37.37% |
| momentum_26 AND breakout_8 | -0.66% | -18.11% | 9.46% | 2.35% | 25.79% |
| momentum_26 + breakout_8 | 0.86% | -12.20% | 9.46% | 4.69% | 50.80% |
| momentum_26 AND reversion_12 | -0.44% | -6.91% | 9.46% | 0.93% | 10.26% |
| momentum_26 + reversion_12 | 2.53% | -4.76% | 9.46% | 4.40% | 47.77% |
| momentum_26 AND volume_26 | 2.15% | -1.64% | 9.46% | 0.21% | 2.37% |
| momentum_26 + volume_26 | 2.27% | -4.00% | 9.46% | 3.66% | 39.87% |
| breakout_8 AND reversion_12 | 0.00% | 0.00% | 9.46% | 0.00% | 0.00% |
| breakout_8 + reversion_12 | 1.29% | -12.94% | 9.46% | 2.22% | 24.35% |
| breakout_8 AND volume_26 | 0.51% | -1.17% | 9.46% | 0.09% | 1.05% |
| breakout_8 + volume_26 | 1.03% | -11.50% | 9.46% | 1.49% | 16.46% |
| reversion_12 AND volume_26 | 0.29% | -2.62% | 9.46% | 0.19% | 2.11% |
| reversion_12 + volume_26 | 2.71% | -5.38% | 9.46% | 1.22% | 13.43% |
| ema_12_26 | 1.19% | -1.75% | 9.46% | 7.44% | 79.47% |
| macd_12_26_9 | 0.29% | -5.43% | 9.46% | 4.02% | 43.68% |
| rsi_14_recovery | -0.08% | -1.33% | 9.46% | 0.07% | 0.79% |
| bollinger_20_reentry | -1.07% | -3.94% | 9.46% | 0.17% | 1.84% |
| donchian_20 | -0.93% | -10.43% | 9.46% | 0.88% | 9.74% |
| atr_14_breakout | 0.47% | -8.01% | 9.46% | 0.52% | 5.79% |
| session_vwap | 1.93% | -8.62% | 9.46% | 6.14% | 66.05% |
| obv_20 | 2.79% | -5.49% | 9.46% | 4.56% | 49.47% |
| stochastic_14_3_recovery | 0.81% | -8.86% | 9.46% | 0.57% | 6.32% |
| mfi_14_recovery | -0.31% | -1.97% | 9.46% | 0.09% | 1.05% |
| adx_14_trend | 3.88% | 0.87% | 9.46% | 4.09% | 44.47% |
| aroon_25_trend | -3.42% | -10.08% | 9.46% | 3.30% | 36.05% |
| cci_20_momentum | 3.54% | -5.60% | 9.46% | 2.67% | 29.21% |
| williams_14_recovery | -0.88% | -7.32% | 9.46% | 0.38% | 4.21% |
| cmf_20_accumulation | 1.74% | -5.27% | 9.46% | 4.59% | 49.74% |
| chaikin_3_10 | 1.63% | -6.55% | 9.46% | 5.54% | 59.74% |
| roc_10_momentum | 0.80% | -5.36% | 9.46% | 1.19% | 13.16% |
| trix_15_trend | 0.95% | -5.21% | 9.46% | 6.27% | 67.37% |
| keltner_20_breakout | 0.18% | -6.72% | 9.46% | 1.58% | 17.37% |
| opening_range_30m | 0.64% | -8.62% | 9.46% | 3.20% | 35.00% |

동일 구간·초기 자금, 종료 시 청산 비용 포함. 노출 맞춤은 사후 설명용이며 v2 실제 계좌 성과가 아닙니다.
[낙폭 분해·비용 영향·전체 구간](XOM/comparison.json)

[v1 전체 기록](XOM/accounts.json) · [v2 전체 기록](XOM/accounts-v2.json)

## JNJ 계좌

| 모델 | 전략 | 평가액 USD | 손익 USD | 최근 매매·이유 |
|---|---|---:|---:|---|
| v1 | cash | 10000.00 | 0.00 | 대기 /  / 새 신호 대기 |
| v1 | buy_hold | 10109.90 | 109.90 | buy /  / buy_hold: prior completed bar target 100%; next bar open simulation |
| v1 | trend_8_26 | 10061.29 | 61.29 | buy /  / trend_8_26: prior completed bar target 100%; next bar open simulation |
| v1 | momentum_26 | 9832.17 | -167.83 | buy /  / momentum_26: prior completed bar target 100%; next bar open simulation |
| v1 | breakout_8 | 9513.91 | -486.09 | sell /  / breakout_8: prior completed bar target 0%; next bar open simulation |
| v1 | reversion_12 | 9891.56 | -108.44 | sell /  / reversion_12: prior completed bar target 0%; next bar open simulation |
| v1 | volume_26 | 9943.90 | -56.10 | sell /  / volume_26: prior completed bar target 0%; next bar open simulation |
| v1 | trend_8_26 AND momentum_26 | 9884.06 | -115.94 | buy /  / trend_8_26 AND momentum_26: prior completed bar target 100%; next bar open simulation |
| v1 | trend_8_26 + momentum_26 | 9946.37 | -53.63 | buy /  / trend_8_26 + momentum_26: prior completed bar target 100%; next bar open simulation |
| v1 | trend_8_26 AND breakout_8 | 9814.73 | -185.27 | sell /  / trend_8_26 AND breakout_8: prior completed bar target 0%; next bar open simulation |
| v1 | trend_8_26 + breakout_8 | 9803.59 | -196.41 | sell /  / trend_8_26 + breakout_8: prior completed bar target 50%; next bar open simulation |
| v1 | trend_8_26 AND reversion_12 | 9992.01 | -7.99 | sell /  / trend_8_26 AND reversion_12: prior completed bar target 0%; next bar open simulation |
| v1 | trend_8_26 + reversion_12 | 9976.18 | -23.82 | sell /  / trend_8_26 + reversion_12: prior completed bar target 50%; next bar open simulation |
| v1 | trend_8_26 AND volume_26 | 9995.12 | -4.88 | sell /  / trend_8_26 AND volume_26: prior completed bar target 0%; next bar open simulation |
| v1 | trend_8_26 + volume_26 | 10002.64 | 2.64 | sell /  / trend_8_26 + volume_26: prior completed bar target 50%; next bar open simulation |
| v1 | momentum_26 AND breakout_8 | 9833.49 | -166.51 | sell /  / momentum_26 AND breakout_8: prior completed bar target 0%; next bar open simulation |
| v1 | momentum_26 + breakout_8 | 9671.58 | -328.42 | sell /  / momentum_26 + breakout_8: prior completed bar target 50%; next bar open simulation |
| v1 | momentum_26 AND reversion_12 | 10000.00 | 0.00 | 대기 /  / 새 신호 대기 |
| v1 | momentum_26 + reversion_12 | 9881.43 | -118.57 | sell /  / momentum_26 + reversion_12: prior completed bar target 50%; next bar open simulation |
| v1 | momentum_26 AND volume_26 | 10000.00 | 0.00 | 대기 /  / 새 신호 대기 |
| v1 | momentum_26 + volume_26 | 9927.51 | -72.49 | sell /  / momentum_26 + volume_26: prior completed bar target 50%; next bar open simulation |
| v1 | breakout_8 AND reversion_12 | 10000.00 | 0.00 | 대기 /  / 새 신호 대기 |
| v1 | breakout_8 + reversion_12 | 9700.73 | -299.27 | sell /  / breakout_8 + reversion_12: prior completed bar target 0%; next bar open simulation |
| v1 | breakout_8 AND volume_26 | 10000.00 | 0.00 | 대기 /  / 새 신호 대기 |
| v1 | breakout_8 + volume_26 | 9745.99 | -254.01 | sell /  / breakout_8 + volume_26: prior completed bar target 0%; next bar open simulation |
| v1 | reversion_12 AND volume_26 | 9974.59 | -25.41 | sell /  / reversion_12 AND volume_26: prior completed bar target 0%; next bar open simulation |
| v1 | reversion_12 + volume_26 | 9937.59 | -62.41 | sell /  / reversion_12 + volume_26: prior completed bar target 0%; next bar open simulation |
| v1 | ema_12_26 | 9930.69 | -69.31 | buy /  / EMA12 > EMA26; 조건 충족; EMA12=253.915, EMA26=253.911 |
| v1 | macd_12_26_9 | 9905.56 | -94.44 | buy /  / MACD > 신호선 그리고 MACD > 0; 조건 충족; MACD=0.00413589, signal9=-0.236181 |
| v1 | rsi_14_recovery | 9923.04 | -76.96 | sell /  / 직전 RSI14 < 30, 현재 RSI14 >= 30 (한 봉 목표); 조건 미충족; RSI14=40.3665, previous_RSI14=36.2025 |
| v1 | bollinger_20_reentry | 9881.04 | -118.96 | sell /  / 직전 종가 < 직전 하단밴드, 현재 하단밴드 <= 종가 <= SMA20 (한 봉 목표); 조건 미충족; close=251.75, lower20=251.316, SMA20=254.208, previous_lower20=251.691 |
| v1 | donchian_20 | 9921.02 | -78.98 | sell /  / 종가 > 현재 봉을 제외한 직전 20봉 최고가; 조건 미충족; close=258.68, prior_high20=260.425 |
| v1 | atr_14_breakout | 9805.90 | -194.10 | sell /  / 종가 > 직전 종가 + 직전 ATR14 그리고 종가 > EMA26; 조건 미충족; close=258.68, threshold=261.221, prior_ATR14=1.00083, EMA26=254.754 |
| v1 | session_vwap | 9832.03 | -167.97 | sell /  / 종가 > 뉴욕 거래일별 누적 전형가격 VWAP; 조건 미충족; close=258.91, session_VWAP=259.405, session_volume=4.28557e+06 |
| v1 | obv_20 | 9664.18 | -335.82 | buy /  / OBV > OBV의 SMA20 그리고 종가 > EMA26; 조건 충족; OBV=4.78456e+06, OBV_SMA20=3.4932e+06, close=254.04, EMA26=253.978 |
| v1 | stochastic_14_3_recovery | 9862.87 | -137.13 | sell /  / 직전 %K14 < 20에서 %K14가 %D3 상향 돌파 (한 봉 목표); 조건 미충족; K14=28.9392, D3=18.1738, previous_K14=19.7943, previous_D3=12.6561 |
| v1 | mfi_14_recovery | 10000.00 | 0.00 | 대기 /  / 새 신호 대기 |
| v1 | adx_14_trend | 9790.93 | -209.07 | buy /  / Wilder ADX14 >= 25 그리고 +DI14 > -DI14; 조건 충족; ADX14=27.0884, plus_DI14=47.0278, minus_DI14=11.4099 |
| v1 | aroon_25_trend | 9901.12 | -98.88 | buy /  / Aroon25 Up > 70 그리고 Down < 30 (동률이면 최신 극값); 조건 충족; Aroon_up=100, Aroon_down=16 |
| v1 | cci_20_momentum | 9818.66 | -181.34 | sell /  / CCI20 > 100 (전형가격·평균절대편차); 조건 미충족; CCI20=95.1073 |
| v1 | williams_14_recovery | 9903.67 | -96.33 | sell /  / 직전 Williams %R14 < -80, 현재 >= -80 (한 봉 목표); 조건 미충족; Williams_R14=-61.3372, previous_R14=-71.0608 |
| v1 | cmf_20_accumulation | 10236.69 | 236.69 | buy /  / Chaikin Money Flow20 > 0.1; 조건 충족; CMF20=0.280188, volume20=5.69706e+06 |
| v1 | chaikin_3_10 | 9882.87 | -117.13 | buy /  / ADL의 EMA3 - EMA10 > 0 그리고 종가 > EMA26; 조건 충족; Chaikin3_10=250777, ADL=4.30146e+06, close=254.04, EMA26=253.978 |
| v1 | roc_10_momentum | 9691.76 | -308.24 | sell /  / 10봉 ROC > 1% 그리고 종가 > EMA26; 조건 미충족; ROC10_percent=-0.503419, close=258.91, EMA26=257.09 |
| v1 | trix_15_trend | 9774.47 | -225.53 | buy /  / 15봉 삼중 EMA의 1봉 변화율 TRIX > 0 그리고 종가 > EMA26; 조건 충족; TRIX15_percent=0.000945132, close=260.22, EMA26=254.44 |
| v1 | keltner_20_breakout | 9916.04 | -83.96 | sell /  / 종가 > EMA20 + 2 x Wilder ATR14; 조건 미충족; close=258.91, upper_Keltner=259.564, EMA20=257.603, ATR14=0.980686 |
| v1 | opening_range_30m | 10000.00 | 0.00 | 대기 /  / 새 신호 대기 |
| v2 | cash | 10000.00 | 0.00 | 대기 /  / 새 신호 대기 |
| v2 | buy_hold | 9873.94 | -126.06 | 중단: 손실 한도 / buy / partial / 직전 완료 봉 목표 비중 100%; 다음 봉 시가 가정 |
| v2 | trend_8_26 | 9873.94 | -126.06 | 중단: 손실 한도 / buy / partial / 직전 완료 봉 목표 비중 100%; 다음 봉 시가 가정 |
| v2 | momentum_26 | 9873.94 | -126.06 | 중단: 손실 한도 / buy / partial / 직전 완료 봉 목표 비중 100%; 다음 봉 시가 가정 |
| v2 | breakout_8 | 9343.39 | -656.61 | 중단: 손실 한도 / sell / filled / 직전 완료 봉 목표 비중 0%; 다음 봉 시가 가정 |
| v2 | reversion_12 | 9581.23 | -418.77 | sell / filled / 직전 완료 봉 목표 비중 0%; 다음 봉 시가 가정 |
| v2 | volume_26 | 9728.64 | -271.36 | sell / filled / 직전 완료 봉 목표 비중 0%; 다음 봉 시가 가정 |
| v2 | trend_8_26 AND momentum_26 | 9873.94 | -126.06 | 중단: 손실 한도 / buy / partial / 직전 완료 봉 목표 비중 100%; 다음 봉 시가 가정 |
| v2 | trend_8_26 + momentum_26 | 9873.94 | -126.06 | 중단: 손실 한도 / buy / partial / 직전 완료 봉 목표 비중 100%; 다음 봉 시가 가정 |
| v2 | trend_8_26 AND breakout_8 | 9419.39 | -580.61 | 중단: 손실 한도 / sell / filled / 직전 완료 봉 목표 비중 0%; 다음 봉 시가 가정 |
| v2 | trend_8_26 + breakout_8 | 9372.94 | -627.06 | sell / filled / 직전 완료 봉 목표 비중 50%; 다음 봉 시가 가정 |
| v2 | trend_8_26 AND reversion_12 | 9968.12 | -31.88 | sell / filled / 직전 완료 봉 목표 비중 0%; 다음 봉 시가 가정 |
| v2 | trend_8_26 + reversion_12 | 9732.92 | -267.08 | 중단: 손실 한도 / sell / filled / 직전 완료 봉 목표 비중 0%; 다음 봉 시가 가정 |
| v2 | trend_8_26 AND volume_26 | 9861.95 | -138.05 | sell / filled / 직전 완료 봉 목표 비중 0%; 다음 봉 시가 가정 |
| v2 | trend_8_26 + volume_26 | 9911.79 | -88.21 | 중단: 손실 한도 / buy / filled / 직전 완료 봉 목표 비중 50%; 다음 봉 시가 가정 |
| v2 | momentum_26 AND breakout_8 | 9435.09 | -564.91 | sell / filled / 직전 완료 봉 목표 비중 0%; 다음 봉 시가 가정 |
| v2 | momentum_26 + breakout_8 | 9237.11 | -762.89 | sell / filled / 직전 완료 봉 목표 비중 50%; 다음 봉 시가 가정 |
| v2 | momentum_26 AND reversion_12 | 9938.87 | -61.13 | sell / filled / 직전 완료 봉 목표 비중 0%; 다음 봉 시가 가정 |
| v2 | momentum_26 + reversion_12 | 9732.92 | -267.08 | 중단: 손실 한도 / sell / filled / 직전 완료 봉 목표 비중 0%; 다음 봉 시가 가정 |
| v2 | momentum_26 AND volume_26 | 9920.93 | -79.07 | sell / filled / 직전 완료 봉 목표 비중 0%; 다음 봉 시가 가정 |
| v2 | momentum_26 + volume_26 | 9911.79 | -88.21 | 중단: 손실 한도 / buy / filled / 직전 완료 봉 목표 비중 50%; 다음 봉 시가 가정 |
| v2 | breakout_8 AND reversion_12 | 10000.00 | 0.00 | 대기 /  / 새 신호 대기 |
| v2 | breakout_8 + reversion_12 | 9284.10 | -715.90 | sell / filled / 직전 완료 봉 목표 비중 0%; 다음 봉 시가 가정 |
| v2 | breakout_8 AND volume_26 | 9814.17 | -185.83 | sell / filled / 직전 완료 봉 목표 비중 0%; 다음 봉 시가 가정 |
| v2 | breakout_8 + volume_26 | 9355.32 | -644.68 | sell / filled / 직전 완료 봉 목표 비중 0%; 다음 봉 시가 가정 |
| v2 | reversion_12 AND volume_26 | 9859.15 | -140.85 | sell / filled / 직전 완료 봉 목표 비중 0%; 다음 봉 시가 가정 |
| v2 | reversion_12 + volume_26 | 9695.58 | -304.42 | sell / filled / 직전 완료 봉 목표 비중 0%; 다음 봉 시가 가정 |
| v2 | ema_12_26 | 9925.72 | -74.28 | buy / partial / EMA12 > EMA26; 조건 충족; EMA12=253.915, EMA26=253.911; 직전 완료 봉 목표를 다음 봉 시가에 모의 적용 |
| v2 | macd_12_26_9 | 9900.61 | -99.39 | buy / partial / MACD > 신호선 그리고 MACD > 0; 조건 충족; MACD=0.00413589, signal9=-0.236181; 직전 완료 봉 목표를 다음 봉 시가에 모의 적용 |
| v2 | rsi_14_recovery | 9919.07 | -80.93 | sell / filled / 직전 RSI14 < 30, 현재 RSI14 >= 30 (한 봉 목표); 조건 미충족; RSI14=40.3665, previous_RSI14=36.2025; 직전 완료 봉 목표를 다음 봉 시가에 모의 적용 |
| v2 | bollinger_20_reentry | 9877.09 | -122.91 | sell / filled / 직전 종가 < 직전 하단밴드, 현재 하단밴드 <= 종가 <= SMA20 (한 봉 목표); 조건 미충족; close=251.75, lower20=251.316, SMA20=254.208, previous_lower20=251.691; 직전 완료 봉 목표를 다음 봉 시가에 모의 적용 |
| v2 | donchian_20 | 9919.03 | -80.97 | sell / filled / 종가 > 현재 봉을 제외한 직전 20봉 최고가; 조건 미충족; close=258.68, prior_high20=260.425; 직전 완료 봉 목표를 다음 봉 시가에 모의 적용 |
| v2 | atr_14_breakout | 9800.02 | -199.98 | sell / filled / 종가 > 직전 종가 + 직전 ATR14 그리고 종가 > EMA26; 조건 미충족; close=258.68, threshold=261.221, prior_ATR14=1.00083, EMA26=254.754; 직전 완료 봉 목표를 다음 봉 시가에 모의 적용 |
| v2 | session_vwap | 9818.27 | -181.73 | sell / filled / 종가 > 뉴욕 거래일별 누적 전형가격 VWAP; 조건 미충족; close=258.91, session_VWAP=259.405, session_volume=4.28557e+06; 직전 완료 봉 목표를 다음 봉 시가에 모의 적용 |
| v2 | obv_20 | 9651.63 | -348.37 | buy / partial / OBV > OBV의 SMA20 그리고 종가 > EMA26; 조건 충족; OBV=4.78456e+06, OBV_SMA20=3.4932e+06, close=254.04, EMA26=253.978; 직전 완료 봉 목표를 다음 봉 시가에 모의 적용 |
| v2 | stochastic_14_3_recovery | 9856.96 | -143.04 | sell / filled / 직전 %K14 < 20에서 %K14가 %D3 상향 돌파 (한 봉 목표); 조건 미충족; K14=28.9392, D3=18.1738, previous_K14=19.7943, previous_D3=12.6561; 직전 완료 봉 목표를 다음 봉 시가에 모의 적용 |
| v2 | mfi_14_recovery | 10000.00 | 0.00 | 대기 /  / 새 신호 대기 |
| v2 | adx_14_trend | 9784.08 | -215.92 | buy / partial / Wilder ADX14 >= 25 그리고 +DI14 > -DI14; 조건 충족; ADX14=27.0884, plus_DI14=47.0278, minus_DI14=11.4099; 직전 완료 봉 목표를 다음 봉 시가에 모의 적용 |
| v2 | aroon_25_trend | 9898.15 | -101.85 | buy / partial / Aroon25 Up > 70 그리고 Down < 30 (동률이면 최신 극값); 조건 충족; Aroon_up=100, Aroon_down=16; 직전 완료 봉 목표를 다음 봉 시가에 모의 적용 |
| v2 | cci_20_momentum | 9812.77 | -187.23 | sell / filled / CCI20 > 100 (전형가격·평균절대편차); 조건 미충족; CCI20=95.1073; 직전 완료 봉 목표를 다음 봉 시가에 모의 적용 |
| v2 | williams_14_recovery | 9899.71 | -100.29 | sell / filled / 직전 Williams %R14 < -80, 현재 >= -80 (한 봉 목표); 조건 미충족; Williams_R14=-61.3372, previous_R14=-71.0608; 직전 완료 봉 목표를 다음 봉 시가에 모의 적용 |
| v2 | cmf_20_accumulation | 10235.67 | 235.67 | buy / partial / Chaikin Money Flow20 > 0.1; 조건 충족; CMF20=0.280188, volume20=5.69706e+06; 직전 완료 봉 목표를 다음 봉 시가에 모의 적용 |
| v2 | chaikin_3_10 | 9875.96 | -124.04 | buy / partial / ADL의 EMA3 - EMA10 > 0 그리고 종가 > EMA26; 조건 충족; Chaikin3_10=250777, ADL=4.30146e+06, close=254.04, EMA26=253.978; 직전 완료 봉 목표를 다음 봉 시가에 모의 적용 |
| v2 | roc_10_momentum | 9684.01 | -315.99 | sell / filled / 10봉 ROC > 1% 그리고 종가 > EMA26; 조건 미충족; ROC10_percent=-0.503419, close=258.91, EMA26=257.09; 직전 완료 봉 목표를 다음 봉 시가에 모의 적용 |
| v2 | trix_15_trend | 9769.58 | -230.42 | buy / partial / 15봉 삼중 EMA의 1봉 변화율 TRIX > 0 그리고 종가 > EMA26; 조건 충족; TRIX15_percent=0.000945132, close=260.22, EMA26=254.44; 직전 완료 봉 목표를 다음 봉 시가에 모의 적용 |
| v2 | keltner_20_breakout | 9914.05 | -85.95 | sell / filled / 종가 > EMA20 + 2 x Wilder ATR14; 조건 미충족; close=258.91, upper_Keltner=259.564, EMA20=257.603, ATR14=0.980686; 직전 완료 봉 목표를 다음 봉 시가에 모의 적용 |
| v2 | opening_range_30m | 10000.00 | 0.00 | 대기 /  / 새 신호 대기 |

### 같은 기간의 비용·노출 비교 (사후 연구)

| 전략 | 비용 전 | 비용 후 | 100% 보유 | 같은 평균 노출 보유 | 평균 노출 |
|---|---:|---:|---:|---:|---:|
| cash | 0.00% | 0.00% | -3.37% | -0.00% | 0.00% |
| buy_hold | -2.96% | -3.37% | -3.37% | -3.37% | 100.00% |
| trend_8_26 | 3.14% | 0.57% | -3.37% | -1.68% | 48.95% |
| momentum_26 | -0.25% | -3.95% | -3.37% | -1.59% | 46.32% |
| breakout_8 | -1.40% | -18.38% | -3.37% | -0.70% | 20.26% |
| reversion_12 | -7.05% | -14.54% | -3.37% | -1.04% | 30.00% |
| volume_26 | -0.92% | -7.75% | -3.37% | -0.23% | 6.58% |
| trend_8_26 AND momentum_26 | 1.01% | -2.33% | -3.37% | -1.42% | 41.05% |
| trend_8_26 + momentum_26 | 1.44% | -1.71% | -3.37% | -1.64% | 47.63% |
| trend_8_26 AND breakout_8 | 0.12% | -11.73% | -3.37% | -0.48% | 13.68% |
| trend_8_26 + breakout_8 | 0.87% | -9.19% | -3.37% | -1.20% | 34.61% |
| trend_8_26 AND reversion_12 | 0.87% | -2.05% | -3.37% | -0.18% | 5.26% |
| trend_8_26 + reversion_12 | -2.05% | -6.89% | -3.37% | -1.36% | 39.48% |
| trend_8_26 AND volume_26 | 1.42% | -1.10% | -3.37% | -0.06% | 1.58% |
| trend_8_26 + volume_26 | 1.12% | -3.46% | -3.37% | -0.96% | 27.77% |
| momentum_26 AND breakout_8 | 0.98% | -9.84% | -3.37% | -0.45% | 12.89% |
| momentum_26 + breakout_8 | -0.80% | -11.26% | -3.37% | -1.15% | 33.30% |
| momentum_26 AND reversion_12 | -0.82% | -2.88% | -3.37% | -0.19% | 5.53% |
| momentum_26 + reversion_12 | -3.68% | -8.82% | -3.37% | -1.32% | 38.16% |
| momentum_26 AND volume_26 | 0.14% | -0.70% | -3.37% | -0.02% | 0.53% |
| momentum_26 + volume_26 | -0.55% | -4.86% | -3.37% | -0.92% | 26.45% |
| breakout_8 AND reversion_12 | 0.00% | 0.00% | -3.37% | -0.00% | 0.00% |
| breakout_8 + reversion_12 | -4.25% | -15.96% | -3.37% | -0.87% | 25.14% |
| breakout_8 AND volume_26 | -0.91% | -2.15% | -3.37% | -0.03% | 0.79% |
| breakout_8 + volume_26 | -1.15% | -12.31% | -3.37% | -0.47% | 13.43% |
| reversion_12 AND volume_26 | -1.84% | -4.69% | -3.37% | -0.10% | 2.89% |
| reversion_12 + volume_26 | -4.02% | -10.46% | -3.37% | -0.64% | 18.29% |
| ema_12_26 | 0.37% | -2.13% | -3.37% | -1.47% | 42.63% |
| macd_12_26_9 | 5.81% | 2.74% | -3.37% | -1.02% | 29.47% |
| rsi_14_recovery | -1.35% | -6.20% | -3.37% | -0.11% | 3.16% |
| bollinger_20_reentry | -1.10% | -5.56% | -3.37% | -0.10% | 2.89% |
| donchian_20 | 0.23% | -7.07% | -3.37% | -0.24% | 6.84% |
| atr_14_breakout | 0.79% | -5.36% | -3.37% | -0.17% | 4.74% |
| session_vwap | 3.37% | -4.96% | -3.37% | -1.70% | 49.47% |
| obv_20 | -5.52% | -14.58% | -3.37% | -1.18% | 34.21% |
| stochastic_14_3_recovery | -0.31% | -12.11% | -3.37% | -0.28% | 7.89% |
| mfi_14_recovery | 0.33% | -0.93% | -3.37% | -0.03% | 0.79% |
| adx_14_trend | -2.69% | -7.86% | -3.37% | -1.17% | 33.68% |
| aroon_25_trend | 3.62% | -0.65% | -3.37% | -1.06% | 30.53% |
| cci_20_momentum | 0.20% | -6.70% | -3.37% | -0.76% | 21.84% |
| williams_14_recovery | -1.58% | -8.74% | -3.37% | -0.17% | 4.74% |
| cmf_20_accumulation | 5.19% | 1.29% | -3.37% | -1.08% | 31.05% |
| chaikin_3_10 | -2.91% | -8.07% | -3.37% | -1.23% | 35.53% |
| roc_10_momentum | -2.79% | -9.49% | -3.37% | -0.61% | 17.63% |
| trix_15_trend | -0.70% | -3.17% | -3.37% | -1.11% | 32.11% |
| keltner_20_breakout | 0.20% | -3.52% | -3.37% | -0.41% | 11.84% |
| opening_range_30m | 0.79% | -2.95% | -3.37% | -0.90% | 26.05% |

동일 구간·초기 자금, 종료 시 청산 비용 포함. 노출 맞춤은 사후 설명용이며 v2 실제 계좌 성과가 아닙니다.
[낙폭 분해·비용 영향·전체 구간](JNJ/comparison.json)

[v1 전체 기록](JNJ/accounts.json) · [v2 전체 기록](JNJ/accounts-v2.json)

## CAT 계좌

| 모델 | 전략 | 평가액 USD | 손익 USD | 최근 매매·이유 |
|---|---|---:|---:|---|
| v1 | cash | 10000.00 | 0.00 | 대기 /  / 새 신호 대기 |
| v1 | buy_hold | 9854.66 | -145.34 | buy /  / buy_hold: prior completed bar target 100%; next bar open simulation |
| v1 | trend_8_26 | 9879.80 | -120.20 | buy /  / trend_8_26: prior completed bar target 100%; next bar open simulation |
| v1 | momentum_26 | 9765.06 | -234.94 | sell /  / momentum_26: prior completed bar target 0%; next bar open simulation |
| v1 | breakout_8 | 9687.36 | -312.64 | sell /  / breakout_8: prior completed bar target 0%; next bar open simulation |
| v1 | reversion_12 | 9927.33 | -72.67 | sell /  / reversion_12: prior completed bar target 0%; next bar open simulation |
| v1 | volume_26 | 10007.30 | 7.30 | sell /  / volume_26: prior completed bar target 0%; next bar open simulation |
| v1 | trend_8_26 AND momentum_26 | 9873.91 | -126.09 | sell /  / trend_8_26 AND momentum_26: prior completed bar target 0%; next bar open simulation |
| v1 | trend_8_26 + momentum_26 | 9822.44 | -177.56 | sell /  / trend_8_26 + momentum_26: prior completed bar target 50%; next bar open simulation |
| v1 | trend_8_26 AND breakout_8 | 9850.32 | -149.68 | sell /  / trend_8_26 AND breakout_8: prior completed bar target 0%; next bar open simulation |
| v1 | trend_8_26 + breakout_8 | 9783.26 | -216.74 | sell /  / trend_8_26 + breakout_8: prior completed bar target 50%; next bar open simulation |
| v1 | trend_8_26 AND reversion_12 | 9928.06 | -71.94 | sell /  / trend_8_26 AND reversion_12: prior completed bar target 0%; next bar open simulation |
| v1 | trend_8_26 + reversion_12 | 9924.06 | -75.94 | sell /  / trend_8_26 + reversion_12: prior completed bar target 50%; next bar open simulation |
| v1 | trend_8_26 AND volume_26 | 10000.00 | 0.00 | 대기 /  / 새 신호 대기 |
| v1 | trend_8_26 + volume_26 | 9963.30 | -36.70 | sell /  / trend_8_26 + volume_26: prior completed bar target 50%; next bar open simulation |
| v1 | momentum_26 AND breakout_8 | 9804.82 | -195.18 | sell /  / momentum_26 AND breakout_8: prior completed bar target 0%; next bar open simulation |
| v1 | momentum_26 + breakout_8 | 9726.19 | -273.81 | sell /  / momentum_26 + breakout_8: prior completed bar target 0%; next bar open simulation |
| v1 | momentum_26 AND reversion_12 | 9887.21 | -112.79 | sell /  / momentum_26 AND reversion_12: prior completed bar target 0%; next bar open simulation |
| v1 | momentum_26 + reversion_12 | 9846.60 | -153.40 | sell /  / momentum_26 + reversion_12: prior completed bar target 0%; next bar open simulation |
| v1 | momentum_26 AND volume_26 | 9985.43 | -14.57 | sell /  / momentum_26 AND volume_26: prior completed bar target 0%; next bar open simulation |
| v1 | momentum_26 + volume_26 | 9885.51 | -114.49 | sell /  / momentum_26 + volume_26: prior completed bar target 0%; next bar open simulation |
| v1 | breakout_8 AND reversion_12 | 10000.00 | 0.00 | 대기 /  / 새 신호 대기 |
| v1 | breakout_8 + reversion_12 | 9807.18 | -192.82 | sell /  / breakout_8 + reversion_12: prior completed bar target 0%; next bar open simulation |
| v1 | breakout_8 AND volume_26 | 9985.43 | -14.57 | sell /  / breakout_8 AND volume_26: prior completed bar target 0%; next bar open simulation |
| v1 | breakout_8 + volume_26 | 9846.03 | -153.97 | sell /  / breakout_8 + volume_26: prior completed bar target 0%; next bar open simulation |
| v1 | reversion_12 AND volume_26 | 10046.29 | 46.29 | sell /  / reversion_12 AND volume_26: prior completed bar target 0%; next bar open simulation |
| v1 | reversion_12 + volume_26 | 9967.75 | -32.25 | sell /  / reversion_12 + volume_26: prior completed bar target 0%; next bar open simulation |
| v1 | ema_12_26 | 9862.47 | -137.53 | sell /  / EMA12 > EMA26; 조건 미충족; EMA12=735.622, EMA26=735.711 |
| v1 | macd_12_26_9 | 9904.18 | -95.82 | sell /  / MACD > 신호선 그리고 MACD > 0; 조건 미충족; MACD=0.746548, signal9=0.752293 |
| v1 | rsi_14_recovery | 9999.22 | -0.78 | sell /  / 직전 RSI14 < 30, 현재 RSI14 >= 30 (한 봉 목표); 조건 미충족; RSI14=43.621, previous_RSI14=38.5787 |
| v1 | bollinger_20_reentry | 9777.09 | -222.91 | sell /  / 직전 종가 < 직전 하단밴드, 현재 하단밴드 <= 종가 <= SMA20 (한 봉 목표); 조건 미충족; close=721.16, lower20=716.851, SMA20=725.821, previous_lower20=717.276 |
| v1 | donchian_20 | 9950.83 | -49.17 | sell /  / 종가 > 현재 봉을 제외한 직전 20봉 최고가; 조건 미충족; close=739.81, prior_high20=742.28 |
| v1 | atr_14_breakout | 9775.74 | -224.26 | sell /  / 종가 > 직전 종가 + 직전 ATR14 그리고 종가 > EMA26; 조건 미충족; close=732.42, threshold=735.931, prior_ATR14=4.99094, EMA26=726.612 |
| v1 | session_vwap | 9438.02 | -561.98 | buy /  / 종가 > 뉴욕 거래일별 누적 전형가격 VWAP; 조건 충족; close=717.87, session_VWAP=713.405, session_volume=283277 |
| v1 | obv_20 | 9683.67 | -316.33 | sell /  / OBV > OBV의 SMA20 그리고 종가 > EMA26; 조건 미충족; OBV=-5.85317e+06, OBV_SMA20=-5.80449e+06, close=725.22, EMA26=726.751 |
| v1 | stochastic_14_3_recovery | 9855.08 | -144.92 | sell /  / 직전 %K14 < 20에서 %K14가 %D3 상향 돌파 (한 봉 목표); 조건 미충족; K14=59.6496, D3=39.2535, previous_K14=43.8356, previous_D3=33.8642 |
| v1 | mfi_14_recovery | 10068.63 | 68.63 | sell /  / 직전 MFI14 < 20, 현재 MFI14 >= 20 (한 봉 목표); 조건 미충족; MFI14=32.7313, previous_MFI14=24.1736 |
| v1 | adx_14_trend | 10000.00 | 0.00 | 대기 /  / 새 신호 대기 |
| v1 | aroon_25_trend | 10031.15 | 31.15 | sell /  / Aroon25 Up > 70 그리고 Down < 30 (동률이면 최신 극값); 조건 미충족; Aroon_up=88, Aroon_down=48 |
| v1 | cci_20_momentum | 9890.31 | -109.69 | sell /  / CCI20 > 100 (전형가격·평균절대편차); 조건 미충족; CCI20=20.3547 |
| v1 | williams_14_recovery | 10007.06 | 7.06 | sell /  / 직전 Williams %R14 < -80, 현재 >= -80 (한 봉 목표); 조건 미충족; Williams_R14=-40.3504, previous_R14=-56.1644 |
| v1 | cmf_20_accumulation | 9782.00 | -218.00 | buy /  / Chaikin Money Flow20 > 0.1; 조건 충족; CMF20=0.130083, volume20=2.38752e+06 |
| v1 | chaikin_3_10 | 9474.17 | -525.83 | sell /  / ADL의 EMA3 - EMA10 > 0 그리고 종가 > EMA26; 조건 미충족; Chaikin3_10=39681.6, ADL=-6.22839e+06, close=725.22, EMA26=726.751 |
| v1 | roc_10_momentum | 9963.13 | -36.87 | sell /  / 10봉 ROC > 1% 그리고 종가 > EMA26; 조건 미충족; ROC10_percent=-0.134597, close=734.53, EMA26=735.486 |
| v1 | trix_15_trend | 9669.78 | -330.22 | sell /  / 15봉 삼중 EMA의 1봉 변화율 TRIX > 0 그리고 종가 > EMA26; 조건 미충족; TRIX15_percent=0.0186631, close=734.925, EMA26=736.093 |
| v1 | keltner_20_breakout | 10000.00 | 0.00 | 대기 /  / 새 신호 대기 |
| v1 | opening_range_30m | 10069.33 | 69.33 | buy /  / 뉴욕 09:30·09:45 두 완료 봉 최고가를 10:00 이후 종가가 돌파; 조건 충족; close=721.16, opening_high=718.07 |
| v2 | cash | 10000.00 | 0.00 | 대기 /  / 새 신호 대기 |
| v2 | buy_hold | 9063.08 | -936.92 | 중단: 손실 한도 / buy / partial / 직전 완료 봉 목표 비중 100%; 다음 봉 시가 가정 |
| v2 | trend_8_26 | 9800.52 | -199.48 | buy / partial / 직전 완료 봉 목표 비중 100%; 다음 봉 시가 가정 |
| v2 | momentum_26 | 9775.40 | -224.60 | sell / filled / 직전 완료 봉 목표 비중 0%; 다음 봉 시가 가정 |
| v2 | breakout_8 | 9506.39 | -493.61 | sell / filled / 직전 완료 봉 목표 비중 0%; 다음 봉 시가 가정 |
| v2 | reversion_12 | 8936.51 | -1063.49 | 중단: 손실 한도 / buy / partial / 직전 완료 봉 목표 비중 100%; 다음 봉 시가 가정 |
| v2 | volume_26 | 9192.09 | -807.91 | 중단: 손실 한도 / buy / partial / 직전 완료 봉 목표 비중 100%; 다음 봉 시가 가정 |
| v2 | trend_8_26 AND momentum_26 | 9914.96 | -85.04 | sell / filled / 직전 완료 봉 목표 비중 0%; 다음 봉 시가 가정 |
| v2 | trend_8_26 + momentum_26 | 9788.13 | -211.87 | sell / filled / 직전 완료 봉 목표 비중 50%; 다음 봉 시가 가정 |
| v2 | trend_8_26 AND breakout_8 | 9765.08 | -234.92 | sell / filled / 직전 완료 봉 목표 비중 0%; 다음 봉 시가 가정 |
| v2 | trend_8_26 + breakout_8 | 9652.75 | -347.25 | sell / filled / 직전 완료 봉 목표 비중 50%; 다음 봉 시가 가정 |
| v2 | trend_8_26 AND reversion_12 | 9738.62 | -261.38 | sell / filled / 직전 완료 봉 목표 비중 0%; 다음 봉 시가 가정 |
| v2 | trend_8_26 + reversion_12 | 9543.01 | -456.99 | sell / filled / 직전 완료 봉 목표 비중 50%; 다음 봉 시가 가정 |
| v2 | trend_8_26 AND volume_26 | 10035.44 | 35.44 | sell / filled / 직전 완료 봉 목표 비중 0%; 다음 봉 시가 가정 |
| v2 | trend_8_26 + volume_26 | 9593.36 | -406.64 | sell / filled / 직전 완료 봉 목표 비중 50%; 다음 봉 시가 가정 |
| v2 | momentum_26 AND breakout_8 | 9776.83 | -223.17 | sell / filled / 직전 완료 봉 목표 비중 0%; 다음 봉 시가 가정 |
| v2 | momentum_26 + breakout_8 | 9640.20 | -359.80 | sell / filled / 직전 완료 봉 목표 비중 0%; 다음 봉 시가 가정 |
| v2 | momentum_26 AND reversion_12 | 9755.55 | -244.45 | sell / filled / 직전 완료 봉 목표 비중 0%; 다음 봉 시가 가정 |
| v2 | momentum_26 + reversion_12 | 9510.81 | -489.19 | sell / filled / 직전 완료 봉 목표 비중 0%; 다음 봉 시가 가정 |
| v2 | momentum_26 AND volume_26 | 10032.13 | 32.13 | sell / filled / 직전 완료 봉 목표 비중 0%; 다음 봉 시가 가정 |
| v2 | momentum_26 + volume_26 | 9581.08 | -418.92 | sell / filled / 직전 완료 봉 목표 비중 0%; 다음 봉 시가 가정 |
| v2 | breakout_8 AND reversion_12 | 10000.00 | 0.00 | 대기 /  / 새 신호 대기 |
| v2 | breakout_8 + reversion_12 | 9610.18 | -389.82 | 중단: 손실 한도 / sell / filled / 직전 완료 봉 목표 비중 0%; 다음 봉 시가 가정 |
| v2 | breakout_8 AND volume_26 | 9982.12 | -17.88 | sell / filled / 직전 완료 봉 목표 비중 0%; 다음 봉 시가 가정 |
| v2 | breakout_8 + volume_26 | 9448.42 | -551.58 | sell / filled / 직전 완료 봉 목표 비중 0%; 다음 봉 시가 가정 |
| v2 | reversion_12 AND volume_26 | 9128.50 | -871.50 | 중단: 손실 한도 / buy / partial / 직전 완료 봉 목표 비중 100%; 다음 봉 시가 가정 |
| v2 | reversion_12 + volume_26 | 9330.33 | -669.67 | 중단: 손실 한도 / sell / filled / 직전 완료 봉 목표 비중 50%; 다음 봉 시가 가정 |
| v2 | ema_12_26 | 9860.50 | -139.50 | sell / filled / EMA12 > EMA26; 조건 미충족; EMA12=735.622, EMA26=735.711; 직전 완료 봉 목표를 다음 봉 시가에 모의 적용 |
| v2 | macd_12_26_9 | 9902.20 | -97.80 | sell / filled / MACD > 신호선 그리고 MACD > 0; 조건 미충족; MACD=0.746548, signal9=0.752293; 직전 완료 봉 목표를 다음 봉 시가에 모의 적용 |
| v2 | rsi_14_recovery | 9995.22 | -4.78 | sell / filled / 직전 RSI14 < 30, 현재 RSI14 >= 30 (한 봉 목표); 조건 미충족; RSI14=43.621, previous_RSI14=38.5787; 직전 완료 봉 목표를 다음 봉 시가에 모의 적용 |
| v2 | bollinger_20_reentry | 9771.22 | -228.78 | sell / filled / 직전 종가 < 직전 하단밴드, 현재 하단밴드 <= 종가 <= SMA20 (한 봉 목표); 조건 미충족; close=721.16, lower20=716.851, SMA20=725.821, previous_lower20=717.276; 직전 완료 봉 목표를 다음 봉 시가에 모의 적용 |
| v2 | donchian_20 | 9948.84 | -51.16 | sell / filled / 종가 > 현재 봉을 제외한 직전 20봉 최고가; 조건 미충족; close=739.81, prior_high20=742.28; 직전 완료 봉 목표를 다음 봉 시가에 모의 적용 |
| v2 | atr_14_breakout | 9767.92 | -232.08 | sell / filled / 종가 > 직전 종가 + 직전 ATR14 그리고 종가 > EMA26; 조건 미충족; close=732.42, threshold=735.931, prior_ATR14=4.99094, EMA26=726.612; 직전 완료 봉 목표를 다음 봉 시가에 모의 적용 |
| v2 | session_vwap | 9423.88 | -576.12 | buy / partial / 종가 > 뉴욕 거래일별 누적 전형가격 VWAP; 조건 충족; close=717.87, session_VWAP=713.405, session_volume=283277; 직전 완료 봉 목표를 다음 봉 시가에 모의 적용 |
| v2 | obv_20 | 9675.93 | -324.07 | sell / filled / OBV > OBV의 SMA20 그리고 종가 > EMA26; 조건 미충족; OBV=-5.85317e+06, OBV_SMA20=-5.80449e+06, close=725.22, EMA26=726.751; 직전 완료 봉 목표를 다음 봉 시가에 모의 적용 |
| v2 | stochastic_14_3_recovery | 9843.26 | -156.74 | sell / filled / 직전 %K14 < 20에서 %K14가 %D3 상향 돌파 (한 봉 목표); 조건 미충족; K14=59.6496, D3=39.2535, previous_K14=43.8356, previous_D3=33.8642; 직전 완료 봉 목표를 다음 봉 시가에 모의 적용 |
| v2 | mfi_14_recovery | 10064.61 | 64.61 | sell / filled / 직전 MFI14 < 20, 현재 MFI14 >= 20 (한 봉 목표); 조건 미충족; MFI14=32.7313, previous_MFI14=24.1736; 직전 완료 봉 목표를 다음 봉 시가에 모의 적용 |
| v2 | adx_14_trend | 10000.00 | 0.00 | 대기 /  / 새 신호 대기 |
| v2 | aroon_25_trend | 10029.14 | 29.14 | sell / filled / Aroon25 Up > 70 그리고 Down < 30 (동률이면 최신 극값); 조건 미충족; Aroon_up=88, Aroon_down=48; 직전 완료 봉 목표를 다음 봉 시가에 모의 적용 |
| v2 | cci_20_momentum | 9886.36 | -113.64 | sell / filled / CCI20 > 100 (전형가격·평균절대편차); 조건 미충족; CCI20=20.3547; 직전 완료 봉 목표를 다음 봉 시가에 모의 적용 |
| v2 | williams_14_recovery | 9999.06 | -0.94 | sell / filled / 직전 Williams %R14 < -80, 현재 >= -80 (한 봉 목표); 조건 미충족; Williams_R14=-40.3504, previous_R14=-56.1644; 직전 완료 봉 목표를 다음 봉 시가에 모의 적용 |
| v2 | cmf_20_accumulation | 9775.15 | -224.85 | buy / partial / Chaikin Money Flow20 > 0.1; 조건 충족; CMF20=0.130083, volume20=2.38752e+06; 직전 완료 봉 목표를 다음 봉 시가에 모의 적용 |
| v2 | chaikin_3_10 | 9544.75 | -455.25 | 중단: 손실 한도 / buy / partial / ADL의 EMA3 - EMA10 > 0 그리고 종가 > EMA26; 조건 충족; Chaikin3_10=293683, ADL=-4.91156e+06, close=739.58, EMA26=736.187; 직전 완료 봉 목표를 다음 봉 시가에 모의 적용 |
| v2 | roc_10_momentum | 9961.14 | -38.86 | sell / filled / 10봉 ROC > 1% 그리고 종가 > EMA26; 조건 미충족; ROC10_percent=-0.134597, close=734.53, EMA26=735.486; 직전 완료 봉 목표를 다음 봉 시가에 모의 적용 |
| v2 | trix_15_trend | 9554.37 | -445.63 | 중단: 손실 한도 / buy / partial / 15봉 삼중 EMA의 1봉 변화율 TRIX > 0 그리고 종가 > EMA26; 조건 충족; TRIX15_percent=0.0196284, close=739.58, EMA26=736.187; 직전 완료 봉 목표를 다음 봉 시가에 모의 적용 |
| v2 | keltner_20_breakout | 10000.00 | 0.00 | 대기 /  / 새 신호 대기 |
| v2 | opening_range_30m | 10066.31 | 66.31 | buy / partial / 뉴욕 09:30·09:45 두 완료 봉 최고가를 10:00 이후 종가가 돌파; 조건 충족; close=721.16, opening_high=718.07; 직전 완료 봉 목표를 다음 봉 시가에 모의 적용 |

### 같은 기간의 비용·노출 비교 (사후 연구)

| 전략 | 비용 전 | 비용 후 | 100% 보유 | 같은 평균 노출 보유 | 평균 노출 |
|---|---:|---:|---:|---:|---:|
| cash | 0.00% | 0.00% | -12.55% | -0.00% | 0.00% |
| buy_hold | -12.19% | -12.55% | -12.55% | -12.55% | 100.00% |
| trend_8_26 | -0.90% | -4.58% | -12.55% | -5.59% | 43.42% |
| momentum_26 | -3.05% | -6.64% | -12.55% | -5.39% | 41.84% |
| breakout_8 | -3.61% | -15.38% | -12.55% | -1.75% | 13.42% |
| reversion_12 | -3.10% | -15.99% | -12.55% | -3.61% | 27.89% |
| volume_26 | -2.12% | -9.25% | -12.55% | -1.06% | 8.16% |
| trend_8_26 AND momentum_26 | 0.69% | -1.81% | -12.55% | -4.72% | 36.58% |
| trend_8_26 + momentum_26 | -1.97% | -5.61% | -12.55% | -5.49% | 42.63% |
| trend_8_26 AND breakout_8 | -2.00% | -7.99% | -12.55% | -0.83% | 6.32% |
| trend_8_26 + breakout_8 | -2.23% | -9.93% | -12.55% | -3.68% | 28.43% |
| trend_8_26 AND reversion_12 | 0.04% | -6.07% | -12.55% | -0.79% | 6.05% |
| trend_8_26 + reversion_12 | -1.94% | -9.87% | -12.55% | -4.60% | 35.66% |
| trend_8_26 AND volume_26 | 1.79% | 0.09% | -12.55% | -0.21% | 1.58% |
| trend_8_26 + volume_26 | -1.46% | -6.53% | -12.55% | -3.34% | 25.79% |
| momentum_26 AND breakout_8 | -2.64% | -8.96% | -12.55% | -0.86% | 6.58% |
| momentum_26 + breakout_8 | -3.29% | -11.09% | -12.55% | -3.58% | 27.64% |
| momentum_26 AND reversion_12 | -3.16% | -8.69% | -12.55% | -0.76% | 5.79% |
| momentum_26 + reversion_12 | -3.01% | -10.67% | -12.55% | -4.50% | 34.87% |
| momentum_26 AND volume_26 | 1.75% | 0.06% | -12.55% | -0.17% | 1.32% |
| momentum_26 + volume_26 | -2.53% | -7.54% | -12.55% | -3.24% | 25.00% |
| breakout_8 AND reversion_12 | 0.00% | 0.00% | -12.55% | -0.00% | 0.00% |
| breakout_8 + reversion_12 | -3.29% | -14.77% | -12.55% | -2.68% | 20.67% |
| breakout_8 AND volume_26 | 0.66% | -0.18% | -12.55% | -0.07% | 0.53% |
| breakout_8 + volume_26 | -2.83% | -11.80% | -12.55% | -1.41% | 10.80% |
| reversion_12 AND volume_26 | -0.54% | -5.03% | -12.55% | -0.69% | 5.26% |
| reversion_12 + volume_26 | -2.57% | -12.11% | -12.55% | -2.34% | 18.03% |
| ema_12_26 | -1.56% | -3.20% | -12.55% | -5.12% | 39.74% |
| macd_12_26_9 | 1.68% | -0.85% | -12.55% | -3.14% | 24.21% |
| rsi_14_recovery | -0.17% | -6.26% | -12.55% | -0.52% | 3.95% |
| bollinger_20_reentry | 0.57% | -5.57% | -12.55% | -0.52% | 3.95% |
| donchian_20 | -1.16% | -4.82% | -12.55% | -0.58% | 4.47% |
| atr_14_breakout | -1.46% | -7.48% | -12.55% | -0.55% | 4.21% |
| session_vwap | -0.81% | -13.29% | -12.55% | -5.99% | 46.58% |
| obv_20 | -4.81% | -13.93% | -12.55% | -2.60% | 20.00% |
| stochastic_14_3_recovery | -2.10% | -12.96% | -12.55% | -0.96% | 7.37% |
| mfi_14_recovery | 1.96% | -1.00% | -12.55% | -0.24% | 1.84% |
| adx_14_trend | -2.02% | -4.05% | -12.55% | -1.10% | 8.42% |
| aroon_25_trend | -0.29% | -3.58% | -12.55% | -1.41% | 10.79% |
| cci_20_momentum | -4.62% | -9.68% | -12.55% | -1.78% | 13.68% |
| williams_14_recovery | 0.05% | -8.78% | -12.55% | -0.76% | 5.79% |
| cmf_20_accumulation | -4.12% | -10.73% | -12.55% | -1.99% | 15.26% |
| chaikin_3_10 | -6.34% | -15.32% | -12.55% | -3.71% | 28.68% |
| roc_10_momentum | -1.68% | -6.91% | -12.55% | -1.61% | 12.37% |
| trix_15_trend | -1.44% | -5.49% | -12.55% | -3.98% | 30.79% |
| keltner_20_breakout | -2.87% | -5.29% | -12.55% | -0.34% | 2.63% |
| opening_range_30m | 6.66% | 1.84% | -12.55% | -2.94% | 22.63% |

동일 구간·초기 자금, 종료 시 청산 비용 포함. 노출 맞춤은 사후 설명용이며 v2 실제 계좌 성과가 아닙니다.
[낙폭 분해·비용 영향·전체 구간](CAT/comparison.json)

[v1 전체 기록](CAT/accounts.json) · [v2 전체 기록](CAT/accounts-v2.json)

## WMT 계좌

| 모델 | 전략 | 평가액 USD | 손익 USD | 최근 매매·이유 |
|---|---|---:|---:|---|
| v1 | cash | 10000.00 | 0.00 | 대기 /  / 새 신호 대기 |
| v1 | buy_hold | 9980.87 | -19.13 | buy /  / buy_hold: prior completed bar target 100%; next bar open simulation |
| v1 | trend_8_26 | 9791.85 | -208.15 | sell /  / trend_8_26: prior completed bar target 0%; next bar open simulation |
| v1 | momentum_26 | 9801.37 | -198.63 | sell /  / momentum_26: prior completed bar target 0%; next bar open simulation |
| v1 | breakout_8 | 9728.67 | -271.33 | sell /  / breakout_8: prior completed bar target 0%; next bar open simulation |
| v1 | reversion_12 | 9716.63 | -283.37 | buy /  / reversion_12: prior completed bar target 100%; next bar open simulation |
| v1 | volume_26 | 9755.08 | -244.92 | sell /  / volume_26: prior completed bar target 0%; next bar open simulation |
| v1 | trend_8_26 AND momentum_26 | 9811.64 | -188.36 | sell /  / trend_8_26 AND momentum_26: prior completed bar target 0%; next bar open simulation |
| v1 | trend_8_26 + momentum_26 | 9796.64 | -203.36 | sell /  / trend_8_26 + momentum_26: prior completed bar target 0%; next bar open simulation |
| v1 | trend_8_26 AND breakout_8 | 9854.29 | -145.71 | sell /  / trend_8_26 AND breakout_8: prior completed bar target 0%; next bar open simulation |
| v1 | trend_8_26 + breakout_8 | 9760.28 | -239.72 | sell /  / trend_8_26 + breakout_8: prior completed bar target 0%; next bar open simulation |
| v1 | trend_8_26 AND reversion_12 | 9798.51 | -201.49 | sell /  / trend_8_26 AND reversion_12: prior completed bar target 0%; next bar open simulation |
| v1 | trend_8_26 + reversion_12 | 9793.45 | -206.55 | buy /  / trend_8_26 + reversion_12: prior completed bar target 50%; next bar open simulation |
| v1 | trend_8_26 AND volume_26 | 9837.96 | -162.04 | sell /  / trend_8_26 AND volume_26: prior completed bar target 0%; next bar open simulation |
| v1 | trend_8_26 + volume_26 | 9773.64 | -226.36 | sell /  / trend_8_26 + volume_26: prior completed bar target 0%; next bar open simulation |
| v1 | momentum_26 AND breakout_8 | 9816.19 | -183.81 | sell /  / momentum_26 AND breakout_8: prior completed bar target 0%; next bar open simulation |
| v1 | momentum_26 + breakout_8 | 9823.93 | -176.07 | sell /  / momentum_26 + breakout_8: prior completed bar target 0%; next bar open simulation |
| v1 | momentum_26 AND reversion_12 | 9935.88 | -64.12 | sell /  / momentum_26 AND reversion_12: prior completed bar target 0%; next bar open simulation |
| v1 | momentum_26 + reversion_12 | 9857.00 | -143.00 | buy /  / momentum_26 + reversion_12: prior completed bar target 50%; next bar open simulation |
| v1 | momentum_26 AND volume_26 | 9905.94 | -94.06 | sell /  / momentum_26 AND volume_26: prior completed bar target 0%; next bar open simulation |
| v1 | momentum_26 + volume_26 | 9817.50 | -182.50 | sell /  / momentum_26 + volume_26: prior completed bar target 0%; next bar open simulation |
| v1 | breakout_8 AND reversion_12 | 10000.00 | 0.00 | 대기 /  / 새 신호 대기 |
| v1 | breakout_8 + reversion_12 | 9761.52 | -238.48 | buy /  / breakout_8 + reversion_12: prior completed bar target 50%; next bar open simulation |
| v1 | breakout_8 AND volume_26 | 9850.09 | -149.91 | sell /  / breakout_8 AND volume_26: prior completed bar target 0%; next bar open simulation |
| v1 | breakout_8 + volume_26 | 9741.88 | -258.12 | sell /  / breakout_8 + volume_26: prior completed bar target 0%; next bar open simulation |
| v1 | reversion_12 AND volume_26 | 9905.10 | -94.90 | sell /  / reversion_12 AND volume_26: prior completed bar target 0%; next bar open simulation |
| v1 | reversion_12 + volume_26 | 9774.80 | -225.20 | buy /  / reversion_12 + volume_26: prior completed bar target 50%; next bar open simulation |
| v1 | ema_12_26 | 9906.58 | -93.42 | sell /  / EMA12 > EMA26; 조건 미충족; EMA12=118.808, EMA26=118.852 |
| v1 | macd_12_26_9 | 9985.46 | -14.54 | sell /  / MACD > 신호선 그리고 MACD > 0; 조건 미충족; MACD=0.122825, signal9=0.127837 |
| v1 | rsi_14_recovery | 10000.00 | 0.00 | 대기 /  / 새 신호 대기 |
| v1 | bollinger_20_reentry | 9943.24 | -56.76 | sell /  / 직전 종가 < 직전 하단밴드, 현재 하단밴드 <= 종가 <= SMA20 (한 봉 목표); 조건 미충족; close=118.09, lower20=118.109, SMA20=118.912, previous_lower20=118.251 |
| v1 | donchian_20 | 9935.97 | -64.03 | sell /  / 종가 > 현재 봉을 제외한 직전 20봉 최고가; 조건 미충족; close=119.52, prior_high20=120.5 |
| v1 | atr_14_breakout | 9915.82 | -84.18 | sell /  / 종가 > 직전 종가 + 직전 ATR14 그리고 종가 > EMA26; 조건 미충족; close=119.52, threshold=120.186, prior_ATR14=0.395874, EMA26=118.952 |
| v1 | session_vwap | 9838.24 | -161.76 | sell /  / 종가 > 뉴욕 거래일별 누적 전형가격 VWAP; 조건 미충족; close=118.71, session_VWAP=118.72, session_volume=1.73369e+07 |
| v1 | obv_20 | 9857.61 | -142.39 | sell /  / OBV > OBV의 SMA20 그리고 종가 > EMA26; 조건 미충족; OBV=1.6238e+07, OBV_SMA20=1.74966e+07, close=118.945, EMA26=118.951 |
| v1 | stochastic_14_3_recovery | 9822.36 | -177.64 | buy /  / 직전 %K14 < 20에서 %K14가 %D3 상향 돌파 (한 봉 목표); 조건 충족; K14=2.82256, D3=2.48296, previous_K14=4.6263, previous_D3=5.81143 |
| v1 | mfi_14_recovery | 10000.00 | 0.00 | 대기 /  / 새 신호 대기 |
| v1 | adx_14_trend | 9991.69 | -8.31 | sell /  / Wilder ADX14 >= 25 그리고 +DI14 > -DI14; 조건 미충족; ADX14=24.5142, plus_DI14=24.7537, minus_DI14=21.6519 |
| v1 | aroon_25_trend | 9947.63 | -52.37 | sell /  / Aroon25 Up > 70 그리고 Down < 30 (동률이면 최신 극값); 조건 미충족; Aroon_up=68, Aroon_down=4 |
| v1 | cci_20_momentum | 9772.81 | -227.19 | sell /  / CCI20 > 100 (전형가격·평균절대편차); 조건 미충족; CCI20=38.8365 |
| v1 | williams_14_recovery | 9911.09 | -88.91 | sell /  / 직전 Williams %R14 < -80, 현재 >= -80 (한 봉 목표); 조건 미충족; Williams_R14=-89.406, previous_R14=-71.5024 |
| v1 | cmf_20_accumulation | 9898.70 | -101.30 | sell /  / Chaikin Money Flow20 > 0.1; 조건 미충족; CMF20=0.0888031, volume20=1.50234e+07 |
| v1 | chaikin_3_10 | 9762.96 | -237.04 | sell /  / ADL의 EMA3 - EMA10 > 0 그리고 종가 > EMA26; 조건 미충족; Chaikin3_10=-178256, ADL=1.4762e+07, close=119.52, EMA26=118.952 |
| v1 | roc_10_momentum | 10000.00 | 0.00 | 대기 /  / 새 신호 대기 |
| v1 | trix_15_trend | 9708.65 | -291.35 | sell /  / 15봉 삼중 EMA의 1봉 변화율 TRIX > 0 그리고 종가 > EMA26; 조건 미충족; TRIX15_percent=0.0142754, close=118.77, EMA26=118.947 |
| v1 | keltner_20_breakout | 9935.97 | -64.03 | sell /  / 종가 > EMA20 + 2 x Wilder ATR14; 조건 미충족; close=119.52, upper_Keltner=119.83, EMA20=119.013, ATR14=0.408312 |
| v1 | opening_range_30m | 9927.51 | -72.49 | sell /  / 뉴욕 09:30·09:45 두 완료 봉 최고가를 10:00 이후 종가가 돌파; 조건 미충족; close=118.85, opening_high=119.14 |
| v2 | cash | 10000.00 | 0.00 | 대기 /  / 새 신호 대기 |
| v2 | buy_hold | 10574.64 | 574.64 | buy / partial / 직전 완료 봉 목표 비중 100%; 다음 봉 시가 가정 |
| v2 | trend_8_26 | 10187.81 | 187.81 | sell / filled / 직전 완료 봉 목표 비중 0%; 다음 봉 시가 가정 |
| v2 | momentum_26 | 10200.51 | 200.51 | sell / filled / 직전 완료 봉 목표 비중 0%; 다음 봉 시가 가정 |
| v2 | breakout_8 | 9682.65 | -317.35 | sell / filled / 직전 완료 봉 목표 비중 0%; 다음 봉 시가 가정 |
| v2 | reversion_12 | 9614.21 | -385.79 | buy / partial / 직전 완료 봉 목표 비중 100%; 다음 봉 시가 가정 |
| v2 | volume_26 | 9711.50 | -288.50 | sell / filled / 직전 완료 봉 목표 비중 0%; 다음 봉 시가 가정 |
| v2 | trend_8_26 AND momentum_26 | 10206.36 | 206.36 | sell / filled / 직전 완료 봉 목표 비중 0%; 다음 봉 시가 가정 |
| v2 | trend_8_26 + momentum_26 | 10194.13 | 194.13 | sell / filled / 직전 완료 봉 목표 비중 0%; 다음 봉 시가 가정 |
| v2 | trend_8_26 AND breakout_8 | 9935.59 | -64.41 | sell / filled / 직전 완료 봉 목표 비중 0%; 다음 봉 시가 가정 |
| v2 | trend_8_26 + breakout_8 | 9932.48 | -67.52 | sell / filled / 직전 완료 봉 목표 비중 0%; 다음 봉 시가 가정 |
| v2 | trend_8_26 AND reversion_12 | 9603.42 | -396.58 | sell / filled / 직전 완료 봉 목표 비중 0%; 다음 봉 시가 가정 |
| v2 | trend_8_26 + reversion_12 | 9940.10 | -59.90 | buy / filled / 직전 완료 봉 목표 비중 50%; 다음 봉 시가 가정 |
| v2 | trend_8_26 AND volume_26 | 9784.10 | -215.90 | sell / filled / 직전 완료 봉 목표 비중 0%; 다음 봉 시가 가정 |
| v2 | trend_8_26 + volume_26 | 9948.42 | -51.58 | sell / filled / 직전 완료 봉 목표 비중 0%; 다음 봉 시가 가정 |
| v2 | momentum_26 AND breakout_8 | 9773.67 | -226.33 | sell / filled / 직전 완료 봉 목표 비중 0%; 다음 봉 시가 가정 |
| v2 | momentum_26 + breakout_8 | 10001.62 | 1.62 | sell / filled / 직전 완료 봉 목표 비중 0%; 다음 봉 시가 가정 |
| v2 | momentum_26 AND reversion_12 | 9759.91 | -240.09 | sell / filled / 직전 완료 봉 목표 비중 0%; 다음 봉 시가 가정 |
| v2 | momentum_26 + reversion_12 | 10051.16 | 51.16 | buy / filled / 직전 완료 봉 목표 비중 50%; 다음 봉 시가 가정 |
| v2 | momentum_26 AND volume_26 | 9814.68 | -185.32 | sell / filled / 직전 완료 봉 목표 비중 0%; 다음 봉 시가 가정 |
| v2 | momentum_26 + volume_26 | 9996.47 | -3.53 | sell / filled / 직전 완료 봉 목표 비중 0%; 다음 봉 시가 가정 |
| v2 | breakout_8 AND reversion_12 | 10000.00 | 0.00 | 대기 /  / 새 신호 대기 |
| v2 | breakout_8 + reversion_12 | 9710.36 | -289.64 | buy / filled / 직전 완료 봉 목표 비중 50%; 다음 봉 시가 가정 |
| v2 | breakout_8 AND volume_26 | 9795.19 | -204.81 | sell / filled / 직전 완료 봉 목표 비중 0%; 다음 봉 시가 가정 |
| v2 | breakout_8 + volume_26 | 9698.42 | -301.58 | sell / filled / 직전 완료 봉 목표 비중 0%; 다음 봉 시가 가정 |
| v2 | reversion_12 AND volume_26 | 9912.80 | -87.20 | sell / filled / 직전 완료 봉 목표 비중 0%; 다음 봉 시가 가정 |
| v2 | reversion_12 + volume_26 | 9703.23 | -296.77 | buy / filled / 직전 완료 봉 목표 비중 50%; 다음 봉 시가 가정 |
| v2 | ema_12_26 | 9902.61 | -97.39 | sell / filled / EMA12 > EMA26; 조건 미충족; EMA12=118.808, EMA26=118.852; 직전 완료 봉 목표를 다음 봉 시가에 모의 적용 |
| v2 | macd_12_26_9 | 9981.46 | -18.54 | sell / filled / MACD > 신호선 그리고 MACD > 0; 조건 미충족; MACD=0.122825, signal9=0.127837; 직전 완료 봉 목표를 다음 봉 시가에 모의 적용 |
| v2 | rsi_14_recovery | 10000.00 | 0.00 | 대기 /  / 새 신호 대기 |
| v2 | bollinger_20_reentry | 9941.25 | -58.75 | sell / filled / 직전 종가 < 직전 하단밴드, 현재 하단밴드 <= 종가 <= SMA20 (한 봉 목표); 조건 미충족; close=118.09, lower20=118.109, SMA20=118.912, previous_lower20=118.251; 직전 완료 봉 목표를 다음 봉 시가에 모의 적용 |
| v2 | donchian_20 | 9933.99 | -66.01 | sell / filled / 종가 > 현재 봉을 제외한 직전 20봉 최고가; 조건 미충족; close=119.52, prior_high20=120.5; 직전 완료 봉 목표를 다음 봉 시가에 모의 적용 |
| v2 | atr_14_breakout | 9911.85 | -88.15 | sell / filled / 종가 > 직전 종가 + 직전 ATR14 그리고 종가 > EMA26; 조건 미충족; close=119.52, threshold=120.186, prior_ATR14=0.395874, EMA26=118.952; 직전 완료 봉 목표를 다음 봉 시가에 모의 적용 |
| v2 | session_vwap | 9826.44 | -173.56 | sell / filled / 종가 > 뉴욕 거래일별 누적 전형가격 VWAP; 조건 미충족; close=118.71, session_VWAP=118.72, session_volume=1.73369e+07; 직전 완료 봉 목표를 다음 봉 시가에 모의 적용 |
| v2 | obv_20 | 9847.76 | -152.24 | sell / filled / OBV > OBV의 SMA20 그리고 종가 > EMA26; 조건 미충족; OBV=1.6238e+07, OBV_SMA20=1.74966e+07, close=118.945, EMA26=118.951; 직전 완료 봉 목표를 다음 봉 시가에 모의 적용 |
| v2 | stochastic_14_3_recovery | 9815.49 | -184.51 | buy / partial / 직전 %K14 < 20에서 %K14가 %D3 상향 돌파 (한 봉 목표); 조건 충족; K14=2.82256, D3=2.48296, previous_K14=4.6263, previous_D3=5.81143; 직전 완료 봉 목표를 다음 봉 시가에 모의 적용 |
| v2 | mfi_14_recovery | 10000.00 | 0.00 | 대기 /  / 새 신호 대기 |
| v2 | adx_14_trend | 9989.70 | -10.30 | sell / filled / Wilder ADX14 >= 25 그리고 +DI14 > -DI14; 조건 미충족; ADX14=24.5142, plus_DI14=24.7537, minus_DI14=21.6519; 직전 완료 봉 목표를 다음 봉 시가에 모의 적용 |
| v2 | aroon_25_trend | 9943.65 | -56.35 | sell / filled / Aroon25 Up > 70 그리고 Down < 30 (동률이면 최신 극값); 조건 미충족; Aroon_up=68, Aroon_down=4; 직전 완료 봉 목표를 다음 봉 시가에 모의 적용 |
| v2 | cci_20_momentum | 9766.95 | -233.05 | sell / filled / CCI20 > 100 (전형가격·평균절대편차); 조건 미충족; CCI20=38.8365; 직전 완료 봉 목표를 다음 봉 시가에 모의 적용 |
| v2 | williams_14_recovery | 9907.12 | -92.88 | sell / filled / 직전 Williams %R14 < -80, 현재 >= -80 (한 봉 목표); 조건 미충족; Williams_R14=-89.406, previous_R14=-71.5024; 직전 완료 봉 목표를 다음 봉 시가에 모의 적용 |
| v2 | cmf_20_accumulation | 9890.78 | -109.22 | sell / filled / Chaikin Money Flow20 > 0.1; 조건 미충족; CMF20=0.0888031, volume20=1.50234e+07; 직전 완료 봉 목표를 다음 봉 시가에 모의 적용 |
| v2 | chaikin_3_10 | 9749.30 | -250.70 | sell / filled / ADL의 EMA3 - EMA10 > 0 그리고 종가 > EMA26; 조건 미충족; Chaikin3_10=-178256, ADL=1.4762e+07, close=119.52, EMA26=118.952; 직전 완료 봉 목표를 다음 봉 시가에 모의 적용 |
| v2 | roc_10_momentum | 10000.00 | 0.00 | 대기 /  / 새 신호 대기 |
| v2 | trix_15_trend | 9697.01 | -302.99 | sell / filled / 15봉 삼중 EMA의 1봉 변화율 TRIX > 0 그리고 종가 > EMA26; 조건 미충족; TRIX15_percent=0.0142754, close=118.77, EMA26=118.947; 직전 완료 봉 목표를 다음 봉 시가에 모의 적용 |
| v2 | keltner_20_breakout | 9933.99 | -66.01 | sell / filled / 종가 > EMA20 + 2 x Wilder ATR14; 조건 미충족; close=119.52, upper_Keltner=119.83, EMA20=119.013, ATR14=0.408312; 직전 완료 봉 목표를 다음 봉 시가에 모의 적용 |
| v2 | opening_range_30m | 9925.52 | -74.48 | sell / filled / 뉴욕 09:30·09:45 두 완료 봉 최고가를 10:00 이후 종가가 돌파; 조건 미충족; close=118.85, opening_high=119.14; 직전 완료 봉 목표를 다음 봉 시가에 모의 적용 |

### 같은 기간의 비용·노출 비교 (사후 연구)

| 전략 | 비용 전 | 비용 후 | 100% 보유 | 같은 평균 노출 보유 | 평균 노출 |
|---|---:|---:|---:|---:|---:|
| cash | 0.00% | 0.00% | 10.11% | 0.00% | 0.00% |
| buy_hold | 10.57% | 10.11% | 10.11% | 10.11% | 100.00% |
| trend_8_26 | 7.47% | 3.92% | 10.11% | 7.05% | 70.53% |
| momentum_26 | 9.58% | 3.32% | 10.11% | 7.11% | 71.05% |
| breakout_8 | 6.11% | -10.30% | 10.11% | 2.54% | 25.79% |
| reversion_12 | 3.51% | -8.36% | 10.11% | 1.75% | 17.89% |
| volume_26 | 0.01% | -6.09% | 10.11% | 0.57% | 5.79% |
| trend_8_26 AND momentum_26 | 7.80% | 2.50% | 10.11% | 6.35% | 63.68% |
| trend_8_26 + momentum_26 | 8.52% | 3.62% | 10.11% | 7.08% | 70.79% |
| trend_8_26 AND breakout_8 | 6.58% | -6.83% | 10.11% | 2.12% | 21.58% |
| trend_8_26 + breakout_8 | 6.80% | -3.45% | 10.11% | 4.78% | 48.16% |
| trend_8_26 AND reversion_12 | -0.24% | -6.33% | 10.11% | 0.72% | 7.37% |
| trend_8_26 + reversion_12 | 5.51% | -1.79% | 10.11% | 4.38% | 44.22% |
| trend_8_26 AND volume_26 | -0.30% | -3.19% | 10.11% | 0.26% | 2.63% |
| trend_8_26 + volume_26 | 3.71% | -0.78% | 10.11% | 3.77% | 38.16% |
| momentum_26 AND breakout_8 | 6.62% | -7.18% | 10.11% | 2.25% | 22.89% |
| momentum_26 + breakout_8 | 7.84% | -2.91% | 10.11% | 4.80% | 48.43% |
| momentum_26 AND reversion_12 | 1.24% | -4.94% | 10.11% | 0.77% | 7.89% |
| momentum_26 + reversion_12 | 6.54% | 0.01% | 10.11% | 4.41% | 44.48% |
| momentum_26 AND volume_26 | 1.58% | -3.01% | 10.11% | 0.31% | 3.16% |
| momentum_26 + volume_26 | 4.72% | -1.07% | 10.11% | 3.80% | 38.42% |
| breakout_8 AND reversion_12 | 0.00% | 0.00% | 10.11% | 0.00% | 0.00% |
| breakout_8 + reversion_12 | 4.83% | -8.57% | 10.11% | 2.15% | 21.85% |
| breakout_8 AND volume_26 | 0.78% | -2.14% | 10.11% | 0.21% | 2.11% |
| breakout_8 + volume_26 | 3.04% | -8.02% | 10.11% | 1.55% | 15.80% |
| reversion_12 AND volume_26 | -1.05% | -3.51% | 10.11% | 0.18% | 1.84% |
| reversion_12 + volume_26 | 1.75% | -6.65% | 10.11% | 1.16% | 11.85% |
| ema_12_26 | 11.20% | 9.81% | 10.11% | 7.30% | 72.89% |
| macd_12_26_9 | 8.67% | 4.64% | 10.11% | 3.59% | 36.32% |
| rsi_14_recovery | -0.25% | -1.50% | 10.11% | 0.08% | 0.79% |
| bollinger_20_reentry | 1.24% | -1.70% | 10.11% | 0.18% | 1.84% |
| donchian_20 | 4.54% | -7.83% | 10.11% | 1.31% | 13.42% |
| atr_14_breakout | -0.86% | -10.74% | 10.11% | 0.75% | 7.63% |
| session_vwap | 9.55% | -0.54% | 10.11% | 5.71% | 57.37% |
| obv_20 | 10.73% | 2.67% | 10.11% | 5.66% | 56.84% |
| stochastic_14_3_recovery | 1.15% | -8.16% | 10.11% | 0.59% | 6.05% |
| mfi_14_recovery | 0.02% | -0.81% | 10.11% | 0.05% | 0.53% |
| adx_14_trend | 8.84% | 6.13% | 10.11% | 5.04% | 50.79% |
| aroon_25_trend | 5.98% | 0.77% | 10.11% | 3.24% | 32.89% |
| cci_20_momentum | 5.91% | -2.63% | 10.11% | 3.22% | 32.63% |
| williams_14_recovery | 0.10% | -7.58% | 10.11% | 0.49% | 5.00% |
| cmf_20_accumulation | 9.11% | -0.10% | 10.11% | 3.61% | 36.58% |
| chaikin_3_10 | 9.43% | 0.61% | 10.11% | 5.23% | 52.63% |
| roc_10_momentum | -0.30% | -5.20% | 10.11% | 1.42% | 14.47% |
| trix_15_trend | 10.97% | 6.86% | 10.11% | 6.49% | 65.00% |
| keltner_20_breakout | 6.59% | 0.08% | 10.11% | 2.62% | 26.58% |
| opening_range_30m | 9.76% | 4.80% | 10.11% | 3.56% | 36.05% |

동일 구간·초기 자금, 종료 시 청산 비용 포함. 노출 맞춤은 사후 설명용이며 v2 실제 계좌 성과가 아닙니다.
[낙폭 분해·비용 영향·전체 구간](WMT/comparison.json)

[v1 전체 기록](WMT/accounts.json) · [v2 전체 기록](WMT/accounts-v2.json)
