# 모의투자 운영 현황

[PC·서버 장애 진단과 복구 방법](https://github.com/BaekJaeYeol/paper-trading-program/blob/main/investment-lab/docs/failure-recovery.md)

이번 실행 복구: {}

완료 봉 확인 주기: 기록 9/16회 · 기록 없는 예정 7회 · 아직 판정 전 10회 · 주의: 예약 시작 지연 또는 실행·저장 누락을 확인하세요.

[주기 판정 기준](https://github.com/BaekJaeYeol/paper-trading-program/blob/main/investment-lab/docs/session-coverage.md)

최근 확인: 2026-10-20T17:52:00.468478+00:00 (UTC)
다음 15분 확인 목표 (세션 실행 중에만 적용): 2026-10-20T18:07:00+00:00 (UTC, 실행 지연 가능)

실제 주문 없음. v1 기존 계좌와 v2 새 계좌의 시작일이 다르므로 수익률을 직접 우열 비교하지 마세요.
v2는 다음 봉 시가에 비용·스프레드·직전 거래량 제한을 적용한 가상 체결입니다. 미체결 잔량은 만료됩니다.

| 종목 | 상태 | 최근 성공 UTC | 마지막 완료 봉 UTC | 이번 새 봉 |
|---|---|---|---|---|
| SPY | updated | 2026-10-20T17:52:00.468478+00:00 | 2026-10-20T17:30:00+00:00 | 1 |
| QQQ | updated | 2026-10-20T17:52:00.468478+00:00 | 2026-10-20T17:30:00+00:00 | 1 |
| IWM | updated | 2026-10-20T17:52:00.468478+00:00 | 2026-10-20T17:30:00+00:00 | 1 |
| DIA | updated | 2026-10-20T17:52:00.468478+00:00 | 2026-10-20T17:30:00+00:00 | 1 |
| MSFT | updated | 2026-10-20T17:52:00.468478+00:00 | 2026-10-20T17:30:00+00:00 | 1 |
| JPM | updated | 2026-10-20T17:52:00.468478+00:00 | 2026-10-20T17:30:00+00:00 | 1 |
| XOM | updated | 2026-10-20T17:52:00.468478+00:00 | 2026-10-20T17:30:00+00:00 | 1 |
| JNJ | updated | 2026-10-20T17:52:00.468478+00:00 | 2026-10-20T17:30:00+00:00 | 1 |
| CAT | updated | 2026-10-20T17:52:00.468478+00:00 | 2026-10-20T17:30:00+00:00 | 1 |
| WMT | updated | 2026-10-20T17:52:00.468478+00:00 | 2026-10-20T17:30:00+00:00 | 1 |

이번 실행 소요: 47.56초
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
| v1 | buy_hold | 9933.31 | -66.69 | buy /  / buy_hold: prior completed bar target 100%; next bar open simulation |
| v1 | trend_8_26 | 9828.43 | -171.57 | buy /  / trend_8_26: prior completed bar target 100%; next bar open simulation |
| v1 | momentum_26 | 9761.34 | -238.66 | buy /  / momentum_26: prior completed bar target 100%; next bar open simulation |
| v1 | breakout_8 | 9752.40 | -247.60 | sell /  / breakout_8: prior completed bar target 0%; next bar open simulation |
| v1 | reversion_12 | 9793.61 | -206.39 | sell /  / reversion_12: prior completed bar target 0%; next bar open simulation |
| v1 | volume_26 | 9661.70 | -338.30 | buy /  / volume_26: prior completed bar target 100%; next bar open simulation |
| v1 | trend_8_26 AND momentum_26 | 9762.11 | -237.89 | buy /  / trend_8_26 AND momentum_26: prior completed bar target 100%; next bar open simulation |
| v1 | trend_8_26 + momentum_26 | 9794.81 | -205.19 | buy /  / trend_8_26 + momentum_26: prior completed bar target 100%; next bar open simulation |
| v1 | trend_8_26 AND breakout_8 | 9859.41 | -140.59 | sell /  / trend_8_26 AND breakout_8: prior completed bar target 0%; next bar open simulation |
| v1 | trend_8_26 + breakout_8 | 9829.46 | -170.54 | sell /  / trend_8_26 + breakout_8: prior completed bar target 50%; next bar open simulation |
| v1 | trend_8_26 AND reversion_12 | 9869.55 | -130.45 | sell /  / trend_8_26 AND reversion_12: prior completed bar target 0%; next bar open simulation |
| v1 | trend_8_26 + reversion_12 | 9810.86 | -189.14 | sell /  / trend_8_26 + reversion_12: prior completed bar target 50%; next bar open simulation |
| v1 | trend_8_26 AND volume_26 | 9707.17 | -292.83 | buy /  / trend_8_26 AND volume_26: prior completed bar target 100%; next bar open simulation |
| v1 | trend_8_26 + volume_26 | 9744.67 | -255.33 | buy /  / trend_8_26 + volume_26: prior completed bar target 100%; next bar open simulation |
| v1 | momentum_26 AND breakout_8 | 9831.79 | -168.21 | sell /  / momentum_26 AND breakout_8: prior completed bar target 0%; next bar open simulation |
| v1 | momentum_26 + breakout_8 | 9756.86 | -243.14 | sell /  / momentum_26 + breakout_8: prior completed bar target 50%; next bar open simulation |
| v1 | momentum_26 AND reversion_12 | 9865.74 | -134.26 | sell /  / momentum_26 AND reversion_12: prior completed bar target 0%; next bar open simulation |
| v1 | momentum_26 + reversion_12 | 9816.53 | -183.47 | sell /  / momentum_26 + reversion_12: prior completed bar target 50%; next bar open simulation |
| v1 | momentum_26 AND volume_26 | 9720.69 | -279.31 | buy /  / momentum_26 AND volume_26: prior completed bar target 100%; next bar open simulation |
| v1 | momentum_26 + volume_26 | 9711.34 | -288.66 | buy /  / momentum_26 + volume_26: prior completed bar target 100%; next bar open simulation |
| v1 | breakout_8 AND reversion_12 | 10000.00 | 0.00 | 대기 /  / 새 신호 대기 |
| v1 | breakout_8 + reversion_12 | 9772.82 | -227.18 | sell /  / breakout_8 + reversion_12: prior completed bar target 0%; next bar open simulation |
| v1 | breakout_8 AND volume_26 | 9878.80 | -121.20 | sell /  / breakout_8 AND volume_26: prior completed bar target 0%; next bar open simulation |
| v1 | breakout_8 + volume_26 | 9726.25 | -273.75 | buy /  / breakout_8 + volume_26: prior completed bar target 50%; next bar open simulation |
| v1 | reversion_12 AND volume_26 | 9861.02 | -138.98 | sell /  / reversion_12 AND volume_26: prior completed bar target 0%; next bar open simulation |
| v1 | reversion_12 + volume_26 | 9727.34 | -272.66 | buy /  / reversion_12 + volume_26: prior completed bar target 50%; next bar open simulation |
| v1 | ema_12_26 | 9793.97 | -206.03 | buy /  / EMA12 > EMA26; 조건 충족; EMA12=767.528, EMA26=767.458 |
| v1 | macd_12_26_9 | 9790.92 | -209.08 | sell /  / MACD > 신호선 그리고 MACD > 0; 조건 미충족; MACD=0.543331, signal9=0.570253 |
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
| v1 | chaikin_3_10 | 9799.08 | -200.92 | buy /  / ADL의 EMA3 - EMA10 > 0 그리고 종가 > EMA26; 조건 충족; Chaikin3_10=3.22035e+06, ADL=9.69276e+06, close=769.57, EMA26=768.805 |
| v1 | roc_10_momentum | 9953.42 | -46.58 | sell /  / 10봉 ROC > 1% 그리고 종가 > EMA26; 조건 미충족; ROC10_percent=0.806376, close=769.45, EMA26=767.181 |
| v1 | trix_15_trend | 9721.85 | -278.15 | buy /  / 15봉 삼중 EMA의 1봉 변화율 TRIX > 0 그리고 종가 > EMA26; 조건 충족; TRIX15_percent=0.0103976, close=768.76, EMA26=768.744 |
| v1 | keltner_20_breakout | 9924.71 | -75.29 | sell /  / 종가 > EMA20 + 2 x Wilder ATR14; 조건 미충족; close=768.93, upper_Keltner=771.837, EMA20=768.595, ATR14=1.6209 |
| v1 | opening_range_30m | 9762.91 | -237.09 | buy /  / 뉴욕 09:30·09:45 두 완료 봉 최고가를 10:00 이후 종가가 돌파; 조건 충족; close=769.1, opening_high=768 |
| v2 | cash | 10000.00 | 0.00 | 대기 /  / 새 신호 대기 |
| v2 | buy_hold | 9861.66 | -138.34 | buy / partial / 직전 완료 봉 목표 비중 100%; 다음 봉 시가 가정 |
| v2 | trend_8_26 | 9710.05 | -289.95 | buy / partial / 직전 완료 봉 목표 비중 100%; 다음 봉 시가 가정 |
| v2 | momentum_26 | 9612.89 | -387.11 | buy / partial / 직전 완료 봉 목표 비중 100%; 다음 봉 시가 가정 |
| v2 | breakout_8 | 9349.72 | -650.28 | sell / filled / 직전 완료 봉 목표 비중 0%; 다음 봉 시가 가정 |
| v2 | reversion_12 | 9327.83 | -672.17 | sell / filled / 직전 완료 봉 목표 비중 0%; 다음 봉 시가 가정 |
| v2 | volume_26 | 9110.20 | -889.80 | buy / partial / 직전 완료 봉 목표 비중 100%; 다음 봉 시가 가정 |
| v2 | trend_8_26 AND momentum_26 | 9620.21 | -379.79 | buy / partial / 직전 완료 봉 목표 비중 100%; 다음 봉 시가 가정 |
| v2 | trend_8_26 + momentum_26 | 9661.35 | -338.65 | buy / partial / 직전 완료 봉 목표 비중 100%; 다음 봉 시가 가정 |
| v2 | trend_8_26 AND breakout_8 | 9681.27 | -318.73 | sell / filled / 직전 완료 봉 목표 비중 0%; 다음 봉 시가 가정 |
| v2 | trend_8_26 + breakout_8 | 9568.05 | -431.95 | sell / filled / 직전 완료 봉 목표 비중 50%; 다음 봉 시가 가정 |
| v2 | trend_8_26 AND reversion_12 | 9761.16 | -238.84 | sell / filled / 직전 완료 봉 목표 비중 0%; 다음 봉 시가 가정 |
| v2 | trend_8_26 + reversion_12 | 9516.55 | -483.45 | sell / filled / 직전 완료 봉 목표 비중 50%; 다음 봉 시가 가정 |
| v2 | trend_8_26 AND volume_26 | 9547.09 | -452.91 | buy / partial / 직전 완료 봉 목표 비중 100%; 다음 봉 시가 가정 |
| v2 | trend_8_26 + volume_26 | 9424.85 | -575.15 | buy / partial / 직전 완료 봉 목표 비중 100%; 다음 봉 시가 가정 |
| v2 | momentum_26 AND breakout_8 | 9611.27 | -388.73 | sell / filled / 직전 완료 봉 목표 비중 0%; 다음 봉 시가 가정 |
| v2 | momentum_26 + breakout_8 | 9480.30 | -519.70 | sell / filled / 직전 완료 봉 목표 비중 50%; 다음 봉 시가 가정 |
| v2 | momentum_26 AND reversion_12 | 9823.55 | -176.45 | sell / filled / 직전 완료 봉 목표 비중 0%; 다음 봉 시가 가정 |
| v2 | momentum_26 + reversion_12 | 9528.70 | -471.30 | sell / filled / 직전 완료 봉 목표 비중 50%; 다음 봉 시가 가정 |
| v2 | momentum_26 AND volume_26 | 9629.65 | -370.35 | buy / partial / 직전 완료 봉 목표 비중 100%; 다음 봉 시가 가정 |
| v2 | momentum_26 + volume_26 | 9417.01 | -582.99 | buy / partial / 직전 완료 봉 목표 비중 100%; 다음 봉 시가 가정 |
| v2 | breakout_8 AND reversion_12 | 10000.00 | 0.00 | 대기 /  / 새 신호 대기 |
| v2 | breakout_8 + reversion_12 | 9377.48 | -622.52 | sell / filled / 직전 완료 봉 목표 비중 0%; 다음 봉 시가 가정 |
| v2 | breakout_8 AND volume_26 | 9808.87 | -191.13 | sell / filled / 직전 완료 봉 목표 비중 0%; 다음 봉 시가 가정 |
| v2 | breakout_8 + volume_26 | 9287.03 | -712.97 | buy / filled / 직전 완료 봉 목표 비중 50%; 다음 봉 시가 가정 |
| v2 | reversion_12 AND volume_26 | 9602.16 | -397.84 | sell / filled / 직전 완료 봉 목표 비중 0%; 다음 봉 시가 가정 |
| v2 | reversion_12 + volume_26 | 9295.77 | -704.23 | buy / filled / 직전 완료 봉 목표 비중 50%; 다음 봉 시가 가정 |
| v2 | ema_12_26 | 9789.07 | -210.93 | buy / partial / EMA12 > EMA26; 조건 충족; EMA12=767.528, EMA26=767.458; 직전 완료 봉 목표를 다음 봉 시가에 모의 적용 |
| v2 | macd_12_26_9 | 9785.04 | -214.96 | sell / filled / MACD > 신호선 그리고 MACD > 0; 조건 미충족; MACD=0.543331, signal9=0.570253; 직전 완료 봉 목표를 다음 봉 시가에 모의 적용 |
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
| v2 | chaikin_3_10 | 9790.26 | -209.74 | buy / partial / ADL의 EMA3 - EMA10 > 0 그리고 종가 > EMA26; 조건 충족; Chaikin3_10=3.22035e+06, ADL=9.69276e+06, close=769.57, EMA26=768.805; 직전 완료 봉 목표를 다음 봉 시가에 모의 적용 |
| v2 | roc_10_momentum | 9951.43 | -48.57 | sell / filled / 10봉 ROC > 1% 그리고 종가 > EMA26; 조건 미충족; ROC10_percent=0.806376, close=769.45, EMA26=767.181; 직전 완료 봉 목표를 다음 봉 시가에 모의 적용 |
| v2 | trix_15_trend | 9711.16 | -288.84 | buy / partial / 15봉 삼중 EMA의 1봉 변화율 TRIX > 0 그리고 종가 > EMA26; 조건 충족; TRIX15_percent=0.0103976, close=768.76, EMA26=768.744; 직전 완료 봉 목표를 다음 봉 시가에 모의 적용 |
| v2 | keltner_20_breakout | 9922.73 | -77.27 | sell / filled / 종가 > EMA20 + 2 x Wilder ATR14; 조건 미충족; close=768.93, upper_Keltner=771.837, EMA20=768.595, ATR14=1.6209; 직전 완료 봉 목표를 다음 봉 시가에 모의 적용 |
| v2 | opening_range_30m | 9754.13 | -245.87 | buy / partial / 뉴욕 09:30·09:45 두 완료 봉 최고가를 10:00 이후 종가가 돌파; 조건 충족; close=769.1, opening_high=768; 직전 완료 봉 목표를 다음 봉 시가에 모의 적용 |

### 같은 기간의 비용·노출 비교 (사후 연구)

| 전략 | 비용 전 | 비용 후 | 100% 보유 | 같은 평균 노출 보유 | 평균 노출 |
|---|---:|---:|---:|---:|---:|
| cash | 0.00% | 0.00% | -0.01% | -0.00% | 0.00% |
| buy_hold | 0.41% | -0.01% | -0.01% | -0.01% | 100.00% |
| trend_8_26 | 0.98% | -2.76% | -0.01% | -0.00% | 54.59% |
| momentum_26 | -0.63% | -5.12% | -0.01% | -0.00% | 53.81% |
| breakout_8 | -0.34% | -16.46% | -0.01% | -0.00% | 22.57% |
| reversion_12 | -1.41% | -11.61% | -0.01% | -0.00% | 27.30% |
| volume_26 | -1.25% | -11.10% | -0.01% | -0.00% | 9.71% |
| trend_8_26 AND momentum_26 | 0.35% | -4.18% | -0.01% | -0.00% | 46.98% |
| trend_8_26 + momentum_26 | 0.17% | -3.95% | -0.01% | -0.00% | 54.20% |
| trend_8_26 AND breakout_8 | -0.15% | -11.60% | -0.01% | -0.00% | 13.91% |
| trend_8_26 + breakout_8 | 0.32% | -9.49% | -0.01% | -0.00% | 38.59% |
| trend_8_26 AND reversion_12 | -0.13% | -4.24% | -0.01% | -0.00% | 6.82% |
| trend_8_26 + reversion_12 | -0.22% | -7.11% | -0.01% | -0.00% | 40.95% |
| trend_8_26 AND volume_26 | -1.00% | -6.65% | -0.01% | -0.00% | 5.77% |
| trend_8_26 + volume_26 | -0.14% | -7.03% | -0.01% | -0.00% | 32.16% |
| momentum_26 AND breakout_8 | 0.28% | -11.60% | -0.01% | -0.00% | 15.22% |
| momentum_26 + breakout_8 | -0.48% | -10.97% | -0.01% | -0.00% | 38.20% |
| momentum_26 AND reversion_12 | -0.93% | -5.80% | -0.01% | -0.00% | 7.35% |
| momentum_26 + reversion_12 | -1.02% | -7.85% | -0.01% | -0.00% | 40.56% |
| momentum_26 AND volume_26 | -0.72% | -5.20% | -0.01% | -0.00% | 3.94% |
| momentum_26 + volume_26 | -0.94% | -7.00% | -0.01% | -0.00% | 31.76% |
| breakout_8 AND reversion_12 | 0.00% | 0.00% | -0.01% | -0.00% | 0.00% |
| breakout_8 + reversion_12 | -0.87% | -13.72% | -0.01% | -0.00% | 24.94% |
| breakout_8 AND volume_26 | -0.33% | -2.40% | -0.01% | -0.00% | 1.84% |
| breakout_8 + volume_26 | -0.80% | -12.73% | -0.01% | -0.00% | 16.15% |
| reversion_12 AND volume_26 | -0.87% | -5.34% | -0.01% | -0.00% | 3.94% |
| reversion_12 + volume_26 | -1.33% | -11.17% | -0.01% | -0.00% | 18.51% |
| ema_12_26 | -0.67% | -4.35% | -0.01% | -0.00% | 56.17% |
| macd_12_26_9 | -0.01% | -4.92% | -0.01% | -0.00% | 33.86% |
| rsi_14_recovery | -0.53% | -4.22% | -0.01% | -0.00% | 2.36% |
| bollinger_20_reentry | -1.07% | -6.72% | -0.01% | -0.00% | 3.67% |
| donchian_20 | 0.09% | -7.58% | -0.01% | -0.00% | 7.09% |
| atr_14_breakout | 0.54% | -5.20% | -0.01% | -0.00% | 4.20% |
| session_vwap | 1.87% | -8.29% | -0.01% | -0.00% | 47.51% |
| obv_20 | 0.35% | -6.95% | -0.01% | -0.00% | 37.80% |
| stochastic_14_3_recovery | -0.40% | -14.02% | -0.01% | -0.00% | 9.19% |
| mfi_14_recovery | -0.01% | -3.31% | -0.01% | -0.00% | 2.10% |
| adx_14_trend | 0.32% | -3.40% | -0.01% | -0.00% | 28.08% |
| aroon_25_trend | 0.82% | -2.10% | -0.01% | -0.00% | 25.72% |
| cci_20_momentum | -0.10% | -8.53% | -0.01% | -0.00% | 23.10% |
| williams_14_recovery | -0.58% | -10.49% | -0.01% | -0.00% | 6.56% |
| cmf_20_accumulation | 1.87% | -1.91% | -0.01% | -0.00% | 43.04% |
| chaikin_3_10 | 1.88% | -5.14% | -0.01% | -0.00% | 39.90% |
| roc_10_momentum | -0.13% | -0.97% | -0.01% | -0.00% | 1.05% |
| trix_15_trend | -0.29% | -4.79% | -0.01% | -0.00% | 42.26% |
| keltner_20_breakout | -0.26% | -4.36% | -0.01% | -0.00% | 11.55% |
| opening_range_30m | 0.11% | -6.40% | -0.01% | -0.00% | 35.96% |

동일 구간·초기 자금, 종료 시 청산 비용 포함. 노출 맞춤은 사후 설명용이며 v2 실제 계좌 성과가 아닙니다.
[낙폭 분해·비용 영향·전체 구간](SPY/comparison.json)

[v1 전체 기록](SPY/accounts.json) · [v2 전체 기록](SPY/accounts-v2.json)

## QQQ 계좌

| 모델 | 전략 | 평가액 USD | 손익 USD | 최근 매매·이유 |
|---|---|---:|---:|---|
| v1 | cash | 10000.00 | 0.00 | 대기 /  / 새 신호 대기 |
| v1 | buy_hold | 9892.66 | -107.34 | buy /  / buy_hold: prior completed bar target 100%; next bar open simulation |
| v1 | trend_8_26 | 9828.61 | -171.39 | sell /  / trend_8_26: prior completed bar target 0%; next bar open simulation |
| v1 | momentum_26 | 9617.56 | -382.44 | sell /  / momentum_26: prior completed bar target 0%; next bar open simulation |
| v1 | breakout_8 | 9742.42 | -257.58 | sell /  / breakout_8: prior completed bar target 0%; next bar open simulation |
| v1 | reversion_12 | 9789.83 | -210.17 | sell /  / reversion_12: prior completed bar target 0%; next bar open simulation |
| v1 | volume_26 | 9624.14 | -375.86 | sell /  / volume_26: prior completed bar target 0%; next bar open simulation |
| v1 | trend_8_26 AND momentum_26 | 9890.12 | -109.88 | sell /  / trend_8_26 AND momentum_26: prior completed bar target 0%; next bar open simulation |
| v1 | trend_8_26 + momentum_26 | 9742.06 | -257.94 | sell /  / trend_8_26 + momentum_26: prior completed bar target 0%; next bar open simulation |
| v1 | trend_8_26 AND breakout_8 | 9989.91 | -10.09 | sell /  / trend_8_26 AND breakout_8: prior completed bar target 0%; next bar open simulation |
| v1 | trend_8_26 + breakout_8 | 9824.62 | -175.38 | sell /  / trend_8_26 + breakout_8: prior completed bar target 0%; next bar open simulation |
| v1 | trend_8_26 AND reversion_12 | 9902.56 | -97.44 | sell /  / trend_8_26 AND reversion_12: prior completed bar target 0%; next bar open simulation |
| v1 | trend_8_26 + reversion_12 | 9828.96 | -171.04 | sell /  / trend_8_26 + reversion_12: prior completed bar target 0%; next bar open simulation |
| v1 | trend_8_26 AND volume_26 | 9864.33 | -135.67 | sell /  / trend_8_26 AND volume_26: prior completed bar target 0%; next bar open simulation |
| v1 | trend_8_26 + volume_26 | 9725.78 | -274.22 | sell /  / trend_8_26 + volume_26: prior completed bar target 0%; next bar open simulation |
| v1 | momentum_26 AND breakout_8 | 9773.97 | -226.03 | sell /  / momentum_26 AND breakout_8: prior completed bar target 0%; next bar open simulation |
| v1 | momentum_26 + breakout_8 | 9679.84 | -320.16 | sell /  / momentum_26 + breakout_8: prior completed bar target 0%; next bar open simulation |
| v1 | momentum_26 AND reversion_12 | 9800.84 | -199.16 | sell /  / momentum_26 AND reversion_12: prior completed bar target 0%; next bar open simulation |
| v1 | momentum_26 + reversion_12 | 9703.55 | -296.45 | sell /  / momentum_26 + reversion_12: prior completed bar target 0%; next bar open simulation |
| v1 | momentum_26 AND volume_26 | 9836.75 | -163.25 | sell /  / momentum_26 AND volume_26: prior completed bar target 0%; next bar open simulation |
| v1 | momentum_26 + volume_26 | 9640.09 | -359.91 | sell /  / momentum_26 + volume_26: prior completed bar target 0%; next bar open simulation |
| v1 | breakout_8 AND reversion_12 | 10000.00 | 0.00 | 대기 /  / 새 신호 대기 |
| v1 | breakout_8 + reversion_12 | 9785.76 | -214.24 | sell /  / breakout_8 + reversion_12: prior completed bar target 0%; next bar open simulation |
| v1 | breakout_8 AND volume_26 | 9947.15 | -52.85 | sell /  / breakout_8 AND volume_26: prior completed bar target 0%; next bar open simulation |
| v1 | breakout_8 + volume_26 | 9702.47 | -297.53 | sell /  / breakout_8 + volume_26: prior completed bar target 0%; next bar open simulation |
| v1 | reversion_12 AND volume_26 | 9907.31 | -92.69 | sell /  / reversion_12 AND volume_26: prior completed bar target 0%; next bar open simulation |
| v1 | reversion_12 + volume_26 | 9745.55 | -254.45 | sell /  / reversion_12 + volume_26: prior completed bar target 0%; next bar open simulation |
| v1 | ema_12_26 | 9663.12 | -336.88 | sell /  / EMA12 > EMA26; 조건 미충족; EMA12=719.14, EMA26=719.146 |
| v1 | macd_12_26_9 | 9793.26 | -206.74 | sell /  / MACD > 신호선 그리고 MACD > 0; 조건 미충족; MACD=0.112193, signal9=0.128925 |
| v1 | rsi_14_recovery | 9809.40 | -190.60 | sell /  / 직전 RSI14 < 30, 현재 RSI14 >= 30 (한 봉 목표); 조건 미충족; RSI14=50.2063, previous_RSI14=44.1729 |
| v1 | bollinger_20_reentry | 9878.60 | -121.40 | sell /  / 직전 종가 < 직전 하단밴드, 현재 하단밴드 <= 종가 <= SMA20 (한 봉 목표); 조건 미충족; close=718.66, lower20=714.386, SMA20=719.409, previous_lower20=714.271 |
| v1 | donchian_20 | 9951.11 | -48.89 | sell /  / 종가 > 현재 봉을 제외한 직전 20봉 최고가; 조건 미충족; close=724.13, prior_high20=724.151 |
| v1 | atr_14_breakout | 9945.80 | -54.20 | sell /  / 종가 > 직전 종가 + 직전 ATR14 그리고 종가 > EMA26; 조건 미충족; close=721.52, threshold=724.646, prior_ATR14=2.53578, EMA26=719.016 |
| v1 | session_vwap | 9757.98 | -242.02 | sell /  / 종가 > 뉴욕 거래일별 누적 전형가격 VWAP; 조건 미충족; close=719.05, session_VWAP=719.729, session_volume=3.45027e+08 |
| v1 | obv_20 | 9745.11 | -254.89 | buy /  / OBV > OBV의 SMA20 그리고 종가 > EMA26; 조건 충족; OBV=2.85061e+08, OBV_SMA20=1.79429e+08, close=719.364, EMA26=719.11 |
| v1 | stochastic_14_3_recovery | 9618.80 | -381.20 | sell /  / 직전 %K14 < 20에서 %K14가 %D3 상향 돌파 (한 봉 목표); 조건 미충족; K14=76.4321, D3=43.007, previous_K14=52.497, previous_D3=21.4564 |
| v1 | mfi_14_recovery | 9813.56 | -186.44 | sell /  / 직전 MFI14 < 20, 현재 MFI14 >= 20 (한 봉 목표); 조건 미충족; MFI14=30.3876, previous_MFI14=31.1747 |
| v1 | adx_14_trend | 9926.53 | -73.47 | sell /  / Wilder ADX14 >= 25 그리고 +DI14 > -DI14; 조건 미충족; ADX14=23.9831, plus_DI14=26.5781, minus_DI14=24.6326 |
| v1 | aroon_25_trend | 9875.01 | -124.99 | sell /  / Aroon25 Up > 70 그리고 Down < 30 (동률이면 최신 극값); 조건 미충족; Aroon_up=68, Aroon_down=20 |
| v1 | cci_20_momentum | 9880.19 | -119.81 | sell /  / CCI20 > 100 (전형가격·평균절대편차); 조건 미충족; CCI20=19.2232 |
| v1 | williams_14_recovery | 9710.09 | -289.91 | sell /  / 직전 Williams %R14 < -80, 현재 >= -80 (한 봉 목표); 조건 미충족; Williams_R14=-23.5679, previous_R14=-47.503 |
| v1 | cmf_20_accumulation | 9616.17 | -383.83 | buy /  / Chaikin Money Flow20 > 0.1; 조건 충족; CMF20=0.152804, volume20=3.24878e+08 |
| v1 | chaikin_3_10 | 9749.71 | -250.29 | buy /  / ADL의 EMA3 - EMA10 > 0 그리고 종가 > EMA26; 조건 충족; Chaikin3_10=4.55281e+06, ADL=2.71567e+08, close=719.364, EMA26=719.11 |
| v1 | roc_10_momentum | 9990.50 | -9.50 | sell /  / 10봉 ROC > 1% 그리고 종가 > EMA26; 조건 미충족; ROC10_percent=0.483561, close=722.477, EMA26=718.78 |
| v1 | trix_15_trend | 9693.96 | -306.04 | buy /  / 15봉 삼중 EMA의 1봉 변화율 TRIX > 0 그리고 종가 > EMA26; 조건 충족; TRIX15_percent=0.00127025, close=719.364, EMA26=719.11 |
| v1 | keltner_20_breakout | 9904.16 | -95.84 | sell /  / 종가 > EMA20 + 2 x Wilder ATR14; 조건 미충족; close=723.31, upper_Keltner=723.407, EMA20=718.722, ATR14=2.34265 |
| v1 | opening_range_30m | 9765.09 | -234.91 | buy /  / 뉴욕 09:30·09:45 두 완료 봉 최고가를 10:00 이후 종가가 돌파; 조건 충족; close=718.66, opening_high=716.18 |
| v2 | cash | 10000.00 | 0.00 | 대기 /  / 새 신호 대기 |
| v2 | buy_hold | 9572.89 | -427.11 | buy / partial / 직전 완료 봉 목표 비중 100%; 다음 봉 시가 가정 |
| v2 | trend_8_26 | 9629.88 | -370.12 | sell / filled / 직전 완료 봉 목표 비중 0%; 다음 봉 시가 가정 |
| v2 | momentum_26 | 9511.63 | -488.37 | sell / filled / 직전 완료 봉 목표 비중 0%; 다음 봉 시가 가정 |
| v2 | breakout_8 | 9411.37 | -588.63 | sell / filled / 직전 완료 봉 목표 비중 0%; 다음 봉 시가 가정 |
| v2 | reversion_12 | 9302.80 | -697.20 | sell / filled / 직전 완료 봉 목표 비중 0%; 다음 봉 시가 가정 |
| v2 | volume_26 | 9565.80 | -434.20 | 중단: 손실 한도 / sell / filled / 직전 완료 봉 목표 비중 0%; 다음 봉 시가 가정 |
| v2 | trend_8_26 AND momentum_26 | 9785.10 | -214.90 | sell / filled / 직전 완료 봉 목표 비중 0%; 다음 봉 시가 가정 |
| v2 | trend_8_26 + momentum_26 | 9590.81 | -409.19 | sell / filled / 직전 완료 봉 목표 비중 0%; 다음 봉 시가 가정 |
| v2 | trend_8_26 AND breakout_8 | 9883.87 | -116.13 | sell / filled / 직전 완료 봉 목표 비중 0%; 다음 봉 시가 가정 |
| v2 | trend_8_26 + breakout_8 | 9560.00 | -440.00 | sell / filled / 직전 완료 봉 목표 비중 0%; 다음 봉 시가 가정 |
| v2 | trend_8_26 AND reversion_12 | 9761.15 | -238.85 | sell / filled / 직전 완료 봉 목표 비중 0%; 다음 봉 시가 가정 |
| v2 | trend_8_26 + reversion_12 | 9484.63 | -515.37 | sell / filled / 직전 완료 봉 목표 비중 0%; 다음 봉 시가 가정 |
| v2 | trend_8_26 AND volume_26 | 9698.84 | -301.16 | sell / filled / 직전 완료 봉 목표 비중 0%; 다음 봉 시가 가정 |
| v2 | trend_8_26 + volume_26 | 9329.51 | -670.49 | sell / filled / 직전 완료 봉 목표 비중 0%; 다음 봉 시가 가정 |
| v2 | momentum_26 AND breakout_8 | 9727.76 | -272.24 | sell / filled / 직전 완료 봉 목표 비중 0%; 다음 봉 시가 가정 |
| v2 | momentum_26 + breakout_8 | 9461.38 | -538.62 | sell / filled / 직전 완료 봉 목표 비중 0%; 다음 봉 시가 가정 |
| v2 | momentum_26 AND reversion_12 | 9794.96 | -205.04 | sell / filled / 직전 완료 봉 목표 비중 0%; 다음 봉 시가 가정 |
| v2 | momentum_26 + reversion_12 | 9426.31 | -573.69 | sell / filled / 직전 완료 봉 목표 비중 0%; 다음 봉 시가 가정 |
| v2 | momentum_26 AND volume_26 | 9768.76 | -231.24 | sell / filled / 직전 완료 봉 목표 비중 0%; 다음 봉 시가 가정 |
| v2 | momentum_26 + volume_26 | 9291.55 | -708.45 | sell / filled / 직전 완료 봉 목표 비중 0%; 다음 봉 시가 가정 |
| v2 | breakout_8 AND reversion_12 | 10000.00 | 0.00 | 대기 /  / 새 신호 대기 |
| v2 | breakout_8 + reversion_12 | 9435.65 | -564.35 | sell / filled / 직전 완료 봉 목표 비중 0%; 다음 봉 시가 가정 |
| v2 | breakout_8 AND volume_26 | 9891.45 | -108.55 | sell / filled / 직전 완료 봉 목표 비중 0%; 다음 봉 시가 가정 |
| v2 | breakout_8 + volume_26 | 9281.43 | -718.57 | sell / filled / 직전 완료 봉 목표 비중 0%; 다음 봉 시가 가정 |
| v2 | reversion_12 AND volume_26 | 9547.64 | -452.36 | 중단: 손실 한도 / sell / filled / 직전 완료 봉 목표 비중 0%; 다음 봉 시가 가정 |
| v2 | reversion_12 + volume_26 | 9227.85 | -772.15 | sell / filled / 직전 완료 봉 목표 비중 0%; 다음 봉 시가 가정 |
| v2 | ema_12_26 | 9657.32 | -342.68 | sell / filled / EMA12 > EMA26; 조건 미충족; EMA12=719.14, EMA26=719.146; 직전 완료 봉 목표를 다음 봉 시가에 모의 적용 |
| v2 | macd_12_26_9 | 9787.38 | -212.62 | sell / filled / MACD > 신호선 그리고 MACD > 0; 조건 미충족; MACD=0.112193, signal9=0.128925; 직전 완료 봉 목표를 다음 봉 시가에 모의 적용 |
| v2 | rsi_14_recovery | 9801.56 | -198.44 | sell / filled / 직전 RSI14 < 30, 현재 RSI14 >= 30 (한 봉 목표); 조건 미충족; RSI14=50.2063, previous_RSI14=44.1729; 직전 완료 봉 목표를 다음 봉 시가에 모의 적용 |
| v2 | bollinger_20_reentry | 9872.68 | -127.32 | sell / filled / 직전 종가 < 직전 하단밴드, 현재 하단밴드 <= 종가 <= SMA20 (한 봉 목표); 조건 미충족; close=718.66, lower20=714.386, SMA20=719.409, previous_lower20=714.271; 직전 완료 봉 목표를 다음 봉 시가에 모의 적용 |
| v2 | donchian_20 | 9947.13 | -52.87 | sell / filled / 종가 > 현재 봉을 제외한 직전 20봉 최고가; 조건 미충족; close=724.13, prior_high20=724.151; 직전 완료 봉 목표를 다음 봉 시가에 모의 적용 |
| v2 | atr_14_breakout | 9941.83 | -58.17 | sell / filled / 종가 > 직전 종가 + 직전 ATR14 그리고 종가 > EMA26; 조건 미충족; close=721.52, threshold=724.646, prior_ATR14=2.53578, EMA26=719.016; 직전 완료 봉 목표를 다음 봉 시가에 모의 적용 |
| v2 | session_vwap | 9746.27 | -253.73 | sell / filled / 종가 > 뉴욕 거래일별 누적 전형가격 VWAP; 조건 미충족; close=719.05, session_VWAP=719.729, session_volume=3.45027e+08; 직전 완료 봉 목표를 다음 봉 시가에 모의 적용 |
| v2 | obv_20 | 9736.34 | -263.66 | buy / partial / OBV > OBV의 SMA20 그리고 종가 > EMA26; 조건 충족; OBV=2.85061e+08, OBV_SMA20=1.79429e+08, close=719.364, EMA26=719.11; 직전 완료 봉 목표를 다음 봉 시가에 모의 적용 |
| v2 | stochastic_14_3_recovery | 9694.13 | -305.87 | 중단: 손실 한도 / sell / filled / 직전 %K14 < 20에서 %K14가 %D3 상향 돌파 (한 봉 목표); 조건 미충족; K14=10.576, D3=8.00581, previous_K14=7.39787, previous_D3=7.27486; 직전 완료 봉 목표를 다음 봉 시가에 모의 적용 |
| v2 | mfi_14_recovery | 9809.63 | -190.37 | sell / filled / 직전 MFI14 < 20, 현재 MFI14 >= 20 (한 봉 목표); 조건 미충족; MFI14=30.3876, previous_MFI14=31.1747; 직전 완료 봉 목표를 다음 봉 시가에 모의 적용 |
| v2 | adx_14_trend | 9922.56 | -77.44 | sell / filled / Wilder ADX14 >= 25 그리고 +DI14 > -DI14; 조건 미충족; ADX14=23.9831, plus_DI14=26.5781, minus_DI14=24.6326; 직전 완료 봉 목표를 다음 봉 시가에 모의 적용 |
| v2 | aroon_25_trend | 9871.06 | -128.94 | sell / filled / Aroon25 Up > 70 그리고 Down < 30 (동률이면 최신 극값); 조건 미충족; Aroon_up=68, Aroon_down=20; 직전 완료 봉 목표를 다음 봉 시가에 모의 적용 |
| v2 | cci_20_momentum | 9874.26 | -125.74 | sell / filled / CCI20 > 100 (전형가격·평균절대편차); 조건 미충족; CCI20=19.2232; 직전 완료 봉 목표를 다음 봉 시가에 모의 적용 |
| v2 | williams_14_recovery | 9696.51 | -303.49 | sell / filled / 직전 Williams %R14 < -80, 현재 >= -80 (한 봉 목표); 조건 미충족; Williams_R14=-23.5679, previous_R14=-47.503; 직전 완료 봉 목표를 다음 봉 시가에 모의 적용 |
| v2 | cmf_20_accumulation | 9603.68 | -396.32 | buy / partial / Chaikin Money Flow20 > 0.1; 조건 충족; CMF20=0.152804, volume20=3.24878e+08; 직전 완료 봉 목표를 다음 봉 시가에 모의 적용 |
| v2 | chaikin_3_10 | 9740.94 | -259.06 | buy / partial / ADL의 EMA3 - EMA10 > 0 그리고 종가 > EMA26; 조건 충족; Chaikin3_10=4.55281e+06, ADL=2.71567e+08, close=719.364, EMA26=719.11; 직전 완료 봉 목표를 다음 봉 시가에 모의 적용 |
| v2 | roc_10_momentum | 9988.50 | -11.50 | sell / filled / 10봉 ROC > 1% 그리고 종가 > EMA26; 조건 미충족; ROC10_percent=0.483561, close=722.477, EMA26=718.78; 직전 완료 봉 목표를 다음 봉 시가에 모의 적용 |
| v2 | trix_15_trend | 9685.24 | -314.76 | buy / partial / 15봉 삼중 EMA의 1봉 변화율 TRIX > 0 그리고 종가 > EMA26; 조건 충족; TRIX15_percent=0.00127025, close=719.364, EMA26=719.11; 직전 완료 봉 목표를 다음 봉 시가에 모의 적용 |
| v2 | keltner_20_breakout | 9900.20 | -99.80 | sell / filled / 종가 > EMA20 + 2 x Wilder ATR14; 조건 미충족; close=723.31, upper_Keltner=723.407, EMA20=718.722, ATR14=2.34265; 직전 완료 봉 목표를 다음 봉 시가에 모의 적용 |
| v2 | opening_range_30m | 9758.25 | -241.75 | buy / partial / 뉴욕 09:30·09:45 두 완료 봉 최고가를 10:00 이후 종가가 돌파; 조건 충족; close=718.66, opening_high=716.18; 직전 완료 봉 목표를 다음 봉 시가에 모의 적용 |

### 같은 기간의 비용·노출 비교 (사후 연구)

| 전략 | 비용 전 | 비용 후 | 100% 보유 | 같은 평균 노출 보유 | 평균 노출 |
|---|---:|---:|---:|---:|---:|
| cash | 0.00% | 0.00% | -3.25% | -0.00% | 0.00% |
| buy_hold | -2.85% | -3.25% | -3.25% | -3.25% | 100.00% |
| trend_8_26 | 0.24% | -3.48% | -3.25% | -1.47% | 45.14% |
| momentum_26 | -2.86% | -8.02% | -3.25% | -1.31% | 40.16% |
| breakout_8 | -1.66% | -16.87% | -3.25% | -0.60% | 18.37% |
| reversion_12 | -0.53% | -12.31% | -3.25% | -0.97% | 29.66% |
| volume_26 | -1.17% | -14.68% | -3.25% | -0.52% | 16.01% |
| trend_8_26 AND momentum_26 | 0.01% | -3.70% | -3.25% | -1.11% | 34.12% |
| trend_8_26 + momentum_26 | -1.31% | -5.38% | -3.25% | -1.39% | 42.65% |
| trend_8_26 AND breakout_8 | -0.01% | -8.84% | -3.25% | -0.37% | 11.29% |
| trend_8_26 + breakout_8 | -0.71% | -9.86% | -3.25% | -1.03% | 31.76% |
| trend_8_26 AND reversion_12 | -0.22% | -4.73% | -3.25% | -0.21% | 6.56% |
| trend_8_26 + reversion_12 | -0.14% | -7.42% | -3.25% | -1.22% | 37.41% |
| trend_8_26 AND volume_26 | 0.45% | -4.49% | -3.25% | -0.16% | 4.99% |
| trend_8_26 + volume_26 | -0.46% | -9.07% | -3.25% | -1.00% | 30.58% |
| momentum_26 AND breakout_8 | -0.75% | -9.89% | -3.25% | -0.37% | 11.29% |
| momentum_26 + breakout_8 | -2.25% | -12.37% | -3.25% | -0.95% | 29.27% |
| momentum_26 AND reversion_12 | -1.16% | -6.41% | -3.25% | -0.22% | 6.82% |
| momentum_26 + reversion_12 | -1.69% | -9.82% | -3.25% | -1.14% | 34.91% |
| momentum_26 AND volume_26 | -0.28% | -4.38% | -3.25% | -0.12% | 3.67% |
| momentum_26 + volume_26 | -2.01% | -11.04% | -3.25% | -0.91% | 28.09% |
| breakout_8 AND reversion_12 | 0.00% | 0.00% | -3.25% | -0.00% | 0.00% |
| breakout_8 + reversion_12 | -1.09% | -13.73% | -3.25% | -0.78% | 24.02% |
| breakout_8 AND volume_26 | 0.32% | -2.18% | -3.25% | -0.06% | 1.84% |
| breakout_8 + volume_26 | -1.41% | -14.36% | -3.25% | -0.56% | 17.20% |
| reversion_12 AND volume_26 | -1.31% | -8.11% | -3.25% | -0.27% | 8.40% |
| reversion_12 + volume_26 | -0.84% | -12.96% | -3.25% | -0.74% | 22.84% |
| ema_12_26 | -1.28% | -3.73% | -3.25% | -1.37% | 41.99% |
| macd_12_26_9 | 0.60% | -3.53% | -3.25% | -0.79% | 24.15% |
| rsi_14_recovery | -0.47% | -5.76% | -3.25% | -0.11% | 3.41% |
| bollinger_20_reentry | -0.08% | -6.18% | -3.25% | -0.13% | 3.94% |
| donchian_20 | 0.59% | -4.75% | -3.25% | -0.19% | 5.77% |
| atr_14_breakout | 0.47% | -3.67% | -3.25% | -0.10% | 3.15% |
| session_vwap | -0.08% | -11.54% | -3.25% | -1.55% | 47.51% |
| obv_20 | -1.14% | -9.86% | -3.25% | -0.94% | 28.87% |
| stochastic_14_3_recovery | -0.31% | -11.75% | -3.25% | -0.25% | 7.61% |
| mfi_14_recovery | -1.23% | -3.69% | -3.25% | -0.05% | 1.57% |
| adx_14_trend | -0.11% | -3.00% | -3.25% | -0.70% | 21.52% |
| aroon_25_trend | 1.27% | -2.07% | -3.25% | -0.59% | 18.11% |
| cci_20_momentum | -0.45% | -5.74% | -3.25% | -0.56% | 17.06% |
| williams_14_recovery | -0.63% | -10.91% | -3.25% | -0.22% | 6.82% |
| cmf_20_accumulation | -1.85% | -9.76% | -3.25% | -1.05% | 32.28% |
| chaikin_3_10 | -2.59% | -10.44% | -3.25% | -1.17% | 35.96% |
| roc_10_momentum | -0.00% | -1.67% | -3.25% | -0.14% | 4.20% |
| trix_15_trend | -0.38% | -3.67% | -3.25% | -1.12% | 34.38% |
| keltner_20_breakout | -0.89% | -5.76% | -3.25% | -0.26% | 8.14% |
| opening_range_30m | -1.03% | -7.85% | -3.25% | -0.94% | 28.87% |

동일 구간·초기 자금, 종료 시 청산 비용 포함. 노출 맞춤은 사후 설명용이며 v2 실제 계좌 성과가 아닙니다.
[낙폭 분해·비용 영향·전체 구간](QQQ/comparison.json)

[v1 전체 기록](QQQ/accounts.json) · [v2 전체 기록](QQQ/accounts-v2.json)

## IWM 계좌

| 모델 | 전략 | 평가액 USD | 손익 USD | 최근 매매·이유 |
|---|---|---:|---:|---|
| v1 | cash | 10000.00 | 0.00 | 대기 /  / 새 신호 대기 |
| v1 | buy_hold | 9991.08 | -8.92 | buy /  / buy_hold: prior completed bar target 100%; next bar open simulation |
| v1 | trend_8_26 | 9796.57 | -203.43 | buy /  / trend_8_26: prior completed bar target 100%; next bar open simulation |
| v1 | momentum_26 | 9967.37 | -32.63 | buy /  / momentum_26: prior completed bar target 100%; next bar open simulation |
| v1 | breakout_8 | 9713.59 | -286.41 | sell /  / breakout_8: prior completed bar target 0%; next bar open simulation |
| v1 | reversion_12 | 9786.62 | -213.38 | sell /  / reversion_12: prior completed bar target 0%; next bar open simulation |
| v1 | volume_26 | 9923.29 | -76.71 | sell /  / volume_26: prior completed bar target 0%; next bar open simulation |
| v1 | trend_8_26 AND momentum_26 | 9812.49 | -187.51 | buy /  / trend_8_26 AND momentum_26: prior completed bar target 100%; next bar open simulation |
| v1 | trend_8_26 + momentum_26 | 9881.66 | -118.34 | buy /  / trend_8_26 + momentum_26: prior completed bar target 100%; next bar open simulation |
| v1 | trend_8_26 AND breakout_8 | 9803.67 | -196.33 | sell /  / trend_8_26 AND breakout_8: prior completed bar target 0%; next bar open simulation |
| v1 | trend_8_26 + breakout_8 | 9755.16 | -244.84 | sell /  / trend_8_26 + breakout_8: prior completed bar target 50%; next bar open simulation |
| v1 | trend_8_26 AND reversion_12 | 9827.31 | -172.69 | sell /  / trend_8_26 AND reversion_12: prior completed bar target 0%; next bar open simulation |
| v1 | trend_8_26 + reversion_12 | 9791.48 | -208.52 | sell /  / trend_8_26 + reversion_12: prior completed bar target 50%; next bar open simulation |
| v1 | trend_8_26 AND volume_26 | 9935.98 | -64.02 | sell /  / trend_8_26 AND volume_26: prior completed bar target 0%; next bar open simulation |
| v1 | trend_8_26 + volume_26 | 9879.36 | -120.64 | sell /  / trend_8_26 + volume_26: prior completed bar target 50%; next bar open simulation |
| v1 | momentum_26 AND breakout_8 | 9853.20 | -146.80 | sell /  / momentum_26 AND breakout_8: prior completed bar target 0%; next bar open simulation |
| v1 | momentum_26 + breakout_8 | 9859.50 | -140.50 | sell /  / momentum_26 + breakout_8: prior completed bar target 50%; next bar open simulation |
| v1 | momentum_26 AND reversion_12 | 9924.34 | -75.66 | sell /  / momentum_26 AND reversion_12: prior completed bar target 0%; next bar open simulation |
| v1 | momentum_26 + reversion_12 | 9896.25 | -103.75 | sell /  / momentum_26 + reversion_12: prior completed bar target 50%; next bar open simulation |
| v1 | momentum_26 AND volume_26 | 10062.05 | 62.05 | sell /  / momentum_26 AND volume_26: prior completed bar target 0%; next bar open simulation |
| v1 | momentum_26 + volume_26 | 9945.19 | -54.81 | sell /  / momentum_26 + volume_26: prior completed bar target 50%; next bar open simulation |
| v1 | breakout_8 AND reversion_12 | 10000.00 | 0.00 | 대기 /  / 새 신호 대기 |
| v1 | breakout_8 + reversion_12 | 9749.93 | -250.07 | sell /  / breakout_8 + reversion_12: prior completed bar target 0%; next bar open simulation |
| v1 | breakout_8 AND volume_26 | 9967.28 | -32.72 | sell /  / breakout_8 AND volume_26: prior completed bar target 0%; next bar open simulation |
| v1 | breakout_8 + volume_26 | 9837.51 | -162.49 | sell /  / breakout_8 + volume_26: prior completed bar target 0%; next bar open simulation |
| v1 | reversion_12 AND volume_26 | 9935.98 | -64.02 | sell /  / reversion_12 AND volume_26: prior completed bar target 0%; next bar open simulation |
| v1 | reversion_12 + volume_26 | 9874.40 | -125.60 | sell /  / reversion_12 + volume_26: prior completed bar target 0%; next bar open simulation |
| v1 | ema_12_26 | 9861.68 | -138.32 | buy /  / EMA12 > EMA26; 조건 충족; EMA12=271.545, EMA26=271.529 |
| v1 | macd_12_26_9 | 9906.42 | -93.58 | sell /  / MACD > 신호선 그리고 MACD > 0; 조건 미충족; MACD=0.978353, signal9=1.01104 |
| v1 | rsi_14_recovery | 9786.95 | -213.05 | sell /  / 직전 RSI14 < 30, 현재 RSI14 >= 30 (한 봉 목표); 조건 미충족; RSI14=46.986, previous_RSI14=37.1649 |
| v1 | bollinger_20_reentry | 9924.03 | -75.97 | sell /  / 직전 종가 < 직전 하단밴드, 현재 하단밴드 <= 종가 <= SMA20 (한 봉 목표); 조건 미충족; close=271.19, lower20=270.018, SMA20=273.224, previous_lower20=270.283 |
| v1 | donchian_20 | 9835.91 | -164.09 | sell /  / 종가 > 현재 봉을 제외한 직전 20봉 최고가; 조건 미충족; close=275.785, prior_high20=276.875 |
| v1 | atr_14_breakout | 9883.94 | -116.06 | sell /  / 종가 > 직전 종가 + 직전 ATR14 그리고 종가 > EMA26; 조건 미충족; close=276.33, threshold=276.592, prior_ATR14=0.747363, EMA26=272.499 |
| v1 | session_vwap | 9864.66 | -135.34 | buy /  / 종가 > 뉴욕 거래일별 누적 전형가격 VWAP; 조건 충족; close=272.6, session_VWAP=272.22, session_volume=3.20722e+06 |
| v1 | obv_20 | 9856.04 | -143.96 | buy /  / OBV > OBV의 SMA20 그리고 종가 > EMA26; 조건 충족; OBV=-2.88653e+07, OBV_SMA20=-3.02185e+07, close=272.6, EMA26=271.529 |
| v1 | stochastic_14_3_recovery | 9665.87 | -334.13 | sell /  / 직전 %K14 < 20에서 %K14가 %D3 상향 돌파 (한 봉 목표); 조건 미충족; K14=72.727, D3=41.2922, previous_K14=34.0903, previous_D3=23.8263 |
| v1 | mfi_14_recovery | 9934.22 | -65.78 | sell /  / 직전 MFI14 < 20, 현재 MFI14 >= 20 (한 봉 목표); 조건 미충족; MFI14=34.131, previous_MFI14=22.0435 |
| v1 | adx_14_trend | 9787.22 | -212.78 | buy /  / Wilder ADX14 >= 25 그리고 +DI14 > -DI14; 조건 충족; ADX14=26.5262, plus_DI14=49.1478, minus_DI14=9.69634 |
| v1 | aroon_25_trend | 9784.20 | -215.80 | sell /  / Aroon25 Up > 70 그리고 Down < 30 (동률이면 최신 극값); 조건 미충족; Aroon_up=68, Aroon_down=20 |
| v1 | cci_20_momentum | 9955.08 | -44.92 | sell /  / CCI20 > 100 (전형가격·평균절대편차); 조건 미충족; CCI20=86.224 |
| v1 | williams_14_recovery | 9833.31 | -166.69 | sell /  / 직전 Williams %R14 < -80, 현재 >= -80 (한 봉 목표); 조건 미충족; Williams_R14=-27.273, previous_R14=-65.9097 |
| v1 | cmf_20_accumulation | 9808.62 | -191.38 | buy /  / Chaikin Money Flow20 > 0.1; 조건 충족; CMF20=0.208851, volume20=1.40263e+07 |
| v1 | chaikin_3_10 | 9856.93 | -143.07 | buy /  / ADL의 EMA3 - EMA10 > 0 그리고 종가 > EMA26; 조건 충족; Chaikin3_10=878293, ADL=-4.92877e+07, close=272.6, EMA26=271.529 |
| v1 | roc_10_momentum | 9996.39 | -3.61 | sell /  / 10봉 ROC > 1% 그리고 종가 > EMA26; 조건 미충족; ROC10_percent=0.995963, close=275.315, EMA26=273.754 |
| v1 | trix_15_trend | 9942.84 | -57.16 | buy /  / 15봉 삼중 EMA의 1봉 변화율 TRIX > 0 그리고 종가 > EMA26; 조건 충족; TRIX15_percent=0.00296855, close=273.97, EMA26=271.9 |
| v1 | keltner_20_breakout | 9933.72 | -66.28 | sell /  / 종가 > EMA20 + 2 x Wilder ATR14; 조건 미충족; close=275.315, upper_Keltner=275.695, EMA20=274.153, ATR14=0.771306 |
| v1 | opening_range_30m | 9947.23 | -52.77 | buy /  / 뉴욕 09:30·09:45 두 완료 봉 최고가를 10:00 이후 종가가 돌파; 조건 충족; close=275.845, opening_high=274.33 |
| v2 | cash | 10000.00 | 0.00 | 대기 /  / 새 신호 대기 |
| v2 | buy_hold | 9884.25 | -115.75 | buy / partial / 직전 완료 봉 목표 비중 100%; 다음 봉 시가 가정 |
| v2 | trend_8_26 | 9665.76 | -334.24 | buy / partial / 직전 완료 봉 목표 비중 100%; 다음 봉 시가 가정 |
| v2 | momentum_26 | 9835.29 | -164.71 | buy / partial / 직전 완료 봉 목표 비중 100%; 다음 봉 시가 가정 |
| v2 | breakout_8 | 9329.18 | -670.82 | sell / filled / 직전 완료 봉 목표 비중 0%; 다음 봉 시가 가정 |
| v2 | reversion_12 | 9325.80 | -674.20 | sell / filled / 직전 완료 봉 목표 비중 0%; 다음 봉 시가 가정 |
| v2 | volume_26 | 9434.73 | -565.27 | sell / filled / 직전 완료 봉 목표 비중 0%; 다음 봉 시가 가정 |
| v2 | trend_8_26 AND momentum_26 | 9829.77 | -170.23 | buy / partial / 직전 완료 봉 목표 비중 100%; 다음 봉 시가 가정 |
| v2 | trend_8_26 + momentum_26 | 9770.85 | -229.15 | buy / partial / 직전 완료 봉 목표 비중 100%; 다음 봉 시가 가정 |
| v2 | trend_8_26 AND breakout_8 | 9710.34 | -289.66 | sell / filled / 직전 완료 봉 목표 비중 0%; 다음 봉 시가 가정 |
| v2 | trend_8_26 + breakout_8 | 9516.24 | -483.76 | sell / filled / 직전 완료 봉 목표 비중 50%; 다음 봉 시가 가정 |
| v2 | trend_8_26 AND reversion_12 | 9705.35 | -294.65 | sell / filled / 직전 완료 봉 목표 비중 0%; 다음 봉 시가 가정 |
| v2 | trend_8_26 + reversion_12 | 9493.99 | -506.01 | sell / filled / 직전 완료 봉 목표 비중 50%; 다음 봉 시가 가정 |
| v2 | trend_8_26 AND volume_26 | 9797.73 | -202.27 | sell / filled / 직전 완료 봉 목표 비중 0%; 다음 봉 시가 가정 |
| v2 | trend_8_26 + volume_26 | 9589.61 | -410.39 | sell / filled / 직전 완료 봉 목표 비중 50%; 다음 봉 시가 가정 |
| v2 | momentum_26 AND breakout_8 | 9653.24 | -346.76 | sell / filled / 직전 완료 봉 목표 비중 0%; 다음 봉 시가 가정 |
| v2 | momentum_26 + breakout_8 | 9599.19 | -400.81 | sell / filled / 직전 완료 봉 목표 비중 50%; 다음 봉 시가 가정 |
| v2 | momentum_26 AND reversion_12 | 9881.28 | -118.72 | sell / filled / 직전 완료 봉 목표 비중 0%; 다음 봉 시가 가정 |
| v2 | momentum_26 + reversion_12 | 9616.97 | -383.03 | sell / filled / 직전 완료 봉 목표 비중 50%; 다음 봉 시가 가정 |
| v2 | momentum_26 AND volume_26 | 9957.22 | -42.78 | sell / filled / 직전 완료 봉 목표 비중 0%; 다음 봉 시가 가정 |
| v2 | momentum_26 + volume_26 | 9632.59 | -367.41 | sell / filled / 직전 완료 봉 목표 비중 50%; 다음 봉 시가 가정 |
| v2 | breakout_8 AND reversion_12 | 10000.00 | 0.00 | 대기 /  / 새 신호 대기 |
| v2 | breakout_8 + reversion_12 | 9366.25 | -633.75 | sell / filled / 직전 완료 봉 목표 비중 0%; 다음 봉 시가 가정 |
| v2 | breakout_8 AND volume_26 | 9710.25 | -289.75 | sell / filled / 직전 완료 봉 목표 비중 0%; 다음 봉 시가 가정 |
| v2 | breakout_8 + volume_26 | 9421.20 | -578.80 | sell / filled / 직전 완료 봉 목표 비중 0%; 다음 봉 시가 가정 |
| v2 | reversion_12 AND volume_26 | 9676.46 | -323.54 | sell / filled / 직전 완료 봉 목표 비중 0%; 다음 봉 시가 가정 |
| v2 | reversion_12 + volume_26 | 9419.31 | -580.69 | sell / filled / 직전 완료 봉 목표 비중 0%; 다음 봉 시가 가정 |
| v2 | ema_12_26 | 9856.75 | -143.25 | buy / partial / EMA12 > EMA26; 조건 충족; EMA12=271.545, EMA26=271.529; 직전 완료 봉 목표를 다음 봉 시가에 모의 적용 |
| v2 | macd_12_26_9 | 9900.47 | -99.53 | sell / filled / MACD > 신호선 그리고 MACD > 0; 조건 미충족; MACD=0.978353, signal9=1.01104; 직전 완료 봉 목표를 다음 봉 시가에 모의 적용 |
| v2 | rsi_14_recovery | 9779.12 | -220.88 | sell / filled / 직전 RSI14 < 30, 현재 RSI14 >= 30 (한 봉 목표); 조건 미충족; RSI14=46.986, previous_RSI14=37.1649; 직전 완료 봉 목표를 다음 봉 시가에 모의 적용 |
| v2 | bollinger_20_reentry | 9920.06 | -79.94 | sell / filled / 직전 종가 < 직전 하단밴드, 현재 하단밴드 <= 종가 <= SMA20 (한 봉 목표); 조건 미충족; close=271.19, lower20=270.018, SMA20=273.224, previous_lower20=270.283; 직전 완료 봉 목표를 다음 봉 시가에 모의 적용 |
| v2 | donchian_20 | 9830.01 | -169.99 | sell / filled / 종가 > 현재 봉을 제외한 직전 20봉 최고가; 조건 미충족; close=275.785, prior_high20=276.875; 직전 완료 봉 목표를 다음 봉 시가에 모의 적용 |
| v2 | atr_14_breakout | 9876.04 | -123.96 | sell / filled / 종가 > 직전 종가 + 직전 ATR14 그리고 종가 > EMA26; 조건 미충족; close=276.33, threshold=276.592, prior_ATR14=0.747363, EMA26=272.499; 직전 완료 봉 목표를 다음 봉 시가에 모의 적용 |
| v2 | session_vwap | 9855.78 | -144.22 | buy / partial / 종가 > 뉴욕 거래일별 누적 전형가격 VWAP; 조건 충족; close=272.6, session_VWAP=272.22, session_volume=3.20722e+06; 직전 완료 봉 목표를 다음 봉 시가에 모의 적용 |
| v2 | obv_20 | 9847.18 | -152.82 | buy / partial / OBV > OBV의 SMA20 그리고 종가 > EMA26; 조건 충족; OBV=-2.88653e+07, OBV_SMA20=-3.02185e+07, close=272.6, EMA26=271.529; 직전 완료 봉 목표를 다음 봉 시가에 모의 적용 |
| v2 | stochastic_14_3_recovery | 9650.41 | -349.59 | sell / filled / 직전 %K14 < 20에서 %K14가 %D3 상향 돌파 (한 봉 목표); 조건 미충족; K14=72.727, D3=41.2922, previous_K14=34.0903, previous_D3=23.8263; 직전 완료 봉 목표를 다음 봉 시가에 모의 적용 |
| v2 | mfi_14_recovery | 9930.25 | -69.75 | sell / filled / 직전 MFI14 < 20, 현재 MFI14 >= 20 (한 봉 목표); 조건 미충족; MFI14=34.131, previous_MFI14=22.0435; 직전 완료 봉 목표를 다음 봉 시가에 모의 적용 |
| v2 | adx_14_trend | 9782.33 | -217.67 | buy / partial / Wilder ADX14 >= 25 그리고 +DI14 > -DI14; 조건 충족; ADX14=26.5262, plus_DI14=49.1478, minus_DI14=9.69634; 직전 완료 봉 목표를 다음 봉 시가에 모의 적용 |
| v2 | aroon_25_trend | 9776.38 | -223.62 | sell / filled / Aroon25 Up > 70 그리고 Down < 30 (동률이면 최신 극값); 조건 미충족; Aroon_up=68, Aroon_down=20; 직전 완료 봉 목표를 다음 봉 시가에 모의 적용 |
| v2 | cci_20_momentum | 9949.11 | -50.89 | sell / filled / CCI20 > 100 (전형가격·평균절대편차); 조건 미충족; CCI20=86.224; 직전 완료 봉 목표를 다음 봉 시가에 모의 적용 |
| v2 | williams_14_recovery | 9825.45 | -174.55 | sell / filled / 직전 Williams %R14 < -80, 현재 >= -80 (한 봉 목표); 조건 미충족; Williams_R14=-27.273, previous_R14=-65.9097; 직전 완료 봉 목표를 다음 봉 시가에 모의 적용 |
| v2 | cmf_20_accumulation | 9795.88 | -204.12 | buy / partial / Chaikin Money Flow20 > 0.1; 조건 충족; CMF20=0.208851, volume20=1.40263e+07; 직전 완료 봉 목표를 다음 봉 시가에 모의 적용 |
| v2 | chaikin_3_10 | 9848.07 | -151.93 | buy / partial / ADL의 EMA3 - EMA10 > 0 그리고 종가 > EMA26; 조건 충족; Chaikin3_10=878293, ADL=-4.92877e+07, close=272.6, EMA26=271.529; 직전 완료 봉 목표를 다음 봉 시가에 모의 적용 |
| v2 | roc_10_momentum | 9994.39 | -5.61 | sell / filled / 10봉 ROC > 1% 그리고 종가 > EMA26; 조건 미충족; ROC10_percent=0.995963, close=275.315, EMA26=273.754; 직전 완료 봉 목표를 다음 봉 시가에 모의 적용 |
| v2 | trix_15_trend | 9939.85 | -60.15 | buy / partial / 15봉 삼중 EMA의 1봉 변화율 TRIX > 0 그리고 종가 > EMA26; 조건 충족; TRIX15_percent=0.00296855, close=273.97, EMA26=271.9; 직전 완료 봉 목표를 다음 봉 시가에 모의 적용 |
| v2 | keltner_20_breakout | 9929.75 | -70.25 | sell / filled / 종가 > EMA20 + 2 x Wilder ATR14; 조건 미충족; close=275.315, upper_Keltner=275.695, EMA20=274.153, ATR14=0.771306; 직전 완료 봉 목표를 다음 봉 시가에 모의 적용 |
| v2 | opening_range_30m | 9944.24 | -55.76 | buy / partial / 뉴욕 09:30·09:45 두 완료 봉 최고가를 10:00 이후 종가가 돌파; 조건 충족; close=275.845, opening_high=274.33; 직전 완료 봉 목표를 다음 봉 시가에 모의 적용 |

### 같은 기간의 비용·노출 비교 (사후 연구)

| 전략 | 비용 전 | 비용 후 | 100% 보유 | 같은 평균 노출 보유 | 평균 노출 |
|---|---:|---:|---:|---:|---:|
| cash | 0.00% | 0.00% | -1.96% | -0.00% | 0.00% |
| buy_hold | -1.55% | -1.96% | -1.96% | -1.96% | 100.00% |
| trend_8_26 | -0.81% | -4.49% | -1.96% | -0.94% | 47.77% |
| momentum_26 | -0.70% | -6.38% | -1.96% | -0.90% | 45.41% |
| breakout_8 | -0.32% | -14.30% | -1.96% | -0.40% | 19.95% |
| reversion_12 | -2.15% | -13.73% | -1.96% | -0.55% | 27.82% |
| volume_26 | -1.61% | -8.78% | -1.96% | -0.17% | 8.66% |
| trend_8_26 AND momentum_26 | -0.73% | -5.21% | -1.96% | -0.76% | 38.58% |
| trend_8_26 + momentum_26 | -0.75% | -5.03% | -1.96% | -0.92% | 46.59% |
| trend_8_26 AND breakout_8 | -0.53% | -8.92% | -1.96% | -0.25% | 12.60% |
| trend_8_26 + breakout_8 | -0.55% | -9.33% | -1.96% | -0.67% | 33.86% |
| trend_8_26 AND reversion_12 | -0.74% | -4.82% | -1.96% | -0.11% | 5.51% |
| trend_8_26 + reversion_12 | -1.47% | -9.04% | -1.96% | -0.75% | 37.80% |
| trend_8_26 AND volume_26 | -0.98% | -3.85% | -1.96% | -0.05% | 2.62% |
| trend_8_26 + volume_26 | -1.20% | -6.27% | -1.96% | -0.56% | 28.22% |
| momentum_26 AND breakout_8 | 0.22% | -8.24% | -1.96% | -0.23% | 11.81% |
| momentum_26 + breakout_8 | -0.51% | -10.24% | -1.96% | -0.65% | 32.68% |
| momentum_26 AND reversion_12 | 0.03% | -3.68% | -1.96% | -0.07% | 3.67% |
| momentum_26 + reversion_12 | -1.42% | -9.19% | -1.96% | -0.72% | 36.62% |
| momentum_26 AND volume_26 | 0.06% | -2.02% | -1.96% | -0.04% | 1.84% |
| momentum_26 + volume_26 | -1.15% | -7.20% | -1.96% | -0.54% | 27.04% |
| breakout_8 AND reversion_12 | 0.00% | 0.00% | -1.96% | -0.00% | 0.00% |
| breakout_8 + reversion_12 | -1.23% | -13.48% | -1.96% | -0.47% | 23.89% |
| breakout_8 AND volume_26 | -0.84% | -4.11% | -1.96% | -0.05% | 2.62% |
| breakout_8 + volume_26 | -0.96% | -11.21% | -1.96% | -0.28% | 14.31% |
| reversion_12 AND volume_26 | -0.62% | -4.31% | -1.96% | -0.08% | 3.94% |
| reversion_12 + volume_26 | -1.87% | -10.73% | -1.96% | -0.36% | 18.25% |
| ema_12_26 | 0.95% | -1.97% | -1.96% | -0.93% | 47.24% |
| macd_12_26_9 | 2.60% | -0.38% | -1.96% | -0.62% | 31.50% |
| rsi_14_recovery | -0.65% | -5.14% | -1.96% | -0.06% | 2.89% |
| bollinger_20_reentry | -0.24% | -4.35% | -1.96% | -0.05% | 2.62% |
| donchian_20 | -0.34% | -6.04% | -1.96% | -0.13% | 6.56% |
| atr_14_breakout | -0.52% | -7.37% | -1.96% | -0.09% | 4.72% |
| session_vwap | 0.27% | -9.34% | -1.96% | -0.87% | 43.83% |
| obv_20 | 0.89% | -3.66% | -1.96% | -0.83% | 41.73% |
| stochastic_14_3_recovery | -0.44% | -12.96% | -1.96% | -0.17% | 8.40% |
| mfi_14_recovery | 0.36% | -4.17% | -1.96% | -0.06% | 2.89% |
| adx_14_trend | -0.34% | -4.03% | -1.96% | -0.67% | 33.86% |
| aroon_25_trend | -1.30% | -5.76% | -1.96% | -0.44% | 22.05% |
| cci_20_momentum | -1.41% | -8.20% | -1.96% | -0.40% | 20.21% |
| williams_14_recovery | -0.09% | -9.29% | -1.96% | -0.12% | 6.04% |
| cmf_20_accumulation | -0.72% | -7.95% | -1.96% | -0.44% | 22.31% |
| chaikin_3_10 | -1.23% | -8.04% | -1.96% | -0.69% | 34.65% |
| roc_10_momentum | -0.27% | -1.93% | -1.96% | -0.11% | 5.51% |
| trix_15_trend | 1.03% | -2.31% | -1.96% | -0.69% | 34.91% |
| keltner_20_breakout | -0.55% | -4.24% | -1.96% | -0.15% | 7.61% |
| opening_range_30m | 2.56% | -1.66% | -1.96% | -0.49% | 24.67% |

동일 구간·초기 자금, 종료 시 청산 비용 포함. 노출 맞춤은 사후 설명용이며 v2 실제 계좌 성과가 아닙니다.
[낙폭 분해·비용 영향·전체 구간](IWM/comparison.json)

[v1 전체 기록](IWM/accounts.json) · [v2 전체 기록](IWM/accounts-v2.json)

## DIA 계좌

| 모델 | 전략 | 평가액 USD | 손익 USD | 최근 매매·이유 |
|---|---|---:|---:|---|
| v1 | cash | 10000.00 | 0.00 | 대기 /  / 새 신호 대기 |
| v1 | buy_hold | 10008.56 | 8.56 | buy /  / buy_hold: prior completed bar target 100%; next bar open simulation |
| v1 | trend_8_26 | 9966.88 | -33.12 | buy /  / trend_8_26: prior completed bar target 100%; next bar open simulation |
| v1 | momentum_26 | 9863.00 | -137.00 | buy /  / momentum_26: prior completed bar target 100%; next bar open simulation |
| v1 | breakout_8 | 9678.32 | -321.68 | buy /  / breakout_8: prior completed bar target 100%; next bar open simulation |
| v1 | reversion_12 | 9897.27 | -102.73 | sell /  / reversion_12: prior completed bar target 0%; next bar open simulation |
| v1 | volume_26 | 9939.83 | -60.17 | sell /  / volume_26: prior completed bar target 0%; next bar open simulation |
| v1 | trend_8_26 AND momentum_26 | 9863.00 | -137.00 | buy /  / trend_8_26 AND momentum_26: prior completed bar target 100%; next bar open simulation |
| v1 | trend_8_26 + momentum_26 | 9914.89 | -85.11 | buy /  / trend_8_26 + momentum_26: prior completed bar target 100%; next bar open simulation |
| v1 | trend_8_26 AND breakout_8 | 9810.26 | -189.74 | buy /  / trend_8_26 AND breakout_8: prior completed bar target 100%; next bar open simulation |
| v1 | trend_8_26 + breakout_8 | 9841.25 | -158.75 | buy /  / trend_8_26 + breakout_8: prior completed bar target 100%; next bar open simulation |
| v1 | trend_8_26 AND reversion_12 | 9940.76 | -59.24 | sell /  / trend_8_26 AND reversion_12: prior completed bar target 0%; next bar open simulation |
| v1 | trend_8_26 + reversion_12 | 9931.88 | -68.12 | sell /  / trend_8_26 + reversion_12: prior completed bar target 50%; next bar open simulation |
| v1 | trend_8_26 AND volume_26 | 9974.09 | -25.91 | sell /  / trend_8_26 AND volume_26: prior completed bar target 0%; next bar open simulation |
| v1 | trend_8_26 + volume_26 | 9953.23 | -46.77 | sell /  / trend_8_26 + volume_26: prior completed bar target 50%; next bar open simulation |
| v1 | momentum_26 AND breakout_8 | 9810.26 | -189.74 | buy /  / momentum_26 AND breakout_8: prior completed bar target 100%; next bar open simulation |
| v1 | momentum_26 + breakout_8 | 9770.23 | -229.77 | buy /  / momentum_26 + breakout_8: prior completed bar target 100%; next bar open simulation |
| v1 | momentum_26 AND reversion_12 | 9940.78 | -59.22 | sell /  / momentum_26 AND reversion_12: prior completed bar target 0%; next bar open simulation |
| v1 | momentum_26 + reversion_12 | 9919.56 | -80.44 | sell /  / momentum_26 + reversion_12: prior completed bar target 50%; next bar open simulation |
| v1 | momentum_26 AND volume_26 | 9929.52 | -70.48 | sell /  / momentum_26 AND volume_26: prior completed bar target 0%; next bar open simulation |
| v1 | momentum_26 + volume_26 | 9921.09 | -78.91 | sell /  / momentum_26 + volume_26: prior completed bar target 50%; next bar open simulation |
| v1 | breakout_8 AND reversion_12 | 10000.00 | 0.00 | 대기 /  / 새 신호 대기 |
| v1 | breakout_8 + reversion_12 | 9806.66 | -193.34 | buy /  / breakout_8 + reversion_12: prior completed bar target 50%; next bar open simulation |
| v1 | breakout_8 AND volume_26 | 9986.25 | -13.75 | sell /  / breakout_8 AND volume_26: prior completed bar target 0%; next bar open simulation |
| v1 | breakout_8 + volume_26 | 9847.48 | -152.52 | buy /  / breakout_8 + volume_26: prior completed bar target 50%; next bar open simulation |
| v1 | reversion_12 AND volume_26 | 9970.42 | -29.58 | sell /  / reversion_12 AND volume_26: prior completed bar target 0%; next bar open simulation |
| v1 | reversion_12 + volume_26 | 9938.32 | -61.68 | sell /  / reversion_12 + volume_26: prior completed bar target 0%; next bar open simulation |
| v1 | ema_12_26 | 9863.23 | -136.77 | buy /  / EMA12 > EMA26; 조건 충족; EMA12=519.74, EMA26=519.585 |
| v1 | macd_12_26_9 | 9895.59 | -104.41 | sell /  / MACD > 신호선 그리고 MACD > 0; 조건 미충족; MACD=1.09098, signal9=1.12388 |
| v1 | rsi_14_recovery | 10000.00 | 0.00 | 대기 /  / 새 신호 대기 |
| v1 | bollinger_20_reentry | 9978.51 | -21.49 | sell /  / 직전 종가 < 직전 하단밴드, 현재 하단밴드 <= 종가 <= SMA20 (한 봉 목표); 조건 미충족; close=519.823, lower20=518.355, SMA20=521.612, previous_lower20=518.548 |
| v1 | donchian_20 | 9822.00 | -178.00 | sell /  / 종가 > 현재 봉을 제외한 직전 20봉 최고가; 조건 미충족; close=523.68, prior_high20=526.17 |
| v1 | atr_14_breakout | 9885.70 | -114.30 | sell /  / 종가 > 직전 종가 + 직전 ATR14 그리고 종가 > EMA26; 조건 미충족; close=525.49, threshold=525.841, prior_ATR14=0.980592, EMA26=520.815 |
| v1 | session_vwap | 9918.20 | -81.80 | buy /  / 종가 > 뉴욕 거래일별 누적 전형가격 VWAP; 조건 충족; close=521.46, session_VWAP=520.55, session_volume=446463 |
| v1 | obv_20 | 9869.50 | -130.50 | buy /  / OBV > OBV의 SMA20 그리고 종가 > EMA26; 조건 충족; OBV=-9.86891e+06, OBV_SMA20=-1.0028e+07, close=521.46, EMA26=519.585 |
| v1 | stochastic_14_3_recovery | 9821.00 | -179.00 | sell /  / 직전 %K14 < 20에서 %K14가 %D3 상향 돌파 (한 봉 목표); 조건 미충족; K14=100, D3=70.5235, previous_K14=91.7443, previous_D3=57.9113 |
| v1 | mfi_14_recovery | 9936.38 | -63.62 | sell /  / 직전 MFI14 < 20, 현재 MFI14 >= 20 (한 봉 목표); 조건 미충족; MFI14=44.8014, previous_MFI14=20.0271 |
| v1 | adx_14_trend | 9811.65 | -188.35 | sell /  / Wilder ADX14 >= 25 그리고 +DI14 > -DI14; 조건 미충족; ADX14=24.7281, plus_DI14=33.8838, minus_DI14=22.7145 |
| v1 | aroon_25_trend | 9928.84 | -71.16 | sell /  / Aroon25 Up > 70 그리고 Down < 30 (동률이면 최신 극값); 조건 미충족; Aroon_up=100, Aroon_down=80 |
| v1 | cci_20_momentum | 9915.48 | -84.52 | sell /  / CCI20 > 100 (전형가격·평균절대편차); 조건 미충족; CCI20=87.8356 |
| v1 | williams_14_recovery | 9854.30 | -145.70 | sell /  / 직전 Williams %R14 < -80, 현재 >= -80 (한 봉 목표); 조건 미충족; Williams_R14=0, previous_R14=-8.25572 |
| v1 | cmf_20_accumulation | 9819.72 | -180.28 | buy /  / Chaikin Money Flow20 > 0.1; 조건 충족; CMF20=0.237356, volume20=1.61808e+06 |
| v1 | chaikin_3_10 | 9871.42 | -128.58 | buy /  / ADL의 EMA3 - EMA10 > 0 그리고 종가 > EMA26; 조건 충족; Chaikin3_10=78733.3, ADL=-1.64223e+07, close=521.46, EMA26=519.585 |
| v1 | roc_10_momentum | 9939.01 | -60.99 | sell /  / 10봉 ROC > 1% 그리고 종가 > EMA26; 조건 미충족; ROC10_percent=0.771645, close=523.68, EMA26=521.367 |
| v1 | trix_15_trend | 9964.79 | -35.21 | buy /  / 15봉 삼중 EMA의 1봉 변화율 TRIX > 0 그리고 종가 > EMA26; 조건 충족; TRIX15_percent=0.000473967, close=521.46, EMA26=519.585 |
| v1 | keltner_20_breakout | 9944.49 | -55.51 | sell /  / 종가 > EMA20 + 2 x Wilder ATR14; 조건 미충족; close=523.68, upper_Keltner=523.985, EMA20=521.785, ATR14=1.10038 |
| v1 | opening_range_30m | 9802.20 | -197.80 | buy /  / 뉴욕 09:30·09:45 두 완료 봉 최고가를 10:00 이후 종가가 돌파; 조건 충족; close=524.86, opening_high=523.47 |
| v2 | cash | 10000.00 | 0.00 | 대기 /  / 새 신호 대기 |
| v2 | buy_hold | 10132.56 | 132.56 | buy / partial / 직전 완료 봉 목표 비중 100%; 다음 봉 시가 가정 |
| v2 | trend_8_26 | 9900.34 | -99.66 | buy / partial / 직전 완료 봉 목표 비중 100%; 다음 봉 시가 가정 |
| v2 | momentum_26 | 9900.90 | -99.10 | buy / partial / 직전 완료 봉 목표 비중 100%; 다음 봉 시가 가정 |
| v2 | breakout_8 | 9205.33 | -794.67 | buy / partial / 직전 완료 봉 목표 비중 100%; 다음 봉 시가 가정 |
| v2 | reversion_12 | 9592.64 | -407.36 | sell / filled / 직전 완료 봉 목표 비중 0%; 다음 봉 시가 가정 |
| v2 | volume_26 | 9652.01 | -347.99 | sell / filled / 직전 완료 봉 목표 비중 0%; 다음 봉 시가 가정 |
| v2 | trend_8_26 AND momentum_26 | 9896.31 | -103.69 | buy / partial / 직전 완료 봉 목표 비중 100%; 다음 봉 시가 가정 |
| v2 | trend_8_26 + momentum_26 | 9900.78 | -99.22 | buy / partial / 직전 완료 봉 목표 비중 100%; 다음 봉 시가 가정 |
| v2 | trend_8_26 AND breakout_8 | 9494.40 | -505.60 | buy / partial / 직전 완료 봉 목표 비중 100%; 다음 봉 시가 가정 |
| v2 | trend_8_26 + breakout_8 | 9566.69 | -433.31 | buy / partial / 직전 완료 봉 목표 비중 100%; 다음 봉 시가 가정 |
| v2 | trend_8_26 AND reversion_12 | 9748.75 | -251.25 | sell / filled / 직전 완료 봉 목표 비중 0%; 다음 봉 시가 가정 |
| v2 | trend_8_26 + reversion_12 | 9744.89 | -255.11 | sell / filled / 직전 완료 봉 목표 비중 50%; 다음 봉 시가 가정 |
| v2 | trend_8_26 AND volume_26 | 9827.44 | -172.56 | sell / filled / 직전 완료 봉 목표 비중 0%; 다음 봉 시가 가정 |
| v2 | trend_8_26 + volume_26 | 9795.76 | -204.24 | sell / filled / 직전 완료 봉 목표 비중 50%; 다음 봉 시가 가정 |
| v2 | momentum_26 AND breakout_8 | 9483.59 | -516.41 | buy / partial / 직전 완료 봉 목표 비중 100%; 다음 봉 시가 가정 |
| v2 | momentum_26 + breakout_8 | 9546.92 | -453.08 | buy / partial / 직전 완료 봉 목표 비중 100%; 다음 봉 시가 가정 |
| v2 | momentum_26 AND reversion_12 | 9895.03 | -104.97 | sell / filled / 직전 완료 봉 목표 비중 0%; 다음 봉 시가 가정 |
| v2 | momentum_26 + reversion_12 | 9786.22 | -213.78 | sell / filled / 직전 완료 봉 목표 비중 50%; 다음 봉 시가 가정 |
| v2 | momentum_26 AND volume_26 | 9716.58 | -283.42 | sell / filled / 직전 완료 봉 목표 비중 0%; 다음 봉 시가 가정 |
| v2 | momentum_26 + volume_26 | 9837.45 | -162.55 | sell / filled / 직전 완료 봉 목표 비중 50%; 다음 봉 시가 가정 |
| v2 | breakout_8 AND reversion_12 | 10000.00 | 0.00 | 대기 /  / 새 신호 대기 |
| v2 | breakout_8 + reversion_12 | 9416.19 | -583.81 | buy / filled / 직전 완료 봉 목표 비중 50%; 다음 봉 시가 가정 |
| v2 | breakout_8 AND volume_26 | 9781.13 | -218.87 | sell / filled / 직전 완료 봉 목표 비중 0%; 다음 봉 시가 가정 |
| v2 | breakout_8 + volume_26 | 9465.50 | -534.50 | buy / filled / 직전 완료 봉 목표 비중 50%; 다음 봉 시가 가정 |
| v2 | reversion_12 AND volume_26 | 9966.44 | -33.56 | sell / filled / 직전 완료 봉 목표 비중 0%; 다음 봉 시가 가정 |
| v2 | reversion_12 + volume_26 | 9642.17 | -357.83 | sell / filled / 직전 완료 봉 목표 비중 0%; 다음 봉 시가 가정 |
| v2 | ema_12_26 | 9858.31 | -141.69 | buy / partial / EMA12 > EMA26; 조건 충족; EMA12=519.74, EMA26=519.585; 직전 완료 봉 목표를 다음 봉 시가에 모의 적용 |
| v2 | macd_12_26_9 | 9889.66 | -110.34 | sell / filled / MACD > 신호선 그리고 MACD > 0; 조건 미충족; MACD=1.09098, signal9=1.12388; 직전 완료 봉 목표를 다음 봉 시가에 모의 적용 |
| v2 | rsi_14_recovery | 10000.00 | 0.00 | 대기 /  / 새 신호 대기 |
| v2 | bollinger_20_reentry | 9976.52 | -23.48 | sell / filled / 직전 종가 < 직전 하단밴드, 현재 하단밴드 <= 종가 <= SMA20 (한 봉 목표); 조건 미충족; close=519.823, lower20=518.355, SMA20=521.612, previous_lower20=518.548; 직전 완료 봉 목표를 다음 봉 시가에 모의 적용 |
| v2 | donchian_20 | 9814.14 | -185.86 | sell / filled / 종가 > 현재 봉을 제외한 직전 20봉 최고가; 조건 미충족; close=523.68, prior_high20=526.17; 직전 완료 봉 목표를 다음 봉 시가에 모의 적용 |
| v2 | atr_14_breakout | 9877.79 | -122.21 | sell / filled / 종가 > 직전 종가 + 직전 ATR14 그리고 종가 > EMA26; 조건 미충족; close=525.49, threshold=525.841, prior_ATR14=0.980592, EMA26=520.815; 직전 완료 봉 목표를 다음 봉 시가에 모의 적용 |
| v2 | session_vwap | 9911.26 | -88.74 | buy / partial / 종가 > 뉴욕 거래일별 누적 전형가격 VWAP; 조건 충족; close=521.46, session_VWAP=520.55, session_volume=446463; 직전 완료 봉 목표를 다음 봉 시가에 모의 적용 |
| v2 | obv_20 | 9862.60 | -137.40 | buy / partial / OBV > OBV의 SMA20 그리고 종가 > EMA26; 조건 충족; OBV=-9.86891e+06, OBV_SMA20=-1.0028e+07, close=521.46, EMA26=519.585; 직전 완료 봉 목표를 다음 봉 시가에 모의 적용 |
| v2 | stochastic_14_3_recovery | 9811.19 | -188.81 | sell / filled / 직전 %K14 < 20에서 %K14가 %D3 상향 돌파 (한 봉 목표); 조건 미충족; K14=100, D3=70.5235, previous_K14=91.7443, previous_D3=57.9113; 직전 완료 봉 목표를 다음 봉 시가에 모의 적용 |
| v2 | mfi_14_recovery | 9932.40 | -67.60 | sell / filled / 직전 MFI14 < 20, 현재 MFI14 >= 20 (한 봉 목표); 조건 미충족; MFI14=44.8014, previous_MFI14=20.0271; 직전 완료 봉 목표를 다음 봉 시가에 모의 적용 |
| v2 | adx_14_trend | 9805.77 | -194.23 | sell / filled / Wilder ADX14 >= 25 그리고 +DI14 > -DI14; 조건 미충족; ADX14=24.7281, plus_DI14=33.8838, minus_DI14=22.7145; 직전 완료 봉 목표를 다음 봉 시가에 모의 적용 |
| v2 | aroon_25_trend | 9922.89 | -77.11 | sell / filled / Aroon25 Up > 70 그리고 Down < 30 (동률이면 최신 극값); 조건 미충족; Aroon_up=100, Aroon_down=80; 직전 완료 봉 목표를 다음 봉 시가에 모의 적용 |
| v2 | cci_20_momentum | 9909.53 | -90.47 | sell / filled / CCI20 > 100 (전형가격·평균절대편차); 조건 미충족; CCI20=87.8356; 직전 완료 봉 목표를 다음 봉 시가에 모의 적용 |
| v2 | williams_14_recovery | 9846.42 | -153.58 | sell / filled / 직전 Williams %R14 < -80, 현재 >= -80 (한 봉 목표); 조건 미충족; Williams_R14=0, previous_R14=-8.25572; 직전 완료 봉 목표를 다음 봉 시가에 모의 적용 |
| v2 | cmf_20_accumulation | 9810.89 | -189.11 | buy / partial / Chaikin Money Flow20 > 0.1; 조건 충족; CMF20=0.237356, volume20=1.61808e+06; 직전 완료 봉 목표를 다음 봉 시가에 모의 적용 |
| v2 | chaikin_3_10 | 9864.51 | -135.49 | buy / partial / ADL의 EMA3 - EMA10 > 0 그리고 종가 > EMA26; 조건 충족; Chaikin3_10=78733.3, ADL=-1.64223e+07, close=521.46, EMA26=519.585; 직전 완료 봉 목표를 다음 봉 시가에 모의 적용 |
| v2 | roc_10_momentum | 9937.03 | -62.97 | sell / filled / 10봉 ROC > 1% 그리고 종가 > EMA26; 조건 미충족; ROC10_percent=0.771645, close=523.68, EMA26=521.367; 직전 완료 봉 목표를 다음 봉 시가에 모의 적용 |
| v2 | trix_15_trend | 9961.80 | -38.20 | buy / partial / 15봉 삼중 EMA의 1봉 변화율 TRIX > 0 그리고 종가 > EMA26; 조건 충족; TRIX15_percent=0.000473967, close=521.46, EMA26=519.585; 직전 완료 봉 목표를 다음 봉 시가에 모의 적용 |
| v2 | keltner_20_breakout | 9940.51 | -59.49 | sell / filled / 종가 > EMA20 + 2 x Wilder ATR14; 조건 미충족; close=523.68, upper_Keltner=523.985, EMA20=521.785, ATR14=1.10038; 직전 완료 봉 목표를 다음 봉 시가에 모의 적용 |
| v2 | opening_range_30m | 9793.38 | -206.62 | buy / partial / 뉴욕 09:30·09:45 두 완료 봉 최고가를 10:00 이후 종가가 돌파; 조건 충족; close=524.86, opening_high=523.47; 직전 완료 봉 목표를 다음 봉 시가에 모의 적용 |

### 같은 기간의 비용·노출 비교 (사후 연구)

| 전략 | 비용 전 | 비용 후 | 100% 보유 | 같은 평균 노출 보유 | 평균 노출 |
|---|---:|---:|---:|---:|---:|
| cash | 0.00% | 0.00% | 1.59% | 0.00% | 0.00% |
| buy_hold | 2.02% | 1.59% | 1.59% | 1.59% | 100.00% |
| trend_8_26 | 2.07% | -1.72% | 1.59% | 0.99% | 61.94% |
| momentum_26 | 0.84% | -3.72% | 1.59% | 0.91% | 56.96% |
| breakout_8 | 0.78% | -16.58% | 1.59% | 0.37% | 23.36% |
| reversion_12 | -0.58% | -8.59% | 1.59% | 0.36% | 22.31% |
| volume_26 | 0.22% | -9.77% | 1.59% | 0.18% | 11.02% |
| trend_8_26 AND momentum_26 | 1.95% | -2.65% | 1.59% | 0.82% | 51.71% |
| trend_8_26 + momentum_26 | 1.45% | -2.72% | 1.59% | 0.95% | 59.45% |
| trend_8_26 AND breakout_8 | 1.17% | -11.55% | 1.59% | 0.26% | 16.27% |
| trend_8_26 + breakout_8 | 1.42% | -9.07% | 1.59% | 0.68% | 42.66% |
| trend_8_26 AND reversion_12 | 0.43% | -4.91% | 1.59% | 0.11% | 6.82% |
| trend_8_26 + reversion_12 | 0.74% | -5.02% | 1.59% | 0.67% | 42.13% |
| trend_8_26 AND volume_26 | 1.48% | -4.32% | 1.59% | 0.10% | 6.04% |
| trend_8_26 + volume_26 | 1.14% | -5.64% | 1.59% | 0.58% | 36.49% |
| momentum_26 AND breakout_8 | 0.34% | -12.28% | 1.59% | 0.27% | 16.80% |
| momentum_26 + breakout_8 | 0.81% | -10.19% | 1.59% | 0.64% | 40.16% |
| momentum_26 AND reversion_12 | -0.27% | -3.57% | 1.59% | 0.09% | 5.77% |
| momentum_26 + reversion_12 | 0.13% | -5.20% | 1.59% | 0.63% | 39.64% |
| momentum_26 AND volume_26 | 0.10% | -5.62% | 1.59% | 0.09% | 5.51% |
| momentum_26 + volume_26 | 0.53% | -6.01% | 1.59% | 0.54% | 33.99% |
| breakout_8 AND reversion_12 | 0.00% | 0.00% | 1.59% | 0.00% | 0.00% |
| breakout_8 + reversion_12 | 0.10% | -12.32% | 1.59% | 0.36% | 22.84% |
| breakout_8 AND volume_26 | -0.47% | -3.75% | 1.59% | 0.05% | 3.15% |
| breakout_8 + volume_26 | 0.50% | -12.15% | 1.59% | 0.27% | 17.20% |
| reversion_12 AND volume_26 | 0.29% | -4.24% | 1.59% | 0.05% | 3.41% |
| reversion_12 + volume_26 | -0.18% | -9.00% | 1.59% | 0.27% | 16.67% |
| ema_12_26 | 0.64% | -2.28% | 1.59% | 0.86% | 54.33% |
| macd_12_26_9 | 1.99% | -1.79% | 1.59% | 0.51% | 32.28% |
| rsi_14_recovery | 0.16% | -1.09% | 1.59% | 0.01% | 0.79% |
| bollinger_20_reentry | 0.11% | -4.01% | 1.59% | 0.04% | 2.62% |
| donchian_20 | 0.36% | -6.94% | 1.59% | 0.15% | 9.71% |
| atr_14_breakout | -0.26% | -7.52% | 1.59% | 0.09% | 5.77% |
| session_vwap | 2.34% | -5.51% | 1.59% | 0.84% | 53.02% |
| obv_20 | 0.91% | -7.22% | 1.59% | 0.74% | 46.19% |
| stochastic_14_3_recovery | 0.95% | -11.00% | 1.59% | 0.13% | 7.87% |
| mfi_14_recovery | 0.16% | -3.15% | 1.59% | 0.03% | 2.10% |
| adx_14_trend | -0.13% | -4.23% | 1.59% | 0.53% | 33.33% |
| aroon_25_trend | 1.36% | -2.40% | 1.59% | 0.43% | 26.77% |
| cci_20_momentum | 0.82% | -5.74% | 1.59% | 0.41% | 25.72% |
| williams_14_recovery | 1.54% | -6.25% | 1.59% | 0.08% | 4.99% |
| cmf_20_accumulation | 1.57% | -6.22% | 1.59% | 0.50% | 31.50% |
| chaikin_3_10 | 2.12% | -7.28% | 1.59% | 0.73% | 45.67% |
| roc_10_momentum | -0.07% | -0.90% | 1.59% | 0.03% | 2.10% |
| trix_15_trend | 0.76% | -2.97% | 1.59% | 0.74% | 46.19% |
| keltner_20_breakout | 0.78% | -5.77% | 1.59% | 0.29% | 18.37% |
| opening_range_30m | 1.65% | -4.15% | 1.59% | 0.44% | 27.56% |

동일 구간·초기 자금, 종료 시 청산 비용 포함. 노출 맞춤은 사후 설명용이며 v2 실제 계좌 성과가 아닙니다.
[낙폭 분해·비용 영향·전체 구간](DIA/comparison.json)

[v1 전체 기록](DIA/accounts.json) · [v2 전체 기록](DIA/accounts-v2.json)

## MSFT 계좌

| 모델 | 전략 | 평가액 USD | 손익 USD | 최근 매매·이유 |
|---|---|---:|---:|---|
| v1 | cash | 10000.00 | 0.00 | 대기 /  / 새 신호 대기 |
| v1 | buy_hold | 9840.95 | -159.05 | buy /  / buy_hold: prior completed bar target 100%; next bar open simulation |
| v1 | trend_8_26 | 9677.44 | -322.56 | sell /  / trend_8_26: prior completed bar target 0%; next bar open simulation |
| v1 | momentum_26 | 9626.73 | -373.27 | buy /  / momentum_26: prior completed bar target 100%; next bar open simulation |
| v1 | breakout_8 | 9698.82 | -301.18 | buy /  / breakout_8: prior completed bar target 100%; next bar open simulation |
| v1 | reversion_12 | 9685.33 | -314.67 | sell /  / reversion_12: prior completed bar target 0%; next bar open simulation |
| v1 | volume_26 | 9811.31 | -188.69 | sell /  / volume_26: prior completed bar target 0%; next bar open simulation |
| v1 | trend_8_26 AND momentum_26 | 9662.97 | -337.03 | sell /  / trend_8_26 AND momentum_26: prior completed bar target 0%; next bar open simulation |
| v1 | trend_8_26 + momentum_26 | 9652.05 | -347.95 | buy /  / trend_8_26 + momentum_26: prior completed bar target 50%; next bar open simulation |
| v1 | trend_8_26 AND breakout_8 | 9820.11 | -179.89 | sell /  / trend_8_26 AND breakout_8: prior completed bar target 0%; next bar open simulation |
| v1 | trend_8_26 + breakout_8 | 9707.78 | -292.22 | sell /  / trend_8_26 + breakout_8: prior completed bar target 50%; next bar open simulation |
| v1 | trend_8_26 AND reversion_12 | 9721.64 | -278.36 | sell /  / trend_8_26 AND reversion_12: prior completed bar target 0%; next bar open simulation |
| v1 | trend_8_26 + reversion_12 | 9681.35 | -318.65 | sell /  / trend_8_26 + reversion_12: prior completed bar target 0%; next bar open simulation |
| v1 | trend_8_26 AND volume_26 | 9916.79 | -83.21 | sell /  / trend_8_26 AND volume_26: prior completed bar target 0%; next bar open simulation |
| v1 | trend_8_26 + volume_26 | 9744.38 | -255.62 | sell /  / trend_8_26 + volume_26: prior completed bar target 0%; next bar open simulation |
| v1 | momentum_26 AND breakout_8 | 9797.56 | -202.44 | buy /  / momentum_26 AND breakout_8: prior completed bar target 100%; next bar open simulation |
| v1 | momentum_26 + breakout_8 | 9662.99 | -337.01 | buy /  / momentum_26 + breakout_8: prior completed bar target 100%; next bar open simulation |
| v1 | momentum_26 AND reversion_12 | 9707.47 | -292.53 | sell /  / momentum_26 AND reversion_12: prior completed bar target 0%; next bar open simulation |
| v1 | momentum_26 + reversion_12 | 9655.94 | -344.06 | buy /  / momentum_26 + reversion_12: prior completed bar target 50%; next bar open simulation |
| v1 | momentum_26 AND volume_26 | 9916.79 | -83.21 | sell /  / momentum_26 AND volume_26: prior completed bar target 0%; next bar open simulation |
| v1 | momentum_26 + volume_26 | 9718.81 | -281.19 | buy /  / momentum_26 + volume_26: prior completed bar target 50%; next bar open simulation |
| v1 | breakout_8 AND reversion_12 | 10000.00 | 0.00 | 대기 /  / 새 신호 대기 |
| v1 | breakout_8 + reversion_12 | 9711.38 | -288.62 | sell /  / breakout_8 + reversion_12: prior completed bar target 50%; next bar open simulation |
| v1 | breakout_8 AND volume_26 | 9953.19 | -46.81 | sell /  / breakout_8 AND volume_26: prior completed bar target 0%; next bar open simulation |
| v1 | breakout_8 + volume_26 | 9774.28 | -225.72 | sell /  / breakout_8 + volume_26: prior completed bar target 50%; next bar open simulation |
| v1 | reversion_12 AND volume_26 | 9938.00 | -62.00 | sell /  / reversion_12 AND volume_26: prior completed bar target 0%; next bar open simulation |
| v1 | reversion_12 + volume_26 | 9748.10 | -251.90 | sell /  / reversion_12 + volume_26: prior completed bar target 0%; next bar open simulation |
| v1 | ema_12_26 | 9640.78 | -359.22 | buy /  / EMA12 > EMA26; 조건 충족; EMA12=532.174, EMA26=532.153 |
| v1 | macd_12_26_9 | 9815.17 | -184.83 | buy /  / MACD > 신호선 그리고 MACD > 0; 조건 충족; MACD=0.0204291, signal9=-0.229841 |
| v1 | rsi_14_recovery | 9957.14 | -42.86 | sell /  / 직전 RSI14 < 30, 현재 RSI14 >= 30 (한 봉 목표); 조건 미충족; RSI14=45.5102, previous_RSI14=37.5844 |
| v1 | bollinger_20_reentry | 9854.81 | -145.19 | sell /  / 직전 종가 < 직전 하단밴드, 현재 하단밴드 <= 종가 <= SMA20 (한 봉 목표); 조건 미충족; close=531.675, lower20=529.239, SMA20=533.058, previous_lower20=529.387 |
| v1 | donchian_20 | 9912.16 | -87.84 | sell /  / 종가 > 현재 봉을 제외한 직전 20봉 최고가; 조건 미충족; close=534.52, prior_high20=535.44 |
| v1 | atr_14_breakout | 9915.10 | -84.90 | sell /  / 종가 > 직전 종가 + 직전 ATR14 그리고 종가 > EMA26; 조건 미충족; close=533.975, threshold=536.307, prior_ATR14=2.16203, EMA26=530.521 |
| v1 | session_vwap | 9908.13 | -91.87 | buy /  / 종가 > 뉴욕 거래일별 누적 전형가격 VWAP; 조건 충족; close=529.315, session_VWAP=528.789, session_volume=2.32763e+06 |
| v1 | obv_20 | 9777.40 | -222.60 | buy /  / OBV > OBV의 SMA20 그리고 종가 > EMA26; 조건 충족; OBV=9.21792e+07, OBV_SMA20=9.21309e+07, close=531.98, EMA26=531.962 |
| v1 | stochastic_14_3_recovery | 9789.03 | -210.97 | sell /  / 직전 %K14 < 20에서 %K14가 %D3 상향 돌파 (한 봉 목표); 조건 미충족; K14=60.6262, D3=34.5689, previous_K14=38.87, previous_D3=26.948 |
| v1 | mfi_14_recovery | 9972.58 | -27.42 | sell /  / 직전 MFI14 < 20, 현재 MFI14 >= 20 (한 봉 목표); 조건 미충족; MFI14=53.413, previous_MFI14=44.3372 |
| v1 | adx_14_trend | 9883.62 | -116.38 | sell /  / Wilder ADX14 >= 25 그리고 +DI14 > -DI14; 조건 미충족; ADX14=23.6824, plus_DI14=22.3066, minus_DI14=19.9214 |
| v1 | aroon_25_trend | 9812.47 | -187.53 | sell /  / Aroon25 Up > 70 그리고 Down < 30 (동률이면 최신 극값); 조건 미충족; Aroon_up=68, Aroon_down=20 |
| v1 | cci_20_momentum | 10012.15 | 12.15 | sell /  / CCI20 > 100 (전형가격·평균절대편차); 조건 미충족; CCI20=86.441 |
| v1 | williams_14_recovery | 9819.22 | -180.78 | sell /  / 직전 Williams %R14 < -80, 현재 >= -80 (한 봉 목표); 조건 미충족; Williams_R14=-39.3738, previous_R14=-61.13 |
| v1 | cmf_20_accumulation | 9741.38 | -258.62 | sell /  / Chaikin Money Flow20 > 0.1; 조건 미충족; CMF20=0.0660116, volume20=2.44678e+07 |
| v1 | chaikin_3_10 | 9767.12 | -232.88 | buy /  / ADL의 EMA3 - EMA10 > 0 그리고 종가 > EMA26; 조건 충족; Chaikin3_10=276696, ADL=1.10993e+08, close=531.98, EMA26=531.962 |
| v1 | roc_10_momentum | 9959.43 | -40.57 | sell /  / 10봉 ROC > 1% 그리고 종가 > EMA26; 조건 미충족; ROC10_percent=0.454191, close=534.125, EMA26=532.186 |
| v1 | trix_15_trend | 9712.42 | -287.58 | sell /  / 15봉 삼중 EMA의 1봉 변화율 TRIX > 0 그리고 종가 > EMA26; 조건 미충족; TRIX15_percent=0.0172213, close=526.676, EMA26=532.897 |
| v1 | keltner_20_breakout | 9958.78 | -41.22 | sell /  / 종가 > EMA20 + 2 x Wilder ATR14; 조건 미충족; close=533.975, upper_Keltner=534.357, EMA20=530.111, ATR14=2.12332 |
| v1 | opening_range_30m | 9711.79 | -288.21 | sell /  / 뉴욕 09:30·09:45 두 완료 봉 최고가를 10:00 이후 종가가 돌파; 자료 부족·변동폭 또는 거래량 없음: 대기; close=526.676 |
| v2 | cash | 10000.00 | 0.00 | 대기 /  / 새 신호 대기 |
| v2 | buy_hold | 9894.65 | -105.35 | buy / partial / 직전 완료 봉 목표 비중 100%; 다음 봉 시가 가정 |
| v2 | trend_8_26 | 9613.14 | -386.86 | sell / filled / 직전 완료 봉 목표 비중 0%; 다음 봉 시가 가정 |
| v2 | momentum_26 | 9669.68 | -330.32 | buy / partial / 직전 완료 봉 목표 비중 100%; 다음 봉 시가 가정 |
| v2 | breakout_8 | 9488.19 | -511.81 | buy / partial / 직전 완료 봉 목표 비중 100%; 다음 봉 시가 가정 |
| v2 | reversion_12 | 9308.50 | -691.50 | sell / filled / 직전 완료 봉 목표 비중 0%; 다음 봉 시가 가정 |
| v2 | volume_26 | 9498.13 | -501.87 | sell / filled / 직전 완료 봉 목표 비중 0%; 다음 봉 시가 가정 |
| v2 | trend_8_26 AND momentum_26 | 9560.49 | -439.51 | sell / filled / 직전 완료 봉 목표 비중 0%; 다음 봉 시가 가정 |
| v2 | trend_8_26 + momentum_26 | 9641.62 | -358.38 | buy / filled / 직전 완료 봉 목표 비중 50%; 다음 봉 시가 가정 |
| v2 | trend_8_26 AND breakout_8 | 9458.32 | -541.68 | sell / filled / 직전 완료 봉 목표 비중 0%; 다음 봉 시가 가정 |
| v2 | trend_8_26 + breakout_8 | 9591.12 | -408.88 | sell / filled / 직전 완료 봉 목표 비중 50%; 다음 봉 시가 가정 |
| v2 | trend_8_26 AND reversion_12 | 9618.75 | -381.25 | sell / filled / 직전 완료 봉 목표 비중 0%; 다음 봉 시가 가정 |
| v2 | trend_8_26 + reversion_12 | 9459.23 | -540.77 | sell / filled / 직전 완료 봉 목표 비중 0%; 다음 봉 시가 가정 |
| v2 | trend_8_26 AND volume_26 | 9861.94 | -138.06 | sell / filled / 직전 완료 봉 목표 비중 0%; 다음 봉 시가 가정 |
| v2 | trend_8_26 + volume_26 | 9575.59 | -424.41 | sell / filled / 직전 완료 봉 목표 비중 0%; 다음 봉 시가 가정 |
| v2 | momentum_26 AND breakout_8 | 9587.47 | -412.53 | buy / partial / 직전 완료 봉 목표 비중 100%; 다음 봉 시가 가정 |
| v2 | momentum_26 + breakout_8 | 9578.86 | -421.14 | buy / partial / 직전 완료 봉 목표 비중 100%; 다음 봉 시가 가정 |
| v2 | momentum_26 AND reversion_12 | 9533.70 | -466.30 | sell / filled / 직전 완료 봉 목표 비중 0%; 다음 봉 시가 가정 |
| v2 | momentum_26 + reversion_12 | 9487.12 | -512.88 | buy / filled / 직전 완료 봉 목표 비중 50%; 다음 봉 시가 가정 |
| v2 | momentum_26 AND volume_26 | 9785.21 | -214.79 | sell / filled / 직전 완료 봉 목표 비중 0%; 다음 봉 시가 가정 |
| v2 | momentum_26 + volume_26 | 9603.83 | -396.17 | buy / filled / 직전 완료 봉 목표 비중 50%; 다음 봉 시가 가정 |
| v2 | breakout_8 AND reversion_12 | 10000.00 | 0.00 | 대기 /  / 새 신호 대기 |
| v2 | breakout_8 + reversion_12 | 9437.15 | -562.85 | sell / filled / 직전 완료 봉 목표 비중 50%; 다음 봉 시가 가정 |
| v2 | breakout_8 AND volume_26 | 9890.09 | -109.91 | sell / filled / 직전 완료 봉 목표 비중 0%; 다음 봉 시가 가정 |
| v2 | breakout_8 + volume_26 | 9532.99 | -467.01 | sell / filled / 직전 완료 봉 목표 비중 50%; 다음 봉 시가 가정 |
| v2 | reversion_12 AND volume_26 | 9699.57 | -300.43 | sell / filled / 직전 완료 봉 목표 비중 0%; 다음 봉 시가 가정 |
| v2 | reversion_12 + volume_26 | 9402.66 | -597.34 | sell / filled / 직전 완료 봉 목표 비중 0%; 다음 봉 시가 가정 |
| v2 | ema_12_26 | 9635.96 | -364.04 | buy / partial / EMA12 > EMA26; 조건 충족; EMA12=532.174, EMA26=532.153; 직전 완료 봉 목표를 다음 봉 시가에 모의 적용 |
| v2 | macd_12_26_9 | 9810.26 | -189.74 | buy / partial / MACD > 신호선 그리고 MACD > 0; 조건 충족; MACD=0.0204291, signal9=-0.229841; 직전 완료 봉 목표를 다음 봉 시가에 모의 적용 |
| v2 | rsi_14_recovery | 9951.17 | -48.83 | sell / filled / 직전 RSI14 < 30, 현재 RSI14 >= 30 (한 봉 목표); 조건 미충족; RSI14=45.5102, previous_RSI14=37.5844; 직전 완료 봉 목표를 다음 봉 시가에 모의 적용 |
| v2 | bollinger_20_reentry | 9848.90 | -151.10 | sell / filled / 직전 종가 < 직전 하단밴드, 현재 하단밴드 <= 종가 <= SMA20 (한 봉 목표); 조건 미충족; close=531.675, lower20=529.239, SMA20=533.058, previous_lower20=529.387; 직전 완료 봉 목표를 다음 봉 시가에 모의 적용 |
| v2 | donchian_20 | 9908.19 | -91.81 | sell / filled / 종가 > 현재 봉을 제외한 직전 20봉 최고가; 조건 미충족; close=534.52, prior_high20=535.44; 직전 완료 봉 목표를 다음 봉 시가에 모의 적용 |
| v2 | atr_14_breakout | 9911.14 | -88.86 | sell / filled / 종가 > 직전 종가 + 직전 ATR14 그리고 종가 > EMA26; 조건 미충족; close=533.975, threshold=536.307, prior_ATR14=2.16203, EMA26=530.521; 직전 완료 봉 목표를 다음 봉 시가에 모의 적용 |
| v2 | session_vwap | 9901.20 | -98.80 | buy / partial / 종가 > 뉴욕 거래일별 누적 전형가격 VWAP; 조건 충족; close=529.315, session_VWAP=528.789, session_volume=2.32763e+06; 직전 완료 봉 목표를 다음 봉 시가에 모의 적용 |
| v2 | obv_20 | 9768.61 | -231.39 | buy / partial / OBV > OBV의 SMA20 그리고 종가 > EMA26; 조건 충족; OBV=9.21792e+07, OBV_SMA20=9.21309e+07, close=531.98, EMA26=531.962; 직전 완료 봉 목표를 다음 봉 시가에 모의 적용 |
| v2 | stochastic_14_3_recovery | 9779.25 | -220.75 | sell / filled / 직전 %K14 < 20에서 %K14가 %D3 상향 돌파 (한 봉 목표); 조건 미충족; K14=60.6262, D3=34.5689, previous_K14=38.87, previous_D3=26.948; 직전 완료 봉 목표를 다음 봉 시가에 모의 적용 |
| v2 | mfi_14_recovery | 9968.59 | -31.41 | sell / filled / 직전 MFI14 < 20, 현재 MFI14 >= 20 (한 봉 목표); 조건 미충족; MFI14=53.413, previous_MFI14=44.3372; 직전 완료 봉 목표를 다음 봉 시가에 모의 적용 |
| v2 | adx_14_trend | 9879.67 | -120.33 | sell / filled / Wilder ADX14 >= 25 그리고 +DI14 > -DI14; 조건 미충족; ADX14=23.6824, plus_DI14=22.3066, minus_DI14=19.9214; 직전 완료 봉 목표를 다음 봉 시가에 모의 적용 |
| v2 | aroon_25_trend | 9808.55 | -191.45 | sell / filled / Aroon25 Up > 70 그리고 Down < 30 (동률이면 최신 극값); 조건 미충족; Aroon_up=68, Aroon_down=20; 직전 완료 봉 목표를 다음 봉 시가에 모의 적용 |
| v2 | cci_20_momentum | 10010.15 | 10.15 | sell / filled / CCI20 > 100 (전형가격·평균절대편차); 조건 미충족; CCI20=86.441; 직전 완료 봉 목표를 다음 봉 시가에 모의 적용 |
| v2 | williams_14_recovery | 9811.37 | -188.63 | sell / filled / 직전 Williams %R14 < -80, 현재 >= -80 (한 봉 목표); 조건 미충족; Williams_R14=-39.3738, previous_R14=-61.13; 직전 완료 봉 목표를 다음 봉 시가에 모의 적용 |
| v2 | cmf_20_accumulation | 9737.48 | -262.52 | sell / filled / Chaikin Money Flow20 > 0.1; 조건 미충족; CMF20=0.0660116, volume20=2.44678e+07; 직전 완료 봉 목표를 다음 봉 시가에 모의 적용 |
| v2 | chaikin_3_10 | 9758.33 | -241.67 | buy / partial / ADL의 EMA3 - EMA10 > 0 그리고 종가 > EMA26; 조건 충족; Chaikin3_10=276696, ADL=1.10993e+08, close=531.98, EMA26=531.962; 직전 완료 봉 목표를 다음 봉 시가에 모의 적용 |
| v2 | roc_10_momentum | 9957.44 | -42.56 | sell / filled / 10봉 ROC > 1% 그리고 종가 > EMA26; 조건 미충족; ROC10_percent=0.454191, close=534.125, EMA26=532.186; 직전 완료 봉 목표를 다음 봉 시가에 모의 적용 |
| v2 | trix_15_trend | 9708.54 | -291.46 | sell / filled / 15봉 삼중 EMA의 1봉 변화율 TRIX > 0 그리고 종가 > EMA26; 조건 미충족; TRIX15_percent=0.0172213, close=526.676, EMA26=532.897; 직전 완료 봉 목표를 다음 봉 시가에 모의 적용 |
| v2 | keltner_20_breakout | 9956.78 | -43.22 | sell / filled / 종가 > EMA20 + 2 x Wilder ATR14; 조건 미충족; close=533.975, upper_Keltner=534.357, EMA20=530.111, ATR14=2.12332; 직전 완료 봉 목표를 다음 봉 시가에 모의 적용 |
| v2 | opening_range_30m | 9707.90 | -292.10 | sell / filled / 뉴욕 09:30·09:45 두 완료 봉 최고가를 10:00 이후 종가가 돌파; 자료 부족·변동폭 또는 거래량 없음: 대기; close=526.676; 직전 완료 봉 목표를 다음 봉 시가에 모의 적용 |

### 같은 기간의 비용·노출 비교 (사후 연구)

| 전략 | 비용 전 | 비용 후 | 100% 보유 | 같은 평균 노출 보유 | 평균 노출 |
|---|---:|---:|---:|---:|---:|
| cash | 0.00% | 0.00% | 4.01% | 0.00% | 0.00% |
| buy_hold | 4.45% | 4.01% | 4.01% | 4.01% | 100.00% |
| trend_8_26 | 1.22% | -2.12% | 4.01% | 2.34% | 59.32% |
| momentum_26 | 0.18% | -5.14% | 4.01% | 2.41% | 60.89% |
| breakout_8 | 6.49% | -8.84% | 4.01% | 0.81% | 20.73% |
| reversion_12 | -4.30% | -12.75% | 4.01% | 0.93% | 23.88% |
| volume_26 | 1.03% | -7.11% | 4.01% | 0.33% | 8.40% |
| trend_8_26 AND momentum_26 | -0.87% | -6.14% | 4.01% | 2.18% | 55.12% |
| trend_8_26 + momentum_26 | 0.71% | -3.63% | 4.01% | 2.38% | 60.11% |
| trend_8_26 AND breakout_8 | 0.70% | -10.09% | 4.01% | 0.52% | 13.39% |
| trend_8_26 + breakout_8 | 3.84% | -4.93% | 4.01% | 1.57% | 40.03% |
| trend_8_26 AND reversion_12 | -1.41% | -7.04% | 4.01% | 0.26% | 6.82% |
| trend_8_26 + reversion_12 | -1.56% | -7.40% | 4.01% | 1.63% | 41.61% |
| trend_8_26 AND volume_26 | 3.42% | -0.42% | 4.01% | 0.12% | 3.15% |
| trend_8_26 + volume_26 | 1.14% | -4.05% | 4.01% | 1.33% | 33.86% |
| momentum_26 AND breakout_8 | 2.96% | -8.47% | 4.01% | 0.53% | 13.65% |
| momentum_26 + breakout_8 | 3.30% | -6.61% | 4.01% | 1.60% | 40.82% |
| momentum_26 AND reversion_12 | -2.41% | -9.14% | 4.01% | 0.38% | 9.71% |
| momentum_26 + reversion_12 | -2.07% | -9.03% | 4.01% | 1.67% | 42.39% |
| momentum_26 AND volume_26 | 1.07% | -3.49% | 4.01% | 0.14% | 3.67% |
| momentum_26 + volume_26 | 0.62% | -5.54% | 4.01% | 1.36% | 34.65% |
| breakout_8 AND reversion_12 | 0.00% | 0.00% | 4.01% | 0.00% | 0.00% |
| breakout_8 + reversion_12 | 0.97% | -10.06% | 4.01% | 0.87% | 22.32% |
| breakout_8 AND volume_26 | 2.04% | -0.50% | 4.01% | 0.07% | 1.84% |
| breakout_8 + volume_26 | 3.73% | -7.00% | 4.01% | 0.57% | 14.57% |
| reversion_12 AND volume_26 | -2.90% | -6.11% | 4.01% | 0.13% | 3.41% |
| reversion_12 + volume_26 | -1.66% | -9.97% | 4.01% | 0.63% | 16.15% |
| ema_12_26 | 0.32% | -3.40% | 4.01% | 2.44% | 61.68% |
| macd_12_26_9 | 1.29% | -4.10% | 4.01% | 1.36% | 34.65% |
| rsi_14_recovery | 0.31% | -2.19% | 4.01% | 0.06% | 1.57% |
| bollinger_20_reentry | -0.92% | -3.79% | 4.01% | 0.07% | 1.84% |
| donchian_20 | 1.76% | -4.05% | 4.01% | 0.19% | 4.99% |
| atr_14_breakout | 1.72% | -3.69% | 4.01% | 0.14% | 3.67% |
| session_vwap | 7.38% | -0.85% | 4.01% | 1.65% | 41.99% |
| obv_20 | 5.83% | -2.28% | 4.01% | 1.91% | 48.56% |
| stochastic_14_3_recovery | -0.50% | -10.42% | 4.01% | 0.25% | 6.56% |
| mfi_14_recovery | 1.58% | -2.19% | 4.01% | 0.09% | 2.36% |
| adx_14_trend | 3.84% | 1.26% | 4.01% | 1.83% | 46.46% |
| aroon_25_trend | 0.07% | -4.85% | 4.01% | 0.89% | 22.83% |
| cci_20_momentum | 3.43% | -2.89% | 4.01% | 0.86% | 22.05% |
| williams_14_recovery | -1.26% | -9.97% | 4.01% | 0.22% | 5.77% |
| cmf_20_accumulation | 0.70% | -4.65% | 4.01% | 1.28% | 32.81% |
| chaikin_3_10 | 4.62% | -3.41% | 4.01% | 1.82% | 46.19% |
| roc_10_momentum | -0.01% | -4.12% | 4.01% | 0.61% | 15.75% |
| trix_15_trend | -0.85% | -4.93% | 4.01% | 1.96% | 49.87% |
| keltner_20_breakout | 1.11% | -4.26% | 4.01% | 0.53% | 13.65% |
| opening_range_30m | -1.09% | -4.36% | 4.01% | 0.87% | 22.31% |

동일 구간·초기 자금, 종료 시 청산 비용 포함. 노출 맞춤은 사후 설명용이며 v2 실제 계좌 성과가 아닙니다.
[낙폭 분해·비용 영향·전체 구간](MSFT/comparison.json)

[v1 전체 기록](MSFT/accounts.json) · [v2 전체 기록](MSFT/accounts-v2.json)

## JPM 계좌

| 모델 | 전략 | 평가액 USD | 손익 USD | 최근 매매·이유 |
|---|---|---:|---:|---|
| v1 | cash | 10000.00 | 0.00 | 대기 /  / 새 신호 대기 |
| v1 | buy_hold | 9850.85 | -149.15 | buy /  / buy_hold: prior completed bar target 100%; next bar open simulation |
| v1 | trend_8_26 | 9786.16 | -213.84 | sell /  / trend_8_26: prior completed bar target 0%; next bar open simulation |
| v1 | momentum_26 | 9706.33 | -293.67 | sell /  / momentum_26: prior completed bar target 0%; next bar open simulation |
| v1 | breakout_8 | 9759.46 | -240.54 | sell /  / breakout_8: prior completed bar target 0%; next bar open simulation |
| v1 | reversion_12 | 9720.30 | -279.70 | sell /  / reversion_12: prior completed bar target 0%; next bar open simulation |
| v1 | volume_26 | 9961.97 | -38.03 | sell /  / volume_26: prior completed bar target 0%; next bar open simulation |
| v1 | trend_8_26 AND momentum_26 | 9793.49 | -206.51 | sell /  / trend_8_26 AND momentum_26: prior completed bar target 0%; next bar open simulation |
| v1 | trend_8_26 + momentum_26 | 9746.16 | -253.84 | sell /  / trend_8_26 + momentum_26: prior completed bar target 0%; next bar open simulation |
| v1 | trend_8_26 AND breakout_8 | 9915.55 | -84.45 | sell /  / trend_8_26 AND breakout_8: prior completed bar target 0%; next bar open simulation |
| v1 | trend_8_26 + breakout_8 | 9792.38 | -207.62 | sell /  / trend_8_26 + breakout_8: prior completed bar target 0%; next bar open simulation |
| v1 | trend_8_26 AND reversion_12 | 9855.61 | -144.39 | sell /  / trend_8_26 AND reversion_12: prior completed bar target 0%; next bar open simulation |
| v1 | trend_8_26 + reversion_12 | 9753.08 | -246.92 | sell /  / trend_8_26 + reversion_12: prior completed bar target 0%; next bar open simulation |
| v1 | trend_8_26 AND volume_26 | 10035.68 | 35.68 | sell /  / trend_8_26 AND volume_26: prior completed bar target 0%; next bar open simulation |
| v1 | trend_8_26 + volume_26 | 9873.52 | -126.48 | sell /  / trend_8_26 + volume_26: prior completed bar target 0%; next bar open simulation |
| v1 | momentum_26 AND breakout_8 | 9733.77 | -266.23 | sell /  / momentum_26 AND breakout_8: prior completed bar target 0%; next bar open simulation |
| v1 | momentum_26 + breakout_8 | 9732.95 | -267.05 | sell /  / momentum_26 + breakout_8: prior completed bar target 0%; next bar open simulation |
| v1 | momentum_26 AND reversion_12 | 9881.87 | -118.13 | sell /  / momentum_26 AND reversion_12: prior completed bar target 0%; next bar open simulation |
| v1 | momentum_26 + reversion_12 | 9752.18 | -247.82 | sell /  / momentum_26 + reversion_12: prior completed bar target 0%; next bar open simulation |
| v1 | momentum_26 AND volume_26 | 10035.68 | 35.68 | sell /  / momentum_26 AND volume_26: prior completed bar target 0%; next bar open simulation |
| v1 | momentum_26 + volume_26 | 9852.93 | -147.07 | sell /  / momentum_26 + volume_26: prior completed bar target 0%; next bar open simulation |
| v1 | breakout_8 AND reversion_12 | 10000.00 | 0.00 | 대기 /  / 새 신호 대기 |
| v1 | breakout_8 + reversion_12 | 9778.79 | -221.21 | sell /  / breakout_8 + reversion_12: prior completed bar target 0%; next bar open simulation |
| v1 | breakout_8 AND volume_26 | 10022.00 | 22.00 | sell /  / breakout_8 AND volume_26: prior completed bar target 0%; next bar open simulation |
| v1 | breakout_8 + volume_26 | 9860.16 | -139.84 | sell /  / breakout_8 + volume_26: prior completed bar target 0%; next bar open simulation |
| v1 | reversion_12 AND volume_26 | 9940.10 | -59.90 | sell /  / reversion_12 AND volume_26: prior completed bar target 0%; next bar open simulation |
| v1 | reversion_12 + volume_26 | 9860.00 | -140.00 | sell /  / reversion_12 + volume_26: prior completed bar target 0%; next bar open simulation |
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
| v1 | cmf_20_accumulation | 9863.93 | -136.07 | buy /  / Chaikin Money Flow20 > 0.1; 조건 충족; CMF20=0.100434, volume20=3.98791e+06 |
| v1 | chaikin_3_10 | 9837.22 | -162.78 | sell /  / ADL의 EMA3 - EMA10 > 0 그리고 종가 > EMA26; 조건 미충족; Chaikin3_10=7273.89, ADL=-1.28498e+07, close=336.08, EMA26=336.65 |
| v1 | roc_10_momentum | 9836.40 | -163.60 | sell /  / 10봉 ROC > 1% 그리고 종가 > EMA26; 조건 미충족; ROC10_percent=0.964142, close=337.72, EMA26=336.695 |
| v1 | trix_15_trend | 9723.73 | -276.27 | sell /  / 15봉 삼중 EMA의 1봉 변화율 TRIX > 0 그리고 종가 > EMA26; 조건 미충족; TRIX15_percent=0.0135144, close=337.6, EMA26=338.759 |
| v1 | keltner_20_breakout | 9905.24 | -94.76 | sell /  / 종가 > EMA20 + 2 x Wilder ATR14; 조건 미충족; close=339.04, upper_Keltner=339.281, EMA20=336.559, ATR14=1.36146 |
| v1 | opening_range_30m | 9850.26 | -149.74 | sell /  / 뉴욕 09:30·09:45 두 완료 봉 최고가를 10:00 이후 종가가 돌파; 조건 미충족; close=337.72, opening_high=339.035 |
| v2 | cash | 10000.00 | 0.00 | 대기 /  / 새 신호 대기 |
| v2 | buy_hold | 10015.45 | 15.45 | buy / partial / 직전 완료 봉 목표 비중 100%; 다음 봉 시가 가정 |
| v2 | trend_8_26 | 9791.24 | -208.76 | sell / filled / 직전 완료 봉 목표 비중 0%; 다음 봉 시가 가정 |
| v2 | momentum_26 | 9219.07 | -780.93 | sell / filled / 직전 완료 봉 목표 비중 0%; 다음 봉 시가 가정 |
| v2 | breakout_8 | 9100.10 | -899.90 | sell / filled / 직전 완료 봉 목표 비중 0%; 다음 봉 시가 가정 |
| v2 | reversion_12 | 9695.03 | -304.97 | sell / filled / 직전 완료 봉 목표 비중 0%; 다음 봉 시가 가정 |
| v2 | volume_26 | 9781.50 | -218.50 | sell / filled / 직전 완료 봉 목표 비중 0%; 다음 봉 시가 가정 |
| v2 | trend_8_26 AND momentum_26 | 9756.41 | -243.59 | sell / filled / 직전 완료 봉 목표 비중 0%; 다음 봉 시가 가정 |
| v2 | trend_8_26 + momentum_26 | 9521.33 | -478.67 | sell / filled / 직전 완료 봉 목표 비중 0%; 다음 봉 시가 가정 |
| v2 | trend_8_26 AND breakout_8 | 9287.76 | -712.24 | sell / filled / 직전 완료 봉 목표 비중 0%; 다음 봉 시가 가정 |
| v2 | trend_8_26 + breakout_8 | 9460.24 | -539.76 | sell / filled / 직전 완료 봉 목표 비중 0%; 다음 봉 시가 가정 |
| v2 | trend_8_26 AND reversion_12 | 9831.59 | -168.41 | sell / filled / 직전 완료 봉 목표 비중 0%; 다음 봉 시가 가정 |
| v2 | trend_8_26 + reversion_12 | 9784.13 | -215.87 | sell / filled / 직전 완료 봉 목표 비중 0%; 다음 봉 시가 가정 |
| v2 | trend_8_26 AND volume_26 | 9833.30 | -166.70 | sell / filled / 직전 완료 봉 목표 비중 0%; 다음 봉 시가 가정 |
| v2 | trend_8_26 + volume_26 | 9787.03 | -212.97 | sell / filled / 직전 완료 봉 목표 비중 0%; 다음 봉 시가 가정 |
| v2 | momentum_26 AND breakout_8 | 9058.00 | -942.00 | sell / filled / 직전 완료 봉 목표 비중 0%; 다음 봉 시가 가정 |
| v2 | momentum_26 + breakout_8 | 9180.31 | -819.69 | sell / filled / 직전 완료 봉 목표 비중 0%; 다음 봉 시가 가정 |
| v2 | momentum_26 AND reversion_12 | 9827.31 | -172.69 | sell / filled / 직전 완료 봉 목표 비중 0%; 다음 봉 시가 가정 |
| v2 | momentum_26 + reversion_12 | 9614.70 | -385.30 | sell / filled / 직전 완료 봉 목표 비중 0%; 다음 봉 시가 가정 |
| v2 | momentum_26 AND volume_26 | 9833.30 | -166.70 | sell / filled / 직전 완료 봉 목표 비중 0%; 다음 봉 시가 가정 |
| v2 | momentum_26 + volume_26 | 9577.38 | -422.62 | sell / filled / 직전 완료 봉 목표 비중 0%; 다음 봉 시가 가정 |
| v2 | breakout_8 AND reversion_12 | 10000.00 | 0.00 | 대기 /  / 새 신호 대기 |
| v2 | breakout_8 + reversion_12 | 9472.20 | -527.80 | sell / filled / 직전 완료 봉 목표 비중 0%; 다음 봉 시가 가정 |
| v2 | breakout_8 AND volume_26 | 9911.14 | -88.86 | sell / filled / 직전 완료 봉 목표 비중 0%; 다음 봉 시가 가정 |
| v2 | breakout_8 + volume_26 | 9454.59 | -545.41 | sell / filled / 직전 완료 봉 목표 비중 0%; 다음 봉 시가 가정 |
| v2 | reversion_12 AND volume_26 | 9987.18 | -12.82 | sell / filled / 직전 완료 봉 목표 비중 0%; 다음 봉 시가 가정 |
| v2 | reversion_12 + volume_26 | 9779.33 | -220.67 | sell / filled / 직전 완료 봉 목표 비중 0%; 다음 봉 시가 가정 |
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
| v2 | cmf_20_accumulation | 9859.00 | -141.00 | buy / partial / Chaikin Money Flow20 > 0.1; 조건 충족; CMF20=0.100434, volume20=3.98791e+06; 직전 완료 봉 목표를 다음 봉 시가에 모의 적용 |
| v2 | chaikin_3_10 | 9831.32 | -168.68 | sell / filled / ADL의 EMA3 - EMA10 > 0 그리고 종가 > EMA26; 조건 미충족; Chaikin3_10=7273.89, ADL=-1.28498e+07, close=336.08, EMA26=336.65; 직전 완료 봉 목표를 다음 봉 시가에 모의 적용 |
| v2 | roc_10_momentum | 9832.47 | -167.53 | sell / filled / 10봉 ROC > 1% 그리고 종가 > EMA26; 조건 미충족; ROC10_percent=0.964142, close=337.72, EMA26=336.695; 직전 완료 봉 목표를 다음 봉 시가에 모의 적용 |
| v2 | trix_15_trend | 9715.96 | -284.04 | sell / filled / 15봉 삼중 EMA의 1봉 변화율 TRIX > 0 그리고 종가 > EMA26; 조건 미충족; TRIX15_percent=0.0135144, close=337.6, EMA26=338.759; 직전 완료 봉 목표를 다음 봉 시가에 모의 적용 |
| v2 | keltner_20_breakout | 9901.28 | -98.72 | sell / filled / 종가 > EMA20 + 2 x Wilder ATR14; 조건 미충족; close=339.04, upper_Keltner=339.281, EMA20=336.559, ATR14=1.36146; 직전 완료 봉 목표를 다음 봉 시가에 모의 적용 |
| v2 | opening_range_30m | 9846.33 | -153.67 | sell / filled / 뉴욕 09:30·09:45 두 완료 봉 최고가를 10:00 이후 종가가 돌파; 조건 미충족; close=337.72, opening_high=339.035; 직전 완료 봉 목표를 다음 봉 시가에 모의 적용 |

### 같은 기간의 비용·노출 비교 (사후 연구)

| 전략 | 비용 전 | 비용 후 | 100% 보유 | 같은 평균 노출 보유 | 평균 노출 |
|---|---:|---:|---:|---:|---:|
| cash | 0.00% | 0.00% | -0.23% | -0.00% | 0.00% |
| buy_hold | 0.19% | -0.23% | -0.23% | -0.23% | 100.00% |
| trend_8_26 | 0.33% | -3.80% | -0.23% | -0.13% | 53.81% |
| momentum_26 | -3.06% | -10.12% | -0.23% | -0.12% | 49.61% |
| breakout_8 | -2.73% | -17.43% | -0.23% | -0.05% | 19.69% |
| reversion_12 | 5.19% | -9.57% | -0.23% | -0.06% | 26.77% |
| volume_26 | 0.25% | -6.27% | -0.23% | -0.02% | 7.09% |
| trend_8_26 AND momentum_26 | 0.56% | -4.38% | -0.23% | -0.10% | 41.21% |
| trend_8_26 + momentum_26 | -1.37% | -6.81% | -0.23% | -0.12% | 51.71% |
| trend_8_26 AND breakout_8 | -3.21% | -13.22% | -0.23% | -0.03% | 12.07% |
| trend_8_26 + breakout_8 | -1.19% | -10.49% | -0.23% | -0.09% | 36.75% |
| trend_8_26 AND reversion_12 | 2.62% | -4.05% | -0.23% | -0.02% | 8.40% |
| trend_8_26 + reversion_12 | 2.75% | -6.14% | -0.23% | -0.09% | 40.29% |
| trend_8_26 AND volume_26 | -0.42% | -4.11% | -0.23% | -0.01% | 3.94% |
| trend_8_26 + volume_26 | 0.31% | -5.04% | -0.23% | -0.07% | 30.45% |
| momentum_26 AND breakout_8 | -2.68% | -13.84% | -0.23% | -0.03% | 12.60% |
| momentum_26 + breakout_8 | -2.87% | -13.65% | -0.23% | -0.08% | 34.65% |
| momentum_26 AND reversion_12 | 2.79% | -4.29% | -0.23% | -0.02% | 6.82% |
| momentum_26 + reversion_12 | 1.01% | -8.12% | -0.23% | -0.09% | 38.19% |
| momentum_26 AND volume_26 | 0.21% | -2.70% | -0.23% | -0.01% | 2.89% |
| momentum_26 + volume_26 | -1.39% | -7.82% | -0.23% | -0.07% | 28.35% |
| breakout_8 AND reversion_12 | 0.00% | 0.00% | -0.23% | -0.00% | 0.00% |
| breakout_8 + reversion_12 | 1.18% | -12.31% | -0.23% | -0.05% | 23.24% |
| breakout_8 AND volume_26 | -0.25% | -2.32% | -0.23% | -0.00% | 1.31% |
| breakout_8 + volume_26 | -1.24% | -11.28% | -0.23% | -0.03% | 13.39% |
| reversion_12 AND volume_26 | 1.33% | -2.01% | -0.23% | -0.01% | 3.41% |
| reversion_12 + volume_26 | 2.70% | -6.96% | -0.23% | -0.04% | 16.93% |
| ema_12_26 | -0.24% | -3.54% | -0.23% | -0.12% | 51.97% |
| macd_12_26_9 | -0.13% | -4.64% | -0.23% | -0.08% | 32.81% |
| rsi_14_recovery | 0.47% | -2.03% | -0.23% | -0.00% | 1.57% |
| bollinger_20_reentry | 0.51% | -3.62% | -0.23% | -0.01% | 2.62% |
| donchian_20 | -1.81% | -5.05% | -0.23% | -0.01% | 3.15% |
| atr_14_breakout | -1.35% | -8.92% | -0.23% | -0.01% | 5.25% |
| session_vwap | 1.67% | -7.69% | -0.23% | -0.11% | 46.72% |
| obv_20 | -3.42% | -13.78% | -0.23% | -0.07% | 29.92% |
| stochastic_14_3_recovery | -1.37% | -11.94% | -0.23% | -0.02% | 7.09% |
| mfi_14_recovery | 0.32% | -2.18% | -0.23% | -0.00% | 1.57% |
| adx_14_trend | -2.43% | -4.85% | -0.23% | -0.07% | 29.66% |
| aroon_25_trend | -1.12% | -5.19% | -0.23% | -0.05% | 22.57% |
| cci_20_momentum | -2.84% | -10.67% | -0.23% | -0.04% | 16.27% |
| williams_14_recovery | -0.99% | -10.48% | -0.23% | -0.01% | 6.30% |
| cmf_20_accumulation | -1.83% | -10.49% | -0.23% | -0.07% | 29.13% |
| chaikin_3_10 | 1.01% | -7.52% | -0.23% | -0.08% | 33.86% |
| roc_10_momentum | -1.36% | -4.22% | -0.23% | -0.02% | 8.40% |
| trix_15_trend | -1.25% | -8.83% | -0.23% | -0.08% | 35.17% |
| keltner_20_breakout | -1.21% | -4.07% | -0.23% | -0.01% | 4.20% |
| opening_range_30m | -0.23% | -3.93% | -0.23% | -0.04% | 17.32% |

동일 구간·초기 자금, 종료 시 청산 비용 포함. 노출 맞춤은 사후 설명용이며 v2 실제 계좌 성과가 아닙니다.
[낙폭 분해·비용 영향·전체 구간](JPM/comparison.json)

[v1 전체 기록](JPM/accounts.json) · [v2 전체 기록](JPM/accounts-v2.json)

## XOM 계좌

| 모델 | 전략 | 평가액 USD | 손익 USD | 최근 매매·이유 |
|---|---|---:|---:|---|
| v1 | cash | 10000.00 | 0.00 | 대기 /  / 새 신호 대기 |
| v1 | buy_hold | 10019.33 | 19.33 | buy /  / buy_hold: prior completed bar target 100%; next bar open simulation |
| v1 | trend_8_26 | 9862.79 | -137.21 | sell /  / trend_8_26: prior completed bar target 0%; next bar open simulation |
| v1 | momentum_26 | 9934.85 | -65.15 | sell /  / momentum_26: prior completed bar target 0%; next bar open simulation |
| v1 | breakout_8 | 9723.09 | -276.91 | sell /  / breakout_8: prior completed bar target 0%; next bar open simulation |
| v1 | reversion_12 | 9657.92 | -342.08 | sell /  / reversion_12: prior completed bar target 0%; next bar open simulation |
| v1 | volume_26 | 9732.23 | -267.77 | sell /  / volume_26: prior completed bar target 0%; next bar open simulation |
| v1 | trend_8_26 AND momentum_26 | 9853.77 | -146.23 | sell /  / trend_8_26 AND momentum_26: prior completed bar target 0%; next bar open simulation |
| v1 | trend_8_26 + momentum_26 | 9898.87 | -101.13 | sell /  / trend_8_26 + momentum_26: prior completed bar target 0%; next bar open simulation |
| v1 | trend_8_26 AND breakout_8 | 9829.71 | -170.29 | sell /  / trend_8_26 AND breakout_8: prior completed bar target 0%; next bar open simulation |
| v1 | trend_8_26 + breakout_8 | 9812.71 | -187.29 | sell /  / trend_8_26 + breakout_8: prior completed bar target 0%; next bar open simulation |
| v1 | trend_8_26 AND reversion_12 | 9652.28 | -347.72 | sell /  / trend_8_26 AND reversion_12: prior completed bar target 0%; next bar open simulation |
| v1 | trend_8_26 + reversion_12 | 9759.79 | -240.21 | sell /  / trend_8_26 + reversion_12: prior completed bar target 0%; next bar open simulation |
| v1 | trend_8_26 AND volume_26 | 9849.16 | -150.84 | sell /  / trend_8_26 AND volume_26: prior completed bar target 0%; next bar open simulation |
| v1 | trend_8_26 + volume_26 | 9797.51 | -202.49 | sell /  / trend_8_26 + volume_26: prior completed bar target 0%; next bar open simulation |
| v1 | momentum_26 AND breakout_8 | 9801.24 | -198.76 | sell /  / momentum_26 AND breakout_8: prior completed bar target 0%; next bar open simulation |
| v1 | momentum_26 + breakout_8 | 9828.65 | -171.35 | sell /  / momentum_26 + breakout_8: prior completed bar target 0%; next bar open simulation |
| v1 | momentum_26 AND reversion_12 | 9766.58 | -233.42 | sell /  / momentum_26 AND reversion_12: prior completed bar target 0%; next bar open simulation |
| v1 | momentum_26 + reversion_12 | 9795.30 | -204.70 | sell /  / momentum_26 + reversion_12: prior completed bar target 0%; next bar open simulation |
| v1 | momentum_26 AND volume_26 | 9985.49 | -14.51 | sell /  / momentum_26 AND volume_26: prior completed bar target 0%; next bar open simulation |
| v1 | momentum_26 + volume_26 | 9833.06 | -166.94 | sell /  / momentum_26 + volume_26: prior completed bar target 0%; next bar open simulation |
| v1 | breakout_8 AND reversion_12 | 10000.00 | 0.00 | 대기 /  / 새 신호 대기 |
| v1 | breakout_8 + reversion_12 | 9690.42 | -309.58 | sell /  / breakout_8 + reversion_12: prior completed bar target 0%; next bar open simulation |
| v1 | breakout_8 AND volume_26 | 9950.44 | -49.56 | sell /  / breakout_8 AND volume_26: prior completed bar target 0%; next bar open simulation |
| v1 | breakout_8 + volume_26 | 9727.52 | -272.48 | sell /  / breakout_8 + volume_26: prior completed bar target 0%; next bar open simulation |
| v1 | reversion_12 AND volume_26 | 9840.91 | -159.09 | sell /  / reversion_12 AND volume_26: prior completed bar target 0%; next bar open simulation |
| v1 | reversion_12 + volume_26 | 9695.08 | -304.92 | sell /  / reversion_12 + volume_26: prior completed bar target 0%; next bar open simulation |
| v1 | ema_12_26 | 9973.99 | -26.01 | sell /  / EMA12 > EMA26; 조건 미충족; EMA12=177.968, EMA26=178.055 |
| v1 | macd_12_26_9 | 10064.24 | 64.24 | sell /  / MACD > 신호선 그리고 MACD > 0; 조건 미충족; MACD=0.288973, signal9=0.30355 |
| v1 | rsi_14_recovery | 9927.64 | -72.36 | sell /  / 직전 RSI14 < 30, 현재 RSI14 >= 30 (한 봉 목표); 조건 미충족; RSI14=37.639, previous_RSI14=31.1023 |
| v1 | bollinger_20_reentry | 9852.90 | -147.10 | sell /  / 직전 종가 < 직전 하단밴드, 현재 하단밴드 <= 종가 <= SMA20 (한 봉 목표); 조건 미충족; close=175.55, lower20=175.189, SMA20=177.794, previous_lower20=175.528 |
| v1 | donchian_20 | 9832.30 | -167.70 | sell /  / 종가 > 현재 봉을 제외한 직전 20봉 최고가; 조건 미충족; close=179.01, prior_high20=179.16 |
| v1 | atr_14_breakout | 9864.96 | -135.04 | sell /  / 종가 > 직전 종가 + 직전 ATR14 그리고 종가 > EMA26; 조건 미충족; close=177.19, threshold=177.748, prior_ATR14=0.663113, EMA26=175.734 |
| v1 | session_vwap | 9971.72 | -28.28 | buy /  / 종가 > 뉴욕 거래일별 누적 전형가격 VWAP; 조건 충족; close=176.885, session_VWAP=176.63, session_volume=5.45281e+06 |
| v1 | obv_20 | 9847.04 | -152.96 | sell /  / OBV > OBV의 SMA20 그리고 종가 > EMA26; 조건 미충족; OBV=1.99239e+07, OBV_SMA20=1.96226e+07, close=176.81, EMA26=177.054 |
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
| v2 | buy_hold | 10339.07 | 339.07 | buy / partial / 직전 완료 봉 목표 비중 100%; 다음 봉 시가 가정 |
| v2 | trend_8_26 | 9953.74 | -46.26 | sell / filled / 직전 완료 봉 목표 비중 0%; 다음 봉 시가 가정 |
| v2 | momentum_26 | 10102.33 | 102.33 | sell / filled / 직전 완료 봉 목표 비중 0%; 다음 봉 시가 가정 |
| v2 | breakout_8 | 9192.19 | -807.81 | sell / filled / 직전 완료 봉 목표 비중 0%; 다음 봉 시가 가정 |
| v2 | reversion_12 | 9475.52 | -524.48 | sell / filled / 직전 완료 봉 목표 비중 0%; 다음 봉 시가 가정 |
| v2 | volume_26 | 9635.02 | -364.98 | sell / filled / 직전 완료 봉 목표 비중 0%; 다음 봉 시가 가정 |
| v2 | trend_8_26 AND momentum_26 | 9950.02 | -49.98 | sell / filled / 직전 완료 봉 목표 비중 0%; 다음 봉 시가 가정 |
| v2 | trend_8_26 + momentum_26 | 10027.90 | 27.90 | sell / filled / 직전 완료 봉 목표 비중 0%; 다음 봉 시가 가정 |
| v2 | trend_8_26 AND breakout_8 | 9281.59 | -718.41 | sell / filled / 직전 완료 봉 목표 비중 0%; 다음 봉 시가 가정 |
| v2 | trend_8_26 + breakout_8 | 9606.41 | -393.59 | sell / filled / 직전 완료 봉 목표 비중 0%; 다음 봉 시가 가정 |
| v2 | trend_8_26 AND reversion_12 | 9493.76 | -506.24 | sell / filled / 직전 완료 봉 목표 비중 0%; 다음 봉 시가 가정 |
| v2 | trend_8_26 + reversion_12 | 9711.74 | -288.26 | sell / filled / 직전 완료 봉 목표 비중 0%; 다음 봉 시가 가정 |
| v2 | trend_8_26 AND volume_26 | 9742.44 | -257.56 | sell / filled / 직전 완료 봉 목표 비중 0%; 다음 봉 시가 가정 |
| v2 | trend_8_26 + volume_26 | 9793.25 | -206.75 | sell / filled / 직전 완료 봉 목표 비중 0%; 다음 봉 시가 가정 |
| v2 | momentum_26 AND breakout_8 | 9269.79 | -730.21 | sell / filled / 직전 완료 봉 목표 비중 0%; 다음 봉 시가 가정 |
| v2 | momentum_26 + breakout_8 | 9637.30 | -362.70 | sell / filled / 직전 완료 봉 목표 비중 0%; 다음 봉 시가 가정 |
| v2 | momentum_26 AND reversion_12 | 9567.55 | -432.45 | sell / filled / 직전 완료 봉 목표 비중 0%; 다음 봉 시가 가정 |
| v2 | momentum_26 + reversion_12 | 9783.90 | -216.10 | sell / filled / 직전 완료 봉 목표 비중 0%; 다음 봉 시가 가정 |
| v2 | momentum_26 AND volume_26 | 9941.52 | -58.48 | sell / filled / 직전 완료 봉 목표 비중 0%; 다음 봉 시가 가정 |
| v2 | momentum_26 + volume_26 | 9886.61 | -113.39 | sell / filled / 직전 완료 봉 목표 비중 0%; 다음 봉 시가 가정 |
| v2 | breakout_8 AND reversion_12 | 10000.00 | 0.00 | 대기 /  / 새 신호 대기 |
| v2 | breakout_8 + reversion_12 | 9332.64 | -667.36 | sell / filled / 직전 완료 봉 목표 비중 0%; 다음 봉 시가 가정 |
| v2 | breakout_8 AND volume_26 | 9918.86 | -81.14 | sell / filled / 직전 완료 봉 목표 비중 0%; 다음 봉 시가 가정 |
| v2 | breakout_8 + volume_26 | 9430.54 | -569.46 | sell / filled / 직전 완료 봉 목표 비중 0%; 다음 봉 시가 가정 |
| v2 | reversion_12 AND volume_26 | 9787.67 | -212.33 | sell / filled / 직전 완료 봉 목표 비중 0%; 다음 봉 시가 가정 |
| v2 | reversion_12 + volume_26 | 9575.11 | -424.89 | sell / filled / 직전 완료 봉 목표 비중 0%; 다음 봉 시가 가정 |
| v2 | ema_12_26 | 9971.99 | -28.01 | sell / filled / EMA12 > EMA26; 조건 미충족; EMA12=177.968, EMA26=178.055; 직전 완료 봉 목표를 다음 봉 시가에 모의 적용 |
| v2 | macd_12_26_9 | 10060.21 | 60.21 | sell / filled / MACD > 신호선 그리고 MACD > 0; 조건 미충족; MACD=0.288973, signal9=0.30355; 직전 완료 봉 목표를 다음 봉 시가에 모의 적용 |
| v2 | rsi_14_recovery | 9923.67 | -76.33 | sell / filled / 직전 RSI14 < 30, 현재 RSI14 >= 30 (한 봉 목표); 조건 미충족; RSI14=37.639, previous_RSI14=31.1023; 직전 완료 봉 목표를 다음 봉 시가에 모의 적용 |
| v2 | bollinger_20_reentry | 9848.96 | -151.04 | sell / filled / 직전 종가 < 직전 하단밴드, 현재 하단밴드 <= 종가 <= SMA20 (한 봉 목표); 조건 미충족; close=175.55, lower20=175.189, SMA20=177.794, previous_lower20=175.528; 직전 완료 봉 목표를 다음 봉 시가에 모의 적용 |
| v2 | donchian_20 | 9824.43 | -175.57 | sell / filled / 종가 > 현재 봉을 제외한 직전 20봉 최고가; 조건 미충족; close=179.01, prior_high20=179.16; 직전 완료 봉 목표를 다음 봉 시가에 모의 적용 |
| v2 | atr_14_breakout | 9859.04 | -140.96 | sell / filled / 종가 > 직전 종가 + 직전 ATR14 그리고 종가 > EMA26; 조건 미충족; close=177.19, threshold=177.748, prior_ATR14=0.663113, EMA26=175.734; 직전 완료 봉 목표를 다음 봉 시가에 모의 적용 |
| v2 | session_vwap | 9964.74 | -35.26 | buy / partial / 종가 > 뉴욕 거래일별 누적 전형가격 VWAP; 조건 충족; close=176.885, session_VWAP=176.63, session_volume=5.45281e+06; 직전 완료 봉 목표를 다음 봉 시가에 모의 적용 |
| v2 | obv_20 | 9837.20 | -162.80 | sell / filled / OBV > OBV의 SMA20 그리고 종가 > EMA26; 조건 미충족; OBV=1.99239e+07, OBV_SMA20=1.96226e+07, close=176.81, EMA26=177.054; 직전 완료 봉 목표를 다음 봉 시가에 모의 적용 |
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
| cash | 0.00% | 0.00% | 8.65% | 0.00% | 0.00% |
| buy_hold | 9.11% | 8.65% | 8.65% | 8.65% | 100.00% |
| trend_8_26 | 1.08% | -3.49% | 8.65% | 5.89% | 69.03% |
| momentum_26 | 2.06% | -4.98% | 8.65% | 6.33% | 74.02% |
| breakout_8 | -0.42% | -18.94% | 8.65% | 2.33% | 27.82% |
| reversion_12 | 2.68% | -6.77% | 8.65% | 1.76% | 21.00% |
| volume_26 | 2.43% | -5.43% | 8.65% | 0.46% | 5.51% |
| trend_8_26 AND momentum_26 | -0.07% | -5.38% | 8.65% | 5.34% | 62.73% |
| trend_8_26 + momentum_26 | 1.57% | -4.03% | 8.65% | 6.11% | 71.53% |
| trend_8_26 AND breakout_8 | -0.36% | -15.77% | 8.65% | 1.82% | 21.78% |
| trend_8_26 + breakout_8 | 0.35% | -11.16% | 8.65% | 4.10% | 48.43% |
| trend_8_26 AND reversion_12 | -1.96% | -7.56% | 8.65% | 0.83% | 9.97% |
| trend_8_26 + reversion_12 | 1.90% | -4.94% | 8.65% | 3.80% | 45.02% |
| trend_8_26 AND volume_26 | 1.38% | -3.20% | 8.65% | 0.26% | 3.15% |
| trend_8_26 + volume_26 | 1.77% | -4.26% | 8.65% | 3.14% | 37.27% |
| momentum_26 AND breakout_8 | -0.66% | -18.11% | 8.65% | 2.16% | 25.72% |
| momentum_26 + breakout_8 | 0.83% | -12.22% | 8.65% | 4.31% | 50.93% |
| momentum_26 AND reversion_12 | -0.44% | -6.91% | 8.65% | 0.85% | 10.24% |
| momentum_26 + reversion_12 | 2.40% | -4.68% | 8.65% | 4.02% | 47.51% |
| momentum_26 AND volume_26 | 2.15% | -1.64% | 8.65% | 0.20% | 2.36% |
| momentum_26 + volume_26 | 2.27% | -4.00% | 8.65% | 3.35% | 39.77% |
| breakout_8 AND reversion_12 | 0.00% | 0.00% | 8.65% | 0.00% | 0.00% |
| breakout_8 + reversion_12 | 1.14% | -12.89% | 8.65% | 2.04% | 24.42% |
| breakout_8 AND volume_26 | 0.51% | -1.17% | 8.65% | 0.09% | 1.05% |
| breakout_8 + volume_26 | 1.01% | -11.52% | 8.65% | 1.39% | 16.67% |
| reversion_12 AND volume_26 | 0.29% | -2.62% | 8.65% | 0.17% | 2.10% |
| reversion_12 + volume_26 | 2.57% | -5.31% | 8.65% | 1.10% | 13.26% |
| ema_12_26 | 1.19% | -1.75% | 8.65% | 6.80% | 79.27% |
| macd_12_26_9 | 0.29% | -5.43% | 8.65% | 3.68% | 43.57% |
| rsi_14_recovery | -0.08% | -1.33% | 8.65% | 0.07% | 0.79% |
| bollinger_20_reentry | -1.07% | -3.94% | 8.65% | 0.15% | 1.84% |
| donchian_20 | -0.93% | -10.43% | 8.65% | 0.81% | 9.71% |
| atr_14_breakout | 0.47% | -8.01% | 8.65% | 0.48% | 5.77% |
| session_vwap | 1.45% | -9.43% | 8.65% | 5.66% | 66.40% |
| obv_20 | 2.64% | -6.03% | 8.65% | 4.20% | 49.61% |
| stochastic_14_3_recovery | 0.79% | -8.49% | 8.65% | 0.50% | 6.04% |
| mfi_14_recovery | -0.31% | -1.97% | 8.65% | 0.09% | 1.05% |
| adx_14_trend | 3.88% | 0.87% | 8.65% | 3.75% | 44.36% |
| aroon_25_trend | -3.42% | -10.08% | 8.65% | 3.03% | 35.96% |
| cci_20_momentum | 3.54% | -5.60% | 8.65% | 2.44% | 29.13% |
| williams_14_recovery | -0.90% | -6.95% | 8.65% | 0.33% | 3.94% |
| cmf_20_accumulation | 0.82% | -6.13% | 8.65% | 4.13% | 48.82% |
| chaikin_3_10 | 1.63% | -6.55% | 8.65% | 5.07% | 59.58% |
| roc_10_momentum | 0.80% | -5.36% | 8.65% | 1.09% | 13.12% |
| trix_15_trend | 0.95% | -5.21% | 8.65% | 5.73% | 67.19% |
| keltner_20_breakout | 0.18% | -6.72% | 8.65% | 1.45% | 17.32% |
| opening_range_30m | -0.01% | -9.21% | 8.65% | 2.89% | 34.38% |

동일 구간·초기 자금, 종료 시 청산 비용 포함. 노출 맞춤은 사후 설명용이며 v2 실제 계좌 성과가 아닙니다.
[낙폭 분해·비용 영향·전체 구간](XOM/comparison.json)

[v1 전체 기록](XOM/accounts.json) · [v2 전체 기록](XOM/accounts-v2.json)

## JNJ 계좌

| 모델 | 전략 | 평가액 USD | 손익 USD | 최근 매매·이유 |
|---|---|---:|---:|---|
| v1 | cash | 10000.00 | 0.00 | 대기 /  / 새 신호 대기 |
| v1 | buy_hold | 10121.03 | 121.03 | buy /  / buy_hold: prior completed bar target 100%; next bar open simulation |
| v1 | trend_8_26 | 10072.37 | 72.37 | buy /  / trend_8_26: prior completed bar target 100%; next bar open simulation |
| v1 | momentum_26 | 9843.00 | -157.00 | buy /  / momentum_26: prior completed bar target 100%; next bar open simulation |
| v1 | breakout_8 | 9513.91 | -486.09 | sell /  / breakout_8: prior completed bar target 0%; next bar open simulation |
| v1 | reversion_12 | 9868.44 | -131.56 | sell /  / reversion_12: prior completed bar target 0%; next bar open simulation |
| v1 | volume_26 | 9943.90 | -56.10 | sell /  / volume_26: prior completed bar target 0%; next bar open simulation |
| v1 | trend_8_26 AND momentum_26 | 9894.95 | -105.05 | buy /  / trend_8_26 AND momentum_26: prior completed bar target 100%; next bar open simulation |
| v1 | trend_8_26 + momentum_26 | 9957.32 | -42.68 | buy /  / trend_8_26 + momentum_26: prior completed bar target 100%; next bar open simulation |
| v1 | trend_8_26 AND breakout_8 | 9814.73 | -185.27 | sell /  / trend_8_26 AND breakout_8: prior completed bar target 0%; next bar open simulation |
| v1 | trend_8_26 + breakout_8 | 9808.98 | -191.02 | buy /  / trend_8_26 + breakout_8: prior completed bar target 50%; next bar open simulation |
| v1 | trend_8_26 AND reversion_12 | 9968.65 | -31.35 | sell /  / trend_8_26 AND reversion_12: prior completed bar target 0%; next bar open simulation |
| v1 | trend_8_26 + reversion_12 | 9969.99 | -30.01 | buy /  / trend_8_26 + reversion_12: prior completed bar target 50%; next bar open simulation |
| v1 | trend_8_26 AND volume_26 | 9995.12 | -4.88 | sell /  / trend_8_26 AND volume_26: prior completed bar target 0%; next bar open simulation |
| v1 | trend_8_26 + volume_26 | 10008.13 | 8.13 | buy /  / trend_8_26 + volume_26: prior completed bar target 50%; next bar open simulation |
| v1 | momentum_26 AND breakout_8 | 9833.49 | -166.51 | sell /  / momentum_26 AND breakout_8: prior completed bar target 0%; next bar open simulation |
| v1 | momentum_26 + breakout_8 | 9676.89 | -323.11 | buy /  / momentum_26 + breakout_8: prior completed bar target 50%; next bar open simulation |
| v1 | momentum_26 AND reversion_12 | 9976.62 | -23.38 | sell /  / momentum_26 AND reversion_12: prior completed bar target 0%; next bar open simulation |
| v1 | momentum_26 + reversion_12 | 9875.30 | -124.70 | buy /  / momentum_26 + reversion_12: prior completed bar target 50%; next bar open simulation |
| v1 | momentum_26 AND volume_26 | 10000.00 | 0.00 | 대기 /  / 새 신호 대기 |
| v1 | momentum_26 + volume_26 | 9932.96 | -67.04 | buy /  / momentum_26 + volume_26: prior completed bar target 50%; next bar open simulation |
| v1 | breakout_8 AND reversion_12 | 10000.00 | 0.00 | 대기 /  / 새 신호 대기 |
| v1 | breakout_8 + reversion_12 | 9689.37 | -310.63 | sell /  / breakout_8 + reversion_12: prior completed bar target 0%; next bar open simulation |
| v1 | breakout_8 AND volume_26 | 10000.00 | 0.00 | 대기 /  / 새 신호 대기 |
| v1 | breakout_8 + volume_26 | 9745.99 | -254.01 | sell /  / breakout_8 + volume_26: prior completed bar target 0%; next bar open simulation |
| v1 | reversion_12 AND volume_26 | 9974.59 | -25.41 | sell /  / reversion_12 AND volume_26: prior completed bar target 0%; next bar open simulation |
| v1 | reversion_12 + volume_26 | 9925.96 | -74.04 | sell /  / reversion_12 + volume_26: prior completed bar target 0%; next bar open simulation |
| v1 | ema_12_26 | 9941.63 | -58.37 | buy /  / EMA12 > EMA26; 조건 충족; EMA12=253.915, EMA26=253.911 |
| v1 | macd_12_26_9 | 9887.47 | -112.53 | sell /  / MACD > 신호선 그리고 MACD > 0; 조건 미충족; MACD=1.30676, signal9=1.31668 |
| v1 | rsi_14_recovery | 9923.04 | -76.96 | sell /  / 직전 RSI14 < 30, 현재 RSI14 >= 30 (한 봉 목표); 조건 미충족; RSI14=40.3665, previous_RSI14=36.2025 |
| v1 | bollinger_20_reentry | 9881.04 | -118.96 | sell /  / 직전 종가 < 직전 하단밴드, 현재 하단밴드 <= 종가 <= SMA20 (한 봉 목표); 조건 미충족; close=251.75, lower20=251.316, SMA20=254.208, previous_lower20=251.691 |
| v1 | donchian_20 | 9921.02 | -78.98 | sell /  / 종가 > 현재 봉을 제외한 직전 20봉 최고가; 조건 미충족; close=258.68, prior_high20=260.425 |
| v1 | atr_14_breakout | 9805.90 | -194.10 | sell /  / 종가 > 직전 종가 + 직전 ATR14 그리고 종가 > EMA26; 조건 미충족; close=258.68, threshold=261.221, prior_ATR14=1.00083, EMA26=254.754 |
| v1 | session_vwap | 9832.03 | -167.97 | sell /  / 종가 > 뉴욕 거래일별 누적 전형가격 VWAP; 조건 미충족; close=258.91, session_VWAP=259.405, session_volume=4.28557e+06 |
| v1 | obv_20 | 9674.83 | -325.17 | buy /  / OBV > OBV의 SMA20 그리고 종가 > EMA26; 조건 충족; OBV=4.78456e+06, OBV_SMA20=3.4932e+06, close=254.04, EMA26=253.978 |
| v1 | stochastic_14_3_recovery | 9862.87 | -137.13 | sell /  / 직전 %K14 < 20에서 %K14가 %D3 상향 돌파 (한 봉 목표); 조건 미충족; K14=28.9392, D3=18.1738, previous_K14=19.7943, previous_D3=12.6561 |
| v1 | mfi_14_recovery | 10000.00 | 0.00 | 대기 /  / 새 신호 대기 |
| v1 | adx_14_trend | 9801.72 | -198.28 | buy /  / Wilder ADX14 >= 25 그리고 +DI14 > -DI14; 조건 충족; ADX14=27.0884, plus_DI14=47.0278, minus_DI14=11.4099 |
| v1 | aroon_25_trend | 9899.46 | -100.54 | sell /  / Aroon25 Up > 70 그리고 Down < 30 (동률이면 최신 극값); 조건 미충족; Aroon_up=68, Aroon_down=44 |
| v1 | cci_20_momentum | 9818.66 | -181.34 | sell /  / CCI20 > 100 (전형가격·평균절대편차); 조건 미충족; CCI20=95.1073 |
| v1 | williams_14_recovery | 9903.67 | -96.33 | sell /  / 직전 Williams %R14 < -80, 현재 >= -80 (한 봉 목표); 조건 미충족; Williams_R14=-61.3372, previous_R14=-71.0608 |
| v1 | cmf_20_accumulation | 10247.97 | 247.97 | buy /  / Chaikin Money Flow20 > 0.1; 조건 충족; CMF20=0.280188, volume20=5.69706e+06 |
| v1 | chaikin_3_10 | 9893.76 | -106.24 | buy /  / ADL의 EMA3 - EMA10 > 0 그리고 종가 > EMA26; 조건 충족; Chaikin3_10=250777, ADL=4.30146e+06, close=254.04, EMA26=253.978 |
| v1 | roc_10_momentum | 9691.76 | -308.24 | sell /  / 10봉 ROC > 1% 그리고 종가 > EMA26; 조건 미충족; ROC10_percent=-0.503419, close=258.91, EMA26=257.09 |
| v1 | trix_15_trend | 9785.23 | -214.77 | buy /  / 15봉 삼중 EMA의 1봉 변화율 TRIX > 0 그리고 종가 > EMA26; 조건 충족; TRIX15_percent=0.000945132, close=260.22, EMA26=254.44 |
| v1 | keltner_20_breakout | 9916.04 | -83.96 | sell /  / 종가 > EMA20 + 2 x Wilder ATR14; 조건 미충족; close=258.91, upper_Keltner=259.564, EMA20=257.603, ATR14=0.980686 |
| v1 | opening_range_30m | 10000.00 | 0.00 | 대기 /  / 새 신호 대기 |
| v2 | cash | 10000.00 | 0.00 | 대기 /  / 새 신호 대기 |
| v2 | buy_hold | 9884.82 | -115.18 | 중단: 손실 한도 / buy / partial / 직전 완료 봉 목표 비중 100%; 다음 봉 시가 가정 |
| v2 | trend_8_26 | 9884.82 | -115.18 | 중단: 손실 한도 / buy / partial / 직전 완료 봉 목표 비중 100%; 다음 봉 시가 가정 |
| v2 | momentum_26 | 9884.82 | -115.18 | 중단: 손실 한도 / buy / partial / 직전 완료 봉 목표 비중 100%; 다음 봉 시가 가정 |
| v2 | breakout_8 | 9343.39 | -656.61 | 중단: 손실 한도 / sell / filled / 직전 완료 봉 목표 비중 0%; 다음 봉 시가 가정 |
| v2 | reversion_12 | 9556.92 | -443.08 | sell / filled / 직전 완료 봉 목표 비중 0%; 다음 봉 시가 가정 |
| v2 | volume_26 | 9728.64 | -271.36 | sell / filled / 직전 완료 봉 목표 비중 0%; 다음 봉 시가 가정 |
| v2 | trend_8_26 AND momentum_26 | 9884.82 | -115.18 | 중단: 손실 한도 / buy / partial / 직전 완료 봉 목표 비중 100%; 다음 봉 시가 가정 |
| v2 | trend_8_26 + momentum_26 | 9884.82 | -115.18 | 중단: 손실 한도 / buy / partial / 직전 완료 봉 목표 비중 100%; 다음 봉 시가 가정 |
| v2 | trend_8_26 AND breakout_8 | 9419.39 | -580.61 | 중단: 손실 한도 / sell / filled / 직전 완료 봉 목표 비중 0%; 다음 봉 시가 가정 |
| v2 | trend_8_26 + breakout_8 | 9378.08 | -621.92 | buy / filled / 직전 완료 봉 목표 비중 50%; 다음 봉 시가 가정 |
| v2 | trend_8_26 AND reversion_12 | 9942.82 | -57.18 | sell / filled / 직전 완료 봉 목표 비중 0%; 다음 봉 시가 가정 |
| v2 | trend_8_26 + reversion_12 | 9732.92 | -267.08 | 중단: 손실 한도 / sell / filled / 직전 완료 봉 목표 비중 0%; 다음 봉 시가 가정 |
| v2 | trend_8_26 AND volume_26 | 9861.95 | -138.05 | sell / filled / 직전 완료 봉 목표 비중 0%; 다음 봉 시가 가정 |
| v2 | trend_8_26 + volume_26 | 9917.36 | -82.64 | 중단: 손실 한도 / buy / filled / 직전 완료 봉 목표 비중 50%; 다음 봉 시가 가정 |
| v2 | momentum_26 AND breakout_8 | 9435.09 | -564.91 | sell / filled / 직전 완료 봉 목표 비중 0%; 다음 봉 시가 가정 |
| v2 | momentum_26 + breakout_8 | 9242.18 | -757.82 | buy / filled / 직전 완료 봉 목표 비중 50%; 다음 봉 시가 가정 |
| v2 | momentum_26 AND reversion_12 | 9913.65 | -86.35 | sell / filled / 직전 완료 봉 목표 비중 0%; 다음 봉 시가 가정 |
| v2 | momentum_26 + reversion_12 | 9732.92 | -267.08 | 중단: 손실 한도 / sell / filled / 직전 완료 봉 목표 비중 0%; 다음 봉 시가 가정 |
| v2 | momentum_26 AND volume_26 | 9920.93 | -79.07 | sell / filled / 직전 완료 봉 목표 비중 0%; 다음 봉 시가 가정 |
| v2 | momentum_26 + volume_26 | 9917.36 | -82.64 | 중단: 손실 한도 / buy / filled / 직전 완료 봉 목표 비중 50%; 다음 봉 시가 가정 |
| v2 | breakout_8 AND reversion_12 | 10000.00 | 0.00 | 대기 /  / 새 신호 대기 |
| v2 | breakout_8 + reversion_12 | 9272.30 | -727.70 | sell / filled / 직전 완료 봉 목표 비중 0%; 다음 봉 시가 가정 |
| v2 | breakout_8 AND volume_26 | 9814.17 | -185.83 | sell / filled / 직전 완료 봉 목표 비중 0%; 다음 봉 시가 가정 |
| v2 | breakout_8 + volume_26 | 9355.32 | -644.68 | sell / filled / 직전 완료 봉 목표 비중 0%; 다음 봉 시가 가정 |
| v2 | reversion_12 AND volume_26 | 9859.15 | -140.85 | sell / filled / 직전 완료 봉 목표 비중 0%; 다음 봉 시가 가정 |
| v2 | reversion_12 + volume_26 | 9683.25 | -316.75 | sell / filled / 직전 완료 봉 목표 비중 0%; 다음 봉 시가 가정 |
| v2 | ema_12_26 | 9936.66 | -63.34 | buy / partial / EMA12 > EMA26; 조건 충족; EMA12=253.915, EMA26=253.911; 직전 완료 봉 목표를 다음 봉 시가에 모의 적용 |
| v2 | macd_12_26_9 | 9881.54 | -118.46 | sell / filled / MACD > 신호선 그리고 MACD > 0; 조건 미충족; MACD=1.30676, signal9=1.31668; 직전 완료 봉 목표를 다음 봉 시가에 모의 적용 |
| v2 | rsi_14_recovery | 9919.07 | -80.93 | sell / filled / 직전 RSI14 < 30, 현재 RSI14 >= 30 (한 봉 목표); 조건 미충족; RSI14=40.3665, previous_RSI14=36.2025; 직전 완료 봉 목표를 다음 봉 시가에 모의 적용 |
| v2 | bollinger_20_reentry | 9877.09 | -122.91 | sell / filled / 직전 종가 < 직전 하단밴드, 현재 하단밴드 <= 종가 <= SMA20 (한 봉 목표); 조건 미충족; close=251.75, lower20=251.316, SMA20=254.208, previous_lower20=251.691; 직전 완료 봉 목표를 다음 봉 시가에 모의 적용 |
| v2 | donchian_20 | 9919.03 | -80.97 | sell / filled / 종가 > 현재 봉을 제외한 직전 20봉 최고가; 조건 미충족; close=258.68, prior_high20=260.425; 직전 완료 봉 목표를 다음 봉 시가에 모의 적용 |
| v2 | atr_14_breakout | 9800.02 | -199.98 | sell / filled / 종가 > 직전 종가 + 직전 ATR14 그리고 종가 > EMA26; 조건 미충족; close=258.68, threshold=261.221, prior_ATR14=1.00083, EMA26=254.754; 직전 완료 봉 목표를 다음 봉 시가에 모의 적용 |
| v2 | session_vwap | 9818.27 | -181.73 | sell / filled / 종가 > 뉴욕 거래일별 누적 전형가격 VWAP; 조건 미충족; close=258.91, session_VWAP=259.405, session_volume=4.28557e+06; 직전 완료 봉 목표를 다음 봉 시가에 모의 적용 |
| v2 | obv_20 | 9662.26 | -337.74 | buy / partial / OBV > OBV의 SMA20 그리고 종가 > EMA26; 조건 충족; OBV=4.78456e+06, OBV_SMA20=3.4932e+06, close=254.04, EMA26=253.978; 직전 완료 봉 목표를 다음 봉 시가에 모의 적용 |
| v2 | stochastic_14_3_recovery | 9856.96 | -143.04 | sell / filled / 직전 %K14 < 20에서 %K14가 %D3 상향 돌파 (한 봉 목표); 조건 미충족; K14=28.9392, D3=18.1738, previous_K14=19.7943, previous_D3=12.6561; 직전 완료 봉 목표를 다음 봉 시가에 모의 적용 |
| v2 | mfi_14_recovery | 10000.00 | 0.00 | 대기 /  / 새 신호 대기 |
| v2 | adx_14_trend | 9794.86 | -205.14 | buy / partial / Wilder ADX14 >= 25 그리고 +DI14 > -DI14; 조건 충족; ADX14=27.0884, plus_DI14=47.0278, minus_DI14=11.4099; 직전 완료 봉 목표를 다음 봉 시가에 모의 적용 |
| v2 | aroon_25_trend | 9895.50 | -104.50 | sell / filled / Aroon25 Up > 70 그리고 Down < 30 (동률이면 최신 극값); 조건 미충족; Aroon_up=68, Aroon_down=44; 직전 완료 봉 목표를 다음 봉 시가에 모의 적용 |
| v2 | cci_20_momentum | 9812.77 | -187.23 | sell / filled / CCI20 > 100 (전형가격·평균절대편차); 조건 미충족; CCI20=95.1073; 직전 완료 봉 목표를 다음 봉 시가에 모의 적용 |
| v2 | williams_14_recovery | 9899.71 | -100.29 | sell / filled / 직전 Williams %R14 < -80, 현재 >= -80 (한 봉 목표); 조건 미충족; Williams_R14=-61.3372, previous_R14=-71.0608; 직전 완료 봉 목표를 다음 봉 시가에 모의 적용 |
| v2 | cmf_20_accumulation | 10246.95 | 246.95 | buy / partial / Chaikin Money Flow20 > 0.1; 조건 충족; CMF20=0.280188, volume20=5.69706e+06; 직전 완료 봉 목표를 다음 봉 시가에 모의 적용 |
| v2 | chaikin_3_10 | 9886.84 | -113.16 | buy / partial / ADL의 EMA3 - EMA10 > 0 그리고 종가 > EMA26; 조건 충족; Chaikin3_10=250777, ADL=4.30146e+06, close=254.04, EMA26=253.978; 직전 완료 봉 목표를 다음 봉 시가에 모의 적용 |
| v2 | roc_10_momentum | 9684.01 | -315.99 | sell / filled / 10봉 ROC > 1% 그리고 종가 > EMA26; 조건 미충족; ROC10_percent=-0.503419, close=258.91, EMA26=257.09; 직전 완료 봉 목표를 다음 봉 시가에 모의 적용 |
| v2 | trix_15_trend | 9780.34 | -219.66 | buy / partial / 15봉 삼중 EMA의 1봉 변화율 TRIX > 0 그리고 종가 > EMA26; 조건 충족; TRIX15_percent=0.000945132, close=260.22, EMA26=254.44; 직전 완료 봉 목표를 다음 봉 시가에 모의 적용 |
| v2 | keltner_20_breakout | 9914.05 | -85.95 | sell / filled / 종가 > EMA20 + 2 x Wilder ATR14; 조건 미충족; close=258.91, upper_Keltner=259.564, EMA20=257.603, ATR14=0.980686; 직전 완료 봉 목표를 다음 봉 시가에 모의 적용 |
| v2 | opening_range_30m | 10000.00 | 0.00 | 대기 /  / 새 신호 대기 |

### 같은 기간의 비용·노출 비교 (사후 연구)

| 전략 | 비용 전 | 비용 후 | 100% 보유 | 같은 평균 노출 보유 | 평균 노출 |
|---|---:|---:|---:|---:|---:|
| cash | 0.00% | 0.00% | -3.68% | -0.00% | 0.00% |
| buy_hold | -3.28% | -3.68% | -3.68% | -3.68% | 100.00% |
| trend_8_26 | 3.25% | 0.68% | -3.68% | -1.88% | 49.87% |
| momentum_26 | -0.14% | -3.85% | -3.68% | -1.78% | 47.24% |
| breakout_8 | -1.40% | -18.38% | -3.68% | -0.77% | 20.21% |
| reversion_12 | -6.90% | -14.76% | -3.68% | -1.15% | 30.18% |
| volume_26 | -0.92% | -7.75% | -3.68% | -0.25% | 6.56% |
| trend_8_26 AND momentum_26 | 1.12% | -2.22% | -3.68% | -1.59% | 41.99% |
| trend_8_26 + momentum_26 | 1.55% | -1.60% | -3.68% | -1.83% | 48.56% |
| trend_8_26 AND breakout_8 | 0.12% | -11.73% | -3.68% | -0.52% | 13.65% |
| trend_8_26 + breakout_8 | 0.93% | -9.14% | -3.68% | -1.33% | 35.05% |
| trend_8_26 AND reversion_12 | 1.04% | -2.30% | -3.68% | -0.21% | 5.51% |
| trend_8_26 + reversion_12 | -1.92% | -6.96% | -3.68% | -1.51% | 40.03% |
| trend_8_26 AND volume_26 | 1.42% | -1.10% | -3.68% | -0.06% | 1.57% |
| trend_8_26 + volume_26 | 1.18% | -3.41% | -3.68% | -1.07% | 28.22% |
| momentum_26 AND breakout_8 | 0.98% | -9.84% | -3.68% | -0.49% | 12.86% |
| momentum_26 + breakout_8 | -0.75% | -11.21% | -3.68% | -1.28% | 33.73% |
| momentum_26 AND reversion_12 | -0.65% | -3.13% | -3.68% | -0.22% | 5.77% |
| momentum_26 + reversion_12 | -3.55% | -8.89% | -3.68% | -1.46% | 38.72% |
| momentum_26 AND volume_26 | 0.14% | -0.70% | -3.68% | -0.02% | 0.52% |
| momentum_26 + volume_26 | -0.50% | -4.81% | -3.68% | -1.02% | 26.91% |
| breakout_8 AND reversion_12 | 0.00% | 0.00% | -3.68% | -0.00% | 0.00% |
| breakout_8 + reversion_12 | -4.17% | -16.07% | -3.68% | -0.96% | 25.21% |
| breakout_8 AND volume_26 | -0.91% | -2.15% | -3.68% | -0.03% | 0.79% |
| breakout_8 + volume_26 | -1.15% | -12.31% | -3.68% | -0.51% | 13.39% |
| reversion_12 AND volume_26 | -1.84% | -4.69% | -3.68% | -0.11% | 2.89% |
| reversion_12 + volume_26 | -3.94% | -10.57% | -3.68% | -0.70% | 18.38% |
| ema_12_26 | 0.48% | -2.02% | -3.68% | -1.64% | 43.57% |
| macd_12_26_9 | 5.83% | 2.76% | -3.68% | -1.12% | 29.40% |
| rsi_14_recovery | -1.35% | -6.20% | -3.68% | -0.12% | 3.15% |
| bollinger_20_reentry | -1.10% | -5.56% | -3.68% | -0.11% | 2.89% |
| donchian_20 | 0.23% | -7.07% | -3.68% | -0.26% | 6.82% |
| atr_14_breakout | 0.79% | -5.36% | -3.68% | -0.18% | 4.72% |
| session_vwap | 3.37% | -4.96% | -3.68% | -1.86% | 49.34% |
| obv_20 | -5.42% | -14.49% | -3.68% | -1.33% | 35.17% |
| stochastic_14_3_recovery | -0.31% | -12.11% | -3.68% | -0.30% | 7.87% |
| mfi_14_recovery | 0.33% | -0.93% | -3.68% | -0.03% | 0.79% |
| adx_14_trend | -2.58% | -7.76% | -3.68% | -1.31% | 34.65% |
| aroon_25_trend | 3.81% | -0.46% | -3.68% | -1.17% | 30.71% |
| cci_20_momentum | -0.07% | -6.96% | -3.68% | -0.82% | 21.52% |
| williams_14_recovery | -1.58% | -8.74% | -3.68% | -0.18% | 4.72% |
| cmf_20_accumulation | 5.31% | 1.40% | -3.68% | -1.21% | 32.02% |
| chaikin_3_10 | -2.80% | -7.97% | -3.68% | -1.38% | 36.48% |
| roc_10_momentum | -2.79% | -9.49% | -3.68% | -0.67% | 17.59% |
| trix_15_trend | -0.59% | -3.06% | -3.68% | -1.25% | 33.07% |
| keltner_20_breakout | 0.20% | -3.52% | -3.68% | -0.45% | 11.81% |
| opening_range_30m | 0.79% | -2.95% | -3.68% | -0.99% | 25.98% |

동일 구간·초기 자금, 종료 시 청산 비용 포함. 노출 맞춤은 사후 설명용이며 v2 실제 계좌 성과가 아닙니다.
[낙폭 분해·비용 영향·전체 구간](JNJ/comparison.json)

[v1 전체 기록](JNJ/accounts.json) · [v2 전체 기록](JNJ/accounts-v2.json)

## CAT 계좌

| 모델 | 전략 | 평가액 USD | 손익 USD | 최근 매매·이유 |
|---|---|---:|---:|---|
| v1 | cash | 10000.00 | 0.00 | 대기 /  / 새 신호 대기 |
| v1 | buy_hold | 9862.95 | -137.05 | buy /  / buy_hold: prior completed bar target 100%; next bar open simulation |
| v1 | trend_8_26 | 9829.12 | -170.88 | sell /  / trend_8_26: prior completed bar target 0%; next bar open simulation |
| v1 | momentum_26 | 9765.06 | -234.94 | sell /  / momentum_26: prior completed bar target 0%; next bar open simulation |
| v1 | breakout_8 | 9687.36 | -312.64 | sell /  / breakout_8: prior completed bar target 0%; next bar open simulation |
| v1 | reversion_12 | 9921.83 | -78.17 | sell /  / reversion_12: prior completed bar target 0%; next bar open simulation |
| v1 | volume_26 | 10007.30 | 7.30 | sell /  / volume_26: prior completed bar target 0%; next bar open simulation |
| v1 | trend_8_26 AND momentum_26 | 9873.91 | -126.09 | sell /  / trend_8_26 AND momentum_26: prior completed bar target 0%; next bar open simulation |
| v1 | trend_8_26 + momentum_26 | 9797.24 | -202.76 | sell /  / trend_8_26 + momentum_26: prior completed bar target 0%; next bar open simulation |
| v1 | trend_8_26 AND breakout_8 | 9850.32 | -149.68 | sell /  / trend_8_26 AND breakout_8: prior completed bar target 0%; next bar open simulation |
| v1 | trend_8_26 + breakout_8 | 9758.16 | -241.84 | sell /  / trend_8_26 + breakout_8: prior completed bar target 0%; next bar open simulation |
| v1 | trend_8_26 AND reversion_12 | 9928.06 | -71.94 | sell /  / trend_8_26 AND reversion_12: prior completed bar target 0%; next bar open simulation |
| v1 | trend_8_26 + reversion_12 | 9915.64 | -84.36 | sell /  / trend_8_26 + reversion_12: prior completed bar target 0%; next bar open simulation |
| v1 | trend_8_26 AND volume_26 | 10000.00 | 0.00 | 대기 /  / 새 신호 대기 |
| v1 | trend_8_26 + volume_26 | 9937.74 | -62.26 | sell /  / trend_8_26 + volume_26: prior completed bar target 0%; next bar open simulation |
| v1 | momentum_26 AND breakout_8 | 9804.82 | -195.18 | sell /  / momentum_26 AND breakout_8: prior completed bar target 0%; next bar open simulation |
| v1 | momentum_26 + breakout_8 | 9726.19 | -273.81 | sell /  / momentum_26 + breakout_8: prior completed bar target 0%; next bar open simulation |
| v1 | momentum_26 AND reversion_12 | 9887.21 | -112.79 | sell /  / momentum_26 AND reversion_12: prior completed bar target 0%; next bar open simulation |
| v1 | momentum_26 + reversion_12 | 9843.85 | -156.15 | sell /  / momentum_26 + reversion_12: prior completed bar target 0%; next bar open simulation |
| v1 | momentum_26 AND volume_26 | 9985.43 | -14.57 | sell /  / momentum_26 AND volume_26: prior completed bar target 0%; next bar open simulation |
| v1 | momentum_26 + volume_26 | 9885.51 | -114.49 | sell /  / momentum_26 + volume_26: prior completed bar target 0%; next bar open simulation |
| v1 | breakout_8 AND reversion_12 | 10000.00 | 0.00 | 대기 /  / 새 신호 대기 |
| v1 | breakout_8 + reversion_12 | 9804.44 | -195.56 | sell /  / breakout_8 + reversion_12: prior completed bar target 0%; next bar open simulation |
| v1 | breakout_8 AND volume_26 | 9985.43 | -14.57 | sell /  / breakout_8 AND volume_26: prior completed bar target 0%; next bar open simulation |
| v1 | breakout_8 + volume_26 | 9846.03 | -153.97 | sell /  / breakout_8 + volume_26: prior completed bar target 0%; next bar open simulation |
| v1 | reversion_12 AND volume_26 | 10046.29 | 46.29 | sell /  / reversion_12 AND volume_26: prior completed bar target 0%; next bar open simulation |
| v1 | reversion_12 + volume_26 | 9964.97 | -35.03 | sell /  / reversion_12 + volume_26: prior completed bar target 0%; next bar open simulation |
| v1 | ema_12_26 | 9862.47 | -137.53 | sell /  / EMA12 > EMA26; 조건 미충족; EMA12=735.622, EMA26=735.711 |
| v1 | macd_12_26_9 | 9904.18 | -95.82 | sell /  / MACD > 신호선 그리고 MACD > 0; 조건 미충족; MACD=0.746548, signal9=0.752293 |
| v1 | rsi_14_recovery | 9999.22 | -0.78 | sell /  / 직전 RSI14 < 30, 현재 RSI14 >= 30 (한 봉 목표); 조건 미충족; RSI14=43.621, previous_RSI14=38.5787 |
| v1 | bollinger_20_reentry | 9777.09 | -222.91 | sell /  / 직전 종가 < 직전 하단밴드, 현재 하단밴드 <= 종가 <= SMA20 (한 봉 목표); 조건 미충족; close=721.16, lower20=716.851, SMA20=725.821, previous_lower20=717.276 |
| v1 | donchian_20 | 9950.83 | -49.17 | sell /  / 종가 > 현재 봉을 제외한 직전 20봉 최고가; 조건 미충족; close=739.81, prior_high20=742.28 |
| v1 | atr_14_breakout | 9775.74 | -224.26 | sell /  / 종가 > 직전 종가 + 직전 ATR14 그리고 종가 > EMA26; 조건 미충족; close=732.42, threshold=735.931, prior_ATR14=4.99094, EMA26=726.612 |
| v1 | session_vwap | 9375.89 | -624.11 | buy /  / 종가 > 뉴욕 거래일별 누적 전형가격 VWAP; 조건 충족; close=725.26, session_VWAP=723.918, session_volume=2.02044e+06 |
| v1 | obv_20 | 9683.67 | -316.33 | sell /  / OBV > OBV의 SMA20 그리고 종가 > EMA26; 조건 미충족; OBV=-5.85317e+06, OBV_SMA20=-5.80449e+06, close=725.22, EMA26=726.751 |
| v1 | stochastic_14_3_recovery | 9855.08 | -144.92 | sell /  / 직전 %K14 < 20에서 %K14가 %D3 상향 돌파 (한 봉 목표); 조건 미충족; K14=59.6496, D3=39.2535, previous_K14=43.8356, previous_D3=33.8642 |
| v1 | mfi_14_recovery | 10068.63 | 68.63 | sell /  / 직전 MFI14 < 20, 현재 MFI14 >= 20 (한 봉 목표); 조건 미충족; MFI14=32.7313, previous_MFI14=24.1736 |
| v1 | adx_14_trend | 10000.00 | 0.00 | 대기 /  / 새 신호 대기 |
| v1 | aroon_25_trend | 10031.15 | 31.15 | sell /  / Aroon25 Up > 70 그리고 Down < 30 (동률이면 최신 극값); 조건 미충족; Aroon_up=88, Aroon_down=48 |
| v1 | cci_20_momentum | 9890.31 | -109.69 | sell /  / CCI20 > 100 (전형가격·평균절대편차); 조건 미충족; CCI20=20.3547 |
| v1 | williams_14_recovery | 10007.06 | 7.06 | sell /  / 직전 Williams %R14 < -80, 현재 >= -80 (한 봉 목표); 조건 미충족; Williams_R14=-40.3504, previous_R14=-56.1644 |
| v1 | cmf_20_accumulation | 9790.23 | -209.77 | buy /  / Chaikin Money Flow20 > 0.1; 조건 충족; CMF20=0.130083, volume20=2.38752e+06 |
| v1 | chaikin_3_10 | 9474.17 | -525.83 | sell /  / ADL의 EMA3 - EMA10 > 0 그리고 종가 > EMA26; 조건 미충족; Chaikin3_10=39681.6, ADL=-6.22839e+06, close=725.22, EMA26=726.751 |
| v1 | roc_10_momentum | 9963.13 | -36.87 | sell /  / 10봉 ROC > 1% 그리고 종가 > EMA26; 조건 미충족; ROC10_percent=-0.134597, close=734.53, EMA26=735.486 |
| v1 | trix_15_trend | 9669.78 | -330.22 | sell /  / 15봉 삼중 EMA의 1봉 변화율 TRIX > 0 그리고 종가 > EMA26; 조건 미충족; TRIX15_percent=0.0186631, close=734.925, EMA26=736.093 |
| v1 | keltner_20_breakout | 10000.00 | 0.00 | 대기 /  / 새 신호 대기 |
| v1 | opening_range_30m | 10077.80 | 77.80 | buy /  / 뉴욕 09:30·09:45 두 완료 봉 최고가를 10:00 이후 종가가 돌파; 조건 충족; close=721.16, opening_high=718.07 |
| v2 | cash | 10000.00 | 0.00 | 대기 /  / 새 신호 대기 |
| v2 | buy_hold | 9070.71 | -929.29 | 중단: 손실 한도 / buy / partial / 직전 완료 봉 목표 비중 100%; 다음 봉 시가 가정 |
| v2 | trend_8_26 | 9749.27 | -250.73 | sell / filled / 직전 완료 봉 목표 비중 0%; 다음 봉 시가 가정 |
| v2 | momentum_26 | 9775.40 | -224.60 | sell / filled / 직전 완료 봉 목표 비중 0%; 다음 봉 시가 가정 |
| v2 | breakout_8 | 9506.39 | -493.61 | sell / filled / 직전 완료 봉 목표 비중 0%; 다음 봉 시가 가정 |
| v2 | reversion_12 | 8944.03 | -1055.97 | 중단: 손실 한도 / buy / partial / 직전 완료 봉 목표 비중 100%; 다음 봉 시가 가정 |
| v2 | volume_26 | 9199.82 | -800.18 | 중단: 손실 한도 / buy / partial / 직전 완료 봉 목표 비중 100%; 다음 봉 시가 가정 |
| v2 | trend_8_26 AND momentum_26 | 9914.96 | -85.04 | sell / filled / 직전 완료 봉 목표 비중 0%; 다음 봉 시가 가정 |
| v2 | trend_8_26 + momentum_26 | 9762.53 | -237.47 | sell / filled / 직전 완료 봉 목표 비중 0%; 다음 봉 시가 가정 |
| v2 | trend_8_26 AND breakout_8 | 9765.08 | -234.92 | sell / filled / 직전 완료 봉 목표 비중 0%; 다음 봉 시가 가정 |
| v2 | trend_8_26 + breakout_8 | 9627.50 | -372.50 | sell / filled / 직전 완료 봉 목표 비중 0%; 다음 봉 시가 가정 |
| v2 | trend_8_26 AND reversion_12 | 9738.62 | -261.38 | sell / filled / 직전 완료 봉 목표 비중 0%; 다음 봉 시가 가정 |
| v2 | trend_8_26 + reversion_12 | 9534.43 | -465.57 | sell / filled / 직전 완료 봉 목표 비중 0%; 다음 봉 시가 가정 |
| v2 | trend_8_26 AND volume_26 | 10035.44 | 35.44 | sell / filled / 직전 완료 봉 목표 비중 0%; 다음 봉 시가 가정 |
| v2 | trend_8_26 + volume_26 | 9568.27 | -431.73 | sell / filled / 직전 완료 봉 목표 비중 0%; 다음 봉 시가 가정 |
| v2 | momentum_26 AND breakout_8 | 9776.83 | -223.17 | sell / filled / 직전 완료 봉 목표 비중 0%; 다음 봉 시가 가정 |
| v2 | momentum_26 + breakout_8 | 9640.20 | -359.80 | sell / filled / 직전 완료 봉 목표 비중 0%; 다음 봉 시가 가정 |
| v2 | momentum_26 AND reversion_12 | 9755.55 | -244.45 | sell / filled / 직전 완료 봉 목표 비중 0%; 다음 봉 시가 가정 |
| v2 | momentum_26 + reversion_12 | 9507.20 | -492.80 | sell / filled / 직전 완료 봉 목표 비중 0%; 다음 봉 시가 가정 |
| v2 | momentum_26 AND volume_26 | 10032.13 | 32.13 | sell / filled / 직전 완료 봉 목표 비중 0%; 다음 봉 시가 가정 |
| v2 | momentum_26 + volume_26 | 9581.08 | -418.92 | sell / filled / 직전 완료 봉 목표 비중 0%; 다음 봉 시가 가정 |
| v2 | breakout_8 AND reversion_12 | 10000.00 | 0.00 | 대기 /  / 새 신호 대기 |
| v2 | breakout_8 + reversion_12 | 9610.18 | -389.82 | 중단: 손실 한도 / sell / filled / 직전 완료 봉 목표 비중 0%; 다음 봉 시가 가정 |
| v2 | breakout_8 AND volume_26 | 9982.12 | -17.88 | sell / filled / 직전 완료 봉 목표 비중 0%; 다음 봉 시가 가정 |
| v2 | breakout_8 + volume_26 | 9448.42 | -551.58 | sell / filled / 직전 완료 봉 목표 비중 0%; 다음 봉 시가 가정 |
| v2 | reversion_12 AND volume_26 | 9136.18 | -863.82 | 중단: 손실 한도 / buy / partial / 직전 완료 봉 목표 비중 100%; 다음 봉 시가 가정 |
| v2 | reversion_12 + volume_26 | 9334.13 | -665.87 | 중단: 손실 한도 / sell / filled / 직전 완료 봉 목표 비중 50%; 다음 봉 시가 가정 |
| v2 | ema_12_26 | 9860.50 | -139.50 | sell / filled / EMA12 > EMA26; 조건 미충족; EMA12=735.622, EMA26=735.711; 직전 완료 봉 목표를 다음 봉 시가에 모의 적용 |
| v2 | macd_12_26_9 | 9902.20 | -97.80 | sell / filled / MACD > 신호선 그리고 MACD > 0; 조건 미충족; MACD=0.746548, signal9=0.752293; 직전 완료 봉 목표를 다음 봉 시가에 모의 적용 |
| v2 | rsi_14_recovery | 9995.22 | -4.78 | sell / filled / 직전 RSI14 < 30, 현재 RSI14 >= 30 (한 봉 목표); 조건 미충족; RSI14=43.621, previous_RSI14=38.5787; 직전 완료 봉 목표를 다음 봉 시가에 모의 적용 |
| v2 | bollinger_20_reentry | 9771.22 | -228.78 | sell / filled / 직전 종가 < 직전 하단밴드, 현재 하단밴드 <= 종가 <= SMA20 (한 봉 목표); 조건 미충족; close=721.16, lower20=716.851, SMA20=725.821, previous_lower20=717.276; 직전 완료 봉 목표를 다음 봉 시가에 모의 적용 |
| v2 | donchian_20 | 9948.84 | -51.16 | sell / filled / 종가 > 현재 봉을 제외한 직전 20봉 최고가; 조건 미충족; close=739.81, prior_high20=742.28; 직전 완료 봉 목표를 다음 봉 시가에 모의 적용 |
| v2 | atr_14_breakout | 9767.92 | -232.08 | sell / filled / 종가 > 직전 종가 + 직전 ATR14 그리고 종가 > EMA26; 조건 미충족; close=732.42, threshold=735.931, prior_ATR14=4.99094, EMA26=726.612; 직전 완료 봉 목표를 다음 봉 시가에 모의 적용 |
| v2 | session_vwap | 9359.97 | -640.03 | buy / partial / 종가 > 뉴욕 거래일별 누적 전형가격 VWAP; 조건 충족; close=725.26, session_VWAP=723.918, session_volume=2.02044e+06; 직전 완료 봉 목표를 다음 봉 시가에 모의 적용 |
| v2 | obv_20 | 9675.93 | -324.07 | sell / filled / OBV > OBV의 SMA20 그리고 종가 > EMA26; 조건 미충족; OBV=-5.85317e+06, OBV_SMA20=-5.80449e+06, close=725.22, EMA26=726.751; 직전 완료 봉 목표를 다음 봉 시가에 모의 적용 |
| v2 | stochastic_14_3_recovery | 9843.26 | -156.74 | sell / filled / 직전 %K14 < 20에서 %K14가 %D3 상향 돌파 (한 봉 목표); 조건 미충족; K14=59.6496, D3=39.2535, previous_K14=43.8356, previous_D3=33.8642; 직전 완료 봉 목표를 다음 봉 시가에 모의 적용 |
| v2 | mfi_14_recovery | 10064.61 | 64.61 | sell / filled / 직전 MFI14 < 20, 현재 MFI14 >= 20 (한 봉 목표); 조건 미충족; MFI14=32.7313, previous_MFI14=24.1736; 직전 완료 봉 목표를 다음 봉 시가에 모의 적용 |
| v2 | adx_14_trend | 10000.00 | 0.00 | 대기 /  / 새 신호 대기 |
| v2 | aroon_25_trend | 10029.14 | 29.14 | sell / filled / Aroon25 Up > 70 그리고 Down < 30 (동률이면 최신 극값); 조건 미충족; Aroon_up=88, Aroon_down=48; 직전 완료 봉 목표를 다음 봉 시가에 모의 적용 |
| v2 | cci_20_momentum | 9886.36 | -113.64 | sell / filled / CCI20 > 100 (전형가격·평균절대편차); 조건 미충족; CCI20=20.3547; 직전 완료 봉 목표를 다음 봉 시가에 모의 적용 |
| v2 | williams_14_recovery | 9999.06 | -0.94 | sell / filled / 직전 Williams %R14 < -80, 현재 >= -80 (한 봉 목표); 조건 미충족; Williams_R14=-40.3504, previous_R14=-56.1644; 직전 완료 봉 목표를 다음 봉 시가에 모의 적용 |
| v2 | cmf_20_accumulation | 9783.38 | -216.62 | buy / partial / Chaikin Money Flow20 > 0.1; 조건 충족; CMF20=0.130083, volume20=2.38752e+06; 직전 완료 봉 목표를 다음 봉 시가에 모의 적용 |
| v2 | chaikin_3_10 | 9552.78 | -447.22 | 중단: 손실 한도 / buy / partial / ADL의 EMA3 - EMA10 > 0 그리고 종가 > EMA26; 조건 충족; Chaikin3_10=293683, ADL=-4.91156e+06, close=739.58, EMA26=736.187; 직전 완료 봉 목표를 다음 봉 시가에 모의 적용 |
| v2 | roc_10_momentum | 9961.14 | -38.86 | sell / filled / 10봉 ROC > 1% 그리고 종가 > EMA26; 조건 미충족; ROC10_percent=-0.134597, close=734.53, EMA26=735.486; 직전 완료 봉 목표를 다음 봉 시가에 모의 적용 |
| v2 | trix_15_trend | 9562.40 | -437.60 | 중단: 손실 한도 / buy / partial / 15봉 삼중 EMA의 1봉 변화율 TRIX > 0 그리고 종가 > EMA26; 조건 충족; TRIX15_percent=0.0196284, close=739.58, EMA26=736.187; 직전 완료 봉 목표를 다음 봉 시가에 모의 적용 |
| v2 | keltner_20_breakout | 10000.00 | 0.00 | 대기 /  / 새 신호 대기 |
| v2 | opening_range_30m | 10074.78 | 74.78 | buy / partial / 뉴욕 09:30·09:45 두 완료 봉 최고가를 10:00 이후 종가가 돌파; 조건 충족; close=721.16, opening_high=718.07; 직전 완료 봉 목표를 다음 봉 시가에 모의 적용 |

### 같은 기간의 비용·노출 비교 (사후 연구)

| 전략 | 비용 전 | 비용 후 | 100% 보유 | 같은 평균 노출 보유 | 평균 노출 |
|---|---:|---:|---:|---:|---:|
| cash | 0.00% | 0.00% | -12.77% | -0.00% | 0.00% |
| buy_hold | -12.40% | -12.77% | -12.77% | -12.77% | 100.00% |
| trend_8_26 | -1.54% | -5.19% | -12.77% | -5.61% | 42.78% |
| momentum_26 | -3.37% | -6.95% | -12.77% | -5.38% | 40.94% |
| breakout_8 | -3.61% | -15.38% | -12.77% | -1.78% | 13.39% |
| reversion_12 | -2.76% | -16.05% | -12.77% | -3.75% | 28.35% |
| volume_26 | -2.12% | -9.25% | -12.77% | -1.08% | 8.14% |
| trend_8_26 AND momentum_26 | 0.36% | -2.14% | -12.77% | -4.70% | 35.70% |
| trend_8_26 + momentum_26 | -2.44% | -6.07% | -12.77% | -5.50% | 41.87% |
| trend_8_26 AND breakout_8 | -2.00% | -7.99% | -12.77% | -0.84% | 6.30% |
| trend_8_26 + breakout_8 | -2.55% | -10.22% | -12.77% | -3.71% | 28.09% |
| trend_8_26 AND reversion_12 | 0.04% | -6.07% | -12.77% | -0.81% | 6.04% |
| trend_8_26 + reversion_12 | -2.08% | -10.01% | -12.77% | -4.68% | 35.57% |
| trend_8_26 AND volume_26 | 1.79% | 0.09% | -12.77% | -0.21% | 1.57% |
| trend_8_26 + volume_26 | -1.78% | -6.83% | -12.77% | -3.37% | 25.46% |
| momentum_26 AND breakout_8 | -2.64% | -8.96% | -12.77% | -0.88% | 6.56% |
| momentum_26 + breakout_8 | -3.45% | -11.24% | -12.77% | -3.59% | 27.17% |
| momentum_26 AND reversion_12 | -3.16% | -8.69% | -12.77% | -0.77% | 5.77% |
| momentum_26 + reversion_12 | -3.01% | -10.85% | -12.77% | -4.56% | 34.65% |
| momentum_26 AND volume_26 | 1.75% | 0.06% | -12.77% | -0.18% | 1.31% |
| momentum_26 + volume_26 | -2.69% | -7.69% | -12.77% | -3.25% | 24.54% |
| breakout_8 AND reversion_12 | 0.00% | 0.00% | -12.77% | -0.00% | 0.00% |
| breakout_8 + reversion_12 | -3.13% | -14.80% | -12.77% | -2.77% | 20.87% |
| breakout_8 AND volume_26 | 0.66% | -0.18% | -12.77% | -0.07% | 0.52% |
| breakout_8 + volume_26 | -2.83% | -11.80% | -12.77% | -1.43% | 10.77% |
| reversion_12 AND volume_26 | -0.54% | -5.03% | -12.77% | -0.70% | 5.25% |
| reversion_12 + volume_26 | -2.40% | -12.15% | -12.77% | -2.42% | 18.25% |
| ema_12_26 | -1.88% | -3.52% | -12.77% | -5.11% | 38.85% |
| macd_12_26_9 | 1.35% | -1.17% | -12.77% | -3.09% | 23.36% |
| rsi_14_recovery | -0.17% | -6.26% | -12.77% | -0.53% | 3.94% |
| bollinger_20_reentry | 0.57% | -5.57% | -12.77% | -0.53% | 3.94% |
| donchian_20 | -1.16% | -4.82% | -12.77% | -0.60% | 4.46% |
| atr_14_breakout | -1.46% | -7.48% | -12.77% | -0.56% | 4.20% |
| session_vwap | -1.40% | -14.16% | -12.77% | -6.05% | 46.19% |
| obv_20 | -5.12% | -14.22% | -12.77% | -2.54% | 19.16% |
| stochastic_14_3_recovery | -2.10% | -12.96% | -12.77% | -0.98% | 7.35% |
| mfi_14_recovery | 1.96% | -1.00% | -12.77% | -0.25% | 1.84% |
| adx_14_trend | -2.02% | -4.05% | -12.77% | -1.12% | 8.40% |
| aroon_25_trend | -0.29% | -3.58% | -12.77% | -1.43% | 10.76% |
| cci_20_momentum | -4.55% | -9.24% | -12.77% | -1.75% | 13.12% |
| williams_14_recovery | 0.05% | -8.78% | -12.77% | -0.77% | 5.77% |
| cmf_20_accumulation | -4.04% | -10.65% | -12.77% | -2.16% | 16.27% |
| chaikin_3_10 | -6.27% | -14.90% | -12.77% | -3.71% | 28.08% |
| roc_10_momentum | -1.68% | -6.91% | -12.77% | -1.64% | 12.34% |
| trix_15_trend | -1.76% | -5.80% | -12.77% | -3.95% | 29.92% |
| keltner_20_breakout | -2.87% | -5.29% | -12.77% | -0.35% | 2.62% |
| opening_range_30m | 6.75% | 1.93% | -12.77% | -3.13% | 23.62% |

동일 구간·초기 자금, 종료 시 청산 비용 포함. 노출 맞춤은 사후 설명용이며 v2 실제 계좌 성과가 아닙니다.
[낙폭 분해·비용 영향·전체 구간](CAT/comparison.json)

[v1 전체 기록](CAT/accounts.json) · [v2 전체 기록](CAT/accounts-v2.json)

## WMT 계좌

| 모델 | 전략 | 평가액 USD | 손익 USD | 최근 매매·이유 |
|---|---|---:|---:|---|
| v1 | cash | 10000.00 | 0.00 | 대기 /  / 새 신호 대기 |
| v1 | buy_hold | 9991.86 | -8.14 | buy /  / buy_hold: prior completed bar target 100%; next bar open simulation |
| v1 | trend_8_26 | 9791.85 | -208.15 | sell /  / trend_8_26: prior completed bar target 0%; next bar open simulation |
| v1 | momentum_26 | 9801.37 | -198.63 | sell /  / momentum_26: prior completed bar target 0%; next bar open simulation |
| v1 | breakout_8 | 9728.67 | -271.33 | sell /  / breakout_8: prior completed bar target 0%; next bar open simulation |
| v1 | reversion_12 | 9716.50 | -283.50 | sell /  / reversion_12: prior completed bar target 0%; next bar open simulation |
| v1 | volume_26 | 9755.08 | -244.92 | sell /  / volume_26: prior completed bar target 0%; next bar open simulation |
| v1 | trend_8_26 AND momentum_26 | 9811.64 | -188.36 | sell /  / trend_8_26 AND momentum_26: prior completed bar target 0%; next bar open simulation |
| v1 | trend_8_26 + momentum_26 | 9796.64 | -203.36 | sell /  / trend_8_26 + momentum_26: prior completed bar target 0%; next bar open simulation |
| v1 | trend_8_26 AND breakout_8 | 9854.29 | -145.71 | sell /  / trend_8_26 AND breakout_8: prior completed bar target 0%; next bar open simulation |
| v1 | trend_8_26 + breakout_8 | 9760.28 | -239.72 | sell /  / trend_8_26 + breakout_8: prior completed bar target 0%; next bar open simulation |
| v1 | trend_8_26 AND reversion_12 | 9798.51 | -201.49 | sell /  / trend_8_26 AND reversion_12: prior completed bar target 0%; next bar open simulation |
| v1 | trend_8_26 + reversion_12 | 9793.37 | -206.63 | sell /  / trend_8_26 + reversion_12: prior completed bar target 0%; next bar open simulation |
| v1 | trend_8_26 AND volume_26 | 9837.96 | -162.04 | sell /  / trend_8_26 AND volume_26: prior completed bar target 0%; next bar open simulation |
| v1 | trend_8_26 + volume_26 | 9773.64 | -226.36 | sell /  / trend_8_26 + volume_26: prior completed bar target 0%; next bar open simulation |
| v1 | momentum_26 AND breakout_8 | 9816.19 | -183.81 | sell /  / momentum_26 AND breakout_8: prior completed bar target 0%; next bar open simulation |
| v1 | momentum_26 + breakout_8 | 9823.93 | -176.07 | sell /  / momentum_26 + breakout_8: prior completed bar target 0%; next bar open simulation |
| v1 | momentum_26 AND reversion_12 | 9935.88 | -64.12 | sell /  / momentum_26 AND reversion_12: prior completed bar target 0%; next bar open simulation |
| v1 | momentum_26 + reversion_12 | 9856.92 | -143.08 | sell /  / momentum_26 + reversion_12: prior completed bar target 0%; next bar open simulation |
| v1 | momentum_26 AND volume_26 | 9905.94 | -94.06 | sell /  / momentum_26 AND volume_26: prior completed bar target 0%; next bar open simulation |
| v1 | momentum_26 + volume_26 | 9817.50 | -182.50 | sell /  / momentum_26 + volume_26: prior completed bar target 0%; next bar open simulation |
| v1 | breakout_8 AND reversion_12 | 10000.00 | 0.00 | 대기 /  / 새 신호 대기 |
| v1 | breakout_8 + reversion_12 | 9761.44 | -238.56 | sell /  / breakout_8 + reversion_12: prior completed bar target 0%; next bar open simulation |
| v1 | breakout_8 AND volume_26 | 9850.09 | -149.91 | sell /  / breakout_8 AND volume_26: prior completed bar target 0%; next bar open simulation |
| v1 | breakout_8 + volume_26 | 9741.88 | -258.12 | sell /  / breakout_8 + volume_26: prior completed bar target 0%; next bar open simulation |
| v1 | reversion_12 AND volume_26 | 9905.10 | -94.90 | sell /  / reversion_12 AND volume_26: prior completed bar target 0%; next bar open simulation |
| v1 | reversion_12 + volume_26 | 9774.73 | -225.27 | sell /  / reversion_12 + volume_26: prior completed bar target 0%; next bar open simulation |
| v1 | ema_12_26 | 9906.58 | -93.42 | sell /  / EMA12 > EMA26; 조건 미충족; EMA12=118.808, EMA26=118.852 |
| v1 | macd_12_26_9 | 9985.46 | -14.54 | sell /  / MACD > 신호선 그리고 MACD > 0; 조건 미충족; MACD=0.122825, signal9=0.127837 |
| v1 | rsi_14_recovery | 10000.00 | 0.00 | 대기 /  / 새 신호 대기 |
| v1 | bollinger_20_reentry | 9901.04 | -98.96 | sell /  / 직전 종가 < 직전 하단밴드, 현재 하단밴드 <= 종가 <= SMA20 (한 봉 목표); 조건 미충족; close=118.132, lower20=117.91, SMA20=118.808, previous_lower20=118.006 |
| v1 | donchian_20 | 9935.97 | -64.03 | sell /  / 종가 > 현재 봉을 제외한 직전 20봉 최고가; 조건 미충족; close=119.52, prior_high20=120.5 |
| v1 | atr_14_breakout | 9915.82 | -84.18 | sell /  / 종가 > 직전 종가 + 직전 ATR14 그리고 종가 > EMA26; 조건 미충족; close=119.52, threshold=120.186, prior_ATR14=0.395874, EMA26=118.952 |
| v1 | session_vwap | 9838.24 | -161.76 | sell /  / 종가 > 뉴욕 거래일별 누적 전형가격 VWAP; 조건 미충족; close=118.71, session_VWAP=118.72, session_volume=1.73369e+07 |
| v1 | obv_20 | 9857.61 | -142.39 | sell /  / OBV > OBV의 SMA20 그리고 종가 > EMA26; 조건 미충족; OBV=1.6238e+07, OBV_SMA20=1.74966e+07, close=118.945, EMA26=118.951 |
| v1 | stochastic_14_3_recovery | 9774.88 | -225.12 | buy /  / 직전 %K14 < 20에서 %K14가 %D3 상향 돌파 (한 봉 목표); 조건 충족; K14=22.4027, D3=10.8235, previous_K14=4.39043, previous_D3=5.54718 |
| v1 | mfi_14_recovery | 9971.18 | -28.82 | buy /  / 직전 MFI14 < 20, 현재 MFI14 >= 20 (한 봉 목표); 조건 충족; MFI14=20.4345, previous_MFI14=16.1658 |
| v1 | adx_14_trend | 9991.69 | -8.31 | sell /  / Wilder ADX14 >= 25 그리고 +DI14 > -DI14; 조건 미충족; ADX14=24.5142, plus_DI14=24.7537, minus_DI14=21.6519 |
| v1 | aroon_25_trend | 9947.63 | -52.37 | sell /  / Aroon25 Up > 70 그리고 Down < 30 (동률이면 최신 극값); 조건 미충족; Aroon_up=68, Aroon_down=4 |
| v1 | cci_20_momentum | 9772.81 | -227.19 | sell /  / CCI20 > 100 (전형가격·평균절대편차); 조건 미충족; CCI20=38.8365 |
| v1 | williams_14_recovery | 9882.52 | -117.48 | buy /  / 직전 Williams %R14 < -80, 현재 >= -80 (한 봉 목표); 조건 충족; Williams_R14=-77.5973, previous_R14=-95.6096 |
| v1 | cmf_20_accumulation | 9898.70 | -101.30 | sell /  / Chaikin Money Flow20 > 0.1; 조건 미충족; CMF20=0.0888031, volume20=1.50234e+07 |
| v1 | chaikin_3_10 | 9762.96 | -237.04 | sell /  / ADL의 EMA3 - EMA10 > 0 그리고 종가 > EMA26; 조건 미충족; Chaikin3_10=-178256, ADL=1.4762e+07, close=119.52, EMA26=118.952 |
| v1 | roc_10_momentum | 10000.00 | 0.00 | 대기 /  / 새 신호 대기 |
| v1 | trix_15_trend | 9708.65 | -291.35 | sell /  / 15봉 삼중 EMA의 1봉 변화율 TRIX > 0 그리고 종가 > EMA26; 조건 미충족; TRIX15_percent=0.0142754, close=118.77, EMA26=118.947 |
| v1 | keltner_20_breakout | 9935.97 | -64.03 | sell /  / 종가 > EMA20 + 2 x Wilder ATR14; 조건 미충족; close=119.52, upper_Keltner=119.83, EMA20=119.013, ATR14=0.408312 |
| v1 | opening_range_30m | 9927.51 | -72.49 | sell /  / 뉴욕 09:30·09:45 두 완료 봉 최고가를 10:00 이후 종가가 돌파; 조건 미충족; close=118.85, opening_high=119.14 |
| v2 | cash | 10000.00 | 0.00 | 대기 /  / 새 신호 대기 |
| v2 | buy_hold | 10586.28 | 586.28 | buy / partial / 직전 완료 봉 목표 비중 100%; 다음 봉 시가 가정 |
| v2 | trend_8_26 | 10187.81 | 187.81 | sell / filled / 직전 완료 봉 목표 비중 0%; 다음 봉 시가 가정 |
| v2 | momentum_26 | 10200.51 | 200.51 | sell / filled / 직전 완료 봉 목표 비중 0%; 다음 봉 시가 가정 |
| v2 | breakout_8 | 9682.65 | -317.35 | sell / filled / 직전 완료 봉 목표 비중 0%; 다음 봉 시가 가정 |
| v2 | reversion_12 | 9613.11 | -386.89 | sell / filled / 직전 완료 봉 목표 비중 0%; 다음 봉 시가 가정 |
| v2 | volume_26 | 9711.50 | -288.50 | sell / filled / 직전 완료 봉 목표 비중 0%; 다음 봉 시가 가정 |
| v2 | trend_8_26 AND momentum_26 | 10206.36 | 206.36 | sell / filled / 직전 완료 봉 목표 비중 0%; 다음 봉 시가 가정 |
| v2 | trend_8_26 + momentum_26 | 10194.13 | 194.13 | sell / filled / 직전 완료 봉 목표 비중 0%; 다음 봉 시가 가정 |
| v2 | trend_8_26 AND breakout_8 | 9935.59 | -64.41 | sell / filled / 직전 완료 봉 목표 비중 0%; 다음 봉 시가 가정 |
| v2 | trend_8_26 + breakout_8 | 9932.48 | -67.52 | sell / filled / 직전 완료 봉 목표 비중 0%; 다음 봉 시가 가정 |
| v2 | trend_8_26 AND reversion_12 | 9603.42 | -396.58 | sell / filled / 직전 완료 봉 목표 비중 0%; 다음 봉 시가 가정 |
| v2 | trend_8_26 + reversion_12 | 9939.52 | -60.48 | sell / filled / 직전 완료 봉 목표 비중 0%; 다음 봉 시가 가정 |
| v2 | trend_8_26 AND volume_26 | 9784.10 | -215.90 | sell / filled / 직전 완료 봉 목표 비중 0%; 다음 봉 시가 가정 |
| v2 | trend_8_26 + volume_26 | 9948.42 | -51.58 | sell / filled / 직전 완료 봉 목표 비중 0%; 다음 봉 시가 가정 |
| v2 | momentum_26 AND breakout_8 | 9773.67 | -226.33 | sell / filled / 직전 완료 봉 목표 비중 0%; 다음 봉 시가 가정 |
| v2 | momentum_26 + breakout_8 | 10001.62 | 1.62 | sell / filled / 직전 완료 봉 목표 비중 0%; 다음 봉 시가 가정 |
| v2 | momentum_26 AND reversion_12 | 9759.91 | -240.09 | sell / filled / 직전 완료 봉 목표 비중 0%; 다음 봉 시가 가정 |
| v2 | momentum_26 + reversion_12 | 10050.58 | 50.58 | sell / filled / 직전 완료 봉 목표 비중 0%; 다음 봉 시가 가정 |
| v2 | momentum_26 AND volume_26 | 9814.68 | -185.32 | sell / filled / 직전 완료 봉 목표 비중 0%; 다음 봉 시가 가정 |
| v2 | momentum_26 + volume_26 | 9996.47 | -3.53 | sell / filled / 직전 완료 봉 목표 비중 0%; 다음 봉 시가 가정 |
| v2 | breakout_8 AND reversion_12 | 10000.00 | 0.00 | 대기 /  / 새 신호 대기 |
| v2 | breakout_8 + reversion_12 | 9709.80 | -290.20 | sell / filled / 직전 완료 봉 목표 비중 0%; 다음 봉 시가 가정 |
| v2 | breakout_8 AND volume_26 | 9795.19 | -204.81 | sell / filled / 직전 완료 봉 목표 비중 0%; 다음 봉 시가 가정 |
| v2 | breakout_8 + volume_26 | 9698.42 | -301.58 | sell / filled / 직전 완료 봉 목표 비중 0%; 다음 봉 시가 가정 |
| v2 | reversion_12 AND volume_26 | 9912.80 | -87.20 | sell / filled / 직전 완료 봉 목표 비중 0%; 다음 봉 시가 가정 |
| v2 | reversion_12 + volume_26 | 9702.67 | -297.33 | sell / filled / 직전 완료 봉 목표 비중 0%; 다음 봉 시가 가정 |
| v2 | ema_12_26 | 9902.61 | -97.39 | sell / filled / EMA12 > EMA26; 조건 미충족; EMA12=118.808, EMA26=118.852; 직전 완료 봉 목표를 다음 봉 시가에 모의 적용 |
| v2 | macd_12_26_9 | 9981.46 | -18.54 | sell / filled / MACD > 신호선 그리고 MACD > 0; 조건 미충족; MACD=0.122825, signal9=0.127837; 직전 완료 봉 목표를 다음 봉 시가에 모의 적용 |
| v2 | rsi_14_recovery | 10000.00 | 0.00 | 대기 /  / 새 신호 대기 |
| v2 | bollinger_20_reentry | 9897.08 | -102.92 | sell / filled / 직전 종가 < 직전 하단밴드, 현재 하단밴드 <= 종가 <= SMA20 (한 봉 목표); 조건 미충족; close=118.132, lower20=117.91, SMA20=118.808, previous_lower20=118.006; 직전 완료 봉 목표를 다음 봉 시가에 모의 적용 |
| v2 | donchian_20 | 9933.99 | -66.01 | sell / filled / 종가 > 현재 봉을 제외한 직전 20봉 최고가; 조건 미충족; close=119.52, prior_high20=120.5; 직전 완료 봉 목표를 다음 봉 시가에 모의 적용 |
| v2 | atr_14_breakout | 9911.85 | -88.15 | sell / filled / 종가 > 직전 종가 + 직전 ATR14 그리고 종가 > EMA26; 조건 미충족; close=119.52, threshold=120.186, prior_ATR14=0.395874, EMA26=118.952; 직전 완료 봉 목표를 다음 봉 시가에 모의 적용 |
| v2 | session_vwap | 9826.44 | -173.56 | sell / filled / 종가 > 뉴욕 거래일별 누적 전형가격 VWAP; 조건 미충족; close=118.71, session_VWAP=118.72, session_volume=1.73369e+07; 직전 완료 봉 목표를 다음 봉 시가에 모의 적용 |
| v2 | obv_20 | 9847.76 | -152.24 | sell / filled / OBV > OBV의 SMA20 그리고 종가 > EMA26; 조건 미충족; OBV=1.6238e+07, OBV_SMA20=1.74966e+07, close=118.945, EMA26=118.951; 직전 완료 봉 목표를 다음 봉 시가에 모의 적용 |
| v2 | stochastic_14_3_recovery | 9766.09 | -233.91 | buy / partial / 직전 %K14 < 20에서 %K14가 %D3 상향 돌파 (한 봉 목표); 조건 충족; K14=22.4027, D3=10.8235, previous_K14=4.39043, previous_D3=5.54718; 직전 완료 봉 목표를 다음 봉 시가에 모의 적용 |
| v2 | mfi_14_recovery | 9970.18 | -29.82 | buy / partial / 직전 MFI14 < 20, 현재 MFI14 >= 20 (한 봉 목표); 조건 충족; MFI14=20.4345, previous_MFI14=16.1658; 직전 완료 봉 목표를 다음 봉 시가에 모의 적용 |
| v2 | adx_14_trend | 9989.70 | -10.30 | sell / filled / Wilder ADX14 >= 25 그리고 +DI14 > -DI14; 조건 미충족; ADX14=24.5142, plus_DI14=24.7537, minus_DI14=21.6519; 직전 완료 봉 목표를 다음 봉 시가에 모의 적용 |
| v2 | aroon_25_trend | 9943.65 | -56.35 | sell / filled / Aroon25 Up > 70 그리고 Down < 30 (동률이면 최신 극값); 조건 미충족; Aroon_up=68, Aroon_down=4; 직전 완료 봉 목표를 다음 봉 시가에 모의 적용 |
| v2 | cci_20_momentum | 9766.95 | -233.05 | sell / filled / CCI20 > 100 (전형가격·평균절대편차); 조건 미충족; CCI20=38.8365; 직전 완료 봉 목표를 다음 봉 시가에 모의 적용 |
| v2 | williams_14_recovery | 9877.58 | -122.42 | buy / partial / 직전 Williams %R14 < -80, 현재 >= -80 (한 봉 목표); 조건 충족; Williams_R14=-77.5973, previous_R14=-95.6096; 직전 완료 봉 목표를 다음 봉 시가에 모의 적용 |
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
| buy_hold | 10.58% | 10.11% | 10.11% | 10.11% | 100.00% |
| trend_8_26 | 7.36% | 3.81% | 10.11% | 6.96% | 69.55% |
| momentum_26 | 9.58% | 3.32% | 10.11% | 7.09% | 70.87% |
| breakout_8 | 6.12% | -9.92% | 10.11% | 2.48% | 25.20% |
| reversion_12 | 3.71% | -8.18% | 10.11% | 1.83% | 18.64% |
| volume_26 | 0.01% | -6.09% | 10.11% | 0.56% | 5.77% |
| trend_8_26 AND momentum_26 | 7.80% | 2.50% | 10.11% | 6.34% | 63.52% |
| trend_8_26 + momentum_26 | 8.47% | 3.57% | 10.11% | 7.03% | 70.21% |
| trend_8_26 AND breakout_8 | 6.59% | -6.43% | 10.11% | 2.06% | 21.00% |
| trend_8_26 + breakout_8 | 6.75% | -3.29% | 10.11% | 4.70% | 47.38% |
| trend_8_26 AND reversion_12 | -0.24% | -6.33% | 10.11% | 0.72% | 7.35% |
| trend_8_26 + reversion_12 | 5.56% | -1.74% | 10.11% | 4.37% | 44.10% |
| trend_8_26 AND volume_26 | -0.30% | -3.19% | 10.11% | 0.26% | 2.62% |
| trend_8_26 + volume_26 | 3.66% | -0.84% | 10.11% | 3.72% | 37.67% |
| momentum_26 AND breakout_8 | 6.62% | -7.18% | 10.11% | 2.25% | 22.83% |
| momentum_26 + breakout_8 | 7.85% | -2.70% | 10.11% | 4.77% | 48.04% |
| momentum_26 AND reversion_12 | 1.24% | -4.94% | 10.11% | 0.77% | 7.87% |
| momentum_26 + reversion_12 | 6.64% | 0.11% | 10.11% | 4.44% | 44.75% |
| momentum_26 AND volume_26 | 1.58% | -3.01% | 10.11% | 0.31% | 3.15% |
| momentum_26 + volume_26 | 4.72% | -1.07% | 10.11% | 3.79% | 38.32% |
| breakout_8 AND reversion_12 | 0.00% | 0.00% | 10.11% | 0.00% | 0.00% |
| breakout_8 + reversion_12 | 4.93% | -8.28% | 10.11% | 2.16% | 21.92% |
| breakout_8 AND volume_26 | 0.78% | -2.14% | 10.11% | 0.20% | 2.10% |
| breakout_8 + volume_26 | 3.04% | -7.82% | 10.11% | 1.52% | 15.49% |
| reversion_12 AND volume_26 | -1.05% | -3.51% | 10.11% | 0.18% | 1.84% |
| reversion_12 + volume_26 | 1.85% | -6.56% | 10.11% | 1.20% | 12.21% |
| ema_12_26 | 11.20% | 9.81% | 10.11% | 7.28% | 72.70% |
| macd_12_26_9 | 8.67% | 4.64% | 10.11% | 3.58% | 36.22% |
| rsi_14_recovery | -0.25% | -1.50% | 10.11% | 0.08% | 0.79% |
| bollinger_20_reentry | 1.21% | -2.13% | 10.11% | 0.20% | 2.10% |
| donchian_20 | 4.55% | -7.44% | 10.11% | 1.26% | 12.86% |
| atr_14_breakout | -0.90% | -10.40% | 10.11% | 0.72% | 7.35% |
| session_vwap | 9.44% | -0.64% | 10.11% | 5.62% | 56.43% |
| obv_20 | 10.62% | 3.00% | 10.11% | 5.57% | 55.91% |
| stochastic_14_3_recovery | 1.07% | -8.63% | 10.11% | 0.62% | 6.30% |
| mfi_14_recovery | -0.06% | -1.32% | 10.11% | 0.08% | 0.79% |
| adx_14_trend | 8.73% | 6.47% | 10.11% | 4.95% | 49.87% |
| aroon_25_trend | 5.98% | 0.77% | 10.11% | 3.24% | 32.81% |
| cci_20_momentum | 5.80% | -2.73% | 10.11% | 3.13% | 31.76% |
| williams_14_recovery | 0.01% | -8.05% | 10.11% | 0.51% | 5.25% |
| cmf_20_accumulation | 9.05% | -0.16% | 10.11% | 3.55% | 35.96% |
| chaikin_3_10 | 9.32% | 0.51% | 10.11% | 5.14% | 51.71% |
| roc_10_momentum | -0.29% | -4.79% | 10.11% | 1.36% | 13.91% |
| trix_15_trend | 10.97% | 6.86% | 10.11% | 6.48% | 64.83% |
| keltner_20_breakout | 6.59% | 0.08% | 10.11% | 2.61% | 26.51% |
| opening_range_30m | 9.76% | 4.80% | 10.11% | 3.55% | 35.96% |

동일 구간·초기 자금, 종료 시 청산 비용 포함. 노출 맞춤은 사후 설명용이며 v2 실제 계좌 성과가 아닙니다.
[낙폭 분해·비용 영향·전체 구간](WMT/comparison.json)

[v1 전체 기록](WMT/accounts.json) · [v2 전체 기록](WMT/accounts-v2.json)
