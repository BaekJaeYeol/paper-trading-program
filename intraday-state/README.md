# 모의투자 운영 현황

[PC·서버 장애 진단과 복구 방법](https://github.com/BaekJaeYeol/paper-trading-program/blob/main/investment-lab/docs/failure-recovery.md)

이번 실행 복구: {}

완료 봉 확인 주기: 기록 1/8회 · 기록 없는 예정 7회 · 아직 판정 전 18회 · 주의: 예약 시작 지연 또는 실행·저장 누락을 확인하세요.

[주기 판정 기준](https://github.com/BaekJaeYeol/paper-trading-program/blob/main/investment-lab/docs/session-coverage.md)

최근 확인: 2026-10-20T15:52:00.468646+00:00 (UTC)
다음 15분 확인 목표 (세션 실행 중에만 적용): 2026-10-20T16:07:00+00:00 (UTC, 실행 지연 가능)

실제 주문 없음. v1 기존 계좌와 v2 새 계좌의 시작일이 다르므로 수익률을 직접 우열 비교하지 마세요.
v2는 다음 봉 시가에 비용·스프레드·직전 거래량 제한을 적용한 가상 체결입니다. 미체결 잔량은 만료됩니다.

| 종목 | 상태 | 최근 성공 UTC | 마지막 완료 봉 UTC | 이번 새 봉 |
|---|---|---|---|---|
| SPY | updated | 2026-10-20T15:52:00.468646+00:00 | 2026-10-20T15:30:00+00:00 | 1 |
| QQQ | updated | 2026-10-20T15:52:00.468646+00:00 | 2026-10-20T15:30:00+00:00 | 1 |
| IWM | updated | 2026-10-20T15:52:00.468646+00:00 | 2026-10-20T15:30:00+00:00 | 1 |
| DIA | updated | 2026-10-20T15:52:00.468646+00:00 | 2026-10-20T15:30:00+00:00 | 1 |
| MSFT | updated | 2026-10-20T15:52:00.468646+00:00 | 2026-10-20T15:30:00+00:00 | 1 |
| JPM | updated | 2026-10-20T15:52:00.468646+00:00 | 2026-10-20T15:30:00+00:00 | 1 |
| XOM | updated | 2026-10-20T15:52:00.468646+00:00 | 2026-10-20T15:30:00+00:00 | 1 |
| JNJ | updated | 2026-10-20T15:52:00.468646+00:00 | 2026-10-20T15:30:00+00:00 | 1 |
| CAT | updated | 2026-10-20T15:52:00.468646+00:00 | 2026-10-20T15:30:00+00:00 | 1 |
| WMT | updated | 2026-10-20T15:52:00.468646+00:00 | 2026-10-20T15:30:00+00:00 | 1 |

이번 실행 소요: 47.17초
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
| v1 | buy_hold | 9932.60 | -67.40 | buy /  / buy_hold: prior completed bar target 100%; next bar open simulation |
| v1 | trend_8_26 | 9827.73 | -172.27 | buy /  / trend_8_26: prior completed bar target 100%; next bar open simulation |
| v1 | momentum_26 | 9784.81 | -215.19 | sell /  / momentum_26: prior completed bar target 0%; next bar open simulation |
| v1 | breakout_8 | 9752.40 | -247.60 | sell /  / breakout_8: prior completed bar target 0%; next bar open simulation |
| v1 | reversion_12 | 9831.96 | -168.04 | sell /  / reversion_12: prior completed bar target 0%; next bar open simulation |
| v1 | volume_26 | 9718.44 | -281.56 | sell /  / volume_26: prior completed bar target 0%; next bar open simulation |
| v1 | trend_8_26 AND momentum_26 | 9785.59 | -214.41 | sell /  / trend_8_26 AND momentum_26: prior completed bar target 0%; next bar open simulation |
| v1 | trend_8_26 + momentum_26 | 9806.24 | -193.76 | sell /  / trend_8_26 + momentum_26: prior completed bar target 50%; next bar open simulation |
| v1 | trend_8_26 AND breakout_8 | 9859.41 | -140.59 | sell /  / trend_8_26 AND breakout_8: prior completed bar target 0%; next bar open simulation |
| v1 | trend_8_26 + breakout_8 | 9829.12 | -170.88 | sell /  / trend_8_26 + breakout_8: prior completed bar target 50%; next bar open simulation |
| v1 | trend_8_26 AND reversion_12 | 9908.20 | -91.80 | sell /  / trend_8_26 AND reversion_12: prior completed bar target 0%; next bar open simulation |
| v1 | trend_8_26 + reversion_12 | 9829.71 | -170.29 | sell /  / trend_8_26 + reversion_12: prior completed bar target 50%; next bar open simulation |
| v1 | trend_8_26 AND volume_26 | 9764.18 | -235.82 | sell /  / trend_8_26 AND volume_26: prior completed bar target 0%; next bar open simulation |
| v1 | trend_8_26 + volume_26 | 9772.87 | -227.13 | sell /  / trend_8_26 + volume_26: prior completed bar target 50%; next bar open simulation |
| v1 | momentum_26 AND breakout_8 | 9831.79 | -168.21 | sell /  / momentum_26 AND breakout_8: prior completed bar target 0%; next bar open simulation |
| v1 | momentum_26 + breakout_8 | 9768.61 | -231.39 | sell /  / momentum_26 + breakout_8: prior completed bar target 0%; next bar open simulation |
| v1 | momentum_26 AND reversion_12 | 9904.38 | -95.62 | sell /  / momentum_26 AND reversion_12: prior completed bar target 0%; next bar open simulation |
| v1 | momentum_26 + reversion_12 | 9847.58 | -152.42 | sell /  / momentum_26 + reversion_12: prior completed bar target 0%; next bar open simulation |
| v1 | momentum_26 AND volume_26 | 9777.78 | -222.22 | sell /  / momentum_26 AND volume_26: prior completed bar target 0%; next bar open simulation |
| v1 | momentum_26 + volume_26 | 9751.51 | -248.49 | sell /  / momentum_26 + volume_26: prior completed bar target 0%; next bar open simulation |
| v1 | breakout_8 AND reversion_12 | 10000.00 | 0.00 | 대기 /  / 새 신호 대기 |
| v1 | breakout_8 + reversion_12 | 9791.96 | -208.04 | sell /  / breakout_8 + reversion_12: prior completed bar target 0%; next bar open simulation |
| v1 | breakout_8 AND volume_26 | 9878.80 | -121.20 | sell /  / breakout_8 AND volume_26: prior completed bar target 0%; next bar open simulation |
| v1 | breakout_8 + volume_26 | 9754.80 | -245.20 | sell /  / breakout_8 + volume_26: prior completed bar target 0%; next bar open simulation |
| v1 | reversion_12 AND volume_26 | 9899.64 | -100.36 | sell /  / reversion_12 AND volume_26: prior completed bar target 0%; next bar open simulation |
| v1 | reversion_12 + volume_26 | 9774.97 | -225.03 | sell /  / reversion_12 + volume_26: prior completed bar target 0%; next bar open simulation |
| v1 | ema_12_26 | 9793.27 | -206.73 | buy /  / EMA12 > EMA26; 조건 충족; EMA12=767.528, EMA26=767.458 |
| v1 | macd_12_26_9 | 9813.52 | -186.48 | buy /  / MACD > 신호선 그리고 MACD > 0; 조건 충족; MACD=0.396374, signal9=0.142666 |
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
| v1 | chaikin_3_10 | 9864.45 | -135.55 | sell /  / ADL의 EMA3 - EMA10 > 0 그리고 종가 > EMA26; 조건 미충족; Chaikin3_10=-974621, ADL=1.2921e+06, close=768.275, EMA26=767.362 |
| v1 | roc_10_momentum | 9953.42 | -46.58 | sell /  / 10봉 ROC > 1% 그리고 종가 > EMA26; 조건 미충족; ROC10_percent=0.806376, close=769.45, EMA26=767.181 |
| v1 | trix_15_trend | 9761.01 | -238.99 | buy /  / 15봉 삼중 EMA의 1봉 변화율 TRIX > 0 그리고 종가 > EMA26; 조건 충족; TRIX15_percent=0.0030347, close=767.955, EMA26=767.326 |
| v1 | keltner_20_breakout | 9924.71 | -75.29 | sell /  / 종가 > EMA20 + 2 x Wilder ATR14; 조건 미충족; close=768.93, upper_Keltner=771.837, EMA20=768.595, ATR14=1.6209 |
| v1 | opening_range_30m | 9762.21 | -237.79 | buy /  / 뉴욕 09:30·09:45 두 완료 봉 최고가를 10:00 이후 종가가 돌파; 조건 충족; close=769.1, opening_high=768 |
| v2 | cash | 10000.00 | 0.00 | 대기 /  / 새 신호 대기 |
| v2 | buy_hold | 9860.95 | -139.05 | buy / partial / 직전 완료 봉 목표 비중 100%; 다음 봉 시가 가정 |
| v2 | trend_8_26 | 9709.36 | -290.64 | buy / partial / 직전 완료 봉 목표 비중 100%; 다음 봉 시가 가정 |
| v2 | momentum_26 | 9636.97 | -363.03 | sell / filled / 직전 완료 봉 목표 비중 0%; 다음 봉 시가 가정 |
| v2 | breakout_8 | 9349.72 | -650.28 | sell / filled / 직전 완료 봉 목표 비중 0%; 다음 봉 시가 가정 |
| v2 | reversion_12 | 9366.23 | -633.77 | sell / filled / 직전 완료 봉 목표 비중 0%; 다음 봉 시가 가정 |
| v2 | volume_26 | 9166.45 | -833.55 | sell / filled / 직전 완료 봉 목표 비중 0%; 다음 봉 시가 가정 |
| v2 | trend_8_26 AND momentum_26 | 9644.30 | -355.70 | sell / filled / 직전 완료 봉 목표 비중 0%; 다음 봉 시가 가정 |
| v2 | trend_8_26 + momentum_26 | 9673.10 | -326.90 | sell / filled / 직전 완료 봉 목표 비중 50%; 다음 봉 시가 가정 |
| v2 | trend_8_26 AND breakout_8 | 9681.27 | -318.73 | sell / filled / 직전 완료 봉 목표 비중 0%; 다음 봉 시가 가정 |
| v2 | trend_8_26 + breakout_8 | 9567.72 | -432.28 | sell / filled / 직전 완료 봉 목표 비중 50%; 다음 봉 시가 가정 |
| v2 | trend_8_26 AND reversion_12 | 9801.35 | -198.65 | sell / filled / 직전 완료 봉 목표 비중 0%; 다음 봉 시가 가정 |
| v2 | trend_8_26 + reversion_12 | 9535.80 | -464.20 | sell / filled / 직전 완료 봉 목표 비중 50%; 다음 봉 시가 가정 |
| v2 | trend_8_26 AND volume_26 | 9606.04 | -393.96 | sell / filled / 직전 완료 봉 목표 비중 0%; 다음 봉 시가 가정 |
| v2 | trend_8_26 + volume_26 | 9453.54 | -546.46 | sell / filled / 직전 완료 봉 목표 비중 50%; 다음 봉 시가 가정 |
| v2 | momentum_26 AND breakout_8 | 9611.27 | -388.73 | sell / filled / 직전 완료 봉 목표 비중 0%; 다음 봉 시가 가정 |
| v2 | momentum_26 + breakout_8 | 9492.20 | -507.80 | sell / filled / 직전 완료 봉 목표 비중 0%; 다음 봉 시가 가정 |
| v2 | momentum_26 AND reversion_12 | 9864.00 | -136.00 | sell / filled / 직전 완료 봉 목표 비중 0%; 다음 봉 시가 가정 |
| v2 | momentum_26 + reversion_12 | 9560.28 | -439.72 | sell / filled / 직전 완료 봉 목표 비중 0%; 다음 봉 시가 가정 |
| v2 | momentum_26 AND volume_26 | 9689.11 | -310.89 | sell / filled / 직전 완료 봉 목표 비중 0%; 다음 봉 시가 가정 |
| v2 | momentum_26 + volume_26 | 9457.85 | -542.15 | sell / filled / 직전 완료 봉 목표 비중 0%; 다음 봉 시가 가정 |
| v2 | breakout_8 AND reversion_12 | 10000.00 | 0.00 | 대기 /  / 새 신호 대기 |
| v2 | breakout_8 + reversion_12 | 9396.79 | -603.21 | sell / filled / 직전 완료 봉 목표 비중 0%; 다음 봉 시가 가정 |
| v2 | breakout_8 AND volume_26 | 9808.87 | -191.13 | sell / filled / 직전 완료 봉 목표 비중 0%; 다음 봉 시가 가정 |
| v2 | breakout_8 + volume_26 | 9315.70 | -684.30 | sell / filled / 직전 완료 봉 목표 비중 0%; 다음 봉 시가 가정 |
| v2 | reversion_12 AND volume_26 | 9641.69 | -358.31 | sell / filled / 직전 완료 봉 목표 비중 0%; 다음 봉 시가 가정 |
| v2 | reversion_12 + volume_26 | 9343.62 | -656.38 | sell / filled / 직전 완료 봉 목표 비중 0%; 다음 봉 시가 가정 |
| v2 | ema_12_26 | 9788.37 | -211.63 | buy / partial / EMA12 > EMA26; 조건 충족; EMA12=767.528, EMA26=767.458; 직전 완료 봉 목표를 다음 봉 시가에 모의 적용 |
| v2 | macd_12_26_9 | 9808.62 | -191.38 | buy / partial / MACD > 신호선 그리고 MACD > 0; 조건 충족; MACD=0.396374, signal9=0.142666; 직전 완료 봉 목표를 다음 봉 시가에 모의 적용 |
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
| v2 | chaikin_3_10 | 9858.53 | -141.47 | sell / filled / ADL의 EMA3 - EMA10 > 0 그리고 종가 > EMA26; 조건 미충족; Chaikin3_10=-974621, ADL=7.60516e+06, close=768.275, EMA26=767.362; 직전 완료 봉 목표를 다음 봉 시가에 모의 적용 |
| v2 | roc_10_momentum | 9951.43 | -48.57 | sell / filled / 10봉 ROC > 1% 그리고 종가 > EMA26; 조건 미충족; ROC10_percent=0.806376, close=769.45, EMA26=767.181; 직전 완료 봉 목표를 다음 봉 시가에 모의 적용 |
| v2 | trix_15_trend | 9752.23 | -247.77 | buy / partial / 15봉 삼중 EMA의 1봉 변화율 TRIX > 0 그리고 종가 > EMA26; 조건 충족; TRIX15_percent=0.0030347, close=767.955, EMA26=767.326; 직전 완료 봉 목표를 다음 봉 시가에 모의 적용 |
| v2 | keltner_20_breakout | 9922.73 | -77.27 | sell / filled / 종가 > EMA20 + 2 x Wilder ATR14; 조건 미충족; close=768.93, upper_Keltner=771.837, EMA20=768.595, ATR14=1.6209; 직전 완료 봉 목표를 다음 봉 시가에 모의 적용 |
| v2 | opening_range_30m | 9753.43 | -246.57 | buy / partial / 뉴욕 09:30·09:45 두 완료 봉 최고가를 10:00 이후 종가가 돌파; 조건 충족; close=769.1, opening_high=768; 직전 완료 봉 목표를 다음 봉 시가에 모의 적용 |

### 같은 기간의 비용·노출 비교 (사후 연구)

| 전략 | 비용 전 | 비용 후 | 100% 보유 | 같은 평균 노출 보유 | 평균 노출 |
|---|---:|---:|---:|---:|---:|
| cash | 0.00% | 0.00% | 0.31% | 0.00% | 0.00% |
| buy_hold | 0.73% | 0.31% | 0.31% | 0.31% | 100.00% |
| trend_8_26 | 1.28% | -2.47% | 0.31% | 0.16% | 53.03% |
| momentum_26 | -0.59% | -4.68% | 0.31% | 0.16% | 52.24% |
| breakout_8 | -0.28% | -16.76% | 0.31% | 0.07% | 23.48% |
| reversion_12 | -1.42% | -11.25% | 0.31% | 0.08% | 27.18% |
| volume_26 | -1.27% | -10.36% | 0.31% | 0.03% | 9.23% |
| trend_8_26 AND momentum_26 | 0.39% | -3.74% | 0.31% | 0.14% | 45.38% |
| trend_8_26 + momentum_26 | 0.34% | -3.58% | 0.31% | 0.16% | 52.64% |
| trend_8_26 AND breakout_8 | -0.15% | -11.60% | 0.31% | 0.04% | 13.98% |
| trend_8_26 + breakout_8 | 0.50% | -9.52% | 0.31% | 0.12% | 38.27% |
| trend_8_26 AND reversion_12 | -0.14% | -3.84% | 0.31% | 0.02% | 6.60% |
| trend_8_26 + reversion_12 | -0.07% | -6.78% | 0.31% | 0.12% | 40.11% |
| trend_8_26 AND volume_26 | -1.01% | -5.87% | 0.31% | 0.02% | 5.28% |
| trend_8_26 + volume_26 | 0.00% | -6.50% | 0.31% | 0.10% | 31.14% |
| momentum_26 AND breakout_8 | 0.28% | -11.60% | 0.31% | 0.05% | 15.30% |
| momentum_26 + breakout_8 | -0.44% | -10.92% | 0.31% | 0.12% | 37.87% |
| momentum_26 AND reversion_12 | -0.94% | -5.41% | 0.31% | 0.02% | 7.12% |
| momentum_26 + reversion_12 | -1.00% | -7.45% | 0.31% | 0.12% | 39.71% |
| momentum_26 AND volume_26 | -0.73% | -4.41% | 0.31% | 0.01% | 3.43% |
| momentum_26 + volume_26 | -0.93% | -6.40% | 0.31% | 0.09% | 30.74% |
| breakout_8 AND reversion_12 | 0.00% | 0.00% | 0.31% | 0.00% | 0.00% |
| breakout_8 + reversion_12 | -0.85% | -13.70% | 0.31% | 0.08% | 25.34% |
| breakout_8 AND volume_26 | -0.33% | -2.40% | 0.31% | 0.01% | 1.85% |
| breakout_8 + volume_26 | -0.78% | -12.53% | 0.31% | 0.05% | 16.37% |
| reversion_12 AND volume_26 | -0.88% | -4.95% | 0.31% | 0.01% | 3.69% |
| reversion_12 + volume_26 | -1.34% | -10.62% | 0.31% | 0.06% | 18.21% |
| ema_12_26 | -0.67% | -4.36% | 0.31% | 0.17% | 54.35% |
| macd_12_26_9 | 0.02% | -4.89% | 0.31% | 0.10% | 32.98% |
| rsi_14_recovery | -0.53% | -4.22% | 0.31% | 0.01% | 2.37% |
| bollinger_20_reentry | -1.07% | -6.72% | 0.31% | 0.01% | 3.69% |
| donchian_20 | 0.09% | -7.58% | 0.31% | 0.02% | 7.12% |
| atr_14_breakout | 0.54% | -5.20% | 0.31% | 0.01% | 4.22% |
| session_vwap | 2.20% | -7.99% | 0.31% | 0.15% | 49.34% |
| obv_20 | 0.26% | -7.43% | 0.31% | 0.12% | 39.05% |
| stochastic_14_3_recovery | -0.40% | -14.02% | 0.31% | 0.03% | 9.23% |
| mfi_14_recovery | -0.01% | -3.31% | 0.31% | 0.01% | 2.11% |
| adx_14_trend | 0.32% | -3.40% | 0.31% | 0.09% | 28.23% |
| aroon_25_trend | 0.82% | -2.10% | 0.31% | 0.08% | 25.86% |
| cci_20_momentum | -0.10% | -8.53% | 0.31% | 0.07% | 23.22% |
| williams_14_recovery | -0.58% | -10.49% | 0.31% | 0.02% | 6.60% |
| cmf_20_accumulation | 2.20% | -1.59% | 0.31% | 0.14% | 44.85% |
| chaikin_3_10 | 1.85% | -4.77% | 0.31% | 0.12% | 40.37% |
| roc_10_momentum | -0.13% | -0.97% | 0.31% | 0.00% | 1.06% |
| trix_15_trend | -0.28% | -4.39% | 0.31% | 0.13% | 40.63% |
| keltner_20_breakout | -0.26% | -4.36% | 0.31% | 0.04% | 11.61% |
| opening_range_30m | 0.10% | -6.40% | 0.31% | 0.11% | 34.04% |

동일 구간·초기 자금, 종료 시 청산 비용 포함. 노출 맞춤은 사후 설명용이며 v2 실제 계좌 성과가 아닙니다.
[낙폭 분해·비용 영향·전체 구간](SPY/comparison.json)

[v1 전체 기록](SPY/accounts.json) · [v2 전체 기록](SPY/accounts-v2.json)

## QQQ 계좌

| 모델 | 전략 | 평가액 USD | 손익 USD | 최근 매매·이유 |
|---|---|---:|---:|---|
| v1 | cash | 10000.00 | 0.00 | 대기 /  / 새 신호 대기 |
| v1 | buy_hold | 9892.46 | -107.54 | buy /  / buy_hold: prior completed bar target 100%; next bar open simulation |
| v1 | trend_8_26 | 9881.60 | -118.40 | sell /  / trend_8_26: prior completed bar target 0%; next bar open simulation |
| v1 | momentum_26 | 9617.56 | -382.44 | sell /  / momentum_26: prior completed bar target 0%; next bar open simulation |
| v1 | breakout_8 | 9742.42 | -257.58 | sell /  / breakout_8: prior completed bar target 0%; next bar open simulation |
| v1 | reversion_12 | 9812.67 | -187.33 | sell /  / reversion_12: prior completed bar target 0%; next bar open simulation |
| v1 | volume_26 | 9671.04 | -328.96 | buy /  / volume_26: prior completed bar target 100%; next bar open simulation |
| v1 | trend_8_26 AND momentum_26 | 9890.12 | -109.88 | sell /  / trend_8_26 AND momentum_26: prior completed bar target 0%; next bar open simulation |
| v1 | trend_8_26 + momentum_26 | 9768.30 | -231.70 | sell /  / trend_8_26 + momentum_26: prior completed bar target 0%; next bar open simulation |
| v1 | trend_8_26 AND breakout_8 | 9989.91 | -10.09 | sell /  / trend_8_26 AND breakout_8: prior completed bar target 0%; next bar open simulation |
| v1 | trend_8_26 + breakout_8 | 9851.08 | -148.92 | sell /  / trend_8_26 + breakout_8: prior completed bar target 0%; next bar open simulation |
| v1 | trend_8_26 AND reversion_12 | 9902.56 | -97.44 | sell /  / trend_8_26 AND reversion_12: prior completed bar target 0%; next bar open simulation |
| v1 | trend_8_26 + reversion_12 | 9847.23 | -152.77 | sell /  / trend_8_26 + reversion_12: prior completed bar target 0%; next bar open simulation |
| v1 | trend_8_26 AND volume_26 | 9932.72 | -67.28 | sell /  / trend_8_26 AND volume_26: prior completed bar target 0%; next bar open simulation |
| v1 | trend_8_26 + volume_26 | 9775.66 | -224.34 | buy /  / trend_8_26 + volume_26: prior completed bar target 50%; next bar open simulation |
| v1 | momentum_26 AND breakout_8 | 9773.97 | -226.03 | sell /  / momentum_26 AND breakout_8: prior completed bar target 0%; next bar open simulation |
| v1 | momentum_26 + breakout_8 | 9679.84 | -320.16 | sell /  / momentum_26 + breakout_8: prior completed bar target 0%; next bar open simulation |
| v1 | momentum_26 AND reversion_12 | 9800.84 | -199.16 | sell /  / momentum_26 AND reversion_12: prior completed bar target 0%; next bar open simulation |
| v1 | momentum_26 + reversion_12 | 9714.89 | -285.11 | sell /  / momentum_26 + reversion_12: prior completed bar target 0%; next bar open simulation |
| v1 | momentum_26 AND volume_26 | 9836.75 | -163.25 | sell /  / momentum_26 AND volume_26: prior completed bar target 0%; next bar open simulation |
| v1 | momentum_26 + volume_26 | 9663.58 | -336.42 | buy /  / momentum_26 + volume_26: prior completed bar target 50%; next bar open simulation |
| v1 | breakout_8 AND reversion_12 | 10000.00 | 0.00 | 대기 /  / 새 신호 대기 |
| v1 | breakout_8 + reversion_12 | 9797.19 | -202.81 | sell /  / breakout_8 + reversion_12: prior completed bar target 0%; next bar open simulation |
| v1 | breakout_8 AND volume_26 | 9947.15 | -52.85 | sell /  / breakout_8 AND volume_26: prior completed bar target 0%; next bar open simulation |
| v1 | breakout_8 + volume_26 | 9726.11 | -273.89 | buy /  / breakout_8 + volume_26: prior completed bar target 50%; next bar open simulation |
| v1 | reversion_12 AND volume_26 | 9907.31 | -92.69 | sell /  / reversion_12 AND volume_26: prior completed bar target 0%; next bar open simulation |
| v1 | reversion_12 + volume_26 | 9780.71 | -219.29 | buy /  / reversion_12 + volume_26: prior completed bar target 50%; next bar open simulation |
| v1 | ema_12_26 | 9695.35 | -304.65 | buy /  / EMA12 > EMA26; 조건 충족; EMA12=719.103, EMA26=719.016 |
| v1 | macd_12_26_9 | 9812.94 | -187.06 | buy /  / MACD > 신호선 그리고 MACD > 0; 조건 충족; MACD=0.086929, signal9=-0.0192949 |
| v1 | rsi_14_recovery | 9809.40 | -190.60 | sell /  / 직전 RSI14 < 30, 현재 RSI14 >= 30 (한 봉 목표); 조건 미충족; RSI14=50.2063, previous_RSI14=44.1729 |
| v1 | bollinger_20_reentry | 9878.60 | -121.40 | sell /  / 직전 종가 < 직전 하단밴드, 현재 하단밴드 <= 종가 <= SMA20 (한 봉 목표); 조건 미충족; close=718.66, lower20=714.386, SMA20=719.409, previous_lower20=714.271 |
| v1 | donchian_20 | 9951.11 | -48.89 | sell /  / 종가 > 현재 봉을 제외한 직전 20봉 최고가; 조건 미충족; close=724.13, prior_high20=724.151 |
| v1 | atr_14_breakout | 9945.80 | -54.20 | sell /  / 종가 > 직전 종가 + 직전 ATR14 그리고 종가 > EMA26; 조건 미충족; close=721.52, threshold=724.646, prior_ATR14=2.53578, EMA26=719.016 |
| v1 | session_vwap | 9808.33 | -191.67 | sell /  / 종가 > 뉴욕 거래일별 누적 전형가격 VWAP; 조건 미충족; close=718.891, session_VWAP=720.759, session_volume=1.23053e+08 |
| v1 | obv_20 | 9818.13 | -181.87 | sell /  / OBV > OBV의 SMA20 그리고 종가 > EMA26; 조건 미충족; OBV=1.44575e+08, OBV_SMA20=8.79592e+07, close=718.891, EMA26=719.211 |
| v1 | stochastic_14_3_recovery | 9618.80 | -381.20 | sell /  / 직전 %K14 < 20에서 %K14가 %D3 상향 돌파 (한 봉 목표); 조건 미충족; K14=76.4321, D3=43.007, previous_K14=52.497, previous_D3=21.4564 |
| v1 | mfi_14_recovery | 9813.56 | -186.44 | sell /  / 직전 MFI14 < 20, 현재 MFI14 >= 20 (한 봉 목표); 조건 미충족; MFI14=30.3876, previous_MFI14=31.1747 |
| v1 | adx_14_trend | 9926.53 | -73.47 | sell /  / Wilder ADX14 >= 25 그리고 +DI14 > -DI14; 조건 미충족; ADX14=23.9831, plus_DI14=26.5781, minus_DI14=24.6326 |
| v1 | aroon_25_trend | 9875.01 | -124.99 | sell /  / Aroon25 Up > 70 그리고 Down < 30 (동률이면 최신 극값); 조건 미충족; Aroon_up=68, Aroon_down=20 |
| v1 | cci_20_momentum | 9880.19 | -119.81 | sell /  / CCI20 > 100 (전형가격·평균절대편차); 조건 미충족; CCI20=19.2232 |
| v1 | williams_14_recovery | 9710.09 | -289.91 | sell /  / 직전 Williams %R14 < -80, 현재 >= -80 (한 봉 목표); 조건 미충족; Williams_R14=-23.5679, previous_R14=-47.503 |
| v1 | cmf_20_accumulation | 9635.68 | -364.32 | sell /  / Chaikin Money Flow20 > 0.1; 조건 미충족; CMF20=0.0748111, volume20=2.30433e+08 |
| v1 | chaikin_3_10 | 9822.77 | -177.23 | sell /  / ADL의 EMA3 - EMA10 > 0 그리고 종가 > EMA26; 조건 미충족; Chaikin3_10=1.65294e+07, ADL=2.56436e+08, close=718.891, EMA26=719.211 |
| v1 | roc_10_momentum | 9990.50 | -9.50 | sell /  / 10봉 ROC > 1% 그리고 종가 > EMA26; 조건 미충족; ROC10_percent=0.483561, close=722.477, EMA26=718.78 |
| v1 | trix_15_trend | 9766.60 | -233.40 | sell /  / 15봉 삼중 EMA의 1봉 변화율 TRIX > 0 그리고 종가 > EMA26; 조건 미충족; TRIX15_percent=0.00310265, close=718.891, EMA26=719.211 |
| v1 | keltner_20_breakout | 9904.16 | -95.84 | sell /  / 종가 > EMA20 + 2 x Wilder ATR14; 조건 미충족; close=723.31, upper_Keltner=723.407, EMA20=718.722, ATR14=2.34265 |
| v1 | opening_range_30m | 9764.88 | -235.12 | buy /  / 뉴욕 09:30·09:45 두 완료 봉 최고가를 10:00 이후 종가가 돌파; 조건 충족; close=718.66, opening_high=716.18 |
| v2 | cash | 10000.00 | 0.00 | 대기 /  / 새 신호 대기 |
| v2 | buy_hold | 9572.69 | -427.31 | buy / partial / 직전 완료 봉 목표 비중 100%; 다음 봉 시가 가정 |
| v2 | trend_8_26 | 9683.75 | -316.25 | sell / filled / 직전 완료 봉 목표 비중 0%; 다음 봉 시가 가정 |
| v2 | momentum_26 | 9511.63 | -488.37 | sell / filled / 직전 완료 봉 목표 비중 0%; 다음 봉 시가 가정 |
| v2 | breakout_8 | 9411.37 | -588.63 | sell / filled / 직전 완료 봉 목표 비중 0%; 다음 봉 시가 가정 |
| v2 | reversion_12 | 9326.37 | -673.63 | sell / filled / 직전 완료 봉 목표 비중 0%; 다음 봉 시가 가정 |
| v2 | volume_26 | 9565.80 | -434.20 | 중단: 손실 한도 / sell / filled / 직전 완료 봉 목표 비중 0%; 다음 봉 시가 가정 |
| v2 | trend_8_26 AND momentum_26 | 9785.10 | -214.90 | sell / filled / 직전 완료 봉 목표 비중 0%; 다음 봉 시가 가정 |
| v2 | trend_8_26 + momentum_26 | 9617.61 | -382.39 | sell / filled / 직전 완료 봉 목표 비중 0%; 다음 봉 시가 가정 |
| v2 | trend_8_26 AND breakout_8 | 9883.87 | -116.13 | sell / filled / 직전 완료 봉 목표 비중 0%; 다음 봉 시가 가정 |
| v2 | trend_8_26 + breakout_8 | 9586.72 | -413.28 | sell / filled / 직전 완료 봉 목표 비중 0%; 다음 봉 시가 가정 |
| v2 | trend_8_26 AND reversion_12 | 9761.15 | -238.85 | sell / filled / 직전 완료 봉 목표 비중 0%; 다음 봉 시가 가정 |
| v2 | trend_8_26 + reversion_12 | 9503.22 | -496.78 | sell / filled / 직전 완료 봉 목표 비중 0%; 다음 봉 시가 가정 |
| v2 | trend_8_26 AND volume_26 | 9769.99 | -230.01 | sell / filled / 직전 완료 봉 목표 비중 0%; 다음 봉 시가 가정 |
| v2 | trend_8_26 + volume_26 | 9379.70 | -620.30 | buy / filled / 직전 완료 봉 목표 비중 50%; 다음 봉 시가 가정 |
| v2 | momentum_26 AND breakout_8 | 9727.76 | -272.24 | sell / filled / 직전 완료 봉 목표 비중 0%; 다음 봉 시가 가정 |
| v2 | momentum_26 + breakout_8 | 9461.38 | -538.62 | sell / filled / 직전 완료 봉 목표 비중 0%; 다음 봉 시가 가정 |
| v2 | momentum_26 AND reversion_12 | 9794.96 | -205.04 | sell / filled / 직전 완료 봉 목표 비중 0%; 다음 봉 시가 가정 |
| v2 | momentum_26 + reversion_12 | 9438.27 | -561.73 | sell / filled / 직전 완료 봉 목표 비중 0%; 다음 봉 시가 가정 |
| v2 | momentum_26 AND volume_26 | 9768.76 | -231.24 | sell / filled / 직전 완료 봉 목표 비중 0%; 다음 봉 시가 가정 |
| v2 | momentum_26 + volume_26 | 9315.59 | -684.41 | buy / filled / 직전 완료 봉 목표 비중 50%; 다음 봉 시가 가정 |
| v2 | breakout_8 AND reversion_12 | 10000.00 | 0.00 | 대기 /  / 새 신호 대기 |
| v2 | breakout_8 + reversion_12 | 9447.62 | -552.38 | sell / filled / 직전 완료 봉 목표 비중 0%; 다음 봉 시가 가정 |
| v2 | breakout_8 AND volume_26 | 9891.45 | -108.55 | sell / filled / 직전 완료 봉 목표 비중 0%; 다음 봉 시가 가정 |
| v2 | breakout_8 + volume_26 | 9305.44 | -694.56 | buy / filled / 직전 완료 봉 목표 비중 50%; 다음 봉 시가 가정 |
| v2 | reversion_12 AND volume_26 | 9547.64 | -452.36 | 중단: 손실 한도 / sell / filled / 직전 완료 봉 목표 비중 0%; 다음 봉 시가 가정 |
| v2 | reversion_12 + volume_26 | 9263.46 | -736.54 | buy / filled / 직전 완료 봉 목표 비중 50%; 다음 봉 시가 가정 |
| v2 | ema_12_26 | 9690.50 | -309.50 | buy / partial / EMA12 > EMA26; 조건 충족; EMA12=719.103, EMA26=719.016; 직전 완료 봉 목표를 다음 봉 시가에 모의 적용 |
| v2 | macd_12_26_9 | 9808.04 | -191.96 | buy / partial / MACD > 신호선 그리고 MACD > 0; 조건 충족; MACD=0.086929, signal9=-0.0192949; 직전 완료 봉 목표를 다음 봉 시가에 모의 적용 |
| v2 | rsi_14_recovery | 9801.56 | -198.44 | sell / filled / 직전 RSI14 < 30, 현재 RSI14 >= 30 (한 봉 목표); 조건 미충족; RSI14=50.2063, previous_RSI14=44.1729; 직전 완료 봉 목표를 다음 봉 시가에 모의 적용 |
| v2 | bollinger_20_reentry | 9872.68 | -127.32 | sell / filled / 직전 종가 < 직전 하단밴드, 현재 하단밴드 <= 종가 <= SMA20 (한 봉 목표); 조건 미충족; close=718.66, lower20=714.386, SMA20=719.409, previous_lower20=714.271; 직전 완료 봉 목표를 다음 봉 시가에 모의 적용 |
| v2 | donchian_20 | 9947.13 | -52.87 | sell / filled / 종가 > 현재 봉을 제외한 직전 20봉 최고가; 조건 미충족; close=724.13, prior_high20=724.151; 직전 완료 봉 목표를 다음 봉 시가에 모의 적용 |
| v2 | atr_14_breakout | 9941.83 | -58.17 | sell / filled / 종가 > 직전 종가 + 직전 ATR14 그리고 종가 > EMA26; 조건 미충족; close=721.52, threshold=724.646, prior_ATR14=2.53578, EMA26=719.016; 직전 완료 봉 목표를 다음 봉 시가에 모의 적용 |
| v2 | session_vwap | 9798.52 | -201.48 | sell / filled / 종가 > 뉴욕 거래일별 누적 전형가격 VWAP; 조건 미충족; close=718.891, session_VWAP=720.759, session_volume=1.23053e+08; 직전 완료 봉 목표를 다음 봉 시가에 모의 적용 |
| v2 | obv_20 | 9812.24 | -187.76 | sell / filled / OBV > OBV의 SMA20 그리고 종가 > EMA26; 조건 미충족; OBV=1.44575e+08, OBV_SMA20=8.79592e+07, close=718.891, EMA26=719.211; 직전 완료 봉 목표를 다음 봉 시가에 모의 적용 |
| v2 | stochastic_14_3_recovery | 9694.13 | -305.87 | 중단: 손실 한도 / sell / filled / 직전 %K14 < 20에서 %K14가 %D3 상향 돌파 (한 봉 목표); 조건 미충족; K14=10.576, D3=8.00581, previous_K14=7.39787, previous_D3=7.27486; 직전 완료 봉 목표를 다음 봉 시가에 모의 적용 |
| v2 | mfi_14_recovery | 9809.63 | -190.37 | sell / filled / 직전 MFI14 < 20, 현재 MFI14 >= 20 (한 봉 목표); 조건 미충족; MFI14=30.3876, previous_MFI14=31.1747; 직전 완료 봉 목표를 다음 봉 시가에 모의 적용 |
| v2 | adx_14_trend | 9922.56 | -77.44 | sell / filled / Wilder ADX14 >= 25 그리고 +DI14 > -DI14; 조건 미충족; ADX14=23.9831, plus_DI14=26.5781, minus_DI14=24.6326; 직전 완료 봉 목표를 다음 봉 시가에 모의 적용 |
| v2 | aroon_25_trend | 9871.06 | -128.94 | sell / filled / Aroon25 Up > 70 그리고 Down < 30 (동률이면 최신 극값); 조건 미충족; Aroon_up=68, Aroon_down=20; 직전 완료 봉 목표를 다음 봉 시가에 모의 적용 |
| v2 | cci_20_momentum | 9874.26 | -125.74 | sell / filled / CCI20 > 100 (전형가격·평균절대편차); 조건 미충족; CCI20=19.2232; 직전 완료 봉 목표를 다음 봉 시가에 모의 적용 |
| v2 | williams_14_recovery | 9696.51 | -303.49 | sell / filled / 직전 Williams %R14 < -80, 현재 >= -80 (한 봉 목표); 조건 미충족; Williams_R14=-23.5679, previous_R14=-47.503; 직전 완료 봉 목표를 다음 봉 시가에 모의 적용 |
| v2 | cmf_20_accumulation | 9624.13 | -375.87 | sell / filled / Chaikin Money Flow20 > 0.1; 조건 미충족; CMF20=0.0748111, volume20=2.30433e+08; 직전 완료 봉 목표를 다음 봉 시가에 모의 적용 |
| v2 | chaikin_3_10 | 9816.88 | -183.12 | sell / filled / ADL의 EMA3 - EMA10 > 0 그리고 종가 > EMA26; 조건 미충족; Chaikin3_10=1.65294e+07, ADL=2.56436e+08, close=718.891, EMA26=719.211; 직전 완료 봉 목표를 다음 봉 시가에 모의 적용 |
| v2 | roc_10_momentum | 9988.50 | -11.50 | sell / filled / 10봉 ROC > 1% 그리고 종가 > EMA26; 조건 미충족; ROC10_percent=0.483561, close=722.477, EMA26=718.78; 직전 완료 봉 목표를 다음 봉 시가에 모의 적용 |
| v2 | trix_15_trend | 9760.74 | -239.26 | sell / filled / 15봉 삼중 EMA의 1봉 변화율 TRIX > 0 그리고 종가 > EMA26; 조건 미충족; TRIX15_percent=0.00310265, close=718.891, EMA26=719.211; 직전 완료 봉 목표를 다음 봉 시가에 모의 적용 |
| v2 | keltner_20_breakout | 9900.20 | -99.80 | sell / filled / 종가 > EMA20 + 2 x Wilder ATR14; 조건 미충족; close=723.31, upper_Keltner=723.407, EMA20=718.722, ATR14=2.34265; 직전 완료 봉 목표를 다음 봉 시가에 모의 적용 |
| v2 | opening_range_30m | 9758.05 | -241.95 | buy / partial / 뉴욕 09:30·09:45 두 완료 봉 최고가를 10:00 이후 종가가 돌파; 조건 충족; close=718.66, opening_high=716.18; 직전 완료 봉 목표를 다음 봉 시가에 모의 적용 |

### 같은 기간의 비용·노출 비교 (사후 연구)

| 전략 | 비용 전 | 비용 후 | 100% 보유 | 같은 평균 노출 보유 | 평균 노출 |
|---|---:|---:|---:|---:|---:|
| cash | 0.00% | 0.00% | -2.92% | -0.00% | 0.00% |
| buy_hold | -2.51% | -2.92% | -2.92% | -2.92% | 100.00% |
| trend_8_26 | 0.66% | -2.66% | -2.92% | -1.31% | 44.85% |
| momentum_26 | -2.64% | -7.81% | -2.92% | -1.22% | 41.69% |
| breakout_8 | -1.60% | -17.17% | -2.92% | -0.56% | 19.26% |
| reversion_12 | -0.70% | -12.09% | -2.92% | -0.85% | 29.29% |
| volume_26 | -1.28% | -14.42% | -2.92% | -0.45% | 15.57% |
| trend_8_26 AND momentum_26 | 0.29% | -3.43% | -2.92% | -1.02% | 35.09% |
| trend_8_26 + momentum_26 | -1.00% | -4.87% | -2.92% | -1.26% | 43.27% |
| trend_8_26 AND breakout_8 | -0.01% | -8.84% | -2.92% | -0.33% | 11.35% |
| trend_8_26 + breakout_8 | -0.47% | -9.45% | -2.92% | -0.93% | 32.06% |
| trend_8_26 AND reversion_12 | -0.22% | -4.73% | -2.92% | -0.19% | 6.60% |
| trend_8_26 + reversion_12 | -0.01% | -7.11% | -2.92% | -1.08% | 37.08% |
| trend_8_26 AND volume_26 | 0.34% | -3.79% | -2.92% | -0.13% | 4.49% |
| trend_8_26 + volume_26 | -0.31% | -8.54% | -2.92% | -0.88% | 30.22% |
| momentum_26 AND breakout_8 | -0.81% | -10.32% | -2.92% | -0.35% | 11.87% |
| momentum_26 + breakout_8 | -2.11% | -12.43% | -2.92% | -0.89% | 30.48% |
| momentum_26 AND reversion_12 | -1.16% | -6.41% | -2.92% | -0.20% | 6.86% |
| momentum_26 + reversion_12 | -1.66% | -9.60% | -2.92% | -1.04% | 35.49% |
| momentum_26 AND volume_26 | -0.28% | -4.38% | -2.92% | -0.11% | 3.69% |
| momentum_26 + volume_26 | -1.96% | -10.81% | -2.92% | -0.83% | 28.63% |
| breakout_8 AND reversion_12 | 0.00% | 0.00% | -2.92% | -0.00% | 0.00% |
| breakout_8 + reversion_12 | -1.14% | -13.77% | -2.92% | -0.71% | 24.28% |
| breakout_8 AND volume_26 | 0.32% | -2.18% | -2.92% | -0.05% | 1.85% |
| breakout_8 + volume_26 | -1.44% | -14.38% | -2.92% | -0.51% | 17.42% |
| reversion_12 AND volume_26 | -1.31% | -8.11% | -2.92% | -0.25% | 8.44% |
| reversion_12 + volume_26 | -0.98% | -12.72% | -2.92% | -0.65% | 22.43% |
| ema_12_26 | -0.87% | -3.33% | -2.92% | -1.22% | 41.69% |
| macd_12_26_9 | 0.89% | -3.26% | -2.92% | -0.71% | 24.27% |
| rsi_14_recovery | -0.47% | -5.76% | -2.92% | -0.10% | 3.43% |
| bollinger_20_reentry | -0.08% | -6.18% | -2.92% | -0.12% | 3.96% |
| donchian_20 | 0.59% | -4.75% | -2.92% | -0.17% | 5.80% |
| atr_14_breakout | 0.47% | -3.67% | -2.92% | -0.09% | 3.17% |
| session_vwap | -0.10% | -11.55% | -2.92% | -1.42% | 48.55% |
| obv_20 | -1.00% | -9.36% | -2.92% | -0.87% | 29.82% |
| stochastic_14_3_recovery | -0.31% | -11.75% | -2.92% | -0.22% | 7.65% |
| mfi_14_recovery | -1.23% | -3.69% | -2.92% | -0.05% | 1.58% |
| adx_14_trend | -0.11% | -3.00% | -2.92% | -0.63% | 21.64% |
| aroon_25_trend | 1.27% | -2.07% | -2.92% | -0.53% | 18.21% |
| cci_20_momentum | -0.45% | -5.74% | -2.92% | -0.50% | 17.15% |
| williams_14_recovery | -0.63% | -10.91% | -2.92% | -0.20% | 6.86% |
| cmf_20_accumulation | -1.85% | -9.37% | -2.92% | -0.88% | 30.34% |
| chaikin_3_10 | -2.46% | -9.94% | -2.92% | -1.08% | 36.94% |
| roc_10_momentum | -0.00% | -1.67% | -2.92% | -0.12% | 4.22% |
| trix_15_trend | -0.23% | -2.72% | -2.92% | -0.99% | 34.04% |
| keltner_20_breakout | -0.89% | -5.76% | -2.92% | -0.24% | 8.18% |
| opening_range_30m | -1.03% | -7.85% | -2.92% | -0.78% | 26.91% |

동일 구간·초기 자금, 종료 시 청산 비용 포함. 노출 맞춤은 사후 설명용이며 v2 실제 계좌 성과가 아닙니다.
[낙폭 분해·비용 영향·전체 구간](QQQ/comparison.json)

[v1 전체 기록](QQQ/accounts.json) · [v2 전체 기록](QQQ/accounts-v2.json)

## IWM 계좌

| 모델 | 전략 | 평가액 USD | 손익 USD | 최근 매매·이유 |
|---|---|---:|---:|---|
| v1 | cash | 10000.00 | 0.00 | 대기 /  / 새 신호 대기 |
| v1 | buy_hold | 10000.13 | 0.13 | buy /  / buy_hold: prior completed bar target 100%; next bar open simulation |
| v1 | trend_8_26 | 9805.45 | -194.55 | buy /  / trend_8_26: prior completed bar target 100%; next bar open simulation |
| v1 | momentum_26 | 9976.40 | -23.60 | buy /  / momentum_26: prior completed bar target 100%; next bar open simulation |
| v1 | breakout_8 | 9713.59 | -286.41 | sell /  / breakout_8: prior completed bar target 0%; next bar open simulation |
| v1 | reversion_12 | 9786.62 | -213.38 | sell /  / reversion_12: prior completed bar target 0%; next bar open simulation |
| v1 | volume_26 | 9923.29 | -76.71 | sell /  / volume_26: prior completed bar target 0%; next bar open simulation |
| v1 | trend_8_26 AND momentum_26 | 9821.38 | -178.62 | buy /  / trend_8_26 AND momentum_26: prior completed bar target 100%; next bar open simulation |
| v1 | trend_8_26 + momentum_26 | 9890.62 | -109.38 | buy /  / trend_8_26 + momentum_26: prior completed bar target 100%; next bar open simulation |
| v1 | trend_8_26 AND breakout_8 | 9803.67 | -196.33 | sell /  / trend_8_26 AND breakout_8: prior completed bar target 0%; next bar open simulation |
| v1 | trend_8_26 + breakout_8 | 9759.60 | -240.40 | sell /  / trend_8_26 + breakout_8: prior completed bar target 50%; next bar open simulation |
| v1 | trend_8_26 AND reversion_12 | 9827.31 | -172.69 | sell /  / trend_8_26 AND reversion_12: prior completed bar target 0%; next bar open simulation |
| v1 | trend_8_26 + reversion_12 | 9795.95 | -204.05 | sell /  / trend_8_26 + reversion_12: prior completed bar target 50%; next bar open simulation |
| v1 | trend_8_26 AND volume_26 | 9935.98 | -64.02 | sell /  / trend_8_26 AND volume_26: prior completed bar target 0%; next bar open simulation |
| v1 | trend_8_26 + volume_26 | 9883.86 | -116.14 | sell /  / trend_8_26 + volume_26: prior completed bar target 50%; next bar open simulation |
| v1 | momentum_26 AND breakout_8 | 9853.20 | -146.80 | sell /  / momentum_26 AND breakout_8: prior completed bar target 0%; next bar open simulation |
| v1 | momentum_26 + breakout_8 | 9863.99 | -136.01 | sell /  / momentum_26 + breakout_8: prior completed bar target 50%; next bar open simulation |
| v1 | momentum_26 AND reversion_12 | 9924.34 | -75.66 | sell /  / momentum_26 AND reversion_12: prior completed bar target 0%; next bar open simulation |
| v1 | momentum_26 + reversion_12 | 9900.76 | -99.24 | sell /  / momentum_26 + reversion_12: prior completed bar target 50%; next bar open simulation |
| v1 | momentum_26 AND volume_26 | 10062.05 | 62.05 | sell /  / momentum_26 AND volume_26: prior completed bar target 0%; next bar open simulation |
| v1 | momentum_26 + volume_26 | 9949.72 | -50.28 | sell /  / momentum_26 + volume_26: prior completed bar target 50%; next bar open simulation |
| v1 | breakout_8 AND reversion_12 | 10000.00 | 0.00 | 대기 /  / 새 신호 대기 |
| v1 | breakout_8 + reversion_12 | 9749.93 | -250.07 | sell /  / breakout_8 + reversion_12: prior completed bar target 0%; next bar open simulation |
| v1 | breakout_8 AND volume_26 | 9967.28 | -32.72 | sell /  / breakout_8 AND volume_26: prior completed bar target 0%; next bar open simulation |
| v1 | breakout_8 + volume_26 | 9837.51 | -162.49 | sell /  / breakout_8 + volume_26: prior completed bar target 0%; next bar open simulation |
| v1 | reversion_12 AND volume_26 | 9935.98 | -64.02 | sell /  / reversion_12 AND volume_26: prior completed bar target 0%; next bar open simulation |
| v1 | reversion_12 + volume_26 | 9874.40 | -125.60 | sell /  / reversion_12 + volume_26: prior completed bar target 0%; next bar open simulation |
| v1 | ema_12_26 | 9870.62 | -129.38 | buy /  / EMA12 > EMA26; 조건 충족; EMA12=271.545, EMA26=271.529 |
| v1 | macd_12_26_9 | 9949.32 | -50.68 | buy /  / MACD > 신호선 그리고 MACD > 0; 조건 충족; MACD=0.0161944, signal9=-0.0860005 |
| v1 | rsi_14_recovery | 9786.95 | -213.05 | sell /  / 직전 RSI14 < 30, 현재 RSI14 >= 30 (한 봉 목표); 조건 미충족; RSI14=46.986, previous_RSI14=37.1649 |
| v1 | bollinger_20_reentry | 9924.03 | -75.97 | sell /  / 직전 종가 < 직전 하단밴드, 현재 하단밴드 <= 종가 <= SMA20 (한 봉 목표); 조건 미충족; close=271.19, lower20=270.018, SMA20=273.224, previous_lower20=270.283 |
| v1 | donchian_20 | 9835.91 | -164.09 | sell /  / 종가 > 현재 봉을 제외한 직전 20봉 최고가; 조건 미충족; close=275.785, prior_high20=276.875 |
| v1 | atr_14_breakout | 9883.94 | -116.06 | sell /  / 종가 > 직전 종가 + 직전 ATR14 그리고 종가 > EMA26; 조건 미충족; close=276.33, threshold=276.592, prior_ATR14=0.747363, EMA26=272.499 |
| v1 | session_vwap | 9873.60 | -126.40 | buy /  / 종가 > 뉴욕 거래일별 누적 전형가격 VWAP; 조건 충족; close=272.6, session_VWAP=272.22, session_volume=3.20722e+06 |
| v1 | obv_20 | 9864.98 | -135.02 | buy /  / OBV > OBV의 SMA20 그리고 종가 > EMA26; 조건 충족; OBV=-2.88653e+07, OBV_SMA20=-3.02185e+07, close=272.6, EMA26=271.529 |
| v1 | stochastic_14_3_recovery | 9665.87 | -334.13 | sell /  / 직전 %K14 < 20에서 %K14가 %D3 상향 돌파 (한 봉 목표); 조건 미충족; K14=72.727, D3=41.2922, previous_K14=34.0903, previous_D3=23.8263 |
| v1 | mfi_14_recovery | 9934.22 | -65.78 | sell /  / 직전 MFI14 < 20, 현재 MFI14 >= 20 (한 봉 목표); 조건 미충족; MFI14=34.131, previous_MFI14=22.0435 |
| v1 | adx_14_trend | 9796.09 | -203.91 | buy /  / Wilder ADX14 >= 25 그리고 +DI14 > -DI14; 조건 충족; ADX14=26.5262, plus_DI14=49.1478, minus_DI14=9.69634 |
| v1 | aroon_25_trend | 9832.16 | -167.84 | sell /  / Aroon25 Up > 70 그리고 Down < 30 (동률이면 최신 극값); 조건 미충족; Aroon_up=100, Aroon_down=68 |
| v1 | cci_20_momentum | 9985.69 | -14.31 | buy /  / CCI20 > 100 (전형가격·평균절대편차); 조건 충족; CCI20=115.766 |
| v1 | williams_14_recovery | 9833.31 | -166.69 | sell /  / 직전 Williams %R14 < -80, 현재 >= -80 (한 봉 목표); 조건 미충족; Williams_R14=-27.273, previous_R14=-65.9097 |
| v1 | cmf_20_accumulation | 9817.51 | -182.49 | buy /  / Chaikin Money Flow20 > 0.1; 조건 충족; CMF20=0.208851, volume20=1.40263e+07 |
| v1 | chaikin_3_10 | 9865.87 | -134.13 | buy /  / ADL의 EMA3 - EMA10 > 0 그리고 종가 > EMA26; 조건 충족; Chaikin3_10=878293, ADL=-4.92877e+07, close=272.6, EMA26=271.529 |
| v1 | roc_10_momentum | 10044.25 | 44.25 | buy /  / 10봉 ROC > 1% 그리고 종가 > EMA26; 조건 충족; ROC10_percent=1.11505, close=274.305, EMA26=271.734 |
| v1 | trix_15_trend | 9951.85 | -48.15 | buy /  / 15봉 삼중 EMA의 1봉 변화율 TRIX > 0 그리고 종가 > EMA26; 조건 충족; TRIX15_percent=0.00296855, close=273.97, EMA26=271.9 |
| v1 | keltner_20_breakout | 9981.27 | -18.73 | buy /  / 종가 > EMA20 + 2 x Wilder ATR14; 조건 충족; close=274.305, upper_Keltner=273.059, EMA20=271.774, ATR14=0.64209 |
| v1 | opening_range_30m | 9956.24 | -43.76 | buy /  / 뉴욕 09:30·09:45 두 완료 봉 최고가를 10:00 이후 종가가 돌파; 조건 충족; close=275.845, opening_high=274.33 |
| v2 | cash | 10000.00 | 0.00 | 대기 /  / 새 신호 대기 |
| v2 | buy_hold | 9893.21 | -106.79 | buy / partial / 직전 완료 봉 목표 비중 100%; 다음 봉 시가 가정 |
| v2 | trend_8_26 | 9674.52 | -325.48 | buy / partial / 직전 완료 봉 목표 비중 100%; 다음 봉 시가 가정 |
| v2 | momentum_26 | 9844.20 | -155.80 | buy / partial / 직전 완료 봉 목표 비중 100%; 다음 봉 시가 가정 |
| v2 | breakout_8 | 9329.18 | -670.82 | sell / filled / 직전 완료 봉 목표 비중 0%; 다음 봉 시가 가정 |
| v2 | reversion_12 | 9325.80 | -674.20 | sell / filled / 직전 완료 봉 목표 비중 0%; 다음 봉 시가 가정 |
| v2 | volume_26 | 9434.73 | -565.27 | sell / filled / 직전 완료 봉 목표 비중 0%; 다음 봉 시가 가정 |
| v2 | trend_8_26 AND momentum_26 | 9838.68 | -161.32 | buy / partial / 직전 완료 봉 목표 비중 100%; 다음 봉 시가 가정 |
| v2 | trend_8_26 + momentum_26 | 9779.70 | -220.30 | buy / partial / 직전 완료 봉 목표 비중 100%; 다음 봉 시가 가정 |
| v2 | trend_8_26 AND breakout_8 | 9710.34 | -289.66 | sell / filled / 직전 완료 봉 목표 비중 0%; 다음 봉 시가 가정 |
| v2 | trend_8_26 + breakout_8 | 9520.58 | -479.42 | sell / filled / 직전 완료 봉 목표 비중 50%; 다음 봉 시가 가정 |
| v2 | trend_8_26 AND reversion_12 | 9705.35 | -294.65 | sell / filled / 직전 완료 봉 목표 비중 0%; 다음 봉 시가 가정 |
| v2 | trend_8_26 + reversion_12 | 9498.31 | -501.69 | sell / filled / 직전 완료 봉 목표 비중 50%; 다음 봉 시가 가정 |
| v2 | trend_8_26 AND volume_26 | 9797.73 | -202.27 | sell / filled / 직전 완료 봉 목표 비중 0%; 다음 봉 시가 가정 |
| v2 | trend_8_26 + volume_26 | 9593.98 | -406.02 | sell / filled / 직전 완료 봉 목표 비중 50%; 다음 봉 시가 가정 |
| v2 | momentum_26 AND breakout_8 | 9653.24 | -346.76 | sell / filled / 직전 완료 봉 목표 비중 0%; 다음 봉 시가 가정 |
| v2 | momentum_26 + breakout_8 | 9603.57 | -396.43 | sell / filled / 직전 완료 봉 목표 비중 50%; 다음 봉 시가 가정 |
| v2 | momentum_26 AND reversion_12 | 9881.28 | -118.72 | sell / filled / 직전 완료 봉 목표 비중 0%; 다음 봉 시가 가정 |
| v2 | momentum_26 + reversion_12 | 9621.36 | -378.64 | sell / filled / 직전 완료 봉 목표 비중 50%; 다음 봉 시가 가정 |
| v2 | momentum_26 AND volume_26 | 9957.22 | -42.78 | sell / filled / 직전 완료 봉 목표 비중 0%; 다음 봉 시가 가정 |
| v2 | momentum_26 + volume_26 | 9636.98 | -363.02 | sell / filled / 직전 완료 봉 목표 비중 50%; 다음 봉 시가 가정 |
| v2 | breakout_8 AND reversion_12 | 10000.00 | 0.00 | 대기 /  / 새 신호 대기 |
| v2 | breakout_8 + reversion_12 | 9366.25 | -633.75 | sell / filled / 직전 완료 봉 목표 비중 0%; 다음 봉 시가 가정 |
| v2 | breakout_8 AND volume_26 | 9710.25 | -289.75 | sell / filled / 직전 완료 봉 목표 비중 0%; 다음 봉 시가 가정 |
| v2 | breakout_8 + volume_26 | 9421.20 | -578.80 | sell / filled / 직전 완료 봉 목표 비중 0%; 다음 봉 시가 가정 |
| v2 | reversion_12 AND volume_26 | 9676.46 | -323.54 | sell / filled / 직전 완료 봉 목표 비중 0%; 다음 봉 시가 가정 |
| v2 | reversion_12 + volume_26 | 9419.31 | -580.69 | sell / filled / 직전 완료 봉 목표 비중 0%; 다음 봉 시가 가정 |
| v2 | ema_12_26 | 9865.69 | -134.31 | buy / partial / EMA12 > EMA26; 조건 충족; EMA12=271.545, EMA26=271.529; 직전 완료 봉 목표를 다음 봉 시가에 모의 적용 |
| v2 | macd_12_26_9 | 9944.35 | -55.65 | buy / partial / MACD > 신호선 그리고 MACD > 0; 조건 충족; MACD=0.0161944, signal9=-0.0860005; 직전 완료 봉 목표를 다음 봉 시가에 모의 적용 |
| v2 | rsi_14_recovery | 9779.12 | -220.88 | sell / filled / 직전 RSI14 < 30, 현재 RSI14 >= 30 (한 봉 목표); 조건 미충족; RSI14=46.986, previous_RSI14=37.1649; 직전 완료 봉 목표를 다음 봉 시가에 모의 적용 |
| v2 | bollinger_20_reentry | 9920.06 | -79.94 | sell / filled / 직전 종가 < 직전 하단밴드, 현재 하단밴드 <= 종가 <= SMA20 (한 봉 목표); 조건 미충족; close=271.19, lower20=270.018, SMA20=273.224, previous_lower20=270.283; 직전 완료 봉 목표를 다음 봉 시가에 모의 적용 |
| v2 | donchian_20 | 9830.01 | -169.99 | sell / filled / 종가 > 현재 봉을 제외한 직전 20봉 최고가; 조건 미충족; close=275.785, prior_high20=276.875; 직전 완료 봉 목표를 다음 봉 시가에 모의 적용 |
| v2 | atr_14_breakout | 9876.04 | -123.96 | sell / filled / 종가 > 직전 종가 + 직전 ATR14 그리고 종가 > EMA26; 조건 미충족; close=276.33, threshold=276.592, prior_ATR14=0.747363, EMA26=272.499; 직전 완료 봉 목표를 다음 봉 시가에 모의 적용 |
| v2 | session_vwap | 9864.72 | -135.28 | buy / partial / 종가 > 뉴욕 거래일별 누적 전형가격 VWAP; 조건 충족; close=272.6, session_VWAP=272.22, session_volume=3.20722e+06; 직전 완료 봉 목표를 다음 봉 시가에 모의 적용 |
| v2 | obv_20 | 9856.10 | -143.90 | buy / partial / OBV > OBV의 SMA20 그리고 종가 > EMA26; 조건 충족; OBV=-2.88653e+07, OBV_SMA20=-3.02185e+07, close=272.6, EMA26=271.529; 직전 완료 봉 목표를 다음 봉 시가에 모의 적용 |
| v2 | stochastic_14_3_recovery | 9650.41 | -349.59 | sell / filled / 직전 %K14 < 20에서 %K14가 %D3 상향 돌파 (한 봉 목표); 조건 미충족; K14=72.727, D3=41.2922, previous_K14=34.0903, previous_D3=23.8263; 직전 완료 봉 목표를 다음 봉 시가에 모의 적용 |
| v2 | mfi_14_recovery | 9930.25 | -69.75 | sell / filled / 직전 MFI14 < 20, 현재 MFI14 >= 20 (한 봉 목표); 조건 미충족; MFI14=34.131, previous_MFI14=22.0435; 직전 완료 봉 목표를 다음 봉 시가에 모의 적용 |
| v2 | adx_14_trend | 9791.20 | -208.80 | buy / partial / Wilder ADX14 >= 25 그리고 +DI14 > -DI14; 조건 충족; ADX14=26.5262, plus_DI14=49.1478, minus_DI14=9.69634; 직전 완료 봉 목표를 다음 봉 시가에 모의 적용 |
| v2 | aroon_25_trend | 9826.26 | -173.74 | sell / filled / Aroon25 Up > 70 그리고 Down < 30 (동률이면 최신 극값); 조건 미충족; Aroon_up=100, Aroon_down=68; 직전 완료 봉 목표를 다음 봉 시가에 모의 적용 |
| v2 | cci_20_momentum | 9980.70 | -19.30 | buy / partial / CCI20 > 100 (전형가격·평균절대편차); 조건 충족; CCI20=115.766; 직전 완료 봉 목표를 다음 봉 시가에 모의 적용 |
| v2 | williams_14_recovery | 9825.45 | -174.55 | sell / filled / 직전 Williams %R14 < -80, 현재 >= -80 (한 봉 목표); 조건 미충족; Williams_R14=-27.273, previous_R14=-65.9097; 직전 완료 봉 목표를 다음 봉 시가에 모의 적용 |
| v2 | cmf_20_accumulation | 9804.76 | -195.24 | buy / partial / Chaikin Money Flow20 > 0.1; 조건 충족; CMF20=0.208851, volume20=1.40263e+07; 직전 완료 봉 목표를 다음 봉 시가에 모의 적용 |
| v2 | chaikin_3_10 | 9856.99 | -143.01 | buy / partial / ADL의 EMA3 - EMA10 > 0 그리고 종가 > EMA26; 조건 충족; Chaikin3_10=878293, ADL=-4.92877e+07, close=272.6, EMA26=271.529; 직전 완료 봉 목표를 다음 봉 시가에 모의 적용 |
| v2 | roc_10_momentum | 10043.24 | 43.24 | buy / partial / 10봉 ROC > 1% 그리고 종가 > EMA26; 조건 충족; ROC10_percent=1.11505, close=274.305, EMA26=271.734; 직전 완료 봉 목표를 다음 봉 시가에 모의 적용 |
| v2 | trix_15_trend | 9948.86 | -51.14 | buy / partial / 15봉 삼중 EMA의 1봉 변화율 TRIX > 0 그리고 종가 > EMA26; 조건 충족; TRIX15_percent=0.00296855, close=273.97, EMA26=271.9; 직전 완료 봉 목표를 다음 봉 시가에 모의 적용 |
| v2 | keltner_20_breakout | 9978.28 | -21.72 | buy / partial / 종가 > EMA20 + 2 x Wilder ATR14; 조건 충족; close=274.305, upper_Keltner=273.059, EMA20=271.774, ATR14=0.64209; 직전 완료 봉 목표를 다음 봉 시가에 모의 적용 |
| v2 | opening_range_30m | 9953.26 | -46.74 | buy / partial / 뉴욕 09:30·09:45 두 완료 봉 최고가를 10:00 이후 종가가 돌파; 조건 충족; close=275.845, opening_high=274.33; 직전 완료 봉 목표를 다음 봉 시가에 모의 적용 |

### 같은 기간의 비용·노출 비교 (사후 연구)

| 전략 | 비용 전 | 비용 후 | 100% 보유 | 같은 평균 노출 보유 | 평균 노출 |
|---|---:|---:|---:|---:|---:|
| cash | 0.00% | 0.00% | -1.17% | -0.00% | 0.00% |
| buy_hold | -0.76% | -1.17% | -1.17% | -1.17% | 100.00% |
| trend_8_26 | -0.72% | -4.40% | -1.17% | -0.54% | 45.91% |
| momentum_26 | -0.61% | -6.29% | -1.17% | -0.51% | 43.54% |
| breakout_8 | -0.12% | -14.50% | -1.17% | -0.25% | 21.37% |
| reversion_12 | -2.15% | -13.73% | -1.17% | -0.33% | 27.97% |
| volume_26 | -1.61% | -8.78% | -1.17% | -0.10% | 8.71% |
| trend_8_26 AND momentum_26 | -0.64% | -5.12% | -1.17% | -0.43% | 36.68% |
| trend_8_26 + momentum_26 | -0.66% | -4.95% | -1.17% | -0.53% | 44.73% |
| trend_8_26 AND breakout_8 | -0.53% | -8.92% | -1.17% | -0.15% | 12.66% |
| trend_8_26 + breakout_8 | -0.41% | -9.40% | -1.17% | -0.40% | 33.65% |
| trend_8_26 AND reversion_12 | -0.74% | -4.82% | -1.17% | -0.07% | 5.54% |
| trend_8_26 + reversion_12 | -1.42% | -9.00% | -1.17% | -0.43% | 36.94% |
| trend_8_26 AND volume_26 | -0.98% | -3.85% | -1.17% | -0.03% | 2.64% |
| trend_8_26 + volume_26 | -1.15% | -6.22% | -1.17% | -0.32% | 27.31% |
| momentum_26 AND breakout_8 | 0.22% | -8.24% | -1.17% | -0.14% | 11.87% |
| momentum_26 + breakout_8 | -0.37% | -10.30% | -1.17% | -0.38% | 32.46% |
| momentum_26 AND reversion_12 | 0.03% | -3.68% | -1.17% | -0.04% | 3.69% |
| momentum_26 + reversion_12 | -1.38% | -9.15% | -1.17% | -0.42% | 35.76% |
| momentum_26 AND volume_26 | 0.06% | -2.02% | -1.17% | -0.02% | 1.85% |
| momentum_26 + volume_26 | -1.11% | -7.16% | -1.17% | -0.31% | 26.12% |
| breakout_8 AND reversion_12 | 0.00% | 0.00% | -1.17% | -0.00% | 0.00% |
| breakout_8 + reversion_12 | -1.13% | -13.58% | -1.17% | -0.29% | 24.68% |
| breakout_8 AND volume_26 | -0.84% | -4.11% | -1.17% | -0.03% | 2.64% |
| breakout_8 + volume_26 | -0.87% | -11.32% | -1.17% | -0.18% | 15.05% |
| reversion_12 AND volume_26 | -0.62% | -4.31% | -1.17% | -0.05% | 3.96% |
| reversion_12 + volume_26 | -1.87% | -10.73% | -1.17% | -0.22% | 18.34% |
| ema_12_26 | 1.04% | -1.88% | -1.17% | -0.53% | 45.38% |
| macd_12_26_9 | 2.83% | -0.15% | -1.17% | -0.35% | 30.08% |
| rsi_14_recovery | -0.65% | -5.14% | -1.17% | -0.03% | 2.90% |
| bollinger_20_reentry | -0.24% | -4.35% | -1.17% | -0.03% | 2.64% |
| donchian_20 | -0.34% | -6.04% | -1.17% | -0.08% | 6.60% |
| atr_14_breakout | -0.52% | -7.37% | -1.17% | -0.06% | 4.75% |
| session_vwap | 0.36% | -9.64% | -1.17% | -0.50% | 42.22% |
| obv_20 | 1.52% | -3.07% | -1.17% | -0.48% | 40.63% |
| stochastic_14_3_recovery | -0.44% | -12.96% | -1.17% | -0.10% | 8.44% |
| mfi_14_recovery | 0.36% | -4.17% | -1.17% | -0.03% | 2.90% |
| adx_14_trend | -0.25% | -3.95% | -1.17% | -0.38% | 31.93% |
| aroon_25_trend | -1.21% | -5.28% | -1.17% | -0.25% | 21.64% |
| cci_20_momentum | -0.79% | -7.62% | -1.17% | -0.24% | 20.58% |
| williams_14_recovery | -0.09% | -9.29% | -1.17% | -0.07% | 6.07% |
| cmf_20_accumulation | -0.63% | -7.87% | -1.17% | -0.24% | 20.32% |
| chaikin_3_10 | -0.62% | -7.47% | -1.17% | -0.39% | 33.51% |
| roc_10_momentum | 0.01% | -1.66% | -1.17% | -0.06% | 5.01% |
| trix_15_trend | 1.12% | -2.22% | -1.17% | -0.39% | 32.98% |
| keltner_20_breakout | -0.27% | -3.97% | -1.17% | -0.08% | 7.12% |
| opening_range_30m | 2.65% | -1.57% | -1.17% | -0.27% | 22.69% |

동일 구간·초기 자금, 종료 시 청산 비용 포함. 노출 맞춤은 사후 설명용이며 v2 실제 계좌 성과가 아닙니다.
[낙폭 분해·비용 영향·전체 구간](IWM/comparison.json)

[v1 전체 기록](IWM/accounts.json) · [v2 전체 기록](IWM/accounts-v2.json)

## DIA 계좌

| 모델 | 전략 | 평가액 USD | 손익 USD | 최근 매매·이유 |
|---|---|---:|---:|---|
| v1 | cash | 10000.00 | 0.00 | 대기 /  / 새 신호 대기 |
| v1 | buy_hold | 10003.13 | 3.13 | buy /  / buy_hold: prior completed bar target 100%; next bar open simulation |
| v1 | trend_8_26 | 9961.47 | -38.53 | buy /  / trend_8_26: prior completed bar target 100%; next bar open simulation |
| v1 | momentum_26 | 9857.64 | -142.36 | buy /  / momentum_26: prior completed bar target 100%; next bar open simulation |
| v1 | breakout_8 | 9693.16 | -306.84 | sell /  / breakout_8: prior completed bar target 0%; next bar open simulation |
| v1 | reversion_12 | 9897.27 | -102.73 | sell /  / reversion_12: prior completed bar target 0%; next bar open simulation |
| v1 | volume_26 | 9939.83 | -60.17 | sell /  / volume_26: prior completed bar target 0%; next bar open simulation |
| v1 | trend_8_26 AND momentum_26 | 9857.64 | -142.36 | buy /  / trend_8_26 AND momentum_26: prior completed bar target 100%; next bar open simulation |
| v1 | trend_8_26 + momentum_26 | 9909.51 | -90.49 | buy /  / trend_8_26 + momentum_26: prior completed bar target 100%; next bar open simulation |
| v1 | trend_8_26 AND breakout_8 | 9825.30 | -174.70 | sell /  / trend_8_26 AND breakout_8: prior completed bar target 0%; next bar open simulation |
| v1 | trend_8_26 + breakout_8 | 9846.11 | -153.89 | sell /  / trend_8_26 + breakout_8: prior completed bar target 50%; next bar open simulation |
| v1 | trend_8_26 AND reversion_12 | 9940.76 | -59.24 | sell /  / trend_8_26 AND reversion_12: prior completed bar target 0%; next bar open simulation |
| v1 | trend_8_26 + reversion_12 | 9929.19 | -70.81 | sell /  / trend_8_26 + reversion_12: prior completed bar target 50%; next bar open simulation |
| v1 | trend_8_26 AND volume_26 | 9974.09 | -25.91 | sell /  / trend_8_26 AND volume_26: prior completed bar target 0%; next bar open simulation |
| v1 | trend_8_26 + volume_26 | 9950.55 | -49.45 | sell /  / trend_8_26 + volume_26: prior completed bar target 50%; next bar open simulation |
| v1 | momentum_26 AND breakout_8 | 9825.30 | -174.70 | sell /  / momentum_26 AND breakout_8: prior completed bar target 0%; next bar open simulation |
| v1 | momentum_26 + breakout_8 | 9775.06 | -224.94 | sell /  / momentum_26 + breakout_8: prior completed bar target 50%; next bar open simulation |
| v1 | momentum_26 AND reversion_12 | 9940.78 | -59.22 | sell /  / momentum_26 AND reversion_12: prior completed bar target 0%; next bar open simulation |
| v1 | momentum_26 + reversion_12 | 9916.87 | -83.13 | sell /  / momentum_26 + reversion_12: prior completed bar target 50%; next bar open simulation |
| v1 | momentum_26 AND volume_26 | 9929.52 | -70.48 | sell /  / momentum_26 AND volume_26: prior completed bar target 0%; next bar open simulation |
| v1 | momentum_26 + volume_26 | 9918.42 | -81.58 | sell /  / momentum_26 + volume_26: prior completed bar target 50%; next bar open simulation |
| v1 | breakout_8 AND reversion_12 | 10000.00 | 0.00 | 대기 /  / 새 신호 대기 |
| v1 | breakout_8 + reversion_12 | 9814.18 | -185.82 | sell /  / breakout_8 + reversion_12: prior completed bar target 0%; next bar open simulation |
| v1 | breakout_8 AND volume_26 | 9986.25 | -13.75 | sell /  / breakout_8 AND volume_26: prior completed bar target 0%; next bar open simulation |
| v1 | breakout_8 + volume_26 | 9855.04 | -144.96 | sell /  / breakout_8 + volume_26: prior completed bar target 0%; next bar open simulation |
| v1 | reversion_12 AND volume_26 | 9970.42 | -29.58 | sell /  / reversion_12 AND volume_26: prior completed bar target 0%; next bar open simulation |
| v1 | reversion_12 + volume_26 | 9938.32 | -61.68 | sell /  / reversion_12 + volume_26: prior completed bar target 0%; next bar open simulation |
| v1 | ema_12_26 | 9857.87 | -142.13 | buy /  / EMA12 > EMA26; 조건 충족; EMA12=519.74, EMA26=519.585 |
| v1 | macd_12_26_9 | 9923.32 | -76.68 | buy /  / MACD > 신호선 그리고 MACD > 0; 조건 충족; MACD=0.154226, signal9=0.0227958 |
| v1 | rsi_14_recovery | 10000.00 | 0.00 | 대기 /  / 새 신호 대기 |
| v1 | bollinger_20_reentry | 9978.51 | -21.49 | sell /  / 직전 종가 < 직전 하단밴드, 현재 하단밴드 <= 종가 <= SMA20 (한 봉 목표); 조건 미충족; close=519.823, lower20=518.355, SMA20=521.612, previous_lower20=518.548 |
| v1 | donchian_20 | 9822.00 | -178.00 | sell /  / 종가 > 현재 봉을 제외한 직전 20봉 최고가; 조건 미충족; close=523.68, prior_high20=526.17 |
| v1 | atr_14_breakout | 9885.70 | -114.30 | sell /  / 종가 > 직전 종가 + 직전 ATR14 그리고 종가 > EMA26; 조건 미충족; close=525.49, threshold=525.841, prior_ATR14=0.980592, EMA26=520.815 |
| v1 | session_vwap | 9912.81 | -87.19 | buy /  / 종가 > 뉴욕 거래일별 누적 전형가격 VWAP; 조건 충족; close=521.46, session_VWAP=520.55, session_volume=446463 |
| v1 | obv_20 | 9864.14 | -135.86 | buy /  / OBV > OBV의 SMA20 그리고 종가 > EMA26; 조건 충족; OBV=-9.86891e+06, OBV_SMA20=-1.0028e+07, close=521.46, EMA26=519.585 |
| v1 | stochastic_14_3_recovery | 9821.00 | -179.00 | sell /  / 직전 %K14 < 20에서 %K14가 %D3 상향 돌파 (한 봉 목표); 조건 미충족; K14=100, D3=70.5235, previous_K14=91.7443, previous_D3=57.9113 |
| v1 | mfi_14_recovery | 9936.38 | -63.62 | sell /  / 직전 MFI14 < 20, 현재 MFI14 >= 20 (한 봉 목표); 조건 미충족; MFI14=44.8014, previous_MFI14=20.0271 |
| v1 | adx_14_trend | 9831.87 | -168.13 | buy /  / Wilder ADX14 >= 25 그리고 +DI14 > -DI14; 조건 충족; ADX14=25.1937, plus_DI14=46.4871, minus_DI14=10.1356 |
| v1 | aroon_25_trend | 9928.84 | -71.16 | sell /  / Aroon25 Up > 70 그리고 Down < 30 (동률이면 최신 극값); 조건 미충족; Aroon_up=100, Aroon_down=80 |
| v1 | cci_20_momentum | 9915.48 | -84.52 | sell /  / CCI20 > 100 (전형가격·평균절대편차); 조건 미충족; CCI20=87.8356 |
| v1 | williams_14_recovery | 9854.30 | -145.70 | sell /  / 직전 Williams %R14 < -80, 현재 >= -80 (한 봉 목표); 조건 미충족; Williams_R14=0, previous_R14=-8.25572 |
| v1 | cmf_20_accumulation | 9814.39 | -185.61 | buy /  / Chaikin Money Flow20 > 0.1; 조건 충족; CMF20=0.237356, volume20=1.61808e+06 |
| v1 | chaikin_3_10 | 9866.05 | -133.95 | buy /  / ADL의 EMA3 - EMA10 > 0 그리고 종가 > EMA26; 조건 충족; Chaikin3_10=78733.3, ADL=-1.64223e+07, close=521.46, EMA26=519.585 |
| v1 | roc_10_momentum | 9939.01 | -60.99 | sell /  / 10봉 ROC > 1% 그리고 종가 > EMA26; 조건 미충족; ROC10_percent=0.771645, close=523.68, EMA26=521.367 |
| v1 | trix_15_trend | 9959.37 | -40.63 | buy /  / 15봉 삼중 EMA의 1봉 변화율 TRIX > 0 그리고 종가 > EMA26; 조건 충족; TRIX15_percent=0.000473967, close=521.46, EMA26=519.585 |
| v1 | keltner_20_breakout | 9944.49 | -55.51 | sell /  / 종가 > EMA20 + 2 x Wilder ATR14; 조건 미충족; close=523.68, upper_Keltner=523.985, EMA20=521.785, ATR14=1.10038 |
| v1 | opening_range_30m | 9796.87 | -203.13 | buy /  / 뉴욕 09:30·09:45 두 완료 봉 최고가를 10:00 이후 종가가 돌파; 조건 충족; close=524.86, opening_high=523.47 |
| v2 | cash | 10000.00 | 0.00 | 대기 /  / 새 신호 대기 |
| v2 | buy_hold | 10127.05 | 127.05 | buy / partial / 직전 완료 봉 목표 비중 100%; 다음 봉 시가 가정 |
| v2 | trend_8_26 | 9894.95 | -105.05 | buy / partial / 직전 완료 봉 목표 비중 100%; 다음 봉 시가 가정 |
| v2 | momentum_26 | 9895.52 | -104.48 | buy / partial / 직전 완료 봉 목표 비중 100%; 다음 봉 시가 가정 |
| v2 | breakout_8 | 9220.36 | -779.64 | sell / filled / 직전 완료 봉 목표 비중 0%; 다음 봉 시가 가정 |
| v2 | reversion_12 | 9592.64 | -407.36 | sell / filled / 직전 완료 봉 목표 비중 0%; 다음 봉 시가 가정 |
| v2 | volume_26 | 9652.01 | -347.99 | sell / filled / 직전 완료 봉 목표 비중 0%; 다음 봉 시가 가정 |
| v2 | trend_8_26 AND momentum_26 | 9890.93 | -109.07 | buy / partial / 직전 완료 봉 목표 비중 100%; 다음 봉 시가 가정 |
| v2 | trend_8_26 + momentum_26 | 9895.40 | -104.60 | buy / partial / 직전 완료 봉 목표 비중 100%; 다음 봉 시가 가정 |
| v2 | trend_8_26 AND breakout_8 | 9509.90 | -490.10 | sell / filled / 직전 완료 봉 목표 비중 0%; 다음 봉 시가 가정 |
| v2 | trend_8_26 + breakout_8 | 9571.90 | -428.10 | sell / filled / 직전 완료 봉 목표 비중 50%; 다음 봉 시가 가정 |
| v2 | trend_8_26 AND reversion_12 | 9748.75 | -251.25 | sell / filled / 직전 완료 봉 목표 비중 0%; 다음 봉 시가 가정 |
| v2 | trend_8_26 + reversion_12 | 9742.25 | -257.75 | sell / filled / 직전 완료 봉 목표 비중 50%; 다음 봉 시가 가정 |
| v2 | trend_8_26 AND volume_26 | 9827.44 | -172.56 | sell / filled / 직전 완료 봉 목표 비중 0%; 다음 봉 시가 가정 |
| v2 | trend_8_26 + volume_26 | 9793.13 | -206.87 | sell / filled / 직전 완료 봉 목표 비중 50%; 다음 봉 시가 가정 |
| v2 | momentum_26 AND breakout_8 | 9499.07 | -500.93 | sell / filled / 직전 완료 봉 목표 비중 0%; 다음 봉 시가 가정 |
| v2 | momentum_26 + breakout_8 | 9552.11 | -447.89 | sell / filled / 직전 완료 봉 목표 비중 50%; 다음 봉 시가 가정 |
| v2 | momentum_26 AND reversion_12 | 9895.03 | -104.97 | sell / filled / 직전 완료 봉 목표 비중 0%; 다음 봉 시가 가정 |
| v2 | momentum_26 + reversion_12 | 9783.57 | -216.43 | sell / filled / 직전 완료 봉 목표 비중 50%; 다음 봉 시가 가정 |
| v2 | momentum_26 AND volume_26 | 9716.58 | -283.42 | sell / filled / 직전 완료 봉 목표 비중 0%; 다음 봉 시가 가정 |
| v2 | momentum_26 + volume_26 | 9834.80 | -165.20 | sell / filled / 직전 완료 봉 목표 비중 50%; 다음 봉 시가 가정 |
| v2 | breakout_8 AND reversion_12 | 10000.00 | 0.00 | 대기 /  / 새 신호 대기 |
| v2 | breakout_8 + reversion_12 | 9423.89 | -576.11 | sell / filled / 직전 완료 봉 목표 비중 0%; 다음 봉 시가 가정 |
| v2 | breakout_8 AND volume_26 | 9781.13 | -218.87 | sell / filled / 직전 완료 봉 목표 비중 0%; 다음 봉 시가 가정 |
| v2 | breakout_8 + volume_26 | 9473.24 | -526.76 | sell / filled / 직전 완료 봉 목표 비중 0%; 다음 봉 시가 가정 |
| v2 | reversion_12 AND volume_26 | 9966.44 | -33.56 | sell / filled / 직전 완료 봉 목표 비중 0%; 다음 봉 시가 가정 |
| v2 | reversion_12 + volume_26 | 9642.17 | -357.83 | sell / filled / 직전 완료 봉 목표 비중 0%; 다음 봉 시가 가정 |
| v2 | ema_12_26 | 9852.95 | -147.05 | buy / partial / EMA12 > EMA26; 조건 충족; EMA12=519.74, EMA26=519.585; 직전 완료 봉 목표를 다음 봉 시가에 모의 적용 |
| v2 | macd_12_26_9 | 9918.36 | -81.64 | buy / partial / MACD > 신호선 그리고 MACD > 0; 조건 충족; MACD=0.154226, signal9=0.0227958; 직전 완료 봉 목표를 다음 봉 시가에 모의 적용 |
| v2 | rsi_14_recovery | 10000.00 | 0.00 | 대기 /  / 새 신호 대기 |
| v2 | bollinger_20_reentry | 9976.52 | -23.48 | sell / filled / 직전 종가 < 직전 하단밴드, 현재 하단밴드 <= 종가 <= SMA20 (한 봉 목표); 조건 미충족; close=519.823, lower20=518.355, SMA20=521.612, previous_lower20=518.548; 직전 완료 봉 목표를 다음 봉 시가에 모의 적용 |
| v2 | donchian_20 | 9814.14 | -185.86 | sell / filled / 종가 > 현재 봉을 제외한 직전 20봉 최고가; 조건 미충족; close=523.68, prior_high20=526.17; 직전 완료 봉 목표를 다음 봉 시가에 모의 적용 |
| v2 | atr_14_breakout | 9877.79 | -122.21 | sell / filled / 종가 > 직전 종가 + 직전 ATR14 그리고 종가 > EMA26; 조건 미충족; close=525.49, threshold=525.841, prior_ATR14=0.980592, EMA26=520.815; 직전 완료 봉 목표를 다음 봉 시가에 모의 적용 |
| v2 | session_vwap | 9905.87 | -94.13 | buy / partial / 종가 > 뉴욕 거래일별 누적 전형가격 VWAP; 조건 충족; close=521.46, session_VWAP=520.55, session_volume=446463; 직전 완료 봉 목표를 다음 봉 시가에 모의 적용 |
| v2 | obv_20 | 9857.24 | -142.76 | buy / partial / OBV > OBV의 SMA20 그리고 종가 > EMA26; 조건 충족; OBV=-9.86891e+06, OBV_SMA20=-1.0028e+07, close=521.46, EMA26=519.585; 직전 완료 봉 목표를 다음 봉 시가에 모의 적용 |
| v2 | stochastic_14_3_recovery | 9811.19 | -188.81 | sell / filled / 직전 %K14 < 20에서 %K14가 %D3 상향 돌파 (한 봉 목표); 조건 미충족; K14=100, D3=70.5235, previous_K14=91.7443, previous_D3=57.9113; 직전 완료 봉 목표를 다음 봉 시가에 모의 적용 |
| v2 | mfi_14_recovery | 9932.40 | -67.60 | sell / filled / 직전 MFI14 < 20, 현재 MFI14 >= 20 (한 봉 목표); 조건 미충족; MFI14=44.8014, previous_MFI14=20.0271; 직전 완료 봉 목표를 다음 봉 시가에 모의 적용 |
| v2 | adx_14_trend | 9826.95 | -173.05 | buy / partial / Wilder ADX14 >= 25 그리고 +DI14 > -DI14; 조건 충족; ADX14=25.1937, plus_DI14=46.4871, minus_DI14=10.1356; 직전 완료 봉 목표를 다음 봉 시가에 모의 적용 |
| v2 | aroon_25_trend | 9922.89 | -77.11 | sell / filled / Aroon25 Up > 70 그리고 Down < 30 (동률이면 최신 극값); 조건 미충족; Aroon_up=100, Aroon_down=80; 직전 완료 봉 목표를 다음 봉 시가에 모의 적용 |
| v2 | cci_20_momentum | 9909.53 | -90.47 | sell / filled / CCI20 > 100 (전형가격·평균절대편차); 조건 미충족; CCI20=87.8356; 직전 완료 봉 목표를 다음 봉 시가에 모의 적용 |
| v2 | williams_14_recovery | 9846.42 | -153.58 | sell / filled / 직전 Williams %R14 < -80, 현재 >= -80 (한 봉 목표); 조건 미충족; Williams_R14=0, previous_R14=-8.25572; 직전 완료 봉 목표를 다음 봉 시가에 모의 적용 |
| v2 | cmf_20_accumulation | 9805.56 | -194.44 | buy / partial / Chaikin Money Flow20 > 0.1; 조건 충족; CMF20=0.237356, volume20=1.61808e+06; 직전 완료 봉 목표를 다음 봉 시가에 모의 적용 |
| v2 | chaikin_3_10 | 9859.15 | -140.85 | buy / partial / ADL의 EMA3 - EMA10 > 0 그리고 종가 > EMA26; 조건 충족; Chaikin3_10=78733.3, ADL=-1.64223e+07, close=521.46, EMA26=519.585; 직전 완료 봉 목표를 다음 봉 시가에 모의 적용 |
| v2 | roc_10_momentum | 9937.03 | -62.97 | sell / filled / 10봉 ROC > 1% 그리고 종가 > EMA26; 조건 미충족; ROC10_percent=0.771645, close=523.68, EMA26=521.367; 직전 완료 봉 목표를 다음 봉 시가에 모의 적용 |
| v2 | trix_15_trend | 9956.38 | -43.62 | buy / partial / 15봉 삼중 EMA의 1봉 변화율 TRIX > 0 그리고 종가 > EMA26; 조건 충족; TRIX15_percent=0.000473967, close=521.46, EMA26=519.585; 직전 완료 봉 목표를 다음 봉 시가에 모의 적용 |
| v2 | keltner_20_breakout | 9940.51 | -59.49 | sell / filled / 종가 > EMA20 + 2 x Wilder ATR14; 조건 미충족; close=523.68, upper_Keltner=523.985, EMA20=521.785, ATR14=1.10038; 직전 완료 봉 목표를 다음 봉 시가에 모의 적용 |
| v2 | opening_range_30m | 9788.06 | -211.94 | buy / partial / 뉴욕 09:30·09:45 두 완료 봉 최고가를 10:00 이후 종가가 돌파; 조건 충족; close=524.86, opening_high=523.47; 직전 완료 봉 목표를 다음 봉 시가에 모의 적용 |

### 같은 기간의 비용·노출 비교 (사후 연구)

| 전략 | 비용 전 | 비용 후 | 100% 보유 | 같은 평균 노출 보유 | 평균 노출 |
|---|---:|---:|---:|---:|---:|
| cash | 0.00% | 0.00% | 1.94% | 0.00% | 0.00% |
| buy_hold | 2.37% | 1.94% | 1.94% | 1.94% | 100.00% |
| trend_8_26 | 2.22% | -1.57% | 1.94% | 1.18% | 60.69% |
| momentum_26 | 0.78% | -3.77% | 1.94% | 1.07% | 55.15% |
| breakout_8 | 0.87% | -16.85% | 1.94% | 0.47% | 24.27% |
| reversion_12 | -0.58% | -8.59% | 1.94% | 0.43% | 22.43% |
| volume_26 | 0.22% | -9.77% | 1.94% | 0.21% | 11.08% |
| trend_8_26 AND momentum_26 | 1.90% | -2.70% | 1.94% | 0.97% | 49.87% |
| trend_8_26 + momentum_26 | 1.51% | -2.67% | 1.94% | 1.12% | 57.92% |
| trend_8_26 AND breakout_8 | 1.09% | -11.62% | 1.94% | 0.32% | 16.36% |
| trend_8_26 + breakout_8 | 1.55% | -9.15% | 1.94% | 0.82% | 42.49% |
| trend_8_26 AND reversion_12 | 0.43% | -4.91% | 1.94% | 0.13% | 6.86% |
| trend_8_26 + reversion_12 | 0.82% | -4.95% | 1.94% | 0.80% | 41.56% |
| trend_8_26 AND volume_26 | 1.48% | -4.32% | 1.94% | 0.12% | 6.07% |
| trend_8_26 + volume_26 | 1.22% | -5.57% | 1.94% | 0.69% | 35.89% |
| momentum_26 AND breakout_8 | 0.30% | -11.95% | 1.94% | 0.32% | 16.62% |
| momentum_26 + breakout_8 | 0.83% | -10.36% | 1.94% | 0.77% | 39.72% |
| momentum_26 AND reversion_12 | -0.27% | -3.57% | 1.94% | 0.11% | 5.80% |
| momentum_26 + reversion_12 | 0.11% | -5.22% | 1.94% | 0.75% | 38.79% |
| momentum_26 AND volume_26 | 0.10% | -5.62% | 1.94% | 0.11% | 5.54% |
| momentum_26 + volume_26 | 0.51% | -6.03% | 1.94% | 0.64% | 33.12% |
| breakout_8 AND reversion_12 | 0.00% | 0.00% | 1.94% | 0.00% | 0.00% |
| breakout_8 + reversion_12 | 0.15% | -12.46% | 1.94% | 0.45% | 23.36% |
| breakout_8 AND volume_26 | -0.47% | -3.75% | 1.94% | 0.06% | 3.17% |
| breakout_8 + volume_26 | 0.55% | -12.29% | 1.94% | 0.34% | 17.69% |
| reversion_12 AND volume_26 | 0.29% | -4.24% | 1.94% | 0.07% | 3.43% |
| reversion_12 + volume_26 | -0.18% | -9.00% | 1.94% | 0.32% | 16.76% |
| ema_12_26 | 0.58% | -2.33% | 1.94% | 1.02% | 52.51% |
| macd_12_26_9 | 2.07% | -1.72% | 1.94% | 0.60% | 31.13% |
| rsi_14_recovery | 0.16% | -1.09% | 1.94% | 0.02% | 0.79% |
| bollinger_20_reentry | 0.11% | -4.01% | 1.94% | 0.05% | 2.64% |
| donchian_20 | 0.36% | -6.94% | 1.94% | 0.19% | 9.76% |
| atr_14_breakout | -0.27% | -7.92% | 1.94% | 0.12% | 6.07% |
| session_vwap | 2.70% | -5.18% | 1.94% | 1.02% | 52.77% |
| obv_20 | 1.10% | -7.04% | 1.94% | 0.88% | 45.65% |
| stochastic_14_3_recovery | 0.95% | -11.00% | 1.94% | 0.15% | 7.92% |
| mfi_14_recovery | 0.16% | -3.15% | 1.94% | 0.04% | 2.11% |
| adx_14_trend | -0.12% | -4.23% | 1.94% | 0.65% | 33.51% |
| aroon_25_trend | 1.36% | -2.40% | 1.94% | 0.52% | 26.91% |
| cci_20_momentum | 1.07% | -5.50% | 1.94% | 0.52% | 26.91% |
| williams_14_recovery | 1.54% | -6.25% | 1.94% | 0.10% | 5.01% |
| cmf_20_accumulation | 1.52% | -6.27% | 1.94% | 0.57% | 29.55% |
| chaikin_3_10 | 2.32% | -7.11% | 1.94% | 0.87% | 45.12% |
| roc_10_momentum | -0.07% | -0.90% | 1.94% | 0.04% | 2.11% |
| trix_15_trend | 0.71% | -3.03% | 1.94% | 0.86% | 44.33% |
| keltner_20_breakout | 0.78% | -5.77% | 1.94% | 0.36% | 18.47% |
| opening_range_30m | 1.60% | -4.20% | 1.94% | 0.50% | 25.59% |

동일 구간·초기 자금, 종료 시 청산 비용 포함. 노출 맞춤은 사후 설명용이며 v2 실제 계좌 성과가 아닙니다.
[낙폭 분해·비용 영향·전체 구간](DIA/comparison.json)

[v1 전체 기록](DIA/accounts.json) · [v2 전체 기록](DIA/accounts-v2.json)

## MSFT 계좌

| 모델 | 전략 | 평가액 USD | 손익 USD | 최근 매매·이유 |
|---|---|---:|---:|---|
| v1 | cash | 10000.00 | 0.00 | 대기 /  / 새 신호 대기 |
| v1 | buy_hold | 9803.69 | -196.31 | buy /  / buy_hold: prior completed bar target 100%; next bar open simulation |
| v1 | trend_8_26 | 9677.44 | -322.56 | sell /  / trend_8_26: prior completed bar target 0%; next bar open simulation |
| v1 | momentum_26 | 9648.89 | -351.11 | sell /  / momentum_26: prior completed bar target 0%; next bar open simulation |
| v1 | breakout_8 | 9791.98 | -208.02 | sell /  / breakout_8: prior completed bar target 0%; next bar open simulation |
| v1 | reversion_12 | 9685.33 | -314.67 | sell /  / reversion_12: prior completed bar target 0%; next bar open simulation |
| v1 | volume_26 | 9811.31 | -188.69 | sell /  / volume_26: prior completed bar target 0%; next bar open simulation |
| v1 | trend_8_26 AND momentum_26 | 9662.97 | -337.03 | sell /  / trend_8_26 AND momentum_26: prior completed bar target 0%; next bar open simulation |
| v1 | trend_8_26 + momentum_26 | 9663.17 | -336.83 | sell /  / trend_8_26 + momentum_26: prior completed bar target 0%; next bar open simulation |
| v1 | trend_8_26 AND breakout_8 | 9820.11 | -179.89 | sell /  / trend_8_26 AND breakout_8: prior completed bar target 0%; next bar open simulation |
| v1 | trend_8_26 + breakout_8 | 9754.35 | -245.65 | sell /  / trend_8_26 + breakout_8: prior completed bar target 0%; next bar open simulation |
| v1 | trend_8_26 AND reversion_12 | 9721.64 | -278.36 | sell /  / trend_8_26 AND reversion_12: prior completed bar target 0%; next bar open simulation |
| v1 | trend_8_26 + reversion_12 | 9681.35 | -318.65 | sell /  / trend_8_26 + reversion_12: prior completed bar target 0%; next bar open simulation |
| v1 | trend_8_26 AND volume_26 | 9916.79 | -83.21 | sell /  / trend_8_26 AND volume_26: prior completed bar target 0%; next bar open simulation |
| v1 | trend_8_26 + volume_26 | 9744.38 | -255.62 | sell /  / trend_8_26 + volume_26: prior completed bar target 0%; next bar open simulation |
| v1 | momentum_26 AND breakout_8 | 9820.11 | -179.89 | sell /  / momentum_26 AND breakout_8: prior completed bar target 0%; next bar open simulation |
| v1 | momentum_26 + breakout_8 | 9720.48 | -279.52 | sell /  / momentum_26 + breakout_8: prior completed bar target 0%; next bar open simulation |
| v1 | momentum_26 AND reversion_12 | 9707.47 | -292.53 | sell /  / momentum_26 AND reversion_12: prior completed bar target 0%; next bar open simulation |
| v1 | momentum_26 + reversion_12 | 9667.06 | -332.94 | sell /  / momentum_26 + reversion_12: prior completed bar target 0%; next bar open simulation |
| v1 | momentum_26 AND volume_26 | 9916.79 | -83.21 | sell /  / momentum_26 AND volume_26: prior completed bar target 0%; next bar open simulation |
| v1 | momentum_26 + volume_26 | 9730.00 | -270.00 | sell /  / momentum_26 + volume_26: prior completed bar target 0%; next bar open simulation |
| v1 | breakout_8 AND reversion_12 | 10000.00 | 0.00 | 대기 /  / 새 신호 대기 |
| v1 | breakout_8 + reversion_12 | 9757.97 | -242.03 | sell /  / breakout_8 + reversion_12: prior completed bar target 0%; next bar open simulation |
| v1 | breakout_8 AND volume_26 | 9953.19 | -46.81 | sell /  / breakout_8 AND volume_26: prior completed bar target 0%; next bar open simulation |
| v1 | breakout_8 + volume_26 | 9821.17 | -178.83 | sell /  / breakout_8 + volume_26: prior completed bar target 0%; next bar open simulation |
| v1 | reversion_12 AND volume_26 | 9938.00 | -62.00 | sell /  / reversion_12 AND volume_26: prior completed bar target 0%; next bar open simulation |
| v1 | reversion_12 + volume_26 | 9748.10 | -251.90 | sell /  / reversion_12 + volume_26: prior completed bar target 0%; next bar open simulation |
| v1 | ema_12_26 | 9662.97 | -337.03 | sell /  / EMA12 > EMA26; 조건 미충족; EMA12=532.823, EMA26=532.897 |
| v1 | macd_12_26_9 | 9837.76 | -162.24 | sell /  / MACD > 신호선 그리고 MACD > 0; 조건 미충족; MACD=0.667719, signal9=0.675659 |
| v1 | rsi_14_recovery | 9957.14 | -42.86 | sell /  / 직전 RSI14 < 30, 현재 RSI14 >= 30 (한 봉 목표); 조건 미충족; RSI14=45.5102, previous_RSI14=37.5844 |
| v1 | bollinger_20_reentry | 9854.81 | -145.19 | sell /  / 직전 종가 < 직전 하단밴드, 현재 하단밴드 <= 종가 <= SMA20 (한 봉 목표); 조건 미충족; close=531.675, lower20=529.239, SMA20=533.058, previous_lower20=529.387 |
| v1 | donchian_20 | 9912.16 | -87.84 | sell /  / 종가 > 현재 봉을 제외한 직전 20봉 최고가; 조건 미충족; close=534.52, prior_high20=535.44 |
| v1 | atr_14_breakout | 9915.10 | -84.90 | sell /  / 종가 > 직전 종가 + 직전 ATR14 그리고 종가 > EMA26; 조건 미충족; close=533.975, threshold=536.307, prior_ATR14=2.16203, EMA26=530.521 |
| v1 | session_vwap | 9870.62 | -129.38 | buy /  / 종가 > 뉴욕 거래일별 누적 전형가격 VWAP; 조건 충족; close=529.315, session_VWAP=528.789, session_volume=2.32763e+06 |
| v1 | obv_20 | 9767.68 | -232.32 | sell /  / OBV > OBV의 SMA20 그리고 종가 > EMA26; 조건 미충족; OBV=9.27348e+07, OBV_SMA20=9.29669e+07, close=533.95, EMA26=532.788 |
| v1 | stochastic_14_3_recovery | 9789.03 | -210.97 | sell /  / 직전 %K14 < 20에서 %K14가 %D3 상향 돌파 (한 봉 목표); 조건 미충족; K14=60.6262, D3=34.5689, previous_K14=38.87, previous_D3=26.948 |
| v1 | mfi_14_recovery | 9972.58 | -27.42 | sell /  / 직전 MFI14 < 20, 현재 MFI14 >= 20 (한 봉 목표); 조건 미충족; MFI14=53.413, previous_MFI14=44.3372 |
| v1 | adx_14_trend | 9883.62 | -116.38 | sell /  / Wilder ADX14 >= 25 그리고 +DI14 > -DI14; 조건 미충족; ADX14=23.6824, plus_DI14=22.3066, minus_DI14=19.9214 |
| v1 | aroon_25_trend | 9812.47 | -187.53 | sell /  / Aroon25 Up > 70 그리고 Down < 30 (동률이면 최신 극값); 조건 미충족; Aroon_up=68, Aroon_down=20 |
| v1 | cci_20_momentum | 10012.15 | 12.15 | sell /  / CCI20 > 100 (전형가격·평균절대편차); 조건 미충족; CCI20=86.441 |
| v1 | williams_14_recovery | 9819.22 | -180.78 | sell /  / 직전 Williams %R14 < -80, 현재 >= -80 (한 봉 목표); 조건 미충족; Williams_R14=-39.3738, previous_R14=-61.13 |
| v1 | cmf_20_accumulation | 9741.38 | -258.62 | sell /  / Chaikin Money Flow20 > 0.1; 조건 미충족; CMF20=0.0660116, volume20=2.44678e+07 |
| v1 | chaikin_3_10 | 9803.05 | -196.95 | sell /  / ADL의 EMA3 - EMA10 > 0 그리고 종가 > EMA26; 조건 미충족; Chaikin3_10=-652.264, ADL=1.10471e+08, close=534.345, EMA26=533.377 |
| v1 | roc_10_momentum | 9959.43 | -40.57 | sell /  / 10봉 ROC > 1% 그리고 종가 > EMA26; 조건 미충족; ROC10_percent=0.454191, close=534.125, EMA26=532.186 |
| v1 | trix_15_trend | 9712.42 | -287.58 | sell /  / 15봉 삼중 EMA의 1봉 변화율 TRIX > 0 그리고 종가 > EMA26; 조건 미충족; TRIX15_percent=0.0172213, close=526.676, EMA26=532.897 |
| v1 | keltner_20_breakout | 9958.78 | -41.22 | sell /  / 종가 > EMA20 + 2 x Wilder ATR14; 조건 미충족; close=533.975, upper_Keltner=534.357, EMA20=530.111, ATR14=2.12332 |
| v1 | opening_range_30m | 9711.79 | -288.21 | sell /  / 뉴욕 09:30·09:45 두 완료 봉 최고가를 10:00 이후 종가가 돌파; 자료 부족·변동폭 또는 거래량 없음: 대기; close=526.676 |
| v2 | cash | 10000.00 | 0.00 | 대기 /  / 새 신호 대기 |
| v2 | buy_hold | 9857.19 | -142.81 | buy / partial / 직전 완료 봉 목표 비중 100%; 다음 봉 시가 가정 |
| v2 | trend_8_26 | 9613.14 | -386.86 | sell / filled / 직전 완료 봉 목표 비중 0%; 다음 봉 시가 가정 |
| v2 | momentum_26 | 9692.90 | -307.10 | sell / filled / 직전 완료 봉 목표 비중 0%; 다음 봉 시가 가정 |
| v2 | breakout_8 | 9584.12 | -415.88 | sell / filled / 직전 완료 봉 목표 비중 0%; 다음 봉 시가 가정 |
| v2 | reversion_12 | 9308.50 | -691.50 | sell / filled / 직전 완료 봉 목표 비중 0%; 다음 봉 시가 가정 |
| v2 | volume_26 | 9498.13 | -501.87 | sell / filled / 직전 완료 봉 목표 비중 0%; 다음 봉 시가 가정 |
| v2 | trend_8_26 AND momentum_26 | 9560.49 | -439.51 | sell / filled / 직전 완료 봉 목표 비중 0%; 다음 봉 시가 가정 |
| v2 | trend_8_26 + momentum_26 | 9653.21 | -346.79 | sell / filled / 직전 완료 봉 목표 비중 0%; 다음 봉 시가 가정 |
| v2 | trend_8_26 AND breakout_8 | 9458.32 | -541.68 | sell / filled / 직전 완료 봉 목표 비중 0%; 다음 봉 시가 가정 |
| v2 | trend_8_26 + breakout_8 | 9639.54 | -360.46 | sell / filled / 직전 완료 봉 목표 비중 0%; 다음 봉 시가 가정 |
| v2 | trend_8_26 AND reversion_12 | 9618.75 | -381.25 | sell / filled / 직전 완료 봉 목표 비중 0%; 다음 봉 시가 가정 |
| v2 | trend_8_26 + reversion_12 | 9459.23 | -540.77 | sell / filled / 직전 완료 봉 목표 비중 0%; 다음 봉 시가 가정 |
| v2 | trend_8_26 AND volume_26 | 9861.94 | -138.06 | sell / filled / 직전 완료 봉 목표 비중 0%; 다음 봉 시가 가정 |
| v2 | trend_8_26 + volume_26 | 9575.59 | -424.41 | sell / filled / 직전 완료 봉 목표 비중 0%; 다음 봉 시가 가정 |
| v2 | momentum_26 AND breakout_8 | 9610.50 | -389.50 | sell / filled / 직전 완료 봉 목표 비중 0%; 다음 봉 시가 가정 |
| v2 | momentum_26 + breakout_8 | 9638.74 | -361.26 | sell / filled / 직전 완료 봉 목표 비중 0%; 다음 봉 시가 가정 |
| v2 | momentum_26 AND reversion_12 | 9533.70 | -466.30 | sell / filled / 직전 완료 봉 목표 비중 0%; 다음 봉 시가 가정 |
| v2 | momentum_26 + reversion_12 | 9498.52 | -501.48 | sell / filled / 직전 완료 봉 목표 비중 0%; 다음 봉 시가 가정 |
| v2 | momentum_26 AND volume_26 | 9785.21 | -214.79 | sell / filled / 직전 완료 봉 목표 비중 0%; 다음 봉 시가 가정 |
| v2 | momentum_26 + volume_26 | 9615.37 | -384.63 | sell / filled / 직전 완료 봉 목표 비중 0%; 다음 봉 시가 가정 |
| v2 | breakout_8 AND reversion_12 | 10000.00 | 0.00 | 대기 /  / 새 신호 대기 |
| v2 | breakout_8 + reversion_12 | 9484.80 | -515.20 | sell / filled / 직전 완료 봉 목표 비중 0%; 다음 봉 시가 가정 |
| v2 | breakout_8 AND volume_26 | 9890.09 | -109.91 | sell / filled / 직전 완료 봉 목표 비중 0%; 다음 봉 시가 가정 |
| v2 | breakout_8 + volume_26 | 9581.13 | -418.87 | sell / filled / 직전 완료 봉 목표 비중 0%; 다음 봉 시가 가정 |
| v2 | reversion_12 AND volume_26 | 9699.57 | -300.43 | sell / filled / 직전 완료 봉 목표 비중 0%; 다음 봉 시가 가정 |
| v2 | reversion_12 + volume_26 | 9402.66 | -597.34 | sell / filled / 직전 완료 봉 목표 비중 0%; 다음 봉 시가 가정 |
| v2 | ema_12_26 | 9659.11 | -340.89 | sell / filled / EMA12 > EMA26; 조건 미충족; EMA12=532.823, EMA26=532.897; 직전 완료 봉 목표를 다음 봉 시가에 모의 적용 |
| v2 | macd_12_26_9 | 9833.82 | -166.18 | sell / filled / MACD > 신호선 그리고 MACD > 0; 조건 미충족; MACD=0.667719, signal9=0.675659; 직전 완료 봉 목표를 다음 봉 시가에 모의 적용 |
| v2 | rsi_14_recovery | 9951.17 | -48.83 | sell / filled / 직전 RSI14 < 30, 현재 RSI14 >= 30 (한 봉 목표); 조건 미충족; RSI14=45.5102, previous_RSI14=37.5844; 직전 완료 봉 목표를 다음 봉 시가에 모의 적용 |
| v2 | bollinger_20_reentry | 9848.90 | -151.10 | sell / filled / 직전 종가 < 직전 하단밴드, 현재 하단밴드 <= 종가 <= SMA20 (한 봉 목표); 조건 미충족; close=531.675, lower20=529.239, SMA20=533.058, previous_lower20=529.387; 직전 완료 봉 목표를 다음 봉 시가에 모의 적용 |
| v2 | donchian_20 | 9908.19 | -91.81 | sell / filled / 종가 > 현재 봉을 제외한 직전 20봉 최고가; 조건 미충족; close=534.52, prior_high20=535.44; 직전 완료 봉 목표를 다음 봉 시가에 모의 적용 |
| v2 | atr_14_breakout | 9911.14 | -88.86 | sell / filled / 종가 > 직전 종가 + 직전 ATR14 그리고 종가 > EMA26; 조건 미충족; close=533.975, threshold=536.307, prior_ATR14=2.16203, EMA26=530.521; 직전 완료 봉 목표를 다음 봉 시가에 모의 적용 |
| v2 | session_vwap | 9863.71 | -136.29 | buy / partial / 종가 > 뉴욕 거래일별 누적 전형가격 VWAP; 조건 충족; close=529.315, session_VWAP=528.789, session_volume=2.32763e+06; 직전 완료 봉 목표를 다음 봉 시가에 모의 적용 |
| v2 | obv_20 | 9759.87 | -240.13 | sell / filled / OBV > OBV의 SMA20 그리고 종가 > EMA26; 조건 미충족; OBV=1.08325e+08, OBV_SMA20=1.08557e+08, close=533.95, EMA26=532.788; 직전 완료 봉 목표를 다음 봉 시가에 모의 적용 |
| v2 | stochastic_14_3_recovery | 9779.25 | -220.75 | sell / filled / 직전 %K14 < 20에서 %K14가 %D3 상향 돌파 (한 봉 목표); 조건 미충족; K14=60.6262, D3=34.5689, previous_K14=38.87, previous_D3=26.948; 직전 완료 봉 목표를 다음 봉 시가에 모의 적용 |
| v2 | mfi_14_recovery | 9968.59 | -31.41 | sell / filled / 직전 MFI14 < 20, 현재 MFI14 >= 20 (한 봉 목표); 조건 미충족; MFI14=53.413, previous_MFI14=44.3372; 직전 완료 봉 목표를 다음 봉 시가에 모의 적용 |
| v2 | adx_14_trend | 9879.67 | -120.33 | sell / filled / Wilder ADX14 >= 25 그리고 +DI14 > -DI14; 조건 미충족; ADX14=23.6824, plus_DI14=22.3066, minus_DI14=19.9214; 직전 완료 봉 목표를 다음 봉 시가에 모의 적용 |
| v2 | aroon_25_trend | 9808.55 | -191.45 | sell / filled / Aroon25 Up > 70 그리고 Down < 30 (동률이면 최신 극값); 조건 미충족; Aroon_up=68, Aroon_down=20; 직전 완료 봉 목표를 다음 봉 시가에 모의 적용 |
| v2 | cci_20_momentum | 10010.15 | 10.15 | sell / filled / CCI20 > 100 (전형가격·평균절대편차); 조건 미충족; CCI20=86.441; 직전 완료 봉 목표를 다음 봉 시가에 모의 적용 |
| v2 | williams_14_recovery | 9811.37 | -188.63 | sell / filled / 직전 Williams %R14 < -80, 현재 >= -80 (한 봉 목표); 조건 미충족; Williams_R14=-39.3738, previous_R14=-61.13; 직전 완료 봉 목표를 다음 봉 시가에 모의 적용 |
| v2 | cmf_20_accumulation | 9737.48 | -262.52 | sell / filled / Chaikin Money Flow20 > 0.1; 조건 미충족; CMF20=0.0660116, volume20=2.44678e+07; 직전 완료 봉 목표를 다음 봉 시가에 모의 적용 |
| v2 | chaikin_3_10 | 9797.17 | -202.83 | sell / filled / ADL의 EMA3 - EMA10 > 0 그리고 종가 > EMA26; 조건 미충족; Chaikin3_10=-652.264, ADL=1.11749e+08, close=534.345, EMA26=533.377; 직전 완료 봉 목표를 다음 봉 시가에 모의 적용 |
| v2 | roc_10_momentum | 9957.44 | -42.56 | sell / filled / 10봉 ROC > 1% 그리고 종가 > EMA26; 조건 미충족; ROC10_percent=0.454191, close=534.125, EMA26=532.186; 직전 완료 봉 목표를 다음 봉 시가에 모의 적용 |
| v2 | trix_15_trend | 9708.54 | -291.46 | sell / filled / 15봉 삼중 EMA의 1봉 변화율 TRIX > 0 그리고 종가 > EMA26; 조건 미충족; TRIX15_percent=0.0172213, close=526.676, EMA26=532.897; 직전 완료 봉 목표를 다음 봉 시가에 모의 적용 |
| v2 | keltner_20_breakout | 9956.78 | -43.22 | sell / filled / 종가 > EMA20 + 2 x Wilder ATR14; 조건 미충족; close=533.975, upper_Keltner=534.357, EMA20=530.111, ATR14=2.12332; 직전 완료 봉 목표를 다음 봉 시가에 모의 적용 |
| v2 | opening_range_30m | 9707.90 | -292.10 | sell / filled / 뉴욕 09:30·09:45 두 완료 봉 최고가를 10:00 이후 종가가 돌파; 자료 부족·변동폭 또는 거래량 없음: 대기; close=526.676; 직전 완료 봉 목표를 다음 봉 시가에 모의 적용 |

### 같은 기간의 비용·노출 비교 (사후 연구)

| 전략 | 비용 전 | 비용 후 | 100% 보유 | 같은 평균 노출 보유 | 평균 노출 |
|---|---:|---:|---:|---:|---:|
| cash | 0.00% | 0.00% | 4.39% | 0.00% | 0.00% |
| buy_hold | 4.83% | 4.39% | 4.39% | 4.39% | 100.00% |
| trend_8_26 | 1.11% | -2.23% | 4.39% | 2.60% | 60.16% |
| momentum_26 | 0.23% | -5.10% | 4.39% | 2.67% | 61.74% |
| breakout_8 | 6.22% | -8.69% | 4.39% | 0.87% | 20.58% |
| reversion_12 | -4.30% | -12.75% | 4.39% | 1.02% | 24.01% |
| volume_26 | 0.99% | -7.53% | 4.39% | 0.37% | 8.71% |
| trend_8_26 AND momentum_26 | -0.98% | -6.64% | 4.39% | 2.41% | 55.94% |
| trend_8_26 + momentum_26 | 0.67% | -3.66% | 4.39% | 2.63% | 60.95% |
| trend_8_26 AND breakout_8 | 0.46% | -10.69% | 4.39% | 0.58% | 13.72% |
| trend_8_26 + breakout_8 | 3.65% | -4.91% | 4.39% | 1.73% | 40.37% |
| trend_8_26 AND reversion_12 | -1.41% | -7.04% | 4.39% | 0.29% | 6.86% |
| trend_8_26 + reversion_12 | -1.62% | -7.45% | 4.39% | 1.80% | 42.09% |
| trend_8_26 AND volume_26 | 3.42% | -0.42% | 4.39% | 0.13% | 3.17% |
| trend_8_26 + volume_26 | 1.06% | -4.32% | 4.39% | 1.47% | 34.44% |
| momentum_26 AND breakout_8 | 2.74% | -8.66% | 4.39% | 0.58% | 13.72% |
| momentum_26 + breakout_8 | 3.19% | -6.32% | 4.39% | 1.76% | 41.17% |
| momentum_26 AND reversion_12 | -2.41% | -9.14% | 4.39% | 0.41% | 9.76% |
| momentum_26 + reversion_12 | -2.04% | -9.01% | 4.39% | 1.84% | 42.88% |
| momentum_26 AND volume_26 | 1.07% | -3.49% | 4.39% | 0.16% | 3.69% |
| momentum_26 + volume_26 | 0.63% | -5.33% | 4.39% | 1.50% | 35.23% |
| breakout_8 AND reversion_12 | 0.00% | 0.00% | 4.39% | 0.00% | 0.00% |
| breakout_8 + reversion_12 | 0.84% | -9.99% | 4.39% | 0.95% | 22.30% |
| breakout_8 AND volume_26 | 2.00% | -0.96% | 4.39% | 0.09% | 2.11% |
| breakout_8 + volume_26 | 3.58% | -7.14% | 4.39% | 0.62% | 14.65% |
| reversion_12 AND volume_26 | -2.90% | -6.11% | 4.39% | 0.14% | 3.43% |
| reversion_12 + volume_26 | -1.68% | -10.18% | 4.39% | 0.69% | 16.36% |
| ema_12_26 | 0.23% | -3.08% | 4.39% | 2.69% | 62.27% |
| macd_12_26_9 | 1.20% | -3.77% | 4.39% | 1.50% | 35.09% |
| rsi_14_recovery | 0.31% | -2.19% | 4.39% | 0.07% | 1.58% |
| bollinger_20_reentry | -0.92% | -3.79% | 4.39% | 0.08% | 1.85% |
| donchian_20 | 1.76% | -4.05% | 4.39% | 0.21% | 5.01% |
| atr_14_breakout | 1.79% | -4.02% | 4.39% | 0.17% | 3.96% |
| session_vwap | 7.03% | -1.18% | 4.39% | 1.77% | 41.42% |
| obv_20 | 5.57% | -2.52% | 4.39% | 2.12% | 49.34% |
| stochastic_14_3_recovery | -0.50% | -10.42% | 4.39% | 0.28% | 6.60% |
| mfi_14_recovery | 1.58% | -2.19% | 4.39% | 0.10% | 2.37% |
| adx_14_trend | 3.84% | 1.26% | 4.39% | 2.00% | 46.70% |
| aroon_25_trend | 0.07% | -4.85% | 4.39% | 0.97% | 22.96% |
| cci_20_momentum | 3.27% | -3.44% | 4.39% | 0.97% | 22.96% |
| williams_14_recovery | -1.26% | -9.97% | 4.39% | 0.24% | 5.80% |
| cmf_20_accumulation | 0.66% | -5.09% | 4.39% | 1.42% | 33.25% |
| chaikin_3_10 | 4.43% | -3.17% | 4.39% | 2.00% | 46.70% |
| roc_10_momentum | -0.01% | -4.12% | 4.39% | 0.67% | 15.83% |
| trix_15_trend | -0.85% | -4.93% | 4.39% | 2.15% | 50.13% |
| keltner_20_breakout | 1.11% | -4.26% | 4.39% | 0.58% | 13.72% |
| opening_range_30m | -1.04% | -4.71% | 4.39% | 1.01% | 23.75% |

동일 구간·초기 자금, 종료 시 청산 비용 포함. 노출 맞춤은 사후 설명용이며 v2 실제 계좌 성과가 아닙니다.
[낙폭 분해·비용 영향·전체 구간](MSFT/comparison.json)

[v1 전체 기록](MSFT/accounts.json) · [v2 전체 기록](MSFT/accounts-v2.json)

## JPM 계좌

| 모델 | 전략 | 평가액 USD | 손익 USD | 최근 매매·이유 |
|---|---|---:|---:|---|
| v1 | cash | 10000.00 | 0.00 | 대기 /  / 새 신호 대기 |
| v1 | buy_hold | 9889.60 | -110.40 | buy /  / buy_hold: prior completed bar target 100%; next bar open simulation |
| v1 | trend_8_26 | 9841.11 | -158.89 | buy /  / trend_8_26: prior completed bar target 100%; next bar open simulation |
| v1 | momentum_26 | 9760.91 | -239.09 | sell /  / momentum_26: prior completed bar target 0%; next bar open simulation |
| v1 | breakout_8 | 9759.46 | -240.54 | sell /  / breakout_8: prior completed bar target 0%; next bar open simulation |
| v1 | reversion_12 | 9763.34 | -236.66 | sell /  / reversion_12: prior completed bar target 0%; next bar open simulation |
| v1 | volume_26 | 9961.97 | -38.03 | sell /  / volume_26: prior completed bar target 0%; next bar open simulation |
| v1 | trend_8_26 AND momentum_26 | 9848.56 | -151.44 | sell /  / trend_8_26 AND momentum_26: prior completed bar target 0%; next bar open simulation |
| v1 | trend_8_26 + momentum_26 | 9800.94 | -199.06 | sell /  / trend_8_26 + momentum_26: prior completed bar target 50%; next bar open simulation |
| v1 | trend_8_26 AND breakout_8 | 9915.55 | -84.45 | sell /  / trend_8_26 AND breakout_8: prior completed bar target 0%; next bar open simulation |
| v1 | trend_8_26 + breakout_8 | 9819.86 | -180.14 | sell /  / trend_8_26 + breakout_8: prior completed bar target 50%; next bar open simulation |
| v1 | trend_8_26 AND reversion_12 | 9899.24 | -100.76 | sell /  / trend_8_26 AND reversion_12: prior completed bar target 0%; next bar open simulation |
| v1 | trend_8_26 + reversion_12 | 9802.07 | -197.93 | sell /  / trend_8_26 + reversion_12: prior completed bar target 50%; next bar open simulation |
| v1 | trend_8_26 AND volume_26 | 10035.68 | 35.68 | sell /  / trend_8_26 AND volume_26: prior completed bar target 0%; next bar open simulation |
| v1 | trend_8_26 + volume_26 | 9901.23 | -98.77 | sell /  / trend_8_26 + volume_26: prior completed bar target 50%; next bar open simulation |
| v1 | momentum_26 AND breakout_8 | 9733.77 | -266.23 | sell /  / momentum_26 AND breakout_8: prior completed bar target 0%; next bar open simulation |
| v1 | momentum_26 + breakout_8 | 9760.29 | -239.71 | sell /  / momentum_26 + breakout_8: prior completed bar target 0%; next bar open simulation |
| v1 | momentum_26 AND reversion_12 | 9881.87 | -118.13 | sell /  / momentum_26 AND reversion_12: prior completed bar target 0%; next bar open simulation |
| v1 | momentum_26 + reversion_12 | 9781.63 | -218.37 | sell /  / momentum_26 + reversion_12: prior completed bar target 0%; next bar open simulation |
| v1 | momentum_26 AND volume_26 | 10035.68 | 35.68 | sell /  / momentum_26 AND volume_26: prior completed bar target 0%; next bar open simulation |
| v1 | momentum_26 + volume_26 | 9880.61 | -119.39 | sell /  / momentum_26 + volume_26: prior completed bar target 0%; next bar open simulation |
| v1 | breakout_8 AND reversion_12 | 10000.00 | 0.00 | 대기 /  / 새 신호 대기 |
| v1 | breakout_8 + reversion_12 | 9800.45 | -199.55 | sell /  / breakout_8 + reversion_12: prior completed bar target 0%; next bar open simulation |
| v1 | breakout_8 AND volume_26 | 10022.00 | 22.00 | sell /  / breakout_8 AND volume_26: prior completed bar target 0%; next bar open simulation |
| v1 | breakout_8 + volume_26 | 9860.16 | -139.84 | sell /  / breakout_8 + volume_26: prior completed bar target 0%; next bar open simulation |
| v1 | reversion_12 AND volume_26 | 9940.10 | -59.90 | sell /  / reversion_12 AND volume_26: prior completed bar target 0%; next bar open simulation |
| v1 | reversion_12 + volume_26 | 9881.84 | -118.16 | sell /  / reversion_12 + volume_26: prior completed bar target 0%; next bar open simulation |
| v1 | ema_12_26 | 9806.10 | -193.90 | buy /  / EMA12 > EMA26; 조건 충족; EMA12=336.77, EMA26=336.613 |
| v1 | macd_12_26_9 | 9890.22 | -109.78 | buy /  / MACD > 신호선 그리고 MACD > 0; 조건 충족; MACD=0.15695, signal9=-0.460372 |
| v1 | rsi_14_recovery | 9986.37 | -13.63 | sell /  / 직전 RSI14 < 30, 현재 RSI14 >= 30 (한 봉 목표); 조건 미충족; RSI14=61.6663, previous_RSI14=57.046 |
| v1 | bollinger_20_reentry | 9964.67 | -35.33 | sell /  / 직전 종가 < 직전 하단밴드, 현재 하단밴드 <= 종가 <= SMA20 (한 봉 목표); 조건 미충족; close=336.53, lower20=336.046, SMA20=337.886, previous_lower20=336.231 |
| v1 | donchian_20 | 9830.85 | -169.15 | sell /  / 종가 > 현재 봉을 제외한 직전 20봉 최고가; 조건 미충족; close=339.04, prior_high20=339.42 |
| v1 | atr_14_breakout | 9746.56 | -253.44 | sell /  / 종가 > 직전 종가 + 직전 ATR14 그리고 종가 > EMA26; 조건 미충족; close=339.04, threshold=340.465, prior_ATR14=1.34545, EMA26=336.613 |
| v1 | session_vwap | 9727.57 | -272.43 | sell /  / 종가 > 뉴욕 거래일별 누적 전형가격 VWAP; 조건 미충족; close=336.08, session_VWAP=337.149, session_volume=2.04555e+06 |
| v1 | obv_20 | 10007.55 | 7.55 | sell /  / OBV > OBV의 SMA20 그리고 종가 > EMA26; 조건 미충족; OBV=-1.60234e+07, OBV_SMA20=-1.31788e+07, close=341.625, EMA26=338.807 |
| v1 | stochastic_14_3_recovery | 9718.50 | -281.50 | sell /  / 직전 %K14 < 20에서 %K14가 %D3 상향 돌파 (한 봉 목표); 조건 미충족; K14=11.111, D3=10.514, previous_K14=15.4166, previous_D3=10.08 |
| v1 | mfi_14_recovery | 9935.64 | -64.36 | sell /  / 직전 MFI14 < 20, 현재 MFI14 >= 20 (한 봉 목표); 조건 미충족; MFI14=30.2719, previous_MFI14=26.8492 |
| v1 | adx_14_trend | 9777.21 | -222.79 | buy /  / Wilder ADX14 >= 25 그리고 +DI14 > -DI14; 조건 충족; ADX14=35.2307, plus_DI14=26.9426, minus_DI14=21.9658 |
| v1 | aroon_25_trend | 9824.71 | -175.29 | sell /  / Aroon25 Up > 70 그리고 Down < 30 (동률이면 최신 극값); 조건 미충족; Aroon_up=68, Aroon_down=16 |
| v1 | cci_20_momentum | 9950.54 | -49.46 | sell /  / CCI20 > 100 (전형가격·평균절대편차); 조건 미충족; CCI20=28.4392 |
| v1 | williams_14_recovery | 9820.43 | -179.57 | sell /  / 직전 Williams %R14 < -80, 현재 >= -80 (한 봉 목표); 조건 미충족; Williams_R14=-13.9552, previous_R14=-4.5732 |
| v1 | cmf_20_accumulation | 9932.16 | -67.84 | sell /  / Chaikin Money Flow20 > 0.1; 조건 미충족; CMF20=-0.14511, volume20=9.3038e+06 |
| v1 | chaikin_3_10 | 9837.22 | -162.78 | sell /  / ADL의 EMA3 - EMA10 > 0 그리고 종가 > EMA26; 조건 미충족; Chaikin3_10=7273.89, ADL=-1.28498e+07, close=336.08, EMA26=336.65 |
| v1 | roc_10_momentum | 9836.40 | -163.60 | sell /  / 10봉 ROC > 1% 그리고 종가 > EMA26; 조건 미충족; ROC10_percent=0.964142, close=337.72, EMA26=336.695 |
| v1 | trix_15_trend | 9723.73 | -276.27 | sell /  / 15봉 삼중 EMA의 1봉 변화율 TRIX > 0 그리고 종가 > EMA26; 조건 미충족; TRIX15_percent=0.0135144, close=337.6, EMA26=338.759 |
| v1 | keltner_20_breakout | 9905.24 | -94.76 | sell /  / 종가 > EMA20 + 2 x Wilder ATR14; 조건 미충족; close=339.04, upper_Keltner=339.281, EMA20=336.559, ATR14=1.36146 |
| v1 | opening_range_30m | 9850.26 | -149.74 | sell /  / 뉴욕 09:30·09:45 두 완료 봉 최고가를 10:00 이후 종가가 돌파; 조건 미충족; close=337.72, opening_high=339.035 |
| v2 | cash | 10000.00 | 0.00 | 대기 /  / 새 신호 대기 |
| v2 | buy_hold | 10054.85 | 54.85 | buy / partial / 직전 완료 봉 목표 비중 100%; 다음 봉 시가 가정 |
| v2 | trend_8_26 | 9847.20 | -152.80 | buy / partial / 직전 완료 봉 목표 비중 100%; 다음 봉 시가 가정 |
| v2 | momentum_26 | 9272.76 | -727.24 | sell / filled / 직전 완료 봉 목표 비중 0%; 다음 봉 시가 가정 |
| v2 | breakout_8 | 9100.10 | -899.90 | sell / filled / 직전 완료 봉 목표 비중 0%; 다음 봉 시가 가정 |
| v2 | reversion_12 | 9739.90 | -260.10 | sell / filled / 직전 완료 봉 목표 비중 0%; 다음 봉 시가 가정 |
| v2 | volume_26 | 9781.50 | -218.50 | sell / filled / 직전 완료 봉 목표 비중 0%; 다음 봉 시가 가정 |
| v2 | trend_8_26 AND momentum_26 | 9813.23 | -186.77 | sell / filled / 직전 완료 봉 목표 비중 0%; 다음 봉 시가 가정 |
| v2 | trend_8_26 + momentum_26 | 9576.29 | -423.71 | sell / filled / 직전 완료 봉 목표 비중 50%; 다음 봉 시가 가정 |
| v2 | trend_8_26 AND breakout_8 | 9287.76 | -712.24 | sell / filled / 직전 완료 봉 목표 비중 0%; 다음 봉 시가 가정 |
| v2 | trend_8_26 + breakout_8 | 9487.27 | -512.73 | sell / filled / 직전 완료 봉 목표 비중 50%; 다음 봉 시가 가정 |
| v2 | trend_8_26 AND reversion_12 | 9877.09 | -122.91 | sell / filled / 직전 완료 봉 목표 비중 0%; 다음 봉 시가 가정 |
| v2 | trend_8_26 + reversion_12 | 9834.74 | -165.26 | sell / filled / 직전 완료 봉 목표 비중 50%; 다음 봉 시가 가정 |
| v2 | trend_8_26 AND volume_26 | 9833.30 | -166.70 | sell / filled / 직전 완료 봉 목표 비중 0%; 다음 봉 시가 가정 |
| v2 | trend_8_26 + volume_26 | 9814.99 | -185.01 | sell / filled / 직전 완료 봉 목표 비중 50%; 다음 봉 시가 가정 |
| v2 | momentum_26 AND breakout_8 | 9058.00 | -942.00 | sell / filled / 직전 완료 봉 목표 비중 0%; 다음 봉 시가 가정 |
| v2 | momentum_26 + breakout_8 | 9207.02 | -792.98 | sell / filled / 직전 완료 봉 목표 비중 0%; 다음 봉 시가 가정 |
| v2 | momentum_26 AND reversion_12 | 9827.31 | -172.69 | sell / filled / 직전 완료 봉 목표 비중 0%; 다음 봉 시가 가정 |
| v2 | momentum_26 + reversion_12 | 9644.70 | -355.30 | sell / filled / 직전 완료 봉 목표 비중 0%; 다음 봉 시가 가정 |
| v2 | momentum_26 AND volume_26 | 9833.30 | -166.70 | sell / filled / 직전 완료 봉 목표 비중 0%; 다음 봉 시가 가정 |
| v2 | momentum_26 + volume_26 | 9605.25 | -394.75 | sell / filled / 직전 완료 봉 목표 비중 0%; 다음 봉 시가 가정 |
| v2 | breakout_8 AND reversion_12 | 10000.00 | 0.00 | 대기 /  / 새 신호 대기 |
| v2 | breakout_8 + reversion_12 | 9494.12 | -505.88 | sell / filled / 직전 완료 봉 목표 비중 0%; 다음 봉 시가 가정 |
| v2 | breakout_8 AND volume_26 | 9911.14 | -88.86 | sell / filled / 직전 완료 봉 목표 비중 0%; 다음 봉 시가 가정 |
| v2 | breakout_8 + volume_26 | 9454.59 | -545.41 | sell / filled / 직전 완료 봉 목표 비중 0%; 다음 봉 시가 가정 |
| v2 | reversion_12 AND volume_26 | 9987.18 | -12.82 | sell / filled / 직전 완료 봉 목표 비중 0%; 다음 봉 시가 가정 |
| v2 | reversion_12 + volume_26 | 9801.97 | -198.03 | sell / filled / 직전 완료 봉 목표 비중 0%; 다음 봉 시가 가정 |
| v2 | ema_12_26 | 9803.16 | -196.84 | buy / partial / EMA12 > EMA26; 조건 충족; EMA12=336.77, EMA26=336.613; 직전 완료 봉 목표를 다음 봉 시가에 모의 적용 |
| v2 | macd_12_26_9 | 9887.25 | -112.75 | buy / partial / MACD > 신호선 그리고 MACD > 0; 조건 충족; MACD=0.15695, signal9=-0.460372; 직전 완료 봉 목표를 다음 봉 시가에 모의 적용 |
| v2 | rsi_14_recovery | 9984.37 | -15.63 | sell / filled / 직전 RSI14 < 30, 현재 RSI14 >= 30 (한 봉 목표); 조건 미충족; RSI14=61.6663, previous_RSI14=57.046; 직전 완료 봉 목표를 다음 봉 시가에 모의 적용 |
| v2 | bollinger_20_reentry | 9962.68 | -37.32 | sell / filled / 직전 종가 < 직전 하단밴드, 현재 하단밴드 <= 종가 <= SMA20 (한 봉 목표); 조건 미충족; close=336.53, lower20=336.046, SMA20=337.886, previous_lower20=336.231; 직전 완료 봉 목표를 다음 봉 시가에 모의 적용 |
| v2 | donchian_20 | 9824.96 | -175.04 | sell / filled / 종가 > 현재 봉을 제외한 직전 20봉 최고가; 조건 미충족; close=339.04, prior_high20=339.42; 직전 완료 봉 목표를 다음 봉 시가에 모의 적용 |
| v2 | atr_14_breakout | 9736.82 | -263.18 | sell / filled / 종가 > 직전 종가 + 직전 ATR14 그리고 종가 > EMA26; 조건 미충족; close=339.04, threshold=340.465, prior_ATR14=1.34545, EMA26=336.613; 직전 완료 봉 목표를 다음 봉 시가에 모의 적용 |
| v2 | session_vwap | 9717.84 | -282.16 | sell / filled / 종가 > 뉴욕 거래일별 누적 전형가격 VWAP; 조건 미충족; close=336.08, session_VWAP=337.149, session_volume=2.04555e+06; 직전 완료 봉 목표를 다음 봉 시가에 모의 적용 |
| v2 | obv_20 | 10005.55 | 5.55 | sell / filled / OBV > OBV의 SMA20 그리고 종가 > EMA26; 조건 미충족; OBV=-1.38544e+07, OBV_SMA20=-1.10099e+07, close=341.625, EMA26=338.807; 직전 완료 봉 목표를 다음 봉 시가에 모의 적용 |
| v2 | stochastic_14_3_recovery | 9704.91 | -295.09 | sell / filled / 직전 %K14 < 20에서 %K14가 %D3 상향 돌파 (한 봉 목표); 조건 미충족; K14=11.111, D3=10.514, previous_K14=15.4166, previous_D3=10.08; 직전 완료 봉 목표를 다음 봉 시가에 모의 적용 |
| v2 | mfi_14_recovery | 9931.66 | -68.34 | sell / filled / 직전 MFI14 < 20, 현재 MFI14 >= 20 (한 봉 목표); 조건 미충족; MFI14=30.2719, previous_MFI14=26.8492; 직전 완료 봉 목표를 다음 봉 시가에 모의 적용 |
| v2 | adx_14_trend | 9774.28 | -225.72 | buy / partial / Wilder ADX14 >= 25 그리고 +DI14 > -DI14; 조건 충족; ADX14=35.2307, plus_DI14=26.9426, minus_DI14=21.9658; 직전 완료 봉 목표를 다음 봉 시가에 모의 적용 |
| v2 | aroon_25_trend | 9822.74 | -177.26 | sell / filled / Aroon25 Up > 70 그리고 Down < 30 (동률이면 최신 극값); 조건 미충족; Aroon_up=68, Aroon_down=16; 직전 완료 봉 목표를 다음 봉 시가에 모의 적용 |
| v2 | cci_20_momentum | 9946.56 | -53.44 | sell / filled / CCI20 > 100 (전형가격·평균절대편차); 조건 미충족; CCI20=28.4392; 직전 완료 봉 목표를 다음 봉 시가에 모의 적용 |
| v2 | williams_14_recovery | 9810.61 | -189.39 | sell / filled / 직전 Williams %R14 < -80, 현재 >= -80 (한 봉 목표); 조건 미충족; Williams_R14=-13.9552, previous_R14=-4.5732; 직전 완료 봉 목표를 다음 봉 시가에 모의 적용 |
| v2 | cmf_20_accumulation | 9930.17 | -69.83 | sell / filled / Chaikin Money Flow20 > 0.1; 조건 미충족; CMF20=-0.14511, volume20=9.3038e+06; 직전 완료 봉 목표를 다음 봉 시가에 모의 적용 |
| v2 | chaikin_3_10 | 9831.32 | -168.68 | sell / filled / ADL의 EMA3 - EMA10 > 0 그리고 종가 > EMA26; 조건 미충족; Chaikin3_10=7273.89, ADL=-1.28498e+07, close=336.08, EMA26=336.65; 직전 완료 봉 목표를 다음 봉 시가에 모의 적용 |
| v2 | roc_10_momentum | 9832.47 | -167.53 | sell / filled / 10봉 ROC > 1% 그리고 종가 > EMA26; 조건 미충족; ROC10_percent=0.964142, close=337.72, EMA26=336.695; 직전 완료 봉 목표를 다음 봉 시가에 모의 적용 |
| v2 | trix_15_trend | 9715.96 | -284.04 | sell / filled / 15봉 삼중 EMA의 1봉 변화율 TRIX > 0 그리고 종가 > EMA26; 조건 미충족; TRIX15_percent=0.0135144, close=337.6, EMA26=338.759; 직전 완료 봉 목표를 다음 봉 시가에 모의 적용 |
| v2 | keltner_20_breakout | 9901.28 | -98.72 | sell / filled / 종가 > EMA20 + 2 x Wilder ATR14; 조건 미충족; close=339.04, upper_Keltner=339.281, EMA20=336.559, ATR14=1.36146; 직전 완료 봉 목표를 다음 봉 시가에 모의 적용 |
| v2 | opening_range_30m | 9846.33 | -153.67 | sell / filled / 뉴욕 09:30·09:45 두 완료 봉 최고가를 10:00 이후 종가가 돌파; 조건 미충족; close=337.72, opening_high=339.035; 직전 완료 봉 목표를 다음 봉 시가에 모의 적용 |

### 같은 기간의 비용·노출 비교 (사후 연구)

| 전략 | 비용 전 | 비용 후 | 100% 보유 | 같은 평균 노출 보유 | 평균 노출 |
|---|---:|---:|---:|---:|---:|
| cash | 0.00% | 0.00% | 0.02% | 0.00% | 0.00% |
| buy_hold | 0.44% | 0.02% | 0.02% | 0.02% | 100.00% |
| trend_8_26 | 0.52% | -3.62% | 0.02% | 0.01% | 53.03% |
| momentum_26 | -2.90% | -9.59% | 0.02% | 0.01% | 49.60% |
| breakout_8 | -2.81% | -17.84% | 0.02% | 0.00% | 20.05% |
| reversion_12 | 5.24% | -9.15% | 0.02% | 0.01% | 25.86% |
| volume_26 | 0.25% | -6.27% | 0.02% | 0.00% | 7.12% |
| trend_8_26 AND momentum_26 | 0.72% | -3.82% | 0.02% | 0.01% | 41.16% |
| trend_8_26 + momentum_26 | -1.20% | -6.45% | 0.02% | 0.01% | 51.32% |
| trend_8_26 AND breakout_8 | -3.21% | -13.22% | 0.02% | 0.00% | 12.14% |
| trend_8_26 + breakout_8 | -1.14% | -10.63% | 0.02% | 0.01% | 36.55% |
| trend_8_26 AND reversion_12 | 2.66% | -3.61% | 0.02% | 0.00% | 7.39% |
| trend_8_26 + reversion_12 | 2.87% | -5.84% | 0.02% | 0.01% | 39.45% |
| trend_8_26 AND volume_26 | -0.42% | -4.11% | 0.02% | 0.00% | 3.96% |
| trend_8_26 + volume_26 | 0.40% | -4.95% | 0.02% | 0.01% | 30.08% |
| momentum_26 AND breakout_8 | -2.68% | -13.84% | 0.02% | 0.00% | 12.66% |
| momentum_26 + breakout_8 | -2.83% | -13.62% | 0.02% | 0.01% | 34.83% |
| momentum_26 AND reversion_12 | 2.79% | -4.29% | 0.02% | 0.00% | 6.86% |
| momentum_26 + reversion_12 | 1.11% | -7.83% | 0.02% | 0.01% | 37.74% |
| momentum_26 AND volume_26 | 0.21% | -2.70% | 0.02% | 0.00% | 2.90% |
| momentum_26 + volume_26 | -1.32% | -7.55% | 0.02% | 0.01% | 28.37% |
| breakout_8 AND reversion_12 | 0.00% | 0.00% | 0.02% | 0.00% | 0.00% |
| breakout_8 + reversion_12 | 1.15% | -12.33% | 0.02% | 0.00% | 22.96% |
| breakout_8 AND volume_26 | -0.25% | -2.32% | 0.02% | 0.00% | 1.32% |
| breakout_8 + volume_26 | -1.28% | -11.51% | 0.02% | 0.00% | 13.60% |
| reversion_12 AND volume_26 | 1.33% | -2.01% | 0.02% | 0.00% | 3.43% |
| reversion_12 + volume_26 | 2.72% | -6.75% | 0.02% | 0.00% | 16.50% |
| ema_12_26 | 0.08% | -3.23% | 0.02% | 0.01% | 51.45% |
| macd_12_26_9 | 0.19% | -4.34% | 0.02% | 0.01% | 32.19% |
| rsi_14_recovery | 0.47% | -2.03% | 0.02% | 0.00% | 1.58% |
| bollinger_20_reentry | 0.51% | -3.62% | 0.02% | 0.00% | 2.64% |
| donchian_20 | -1.81% | -5.05% | 0.02% | 0.00% | 3.17% |
| atr_14_breakout | -1.35% | -8.92% | 0.02% | 0.00% | 5.28% |
| session_vwap | 1.60% | -8.14% | 0.02% | 0.01% | 48.02% |
| obv_20 | -3.51% | -14.21% | 0.02% | 0.01% | 30.34% |
| stochastic_14_3_recovery | -1.37% | -11.94% | 0.02% | 0.00% | 7.12% |
| mfi_14_recovery | 0.32% | -2.18% | 0.02% | 0.00% | 1.58% |
| adx_14_trend | -2.12% | -4.55% | 0.02% | 0.01% | 29.02% |
| aroon_25_trend | -1.12% | -5.19% | 0.02% | 0.00% | 22.69% |
| cci_20_momentum | -2.84% | -10.67% | 0.02% | 0.00% | 16.36% |
| williams_14_recovery | -0.99% | -10.48% | 0.02% | 0.00% | 6.33% |
| cmf_20_accumulation | -1.74% | -9.66% | 0.02% | 0.01% | 28.76% |
| chaikin_3_10 | 0.92% | -7.98% | 0.02% | 0.01% | 34.30% |
| roc_10_momentum | -1.36% | -4.22% | 0.02% | 0.00% | 8.44% |
| trix_15_trend | -1.25% | -8.83% | 0.02% | 0.01% | 35.36% |
| keltner_20_breakout | -1.21% | -4.07% | 0.02% | 0.00% | 4.22% |
| opening_range_30m | -0.23% | -3.93% | 0.02% | 0.00% | 17.41% |

동일 구간·초기 자금, 종료 시 청산 비용 포함. 노출 맞춤은 사후 설명용이며 v2 실제 계좌 성과가 아닙니다.
[낙폭 분해·비용 영향·전체 구간](JPM/comparison.json)

[v1 전체 기록](JPM/accounts.json) · [v2 전체 기록](JPM/accounts-v2.json)

## XOM 계좌

| 모델 | 전략 | 평가액 USD | 손익 USD | 최근 매매·이유 |
|---|---|---:|---:|---|
| v1 | cash | 10000.00 | 0.00 | 대기 /  / 새 신호 대기 |
| v1 | buy_hold | 9933.38 | -66.62 | buy /  / buy_hold: prior completed bar target 100%; next bar open simulation |
| v1 | trend_8_26 | 9862.79 | -137.21 | sell /  / trend_8_26: prior completed bar target 0%; next bar open simulation |
| v1 | momentum_26 | 9934.85 | -65.15 | sell /  / momentum_26: prior completed bar target 0%; next bar open simulation |
| v1 | breakout_8 | 9752.67 | -247.33 | sell /  / breakout_8: prior completed bar target 0%; next bar open simulation |
| v1 | reversion_12 | 9680.85 | -319.15 | buy /  / reversion_12: prior completed bar target 100%; next bar open simulation |
| v1 | volume_26 | 9732.23 | -267.77 | sell /  / volume_26: prior completed bar target 0%; next bar open simulation |
| v1 | trend_8_26 AND momentum_26 | 9853.77 | -146.23 | sell /  / trend_8_26 AND momentum_26: prior completed bar target 0%; next bar open simulation |
| v1 | trend_8_26 + momentum_26 | 9898.87 | -101.13 | sell /  / trend_8_26 + momentum_26: prior completed bar target 0%; next bar open simulation |
| v1 | trend_8_26 AND breakout_8 | 9829.71 | -170.29 | sell /  / trend_8_26 AND breakout_8: prior completed bar target 0%; next bar open simulation |
| v1 | trend_8_26 + breakout_8 | 9827.64 | -172.36 | sell /  / trend_8_26 + breakout_8: prior completed bar target 0%; next bar open simulation |
| v1 | trend_8_26 AND reversion_12 | 9652.28 | -347.72 | sell /  / trend_8_26 AND reversion_12: prior completed bar target 0%; next bar open simulation |
| v1 | trend_8_26 + reversion_12 | 9771.37 | -228.63 | buy /  / trend_8_26 + reversion_12: prior completed bar target 50%; next bar open simulation |
| v1 | trend_8_26 AND volume_26 | 9849.16 | -150.84 | sell /  / trend_8_26 AND volume_26: prior completed bar target 0%; next bar open simulation |
| v1 | trend_8_26 + volume_26 | 9797.51 | -202.49 | sell /  / trend_8_26 + volume_26: prior completed bar target 0%; next bar open simulation |
| v1 | momentum_26 AND breakout_8 | 9801.24 | -198.76 | sell /  / momentum_26 AND breakout_8: prior completed bar target 0%; next bar open simulation |
| v1 | momentum_26 + breakout_8 | 9843.61 | -156.39 | sell /  / momentum_26 + breakout_8: prior completed bar target 0%; next bar open simulation |
| v1 | momentum_26 AND reversion_12 | 9766.58 | -233.42 | sell /  / momentum_26 AND reversion_12: prior completed bar target 0%; next bar open simulation |
| v1 | momentum_26 + reversion_12 | 9806.91 | -193.09 | buy /  / momentum_26 + reversion_12: prior completed bar target 50%; next bar open simulation |
| v1 | momentum_26 AND volume_26 | 9985.49 | -14.51 | sell /  / momentum_26 AND volume_26: prior completed bar target 0%; next bar open simulation |
| v1 | momentum_26 + volume_26 | 9833.06 | -166.94 | sell /  / momentum_26 + volume_26: prior completed bar target 0%; next bar open simulation |
| v1 | breakout_8 AND reversion_12 | 10000.00 | 0.00 | 대기 /  / 새 신호 대기 |
| v1 | breakout_8 + reversion_12 | 9716.67 | -283.33 | buy /  / breakout_8 + reversion_12: prior completed bar target 50%; next bar open simulation |
| v1 | breakout_8 AND volume_26 | 9950.44 | -49.56 | sell /  / breakout_8 AND volume_26: prior completed bar target 0%; next bar open simulation |
| v1 | breakout_8 + volume_26 | 9742.32 | -257.68 | sell /  / breakout_8 + volume_26: prior completed bar target 0%; next bar open simulation |
| v1 | reversion_12 AND volume_26 | 9840.91 | -159.09 | sell /  / reversion_12 AND volume_26: prior completed bar target 0%; next bar open simulation |
| v1 | reversion_12 + volume_26 | 9706.57 | -293.43 | buy /  / reversion_12 + volume_26: prior completed bar target 50%; next bar open simulation |
| v1 | ema_12_26 | 9973.99 | -26.01 | sell /  / EMA12 > EMA26; 조건 미충족; EMA12=177.968, EMA26=178.055 |
| v1 | macd_12_26_9 | 10064.24 | 64.24 | sell /  / MACD > 신호선 그리고 MACD > 0; 조건 미충족; MACD=0.288973, signal9=0.30355 |
| v1 | rsi_14_recovery | 9938.85 | -61.15 | sell /  / 직전 RSI14 < 30, 현재 RSI14 >= 30 (한 봉 목표); 조건 미충족; RSI14=29.423, previous_RSI14=31.8651 |
| v1 | bollinger_20_reentry | 9852.90 | -147.10 | sell /  / 직전 종가 < 직전 하단밴드, 현재 하단밴드 <= 종가 <= SMA20 (한 봉 목표); 조건 미충족; close=175.55, lower20=175.189, SMA20=177.794, previous_lower20=175.528 |
| v1 | donchian_20 | 9832.30 | -167.70 | sell /  / 종가 > 현재 봉을 제외한 직전 20봉 최고가; 조건 미충족; close=179.01, prior_high20=179.16 |
| v1 | atr_14_breakout | 9864.96 | -135.04 | sell /  / 종가 > 직전 종가 + 직전 ATR14 그리고 종가 > EMA26; 조건 미충족; close=177.19, threshold=177.748, prior_ATR14=0.663113, EMA26=175.734 |
| v1 | session_vwap | 9973.63 | -26.37 | sell /  / 종가 > 뉴욕 거래일별 누적 전형가격 VWAP; 조건 미충족; close=178.14, session_VWAP=178.717, session_volume=890333 |
| v1 | obv_20 | 9901.33 | -98.67 | sell /  / OBV > OBV의 SMA20 그리고 종가 > EMA26; 조건 미충족; OBV=1.97825e+07, OBV_SMA20=1.99344e+07, close=178.275, EMA26=178.258 |
| v1 | stochastic_14_3_recovery | 9739.81 | -260.19 | sell /  / 직전 %K14 < 20에서 %K14가 %D3 상향 돌파 (한 봉 목표); 조건 미충족; K14=18.8495, D3=10.0725, previous_K14=10.3837, previous_D3=4.08009 |
| v1 | mfi_14_recovery | 10000.00 | 0.00 | 대기 /  / 새 신호 대기 |
| v1 | adx_14_trend | 9999.47 | -0.53 | sell /  / Wilder ADX14 >= 25 그리고 +DI14 > -DI14; 조건 미충족; ADX14=23.8302, plus_DI14=25.6436, minus_DI14=22.6035 |
| v1 | aroon_25_trend | 9754.76 | -245.24 | sell /  / Aroon25 Up > 70 그리고 Down < 30 (동률이면 최신 극값); 조건 미충족; Aroon_up=88, Aroon_down=100 |
| v1 | cci_20_momentum | 9743.77 | -256.23 | sell /  / CCI20 > 100 (전형가격·평균절대편차); 조건 미충족; CCI20=96.5349 |
| v1 | williams_14_recovery | 9671.96 | -328.04 | sell /  / 직전 Williams %R14 < -80, 현재 >= -80 (한 봉 목표); 조건 미충족; Williams_R14=-99.1277, previous_R14=-77.3942 |
| v1 | cmf_20_accumulation | 9966.29 | -33.71 | sell /  / Chaikin Money Flow20 > 0.1; 조건 미충족; CMF20=0.0744325, volume20=5.28871e+06 |
| v1 | chaikin_3_10 | 9954.74 | -45.26 | sell /  / ADL의 EMA3 - EMA10 > 0 그리고 종가 > EMA26; 조건 미충족; Chaikin3_10=-7287.74, ADL=2.55494e+07, close=178.275, EMA26=178.258 |
| v1 | roc_10_momentum | 9940.60 | -59.40 | sell /  / 10봉 ROC > 1% 그리고 종가 > EMA26; 조건 미충족; ROC10_percent=0.782107, close=178.47, EMA26=176.891 |
| v1 | trix_15_trend | 9952.41 | -47.59 | sell /  / 15봉 삼중 EMA의 1봉 변화율 TRIX > 0 그리고 종가 > EMA26; 조건 미충족; TRIX15_percent=0.0212551, close=178.14, EMA26=178.249 |
| v1 | keltner_20_breakout | 9937.30 | -62.70 | sell /  / 종가 > EMA20 + 2 x Wilder ATR14; 조건 미충족; close=178.845, upper_Keltner=179.079, EMA20=177.884, ATR14=0.597175 |
| v1 | opening_range_30m | 10049.37 | 49.37 | sell /  / 뉴욕 09:30·09:45 두 완료 봉 최고가를 10:00 이후 종가가 돌파; 자료 부족·변동폭 또는 거래량 없음: 대기; close=179.01 |
| v2 | cash | 10000.00 | 0.00 | 대기 /  / 새 신호 대기 |
| v2 | buy_hold | 10250.38 | 250.38 | buy / partial / 직전 완료 봉 목표 비중 100%; 다음 봉 시가 가정 |
| v2 | trend_8_26 | 9953.74 | -46.26 | sell / filled / 직전 완료 봉 목표 비중 0%; 다음 봉 시가 가정 |
| v2 | momentum_26 | 10102.33 | 102.33 | sell / filled / 직전 완료 봉 목표 비중 0%; 다음 봉 시가 가정 |
| v2 | breakout_8 | 9222.01 | -777.99 | sell / filled / 직전 완료 봉 목표 비중 0%; 다음 봉 시가 가정 |
| v2 | reversion_12 | 9498.96 | -501.04 | buy / partial / 직전 완료 봉 목표 비중 100%; 다음 봉 시가 가정 |
| v2 | volume_26 | 9635.02 | -364.98 | sell / filled / 직전 완료 봉 목표 비중 0%; 다음 봉 시가 가정 |
| v2 | trend_8_26 AND momentum_26 | 9950.02 | -49.98 | sell / filled / 직전 완료 봉 목표 비중 0%; 다음 봉 시가 가정 |
| v2 | trend_8_26 + momentum_26 | 10027.90 | 27.90 | sell / filled / 직전 완료 봉 목표 비중 0%; 다음 봉 시가 가정 |
| v2 | trend_8_26 AND breakout_8 | 9281.59 | -718.41 | sell / filled / 직전 완료 봉 목표 비중 0%; 다음 봉 시가 가정 |
| v2 | trend_8_26 + breakout_8 | 9621.99 | -378.01 | sell / filled / 직전 완료 봉 목표 비중 0%; 다음 봉 시가 가정 |
| v2 | trend_8_26 AND reversion_12 | 9493.76 | -506.24 | sell / filled / 직전 완료 봉 목표 비중 0%; 다음 봉 시가 가정 |
| v2 | trend_8_26 + reversion_12 | 9723.74 | -276.26 | buy / filled / 직전 완료 봉 목표 비중 50%; 다음 봉 시가 가정 |
| v2 | trend_8_26 AND volume_26 | 9742.44 | -257.56 | sell / filled / 직전 완료 봉 목표 비중 0%; 다음 봉 시가 가정 |
| v2 | trend_8_26 + volume_26 | 9793.25 | -206.75 | sell / filled / 직전 완료 봉 목표 비중 0%; 다음 봉 시가 가정 |
| v2 | momentum_26 AND breakout_8 | 9269.79 | -730.21 | sell / filled / 직전 완료 봉 목표 비중 0%; 다음 봉 시가 가정 |
| v2 | momentum_26 + breakout_8 | 9652.93 | -347.07 | sell / filled / 직전 완료 봉 목표 비중 0%; 다음 봉 시가 가정 |
| v2 | momentum_26 AND reversion_12 | 9567.55 | -432.45 | sell / filled / 직전 완료 봉 목표 비중 0%; 다음 봉 시가 가정 |
| v2 | momentum_26 + reversion_12 | 9795.99 | -204.01 | buy / filled / 직전 완료 봉 목표 비중 50%; 다음 봉 시가 가정 |
| v2 | momentum_26 AND volume_26 | 9941.52 | -58.48 | sell / filled / 직전 완료 봉 목표 비중 0%; 다음 봉 시가 가정 |
| v2 | momentum_26 + volume_26 | 9886.61 | -113.39 | sell / filled / 직전 완료 봉 목표 비중 0%; 다음 봉 시가 가정 |
| v2 | breakout_8 AND reversion_12 | 10000.00 | 0.00 | 대기 /  / 새 신호 대기 |
| v2 | breakout_8 + reversion_12 | 9359.32 | -640.68 | buy / filled / 직전 완료 봉 목표 비중 50%; 다음 봉 시가 가정 |
| v2 | breakout_8 AND volume_26 | 9918.86 | -81.14 | sell / filled / 직전 완료 봉 목표 비중 0%; 다음 봉 시가 가정 |
| v2 | breakout_8 + volume_26 | 9445.83 | -554.17 | sell / filled / 직전 완료 봉 목표 비중 0%; 다음 봉 시가 가정 |
| v2 | reversion_12 AND volume_26 | 9787.67 | -212.33 | sell / filled / 직전 완료 봉 목표 비중 0%; 다음 봉 시가 가정 |
| v2 | reversion_12 + volume_26 | 9586.94 | -413.06 | buy / filled / 직전 완료 봉 목표 비중 50%; 다음 봉 시가 가정 |
| v2 | ema_12_26 | 9971.99 | -28.01 | sell / filled / EMA12 > EMA26; 조건 미충족; EMA12=177.968, EMA26=178.055; 직전 완료 봉 목표를 다음 봉 시가에 모의 적용 |
| v2 | macd_12_26_9 | 10060.21 | 60.21 | sell / filled / MACD > 신호선 그리고 MACD > 0; 조건 미충족; MACD=0.288973, signal9=0.30355; 직전 완료 봉 목표를 다음 봉 시가에 모의 적용 |
| v2 | rsi_14_recovery | 9936.86 | -63.14 | sell / filled / 직전 RSI14 < 30, 현재 RSI14 >= 30 (한 봉 목표); 조건 미충족; RSI14=29.423, previous_RSI14=31.8651; 직전 완료 봉 목표를 다음 봉 시가에 모의 적용 |
| v2 | bollinger_20_reentry | 9848.96 | -151.04 | sell / filled / 직전 종가 < 직전 하단밴드, 현재 하단밴드 <= 종가 <= SMA20 (한 봉 목표); 조건 미충족; close=175.55, lower20=175.189, SMA20=177.794, previous_lower20=175.528; 직전 완료 봉 목표를 다음 봉 시가에 모의 적용 |
| v2 | donchian_20 | 9824.43 | -175.57 | sell / filled / 종가 > 현재 봉을 제외한 직전 20봉 최고가; 조건 미충족; close=179.01, prior_high20=179.16; 직전 완료 봉 목표를 다음 봉 시가에 모의 적용 |
| v2 | atr_14_breakout | 9859.04 | -140.96 | sell / filled / 종가 > 직전 종가 + 직전 ATR14 그리고 종가 > EMA26; 조건 미충족; close=177.19, threshold=177.748, prior_ATR14=0.663113, EMA26=175.734; 직전 완료 봉 목표를 다음 봉 시가에 모의 적용 |
| v2 | session_vwap | 9967.65 | -32.35 | sell / filled / 종가 > 뉴욕 거래일별 누적 전형가격 VWAP; 조건 미충족; close=178.14, session_VWAP=178.717, session_volume=890333; 직전 완료 봉 목표를 다음 봉 시가에 모의 적용 |
| v2 | obv_20 | 9893.41 | -106.59 | sell / filled / OBV > OBV의 SMA20 그리고 종가 > EMA26; 조건 미충족; OBV=1.97825e+07, OBV_SMA20=1.99344e+07, close=178.275, EMA26=178.258; 직전 완료 봉 목표를 다음 봉 시가에 모의 적용 |
| v2 | stochastic_14_3_recovery | 9732.02 | -267.98 | sell / filled / 직전 %K14 < 20에서 %K14가 %D3 상향 돌파 (한 봉 목표); 조건 미충족; K14=18.8495, D3=10.0725, previous_K14=10.3837, previous_D3=4.08009; 직전 완료 봉 목표를 다음 봉 시가에 모의 적용 |
| v2 | mfi_14_recovery | 10000.00 | 0.00 | 대기 /  / 새 신호 대기 |
| v2 | adx_14_trend | 9993.47 | -6.53 | sell / filled / Wilder ADX14 >= 25 그리고 +DI14 > -DI14; 조건 미충족; ADX14=23.8302, plus_DI14=25.6436, minus_DI14=22.6035; 직전 완료 봉 목표를 다음 봉 시가에 모의 적용 |
| v2 | aroon_25_trend | 9750.86 | -249.14 | sell / filled / Aroon25 Up > 70 그리고 Down < 30 (동률이면 최신 극값); 조건 미충족; Aroon_up=88, Aroon_down=100; 직전 완료 봉 목표를 다음 봉 시가에 모의 적용 |
| v2 | cci_20_momentum | 9730.14 | -269.86 | sell / filled / CCI20 > 100 (전형가격·평균절대편차); 조건 미충족; CCI20=96.5349; 직전 완료 봉 목표를 다음 봉 시가에 모의 적용 |
| v2 | williams_14_recovery | 9664.23 | -335.77 | sell / filled / 직전 Williams %R14 < -80, 현재 >= -80 (한 봉 목표); 조건 미충족; Williams_R14=-99.1277, previous_R14=-77.3942; 직전 완료 봉 목표를 다음 봉 시가에 모의 적용 |
| v2 | cmf_20_accumulation | 9962.31 | -37.69 | sell / filled / Chaikin Money Flow20 > 0.1; 조건 미충족; CMF20=0.0744325, volume20=5.28871e+06; 직전 완료 봉 목표를 다음 봉 시가에 모의 적용 |
| v2 | chaikin_3_10 | 9948.77 | -51.23 | sell / filled / ADL의 EMA3 - EMA10 > 0 그리고 종가 > EMA26; 조건 미충족; Chaikin3_10=-7287.74, ADL=2.55494e+07, close=178.275, EMA26=178.258; 직전 완료 봉 목표를 다음 봉 시가에 모의 적용 |
| v2 | roc_10_momentum | 9934.64 | -65.36 | sell / filled / 10봉 ROC > 1% 그리고 종가 > EMA26; 조건 미충족; ROC10_percent=0.782107, close=178.47, EMA26=176.891; 직전 완료 봉 목표를 다음 봉 시가에 모의 적용 |
| v2 | trix_15_trend | 9946.44 | -53.56 | sell / filled / 15봉 삼중 EMA의 1봉 변화율 TRIX > 0 그리고 종가 > EMA26; 조건 미충족; TRIX15_percent=0.0212551, close=178.14, EMA26=178.249; 직전 완료 봉 목표를 다음 봉 시가에 모의 적용 |
| v2 | keltner_20_breakout | 9931.34 | -68.66 | sell / filled / 종가 > EMA20 + 2 x Wilder ATR14; 조건 미충족; close=178.845, upper_Keltner=179.079, EMA20=177.884, ATR14=0.597175; 직전 완료 봉 목표를 다음 봉 시가에 모의 적용 |
| v2 | opening_range_30m | 10047.36 | 47.36 | sell / filled / 뉴욕 09:30·09:45 두 완료 봉 최고가를 10:00 이후 종가가 돌파; 자료 부족·변동폭 또는 거래량 없음: 대기; close=179.01; 직전 완료 봉 목표를 다음 봉 시가에 모의 적용 |

### 같은 기간의 비용·노출 비교 (사후 연구)

| 전략 | 비용 전 | 비용 후 | 100% 보유 | 같은 평균 노출 보유 | 평균 노출 |
|---|---:|---:|---:|---:|---:|
| cash | 0.00% | 0.00% | 8.50% | 0.00% | 0.00% |
| buy_hold | 8.96% | 8.50% | 8.50% | 8.50% | 100.00% |
| trend_8_26 | 1.08% | -3.49% | 8.50% | 5.81% | 69.39% |
| momentum_26 | 2.06% | -4.98% | 8.50% | 6.25% | 74.41% |
| breakout_8 | -0.52% | -18.68% | 8.50% | 2.23% | 27.18% |
| reversion_12 | 2.80% | -7.06% | 8.50% | 1.81% | 22.16% |
| volume_26 | 2.43% | -5.43% | 8.50% | 0.45% | 5.54% |
| trend_8_26 AND momentum_26 | -0.07% | -5.38% | 8.50% | 5.26% | 63.06% |
| trend_8_26 + momentum_26 | 1.57% | -4.03% | 8.50% | 6.03% | 71.90% |
| trend_8_26 AND breakout_8 | -0.36% | -15.77% | 8.50% | 1.79% | 21.90% |
| trend_8_26 + breakout_8 | 0.30% | -11.02% | 8.50% | 4.00% | 48.29% |
| trend_8_26 AND reversion_12 | -1.96% | -7.56% | 8.50% | 0.82% | 10.03% |
| trend_8_26 + reversion_12 | 1.96% | -5.09% | 8.50% | 3.79% | 45.78% |
| trend_8_26 AND volume_26 | 1.38% | -3.20% | 8.50% | 0.26% | 3.17% |
| trend_8_26 + volume_26 | 1.77% | -4.26% | 8.50% | 3.09% | 37.47% |
| momentum_26 AND breakout_8 | -0.66% | -18.11% | 8.50% | 2.12% | 25.86% |
| momentum_26 + breakout_8 | 0.79% | -12.08% | 8.50% | 4.22% | 50.80% |
| momentum_26 AND reversion_12 | -0.44% | -6.91% | 8.50% | 0.84% | 10.29% |
| momentum_26 + reversion_12 | 2.45% | -4.83% | 8.50% | 4.00% | 48.29% |
| momentum_26 AND volume_26 | 2.15% | -1.64% | 8.50% | 0.19% | 2.37% |
| momentum_26 + volume_26 | 2.27% | -4.00% | 8.50% | 3.30% | 39.98% |
| breakout_8 AND reversion_12 | 0.00% | 0.00% | 8.50% | 0.00% | 0.00% |
| breakout_8 + reversion_12 | 1.15% | -12.89% | 8.50% | 2.02% | 24.68% |
| breakout_8 AND volume_26 | 0.51% | -1.17% | 8.50% | 0.09% | 1.06% |
| breakout_8 + volume_26 | 0.96% | -11.38% | 8.50% | 1.34% | 16.37% |
| reversion_12 AND volume_26 | 0.29% | -2.62% | 8.50% | 0.17% | 2.11% |
| reversion_12 + volume_26 | 2.63% | -5.45% | 8.50% | 1.13% | 13.86% |
| ema_12_26 | 1.19% | -1.75% | 8.50% | 6.71% | 79.68% |
| macd_12_26_9 | 0.29% | -5.43% | 8.50% | 3.62% | 43.80% |
| rsi_14_recovery | -0.37% | -1.20% | 8.50% | 0.04% | 0.53% |
| bollinger_20_reentry | -1.07% | -3.94% | 8.50% | 0.15% | 1.85% |
| donchian_20 | -0.93% | -10.43% | 8.50% | 0.79% | 9.76% |
| atr_14_breakout | 0.47% | -8.01% | 8.50% | 0.47% | 5.80% |
| session_vwap | 1.85% | -9.07% | 8.50% | 5.56% | 66.49% |
| obv_20 | 2.79% | -5.49% | 8.50% | 4.11% | 49.60% |
| stochastic_14_3_recovery | 0.60% | -8.67% | 8.50% | 0.49% | 6.07% |
| mfi_14_recovery | -0.31% | -1.97% | 8.50% | 0.09% | 1.06% |
| adx_14_trend | 3.88% | 0.87% | 8.50% | 3.69% | 44.59% |
| aroon_25_trend | -3.42% | -10.08% | 8.50% | 2.98% | 36.15% |
| cci_20_momentum | 3.54% | -5.60% | 8.50% | 2.41% | 29.29% |
| williams_14_recovery | -1.09% | -7.13% | 8.50% | 0.32% | 3.96% |
| cmf_20_accumulation | 1.55% | -5.45% | 8.50% | 4.20% | 50.66% |
| chaikin_3_10 | 1.63% | -6.55% | 8.50% | 4.99% | 59.89% |
| roc_10_momentum | 0.80% | -5.36% | 8.50% | 1.07% | 13.19% |
| trix_15_trend | 0.95% | -5.21% | 8.50% | 5.65% | 67.55% |
| keltner_20_breakout | 0.18% | -6.72% | 8.50% | 1.42% | 17.41% |
| opening_range_30m | 0.43% | -9.20% | 8.50% | 2.93% | 35.62% |

동일 구간·초기 자금, 종료 시 청산 비용 포함. 노출 맞춤은 사후 설명용이며 v2 실제 계좌 성과가 아닙니다.
[낙폭 분해·비용 영향·전체 구간](XOM/comparison.json)

[v1 전체 기록](XOM/accounts.json) · [v2 전체 기록](XOM/accounts-v2.json)

## JNJ 계좌

| 모델 | 전략 | 평가액 USD | 손익 USD | 최근 매매·이유 |
|---|---|---:|---:|---|
| v1 | cash | 10000.00 | 0.00 | 대기 /  / 새 신호 대기 |
| v1 | buy_hold | 10137.82 | 137.82 | buy /  / buy_hold: prior completed bar target 100%; next bar open simulation |
| v1 | trend_8_26 | 10089.08 | 89.08 | buy /  / trend_8_26: prior completed bar target 100%; next bar open simulation |
| v1 | momentum_26 | 9859.33 | -140.67 | buy /  / momentum_26: prior completed bar target 100%; next bar open simulation |
| v1 | breakout_8 | 9513.91 | -486.09 | sell /  / breakout_8: prior completed bar target 0%; next bar open simulation |
| v1 | reversion_12 | 9891.56 | -108.44 | sell /  / reversion_12: prior completed bar target 0%; next bar open simulation |
| v1 | volume_26 | 9943.90 | -56.10 | sell /  / volume_26: prior completed bar target 0%; next bar open simulation |
| v1 | trend_8_26 AND momentum_26 | 9911.36 | -88.64 | buy /  / trend_8_26 AND momentum_26: prior completed bar target 100%; next bar open simulation |
| v1 | trend_8_26 + momentum_26 | 9973.84 | -26.16 | buy /  / trend_8_26 + momentum_26: prior completed bar target 100%; next bar open simulation |
| v1 | trend_8_26 AND breakout_8 | 9814.73 | -185.27 | sell /  / trend_8_26 AND breakout_8: prior completed bar target 0%; next bar open simulation |
| v1 | trend_8_26 + breakout_8 | 9817.14 | -182.86 | sell /  / trend_8_26 + breakout_8: prior completed bar target 50%; next bar open simulation |
| v1 | trend_8_26 AND reversion_12 | 9992.01 | -7.99 | sell /  / trend_8_26 AND reversion_12: prior completed bar target 0%; next bar open simulation |
| v1 | trend_8_26 + reversion_12 | 9989.96 | -10.04 | sell /  / trend_8_26 + reversion_12: prior completed bar target 50%; next bar open simulation |
| v1 | trend_8_26 AND volume_26 | 9995.12 | -4.88 | sell /  / trend_8_26 AND volume_26: prior completed bar target 0%; next bar open simulation |
| v1 | trend_8_26 + volume_26 | 10016.46 | 16.46 | sell /  / trend_8_26 + volume_26: prior completed bar target 50%; next bar open simulation |
| v1 | momentum_26 AND breakout_8 | 9833.49 | -166.51 | sell /  / momentum_26 AND breakout_8: prior completed bar target 0%; next bar open simulation |
| v1 | momentum_26 + breakout_8 | 9684.94 | -315.06 | sell /  / momentum_26 + breakout_8: prior completed bar target 50%; next bar open simulation |
| v1 | momentum_26 AND reversion_12 | 10000.00 | 0.00 | 대기 /  / 새 신호 대기 |
| v1 | momentum_26 + reversion_12 | 9895.08 | -104.92 | sell /  / momentum_26 + reversion_12: prior completed bar target 50%; next bar open simulation |
| v1 | momentum_26 AND volume_26 | 10000.00 | 0.00 | 대기 /  / 새 신호 대기 |
| v1 | momentum_26 + volume_26 | 9941.22 | -58.78 | sell /  / momentum_26 + volume_26: prior completed bar target 50%; next bar open simulation |
| v1 | breakout_8 AND reversion_12 | 10000.00 | 0.00 | 대기 /  / 새 신호 대기 |
| v1 | breakout_8 + reversion_12 | 9700.73 | -299.27 | sell /  / breakout_8 + reversion_12: prior completed bar target 0%; next bar open simulation |
| v1 | breakout_8 AND volume_26 | 10000.00 | 0.00 | 대기 /  / 새 신호 대기 |
| v1 | breakout_8 + volume_26 | 9745.99 | -254.01 | sell /  / breakout_8 + volume_26: prior completed bar target 0%; next bar open simulation |
| v1 | reversion_12 AND volume_26 | 9974.59 | -25.41 | sell /  / reversion_12 AND volume_26: prior completed bar target 0%; next bar open simulation |
| v1 | reversion_12 + volume_26 | 9937.59 | -62.41 | sell /  / reversion_12 + volume_26: prior completed bar target 0%; next bar open simulation |
| v1 | ema_12_26 | 9958.12 | -41.88 | buy /  / EMA12 > EMA26; 조건 충족; EMA12=253.915, EMA26=253.911 |
| v1 | macd_12_26_9 | 9932.92 | -67.08 | buy /  / MACD > 신호선 그리고 MACD > 0; 조건 충족; MACD=0.00413589, signal9=-0.236181 |
| v1 | rsi_14_recovery | 9923.04 | -76.96 | sell /  / 직전 RSI14 < 30, 현재 RSI14 >= 30 (한 봉 목표); 조건 미충족; RSI14=40.3665, previous_RSI14=36.2025 |
| v1 | bollinger_20_reentry | 9881.04 | -118.96 | sell /  / 직전 종가 < 직전 하단밴드, 현재 하단밴드 <= 종가 <= SMA20 (한 봉 목표); 조건 미충족; close=251.75, lower20=251.316, SMA20=254.208, previous_lower20=251.691 |
| v1 | donchian_20 | 9921.02 | -78.98 | sell /  / 종가 > 현재 봉을 제외한 직전 20봉 최고가; 조건 미충족; close=258.68, prior_high20=260.425 |
| v1 | atr_14_breakout | 9805.90 | -194.10 | sell /  / 종가 > 직전 종가 + 직전 ATR14 그리고 종가 > EMA26; 조건 미충족; close=258.68, threshold=261.221, prior_ATR14=1.00083, EMA26=254.754 |
| v1 | session_vwap | 9876.46 | -123.54 | buy /  / 종가 > 뉴욕 거래일별 누적 전형가격 VWAP; 조건 충족; close=259.535, session_VWAP=259.395, session_volume=3.8214e+06 |
| v1 | obv_20 | 9690.88 | -309.12 | buy /  / OBV > OBV의 SMA20 그리고 종가 > EMA26; 조건 충족; OBV=4.78456e+06, OBV_SMA20=3.4932e+06, close=254.04, EMA26=253.978 |
| v1 | stochastic_14_3_recovery | 9862.87 | -137.13 | sell /  / 직전 %K14 < 20에서 %K14가 %D3 상향 돌파 (한 봉 목표); 조건 미충족; K14=28.9392, D3=18.1738, previous_K14=19.7943, previous_D3=12.6561 |
| v1 | mfi_14_recovery | 10000.00 | 0.00 | 대기 /  / 새 신호 대기 |
| v1 | adx_14_trend | 9817.98 | -182.02 | buy /  / Wilder ADX14 >= 25 그리고 +DI14 > -DI14; 조건 충족; ADX14=27.0884, plus_DI14=47.0278, minus_DI14=11.4099 |
| v1 | aroon_25_trend | 9928.47 | -71.53 | buy /  / Aroon25 Up > 70 그리고 Down < 30 (동률이면 최신 극값); 조건 충족; Aroon_up=100, Aroon_down=16 |
| v1 | cci_20_momentum | 9818.66 | -181.34 | sell /  / CCI20 > 100 (전형가격·평균절대편차); 조건 미충족; CCI20=95.1073 |
| v1 | williams_14_recovery | 9903.67 | -96.33 | sell /  / 직전 Williams %R14 < -80, 현재 >= -80 (한 봉 목표); 조건 미충족; Williams_R14=-61.3372, previous_R14=-71.0608 |
| v1 | cmf_20_accumulation | 10264.97 | 264.97 | buy /  / Chaikin Money Flow20 > 0.1; 조건 충족; CMF20=0.280188, volume20=5.69706e+06 |
| v1 | chaikin_3_10 | 9910.17 | -89.83 | buy /  / ADL의 EMA3 - EMA10 > 0 그리고 종가 > EMA26; 조건 충족; Chaikin3_10=250777, ADL=4.30146e+06, close=254.04, EMA26=253.978 |
| v1 | roc_10_momentum | 9735.55 | -264.45 | buy /  / 10봉 ROC > 1% 그리고 종가 > EMA26; 조건 충족; ROC10_percent=2.42079, close=260.22, EMA26=254.44 |
| v1 | trix_15_trend | 9801.47 | -198.53 | buy /  / 15봉 삼중 EMA의 1봉 변화율 TRIX > 0 그리고 종가 > EMA26; 조건 충족; TRIX15_percent=0.000945132, close=260.22, EMA26=254.44 |
| v1 | keltner_20_breakout | 9960.84 | -39.16 | buy /  / 종가 > EMA20 + 2 x Wilder ATR14; 조건 충족; close=260.22, upper_Keltner=256.552, EMA20=254.551, ATR14=1.00083 |
| v1 | opening_range_30m | 10000.00 | 0.00 | 대기 /  / 새 신호 대기 |
| v2 | cash | 10000.00 | 0.00 | 대기 /  / 새 신호 대기 |
| v2 | buy_hold | 9901.21 | -98.79 | 중단: 손실 한도 / buy / partial / 직전 완료 봉 목표 비중 100%; 다음 봉 시가 가정 |
| v2 | trend_8_26 | 9901.21 | -98.79 | 중단: 손실 한도 / buy / partial / 직전 완료 봉 목표 비중 100%; 다음 봉 시가 가정 |
| v2 | momentum_26 | 9901.21 | -98.79 | 중단: 손실 한도 / buy / partial / 직전 완료 봉 목표 비중 100%; 다음 봉 시가 가정 |
| v2 | breakout_8 | 9343.39 | -656.61 | 중단: 손실 한도 / sell / filled / 직전 완료 봉 목표 비중 0%; 다음 봉 시가 가정 |
| v2 | reversion_12 | 9581.23 | -418.77 | sell / filled / 직전 완료 봉 목표 비중 0%; 다음 봉 시가 가정 |
| v2 | volume_26 | 9728.64 | -271.36 | sell / filled / 직전 완료 봉 목표 비중 0%; 다음 봉 시가 가정 |
| v2 | trend_8_26 AND momentum_26 | 9901.21 | -98.79 | 중단: 손실 한도 / buy / partial / 직전 완료 봉 목표 비중 100%; 다음 봉 시가 가정 |
| v2 | trend_8_26 + momentum_26 | 9901.21 | -98.79 | 중단: 손실 한도 / buy / partial / 직전 완료 봉 목표 비중 100%; 다음 봉 시가 가정 |
| v2 | trend_8_26 AND breakout_8 | 9419.39 | -580.61 | 중단: 손실 한도 / sell / filled / 직전 완료 봉 목표 비중 0%; 다음 봉 시가 가정 |
| v2 | trend_8_26 + breakout_8 | 9385.88 | -614.12 | sell / filled / 직전 완료 봉 목표 비중 50%; 다음 봉 시가 가정 |
| v2 | trend_8_26 AND reversion_12 | 9968.12 | -31.88 | sell / filled / 직전 완료 봉 목표 비중 0%; 다음 봉 시가 가정 |
| v2 | trend_8_26 + reversion_12 | 9732.92 | -267.08 | 중단: 손실 한도 / sell / filled / 직전 완료 봉 목표 비중 0%; 다음 봉 시가 가정 |
| v2 | trend_8_26 AND volume_26 | 9861.95 | -138.05 | sell / filled / 직전 완료 봉 목표 비중 0%; 다음 봉 시가 가정 |
| v2 | trend_8_26 + volume_26 | 9925.75 | -74.25 | 중단: 손실 한도 / buy / filled / 직전 완료 봉 목표 비중 50%; 다음 봉 시가 가정 |
| v2 | momentum_26 AND breakout_8 | 9435.09 | -564.91 | sell / filled / 직전 완료 봉 목표 비중 0%; 다음 봉 시가 가정 |
| v2 | momentum_26 + breakout_8 | 9249.87 | -750.13 | sell / filled / 직전 완료 봉 목표 비중 50%; 다음 봉 시가 가정 |
| v2 | momentum_26 AND reversion_12 | 9938.87 | -61.13 | sell / filled / 직전 완료 봉 목표 비중 0%; 다음 봉 시가 가정 |
| v2 | momentum_26 + reversion_12 | 9732.92 | -267.08 | 중단: 손실 한도 / sell / filled / 직전 완료 봉 목표 비중 0%; 다음 봉 시가 가정 |
| v2 | momentum_26 AND volume_26 | 9920.93 | -79.07 | sell / filled / 직전 완료 봉 목표 비중 0%; 다음 봉 시가 가정 |
| v2 | momentum_26 + volume_26 | 9925.75 | -74.25 | 중단: 손실 한도 / buy / filled / 직전 완료 봉 목표 비중 50%; 다음 봉 시가 가정 |
| v2 | breakout_8 AND reversion_12 | 10000.00 | 0.00 | 대기 /  / 새 신호 대기 |
| v2 | breakout_8 + reversion_12 | 9284.10 | -715.90 | sell / filled / 직전 완료 봉 목표 비중 0%; 다음 봉 시가 가정 |
| v2 | breakout_8 AND volume_26 | 9814.17 | -185.83 | sell / filled / 직전 완료 봉 목표 비중 0%; 다음 봉 시가 가정 |
| v2 | breakout_8 + volume_26 | 9355.32 | -644.68 | sell / filled / 직전 완료 봉 목표 비중 0%; 다음 봉 시가 가정 |
| v2 | reversion_12 AND volume_26 | 9859.15 | -140.85 | sell / filled / 직전 완료 봉 목표 비중 0%; 다음 봉 시가 가정 |
| v2 | reversion_12 + volume_26 | 9695.58 | -304.42 | sell / filled / 직전 완료 봉 목표 비중 0%; 다음 봉 시가 가정 |
| v2 | ema_12_26 | 9953.14 | -46.86 | buy / partial / EMA12 > EMA26; 조건 충족; EMA12=253.915, EMA26=253.911; 직전 완료 봉 목표를 다음 봉 시가에 모의 적용 |
| v2 | macd_12_26_9 | 9927.95 | -72.05 | buy / partial / MACD > 신호선 그리고 MACD > 0; 조건 충족; MACD=0.00413589, signal9=-0.236181; 직전 완료 봉 목표를 다음 봉 시가에 모의 적용 |
| v2 | rsi_14_recovery | 9919.07 | -80.93 | sell / filled / 직전 RSI14 < 30, 현재 RSI14 >= 30 (한 봉 목표); 조건 미충족; RSI14=40.3665, previous_RSI14=36.2025; 직전 완료 봉 목표를 다음 봉 시가에 모의 적용 |
| v2 | bollinger_20_reentry | 9877.09 | -122.91 | sell / filled / 직전 종가 < 직전 하단밴드, 현재 하단밴드 <= 종가 <= SMA20 (한 봉 목표); 조건 미충족; close=251.75, lower20=251.316, SMA20=254.208, previous_lower20=251.691; 직전 완료 봉 목표를 다음 봉 시가에 모의 적용 |
| v2 | donchian_20 | 9919.03 | -80.97 | sell / filled / 종가 > 현재 봉을 제외한 직전 20봉 최고가; 조건 미충족; close=258.68, prior_high20=260.425; 직전 완료 봉 목표를 다음 봉 시가에 모의 적용 |
| v2 | atr_14_breakout | 9800.02 | -199.98 | sell / filled / 종가 > 직전 종가 + 직전 ATR14 그리고 종가 > EMA26; 조건 미충족; close=258.68, threshold=261.221, prior_ATR14=1.00083, EMA26=254.754; 직전 완료 봉 목표를 다음 봉 시가에 모의 적용 |
| v2 | session_vwap | 9863.63 | -136.37 | buy / partial / 종가 > 뉴욕 거래일별 누적 전형가격 VWAP; 조건 충족; close=259.535, session_VWAP=259.395, session_volume=3.8214e+06; 직전 완료 봉 목표를 다음 봉 시가에 모의 적용 |
| v2 | obv_20 | 9678.29 | -321.71 | buy / partial / OBV > OBV의 SMA20 그리고 종가 > EMA26; 조건 충족; OBV=4.78456e+06, OBV_SMA20=3.4932e+06, close=254.04, EMA26=253.978; 직전 완료 봉 목표를 다음 봉 시가에 모의 적용 |
| v2 | stochastic_14_3_recovery | 9856.96 | -143.04 | sell / filled / 직전 %K14 < 20에서 %K14가 %D3 상향 돌파 (한 봉 목표); 조건 미충족; K14=28.9392, D3=18.1738, previous_K14=19.7943, previous_D3=12.6561; 직전 완료 봉 목표를 다음 봉 시가에 모의 적용 |
| v2 | mfi_14_recovery | 10000.00 | 0.00 | 대기 /  / 새 신호 대기 |
| v2 | adx_14_trend | 9811.11 | -188.89 | buy / partial / Wilder ADX14 >= 25 그리고 +DI14 > -DI14; 조건 충족; ADX14=27.0884, plus_DI14=47.0278, minus_DI14=11.4099; 직전 완료 봉 목표를 다음 봉 시가에 모의 적용 |
| v2 | aroon_25_trend | 9925.49 | -74.51 | buy / partial / Aroon25 Up > 70 그리고 Down < 30 (동률이면 최신 극값); 조건 충족; Aroon_up=100, Aroon_down=16; 직전 완료 봉 목표를 다음 봉 시가에 모의 적용 |
| v2 | cci_20_momentum | 9812.77 | -187.23 | sell / filled / CCI20 > 100 (전형가격·평균절대편차); 조건 미충족; CCI20=95.1073; 직전 완료 봉 목표를 다음 봉 시가에 모의 적용 |
| v2 | williams_14_recovery | 9899.71 | -100.29 | sell / filled / 직전 Williams %R14 < -80, 현재 >= -80 (한 봉 목표); 조건 미충족; Williams_R14=-61.3372, previous_R14=-71.0608; 직전 완료 봉 목표를 다음 봉 시가에 모의 적용 |
| v2 | cmf_20_accumulation | 10263.94 | 263.94 | buy / partial / Chaikin Money Flow20 > 0.1; 조건 충족; CMF20=0.280188, volume20=5.69706e+06; 직전 완료 봉 목표를 다음 봉 시가에 모의 적용 |
| v2 | chaikin_3_10 | 9903.24 | -96.76 | buy / partial / ADL의 EMA3 - EMA10 > 0 그리고 종가 > EMA26; 조건 충족; Chaikin3_10=250777, ADL=4.30146e+06, close=254.04, EMA26=253.978; 직전 완료 봉 목표를 다음 봉 시가에 모의 적용 |
| v2 | roc_10_momentum | 9728.74 | -271.26 | buy / partial / 10봉 ROC > 1% 그리고 종가 > EMA26; 조건 충족; ROC10_percent=2.42079, close=260.22, EMA26=254.44; 직전 완료 봉 목표를 다음 봉 시가에 모의 적용 |
| v2 | trix_15_trend | 9796.57 | -203.43 | buy / partial / 15봉 삼중 EMA의 1봉 변화율 TRIX > 0 그리고 종가 > EMA26; 조건 충족; TRIX15_percent=0.000945132, close=260.22, EMA26=254.44; 직전 완료 봉 목표를 다음 봉 시가에 모의 적용 |
| v2 | keltner_20_breakout | 9959.85 | -40.15 | buy / partial / 종가 > EMA20 + 2 x Wilder ATR14; 조건 충족; close=260.22, upper_Keltner=256.552, EMA20=254.551, ATR14=1.00083; 직전 완료 봉 목표를 다음 봉 시가에 모의 적용 |
| v2 | opening_range_30m | 10000.00 | 0.00 | 대기 /  / 새 신호 대기 |

### 같은 기간의 비용·노출 비교 (사후 연구)

| 전략 | 비용 전 | 비용 후 | 100% 보유 | 같은 평균 노출 보유 | 평균 노출 |
|---|---:|---:|---:|---:|---:|
| cash | 0.00% | 0.00% | -3.21% | -0.00% | 0.00% |
| buy_hold | -2.80% | -3.21% | -3.21% | -3.21% | 100.00% |
| trend_8_26 | 3.42% | 0.85% | -3.21% | -1.57% | 48.02% |
| momentum_26 | 0.02% | -3.69% | -3.21% | -1.49% | 45.38% |
| breakout_8 | -1.40% | -18.38% | -3.21% | -0.67% | 20.32% |
| reversion_12 | -7.05% | -14.54% | -3.21% | -0.99% | 30.08% |
| volume_26 | -0.92% | -7.75% | -3.21% | -0.22% | 6.60% |
| trend_8_26 AND momentum_26 | 1.28% | -2.06% | -3.21% | -1.32% | 40.11% |
| trend_8_26 + momentum_26 | 1.72% | -1.44% | -3.21% | -1.53% | 46.70% |
| trend_8_26 AND breakout_8 | 0.12% | -11.73% | -3.21% | -0.46% | 13.72% |
| trend_8_26 + breakout_8 | 1.01% | -9.06% | -3.21% | -1.13% | 34.18% |
| trend_8_26 AND reversion_12 | 0.87% | -2.05% | -3.21% | -0.18% | 5.28% |
| trend_8_26 + reversion_12 | -1.92% | -6.77% | -3.21% | -1.28% | 39.05% |
| trend_8_26 AND volume_26 | 1.42% | -1.10% | -3.21% | -0.05% | 1.58% |
| trend_8_26 + volume_26 | 1.26% | -3.33% | -3.21% | -0.90% | 27.31% |
| momentum_26 AND breakout_8 | 0.98% | -9.84% | -3.21% | -0.43% | 12.93% |
| momentum_26 + breakout_8 | -0.67% | -11.13% | -3.21% | -1.08% | 32.86% |
| momentum_26 AND reversion_12 | -0.82% | -2.88% | -3.21% | -0.18% | 5.54% |
| momentum_26 + reversion_12 | -3.55% | -8.70% | -3.21% | -1.24% | 37.73% |
| momentum_26 AND volume_26 | 0.14% | -0.70% | -3.21% | -0.02% | 0.53% |
| momentum_26 + volume_26 | -0.41% | -4.73% | -3.21% | -0.86% | 25.99% |
| breakout_8 AND reversion_12 | 0.00% | 0.00% | -3.21% | -0.00% | 0.00% |
| breakout_8 + reversion_12 | -4.25% | -15.96% | -3.21% | -0.83% | 25.21% |
| breakout_8 AND volume_26 | -0.91% | -2.15% | -3.21% | -0.03% | 0.79% |
| breakout_8 + volume_26 | -1.15% | -12.31% | -3.21% | -0.45% | 13.46% |
| reversion_12 AND volume_26 | -1.84% | -4.69% | -3.21% | -0.10% | 2.90% |
| reversion_12 + volume_26 | -4.02% | -10.46% | -3.21% | -0.61% | 18.34% |
| ema_12_26 | 0.65% | -1.85% | -3.21% | -1.37% | 41.69% |
| macd_12_26_9 | 6.10% | 3.03% | -3.21% | -0.94% | 28.50% |
| rsi_14_recovery | -1.35% | -6.20% | -3.21% | -0.11% | 3.17% |
| bollinger_20_reentry | -1.10% | -5.56% | -3.21% | -0.10% | 2.90% |
| donchian_20 | 0.23% | -7.07% | -3.21% | -0.23% | 6.86% |
| atr_14_breakout | 0.79% | -5.36% | -3.21% | -0.16% | 4.75% |
| session_vwap | 3.63% | -4.72% | -3.21% | -1.61% | 49.08% |
| obv_20 | -5.26% | -14.35% | -3.21% | -1.10% | 33.25% |
| stochastic_14_3_recovery | -0.31% | -12.11% | -3.21% | -0.26% | 7.92% |
| mfi_14_recovery | 0.33% | -0.93% | -3.21% | -0.03% | 0.79% |
| adx_14_trend | -2.42% | -7.61% | -3.21% | -1.08% | 32.72% |
| aroon_25_trend | 3.90% | -0.37% | -3.21% | -0.98% | 29.55% |
| cci_20_momentum | 0.20% | -6.70% | -3.21% | -0.73% | 21.90% |
| williams_14_recovery | -1.58% | -8.74% | -3.21% | -0.16% | 4.75% |
| cmf_20_accumulation | 5.48% | 1.57% | -3.21% | -0.99% | 30.08% |
| chaikin_3_10 | -2.64% | -7.81% | -3.21% | -1.14% | 34.56% |
| roc_10_momentum | -2.55% | -9.26% | -3.21% | -0.57% | 17.15% |
| trix_15_trend | -0.42% | -2.90% | -3.21% | -1.03% | 31.13% |
| keltner_20_breakout | 0.45% | -3.27% | -3.21% | -0.38% | 11.35% |
| opening_range_30m | 0.79% | -2.95% | -3.21% | -0.86% | 26.12% |

동일 구간·초기 자금, 종료 시 청산 비용 포함. 노출 맞춤은 사후 설명용이며 v2 실제 계좌 성과가 아닙니다.
[낙폭 분해·비용 영향·전체 구간](JNJ/comparison.json)

[v1 전체 기록](JNJ/accounts.json) · [v2 전체 기록](JNJ/accounts-v2.json)

## CAT 계좌

| 모델 | 전략 | 평가액 USD | 손익 USD | 최근 매매·이유 |
|---|---|---:|---:|---|
| v1 | cash | 10000.00 | 0.00 | 대기 /  / 새 신호 대기 |
| v1 | buy_hold | 9858.94 | -141.06 | buy /  / buy_hold: prior completed bar target 100%; next bar open simulation |
| v1 | trend_8_26 | 9909.54 | -90.46 | sell /  / trend_8_26: prior completed bar target 0%; next bar open simulation |
| v1 | momentum_26 | 9765.06 | -234.94 | sell /  / momentum_26: prior completed bar target 0%; next bar open simulation |
| v1 | breakout_8 | 9687.36 | -312.64 | sell /  / breakout_8: prior completed bar target 0%; next bar open simulation |
| v1 | reversion_12 | 9927.33 | -72.67 | sell /  / reversion_12: prior completed bar target 0%; next bar open simulation |
| v1 | volume_26 | 10041.67 | 41.67 | sell /  / volume_26: prior completed bar target 0%; next bar open simulation |
| v1 | trend_8_26 AND momentum_26 | 9873.91 | -126.09 | sell /  / trend_8_26 AND momentum_26: prior completed bar target 0%; next bar open simulation |
| v1 | trend_8_26 + momentum_26 | 9837.24 | -162.76 | sell /  / trend_8_26 + momentum_26: prior completed bar target 0%; next bar open simulation |
| v1 | trend_8_26 AND breakout_8 | 9850.32 | -149.68 | sell /  / trend_8_26 AND breakout_8: prior completed bar target 0%; next bar open simulation |
| v1 | trend_8_26 + breakout_8 | 9797.99 | -202.01 | sell /  / trend_8_26 + breakout_8: prior completed bar target 0%; next bar open simulation |
| v1 | trend_8_26 AND reversion_12 | 9928.06 | -71.94 | sell /  / trend_8_26 AND reversion_12: prior completed bar target 0%; next bar open simulation |
| v1 | trend_8_26 + reversion_12 | 9939.01 | -60.99 | sell /  / trend_8_26 + reversion_12: prior completed bar target 0%; next bar open simulation |
| v1 | trend_8_26 AND volume_26 | 10000.00 | 0.00 | 대기 /  / 새 신호 대기 |
| v1 | trend_8_26 + volume_26 | 9975.46 | -24.54 | sell /  / trend_8_26 + volume_26: prior completed bar target 0%; next bar open simulation |
| v1 | momentum_26 AND breakout_8 | 9804.82 | -195.18 | sell /  / momentum_26 AND breakout_8: prior completed bar target 0%; next bar open simulation |
| v1 | momentum_26 + breakout_8 | 9726.19 | -273.81 | sell /  / momentum_26 + breakout_8: prior completed bar target 0%; next bar open simulation |
| v1 | momentum_26 AND reversion_12 | 9887.21 | -112.79 | sell /  / momentum_26 AND reversion_12: prior completed bar target 0%; next bar open simulation |
| v1 | momentum_26 + reversion_12 | 9846.60 | -153.40 | sell /  / momentum_26 + reversion_12: prior completed bar target 0%; next bar open simulation |
| v1 | momentum_26 AND volume_26 | 9985.43 | -14.57 | sell /  / momentum_26 AND volume_26: prior completed bar target 0%; next bar open simulation |
| v1 | momentum_26 + volume_26 | 9902.49 | -97.51 | sell /  / momentum_26 + volume_26: prior completed bar target 0%; next bar open simulation |
| v1 | breakout_8 AND reversion_12 | 10000.00 | 0.00 | 대기 /  / 새 신호 대기 |
| v1 | breakout_8 + reversion_12 | 9807.18 | -192.82 | sell /  / breakout_8 + reversion_12: prior completed bar target 0%; next bar open simulation |
| v1 | breakout_8 AND volume_26 | 9985.43 | -14.57 | sell /  / breakout_8 AND volume_26: prior completed bar target 0%; next bar open simulation |
| v1 | breakout_8 + volume_26 | 9862.94 | -137.06 | sell /  / breakout_8 + volume_26: prior completed bar target 0%; next bar open simulation |
| v1 | reversion_12 AND volume_26 | 10046.29 | 46.29 | sell /  / reversion_12 AND volume_26: prior completed bar target 0%; next bar open simulation |
| v1 | reversion_12 + volume_26 | 9984.87 | -15.13 | sell /  / reversion_12 + volume_26: prior completed bar target 0%; next bar open simulation |
| v1 | ema_12_26 | 9862.47 | -137.53 | sell /  / EMA12 > EMA26; 조건 미충족; EMA12=735.622, EMA26=735.711 |
| v1 | macd_12_26_9 | 9904.18 | -95.82 | sell /  / MACD > 신호선 그리고 MACD > 0; 조건 미충족; MACD=0.746548, signal9=0.752293 |
| v1 | rsi_14_recovery | 9999.22 | -0.78 | sell /  / 직전 RSI14 < 30, 현재 RSI14 >= 30 (한 봉 목표); 조건 미충족; RSI14=43.621, previous_RSI14=38.5787 |
| v1 | bollinger_20_reentry | 9777.09 | -222.91 | sell /  / 직전 종가 < 직전 하단밴드, 현재 하단밴드 <= 종가 <= SMA20 (한 봉 목표); 조건 미충족; close=721.16, lower20=716.851, SMA20=725.821, previous_lower20=717.276 |
| v1 | donchian_20 | 9950.83 | -49.17 | sell /  / 종가 > 현재 봉을 제외한 직전 20봉 최고가; 조건 미충족; close=739.81, prior_high20=742.28 |
| v1 | atr_14_breakout | 9775.74 | -224.26 | sell /  / 종가 > 직전 종가 + 직전 ATR14 그리고 종가 > EMA26; 조건 미충족; close=732.42, threshold=735.931, prior_ATR14=4.99094, EMA26=726.612 |
| v1 | session_vwap | 9442.12 | -557.88 | buy /  / 종가 > 뉴욕 거래일별 누적 전형가격 VWAP; 조건 충족; close=717.87, session_VWAP=713.405, session_volume=283277 |
| v1 | obv_20 | 9683.67 | -316.33 | sell /  / OBV > OBV의 SMA20 그리고 종가 > EMA26; 조건 미충족; OBV=-5.85317e+06, OBV_SMA20=-5.80449e+06, close=725.22, EMA26=726.751 |
| v1 | stochastic_14_3_recovery | 9855.08 | -144.92 | sell /  / 직전 %K14 < 20에서 %K14가 %D3 상향 돌파 (한 봉 목표); 조건 미충족; K14=59.6496, D3=39.2535, previous_K14=43.8356, previous_D3=33.8642 |
| v1 | mfi_14_recovery | 10068.63 | 68.63 | sell /  / 직전 MFI14 < 20, 현재 MFI14 >= 20 (한 봉 목표); 조건 미충족; MFI14=32.7313, previous_MFI14=24.1736 |
| v1 | adx_14_trend | 10000.00 | 0.00 | 대기 /  / 새 신호 대기 |
| v1 | aroon_25_trend | 10031.15 | 31.15 | sell /  / Aroon25 Up > 70 그리고 Down < 30 (동률이면 최신 극값); 조건 미충족; Aroon_up=88, Aroon_down=48 |
| v1 | cci_20_momentum | 9890.31 | -109.69 | sell /  / CCI20 > 100 (전형가격·평균절대편차); 조건 미충족; CCI20=20.3547 |
| v1 | williams_14_recovery | 10007.06 | 7.06 | sell /  / 직전 Williams %R14 < -80, 현재 >= -80 (한 봉 목표); 조건 미충족; Williams_R14=-40.3504, previous_R14=-56.1644 |
| v1 | cmf_20_accumulation | 9805.83 | -194.17 | sell /  / Chaikin Money Flow20 > 0.1; 조건 미충족; CMF20=-0.00568846, volume20=1.09018e+06 |
| v1 | chaikin_3_10 | 9474.17 | -525.83 | sell /  / ADL의 EMA3 - EMA10 > 0 그리고 종가 > EMA26; 조건 미충족; Chaikin3_10=39681.6, ADL=-6.22839e+06, close=725.22, EMA26=726.751 |
| v1 | roc_10_momentum | 9963.13 | -36.87 | sell /  / 10봉 ROC > 1% 그리고 종가 > EMA26; 조건 미충족; ROC10_percent=-0.134597, close=734.53, EMA26=735.486 |
| v1 | trix_15_trend | 9669.78 | -330.22 | sell /  / 15봉 삼중 EMA의 1봉 변화율 TRIX > 0 그리고 종가 > EMA26; 조건 미충족; TRIX15_percent=0.0186631, close=734.925, EMA26=736.093 |
| v1 | keltner_20_breakout | 10000.00 | 0.00 | 대기 /  / 새 신호 대기 |
| v1 | opening_range_30m | 10073.71 | 73.71 | buy /  / 뉴욕 09:30·09:45 두 완료 봉 최고가를 10:00 이후 종가가 돌파; 조건 충족; close=721.16, opening_high=718.07 |
| v2 | cash | 10000.00 | 0.00 | 대기 /  / 새 신호 대기 |
| v2 | buy_hold | 9067.02 | -932.98 | 중단: 손실 한도 / buy / partial / 직전 완료 봉 목표 비중 100%; 다음 봉 시가 가정 |
| v2 | trend_8_26 | 9831.00 | -169.00 | sell / filled / 직전 완료 봉 목표 비중 0%; 다음 봉 시가 가정 |
| v2 | momentum_26 | 9775.40 | -224.60 | sell / filled / 직전 완료 봉 목표 비중 0%; 다음 봉 시가 가정 |
| v2 | breakout_8 | 9506.39 | -493.61 | sell / filled / 직전 완료 봉 목표 비중 0%; 다음 봉 시가 가정 |
| v2 | reversion_12 | 8940.40 | -1059.60 | 중단: 손실 한도 / buy / partial / 직전 완료 봉 목표 비중 100%; 다음 봉 시가 가정 |
| v2 | volume_26 | 9196.08 | -803.92 | 중단: 손실 한도 / buy / partial / 직전 완료 봉 목표 비중 100%; 다음 봉 시가 가정 |
| v2 | trend_8_26 AND momentum_26 | 9914.96 | -85.04 | sell / filled / 직전 완료 봉 목표 비중 0%; 다음 봉 시가 가정 |
| v2 | trend_8_26 + momentum_26 | 9803.36 | -196.64 | sell / filled / 직전 완료 봉 목표 비중 0%; 다음 봉 시가 가정 |
| v2 | trend_8_26 AND breakout_8 | 9765.08 | -234.92 | sell / filled / 직전 완료 봉 목표 비중 0%; 다음 봉 시가 가정 |
| v2 | trend_8_26 + breakout_8 | 9667.77 | -332.23 | sell / filled / 직전 완료 봉 목표 비중 0%; 다음 봉 시가 가정 |
| v2 | trend_8_26 AND reversion_12 | 9738.62 | -261.38 | sell / filled / 직전 완료 봉 목표 비중 0%; 다음 봉 시가 가정 |
| v2 | trend_8_26 + reversion_12 | 9557.86 | -442.14 | sell / filled / 직전 완료 봉 목표 비중 0%; 다음 봉 시가 가정 |
| v2 | trend_8_26 AND volume_26 | 10035.44 | 35.44 | sell / filled / 직전 완료 봉 목표 비중 0%; 다음 봉 시가 가정 |
| v2 | trend_8_26 + volume_26 | 9605.55 | -394.45 | sell / filled / 직전 완료 봉 목표 비중 0%; 다음 봉 시가 가정 |
| v2 | momentum_26 AND breakout_8 | 9776.83 | -223.17 | sell / filled / 직전 완료 봉 목표 비중 0%; 다음 봉 시가 가정 |
| v2 | momentum_26 + breakout_8 | 9640.20 | -359.80 | sell / filled / 직전 완료 봉 목표 비중 0%; 다음 봉 시가 가정 |
| v2 | momentum_26 AND reversion_12 | 9755.55 | -244.45 | sell / filled / 직전 완료 봉 목표 비중 0%; 다음 봉 시가 가정 |
| v2 | momentum_26 + reversion_12 | 9510.81 | -489.19 | sell / filled / 직전 완료 봉 목표 비중 0%; 다음 봉 시가 가정 |
| v2 | momentum_26 AND volume_26 | 10032.13 | 32.13 | sell / filled / 직전 완료 봉 목표 비중 0%; 다음 봉 시가 가정 |
| v2 | momentum_26 + volume_26 | 9598.50 | -401.50 | sell / filled / 직전 완료 봉 목표 비중 0%; 다음 봉 시가 가정 |
| v2 | breakout_8 AND reversion_12 | 10000.00 | 0.00 | 대기 /  / 새 신호 대기 |
| v2 | breakout_8 + reversion_12 | 9610.18 | -389.82 | 중단: 손실 한도 / sell / filled / 직전 완료 봉 목표 비중 0%; 다음 봉 시가 가정 |
| v2 | breakout_8 AND volume_26 | 9982.12 | -17.88 | sell / filled / 직전 완료 봉 목표 비중 0%; 다음 봉 시가 가정 |
| v2 | breakout_8 + volume_26 | 9465.60 | -534.40 | sell / filled / 직전 완료 봉 목표 비중 0%; 다음 봉 시가 가정 |
| v2 | reversion_12 AND volume_26 | 9132.47 | -867.53 | 중단: 손실 한도 / buy / partial / 직전 완료 봉 목표 비중 100%; 다음 봉 시가 가정 |
| v2 | reversion_12 + volume_26 | 9332.30 | -667.70 | 중단: 손실 한도 / sell / filled / 직전 완료 봉 목표 비중 50%; 다음 봉 시가 가정 |
| v2 | ema_12_26 | 9860.50 | -139.50 | sell / filled / EMA12 > EMA26; 조건 미충족; EMA12=735.622, EMA26=735.711; 직전 완료 봉 목표를 다음 봉 시가에 모의 적용 |
| v2 | macd_12_26_9 | 9902.20 | -97.80 | sell / filled / MACD > 신호선 그리고 MACD > 0; 조건 미충족; MACD=0.746548, signal9=0.752293; 직전 완료 봉 목표를 다음 봉 시가에 모의 적용 |
| v2 | rsi_14_recovery | 9995.22 | -4.78 | sell / filled / 직전 RSI14 < 30, 현재 RSI14 >= 30 (한 봉 목표); 조건 미충족; RSI14=43.621, previous_RSI14=38.5787; 직전 완료 봉 목표를 다음 봉 시가에 모의 적용 |
| v2 | bollinger_20_reentry | 9771.22 | -228.78 | sell / filled / 직전 종가 < 직전 하단밴드, 현재 하단밴드 <= 종가 <= SMA20 (한 봉 목표); 조건 미충족; close=721.16, lower20=716.851, SMA20=725.821, previous_lower20=717.276; 직전 완료 봉 목표를 다음 봉 시가에 모의 적용 |
| v2 | donchian_20 | 9948.84 | -51.16 | sell / filled / 종가 > 현재 봉을 제외한 직전 20봉 최고가; 조건 미충족; close=739.81, prior_high20=742.28; 직전 완료 봉 목표를 다음 봉 시가에 모의 적용 |
| v2 | atr_14_breakout | 9767.92 | -232.08 | sell / filled / 종가 > 직전 종가 + 직전 ATR14 그리고 종가 > EMA26; 조건 미충족; close=732.42, threshold=735.931, prior_ATR14=4.99094, EMA26=726.612; 직전 완료 봉 목표를 다음 봉 시가에 모의 적용 |
| v2 | session_vwap | 9427.97 | -572.03 | buy / partial / 종가 > 뉴욕 거래일별 누적 전형가격 VWAP; 조건 충족; close=717.87, session_VWAP=713.405, session_volume=283277; 직전 완료 봉 목표를 다음 봉 시가에 모의 적용 |
| v2 | obv_20 | 9675.93 | -324.07 | sell / filled / OBV > OBV의 SMA20 그리고 종가 > EMA26; 조건 미충족; OBV=-5.85317e+06, OBV_SMA20=-5.80449e+06, close=725.22, EMA26=726.751; 직전 완료 봉 목표를 다음 봉 시가에 모의 적용 |
| v2 | stochastic_14_3_recovery | 9843.26 | -156.74 | sell / filled / 직전 %K14 < 20에서 %K14가 %D3 상향 돌파 (한 봉 목표); 조건 미충족; K14=59.6496, D3=39.2535, previous_K14=43.8356, previous_D3=33.8642; 직전 완료 봉 목표를 다음 봉 시가에 모의 적용 |
| v2 | mfi_14_recovery | 10064.61 | 64.61 | sell / filled / 직전 MFI14 < 20, 현재 MFI14 >= 20 (한 봉 목표); 조건 미충족; MFI14=32.7313, previous_MFI14=24.1736; 직전 완료 봉 목표를 다음 봉 시가에 모의 적용 |
| v2 | adx_14_trend | 10000.00 | 0.00 | 대기 /  / 새 신호 대기 |
| v2 | aroon_25_trend | 10029.14 | 29.14 | sell / filled / Aroon25 Up > 70 그리고 Down < 30 (동률이면 최신 극값); 조건 미충족; Aroon_up=88, Aroon_down=48; 직전 완료 봉 목표를 다음 봉 시가에 모의 적용 |
| v2 | cci_20_momentum | 9886.36 | -113.64 | sell / filled / CCI20 > 100 (전형가격·평균절대편차); 조건 미충족; CCI20=20.3547; 직전 완료 봉 목표를 다음 봉 시가에 모의 적용 |
| v2 | williams_14_recovery | 9999.06 | -0.94 | sell / filled / 직전 Williams %R14 < -80, 현재 >= -80 (한 봉 목표); 조건 미충족; Williams_R14=-40.3504, previous_R14=-56.1644; 직전 완료 봉 목표를 다음 봉 시가에 모의 적용 |
| v2 | cmf_20_accumulation | 9799.95 | -200.05 | sell / filled / Chaikin Money Flow20 > 0.1; 조건 미충족; CMF20=-0.00568846, volume20=1.09018e+06; 직전 완료 봉 목표를 다음 봉 시가에 모의 적용 |
| v2 | chaikin_3_10 | 9548.90 | -451.10 | 중단: 손실 한도 / buy / partial / ADL의 EMA3 - EMA10 > 0 그리고 종가 > EMA26; 조건 충족; Chaikin3_10=293683, ADL=-4.91156e+06, close=739.58, EMA26=736.187; 직전 완료 봉 목표를 다음 봉 시가에 모의 적용 |
| v2 | roc_10_momentum | 9961.14 | -38.86 | sell / filled / 10봉 ROC > 1% 그리고 종가 > EMA26; 조건 미충족; ROC10_percent=-0.134597, close=734.53, EMA26=735.486; 직전 완료 봉 목표를 다음 봉 시가에 모의 적용 |
| v2 | trix_15_trend | 9558.52 | -441.48 | 중단: 손실 한도 / buy / partial / 15봉 삼중 EMA의 1봉 변화율 TRIX > 0 그리고 종가 > EMA26; 조건 충족; TRIX15_percent=0.0196284, close=739.58, EMA26=736.187; 직전 완료 봉 목표를 다음 봉 시가에 모의 적용 |
| v2 | keltner_20_breakout | 10000.00 | 0.00 | 대기 /  / 새 신호 대기 |
| v2 | opening_range_30m | 10070.68 | 70.68 | buy / partial / 뉴욕 09:30·09:45 두 완료 봉 최고가를 10:00 이후 종가가 돌파; 조건 충족; close=721.16, opening_high=718.07; 직전 완료 봉 목표를 다음 봉 시가에 모의 적용 |

### 같은 기간의 비용·노출 비교 (사후 연구)

| 전략 | 비용 전 | 비용 후 | 100% 보유 | 같은 평균 노출 보유 | 평균 노출 |
|---|---:|---:|---:|---:|---:|
| cash | 0.00% | 0.00% | -12.25% | -0.00% | 0.00% |
| buy_hold | -11.89% | -12.25% | -12.25% | -12.25% | 100.00% |
| trend_8_26 | -0.50% | -3.79% | -12.25% | -5.45% | 43.54% |
| momentum_26 | -2.76% | -6.36% | -12.25% | -5.36% | 42.74% |
| breakout_8 | -3.26% | -15.43% | -12.25% | -1.77% | 13.98% |
| reversion_12 | -3.10% | -15.99% | -12.25% | -3.52% | 27.97% |
| volume_26 | -2.18% | -8.92% | -12.25% | -1.00% | 7.92% |
| trend_8_26 AND momentum_26 | 0.99% | -1.52% | -12.25% | -4.71% | 37.47% |
| trend_8_26 + momentum_26 | -1.62% | -5.08% | -12.25% | -5.41% | 43.14% |
| trend_8_26 AND breakout_8 | -1.65% | -8.04% | -12.25% | -0.87% | 6.86% |
| trend_8_26 + breakout_8 | -1.86% | -9.58% | -12.25% | -3.62% | 28.77% |
| trend_8_26 AND reversion_12 | 0.04% | -6.07% | -12.25% | -0.77% | 6.07% |
| trend_8_26 + reversion_12 | -1.74% | -9.50% | -12.25% | -4.49% | 35.76% |
| trend_8_26 AND volume_26 | 1.79% | 0.09% | -12.25% | -0.20% | 1.58% |
| trend_8_26 + volume_26 | -1.29% | -6.17% | -12.25% | -3.25% | 25.73% |
| momentum_26 AND breakout_8 | -2.28% | -9.01% | -12.25% | -0.90% | 7.12% |
| momentum_26 + breakout_8 | -2.97% | -10.98% | -12.25% | -3.57% | 28.37% |
| momentum_26 AND reversion_12 | -3.16% | -8.69% | -12.25% | -0.74% | 5.80% |
| momentum_26 + reversion_12 | -2.87% | -10.54% | -12.25% | -4.44% | 35.36% |
| momentum_26 AND volume_26 | 1.75% | 0.06% | -12.25% | -0.17% | 1.32% |
| momentum_26 + volume_26 | -2.41% | -7.23% | -12.25% | -3.20% | 25.33% |
| breakout_8 AND reversion_12 | 0.00% | 0.00% | -12.25% | -0.00% | 0.00% |
| breakout_8 + reversion_12 | -3.12% | -14.80% | -12.25% | -2.65% | 20.98% |
| breakout_8 AND volume_26 | 0.66% | -0.18% | -12.25% | -0.07% | 0.53% |
| breakout_8 + volume_26 | -2.69% | -11.66% | -12.25% | -1.39% | 10.96% |
| reversion_12 AND volume_26 | -0.54% | -5.03% | -12.25% | -0.67% | 5.28% |
| reversion_12 + volume_26 | -2.59% | -11.95% | -12.25% | -2.27% | 17.95% |
| ema_12_26 | -1.26% | -2.91% | -12.25% | -5.10% | 40.63% |
| macd_12_26_9 | 1.99% | -0.55% | -12.25% | -3.16% | 25.07% |
| rsi_14_recovery | -0.17% | -6.26% | -12.25% | -0.50% | 3.96% |
| bollinger_20_reentry | 0.57% | -5.57% | -12.25% | -0.50% | 3.96% |
| donchian_20 | -1.16% | -4.82% | -12.25% | -0.57% | 4.49% |
| atr_14_breakout | -1.56% | -7.96% | -12.25% | -0.57% | 4.49% |
| session_vwap | -0.94% | -13.39% | -12.25% | -5.78% | 46.17% |
| obv_20 | -4.52% | -13.68% | -12.25% | -2.63% | 20.84% |
| stochastic_14_3_recovery | -2.10% | -12.96% | -12.25% | -0.94% | 7.39% |
| mfi_14_recovery | 1.96% | -1.00% | -12.25% | -0.23% | 1.85% |
| adx_14_trend | -2.02% | -4.05% | -12.25% | -1.07% | 8.44% |
| aroon_25_trend | -0.29% | -3.58% | -12.25% | -1.37% | 10.82% |
| cci_20_momentum | -4.78% | -9.84% | -12.25% | -1.80% | 14.25% |
| williams_14_recovery | 0.05% | -8.78% | -12.25% | -0.74% | 5.80% |
| cmf_20_accumulation | -4.08% | -10.31% | -12.25% | -1.80% | 14.25% |
| chaikin_3_10 | -6.05% | -15.06% | -12.25% | -3.72% | 29.55% |
| roc_10_momentum | -1.79% | -7.40% | -12.25% | -1.61% | 12.66% |
| trix_15_trend | -1.14% | -5.21% | -12.25% | -3.98% | 31.66% |
| keltner_20_breakout | -2.87% | -5.29% | -12.25% | -0.34% | 2.64% |
| opening_range_30m | 6.70% | 1.88% | -12.25% | -2.73% | 21.64% |

동일 구간·초기 자금, 종료 시 청산 비용 포함. 노출 맞춤은 사후 설명용이며 v2 실제 계좌 성과가 아닙니다.
[낙폭 분해·비용 영향·전체 구간](CAT/comparison.json)

[v1 전체 기록](CAT/accounts.json) · [v2 전체 기록](CAT/accounts-v2.json)

## WMT 계좌

| 모델 | 전략 | 평가액 USD | 손익 USD | 최근 매매·이유 |
|---|---|---:|---:|---|
| v1 | cash | 10000.00 | 0.00 | 대기 /  / 새 신호 대기 |
| v1 | buy_hold | 10029.45 | 29.45 | buy /  / buy_hold: prior completed bar target 100%; next bar open simulation |
| v1 | trend_8_26 | 9847.13 | -152.87 | buy /  / trend_8_26: prior completed bar target 100%; next bar open simulation |
| v1 | momentum_26 | 9856.70 | -143.30 | buy /  / momentum_26: prior completed bar target 100%; next bar open simulation |
| v1 | breakout_8 | 9728.67 | -271.33 | sell /  / breakout_8: prior completed bar target 0%; next bar open simulation |
| v1 | reversion_12 | 9768.37 | -231.63 | buy /  / reversion_12: prior completed bar target 100%; next bar open simulation |
| v1 | volume_26 | 9755.08 | -244.92 | sell /  / volume_26: prior completed bar target 0%; next bar open simulation |
| v1 | trend_8_26 AND momentum_26 | 9867.03 | -132.97 | buy /  / trend_8_26 AND momentum_26: prior completed bar target 100%; next bar open simulation |
| v1 | trend_8_26 + momentum_26 | 9851.94 | -148.06 | buy /  / trend_8_26 + momentum_26: prior completed bar target 100%; next bar open simulation |
| v1 | trend_8_26 AND breakout_8 | 9854.29 | -145.71 | sell /  / trend_8_26 AND breakout_8: prior completed bar target 0%; next bar open simulation |
| v1 | trend_8_26 + breakout_8 | 9787.76 | -212.24 | buy /  / trend_8_26 + breakout_8: prior completed bar target 50%; next bar open simulation |
| v1 | trend_8_26 AND reversion_12 | 9818.96 | -181.04 | buy /  / trend_8_26 AND reversion_12: prior completed bar target 100%; next bar open simulation |
| v1 | trend_8_26 + reversion_12 | 9827.50 | -172.50 | buy /  / trend_8_26 + reversion_12: prior completed bar target 100%; next bar open simulation |
| v1 | trend_8_26 AND volume_26 | 9837.96 | -162.04 | sell /  / trend_8_26 AND volume_26: prior completed bar target 0%; next bar open simulation |
| v1 | trend_8_26 + volume_26 | 9801.16 | -198.84 | buy /  / trend_8_26 + volume_26: prior completed bar target 50%; next bar open simulation |
| v1 | momentum_26 AND breakout_8 | 9816.19 | -183.81 | sell /  / momentum_26 AND breakout_8: prior completed bar target 0%; next bar open simulation |
| v1 | momentum_26 + breakout_8 | 9851.59 | -148.41 | buy /  / momentum_26 + breakout_8: prior completed bar target 50%; next bar open simulation |
| v1 | momentum_26 AND reversion_12 | 9956.62 | -43.38 | buy /  / momentum_26 AND reversion_12: prior completed bar target 100%; next bar open simulation |
| v1 | momentum_26 + reversion_12 | 9891.27 | -108.73 | buy /  / momentum_26 + reversion_12: prior completed bar target 100%; next bar open simulation |
| v1 | momentum_26 AND volume_26 | 9905.94 | -94.06 | sell /  / momentum_26 AND volume_26: prior completed bar target 0%; next bar open simulation |
| v1 | momentum_26 + volume_26 | 9845.14 | -154.86 | buy /  / momentum_26 + volume_26: prior completed bar target 50%; next bar open simulation |
| v1 | breakout_8 AND reversion_12 | 10000.00 | 0.00 | 대기 /  / 새 신호 대기 |
| v1 | breakout_8 + reversion_12 | 9787.51 | -212.49 | buy /  / breakout_8 + reversion_12: prior completed bar target 50%; next bar open simulation |
| v1 | breakout_8 AND volume_26 | 9850.09 | -149.91 | sell /  / breakout_8 AND volume_26: prior completed bar target 0%; next bar open simulation |
| v1 | breakout_8 + volume_26 | 9741.88 | -258.12 | sell /  / breakout_8 + volume_26: prior completed bar target 0%; next bar open simulation |
| v1 | reversion_12 AND volume_26 | 9905.10 | -94.90 | sell /  / reversion_12 AND volume_26: prior completed bar target 0%; next bar open simulation |
| v1 | reversion_12 + volume_26 | 9800.83 | -199.17 | buy /  / reversion_12 + volume_26: prior completed bar target 50%; next bar open simulation |
| v1 | ema_12_26 | 9962.50 | -37.50 | buy /  / EMA12 > EMA26; 조건 충족; EMA12=118.628, EMA26=118.619 |
| v1 | macd_12_26_9 | 9985.46 | -14.54 | sell /  / MACD > 신호선 그리고 MACD > 0; 조건 미충족; MACD=0.122825, signal9=0.127837 |
| v1 | rsi_14_recovery | 10000.00 | 0.00 | 대기 /  / 새 신호 대기 |
| v1 | bollinger_20_reentry | 10000.00 | 0.00 | 대기 /  / 새 신호 대기 |
| v1 | donchian_20 | 9935.97 | -64.03 | sell /  / 종가 > 현재 봉을 제외한 직전 20봉 최고가; 조건 미충족; close=119.52, prior_high20=120.5 |
| v1 | atr_14_breakout | 9915.82 | -84.18 | sell /  / 종가 > 직전 종가 + 직전 ATR14 그리고 종가 > EMA26; 조건 미충족; close=119.52, threshold=120.186, prior_ATR14=0.395874, EMA26=118.952 |
| v1 | session_vwap | 9838.24 | -161.76 | sell /  / 종가 > 뉴욕 거래일별 누적 전형가격 VWAP; 조건 미충족; close=118.71, session_VWAP=118.72, session_volume=1.73369e+07 |
| v1 | obv_20 | 9857.61 | -142.39 | sell /  / OBV > OBV의 SMA20 그리고 종가 > EMA26; 조건 미충족; OBV=1.6238e+07, OBV_SMA20=1.74966e+07, close=118.945, EMA26=118.951 |
| v1 | stochastic_14_3_recovery | 9911.09 | -88.91 | sell /  / 직전 %K14 < 20에서 %K14가 %D3 상향 돌파 (한 봉 목표); 조건 미충족; K14=10.594, D3=19.0754, previous_K14=28.4976, previous_D3=22.0207 |
| v1 | mfi_14_recovery | 10000.00 | 0.00 | 대기 /  / 새 신호 대기 |
| v1 | adx_14_trend | 9991.69 | -8.31 | sell /  / Wilder ADX14 >= 25 그리고 +DI14 > -DI14; 조건 미충족; ADX14=24.5142, plus_DI14=24.7537, minus_DI14=21.6519 |
| v1 | aroon_25_trend | 9968.40 | -31.60 | buy /  / Aroon25 Up > 70 그리고 Down < 30 (동률이면 최신 극값); 조건 충족; Aroon_up=92, Aroon_down=28 |
| v1 | cci_20_momentum | 9772.81 | -227.19 | sell /  / CCI20 > 100 (전형가격·평균절대편차); 조건 미충족; CCI20=38.8365 |
| v1 | williams_14_recovery | 9911.09 | -88.91 | sell /  / 직전 Williams %R14 < -80, 현재 >= -80 (한 봉 목표); 조건 미충족; Williams_R14=-89.406, previous_R14=-71.5024 |
| v1 | cmf_20_accumulation | 9898.70 | -101.30 | sell /  / Chaikin Money Flow20 > 0.1; 조건 미충족; CMF20=0.0888031, volume20=1.50234e+07 |
| v1 | chaikin_3_10 | 9762.96 | -237.04 | sell /  / ADL의 EMA3 - EMA10 > 0 그리고 종가 > EMA26; 조건 미충족; Chaikin3_10=-178256, ADL=1.4762e+07, close=119.52, EMA26=118.952 |
| v1 | roc_10_momentum | 10000.00 | 0.00 | 대기 /  / 새 신호 대기 |
| v1 | trix_15_trend | 9708.65 | -291.35 | sell /  / 15봉 삼중 EMA의 1봉 변화율 TRIX > 0 그리고 종가 > EMA26; 조건 미충족; TRIX15_percent=0.0142754, close=118.77, EMA26=118.947 |
| v1 | keltner_20_breakout | 9935.97 | -64.03 | sell /  / 종가 > EMA20 + 2 x Wilder ATR14; 조건 미충족; close=119.52, upper_Keltner=119.83, EMA20=119.013, ATR14=0.408312 |
| v1 | opening_range_30m | 9927.51 | -72.49 | sell /  / 뉴욕 09:30·09:45 두 완료 봉 최고가를 10:00 이후 종가가 돌파; 조건 미충족; close=118.85, opening_high=119.14 |
| v2 | cash | 10000.00 | 0.00 | 대기 /  / 새 신호 대기 |
| v2 | buy_hold | 10626.10 | 626.10 | buy / partial / 직전 완료 봉 목표 비중 100%; 다음 봉 시가 가정 |
| v2 | trend_8_26 | 10246.35 | 246.35 | buy / partial / 직전 완료 봉 목표 비중 100%; 다음 봉 시가 가정 |
| v2 | momentum_26 | 10259.12 | 259.12 | buy / partial / 직전 완료 봉 목표 비중 100%; 다음 봉 시가 가정 |
| v2 | breakout_8 | 9682.65 | -317.35 | sell / filled / 직전 완료 봉 목표 비중 0%; 다음 봉 시가 가정 |
| v2 | reversion_12 | 9667.34 | -332.66 | buy / partial / 직전 완료 봉 목표 비중 100%; 다음 봉 시가 가정 |
| v2 | volume_26 | 9711.50 | -288.50 | sell / filled / 직전 완료 봉 목표 비중 0%; 다음 봉 시가 가정 |
| v2 | trend_8_26 AND momentum_26 | 10265.00 | 265.00 | buy / partial / 직전 완료 봉 목표 비중 100%; 다음 봉 시가 가정 |
| v2 | trend_8_26 + momentum_26 | 10252.71 | 252.71 | buy / partial / 직전 완료 봉 목표 비중 100%; 다음 봉 시가 가정 |
| v2 | trend_8_26 AND breakout_8 | 9935.59 | -64.41 | sell / filled / 직전 완료 봉 목표 비중 0%; 다음 봉 시가 가정 |
| v2 | trend_8_26 + breakout_8 | 9960.94 | -39.06 | buy / filled / 직전 완료 봉 목표 비중 50%; 다음 봉 시가 가정 |
| v2 | trend_8_26 AND reversion_12 | 9624.43 | -375.57 | buy / partial / 직전 완료 봉 목표 비중 100%; 다음 봉 시가 가정 |
| v2 | trend_8_26 + reversion_12 | 9975.16 | -24.84 | buy / partial / 직전 완료 봉 목표 비중 100%; 다음 봉 시가 가정 |
| v2 | trend_8_26 AND volume_26 | 9784.10 | -215.90 | sell / filled / 직전 완료 봉 목표 비중 0%; 다음 봉 시가 가정 |
| v2 | trend_8_26 + volume_26 | 9976.92 | -23.08 | buy / filled / 직전 완료 봉 목표 비중 50%; 다음 봉 시가 가정 |
| v2 | momentum_26 AND breakout_8 | 9773.67 | -226.33 | sell / filled / 직전 완료 봉 목표 비중 0%; 다음 봉 시가 가정 |
| v2 | momentum_26 + breakout_8 | 10030.28 | 30.28 | buy / filled / 직전 완료 봉 목표 비중 50%; 다음 봉 시가 가정 |
| v2 | momentum_26 AND reversion_12 | 9781.26 | -218.74 | buy / partial / 직전 완료 봉 목표 비중 100%; 다음 봉 시가 가정 |
| v2 | momentum_26 + reversion_12 | 10086.61 | 86.61 | buy / partial / 직전 완료 봉 목표 비중 100%; 다음 봉 시가 가정 |
| v2 | momentum_26 AND volume_26 | 9814.68 | -185.32 | sell / filled / 직전 완료 봉 목표 비중 0%; 다음 봉 시가 가정 |
| v2 | momentum_26 + volume_26 | 10025.11 | 25.11 | buy / filled / 직전 완료 봉 목표 비중 50%; 다음 봉 시가 가정 |
| v2 | breakout_8 AND reversion_12 | 10000.00 | 0.00 | 대기 /  / 새 신호 대기 |
| v2 | breakout_8 + reversion_12 | 9737.19 | -262.81 | buy / filled / 직전 완료 봉 목표 비중 50%; 다음 봉 시가 가정 |
| v2 | breakout_8 AND volume_26 | 9795.19 | -204.81 | sell / filled / 직전 완료 봉 목표 비중 0%; 다음 봉 시가 가정 |
| v2 | breakout_8 + volume_26 | 9698.42 | -301.58 | sell / filled / 직전 완료 봉 목표 비중 0%; 다음 봉 시가 가정 |
| v2 | reversion_12 AND volume_26 | 9912.80 | -87.20 | sell / filled / 직전 완료 봉 목표 비중 0%; 다음 봉 시가 가정 |
| v2 | reversion_12 + volume_26 | 9730.05 | -269.95 | buy / filled / 직전 완료 봉 목표 비중 50%; 다음 봉 시가 가정 |
| v2 | ema_12_26 | 9959.51 | -40.49 | buy / partial / EMA12 > EMA26; 조건 충족; EMA12=118.628, EMA26=118.619; 직전 완료 봉 목표를 다음 봉 시가에 모의 적용 |
| v2 | macd_12_26_9 | 9981.46 | -18.54 | sell / filled / MACD > 신호선 그리고 MACD > 0; 조건 미충족; MACD=0.122825, signal9=0.127837; 직전 완료 봉 목표를 다음 봉 시가에 모의 적용 |
| v2 | rsi_14_recovery | 10000.00 | 0.00 | 대기 /  / 새 신호 대기 |
| v2 | bollinger_20_reentry | 10000.00 | 0.00 | 대기 /  / 새 신호 대기 |
| v2 | donchian_20 | 9933.99 | -66.01 | sell / filled / 종가 > 현재 봉을 제외한 직전 20봉 최고가; 조건 미충족; close=119.52, prior_high20=120.5; 직전 완료 봉 목표를 다음 봉 시가에 모의 적용 |
| v2 | atr_14_breakout | 9911.85 | -88.15 | sell / filled / 종가 > 직전 종가 + 직전 ATR14 그리고 종가 > EMA26; 조건 미충족; close=119.52, threshold=120.186, prior_ATR14=0.395874, EMA26=118.952; 직전 완료 봉 목표를 다음 봉 시가에 모의 적용 |
| v2 | session_vwap | 9826.44 | -173.56 | sell / filled / 종가 > 뉴욕 거래일별 누적 전형가격 VWAP; 조건 미충족; close=118.71, session_VWAP=118.72, session_volume=1.73369e+07; 직전 완료 봉 목표를 다음 봉 시가에 모의 적용 |
| v2 | obv_20 | 9847.76 | -152.24 | sell / filled / OBV > OBV의 SMA20 그리고 종가 > EMA26; 조건 미충족; OBV=1.6238e+07, OBV_SMA20=1.74966e+07, close=118.945, EMA26=118.951; 직전 완료 봉 목표를 다음 봉 시가에 모의 적용 |
| v2 | stochastic_14_3_recovery | 9907.12 | -92.88 | sell / filled / 직전 %K14 < 20에서 %K14가 %D3 상향 돌파 (한 봉 목표); 조건 미충족; K14=10.594, D3=19.0754, previous_K14=28.4976, previous_D3=22.0207; 직전 완료 봉 목표를 다음 봉 시가에 모의 적용 |
| v2 | mfi_14_recovery | 10000.00 | 0.00 | 대기 /  / 새 신호 대기 |
| v2 | adx_14_trend | 9989.70 | -10.30 | sell / filled / Wilder ADX14 >= 25 그리고 +DI14 > -DI14; 조건 미충족; ADX14=24.5142, plus_DI14=24.7537, minus_DI14=21.6519; 직전 완료 봉 목표를 다음 봉 시가에 모의 적용 |
| v2 | aroon_25_trend | 9965.41 | -34.59 | buy / partial / Aroon25 Up > 70 그리고 Down < 30 (동률이면 최신 극값); 조건 충족; Aroon_up=92, Aroon_down=28; 직전 완료 봉 목표를 다음 봉 시가에 모의 적용 |
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
| cash | 0.00% | 0.00% | 11.06% | 0.00% | 0.00% |
| buy_hold | 11.53% | 11.06% | 11.06% | 11.06% | 100.00% |
| trend_8_26 | 7.86% | 4.29% | 11.06% | 7.71% | 70.45% |
| momentum_26 | 9.98% | 3.70% | 11.06% | 7.76% | 70.98% |
| breakout_8 | 6.44% | -10.02% | 11.06% | 2.81% | 26.12% |
| reversion_12 | 3.64% | -7.86% | 11.06% | 1.84% | 17.15% |
| volume_26 | 0.01% | -6.09% | 11.06% | 0.62% | 5.80% |
| trend_8_26 AND momentum_26 | 8.19% | 2.87% | 11.06% | 6.94% | 63.59% |
| trend_8_26 + momentum_26 | 8.92% | 4.00% | 11.06% | 7.74% | 70.72% |
| trend_8_26 AND breakout_8 | 6.58% | -6.83% | 11.06% | 2.32% | 21.64% |
| trend_8_26 + breakout_8 | 7.16% | -3.12% | 11.06% | 5.24% | 48.29% |
| trend_8_26 AND reversion_12 | -0.23% | -6.33% | 11.06% | 0.79% | 7.39% |
| trend_8_26 + reversion_12 | 5.77% | -1.55% | 11.06% | 4.74% | 43.80% |
| trend_8_26 AND volume_26 | -0.30% | -3.19% | 11.06% | 0.28% | 2.64% |
| trend_8_26 + volume_26 | 3.90% | -0.60% | 11.06% | 4.12% | 38.13% |
| momentum_26 AND breakout_8 | 6.62% | -7.18% | 11.06% | 2.46% | 22.96% |
| momentum_26 + breakout_8 | 8.21% | -2.58% | 11.06% | 5.27% | 48.56% |
| momentum_26 AND reversion_12 | 1.25% | -4.93% | 11.06% | 0.84% | 7.92% |
| momentum_26 + reversion_12 | 6.80% | 0.25% | 11.06% | 4.77% | 44.07% |
| momentum_26 AND volume_26 | 1.58% | -3.01% | 11.06% | 0.34% | 3.17% |
| momentum_26 + volume_26 | 4.91% | -0.89% | 11.06% | 4.15% | 38.39% |
| breakout_8 AND reversion_12 | 0.00% | 0.00% | 11.06% | 0.00% | 0.00% |
| breakout_8 + reversion_12 | 5.06% | -8.17% | 11.06% | 2.32% | 21.64% |
| breakout_8 AND volume_26 | 0.78% | -2.14% | 11.06% | 0.22% | 2.11% |
| breakout_8 + volume_26 | 3.20% | -7.88% | 11.06% | 1.71% | 15.97% |
| reversion_12 AND volume_26 | -1.05% | -3.51% | 11.06% | 0.20% | 1.85% |
| reversion_12 + volume_26 | 1.82% | -6.39% | 11.06% | 1.23% | 11.48% |
| ema_12_26 | 11.60% | 10.21% | 11.06% | 7.97% | 72.82% |
| macd_12_26_9 | 8.67% | 4.64% | 11.06% | 3.93% | 36.41% |
| rsi_14_recovery | -0.25% | -1.50% | 11.06% | 0.08% | 0.79% |
| bollinger_20_reentry | 1.41% | -1.12% | 11.06% | 0.17% | 1.58% |
| donchian_20 | 4.54% | -7.83% | 11.06% | 1.44% | 13.46% |
| atr_14_breakout | -0.86% | -10.74% | 11.06% | 0.82% | 7.65% |
| session_vwap | 9.97% | -0.16% | 11.06% | 6.35% | 58.31% |
| obv_20 | 10.73% | 2.67% | 11.06% | 6.20% | 56.99% |
| stochastic_14_3_recovery | 1.45% | -7.11% | 11.06% | 0.59% | 5.54% |
| mfi_14_recovery | 0.02% | -0.81% | 11.06% | 0.06% | 0.53% |
| adx_14_trend | 8.84% | 6.13% | 11.06% | 5.53% | 50.92% |
| aroon_25_trend | 5.99% | 0.78% | 11.06% | 3.55% | 32.98% |
| cci_20_momentum | 6.31% | -2.26% | 11.06% | 3.61% | 33.51% |
| williams_14_recovery | 0.10% | -7.58% | 11.06% | 0.53% | 5.01% |
| cmf_20_accumulation | 9.11% | -0.10% | 11.06% | 3.96% | 36.68% |
| chaikin_3_10 | 9.43% | 0.61% | 11.06% | 5.73% | 52.77% |
| roc_10_momentum | -0.30% | -5.20% | 11.06% | 1.55% | 14.51% |
| trix_15_trend | 10.97% | 6.86% | 11.06% | 7.11% | 65.17% |
| keltner_20_breakout | 6.59% | 0.08% | 11.06% | 2.86% | 26.65% |
| opening_range_30m | 9.76% | 4.80% | 11.06% | 3.90% | 36.15% |

동일 구간·초기 자금, 종료 시 청산 비용 포함. 노출 맞춤은 사후 설명용이며 v2 실제 계좌 성과가 아닙니다.
[낙폭 분해·비용 영향·전체 구간](WMT/comparison.json)

[v1 전체 기록](WMT/accounts.json) · [v2 전체 기록](WMT/accounts-v2.json)
