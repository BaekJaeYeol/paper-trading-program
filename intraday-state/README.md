# 모의투자 운영 현황

[PC·서버 장애 진단과 복구 방법](https://github.com/BaekJaeYeol/paper-trading-program/blob/main/investment-lab/docs/failure-recovery.md)

이번 실행 복구: {}

완료 봉 확인 주기: 기록 5/13회 · 기록 없는 예정 8회 · 아직 판정 전 13회 · 주의: 예약 시작 지연 또는 실행·저장 누락을 확인하세요.

[주기 판정 기준](https://github.com/BaekJaeYeol/paper-trading-program/blob/main/investment-lab/docs/session-coverage.md)

최근 확인: 2026-10-22T17:07:00.568027+00:00 (UTC)
다음 15분 확인 목표 (세션 실행 중에만 적용): 2026-10-22T17:22:00+00:00 (UTC, 실행 지연 가능)

실제 주문 없음. v1 기존 계좌와 v2 새 계좌의 시작일이 다르므로 수익률을 직접 우열 비교하지 마세요.
v2는 다음 봉 시가에 비용·스프레드·직전 거래량 제한을 적용한 가상 체결입니다. 미체결 잔량은 만료됩니다.

| 종목 | 상태 | 최근 성공 UTC | 마지막 완료 봉 UTC | 이번 새 봉 |
|---|---|---|---|---|
| SPY | updated | 2026-10-22T17:07:00.568027+00:00 | 2026-10-22T16:45:00+00:00 | 1 |
| QQQ | updated | 2026-10-22T17:07:00.568027+00:00 | 2026-10-22T16:45:00+00:00 | 1 |
| IWM | updated | 2026-10-22T17:07:00.568027+00:00 | 2026-10-22T16:45:00+00:00 | 1 |
| DIA | updated | 2026-10-22T17:07:00.568027+00:00 | 2026-10-22T16:45:00+00:00 | 1 |
| MSFT | updated | 2026-10-22T17:07:00.568027+00:00 | 2026-10-22T16:45:00+00:00 | 1 |
| JPM | updated | 2026-10-22T17:07:00.568027+00:00 | 2026-10-22T16:45:00+00:00 | 1 |
| XOM | updated | 2026-10-22T17:07:00.568027+00:00 | 2026-10-22T16:45:00+00:00 | 1 |
| JNJ | updated | 2026-10-22T17:07:00.568027+00:00 | 2026-10-22T16:45:00+00:00 | 1 |
| CAT | updated | 2026-10-22T17:07:00.568027+00:00 | 2026-10-22T16:45:00+00:00 | 1 |
| WMT | updated | 2026-10-22T17:07:00.568027+00:00 | 2026-10-22T16:45:00+00:00 | 1 |

이번 실행 소요: 40.04초
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
| v1 | buy_hold | 9857.42 | -142.58 | buy /  / buy_hold: prior completed bar target 100%; next bar open simulation |
| v1 | trend_8_26 | 9711.09 | -288.91 | sell /  / trend_8_26: prior completed bar target 0%; next bar open simulation |
| v1 | momentum_26 | 9631.54 | -368.46 | sell /  / momentum_26: prior completed bar target 0%; next bar open simulation |
| v1 | breakout_8 | 9503.28 | -496.72 | sell /  / breakout_8: prior completed bar target 0%; next bar open simulation |
| v1 | reversion_12 | 9619.35 | -380.65 | sell /  / reversion_12: prior completed bar target 0%; next bar open simulation |
| v1 | volume_26 | 9438.20 | -561.80 | sell /  / volume_26: prior completed bar target 0%; next bar open simulation |
| v1 | trend_8_26 AND momentum_26 | 9624.28 | -375.72 | sell /  / trend_8_26 AND momentum_26: prior completed bar target 0%; next bar open simulation |
| v1 | trend_8_26 + momentum_26 | 9671.22 | -328.78 | sell /  / trend_8_26 + momentum_26: prior completed bar target 0%; next bar open simulation |
| v1 | trend_8_26 AND breakout_8 | 9730.71 | -269.29 | sell /  / trend_8_26 AND breakout_8: prior completed bar target 0%; next bar open simulation |
| v1 | trend_8_26 + breakout_8 | 9645.08 | -354.92 | sell /  / trend_8_26 + breakout_8: prior completed bar target 0%; next bar open simulation |
| v1 | trend_8_26 AND reversion_12 | 9736.23 | -263.77 | sell /  / trend_8_26 AND reversion_12: prior completed bar target 0%; next bar open simulation |
| v1 | trend_8_26 + reversion_12 | 9664.97 | -335.03 | sell /  / trend_8_26 + reversion_12: prior completed bar target 0%; next bar open simulation |
| v1 | trend_8_26 AND volume_26 | 9605.36 | -394.64 | sell /  / trend_8_26 AND volume_26: prior completed bar target 0%; next bar open simulation |
| v1 | trend_8_26 + volume_26 | 9573.57 | -426.43 | sell /  / trend_8_26 + volume_26: prior completed bar target 0%; next bar open simulation |
| v1 | momentum_26 AND breakout_8 | 9640.01 | -359.99 | sell /  / momentum_26 AND breakout_8: prior completed bar target 0%; next bar open simulation |
| v1 | momentum_26 + breakout_8 | 9567.24 | -432.76 | sell /  / momentum_26 + breakout_8: prior completed bar target 0%; next bar open simulation |
| v1 | momentum_26 AND reversion_12 | 9769.70 | -230.30 | sell /  / momentum_26 AND reversion_12: prior completed bar target 0%; next bar open simulation |
| v1 | momentum_26 + reversion_12 | 9683.27 | -316.73 | sell /  / momentum_26 + reversion_12: prior completed bar target 0%; next bar open simulation |
| v1 | momentum_26 AND volume_26 | 9618.73 | -381.27 | sell /  / momentum_26 AND volume_26: prior completed bar target 0%; next bar open simulation |
| v1 | momentum_26 + volume_26 | 9534.28 | -465.72 | sell /  / momentum_26 + volume_26: prior completed bar target 0%; next bar open simulation |
| v1 | breakout_8 AND reversion_12 | 10000.00 | 0.00 | 대기 /  / 새 신호 대기 |
| v1 | breakout_8 + reversion_12 | 9560.78 | -439.22 | sell /  / breakout_8 + reversion_12: prior completed bar target 0%; next bar open simulation |
| v1 | breakout_8 AND volume_26 | 9837.59 | -162.41 | sell /  / breakout_8 AND volume_26: prior completed bar target 0%; next bar open simulation |
| v1 | breakout_8 + volume_26 | 9508.37 | -491.63 | sell /  / breakout_8 + volume_26: prior completed bar target 0%; next bar open simulation |
| v1 | reversion_12 AND volume_26 | 9811.81 | -188.19 | sell /  / reversion_12 AND volume_26: prior completed bar target 0%; next bar open simulation |
| v1 | reversion_12 + volume_26 | 9547.19 | -452.81 | sell /  / reversion_12 + volume_26: prior completed bar target 0%; next bar open simulation |
| v1 | ema_12_26 | 9742.51 | -257.49 | sell /  / EMA12 > EMA26; 조건 미충족; EMA12=771.277, EMA26=771.539 |
| v1 | macd_12_26_9 | 9769.55 | -230.45 | sell /  / MACD > 신호선 그리고 MACD > 0; 조건 미충족; MACD=1.03945, signal9=1.12358 |
| v1 | rsi_14_recovery | 9805.98 | -194.02 | sell /  / 직전 RSI14 < 30, 현재 RSI14 >= 30 (한 봉 목표); 조건 미충족; RSI14=38.7389, previous_RSI14=37.2051 |
| v1 | bollinger_20_reentry | 9787.44 | -212.56 | sell /  / 직전 종가 < 직전 하단밴드, 현재 하단밴드 <= 종가 <= SMA20 (한 봉 목표); 조건 미충족; close=762.71, lower20=761.42, SMA20=770.302, previous_lower20=762.585 |
| v1 | donchian_20 | 9818.08 | -181.92 | sell /  / 종가 > 현재 봉을 제외한 직전 20봉 최고가; 조건 미충족; close=774.19, prior_high20=774.44 |
| v1 | atr_14_breakout | 9816.89 | -183.11 | sell /  / 종가 > 직전 종가 + 직전 ATR14 그리고 종가 > EMA26; 조건 미충족; close=773.07, threshold=774.291, prior_ATR14=1.05565, EMA26=772.249 |
| v1 | session_vwap | 9464.46 | -535.54 | sell /  / 종가 > 뉴욕 거래일별 누적 전형가격 VWAP; 조건 미충족; close=763.06, session_VWAP=764.207, session_volume=6.24478e+07 |
| v1 | obv_20 | 9597.93 | -402.07 | sell /  / OBV > OBV의 SMA20 그리고 종가 > EMA26; 조건 미충족; OBV=-949325, OBV_SMA20=-1.03221e+07, close=766.62, EMA26=771.893 |
| v1 | stochastic_14_3_recovery | 9624.33 | -375.67 | sell /  / 직전 %K14 < 20에서 %K14가 %D3 상향 돌파 (한 봉 목표); 조건 미충족; K14=9.33394, D3=8.42378, previous_K14=10.9938, previous_D3=8.71605 |
| v1 | mfi_14_recovery | 9810.25 | -189.75 | sell /  / 직전 MFI14 < 20, 현재 MFI14 >= 20 (한 봉 목표); 조건 미충족; MFI14=24.2496, previous_MFI14=22.3876 |
| v1 | adx_14_trend | 9981.96 | -18.04 | sell /  / Wilder ADX14 >= 25 그리고 +DI14 > -DI14; 조건 미충족; ADX14=24.2312, plus_DI14=28.3519, minus_DI14=24.6578 |
| v1 | aroon_25_trend | 9728.66 | -271.34 | sell /  / Aroon25 Up > 70 그리고 Down < 30 (동률이면 최신 극값); 조건 미충족; Aroon_up=72, Aroon_down=100 |
| v1 | cci_20_momentum | 9766.23 | -233.77 | sell /  / CCI20 > 100 (전형가격·평균절대편차); 조건 미충족; CCI20=97.3932 |
| v1 | williams_14_recovery | 9614.06 | -385.94 | sell /  / 직전 Williams %R14 < -80, 현재 >= -80 (한 봉 목표); 조건 미충족; Williams_R14=-74.6558, previous_R14=-77.3303 |
| v1 | cmf_20_accumulation | 9690.93 | -309.07 | sell /  / Chaikin Money Flow20 > 0.1; 조건 미충족; CMF20=0.0473512, volume20=7.32623e+07 |
| v1 | chaikin_3_10 | 9565.38 | -434.62 | sell /  / ADL의 EMA3 - EMA10 > 0 그리고 종가 > EMA26; 조건 미충족; Chaikin3_10=1.08024e+06, ADL=4.99714e+07, close=766.62, EMA26=771.893 |
| v1 | roc_10_momentum | 9953.42 | -46.58 | sell /  / 10봉 ROC > 1% 그리고 종가 > EMA26; 조건 미충족; ROC10_percent=0.806376, close=769.45, EMA26=767.181 |
| v1 | trix_15_trend | 9489.99 | -510.01 | sell /  / 15봉 삼중 EMA의 1봉 변화율 TRIX > 0 그리고 종가 > EMA26; 조건 미충족; TRIX15_percent=0.0154379, close=766.62, EMA26=771.893 |
| v1 | keltner_20_breakout | 9810.90 | -189.10 | sell /  / 종가 > EMA20 + 2 x Wilder ATR14; 조건 미충족; close=774.19, upper_Keltner=774.31, EMA20=772.615, ATR14=0.847257 |
| v1 | opening_range_30m | 9651.00 | -349.00 | sell /  / 뉴욕 09:30·09:45 두 완료 봉 최고가를 10:00 이후 종가가 돌파; 자료 부족·변동폭 또는 거래량 없음: 대기; close=766.62 |
| v2 | cash | 10000.00 | 0.00 | 대기 /  / 새 신호 대기 |
| v2 | buy_hold | 9786.31 | -213.69 | buy / partial / 직전 완료 봉 목표 비중 100%; 다음 봉 시가 가정 |
| v2 | trend_8_26 | 9591.24 | -408.76 | sell / filled / 직전 완료 봉 목표 비중 0%; 다음 봉 시가 가정 |
| v2 | momentum_26 | 9482.22 | -517.78 | sell / filled / 직전 완료 봉 목표 비중 0%; 다음 봉 시가 가정 |
| v2 | breakout_8 | 9099.96 | -900.04 | sell / filled / 직전 완료 봉 목표 비중 0%; 다음 봉 시가 가정 |
| v2 | reversion_12 | 9154.53 | -845.47 | sell / filled / 직전 완료 봉 목표 비중 0%; 다음 봉 시가 가정 |
| v2 | volume_26 | 8996.01 | -1003.99 | 중단: 손실 한도 / buy / partial / 직전 완료 봉 목표 비중 100%; 다음 봉 시가 가정 |
| v2 | trend_8_26 AND momentum_26 | 9481.53 | -518.47 | sell / filled / 직전 완료 봉 목표 비중 0%; 다음 봉 시가 가정 |
| v2 | trend_8_26 + momentum_26 | 9536.57 | -463.43 | sell / filled / 직전 완료 봉 목표 비중 0%; 다음 봉 시가 가정 |
| v2 | trend_8_26 AND breakout_8 | 9547.25 | -452.75 | sell / filled / 직전 완료 봉 목표 비중 0%; 다음 봉 시가 가정 |
| v2 | trend_8_26 + breakout_8 | 9381.53 | -618.47 | sell / filled / 직전 완료 봉 목표 비중 0%; 다음 봉 시가 가정 |
| v2 | trend_8_26 AND reversion_12 | 9621.61 | -378.39 | sell / filled / 직전 완료 봉 목표 비중 0%; 다음 봉 시가 가정 |
| v2 | trend_8_26 + reversion_12 | 9369.89 | -630.11 | sell / filled / 직전 완료 봉 목표 비중 0%; 다음 봉 시가 가정 |
| v2 | trend_8_26 AND volume_26 | 9442.22 | -557.78 | sell / filled / 직전 완료 봉 목표 비중 0%; 다음 봉 시가 가정 |
| v2 | trend_8_26 + volume_26 | 9252.87 | -747.13 | sell / filled / 직전 완료 봉 목표 비중 0%; 다음 봉 시가 가정 |
| v2 | momentum_26 AND breakout_8 | 9414.38 | -585.62 | sell / filled / 직전 완료 봉 목표 비중 0%; 다음 봉 시가 가정 |
| v2 | momentum_26 + breakout_8 | 9289.09 | -710.91 | sell / filled / 직전 완료 봉 목표 비중 0%; 다음 봉 시가 가정 |
| v2 | momentum_26 AND reversion_12 | 9722.08 | -277.92 | sell / filled / 직전 완료 봉 목표 비중 0%; 다음 봉 시가 가정 |
| v2 | momentum_26 + reversion_12 | 9395.12 | -604.88 | sell / filled / 직전 완료 봉 목표 비중 0%; 다음 봉 시가 가정 |
| v2 | momentum_26 AND volume_26 | 9523.88 | -476.12 | sell / filled / 직전 완료 봉 목표 비중 0%; 다음 봉 시가 가정 |
| v2 | momentum_26 + volume_26 | 9238.83 | -761.17 | sell / filled / 직전 완료 봉 목표 비중 0%; 다음 봉 시가 가정 |
| v2 | breakout_8 AND reversion_12 | 10000.00 | 0.00 | 대기 /  / 새 신호 대기 |
| v2 | breakout_8 + reversion_12 | 9164.83 | -835.17 | sell / filled / 직전 완료 봉 목표 비중 0%; 다음 봉 시가 가정 |
| v2 | breakout_8 AND volume_26 | 9765.99 | -234.01 | sell / filled / 직전 완료 봉 목표 비중 0%; 다음 봉 시가 가정 |
| v2 | breakout_8 + volume_26 | 9069.44 | -930.56 | sell / filled / 직전 완료 봉 목표 비중 0%; 다음 봉 시가 가정 |
| v2 | reversion_12 AND volume_26 | 9552.33 | -447.67 | sell / filled / 직전 완료 봉 목표 비중 0%; 다음 봉 시가 가정 |
| v2 | reversion_12 + volume_26 | 9115.84 | -884.16 | sell / filled / 직전 완료 봉 목표 비중 0%; 다음 봉 시가 가정 |
| v2 | ema_12_26 | 9736.67 | -263.33 | sell / filled / EMA12 > EMA26; 조건 미충족; EMA12=771.277, EMA26=771.539; 직전 완료 봉 목표를 다음 봉 시가에 모의 적용 |
| v2 | macd_12_26_9 | 9761.73 | -238.27 | sell / filled / MACD > 신호선 그리고 MACD > 0; 조건 미충족; MACD=1.03945, signal9=1.12358; 직전 완료 봉 목표를 다음 봉 시가에 모의 적용 |
| v2 | rsi_14_recovery | 9798.14 | -201.86 | sell / filled / 직전 RSI14 < 30, 현재 RSI14 >= 30 (한 봉 목표); 조건 미충족; RSI14=38.7389, previous_RSI14=37.2051; 직전 완료 봉 목표를 다음 봉 시가에 모의 적용 |
| v2 | bollinger_20_reentry | 9779.61 | -220.39 | sell / filled / 직전 종가 < 직전 하단밴드, 현재 하단밴드 <= 종가 <= SMA20 (한 봉 목표); 조건 미충족; close=762.71, lower20=761.42, SMA20=770.302, previous_lower20=762.585; 직전 완료 봉 목표를 다음 봉 시가에 모의 적용 |
| v2 | donchian_20 | 9808.27 | -191.73 | sell / filled / 종가 > 현재 봉을 제외한 직전 20봉 최고가; 조건 미충족; close=774.19, prior_high20=774.44; 직전 완료 봉 목표를 다음 봉 시가에 모의 적용 |
| v2 | atr_14_breakout | 9807.08 | -192.92 | sell / filled / 종가 > 직전 종가 + 직전 ATR14 그리고 종가 > EMA26; 조건 미충족; close=773.07, threshold=774.291, prior_ATR14=1.05565, EMA26=772.249; 직전 완료 봉 목표를 다음 봉 시가에 모의 적용 |
| v2 | session_vwap | 9445.55 | -554.45 | sell / filled / 종가 > 뉴욕 거래일별 누적 전형가격 VWAP; 조건 미충족; close=763.06, session_VWAP=764.207, session_volume=6.24478e+07; 직전 완료 봉 목표를 다음 봉 시가에 모의 적용 |
| v2 | obv_20 | 9584.50 | -415.50 | sell / filled / OBV > OBV의 SMA20 그리고 종가 > EMA26; 조건 미충족; OBV=-949325, OBV_SMA20=-1.03221e+07, close=766.62, EMA26=771.893; 직전 완료 봉 목표를 다음 봉 시가에 모의 적용 |
| v2 | stochastic_14_3_recovery | 9603.18 | -396.82 | sell / filled / 직전 %K14 < 20에서 %K14가 %D3 상향 돌파 (한 봉 목표); 조건 미충족; K14=9.33394, D3=8.42378, previous_K14=10.9938, previous_D3=8.71605; 직전 완료 봉 목표를 다음 봉 시가에 모의 적용 |
| v2 | mfi_14_recovery | 9800.44 | -199.56 | sell / filled / 직전 MFI14 < 20, 현재 MFI14 >= 20 (한 봉 목표); 조건 미충족; MFI14=24.2496, previous_MFI14=22.3876; 직전 완료 봉 목표를 다음 봉 시가에 모의 적용 |
| v2 | adx_14_trend | 9979.97 | -20.03 | sell / filled / Wilder ADX14 >= 25 그리고 +DI14 > -DI14; 조건 미충족; ADX14=24.2312, plus_DI14=28.3519, minus_DI14=24.6578; 직전 완료 봉 목표를 다음 봉 시가에 모의 적용 |
| v2 | aroon_25_trend | 9722.82 | -277.18 | sell / filled / Aroon25 Up > 70 그리고 Down < 30 (동률이면 최신 극값); 조건 미충족; Aroon_up=72, Aroon_down=100; 직전 완료 봉 목표를 다음 봉 시가에 모의 적용 |
| v2 | cci_20_momentum | 9754.52 | -245.48 | sell / filled / CCI20 > 100 (전형가격·평균절대편차); 조건 미충족; CCI20=97.3932; 직전 완료 봉 목표를 다음 봉 시가에 모의 적용 |
| v2 | williams_14_recovery | 9592.94 | -407.06 | sell / filled / 직전 Williams %R14 < -80, 현재 >= -80 (한 봉 목표); 조건 미충족; Williams_R14=-74.6558, previous_R14=-77.3303; 직전 완료 봉 목표를 다음 봉 시가에 모의 적용 |
| v2 | cmf_20_accumulation | 9681.24 | -318.76 | sell / filled / Chaikin Money Flow20 > 0.1; 조건 미충족; CMF20=0.0473512, volume20=7.32623e+07; 직전 완료 봉 목표를 다음 봉 시가에 모의 적용 |
| v2 | chaikin_3_10 | 9550.09 | -449.91 | sell / filled / ADL의 EMA3 - EMA10 > 0 그리고 종가 > EMA26; 조건 미충족; Chaikin3_10=1.08024e+06, ADL=4.99714e+07, close=766.62, EMA26=771.893; 직전 완료 봉 목표를 다음 봉 시가에 모의 적용 |
| v2 | roc_10_momentum | 9951.43 | -48.57 | sell / filled / 10봉 ROC > 1% 그리고 종가 > EMA26; 조건 미충족; ROC10_percent=0.806376, close=769.45, EMA26=767.181; 직전 완료 봉 목표를 다음 봉 시가에 모의 적용 |
| v2 | trix_15_trend | 9472.93 | -527.07 | sell / filled / 15봉 삼중 EMA의 1봉 변화율 TRIX > 0 그리고 종가 > EMA26; 조건 미충족; TRIX15_percent=0.0154379, close=766.62, EMA26=771.893; 직전 완료 봉 목표를 다음 봉 시가에 모의 적용 |
| v2 | keltner_20_breakout | 9803.05 | -196.95 | sell / filled / 종가 > EMA20 + 2 x Wilder ATR14; 조건 미충족; close=774.19, upper_Keltner=774.31, EMA20=772.615, ATR14=0.847257; 직전 완료 봉 목표를 다음 봉 시가에 모의 적용 |
| v2 | opening_range_30m | 9639.43 | -360.57 | sell / filled / 뉴욕 09:30·09:45 두 완료 봉 최고가를 10:00 이후 종가가 돌파; 자료 부족·변동폭 또는 거래량 없음: 대기; close=766.62; 직전 완료 봉 목표를 다음 봉 시가에 모의 적용 |

### 같은 기간의 비용·노출 비교 (사후 연구)

| 전략 | 비용 전 | 비용 후 | 100% 보유 | 같은 평균 노출 보유 | 평균 노출 |
|---|---:|---:|---:|---:|---:|
| cash | 0.00% | 0.00% | -0.53% | -0.00% | 0.00% |
| buy_hold | -0.11% | -0.53% | -0.53% | -0.53% | 100.00% |
| trend_8_26 | 0.30% | -3.42% | -0.53% | -0.29% | 55.91% |
| momentum_26 | -1.12% | -5.58% | -0.53% | -0.29% | 55.64% |
| breakout_8 | -0.24% | -16.38% | -0.53% | -0.13% | 24.41% |
| reversion_12 | -0.90% | -11.15% | -0.53% | -0.13% | 25.72% |
| volume_26 | -1.49% | -10.93% | -0.53% | -0.05% | 9.45% |
| trend_8_26 AND momentum_26 | -0.52% | -5.01% | -0.53% | -0.25% | 48.56% |
| trend_8_26 + momentum_26 | -0.41% | -4.51% | -0.53% | -0.29% | 55.78% |
| trend_8_26 AND breakout_8 | 0.13% | -11.35% | -0.53% | -0.08% | 15.75% |
| trend_8_26 + breakout_8 | 0.03% | -9.75% | -0.53% | -0.21% | 40.16% |
| trend_8_26 AND reversion_12 | 0.21% | -4.72% | -0.53% | -0.03% | 6.56% |
| trend_8_26 + reversion_12 | -0.29% | -7.18% | -0.53% | -0.21% | 40.82% |
| trend_8_26 AND volume_26 | -1.05% | -6.30% | -0.53% | -0.03% | 5.51% |
| trend_8_26 + volume_26 | -0.59% | -7.26% | -0.53% | -0.17% | 32.68% |
| momentum_26 AND breakout_8 | 0.30% | -11.95% | -0.53% | -0.09% | 17.32% |
| momentum_26 + breakout_8 | -0.68% | -11.14% | -0.53% | -0.21% | 40.03% |
| momentum_26 AND reversion_12 | -0.39% | -5.28% | -0.53% | -0.03% | 6.30% |
| momentum_26 + reversion_12 | -1.00% | -7.64% | -0.53% | -0.21% | 40.69% |
| momentum_26 AND volume_26 | -0.79% | -5.27% | -0.53% | -0.02% | 3.94% |
| momentum_26 + volume_26 | -1.30% | -7.53% | -0.53% | -0.17% | 32.55% |
| breakout_8 AND reversion_12 | 0.00% | 0.00% | -0.53% | -0.00% | 0.00% |
| breakout_8 + reversion_12 | -0.57% | -13.45% | -0.53% | -0.13% | 25.07% |
| breakout_8 AND volume_26 | -0.35% | -2.83% | -0.53% | -0.01% | 2.10% |
| breakout_8 + volume_26 | -0.87% | -13.16% | -0.53% | -0.09% | 16.94% |
| reversion_12 AND volume_26 | -0.97% | -5.05% | -0.53% | -0.02% | 3.67% |
| reversion_12 + volume_26 | -1.19% | -10.67% | -0.53% | -0.09% | 17.59% |
| ema_12_26 | -0.52% | -3.81% | -0.53% | -0.31% | 59.58% |
| macd_12_26_9 | 0.21% | -4.71% | -0.53% | -0.19% | 35.70% |
| rsi_14_recovery | -0.42% | -3.71% | -0.53% | -0.01% | 2.10% |
| bollinger_20_reentry | -0.96% | -6.22% | -0.53% | -0.02% | 3.41% |
| donchian_20 | 0.06% | -8.39% | -0.53% | -0.04% | 7.61% |
| atr_14_breakout | 0.29% | -5.44% | -0.53% | -0.02% | 3.94% |
| session_vwap | 0.19% | -10.55% | -0.53% | -0.25% | 47.77% |
| obv_20 | -1.15% | -9.87% | -0.53% | -0.22% | 41.99% |
| stochastic_14_3_recovery | 0.34% | -12.64% | -0.53% | -0.05% | 8.66% |
| mfi_14_recovery | 0.11% | -2.79% | -0.53% | -0.01% | 1.84% |
| adx_14_trend | 0.73% | -1.77% | -0.53% | -0.13% | 24.15% |
| aroon_25_trend | -0.07% | -2.97% | -0.53% | -0.14% | 26.77% |
| cci_20_momentum | 0.06% | -8.39% | -0.53% | -0.13% | 23.88% |
| williams_14_recovery | 0.23% | -9.76% | -0.53% | -0.03% | 6.56% |
| cmf_20_accumulation | 0.68% | -3.86% | -0.53% | -0.26% | 49.87% |
| chaikin_3_10 | 0.72% | -6.62% | -0.53% | -0.24% | 46.19% |
| roc_10_momentum | -0.13% | -0.97% | -0.53% | -0.01% | 1.05% |
| trix_15_trend | -1.14% | -6.39% | -0.53% | -0.24% | 45.67% |
| keltner_20_breakout | -0.22% | -4.73% | -0.53% | -0.06% | 12.34% |
| opening_range_30m | -0.27% | -6.36% | -0.53% | -0.22% | 41.21% |

동일 구간·초기 자금, 종료 시 청산 비용 포함. 노출 맞춤은 사후 설명용이며 v2 실제 계좌 성과가 아닙니다.
[낙폭 분해·비용 영향·전체 구간](SPY/comparison.json)

[v1 전체 기록](SPY/accounts.json) · [v2 전체 기록](SPY/accounts-v2.json)

## QQQ 계좌

| 모델 | 전략 | 평가액 USD | 손익 USD | 최근 매매·이유 |
|---|---|---:|---:|---|
| v1 | cash | 10000.00 | 0.00 | 대기 /  / 새 신호 대기 |
| v1 | buy_hold | 9724.42 | -275.58 | buy /  / buy_hold: prior completed bar target 100%; next bar open simulation |
| v1 | trend_8_26 | 9679.99 | -320.01 | sell /  / trend_8_26: prior completed bar target 0%; next bar open simulation |
| v1 | momentum_26 | 9370.26 | -629.74 | sell /  / momentum_26: prior completed bar target 0%; next bar open simulation |
| v1 | breakout_8 | 9613.51 | -386.49 | sell /  / breakout_8: prior completed bar target 0%; next bar open simulation |
| v1 | reversion_12 | 9618.66 | -381.34 | buy /  / reversion_12: prior completed bar target 100%; next bar open simulation |
| v1 | volume_26 | 9583.68 | -416.32 | sell /  / volume_26: prior completed bar target 0%; next bar open simulation |
| v1 | trend_8_26 AND momentum_26 | 9732.14 | -267.86 | sell /  / trend_8_26 AND momentum_26: prior completed bar target 0%; next bar open simulation |
| v1 | trend_8_26 + momentum_26 | 9562.10 | -437.90 | sell /  / trend_8_26 + momentum_26: prior completed bar target 0%; next bar open simulation |
| v1 | trend_8_26 AND breakout_8 | 9949.62 | -50.38 | sell /  / trend_8_26 AND breakout_8: prior completed bar target 0%; next bar open simulation |
| v1 | trend_8_26 + breakout_8 | 9685.58 | -314.42 | sell /  / trend_8_26 + breakout_8: prior completed bar target 0%; next bar open simulation |
| v1 | trend_8_26 AND reversion_12 | 9885.50 | -114.50 | sell /  / trend_8_26 AND reversion_12: prior completed bar target 0%; next bar open simulation |
| v1 | trend_8_26 + reversion_12 | 9688.23 | -311.77 | buy /  / trend_8_26 + reversion_12: prior completed bar target 50%; next bar open simulation |
| v1 | trend_8_26 AND volume_26 | 9846.67 | -153.33 | sell /  / trend_8_26 AND volume_26: prior completed bar target 0%; next bar open simulation |
| v1 | trend_8_26 + volume_26 | 9631.84 | -368.16 | sell /  / trend_8_26 + volume_26: prior completed bar target 0%; next bar open simulation |
| v1 | momentum_26 AND breakout_8 | 9644.64 | -355.36 | sell /  / momentum_26 AND breakout_8: prior completed bar target 0%; next bar open simulation |
| v1 | momentum_26 + breakout_8 | 9491.44 | -508.56 | sell /  / momentum_26 + breakout_8: prior completed bar target 0%; next bar open simulation |
| v1 | momentum_26 AND reversion_12 | 9783.95 | -216.05 | sell /  / momentum_26 AND reversion_12: prior completed bar target 0%; next bar open simulation |
| v1 | momentum_26 + reversion_12 | 9551.14 | -448.86 | buy /  / momentum_26 + reversion_12: prior completed bar target 50%; next bar open simulation |
| v1 | momentum_26 AND volume_26 | 9819.14 | -180.86 | sell /  / momentum_26 AND volume_26: prior completed bar target 0%; next bar open simulation |
| v1 | momentum_26 + volume_26 | 9495.49 | -504.51 | sell /  / momentum_26 + volume_26: prior completed bar target 0%; next bar open simulation |
| v1 | breakout_8 AND reversion_12 | 10000.00 | 0.00 | 대기 /  / 새 신호 대기 |
| v1 | breakout_8 + reversion_12 | 9654.60 | -345.40 | buy /  / breakout_8 + reversion_12: prior completed bar target 50%; next bar open simulation |
| v1 | breakout_8 AND volume_26 | 9929.33 | -70.67 | sell /  / breakout_8 AND volume_26: prior completed bar target 0%; next bar open simulation |
| v1 | breakout_8 + volume_26 | 9617.74 | -382.26 | sell /  / breakout_8 + volume_26: prior completed bar target 0%; next bar open simulation |
| v1 | reversion_12 AND volume_26 | 9860.10 | -139.90 | sell /  / reversion_12 AND volume_26: prior completed bar target 0%; next bar open simulation |
| v1 | reversion_12 + volume_26 | 9639.55 | -360.45 | buy /  / reversion_12 + volume_26: prior completed bar target 50%; next bar open simulation |
| v1 | ema_12_26 | 9439.49 | -560.51 | sell /  / EMA12 > EMA26; 조건 미충족; EMA12=723.809, EMA26=723.847 |
| v1 | macd_12_26_9 | 9765.43 | -234.57 | sell /  / MACD > 신호선 그리고 MACD > 0; 조건 미충족; MACD=1.7811, signal9=1.82319 |
| v1 | rsi_14_recovery | 9764.60 | -235.40 | sell /  / 직전 RSI14 < 30, 현재 RSI14 >= 30 (한 봉 목표); 조건 미충족; RSI14=30.4228, previous_RSI14=31.111 |
| v1 | bollinger_20_reentry | 9823.48 | -176.52 | sell /  / 직전 종가 < 직전 하단밴드, 현재 하단밴드 <= 종가 <= SMA20 (한 봉 목표); 조건 미충족; close=706.995, lower20=705.434, SMA20=720.761, previous_lower20=707.596 |
| v1 | donchian_20 | 9889.14 | -110.86 | sell /  / 종가 > 현재 봉을 제외한 직전 20봉 최고가; 조건 미충족; close=726.885, prior_high20=727.77 |
| v1 | atr_14_breakout | 9887.37 | -112.63 | sell /  / 종가 > 직전 종가 + 직전 ATR14 그리고 종가 > EMA26; 조건 미충족; close=725.79, threshold=727.527, prior_ATR14=1.49237, EMA26=724.609 |
| v1 | session_vwap | 9387.48 | -612.52 | sell /  / 종가 > 뉴욕 거래일별 누적 전형가격 VWAP; 조건 미충족; close=706.51, session_VWAP=708.65, session_volume=2.91223e+08 |
| v1 | obv_20 | 9508.81 | -491.19 | sell /  / OBV > OBV의 SMA20 그리고 종가 > EMA26; 조건 미충족; OBV=4.39726e+08, OBV_SMA20=4.50483e+08, close=713.775, EMA26=723.847 |
| v1 | stochastic_14_3_recovery | 9502.41 | -497.59 | sell /  / 직전 %K14 < 20에서 %K14가 %D3 상향 돌파 (한 봉 목표); 조건 미충족; K14=5.63186, D3=4.89371, previous_K14=7.28772, previous_D3=5.3193 |
| v1 | mfi_14_recovery | 9813.56 | -186.44 | sell /  / 직전 MFI14 < 20, 현재 MFI14 >= 20 (한 봉 목표); 조건 미충족; MFI14=30.3876, previous_MFI14=31.1747 |
| v1 | adx_14_trend | 9825.33 | -174.67 | sell /  / Wilder ADX14 >= 25 그리고 +DI14 > -DI14; 조건 미충족; ADX14=23.847, plus_DI14=27.825, minus_DI14=26.997 |
| v1 | aroon_25_trend | 9774.48 | -225.52 | sell /  / Aroon25 Up > 70 그리고 Down < 30 (동률이면 최신 극값); 조건 미충족; Aroon_up=68, Aroon_down=4 |
| v1 | cci_20_momentum | 9862.10 | -137.90 | sell /  / CCI20 > 100 (전형가격·평균절대편차); 조건 미충족; CCI20=80.102 |
| v1 | williams_14_recovery | 9677.65 | -322.35 | sell /  / 직전 Williams %R14 < -80, 현재 >= -80 (한 봉 목표); 조건 미충족; Williams_R14=-35.3329, previous_R14=-72.5093 |
| v1 | cmf_20_accumulation | 9379.66 | -620.34 | sell /  / Chaikin Money Flow20 > 0.1; 조건 미충족; CMF20=0.025426, volume20=1.62711e+08 |
| v1 | chaikin_3_10 | 9515.49 | -484.51 | sell /  / ADL의 EMA3 - EMA10 > 0 그리고 종가 > EMA26; 조건 미충족; Chaikin3_10=7.32608e+06, ADL=3.89342e+08, close=713.775, EMA26=723.847 |
| v1 | roc_10_momentum | 9961.33 | -38.67 | sell /  / 10봉 ROC > 1% 그리고 종가 > EMA26; 조건 미충족; ROC10_percent=0.681109, close=725.78, EMA26=721.667 |
| v1 | trix_15_trend | 9467.11 | -532.89 | sell /  / 15봉 삼중 EMA의 1봉 변화율 TRIX > 0 그리고 종가 > EMA26; 조건 미충족; TRIX15_percent=0.0245938, close=713.775, EMA26=723.847 |
| v1 | keltner_20_breakout | 9782.40 | -217.60 | sell /  / 종가 > EMA20 + 2 x Wilder ATR14; 조건 미충족; close=726.815, upper_Keltner=727.39, EMA20=724.295, ATR14=1.54727 |
| v1 | opening_range_30m | 9599.28 | -400.72 | sell /  / 뉴욕 09:30·09:45 두 완료 봉 최고가를 10:00 이후 종가가 돌파; 자료 부족·변동폭 또는 거래량 없음: 대기; close=713.775 |
| v2 | cash | 10000.00 | 0.00 | 대기 /  / 새 신호 대기 |
| v2 | buy_hold | 9410.09 | -589.91 | buy / partial / 직전 완료 봉 목표 비중 100%; 다음 봉 시가 가정 |
| v2 | trend_8_26 | 9482.37 | -517.63 | sell / filled / 직전 완료 봉 목표 비중 0%; 다음 봉 시가 가정 |
| v2 | momentum_26 | 9261.49 | -738.51 | sell / filled / 직전 완료 봉 목표 비중 0%; 다음 봉 시가 가정 |
| v2 | breakout_8 | 9279.42 | -720.58 | sell / filled / 직전 완료 봉 목표 비중 0%; 다음 봉 시가 가정 |
| v2 | reversion_12 | 9131.93 | -868.07 | buy / partial / 직전 완료 봉 목표 비중 100%; 다음 봉 시가 가정 |
| v2 | volume_26 | 9565.80 | -434.20 | 중단: 손실 한도 / sell / filled / 직전 완료 봉 목표 비중 0%; 다음 봉 시가 가정 |
| v2 | trend_8_26 AND momentum_26 | 9626.87 | -373.13 | sell / filled / 직전 완료 봉 목표 비중 0%; 다음 봉 시가 가정 |
| v2 | trend_8_26 + momentum_26 | 9410.82 | -589.18 | sell / filled / 직전 완료 봉 목표 비중 0%; 다음 봉 시가 가정 |
| v2 | trend_8_26 AND breakout_8 | 9840.07 | -159.93 | sell / filled / 직전 완료 봉 목표 비중 0%; 다음 봉 시가 가정 |
| v2 | trend_8_26 + breakout_8 | 9419.99 | -580.01 | sell / filled / 직전 완료 봉 목표 비중 0%; 다음 봉 시가 가정 |
| v2 | trend_8_26 AND reversion_12 | 9742.38 | -257.62 | sell / filled / 직전 완료 봉 목표 비중 0%; 다음 봉 시가 가정 |
| v2 | trend_8_26 + reversion_12 | 9344.61 | -655.39 | buy / filled / 직전 완료 봉 목표 비중 50%; 다음 봉 시가 가정 |
| v2 | trend_8_26 AND volume_26 | 9679.53 | -320.47 | sell / filled / 직전 완료 봉 목표 비중 0%; 다음 봉 시가 가정 |
| v2 | trend_8_26 + volume_26 | 9236.62 | -763.38 | sell / filled / 직전 완료 봉 목표 비중 0%; 다음 봉 시가 가정 |
| v2 | momentum_26 AND breakout_8 | 9591.37 | -408.63 | sell / filled / 직전 완료 봉 목표 비중 0%; 다음 봉 시가 가정 |
| v2 | momentum_26 + breakout_8 | 9270.73 | -729.27 | sell / filled / 직전 완료 봉 목표 비중 0%; 다음 봉 시가 가정 |
| v2 | momentum_26 AND reversion_12 | 9776.12 | -223.88 | sell / filled / 직전 완료 봉 목표 비중 0%; 다음 봉 시가 가정 |
| v2 | momentum_26 + reversion_12 | 9274.05 | -725.95 | buy / filled / 직전 완료 봉 목표 비중 50%; 다음 봉 시가 가정 |
| v2 | momentum_26 AND volume_26 | 9749.31 | -250.69 | sell / filled / 직전 완료 봉 목표 비중 0%; 다음 봉 시가 가정 |
| v2 | momentum_26 + volume_26 | 9147.59 | -852.41 | sell / filled / 직전 완료 봉 목표 비중 0%; 다음 봉 시가 가정 |
| v2 | breakout_8 AND reversion_12 | 10000.00 | 0.00 | 대기 /  / 새 신호 대기 |
| v2 | breakout_8 + reversion_12 | 9302.18 | -697.82 | buy / filled / 직전 완료 봉 목표 비중 50%; 다음 봉 시가 가정 |
| v2 | breakout_8 AND volume_26 | 9871.76 | -128.24 | sell / filled / 직전 완료 봉 목표 비중 0%; 다음 봉 시가 가정 |
| v2 | breakout_8 + volume_26 | 9194.86 | -805.14 | sell / filled / 직전 완료 봉 목표 비중 0%; 다음 봉 시가 가정 |
| v2 | reversion_12 AND volume_26 | 9547.64 | -452.36 | 중단: 손실 한도 / sell / filled / 직전 완료 봉 목표 비중 0%; 다음 봉 시가 가정 |
| v2 | reversion_12 + volume_26 | 9121.54 | -878.46 | buy / filled / 직전 완료 봉 목표 비중 50%; 다음 봉 시가 가정 |
| v2 | ema_12_26 | 9430.06 | -569.94 | sell / filled / EMA12 > EMA26; 조건 미충족; EMA12=723.809, EMA26=723.847; 직전 완료 봉 목표를 다음 봉 시가에 모의 적용 |
| v2 | macd_12_26_9 | 9755.67 | -244.33 | sell / filled / MACD > 신호선 그리고 MACD > 0; 조건 미충족; MACD=1.7811, signal9=1.82319; 직전 완료 봉 목표를 다음 봉 시가에 모의 적용 |
| v2 | rsi_14_recovery | 9754.84 | -245.16 | sell / filled / 직전 RSI14 < 30, 현재 RSI14 >= 30 (한 봉 목표); 조건 미충족; RSI14=30.4228, previous_RSI14=31.111; 직전 완료 봉 목표를 다음 봉 시가에 모의 적용 |
| v2 | bollinger_20_reentry | 9815.62 | -184.38 | sell / filled / 직전 종가 < 직전 하단밴드, 현재 하단밴드 <= 종가 <= SMA20 (한 봉 목표); 조건 미충족; close=706.995, lower20=705.434, SMA20=720.761, previous_lower20=707.596; 직전 완료 봉 목표를 다음 봉 시가에 모의 적용 |
| v2 | donchian_20 | 9881.23 | -118.77 | sell / filled / 종가 > 현재 봉을 제외한 직전 20봉 최고가; 조건 미충족; close=726.885, prior_high20=727.77; 직전 완료 봉 목표를 다음 봉 시가에 모의 적용 |
| v2 | atr_14_breakout | 9879.47 | -120.53 | sell / filled / 종가 > 직전 종가 + 직전 ATR14 그리고 종가 > EMA26; 조건 미충족; close=725.79, threshold=727.527, prior_ATR14=1.49237, EMA26=724.609; 직전 완료 봉 목표를 다음 봉 시가에 모의 적용 |
| v2 | session_vwap | 9368.73 | -631.27 | sell / filled / 종가 > 뉴욕 거래일별 누적 전형가격 VWAP; 조건 미충족; close=706.51, session_VWAP=708.65, session_volume=2.91223e+08; 직전 완료 봉 목표를 다음 봉 시가에 모의 적용 |
| v2 | obv_20 | 9495.51 | -504.49 | sell / filled / OBV > OBV의 SMA20 그리고 종가 > EMA26; 조건 미충족; OBV=4.39726e+08, OBV_SMA20=4.50483e+08, close=713.775, EMA26=723.847; 직전 완료 봉 목표를 다음 봉 시가에 모의 적용 |
| v2 | stochastic_14_3_recovery | 9694.13 | -305.87 | 중단: 손실 한도 / sell / filled / 직전 %K14 < 20에서 %K14가 %D3 상향 돌파 (한 봉 목표); 조건 미충족; K14=10.576, D3=8.00581, previous_K14=7.39787, previous_D3=7.27486; 직전 완료 봉 목표를 다음 봉 시가에 모의 적용 |
| v2 | mfi_14_recovery | 9809.63 | -190.37 | sell / filled / 직전 MFI14 < 20, 현재 MFI14 >= 20 (한 봉 목표); 조건 미충족; MFI14=30.3876, previous_MFI14=31.1747; 직전 완료 봉 목표를 다음 봉 시가에 모의 적용 |
| v2 | adx_14_trend | 9817.47 | -182.53 | sell / filled / Wilder ADX14 >= 25 그리고 +DI14 > -DI14; 조건 미충족; ADX14=23.847, plus_DI14=27.825, minus_DI14=26.997; 직전 완료 봉 목표를 다음 봉 시가에 모의 적용 |
| v2 | aroon_25_trend | 9766.66 | -233.34 | sell / filled / Aroon25 Up > 70 그리고 Down < 30 (동률이면 최신 극값); 조건 미충족; Aroon_up=68, Aroon_down=4; 직전 완료 봉 목표를 다음 봉 시가에 모의 적용 |
| v2 | cci_20_momentum | 9852.25 | -147.75 | sell / filled / CCI20 > 100 (전형가격·평균절대편차); 조건 미충족; CCI20=80.102; 직전 완료 봉 목표를 다음 봉 시가에 모의 적용 |
| v2 | williams_14_recovery | 9658.32 | -341.68 | sell / filled / 직전 Williams %R14 < -80, 현재 >= -80 (한 봉 목표); 조건 미충족; Williams_R14=-35.3329, previous_R14=-72.5093; 직전 완료 봉 목표를 다음 봉 시가에 모의 적용 |
| v2 | cmf_20_accumulation | 9364.67 | -635.33 | sell / filled / Chaikin Money Flow20 > 0.1; 조건 미충족; CMF20=0.025426, volume20=1.62711e+08; 직전 완료 봉 목표를 다음 봉 시가에 모의 적용 |
| v2 | chaikin_3_10 | 9502.18 | -497.82 | sell / filled / ADL의 EMA3 - EMA10 > 0 그리고 종가 > EMA26; 조건 미충족; Chaikin3_10=7.32608e+06, ADL=3.89342e+08, close=713.775, EMA26=723.847; 직전 완료 봉 목표를 다음 봉 시가에 모의 적용 |
| v2 | roc_10_momentum | 9957.34 | -42.66 | sell / filled / 10봉 ROC > 1% 그리고 종가 > EMA26; 조건 미충족; ROC10_percent=0.681109, close=725.78, EMA26=721.667; 직전 완료 봉 목표를 다음 봉 시가에 모의 적용 |
| v2 | trix_15_trend | 9453.87 | -546.13 | sell / filled / 15봉 삼중 EMA의 1봉 변화율 TRIX > 0 그리고 종가 > EMA26; 조건 미충족; TRIX15_percent=0.0245938, close=713.775, EMA26=723.847; 직전 완료 봉 목표를 다음 봉 시가에 모의 적용 |
| v2 | keltner_20_breakout | 9772.62 | -227.38 | sell / filled / 종가 > EMA20 + 2 x Wilder ATR14; 조건 미충족; close=726.815, upper_Keltner=727.39, EMA20=724.295, ATR14=1.54727; 직전 완료 봉 목표를 다음 봉 시가에 모의 적용 |
| v2 | opening_range_30m | 9589.69 | -410.31 | sell / filled / 뉴욕 09:30·09:45 두 완료 봉 최고가를 10:00 이후 종가가 돌파; 자료 부족·변동폭 또는 거래량 없음: 대기; close=713.775; 직전 완료 봉 목표를 다음 봉 시가에 모의 적용 |

### 같은 기간의 비용·노출 비교 (사후 연구)

| 전략 | 비용 전 | 비용 후 | 100% 보유 | 같은 평균 노출 보유 | 평균 노출 |
|---|---:|---:|---:|---:|---:|
| cash | 0.00% | 0.00% | -5.22% | -0.00% | 0.00% |
| buy_hold | -4.82% | -5.22% | -5.22% | -5.22% | 100.00% |
| trend_8_26 | -1.39% | -5.05% | -5.22% | -2.27% | 43.31% |
| momentum_26 | -4.20% | -9.29% | -5.22% | -2.07% | 39.37% |
| breakout_8 | -1.70% | -16.55% | -5.22% | -0.99% | 18.90% |
| reversion_12 | -0.34% | -12.50% | -5.22% | -1.61% | 30.71% |
| volume_26 | -1.07% | -14.59% | -5.22% | -0.90% | 17.06% |
| trend_8_26 AND momentum_26 | -1.38% | -4.64% | -5.22% | -1.72% | 32.81% |
| trend_8_26 + momentum_26 | -2.80% | -6.60% | -5.22% | -2.17% | 41.34% |
| trend_8_26 AND breakout_8 | 0.42% | -7.67% | -5.22% | -0.62% | 11.81% |
| trend_8_26 + breakout_8 | -1.54% | -10.42% | -5.22% | -1.63% | 31.11% |
| trend_8_26 AND reversion_12 | -0.22% | -4.33% | -5.22% | -0.35% | 6.56% |
| trend_8_26 + reversion_12 | -0.85% | -8.28% | -5.22% | -1.94% | 37.01% |
| trend_8_26 AND volume_26 | 0.23% | -4.70% | -5.22% | -0.28% | 5.25% |
| trend_8_26 + volume_26 | -1.22% | -9.95% | -5.22% | -1.59% | 30.19% |
| momentum_26 AND breakout_8 | -0.36% | -9.16% | -5.22% | -0.63% | 12.07% |
| momentum_26 + breakout_8 | -2.95% | -12.81% | -5.22% | -1.53% | 29.14% |
| momentum_26 AND reversion_12 | -1.04% | -5.51% | -5.22% | -0.35% | 6.56% |
| momentum_26 + reversion_12 | -2.27% | -9.97% | -5.22% | -1.84% | 35.04% |
| momentum_26 AND volume_26 | -0.38% | -4.08% | -5.22% | -0.19% | 3.67% |
| momentum_26 + volume_26 | -2.64% | -11.61% | -5.22% | -1.48% | 28.22% |
| breakout_8 AND reversion_12 | 0.00% | 0.00% | -5.22% | -0.00% | 0.00% |
| breakout_8 + reversion_12 | -1.01% | -13.48% | -5.22% | -1.30% | 24.81% |
| breakout_8 AND volume_26 | 0.32% | -2.18% | -5.22% | -0.12% | 2.36% |
| breakout_8 + volume_26 | -1.38% | -14.15% | -5.22% | -0.95% | 17.99% |
| reversion_12 AND volume_26 | -1.22% | -8.03% | -5.22% | -0.44% | 8.40% |
| reversion_12 + volume_26 | -0.69% | -13.01% | -5.22% | -1.26% | 23.89% |
| ema_12_26 | -2.73% | -5.55% | -5.22% | -2.12% | 40.42% |
| macd_12_26_9 | 0.60% | -3.95% | -5.22% | -1.27% | 24.15% |
| rsi_14_recovery | -0.53% | -6.21% | -5.22% | -0.19% | 3.67% |
| bollinger_20_reentry | -0.05% | -5.76% | -5.22% | -0.19% | 3.67% |
| donchian_20 | 0.58% | -5.17% | -5.22% | -0.35% | 6.56% |
| atr_14_breakout | 0.32% | -3.81% | -5.22% | -0.15% | 2.89% |
| session_vwap | -2.21% | -13.79% | -5.22% | -2.45% | 46.72% |
| obv_20 | -2.88% | -11.45% | -5.22% | -1.49% | 28.35% |
| stochastic_14_3_recovery | 0.06% | -11.78% | -5.22% | -0.41% | 7.87% |
| mfi_14_recovery | -1.19% | -3.24% | -5.22% | -0.07% | 1.31% |
| adx_14_trend | -0.10% | -3.00% | -5.22% | -1.05% | 19.95% |
| aroon_25_trend | 1.00% | -2.75% | -5.22% | -0.92% | 17.59% |
| cci_20_momentum | 0.26% | -4.67% | -5.22% | -0.95% | 18.11% |
| williams_14_recovery | 0.23% | -10.14% | -5.22% | -0.36% | 6.82% |
| cmf_20_accumulation | -3.30% | -9.96% | -5.22% | -1.96% | 37.27% |
| chaikin_3_10 | -4.09% | -12.18% | -5.22% | -1.72% | 32.81% |
| roc_10_momentum | 0.13% | -1.54% | -5.22% | -0.25% | 4.72% |
| trix_15_trend | -1.62% | -5.27% | -5.22% | -1.80% | 34.38% |
| keltner_20_breakout | -0.82% | -5.70% | -5.22% | -0.46% | 8.66% |
| opening_range_30m | -1.73% | -6.95% | -5.22% | -1.80% | 34.38% |

동일 구간·초기 자금, 종료 시 청산 비용 포함. 노출 맞춤은 사후 설명용이며 v2 실제 계좌 성과가 아닙니다.
[낙폭 분해·비용 영향·전체 구간](QQQ/comparison.json)

[v1 전체 기록](QQQ/accounts.json) · [v2 전체 기록](QQQ/accounts-v2.json)

## IWM 계좌

| 모델 | 전략 | 평가액 USD | 손익 USD | 최근 매매·이유 |
|---|---|---:|---:|---|
| v1 | cash | 10000.00 | 0.00 | 대기 /  / 새 신호 대기 |
| v1 | buy_hold | 10007.10 | 7.10 | buy /  / buy_hold: prior completed bar target 100%; next bar open simulation |
| v1 | trend_8_26 | 9801.27 | -198.73 | sell /  / trend_8_26: prior completed bar target 0%; next bar open simulation |
| v1 | momentum_26 | 9795.94 | -204.06 | sell /  / momentum_26: prior completed bar target 0%; next bar open simulation |
| v1 | breakout_8 | 9349.32 | -650.68 | sell /  / breakout_8: prior completed bar target 0%; next bar open simulation |
| v1 | reversion_12 | 9736.37 | -263.63 | sell /  / reversion_12: prior completed bar target 0%; next bar open simulation |
| v1 | volume_26 | 9885.16 | -114.84 | sell /  / volume_26: prior completed bar target 0%; next bar open simulation |
| v1 | trend_8_26 AND momentum_26 | 9746.90 | -253.10 | sell /  / trend_8_26 AND momentum_26: prior completed bar target 0%; next bar open simulation |
| v1 | trend_8_26 + momentum_26 | 9798.73 | -201.27 | sell /  / trend_8_26 + momentum_26: prior completed bar target 0%; next bar open simulation |
| v1 | trend_8_26 AND breakout_8 | 9504.10 | -495.90 | sell /  / trend_8_26 AND breakout_8: prior completed bar target 0%; next bar open simulation |
| v1 | trend_8_26 + breakout_8 | 9572.84 | -427.16 | sell /  / trend_8_26 + breakout_8: prior completed bar target 0%; next bar open simulation |
| v1 | trend_8_26 AND reversion_12 | 9811.31 | -188.69 | sell /  / trend_8_26 AND reversion_12: prior completed bar target 0%; next bar open simulation |
| v1 | trend_8_26 + reversion_12 | 9768.56 | -231.44 | sell /  / trend_8_26 + reversion_12: prior completed bar target 0%; next bar open simulation |
| v1 | trend_8_26 AND volume_26 | 9927.90 | -72.10 | sell /  / trend_8_26 AND volume_26: prior completed bar target 0%; next bar open simulation |
| v1 | trend_8_26 + volume_26 | 9862.68 | -137.32 | sell /  / trend_8_26 + volume_26: prior completed bar target 0%; next bar open simulation |
| v1 | momentum_26 AND breakout_8 | 9552.12 | -447.88 | sell /  / momentum_26 AND breakout_8: prior completed bar target 0%; next bar open simulation |
| v1 | momentum_26 + breakout_8 | 9589.36 | -410.64 | sell /  / momentum_26 + breakout_8: prior completed bar target 0%; next bar open simulation |
| v1 | momentum_26 AND reversion_12 | 9876.67 | -123.33 | sell /  / momentum_26 AND reversion_12: prior completed bar target 0%; next bar open simulation |
| v1 | momentum_26 + reversion_12 | 9844.41 | -155.59 | sell /  / momentum_26 + reversion_12: prior completed bar target 0%; next bar open simulation |
| v1 | momentum_26 AND volume_26 | 9977.14 | -22.86 | sell /  / momentum_26 AND volume_26: prior completed bar target 0%; next bar open simulation |
| v1 | momentum_26 + volume_26 | 9879.83 | -120.17 | sell /  / momentum_26 + volume_26: prior completed bar target 0%; next bar open simulation |
| v1 | breakout_8 AND reversion_12 | 10000.00 | 0.00 | 대기 /  / 새 신호 대기 |
| v1 | breakout_8 + reversion_12 | 9559.78 | -440.22 | sell /  / breakout_8 + reversion_12: prior completed bar target 0%; next bar open simulation |
| v1 | breakout_8 AND volume_26 | 9967.28 | -32.72 | sell /  / breakout_8 AND volume_26: prior completed bar target 0%; next bar open simulation |
| v1 | breakout_8 + volume_26 | 9632.70 | -367.30 | sell /  / breakout_8 + volume_26: prior completed bar target 0%; next bar open simulation |
| v1 | reversion_12 AND volume_26 | 9937.60 | -62.40 | sell /  / reversion_12 AND volume_26: prior completed bar target 0%; next bar open simulation |
| v1 | reversion_12 + volume_26 | 9849.76 | -150.24 | sell /  / reversion_12 + volume_26: prior completed bar target 0%; next bar open simulation |
| v1 | ema_12_26 | 9815.21 | -184.79 | sell /  / EMA12 > EMA26; 조건 미충족; EMA12=276.256, EMA26=276.345 |
| v1 | macd_12_26_9 | 9906.42 | -93.58 | sell /  / MACD > 신호선 그리고 MACD > 0; 조건 미충족; MACD=0.978353, signal9=1.01104 |
| v1 | rsi_14_recovery | 9786.95 | -213.05 | sell /  / 직전 RSI14 < 30, 현재 RSI14 >= 30 (한 봉 목표); 조건 미충족; RSI14=46.986, previous_RSI14=37.1649 |
| v1 | bollinger_20_reentry | 9848.19 | -151.81 | sell /  / 직전 종가 < 직전 하단밴드, 현재 하단밴드 <= 종가 <= SMA20 (한 봉 목표); 조건 미충족; close=275.52, lower20=275.107, SMA20=276.469, previous_lower20=275.234 |
| v1 | donchian_20 | 9835.91 | -164.09 | sell /  / 종가 > 현재 봉을 제외한 직전 20봉 최고가; 조건 미충족; close=275.785, prior_high20=276.875 |
| v1 | atr_14_breakout | 9732.89 | -267.11 | sell /  / 종가 > 직전 종가 + 직전 ATR14 그리고 종가 > EMA26; 조건 미충족; close=276.06, threshold=277.643, prior_ATR14=0.662564, EMA26=276.447 |
| v1 | session_vwap | 9537.59 | -462.41 | sell /  / 종가 > 뉴욕 거래일별 누적 전형가격 VWAP; 조건 미충족; close=275.532, session_VWAP=275.837, session_volume=1.37078e+07 |
| v1 | obv_20 | 9772.61 | -227.39 | sell /  / OBV > OBV의 SMA20 그리고 종가 > EMA26; 조건 미충족; OBV=-1.90163e+07, OBV_SMA20=-1.97011e+07, close=275.532, EMA26=276.085 |
| v1 | stochastic_14_3_recovery | 9629.03 | -370.97 | sell /  / 직전 %K14 < 20에서 %K14가 %D3 상향 돌파 (한 봉 목표); 조건 미충족; K14=39.2924, D3=31.5748, previous_K14=36.5078, previous_D3=30.3985 |
| v1 | mfi_14_recovery | 9934.22 | -65.78 | sell /  / 직전 MFI14 < 20, 현재 MFI14 >= 20 (한 봉 목표); 조건 미충족; MFI14=34.131, previous_MFI14=22.0435 |
| v1 | adx_14_trend | 9726.05 | -273.95 | sell /  / Wilder ADX14 >= 25 그리고 +DI14 > -DI14; 조건 미충족; ADX14=27.8461, plus_DI14=25.882, minus_DI14=28.4558 |
| v1 | aroon_25_trend | 9745.85 | -254.15 | sell /  / Aroon25 Up > 70 그리고 Down < 30 (동률이면 최신 극값); 조건 미충족; Aroon_up=68, Aroon_down=4 |
| v1 | cci_20_momentum | 9825.51 | -174.49 | sell /  / CCI20 > 100 (전형가격·평균절대편차); 조건 미충족; CCI20=-152.101 |
| v1 | williams_14_recovery | 9757.64 | -242.36 | sell /  / 직전 Williams %R14 < -80, 현재 >= -80 (한 봉 목표); 조건 미충족; Williams_R14=-60.7076, previous_R14=-63.4922 |
| v1 | cmf_20_accumulation | 9709.11 | -290.89 | sell /  / Chaikin Money Flow20 > 0.1; 조건 미충족; CMF20=0.0178538, volume20=1.46976e+07 |
| v1 | chaikin_3_10 | 9618.93 | -381.07 | sell /  / ADL의 EMA3 - EMA10 > 0 그리고 종가 > EMA26; 조건 미충족; Chaikin3_10=188377, ADL=-3.27277e+07, close=275.532, EMA26=276.085 |
| v1 | roc_10_momentum | 9996.39 | -3.61 | sell /  / 10봉 ROC > 1% 그리고 종가 > EMA26; 조건 미충족; ROC10_percent=0.995963, close=275.315, EMA26=273.754 |
| v1 | trix_15_trend | 9811.92 | -188.08 | sell /  / 15봉 삼중 EMA의 1봉 변화율 TRIX > 0 그리고 종가 > EMA26; 조건 미충족; TRIX15_percent=0.00744142, close=276.06, EMA26=276.447 |
| v1 | keltner_20_breakout | 9879.23 | -120.77 | sell /  / 종가 > EMA20 + 2 x Wilder ATR14; 조건 미충족; close=276.4, upper_Keltner=277.094, EMA20=275.768, ATR14=0.662947 |
| v1 | opening_range_30m | 9963.15 | -36.85 | sell /  / 뉴욕 09:30·09:45 두 완료 봉 최고가를 10:00 이후 종가가 돌파; 자료 부족·변동폭 또는 거래량 없음: 대기; close=276.82 |
| v2 | cash | 10000.00 | 0.00 | 대기 /  / 새 신호 대기 |
| v2 | buy_hold | 9900.10 | -99.90 | buy / partial / 직전 완료 봉 목표 비중 100%; 다음 봉 시가 가정 |
| v2 | trend_8_26 | 9669.43 | -330.57 | sell / filled / 직전 완료 봉 목표 비중 0%; 다음 봉 시가 가정 |
| v2 | momentum_26 | 9661.30 | -338.70 | sell / filled / 직전 완료 봉 목표 비중 0%; 다음 봉 시가 가정 |
| v2 | breakout_8 | 9009.35 | -990.65 | 중단: 손실 한도 / buy / partial / 직전 완료 봉 목표 비중 100%; 다음 봉 시가 가정 |
| v2 | reversion_12 | 9270.49 | -729.51 | sell / filled / 직전 완료 봉 목표 비중 0%; 다음 봉 시가 가정 |
| v2 | volume_26 | 9394.71 | -605.29 | sell / filled / 직전 완료 봉 목표 비중 0%; 다음 봉 시가 가정 |
| v2 | trend_8_26 AND momentum_26 | 9761.14 | -238.86 | sell / filled / 직전 완료 봉 목표 비중 0%; 다음 봉 시가 가정 |
| v2 | trend_8_26 + momentum_26 | 9685.93 | -314.07 | sell / filled / 직전 완료 봉 목표 비중 0%; 다음 봉 시가 가정 |
| v2 | trend_8_26 AND breakout_8 | 9402.34 | -597.66 | sell / filled / 직전 완료 봉 목표 비중 0%; 다음 봉 시가 가정 |
| v2 | trend_8_26 + breakout_8 | 9331.39 | -668.61 | sell / filled / 직전 완료 봉 목표 비중 0%; 다음 봉 시가 가정 |
| v2 | trend_8_26 AND reversion_12 | 9687.61 | -312.39 | sell / filled / 직전 완료 봉 목표 비중 0%; 다음 봉 시가 가정 |
| v2 | trend_8_26 + reversion_12 | 9467.49 | -532.51 | sell / filled / 직전 완료 봉 목표 비중 0%; 다음 봉 시가 가정 |
| v2 | trend_8_26 AND volume_26 | 9787.80 | -212.20 | sell / filled / 직전 완료 봉 목표 비중 0%; 다음 봉 시가 가정 |
| v2 | trend_8_26 + volume_26 | 9571.02 | -428.98 | sell / filled / 직전 완료 봉 목표 비중 0%; 다음 봉 시가 가정 |
| v2 | momentum_26 AND breakout_8 | 9347.05 | -652.95 | sell / filled / 직전 완료 봉 목표 비중 0%; 다음 봉 시가 가정 |
| v2 | momentum_26 + breakout_8 | 9327.31 | -672.69 | sell / filled / 직전 완료 봉 목표 비중 0%; 다음 봉 시가 가정 |
| v2 | momentum_26 AND reversion_12 | 9831.84 | -168.16 | sell / filled / 직전 완료 봉 목표 비중 0%; 다음 봉 시가 가정 |
| v2 | momentum_26 + reversion_12 | 9563.23 | -436.77 | sell / filled / 직전 완료 봉 목표 비중 0%; 다음 봉 시가 가정 |
| v2 | momentum_26 AND volume_26 | 9869.24 | -130.76 | sell / filled / 직전 완료 봉 목표 비중 0%; 다음 봉 시가 가정 |
| v2 | momentum_26 + volume_26 | 9566.89 | -433.11 | sell / filled / 직전 완료 봉 목표 비중 0%; 다음 봉 시가 가정 |
| v2 | breakout_8 AND reversion_12 | 10000.00 | 0.00 | 대기 /  / 새 신호 대기 |
| v2 | breakout_8 + reversion_12 | 9174.38 | -825.62 | sell / filled / 직전 완료 봉 목표 비중 0%; 다음 봉 시가 가정 |
| v2 | breakout_8 AND volume_26 | 9710.25 | -289.75 | sell / filled / 직전 완료 봉 목표 비중 0%; 다음 봉 시가 가정 |
| v2 | breakout_8 + volume_26 | 9216.75 | -783.25 | sell / filled / 직전 완료 봉 목표 비중 0%; 다음 봉 시가 가정 |
| v2 | reversion_12 AND volume_26 | 9674.16 | -325.84 | sell / filled / 직전 완료 봉 목표 비중 0%; 다음 봉 시가 가정 |
| v2 | reversion_12 + volume_26 | 9391.11 | -608.89 | sell / filled / 직전 완료 봉 목표 비중 0%; 다음 봉 시가 가정 |
| v2 | ema_12_26 | 9809.32 | -190.68 | sell / filled / EMA12 > EMA26; 조건 미충족; EMA12=276.256, EMA26=276.345; 직전 완료 봉 목표를 다음 봉 시가에 모의 적용 |
| v2 | macd_12_26_9 | 9900.47 | -99.53 | sell / filled / MACD > 신호선 그리고 MACD > 0; 조건 미충족; MACD=0.978353, signal9=1.01104; 직전 완료 봉 목표를 다음 봉 시가에 모의 적용 |
| v2 | rsi_14_recovery | 9779.12 | -220.88 | sell / filled / 직전 RSI14 < 30, 현재 RSI14 >= 30 (한 봉 목표); 조건 미충족; RSI14=46.986, previous_RSI14=37.1649; 직전 완료 봉 목표를 다음 봉 시가에 모의 적용 |
| v2 | bollinger_20_reentry | 9840.32 | -159.68 | sell / filled / 직전 종가 < 직전 하단밴드, 현재 하단밴드 <= 종가 <= SMA20 (한 봉 목표); 조건 미충족; close=275.52, lower20=275.107, SMA20=276.469, previous_lower20=275.234; 직전 완료 봉 목표를 다음 봉 시가에 모의 적용 |
| v2 | donchian_20 | 9830.01 | -169.99 | sell / filled / 종가 > 현재 봉을 제외한 직전 20봉 최고가; 조건 미충족; close=275.785, prior_high20=276.875; 직전 완료 봉 목표를 다음 봉 시가에 모의 적용 |
| v2 | atr_14_breakout | 9719.27 | -280.73 | sell / filled / 종가 > 직전 종가 + 직전 ATR14 그리고 종가 > EMA26; 조건 미충족; close=276.06, threshold=277.643, prior_ATR14=0.662564, EMA26=276.447; 직전 완료 봉 목표를 다음 봉 시가에 모의 적용 |
| v2 | session_vwap | 9514.73 | -485.27 | sell / filled / 종가 > 뉴욕 거래일별 누적 전형가격 VWAP; 조건 미충족; close=275.532, session_VWAP=275.837, session_volume=1.37078e+07; 직전 완료 봉 목표를 다음 봉 시가에 모의 적용 |
| v2 | obv_20 | 9760.89 | -239.11 | sell / filled / OBV > OBV의 SMA20 그리고 종가 > EMA26; 조건 미충족; OBV=-1.90163e+07, OBV_SMA20=-1.97011e+07, close=275.532, EMA26=276.085; 직전 완료 봉 목표를 다음 봉 시가에 모의 적용 |
| v2 | stochastic_14_3_recovery | 9611.71 | -388.29 | sell / filled / 직전 %K14 < 20에서 %K14가 %D3 상향 돌파 (한 봉 목표); 조건 미충족; K14=39.2924, D3=31.5748, previous_K14=36.5078, previous_D3=30.3985; 직전 완료 봉 목표를 다음 봉 시가에 모의 적용 |
| v2 | mfi_14_recovery | 9930.25 | -69.75 | sell / filled / 직전 MFI14 < 20, 현재 MFI14 >= 20 (한 봉 목표); 조건 미충족; MFI14=34.131, previous_MFI14=22.0435; 직전 완료 봉 목표를 다음 봉 시가에 모의 적용 |
| v2 | adx_14_trend | 9718.27 | -281.73 | sell / filled / Wilder ADX14 >= 25 그리고 +DI14 > -DI14; 조건 미충족; ADX14=27.8461, plus_DI14=25.882, minus_DI14=28.4558; 직전 완료 봉 목표를 다음 봉 시가에 모의 적용 |
| v2 | aroon_25_trend | 9736.11 | -263.89 | sell / filled / Aroon25 Up > 70 그리고 Down < 30 (동률이면 최신 극값); 조건 미충족; Aroon_up=68, Aroon_down=4; 직전 완료 봉 목표를 다음 봉 시가에 모의 적용 |
| v2 | cci_20_momentum | 9815.69 | -184.31 | sell / filled / CCI20 > 100 (전형가격·평균절대편차); 조건 미충족; CCI20=-152.101; 직전 완료 봉 목표를 다음 봉 시가에 모의 적용 |
| v2 | williams_14_recovery | 9743.99 | -256.01 | sell / filled / 직전 Williams %R14 < -80, 현재 >= -80 (한 봉 목표); 조건 미충족; Williams_R14=-60.7076, previous_R14=-63.4922; 직전 완료 봉 목표를 다음 봉 시가에 모의 적용 |
| v2 | cmf_20_accumulation | 9691.65 | -308.35 | sell / filled / Chaikin Money Flow20 > 0.1; 조건 미충족; CMF20=0.0178538, volume20=1.46976e+07; 직전 완료 봉 목표를 다음 봉 시가에 모의 적용 |
| v2 | chaikin_3_10 | 9601.63 | -398.37 | sell / filled / ADL의 EMA3 - EMA10 > 0 그리고 종가 > EMA26; 조건 미충족; Chaikin3_10=188377, ADL=-3.27277e+07, close=275.532, EMA26=276.085; 직전 완료 봉 목표를 다음 봉 시가에 모의 적용 |
| v2 | roc_10_momentum | 9994.39 | -5.61 | sell / filled / 10봉 ROC > 1% 그리고 종가 > EMA26; 조건 미충족; ROC10_percent=0.995963, close=275.315, EMA26=273.754; 직전 완료 봉 목표를 다음 봉 시가에 모의 적용 |
| v2 | trix_15_trend | 9804.07 | -195.93 | sell / filled / 15봉 삼중 EMA의 1봉 변화율 TRIX > 0 그리고 종가 > EMA26; 조건 미충족; TRIX15_percent=0.00744142, close=276.06, EMA26=276.447; 직전 완료 봉 목표를 다음 봉 시가에 모의 적용 |
| v2 | keltner_20_breakout | 9873.30 | -126.70 | sell / filled / 종가 > EMA20 + 2 x Wilder ATR14; 조건 미충족; close=276.4, upper_Keltner=277.094, EMA20=275.768, ATR14=0.662947; 직전 완료 봉 목표를 다음 봉 시가에 모의 적용 |
| v2 | opening_range_30m | 9959.17 | -40.83 | sell / filled / 뉴욕 09:30·09:45 두 완료 봉 최고가를 10:00 이후 종가가 돌파; 자료 부족·변동폭 또는 거래량 없음: 대기; close=276.82; 직전 완료 봉 목표를 다음 봉 시가에 모의 적용 |

### 같은 기간의 비용·노출 비교 (사후 연구)

| 전략 | 비용 전 | 비용 후 | 100% 보유 | 같은 평균 노출 보유 | 평균 노출 |
|---|---:|---:|---:|---:|---:|
| cash | 0.00% | 0.00% | -1.45% | -0.00% | 0.00% |
| buy_hold | -1.03% | -1.45% | -1.45% | -1.45% | 100.00% |
| trend_8_26 | 0.07% | -3.23% | -1.45% | -0.73% | 49.87% |
| momentum_26 | -0.08% | -5.39% | -1.45% | -0.70% | 47.77% |
| breakout_8 | -0.92% | -15.54% | -1.45% | -0.29% | 19.95% |
| reversion_12 | -0.85% | -12.59% | -1.45% | -0.39% | 26.77% |
| volume_26 | -0.50% | -7.75% | -1.45% | -0.12% | 8.40% |
| trend_8_26 AND momentum_26 | -0.05% | -3.75% | -1.45% | -0.61% | 41.99% |
| trend_8_26 + momentum_26 | 0.00% | -3.91% | -1.45% | -0.71% | 48.82% |
| trend_8_26 AND breakout_8 | -0.23% | -9.42% | -1.45% | -0.20% | 13.39% |
| trend_8_26 + breakout_8 | -0.42% | -9.40% | -1.45% | -0.51% | 34.91% |
| trend_8_26 AND reversion_12 | -0.50% | -4.60% | -1.45% | -0.08% | 5.51% |
| trend_8_26 + reversion_12 | -0.38% | -8.04% | -1.45% | -0.56% | 38.33% |
| trend_8_26 AND volume_26 | -0.37% | -3.25% | -1.45% | -0.03% | 2.36% |
| trend_8_26 + volume_26 | -0.20% | -5.12% | -1.45% | -0.43% | 29.14% |
| momentum_26 AND breakout_8 | 0.22% | -9.39% | -1.45% | -0.19% | 13.12% |
| momentum_26 + breakout_8 | -0.50% | -10.42% | -1.45% | -0.49% | 33.86% |
| momentum_26 AND reversion_12 | -0.09% | -2.98% | -1.45% | -0.04% | 2.89% |
| momentum_26 + reversion_12 | -0.46% | -7.72% | -1.45% | -0.54% | 37.28% |
| momentum_26 AND volume_26 | 0.01% | -2.89% | -1.45% | -0.03% | 2.36% |
| momentum_26 + volume_26 | -0.29% | -5.99% | -1.45% | -0.41% | 28.09% |
| breakout_8 AND reversion_12 | 0.00% | 0.00% | -1.45% | -0.00% | 0.00% |
| breakout_8 + reversion_12 | -0.88% | -13.36% | -1.45% | -0.34% | 23.37% |
| breakout_8 AND volume_26 | -0.54% | -3.42% | -1.45% | -0.03% | 2.10% |
| breakout_8 + volume_26 | -0.71% | -11.36% | -1.45% | -0.21% | 14.18% |
| reversion_12 AND volume_26 | 0.60% | -3.54% | -1.45% | -0.05% | 3.41% |
| reversion_12 + volume_26 | -0.67% | -9.45% | -1.45% | -0.26% | 17.59% |
| ema_12_26 | 1.31% | -1.21% | -1.45% | -0.74% | 50.66% |
| macd_12_26_9 | 3.17% | 0.60% | -1.45% | -0.39% | 26.51% |
| rsi_14_recovery | -0.88% | -4.95% | -1.45% | -0.04% | 2.62% |
| bollinger_20_reentry | -0.20% | -4.70% | -1.45% | -0.04% | 2.89% |
| donchian_20 | -0.04% | -4.96% | -1.45% | -0.08% | 5.77% |
| atr_14_breakout | -0.63% | -7.48% | -1.45% | -0.07% | 4.72% |
| session_vwap | -0.01% | -11.10% | -1.45% | -0.67% | 46.19% |
| obv_20 | 0.91% | -3.65% | -1.45% | -0.65% | 44.36% |
| stochastic_14_3_recovery | -0.30% | -12.47% | -1.45% | -0.12% | 8.14% |
| mfi_14_recovery | 0.20% | -3.92% | -1.45% | -0.04% | 2.62% |
| adx_14_trend | -0.12% | -3.02% | -1.45% | -0.50% | 34.38% |
| aroon_25_trend | -0.77% | -5.25% | -1.45% | -0.31% | 21.26% |
| cci_20_momentum | -0.99% | -7.42% | -1.45% | -0.29% | 19.69% |
| williams_14_recovery | 0.41% | -9.22% | -1.45% | -0.09% | 6.30% |
| cmf_20_accumulation | 0.17% | -6.73% | -1.45% | -0.34% | 23.36% |
| chaikin_3_10 | -1.37% | -8.55% | -1.45% | -0.51% | 34.65% |
| roc_10_momentum | -0.02% | -1.27% | -1.45% | -0.07% | 4.99% |
| trix_15_trend | 1.13% | -2.62% | -1.45% | -0.59% | 40.68% |
| keltner_20_breakout | -0.10% | -3.40% | -1.45% | -0.11% | 7.35% |
| opening_range_30m | 2.69% | -1.53% | -1.45% | -0.36% | 24.41% |

동일 구간·초기 자금, 종료 시 청산 비용 포함. 노출 맞춤은 사후 설명용이며 v2 실제 계좌 성과가 아닙니다.
[낙폭 분해·비용 영향·전체 구간](IWM/comparison.json)

[v1 전체 기록](IWM/accounts.json) · [v2 전체 기록](IWM/accounts-v2.json)

## DIA 계좌

| 모델 | 전략 | 평가액 USD | 손익 USD | 최근 매매·이유 |
|---|---|---:|---:|---|
| v1 | cash | 10000.00 | 0.00 | 대기 /  / 새 신호 대기 |
| v1 | buy_hold | 10063.44 | 63.44 | buy /  / buy_hold: prior completed bar target 100%; next bar open simulation |
| v1 | trend_8_26 | 9969.94 | -30.06 | buy /  / trend_8_26: prior completed bar target 100%; next bar open simulation |
| v1 | momentum_26 | 9862.90 | -137.10 | buy /  / momentum_26: prior completed bar target 100%; next bar open simulation |
| v1 | breakout_8 | 9378.75 | -621.25 | sell /  / breakout_8: prior completed bar target 0%; next bar open simulation |
| v1 | reversion_12 | 9822.56 | -177.44 | sell /  / reversion_12: prior completed bar target 0%; next bar open simulation |
| v1 | volume_26 | 9816.03 | -183.97 | sell /  / volume_26: prior completed bar target 0%; next bar open simulation |
| v1 | trend_8_26 AND momentum_26 | 9859.72 | -140.28 | buy /  / trend_8_26 AND momentum_26: prior completed bar target 100%; next bar open simulation |
| v1 | trend_8_26 + momentum_26 | 9916.33 | -83.67 | buy /  / trend_8_26 + momentum_26: prior completed bar target 100%; next bar open simulation |
| v1 | trend_8_26 AND breakout_8 | 9649.65 | -350.35 | sell /  / trend_8_26 AND breakout_8: prior completed bar target 0%; next bar open simulation |
| v1 | trend_8_26 + breakout_8 | 9728.05 | -271.95 | buy /  / trend_8_26 + breakout_8: prior completed bar target 50%; next bar open simulation |
| v1 | trend_8_26 AND reversion_12 | 9865.72 | -134.28 | sell /  / trend_8_26 AND reversion_12: prior completed bar target 0%; next bar open simulation |
| v1 | trend_8_26 + reversion_12 | 9895.77 | -104.23 | buy /  / trend_8_26 + reversion_12: prior completed bar target 50%; next bar open simulation |
| v1 | trend_8_26 AND volume_26 | 9888.21 | -111.79 | sell /  / trend_8_26 AND volume_26: prior completed bar target 0%; next bar open simulation |
| v1 | trend_8_26 + volume_26 | 9892.49 | -107.51 | buy /  / trend_8_26 + volume_26: prior completed bar target 50%; next bar open simulation |
| v1 | momentum_26 AND breakout_8 | 9506.61 | -493.39 | sell /  / momentum_26 AND breakout_8: prior completed bar target 0%; next bar open simulation |
| v1 | momentum_26 + breakout_8 | 9617.90 | -382.10 | sell /  / momentum_26 + breakout_8: prior completed bar target 50%; next bar open simulation |
| v1 | momentum_26 AND reversion_12 | 9865.74 | -134.26 | sell /  / momentum_26 AND reversion_12: prior completed bar target 0%; next bar open simulation |
| v1 | momentum_26 + reversion_12 | 9881.92 | -118.08 | buy /  / momentum_26 + reversion_12: prior completed bar target 50%; next bar open simulation |
| v1 | momentum_26 AND volume_26 | 9805.85 | -194.15 | sell /  / momentum_26 AND volume_26: prior completed bar target 0%; next bar open simulation |
| v1 | momentum_26 + volume_26 | 9859.01 | -140.99 | buy /  / momentum_26 + volume_26: prior completed bar target 50%; next bar open simulation |
| v1 | breakout_8 AND reversion_12 | 10000.00 | 0.00 | 대기 /  / 새 신호 대기 |
| v1 | breakout_8 + reversion_12 | 9617.07 | -382.93 | sell /  / breakout_8 + reversion_12: prior completed bar target 0%; next bar open simulation |
| v1 | breakout_8 AND volume_26 | 9925.92 | -74.08 | sell /  / breakout_8 AND volume_26: prior completed bar target 0%; next bar open simulation |
| v1 | breakout_8 + volume_26 | 9633.26 | -366.74 | sell /  / breakout_8 + volume_26: prior completed bar target 0%; next bar open simulation |
| v1 | reversion_12 AND volume_26 | 9970.42 | -29.58 | sell /  / reversion_12 AND volume_26: prior completed bar target 0%; next bar open simulation |
| v1 | reversion_12 + volume_26 | 9858.49 | -141.51 | sell /  / reversion_12 + volume_26: prior completed bar target 0%; next bar open simulation |
| v1 | ema_12_26 | 9917.31 | -82.69 | buy /  / EMA12 > EMA26; 조건 충족; EMA12=519.74, EMA26=519.585 |
| v1 | macd_12_26_9 | 9834.94 | -165.06 | buy /  / MACD > 신호선 그리고 MACD > 0; 조건 충족; MACD=0.347133, signal9=0.325402 |
| v1 | rsi_14_recovery | 10000.00 | 0.00 | 대기 /  / 새 신호 대기 |
| v1 | bollinger_20_reentry | 9939.81 | -60.19 | sell /  / 직전 종가 < 직전 하단밴드, 현재 하단밴드 <= 종가 <= SMA20 (한 봉 목표); 조건 미충족; close=525.81, lower20=524.898, SMA20=526.51, previous_lower20=524.945 |
| v1 | donchian_20 | 9675.11 | -324.89 | sell /  / 종가 > 현재 봉을 제외한 직전 20봉 최고가; 조건 미충족; close=526.71, prior_high20=528.45 |
| v1 | atr_14_breakout | 9709.35 | -290.65 | sell /  / 종가 > 직전 종가 + 직전 ATR14 그리고 종가 > EMA26; 조건 미충족; close=527.625, threshold=528.531, prior_ATR14=1.00085, EMA26=526.218 |
| v1 | session_vwap | 9806.18 | -193.82 | buy /  / 종가 > 뉴욕 거래일별 누적 전형가격 VWAP; 조건 충족; close=526.37, session_VWAP=526.232, session_volume=1.64733e+06 |
| v1 | obv_20 | 9851.67 | -148.33 | sell /  / OBV > OBV의 SMA20 그리고 종가 > EMA26; 조건 미충족; OBV=-5.81025e+06, OBV_SMA20=-5.32802e+06, close=526.941, EMA26=526.147 |
| v1 | stochastic_14_3_recovery | 9702.74 | -297.26 | sell /  / 직전 %K14 < 20에서 %K14가 %D3 상향 돌파 (한 봉 목표); 조건 미충족; K14=43.4299, D3=31.8109, previous_K14=42.0016, previous_D3=18.964 |
| v1 | mfi_14_recovery | 9902.01 | -97.99 | sell /  / 직전 MFI14 < 20, 현재 MFI14 >= 20 (한 봉 목표); 조건 미충족; MFI14=29.4378, previous_MFI14=21.6288 |
| v1 | adx_14_trend | 9711.49 | -288.51 | sell /  / Wilder ADX14 >= 25 그리고 +DI14 > -DI14; 조건 미충족; ADX14=28.0997, plus_DI14=30.0206, minus_DI14=36.1913 |
| v1 | aroon_25_trend | 9820.69 | -179.31 | sell /  / Aroon25 Up > 70 그리고 Down < 30 (동률이면 최신 극값); 조건 미충족; Aroon_up=72, Aroon_down=92 |
| v1 | cci_20_momentum | 9758.00 | -242.00 | sell /  / CCI20 > 100 (전형가격·평균절대편차); 조건 미충족; CCI20=65.0571 |
| v1 | williams_14_recovery | 9735.64 | -264.36 | sell /  / 직전 Williams %R14 < -80, 현재 >= -80 (한 봉 목표); 조건 미충족; Williams_R14=-56.5701, previous_R14=-57.9984 |
| v1 | cmf_20_accumulation | 9588.02 | -411.98 | buy /  / Chaikin Money Flow20 > 0.1; 조건 충족; CMF20=0.162227, volume20=1.04086e+06 |
| v1 | chaikin_3_10 | 9818.86 | -181.14 | buy /  / ADL의 EMA3 - EMA10 > 0 그리고 종가 > EMA26; 조건 충족; Chaikin3_10=215386, ADL=-1.16382e+07, close=526.37, EMA26=525.963 |
| v1 | roc_10_momentum | 9939.01 | -60.99 | sell /  / 10봉 ROC > 1% 그리고 종가 > EMA26; 조건 미충족; ROC10_percent=0.771645, close=523.68, EMA26=521.367 |
| v1 | trix_15_trend | 9952.22 | -47.78 | buy /  / 15봉 삼중 EMA의 1봉 변화율 TRIX > 0 그리고 종가 > EMA26; 조건 충족; TRIX15_percent=0.0108744, close=526.37, EMA26=525.963 |
| v1 | keltner_20_breakout | 9826.82 | -173.18 | sell /  / 종가 > EMA20 + 2 x Wilder ATR14; 조건 미충족; close=526.34, upper_Keltner=527.991, EMA20=526.293, ATR14=0.848911 |
| v1 | opening_range_30m | 9583.64 | -416.36 | sell /  / 뉴욕 09:30·09:45 두 완료 봉 최고가를 10:00 이후 종가가 돌파; 조건 미충족; close=526.71, opening_high=527.34 |
| v2 | cash | 10000.00 | 0.00 | 대기 /  / 새 신호 대기 |
| v2 | buy_hold | 10188.11 | 188.11 | buy / partial / 직전 완료 봉 목표 비중 100%; 다음 봉 시가 가정 |
| v2 | trend_8_26 | 9899.40 | -100.60 | buy / partial / 직전 완료 봉 목표 비중 100%; 다음 봉 시가 가정 |
| v2 | momentum_26 | 9898.82 | -101.18 | buy / partial / 직전 완료 봉 목표 비중 100%; 다음 봉 시가 가정 |
| v2 | breakout_8 | 9017.70 | -982.30 | 중단: 손실 한도 / buy / partial / 직전 완료 봉 목표 비중 100%; 다음 봉 시가 가정 |
| v2 | reversion_12 | 9514.52 | -485.48 | sell / filled / 직전 완료 봉 목표 비중 0%; 다음 봉 시가 가정 |
| v2 | volume_26 | 9526.08 | -473.92 | sell / filled / 직전 완료 봉 목표 비중 0%; 다음 봉 시가 가정 |
| v2 | trend_8_26 AND momentum_26 | 9889.06 | -110.94 | buy / partial / 직전 완료 봉 목표 비중 100%; 다음 봉 시가 가정 |
| v2 | trend_8_26 + momentum_26 | 9899.23 | -100.77 | buy / partial / 직전 완료 봉 목표 비중 100%; 다음 봉 시가 가정 |
| v2 | trend_8_26 AND breakout_8 | 9330.55 | -669.45 | sell / filled / 직전 완료 봉 목표 비중 0%; 다음 봉 시가 가정 |
| v2 | trend_8_26 + breakout_8 | 9450.50 | -549.50 | buy / filled / 직전 완료 봉 목표 비중 50%; 다음 봉 시가 가정 |
| v2 | trend_8_26 AND reversion_12 | 9669.36 | -330.64 | sell / filled / 직전 완료 봉 목표 비중 0%; 다음 봉 시가 가정 |
| v2 | trend_8_26 + reversion_12 | 9704.59 | -295.41 | buy / filled / 직전 완료 봉 목표 비중 50%; 다음 봉 시가 가정 |
| v2 | trend_8_26 AND volume_26 | 9738.93 | -261.07 | sell / filled / 직전 완료 봉 목표 비중 0%; 다음 봉 시가 가정 |
| v2 | trend_8_26 + volume_26 | 9731.11 | -268.89 | buy / filled / 직전 완료 봉 목표 비중 50%; 다음 봉 시가 가정 |
| v2 | momentum_26 AND breakout_8 | 9178.11 | -821.89 | sell / filled / 직전 완료 봉 목표 비중 0%; 다음 봉 시가 가정 |
| v2 | momentum_26 + breakout_8 | 9391.03 | -608.97 | sell / filled / 직전 완료 봉 목표 비중 50%; 다음 봉 시가 가정 |
| v2 | momentum_26 AND reversion_12 | 9814.45 | -185.55 | sell / filled / 직전 완료 봉 목표 비중 0%; 다음 봉 시가 가정 |
| v2 | momentum_26 + reversion_12 | 9745.18 | -254.82 | buy / filled / 직전 완료 봉 목표 비중 50%; 다음 봉 시가 가정 |
| v2 | momentum_26 AND volume_26 | 9589.81 | -410.19 | sell / filled / 직전 완료 봉 목표 비중 0%; 다음 봉 시가 가정 |
| v2 | momentum_26 + volume_26 | 9771.97 | -228.03 | buy / filled / 직전 완료 봉 목표 비중 50%; 다음 봉 시가 가정 |
| v2 | breakout_8 AND reversion_12 | 10000.00 | 0.00 | 대기 /  / 새 신호 대기 |
| v2 | breakout_8 + reversion_12 | 9225.36 | -774.64 | sell / filled / 직전 완료 봉 목표 비중 0%; 다음 봉 시가 가정 |
| v2 | breakout_8 AND volume_26 | 9718.15 | -281.85 | sell / filled / 직전 완료 봉 목표 비중 0%; 다음 봉 시가 가정 |
| v2 | breakout_8 + volume_26 | 9250.79 | -749.21 | sell / filled / 직전 완료 봉 목표 비중 0%; 다음 봉 시가 가정 |
| v2 | reversion_12 AND volume_26 | 9966.44 | -33.56 | sell / filled / 직전 완료 봉 목표 비중 0%; 다음 봉 시가 가정 |
| v2 | reversion_12 + volume_26 | 9559.93 | -440.07 | sell / filled / 직전 완료 봉 목표 비중 0%; 다음 봉 시가 가정 |
| v2 | ema_12_26 | 9912.36 | -87.64 | buy / partial / EMA12 > EMA26; 조건 충족; EMA12=519.74, EMA26=519.585; 직전 완료 봉 목표를 다음 봉 시가에 모의 적용 |
| v2 | macd_12_26_9 | 9826.09 | -173.91 | buy / partial / MACD > 신호선 그리고 MACD > 0; 조건 충족; MACD=0.347133, signal9=0.325402; 직전 완료 봉 목표를 다음 봉 시가에 모의 적용 |
| v2 | rsi_14_recovery | 10000.00 | 0.00 | 대기 /  / 새 신호 대기 |
| v2 | bollinger_20_reentry | 9935.84 | -64.16 | sell / filled / 직전 종가 < 직전 하단밴드, 현재 하단밴드 <= 종가 <= SMA20 (한 봉 목표); 조건 미충족; close=525.81, lower20=524.898, SMA20=526.51, previous_lower20=524.945; 직전 완료 봉 목표를 다음 봉 시가에 모의 적용 |
| v2 | donchian_20 | 9661.57 | -338.43 | sell / filled / 종가 > 현재 봉을 제외한 직전 20봉 최고가; 조건 미충족; close=526.71, prior_high20=528.45; 직전 완료 봉 목표를 다음 봉 시가에 모의 적용 |
| v2 | atr_14_breakout | 9693.83 | -306.17 | sell / filled / 종가 > 직전 종가 + 직전 ATR14 그리고 종가 > EMA26; 조건 미충족; close=527.625, threshold=528.531, prior_ATR14=1.00085, EMA26=526.218; 직전 완료 봉 목표를 다음 봉 시가에 모의 적용 |
| v2 | session_vwap | 9793.44 | -206.56 | buy / partial / 종가 > 뉴욕 거래일별 누적 전형가격 VWAP; 조건 충족; close=526.37, session_VWAP=526.232, session_volume=1.64733e+06; 직전 완료 봉 목표를 다음 봉 시가에 모의 적용 |
| v2 | obv_20 | 9841.82 | -158.18 | sell / filled / OBV > OBV의 SMA20 그리고 종가 > EMA26; 조건 미충족; OBV=-5.81025e+06, OBV_SMA20=-5.32802e+06, close=526.941, EMA26=526.147; 직전 완료 봉 목표를 다음 봉 시가에 모의 적용 |
| v2 | stochastic_14_3_recovery | 9687.23 | -312.77 | sell / filled / 직전 %K14 < 20에서 %K14가 %D3 상향 돌파 (한 봉 목표); 조건 미충족; K14=43.4299, D3=31.8109, previous_K14=42.0016, previous_D3=18.964; 직전 완료 봉 목표를 다음 봉 시가에 모의 적용 |
| v2 | mfi_14_recovery | 9896.07 | -103.93 | sell / filled / 직전 MFI14 < 20, 현재 MFI14 >= 20 (한 봉 목표); 조건 미충족; MFI14=29.4378, previous_MFI14=21.6288; 직전 완료 봉 목표를 다음 봉 시가에 모의 적용 |
| v2 | adx_14_trend | 9701.78 | -298.22 | sell / filled / Wilder ADX14 >= 25 그리고 +DI14 > -DI14; 조건 미충족; ADX14=28.0997, plus_DI14=30.0206, minus_DI14=36.1913; 직전 완료 봉 목표를 다음 봉 시가에 모의 적용 |
| v2 | aroon_25_trend | 9810.88 | -189.12 | sell / filled / Aroon25 Up > 70 그리고 Down < 30 (동률이면 최신 극값); 조건 미충족; Aroon_up=72, Aroon_down=92; 직전 완료 봉 목표를 다음 봉 시가에 모의 적용 |
| v2 | cci_20_momentum | 9744.35 | -255.65 | sell / filled / CCI20 > 100 (전형가격·평균절대편차); 조건 미충족; CCI20=65.0571; 직전 완료 봉 목표를 다음 봉 시가에 모의 적용 |
| v2 | williams_14_recovery | 9722.02 | -277.98 | sell / filled / 직전 Williams %R14 < -80, 현재 >= -80 (한 봉 목표); 조건 미충족; Williams_R14=-56.5701, previous_R14=-57.9984; 직전 완료 봉 목표를 다음 봉 시가에 모의 적용 |
| v2 | cmf_20_accumulation | 9569.82 | -430.18 | buy / partial / Chaikin Money Flow20 > 0.1; 조건 충족; CMF20=0.162227, volume20=1.04086e+06; 직전 완료 봉 목표를 다음 봉 시가에 모의 적용 |
| v2 | chaikin_3_10 | 9808.06 | -191.94 | buy / partial / ADL의 EMA3 - EMA10 > 0 그리고 종가 > EMA26; 조건 충족; Chaikin3_10=215386, ADL=-1.16382e+07, close=526.37, EMA26=525.963; 직전 완료 봉 목표를 다음 봉 시가에 모의 적용 |
| v2 | roc_10_momentum | 9937.03 | -62.97 | sell / filled / 10봉 ROC > 1% 그리고 종가 > EMA26; 조건 미충족; ROC10_percent=0.771645, close=523.68, EMA26=521.367; 직전 완료 봉 목표를 다음 봉 시가에 모의 적용 |
| v2 | trix_15_trend | 9947.25 | -52.75 | buy / partial / 15봉 삼중 EMA의 1봉 변화율 TRIX > 0 그리고 종가 > EMA26; 조건 충족; TRIX15_percent=0.0108744, close=526.37, EMA26=525.963; 직전 완료 봉 목표를 다음 봉 시가에 모의 적용 |
| v2 | keltner_20_breakout | 9817.00 | -183.00 | sell / filled / 종가 > EMA20 + 2 x Wilder ATR14; 조건 미충족; close=526.34, upper_Keltner=527.991, EMA20=526.293, ATR14=0.848911; 직전 완료 봉 목표를 다음 봉 시가에 모의 적용 |
| v2 | opening_range_30m | 9566.41 | -433.59 | sell / filled / 뉴욕 09:30·09:45 두 완료 봉 최고가를 10:00 이후 종가가 돌파; 조건 미충족; close=526.71, opening_high=527.34; 직전 완료 봉 목표를 다음 봉 시가에 모의 적용 |

### 같은 기간의 비용·노출 비교 (사후 연구)

| 전략 | 비용 전 | 비용 후 | 100% 보유 | 같은 평균 노출 보유 | 평균 노출 |
|---|---:|---:|---:|---:|---:|
| cash | 0.00% | 0.00% | 3.22% | 0.00% | 0.00% |
| buy_hold | 3.65% | 3.22% | 3.22% | 3.22% | 100.00% |
| trend_8_26 | 3.27% | -0.97% | 3.22% | 2.15% | 66.93% |
| momentum_26 | 1.61% | -2.57% | 3.22% | 2.08% | 64.83% |
| breakout_8 | 0.35% | -17.97% | 3.22% | 0.85% | 26.51% |
| reversion_12 | 0.92% | -6.82% | 3.22% | 0.57% | 17.85% |
| volume_26 | 0.99% | -8.31% | 3.22% | 0.33% | 10.24% |
| trend_8_26 AND momentum_26 | 3.00% | -1.65% | 3.22% | 1.86% | 58.01% |
| trend_8_26 + momentum_26 | 2.44% | -1.77% | 3.22% | 2.11% | 65.88% |
| trend_8_26 AND breakout_8 | 1.43% | -12.44% | 3.22% | 0.61% | 19.16% |
| trend_8_26 + breakout_8 | 1.81% | -9.11% | 3.22% | 1.49% | 46.73% |
| trend_8_26 AND reversion_12 | 0.81% | -4.55% | 3.22% | 0.23% | 7.09% |
| trend_8_26 + reversion_12 | 2.09% | -3.75% | 3.22% | 1.35% | 42.39% |
| trend_8_26 AND volume_26 | 1.59% | -4.61% | 3.22% | 0.20% | 6.30% |
| trend_8_26 + volume_26 | 2.13% | -4.52% | 3.22% | 1.23% | 38.59% |
| momentum_26 AND breakout_8 | -0.10% | -14.48% | 3.22% | 0.68% | 21.26% |
| momentum_26 + breakout_8 | 0.98% | -10.41% | 3.22% | 1.46% | 45.68% |
| momentum_26 AND reversion_12 | 0.10% | -3.21% | 3.22% | 0.18% | 5.51% |
| momentum_26 + reversion_12 | 1.27% | -3.92% | 3.22% | 1.32% | 41.34% |
| momentum_26 AND volume_26 | 0.04% | -6.85% | 3.22% | 0.21% | 6.56% |
| momentum_26 + volume_26 | 1.30% | -4.89% | 3.22% | 1.20% | 37.54% |
| breakout_8 AND reversion_12 | 0.00% | 0.00% | 3.22% | 0.00% | 0.00% |
| breakout_8 + reversion_12 | 0.64% | -12.22% | 3.22% | 0.71% | 22.19% |
| breakout_8 AND volume_26 | -0.27% | -4.37% | 3.22% | 0.12% | 3.67% |
| breakout_8 + volume_26 | 0.67% | -12.37% | 3.22% | 0.59% | 18.38% |
| reversion_12 AND volume_26 | 0.94% | -1.99% | 3.22% | 0.07% | 2.10% |
| reversion_12 + volume_26 | 0.95% | -7.19% | 3.22% | 0.45% | 14.05% |
| ema_12_26 | 1.39% | -1.13% | 3.22% | 2.07% | 64.57% |
| macd_12_26_9 | 2.23% | -1.97% | 3.22% | 1.09% | 34.12% |
| rsi_14_recovery | 0.14% | -0.69% | 3.22% | 0.02% | 0.52% |
| bollinger_20_reentry | 0.35% | -2.56% | 3.22% | 0.06% | 1.84% |
| donchian_20 | 0.06% | -8.39% | 3.22% | 0.36% | 11.29% |
| atr_14_breakout | -0.46% | -9.25% | 3.22% | 0.22% | 6.82% |
| session_vwap | 2.80% | -4.68% | 3.22% | 1.88% | 58.79% |
| obv_20 | 1.73% | -5.67% | 3.22% | 1.65% | 51.44% |
| stochastic_14_3_recovery | 1.36% | -9.12% | 3.22% | 0.22% | 6.82% |
| mfi_14_recovery | 0.37% | -2.95% | 3.22% | 0.07% | 2.10% |
| adx_14_trend | -0.02% | -4.14% | 3.22% | 1.07% | 33.60% |
| aroon_25_trend | 1.33% | -2.84% | 3.22% | 0.95% | 29.92% |
| cci_20_momentum | 1.15% | -5.82% | 3.22% | 0.95% | 29.66% |
| williams_14_recovery | 1.55% | -5.85% | 3.22% | 0.15% | 4.72% |
| cmf_20_accumulation | 1.18% | -8.52% | 3.22% | 1.30% | 40.68% |
| chaikin_3_10 | 2.53% | -6.91% | 3.22% | 1.79% | 55.91% |
| roc_10_momentum | -0.07% | -0.90% | 3.22% | 0.07% | 2.10% |
| trix_15_trend | 1.24% | -2.52% | 3.22% | 1.85% | 57.74% |
| keltner_20_breakout | 0.79% | -6.94% | 3.22% | 0.64% | 20.21% |
| opening_range_30m | 1.19% | -6.18% | 3.22% | 1.04% | 32.55% |

동일 구간·초기 자금, 종료 시 청산 비용 포함. 노출 맞춤은 사후 설명용이며 v2 실제 계좌 성과가 아닙니다.
[낙폭 분해·비용 영향·전체 구간](DIA/comparison.json)

[v1 전체 기록](DIA/accounts.json) · [v2 전체 기록](DIA/accounts-v2.json)

## MSFT 계좌

| 모델 | 전략 | 평가액 USD | 손익 USD | 최근 매매·이유 |
|---|---|---:|---:|---|
| v1 | cash | 10000.00 | 0.00 | 대기 /  / 새 신호 대기 |
| v1 | buy_hold | 9692.28 | -307.72 | buy /  / buy_hold: prior completed bar target 100%; next bar open simulation |
| v1 | trend_8_26 | 9433.22 | -566.78 | sell /  / trend_8_26: prior completed bar target 0%; next bar open simulation |
| v1 | momentum_26 | 9297.87 | -702.13 | sell /  / momentum_26: prior completed bar target 0%; next bar open simulation |
| v1 | breakout_8 | 9511.89 | -488.11 | sell /  / breakout_8: prior completed bar target 0%; next bar open simulation |
| v1 | reversion_12 | 9431.50 | -568.50 | sell /  / reversion_12: prior completed bar target 0%; next bar open simulation |
| v1 | volume_26 | 9623.19 | -376.81 | sell /  / volume_26: prior completed bar target 0%; next bar open simulation |
| v1 | trend_8_26 AND momentum_26 | 9427.87 | -572.13 | sell /  / trend_8_26 AND momentum_26: prior completed bar target 0%; next bar open simulation |
| v1 | trend_8_26 + momentum_26 | 9402.84 | -597.16 | sell /  / trend_8_26 + momentum_26: prior completed bar target 0%; next bar open simulation |
| v1 | trend_8_26 AND breakout_8 | 9678.51 | -321.49 | sell /  / trend_8_26 AND breakout_8: prior completed bar target 0%; next bar open simulation |
| v1 | trend_8_26 + breakout_8 | 9510.67 | -489.33 | sell /  / trend_8_26 + breakout_8: prior completed bar target 0%; next bar open simulation |
| v1 | trend_8_26 AND reversion_12 | 9519.35 | -480.65 | sell /  / trend_8_26 AND reversion_12: prior completed bar target 0%; next bar open simulation |
| v1 | trend_8_26 + reversion_12 | 9451.14 | -548.86 | sell /  / trend_8_26 + reversion_12: prior completed bar target 0%; next bar open simulation |
| v1 | trend_8_26 AND volume_26 | 9802.11 | -197.89 | sell /  / trend_8_26 AND volume_26: prior completed bar target 0%; next bar open simulation |
| v1 | trend_8_26 + volume_26 | 9527.85 | -472.15 | sell /  / trend_8_26 + volume_26: prior completed bar target 0%; next bar open simulation |
| v1 | momentum_26 AND breakout_8 | 9642.25 | -357.75 | sell /  / momentum_26 AND breakout_8: prior completed bar target 0%; next bar open simulation |
| v1 | momentum_26 + breakout_8 | 9423.30 | -576.70 | sell /  / momentum_26 + breakout_8: prior completed bar target 0%; next bar open simulation |
| v1 | momentum_26 AND reversion_12 | 9649.76 | -350.24 | sell /  / momentum_26 AND reversion_12: prior completed bar target 0%; next bar open simulation |
| v1 | momentum_26 + reversion_12 | 9420.66 | -579.34 | sell /  / momentum_26 + reversion_12: prior completed bar target 0%; next bar open simulation |
| v1 | momentum_26 AND volume_26 | 9830.16 | -169.84 | sell /  / momentum_26 AND volume_26: prior completed bar target 0%; next bar open simulation |
| v1 | momentum_26 + volume_26 | 9478.30 | -521.70 | sell /  / momentum_26 + volume_26: prior completed bar target 0%; next bar open simulation |
| v1 | breakout_8 AND reversion_12 | 10000.00 | 0.00 | 대기 /  / 새 신호 대기 |
| v1 | breakout_8 + reversion_12 | 9509.38 | -490.62 | sell /  / breakout_8 + reversion_12: prior completed bar target 0%; next bar open simulation |
| v1 | breakout_8 AND volume_26 | 9953.19 | -46.81 | sell /  / breakout_8 AND volume_26: prior completed bar target 0%; next bar open simulation |
| v1 | breakout_8 + volume_26 | 9605.54 | -394.46 | sell /  / breakout_8 + volume_26: prior completed bar target 0%; next bar open simulation |
| v1 | reversion_12 AND volume_26 | 9770.39 | -229.61 | sell /  / reversion_12 AND volume_26: prior completed bar target 0%; next bar open simulation |
| v1 | reversion_12 + volume_26 | 9545.85 | -454.15 | sell /  / reversion_12 + volume_26: prior completed bar target 0%; next bar open simulation |
| v1 | ema_12_26 | 9491.42 | -508.58 | sell /  / EMA12 > EMA26; 조건 미충족; EMA12=531.766, EMA26=531.788 |
| v1 | macd_12_26_9 | 9603.93 | -396.07 | sell /  / MACD > 신호선 그리고 MACD > 0; 조건 미충족; MACD=-0.0222122, signal9=0.149678 |
| v1 | rsi_14_recovery | 9932.10 | -67.90 | sell /  / 직전 RSI14 < 30, 현재 RSI14 >= 30 (한 봉 목표); 조건 미충족; RSI14=39.2066, previous_RSI14=35.1952 |
| v1 | bollinger_20_reentry | 9789.12 | -210.88 | sell /  / 직전 종가 < 직전 하단밴드, 현재 하단밴드 <= 종가 <= SMA20 (한 봉 목표); 조건 미충족; close=526.675, lower20=523.276, SMA20=530.073, previous_lower20=523.675 |
| v1 | donchian_20 | 9912.16 | -87.84 | sell /  / 종가 > 현재 봉을 제외한 직전 20봉 최고가; 조건 미충족; close=534.52, prior_high20=535.44 |
| v1 | atr_14_breakout | 9915.10 | -84.90 | sell /  / 종가 > 직전 종가 + 직전 ATR14 그리고 종가 > EMA26; 조건 미충족; close=533.975, threshold=536.307, prior_ATR14=2.16203, EMA26=530.521 |
| v1 | session_vwap | 9639.41 | -360.59 | sell /  / 종가 > 뉴욕 거래일별 누적 전형가격 VWAP; 조건 미충족; close=524.76, session_VWAP=524.823, session_volume=2.14412e+07 |
| v1 | obv_20 | 9537.51 | -462.49 | sell /  / OBV > OBV의 SMA20 그리고 종가 > EMA26; 조건 미충족; OBV=5.91823e+07, OBV_SMA20=5.93103e+07, close=529.54, EMA26=531.788 |
| v1 | stochastic_14_3_recovery | 9731.13 | -268.87 | sell /  / 직전 %K14 < 20에서 %K14가 %D3 상향 돌파 (한 봉 목표); 조건 미충족; K14=35.5998, D3=27.8717, previous_K14=31.4616, previous_D3=23.8817 |
| v1 | mfi_14_recovery | 9972.58 | -27.42 | sell /  / 직전 MFI14 < 20, 현재 MFI14 >= 20 (한 봉 목표); 조건 미충족; MFI14=53.413, previous_MFI14=44.3372 |
| v1 | adx_14_trend | 9883.62 | -116.38 | sell /  / Wilder ADX14 >= 25 그리고 +DI14 > -DI14; 조건 미충족; ADX14=23.6824, plus_DI14=22.3066, minus_DI14=19.9214 |
| v1 | aroon_25_trend | 9616.60 | -383.40 | sell /  / Aroon25 Up > 70 그리고 Down < 30 (동률이면 최신 극값); 조건 미충족; Aroon_up=96, Aroon_down=100 |
| v1 | cci_20_momentum | 9912.64 | -87.36 | sell /  / CCI20 > 100 (전형가격·평균절대편차); 조건 미충족; CCI20=96.8192 |
| v1 | williams_14_recovery | 9670.32 | -329.68 | sell /  / 직전 Williams %R14 < -80, 현재 >= -80 (한 봉 목표); 조건 미충족; Williams_R14=-64.4002, previous_R14=-68.5384 |
| v1 | cmf_20_accumulation | 9579.01 | -420.99 | sell /  / Chaikin Money Flow20 > 0.1; 조건 미충족; CMF20=-0.038027, volume20=2.32417e+07 |
| v1 | chaikin_3_10 | 9575.46 | -424.54 | sell /  / ADL의 EMA3 - EMA10 > 0 그리고 종가 > EMA26; 조건 미충족; Chaikin3_10=-50549, ADL=1.1482e+08, close=529.54, EMA26=531.788 |
| v1 | roc_10_momentum | 9959.43 | -40.57 | sell /  / 10봉 ROC > 1% 그리고 종가 > EMA26; 조건 미충족; ROC10_percent=0.454191, close=534.125, EMA26=532.186 |
| v1 | trix_15_trend | 9557.09 | -442.91 | sell /  / 15봉 삼중 EMA의 1봉 변화율 TRIX > 0 그리고 종가 > EMA26; 조건 미충족; TRIX15_percent=0.00481299, close=529.54, EMA26=531.788 |
| v1 | keltner_20_breakout | 9958.78 | -41.22 | sell /  / 종가 > EMA20 + 2 x Wilder ATR14; 조건 미충족; close=533.975, upper_Keltner=534.357, EMA20=530.111, ATR14=2.12332 |
| v1 | opening_range_30m | 9589.30 | -410.70 | sell /  / 뉴욕 09:30·09:45 두 완료 봉 최고가를 10:00 이후 종가가 돌파; 자료 부족·변동폭 또는 거래량 없음: 대기; close=529.54 |
| v2 | cash | 10000.00 | 0.00 | 대기 /  / 새 신호 대기 |
| v2 | buy_hold | 9745.17 | -254.83 | buy / partial / 직전 완료 봉 목표 비중 100%; 다음 봉 시가 가정 |
| v2 | trend_8_26 | 9366.79 | -633.21 | sell / filled / 직전 완료 봉 목표 비중 0%; 다음 봉 시가 가정 |
| v2 | momentum_26 | 9327.21 | -672.79 | sell / filled / 직전 완료 봉 목표 비중 0%; 다음 봉 시가 가정 |
| v2 | breakout_8 | 9298.81 | -701.19 | sell / filled / 직전 완료 봉 목표 비중 0%; 다음 봉 시가 가정 |
| v2 | reversion_12 | 9055.49 | -944.51 | sell / filled / 직전 완료 봉 목표 비중 0%; 다음 봉 시가 가정 |
| v2 | volume_26 | 9304.84 | -695.16 | sell / filled / 직전 완료 봉 목표 비중 0%; 다음 봉 시가 가정 |
| v2 | trend_8_26 AND momentum_26 | 9320.43 | -679.57 | sell / filled / 직전 완료 봉 목표 비중 0%; 다음 봉 시가 가정 |
| v2 | trend_8_26 + momentum_26 | 9386.57 | -613.43 | sell / filled / 직전 완료 봉 목표 비중 0%; 다음 봉 시가 가정 |
| v2 | trend_8_26 AND breakout_8 | 9318.21 | -681.79 | sell / filled / 직전 완료 봉 목표 비중 0%; 다음 봉 시가 가정 |
| v2 | trend_8_26 + breakout_8 | 9392.14 | -607.86 | sell / filled / 직전 완료 봉 목표 비중 0%; 다음 봉 시가 가정 |
| v2 | trend_8_26 AND reversion_12 | 9411.07 | -588.93 | sell / filled / 직전 완료 봉 목표 비중 0%; 다음 봉 시가 가정 |
| v2 | trend_8_26 + reversion_12 | 9228.75 | -771.25 | sell / filled / 직전 완료 봉 목표 비중 0%; 다음 봉 시가 가정 |
| v2 | trend_8_26 AND volume_26 | 9743.99 | -256.01 | sell / filled / 직전 완료 봉 목표 비중 0%; 다음 봉 시가 가정 |
| v2 | trend_8_26 + volume_26 | 9355.31 | -644.69 | sell / filled / 직전 완료 봉 목표 비중 0%; 다음 봉 시가 가정 |
| v2 | momentum_26 AND breakout_8 | 9430.77 | -569.23 | sell / filled / 직전 완료 봉 목표 비중 0%; 다음 봉 시가 가정 |
| v2 | momentum_26 + breakout_8 | 9332.85 | -667.15 | sell / filled / 직전 완료 봉 목표 비중 0%; 다음 봉 시가 가정 |
| v2 | momentum_26 AND reversion_12 | 9475.12 | -524.88 | sell / filled / 직전 완료 봉 목표 비중 0%; 다음 봉 시가 가정 |
| v2 | momentum_26 + reversion_12 | 9248.07 | -751.93 | sell / filled / 직전 완료 봉 목표 비중 0%; 다음 봉 시가 가정 |
| v2 | momentum_26 AND volume_26 | 9695.84 | -304.16 | sell / filled / 직전 완료 봉 목표 비중 0%; 다음 봉 시가 가정 |
| v2 | momentum_26 + volume_26 | 9355.39 | -644.61 | sell / filled / 직전 완료 봉 목표 비중 0%; 다음 봉 시가 가정 |
| v2 | breakout_8 AND reversion_12 | 10000.00 | 0.00 | 대기 /  / 새 신호 대기 |
| v2 | breakout_8 + reversion_12 | 9233.90 | -766.10 | sell / filled / 직전 완료 봉 목표 비중 0%; 다음 봉 시가 가정 |
| v2 | breakout_8 AND volume_26 | 9890.09 | -109.91 | sell / filled / 직전 완료 봉 목표 비중 0%; 다음 봉 시가 가정 |
| v2 | breakout_8 + volume_26 | 9360.45 | -639.55 | sell / filled / 직전 완료 봉 목표 비중 0%; 다음 봉 시가 가정 |
| v2 | reversion_12 AND volume_26 | 9528.36 | -471.64 | sell / filled / 직전 완료 봉 목표 비중 0%; 다음 봉 시가 가정 |
| v2 | reversion_12 + volume_26 | 9198.36 | -801.64 | sell / filled / 직전 완료 봉 목표 비중 0%; 다음 봉 시가 가정 |
| v2 | ema_12_26 | 9483.83 | -516.17 | sell / filled / EMA12 > EMA26; 조건 미충족; EMA12=531.766, EMA26=531.788; 직전 완료 봉 목표를 다음 봉 시가에 모의 적용 |
| v2 | macd_12_26_9 | 9594.34 | -405.66 | sell / filled / MACD > 신호선 그리고 MACD > 0; 조건 미충족; MACD=-0.0222122, signal9=0.149678; 직전 완료 봉 목표를 다음 봉 시가에 모의 적용 |
| v2 | rsi_14_recovery | 9924.16 | -75.84 | sell / filled / 직전 RSI14 < 30, 현재 RSI14 >= 30 (한 봉 목표); 조건 미충족; RSI14=39.2066, previous_RSI14=35.1952; 직전 완료 봉 목표를 다음 봉 시가에 모의 적용 |
| v2 | bollinger_20_reentry | 9779.33 | -220.67 | sell / filled / 직전 종가 < 직전 하단밴드, 현재 하단밴드 <= 종가 <= SMA20 (한 봉 목표); 조건 미충족; close=526.675, lower20=523.276, SMA20=530.073, previous_lower20=523.675; 직전 완료 봉 목표를 다음 봉 시가에 모의 적용 |
| v2 | donchian_20 | 9908.19 | -91.81 | sell / filled / 종가 > 현재 봉을 제외한 직전 20봉 최고가; 조건 미충족; close=534.52, prior_high20=535.44; 직전 완료 봉 목표를 다음 봉 시가에 모의 적용 |
| v2 | atr_14_breakout | 9911.14 | -88.86 | sell / filled / 종가 > 직전 종가 + 직전 ATR14 그리고 종가 > EMA26; 조건 미충족; close=533.975, threshold=536.307, prior_ATR14=2.16203, EMA26=530.521; 직전 완료 봉 목표를 다음 봉 시가에 모의 적용 |
| v2 | session_vwap | 9625.93 | -374.07 | sell / filled / 종가 > 뉴욕 거래일별 누적 전형가격 VWAP; 조건 미충족; close=524.76, session_VWAP=524.823, session_volume=2.14412e+07; 직전 완료 봉 목표를 다음 봉 시가에 모의 적용 |
| v2 | obv_20 | 9520.36 | -479.64 | sell / filled / OBV > OBV의 SMA20 그리고 종가 > EMA26; 조건 미충족; OBV=5.91823e+07, OBV_SMA20=5.93103e+07, close=529.54, EMA26=531.788; 직전 완료 봉 목표를 다음 봉 시가에 모의 적용 |
| v2 | stochastic_14_3_recovery | 9715.58 | -284.42 | sell / filled / 직전 %K14 < 20에서 %K14가 %D3 상향 돌파 (한 봉 목표); 조건 미충족; K14=35.5998, D3=27.8717, previous_K14=31.4616, previous_D3=23.8817; 직전 완료 봉 목표를 다음 봉 시가에 모의 적용 |
| v2 | mfi_14_recovery | 9968.59 | -31.41 | sell / filled / 직전 MFI14 < 20, 현재 MFI14 >= 20 (한 봉 목표); 조건 미충족; MFI14=53.413, previous_MFI14=44.3372; 직전 완료 봉 목표를 다음 봉 시가에 모의 적용 |
| v2 | adx_14_trend | 9879.67 | -120.33 | sell / filled / Wilder ADX14 >= 25 그리고 +DI14 > -DI14; 조건 미충족; ADX14=23.6824, plus_DI14=22.3066, minus_DI14=19.9214; 직전 완료 봉 목표를 다음 봉 시가에 모의 적용 |
| v2 | aroon_25_trend | 9608.91 | -391.09 | sell / filled / Aroon25 Up > 70 그리고 Down < 30 (동률이면 최신 극값); 조건 미충족; Aroon_up=96, Aroon_down=100; 직전 완료 봉 목표를 다음 봉 시가에 모의 적용 |
| v2 | cci_20_momentum | 9906.70 | -93.30 | sell / filled / CCI20 > 100 (전형가격·평균절대편차); 조건 미충족; CCI20=96.8192; 직전 완료 봉 목표를 다음 봉 시가에 모의 적용 |
| v2 | williams_14_recovery | 9654.86 | -345.14 | sell / filled / 직전 Williams %R14 < -80, 현재 >= -80 (한 봉 목표); 조건 미충족; Williams_R14=-64.4002, previous_R14=-68.5384; 직전 완료 봉 목표를 다음 봉 시가에 모의 적용 |
| v2 | cmf_20_accumulation | 9569.43 | -430.57 | sell / filled / Chaikin Money Flow20 > 0.1; 조건 미충족; CMF20=-0.038027, volume20=2.32417e+07; 직전 완료 봉 목표를 다음 봉 시가에 모의 적용 |
| v2 | chaikin_3_10 | 9560.15 | -439.85 | sell / filled / ADL의 EMA3 - EMA10 > 0 그리고 종가 > EMA26; 조건 미충족; Chaikin3_10=-50549, ADL=1.1482e+08, close=529.54, EMA26=531.788; 직전 완료 봉 목표를 다음 봉 시가에 모의 적용 |
| v2 | roc_10_momentum | 9957.44 | -42.56 | sell / filled / 10봉 ROC > 1% 그리고 종가 > EMA26; 조건 미충족; ROC10_percent=0.454191, close=534.125, EMA26=532.186; 직전 완료 봉 목표를 다음 봉 시가에 모의 적용 |
| v2 | trix_15_trend | 9549.45 | -450.55 | sell / filled / 15봉 삼중 EMA의 1봉 변화율 TRIX > 0 그리고 종가 > EMA26; 조건 미충족; TRIX15_percent=0.00481299, close=529.54, EMA26=531.788; 직전 완료 봉 목표를 다음 봉 시가에 모의 적용 |
| v2 | keltner_20_breakout | 9956.78 | -43.22 | sell / filled / 종가 > EMA20 + 2 x Wilder ATR14; 조건 미충족; close=533.975, upper_Keltner=534.357, EMA20=530.111, ATR14=2.12332; 직전 완료 봉 목표를 다음 봉 시가에 모의 적용 |
| v2 | opening_range_30m | 9581.64 | -418.36 | sell / filled / 뉴욕 09:30·09:45 두 완료 봉 최고가를 10:00 이후 종가가 돌파; 자료 부족·변동폭 또는 거래량 없음: 대기; close=529.54; 직전 완료 봉 목표를 다음 봉 시가에 모의 적용 |

### 같은 기간의 비용·노출 비교 (사후 연구)

| 전략 | 비용 전 | 비용 후 | 100% 보유 | 같은 평균 노출 보유 | 평균 노출 |
|---|---:|---:|---:|---:|---:|
| cash | 0.00% | 0.00% | 1.38% | 0.00% | 0.00% |
| buy_hold | 1.81% | 1.38% | 1.38% | 1.38% | 100.00% |
| trend_8_26 | -2.36% | -5.98% | 1.38% | 0.80% | 58.53% |
| momentum_26 | -1.02% | -8.23% | 1.38% | 0.78% | 56.96% |
| breakout_8 | 5.86% | -8.61% | 1.38% | 0.27% | 20.21% |
| reversion_12 | -5.45% | -14.15% | 1.38% | 0.34% | 24.93% |
| volume_26 | 0.86% | -8.43% | 1.38% | 0.12% | 9.19% |
| trend_8_26 AND momentum_26 | -2.66% | -8.98% | 1.38% | 0.69% | 50.66% |
| trend_8_26 + momentum_26 | -1.69% | -6.71% | 1.38% | 0.79% | 57.75% |
| trend_8_26 AND breakout_8 | -0.15% | -10.48% | 1.38% | 0.17% | 12.60% |
| trend_8_26 + breakout_8 | 1.68% | -6.71% | 1.38% | 0.54% | 39.38% |
| trend_8_26 AND reversion_12 | -2.62% | -8.95% | 1.38% | 0.10% | 7.61% |
| trend_8_26 + reversion_12 | -3.90% | -9.78% | 1.38% | 0.57% | 41.74% |
| trend_8_26 AND volume_26 | 2.03% | -1.75% | 1.38% | 0.04% | 3.15% |
| trend_8_26 + volume_26 | -0.75% | -6.82% | 1.38% | 0.46% | 33.86% |
| momentum_26 AND breakout_8 | 2.14% | -8.81% | 1.38% | 0.18% | 13.12% |
| momentum_26 + breakout_8 | 2.37% | -7.84% | 1.38% | 0.53% | 38.59% |
| momentum_26 AND reversion_12 | -3.22% | -9.51% | 1.38% | 0.12% | 9.19% |
| momentum_26 + reversion_12 | -3.24% | -10.68% | 1.38% | 0.56% | 40.95% |
| momentum_26 AND volume_26 | 1.17% | -3.40% | 1.38% | 0.05% | 3.41% |
| momentum_26 + volume_26 | -0.07% | -7.75% | 1.38% | 0.45% | 33.08% |
| breakout_8 AND reversion_12 | 0.00% | 0.00% | 1.38% | 0.00% | 0.00% |
| breakout_8 + reversion_12 | 0.07% | -10.49% | 1.38% | 0.31% | 22.58% |
| breakout_8 AND volume_26 | 2.04% | -0.50% | 1.38% | 0.02% | 1.84% |
| breakout_8 + volume_26 | 3.34% | -7.75% | 1.38% | 0.20% | 14.71% |
| reversion_12 AND volume_26 | -2.90% | -7.29% | 1.38% | 0.06% | 4.20% |
| reversion_12 + volume_26 | -2.33% | -11.15% | 1.38% | 0.23% | 17.07% |
| ema_12_26 | -1.46% | -5.11% | 1.38% | 0.79% | 57.74% |
| macd_12_26_9 | -1.32% | -6.95% | 1.38% | 0.47% | 34.65% |
| rsi_14_recovery | 0.46% | -2.45% | 1.38% | 0.02% | 1.84% |
| bollinger_20_reentry | -0.59% | -3.87% | 1.38% | 0.03% | 2.10% |
| donchian_20 | 1.05% | -4.32% | 1.38% | 0.06% | 4.20% |
| atr_14_breakout | 1.62% | -2.97% | 1.38% | 0.04% | 3.15% |
| session_vwap | 4.86% | -3.59% | 1.38% | 0.64% | 46.72% |
| obv_20 | 4.63% | -4.60% | 1.38% | 0.70% | 51.18% |
| stochastic_14_3_recovery | -0.02% | -9.61% | 1.38% | 0.08% | 6.30% |
| mfi_14_recovery | 1.84% | -1.53% | 1.38% | 0.03% | 2.10% |
| adx_14_trend | 4.03% | 1.87% | 1.38% | 0.59% | 43.57% |
| aroon_25_trend | -1.70% | -6.53% | 1.38% | 0.31% | 23.10% |
| cci_20_momentum | 2.85% | -3.43% | 1.38% | 0.28% | 21.00% |
| williams_14_recovery | -1.14% | -9.87% | 1.38% | 0.08% | 5.77% |
| cmf_20_accumulation | 0.22% | -6.30% | 1.38% | 0.58% | 42.26% |
| chaikin_3_10 | 3.55% | -4.80% | 1.38% | 0.67% | 49.34% |
| roc_10_momentum | -0.61% | -4.30% | 1.38% | 0.18% | 13.12% |
| trix_15_trend | -1.48% | -5.53% | 1.38% | 0.60% | 44.36% |
| keltner_20_breakout | 0.49% | -4.45% | 1.38% | 0.16% | 11.55% |
| opening_range_30m | -1.39% | -5.05% | 1.38% | 0.28% | 20.73% |

동일 구간·초기 자금, 종료 시 청산 비용 포함. 노출 맞춤은 사후 설명용이며 v2 실제 계좌 성과가 아닙니다.
[낙폭 분해·비용 영향·전체 구간](MSFT/comparison.json)

[v1 전체 기록](MSFT/accounts.json) · [v2 전체 기록](MSFT/accounts-v2.json)

## JPM 계좌

| 모델 | 전략 | 평가액 USD | 손익 USD | 최근 매매·이유 |
|---|---|---:|---:|---|
| v1 | cash | 10000.00 | 0.00 | 대기 /  / 새 신호 대기 |
| v1 | buy_hold | 9830.00 | -170.00 | buy /  / buy_hold: prior completed bar target 100%; next bar open simulation |
| v1 | trend_8_26 | 9709.94 | -290.06 | sell /  / trend_8_26: prior completed bar target 0%; next bar open simulation |
| v1 | momentum_26 | 9437.37 | -562.63 | buy /  / momentum_26: prior completed bar target 100%; next bar open simulation |
| v1 | breakout_8 | 9582.11 | -417.89 | sell /  / breakout_8: prior completed bar target 0%; next bar open simulation |
| v1 | reversion_12 | 9549.62 | -450.38 | sell /  / reversion_12: prior completed bar target 0%; next bar open simulation |
| v1 | volume_26 | 9920.77 | -79.23 | sell /  / volume_26: prior completed bar target 0%; next bar open simulation |
| v1 | trend_8_26 AND momentum_26 | 9591.12 | -408.88 | sell /  / trend_8_26 AND momentum_26: prior completed bar target 0%; next bar open simulation |
| v1 | trend_8_26 + momentum_26 | 9572.78 | -427.22 | buy /  / trend_8_26 + momentum_26: prior completed bar target 50%; next bar open simulation |
| v1 | trend_8_26 AND breakout_8 | 9808.13 | -191.87 | sell /  / trend_8_26 AND breakout_8: prior completed bar target 0%; next bar open simulation |
| v1 | trend_8_26 + breakout_8 | 9684.52 | -315.48 | sell /  / trend_8_26 + breakout_8: prior completed bar target 0%; next bar open simulation |
| v1 | trend_8_26 AND reversion_12 | 9757.16 | -242.84 | sell /  / trend_8_26 AND reversion_12: prior completed bar target 0%; next bar open simulation |
| v1 | trend_8_26 + reversion_12 | 9629.33 | -370.67 | sell /  / trend_8_26 + reversion_12: prior completed bar target 0%; next bar open simulation |
| v1 | trend_8_26 AND volume_26 | 10103.61 | 103.61 | sell /  / trend_8_26 AND volume_26: prior completed bar target 0%; next bar open simulation |
| v1 | trend_8_26 + volume_26 | 9814.64 | -185.36 | sell /  / trend_8_26 + volume_26: prior completed bar target 0%; next bar open simulation |
| v1 | momentum_26 AND breakout_8 | 9597.01 | -402.99 | sell /  / momentum_26 AND breakout_8: prior completed bar target 0%; next bar open simulation |
| v1 | momentum_26 + breakout_8 | 9509.57 | -490.43 | buy /  / momentum_26 + breakout_8: prior completed bar target 50%; next bar open simulation |
| v1 | momentum_26 AND reversion_12 | 9788.16 | -211.84 | sell /  / momentum_26 AND reversion_12: prior completed bar target 0%; next bar open simulation |
| v1 | momentum_26 + reversion_12 | 9588.57 | -411.43 | buy /  / momentum_26 + reversion_12: prior completed bar target 50%; next bar open simulation |
| v1 | momentum_26 AND volume_26 | 9926.98 | -73.02 | sell /  / momentum_26 AND volume_26: prior completed bar target 0%; next bar open simulation |
| v1 | momentum_26 + volume_26 | 9714.77 | -285.23 | buy /  / momentum_26 + volume_26: prior completed bar target 50%; next bar open simulation |
| v1 | breakout_8 AND reversion_12 | 10000.00 | 0.00 | 대기 /  / 새 신호 대기 |
| v1 | breakout_8 + reversion_12 | 9604.00 | -396.00 | sell /  / breakout_8 + reversion_12: prior completed bar target 0%; next bar open simulation |
| v1 | breakout_8 AND volume_26 | 10054.69 | 54.69 | sell /  / breakout_8 AND volume_26: prior completed bar target 0%; next bar open simulation |
| v1 | breakout_8 + volume_26 | 9769.49 | -230.51 | sell /  / breakout_8 + volume_26: prior completed bar target 0%; next bar open simulation |
| v1 | reversion_12 AND volume_26 | 9940.10 | -59.90 | sell /  / reversion_12 AND volume_26: prior completed bar target 0%; next bar open simulation |
| v1 | reversion_12 + volume_26 | 9772.29 | -227.71 | sell /  / reversion_12 + volume_26: prior completed bar target 0%; next bar open simulation |
| v1 | ema_12_26 | 9641.25 | -358.75 | sell /  / EMA12 > EMA26; 조건 미충족; EMA12=334.549, EMA26=334.619 |
| v1 | macd_12_26_9 | 9723.96 | -276.04 | sell /  / MACD > 신호선 그리고 MACD > 0; 조건 미충족; MACD=-0.0706145, signal9=0.000366165 |
| v1 | rsi_14_recovery | 9986.37 | -13.63 | sell /  / 직전 RSI14 < 30, 현재 RSI14 >= 30 (한 봉 목표); 조건 미충족; RSI14=61.6663, previous_RSI14=57.046 |
| v1 | bollinger_20_reentry | 9848.44 | -151.56 | sell /  / 직전 종가 < 직전 하단밴드, 현재 하단밴드 <= 종가 <= SMA20 (한 봉 목표); 조건 미충족; close=334.49, lower20=332.961, SMA20=334.508, previous_lower20=332.957 |
| v1 | donchian_20 | 9792.78 | -207.22 | sell /  / 종가 > 현재 봉을 제외한 직전 20봉 최고가; 조건 미충족; close=335.915, prior_high20=336.169 |
| v1 | atr_14_breakout | 9691.73 | -308.27 | sell /  / 종가 > 직전 종가 + 직전 ATR14 그리고 종가 > EMA26; 조건 미충족; close=335.21, threshold=335.598, prior_ATR14=1.10843, EMA26=334.445 |
| v1 | session_vwap | 9636.54 | -363.46 | buy /  / 종가 > 뉴욕 거래일별 누적 전형가격 VWAP; 조건 충족; close=334.49, session_VWAP=334.279, session_volume=1.55816e+06 |
| v1 | obv_20 | 9824.32 | -175.68 | sell /  / OBV > OBV의 SMA20 그리고 종가 > EMA26; 조건 미충족; OBV=-2.02195e+07, OBV_SMA20=-2.0213e+07, close=334.65, EMA26=334.509 |
| v1 | stochastic_14_3_recovery | 9574.52 | -425.48 | sell /  / 직전 %K14 < 20에서 %K14가 %D3 상향 돌파 (한 봉 목표); 조건 미충족; K14=53.9297, D3=28.1336, previous_K14=24.5463, previous_D3=18.2988 |
| v1 | mfi_14_recovery | 9935.64 | -64.36 | sell /  / 직전 MFI14 < 20, 현재 MFI14 >= 20 (한 봉 목표); 조건 미충족; MFI14=30.2719, previous_MFI14=26.8492 |
| v1 | adx_14_trend | 9726.68 | -273.32 | sell /  / Wilder ADX14 >= 25 그리고 +DI14 > -DI14; 조건 미충족; ADX14=23.9395, plus_DI14=23.2021, minus_DI14=22.594 |
| v1 | aroon_25_trend | 9824.71 | -175.29 | sell /  / Aroon25 Up > 70 그리고 Down < 30 (동률이면 최신 극값); 조건 미충족; Aroon_up=68, Aroon_down=16 |
| v1 | cci_20_momentum | 9810.74 | -189.26 | sell /  / CCI20 > 100 (전형가격·평균절대편차); 조건 미충족; CCI20=57.5465 |
| v1 | williams_14_recovery | 9567.46 | -432.54 | sell /  / 직전 Williams %R14 < -80, 현재 >= -80 (한 봉 목표); 조건 미충족; Williams_R14=-46.0703, previous_R14=-75.4537 |
| v1 | cmf_20_accumulation | 9803.03 | -196.97 | buy /  / Chaikin Money Flow20 > 0.1; 조건 충족; CMF20=0.131084, volume20=2.22061e+06 |
| v1 | chaikin_3_10 | 9752.44 | -247.56 | buy /  / ADL의 EMA3 - EMA10 > 0 그리고 종가 > EMA26; 조건 충족; Chaikin3_10=101858, ADL=-9.7555e+06, close=334.49, EMA26=334.383 |
| v1 | roc_10_momentum | 9836.40 | -163.60 | sell /  / 10봉 ROC > 1% 그리고 종가 > EMA26; 조건 미충족; ROC10_percent=0.964142, close=337.72, EMA26=336.695 |
| v1 | trix_15_trend | 9723.73 | -276.27 | sell /  / 15봉 삼중 EMA의 1봉 변화율 TRIX > 0 그리고 종가 > EMA26; 조건 미충족; TRIX15_percent=0.0135144, close=337.6, EMA26=338.759 |
| v1 | keltner_20_breakout | 9905.24 | -94.76 | sell /  / 종가 > EMA20 + 2 x Wilder ATR14; 조건 미충족; close=339.04, upper_Keltner=339.281, EMA20=336.559, ATR14=1.36146 |
| v1 | opening_range_30m | 9850.26 | -149.74 | sell /  / 뉴욕 09:30·09:45 두 완료 봉 최고가를 10:00 이후 종가가 돌파; 조건 미충족; close=337.72, opening_high=339.035 |
| v2 | cash | 10000.00 | 0.00 | 대기 /  / 새 신호 대기 |
| v2 | buy_hold | 9994.26 | -5.74 | buy / partial / 직전 완료 봉 목표 비중 100%; 다음 봉 시가 가정 |
| v2 | trend_8_26 | 9713.03 | -286.97 | sell / filled / 직전 완료 봉 목표 비중 0%; 다음 봉 시가 가정 |
| v2 | momentum_26 | 9135.38 | -864.62 | 중단: 손실 한도 / buy / partial / 직전 완료 봉 목표 비중 100%; 다음 봉 시가 가정 |
| v2 | breakout_8 | 9004.26 | -995.74 | 중단: 손실 한도 / buy / partial / 직전 완료 봉 목표 비중 100%; 다음 봉 시가 가정 |
| v2 | reversion_12 | 9515.28 | -484.72 | sell / filled / 직전 완료 봉 목표 비중 0%; 다음 봉 시가 가정 |
| v2 | volume_26 | 9737.15 | -262.85 | sell / filled / 직전 완료 봉 목표 비중 0%; 다음 봉 시가 가정 |
| v2 | trend_8_26 AND momentum_26 | 9549.07 | -450.93 | sell / filled / 직전 완료 봉 목표 비중 0%; 다음 봉 시가 가정 |
| v2 | trend_8_26 + momentum_26 | 9346.80 | -653.20 | buy / filled / 직전 완료 봉 목표 비중 50%; 다음 봉 시가 가정 |
| v2 | trend_8_26 AND breakout_8 | 9181.63 | -818.37 | sell / filled / 직전 완료 봉 목표 비중 0%; 다음 봉 시가 가정 |
| v2 | trend_8_26 + breakout_8 | 9351.36 | -648.64 | sell / filled / 직전 완료 봉 목표 비중 0%; 다음 봉 시가 가정 |
| v2 | trend_8_26 AND reversion_12 | 9729.48 | -270.52 | sell / filled / 직전 완료 봉 목표 비중 0%; 다음 봉 시가 가정 |
| v2 | trend_8_26 + reversion_12 | 9654.17 | -345.83 | sell / filled / 직전 완료 봉 목표 비중 0%; 다음 봉 시가 가정 |
| v2 | trend_8_26 AND volume_26 | 9897.88 | -102.12 | sell / filled / 직전 완료 봉 목표 비중 0%; 다음 봉 시가 가정 |
| v2 | trend_8_26 + volume_26 | 9725.74 | -274.26 | sell / filled / 직전 완료 봉 목표 비중 0%; 다음 봉 시가 가정 |
| v2 | momentum_26 AND breakout_8 | 8956.38 | -1043.62 | 중단: 손실 한도 / buy / partial / 직전 완료 봉 목표 비중 100%; 다음 봉 시가 가정 |
| v2 | momentum_26 + breakout_8 | 8995.36 | -1004.64 | 중단: 손실 한도 / sell / filled / 직전 완료 봉 목표 비중 0%; 다음 봉 시가 가정 |
| v2 | momentum_26 AND reversion_12 | 9730.22 | -269.78 | sell / filled / 직전 완료 봉 목표 비중 0%; 다음 봉 시가 가정 |
| v2 | momentum_26 + reversion_12 | 9447.24 | -552.76 | buy / filled / 직전 완료 봉 목표 비중 50%; 다음 봉 시가 가정 |
| v2 | momentum_26 AND volume_26 | 9724.84 | -275.16 | sell / filled / 직전 완료 봉 목표 비중 0%; 다음 봉 시가 가정 |
| v2 | momentum_26 + volume_26 | 9437.88 | -562.12 | buy / filled / 직전 완료 봉 목표 비중 50%; 다음 봉 시가 가정 |
| v2 | breakout_8 AND reversion_12 | 10000.00 | 0.00 | 대기 /  / 새 신호 대기 |
| v2 | breakout_8 + reversion_12 | 9293.56 | -706.44 | sell / filled / 직전 완료 봉 목표 비중 0%; 다음 봉 시가 가정 |
| v2 | breakout_8 AND volume_26 | 9941.48 | -58.52 | sell / filled / 직전 완료 봉 목표 비중 0%; 다음 봉 시가 가정 |
| v2 | breakout_8 + volume_26 | 9362.03 | -637.97 | sell / filled / 직전 완료 봉 목표 비중 0%; 다음 봉 시가 가정 |
| v2 | reversion_12 AND volume_26 | 9987.18 | -12.82 | sell / filled / 직전 완료 봉 목표 비중 0%; 다음 봉 시가 가정 |
| v2 | reversion_12 + volume_26 | 9686.50 | -313.50 | sell / filled / 직전 완료 봉 목표 비중 0%; 다음 봉 시가 가정 |
| v2 | ema_12_26 | 9635.47 | -364.53 | sell / filled / EMA12 > EMA26; 조건 미충족; EMA12=334.549, EMA26=334.619; 직전 완료 봉 목표를 다음 봉 시가에 모의 적용 |
| v2 | macd_12_26_9 | 9718.13 | -281.87 | sell / filled / MACD > 신호선 그리고 MACD > 0; 조건 미충족; MACD=-0.0706145, signal9=0.000366165; 직전 완료 봉 목표를 다음 봉 시가에 모의 적용 |
| v2 | rsi_14_recovery | 9984.37 | -15.63 | sell / filled / 직전 RSI14 < 30, 현재 RSI14 >= 30 (한 봉 목표); 조건 미충족; RSI14=61.6663, previous_RSI14=57.046; 직전 완료 봉 목표를 다음 봉 시가에 모의 적용 |
| v2 | bollinger_20_reentry | 9840.57 | -159.43 | sell / filled / 직전 종가 < 직전 하단밴드, 현재 하단밴드 <= 종가 <= SMA20 (한 봉 목표); 조건 미충족; close=334.49, lower20=332.961, SMA20=334.508, previous_lower20=332.957; 직전 완료 봉 목표를 다음 봉 시가에 모의 적용 |
| v2 | donchian_20 | 9784.95 | -215.05 | sell / filled / 종가 > 현재 봉을 제외한 직전 20봉 최고가; 조건 미충족; close=335.915, prior_high20=336.169; 직전 완료 봉 목표를 다음 봉 시가에 모의 적용 |
| v2 | atr_14_breakout | 9678.18 | -321.82 | sell / filled / 종가 > 직전 종가 + 직전 ATR14 그리고 종가 > EMA26; 조건 미충족; close=335.21, threshold=335.598, prior_ATR14=1.10843, EMA26=334.445; 직전 완료 봉 목표를 다음 봉 시가에 모의 적용 |
| v2 | session_vwap | 9622.10 | -377.90 | buy / partial / 종가 > 뉴욕 거래일별 누적 전형가격 VWAP; 조건 충족; close=334.49, session_VWAP=334.279, session_volume=1.55816e+06; 직전 완료 봉 목표를 다음 봉 시가에 모의 적용 |
| v2 | obv_20 | 9812.53 | -187.47 | sell / filled / OBV > OBV의 SMA20 그리고 종가 > EMA26; 조건 미충족; OBV=-2.02195e+07, OBV_SMA20=-2.0213e+07, close=334.65, EMA26=334.509; 직전 완료 봉 목표를 다음 봉 시가에 모의 적용 |
| v2 | stochastic_14_3_recovery | 9551.56 | -448.44 | sell / filled / 직전 %K14 < 20에서 %K14가 %D3 상향 돌파 (한 봉 목표); 조건 미충족; K14=53.9297, D3=28.1336, previous_K14=24.5463, previous_D3=18.2988; 직전 완료 봉 목표를 다음 봉 시가에 모의 적용 |
| v2 | mfi_14_recovery | 9931.66 | -68.34 | sell / filled / 직전 MFI14 < 20, 현재 MFI14 >= 20 (한 봉 목표); 조건 미충족; MFI14=30.2719, previous_MFI14=26.8492; 직전 완료 봉 목표를 다음 봉 시가에 모의 적용 |
| v2 | adx_14_trend | 9722.79 | -277.21 | sell / filled / Wilder ADX14 >= 25 그리고 +DI14 > -DI14; 조건 미충족; ADX14=23.9395, plus_DI14=23.2021, minus_DI14=22.594; 직전 완료 봉 목표를 다음 봉 시가에 모의 적용 |
| v2 | aroon_25_trend | 9822.74 | -177.26 | sell / filled / Aroon25 Up > 70 그리고 Down < 30 (동률이면 최신 극값); 조건 미충족; Aroon_up=68, Aroon_down=16; 직전 완료 봉 목표를 다음 봉 시가에 모의 적용 |
| v2 | cci_20_momentum | 9802.89 | -197.11 | sell / filled / CCI20 > 100 (전형가격·평균절대편차); 조건 미충족; CCI20=57.5465; 직전 완료 봉 목표를 다음 봉 시가에 모의 적용 |
| v2 | williams_14_recovery | 9546.43 | -453.57 | sell / filled / 직전 Williams %R14 < -80, 현재 >= -80 (한 봉 목표); 조건 미충족; Williams_R14=-46.0703, previous_R14=-75.4537; 직전 완료 봉 목표를 다음 봉 시가에 모의 적용 |
| v2 | cmf_20_accumulation | 9796.17 | -203.83 | buy / partial / Chaikin Money Flow20 > 0.1; 조건 충족; CMF20=0.131084, volume20=2.22061e+06; 직전 완료 봉 목표를 다음 봉 시가에 모의 적용 |
| v2 | chaikin_3_10 | 9739.77 | -260.23 | buy / partial / ADL의 EMA3 - EMA10 > 0 그리고 종가 > EMA26; 조건 충족; Chaikin3_10=101858, ADL=-9.7555e+06, close=334.49, EMA26=334.383; 직전 완료 봉 목표를 다음 봉 시가에 모의 적용 |
| v2 | roc_10_momentum | 9832.47 | -167.53 | sell / filled / 10봉 ROC > 1% 그리고 종가 > EMA26; 조건 미충족; ROC10_percent=0.964142, close=337.72, EMA26=336.695; 직전 완료 봉 목표를 다음 봉 시가에 모의 적용 |
| v2 | trix_15_trend | 9715.96 | -284.04 | sell / filled / 15봉 삼중 EMA의 1봉 변화율 TRIX > 0 그리고 종가 > EMA26; 조건 미충족; TRIX15_percent=0.0135144, close=337.6, EMA26=338.759; 직전 완료 봉 목표를 다음 봉 시가에 모의 적용 |
| v2 | keltner_20_breakout | 9901.28 | -98.72 | sell / filled / 종가 > EMA20 + 2 x Wilder ATR14; 조건 미충족; close=339.04, upper_Keltner=339.281, EMA20=336.559, ATR14=1.36146; 직전 완료 봉 목표를 다음 봉 시가에 모의 적용 |
| v2 | opening_range_30m | 9846.33 | -153.67 | sell / filled / 뉴욕 09:30·09:45 두 완료 봉 최고가를 10:00 이후 종가가 돌파; 조건 미충족; close=337.72, opening_high=339.035; 직전 완료 봉 목표를 다음 봉 시가에 모의 적용 |

### 같은 기간의 비용·노출 비교 (사후 연구)

| 전략 | 비용 전 | 비용 후 | 100% 보유 | 같은 평균 노출 보유 | 평균 노출 |
|---|---:|---:|---:|---:|---:|
| cash | 0.00% | 0.00% | 0.24% | 0.00% | 0.00% |
| buy_hold | 0.66% | 0.24% | 0.24% | 0.24% | 100.00% |
| trend_8_26 | -0.08% | -4.19% | 0.24% | 0.13% | 54.59% |
| momentum_26 | -3.83% | -12.32% | 0.24% | 0.13% | 54.07% |
| breakout_8 | -3.22% | -18.53% | 0.24% | 0.05% | 20.21% |
| reversion_12 | 7.20% | -8.23% | 0.24% | 0.06% | 23.62% |
| volume_26 | 1.38% | -5.21% | 0.24% | 0.02% | 6.56% |
| trend_8_26 AND momentum_26 | -0.12% | -5.83% | 0.24% | 0.10% | 41.99% |
| trend_8_26 + momentum_26 | -1.96% | -8.15% | 0.24% | 0.13% | 54.33% |
| trend_8_26 AND breakout_8 | -3.01% | -13.41% | 0.24% | 0.03% | 12.60% |
| trend_8_26 + breakout_8 | -1.64% | -11.08% | 0.24% | 0.09% | 37.41% |
| trend_8_26 AND reversion_12 | 2.60% | -4.47% | 0.24% | 0.02% | 8.14% |
| trend_8_26 + reversion_12 | 3.52% | -5.64% | 0.24% | 0.09% | 39.11% |
| trend_8_26 AND volume_26 | 0.71% | -3.03% | 0.24% | 0.01% | 4.20% |
| trend_8_26 + volume_26 | 0.67% | -4.69% | 0.24% | 0.07% | 30.58% |
| momentum_26 AND breakout_8 | -3.19% | -14.65% | 0.24% | 0.03% | 13.12% |
| momentum_26 + breakout_8 | -3.50% | -15.28% | 0.24% | 0.09% | 37.15% |
| momentum_26 AND reversion_12 | 2.63% | -5.24% | 0.24% | 0.02% | 7.35% |
| momentum_26 + reversion_12 | 1.56% | -8.01% | 0.24% | 0.09% | 38.85% |
| momentum_26 AND volume_26 | -0.48% | -3.77% | 0.24% | 0.01% | 3.15% |
| momentum_26 + volume_26 | -1.23% | -8.25% | 0.24% | 0.07% | 30.32% |
| breakout_8 AND reversion_12 | 0.00% | 0.00% | 0.24% | 0.00% | 0.00% |
| breakout_8 + reversion_12 | 1.88% | -12.25% | 0.24% | 0.05% | 21.93% |
| breakout_8 AND volume_26 | 0.48% | -2.02% | 0.24% | 0.00% | 1.57% |
| breakout_8 + volume_26 | -0.93% | -11.19% | 0.24% | 0.03% | 13.39% |
| reversion_12 AND volume_26 | 2.09% | -0.45% | 0.24% | 0.00% | 2.10% |
| reversion_12 + volume_26 | 4.26% | -5.55% | 0.24% | 0.04% | 15.10% |
| ema_12_26 | -1.13% | -4.80% | 0.24% | 0.12% | 51.71% |
| macd_12_26_9 | -1.02% | -5.88% | 0.24% | 0.08% | 32.55% |
| rsi_14_recovery | 0.40% | -0.86% | 0.24% | 0.00% | 0.79% |
| bollinger_20_reentry | 0.62% | -3.52% | 0.24% | 0.01% | 2.62% |
| donchian_20 | -1.80% | -5.44% | 0.24% | 0.01% | 3.41% |
| atr_14_breakout | -1.02% | -9.00% | 0.24% | 0.01% | 5.51% |
| session_vwap | 0.34% | -10.04% | 0.24% | 0.12% | 48.56% |
| obv_20 | -3.84% | -15.93% | 0.24% | 0.07% | 29.92% |
| stochastic_14_3_recovery | -0.15% | -10.48% | 0.24% | 0.02% | 6.82% |
| mfi_14_recovery | 0.12% | -1.13% | 0.24% | 0.00% | 0.79% |
| adx_14_trend | -2.56% | -4.99% | 0.24% | 0.06% | 27.03% |
| aroon_25_trend | -0.96% | -4.64% | 0.24% | 0.05% | 21.26% |
| cci_20_momentum | -3.44% | -11.96% | 0.24% | 0.04% | 17.06% |
| williams_14_recovery | -0.60% | -10.88% | 0.24% | 0.02% | 6.82% |
| cmf_20_accumulation | -2.23% | -11.23% | 0.24% | 0.08% | 34.91% |
| chaikin_3_10 | 0.96% | -9.10% | 0.24% | 0.08% | 34.65% |
| roc_10_momentum | -1.40% | -3.86% | 0.24% | 0.02% | 6.56% |
| trix_15_trend | -1.25% | -8.83% | 0.24% | 0.08% | 35.17% |
| keltner_20_breakout | -1.21% | -4.07% | 0.24% | 0.01% | 4.20% |
| opening_range_30m | -0.23% | -3.93% | 0.24% | 0.04% | 17.32% |

동일 구간·초기 자금, 종료 시 청산 비용 포함. 노출 맞춤은 사후 설명용이며 v2 실제 계좌 성과가 아닙니다.
[낙폭 분해·비용 영향·전체 구간](JPM/comparison.json)

[v1 전체 기록](JPM/accounts.json) · [v2 전체 기록](JPM/accounts-v2.json)

## XOM 계좌

| 모델 | 전략 | 평가액 USD | 손익 USD | 최근 매매·이유 |
|---|---|---:|---:|---|
| v1 | cash | 10000.00 | 0.00 | 대기 /  / 새 신호 대기 |
| v1 | buy_hold | 10018.20 | 18.20 | buy /  / buy_hold: prior completed bar target 100%; next bar open simulation |
| v1 | trend_8_26 | 9707.62 | -292.38 | sell /  / trend_8_26: prior completed bar target 0%; next bar open simulation |
| v1 | momentum_26 | 9812.01 | -187.99 | sell /  / momentum_26: prior completed bar target 0%; next bar open simulation |
| v1 | breakout_8 | 9488.17 | -511.83 | buy /  / breakout_8: prior completed bar target 100%; next bar open simulation |
| v1 | reversion_12 | 9541.48 | -458.52 | sell /  / reversion_12: prior completed bar target 0%; next bar open simulation |
| v1 | volume_26 | 9510.72 | -489.28 | sell /  / volume_26: prior completed bar target 0%; next bar open simulation |
| v1 | trend_8_26 AND momentum_26 | 9682.17 | -317.83 | sell /  / trend_8_26 AND momentum_26: prior completed bar target 0%; next bar open simulation |
| v1 | trend_8_26 + momentum_26 | 9759.82 | -240.18 | sell /  / trend_8_26 + momentum_26: prior completed bar target 0%; next bar open simulation |
| v1 | trend_8_26 AND breakout_8 | 9628.70 | -371.30 | sell /  / trend_8_26 AND breakout_8: prior completed bar target 0%; next bar open simulation |
| v1 | trend_8_26 + breakout_8 | 9617.02 | -382.98 | buy /  / trend_8_26 + breakout_8: prior completed bar target 50%; next bar open simulation |
| v1 | trend_8_26 AND reversion_12 | 9569.59 | -430.41 | sell /  / trend_8_26 AND reversion_12: prior completed bar target 0%; next bar open simulation |
| v1 | trend_8_26 + reversion_12 | 9624.28 | -375.72 | sell /  / trend_8_26 + reversion_12: prior completed bar target 0%; next bar open simulation |
| v1 | trend_8_26 AND volume_26 | 9624.99 | -375.01 | sell /  / trend_8_26 AND volume_26: prior completed bar target 0%; next bar open simulation |
| v1 | trend_8_26 + volume_26 | 9609.08 | -390.92 | sell /  / trend_8_26 + volume_26: prior completed bar target 0%; next bar open simulation |
| v1 | momentum_26 AND breakout_8 | 9724.23 | -275.77 | sell /  / momentum_26 AND breakout_8: prior completed bar target 0%; next bar open simulation |
| v1 | momentum_26 + breakout_8 | 9649.18 | -350.82 | buy /  / momentum_26 + breakout_8: prior completed bar target 50%; next bar open simulation |
| v1 | momentum_26 AND reversion_12 | 9667.08 | -332.92 | sell /  / momentum_26 AND reversion_12: prior completed bar target 0%; next bar open simulation |
| v1 | momentum_26 + reversion_12 | 9675.78 | -324.22 | sell /  / momentum_26 + reversion_12: prior completed bar target 0%; next bar open simulation |
| v1 | momentum_26 AND volume_26 | 9843.02 | -156.98 | sell /  / momentum_26 AND volume_26: prior completed bar target 0%; next bar open simulation |
| v1 | momentum_26 + volume_26 | 9660.41 | -339.59 | sell /  / momentum_26 + volume_26: prior completed bar target 0%; next bar open simulation |
| v1 | breakout_8 AND reversion_12 | 10000.00 | 0.00 | 대기 /  / 새 신호 대기 |
| v1 | breakout_8 + reversion_12 | 9533.75 | -466.25 | buy /  / breakout_8 + reversion_12: prior completed bar target 50%; next bar open simulation |
| v1 | breakout_8 AND volume_26 | 9851.05 | -148.95 | sell /  / breakout_8 AND volume_26: prior completed bar target 0%; next bar open simulation |
| v1 | breakout_8 + volume_26 | 9499.34 | -500.66 | buy /  / breakout_8 + volume_26: prior completed bar target 50%; next bar open simulation |
| v1 | reversion_12 AND volume_26 | 9794.27 | -205.73 | sell /  / reversion_12 AND volume_26: prior completed bar target 0%; next bar open simulation |
| v1 | reversion_12 + volume_26 | 9526.20 | -473.80 | sell /  / reversion_12 + volume_26: prior completed bar target 0%; next bar open simulation |
| v1 | ema_12_26 | 9780.43 | -219.57 | sell /  / EMA12 > EMA26; 조건 미충족; EMA12=177.479, EMA26=177.559 |
| v1 | macd_12_26_9 | 9819.68 | -180.32 | sell /  / MACD > 신호선 그리고 MACD > 0; 조건 미충족; MACD=0.15005, signal9=0.18271 |
| v1 | rsi_14_recovery | 9927.64 | -72.36 | sell /  / 직전 RSI14 < 30, 현재 RSI14 >= 30 (한 봉 목표); 조건 미충족; RSI14=37.639, previous_RSI14=31.1023 |
| v1 | bollinger_20_reentry | 9694.21 | -305.79 | sell /  / 직전 종가 < 직전 하단밴드, 현재 하단밴드 <= 종가 <= SMA20 (한 봉 목표); 조건 미충족; close=175.53, lower20=174.782, SMA20=177.101, previous_lower20=174.994 |
| v1 | donchian_20 | 9665.93 | -334.07 | sell /  / 종가 > 현재 봉을 제외한 직전 20봉 최고가; 조건 미충족; close=178.045, prior_high20=179.205 |
| v1 | atr_14_breakout | 9803.61 | -196.39 | sell /  / 종가 > 직전 종가 + 직전 ATR14 그리고 종가 > EMA26; 조건 미충족; close=178.95, threshold=179.19, prior_ATR14=0.519565, EMA26=177.678 |
| v1 | session_vwap | 9786.18 | -213.82 | buy /  / 종가 > 뉴욕 거래일별 누적 전형가격 VWAP; 조건 충족; close=176.86, session_VWAP=176.627, session_volume=3.72585e+06 |
| v1 | obv_20 | 9263.00 | -737.00 | buy /  / OBV > OBV의 SMA20 그리고 종가 > EMA26; 조건 충족; OBV=2.23431e+07, OBV_SMA20=2.157e+07, close=176.86, EMA26=176.75 |
| v1 | stochastic_14_3_recovery | 9636.26 | -363.74 | sell /  / 직전 %K14 < 20에서 %K14가 %D3 상향 돌파 (한 봉 목표); 조건 미충족; K14=11.8836, D3=5.65987, previous_K14=4.66302, previous_D3=2.02546 |
| v1 | mfi_14_recovery | 10000.00 | 0.00 | 대기 /  / 새 신호 대기 |
| v1 | adx_14_trend | 9999.47 | -0.53 | sell /  / Wilder ADX14 >= 25 그리고 +DI14 > -DI14; 조건 미충족; ADX14=23.8302, plus_DI14=25.6436, minus_DI14=22.6035 |
| v1 | aroon_25_trend | 9589.85 | -410.15 | sell /  / Aroon25 Up > 70 그리고 Down < 30 (동률이면 최신 극값); 조건 미충족; Aroon_up=96, Aroon_down=40 |
| v1 | cci_20_momentum | 9418.76 | -581.24 | sell /  / CCI20 > 100 (전형가격·평균절대편차); 조건 미충족; CCI20=-36.6043 |
| v1 | williams_14_recovery | 9643.01 | -356.99 | sell /  / 직전 Williams %R14 < -80, 현재 >= -80 (한 봉 목표); 조건 미충족; Williams_R14=-68.9948, previous_R14=-74.4719 |
| v1 | cmf_20_accumulation | 9710.54 | -289.46 | sell /  / Chaikin Money Flow20 > 0.1; 조건 미충족; CMF20=0.0640816, volume20=6.12929e+06 |
| v1 | chaikin_3_10 | 9610.75 | -389.25 | buy /  / ADL의 EMA3 - EMA10 > 0 그리고 종가 > EMA26; 조건 충족; Chaikin3_10=152048, ADL=2.87515e+07, close=176.86, EMA26=176.75 |
| v1 | roc_10_momentum | 9848.63 | -151.37 | sell /  / 10봉 ROC > 1% 그리고 종가 > EMA26; 조건 미충족; ROC10_percent=0.417363, close=178.045, EMA26=177.705 |
| v1 | trix_15_trend | 9744.30 | -255.70 | sell /  / 15봉 삼중 EMA의 1봉 변화율 TRIX > 0 그리고 종가 > EMA26; 조건 미충족; TRIX15_percent=0.0153444, close=177.148, EMA26=177.751 |
| v1 | keltner_20_breakout | 9862.17 | -137.83 | sell /  / 종가 > EMA20 + 2 x Wilder ATR14; 조건 미충족; close=178.045, upper_Keltner=178.914, EMA20=177.784, ATR14=0.564804 |
| v1 | opening_range_30m | 9973.39 | -26.61 | sell /  / 뉴욕 09:30·09:45 두 완료 봉 최고가를 10:00 이후 종가가 돌파; 조건 미충족; close=178.045, opening_high=178.105 |
| v2 | cash | 10000.00 | 0.00 | 대기 /  / 새 신호 대기 |
| v2 | buy_hold | 10337.91 | 337.91 | buy / partial / 직전 완료 봉 목표 비중 100%; 다음 봉 시가 가정 |
| v2 | trend_8_26 | 9793.22 | -206.78 | sell / filled / 직전 완료 봉 목표 비중 0%; 다음 봉 시가 가정 |
| v2 | momentum_26 | 9975.42 | -24.58 | sell / filled / 직전 완료 봉 목표 비중 0%; 다음 봉 시가 가정 |
| v2 | breakout_8 | 8988.95 | -1011.05 | 중단: 손실 한도 / sell / filled / 직전 완료 봉 목표 비중 0%; 다음 봉 시가 가정 |
| v2 | reversion_12 | 9355.66 | -644.34 | sell / filled / 직전 완료 봉 목표 비중 0%; 다음 봉 시가 가정 |
| v2 | volume_26 | 9410.08 | -589.92 | sell / filled / 직전 완료 봉 목표 비중 0%; 다음 봉 시가 가정 |
| v2 | trend_8_26 AND momentum_26 | 9772.84 | -227.16 | sell / filled / 직전 완료 봉 목표 비중 0%; 다음 봉 시가 가정 |
| v2 | trend_8_26 + momentum_26 | 9884.07 | -115.93 | sell / filled / 직전 완료 봉 목표 비중 0%; 다음 봉 시가 가정 |
| v2 | trend_8_26 AND breakout_8 | 9084.52 | -915.48 | sell / filled / 직전 완료 봉 목표 비중 0%; 다음 봉 시가 가정 |
| v2 | trend_8_26 + breakout_8 | 9407.77 | -592.23 | buy / filled / 직전 완료 봉 목표 비중 50%; 다음 봉 시가 가정 |
| v2 | trend_8_26 AND reversion_12 | 9406.78 | -593.22 | sell / filled / 직전 완료 봉 목표 비중 0%; 다음 봉 시가 가정 |
| v2 | trend_8_26 + reversion_12 | 9572.09 | -427.91 | sell / filled / 직전 완료 봉 목표 비중 0%; 다음 봉 시가 가정 |
| v2 | trend_8_26 AND volume_26 | 9514.99 | -485.01 | sell / filled / 직전 완료 봉 목표 비중 0%; 다음 봉 시가 가정 |
| v2 | trend_8_26 + volume_26 | 9600.09 | -399.91 | sell / filled / 직전 완료 봉 목표 비중 0%; 다음 봉 시가 가정 |
| v2 | momentum_26 AND breakout_8 | 9193.28 | -806.72 | sell / filled / 직전 완료 봉 목표 비중 0%; 다음 봉 시가 가정 |
| v2 | momentum_26 + breakout_8 | 9455.16 | -544.84 | buy / filled / 직전 완료 봉 목표 비중 50%; 다음 봉 시가 가정 |
| v2 | momentum_26 AND reversion_12 | 9466.29 | -533.71 | sell / filled / 직전 완료 봉 목표 비중 0%; 다음 봉 시가 가정 |
| v2 | momentum_26 + reversion_12 | 9660.63 | -339.37 | sell / filled / 직전 완료 봉 목표 비중 0%; 다음 봉 시가 가정 |
| v2 | momentum_26 AND volume_26 | 9795.76 | -204.24 | sell / filled / 직전 완료 봉 목표 비중 0%; 다음 봉 시가 가정 |
| v2 | momentum_26 + volume_26 | 9709.12 | -290.88 | sell / filled / 직전 완료 봉 목표 비중 0%; 다음 봉 시가 가정 |
| v2 | breakout_8 AND reversion_12 | 10000.00 | 0.00 | 대기 /  / 새 신호 대기 |
| v2 | breakout_8 + reversion_12 | 9174.85 | -825.15 | buy / filled / 직전 완료 봉 목표 비중 50%; 다음 봉 시가 가정 |
| v2 | breakout_8 AND volume_26 | 9817.82 | -182.18 | sell / filled / 직전 완료 봉 목표 비중 0%; 다음 봉 시가 가정 |
| v2 | breakout_8 + volume_26 | 9201.50 | -798.50 | buy / filled / 직전 완료 봉 목표 비중 50%; 다음 봉 시가 가정 |
| v2 | reversion_12 AND volume_26 | 9737.38 | -262.62 | sell / filled / 직전 완료 봉 목표 비중 0%; 다음 봉 시가 가정 |
| v2 | reversion_12 + volume_26 | 9402.67 | -597.33 | sell / filled / 직전 완료 봉 목표 비중 0%; 다음 봉 시가 가정 |
| v2 | ema_12_26 | 9774.56 | -225.44 | sell / filled / EMA12 > EMA26; 조건 미충족; EMA12=177.479, EMA26=177.559; 직전 완료 봉 목표를 다음 봉 시가에 모의 적용 |
| v2 | macd_12_26_9 | 9809.86 | -190.14 | sell / filled / MACD > 신호선 그리고 MACD > 0; 조건 미충족; MACD=0.15005, signal9=0.18271; 직전 완료 봉 목표를 다음 봉 시가에 모의 적용 |
| v2 | rsi_14_recovery | 9923.67 | -76.33 | sell / filled / 직전 RSI14 < 30, 현재 RSI14 >= 30 (한 봉 목표); 조건 미충족; RSI14=37.639, previous_RSI14=31.1023; 직전 완료 봉 목표를 다음 봉 시가에 모의 적용 |
| v2 | bollinger_20_reentry | 9684.52 | -315.48 | sell / filled / 직전 종가 < 직전 하단밴드, 현재 하단밴드 <= 종가 <= SMA20 (한 봉 목표); 조건 미충족; close=175.53, lower20=174.782, SMA20=177.101, previous_lower20=174.994; 직전 완료 봉 목표를 다음 봉 시가에 모의 적용 |
| v2 | donchian_20 | 9654.34 | -345.66 | sell / filled / 종가 > 현재 봉을 제외한 직전 20봉 최고가; 조건 미충족; close=178.045, prior_high20=179.205; 직전 완료 봉 목표를 다음 봉 시가에 모의 적용 |
| v2 | atr_14_breakout | 9793.82 | -206.18 | sell / filled / 종가 > 직전 종가 + 직전 ATR14 그리고 종가 > EMA26; 조건 미충족; close=178.95, threshold=179.19, prior_ATR14=0.519565, EMA26=177.678; 직전 완료 봉 목표를 다음 봉 시가에 모의 적용 |
| v2 | session_vwap | 9771.51 | -228.49 | buy / partial / 종가 > 뉴욕 거래일별 누적 전형가격 VWAP; 조건 충족; close=176.86, session_VWAP=176.627, session_volume=3.72585e+06; 직전 완료 봉 목표를 다음 봉 시가에 모의 적용 |
| v2 | obv_20 | 9502.46 | -497.54 | 중단: 손실 한도 / sell / filled / OBV > OBV의 SMA20 그리고 종가 > EMA26; 조건 미충족; OBV=2.24329e+07, OBV_SMA20=2.30895e+07, close=177.005, EMA26=177.393; 직전 완료 봉 목표를 다음 봉 시가에 모의 적용 |
| v2 | stochastic_14_3_recovery | 9622.78 | -377.22 | sell / filled / 직전 %K14 < 20에서 %K14가 %D3 상향 돌파 (한 봉 목표); 조건 미충족; K14=11.8836, D3=5.65987, previous_K14=4.66302, previous_D3=2.02546; 직전 완료 봉 목표를 다음 봉 시가에 모의 적용 |
| v2 | mfi_14_recovery | 10000.00 | 0.00 | 대기 /  / 새 신호 대기 |
| v2 | adx_14_trend | 9993.47 | -6.53 | sell / filled / Wilder ADX14 >= 25 그리고 +DI14 > -DI14; 조건 미충족; ADX14=23.8302, plus_DI14=25.6436, minus_DI14=22.6035; 직전 완료 봉 목표를 다음 봉 시가에 모의 적용 |
| v2 | aroon_25_trend | 9582.18 | -417.82 | sell / filled / Aroon25 Up > 70 그리고 Down < 30 (동률이면 최신 극값); 조건 미충족; Aroon_up=96, Aroon_down=40; 직전 완료 봉 목표를 다음 봉 시가에 모의 적용 |
| v2 | cci_20_momentum | 9398.06 | -601.94 | sell / filled / CCI20 > 100 (전형가격·평균절대편차); 조건 미충족; CCI20=-36.6043; 직전 완료 봉 목표를 다음 봉 시가에 모의 적용 |
| v2 | williams_14_recovery | 9629.52 | -370.48 | sell / filled / 직전 Williams %R14 < -80, 현재 >= -80 (한 봉 목표); 조건 미충족; Williams_R14=-68.9948, previous_R14=-74.4719; 직전 완료 봉 목표를 다음 봉 시가에 모의 적용 |
| v2 | cmf_20_accumulation | 9698.90 | -301.10 | sell / filled / Chaikin Money Flow20 > 0.1; 조건 미충족; CMF20=0.0640816, volume20=6.12929e+06; 직전 완료 봉 목표를 다음 봉 시가에 모의 적용 |
| v2 | chaikin_3_10 | 9594.43 | -405.57 | buy / partial / ADL의 EMA3 - EMA10 > 0 그리고 종가 > EMA26; 조건 충족; Chaikin3_10=152048, ADL=2.87515e+07, close=176.86, EMA26=176.75; 직전 완료 봉 목표를 다음 봉 시가에 모의 적용 |
| v2 | roc_10_momentum | 9840.76 | -159.24 | sell / filled / 10봉 ROC > 1% 그리고 종가 > EMA26; 조건 미충족; ROC10_percent=0.417363, close=178.045, EMA26=177.705; 직전 완료 봉 목표를 다음 봉 시가에 모의 적용 |
| v2 | trix_15_trend | 9732.61 | -267.39 | sell / filled / 15봉 삼중 EMA의 1봉 변화율 TRIX > 0 그리고 종가 > EMA26; 조건 미충족; TRIX15_percent=0.0153444, close=177.148, EMA26=177.751; 직전 완료 봉 목표를 다음 봉 시가에 모의 적용 |
| v2 | keltner_20_breakout | 9854.29 | -145.71 | sell / filled / 종가 > EMA20 + 2 x Wilder ATR14; 조건 미충족; close=178.045, upper_Keltner=178.914, EMA20=177.784, ATR14=0.564804; 직전 완료 봉 목표를 다음 봉 시가에 모의 적용 |
| v2 | opening_range_30m | 9969.40 | -30.60 | sell / filled / 뉴욕 09:30·09:45 두 완료 봉 최고가를 10:00 이후 종가가 돌파; 조건 미충족; close=178.045, opening_high=178.105; 직전 완료 봉 목표를 다음 봉 시가에 모의 적용 |

### 같은 기간의 비용·노출 비교 (사후 연구)

| 전략 | 비용 전 | 비용 후 | 100% 보유 | 같은 평균 노출 보유 | 평균 노출 |
|---|---:|---:|---:|---:|---:|
| cash | 0.00% | 0.00% | 7.76% | 0.00% | 0.00% |
| buy_hold | 8.22% | 7.76% | 7.76% | 7.76% | 100.00% |
| trend_8_26 | 1.38% | -2.79% | 7.76% | 5.37% | 70.08% |
| momentum_26 | 1.57% | -3.82% | 7.76% | 5.43% | 70.87% |
| breakout_8 | -0.61% | -18.41% | 7.76% | 1.97% | 26.25% |
| reversion_12 | 2.50% | -7.33% | 7.76% | 1.63% | 21.78% |
| volume_26 | 0.43% | -7.66% | 7.76% | 0.45% | 6.04% |
| trend_8_26 AND momentum_26 | -0.32% | -5.22% | 7.76% | 4.71% | 61.68% |
| trend_8_26 + momentum_26 | 1.49% | -3.10% | 7.76% | 5.40% | 70.48% |
| trend_8_26 AND breakout_8 | -0.60% | -15.27% | 7.76% | 1.55% | 20.73% |
| trend_8_26 + breakout_8 | 0.41% | -10.55% | 7.76% | 3.65% | 48.17% |
| trend_8_26 AND reversion_12 | -0.82% | -6.87% | 7.76% | 0.76% | 10.24% |
| trend_8_26 + reversion_12 | 1.97% | -4.88% | 7.76% | 3.48% | 45.94% |
| trend_8_26 AND volume_26 | -0.39% | -5.68% | 7.76% | 0.29% | 3.94% |
| trend_8_26 + volume_26 | 0.93% | -5.05% | 7.76% | 2.87% | 38.06% |
| momentum_26 AND breakout_8 | -0.52% | -15.90% | 7.76% | 1.69% | 22.57% |
| momentum_26 + breakout_8 | 0.50% | -11.40% | 7.76% | 3.68% | 48.56% |
| momentum_26 AND reversion_12 | -0.06% | -6.95% | 7.76% | 0.72% | 9.71% |
| momentum_26 + reversion_12 | 2.07% | -4.59% | 7.76% | 3.51% | 46.33% |
| momentum_26 AND volume_26 | 0.84% | -3.31% | 7.76% | 0.19% | 2.62% |
| momentum_26 + volume_26 | 1.03% | -4.76% | 7.76% | 2.90% | 38.46% |
| breakout_8 AND reversion_12 | 0.00% | 0.00% | 7.76% | 0.00% | 0.00% |
| breakout_8 + reversion_12 | 0.95% | -12.69% | 7.76% | 1.80% | 24.03% |
| breakout_8 AND volume_26 | -0.10% | -2.18% | 7.76% | 0.10% | 1.31% |
| breakout_8 + volume_26 | -0.08% | -12.47% | 7.76% | 1.21% | 16.15% |
| reversion_12 AND volume_26 | -0.04% | -3.35% | 7.76% | 0.18% | 2.36% |
| reversion_12 + volume_26 | 1.48% | -6.71% | 7.76% | 1.04% | 13.92% |
| ema_12_26 | 0.21% | -3.10% | 7.76% | 5.76% | 75.07% |
| macd_12_26_9 | -1.13% | -7.17% | 7.76% | 3.28% | 43.31% |
| rsi_14_recovery | -0.08% | -1.33% | 7.76% | 0.06% | 0.79% |
| bollinger_20_reentry | -1.53% | -5.18% | 7.76% | 0.18% | 2.36% |
| donchian_20 | -2.09% | -10.73% | 7.76% | 0.70% | 9.45% |
| atr_14_breakout | 0.61% | -7.11% | 7.76% | 0.39% | 5.25% |
| session_vwap | 0.94% | -9.88% | 7.76% | 4.89% | 64.04% |
| obv_20 | -0.68% | -11.70% | 7.76% | 3.68% | 48.56% |
| stochastic_14_3_recovery | 0.05% | -9.54% | 7.76% | 0.47% | 6.30% |
| mfi_14_recovery | -0.31% | -1.97% | 7.76% | 0.08% | 1.05% |
| adx_14_trend | 3.33% | 0.76% | 7.76% | 2.91% | 38.58% |
| aroon_25_trend | -3.68% | -10.32% | 7.76% | 2.51% | 33.33% |
| cci_20_momentum | 1.06% | -8.63% | 7.76% | 2.13% | 28.35% |
| williams_14_recovery | -1.21% | -7.24% | 7.76% | 0.29% | 3.94% |
| cmf_20_accumulation | 1.57% | -5.03% | 7.76% | 3.97% | 52.23% |
| chaikin_3_10 | 1.11% | -8.20% | 7.76% | 4.56% | 59.84% |
| roc_10_momentum | -0.09% | -5.80% | 7.76% | 0.88% | 11.81% |
| trix_15_trend | -0.04% | -6.53% | 7.76% | 4.75% | 62.20% |
| keltner_20_breakout | 0.18% | -5.94% | 7.76% | 1.22% | 16.27% |
| opening_range_30m | -0.16% | -8.21% | 7.76% | 2.07% | 27.56% |

동일 구간·초기 자금, 종료 시 청산 비용 포함. 노출 맞춤은 사후 설명용이며 v2 실제 계좌 성과가 아닙니다.
[낙폭 분해·비용 영향·전체 구간](XOM/comparison.json)

[v1 전체 기록](XOM/accounts.json) · [v2 전체 기록](XOM/accounts-v2.json)

## JNJ 계좌

| 모델 | 전략 | 평가액 USD | 손익 USD | 최근 매매·이유 |
|---|---|---:|---:|---|
| v1 | cash | 10000.00 | 0.00 | 대기 /  / 새 신호 대기 |
| v1 | buy_hold | 10445.60 | 445.60 | buy /  / buy_hold: prior completed bar target 100%; next bar open simulation |
| v1 | trend_8_26 | 10374.02 | 374.02 | buy /  / trend_8_26: prior completed bar target 100%; next bar open simulation |
| v1 | momentum_26 | 9913.55 | -86.45 | buy /  / momentum_26: prior completed bar target 100%; next bar open simulation |
| v1 | breakout_8 | 9598.88 | -401.12 | sell /  / breakout_8: prior completed bar target 0%; next bar open simulation |
| v1 | reversion_12 | 9747.78 | -252.22 | sell /  / reversion_12: prior completed bar target 0%; next bar open simulation |
| v1 | volume_26 | 10040.58 | 40.58 | sell /  / volume_26: prior completed bar target 0%; next bar open simulation |
| v1 | trend_8_26 AND momentum_26 | 10006.28 | 6.28 | buy /  / trend_8_26 AND momentum_26: prior completed bar target 100%; next bar open simulation |
| v1 | trend_8_26 + momentum_26 | 10141.68 | 141.68 | buy /  / trend_8_26 + momentum_26: prior completed bar target 100%; next bar open simulation |
| v1 | trend_8_26 AND breakout_8 | 9994.20 | -5.80 | sell /  / trend_8_26 AND breakout_8: prior completed bar target 0%; next bar open simulation |
| v1 | trend_8_26 + breakout_8 | 9999.29 | -0.71 | sell /  / trend_8_26 + breakout_8: prior completed bar target 50%; next bar open simulation |
| v1 | trend_8_26 AND reversion_12 | 9930.57 | -69.43 | sell /  / trend_8_26 AND reversion_12: prior completed bar target 0%; next bar open simulation |
| v1 | trend_8_26 + reversion_12 | 10056.25 | 56.25 | buy /  / trend_8_26 + reversion_12: prior completed bar target 50%; next bar open simulation |
| v1 | trend_8_26 AND volume_26 | 10134.54 | 134.54 | sell /  / trend_8_26 AND volume_26: prior completed bar target 0%; next bar open simulation |
| v1 | trend_8_26 + volume_26 | 10206.17 | 206.17 | buy /  / trend_8_26 + volume_26: prior completed bar target 50%; next bar open simulation |
| v1 | momentum_26 AND breakout_8 | 9831.54 | -168.46 | sell /  / momentum_26 AND breakout_8: prior completed bar target 0%; next bar open simulation |
| v1 | momentum_26 + breakout_8 | 9755.09 | -244.91 | sell /  / momentum_26 + breakout_8: prior completed bar target 50%; next bar open simulation |
| v1 | momentum_26 AND reversion_12 | 9938.52 | -61.48 | sell /  / momentum_26 AND reversion_12: prior completed bar target 0%; next bar open simulation |
| v1 | momentum_26 + reversion_12 | 9869.52 | -130.48 | buy /  / momentum_26 + reversion_12: prior completed bar target 50%; next bar open simulation |
| v1 | momentum_26 AND volume_26 | 10000.00 | 0.00 | 대기 /  / 새 신호 대기 |
| v1 | momentum_26 + volume_26 | 10037.09 | 37.09 | buy /  / momentum_26 + volume_26: prior completed bar target 50%; next bar open simulation |
| v1 | breakout_8 AND reversion_12 | 10000.00 | 0.00 | 대기 /  / 새 신호 대기 |
| v1 | breakout_8 + reversion_12 | 9672.90 | -327.10 | sell /  / breakout_8 + reversion_12: prior completed bar target 0%; next bar open simulation |
| v1 | breakout_8 AND volume_26 | 10139.49 | 139.49 | sell /  / breakout_8 AND volume_26: prior completed bar target 0%; next bar open simulation |
| v1 | breakout_8 + volume_26 | 9836.84 | -163.16 | sell /  / breakout_8 + volume_26: prior completed bar target 0%; next bar open simulation |
| v1 | reversion_12 AND volume_26 | 9933.02 | -66.98 | sell /  / reversion_12 AND volume_26: prior completed bar target 0%; next bar open simulation |
| v1 | reversion_12 + volume_26 | 9913.08 | -86.92 | sell /  / reversion_12 + volume_26: prior completed bar target 0%; next bar open simulation |
| v1 | ema_12_26 | 10008.84 | 8.84 | buy /  / EMA12 > EMA26; 조건 충족; EMA12=256.701, EMA26=256.629 |
| v1 | macd_12_26_9 | 10129.06 | 129.06 | buy /  / MACD > 신호선 그리고 MACD > 0; 조건 충족; MACD=0.0724674, signal9=-0.175801 |
| v1 | rsi_14_recovery | 9923.04 | -76.96 | sell /  / 직전 RSI14 < 30, 현재 RSI14 >= 30 (한 봉 목표); 조건 미충족; RSI14=40.3665, previous_RSI14=36.2025 |
| v1 | bollinger_20_reentry | 9816.96 | -183.04 | sell /  / 직전 종가 < 직전 하단밴드, 현재 하단밴드 <= 종가 <= SMA20 (한 봉 목표); 조건 미충족; close=255.05, lower20=254.819, SMA20=258.099, previous_lower20=255.312 |
| v1 | donchian_20 | 9872.09 | -127.91 | sell /  / 종가 > 현재 봉을 제외한 직전 20봉 최고가; 조건 미충족; close=267.185, prior_high20=267.475 |
| v1 | atr_14_breakout | 9670.87 | -329.13 | sell /  / 종가 > 직전 종가 + 직전 ATR14 그리고 종가 > EMA26; 조건 미충족; close=267.475, threshold=268.093, prior_ATR14=0.987507, EMA26=261.689 |
| v1 | session_vwap | 10086.64 | 86.64 | buy /  / 종가 > 뉴욕 거래일별 누적 전형가격 VWAP; 조건 충족; close=256.05, session_VWAP=255.552, session_volume=3.26826e+06 |
| v1 | obv_20 | 9868.76 | -131.24 | buy /  / OBV > OBV의 SMA20 그리고 종가 > EMA26; 조건 충족; OBV=8.73204e+06, OBV_SMA20=8.54861e+06, close=257.085, EMA26=256.499 |
| v1 | stochastic_14_3_recovery | 9576.18 | -423.82 | sell /  / 직전 %K14 < 20에서 %K14가 %D3 상향 돌파 (한 봉 목표); 조건 미충족; K14=33.4928, D3=23.2217, previous_K14=28.5165, previous_D3=14.8644 |
| v1 | mfi_14_recovery | 9931.49 | -68.51 | sell /  / 직전 MFI14 < 20, 현재 MFI14 >= 20 (한 봉 목표); 조건 미충족; MFI14=35.8262, previous_MFI14=31.0222 |
| v1 | adx_14_trend | 9821.37 | -178.63 | buy /  / Wilder ADX14 >= 25 그리고 +DI14 > -DI14; 조건 충족; ADX14=27.0686, plus_DI14=50.9231, minus_DI14=9.79199 |
| v1 | aroon_25_trend | 10141.34 | 141.34 | buy /  / Aroon25 Up > 70 그리고 Down < 30 (동률이면 최신 극값); 조건 충족; Aroon_up=100, Aroon_down=24 |
| v1 | cci_20_momentum | 10185.26 | 185.26 | sell /  / CCI20 > 100 (전형가격·평균절대편차); 조건 미충족; CCI20=97.4316 |
| v1 | williams_14_recovery | 9706.89 | -293.11 | sell /  / 직전 Williams %R14 < -80, 현재 >= -80 (한 봉 목표); 조건 미충족; Williams_R14=-66.5072, previous_R14=-71.4835 |
| v1 | cmf_20_accumulation | 10443.59 | 443.59 | buy /  / Chaikin Money Flow20 > 0.1; 조건 충족; CMF20=0.396629, volume20=6.26242e+06 |
| v1 | chaikin_3_10 | 10167.30 | 167.30 | buy /  / ADL의 EMA3 - EMA10 > 0 그리고 종가 > EMA26; 조건 충족; Chaikin3_10=8814.88, ADL=5.01916e+06, close=256.505, EMA26=256.405 |
| v1 | roc_10_momentum | 9882.61 | -117.39 | buy /  / 10봉 ROC > 1% 그리고 종가 > EMA26; 조건 충족; ROC10_percent=2.2132, close=261.63, EMA26=256.999 |
| v1 | trix_15_trend | 9814.75 | -185.25 | buy /  / 15봉 삼중 EMA의 1봉 변화율 TRIX > 0 그리고 종가 > EMA26; 조건 충족; TRIX15_percent=0.00204174, close=262.76, EMA26=257.426 |
| v1 | keltner_20_breakout | 10111.30 | 111.30 | buy /  / 종가 > EMA20 + 2 x Wilder ATR14; 조건 충족; close=261.63, upper_Keltner=258.85, EMA20=257.085, ATR14=0.882261 |
| v1 | opening_range_30m | 10127.34 | 127.34 | buy /  / 뉴욕 09:30·09:45 두 완료 봉 최고가를 10:00 이후 종가가 돌파; 조건 충족; close=263.54, opening_high=263.19 |
| v2 | cash | 10000.00 | 0.00 | 대기 /  / 새 신호 대기 |
| v2 | buy_hold | 10201.81 | 201.81 | 중단: 손실 한도 / buy / partial / 직전 완료 봉 목표 비중 100%; 다음 봉 시가 가정 |
| v2 | trend_8_26 | 10201.81 | 201.81 | 중단: 손실 한도 / buy / partial / 직전 완료 봉 목표 비중 100%; 다음 봉 시가 가정 |
| v2 | momentum_26 | 10201.81 | 201.81 | 중단: 손실 한도 / buy / partial / 직전 완료 봉 목표 비중 100%; 다음 봉 시가 가정 |
| v2 | breakout_8 | 9343.39 | -656.61 | 중단: 손실 한도 / sell / filled / 직전 완료 봉 목표 비중 0%; 다음 봉 시가 가정 |
| v2 | reversion_12 | 9434.41 | -565.59 | sell / filled / 직전 완료 봉 목표 비중 0%; 다음 봉 시가 가정 |
| v2 | volume_26 | 9819.31 | -180.69 | sell / filled / 직전 완료 봉 목표 비중 0%; 다음 봉 시가 가정 |
| v2 | trend_8_26 AND momentum_26 | 10201.81 | 201.81 | 중단: 손실 한도 / buy / partial / 직전 완료 봉 목표 비중 100%; 다음 봉 시가 가정 |
| v2 | trend_8_26 + momentum_26 | 10201.81 | 201.81 | 중단: 손실 한도 / buy / partial / 직전 완료 봉 목표 비중 100%; 다음 봉 시가 가정 |
| v2 | trend_8_26 AND breakout_8 | 9419.39 | -580.61 | 중단: 손실 한도 / sell / filled / 직전 완료 봉 목표 비중 0%; 다음 봉 시가 가정 |
| v2 | trend_8_26 + breakout_8 | 9553.35 | -446.65 | sell / filled / 직전 완료 봉 목표 비중 50%; 다음 봉 시가 가정 |
| v2 | trend_8_26 AND reversion_12 | 9900.89 | -99.11 | sell / filled / 직전 완료 봉 목표 비중 0%; 다음 봉 시가 가정 |
| v2 | trend_8_26 + reversion_12 | 9732.92 | -267.08 | 중단: 손실 한도 / sell / filled / 직전 완료 봉 목표 비중 0%; 다음 봉 시가 가정 |
| v2 | trend_8_26 AND volume_26 | 9997.51 | -2.49 | sell / filled / 직전 완료 봉 목표 비중 0%; 다음 봉 시가 가정 |
| v2 | trend_8_26 + volume_26 | 10079.56 | 79.56 | 중단: 손실 한도 / buy / filled / 직전 완료 봉 목표 비중 50%; 다음 봉 시가 가정 |
| v2 | momentum_26 AND breakout_8 | 9425.68 | -574.32 | sell / filled / 직전 완료 봉 목표 비중 0%; 다음 봉 시가 가정 |
| v2 | momentum_26 + breakout_8 | 9310.34 | -689.66 | sell / filled / 직전 완료 봉 목표 비중 50%; 다음 봉 시가 가정 |
| v2 | momentum_26 AND reversion_12 | 9871.83 | -128.17 | sell / filled / 직전 완료 봉 목표 비중 0%; 다음 봉 시가 가정 |
| v2 | momentum_26 + reversion_12 | 9732.92 | -267.08 | 중단: 손실 한도 / sell / filled / 직전 완료 봉 목표 비중 0%; 다음 봉 시가 가정 |
| v2 | momentum_26 AND volume_26 | 9920.93 | -79.07 | sell / filled / 직전 완료 봉 목표 비중 0%; 다음 봉 시가 가정 |
| v2 | momentum_26 + volume_26 | 10079.56 | 79.56 | 중단: 손실 한도 / buy / filled / 직전 완료 봉 목표 비중 50%; 다음 봉 시가 가정 |
| v2 | breakout_8 AND reversion_12 | 10000.00 | 0.00 | 대기 /  / 새 신호 대기 |
| v2 | breakout_8 + reversion_12 | 9248.19 | -751.81 | sell / filled / 직전 완료 봉 목표 비중 0%; 다음 봉 시가 가정 |
| v2 | breakout_8 AND volume_26 | 9949.08 | -50.92 | sell / filled / 직전 완료 봉 목표 비중 0%; 다음 봉 시가 가정 |
| v2 | breakout_8 + volume_26 | 9434.96 | -565.04 | sell / filled / 직전 완료 봉 목표 비중 0%; 다음 봉 시가 가정 |
| v2 | reversion_12 AND volume_26 | 9816.09 | -183.91 | sell / filled / 직전 완료 봉 목표 비중 0%; 다음 봉 시가 가정 |
| v2 | reversion_12 + volume_26 | 9665.84 | -334.16 | sell / filled / 직전 완료 봉 목표 비중 0%; 다음 봉 시가 가정 |
| v2 | ema_12_26 | 10001.84 | 1.84 | buy / partial / EMA12 > EMA26; 조건 충족; EMA12=256.701, EMA26=256.629; 직전 완료 봉 목표를 다음 봉 시가에 모의 적용 |
| v2 | macd_12_26_9 | 10121.97 | 121.97 | buy / partial / MACD > 신호선 그리고 MACD > 0; 조건 충족; MACD=0.0724674, signal9=-0.175801; 직전 완료 봉 목표를 다음 봉 시가에 모의 적용 |
| v2 | rsi_14_recovery | 9919.07 | -80.93 | sell / filled / 직전 RSI14 < 30, 현재 RSI14 >= 30 (한 봉 목표); 조건 미충족; RSI14=40.3665, previous_RSI14=36.2025; 직전 완료 봉 목표를 다음 봉 시가에 모의 적용 |
| v2 | bollinger_20_reentry | 9811.07 | -188.93 | sell / filled / 직전 종가 < 직전 하단밴드, 현재 하단밴드 <= 종가 <= SMA20 (한 봉 목표); 조건 미충족; close=255.05, lower20=254.819, SMA20=258.099, previous_lower20=255.312; 직전 완료 봉 목표를 다음 봉 시가에 모의 적용 |
| v2 | donchian_20 | 9860.25 | -139.75 | sell / filled / 종가 > 현재 봉을 제외한 직전 20봉 최고가; 조건 미충족; close=267.185, prior_high20=267.475; 직전 완료 봉 목표를 다음 봉 시가에 모의 적용 |
| v2 | atr_14_breakout | 9657.34 | -342.66 | sell / filled / 종가 > 직전 종가 + 직전 ATR14 그리고 종가 > EMA26; 조건 미충족; close=267.475, threshold=268.093, prior_ATR14=0.987507, EMA26=261.689; 직전 완료 봉 목표를 다음 봉 시가에 모의 적용 |
| v2 | session_vwap | 10067.49 | 67.49 | buy / partial / 종가 > 뉴욕 거래일별 누적 전형가격 VWAP; 조건 충족; close=256.05, session_VWAP=255.552, session_volume=3.26826e+06; 직전 완료 봉 목표를 다음 봉 시가에 모의 적용 |
| v2 | obv_20 | 9850.03 | -149.97 | buy / partial / OBV > OBV의 SMA20 그리고 종가 > EMA26; 조건 충족; OBV=8.59102e+06, OBV_SMA20=8.40759e+06, close=257.085, EMA26=256.499; 직전 완료 봉 목표를 다음 봉 시가에 모의 적용 |
| v2 | stochastic_14_3_recovery | 9560.87 | -439.13 | sell / filled / 직전 %K14 < 20에서 %K14가 %D3 상향 돌파 (한 봉 목표); 조건 미충족; K14=33.4928, D3=23.2217, previous_K14=28.5165, previous_D3=14.8644; 직전 완료 봉 목표를 다음 봉 시가에 모의 적용 |
| v2 | mfi_14_recovery | 9925.53 | -74.47 | sell / filled / 직전 MFI14 < 20, 현재 MFI14 >= 20 (한 봉 목표); 조건 미충족; MFI14=35.8262, previous_MFI14=31.0222; 직전 완료 봉 목표를 다음 봉 시가에 모의 적용 |
| v2 | adx_14_trend | 9812.54 | -187.46 | buy / partial / Wilder ADX14 >= 25 그리고 +DI14 > -DI14; 조건 충족; ADX14=27.0686, plus_DI14=50.9231, minus_DI14=9.79199; 직전 완료 봉 목표를 다음 봉 시가에 모의 적용 |
| v2 | aroon_25_trend | 10136.27 | 136.27 | buy / partial / Aroon25 Up > 70 그리고 Down < 30 (동률이면 최신 극값); 조건 충족; Aroon_up=100, Aroon_down=24; 직전 완료 봉 목표를 다음 봉 시가에 모의 적용 |
| v2 | cci_20_momentum | 10177.12 | 177.12 | sell / filled / CCI20 > 100 (전형가격·평균절대편차); 조건 미충족; CCI20=97.4316; 직전 완료 봉 목표를 다음 봉 시가에 모의 적용 |
| v2 | williams_14_recovery | 9697.19 | -302.81 | sell / filled / 직전 Williams %R14 < -80, 현재 >= -80 (한 봉 목표); 조건 미충족; Williams_R14=-66.5072, previous_R14=-71.4835; 직전 완료 봉 목표를 다음 봉 시가에 모의 적용 |
| v2 | cmf_20_accumulation | 10438.37 | 438.37 | buy / partial / Chaikin Money Flow20 > 0.1; 조건 충족; CMF20=0.396629, volume20=6.26242e+06; 직전 완료 봉 목표를 다음 봉 시가에 모의 적용 |
| v2 | chaikin_3_10 | 10158.15 | 158.15 | buy / partial / ADL의 EMA3 - EMA10 > 0 그리고 종가 > EMA26; 조건 충족; Chaikin3_10=8814.88, ADL=4.70768e+06, close=256.505, EMA26=256.405; 직전 완료 봉 목표를 다음 봉 시가에 모의 적용 |
| v2 | roc_10_momentum | 9873.72 | -126.28 | buy / partial / 10봉 ROC > 1% 그리고 종가 > EMA26; 조건 충족; ROC10_percent=2.2132, close=261.63, EMA26=256.999; 직전 완료 봉 목표를 다음 봉 시가에 모의 적용 |
| v2 | trix_15_trend | 9807.88 | -192.12 | buy / partial / 15봉 삼중 EMA의 1봉 변화율 TRIX > 0 그리고 종가 > EMA26; 조건 충족; TRIX15_percent=0.00204174, close=262.76, EMA26=257.426; 직전 완료 봉 목표를 다음 봉 시가에 모의 적용 |
| v2 | keltner_20_breakout | 10108.27 | 108.27 | buy / partial / 종가 > EMA20 + 2 x Wilder ATR14; 조건 충족; close=261.63, upper_Keltner=258.85, EMA20=257.085, ATR14=0.882261; 직전 완료 봉 목표를 다음 봉 시가에 모의 적용 |
| v2 | opening_range_30m | 10126.32 | 126.32 | buy / partial / 뉴욕 09:30·09:45 두 완료 봉 최고가를 10:00 이후 종가가 돌파; 조건 충족; close=263.54, opening_high=263.19; 직전 완료 봉 목표를 다음 봉 시가에 모의 적용 |

### 같은 기간의 비용·노출 비교 (사후 연구)

| 전략 | 비용 전 | 비용 후 | 100% 보유 | 같은 평균 노출 보유 | 평균 노출 |
|---|---:|---:|---:|---:|---:|
| cash | 0.00% | 0.00% | 2.55% | 0.00% | 0.00% |
| buy_hold | 2.98% | 2.55% | 2.55% | 2.55% | 100.00% |
| trend_8_26 | 6.77% | 4.11% | 2.55% | 1.34% | 52.23% |
| momentum_26 | 1.29% | -2.06% | 2.55% | 1.28% | 49.61% |
| breakout_8 | 2.43% | -16.62% | 2.55% | 0.62% | 24.15% |
| reversion_12 | -4.65% | -12.34% | 2.55% | 0.67% | 25.98% |
| volume_26 | 1.99% | -4.64% | 2.55% | 0.16% | 6.04% |
| trend_8_26 AND momentum_26 | 2.98% | -0.00% | 2.55% | 1.13% | 44.09% |
| trend_8_26 + momentum_26 | 4.01% | 0.99% | 2.55% | 1.31% | 50.92% |
| trend_8_26 AND breakout_8 | 3.72% | -9.70% | 2.55% | 0.45% | 17.32% |
| trend_8_26 + breakout_8 | 4.61% | -6.61% | 2.55% | 0.98% | 38.20% |
| trend_8_26 AND reversion_12 | 1.37% | -1.98% | 2.55% | 0.15% | 5.77% |
| trend_8_26 + reversion_12 | 0.94% | -4.25% | 2.55% | 1.01% | 39.11% |
| trend_8_26 AND volume_26 | 3.25% | 0.26% | 2.55% | 0.05% | 2.10% |
| trend_8_26 + volume_26 | 4.39% | -0.13% | 2.55% | 0.75% | 29.14% |
| momentum_26 AND breakout_8 | 2.72% | -9.44% | 2.55% | 0.40% | 15.49% |
| momentum_26 + breakout_8 | 1.89% | -9.42% | 2.55% | 0.95% | 36.88% |
| momentum_26 AND reversion_12 | -0.27% | -3.16% | 2.55% | 0.16% | 6.30% |
| momentum_26 + reversion_12 | -1.70% | -6.75% | 2.55% | 0.97% | 37.80% |
| momentum_26 AND volume_26 | 0.14% | -0.70% | 2.55% | 0.01% | 0.52% |
| momentum_26 + volume_26 | 1.68% | -2.12% | 2.55% | 0.72% | 27.82% |
| breakout_8 AND reversion_12 | 0.00% | 0.00% | 2.55% | 0.00% | 0.00% |
| breakout_8 + reversion_12 | -1.15% | -14.15% | 2.55% | 0.65% | 25.07% |
| breakout_8 AND volume_26 | 1.33% | 0.06% | 2.55% | 0.03% | 1.05% |
| breakout_8 + volume_26 | 2.22% | -9.89% | 2.55% | 0.39% | 15.10% |
| reversion_12 AND volume_26 | -1.19% | -3.65% | 2.55% | 0.05% | 2.10% |
| reversion_12 + volume_26 | -1.37% | -7.99% | 2.55% | 0.41% | 16.01% |
| ema_12_26 | 1.57% | -1.37% | 2.55% | 1.30% | 50.39% |
| macd_12_26_9 | 8.63% | 5.04% | 2.55% | 0.85% | 33.07% |
| rsi_14_recovery | -1.35% | -6.20% | 2.55% | 0.08% | 3.15% |
| bollinger_20_reentry | -1.28% | -5.34% | 2.55% | 0.07% | 2.62% |
| donchian_20 | 2.21% | -6.81% | 2.55% | 0.24% | 9.19% |
| atr_14_breakout | 1.13% | -6.24% | 2.55% | 0.15% | 5.77% |
| session_vwap | 7.84% | -0.84% | 2.55% | 1.42% | 55.12% |
| obv_20 | -1.98% | -12.12% | 2.55% | 1.02% | 39.63% |
| stochastic_14_3_recovery | -0.70% | -11.35% | 2.55% | 0.18% | 7.09% |
| mfi_14_recovery | 0.80% | -1.30% | 2.55% | 0.03% | 1.31% |
| adx_14_trend | -2.02% | -7.23% | 2.55% | 1.02% | 39.63% |
| aroon_25_trend | 6.01% | 1.65% | 2.55% | 0.87% | 33.60% |
| cci_20_momentum | 4.75% | -1.65% | 2.55% | 0.63% | 24.41% |
| williams_14_recovery | -2.20% | -8.94% | 2.55% | 0.12% | 4.46% |
| cmf_20_accumulation | 8.18% | 3.29% | 2.55% | 0.99% | 38.58% |
| chaikin_3_10 | 0.67% | -4.68% | 2.55% | 1.09% | 42.52% |
| roc_10_momentum | -0.68% | -7.91% | 2.55% | 0.54% | 21.00% |
| trix_15_trend | 0.11% | -2.79% | 2.55% | 1.00% | 38.85% |
| keltner_20_breakout | 2.38% | -1.83% | 2.55% | 0.39% | 15.22% |
| opening_range_30m | 2.28% | -1.93% | 2.55% | 0.74% | 28.61% |

동일 구간·초기 자금, 종료 시 청산 비용 포함. 노출 맞춤은 사후 설명용이며 v2 실제 계좌 성과가 아닙니다.
[낙폭 분해·비용 영향·전체 구간](JNJ/comparison.json)

[v1 전체 기록](JNJ/accounts.json) · [v2 전체 기록](JNJ/accounts-v2.json)

## CAT 계좌

| 모델 | 전략 | 평가액 USD | 손익 USD | 최근 매매·이유 |
|---|---|---:|---:|---|
| v1 | cash | 10000.00 | 0.00 | 대기 /  / 새 신호 대기 |
| v1 | buy_hold | 9562.13 | -437.87 | buy /  / buy_hold: prior completed bar target 100%; next bar open simulation |
| v1 | trend_8_26 | 9570.52 | -429.48 | sell /  / trend_8_26: prior completed bar target 0%; next bar open simulation |
| v1 | momentum_26 | 9290.58 | -709.42 | sell /  / momentum_26: prior completed bar target 0%; next bar open simulation |
| v1 | breakout_8 | 9544.96 | -455.04 | sell /  / breakout_8: prior completed bar target 0%; next bar open simulation |
| v1 | reversion_12 | 9689.85 | -310.15 | sell /  / reversion_12: prior completed bar target 0%; next bar open simulation |
| v1 | volume_26 | 9683.18 | -316.82 | sell /  / volume_26: prior completed bar target 0%; next bar open simulation |
| v1 | trend_8_26 AND momentum_26 | 9471.21 | -528.79 | sell /  / trend_8_26 AND momentum_26: prior completed bar target 0%; next bar open simulation |
| v1 | trend_8_26 + momentum_26 | 9430.55 | -569.45 | sell /  / trend_8_26 + momentum_26: prior completed bar target 0%; next bar open simulation |
| v1 | trend_8_26 AND breakout_8 | 9747.92 | -252.08 | sell /  / trend_8_26 AND breakout_8: prior completed bar target 0%; next bar open simulation |
| v1 | trend_8_26 + breakout_8 | 9559.68 | -440.32 | sell /  / trend_8_26 + breakout_8: prior completed bar target 0%; next bar open simulation |
| v1 | trend_8_26 AND reversion_12 | 9919.62 | -80.38 | sell /  / trend_8_26 AND reversion_12: prior completed bar target 0%; next bar open simulation |
| v1 | trend_8_26 + reversion_12 | 9690.38 | -309.62 | sell /  / trend_8_26 + reversion_12: prior completed bar target 0%; next bar open simulation |
| v1 | trend_8_26 AND volume_26 | 9965.69 | -34.31 | sell /  / trend_8_26 AND volume_26: prior completed bar target 0%; next bar open simulation |
| v1 | trend_8_26 + volume_26 | 9667.13 | -332.87 | sell /  / trend_8_26 + volume_26: prior completed bar target 0%; next bar open simulation |
| v1 | momentum_26 AND breakout_8 | 9615.85 | -384.15 | sell /  / momentum_26 AND breakout_8: prior completed bar target 0%; next bar open simulation |
| v1 | momentum_26 + breakout_8 | 9417.88 | -582.12 | sell /  / momentum_26 + breakout_8: prior completed bar target 0%; next bar open simulation |
| v1 | momentum_26 AND reversion_12 | 9878.81 | -121.19 | sell /  / momentum_26 AND reversion_12: prior completed bar target 0%; next bar open simulation |
| v1 | momentum_26 + reversion_12 | 9508.61 | -491.39 | sell /  / momentum_26 + reversion_12: prior completed bar target 0%; next bar open simulation |
| v1 | momentum_26 AND volume_26 | 9894.55 | -105.45 | sell /  / momentum_26 AND volume_26: prior completed bar target 0%; next bar open simulation |
| v1 | momentum_26 + volume_26 | 9504.77 | -495.23 | sell /  / momentum_26 + volume_26: prior completed bar target 0%; next bar open simulation |
| v1 | breakout_8 AND reversion_12 | 10000.00 | 0.00 | 대기 /  / 새 신호 대기 |
| v1 | breakout_8 + reversion_12 | 9617.78 | -382.22 | sell /  / breakout_8 + reversion_12: prior completed bar target 0%; next bar open simulation |
| v1 | breakout_8 AND volume_26 | 9894.55 | -105.45 | sell /  / breakout_8 AND volume_26: prior completed bar target 0%; next bar open simulation |
| v1 | breakout_8 + volume_26 | 9614.01 | -385.99 | sell /  / breakout_8 + volume_26: prior completed bar target 0%; next bar open simulation |
| v1 | reversion_12 AND volume_26 | 9810.19 | -189.81 | sell /  / reversion_12 AND volume_26: prior completed bar target 0%; next bar open simulation |
| v1 | reversion_12 + volume_26 | 9686.95 | -313.05 | sell /  / reversion_12 + volume_26: prior completed bar target 0%; next bar open simulation |
| v1 | ema_12_26 | 9597.59 | -402.41 | sell /  / EMA12 > EMA26; 조건 미충족; EMA12=734.57, EMA26=734.673 |
| v1 | macd_12_26_9 | 9988.51 | -11.49 | sell /  / MACD > 신호선 그리고 MACD > 0; 조건 미충족; MACD=2.92675, signal9=3.02629 |
| v1 | rsi_14_recovery | 9950.97 | -49.03 | sell /  / 직전 RSI14 < 30, 현재 RSI14 >= 30 (한 봉 목표); 조건 미충족; RSI14=34.1484, previous_RSI14=34.3526 |
| v1 | bollinger_20_reentry | 9693.48 | -306.52 | sell /  / 직전 종가 < 직전 하단밴드, 현재 하단밴드 <= 종가 <= SMA20 (한 봉 목표); 조건 미충족; close=698.04, lower20=693.892, SMA20=727.609, previous_lower20=698.501 |
| v1 | donchian_20 | 9943.28 | -56.72 | sell /  / 종가 > 현재 봉을 제외한 직전 20봉 최고가; 조건 미충족; close=735.35, prior_high20=745 |
| v1 | atr_14_breakout | 9768.31 | -231.69 | sell /  / 종가 > 직전 종가 + 직전 ATR14 그리고 종가 > EMA26; 조건 미충족; close=735.35, threshold=737.263, prior_ATR14=4.10289, EMA26=727.331 |
| v1 | session_vwap | 9184.29 | -815.71 | sell /  / 종가 > 뉴욕 거래일별 누적 전형가격 VWAP; 조건 미충족; close=702.21, session_VWAP=704.334, session_volume=2.86686e+06 |
| v1 | obv_20 | 9541.23 | -458.77 | sell /  / OBV > OBV의 SMA20 그리고 종가 > EMA26; 조건 미충족; OBV=-4.81948e+06, OBV_SMA20=-4.73979e+06, close=711.18, EMA26=734.673 |
| v1 | stochastic_14_3_recovery | 9783.81 | -216.19 | sell /  / 직전 %K14 < 20에서 %K14가 %D3 상향 돌파 (한 봉 목표); 조건 미충족; K14=13.5114, D3=6.65149, previous_K14=5.262, previous_D3=2.35532 |
| v1 | mfi_14_recovery | 10068.63 | 68.63 | sell /  / 직전 MFI14 < 20, 현재 MFI14 >= 20 (한 봉 목표); 조건 미충족; MFI14=32.7313, previous_MFI14=24.1736 |
| v1 | adx_14_trend | 9614.13 | -385.87 | sell /  / Wilder ADX14 >= 25 그리고 +DI14 > -DI14; 조건 미충족; ADX14=37.6898, plus_DI14=16.8278, minus_DI14=52.0976 |
| v1 | aroon_25_trend | 9979.61 | -20.39 | sell /  / Aroon25 Up > 70 그리고 Down < 30 (동률이면 최신 극값); 조건 미충족; Aroon_up=68, Aroon_down=20 |
| v1 | cci_20_momentum | 9862.85 | -137.15 | sell /  / CCI20 > 100 (전형가격·평균절대편차); 조건 미충족; CCI20=99.2123 |
| v1 | williams_14_recovery | 9958.77 | -41.23 | sell /  / 직전 Williams %R14 < -80, 현재 >= -80 (한 봉 목표); 조건 미충족; Williams_R14=-79.0512, previous_R14=-78.5192 |
| v1 | cmf_20_accumulation | 9458.11 | -541.89 | sell /  / Chaikin Money Flow20 > 0.1; 조건 미충족; CMF20=0.0105743, volume20=1.36134e+06 |
| v1 | chaikin_3_10 | 9240.53 | -759.47 | sell /  / ADL의 EMA3 - EMA10 > 0 그리고 종가 > EMA26; 조건 미충족; Chaikin3_10=-27551.7, ADL=-5.11151e+06, close=711.18, EMA26=734.673 |
| v1 | roc_10_momentum | 9896.73 | -103.27 | sell /  / 10봉 ROC > 1% 그리고 종가 > EMA26; 조건 미충족; ROC10_percent=0.883016, close=741.47, EMA26=734.681 |
| v1 | trix_15_trend | 9340.52 | -659.48 | sell /  / 15봉 삼중 EMA의 1봉 변화율 TRIX > 0 그리고 종가 > EMA26; 조건 미충족; TRIX15_percent=0.0460682, close=711.18, EMA26=734.673 |
| v1 | keltner_20_breakout | 10000.00 | 0.00 | 대기 /  / 새 신호 대기 |
| v1 | opening_range_30m | 10162.22 | 162.22 | sell /  / 뉴욕 09:30·09:45 두 완료 봉 최고가를 10:00 이후 종가가 돌파; 자료 부족·변동폭 또는 거래량 없음: 대기; close=733.16 |
| v2 | cash | 10000.00 | 0.00 | 대기 /  / 새 신호 대기 |
| v2 | buy_hold | 8794.05 | -1205.95 | 중단: 손실 한도 / buy / partial / 직전 완료 봉 목표 비중 100%; 다음 봉 시가 가정 |
| v2 | trend_8_26 | 9409.87 | -590.13 | 중단: 손실 한도 / buy / partial / 직전 완료 봉 목표 비중 100%; 다음 봉 시가 가정 |
| v2 | momentum_26 | 9211.81 | -788.19 | 중단: 손실 한도 / buy / partial / 직전 완료 봉 목표 비중 100%; 다음 봉 시가 가정 |
| v2 | breakout_8 | 9357.29 | -642.71 | sell / filled / 직전 완료 봉 목표 비중 0%; 다음 봉 시가 가정 |
| v2 | reversion_12 | 8671.24 | -1328.76 | 중단: 손실 한도 / buy / partial / 직전 완료 봉 목표 비중 100%; 다음 봉 시가 가정 |
| v2 | volume_26 | 8919.23 | -1080.77 | 중단: 손실 한도 / buy / partial / 직전 완료 봉 목표 비중 100%; 다음 봉 시가 가정 |
| v2 | trend_8_26 AND momentum_26 | 9423.76 | -576.24 | 중단: 손실 한도 / buy / partial / 직전 완료 봉 목표 비중 100%; 다음 봉 시가 가정 |
| v2 | trend_8_26 + momentum_26 | 9311.32 | -688.68 | 중단: 손실 한도 / buy / partial / 직전 완료 봉 목표 비중 100%; 다음 봉 시가 가정 |
| v2 | trend_8_26 AND breakout_8 | 9655.84 | -344.16 | sell / filled / 직전 완료 봉 목표 비중 0%; 다음 봉 시가 가정 |
| v2 | trend_8_26 + breakout_8 | 9426.02 | -573.98 | sell / filled / 직전 완료 봉 목표 비중 0%; 다음 봉 시가 가정 |
| v2 | trend_8_26 AND reversion_12 | 9728.39 | -271.61 | sell / filled / 직전 완료 봉 목표 비중 0%; 다음 봉 시가 가정 |
| v2 | trend_8_26 + reversion_12 | 9315.94 | -684.06 | sell / filled / 직전 완료 봉 목표 비중 0%; 다음 봉 시가 가정 |
| v2 | trend_8_26 AND volume_26 | 9999.01 | -0.99 | sell / filled / 직전 완료 봉 목표 비중 0%; 다음 봉 시가 가정 |
| v2 | trend_8_26 + volume_26 | 9303.04 | -696.96 | 중단: 손실 한도 / sell / filled / 직전 완료 봉 목표 비중 0%; 다음 봉 시가 가정 |
| v2 | momentum_26 AND breakout_8 | 9576.90 | -423.10 | sell / filled / 직전 완료 봉 목표 비중 0%; 다음 봉 시가 가정 |
| v2 | momentum_26 + breakout_8 | 9325.28 | -674.72 | sell / filled / 직전 완료 봉 목표 비중 0%; 다음 봉 시가 가정 |
| v2 | momentum_26 AND reversion_12 | 9745.30 | -254.70 | sell / filled / 직전 완료 봉 목표 비중 0%; 다음 봉 시가 가정 |
| v2 | momentum_26 + reversion_12 | 9177.89 | -822.11 | sell / filled / 직전 완료 봉 목표 비중 0%; 다음 봉 시가 가정 |
| v2 | momentum_26 AND volume_26 | 9936.85 | -63.15 | sell / filled / 직전 완료 봉 목표 비중 0%; 다음 봉 시가 가정 |
| v2 | momentum_26 + volume_26 | 9203.76 | -796.24 | 중단: 손실 한도 / sell / filled / 직전 완료 봉 목표 비중 0%; 다음 봉 시가 가정 |
| v2 | breakout_8 AND reversion_12 | 10000.00 | 0.00 | 대기 /  / 새 신호 대기 |
| v2 | breakout_8 + reversion_12 | 9610.18 | -389.82 | 중단: 손실 한도 / sell / filled / 직전 완료 봉 목표 비중 0%; 다음 봉 시가 가정 |
| v2 | breakout_8 AND volume_26 | 9887.31 | -112.69 | sell / filled / 직전 완료 봉 목표 비중 0%; 다음 봉 시가 가정 |
| v2 | breakout_8 + volume_26 | 9216.53 | -783.47 | sell / filled / 직전 완료 봉 목표 비중 0%; 다음 봉 시가 가정 |
| v2 | reversion_12 AND volume_26 | 8857.53 | -1142.47 | 중단: 손실 한도 / buy / partial / 직전 완료 봉 목표 비중 100%; 다음 봉 시가 가정 |
| v2 | reversion_12 + volume_26 | 9196.25 | -803.75 | 중단: 손실 한도 / sell / filled / 직전 완료 봉 목표 비중 50%; 다음 봉 시가 가정 |
| v2 | ema_12_26 | 9511.86 | -488.14 | 중단: 손실 한도 / buy / partial / EMA12 > EMA26; 조건 충족; EMA12=726.261, EMA26=726.172; 직전 완료 봉 목표를 다음 봉 시가에 모의 적용 |
| v2 | macd_12_26_9 | 9984.52 | -15.48 | sell / filled / MACD > 신호선 그리고 MACD > 0; 조건 미충족; MACD=2.92675, signal9=3.02629; 직전 완료 봉 목표를 다음 봉 시가에 모의 적용 |
| v2 | rsi_14_recovery | 9945.00 | -55.00 | sell / filled / 직전 RSI14 < 30, 현재 RSI14 >= 30 (한 봉 목표); 조건 미충족; RSI14=34.1484, previous_RSI14=34.3526; 직전 완료 봉 목표를 다음 봉 시가에 모의 적용 |
| v2 | bollinger_20_reentry | 9685.73 | -314.27 | sell / filled / 직전 종가 < 직전 하단밴드, 현재 하단밴드 <= 종가 <= SMA20 (한 봉 목표); 조건 미충족; close=698.04, lower20=693.892, SMA20=727.609, previous_lower20=698.501; 직전 완료 봉 목표를 다음 봉 시가에 모의 적용 |
| v2 | donchian_20 | 9939.30 | -60.70 | sell / filled / 종가 > 현재 봉을 제외한 직전 20봉 최고가; 조건 미충족; close=735.35, prior_high20=745; 직전 완료 봉 목표를 다음 봉 시가에 모의 적용 |
| v2 | atr_14_breakout | 9758.55 | -241.45 | sell / filled / 종가 > 직전 종가 + 직전 ATR14 그리고 종가 > EMA26; 조건 미충족; close=735.35, threshold=737.263, prior_ATR14=4.10289, EMA26=727.331; 직전 완료 봉 목표를 다음 봉 시가에 모의 적용 |
| v2 | session_vwap | 9159.53 | -840.47 | 중단: 손실 한도 / buy / partial / 종가 > 뉴욕 거래일별 누적 전형가격 VWAP; 조건 충족; close=734.98, session_VWAP=734.093, session_volume=764353; 직전 완료 봉 목표를 다음 봉 시가에 모의 적용 |
| v2 | obv_20 | 9448.45 | -551.55 | 중단: 손실 한도 / buy / partial / OBV > OBV의 SMA20 그리고 종가 > EMA26; 조건 충족; OBV=-5.0567e+06, OBV_SMA20=-6.30537e+06, close=733.16, EMA26=726.69; 직전 완료 봉 목표를 다음 봉 시가에 모의 적용 |
| v2 | stochastic_14_3_recovery | 9768.17 | -231.83 | sell / filled / 직전 %K14 < 20에서 %K14가 %D3 상향 돌파 (한 봉 목표); 조건 미충족; K14=13.5114, D3=6.65149, previous_K14=5.262, previous_D3=2.35532; 직전 완료 봉 목표를 다음 봉 시가에 모의 적용 |
| v2 | mfi_14_recovery | 10064.61 | 64.61 | sell / filled / 직전 MFI14 < 20, 현재 MFI14 >= 20 (한 봉 목표); 조건 미충족; MFI14=32.7313, previous_MFI14=24.1736; 직전 완료 봉 목표를 다음 봉 시가에 모의 적용 |
| v2 | adx_14_trend | 9530.16 | -469.84 | 중단: 손실 한도 / buy / partial / Wilder ADX14 >= 25 그리고 +DI14 > -DI14; 조건 충족; ADX14=25.4031, plus_DI14=35.2628, minus_DI14=13.9603; 직전 완료 봉 목표를 다음 봉 시가에 모의 적용 |
| v2 | aroon_25_trend | 9973.62 | -26.38 | sell / filled / Aroon25 Up > 70 그리고 Down < 30 (동률이면 최신 극값); 조건 미충족; Aroon_up=68, Aroon_down=20; 직전 완료 봉 목표를 다음 봉 시가에 모의 적용 |
| v2 | cci_20_momentum | 9854.97 | -145.03 | sell / filled / CCI20 > 100 (전형가격·평균절대편차); 조건 미충족; CCI20=99.2123; 직전 완료 봉 목표를 다음 봉 시가에 모의 적용 |
| v2 | williams_14_recovery | 9948.82 | -51.18 | sell / filled / 직전 Williams %R14 < -80, 현재 >= -80 (한 봉 목표); 조건 미충족; Williams_R14=-79.0512, previous_R14=-78.5192; 직전 완료 봉 목표를 다음 봉 시가에 모의 적용 |
| v2 | cmf_20_accumulation | 9368.01 | -631.99 | 중단: 손실 한도 / buy / partial / Chaikin Money Flow20 > 0.1; 조건 충족; CMF20=0.145111, volume20=965726; 직전 완료 봉 목표를 다음 봉 시가에 모의 적용 |
| v2 | chaikin_3_10 | 9261.42 | -738.58 | 중단: 손실 한도 / buy / partial / ADL의 EMA3 - EMA10 > 0 그리고 종가 > EMA26; 조건 충족; Chaikin3_10=293683, ADL=-4.91156e+06, close=739.58, EMA26=736.187; 직전 완료 봉 목표를 다음 봉 시가에 모의 적용 |
| v2 | roc_10_momentum | 9888.81 | -111.19 | sell / filled / 10봉 ROC > 1% 그리고 종가 > EMA26; 조건 미충족; ROC10_percent=0.883016, close=741.47, EMA26=734.681; 직전 완료 봉 목표를 다음 봉 시가에 모의 적용 |
| v2 | trix_15_trend | 9270.75 | -729.25 | 중단: 손실 한도 / buy / partial / 15봉 삼중 EMA의 1봉 변화율 TRIX > 0 그리고 종가 > EMA26; 조건 충족; TRIX15_percent=0.0196284, close=739.58, EMA26=736.187; 직전 완료 봉 목표를 다음 봉 시가에 모의 적용 |
| v2 | keltner_20_breakout | 10000.00 | 0.00 | 대기 /  / 새 신호 대기 |
| v2 | opening_range_30m | 10158.15 | 158.15 | sell / filled / 뉴욕 09:30·09:45 두 완료 봉 최고가를 10:00 이후 종가가 돌파; 자료 부족·변동폭 또는 거래량 없음: 대기; close=733.16; 직전 완료 봉 목표를 다음 봉 시가에 모의 적용 |

### 같은 기간의 비용·노출 비교 (사후 연구)

| 전략 | 비용 전 | 비용 후 | 100% 보유 | 같은 평균 노출 보유 | 평균 노출 |
|---|---:|---:|---:|---:|---:|
| cash | 0.00% | 0.00% | -15.01% | -0.00% | 0.00% |
| buy_hold | -14.65% | -15.01% | -15.01% | -15.01% | 100.00% |
| trend_8_26 | -2.26% | -5.89% | -15.01% | -7.19% | 46.46% |
| momentum_26 | -5.78% | -10.03% | -15.01% | -6.88% | 44.36% |
| breakout_8 | -2.56% | -14.45% | -15.01% | -2.40% | 15.22% |
| reversion_12 | -4.72% | -17.05% | -15.01% | -4.23% | 27.03% |
| volume_26 | -2.47% | -10.70% | -15.01% | -1.37% | 8.66% |
| trend_8_26 AND momentum_26 | -1.67% | -4.92% | -15.01% | -6.12% | 39.37% |
| trend_8_26 + momentum_26 | -4.02% | -7.97% | -15.01% | -7.04% | 45.41% |
| trend_8_26 AND breakout_8 | -1.08% | -7.90% | -15.01% | -1.37% | 8.66% |
| trend_8_26 + breakout_8 | -2.36% | -10.05% | -15.01% | -4.82% | 30.85% |
| trend_8_26 AND reversion_12 | 0.96% | -5.20% | -15.01% | -0.87% | 5.51% |
| trend_8_26 + reversion_12 | -3.41% | -10.67% | -15.01% | -5.72% | 36.75% |
| trend_8_26 AND volume_26 | 2.90% | 1.18% | -15.01% | -0.25% | 1.57% |
| trend_8_26 + volume_26 | -2.29% | -7.71% | -15.01% | -4.31% | 27.56% |
| momentum_26 AND breakout_8 | -1.82% | -9.35% | -15.01% | -1.41% | 8.92% |
| momentum_26 + breakout_8 | -4.14% | -12.24% | -15.01% | -4.66% | 29.80% |
| momentum_26 AND reversion_12 | -2.85% | -8.78% | -15.01% | -1.00% | 6.30% |
| momentum_26 + reversion_12 | -5.19% | -13.40% | -15.01% | -5.56% | 35.70% |
| momentum_26 AND volume_26 | 2.69% | 0.55% | -15.01% | -0.25% | 1.57% |
| momentum_26 + volume_26 | -4.07% | -9.77% | -15.01% | -4.15% | 26.51% |
| breakout_8 AND reversion_12 | 0.00% | 0.00% | -15.01% | -0.00% | 0.00% |
| breakout_8 + reversion_12 | -3.58% | -15.03% | -15.01% | -3.32% | 21.14% |
| breakout_8 AND volume_26 | 0.55% | -1.13% | -15.01% | -0.17% | 1.05% |
| breakout_8 + volume_26 | -2.48% | -12.03% | -15.01% | -1.89% | 11.95% |
| reversion_12 AND volume_26 | -1.80% | -7.02% | -15.01% | -0.87% | 5.51% |
| reversion_12 + volume_26 | -3.56% | -13.56% | -15.01% | -2.81% | 17.85% |
| ema_12_26 | -2.52% | -4.14% | -15.01% | -6.60% | 42.52% |
| macd_12_26_9 | 3.33% | 0.76% | -15.01% | -4.11% | 26.25% |
| rsi_14_recovery | 0.37% | -5.76% | -15.01% | -0.62% | 3.94% |
| bollinger_20_reentry | -0.39% | -5.68% | -15.01% | -0.54% | 3.41% |
| donchian_20 | -0.65% | -3.93% | -15.01% | -0.54% | 3.41% |
| atr_14_breakout | -1.18% | -6.04% | -15.01% | -0.54% | 3.41% |
| session_vwap | -0.99% | -13.08% | -15.01% | -7.43% | 48.03% |
| obv_20 | -4.29% | -13.10% | -15.01% | -3.75% | 23.88% |
| stochastic_14_3_recovery | -1.02% | -11.26% | -15.01% | -1.08% | 6.82% |
| mfi_14_recovery | 2.16% | -0.38% | -15.01% | -0.25% | 1.57% |
| adx_14_trend | -5.42% | -7.77% | -15.01% | -1.99% | 12.60% |
| aroon_25_trend | 0.04% | -3.67% | -15.01% | -1.74% | 11.02% |
| cci_20_momentum | -3.28% | -8.04% | -15.01% | -2.32% | 14.70% |
| williams_14_recovery | 0.33% | -6.97% | -15.01% | -0.75% | 4.72% |
| cmf_20_accumulation | -6.74% | -13.53% | -15.01% | -3.09% | 19.69% |
| chaikin_3_10 | -6.34% | -14.96% | -15.01% | -5.00% | 32.02% |
| roc_10_momentum | -1.46% | -7.08% | -15.01% | -1.91% | 12.07% |
| trix_15_trend | -3.68% | -7.64% | -15.01% | -5.36% | 34.38% |
| keltner_20_breakout | -2.06% | -3.70% | -15.01% | -0.29% | 1.84% |
| opening_range_30m | 7.74% | 3.31% | -15.01% | -3.54% | 22.57% |

동일 구간·초기 자금, 종료 시 청산 비용 포함. 노출 맞춤은 사후 설명용이며 v2 실제 계좌 성과가 아닙니다.
[낙폭 분해·비용 영향·전체 구간](CAT/comparison.json)

[v1 전체 기록](CAT/accounts.json) · [v2 전체 기록](CAT/accounts-v2.json)

## WMT 계좌

| 모델 | 전략 | 평가액 USD | 손익 USD | 최근 매매·이유 |
|---|---|---:|---:|---|
| v1 | cash | 10000.00 | 0.00 | 대기 /  / 새 신호 대기 |
| v1 | buy_hold | 10167.56 | 167.56 | buy /  / buy_hold: prior completed bar target 100%; next bar open simulation |
| v1 | trend_8_26 | 9825.70 | -174.30 | buy /  / trend_8_26: prior completed bar target 100%; next bar open simulation |
| v1 | momentum_26 | 9942.06 | -57.94 | buy /  / momentum_26: prior completed bar target 100%; next bar open simulation |
| v1 | breakout_8 | 9486.99 | -513.01 | buy /  / breakout_8: prior completed bar target 100%; next bar open simulation |
| v1 | reversion_12 | 9573.71 | -426.29 | sell /  / reversion_12: prior completed bar target 0%; next bar open simulation |
| v1 | volume_26 | 9775.35 | -224.65 | sell /  / volume_26: prior completed bar target 0%; next bar open simulation |
| v1 | trend_8_26 AND momentum_26 | 9907.70 | -92.30 | buy /  / trend_8_26 AND momentum_26: prior completed bar target 100%; next bar open simulation |
| v1 | trend_8_26 + momentum_26 | 9883.74 | -116.26 | buy /  / trend_8_26 + momentum_26: prior completed bar target 100%; next bar open simulation |
| v1 | trend_8_26 AND breakout_8 | 9751.02 | -248.98 | buy /  / trend_8_26 AND breakout_8: prior completed bar target 100%; next bar open simulation |
| v1 | trend_8_26 + breakout_8 | 9674.39 | -325.61 | buy /  / trend_8_26 + breakout_8: prior completed bar target 100%; next bar open simulation |
| v1 | trend_8_26 AND reversion_12 | 9741.18 | -258.82 | sell /  / trend_8_26 AND reversion_12: prior completed bar target 0%; next bar open simulation |
| v1 | trend_8_26 + reversion_12 | 9737.91 | -262.09 | sell /  / trend_8_26 + reversion_12: prior completed bar target 50%; next bar open simulation |
| v1 | trend_8_26 AND volume_26 | 9837.96 | -162.04 | sell /  / trend_8_26 AND volume_26: prior completed bar target 0%; next bar open simulation |
| v1 | trend_8_26 + volume_26 | 9800.96 | -199.04 | sell /  / trend_8_26 + volume_26: prior completed bar target 50%; next bar open simulation |
| v1 | momentum_26 AND breakout_8 | 9661.91 | -338.09 | buy /  / momentum_26 AND breakout_8: prior completed bar target 100%; next bar open simulation |
| v1 | momentum_26 + breakout_8 | 9770.72 | -229.28 | buy /  / momentum_26 + breakout_8: prior completed bar target 100%; next bar open simulation |
| v1 | momentum_26 AND reversion_12 | 9935.88 | -64.12 | sell /  / momentum_26 AND reversion_12: prior completed bar target 0%; next bar open simulation |
| v1 | momentum_26 + reversion_12 | 9854.17 | -145.83 | sell /  / momentum_26 + reversion_12: prior completed bar target 50%; next bar open simulation |
| v1 | momentum_26 AND volume_26 | 9853.50 | -146.50 | sell /  / momentum_26 AND volume_26: prior completed bar target 0%; next bar open simulation |
| v1 | momentum_26 + volume_26 | 9898.29 | -101.71 | sell /  / momentum_26 + volume_26: prior completed bar target 50%; next bar open simulation |
| v1 | breakout_8 AND reversion_12 | 10000.00 | 0.00 | 대기 /  / 새 신호 대기 |
| v1 | breakout_8 + reversion_12 | 9568.24 | -431.76 | sell /  / breakout_8 + reversion_12: prior completed bar target 50%; next bar open simulation |
| v1 | breakout_8 AND volume_26 | 9797.95 | -202.05 | sell /  / breakout_8 AND volume_26: prior completed bar target 0%; next bar open simulation |
| v1 | breakout_8 + volume_26 | 9630.33 | -369.67 | sell /  / breakout_8 + volume_26: prior completed bar target 50%; next bar open simulation |
| v1 | reversion_12 AND volume_26 | 9911.53 | -88.47 | sell /  / reversion_12 AND volume_26: prior completed bar target 0%; next bar open simulation |
| v1 | reversion_12 + volume_26 | 9732.36 | -267.64 | sell /  / reversion_12 + volume_26: prior completed bar target 0%; next bar open simulation |
| v1 | ema_12_26 | 10046.63 | 46.63 | buy /  / EMA12 > EMA26; 조건 충족; EMA12=117.957, EMA26=117.935 |
| v1 | macd_12_26_9 | 10126.63 | 126.63 | buy /  / MACD > 신호선 그리고 MACD > 0; 조건 충족; MACD=0.0217894, signal9=-0.0690006 |
| v1 | rsi_14_recovery | 9973.19 | -26.81 | sell /  / 직전 RSI14 < 30, 현재 RSI14 >= 30 (한 봉 목표); 조건 미충족; RSI14=46.7246, previous_RSI14=43.1348 |
| v1 | bollinger_20_reentry | 9975.54 | -24.46 | sell /  / 직전 종가 < 직전 하단밴드, 현재 하단밴드 <= 종가 <= SMA20 (한 봉 목표); 조건 미충족; close=117.73, lower20=117.465, SMA20=117.829, previous_lower20=117.475 |
| v1 | donchian_20 | 9784.71 | -215.29 | buy /  / 종가 > 현재 봉을 제외한 직전 20봉 최고가; 조건 충족; close=120.48, prior_high20=120.23 |
| v1 | atr_14_breakout | 9811.78 | -188.22 | sell /  / 종가 > 직전 종가 + 직전 ATR14 그리고 종가 > EMA26; 조건 미충족; close=120.03, threshold=120.128, prior_ATR14=0.443028, EMA26=118.335 |
| v1 | session_vwap | 9642.21 | -357.79 | buy /  / 종가 > 뉴욕 거래일별 누적 전형가격 VWAP; 조건 충족; close=118.96, session_VWAP=118.576, session_volume=4.484e+06 |
| v1 | obv_20 | 9999.11 | -0.89 | buy /  / OBV > OBV의 SMA20 그리고 종가 > EMA26; 조건 충족; OBV=1.42093e+07, OBV_SMA20=1.04391e+07, close=118.41, EMA26=117.87 |
| v1 | stochastic_14_3_recovery | 9463.72 | -536.28 | sell /  / 직전 %K14 < 20에서 %K14가 %D3 상향 돌파 (한 봉 목표); 조건 미충족; K14=38.3112, D3=17.7755, previous_K14=8.66597, previous_D3=7.09962 |
| v1 | mfi_14_recovery | 9969.08 | -30.92 | sell /  / 직전 MFI14 < 20, 현재 MFI14 >= 20 (한 봉 목표); 조건 미충족; MFI14=57.3162, previous_MFI14=36.5877 |
| v1 | adx_14_trend | 10135.12 | 135.12 | buy /  / Wilder ADX14 >= 25 그리고 +DI14 > -DI14; 조건 충족; ADX14=32.9742, plus_DI14=41.4463, minus_DI14=15.2475 |
| v1 | aroon_25_trend | 9954.43 | -45.57 | sell /  / Aroon25 Up > 70 그리고 Down < 30 (동률이면 최신 극값); 조건 미충족; Aroon_up=84, Aroon_down=76 |
| v1 | cci_20_momentum | 9831.19 | -168.81 | buy /  / CCI20 > 100 (전형가격·평균절대편차); 조건 충족; CCI20=227.859 |
| v1 | williams_14_recovery | 9739.33 | -260.67 | sell /  / 직전 Williams %R14 < -80, 현재 >= -80 (한 봉 목표); 조건 미충족; Williams_R14=-50.649, previous_R14=-61.6888 |
| v1 | cmf_20_accumulation | 9764.65 | -235.35 | buy /  / Chaikin Money Flow20 > 0.1; 조건 충족; CMF20=0.134813, volume20=1.25189e+07 |
| v1 | chaikin_3_10 | 9755.63 | -244.37 | buy /  / ADL의 EMA3 - EMA10 > 0 그리고 종가 > EMA26; 조건 충족; Chaikin3_10=239030, ADL=8.86177e+06, close=118.96, EMA26=118.011 |
| v1 | roc_10_momentum | 10097.90 | 97.90 | buy /  / 10봉 ROC > 1% 그리고 종가 > EMA26; 조건 충족; ROC10_percent=1.0791, close=118.96, EMA26=118.011 |
| v1 | trix_15_trend | 9743.09 | -256.91 | buy /  / 15봉 삼중 EMA의 1봉 변화율 TRIX > 0 그리고 종가 > EMA26; 조건 충족; TRIX15_percent=0.00531527, close=119.685, EMA26=118.199 |
| v1 | keltner_20_breakout | 10033.25 | 33.25 | buy /  / 종가 > EMA20 + 2 x Wilder ATR14; 조건 충족; close=118.96, upper_Keltner=118.84, EMA20=118.021, ATR14=0.409337 |
| v1 | opening_range_30m | 9820.56 | -179.44 | buy /  / 뉴욕 09:30·09:45 두 완료 봉 최고가를 10:00 이후 종가가 돌파; 조건 충족; close=119.685, opening_high=119.42 |
| v2 | cash | 10000.00 | 0.00 | 대기 /  / 새 신호 대기 |
| v2 | buy_hold | 10772.43 | 772.43 | buy / partial / 직전 완료 봉 목표 비중 100%; 다음 봉 시가 가정 |
| v2 | trend_8_26 | 10219.96 | 219.96 | buy / partial / 직전 완료 봉 목표 비중 100%; 다음 봉 시가 가정 |
| v2 | momentum_26 | 10345.90 | 345.90 | buy / partial / 직전 완료 봉 목표 비중 100%; 다음 봉 시가 가정 |
| v2 | breakout_8 | 9429.85 | -570.15 | buy / partial / 직전 완료 봉 목표 비중 100%; 다음 봉 시가 가정 |
| v2 | reversion_12 | 9466.17 | -533.83 | sell / filled / 직전 완료 봉 목표 비중 0%; 다음 봉 시가 가정 |
| v2 | volume_26 | 9727.78 | -272.22 | sell / filled / 직전 완료 봉 목표 비중 0%; 다음 봉 시가 가정 |
| v2 | trend_8_26 AND momentum_26 | 10305.25 | 305.25 | buy / partial / 직전 완료 봉 목표 비중 100%; 다음 봉 시가 가정 |
| v2 | trend_8_26 + momentum_26 | 10282.71 | 282.71 | buy / partial / 직전 완료 봉 목표 비중 100%; 다음 봉 시가 가정 |
| v2 | trend_8_26 AND breakout_8 | 9824.59 | -175.41 | buy / partial / 직전 완료 봉 목표 비중 100%; 다음 봉 시가 가정 |
| v2 | trend_8_26 + breakout_8 | 9838.18 | -161.82 | buy / partial / 직전 완료 봉 목표 비중 100%; 다음 봉 시가 가정 |
| v2 | trend_8_26 AND reversion_12 | 9545.32 | -454.68 | sell / filled / 직전 완료 봉 목표 비중 0%; 다음 봉 시가 가정 |
| v2 | trend_8_26 + reversion_12 | 9878.77 | -121.23 | sell / filled / 직전 완료 봉 목표 비중 50%; 다음 봉 시가 가정 |
| v2 | trend_8_26 AND volume_26 | 9784.10 | -215.90 | sell / filled / 직전 완료 봉 목표 비중 0%; 다음 봉 시가 가정 |
| v2 | trend_8_26 + volume_26 | 9972.71 | -27.29 | sell / filled / 직전 완료 봉 목표 비중 50%; 다음 봉 시가 가정 |
| v2 | momentum_26 AND breakout_8 | 9611.40 | -388.60 | buy / partial / 직전 완료 봉 목표 비중 100%; 다음 봉 시가 가정 |
| v2 | momentum_26 + breakout_8 | 9940.49 | -59.51 | buy / partial / 직전 완료 봉 목표 비중 100%; 다음 봉 시가 가정 |
| v2 | momentum_26 AND reversion_12 | 9759.91 | -240.09 | sell / filled / 직전 완료 봉 목표 비중 0%; 다음 봉 시가 가정 |
| v2 | momentum_26 + reversion_12 | 10044.24 | 44.24 | sell / filled / 직전 완료 봉 목표 비중 50%; 다음 봉 시가 가정 |
| v2 | momentum_26 AND volume_26 | 9760.78 | -239.22 | sell / filled / 직전 완료 봉 목표 비중 0%; 다음 봉 시가 가정 |
| v2 | momentum_26 + volume_26 | 10076.20 | 76.20 | sell / filled / 직전 완료 봉 목표 비중 50%; 다음 봉 시가 가정 |
| v2 | breakout_8 AND reversion_12 | 10000.00 | 0.00 | 대기 /  / 새 신호 대기 |
| v2 | breakout_8 + reversion_12 | 9508.55 | -491.45 | sell / filled / 직전 완료 봉 목표 비중 50%; 다음 봉 시가 가정 |
| v2 | breakout_8 AND volume_26 | 9741.39 | -258.61 | sell / filled / 직전 완료 봉 목표 비중 0%; 다음 봉 시가 가정 |
| v2 | breakout_8 + volume_26 | 9579.20 | -420.80 | sell / filled / 직전 완료 봉 목표 비중 50%; 다음 봉 시가 가정 |
| v2 | reversion_12 AND volume_26 | 9917.25 | -82.75 | sell / filled / 직전 완료 봉 목표 비중 0%; 다음 봉 시가 가정 |
| v2 | reversion_12 + volume_26 | 9656.74 | -343.26 | sell / filled / 직전 완료 봉 목표 비중 0%; 다음 봉 시가 가정 |
| v2 | ema_12_26 | 10041.61 | 41.61 | buy / partial / EMA12 > EMA26; 조건 충족; EMA12=117.957, EMA26=117.935; 직전 완료 봉 목표를 다음 봉 시가에 모의 적용 |
| v2 | macd_12_26_9 | 10121.57 | 121.57 | buy / partial / MACD > 신호선 그리고 MACD > 0; 조건 충족; MACD=0.0217894, signal9=-0.0690006; 직전 완료 봉 목표를 다음 봉 시가에 모의 적용 |
| v2 | rsi_14_recovery | 9971.19 | -28.81 | sell / filled / 직전 RSI14 < 30, 현재 RSI14 >= 30 (한 봉 목표); 조건 미충족; RSI14=46.7246, previous_RSI14=43.1348; 직전 완료 봉 목표를 다음 봉 시가에 모의 적용 |
| v2 | bollinger_20_reentry | 9967.56 | -32.44 | sell / filled / 직전 종가 < 직전 하단밴드, 현재 하단밴드 <= 종가 <= SMA20 (한 봉 목표); 조건 미충족; close=117.73, lower20=117.465, SMA20=117.829, previous_lower20=117.475; 직전 완료 봉 목표를 다음 봉 시가에 모의 적용 |
| v2 | donchian_20 | 9775.91 | -224.09 | buy / partial / 종가 > 현재 봉을 제외한 직전 20봉 최고가; 조건 충족; close=120.48, prior_high20=120.23; 직전 완료 봉 목표를 다음 봉 시가에 모의 적용 |
| v2 | atr_14_breakout | 9801.98 | -198.02 | sell / filled / 종가 > 직전 종가 + 직전 ATR14 그리고 종가 > EMA26; 조건 미충족; close=120.03, threshold=120.128, prior_ATR14=0.443028, EMA26=118.335; 직전 완료 봉 목표를 다음 봉 시가에 모의 적용 |
| v2 | session_vwap | 9621.98 | -378.02 | buy / partial / 종가 > 뉴욕 거래일별 누적 전형가격 VWAP; 조건 충족; close=118.96, session_VWAP=118.576, session_volume=4.484e+06; 직전 완료 봉 목표를 다음 봉 시가에 모의 적용 |
| v2 | obv_20 | 9988.12 | -11.88 | buy / partial / OBV > OBV의 SMA20 그리고 종가 > EMA26; 조건 충족; OBV=1.42093e+07, OBV_SMA20=1.04391e+07, close=118.41, EMA26=117.87; 직전 완료 봉 목표를 다음 봉 시가에 모의 적용 |
| v2 | stochastic_14_3_recovery | 9865.79 | -134.21 | 중단: 손실 한도 / buy / partial / 직전 %K14 < 20에서 %K14가 %D3 상향 돌파 (한 봉 목표); 조건 충족; K14=25.6758, D3=22.4971, previous_K14=12.8379, previous_D3=25.8704; 직전 완료 봉 목표를 다음 봉 시가에 모의 적용 |
| v2 | mfi_14_recovery | 9961.11 | -38.89 | sell / filled / 직전 MFI14 < 20, 현재 MFI14 >= 20 (한 봉 목표); 조건 미충족; MFI14=57.3162, previous_MFI14=36.5877; 직전 완료 봉 목표를 다음 봉 시가에 모의 적용 |
| v2 | adx_14_trend | 10132.08 | 132.08 | buy / partial / Wilder ADX14 >= 25 그리고 +DI14 > -DI14; 조건 충족; ADX14=32.9742, plus_DI14=41.4463, minus_DI14=15.2475; 직전 완료 봉 목표를 다음 봉 시가에 모의 적용 |
| v2 | aroon_25_trend | 9948.46 | -51.54 | sell / filled / Aroon25 Up > 70 그리고 Down < 30 (동률이면 최신 극값); 조건 미충족; Aroon_up=84, Aroon_down=76; 직전 완료 봉 목표를 다음 봉 시가에 모의 적용 |
| v2 | cci_20_momentum | 9822.35 | -177.65 | buy / partial / CCI20 > 100 (전형가격·평균절대편차); 조건 충족; CCI20=227.859; 직전 완료 봉 목표를 다음 봉 시가에 모의 적용 |
| v2 | williams_14_recovery | 9725.71 | -274.29 | sell / filled / 직전 Williams %R14 < -80, 현재 >= -80 (한 봉 목표); 조건 미충족; Williams_R14=-50.649, previous_R14=-61.6888; 직전 완료 봉 목표를 다음 봉 시가에 모의 적용 |
| v2 | cmf_20_accumulation | 9751.97 | -248.03 | buy / partial / Chaikin Money Flow20 > 0.1; 조건 충족; CMF20=0.134813, volume20=1.25189e+07; 직전 완료 봉 목표를 다음 봉 시가에 모의 적용 |
| v2 | chaikin_3_10 | 9737.11 | -262.89 | buy / partial / ADL의 EMA3 - EMA10 > 0 그리고 종가 > EMA26; 조건 충족; Chaikin3_10=239030, ADL=8.86177e+06, close=118.96, EMA26=118.011; 직전 완료 봉 목표를 다음 봉 시가에 모의 적용 |
| v2 | roc_10_momentum | 10096.89 | 96.89 | buy / partial / 10봉 ROC > 1% 그리고 종가 > EMA26; 조건 충족; ROC10_percent=1.0791, close=118.96, EMA26=118.011; 직전 완료 봉 목표를 다음 봉 시가에 모의 적용 |
| v2 | trix_15_trend | 9730.43 | -269.57 | buy / partial / 15봉 삼중 EMA의 1봉 변화율 TRIX > 0 그리고 종가 > EMA26; 조건 충족; TRIX15_percent=0.00531527, close=119.685, EMA26=118.199; 직전 완료 봉 목표를 다음 봉 시가에 모의 적용 |
| v2 | keltner_20_breakout | 10030.24 | 30.24 | buy / partial / 종가 > EMA20 + 2 x Wilder ATR14; 조건 충족; close=118.96, upper_Keltner=118.84, EMA20=118.021, ATR14=0.409337; 직전 완료 봉 목표를 다음 봉 시가에 모의 적용 |
| v2 | opening_range_30m | 9811.73 | -188.27 | buy / partial / 뉴욕 09:30·09:45 두 완료 봉 최고가를 10:00 이후 종가가 돌파; 조건 충족; close=119.685, opening_high=119.42; 직전 완료 봉 목표를 다음 봉 시가에 모의 적용 |

### 같은 기간의 비용·노출 비교 (사후 연구)

| 전략 | 비용 전 | 비용 후 | 100% 보유 | 같은 평균 노출 보유 | 평균 노출 |
|---|---:|---:|---:|---:|---:|
| cash | 0.00% | 0.00% | 14.44% | 0.00% | 0.00% |
| buy_hold | 14.92% | 14.44% | 14.44% | 14.44% | 100.00% |
| trend_8_26 | 9.99% | 5.91% | 14.44% | 9.86% | 69.82% |
| momentum_26 | 12.63% | 7.09% | 14.44% | 10.29% | 72.70% |
| breakout_8 | 6.56% | -11.05% | 14.44% | 3.70% | 27.03% |
| reversion_12 | 3.96% | -6.80% | 14.44% | 2.50% | 18.37% |
| volume_26 | 2.19% | -4.05% | 14.44% | 0.81% | 6.04% |
| trend_8_26 AND momentum_26 | 10.30% | 5.76% | 14.44% | 9.09% | 64.57% |
| trend_8_26 + momentum_26 | 11.31% | 6.50% | 14.44% | 10.08% | 71.26% |
| trend_8_26 AND breakout_8 | 7.02% | -7.22% | 14.44% | 3.08% | 22.57% |
| trend_8_26 + breakout_8 | 8.28% | -2.72% | 14.44% | 6.73% | 48.43% |
| trend_8_26 AND reversion_12 | 0.03% | -5.68% | 14.44% | 0.96% | 7.09% |
| trend_8_26 + reversion_12 | 6.97% | -0.00% | 14.44% | 6.11% | 44.10% |
| trend_8_26 AND volume_26 | 0.24% | -2.26% | 14.44% | 0.28% | 2.10% |
| trend_8_26 + volume_26 | 6.06% | 1.25% | 14.44% | 5.23% | 37.93% |
| momentum_26 AND breakout_8 | 6.85% | -8.91% | 14.44% | 3.41% | 24.93% |
| momentum_26 + breakout_8 | 9.57% | -1.77% | 14.44% | 6.94% | 49.87% |
| momentum_26 AND reversion_12 | 1.65% | -4.16% | 14.44% | 0.99% | 7.35% |
| momentum_26 + reversion_12 | 8.25% | 2.04% | 14.44% | 6.32% | 45.54% |
| momentum_26 AND volume_26 | 1.51% | -3.07% | 14.44% | 0.42% | 3.15% |
| momentum_26 + volume_26 | 7.33% | 1.81% | 14.44% | 5.44% | 39.37% |
| breakout_8 AND reversion_12 | 0.00% | 0.00% | 14.44% | 0.00% | 0.00% |
| breakout_8 + reversion_12 | 5.28% | -8.17% | 14.44% | 3.10% | 22.71% |
| breakout_8 AND volume_26 | 0.64% | -2.68% | 14.44% | 0.32% | 2.36% |
| breakout_8 + volume_26 | 4.38% | -7.41% | 14.44% | 2.25% | 16.54% |
| reversion_12 AND volume_26 | 0.01% | -2.48% | 14.44% | 0.25% | 1.84% |
| reversion_12 + volume_26 | 3.08% | -4.64% | 14.44% | 1.65% | 12.21% |
| ema_12_26 | 13.00% | 11.12% | 14.44% | 10.72% | 75.59% |
| macd_12_26_9 | 10.42% | 5.88% | 14.44% | 5.40% | 39.11% |
| rsi_14_recovery | 0.20% | -0.64% | 14.44% | 0.07% | 0.52% |
| bollinger_20_reentry | 2.64% | -0.34% | 14.44% | 0.25% | 1.84% |
| donchian_20 | 4.48% | -8.66% | 14.44% | 1.89% | 13.91% |
| atr_14_breakout | -0.69% | -10.96% | 14.44% | 1.06% | 7.87% |
| session_vwap | 9.33% | -2.39% | 14.44% | 8.20% | 58.53% |
| obv_20 | 12.67% | 4.91% | 14.44% | 8.24% | 58.79% |
| stochastic_14_3_recovery | 0.13% | -8.71% | 14.44% | 0.78% | 5.77% |
| mfi_14_recovery | 1.30% | -0.39% | 14.44% | 0.14% | 1.05% |
| adx_14_trend | 10.51% | 7.76% | 14.44% | 7.44% | 53.28% |
| aroon_25_trend | 7.58% | 2.29% | 14.44% | 4.36% | 31.76% |
| cci_20_momentum | 7.59% | -1.50% | 14.44% | 4.77% | 34.65% |
| williams_14_recovery | 0.89% | -7.63% | 14.44% | 0.74% | 5.51% |
| cmf_20_accumulation | 9.41% | 0.17% | 14.44% | 5.70% | 41.21% |
| chaikin_3_10 | 10.87% | 1.08% | 14.44% | 7.63% | 54.59% |
| roc_10_momentum | 0.89% | -4.07% | 14.44% | 2.25% | 16.54% |
| trix_15_trend | 11.59% | 7.00% | 14.44% | 9.43% | 66.93% |
| keltner_20_breakout | 7.85% | 0.84% | 14.44% | 3.99% | 29.13% |
| opening_range_30m | 10.34% | 4.04% | 14.44% | 5.44% | 39.37% |

동일 구간·초기 자금, 종료 시 청산 비용 포함. 노출 맞춤은 사후 설명용이며 v2 실제 계좌 성과가 아닙니다.
[낙폭 분해·비용 영향·전체 구간](WMT/comparison.json)

[v1 전체 기록](WMT/accounts.json) · [v2 전체 기록](WMT/accounts-v2.json)
