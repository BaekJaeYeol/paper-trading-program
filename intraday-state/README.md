# 모의투자 운영 현황

[PC·서버 장애 진단과 복구 방법](https://github.com/BaekJaeYeol/paper-trading-program/blob/main/investment-lab/docs/failure-recovery.md)

이번 실행 복구: {}

완료 봉 확인 주기: 기록 8/15회 · 기록 없는 예정 7회 · 아직 판정 전 11회 · 주의: 예약 시작 지연 또는 실행·저장 누락을 확인하세요.

[주기 판정 기준](https://github.com/BaekJaeYeol/paper-trading-program/blob/main/investment-lab/docs/session-coverage.md)

최근 확인: 2026-10-20T17:37:00.426362+00:00 (UTC)
다음 15분 확인 목표 (세션 실행 중에만 적용): 2026-10-20T17:52:00+00:00 (UTC, 실행 지연 가능)

실제 주문 없음. v1 기존 계좌와 v2 새 계좌의 시작일이 다르므로 수익률을 직접 우열 비교하지 마세요.
v2는 다음 봉 시가에 비용·스프레드·직전 거래량 제한을 적용한 가상 체결입니다. 미체결 잔량은 만료됩니다.

| 종목 | 상태 | 최근 성공 UTC | 마지막 완료 봉 UTC | 이번 새 봉 |
|---|---|---|---|---|
| SPY | updated | 2026-10-20T17:37:00.426362+00:00 | 2026-10-20T17:15:00+00:00 | 1 |
| QQQ | updated | 2026-10-20T17:37:00.426362+00:00 | 2026-10-20T17:15:00+00:00 | 1 |
| IWM | updated | 2026-10-20T17:37:00.426362+00:00 | 2026-10-20T17:15:00+00:00 | 1 |
| DIA | updated | 2026-10-20T17:37:00.426362+00:00 | 2026-10-20T17:15:00+00:00 | 1 |
| MSFT | updated | 2026-10-20T17:37:00.426362+00:00 | 2026-10-20T17:15:00+00:00 | 1 |
| JPM | updated | 2026-10-20T17:37:00.426362+00:00 | 2026-10-20T17:15:00+00:00 | 1 |
| XOM | updated | 2026-10-20T17:37:00.426362+00:00 | 2026-10-20T17:15:00+00:00 | 1 |
| JNJ | updated | 2026-10-20T17:37:00.426362+00:00 | 2026-10-20T17:15:00+00:00 | 1 |
| CAT | updated | 2026-10-20T17:37:00.426362+00:00 | 2026-10-20T17:15:00+00:00 | 1 |
| WMT | updated | 2026-10-20T17:37:00.426362+00:00 | 2026-10-20T17:15:00+00:00 | 1 |

이번 실행 소요: 47.13초
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
| v1 | buy_hold | 9932.66 | -67.34 | buy /  / buy_hold: prior completed bar target 100%; next bar open simulation |
| v1 | trend_8_26 | 9827.79 | -172.21 | buy /  / trend_8_26: prior completed bar target 100%; next bar open simulation |
| v1 | momentum_26 | 9760.70 | -239.30 | buy /  / momentum_26: prior completed bar target 100%; next bar open simulation |
| v1 | breakout_8 | 9752.40 | -247.60 | sell /  / breakout_8: prior completed bar target 0%; next bar open simulation |
| v1 | reversion_12 | 9793.61 | -206.39 | sell /  / reversion_12: prior completed bar target 0%; next bar open simulation |
| v1 | volume_26 | 9680.53 | -319.47 | sell /  / volume_26: prior completed bar target 0%; next bar open simulation |
| v1 | trend_8_26 AND momentum_26 | 9761.48 | -238.52 | buy /  / trend_8_26 AND momentum_26: prior completed bar target 100%; next bar open simulation |
| v1 | trend_8_26 + momentum_26 | 9794.18 | -205.82 | buy /  / trend_8_26 + momentum_26: prior completed bar target 100%; next bar open simulation |
| v1 | trend_8_26 AND breakout_8 | 9859.41 | -140.59 | sell /  / trend_8_26 AND breakout_8: prior completed bar target 0%; next bar open simulation |
| v1 | trend_8_26 + breakout_8 | 9829.15 | -170.85 | sell /  / trend_8_26 + breakout_8: prior completed bar target 50%; next bar open simulation |
| v1 | trend_8_26 AND reversion_12 | 9869.55 | -130.45 | sell /  / trend_8_26 AND reversion_12: prior completed bar target 0%; next bar open simulation |
| v1 | trend_8_26 + reversion_12 | 9810.55 | -189.45 | sell /  / trend_8_26 + reversion_12: prior completed bar target 50%; next bar open simulation |
| v1 | trend_8_26 AND volume_26 | 9726.09 | -273.91 | sell /  / trend_8_26 AND volume_26: prior completed bar target 0%; next bar open simulation |
| v1 | trend_8_26 + volume_26 | 9753.82 | -246.18 | sell /  / trend_8_26 + volume_26: prior completed bar target 50%; next bar open simulation |
| v1 | momentum_26 AND breakout_8 | 9831.79 | -168.21 | sell /  / momentum_26 AND breakout_8: prior completed bar target 0%; next bar open simulation |
| v1 | momentum_26 + breakout_8 | 9756.55 | -243.45 | sell /  / momentum_26 + breakout_8: prior completed bar target 50%; next bar open simulation |
| v1 | momentum_26 AND reversion_12 | 9865.74 | -134.26 | sell /  / momentum_26 AND reversion_12: prior completed bar target 0%; next bar open simulation |
| v1 | momentum_26 + reversion_12 | 9816.22 | -183.78 | sell /  / momentum_26 + reversion_12: prior completed bar target 50%; next bar open simulation |
| v1 | momentum_26 AND volume_26 | 9739.63 | -260.37 | sell /  / momentum_26 AND volume_26: prior completed bar target 0%; next bar open simulation |
| v1 | momentum_26 + volume_26 | 9720.46 | -279.54 | sell /  / momentum_26 + volume_26: prior completed bar target 50%; next bar open simulation |
| v1 | breakout_8 AND reversion_12 | 10000.00 | 0.00 | 대기 /  / 새 신호 대기 |
| v1 | breakout_8 + reversion_12 | 9772.82 | -227.18 | sell /  / breakout_8 + reversion_12: prior completed bar target 0%; next bar open simulation |
| v1 | breakout_8 AND volume_26 | 9878.80 | -121.20 | sell /  / breakout_8 AND volume_26: prior completed bar target 0%; next bar open simulation |
| v1 | breakout_8 + volume_26 | 9735.74 | -264.26 | sell /  / breakout_8 + volume_26: prior completed bar target 0%; next bar open simulation |
| v1 | reversion_12 AND volume_26 | 9861.02 | -138.98 | sell /  / reversion_12 AND volume_26: prior completed bar target 0%; next bar open simulation |
| v1 | reversion_12 + volume_26 | 9736.83 | -263.17 | sell /  / reversion_12 + volume_26: prior completed bar target 0%; next bar open simulation |
| v1 | ema_12_26 | 9793.33 | -206.67 | buy /  / EMA12 > EMA26; 조건 충족; EMA12=767.528, EMA26=767.458 |
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
| v1 | chaikin_3_10 | 9818.17 | -181.83 | sell /  / ADL의 EMA3 - EMA10 > 0 그리고 종가 > EMA26; 조건 미충족; Chaikin3_10=-2.13224e+06, ADL=-9.44662e+06, close=768.655, EMA26=768.743 |
| v1 | roc_10_momentum | 9953.42 | -46.58 | sell /  / 10봉 ROC > 1% 그리고 종가 > EMA26; 조건 미충족; ROC10_percent=0.806376, close=769.45, EMA26=767.181 |
| v1 | trix_15_trend | 9721.22 | -278.78 | buy /  / 15봉 삼중 EMA의 1봉 변화율 TRIX > 0 그리고 종가 > EMA26; 조건 충족; TRIX15_percent=0.0103976, close=768.76, EMA26=768.744 |
| v1 | keltner_20_breakout | 9924.71 | -75.29 | sell /  / 종가 > EMA20 + 2 x Wilder ATR14; 조건 미충족; close=768.93, upper_Keltner=771.837, EMA20=768.595, ATR14=1.6209 |
| v1 | opening_range_30m | 9762.27 | -237.73 | buy /  / 뉴욕 09:30·09:45 두 완료 봉 최고가를 10:00 이후 종가가 돌파; 조건 충족; close=769.1, opening_high=768 |
| v2 | cash | 10000.00 | 0.00 | 대기 /  / 새 신호 대기 |
| v2 | buy_hold | 9861.02 | -138.98 | buy / partial / 직전 완료 봉 목표 비중 100%; 다음 봉 시가 가정 |
| v2 | trend_8_26 | 9709.42 | -290.58 | buy / partial / 직전 완료 봉 목표 비중 100%; 다음 봉 시가 가정 |
| v2 | momentum_26 | 9612.27 | -387.73 | buy / partial / 직전 완료 봉 목표 비중 100%; 다음 봉 시가 가정 |
| v2 | breakout_8 | 9349.72 | -650.28 | sell / filled / 직전 완료 봉 목표 비중 0%; 다음 봉 시가 가정 |
| v2 | reversion_12 | 9327.83 | -672.17 | sell / filled / 직전 완료 봉 목표 비중 0%; 다음 봉 시가 가정 |
| v2 | volume_26 | 9128.87 | -871.13 | sell / filled / 직전 완료 봉 목표 비중 0%; 다음 봉 시가 가정 |
| v2 | trend_8_26 AND momentum_26 | 9619.58 | -380.42 | buy / partial / 직전 완료 봉 목표 비중 100%; 다음 봉 시가 가정 |
| v2 | trend_8_26 + momentum_26 | 9660.72 | -339.28 | buy / partial / 직전 완료 봉 목표 비중 100%; 다음 봉 시가 가정 |
| v2 | trend_8_26 AND breakout_8 | 9681.27 | -318.73 | sell / filled / 직전 완료 봉 목표 비중 0%; 다음 봉 시가 가정 |
| v2 | trend_8_26 + breakout_8 | 9567.74 | -432.26 | sell / filled / 직전 완료 봉 목표 비중 50%; 다음 봉 시가 가정 |
| v2 | trend_8_26 AND reversion_12 | 9761.16 | -238.84 | sell / filled / 직전 완료 봉 목표 비중 0%; 다음 봉 시가 가정 |
| v2 | trend_8_26 + reversion_12 | 9516.26 | -483.74 | sell / filled / 직전 완료 봉 목표 비중 50%; 다음 봉 시가 가정 |
| v2 | trend_8_26 AND volume_26 | 9566.65 | -433.35 | sell / filled / 직전 완료 봉 목표 비중 0%; 다음 봉 시가 가정 |
| v2 | trend_8_26 + volume_26 | 9434.17 | -565.83 | sell / filled / 직전 완료 봉 목표 비중 50%; 다음 봉 시가 가정 |
| v2 | momentum_26 AND breakout_8 | 9611.27 | -388.73 | sell / filled / 직전 완료 봉 목표 비중 0%; 다음 봉 시가 가정 |
| v2 | momentum_26 + breakout_8 | 9480.00 | -520.00 | sell / filled / 직전 완료 봉 목표 비중 50%; 다음 봉 시가 가정 |
| v2 | momentum_26 AND reversion_12 | 9823.55 | -176.45 | sell / filled / 직전 완료 봉 목표 비중 0%; 다음 봉 시가 가정 |
| v2 | momentum_26 + reversion_12 | 9528.41 | -471.59 | sell / filled / 직전 완료 봉 목표 비중 50%; 다음 봉 시가 가정 |
| v2 | momentum_26 AND volume_26 | 9649.38 | -350.62 | sell / filled / 직전 완료 봉 목표 비중 0%; 다음 봉 시가 가정 |
| v2 | momentum_26 + volume_26 | 9426.33 | -573.67 | sell / filled / 직전 완료 봉 목표 비중 50%; 다음 봉 시가 가정 |
| v2 | breakout_8 AND reversion_12 | 10000.00 | 0.00 | 대기 /  / 새 신호 대기 |
| v2 | breakout_8 + reversion_12 | 9377.48 | -622.52 | sell / filled / 직전 완료 봉 목표 비중 0%; 다음 봉 시가 가정 |
| v2 | breakout_8 AND volume_26 | 9808.87 | -191.13 | sell / filled / 직전 완료 봉 목표 비중 0%; 다음 봉 시가 가정 |
| v2 | breakout_8 + volume_26 | 9296.56 | -703.44 | sell / filled / 직전 완료 봉 목표 비중 0%; 다음 봉 시가 가정 |
| v2 | reversion_12 AND volume_26 | 9602.16 | -397.84 | sell / filled / 직전 완료 봉 목표 비중 0%; 다음 봉 시가 가정 |
| v2 | reversion_12 + volume_26 | 9305.31 | -694.69 | sell / filled / 직전 완료 봉 목표 비중 0%; 다음 봉 시가 가정 |
| v2 | ema_12_26 | 9788.44 | -211.56 | buy / partial / EMA12 > EMA26; 조건 충족; EMA12=767.528, EMA26=767.458; 직전 완료 봉 목표를 다음 봉 시가에 모의 적용 |
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
| v2 | chaikin_3_10 | 9810.32 | -189.68 | sell / filled / ADL의 EMA3 - EMA10 > 0 그리고 종가 > EMA26; 조건 미충족; Chaikin3_10=-2.13224e+06, ADL=-9.44662e+06, close=768.655, EMA26=768.743; 직전 완료 봉 목표를 다음 봉 시가에 모의 적용 |
| v2 | roc_10_momentum | 9951.43 | -48.57 | sell / filled / 10봉 ROC > 1% 그리고 종가 > EMA26; 조건 미충족; ROC10_percent=0.806376, close=769.45, EMA26=767.181; 직전 완료 봉 목표를 다음 봉 시가에 모의 적용 |
| v2 | trix_15_trend | 9710.53 | -289.47 | buy / partial / 15봉 삼중 EMA의 1봉 변화율 TRIX > 0 그리고 종가 > EMA26; 조건 충족; TRIX15_percent=0.0103976, close=768.76, EMA26=768.744; 직전 완료 봉 목표를 다음 봉 시가에 모의 적용 |
| v2 | keltner_20_breakout | 9922.73 | -77.27 | sell / filled / 종가 > EMA20 + 2 x Wilder ATR14; 조건 미충족; close=768.93, upper_Keltner=771.837, EMA20=768.595, ATR14=1.6209; 직전 완료 봉 목표를 다음 봉 시가에 모의 적용 |
| v2 | opening_range_30m | 9753.49 | -246.51 | buy / partial / 뉴욕 09:30·09:45 두 완료 봉 최고가를 10:00 이후 종가가 돌파; 조건 충족; close=769.1, opening_high=768; 직전 완료 봉 목표를 다음 봉 시가에 모의 적용 |

### 같은 기간의 비용·노출 비교 (사후 연구)

| 전략 | 비용 전 | 비용 후 | 100% 보유 | 같은 평균 노출 보유 | 평균 노출 |
|---|---:|---:|---:|---:|---:|
| cash | 0.00% | 0.00% | 0.29% | 0.00% | 0.00% |
| buy_hold | 0.71% | 0.29% | 0.29% | 0.29% | 100.00% |
| trend_8_26 | 1.29% | -2.47% | 0.29% | 0.16% | 54.59% |
| momentum_26 | -0.64% | -5.12% | 0.29% | 0.16% | 53.54% |
| breakout_8 | -0.34% | -16.46% | 0.29% | 0.07% | 22.57% |
| reversion_12 | -1.41% | -11.61% | 0.29% | 0.08% | 27.30% |
| volume_26 | -1.26% | -10.73% | 0.29% | 0.03% | 9.45% |
| trend_8_26 AND momentum_26 | 0.34% | -4.19% | 0.29% | 0.14% | 46.72% |
| trend_8_26 + momentum_26 | 0.32% | -3.81% | 0.29% | 0.16% | 54.07% |
| trend_8_26 AND breakout_8 | -0.15% | -11.60% | 0.29% | 0.04% | 13.91% |
| trend_8_26 + breakout_8 | 0.47% | -9.36% | 0.29% | 0.11% | 38.59% |
| trend_8_26 AND reversion_12 | -0.13% | -4.24% | 0.29% | 0.02% | 6.82% |
| trend_8_26 + reversion_12 | -0.07% | -6.97% | 0.29% | 0.12% | 40.95% |
| trend_8_26 AND volume_26 | -1.00% | -6.26% | 0.29% | 0.02% | 5.51% |
| trend_8_26 + volume_26 | 0.01% | -6.70% | 0.29% | 0.09% | 32.03% |
| momentum_26 AND breakout_8 | 0.28% | -11.60% | 0.29% | 0.04% | 15.22% |
| momentum_26 + breakout_8 | -0.49% | -10.97% | 0.29% | 0.11% | 38.06% |
| momentum_26 AND reversion_12 | -0.93% | -5.80% | 0.29% | 0.02% | 7.35% |
| momentum_26 + reversion_12 | -1.02% | -7.85% | 0.29% | 0.12% | 40.42% |
| momentum_26 AND volume_26 | -0.72% | -4.80% | 0.29% | 0.01% | 3.67% |
| momentum_26 + volume_26 | -0.95% | -6.81% | 0.29% | 0.09% | 31.50% |
| breakout_8 AND reversion_12 | 0.00% | 0.00% | 0.29% | 0.00% | 0.00% |
| breakout_8 + reversion_12 | -0.87% | -13.72% | 0.29% | 0.07% | 24.94% |
| breakout_8 AND volume_26 | -0.33% | -2.40% | 0.29% | 0.01% | 1.84% |
| breakout_8 + volume_26 | -0.80% | -12.55% | 0.29% | 0.05% | 16.02% |
| reversion_12 AND volume_26 | -0.87% | -5.34% | 0.29% | 0.01% | 3.94% |
| reversion_12 + volume_26 | -1.33% | -10.99% | 0.29% | 0.05% | 18.38% |
| ema_12_26 | -0.67% | -4.36% | 0.29% | 0.16% | 55.91% |
| macd_12_26_9 | -0.01% | -4.92% | 0.29% | 0.10% | 33.86% |
| rsi_14_recovery | -0.53% | -4.22% | 0.29% | 0.01% | 2.36% |
| bollinger_20_reentry | -1.07% | -6.72% | 0.29% | 0.01% | 3.67% |
| donchian_20 | 0.09% | -7.58% | 0.29% | 0.02% | 7.09% |
| atr_14_breakout | 0.54% | -5.20% | 0.29% | 0.01% | 4.20% |
| session_vwap | 2.18% | -8.01% | 0.29% | 0.14% | 47.77% |
| obv_20 | 0.35% | -6.95% | 0.29% | 0.11% | 37.80% |
| stochastic_14_3_recovery | -0.40% | -14.02% | 0.29% | 0.03% | 9.19% |
| mfi_14_recovery | -0.01% | -3.31% | 0.29% | 0.01% | 2.10% |
| adx_14_trend | 0.32% | -3.40% | 0.29% | 0.08% | 28.08% |
| aroon_25_trend | 0.82% | -2.10% | 0.29% | 0.07% | 25.72% |
| cci_20_momentum | -0.10% | -8.53% | 0.29% | 0.07% | 23.10% |
| williams_14_recovery | -0.58% | -10.49% | 0.29% | 0.02% | 6.56% |
| cmf_20_accumulation | 2.18% | -1.61% | 0.29% | 0.13% | 43.31% |
| chaikin_3_10 | 1.88% | -4.74% | 0.29% | 0.11% | 39.63% |
| roc_10_momentum | -0.13% | -0.97% | 0.29% | 0.00% | 1.05% |
| trix_15_trend | -0.29% | -4.79% | 0.29% | 0.12% | 41.99% |
| keltner_20_breakout | -0.26% | -4.36% | 0.29% | 0.03% | 11.55% |
| opening_range_30m | 0.10% | -6.40% | 0.29% | 0.10% | 35.70% |

동일 구간·초기 자금, 종료 시 청산 비용 포함. 노출 맞춤은 사후 설명용이며 v2 실제 계좌 성과가 아닙니다.
[낙폭 분해·비용 영향·전체 구간](SPY/comparison.json)

[v1 전체 기록](SPY/accounts.json) · [v2 전체 기록](SPY/accounts-v2.json)

## QQQ 계좌

| 모델 | 전략 | 평가액 USD | 손익 USD | 최근 매매·이유 |
|---|---|---:|---:|---|
| v1 | cash | 10000.00 | 0.00 | 대기 /  / 새 신호 대기 |
| v1 | buy_hold | 9895.88 | -104.12 | buy /  / buy_hold: prior completed bar target 100%; next bar open simulation |
| v1 | trend_8_26 | 9828.61 | -171.39 | sell /  / trend_8_26: prior completed bar target 0%; next bar open simulation |
| v1 | momentum_26 | 9617.56 | -382.44 | sell /  / momentum_26: prior completed bar target 0%; next bar open simulation |
| v1 | breakout_8 | 9742.42 | -257.58 | sell /  / breakout_8: prior completed bar target 0%; next bar open simulation |
| v1 | reversion_12 | 9809.49 | -190.51 | buy /  / reversion_12: prior completed bar target 100%; next bar open simulation |
| v1 | volume_26 | 9624.14 | -375.86 | sell /  / volume_26: prior completed bar target 0%; next bar open simulation |
| v1 | trend_8_26 AND momentum_26 | 9890.12 | -109.88 | sell /  / trend_8_26 AND momentum_26: prior completed bar target 0%; next bar open simulation |
| v1 | trend_8_26 + momentum_26 | 9742.06 | -257.94 | sell /  / trend_8_26 + momentum_26: prior completed bar target 0%; next bar open simulation |
| v1 | trend_8_26 AND breakout_8 | 9989.91 | -10.09 | sell /  / trend_8_26 AND breakout_8: prior completed bar target 0%; next bar open simulation |
| v1 | trend_8_26 + breakout_8 | 9824.62 | -175.38 | sell /  / trend_8_26 + breakout_8: prior completed bar target 0%; next bar open simulation |
| v1 | trend_8_26 AND reversion_12 | 9902.56 | -97.44 | sell /  / trend_8_26 AND reversion_12: prior completed bar target 0%; next bar open simulation |
| v1 | trend_8_26 + reversion_12 | 9838.82 | -161.18 | sell /  / trend_8_26 + reversion_12: prior completed bar target 50%; next bar open simulation |
| v1 | trend_8_26 AND volume_26 | 9864.33 | -135.67 | sell /  / trend_8_26 AND volume_26: prior completed bar target 0%; next bar open simulation |
| v1 | trend_8_26 + volume_26 | 9725.78 | -274.22 | sell /  / trend_8_26 + volume_26: prior completed bar target 0%; next bar open simulation |
| v1 | momentum_26 AND breakout_8 | 9773.97 | -226.03 | sell /  / momentum_26 AND breakout_8: prior completed bar target 0%; next bar open simulation |
| v1 | momentum_26 + breakout_8 | 9679.84 | -320.16 | sell /  / momentum_26 + breakout_8: prior completed bar target 0%; next bar open simulation |
| v1 | momentum_26 AND reversion_12 | 9800.84 | -199.16 | sell /  / momentum_26 AND reversion_12: prior completed bar target 0%; next bar open simulation |
| v1 | momentum_26 + reversion_12 | 9713.29 | -286.71 | sell /  / momentum_26 + reversion_12: prior completed bar target 50%; next bar open simulation |
| v1 | momentum_26 AND volume_26 | 9836.75 | -163.25 | sell /  / momentum_26 AND volume_26: prior completed bar target 0%; next bar open simulation |
| v1 | momentum_26 + volume_26 | 9640.09 | -359.91 | sell /  / momentum_26 + volume_26: prior completed bar target 0%; next bar open simulation |
| v1 | breakout_8 AND reversion_12 | 10000.00 | 0.00 | 대기 /  / 새 신호 대기 |
| v1 | breakout_8 + reversion_12 | 9795.58 | -204.42 | sell /  / breakout_8 + reversion_12: prior completed bar target 50%; next bar open simulation |
| v1 | breakout_8 AND volume_26 | 9947.15 | -52.85 | sell /  / breakout_8 AND volume_26: prior completed bar target 0%; next bar open simulation |
| v1 | breakout_8 + volume_26 | 9702.47 | -297.53 | sell /  / breakout_8 + volume_26: prior completed bar target 0%; next bar open simulation |
| v1 | reversion_12 AND volume_26 | 9907.31 | -92.69 | sell /  / reversion_12 AND volume_26: prior completed bar target 0%; next bar open simulation |
| v1 | reversion_12 + volume_26 | 9755.33 | -244.67 | sell /  / reversion_12 + volume_26: prior completed bar target 50%; next bar open simulation |
| v1 | ema_12_26 | 9663.12 | -336.88 | sell /  / EMA12 > EMA26; 조건 미충족; EMA12=719.14, EMA26=719.146 |
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
| v1 | cmf_20_accumulation | 9619.30 | -380.70 | buy /  / Chaikin Money Flow20 > 0.1; 조건 충족; CMF20=0.152804, volume20=3.24878e+08 |
| v1 | chaikin_3_10 | 9772.35 | -227.65 | sell /  / ADL의 EMA3 - EMA10 > 0 그리고 종가 > EMA26; 조건 미충족; Chaikin3_10=2.03031e+07, ADL=2.77046e+08, close=719.05, EMA26=719.237 |
| v1 | roc_10_momentum | 9990.50 | -9.50 | sell /  / 10봉 ROC > 1% 그리고 종가 > EMA26; 조건 미충족; ROC10_percent=0.483561, close=722.477, EMA26=718.78 |
| v1 | trix_15_trend | 9716.47 | -283.53 | sell /  / 15봉 삼중 EMA의 1봉 변화율 TRIX > 0 그리고 종가 > EMA26; 조건 미충족; TRIX15_percent=0.00323587, close=719.05, EMA26=719.237 |
| v1 | keltner_20_breakout | 9904.16 | -95.84 | sell /  / 종가 > EMA20 + 2 x Wilder ATR14; 조건 미충족; close=723.31, upper_Keltner=723.407, EMA20=718.722, ATR14=2.34265 |
| v1 | opening_range_30m | 9768.26 | -231.74 | buy /  / 뉴욕 09:30·09:45 두 완료 봉 최고가를 10:00 이후 종가가 돌파; 조건 충족; close=718.66, opening_high=716.18 |
| v2 | cash | 10000.00 | 0.00 | 대기 /  / 새 신호 대기 |
| v2 | buy_hold | 9576.00 | -424.00 | buy / partial / 직전 완료 봉 목표 비중 100%; 다음 봉 시가 가정 |
| v2 | trend_8_26 | 9629.88 | -370.12 | sell / filled / 직전 완료 봉 목표 비중 0%; 다음 봉 시가 가정 |
| v2 | momentum_26 | 9511.63 | -488.37 | sell / filled / 직전 완료 봉 목표 비중 0%; 다음 봉 시가 가정 |
| v2 | breakout_8 | 9411.37 | -588.63 | sell / filled / 직전 완료 봉 목표 비중 0%; 다음 봉 시가 가정 |
| v2 | reversion_12 | 9322.42 | -677.58 | buy / partial / 직전 완료 봉 목표 비중 100%; 다음 봉 시가 가정 |
| v2 | volume_26 | 9565.80 | -434.20 | 중단: 손실 한도 / sell / filled / 직전 완료 봉 목표 비중 0%; 다음 봉 시가 가정 |
| v2 | trend_8_26 AND momentum_26 | 9785.10 | -214.90 | sell / filled / 직전 완료 봉 목표 비중 0%; 다음 봉 시가 가정 |
| v2 | trend_8_26 + momentum_26 | 9590.81 | -409.19 | sell / filled / 직전 완료 봉 목표 비중 0%; 다음 봉 시가 가정 |
| v2 | trend_8_26 AND breakout_8 | 9883.87 | -116.13 | sell / filled / 직전 완료 봉 목표 비중 0%; 다음 봉 시가 가정 |
| v2 | trend_8_26 + breakout_8 | 9560.00 | -440.00 | sell / filled / 직전 완료 봉 목표 비중 0%; 다음 봉 시가 가정 |
| v2 | trend_8_26 AND reversion_12 | 9761.15 | -238.85 | sell / filled / 직전 완료 봉 목표 비중 0%; 다음 봉 시가 가정 |
| v2 | trend_8_26 + reversion_12 | 9494.63 | -505.37 | sell / filled / 직전 완료 봉 목표 비중 50%; 다음 봉 시가 가정 |
| v2 | trend_8_26 AND volume_26 | 9698.84 | -301.16 | sell / filled / 직전 완료 봉 목표 비중 0%; 다음 봉 시가 가정 |
| v2 | trend_8_26 + volume_26 | 9329.51 | -670.49 | sell / filled / 직전 완료 봉 목표 비중 0%; 다음 봉 시가 가정 |
| v2 | momentum_26 AND breakout_8 | 9727.76 | -272.24 | sell / filled / 직전 완료 봉 목표 비중 0%; 다음 봉 시가 가정 |
| v2 | momentum_26 + breakout_8 | 9461.38 | -538.62 | sell / filled / 직전 완료 봉 목표 비중 0%; 다음 봉 시가 가정 |
| v2 | momentum_26 AND reversion_12 | 9794.96 | -205.04 | sell / filled / 직전 완료 봉 목표 비중 0%; 다음 봉 시가 가정 |
| v2 | momentum_26 + reversion_12 | 9436.24 | -563.76 | sell / filled / 직전 완료 봉 목표 비중 50%; 다음 봉 시가 가정 |
| v2 | momentum_26 AND volume_26 | 9768.76 | -231.24 | sell / filled / 직전 완료 봉 목표 비중 0%; 다음 봉 시가 가정 |
| v2 | momentum_26 + volume_26 | 9291.55 | -708.45 | sell / filled / 직전 완료 봉 목표 비중 0%; 다음 봉 시가 가정 |
| v2 | breakout_8 AND reversion_12 | 10000.00 | 0.00 | 대기 /  / 새 신호 대기 |
| v2 | breakout_8 + reversion_12 | 9445.59 | -554.41 | sell / filled / 직전 완료 봉 목표 비중 50%; 다음 봉 시가 가정 |
| v2 | breakout_8 AND volume_26 | 9891.45 | -108.55 | sell / filled / 직전 완료 봉 목표 비중 0%; 다음 봉 시가 가정 |
| v2 | breakout_8 + volume_26 | 9281.43 | -718.57 | sell / filled / 직전 완료 봉 목표 비중 0%; 다음 봉 시가 가정 |
| v2 | reversion_12 AND volume_26 | 9547.64 | -452.36 | 중단: 손실 한도 / sell / filled / 직전 완료 봉 목표 비중 0%; 다음 봉 시가 가정 |
| v2 | reversion_12 + volume_26 | 9237.57 | -762.43 | sell / filled / 직전 완료 봉 목표 비중 50%; 다음 봉 시가 가정 |
| v2 | ema_12_26 | 9657.32 | -342.68 | sell / filled / EMA12 > EMA26; 조건 미충족; EMA12=719.14, EMA26=719.146; 직전 완료 봉 목표를 다음 봉 시가에 모의 적용 |
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
| v2 | cmf_20_accumulation | 9606.80 | -393.20 | buy / partial / Chaikin Money Flow20 > 0.1; 조건 충족; CMF20=0.152804, volume20=3.24878e+08; 직전 완료 봉 목표를 다음 봉 시가에 모의 적용 |
| v2 | chaikin_3_10 | 9764.53 | -235.47 | sell / filled / ADL의 EMA3 - EMA10 > 0 그리고 종가 > EMA26; 조건 미충족; Chaikin3_10=2.03031e+07, ADL=2.77046e+08, close=719.05, EMA26=719.237; 직전 완료 봉 목표를 다음 봉 시가에 모의 적용 |
| v2 | roc_10_momentum | 9988.50 | -11.50 | sell / filled / 10봉 ROC > 1% 그리고 종가 > EMA26; 조건 미충족; ROC10_percent=0.483561, close=722.477, EMA26=718.78; 직전 완료 봉 목표를 다음 봉 시가에 모의 적용 |
| v2 | trix_15_trend | 9708.70 | -291.30 | sell / filled / 15봉 삼중 EMA의 1봉 변화율 TRIX > 0 그리고 종가 > EMA26; 조건 미충족; TRIX15_percent=0.00323587, close=719.05, EMA26=719.237; 직전 완료 봉 목표를 다음 봉 시가에 모의 적용 |
| v2 | keltner_20_breakout | 9900.20 | -99.80 | sell / filled / 종가 > EMA20 + 2 x Wilder ATR14; 조건 미충족; close=723.31, upper_Keltner=723.407, EMA20=718.722, ATR14=2.34265; 직전 완료 봉 목표를 다음 봉 시가에 모의 적용 |
| v2 | opening_range_30m | 9761.42 | -238.58 | buy / partial / 뉴욕 09:30·09:45 두 완료 봉 최고가를 10:00 이후 종가가 돌파; 조건 충족; close=718.66, opening_high=716.18; 직전 완료 봉 목표를 다음 봉 시가에 모의 적용 |

### 같은 기간의 비용·노출 비교 (사후 연구)

| 전략 | 비용 전 | 비용 후 | 100% 보유 | 같은 평균 노출 보유 | 평균 노출 |
|---|---:|---:|---:|---:|---:|
| cash | 0.00% | 0.00% | -2.88% | -0.00% | 0.00% |
| buy_hold | -2.47% | -2.88% | -2.88% | -2.88% | 100.00% |
| trend_8_26 | 0.59% | -3.14% | -2.88% | -1.30% | 45.41% |
| momentum_26 | -2.51% | -7.69% | -2.88% | -1.16% | 40.42% |
| breakout_8 | -1.66% | -16.87% | -2.88% | -0.53% | 18.37% |
| reversion_12 | -0.53% | -12.31% | -2.88% | -0.85% | 29.66% |
| volume_26 | -1.17% | -14.68% | -2.88% | -0.46% | 16.01% |
| trend_8_26 AND momentum_26 | 0.37% | -3.36% | -2.88% | -0.99% | 34.38% |
| trend_8_26 + momentum_26 | -0.96% | -5.04% | -2.88% | -1.23% | 42.92% |
| trend_8_26 AND breakout_8 | -0.01% | -8.84% | -2.88% | -0.32% | 11.29% |
| trend_8_26 + breakout_8 | -0.53% | -9.70% | -2.88% | -0.92% | 31.90% |
| trend_8_26 AND reversion_12 | -0.22% | -4.73% | -2.88% | -0.19% | 6.56% |
| trend_8_26 + reversion_12 | 0.04% | -7.26% | -2.88% | -1.08% | 37.54% |
| trend_8_26 AND volume_26 | 0.45% | -4.49% | -2.88% | -0.14% | 4.99% |
| trend_8_26 + volume_26 | -0.29% | -8.91% | -2.88% | -0.88% | 30.71% |
| momentum_26 AND breakout_8 | -0.75% | -9.89% | -2.88% | -0.32% | 11.29% |
| momentum_26 + breakout_8 | -2.08% | -12.21% | -2.88% | -0.84% | 29.40% |
| momentum_26 AND reversion_12 | -1.16% | -6.41% | -2.88% | -0.20% | 6.82% |
| momentum_26 + reversion_12 | -1.52% | -9.66% | -2.88% | -1.01% | 35.04% |
| momentum_26 AND volume_26 | -0.28% | -4.38% | -2.88% | -0.11% | 3.67% |
| momentum_26 + volume_26 | -1.84% | -10.89% | -2.88% | -0.81% | 28.22% |
| breakout_8 AND reversion_12 | 0.00% | 0.00% | -2.88% | -0.00% | 0.00% |
| breakout_8 + reversion_12 | -1.09% | -13.73% | -2.88% | -0.69% | 24.02% |
| breakout_8 AND volume_26 | 0.32% | -2.18% | -2.88% | -0.05% | 1.84% |
| breakout_8 + volume_26 | -1.41% | -14.36% | -2.88% | -0.49% | 17.20% |
| reversion_12 AND volume_26 | -1.31% | -8.11% | -2.88% | -0.24% | 8.40% |
| reversion_12 + volume_26 | -0.84% | -12.96% | -2.88% | -0.66% | 22.84% |
| ema_12_26 | -0.93% | -3.39% | -2.88% | -1.21% | 42.26% |
| macd_12_26_9 | 0.96% | -3.19% | -2.88% | -0.70% | 24.41% |
| rsi_14_recovery | -0.47% | -5.76% | -2.88% | -0.10% | 3.41% |
| bollinger_20_reentry | -0.08% | -6.18% | -2.88% | -0.11% | 3.94% |
| donchian_20 | 0.59% | -4.75% | -2.88% | -0.17% | 5.77% |
| atr_14_breakout | 0.47% | -3.67% | -2.88% | -0.09% | 3.15% |
| session_vwap | -0.08% | -11.54% | -2.88% | -1.37% | 47.51% |
| obv_20 | -1.11% | -9.46% | -2.88% | -0.82% | 28.61% |
| stochastic_14_3_recovery | -0.31% | -11.75% | -2.88% | -0.22% | 7.61% |
| mfi_14_recovery | -1.23% | -3.69% | -2.88% | -0.05% | 1.57% |
| adx_14_trend | -0.11% | -3.00% | -2.88% | -0.62% | 21.52% |
| aroon_25_trend | 1.27% | -2.07% | -2.88% | -0.52% | 18.11% |
| cci_20_momentum | -0.45% | -5.74% | -2.88% | -0.49% | 17.06% |
| williams_14_recovery | -0.63% | -10.91% | -2.88% | -0.20% | 6.82% |
| cmf_20_accumulation | -1.82% | -9.73% | -2.88% | -0.92% | 32.02% |
| chaikin_3_10 | -2.56% | -10.04% | -2.88% | -1.03% | 35.70% |
| roc_10_momentum | -0.00% | -1.67% | -2.88% | -0.12% | 4.20% |
| trix_15_trend | -0.35% | -3.23% | -2.88% | -0.98% | 34.12% |
| keltner_20_breakout | -0.89% | -5.76% | -2.88% | -0.23% | 8.14% |
| opening_range_30m | -1.00% | -7.82% | -2.88% | -0.82% | 28.61% |

동일 구간·초기 자금, 종료 시 청산 비용 포함. 노출 맞춤은 사후 설명용이며 v2 실제 계좌 성과가 아닙니다.
[낙폭 분해·비용 영향·전체 구간](QQQ/comparison.json)

[v1 전체 기록](QQQ/accounts.json) · [v2 전체 기록](QQQ/accounts-v2.json)

## IWM 계좌

| 모델 | 전략 | 평가액 USD | 손익 USD | 최근 매매·이유 |
|---|---|---:|---:|---|
| v1 | cash | 10000.00 | 0.00 | 대기 /  / 새 신호 대기 |
| v1 | buy_hold | 9985.28 | -14.72 | buy /  / buy_hold: prior completed bar target 100%; next bar open simulation |
| v1 | trend_8_26 | 9790.89 | -209.11 | buy /  / trend_8_26: prior completed bar target 100%; next bar open simulation |
| v1 | momentum_26 | 9961.58 | -38.42 | buy /  / momentum_26: prior completed bar target 100%; next bar open simulation |
| v1 | breakout_8 | 9713.59 | -286.41 | sell /  / breakout_8: prior completed bar target 0%; next bar open simulation |
| v1 | reversion_12 | 9786.62 | -213.38 | sell /  / reversion_12: prior completed bar target 0%; next bar open simulation |
| v1 | volume_26 | 9923.29 | -76.71 | sell /  / volume_26: prior completed bar target 0%; next bar open simulation |
| v1 | trend_8_26 AND momentum_26 | 9806.80 | -193.20 | buy /  / trend_8_26 AND momentum_26: prior completed bar target 100%; next bar open simulation |
| v1 | trend_8_26 + momentum_26 | 9875.93 | -124.07 | buy /  / trend_8_26 + momentum_26: prior completed bar target 100%; next bar open simulation |
| v1 | trend_8_26 AND breakout_8 | 9803.67 | -196.33 | sell /  / trend_8_26 AND breakout_8: prior completed bar target 0%; next bar open simulation |
| v1 | trend_8_26 + breakout_8 | 9752.33 | -247.67 | sell /  / trend_8_26 + breakout_8: prior completed bar target 50%; next bar open simulation |
| v1 | trend_8_26 AND reversion_12 | 9827.31 | -172.69 | sell /  / trend_8_26 AND reversion_12: prior completed bar target 0%; next bar open simulation |
| v1 | trend_8_26 + reversion_12 | 9788.65 | -211.35 | sell /  / trend_8_26 + reversion_12: prior completed bar target 50%; next bar open simulation |
| v1 | trend_8_26 AND volume_26 | 9935.98 | -64.02 | sell /  / trend_8_26 AND volume_26: prior completed bar target 0%; next bar open simulation |
| v1 | trend_8_26 + volume_26 | 9876.49 | -123.51 | sell /  / trend_8_26 + volume_26: prior completed bar target 50%; next bar open simulation |
| v1 | momentum_26 AND breakout_8 | 9853.20 | -146.80 | sell /  / momentum_26 AND breakout_8: prior completed bar target 0%; next bar open simulation |
| v1 | momentum_26 + breakout_8 | 9856.64 | -143.36 | sell /  / momentum_26 + breakout_8: prior completed bar target 50%; next bar open simulation |
| v1 | momentum_26 AND reversion_12 | 9924.34 | -75.66 | sell /  / momentum_26 AND reversion_12: prior completed bar target 0%; next bar open simulation |
| v1 | momentum_26 + reversion_12 | 9893.38 | -106.62 | sell /  / momentum_26 + reversion_12: prior completed bar target 50%; next bar open simulation |
| v1 | momentum_26 AND volume_26 | 10062.05 | 62.05 | sell /  / momentum_26 AND volume_26: prior completed bar target 0%; next bar open simulation |
| v1 | momentum_26 + volume_26 | 9942.31 | -57.69 | sell /  / momentum_26 + volume_26: prior completed bar target 50%; next bar open simulation |
| v1 | breakout_8 AND reversion_12 | 10000.00 | 0.00 | 대기 /  / 새 신호 대기 |
| v1 | breakout_8 + reversion_12 | 9749.93 | -250.07 | sell /  / breakout_8 + reversion_12: prior completed bar target 0%; next bar open simulation |
| v1 | breakout_8 AND volume_26 | 9967.28 | -32.72 | sell /  / breakout_8 AND volume_26: prior completed bar target 0%; next bar open simulation |
| v1 | breakout_8 + volume_26 | 9837.51 | -162.49 | sell /  / breakout_8 + volume_26: prior completed bar target 0%; next bar open simulation |
| v1 | reversion_12 AND volume_26 | 9935.98 | -64.02 | sell /  / reversion_12 AND volume_26: prior completed bar target 0%; next bar open simulation |
| v1 | reversion_12 + volume_26 | 9874.40 | -125.60 | sell /  / reversion_12 + volume_26: prior completed bar target 0%; next bar open simulation |
| v1 | ema_12_26 | 9855.96 | -144.04 | buy /  / EMA12 > EMA26; 조건 충족; EMA12=271.545, EMA26=271.529 |
| v1 | macd_12_26_9 | 9906.42 | -93.58 | sell /  / MACD > 신호선 그리고 MACD > 0; 조건 미충족; MACD=0.978353, signal9=1.01104 |
| v1 | rsi_14_recovery | 9786.95 | -213.05 | sell /  / 직전 RSI14 < 30, 현재 RSI14 >= 30 (한 봉 목표); 조건 미충족; RSI14=46.986, previous_RSI14=37.1649 |
| v1 | bollinger_20_reentry | 9924.03 | -75.97 | sell /  / 직전 종가 < 직전 하단밴드, 현재 하단밴드 <= 종가 <= SMA20 (한 봉 목표); 조건 미충족; close=271.19, lower20=270.018, SMA20=273.224, previous_lower20=270.283 |
| v1 | donchian_20 | 9835.91 | -164.09 | sell /  / 종가 > 현재 봉을 제외한 직전 20봉 최고가; 조건 미충족; close=275.785, prior_high20=276.875 |
| v1 | atr_14_breakout | 9883.94 | -116.06 | sell /  / 종가 > 직전 종가 + 직전 ATR14 그리고 종가 > EMA26; 조건 미충족; close=276.33, threshold=276.592, prior_ATR14=0.747363, EMA26=272.499 |
| v1 | session_vwap | 9858.93 | -141.07 | buy /  / 종가 > 뉴욕 거래일별 누적 전형가격 VWAP; 조건 충족; close=272.6, session_VWAP=272.22, session_volume=3.20722e+06 |
| v1 | obv_20 | 9850.33 | -149.67 | buy /  / OBV > OBV의 SMA20 그리고 종가 > EMA26; 조건 충족; OBV=-2.88653e+07, OBV_SMA20=-3.02185e+07, close=272.6, EMA26=271.529 |
| v1 | stochastic_14_3_recovery | 9665.87 | -334.13 | sell /  / 직전 %K14 < 20에서 %K14가 %D3 상향 돌파 (한 봉 목표); 조건 미충족; K14=72.727, D3=41.2922, previous_K14=34.0903, previous_D3=23.8263 |
| v1 | mfi_14_recovery | 9934.22 | -65.78 | sell /  / 직전 MFI14 < 20, 현재 MFI14 >= 20 (한 봉 목표); 조건 미충족; MFI14=34.131, previous_MFI14=22.0435 |
| v1 | adx_14_trend | 9781.55 | -218.45 | buy /  / Wilder ADX14 >= 25 그리고 +DI14 > -DI14; 조건 충족; ADX14=26.5262, plus_DI14=49.1478, minus_DI14=9.69634 |
| v1 | aroon_25_trend | 9784.20 | -215.80 | sell /  / Aroon25 Up > 70 그리고 Down < 30 (동률이면 최신 극값); 조건 미충족; Aroon_up=68, Aroon_down=20 |
| v1 | cci_20_momentum | 9955.08 | -44.92 | sell /  / CCI20 > 100 (전형가격·평균절대편차); 조건 미충족; CCI20=86.224 |
| v1 | williams_14_recovery | 9833.31 | -166.69 | sell /  / 직전 Williams %R14 < -80, 현재 >= -80 (한 봉 목표); 조건 미충족; Williams_R14=-27.273, previous_R14=-65.9097 |
| v1 | cmf_20_accumulation | 9802.93 | -197.07 | buy /  / Chaikin Money Flow20 > 0.1; 조건 충족; CMF20=0.208851, volume20=1.40263e+07 |
| v1 | chaikin_3_10 | 9851.21 | -148.79 | buy /  / ADL의 EMA3 - EMA10 > 0 그리고 종가 > EMA26; 조건 충족; Chaikin3_10=878293, ADL=-4.92877e+07, close=272.6, EMA26=271.529 |
| v1 | roc_10_momentum | 9996.39 | -3.61 | sell /  / 10봉 ROC > 1% 그리고 종가 > EMA26; 조건 미충족; ROC10_percent=0.995963, close=275.315, EMA26=273.754 |
| v1 | trix_15_trend | 9937.07 | -62.93 | buy /  / 15봉 삼중 EMA의 1봉 변화율 TRIX > 0 그리고 종가 > EMA26; 조건 충족; TRIX15_percent=0.00296855, close=273.97, EMA26=271.9 |
| v1 | keltner_20_breakout | 9933.72 | -66.28 | sell /  / 종가 > EMA20 + 2 x Wilder ATR14; 조건 미충족; close=275.315, upper_Keltner=275.695, EMA20=274.153, ATR14=0.771306 |
| v1 | opening_range_30m | 9941.46 | -58.54 | buy /  / 뉴욕 09:30·09:45 두 완료 봉 최고가를 10:00 이후 종가가 돌파; 조건 충족; close=275.845, opening_high=274.33 |
| v2 | cash | 10000.00 | 0.00 | 대기 /  / 새 신호 대기 |
| v2 | buy_hold | 9878.52 | -121.48 | buy / partial / 직전 완료 봉 목표 비중 100%; 다음 봉 시가 가정 |
| v2 | trend_8_26 | 9660.15 | -339.85 | buy / partial / 직전 완료 봉 목표 비중 100%; 다음 봉 시가 가정 |
| v2 | momentum_26 | 9829.58 | -170.42 | buy / partial / 직전 완료 봉 목표 비중 100%; 다음 봉 시가 가정 |
| v2 | breakout_8 | 9329.18 | -670.82 | sell / filled / 직전 완료 봉 목표 비중 0%; 다음 봉 시가 가정 |
| v2 | reversion_12 | 9325.80 | -674.20 | sell / filled / 직전 완료 봉 목표 비중 0%; 다음 봉 시가 가정 |
| v2 | volume_26 | 9434.73 | -565.27 | sell / filled / 직전 완료 봉 목표 비중 0%; 다음 봉 시가 가정 |
| v2 | trend_8_26 AND momentum_26 | 9824.07 | -175.93 | buy / partial / 직전 완료 봉 목표 비중 100%; 다음 봉 시가 가정 |
| v2 | trend_8_26 + momentum_26 | 9765.18 | -234.82 | buy / partial / 직전 완료 봉 목표 비중 100%; 다음 봉 시가 가정 |
| v2 | trend_8_26 AND breakout_8 | 9710.34 | -289.66 | sell / filled / 직전 완료 봉 목표 비중 0%; 다음 봉 시가 가정 |
| v2 | trend_8_26 + breakout_8 | 9513.49 | -486.51 | sell / filled / 직전 완료 봉 목표 비중 50%; 다음 봉 시가 가정 |
| v2 | trend_8_26 AND reversion_12 | 9705.35 | -294.65 | sell / filled / 직전 완료 봉 목표 비중 0%; 다음 봉 시가 가정 |
| v2 | trend_8_26 + reversion_12 | 9491.23 | -508.77 | sell / filled / 직전 완료 봉 목표 비중 50%; 다음 봉 시가 가정 |
| v2 | trend_8_26 AND volume_26 | 9797.73 | -202.27 | sell / filled / 직전 완료 봉 목표 비중 0%; 다음 봉 시가 가정 |
| v2 | trend_8_26 + volume_26 | 9586.83 | -413.17 | sell / filled / 직전 완료 봉 목표 비중 50%; 다음 봉 시가 가정 |
| v2 | momentum_26 AND breakout_8 | 9653.24 | -346.76 | sell / filled / 직전 완료 봉 목표 비중 0%; 다음 봉 시가 가정 |
| v2 | momentum_26 + breakout_8 | 9596.41 | -403.59 | sell / filled / 직전 완료 봉 목표 비중 50%; 다음 봉 시가 가정 |
| v2 | momentum_26 AND reversion_12 | 9881.28 | -118.72 | sell / filled / 직전 완료 봉 목표 비중 0%; 다음 봉 시가 가정 |
| v2 | momentum_26 + reversion_12 | 9614.19 | -385.81 | sell / filled / 직전 완료 봉 목표 비중 50%; 다음 봉 시가 가정 |
| v2 | momentum_26 AND volume_26 | 9957.22 | -42.78 | sell / filled / 직전 완료 봉 목표 비중 0%; 다음 봉 시가 가정 |
| v2 | momentum_26 + volume_26 | 9629.80 | -370.20 | sell / filled / 직전 완료 봉 목표 비중 50%; 다음 봉 시가 가정 |
| v2 | breakout_8 AND reversion_12 | 10000.00 | 0.00 | 대기 /  / 새 신호 대기 |
| v2 | breakout_8 + reversion_12 | 9366.25 | -633.75 | sell / filled / 직전 완료 봉 목표 비중 0%; 다음 봉 시가 가정 |
| v2 | breakout_8 AND volume_26 | 9710.25 | -289.75 | sell / filled / 직전 완료 봉 목표 비중 0%; 다음 봉 시가 가정 |
| v2 | breakout_8 + volume_26 | 9421.20 | -578.80 | sell / filled / 직전 완료 봉 목표 비중 0%; 다음 봉 시가 가정 |
| v2 | reversion_12 AND volume_26 | 9676.46 | -323.54 | sell / filled / 직전 완료 봉 목표 비중 0%; 다음 봉 시가 가정 |
| v2 | reversion_12 + volume_26 | 9419.31 | -580.69 | sell / filled / 직전 완료 봉 목표 비중 0%; 다음 봉 시가 가정 |
| v2 | ema_12_26 | 9851.03 | -148.97 | buy / partial / EMA12 > EMA26; 조건 충족; EMA12=271.545, EMA26=271.529; 직전 완료 봉 목표를 다음 봉 시가에 모의 적용 |
| v2 | macd_12_26_9 | 9900.47 | -99.53 | sell / filled / MACD > 신호선 그리고 MACD > 0; 조건 미충족; MACD=0.978353, signal9=1.01104; 직전 완료 봉 목표를 다음 봉 시가에 모의 적용 |
| v2 | rsi_14_recovery | 9779.12 | -220.88 | sell / filled / 직전 RSI14 < 30, 현재 RSI14 >= 30 (한 봉 목표); 조건 미충족; RSI14=46.986, previous_RSI14=37.1649; 직전 완료 봉 목표를 다음 봉 시가에 모의 적용 |
| v2 | bollinger_20_reentry | 9920.06 | -79.94 | sell / filled / 직전 종가 < 직전 하단밴드, 현재 하단밴드 <= 종가 <= SMA20 (한 봉 목표); 조건 미충족; close=271.19, lower20=270.018, SMA20=273.224, previous_lower20=270.283; 직전 완료 봉 목표를 다음 봉 시가에 모의 적용 |
| v2 | donchian_20 | 9830.01 | -169.99 | sell / filled / 종가 > 현재 봉을 제외한 직전 20봉 최고가; 조건 미충족; close=275.785, prior_high20=276.875; 직전 완료 봉 목표를 다음 봉 시가에 모의 적용 |
| v2 | atr_14_breakout | 9876.04 | -123.96 | sell / filled / 종가 > 직전 종가 + 직전 ATR14 그리고 종가 > EMA26; 조건 미충족; close=276.33, threshold=276.592, prior_ATR14=0.747363, EMA26=272.499; 직전 완료 봉 목표를 다음 봉 시가에 모의 적용 |
| v2 | session_vwap | 9850.07 | -149.93 | buy / partial / 종가 > 뉴욕 거래일별 누적 전형가격 VWAP; 조건 충족; close=272.6, session_VWAP=272.22, session_volume=3.20722e+06; 직전 완료 봉 목표를 다음 봉 시가에 모의 적용 |
| v2 | obv_20 | 9841.47 | -158.53 | buy / partial / OBV > OBV의 SMA20 그리고 종가 > EMA26; 조건 충족; OBV=-2.88653e+07, OBV_SMA20=-3.02185e+07, close=272.6, EMA26=271.529; 직전 완료 봉 목표를 다음 봉 시가에 모의 적용 |
| v2 | stochastic_14_3_recovery | 9650.41 | -349.59 | sell / filled / 직전 %K14 < 20에서 %K14가 %D3 상향 돌파 (한 봉 목표); 조건 미충족; K14=72.727, D3=41.2922, previous_K14=34.0903, previous_D3=23.8263; 직전 완료 봉 목표를 다음 봉 시가에 모의 적용 |
| v2 | mfi_14_recovery | 9930.25 | -69.75 | sell / filled / 직전 MFI14 < 20, 현재 MFI14 >= 20 (한 봉 목표); 조건 미충족; MFI14=34.131, previous_MFI14=22.0435; 직전 완료 봉 목표를 다음 봉 시가에 모의 적용 |
| v2 | adx_14_trend | 9776.66 | -223.34 | buy / partial / Wilder ADX14 >= 25 그리고 +DI14 > -DI14; 조건 충족; ADX14=26.5262, plus_DI14=49.1478, minus_DI14=9.69634; 직전 완료 봉 목표를 다음 봉 시가에 모의 적용 |
| v2 | aroon_25_trend | 9776.38 | -223.62 | sell / filled / Aroon25 Up > 70 그리고 Down < 30 (동률이면 최신 극값); 조건 미충족; Aroon_up=68, Aroon_down=20; 직전 완료 봉 목표를 다음 봉 시가에 모의 적용 |
| v2 | cci_20_momentum | 9949.11 | -50.89 | sell / filled / CCI20 > 100 (전형가격·평균절대편차); 조건 미충족; CCI20=86.224; 직전 완료 봉 목표를 다음 봉 시가에 모의 적용 |
| v2 | williams_14_recovery | 9825.45 | -174.55 | sell / filled / 직전 Williams %R14 < -80, 현재 >= -80 (한 봉 목표); 조건 미충족; Williams_R14=-27.273, previous_R14=-65.9097; 직전 완료 봉 목표를 다음 봉 시가에 모의 적용 |
| v2 | cmf_20_accumulation | 9790.20 | -209.80 | buy / partial / Chaikin Money Flow20 > 0.1; 조건 충족; CMF20=0.208851, volume20=1.40263e+07; 직전 완료 봉 목표를 다음 봉 시가에 모의 적용 |
| v2 | chaikin_3_10 | 9842.35 | -157.65 | buy / partial / ADL의 EMA3 - EMA10 > 0 그리고 종가 > EMA26; 조건 충족; Chaikin3_10=878293, ADL=-4.92877e+07, close=272.6, EMA26=271.529; 직전 완료 봉 목표를 다음 봉 시가에 모의 적용 |
| v2 | roc_10_momentum | 9994.39 | -5.61 | sell / filled / 10봉 ROC > 1% 그리고 종가 > EMA26; 조건 미충족; ROC10_percent=0.995963, close=275.315, EMA26=273.754; 직전 완료 봉 목표를 다음 봉 시가에 모의 적용 |
| v2 | trix_15_trend | 9934.09 | -65.91 | buy / partial / 15봉 삼중 EMA의 1봉 변화율 TRIX > 0 그리고 종가 > EMA26; 조건 충족; TRIX15_percent=0.00296855, close=273.97, EMA26=271.9; 직전 완료 봉 목표를 다음 봉 시가에 모의 적용 |
| v2 | keltner_20_breakout | 9929.75 | -70.25 | sell / filled / 종가 > EMA20 + 2 x Wilder ATR14; 조건 미충족; close=275.315, upper_Keltner=275.695, EMA20=274.153, ATR14=0.771306; 직전 완료 봉 목표를 다음 봉 시가에 모의 적용 |
| v2 | opening_range_30m | 9938.47 | -61.53 | buy / partial / 뉴욕 09:30·09:45 두 완료 봉 최고가를 10:00 이후 종가가 돌파; 조건 충족; close=275.845, opening_high=274.33; 직전 완료 봉 목표를 다음 봉 시가에 모의 적용 |

### 같은 기간의 비용·노출 비교 (사후 연구)

| 전략 | 비용 전 | 비용 후 | 100% 보유 | 같은 평균 노출 보유 | 평균 노출 |
|---|---:|---:|---:|---:|---:|
| cash | 0.00% | 0.00% | -1.51% | -0.00% | 0.00% |
| buy_hold | -1.09% | -1.51% | -1.51% | -1.51% | 100.00% |
| trend_8_26 | -0.86% | -4.54% | -1.51% | -0.72% | 47.51% |
| momentum_26 | -0.76% | -6.43% | -1.51% | -0.68% | 45.14% |
| breakout_8 | -0.32% | -14.30% | -1.51% | -0.30% | 19.95% |
| reversion_12 | -2.15% | -13.73% | -1.51% | -0.42% | 27.82% |
| volume_26 | -1.61% | -8.78% | -1.51% | -0.13% | 8.66% |
| trend_8_26 AND momentum_26 | -0.79% | -5.26% | -1.51% | -0.58% | 38.32% |
| trend_8_26 + momentum_26 | -0.81% | -5.09% | -1.51% | -0.70% | 46.33% |
| trend_8_26 AND breakout_8 | -0.53% | -8.92% | -1.51% | -0.19% | 12.60% |
| trend_8_26 + breakout_8 | -0.58% | -9.36% | -1.51% | -0.51% | 33.73% |
| trend_8_26 AND reversion_12 | -0.74% | -4.82% | -1.51% | -0.08% | 5.51% |
| trend_8_26 + reversion_12 | -1.50% | -9.07% | -1.51% | -0.57% | 37.67% |
| trend_8_26 AND volume_26 | -0.98% | -3.85% | -1.51% | -0.04% | 2.62% |
| trend_8_26 + volume_26 | -1.23% | -6.29% | -1.51% | -0.43% | 28.09% |
| momentum_26 AND breakout_8 | 0.22% | -8.24% | -1.51% | -0.18% | 11.81% |
| momentum_26 + breakout_8 | -0.53% | -10.26% | -1.51% | -0.49% | 32.55% |
| momentum_26 AND reversion_12 | 0.03% | -3.68% | -1.51% | -0.06% | 3.67% |
| momentum_26 + reversion_12 | -1.45% | -9.21% | -1.51% | -0.55% | 36.49% |
| momentum_26 AND volume_26 | 0.06% | -2.02% | -1.51% | -0.03% | 1.84% |
| momentum_26 + volume_26 | -1.18% | -7.23% | -1.51% | -0.41% | 26.91% |
| breakout_8 AND reversion_12 | 0.00% | 0.00% | -1.51% | -0.00% | 0.00% |
| breakout_8 + reversion_12 | -1.23% | -13.48% | -1.51% | -0.36% | 23.89% |
| breakout_8 AND volume_26 | -0.84% | -4.11% | -1.51% | -0.04% | 2.62% |
| breakout_8 + volume_26 | -0.96% | -11.21% | -1.51% | -0.22% | 14.31% |
| reversion_12 AND volume_26 | -0.62% | -4.31% | -1.51% | -0.06% | 3.94% |
| reversion_12 + volume_26 | -1.87% | -10.73% | -1.51% | -0.28% | 18.25% |
| ema_12_26 | 0.89% | -2.03% | -1.51% | -0.71% | 46.98% |
| macd_12_26_9 | 2.60% | -0.38% | -1.51% | -0.48% | 31.50% |
| rsi_14_recovery | -0.65% | -5.14% | -1.51% | -0.04% | 2.89% |
| bollinger_20_reentry | -0.24% | -4.35% | -1.51% | -0.04% | 2.62% |
| donchian_20 | -0.34% | -6.04% | -1.51% | -0.10% | 6.56% |
| atr_14_breakout | -0.52% | -7.37% | -1.51% | -0.07% | 4.72% |
| session_vwap | 0.22% | -9.39% | -1.51% | -0.66% | 43.57% |
| obv_20 | 1.36% | -3.21% | -1.51% | -0.63% | 41.73% |
| stochastic_14_3_recovery | -0.44% | -12.96% | -1.51% | -0.13% | 8.40% |
| mfi_14_recovery | 0.36% | -4.17% | -1.51% | -0.04% | 2.89% |
| adx_14_trend | -0.39% | -4.09% | -1.51% | -0.51% | 33.60% |
| aroon_25_trend | -1.30% | -5.76% | -1.51% | -0.33% | 22.05% |
| cci_20_momentum | -0.89% | -7.72% | -1.51% | -0.31% | 20.47% |
| williams_14_recovery | -0.09% | -9.29% | -1.51% | -0.09% | 6.04% |
| cmf_20_accumulation | -0.78% | -8.01% | -1.51% | -0.33% | 22.05% |
| chaikin_3_10 | -0.77% | -7.61% | -1.51% | -0.53% | 34.65% |
| roc_10_momentum | -0.27% | -1.93% | -1.51% | -0.08% | 5.51% |
| trix_15_trend | 0.97% | -2.37% | -1.51% | -0.53% | 34.65% |
| keltner_20_breakout | -0.55% | -4.24% | -1.51% | -0.12% | 7.61% |
| opening_range_30m | 2.50% | -1.71% | -1.51% | -0.37% | 24.41% |

동일 구간·초기 자금, 종료 시 청산 비용 포함. 노출 맞춤은 사후 설명용이며 v2 실제 계좌 성과가 아닙니다.
[낙폭 분해·비용 영향·전체 구간](IWM/comparison.json)

[v1 전체 기록](IWM/accounts.json) · [v2 전체 기록](IWM/accounts-v2.json)

## DIA 계좌

| 모델 | 전략 | 평가액 USD | 손익 USD | 최근 매매·이유 |
|---|---|---:|---:|---|
| v1 | cash | 10000.00 | 0.00 | 대기 /  / 새 신호 대기 |
| v1 | buy_hold | 10003.70 | 3.70 | buy /  / buy_hold: prior completed bar target 100%; next bar open simulation |
| v1 | trend_8_26 | 9962.04 | -37.96 | buy /  / trend_8_26: prior completed bar target 100%; next bar open simulation |
| v1 | momentum_26 | 9858.21 | -141.79 | buy /  / momentum_26: prior completed bar target 100%; next bar open simulation |
| v1 | breakout_8 | 9693.16 | -306.84 | sell /  / breakout_8: prior completed bar target 0%; next bar open simulation |
| v1 | reversion_12 | 9897.27 | -102.73 | sell /  / reversion_12: prior completed bar target 0%; next bar open simulation |
| v1 | volume_26 | 9939.83 | -60.17 | sell /  / volume_26: prior completed bar target 0%; next bar open simulation |
| v1 | trend_8_26 AND momentum_26 | 9858.21 | -141.79 | buy /  / trend_8_26 AND momentum_26: prior completed bar target 100%; next bar open simulation |
| v1 | trend_8_26 + momentum_26 | 9910.07 | -89.93 | buy /  / trend_8_26 + momentum_26: prior completed bar target 100%; next bar open simulation |
| v1 | trend_8_26 AND breakout_8 | 9825.30 | -174.70 | sell /  / trend_8_26 AND breakout_8: prior completed bar target 0%; next bar open simulation |
| v1 | trend_8_26 + breakout_8 | 9846.39 | -153.61 | sell /  / trend_8_26 + breakout_8: prior completed bar target 50%; next bar open simulation |
| v1 | trend_8_26 AND reversion_12 | 9940.76 | -59.24 | sell /  / trend_8_26 AND reversion_12: prior completed bar target 0%; next bar open simulation |
| v1 | trend_8_26 + reversion_12 | 9929.47 | -70.53 | sell /  / trend_8_26 + reversion_12: prior completed bar target 50%; next bar open simulation |
| v1 | trend_8_26 AND volume_26 | 9974.09 | -25.91 | sell /  / trend_8_26 AND volume_26: prior completed bar target 0%; next bar open simulation |
| v1 | trend_8_26 + volume_26 | 9950.81 | -49.19 | sell /  / trend_8_26 + volume_26: prior completed bar target 50%; next bar open simulation |
| v1 | momentum_26 AND breakout_8 | 9825.30 | -174.70 | sell /  / momentum_26 AND breakout_8: prior completed bar target 0%; next bar open simulation |
| v1 | momentum_26 + breakout_8 | 9775.33 | -224.67 | sell /  / momentum_26 + breakout_8: prior completed bar target 50%; next bar open simulation |
| v1 | momentum_26 AND reversion_12 | 9940.78 | -59.22 | sell /  / momentum_26 AND reversion_12: prior completed bar target 0%; next bar open simulation |
| v1 | momentum_26 + reversion_12 | 9917.15 | -82.85 | sell /  / momentum_26 + reversion_12: prior completed bar target 50%; next bar open simulation |
| v1 | momentum_26 AND volume_26 | 9929.52 | -70.48 | sell /  / momentum_26 AND volume_26: prior completed bar target 0%; next bar open simulation |
| v1 | momentum_26 + volume_26 | 9918.68 | -81.32 | sell /  / momentum_26 + volume_26: prior completed bar target 50%; next bar open simulation |
| v1 | breakout_8 AND reversion_12 | 10000.00 | 0.00 | 대기 /  / 새 신호 대기 |
| v1 | breakout_8 + reversion_12 | 9814.18 | -185.82 | sell /  / breakout_8 + reversion_12: prior completed bar target 0%; next bar open simulation |
| v1 | breakout_8 AND volume_26 | 9986.25 | -13.75 | sell /  / breakout_8 AND volume_26: prior completed bar target 0%; next bar open simulation |
| v1 | breakout_8 + volume_26 | 9855.04 | -144.96 | sell /  / breakout_8 + volume_26: prior completed bar target 0%; next bar open simulation |
| v1 | reversion_12 AND volume_26 | 9970.42 | -29.58 | sell /  / reversion_12 AND volume_26: prior completed bar target 0%; next bar open simulation |
| v1 | reversion_12 + volume_26 | 9938.32 | -61.68 | sell /  / reversion_12 + volume_26: prior completed bar target 0%; next bar open simulation |
| v1 | ema_12_26 | 9858.44 | -141.56 | buy /  / EMA12 > EMA26; 조건 충족; EMA12=519.74, EMA26=519.585 |
| v1 | macd_12_26_9 | 9895.59 | -104.41 | sell /  / MACD > 신호선 그리고 MACD > 0; 조건 미충족; MACD=1.09098, signal9=1.12388 |
| v1 | rsi_14_recovery | 10000.00 | 0.00 | 대기 /  / 새 신호 대기 |
| v1 | bollinger_20_reentry | 9978.51 | -21.49 | sell /  / 직전 종가 < 직전 하단밴드, 현재 하단밴드 <= 종가 <= SMA20 (한 봉 목표); 조건 미충족; close=519.823, lower20=518.355, SMA20=521.612, previous_lower20=518.548 |
| v1 | donchian_20 | 9822.00 | -178.00 | sell /  / 종가 > 현재 봉을 제외한 직전 20봉 최고가; 조건 미충족; close=523.68, prior_high20=526.17 |
| v1 | atr_14_breakout | 9885.70 | -114.30 | sell /  / 종가 > 직전 종가 + 직전 ATR14 그리고 종가 > EMA26; 조건 미충족; close=525.49, threshold=525.841, prior_ATR14=0.980592, EMA26=520.815 |
| v1 | session_vwap | 9913.38 | -86.62 | buy /  / 종가 > 뉴욕 거래일별 누적 전형가격 VWAP; 조건 충족; close=521.46, session_VWAP=520.55, session_volume=446463 |
| v1 | obv_20 | 9864.70 | -135.30 | buy /  / OBV > OBV의 SMA20 그리고 종가 > EMA26; 조건 충족; OBV=-9.86891e+06, OBV_SMA20=-1.0028e+07, close=521.46, EMA26=519.585 |
| v1 | stochastic_14_3_recovery | 9821.00 | -179.00 | sell /  / 직전 %K14 < 20에서 %K14가 %D3 상향 돌파 (한 봉 목표); 조건 미충족; K14=100, D3=70.5235, previous_K14=91.7443, previous_D3=57.9113 |
| v1 | mfi_14_recovery | 9936.38 | -63.62 | sell /  / 직전 MFI14 < 20, 현재 MFI14 >= 20 (한 봉 목표); 조건 미충족; MFI14=44.8014, previous_MFI14=20.0271 |
| v1 | adx_14_trend | 9811.65 | -188.35 | sell /  / Wilder ADX14 >= 25 그리고 +DI14 > -DI14; 조건 미충족; ADX14=24.7281, plus_DI14=33.8838, minus_DI14=22.7145 |
| v1 | aroon_25_trend | 9928.84 | -71.16 | sell /  / Aroon25 Up > 70 그리고 Down < 30 (동률이면 최신 극값); 조건 미충족; Aroon_up=100, Aroon_down=80 |
| v1 | cci_20_momentum | 9915.48 | -84.52 | sell /  / CCI20 > 100 (전형가격·평균절대편차); 조건 미충족; CCI20=87.8356 |
| v1 | williams_14_recovery | 9854.30 | -145.70 | sell /  / 직전 Williams %R14 < -80, 현재 >= -80 (한 봉 목표); 조건 미충족; Williams_R14=0, previous_R14=-8.25572 |
| v1 | cmf_20_accumulation | 9814.95 | -185.05 | buy /  / Chaikin Money Flow20 > 0.1; 조건 충족; CMF20=0.237356, volume20=1.61808e+06 |
| v1 | chaikin_3_10 | 9866.61 | -133.39 | buy /  / ADL의 EMA3 - EMA10 > 0 그리고 종가 > EMA26; 조건 충족; Chaikin3_10=78733.3, ADL=-1.64223e+07, close=521.46, EMA26=519.585 |
| v1 | roc_10_momentum | 9939.01 | -60.99 | sell /  / 10봉 ROC > 1% 그리고 종가 > EMA26; 조건 미충족; ROC10_percent=0.771645, close=523.68, EMA26=521.367 |
| v1 | trix_15_trend | 9959.94 | -40.06 | buy /  / 15봉 삼중 EMA의 1봉 변화율 TRIX > 0 그리고 종가 > EMA26; 조건 충족; TRIX15_percent=0.000473967, close=521.46, EMA26=519.585 |
| v1 | keltner_20_breakout | 9944.49 | -55.51 | sell /  / 종가 > EMA20 + 2 x Wilder ATR14; 조건 미충족; close=523.68, upper_Keltner=523.985, EMA20=521.785, ATR14=1.10038 |
| v1 | opening_range_30m | 9797.43 | -202.57 | buy /  / 뉴욕 09:30·09:45 두 완료 봉 최고가를 10:00 이후 종가가 돌파; 조건 충족; close=524.86, opening_high=523.47 |
| v2 | cash | 10000.00 | 0.00 | 대기 /  / 새 신호 대기 |
| v2 | buy_hold | 10127.63 | 127.63 | buy / partial / 직전 완료 봉 목표 비중 100%; 다음 봉 시가 가정 |
| v2 | trend_8_26 | 9895.52 | -104.48 | buy / partial / 직전 완료 봉 목표 비중 100%; 다음 봉 시가 가정 |
| v2 | momentum_26 | 9896.09 | -103.91 | buy / partial / 직전 완료 봉 목표 비중 100%; 다음 봉 시가 가정 |
| v2 | breakout_8 | 9220.36 | -779.64 | sell / filled / 직전 완료 봉 목표 비중 0%; 다음 봉 시가 가정 |
| v2 | reversion_12 | 9592.64 | -407.36 | sell / filled / 직전 완료 봉 목표 비중 0%; 다음 봉 시가 가정 |
| v2 | volume_26 | 9652.01 | -347.99 | sell / filled / 직전 완료 봉 목표 비중 0%; 다음 봉 시가 가정 |
| v2 | trend_8_26 AND momentum_26 | 9891.50 | -108.50 | buy / partial / 직전 완료 봉 목표 비중 100%; 다음 봉 시가 가정 |
| v2 | trend_8_26 + momentum_26 | 9895.96 | -104.04 | buy / partial / 직전 완료 봉 목표 비중 100%; 다음 봉 시가 가정 |
| v2 | trend_8_26 AND breakout_8 | 9509.90 | -490.10 | sell / filled / 직전 완료 봉 목표 비중 0%; 다음 봉 시가 가정 |
| v2 | trend_8_26 + breakout_8 | 9572.16 | -427.84 | sell / filled / 직전 완료 봉 목표 비중 50%; 다음 봉 시가 가정 |
| v2 | trend_8_26 AND reversion_12 | 9748.75 | -251.25 | sell / filled / 직전 완료 봉 목표 비중 0%; 다음 봉 시가 가정 |
| v2 | trend_8_26 + reversion_12 | 9742.52 | -257.48 | sell / filled / 직전 완료 봉 목표 비중 50%; 다음 봉 시가 가정 |
| v2 | trend_8_26 AND volume_26 | 9827.44 | -172.56 | sell / filled / 직전 완료 봉 목표 비중 0%; 다음 봉 시가 가정 |
| v2 | trend_8_26 + volume_26 | 9793.39 | -206.61 | sell / filled / 직전 완료 봉 목표 비중 50%; 다음 봉 시가 가정 |
| v2 | momentum_26 AND breakout_8 | 9499.07 | -500.93 | sell / filled / 직전 완료 봉 목표 비중 0%; 다음 봉 시가 가정 |
| v2 | momentum_26 + breakout_8 | 9552.38 | -447.62 | sell / filled / 직전 완료 봉 목표 비중 50%; 다음 봉 시가 가정 |
| v2 | momentum_26 AND reversion_12 | 9895.03 | -104.97 | sell / filled / 직전 완료 봉 목표 비중 0%; 다음 봉 시가 가정 |
| v2 | momentum_26 + reversion_12 | 9783.85 | -216.15 | sell / filled / 직전 완료 봉 목표 비중 50%; 다음 봉 시가 가정 |
| v2 | momentum_26 AND volume_26 | 9716.58 | -283.42 | sell / filled / 직전 완료 봉 목표 비중 0%; 다음 봉 시가 가정 |
| v2 | momentum_26 + volume_26 | 9835.06 | -164.94 | sell / filled / 직전 완료 봉 목표 비중 50%; 다음 봉 시가 가정 |
| v2 | breakout_8 AND reversion_12 | 10000.00 | 0.00 | 대기 /  / 새 신호 대기 |
| v2 | breakout_8 + reversion_12 | 9423.89 | -576.11 | sell / filled / 직전 완료 봉 목표 비중 0%; 다음 봉 시가 가정 |
| v2 | breakout_8 AND volume_26 | 9781.13 | -218.87 | sell / filled / 직전 완료 봉 목표 비중 0%; 다음 봉 시가 가정 |
| v2 | breakout_8 + volume_26 | 9473.24 | -526.76 | sell / filled / 직전 완료 봉 목표 비중 0%; 다음 봉 시가 가정 |
| v2 | reversion_12 AND volume_26 | 9966.44 | -33.56 | sell / filled / 직전 완료 봉 목표 비중 0%; 다음 봉 시가 가정 |
| v2 | reversion_12 + volume_26 | 9642.17 | -357.83 | sell / filled / 직전 완료 봉 목표 비중 0%; 다음 봉 시가 가정 |
| v2 | ema_12_26 | 9853.51 | -146.49 | buy / partial / EMA12 > EMA26; 조건 충족; EMA12=519.74, EMA26=519.585; 직전 완료 봉 목표를 다음 봉 시가에 모의 적용 |
| v2 | macd_12_26_9 | 9889.66 | -110.34 | sell / filled / MACD > 신호선 그리고 MACD > 0; 조건 미충족; MACD=1.09098, signal9=1.12388; 직전 완료 봉 목표를 다음 봉 시가에 모의 적용 |
| v2 | rsi_14_recovery | 10000.00 | 0.00 | 대기 /  / 새 신호 대기 |
| v2 | bollinger_20_reentry | 9976.52 | -23.48 | sell / filled / 직전 종가 < 직전 하단밴드, 현재 하단밴드 <= 종가 <= SMA20 (한 봉 목표); 조건 미충족; close=519.823, lower20=518.355, SMA20=521.612, previous_lower20=518.548; 직전 완료 봉 목표를 다음 봉 시가에 모의 적용 |
| v2 | donchian_20 | 9814.14 | -185.86 | sell / filled / 종가 > 현재 봉을 제외한 직전 20봉 최고가; 조건 미충족; close=523.68, prior_high20=526.17; 직전 완료 봉 목표를 다음 봉 시가에 모의 적용 |
| v2 | atr_14_breakout | 9877.79 | -122.21 | sell / filled / 종가 > 직전 종가 + 직전 ATR14 그리고 종가 > EMA26; 조건 미충족; close=525.49, threshold=525.841, prior_ATR14=0.980592, EMA26=520.815; 직전 완료 봉 목표를 다음 봉 시가에 모의 적용 |
| v2 | session_vwap | 9906.44 | -93.56 | buy / partial / 종가 > 뉴욕 거래일별 누적 전형가격 VWAP; 조건 충족; close=521.46, session_VWAP=520.55, session_volume=446463; 직전 완료 봉 목표를 다음 봉 시가에 모의 적용 |
| v2 | obv_20 | 9857.80 | -142.20 | buy / partial / OBV > OBV의 SMA20 그리고 종가 > EMA26; 조건 충족; OBV=-9.86891e+06, OBV_SMA20=-1.0028e+07, close=521.46, EMA26=519.585; 직전 완료 봉 목표를 다음 봉 시가에 모의 적용 |
| v2 | stochastic_14_3_recovery | 9811.19 | -188.81 | sell / filled / 직전 %K14 < 20에서 %K14가 %D3 상향 돌파 (한 봉 목표); 조건 미충족; K14=100, D3=70.5235, previous_K14=91.7443, previous_D3=57.9113; 직전 완료 봉 목표를 다음 봉 시가에 모의 적용 |
| v2 | mfi_14_recovery | 9932.40 | -67.60 | sell / filled / 직전 MFI14 < 20, 현재 MFI14 >= 20 (한 봉 목표); 조건 미충족; MFI14=44.8014, previous_MFI14=20.0271; 직전 완료 봉 목표를 다음 봉 시가에 모의 적용 |
| v2 | adx_14_trend | 9805.77 | -194.23 | sell / filled / Wilder ADX14 >= 25 그리고 +DI14 > -DI14; 조건 미충족; ADX14=24.7281, plus_DI14=33.8838, minus_DI14=22.7145; 직전 완료 봉 목표를 다음 봉 시가에 모의 적용 |
| v2 | aroon_25_trend | 9922.89 | -77.11 | sell / filled / Aroon25 Up > 70 그리고 Down < 30 (동률이면 최신 극값); 조건 미충족; Aroon_up=100, Aroon_down=80; 직전 완료 봉 목표를 다음 봉 시가에 모의 적용 |
| v2 | cci_20_momentum | 9909.53 | -90.47 | sell / filled / CCI20 > 100 (전형가격·평균절대편차); 조건 미충족; CCI20=87.8356; 직전 완료 봉 목표를 다음 봉 시가에 모의 적용 |
| v2 | williams_14_recovery | 9846.42 | -153.58 | sell / filled / 직전 Williams %R14 < -80, 현재 >= -80 (한 봉 목표); 조건 미충족; Williams_R14=0, previous_R14=-8.25572; 직전 완료 봉 목표를 다음 봉 시가에 모의 적용 |
| v2 | cmf_20_accumulation | 9806.12 | -193.88 | buy / partial / Chaikin Money Flow20 > 0.1; 조건 충족; CMF20=0.237356, volume20=1.61808e+06; 직전 완료 봉 목표를 다음 봉 시가에 모의 적용 |
| v2 | chaikin_3_10 | 9859.71 | -140.29 | buy / partial / ADL의 EMA3 - EMA10 > 0 그리고 종가 > EMA26; 조건 충족; Chaikin3_10=78733.3, ADL=-1.64223e+07, close=521.46, EMA26=519.585; 직전 완료 봉 목표를 다음 봉 시가에 모의 적용 |
| v2 | roc_10_momentum | 9937.03 | -62.97 | sell / filled / 10봉 ROC > 1% 그리고 종가 > EMA26; 조건 미충족; ROC10_percent=0.771645, close=523.68, EMA26=521.367; 직전 완료 봉 목표를 다음 봉 시가에 모의 적용 |
| v2 | trix_15_trend | 9956.95 | -43.05 | buy / partial / 15봉 삼중 EMA의 1봉 변화율 TRIX > 0 그리고 종가 > EMA26; 조건 충족; TRIX15_percent=0.000473967, close=521.46, EMA26=519.585; 직전 완료 봉 목표를 다음 봉 시가에 모의 적용 |
| v2 | keltner_20_breakout | 9940.51 | -59.49 | sell / filled / 종가 > EMA20 + 2 x Wilder ATR14; 조건 미충족; close=523.68, upper_Keltner=523.985, EMA20=521.785, ATR14=1.10038; 직전 완료 봉 목표를 다음 봉 시가에 모의 적용 |
| v2 | opening_range_30m | 9788.62 | -211.38 | buy / partial / 뉴욕 09:30·09:45 두 완료 봉 최고가를 10:00 이후 종가가 돌파; 조건 충족; close=524.86, opening_high=523.47; 직전 완료 봉 목표를 다음 봉 시가에 모의 적용 |

### 같은 기간의 비용·노출 비교 (사후 연구)

| 전략 | 비용 전 | 비용 후 | 100% 보유 | 같은 평균 노출 보유 | 평균 노출 |
|---|---:|---:|---:|---:|---:|
| cash | 0.00% | 0.00% | 1.79% | 0.00% | 0.00% |
| buy_hold | 2.21% | 1.79% | 1.79% | 1.79% | 100.00% |
| trend_8_26 | 2.26% | -1.53% | 1.79% | 1.10% | 61.94% |
| momentum_26 | 0.79% | -3.76% | 1.79% | 1.01% | 56.69% |
| breakout_8 | 0.73% | -16.27% | 1.79% | 0.41% | 23.10% |
| reversion_12 | -0.58% | -8.59% | 1.79% | 0.40% | 22.31% |
| volume_26 | 0.22% | -9.77% | 1.79% | 0.20% | 11.02% |
| trend_8_26 AND momentum_26 | 1.91% | -2.70% | 1.79% | 0.92% | 51.44% |
| trend_8_26 + momentum_26 | 1.53% | -2.65% | 1.79% | 1.06% | 59.32% |
| trend_8_26 AND breakout_8 | 1.13% | -11.22% | 1.79% | 0.29% | 16.01% |
| trend_8_26 + breakout_8 | 1.50% | -8.81% | 1.79% | 0.76% | 42.53% |
| trend_8_26 AND reversion_12 | 0.43% | -4.91% | 1.79% | 0.12% | 6.82% |
| trend_8_26 + reversion_12 | 0.84% | -4.93% | 1.79% | 0.75% | 42.13% |
| trend_8_26 AND volume_26 | 1.48% | -4.32% | 1.79% | 0.11% | 6.04% |
| trend_8_26 + volume_26 | 1.24% | -5.55% | 1.79% | 0.65% | 36.49% |
| momentum_26 AND breakout_8 | 0.30% | -11.95% | 1.79% | 0.29% | 16.54% |
| momentum_26 + breakout_8 | 0.76% | -10.04% | 1.79% | 0.71% | 39.90% |
| momentum_26 AND reversion_12 | -0.27% | -3.57% | 1.79% | 0.10% | 5.77% |
| momentum_26 + reversion_12 | 0.11% | -5.22% | 1.79% | 0.70% | 39.50% |
| momentum_26 AND volume_26 | 0.10% | -5.62% | 1.79% | 0.10% | 5.51% |
| momentum_26 + volume_26 | 0.51% | -6.03% | 1.79% | 0.60% | 33.86% |
| breakout_8 AND reversion_12 | 0.00% | 0.00% | 1.79% | 0.00% | 0.00% |
| breakout_8 + reversion_12 | 0.08% | -12.15% | 1.79% | 0.40% | 22.71% |
| breakout_8 AND volume_26 | -0.47% | -3.75% | 1.79% | 0.06% | 3.15% |
| breakout_8 + volume_26 | 0.48% | -11.98% | 1.79% | 0.30% | 17.07% |
| reversion_12 AND volume_26 | 0.29% | -4.24% | 1.79% | 0.06% | 3.41% |
| reversion_12 + volume_26 | -0.18% | -9.00% | 1.79% | 0.30% | 16.67% |
| ema_12_26 | 0.59% | -2.32% | 1.79% | 0.96% | 54.07% |
| macd_12_26_9 | 1.99% | -1.79% | 1.79% | 0.58% | 32.28% |
| rsi_14_recovery | 0.16% | -1.09% | 1.79% | 0.01% | 0.79% |
| bollinger_20_reentry | 0.11% | -4.01% | 1.79% | 0.05% | 2.62% |
| donchian_20 | 0.36% | -6.94% | 1.79% | 0.17% | 9.71% |
| atr_14_breakout | -0.26% | -7.52% | 1.79% | 0.10% | 5.77% |
| session_vwap | 2.54% | -5.33% | 1.79% | 0.95% | 53.02% |
| obv_20 | 1.10% | -7.04% | 1.79% | 0.82% | 46.19% |
| stochastic_14_3_recovery | 0.95% | -11.00% | 1.79% | 0.14% | 7.87% |
| mfi_14_recovery | 0.16% | -3.15% | 1.79% | 0.04% | 2.10% |
| adx_14_trend | -0.13% | -4.23% | 1.79% | 0.59% | 33.33% |
| aroon_25_trend | 1.36% | -2.40% | 1.79% | 0.48% | 26.77% |
| cci_20_momentum | 1.06% | -5.51% | 1.79% | 0.46% | 25.98% |
| williams_14_recovery | 1.54% | -6.25% | 1.79% | 0.09% | 4.99% |
| cmf_20_accumulation | 1.53% | -6.26% | 1.79% | 0.56% | 31.23% |
| chaikin_3_10 | 2.32% | -7.10% | 1.79% | 0.81% | 45.67% |
| roc_10_momentum | -0.07% | -0.90% | 1.79% | 0.04% | 2.10% |
| trix_15_trend | 0.71% | -3.02% | 1.79% | 0.82% | 45.93% |
| keltner_20_breakout | 0.78% | -5.77% | 1.79% | 0.33% | 18.37% |
| opening_range_30m | 1.60% | -4.20% | 1.79% | 0.49% | 27.30% |

동일 구간·초기 자금, 종료 시 청산 비용 포함. 노출 맞춤은 사후 설명용이며 v2 실제 계좌 성과가 아닙니다.
[낙폭 분해·비용 영향·전체 구간](DIA/comparison.json)

[v1 전체 기록](DIA/accounts.json) · [v2 전체 기록](DIA/accounts-v2.json)

## MSFT 계좌

| 모델 | 전략 | 평가액 USD | 손익 USD | 최근 매매·이유 |
|---|---|---:|---:|---|
| v1 | cash | 10000.00 | 0.00 | 대기 /  / 새 신호 대기 |
| v1 | buy_hold | 9844.60 | -155.40 | buy /  / buy_hold: prior completed bar target 100%; next bar open simulation |
| v1 | trend_8_26 | 9677.44 | -322.56 | sell /  / trend_8_26: prior completed bar target 0%; next bar open simulation |
| v1 | momentum_26 | 9648.89 | -351.11 | sell /  / momentum_26: prior completed bar target 0%; next bar open simulation |
| v1 | breakout_8 | 9702.41 | -297.59 | buy /  / breakout_8: prior completed bar target 100%; next bar open simulation |
| v1 | reversion_12 | 9685.33 | -314.67 | sell /  / reversion_12: prior completed bar target 0%; next bar open simulation |
| v1 | volume_26 | 9811.31 | -188.69 | sell /  / volume_26: prior completed bar target 0%; next bar open simulation |
| v1 | trend_8_26 AND momentum_26 | 9662.97 | -337.03 | sell /  / trend_8_26 AND momentum_26: prior completed bar target 0%; next bar open simulation |
| v1 | trend_8_26 + momentum_26 | 9663.17 | -336.83 | sell /  / trend_8_26 + momentum_26: prior completed bar target 0%; next bar open simulation |
| v1 | trend_8_26 AND breakout_8 | 9820.11 | -179.89 | sell /  / trend_8_26 AND breakout_8: prior completed bar target 0%; next bar open simulation |
| v1 | trend_8_26 + breakout_8 | 9709.59 | -290.41 | buy /  / trend_8_26 + breakout_8: prior completed bar target 50%; next bar open simulation |
| v1 | trend_8_26 AND reversion_12 | 9721.64 | -278.36 | sell /  / trend_8_26 AND reversion_12: prior completed bar target 0%; next bar open simulation |
| v1 | trend_8_26 + reversion_12 | 9681.35 | -318.65 | sell /  / trend_8_26 + reversion_12: prior completed bar target 0%; next bar open simulation |
| v1 | trend_8_26 AND volume_26 | 9916.79 | -83.21 | sell /  / trend_8_26 AND volume_26: prior completed bar target 0%; next bar open simulation |
| v1 | trend_8_26 + volume_26 | 9744.38 | -255.62 | sell /  / trend_8_26 + volume_26: prior completed bar target 0%; next bar open simulation |
| v1 | momentum_26 AND breakout_8 | 9820.11 | -179.89 | sell /  / momentum_26 AND breakout_8: prior completed bar target 0%; next bar open simulation |
| v1 | momentum_26 + breakout_8 | 9675.88 | -324.12 | buy /  / momentum_26 + breakout_8: prior completed bar target 50%; next bar open simulation |
| v1 | momentum_26 AND reversion_12 | 9707.47 | -292.53 | sell /  / momentum_26 AND reversion_12: prior completed bar target 0%; next bar open simulation |
| v1 | momentum_26 + reversion_12 | 9667.06 | -332.94 | sell /  / momentum_26 + reversion_12: prior completed bar target 0%; next bar open simulation |
| v1 | momentum_26 AND volume_26 | 9916.79 | -83.21 | sell /  / momentum_26 AND volume_26: prior completed bar target 0%; next bar open simulation |
| v1 | momentum_26 + volume_26 | 9730.00 | -270.00 | sell /  / momentum_26 + volume_26: prior completed bar target 0%; next bar open simulation |
| v1 | breakout_8 AND reversion_12 | 10000.00 | 0.00 | 대기 /  / 새 신호 대기 |
| v1 | breakout_8 + reversion_12 | 9713.20 | -286.80 | buy /  / breakout_8 + reversion_12: prior completed bar target 50%; next bar open simulation |
| v1 | breakout_8 AND volume_26 | 9953.19 | -46.81 | sell /  / breakout_8 AND volume_26: prior completed bar target 0%; next bar open simulation |
| v1 | breakout_8 + volume_26 | 9776.10 | -223.90 | buy /  / breakout_8 + volume_26: prior completed bar target 50%; next bar open simulation |
| v1 | reversion_12 AND volume_26 | 9938.00 | -62.00 | sell /  / reversion_12 AND volume_26: prior completed bar target 0%; next bar open simulation |
| v1 | reversion_12 + volume_26 | 9748.10 | -251.90 | sell /  / reversion_12 + volume_26: prior completed bar target 0%; next bar open simulation |
| v1 | ema_12_26 | 9662.97 | -337.03 | sell /  / EMA12 > EMA26; 조건 미충족; EMA12=532.823, EMA26=532.897 |
| v1 | macd_12_26_9 | 9837.76 | -162.24 | sell /  / MACD > 신호선 그리고 MACD > 0; 조건 미충족; MACD=0.667719, signal9=0.675659 |
| v1 | rsi_14_recovery | 9957.14 | -42.86 | sell /  / 직전 RSI14 < 30, 현재 RSI14 >= 30 (한 봉 목표); 조건 미충족; RSI14=45.5102, previous_RSI14=37.5844 |
| v1 | bollinger_20_reentry | 9854.81 | -145.19 | sell /  / 직전 종가 < 직전 하단밴드, 현재 하단밴드 <= 종가 <= SMA20 (한 봉 목표); 조건 미충족; close=531.675, lower20=529.239, SMA20=533.058, previous_lower20=529.387 |
| v1 | donchian_20 | 9912.16 | -87.84 | sell /  / 종가 > 현재 봉을 제외한 직전 20봉 최고가; 조건 미충족; close=534.52, prior_high20=535.44 |
| v1 | atr_14_breakout | 9915.10 | -84.90 | sell /  / 종가 > 직전 종가 + 직전 ATR14 그리고 종가 > EMA26; 조건 미충족; close=533.975, threshold=536.307, prior_ATR14=2.16203, EMA26=530.521 |
| v1 | session_vwap | 9911.80 | -88.20 | buy /  / 종가 > 뉴욕 거래일별 누적 전형가격 VWAP; 조건 충족; close=529.315, session_VWAP=528.789, session_volume=2.32763e+06 |
| v1 | obv_20 | 9781.02 | -218.98 | buy /  / OBV > OBV의 SMA20 그리고 종가 > EMA26; 조건 충족; OBV=9.21792e+07, OBV_SMA20=9.21309e+07, close=531.98, EMA26=531.962 |
| v1 | stochastic_14_3_recovery | 9789.03 | -210.97 | sell /  / 직전 %K14 < 20에서 %K14가 %D3 상향 돌파 (한 봉 목표); 조건 미충족; K14=60.6262, D3=34.5689, previous_K14=38.87, previous_D3=26.948 |
| v1 | mfi_14_recovery | 9972.58 | -27.42 | sell /  / 직전 MFI14 < 20, 현재 MFI14 >= 20 (한 봉 목표); 조건 미충족; MFI14=53.413, previous_MFI14=44.3372 |
| v1 | adx_14_trend | 9883.62 | -116.38 | sell /  / Wilder ADX14 >= 25 그리고 +DI14 > -DI14; 조건 미충족; ADX14=23.6824, plus_DI14=22.3066, minus_DI14=19.9214 |
| v1 | aroon_25_trend | 9812.47 | -187.53 | sell /  / Aroon25 Up > 70 그리고 Down < 30 (동률이면 최신 극값); 조건 미충족; Aroon_up=68, Aroon_down=20 |
| v1 | cci_20_momentum | 10012.15 | 12.15 | sell /  / CCI20 > 100 (전형가격·평균절대편차); 조건 미충족; CCI20=86.441 |
| v1 | williams_14_recovery | 9819.22 | -180.78 | sell /  / 직전 Williams %R14 < -80, 현재 >= -80 (한 봉 목표); 조건 미충족; Williams_R14=-39.3738, previous_R14=-61.13 |
| v1 | cmf_20_accumulation | 9741.38 | -258.62 | sell /  / Chaikin Money Flow20 > 0.1; 조건 미충족; CMF20=0.0660116, volume20=2.44678e+07 |
| v1 | chaikin_3_10 | 9770.74 | -229.26 | buy /  / ADL의 EMA3 - EMA10 > 0 그리고 종가 > EMA26; 조건 충족; Chaikin3_10=276696, ADL=1.10993e+08, close=531.98, EMA26=531.962 |
| v1 | roc_10_momentum | 9959.43 | -40.57 | sell /  / 10봉 ROC > 1% 그리고 종가 > EMA26; 조건 미충족; ROC10_percent=0.454191, close=534.125, EMA26=532.186 |
| v1 | trix_15_trend | 9712.42 | -287.58 | sell /  / 15봉 삼중 EMA의 1봉 변화율 TRIX > 0 그리고 종가 > EMA26; 조건 미충족; TRIX15_percent=0.0172213, close=526.676, EMA26=532.897 |
| v1 | keltner_20_breakout | 9958.78 | -41.22 | sell /  / 종가 > EMA20 + 2 x Wilder ATR14; 조건 미충족; close=533.975, upper_Keltner=534.357, EMA20=530.111, ATR14=2.12332 |
| v1 | opening_range_30m | 9711.79 | -288.21 | sell /  / 뉴욕 09:30·09:45 두 완료 봉 최고가를 10:00 이후 종가가 돌파; 자료 부족·변동폭 또는 거래량 없음: 대기; close=526.676 |
| v2 | cash | 10000.00 | 0.00 | 대기 /  / 새 신호 대기 |
| v2 | buy_hold | 9898.31 | -101.69 | buy / partial / 직전 완료 봉 목표 비중 100%; 다음 봉 시가 가정 |
| v2 | trend_8_26 | 9613.14 | -386.86 | sell / filled / 직전 완료 봉 목표 비중 0%; 다음 봉 시가 가정 |
| v2 | momentum_26 | 9692.90 | -307.10 | sell / filled / 직전 완료 봉 목표 비중 0%; 다음 봉 시가 가정 |
| v2 | breakout_8 | 9491.71 | -508.29 | buy / partial / 직전 완료 봉 목표 비중 100%; 다음 봉 시가 가정 |
| v2 | reversion_12 | 9308.50 | -691.50 | sell / filled / 직전 완료 봉 목표 비중 0%; 다음 봉 시가 가정 |
| v2 | volume_26 | 9498.13 | -501.87 | sell / filled / 직전 완료 봉 목표 비중 0%; 다음 봉 시가 가정 |
| v2 | trend_8_26 AND momentum_26 | 9560.49 | -439.51 | sell / filled / 직전 완료 봉 목표 비중 0%; 다음 봉 시가 가정 |
| v2 | trend_8_26 + momentum_26 | 9653.21 | -346.79 | sell / filled / 직전 완료 봉 목표 비중 0%; 다음 봉 시가 가정 |
| v2 | trend_8_26 AND breakout_8 | 9458.32 | -541.68 | sell / filled / 직전 완료 봉 목표 비중 0%; 다음 봉 시가 가정 |
| v2 | trend_8_26 + breakout_8 | 9592.91 | -407.09 | buy / filled / 직전 완료 봉 목표 비중 50%; 다음 봉 시가 가정 |
| v2 | trend_8_26 AND reversion_12 | 9618.75 | -381.25 | sell / filled / 직전 완료 봉 목표 비중 0%; 다음 봉 시가 가정 |
| v2 | trend_8_26 + reversion_12 | 9459.23 | -540.77 | sell / filled / 직전 완료 봉 목표 비중 0%; 다음 봉 시가 가정 |
| v2 | trend_8_26 AND volume_26 | 9861.94 | -138.06 | sell / filled / 직전 완료 봉 목표 비중 0%; 다음 봉 시가 가정 |
| v2 | trend_8_26 + volume_26 | 9575.59 | -424.41 | sell / filled / 직전 완료 봉 목표 비중 0%; 다음 봉 시가 가정 |
| v2 | momentum_26 AND breakout_8 | 9610.50 | -389.50 | sell / filled / 직전 완료 봉 목표 비중 0%; 다음 봉 시가 가정 |
| v2 | momentum_26 + breakout_8 | 9592.11 | -407.89 | buy / filled / 직전 완료 봉 목표 비중 50%; 다음 봉 시가 가정 |
| v2 | momentum_26 AND reversion_12 | 9533.70 | -466.30 | sell / filled / 직전 완료 봉 목표 비중 0%; 다음 봉 시가 가정 |
| v2 | momentum_26 + reversion_12 | 9498.52 | -501.48 | sell / filled / 직전 완료 봉 목표 비중 0%; 다음 봉 시가 가정 |
| v2 | momentum_26 AND volume_26 | 9785.21 | -214.79 | sell / filled / 직전 완료 봉 목표 비중 0%; 다음 봉 시가 가정 |
| v2 | momentum_26 + volume_26 | 9615.37 | -384.63 | sell / filled / 직전 완료 봉 목표 비중 0%; 다음 봉 시가 가정 |
| v2 | breakout_8 AND reversion_12 | 10000.00 | 0.00 | 대기 /  / 새 신호 대기 |
| v2 | breakout_8 + reversion_12 | 9438.91 | -561.09 | buy / filled / 직전 완료 봉 목표 비중 50%; 다음 봉 시가 가정 |
| v2 | breakout_8 AND volume_26 | 9890.09 | -109.91 | sell / filled / 직전 완료 봉 목표 비중 0%; 다음 봉 시가 가정 |
| v2 | breakout_8 + volume_26 | 9534.78 | -465.22 | buy / filled / 직전 완료 봉 목표 비중 50%; 다음 봉 시가 가정 |
| v2 | reversion_12 AND volume_26 | 9699.57 | -300.43 | sell / filled / 직전 완료 봉 목표 비중 0%; 다음 봉 시가 가정 |
| v2 | reversion_12 + volume_26 | 9402.66 | -597.34 | sell / filled / 직전 완료 봉 목표 비중 0%; 다음 봉 시가 가정 |
| v2 | ema_12_26 | 9659.11 | -340.89 | sell / filled / EMA12 > EMA26; 조건 미충족; EMA12=532.823, EMA26=532.897; 직전 완료 봉 목표를 다음 봉 시가에 모의 적용 |
| v2 | macd_12_26_9 | 9833.82 | -166.18 | sell / filled / MACD > 신호선 그리고 MACD > 0; 조건 미충족; MACD=0.667719, signal9=0.675659; 직전 완료 봉 목표를 다음 봉 시가에 모의 적용 |
| v2 | rsi_14_recovery | 9951.17 | -48.83 | sell / filled / 직전 RSI14 < 30, 현재 RSI14 >= 30 (한 봉 목표); 조건 미충족; RSI14=45.5102, previous_RSI14=37.5844; 직전 완료 봉 목표를 다음 봉 시가에 모의 적용 |
| v2 | bollinger_20_reentry | 9848.90 | -151.10 | sell / filled / 직전 종가 < 직전 하단밴드, 현재 하단밴드 <= 종가 <= SMA20 (한 봉 목표); 조건 미충족; close=531.675, lower20=529.239, SMA20=533.058, previous_lower20=529.387; 직전 완료 봉 목표를 다음 봉 시가에 모의 적용 |
| v2 | donchian_20 | 9908.19 | -91.81 | sell / filled / 종가 > 현재 봉을 제외한 직전 20봉 최고가; 조건 미충족; close=534.52, prior_high20=535.44; 직전 완료 봉 목표를 다음 봉 시가에 모의 적용 |
| v2 | atr_14_breakout | 9911.14 | -88.86 | sell / filled / 종가 > 직전 종가 + 직전 ATR14 그리고 종가 > EMA26; 조건 미충족; close=533.975, threshold=536.307, prior_ATR14=2.16203, EMA26=530.521; 직전 완료 봉 목표를 다음 봉 시가에 모의 적용 |
| v2 | session_vwap | 9904.87 | -95.13 | buy / partial / 종가 > 뉴욕 거래일별 누적 전형가격 VWAP; 조건 충족; close=529.315, session_VWAP=528.789, session_volume=2.32763e+06; 직전 완료 봉 목표를 다음 봉 시가에 모의 적용 |
| v2 | obv_20 | 9772.23 | -227.77 | buy / partial / OBV > OBV의 SMA20 그리고 종가 > EMA26; 조건 충족; OBV=9.21792e+07, OBV_SMA20=9.21309e+07, close=531.98, EMA26=531.962; 직전 완료 봉 목표를 다음 봉 시가에 모의 적용 |
| v2 | stochastic_14_3_recovery | 9779.25 | -220.75 | sell / filled / 직전 %K14 < 20에서 %K14가 %D3 상향 돌파 (한 봉 목표); 조건 미충족; K14=60.6262, D3=34.5689, previous_K14=38.87, previous_D3=26.948; 직전 완료 봉 목표를 다음 봉 시가에 모의 적용 |
| v2 | mfi_14_recovery | 9968.59 | -31.41 | sell / filled / 직전 MFI14 < 20, 현재 MFI14 >= 20 (한 봉 목표); 조건 미충족; MFI14=53.413, previous_MFI14=44.3372; 직전 완료 봉 목표를 다음 봉 시가에 모의 적용 |
| v2 | adx_14_trend | 9879.67 | -120.33 | sell / filled / Wilder ADX14 >= 25 그리고 +DI14 > -DI14; 조건 미충족; ADX14=23.6824, plus_DI14=22.3066, minus_DI14=19.9214; 직전 완료 봉 목표를 다음 봉 시가에 모의 적용 |
| v2 | aroon_25_trend | 9808.55 | -191.45 | sell / filled / Aroon25 Up > 70 그리고 Down < 30 (동률이면 최신 극값); 조건 미충족; Aroon_up=68, Aroon_down=20; 직전 완료 봉 목표를 다음 봉 시가에 모의 적용 |
| v2 | cci_20_momentum | 10010.15 | 10.15 | sell / filled / CCI20 > 100 (전형가격·평균절대편차); 조건 미충족; CCI20=86.441; 직전 완료 봉 목표를 다음 봉 시가에 모의 적용 |
| v2 | williams_14_recovery | 9811.37 | -188.63 | sell / filled / 직전 Williams %R14 < -80, 현재 >= -80 (한 봉 목표); 조건 미충족; Williams_R14=-39.3738, previous_R14=-61.13; 직전 완료 봉 목표를 다음 봉 시가에 모의 적용 |
| v2 | cmf_20_accumulation | 9737.48 | -262.52 | sell / filled / Chaikin Money Flow20 > 0.1; 조건 미충족; CMF20=0.0660116, volume20=2.44678e+07; 직전 완료 봉 목표를 다음 봉 시가에 모의 적용 |
| v2 | chaikin_3_10 | 9761.95 | -238.05 | buy / partial / ADL의 EMA3 - EMA10 > 0 그리고 종가 > EMA26; 조건 충족; Chaikin3_10=276696, ADL=1.10993e+08, close=531.98, EMA26=531.962; 직전 완료 봉 목표를 다음 봉 시가에 모의 적용 |
| v2 | roc_10_momentum | 9957.44 | -42.56 | sell / filled / 10봉 ROC > 1% 그리고 종가 > EMA26; 조건 미충족; ROC10_percent=0.454191, close=534.125, EMA26=532.186; 직전 완료 봉 목표를 다음 봉 시가에 모의 적용 |
| v2 | trix_15_trend | 9708.54 | -291.46 | sell / filled / 15봉 삼중 EMA의 1봉 변화율 TRIX > 0 그리고 종가 > EMA26; 조건 미충족; TRIX15_percent=0.0172213, close=526.676, EMA26=532.897; 직전 완료 봉 목표를 다음 봉 시가에 모의 적용 |
| v2 | keltner_20_breakout | 9956.78 | -43.22 | sell / filled / 종가 > EMA20 + 2 x Wilder ATR14; 조건 미충족; close=533.975, upper_Keltner=534.357, EMA20=530.111, ATR14=2.12332; 직전 완료 봉 목표를 다음 봉 시가에 모의 적용 |
| v2 | opening_range_30m | 9707.90 | -292.10 | sell / filled / 뉴욕 09:30·09:45 두 완료 봉 최고가를 10:00 이후 종가가 돌파; 자료 부족·변동폭 또는 거래량 없음: 대기; close=526.676; 직전 완료 봉 목표를 다음 봉 시가에 모의 적용 |

### 같은 기간의 비용·노출 비교 (사후 연구)

| 전략 | 비용 전 | 비용 후 | 100% 보유 | 같은 평균 노출 보유 | 평균 노출 |
|---|---:|---:|---:|---:|---:|
| cash | 0.00% | 0.00% | 4.18% | 0.00% | 0.00% |
| buy_hold | 4.62% | 4.18% | 4.18% | 4.18% | 100.00% |
| trend_8_26 | 1.35% | -1.99% | 4.18% | 2.46% | 59.58% |
| momentum_26 | 0.34% | -4.99% | 4.18% | 2.51% | 60.89% |
| breakout_8 | 6.53% | -8.81% | 4.18% | 0.83% | 20.47% |
| reversion_12 | -4.30% | -12.75% | 4.18% | 0.97% | 23.88% |
| volume_26 | 1.03% | -7.11% | 4.18% | 0.34% | 8.40% |
| trend_8_26 AND momentum_26 | -0.74% | -6.41% | 4.18% | 2.28% | 55.38% |
| trend_8_26 + momentum_26 | 0.85% | -3.49% | 4.18% | 2.48% | 60.24% |
| trend_8_26 AND breakout_8 | 0.70% | -10.09% | 4.18% | 0.54% | 13.39% |
| trend_8_26 + breakout_8 | 3.93% | -4.85% | 4.18% | 1.64% | 40.03% |
| trend_8_26 AND reversion_12 | -1.41% | -7.04% | 4.18% | 0.28% | 6.82% |
| trend_8_26 + reversion_12 | -1.50% | -7.34% | 4.18% | 1.71% | 41.74% |
| trend_8_26 AND volume_26 | 3.42% | -0.42% | 4.18% | 0.13% | 3.15% |
| trend_8_26 + volume_26 | 1.21% | -3.98% | 4.18% | 1.39% | 33.99% |
| momentum_26 AND breakout_8 | 2.99% | -8.05% | 4.18% | 0.54% | 13.39% |
| momentum_26 + breakout_8 | 3.40% | -6.52% | 4.18% | 1.67% | 40.69% |
| momentum_26 AND reversion_12 | -2.41% | -9.14% | 4.18% | 0.39% | 9.71% |
| momentum_26 + reversion_12 | -1.99% | -8.95% | 4.18% | 1.74% | 42.39% |
| momentum_26 AND volume_26 | 1.07% | -3.49% | 4.18% | 0.15% | 3.67% |
| momentum_26 + volume_26 | 0.70% | -5.26% | 4.18% | 1.42% | 34.65% |
| breakout_8 AND reversion_12 | 0.00% | 0.00% | 4.18% | 0.00% | 0.00% |
| breakout_8 + reversion_12 | 0.99% | -10.05% | 4.18% | 0.90% | 22.19% |
| breakout_8 AND volume_26 | 2.04% | -0.50% | 4.18% | 0.07% | 1.84% |
| breakout_8 + volume_26 | 3.75% | -6.99% | 4.18% | 0.59% | 14.44% |
| reversion_12 AND volume_26 | -2.90% | -6.11% | 4.18% | 0.14% | 3.41% |
| reversion_12 + volume_26 | -1.66% | -9.97% | 4.18% | 0.66% | 16.15% |
| ema_12_26 | 0.48% | -2.84% | 4.18% | 2.54% | 61.68% |
| macd_12_26_9 | 1.45% | -3.54% | 4.18% | 1.42% | 34.65% |
| rsi_14_recovery | 0.31% | -2.19% | 4.18% | 0.06% | 1.57% |
| bollinger_20_reentry | -0.92% | -3.79% | 4.18% | 0.07% | 1.84% |
| donchian_20 | 1.76% | -4.05% | 4.18% | 0.20% | 4.99% |
| atr_14_breakout | 1.72% | -3.69% | 4.18% | 0.15% | 3.67% |
| session_vwap | 7.56% | -0.69% | 4.18% | 1.72% | 41.99% |
| obv_20 | 6.01% | -2.53% | 4.18% | 1.99% | 48.56% |
| stochastic_14_3_recovery | -0.50% | -10.42% | 4.18% | 0.27% | 6.56% |
| mfi_14_recovery | 1.58% | -2.19% | 4.18% | 0.10% | 2.36% |
| adx_14_trend | 3.84% | 1.26% | 4.18% | 1.91% | 46.46% |
| aroon_25_trend | 0.07% | -4.85% | 4.18% | 0.93% | 22.83% |
| cci_20_momentum | 3.43% | -2.89% | 4.18% | 0.90% | 22.05% |
| williams_14_recovery | -1.26% | -9.97% | 4.18% | 0.23% | 5.77% |
| cmf_20_accumulation | 0.70% | -4.65% | 4.18% | 1.34% | 32.81% |
| chaikin_3_10 | 4.79% | -3.65% | 4.18% | 1.90% | 46.19% |
| roc_10_momentum | -0.01% | -4.12% | 4.18% | 0.64% | 15.75% |
| trix_15_trend | -0.85% | -4.93% | 4.18% | 2.05% | 49.87% |
| keltner_20_breakout | 1.11% | -4.26% | 4.18% | 0.55% | 13.65% |
| opening_range_30m | -0.96% | -4.64% | 4.18% | 0.92% | 22.57% |

동일 구간·초기 자금, 종료 시 청산 비용 포함. 노출 맞춤은 사후 설명용이며 v2 실제 계좌 성과가 아닙니다.
[낙폭 분해·비용 영향·전체 구간](MSFT/comparison.json)

[v1 전체 기록](MSFT/accounts.json) · [v2 전체 기록](MSFT/accounts-v2.json)

## JPM 계좌

| 모델 | 전략 | 평가액 USD | 손익 USD | 최근 매매·이유 |
|---|---|---:|---:|---|
| v1 | cash | 10000.00 | 0.00 | 대기 /  / 새 신호 대기 |
| v1 | buy_hold | 9853.49 | -146.51 | buy /  / buy_hold: prior completed bar target 100%; next bar open simulation |
| v1 | trend_8_26 | 9805.18 | -194.82 | buy /  / trend_8_26: prior completed bar target 100%; next bar open simulation |
| v1 | momentum_26 | 9706.33 | -293.67 | sell /  / momentum_26: prior completed bar target 0%; next bar open simulation |
| v1 | breakout_8 | 9759.46 | -240.54 | sell /  / breakout_8: prior completed bar target 0%; next bar open simulation |
| v1 | reversion_12 | 9739.19 | -260.81 | buy /  / reversion_12: prior completed bar target 100%; next bar open simulation |
| v1 | volume_26 | 9961.97 | -38.03 | sell /  / volume_26: prior completed bar target 0%; next bar open simulation |
| v1 | trend_8_26 AND momentum_26 | 9793.49 | -206.51 | sell /  / trend_8_26 AND momentum_26: prior completed bar target 0%; next bar open simulation |
| v1 | trend_8_26 + momentum_26 | 9755.63 | -244.37 | sell /  / trend_8_26 + momentum_26: prior completed bar target 50%; next bar open simulation |
| v1 | trend_8_26 AND breakout_8 | 9915.55 | -84.45 | sell /  / trend_8_26 AND breakout_8: prior completed bar target 0%; next bar open simulation |
| v1 | trend_8_26 + breakout_8 | 9801.89 | -198.11 | sell /  / trend_8_26 + breakout_8: prior completed bar target 50%; next bar open simulation |
| v1 | trend_8_26 AND reversion_12 | 9874.76 | -125.24 | buy /  / trend_8_26 AND reversion_12: prior completed bar target 100%; next bar open simulation |
| v1 | trend_8_26 + reversion_12 | 9772.03 | -227.97 | buy /  / trend_8_26 + reversion_12: prior completed bar target 100%; next bar open simulation |
| v1 | trend_8_26 AND volume_26 | 10035.68 | 35.68 | sell /  / trend_8_26 AND volume_26: prior completed bar target 0%; next bar open simulation |
| v1 | trend_8_26 + volume_26 | 9883.11 | -116.89 | sell /  / trend_8_26 + volume_26: prior completed bar target 50%; next bar open simulation |
| v1 | momentum_26 AND breakout_8 | 9733.77 | -266.23 | sell /  / momentum_26 AND breakout_8: prior completed bar target 0%; next bar open simulation |
| v1 | momentum_26 + breakout_8 | 9732.95 | -267.05 | sell /  / momentum_26 + breakout_8: prior completed bar target 0%; next bar open simulation |
| v1 | momentum_26 AND reversion_12 | 9881.87 | -118.13 | sell /  / momentum_26 AND reversion_12: prior completed bar target 0%; next bar open simulation |
| v1 | momentum_26 + reversion_12 | 9761.65 | -238.35 | sell /  / momentum_26 + reversion_12: prior completed bar target 50%; next bar open simulation |
| v1 | momentum_26 AND volume_26 | 10035.68 | 35.68 | sell /  / momentum_26 AND volume_26: prior completed bar target 0%; next bar open simulation |
| v1 | momentum_26 + volume_26 | 9852.93 | -147.07 | sell /  / momentum_26 + volume_26: prior completed bar target 0%; next bar open simulation |
| v1 | breakout_8 AND reversion_12 | 10000.00 | 0.00 | 대기 /  / 새 신호 대기 |
| v1 | breakout_8 + reversion_12 | 9788.29 | -211.71 | sell /  / breakout_8 + reversion_12: prior completed bar target 50%; next bar open simulation |
| v1 | breakout_8 AND volume_26 | 10022.00 | 22.00 | sell /  / breakout_8 AND volume_26: prior completed bar target 0%; next bar open simulation |
| v1 | breakout_8 + volume_26 | 9860.16 | -139.84 | sell /  / breakout_8 + volume_26: prior completed bar target 0%; next bar open simulation |
| v1 | reversion_12 AND volume_26 | 9940.10 | -59.90 | sell /  / reversion_12 AND volume_26: prior completed bar target 0%; next bar open simulation |
| v1 | reversion_12 + volume_26 | 9869.58 | -130.42 | sell /  / reversion_12 + volume_26: prior completed bar target 50%; next bar open simulation |
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
| v1 | cmf_20_accumulation | 9886.91 | -113.09 | sell /  / Chaikin Money Flow20 > 0.1; 조건 미충족; CMF20=0.0812849, volume20=3.96407e+06 |
| v1 | chaikin_3_10 | 9837.22 | -162.78 | sell /  / ADL의 EMA3 - EMA10 > 0 그리고 종가 > EMA26; 조건 미충족; Chaikin3_10=7273.89, ADL=-1.28498e+07, close=336.08, EMA26=336.65 |
| v1 | roc_10_momentum | 9836.40 | -163.60 | sell /  / 10봉 ROC > 1% 그리고 종가 > EMA26; 조건 미충족; ROC10_percent=0.964142, close=337.72, EMA26=336.695 |
| v1 | trix_15_trend | 9723.73 | -276.27 | sell /  / 15봉 삼중 EMA의 1봉 변화율 TRIX > 0 그리고 종가 > EMA26; 조건 미충족; TRIX15_percent=0.0135144, close=337.6, EMA26=338.759 |
| v1 | keltner_20_breakout | 9905.24 | -94.76 | sell /  / 종가 > EMA20 + 2 x Wilder ATR14; 조건 미충족; close=339.04, upper_Keltner=339.281, EMA20=336.559, ATR14=1.36146 |
| v1 | opening_range_30m | 9850.26 | -149.74 | sell /  / 뉴욕 09:30·09:45 두 완료 봉 최고가를 10:00 이후 종가가 돌파; 조건 미충족; close=337.72, opening_high=339.035 |
| v2 | cash | 10000.00 | 0.00 | 대기 /  / 새 신호 대기 |
| v2 | buy_hold | 10018.14 | 18.14 | buy / partial / 직전 완료 봉 목표 비중 100%; 다음 봉 시가 가정 |
| v2 | trend_8_26 | 9811.24 | -188.76 | buy / partial / 직전 완료 봉 목표 비중 100%; 다음 봉 시가 가정 |
| v2 | momentum_26 | 9219.07 | -780.93 | sell / filled / 직전 완료 봉 목표 비중 0%; 다음 봉 시가 가정 |
| v2 | breakout_8 | 9100.10 | -899.90 | sell / filled / 직전 완료 봉 목표 비중 0%; 다음 봉 시가 가정 |
| v2 | reversion_12 | 9714.85 | -285.15 | buy / partial / 직전 완료 봉 목표 비중 100%; 다음 봉 시가 가정 |
| v2 | volume_26 | 9781.50 | -218.50 | sell / filled / 직전 완료 봉 목표 비중 0%; 다음 봉 시가 가정 |
| v2 | trend_8_26 AND momentum_26 | 9756.41 | -243.59 | sell / filled / 직전 완료 봉 목표 비중 0%; 다음 봉 시가 가정 |
| v2 | trend_8_26 + momentum_26 | 9531.06 | -468.94 | sell / filled / 직전 완료 봉 목표 비중 50%; 다음 봉 시가 가정 |
| v2 | trend_8_26 AND breakout_8 | 9287.76 | -712.24 | sell / filled / 직전 완료 봉 목표 비중 0%; 다음 봉 시가 가정 |
| v2 | trend_8_26 + breakout_8 | 9469.91 | -530.09 | sell / filled / 직전 완료 봉 목표 비중 50%; 다음 봉 시가 가정 |
| v2 | trend_8_26 AND reversion_12 | 9851.68 | -148.32 | buy / partial / 직전 완료 봉 목표 비중 100%; 다음 봉 시가 가정 |
| v2 | trend_8_26 + reversion_12 | 9804.12 | -195.88 | buy / partial / 직전 완료 봉 목표 비중 100%; 다음 봉 시가 가정 |
| v2 | trend_8_26 AND volume_26 | 9833.30 | -166.70 | sell / filled / 직전 완료 봉 목표 비중 0%; 다음 봉 시가 가정 |
| v2 | trend_8_26 + volume_26 | 9797.03 | -202.97 | sell / filled / 직전 완료 봉 목표 비중 50%; 다음 봉 시가 가정 |
| v2 | momentum_26 AND breakout_8 | 9058.00 | -942.00 | sell / filled / 직전 완료 봉 목표 비중 0%; 다음 봉 시가 가정 |
| v2 | momentum_26 + breakout_8 | 9180.31 | -819.69 | sell / filled / 직전 완료 봉 목표 비중 0%; 다음 봉 시가 가정 |
| v2 | momentum_26 AND reversion_12 | 9827.31 | -172.69 | sell / filled / 직전 완료 봉 목표 비중 0%; 다음 봉 시가 가정 |
| v2 | momentum_26 + reversion_12 | 9624.52 | -375.48 | sell / filled / 직전 완료 봉 목표 비중 50%; 다음 봉 시가 가정 |
| v2 | momentum_26 AND volume_26 | 9833.30 | -166.70 | sell / filled / 직전 완료 봉 목표 비중 0%; 다음 봉 시가 가정 |
| v2 | momentum_26 + volume_26 | 9577.38 | -422.62 | sell / filled / 직전 완료 봉 목표 비중 0%; 다음 봉 시가 가정 |
| v2 | breakout_8 AND reversion_12 | 10000.00 | 0.00 | 대기 /  / 새 신호 대기 |
| v2 | breakout_8 + reversion_12 | 9481.87 | -518.13 | sell / filled / 직전 완료 봉 목표 비중 50%; 다음 봉 시가 가정 |
| v2 | breakout_8 AND volume_26 | 9911.14 | -88.86 | sell / filled / 직전 완료 봉 목표 비중 0%; 다음 봉 시가 가정 |
| v2 | breakout_8 + volume_26 | 9454.59 | -545.41 | sell / filled / 직전 완료 봉 목표 비중 0%; 다음 봉 시가 가정 |
| v2 | reversion_12 AND volume_26 | 9987.18 | -12.82 | sell / filled / 직전 완료 봉 목표 비중 0%; 다음 봉 시가 가정 |
| v2 | reversion_12 + volume_26 | 9789.32 | -210.68 | sell / filled / 직전 완료 봉 목표 비중 50%; 다음 봉 시가 가정 |
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
| v2 | cmf_20_accumulation | 9882.96 | -117.04 | sell / filled / Chaikin Money Flow20 > 0.1; 조건 미충족; CMF20=0.0812849, volume20=3.96407e+06; 직전 완료 봉 목표를 다음 봉 시가에 모의 적용 |
| v2 | chaikin_3_10 | 9831.32 | -168.68 | sell / filled / ADL의 EMA3 - EMA10 > 0 그리고 종가 > EMA26; 조건 미충족; Chaikin3_10=7273.89, ADL=-1.28498e+07, close=336.08, EMA26=336.65; 직전 완료 봉 목표를 다음 봉 시가에 모의 적용 |
| v2 | roc_10_momentum | 9832.47 | -167.53 | sell / filled / 10봉 ROC > 1% 그리고 종가 > EMA26; 조건 미충족; ROC10_percent=0.964142, close=337.72, EMA26=336.695; 직전 완료 봉 목표를 다음 봉 시가에 모의 적용 |
| v2 | trix_15_trend | 9715.96 | -284.04 | sell / filled / 15봉 삼중 EMA의 1봉 변화율 TRIX > 0 그리고 종가 > EMA26; 조건 미충족; TRIX15_percent=0.0135144, close=337.6, EMA26=338.759; 직전 완료 봉 목표를 다음 봉 시가에 모의 적용 |
| v2 | keltner_20_breakout | 9901.28 | -98.72 | sell / filled / 종가 > EMA20 + 2 x Wilder ATR14; 조건 미충족; close=339.04, upper_Keltner=339.281, EMA20=336.559, ATR14=1.36146; 직전 완료 봉 목표를 다음 봉 시가에 모의 적용 |
| v2 | opening_range_30m | 9846.33 | -153.67 | sell / filled / 뉴욕 09:30·09:45 두 완료 봉 최고가를 10:00 이후 종가가 돌파; 조건 미충족; close=337.72, opening_high=339.035; 직전 완료 봉 목표를 다음 봉 시가에 모의 적용 |

### 같은 기간의 비용·노출 비교 (사후 연구)

| 전략 | 비용 전 | 비용 후 | 100% 보유 | 같은 평균 노출 보유 | 평균 노출 |
|---|---:|---:|---:|---:|---:|
| cash | 0.00% | 0.00% | -0.30% | -0.00% | 0.00% |
| buy_hold | 0.12% | -0.30% | -0.30% | -0.30% | 100.00% |
| trend_8_26 | 0.22% | -3.90% | -0.30% | -0.16% | 54.07% |
| momentum_26 | -3.06% | -10.12% | -0.30% | -0.15% | 49.61% |
| breakout_8 | -2.73% | -17.43% | -0.30% | -0.06% | 19.69% |
| reversion_12 | 5.19% | -9.57% | -0.30% | -0.08% | 26.77% |
| volume_26 | 0.25% | -6.27% | -0.30% | -0.02% | 7.09% |
| trend_8_26 AND momentum_26 | 0.56% | -4.38% | -0.30% | -0.13% | 41.21% |
| trend_8_26 + momentum_26 | -1.42% | -6.86% | -0.30% | -0.16% | 51.84% |
| trend_8_26 AND breakout_8 | -3.21% | -13.22% | -0.30% | -0.04% | 12.07% |
| trend_8_26 + breakout_8 | -1.25% | -10.53% | -0.30% | -0.11% | 36.88% |
| trend_8_26 AND reversion_12 | 2.61% | -4.06% | -0.30% | -0.03% | 8.40% |
| trend_8_26 + reversion_12 | 2.70% | -6.19% | -0.30% | -0.12% | 40.43% |
| trend_8_26 AND volume_26 | -0.42% | -4.11% | -0.30% | -0.01% | 3.94% |
| trend_8_26 + volume_26 | 0.25% | -5.09% | -0.30% | -0.09% | 30.58% |
| momentum_26 AND breakout_8 | -2.68% | -13.84% | -0.30% | -0.04% | 12.60% |
| momentum_26 + breakout_8 | -2.87% | -13.65% | -0.30% | -0.11% | 34.65% |
| momentum_26 AND reversion_12 | 2.79% | -4.29% | -0.30% | -0.02% | 6.82% |
| momentum_26 + reversion_12 | 1.01% | -8.12% | -0.30% | -0.12% | 38.19% |
| momentum_26 AND volume_26 | 0.21% | -2.70% | -0.30% | -0.01% | 2.89% |
| momentum_26 + volume_26 | -1.39% | -7.82% | -0.30% | -0.09% | 28.35% |
| breakout_8 AND reversion_12 | 0.00% | 0.00% | -0.30% | -0.00% | 0.00% |
| breakout_8 + reversion_12 | 1.17% | -12.31% | -0.30% | -0.07% | 23.24% |
| breakout_8 AND volume_26 | -0.25% | -2.32% | -0.30% | -0.00% | 1.31% |
| breakout_8 + volume_26 | -1.24% | -11.28% | -0.30% | -0.04% | 13.39% |
| reversion_12 AND volume_26 | 1.33% | -2.01% | -0.30% | -0.01% | 3.41% |
| reversion_12 + volume_26 | 2.70% | -6.97% | -0.30% | -0.05% | 16.93% |
| ema_12_26 | -0.24% | -3.54% | -0.30% | -0.16% | 51.97% |
| macd_12_26_9 | -0.13% | -4.64% | -0.30% | -0.10% | 32.81% |
| rsi_14_recovery | 0.47% | -2.03% | -0.30% | -0.00% | 1.57% |
| bollinger_20_reentry | 0.51% | -3.62% | -0.30% | -0.01% | 2.62% |
| donchian_20 | -1.81% | -5.05% | -0.30% | -0.01% | 3.15% |
| atr_14_breakout | -1.35% | -8.92% | -0.30% | -0.02% | 5.25% |
| session_vwap | 1.67% | -7.69% | -0.30% | -0.14% | 46.72% |
| obv_20 | -3.42% | -13.78% | -0.30% | -0.09% | 29.92% |
| stochastic_14_3_recovery | -1.37% | -11.94% | -0.30% | -0.02% | 7.09% |
| mfi_14_recovery | 0.32% | -2.18% | -0.30% | -0.00% | 1.57% |
| adx_14_trend | -2.43% | -4.85% | -0.30% | -0.09% | 29.66% |
| aroon_25_trend | -1.12% | -5.19% | -0.30% | -0.07% | 22.57% |
| cci_20_momentum | -2.84% | -10.67% | -0.30% | -0.05% | 16.27% |
| williams_14_recovery | -0.99% | -10.48% | -0.30% | -0.02% | 6.30% |
| cmf_20_accumulation | -1.80% | -10.09% | -0.30% | -0.09% | 28.87% |
| chaikin_3_10 | 1.01% | -7.52% | -0.30% | -0.10% | 33.86% |
| roc_10_momentum | -1.36% | -4.22% | -0.30% | -0.03% | 8.40% |
| trix_15_trend | -1.25% | -8.83% | -0.30% | -0.11% | 35.17% |
| keltner_20_breakout | -1.21% | -4.07% | -0.30% | -0.01% | 4.20% |
| opening_range_30m | -0.23% | -3.93% | -0.30% | -0.05% | 17.32% |

동일 구간·초기 자금, 종료 시 청산 비용 포함. 노출 맞춤은 사후 설명용이며 v2 실제 계좌 성과가 아닙니다.
[낙폭 분해·비용 영향·전체 구간](JPM/comparison.json)

[v1 전체 기록](JPM/accounts.json) · [v2 전체 기록](JPM/accounts-v2.json)

## XOM 계좌

| 모델 | 전략 | 평가액 USD | 손익 USD | 최근 매매·이유 |
|---|---|---:|---:|---|
| v1 | cash | 10000.00 | 0.00 | 대기 /  / 새 신호 대기 |
| v1 | buy_hold | 10001.52 | 1.52 | buy /  / buy_hold: prior completed bar target 100%; next bar open simulation |
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
| v1 | session_vwap | 9953.99 | -46.01 | buy /  / 종가 > 뉴욕 거래일별 누적 전형가격 VWAP; 조건 충족; close=176.885, session_VWAP=176.63, session_volume=5.45281e+06 |
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
| v2 | buy_hold | 10320.69 | 320.69 | buy / partial / 직전 완료 봉 목표 비중 100%; 다음 봉 시가 가정 |
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
| v2 | session_vwap | 9947.03 | -52.97 | buy / partial / 종가 > 뉴욕 거래일별 누적 전형가격 VWAP; 조건 충족; close=176.885, session_VWAP=176.63, session_volume=5.45281e+06; 직전 완료 봉 목표를 다음 봉 시가에 모의 적용 |
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
| cash | 0.00% | 0.00% | 9.14% | 0.00% | 0.00% |
| buy_hold | 9.60% | 9.14% | 9.14% | 9.14% | 100.00% |
| trend_8_26 | 1.08% | -3.49% | 9.14% | 6.22% | 69.03% |
| momentum_26 | 2.06% | -4.98% | 9.14% | 6.68% | 74.02% |
| breakout_8 | -0.42% | -18.94% | 9.14% | 2.45% | 27.82% |
| reversion_12 | 2.68% | -6.77% | 9.14% | 1.85% | 21.00% |
| volume_26 | 2.43% | -5.43% | 9.14% | 0.48% | 5.51% |
| trend_8_26 AND momentum_26 | -0.07% | -5.38% | 9.14% | 5.63% | 62.73% |
| trend_8_26 + momentum_26 | 1.57% | -4.03% | 9.14% | 6.45% | 71.53% |
| trend_8_26 AND breakout_8 | -0.36% | -15.77% | 9.14% | 1.92% | 21.78% |
| trend_8_26 + breakout_8 | 0.35% | -11.16% | 9.14% | 4.32% | 48.43% |
| trend_8_26 AND reversion_12 | -1.96% | -7.56% | 9.14% | 0.87% | 9.97% |
| trend_8_26 + reversion_12 | 1.90% | -4.94% | 9.14% | 4.01% | 45.02% |
| trend_8_26 AND volume_26 | 1.38% | -3.20% | 9.14% | 0.27% | 3.15% |
| trend_8_26 + volume_26 | 1.77% | -4.26% | 9.14% | 3.30% | 37.27% |
| momentum_26 AND breakout_8 | -0.66% | -18.11% | 9.14% | 2.27% | 25.72% |
| momentum_26 + breakout_8 | 0.83% | -12.22% | 9.14% | 4.55% | 50.93% |
| momentum_26 AND reversion_12 | -0.44% | -6.91% | 9.14% | 0.90% | 10.24% |
| momentum_26 + reversion_12 | 2.40% | -4.68% | 9.14% | 4.23% | 47.51% |
| momentum_26 AND volume_26 | 2.15% | -1.64% | 9.14% | 0.21% | 2.36% |
| momentum_26 + volume_26 | 2.27% | -4.00% | 9.14% | 3.53% | 39.77% |
| breakout_8 AND reversion_12 | 0.00% | 0.00% | 9.14% | 0.00% | 0.00% |
| breakout_8 + reversion_12 | 1.14% | -12.89% | 9.14% | 2.15% | 24.42% |
| breakout_8 AND volume_26 | 0.51% | -1.17% | 9.14% | 0.09% | 1.05% |
| breakout_8 + volume_26 | 1.01% | -11.52% | 9.14% | 1.46% | 16.67% |
| reversion_12 AND volume_26 | 0.29% | -2.62% | 9.14% | 0.18% | 2.10% |
| reversion_12 + volume_26 | 2.57% | -5.31% | 9.14% | 1.16% | 13.26% |
| ema_12_26 | 1.19% | -1.75% | 9.14% | 7.17% | 79.27% |
| macd_12_26_9 | 0.29% | -5.43% | 9.14% | 3.87% | 43.57% |
| rsi_14_recovery | -0.08% | -1.33% | 9.14% | 0.07% | 0.79% |
| bollinger_20_reentry | -1.07% | -3.94% | 9.14% | 0.16% | 1.84% |
| donchian_20 | -0.93% | -10.43% | 9.14% | 0.85% | 9.71% |
| atr_14_breakout | 0.47% | -8.01% | 9.14% | 0.50% | 5.77% |
| session_vwap | 1.91% | -9.02% | 9.14% | 5.97% | 66.40% |
| obv_20 | 2.64% | -6.03% | 9.14% | 4.42% | 49.61% |
| stochastic_14_3_recovery | 0.79% | -8.49% | 9.14% | 0.53% | 6.04% |
| mfi_14_recovery | -0.31% | -1.97% | 9.14% | 0.09% | 1.05% |
| adx_14_trend | 3.88% | 0.87% | 9.14% | 3.95% | 44.36% |
| aroon_25_trend | -3.42% | -10.08% | 9.14% | 3.19% | 35.96% |
| cci_20_momentum | 3.54% | -5.60% | 9.14% | 2.57% | 29.13% |
| williams_14_recovery | -0.90% | -6.95% | 9.14% | 0.34% | 3.94% |
| cmf_20_accumulation | 1.45% | -5.54% | 9.14% | 4.38% | 49.08% |
| chaikin_3_10 | 1.63% | -6.55% | 9.14% | 5.34% | 59.58% |
| roc_10_momentum | 0.80% | -5.36% | 9.14% | 1.15% | 13.12% |
| trix_15_trend | 0.95% | -5.21% | 9.14% | 6.04% | 67.19% |
| keltner_20_breakout | 0.18% | -6.72% | 9.14% | 1.52% | 17.32% |
| opening_range_30m | 0.63% | -8.64% | 9.14% | 3.07% | 34.65% |

동일 구간·초기 자금, 종료 시 청산 비용 포함. 노출 맞춤은 사후 설명용이며 v2 실제 계좌 성과가 아닙니다.
[낙폭 분해·비용 영향·전체 구간](XOM/comparison.json)

[v1 전체 기록](XOM/accounts.json) · [v2 전체 기록](XOM/accounts-v2.json)

## JNJ 계좌

| 모델 | 전략 | 평가액 USD | 손익 USD | 최근 매매·이유 |
|---|---|---:|---:|---|
| v1 | cash | 10000.00 | 0.00 | 대기 /  / 새 신호 대기 |
| v1 | buy_hold | 10122.20 | 122.20 | buy /  / buy_hold: prior completed bar target 100%; next bar open simulation |
| v1 | trend_8_26 | 10073.53 | 73.53 | buy /  / trend_8_26: prior completed bar target 100%; next bar open simulation |
| v1 | momentum_26 | 9844.13 | -155.87 | buy /  / momentum_26: prior completed bar target 100%; next bar open simulation |
| v1 | breakout_8 | 9513.91 | -486.09 | sell /  / breakout_8: prior completed bar target 0%; next bar open simulation |
| v1 | reversion_12 | 9868.44 | -131.56 | sell /  / reversion_12: prior completed bar target 0%; next bar open simulation |
| v1 | volume_26 | 9943.90 | -56.10 | sell /  / volume_26: prior completed bar target 0%; next bar open simulation |
| v1 | trend_8_26 AND momentum_26 | 9896.09 | -103.91 | buy /  / trend_8_26 AND momentum_26: prior completed bar target 100%; next bar open simulation |
| v1 | trend_8_26 + momentum_26 | 9958.47 | -41.53 | buy /  / trend_8_26 + momentum_26: prior completed bar target 100%; next bar open simulation |
| v1 | trend_8_26 AND breakout_8 | 9814.73 | -185.27 | sell /  / trend_8_26 AND breakout_8: prior completed bar target 0%; next bar open simulation |
| v1 | trend_8_26 + breakout_8 | 9809.55 | -190.45 | sell /  / trend_8_26 + breakout_8: prior completed bar target 50%; next bar open simulation |
| v1 | trend_8_26 AND reversion_12 | 9968.65 | -31.35 | sell /  / trend_8_26 AND reversion_12: prior completed bar target 0%; next bar open simulation |
| v1 | trend_8_26 + reversion_12 | 9970.57 | -29.43 | sell /  / trend_8_26 + reversion_12: prior completed bar target 50%; next bar open simulation |
| v1 | trend_8_26 AND volume_26 | 9995.12 | -4.88 | sell /  / trend_8_26 AND volume_26: prior completed bar target 0%; next bar open simulation |
| v1 | trend_8_26 + volume_26 | 10008.72 | 8.72 | sell /  / trend_8_26 + volume_26: prior completed bar target 50%; next bar open simulation |
| v1 | momentum_26 AND breakout_8 | 9833.49 | -166.51 | sell /  / momentum_26 AND breakout_8: prior completed bar target 0%; next bar open simulation |
| v1 | momentum_26 + breakout_8 | 9677.45 | -322.55 | sell /  / momentum_26 + breakout_8: prior completed bar target 50%; next bar open simulation |
| v1 | momentum_26 AND reversion_12 | 9976.62 | -23.38 | sell /  / momentum_26 AND reversion_12: prior completed bar target 0%; next bar open simulation |
| v1 | momentum_26 + reversion_12 | 9875.87 | -124.13 | sell /  / momentum_26 + reversion_12: prior completed bar target 50%; next bar open simulation |
| v1 | momentum_26 AND volume_26 | 10000.00 | 0.00 | 대기 /  / 새 신호 대기 |
| v1 | momentum_26 + volume_26 | 9933.54 | -66.46 | sell /  / momentum_26 + volume_26: prior completed bar target 50%; next bar open simulation |
| v1 | breakout_8 AND reversion_12 | 10000.00 | 0.00 | 대기 /  / 새 신호 대기 |
| v1 | breakout_8 + reversion_12 | 9689.37 | -310.63 | sell /  / breakout_8 + reversion_12: prior completed bar target 0%; next bar open simulation |
| v1 | breakout_8 AND volume_26 | 10000.00 | 0.00 | 대기 /  / 새 신호 대기 |
| v1 | breakout_8 + volume_26 | 9745.99 | -254.01 | sell /  / breakout_8 + volume_26: prior completed bar target 0%; next bar open simulation |
| v1 | reversion_12 AND volume_26 | 9974.59 | -25.41 | sell /  / reversion_12 AND volume_26: prior completed bar target 0%; next bar open simulation |
| v1 | reversion_12 + volume_26 | 9925.96 | -74.04 | sell /  / reversion_12 + volume_26: prior completed bar target 0%; next bar open simulation |
| v1 | ema_12_26 | 9942.77 | -57.23 | buy /  / EMA12 > EMA26; 조건 충족; EMA12=253.915, EMA26=253.911 |
| v1 | macd_12_26_9 | 9887.47 | -112.53 | sell /  / MACD > 신호선 그리고 MACD > 0; 조건 미충족; MACD=1.30676, signal9=1.31668 |
| v1 | rsi_14_recovery | 9923.04 | -76.96 | sell /  / 직전 RSI14 < 30, 현재 RSI14 >= 30 (한 봉 목표); 조건 미충족; RSI14=40.3665, previous_RSI14=36.2025 |
| v1 | bollinger_20_reentry | 9881.04 | -118.96 | sell /  / 직전 종가 < 직전 하단밴드, 현재 하단밴드 <= 종가 <= SMA20 (한 봉 목표); 조건 미충족; close=251.75, lower20=251.316, SMA20=254.208, previous_lower20=251.691 |
| v1 | donchian_20 | 9921.02 | -78.98 | sell /  / 종가 > 현재 봉을 제외한 직전 20봉 최고가; 조건 미충족; close=258.68, prior_high20=260.425 |
| v1 | atr_14_breakout | 9805.90 | -194.10 | sell /  / 종가 > 직전 종가 + 직전 ATR14 그리고 종가 > EMA26; 조건 미충족; close=258.68, threshold=261.221, prior_ATR14=1.00083, EMA26=254.754 |
| v1 | session_vwap | 9832.03 | -167.97 | sell /  / 종가 > 뉴욕 거래일별 누적 전형가격 VWAP; 조건 미충족; close=258.91, session_VWAP=259.405, session_volume=4.28557e+06 |
| v1 | obv_20 | 9675.94 | -324.06 | buy /  / OBV > OBV의 SMA20 그리고 종가 > EMA26; 조건 충족; OBV=4.78456e+06, OBV_SMA20=3.4932e+06, close=254.04, EMA26=253.978 |
| v1 | stochastic_14_3_recovery | 9862.87 | -137.13 | sell /  / 직전 %K14 < 20에서 %K14가 %D3 상향 돌파 (한 봉 목표); 조건 미충족; K14=28.9392, D3=18.1738, previous_K14=19.7943, previous_D3=12.6561 |
| v1 | mfi_14_recovery | 10000.00 | 0.00 | 대기 /  / 새 신호 대기 |
| v1 | adx_14_trend | 9802.85 | -197.15 | buy /  / Wilder ADX14 >= 25 그리고 +DI14 > -DI14; 조건 충족; ADX14=27.0884, plus_DI14=47.0278, minus_DI14=11.4099 |
| v1 | aroon_25_trend | 9899.46 | -100.54 | sell /  / Aroon25 Up > 70 그리고 Down < 30 (동률이면 최신 극값); 조건 미충족; Aroon_up=68, Aroon_down=44 |
| v1 | cci_20_momentum | 9818.66 | -181.34 | sell /  / CCI20 > 100 (전형가격·평균절대편차); 조건 미충족; CCI20=95.1073 |
| v1 | williams_14_recovery | 9903.67 | -96.33 | sell /  / 직전 Williams %R14 < -80, 현재 >= -80 (한 봉 목표); 조건 미충족; Williams_R14=-61.3372, previous_R14=-71.0608 |
| v1 | cmf_20_accumulation | 10249.15 | 249.15 | buy /  / Chaikin Money Flow20 > 0.1; 조건 충족; CMF20=0.280188, volume20=5.69706e+06 |
| v1 | chaikin_3_10 | 9894.90 | -105.10 | buy /  / ADL의 EMA3 - EMA10 > 0 그리고 종가 > EMA26; 조건 충족; Chaikin3_10=250777, ADL=4.30146e+06, close=254.04, EMA26=253.978 |
| v1 | roc_10_momentum | 9691.76 | -308.24 | sell /  / 10봉 ROC > 1% 그리고 종가 > EMA26; 조건 미충족; ROC10_percent=-0.503419, close=258.91, EMA26=257.09 |
| v1 | trix_15_trend | 9786.36 | -213.64 | buy /  / 15봉 삼중 EMA의 1봉 변화율 TRIX > 0 그리고 종가 > EMA26; 조건 충족; TRIX15_percent=0.000945132, close=260.22, EMA26=254.44 |
| v1 | keltner_20_breakout | 9916.04 | -83.96 | sell /  / 종가 > EMA20 + 2 x Wilder ATR14; 조건 미충족; close=258.91, upper_Keltner=259.564, EMA20=257.603, ATR14=0.980686 |
| v1 | opening_range_30m | 10000.00 | 0.00 | 대기 /  / 새 신호 대기 |
| v2 | cash | 10000.00 | 0.00 | 대기 /  / 새 신호 대기 |
| v2 | buy_hold | 9885.96 | -114.04 | 중단: 손실 한도 / buy / partial / 직전 완료 봉 목표 비중 100%; 다음 봉 시가 가정 |
| v2 | trend_8_26 | 9885.96 | -114.04 | 중단: 손실 한도 / buy / partial / 직전 완료 봉 목표 비중 100%; 다음 봉 시가 가정 |
| v2 | momentum_26 | 9885.96 | -114.04 | 중단: 손실 한도 / buy / partial / 직전 완료 봉 목표 비중 100%; 다음 봉 시가 가정 |
| v2 | breakout_8 | 9343.39 | -656.61 | 중단: 손실 한도 / sell / filled / 직전 완료 봉 목표 비중 0%; 다음 봉 시가 가정 |
| v2 | reversion_12 | 9556.92 | -443.08 | sell / filled / 직전 완료 봉 목표 비중 0%; 다음 봉 시가 가정 |
| v2 | volume_26 | 9728.64 | -271.36 | sell / filled / 직전 완료 봉 목표 비중 0%; 다음 봉 시가 가정 |
| v2 | trend_8_26 AND momentum_26 | 9885.96 | -114.04 | 중단: 손실 한도 / buy / partial / 직전 완료 봉 목표 비중 100%; 다음 봉 시가 가정 |
| v2 | trend_8_26 + momentum_26 | 9885.96 | -114.04 | 중단: 손실 한도 / buy / partial / 직전 완료 봉 목표 비중 100%; 다음 봉 시가 가정 |
| v2 | trend_8_26 AND breakout_8 | 9419.39 | -580.61 | 중단: 손실 한도 / sell / filled / 직전 완료 봉 목표 비중 0%; 다음 봉 시가 가정 |
| v2 | trend_8_26 + breakout_8 | 9378.63 | -621.37 | sell / filled / 직전 완료 봉 목표 비중 50%; 다음 봉 시가 가정 |
| v2 | trend_8_26 AND reversion_12 | 9942.82 | -57.18 | sell / filled / 직전 완료 봉 목표 비중 0%; 다음 봉 시가 가정 |
| v2 | trend_8_26 + reversion_12 | 9732.92 | -267.08 | 중단: 손실 한도 / sell / filled / 직전 완료 봉 목표 비중 0%; 다음 봉 시가 가정 |
| v2 | trend_8_26 AND volume_26 | 9861.95 | -138.05 | sell / filled / 직전 완료 봉 목표 비중 0%; 다음 봉 시가 가정 |
| v2 | trend_8_26 + volume_26 | 9917.94 | -82.06 | 중단: 손실 한도 / buy / filled / 직전 완료 봉 목표 비중 50%; 다음 봉 시가 가정 |
| v2 | momentum_26 AND breakout_8 | 9435.09 | -564.91 | sell / filled / 직전 완료 봉 목표 비중 0%; 다음 봉 시가 가정 |
| v2 | momentum_26 + breakout_8 | 9242.72 | -757.28 | sell / filled / 직전 완료 봉 목표 비중 50%; 다음 봉 시가 가정 |
| v2 | momentum_26 AND reversion_12 | 9913.65 | -86.35 | sell / filled / 직전 완료 봉 목표 비중 0%; 다음 봉 시가 가정 |
| v2 | momentum_26 + reversion_12 | 9732.92 | -267.08 | 중단: 손실 한도 / sell / filled / 직전 완료 봉 목표 비중 0%; 다음 봉 시가 가정 |
| v2 | momentum_26 AND volume_26 | 9920.93 | -79.07 | sell / filled / 직전 완료 봉 목표 비중 0%; 다음 봉 시가 가정 |
| v2 | momentum_26 + volume_26 | 9917.94 | -82.06 | 중단: 손실 한도 / buy / filled / 직전 완료 봉 목표 비중 50%; 다음 봉 시가 가정 |
| v2 | breakout_8 AND reversion_12 | 10000.00 | 0.00 | 대기 /  / 새 신호 대기 |
| v2 | breakout_8 + reversion_12 | 9272.30 | -727.70 | sell / filled / 직전 완료 봉 목표 비중 0%; 다음 봉 시가 가정 |
| v2 | breakout_8 AND volume_26 | 9814.17 | -185.83 | sell / filled / 직전 완료 봉 목표 비중 0%; 다음 봉 시가 가정 |
| v2 | breakout_8 + volume_26 | 9355.32 | -644.68 | sell / filled / 직전 완료 봉 목표 비중 0%; 다음 봉 시가 가정 |
| v2 | reversion_12 AND volume_26 | 9859.15 | -140.85 | sell / filled / 직전 완료 봉 목표 비중 0%; 다음 봉 시가 가정 |
| v2 | reversion_12 + volume_26 | 9683.25 | -316.75 | sell / filled / 직전 완료 봉 목표 비중 0%; 다음 봉 시가 가정 |
| v2 | ema_12_26 | 9937.80 | -62.20 | buy / partial / EMA12 > EMA26; 조건 충족; EMA12=253.915, EMA26=253.911; 직전 완료 봉 목표를 다음 봉 시가에 모의 적용 |
| v2 | macd_12_26_9 | 9881.54 | -118.46 | sell / filled / MACD > 신호선 그리고 MACD > 0; 조건 미충족; MACD=1.30676, signal9=1.31668; 직전 완료 봉 목표를 다음 봉 시가에 모의 적용 |
| v2 | rsi_14_recovery | 9919.07 | -80.93 | sell / filled / 직전 RSI14 < 30, 현재 RSI14 >= 30 (한 봉 목표); 조건 미충족; RSI14=40.3665, previous_RSI14=36.2025; 직전 완료 봉 목표를 다음 봉 시가에 모의 적용 |
| v2 | bollinger_20_reentry | 9877.09 | -122.91 | sell / filled / 직전 종가 < 직전 하단밴드, 현재 하단밴드 <= 종가 <= SMA20 (한 봉 목표); 조건 미충족; close=251.75, lower20=251.316, SMA20=254.208, previous_lower20=251.691; 직전 완료 봉 목표를 다음 봉 시가에 모의 적용 |
| v2 | donchian_20 | 9919.03 | -80.97 | sell / filled / 종가 > 현재 봉을 제외한 직전 20봉 최고가; 조건 미충족; close=258.68, prior_high20=260.425; 직전 완료 봉 목표를 다음 봉 시가에 모의 적용 |
| v2 | atr_14_breakout | 9800.02 | -199.98 | sell / filled / 종가 > 직전 종가 + 직전 ATR14 그리고 종가 > EMA26; 조건 미충족; close=258.68, threshold=261.221, prior_ATR14=1.00083, EMA26=254.754; 직전 완료 봉 목표를 다음 봉 시가에 모의 적용 |
| v2 | session_vwap | 9818.27 | -181.73 | sell / filled / 종가 > 뉴욕 거래일별 누적 전형가격 VWAP; 조건 미충족; close=258.91, session_VWAP=259.405, session_volume=4.28557e+06; 직전 완료 봉 목표를 다음 봉 시가에 모의 적용 |
| v2 | obv_20 | 9663.37 | -336.63 | buy / partial / OBV > OBV의 SMA20 그리고 종가 > EMA26; 조건 충족; OBV=4.78456e+06, OBV_SMA20=3.4932e+06, close=254.04, EMA26=253.978; 직전 완료 봉 목표를 다음 봉 시가에 모의 적용 |
| v2 | stochastic_14_3_recovery | 9856.96 | -143.04 | sell / filled / 직전 %K14 < 20에서 %K14가 %D3 상향 돌파 (한 봉 목표); 조건 미충족; K14=28.9392, D3=18.1738, previous_K14=19.7943, previous_D3=12.6561; 직전 완료 봉 목표를 다음 봉 시가에 모의 적용 |
| v2 | mfi_14_recovery | 10000.00 | 0.00 | 대기 /  / 새 신호 대기 |
| v2 | adx_14_trend | 9795.99 | -204.01 | buy / partial / Wilder ADX14 >= 25 그리고 +DI14 > -DI14; 조건 충족; ADX14=27.0884, plus_DI14=47.0278, minus_DI14=11.4099; 직전 완료 봉 목표를 다음 봉 시가에 모의 적용 |
| v2 | aroon_25_trend | 9895.50 | -104.50 | sell / filled / Aroon25 Up > 70 그리고 Down < 30 (동률이면 최신 극값); 조건 미충족; Aroon_up=68, Aroon_down=44; 직전 완료 봉 목표를 다음 봉 시가에 모의 적용 |
| v2 | cci_20_momentum | 9812.77 | -187.23 | sell / filled / CCI20 > 100 (전형가격·평균절대편차); 조건 미충족; CCI20=95.1073; 직전 완료 봉 목표를 다음 봉 시가에 모의 적용 |
| v2 | williams_14_recovery | 9899.71 | -100.29 | sell / filled / 직전 Williams %R14 < -80, 현재 >= -80 (한 봉 목표); 조건 미충족; Williams_R14=-61.3372, previous_R14=-71.0608; 직전 완료 봉 목표를 다음 봉 시가에 모의 적용 |
| v2 | cmf_20_accumulation | 10248.13 | 248.13 | buy / partial / Chaikin Money Flow20 > 0.1; 조건 충족; CMF20=0.280188, volume20=5.69706e+06; 직전 완료 봉 목표를 다음 봉 시가에 모의 적용 |
| v2 | chaikin_3_10 | 9887.98 | -112.02 | buy / partial / ADL의 EMA3 - EMA10 > 0 그리고 종가 > EMA26; 조건 충족; Chaikin3_10=250777, ADL=4.30146e+06, close=254.04, EMA26=253.978; 직전 완료 봉 목표를 다음 봉 시가에 모의 적용 |
| v2 | roc_10_momentum | 9684.01 | -315.99 | sell / filled / 10봉 ROC > 1% 그리고 종가 > EMA26; 조건 미충족; ROC10_percent=-0.503419, close=258.91, EMA26=257.09; 직전 완료 봉 목표를 다음 봉 시가에 모의 적용 |
| v2 | trix_15_trend | 9781.47 | -218.53 | buy / partial / 15봉 삼중 EMA의 1봉 변화율 TRIX > 0 그리고 종가 > EMA26; 조건 충족; TRIX15_percent=0.000945132, close=260.22, EMA26=254.44; 직전 완료 봉 목표를 다음 봉 시가에 모의 적용 |
| v2 | keltner_20_breakout | 9914.05 | -85.95 | sell / filled / 종가 > EMA20 + 2 x Wilder ATR14; 조건 미충족; close=258.91, upper_Keltner=259.564, EMA20=257.603, ATR14=0.980686; 직전 완료 봉 목표를 다음 봉 시가에 모의 적용 |
| v2 | opening_range_30m | 10000.00 | 0.00 | 대기 /  / 새 신호 대기 |

### 같은 기간의 비용·노출 비교 (사후 연구)

| 전략 | 비용 전 | 비용 후 | 100% 보유 | 같은 평균 노출 보유 | 평균 노출 |
|---|---:|---:|---:|---:|---:|
| cash | 0.00% | 0.00% | -3.41% | -0.00% | 0.00% |
| buy_hold | -3.00% | -3.41% | -3.41% | -3.41% | 100.00% |
| trend_8_26 | 3.26% | 0.69% | -3.41% | -1.73% | 49.61% |
| momentum_26 | -0.13% | -3.83% | -3.41% | -1.64% | 46.98% |
| breakout_8 | -1.40% | -18.38% | -3.41% | -0.71% | 20.21% |
| reversion_12 | -6.90% | -14.76% | -3.41% | -1.06% | 30.18% |
| volume_26 | -0.92% | -7.75% | -3.41% | -0.23% | 6.56% |
| trend_8_26 AND momentum_26 | 1.13% | -2.21% | -3.41% | -1.46% | 41.73% |
| trend_8_26 + momentum_26 | 1.56% | -1.59% | -3.41% | -1.68% | 48.30% |
| trend_8_26 AND breakout_8 | 0.12% | -11.73% | -3.41% | -0.48% | 13.65% |
| trend_8_26 + breakout_8 | 0.93% | -9.13% | -3.41% | -1.22% | 34.91% |
| trend_8_26 AND reversion_12 | 1.04% | -2.30% | -3.41% | -0.20% | 5.51% |
| trend_8_26 + reversion_12 | -1.91% | -6.96% | -3.41% | -1.39% | 39.90% |
| trend_8_26 AND volume_26 | 1.42% | -1.10% | -3.41% | -0.06% | 1.57% |
| trend_8_26 + volume_26 | 1.19% | -3.40% | -3.41% | -0.99% | 28.09% |
| momentum_26 AND breakout_8 | 0.98% | -9.84% | -3.41% | -0.45% | 12.86% |
| momentum_26 + breakout_8 | -0.74% | -11.20% | -3.41% | -1.18% | 33.60% |
| momentum_26 AND reversion_12 | -0.65% | -3.13% | -3.41% | -0.20% | 5.77% |
| momentum_26 + reversion_12 | -3.54% | -8.88% | -3.41% | -1.35% | 38.59% |
| momentum_26 AND volume_26 | 0.14% | -0.70% | -3.41% | -0.02% | 0.52% |
| momentum_26 + volume_26 | -0.49% | -4.80% | -3.41% | -0.94% | 26.77% |
| breakout_8 AND reversion_12 | 0.00% | 0.00% | -3.41% | -0.00% | 0.00% |
| breakout_8 + reversion_12 | -4.17% | -16.07% | -3.41% | -0.89% | 25.21% |
| breakout_8 AND volume_26 | -0.91% | -2.15% | -3.41% | -0.03% | 0.79% |
| breakout_8 + volume_26 | -1.15% | -12.31% | -3.41% | -0.47% | 13.39% |
| reversion_12 AND volume_26 | -1.84% | -4.69% | -3.41% | -0.10% | 2.89% |
| reversion_12 + volume_26 | -3.94% | -10.57% | -3.41% | -0.65% | 18.38% |
| ema_12_26 | 0.49% | -2.01% | -3.41% | -1.51% | 43.31% |
| macd_12_26_9 | 5.83% | 2.76% | -3.41% | -1.03% | 29.40% |
| rsi_14_recovery | -1.35% | -6.20% | -3.41% | -0.11% | 3.15% |
| bollinger_20_reentry | -1.10% | -5.56% | -3.41% | -0.10% | 2.89% |
| donchian_20 | 0.23% | -7.07% | -3.41% | -0.24% | 6.82% |
| atr_14_breakout | 0.79% | -5.36% | -3.41% | -0.17% | 4.72% |
| session_vwap | 3.37% | -4.96% | -3.41% | -1.72% | 49.34% |
| obv_20 | -5.41% | -14.48% | -3.41% | -1.22% | 34.91% |
| stochastic_14_3_recovery | -0.31% | -12.11% | -3.41% | -0.28% | 7.87% |
| mfi_14_recovery | 0.33% | -0.93% | -3.41% | -0.03% | 0.79% |
| adx_14_trend | -2.57% | -7.75% | -3.41% | -1.20% | 34.38% |
| aroon_25_trend | 3.81% | -0.46% | -3.41% | -1.08% | 30.71% |
| cci_20_momentum | 0.20% | -6.70% | -3.41% | -0.77% | 21.78% |
| williams_14_recovery | -1.58% | -8.74% | -3.41% | -0.17% | 4.72% |
| cmf_20_accumulation | 5.32% | 1.41% | -3.41% | -1.11% | 31.76% |
| chaikin_3_10 | -2.79% | -7.95% | -3.41% | -1.27% | 36.22% |
| roc_10_momentum | -2.79% | -9.49% | -3.41% | -0.62% | 17.59% |
| trix_15_trend | -0.58% | -3.05% | -3.41% | -1.15% | 32.81% |
| keltner_20_breakout | 0.20% | -3.52% | -3.41% | -0.42% | 11.81% |
| opening_range_30m | 0.79% | -2.95% | -3.41% | -0.91% | 25.98% |

동일 구간·초기 자금, 종료 시 청산 비용 포함. 노출 맞춤은 사후 설명용이며 v2 실제 계좌 성과가 아닙니다.
[낙폭 분해·비용 영향·전체 구간](JNJ/comparison.json)

[v1 전체 기록](JNJ/accounts.json) · [v2 전체 기록](JNJ/accounts-v2.json)

## CAT 계좌

| 모델 | 전략 | 평가액 USD | 손익 USD | 최근 매매·이유 |
|---|---|---:|---:|---|
| v1 | cash | 10000.00 | 0.00 | 대기 /  / 새 신호 대기 |
| v1 | buy_hold | 9856.36 | -143.64 | buy /  / buy_hold: prior completed bar target 100%; next bar open simulation |
| v1 | trend_8_26 | 9829.12 | -170.88 | sell /  / trend_8_26: prior completed bar target 0%; next bar open simulation |
| v1 | momentum_26 | 9765.06 | -234.94 | sell /  / momentum_26: prior completed bar target 0%; next bar open simulation |
| v1 | breakout_8 | 9687.36 | -312.64 | sell /  / breakout_8: prior completed bar target 0%; next bar open simulation |
| v1 | reversion_12 | 9940.40 | -59.60 | buy /  / reversion_12: prior completed bar target 100%; next bar open simulation |
| v1 | volume_26 | 10007.30 | 7.30 | sell /  / volume_26: prior completed bar target 0%; next bar open simulation |
| v1 | trend_8_26 AND momentum_26 | 9873.91 | -126.09 | sell /  / trend_8_26 AND momentum_26: prior completed bar target 0%; next bar open simulation |
| v1 | trend_8_26 + momentum_26 | 9797.24 | -202.76 | sell /  / trend_8_26 + momentum_26: prior completed bar target 0%; next bar open simulation |
| v1 | trend_8_26 AND breakout_8 | 9850.32 | -149.68 | sell /  / trend_8_26 AND breakout_8: prior completed bar target 0%; next bar open simulation |
| v1 | trend_8_26 + breakout_8 | 9758.16 | -241.84 | sell /  / trend_8_26 + breakout_8: prior completed bar target 0%; next bar open simulation |
| v1 | trend_8_26 AND reversion_12 | 9928.06 | -71.94 | sell /  / trend_8_26 AND reversion_12: prior completed bar target 0%; next bar open simulation |
| v1 | trend_8_26 + reversion_12 | 9924.92 | -75.08 | sell /  / trend_8_26 + reversion_12: prior completed bar target 50%; next bar open simulation |
| v1 | trend_8_26 AND volume_26 | 10000.00 | 0.00 | 대기 /  / 새 신호 대기 |
| v1 | trend_8_26 + volume_26 | 9937.74 | -62.26 | sell /  / trend_8_26 + volume_26: prior completed bar target 0%; next bar open simulation |
| v1 | momentum_26 AND breakout_8 | 9804.82 | -195.18 | sell /  / momentum_26 AND breakout_8: prior completed bar target 0%; next bar open simulation |
| v1 | momentum_26 + breakout_8 | 9726.19 | -273.81 | sell /  / momentum_26 + breakout_8: prior completed bar target 0%; next bar open simulation |
| v1 | momentum_26 AND reversion_12 | 9887.21 | -112.79 | sell /  / momentum_26 AND reversion_12: prior completed bar target 0%; next bar open simulation |
| v1 | momentum_26 + reversion_12 | 9853.07 | -146.93 | sell /  / momentum_26 + reversion_12: prior completed bar target 50%; next bar open simulation |
| v1 | momentum_26 AND volume_26 | 9985.43 | -14.57 | sell /  / momentum_26 AND volume_26: prior completed bar target 0%; next bar open simulation |
| v1 | momentum_26 + volume_26 | 9885.51 | -114.49 | sell /  / momentum_26 + volume_26: prior completed bar target 0%; next bar open simulation |
| v1 | breakout_8 AND reversion_12 | 10000.00 | 0.00 | 대기 /  / 새 신호 대기 |
| v1 | breakout_8 + reversion_12 | 9813.62 | -186.38 | sell /  / breakout_8 + reversion_12: prior completed bar target 50%; next bar open simulation |
| v1 | breakout_8 AND volume_26 | 9985.43 | -14.57 | sell /  / breakout_8 AND volume_26: prior completed bar target 0%; next bar open simulation |
| v1 | breakout_8 + volume_26 | 9846.03 | -153.97 | sell /  / breakout_8 + volume_26: prior completed bar target 0%; next bar open simulation |
| v1 | reversion_12 AND volume_26 | 10046.29 | 46.29 | sell /  / reversion_12 AND volume_26: prior completed bar target 0%; next bar open simulation |
| v1 | reversion_12 + volume_26 | 9974.30 | -25.70 | sell /  / reversion_12 + volume_26: prior completed bar target 50%; next bar open simulation |
| v1 | ema_12_26 | 9862.47 | -137.53 | sell /  / EMA12 > EMA26; 조건 미충족; EMA12=735.622, EMA26=735.711 |
| v1 | macd_12_26_9 | 9904.18 | -95.82 | sell /  / MACD > 신호선 그리고 MACD > 0; 조건 미충족; MACD=0.746548, signal9=0.752293 |
| v1 | rsi_14_recovery | 9999.22 | -0.78 | sell /  / 직전 RSI14 < 30, 현재 RSI14 >= 30 (한 봉 목표); 조건 미충족; RSI14=43.621, previous_RSI14=38.5787 |
| v1 | bollinger_20_reentry | 9777.09 | -222.91 | sell /  / 직전 종가 < 직전 하단밴드, 현재 하단밴드 <= 종가 <= SMA20 (한 봉 목표); 조건 미충족; close=721.16, lower20=716.851, SMA20=725.821, previous_lower20=717.276 |
| v1 | donchian_20 | 9950.83 | -49.17 | sell /  / 종가 > 현재 봉을 제외한 직전 20봉 최고가; 조건 미충족; close=739.81, prior_high20=742.28 |
| v1 | atr_14_breakout | 9775.74 | -224.26 | sell /  / 종가 > 직전 종가 + 직전 ATR14 그리고 종가 > EMA26; 조건 미충족; close=732.42, threshold=735.931, prior_ATR14=4.99094, EMA26=726.612 |
| v1 | session_vwap | 9389.60 | -610.40 | sell /  / 종가 > 뉴욕 거래일별 누적 전형가격 VWAP; 조건 미충족; close=722.65, session_VWAP=723.935, session_volume=1.94253e+06 |
| v1 | obv_20 | 9683.67 | -316.33 | sell /  / OBV > OBV의 SMA20 그리고 종가 > EMA26; 조건 미충족; OBV=-5.85317e+06, OBV_SMA20=-5.80449e+06, close=725.22, EMA26=726.751 |
| v1 | stochastic_14_3_recovery | 9855.08 | -144.92 | sell /  / 직전 %K14 < 20에서 %K14가 %D3 상향 돌파 (한 봉 목표); 조건 미충족; K14=59.6496, D3=39.2535, previous_K14=43.8356, previous_D3=33.8642 |
| v1 | mfi_14_recovery | 10068.63 | 68.63 | sell /  / 직전 MFI14 < 20, 현재 MFI14 >= 20 (한 봉 목표); 조건 미충족; MFI14=32.7313, previous_MFI14=24.1736 |
| v1 | adx_14_trend | 10000.00 | 0.00 | 대기 /  / 새 신호 대기 |
| v1 | aroon_25_trend | 10031.15 | 31.15 | sell /  / Aroon25 Up > 70 그리고 Down < 30 (동률이면 최신 극값); 조건 미충족; Aroon_up=88, Aroon_down=48 |
| v1 | cci_20_momentum | 9890.31 | -109.69 | sell /  / CCI20 > 100 (전형가격·평균절대편차); 조건 미충족; CCI20=20.3547 |
| v1 | williams_14_recovery | 10007.06 | 7.06 | sell /  / 직전 Williams %R14 < -80, 현재 >= -80 (한 봉 목표); 조건 미충족; Williams_R14=-40.3504, previous_R14=-56.1644 |
| v1 | cmf_20_accumulation | 9783.68 | -216.32 | buy /  / Chaikin Money Flow20 > 0.1; 조건 충족; CMF20=0.130083, volume20=2.38752e+06 |
| v1 | chaikin_3_10 | 9474.17 | -525.83 | sell /  / ADL의 EMA3 - EMA10 > 0 그리고 종가 > EMA26; 조건 미충족; Chaikin3_10=39681.6, ADL=-6.22839e+06, close=725.22, EMA26=726.751 |
| v1 | roc_10_momentum | 9963.13 | -36.87 | sell /  / 10봉 ROC > 1% 그리고 종가 > EMA26; 조건 미충족; ROC10_percent=-0.134597, close=734.53, EMA26=735.486 |
| v1 | trix_15_trend | 9669.78 | -330.22 | sell /  / 15봉 삼중 EMA의 1봉 변화율 TRIX > 0 그리고 종가 > EMA26; 조건 미충족; TRIX15_percent=0.0186631, close=734.925, EMA26=736.093 |
| v1 | keltner_20_breakout | 10000.00 | 0.00 | 대기 /  / 새 신호 대기 |
| v1 | opening_range_30m | 10071.07 | 71.07 | buy /  / 뉴욕 09:30·09:45 두 완료 봉 최고가를 10:00 이후 종가가 돌파; 조건 충족; close=721.16, opening_high=718.07 |
| v2 | cash | 10000.00 | 0.00 | 대기 /  / 새 신호 대기 |
| v2 | buy_hold | 9064.64 | -935.36 | 중단: 손실 한도 / buy / partial / 직전 완료 봉 목표 비중 100%; 다음 봉 시가 가정 |
| v2 | trend_8_26 | 9749.27 | -250.73 | sell / filled / 직전 완료 봉 목표 비중 0%; 다음 봉 시가 가정 |
| v2 | momentum_26 | 9775.40 | -224.60 | sell / filled / 직전 완료 봉 목표 비중 0%; 다음 봉 시가 가정 |
| v2 | breakout_8 | 9506.39 | -493.61 | sell / filled / 직전 완료 봉 목표 비중 0%; 다음 봉 시가 가정 |
| v2 | reversion_12 | 8938.05 | -1061.95 | 중단: 손실 한도 / buy / partial / 직전 완료 봉 목표 비중 100%; 다음 봉 시가 가정 |
| v2 | volume_26 | 9193.67 | -806.33 | 중단: 손실 한도 / buy / partial / 직전 완료 봉 목표 비중 100%; 다음 봉 시가 가정 |
| v2 | trend_8_26 AND momentum_26 | 9914.96 | -85.04 | sell / filled / 직전 완료 봉 목표 비중 0%; 다음 봉 시가 가정 |
| v2 | trend_8_26 + momentum_26 | 9762.53 | -237.47 | sell / filled / 직전 완료 봉 목표 비중 0%; 다음 봉 시가 가정 |
| v2 | trend_8_26 AND breakout_8 | 9765.08 | -234.92 | sell / filled / 직전 완료 봉 목표 비중 0%; 다음 봉 시가 가정 |
| v2 | trend_8_26 + breakout_8 | 9627.50 | -372.50 | sell / filled / 직전 완료 봉 목표 비중 0%; 다음 봉 시가 가정 |
| v2 | trend_8_26 AND reversion_12 | 9738.62 | -261.38 | sell / filled / 직전 완료 봉 목표 비중 0%; 다음 봉 시가 가정 |
| v2 | trend_8_26 + reversion_12 | 9543.83 | -456.17 | sell / filled / 직전 완료 봉 목표 비중 50%; 다음 봉 시가 가정 |
| v2 | trend_8_26 AND volume_26 | 10035.44 | 35.44 | sell / filled / 직전 완료 봉 목표 비중 0%; 다음 봉 시가 가정 |
| v2 | trend_8_26 + volume_26 | 9568.27 | -431.73 | sell / filled / 직전 완료 봉 목표 비중 0%; 다음 봉 시가 가정 |
| v2 | momentum_26 AND breakout_8 | 9776.83 | -223.17 | sell / filled / 직전 완료 봉 목표 비중 0%; 다음 봉 시가 가정 |
| v2 | momentum_26 + breakout_8 | 9640.20 | -359.80 | sell / filled / 직전 완료 봉 목표 비중 0%; 다음 봉 시가 가정 |
| v2 | momentum_26 AND reversion_12 | 9755.55 | -244.45 | sell / filled / 직전 완료 봉 목표 비중 0%; 다음 봉 시가 가정 |
| v2 | momentum_26 + reversion_12 | 9516.58 | -483.42 | sell / filled / 직전 완료 봉 목표 비중 50%; 다음 봉 시가 가정 |
| v2 | momentum_26 AND volume_26 | 10032.13 | 32.13 | sell / filled / 직전 완료 봉 목표 비중 0%; 다음 봉 시가 가정 |
| v2 | momentum_26 + volume_26 | 9581.08 | -418.92 | sell / filled / 직전 완료 봉 목표 비중 0%; 다음 봉 시가 가정 |
| v2 | breakout_8 AND reversion_12 | 10000.00 | 0.00 | 대기 /  / 새 신호 대기 |
| v2 | breakout_8 + reversion_12 | 9610.18 | -389.82 | 중단: 손실 한도 / sell / filled / 직전 완료 봉 목표 비중 0%; 다음 봉 시가 가정 |
| v2 | breakout_8 AND volume_26 | 9982.12 | -17.88 | sell / filled / 직전 완료 봉 목표 비중 0%; 다음 봉 시가 가정 |
| v2 | breakout_8 + volume_26 | 9448.42 | -551.58 | sell / filled / 직전 완료 봉 목표 비중 0%; 다음 봉 시가 가정 |
| v2 | reversion_12 AND volume_26 | 9130.07 | -869.93 | 중단: 손실 한도 / buy / partial / 직전 완료 봉 목표 비중 100%; 다음 봉 시가 가정 |
| v2 | reversion_12 + volume_26 | 9331.11 | -668.89 | 중단: 손실 한도 / sell / filled / 직전 완료 봉 목표 비중 50%; 다음 봉 시가 가정 |
| v2 | ema_12_26 | 9860.50 | -139.50 | sell / filled / EMA12 > EMA26; 조건 미충족; EMA12=735.622, EMA26=735.711; 직전 완료 봉 목표를 다음 봉 시가에 모의 적용 |
| v2 | macd_12_26_9 | 9902.20 | -97.80 | sell / filled / MACD > 신호선 그리고 MACD > 0; 조건 미충족; MACD=0.746548, signal9=0.752293; 직전 완료 봉 목표를 다음 봉 시가에 모의 적용 |
| v2 | rsi_14_recovery | 9995.22 | -4.78 | sell / filled / 직전 RSI14 < 30, 현재 RSI14 >= 30 (한 봉 목표); 조건 미충족; RSI14=43.621, previous_RSI14=38.5787; 직전 완료 봉 목표를 다음 봉 시가에 모의 적용 |
| v2 | bollinger_20_reentry | 9771.22 | -228.78 | sell / filled / 직전 종가 < 직전 하단밴드, 현재 하단밴드 <= 종가 <= SMA20 (한 봉 목표); 조건 미충족; close=721.16, lower20=716.851, SMA20=725.821, previous_lower20=717.276; 직전 완료 봉 목표를 다음 봉 시가에 모의 적용 |
| v2 | donchian_20 | 9948.84 | -51.16 | sell / filled / 종가 > 현재 봉을 제외한 직전 20봉 최고가; 조건 미충족; close=739.81, prior_high20=742.28; 직전 완료 봉 목표를 다음 봉 시가에 모의 적용 |
| v2 | atr_14_breakout | 9767.92 | -232.08 | sell / filled / 종가 > 직전 종가 + 직전 ATR14 그리고 종가 > EMA26; 조건 미충족; close=732.42, threshold=735.931, prior_ATR14=4.99094, EMA26=726.612; 직전 완료 봉 목표를 다음 봉 시가에 모의 적용 |
| v2 | session_vwap | 9374.59 | -625.41 | sell / filled / 종가 > 뉴욕 거래일별 누적 전형가격 VWAP; 조건 미충족; close=722.65, session_VWAP=723.935, session_volume=1.94253e+06; 직전 완료 봉 목표를 다음 봉 시가에 모의 적용 |
| v2 | obv_20 | 9675.93 | -324.07 | sell / filled / OBV > OBV의 SMA20 그리고 종가 > EMA26; 조건 미충족; OBV=-5.85317e+06, OBV_SMA20=-5.80449e+06, close=725.22, EMA26=726.751; 직전 완료 봉 목표를 다음 봉 시가에 모의 적용 |
| v2 | stochastic_14_3_recovery | 9843.26 | -156.74 | sell / filled / 직전 %K14 < 20에서 %K14가 %D3 상향 돌파 (한 봉 목표); 조건 미충족; K14=59.6496, D3=39.2535, previous_K14=43.8356, previous_D3=33.8642; 직전 완료 봉 목표를 다음 봉 시가에 모의 적용 |
| v2 | mfi_14_recovery | 10064.61 | 64.61 | sell / filled / 직전 MFI14 < 20, 현재 MFI14 >= 20 (한 봉 목표); 조건 미충족; MFI14=32.7313, previous_MFI14=24.1736; 직전 완료 봉 목표를 다음 봉 시가에 모의 적용 |
| v2 | adx_14_trend | 10000.00 | 0.00 | 대기 /  / 새 신호 대기 |
| v2 | aroon_25_trend | 10029.14 | 29.14 | sell / filled / Aroon25 Up > 70 그리고 Down < 30 (동률이면 최신 극값); 조건 미충족; Aroon_up=88, Aroon_down=48; 직전 완료 봉 목표를 다음 봉 시가에 모의 적용 |
| v2 | cci_20_momentum | 9886.36 | -113.64 | sell / filled / CCI20 > 100 (전형가격·평균절대편차); 조건 미충족; CCI20=20.3547; 직전 완료 봉 목표를 다음 봉 시가에 모의 적용 |
| v2 | williams_14_recovery | 9999.06 | -0.94 | sell / filled / 직전 Williams %R14 < -80, 현재 >= -80 (한 봉 목표); 조건 미충족; Williams_R14=-40.3504, previous_R14=-56.1644; 직전 완료 봉 목표를 다음 봉 시가에 모의 적용 |
| v2 | cmf_20_accumulation | 9776.84 | -223.16 | buy / partial / Chaikin Money Flow20 > 0.1; 조건 충족; CMF20=0.130083, volume20=2.38752e+06; 직전 완료 봉 목표를 다음 봉 시가에 모의 적용 |
| v2 | chaikin_3_10 | 9546.39 | -453.61 | 중단: 손실 한도 / buy / partial / ADL의 EMA3 - EMA10 > 0 그리고 종가 > EMA26; 조건 충족; Chaikin3_10=293683, ADL=-4.91156e+06, close=739.58, EMA26=736.187; 직전 완료 봉 목표를 다음 봉 시가에 모의 적용 |
| v2 | roc_10_momentum | 9961.14 | -38.86 | sell / filled / 10봉 ROC > 1% 그리고 종가 > EMA26; 조건 미충족; ROC10_percent=-0.134597, close=734.53, EMA26=735.486; 직전 완료 봉 목표를 다음 봉 시가에 모의 적용 |
| v2 | trix_15_trend | 9556.01 | -443.99 | 중단: 손실 한도 / buy / partial / 15봉 삼중 EMA의 1봉 변화율 TRIX > 0 그리고 종가 > EMA26; 조건 충족; TRIX15_percent=0.0196284, close=739.58, EMA26=736.187; 직전 완료 봉 목표를 다음 봉 시가에 모의 적용 |
| v2 | keltner_20_breakout | 10000.00 | 0.00 | 대기 /  / 새 신호 대기 |
| v2 | opening_range_30m | 10068.05 | 68.05 | buy / partial / 뉴욕 09:30·09:45 두 완료 봉 최고가를 10:00 이후 종가가 돌파; 조건 충족; close=721.16, opening_high=718.07; 직전 완료 봉 목표를 다음 봉 시가에 모의 적용 |

### 같은 기간의 비용·노출 비교 (사후 연구)

| 전략 | 비용 전 | 비용 후 | 100% 보유 | 같은 평균 노출 보유 | 평균 노출 |
|---|---:|---:|---:|---:|---:|
| cash | 0.00% | 0.00% | -12.48% | -0.00% | 0.00% |
| buy_hold | -12.11% | -12.48% | -12.48% | -12.48% | 100.00% |
| trend_8_26 | -1.14% | -4.81% | -12.48% | -5.51% | 43.04% |
| momentum_26 | -2.98% | -6.58% | -12.48% | -5.27% | 41.21% |
| breakout_8 | -3.61% | -15.38% | -12.48% | -1.73% | 13.39% |
| reversion_12 | -2.77% | -16.07% | -12.48% | -3.65% | 28.35% |
| volume_26 | -2.12% | -9.25% | -12.48% | -1.06% | 8.14% |
| trend_8_26 AND momentum_26 | 0.76% | -1.74% | -12.48% | -4.61% | 35.96% |
| trend_8_26 + momentum_26 | -2.05% | -5.69% | -12.48% | -5.39% | 42.13% |
| trend_8_26 AND breakout_8 | -2.00% | -7.99% | -12.48% | -0.82% | 6.30% |
| trend_8_26 + breakout_8 | -2.35% | -10.04% | -12.48% | -3.63% | 28.22% |
| trend_8_26 AND reversion_12 | 0.04% | -6.07% | -12.48% | -0.78% | 6.04% |
| trend_8_26 + reversion_12 | -1.89% | -9.83% | -12.48% | -4.58% | 35.70% |
| trend_8_26 AND volume_26 | 1.79% | 0.09% | -12.48% | -0.20% | 1.57% |
| trend_8_26 + volume_26 | -1.58% | -6.64% | -12.48% | -3.30% | 25.59% |
| momentum_26 AND breakout_8 | -2.64% | -8.96% | -12.48% | -0.85% | 6.56% |
| momentum_26 + breakout_8 | -3.26% | -11.06% | -12.48% | -3.51% | 27.30% |
| momentum_26 AND reversion_12 | -3.16% | -8.69% | -12.48% | -0.75% | 5.77% |
| momentum_26 + reversion_12 | -2.82% | -10.68% | -12.48% | -4.46% | 34.78% |
| momentum_26 AND volume_26 | 1.75% | 0.06% | -12.48% | -0.17% | 1.31% |
| momentum_26 + volume_26 | -2.49% | -7.50% | -12.48% | -3.18% | 24.68% |
| breakout_8 AND reversion_12 | 0.00% | 0.00% | -12.48% | -0.00% | 0.00% |
| breakout_8 + reversion_12 | -3.13% | -14.81% | -12.48% | -2.69% | 20.87% |
| breakout_8 AND volume_26 | 0.66% | -0.18% | -12.48% | -0.07% | 0.52% |
| breakout_8 + volume_26 | -2.83% | -11.80% | -12.48% | -1.40% | 10.77% |
| reversion_12 AND volume_26 | -0.54% | -5.03% | -12.48% | -0.68% | 5.25% |
| reversion_12 + volume_26 | -2.40% | -12.15% | -12.48% | -2.36% | 18.25% |
| ema_12_26 | -1.49% | -3.13% | -12.48% | -5.01% | 39.11% |
| macd_12_26_9 | 1.76% | -0.78% | -12.48% | -3.05% | 23.62% |
| rsi_14_recovery | -0.17% | -6.26% | -12.48% | -0.51% | 3.94% |
| bollinger_20_reentry | 0.57% | -5.57% | -12.48% | -0.51% | 3.94% |
| donchian_20 | -1.16% | -4.82% | -12.48% | -0.58% | 4.46% |
| atr_14_breakout | -1.46% | -7.48% | -12.48% | -0.55% | 4.20% |
| session_vwap | -1.05% | -13.50% | -12.48% | -5.90% | 46.19% |
| obv_20 | -4.74% | -13.87% | -12.48% | -2.51% | 19.42% |
| stochastic_14_3_recovery | -2.10% | -12.96% | -12.48% | -0.95% | 7.35% |
| mfi_14_recovery | 1.96% | -1.00% | -12.48% | -0.24% | 1.84% |
| adx_14_trend | -2.02% | -4.05% | -12.48% | -1.09% | 8.40% |
| aroon_25_trend | -0.29% | -3.58% | -12.48% | -1.39% | 10.76% |
| cci_20_momentum | -4.55% | -9.24% | -12.48% | -1.70% | 13.12% |
| williams_14_recovery | 0.05% | -8.78% | -12.48% | -0.75% | 5.77% |
| cmf_20_accumulation | -4.10% | -10.71% | -12.48% | -2.07% | 16.01% |
| chaikin_3_10 | -6.27% | -14.90% | -12.48% | -3.61% | 28.08% |
| roc_10_momentum | -1.68% | -6.91% | -12.48% | -1.60% | 12.34% |
| trix_15_trend | -1.37% | -5.42% | -12.48% | -3.88% | 30.18% |
| keltner_20_breakout | -2.87% | -5.29% | -12.48% | -0.34% | 2.62% |
| opening_range_30m | 6.67% | 1.86% | -12.48% | -3.01% | 23.36% |

동일 구간·초기 자금, 종료 시 청산 비용 포함. 노출 맞춤은 사후 설명용이며 v2 실제 계좌 성과가 아닙니다.
[낙폭 분해·비용 영향·전체 구간](CAT/comparison.json)

[v1 전체 기록](CAT/accounts.json) · [v2 전체 기록](CAT/accounts-v2.json)

## WMT 계좌

| 모델 | 전략 | 평가액 USD | 손익 USD | 최근 매매·이유 |
|---|---|---:|---:|---|
| v1 | cash | 10000.00 | 0.00 | 대기 /  / 새 신호 대기 |
| v1 | buy_hold | 9996.08 | -3.92 | buy /  / buy_hold: prior completed bar target 100%; next bar open simulation |
| v1 | trend_8_26 | 9791.85 | -208.15 | sell /  / trend_8_26: prior completed bar target 0%; next bar open simulation |
| v1 | momentum_26 | 9801.37 | -198.63 | sell /  / momentum_26: prior completed bar target 0%; next bar open simulation |
| v1 | breakout_8 | 9728.67 | -271.33 | sell /  / breakout_8: prior completed bar target 0%; next bar open simulation |
| v1 | reversion_12 | 9731.44 | -268.56 | buy /  / reversion_12: prior completed bar target 100%; next bar open simulation |
| v1 | volume_26 | 9755.08 | -244.92 | sell /  / volume_26: prior completed bar target 0%; next bar open simulation |
| v1 | trend_8_26 AND momentum_26 | 9811.64 | -188.36 | sell /  / trend_8_26 AND momentum_26: prior completed bar target 0%; next bar open simulation |
| v1 | trend_8_26 + momentum_26 | 9796.64 | -203.36 | sell /  / trend_8_26 + momentum_26: prior completed bar target 0%; next bar open simulation |
| v1 | trend_8_26 AND breakout_8 | 9854.29 | -145.71 | sell /  / trend_8_26 AND breakout_8: prior completed bar target 0%; next bar open simulation |
| v1 | trend_8_26 + breakout_8 | 9760.28 | -239.72 | sell /  / trend_8_26 + breakout_8: prior completed bar target 0%; next bar open simulation |
| v1 | trend_8_26 AND reversion_12 | 9798.51 | -201.49 | sell /  / trend_8_26 AND reversion_12: prior completed bar target 0%; next bar open simulation |
| v1 | trend_8_26 + reversion_12 | 9800.91 | -199.09 | buy /  / trend_8_26 + reversion_12: prior completed bar target 50%; next bar open simulation |
| v1 | trend_8_26 AND volume_26 | 9837.96 | -162.04 | sell /  / trend_8_26 AND volume_26: prior completed bar target 0%; next bar open simulation |
| v1 | trend_8_26 + volume_26 | 9773.64 | -226.36 | sell /  / trend_8_26 + volume_26: prior completed bar target 0%; next bar open simulation |
| v1 | momentum_26 AND breakout_8 | 9816.19 | -183.81 | sell /  / momentum_26 AND breakout_8: prior completed bar target 0%; next bar open simulation |
| v1 | momentum_26 + breakout_8 | 9823.93 | -176.07 | sell /  / momentum_26 + breakout_8: prior completed bar target 0%; next bar open simulation |
| v1 | momentum_26 AND reversion_12 | 9935.88 | -64.12 | sell /  / momentum_26 AND reversion_12: prior completed bar target 0%; next bar open simulation |
| v1 | momentum_26 + reversion_12 | 9864.50 | -135.50 | buy /  / momentum_26 + reversion_12: prior completed bar target 50%; next bar open simulation |
| v1 | momentum_26 AND volume_26 | 9905.94 | -94.06 | sell /  / momentum_26 AND volume_26: prior completed bar target 0%; next bar open simulation |
| v1 | momentum_26 + volume_26 | 9817.50 | -182.50 | sell /  / momentum_26 + volume_26: prior completed bar target 0%; next bar open simulation |
| v1 | breakout_8 AND reversion_12 | 10000.00 | 0.00 | 대기 /  / 새 신호 대기 |
| v1 | breakout_8 + reversion_12 | 9768.95 | -231.05 | buy /  / breakout_8 + reversion_12: prior completed bar target 50%; next bar open simulation |
| v1 | breakout_8 AND volume_26 | 9850.09 | -149.91 | sell /  / breakout_8 AND volume_26: prior completed bar target 0%; next bar open simulation |
| v1 | breakout_8 + volume_26 | 9741.88 | -258.12 | sell /  / breakout_8 + volume_26: prior completed bar target 0%; next bar open simulation |
| v1 | reversion_12 AND volume_26 | 9905.10 | -94.90 | sell /  / reversion_12 AND volume_26: prior completed bar target 0%; next bar open simulation |
| v1 | reversion_12 + volume_26 | 9782.25 | -217.75 | buy /  / reversion_12 + volume_26: prior completed bar target 50%; next bar open simulation |
| v1 | ema_12_26 | 9906.58 | -93.42 | sell /  / EMA12 > EMA26; 조건 미충족; EMA12=118.808, EMA26=118.852 |
| v1 | macd_12_26_9 | 9985.46 | -14.54 | sell /  / MACD > 신호선 그리고 MACD > 0; 조건 미충족; MACD=0.122825, signal9=0.127837 |
| v1 | rsi_14_recovery | 10000.00 | 0.00 | 대기 /  / 새 신호 대기 |
| v1 | bollinger_20_reentry | 9901.04 | -98.96 | sell /  / 직전 종가 < 직전 하단밴드, 현재 하단밴드 <= 종가 <= SMA20 (한 봉 목표); 조건 미충족; close=118.132, lower20=117.91, SMA20=118.808, previous_lower20=118.006 |
| v1 | donchian_20 | 9935.97 | -64.03 | sell /  / 종가 > 현재 봉을 제외한 직전 20봉 최고가; 조건 미충족; close=119.52, prior_high20=120.5 |
| v1 | atr_14_breakout | 9915.82 | -84.18 | sell /  / 종가 > 직전 종가 + 직전 ATR14 그리고 종가 > EMA26; 조건 미충족; close=119.52, threshold=120.186, prior_ATR14=0.395874, EMA26=118.952 |
| v1 | session_vwap | 9838.24 | -161.76 | sell /  / 종가 > 뉴욕 거래일별 누적 전형가격 VWAP; 조건 미충족; close=118.71, session_VWAP=118.72, session_volume=1.73369e+07 |
| v1 | obv_20 | 9857.61 | -142.39 | sell /  / OBV > OBV의 SMA20 그리고 종가 > EMA26; 조건 미충족; OBV=1.6238e+07, OBV_SMA20=1.74966e+07, close=118.945, EMA26=118.951 |
| v1 | stochastic_14_3_recovery | 9803.13 | -196.87 | sell /  / 직전 %K14 < 20에서 %K14가 %D3 상향 돌파 (한 봉 목표); 조건 미충족; K14=6.57374, D3=4.6742, previous_K14=2.82256, previous_D3=2.48296 |
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
| v2 | buy_hold | 10590.75 | 590.75 | buy / partial / 직전 완료 봉 목표 비중 100%; 다음 봉 시가 가정 |
| v2 | trend_8_26 | 10187.81 | 187.81 | sell / filled / 직전 완료 봉 목표 비중 0%; 다음 봉 시가 가정 |
| v2 | momentum_26 | 10200.51 | 200.51 | sell / filled / 직전 완료 봉 목표 비중 0%; 다음 봉 시가 가정 |
| v2 | breakout_8 | 9682.65 | -317.35 | sell / filled / 직전 완료 봉 목표 비중 0%; 다음 봉 시가 가정 |
| v2 | reversion_12 | 9628.86 | -371.14 | buy / partial / 직전 완료 봉 목표 비중 100%; 다음 봉 시가 가정 |
| v2 | volume_26 | 9711.50 | -288.50 | sell / filled / 직전 완료 봉 목표 비중 0%; 다음 봉 시가 가정 |
| v2 | trend_8_26 AND momentum_26 | 10206.36 | 206.36 | sell / filled / 직전 완료 봉 목표 비중 0%; 다음 봉 시가 가정 |
| v2 | trend_8_26 + momentum_26 | 10194.13 | 194.13 | sell / filled / 직전 완료 봉 목표 비중 0%; 다음 봉 시가 가정 |
| v2 | trend_8_26 AND breakout_8 | 9935.59 | -64.41 | sell / filled / 직전 완료 봉 목표 비중 0%; 다음 봉 시가 가정 |
| v2 | trend_8_26 + breakout_8 | 9932.48 | -67.52 | sell / filled / 직전 완료 봉 목표 비중 0%; 다음 봉 시가 가정 |
| v2 | trend_8_26 AND reversion_12 | 9603.42 | -396.58 | sell / filled / 직전 완료 봉 목표 비중 0%; 다음 봉 시가 가정 |
| v2 | trend_8_26 + reversion_12 | 9947.67 | -52.33 | buy / filled / 직전 완료 봉 목표 비중 50%; 다음 봉 시가 가정 |
| v2 | trend_8_26 AND volume_26 | 9784.10 | -215.90 | sell / filled / 직전 완료 봉 목표 비중 0%; 다음 봉 시가 가정 |
| v2 | trend_8_26 + volume_26 | 9948.42 | -51.58 | sell / filled / 직전 완료 봉 목표 비중 0%; 다음 봉 시가 가정 |
| v2 | momentum_26 AND breakout_8 | 9773.67 | -226.33 | sell / filled / 직전 완료 봉 목표 비중 0%; 다음 봉 시가 가정 |
| v2 | momentum_26 + breakout_8 | 10001.62 | 1.62 | sell / filled / 직전 완료 봉 목표 비중 0%; 다음 봉 시가 가정 |
| v2 | momentum_26 AND reversion_12 | 9759.91 | -240.09 | sell / filled / 직전 완료 봉 목표 비중 0%; 다음 봉 시가 가정 |
| v2 | momentum_26 + reversion_12 | 10058.81 | 58.81 | buy / filled / 직전 완료 봉 목표 비중 50%; 다음 봉 시가 가정 |
| v2 | momentum_26 AND volume_26 | 9814.68 | -185.32 | sell / filled / 직전 완료 봉 목표 비중 0%; 다음 봉 시가 가정 |
| v2 | momentum_26 + volume_26 | 9996.47 | -3.53 | sell / filled / 직전 완료 봉 목표 비중 0%; 다음 봉 시가 가정 |
| v2 | breakout_8 AND reversion_12 | 10000.00 | 0.00 | 대기 /  / 새 신호 대기 |
| v2 | breakout_8 + reversion_12 | 9717.75 | -282.25 | buy / filled / 직전 완료 봉 목표 비중 50%; 다음 봉 시가 가정 |
| v2 | breakout_8 AND volume_26 | 9795.19 | -204.81 | sell / filled / 직전 완료 봉 목표 비중 0%; 다음 봉 시가 가정 |
| v2 | breakout_8 + volume_26 | 9698.42 | -301.58 | sell / filled / 직전 완료 봉 목표 비중 0%; 다음 봉 시가 가정 |
| v2 | reversion_12 AND volume_26 | 9912.80 | -87.20 | sell / filled / 직전 완료 봉 목표 비중 0%; 다음 봉 시가 가정 |
| v2 | reversion_12 + volume_26 | 9710.62 | -289.38 | buy / filled / 직전 완료 봉 목표 비중 50%; 다음 봉 시가 가정 |
| v2 | ema_12_26 | 9902.61 | -97.39 | sell / filled / EMA12 > EMA26; 조건 미충족; EMA12=118.808, EMA26=118.852; 직전 완료 봉 목표를 다음 봉 시가에 모의 적용 |
| v2 | macd_12_26_9 | 9981.46 | -18.54 | sell / filled / MACD > 신호선 그리고 MACD > 0; 조건 미충족; MACD=0.122825, signal9=0.127837; 직전 완료 봉 목표를 다음 봉 시가에 모의 적용 |
| v2 | rsi_14_recovery | 10000.00 | 0.00 | 대기 /  / 새 신호 대기 |
| v2 | bollinger_20_reentry | 9897.08 | -102.92 | sell / filled / 직전 종가 < 직전 하단밴드, 현재 하단밴드 <= 종가 <= SMA20 (한 봉 목표); 조건 미충족; close=118.132, lower20=117.91, SMA20=118.808, previous_lower20=118.006; 직전 완료 봉 목표를 다음 봉 시가에 모의 적용 |
| v2 | donchian_20 | 9933.99 | -66.01 | sell / filled / 종가 > 현재 봉을 제외한 직전 20봉 최고가; 조건 미충족; close=119.52, prior_high20=120.5; 직전 완료 봉 목표를 다음 봉 시가에 모의 적용 |
| v2 | atr_14_breakout | 9911.85 | -88.15 | sell / filled / 종가 > 직전 종가 + 직전 ATR14 그리고 종가 > EMA26; 조건 미충족; close=119.52, threshold=120.186, prior_ATR14=0.395874, EMA26=118.952; 직전 완료 봉 목표를 다음 봉 시가에 모의 적용 |
| v2 | session_vwap | 9826.44 | -173.56 | sell / filled / 종가 > 뉴욕 거래일별 누적 전형가격 VWAP; 조건 미충족; close=118.71, session_VWAP=118.72, session_volume=1.73369e+07; 직전 완료 봉 목표를 다음 봉 시가에 모의 적용 |
| v2 | obv_20 | 9847.76 | -152.24 | sell / filled / OBV > OBV의 SMA20 그리고 종가 > EMA26; 조건 미충족; OBV=1.6238e+07, OBV_SMA20=1.74966e+07, close=118.945, EMA26=118.951; 직전 완료 봉 목표를 다음 봉 시가에 모의 적용 |
| v2 | stochastic_14_3_recovery | 9795.29 | -204.71 | sell / filled / 직전 %K14 < 20에서 %K14가 %D3 상향 돌파 (한 봉 목표); 조건 미충족; K14=6.57374, D3=4.6742, previous_K14=2.82256, previous_D3=2.48296; 직전 완료 봉 목표를 다음 봉 시가에 모의 적용 |
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
| cash | 0.00% | 0.00% | 10.28% | 0.00% | 0.00% |
| buy_hold | 10.75% | 10.28% | 10.28% | 10.28% | 100.00% |
| trend_8_26 | 7.48% | 3.93% | 10.28% | 7.10% | 69.82% |
| momentum_26 | 9.58% | 3.32% | 10.28% | 7.21% | 70.87% |
| breakout_8 | 6.12% | -9.92% | 10.28% | 2.52% | 25.20% |
| reversion_12 | 3.66% | -8.22% | 10.28% | 1.86% | 18.64% |
| volume_26 | 0.01% | -6.09% | 10.28% | 0.57% | 5.77% |
| trend_8_26 AND momentum_26 | 7.80% | 2.50% | 10.28% | 6.45% | 63.52% |
| trend_8_26 + momentum_26 | 8.53% | 3.62% | 10.28% | 7.16% | 70.34% |
| trend_8_26 AND breakout_8 | 6.59% | -6.43% | 10.28% | 2.10% | 21.00% |
| trend_8_26 + breakout_8 | 6.81% | -3.23% | 10.28% | 4.79% | 47.51% |
| trend_8_26 AND reversion_12 | -0.24% | -6.33% | 10.28% | 0.73% | 7.35% |
| trend_8_26 + reversion_12 | 5.59% | -1.71% | 10.28% | 4.46% | 44.23% |
| trend_8_26 AND volume_26 | -0.30% | -3.19% | 10.28% | 0.26% | 2.62% |
| trend_8_26 + volume_26 | 3.72% | -0.78% | 10.28% | 3.80% | 37.80% |
| momentum_26 AND breakout_8 | 6.62% | -7.18% | 10.28% | 2.28% | 22.83% |
| momentum_26 + breakout_8 | 7.85% | -2.70% | 10.28% | 4.85% | 48.04% |
| momentum_26 AND reversion_12 | 1.24% | -4.94% | 10.28% | 0.78% | 7.87% |
| momentum_26 + reversion_12 | 6.62% | 0.08% | 10.28% | 4.51% | 44.75% |
| momentum_26 AND volume_26 | 1.58% | -3.01% | 10.28% | 0.31% | 3.15% |
| momentum_26 + volume_26 | 4.72% | -1.07% | 10.28% | 3.85% | 38.32% |
| breakout_8 AND reversion_12 | 0.00% | 0.00% | 10.28% | 0.00% | 0.00% |
| breakout_8 + reversion_12 | 4.91% | -8.30% | 10.28% | 2.19% | 21.92% |
| breakout_8 AND volume_26 | 0.78% | -2.14% | 10.28% | 0.21% | 2.10% |
| breakout_8 + volume_26 | 3.04% | -7.82% | 10.28% | 1.54% | 15.49% |
| reversion_12 AND volume_26 | -1.05% | -3.51% | 10.28% | 0.18% | 1.84% |
| reversion_12 + volume_26 | 1.83% | -6.58% | 10.28% | 1.22% | 12.21% |
| ema_12_26 | 11.20% | 9.81% | 10.28% | 7.40% | 72.70% |
| macd_12_26_9 | 8.67% | 4.64% | 10.28% | 3.64% | 36.22% |
| rsi_14_recovery | -0.25% | -1.50% | 10.28% | 0.08% | 0.79% |
| bollinger_20_reentry | 1.21% | -2.13% | 10.28% | 0.21% | 2.10% |
| donchian_20 | 4.55% | -7.44% | 10.28% | 1.28% | 12.86% |
| atr_14_breakout | -0.90% | -10.40% | 10.28% | 0.73% | 7.35% |
| session_vwap | 9.56% | -0.53% | 10.28% | 5.74% | 56.69% |
| obv_20 | 10.74% | 2.68% | 10.28% | 5.68% | 56.17% |
| stochastic_14_3_recovery | 1.16% | -8.16% | 10.28% | 0.60% | 6.04% |
| mfi_14_recovery | 0.02% | -0.81% | 10.28% | 0.05% | 0.52% |
| adx_14_trend | 8.85% | 6.14% | 10.28% | 5.06% | 50.13% |
| aroon_25_trend | 5.98% | 0.77% | 10.28% | 3.29% | 32.81% |
| cci_20_momentum | 5.92% | -2.62% | 10.28% | 3.21% | 32.02% |
| williams_14_recovery | 0.10% | -7.58% | 10.28% | 0.49% | 4.99% |
| cmf_20_accumulation | 9.17% | -0.05% | 10.28% | 3.64% | 36.22% |
| chaikin_3_10 | 9.44% | 0.62% | 10.28% | 5.25% | 51.97% |
| roc_10_momentum | -0.29% | -4.79% | 10.28% | 1.39% | 13.91% |
| trix_15_trend | 10.97% | 6.86% | 10.28% | 6.58% | 64.83% |
| keltner_20_breakout | 6.59% | 0.08% | 10.28% | 2.65% | 26.51% |
| opening_range_30m | 9.76% | 4.80% | 10.28% | 3.61% | 35.96% |

동일 구간·초기 자금, 종료 시 청산 비용 포함. 노출 맞춤은 사후 설명용이며 v2 실제 계좌 성과가 아닙니다.
[낙폭 분해·비용 영향·전체 구간](WMT/comparison.json)

[v1 전체 기록](WMT/accounts.json) · [v2 전체 기록](WMT/accounts-v2.json)
