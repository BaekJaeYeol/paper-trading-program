# 모의투자 운영 현황

[PC·서버 장애 진단과 복구 방법](https://github.com/BaekJaeYeol/paper-trading-program/blob/main/investment-lab/docs/failure-recovery.md)

이번 실행 복구: {}

완료 봉 확인 주기: 기록 3/12회 · 기록 없는 예정 9회 · 아직 판정 전 14회 · 주의: 예약 시작 지연 또는 실행·저장 누락을 확인하세요.

[주기 판정 기준](https://github.com/BaekJaeYeol/paper-trading-program/blob/main/investment-lab/docs/session-coverage.md)

최근 확인: 2026-10-21T16:52:00.855471+00:00 (UTC)
다음 15분 확인 목표 (세션 실행 중에만 적용): 2026-10-21T17:07:00+00:00 (UTC, 실행 지연 가능)

실제 주문 없음. v1 기존 계좌와 v2 새 계좌의 시작일이 다르므로 수익률을 직접 우열 비교하지 마세요.
v2는 다음 봉 시가에 비용·스프레드·직전 거래량 제한을 적용한 가상 체결입니다. 미체결 잔량은 만료됩니다.

| 종목 | 상태 | 최근 성공 UTC | 마지막 완료 봉 UTC | 이번 새 봉 |
|---|---|---|---|---|
| SPY | updated | 2026-10-21T16:52:00.855471+00:00 | 2026-10-21T16:30:00+00:00 | 1 |
| QQQ | updated | 2026-10-21T16:52:00.855471+00:00 | 2026-10-21T16:30:00+00:00 | 1 |
| IWM | updated | 2026-10-21T16:52:00.855471+00:00 | 2026-10-21T16:30:00+00:00 | 1 |
| DIA | updated | 2026-10-21T16:52:00.855471+00:00 | 2026-10-21T16:30:00+00:00 | 1 |
| MSFT | updated | 2026-10-21T16:52:00.855471+00:00 | 2026-10-21T16:30:00+00:00 | 1 |
| JPM | updated | 2026-10-21T16:52:00.855471+00:00 | 2026-10-21T16:30:00+00:00 | 1 |
| XOM | updated | 2026-10-21T16:52:00.855471+00:00 | 2026-10-21T16:30:00+00:00 | 1 |
| JNJ | updated | 2026-10-21T16:52:00.855471+00:00 | 2026-10-21T16:30:00+00:00 | 1 |
| CAT | updated | 2026-10-21T16:52:00.855471+00:00 | 2026-10-21T16:30:00+00:00 | 1 |
| WMT | updated | 2026-10-21T16:52:00.855471+00:00 | 2026-10-21T16:30:00+00:00 | 1 |

이번 실행 소요: 29.1초
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
| v1 | buy_hold | 9977.71 | -22.29 | buy /  / buy_hold: prior completed bar target 100%; next bar open simulation |
| v1 | trend_8_26 | 9806.01 | -193.99 | buy /  / trend_8_26: prior completed bar target 100%; next bar open simulation |
| v1 | momentum_26 | 9731.90 | -268.10 | buy /  / momentum_26: prior completed bar target 100%; next bar open simulation |
| v1 | breakout_8 | 9633.88 | -366.12 | sell /  / breakout_8: prior completed bar target 0%; next bar open simulation |
| v1 | reversion_12 | 9722.53 | -277.47 | sell /  / reversion_12: prior completed bar target 0%; next bar open simulation |
| v1 | volume_26 | 9600.41 | -399.59 | sell /  / volume_26: prior completed bar target 0%; next bar open simulation |
| v1 | trend_8_26 AND momentum_26 | 9724.57 | -275.43 | buy /  / trend_8_26 AND momentum_26: prior completed bar target 100%; next bar open simulation |
| v1 | trend_8_26 + momentum_26 | 9768.87 | -231.13 | buy /  / trend_8_26 + momentum_26: prior completed bar target 100%; next bar open simulation |
| v1 | trend_8_26 AND breakout_8 | 9796.82 | -203.18 | sell /  / trend_8_26 AND breakout_8: prior completed bar target 0%; next bar open simulation |
| v1 | trend_8_26 + breakout_8 | 9758.41 | -241.59 | sell /  / trend_8_26 + breakout_8: prior completed bar target 50%; next bar open simulation |
| v1 | trend_8_26 AND reversion_12 | 9793.45 | -206.55 | sell /  / trend_8_26 AND reversion_12: prior completed bar target 0%; next bar open simulation |
| v1 | trend_8_26 + reversion_12 | 9764.02 | -235.98 | buy /  / trend_8_26 + reversion_12: prior completed bar target 50%; next bar open simulation |
| v1 | trend_8_26 AND volume_26 | 9645.60 | -354.40 | sell /  / trend_8_26 AND volume_26: prior completed bar target 0%; next bar open simulation |
| v1 | trend_8_26 + volume_26 | 9702.61 | -297.39 | sell /  / trend_8_26 + volume_26: prior completed bar target 50%; next bar open simulation |
| v1 | momentum_26 AND breakout_8 | 9705.50 | -294.50 | sell /  / momentum_26 AND breakout_8: prior completed bar target 0%; next bar open simulation |
| v1 | momentum_26 + breakout_8 | 9682.75 | -317.25 | sell /  / momentum_26 + breakout_8: prior completed bar target 50%; next bar open simulation |
| v1 | momentum_26 AND reversion_12 | 9794.14 | -205.86 | sell /  / momentum_26 AND reversion_12: prior completed bar target 0%; next bar open simulation |
| v1 | momentum_26 + reversion_12 | 9766.09 | -233.91 | buy /  / momentum_26 + reversion_12: prior completed bar target 50%; next bar open simulation |
| v1 | momentum_26 AND volume_26 | 9659.03 | -340.97 | sell /  / momentum_26 AND volume_26: prior completed bar target 0%; next bar open simulation |
| v1 | momentum_26 + volume_26 | 9665.87 | -334.13 | sell /  / momentum_26 + volume_26: prior completed bar target 50%; next bar open simulation |
| v1 | breakout_8 AND reversion_12 | 10000.00 | 0.00 | 대기 /  / 새 신호 대기 |
| v1 | breakout_8 + reversion_12 | 9677.86 | -322.14 | sell /  / breakout_8 + reversion_12: prior completed bar target 0%; next bar open simulation |
| v1 | breakout_8 AND volume_26 | 9878.80 | -121.20 | sell /  / breakout_8 AND volume_26: prior completed bar target 0%; next bar open simulation |
| v1 | breakout_8 + volume_26 | 9655.50 | -344.50 | sell /  / breakout_8 + volume_26: prior completed bar target 0%; next bar open simulation |
| v1 | reversion_12 AND volume_26 | 9861.02 | -138.98 | sell /  / reversion_12 AND volume_26: prior completed bar target 0%; next bar open simulation |
| v1 | reversion_12 + volume_26 | 9661.13 | -338.87 | sell /  / reversion_12 + volume_26: prior completed bar target 0%; next bar open simulation |
| v1 | ema_12_26 | 9837.74 | -162.26 | buy /  / EMA12 > EMA26; 조건 충족; EMA12=767.528, EMA26=767.458 |
| v1 | macd_12_26_9 | 9801.79 | -198.21 | buy /  / MACD > 신호선 그리고 MACD > 0; 조건 충족; MACD=0.244662, signal9=0.176064 |
| v1 | rsi_14_recovery | 9899.32 | -100.68 | sell /  / 직전 RSI14 < 30, 현재 RSI14 >= 30 (한 봉 목표); 조건 미충족; RSI14=34.3611, previous_RSI14=32.906 |
| v1 | bollinger_20_reentry | 9835.17 | -164.83 | sell /  / 직전 종가 < 직전 하단밴드, 현재 하단밴드 <= 종가 <= SMA20 (한 봉 목표); 조건 미충족; close=763.39, lower20=762.854, SMA20=768.639, previous_lower20=763.636 |
| v1 | donchian_20 | 9893.10 | -106.90 | sell /  / 종가 > 현재 봉을 제외한 직전 20봉 최고가; 조건 미충족; close=772.665, prior_high20=772.79 |
| v1 | atr_14_breakout | 9858.15 | -141.85 | sell /  / 종가 > 직전 종가 + 직전 ATR14 그리고 종가 > EMA26; 조건 미충족; close=770.65, threshold=771.314, prior_ATR14=1.1542, EMA26=769.052 |
| v1 | session_vwap | 9733.19 | -266.81 | buy /  / 종가 > 뉴욕 거래일별 누적 전형가격 VWAP; 조건 충족; close=770.23, session_VWAP=770.038, session_volume=6.50217e+06 |
| v1 | obv_20 | 9782.45 | -217.55 | sell /  / OBV > OBV의 SMA20 그리고 종가 > EMA26; 조건 미충족; OBV=-4.95693e+07, OBV_SMA20=-4.53436e+07, close=772.59, EMA26=770.236 |
| v1 | stochastic_14_3_recovery | 9694.64 | -305.36 | sell /  / 직전 %K14 < 20에서 %K14가 %D3 상향 돌파 (한 봉 목표); 조건 미충족; K14=53.6357, D3=31.478, previous_K14=28.6364, previous_D3=21.2782 |
| v1 | mfi_14_recovery | 9875.98 | -124.02 | sell /  / 직전 MFI14 < 20, 현재 MFI14 >= 20 (한 봉 목표); 조건 미충족; MFI14=33.0962, previous_MFI14=27.4403 |
| v1 | adx_14_trend | 9981.96 | -18.04 | sell /  / Wilder ADX14 >= 25 그리고 +DI14 > -DI14; 조건 미충족; ADX14=24.2312, plus_DI14=28.3519, minus_DI14=24.6578 |
| v1 | aroon_25_trend | 9861.30 | -138.70 | sell /  / Aroon25 Up > 70 그리고 Down < 30 (동률이면 최신 극값); 조건 미충족; Aroon_up=68, Aroon_down=20 |
| v1 | cci_20_momentum | 9776.05 | -223.95 | buy /  / CCI20 > 100 (전형가격·평균절대편차); 조건 충족; CCI20=100.444 |
| v1 | williams_14_recovery | 9666.94 | -333.06 | sell /  / 직전 Williams %R14 < -80, 현재 >= -80 (한 봉 목표); 조건 미충족; Williams_R14=-46.3643, previous_R14=-71.3636 |
| v1 | cmf_20_accumulation | 9879.23 | -120.77 | buy /  / Chaikin Money Flow20 > 0.1; 조건 충족; CMF20=0.196699, volume20=2.80437e+07 |
| v1 | chaikin_3_10 | 9718.37 | -281.63 | buy /  / ADL의 EMA3 - EMA10 > 0 그리고 종가 > EMA26; 조건 충족; Chaikin3_10=644152, ADL=1.0752e+07, close=769.37, EMA26=769.056 |
| v1 | roc_10_momentum | 9953.42 | -46.58 | sell /  / 10봉 ROC > 1% 그리고 종가 > EMA26; 조건 미충족; ROC10_percent=0.806376, close=769.45, EMA26=767.181 |
| v1 | trix_15_trend | 9641.78 | -358.22 | buy /  / 15봉 삼중 EMA의 1봉 변화율 TRIX > 0 그리고 종가 > EMA26; 조건 충족; TRIX15_percent=0.00337952, close=769.37, EMA26=769.056 |
| v1 | keltner_20_breakout | 9885.61 | -114.39 | sell /  / 종가 > EMA20 + 2 x Wilder ATR14; 조건 미충족; close=772.59, upper_Keltner=772.687, EMA20=770.545, ATR14=1.07124 |
| v1 | opening_range_30m | 9751.57 | -248.43 | buy /  / 뉴욕 09:30·09:45 두 완료 봉 최고가를 10:00 이후 종가가 돌파; 조건 충족; close=771.43, opening_high=771.34 |
| v2 | cash | 10000.00 | 0.00 | 대기 /  / 새 신호 대기 |
| v2 | buy_hold | 9905.74 | -94.26 | buy / partial / 직전 완료 봉 목표 비중 100%; 다음 봉 시가 가정 |
| v2 | trend_8_26 | 9685.97 | -314.03 | buy / partial / 직전 완료 봉 목표 비중 100%; 다음 봉 시가 가정 |
| v2 | momentum_26 | 9581.99 | -418.01 | buy / partial / 직전 완료 봉 목표 비중 100%; 다음 봉 시가 가정 |
| v2 | breakout_8 | 9230.56 | -769.44 | sell / filled / 직전 완료 봉 목표 비중 0%; 다음 봉 시가 가정 |
| v2 | reversion_12 | 9256.42 | -743.58 | sell / filled / 직전 완료 봉 목표 비중 0%; 다음 봉 시가 가정 |
| v2 | volume_26 | 9049.69 | -950.31 | sell / filled / 직전 완료 봉 목표 비중 0%; 다음 봉 시가 가정 |
| v2 | trend_8_26 AND momentum_26 | 9581.29 | -418.71 | buy / partial / 직전 완료 봉 목표 비중 100%; 다음 봉 시가 가정 |
| v2 | trend_8_26 + momentum_26 | 9633.83 | -366.17 | buy / partial / 직전 완료 봉 목표 비중 100%; 다음 봉 시가 가정 |
| v2 | trend_8_26 AND breakout_8 | 9615.96 | -384.04 | sell / filled / 직전 완료 봉 목표 비중 0%; 다음 봉 시가 가정 |
| v2 | trend_8_26 + breakout_8 | 9495.09 | -504.91 | sell / filled / 직전 완료 봉 목표 비중 50%; 다음 봉 시가 가정 |
| v2 | trend_8_26 AND reversion_12 | 9682.03 | -317.97 | sell / filled / 직전 완료 봉 목표 비중 0%; 다음 봉 시가 가정 |
| v2 | trend_8_26 + reversion_12 | 9468.28 | -531.72 | buy / filled / 직전 완료 봉 목표 비중 50%; 다음 봉 시가 가정 |
| v2 | trend_8_26 AND volume_26 | 9483.68 | -516.32 | sell / filled / 직전 완료 봉 목표 비중 0%; 다음 봉 시가 가정 |
| v2 | trend_8_26 + volume_26 | 9381.82 | -618.18 | sell / filled / 직전 완료 봉 목표 비중 50%; 다음 봉 시가 가정 |
| v2 | momentum_26 AND breakout_8 | 9482.12 | -517.88 | sell / filled / 직전 완료 봉 목표 비중 0%; 다음 봉 시가 가정 |
| v2 | momentum_26 + breakout_8 | 9404.53 | -595.47 | sell / filled / 직전 완료 봉 목표 비중 50%; 다음 봉 시가 가정 |
| v2 | momentum_26 AND reversion_12 | 9748.35 | -251.65 | sell / filled / 직전 완료 봉 목표 비중 0%; 다음 봉 시가 가정 |
| v2 | momentum_26 + reversion_12 | 9476.91 | -523.09 | buy / filled / 직전 완료 봉 목표 비중 50%; 다음 봉 시가 가정 |
| v2 | momentum_26 AND volume_26 | 9565.70 | -434.30 | sell / filled / 직전 완료 봉 목표 비중 0%; 다음 봉 시가 가정 |
| v2 | momentum_26 + volume_26 | 9370.57 | -629.43 | sell / filled / 직전 완료 봉 목표 비중 50%; 다음 봉 시가 가정 |
| v2 | breakout_8 AND reversion_12 | 10000.00 | 0.00 | 대기 /  / 새 신호 대기 |
| v2 | breakout_8 + reversion_12 | 9281.71 | -718.29 | sell / filled / 직전 완료 봉 목표 비중 0%; 다음 봉 시가 가정 |
| v2 | breakout_8 AND volume_26 | 9808.87 | -191.13 | sell / filled / 직전 완료 봉 목표 비중 0%; 다음 봉 시가 가정 |
| v2 | breakout_8 + volume_26 | 9216.25 | -783.75 | sell / filled / 직전 완료 봉 목표 비중 0%; 다음 봉 시가 가정 |
| v2 | reversion_12 AND volume_26 | 9602.16 | -397.84 | sell / filled / 직전 완료 봉 목표 비중 0%; 다음 봉 시가 가정 |
| v2 | reversion_12 + volume_26 | 9229.26 | -770.74 | sell / filled / 직전 완료 봉 목표 비중 0%; 다음 봉 시가 가정 |
| v2 | ema_12_26 | 9832.83 | -167.17 | buy / partial / EMA12 > EMA26; 조건 충족; EMA12=767.528, EMA26=767.458; 직전 완료 봉 목표를 다음 봉 시가에 모의 적용 |
| v2 | macd_12_26_9 | 9794.94 | -205.06 | buy / partial / MACD > 신호선 그리고 MACD > 0; 조건 충족; MACD=0.244662, signal9=0.176064; 직전 완료 봉 목표를 다음 봉 시가에 모의 적용 |
| v2 | rsi_14_recovery | 9895.36 | -104.64 | sell / filled / 직전 RSI14 < 30, 현재 RSI14 >= 30 (한 봉 목표); 조건 미충족; RSI14=34.3611, previous_RSI14=32.906; 직전 완료 봉 목표를 다음 봉 시가에 모의 적용 |
| v2 | bollinger_20_reentry | 9829.27 | -170.73 | sell / filled / 직전 종가 < 직전 하단밴드, 현재 하단밴드 <= 종가 <= SMA20 (한 봉 목표); 조건 미충족; close=763.39, lower20=762.854, SMA20=768.639, previous_lower20=763.636; 직전 완료 봉 목표를 다음 봉 시가에 모의 적용 |
| v2 | donchian_20 | 9887.17 | -112.83 | sell / filled / 종가 > 현재 봉을 제외한 직전 20봉 최고가; 조건 미충족; close=772.665, prior_high20=772.79; 직전 완료 봉 목표를 다음 봉 시가에 모의 적용 |
| v2 | atr_14_breakout | 9850.26 | -149.74 | sell / filled / 종가 > 직전 종가 + 직전 ATR14 그리고 종가 > EMA26; 조건 미충족; close=770.65, threshold=771.314, prior_ATR14=1.1542, EMA26=769.052; 직전 완료 봉 목표를 다음 봉 시가에 모의 적용 |
| v2 | session_vwap | 9720.55 | -279.45 | buy / partial / 종가 > 뉴욕 거래일별 누적 전형가격 VWAP; 조건 충족; close=770.23, session_VWAP=770.038, session_volume=6.50217e+06; 직전 완료 봉 목표를 다음 봉 시가에 모의 적용 |
| v2 | obv_20 | 9772.67 | -227.33 | sell / filled / OBV > OBV의 SMA20 그리고 종가 > EMA26; 조건 미충족; OBV=-4.95693e+07, OBV_SMA20=-4.53436e+07, close=772.59, EMA26=770.236; 직전 완료 봉 목표를 다음 봉 시가에 모의 적용 |
| v2 | stochastic_14_3_recovery | 9677.21 | -322.79 | sell / filled / 직전 %K14 < 20에서 %K14가 %D3 상향 돌파 (한 봉 목표); 조건 미충족; K14=53.6357, D3=31.478, previous_K14=28.6364, previous_D3=21.2782; 직전 완료 봉 목표를 다음 봉 시가에 모의 적용 |
| v2 | mfi_14_recovery | 9870.05 | -129.95 | sell / filled / 직전 MFI14 < 20, 현재 MFI14 >= 20 (한 봉 목표); 조건 미충족; MFI14=33.0962, previous_MFI14=27.4403; 직전 완료 봉 목표를 다음 봉 시가에 모의 적용 |
| v2 | adx_14_trend | 9979.97 | -20.03 | sell / filled / Wilder ADX14 >= 25 그리고 +DI14 > -DI14; 조건 미충족; ADX14=24.2312, plus_DI14=28.3519, minus_DI14=24.6578; 직전 완료 봉 목표를 다음 봉 시가에 모의 적용 |
| v2 | aroon_25_trend | 9857.36 | -142.64 | sell / filled / Aroon25 Up > 70 그리고 Down < 30 (동률이면 최신 극값); 조건 미충족; Aroon_up=68, Aroon_down=20; 직전 완료 봉 목표를 다음 봉 시가에 모의 적용 |
| v2 | cci_20_momentum | 9765.31 | -234.69 | buy / partial / CCI20 > 100 (전형가격·평균절대편차); 조건 충족; CCI20=100.444; 직전 완료 봉 목표를 다음 봉 시가에 모의 적용 |
| v2 | williams_14_recovery | 9649.55 | -350.45 | sell / filled / 직전 Williams %R14 < -80, 현재 >= -80 (한 봉 목표); 조건 미충족; Williams_R14=-46.3643, previous_R14=-71.3636; 직전 완료 봉 목표를 다음 봉 시가에 모의 적용 |
| v2 | cmf_20_accumulation | 9872.32 | -127.68 | buy / partial / Chaikin Money Flow20 > 0.1; 조건 충족; CMF20=0.196699, volume20=2.80437e+07; 직전 완료 봉 목표를 다음 봉 시가에 모의 적용 |
| v2 | chaikin_3_10 | 9705.74 | -294.26 | buy / partial / ADL의 EMA3 - EMA10 > 0 그리고 종가 > EMA26; 조건 충족; Chaikin3_10=644152, ADL=1.0752e+07, close=769.37, EMA26=769.056; 직전 완료 봉 목표를 다음 봉 시가에 모의 적용 |
| v2 | roc_10_momentum | 9951.43 | -48.57 | sell / filled / 10봉 ROC > 1% 그리고 종가 > EMA26; 조건 미충족; ROC10_percent=0.806376, close=769.45, EMA26=767.181; 직전 완료 봉 목표를 다음 봉 시가에 모의 적용 |
| v2 | trix_15_trend | 9627.33 | -372.67 | buy / partial / 15봉 삼중 EMA의 1봉 변화율 TRIX > 0 그리고 종가 > EMA26; 조건 충족; TRIX15_percent=0.00337952, close=769.37, EMA26=769.056; 직전 완료 봉 목표를 다음 봉 시가에 모의 적용 |
| v2 | keltner_20_breakout | 9881.65 | -118.35 | sell / filled / 종가 > EMA20 + 2 x Wilder ATR14; 조건 미충족; close=772.59, upper_Keltner=772.687, EMA20=770.545, ATR14=1.07124; 직전 완료 봉 목표를 다음 봉 시가에 모의 적용 |
| v2 | opening_range_30m | 9740.85 | -259.15 | buy / partial / 뉴욕 09:30·09:45 두 완료 봉 최고가를 10:00 이후 종가가 돌파; 조건 충족; close=771.43, opening_high=771.34; 직전 완료 봉 목표를 다음 봉 시가에 모의 적용 |

### 같은 기간의 비용·노출 비교 (사후 연구)

| 전략 | 비용 전 | 비용 후 | 100% 보유 | 같은 평균 노출 보유 | 평균 노출 |
|---|---:|---:|---:|---:|---:|
| cash | 0.00% | 0.00% | 0.39% | 0.00% | 0.00% |
| buy_hold | 0.82% | 0.39% | 0.39% | 0.39% | 100.00% |
| trend_8_26 | 1.14% | -2.61% | 0.39% | 0.21% | 52.89% |
| momentum_26 | -0.61% | -5.49% | 0.39% | 0.21% | 52.89% |
| breakout_8 | -0.37% | -16.13% | 0.39% | 0.09% | 23.16% |
| reversion_12 | -1.28% | -11.49% | 0.39% | 0.10% | 26.32% |
| volume_26 | -1.29% | -10.38% | 0.39% | 0.04% | 9.21% |
| trend_8_26 AND momentum_26 | 0.32% | -4.21% | 0.39% | 0.18% | 45.00% |
| trend_8_26 + momentum_26 | 0.26% | -4.06% | 0.39% | 0.21% | 52.90% |
| trend_8_26 AND breakout_8 | 0.01% | -10.71% | 0.39% | 0.05% | 13.95% |
| trend_8_26 + breakout_8 | 0.38% | -9.24% | 0.39% | 0.15% | 38.03% |
| trend_8_26 AND reversion_12 | -0.00% | -4.12% | 0.39% | 0.02% | 5.79% |
| trend_8_26 + reversion_12 | -0.07% | -6.97% | 0.39% | 0.16% | 39.61% |
| trend_8_26 AND volume_26 | -1.03% | -5.89% | 0.39% | 0.02% | 5.26% |
| trend_8_26 + volume_26 | -0.08% | -6.58% | 0.39% | 0.12% | 31.06% |
| momentum_26 AND breakout_8 | 0.17% | -11.31% | 0.39% | 0.06% | 15.53% |
| momentum_26 + breakout_8 | -0.49% | -10.97% | 0.39% | 0.15% | 38.03% |
| momentum_26 AND reversion_12 | -0.79% | -5.67% | 0.39% | 0.02% | 6.32% |
| momentum_26 + reversion_12 | -0.94% | -7.97% | 0.39% | 0.16% | 39.61% |
| momentum_26 AND volume_26 | -0.78% | -4.86% | 0.39% | 0.01% | 3.68% |
| momentum_26 + volume_26 | -0.94% | -7.00% | 0.39% | 0.12% | 31.06% |
| breakout_8 AND reversion_12 | 0.00% | 0.00% | 0.39% | 0.00% | 0.00% |
| breakout_8 + reversion_12 | -0.82% | -13.49% | 0.39% | 0.10% | 24.75% |
| breakout_8 AND volume_26 | -0.33% | -2.40% | 0.39% | 0.01% | 1.84% |
| breakout_8 + volume_26 | -0.83% | -12.76% | 0.39% | 0.06% | 16.19% |
| reversion_12 AND volume_26 | -0.87% | -5.34% | 0.39% | 0.02% | 3.95% |
| reversion_12 + volume_26 | -1.28% | -10.75% | 0.39% | 0.07% | 17.77% |
| ema_12_26 | -0.07% | -3.78% | 0.39% | 0.22% | 56.58% |
| macd_12_26_9 | 0.34% | -4.59% | 0.39% | 0.13% | 33.42% |
| rsi_14_recovery | -0.53% | -4.22% | 0.39% | 0.01% | 2.37% |
| bollinger_20_reentry | -1.07% | -6.72% | 0.39% | 0.01% | 3.68% |
| donchian_20 | 0.02% | -7.65% | 0.39% | 0.03% | 7.11% |
| atr_14_breakout | 0.32% | -5.40% | 0.39% | 0.02% | 3.95% |
| session_vwap | 1.90% | -8.26% | 0.39% | 0.18% | 46.32% |
| obv_20 | -0.05% | -8.10% | 0.39% | 0.16% | 40.00% |
| stochastic_14_3_recovery | -0.08% | -14.46% | 0.39% | 0.04% | 9.74% |
| mfi_14_recovery | 0.08% | -2.41% | 0.39% | 0.01% | 1.58% |
| adx_14_trend | 0.57% | -2.34% | 0.39% | 0.10% | 25.26% |
| aroon_25_trend | 0.89% | -1.62% | 0.39% | 0.09% | 24.21% |
| cci_20_momentum | -0.14% | -8.96% | 0.39% | 0.09% | 23.68% |
| williams_14_recovery | -0.22% | -10.55% | 0.39% | 0.03% | 6.84% |
| cmf_20_accumulation | 2.03% | -2.17% | 0.39% | 0.18% | 45.00% |
| chaikin_3_10 | 1.72% | -5.29% | 0.39% | 0.17% | 43.16% |
| roc_10_momentum | -0.13% | -0.97% | 0.39% | 0.00% | 1.05% |
| trix_15_trend | -0.16% | -5.07% | 0.39% | 0.17% | 42.63% |
| keltner_20_breakout | -0.27% | -3.96% | 0.39% | 0.04% | 11.05% |
| opening_range_30m | 0.57% | -5.57% | 0.39% | 0.15% | 37.63% |

동일 구간·초기 자금, 종료 시 청산 비용 포함. 노출 맞춤은 사후 설명용이며 v2 실제 계좌 성과가 아닙니다.
[낙폭 분해·비용 영향·전체 구간](SPY/comparison.json)

[v1 전체 기록](SPY/accounts.json) · [v2 전체 기록](SPY/accounts-v2.json)

## QQQ 계좌

| 모델 | 전략 | 평가액 USD | 손익 USD | 최근 매매·이유 |
|---|---|---:|---:|---|
| v1 | cash | 10000.00 | 0.00 | 대기 /  / 새 신호 대기 |
| v1 | buy_hold | 9997.90 | -2.10 | buy /  / buy_hold: prior completed bar target 100%; next bar open simulation |
| v1 | trend_8_26 | 9876.59 | -123.41 | buy /  / trend_8_26: prior completed bar target 100%; next bar open simulation |
| v1 | momentum_26 | 9560.57 | -439.43 | buy /  / momentum_26: prior completed bar target 100%; next bar open simulation |
| v1 | breakout_8 | 9645.01 | -354.99 | sell /  / breakout_8: prior completed bar target 0%; next bar open simulation |
| v1 | reversion_12 | 9765.33 | -234.67 | sell /  / reversion_12: prior completed bar target 0%; next bar open simulation |
| v1 | volume_26 | 9606.91 | -393.09 | sell /  / volume_26: prior completed bar target 0%; next bar open simulation |
| v1 | trend_8_26 AND momentum_26 | 9929.79 | -70.21 | buy /  / trend_8_26 AND momentum_26: prior completed bar target 100%; next bar open simulation |
| v1 | trend_8_26 + momentum_26 | 9756.30 | -243.70 | buy /  / trend_8_26 + momentum_26: prior completed bar target 100%; next bar open simulation |
| v1 | trend_8_26 AND breakout_8 | 9982.22 | -17.78 | sell /  / trend_8_26 AND breakout_8: prior completed bar target 0%; next bar open simulation |
| v1 | trend_8_26 + breakout_8 | 9799.19 | -200.81 | sell /  / trend_8_26 + breakout_8: prior completed bar target 50%; next bar open simulation |
| v1 | trend_8_26 AND reversion_12 | 9902.56 | -97.44 | sell /  / trend_8_26 AND reversion_12: prior completed bar target 0%; next bar open simulation |
| v1 | trend_8_26 + reversion_12 | 9840.54 | -159.46 | buy /  / trend_8_26 + reversion_12: prior completed bar target 50%; next bar open simulation |
| v1 | trend_8_26 AND volume_26 | 9846.67 | -153.33 | sell /  / trend_8_26 AND volume_26: prior completed bar target 0%; next bar open simulation |
| v1 | trend_8_26 + volume_26 | 9740.74 | -259.26 | buy /  / trend_8_26 + volume_26: prior completed bar target 50%; next bar open simulation |
| v1 | momentum_26 AND breakout_8 | 9676.24 | -323.76 | sell /  / momentum_26 AND breakout_8: prior completed bar target 0%; next bar open simulation |
| v1 | momentum_26 + breakout_8 | 9602.78 | -397.22 | sell /  / momentum_26 + breakout_8: prior completed bar target 50%; next bar open simulation |
| v1 | momentum_26 AND reversion_12 | 9800.84 | -199.16 | sell /  / momentum_26 AND reversion_12: prior completed bar target 0%; next bar open simulation |
| v1 | momentum_26 + reversion_12 | 9701.29 | -298.71 | buy /  / momentum_26 + reversion_12: prior completed bar target 50%; next bar open simulation |
| v1 | momentum_26 AND volume_26 | 9819.14 | -180.86 | sell /  / momentum_26 AND volume_26: prior completed bar target 0%; next bar open simulation |
| v1 | momentum_26 + volume_26 | 9602.84 | -397.16 | buy /  / momentum_26 + volume_26: prior completed bar target 50%; next bar open simulation |
| v1 | breakout_8 AND reversion_12 | 10000.00 | 0.00 | 대기 /  / 새 신호 대기 |
| v1 | breakout_8 + reversion_12 | 9743.95 | -256.05 | sell /  / breakout_8 + reversion_12: prior completed bar target 0%; next bar open simulation |
| v1 | breakout_8 AND volume_26 | 9929.33 | -70.67 | sell /  / breakout_8 AND volume_26: prior completed bar target 0%; next bar open simulation |
| v1 | breakout_8 + volume_26 | 9645.20 | -354.80 | sell /  / breakout_8 + volume_26: prior completed bar target 0%; next bar open simulation |
| v1 | reversion_12 AND volume_26 | 9907.31 | -92.69 | sell /  / reversion_12 AND volume_26: prior completed bar target 0%; next bar open simulation |
| v1 | reversion_12 + volume_26 | 9724.60 | -275.40 | sell /  / reversion_12 + volume_26: prior completed bar target 0%; next bar open simulation |
| v1 | ema_12_26 | 9631.21 | -368.79 | buy /  / EMA12 > EMA26; 조건 충족; EMA12=719.205, EMA26=719.04 |
| v1 | macd_12_26_9 | 9783.10 | -216.90 | buy /  / MACD > 신호선 그리고 MACD > 0; 조건 충족; MACD=0.165076, signal9=-0.134014 |
| v1 | rsi_14_recovery | 9809.40 | -190.60 | sell /  / 직전 RSI14 < 30, 현재 RSI14 >= 30 (한 봉 목표); 조건 미충족; RSI14=50.2063, previous_RSI14=44.1729 |
| v1 | bollinger_20_reentry | 9878.60 | -121.40 | sell /  / 직전 종가 < 직전 하단밴드, 현재 하단밴드 <= 종가 <= SMA20 (한 봉 목표); 조건 미충족; close=718.66, lower20=714.386, SMA20=719.409, previous_lower20=714.271 |
| v1 | donchian_20 | 9927.41 | -72.59 | sell /  / 종가 > 현재 봉을 제외한 직전 20봉 최고가; 조건 미충족; close=725.78, prior_high20=726.6 |
| v1 | atr_14_breakout | 9930.01 | -69.99 | sell /  / 종가 > 직전 종가 + 직전 ATR14 그리고 종가 > EMA26; 조건 미충족; close=722.535, threshold=722.712, prior_ATR14=1.8425, EMA26=719.04 |
| v1 | session_vwap | 9738.62 | -261.38 | buy /  / 종가 > 뉴욕 거래일별 누적 전형가격 VWAP; 조건 충족; close=721.81, session_VWAP=721.45, session_volume=2.32267e+07 |
| v1 | obv_20 | 9763.01 | -236.99 | buy /  / OBV > OBV의 SMA20 그리고 종가 > EMA26; 조건 충족; OBV=2.23867e+08, OBV_SMA20=2.10034e+08, close=722.48, EMA26=719.576 |
| v1 | stochastic_14_3_recovery | 9598.51 | -401.49 | sell /  / 직전 %K14 < 20에서 %K14가 %D3 상향 돌파 (한 봉 목표); 조건 미충족; K14=21.6302, D3=18.3878, previous_K14=24.7642, previous_D3=19.9023 |
| v1 | mfi_14_recovery | 9813.56 | -186.44 | sell /  / 직전 MFI14 < 20, 현재 MFI14 >= 20 (한 봉 목표); 조건 미충족; MFI14=30.3876, previous_MFI14=31.1747 |
| v1 | adx_14_trend | 9920.36 | -79.64 | buy /  / Wilder ADX14 >= 25 그리고 +DI14 > -DI14; 조건 충족; ADX14=25.1063, plus_DI14=29.8515, minus_DI14=14.2405 |
| v1 | aroon_25_trend | 9831.22 | -168.78 | sell /  / Aroon25 Up > 70 그리고 Down < 30 (동률이면 최신 극값); 조건 미충족; Aroon_up=100, Aroon_down=80 |
| v1 | cci_20_momentum | 9900.95 | -99.05 | sell /  / CCI20 > 100 (전형가격·평균절대편차); 조건 미충족; CCI20=99.5288 |
| v1 | williams_14_recovery | 9689.61 | -310.39 | sell /  / 직전 Williams %R14 < -80, 현재 >= -80 (한 봉 목표); 조건 미충족; Williams_R14=-78.3698, previous_R14=-75.2358 |
| v1 | cmf_20_accumulation | 9590.99 | -409.01 | buy /  / Chaikin Money Flow20 > 0.1; 조건 충족; CMF20=0.185201, volume20=2.07769e+08 |
| v1 | chaikin_3_10 | 9769.86 | -230.14 | buy /  / ADL의 EMA3 - EMA10 > 0 그리고 종가 > EMA26; 조건 충족; Chaikin3_10=659089, ADL=2.27792e+08, close=722.48, EMA26=719.576 |
| v1 | roc_10_momentum | 9961.33 | -38.67 | sell /  / 10봉 ROC > 1% 그리고 종가 > EMA26; 조건 미충족; ROC10_percent=0.681109, close=725.78, EMA26=721.667 |
| v1 | trix_15_trend | 9720.19 | -279.81 | buy /  / 15봉 삼중 EMA의 1봉 변화율 TRIX > 0 그리고 종가 > EMA26; 조건 충족; TRIX15_percent=3.24292e-05, close=721.81, EMA26=719.344 |
| v1 | keltner_20_breakout | 9820.93 | -179.07 | sell /  / 종가 > EMA20 + 2 x Wilder ATR14; 조건 미충족; close=725.221, upper_Keltner=725.877, EMA20=722.517, ATR14=1.67972 |
| v1 | opening_range_30m | 9794.24 | -205.76 | buy /  / 뉴욕 09:30·09:45 두 완료 봉 최고가를 10:00 이후 종가가 돌파; 조건 충족; close=723.37, opening_high=723.2 |
| v2 | cash | 10000.00 | 0.00 | 대기 /  / 새 신호 대기 |
| v2 | buy_hold | 9674.73 | -325.27 | buy / partial / 직전 완료 봉 목표 비중 100%; 다음 봉 시가 가정 |
| v2 | trend_8_26 | 9675.93 | -324.07 | buy / partial / 직전 완료 봉 목표 비중 100%; 다음 봉 시가 가정 |
| v2 | momentum_26 | 9450.54 | -549.46 | buy / partial / 직전 완료 봉 목표 비중 100%; 다음 봉 시가 가정 |
| v2 | breakout_8 | 9311.68 | -688.32 | sell / filled / 직전 완료 봉 목표 비중 0%; 다음 봉 시가 가정 |
| v2 | reversion_12 | 9275.81 | -724.19 | sell / filled / 직전 완료 봉 목표 비중 0%; 다음 봉 시가 가정 |
| v2 | volume_26 | 9565.80 | -434.20 | 중단: 손실 한도 / sell / filled / 직전 완료 봉 목표 비중 0%; 다음 봉 시가 가정 |
| v2 | trend_8_26 AND momentum_26 | 9823.37 | -176.63 | buy / partial / 직전 완료 봉 목표 비중 100%; 다음 봉 시가 가정 |
| v2 | trend_8_26 + momentum_26 | 9602.91 | -397.09 | buy / partial / 직전 완료 봉 목표 비중 100%; 다음 봉 시가 가정 |
| v2 | trend_8_26 AND breakout_8 | 9874.28 | -125.72 | sell / filled / 직전 완료 봉 목표 비중 0%; 다음 봉 시가 가정 |
| v2 | trend_8_26 + breakout_8 | 9531.92 | -468.08 | sell / filled / 직전 완료 봉 목표 비중 50%; 다음 봉 시가 가정 |
| v2 | trend_8_26 AND reversion_12 | 9761.15 | -238.85 | sell / filled / 직전 완료 봉 목표 비중 0%; 다음 봉 시가 가정 |
| v2 | trend_8_26 + reversion_12 | 9493.43 | -506.57 | buy / filled / 직전 완료 봉 목표 비중 50%; 다음 봉 시가 가정 |
| v2 | trend_8_26 AND volume_26 | 9679.53 | -320.47 | sell / filled / 직전 완료 봉 목표 비중 0%; 다음 봉 시가 가정 |
| v2 | trend_8_26 + volume_26 | 9342.46 | -657.54 | buy / filled / 직전 완료 봉 목표 비중 50%; 다음 봉 시가 가정 |
| v2 | momentum_26 AND breakout_8 | 9624.72 | -375.28 | sell / filled / 직전 완료 봉 목표 비중 0%; 다음 봉 시가 가정 |
| v2 | momentum_26 + breakout_8 | 9380.89 | -619.11 | sell / filled / 직전 완료 봉 목표 비중 50%; 다음 봉 시가 가정 |
| v2 | momentum_26 AND reversion_12 | 9794.96 | -205.04 | sell / filled / 직전 완료 봉 목표 비중 0%; 다음 봉 시가 가정 |
| v2 | momentum_26 + reversion_12 | 9421.74 | -578.26 | buy / filled / 직전 완료 봉 목표 비중 50%; 다음 봉 시가 가정 |
| v2 | momentum_26 AND volume_26 | 9749.31 | -250.69 | sell / filled / 직전 완료 봉 목표 비중 0%; 다음 봉 시가 가정 |
| v2 | momentum_26 + volume_26 | 9252.41 | -747.59 | buy / filled / 직전 완료 봉 목표 비중 50%; 다음 봉 시가 가정 |
| v2 | breakout_8 AND reversion_12 | 10000.00 | 0.00 | 대기 /  / 새 신호 대기 |
| v2 | breakout_8 + reversion_12 | 9391.56 | -608.44 | sell / filled / 직전 완료 봉 목표 비중 0%; 다음 봉 시가 가정 |
| v2 | breakout_8 AND volume_26 | 9871.76 | -128.24 | sell / filled / 직전 완료 봉 목표 비중 0%; 다음 봉 시가 가정 |
| v2 | breakout_8 + volume_26 | 9222.96 | -777.04 | sell / filled / 직전 완료 봉 목표 비중 0%; 다음 봉 시가 가정 |
| v2 | reversion_12 AND volume_26 | 9547.64 | -452.36 | 중단: 손실 한도 / sell / filled / 직전 완료 봉 목표 비중 0%; 다음 봉 시가 가정 |
| v2 | reversion_12 + volume_26 | 9205.24 | -794.76 | sell / filled / 직전 완료 봉 목표 비중 0%; 다음 봉 시가 가정 |
| v2 | ema_12_26 | 9622.54 | -377.46 | buy / partial / EMA12 > EMA26; 조건 충족; EMA12=719.205, EMA26=719.04; 직전 완료 봉 목표를 다음 봉 시가에 모의 적용 |
| v2 | macd_12_26_9 | 9774.30 | -225.70 | buy / partial / MACD > 신호선 그리고 MACD > 0; 조건 충족; MACD=0.165076, signal9=-0.134014; 직전 완료 봉 목표를 다음 봉 시가에 모의 적용 |
| v2 | rsi_14_recovery | 9801.56 | -198.44 | sell / filled / 직전 RSI14 < 30, 현재 RSI14 >= 30 (한 봉 목표); 조건 미충족; RSI14=50.2063, previous_RSI14=44.1729; 직전 완료 봉 목표를 다음 봉 시가에 모의 적용 |
| v2 | bollinger_20_reentry | 9872.68 | -127.32 | sell / filled / 직전 종가 < 직전 하단밴드, 현재 하단밴드 <= 종가 <= SMA20 (한 봉 목표); 조건 미충족; close=718.66, lower20=714.386, SMA20=719.409, previous_lower20=714.271; 직전 완료 봉 목표를 다음 봉 시가에 모의 적용 |
| v2 | donchian_20 | 9921.45 | -78.55 | sell / filled / 종가 > 현재 봉을 제외한 직전 20봉 최고가; 조건 미충족; close=725.78, prior_high20=726.6; 직전 완료 봉 목표를 다음 봉 시가에 모의 적용 |
| v2 | atr_14_breakout | 9924.06 | -75.94 | sell / filled / 종가 > 직전 종가 + 직전 ATR14 그리고 종가 > EMA26; 조건 미충족; close=722.535, threshold=722.712, prior_ATR14=1.8425, EMA26=719.04; 직전 완료 봉 목표를 다음 봉 시가에 모의 적용 |
| v2 | session_vwap | 9724.03 | -275.97 | buy / partial / 종가 > 뉴욕 거래일별 누적 전형가격 VWAP; 조건 충족; close=721.81, session_VWAP=721.45, session_volume=2.32267e+07; 직전 완료 봉 목표를 다음 봉 시가에 모의 적용 |
| v2 | obv_20 | 9752.28 | -247.72 | buy / partial / OBV > OBV의 SMA20 그리고 종가 > EMA26; 조건 충족; OBV=2.23867e+08, OBV_SMA20=2.10034e+08, close=722.48, EMA26=719.576; 직전 완료 봉 목표를 다음 봉 시가에 모의 적용 |
| v2 | stochastic_14_3_recovery | 9694.13 | -305.87 | 중단: 손실 한도 / sell / filled / 직전 %K14 < 20에서 %K14가 %D3 상향 돌파 (한 봉 목표); 조건 미충족; K14=10.576, D3=8.00581, previous_K14=7.39787, previous_D3=7.27486; 직전 완료 봉 목표를 다음 봉 시가에 모의 적용 |
| v2 | mfi_14_recovery | 9809.63 | -190.37 | sell / filled / 직전 MFI14 < 20, 현재 MFI14 >= 20 (한 봉 목표); 조건 미충족; MFI14=30.3876, previous_MFI14=31.1747; 직전 완료 봉 목표를 다음 봉 시가에 모의 적용 |
| v2 | adx_14_trend | 9915.40 | -84.60 | buy / partial / Wilder ADX14 >= 25 그리고 +DI14 > -DI14; 조건 충족; ADX14=25.1063, plus_DI14=29.8515, minus_DI14=14.2405; 직전 완료 봉 목표를 다음 봉 시가에 모의 적용 |
| v2 | aroon_25_trend | 9825.33 | -174.67 | sell / filled / Aroon25 Up > 70 그리고 Down < 30 (동률이면 최신 극값); 조건 미충족; Aroon_up=100, Aroon_down=80; 직전 완료 봉 목표를 다음 봉 시가에 모의 적용 |
| v2 | cci_20_momentum | 9893.03 | -106.97 | sell / filled / CCI20 > 100 (전형가격·평균절대편차); 조건 미충족; CCI20=99.5288; 직전 완료 봉 목표를 다음 봉 시가에 모의 적용 |
| v2 | williams_14_recovery | 9672.18 | -327.82 | sell / filled / 직전 Williams %R14 < -80, 현재 >= -80 (한 봉 목표); 조건 미충족; Williams_R14=-78.3698, previous_R14=-75.2358; 직전 완료 봉 목표를 다음 봉 시가에 모의 적용 |
| v2 | cmf_20_accumulation | 9576.61 | -423.39 | buy / partial / Chaikin Money Flow20 > 0.1; 조건 충족; CMF20=0.185201, volume20=2.07769e+08; 직전 완료 봉 목표를 다음 봉 시가에 모의 적용 |
| v2 | chaikin_3_10 | 9759.12 | -240.88 | buy / partial / ADL의 EMA3 - EMA10 > 0 그리고 종가 > EMA26; 조건 충족; Chaikin3_10=659089, ADL=2.27792e+08, close=722.48, EMA26=719.576; 직전 완료 봉 목표를 다음 봉 시가에 모의 적용 |
| v2 | roc_10_momentum | 9957.34 | -42.66 | sell / filled / 10봉 ROC > 1% 그리고 종가 > EMA26; 조건 미충족; ROC10_percent=0.681109, close=725.78, EMA26=721.667; 직전 완료 봉 목표를 다음 봉 시가에 모의 적용 |
| v2 | trix_15_trend | 9709.50 | -290.50 | buy / partial / 15봉 삼중 EMA의 1봉 변화율 TRIX > 0 그리고 종가 > EMA26; 조건 충족; TRIX15_percent=3.24292e-05, close=721.81, EMA26=719.344; 직전 완료 봉 목표를 다음 봉 시가에 모의 적용 |
| v2 | keltner_20_breakout | 9813.08 | -186.92 | sell / filled / 종가 > EMA20 + 2 x Wilder ATR14; 조건 미충족; close=725.221, upper_Keltner=725.877, EMA20=722.517, ATR14=1.67972; 직전 완료 봉 목표를 다음 봉 시가에 모의 적용 |
| v2 | opening_range_30m | 9785.43 | -214.57 | buy / partial / 뉴욕 09:30·09:45 두 완료 봉 최고가를 10:00 이후 종가가 돌파; 조건 충족; close=723.37, opening_high=723.2; 직전 완료 봉 목표를 다음 봉 시가에 모의 적용 |

### 같은 기간의 비용·노출 비교 (사후 연구)

| 전략 | 비용 전 | 비용 후 | 100% 보유 | 같은 평균 노출 보유 | 평균 노출 |
|---|---:|---:|---:|---:|---:|
| cash | 0.00% | 0.00% | -2.69% | -0.00% | 0.00% |
| buy_hold | -2.28% | -2.69% | -2.69% | -2.69% | 100.00% |
| trend_8_26 | 0.45% | -3.68% | -2.69% | -1.12% | 41.58% |
| momentum_26 | -2.92% | -9.23% | -2.69% | -1.02% | 37.63% |
| breakout_8 | -1.43% | -16.33% | -2.69% | -0.51% | 18.95% |
| reversion_12 | -0.21% | -12.03% | -2.69% | -0.82% | 30.53% |
| volume_26 | -1.39% | -14.87% | -2.69% | -0.44% | 16.32% |
| trend_8_26 AND momentum_26 | 0.14% | -3.98% | -2.69% | -0.82% | 30.26% |
| trend_8_26 + momentum_26 | -1.24% | -5.90% | -2.69% | -1.07% | 39.61% |
| trend_8_26 AND breakout_8 | 0.35% | -7.35% | -2.69% | -0.30% | 11.05% |
| trend_8_26 + breakout_8 | -0.49% | -9.66% | -2.69% | -0.82% | 30.27% |
| trend_8_26 AND reversion_12 | -0.45% | -4.14% | -2.69% | -0.16% | 6.05% |
| trend_8_26 + reversion_12 | 0.13% | -7.37% | -2.69% | -0.97% | 36.06% |
| trend_8_26 AND volume_26 | 0.23% | -4.70% | -2.69% | -0.14% | 5.26% |
| trend_8_26 + volume_26 | -0.47% | -9.26% | -2.69% | -0.78% | 28.95% |
| momentum_26 AND breakout_8 | -0.52% | -9.30% | -2.69% | -0.32% | 11.84% |
| momentum_26 + breakout_8 | -2.18% | -12.67% | -2.69% | -0.76% | 28.30% |
| momentum_26 AND reversion_12 | -1.39% | -5.84% | -2.69% | -0.17% | 6.32% |
| momentum_26 + reversion_12 | -1.57% | -9.89% | -2.69% | -0.92% | 34.08% |
| momentum_26 AND volume_26 | -0.50% | -4.59% | -2.69% | -0.11% | 3.95% |
| momentum_26 + volume_26 | -2.15% | -11.73% | -2.69% | -0.73% | 26.98% |
| breakout_8 AND reversion_12 | 0.00% | 0.00% | -2.69% | -0.00% | 0.00% |
| breakout_8 + reversion_12 | -0.81% | -13.12% | -2.69% | -0.67% | 24.75% |
| breakout_8 AND volume_26 | 0.32% | -2.18% | -2.69% | -0.06% | 2.37% |
| breakout_8 + volume_26 | -1.41% | -14.18% | -2.69% | -0.48% | 17.64% |
| reversion_12 AND volume_26 | -1.31% | -8.11% | -2.69% | -0.23% | 8.42% |
| reversion_12 + volume_26 | -0.79% | -12.92% | -2.69% | -0.63% | 23.43% |
| ema_12_26 | -1.48% | -4.74% | -2.69% | -1.07% | 39.74% |
| macd_12_26_9 | 0.67% | -3.87% | -2.69% | -0.63% | 23.42% |
| rsi_14_recovery | -0.47% | -5.76% | -2.69% | -0.09% | 3.42% |
| bollinger_20_reentry | -0.08% | -6.18% | -2.69% | -0.11% | 3.95% |
| donchian_20 | 0.56% | -4.78% | -2.69% | -0.17% | 6.32% |
| atr_14_breakout | 0.51% | -3.62% | -2.69% | -0.08% | 2.89% |
| session_vwap | 0.29% | -11.21% | -2.69% | -1.21% | 45.00% |
| obv_20 | -1.06% | -9.79% | -2.69% | -0.72% | 26.84% |
| stochastic_14_3_recovery | 0.18% | -11.68% | -2.69% | -0.21% | 7.89% |
| mfi_14_recovery | -1.23% | -3.69% | -2.69% | -0.04% | 1.58% |
| adx_14_trend | 0.08% | -2.82% | -2.69% | -0.49% | 18.16% |
| aroon_25_trend | 1.18% | -2.16% | -2.69% | -0.42% | 15.53% |
| cci_20_momentum | -0.12% | -5.43% | -2.69% | -0.49% | 18.16% |
| williams_14_recovery | -0.13% | -10.84% | -2.69% | -0.19% | 7.11% |
| cmf_20_accumulation | -1.47% | -8.64% | -2.69% | -0.92% | 33.95% |
| chaikin_3_10 | -2.25% | -10.50% | -2.69% | -0.87% | 32.37% |
| roc_10_momentum | 0.13% | -1.54% | -2.69% | -0.13% | 4.74% |
| trix_15_trend | 0.26% | -3.46% | -2.69% | -0.87% | 32.11% |
| keltner_20_breakout | -0.83% | -5.31% | -2.69% | -0.21% | 7.63% |
| opening_range_30m | 0.01% | -5.70% | -2.69% | -0.84% | 31.05% |

동일 구간·초기 자금, 종료 시 청산 비용 포함. 노출 맞춤은 사후 설명용이며 v2 실제 계좌 성과가 아닙니다.
[낙폭 분해·비용 영향·전체 구간](QQQ/comparison.json)

[v1 전체 기록](QQQ/accounts.json) · [v2 전체 기록](QQQ/accounts-v2.json)

## IWM 계좌

| 모델 | 전략 | 평가액 USD | 손익 USD | 최근 매매·이유 |
|---|---|---:|---:|---|
| v1 | cash | 10000.00 | 0.00 | 대기 /  / 새 신호 대기 |
| v1 | buy_hold | 10031.10 | 31.10 | buy /  / buy_hold: prior completed bar target 100%; next bar open simulation |
| v1 | trend_8_26 | 9835.81 | -164.19 | buy /  / trend_8_26: prior completed bar target 100%; next bar open simulation |
| v1 | momentum_26 | 10007.30 | 7.30 | buy /  / momentum_26: prior completed bar target 100%; next bar open simulation |
| v1 | breakout_8 | 9572.95 | -427.05 | sell /  / breakout_8: prior completed bar target 0%; next bar open simulation |
| v1 | reversion_12 | 9786.62 | -213.38 | sell /  / reversion_12: prior completed bar target 0%; next bar open simulation |
| v1 | volume_26 | 9923.29 | -76.71 | sell /  / volume_26: prior completed bar target 0%; next bar open simulation |
| v1 | trend_8_26 AND momentum_26 | 9851.80 | -148.20 | buy /  / trend_8_26 AND momentum_26: prior completed bar target 100%; next bar open simulation |
| v1 | trend_8_26 + momentum_26 | 9921.25 | -78.75 | buy /  / trend_8_26 + momentum_26: prior completed bar target 100%; next bar open simulation |
| v1 | trend_8_26 AND breakout_8 | 9661.72 | -338.28 | sell /  / trend_8_26 AND breakout_8: prior completed bar target 0%; next bar open simulation |
| v1 | trend_8_26 + breakout_8 | 9703.65 | -296.35 | sell /  / trend_8_26 + breakout_8: prior completed bar target 50%; next bar open simulation |
| v1 | trend_8_26 AND reversion_12 | 9827.31 | -172.69 | sell /  / trend_8_26 AND reversion_12: prior completed bar target 0%; next bar open simulation |
| v1 | trend_8_26 + reversion_12 | 9811.02 | -188.98 | sell /  / trend_8_26 + reversion_12: prior completed bar target 50%; next bar open simulation |
| v1 | trend_8_26 AND volume_26 | 9935.98 | -64.02 | sell /  / trend_8_26 AND volume_26: prior completed bar target 0%; next bar open simulation |
| v1 | trend_8_26 + volume_26 | 9899.07 | -100.93 | sell /  / trend_8_26 + volume_26: prior completed bar target 50%; next bar open simulation |
| v1 | momentum_26 AND breakout_8 | 9710.54 | -289.46 | sell /  / momentum_26 AND breakout_8: prior completed bar target 0%; next bar open simulation |
| v1 | momentum_26 + breakout_8 | 9807.44 | -192.56 | sell /  / momentum_26 + breakout_8: prior completed bar target 50%; next bar open simulation |
| v1 | momentum_26 AND reversion_12 | 9924.34 | -75.66 | sell /  / momentum_26 AND reversion_12: prior completed bar target 0%; next bar open simulation |
| v1 | momentum_26 + reversion_12 | 9915.99 | -84.01 | sell /  / momentum_26 + reversion_12: prior completed bar target 50%; next bar open simulation |
| v1 | momentum_26 AND volume_26 | 10062.05 | 62.05 | sell /  / momentum_26 AND volume_26: prior completed bar target 0%; next bar open simulation |
| v1 | momentum_26 + volume_26 | 9965.03 | -34.97 | sell /  / momentum_26 + volume_26: prior completed bar target 50%; next bar open simulation |
| v1 | breakout_8 AND reversion_12 | 10000.00 | 0.00 | 대기 /  / 새 신호 대기 |
| v1 | breakout_8 + reversion_12 | 9679.06 | -320.94 | sell /  / breakout_8 + reversion_12: prior completed bar target 0%; next bar open simulation |
| v1 | breakout_8 AND volume_26 | 9967.28 | -32.72 | sell /  / breakout_8 AND volume_26: prior completed bar target 0%; next bar open simulation |
| v1 | breakout_8 + volume_26 | 9766.00 | -234.00 | sell /  / breakout_8 + volume_26: prior completed bar target 0%; next bar open simulation |
| v1 | reversion_12 AND volume_26 | 9935.98 | -64.02 | sell /  / reversion_12 AND volume_26: prior completed bar target 0%; next bar open simulation |
| v1 | reversion_12 + volume_26 | 9874.40 | -125.60 | sell /  / reversion_12 + volume_26: prior completed bar target 0%; next bar open simulation |
| v1 | ema_12_26 | 9901.19 | -98.81 | buy /  / EMA12 > EMA26; 조건 충족; EMA12=271.545, EMA26=271.529 |
| v1 | macd_12_26_9 | 9906.42 | -93.58 | sell /  / MACD > 신호선 그리고 MACD > 0; 조건 미충족; MACD=0.978353, signal9=1.01104 |
| v1 | rsi_14_recovery | 9786.95 | -213.05 | sell /  / 직전 RSI14 < 30, 현재 RSI14 >= 30 (한 봉 목표); 조건 미충족; RSI14=46.986, previous_RSI14=37.1649 |
| v1 | bollinger_20_reentry | 9924.03 | -75.97 | sell /  / 직전 종가 < 직전 하단밴드, 현재 하단밴드 <= 종가 <= SMA20 (한 봉 목표); 조건 미충족; close=271.19, lower20=270.018, SMA20=273.224, previous_lower20=270.283 |
| v1 | donchian_20 | 9835.91 | -164.09 | sell /  / 종가 > 현재 봉을 제외한 직전 20봉 최고가; 조건 미충족; close=275.785, prior_high20=276.875 |
| v1 | atr_14_breakout | 9849.82 | -150.18 | sell /  / 종가 > 직전 종가 + 직전 ATR14 그리고 종가 > EMA26; 조건 미충족; close=276.97, threshold=277.417, prior_ATR14=0.596703, EMA26=275.4 |
| v1 | session_vwap | 9740.46 | -259.54 | sell /  / 종가 > 뉴욕 거래일별 누적 전형가격 VWAP; 조건 미충족; close=276.595, session_VWAP=276.814, session_volume=6.52947e+06 |
| v1 | obv_20 | 9895.53 | -104.47 | buy /  / OBV > OBV의 SMA20 그리고 종가 > EMA26; 조건 충족; OBV=-3.32696e+07, OBV_SMA20=-3.46228e+07, close=272.6, EMA26=271.529 |
| v1 | stochastic_14_3_recovery | 9665.87 | -334.13 | sell /  / 직전 %K14 < 20에서 %K14가 %D3 상향 돌파 (한 봉 목표); 조건 미충족; K14=72.727, D3=41.2922, previous_K14=34.0903, previous_D3=23.8263 |
| v1 | mfi_14_recovery | 9934.22 | -65.78 | sell /  / 직전 MFI14 < 20, 현재 MFI14 >= 20 (한 봉 목표); 조건 미충족; MFI14=34.131, previous_MFI14=22.0435 |
| v1 | adx_14_trend | 9794.93 | -205.07 | sell /  / Wilder ADX14 >= 25 그리고 +DI14 > -DI14; 조건 미충족; ADX14=24.5981, plus_DI14=27.3652, minus_DI14=21.235 |
| v1 | aroon_25_trend | 9745.85 | -254.15 | sell /  / Aroon25 Up > 70 그리고 Down < 30 (동률이면 최신 극값); 조건 미충족; Aroon_up=68, Aroon_down=4 |
| v1 | cci_20_momentum | 9907.78 | -92.22 | sell /  / CCI20 > 100 (전형가격·평균절대편차); 조건 미충족; CCI20=71.4927 |
| v1 | williams_14_recovery | 9833.31 | -166.69 | sell /  / 직전 Williams %R14 < -80, 현재 >= -80 (한 봉 목표); 조건 미충족; Williams_R14=-27.273, previous_R14=-65.9097 |
| v1 | cmf_20_accumulation | 9825.75 | -174.25 | sell /  / Chaikin Money Flow20 > 0.1; 조건 미충족; CMF20=0.0815655, volume20=1.22806e+07 |
| v1 | chaikin_3_10 | 9878.06 | -121.94 | sell /  / ADL의 EMA3 - EMA10 > 0 그리고 종가 > EMA26; 조건 미충족; Chaikin3_10=-108533, ADL=-4.17289e+07, close=276.97, EMA26=275.4 |
| v1 | roc_10_momentum | 9996.39 | -3.61 | sell /  / 10봉 ROC > 1% 그리고 종가 > EMA26; 조건 미충족; ROC10_percent=0.995963, close=275.315, EMA26=273.754 |
| v1 | trix_15_trend | 9982.67 | -17.33 | buy /  / 15봉 삼중 EMA의 1봉 변화율 TRIX > 0 그리고 종가 > EMA26; 조건 충족; TRIX15_percent=0.00296855, close=273.97, EMA26=271.9 |
| v1 | keltner_20_breakout | 9879.23 | -120.77 | sell /  / 종가 > EMA20 + 2 x Wilder ATR14; 조건 미충족; close=276.4, upper_Keltner=277.094, EMA20=275.768, ATR14=0.662947 |
| v1 | opening_range_30m | 9963.15 | -36.85 | sell /  / 뉴욕 09:30·09:45 두 완료 봉 최고가를 10:00 이후 종가가 돌파; 자료 부족·변동폭 또는 거래량 없음: 대기; close=276.82 |
| v2 | cash | 10000.00 | 0.00 | 대기 /  / 새 신호 대기 |
| v2 | buy_hold | 9923.85 | -76.15 | buy / partial / 직전 완료 봉 목표 비중 100%; 다음 봉 시가 가정 |
| v2 | trend_8_26 | 9704.48 | -295.52 | buy / partial / 직전 완료 봉 목표 비중 100%; 다음 봉 시가 가정 |
| v2 | momentum_26 | 9874.69 | -125.31 | buy / partial / 직전 완료 봉 목표 비중 100%; 다음 봉 시가 가정 |
| v2 | breakout_8 | 9188.59 | -811.41 | sell / filled / 직전 완료 봉 목표 비중 0%; 다음 봉 시가 가정 |
| v2 | reversion_12 | 9325.80 | -674.20 | sell / filled / 직전 완료 봉 목표 비중 0%; 다음 봉 시가 가정 |
| v2 | volume_26 | 9434.73 | -565.27 | sell / filled / 직전 완료 봉 목표 비중 0%; 다음 봉 시가 가정 |
| v2 | trend_8_26 AND momentum_26 | 9869.15 | -130.85 | buy / partial / 직전 완료 봉 목표 비중 100%; 다음 봉 시가 가정 |
| v2 | trend_8_26 + momentum_26 | 9809.99 | -190.01 | buy / partial / 직전 완료 봉 목표 비중 100%; 다음 봉 시가 가정 |
| v2 | trend_8_26 AND breakout_8 | 9564.01 | -435.99 | sell / filled / 직전 완료 봉 목표 비중 0%; 다음 봉 시가 가정 |
| v2 | trend_8_26 + breakout_8 | 9463.16 | -536.84 | sell / filled / 직전 완료 봉 목표 비중 50%; 다음 봉 시가 가정 |
| v2 | trend_8_26 AND reversion_12 | 9705.35 | -294.65 | sell / filled / 직전 완료 봉 목표 비중 0%; 다음 봉 시가 가정 |
| v2 | trend_8_26 + reversion_12 | 9512.92 | -487.08 | sell / filled / 직전 완료 봉 목표 비중 50%; 다음 봉 시가 가정 |
| v2 | trend_8_26 AND volume_26 | 9797.73 | -202.27 | sell / filled / 직전 완료 봉 목표 비중 0%; 다음 봉 시가 가정 |
| v2 | trend_8_26 + volume_26 | 9608.74 | -391.26 | sell / filled / 직전 완료 봉 목표 비중 50%; 다음 봉 시가 가정 |
| v2 | momentum_26 AND breakout_8 | 9507.76 | -492.24 | sell / filled / 직전 완료 봉 목표 비중 0%; 다음 봉 시가 가정 |
| v2 | momentum_26 + breakout_8 | 9545.64 | -454.36 | sell / filled / 직전 완료 봉 목표 비중 50%; 다음 봉 시가 가정 |
| v2 | momentum_26 AND reversion_12 | 9881.28 | -118.72 | sell / filled / 직전 완료 봉 목표 비중 0%; 다음 봉 시가 가정 |
| v2 | momentum_26 + reversion_12 | 9636.16 | -363.84 | sell / filled / 직전 완료 봉 목표 비중 50%; 다음 봉 시가 가정 |
| v2 | momentum_26 AND volume_26 | 9957.22 | -42.78 | sell / filled / 직전 완료 봉 목표 비중 0%; 다음 봉 시가 가정 |
| v2 | momentum_26 + volume_26 | 9651.80 | -348.20 | sell / filled / 직전 완료 봉 목표 비중 50%; 다음 봉 시가 가정 |
| v2 | breakout_8 AND reversion_12 | 10000.00 | 0.00 | 대기 /  / 새 신호 대기 |
| v2 | breakout_8 + reversion_12 | 9295.37 | -704.63 | sell / filled / 직전 완료 봉 목표 비중 0%; 다음 봉 시가 가정 |
| v2 | breakout_8 AND volume_26 | 9710.25 | -289.75 | sell / filled / 직전 완료 봉 목표 비중 0%; 다음 봉 시가 가정 |
| v2 | breakout_8 + volume_26 | 9349.91 | -650.09 | sell / filled / 직전 완료 봉 목표 비중 0%; 다음 봉 시가 가정 |
| v2 | reversion_12 AND volume_26 | 9676.46 | -323.54 | sell / filled / 직전 완료 봉 목표 비중 0%; 다음 봉 시가 가정 |
| v2 | reversion_12 + volume_26 | 9419.31 | -580.69 | sell / filled / 직전 완료 봉 목표 비중 0%; 다음 봉 시가 가정 |
| v2 | ema_12_26 | 9896.24 | -103.76 | buy / partial / EMA12 > EMA26; 조건 충족; EMA12=271.545, EMA26=271.529; 직전 완료 봉 목표를 다음 봉 시가에 모의 적용 |
| v2 | macd_12_26_9 | 9900.47 | -99.53 | sell / filled / MACD > 신호선 그리고 MACD > 0; 조건 미충족; MACD=0.978353, signal9=1.01104; 직전 완료 봉 목표를 다음 봉 시가에 모의 적용 |
| v2 | rsi_14_recovery | 9779.12 | -220.88 | sell / filled / 직전 RSI14 < 30, 현재 RSI14 >= 30 (한 봉 목표); 조건 미충족; RSI14=46.986, previous_RSI14=37.1649; 직전 완료 봉 목표를 다음 봉 시가에 모의 적용 |
| v2 | bollinger_20_reentry | 9920.06 | -79.94 | sell / filled / 직전 종가 < 직전 하단밴드, 현재 하단밴드 <= 종가 <= SMA20 (한 봉 목표); 조건 미충족; close=271.19, lower20=270.018, SMA20=273.224, previous_lower20=270.283; 직전 완료 봉 목표를 다음 봉 시가에 모의 적용 |
| v2 | donchian_20 | 9830.01 | -169.99 | sell / filled / 종가 > 현재 봉을 제외한 직전 20봉 최고가; 조건 미충족; close=275.785, prior_high20=276.875; 직전 완료 봉 목표를 다음 봉 시가에 모의 적용 |
| v2 | atr_14_breakout | 9839.97 | -160.03 | sell / filled / 종가 > 직전 종가 + 직전 ATR14 그리고 종가 > EMA26; 조건 미충족; close=276.97, threshold=277.417, prior_ATR14=0.596703, EMA26=275.4; 직전 완료 봉 목표를 다음 봉 시가에 모의 적용 |
| v2 | session_vwap | 9724.89 | -275.11 | sell / filled / 종가 > 뉴욕 거래일별 누적 전형가격 VWAP; 조건 미충족; close=276.595, session_VWAP=276.814, session_volume=6.52947e+06; 직전 완료 봉 목표를 다음 봉 시가에 모의 적용 |
| v2 | obv_20 | 9886.63 | -113.37 | buy / partial / OBV > OBV의 SMA20 그리고 종가 > EMA26; 조건 충족; OBV=-2.88653e+07, OBV_SMA20=-3.02185e+07, close=272.6, EMA26=271.529; 직전 완료 봉 목표를 다음 봉 시가에 모의 적용 |
| v2 | stochastic_14_3_recovery | 9650.41 | -349.59 | sell / filled / 직전 %K14 < 20에서 %K14가 %D3 상향 돌파 (한 봉 목표); 조건 미충족; K14=72.727, D3=41.2922, previous_K14=34.0903, previous_D3=23.8263; 직전 완료 봉 목표를 다음 봉 시가에 모의 적용 |
| v2 | mfi_14_recovery | 9930.25 | -69.75 | sell / filled / 직전 MFI14 < 20, 현재 MFI14 >= 20 (한 봉 목표); 조건 미충족; MFI14=34.131, previous_MFI14=22.0435; 직전 완료 봉 목표를 다음 봉 시가에 모의 적용 |
| v2 | adx_14_trend | 9789.05 | -210.95 | sell / filled / Wilder ADX14 >= 25 그리고 +DI14 > -DI14; 조건 미충족; ADX14=24.5981, plus_DI14=27.3652, minus_DI14=21.235; 직전 완료 봉 목표를 다음 봉 시가에 모의 적용 |
| v2 | aroon_25_trend | 9736.11 | -263.89 | sell / filled / Aroon25 Up > 70 그리고 Down < 30 (동률이면 최신 극값); 조건 미충족; Aroon_up=68, Aroon_down=4; 직전 완료 봉 목표를 다음 봉 시가에 모의 적용 |
| v2 | cci_20_momentum | 9899.86 | -100.14 | sell / filled / CCI20 > 100 (전형가격·평균절대편차); 조건 미충족; CCI20=71.4927; 직전 완료 봉 목표를 다음 봉 시가에 모의 적용 |
| v2 | williams_14_recovery | 9825.45 | -174.55 | sell / filled / 직전 Williams %R14 < -80, 현재 >= -80 (한 봉 목표); 조건 미충족; Williams_R14=-27.273, previous_R14=-65.9097; 직전 완료 봉 목표를 다음 봉 시가에 모의 적용 |
| v2 | cmf_20_accumulation | 9812.00 | -188.00 | sell / filled / Chaikin Money Flow20 > 0.1; 조건 미충족; CMF20=0.0815655, volume20=1.22806e+07; 직전 완료 봉 목표를 다음 봉 시가에 모의 적용 |
| v2 | chaikin_3_10 | 9868.19 | -131.81 | sell / filled / ADL의 EMA3 - EMA10 > 0 그리고 종가 > EMA26; 조건 미충족; Chaikin3_10=-108533, ADL=-4.17289e+07, close=276.97, EMA26=275.4; 직전 완료 봉 목표를 다음 봉 시가에 모의 적용 |
| v2 | roc_10_momentum | 9994.39 | -5.61 | sell / filled / 10봉 ROC > 1% 그리고 종가 > EMA26; 조건 미충족; ROC10_percent=0.995963, close=275.315, EMA26=273.754; 직전 완료 봉 목표를 다음 봉 시가에 모의 적용 |
| v2 | trix_15_trend | 9979.67 | -20.33 | buy / partial / 15봉 삼중 EMA의 1봉 변화율 TRIX > 0 그리고 종가 > EMA26; 조건 충족; TRIX15_percent=0.00296855, close=273.97, EMA26=271.9; 직전 완료 봉 목표를 다음 봉 시가에 모의 적용 |
| v2 | keltner_20_breakout | 9873.30 | -126.70 | sell / filled / 종가 > EMA20 + 2 x Wilder ATR14; 조건 미충족; close=276.4, upper_Keltner=277.094, EMA20=275.768, ATR14=0.662947; 직전 완료 봉 목표를 다음 봉 시가에 모의 적용 |
| v2 | opening_range_30m | 9959.17 | -40.83 | sell / filled / 뉴욕 09:30·09:45 두 완료 봉 최고가를 10:00 이후 종가가 돌파; 자료 부족·변동폭 또는 거래량 없음: 대기; close=276.82; 직전 완료 봉 목표를 다음 봉 시가에 모의 적용 |

### 같은 기간의 비용·노출 비교 (사후 연구)

| 전략 | 비용 전 | 비용 후 | 100% 보유 | 같은 평균 노출 보유 | 평균 노출 |
|---|---:|---:|---:|---:|---:|
| cash | 0.00% | 0.00% | -1.18% | -0.00% | 0.00% |
| buy_hold | -0.76% | -1.18% | -1.18% | -1.18% | 100.00% |
| trend_8_26 | -0.01% | -3.31% | -1.18% | -0.58% | 48.68% |
| momentum_26 | 0.15% | -5.18% | -1.18% | -0.55% | 46.32% |
| breakout_8 | 0.18% | -13.88% | -1.18% | -0.24% | 20.00% |
| reversion_12 | -2.16% | -13.02% | -1.18% | -0.32% | 27.11% |
| volume_26 | -1.32% | -8.12% | -1.18% | -0.10% | 8.16% |
| trend_8_26 AND momentum_26 | 0.12% | -3.59% | -1.18% | -0.48% | 40.53% |
| trend_8_26 + momentum_26 | 0.07% | -3.84% | -1.18% | -0.56% | 47.50% |
| trend_8_26 AND breakout_8 | -0.03% | -8.47% | -1.18% | -0.15% | 12.63% |
| trend_8_26 + breakout_8 | 0.09% | -8.55% | -1.18% | -0.41% | 34.35% |
| trend_8_26 AND reversion_12 | -0.74% | -4.42% | -1.18% | -0.06% | 5.00% |
| trend_8_26 + reversion_12 | -1.08% | -8.30% | -1.18% | -0.45% | 37.90% |
| trend_8_26 AND volume_26 | -0.68% | -3.16% | -1.18% | -0.03% | 2.11% |
| trend_8_26 + volume_26 | -0.66% | -5.35% | -1.18% | -0.34% | 28.42% |
| momentum_26 AND breakout_8 | 0.41% | -8.45% | -1.18% | -0.15% | 12.37% |
| momentum_26 + breakout_8 | 0.17% | -9.44% | -1.18% | -0.39% | 33.16% |
| momentum_26 AND reversion_12 | 0.02% | -2.88% | -1.18% | -0.03% | 2.89% |
| momentum_26 + reversion_12 | -1.01% | -8.23% | -1.18% | -0.43% | 36.72% |
| momentum_26 AND volume_26 | 0.06% | -2.02% | -1.18% | -0.02% | 1.84% |
| momentum_26 + volume_26 | -0.58% | -6.27% | -1.18% | -0.32% | 27.24% |
| breakout_8 AND reversion_12 | 0.00% | 0.00% | -1.18% | -0.00% | 0.00% |
| breakout_8 + reversion_12 | -0.99% | -12.91% | -1.18% | -0.28% | 23.56% |
| breakout_8 AND volume_26 | -0.54% | -3.42% | -1.18% | -0.03% | 2.11% |
| breakout_8 + volume_26 | -0.57% | -10.67% | -1.18% | -0.17% | 14.09% |
| reversion_12 AND volume_26 | -0.62% | -4.31% | -1.18% | -0.05% | 3.95% |
| reversion_12 + volume_26 | -1.73% | -10.04% | -1.18% | -0.21% | 17.64% |
| ema_12_26 | 1.76% | -0.78% | -1.18% | -0.57% | 48.16% |
| macd_12_26_9 | 2.93% | 0.37% | -1.18% | -0.34% | 28.42% |
| rsi_14_recovery | -0.65% | -5.14% | -1.18% | -0.03% | 2.89% |
| bollinger_20_reentry | -0.24% | -4.35% | -1.18% | -0.03% | 2.63% |
| donchian_20 | -0.29% | -5.59% | -1.18% | -0.08% | 6.32% |
| atr_14_breakout | -0.12% | -6.61% | -1.18% | -0.05% | 4.47% |
| session_vwap | 1.32% | -8.40% | -1.18% | -0.55% | 46.05% |
| obv_20 | 1.66% | -2.52% | -1.18% | -0.52% | 43.68% |
| stochastic_14_3_recovery | -0.42% | -12.58% | -1.18% | -0.10% | 8.16% |
| mfi_14_recovery | 0.36% | -4.17% | -1.18% | -0.03% | 2.89% |
| adx_14_trend | 0.42% | -2.49% | -1.18% | -0.42% | 35.53% |
| aroon_25_trend | -0.81% | -5.29% | -1.18% | -0.26% | 21.84% |
| cci_20_momentum | -0.89% | -7.33% | -1.18% | -0.23% | 19.74% |
| williams_14_recovery | -0.07% | -8.89% | -1.18% | -0.07% | 5.79% |
| cmf_20_accumulation | -0.10% | -6.99% | -1.18% | -0.28% | 23.95% |
| chaikin_3_10 | -0.09% | -5.80% | -1.18% | -0.42% | 35.26% |
| roc_10_momentum | -0.27% | -1.93% | -1.18% | -0.07% | 5.53% |
| trix_15_trend | 1.81% | -1.14% | -1.18% | -0.46% | 38.68% |
| keltner_20_breakout | -0.34% | -4.04% | -1.18% | -0.09% | 7.89% |
| opening_range_30m | 2.93% | -1.30% | -1.18% | -0.32% | 27.37% |

동일 구간·초기 자금, 종료 시 청산 비용 포함. 노출 맞춤은 사후 설명용이며 v2 실제 계좌 성과가 아닙니다.
[낙폭 분해·비용 영향·전체 구간](IWM/comparison.json)

[v1 전체 기록](IWM/accounts.json) · [v2 전체 기록](IWM/accounts-v2.json)

## DIA 계좌

| 모델 | 전략 | 평가액 USD | 손익 USD | 최근 매매·이유 |
|---|---|---:|---:|---|
| v1 | cash | 10000.00 | 0.00 | 대기 /  / 새 신호 대기 |
| v1 | buy_hold | 10044.16 | 44.16 | buy /  / buy_hold: prior completed bar target 100%; next bar open simulation |
| v1 | trend_8_26 | 10010.67 | 10.67 | buy /  / trend_8_26: prior completed bar target 100%; next bar open simulation |
| v1 | momentum_26 | 9844.00 | -156.00 | buy /  / momentum_26: prior completed bar target 100%; next bar open simulation |
| v1 | breakout_8 | 9516.19 | -483.81 | buy /  / breakout_8: prior completed bar target 100%; next bar open simulation |
| v1 | reversion_12 | 9863.03 | -136.97 | sell /  / reversion_12: prior completed bar target 0%; next bar open simulation |
| v1 | volume_26 | 9901.29 | -98.71 | sell /  / volume_26: prior completed bar target 0%; next bar open simulation |
| v1 | trend_8_26 AND momentum_26 | 9900.00 | -100.00 | buy /  / trend_8_26 AND momentum_26: prior completed bar target 100%; next bar open simulation |
| v1 | trend_8_26 + momentum_26 | 9927.05 | -72.95 | buy /  / trend_8_26 + momentum_26: prior completed bar target 100%; next bar open simulation |
| v1 | trend_8_26 AND breakout_8 | 9740.32 | -259.68 | buy /  / trend_8_26 AND breakout_8: prior completed bar target 100%; next bar open simulation |
| v1 | trend_8_26 + breakout_8 | 9799.47 | -200.53 | buy /  / trend_8_26 + breakout_8: prior completed bar target 100%; next bar open simulation |
| v1 | trend_8_26 AND reversion_12 | 9906.37 | -93.63 | sell /  / trend_8_26 AND reversion_12: prior completed bar target 0%; next bar open simulation |
| v1 | trend_8_26 + reversion_12 | 9936.42 | -63.58 | sell /  / trend_8_26 + reversion_12: prior completed bar target 50%; next bar open simulation |
| v1 | trend_8_26 AND volume_26 | 9974.09 | -25.91 | sell /  / trend_8_26 AND volume_26: prior completed bar target 0%; next bar open simulation |
| v1 | trend_8_26 + volume_26 | 9955.66 | -44.34 | sell /  / trend_8_26 + volume_26: prior completed bar target 50%; next bar open simulation |
| v1 | momentum_26 AND breakout_8 | 9645.92 | -354.08 | buy /  / momentum_26 AND breakout_8: prior completed bar target 100%; next bar open simulation |
| v1 | momentum_26 + breakout_8 | 9678.80 | -321.20 | buy /  / momentum_26 + breakout_8: prior completed bar target 100%; next bar open simulation |
| v1 | momentum_26 AND reversion_12 | 9906.39 | -93.61 | sell /  / momentum_26 AND reversion_12: prior completed bar target 0%; next bar open simulation |
| v1 | momentum_26 + reversion_12 | 9892.82 | -107.18 | sell /  / momentum_26 + reversion_12: prior completed bar target 50%; next bar open simulation |
| v1 | momentum_26 AND volume_26 | 9891.01 | -108.99 | sell /  / momentum_26 AND volume_26: prior completed bar target 0%; next bar open simulation |
| v1 | momentum_26 + volume_26 | 9892.28 | -107.72 | sell /  / momentum_26 + volume_26: prior completed bar target 50%; next bar open simulation |
| v1 | breakout_8 AND reversion_12 | 10000.00 | 0.00 | 대기 /  / 새 신호 대기 |
| v1 | breakout_8 + reversion_12 | 9707.28 | -292.72 | buy /  / breakout_8 + reversion_12: prior completed bar target 50%; next bar open simulation |
| v1 | breakout_8 AND volume_26 | 9947.52 | -52.48 | sell /  / breakout_8 AND volume_26: prior completed bar target 0%; next bar open simulation |
| v1 | breakout_8 + volume_26 | 9745.65 | -254.35 | buy /  / breakout_8 + volume_26: prior completed bar target 50%; next bar open simulation |
| v1 | reversion_12 AND volume_26 | 9970.42 | -29.58 | sell /  / reversion_12 AND volume_26: prior completed bar target 0%; next bar open simulation |
| v1 | reversion_12 + volume_26 | 9901.82 | -98.18 | sell /  / reversion_12 + volume_26: prior completed bar target 0%; next bar open simulation |
| v1 | ema_12_26 | 9898.31 | -101.69 | buy /  / EMA12 > EMA26; 조건 충족; EMA12=519.74, EMA26=519.585 |
| v1 | macd_12_26_9 | 9886.92 | -113.08 | buy /  / MACD > 신호선 그리고 MACD > 0; 조건 충족; MACD=0.578657, signal9=0.526919 |
| v1 | rsi_14_recovery | 10000.00 | 0.00 | 대기 /  / 새 신호 대기 |
| v1 | bollinger_20_reentry | 9978.51 | -21.49 | sell /  / 직전 종가 < 직전 하단밴드, 현재 하단밴드 <= 종가 <= SMA20 (한 봉 목표); 조건 미충족; close=519.823, lower20=518.355, SMA20=521.612, previous_lower20=518.548 |
| v1 | donchian_20 | 9822.00 | -178.00 | sell /  / 종가 > 현재 봉을 제외한 직전 20봉 최고가; 조건 미충족; close=523.68, prior_high20=526.17 |
| v1 | atr_14_breakout | 9804.37 | -195.63 | sell /  / 종가 > 직전 종가 + 직전 ATR14 그리고 종가 > EMA26; 조건 미충족; close=524.62, threshold=525.055, prior_ATR14=0.664902, EMA26=523.373 |
| v1 | session_vwap | 9853.48 | -146.52 | buy /  / 종가 > 뉴욕 거래일별 누적 전형가격 VWAP; 조건 충족; close=525.38, session_VWAP=524.679, session_volume=1.14471e+06 |
| v1 | obv_20 | 9859.04 | -140.96 | buy /  / OBV > OBV의 SMA20 그리고 종가 > EMA26; 조건 충족; OBV=-8.96454e+06, OBV_SMA20=-9.07774e+06, close=523.66, EMA26=523.184 |
| v1 | stochastic_14_3_recovery | 9740.52 | -259.48 | sell /  / 직전 %K14 < 20에서 %K14가 %D3 상향 돌파 (한 봉 목표); 조건 미충족; K14=29.7295, D3=26.3059, previous_K14=30.81, previous_D3=22.4321 |
| v1 | mfi_14_recovery | 9902.01 | -97.99 | sell /  / 직전 MFI14 < 20, 현재 MFI14 >= 20 (한 봉 목표); 조건 미충족; MFI14=29.4378, previous_MFI14=21.6288 |
| v1 | adx_14_trend | 9811.65 | -188.35 | sell /  / Wilder ADX14 >= 25 그리고 +DI14 > -DI14; 조건 미충족; ADX14=24.7281, plus_DI14=33.8838, minus_DI14=22.7145 |
| v1 | aroon_25_trend | 9889.87 | -110.13 | sell /  / Aroon25 Up > 70 그리고 Down < 30 (동률이면 최신 극값); 조건 미충족; Aroon_up=76, Aroon_down=84 |
| v1 | cci_20_momentum | 9856.97 | -143.03 | buy /  / CCI20 > 100 (전형가격·평균절대편차); 조건 충족; CCI20=182.27 |
| v1 | williams_14_recovery | 9773.54 | -226.46 | sell /  / 직전 Williams %R14 < -80, 현재 >= -80 (한 봉 목표); 조건 미충족; Williams_R14=-70.2705, previous_R14=-69.19 |
| v1 | cmf_20_accumulation | 9631.07 | -368.93 | sell /  / Chaikin Money Flow20 > 0.1; 조건 미충족; CMF20=0.0877103, volume20=2.12813e+06 |
| v1 | chaikin_3_10 | 9866.22 | -133.78 | buy /  / ADL의 EMA3 - EMA10 > 0 그리고 종가 > EMA26; 조건 충족; Chaikin3_10=17236.9, ADL=-1.53967e+07, close=523.66, EMA26=523.184 |
| v1 | roc_10_momentum | 9939.01 | -60.99 | sell /  / 10봉 ROC > 1% 그리고 종가 > EMA26; 조건 미충족; ROC10_percent=0.771645, close=523.68, EMA26=521.367 |
| v1 | trix_15_trend | 10000.23 | 0.23 | buy /  / 15봉 삼중 EMA의 1봉 변화율 TRIX > 0 그리고 종가 > EMA26; 조건 충족; TRIX15_percent=0.000473967, close=521.46, EMA26=519.585 |
| v1 | keltner_20_breakout | 9944.49 | -55.51 | sell /  / 종가 > EMA20 + 2 x Wilder ATR14; 조건 미충족; close=523.68, upper_Keltner=523.985, EMA20=521.785, ATR14=1.10038 |
| v1 | opening_range_30m | 9742.52 | -257.48 | sell /  / 뉴욕 09:30·09:45 두 완료 봉 최고가를 10:00 이후 종가가 돌파; 자료 부족·변동폭 또는 거래량 없음: 대기; close=524.62 |
| v2 | cash | 10000.00 | 0.00 | 대기 /  / 새 신호 대기 |
| v2 | buy_hold | 10168.60 | 168.60 | buy / partial / 직전 완료 봉 목표 비중 100%; 다음 봉 시가 가정 |
| v2 | trend_8_26 | 9941.84 | -58.16 | buy / partial / 직전 완료 봉 목표 비중 100%; 다음 봉 시가 가정 |
| v2 | momentum_26 | 9879.85 | -120.15 | buy / partial / 직전 완료 봉 목표 비중 100%; 다음 봉 시가 가정 |
| v2 | breakout_8 | 9045.69 | -954.31 | buy / partial / 직전 완료 봉 목표 비중 100%; 다음 봉 시가 가정 |
| v2 | reversion_12 | 9557.55 | -442.45 | sell / filled / 직전 완료 봉 목표 비중 0%; 다음 봉 시가 가정 |
| v2 | volume_26 | 9612.66 | -387.34 | sell / filled / 직전 완료 봉 목표 비중 0%; 다음 봉 시가 가정 |
| v2 | trend_8_26 AND momentum_26 | 9931.45 | -68.55 | buy / partial / 직전 완료 봉 목표 비중 100%; 다음 봉 시가 가정 |
| v2 | trend_8_26 + momentum_26 | 9910.94 | -89.06 | buy / partial / 직전 완료 봉 목표 비중 100%; 다음 봉 시가 가정 |
| v2 | trend_8_26 AND breakout_8 | 9422.94 | -577.06 | buy / partial / 직전 완료 봉 목표 비중 100%; 다음 봉 시가 가정 |
| v2 | trend_8_26 + breakout_8 | 9523.21 | -476.79 | buy / partial / 직전 완료 봉 목표 비중 100%; 다음 봉 시가 가정 |
| v2 | trend_8_26 AND reversion_12 | 9713.09 | -286.91 | sell / filled / 직전 완료 봉 목표 비중 0%; 다음 봉 시가 가정 |
| v2 | trend_8_26 + reversion_12 | 9747.38 | -252.62 | sell / filled / 직전 완료 봉 목표 비중 50%; 다음 봉 시가 가정 |
| v2 | trend_8_26 AND volume_26 | 9827.44 | -172.56 | sell / filled / 직전 완료 봉 목표 비중 0%; 다음 봉 시가 가정 |
| v2 | trend_8_26 + volume_26 | 9796.19 | -203.81 | sell / filled / 직전 완료 봉 목표 비중 50%; 다음 봉 시가 가정 |
| v2 | momentum_26 AND breakout_8 | 9319.13 | -680.87 | buy / partial / 직전 완료 봉 목표 비중 100%; 다음 봉 시가 가정 |
| v2 | momentum_26 + breakout_8 | 9453.80 | -546.20 | buy / partial / 직전 완료 봉 목표 비중 100%; 다음 봉 시가 가정 |
| v2 | momentum_26 AND reversion_12 | 9858.83 | -141.17 | sell / filled / 직전 완료 봉 목표 비중 0%; 다음 봉 시가 가정 |
| v2 | momentum_26 + reversion_12 | 9757.89 | -242.11 | sell / filled / 직전 완료 봉 목표 비중 50%; 다음 봉 시가 가정 |
| v2 | momentum_26 AND volume_26 | 9676.97 | -323.03 | sell / filled / 직전 완료 봉 목표 비중 0%; 다음 봉 시가 가정 |
| v2 | momentum_26 + volume_26 | 9806.92 | -193.08 | sell / filled / 직전 완료 봉 목표 비중 50%; 다음 봉 시가 가정 |
| v2 | breakout_8 AND reversion_12 | 10000.00 | 0.00 | 대기 /  / 새 신호 대기 |
| v2 | breakout_8 + reversion_12 | 9317.03 | -682.97 | buy / filled / 직전 완료 봉 목표 비중 50%; 다음 봉 시가 가정 |
| v2 | breakout_8 AND volume_26 | 9741.25 | -258.75 | sell / filled / 직전 완료 봉 목표 비중 0%; 다음 봉 시가 가정 |
| v2 | breakout_8 + volume_26 | 9363.87 | -636.13 | buy / filled / 직전 완료 봉 목표 비중 50%; 다음 봉 시가 가정 |
| v2 | reversion_12 AND volume_26 | 9966.44 | -33.56 | sell / filled / 직전 완료 봉 목표 비중 0%; 다음 봉 시가 가정 |
| v2 | reversion_12 + volume_26 | 9604.84 | -395.16 | sell / filled / 직전 완료 봉 목표 비중 0%; 다음 봉 시가 가정 |
| v2 | ema_12_26 | 9893.37 | -106.63 | buy / partial / EMA12 > EMA26; 조건 충족; EMA12=519.74, EMA26=519.585; 직전 완료 봉 목표를 다음 봉 시가에 모의 적용 |
| v2 | macd_12_26_9 | 9880.00 | -120.00 | buy / partial / MACD > 신호선 그리고 MACD > 0; 조건 충족; MACD=0.578657, signal9=0.526919; 직전 완료 봉 목표를 다음 봉 시가에 모의 적용 |
| v2 | rsi_14_recovery | 10000.00 | 0.00 | 대기 /  / 새 신호 대기 |
| v2 | bollinger_20_reentry | 9976.52 | -23.48 | sell / filled / 직전 종가 < 직전 하단밴드, 현재 하단밴드 <= 종가 <= SMA20 (한 봉 목표); 조건 미충족; close=519.823, lower20=518.355, SMA20=521.612, previous_lower20=518.548; 직전 완료 봉 목표를 다음 봉 시가에 모의 적용 |
| v2 | donchian_20 | 9814.14 | -185.86 | sell / filled / 종가 > 현재 봉을 제외한 직전 20봉 최고가; 조건 미충족; close=523.68, prior_high20=526.17; 직전 완료 봉 목표를 다음 봉 시가에 모의 적용 |
| v2 | atr_14_breakout | 9794.57 | -205.43 | sell / filled / 종가 > 직전 종가 + 직전 ATR14 그리고 종가 > EMA26; 조건 미충족; close=524.62, threshold=525.055, prior_ATR14=0.664902, EMA26=523.373; 직전 완료 봉 목표를 다음 봉 시가에 모의 적용 |
| v2 | session_vwap | 9842.65 | -157.35 | buy / partial / 종가 > 뉴욕 거래일별 누적 전형가격 VWAP; 조건 충족; close=525.38, session_VWAP=524.679, session_volume=1.14471e+06; 직전 완료 봉 목표를 다음 봉 시가에 모의 적용 |
| v2 | obv_20 | 9850.17 | -149.83 | buy / partial / OBV > OBV의 SMA20 그리고 종가 > EMA26; 조건 충족; OBV=-9.15207e+06, OBV_SMA20=-9.26528e+06, close=523.66, EMA26=523.184; 직전 완료 봉 목표를 다음 봉 시가에 모의 적용 |
| v2 | stochastic_14_3_recovery | 9726.89 | -273.11 | sell / filled / 직전 %K14 < 20에서 %K14가 %D3 상향 돌파 (한 봉 목표); 조건 미충족; K14=29.7295, D3=26.3059, previous_K14=30.81, previous_D3=22.4321; 직전 완료 봉 목표를 다음 봉 시가에 모의 적용 |
| v2 | mfi_14_recovery | 9896.07 | -103.93 | sell / filled / 직전 MFI14 < 20, 현재 MFI14 >= 20 (한 봉 목표); 조건 미충족; MFI14=29.4378, previous_MFI14=21.6288; 직전 완료 봉 목표를 다음 봉 시가에 모의 적용 |
| v2 | adx_14_trend | 9805.77 | -194.23 | sell / filled / Wilder ADX14 >= 25 그리고 +DI14 > -DI14; 조건 미충족; ADX14=24.7281, plus_DI14=33.8838, minus_DI14=22.7145; 직전 완료 봉 목표를 다음 봉 시가에 모의 적용 |
| v2 | aroon_25_trend | 9881.96 | -118.04 | sell / filled / Aroon25 Up > 70 그리고 Down < 30 (동률이면 최신 극값); 조건 미충족; Aroon_up=76, Aroon_down=84; 직전 완료 봉 목표를 다음 봉 시가에 모의 적용 |
| v2 | cci_20_momentum | 9848.10 | -151.90 | buy / partial / CCI20 > 100 (전형가격·평균절대편차); 조건 충족; CCI20=182.27; 직전 완료 봉 목표를 다음 봉 시가에 모의 적용 |
| v2 | williams_14_recovery | 9761.82 | -238.18 | sell / filled / 직전 Williams %R14 < -80, 현재 >= -80 (한 봉 목표); 조건 미충족; Williams_R14=-70.2705, previous_R14=-69.19; 직전 완료 봉 목표를 다음 봉 시가에 모의 적용 |
| v2 | cmf_20_accumulation | 9615.68 | -384.32 | sell / filled / Chaikin Money Flow20 > 0.1; 조건 미충족; CMF20=0.0877103, volume20=2.12813e+06; 직전 완료 봉 목표를 다음 봉 시가에 모의 적용 |
| v2 | chaikin_3_10 | 9857.35 | -142.65 | buy / partial / ADL의 EMA3 - EMA10 > 0 그리고 종가 > EMA26; 조건 충족; Chaikin3_10=17236.9, ADL=-1.59365e+07, close=523.66, EMA26=523.184; 직전 완료 봉 목표를 다음 봉 시가에 모의 적용 |
| v2 | roc_10_momentum | 9937.03 | -62.97 | sell / filled / 10봉 ROC > 1% 그리고 종가 > EMA26; 조건 미충족; ROC10_percent=0.771645, close=523.68, EMA26=521.367; 직전 완료 봉 목표를 다음 봉 시가에 모의 적용 |
| v2 | trix_15_trend | 9997.23 | -2.77 | buy / partial / 15봉 삼중 EMA의 1봉 변화율 TRIX > 0 그리고 종가 > EMA26; 조건 충족; TRIX15_percent=0.000473967, close=521.46, EMA26=519.585; 직전 완료 봉 목표를 다음 봉 시가에 모의 적용 |
| v2 | keltner_20_breakout | 9940.51 | -59.49 | sell / filled / 종가 > EMA20 + 2 x Wilder ATR14; 조건 미충족; close=523.68, upper_Keltner=523.985, EMA20=521.785, ATR14=1.10038; 직전 완료 봉 목표를 다음 봉 시가에 모의 적용 |
| v2 | opening_range_30m | 9730.84 | -269.16 | sell / filled / 뉴욕 09:30·09:45 두 완료 봉 최고가를 10:00 이후 종가가 돌파; 자료 부족·변동폭 또는 거래량 없음: 대기; close=524.62; 직전 완료 봉 목표를 다음 봉 시가에 모의 적용 |

### 같은 기간의 비용·노출 비교 (사후 연구)

| 전략 | 비용 전 | 비용 후 | 100% 보유 | 같은 평균 노출 보유 | 평균 노출 |
|---|---:|---:|---:|---:|---:|
| cash | 0.00% | 0.00% | 2.62% | 0.00% | 0.00% |
| buy_hold | 3.05% | 2.62% | 2.62% | 2.62% | 100.00% |
| trend_8_26 | 3.35% | -0.48% | 2.62% | 1.64% | 62.63% |
| momentum_26 | 1.41% | -2.76% | 2.62% | 1.51% | 57.89% |
| breakout_8 | 0.39% | -17.60% | 2.62% | 0.64% | 24.74% |
| reversion_12 | -0.46% | -7.71% | 2.62% | 0.53% | 20.26% |
| volume_26 | 0.40% | -9.60% | 2.62% | 0.28% | 10.79% |
| trend_8_26 AND momentum_26 | 3.01% | -1.22% | 2.62% | 1.37% | 52.63% |
| trend_8_26 + momentum_26 | 2.38% | -1.62% | 2.62% | 1.57% | 60.27% |
| trend_8_26 AND breakout_8 | 1.36% | -11.76% | 2.62% | 0.44% | 16.84% |
| trend_8_26 + breakout_8 | 1.86% | -8.87% | 2.62% | 1.14% | 43.69% |
| trend_8_26 AND reversion_12 | 0.42% | -4.12% | 2.62% | 0.16% | 6.32% |
| trend_8_26 + reversion_12 | 1.43% | -3.97% | 2.62% | 1.08% | 41.45% |
| trend_8_26 AND volume_26 | 1.66% | -3.75% | 2.62% | 0.14% | 5.53% |
| trend_8_26 + volume_26 | 1.87% | -4.96% | 2.62% | 0.96% | 36.72% |
| momentum_26 AND breakout_8 | -0.05% | -13.35% | 2.62% | 0.47% | 18.16% |
| momentum_26 + breakout_8 | 0.91% | -10.29% | 2.62% | 1.08% | 41.32% |
| momentum_26 AND reversion_12 | -0.29% | -2.77% | 2.62% | 0.12% | 4.74% |
| momentum_26 + reversion_12 | 0.48% | -4.47% | 2.62% | 1.02% | 39.08% |
| momentum_26 AND volume_26 | 0.11% | -6.00% | 2.62% | 0.15% | 5.79% |
| momentum_26 + volume_26 | 0.91% | -5.65% | 2.62% | 0.90% | 34.35% |
| breakout_8 AND reversion_12 | 0.00% | 0.00% | 2.62% | 0.00% | 0.00% |
| breakout_8 + reversion_12 | -0.03% | -12.44% | 2.62% | 0.59% | 22.51% |
| breakout_8 AND volume_26 | -0.45% | -4.15% | 2.62% | 0.09% | 3.42% |
| breakout_8 + volume_26 | 0.40% | -12.79% | 2.62% | 0.46% | 17.77% |
| reversion_12 AND volume_26 | 0.29% | -4.24% | 2.62% | 0.09% | 3.42% |
| reversion_12 + volume_26 | -0.03% | -8.47% | 2.62% | 0.40% | 15.53% |
| ema_12_26 | 1.20% | -1.32% | 2.62% | 1.50% | 57.63% |
| macd_12_26_9 | 2.36% | -1.43% | 2.62% | 0.81% | 31.05% |
| rsi_14_recovery | 0.16% | -1.09% | 2.62% | 0.02% | 0.79% |
| bollinger_20_reentry | 0.20% | -3.11% | 2.62% | 0.05% | 2.11% |
| donchian_20 | 0.36% | -6.94% | 2.62% | 0.25% | 9.74% |
| atr_14_breakout | -0.69% | -8.30% | 2.62% | 0.16% | 6.05% |
| session_vwap | 3.12% | -3.98% | 2.62% | 1.46% | 55.79% |
| obv_20 | 1.59% | -6.20% | 2.62% | 1.28% | 48.95% |
| stochastic_14_3_recovery | 0.87% | -11.07% | 2.62% | 0.21% | 7.89% |
| mfi_14_recovery | 0.22% | -3.50% | 2.62% | 0.06% | 2.37% |
| adx_14_trend | 0.13% | -3.59% | 2.62% | 0.81% | 31.05% |
| aroon_25_trend | 1.63% | -2.14% | 2.62% | 0.70% | 26.84% |
| cci_20_momentum | 1.18% | -5.40% | 2.62% | 0.70% | 26.84% |
| williams_14_recovery | 1.55% | -5.84% | 2.62% | 0.12% | 4.74% |
| cmf_20_accumulation | 1.03% | -7.89% | 2.62% | 0.89% | 34.21% |
| chaikin_3_10 | 2.72% | -6.73% | 2.62% | 1.32% | 50.53% |
| roc_10_momentum | -0.07% | -0.90% | 2.62% | 0.05% | 2.11% |
| trix_15_trend | 1.32% | -2.03% | 2.62% | 1.35% | 51.84% |
| keltner_20_breakout | 0.78% | -5.77% | 2.62% | 0.48% | 18.42% |
| opening_range_30m | 1.64% | -4.56% | 2.62% | 0.78% | 30.00% |

동일 구간·초기 자금, 종료 시 청산 비용 포함. 노출 맞춤은 사후 설명용이며 v2 실제 계좌 성과가 아닙니다.
[낙폭 분해·비용 영향·전체 구간](DIA/comparison.json)

[v1 전체 기록](DIA/accounts.json) · [v2 전체 기록](DIA/accounts-v2.json)

## MSFT 계좌

| 모델 | 전략 | 평가액 USD | 손익 USD | 최근 매매·이유 |
|---|---|---:|---:|---|
| v1 | cash | 10000.00 | 0.00 | 대기 /  / 새 신호 대기 |
| v1 | buy_hold | 9823.61 | -176.39 | buy /  / buy_hold: prior completed bar target 100%; next bar open simulation |
| v1 | trend_8_26 | 9581.90 | -418.10 | sell /  / trend_8_26: prior completed bar target 0%; next bar open simulation |
| v1 | momentum_26 | 9524.88 | -475.12 | sell /  / momentum_26: prior completed bar target 0%; next bar open simulation |
| v1 | breakout_8 | 9646.14 | -353.86 | sell /  / breakout_8: prior completed bar target 0%; next bar open simulation |
| v1 | reversion_12 | 9552.38 | -447.62 | sell /  / reversion_12: prior completed bar target 0%; next bar open simulation |
| v1 | volume_26 | 9722.84 | -277.16 | sell /  / volume_26: prior completed bar target 0%; next bar open simulation |
| v1 | trend_8_26 AND momentum_26 | 9662.97 | -337.03 | sell /  / trend_8_26 AND momentum_26: prior completed bar target 0%; next bar open simulation |
| v1 | trend_8_26 + momentum_26 | 9591.58 | -408.42 | sell /  / trend_8_26 + momentum_26: prior completed bar target 0%; next bar open simulation |
| v1 | trend_8_26 AND breakout_8 | 9820.11 | -179.89 | sell /  / trend_8_26 AND breakout_8: prior completed bar target 0%; next bar open simulation |
| v1 | trend_8_26 + breakout_8 | 9652.70 | -347.30 | sell /  / trend_8_26 + breakout_8: prior completed bar target 0%; next bar open simulation |
| v1 | trend_8_26 AND reversion_12 | 9627.16 | -372.84 | sell /  / trend_8_26 AND reversion_12: prior completed bar target 0%; next bar open simulation |
| v1 | trend_8_26 + reversion_12 | 9586.21 | -413.79 | sell /  / trend_8_26 + reversion_12: prior completed bar target 0%; next bar open simulation |
| v1 | trend_8_26 AND volume_26 | 9894.93 | -105.07 | sell /  / trend_8_26 AND volume_26: prior completed bar target 0%; next bar open simulation |
| v1 | trend_8_26 + volume_26 | 9652.28 | -347.72 | sell /  / trend_8_26 + volume_26: prior completed bar target 0%; next bar open simulation |
| v1 | momentum_26 AND breakout_8 | 9778.34 | -221.66 | sell /  / momentum_26 AND breakout_8: prior completed bar target 0%; next bar open simulation |
| v1 | momentum_26 + breakout_8 | 9604.75 | -395.25 | sell /  / momentum_26 + breakout_8: prior completed bar target 0%; next bar open simulation |
| v1 | momentum_26 AND reversion_12 | 9649.76 | -350.24 | sell /  / momentum_26 AND reversion_12: prior completed bar target 0%; next bar open simulation |
| v1 | momentum_26 + reversion_12 | 9538.53 | -461.47 | sell /  / momentum_26 + reversion_12: prior completed bar target 0%; next bar open simulation |
| v1 | momentum_26 AND volume_26 | 9830.16 | -169.84 | sell /  / momentum_26 AND volume_26: prior completed bar target 0%; next bar open simulation |
| v1 | momentum_26 + volume_26 | 9623.58 | -376.42 | sell /  / momentum_26 + volume_26: prior completed bar target 0%; next bar open simulation |
| v1 | breakout_8 AND reversion_12 | 10000.00 | 0.00 | 대기 /  / 새 신호 대기 |
| v1 | breakout_8 + reversion_12 | 9618.22 | -381.78 | sell /  / breakout_8 + reversion_12: prior completed bar target 0%; next bar open simulation |
| v1 | breakout_8 AND volume_26 | 9953.19 | -46.81 | sell /  / breakout_8 AND volume_26: prior completed bar target 0%; next bar open simulation |
| v1 | breakout_8 + volume_26 | 9703.60 | -296.40 | sell /  / breakout_8 + volume_26: prior completed bar target 0%; next bar open simulation |
| v1 | reversion_12 AND volume_26 | 9863.28 | -136.72 | sell /  / reversion_12 AND volume_26: prior completed bar target 0%; next bar open simulation |
| v1 | reversion_12 + volume_26 | 9656.47 | -343.53 | sell /  / reversion_12 + volume_26: prior completed bar target 0%; next bar open simulation |
| v1 | ema_12_26 | 9588.87 | -411.13 | sell /  / EMA12 > EMA26; 조건 미충족; EMA12=532.137, EMA26=532.175 |
| v1 | macd_12_26_9 | 9762.31 | -237.69 | sell /  / MACD > 신호선 그리고 MACD > 0; 조건 미충족; MACD=-0.0387557, signal9=-0.0148606 |
| v1 | rsi_14_recovery | 9957.14 | -42.86 | sell /  / 직전 RSI14 < 30, 현재 RSI14 >= 30 (한 봉 목표); 조건 미충족; RSI14=45.5102, previous_RSI14=37.5844 |
| v1 | bollinger_20_reentry | 9813.80 | -186.20 | sell /  / 직전 종가 < 직전 하단밴드, 현재 하단밴드 <= 종가 <= SMA20 (한 봉 목표); 조건 미충족; close=529.335, lower20=528.85, SMA20=531.508, previous_lower20=529.166 |
| v1 | donchian_20 | 9912.16 | -87.84 | sell /  / 종가 > 현재 봉을 제외한 직전 20봉 최고가; 조건 미충족; close=534.52, prior_high20=535.44 |
| v1 | atr_14_breakout | 9915.10 | -84.90 | sell /  / 종가 > 직전 종가 + 직전 ATR14 그리고 종가 > EMA26; 조건 미충족; close=533.975, threshold=536.307, prior_ATR14=2.16203, EMA26=530.521 |
| v1 | session_vwap | 9844.14 | -155.86 | buy /  / 종가 > 뉴욕 거래일별 누적 전형가격 VWAP; 조건 충족; close=530.964, session_VWAP=530.832, session_volume=8.43578e+06 |
| v1 | obv_20 | 9670.99 | -329.01 | buy /  / OBV > OBV의 SMA20 그리고 종가 > EMA26; 조건 충족; OBV=9.04505e+07, OBV_SMA20=9.01119e+07, close=531.15, EMA26=531.118 |
| v1 | stochastic_14_3_recovery | 9789.03 | -210.97 | sell /  / 직전 %K14 < 20에서 %K14가 %D3 상향 돌파 (한 봉 목표); 조건 미충족; K14=60.6262, D3=34.5689, previous_K14=38.87, previous_D3=26.948 |
| v1 | mfi_14_recovery | 9972.58 | -27.42 | sell /  / 직전 MFI14 < 20, 현재 MFI14 >= 20 (한 봉 목표); 조건 미충족; MFI14=53.413, previous_MFI14=44.3372 |
| v1 | adx_14_trend | 9883.62 | -116.38 | sell /  / Wilder ADX14 >= 25 그리고 +DI14 > -DI14; 조건 미충족; ADX14=23.6824, plus_DI14=22.3066, minus_DI14=19.9214 |
| v1 | aroon_25_trend | 9812.47 | -187.53 | sell /  / Aroon25 Up > 70 그리고 Down < 30 (동률이면 최신 극값); 조건 미충족; Aroon_up=68, Aroon_down=20 |
| v1 | cci_20_momentum | 9949.66 | -50.34 | sell /  / CCI20 > 100 (전형가격·평균절대편차); 조건 미충족; CCI20=69.3811 |
| v1 | williams_14_recovery | 9752.02 | -247.98 | sell /  / 직전 Williams %R14 < -80, 현재 >= -80 (한 봉 목표); 조건 미충족; Williams_R14=-49.2857, previous_R14=-77.0479 |
| v1 | cmf_20_accumulation | 9682.91 | -317.09 | buy /  / Chaikin Money Flow20 > 0.1; 조건 충족; CMF20=0.135675, volume20=5.00055e+06 |
| v1 | chaikin_3_10 | 9709.46 | -290.54 | buy /  / ADL의 EMA3 - EMA10 > 0 그리고 종가 > EMA26; 조건 충족; Chaikin3_10=2.08944e+06, ADL=1.17343e+08, close=531.15, EMA26=531.118 |
| v1 | roc_10_momentum | 9959.43 | -40.57 | sell /  / 10봉 ROC > 1% 그리고 종가 > EMA26; 조건 미충족; ROC10_percent=0.454191, close=534.125, EMA26=532.186 |
| v1 | trix_15_trend | 9712.42 | -287.58 | sell /  / 15봉 삼중 EMA의 1봉 변화율 TRIX > 0 그리고 종가 > EMA26; 조건 미충족; TRIX15_percent=0.0172213, close=526.676, EMA26=532.897 |
| v1 | keltner_20_breakout | 9958.78 | -41.22 | sell /  / 종가 > EMA20 + 2 x Wilder ATR14; 조건 미충족; close=533.975, upper_Keltner=534.357, EMA20=530.111, ATR14=2.12332 |
| v1 | opening_range_30m | 9710.44 | -289.56 | buy /  / 뉴욕 09:30·09:45 두 완료 봉 최고가를 10:00 이후 종가가 돌파; 조건 충족; close=531.65, opening_high=531.48 |
| v2 | cash | 10000.00 | 0.00 | 대기 /  / 새 신호 대기 |
| v2 | buy_hold | 9877.22 | -122.78 | buy / partial / 직전 완료 봉 목표 비중 100%; 다음 봉 시가 가정 |
| v2 | trend_8_26 | 9516.34 | -483.66 | sell / filled / 직전 완료 봉 목표 비중 0%; 다음 봉 시가 가정 |
| v2 | momentum_26 | 9562.59 | -437.41 | sell / filled / 직전 완료 봉 목표 비중 0%; 다음 봉 시가 가정 |
| v2 | breakout_8 | 9433.83 | -566.17 | sell / filled / 직전 완료 봉 목표 비중 0%; 다음 봉 시가 가정 |
| v2 | reversion_12 | 9175.21 | -824.79 | sell / filled / 직전 완료 봉 목표 비중 0%; 다음 봉 시가 가정 |
| v2 | volume_26 | 9406.85 | -593.15 | sell / filled / 직전 완료 봉 목표 비중 0%; 다음 봉 시가 가정 |
| v2 | trend_8_26 AND momentum_26 | 9560.49 | -439.51 | sell / filled / 직전 완료 봉 목표 비중 0%; 다음 봉 시가 가정 |
| v2 | trend_8_26 + momentum_26 | 9579.76 | -420.24 | sell / filled / 직전 완료 봉 목표 비중 0%; 다음 봉 시가 가정 |
| v2 | trend_8_26 AND breakout_8 | 9458.32 | -541.68 | sell / filled / 직전 완료 봉 목표 비중 0%; 다음 봉 시가 가정 |
| v2 | trend_8_26 + breakout_8 | 9535.27 | -464.73 | sell / filled / 직전 완료 봉 목표 비중 0%; 다음 봉 시가 가정 |
| v2 | trend_8_26 AND reversion_12 | 9521.46 | -478.54 | sell / filled / 직전 완료 봉 목표 비중 0%; 다음 봉 시가 가정 |
| v2 | trend_8_26 + reversion_12 | 9363.46 | -636.54 | sell / filled / 직전 완료 봉 목표 비중 0%; 다음 봉 시가 가정 |
| v2 | trend_8_26 AND volume_26 | 9838.23 | -161.77 | sell / filled / 직전 완료 봉 목표 비중 0%; 다음 봉 시가 가정 |
| v2 | trend_8_26 + volume_26 | 9481.28 | -518.72 | sell / filled / 직전 완료 봉 목표 비중 0%; 다음 봉 시가 가정 |
| v2 | momentum_26 AND breakout_8 | 9567.71 | -432.29 | sell / filled / 직전 완료 봉 목표 비중 0%; 다음 봉 시가 가정 |
| v2 | momentum_26 + breakout_8 | 9518.27 | -481.73 | sell / filled / 직전 완료 봉 목표 비중 0%; 다음 봉 시가 가정 |
| v2 | momentum_26 AND reversion_12 | 9475.12 | -524.88 | sell / filled / 직전 완료 봉 목표 비중 0%; 다음 봉 시가 가정 |
| v2 | momentum_26 + reversion_12 | 9366.60 | -633.40 | sell / filled / 직전 완료 봉 목표 비중 0%; 다음 봉 시가 가정 |
| v2 | momentum_26 AND volume_26 | 9695.84 | -304.16 | sell / filled / 직전 완료 봉 목표 비중 0%; 다음 봉 시가 가정 |
| v2 | momentum_26 + volume_26 | 9504.50 | -495.50 | sell / filled / 직전 완료 봉 목표 비중 0%; 다음 봉 시가 가정 |
| v2 | breakout_8 AND reversion_12 | 10000.00 | 0.00 | 대기 /  / 새 신호 대기 |
| v2 | breakout_8 + reversion_12 | 9342.40 | -657.60 | sell / filled / 직전 완료 봉 목표 비중 0%; 다음 봉 시가 가정 |
| v2 | breakout_8 AND volume_26 | 9890.09 | -109.91 | sell / filled / 직전 완료 봉 목표 비중 0%; 다음 봉 시가 가정 |
| v2 | breakout_8 + volume_26 | 9459.80 | -540.20 | sell / filled / 직전 완료 봉 목표 비중 0%; 다음 봉 시가 가정 |
| v2 | reversion_12 AND volume_26 | 9622.80 | -377.20 | sell / filled / 직전 완료 봉 목표 비중 0%; 다음 봉 시가 가정 |
| v2 | reversion_12 + volume_26 | 9309.61 | -690.39 | sell / filled / 직전 완료 봉 목표 비중 0%; 다음 봉 시가 가정 |
| v2 | ema_12_26 | 9583.12 | -416.88 | sell / filled / EMA12 > EMA26; 조건 미충족; EMA12=532.137, EMA26=532.175; 직전 완료 봉 목표를 다음 봉 시가에 모의 적용 |
| v2 | macd_12_26_9 | 9756.46 | -243.54 | sell / filled / MACD > 신호선 그리고 MACD > 0; 조건 미충족; MACD=-0.0387557, signal9=-0.0148606; 직전 완료 봉 목표를 다음 봉 시가에 모의 적용 |
| v2 | rsi_14_recovery | 9951.17 | -48.83 | sell / filled / 직전 RSI14 < 30, 현재 RSI14 >= 30 (한 봉 목표); 조건 미충족; RSI14=45.5102, previous_RSI14=37.5844; 직전 완료 봉 목표를 다음 봉 시가에 모의 적용 |
| v2 | bollinger_20_reentry | 9805.95 | -194.05 | sell / filled / 직전 종가 < 직전 하단밴드, 현재 하단밴드 <= 종가 <= SMA20 (한 봉 목표); 조건 미충족; close=529.335, lower20=528.85, SMA20=531.508, previous_lower20=529.166; 직전 완료 봉 목표를 다음 봉 시가에 모의 적용 |
| v2 | donchian_20 | 9908.19 | -91.81 | sell / filled / 종가 > 현재 봉을 제외한 직전 20봉 최고가; 조건 미충족; close=534.52, prior_high20=535.44; 직전 완료 봉 목표를 다음 봉 시가에 모의 적용 |
| v2 | atr_14_breakout | 9911.14 | -88.86 | sell / filled / 종가 > 직전 종가 + 직전 ATR14 그리고 종가 > EMA26; 조건 미충족; close=533.975, threshold=536.307, prior_ATR14=2.16203, EMA26=530.521; 직전 완료 봉 목표를 다음 봉 시가에 모의 적용 |
| v2 | session_vwap | 9835.29 | -164.71 | buy / partial / 종가 > 뉴욕 거래일별 누적 전형가격 VWAP; 조건 충족; close=530.964, session_VWAP=530.832, session_volume=8.43578e+06; 직전 완료 봉 목표를 다음 봉 시가에 모의 적용 |
| v2 | obv_20 | 9656.49 | -343.51 | buy / partial / OBV > OBV의 SMA20 그리고 종가 > EMA26; 조건 충족; OBV=9.04505e+07, OBV_SMA20=9.01119e+07, close=531.15, EMA26=531.118; 직전 완료 봉 목표를 다음 봉 시가에 모의 적용 |
| v2 | stochastic_14_3_recovery | 9779.25 | -220.75 | sell / filled / 직전 %K14 < 20에서 %K14가 %D3 상향 돌파 (한 봉 목표); 조건 미충족; K14=60.6262, D3=34.5689, previous_K14=38.87, previous_D3=26.948; 직전 완료 봉 목표를 다음 봉 시가에 모의 적용 |
| v2 | mfi_14_recovery | 9968.59 | -31.41 | sell / filled / 직전 MFI14 < 20, 현재 MFI14 >= 20 (한 봉 목표); 조건 미충족; MFI14=53.413, previous_MFI14=44.3372; 직전 완료 봉 목표를 다음 봉 시가에 모의 적용 |
| v2 | adx_14_trend | 9879.67 | -120.33 | sell / filled / Wilder ADX14 >= 25 그리고 +DI14 > -DI14; 조건 미충족; ADX14=23.6824, plus_DI14=22.3066, minus_DI14=19.9214; 직전 완료 봉 목표를 다음 봉 시가에 모의 적용 |
| v2 | aroon_25_trend | 9808.55 | -191.45 | sell / filled / Aroon25 Up > 70 그리고 Down < 30 (동률이면 최신 극값); 조건 미충족; Aroon_up=68, Aroon_down=20; 직전 완료 봉 목표를 다음 봉 시가에 모의 적용 |
| v2 | cci_20_momentum | 9945.68 | -54.32 | sell / filled / CCI20 > 100 (전형가격·평균절대편차); 조건 미충족; CCI20=69.3811; 직전 완료 봉 목표를 다음 봉 시가에 모의 적용 |
| v2 | williams_14_recovery | 9742.27 | -257.73 | sell / filled / 직전 Williams %R14 < -80, 현재 >= -80 (한 봉 목표); 조건 미충족; Williams_R14=-49.2857, previous_R14=-77.0479; 직전 완료 봉 목표를 다음 봉 시가에 모의 적용 |
| v2 | cmf_20_accumulation | 9676.14 | -323.86 | buy / partial / Chaikin Money Flow20 > 0.1; 조건 충족; CMF20=0.135675, volume20=5.00055e+06; 직전 완료 봉 목표를 다음 봉 시가에 모의 적용 |
| v2 | chaikin_3_10 | 9696.85 | -303.15 | buy / partial / ADL의 EMA3 - EMA10 > 0 그리고 종가 > EMA26; 조건 충족; Chaikin3_10=2.08944e+06, ADL=1.17343e+08, close=531.15, EMA26=531.118; 직전 완료 봉 목표를 다음 봉 시가에 모의 적용 |
| v2 | roc_10_momentum | 9957.44 | -42.56 | sell / filled / 10봉 ROC > 1% 그리고 종가 > EMA26; 조건 미충족; ROC10_percent=0.454191, close=534.125, EMA26=532.186; 직전 완료 봉 목표를 다음 봉 시가에 모의 적용 |
| v2 | trix_15_trend | 9708.54 | -291.46 | sell / filled / 15봉 삼중 EMA의 1봉 변화율 TRIX > 0 그리고 종가 > EMA26; 조건 미충족; TRIX15_percent=0.0172213, close=526.676, EMA26=532.897; 직전 완료 봉 목표를 다음 봉 시가에 모의 적용 |
| v2 | keltner_20_breakout | 9956.78 | -43.22 | sell / filled / 종가 > EMA20 + 2 x Wilder ATR14; 조건 미충족; close=533.975, upper_Keltner=534.357, EMA20=530.111, ATR14=2.12332; 직전 완료 봉 목표를 다음 봉 시가에 모의 적용 |
| v2 | opening_range_30m | 9705.59 | -294.41 | buy / partial / 뉴욕 09:30·09:45 두 완료 봉 최고가를 10:00 이후 종가가 돌파; 조건 충족; close=531.65, opening_high=531.48; 직전 완료 봉 목표를 다음 봉 시가에 모의 적용 |

### 같은 기간의 비용·노출 비교 (사후 연구)

| 전략 | 비용 전 | 비용 후 | 100% 보유 | 같은 평균 노출 보유 | 평균 노출 |
|---|---:|---:|---:|---:|---:|
| cash | 0.00% | 0.00% | 2.45% | 0.00% | 0.00% |
| buy_hold | 2.88% | 2.45% | 2.45% | 2.45% | 100.00% |
| trend_8_26 | -0.71% | -4.40% | 2.45% | 1.36% | 56.05% |
| momentum_26 | -0.42% | -6.50% | 2.45% | 1.36% | 56.32% |
| breakout_8 | 6.34% | -8.20% | 2.45% | 0.48% | 20.00% |
| reversion_12 | -4.69% | -13.83% | 2.45% | 0.62% | 25.79% |
| volume_26 | 0.33% | -8.14% | 2.45% | 0.21% | 8.95% |
| trend_8_26 AND momentum_26 | -1.40% | -6.64% | 2.45% | 1.20% | 49.47% |
| trend_8_26 + momentum_26 | -0.56% | -5.05% | 2.45% | 1.36% | 56.19% |
| trend_8_26 AND breakout_8 | 0.51% | -9.13% | 2.45% | 0.28% | 11.84% |
| trend_8_26 + breakout_8 | 2.77% | -5.52% | 2.45% | 0.92% | 38.03% |
| trend_8_26 AND reversion_12 | -1.80% | -7.80% | 2.45% | 0.18% | 7.37% |
| trend_8_26 + reversion_12 | -2.70% | -8.85% | 2.45% | 0.99% | 40.93% |
| trend_8_26 AND volume_26 | 2.59% | -0.80% | 2.45% | 0.07% | 2.89% |
| trend_8_26 + volume_26 | -0.18% | -5.70% | 2.45% | 0.78% | 32.50% |
| momentum_26 AND breakout_8 | 2.76% | -7.48% | 2.45% | 0.29% | 12.11% |
| momentum_26 + breakout_8 | 2.92% | -6.76% | 2.45% | 0.92% | 38.16% |
| momentum_26 AND reversion_12 | -2.82% | -9.51% | 2.45% | 0.24% | 10.00% |
| momentum_26 + reversion_12 | -2.56% | -10.24% | 2.45% | 0.99% | 41.06% |
| momentum_26 AND volume_26 | 0.81% | -4.14% | 2.45% | 0.09% | 3.95% |
| momentum_26 + volume_26 | -0.03% | -6.93% | 2.45% | 0.79% | 32.64% |
| breakout_8 AND reversion_12 | 0.00% | 0.00% | 2.45% | 0.00% | 0.00% |
| breakout_8 + reversion_12 | 0.70% | -10.31% | 2.45% | 0.55% | 22.90% |
| breakout_8 AND volume_26 | 2.04% | -0.50% | 2.45% | 0.04% | 1.84% |
| breakout_8 + volume_26 | 3.30% | -7.59% | 2.45% | 0.35% | 14.48% |
| reversion_12 AND volume_26 | -2.86% | -6.85% | 2.45% | 0.09% | 3.95% |
| reversion_12 + volume_26 | -2.20% | -10.84% | 2.45% | 0.42% | 17.37% |
| ema_12_26 | -1.35% | -5.01% | 2.45% | 1.39% | 57.37% |
| macd_12_26_9 | -0.41% | -5.30% | 2.45% | 0.78% | 32.37% |
| rsi_14_recovery | 0.31% | -2.19% | 2.45% | 0.04% | 1.58% |
| bollinger_20_reentry | -0.93% | -4.21% | 2.45% | 0.05% | 2.11% |
| donchian_20 | 1.05% | -4.32% | 2.45% | 0.10% | 4.21% |
| atr_14_breakout | 1.36% | -3.62% | 2.45% | 0.08% | 3.42% |
| session_vwap | 5.92% | -2.20% | 2.45% | 1.01% | 41.84% |
| obv_20 | 5.46% | -3.44% | 2.45% | 1.20% | 49.74% |
| stochastic_14_3_recovery | -0.57% | -10.11% | 2.45% | 0.15% | 6.32% |
| mfi_14_recovery | 1.58% | -2.19% | 2.45% | 0.06% | 2.37% |
| adx_14_trend | 4.03% | 1.87% | 2.45% | 1.05% | 43.68% |
| aroon_25_trend | -0.49% | -4.59% | 2.45% | 0.51% | 21.32% |
| cci_20_momentum | 2.56% | -3.70% | 2.45% | 0.49% | 20.26% |
| williams_14_recovery | -1.61% | -10.30% | 2.45% | 0.14% | 5.79% |
| cmf_20_accumulation | 0.70% | -5.45% | 2.45% | 0.91% | 37.63% |
| chaikin_3_10 | 4.40% | -3.61% | 2.45% | 1.14% | 47.11% |
| roc_10_momentum | -0.61% | -4.30% | 2.45% | 0.32% | 13.16% |
| trix_15_trend | -1.03% | -5.10% | 2.45% | 1.07% | 44.47% |
| keltner_20_breakout | 0.49% | -4.45% | 2.45% | 0.28% | 11.58% |
| opening_range_30m | -0.92% | -4.59% | 2.45% | 0.43% | 17.89% |

동일 구간·초기 자금, 종료 시 청산 비용 포함. 노출 맞춤은 사후 설명용이며 v2 실제 계좌 성과가 아닙니다.
[낙폭 분해·비용 영향·전체 구간](MSFT/comparison.json)

[v1 전체 기록](MSFT/accounts.json) · [v2 전체 기록](MSFT/accounts-v2.json)

## JPM 계좌

| 모델 | 전략 | 평가액 USD | 손익 USD | 최근 매매·이유 |
|---|---|---:|---:|---|
| v1 | cash | 10000.00 | 0.00 | 대기 /  / 새 신호 대기 |
| v1 | buy_hold | 9812.09 | -187.91 | buy /  / buy_hold: prior completed bar target 100%; next bar open simulation |
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
| v1 | session_vwap | 9709.59 | -290.41 | buy /  / 종가 > 뉴욕 거래일별 누적 전형가격 VWAP; 조건 충족; close=334.131, session_VWAP=334.059, session_volume=1.73099e+06 |
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
| v2 | buy_hold | 9976.05 | -23.95 | buy / partial / 직전 완료 봉 목표 비중 100%; 다음 봉 시가 가정 |
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
| v2 | session_vwap | 9698.92 | -301.08 | buy / partial / 종가 > 뉴욕 거래일별 누적 전형가격 VWAP; 조건 충족; close=334.131, session_VWAP=334.059, session_volume=1.73099e+06; 직전 완료 봉 목표를 다음 봉 시가에 모의 적용 |
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
| cash | 0.00% | 0.00% | 0.13% | 0.00% | 0.00% |
| buy_hold | 0.55% | 0.13% | 0.13% | 0.13% | 100.00% |
| trend_8_26 | 0.52% | -3.21% | 0.13% | 0.07% | 52.63% |
| momentum_26 | -3.27% | -10.69% | 0.13% | 0.07% | 52.11% |
| breakout_8 | -2.73% | -17.43% | 0.13% | 0.03% | 19.74% |
| reversion_12 | 5.62% | -9.20% | 0.13% | 0.03% | 24.47% |
| volume_26 | -0.40% | -6.87% | 0.13% | 0.01% | 7.11% |
| trend_8_26 AND momentum_26 | 0.56% | -4.38% | 0.13% | 0.05% | 41.32% |
| trend_8_26 + momentum_26 | -1.38% | -6.82% | 0.13% | 0.07% | 52.37% |
| trend_8_26 AND breakout_8 | -3.21% | -13.22% | 0.13% | 0.02% | 12.11% |
| trend_8_26 + breakout_8 | -1.10% | -10.21% | 0.13% | 0.05% | 36.19% |
| trend_8_26 AND reversion_12 | 2.81% | -3.46% | 0.13% | 0.01% | 7.11% |
| trend_8_26 + reversion_12 | 3.06% | -5.66% | 0.13% | 0.05% | 38.56% |
| trend_8_26 AND volume_26 | -0.37% | -3.66% | 0.13% | 0.00% | 3.68% |
| trend_8_26 + volume_26 | 0.08% | -5.05% | 0.13% | 0.04% | 29.87% |
| momentum_26 AND breakout_8 | -2.68% | -13.84% | 0.13% | 0.02% | 12.63% |
| momentum_26 + breakout_8 | -2.97% | -13.92% | 0.13% | 0.05% | 35.93% |
| momentum_26 AND reversion_12 | 2.87% | -4.62% | 0.13% | 0.01% | 7.11% |
| momentum_26 + reversion_12 | 1.11% | -8.03% | 0.13% | 0.05% | 38.30% |
| momentum_26 AND volume_26 | -0.48% | -3.77% | 0.13% | 0.00% | 3.16% |
| momentum_26 + volume_26 | -1.82% | -8.41% | 0.13% | 0.04% | 29.61% |
| breakout_8 AND reversion_12 | 0.00% | 0.00% | 0.13% | 0.00% | 0.00% |
| breakout_8 + reversion_12 | 1.38% | -12.13% | 0.13% | 0.03% | 22.11% |
| breakout_8 AND volume_26 | -0.25% | -2.32% | 0.13% | 0.00% | 1.32% |
| breakout_8 + volume_26 | -1.56% | -11.57% | 0.13% | 0.02% | 13.43% |
| reversion_12 AND volume_26 | 1.38% | -1.56% | 0.13% | 0.00% | 3.16% |
| reversion_12 + volume_26 | 2.58% | -6.88% | 0.13% | 0.02% | 15.80% |
| ema_12_26 | -0.24% | -3.54% | 0.13% | 0.07% | 52.11% |
| macd_12_26_9 | -0.13% | -4.64% | 0.13% | 0.04% | 32.89% |
| rsi_14_recovery | 0.59% | -1.08% | 0.13% | 0.00% | 1.05% |
| bollinger_20_reentry | 0.25% | -3.87% | 0.13% | 0.00% | 2.63% |
| donchian_20 | -1.81% | -5.05% | 0.13% | 0.00% | 3.16% |
| atr_14_breakout | -1.35% | -8.92% | 0.13% | 0.01% | 5.26% |
| session_vwap | 1.69% | -8.06% | 0.13% | 0.06% | 47.11% |
| obv_20 | -3.42% | -13.78% | 0.13% | 0.04% | 30.00% |
| stochastic_14_3_recovery | -0.96% | -11.58% | 0.13% | 0.01% | 7.11% |
| mfi_14_recovery | 0.25% | -1.42% | 0.13% | 0.00% | 1.05% |
| adx_14_trend | -2.43% | -4.85% | 0.13% | 0.04% | 29.74% |
| aroon_25_trend | -0.75% | -4.43% | 0.13% | 0.03% | 21.84% |
| cci_20_momentum | -2.84% | -10.67% | 0.13% | 0.02% | 16.32% |
| williams_14_recovery | -1.30% | -11.88% | 0.13% | 0.01% | 7.11% |
| cmf_20_accumulation | -1.98% | -10.63% | 0.13% | 0.04% | 30.26% |
| chaikin_3_10 | 1.01% | -7.52% | 0.13% | 0.04% | 33.95% |
| roc_10_momentum | -1.36% | -4.22% | 0.13% | 0.01% | 8.42% |
| trix_15_trend | -1.25% | -8.83% | 0.13% | 0.05% | 35.26% |
| keltner_20_breakout | -1.21% | -4.07% | 0.13% | 0.01% | 4.21% |
| opening_range_30m | -0.23% | -3.93% | 0.13% | 0.02% | 17.37% |

동일 구간·초기 자금, 종료 시 청산 비용 포함. 노출 맞춤은 사후 설명용이며 v2 실제 계좌 성과가 아닙니다.
[낙폭 분해·비용 영향·전체 구간](JPM/comparison.json)

[v1 전체 기록](JPM/accounts.json) · [v2 전체 기록](JPM/accounts-v2.json)

## XOM 계좌

| 모델 | 전략 | 평가액 USD | 손익 USD | 최근 매매·이유 |
|---|---|---:|---:|---|
| v1 | cash | 10000.00 | 0.00 | 대기 /  / 새 신호 대기 |
| v1 | buy_hold | 10009.44 | 9.44 | buy /  / buy_hold: prior completed bar target 100%; next bar open simulation |
| v1 | trend_8_26 | 9823.67 | -176.33 | buy /  / trend_8_26: prior completed bar target 100%; next bar open simulation |
| v1 | momentum_26 | 9868.46 | -131.54 | buy /  / momentum_26: prior completed bar target 100%; next bar open simulation |
| v1 | breakout_8 | 9566.22 | -433.78 | sell /  / breakout_8: prior completed bar target 0%; next bar open simulation |
| v1 | reversion_12 | 9683.62 | -316.38 | sell /  / reversion_12: prior completed bar target 0%; next bar open simulation |
| v1 | volume_26 | 9648.38 | -351.62 | sell /  / volume_26: prior completed bar target 0%; next bar open simulation |
| v1 | trend_8_26 AND momentum_26 | 9787.92 | -212.08 | buy /  / trend_8_26 AND momentum_26: prior completed bar target 100%; next bar open simulation |
| v1 | trend_8_26 + momentum_26 | 9846.14 | -153.86 | buy /  / trend_8_26 + momentum_26: prior completed bar target 100%; next bar open simulation |
| v1 | trend_8_26 AND breakout_8 | 9704.96 | -295.04 | sell /  / trend_8_26 AND breakout_8: prior completed bar target 0%; next bar open simulation |
| v1 | trend_8_26 + breakout_8 | 9713.90 | -286.10 | sell /  / trend_8_26 + breakout_8: prior completed bar target 50%; next bar open simulation |
| v1 | trend_8_26 AND reversion_12 | 9677.97 | -322.03 | sell /  / trend_8_26 AND reversion_12: prior completed bar target 0%; next bar open simulation |
| v1 | trend_8_26 + reversion_12 | 9753.33 | -246.67 | sell /  / trend_8_26 + reversion_12: prior completed bar target 50%; next bar open simulation |
| v1 | trend_8_26 AND volume_26 | 9764.30 | -235.70 | sell /  / trend_8_26 AND volume_26: prior completed bar target 0%; next bar open simulation |
| v1 | trend_8_26 + volume_26 | 9735.83 | -264.17 | sell /  / trend_8_26 + volume_26: prior completed bar target 50%; next bar open simulation |
| v1 | momentum_26 AND breakout_8 | 9801.24 | -198.76 | sell /  / momentum_26 AND breakout_8: prior completed bar target 0%; next bar open simulation |
| v1 | momentum_26 + breakout_8 | 9716.40 | -283.60 | sell /  / momentum_26 + breakout_8: prior completed bar target 50%; next bar open simulation |
| v1 | momentum_26 AND reversion_12 | 9766.58 | -233.42 | sell /  / momentum_26 AND reversion_12: prior completed bar target 0%; next bar open simulation |
| v1 | momentum_26 + reversion_12 | 9775.46 | -224.54 | sell /  / momentum_26 + reversion_12: prior completed bar target 50%; next bar open simulation |
| v1 | momentum_26 AND volume_26 | 9985.49 | -14.51 | sell /  / momentum_26 AND volume_26: prior completed bar target 0%; next bar open simulation |
| v1 | momentum_26 + volume_26 | 9757.79 | -242.21 | sell /  / momentum_26 + volume_26: prior completed bar target 50%; next bar open simulation |
| v1 | breakout_8 AND reversion_12 | 10000.00 | 0.00 | 대기 /  / 새 신호 대기 |
| v1 | breakout_8 + reversion_12 | 9643.94 | -356.06 | sell /  / breakout_8 + reversion_12: prior completed bar target 0%; next bar open simulation |
| v1 | breakout_8 AND volume_26 | 9851.05 | -148.95 | sell /  / breakout_8 AND volume_26: prior completed bar target 0%; next bar open simulation |
| v1 | breakout_8 + volume_26 | 9607.03 | -392.97 | sell /  / breakout_8 + volume_26: prior completed bar target 0%; next bar open simulation |
| v1 | reversion_12 AND volume_26 | 9815.22 | -184.78 | sell /  / reversion_12 AND volume_26: prior completed bar target 0%; next bar open simulation |
| v1 | reversion_12 + volume_26 | 9666.08 | -333.92 | sell /  / reversion_12 + volume_26: prior completed bar target 0%; next bar open simulation |
| v1 | ema_12_26 | 9828.06 | -171.94 | buy /  / EMA12 > EMA26; 조건 충족; EMA12=177.271, EMA26=177.221 |
| v1 | macd_12_26_9 | 9916.99 | -83.01 | buy /  / MACD > 신호선 그리고 MACD > 0; 조건 충족; MACD=0.0503325, signal9=-0.0213957 |
| v1 | rsi_14_recovery | 9927.64 | -72.36 | sell /  / 직전 RSI14 < 30, 현재 RSI14 >= 30 (한 봉 목표); 조건 미충족; RSI14=37.639, previous_RSI14=31.1023 |
| v1 | bollinger_20_reentry | 9852.90 | -147.10 | sell /  / 직전 종가 < 직전 하단밴드, 현재 하단밴드 <= 종가 <= SMA20 (한 봉 목표); 조건 미충족; close=175.55, lower20=175.189, SMA20=177.794, previous_lower20=175.528 |
| v1 | donchian_20 | 9739.57 | -260.43 | sell /  / 종가 > 현재 봉을 제외한 직전 20봉 최고가; 조건 미충족; close=176.61, prior_high20=177.952 |
| v1 | atr_14_breakout | 9826.13 | -173.87 | sell /  / 종가 > 직전 종가 + 직전 ATR14 그리고 종가 > EMA26; 조건 미충족; close=177.865, threshold=178.483, prior_ATR14=0.612834, EMA26=177.268 |
| v1 | session_vwap | 9792.89 | -207.11 | buy /  / 종가 > 뉴욕 거래일별 누적 전형가격 VWAP; 조건 충족; close=177.7, session_VWAP=177.368, session_volume=2.94256e+06 |
| v1 | obv_20 | 9542.98 | -457.02 | buy /  / OBV > OBV의 SMA20 그리고 종가 > EMA26; 조건 충족; OBV=2.31927e+07, OBV_SMA20=2.30886e+07, close=177.705, EMA26=177.399 |
| v1 | stochastic_14_3_recovery | 9721.31 | -278.69 | sell /  / 직전 %K14 < 20에서 %K14가 %D3 상향 돌파 (한 봉 목표); 조건 미충족; K14=29.2797, D3=21.8586, previous_K14=22.3575, previous_D3=16.0588 |
| v1 | mfi_14_recovery | 10000.00 | 0.00 | 대기 /  / 새 신호 대기 |
| v1 | adx_14_trend | 9999.47 | -0.53 | sell /  / Wilder ADX14 >= 25 그리고 +DI14 > -DI14; 조건 미충족; ADX14=23.8302, plus_DI14=25.6436, minus_DI14=22.6035 |
| v1 | aroon_25_trend | 9709.81 | -290.19 | sell /  / Aroon25 Up > 70 그리고 Down < 30 (동률이면 최신 극값); 조건 미충족; Aroon_up=72, Aroon_down=64 |
| v1 | cci_20_momentum | 9599.29 | -400.71 | sell /  / CCI20 > 100 (전형가격·평균절대편차); 조건 미충족; CCI20=74.6634 |
| v1 | williams_14_recovery | 9665.88 | -334.12 | sell /  / 직전 Williams %R14 < -80, 현재 >= -80 (한 봉 목표); 조건 미충족; Williams_R14=-12.0205, previous_R14=-62.6593 |
| v1 | cmf_20_accumulation | 9911.95 | -88.05 | buy /  / Chaikin Money Flow20 > 0.1; 조건 충족; CMF20=0.210618, volume20=5.30029e+06 |
| v1 | chaikin_3_10 | 9703.22 | -296.78 | buy /  / ADL의 EMA3 - EMA10 > 0 그리고 종가 > EMA26; 조건 충족; Chaikin3_10=46780.1, ADL=2.83087e+07, close=177.7, EMA26=177.374 |
| v1 | roc_10_momentum | 9940.60 | -59.40 | sell /  / 10봉 ROC > 1% 그리고 종가 > EMA26; 조건 미충족; ROC10_percent=0.782107, close=178.47, EMA26=176.891 |
| v1 | trix_15_trend | 9835.05 | -164.95 | buy /  / 15봉 삼중 EMA의 1봉 변화율 TRIX > 0 그리고 종가 > EMA26; 조건 충족; TRIX15_percent=0.00640926, close=177.7, EMA26=177.374 |
| v1 | keltner_20_breakout | 9937.30 | -62.70 | sell /  / 종가 > EMA20 + 2 x Wilder ATR14; 조건 미충족; close=178.845, upper_Keltner=179.079, EMA20=177.884, ATR14=0.597175 |
| v1 | opening_range_30m | 10049.37 | 49.37 | sell /  / 뉴욕 09:30·09:45 두 완료 봉 최고가를 10:00 이후 종가가 돌파; 자료 부족·변동폭 또는 거래량 없음: 대기; close=179.01 |
| v2 | cash | 10000.00 | 0.00 | 대기 /  / 새 신호 대기 |
| v2 | buy_hold | 10328.86 | 328.86 | buy / partial / 직전 완료 봉 목표 비중 100%; 다음 봉 시가 가정 |
| v2 | trend_8_26 | 9913.27 | -86.73 | buy / partial / 직전 완료 봉 목표 비중 100%; 다음 봉 시가 가정 |
| v2 | momentum_26 | 10033.82 | 33.82 | buy / partial / 직전 완료 봉 목표 비중 100%; 다음 봉 시가 가정 |
| v2 | breakout_8 | 9038.47 | -961.53 | sell / filled / 직전 완료 봉 목표 비중 0%; 다음 봉 시가 가정 |
| v2 | reversion_12 | 9498.83 | -501.17 | sell / filled / 직전 완료 봉 목표 비중 0%; 다음 봉 시가 가정 |
| v2 | volume_26 | 9550.10 | -449.90 | sell / filled / 직전 완료 봉 목표 비중 0%; 다음 봉 시가 가정 |
| v2 | trend_8_26 AND momentum_26 | 9882.54 | -117.46 | buy / partial / 직전 완료 봉 목표 비중 100%; 다음 봉 시가 가정 |
| v2 | trend_8_26 + momentum_26 | 9973.48 | -26.52 | buy / partial / 직전 완료 봉 목표 비중 100%; 다음 봉 시가 가정 |
| v2 | trend_8_26 AND breakout_8 | 9160.13 | -839.87 | sell / filled / 직전 완료 봉 목표 비중 0%; 다음 봉 시가 가정 |
| v2 | trend_8_26 + breakout_8 | 9506.35 | -493.65 | sell / filled / 직전 완료 봉 목표 비중 50%; 다음 봉 시가 가정 |
| v2 | trend_8_26 AND reversion_12 | 9517.12 | -482.88 | sell / filled / 직전 완료 봉 목표 비중 0%; 다음 봉 시가 가정 |
| v2 | trend_8_26 + reversion_12 | 9703.85 | -296.15 | sell / filled / 직전 완료 봉 목표 비중 50%; 다음 봉 시가 가정 |
| v2 | trend_8_26 AND volume_26 | 9656.58 | -343.42 | sell / filled / 직전 완료 봉 목표 비중 0%; 다음 봉 시가 가정 |
| v2 | trend_8_26 + volume_26 | 9730.13 | -269.87 | sell / filled / 직전 완료 봉 목표 비중 50%; 다음 봉 시가 가정 |
| v2 | momentum_26 AND breakout_8 | 9269.79 | -730.21 | sell / filled / 직전 완료 봉 목표 비중 0%; 다음 봉 시가 가정 |
| v2 | momentum_26 + breakout_8 | 9523.89 | -476.11 | sell / filled / 직전 완료 봉 목표 비중 50%; 다음 봉 시가 가정 |
| v2 | momentum_26 AND reversion_12 | 9567.55 | -432.45 | sell / filled / 직전 완료 봉 목표 비중 0%; 다음 봉 시가 가정 |
| v2 | momentum_26 + reversion_12 | 9762.61 | -237.39 | sell / filled / 직전 완료 봉 목표 비중 50%; 다음 봉 시가 가정 |
| v2 | momentum_26 AND volume_26 | 9941.52 | -58.48 | sell / filled / 직전 완료 봉 목표 비중 0%; 다음 봉 시가 가정 |
| v2 | momentum_26 + volume_26 | 9809.45 | -190.55 | sell / filled / 직전 완료 봉 목표 비중 50%; 다음 봉 시가 가정 |
| v2 | breakout_8 AND reversion_12 | 10000.00 | 0.00 | 대기 /  / 새 신호 대기 |
| v2 | breakout_8 + reversion_12 | 9285.08 | -714.92 | sell / filled / 직전 완료 봉 목표 비중 0%; 다음 봉 시가 가정 |
| v2 | breakout_8 AND volume_26 | 9817.82 | -182.18 | sell / filled / 직전 완료 봉 목표 비중 0%; 다음 봉 시가 가정 |
| v2 | breakout_8 + volume_26 | 9310.00 | -690.00 | sell / filled / 직전 완료 봉 목표 비중 0%; 다음 봉 시가 가정 |
| v2 | reversion_12 AND volume_26 | 9760.17 | -239.83 | sell / filled / 직전 완료 봉 목표 비중 0%; 다음 봉 시가 가정 |
| v2 | reversion_12 + volume_26 | 9544.56 | -455.44 | sell / filled / 직전 완료 봉 목표 비중 0%; 다음 봉 시가 가정 |
| v2 | ema_12_26 | 9823.15 | -176.85 | buy / partial / EMA12 > EMA26; 조건 충족; EMA12=177.271, EMA26=177.221; 직전 완료 봉 목표를 다음 봉 시가에 모의 적용 |
| v2 | macd_12_26_9 | 9910.05 | -89.95 | buy / partial / MACD > 신호선 그리고 MACD > 0; 조건 충족; MACD=0.0503325, signal9=-0.0213957; 직전 완료 봉 목표를 다음 봉 시가에 모의 적용 |
| v2 | rsi_14_recovery | 9923.67 | -76.33 | sell / filled / 직전 RSI14 < 30, 현재 RSI14 >= 30 (한 봉 목표); 조건 미충족; RSI14=37.639, previous_RSI14=31.1023; 직전 완료 봉 목표를 다음 봉 시가에 모의 적용 |
| v2 | bollinger_20_reentry | 9848.96 | -151.04 | sell / filled / 직전 종가 < 직전 하단밴드, 현재 하단밴드 <= 종가 <= SMA20 (한 봉 목표); 조건 미충족; close=175.55, lower20=175.189, SMA20=177.794, previous_lower20=175.528; 직전 완료 봉 목표를 다음 봉 시가에 모의 적용 |
| v2 | donchian_20 | 9729.83 | -270.17 | sell / filled / 종가 > 현재 봉을 제외한 직전 20봉 최고가; 조건 미충족; close=176.61, prior_high20=177.952; 직전 완료 봉 목표를 다음 봉 시가에 모의 적용 |
| v2 | atr_14_breakout | 9818.27 | -181.73 | sell / filled / 종가 > 직전 종가 + 직전 ATR14 그리고 종가 > EMA26; 조건 미충족; close=177.865, threshold=178.483, prior_ATR14=0.612834, EMA26=177.268; 직전 완료 봉 목표를 다음 봉 시가에 모의 적용 |
| v2 | session_vwap | 9782.12 | -217.88 | buy / partial / 종가 > 뉴욕 거래일별 누적 전형가격 VWAP; 조건 충족; close=177.7, session_VWAP=177.368, session_volume=2.94256e+06; 직전 완료 봉 목표를 다음 봉 시가에 모의 적용 |
| v2 | obv_20 | 9524.86 | -475.14 | buy / partial / OBV > OBV의 SMA20 그리고 종가 > EMA26; 조건 충족; OBV=2.31927e+07, OBV_SMA20=2.30886e+07, close=177.705, EMA26=177.399; 직전 완료 봉 목표를 다음 봉 시가에 모의 적용 |
| v2 | stochastic_14_3_recovery | 9711.59 | -288.41 | sell / filled / 직전 %K14 < 20에서 %K14가 %D3 상향 돌파 (한 봉 목표); 조건 미충족; K14=29.2797, D3=21.8586, previous_K14=22.3575, previous_D3=16.0588; 직전 완료 봉 목표를 다음 봉 시가에 모의 적용 |
| v2 | mfi_14_recovery | 10000.00 | 0.00 | 대기 /  / 새 신호 대기 |
| v2 | adx_14_trend | 9993.47 | -6.53 | sell / filled / Wilder ADX14 >= 25 그리고 +DI14 > -DI14; 조건 미충족; ADX14=23.8302, plus_DI14=25.6436, minus_DI14=22.6035; 직전 완료 봉 목표를 다음 봉 시가에 모의 적용 |
| v2 | aroon_25_trend | 9703.99 | -296.01 | sell / filled / Aroon25 Up > 70 그리고 Down < 30 (동률이면 최신 극값); 조건 미충족; Aroon_up=72, Aroon_down=64; 직전 완료 봉 목표를 다음 봉 시가에 모의 적용 |
| v2 | cci_20_momentum | 9582.02 | -417.98 | sell / filled / CCI20 > 100 (전형가격·평균절대편차); 조건 미충족; CCI20=74.6634; 직전 완료 봉 목표를 다음 봉 시가에 모의 적용 |
| v2 | williams_14_recovery | 9654.28 | -345.72 | sell / filled / 직전 Williams %R14 < -80, 현재 >= -80 (한 봉 목표); 조건 미충족; Williams_R14=-12.0205, previous_R14=-62.6593; 직전 완료 봉 목표를 다음 봉 시가에 모의 적용 |
| v2 | cmf_20_accumulation | 9907.00 | -93.00 | buy / partial / Chaikin Money Flow20 > 0.1; 조건 충족; CMF20=0.210618, volume20=5.30029e+06; 직전 완료 봉 목표를 다음 봉 시가에 모의 적용 |
| v2 | chaikin_3_10 | 9690.61 | -309.39 | buy / partial / ADL의 EMA3 - EMA10 > 0 그리고 종가 > EMA26; 조건 충족; Chaikin3_10=46780.1, ADL=2.83087e+07, close=177.7, EMA26=177.374; 직전 완료 봉 목표를 다음 봉 시가에 모의 적용 |
| v2 | roc_10_momentum | 9934.64 | -65.36 | sell / filled / 10봉 ROC > 1% 그리고 종가 > EMA26; 조건 미충족; ROC10_percent=0.782107, close=178.47, EMA26=176.891; 직전 완료 봉 목표를 다음 봉 시가에 모의 적용 |
| v2 | trix_15_trend | 9826.21 | -173.79 | buy / partial / 15봉 삼중 EMA의 1봉 변화율 TRIX > 0 그리고 종가 > EMA26; 조건 충족; TRIX15_percent=0.00640926, close=177.7, EMA26=177.374; 직전 완료 봉 목표를 다음 봉 시가에 모의 적용 |
| v2 | keltner_20_breakout | 9931.34 | -68.66 | sell / filled / 종가 > EMA20 + 2 x Wilder ATR14; 조건 미충족; close=178.845, upper_Keltner=179.079, EMA20=177.884, ATR14=0.597175; 직전 완료 봉 목표를 다음 봉 시가에 모의 적용 |
| v2 | opening_range_30m | 10047.36 | 47.36 | sell / filled / 뉴욕 09:30·09:45 두 완료 봉 최고가를 10:00 이후 종가가 돌파; 자료 부족·변동폭 또는 거래량 없음: 대기; close=179.01; 직전 완료 봉 목표를 다음 봉 시가에 모의 적용 |

### 같은 기간의 비용·노출 비교 (사후 연구)

| 전략 | 비용 전 | 비용 후 | 100% 보유 | 같은 평균 노출 보유 | 평균 노출 |
|---|---:|---:|---:|---:|---:|
| cash | 0.00% | 0.00% | 7.74% | 0.00% | 0.00% |
| buy_hold | 8.19% | 7.74% | 7.74% | 7.74% | 100.00% |
| trend_8_26 | 0.50% | -4.44% | 7.74% | 5.23% | 68.42% |
| momentum_26 | 1.04% | -6.32% | 7.74% | 5.42% | 70.79% |
| breakout_8 | -1.21% | -19.24% | 7.74% | 2.00% | 26.58% |
| reversion_12 | 3.33% | -6.58% | 7.74% | 1.60% | 21.32% |
| volume_26 | 1.74% | -6.06% | 7.74% | 0.43% | 5.79% |
| trend_8_26 AND momentum_26 | -0.91% | -6.57% | 7.74% | 4.55% | 59.74% |
| trend_8_26 + momentum_26 | 0.78% | -5.18% | 7.74% | 5.32% | 69.61% |
| trend_8_26 AND breakout_8 | -1.05% | -15.64% | 7.74% | 1.52% | 20.26% |
| trend_8_26 + breakout_8 | -0.33% | -11.77% | 7.74% | 3.60% | 47.51% |
| trend_8_26 AND reversion_12 | -1.34% | -7.37% | 7.74% | 0.77% | 10.26% |
| trend_8_26 + reversion_12 | 1.94% | -5.31% | 7.74% | 3.40% | 44.87% |
| trend_8_26 AND volume_26 | 0.91% | -4.05% | 7.74% | 0.27% | 3.68% |
| trend_8_26 + volume_26 | 1.14% | -5.05% | 7.74% | 2.80% | 37.11% |
| momentum_26 AND breakout_8 | -1.02% | -17.03% | 7.74% | 1.72% | 22.89% |
| momentum_26 + breakout_8 | -0.07% | -13.00% | 7.74% | 3.69% | 48.69% |
| momentum_26 AND reversion_12 | -0.47% | -6.94% | 7.74% | 0.75% | 10.00% |
| momentum_26 + reversion_12 | 2.21% | -5.26% | 7.74% | 3.49% | 46.06% |
| momentum_26 AND volume_26 | 2.15% | -1.64% | 7.74% | 0.18% | 2.37% |
| momentum_26 + volume_26 | 1.41% | -5.20% | 7.74% | 2.89% | 38.29% |
| breakout_8 AND reversion_12 | 0.00% | 0.00% | 7.74% | 0.00% | 0.00% |
| breakout_8 + reversion_12 | 1.06% | -12.78% | 7.74% | 1.80% | 23.96% |
| breakout_8 AND volume_26 | -0.10% | -2.18% | 7.74% | 0.10% | 1.32% |
| breakout_8 + volume_26 | 0.27% | -12.17% | 7.74% | 1.21% | 16.19% |
| reversion_12 AND volume_26 | 0.43% | -2.89% | 7.74% | 0.18% | 2.37% |
| reversion_12 + volume_26 | 2.55% | -5.53% | 7.74% | 1.01% | 13.56% |
| ema_12_26 | -0.07% | -3.78% | 7.74% | 5.93% | 77.37% |
| macd_12_26_9 | -1.07% | -7.11% | 7.74% | 3.20% | 42.37% |
| rsi_14_recovery | -0.08% | -1.33% | 7.74% | 0.06% | 0.79% |
| bollinger_20_reentry | -1.07% | -3.94% | 7.74% | 0.14% | 1.84% |
| donchian_20 | -1.73% | -10.03% | 7.74% | 0.67% | 8.95% |
| atr_14_breakout | 0.55% | -7.55% | 7.74% | 0.41% | 5.53% |
| session_vwap | 0.23% | -10.52% | 7.74% | 5.04% | 66.05% |
| obv_20 | 0.74% | -9.68% | 7.74% | 3.67% | 48.42% |
| stochastic_14_3_recovery | 0.79% | -8.49% | 7.74% | 0.45% | 6.05% |
| mfi_14_recovery | -0.31% | -1.97% | 7.74% | 0.08% | 1.05% |
| adx_14_trend | 3.33% | 0.76% | 7.74% | 2.92% | 38.68% |
| aroon_25_trend | -3.43% | -10.08% | 7.74% | 2.52% | 33.42% |
| cci_20_momentum | 2.18% | -6.84% | 7.74% | 2.06% | 27.37% |
| williams_14_recovery | -0.38% | -6.85% | 7.74% | 0.31% | 4.21% |
| cmf_20_accumulation | 0.88% | -5.28% | 7.74% | 3.85% | 50.79% |
| chaikin_3_10 | 0.52% | -8.74% | 7.74% | 4.55% | 59.74% |
| roc_10_momentum | 0.44% | -4.90% | 7.74% | 0.86% | 11.58% |
| trix_15_trend | -0.06% | -6.95% | 7.74% | 4.90% | 64.21% |
| keltner_20_breakout | 0.54% | -5.20% | 7.74% | 1.18% | 15.79% |
| opening_range_30m | -0.29% | -9.09% | 7.74% | 2.28% | 30.26% |

동일 구간·초기 자금, 종료 시 청산 비용 포함. 노출 맞춤은 사후 설명용이며 v2 실제 계좌 성과가 아닙니다.
[낙폭 분해·비용 영향·전체 구간](XOM/comparison.json)

[v1 전체 기록](XOM/accounts.json) · [v2 전체 기록](XOM/accounts-v2.json)

## JNJ 계좌

| 모델 | 전략 | 평가액 USD | 손익 USD | 최근 매매·이유 |
|---|---|---:|---:|---|
| v1 | cash | 10000.00 | 0.00 | 대기 /  / 새 신호 대기 |
| v1 | buy_hold | 9987.84 | -12.16 | buy /  / buy_hold: prior completed bar target 100%; next bar open simulation |
| v1 | trend_8_26 | 9989.00 | -11.00 | sell /  / trend_8_26: prior completed bar target 0%; next bar open simulation |
| v1 | momentum_26 | 9722.10 | -277.90 | sell /  / momentum_26: prior completed bar target 0%; next bar open simulation |
| v1 | breakout_8 | 9435.72 | -564.28 | buy /  / breakout_8: prior completed bar target 100%; next bar open simulation |
| v1 | reversion_12 | 9747.78 | -252.22 | sell /  / reversion_12: prior completed bar target 0%; next bar open simulation |
| v1 | volume_26 | 9902.45 | -97.55 | sell /  / volume_26: prior completed bar target 0%; next bar open simulation |
| v1 | trend_8_26 AND momentum_26 | 9813.05 | -186.95 | sell /  / trend_8_26 AND momentum_26: prior completed bar target 0%; next bar open simulation |
| v1 | trend_8_26 + momentum_26 | 9854.96 | -145.04 | sell /  / trend_8_26 + momentum_26: prior completed bar target 0%; next bar open simulation |
| v1 | trend_8_26 AND breakout_8 | 9765.55 | -234.45 | sell /  / trend_8_26 AND breakout_8: prior completed bar target 0%; next bar open simulation |
| v1 | trend_8_26 + breakout_8 | 9728.14 | -271.86 | sell /  / trend_8_26 + breakout_8: prior completed bar target 50%; next bar open simulation |
| v1 | trend_8_26 AND reversion_12 | 9930.57 | -69.43 | sell /  / trend_8_26 AND reversion_12: prior completed bar target 0%; next bar open simulation |
| v1 | trend_8_26 + reversion_12 | 9867.78 | -132.22 | sell /  / trend_8_26 + reversion_12: prior completed bar target 0%; next bar open simulation |
| v1 | trend_8_26 AND volume_26 | 9995.12 | -4.88 | sell /  / trend_8_26 AND volume_26: prior completed bar target 0%; next bar open simulation |
| v1 | trend_8_26 + volume_26 | 9945.88 | -54.12 | sell /  / trend_8_26 + volume_26: prior completed bar target 0%; next bar open simulation |
| v1 | momentum_26 AND breakout_8 | 9784.22 | -215.78 | sell /  / momentum_26 AND breakout_8: prior completed bar target 0%; next bar open simulation |
| v1 | momentum_26 + breakout_8 | 9577.72 | -422.28 | sell /  / momentum_26 + breakout_8: prior completed bar target 50%; next bar open simulation |
| v1 | momentum_26 AND reversion_12 | 9938.52 | -61.48 | sell /  / momentum_26 AND reversion_12: prior completed bar target 0%; next bar open simulation |
| v1 | momentum_26 + reversion_12 | 9773.79 | -226.21 | sell /  / momentum_26 + reversion_12: prior completed bar target 0%; next bar open simulation |
| v1 | momentum_26 AND volume_26 | 10000.00 | 0.00 | 대기 /  / 새 신호 대기 |
| v1 | momentum_26 + volume_26 | 9851.20 | -148.80 | sell /  / momentum_26 + volume_26: prior completed bar target 0%; next bar open simulation |
| v1 | breakout_8 AND reversion_12 | 10000.00 | 0.00 | 대기 /  / 새 신호 대기 |
| v1 | breakout_8 + reversion_12 | 9590.20 | -409.80 | sell /  / breakout_8 + reversion_12: prior completed bar target 50%; next bar open simulation |
| v1 | breakout_8 AND volume_26 | 10000.00 | 0.00 | 대기 /  / 새 신호 대기 |
| v1 | breakout_8 + volume_26 | 9685.55 | -314.45 | sell /  / breakout_8 + volume_26: prior completed bar target 50%; next bar open simulation |
| v1 | reversion_12 AND volume_26 | 9933.02 | -66.98 | sell /  / reversion_12 AND volume_26: prior completed bar target 0%; next bar open simulation |
| v1 | reversion_12 + volume_26 | 9844.46 | -155.54 | sell /  / reversion_12 + volume_26: prior completed bar target 0%; next bar open simulation |
| v1 | ema_12_26 | 9770.13 | -229.87 | sell /  / EMA12 > EMA26; 조건 미충족; EMA12=257.771, EMA26=257.934 |
| v1 | macd_12_26_9 | 9887.47 | -112.53 | sell /  / MACD > 신호선 그리고 MACD > 0; 조건 미충족; MACD=1.30676, signal9=1.31668 |
| v1 | rsi_14_recovery | 9923.04 | -76.96 | sell /  / 직전 RSI14 < 30, 현재 RSI14 >= 30 (한 봉 목표); 조건 미충족; RSI14=40.3665, previous_RSI14=36.2025 |
| v1 | bollinger_20_reentry | 9816.96 | -183.04 | sell /  / 직전 종가 < 직전 하단밴드, 현재 하단밴드 <= 종가 <= SMA20 (한 봉 목표); 조건 미충족; close=255.05, lower20=254.819, SMA20=258.099, previous_lower20=255.312 |
| v1 | donchian_20 | 9921.02 | -78.98 | sell /  / 종가 > 현재 봉을 제외한 직전 20봉 최고가; 조건 미충족; close=258.68, prior_high20=260.425 |
| v1 | atr_14_breakout | 9701.58 | -298.42 | sell /  / 종가 > 직전 종가 + 직전 ATR14 그리고 종가 > EMA26; 조건 미충족; close=259.42, threshold=260.032, prior_ATR14=0.777474, EMA26=258.478 |
| v1 | session_vwap | 9644.61 | -355.39 | buy /  / 종가 > 뉴욕 거래일별 누적 전형가격 VWAP; 조건 충족; close=256.05, session_VWAP=255.552, session_volume=3.26826e+06 |
| v1 | obv_20 | 9506.00 | -494.00 | sell /  / OBV > OBV의 SMA20 그리고 종가 > EMA26; 조건 미충족; OBV=1.05978e+07, OBV_SMA20=1.06874e+07, close=256.41, EMA26=258.325 |
| v1 | stochastic_14_3_recovery | 9576.18 | -423.82 | sell /  / 직전 %K14 < 20에서 %K14가 %D3 상향 돌파 (한 봉 목표); 조건 미충족; K14=33.4928, D3=23.2217, previous_K14=28.5165, previous_D3=14.8644 |
| v1 | mfi_14_recovery | 10000.00 | 0.00 | 대기 /  / 새 신호 대기 |
| v1 | adx_14_trend | 9681.33 | -318.67 | sell /  / Wilder ADX14 >= 25 그리고 +DI14 > -DI14; 조건 미충족; ADX14=33.0847, plus_DI14=22.751, minus_DI14=33.7106 |
| v1 | aroon_25_trend | 9899.46 | -100.54 | sell /  / Aroon25 Up > 70 그리고 Down < 30 (동률이면 최신 극값); 조건 미충족; Aroon_up=68, Aroon_down=44 |
| v1 | cci_20_momentum | 9818.66 | -181.34 | sell /  / CCI20 > 100 (전형가격·평균절대편차); 조건 미충족; CCI20=95.1073 |
| v1 | williams_14_recovery | 9706.89 | -293.11 | sell /  / 직전 Williams %R14 < -80, 현재 >= -80 (한 봉 목표); 조건 미충족; Williams_R14=-66.5072, previous_R14=-71.4835 |
| v1 | cmf_20_accumulation | 10060.68 | 60.68 | sell /  / Chaikin Money Flow20 > 0.1; 조건 미충족; CMF20=-0.0883438, volume20=4.47769e+06 |
| v1 | chaikin_3_10 | 9772.24 | -227.76 | sell /  / ADL의 EMA3 - EMA10 > 0 그리고 종가 > EMA26; 조건 미충족; Chaikin3_10=-71247.4, ADL=5.61269e+06, close=256.41, EMA26=258.325 |
| v1 | roc_10_momentum | 9691.76 | -308.24 | sell /  / 10봉 ROC > 1% 그리고 종가 > EMA26; 조건 미충족; ROC10_percent=-0.503419, close=258.91, EMA26=257.09 |
| v1 | trix_15_trend | 9665.05 | -334.95 | sell /  / 15봉 삼중 EMA의 1봉 변화율 TRIX > 0 그리고 종가 > EMA26; 조건 미충족; TRIX15_percent=0.0421187, close=256.41, EMA26=258.325 |
| v1 | keltner_20_breakout | 9916.04 | -83.96 | sell /  / 종가 > EMA20 + 2 x Wilder ATR14; 조건 미충족; close=258.91, upper_Keltner=259.564, EMA20=257.603, ATR14=0.980686 |
| v1 | opening_range_30m | 10000.00 | 0.00 | 대기 /  / 새 신호 대기 |
| v2 | cash | 10000.00 | 0.00 | 대기 /  / 새 신호 대기 |
| v2 | buy_hold | 9754.73 | -245.27 | 중단: 손실 한도 / buy / partial / 직전 완료 봉 목표 비중 100%; 다음 봉 시가 가정 |
| v2 | trend_8_26 | 9754.73 | -245.27 | 중단: 손실 한도 / buy / partial / 직전 완료 봉 목표 비중 100%; 다음 봉 시가 가정 |
| v2 | momentum_26 | 9754.73 | -245.27 | 중단: 손실 한도 / buy / partial / 직전 완료 봉 목표 비중 100%; 다음 봉 시가 가정 |
| v2 | breakout_8 | 9343.39 | -656.61 | 중단: 손실 한도 / sell / filled / 직전 완료 봉 목표 비중 0%; 다음 봉 시가 가정 |
| v2 | reversion_12 | 9434.41 | -565.59 | sell / filled / 직전 완료 봉 목표 비중 0%; 다음 봉 시가 가정 |
| v2 | volume_26 | 9686.16 | -313.84 | sell / filled / 직전 완료 봉 목표 비중 0%; 다음 봉 시가 가정 |
| v2 | trend_8_26 AND momentum_26 | 9754.73 | -245.27 | 중단: 손실 한도 / buy / partial / 직전 완료 봉 목표 비중 100%; 다음 봉 시가 가정 |
| v2 | trend_8_26 + momentum_26 | 9754.73 | -245.27 | 중단: 손실 한도 / buy / partial / 직전 완료 봉 목표 비중 100%; 다음 봉 시가 가정 |
| v2 | trend_8_26 AND breakout_8 | 9419.39 | -580.61 | 중단: 손실 한도 / sell / filled / 직전 완료 봉 목표 비중 0%; 다음 봉 시가 가정 |
| v2 | trend_8_26 + breakout_8 | 9298.94 | -701.06 | sell / filled / 직전 완료 봉 목표 비중 50%; 다음 봉 시가 가정 |
| v2 | trend_8_26 AND reversion_12 | 9900.89 | -99.11 | sell / filled / 직전 완료 봉 목표 비중 0%; 다음 봉 시가 가정 |
| v2 | trend_8_26 + reversion_12 | 9732.92 | -267.08 | 중단: 손실 한도 / sell / filled / 직전 완료 봉 목표 비중 0%; 다음 봉 시가 가정 |
| v2 | trend_8_26 AND volume_26 | 9861.95 | -138.05 | sell / filled / 직전 완료 봉 목표 비중 0%; 다음 봉 시가 가정 |
| v2 | trend_8_26 + volume_26 | 9850.80 | -149.20 | 중단: 손실 한도 / buy / filled / 직전 완료 봉 목표 비중 50%; 다음 봉 시가 가정 |
| v2 | momentum_26 AND breakout_8 | 9385.94 | -614.06 | sell / filled / 직전 완료 봉 목표 비중 0%; 다음 봉 시가 가정 |
| v2 | momentum_26 + breakout_8 | 9145.63 | -854.37 | sell / filled / 직전 완료 봉 목표 비중 50%; 다음 봉 시가 가정 |
| v2 | momentum_26 AND reversion_12 | 9871.83 | -128.17 | sell / filled / 직전 완료 봉 목표 비중 0%; 다음 봉 시가 가정 |
| v2 | momentum_26 + reversion_12 | 9732.92 | -267.08 | 중단: 손실 한도 / sell / filled / 직전 완료 봉 목표 비중 0%; 다음 봉 시가 가정 |
| v2 | momentum_26 AND volume_26 | 9920.93 | -79.07 | sell / filled / 직전 완료 봉 목표 비중 0%; 다음 봉 시가 가정 |
| v2 | momentum_26 + volume_26 | 9850.80 | -149.20 | 중단: 손실 한도 / buy / filled / 직전 완료 봉 목표 비중 50%; 다음 봉 시가 가정 |
| v2 | breakout_8 AND reversion_12 | 10000.00 | 0.00 | 대기 /  / 새 신호 대기 |
| v2 | breakout_8 + reversion_12 | 9173.26 | -826.74 | sell / filled / 직전 완료 봉 목표 비중 50%; 다음 봉 시가 가정 |
| v2 | breakout_8 AND volume_26 | 9814.17 | -185.83 | sell / filled / 직전 완료 봉 목표 비중 0%; 다음 봉 시가 가정 |
| v2 | breakout_8 + volume_26 | 9294.97 | -705.03 | sell / filled / 직전 완료 봉 목표 비중 50%; 다음 봉 시가 가정 |
| v2 | reversion_12 AND volume_26 | 9816.09 | -183.91 | sell / filled / 직전 완료 봉 목표 비중 0%; 다음 봉 시가 가정 |
| v2 | reversion_12 + volume_26 | 9599.90 | -400.10 | sell / filled / 직전 완료 봉 목표 비중 0%; 다음 봉 시가 가정 |
| v2 | ema_12_26 | 9764.26 | -235.74 | sell / filled / EMA12 > EMA26; 조건 미충족; EMA12=257.771, EMA26=257.934; 직전 완료 봉 목표를 다음 봉 시가에 모의 적용 |
| v2 | macd_12_26_9 | 9881.54 | -118.46 | sell / filled / MACD > 신호선 그리고 MACD > 0; 조건 미충족; MACD=1.30676, signal9=1.31668; 직전 완료 봉 목표를 다음 봉 시가에 모의 적용 |
| v2 | rsi_14_recovery | 9919.07 | -80.93 | sell / filled / 직전 RSI14 < 30, 현재 RSI14 >= 30 (한 봉 목표); 조건 미충족; RSI14=40.3665, previous_RSI14=36.2025; 직전 완료 봉 목표를 다음 봉 시가에 모의 적용 |
| v2 | bollinger_20_reentry | 9811.07 | -188.93 | sell / filled / 직전 종가 < 직전 하단밴드, 현재 하단밴드 <= 종가 <= SMA20 (한 봉 목표); 조건 미충족; close=255.05, lower20=254.819, SMA20=258.099, previous_lower20=255.312; 직전 완료 봉 목표를 다음 봉 시가에 모의 적용 |
| v2 | donchian_20 | 9919.03 | -80.97 | sell / filled / 종가 > 현재 봉을 제외한 직전 20봉 최고가; 조건 미충족; close=258.68, prior_high20=260.425; 직전 완료 봉 목표를 다음 봉 시가에 모의 적용 |
| v2 | atr_14_breakout | 9693.82 | -306.18 | sell / filled / 종가 > 직전 종가 + 직전 ATR14 그리고 종가 > EMA26; 조건 미충족; close=259.42, threshold=260.032, prior_ATR14=0.777474, EMA26=258.478; 직전 완료 봉 목표를 다음 봉 시가에 모의 적용 |
| v2 | session_vwap | 9626.31 | -373.69 | buy / partial / 종가 > 뉴욕 거래일별 누적 전형가격 VWAP; 조건 충족; close=256.05, session_VWAP=255.552, session_volume=3.26826e+06; 직전 완료 봉 목표를 다음 봉 시가에 모의 적용 |
| v2 | obv_20 | 9488.91 | -511.09 | sell / filled / OBV > OBV의 SMA20 그리고 종가 > EMA26; 조건 미충족; OBV=1.05978e+07, OBV_SMA20=1.06874e+07, close=256.41, EMA26=258.325; 직전 완료 봉 목표를 다음 봉 시가에 모의 적용 |
| v2 | stochastic_14_3_recovery | 9560.87 | -439.13 | sell / filled / 직전 %K14 < 20에서 %K14가 %D3 상향 돌파 (한 봉 목표); 조건 미충족; K14=33.4928, D3=23.2217, previous_K14=28.5165, previous_D3=14.8644; 직전 완료 봉 목표를 다음 봉 시가에 모의 적용 |
| v2 | mfi_14_recovery | 10000.00 | 0.00 | 대기 /  / 새 신호 대기 |
| v2 | adx_14_trend | 9673.58 | -326.42 | sell / filled / Wilder ADX14 >= 25 그리고 +DI14 > -DI14; 조건 미충족; ADX14=33.0847, plus_DI14=22.751, minus_DI14=33.7106; 직전 완료 봉 목표를 다음 봉 시가에 모의 적용 |
| v2 | aroon_25_trend | 9895.50 | -104.50 | sell / filled / Aroon25 Up > 70 그리고 Down < 30 (동률이면 최신 극값); 조건 미충족; Aroon_up=68, Aroon_down=44; 직전 완료 봉 목표를 다음 봉 시가에 모의 적용 |
| v2 | cci_20_momentum | 9812.77 | -187.23 | sell / filled / CCI20 > 100 (전형가격·평균절대편차); 조건 미충족; CCI20=95.1073; 직전 완료 봉 목표를 다음 봉 시가에 모의 적용 |
| v2 | williams_14_recovery | 9697.19 | -302.81 | sell / filled / 직전 Williams %R14 < -80, 현재 >= -80 (한 봉 목표); 조건 미충족; Williams_R14=-66.5072, previous_R14=-71.4835; 직전 완료 봉 목표를 다음 봉 시가에 모의 적용 |
| v2 | cmf_20_accumulation | 10056.66 | 56.66 | sell / filled / Chaikin Money Flow20 > 0.1; 조건 미충족; CMF20=-0.0883438, volume20=4.47769e+06; 직전 완료 봉 목표를 다음 봉 시가에 모의 적용 |
| v2 | chaikin_3_10 | 9764.42 | -235.58 | sell / filled / ADL의 EMA3 - EMA10 > 0 그리고 종가 > EMA26; 조건 미충족; Chaikin3_10=-71247.4, ADL=5.61269e+06, close=256.41, EMA26=258.325; 직전 완료 봉 목표를 다음 봉 시가에 모의 적용 |
| v2 | roc_10_momentum | 9684.01 | -315.99 | sell / filled / 10봉 ROC > 1% 그리고 종가 > EMA26; 조건 미충족; ROC10_percent=-0.503419, close=258.91, EMA26=257.09; 직전 완료 봉 목표를 다음 봉 시가에 모의 적용 |
| v2 | trix_15_trend | 9659.25 | -340.75 | sell / filled / 15봉 삼중 EMA의 1봉 변화율 TRIX > 0 그리고 종가 > EMA26; 조건 미충족; TRIX15_percent=0.0421187, close=256.41, EMA26=258.325; 직전 완료 봉 목표를 다음 봉 시가에 모의 적용 |
| v2 | keltner_20_breakout | 9914.05 | -85.95 | sell / filled / 종가 > EMA20 + 2 x Wilder ATR14; 조건 미충족; close=258.91, upper_Keltner=259.564, EMA20=257.603, ATR14=0.980686; 직전 완료 봉 목표를 다음 봉 시가에 모의 적용 |
| v2 | opening_range_30m | 10000.00 | 0.00 | 대기 /  / 새 신호 대기 |

### 같은 기간의 비용·노출 비교 (사후 연구)

| 전략 | 비용 전 | 비용 후 | 100% 보유 | 같은 평균 노출 보유 | 평균 노출 |
|---|---:|---:|---:|---:|---:|
| cash | 0.00% | 0.00% | -4.09% | -0.00% | 0.00% |
| buy_hold | -3.69% | -4.09% | -4.09% | -4.09% | 100.00% |
| trend_8_26 | 2.60% | 0.47% | -4.09% | -2.00% | 47.89% |
| momentum_26 | -0.86% | -3.74% | -4.09% | -1.93% | 46.32% |
| breakout_8 | -1.06% | -18.10% | -4.09% | -0.87% | 20.53% |
| reversion_12 | -6.59% | -14.83% | -4.09% | -1.30% | 31.05% |
| volume_26 | -0.49% | -7.35% | -4.09% | -0.28% | 6.58% |
| trend_8_26 AND momentum_26 | 0.79% | -1.72% | -4.09% | -1.71% | 40.79% |
| trend_8_26 + momentum_26 | 0.86% | -1.65% | -4.09% | -1.97% | 47.11% |
| trend_8_26 AND breakout_8 | 0.14% | -11.71% | -4.09% | -0.58% | 13.68% |
| trend_8_26 + breakout_8 | 0.78% | -9.08% | -4.09% | -1.44% | 34.22% |
| trend_8_26 AND reversion_12 | 1.37% | -1.98% | -4.09% | -0.25% | 5.79% |
| trend_8_26 + reversion_12 | -2.06% | -7.29% | -4.09% | -1.65% | 39.48% |
| trend_8_26 AND volume_26 | 1.42% | -1.10% | -4.09% | -0.07% | 1.58% |
| trend_8_26 + volume_26 | 1.08% | -3.30% | -4.09% | -1.15% | 27.24% |
| momentum_26 AND breakout_8 | 1.00% | -9.83% | -4.09% | -0.55% | 12.89% |
| momentum_26 + breakout_8 | -0.94% | -11.00% | -4.09% | -1.40% | 33.43% |
| momentum_26 AND reversion_12 | -0.27% | -3.16% | -4.09% | -0.27% | 6.32% |
| momentum_26 + reversion_12 | -3.74% | -8.88% | -4.09% | -1.62% | 38.69% |
| momentum_26 AND volume_26 | 0.14% | -0.70% | -4.09% | -0.02% | 0.53% |
| momentum_26 + volume_26 | -0.64% | -4.55% | -4.09% | -1.11% | 26.45% |
| breakout_8 AND reversion_12 | 0.00% | 0.00% | -4.09% | -0.00% | 0.00% |
| breakout_8 + reversion_12 | -3.85% | -16.14% | -4.09% | -1.09% | 25.80% |
| breakout_8 AND volume_26 | -0.46% | -1.29% | -4.09% | -0.02% | 0.53% |
| breakout_8 + volume_26 | -0.77% | -11.97% | -4.09% | -0.57% | 13.56% |
| reversion_12 AND volume_26 | -1.86% | -5.10% | -4.09% | -0.13% | 3.16% |
| reversion_12 + volume_26 | -3.57% | -10.61% | -4.09% | -0.79% | 18.82% |
| ema_12_26 | -1.05% | -3.51% | -4.09% | -1.96% | 46.84% |
| macd_12_26_9 | 5.83% | 2.76% | -4.09% | -1.24% | 29.47% |
| rsi_14_recovery | -1.35% | -6.20% | -4.09% | -0.13% | 3.16% |
| bollinger_20_reentry | -1.34% | -6.19% | -4.09% | -0.13% | 3.16% |
| donchian_20 | 0.68% | -6.26% | -4.09% | -0.28% | 6.58% |
| atr_14_breakout | 0.24% | -5.88% | -4.09% | -0.20% | 4.74% |
| session_vwap | 3.04% | -5.66% | -4.09% | -2.03% | 48.68% |
| obv_20 | -5.78% | -15.17% | -4.09% | -1.49% | 35.53% |
| stochastic_14_3_recovery | -1.10% | -14.26% | -4.09% | -0.38% | 8.95% |
| mfi_14_recovery | 0.33% | -0.93% | -4.09% | -0.03% | 0.79% |
| adx_14_trend | -3.61% | -8.35% | -4.09% | -1.54% | 36.84% |
| aroon_25_trend | 3.28% | -0.55% | -4.09% | -1.26% | 30.00% |
| cci_20_momentum | 0.58% | -5.17% | -4.09% | -0.83% | 19.74% |
| williams_14_recovery | -2.42% | -10.28% | -4.09% | -0.22% | 5.26% |
| cmf_20_accumulation | 4.00% | -0.27% | -4.09% | -1.46% | 34.74% |
| chaikin_3_10 | -3.43% | -8.18% | -4.09% | -1.58% | 37.63% |
| roc_10_momentum | -2.79% | -9.49% | -4.09% | -0.74% | 17.63% |
| trix_15_trend | -1.61% | -4.06% | -4.09% | -1.50% | 35.79% |
| keltner_20_breakout | 0.20% | -3.52% | -4.09% | -0.50% | 11.84% |
| opening_range_30m | 0.79% | -2.95% | -4.09% | -1.10% | 26.05% |

동일 구간·초기 자금, 종료 시 청산 비용 포함. 노출 맞춤은 사후 설명용이며 v2 실제 계좌 성과가 아닙니다.
[낙폭 분해·비용 영향·전체 구간](JNJ/comparison.json)

[v1 전체 기록](JNJ/accounts.json) · [v2 전체 기록](JNJ/accounts-v2.json)

## CAT 계좌

| 모델 | 전략 | 평가액 USD | 손익 USD | 최근 매매·이유 |
|---|---|---:|---:|---|
| v1 | cash | 10000.00 | 0.00 | 대기 /  / 새 신호 대기 |
| v1 | buy_hold | 10027.12 | 27.12 | buy /  / buy_hold: prior completed bar target 100%; next bar open simulation |
| v1 | trend_8_26 | 9949.26 | -50.74 | buy /  / trend_8_26: prior completed bar target 100%; next bar open simulation |
| v1 | momentum_26 | 9658.24 | -341.76 | buy /  / momentum_26: prior completed bar target 100%; next bar open simulation |
| v1 | breakout_8 | 9539.74 | -460.26 | sell /  / breakout_8: prior completed bar target 0%; next bar open simulation |
| v1 | reversion_12 | 9921.83 | -78.17 | sell /  / reversion_12: prior completed bar target 0%; next bar open simulation |
| v1 | volume_26 | 9916.22 | -83.78 | sell /  / volume_26: prior completed bar target 0%; next bar open simulation |
| v1 | trend_8_26 AND momentum_26 | 9846.02 | -153.98 | buy /  / trend_8_26 AND momentum_26: prior completed bar target 100%; next bar open simulation |
| v1 | trend_8_26 + momentum_26 | 9803.74 | -196.26 | buy /  / trend_8_26 + momentum_26: prior completed bar target 100%; next bar open simulation |
| v1 | trend_8_26 AND breakout_8 | 9742.58 | -257.42 | sell /  / trend_8_26 AND breakout_8: prior completed bar target 0%; next bar open simulation |
| v1 | trend_8_26 + breakout_8 | 9743.42 | -256.58 | sell /  / trend_8_26 + breakout_8: prior completed bar target 50%; next bar open simulation |
| v1 | trend_8_26 AND reversion_12 | 9928.06 | -71.94 | sell /  / trend_8_26 AND reversion_12: prior completed bar target 0%; next bar open simulation |
| v1 | trend_8_26 + reversion_12 | 9976.91 | -23.09 | buy /  / trend_8_26 + reversion_12: prior completed bar target 50%; next bar open simulation |
| v1 | trend_8_26 AND volume_26 | 9965.69 | -34.31 | sell /  / trend_8_26 AND volume_26: prior completed bar target 0%; next bar open simulation |
| v1 | trend_8_26 + volume_26 | 9953.55 | -46.45 | buy /  / trend_8_26 + volume_26: prior completed bar target 50%; next bar open simulation |
| v1 | momentum_26 AND breakout_8 | 9610.59 | -389.41 | sell /  / momentum_26 AND breakout_8: prior completed bar target 0%; next bar open simulation |
| v1 | momentum_26 + breakout_8 | 9598.90 | -401.10 | sell /  / momentum_26 + breakout_8: prior completed bar target 50%; next bar open simulation |
| v1 | momentum_26 AND reversion_12 | 9887.21 | -112.79 | sell /  / momentum_26 AND reversion_12: prior completed bar target 0%; next bar open simulation |
| v1 | momentum_26 + reversion_12 | 9789.76 | -210.24 | buy /  / momentum_26 + reversion_12: prior completed bar target 50%; next bar open simulation |
| v1 | momentum_26 AND volume_26 | 9894.55 | -105.45 | sell /  / momentum_26 AND volume_26: prior completed bar target 0%; next bar open simulation |
| v1 | momentum_26 + volume_26 | 9786.38 | -213.62 | buy /  / momentum_26 + volume_26: prior completed bar target 50%; next bar open simulation |
| v1 | breakout_8 AND reversion_12 | 10000.00 | 0.00 | 대기 /  / 새 신호 대기 |
| v1 | breakout_8 + reversion_12 | 9729.43 | -270.57 | sell /  / breakout_8 + reversion_12: prior completed bar target 0%; next bar open simulation |
| v1 | breakout_8 AND volume_26 | 9894.55 | -105.45 | sell /  / breakout_8 AND volume_26: prior completed bar target 0%; next bar open simulation |
| v1 | breakout_8 + volume_26 | 9726.15 | -273.85 | sell /  / breakout_8 + volume_26: prior completed bar target 0%; next bar open simulation |
| v1 | reversion_12 AND volume_26 | 10046.29 | 46.29 | sell /  / reversion_12 AND volume_26: prior completed bar target 0%; next bar open simulation |
| v1 | reversion_12 + volume_26 | 9919.48 | -80.52 | sell /  / reversion_12 + volume_26: prior completed bar target 0%; next bar open simulation |
| v1 | ema_12_26 | 9977.39 | -22.61 | buy /  / EMA12 > EMA26; 조건 충족; EMA12=726.261, EMA26=726.172 |
| v1 | macd_12_26_9 | 10019.59 | 19.59 | buy /  / MACD > 신호선 그리고 MACD > 0; 조건 충족; MACD=0.0889648, signal9=-0.313692 |
| v1 | rsi_14_recovery | 9999.22 | -0.78 | sell /  / 직전 RSI14 < 30, 현재 RSI14 >= 30 (한 봉 목표); 조건 미충족; RSI14=43.621, previous_RSI14=38.5787 |
| v1 | bollinger_20_reentry | 9777.09 | -222.91 | sell /  / 직전 종가 < 직전 하단밴드, 현재 하단밴드 <= 종가 <= SMA20 (한 봉 목표); 조건 미충족; close=721.16, lower20=716.851, SMA20=725.821, previous_lower20=717.276 |
| v1 | donchian_20 | 9943.28 | -56.72 | sell /  / 종가 > 현재 봉을 제외한 직전 20봉 최고가; 조건 미충족; close=735.35, prior_high20=745 |
| v1 | atr_14_breakout | 9768.31 | -231.69 | sell /  / 종가 > 직전 종가 + 직전 ATR14 그리고 종가 > EMA26; 조건 미충족; close=735.35, threshold=737.263, prior_ATR14=4.10289, EMA26=727.331 |
| v1 | session_vwap | 9623.20 | -376.80 | buy /  / 종가 > 뉴욕 거래일별 누적 전형가격 VWAP; 조건 충족; close=734.98, session_VWAP=734.093, session_volume=764353 |
| v1 | obv_20 | 9918.81 | -81.19 | buy /  / OBV > OBV의 SMA20 그리고 종가 > EMA26; 조건 충족; OBV=-5.0567e+06, OBV_SMA20=-6.30537e+06, close=733.16, EMA26=726.69 |
| v1 | stochastic_14_3_recovery | 9855.08 | -144.92 | sell /  / 직전 %K14 < 20에서 %K14가 %D3 상향 돌파 (한 봉 목표); 조건 미충족; K14=59.6496, D3=39.2535, previous_K14=43.8356, previous_D3=33.8642 |
| v1 | mfi_14_recovery | 10068.63 | 68.63 | sell /  / 직전 MFI14 < 20, 현재 MFI14 >= 20 (한 봉 목표); 조건 미충족; MFI14=32.7313, previous_MFI14=24.1736 |
| v1 | adx_14_trend | 9994.59 | -5.41 | buy /  / Wilder ADX14 >= 25 그리고 +DI14 > -DI14; 조건 충족; ADX14=25.4031, plus_DI14=35.2628, minus_DI14=13.9603 |
| v1 | aroon_25_trend | 9979.61 | -20.39 | sell /  / Aroon25 Up > 70 그리고 Down < 30 (동률이면 최신 극값); 조건 미충족; Aroon_up=68, Aroon_down=20 |
| v1 | cci_20_momentum | 9840.53 | -159.47 | buy /  / CCI20 > 100 (전형가격·평균절대편차); 조건 충족; CCI20=103.948 |
| v1 | williams_14_recovery | 10007.06 | 7.06 | sell /  / 직전 Williams %R14 < -80, 현재 >= -80 (한 봉 목표); 조건 미충족; Williams_R14=-40.3504, previous_R14=-56.1644 |
| v1 | cmf_20_accumulation | 9872.23 | -127.77 | sell /  / Chaikin Money Flow20 > 0.1; 조건 미충족; CMF20=0.061511, volume20=3.85936e+06 |
| v1 | chaikin_3_10 | 9675.14 | -324.86 | buy /  / ADL의 EMA3 - EMA10 > 0 그리고 종가 > EMA26; 조건 충족; Chaikin3_10=1976.77, ADL=-5.29509e+06, close=736.7, EMA26=730.386 |
| v1 | roc_10_momentum | 9912.41 | -87.59 | sell /  / 10봉 ROC > 1% 그리고 종가 > EMA26; 조건 미충족; ROC10_percent=0.482847, close=736.7, EMA26=730.386 |
| v1 | trix_15_trend | 9710.15 | -289.85 | buy /  / 15봉 삼중 EMA의 1봉 변화율 TRIX > 0 그리고 종가 > EMA26; 조건 충족; TRIX15_percent=0.00081134, close=733.16, EMA26=726.69 |
| v1 | keltner_20_breakout | 10000.00 | 0.00 | 대기 /  / 새 신호 대기 |
| v1 | opening_range_30m | 10162.22 | 162.22 | sell /  / 뉴욕 09:30·09:45 두 완료 봉 최고가를 10:00 이후 종가가 돌파; 자료 부족·변동폭 또는 거래량 없음: 대기; close=733.16 |
| v2 | cash | 10000.00 | 0.00 | 대기 /  / 새 신호 대기 |
| v2 | buy_hold | 9221.69 | -778.31 | 중단: 손실 한도 / buy / partial / 직전 완료 봉 목표 비중 100%; 다음 봉 시가 가정 |
| v2 | trend_8_26 | 9867.45 | -132.55 | buy / partial / 직전 완료 봉 목표 비중 100%; 다음 봉 시가 가정 |
| v2 | momentum_26 | 9659.76 | -340.24 | buy / partial / 직전 완료 봉 목표 비중 100%; 다음 봉 시가 가정 |
| v2 | breakout_8 | 9354.04 | -645.96 | sell / filled / 직전 완료 봉 목표 비중 0%; 다음 봉 시가 가정 |
| v2 | reversion_12 | 9092.90 | -907.10 | 중단: 손실 한도 / buy / partial / 직전 완료 봉 목표 비중 100%; 다음 봉 시가 가정 |
| v2 | volume_26 | 9352.95 | -647.05 | 중단: 손실 한도 / buy / partial / 직전 완료 봉 목표 비중 100%; 다음 봉 시가 가정 |
| v2 | trend_8_26 AND momentum_26 | 9882.01 | -117.99 | buy / partial / 직전 완료 봉 목표 비중 100%; 다음 봉 시가 가정 |
| v2 | trend_8_26 + momentum_26 | 9764.11 | -235.89 | buy / partial / 직전 완료 봉 목표 비중 100%; 다음 봉 시가 가정 |
| v2 | trend_8_26 AND breakout_8 | 9652.48 | -347.52 | sell / filled / 직전 완료 봉 목표 비중 0%; 다음 봉 시가 가정 |
| v2 | trend_8_26 + breakout_8 | 9608.63 | -391.37 | sell / filled / 직전 완료 봉 목표 비중 50%; 다음 봉 시가 가정 |
| v2 | trend_8_26 AND reversion_12 | 9738.62 | -261.38 | sell / filled / 직전 완료 봉 목표 비중 0%; 다음 봉 시가 가정 |
| v2 | trend_8_26 + reversion_12 | 9592.85 | -407.15 | buy / filled / 직전 완료 봉 목표 비중 50%; 다음 봉 시가 가정 |
| v2 | trend_8_26 AND volume_26 | 9999.01 | -0.99 | sell / filled / 직전 완료 봉 목표 비중 0%; 다음 봉 시가 가정 |
| v2 | trend_8_26 + volume_26 | 9581.08 | -418.92 | buy / filled / 직전 완료 봉 목표 비중 50%; 다음 봉 시가 가정 |
| v2 | momentum_26 AND breakout_8 | 9573.57 | -426.43 | sell / filled / 직전 완료 봉 목표 비중 0%; 다음 봉 시가 가정 |
| v2 | momentum_26 + breakout_8 | 9505.95 | -494.05 | sell / filled / 직전 완료 봉 목표 비중 50%; 다음 봉 시가 가정 |
| v2 | momentum_26 AND reversion_12 | 9755.55 | -244.45 | sell / filled / 직전 완료 봉 목표 비중 0%; 다음 봉 시가 가정 |
| v2 | momentum_26 + reversion_12 | 9450.69 | -549.31 | buy / filled / 직전 완료 봉 목표 비중 50%; 다음 봉 시가 가정 |
| v2 | momentum_26 AND volume_26 | 9936.85 | -63.15 | sell / filled / 직전 완료 봉 목표 비중 0%; 다음 봉 시가 가정 |
| v2 | momentum_26 + volume_26 | 9478.83 | -521.17 | buy / filled / 직전 완료 봉 목표 비중 50%; 다음 봉 시가 가정 |
| v2 | breakout_8 AND reversion_12 | 10000.00 | 0.00 | 대기 /  / 새 신호 대기 |
| v2 | breakout_8 + reversion_12 | 9610.18 | -389.82 | 중단: 손실 한도 / sell / filled / 직전 완료 봉 목표 비중 0%; 다음 봉 시가 가정 |
| v2 | breakout_8 AND volume_26 | 9887.31 | -112.69 | sell / filled / 직전 완료 봉 목표 비중 0%; 다음 봉 시가 가정 |
| v2 | breakout_8 + volume_26 | 9327.77 | -672.23 | sell / filled / 직전 완료 봉 목표 비중 0%; 다음 봉 시가 가정 |
| v2 | reversion_12 AND volume_26 | 9288.25 | -711.75 | 중단: 손실 한도 / buy / partial / 직전 완료 봉 목표 비중 100%; 다음 봉 시가 가정 |
| v2 | reversion_12 + volume_26 | 9409.38 | -590.62 | 중단: 손실 한도 / sell / filled / 직전 완료 봉 목표 비중 50%; 다음 봉 시가 가정 |
| v2 | ema_12_26 | 9974.40 | -25.60 | buy / partial / EMA12 > EMA26; 조건 충족; EMA12=726.261, EMA26=726.172; 직전 완료 봉 목표를 다음 봉 시가에 모의 적용 |
| v2 | macd_12_26_9 | 10016.58 | 16.58 | buy / partial / MACD > 신호선 그리고 MACD > 0; 조건 충족; MACD=0.0889648, signal9=-0.313692; 직전 완료 봉 목표를 다음 봉 시가에 모의 적용 |
| v2 | rsi_14_recovery | 9995.22 | -4.78 | sell / filled / 직전 RSI14 < 30, 현재 RSI14 >= 30 (한 봉 목표); 조건 미충족; RSI14=43.621, previous_RSI14=38.5787; 직전 완료 봉 목표를 다음 봉 시가에 모의 적용 |
| v2 | bollinger_20_reentry | 9771.22 | -228.78 | sell / filled / 직전 종가 < 직전 하단밴드, 현재 하단밴드 <= 종가 <= SMA20 (한 봉 목표); 조건 미충족; close=721.16, lower20=716.851, SMA20=725.821, previous_lower20=717.276; 직전 완료 봉 목표를 다음 봉 시가에 모의 적용 |
| v2 | donchian_20 | 9939.30 | -60.70 | sell / filled / 종가 > 현재 봉을 제외한 직전 20봉 최고가; 조건 미충족; close=735.35, prior_high20=745; 직전 완료 봉 목표를 다음 봉 시가에 모의 적용 |
| v2 | atr_14_breakout | 9758.55 | -241.45 | sell / filled / 종가 > 직전 종가 + 직전 ATR14 그리고 종가 > EMA26; 조건 미충족; close=735.35, threshold=737.263, prior_ATR14=4.10289, EMA26=727.331; 직전 완료 봉 목표를 다음 봉 시가에 모의 적용 |
| v2 | session_vwap | 9604.94 | -395.06 | buy / partial / 종가 > 뉴욕 거래일별 누적 전형가격 VWAP; 조건 충족; close=734.98, session_VWAP=734.093, session_volume=764353; 직전 완료 봉 목표를 다음 봉 시가에 모의 적용 |
| v2 | obv_20 | 9907.91 | -92.09 | buy / partial / OBV > OBV의 SMA20 그리고 종가 > EMA26; 조건 충족; OBV=-5.0567e+06, OBV_SMA20=-6.30537e+06, close=733.16, EMA26=726.69; 직전 완료 봉 목표를 다음 봉 시가에 모의 적용 |
| v2 | stochastic_14_3_recovery | 9843.26 | -156.74 | sell / filled / 직전 %K14 < 20에서 %K14가 %D3 상향 돌파 (한 봉 목표); 조건 미충족; K14=59.6496, D3=39.2535, previous_K14=43.8356, previous_D3=33.8642; 직전 완료 봉 목표를 다음 봉 시가에 모의 적용 |
| v2 | mfi_14_recovery | 10064.61 | 64.61 | sell / filled / 직전 MFI14 < 20, 현재 MFI14 >= 20 (한 봉 목표); 조건 미충족; MFI14=32.7313, previous_MFI14=24.1736; 직전 완료 봉 목표를 다음 봉 시가에 모의 적용 |
| v2 | adx_14_trend | 9993.59 | -6.41 | buy / partial / Wilder ADX14 >= 25 그리고 +DI14 > -DI14; 조건 충족; ADX14=25.4031, plus_DI14=35.2628, minus_DI14=13.9603; 직전 완료 봉 목표를 다음 봉 시가에 모의 적용 |
| v2 | aroon_25_trend | 9973.62 | -26.38 | sell / filled / Aroon25 Up > 70 그리고 Down < 30 (동률이면 최신 극값); 조건 미충족; Aroon_up=68, Aroon_down=20; 직전 완료 봉 목표를 다음 봉 시가에 모의 적용 |
| v2 | cci_20_momentum | 9833.65 | -166.35 | buy / partial / CCI20 > 100 (전형가격·평균절대편차); 조건 충족; CCI20=103.948; 직전 완료 봉 목표를 다음 봉 시가에 모의 적용 |
| v2 | williams_14_recovery | 9999.06 | -0.94 | sell / filled / 직전 Williams %R14 < -80, 현재 >= -80 (한 봉 목표); 조건 미충족; Williams_R14=-40.3504, previous_R14=-56.1644; 직전 완료 봉 목표를 다음 봉 시가에 모의 적용 |
| v2 | cmf_20_accumulation | 9864.34 | -135.66 | sell / filled / Chaikin Money Flow20 > 0.1; 조건 미충족; CMF20=0.061511, volume20=3.85936e+06; 직전 완료 봉 목표를 다음 봉 시가에 모의 적용 |
| v2 | chaikin_3_10 | 9711.78 | -288.22 | 중단: 손실 한도 / buy / partial / ADL의 EMA3 - EMA10 > 0 그리고 종가 > EMA26; 조건 충족; Chaikin3_10=293683, ADL=-4.91156e+06, close=739.58, EMA26=736.187; 직전 완료 봉 목표를 다음 봉 시가에 모의 적용 |
| v2 | roc_10_momentum | 9906.47 | -93.53 | sell / filled / 10봉 ROC > 1% 그리고 종가 > EMA26; 조건 미충족; ROC10_percent=0.482847, close=736.7, EMA26=730.386; 직전 완료 봉 목표를 다음 봉 시가에 모의 적용 |
| v2 | trix_15_trend | 9721.57 | -278.43 | 중단: 손실 한도 / buy / partial / 15봉 삼중 EMA의 1봉 변화율 TRIX > 0 그리고 종가 > EMA26; 조건 충족; TRIX15_percent=0.0196284, close=739.58, EMA26=736.187; 직전 완료 봉 목표를 다음 봉 시가에 모의 적용 |
| v2 | keltner_20_breakout | 10000.00 | 0.00 | 대기 /  / 새 신호 대기 |
| v2 | opening_range_30m | 10158.15 | 158.15 | sell / filled / 뉴욕 09:30·09:45 두 완료 봉 최고가를 10:00 이후 종가가 돌파; 자료 부족·변동폭 또는 거래량 없음: 대기; close=733.16; 직전 완료 봉 목표를 다음 봉 시가에 모의 적용 |

### 같은 기간의 비용·노출 비교 (사후 연구)

| 전략 | 비용 전 | 비용 후 | 100% 보유 | 같은 평균 노출 보유 | 평균 노출 |
|---|---:|---:|---:|---:|---:|
| cash | 0.00% | 0.00% | -9.85% | -0.00% | 0.00% |
| buy_hold | -9.47% | -9.85% | -9.85% | -9.85% | 100.00% |
| trend_8_26 | 1.51% | -2.25% | -9.85% | -4.63% | 46.05% |
| momentum_26 | -1.25% | -6.10% | -9.85% | -4.50% | 44.74% |
| breakout_8 | -3.37% | -15.88% | -9.85% | -1.53% | 15.00% |
| reversion_12 | -2.52% | -15.13% | -9.85% | -2.67% | 26.32% |
| volume_26 | -1.22% | -8.80% | -9.85% | -0.86% | 8.42% |
| trend_8_26 AND momentum_26 | 2.13% | -1.25% | -9.85% | -3.93% | 38.95% |
| trend_8_26 + momentum_26 | 0.15% | -4.18% | -9.85% | -4.57% | 45.40% |
| trend_8_26 AND breakout_8 | -1.90% | -9.05% | -9.85% | -0.81% | 7.89% |
| trend_8_26 + breakout_8 | -0.92% | -9.10% | -9.85% | -3.09% | 30.53% |
| trend_8_26 AND reversion_12 | 0.65% | -5.10% | -9.85% | -0.51% | 5.00% |
| trend_8_26 + reversion_12 | -0.44% | -8.11% | -9.85% | -3.65% | 36.19% |
| trend_8_26 AND volume_26 | 2.90% | 1.18% | -9.85% | -0.16% | 1.58% |
| trend_8_26 + volume_26 | 0.20% | -5.15% | -9.85% | -2.76% | 27.24% |
| momentum_26 AND breakout_8 | -2.64% | -10.86% | -9.85% | -0.89% | 8.68% |
| momentum_26 + breakout_8 | -2.28% | -11.10% | -9.85% | -3.02% | 29.87% |
| momentum_26 AND reversion_12 | -3.16% | -8.69% | -9.85% | -0.59% | 5.79% |
| momentum_26 + reversion_12 | -1.83% | -10.52% | -9.85% | -3.59% | 35.53% |
| momentum_26 AND volume_26 | 2.69% | 0.55% | -9.85% | -0.16% | 1.58% |
| momentum_26 + volume_26 | -1.18% | -7.04% | -9.85% | -2.69% | 26.58% |
| breakout_8 AND reversion_12 | 0.00% | 0.00% | -9.85% | -0.00% | 0.00% |
| breakout_8 + reversion_12 | -2.89% | -14.59% | -9.85% | -2.10% | 20.67% |
| breakout_8 AND volume_26 | 0.55% | -1.13% | -9.85% | -0.11% | 1.05% |
| breakout_8 + volume_26 | -2.27% | -11.84% | -9.85% | -1.19% | 11.72% |
| reversion_12 AND volume_26 | -0.54% | -5.03% | -9.85% | -0.54% | 5.26% |
| reversion_12 + volume_26 | -1.83% | -11.63% | -9.85% | -1.77% | 17.37% |
| ema_12_26 | 1.25% | -0.44% | -9.85% | -4.24% | 42.11% |
| macd_12_26_9 | 3.56% | 0.98% | -9.85% | -2.75% | 27.11% |
| rsi_14_recovery | -0.17% | -6.26% | -9.85% | -0.40% | 3.95% |
| bollinger_20_reentry | 0.54% | -5.20% | -9.85% | -0.38% | 3.68% |
| donchian_20 | -0.84% | -4.91% | -9.85% | -0.48% | 4.74% |
| atr_14_breakout | -1.25% | -7.28% | -9.85% | -0.43% | 4.21% |
| session_vwap | 2.88% | -10.06% | -9.85% | -4.89% | 48.68% |
| obv_20 | -1.01% | -10.50% | -9.85% | -2.27% | 22.37% |
| stochastic_14_3_recovery | -1.65% | -11.45% | -9.85% | -0.67% | 6.58% |
| mfi_14_recovery | 1.96% | -1.00% | -9.85% | -0.19% | 1.84% |
| adx_14_trend | -1.87% | -4.32% | -9.85% | -0.91% | 8.95% |
| aroon_25_trend | 0.17% | -3.54% | -9.85% | -1.18% | 11.58% |
| cci_20_momentum | -3.47% | -8.60% | -9.85% | -1.50% | 14.74% |
| williams_14_recovery | 0.89% | -6.85% | -9.85% | -0.51% | 5.00% |
| cmf_20_accumulation | -3.04% | -9.72% | -9.85% | -1.92% | 18.95% |
| chaikin_3_10 | -2.56% | -11.53% | -9.85% | -3.06% | 30.26% |
| roc_10_momentum | -1.40% | -7.42% | -9.85% | -1.37% | 13.42% |
| trix_15_trend | -0.13% | -4.24% | -9.85% | -3.32% | 32.89% |
| keltner_20_breakout | -2.87% | -5.29% | -9.85% | -0.27% | 2.63% |
| opening_range_30m | 7.86% | 2.99% | -9.85% | -2.67% | 26.32% |

동일 구간·초기 자금, 종료 시 청산 비용 포함. 노출 맞춤은 사후 설명용이며 v2 실제 계좌 성과가 아닙니다.
[낙폭 분해·비용 영향·전체 구간](CAT/comparison.json)

[v1 전체 기록](CAT/accounts.json) · [v2 전체 기록](CAT/accounts-v2.json)

## WMT 계좌

| 모델 | 전략 | 평가액 USD | 손익 USD | 최근 매매·이유 |
|---|---|---:|---:|---|
| v1 | cash | 10000.00 | 0.00 | 대기 /  / 새 신호 대기 |
| v1 | buy_hold | 9963.56 | -36.44 | buy /  / buy_hold: prior completed bar target 100%; next bar open simulation |
| v1 | trend_8_26 | 9791.85 | -208.15 | sell /  / trend_8_26: prior completed bar target 0%; next bar open simulation |
| v1 | momentum_26 | 9801.37 | -198.63 | sell /  / momentum_26: prior completed bar target 0%; next bar open simulation |
| v1 | breakout_8 | 9657.79 | -342.21 | buy /  / breakout_8: prior completed bar target 100%; next bar open simulation |
| v1 | reversion_12 | 9634.15 | -365.85 | sell /  / reversion_12: prior completed bar target 0%; next bar open simulation |
| v1 | volume_26 | 9761.42 | -238.58 | sell /  / volume_26: prior completed bar target 0%; next bar open simulation |
| v1 | trend_8_26 AND momentum_26 | 9811.64 | -188.36 | sell /  / trend_8_26 AND momentum_26: prior completed bar target 0%; next bar open simulation |
| v1 | trend_8_26 + momentum_26 | 9796.64 | -203.36 | sell /  / trend_8_26 + momentum_26: prior completed bar target 0%; next bar open simulation |
| v1 | trend_8_26 AND breakout_8 | 9854.29 | -145.71 | sell /  / trend_8_26 AND breakout_8: prior completed bar target 0%; next bar open simulation |
| v1 | trend_8_26 + breakout_8 | 9724.63 | -275.37 | buy /  / trend_8_26 + breakout_8: prior completed bar target 50%; next bar open simulation |
| v1 | trend_8_26 AND reversion_12 | 9798.51 | -201.49 | sell /  / trend_8_26 AND reversion_12: prior completed bar target 0%; next bar open simulation |
| v1 | trend_8_26 + reversion_12 | 9751.83 | -248.17 | sell /  / trend_8_26 + reversion_12: prior completed bar target 0%; next bar open simulation |
| v1 | trend_8_26 AND volume_26 | 9837.96 | -162.04 | sell /  / trend_8_26 AND volume_26: prior completed bar target 0%; next bar open simulation |
| v1 | trend_8_26 + volume_26 | 9776.88 | -223.12 | sell /  / trend_8_26 + volume_26: prior completed bar target 0%; next bar open simulation |
| v1 | momentum_26 AND breakout_8 | 9816.19 | -183.81 | sell /  / momentum_26 AND breakout_8: prior completed bar target 0%; next bar open simulation |
| v1 | momentum_26 + breakout_8 | 9788.04 | -211.96 | buy /  / momentum_26 + breakout_8: prior completed bar target 50%; next bar open simulation |
| v1 | momentum_26 AND reversion_12 | 9935.88 | -64.12 | sell /  / momentum_26 AND reversion_12: prior completed bar target 0%; next bar open simulation |
| v1 | momentum_26 + reversion_12 | 9815.11 | -184.89 | sell /  / momentum_26 + reversion_12: prior completed bar target 0%; next bar open simulation |
| v1 | momentum_26 AND volume_26 | 9905.94 | -94.06 | sell /  / momentum_26 AND volume_26: prior completed bar target 0%; next bar open simulation |
| v1 | momentum_26 + volume_26 | 9820.75 | -179.25 | sell /  / momentum_26 + volume_26: prior completed bar target 0%; next bar open simulation |
| v1 | breakout_8 AND reversion_12 | 10000.00 | 0.00 | 대기 /  / 새 신호 대기 |
| v1 | breakout_8 + reversion_12 | 9684.52 | -315.48 | buy /  / breakout_8 + reversion_12: prior completed bar target 50%; next bar open simulation |
| v1 | breakout_8 AND volume_26 | 9850.09 | -149.91 | sell /  / breakout_8 AND volume_26: prior completed bar target 0%; next bar open simulation |
| v1 | breakout_8 + volume_26 | 9709.50 | -290.50 | buy /  / breakout_8 + volume_26: prior completed bar target 50%; next bar open simulation |
| v1 | reversion_12 AND volume_26 | 9911.53 | -88.47 | sell /  / reversion_12 AND volume_26: prior completed bar target 0%; next bar open simulation |
| v1 | reversion_12 + volume_26 | 9736.41 | -263.59 | sell /  / reversion_12 + volume_26: prior completed bar target 0%; next bar open simulation |
| v1 | ema_12_26 | 9906.58 | -93.42 | sell /  / EMA12 > EMA26; 조건 미충족; EMA12=118.808, EMA26=118.852 |
| v1 | macd_12_26_9 | 9985.46 | -14.54 | sell /  / MACD > 신호선 그리고 MACD > 0; 조건 미충족; MACD=0.122825, signal9=0.127837 |
| v1 | rsi_14_recovery | 9973.19 | -26.81 | sell /  / 직전 RSI14 < 30, 현재 RSI14 >= 30 (한 봉 목표); 조건 미충족; RSI14=46.7246, previous_RSI14=43.1348 |
| v1 | bollinger_20_reentry | 9874.49 | -125.51 | sell /  / 직전 종가 < 직전 하단밴드, 현재 하단밴드 <= 종가 <= SMA20 (한 봉 목표); 조건 미충족; close=117.94, lower20=117.359, SMA20=117.989, previous_lower20=117.365 |
| v1 | donchian_20 | 9935.97 | -64.03 | sell /  / 종가 > 현재 봉을 제외한 직전 20봉 최고가; 조건 미충족; close=119.52, prior_high20=120.5 |
| v1 | atr_14_breakout | 9915.82 | -84.18 | sell /  / 종가 > 직전 종가 + 직전 ATR14 그리고 종가 > EMA26; 조건 미충족; close=119.52, threshold=120.186, prior_ATR14=0.395874, EMA26=118.952 |
| v1 | session_vwap | 9750.28 | -249.72 | buy /  / 종가 > 뉴욕 거래일별 누적 전형가격 VWAP; 조건 충족; close=117.788, session_VWAP=117.467, session_volume=3.21959e+06 |
| v1 | obv_20 | 9857.61 | -142.39 | sell /  / OBV > OBV의 SMA20 그리고 종가 > EMA26; 조건 미충족; OBV=1.5985e+07, OBV_SMA20=1.72435e+07, close=118.945, EMA26=118.951 |
| v1 | stochastic_14_3_recovery | 9535.67 | -464.33 | sell /  / 직전 %K14 < 20에서 %K14가 %D3 상향 돌파 (한 봉 목표); 조건 미충족; K14=41.7922, D3=26.634, previous_K14=28.1734, previous_D3=21.2618 |
| v1 | mfi_14_recovery | 9868.10 | -131.90 | sell /  / 직전 MFI14 < 20, 현재 MFI14 >= 20 (한 봉 목표); 조건 미충족; MFI14=23.7816, previous_MFI14=20.1936 |
| v1 | adx_14_trend | 9991.69 | -8.31 | sell /  / Wilder ADX14 >= 25 그리고 +DI14 > -DI14; 조건 미충족; ADX14=24.5142, plus_DI14=24.7537, minus_DI14=21.6519 |
| v1 | aroon_25_trend | 9947.63 | -52.37 | sell /  / Aroon25 Up > 70 그리고 Down < 30 (동률이면 최신 극값); 조건 미충족; Aroon_up=68, Aroon_down=4 |
| v1 | cci_20_momentum | 9772.81 | -227.19 | sell /  / CCI20 > 100 (전형가격·평균절대편차); 조건 미충족; CCI20=38.8365 |
| v1 | williams_14_recovery | 9640.68 | -359.32 | sell /  / 직전 Williams %R14 < -80, 현재 >= -80 (한 봉 목표); 조건 미충족; Williams_R14=-58.2078, previous_R14=-71.8266 |
| v1 | cmf_20_accumulation | 9797.30 | -202.70 | buy /  / Chaikin Money Flow20 > 0.1; 조건 충족; CMF20=0.126029, volume20=1.02737e+07 |
| v1 | chaikin_3_10 | 9731.91 | -268.09 | buy /  / ADL의 EMA3 - EMA10 > 0 그리고 종가 > EMA26; 조건 충족; Chaikin3_10=184566, ADL=1.04783e+07, close=118.09, EMA26=118.047 |
| v1 | roc_10_momentum | 10000.00 | 0.00 | 대기 /  / 새 신호 대기 |
| v1 | trix_15_trend | 9708.65 | -291.35 | sell /  / 15봉 삼중 EMA의 1봉 변화율 TRIX > 0 그리고 종가 > EMA26; 조건 미충족; TRIX15_percent=0.0142754, close=118.77, EMA26=118.947 |
| v1 | keltner_20_breakout | 9935.97 | -64.03 | sell /  / 종가 > EMA20 + 2 x Wilder ATR14; 조건 미충족; close=119.52, upper_Keltner=119.83, EMA20=119.013, ATR14=0.408312 |
| v1 | opening_range_30m | 9853.09 | -146.91 | buy /  / 뉴욕 09:30·09:45 두 완료 봉 최고가를 10:00 이후 종가가 돌파; 조건 충족; close=118.09, opening_high=117.96 |
| v2 | cash | 10000.00 | 0.00 | 대기 /  / 새 신호 대기 |
| v2 | buy_hold | 10556.30 | 556.30 | buy / partial / 직전 완료 봉 목표 비중 100%; 다음 봉 시가 가정 |
| v2 | trend_8_26 | 10187.81 | 187.81 | sell / filled / 직전 완료 봉 목표 비중 0%; 다음 봉 시가 가정 |
| v2 | momentum_26 | 10200.51 | 200.51 | sell / filled / 직전 완료 봉 목표 비중 0%; 다음 봉 시가 가정 |
| v2 | breakout_8 | 9609.22 | -390.78 | buy / partial / 직전 완료 봉 목표 비중 100%; 다음 봉 시가 가정 |
| v2 | reversion_12 | 9527.83 | -472.17 | sell / filled / 직전 완료 봉 목표 비중 0%; 다음 봉 시가 가정 |
| v2 | volume_26 | 9715.86 | -284.14 | sell / filled / 직전 완료 봉 목표 비중 0%; 다음 봉 시가 가정 |
| v2 | trend_8_26 AND momentum_26 | 10206.36 | 206.36 | sell / filled / 직전 완료 봉 목표 비중 0%; 다음 봉 시가 가정 |
| v2 | trend_8_26 + momentum_26 | 10194.13 | 194.13 | sell / filled / 직전 완료 봉 목표 비중 0%; 다음 봉 시가 가정 |
| v2 | trend_8_26 AND breakout_8 | 9935.59 | -64.41 | sell / filled / 직전 완료 봉 목표 비중 0%; 다음 봉 시가 가정 |
| v2 | trend_8_26 + breakout_8 | 9894.71 | -105.29 | buy / filled / 직전 완료 봉 목표 비중 50%; 다음 봉 시가 가정 |
| v2 | trend_8_26 AND reversion_12 | 9603.42 | -396.58 | sell / filled / 직전 완료 봉 목표 비중 0%; 다음 봉 시가 가정 |
| v2 | trend_8_26 + reversion_12 | 9895.37 | -104.63 | sell / filled / 직전 완료 봉 목표 비중 0%; 다음 봉 시가 가정 |
| v2 | trend_8_26 AND volume_26 | 9784.10 | -215.90 | sell / filled / 직전 완료 봉 목표 비중 0%; 다음 봉 시가 가정 |
| v2 | trend_8_26 + volume_26 | 9950.71 | -49.29 | sell / filled / 직전 완료 봉 목표 비중 0%; 다음 봉 시가 가정 |
| v2 | momentum_26 AND breakout_8 | 9773.67 | -226.33 | sell / filled / 직전 완료 봉 목표 비중 0%; 다음 봉 시가 가정 |
| v2 | momentum_26 + breakout_8 | 9963.58 | -36.42 | buy / filled / 직전 완료 봉 목표 비중 50%; 다음 봉 시가 가정 |
| v2 | momentum_26 AND reversion_12 | 9759.91 | -240.09 | sell / filled / 직전 완료 봉 목표 비중 0%; 다음 봉 시가 가정 |
| v2 | momentum_26 + reversion_12 | 10005.93 | 5.93 | sell / filled / 직전 완료 봉 목표 비중 0%; 다음 봉 시가 가정 |
| v2 | momentum_26 AND volume_26 | 9814.68 | -185.32 | sell / filled / 직전 완료 봉 목표 비중 0%; 다음 봉 시가 가정 |
| v2 | momentum_26 + volume_26 | 9998.77 | -1.23 | sell / filled / 직전 완료 봉 목표 비중 0%; 다음 봉 시가 가정 |
| v2 | breakout_8 AND reversion_12 | 10000.00 | 0.00 | 대기 /  / 새 신호 대기 |
| v2 | breakout_8 + reversion_12 | 9629.90 | -370.10 | buy / filled / 직전 완료 봉 목표 비중 50%; 다음 봉 시가 가정 |
| v2 | breakout_8 AND volume_26 | 9795.19 | -204.81 | sell / filled / 직전 완료 봉 목표 비중 0%; 다음 봉 시가 가정 |
| v2 | breakout_8 + volume_26 | 9663.76 | -336.24 | buy / filled / 직전 완료 봉 목표 비중 50%; 다음 봉 시가 가정 |
| v2 | reversion_12 AND volume_26 | 9917.25 | -82.75 | sell / filled / 직전 완료 봉 목표 비중 0%; 다음 봉 시가 가정 |
| v2 | reversion_12 + volume_26 | 9661.72 | -338.28 | sell / filled / 직전 완료 봉 목표 비중 0%; 다음 봉 시가 가정 |
| v2 | ema_12_26 | 9902.61 | -97.39 | sell / filled / EMA12 > EMA26; 조건 미충족; EMA12=118.808, EMA26=118.852; 직전 완료 봉 목표를 다음 봉 시가에 모의 적용 |
| v2 | macd_12_26_9 | 9981.46 | -18.54 | sell / filled / MACD > 신호선 그리고 MACD > 0; 조건 미충족; MACD=0.122825, signal9=0.127837; 직전 완료 봉 목표를 다음 봉 시가에 모의 적용 |
| v2 | rsi_14_recovery | 9971.19 | -28.81 | sell / filled / 직전 RSI14 < 30, 현재 RSI14 >= 30 (한 봉 목표); 조건 미충족; RSI14=46.7246, previous_RSI14=43.1348; 직전 완료 봉 목표를 다음 봉 시가에 모의 적용 |
| v2 | bollinger_20_reentry | 9868.57 | -131.43 | sell / filled / 직전 종가 < 직전 하단밴드, 현재 하단밴드 <= 종가 <= SMA20 (한 봉 목표); 조건 미충족; close=117.94, lower20=117.359, SMA20=117.989, previous_lower20=117.365; 직전 완료 봉 목표를 다음 봉 시가에 모의 적용 |
| v2 | donchian_20 | 9933.99 | -66.01 | sell / filled / 종가 > 현재 봉을 제외한 직전 20봉 최고가; 조건 미충족; close=119.52, prior_high20=120.5; 직전 완료 봉 목표를 다음 봉 시가에 모의 적용 |
| v2 | atr_14_breakout | 9911.85 | -88.15 | sell / filled / 종가 > 직전 종가 + 직전 ATR14 그리고 종가 > EMA26; 조건 미충족; close=119.52, threshold=120.186, prior_ATR14=0.395874, EMA26=118.952; 직전 완료 봉 목표를 다음 봉 시가에 모의 적용 |
| v2 | session_vwap | 9735.67 | -264.33 | buy / partial / 종가 > 뉴욕 거래일별 누적 전형가격 VWAP; 조건 충족; close=117.788, session_VWAP=117.467, session_volume=3.21959e+06; 직전 완료 봉 목표를 다음 봉 시가에 모의 적용 |
| v2 | obv_20 | 9847.76 | -152.24 | sell / filled / OBV > OBV의 SMA20 그리고 종가 > EMA26; 조건 미충족; OBV=1.6238e+07, OBV_SMA20=1.74966e+07, close=118.945, EMA26=118.951; 직전 완료 봉 목표를 다음 봉 시가에 모의 적용 |
| v2 | stochastic_14_3_recovery | 9667.84 | -332.16 | 중단: 손실 한도 / buy / partial / 직전 %K14 < 20에서 %K14가 %D3 상향 돌파 (한 봉 목표); 조건 충족; K14=25.6758, D3=22.4971, previous_K14=12.8379, previous_D3=25.8704; 직전 완료 봉 목표를 다음 봉 시가에 모의 적용 |
| v2 | mfi_14_recovery | 9862.18 | -137.82 | sell / filled / 직전 MFI14 < 20, 현재 MFI14 >= 20 (한 봉 목표); 조건 미충족; MFI14=23.7816, previous_MFI14=20.1936; 직전 완료 봉 목표를 다음 봉 시가에 모의 적용 |
| v2 | adx_14_trend | 9989.70 | -10.30 | sell / filled / Wilder ADX14 >= 25 그리고 +DI14 > -DI14; 조건 미충족; ADX14=24.5142, plus_DI14=24.7537, minus_DI14=21.6519; 직전 완료 봉 목표를 다음 봉 시가에 모의 적용 |
| v2 | aroon_25_trend | 9943.65 | -56.35 | sell / filled / Aroon25 Up > 70 그리고 Down < 30 (동률이면 최신 극값); 조건 미충족; Aroon_up=68, Aroon_down=4; 직전 완료 봉 목표를 다음 봉 시가에 모의 적용 |
| v2 | cci_20_momentum | 9766.95 | -233.05 | sell / filled / CCI20 > 100 (전형가격·평균절대편차); 조건 미충족; CCI20=38.8365; 직전 완료 봉 목표를 다음 봉 시가에 모의 적용 |
| v2 | williams_14_recovery | 9629.12 | -370.88 | sell / filled / 직전 Williams %R14 < -80, 현재 >= -80 (한 봉 목표); 조건 미충족; Williams_R14=-58.2078, previous_R14=-71.8266; 직전 완료 봉 목표를 다음 봉 시가에 모의 적용 |
| v2 | cmf_20_accumulation | 9786.53 | -213.47 | buy / partial / Chaikin Money Flow20 > 0.1; 조건 충족; CMF20=0.126029, volume20=1.02737e+07; 직전 완료 봉 목표를 다음 봉 시가에 모의 적용 |
| v2 | chaikin_3_10 | 9717.33 | -282.67 | buy / partial / ADL의 EMA3 - EMA10 > 0 그리고 종가 > EMA26; 조건 충족; Chaikin3_10=184566, ADL=1.04783e+07, close=118.09, EMA26=118.047; 직전 완료 봉 목표를 다음 봉 시가에 모의 적용 |
| v2 | roc_10_momentum | 10000.00 | 0.00 | 대기 /  / 새 신호 대기 |
| v2 | trix_15_trend | 9697.01 | -302.99 | sell / filled / 15봉 삼중 EMA의 1봉 변화율 TRIX > 0 그리고 종가 > EMA26; 조건 미충족; TRIX15_percent=0.0142754, close=118.77, EMA26=118.947; 직전 완료 봉 목표를 다음 봉 시가에 모의 적용 |
| v2 | keltner_20_breakout | 9933.99 | -66.01 | sell / filled / 종가 > EMA20 + 2 x Wilder ATR14; 조건 미충족; close=119.52, upper_Keltner=119.83, EMA20=119.013, ATR14=0.408312; 직전 완료 봉 목표를 다음 봉 시가에 모의 적용 |
| v2 | opening_range_30m | 9848.16 | -151.84 | buy / partial / 뉴욕 09:30·09:45 두 완료 봉 최고가를 10:00 이후 종가가 돌파; 조건 충족; close=118.09, opening_high=117.96; 직전 완료 봉 목표를 다음 봉 시가에 모의 적용 |

### 같은 기간의 비용·노출 비교 (사후 연구)

| 전략 | 비용 전 | 비용 후 | 100% 보유 | 같은 평균 노출 보유 | 평균 노출 |
|---|---:|---:|---:|---:|---:|
| cash | 0.00% | 0.00% | 12.25% | 0.00% | 0.00% |
| buy_hold | 12.72% | 12.25% | 12.25% | 12.25% | 100.00% |
| trend_8_26 | 8.93% | 5.77% | 12.25% | 8.14% | 67.89% |
| momentum_26 | 10.44% | 5.02% | 12.25% | 8.41% | 70.00% |
| breakout_8 | 5.98% | -10.79% | 12.25% | 3.01% | 25.79% |
| reversion_12 | 4.53% | -7.07% | 12.25% | 2.02% | 17.37% |
| volume_26 | 1.03% | -5.14% | 12.25% | 0.67% | 5.79% |
| trend_8_26 AND momentum_26 | 8.65% | 4.18% | 12.25% | 7.49% | 62.63% |
| trend_8_26 + momentum_26 | 9.69% | 5.39% | 12.25% | 8.28% | 68.95% |
| trend_8_26 AND breakout_8 | 6.59% | -6.43% | 12.25% | 2.45% | 21.05% |
| trend_8_26 + breakout_8 | 7.46% | -2.85% | 12.25% | 5.54% | 46.85% |
| trend_8_26 AND reversion_12 | 0.33% | -5.40% | 12.25% | 0.73% | 6.32% |
| trend_8_26 + reversion_12 | 6.75% | -0.22% | 12.25% | 5.03% | 42.64% |
| trend_8_26 AND volume_26 | 0.24% | -2.26% | 12.25% | 0.24% | 2.11% |
| trend_8_26 + volume_26 | 4.94% | 0.60% | 12.25% | 4.33% | 36.84% |
| momentum_26 AND breakout_8 | 6.62% | -7.18% | 12.25% | 2.67% | 22.89% |
| momentum_26 + breakout_8 | 8.20% | -2.38% | 12.25% | 5.67% | 47.90% |
| momentum_26 AND reversion_12 | 1.65% | -4.16% | 12.25% | 0.85% | 7.37% |
| momentum_26 + reversion_12 | 7.49% | 1.32% | 12.25% | 5.16% | 43.69% |
| momentum_26 AND volume_26 | 1.64% | -2.54% | 12.25% | 0.33% | 2.89% |
| momentum_26 + volume_26 | 5.67% | 0.24% | 12.25% | 4.46% | 37.90% |
| breakout_8 AND reversion_12 | 0.00% | 0.00% | 12.25% | 0.00% | 0.00% |
| breakout_8 + reversion_12 | 5.28% | -8.17% | 12.25% | 2.51% | 21.59% |
| breakout_8 AND volume_26 | 0.78% | -2.14% | 12.25% | 0.24% | 2.11% |
| breakout_8 + volume_26 | 3.50% | -7.80% | 12.25% | 1.83% | 15.80% |
| reversion_12 AND volume_26 | -0.59% | -3.47% | 12.25% | 0.27% | 2.37% |
| reversion_12 + volume_26 | 2.77% | -5.52% | 12.25% | 1.34% | 11.58% |
| ema_12_26 | 11.20% | 9.81% | 12.25% | 8.77% | 72.89% |
| macd_12_26_9 | 8.67% | 4.64% | 12.25% | 4.27% | 36.32% |
| rsi_14_recovery | -0.12% | -1.78% | 12.25% | 0.12% | 1.05% |
| bollinger_20_reentry | 1.28% | -2.07% | 12.25% | 0.24% | 2.11% |
| donchian_20 | 4.55% | -7.44% | 12.25% | 1.49% | 12.89% |
| atr_14_breakout | -0.90% | -10.40% | 12.25% | 0.85% | 7.37% |
| session_vwap | 9.64% | -0.87% | 12.25% | 7.03% | 58.95% |
| obv_20 | 10.62% | 3.00% | 12.25% | 6.67% | 56.05% |
| stochastic_14_3_recovery | 0.89% | -8.02% | 12.25% | 0.67% | 5.79% |
| mfi_14_recovery | -0.10% | -2.18% | 12.25% | 0.15% | 1.32% |
| adx_14_trend | 8.73% | 6.47% | 12.25% | 5.93% | 50.00% |
| aroon_25_trend | 7.01% | 2.18% | 12.25% | 3.67% | 31.32% |
| cci_20_momentum | 6.31% | -1.85% | 12.25% | 3.70% | 31.58% |
| williams_14_recovery | -0.84% | -9.59% | 12.25% | 0.67% | 5.79% |
| cmf_20_accumulation | 9.46% | 0.22% | 12.25% | 4.46% | 37.89% |
| chaikin_3_10 | 9.72% | 0.88% | 12.25% | 6.15% | 51.84% |
| roc_10_momentum | -0.29% | -4.79% | 12.25% | 1.61% | 13.95% |
| trix_15_trend | 10.97% | 6.86% | 12.25% | 7.78% | 65.00% |
| keltner_20_breakout | 6.59% | 0.08% | 12.25% | 3.10% | 26.58% |
| opening_range_30m | 9.59% | 3.76% | 12.25% | 4.39% | 37.37% |

동일 구간·초기 자금, 종료 시 청산 비용 포함. 노출 맞춤은 사후 설명용이며 v2 실제 계좌 성과가 아닙니다.
[낙폭 분해·비용 영향·전체 구간](WMT/comparison.json)

[v1 전체 기록](WMT/accounts.json) · [v2 전체 기록](WMT/accounts-v2.json)
