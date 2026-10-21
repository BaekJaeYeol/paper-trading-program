# 모의투자 운영 현황

[PC·서버 장애 진단과 복구 방법](https://github.com/BaekJaeYeol/paper-trading-program/blob/main/investment-lab/docs/failure-recovery.md)

이번 실행 복구: {}

완료 봉 확인 주기: 기록 15/24회 · 기록 없는 예정 9회 · 아직 판정 전 2회 · 주의: 예약 시작 지연 또는 실행·저장 누락을 확인하세요.

[주기 판정 기준](https://github.com/BaekJaeYeol/paper-trading-program/blob/main/investment-lab/docs/session-coverage.md)

최근 확인: 2026-10-21T19:52:00.591528+00:00 (UTC)
다음 15분 확인 목표 (세션 실행 중에만 적용): 2026-10-21T20:07:00+00:00 (UTC, 실행 지연 가능)

실제 주문 없음. v1 기존 계좌와 v2 새 계좌의 시작일이 다르므로 수익률을 직접 우열 비교하지 마세요.
v2는 다음 봉 시가에 비용·스프레드·직전 거래량 제한을 적용한 가상 체결입니다. 미체결 잔량은 만료됩니다.

| 종목 | 상태 | 최근 성공 UTC | 마지막 완료 봉 UTC | 이번 새 봉 |
|---|---|---|---|---|
| SPY | updated | 2026-10-21T19:52:00.591528+00:00 | 2026-10-21T19:30:00+00:00 | 1 |
| QQQ | updated | 2026-10-21T19:52:00.591528+00:00 | 2026-10-21T19:30:00+00:00 | 1 |
| IWM | updated | 2026-10-21T19:52:00.591528+00:00 | 2026-10-21T19:30:00+00:00 | 1 |
| DIA | updated | 2026-10-21T19:52:00.591528+00:00 | 2026-10-21T19:30:00+00:00 | 1 |
| MSFT | updated | 2026-10-21T19:52:00.591528+00:00 | 2026-10-21T19:30:00+00:00 | 1 |
| JPM | updated | 2026-10-21T19:52:00.591528+00:00 | 2026-10-21T19:30:00+00:00 | 1 |
| XOM | updated | 2026-10-21T19:52:00.591528+00:00 | 2026-10-21T19:30:00+00:00 | 1 |
| JNJ | updated | 2026-10-21T19:52:00.591528+00:00 | 2026-10-21T19:30:00+00:00 | 1 |
| CAT | updated | 2026-10-21T19:52:00.591528+00:00 | 2026-10-21T19:30:00+00:00 | 1 |
| WMT | updated | 2026-10-21T19:52:00.591528+00:00 | 2026-10-21T19:30:00+00:00 | 1 |

이번 실행 소요: 29.08초
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
| v1 | buy_hold | 9977.84 | -22.16 | buy /  / buy_hold: prior completed bar target 100%; next bar open simulation |
| v1 | trend_8_26 | 9806.14 | -193.86 | buy /  / trend_8_26: prior completed bar target 100%; next bar open simulation |
| v1 | momentum_26 | 9732.02 | -267.98 | buy /  / momentum_26: prior completed bar target 100%; next bar open simulation |
| v1 | breakout_8 | 9568.88 | -431.12 | sell /  / breakout_8: prior completed bar target 0%; next bar open simulation |
| v1 | reversion_12 | 9698.26 | -301.74 | sell /  / reversion_12: prior completed bar target 0%; next bar open simulation |
| v1 | volume_26 | 9560.36 | -439.64 | sell /  / volume_26: prior completed bar target 0%; next bar open simulation |
| v1 | trend_8_26 AND momentum_26 | 9724.69 | -275.31 | buy /  / trend_8_26 AND momentum_26: prior completed bar target 100%; next bar open simulation |
| v1 | trend_8_26 + momentum_26 | 9769.00 | -231.00 | buy /  / trend_8_26 + momentum_26: prior completed bar target 100%; next bar open simulation |
| v1 | trend_8_26 AND breakout_8 | 9730.71 | -269.29 | sell /  / trend_8_26 AND breakout_8: prior completed bar target 0%; next bar open simulation |
| v1 | trend_8_26 + breakout_8 | 9725.52 | -274.48 | sell /  / trend_8_26 + breakout_8: prior completed bar target 50%; next bar open simulation |
| v1 | trend_8_26 AND reversion_12 | 9769.01 | -230.99 | sell /  / trend_8_26 AND reversion_12: prior completed bar target 0%; next bar open simulation |
| v1 | trend_8_26 + reversion_12 | 9751.88 | -248.12 | sell /  / trend_8_26 + reversion_12: prior completed bar target 50%; next bar open simulation |
| v1 | trend_8_26 AND volume_26 | 9605.36 | -394.64 | sell /  / trend_8_26 AND volume_26: prior completed bar target 0%; next bar open simulation |
| v1 | trend_8_26 + volume_26 | 9682.37 | -317.63 | sell /  / trend_8_26 + volume_26: prior completed bar target 50%; next bar open simulation |
| v1 | momentum_26 AND breakout_8 | 9640.01 | -359.99 | sell /  / momentum_26 AND breakout_8: prior completed bar target 0%; next bar open simulation |
| v1 | momentum_26 + breakout_8 | 9650.11 | -349.89 | sell /  / momentum_26 + breakout_8: prior completed bar target 50%; next bar open simulation |
| v1 | momentum_26 AND reversion_12 | 9769.70 | -230.30 | sell /  / momentum_26 AND reversion_12: prior completed bar target 0%; next bar open simulation |
| v1 | momentum_26 + reversion_12 | 9753.95 | -246.05 | sell /  / momentum_26 + reversion_12: prior completed bar target 50%; next bar open simulation |
| v1 | momentum_26 AND volume_26 | 9618.73 | -381.27 | sell /  / momentum_26 AND volume_26: prior completed bar target 0%; next bar open simulation |
| v1 | momentum_26 + volume_26 | 9645.71 | -354.29 | sell /  / momentum_26 + volume_26: prior completed bar target 50%; next bar open simulation |
| v1 | breakout_8 AND reversion_12 | 10000.00 | 0.00 | 대기 /  / 새 신호 대기 |
| v1 | breakout_8 + reversion_12 | 9633.04 | -366.96 | sell /  / breakout_8 + reversion_12: prior completed bar target 0%; next bar open simulation |
| v1 | breakout_8 AND volume_26 | 9837.59 | -162.41 | sell /  / breakout_8 AND volume_26: prior completed bar target 0%; next bar open simulation |
| v1 | breakout_8 + volume_26 | 9602.74 | -397.26 | sell /  / breakout_8 + volume_26: prior completed bar target 0%; next bar open simulation |
| v1 | reversion_12 AND volume_26 | 9861.02 | -138.98 | sell /  / reversion_12 AND volume_26: prior completed bar target 0%; next bar open simulation |
| v1 | reversion_12 + volume_26 | 9628.87 | -371.13 | sell /  / reversion_12 + volume_26: prior completed bar target 0%; next bar open simulation |
| v1 | ema_12_26 | 9837.87 | -162.13 | buy /  / EMA12 > EMA26; 조건 충족; EMA12=767.528, EMA26=767.458 |
| v1 | macd_12_26_9 | 9769.55 | -230.45 | sell /  / MACD > 신호선 그리고 MACD > 0; 조건 미충족; MACD=1.03945, signal9=1.12358 |
| v1 | rsi_14_recovery | 9899.32 | -100.68 | sell /  / 직전 RSI14 < 30, 현재 RSI14 >= 30 (한 봉 목표); 조건 미충족; RSI14=34.3611, previous_RSI14=32.906 |
| v1 | bollinger_20_reentry | 9835.17 | -164.83 | sell /  / 직전 종가 < 직전 하단밴드, 현재 하단밴드 <= 종가 <= SMA20 (한 봉 목표); 조건 미충족; close=763.39, lower20=762.854, SMA20=768.639, previous_lower20=763.636 |
| v1 | donchian_20 | 9818.08 | -181.92 | sell /  / 종가 > 현재 봉을 제외한 직전 20봉 최고가; 조건 미충족; close=774.19, prior_high20=774.44 |
| v1 | atr_14_breakout | 9836.55 | -163.45 | buy /  / 종가 > 직전 종가 + 직전 ATR14 그리고 종가 > EMA26; 조건 충족; close=773.235, threshold=772.626, prior_ATR14=1.00554, EMA26=772.183 |
| v1 | session_vwap | 9679.92 | -320.08 | buy /  / 종가 > 뉴욕 거래일별 누적 전형가격 VWAP; 조건 충족; close=773.235, session_VWAP=772.923, session_volume=5.92416e+07 |
| v1 | obv_20 | 9698.07 | -301.93 | buy /  / OBV > OBV의 SMA20 그리고 종가 > EMA26; 조건 충족; OBV=-2.05936e+07, OBV_SMA20=-3.45629e+07, close=773.235, EMA26=772.183 |
| v1 | stochastic_14_3_recovery | 9694.64 | -305.36 | sell /  / 직전 %K14 < 20에서 %K14가 %D3 상향 돌파 (한 봉 목표); 조건 미충족; K14=53.6357, D3=31.478, previous_K14=28.6364, previous_D3=21.2782 |
| v1 | mfi_14_recovery | 9875.98 | -124.02 | sell /  / 직전 MFI14 < 20, 현재 MFI14 >= 20 (한 봉 목표); 조건 미충족; MFI14=33.0962, previous_MFI14=27.4403 |
| v1 | adx_14_trend | 9981.96 | -18.04 | sell /  / Wilder ADX14 >= 25 그리고 +DI14 > -DI14; 조건 미충족; ADX14=24.2312, plus_DI14=28.3519, minus_DI14=24.6578 |
| v1 | aroon_25_trend | 9830.16 | -169.84 | buy /  / Aroon25 Up > 70 그리고 Down < 30 (동률이면 최신 극값); 조건 충족; Aroon_up=96, Aroon_down=28 |
| v1 | cci_20_momentum | 9766.23 | -233.77 | sell /  / CCI20 > 100 (전형가격·평균절대편차); 조건 미충족; CCI20=97.3932 |
| v1 | williams_14_recovery | 9648.56 | -351.44 | sell /  / 직전 Williams %R14 < -80, 현재 >= -80 (한 봉 목표); 조건 미충족; Williams_R14=-30.1254, previous_R14=-70.5002 |
| v1 | cmf_20_accumulation | 9879.36 | -120.64 | buy /  / Chaikin Money Flow20 > 0.1; 조건 충족; CMF20=0.196699, volume20=2.80437e+07 |
| v1 | chaikin_3_10 | 9665.18 | -334.82 | buy /  / ADL의 EMA3 - EMA10 > 0 그리고 종가 > EMA26; 조건 충족; Chaikin3_10=3.34687e+06, ADL=3.20252e+07, close=773.235, EMA26=772.183 |
| v1 | roc_10_momentum | 9953.42 | -46.58 | sell /  / 10봉 ROC > 1% 그리고 종가 > EMA26; 조건 미충족; ROC10_percent=0.806376, close=769.45, EMA26=767.181 |
| v1 | trix_15_trend | 9589.01 | -410.99 | buy /  / 15봉 삼중 EMA의 1봉 변화율 TRIX > 0 그리고 종가 > EMA26; 조건 충족; TRIX15_percent=0.0197813, close=773.235, EMA26=772.183 |
| v1 | keltner_20_breakout | 9810.90 | -189.10 | sell /  / 종가 > EMA20 + 2 x Wilder ATR14; 조건 미충족; close=774.19, upper_Keltner=774.31, EMA20=772.615, ATR14=0.847257 |
| v1 | opening_range_30m | 9751.70 | -248.30 | buy /  / 뉴욕 09:30·09:45 두 완료 봉 최고가를 10:00 이후 종가가 돌파; 조건 충족; close=771.43, opening_high=771.34 |
| v2 | cash | 10000.00 | 0.00 | 대기 /  / 새 신호 대기 |
| v2 | buy_hold | 9905.87 | -94.13 | buy / partial / 직전 완료 봉 목표 비중 100%; 다음 봉 시가 가정 |
| v2 | trend_8_26 | 9686.09 | -313.91 | buy / partial / 직전 완료 봉 목표 비중 100%; 다음 봉 시가 가정 |
| v2 | momentum_26 | 9582.11 | -417.89 | buy / partial / 직전 완료 봉 목표 비중 100%; 다음 봉 시가 가정 |
| v2 | breakout_8 | 9164.60 | -835.40 | sell / filled / 직전 완료 봉 목표 비중 0%; 다음 봉 시가 가정 |
| v2 | reversion_12 | 9231.48 | -768.52 | sell / filled / 직전 완료 봉 목표 비중 0%; 다음 봉 시가 가정 |
| v2 | volume_26 | 9010.14 | -989.86 | sell / filled / 직전 완료 봉 목표 비중 0%; 다음 봉 시가 가정 |
| v2 | trend_8_26 AND momentum_26 | 9581.42 | -418.58 | buy / partial / 직전 완료 봉 목표 비중 100%; 다음 봉 시가 가정 |
| v2 | trend_8_26 + momentum_26 | 9633.95 | -366.05 | buy / partial / 직전 완료 봉 목표 비중 100%; 다음 봉 시가 가정 |
| v2 | trend_8_26 AND breakout_8 | 9547.25 | -452.75 | sell / filled / 직전 완료 봉 목표 비중 0%; 다음 봉 시가 가정 |
| v2 | trend_8_26 + breakout_8 | 9461.19 | -538.81 | sell / filled / 직전 완료 봉 목표 비중 50%; 다음 봉 시가 가정 |
| v2 | trend_8_26 AND reversion_12 | 9655.93 | -344.07 | sell / filled / 직전 완료 봉 목표 비중 0%; 다음 봉 시가 가정 |
| v2 | trend_8_26 + reversion_12 | 9455.56 | -544.44 | sell / filled / 직전 완료 봉 목표 비중 50%; 다음 봉 시가 가정 |
| v2 | trend_8_26 AND volume_26 | 9442.22 | -557.78 | sell / filled / 직전 완료 봉 목표 비중 0%; 다음 봉 시가 가정 |
| v2 | trend_8_26 + volume_26 | 9361.32 | -638.68 | sell / filled / 직전 완료 봉 목표 비중 50%; 다음 봉 시가 가정 |
| v2 | momentum_26 AND breakout_8 | 9414.38 | -585.62 | sell / filled / 직전 완료 봉 목표 비중 0%; 다음 봉 시가 가정 |
| v2 | momentum_26 + breakout_8 | 9370.96 | -629.04 | sell / filled / 직전 완료 봉 목표 비중 50%; 다음 봉 시가 가정 |
| v2 | momentum_26 AND reversion_12 | 9722.08 | -277.92 | sell / filled / 직전 완료 봉 목표 비중 0%; 다음 봉 시가 가정 |
| v2 | momentum_26 + reversion_12 | 9464.18 | -535.82 | sell / filled / 직전 완료 봉 목표 비중 50%; 다음 봉 시가 가정 |
| v2 | momentum_26 AND volume_26 | 9523.88 | -476.12 | sell / filled / 직전 완료 봉 목표 비중 0%; 다음 봉 시가 가정 |
| v2 | momentum_26 + volume_26 | 9350.09 | -649.91 | sell / filled / 직전 완료 봉 목표 비중 50%; 다음 봉 시가 가정 |
| v2 | breakout_8 AND reversion_12 | 10000.00 | 0.00 | 대기 /  / 새 신호 대기 |
| v2 | breakout_8 + reversion_12 | 9235.95 | -764.05 | sell / filled / 직전 완료 봉 목표 비중 0%; 다음 봉 시가 가정 |
| v2 | breakout_8 AND volume_26 | 9765.99 | -234.01 | sell / filled / 직전 완료 봉 목표 비중 0%; 다음 봉 시가 가정 |
| v2 | breakout_8 + volume_26 | 9163.13 | -836.87 | sell / filled / 직전 완료 봉 목표 비중 0%; 다음 봉 시가 가정 |
| v2 | reversion_12 AND volume_26 | 9602.16 | -397.84 | sell / filled / 직전 완료 봉 목표 비중 0%; 다음 봉 시가 가정 |
| v2 | reversion_12 + volume_26 | 9196.60 | -803.40 | sell / filled / 직전 완료 봉 목표 비중 0%; 다음 봉 시가 가정 |
| v2 | ema_12_26 | 9832.95 | -167.05 | buy / partial / EMA12 > EMA26; 조건 충족; EMA12=767.528, EMA26=767.458; 직전 완료 봉 목표를 다음 봉 시가에 모의 적용 |
| v2 | macd_12_26_9 | 9761.73 | -238.27 | sell / filled / MACD > 신호선 그리고 MACD > 0; 조건 미충족; MACD=1.03945, signal9=1.12358; 직전 완료 봉 목표를 다음 봉 시가에 모의 적용 |
| v2 | rsi_14_recovery | 9895.36 | -104.64 | sell / filled / 직전 RSI14 < 30, 현재 RSI14 >= 30 (한 봉 목표); 조건 미충족; RSI14=34.3611, previous_RSI14=32.906; 직전 완료 봉 목표를 다음 봉 시가에 모의 적용 |
| v2 | bollinger_20_reentry | 9829.27 | -170.73 | sell / filled / 직전 종가 < 직전 하단밴드, 현재 하단밴드 <= 종가 <= SMA20 (한 봉 목표); 조건 미충족; close=763.39, lower20=762.854, SMA20=768.639, previous_lower20=763.636; 직전 완료 봉 목표를 다음 봉 시가에 모의 적용 |
| v2 | donchian_20 | 9808.27 | -191.73 | sell / filled / 종가 > 현재 봉을 제외한 직전 20봉 최고가; 조건 미충족; close=774.19, prior_high20=774.44; 직전 완료 봉 목표를 다음 봉 시가에 모의 적용 |
| v2 | atr_14_breakout | 9827.70 | -172.30 | buy / partial / 종가 > 직전 종가 + 직전 ATR14 그리고 종가 > EMA26; 조건 충족; close=773.235, threshold=772.626, prior_ATR14=1.00554, EMA26=772.183; 직전 완료 봉 목표를 다음 봉 시가에 모의 적용 |
| v2 | session_vwap | 9665.41 | -334.59 | buy / partial / 종가 > 뉴욕 거래일별 누적 전형가격 VWAP; 조건 충족; close=773.235, session_VWAP=772.923, session_volume=5.92416e+07; 직전 완료 봉 목표를 다음 봉 시가에 모의 적용 |
| v2 | obv_20 | 9685.47 | -314.53 | buy / partial / OBV > OBV의 SMA20 그리고 종가 > EMA26; 조건 충족; OBV=-2.05936e+07, OBV_SMA20=-3.45629e+07, close=773.235, EMA26=772.183; 직전 완료 봉 목표를 다음 봉 시가에 모의 적용 |
| v2 | stochastic_14_3_recovery | 9677.21 | -322.79 | sell / filled / 직전 %K14 < 20에서 %K14가 %D3 상향 돌파 (한 봉 목표); 조건 미충족; K14=53.6357, D3=31.478, previous_K14=28.6364, previous_D3=21.2782; 직전 완료 봉 목표를 다음 봉 시가에 모의 적용 |
| v2 | mfi_14_recovery | 9870.05 | -129.95 | sell / filled / 직전 MFI14 < 20, 현재 MFI14 >= 20 (한 봉 목표); 조건 미충족; MFI14=33.0962, previous_MFI14=27.4403; 직전 완료 봉 목표를 다음 봉 시가에 모의 적용 |
| v2 | adx_14_trend | 9979.97 | -20.03 | sell / filled / Wilder ADX14 >= 25 그리고 +DI14 > -DI14; 조건 미충족; ADX14=24.2312, plus_DI14=28.3519, minus_DI14=24.6578; 직전 완료 봉 목표를 다음 봉 시가에 모의 적용 |
| v2 | aroon_25_trend | 9825.25 | -174.75 | buy / partial / Aroon25 Up > 70 그리고 Down < 30 (동률이면 최신 극값); 조건 충족; Aroon_up=96, Aroon_down=28; 직전 완료 봉 목표를 다음 봉 시가에 모의 적용 |
| v2 | cci_20_momentum | 9754.52 | -245.48 | sell / filled / CCI20 > 100 (전형가격·평균절대편차); 조건 미충족; CCI20=97.3932; 직전 완료 봉 목표를 다음 봉 시가에 모의 적용 |
| v2 | williams_14_recovery | 9629.28 | -370.72 | sell / filled / 직전 Williams %R14 < -80, 현재 >= -80 (한 봉 목표); 조건 미충족; Williams_R14=-30.1254, previous_R14=-70.5002; 직전 완료 봉 목표를 다음 봉 시가에 모의 적용 |
| v2 | cmf_20_accumulation | 9872.45 | -127.55 | buy / partial / Chaikin Money Flow20 > 0.1; 조건 충족; CMF20=0.196699, volume20=2.80437e+07; 직전 완료 봉 목표를 다음 봉 시가에 모의 적용 |
| v2 | chaikin_3_10 | 9650.69 | -349.31 | buy / partial / ADL의 EMA3 - EMA10 > 0 그리고 종가 > EMA26; 조건 충족; Chaikin3_10=3.34687e+06, ADL=3.20252e+07, close=773.235, EMA26=772.183; 직전 완료 봉 목표를 다음 봉 시가에 모의 적용 |
| v2 | roc_10_momentum | 9951.43 | -48.57 | sell / filled / 10봉 ROC > 1% 그리고 종가 > EMA26; 조건 미충족; ROC10_percent=0.806376, close=769.45, EMA26=767.181; 직전 완료 봉 목표를 다음 봉 시가에 모의 적용 |
| v2 | trix_15_trend | 9572.72 | -427.28 | buy / partial / 15봉 삼중 EMA의 1봉 변화율 TRIX > 0 그리고 종가 > EMA26; 조건 충족; TRIX15_percent=0.0197813, close=773.235, EMA26=772.183; 직전 완료 봉 목표를 다음 봉 시가에 모의 적용 |
| v2 | keltner_20_breakout | 9803.05 | -196.95 | sell / filled / 종가 > EMA20 + 2 x Wilder ATR14; 조건 미충족; close=774.19, upper_Keltner=774.31, EMA20=772.615, ATR14=0.847257; 직전 완료 봉 목표를 다음 봉 시가에 모의 적용 |
| v2 | opening_range_30m | 9740.98 | -259.02 | buy / partial / 뉴욕 09:30·09:45 두 완료 봉 최고가를 10:00 이후 종가가 돌파; 조건 충족; close=771.43, opening_high=771.34; 직전 완료 봉 목표를 다음 봉 시가에 모의 적용 |

### 같은 기간의 비용·노출 비교 (사후 연구)

| 전략 | 비용 전 | 비용 후 | 100% 보유 | 같은 평균 노출 보유 | 평균 노출 |
|---|---:|---:|---:|---:|---:|
| cash | 0.00% | 0.00% | 1.24% | 0.00% | 0.00% |
| buy_hold | 1.66% | 1.24% | 1.24% | 1.24% | 100.00% |
| trend_8_26 | 1.14% | -2.61% | 1.24% | 0.68% | 55.61% |
| momentum_26 | -0.29% | -4.79% | 1.24% | 0.68% | 54.83% |
| breakout_8 | -0.25% | -16.73% | 1.24% | 0.30% | 24.80% |
| reversion_12 | -0.36% | -11.04% | 1.24% | 0.30% | 24.54% |
| volume_26 | -1.31% | -10.02% | 1.24% | 0.11% | 8.88% |
| trend_8_26 AND momentum_26 | 0.32% | -4.21% | 1.24% | 0.59% | 47.78% |
| trend_8_26 + momentum_26 | 0.43% | -3.71% | 1.24% | 0.68% | 55.22% |
| trend_8_26 AND breakout_8 | 0.13% | -11.35% | 1.24% | 0.19% | 15.67% |
| trend_8_26 + breakout_8 | 0.45% | -9.57% | 1.24% | 0.49% | 40.22% |
| trend_8_26 AND reversion_12 | 0.15% | -4.38% | 1.24% | 0.08% | 6.27% |
| trend_8_26 + reversion_12 | 0.39% | -6.73% | 1.24% | 0.49% | 40.08% |
| trend_8_26 AND volume_26 | -1.05% | -6.30% | 1.24% | 0.07% | 5.48% |
| trend_8_26 + volume_26 | -0.09% | -6.39% | 1.24% | 0.40% | 32.25% |
| momentum_26 AND breakout_8 | 0.30% | -11.95% | 1.24% | 0.21% | 17.23% |
| momentum_26 + breakout_8 | -0.27% | -10.96% | 1.24% | 0.49% | 39.82% |
| momentum_26 AND reversion_12 | -0.39% | -5.28% | 1.24% | 0.08% | 6.27% |
| momentum_26 + reversion_12 | -0.32% | -7.39% | 1.24% | 0.49% | 39.69% |
| momentum_26 AND volume_26 | -0.79% | -5.27% | 1.24% | 0.05% | 3.92% |
| momentum_26 + volume_26 | -0.80% | -6.67% | 1.24% | 0.39% | 31.86% |
| breakout_8 AND reversion_12 | 0.00% | 0.00% | 1.24% | 0.00% | 0.00% |
| breakout_8 + reversion_12 | -0.30% | -13.58% | 1.24% | 0.30% | 24.68% |
| breakout_8 AND volume_26 | -0.35% | -2.83% | 1.24% | 0.03% | 2.09% |
| breakout_8 + volume_26 | -0.78% | -12.90% | 1.24% | 0.21% | 16.85% |
| reversion_12 AND volume_26 | -0.87% | -4.55% | 1.24% | 0.04% | 3.39% |
| reversion_12 + volume_26 | -0.83% | -10.35% | 1.24% | 0.20% | 16.72% |
| ema_12_26 | 0.25% | -3.06% | 1.24% | 0.72% | 58.49% |
| macd_12_26_9 | 0.21% | -4.71% | 1.24% | 0.44% | 35.51% |
| rsi_14_recovery | -0.29% | -3.18% | 1.24% | 0.02% | 1.83% |
| bollinger_20_reentry | -0.88% | -5.75% | 1.24% | 0.04% | 3.13% |
| donchian_20 | 0.06% | -8.39% | 1.24% | 0.09% | 7.57% |
| atr_14_breakout | 0.30% | -5.82% | 1.24% | 0.05% | 4.18% |
| session_vwap | 1.75% | -8.78% | 1.24% | 0.60% | 48.56% |
| obv_20 | -0.31% | -9.11% | 1.24% | 0.51% | 41.25% |
| stochastic_14_3_recovery | 0.28% | -12.70% | 1.24% | 0.11% | 8.62% |
| mfi_14_recovery | 0.08% | -2.41% | 1.24% | 0.02% | 1.57% |
| adx_14_trend | 0.57% | -2.34% | 1.24% | 0.31% | 25.07% |
| aroon_25_trend | 0.77% | -2.15% | 1.24% | 0.32% | 26.11% |
| cci_20_momentum | -0.04% | -8.87% | 1.24% | 0.30% | 24.80% |
| williams_14_recovery | 0.18% | -9.81% | 1.24% | 0.08% | 6.53% |
| cmf_20_accumulation | 2.03% | -2.17% | 1.24% | 0.59% | 47.78% |
| chaikin_3_10 | 1.56% | -5.83% | 1.24% | 0.56% | 45.43% |
| roc_10_momentum | -0.13% | -0.97% | 1.24% | 0.01% | 1.04% |
| trix_15_trend | -0.31% | -5.61% | 1.24% | 0.55% | 44.91% |
| keltner_20_breakout | -0.22% | -4.73% | 1.24% | 0.15% | 12.27% |
| opening_range_30m | 0.57% | -5.57% | 1.24% | 0.50% | 40.47% |

동일 구간·초기 자금, 종료 시 청산 비용 포함. 노출 맞춤은 사후 설명용이며 v2 실제 계좌 성과가 아닙니다.
[낙폭 분해·비용 영향·전체 구간](SPY/comparison.json)

[v1 전체 기록](SPY/accounts.json) · [v2 전체 기록](SPY/accounts-v2.json)

## QQQ 계좌

| 모델 | 전략 | 평가액 USD | 손익 USD | 최근 매매·이유 |
|---|---|---:|---:|---|
| v1 | cash | 10000.00 | 0.00 | 대기 /  / 새 신호 대기 |
| v1 | buy_hold | 9984.28 | -15.72 | buy /  / buy_hold: prior completed bar target 100%; next bar open simulation |
| v1 | trend_8_26 | 9863.13 | -136.87 | buy /  / trend_8_26: prior completed bar target 100%; next bar open simulation |
| v1 | momentum_26 | 9547.54 | -452.46 | buy /  / momentum_26: prior completed bar target 100%; next bar open simulation |
| v1 | breakout_8 | 9613.51 | -386.49 | sell /  / breakout_8: prior completed bar target 0%; next bar open simulation |
| v1 | reversion_12 | 9748.50 | -251.50 | sell /  / reversion_12: prior completed bar target 0%; next bar open simulation |
| v1 | volume_26 | 9606.91 | -393.09 | sell /  / volume_26: prior completed bar target 0%; next bar open simulation |
| v1 | trend_8_26 AND momentum_26 | 9916.26 | -83.74 | buy /  / trend_8_26 AND momentum_26: prior completed bar target 100%; next bar open simulation |
| v1 | trend_8_26 + momentum_26 | 9743.01 | -256.99 | buy /  / trend_8_26 + momentum_26: prior completed bar target 100%; next bar open simulation |
| v1 | trend_8_26 AND breakout_8 | 9949.62 | -50.38 | sell /  / trend_8_26 AND breakout_8: prior completed bar target 0%; next bar open simulation |
| v1 | trend_8_26 + breakout_8 | 9776.51 | -223.49 | sell /  / trend_8_26 + breakout_8: prior completed bar target 50%; next bar open simulation |
| v1 | trend_8_26 AND reversion_12 | 9885.50 | -114.50 | sell /  / trend_8_26 AND reversion_12: prior completed bar target 0%; next bar open simulation |
| v1 | trend_8_26 + reversion_12 | 9825.34 | -174.66 | sell /  / trend_8_26 + reversion_12: prior completed bar target 50%; next bar open simulation |
| v1 | trend_8_26 AND volume_26 | 9846.67 | -153.33 | sell /  / trend_8_26 AND volume_26: prior completed bar target 0%; next bar open simulation |
| v1 | trend_8_26 + volume_26 | 9734.07 | -265.93 | sell /  / trend_8_26 + volume_26: prior completed bar target 50%; next bar open simulation |
| v1 | momentum_26 AND breakout_8 | 9644.64 | -355.36 | sell /  / momentum_26 AND breakout_8: prior completed bar target 0%; next bar open simulation |
| v1 | momentum_26 + breakout_8 | 9580.55 | -419.45 | sell /  / momentum_26 + breakout_8: prior completed bar target 50%; next bar open simulation |
| v1 | momentum_26 AND reversion_12 | 9783.95 | -216.05 | sell /  / momentum_26 AND reversion_12: prior completed bar target 0%; next bar open simulation |
| v1 | momentum_26 + reversion_12 | 9686.30 | -313.70 | sell /  / momentum_26 + reversion_12: prior completed bar target 50%; next bar open simulation |
| v1 | momentum_26 AND volume_26 | 9819.14 | -180.86 | sell /  / momentum_26 AND volume_26: prior completed bar target 0%; next bar open simulation |
| v1 | momentum_26 + volume_26 | 9596.26 | -403.74 | sell /  / momentum_26 + volume_26: prior completed bar target 50%; next bar open simulation |
| v1 | breakout_8 AND reversion_12 | 10000.00 | 0.00 | 대기 /  / 새 신호 대기 |
| v1 | breakout_8 + reversion_12 | 9719.59 | -280.41 | sell /  / breakout_8 + reversion_12: prior completed bar target 0%; next bar open simulation |
| v1 | breakout_8 AND volume_26 | 9929.33 | -70.67 | sell /  / breakout_8 AND volume_26: prior completed bar target 0%; next bar open simulation |
| v1 | breakout_8 + volume_26 | 9629.42 | -370.58 | sell /  / breakout_8 + volume_26: prior completed bar target 0%; next bar open simulation |
| v1 | reversion_12 AND volume_26 | 9907.31 | -92.69 | sell /  / reversion_12 AND volume_26: prior completed bar target 0%; next bar open simulation |
| v1 | reversion_12 + volume_26 | 9716.19 | -283.81 | sell /  / reversion_12 + volume_26: prior completed bar target 0%; next bar open simulation |
| v1 | ema_12_26 | 9618.09 | -381.91 | buy /  / EMA12 > EMA26; 조건 충족; EMA12=719.205, EMA26=719.04 |
| v1 | macd_12_26_9 | 9765.43 | -234.57 | sell /  / MACD > 신호선 그리고 MACD > 0; 조건 미충족; MACD=1.7811, signal9=1.82319 |
| v1 | rsi_14_recovery | 9809.40 | -190.60 | sell /  / 직전 RSI14 < 30, 현재 RSI14 >= 30 (한 봉 목표); 조건 미충족; RSI14=50.2063, previous_RSI14=44.1729 |
| v1 | bollinger_20_reentry | 9878.60 | -121.40 | sell /  / 직전 종가 < 직전 하단밴드, 현재 하단밴드 <= 종가 <= SMA20 (한 봉 목표); 조건 미충족; close=718.66, lower20=714.386, SMA20=719.409, previous_lower20=714.271 |
| v1 | donchian_20 | 9889.14 | -110.86 | sell /  / 종가 > 현재 봉을 제외한 직전 20봉 최고가; 조건 미충족; close=726.885, prior_high20=727.77 |
| v1 | atr_14_breakout | 9907.04 | -92.96 | buy /  / 종가 > 직전 종가 + 직전 ATR14 그리고 종가 > EMA26; 조건 충족; close=726.035, threshold=725.469, prior_ATR14=1.44871, EMA26=724.514 |
| v1 | session_vwap | 9664.52 | -335.48 | buy /  / 종가 > 뉴욕 거래일별 누적 전형가격 VWAP; 조건 충족; close=726.035, session_VWAP=725.025, session_volume=3.37185e+08 |
| v1 | obv_20 | 9688.72 | -311.28 | buy /  / OBV > OBV의 SMA20 그리고 종가 > EMA26; 조건 충족; OBV=4.6809e+08, OBV_SMA20=4.15652e+08, close=726.035, EMA26=724.514 |
| v1 | stochastic_14_3_recovery | 9598.51 | -401.49 | sell /  / 직전 %K14 < 20에서 %K14가 %D3 상향 돌파 (한 봉 목표); 조건 미충족; K14=21.6302, D3=18.3878, previous_K14=24.7642, previous_D3=19.9023 |
| v1 | mfi_14_recovery | 9813.56 | -186.44 | sell /  / 직전 MFI14 < 20, 현재 MFI14 >= 20 (한 봉 목표); 조건 미충족; MFI14=30.3876, previous_MFI14=31.1747 |
| v1 | adx_14_trend | 9844.87 | -155.13 | buy /  / Wilder ADX14 >= 25 그리고 +DI14 > -DI14; 조건 충족; ADX14=25.5652, plus_DI14=28.4845, minus_DI14=28.3121 |
| v1 | aroon_25_trend | 9774.48 | -225.52 | sell /  / Aroon25 Up > 70 그리고 Down < 30 (동률이면 최신 극값); 조건 미충족; Aroon_up=68, Aroon_down=4 |
| v1 | cci_20_momentum | 9862.10 | -137.90 | sell /  / CCI20 > 100 (전형가격·평균절대편차); 조건 미충족; CCI20=80.102 |
| v1 | williams_14_recovery | 9677.65 | -322.35 | sell /  / 직전 Williams %R14 < -80, 현재 >= -80 (한 봉 목표); 조건 미충족; Williams_R14=-35.3329, previous_R14=-72.5093 |
| v1 | cmf_20_accumulation | 9577.92 | -422.08 | buy /  / Chaikin Money Flow20 > 0.1; 조건 충족; CMF20=0.185201, volume20=2.07769e+08 |
| v1 | chaikin_3_10 | 9695.52 | -304.48 | buy /  / ADL의 EMA3 - EMA10 > 0 그리고 종가 > EMA26; 조건 충족; Chaikin3_10=9.22379e+06, ADL=3.74683e+08, close=726.035, EMA26=724.514 |
| v1 | roc_10_momentum | 9961.33 | -38.67 | sell /  / 10봉 ROC > 1% 그리고 종가 > EMA26; 조건 미충족; ROC10_percent=0.681109, close=725.78, EMA26=721.667 |
| v1 | trix_15_trend | 9646.23 | -353.77 | buy /  / 15봉 삼중 EMA의 1봉 변화율 TRIX > 0 그리고 종가 > EMA26; 조건 충족; TRIX15_percent=0.0333889, close=726.035, EMA26=724.514 |
| v1 | keltner_20_breakout | 9782.40 | -217.60 | sell /  / 종가 > EMA20 + 2 x Wilder ATR14; 조건 미충족; close=726.815, upper_Keltner=727.39, EMA20=724.295, ATR14=1.54727 |
| v1 | opening_range_30m | 9780.90 | -219.10 | buy /  / 뉴욕 09:30·09:45 두 완료 봉 최고가를 10:00 이후 종가가 돌파; 조건 충족; close=723.37, opening_high=723.2 |
| v2 | cash | 10000.00 | 0.00 | 대기 /  / 새 신호 대기 |
| v2 | buy_hold | 9661.55 | -338.45 | buy / partial / 직전 완료 봉 목표 비중 100%; 다음 봉 시가 가정 |
| v2 | trend_8_26 | 9662.75 | -337.25 | buy / partial / 직전 완료 봉 목표 비중 100%; 다음 봉 시가 가정 |
| v2 | momentum_26 | 9437.66 | -562.34 | buy / partial / 직전 완료 봉 목표 비중 100%; 다음 봉 시가 가정 |
| v2 | breakout_8 | 9279.42 | -720.58 | sell / filled / 직전 완료 봉 목표 비중 0%; 다음 봉 시가 가정 |
| v2 | reversion_12 | 9257.97 | -742.03 | sell / filled / 직전 완료 봉 목표 비중 0%; 다음 봉 시가 가정 |
| v2 | volume_26 | 9565.80 | -434.20 | 중단: 손실 한도 / sell / filled / 직전 완료 봉 목표 비중 0%; 다음 봉 시가 가정 |
| v2 | trend_8_26 AND momentum_26 | 9809.98 | -190.02 | buy / partial / 직전 완료 봉 목표 비중 100%; 다음 봉 시가 가정 |
| v2 | trend_8_26 + momentum_26 | 9589.83 | -410.17 | buy / partial / 직전 완료 봉 목표 비중 100%; 다음 봉 시가 가정 |
| v2 | trend_8_26 AND breakout_8 | 9840.07 | -159.93 | sell / filled / 직전 완료 봉 목표 비중 0%; 다음 봉 시가 가정 |
| v2 | trend_8_26 + breakout_8 | 9508.91 | -491.09 | sell / filled / 직전 완료 봉 목표 비중 50%; 다음 봉 시가 가정 |
| v2 | trend_8_26 AND reversion_12 | 9742.38 | -257.62 | sell / filled / 직전 완료 봉 목표 비중 0%; 다음 봉 시가 가정 |
| v2 | trend_8_26 + reversion_12 | 9477.81 | -522.19 | sell / filled / 직전 완료 봉 목표 비중 50%; 다음 봉 시가 가정 |
| v2 | trend_8_26 AND volume_26 | 9679.53 | -320.47 | sell / filled / 직전 완료 봉 목표 비중 0%; 다음 봉 시가 가정 |
| v2 | trend_8_26 + volume_26 | 9336.06 | -663.94 | sell / filled / 직전 완료 봉 목표 비중 50%; 다음 봉 시가 가정 |
| v2 | momentum_26 AND breakout_8 | 9591.37 | -408.63 | sell / filled / 직전 완료 봉 목표 비중 0%; 다음 봉 시가 가정 |
| v2 | momentum_26 + breakout_8 | 9358.23 | -641.77 | sell / filled / 직전 완료 봉 목표 비중 50%; 다음 봉 시가 가정 |
| v2 | momentum_26 AND reversion_12 | 9776.12 | -223.88 | sell / filled / 직전 완료 봉 목표 비중 0%; 다음 봉 시가 가정 |
| v2 | momentum_26 + reversion_12 | 9406.25 | -593.75 | sell / filled / 직전 완료 봉 목표 비중 50%; 다음 봉 시가 가정 |
| v2 | momentum_26 AND volume_26 | 9749.31 | -250.69 | sell / filled / 직전 완료 봉 목표 비중 0%; 다음 봉 시가 가정 |
| v2 | momentum_26 + volume_26 | 9246.07 | -753.93 | sell / filled / 직전 완료 봉 목표 비중 50%; 다음 봉 시가 가정 |
| v2 | breakout_8 AND reversion_12 | 10000.00 | 0.00 | 대기 /  / 새 신호 대기 |
| v2 | breakout_8 + reversion_12 | 9366.21 | -633.79 | sell / filled / 직전 완료 봉 목표 비중 0%; 다음 봉 시가 가정 |
| v2 | breakout_8 AND volume_26 | 9871.76 | -128.24 | sell / filled / 직전 완료 봉 목표 비중 0%; 다음 봉 시가 가정 |
| v2 | breakout_8 + volume_26 | 9206.94 | -793.06 | sell / filled / 직전 완료 봉 목표 비중 0%; 다음 봉 시가 가정 |
| v2 | reversion_12 AND volume_26 | 9547.64 | -452.36 | 중단: 손실 한도 / sell / filled / 직전 완료 봉 목표 비중 0%; 다음 봉 시가 가정 |
| v2 | reversion_12 + volume_26 | 9196.36 | -803.64 | sell / filled / 직전 완료 봉 목표 비중 0%; 다음 봉 시가 가정 |
| v2 | ema_12_26 | 9609.44 | -390.56 | buy / partial / EMA12 > EMA26; 조건 충족; EMA12=719.205, EMA26=719.04; 직전 완료 봉 목표를 다음 봉 시가에 모의 적용 |
| v2 | macd_12_26_9 | 9755.67 | -244.33 | sell / filled / MACD > 신호선 그리고 MACD > 0; 조건 미충족; MACD=1.7811, signal9=1.82319; 직전 완료 봉 목표를 다음 봉 시가에 모의 적용 |
| v2 | rsi_14_recovery | 9801.56 | -198.44 | sell / filled / 직전 RSI14 < 30, 현재 RSI14 >= 30 (한 봉 목표); 조건 미충족; RSI14=50.2063, previous_RSI14=44.1729; 직전 완료 봉 목표를 다음 봉 시가에 모의 적용 |
| v2 | bollinger_20_reentry | 9872.68 | -127.32 | sell / filled / 직전 종가 < 직전 하단밴드, 현재 하단밴드 <= 종가 <= SMA20 (한 봉 목표); 조건 미충족; close=718.66, lower20=714.386, SMA20=719.409, previous_lower20=714.271; 직전 완료 봉 목표를 다음 봉 시가에 모의 적용 |
| v2 | donchian_20 | 9881.23 | -118.77 | sell / filled / 종가 > 현재 봉을 제외한 직전 20봉 최고가; 조건 미충족; close=726.885, prior_high20=727.77; 직전 완료 봉 목표를 다음 봉 시가에 모의 적용 |
| v2 | atr_14_breakout | 9900.11 | -99.89 | buy / partial / 종가 > 직전 종가 + 직전 ATR14 그리고 종가 > EMA26; 조건 충족; close=726.035, threshold=725.469, prior_ATR14=1.44871, EMA26=724.514; 직전 완료 봉 목표를 다음 봉 시가에 모의 적용 |
| v2 | session_vwap | 9648.10 | -351.90 | buy / partial / 종가 > 뉴욕 거래일별 누적 전형가격 VWAP; 조건 충족; close=726.035, session_VWAP=725.025, session_volume=3.37185e+08; 직전 완료 봉 목표를 다음 봉 시가에 모의 적용 |
| v2 | obv_20 | 9676.13 | -323.87 | buy / partial / OBV > OBV의 SMA20 그리고 종가 > EMA26; 조건 충족; OBV=4.6809e+08, OBV_SMA20=4.15652e+08, close=726.035, EMA26=724.514; 직전 완료 봉 목표를 다음 봉 시가에 모의 적용 |
| v2 | stochastic_14_3_recovery | 9694.13 | -305.87 | 중단: 손실 한도 / sell / filled / 직전 %K14 < 20에서 %K14가 %D3 상향 돌파 (한 봉 목표); 조건 미충족; K14=10.576, D3=8.00581, previous_K14=7.39787, previous_D3=7.27486; 직전 완료 봉 목표를 다음 봉 시가에 모의 적용 |
| v2 | mfi_14_recovery | 9809.63 | -190.37 | sell / filled / 직전 MFI14 < 20, 현재 MFI14 >= 20 (한 봉 목표); 조건 미충족; MFI14=30.3876, previous_MFI14=31.1747; 직전 완료 봉 목표를 다음 봉 시가에 모의 적용 |
| v2 | adx_14_trend | 9837.98 | -162.02 | buy / partial / Wilder ADX14 >= 25 그리고 +DI14 > -DI14; 조건 충족; ADX14=25.5652, plus_DI14=28.4845, minus_DI14=28.3121; 직전 완료 봉 목표를 다음 봉 시가에 모의 적용 |
| v2 | aroon_25_trend | 9766.66 | -233.34 | sell / filled / Aroon25 Up > 70 그리고 Down < 30 (동률이면 최신 극값); 조건 미충족; Aroon_up=68, Aroon_down=4; 직전 완료 봉 목표를 다음 봉 시가에 모의 적용 |
| v2 | cci_20_momentum | 9852.25 | -147.75 | sell / filled / CCI20 > 100 (전형가격·평균절대편차); 조건 미충족; CCI20=80.102; 직전 완료 봉 목표를 다음 봉 시가에 모의 적용 |
| v2 | williams_14_recovery | 9658.32 | -341.68 | sell / filled / 직전 Williams %R14 < -80, 현재 >= -80 (한 봉 목표); 조건 미충족; Williams_R14=-35.3329, previous_R14=-72.5093; 직전 완료 봉 목표를 다음 봉 시가에 모의 적용 |
| v2 | cmf_20_accumulation | 9563.57 | -436.43 | buy / partial / Chaikin Money Flow20 > 0.1; 조건 충족; CMF20=0.185201, volume20=2.07769e+08; 직전 완료 봉 목표를 다음 봉 시가에 모의 적용 |
| v2 | chaikin_3_10 | 9682.93 | -317.07 | buy / partial / ADL의 EMA3 - EMA10 > 0 그리고 종가 > EMA26; 조건 충족; Chaikin3_10=9.22379e+06, ADL=3.74683e+08, close=726.035, EMA26=724.514; 직전 완료 봉 목표를 다음 봉 시가에 모의 적용 |
| v2 | roc_10_momentum | 9957.34 | -42.66 | sell / filled / 10봉 ROC > 1% 그리고 종가 > EMA26; 조건 미충족; ROC10_percent=0.681109, close=725.78, EMA26=721.667; 직전 완료 봉 목표를 다음 봉 시가에 모의 적용 |
| v2 | trix_15_trend | 9633.69 | -366.31 | buy / partial / 15봉 삼중 EMA의 1봉 변화율 TRIX > 0 그리고 종가 > EMA26; 조건 충족; TRIX15_percent=0.0333889, close=726.035, EMA26=724.514; 직전 완료 봉 목표를 다음 봉 시가에 모의 적용 |
| v2 | keltner_20_breakout | 9772.62 | -227.38 | sell / filled / 종가 > EMA20 + 2 x Wilder ATR14; 조건 미충족; close=726.815, upper_Keltner=727.39, EMA20=724.295, ATR14=1.54727; 직전 완료 봉 목표를 다음 봉 시가에 모의 적용 |
| v2 | opening_range_30m | 9772.10 | -227.90 | buy / partial / 뉴욕 09:30·09:45 두 완료 봉 최고가를 10:00 이후 종가가 돌파; 조건 충족; close=723.37, opening_high=723.2; 직전 완료 봉 목표를 다음 봉 시가에 모의 적용 |

### 같은 기간의 비용·노출 비교 (사후 연구)

| 전략 | 비용 전 | 비용 후 | 100% 보유 | 같은 평균 노출 보유 | 평균 노출 |
|---|---:|---:|---:|---:|---:|
| cash | 0.00% | 0.00% | -2.17% | -0.00% | 0.00% |
| buy_hold | -1.75% | -2.17% | -2.17% | -2.17% | 100.00% |
| trend_8_26 | 0.47% | -3.26% | -2.17% | -0.95% | 43.60% |
| momentum_26 | -2.79% | -8.73% | -2.17% | -0.86% | 39.43% |
| breakout_8 | -1.36% | -16.62% | -2.17% | -0.42% | 19.58% |
| reversion_12 | 0.53% | -11.74% | -2.17% | -0.63% | 29.24% |
| volume_26 | -1.22% | -14.37% | -2.17% | -0.34% | 15.67% |
| trend_8_26 AND momentum_26 | 0.15% | -3.56% | -2.17% | -0.70% | 32.38% |
| trend_8_26 + momentum_26 | -1.17% | -5.44% | -2.17% | -0.90% | 41.52% |
| trend_8_26 AND breakout_8 | 0.42% | -7.67% | -2.17% | -0.25% | 11.75% |
| trend_8_26 + breakout_8 | -0.44% | -9.62% | -2.17% | -0.69% | 31.60% |
| trend_8_26 AND reversion_12 | -0.22% | -4.33% | -2.17% | -0.14% | 6.53% |
| trend_8_26 + reversion_12 | 0.51% | -7.21% | -2.17% | -0.79% | 36.43% |
| trend_8_26 AND volume_26 | 0.23% | -4.70% | -2.17% | -0.11% | 5.22% |
| trend_8_26 + volume_26 | -0.37% | -8.99% | -2.17% | -0.64% | 29.64% |
| momentum_26 AND breakout_8 | -0.45% | -9.61% | -2.17% | -0.27% | 12.53% |
| momentum_26 + breakout_8 | -2.07% | -12.58% | -2.17% | -0.64% | 29.51% |
| momentum_26 AND reversion_12 | -1.04% | -5.51% | -2.17% | -0.14% | 6.53% |
| momentum_26 + reversion_12 | -1.13% | -9.49% | -2.17% | -0.74% | 34.34% |
| momentum_26 AND volume_26 | -0.38% | -4.08% | -2.17% | -0.08% | 3.66% |
| momentum_26 + volume_26 | -2.00% | -11.22% | -2.17% | -0.60% | 27.55% |
| breakout_8 AND reversion_12 | 0.00% | 0.00% | -2.17% | -0.00% | 0.00% |
| breakout_8 + reversion_12 | -0.41% | -13.13% | -2.17% | -0.53% | 24.42% |
| breakout_8 AND volume_26 | 0.32% | -2.18% | -2.17% | -0.05% | 2.35% |
| breakout_8 + volume_26 | -1.29% | -14.07% | -2.17% | -0.38% | 17.63% |
| reversion_12 AND volume_26 | -1.15% | -7.57% | -2.17% | -0.17% | 7.83% |
| reversion_12 + volume_26 | -0.34% | -12.52% | -2.17% | -0.49% | 22.46% |
| ema_12_26 | -0.99% | -3.86% | -2.17% | -0.89% | 40.99% |
| macd_12_26_9 | 0.69% | -3.86% | -2.17% | -0.55% | 25.33% |
| rsi_14_recovery | -0.47% | -5.76% | -2.17% | -0.07% | 3.39% |
| bollinger_20_reentry | 0.11% | -5.21% | -2.17% | -0.07% | 3.39% |
| donchian_20 | 0.58% | -5.17% | -2.17% | -0.14% | 6.53% |
| atr_14_breakout | 0.48% | -4.06% | -2.17% | -0.07% | 3.13% |
| session_vwap | 0.08% | -11.40% | -2.17% | -1.01% | 46.48% |
| obv_20 | -1.42% | -10.50% | -2.17% | -0.63% | 29.24% |
| stochastic_14_3_recovery | 0.23% | -11.26% | -2.17% | -0.16% | 7.57% |
| mfi_14_recovery | -1.19% | -3.24% | -2.17% | -0.03% | 1.31% |
| adx_14_trend | -0.29% | -3.58% | -2.17% | -0.45% | 20.63% |
| aroon_25_trend | 1.00% | -2.75% | -2.17% | -0.38% | 17.49% |
| cci_20_momentum | -0.11% | -5.82% | -2.17% | -0.41% | 19.06% |
| williams_14_recovery | 0.19% | -10.55% | -2.17% | -0.15% | 7.05% |
| cmf_20_accumulation | -1.45% | -8.24% | -2.17% | -0.78% | 36.03% |
| chaikin_3_10 | -2.46% | -10.69% | -2.17% | -0.74% | 33.94% |
| roc_10_momentum | 0.13% | -1.54% | -2.17% | -0.10% | 4.70% |
| trix_15_trend | 0.05% | -3.67% | -2.17% | -0.73% | 33.68% |
| keltner_20_breakout | -0.82% | -5.70% | -2.17% | -0.19% | 8.62% |
| opening_range_30m | -0.07% | -5.38% | -2.17% | -0.73% | 33.68% |

동일 구간·초기 자금, 종료 시 청산 비용 포함. 노출 맞춤은 사후 설명용이며 v2 실제 계좌 성과가 아닙니다.
[낙폭 분해·비용 영향·전체 구간](QQQ/comparison.json)

[v1 전체 기록](QQQ/accounts.json) · [v2 전체 기록](QQQ/accounts-v2.json)

## IWM 계좌

| 모델 | 전략 | 평가액 USD | 손익 USD | 최근 매매·이유 |
|---|---|---:|---:|---|
| v1 | cash | 10000.00 | 0.00 | 대기 /  / 새 신호 대기 |
| v1 | buy_hold | 10015.53 | 15.53 | buy /  / buy_hold: prior completed bar target 100%; next bar open simulation |
| v1 | trend_8_26 | 9820.54 | -179.46 | buy /  / trend_8_26: prior completed bar target 100%; next bar open simulation |
| v1 | momentum_26 | 9920.22 | -79.78 | buy /  / momentum_26: prior completed bar target 100%; next bar open simulation |
| v1 | breakout_8 | 9416.78 | -583.22 | sell /  / breakout_8: prior completed bar target 0%; next bar open simulation |
| v1 | reversion_12 | 9770.68 | -229.32 | sell /  / reversion_12: prior completed bar target 0%; next bar open simulation |
| v1 | volume_26 | 9915.22 | -84.78 | sell /  / volume_26: prior completed bar target 0%; next bar open simulation |
| v1 | trend_8_26 AND momentum_26 | 9766.07 | -233.93 | buy /  / trend_8_26 AND momentum_26: prior completed bar target 100%; next bar open simulation |
| v1 | trend_8_26 + momentum_26 | 9870.38 | -129.62 | buy /  / trend_8_26 + momentum_26: prior completed bar target 100%; next bar open simulation |
| v1 | trend_8_26 AND breakout_8 | 9504.10 | -495.90 | sell /  / trend_8_26 AND breakout_8: prior completed bar target 0%; next bar open simulation |
| v1 | trend_8_26 + breakout_8 | 9616.72 | -383.28 | sell /  / trend_8_26 + breakout_8: prior completed bar target 50%; next bar open simulation |
| v1 | trend_8_26 AND reversion_12 | 9811.31 | -188.69 | sell /  / trend_8_26 AND reversion_12: prior completed bar target 0%; next bar open simulation |
| v1 | trend_8_26 + reversion_12 | 9795.41 | -204.59 | sell /  / trend_8_26 + reversion_12: prior completed bar target 50%; next bar open simulation |
| v1 | trend_8_26 AND volume_26 | 9927.90 | -72.10 | sell /  / trend_8_26 AND volume_26: prior completed bar target 0%; next bar open simulation |
| v1 | trend_8_26 + volume_26 | 9887.35 | -112.65 | sell /  / trend_8_26 + volume_26: prior completed bar target 50%; next bar open simulation |
| v1 | momentum_26 AND breakout_8 | 9552.12 | -447.88 | sell /  / momentum_26 AND breakout_8: prior completed bar target 0%; next bar open simulation |
| v1 | momentum_26 + breakout_8 | 9684.72 | -315.28 | buy /  / momentum_26 + breakout_8: prior completed bar target 50%; next bar open simulation |
| v1 | momentum_26 AND reversion_12 | 9876.67 | -123.33 | sell /  / momentum_26 AND reversion_12: prior completed bar target 0%; next bar open simulation |
| v1 | momentum_26 + reversion_12 | 9884.46 | -115.54 | sell /  / momentum_26 + reversion_12: prior completed bar target 50%; next bar open simulation |
| v1 | momentum_26 AND volume_26 | 10062.05 | 62.05 | sell /  / momentum_26 AND volume_26: prior completed bar target 0%; next bar open simulation |
| v1 | momentum_26 + volume_26 | 9957.28 | -42.72 | sell /  / momentum_26 + volume_26: prior completed bar target 50%; next bar open simulation |
| v1 | breakout_8 AND reversion_12 | 10000.00 | 0.00 | 대기 /  / 새 신호 대기 |
| v1 | breakout_8 + reversion_12 | 9611.10 | -388.90 | sell /  / breakout_8 + reversion_12: prior completed bar target 0%; next bar open simulation |
| v1 | breakout_8 AND volume_26 | 9967.28 | -32.72 | sell /  / breakout_8 AND volume_26: prior completed bar target 0%; next bar open simulation |
| v1 | breakout_8 + volume_26 | 9682.03 | -317.97 | sell /  / breakout_8 + volume_26: prior completed bar target 0%; next bar open simulation |
| v1 | reversion_12 AND volume_26 | 9927.90 | -72.10 | sell /  / reversion_12 AND volume_26: prior completed bar target 0%; next bar open simulation |
| v1 | reversion_12 + volume_26 | 9862.33 | -137.67 | sell /  / reversion_12 + volume_26: prior completed bar target 0%; next bar open simulation |
| v1 | ema_12_26 | 9885.81 | -114.19 | buy /  / EMA12 > EMA26; 조건 충족; EMA12=271.545, EMA26=271.529 |
| v1 | macd_12_26_9 | 9906.42 | -93.58 | sell /  / MACD > 신호선 그리고 MACD > 0; 조건 미충족; MACD=0.978353, signal9=1.01104 |
| v1 | rsi_14_recovery | 9786.95 | -213.05 | sell /  / 직전 RSI14 < 30, 현재 RSI14 >= 30 (한 봉 목표); 조건 미충족; RSI14=46.986, previous_RSI14=37.1649 |
| v1 | bollinger_20_reentry | 9898.12 | -101.88 | buy /  / 직전 종가 < 직전 하단밴드, 현재 하단밴드 <= 종가 <= SMA20 (한 봉 목표); 조건 충족; close=276.68, lower20=276.099, SMA20=276.809, previous_lower20=276.092 |
| v1 | donchian_20 | 9835.91 | -164.09 | sell /  / 종가 > 현재 봉을 제외한 직전 20봉 최고가; 조건 미충족; close=275.785, prior_high20=276.875 |
| v1 | atr_14_breakout | 9824.11 | -175.89 | buy /  / 종가 > 직전 종가 + 직전 ATR14 그리고 종가 > EMA26; 조건 충족; close=276.68, threshold=276.308, prior_ATR14=0.507658, EMA26=276.508 |
| v1 | session_vwap | 9645.15 | -354.85 | buy /  / 종가 > 뉴욕 거래일별 누적 전형가격 VWAP; 조건 충족; close=276.68, session_VWAP=276.635, session_volume=1.23835e+07 |
| v1 | obv_20 | 9843.12 | -156.88 | sell /  / OBV > OBV의 SMA20 그리고 종가 > EMA26; 조건 미충족; OBV=-2.34336e+07, OBV_SMA20=-2.34421e+07, close=276.015, EMA26=276.549 |
| v1 | stochastic_14_3_recovery | 9665.87 | -334.13 | sell /  / 직전 %K14 < 20에서 %K14가 %D3 상향 돌파 (한 봉 목표); 조건 미충족; K14=72.727, D3=41.2922, previous_K14=34.0903, previous_D3=23.8263 |
| v1 | mfi_14_recovery | 9934.22 | -65.78 | sell /  / 직전 MFI14 < 20, 현재 MFI14 >= 20 (한 봉 목표); 조건 미충족; MFI14=34.131, previous_MFI14=22.0435 |
| v1 | adx_14_trend | 9726.05 | -273.95 | sell /  / Wilder ADX14 >= 25 그리고 +DI14 > -DI14; 조건 미충족; ADX14=27.8461, plus_DI14=25.882, minus_DI14=28.4558 |
| v1 | aroon_25_trend | 9745.85 | -254.15 | sell /  / Aroon25 Up > 70 그리고 Down < 30 (동률이면 최신 극값); 조건 미충족; Aroon_up=68, Aroon_down=4 |
| v1 | cci_20_momentum | 9825.51 | -174.49 | sell /  / CCI20 > 100 (전형가격·평균절대편차); 조건 미충족; CCI20=-152.101 |
| v1 | williams_14_recovery | 9825.31 | -174.69 | sell /  / 직전 Williams %R14 < -80, 현재 >= -80 (한 봉 목표); 조건 미충족; Williams_R14=-38.1167, previous_R14=-77.5786 |
| v1 | cmf_20_accumulation | 9800.10 | -199.90 | buy /  / Chaikin Money Flow20 > 0.1; 조건 충족; CMF20=0.119402, volume20=8.33053e+06 |
| v1 | chaikin_3_10 | 9775.94 | -224.06 | buy /  / ADL의 EMA3 - EMA10 > 0 그리고 종가 > EMA26; 조건 충족; Chaikin3_10=294514, ADL=-4.06803e+07, close=276.68, EMA26=276.508 |
| v1 | roc_10_momentum | 9996.39 | -3.61 | sell /  / 10봉 ROC > 1% 그리고 종가 > EMA26; 조건 미충족; ROC10_percent=0.995963, close=275.315, EMA26=273.754 |
| v1 | trix_15_trend | 9903.88 | -96.12 | buy /  / 15봉 삼중 EMA의 1봉 변화율 TRIX > 0 그리고 종가 > EMA26; 조건 충족; TRIX15_percent=0.0167985, close=276.68, EMA26=276.508 |
| v1 | keltner_20_breakout | 9879.23 | -120.77 | sell /  / 종가 > EMA20 + 2 x Wilder ATR14; 조건 미충족; close=276.4, upper_Keltner=277.094, EMA20=275.768, ATR14=0.662947 |
| v1 | opening_range_30m | 9963.15 | -36.85 | sell /  / 뉴욕 09:30·09:45 두 완료 봉 최고가를 10:00 이후 종가가 돌파; 자료 부족·변동폭 또는 거래량 없음: 대기; close=276.82 |
| v2 | cash | 10000.00 | 0.00 | 대기 /  / 새 신호 대기 |
| v2 | buy_hold | 9908.44 | -91.56 | buy / partial / 직전 완료 봉 목표 비중 100%; 다음 봉 시가 가정 |
| v2 | trend_8_26 | 9689.41 | -310.59 | buy / partial / 직전 완료 봉 목표 비중 100%; 다음 봉 시가 가정 |
| v2 | momentum_26 | 9786.80 | -213.20 | buy / partial / 직전 완료 봉 목표 비중 100%; 다음 봉 시가 가정 |
| v2 | breakout_8 | 9033.27 | -966.73 | sell / filled / 직전 완료 봉 목표 비중 0%; 다음 봉 시가 가정 |
| v2 | reversion_12 | 9308.75 | -691.25 | sell / filled / 직전 완료 봉 목표 비중 0%; 다음 봉 시가 가정 |
| v2 | volume_26 | 9425.16 | -574.84 | sell / filled / 직전 완료 봉 목표 비중 0%; 다음 봉 시가 가정 |
| v2 | trend_8_26 AND momentum_26 | 9781.32 | -218.68 | buy / partial / 직전 완료 봉 목표 비중 100%; 다음 봉 시가 가정 |
| v2 | trend_8_26 + momentum_26 | 9758.72 | -241.28 | buy / partial / 직전 완료 봉 목표 비중 100%; 다음 봉 시가 가정 |
| v2 | trend_8_26 AND breakout_8 | 9402.34 | -597.66 | sell / filled / 직전 완료 봉 목표 비중 0%; 다음 봉 시가 가정 |
| v2 | trend_8_26 + breakout_8 | 9375.57 | -624.43 | sell / filled / 직전 완료 봉 목표 비중 50%; 다음 봉 시가 가정 |
| v2 | trend_8_26 AND reversion_12 | 9687.61 | -312.39 | sell / filled / 직전 완료 봉 목표 비중 0%; 다음 봉 시가 가정 |
| v2 | trend_8_26 + reversion_12 | 9496.84 | -503.16 | sell / filled / 직전 완료 봉 목표 비중 50%; 다음 봉 시가 가정 |
| v2 | trend_8_26 AND volume_26 | 9787.80 | -212.20 | sell / filled / 직전 완료 봉 목표 비중 0%; 다음 봉 시가 가정 |
| v2 | trend_8_26 + volume_26 | 9596.40 | -403.60 | sell / filled / 직전 완료 봉 목표 비중 50%; 다음 봉 시가 가정 |
| v2 | momentum_26 AND breakout_8 | 9347.05 | -652.95 | sell / filled / 직전 완료 봉 목표 비중 0%; 다음 봉 시가 가정 |
| v2 | momentum_26 + breakout_8 | 9422.42 | -577.58 | buy / filled / 직전 완료 봉 목표 비중 50%; 다음 봉 시가 가정 |
| v2 | momentum_26 AND reversion_12 | 9831.84 | -168.16 | sell / filled / 직전 완료 봉 목표 비중 0%; 다음 봉 시가 가정 |
| v2 | momentum_26 + reversion_12 | 9604.55 | -395.45 | sell / filled / 직전 완료 봉 목표 비중 50%; 다음 봉 시가 가정 |
| v2 | momentum_26 AND volume_26 | 9957.22 | -42.78 | sell / filled / 직전 완료 봉 목표 비중 0%; 다음 봉 시가 가정 |
| v2 | momentum_26 + volume_26 | 9644.29 | -355.71 | sell / filled / 직전 완료 봉 목표 비중 50%; 다음 봉 시가 가정 |
| v2 | breakout_8 AND reversion_12 | 10000.00 | 0.00 | 대기 /  / 새 신호 대기 |
| v2 | breakout_8 + reversion_12 | 9227.33 | -772.67 | sell / filled / 직전 완료 봉 목표 비중 0%; 다음 봉 시가 가정 |
| v2 | breakout_8 AND volume_26 | 9710.25 | -289.75 | sell / filled / 직전 완료 봉 목표 비중 0%; 다음 봉 시가 가정 |
| v2 | breakout_8 + volume_26 | 9265.80 | -734.20 | sell / filled / 직전 완료 봉 목표 비중 0%; 다음 봉 시가 가정 |
| v2 | reversion_12 AND volume_26 | 9666.65 | -333.35 | sell / filled / 직전 완료 봉 목표 비중 0%; 다음 봉 시가 가정 |
| v2 | reversion_12 + volume_26 | 9405.92 | -594.08 | sell / filled / 직전 완료 봉 목표 비중 0%; 다음 봉 시가 가정 |
| v2 | ema_12_26 | 9880.87 | -119.13 | buy / partial / EMA12 > EMA26; 조건 충족; EMA12=271.545, EMA26=271.529; 직전 완료 봉 목표를 다음 봉 시가에 모의 적용 |
| v2 | macd_12_26_9 | 9900.47 | -99.53 | sell / filled / MACD > 신호선 그리고 MACD > 0; 조건 미충족; MACD=0.978353, signal9=1.01104; 직전 완료 봉 목표를 다음 봉 시가에 모의 적용 |
| v2 | rsi_14_recovery | 9779.12 | -220.88 | sell / filled / 직전 RSI14 < 30, 현재 RSI14 >= 30 (한 봉 목표); 조건 미충족; RSI14=46.986, previous_RSI14=37.1649; 직전 완료 봉 목표를 다음 봉 시가에 모의 적용 |
| v2 | bollinger_20_reentry | 9893.18 | -106.82 | buy / partial / 직전 종가 < 직전 하단밴드, 현재 하단밴드 <= 종가 <= SMA20 (한 봉 목표); 조건 충족; close=276.68, lower20=276.099, SMA20=276.809, previous_lower20=276.092; 직전 완료 봉 목표를 다음 봉 시가에 모의 적용 |
| v2 | donchian_20 | 9830.01 | -169.99 | sell / filled / 종가 > 현재 봉을 제외한 직전 20봉 최고가; 조건 미충족; close=275.785, prior_high20=276.875; 직전 완료 봉 목표를 다음 봉 시가에 모의 적용 |
| v2 | atr_14_breakout | 9813.31 | -186.69 | buy / partial / 종가 > 직전 종가 + 직전 ATR14 그리고 종가 > EMA26; 조건 충족; close=276.68, threshold=276.308, prior_ATR14=0.507658, EMA26=276.508; 직전 완료 봉 목표를 다음 봉 시가에 모의 적용 |
| v2 | session_vwap | 9626.84 | -373.16 | buy / partial / 종가 > 뉴욕 거래일별 누적 전형가격 VWAP; 조건 충족; close=276.68, session_VWAP=276.635, session_volume=1.23835e+07; 직전 완료 봉 목표를 다음 봉 시가에 모의 적용 |
| v2 | obv_20 | 9833.28 | -166.72 | sell / filled / OBV > OBV의 SMA20 그리고 종가 > EMA26; 조건 미충족; OBV=-2.34336e+07, OBV_SMA20=-2.34421e+07, close=276.015, EMA26=276.549; 직전 완료 봉 목표를 다음 봉 시가에 모의 적용 |
| v2 | stochastic_14_3_recovery | 9650.41 | -349.59 | sell / filled / 직전 %K14 < 20에서 %K14가 %D3 상향 돌파 (한 봉 목표); 조건 미충족; K14=72.727, D3=41.2922, previous_K14=34.0903, previous_D3=23.8263; 직전 완료 봉 목표를 다음 봉 시가에 모의 적용 |
| v2 | mfi_14_recovery | 9930.25 | -69.75 | sell / filled / 직전 MFI14 < 20, 현재 MFI14 >= 20 (한 봉 목표); 조건 미충족; MFI14=34.131, previous_MFI14=22.0435; 직전 완료 봉 목표를 다음 봉 시가에 모의 적용 |
| v2 | adx_14_trend | 9718.27 | -281.73 | sell / filled / Wilder ADX14 >= 25 그리고 +DI14 > -DI14; 조건 미충족; ADX14=27.8461, plus_DI14=25.882, minus_DI14=28.4558; 직전 완료 봉 목표를 다음 봉 시가에 모의 적용 |
| v2 | aroon_25_trend | 9736.11 | -263.89 | sell / filled / Aroon25 Up > 70 그리고 Down < 30 (동률이면 최신 극값); 조건 미충족; Aroon_up=68, Aroon_down=4; 직전 완료 봉 목표를 다음 봉 시가에 모의 적용 |
| v2 | cci_20_momentum | 9815.69 | -184.31 | sell / filled / CCI20 > 100 (전형가격·평균절대편차); 조건 미충족; CCI20=-152.101; 직전 완료 봉 목표를 다음 봉 시가에 모의 적용 |
| v2 | williams_14_recovery | 9815.49 | -184.51 | sell / filled / 직전 Williams %R14 < -80, 현재 >= -80 (한 봉 목표); 조건 미충족; Williams_R14=-38.1167, previous_R14=-77.5786; 직전 완료 봉 목표를 다음 봉 시가에 모의 적용 |
| v2 | cmf_20_accumulation | 9785.41 | -214.59 | buy / partial / Chaikin Money Flow20 > 0.1; 조건 충족; CMF20=0.119402, volume20=8.33053e+06; 직전 완료 봉 목표를 다음 봉 시가에 모의 적용 |
| v2 | chaikin_3_10 | 9763.24 | -236.76 | buy / partial / ADL의 EMA3 - EMA10 > 0 그리고 종가 > EMA26; 조건 충족; Chaikin3_10=294514, ADL=-4.06803e+07, close=276.68, EMA26=276.508; 직전 완료 봉 목표를 다음 봉 시가에 모의 적용 |
| v2 | roc_10_momentum | 9994.39 | -5.61 | sell / filled / 10봉 ROC > 1% 그리고 종가 > EMA26; 조건 미충족; ROC10_percent=0.995963, close=275.315, EMA26=273.754; 직전 완료 봉 목표를 다음 봉 시가에 모의 적용 |
| v2 | trix_15_trend | 9898.93 | -101.07 | buy / partial / 15봉 삼중 EMA의 1봉 변화율 TRIX > 0 그리고 종가 > EMA26; 조건 충족; TRIX15_percent=0.0167985, close=276.68, EMA26=276.508; 직전 완료 봉 목표를 다음 봉 시가에 모의 적용 |
| v2 | keltner_20_breakout | 9873.30 | -126.70 | sell / filled / 종가 > EMA20 + 2 x Wilder ATR14; 조건 미충족; close=276.4, upper_Keltner=277.094, EMA20=275.768, ATR14=0.662947; 직전 완료 봉 목표를 다음 봉 시가에 모의 적용 |
| v2 | opening_range_30m | 9959.17 | -40.83 | sell / filled / 뉴욕 09:30·09:45 두 완료 봉 최고가를 10:00 이후 종가가 돌파; 자료 부족·변동폭 또는 거래량 없음: 대기; close=276.82; 직전 완료 봉 목표를 다음 봉 시가에 모의 적용 |

### 같은 기간의 비용·노출 비교 (사후 연구)

| 전략 | 비용 전 | 비용 후 | 100% 보유 | 같은 평균 노출 보유 | 평균 노출 |
|---|---:|---:|---:|---:|---:|
| cash | 0.00% | 0.00% | -0.47% | -0.00% | 0.00% |
| buy_hold | -0.05% | -0.47% | -0.47% | -0.47% | 100.00% |
| trend_8_26 | -0.17% | -3.46% | -0.47% | -0.24% | 51.44% |
| momentum_26 | 0.28% | -5.05% | -0.47% | -0.22% | 48.04% |
| breakout_8 | -0.27% | -15.33% | -0.47% | -0.10% | 21.15% |
| reversion_12 | -1.69% | -12.23% | -0.47% | -0.12% | 25.59% |
| volume_26 | -0.60% | -7.45% | -0.47% | -0.03% | 7.31% |
| trend_8_26 AND momentum_26 | -0.35% | -4.45% | -0.47% | -0.20% | 43.08% |
| trend_8_26 + momentum_26 | 0.06% | -3.85% | -0.47% | -0.23% | 49.74% |
| trend_8_26 AND breakout_8 | -0.48% | -10.02% | -0.47% | -0.06% | 13.84% |
| trend_8_26 + breakout_8 | -0.21% | -9.40% | -0.47% | -0.17% | 36.30% |
| trend_8_26 AND reversion_12 | -0.50% | -4.60% | -0.47% | -0.03% | 5.48% |
| trend_8_26 + reversion_12 | -0.92% | -7.96% | -0.47% | -0.18% | 38.52% |
| trend_8_26 AND volume_26 | -0.37% | -3.25% | -0.47% | -0.01% | 2.35% |
| trend_8_26 + volume_26 | -0.37% | -5.08% | -0.47% | -0.14% | 29.38% |
| momentum_26 AND breakout_8 | -0.03% | -10.00% | -0.47% | -0.06% | 13.58% |
| momentum_26 + breakout_8 | 0.01% | -10.15% | -0.47% | -0.16% | 34.60% |
| momentum_26 AND reversion_12 | -0.09% | -2.98% | -0.47% | -0.01% | 2.87% |
| momentum_26 + reversion_12 | -0.70% | -7.75% | -0.47% | -0.17% | 36.82% |
| momentum_26 AND volume_26 | 0.06% | -2.02% | -0.47% | -0.01% | 1.83% |
| momentum_26 + volume_26 | -0.16% | -5.67% | -0.47% | -0.13% | 27.68% |
| breakout_8 AND reversion_12 | 0.00% | 0.00% | -0.47% | -0.00% | 0.00% |
| breakout_8 + reversion_12 | -0.97% | -13.08% | -0.47% | -0.11% | 23.38% |
| breakout_8 AND volume_26 | -0.54% | -3.42% | -0.47% | -0.01% | 2.09% |
| breakout_8 + volume_26 | -0.43% | -11.11% | -0.47% | -0.07% | 14.24% |
| reversion_12 AND volume_26 | 0.10% | -3.61% | -0.47% | -0.01% | 3.13% |
| reversion_12 + volume_26 | -1.14% | -9.30% | -0.47% | -0.08% | 16.45% |
| ema_12_26 | 1.60% | -0.93% | -0.47% | -0.24% | 50.91% |
| macd_12_26_9 | 2.93% | 0.37% | -0.47% | -0.13% | 28.20% |
| rsi_14_recovery | -0.65% | -5.14% | -0.47% | -0.01% | 2.87% |
| bollinger_20_reentry | -0.29% | -4.39% | -0.47% | -0.01% | 2.61% |
| donchian_20 | -0.29% | -5.59% | -0.47% | -0.03% | 6.27% |
| atr_14_breakout | -0.18% | -7.06% | -0.47% | -0.02% | 4.70% |
| session_vwap | 0.93% | -9.51% | -0.47% | -0.23% | 48.30% |
| obv_20 | 1.32% | -2.85% | -0.47% | -0.21% | 45.69% |
| stochastic_14_3_recovery | -0.32% | -12.12% | -0.47% | -0.04% | 7.83% |
| mfi_14_recovery | 0.20% | -3.92% | -0.47% | -0.01% | 2.61% |
| adx_14_trend | 0.11% | -3.20% | -0.47% | -0.17% | 37.08% |
| aroon_25_trend | -0.81% | -5.29% | -0.47% | -0.10% | 21.67% |
| cci_20_momentum | -1.32% | -8.12% | -0.47% | -0.09% | 20.37% |
| williams_14_recovery | 0.30% | -8.55% | -0.47% | -0.03% | 5.74% |
| cmf_20_accumulation | 0.44% | -6.48% | -0.47% | -0.11% | 23.24% |
| chaikin_3_10 | -0.53% | -6.99% | -0.47% | -0.17% | 36.29% |
| roc_10_momentum | -0.27% | -1.93% | -0.47% | -0.03% | 5.48% |
| trix_15_trend | 1.41% | -1.94% | -0.47% | -0.19% | 40.99% |
| keltner_20_breakout | -0.34% | -4.04% | -0.47% | -0.04% | 7.83% |
| opening_range_30m | 2.93% | -1.30% | -0.47% | -0.13% | 27.15% |

동일 구간·초기 자금, 종료 시 청산 비용 포함. 노출 맞춤은 사후 설명용이며 v2 실제 계좌 성과가 아닙니다.
[낙폭 분해·비용 영향·전체 구간](IWM/comparison.json)

[v1 전체 기록](IWM/accounts.json) · [v2 전체 기록](IWM/accounts-v2.json)

## DIA 계좌

| 모델 | 전략 | 평가액 USD | 손익 USD | 최근 매매·이유 |
|---|---|---:|---:|---|
| v1 | cash | 10000.00 | 0.00 | 대기 /  / 새 신호 대기 |
| v1 | buy_hold | 10058.10 | 58.10 | buy /  / buy_hold: prior completed bar target 100%; next bar open simulation |
| v1 | trend_8_26 | 10024.56 | 24.56 | buy /  / trend_8_26: prior completed bar target 100%; next bar open simulation |
| v1 | momentum_26 | 9857.66 | -142.34 | buy /  / momentum_26: prior completed bar target 100%; next bar open simulation |
| v1 | breakout_8 | 9448.12 | -551.88 | sell /  / breakout_8: prior completed bar target 0%; next bar open simulation |
| v1 | reversion_12 | 9846.27 | -153.73 | sell /  / reversion_12: prior completed bar target 0%; next bar open simulation |
| v1 | volume_26 | 9901.29 | -98.71 | sell /  / volume_26: prior completed bar target 0%; next bar open simulation |
| v1 | trend_8_26 AND momentum_26 | 9913.74 | -86.26 | buy /  / trend_8_26 AND momentum_26: prior completed bar target 100%; next bar open simulation |
| v1 | trend_8_26 + momentum_26 | 9940.83 | -59.17 | buy /  / trend_8_26 + momentum_26: prior completed bar target 100%; next bar open simulation |
| v1 | trend_8_26 AND breakout_8 | 9670.65 | -329.35 | sell /  / trend_8_26 AND breakout_8: prior completed bar target 0%; next bar open simulation |
| v1 | trend_8_26 + breakout_8 | 9771.15 | -228.85 | sell /  / trend_8_26 + breakout_8: prior completed bar target 50%; next bar open simulation |
| v1 | trend_8_26 AND reversion_12 | 9889.54 | -110.46 | sell /  / trend_8_26 AND reversion_12: prior completed bar target 0%; next bar open simulation |
| v1 | trend_8_26 + reversion_12 | 9934.84 | -65.16 | sell /  / trend_8_26 + reversion_12: prior completed bar target 50%; next bar open simulation |
| v1 | trend_8_26 AND volume_26 | 9974.09 | -25.91 | sell /  / trend_8_26 AND volume_26: prior completed bar target 0%; next bar open simulation |
| v1 | trend_8_26 + volume_26 | 9962.53 | -37.47 | sell /  / trend_8_26 + volume_26: prior completed bar target 50%; next bar open simulation |
| v1 | momentum_26 AND breakout_8 | 9576.92 | -423.08 | sell /  / momentum_26 AND breakout_8: prior completed bar target 0%; next bar open simulation |
| v1 | momentum_26 + breakout_8 | 9650.83 | -349.17 | sell /  / momentum_26 + breakout_8: prior completed bar target 50%; next bar open simulation |
| v1 | momentum_26 AND reversion_12 | 9889.56 | -110.44 | sell /  / momentum_26 AND reversion_12: prior completed bar target 0%; next bar open simulation |
| v1 | momentum_26 + reversion_12 | 9891.25 | -108.75 | sell /  / momentum_26 + reversion_12: prior completed bar target 50%; next bar open simulation |
| v1 | momentum_26 AND volume_26 | 9891.01 | -108.99 | sell /  / momentum_26 AND volume_26: prior completed bar target 0%; next bar open simulation |
| v1 | momentum_26 + volume_26 | 9899.11 | -100.89 | sell /  / momentum_26 + volume_26: prior completed bar target 50%; next bar open simulation |
| v1 | breakout_8 AND reversion_12 | 10000.00 | 0.00 | 대기 /  / 새 신호 대기 |
| v1 | breakout_8 + reversion_12 | 9664.25 | -335.75 | sell /  / breakout_8 + reversion_12: prior completed bar target 0%; next bar open simulation |
| v1 | breakout_8 AND volume_26 | 9947.52 | -52.48 | sell /  / breakout_8 AND volume_26: prior completed bar target 0%; next bar open simulation |
| v1 | breakout_8 + volume_26 | 9710.72 | -289.28 | sell /  / breakout_8 + volume_26: prior completed bar target 0%; next bar open simulation |
| v1 | reversion_12 AND volume_26 | 9970.42 | -29.58 | sell /  / reversion_12 AND volume_26: prior completed bar target 0%; next bar open simulation |
| v1 | reversion_12 + volume_26 | 9893.39 | -106.61 | sell /  / reversion_12 + volume_26: prior completed bar target 0%; next bar open simulation |
| v1 | ema_12_26 | 9912.05 | -87.95 | buy /  / EMA12 > EMA26; 조건 충족; EMA12=519.74, EMA26=519.585 |
| v1 | macd_12_26_9 | 9863.59 | -136.41 | sell /  / MACD > 신호선 그리고 MACD > 0; 조건 미충족; MACD=0.835411, signal9=0.838693 |
| v1 | rsi_14_recovery | 10000.00 | 0.00 | 대기 /  / 새 신호 대기 |
| v1 | bollinger_20_reentry | 9978.51 | -21.49 | sell /  / 직전 종가 < 직전 하단밴드, 현재 하단밴드 <= 종가 <= SMA20 (한 봉 목표); 조건 미충족; close=519.823, lower20=518.355, SMA20=521.612, previous_lower20=518.548 |
| v1 | donchian_20 | 9762.93 | -237.07 | sell /  / 종가 > 현재 봉을 제외한 직전 20봉 최고가; 조건 미충족; close=526.047, prior_high20=527.51 |
| v1 | atr_14_breakout | 9784.79 | -215.21 | buy /  / 종가 > 직전 종가 + 직전 ATR14 그리고 종가 > EMA26; 조건 충족; close=527.03, threshold=526.322, prior_ATR14=0.662293, EMA26=525.741 |
| v1 | session_vwap | 9867.15 | -132.85 | buy /  / 종가 > 뉴욕 거래일별 누적 전형가격 VWAP; 조건 충족; close=525.38, session_VWAP=524.679, session_volume=1.14471e+06 |
| v1 | obv_20 | 9872.72 | -127.28 | buy /  / OBV > OBV의 SMA20 그리고 종가 > EMA26; 조건 충족; OBV=-8.96454e+06, OBV_SMA20=-9.07774e+06, close=523.66, EMA26=523.184 |
| v1 | stochastic_14_3_recovery | 9740.52 | -259.48 | sell /  / 직전 %K14 < 20에서 %K14가 %D3 상향 돌파 (한 봉 목표); 조건 미충족; K14=29.7295, D3=26.3059, previous_K14=30.81, previous_D3=22.4321 |
| v1 | mfi_14_recovery | 9902.01 | -97.99 | sell /  / 직전 MFI14 < 20, 현재 MFI14 >= 20 (한 봉 목표); 조건 미충족; MFI14=29.4378, previous_MFI14=21.6288 |
| v1 | adx_14_trend | 9742.77 | -257.23 | buy /  / Wilder ADX14 >= 25 그리고 +DI14 > -DI14; 조건 충족; ADX14=31.1748, plus_DI14=35.8211, minus_DI14=27.1104 |
| v1 | aroon_25_trend | 9861.14 | -138.86 | buy /  / Aroon25 Up > 70 그리고 Down < 30 (동률이면 최신 극값); 조건 충족; Aroon_up=100, Aroon_down=28 |
| v1 | cci_20_momentum | 9833.71 | -166.29 | sell /  / CCI20 > 100 (전형가격·평균절대편차); 조건 미충족; CCI20=50.6478 |
| v1 | williams_14_recovery | 9773.54 | -226.46 | sell /  / 직전 Williams %R14 < -80, 현재 >= -80 (한 봉 목표); 조건 미충족; Williams_R14=-70.2705, previous_R14=-69.19 |
| v1 | cmf_20_accumulation | 9582.93 | -417.07 | buy /  / Chaikin Money Flow20 > 0.1; 조건 충족; CMF20=0.162227, volume20=1.04086e+06 |
| v1 | chaikin_3_10 | 9879.91 | -120.09 | buy /  / ADL의 EMA3 - EMA10 > 0 그리고 종가 > EMA26; 조건 충족; Chaikin3_10=17236.9, ADL=-1.53967e+07, close=523.66, EMA26=523.184 |
| v1 | roc_10_momentum | 9939.01 | -60.99 | sell /  / 10봉 ROC > 1% 그리고 종가 > EMA26; 조건 미충족; ROC10_percent=0.771645, close=523.68, EMA26=521.367 |
| v1 | trix_15_trend | 10014.10 | 14.10 | buy /  / 15봉 삼중 EMA의 1봉 변화율 TRIX > 0 그리고 종가 > EMA26; 조건 충족; TRIX15_percent=0.000473967, close=521.46, EMA26=519.585 |
| v1 | keltner_20_breakout | 9848.21 | -151.79 | sell /  / 종가 > EMA20 + 2 x Wilder ATR14; 조건 미충족; close=526.047, upper_Keltner=527.256, EMA20=525.982, ATR14=0.637339 |
| v1 | opening_range_30m | 9664.59 | -335.41 | buy /  / 뉴욕 09:30·09:45 두 완료 봉 최고가를 10:00 이후 종가가 돌파; 조건 충족; close=527.03, opening_high=526.85 |
| v2 | cash | 10000.00 | 0.00 | 대기 /  / 새 신호 대기 |
| v2 | buy_hold | 10182.70 | 182.70 | buy / partial / 직전 완료 봉 목표 비중 100%; 다음 봉 시가 가정 |
| v2 | trend_8_26 | 9955.63 | -44.37 | buy / partial / 직전 완료 봉 목표 비중 100%; 다음 봉 시가 가정 |
| v2 | momentum_26 | 9893.56 | -106.44 | buy / partial / 직전 완료 봉 목표 비중 100%; 다음 봉 시가 가정 |
| v2 | breakout_8 | 9012.91 | -987.09 | 중단: 손실 한도 / buy / partial / 직전 완료 봉 목표 비중 100%; 다음 봉 시가 가정 |
| v2 | reversion_12 | 9539.39 | -460.61 | sell / filled / 직전 완료 봉 목표 비중 0%; 다음 봉 시가 가정 |
| v2 | volume_26 | 9612.66 | -387.34 | sell / filled / 직전 완료 봉 목표 비중 0%; 다음 봉 시가 가정 |
| v2 | trend_8_26 AND momentum_26 | 9945.23 | -54.77 | buy / partial / 직전 완료 봉 목표 비중 100%; 다음 봉 시가 가정 |
| v2 | trend_8_26 + momentum_26 | 9924.68 | -75.32 | buy / partial / 직전 완료 봉 목표 비중 100%; 다음 봉 시가 가정 |
| v2 | trend_8_26 AND breakout_8 | 9352.73 | -647.27 | sell / filled / 직전 완료 봉 목표 비중 0%; 다음 봉 시가 가정 |
| v2 | trend_8_26 + breakout_8 | 9494.27 | -505.73 | sell / filled / 직전 완료 봉 목표 비중 50%; 다음 봉 시가 가정 |
| v2 | trend_8_26 AND reversion_12 | 9694.64 | -305.36 | sell / filled / 직전 완료 봉 목표 비중 0%; 다음 봉 시가 가정 |
| v2 | trend_8_26 + reversion_12 | 9744.86 | -255.14 | sell / filled / 직전 완료 봉 목표 비중 50%; 다음 봉 시가 가정 |
| v2 | trend_8_26 AND volume_26 | 9827.44 | -172.56 | sell / filled / 직전 완료 봉 목표 비중 0%; 다음 봉 시가 가정 |
| v2 | trend_8_26 + volume_26 | 9802.95 | -197.05 | sell / filled / 직전 완료 봉 목표 비중 50%; 다음 봉 시가 가정 |
| v2 | momentum_26 AND breakout_8 | 9249.69 | -750.31 | sell / filled / 직전 완료 봉 목표 비중 0%; 다음 봉 시가 가정 |
| v2 | momentum_26 + breakout_8 | 9425.06 | -574.94 | sell / filled / 직전 완료 봉 목표 비중 50%; 다음 봉 시가 가정 |
| v2 | momentum_26 AND reversion_12 | 9840.11 | -159.89 | sell / filled / 직전 완료 봉 목표 비중 0%; 다음 봉 시가 가정 |
| v2 | momentum_26 + reversion_12 | 9755.37 | -244.63 | sell / filled / 직전 완료 봉 목표 비중 50%; 다음 봉 시가 가정 |
| v2 | momentum_26 AND volume_26 | 9676.97 | -323.03 | sell / filled / 직전 완료 봉 목표 비중 0%; 다음 봉 시가 가정 |
| v2 | momentum_26 + volume_26 | 9813.69 | -186.31 | sell / filled / 직전 완료 봉 목표 비중 50%; 다음 봉 시가 가정 |
| v2 | breakout_8 AND reversion_12 | 10000.00 | 0.00 | 대기 /  / 새 신호 대기 |
| v2 | breakout_8 + reversion_12 | 9273.41 | -726.59 | sell / filled / 직전 완료 봉 목표 비중 0%; 다음 봉 시가 가정 |
| v2 | breakout_8 AND volume_26 | 9741.25 | -258.75 | sell / filled / 직전 완료 봉 목표 비중 0%; 다음 봉 시가 가정 |
| v2 | breakout_8 + volume_26 | 9328.91 | -671.09 | sell / filled / 직전 완료 봉 목표 비중 0%; 다음 봉 시가 가정 |
| v2 | reversion_12 AND volume_26 | 9966.44 | -33.56 | sell / filled / 직전 완료 봉 목표 비중 0%; 다음 봉 시가 가정 |
| v2 | reversion_12 + volume_26 | 9595.70 | -404.30 | sell / filled / 직전 완료 봉 목표 비중 0%; 다음 봉 시가 가정 |
| v2 | ema_12_26 | 9907.09 | -92.91 | buy / partial / EMA12 > EMA26; 조건 충족; EMA12=519.74, EMA26=519.585; 직전 완료 봉 목표를 다음 봉 시가에 모의 적용 |
| v2 | macd_12_26_9 | 9855.70 | -144.30 | sell / filled / MACD > 신호선 그리고 MACD > 0; 조건 미충족; MACD=0.835411, signal9=0.838693; 직전 완료 봉 목표를 다음 봉 시가에 모의 적용 |
| v2 | rsi_14_recovery | 10000.00 | 0.00 | 대기 /  / 새 신호 대기 |
| v2 | bollinger_20_reentry | 9976.52 | -23.48 | sell / filled / 직전 종가 < 직전 하단밴드, 현재 하단밴드 <= 종가 <= SMA20 (한 봉 목표); 조건 미충족; close=519.823, lower20=518.355, SMA20=521.612, previous_lower20=518.548; 직전 완료 봉 목표를 다음 봉 시가에 모의 적용 |
| v2 | donchian_20 | 9753.17 | -246.83 | sell / filled / 종가 > 현재 봉을 제외한 직전 20봉 최고가; 조건 미충족; close=526.047, prior_high20=527.51; 직전 완료 봉 목표를 다음 봉 시가에 모의 적용 |
| v2 | atr_14_breakout | 9774.03 | -225.97 | buy / partial / 종가 > 직전 종가 + 직전 ATR14 그리고 종가 > EMA26; 조건 충족; close=527.03, threshold=526.322, prior_ATR14=0.662293, EMA26=525.741; 직전 완료 봉 목표를 다음 봉 시가에 모의 적용 |
| v2 | session_vwap | 9856.31 | -143.69 | buy / partial / 종가 > 뉴욕 거래일별 누적 전형가격 VWAP; 조건 충족; close=525.38, session_VWAP=524.679, session_volume=1.14471e+06; 직전 완료 봉 목표를 다음 봉 시가에 모의 적용 |
| v2 | obv_20 | 9863.83 | -136.17 | buy / partial / OBV > OBV의 SMA20 그리고 종가 > EMA26; 조건 충족; OBV=-9.15207e+06, OBV_SMA20=-9.26528e+06, close=523.66, EMA26=523.184; 직전 완료 봉 목표를 다음 봉 시가에 모의 적용 |
| v2 | stochastic_14_3_recovery | 9726.89 | -273.11 | sell / filled / 직전 %K14 < 20에서 %K14가 %D3 상향 돌파 (한 봉 목표); 조건 미충족; K14=29.7295, D3=26.3059, previous_K14=30.81, previous_D3=22.4321; 직전 완료 봉 목표를 다음 봉 시가에 모의 적용 |
| v2 | mfi_14_recovery | 9896.07 | -103.93 | sell / filled / 직전 MFI14 < 20, 현재 MFI14 >= 20 (한 봉 목표); 조건 미충족; MFI14=29.4378, previous_MFI14=21.6288; 직전 완료 봉 목표를 다음 봉 시가에 모의 적용 |
| v2 | adx_14_trend | 9734.01 | -265.99 | buy / partial / Wilder ADX14 >= 25 그리고 +DI14 > -DI14; 조건 충족; ADX14=31.1748, plus_DI14=35.8211, minus_DI14=27.1104; 직전 완료 봉 목표를 다음 봉 시가에 모의 적용 |
| v2 | aroon_25_trend | 9852.27 | -147.73 | buy / partial / Aroon25 Up > 70 그리고 Down < 30 (동률이면 최신 극값); 조건 충족; Aroon_up=100, Aroon_down=28; 직전 완료 봉 목표를 다음 봉 시가에 모의 적용 |
| v2 | cci_20_momentum | 9823.88 | -176.12 | sell / filled / CCI20 > 100 (전형가격·평균절대편차); 조건 미충족; CCI20=50.6478; 직전 완료 봉 목표를 다음 봉 시가에 모의 적용 |
| v2 | williams_14_recovery | 9761.82 | -238.18 | sell / filled / 직전 Williams %R14 < -80, 현재 >= -80 (한 봉 목표); 조건 미충족; Williams_R14=-70.2705, previous_R14=-69.19; 직전 완료 봉 목표를 다음 봉 시가에 모의 적용 |
| v2 | cmf_20_accumulation | 9564.74 | -435.26 | buy / partial / Chaikin Money Flow20 > 0.1; 조건 충족; CMF20=0.162227, volume20=1.04086e+06; 직전 완료 봉 목표를 다음 봉 시가에 모의 적용 |
| v2 | chaikin_3_10 | 9871.02 | -128.98 | buy / partial / ADL의 EMA3 - EMA10 > 0 그리고 종가 > EMA26; 조건 충족; Chaikin3_10=17236.9, ADL=-1.59365e+07, close=523.66, EMA26=523.184; 직전 완료 봉 목표를 다음 봉 시가에 모의 적용 |
| v2 | roc_10_momentum | 9937.03 | -62.97 | sell / filled / 10봉 ROC > 1% 그리고 종가 > EMA26; 조건 미충족; ROC10_percent=0.771645, close=523.68, EMA26=521.367; 직전 완료 봉 목표를 다음 봉 시가에 모의 적용 |
| v2 | trix_15_trend | 10011.10 | 11.10 | buy / partial / 15봉 삼중 EMA의 1봉 변화율 TRIX > 0 그리고 종가 > EMA26; 조건 충족; TRIX15_percent=0.000473967, close=521.46, EMA26=519.585; 직전 완료 봉 목표를 다음 봉 시가에 모의 적용 |
| v2 | keltner_20_breakout | 9840.34 | -159.66 | sell / filled / 종가 > EMA20 + 2 x Wilder ATR14; 조건 미충족; close=526.047, upper_Keltner=527.256, EMA20=525.982, ATR14=0.637339; 직전 완료 봉 목표를 다음 봉 시가에 모의 적용 |
| v2 | opening_range_30m | 9650.11 | -349.89 | buy / partial / 뉴욕 09:30·09:45 두 완료 봉 최고가를 10:00 이후 종가가 돌파; 조건 충족; close=527.03, opening_high=526.85; 직전 완료 봉 목표를 다음 봉 시가에 모의 적용 |

### 같은 기간의 비용·노출 비교 (사후 연구)

| 전략 | 비용 전 | 비용 후 | 100% 보유 | 같은 평균 노출 보유 | 평균 노출 |
|---|---:|---:|---:|---:|---:|
| cash | 0.00% | 0.00% | 3.71% | 0.00% | 0.00% |
| buy_hold | 4.15% | 3.71% | 3.71% | 3.71% | 100.00% |
| trend_8_26 | 3.50% | -0.34% | 3.71% | 2.41% | 65.27% |
| momentum_26 | 1.56% | -2.62% | 3.71% | 2.23% | 60.57% |
| breakout_8 | 0.27% | -18.04% | 3.71% | 0.98% | 26.63% |
| reversion_12 | 0.69% | -7.03% | 3.71% | 0.66% | 18.02% |
| volume_26 | 1.05% | -7.48% | 3.71% | 0.34% | 9.40% |
| trend_8_26 AND momentum_26 | 3.16% | -1.09% | 3.71% | 2.04% | 55.35% |
| trend_8_26 + momentum_26 | 2.53% | -1.49% | 3.71% | 2.32% | 62.93% |
| trend_8_26 AND breakout_8 | 1.24% | -12.23% | 3.71% | 0.69% | 18.80% |
| trend_8_26 + breakout_8 | 1.87% | -9.05% | 3.71% | 1.69% | 45.96% |
| trend_8_26 AND reversion_12 | 0.65% | -4.30% | 3.71% | 0.24% | 6.53% |
| trend_8_26 + reversion_12 | 2.09% | -3.55% | 3.71% | 1.53% | 41.65% |
| trend_8_26 AND volume_26 | 1.66% | -3.75% | 3.71% | 0.20% | 5.48% |
| trend_8_26 + volume_26 | 2.27% | -3.78% | 3.71% | 1.37% | 37.34% |
| momentum_26 AND breakout_8 | -0.16% | -13.81% | 3.71% | 0.74% | 20.10% |
| momentum_26 + breakout_8 | 0.92% | -10.47% | 3.71% | 1.60% | 43.61% |
| momentum_26 AND reversion_12 | -0.06% | -2.95% | 3.71% | 0.18% | 4.96% |
| momentum_26 + reversion_12 | 1.13% | -4.06% | 3.71% | 1.44% | 39.30% |
| momentum_26 AND volume_26 | 0.11% | -6.00% | 3.71% | 0.21% | 5.74% |
| momentum_26 + volume_26 | 1.31% | -4.48% | 3.71% | 1.28% | 34.99% |
| breakout_8 AND reversion_12 | 0.00% | 0.00% | 3.71% | 0.00% | 0.00% |
| breakout_8 + reversion_12 | 0.48% | -12.35% | 3.71% | 0.82% | 22.33% |
| breakout_8 AND volume_26 | -0.45% | -4.15% | 3.71% | 0.12% | 3.39% |
| breakout_8 + volume_26 | 0.66% | -12.01% | 3.71% | 0.66% | 18.02% |
| reversion_12 AND volume_26 | 0.94% | -1.99% | 3.71% | 0.08% | 2.09% |
| reversion_12 + volume_26 | 0.87% | -7.07% | 3.71% | 0.50% | 13.71% |
| ema_12_26 | 1.34% | -1.18% | 3.71% | 2.22% | 60.31% |
| macd_12_26_9 | 2.33% | -1.47% | 3.71% | 1.22% | 33.16% |
| rsi_14_recovery | 0.16% | -1.09% | 3.71% | 0.03% | 0.78% |
| bollinger_20_reentry | 0.34% | -2.16% | 3.71% | 0.06% | 1.57% |
| donchian_20 | 0.16% | -7.52% | 3.71% | 0.39% | 10.70% |
| atr_14_breakout | -0.69% | -8.69% | 3.71% | 0.23% | 6.27% |
| session_vwap | 3.27% | -3.85% | 3.71% | 2.15% | 58.49% |
| obv_20 | 1.73% | -6.07% | 3.71% | 1.90% | 51.70% |
| stochastic_14_3_recovery | 1.35% | -9.13% | 3.71% | 0.25% | 6.79% |
| mfi_14_recovery | 0.37% | -2.95% | 3.71% | 0.08% | 2.09% |
| adx_14_trend | 0.02% | -4.49% | 3.71% | 1.23% | 33.42% |
| aroon_25_trend | 1.54% | -2.64% | 3.71% | 1.01% | 27.68% |
| cci_20_momentum | 1.14% | -5.43% | 3.71% | 1.06% | 28.98% |
| williams_14_recovery | 1.55% | -5.84% | 3.71% | 0.17% | 4.70% |
| cmf_20_accumulation | 1.13% | -8.57% | 3.71% | 1.34% | 36.55% |
| chaikin_3_10 | 2.87% | -6.61% | 3.71% | 1.96% | 53.26% |
| roc_10_momentum | -0.07% | -0.90% | 3.71% | 0.08% | 2.09% |
| trix_15_trend | 1.46% | -1.89% | 3.71% | 2.01% | 54.57% |
| keltner_20_breakout | 0.60% | -6.72% | 3.71% | 0.73% | 19.84% |
| opening_range_30m | 1.44% | -5.55% | 3.71% | 1.14% | 31.07% |

동일 구간·초기 자금, 종료 시 청산 비용 포함. 노출 맞춤은 사후 설명용이며 v2 실제 계좌 성과가 아닙니다.
[낙폭 분해·비용 영향·전체 구간](DIA/comparison.json)

[v1 전체 기록](DIA/accounts.json) · [v2 전체 기록](DIA/accounts-v2.json)

## MSFT 계좌

| 모델 | 전략 | 평가액 USD | 손익 USD | 최근 매매·이유 |
|---|---|---:|---:|---|
| v1 | cash | 10000.00 | 0.00 | 대기 /  / 새 신호 대기 |
| v1 | buy_hold | 9813.10 | -186.90 | buy /  / buy_hold: prior completed bar target 100%; next bar open simulation |
| v1 | trend_8_26 | 9547.95 | -452.05 | buy /  / trend_8_26: prior completed bar target 100%; next bar open simulation |
| v1 | momentum_26 | 9360.04 | -639.96 | buy /  / momentum_26: prior completed bar target 100%; next bar open simulation |
| v1 | breakout_8 | 9607.09 | -392.91 | sell /  / breakout_8: prior completed bar target 0%; next bar open simulation |
| v1 | reversion_12 | 9534.84 | -465.16 | sell /  / reversion_12: prior completed bar target 0%; next bar open simulation |
| v1 | volume_26 | 9722.84 | -277.16 | sell /  / volume_26: prior completed bar target 0%; next bar open simulation |
| v1 | trend_8_26 AND momentum_26 | 9490.91 | -509.09 | buy /  / trend_8_26 AND momentum_26: prior completed bar target 100%; next bar open simulation |
| v1 | trend_8_26 + momentum_26 | 9491.38 | -508.62 | buy /  / trend_8_26 + momentum_26: prior completed bar target 100%; next bar open simulation |
| v1 | trend_8_26 AND breakout_8 | 9775.38 | -224.62 | sell /  / trend_8_26 AND breakout_8: prior completed bar target 0%; next bar open simulation |
| v1 | trend_8_26 + breakout_8 | 9616.05 | -383.95 | sell /  / trend_8_26 + breakout_8: prior completed bar target 50%; next bar open simulation |
| v1 | trend_8_26 AND reversion_12 | 9609.49 | -390.51 | sell /  / trend_8_26 AND reversion_12: prior completed bar target 0%; next bar open simulation |
| v1 | trend_8_26 + reversion_12 | 9560.39 | -439.61 | sell /  / trend_8_26 + reversion_12: prior completed bar target 50%; next bar open simulation |
| v1 | trend_8_26 AND volume_26 | 9894.93 | -105.07 | sell /  / trend_8_26 AND volume_26: prior completed bar target 0%; next bar open simulation |
| v1 | trend_8_26 + volume_26 | 9635.12 | -364.88 | sell /  / trend_8_26 + volume_26: prior completed bar target 50%; next bar open simulation |
| v1 | momentum_26 AND breakout_8 | 9738.76 | -261.24 | sell /  / momentum_26 AND breakout_8: prior completed bar target 0%; next bar open simulation |
| v1 | momentum_26 + breakout_8 | 9501.95 | -498.05 | buy /  / momentum_26 + breakout_8: prior completed bar target 50%; next bar open simulation |
| v1 | momentum_26 AND reversion_12 | 9649.76 | -350.24 | sell /  / momentum_26 AND reversion_12: prior completed bar target 0%; next bar open simulation |
| v1 | momentum_26 + reversion_12 | 9484.75 | -515.25 | sell /  / momentum_26 + reversion_12: prior completed bar target 50%; next bar open simulation |
| v1 | momentum_26 AND volume_26 | 9830.16 | -169.84 | sell /  / momentum_26 AND volume_26: prior completed bar target 0%; next bar open simulation |
| v1 | momentum_26 + volume_26 | 9539.89 | -460.11 | buy /  / momentum_26 + volume_26: prior completed bar target 50%; next bar open simulation |
| v1 | breakout_8 AND reversion_12 | 10000.00 | 0.00 | 대기 /  / 새 신호 대기 |
| v1 | breakout_8 + reversion_12 | 9589.88 | -410.12 | sell /  / breakout_8 + reversion_12: prior completed bar target 0%; next bar open simulation |
| v1 | breakout_8 AND volume_26 | 9953.19 | -46.81 | sell /  / breakout_8 AND volume_26: prior completed bar target 0%; next bar open simulation |
| v1 | breakout_8 + volume_26 | 9683.92 | -316.08 | sell /  / breakout_8 + volume_26: prior completed bar target 0%; next bar open simulation |
| v1 | reversion_12 AND volume_26 | 9863.28 | -136.72 | sell /  / reversion_12 AND volume_26: prior completed bar target 0%; next bar open simulation |
| v1 | reversion_12 + volume_26 | 9647.58 | -352.42 | sell /  / reversion_12 + volume_26: prior completed bar target 0%; next bar open simulation |
| v1 | ema_12_26 | 9554.89 | -445.11 | buy /  / EMA12 > EMA26; 조건 충족; EMA12=531.547, EMA26=531.449 |
| v1 | macd_12_26_9 | 9700.06 | -299.94 | sell /  / MACD > 신호선 그리고 MACD > 0; 조건 미충족; MACD=0.164536, signal9=0.206445 |
| v1 | rsi_14_recovery | 9957.14 | -42.86 | sell /  / 직전 RSI14 < 30, 현재 RSI14 >= 30 (한 봉 목표); 조건 미충족; RSI14=45.5102, previous_RSI14=37.5844 |
| v1 | bollinger_20_reentry | 9813.80 | -186.20 | sell /  / 직전 종가 < 직전 하단밴드, 현재 하단밴드 <= 종가 <= SMA20 (한 봉 목표); 조건 미충족; close=529.335, lower20=528.85, SMA20=531.508, previous_lower20=529.166 |
| v1 | donchian_20 | 9912.16 | -87.84 | sell /  / 종가 > 현재 봉을 제외한 직전 20봉 최고가; 조건 미충족; close=534.52, prior_high20=535.44 |
| v1 | atr_14_breakout | 9915.10 | -84.90 | sell /  / 종가 > 직전 종가 + 직전 ATR14 그리고 종가 > EMA26; 조건 미충족; close=533.975, threshold=536.307, prior_ATR14=2.16203, EMA26=530.521 |
| v1 | session_vwap | 9833.61 | -166.39 | buy /  / 종가 > 뉴욕 거래일별 누적 전형가격 VWAP; 조건 충족; close=530.964, session_VWAP=530.832, session_volume=8.43578e+06 |
| v1 | obv_20 | 9601.28 | -398.72 | buy /  / OBV > OBV의 SMA20 그리고 종가 > EMA26; 조건 충족; OBV=9.21157e+07, OBV_SMA20=9.09825e+07, close=532.255, EMA26=531.892 |
| v1 | stochastic_14_3_recovery | 9763.07 | -236.93 | sell /  / 직전 %K14 < 20에서 %K14가 %D3 상향 돌파 (한 봉 목표); 조건 미충족; K14=68.5623, D3=40.984, previous_K14=46.1286, previous_D3=42.0035 |
| v1 | mfi_14_recovery | 9972.58 | -27.42 | sell /  / 직전 MFI14 < 20, 현재 MFI14 >= 20 (한 봉 목표); 조건 미충족; MFI14=53.413, previous_MFI14=44.3372 |
| v1 | adx_14_trend | 9883.62 | -116.38 | sell /  / Wilder ADX14 >= 25 그리고 +DI14 > -DI14; 조건 미충족; ADX14=23.6824, plus_DI14=22.3066, minus_DI14=19.9214 |
| v1 | aroon_25_trend | 9765.69 | -234.31 | sell /  / Aroon25 Up > 70 그리고 Down < 30 (동률이면 최신 극값); 조건 미충족; Aroon_up=68, Aroon_down=8 |
| v1 | cci_20_momentum | 9912.64 | -87.36 | sell /  / CCI20 > 100 (전형가격·평균절대편차); 조건 미충족; CCI20=96.8192 |
| v1 | williams_14_recovery | 9726.16 | -273.84 | sell /  / 직전 Williams %R14 < -80, 현재 >= -80 (한 봉 목표); 조건 미충족; Williams_R14=-31.4377, previous_R14=-53.8714 |
| v1 | cmf_20_accumulation | 9672.55 | -327.45 | buy /  / Chaikin Money Flow20 > 0.1; 조건 충족; CMF20=0.135675, volume20=5.00055e+06 |
| v1 | chaikin_3_10 | 9639.48 | -360.52 | buy /  / ADL의 EMA3 - EMA10 > 0 그리고 종가 > EMA26; 조건 충족; Chaikin3_10=182478, ADL=1.17674e+08, close=532.255, EMA26=531.892 |
| v1 | roc_10_momentum | 9959.43 | -40.57 | sell /  / 10봉 ROC > 1% 그리고 종가 > EMA26; 조건 미충족; ROC10_percent=0.454191, close=534.125, EMA26=532.186 |
| v1 | trix_15_trend | 9621.00 | -379.00 | buy /  / 15봉 삼중 EMA의 1봉 변화율 TRIX > 0 그리고 종가 > EMA26; 조건 충족; TRIX15_percent=0.00566573, close=532.255, EMA26=531.892 |
| v1 | keltner_20_breakout | 9958.78 | -41.22 | sell /  / 종가 > EMA20 + 2 x Wilder ATR14; 조건 미충족; close=533.975, upper_Keltner=534.357, EMA20=530.111, ATR14=2.12332 |
| v1 | opening_range_30m | 9653.42 | -346.58 | buy /  / 뉴욕 09:30·09:45 두 완료 봉 최고가를 10:00 이후 종가가 돌파; 조건 충족; close=531.545, opening_high=531.48 |
| v2 | cash | 10000.00 | 0.00 | 대기 /  / 새 신호 대기 |
| v2 | buy_hold | 9866.64 | -133.36 | buy / partial / 직전 완료 봉 목표 비중 100%; 다음 봉 시가 가정 |
| v2 | trend_8_26 | 9481.67 | -518.33 | buy / partial / 직전 완료 봉 목표 비중 100%; 다음 봉 시가 가정 |
| v2 | momentum_26 | 9390.52 | -609.48 | buy / partial / 직전 완료 봉 목표 비중 100%; 다음 봉 시가 가정 |
| v2 | breakout_8 | 9393.76 | -606.24 | sell / filled / 직전 완료 봉 목표 비중 0%; 다음 봉 시가 가정 |
| v2 | reversion_12 | 9156.54 | -843.46 | sell / filled / 직전 완료 봉 목표 비중 0%; 다음 봉 시가 가정 |
| v2 | volume_26 | 9406.85 | -593.15 | sell / filled / 직전 완료 봉 목표 비중 0%; 다음 봉 시가 가정 |
| v2 | trend_8_26 AND momentum_26 | 9383.69 | -616.31 | buy / partial / 직전 완료 봉 목표 비중 100%; 다음 봉 시가 가정 |
| v2 | trend_8_26 + momentum_26 | 9475.91 | -524.09 | buy / partial / 직전 완료 봉 목표 비중 100%; 다음 봉 시가 가정 |
| v2 | trend_8_26 AND breakout_8 | 9413.36 | -586.64 | sell / filled / 직전 완료 봉 목표 비중 0%; 다음 봉 시가 가정 |
| v2 | trend_8_26 + breakout_8 | 9497.63 | -502.37 | sell / filled / 직전 완료 봉 목표 비중 50%; 다음 봉 시가 가정 |
| v2 | trend_8_26 AND reversion_12 | 9502.09 | -497.91 | sell / filled / 직전 완료 봉 목표 비중 0%; 다음 봉 시가 가정 |
| v2 | trend_8_26 + reversion_12 | 9336.84 | -663.16 | sell / filled / 직전 완료 봉 목표 비중 50%; 다음 봉 시가 가정 |
| v2 | trend_8_26 AND volume_26 | 9838.23 | -161.77 | sell / filled / 직전 완료 봉 목표 비중 0%; 다음 봉 시가 가정 |
| v2 | trend_8_26 + volume_26 | 9463.95 | -536.05 | sell / filled / 직전 완료 봉 목표 비중 50%; 다음 봉 시가 가정 |
| v2 | momentum_26 AND breakout_8 | 9527.07 | -472.93 | sell / filled / 직전 완료 봉 목표 비중 0%; 다음 봉 시가 가정 |
| v2 | momentum_26 + breakout_8 | 9412.15 | -587.85 | buy / filled / 직전 완료 봉 목표 비중 50%; 다음 봉 시가 가정 |
| v2 | momentum_26 AND reversion_12 | 9475.12 | -524.88 | sell / filled / 직전 완료 봉 목표 비중 0%; 다음 봉 시가 가정 |
| v2 | momentum_26 + reversion_12 | 9311.45 | -688.55 | sell / filled / 직전 완료 봉 목표 비중 50%; 다음 봉 시가 가정 |
| v2 | momentum_26 AND volume_26 | 9695.84 | -304.16 | sell / filled / 직전 완료 봉 목표 비중 0%; 다음 봉 시가 가정 |
| v2 | momentum_26 + volume_26 | 9418.54 | -581.46 | buy / filled / 직전 완료 봉 목표 비중 50%; 다음 봉 시가 가정 |
| v2 | breakout_8 AND reversion_12 | 10000.00 | 0.00 | 대기 /  / 새 신호 대기 |
| v2 | breakout_8 + reversion_12 | 9313.01 | -686.99 | sell / filled / 직전 완료 봉 목표 비중 0%; 다음 봉 시가 가정 |
| v2 | breakout_8 AND volume_26 | 9890.09 | -109.91 | sell / filled / 직전 완료 봉 목표 비중 0%; 다음 봉 시가 가정 |
| v2 | breakout_8 + volume_26 | 9439.67 | -560.33 | sell / filled / 직전 완료 봉 목표 비중 0%; 다음 봉 시가 가정 |
| v2 | reversion_12 AND volume_26 | 9622.80 | -377.20 | sell / filled / 직전 완료 봉 목표 비중 0%; 다음 봉 시가 가정 |
| v2 | reversion_12 + volume_26 | 9300.11 | -699.89 | sell / filled / 직전 완료 봉 목표 비중 0%; 다음 봉 시가 가정 |
| v2 | ema_12_26 | 9548.20 | -451.80 | buy / partial / EMA12 > EMA26; 조건 충족; EMA12=531.547, EMA26=531.449; 직전 완료 봉 목표를 다음 봉 시가에 모의 적용 |
| v2 | macd_12_26_9 | 9692.30 | -307.70 | sell / filled / MACD > 신호선 그리고 MACD > 0; 조건 미충족; MACD=0.164536, signal9=0.206445; 직전 완료 봉 목표를 다음 봉 시가에 모의 적용 |
| v2 | rsi_14_recovery | 9951.17 | -48.83 | sell / filled / 직전 RSI14 < 30, 현재 RSI14 >= 30 (한 봉 목표); 조건 미충족; RSI14=45.5102, previous_RSI14=37.5844; 직전 완료 봉 목표를 다음 봉 시가에 모의 적용 |
| v2 | bollinger_20_reentry | 9805.95 | -194.05 | sell / filled / 직전 종가 < 직전 하단밴드, 현재 하단밴드 <= 종가 <= SMA20 (한 봉 목표); 조건 미충족; close=529.335, lower20=528.85, SMA20=531.508, previous_lower20=529.166; 직전 완료 봉 목표를 다음 봉 시가에 모의 적용 |
| v2 | donchian_20 | 9908.19 | -91.81 | sell / filled / 종가 > 현재 봉을 제외한 직전 20봉 최고가; 조건 미충족; close=534.52, prior_high20=535.44; 직전 완료 봉 목표를 다음 봉 시가에 모의 적용 |
| v2 | atr_14_breakout | 9911.14 | -88.86 | sell / filled / 종가 > 직전 종가 + 직전 ATR14 그리고 종가 > EMA26; 조건 미충족; close=533.975, threshold=536.307, prior_ATR14=2.16203, EMA26=530.521; 직전 완료 봉 목표를 다음 봉 시가에 모의 적용 |
| v2 | session_vwap | 9824.76 | -175.24 | buy / partial / 종가 > 뉴욕 거래일별 누적 전형가격 VWAP; 조건 충족; close=530.964, session_VWAP=530.832, session_volume=8.43578e+06; 직전 완료 봉 목표를 다음 봉 시가에 모의 적용 |
| v2 | obv_20 | 9584.97 | -415.03 | buy / partial / OBV > OBV의 SMA20 그리고 종가 > EMA26; 조건 충족; OBV=9.21157e+07, OBV_SMA20=9.09825e+07, close=532.255, EMA26=531.892; 직전 완료 봉 목표를 다음 봉 시가에 모의 적용 |
| v2 | stochastic_14_3_recovery | 9751.36 | -248.64 | sell / filled / 직전 %K14 < 20에서 %K14가 %D3 상향 돌파 (한 봉 목표); 조건 미충족; K14=68.5623, D3=40.984, previous_K14=46.1286, previous_D3=42.0035; 직전 완료 봉 목표를 다음 봉 시가에 모의 적용 |
| v2 | mfi_14_recovery | 9968.59 | -31.41 | sell / filled / 직전 MFI14 < 20, 현재 MFI14 >= 20 (한 봉 목표); 조건 미충족; MFI14=53.413, previous_MFI14=44.3372; 직전 완료 봉 목표를 다음 봉 시가에 모의 적용 |
| v2 | adx_14_trend | 9879.67 | -120.33 | sell / filled / Wilder ADX14 >= 25 그리고 +DI14 > -DI14; 조건 미충족; ADX14=23.6824, plus_DI14=22.3066, minus_DI14=19.9214; 직전 완료 봉 목표를 다음 봉 시가에 모의 적용 |
| v2 | aroon_25_trend | 9759.83 | -240.17 | sell / filled / Aroon25 Up > 70 그리고 Down < 30 (동률이면 최신 극값); 조건 미충족; Aroon_up=68, Aroon_down=8; 직전 완료 봉 목표를 다음 봉 시가에 모의 적용 |
| v2 | cci_20_momentum | 9906.70 | -93.30 | sell / filled / CCI20 > 100 (전형가격·평균절대편차); 조건 미충족; CCI20=96.8192; 직전 완료 봉 목표를 다음 봉 시가에 모의 적용 |
| v2 | williams_14_recovery | 9714.49 | -285.51 | sell / filled / 직전 Williams %R14 < -80, 현재 >= -80 (한 봉 목표); 조건 미충족; Williams_R14=-31.4377, previous_R14=-53.8714; 직전 완료 봉 목표를 다음 봉 시가에 모의 적용 |
| v2 | cmf_20_accumulation | 9665.78 | -334.22 | buy / partial / Chaikin Money Flow20 > 0.1; 조건 충족; CMF20=0.135675, volume20=5.00055e+06; 직전 완료 봉 목표를 다음 봉 시가에 모의 적용 |
| v2 | chaikin_3_10 | 9625.03 | -374.97 | buy / partial / ADL의 EMA3 - EMA10 > 0 그리고 종가 > EMA26; 조건 충족; Chaikin3_10=182478, ADL=1.17674e+08, close=532.255, EMA26=531.892; 직전 완료 봉 목표를 다음 봉 시가에 모의 적용 |
| v2 | roc_10_momentum | 9957.44 | -42.56 | sell / filled / 10봉 ROC > 1% 그리고 종가 > EMA26; 조건 미충족; ROC10_percent=0.454191, close=534.125, EMA26=532.186; 직전 완료 봉 목표를 다음 봉 시가에 모의 적용 |
| v2 | trix_15_trend | 9614.26 | -385.74 | buy / partial / 15봉 삼중 EMA의 1봉 변화율 TRIX > 0 그리고 종가 > EMA26; 조건 충족; TRIX15_percent=0.00566573, close=532.255, EMA26=531.892; 직전 완료 봉 목표를 다음 봉 시가에 모의 적용 |
| v2 | keltner_20_breakout | 9956.78 | -43.22 | sell / filled / 종가 > EMA20 + 2 x Wilder ATR14; 조건 미충족; close=533.975, upper_Keltner=534.357, EMA20=530.111, ATR14=2.12332; 직전 완료 봉 목표를 다음 봉 시가에 모의 적용 |
| v2 | opening_range_30m | 9646.67 | -353.33 | buy / partial / 뉴욕 09:30·09:45 두 완료 봉 최고가를 10:00 이후 종가가 돌파; 조건 충족; close=531.545, opening_high=531.48; 직전 완료 봉 목표를 다음 봉 시가에 모의 적용 |

### 같은 기간의 비용·노출 비교 (사후 연구)

| 전략 | 비용 전 | 비용 후 | 100% 보유 | 같은 평균 노출 보유 | 평균 노출 |
|---|---:|---:|---:|---:|---:|
| cash | 0.00% | 0.00% | 3.00% | 0.00% | 0.00% |
| buy_hold | 3.44% | 3.00% | 3.00% | 3.00% | 100.00% |
| trend_8_26 | -1.29% | -4.95% | 3.00% | 1.71% | 57.70% |
| momentum_26 | -0.56% | -7.80% | 3.00% | 1.66% | 56.14% |
| breakout_8 | 6.33% | -8.59% | 3.00% | 0.60% | 20.63% |
| reversion_12 | -4.69% | -13.83% | 3.00% | 0.74% | 25.07% |
| volume_26 | 0.69% | -7.42% | 3.00% | 0.24% | 8.36% |
| trend_8_26 AND momentum_26 | -2.20% | -8.56% | 3.00% | 1.48% | 49.87% |
| trend_8_26 + momentum_26 | -0.92% | -5.98% | 3.00% | 1.69% | 56.92% |
| trend_8_26 AND breakout_8 | 0.45% | -9.56% | 3.00% | 0.36% | 12.27% |
| trend_8_26 + breakout_8 | 2.47% | -5.99% | 3.00% | 1.15% | 39.17% |
| trend_8_26 AND reversion_12 | -2.09% | -8.07% | 3.00% | 0.21% | 7.31% |
| trend_8_26 + reversion_12 | -2.99% | -9.12% | 3.00% | 1.22% | 41.39% |
| trend_8_26 AND volume_26 | 2.59% | -0.80% | 3.00% | 0.08% | 2.87% |
| trend_8_26 + volume_26 | -0.29% | -5.80% | 3.00% | 0.97% | 33.03% |
| momentum_26 AND breakout_8 | 2.75% | -7.88% | 3.00% | 0.37% | 12.79% |
| momentum_26 + breakout_8 | 2.84% | -7.61% | 3.00% | 1.13% | 38.39% |
| momentum_26 AND reversion_12 | -3.22% | -9.51% | 3.00% | 0.27% | 9.14% |
| momentum_26 + reversion_12 | -2.63% | -10.49% | 3.00% | 1.20% | 40.61% |
| momentum_26 AND volume_26 | 1.17% | -3.40% | 3.00% | 0.10% | 3.39% |
| momentum_26 + volume_26 | 0.08% | -7.22% | 3.00% | 0.95% | 32.25% |
| breakout_8 AND reversion_12 | 0.00% | 0.00% | 3.00% | 0.00% | 0.00% |
| breakout_8 + reversion_12 | 0.69% | -10.50% | 3.00% | 0.67% | 22.85% |
| breakout_8 AND volume_26 | 2.04% | -0.50% | 3.00% | 0.05% | 1.83% |
| breakout_8 + volume_26 | 3.48% | -7.43% | 3.00% | 0.42% | 14.50% |
| reversion_12 AND volume_26 | -2.76% | -6.37% | 3.00% | 0.11% | 3.66% |
| reversion_12 + volume_26 | -2.03% | -10.50% | 3.00% | 0.49% | 16.72% |
| ema_12_26 | -0.86% | -4.94% | 3.00% | 1.70% | 57.44% |
| macd_12_26_9 | -0.64% | -5.92% | 3.00% | 1.01% | 34.46% |
| rsi_14_recovery | 0.31% | -2.19% | 3.00% | 0.05% | 1.57% |
| bollinger_20_reentry | -0.93% | -4.21% | 3.00% | 0.06% | 2.09% |
| donchian_20 | 1.05% | -4.32% | 3.00% | 0.12% | 4.18% |
| atr_14_breakout | 1.62% | -2.97% | 3.00% | 0.09% | 3.13% |
| session_vwap | 5.91% | -1.81% | 3.00% | 1.31% | 44.39% |
| obv_20 | 5.12% | -4.16% | 3.00% | 1.54% | 51.96% |
| stochastic_14_3_recovery | -0.18% | -9.75% | 3.00% | 0.18% | 6.27% |
| mfi_14_recovery | 1.84% | -1.53% | 3.00% | 0.06% | 2.09% |
| adx_14_trend | 4.03% | 1.87% | 3.00% | 1.28% | 43.34% |
| aroon_25_trend | -0.57% | -5.06% | 3.00% | 0.66% | 22.45% |
| cci_20_momentum | 2.85% | -3.43% | 3.00% | 0.61% | 20.89% |
| williams_14_recovery | -1.23% | -9.94% | 3.00% | 0.17% | 5.74% |
| cmf_20_accumulation | 0.59% | -5.55% | 3.00% | 1.19% | 40.47% |
| chaikin_3_10 | 4.06% | -4.33% | 3.00% | 1.46% | 49.35% |
| roc_10_momentum | -0.61% | -4.30% | 3.00% | 0.38% | 13.05% |
| trix_15_trend | -1.02% | -5.09% | 3.00% | 1.29% | 43.60% |
| keltner_20_breakout | 0.49% | -4.45% | 3.00% | 0.34% | 11.49% |
| opening_range_30m | -0.93% | -4.60% | 3.00% | 0.59% | 20.10% |

동일 구간·초기 자금, 종료 시 청산 비용 포함. 노출 맞춤은 사후 설명용이며 v2 실제 계좌 성과가 아닙니다.
[낙폭 분해·비용 영향·전체 구간](MSFT/comparison.json)

[v1 전체 기록](MSFT/accounts.json) · [v2 전체 기록](MSFT/accounts-v2.json)

## JPM 계좌

| 모델 | 전략 | 평가액 USD | 손익 USD | 최근 매매·이유 |
|---|---|---:|---:|---|
| v1 | cash | 10000.00 | 0.00 | 대기 /  / 새 신호 대기 |
| v1 | buy_hold | 9819.28 | -180.72 | buy /  / buy_hold: prior completed bar target 100%; next bar open simulation |
| v1 | trend_8_26 | 9765.74 | -234.26 | buy /  / trend_8_26: prior completed bar target 100%; next bar open simulation |
| v1 | momentum_26 | 9590.55 | -409.45 | sell /  / momentum_26: prior completed bar target 0%; next bar open simulation |
| v1 | breakout_8 | 9630.81 | -369.19 | sell /  / breakout_8: prior completed bar target 0%; next bar open simulation |
| v1 | reversion_12 | 9581.59 | -418.41 | sell /  / reversion_12: prior completed bar target 0%; next bar open simulation |
| v1 | volume_26 | 9854.06 | -145.94 | sell /  / volume_26: prior completed bar target 0%; next bar open simulation |
| v1 | trend_8_26 AND momentum_26 | 9736.63 | -263.37 | sell /  / trend_8_26 AND momentum_26: prior completed bar target 0%; next bar open simulation |
| v1 | trend_8_26 + momentum_26 | 9677.78 | -322.22 | sell /  / trend_8_26 + momentum_26: prior completed bar target 50%; next bar open simulation |
| v1 | trend_8_26 AND breakout_8 | 9857.98 | -142.02 | sell /  / trend_8_26 AND breakout_8: prior completed bar target 0%; next bar open simulation |
| v1 | trend_8_26 + breakout_8 | 9736.88 | -263.12 | sell /  / trend_8_26 + breakout_8: prior completed bar target 50%; next bar open simulation |
| v1 | trend_8_26 AND reversion_12 | 9827.73 | -172.27 | sell /  / trend_8_26 AND reversion_12: prior completed bar target 0%; next bar open simulation |
| v1 | trend_8_26 + reversion_12 | 9673.05 | -326.95 | sell /  / trend_8_26 + reversion_12: prior completed bar target 50%; next bar open simulation |
| v1 | trend_8_26 AND volume_26 | 10035.68 | 35.68 | sell /  / trend_8_26 AND volume_26: prior completed bar target 0%; next bar open simulation |
| v1 | trend_8_26 + volume_26 | 9809.65 | -190.35 | sell /  / trend_8_26 + volume_26: prior completed bar target 50%; next bar open simulation |
| v1 | momentum_26 AND breakout_8 | 9677.26 | -322.74 | sell /  / momentum_26 AND breakout_8: prior completed bar target 0%; next bar open simulation |
| v1 | momentum_26 + breakout_8 | 9610.77 | -389.23 | sell /  / momentum_26 + breakout_8: prior completed bar target 0%; next bar open simulation |
| v1 | momentum_26 AND reversion_12 | 9849.85 | -150.15 | sell /  / momentum_26 AND reversion_12: prior completed bar target 0%; next bar open simulation |
| v1 | momentum_26 + reversion_12 | 9643.63 | -356.37 | sell /  / momentum_26 + reversion_12: prior completed bar target 0%; next bar open simulation |
| v1 | momentum_26 AND volume_26 | 9926.98 | -73.02 | sell /  / momentum_26 AND volume_26: prior completed bar target 0%; next bar open simulation |
| v1 | momentum_26 + volume_26 | 9740.82 | -259.18 | sell /  / momentum_26 + volume_26: prior completed bar target 0%; next bar open simulation |
| v1 | breakout_8 AND reversion_12 | 10000.00 | 0.00 | 대기 /  / 새 신호 대기 |
| v1 | breakout_8 + reversion_12 | 9644.44 | -355.56 | sell /  / breakout_8 + reversion_12: prior completed bar target 0%; next bar open simulation |
| v1 | breakout_8 AND volume_26 | 10022.00 | 22.00 | sell /  / breakout_8 AND volume_26: prior completed bar target 0%; next bar open simulation |
| v1 | breakout_8 + volume_26 | 9741.75 | -258.25 | sell /  / breakout_8 + volume_26: prior completed bar target 0%; next bar open simulation |
| v1 | reversion_12 AND volume_26 | 9940.10 | -59.90 | sell /  / reversion_12 AND volume_26: prior completed bar target 0%; next bar open simulation |
| v1 | reversion_12 + volume_26 | 9755.65 | -244.35 | sell /  / reversion_12 + volume_26: prior completed bar target 0%; next bar open simulation |
| v1 | ema_12_26 | 9755.41 | -244.59 | sell /  / EMA12 > EMA26; 조건 미충족; EMA12=336.517, EMA26=336.551 |
| v1 | macd_12_26_9 | 9839.10 | -160.90 | sell /  / MACD > 신호선 그리고 MACD > 0; 조건 미충족; MACD=-0.0344827, signal9=-0.0504891 |
| v1 | rsi_14_recovery | 9986.37 | -13.63 | sell /  / 직전 RSI14 < 30, 현재 RSI14 >= 30 (한 봉 목표); 조건 미충족; RSI14=61.6663, previous_RSI14=57.046 |
| v1 | bollinger_20_reentry | 9849.78 | -150.22 | sell /  / 직전 종가 < 직전 하단밴드, 현재 하단밴드 <= 종가 <= SMA20 (한 봉 목표); 조건 미충족; close=333.59, lower20=333.09, SMA20=334.751, previous_lower20=333.244 |
| v1 | donchian_20 | 9830.85 | -169.15 | sell /  / 종가 > 현재 봉을 제외한 직전 20봉 최고가; 조건 미충족; close=339.04, prior_high20=339.42 |
| v1 | atr_14_breakout | 9746.56 | -253.44 | sell /  / 종가 > 직전 종가 + 직전 ATR14 그리고 종가 > EMA26; 조건 미충족; close=339.04, threshold=340.465, prior_ATR14=1.34545, EMA26=336.613 |
| v1 | session_vwap | 9666.64 | -333.36 | buy /  / 종가 > 뉴욕 거래일별 누적 전형가격 VWAP; 조건 충족; close=334.517, session_VWAP=334.244, session_volume=2.89587e+06 |
| v1 | obv_20 | 9907.65 | -92.35 | sell /  / OBV > OBV의 SMA20 그리고 종가 > EMA26; 조건 미충족; OBV=-2.22359e+07, OBV_SMA20=-2.24528e+07, close=334.415, EMA26=334.612 |
| v1 | stochastic_14_3_recovery | 9575.82 | -424.18 | sell /  / 직전 %K14 < 20에서 %K14가 %D3 상향 돌파 (한 봉 목표); 조건 미충족; K14=36.1707, D3=21.3001, previous_K14=19.2613, previous_D3=15.9414 |
| v1 | mfi_14_recovery | 9935.64 | -64.36 | sell /  / 직전 MFI14 < 20, 현재 MFI14 >= 20 (한 봉 목표); 조건 미충족; MFI14=30.2719, previous_MFI14=26.8492 |
| v1 | adx_14_trend | 9726.68 | -273.32 | sell /  / Wilder ADX14 >= 25 그리고 +DI14 > -DI14; 조건 미충족; ADX14=23.9395, plus_DI14=23.2021, minus_DI14=22.594 |
| v1 | aroon_25_trend | 9824.71 | -175.29 | sell /  / Aroon25 Up > 70 그리고 Down < 30 (동률이면 최신 극값); 조건 미충족; Aroon_up=68, Aroon_down=16 |
| v1 | cci_20_momentum | 9892.77 | -107.23 | sell /  / CCI20 > 100 (전형가격·평균절대편차); 조건 미충족; CCI20=72.0963 |
| v1 | williams_14_recovery | 9568.76 | -431.24 | sell /  / 직전 Williams %R14 < -80, 현재 >= -80 (한 봉 목표); 조건 미충족; Williams_R14=-78.9473, previous_R14=-79.2829 |
| v1 | cmf_20_accumulation | 9792.34 | -207.66 | buy /  / Chaikin Money Flow20 > 0.1; 조건 충족; CMF20=0.131084, volume20=2.22061e+06 |
| v1 | chaikin_3_10 | 9739.02 | -260.98 | sell /  / ADL의 EMA3 - EMA10 > 0 그리고 종가 > EMA26; 조건 미충족; Chaikin3_10=23167, ADL=-1.29429e+07, close=334.415, EMA26=334.612 |
| v1 | roc_10_momentum | 9836.40 | -163.60 | sell /  / 10봉 ROC > 1% 그리고 종가 > EMA26; 조건 미충족; ROC10_percent=0.964142, close=337.72, EMA26=336.695 |
| v1 | trix_15_trend | 9723.73 | -276.27 | sell /  / 15봉 삼중 EMA의 1봉 변화율 TRIX > 0 그리고 종가 > EMA26; 조건 미충족; TRIX15_percent=0.0135144, close=337.6, EMA26=338.759 |
| v1 | keltner_20_breakout | 9905.24 | -94.76 | sell /  / 종가 > EMA20 + 2 x Wilder ATR14; 조건 미충족; close=339.04, upper_Keltner=339.281, EMA20=336.559, ATR14=1.36146 |
| v1 | opening_range_30m | 9850.26 | -149.74 | sell /  / 뉴욕 09:30·09:45 두 완료 봉 최고가를 10:00 이후 종가가 돌파; 조건 미충족; close=337.72, opening_high=339.035 |
| v2 | cash | 10000.00 | 0.00 | 대기 /  / 새 신호 대기 |
| v2 | buy_hold | 9983.36 | -16.64 | buy / partial / 직전 완료 봉 목표 비중 100%; 다음 봉 시가 가정 |
| v2 | trend_8_26 | 9769.83 | -230.17 | buy / partial / 직전 완료 봉 목표 비중 100%; 다음 봉 시가 가정 |
| v2 | momentum_26 | 9125.42 | -874.58 | 중단: 손실 한도 / buy / partial / 직전 완료 봉 목표 비중 100%; 다음 봉 시가 가정 |
| v2 | breakout_8 | 8994.45 | -1005.55 | 중단: 손실 한도 / buy / partial / 직전 완료 봉 목표 비중 100%; 다음 봉 시가 가정 |
| v2 | reversion_12 | 9549.04 | -450.96 | sell / filled / 직전 완료 봉 목표 비중 0%; 다음 봉 시가 가정 |
| v2 | volume_26 | 9673.61 | -326.39 | sell / filled / 직전 완료 봉 목표 비중 0%; 다음 봉 시가 가정 |
| v2 | trend_8_26 AND momentum_26 | 9697.82 | -302.18 | sell / filled / 직전 완료 봉 목표 비중 0%; 다음 봉 시가 가정 |
| v2 | trend_8_26 + momentum_26 | 9452.17 | -547.83 | sell / filled / 직전 완료 봉 목표 비중 50%; 다음 봉 시가 가정 |
| v2 | trend_8_26 AND breakout_8 | 9231.99 | -768.01 | sell / filled / 직전 완료 봉 목표 비중 0%; 다음 봉 시가 가정 |
| v2 | trend_8_26 + breakout_8 | 9404.27 | -595.73 | sell / filled / 직전 완료 봉 목표 비중 50%; 다음 봉 시가 가정 |
| v2 | trend_8_26 AND reversion_12 | 9801.81 | -198.19 | sell / filled / 직전 완료 봉 목표 비중 0%; 다음 봉 시가 가정 |
| v2 | trend_8_26 + reversion_12 | 9699.46 | -300.54 | sell / filled / 직전 완료 봉 목표 비중 50%; 다음 봉 시가 가정 |
| v2 | trend_8_26 AND volume_26 | 9833.30 | -166.70 | sell / filled / 직전 완료 봉 목표 비중 0%; 다음 봉 시가 가정 |
| v2 | trend_8_26 + volume_26 | 9722.26 | -277.74 | sell / filled / 직전 완료 봉 목표 비중 50%; 다음 봉 시가 가정 |
| v2 | momentum_26 AND breakout_8 | 9003.61 | -996.39 | sell / filled / 직전 완료 봉 목표 비중 0%; 다음 봉 시가 가정 |
| v2 | momentum_26 + breakout_8 | 9060.53 | -939.47 | sell / filled / 직전 완료 봉 목표 비중 0%; 다음 봉 시가 가정 |
| v2 | momentum_26 AND reversion_12 | 9793.51 | -206.49 | sell / filled / 직전 완료 봉 목표 비중 0%; 다음 봉 시가 가정 |
| v2 | momentum_26 + reversion_12 | 9502.91 | -497.09 | sell / filled / 직전 완료 봉 목표 비중 0%; 다음 봉 시가 가정 |
| v2 | momentum_26 AND volume_26 | 9724.84 | -275.16 | sell / filled / 직전 완료 봉 목표 비중 0%; 다음 봉 시가 가정 |
| v2 | momentum_26 + volume_26 | 9465.55 | -534.45 | sell / filled / 직전 완료 봉 목표 비중 0%; 다음 봉 시가 가정 |
| v2 | breakout_8 AND reversion_12 | 10000.00 | 0.00 | 대기 /  / 새 신호 대기 |
| v2 | breakout_8 + reversion_12 | 9335.50 | -664.50 | sell / filled / 직전 완료 봉 목표 비중 0%; 다음 봉 시가 가정 |
| v2 | breakout_8 AND volume_26 | 9911.14 | -88.86 | sell / filled / 직전 완료 봉 목표 비중 0%; 다음 봉 시가 가정 |
| v2 | breakout_8 + volume_26 | 9337.30 | -662.70 | sell / filled / 직전 완료 봉 목표 비중 0%; 다음 봉 시가 가정 |
| v2 | reversion_12 AND volume_26 | 9987.18 | -12.82 | sell / filled / 직전 완료 봉 목표 비중 0%; 다음 봉 시가 가정 |
| v2 | reversion_12 + volume_26 | 9671.95 | -328.05 | sell / filled / 직전 완료 봉 목표 비중 0%; 다음 봉 시가 가정 |
| v2 | ema_12_26 | 9751.51 | -248.49 | sell / filled / EMA12 > EMA26; 조건 미충족; EMA12=336.517, EMA26=336.551; 직전 완료 봉 목표를 다음 봉 시가에 모의 적용 |
| v2 | macd_12_26_9 | 9835.16 | -164.84 | sell / filled / MACD > 신호선 그리고 MACD > 0; 조건 미충족; MACD=-0.0344827, signal9=-0.0504891; 직전 완료 봉 목표를 다음 봉 시가에 모의 적용 |
| v2 | rsi_14_recovery | 9984.37 | -15.63 | sell / filled / 직전 RSI14 < 30, 현재 RSI14 >= 30 (한 봉 목표); 조건 미충족; RSI14=61.6663, previous_RSI14=57.046; 직전 완료 봉 목표를 다음 봉 시가에 모의 적용 |
| v2 | bollinger_20_reentry | 9843.87 | -156.13 | sell / filled / 직전 종가 < 직전 하단밴드, 현재 하단밴드 <= 종가 <= SMA20 (한 봉 목표); 조건 미충족; close=333.59, lower20=333.09, SMA20=334.751, previous_lower20=333.244; 직전 완료 봉 목표를 다음 봉 시가에 모의 적용 |
| v2 | donchian_20 | 9824.96 | -175.04 | sell / filled / 종가 > 현재 봉을 제외한 직전 20봉 최고가; 조건 미충족; close=339.04, prior_high20=339.42; 직전 완료 봉 목표를 다음 봉 시가에 모의 적용 |
| v2 | atr_14_breakout | 9736.82 | -263.18 | sell / filled / 종가 > 직전 종가 + 직전 ATR14 그리고 종가 > EMA26; 조건 미충족; close=339.04, threshold=340.465, prior_ATR14=1.34545, EMA26=336.613; 직전 완료 봉 목표를 다음 봉 시가에 모의 적용 |
| v2 | session_vwap | 9654.08 | -345.92 | buy / partial / 종가 > 뉴욕 거래일별 누적 전형가격 VWAP; 조건 충족; close=334.517, session_VWAP=334.244, session_volume=2.89587e+06; 직전 완료 봉 목표를 다음 봉 시가에 모의 적용 |
| v2 | obv_20 | 9901.71 | -98.29 | sell / filled / OBV > OBV의 SMA20 그리고 종가 > EMA26; 조건 미충족; OBV=-2.22359e+07, OBV_SMA20=-2.24528e+07, close=334.415, EMA26=334.612; 직전 완료 봉 목표를 다음 봉 시가에 모의 적용 |
| v2 | stochastic_14_3_recovery | 9554.77 | -445.23 | sell / filled / 직전 %K14 < 20에서 %K14가 %D3 상향 돌파 (한 봉 목표); 조건 미충족; K14=36.1707, D3=21.3001, previous_K14=19.2613, previous_D3=15.9414; 직전 완료 봉 목표를 다음 봉 시가에 모의 적용 |
| v2 | mfi_14_recovery | 9931.66 | -68.34 | sell / filled / 직전 MFI14 < 20, 현재 MFI14 >= 20 (한 봉 목표); 조건 미충족; MFI14=30.2719, previous_MFI14=26.8492; 직전 완료 봉 목표를 다음 봉 시가에 모의 적용 |
| v2 | adx_14_trend | 9722.79 | -277.21 | sell / filled / Wilder ADX14 >= 25 그리고 +DI14 > -DI14; 조건 미충족; ADX14=23.9395, plus_DI14=23.2021, minus_DI14=22.594; 직전 완료 봉 목표를 다음 봉 시가에 모의 적용 |
| v2 | aroon_25_trend | 9822.74 | -177.26 | sell / filled / Aroon25 Up > 70 그리고 Down < 30 (동률이면 최신 극값); 조건 미충족; Aroon_up=68, Aroon_down=16; 직전 완료 봉 목표를 다음 봉 시가에 모의 적용 |
| v2 | cci_20_momentum | 9886.83 | -113.17 | sell / filled / CCI20 > 100 (전형가격·평균절대편차); 조건 미충족; CCI20=72.0963; 직전 완료 봉 목표를 다음 봉 시가에 모의 적용 |
| v2 | williams_14_recovery | 9549.64 | -450.36 | sell / filled / 직전 Williams %R14 < -80, 현재 >= -80 (한 봉 목표); 조건 미충족; Williams_R14=-78.9473, previous_R14=-79.2829; 직전 완료 봉 목표를 다음 봉 시가에 모의 적용 |
| v2 | cmf_20_accumulation | 9785.49 | -214.51 | buy / partial / Chaikin Money Flow20 > 0.1; 조건 충족; CMF20=0.131084, volume20=2.22061e+06; 직전 완료 봉 목표를 다음 봉 시가에 모의 적용 |
| v2 | chaikin_3_10 | 9729.29 | -270.71 | sell / filled / ADL의 EMA3 - EMA10 > 0 그리고 종가 > EMA26; 조건 미충족; Chaikin3_10=23167, ADL=-1.29429e+07, close=334.415, EMA26=334.612; 직전 완료 봉 목표를 다음 봉 시가에 모의 적용 |
| v2 | roc_10_momentum | 9832.47 | -167.53 | sell / filled / 10봉 ROC > 1% 그리고 종가 > EMA26; 조건 미충족; ROC10_percent=0.964142, close=337.72, EMA26=336.695; 직전 완료 봉 목표를 다음 봉 시가에 모의 적용 |
| v2 | trix_15_trend | 9715.96 | -284.04 | sell / filled / 15봉 삼중 EMA의 1봉 변화율 TRIX > 0 그리고 종가 > EMA26; 조건 미충족; TRIX15_percent=0.0135144, close=337.6, EMA26=338.759; 직전 완료 봉 목표를 다음 봉 시가에 모의 적용 |
| v2 | keltner_20_breakout | 9901.28 | -98.72 | sell / filled / 종가 > EMA20 + 2 x Wilder ATR14; 조건 미충족; close=339.04, upper_Keltner=339.281, EMA20=336.559, ATR14=1.36146; 직전 완료 봉 목표를 다음 봉 시가에 모의 적용 |
| v2 | opening_range_30m | 9846.33 | -153.67 | sell / filled / 뉴욕 09:30·09:45 두 완료 봉 최고가를 10:00 이후 종가가 돌파; 조건 미충족; close=337.72, opening_high=339.035; 직전 완료 봉 목표를 다음 봉 시가에 모의 적용 |

### 같은 기간의 비용·노출 비교 (사후 연구)

| 전략 | 비용 전 | 비용 후 | 100% 보유 | 같은 평균 노출 보유 | 평균 노출 |
|---|---:|---:|---:|---:|---:|
| cash | 0.00% | 0.00% | 1.78% | 0.00% | 0.00% |
| buy_hold | 2.20% | 1.78% | 1.78% | 1.78% | 100.00% |
| trend_8_26 | 0.51% | -3.63% | 1.78% | 0.95% | 53.79% |
| momentum_26 | -3.44% | -11.22% | 1.78% | 0.92% | 51.96% |
| breakout_8 | -2.85% | -18.56% | 1.78% | 0.37% | 20.89% |
| reversion_12 | 7.26% | -8.18% | 1.78% | 0.40% | 22.72% |
| volume_26 | 0.30% | -5.83% | 1.78% | 0.11% | 6.01% |
| trend_8_26 AND momentum_26 | 0.38% | -4.96% | 1.78% | 0.73% | 41.25% |
| trend_8_26 + momentum_26 | -1.48% | -7.30% | 1.78% | 0.93% | 52.88% |
| trend_8_26 AND breakout_8 | -3.39% | -13.75% | 1.78% | 0.21% | 12.27% |
| trend_8_26 + breakout_8 | -1.17% | -10.84% | 1.78% | 0.66% | 37.34% |
| trend_8_26 AND reversion_12 | 2.93% | -3.76% | 1.78% | 0.13% | 7.31% |
| trend_8_26 + reversion_12 | 3.85% | -5.34% | 1.78% | 0.67% | 38.26% |
| trend_8_26 AND volume_26 | -0.37% | -3.66% | 1.78% | 0.06% | 3.66% |
| trend_8_26 + volume_26 | 0.42% | -4.73% | 1.78% | 0.52% | 29.90% |
| momentum_26 AND breakout_8 | -2.86% | -14.36% | 1.78% | 0.22% | 12.79% |
| momentum_26 + breakout_8 | -3.12% | -14.77% | 1.78% | 0.64% | 36.43% |
| momentum_26 AND reversion_12 | 2.87% | -4.62% | 1.78% | 0.12% | 7.05% |
| momentum_26 + reversion_12 | 1.79% | -7.80% | 1.78% | 0.66% | 37.34% |
| momentum_26 AND volume_26 | -0.48% | -3.77% | 1.78% | 0.05% | 3.13% |
| momentum_26 + volume_26 | -1.57% | -8.17% | 1.78% | 0.51% | 28.99% |
| breakout_8 AND reversion_12 | 0.00% | 0.00% | 1.78% | 0.00% | 0.00% |
| breakout_8 + reversion_12 | 2.10% | -12.25% | 1.78% | 0.38% | 21.81% |
| breakout_8 AND volume_26 | -0.25% | -2.32% | 1.78% | 0.02% | 1.31% |
| breakout_8 + volume_26 | -1.28% | -11.69% | 1.78% | 0.24% | 13.45% |
| reversion_12 AND volume_26 | 2.09% | -0.45% | 1.78% | 0.04% | 2.09% |
| reversion_12 + volume_26 | 3.73% | -5.83% | 1.78% | 0.25% | 14.37% |
| ema_12_26 | -0.24% | -3.54% | 1.78% | 0.91% | 51.70% |
| macd_12_26_9 | -0.13% | -4.64% | 1.78% | 0.57% | 32.64% |
| rsi_14_recovery | 0.59% | -1.08% | 1.78% | 0.02% | 1.04% |
| bollinger_20_reentry | 0.23% | -3.49% | 1.78% | 0.04% | 2.35% |
| donchian_20 | -1.81% | -5.05% | 1.78% | 0.05% | 3.13% |
| atr_14_breakout | -1.35% | -8.92% | 1.78% | 0.09% | 5.22% |
| session_vwap | 1.64% | -8.49% | 1.78% | 0.87% | 49.61% |
| obv_20 | -3.62% | -14.67% | 1.78% | 0.55% | 31.07% |
| stochastic_14_3_recovery | -0.53% | -10.45% | 1.78% | 0.11% | 6.53% |
| mfi_14_recovery | 0.25% | -1.42% | 1.78% | 0.02% | 1.04% |
| adx_14_trend | -2.43% | -4.85% | 1.78% | 0.52% | 29.50% |
| aroon_25_trend | -0.75% | -4.43% | 1.78% | 0.38% | 21.67% |
| cci_20_momentum | -3.02% | -11.21% | 1.78% | 0.29% | 16.45% |
| williams_14_recovery | -0.86% | -11.11% | 1.78% | 0.12% | 6.79% |
| cmf_20_accumulation | -2.15% | -11.16% | 1.78% | 0.55% | 31.07% |
| chaikin_3_10 | 0.81% | -8.48% | 1.78% | 0.61% | 34.99% |
| roc_10_momentum | -1.36% | -4.22% | 1.78% | 0.15% | 8.36% |
| trix_15_trend | -1.25% | -8.83% | 1.78% | 0.61% | 34.99% |
| keltner_20_breakout | -1.21% | -4.07% | 1.78% | 0.07% | 4.18% |
| opening_range_30m | -0.23% | -3.93% | 1.78% | 0.30% | 17.23% |

동일 구간·초기 자금, 종료 시 청산 비용 포함. 노출 맞춤은 사후 설명용이며 v2 실제 계좌 성과가 아닙니다.
[낙폭 분해·비용 영향·전체 구간](JPM/comparison.json)

[v1 전체 기록](JPM/accounts.json) · [v2 전체 기록](JPM/accounts-v2.json)

## XOM 계좌

| 모델 | 전략 | 평가액 USD | 손익 USD | 최근 매매·이유 |
|---|---|---:|---:|---|
| v1 | cash | 10000.00 | 0.00 | 대기 /  / 새 신호 대기 |
| v1 | buy_hold | 10065.70 | 65.70 | buy /  / buy_hold: prior completed bar target 100%; next bar open simulation |
| v1 | trend_8_26 | 9828.38 | -171.62 | buy /  / trend_8_26: prior completed bar target 100%; next bar open simulation |
| v1 | momentum_26 | 9923.94 | -76.06 | buy /  / momentum_26: prior completed bar target 100%; next bar open simulation |
| v1 | breakout_8 | 9491.06 | -508.94 | sell /  / breakout_8: prior completed bar target 0%; next bar open simulation |
| v1 | reversion_12 | 9667.31 | -332.69 | sell /  / reversion_12: prior completed bar target 0%; next bar open simulation |
| v1 | volume_26 | 9627.78 | -372.22 | sell /  / volume_26: prior completed bar target 0%; next bar open simulation |
| v1 | trend_8_26 AND momentum_26 | 9792.62 | -207.38 | buy /  / trend_8_26 AND momentum_26: prior completed bar target 100%; next bar open simulation |
| v1 | trend_8_26 + momentum_26 | 9876.17 | -123.83 | buy /  / trend_8_26 + momentum_26: prior completed bar target 100%; next bar open simulation |
| v1 | trend_8_26 AND breakout_8 | 9628.70 | -371.30 | sell /  / trend_8_26 AND breakout_8: prior completed bar target 0%; next bar open simulation |
| v1 | trend_8_26 + breakout_8 | 9677.96 | -322.04 | sell /  / trend_8_26 + breakout_8: prior completed bar target 50%; next bar open simulation |
| v1 | trend_8_26 AND reversion_12 | 9661.66 | -338.34 | sell /  / trend_8_26 AND reversion_12: prior completed bar target 0%; next bar open simulation |
| v1 | trend_8_26 + reversion_12 | 9747.45 | -252.55 | buy /  / trend_8_26 + reversion_12: prior completed bar target 50%; next bar open simulation |
| v1 | trend_8_26 AND volume_26 | 9743.46 | -256.54 | sell /  / trend_8_26 AND volume_26: prior completed bar target 0%; next bar open simulation |
| v1 | trend_8_26 + volume_26 | 9727.76 | -272.24 | buy /  / trend_8_26 + volume_26: prior completed bar target 50%; next bar open simulation |
| v1 | momentum_26 AND breakout_8 | 9724.23 | -275.77 | sell /  / momentum_26 AND breakout_8: prior completed bar target 0%; next bar open simulation |
| v1 | momentum_26 + breakout_8 | 9705.33 | -294.67 | sell /  / momentum_26 + breakout_8: prior completed bar target 50%; next bar open simulation |
| v1 | momentum_26 AND reversion_12 | 9750.13 | -249.87 | sell /  / momentum_26 AND reversion_12: prior completed bar target 0%; next bar open simulation |
| v1 | momentum_26 + reversion_12 | 9794.61 | -205.39 | buy /  / momentum_26 + reversion_12: prior completed bar target 50%; next bar open simulation |
| v1 | momentum_26 AND volume_26 | 9964.17 | -35.83 | sell /  / momentum_26 AND volume_26: prior completed bar target 0%; next bar open simulation |
| v1 | momentum_26 + volume_26 | 9774.70 | -225.30 | buy /  / momentum_26 + volume_26: prior completed bar target 50%; next bar open simulation |
| v1 | breakout_8 AND reversion_12 | 10000.00 | 0.00 | 대기 /  / 새 신호 대기 |
| v1 | breakout_8 + reversion_12 | 9597.91 | -402.09 | sell /  / breakout_8 + reversion_12: prior completed bar target 0%; next bar open simulation |
| v1 | breakout_8 AND volume_26 | 9851.05 | -148.95 | sell /  / breakout_8 AND volume_26: prior completed bar target 0%; next bar open simulation |
| v1 | breakout_8 + volume_26 | 9559.02 | -440.98 | sell /  / breakout_8 + volume_26: prior completed bar target 0%; next bar open simulation |
| v1 | reversion_12 AND volume_26 | 9794.27 | -205.73 | sell /  / reversion_12 AND volume_26: prior completed bar target 0%; next bar open simulation |
| v1 | reversion_12 + volume_26 | 9647.62 | -352.38 | sell /  / reversion_12 + volume_26: prior completed bar target 0%; next bar open simulation |
| v1 | ema_12_26 | 9883.30 | -116.70 | buy /  / EMA12 > EMA26; 조건 충족; EMA12=177.271, EMA26=177.221 |
| v1 | macd_12_26_9 | 9886.56 | -113.44 | buy /  / MACD > 신호선 그리고 MACD > 0; 조건 충족; MACD=0.0851362, signal9=0.0737531 |
| v1 | rsi_14_recovery | 9927.64 | -72.36 | sell /  / 직전 RSI14 < 30, 현재 RSI14 >= 30 (한 봉 목표); 조건 미충족; RSI14=37.639, previous_RSI14=31.1023 |
| v1 | bollinger_20_reentry | 9852.90 | -147.10 | sell /  / 직전 종가 < 직전 하단밴드, 현재 하단밴드 <= 종가 <= SMA20 (한 봉 목표); 조건 미충족; close=175.55, lower20=175.189, SMA20=177.794, previous_lower20=175.528 |
| v1 | donchian_20 | 9665.93 | -334.07 | sell /  / 종가 > 현재 봉을 제외한 직전 20봉 최고가; 조건 미충족; close=178.045, prior_high20=179.205 |
| v1 | atr_14_breakout | 9803.61 | -196.39 | sell /  / 종가 > 직전 종가 + 직전 ATR14 그리고 종가 > EMA26; 조건 미충족; close=178.95, threshold=179.19, prior_ATR14=0.519565, EMA26=177.678 |
| v1 | session_vwap | 9785.95 | -214.05 | buy /  / 종가 > 뉴욕 거래일별 누적 전형가격 VWAP; 조건 충족; close=177.325, session_VWAP=177.324, session_volume=4.58361e+06 |
| v1 | obv_20 | 9467.89 | -532.11 | buy /  / OBV > OBV의 SMA20 그리고 종가 > EMA26; 조건 충족; OBV=2.31608e+07, OBV_SMA20=2.3021e+07, close=178.67, EMA26=177.576 |
| v1 | stochastic_14_3_recovery | 9721.31 | -278.69 | sell /  / 직전 %K14 < 20에서 %K14가 %D3 상향 돌파 (한 봉 목표); 조건 미충족; K14=29.2797, D3=21.8586, previous_K14=22.3575, previous_D3=16.0588 |
| v1 | mfi_14_recovery | 10000.00 | 0.00 | 대기 /  / 새 신호 대기 |
| v1 | adx_14_trend | 9999.47 | -0.53 | sell /  / Wilder ADX14 >= 25 그리고 +DI14 > -DI14; 조건 미충족; ADX14=23.8302, plus_DI14=25.6436, minus_DI14=22.6035 |
| v1 | aroon_25_trend | 9655.16 | -344.84 | buy /  / Aroon25 Up > 70 그리고 Down < 30 (동률이면 최신 극값); 조건 충족; Aroon_up=100, Aroon_down=20 |
| v1 | cci_20_momentum | 9545.26 | -454.74 | buy /  / CCI20 > 100 (전형가격·평균절대편차); 조건 충족; CCI20=273.695 |
| v1 | williams_14_recovery | 9665.88 | -334.12 | sell /  / 직전 Williams %R14 < -80, 현재 >= -80 (한 봉 목표); 조건 미충족; Williams_R14=-12.0205, previous_R14=-62.6593 |
| v1 | cmf_20_accumulation | 9838.75 | -161.25 | sell /  / Chaikin Money Flow20 > 0.1; 조건 미충족; CMF20=0.070754, volume20=4.44162e+06 |
| v1 | chaikin_3_10 | 9679.15 | -320.85 | buy /  / ADL의 EMA3 - EMA10 > 0 그리고 종가 > EMA26; 조건 충족; Chaikin3_10=139280, ADL=2.86253e+07, close=177.685, EMA26=177.404 |
| v1 | roc_10_momentum | 9848.63 | -151.37 | sell /  / 10봉 ROC > 1% 그리고 종가 > EMA26; 조건 미충족; ROC10_percent=0.417363, close=178.045, EMA26=177.705 |
| v1 | trix_15_trend | 9810.66 | -189.34 | buy /  / 15봉 삼중 EMA의 1봉 변화율 TRIX > 0 그리고 종가 > EMA26; 조건 충족; TRIX15_percent=0.00698676, close=177.685, EMA26=177.404 |
| v1 | keltner_20_breakout | 9862.17 | -137.83 | sell /  / 종가 > EMA20 + 2 x Wilder ATR14; 조건 미충족; close=178.045, upper_Keltner=178.914, EMA20=177.784, ATR14=0.564804 |
| v1 | opening_range_30m | 9973.39 | -26.61 | sell /  / 뉴욕 09:30·09:45 두 완료 봉 최고가를 10:00 이후 종가가 돌파; 조건 미충족; close=178.045, opening_high=178.105 |
| v2 | cash | 10000.00 | 0.00 | 대기 /  / 새 신호 대기 |
| v2 | buy_hold | 10386.92 | 386.92 | buy / partial / 직전 완료 봉 목표 비중 100%; 다음 봉 시가 가정 |
| v2 | trend_8_26 | 9916.04 | -83.96 | buy / partial / 직전 완료 봉 목표 비중 100%; 다음 봉 시가 가정 |
| v2 | momentum_26 | 10090.22 | 90.22 | buy / partial / 직전 완료 봉 목표 비중 100%; 다음 봉 시가 가정 |
| v2 | breakout_8 | 8988.95 | -1011.05 | 중단: 손실 한도 / sell / filled / 직전 완료 봉 목표 비중 0%; 다음 봉 시가 가정 |
| v2 | reversion_12 | 9480.94 | -519.06 | sell / filled / 직전 완료 봉 목표 비중 0%; 다음 봉 시가 가정 |
| v2 | volume_26 | 9527.81 | -472.19 | sell / filled / 직전 완료 봉 목표 비중 0%; 다음 봉 시가 가정 |
| v2 | trend_8_26 AND momentum_26 | 9885.30 | -114.70 | buy / partial / 직전 완료 봉 목표 비중 100%; 다음 봉 시가 가정 |
| v2 | trend_8_26 + momentum_26 | 10002.91 | 2.91 | buy / partial / 직전 완료 봉 목표 비중 100%; 다음 봉 시가 가정 |
| v2 | trend_8_26 AND breakout_8 | 9084.52 | -915.48 | sell / filled / 직전 완료 봉 목표 비중 0%; 다음 봉 시가 가정 |
| v2 | trend_8_26 + breakout_8 | 9468.34 | -531.66 | sell / filled / 직전 완료 봉 목표 비중 50%; 다음 봉 시가 가정 |
| v2 | trend_8_26 AND reversion_12 | 9499.19 | -500.81 | sell / filled / 직전 완료 봉 목표 비중 0%; 다음 봉 시가 가정 |
| v2 | trend_8_26 + reversion_12 | 9696.05 | -303.95 | buy / filled / 직전 완료 봉 목표 비중 50%; 다음 봉 시가 가정 |
| v2 | trend_8_26 AND volume_26 | 9634.03 | -365.97 | sell / filled / 직전 완료 봉 목표 비중 0%; 다음 봉 시가 가정 |
| v2 | trend_8_26 + volume_26 | 9720.12 | -279.88 | buy / filled / 직전 완료 봉 목표 비중 50%; 다음 봉 시가 가정 |
| v2 | momentum_26 AND breakout_8 | 9193.28 | -806.72 | sell / filled / 직전 완료 봉 목표 비중 0%; 다음 봉 시가 가정 |
| v2 | momentum_26 + breakout_8 | 9511.14 | -488.86 | sell / filled / 직전 완료 봉 목표 비중 50%; 다음 봉 시가 가정 |
| v2 | momentum_26 AND reversion_12 | 9549.52 | -450.48 | sell / filled / 직전 완료 봉 목표 비중 0%; 다음 봉 시가 가정 |
| v2 | momentum_26 + reversion_12 | 9780.76 | -219.24 | buy / filled / 직전 완료 봉 목표 비중 50%; 다음 봉 시가 가정 |
| v2 | momentum_26 AND volume_26 | 9918.32 | -81.68 | sell / filled / 직전 완료 봉 목표 비중 0%; 다음 봉 시가 가정 |
| v2 | momentum_26 + volume_26 | 9825.46 | -174.54 | buy / filled / 직전 완료 봉 목표 비중 50%; 다음 봉 시가 가정 |
| v2 | breakout_8 AND reversion_12 | 10000.00 | 0.00 | 대기 /  / 새 신호 대기 |
| v2 | breakout_8 + reversion_12 | 9237.99 | -762.01 | sell / filled / 직전 완료 봉 목표 비중 0%; 다음 봉 시가 가정 |
| v2 | breakout_8 AND volume_26 | 9817.82 | -182.18 | sell / filled / 직전 완료 봉 목표 비중 0%; 다음 봉 시가 가정 |
| v2 | breakout_8 + volume_26 | 9260.69 | -739.31 | sell / filled / 직전 완료 봉 목표 비중 0%; 다음 봉 시가 가정 |
| v2 | reversion_12 AND volume_26 | 9737.38 | -262.62 | sell / filled / 직전 완료 봉 목표 비중 0%; 다음 봉 시가 가정 |
| v2 | reversion_12 + volume_26 | 9524.43 | -475.57 | sell / filled / 직전 완료 봉 목표 비중 0%; 다음 봉 시가 가정 |
| v2 | ema_12_26 | 9878.36 | -121.64 | buy / partial / EMA12 > EMA26; 조건 충족; EMA12=177.271, EMA26=177.221; 직전 완료 봉 목표를 다음 봉 시가에 모의 적용 |
| v2 | macd_12_26_9 | 9877.66 | -122.34 | buy / partial / MACD > 신호선 그리고 MACD > 0; 조건 충족; MACD=0.0851362, signal9=0.0737531; 직전 완료 봉 목표를 다음 봉 시가에 모의 적용 |
| v2 | rsi_14_recovery | 9923.67 | -76.33 | sell / filled / 직전 RSI14 < 30, 현재 RSI14 >= 30 (한 봉 목표); 조건 미충족; RSI14=37.639, previous_RSI14=31.1023; 직전 완료 봉 목표를 다음 봉 시가에 모의 적용 |
| v2 | bollinger_20_reentry | 9848.96 | -151.04 | sell / filled / 직전 종가 < 직전 하단밴드, 현재 하단밴드 <= 종가 <= SMA20 (한 봉 목표); 조건 미충족; close=175.55, lower20=175.189, SMA20=177.794, previous_lower20=175.528; 직전 완료 봉 목표를 다음 봉 시가에 모의 적용 |
| v2 | donchian_20 | 9654.34 | -345.66 | sell / filled / 종가 > 현재 봉을 제외한 직전 20봉 최고가; 조건 미충족; close=178.045, prior_high20=179.205; 직전 완료 봉 목표를 다음 봉 시가에 모의 적용 |
| v2 | atr_14_breakout | 9793.82 | -206.18 | sell / filled / 종가 > 직전 종가 + 직전 ATR14 그리고 종가 > EMA26; 조건 미충족; close=178.95, threshold=179.19, prior_ATR14=0.519565, EMA26=177.678; 직전 완료 봉 목표를 다음 봉 시가에 모의 적용 |
| v2 | session_vwap | 9773.24 | -226.76 | buy / partial / 종가 > 뉴욕 거래일별 누적 전형가격 VWAP; 조건 충족; close=177.325, session_VWAP=177.324, session_volume=4.58361e+06; 직전 완료 봉 목표를 다음 봉 시가에 모의 적용 |
| v2 | obv_20 | 9502.46 | -497.54 | 중단: 손실 한도 / sell / filled / OBV > OBV의 SMA20 그리고 종가 > EMA26; 조건 미충족; OBV=2.24329e+07, OBV_SMA20=2.30895e+07, close=177.005, EMA26=177.393; 직전 완료 봉 목표를 다음 봉 시가에 모의 적용 |
| v2 | stochastic_14_3_recovery | 9711.59 | -288.41 | sell / filled / 직전 %K14 < 20에서 %K14가 %D3 상향 돌파 (한 봉 목표); 조건 미충족; K14=29.2797, D3=21.8586, previous_K14=22.3575, previous_D3=16.0588; 직전 완료 봉 목표를 다음 봉 시가에 모의 적용 |
| v2 | mfi_14_recovery | 10000.00 | 0.00 | 대기 /  / 새 신호 대기 |
| v2 | adx_14_trend | 9993.47 | -6.53 | sell / filled / Wilder ADX14 >= 25 그리고 +DI14 > -DI14; 조건 미충족; ADX14=23.8302, plus_DI14=25.6436, minus_DI14=22.6035; 직전 완료 봉 목표를 다음 봉 시가에 모의 적용 |
| v2 | aroon_25_trend | 9648.41 | -351.59 | buy / partial / Aroon25 Up > 70 그리고 Down < 30 (동률이면 최신 극값); 조건 충족; Aroon_up=100, Aroon_down=20; 직전 완료 봉 목표를 다음 봉 시가에 모의 적용 |
| v2 | cci_20_momentum | 9527.14 | -472.86 | buy / partial / CCI20 > 100 (전형가격·평균절대편차); 조건 충족; CCI20=273.695; 직전 완료 봉 목표를 다음 봉 시가에 모의 적용 |
| v2 | williams_14_recovery | 9654.28 | -345.72 | sell / filled / 직전 Williams %R14 < -80, 현재 >= -80 (한 봉 목표); 조건 미충족; Williams_R14=-12.0205, previous_R14=-62.6593; 직전 완료 봉 목표를 다음 봉 시가에 모의 적용 |
| v2 | cmf_20_accumulation | 9828.92 | -171.08 | sell / filled / Chaikin Money Flow20 > 0.1; 조건 미충족; CMF20=0.070754, volume20=4.44162e+06; 직전 완료 봉 목표를 다음 봉 시가에 모의 적용 |
| v2 | chaikin_3_10 | 9664.65 | -335.35 | buy / partial / ADL의 EMA3 - EMA10 > 0 그리고 종가 > EMA26; 조건 충족; Chaikin3_10=139280, ADL=2.86253e+07, close=177.685, EMA26=177.404; 직전 완료 봉 목표를 다음 봉 시가에 모의 적용 |
| v2 | roc_10_momentum | 9840.76 | -159.24 | sell / filled / 10봉 ROC > 1% 그리고 종가 > EMA26; 조건 미충족; ROC10_percent=0.417363, close=178.045, EMA26=177.705; 직전 완료 봉 목표를 다음 봉 시가에 모의 적용 |
| v2 | trix_15_trend | 9799.88 | -200.12 | buy / partial / 15봉 삼중 EMA의 1봉 변화율 TRIX > 0 그리고 종가 > EMA26; 조건 충족; TRIX15_percent=0.00698676, close=177.685, EMA26=177.404; 직전 완료 봉 목표를 다음 봉 시가에 모의 적용 |
| v2 | keltner_20_breakout | 9854.29 | -145.71 | sell / filled / 종가 > EMA20 + 2 x Wilder ATR14; 조건 미충족; close=178.045, upper_Keltner=178.914, EMA20=177.784, ATR14=0.564804; 직전 완료 봉 목표를 다음 봉 시가에 모의 적용 |
| v2 | opening_range_30m | 9969.40 | -30.60 | sell / filled / 뉴욕 09:30·09:45 두 완료 봉 최고가를 10:00 이후 종가가 돌파; 조건 미충족; close=178.045, opening_high=178.105; 직전 완료 봉 목표를 다음 봉 시가에 모의 적용 |

### 같은 기간의 비용·노출 비교 (사후 연구)

| 전략 | 비용 전 | 비용 후 | 100% 보유 | 같은 평균 노출 보유 | 평균 노출 |
|---|---:|---:|---:|---:|---:|
| cash | 0.00% | 0.00% | 8.54% | 0.00% | 0.00% |
| buy_hold | 9.00% | 8.54% | 8.54% | 8.54% | 100.00% |
| trend_8_26 | 1.60% | -3.40% | 8.54% | 5.87% | 69.71% |
| momentum_26 | 2.17% | -4.87% | 8.54% | 6.01% | 71.28% |
| breakout_8 | -1.19% | -19.91% | 8.54% | 2.27% | 27.42% |
| reversion_12 | 3.84% | -6.12% | 8.54% | 1.68% | 20.37% |
| volume_26 | 1.26% | -6.51% | 8.54% | 0.47% | 5.74% |
| trend_8_26 AND momentum_26 | 0.17% | -5.55% | 8.54% | 5.13% | 61.10% |
| trend_8_26 + momentum_26 | 1.89% | -3.93% | 8.54% | 5.94% | 70.50% |
| trend_8_26 AND breakout_8 | -1.03% | -16.34% | 8.54% | 1.74% | 21.15% |
| trend_8_26 + breakout_8 | 0.22% | -11.65% | 8.54% | 4.05% | 48.57% |
| trend_8_26 AND reversion_12 | -0.48% | -6.56% | 8.54% | 0.79% | 9.66% |
| trend_8_26 + reversion_12 | 2.74% | -4.56% | 8.54% | 3.75% | 45.04% |
| trend_8_26 AND volume_26 | 0.44% | -4.50% | 8.54% | 0.30% | 3.66% |
| trend_8_26 + volume_26 | 1.45% | -4.76% | 8.54% | 3.13% | 37.73% |
| momentum_26 AND breakout_8 | -1.01% | -17.71% | 8.54% | 1.96% | 23.76% |
| momentum_26 + breakout_8 | 0.50% | -12.69% | 8.54% | 4.12% | 49.35% |
| momentum_26 AND reversion_12 | 0.39% | -6.13% | 8.54% | 0.77% | 9.40% |
| momentum_26 + reversion_12 | 3.03% | -4.49% | 8.54% | 3.82% | 45.83% |
| momentum_26 AND volume_26 | 1.67% | -2.10% | 8.54% | 0.19% | 2.35% |
| momentum_26 + volume_26 | 1.74% | -4.69% | 8.54% | 3.20% | 38.52% |
| breakout_8 AND reversion_12 | 0.00% | 0.00% | 8.54% | 0.00% | 0.00% |
| breakout_8 + reversion_12 | 1.31% | -12.93% | 8.54% | 1.97% | 23.90% |
| breakout_8 AND volume_26 | -0.10% | -2.18% | 8.54% | 0.11% | 1.31% |
| breakout_8 + volume_26 | 0.04% | -12.74% | 8.54% | 1.37% | 16.59% |
| reversion_12 AND volume_26 | -0.04% | -3.35% | 8.54% | 0.19% | 2.35% |
| reversion_12 + volume_26 | 2.56% | -5.52% | 8.54% | 1.07% | 13.06% |
| ema_12_26 | 0.67% | -3.06% | 8.54% | 6.56% | 77.55% |
| macd_12_26_9 | -0.97% | -7.41% | 8.54% | 3.63% | 43.60% |
| rsi_14_recovery | -0.08% | -1.33% | 8.54% | 0.06% | 0.78% |
| bollinger_20_reentry | -1.11% | -3.57% | 8.54% | 0.13% | 1.57% |
| donchian_20 | -2.09% | -10.73% | 8.54% | 0.77% | 9.40% |
| atr_14_breakout | 0.68% | -7.44% | 8.54% | 0.45% | 5.48% |
| session_vwap | 0.39% | -10.38% | 8.54% | 5.60% | 66.58% |
| obv_20 | 0.63% | -9.78% | 8.54% | 4.05% | 48.56% |
| stochastic_14_3_recovery | 0.13% | -8.71% | 8.54% | 0.47% | 5.74% |
| mfi_14_recovery | -0.31% | -1.97% | 8.54% | 0.09% | 1.04% |
| adx_14_trend | 3.33% | 0.76% | 8.54% | 3.19% | 38.38% |
| aroon_25_trend | -3.17% | -9.84% | 8.54% | 2.73% | 32.90% |
| cci_20_momentum | 1.81% | -7.57% | 8.54% | 2.31% | 27.94% |
| williams_14_recovery | -0.75% | -6.81% | 8.54% | 0.32% | 3.92% |
| cmf_20_accumulation | 2.35% | -3.90% | 8.54% | 4.32% | 51.70% |
| chaikin_3_10 | 0.96% | -8.34% | 8.54% | 5.15% | 61.36% |
| roc_10_momentum | -0.09% | -5.80% | 8.54% | 0.96% | 11.75% |
| trix_15_trend | 0.30% | -6.61% | 8.54% | 5.44% | 64.75% |
| keltner_20_breakout | 0.18% | -5.94% | 8.54% | 1.33% | 16.19% |
| opening_range_30m | -0.37% | -9.16% | 8.54% | 2.51% | 30.29% |

동일 구간·초기 자금, 종료 시 청산 비용 포함. 노출 맞춤은 사후 설명용이며 v2 실제 계좌 성과가 아닙니다.
[낙폭 분해·비용 영향·전체 구간](XOM/comparison.json)

[v1 전체 기록](XOM/accounts.json) · [v2 전체 기록](XOM/accounts-v2.json)

## JNJ 계좌

| 모델 | 전략 | 평가액 USD | 손익 USD | 최근 매매·이유 |
|---|---|---:|---:|---|
| v1 | cash | 10000.00 | 0.00 | 대기 /  / 새 신호 대기 |
| v1 | buy_hold | 10043.69 | 43.69 | buy /  / buy_hold: prior completed bar target 100%; next bar open simulation |
| v1 | trend_8_26 | 9974.87 | -25.13 | buy /  / trend_8_26: prior completed bar target 100%; next bar open simulation |
| v1 | momentum_26 | 9722.10 | -277.90 | sell /  / momentum_26: prior completed bar target 0%; next bar open simulation |
| v1 | breakout_8 | 9366.01 | -633.99 | buy /  / breakout_8: prior completed bar target 100%; next bar open simulation |
| v1 | reversion_12 | 9747.78 | -252.22 | sell /  / reversion_12: prior completed bar target 0%; next bar open simulation |
| v1 | volume_26 | 9902.45 | -97.55 | sell /  / volume_26: prior completed bar target 0%; next bar open simulation |
| v1 | trend_8_26 AND momentum_26 | 9813.05 | -186.95 | sell /  / trend_8_26 AND momentum_26: prior completed bar target 0%; next bar open simulation |
| v1 | trend_8_26 + momentum_26 | 9847.97 | -152.03 | sell /  / trend_8_26 + momentum_26: prior completed bar target 50%; next bar open simulation |
| v1 | trend_8_26 AND breakout_8 | 9751.74 | -248.26 | buy /  / trend_8_26 AND breakout_8: prior completed bar target 100%; next bar open simulation |
| v1 | trend_8_26 + breakout_8 | 9685.28 | -314.72 | buy /  / trend_8_26 + breakout_8: prior completed bar target 100%; next bar open simulation |
| v1 | trend_8_26 AND reversion_12 | 9930.57 | -69.43 | sell /  / trend_8_26 AND reversion_12: prior completed bar target 0%; next bar open simulation |
| v1 | trend_8_26 + reversion_12 | 9860.77 | -139.23 | sell /  / trend_8_26 + reversion_12: prior completed bar target 50%; next bar open simulation |
| v1 | trend_8_26 AND volume_26 | 9995.12 | -4.88 | sell /  / trend_8_26 AND volume_26: prior completed bar target 0%; next bar open simulation |
| v1 | trend_8_26 + volume_26 | 9938.82 | -61.18 | sell /  / trend_8_26 + volume_26: prior completed bar target 50%; next bar open simulation |
| v1 | momentum_26 AND breakout_8 | 9784.22 | -215.78 | sell /  / momentum_26 AND breakout_8: prior completed bar target 0%; next bar open simulation |
| v1 | momentum_26 + breakout_8 | 9542.24 | -457.76 | sell /  / momentum_26 + breakout_8: prior completed bar target 50%; next bar open simulation |
| v1 | momentum_26 AND reversion_12 | 9938.52 | -61.48 | sell /  / momentum_26 AND reversion_12: prior completed bar target 0%; next bar open simulation |
| v1 | momentum_26 + reversion_12 | 9773.79 | -226.21 | sell /  / momentum_26 + reversion_12: prior completed bar target 0%; next bar open simulation |
| v1 | momentum_26 AND volume_26 | 10000.00 | 0.00 | 대기 /  / 새 신호 대기 |
| v1 | momentum_26 + volume_26 | 9851.20 | -148.80 | sell /  / momentum_26 + volume_26: prior completed bar target 0%; next bar open simulation |
| v1 | breakout_8 AND reversion_12 | 10000.00 | 0.00 | 대기 /  / 새 신호 대기 |
| v1 | breakout_8 + reversion_12 | 9554.68 | -445.32 | sell /  / breakout_8 + reversion_12: prior completed bar target 50%; next bar open simulation |
| v1 | breakout_8 AND volume_26 | 10000.00 | 0.00 | 대기 /  / 새 신호 대기 |
| v1 | breakout_8 + volume_26 | 9649.68 | -350.32 | sell /  / breakout_8 + volume_26: prior completed bar target 50%; next bar open simulation |
| v1 | reversion_12 AND volume_26 | 9933.02 | -66.98 | sell /  / reversion_12 AND volume_26: prior completed bar target 0%; next bar open simulation |
| v1 | reversion_12 + volume_26 | 9844.46 | -155.54 | sell /  / reversion_12 + volume_26: prior completed bar target 0%; next bar open simulation |
| v1 | ema_12_26 | 9770.13 | -229.87 | sell /  / EMA12 > EMA26; 조건 미충족; EMA12=257.771, EMA26=257.934 |
| v1 | macd_12_26_9 | 9887.47 | -112.53 | sell /  / MACD > 신호선 그리고 MACD > 0; 조건 미충족; MACD=1.30676, signal9=1.31668 |
| v1 | rsi_14_recovery | 9923.04 | -76.96 | sell /  / 직전 RSI14 < 30, 현재 RSI14 >= 30 (한 봉 목표); 조건 미충족; RSI14=40.3665, previous_RSI14=36.2025 |
| v1 | bollinger_20_reentry | 9816.96 | -183.04 | sell /  / 직전 종가 < 직전 하단밴드, 현재 하단밴드 <= 종가 <= SMA20 (한 봉 목표); 조건 미충족; close=255.05, lower20=254.819, SMA20=258.099, previous_lower20=255.312 |
| v1 | donchian_20 | 9885.06 | -114.94 | sell /  / 종가 > 현재 봉을 제외한 직전 20봉 최고가; 조건 미충족; close=257.085, prior_high20=257.175 |
| v1 | atr_14_breakout | 9701.58 | -298.42 | sell /  / 종가 > 직전 종가 + 직전 ATR14 그리고 종가 > EMA26; 조건 미충족; close=259.42, threshold=260.032, prior_ATR14=0.777474, EMA26=258.478 |
| v1 | session_vwap | 9698.55 | -301.45 | buy /  / 종가 > 뉴욕 거래일별 누적 전형가격 VWAP; 조건 충족; close=256.05, session_VWAP=255.552, session_volume=3.26826e+06 |
| v1 | obv_20 | 9489.05 | -510.95 | buy /  / OBV > OBV의 SMA20 그리고 종가 > EMA26; 조건 충족; OBV=8.59102e+06, OBV_SMA20=8.40759e+06, close=257.085, EMA26=256.499 |
| v1 | stochastic_14_3_recovery | 9576.18 | -423.82 | sell /  / 직전 %K14 < 20에서 %K14가 %D3 상향 돌파 (한 봉 목표); 조건 미충족; K14=33.4928, D3=23.2217, previous_K14=28.5165, previous_D3=14.8644 |
| v1 | mfi_14_recovery | 9925.14 | -74.86 | sell /  / 직전 MFI14 < 20, 현재 MFI14 >= 20 (한 봉 목표); 조건 미충족; MFI14=63.7046, previous_MFI14=52.8256 |
| v1 | adx_14_trend | 9681.33 | -318.67 | sell /  / Wilder ADX14 >= 25 그리고 +DI14 > -DI14; 조건 미충족; ADX14=33.0847, plus_DI14=22.751, minus_DI14=33.7106 |
| v1 | aroon_25_trend | 9899.46 | -100.54 | sell /  / Aroon25 Up > 70 그리고 Down < 30 (동률이면 최신 극값); 조건 미충족; Aroon_up=68, Aroon_down=44 |
| v1 | cci_20_momentum | 9822.54 | -177.46 | buy /  / CCI20 > 100 (전형가격·평균절대편차); 조건 충족; CCI20=114.549 |
| v1 | williams_14_recovery | 9706.89 | -293.11 | sell /  / 직전 Williams %R14 < -80, 현재 >= -80 (한 봉 목표); 조건 미충족; Williams_R14=-66.5072, previous_R14=-71.4835 |
| v1 | cmf_20_accumulation | 10060.68 | 60.68 | sell /  / Chaikin Money Flow20 > 0.1; 조건 미충족; CMF20=-0.0883438, volume20=4.47769e+06 |
| v1 | chaikin_3_10 | 9776.10 | -223.90 | buy /  / ADL의 EMA3 - EMA10 > 0 그리고 종가 > EMA26; 조건 충족; Chaikin3_10=8814.88, ADL=4.70768e+06, close=256.505, EMA26=256.405 |
| v1 | roc_10_momentum | 9691.76 | -308.24 | sell /  / 10봉 ROC > 1% 그리고 종가 > EMA26; 조건 미충족; ROC10_percent=-0.503419, close=258.91, EMA26=257.09 |
| v1 | trix_15_trend | 9665.05 | -334.95 | sell /  / 15봉 삼중 EMA의 1봉 변화율 TRIX > 0 그리고 종가 > EMA26; 조건 미충족; TRIX15_percent=0.0421187, close=256.41, EMA26=258.325 |
| v1 | keltner_20_breakout | 9916.04 | -83.96 | sell /  / 종가 > EMA20 + 2 x Wilder ATR14; 조건 미충족; close=258.91, upper_Keltner=259.564, EMA20=257.603, ATR14=0.980686 |
| v1 | opening_range_30m | 10000.00 | 0.00 | 대기 /  / 새 신호 대기 |
| v2 | cash | 10000.00 | 0.00 | 대기 /  / 새 신호 대기 |
| v2 | buy_hold | 9809.28 | -190.72 | 중단: 손실 한도 / buy / partial / 직전 완료 봉 목표 비중 100%; 다음 봉 시가 가정 |
| v2 | trend_8_26 | 9809.28 | -190.72 | 중단: 손실 한도 / buy / partial / 직전 완료 봉 목표 비중 100%; 다음 봉 시가 가정 |
| v2 | momentum_26 | 9809.28 | -190.72 | 중단: 손실 한도 / buy / partial / 직전 완료 봉 목표 비중 100%; 다음 봉 시가 가정 |
| v2 | breakout_8 | 9343.39 | -656.61 | 중단: 손실 한도 / sell / filled / 직전 완료 봉 목표 비중 0%; 다음 봉 시가 가정 |
| v2 | reversion_12 | 9434.41 | -565.59 | sell / filled / 직전 완료 봉 목표 비중 0%; 다음 봉 시가 가정 |
| v2 | volume_26 | 9686.16 | -313.84 | sell / filled / 직전 완료 봉 목표 비중 0%; 다음 봉 시가 가정 |
| v2 | trend_8_26 AND momentum_26 | 9809.28 | -190.72 | 중단: 손실 한도 / buy / partial / 직전 완료 봉 목표 비중 100%; 다음 봉 시가 가정 |
| v2 | trend_8_26 + momentum_26 | 9809.28 | -190.72 | 중단: 손실 한도 / buy / partial / 직전 완료 봉 목표 비중 100%; 다음 봉 시가 가정 |
| v2 | trend_8_26 AND breakout_8 | 9419.39 | -580.61 | 중단: 손실 한도 / sell / filled / 직전 완료 봉 목표 비중 0%; 다음 봉 시가 가정 |
| v2 | trend_8_26 + breakout_8 | 9255.64 | -744.36 | buy / partial / 직전 완료 봉 목표 비중 100%; 다음 봉 시가 가정 |
| v2 | trend_8_26 AND reversion_12 | 9900.89 | -99.11 | sell / filled / 직전 완료 봉 목표 비중 0%; 다음 봉 시가 가정 |
| v2 | trend_8_26 + reversion_12 | 9732.92 | -267.08 | 중단: 손실 한도 / sell / filled / 직전 완료 봉 목표 비중 0%; 다음 봉 시가 가정 |
| v2 | trend_8_26 AND volume_26 | 9861.95 | -138.05 | sell / filled / 직전 완료 봉 목표 비중 0%; 다음 봉 시가 가정 |
| v2 | trend_8_26 + volume_26 | 9878.71 | -121.29 | 중단: 손실 한도 / buy / filled / 직전 완료 봉 목표 비중 50%; 다음 봉 시가 가정 |
| v2 | momentum_26 AND breakout_8 | 9385.94 | -614.06 | sell / filled / 직전 완료 봉 목표 비중 0%; 다음 봉 시가 가정 |
| v2 | momentum_26 + breakout_8 | 9109.93 | -890.07 | sell / filled / 직전 완료 봉 목표 비중 50%; 다음 봉 시가 가정 |
| v2 | momentum_26 AND reversion_12 | 9871.83 | -128.17 | sell / filled / 직전 완료 봉 목표 비중 0%; 다음 봉 시가 가정 |
| v2 | momentum_26 + reversion_12 | 9732.92 | -267.08 | 중단: 손실 한도 / sell / filled / 직전 완료 봉 목표 비중 0%; 다음 봉 시가 가정 |
| v2 | momentum_26 AND volume_26 | 9920.93 | -79.07 | sell / filled / 직전 완료 봉 목표 비중 0%; 다음 봉 시가 가정 |
| v2 | momentum_26 + volume_26 | 9878.71 | -121.29 | 중단: 손실 한도 / buy / filled / 직전 완료 봉 목표 비중 50%; 다음 봉 시가 가정 |
| v2 | breakout_8 AND reversion_12 | 10000.00 | 0.00 | 대기 /  / 새 신호 대기 |
| v2 | breakout_8 + reversion_12 | 9137.45 | -862.55 | sell / filled / 직전 완료 봉 목표 비중 50%; 다음 봉 시가 가정 |
| v2 | breakout_8 AND volume_26 | 9814.17 | -185.83 | sell / filled / 직전 완료 봉 목표 비중 0%; 다음 봉 시가 가정 |
| v2 | breakout_8 + volume_26 | 9258.69 | -741.31 | sell / filled / 직전 완료 봉 목표 비중 50%; 다음 봉 시가 가정 |
| v2 | reversion_12 AND volume_26 | 9816.09 | -183.91 | sell / filled / 직전 완료 봉 목표 비중 0%; 다음 봉 시가 가정 |
| v2 | reversion_12 + volume_26 | 9599.90 | -400.10 | sell / filled / 직전 완료 봉 목표 비중 0%; 다음 봉 시가 가정 |
| v2 | ema_12_26 | 9764.26 | -235.74 | sell / filled / EMA12 > EMA26; 조건 미충족; EMA12=257.771, EMA26=257.934; 직전 완료 봉 목표를 다음 봉 시가에 모의 적용 |
| v2 | macd_12_26_9 | 9881.54 | -118.46 | sell / filled / MACD > 신호선 그리고 MACD > 0; 조건 미충족; MACD=1.30676, signal9=1.31668; 직전 완료 봉 목표를 다음 봉 시가에 모의 적용 |
| v2 | rsi_14_recovery | 9919.07 | -80.93 | sell / filled / 직전 RSI14 < 30, 현재 RSI14 >= 30 (한 봉 목표); 조건 미충족; RSI14=40.3665, previous_RSI14=36.2025; 직전 완료 봉 목표를 다음 봉 시가에 모의 적용 |
| v2 | bollinger_20_reentry | 9811.07 | -188.93 | sell / filled / 직전 종가 < 직전 하단밴드, 현재 하단밴드 <= 종가 <= SMA20 (한 봉 목표); 조건 미충족; close=255.05, lower20=254.819, SMA20=258.099, previous_lower20=255.312; 직전 완료 봉 목표를 다음 봉 시가에 모의 적용 |
| v2 | donchian_20 | 9881.11 | -118.89 | sell / filled / 종가 > 현재 봉을 제외한 직전 20봉 최고가; 조건 미충족; close=257.085, prior_high20=257.175; 직전 완료 봉 목표를 다음 봉 시가에 모의 적용 |
| v2 | atr_14_breakout | 9693.82 | -306.18 | sell / filled / 종가 > 직전 종가 + 직전 ATR14 그리고 종가 > EMA26; 조건 미충족; close=259.42, threshold=260.032, prior_ATR14=0.777474, EMA26=258.478; 직전 완료 봉 목표를 다음 봉 시가에 모의 적용 |
| v2 | session_vwap | 9680.14 | -319.86 | buy / partial / 종가 > 뉴욕 거래일별 누적 전형가격 VWAP; 조건 충족; close=256.05, session_VWAP=255.552, session_volume=3.26826e+06; 직전 완료 봉 목표를 다음 봉 시가에 모의 적용 |
| v2 | obv_20 | 9471.04 | -528.96 | buy / partial / OBV > OBV의 SMA20 그리고 종가 > EMA26; 조건 충족; OBV=8.59102e+06, OBV_SMA20=8.40759e+06, close=257.085, EMA26=256.499; 직전 완료 봉 목표를 다음 봉 시가에 모의 적용 |
| v2 | stochastic_14_3_recovery | 9560.87 | -439.13 | sell / filled / 직전 %K14 < 20에서 %K14가 %D3 상향 돌파 (한 봉 목표); 조건 미충족; K14=33.4928, D3=23.2217, previous_K14=28.5165, previous_D3=14.8644; 직전 완료 봉 목표를 다음 봉 시가에 모의 적용 |
| v2 | mfi_14_recovery | 9921.17 | -78.83 | sell / filled / 직전 MFI14 < 20, 현재 MFI14 >= 20 (한 봉 목표); 조건 미충족; MFI14=63.7046, previous_MFI14=52.8256; 직전 완료 봉 목표를 다음 봉 시가에 모의 적용 |
| v2 | adx_14_trend | 9673.58 | -326.42 | sell / filled / Wilder ADX14 >= 25 그리고 +DI14 > -DI14; 조건 미충족; ADX14=33.0847, plus_DI14=22.751, minus_DI14=33.7106; 직전 완료 봉 목표를 다음 봉 시가에 모의 적용 |
| v2 | aroon_25_trend | 9895.50 | -104.50 | sell / filled / Aroon25 Up > 70 그리고 Down < 30 (동률이면 최신 극값); 조건 미충족; Aroon_up=68, Aroon_down=44; 직전 완료 봉 목표를 다음 봉 시가에 모의 적용 |
| v2 | cci_20_momentum | 9815.67 | -184.33 | buy / partial / CCI20 > 100 (전형가격·평균절대편차); 조건 충족; CCI20=114.549; 직전 완료 봉 목표를 다음 봉 시가에 모의 적용 |
| v2 | williams_14_recovery | 9697.19 | -302.81 | sell / filled / 직전 Williams %R14 < -80, 현재 >= -80 (한 봉 목표); 조건 미충족; Williams_R14=-66.5072, previous_R14=-71.4835; 직전 완료 봉 목표를 다음 봉 시가에 모의 적용 |
| v2 | cmf_20_accumulation | 10056.66 | 56.66 | sell / filled / Chaikin Money Flow20 > 0.1; 조건 미충족; CMF20=-0.0883438, volume20=4.47769e+06; 직전 완료 봉 목표를 다음 봉 시가에 모의 적용 |
| v2 | chaikin_3_10 | 9767.31 | -232.69 | buy / partial / ADL의 EMA3 - EMA10 > 0 그리고 종가 > EMA26; 조건 충족; Chaikin3_10=8814.88, ADL=4.70768e+06, close=256.505, EMA26=256.405; 직전 완료 봉 목표를 다음 봉 시가에 모의 적용 |
| v2 | roc_10_momentum | 9684.01 | -315.99 | sell / filled / 10봉 ROC > 1% 그리고 종가 > EMA26; 조건 미충족; ROC10_percent=-0.503419, close=258.91, EMA26=257.09; 직전 완료 봉 목표를 다음 봉 시가에 모의 적용 |
| v2 | trix_15_trend | 9659.25 | -340.75 | sell / filled / 15봉 삼중 EMA의 1봉 변화율 TRIX > 0 그리고 종가 > EMA26; 조건 미충족; TRIX15_percent=0.0421187, close=256.41, EMA26=258.325; 직전 완료 봉 목표를 다음 봉 시가에 모의 적용 |
| v2 | keltner_20_breakout | 9914.05 | -85.95 | sell / filled / 종가 > EMA20 + 2 x Wilder ATR14; 조건 미충족; close=258.91, upper_Keltner=259.564, EMA20=257.603, ATR14=0.980686; 직전 완료 봉 목표를 다음 봉 시가에 모의 적용 |
| v2 | opening_range_30m | 10000.00 | 0.00 | 대기 /  / 새 신호 대기 |

### 같은 기간의 비용·노출 비교 (사후 연구)

| 전략 | 비용 전 | 비용 후 | 100% 보유 | 같은 평균 노출 보유 | 평균 노출 |
|---|---:|---:|---:|---:|---:|
| cash | 0.00% | 0.00% | -2.52% | -0.00% | 0.00% |
| buy_hold | -2.11% | -2.52% | -2.52% | -2.52% | 100.00% |
| trend_8_26 | 2.66% | 0.11% | -2.52% | -1.23% | 48.04% |
| momentum_26 | -0.86% | -3.74% | -2.52% | -1.17% | 45.95% |
| breakout_8 | -1.01% | -18.74% | -2.52% | -0.54% | 21.15% |
| reversion_12 | -5.58% | -13.55% | -2.52% | -0.73% | 28.46% |
| volume_26 | 0.16% | -6.35% | -2.52% | -0.15% | 5.74% |
| trend_8_26 AND momentum_26 | 0.79% | -1.72% | -2.52% | -1.04% | 40.47% |
| trend_8_26 + momentum_26 | 0.89% | -1.83% | -2.52% | -1.20% | 47.00% |
| trend_8_26 AND breakout_8 | 0.20% | -12.03% | -2.52% | -0.36% | 14.10% |
| trend_8_26 + breakout_8 | 0.84% | -9.59% | -2.52% | -0.89% | 34.60% |
| trend_8_26 AND reversion_12 | 1.37% | -1.98% | -2.52% | -0.15% | 5.74% |
| trend_8_26 + reversion_12 | -1.51% | -6.77% | -2.52% | -0.98% | 38.25% |
| trend_8_26 AND volume_26 | 1.42% | -1.10% | -2.52% | -0.04% | 1.57% |
| trend_8_26 + volume_26 | 1.44% | -2.95% | -2.52% | -0.69% | 26.90% |
| momentum_26 AND breakout_8 | 1.00% | -9.83% | -2.52% | -0.33% | 12.79% |
| momentum_26 + breakout_8 | -0.91% | -11.35% | -2.52% | -0.86% | 33.56% |
| momentum_26 AND reversion_12 | -0.27% | -3.16% | -2.52% | -0.16% | 6.27% |
| momentum_26 + reversion_12 | -3.22% | -8.19% | -2.52% | -0.95% | 37.21% |
| momentum_26 AND volume_26 | 0.14% | -0.70% | -2.52% | -0.01% | 0.52% |
| momentum_26 + volume_26 | -0.32% | -4.03% | -2.52% | -0.66% | 25.85% |
| breakout_8 AND reversion_12 | 0.00% | 0.00% | -2.52% | -0.00% | 0.00% |
| breakout_8 + reversion_12 | -3.30% | -15.84% | -2.52% | -0.64% | 24.81% |
| breakout_8 AND volume_26 | -0.46% | -1.29% | -2.52% | -0.01% | 0.52% |
| breakout_8 + volume_26 | -0.41% | -11.84% | -2.52% | -0.35% | 13.45% |
| reversion_12 AND volume_26 | -1.21% | -4.08% | -2.52% | -0.06% | 2.35% |
| reversion_12 + volume_26 | -2.74% | -9.45% | -2.52% | -0.44% | 17.11% |
| ema_12_26 | -1.05% | -3.51% | -2.52% | -1.19% | 46.48% |
| macd_12_26_9 | 5.83% | 2.76% | -2.52% | -0.75% | 29.24% |
| rsi_14_recovery | -1.35% | -6.20% | -2.52% | -0.08% | 3.13% |
| bollinger_20_reentry | -1.28% | -5.34% | -2.52% | -0.07% | 2.61% |
| donchian_20 | 0.72% | -6.61% | -2.52% | -0.18% | 6.79% |
| atr_14_breakout | 0.24% | -5.88% | -2.52% | -0.12% | 4.70% |
| session_vwap | 3.70% | -4.66% | -2.52% | -1.30% | 50.91% |
| obv_20 | -5.76% | -15.51% | -2.52% | -0.91% | 35.51% |
| stochastic_14_3_recovery | -0.85% | -12.95% | -2.52% | -0.21% | 8.09% |
| mfi_14_recovery | 0.38% | -1.71% | -2.52% | -0.03% | 1.31% |
| adx_14_trend | -3.61% | -8.35% | -2.52% | -0.94% | 36.55% |
| aroon_25_trend | 3.28% | -0.55% | -2.52% | -0.76% | 29.77% |
| cci_20_momentum | 0.82% | -5.34% | -2.52% | -0.53% | 20.63% |
| williams_14_recovery | -2.28% | -9.78% | -2.52% | -0.13% | 4.96% |
| cmf_20_accumulation | 4.00% | -0.27% | -2.52% | -0.88% | 34.46% |
| chaikin_3_10 | -3.20% | -8.35% | -2.52% | -0.98% | 38.38% |
| roc_10_momentum | -2.79% | -9.49% | -2.52% | -0.45% | 17.49% |
| trix_15_trend | -1.61% | -4.06% | -2.52% | -0.91% | 35.51% |
| keltner_20_breakout | 0.20% | -3.52% | -2.52% | -0.30% | 11.75% |
| opening_range_30m | 0.79% | -2.95% | -2.52% | -0.66% | 25.85% |

동일 구간·초기 자금, 종료 시 청산 비용 포함. 노출 맞춤은 사후 설명용이며 v2 실제 계좌 성과가 아닙니다.
[낙폭 분해·비용 영향·전체 구간](JNJ/comparison.json)

[v1 전체 기록](JNJ/accounts.json) · [v2 전체 기록](JNJ/accounts-v2.json)

## CAT 계좌

| 모델 | 전략 | 평가액 USD | 손익 USD | 최근 매매·이유 |
|---|---|---:|---:|---|
| v1 | cash | 10000.00 | 0.00 | 대기 /  / 새 신호 대기 |
| v1 | buy_hold | 10039.49 | 39.49 | buy /  / buy_hold: prior completed bar target 100%; next bar open simulation |
| v1 | trend_8_26 | 9961.53 | -38.47 | buy /  / trend_8_26: prior completed bar target 100%; next bar open simulation |
| v1 | momentum_26 | 9670.15 | -329.85 | buy /  / momentum_26: prior completed bar target 100%; next bar open simulation |
| v1 | breakout_8 | 9544.96 | -455.04 | sell /  / breakout_8: prior completed bar target 0%; next bar open simulation |
| v1 | reversion_12 | 9913.39 | -86.61 | sell /  / reversion_12: prior completed bar target 0%; next bar open simulation |
| v1 | volume_26 | 9916.22 | -83.78 | sell /  / volume_26: prior completed bar target 0%; next bar open simulation |
| v1 | trend_8_26 AND momentum_26 | 9858.16 | -141.84 | buy /  / trend_8_26 AND momentum_26: prior completed bar target 100%; next bar open simulation |
| v1 | trend_8_26 + momentum_26 | 9815.84 | -184.16 | buy /  / trend_8_26 + momentum_26: prior completed bar target 100%; next bar open simulation |
| v1 | trend_8_26 AND breakout_8 | 9747.92 | -252.08 | sell /  / trend_8_26 AND breakout_8: prior completed bar target 0%; next bar open simulation |
| v1 | trend_8_26 + breakout_8 | 9752.12 | -247.88 | sell /  / trend_8_26 + breakout_8: prior completed bar target 50%; next bar open simulation |
| v1 | trend_8_26 AND reversion_12 | 9919.62 | -80.38 | sell /  / trend_8_26 AND reversion_12: prior completed bar target 0%; next bar open simulation |
| v1 | trend_8_26 + reversion_12 | 9978.80 | -21.20 | sell /  / trend_8_26 + reversion_12: prior completed bar target 50%; next bar open simulation |
| v1 | trend_8_26 AND volume_26 | 9965.69 | -34.31 | sell /  / trend_8_26 AND volume_26: prior completed bar target 0%; next bar open simulation |
| v1 | trend_8_26 + volume_26 | 9959.66 | -40.34 | sell /  / trend_8_26 + volume_26: prior completed bar target 50%; next bar open simulation |
| v1 | momentum_26 AND breakout_8 | 9615.85 | -384.15 | sell /  / momentum_26 AND breakout_8: prior completed bar target 0%; next bar open simulation |
| v1 | momentum_26 + breakout_8 | 9607.46 | -392.54 | sell /  / momentum_26 + breakout_8: prior completed bar target 50%; next bar open simulation |
| v1 | momentum_26 AND reversion_12 | 9878.81 | -121.19 | sell /  / momentum_26 AND reversion_12: prior completed bar target 0%; next bar open simulation |
| v1 | momentum_26 + reversion_12 | 9791.62 | -208.38 | sell /  / momentum_26 + reversion_12: prior completed bar target 50%; next bar open simulation |
| v1 | momentum_26 AND volume_26 | 9894.55 | -105.45 | sell /  / momentum_26 AND volume_26: prior completed bar target 0%; next bar open simulation |
| v1 | momentum_26 + volume_26 | 9792.38 | -207.62 | sell /  / momentum_26 + volume_26: prior completed bar target 50%; next bar open simulation |
| v1 | breakout_8 AND reversion_12 | 10000.00 | 0.00 | 대기 /  / 새 신호 대기 |
| v1 | breakout_8 + reversion_12 | 9727.90 | -272.10 | sell /  / breakout_8 + reversion_12: prior completed bar target 0%; next bar open simulation |
| v1 | breakout_8 AND volume_26 | 9894.55 | -105.45 | sell /  / breakout_8 AND volume_26: prior completed bar target 0%; next bar open simulation |
| v1 | breakout_8 + volume_26 | 9728.78 | -271.22 | sell /  / breakout_8 + volume_26: prior completed bar target 0%; next bar open simulation |
| v1 | reversion_12 AND volume_26 | 10046.29 | 46.29 | sell /  / reversion_12 AND volume_26: prior completed bar target 0%; next bar open simulation |
| v1 | reversion_12 + volume_26 | 9915.24 | -84.76 | sell /  / reversion_12 + volume_26: prior completed bar target 0%; next bar open simulation |
| v1 | ema_12_26 | 9989.70 | -10.30 | buy /  / EMA12 > EMA26; 조건 충족; EMA12=726.261, EMA26=726.172 |
| v1 | macd_12_26_9 | 9988.51 | -11.49 | sell /  / MACD > 신호선 그리고 MACD > 0; 조건 미충족; MACD=2.92675, signal9=3.02629 |
| v1 | rsi_14_recovery | 9999.22 | -0.78 | sell /  / 직전 RSI14 < 30, 현재 RSI14 >= 30 (한 봉 목표); 조건 미충족; RSI14=43.621, previous_RSI14=38.5787 |
| v1 | bollinger_20_reentry | 9777.09 | -222.91 | sell /  / 직전 종가 < 직전 하단밴드, 현재 하단밴드 <= 종가 <= SMA20 (한 봉 목표); 조건 미충족; close=721.16, lower20=716.851, SMA20=725.821, previous_lower20=717.276 |
| v1 | donchian_20 | 9943.28 | -56.72 | sell /  / 종가 > 현재 봉을 제외한 직전 20봉 최고가; 조건 미충족; close=735.35, prior_high20=745 |
| v1 | atr_14_breakout | 9768.31 | -231.69 | sell /  / 종가 > 직전 종가 + 직전 ATR14 그리고 종가 > EMA26; 조건 미충족; close=735.35, threshold=737.263, prior_ATR14=4.10289, EMA26=727.331 |
| v1 | session_vwap | 9635.07 | -364.93 | buy /  / 종가 > 뉴욕 거래일별 누적 전형가격 VWAP; 조건 충족; close=734.98, session_VWAP=734.093, session_volume=764353 |
| v1 | obv_20 | 9931.04 | -68.96 | buy /  / OBV > OBV의 SMA20 그리고 종가 > EMA26; 조건 충족; OBV=-5.0567e+06, OBV_SMA20=-6.30537e+06, close=733.16, EMA26=726.69 |
| v1 | stochastic_14_3_recovery | 9855.08 | -144.92 | sell /  / 직전 %K14 < 20에서 %K14가 %D3 상향 돌파 (한 봉 목표); 조건 미충족; K14=59.6496, D3=39.2535, previous_K14=43.8356, previous_D3=33.8642 |
| v1 | mfi_14_recovery | 10068.63 | 68.63 | sell /  / 직전 MFI14 < 20, 현재 MFI14 >= 20 (한 봉 목표); 조건 미충족; MFI14=32.7313, previous_MFI14=24.1736 |
| v1 | adx_14_trend | 10006.92 | 6.92 | buy /  / Wilder ADX14 >= 25 그리고 +DI14 > -DI14; 조건 충족; ADX14=25.4031, plus_DI14=35.2628, minus_DI14=13.9603 |
| v1 | aroon_25_trend | 9979.61 | -20.39 | sell /  / Aroon25 Up > 70 그리고 Down < 30 (동률이면 최신 극값); 조건 미충족; Aroon_up=68, Aroon_down=20 |
| v1 | cci_20_momentum | 9862.85 | -137.15 | sell /  / CCI20 > 100 (전형가격·평균절대편차); 조건 미충족; CCI20=99.2123 |
| v1 | williams_14_recovery | 10007.06 | 7.06 | sell /  / 직전 Williams %R14 < -80, 현재 >= -80 (한 봉 목표); 조건 미충족; Williams_R14=-40.3504, previous_R14=-56.1644 |
| v1 | cmf_20_accumulation | 9844.52 | -155.48 | buy /  / Chaikin Money Flow20 > 0.1; 조건 충족; CMF20=0.145111, volume20=965726 |
| v1 | chaikin_3_10 | 9618.06 | -381.94 | buy /  / ADL의 EMA3 - EMA10 > 0 그리고 종가 > EMA26; 조건 충족; Chaikin3_10=8419.46, ADL=-5.25074e+06, close=739.39, EMA26=736.067 |
| v1 | roc_10_momentum | 9896.73 | -103.27 | sell /  / 10봉 ROC > 1% 그리고 종가 > EMA26; 조건 미충족; ROC10_percent=0.883016, close=741.47, EMA26=734.681 |
| v1 | trix_15_trend | 9722.13 | -277.87 | buy /  / 15봉 삼중 EMA의 1봉 변화율 TRIX > 0 그리고 종가 > EMA26; 조건 충족; TRIX15_percent=0.00081134, close=733.16, EMA26=726.69 |
| v1 | keltner_20_breakout | 10000.00 | 0.00 | 대기 /  / 새 신호 대기 |
| v1 | opening_range_30m | 10162.22 | 162.22 | sell /  / 뉴욕 09:30·09:45 두 완료 봉 최고가를 10:00 이후 종가가 돌파; 자료 부족·변동폭 또는 거래량 없음: 대기; close=733.16 |
| v2 | cash | 10000.00 | 0.00 | 대기 /  / 새 신호 대기 |
| v2 | buy_hold | 9233.06 | -766.94 | 중단: 손실 한도 / buy / partial / 직전 완료 봉 목표 비중 100%; 다음 봉 시가 가정 |
| v2 | trend_8_26 | 9879.62 | -120.38 | buy / partial / 직전 완료 봉 목표 비중 100%; 다음 봉 시가 가정 |
| v2 | momentum_26 | 9671.68 | -328.32 | buy / partial / 직전 완료 봉 목표 비중 100%; 다음 봉 시가 가정 |
| v2 | breakout_8 | 9357.29 | -642.71 | sell / filled / 직전 완료 봉 목표 비중 0%; 다음 봉 시가 가정 |
| v2 | reversion_12 | 9104.12 | -895.88 | 중단: 손실 한도 / buy / partial / 직전 완료 봉 목표 비중 100%; 다음 봉 시가 가정 |
| v2 | volume_26 | 9364.49 | -635.51 | 중단: 손실 한도 / buy / partial / 직전 완료 봉 목표 비중 100%; 다음 봉 시가 가정 |
| v2 | trend_8_26 AND momentum_26 | 9894.20 | -105.80 | buy / partial / 직전 완료 봉 목표 비중 100%; 다음 봉 시가 가정 |
| v2 | trend_8_26 + momentum_26 | 9776.15 | -223.85 | buy / partial / 직전 완료 봉 목표 비중 100%; 다음 봉 시가 가정 |
| v2 | trend_8_26 AND breakout_8 | 9655.84 | -344.16 | sell / filled / 직전 완료 봉 목표 비중 0%; 다음 봉 시가 가정 |
| v2 | trend_8_26 + breakout_8 | 9616.24 | -383.76 | sell / filled / 직전 완료 봉 목표 비중 50%; 다음 봉 시가 가정 |
| v2 | trend_8_26 AND reversion_12 | 9728.39 | -271.61 | sell / filled / 직전 완료 봉 목표 비중 0%; 다음 봉 시가 가정 |
| v2 | trend_8_26 + reversion_12 | 9593.70 | -406.30 | sell / filled / 직전 완료 봉 목표 비중 50%; 다음 봉 시가 가정 |
| v2 | trend_8_26 AND volume_26 | 9999.01 | -0.99 | sell / filled / 직전 완료 봉 목표 비중 0%; 다음 봉 시가 가정 |
| v2 | trend_8_26 + volume_26 | 9586.96 | -413.04 | sell / filled / 직전 완료 봉 목표 비중 50%; 다음 봉 시가 가정 |
| v2 | momentum_26 AND breakout_8 | 9576.90 | -423.10 | sell / filled / 직전 완료 봉 목표 비중 0%; 다음 봉 시가 가정 |
| v2 | momentum_26 + breakout_8 | 9513.48 | -486.52 | sell / filled / 직전 완료 봉 목표 비중 50%; 다음 봉 시가 가정 |
| v2 | momentum_26 AND reversion_12 | 9745.30 | -254.70 | sell / filled / 직전 완료 봉 목표 비중 0%; 다음 봉 시가 가정 |
| v2 | momentum_26 + reversion_12 | 9451.54 | -548.46 | sell / filled / 직전 완료 봉 목표 비중 50%; 다음 봉 시가 가정 |
| v2 | momentum_26 AND volume_26 | 9936.85 | -63.15 | sell / filled / 직전 완료 봉 목표 비중 0%; 다음 봉 시가 가정 |
| v2 | momentum_26 + volume_26 | 9484.65 | -515.35 | sell / filled / 직전 완료 봉 목표 비중 50%; 다음 봉 시가 가정 |
| v2 | breakout_8 AND reversion_12 | 10000.00 | 0.00 | 대기 /  / 새 신호 대기 |
| v2 | breakout_8 + reversion_12 | 9610.18 | -389.82 | 중단: 손실 한도 / sell / filled / 직전 완료 봉 목표 비중 0%; 다음 봉 시가 가정 |
| v2 | breakout_8 AND volume_26 | 9887.31 | -112.69 | sell / filled / 직전 완료 봉 목표 비중 0%; 다음 봉 시가 가정 |
| v2 | breakout_8 + volume_26 | 9329.36 | -670.64 | sell / filled / 직전 완료 봉 목표 비중 0%; 다음 봉 시가 가정 |
| v2 | reversion_12 AND volume_26 | 9299.71 | -700.29 | 중단: 손실 한도 / buy / partial / 직전 완료 봉 목표 비중 100%; 다음 봉 시가 가정 |
| v2 | reversion_12 + volume_26 | 9415.05 | -584.95 | 중단: 손실 한도 / sell / filled / 직전 완료 봉 목표 비중 50%; 다음 봉 시가 가정 |
| v2 | ema_12_26 | 9986.70 | -13.30 | buy / partial / EMA12 > EMA26; 조건 충족; EMA12=726.261, EMA26=726.172; 직전 완료 봉 목표를 다음 봉 시가에 모의 적용 |
| v2 | macd_12_26_9 | 9984.52 | -15.48 | sell / filled / MACD > 신호선 그리고 MACD > 0; 조건 미충족; MACD=2.92675, signal9=3.02629; 직전 완료 봉 목표를 다음 봉 시가에 모의 적용 |
| v2 | rsi_14_recovery | 9995.22 | -4.78 | sell / filled / 직전 RSI14 < 30, 현재 RSI14 >= 30 (한 봉 목표); 조건 미충족; RSI14=43.621, previous_RSI14=38.5787; 직전 완료 봉 목표를 다음 봉 시가에 모의 적용 |
| v2 | bollinger_20_reentry | 9771.22 | -228.78 | sell / filled / 직전 종가 < 직전 하단밴드, 현재 하단밴드 <= 종가 <= SMA20 (한 봉 목표); 조건 미충족; close=721.16, lower20=716.851, SMA20=725.821, previous_lower20=717.276; 직전 완료 봉 목표를 다음 봉 시가에 모의 적용 |
| v2 | donchian_20 | 9939.30 | -60.70 | sell / filled / 종가 > 현재 봉을 제외한 직전 20봉 최고가; 조건 미충족; close=735.35, prior_high20=745; 직전 완료 봉 목표를 다음 봉 시가에 모의 적용 |
| v2 | atr_14_breakout | 9758.55 | -241.45 | sell / filled / 종가 > 직전 종가 + 직전 ATR14 그리고 종가 > EMA26; 조건 미충족; close=735.35, threshold=737.263, prior_ATR14=4.10289, EMA26=727.331; 직전 완료 봉 목표를 다음 봉 시가에 모의 적용 |
| v2 | session_vwap | 9616.78 | -383.22 | buy / partial / 종가 > 뉴욕 거래일별 누적 전형가격 VWAP; 조건 충족; close=734.98, session_VWAP=734.093, session_volume=764353; 직전 완료 봉 목표를 다음 봉 시가에 모의 적용 |
| v2 | obv_20 | 9920.12 | -79.88 | buy / partial / OBV > OBV의 SMA20 그리고 종가 > EMA26; 조건 충족; OBV=-5.0567e+06, OBV_SMA20=-6.30537e+06, close=733.16, EMA26=726.69; 직전 완료 봉 목표를 다음 봉 시가에 모의 적용 |
| v2 | stochastic_14_3_recovery | 9843.26 | -156.74 | sell / filled / 직전 %K14 < 20에서 %K14가 %D3 상향 돌파 (한 봉 목표); 조건 미충족; K14=59.6496, D3=39.2535, previous_K14=43.8356, previous_D3=33.8642; 직전 완료 봉 목표를 다음 봉 시가에 모의 적용 |
| v2 | mfi_14_recovery | 10064.61 | 64.61 | sell / filled / 직전 MFI14 < 20, 현재 MFI14 >= 20 (한 봉 목표); 조건 미충족; MFI14=32.7313, previous_MFI14=24.1736; 직전 완료 봉 목표를 다음 봉 시가에 모의 적용 |
| v2 | adx_14_trend | 10005.92 | 5.92 | buy / partial / Wilder ADX14 >= 25 그리고 +DI14 > -DI14; 조건 충족; ADX14=25.4031, plus_DI14=35.2628, minus_DI14=13.9603; 직전 완료 봉 목표를 다음 봉 시가에 모의 적용 |
| v2 | aroon_25_trend | 9973.62 | -26.38 | sell / filled / Aroon25 Up > 70 그리고 Down < 30 (동률이면 최신 극값); 조건 미충족; Aroon_up=68, Aroon_down=20; 직전 완료 봉 목표를 다음 봉 시가에 모의 적용 |
| v2 | cci_20_momentum | 9854.97 | -145.03 | sell / filled / CCI20 > 100 (전형가격·평균절대편차); 조건 미충족; CCI20=99.2123; 직전 완료 봉 목표를 다음 봉 시가에 모의 적용 |
| v2 | williams_14_recovery | 9999.06 | -0.94 | sell / filled / 직전 Williams %R14 < -80, 현재 >= -80 (한 봉 목표); 조건 미충족; Williams_R14=-40.3504, previous_R14=-56.1644; 직전 완료 봉 목표를 다음 봉 시가에 모의 적용 |
| v2 | cmf_20_accumulation | 9835.67 | -164.33 | buy / partial / Chaikin Money Flow20 > 0.1; 조건 충족; CMF20=0.145111, volume20=965726; 직전 완료 봉 목표를 다음 봉 시가에 모의 적용 |
| v2 | chaikin_3_10 | 9723.76 | -276.24 | 중단: 손실 한도 / buy / partial / ADL의 EMA3 - EMA10 > 0 그리고 종가 > EMA26; 조건 충족; Chaikin3_10=293683, ADL=-4.91156e+06, close=739.58, EMA26=736.187; 직전 완료 봉 목표를 다음 봉 시가에 모의 적용 |
| v2 | roc_10_momentum | 9888.81 | -111.19 | sell / filled / 10봉 ROC > 1% 그리고 종가 > EMA26; 조건 미충족; ROC10_percent=0.883016, close=741.47, EMA26=734.681; 직전 완료 봉 목표를 다음 봉 시가에 모의 적용 |
| v2 | trix_15_trend | 9733.56 | -266.44 | 중단: 손실 한도 / buy / partial / 15봉 삼중 EMA의 1봉 변화율 TRIX > 0 그리고 종가 > EMA26; 조건 충족; TRIX15_percent=0.0196284, close=739.58, EMA26=736.187; 직전 완료 봉 목표를 다음 봉 시가에 모의 적용 |
| v2 | keltner_20_breakout | 10000.00 | 0.00 | 대기 /  / 새 신호 대기 |
| v2 | opening_range_30m | 10158.15 | 158.15 | sell / filled / 뉴욕 09:30·09:45 두 완료 봉 최고가를 10:00 이후 종가가 돌파; 자료 부족·변동폭 또는 거래량 없음: 대기; close=733.16; 직전 완료 봉 목표를 다음 봉 시가에 모의 적용 |

### 같은 기간의 비용·노출 비교 (사후 연구)

| 전략 | 비용 전 | 비용 후 | 100% 보유 | 같은 평균 노출 보유 | 평균 노출 |
|---|---:|---:|---:|---:|---:|
| cash | 0.00% | 0.00% | -9.65% | -0.00% | 0.00% |
| buy_hold | -9.27% | -9.65% | -9.65% | -9.65% | 100.00% |
| trend_8_26 | 1.64% | -2.13% | -9.65% | -4.81% | 48.83% |
| momentum_26 | -0.93% | -5.40% | -9.65% | -4.66% | 47.26% |
| breakout_8 | -2.74% | -15.33% | -9.65% | -1.64% | 16.45% |
| reversion_12 | -2.91% | -15.12% | -9.65% | -2.47% | 24.80% |
| volume_26 | -1.31% | -8.50% | -9.65% | -0.78% | 7.83% |
| trend_8_26 AND momentum_26 | 2.25% | -1.13% | -9.65% | -4.13% | 41.78% |
| trend_8_26 + momentum_26 | 0.37% | -3.76% | -9.65% | -4.73% | 48.04% |
| trend_8_26 AND breakout_8 | -1.46% | -9.02% | -9.65% | -0.97% | 9.66% |
| trend_8_26 + breakout_8 | -0.53% | -8.75% | -9.65% | -3.24% | 32.64% |
| trend_8_26 AND reversion_12 | 0.96% | -5.20% | -9.65% | -0.55% | 5.48% |
| trend_8_26 + reversion_12 | -0.58% | -8.05% | -9.65% | -3.64% | 36.82% |
| trend_8_26 AND volume_26 | 2.90% | 1.18% | -9.65% | -0.16% | 1.57% |
| trend_8_26 + volume_26 | 0.21% | -4.94% | -9.65% | -2.81% | 28.33% |
| momentum_26 AND breakout_8 | -2.00% | -10.27% | -9.65% | -1.02% | 10.18% |
| momentum_26 + breakout_8 | -1.80% | -10.47% | -9.65% | -3.16% | 31.86% |
| momentum_26 AND reversion_12 | -2.85% | -8.78% | -9.65% | -0.63% | 6.27% |
| momentum_26 + reversion_12 | -1.87% | -10.37% | -9.65% | -3.57% | 36.04% |
| momentum_26 AND volume_26 | 2.69% | 0.55% | -9.65% | -0.16% | 1.57% |
| momentum_26 + volume_26 | -1.06% | -6.55% | -9.65% | -2.74% | 27.55% |
| breakout_8 AND reversion_12 | 0.00% | 0.00% | -9.65% | -0.00% | 0.00% |
| breakout_8 + reversion_12 | -2.77% | -14.49% | -9.65% | -2.05% | 20.64% |
| breakout_8 AND volume_26 | 0.55% | -1.13% | -9.65% | -0.10% | 1.04% |
| breakout_8 + volume_26 | -2.00% | -11.41% | -9.65% | -1.21% | 12.15% |
| reversion_12 AND volume_26 | -0.64% | -4.73% | -9.65% | -0.47% | 4.70% |
| reversion_12 + volume_26 | -2.07% | -11.48% | -9.65% | -1.63% | 16.32% |
| ema_12_26 | 1.38% | -0.31% | -9.65% | -4.43% | 44.91% |
| macd_12_26_9 | 3.45% | 0.87% | -9.65% | -2.90% | 29.24% |
| rsi_14_recovery | 0.45% | -5.28% | -9.65% | -0.37% | 3.66% |
| bollinger_20_reentry | 0.07% | -4.85% | -9.65% | -0.31% | 3.13% |
| donchian_20 | -0.84% | -4.91% | -9.65% | -0.47% | 4.70% |
| atr_14_breakout | -1.06% | -6.71% | -9.65% | -0.39% | 3.92% |
| session_vwap | 3.85% | -8.83% | -9.65% | -5.01% | 50.91% |
| obv_20 | -0.89% | -10.39% | -9.65% | -2.52% | 25.33% |
| stochastic_14_3_recovery | -1.09% | -10.57% | -9.65% | -0.63% | 6.27% |
| mfi_14_recovery | 2.16% | -0.38% | -9.65% | -0.16% | 1.57% |
| adx_14_trend | -1.75% | -4.20% | -9.65% | -1.20% | 12.01% |
| aroon_25_trend | 0.17% | -3.54% | -9.65% | -1.15% | 11.49% |
| cci_20_momentum | -3.05% | -8.21% | -9.65% | -1.67% | 16.71% |
| williams_14_recovery | 0.42% | -6.50% | -9.65% | -0.44% | 4.44% |
| cmf_20_accumulation | -3.12% | -10.17% | -9.65% | -1.90% | 19.06% |
| chaikin_3_10 | -2.75% | -12.07% | -9.65% | -3.24% | 32.64% |
| roc_10_momentum | -1.16% | -7.58% | -9.65% | -1.43% | 14.36% |
| trix_15_trend | -0.01% | -4.12% | -9.65% | -3.54% | 35.77% |
| keltner_20_breakout | -2.87% | -5.29% | -9.65% | -0.26% | 2.61% |
| opening_range_30m | 8.07% | 3.62% | -9.65% | -2.57% | 25.85% |

동일 구간·초기 자금, 종료 시 청산 비용 포함. 노출 맞춤은 사후 설명용이며 v2 실제 계좌 성과가 아닙니다.
[낙폭 분해·비용 영향·전체 구간](CAT/comparison.json)

[v1 전체 기록](CAT/accounts.json) · [v2 전체 기록](CAT/accounts-v2.json)

## WMT 계좌

| 모델 | 전략 | 평가액 USD | 손익 USD | 최근 매매·이유 |
|---|---|---:|---:|---|
| v1 | cash | 10000.00 | 0.00 | 대기 /  / 새 신호 대기 |
| v1 | buy_hold | 9937.79 | -62.21 | buy /  / buy_hold: prior completed bar target 100%; next bar open simulation |
| v1 | trend_8_26 | 9730.44 | -269.56 | sell /  / trend_8_26: prior completed bar target 0%; next bar open simulation |
| v1 | momentum_26 | 9801.37 | -198.63 | sell /  / momentum_26: prior completed bar target 0%; next bar open simulation |
| v1 | breakout_8 | 9638.48 | -361.52 | sell /  / breakout_8: prior completed bar target 0%; next bar open simulation |
| v1 | reversion_12 | 9594.11 | -405.89 | buy /  / reversion_12: prior completed bar target 100%; next bar open simulation |
| v1 | volume_26 | 9761.42 | -238.58 | sell /  / volume_26: prior completed bar target 0%; next bar open simulation |
| v1 | trend_8_26 AND momentum_26 | 9811.64 | -188.36 | sell /  / trend_8_26 AND momentum_26: prior completed bar target 0%; next bar open simulation |
| v1 | trend_8_26 + momentum_26 | 9765.84 | -234.16 | sell /  / trend_8_26 + momentum_26: prior completed bar target 0%; next bar open simulation |
| v1 | trend_8_26 AND breakout_8 | 9854.29 | -145.71 | sell /  / trend_8_26 AND breakout_8: prior completed bar target 0%; next bar open simulation |
| v1 | trend_8_26 + breakout_8 | 9703.77 | -296.23 | sell /  / trend_8_26 + breakout_8: prior completed bar target 0%; next bar open simulation |
| v1 | trend_8_26 AND reversion_12 | 9741.18 | -258.82 | sell /  / trend_8_26 AND reversion_12: prior completed bar target 0%; next bar open simulation |
| v1 | trend_8_26 + reversion_12 | 9700.94 | -299.06 | buy /  / trend_8_26 + reversion_12: prior completed bar target 50%; next bar open simulation |
| v1 | trend_8_26 AND volume_26 | 9837.96 | -162.04 | sell /  / trend_8_26 AND volume_26: prior completed bar target 0%; next bar open simulation |
| v1 | trend_8_26 + volume_26 | 9746.15 | -253.85 | sell /  / trend_8_26 + volume_26: prior completed bar target 0%; next bar open simulation |
| v1 | momentum_26 AND breakout_8 | 9816.19 | -183.81 | sell /  / momentum_26 AND breakout_8: prior completed bar target 0%; next bar open simulation |
| v1 | momentum_26 + breakout_8 | 9778.26 | -221.74 | sell /  / momentum_26 + breakout_8: prior completed bar target 0%; next bar open simulation |
| v1 | momentum_26 AND reversion_12 | 9935.88 | -64.12 | sell /  / momentum_26 AND reversion_12: prior completed bar target 0%; next bar open simulation |
| v1 | momentum_26 + reversion_12 | 9794.65 | -205.35 | buy /  / momentum_26 + reversion_12: prior completed bar target 50%; next bar open simulation |
| v1 | momentum_26 AND volume_26 | 9905.94 | -94.06 | sell /  / momentum_26 AND volume_26: prior completed bar target 0%; next bar open simulation |
| v1 | momentum_26 + volume_26 | 9820.75 | -179.25 | sell /  / momentum_26 + volume_26: prior completed bar target 0%; next bar open simulation |
| v1 | breakout_8 AND reversion_12 | 10000.00 | 0.00 | 대기 /  / 새 신호 대기 |
| v1 | breakout_8 + reversion_12 | 9654.67 | -345.33 | buy /  / breakout_8 + reversion_12: prior completed bar target 50%; next bar open simulation |
| v1 | breakout_8 AND volume_26 | 9850.09 | -149.91 | sell /  / breakout_8 AND volume_26: prior completed bar target 0%; next bar open simulation |
| v1 | breakout_8 + volume_26 | 9699.80 | -300.20 | sell /  / breakout_8 + volume_26: prior completed bar target 0%; next bar open simulation |
| v1 | reversion_12 AND volume_26 | 9911.53 | -88.47 | sell /  / reversion_12 AND volume_26: prior completed bar target 0%; next bar open simulation |
| v1 | reversion_12 + volume_26 | 9716.12 | -283.88 | buy /  / reversion_12 + volume_26: prior completed bar target 50%; next bar open simulation |
| v1 | ema_12_26 | 9906.58 | -93.42 | sell /  / EMA12 > EMA26; 조건 미충족; EMA12=118.808, EMA26=118.852 |
| v1 | macd_12_26_9 | 9985.46 | -14.54 | sell /  / MACD > 신호선 그리고 MACD > 0; 조건 미충족; MACD=0.122825, signal9=0.127837 |
| v1 | rsi_14_recovery | 9973.19 | -26.81 | sell /  / 직전 RSI14 < 30, 현재 RSI14 >= 30 (한 봉 목표); 조건 미충족; RSI14=46.7246, previous_RSI14=43.1348 |
| v1 | bollinger_20_reentry | 9874.49 | -125.51 | sell /  / 직전 종가 < 직전 하단밴드, 현재 하단밴드 <= 종가 <= SMA20 (한 봉 목표); 조건 미충족; close=117.94, lower20=117.359, SMA20=117.989, previous_lower20=117.365 |
| v1 | donchian_20 | 9935.97 | -64.03 | sell /  / 종가 > 현재 봉을 제외한 직전 20봉 최고가; 조건 미충족; close=119.52, prior_high20=120.5 |
| v1 | atr_14_breakout | 9915.82 | -84.18 | sell /  / 종가 > 직전 종가 + 직전 ATR14 그리고 종가 > EMA26; 조건 미충족; close=119.52, threshold=120.186, prior_ATR14=0.395874, EMA26=118.952 |
| v1 | session_vwap | 9658.67 | -341.33 | sell /  / 종가 > 뉴욕 거래일별 누적 전형가격 VWAP; 조건 미충족; close=117.56, session_VWAP=117.695, session_volume=6.9888e+06 |
| v1 | obv_20 | 9857.61 | -142.39 | sell /  / OBV > OBV의 SMA20 그리고 종가 > EMA26; 조건 미충족; OBV=1.5985e+07, OBV_SMA20=1.72435e+07, close=118.945, EMA26=118.951 |
| v1 | stochastic_14_3_recovery | 9483.89 | -516.11 | buy /  / 직전 %K14 < 20에서 %K14가 %D3 상향 돌파 (한 봉 목표); 조건 충족; K14=8.66597, D3=7.09962, previous_K14=6.3493, previous_D3=8.69815 |
| v1 | mfi_14_recovery | 9868.10 | -131.90 | sell /  / 직전 MFI14 < 20, 현재 MFI14 >= 20 (한 봉 목표); 조건 미충족; MFI14=23.7816, previous_MFI14=20.1936 |
| v1 | adx_14_trend | 9991.69 | -8.31 | sell /  / Wilder ADX14 >= 25 그리고 +DI14 > -DI14; 조건 미충족; ADX14=24.5142, plus_DI14=24.7537, minus_DI14=21.6519 |
| v1 | aroon_25_trend | 9947.63 | -52.37 | sell /  / Aroon25 Up > 70 그리고 Down < 30 (동률이면 최신 극값); 조건 미충족; Aroon_up=68, Aroon_down=4 |
| v1 | cci_20_momentum | 9772.81 | -227.19 | sell /  / CCI20 > 100 (전형가격·평균절대편차); 조건 미충족; CCI20=38.8365 |
| v1 | williams_14_recovery | 9640.68 | -359.32 | sell /  / 직전 Williams %R14 < -80, 현재 >= -80 (한 봉 목표); 조건 미충족; Williams_R14=-58.2078, previous_R14=-71.8266 |
| v1 | cmf_20_accumulation | 9755.34 | -244.66 | sell /  / Chaikin Money Flow20 > 0.1; 조건 미충족; CMF20=0.0843695, volume20=6.48078e+06 |
| v1 | chaikin_3_10 | 9712.46 | -287.54 | sell /  / ADL의 EMA3 - EMA10 > 0 그리고 종가 > EMA26; 조건 미충족; Chaikin3_10=126716, ADL=1.03877e+07, close=117.95, EMA26=118.04 |
| v1 | roc_10_momentum | 10000.00 | 0.00 | 대기 /  / 새 신호 대기 |
| v1 | trix_15_trend | 9708.65 | -291.35 | sell /  / 15봉 삼중 EMA의 1봉 변화율 TRIX > 0 그리고 종가 > EMA26; 조건 미충족; TRIX15_percent=0.0142754, close=118.77, EMA26=118.947 |
| v1 | keltner_20_breakout | 9935.97 | -64.03 | sell /  / 종가 > EMA20 + 2 x Wilder ATR14; 조건 미충족; close=119.52, upper_Keltner=119.83, EMA20=119.013, ATR14=0.408312 |
| v1 | opening_range_30m | 9785.85 | -214.15 | sell /  / 뉴욕 09:30·09:45 두 완료 봉 최고가를 10:00 이후 종가가 돌파; 조건 미충족; close=117.89, opening_high=117.96 |
| v2 | cash | 10000.00 | 0.00 | 대기 /  / 새 신호 대기 |
| v2 | buy_hold | 10529.00 | 529.00 | buy / partial / 직전 완료 봉 목표 비중 100%; 다음 봉 시가 가정 |
| v2 | trend_8_26 | 10121.89 | 121.89 | sell / filled / 직전 완료 봉 목표 비중 0%; 다음 봉 시가 가정 |
| v2 | momentum_26 | 10200.51 | 200.51 | sell / filled / 직전 완료 봉 목표 비중 0%; 다음 봉 시가 가정 |
| v2 | breakout_8 | 9589.05 | -410.95 | sell / filled / 직전 완료 봉 목표 비중 0%; 다음 봉 시가 가정 |
| v2 | reversion_12 | 9487.29 | -512.71 | buy / partial / 직전 완료 봉 목표 비중 100%; 다음 봉 시가 가정 |
| v2 | volume_26 | 9715.86 | -284.14 | sell / filled / 직전 완료 봉 목표 비중 0%; 다음 봉 시가 가정 |
| v2 | trend_8_26 AND momentum_26 | 10206.36 | 206.36 | sell / filled / 직전 완료 봉 목표 비중 0%; 다음 봉 시가 가정 |
| v2 | trend_8_26 + momentum_26 | 10161.07 | 161.07 | sell / filled / 직전 완료 봉 목표 비중 0%; 다음 봉 시가 가정 |
| v2 | trend_8_26 AND breakout_8 | 9935.59 | -64.41 | sell / filled / 직전 완료 봉 목표 비중 0%; 다음 봉 시가 가정 |
| v2 | trend_8_26 + breakout_8 | 9872.99 | -127.01 | sell / filled / 직전 완료 봉 목표 비중 0%; 다음 봉 시가 가정 |
| v2 | trend_8_26 AND reversion_12 | 9545.32 | -454.68 | sell / filled / 직전 완료 봉 목표 비중 0%; 다음 봉 시가 가정 |
| v2 | trend_8_26 + reversion_12 | 9842.26 | -157.74 | buy / filled / 직전 완료 봉 목표 비중 50%; 다음 봉 시가 가정 |
| v2 | trend_8_26 AND volume_26 | 9784.10 | -215.90 | sell / filled / 직전 완료 봉 목표 비중 0%; 다음 봉 시가 가정 |
| v2 | trend_8_26 + volume_26 | 9918.44 | -81.56 | sell / filled / 직전 완료 봉 목표 비중 0%; 다음 봉 시가 가정 |
| v2 | momentum_26 AND breakout_8 | 9773.67 | -226.33 | sell / filled / 직전 완료 봉 목표 비중 0%; 다음 봉 시가 가정 |
| v2 | momentum_26 + breakout_8 | 9953.12 | -46.88 | sell / filled / 직전 완료 봉 목표 비중 0%; 다음 봉 시가 가정 |
| v2 | momentum_26 AND reversion_12 | 9759.91 | -240.09 | sell / filled / 직전 완료 봉 목표 비중 0%; 다음 봉 시가 가정 |
| v2 | momentum_26 + reversion_12 | 9984.57 | -15.43 | buy / filled / 직전 완료 봉 목표 비중 50%; 다음 봉 시가 가정 |
| v2 | momentum_26 AND volume_26 | 9814.68 | -185.32 | sell / filled / 직전 완료 봉 목표 비중 0%; 다음 봉 시가 가정 |
| v2 | momentum_26 + volume_26 | 9998.77 | -1.23 | sell / filled / 직전 완료 봉 목표 비중 0%; 다음 봉 시가 가정 |
| v2 | breakout_8 AND reversion_12 | 10000.00 | 0.00 | 대기 /  / 새 신호 대기 |
| v2 | breakout_8 + reversion_12 | 9599.26 | -400.74 | buy / filled / 직전 완료 봉 목표 비중 50%; 다음 봉 시가 가정 |
| v2 | breakout_8 AND volume_26 | 9795.19 | -204.81 | sell / filled / 직전 완료 봉 목표 비중 0%; 다음 봉 시가 가정 |
| v2 | breakout_8 + volume_26 | 9653.61 | -346.39 | sell / filled / 직전 완료 봉 목표 비중 0%; 다음 봉 시가 가정 |
| v2 | reversion_12 AND volume_26 | 9917.25 | -82.75 | sell / filled / 직전 완료 봉 목표 비중 0%; 다음 봉 시가 가정 |
| v2 | reversion_12 + volume_26 | 9641.11 | -358.89 | buy / filled / 직전 완료 봉 목표 비중 50%; 다음 봉 시가 가정 |
| v2 | ema_12_26 | 9902.61 | -97.39 | sell / filled / EMA12 > EMA26; 조건 미충족; EMA12=118.808, EMA26=118.852; 직전 완료 봉 목표를 다음 봉 시가에 모의 적용 |
| v2 | macd_12_26_9 | 9981.46 | -18.54 | sell / filled / MACD > 신호선 그리고 MACD > 0; 조건 미충족; MACD=0.122825, signal9=0.127837; 직전 완료 봉 목표를 다음 봉 시가에 모의 적용 |
| v2 | rsi_14_recovery | 9971.19 | -28.81 | sell / filled / 직전 RSI14 < 30, 현재 RSI14 >= 30 (한 봉 목표); 조건 미충족; RSI14=46.7246, previous_RSI14=43.1348; 직전 완료 봉 목표를 다음 봉 시가에 모의 적용 |
| v2 | bollinger_20_reentry | 9868.57 | -131.43 | sell / filled / 직전 종가 < 직전 하단밴드, 현재 하단밴드 <= 종가 <= SMA20 (한 봉 목표); 조건 미충족; close=117.94, lower20=117.359, SMA20=117.989, previous_lower20=117.365; 직전 완료 봉 목표를 다음 봉 시가에 모의 적용 |
| v2 | donchian_20 | 9933.99 | -66.01 | sell / filled / 종가 > 현재 봉을 제외한 직전 20봉 최고가; 조건 미충족; close=119.52, prior_high20=120.5; 직전 완료 봉 목표를 다음 봉 시가에 모의 적용 |
| v2 | atr_14_breakout | 9911.85 | -88.15 | sell / filled / 종가 > 직전 종가 + 직전 ATR14 그리고 종가 > EMA26; 조건 미충족; close=119.52, threshold=120.186, prior_ATR14=0.395874, EMA26=118.952; 직전 완료 봉 목표를 다음 봉 시가에 모의 적용 |
| v2 | session_vwap | 9641.30 | -358.70 | sell / filled / 종가 > 뉴욕 거래일별 누적 전형가격 VWAP; 조건 미충족; close=117.56, session_VWAP=117.695, session_volume=6.9888e+06; 직전 완료 봉 목표를 다음 봉 시가에 모의 적용 |
| v2 | obv_20 | 9847.76 | -152.24 | sell / filled / OBV > OBV의 SMA20 그리고 종가 > EMA26; 조건 미충족; OBV=1.6238e+07, OBV_SMA20=1.74966e+07, close=118.945, EMA26=118.951; 직전 완료 봉 목표를 다음 봉 시가에 모의 적용 |
| v2 | stochastic_14_3_recovery | 9642.84 | -357.16 | 중단: 손실 한도 / buy / partial / 직전 %K14 < 20에서 %K14가 %D3 상향 돌파 (한 봉 목표); 조건 충족; K14=25.6758, D3=22.4971, previous_K14=12.8379, previous_D3=25.8704; 직전 완료 봉 목표를 다음 봉 시가에 모의 적용 |
| v2 | mfi_14_recovery | 9862.18 | -137.82 | sell / filled / 직전 MFI14 < 20, 현재 MFI14 >= 20 (한 봉 목표); 조건 미충족; MFI14=23.7816, previous_MFI14=20.1936; 직전 완료 봉 목표를 다음 봉 시가에 모의 적용 |
| v2 | adx_14_trend | 9989.70 | -10.30 | sell / filled / Wilder ADX14 >= 25 그리고 +DI14 > -DI14; 조건 미충족; ADX14=24.5142, plus_DI14=24.7537, minus_DI14=21.6519; 직전 완료 봉 목표를 다음 봉 시가에 모의 적용 |
| v2 | aroon_25_trend | 9943.65 | -56.35 | sell / filled / Aroon25 Up > 70 그리고 Down < 30 (동률이면 최신 극값); 조건 미충족; Aroon_up=68, Aroon_down=4; 직전 완료 봉 목표를 다음 봉 시가에 모의 적용 |
| v2 | cci_20_momentum | 9766.95 | -233.05 | sell / filled / CCI20 > 100 (전형가격·평균절대편차); 조건 미충족; CCI20=38.8365; 직전 완료 봉 목표를 다음 봉 시가에 모의 적용 |
| v2 | williams_14_recovery | 9629.12 | -370.88 | sell / filled / 직전 Williams %R14 < -80, 현재 >= -80 (한 봉 목표); 조건 미충족; Williams_R14=-58.2078, previous_R14=-71.8266; 직전 완료 봉 목표를 다음 봉 시가에 모의 적용 |
| v2 | cmf_20_accumulation | 9743.64 | -256.36 | sell / filled / Chaikin Money Flow20 > 0.1; 조건 미충족; CMF20=0.0843695, volume20=6.48078e+06; 직전 완료 봉 목표를 다음 봉 시가에 모의 적용 |
| v2 | chaikin_3_10 | 9696.93 | -303.07 | sell / filled / ADL의 EMA3 - EMA10 > 0 그리고 종가 > EMA26; 조건 미충족; Chaikin3_10=126716, ADL=1.03877e+07, close=117.95, EMA26=118.04; 직전 완료 봉 목표를 다음 봉 시가에 모의 적용 |
| v2 | roc_10_momentum | 10000.00 | 0.00 | 대기 /  / 새 신호 대기 |
| v2 | trix_15_trend | 9697.01 | -302.99 | sell / filled / 15봉 삼중 EMA의 1봉 변화율 TRIX > 0 그리고 종가 > EMA26; 조건 미충족; TRIX15_percent=0.0142754, close=118.77, EMA26=118.947; 직전 완료 봉 목표를 다음 봉 시가에 모의 적용 |
| v2 | keltner_20_breakout | 9933.99 | -66.01 | sell / filled / 종가 > EMA20 + 2 x Wilder ATR14; 조건 미충족; close=119.52, upper_Keltner=119.83, EMA20=119.013, ATR14=0.408312; 직전 완료 봉 목표를 다음 봉 시가에 모의 적용 |
| v2 | opening_range_30m | 9778.02 | -221.98 | sell / filled / 뉴욕 09:30·09:45 두 완료 봉 최고가를 10:00 이후 종가가 돌파; 조건 미충족; close=117.89, opening_high=117.96; 직전 완료 봉 목표를 다음 봉 시가에 모의 적용 |

### 같은 기간의 비용·노출 비교 (사후 연구)

| 전략 | 비용 전 | 비용 후 | 100% 보유 | 같은 평균 노출 보유 | 평균 노출 |
|---|---:|---:|---:|---:|---:|
| cash | 0.00% | 0.00% | 12.19% | 0.00% | 0.00% |
| buy_hold | 12.67% | 12.19% | 12.19% | 12.19% | 100.00% |
| trend_8_26 | 8.68% | 5.09% | 12.19% | 8.25% | 69.19% |
| momentum_26 | 10.44% | 5.02% | 12.19% | 8.29% | 69.45% |
| breakout_8 | 5.98% | -10.79% | 12.19% | 2.96% | 25.59% |
| reversion_12 | 4.09% | -7.07% | 12.19% | 2.13% | 18.54% |
| volume_26 | 1.64% | -4.17% | 12.19% | 0.60% | 5.22% |
| trend_8_26 AND momentum_26 | 8.65% | 4.18% | 12.19% | 7.38% | 62.14% |
| trend_8_26 + momentum_26 | 9.56% | 5.05% | 12.19% | 8.27% | 69.32% |
| trend_8_26 AND breakout_8 | 6.59% | -6.43% | 12.19% | 2.41% | 20.89% |
| trend_8_26 + breakout_8 | 7.33% | -2.96% | 12.19% | 5.57% | 47.40% |
| trend_8_26 AND reversion_12 | 0.15% | -5.97% | 12.19% | 0.83% | 7.31% |
| trend_8_26 + reversion_12 | 6.40% | -0.54% | 12.19% | 5.14% | 43.87% |
| trend_8_26 AND volume_26 | 0.24% | -2.26% | 12.19% | 0.24% | 2.09% |
| trend_8_26 + volume_26 | 5.13% | 0.79% | 12.19% | 4.34% | 37.21% |
| momentum_26 AND breakout_8 | 6.62% | -7.18% | 12.19% | 2.62% | 22.72% |
| momentum_26 + breakout_8 | 8.20% | -2.38% | 12.19% | 5.58% | 47.53% |
| momentum_26 AND reversion_12 | 1.65% | -4.16% | 12.19% | 0.83% | 7.31% |
| momentum_26 + reversion_12 | 7.26% | 1.33% | 12.19% | 5.16% | 44.00% |
| momentum_26 AND volume_26 | 1.64% | -2.54% | 12.19% | 0.33% | 2.87% |
| momentum_26 + volume_26 | 5.99% | 0.76% | 12.19% | 4.36% | 37.34% |
| breakout_8 AND reversion_12 | 0.00% | 0.00% | 12.19% | 0.00% | 0.00% |
| breakout_8 + reversion_12 | 5.06% | -8.17% | 12.19% | 2.55% | 22.07% |
| breakout_8 AND volume_26 | 0.78% | -2.14% | 12.19% | 0.24% | 2.09% |
| breakout_8 + volume_26 | 3.81% | -7.33% | 12.19% | 1.77% | 15.41% |
| reversion_12 AND volume_26 | 0.01% | -2.48% | 12.19% | 0.21% | 1.83% |
| reversion_12 + volume_26 | 2.87% | -5.03% | 12.19% | 1.36% | 11.88% |
| ema_12_26 | 11.20% | 9.81% | 12.19% | 8.65% | 72.32% |
| macd_12_26_9 | 8.67% | 4.64% | 12.19% | 4.20% | 36.03% |
| rsi_14_recovery | 0.20% | -0.64% | 12.19% | 0.06% | 0.52% |
| bollinger_20_reentry | 1.19% | -1.33% | 12.19% | 0.18% | 1.57% |
| donchian_20 | 4.55% | -7.44% | 12.19% | 1.47% | 12.79% |
| atr_14_breakout | -0.90% | -10.40% | 12.19% | 0.83% | 7.31% |
| session_vwap | 9.19% | -1.69% | 12.19% | 7.09% | 59.79% |
| obv_20 | 10.62% | 3.00% | 12.19% | 6.57% | 55.61% |
| stochastic_14_3_recovery | 0.14% | -8.70% | 12.19% | 0.66% | 5.74% |
| mfi_14_recovery | 0.05% | -1.61% | 12.19% | 0.12% | 1.04% |
| adx_14_trend | 8.73% | 6.47% | 12.19% | 5.84% | 49.61% |
| aroon_25_trend | 7.01% | 2.18% | 12.19% | 3.61% | 31.07% |
| cci_20_momentum | 6.31% | -1.85% | 12.19% | 3.64% | 31.33% |
| williams_14_recovery | -0.53% | -8.55% | 12.19% | 0.60% | 5.22% |
| cmf_20_accumulation | 9.21% | -0.01% | 12.19% | 4.61% | 39.43% |
| chaikin_3_10 | 9.72% | 0.88% | 12.19% | 6.06% | 51.44% |
| roc_10_momentum | -0.29% | -4.79% | 12.19% | 1.59% | 13.84% |
| trix_15_trend | 10.97% | 6.86% | 12.19% | 7.67% | 64.49% |
| keltner_20_breakout | 6.59% | 0.08% | 12.19% | 3.05% | 26.37% |
| opening_range_30m | 9.50% | 3.24% | 12.19% | 4.39% | 37.60% |

동일 구간·초기 자금, 종료 시 청산 비용 포함. 노출 맞춤은 사후 설명용이며 v2 실제 계좌 성과가 아닙니다.
[낙폭 분해·비용 영향·전체 구간](WMT/comparison.json)

[v1 전체 기록](WMT/accounts.json) · [v2 전체 기록](WMT/accounts-v2.json)
