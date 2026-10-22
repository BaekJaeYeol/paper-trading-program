# 모의투자 운영 현황

[PC·서버 장애 진단과 복구 방법](https://github.com/BaekJaeYeol/paper-trading-program/blob/main/investment-lab/docs/failure-recovery.md)

이번 실행 복구: {}

완료 봉 확인 주기: 기록 1/9회 · 기록 없는 예정 8회 · 아직 판정 전 17회 · 주의: 예약 시작 지연 또는 실행·저장 누락을 확인하세요.

[주기 판정 기준](https://github.com/BaekJaeYeol/paper-trading-program/blob/main/investment-lab/docs/session-coverage.md)

최근 확인: 2026-10-22T15:55:13.529186+00:00 (UTC)
다음 15분 확인 목표 (세션 실행 중에만 적용): 2026-10-22T16:07:00+00:00 (UTC, 실행 지연 가능)

실제 주문 없음. v1 기존 계좌와 v2 새 계좌의 시작일이 다르므로 수익률을 직접 우열 비교하지 마세요.
v2는 다음 봉 시가에 비용·스프레드·직전 거래량 제한을 적용한 가상 체결입니다. 미체결 잔량은 만료됩니다.

| 종목 | 상태 | 최근 성공 UTC | 마지막 완료 봉 UTC | 이번 새 봉 |
|---|---|---|---|---|
| SPY | 새 데이터 없음 / 장중 | 2026-10-22T15:55:13.529186+00:00 | 2026-10-22T15:30:00+00:00 | 0 |
| QQQ | 새 데이터 없음 / 장중 | 2026-10-22T15:55:13.529186+00:00 | 2026-10-22T15:30:00+00:00 | 0 |
| IWM | 새 데이터 없음 / 장중 | 2026-10-22T15:55:13.529186+00:00 | 2026-10-22T15:30:00+00:00 | 0 |
| DIA | 새 데이터 없음 / 장중 | 2026-10-22T15:55:13.529186+00:00 | 2026-10-22T15:30:00+00:00 | 0 |
| MSFT | 새 데이터 없음 / 장중 | 2026-10-22T15:55:13.529186+00:00 | 2026-10-22T15:30:00+00:00 | 0 |
| JPM | 새 데이터 없음 / 장중 | 2026-10-22T15:55:13.529186+00:00 | 2026-10-22T15:30:00+00:00 | 0 |
| XOM | 새 데이터 없음 / 장중 | 2026-10-22T15:55:13.529186+00:00 | 2026-10-22T15:30:00+00:00 | 0 |
| JNJ | 새 데이터 없음 / 장중 | 2026-10-22T15:55:13.529186+00:00 | 2026-10-22T15:30:00+00:00 | 0 |
| CAT | 새 데이터 없음 / 장중 | 2026-10-22T15:55:13.529186+00:00 | 2026-10-22T15:30:00+00:00 | 0 |
| WMT | 새 데이터 없음 / 장중 | 2026-10-22T15:55:13.529186+00:00 | 2026-10-22T15:30:00+00:00 | 0 |

이번 실행 소요: 16.19초
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
| v1 | buy_hold | 9850.90 | -149.10 | buy /  / buy_hold: prior completed bar target 100%; next bar open simulation |
| v1 | trend_8_26 | 9711.09 | -288.91 | sell /  / trend_8_26: prior completed bar target 0%; next bar open simulation |
| v1 | momentum_26 | 9631.54 | -368.46 | sell /  / momentum_26: prior completed bar target 0%; next bar open simulation |
| v1 | breakout_8 | 9568.88 | -431.12 | sell /  / breakout_8: prior completed bar target 0%; next bar open simulation |
| v1 | reversion_12 | 9619.35 | -380.65 | sell /  / reversion_12: prior completed bar target 0%; next bar open simulation |
| v1 | volume_26 | 9491.23 | -508.77 | buy /  / volume_26: prior completed bar target 100%; next bar open simulation |
| v1 | trend_8_26 AND momentum_26 | 9624.28 | -375.72 | sell /  / trend_8_26 AND momentum_26: prior completed bar target 0%; next bar open simulation |
| v1 | trend_8_26 + momentum_26 | 9671.22 | -328.78 | sell /  / trend_8_26 + momentum_26: prior completed bar target 0%; next bar open simulation |
| v1 | trend_8_26 AND breakout_8 | 9730.71 | -269.29 | sell /  / trend_8_26 AND breakout_8: prior completed bar target 0%; next bar open simulation |
| v1 | trend_8_26 + breakout_8 | 9678.32 | -321.68 | sell /  / trend_8_26 + breakout_8: prior completed bar target 0%; next bar open simulation |
| v1 | trend_8_26 AND reversion_12 | 9736.23 | -263.77 | sell /  / trend_8_26 AND reversion_12: prior completed bar target 0%; next bar open simulation |
| v1 | trend_8_26 + reversion_12 | 9664.97 | -335.03 | sell /  / trend_8_26 + reversion_12: prior completed bar target 0%; next bar open simulation |
| v1 | trend_8_26 AND volume_26 | 9605.36 | -394.64 | sell /  / trend_8_26 AND volume_26: prior completed bar target 0%; next bar open simulation |
| v1 | trend_8_26 + volume_26 | 9600.45 | -399.55 | buy /  / trend_8_26 + volume_26: prior completed bar target 50%; next bar open simulation |
| v1 | momentum_26 AND breakout_8 | 9640.01 | -359.99 | sell /  / momentum_26 AND breakout_8: prior completed bar target 0%; next bar open simulation |
| v1 | momentum_26 + breakout_8 | 9600.21 | -399.79 | sell /  / momentum_26 + breakout_8: prior completed bar target 0%; next bar open simulation |
| v1 | momentum_26 AND reversion_12 | 9769.70 | -230.30 | sell /  / momentum_26 AND reversion_12: prior completed bar target 0%; next bar open simulation |
| v1 | momentum_26 + reversion_12 | 9683.27 | -316.73 | sell /  / momentum_26 + reversion_12: prior completed bar target 0%; next bar open simulation |
| v1 | momentum_26 AND volume_26 | 9618.73 | -381.27 | sell /  / momentum_26 AND volume_26: prior completed bar target 0%; next bar open simulation |
| v1 | momentum_26 + volume_26 | 9561.05 | -438.95 | buy /  / momentum_26 + volume_26: prior completed bar target 50%; next bar open simulation |
| v1 | breakout_8 AND reversion_12 | 10000.00 | 0.00 | 대기 /  / 새 신호 대기 |
| v1 | breakout_8 + reversion_12 | 9593.73 | -406.27 | sell /  / breakout_8 + reversion_12: prior completed bar target 0%; next bar open simulation |
| v1 | breakout_8 AND volume_26 | 9837.59 | -162.41 | sell /  / breakout_8 AND volume_26: prior completed bar target 0%; next bar open simulation |
| v1 | breakout_8 + volume_26 | 9567.92 | -432.08 | buy /  / breakout_8 + volume_26: prior completed bar target 50%; next bar open simulation |
| v1 | reversion_12 AND volume_26 | 9811.81 | -188.19 | sell /  / reversion_12 AND volume_26: prior completed bar target 0%; next bar open simulation |
| v1 | reversion_12 + volume_26 | 9573.98 | -426.02 | sell /  / reversion_12 + volume_26: prior completed bar target 50%; next bar open simulation |
| v1 | ema_12_26 | 9742.51 | -257.49 | sell /  / EMA12 > EMA26; 조건 미충족; EMA12=771.277, EMA26=771.539 |
| v1 | macd_12_26_9 | 9769.55 | -230.45 | sell /  / MACD > 신호선 그리고 MACD > 0; 조건 미충족; MACD=1.03945, signal9=1.12358 |
| v1 | rsi_14_recovery | 9841.16 | -158.84 | sell /  / 직전 RSI14 < 30, 현재 RSI14 >= 30 (한 봉 목표); 조건 미충족; RSI14=28.3968, previous_RSI14=31.7649 |
| v1 | bollinger_20_reentry | 9787.44 | -212.56 | sell /  / 직전 종가 < 직전 하단밴드, 현재 하단밴드 <= 종가 <= SMA20 (한 봉 목표); 조건 미충족; close=762.71, lower20=761.42, SMA20=770.302, previous_lower20=762.585 |
| v1 | donchian_20 | 9818.08 | -181.92 | sell /  / 종가 > 현재 봉을 제외한 직전 20봉 최고가; 조건 미충족; close=774.19, prior_high20=774.44 |
| v1 | atr_14_breakout | 9816.89 | -183.11 | sell /  / 종가 > 직전 종가 + 직전 ATR14 그리고 종가 > EMA26; 조건 미충족; close=773.07, threshold=774.291, prior_ATR14=1.05565, EMA26=772.249 |
| v1 | session_vwap | 9523.68 | -476.32 | sell /  / 종가 > 뉴욕 거래일별 누적 전형가격 VWAP; 조건 미충족; close=765.69, session_VWAP=766.586, session_volume=7.58519e+06 |
| v1 | obv_20 | 9597.93 | -402.07 | sell /  / OBV > OBV의 SMA20 그리고 종가 > EMA26; 조건 미충족; OBV=-949325, OBV_SMA20=-1.03221e+07, close=766.62, EMA26=771.893 |
| v1 | stochastic_14_3_recovery | 9643.80 | -356.20 | buy /  / 직전 %K14 < 20에서 %K14가 %D3 상향 돌파 (한 봉 목표); 조건 충족; K14=10.9938, D3=8.71605, previous_K14=4.94364, previous_D3=6.32113 |
| v1 | mfi_14_recovery | 9810.25 | -189.75 | sell /  / 직전 MFI14 < 20, 현재 MFI14 >= 20 (한 봉 목표); 조건 미충족; MFI14=24.2496, previous_MFI14=22.3876 |
| v1 | adx_14_trend | 9981.96 | -18.04 | sell /  / Wilder ADX14 >= 25 그리고 +DI14 > -DI14; 조건 미충족; ADX14=24.2312, plus_DI14=28.3519, minus_DI14=24.6578 |
| v1 | aroon_25_trend | 9728.66 | -271.34 | sell /  / Aroon25 Up > 70 그리고 Down < 30 (동률이면 최신 극값); 조건 미충족; Aroon_up=72, Aroon_down=100 |
| v1 | cci_20_momentum | 9766.23 | -233.77 | sell /  / CCI20 > 100 (전형가격·평균절대편차); 조건 미충족; CCI20=97.3932 |
| v1 | williams_14_recovery | 9648.56 | -351.44 | sell /  / 직전 Williams %R14 < -80, 현재 >= -80 (한 봉 목표); 조건 미충족; Williams_R14=-30.1254, previous_R14=-70.5002 |
| v1 | cmf_20_accumulation | 9725.70 | -274.30 | sell /  / Chaikin Money Flow20 > 0.1; 조건 미충족; CMF20=0.0565798, volume20=6.40332e+07 |
| v1 | chaikin_3_10 | 9565.38 | -434.62 | sell /  / ADL의 EMA3 - EMA10 > 0 그리고 종가 > EMA26; 조건 미충족; Chaikin3_10=1.08024e+06, ADL=4.99714e+07, close=766.62, EMA26=771.893 |
| v1 | roc_10_momentum | 9953.42 | -46.58 | sell /  / 10봉 ROC > 1% 그리고 종가 > EMA26; 조건 미충족; ROC10_percent=0.806376, close=769.45, EMA26=767.181 |
| v1 | trix_15_trend | 9489.99 | -510.01 | sell /  / 15봉 삼중 EMA의 1봉 변화율 TRIX > 0 그리고 종가 > EMA26; 조건 미충족; TRIX15_percent=0.0154379, close=766.62, EMA26=771.893 |
| v1 | keltner_20_breakout | 9810.90 | -189.10 | sell /  / 종가 > EMA20 + 2 x Wilder ATR14; 조건 미충족; close=774.19, upper_Keltner=774.31, EMA20=772.615, ATR14=0.847257 |
| v1 | opening_range_30m | 9651.00 | -349.00 | sell /  / 뉴욕 09:30·09:45 두 완료 봉 최고가를 10:00 이후 종가가 돌파; 자료 부족·변동폭 또는 거래량 없음: 대기; close=766.62 |
| v2 | cash | 10000.00 | 0.00 | 대기 /  / 새 신호 대기 |
| v2 | buy_hold | 9779.84 | -220.16 | buy / partial / 직전 완료 봉 목표 비중 100%; 다음 봉 시가 가정 |
| v2 | trend_8_26 | 9591.24 | -408.76 | sell / filled / 직전 완료 봉 목표 비중 0%; 다음 봉 시가 가정 |
| v2 | momentum_26 | 9482.22 | -517.78 | sell / filled / 직전 완료 봉 목표 비중 0%; 다음 봉 시가 가정 |
| v2 | breakout_8 | 9164.60 | -835.40 | sell / filled / 직전 완료 봉 목표 비중 0%; 다음 봉 시가 가정 |
| v2 | reversion_12 | 9154.53 | -845.47 | sell / filled / 직전 완료 봉 목표 비중 0%; 다음 봉 시가 가정 |
| v2 | volume_26 | 8990.07 | -1009.93 | 중단: 손실 한도 / buy / partial / 직전 완료 봉 목표 비중 100%; 다음 봉 시가 가정 |
| v2 | trend_8_26 AND momentum_26 | 9481.53 | -518.47 | sell / filled / 직전 완료 봉 목표 비중 0%; 다음 봉 시가 가정 |
| v2 | trend_8_26 + momentum_26 | 9536.57 | -463.43 | sell / filled / 직전 완료 봉 목표 비중 0%; 다음 봉 시가 가정 |
| v2 | trend_8_26 AND breakout_8 | 9547.25 | -452.75 | sell / filled / 직전 완료 봉 목표 비중 0%; 다음 봉 시가 가정 |
| v2 | trend_8_26 + breakout_8 | 9414.80 | -585.20 | sell / filled / 직전 완료 봉 목표 비중 0%; 다음 봉 시가 가정 |
| v2 | trend_8_26 AND reversion_12 | 9621.61 | -378.39 | sell / filled / 직전 완료 봉 목표 비중 0%; 다음 봉 시가 가정 |
| v2 | trend_8_26 + reversion_12 | 9369.89 | -630.11 | sell / filled / 직전 완료 봉 목표 비중 0%; 다음 봉 시가 가정 |
| v2 | trend_8_26 AND volume_26 | 9442.22 | -557.78 | sell / filled / 직전 완료 봉 목표 비중 0%; 다음 봉 시가 가정 |
| v2 | trend_8_26 + volume_26 | 9280.25 | -719.75 | buy / filled / 직전 완료 봉 목표 비중 50%; 다음 봉 시가 가정 |
| v2 | momentum_26 AND breakout_8 | 9414.38 | -585.62 | sell / filled / 직전 완료 봉 목표 비중 0%; 다음 봉 시가 가정 |
| v2 | momentum_26 + breakout_8 | 9322.04 | -677.96 | sell / filled / 직전 완료 봉 목표 비중 0%; 다음 봉 시가 가정 |
| v2 | momentum_26 AND reversion_12 | 9722.08 | -277.92 | sell / filled / 직전 완료 봉 목표 비중 0%; 다음 봉 시가 가정 |
| v2 | momentum_26 + reversion_12 | 9395.12 | -604.88 | sell / filled / 직전 완료 봉 목표 비중 0%; 다음 봉 시가 가정 |
| v2 | momentum_26 AND volume_26 | 9523.88 | -476.12 | sell / filled / 직전 완료 봉 목표 비중 0%; 다음 봉 시가 가정 |
| v2 | momentum_26 + volume_26 | 9266.16 | -733.84 | buy / filled / 직전 완료 봉 목표 비중 50%; 다음 봉 시가 가정 |
| v2 | breakout_8 AND reversion_12 | 10000.00 | 0.00 | 대기 /  / 새 신호 대기 |
| v2 | breakout_8 + reversion_12 | 9197.34 | -802.66 | sell / filled / 직전 완료 봉 목표 비중 0%; 다음 봉 시가 가정 |
| v2 | breakout_8 AND volume_26 | 9765.99 | -234.01 | sell / filled / 직전 완료 봉 목표 비중 0%; 다음 봉 시가 가정 |
| v2 | breakout_8 + volume_26 | 9128.54 | -871.46 | buy / filled / 직전 완료 봉 목표 비중 50%; 다음 봉 시가 가정 |
| v2 | reversion_12 AND volume_26 | 9552.33 | -447.67 | sell / filled / 직전 완료 봉 목표 비중 0%; 다음 봉 시가 가정 |
| v2 | reversion_12 + volume_26 | 9142.80 | -857.20 | sell / filled / 직전 완료 봉 목표 비중 50%; 다음 봉 시가 가정 |
| v2 | ema_12_26 | 9736.67 | -263.33 | sell / filled / EMA12 > EMA26; 조건 미충족; EMA12=771.277, EMA26=771.539; 직전 완료 봉 목표를 다음 봉 시가에 모의 적용 |
| v2 | macd_12_26_9 | 9761.73 | -238.27 | sell / filled / MACD > 신호선 그리고 MACD > 0; 조건 미충족; MACD=1.03945, signal9=1.12358; 직전 완료 봉 목표를 다음 봉 시가에 모의 적용 |
| v2 | rsi_14_recovery | 9835.26 | -164.74 | sell / filled / 직전 RSI14 < 30, 현재 RSI14 >= 30 (한 봉 목표); 조건 미충족; RSI14=28.3968, previous_RSI14=31.7649; 직전 완료 봉 목표를 다음 봉 시가에 모의 적용 |
| v2 | bollinger_20_reentry | 9779.61 | -220.39 | sell / filled / 직전 종가 < 직전 하단밴드, 현재 하단밴드 <= 종가 <= SMA20 (한 봉 목표); 조건 미충족; close=762.71, lower20=761.42, SMA20=770.302, previous_lower20=762.585; 직전 완료 봉 목표를 다음 봉 시가에 모의 적용 |
| v2 | donchian_20 | 9808.27 | -191.73 | sell / filled / 종가 > 현재 봉을 제외한 직전 20봉 최고가; 조건 미충족; close=774.19, prior_high20=774.44; 직전 완료 봉 목표를 다음 봉 시가에 모의 적용 |
| v2 | atr_14_breakout | 9807.08 | -192.92 | sell / filled / 종가 > 직전 종가 + 직전 ATR14 그리고 종가 > EMA26; 조건 미충족; close=773.07, threshold=774.291, prior_ATR14=1.05565, EMA26=772.249; 직전 완료 봉 목표를 다음 봉 시가에 모의 적용 |
| v2 | session_vwap | 9506.56 | -493.44 | sell / filled / 종가 > 뉴욕 거래일별 누적 전형가격 VWAP; 조건 미충족; close=765.69, session_VWAP=766.586, session_volume=7.58519e+06; 직전 완료 봉 목표를 다음 봉 시가에 모의 적용 |
| v2 | obv_20 | 9584.50 | -415.50 | sell / filled / OBV > OBV의 SMA20 그리고 종가 > EMA26; 조건 미충족; OBV=-949325, OBV_SMA20=-1.03221e+07, close=766.62, EMA26=771.893; 직전 완료 봉 목표를 다음 봉 시가에 모의 적용 |
| v2 | stochastic_14_3_recovery | 9623.57 | -376.43 | buy / partial / 직전 %K14 < 20에서 %K14가 %D3 상향 돌파 (한 봉 목표); 조건 충족; K14=10.9938, D3=8.71605, previous_K14=4.94364, previous_D3=6.32113; 직전 완료 봉 목표를 다음 봉 시가에 모의 적용 |
| v2 | mfi_14_recovery | 9800.44 | -199.56 | sell / filled / 직전 MFI14 < 20, 현재 MFI14 >= 20 (한 봉 목표); 조건 미충족; MFI14=24.2496, previous_MFI14=22.3876; 직전 완료 봉 목표를 다음 봉 시가에 모의 적용 |
| v2 | adx_14_trend | 9979.97 | -20.03 | sell / filled / Wilder ADX14 >= 25 그리고 +DI14 > -DI14; 조건 미충족; ADX14=24.2312, plus_DI14=28.3519, minus_DI14=24.6578; 직전 완료 봉 목표를 다음 봉 시가에 모의 적용 |
| v2 | aroon_25_trend | 9722.82 | -277.18 | sell / filled / Aroon25 Up > 70 그리고 Down < 30 (동률이면 최신 극값); 조건 미충족; Aroon_up=72, Aroon_down=100; 직전 완료 봉 목표를 다음 봉 시가에 모의 적용 |
| v2 | cci_20_momentum | 9754.52 | -245.48 | sell / filled / CCI20 > 100 (전형가격·평균절대편차); 조건 미충족; CCI20=97.3932; 직전 완료 봉 목표를 다음 봉 시가에 모의 적용 |
| v2 | williams_14_recovery | 9629.28 | -370.72 | sell / filled / 직전 Williams %R14 < -80, 현재 >= -80 (한 봉 목표); 조건 미충족; Williams_R14=-30.1254, previous_R14=-70.5002; 직전 완료 봉 목표를 다음 봉 시가에 모의 적용 |
| v2 | cmf_20_accumulation | 9717.92 | -282.08 | sell / filled / Chaikin Money Flow20 > 0.1; 조건 미충족; CMF20=0.0565798, volume20=6.40332e+07; 직전 완료 봉 목표를 다음 봉 시가에 모의 적용 |
| v2 | chaikin_3_10 | 9550.09 | -449.91 | sell / filled / ADL의 EMA3 - EMA10 > 0 그리고 종가 > EMA26; 조건 미충족; Chaikin3_10=1.08024e+06, ADL=4.99714e+07, close=766.62, EMA26=771.893; 직전 완료 봉 목표를 다음 봉 시가에 모의 적용 |
| v2 | roc_10_momentum | 9951.43 | -48.57 | sell / filled / 10봉 ROC > 1% 그리고 종가 > EMA26; 조건 미충족; ROC10_percent=0.806376, close=769.45, EMA26=767.181; 직전 완료 봉 목표를 다음 봉 시가에 모의 적용 |
| v2 | trix_15_trend | 9472.93 | -527.07 | sell / filled / 15봉 삼중 EMA의 1봉 변화율 TRIX > 0 그리고 종가 > EMA26; 조건 미충족; TRIX15_percent=0.0154379, close=766.62, EMA26=771.893; 직전 완료 봉 목표를 다음 봉 시가에 모의 적용 |
| v2 | keltner_20_breakout | 9803.05 | -196.95 | sell / filled / 종가 > EMA20 + 2 x Wilder ATR14; 조건 미충족; close=774.19, upper_Keltner=774.31, EMA20=772.615, ATR14=0.847257; 직전 완료 봉 목표를 다음 봉 시가에 모의 적용 |
| v2 | opening_range_30m | 9639.43 | -360.57 | sell / filled / 뉴욕 09:30·09:45 두 완료 봉 최고가를 10:00 이후 종가가 돌파; 자료 부족·변동폭 또는 거래량 없음: 대기; close=766.62; 직전 완료 봉 목표를 다음 봉 시가에 모의 적용 |

### 같은 기간의 비용·노출 비교 (사후 연구)

| 전략 | 비용 전 | 비용 후 | 100% 보유 | 같은 평균 노출 보유 | 평균 노출 |
|---|---:|---:|---:|---:|---:|
| cash | 0.00% | 0.00% | -0.54% | -0.00% | 0.00% |
| buy_hold | -0.12% | -0.54% | -0.54% | -0.54% | 100.00% |
| trend_8_26 | 0.36% | -3.36% | -0.54% | -0.30% | 56.99% |
| momentum_26 | -1.12% | -5.58% | -0.54% | -0.30% | 55.94% |
| breakout_8 | 0.04% | -15.78% | -0.54% | -0.13% | 24.27% |
| reversion_12 | -0.90% | -11.15% | -0.54% | -0.14% | 25.86% |
| volume_26 | -1.53% | -10.60% | -0.54% | -0.05% | 9.23% |
| trend_8_26 AND momentum_26 | -0.52% | -5.01% | -0.54% | -0.26% | 48.81% |
| trend_8_26 + momentum_26 | -0.38% | -4.48% | -0.54% | -0.30% | 56.47% |
| trend_8_26 AND breakout_8 | 0.13% | -11.35% | -0.54% | -0.08% | 15.83% |
| trend_8_26 + breakout_8 | 0.21% | -9.41% | -0.54% | -0.22% | 40.64% |
| trend_8_26 AND reversion_12 | 0.21% | -4.72% | -0.54% | -0.04% | 6.60% |
| trend_8_26 + reversion_12 | -0.26% | -7.15% | -0.54% | -0.22% | 41.43% |
| trend_8_26 AND volume_26 | -1.05% | -6.30% | -0.54% | -0.03% | 5.54% |
| trend_8_26 + volume_26 | -0.58% | -7.05% | -0.54% | -0.18% | 33.12% |
| momentum_26 AND breakout_8 | 0.30% | -11.95% | -0.54% | -0.09% | 17.41% |
| momentum_26 + breakout_8 | -0.54% | -10.83% | -0.54% | -0.21% | 40.11% |
| momentum_26 AND reversion_12 | -0.39% | -5.28% | -0.54% | -0.03% | 6.33% |
| momentum_26 + reversion_12 | -1.00% | -7.64% | -0.54% | -0.22% | 40.90% |
| momentum_26 AND volume_26 | -0.79% | -5.27% | -0.54% | -0.02% | 3.96% |
| momentum_26 + volume_26 | -1.32% | -7.35% | -0.54% | -0.17% | 32.59% |
| breakout_8 AND reversion_12 | 0.00% | 0.00% | -0.54% | -0.00% | 0.00% |
| breakout_8 + reversion_12 | -0.43% | -13.15% | -0.54% | -0.13% | 25.07% |
| breakout_8 AND volume_26 | -0.35% | -2.83% | -0.54% | -0.01% | 2.11% |
| breakout_8 + volume_26 | -0.74% | -12.69% | -0.54% | -0.09% | 16.76% |
| reversion_12 AND volume_26 | -0.97% | -5.05% | -0.54% | -0.02% | 3.69% |
| reversion_12 + volume_26 | -1.21% | -10.50% | -0.54% | -0.09% | 17.55% |
| ema_12_26 | -0.52% | -3.81% | -0.54% | -0.32% | 59.89% |
| macd_12_26_9 | 0.21% | -4.71% | -0.54% | -0.19% | 35.88% |
| rsi_14_recovery | -0.46% | -3.35% | -0.54% | -0.01% | 1.85% |
| bollinger_20_reentry | -0.96% | -6.22% | -0.54% | -0.02% | 3.43% |
| donchian_20 | 0.06% | -8.39% | -0.54% | -0.04% | 7.65% |
| atr_14_breakout | 0.29% | -5.44% | -0.54% | -0.02% | 3.96% |
| session_vwap | 0.47% | -9.92% | -0.54% | -0.26% | 48.02% |
| obv_20 | -1.15% | -9.87% | -0.54% | -0.22% | 42.22% |
| stochastic_14_3_recovery | 0.35% | -12.64% | -0.54% | -0.05% | 8.71% |
| mfi_14_recovery | 0.11% | -2.79% | -0.54% | -0.01% | 1.85% |
| adx_14_trend | 0.77% | -1.74% | -0.54% | -0.13% | 24.80% |
| aroon_25_trend | -0.07% | -2.97% | -0.54% | -0.14% | 26.91% |
| cci_20_momentum | 0.12% | -8.33% | -0.54% | -0.13% | 24.80% |
| williams_14_recovery | 0.19% | -9.41% | -0.54% | -0.03% | 6.33% |
| cmf_20_accumulation | 0.64% | -3.50% | -0.54% | -0.27% | 49.87% |
| chaikin_3_10 | 0.72% | -6.62% | -0.54% | -0.25% | 46.44% |
| roc_10_momentum | -0.13% | -0.97% | -0.54% | -0.01% | 1.06% |
| trix_15_trend | -1.14% | -6.39% | -0.54% | -0.24% | 45.91% |
| keltner_20_breakout | -0.22% | -4.73% | -0.54% | -0.07% | 12.40% |
| opening_range_30m | -0.27% | -6.36% | -0.54% | -0.22% | 41.42% |

동일 구간·초기 자금, 종료 시 청산 비용 포함. 노출 맞춤은 사후 설명용이며 v2 실제 계좌 성과가 아닙니다.
[낙폭 분해·비용 영향·전체 구간](SPY/comparison.json)

[v1 전체 기록](SPY/accounts.json) · [v2 전체 기록](SPY/accounts-v2.json)

## QQQ 계좌

| 모델 | 전략 | 평가액 USD | 손익 USD | 최근 매매·이유 |
|---|---|---:|---:|---|
| v1 | cash | 10000.00 | 0.00 | 대기 /  / 새 신호 대기 |
| v1 | buy_hold | 9736.53 | -263.47 | buy /  / buy_hold: prior completed bar target 100%; next bar open simulation |
| v1 | trend_8_26 | 9679.99 | -320.01 | sell /  / trend_8_26: prior completed bar target 0%; next bar open simulation |
| v1 | momentum_26 | 9370.26 | -629.74 | sell /  / momentum_26: prior completed bar target 0%; next bar open simulation |
| v1 | breakout_8 | 9613.51 | -386.49 | sell /  / breakout_8: prior completed bar target 0%; next bar open simulation |
| v1 | reversion_12 | 9632.18 | -367.82 | sell /  / reversion_12: prior completed bar target 0%; next bar open simulation |
| v1 | volume_26 | 9576.63 | -423.37 | buy /  / volume_26: prior completed bar target 100%; next bar open simulation |
| v1 | trend_8_26 AND momentum_26 | 9732.14 | -267.86 | sell /  / trend_8_26 AND momentum_26: prior completed bar target 0%; next bar open simulation |
| v1 | trend_8_26 + momentum_26 | 9562.10 | -437.90 | sell /  / trend_8_26 + momentum_26: prior completed bar target 0%; next bar open simulation |
| v1 | trend_8_26 AND breakout_8 | 9949.62 | -50.38 | sell /  / trend_8_26 AND breakout_8: prior completed bar target 0%; next bar open simulation |
| v1 | trend_8_26 + breakout_8 | 9685.58 | -314.42 | sell /  / trend_8_26 + breakout_8: prior completed bar target 0%; next bar open simulation |
| v1 | trend_8_26 AND reversion_12 | 9885.50 | -114.50 | sell /  / trend_8_26 AND reversion_12: prior completed bar target 0%; next bar open simulation |
| v1 | trend_8_26 + reversion_12 | 9695.05 | -304.95 | sell /  / trend_8_26 + reversion_12: prior completed bar target 0%; next bar open simulation |
| v1 | trend_8_26 AND volume_26 | 9846.67 | -153.33 | sell /  / trend_8_26 AND volume_26: prior completed bar target 0%; next bar open simulation |
| v1 | trend_8_26 + volume_26 | 9628.30 | -371.70 | sell /  / trend_8_26 + volume_26: prior completed bar target 50%; next bar open simulation |
| v1 | momentum_26 AND breakout_8 | 9644.64 | -355.36 | sell /  / momentum_26 AND breakout_8: prior completed bar target 0%; next bar open simulation |
| v1 | momentum_26 + breakout_8 | 9491.44 | -508.56 | sell /  / momentum_26 + breakout_8: prior completed bar target 0%; next bar open simulation |
| v1 | momentum_26 AND reversion_12 | 9783.95 | -216.05 | sell /  / momentum_26 AND reversion_12: prior completed bar target 0%; next bar open simulation |
| v1 | momentum_26 + reversion_12 | 9557.86 | -442.14 | sell /  / momentum_26 + reversion_12: prior completed bar target 0%; next bar open simulation |
| v1 | momentum_26 AND volume_26 | 9819.14 | -180.86 | sell /  / momentum_26 AND volume_26: prior completed bar target 0%; next bar open simulation |
| v1 | momentum_26 + volume_26 | 9492.00 | -508.00 | sell /  / momentum_26 + volume_26: prior completed bar target 50%; next bar open simulation |
| v1 | breakout_8 AND reversion_12 | 10000.00 | 0.00 | 대기 /  / 새 신호 대기 |
| v1 | breakout_8 + reversion_12 | 9661.39 | -338.61 | sell /  / breakout_8 + reversion_12: prior completed bar target 0%; next bar open simulation |
| v1 | breakout_8 AND volume_26 | 9929.33 | -70.67 | sell /  / breakout_8 AND volume_26: prior completed bar target 0%; next bar open simulation |
| v1 | breakout_8 + volume_26 | 9614.21 | -385.79 | sell /  / breakout_8 + volume_26: prior completed bar target 50%; next bar open simulation |
| v1 | reversion_12 AND volume_26 | 9860.10 | -139.90 | sell /  / reversion_12 AND volume_26: prior completed bar target 0%; next bar open simulation |
| v1 | reversion_12 + volume_26 | 9642.79 | -357.21 | sell /  / reversion_12 + volume_26: prior completed bar target 50%; next bar open simulation |
| v1 | ema_12_26 | 9439.49 | -560.51 | sell /  / EMA12 > EMA26; 조건 미충족; EMA12=723.809, EMA26=723.847 |
| v1 | macd_12_26_9 | 9765.43 | -234.57 | sell /  / MACD > 신호선 그리고 MACD > 0; 조건 미충족; MACD=1.7811, signal9=1.82319 |
| v1 | rsi_14_recovery | 9809.40 | -190.60 | sell /  / 직전 RSI14 < 30, 현재 RSI14 >= 30 (한 봉 목표); 조건 미충족; RSI14=50.2063, previous_RSI14=44.1729 |
| v1 | bollinger_20_reentry | 9823.48 | -176.52 | sell /  / 직전 종가 < 직전 하단밴드, 현재 하단밴드 <= 종가 <= SMA20 (한 봉 목표); 조건 미충족; close=706.995, lower20=705.434, SMA20=720.761, previous_lower20=707.596 |
| v1 | donchian_20 | 9889.14 | -110.86 | sell /  / 종가 > 현재 봉을 제외한 직전 20봉 최고가; 조건 미충족; close=726.885, prior_high20=727.77 |
| v1 | atr_14_breakout | 9887.37 | -112.63 | sell /  / 종가 > 직전 종가 + 직전 ATR14 그리고 종가 > EMA26; 조건 미충족; close=725.79, threshold=727.527, prior_ATR14=1.49237, EMA26=724.609 |
| v1 | session_vwap | 9464.47 | -535.53 | sell /  / 종가 > 뉴욕 거래일별 누적 전형가격 VWAP; 조건 미충족; close=712.29, session_VWAP=713.442, session_volume=1.82088e+07 |
| v1 | obv_20 | 9508.81 | -491.19 | sell /  / OBV > OBV의 SMA20 그리고 종가 > EMA26; 조건 미충족; OBV=4.39726e+08, OBV_SMA20=4.50483e+08, close=713.775, EMA26=723.847 |
| v1 | stochastic_14_3_recovery | 9522.25 | -477.75 | buy /  / 직전 %K14 < 20에서 %K14가 %D3 상향 돌파 (한 봉 목표); 조건 충족; K14=7.28772, D3=5.3193, previous_K14=1.76154, previous_D3=3.63612 |
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
| v2 | buy_hold | 9421.80 | -578.20 | buy / partial / 직전 완료 봉 목표 비중 100%; 다음 봉 시가 가정 |
| v2 | trend_8_26 | 9482.37 | -517.63 | sell / filled / 직전 완료 봉 목표 비중 0%; 다음 봉 시가 가정 |
| v2 | momentum_26 | 9261.49 | -738.51 | sell / filled / 직전 완료 봉 목표 비중 0%; 다음 봉 시가 가정 |
| v2 | breakout_8 | 9279.42 | -720.58 | sell / filled / 직전 완료 봉 목표 비중 0%; 다음 봉 시가 가정 |
| v2 | reversion_12 | 9145.68 | -854.32 | sell / filled / 직전 완료 봉 목표 비중 0%; 다음 봉 시가 가정 |
| v2 | volume_26 | 9565.80 | -434.20 | 중단: 손실 한도 / sell / filled / 직전 완료 봉 목표 비중 0%; 다음 봉 시가 가정 |
| v2 | trend_8_26 AND momentum_26 | 9626.87 | -373.13 | sell / filled / 직전 완료 봉 목표 비중 0%; 다음 봉 시가 가정 |
| v2 | trend_8_26 + momentum_26 | 9410.82 | -589.18 | sell / filled / 직전 완료 봉 목표 비중 0%; 다음 봉 시가 가정 |
| v2 | trend_8_26 AND breakout_8 | 9840.07 | -159.93 | sell / filled / 직전 완료 봉 목표 비중 0%; 다음 봉 시가 가정 |
| v2 | trend_8_26 + breakout_8 | 9419.99 | -580.01 | sell / filled / 직전 완료 봉 목표 비중 0%; 다음 봉 시가 가정 |
| v2 | trend_8_26 AND reversion_12 | 9742.38 | -257.62 | sell / filled / 직전 완료 봉 목표 비중 0%; 다음 봉 시가 가정 |
| v2 | trend_8_26 + reversion_12 | 9351.66 | -648.34 | sell / filled / 직전 완료 봉 목표 비중 0%; 다음 봉 시가 가정 |
| v2 | trend_8_26 AND volume_26 | 9679.53 | -320.47 | sell / filled / 직전 완료 봉 목표 비중 0%; 다음 봉 시가 가정 |
| v2 | trend_8_26 + volume_26 | 9233.69 | -766.31 | sell / filled / 직전 완료 봉 목표 비중 50%; 다음 봉 시가 가정 |
| v2 | momentum_26 AND breakout_8 | 9591.37 | -408.63 | sell / filled / 직전 완료 봉 목표 비중 0%; 다음 봉 시가 가정 |
| v2 | momentum_26 + breakout_8 | 9270.73 | -729.27 | sell / filled / 직전 완료 봉 목표 비중 0%; 다음 봉 시가 가정 |
| v2 | momentum_26 AND reversion_12 | 9776.12 | -223.88 | sell / filled / 직전 완료 봉 목표 비중 0%; 다음 봉 시가 가정 |
| v2 | momentum_26 + reversion_12 | 9281.04 | -718.96 | sell / filled / 직전 완료 봉 목표 비중 0%; 다음 봉 시가 가정 |
| v2 | momentum_26 AND volume_26 | 9749.31 | -250.69 | sell / filled / 직전 완료 봉 목표 비중 0%; 다음 봉 시가 가정 |
| v2 | momentum_26 + volume_26 | 9144.69 | -855.31 | sell / filled / 직전 완료 봉 목표 비중 50%; 다음 봉 시가 가정 |
| v2 | breakout_8 AND reversion_12 | 10000.00 | 0.00 | 대기 /  / 새 신호 대기 |
| v2 | breakout_8 + reversion_12 | 9309.19 | -690.81 | sell / filled / 직전 완료 봉 목표 비중 0%; 다음 봉 시가 가정 |
| v2 | breakout_8 AND volume_26 | 9871.76 | -128.24 | sell / filled / 직전 완료 봉 목표 비중 0%; 다음 봉 시가 가정 |
| v2 | breakout_8 + volume_26 | 9191.94 | -808.06 | sell / filled / 직전 완료 봉 목표 비중 50%; 다음 봉 시가 가정 |
| v2 | reversion_12 AND volume_26 | 9547.64 | -452.36 | 중단: 손실 한도 / sell / filled / 직전 완료 봉 목표 비중 0%; 다음 봉 시가 가정 |
| v2 | reversion_12 + volume_26 | 9125.52 | -874.48 | sell / filled / 직전 완료 봉 목표 비중 50%; 다음 봉 시가 가정 |
| v2 | ema_12_26 | 9430.06 | -569.94 | sell / filled / EMA12 > EMA26; 조건 미충족; EMA12=723.809, EMA26=723.847; 직전 완료 봉 목표를 다음 봉 시가에 모의 적용 |
| v2 | macd_12_26_9 | 9755.67 | -244.33 | sell / filled / MACD > 신호선 그리고 MACD > 0; 조건 미충족; MACD=1.7811, signal9=1.82319; 직전 완료 봉 목표를 다음 봉 시가에 모의 적용 |
| v2 | rsi_14_recovery | 9801.56 | -198.44 | sell / filled / 직전 RSI14 < 30, 현재 RSI14 >= 30 (한 봉 목표); 조건 미충족; RSI14=50.2063, previous_RSI14=44.1729; 직전 완료 봉 목표를 다음 봉 시가에 모의 적용 |
| v2 | bollinger_20_reentry | 9815.62 | -184.38 | sell / filled / 직전 종가 < 직전 하단밴드, 현재 하단밴드 <= 종가 <= SMA20 (한 봉 목표); 조건 미충족; close=706.995, lower20=705.434, SMA20=720.761, previous_lower20=707.596; 직전 완료 봉 목표를 다음 봉 시가에 모의 적용 |
| v2 | donchian_20 | 9881.23 | -118.77 | sell / filled / 종가 > 현재 봉을 제외한 직전 20봉 최고가; 조건 미충족; close=726.885, prior_high20=727.77; 직전 완료 봉 목표를 다음 봉 시가에 모의 적용 |
| v2 | atr_14_breakout | 9879.47 | -120.53 | sell / filled / 종가 > 직전 종가 + 직전 ATR14 그리고 종가 > EMA26; 조건 미충족; close=725.79, threshold=727.527, prior_ATR14=1.49237, EMA26=724.609; 직전 완료 봉 목표를 다음 봉 시가에 모의 적용 |
| v2 | session_vwap | 9447.45 | -552.55 | sell / filled / 종가 > 뉴욕 거래일별 누적 전형가격 VWAP; 조건 미충족; close=712.29, session_VWAP=713.442, session_volume=1.82088e+07; 직전 완료 봉 목표를 다음 봉 시가에 모의 적용 |
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
| cash | 0.00% | 0.00% | -5.11% | -0.00% | 0.00% |
| buy_hold | -4.71% | -5.11% | -5.11% | -5.11% | 100.00% |
| trend_8_26 | -1.39% | -5.05% | -5.11% | -2.27% | 44.33% |
| momentum_26 | -4.32% | -9.79% | -5.11% | -2.04% | 39.84% |
| breakout_8 | -1.70% | -16.55% | -5.11% | -0.98% | 19.00% |
| reversion_12 | -0.40% | -12.19% | -5.11% | -1.57% | 30.61% |
| volume_26 | -1.34% | -14.82% | -5.11% | -0.85% | 16.62% |
| trend_8_26 AND momentum_26 | -1.51% | -5.16% | -5.11% | -1.71% | 33.25% |
| trend_8_26 + momentum_26 | -2.86% | -6.86% | -5.11% | -2.16% | 42.09% |
| trend_8_26 AND breakout_8 | 0.42% | -7.67% | -5.11% | -0.61% | 11.87% |
| trend_8_26 + breakout_8 | -1.54% | -10.42% | -5.11% | -1.63% | 31.67% |
| trend_8_26 AND reversion_12 | -0.22% | -4.33% | -5.11% | -0.34% | 6.60% |
| trend_8_26 + reversion_12 | -0.88% | -8.11% | -5.11% | -1.92% | 37.47% |
| trend_8_26 AND volume_26 | 0.23% | -4.70% | -5.11% | -0.27% | 5.28% |
| trend_8_26 + volume_26 | -1.35% | -10.07% | -5.11% | -1.56% | 30.48% |
| momentum_26 AND breakout_8 | -0.36% | -9.16% | -5.11% | -0.62% | 12.14% |
| momentum_26 + breakout_8 | -3.01% | -13.05% | -5.11% | -1.51% | 29.43% |
| momentum_26 AND reversion_12 | -1.04% | -5.51% | -5.11% | -0.34% | 6.60% |
| momentum_26 + reversion_12 | -2.37% | -10.06% | -5.11% | -1.81% | 35.23% |
| momentum_26 AND volume_26 | -0.38% | -4.08% | -5.11% | -0.19% | 3.69% |
| momentum_26 + volume_26 | -2.83% | -11.98% | -5.11% | -1.45% | 28.24% |
| breakout_8 AND reversion_12 | 0.00% | 0.00% | -5.11% | -0.00% | 0.00% |
| breakout_8 + reversion_12 | -1.04% | -13.32% | -5.11% | -1.27% | 24.81% |
| breakout_8 AND volume_26 | 0.32% | -2.18% | -5.11% | -0.12% | 2.37% |
| breakout_8 + volume_26 | -1.51% | -14.27% | -5.11% | -0.92% | 17.82% |
| reversion_12 AND volume_26 | -1.22% | -8.03% | -5.11% | -0.43% | 8.44% |
| reversion_12 + volume_26 | -0.86% | -12.97% | -5.11% | -1.21% | 23.62% |
| ema_12_26 | -2.73% | -5.55% | -5.11% | -2.12% | 41.42% |
| macd_12_26_9 | 0.59% | -3.95% | -5.11% | -1.29% | 25.07% |
| rsi_14_recovery | -0.47% | -5.76% | -5.11% | -0.18% | 3.43% |
| bollinger_20_reentry | -0.05% | -5.76% | -5.11% | -0.19% | 3.69% |
| donchian_20 | 0.58% | -5.17% | -5.11% | -0.34% | 6.60% |
| atr_14_breakout | 0.32% | -3.81% | -5.11% | -0.15% | 2.90% |
| session_vwap | -1.81% | -13.07% | -5.11% | -2.41% | 46.97% |
| obv_20 | -2.88% | -11.45% | -5.11% | -1.50% | 29.29% |
| stochastic_14_3_recovery | 0.07% | -11.78% | -5.11% | -0.41% | 7.92% |
| mfi_14_recovery | -1.19% | -3.24% | -5.11% | -0.07% | 1.32% |
| adx_14_trend | -0.10% | -3.00% | -5.11% | -1.03% | 20.05% |
| aroon_25_trend | 1.00% | -2.75% | -5.11% | -0.91% | 17.68% |
| cci_20_momentum | 0.23% | -5.09% | -5.11% | -0.96% | 18.73% |
| williams_14_recovery | 0.23% | -10.14% | -5.11% | -0.35% | 6.86% |
| cmf_20_accumulation | -3.30% | -9.96% | -5.11% | -1.92% | 37.47% |
| chaikin_3_10 | -4.09% | -12.19% | -5.11% | -1.73% | 33.77% |
| roc_10_momentum | 0.13% | -1.54% | -5.11% | -0.24% | 4.75% |
| trix_15_trend | -1.62% | -5.27% | -5.11% | -1.77% | 34.56% |
| keltner_20_breakout | -0.82% | -5.70% | -5.11% | -0.45% | 8.71% |
| opening_range_30m | -1.73% | -6.95% | -5.11% | -1.77% | 34.56% |

동일 구간·초기 자금, 종료 시 청산 비용 포함. 노출 맞춤은 사후 설명용이며 v2 실제 계좌 성과가 아닙니다.
[낙폭 분해·비용 영향·전체 구간](QQQ/comparison.json)

[v1 전체 기록](QQQ/accounts.json) · [v2 전체 기록](QQQ/accounts-v2.json)

## IWM 계좌

| 모델 | 전략 | 평가액 USD | 손익 USD | 최근 매매·이유 |
|---|---|---:|---:|---|
| v1 | cash | 10000.00 | 0.00 | 대기 /  / 새 신호 대기 |
| v1 | buy_hold | 9982.93 | -17.07 | buy /  / buy_hold: prior completed bar target 100%; next bar open simulation |
| v1 | trend_8_26 | 9801.27 | -198.73 | sell /  / trend_8_26: prior completed bar target 0%; next bar open simulation |
| v1 | momentum_26 | 9795.94 | -204.06 | sell /  / momentum_26: prior completed bar target 0%; next bar open simulation |
| v1 | breakout_8 | 9416.78 | -583.22 | sell /  / breakout_8: prior completed bar target 0%; next bar open simulation |
| v1 | reversion_12 | 9736.37 | -263.63 | sell /  / reversion_12: prior completed bar target 0%; next bar open simulation |
| v1 | volume_26 | 9885.16 | -114.84 | sell /  / volume_26: prior completed bar target 0%; next bar open simulation |
| v1 | trend_8_26 AND momentum_26 | 9746.90 | -253.10 | sell /  / trend_8_26 AND momentum_26: prior completed bar target 0%; next bar open simulation |
| v1 | trend_8_26 + momentum_26 | 9798.73 | -201.27 | sell /  / trend_8_26 + momentum_26: prior completed bar target 0%; next bar open simulation |
| v1 | trend_8_26 AND breakout_8 | 9504.10 | -495.90 | sell /  / trend_8_26 AND breakout_8: prior completed bar target 0%; next bar open simulation |
| v1 | trend_8_26 + breakout_8 | 9607.29 | -392.71 | sell /  / trend_8_26 + breakout_8: prior completed bar target 0%; next bar open simulation |
| v1 | trend_8_26 AND reversion_12 | 9811.31 | -188.69 | sell /  / trend_8_26 AND reversion_12: prior completed bar target 0%; next bar open simulation |
| v1 | trend_8_26 + reversion_12 | 9768.56 | -231.44 | sell /  / trend_8_26 + reversion_12: prior completed bar target 0%; next bar open simulation |
| v1 | trend_8_26 AND volume_26 | 9927.90 | -72.10 | sell /  / trend_8_26 AND volume_26: prior completed bar target 0%; next bar open simulation |
| v1 | trend_8_26 + volume_26 | 9862.68 | -137.32 | sell /  / trend_8_26 + volume_26: prior completed bar target 0%; next bar open simulation |
| v1 | momentum_26 AND breakout_8 | 9552.12 | -447.88 | sell /  / momentum_26 AND breakout_8: prior completed bar target 0%; next bar open simulation |
| v1 | momentum_26 + breakout_8 | 9623.87 | -376.13 | sell /  / momentum_26 + breakout_8: prior completed bar target 0%; next bar open simulation |
| v1 | momentum_26 AND reversion_12 | 9876.67 | -123.33 | sell /  / momentum_26 AND reversion_12: prior completed bar target 0%; next bar open simulation |
| v1 | momentum_26 + reversion_12 | 9844.41 | -155.59 | sell /  / momentum_26 + reversion_12: prior completed bar target 0%; next bar open simulation |
| v1 | momentum_26 AND volume_26 | 9977.14 | -22.86 | sell /  / momentum_26 AND volume_26: prior completed bar target 0%; next bar open simulation |
| v1 | momentum_26 + volume_26 | 9879.83 | -120.17 | sell /  / momentum_26 + volume_26: prior completed bar target 0%; next bar open simulation |
| v1 | breakout_8 AND reversion_12 | 10000.00 | 0.00 | 대기 /  / 새 신호 대기 |
| v1 | breakout_8 + reversion_12 | 9594.19 | -405.81 | sell /  / breakout_8 + reversion_12: prior completed bar target 0%; next bar open simulation |
| v1 | breakout_8 AND volume_26 | 9967.28 | -32.72 | sell /  / breakout_8 AND volume_26: prior completed bar target 0%; next bar open simulation |
| v1 | breakout_8 + volume_26 | 9667.37 | -332.63 | sell /  / breakout_8 + volume_26: prior completed bar target 0%; next bar open simulation |
| v1 | reversion_12 AND volume_26 | 9937.60 | -62.40 | sell /  / reversion_12 AND volume_26: prior completed bar target 0%; next bar open simulation |
| v1 | reversion_12 + volume_26 | 9849.76 | -150.24 | sell /  / reversion_12 + volume_26: prior completed bar target 0%; next bar open simulation |
| v1 | ema_12_26 | 9815.21 | -184.79 | sell /  / EMA12 > EMA26; 조건 미충족; EMA12=276.256, EMA26=276.345 |
| v1 | macd_12_26_9 | 9906.42 | -93.58 | sell /  / MACD > 신호선 그리고 MACD > 0; 조건 미충족; MACD=0.978353, signal9=1.01104 |
| v1 | rsi_14_recovery | 9786.95 | -213.05 | sell /  / 직전 RSI14 < 30, 현재 RSI14 >= 30 (한 봉 목표); 조건 미충족; RSI14=46.986, previous_RSI14=37.1649 |
| v1 | bollinger_20_reentry | 9848.19 | -151.81 | sell /  / 직전 종가 < 직전 하단밴드, 현재 하단밴드 <= 종가 <= SMA20 (한 봉 목표); 조건 미충족; close=275.52, lower20=275.107, SMA20=276.469, previous_lower20=275.234 |
| v1 | donchian_20 | 9835.91 | -164.09 | sell /  / 종가 > 현재 봉을 제외한 직전 20봉 최고가; 조건 미충족; close=275.785, prior_high20=276.875 |
| v1 | atr_14_breakout | 9732.89 | -267.11 | sell /  / 종가 > 직전 종가 + 직전 ATR14 그리고 종가 > EMA26; 조건 미충족; close=276.06, threshold=277.643, prior_ATR14=0.662564, EMA26=276.447 |
| v1 | session_vwap | 9603.27 | -396.73 | sell /  / 종가 > 뉴욕 거래일별 누적 전형가격 VWAP; 조건 미충족; close=276.06, session_VWAP=276.109, session_volume=6.10739e+06 |
| v1 | obv_20 | 9843.12 | -156.88 | sell /  / OBV > OBV의 SMA20 그리고 종가 > EMA26; 조건 미충족; OBV=-1.67312e+07, OBV_SMA20=-1.67396e+07, close=276.015, EMA26=276.549 |
| v1 | stochastic_14_3_recovery | 9649.02 | -350.98 | buy /  / 직전 %K14 < 20에서 %K14가 %D3 상향 돌파 (한 봉 목표); 조건 충족; K14=36.5078, D3=30.3985, previous_K14=18.924, previous_D3=27.4308 |
| v1 | mfi_14_recovery | 9934.22 | -65.78 | sell /  / 직전 MFI14 < 20, 현재 MFI14 >= 20 (한 봉 목표); 조건 미충족; MFI14=34.131, previous_MFI14=22.0435 |
| v1 | adx_14_trend | 9726.05 | -273.95 | sell /  / Wilder ADX14 >= 25 그리고 +DI14 > -DI14; 조건 미충족; ADX14=27.8461, plus_DI14=25.882, minus_DI14=28.4558 |
| v1 | aroon_25_trend | 9745.85 | -254.15 | sell /  / Aroon25 Up > 70 그리고 Down < 30 (동률이면 최신 극값); 조건 미충족; Aroon_up=68, Aroon_down=4 |
| v1 | cci_20_momentum | 9825.51 | -174.49 | sell /  / CCI20 > 100 (전형가격·평균절대편차); 조건 미충족; CCI20=-152.101 |
| v1 | williams_14_recovery | 9777.89 | -222.11 | buy /  / 직전 Williams %R14 < -80, 현재 >= -80 (한 봉 목표); 조건 충족; Williams_R14=-63.4922, previous_R14=-81.076 |
| v1 | cmf_20_accumulation | 9709.11 | -290.89 | sell /  / Chaikin Money Flow20 > 0.1; 조건 미충족; CMF20=0.0178538, volume20=1.46976e+07 |
| v1 | chaikin_3_10 | 9685.17 | -314.83 | sell /  / ADL의 EMA3 - EMA10 > 0 그리고 종가 > EMA26; 조건 미충족; Chaikin3_10=252164, ADL=-3.32524e+07, close=276.06, EMA26=276.447 |
| v1 | roc_10_momentum | 9996.39 | -3.61 | sell /  / 10봉 ROC > 1% 그리고 종가 > EMA26; 조건 미충족; ROC10_percent=0.995963, close=275.315, EMA26=273.754 |
| v1 | trix_15_trend | 9811.92 | -188.08 | sell /  / 15봉 삼중 EMA의 1봉 변화율 TRIX > 0 그리고 종가 > EMA26; 조건 미충족; TRIX15_percent=0.00744142, close=276.06, EMA26=276.447 |
| v1 | keltner_20_breakout | 9879.23 | -120.77 | sell /  / 종가 > EMA20 + 2 x Wilder ATR14; 조건 미충족; close=276.4, upper_Keltner=277.094, EMA20=275.768, ATR14=0.662947 |
| v1 | opening_range_30m | 9963.15 | -36.85 | sell /  / 뉴욕 09:30·09:45 두 완료 봉 최고가를 10:00 이후 종가가 돌파; 자료 부족·변동폭 또는 거래량 없음: 대기; close=276.82 |
| v2 | cash | 10000.00 | 0.00 | 대기 /  / 새 신호 대기 |
| v2 | buy_hold | 9876.19 | -123.81 | buy / partial / 직전 완료 봉 목표 비중 100%; 다음 봉 시가 가정 |
| v2 | trend_8_26 | 9669.43 | -330.57 | sell / filled / 직전 완료 봉 목표 비중 0%; 다음 봉 시가 가정 |
| v2 | momentum_26 | 9661.30 | -338.70 | sell / filled / 직전 완료 봉 목표 비중 0%; 다음 봉 시가 가정 |
| v2 | breakout_8 | 9033.27 | -966.73 | sell / filled / 직전 완료 봉 목표 비중 0%; 다음 봉 시가 가정 |
| v2 | reversion_12 | 9270.49 | -729.51 | sell / filled / 직전 완료 봉 목표 비중 0%; 다음 봉 시가 가정 |
| v2 | volume_26 | 9394.71 | -605.29 | sell / filled / 직전 완료 봉 목표 비중 0%; 다음 봉 시가 가정 |
| v2 | trend_8_26 AND momentum_26 | 9761.14 | -238.86 | sell / filled / 직전 완료 봉 목표 비중 0%; 다음 봉 시가 가정 |
| v2 | trend_8_26 + momentum_26 | 9685.93 | -314.07 | sell / filled / 직전 완료 봉 목표 비중 0%; 다음 봉 시가 가정 |
| v2 | trend_8_26 AND breakout_8 | 9402.34 | -597.66 | sell / filled / 직전 완료 봉 목표 비중 0%; 다음 봉 시가 가정 |
| v2 | trend_8_26 + breakout_8 | 9365.90 | -634.10 | sell / filled / 직전 완료 봉 목표 비중 0%; 다음 봉 시가 가정 |
| v2 | trend_8_26 AND reversion_12 | 9687.61 | -312.39 | sell / filled / 직전 완료 봉 목표 비중 0%; 다음 봉 시가 가정 |
| v2 | trend_8_26 + reversion_12 | 9467.49 | -532.51 | sell / filled / 직전 완료 봉 목표 비중 0%; 다음 봉 시가 가정 |
| v2 | trend_8_26 AND volume_26 | 9787.80 | -212.20 | sell / filled / 직전 완료 봉 목표 비중 0%; 다음 봉 시가 가정 |
| v2 | trend_8_26 + volume_26 | 9571.02 | -428.98 | sell / filled / 직전 완료 봉 목표 비중 0%; 다음 봉 시가 가정 |
| v2 | momentum_26 AND breakout_8 | 9347.05 | -652.95 | sell / filled / 직전 완료 봉 목표 비중 0%; 다음 봉 시가 가정 |
| v2 | momentum_26 + breakout_8 | 9361.81 | -638.19 | sell / filled / 직전 완료 봉 목표 비중 0%; 다음 봉 시가 가정 |
| v2 | momentum_26 AND reversion_12 | 9831.84 | -168.16 | sell / filled / 직전 완료 봉 목표 비중 0%; 다음 봉 시가 가정 |
| v2 | momentum_26 + reversion_12 | 9563.23 | -436.77 | sell / filled / 직전 완료 봉 목표 비중 0%; 다음 봉 시가 가정 |
| v2 | momentum_26 AND volume_26 | 9869.24 | -130.76 | sell / filled / 직전 완료 봉 목표 비중 0%; 다음 봉 시가 가정 |
| v2 | momentum_26 + volume_26 | 9566.89 | -433.11 | sell / filled / 직전 완료 봉 목표 비중 0%; 다음 봉 시가 가정 |
| v2 | breakout_8 AND reversion_12 | 10000.00 | 0.00 | 대기 /  / 새 신호 대기 |
| v2 | breakout_8 + reversion_12 | 9208.32 | -791.68 | sell / filled / 직전 완료 봉 목표 비중 0%; 다음 봉 시가 가정 |
| v2 | breakout_8 AND volume_26 | 9710.25 | -289.75 | sell / filled / 직전 완료 봉 목표 비중 0%; 다음 봉 시가 가정 |
| v2 | breakout_8 + volume_26 | 9250.84 | -749.16 | sell / filled / 직전 완료 봉 목표 비중 0%; 다음 봉 시가 가정 |
| v2 | reversion_12 AND volume_26 | 9674.16 | -325.84 | sell / filled / 직전 완료 봉 목표 비중 0%; 다음 봉 시가 가정 |
| v2 | reversion_12 + volume_26 | 9391.11 | -608.89 | sell / filled / 직전 완료 봉 목표 비중 0%; 다음 봉 시가 가정 |
| v2 | ema_12_26 | 9809.32 | -190.68 | sell / filled / EMA12 > EMA26; 조건 미충족; EMA12=276.256, EMA26=276.345; 직전 완료 봉 목표를 다음 봉 시가에 모의 적용 |
| v2 | macd_12_26_9 | 9900.47 | -99.53 | sell / filled / MACD > 신호선 그리고 MACD > 0; 조건 미충족; MACD=0.978353, signal9=1.01104; 직전 완료 봉 목표를 다음 봉 시가에 모의 적용 |
| v2 | rsi_14_recovery | 9779.12 | -220.88 | sell / filled / 직전 RSI14 < 30, 현재 RSI14 >= 30 (한 봉 목표); 조건 미충족; RSI14=46.986, previous_RSI14=37.1649; 직전 완료 봉 목표를 다음 봉 시가에 모의 적용 |
| v2 | bollinger_20_reentry | 9840.32 | -159.68 | sell / filled / 직전 종가 < 직전 하단밴드, 현재 하단밴드 <= 종가 <= SMA20 (한 봉 목표); 조건 미충족; close=275.52, lower20=275.107, SMA20=276.469, previous_lower20=275.234; 직전 완료 봉 목표를 다음 봉 시가에 모의 적용 |
| v2 | donchian_20 | 9830.01 | -169.99 | sell / filled / 종가 > 현재 봉을 제외한 직전 20봉 최고가; 조건 미충족; close=275.785, prior_high20=276.875; 직전 완료 봉 목표를 다음 봉 시가에 모의 적용 |
| v2 | atr_14_breakout | 9719.27 | -280.73 | sell / filled / 종가 > 직전 종가 + 직전 ATR14 그리고 종가 > EMA26; 조건 미충족; close=276.06, threshold=277.643, prior_ATR14=0.662564, EMA26=276.447; 직전 완료 봉 목표를 다음 봉 시가에 모의 적용 |
| v2 | session_vwap | 9582.17 | -417.83 | sell / filled / 종가 > 뉴욕 거래일별 누적 전형가격 VWAP; 조건 미충족; close=276.06, session_VWAP=276.109, session_volume=6.10739e+06; 직전 완료 봉 목표를 다음 봉 시가에 모의 적용 |
| v2 | obv_20 | 9833.28 | -166.72 | sell / filled / OBV > OBV의 SMA20 그리고 종가 > EMA26; 조건 미충족; OBV=-2.34336e+07, OBV_SMA20=-2.34421e+07, close=276.015, EMA26=276.549; 직전 완료 봉 목표를 다음 봉 시가에 모의 적용 |
| v2 | stochastic_14_3_recovery | 9632.63 | -367.37 | buy / partial / 직전 %K14 < 20에서 %K14가 %D3 상향 돌파 (한 봉 목표); 조건 충족; K14=36.5078, D3=30.3985, previous_K14=18.924, previous_D3=27.4308; 직전 완료 봉 목표를 다음 봉 시가에 모의 적용 |
| v2 | mfi_14_recovery | 9930.25 | -69.75 | sell / filled / 직전 MFI14 < 20, 현재 MFI14 >= 20 (한 봉 목표); 조건 미충족; MFI14=34.131, previous_MFI14=22.0435; 직전 완료 봉 목표를 다음 봉 시가에 모의 적용 |
| v2 | adx_14_trend | 9718.27 | -281.73 | sell / filled / Wilder ADX14 >= 25 그리고 +DI14 > -DI14; 조건 미충족; ADX14=27.8461, plus_DI14=25.882, minus_DI14=28.4558; 직전 완료 봉 목표를 다음 봉 시가에 모의 적용 |
| v2 | aroon_25_trend | 9736.11 | -263.89 | sell / filled / Aroon25 Up > 70 그리고 Down < 30 (동률이면 최신 극값); 조건 미충족; Aroon_up=68, Aroon_down=4; 직전 완료 봉 목표를 다음 봉 시가에 모의 적용 |
| v2 | cci_20_momentum | 9815.69 | -184.31 | sell / filled / CCI20 > 100 (전형가격·평균절대편차); 조건 미충족; CCI20=-152.101; 직전 완료 봉 목표를 다음 봉 시가에 모의 적용 |
| v2 | williams_14_recovery | 9765.19 | -234.81 | buy / partial / 직전 Williams %R14 < -80, 현재 >= -80 (한 봉 목표); 조건 충족; Williams_R14=-63.4922, previous_R14=-81.076; 직전 완료 봉 목표를 다음 봉 시가에 모의 적용 |
| v2 | cmf_20_accumulation | 9691.65 | -308.35 | sell / filled / Chaikin Money Flow20 > 0.1; 조건 미충족; CMF20=0.0178538, volume20=1.46976e+07; 직전 완료 봉 목표를 다음 봉 시가에 모의 적용 |
| v2 | chaikin_3_10 | 9669.69 | -330.31 | sell / filled / ADL의 EMA3 - EMA10 > 0 그리고 종가 > EMA26; 조건 미충족; Chaikin3_10=252164, ADL=-3.32524e+07, close=276.06, EMA26=276.447; 직전 완료 봉 목표를 다음 봉 시가에 모의 적용 |
| v2 | roc_10_momentum | 9994.39 | -5.61 | sell / filled / 10봉 ROC > 1% 그리고 종가 > EMA26; 조건 미충족; ROC10_percent=0.995963, close=275.315, EMA26=273.754; 직전 완료 봉 목표를 다음 봉 시가에 모의 적용 |
| v2 | trix_15_trend | 9804.07 | -195.93 | sell / filled / 15봉 삼중 EMA의 1봉 변화율 TRIX > 0 그리고 종가 > EMA26; 조건 미충족; TRIX15_percent=0.00744142, close=276.06, EMA26=276.447; 직전 완료 봉 목표를 다음 봉 시가에 모의 적용 |
| v2 | keltner_20_breakout | 9873.30 | -126.70 | sell / filled / 종가 > EMA20 + 2 x Wilder ATR14; 조건 미충족; close=276.4, upper_Keltner=277.094, EMA20=275.768, ATR14=0.662947; 직전 완료 봉 목표를 다음 봉 시가에 모의 적용 |
| v2 | opening_range_30m | 9959.17 | -40.83 | sell / filled / 뉴욕 09:30·09:45 두 완료 봉 최고가를 10:00 이후 종가가 돌파; 자료 부족·변동폭 또는 거래량 없음: 대기; close=276.82; 직전 완료 봉 목표를 다음 봉 시가에 모의 적용 |

### 같은 기간의 비용·노출 비교 (사후 연구)

| 전략 | 비용 전 | 비용 후 | 100% 보유 | 같은 평균 노출 보유 | 평균 노출 |
|---|---:|---:|---:|---:|---:|
| cash | 0.00% | 0.00% | -1.74% | -0.00% | 0.00% |
| buy_hold | -1.33% | -1.74% | -1.74% | -1.74% | 100.00% |
| trend_8_26 | 0.02% | -3.29% | -1.74% | -0.89% | 50.92% |
| momentum_26 | -0.14% | -5.44% | -1.74% | -0.86% | 48.81% |
| breakout_8 | -0.60% | -14.91% | -1.74% | -0.34% | 19.53% |
| reversion_12 | -0.85% | -12.59% | -1.74% | -0.47% | 26.91% |
| volume_26 | -0.50% | -7.75% | -1.74% | -0.15% | 8.44% |
| trend_8_26 AND momentum_26 | -0.10% | -3.81% | -1.74% | -0.75% | 43.01% |
| trend_8_26 + momentum_26 | -0.05% | -3.96% | -1.74% | -0.87% | 49.87% |
| trend_8_26 AND breakout_8 | -0.23% | -9.42% | -1.74% | -0.24% | 13.46% |
| trend_8_26 + breakout_8 | -0.28% | -9.09% | -1.74% | -0.62% | 35.23% |
| trend_8_26 AND reversion_12 | -0.50% | -4.60% | -1.74% | -0.10% | 5.54% |
| trend_8_26 + reversion_12 | -0.41% | -8.06% | -1.74% | -0.68% | 38.92% |
| trend_8_26 AND volume_26 | -0.37% | -3.25% | -1.74% | -0.04% | 2.37% |
| trend_8_26 + volume_26 | -0.23% | -5.15% | -1.74% | -0.52% | 29.69% |
| momentum_26 AND breakout_8 | 0.22% | -9.39% | -1.74% | -0.23% | 13.19% |
| momentum_26 + breakout_8 | -0.37% | -10.11% | -1.74% | -0.60% | 34.18% |
| momentum_26 AND reversion_12 | -0.09% | -2.98% | -1.74% | -0.05% | 2.90% |
| momentum_26 + reversion_12 | -0.49% | -7.75% | -1.74% | -0.66% | 37.87% |
| momentum_26 AND volume_26 | 0.01% | -2.89% | -1.74% | -0.04% | 2.37% |
| momentum_26 + volume_26 | -0.31% | -6.02% | -1.74% | -0.50% | 28.63% |
| breakout_8 AND reversion_12 | 0.00% | 0.00% | -1.74% | -0.00% | 0.00% |
| breakout_8 + reversion_12 | -0.72% | -13.04% | -1.74% | -0.41% | 23.23% |
| breakout_8 AND volume_26 | -0.54% | -3.42% | -1.74% | -0.04% | 2.11% |
| breakout_8 + volume_26 | -0.55% | -11.03% | -1.74% | -0.25% | 13.99% |
| reversion_12 AND volume_26 | 0.60% | -3.54% | -1.74% | -0.06% | 3.43% |
| reversion_12 + volume_26 | -0.67% | -9.45% | -1.74% | -0.31% | 17.68% |
| ema_12_26 | 1.26% | -1.26% | -1.74% | -0.91% | 51.72% |
| macd_12_26_9 | 3.11% | 0.54% | -1.74% | -0.48% | 27.44% |
| rsi_14_recovery | -0.88% | -4.95% | -1.74% | -0.05% | 2.64% |
| bollinger_20_reentry | -0.20% | -4.70% | -1.74% | -0.05% | 2.90% |
| donchian_20 | -0.04% | -4.96% | -1.74% | -0.10% | 5.80% |
| atr_14_breakout | -0.63% | -7.48% | -1.74% | -0.08% | 4.75% |
| session_vwap | 0.22% | -10.52% | -1.74% | -0.81% | 46.44% |
| obv_20 | 1.17% | -2.99% | -1.74% | -0.79% | 44.85% |
| stochastic_14_3_recovery | -0.29% | -12.46% | -1.74% | -0.14% | 8.18% |
| mfi_14_recovery | 0.20% | -3.92% | -1.74% | -0.05% | 2.64% |
| adx_14_trend | -0.18% | -3.48% | -1.74% | -0.62% | 35.36% |
| aroon_25_trend | -0.81% | -5.29% | -1.74% | -0.38% | 21.90% |
| cci_20_momentum | -0.99% | -7.42% | -1.74% | -0.35% | 19.79% |
| williams_14_recovery | 0.42% | -9.21% | -1.74% | -0.11% | 6.33% |
| cmf_20_accumulation | 0.11% | -7.18% | -1.74% | -0.42% | 23.75% |
| chaikin_3_10 | -1.15% | -7.96% | -1.74% | -0.61% | 34.83% |
| roc_10_momentum | -0.02% | -1.27% | -1.74% | -0.09% | 5.01% |
| trix_15_trend | 1.07% | -2.68% | -1.74% | -0.73% | 41.69% |
| keltner_20_breakout | -0.10% | -3.40% | -1.74% | -0.13% | 7.39% |
| opening_range_30m | 2.63% | -1.59% | -1.74% | -0.44% | 25.33% |

동일 구간·초기 자금, 종료 시 청산 비용 포함. 노출 맞춤은 사후 설명용이며 v2 실제 계좌 성과가 아닙니다.
[낙폭 분해·비용 영향·전체 구간](IWM/comparison.json)

[v1 전체 기록](IWM/accounts.json) · [v2 전체 기록](IWM/accounts-v2.json)

## DIA 계좌

| 모델 | 전략 | 평가액 USD | 손익 USD | 최근 매매·이유 |
|---|---|---:|---:|---|
| v1 | cash | 10000.00 | 0.00 | 대기 /  / 새 신호 대기 |
| v1 | buy_hold | 10046.26 | 46.26 | buy /  / buy_hold: prior completed bar target 100%; next bar open simulation |
| v1 | trend_8_26 | 9983.44 | -16.56 | sell /  / trend_8_26: prior completed bar target 0%; next bar open simulation |
| v1 | momentum_26 | 9846.06 | -153.94 | buy /  / momentum_26: prior completed bar target 100%; next bar open simulation |
| v1 | breakout_8 | 9427.60 | -572.40 | sell /  / breakout_8: prior completed bar target 0%; next bar open simulation |
| v1 | reversion_12 | 9822.56 | -177.44 | sell /  / reversion_12: prior completed bar target 0%; next bar open simulation |
| v1 | volume_26 | 9816.03 | -183.97 | sell /  / volume_26: prior completed bar target 0%; next bar open simulation |
| v1 | trend_8_26 AND momentum_26 | 9873.08 | -126.92 | sell /  / trend_8_26 AND momentum_26: prior completed bar target 0%; next bar open simulation |
| v1 | trend_8_26 + momentum_26 | 9914.58 | -85.42 | sell /  / trend_8_26 + momentum_26: prior completed bar target 50%; next bar open simulation |
| v1 | trend_8_26 AND breakout_8 | 9649.65 | -350.35 | sell /  / trend_8_26 AND breakout_8: prior completed bar target 0%; next bar open simulation |
| v1 | trend_8_26 + breakout_8 | 9740.49 | -259.51 | sell /  / trend_8_26 + breakout_8: prior completed bar target 0%; next bar open simulation |
| v1 | trend_8_26 AND reversion_12 | 9865.72 | -134.28 | sell /  / trend_8_26 AND reversion_12: prior completed bar target 0%; next bar open simulation |
| v1 | trend_8_26 + reversion_12 | 9902.48 | -97.52 | sell /  / trend_8_26 + reversion_12: prior completed bar target 0%; next bar open simulation |
| v1 | trend_8_26 AND volume_26 | 9888.21 | -111.79 | sell /  / trend_8_26 AND volume_26: prior completed bar target 0%; next bar open simulation |
| v1 | trend_8_26 + volume_26 | 9899.20 | -100.80 | sell /  / trend_8_26 + volume_26: prior completed bar target 0%; next bar open simulation |
| v1 | momentum_26 AND breakout_8 | 9556.12 | -443.88 | sell /  / momentum_26 AND breakout_8: prior completed bar target 0%; next bar open simulation |
| v1 | momentum_26 + breakout_8 | 9634.65 | -365.35 | sell /  / momentum_26 + breakout_8: prior completed bar target 50%; next bar open simulation |
| v1 | momentum_26 AND reversion_12 | 9865.74 | -134.26 | sell /  / momentum_26 AND reversion_12: prior completed bar target 0%; next bar open simulation |
| v1 | momentum_26 + reversion_12 | 9873.50 | -126.50 | sell /  / momentum_26 + reversion_12: prior completed bar target 50%; next bar open simulation |
| v1 | momentum_26 AND volume_26 | 9805.85 | -194.15 | sell /  / momentum_26 AND volume_26: prior completed bar target 0%; next bar open simulation |
| v1 | momentum_26 + volume_26 | 9850.61 | -149.39 | sell /  / momentum_26 + volume_26: prior completed bar target 50%; next bar open simulation |
| v1 | breakout_8 AND reversion_12 | 10000.00 | 0.00 | 대기 /  / 새 신호 대기 |
| v1 | breakout_8 + reversion_12 | 9642.08 | -357.92 | sell /  / breakout_8 + reversion_12: prior completed bar target 0%; next bar open simulation |
| v1 | breakout_8 AND volume_26 | 9925.92 | -74.08 | sell /  / breakout_8 AND volume_26: prior completed bar target 0%; next bar open simulation |
| v1 | breakout_8 + volume_26 | 9658.32 | -341.68 | sell /  / breakout_8 + volume_26: prior completed bar target 0%; next bar open simulation |
| v1 | reversion_12 AND volume_26 | 9970.42 | -29.58 | sell /  / reversion_12 AND volume_26: prior completed bar target 0%; next bar open simulation |
| v1 | reversion_12 + volume_26 | 9858.49 | -141.51 | sell /  / reversion_12 + volume_26: prior completed bar target 0%; next bar open simulation |
| v1 | ema_12_26 | 9900.38 | -99.62 | buy /  / EMA12 > EMA26; 조건 충족; EMA12=519.74, EMA26=519.585 |
| v1 | macd_12_26_9 | 9863.59 | -136.41 | sell /  / MACD > 신호선 그리고 MACD > 0; 조건 미충족; MACD=0.835411, signal9=0.838693 |
| v1 | rsi_14_recovery | 10000.00 | 0.00 | 대기 /  / 새 신호 대기 |
| v1 | bollinger_20_reentry | 9939.81 | -60.19 | sell /  / 직전 종가 < 직전 하단밴드, 현재 하단밴드 <= 종가 <= SMA20 (한 봉 목표); 조건 미충족; close=525.81, lower20=524.898, SMA20=526.51, previous_lower20=524.945 |
| v1 | donchian_20 | 9741.72 | -258.28 | sell /  / 종가 > 현재 봉을 제외한 직전 20봉 최고가; 조건 미충족; close=526.34, prior_high20=527.79 |
| v1 | atr_14_breakout | 9744.76 | -255.24 | sell /  / 종가 > 직전 종가 + 직전 ATR14 그리고 종가 > EMA26; 조건 미충족; close=526.34, threshold=528.384, prior_ATR14=0.693828, EMA26=525.997 |
| v1 | session_vwap | 9789.44 | -210.56 | buy /  / 종가 > 뉴욕 거래일별 누적 전형가격 VWAP; 조건 충족; close=526.37, session_VWAP=526.232, session_volume=1.64733e+06 |
| v1 | obv_20 | 9851.67 | -148.33 | sell /  / OBV > OBV의 SMA20 그리고 종가 > EMA26; 조건 미충족; OBV=-5.81025e+06, OBV_SMA20=-5.32802e+06, close=526.941, EMA26=526.147 |
| v1 | stochastic_14_3_recovery | 9702.74 | -297.26 | sell /  / 직전 %K14 < 20에서 %K14가 %D3 상향 돌파 (한 봉 목표); 조건 미충족; K14=43.4299, D3=31.8109, previous_K14=42.0016, previous_D3=18.964 |
| v1 | mfi_14_recovery | 9902.01 | -97.99 | sell /  / 직전 MFI14 < 20, 현재 MFI14 >= 20 (한 봉 목표); 조건 미충족; MFI14=29.4378, previous_MFI14=21.6288 |
| v1 | adx_14_trend | 9711.49 | -288.51 | sell /  / Wilder ADX14 >= 25 그리고 +DI14 > -DI14; 조건 미충족; ADX14=28.0997, plus_DI14=30.0206, minus_DI14=36.1913 |
| v1 | aroon_25_trend | 9820.69 | -179.31 | sell /  / Aroon25 Up > 70 그리고 Down < 30 (동률이면 최신 극값); 조건 미충족; Aroon_up=72, Aroon_down=92 |
| v1 | cci_20_momentum | 9812.36 | -187.64 | sell /  / CCI20 > 100 (전형가격·평균절대편차); 조건 미충족; CCI20=-47.7538 |
| v1 | williams_14_recovery | 9735.64 | -264.36 | sell /  / 직전 Williams %R14 < -80, 현재 >= -80 (한 봉 목표); 조건 미충족; Williams_R14=-56.5701, previous_R14=-57.9984 |
| v1 | cmf_20_accumulation | 9571.66 | -428.34 | buy /  / Chaikin Money Flow20 > 0.1; 조건 충족; CMF20=0.162227, volume20=1.04086e+06 |
| v1 | chaikin_3_10 | 9802.10 | -197.90 | buy /  / ADL의 EMA3 - EMA10 > 0 그리고 종가 > EMA26; 조건 충족; Chaikin3_10=215386, ADL=-1.16382e+07, close=526.37, EMA26=525.963 |
| v1 | roc_10_momentum | 9939.01 | -60.99 | sell /  / 10봉 ROC > 1% 그리고 종가 > EMA26; 조건 미충족; ROC10_percent=0.771645, close=523.68, EMA26=521.367 |
| v1 | trix_15_trend | 9935.23 | -64.77 | buy /  / 15봉 삼중 EMA의 1봉 변화율 TRIX > 0 그리고 종가 > EMA26; 조건 충족; TRIX15_percent=0.0108744, close=526.37, EMA26=525.963 |
| v1 | keltner_20_breakout | 9826.82 | -173.18 | sell /  / 종가 > EMA20 + 2 x Wilder ATR14; 조건 미충족; close=526.34, upper_Keltner=527.991, EMA20=526.293, ATR14=0.848911 |
| v1 | opening_range_30m | 9633.56 | -366.44 | sell /  / 뉴욕 09:30·09:45 두 완료 봉 최고가를 10:00 이후 종가가 돌파; 자료 부족·변동폭 또는 거래량 없음: 대기; close=526.34 |
| v2 | cash | 10000.00 | 0.00 | 대기 /  / 새 신호 대기 |
| v2 | buy_hold | 10170.72 | 170.72 | buy / partial / 직전 완료 봉 목표 비중 100%; 다음 봉 시가 가정 |
| v2 | trend_8_26 | 9913.81 | -86.19 | sell / filled / 직전 완료 봉 목표 비중 0%; 다음 봉 시가 가정 |
| v2 | momentum_26 | 9881.92 | -118.08 | buy / partial / 직전 완료 봉 목표 비중 100%; 다음 봉 시가 가정 |
| v2 | breakout_8 | 9002.31 | -997.69 | 중단: 손실 한도 / buy / partial / 직전 완료 봉 목표 비중 100%; 다음 봉 시가 가정 |
| v2 | reversion_12 | 9514.52 | -485.48 | sell / filled / 직전 완료 봉 목표 비중 0%; 다음 봉 시가 가정 |
| v2 | volume_26 | 9526.08 | -473.92 | sell / filled / 직전 완료 봉 목표 비중 0%; 다음 봉 시가 가정 |
| v2 | trend_8_26 AND momentum_26 | 9903.45 | -96.55 | sell / filled / 직전 완료 봉 목표 비중 0%; 다음 봉 시가 가정 |
| v2 | trend_8_26 + momentum_26 | 9897.98 | -102.02 | sell / filled / 직전 완료 봉 목표 비중 50%; 다음 봉 시가 가정 |
| v2 | trend_8_26 AND breakout_8 | 9330.55 | -669.45 | sell / filled / 직전 완료 봉 목표 비중 0%; 다음 봉 시가 가정 |
| v2 | trend_8_26 + breakout_8 | 9463.06 | -536.94 | sell / filled / 직전 완료 봉 목표 비중 0%; 다음 봉 시가 가정 |
| v2 | trend_8_26 AND reversion_12 | 9669.36 | -330.64 | sell / filled / 직전 완료 봉 목표 비중 0%; 다음 봉 시가 가정 |
| v2 | trend_8_26 + reversion_12 | 9711.66 | -288.34 | sell / filled / 직전 완료 봉 목표 비중 0%; 다음 봉 시가 가정 |
| v2 | trend_8_26 AND volume_26 | 9738.93 | -261.07 | sell / filled / 직전 완료 봉 목표 비중 0%; 다음 봉 시가 가정 |
| v2 | trend_8_26 + volume_26 | 9738.20 | -261.80 | sell / filled / 직전 완료 봉 목표 비중 0%; 다음 봉 시가 가정 |
| v2 | momentum_26 AND breakout_8 | 9227.75 | -772.25 | sell / filled / 직전 완료 봉 목표 비중 0%; 다음 봉 시가 가정 |
| v2 | momentum_26 + breakout_8 | 9408.32 | -591.68 | sell / filled / 직전 완료 봉 목표 비중 50%; 다음 봉 시가 가정 |
| v2 | momentum_26 AND reversion_12 | 9814.45 | -185.55 | sell / filled / 직전 완료 봉 목표 비중 0%; 다음 봉 시가 가정 |
| v2 | momentum_26 + reversion_12 | 9736.87 | -263.13 | sell / filled / 직전 완료 봉 목표 비중 50%; 다음 봉 시가 가정 |
| v2 | momentum_26 AND volume_26 | 9589.81 | -410.19 | sell / filled / 직전 완료 봉 목표 비중 0%; 다음 봉 시가 가정 |
| v2 | momentum_26 + volume_26 | 9763.65 | -236.35 | sell / filled / 직전 완료 봉 목표 비중 50%; 다음 봉 시가 가정 |
| v2 | breakout_8 AND reversion_12 | 10000.00 | 0.00 | 대기 /  / 새 신호 대기 |
| v2 | breakout_8 + reversion_12 | 9250.28 | -749.72 | sell / filled / 직전 완료 봉 목표 비중 0%; 다음 봉 시가 가정 |
| v2 | breakout_8 AND volume_26 | 9718.15 | -281.85 | sell / filled / 직전 완료 봉 목표 비중 0%; 다음 봉 시가 가정 |
| v2 | breakout_8 + volume_26 | 9275.78 | -724.22 | sell / filled / 직전 완료 봉 목표 비중 0%; 다음 봉 시가 가정 |
| v2 | reversion_12 AND volume_26 | 9966.44 | -33.56 | sell / filled / 직전 완료 봉 목표 비중 0%; 다음 봉 시가 가정 |
| v2 | reversion_12 + volume_26 | 9559.93 | -440.07 | sell / filled / 직전 완료 봉 목표 비중 0%; 다음 봉 시가 가정 |
| v2 | ema_12_26 | 9895.44 | -104.56 | buy / partial / EMA12 > EMA26; 조건 충족; EMA12=519.74, EMA26=519.585; 직전 완료 봉 목표를 다음 봉 시가에 모의 적용 |
| v2 | macd_12_26_9 | 9855.70 | -144.30 | sell / filled / MACD > 신호선 그리고 MACD > 0; 조건 미충족; MACD=0.835411, signal9=0.838693; 직전 완료 봉 목표를 다음 봉 시가에 모의 적용 |
| v2 | rsi_14_recovery | 10000.00 | 0.00 | 대기 /  / 새 신호 대기 |
| v2 | bollinger_20_reentry | 9935.84 | -64.16 | sell / filled / 직전 종가 < 직전 하단밴드, 현재 하단밴드 <= 종가 <= SMA20 (한 봉 목표); 조건 미충족; close=525.81, lower20=524.898, SMA20=526.51, previous_lower20=524.945; 직전 완료 봉 목표를 다음 봉 시가에 모의 적용 |
| v2 | donchian_20 | 9730.04 | -269.96 | sell / filled / 종가 > 현재 봉을 제외한 직전 20봉 최고가; 조건 미충족; close=526.34, prior_high20=527.79; 직전 완료 봉 목표를 다음 봉 시가에 모의 적용 |
| v2 | atr_14_breakout | 9731.13 | -268.87 | sell / filled / 종가 > 직전 종가 + 직전 ATR14 그리고 종가 > EMA26; 조건 미충족; close=526.34, threshold=528.384, prior_ATR14=0.693828, EMA26=525.997; 직전 완료 봉 목표를 다음 봉 시가에 모의 적용 |
| v2 | session_vwap | 9776.72 | -223.28 | buy / partial / 종가 > 뉴욕 거래일별 누적 전형가격 VWAP; 조건 충족; close=526.37, session_VWAP=526.232, session_volume=1.64733e+06; 직전 완료 봉 목표를 다음 봉 시가에 모의 적용 |
| v2 | obv_20 | 9841.82 | -158.18 | sell / filled / OBV > OBV의 SMA20 그리고 종가 > EMA26; 조건 미충족; OBV=-5.81025e+06, OBV_SMA20=-5.32802e+06, close=526.941, EMA26=526.147; 직전 완료 봉 목표를 다음 봉 시가에 모의 적용 |
| v2 | stochastic_14_3_recovery | 9687.23 | -312.77 | sell / filled / 직전 %K14 < 20에서 %K14가 %D3 상향 돌파 (한 봉 목표); 조건 미충족; K14=43.4299, D3=31.8109, previous_K14=42.0016, previous_D3=18.964; 직전 완료 봉 목표를 다음 봉 시가에 모의 적용 |
| v2 | mfi_14_recovery | 9896.07 | -103.93 | sell / filled / 직전 MFI14 < 20, 현재 MFI14 >= 20 (한 봉 목표); 조건 미충족; MFI14=29.4378, previous_MFI14=21.6288; 직전 완료 봉 목표를 다음 봉 시가에 모의 적용 |
| v2 | adx_14_trend | 9701.78 | -298.22 | sell / filled / Wilder ADX14 >= 25 그리고 +DI14 > -DI14; 조건 미충족; ADX14=28.0997, plus_DI14=30.0206, minus_DI14=36.1913; 직전 완료 봉 목표를 다음 봉 시가에 모의 적용 |
| v2 | aroon_25_trend | 9810.88 | -189.12 | sell / filled / Aroon25 Up > 70 그리고 Down < 30 (동률이면 최신 극값); 조건 미충족; Aroon_up=72, Aroon_down=92; 직전 완료 봉 목표를 다음 봉 시가에 모의 적용 |
| v2 | cci_20_momentum | 9800.59 | -199.41 | sell / filled / CCI20 > 100 (전형가격·평균절대편차); 조건 미충족; CCI20=-47.7538; 직전 완료 봉 목표를 다음 봉 시가에 모의 적용 |
| v2 | williams_14_recovery | 9722.02 | -277.98 | sell / filled / 직전 Williams %R14 < -80, 현재 >= -80 (한 봉 목표); 조건 미충족; Williams_R14=-56.5701, previous_R14=-57.9984; 직전 완료 봉 목표를 다음 봉 시가에 모의 적용 |
| v2 | cmf_20_accumulation | 9553.49 | -446.51 | buy / partial / Chaikin Money Flow20 > 0.1; 조건 충족; CMF20=0.162227, volume20=1.04086e+06; 직전 완료 봉 목표를 다음 봉 시가에 모의 적용 |
| v2 | chaikin_3_10 | 9791.32 | -208.68 | buy / partial / ADL의 EMA3 - EMA10 > 0 그리고 종가 > EMA26; 조건 충족; Chaikin3_10=215386, ADL=-1.16382e+07, close=526.37, EMA26=525.963; 직전 완료 봉 목표를 다음 봉 시가에 모의 적용 |
| v2 | roc_10_momentum | 9937.03 | -62.97 | sell / filled / 10봉 ROC > 1% 그리고 종가 > EMA26; 조건 미충족; ROC10_percent=0.771645, close=523.68, EMA26=521.367; 직전 완료 봉 목표를 다음 봉 시가에 모의 적용 |
| v2 | trix_15_trend | 9930.27 | -69.73 | buy / partial / 15봉 삼중 EMA의 1봉 변화율 TRIX > 0 그리고 종가 > EMA26; 조건 충족; TRIX15_percent=0.0108744, close=526.37, EMA26=525.963; 직전 완료 봉 목표를 다음 봉 시가에 모의 적용 |
| v2 | keltner_20_breakout | 9817.00 | -183.00 | sell / filled / 종가 > EMA20 + 2 x Wilder ATR14; 조건 미충족; close=526.34, upper_Keltner=527.991, EMA20=526.293, ATR14=0.848911; 직전 완료 봉 목표를 다음 봉 시가에 모의 적용 |
| v2 | opening_range_30m | 9618.16 | -381.84 | sell / filled / 뉴욕 09:30·09:45 두 완료 봉 최고가를 10:00 이후 종가가 돌파; 자료 부족·변동폭 또는 거래량 없음: 대기; close=526.34; 직전 완료 봉 목표를 다음 봉 시가에 모의 적용 |

### 같은 기간의 비용·노출 비교 (사후 연구)

| 전략 | 비용 전 | 비용 후 | 100% 보유 | 같은 평균 노출 보유 | 평균 노출 |
|---|---:|---:|---:|---:|---:|
| cash | 0.00% | 0.00% | 3.12% | 0.00% | 0.00% |
| buy_hold | 3.55% | 3.12% | 3.12% | 3.12% | 100.00% |
| trend_8_26 | 3.28% | -0.55% | 3.12% | 2.11% | 67.81% |
| momentum_26 | 1.44% | -2.74% | 3.12% | 1.98% | 63.85% |
| breakout_8 | 0.47% | -17.53% | 3.12% | 0.80% | 25.86% |
| reversion_12 | 0.92% | -6.82% | 3.12% | 0.55% | 17.94% |
| volume_26 | 0.99% | -8.31% | 3.12% | 0.32% | 10.29% |
| trend_8_26 AND momentum_26 | 2.94% | -1.30% | 3.12% | 1.80% | 58.05% |
| trend_8_26 + momentum_26 | 2.36% | -1.65% | 3.12% | 2.04% | 65.83% |
| trend_8_26 AND breakout_8 | 1.43% | -12.44% | 3.12% | 0.59% | 19.26% |
| trend_8_26 + breakout_8 | 1.87% | -8.86% | 3.12% | 1.45% | 46.84% |
| trend_8_26 AND reversion_12 | 0.81% | -4.55% | 3.12% | 0.22% | 7.12% |
| trend_8_26 + reversion_12 | 2.10% | -3.54% | 3.12% | 1.33% | 42.88% |
| trend_8_26 AND volume_26 | 1.59% | -4.61% | 3.12% | 0.19% | 6.33% |
| trend_8_26 + volume_26 | 2.13% | -4.31% | 3.12% | 1.21% | 39.05% |
| momentum_26 AND breakout_8 | 0.02% | -14.02% | 3.12% | 0.63% | 20.58% |
| momentum_26 + breakout_8 | 0.96% | -10.24% | 3.12% | 1.39% | 44.86% |
| momentum_26 AND reversion_12 | 0.10% | -3.21% | 3.12% | 0.17% | 5.54% |
| momentum_26 + reversion_12 | 1.18% | -4.00% | 3.12% | 1.27% | 40.90% |
| momentum_26 AND volume_26 | 0.04% | -6.85% | 3.12% | 0.20% | 6.60% |
| momentum_26 + volume_26 | 1.22% | -4.97% | 3.12% | 1.15% | 37.08% |
| breakout_8 AND reversion_12 | 0.00% | 0.00% | 3.12% | 0.00% | 0.00% |
| breakout_8 + reversion_12 | 0.70% | -11.98% | 3.12% | 0.68% | 21.91% |
| breakout_8 AND volume_26 | -0.27% | -4.37% | 3.12% | 0.11% | 3.69% |
| breakout_8 + volume_26 | 0.73% | -12.13% | 3.12% | 0.56% | 18.08% |
| reversion_12 AND volume_26 | 0.94% | -1.99% | 3.12% | 0.06% | 2.11% |
| reversion_12 + volume_26 | 0.95% | -7.19% | 3.12% | 0.44% | 14.12% |
| ema_12_26 | 1.22% | -1.30% | 3.12% | 1.97% | 63.59% |
| macd_12_26_9 | 2.33% | -1.47% | 3.12% | 1.04% | 33.51% |
| rsi_14_recovery | 0.14% | -0.69% | 3.12% | 0.02% | 0.53% |
| bollinger_20_reentry | 0.35% | -2.56% | 3.12% | 0.06% | 1.85% |
| donchian_20 | 0.34% | -7.74% | 3.12% | 0.34% | 11.08% |
| atr_14_breakout | -0.50% | -8.90% | 3.12% | 0.20% | 6.60% |
| session_vwap | 2.70% | -4.78% | 3.12% | 1.82% | 58.58% |
| obv_20 | 1.81% | -5.61% | 3.12% | 1.63% | 52.51% |
| stochastic_14_3_recovery | 1.36% | -9.12% | 3.12% | 0.21% | 6.86% |
| mfi_14_recovery | 0.37% | -2.95% | 3.12% | 0.06% | 2.11% |
| adx_14_trend | -0.02% | -4.14% | 3.12% | 1.04% | 33.77% |
| aroon_25_trend | 1.33% | -2.84% | 3.12% | 0.93% | 30.08% |
| cci_20_momentum | 1.32% | -5.66% | 3.12% | 0.91% | 29.55% |
| williams_14_recovery | 1.55% | -5.85% | 3.12% | 0.15% | 4.75% |
| cmf_20_accumulation | 1.01% | -8.68% | 3.12% | 1.22% | 39.58% |
| chaikin_3_10 | 2.41% | -7.02% | 3.12% | 1.71% | 55.15% |
| roc_10_momentum | -0.07% | -0.90% | 3.12% | 0.06% | 2.11% |
| trix_15_trend | 1.07% | -2.68% | 3.12% | 1.76% | 56.73% |
| keltner_20_breakout | 0.79% | -6.94% | 3.12% | 0.63% | 20.32% |
| opening_range_30m | 1.31% | -5.67% | 3.12% | 0.99% | 31.93% |

동일 구간·초기 자금, 종료 시 청산 비용 포함. 노출 맞춤은 사후 설명용이며 v2 실제 계좌 성과가 아닙니다.
[낙폭 분해·비용 영향·전체 구간](DIA/comparison.json)

[v1 전체 기록](DIA/accounts.json) · [v2 전체 기록](DIA/accounts-v2.json)

## MSFT 계좌

| 모델 | 전략 | 평가액 USD | 손익 USD | 최근 매매·이유 |
|---|---|---:|---:|---|
| v1 | cash | 10000.00 | 0.00 | 대기 /  / 새 신호 대기 |
| v1 | buy_hold | 9669.41 | -330.59 | buy /  / buy_hold: prior completed bar target 100%; next bar open simulation |
| v1 | trend_8_26 | 9433.22 | -566.78 | sell /  / trend_8_26: prior completed bar target 0%; next bar open simulation |
| v1 | momentum_26 | 9297.87 | -702.13 | sell /  / momentum_26: prior completed bar target 0%; next bar open simulation |
| v1 | breakout_8 | 9511.89 | -488.11 | sell /  / breakout_8: prior completed bar target 0%; next bar open simulation |
| v1 | reversion_12 | 9431.50 | -568.50 | sell /  / reversion_12: prior completed bar target 0%; next bar open simulation |
| v1 | volume_26 | 9631.28 | -368.72 | sell /  / volume_26: prior completed bar target 0%; next bar open simulation |
| v1 | trend_8_26 AND momentum_26 | 9427.87 | -572.13 | sell /  / trend_8_26 AND momentum_26: prior completed bar target 0%; next bar open simulation |
| v1 | trend_8_26 + momentum_26 | 9402.84 | -597.16 | sell /  / trend_8_26 + momentum_26: prior completed bar target 0%; next bar open simulation |
| v1 | trend_8_26 AND breakout_8 | 9678.51 | -321.49 | sell /  / trend_8_26 AND breakout_8: prior completed bar target 0%; next bar open simulation |
| v1 | trend_8_26 + breakout_8 | 9510.67 | -489.33 | sell /  / trend_8_26 + breakout_8: prior completed bar target 0%; next bar open simulation |
| v1 | trend_8_26 AND reversion_12 | 9519.35 | -480.65 | sell /  / trend_8_26 AND reversion_12: prior completed bar target 0%; next bar open simulation |
| v1 | trend_8_26 + reversion_12 | 9451.14 | -548.86 | sell /  / trend_8_26 + reversion_12: prior completed bar target 0%; next bar open simulation |
| v1 | trend_8_26 AND volume_26 | 9802.11 | -197.89 | sell /  / trend_8_26 AND volume_26: prior completed bar target 0%; next bar open simulation |
| v1 | trend_8_26 + volume_26 | 9531.86 | -468.14 | sell /  / trend_8_26 + volume_26: prior completed bar target 0%; next bar open simulation |
| v1 | momentum_26 AND breakout_8 | 9642.25 | -357.75 | sell /  / momentum_26 AND breakout_8: prior completed bar target 0%; next bar open simulation |
| v1 | momentum_26 + breakout_8 | 9423.30 | -576.70 | sell /  / momentum_26 + breakout_8: prior completed bar target 0%; next bar open simulation |
| v1 | momentum_26 AND reversion_12 | 9649.76 | -350.24 | sell /  / momentum_26 AND reversion_12: prior completed bar target 0%; next bar open simulation |
| v1 | momentum_26 + reversion_12 | 9420.66 | -579.34 | sell /  / momentum_26 + reversion_12: prior completed bar target 0%; next bar open simulation |
| v1 | momentum_26 AND volume_26 | 9830.16 | -169.84 | sell /  / momentum_26 AND volume_26: prior completed bar target 0%; next bar open simulation |
| v1 | momentum_26 + volume_26 | 9482.29 | -517.71 | sell /  / momentum_26 + volume_26: prior completed bar target 0%; next bar open simulation |
| v1 | breakout_8 AND reversion_12 | 10000.00 | 0.00 | 대기 /  / 새 신호 대기 |
| v1 | breakout_8 + reversion_12 | 9509.38 | -490.62 | sell /  / breakout_8 + reversion_12: prior completed bar target 0%; next bar open simulation |
| v1 | breakout_8 AND volume_26 | 9953.19 | -46.81 | sell /  / breakout_8 AND volume_26: prior completed bar target 0%; next bar open simulation |
| v1 | breakout_8 + volume_26 | 9609.59 | -390.41 | sell /  / breakout_8 + volume_26: prior completed bar target 0%; next bar open simulation |
| v1 | reversion_12 AND volume_26 | 9770.39 | -229.61 | sell /  / reversion_12 AND volume_26: prior completed bar target 0%; next bar open simulation |
| v1 | reversion_12 + volume_26 | 9549.87 | -450.13 | sell /  / reversion_12 + volume_26: prior completed bar target 0%; next bar open simulation |
| v1 | ema_12_26 | 9491.42 | -508.58 | sell /  / EMA12 > EMA26; 조건 미충족; EMA12=531.766, EMA26=531.788 |
| v1 | macd_12_26_9 | 9603.93 | -396.07 | sell /  / MACD > 신호선 그리고 MACD > 0; 조건 미충족; MACD=-0.0222122, signal9=0.149678 |
| v1 | rsi_14_recovery | 9932.10 | -67.90 | sell /  / 직전 RSI14 < 30, 현재 RSI14 >= 30 (한 봉 목표); 조건 미충족; RSI14=39.2066, previous_RSI14=35.1952 |
| v1 | bollinger_20_reentry | 9789.12 | -210.88 | sell /  / 직전 종가 < 직전 하단밴드, 현재 하단밴드 <= 종가 <= SMA20 (한 봉 목표); 조건 미충족; close=526.675, lower20=523.276, SMA20=530.073, previous_lower20=523.675 |
| v1 | donchian_20 | 9912.16 | -87.84 | sell /  / 종가 > 현재 봉을 제외한 직전 20봉 최고가; 조건 미충족; close=534.52, prior_high20=535.44 |
| v1 | atr_14_breakout | 9915.10 | -84.90 | sell /  / 종가 > 직전 종가 + 직전 ATR14 그리고 종가 > EMA26; 조건 미충족; close=533.975, threshold=536.307, prior_ATR14=2.16203, EMA26=530.521 |
| v1 | session_vwap | 9717.73 | -282.27 | buy /  / 종가 > 뉴욕 거래일별 누적 전형가격 VWAP; 조건 충족; close=525.83, session_VWAP=524.714, session_volume=1.25707e+07 |
| v1 | obv_20 | 9537.51 | -462.49 | sell /  / OBV > OBV의 SMA20 그리고 종가 > EMA26; 조건 미충족; OBV=5.91823e+07, OBV_SMA20=5.93103e+07, close=529.54, EMA26=531.788 |
| v1 | stochastic_14_3_recovery | 9762.71 | -237.29 | sell /  / 직전 %K14 < 20에서 %K14가 %D3 상향 돌파 (한 봉 목표); 조건 미충족; K14=30.8831, D3=15.7231, previous_K14=13.0832, previous_D3=6.79346 |
| v1 | mfi_14_recovery | 9972.58 | -27.42 | sell /  / 직전 MFI14 < 20, 현재 MFI14 >= 20 (한 봉 목표); 조건 미충족; MFI14=53.413, previous_MFI14=44.3372 |
| v1 | adx_14_trend | 9883.62 | -116.38 | sell /  / Wilder ADX14 >= 25 그리고 +DI14 > -DI14; 조건 미충족; ADX14=23.6824, plus_DI14=22.3066, minus_DI14=19.9214 |
| v1 | aroon_25_trend | 9616.60 | -383.40 | sell /  / Aroon25 Up > 70 그리고 Down < 30 (동률이면 최신 극값); 조건 미충족; Aroon_up=96, Aroon_down=100 |
| v1 | cci_20_momentum | 9912.64 | -87.36 | sell /  / CCI20 > 100 (전형가격·평균절대편차); 조건 미충족; CCI20=96.8192 |
| v1 | williams_14_recovery | 9701.70 | -298.30 | sell /  / 직전 Williams %R14 < -80, 현재 >= -80 (한 봉 목표); 조건 미충족; Williams_R14=-61.5967, previous_R14=-69.1169 |
| v1 | cmf_20_accumulation | 9596.53 | -403.47 | buy /  / Chaikin Money Flow20 > 0.1; 조건 충족; CMF20=0.18569, volume20=1.61634e+07 |
| v1 | chaikin_3_10 | 9575.46 | -424.54 | sell /  / ADL의 EMA3 - EMA10 > 0 그리고 종가 > EMA26; 조건 미충족; Chaikin3_10=-50549, ADL=1.1482e+08, close=529.54, EMA26=531.788 |
| v1 | roc_10_momentum | 9959.43 | -40.57 | sell /  / 10봉 ROC > 1% 그리고 종가 > EMA26; 조건 미충족; ROC10_percent=0.454191, close=534.125, EMA26=532.186 |
| v1 | trix_15_trend | 9557.09 | -442.91 | sell /  / 15봉 삼중 EMA의 1봉 변화율 TRIX > 0 그리고 종가 > EMA26; 조건 미충족; TRIX15_percent=0.00481299, close=529.54, EMA26=531.788 |
| v1 | keltner_20_breakout | 9958.78 | -41.22 | sell /  / 종가 > EMA20 + 2 x Wilder ATR14; 조건 미충족; close=533.975, upper_Keltner=534.357, EMA20=530.111, ATR14=2.12332 |
| v1 | opening_range_30m | 9589.30 | -410.70 | sell /  / 뉴욕 09:30·09:45 두 완료 봉 최고가를 10:00 이후 종가가 돌파; 자료 부족·변동폭 또는 거래량 없음: 대기; close=529.54 |
| v2 | cash | 10000.00 | 0.00 | 대기 /  / 새 신호 대기 |
| v2 | buy_hold | 9722.17 | -277.83 | buy / partial / 직전 완료 봉 목표 비중 100%; 다음 봉 시가 가정 |
| v2 | trend_8_26 | 9366.79 | -633.21 | sell / filled / 직전 완료 봉 목표 비중 0%; 다음 봉 시가 가정 |
| v2 | momentum_26 | 9327.21 | -672.79 | sell / filled / 직전 완료 봉 목표 비중 0%; 다음 봉 시가 가정 |
| v2 | breakout_8 | 9298.81 | -701.19 | sell / filled / 직전 완료 봉 목표 비중 0%; 다음 봉 시가 가정 |
| v2 | reversion_12 | 9055.49 | -944.51 | sell / filled / 직전 완료 봉 목표 비중 0%; 다음 봉 시가 가정 |
| v2 | volume_26 | 9314.53 | -685.47 | sell / filled / 직전 완료 봉 목표 비중 0%; 다음 봉 시가 가정 |
| v2 | trend_8_26 AND momentum_26 | 9320.43 | -679.57 | sell / filled / 직전 완료 봉 목표 비중 0%; 다음 봉 시가 가정 |
| v2 | trend_8_26 + momentum_26 | 9386.57 | -613.43 | sell / filled / 직전 완료 봉 목표 비중 0%; 다음 봉 시가 가정 |
| v2 | trend_8_26 AND breakout_8 | 9318.21 | -681.79 | sell / filled / 직전 완료 봉 목표 비중 0%; 다음 봉 시가 가정 |
| v2 | trend_8_26 + breakout_8 | 9392.14 | -607.86 | sell / filled / 직전 완료 봉 목표 비중 0%; 다음 봉 시가 가정 |
| v2 | trend_8_26 AND reversion_12 | 9411.07 | -588.93 | sell / filled / 직전 완료 봉 목표 비중 0%; 다음 봉 시가 가정 |
| v2 | trend_8_26 + reversion_12 | 9228.75 | -771.25 | sell / filled / 직전 완료 봉 목표 비중 0%; 다음 봉 시가 가정 |
| v2 | trend_8_26 AND volume_26 | 9743.99 | -256.01 | sell / filled / 직전 완료 봉 목표 비중 0%; 다음 봉 시가 가정 |
| v2 | trend_8_26 + volume_26 | 9360.19 | -639.81 | sell / filled / 직전 완료 봉 목표 비중 0%; 다음 봉 시가 가정 |
| v2 | momentum_26 AND breakout_8 | 9430.77 | -569.23 | sell / filled / 직전 완료 봉 목표 비중 0%; 다음 봉 시가 가정 |
| v2 | momentum_26 + breakout_8 | 9332.85 | -667.15 | sell / filled / 직전 완료 봉 목표 비중 0%; 다음 봉 시가 가정 |
| v2 | momentum_26 AND reversion_12 | 9475.12 | -524.88 | sell / filled / 직전 완료 봉 목표 비중 0%; 다음 봉 시가 가정 |
| v2 | momentum_26 + reversion_12 | 9248.07 | -751.93 | sell / filled / 직전 완료 봉 목표 비중 0%; 다음 봉 시가 가정 |
| v2 | momentum_26 AND volume_26 | 9695.84 | -304.16 | sell / filled / 직전 완료 봉 목표 비중 0%; 다음 봉 시가 가정 |
| v2 | momentum_26 + volume_26 | 9360.27 | -639.73 | sell / filled / 직전 완료 봉 목표 비중 0%; 다음 봉 시가 가정 |
| v2 | breakout_8 AND reversion_12 | 10000.00 | 0.00 | 대기 /  / 새 신호 대기 |
| v2 | breakout_8 + reversion_12 | 9233.90 | -766.10 | sell / filled / 직전 완료 봉 목표 비중 0%; 다음 봉 시가 가정 |
| v2 | breakout_8 AND volume_26 | 9890.09 | -109.91 | sell / filled / 직전 완료 봉 목표 비중 0%; 다음 봉 시가 가정 |
| v2 | breakout_8 + volume_26 | 9365.33 | -634.67 | sell / filled / 직전 완료 봉 목표 비중 0%; 다음 봉 시가 가정 |
| v2 | reversion_12 AND volume_26 | 9528.36 | -471.64 | sell / filled / 직전 완료 봉 목표 비중 0%; 다음 봉 시가 가정 |
| v2 | reversion_12 + volume_26 | 9203.15 | -796.85 | sell / filled / 직전 완료 봉 목표 비중 0%; 다음 봉 시가 가정 |
| v2 | ema_12_26 | 9483.83 | -516.17 | sell / filled / EMA12 > EMA26; 조건 미충족; EMA12=531.766, EMA26=531.788; 직전 완료 봉 목표를 다음 봉 시가에 모의 적용 |
| v2 | macd_12_26_9 | 9594.34 | -405.66 | sell / filled / MACD > 신호선 그리고 MACD > 0; 조건 미충족; MACD=-0.0222122, signal9=0.149678; 직전 완료 봉 목표를 다음 봉 시가에 모의 적용 |
| v2 | rsi_14_recovery | 9924.16 | -75.84 | sell / filled / 직전 RSI14 < 30, 현재 RSI14 >= 30 (한 봉 목표); 조건 미충족; RSI14=39.2066, previous_RSI14=35.1952; 직전 완료 봉 목표를 다음 봉 시가에 모의 적용 |
| v2 | bollinger_20_reentry | 9779.33 | -220.67 | sell / filled / 직전 종가 < 직전 하단밴드, 현재 하단밴드 <= 종가 <= SMA20 (한 봉 목표); 조건 미충족; close=526.675, lower20=523.276, SMA20=530.073, previous_lower20=523.675; 직전 완료 봉 목표를 다음 봉 시가에 모의 적용 |
| v2 | donchian_20 | 9908.19 | -91.81 | sell / filled / 종가 > 현재 봉을 제외한 직전 20봉 최고가; 조건 미충족; close=534.52, prior_high20=535.44; 직전 완료 봉 목표를 다음 봉 시가에 모의 적용 |
| v2 | atr_14_breakout | 9911.14 | -88.86 | sell / filled / 종가 > 직전 종가 + 직전 ATR14 그리고 종가 > EMA26; 조건 미충족; close=533.975, threshold=536.307, prior_ATR14=2.16203, EMA26=530.521; 직전 완료 봉 목표를 다음 봉 시가에 모의 적용 |
| v2 | session_vwap | 9707.05 | -292.95 | buy / partial / 종가 > 뉴욕 거래일별 누적 전형가격 VWAP; 조건 충족; close=525.83, session_VWAP=524.714, session_volume=1.25707e+07; 직전 완료 봉 목표를 다음 봉 시가에 모의 적용 |
| v2 | obv_20 | 9520.36 | -479.64 | sell / filled / OBV > OBV의 SMA20 그리고 종가 > EMA26; 조건 미충족; OBV=5.91823e+07, OBV_SMA20=5.93103e+07, close=529.54, EMA26=531.788; 직전 완료 봉 목표를 다음 봉 시가에 모의 적용 |
| v2 | stochastic_14_3_recovery | 9749.05 | -250.95 | sell / filled / 직전 %K14 < 20에서 %K14가 %D3 상향 돌파 (한 봉 목표); 조건 미충족; K14=30.8831, D3=15.7231, previous_K14=13.0832, previous_D3=6.79346; 직전 완료 봉 목표를 다음 봉 시가에 모의 적용 |
| v2 | mfi_14_recovery | 9968.59 | -31.41 | sell / filled / 직전 MFI14 < 20, 현재 MFI14 >= 20 (한 봉 목표); 조건 미충족; MFI14=53.413, previous_MFI14=44.3372; 직전 완료 봉 목표를 다음 봉 시가에 모의 적용 |
| v2 | adx_14_trend | 9879.67 | -120.33 | sell / filled / Wilder ADX14 >= 25 그리고 +DI14 > -DI14; 조건 미충족; ADX14=23.6824, plus_DI14=22.3066, minus_DI14=19.9214; 직전 완료 봉 목표를 다음 봉 시가에 모의 적용 |
| v2 | aroon_25_trend | 9608.91 | -391.09 | sell / filled / Aroon25 Up > 70 그리고 Down < 30 (동률이면 최신 극값); 조건 미충족; Aroon_up=96, Aroon_down=100; 직전 완료 봉 목표를 다음 봉 시가에 모의 적용 |
| v2 | cci_20_momentum | 9906.70 | -93.30 | sell / filled / CCI20 > 100 (전형가격·평균절대편차); 조건 미충족; CCI20=96.8192; 직전 완료 봉 목표를 다음 봉 시가에 모의 적용 |
| v2 | williams_14_recovery | 9688.12 | -311.88 | sell / filled / 직전 Williams %R14 < -80, 현재 >= -80 (한 봉 목표); 조건 미충족; Williams_R14=-61.5967, previous_R14=-69.1169; 직전 완료 봉 목표를 다음 봉 시가에 모의 적용 |
| v2 | cmf_20_accumulation | 9587.90 | -412.10 | buy / partial / Chaikin Money Flow20 > 0.1; 조건 충족; CMF20=0.18569, volume20=1.61634e+07; 직전 완료 봉 목표를 다음 봉 시가에 모의 적용 |
| v2 | chaikin_3_10 | 9560.15 | -439.85 | sell / filled / ADL의 EMA3 - EMA10 > 0 그리고 종가 > EMA26; 조건 미충족; Chaikin3_10=-50549, ADL=1.1482e+08, close=529.54, EMA26=531.788; 직전 완료 봉 목표를 다음 봉 시가에 모의 적용 |
| v2 | roc_10_momentum | 9957.44 | -42.56 | sell / filled / 10봉 ROC > 1% 그리고 종가 > EMA26; 조건 미충족; ROC10_percent=0.454191, close=534.125, EMA26=532.186; 직전 완료 봉 목표를 다음 봉 시가에 모의 적용 |
| v2 | trix_15_trend | 9549.45 | -450.55 | sell / filled / 15봉 삼중 EMA의 1봉 변화율 TRIX > 0 그리고 종가 > EMA26; 조건 미충족; TRIX15_percent=0.00481299, close=529.54, EMA26=531.788; 직전 완료 봉 목표를 다음 봉 시가에 모의 적용 |
| v2 | keltner_20_breakout | 9956.78 | -43.22 | sell / filled / 종가 > EMA20 + 2 x Wilder ATR14; 조건 미충족; close=533.975, upper_Keltner=534.357, EMA20=530.111, ATR14=2.12332; 직전 완료 봉 목표를 다음 봉 시가에 모의 적용 |
| v2 | opening_range_30m | 9581.64 | -418.36 | sell / filled / 뉴욕 09:30·09:45 두 완료 봉 최고가를 10:00 이후 종가가 돌파; 자료 부족·변동폭 또는 거래량 없음: 대기; close=529.54; 직전 완료 봉 목표를 다음 봉 시가에 모의 적용 |

### 같은 기간의 비용·노출 비교 (사후 연구)

| 전략 | 비용 전 | 비용 후 | 100% 보유 | 같은 평균 노출 보유 | 평균 노출 |
|---|---:|---:|---:|---:|---:|
| cash | 0.00% | 0.00% | 1.17% | 0.00% | 0.00% |
| buy_hold | 1.60% | 1.17% | 1.17% | 1.17% | 100.00% |
| trend_8_26 | -2.28% | -5.90% | 1.17% | 0.69% | 59.10% |
| momentum_26 | -1.02% | -8.23% | 1.17% | 0.66% | 57.26% |
| breakout_8 | 5.71% | -9.12% | 1.17% | 0.24% | 20.58% |
| reversion_12 | -5.45% | -14.15% | 1.17% | 0.29% | 25.07% |
| volume_26 | 0.54% | -8.33% | 1.17% | 0.10% | 8.97% |
| trend_8_26 AND momentum_26 | -2.66% | -8.98% | 1.17% | 0.59% | 50.92% |
| trend_8_26 + momentum_26 | -1.64% | -6.67% | 1.17% | 0.67% | 58.18% |
| trend_8_26 AND breakout_8 | -0.15% | -10.48% | 1.17% | 0.14% | 12.66% |
| trend_8_26 + breakout_8 | 1.66% | -6.74% | 1.17% | 0.46% | 39.85% |
| trend_8_26 AND reversion_12 | -2.62% | -8.95% | 1.17% | 0.09% | 7.65% |
| trend_8_26 + reversion_12 | -3.86% | -9.75% | 1.17% | 0.49% | 42.09% |
| trend_8_26 AND volume_26 | 2.03% | -1.75% | 1.17% | 0.04% | 3.17% |
| trend_8_26 + volume_26 | -0.86% | -6.74% | 1.17% | 0.39% | 34.04% |
| momentum_26 AND breakout_8 | 2.14% | -8.81% | 1.17% | 0.15% | 13.19% |
| momentum_26 + breakout_8 | 2.30% | -8.09% | 1.17% | 0.45% | 38.92% |
| momentum_26 AND reversion_12 | -3.22% | -9.51% | 1.17% | 0.11% | 9.23% |
| momentum_26 + reversion_12 | -3.24% | -10.68% | 1.17% | 0.47% | 41.17% |
| momentum_26 AND volume_26 | 1.17% | -3.40% | 1.17% | 0.04% | 3.43% |
| momentum_26 + volume_26 | -0.23% | -7.70% | 1.17% | 0.38% | 33.12% |
| breakout_8 AND reversion_12 | 0.00% | 0.00% | 1.17% | 0.00% | 0.00% |
| breakout_8 + reversion_12 | 0.00% | -10.74% | 1.17% | 0.26% | 22.83% |
| breakout_8 AND volume_26 | 2.04% | -0.50% | 1.17% | 0.02% | 1.85% |
| breakout_8 + volume_26 | 3.11% | -7.95% | 1.17% | 0.17% | 14.78% |
| reversion_12 AND volume_26 | -2.90% | -7.29% | 1.17% | 0.05% | 4.22% |
| reversion_12 + volume_26 | -2.49% | -11.10% | 1.17% | 0.20% | 17.02% |
| ema_12_26 | -1.37% | -5.03% | 1.17% | 0.68% | 58.31% |
| macd_12_26_9 | -1.23% | -6.87% | 1.17% | 0.40% | 35.09% |
| rsi_14_recovery | 0.46% | -2.45% | 1.17% | 0.02% | 1.85% |
| bollinger_20_reentry | -0.59% | -3.87% | 1.17% | 0.02% | 2.11% |
| donchian_20 | 1.05% | -4.32% | 1.17% | 0.05% | 4.22% |
| atr_14_breakout | 1.62% | -2.97% | 1.17% | 0.04% | 3.17% |
| session_vwap | 5.08% | -2.98% | 1.17% | 0.53% | 46.17% |
| obv_20 | 4.66% | -4.58% | 1.17% | 0.60% | 52.24% |
| stochastic_14_3_recovery | -0.10% | -9.30% | 1.17% | 0.07% | 6.07% |
| mfi_14_recovery | 1.84% | -1.53% | 1.17% | 0.02% | 2.11% |
| adx_14_trend | 4.03% | 1.87% | 1.17% | 0.51% | 43.80% |
| aroon_25_trend | -1.70% | -6.53% | 1.17% | 0.27% | 23.22% |
| cci_20_momentum | 2.85% | -3.43% | 1.17% | 0.24% | 21.11% |
| williams_14_recovery | -1.22% | -9.56% | 1.17% | 0.06% | 5.54% |
| cmf_20_accumulation | 0.20% | -6.31% | 1.17% | 0.49% | 42.48% |
| chaikin_3_10 | 3.57% | -4.77% | 1.17% | 0.58% | 50.40% |
| roc_10_momentum | -0.61% | -4.30% | 1.17% | 0.15% | 13.19% |
| trix_15_trend | -1.48% | -5.53% | 1.17% | 0.51% | 44.59% |
| keltner_20_breakout | 0.49% | -4.45% | 1.17% | 0.13% | 11.61% |
| opening_range_30m | -1.39% | -5.05% | 1.17% | 0.24% | 20.84% |

동일 구간·초기 자금, 종료 시 청산 비용 포함. 노출 맞춤은 사후 설명용이며 v2 실제 계좌 성과가 아닙니다.
[낙폭 분해·비용 영향·전체 구간](MSFT/comparison.json)

[v1 전체 기록](MSFT/accounts.json) · [v2 전체 기록](MSFT/accounts-v2.json)

## JPM 계좌

| 모델 | 전략 | 평가액 USD | 손익 USD | 최근 매매·이유 |
|---|---|---:|---:|---|
| v1 | cash | 10000.00 | 0.00 | 대기 /  / 새 신호 대기 |
| v1 | buy_hold | 9820.60 | -179.40 | buy /  / buy_hold: prior completed bar target 100%; next bar open simulation |
| v1 | trend_8_26 | 9709.94 | -290.06 | sell /  / trend_8_26: prior completed bar target 0%; next bar open simulation |
| v1 | momentum_26 | 9447.21 | -552.79 | sell /  / momentum_26: prior completed bar target 0%; next bar open simulation |
| v1 | breakout_8 | 9582.11 | -417.89 | sell /  / breakout_8: prior completed bar target 0%; next bar open simulation |
| v1 | reversion_12 | 9568.75 | -431.25 | buy /  / reversion_12: prior completed bar target 100%; next bar open simulation |
| v1 | volume_26 | 9920.77 | -79.23 | sell /  / volume_26: prior completed bar target 0%; next bar open simulation |
| v1 | trend_8_26 AND momentum_26 | 9591.12 | -408.88 | sell /  / trend_8_26 AND momentum_26: prior completed bar target 0%; next bar open simulation |
| v1 | trend_8_26 + momentum_26 | 9577.80 | -422.20 | sell /  / trend_8_26 + momentum_26: prior completed bar target 0%; next bar open simulation |
| v1 | trend_8_26 AND breakout_8 | 9808.13 | -191.87 | sell /  / trend_8_26 AND breakout_8: prior completed bar target 0%; next bar open simulation |
| v1 | trend_8_26 + breakout_8 | 9684.52 | -315.48 | sell /  / trend_8_26 + breakout_8: prior completed bar target 0%; next bar open simulation |
| v1 | trend_8_26 AND reversion_12 | 9757.16 | -242.84 | sell /  / trend_8_26 AND reversion_12: prior completed bar target 0%; next bar open simulation |
| v1 | trend_8_26 + reversion_12 | 9638.99 | -361.01 | sell /  / trend_8_26 + reversion_12: prior completed bar target 50%; next bar open simulation |
| v1 | trend_8_26 AND volume_26 | 10103.61 | 103.61 | sell /  / trend_8_26 AND volume_26: prior completed bar target 0%; next bar open simulation |
| v1 | trend_8_26 + volume_26 | 9814.64 | -185.36 | sell /  / trend_8_26 + volume_26: prior completed bar target 0%; next bar open simulation |
| v1 | momentum_26 AND breakout_8 | 9597.01 | -402.99 | sell /  / momentum_26 AND breakout_8: prior completed bar target 0%; next bar open simulation |
| v1 | momentum_26 + breakout_8 | 9514.56 | -485.44 | sell /  / momentum_26 + breakout_8: prior completed bar target 0%; next bar open simulation |
| v1 | momentum_26 AND reversion_12 | 9788.16 | -211.84 | sell /  / momentum_26 AND reversion_12: prior completed bar target 0%; next bar open simulation |
| v1 | momentum_26 + reversion_12 | 9584.02 | -415.98 | sell /  / momentum_26 + reversion_12: prior completed bar target 50%; next bar open simulation |
| v1 | momentum_26 AND volume_26 | 9926.98 | -73.02 | sell /  / momentum_26 AND volume_26: prior completed bar target 0%; next bar open simulation |
| v1 | momentum_26 + volume_26 | 9719.87 | -280.13 | sell /  / momentum_26 + volume_26: prior completed bar target 0%; next bar open simulation |
| v1 | breakout_8 AND reversion_12 | 10000.00 | 0.00 | 대기 /  / 새 신호 대기 |
| v1 | breakout_8 + reversion_12 | 9613.63 | -386.37 | sell /  / breakout_8 + reversion_12: prior completed bar target 50%; next bar open simulation |
| v1 | breakout_8 AND volume_26 | 10054.69 | 54.69 | sell /  / breakout_8 AND volume_26: prior completed bar target 0%; next bar open simulation |
| v1 | breakout_8 + volume_26 | 9769.49 | -230.51 | sell /  / breakout_8 + volume_26: prior completed bar target 0%; next bar open simulation |
| v1 | reversion_12 AND volume_26 | 9940.10 | -59.90 | sell /  / reversion_12 AND volume_26: prior completed bar target 0%; next bar open simulation |
| v1 | reversion_12 + volume_26 | 9782.08 | -217.92 | sell /  / reversion_12 + volume_26: prior completed bar target 50%; next bar open simulation |
| v1 | ema_12_26 | 9641.25 | -358.75 | sell /  / EMA12 > EMA26; 조건 미충족; EMA12=334.549, EMA26=334.619 |
| v1 | macd_12_26_9 | 9723.96 | -276.04 | sell /  / MACD > 신호선 그리고 MACD > 0; 조건 미충족; MACD=-0.0706145, signal9=0.000366165 |
| v1 | rsi_14_recovery | 9986.37 | -13.63 | sell /  / 직전 RSI14 < 30, 현재 RSI14 >= 30 (한 봉 목표); 조건 미충족; RSI14=61.6663, previous_RSI14=57.046 |
| v1 | bollinger_20_reentry | 9868.17 | -131.83 | buy /  / 직전 종가 < 직전 하단밴드, 현재 하단밴드 <= 종가 <= SMA20 (한 봉 목표); 조건 충족; close=333.275, lower20=332.957, SMA20=334.505, previous_lower20=333.105 |
| v1 | donchian_20 | 9792.78 | -207.22 | sell /  / 종가 > 현재 봉을 제외한 직전 20봉 최고가; 조건 미충족; close=335.915, prior_high20=336.169 |
| v1 | atr_14_breakout | 9708.81 | -291.19 | sell /  / 종가 > 직전 종가 + 직전 ATR14 그리고 종가 > EMA26; 조건 미충족; close=335.915, threshold=336.711, prior_ATR14=0.931481, EMA26=334.792 |
| v1 | session_vwap | 9646.60 | -353.40 | sell /  / 종가 > 뉴욕 거래일별 누적 전형가격 VWAP; 조건 미충족; close=334.455, session_VWAP=334.987, session_volume=800398 |
| v1 | obv_20 | 9931.66 | -68.34 | sell /  / OBV > OBV의 SMA20 그리고 종가 > EMA26; 조건 미충족; OBV=-2.0016e+07, OBV_SMA20=-2.02591e+07, close=334.455, EMA26=334.767 |
| v1 | stochastic_14_3_recovery | 9593.69 | -406.31 | buy /  / 직전 %K14 < 20에서 %K14가 %D3 상향 돌파 (한 봉 목표); 조건 충족; K14=24.5463, D3=18.2988, previous_K14=5.92494, previous_D3=25.9572 |
| v1 | mfi_14_recovery | 9935.64 | -64.36 | sell /  / 직전 MFI14 < 20, 현재 MFI14 >= 20 (한 봉 목표); 조건 미충족; MFI14=30.2719, previous_MFI14=26.8492 |
| v1 | adx_14_trend | 9726.68 | -273.32 | sell /  / Wilder ADX14 >= 25 그리고 +DI14 > -DI14; 조건 미충족; ADX14=23.9395, plus_DI14=23.2021, minus_DI14=22.594 |
| v1 | aroon_25_trend | 9824.71 | -175.29 | sell /  / Aroon25 Up > 70 그리고 Down < 30 (동률이면 최신 극값); 조건 미충족; Aroon_up=68, Aroon_down=16 |
| v1 | cci_20_momentum | 9810.74 | -189.26 | sell /  / CCI20 > 100 (전형가격·평균절대편차); 조건 미충족; CCI20=57.5465 |
| v1 | williams_14_recovery | 9586.62 | -413.38 | buy /  / 직전 Williams %R14 < -80, 현재 >= -80 (한 봉 목표); 조건 충족; Williams_R14=-75.4537, previous_R14=-94.0751 |
| v1 | cmf_20_accumulation | 9793.66 | -206.34 | buy /  / Chaikin Money Flow20 > 0.1; 조건 충족; CMF20=0.131084, volume20=2.22061e+06 |
| v1 | chaikin_3_10 | 9762.62 | -237.38 | sell /  / ADL의 EMA3 - EMA10 > 0 그리고 종가 > EMA26; 조건 미충족; Chaikin3_10=246051, ADL=-9.83788e+06, close=334.455, EMA26=334.767 |
| v1 | roc_10_momentum | 9836.40 | -163.60 | sell /  / 10봉 ROC > 1% 그리고 종가 > EMA26; 조건 미충족; ROC10_percent=0.964142, close=337.72, EMA26=336.695 |
| v1 | trix_15_trend | 9723.73 | -276.27 | sell /  / 15봉 삼중 EMA의 1봉 변화율 TRIX > 0 그리고 종가 > EMA26; 조건 미충족; TRIX15_percent=0.0135144, close=337.6, EMA26=338.759 |
| v1 | keltner_20_breakout | 9905.24 | -94.76 | sell /  / 종가 > EMA20 + 2 x Wilder ATR14; 조건 미충족; close=339.04, upper_Keltner=339.281, EMA20=336.559, ATR14=1.36146 |
| v1 | opening_range_30m | 9850.26 | -149.74 | sell /  / 뉴욕 09:30·09:45 두 완료 봉 최고가를 10:00 이후 종가가 돌파; 조건 미충족; close=337.72, opening_high=339.035 |
| v2 | cash | 10000.00 | 0.00 | 대기 /  / 새 신호 대기 |
| v2 | buy_hold | 9984.70 | -15.30 | buy / partial / 직전 완료 봉 목표 비중 100%; 다음 봉 시가 가정 |
| v2 | trend_8_26 | 9713.03 | -286.97 | sell / filled / 직전 완료 봉 목표 비중 0%; 다음 봉 시가 가정 |
| v2 | momentum_26 | 9126.65 | -873.35 | 중단: 손실 한도 / buy / partial / 직전 완료 봉 목표 비중 100%; 다음 봉 시가 가정 |
| v2 | breakout_8 | 8995.65 | -1004.35 | 중단: 손실 한도 / buy / partial / 직전 완료 봉 목표 비중 100%; 다음 봉 시가 가정 |
| v2 | reversion_12 | 9535.29 | -464.71 | buy / partial / 직전 완료 봉 목표 비중 100%; 다음 봉 시가 가정 |
| v2 | volume_26 | 9737.15 | -262.85 | sell / filled / 직전 완료 봉 목표 비중 0%; 다음 봉 시가 가정 |
| v2 | trend_8_26 AND momentum_26 | 9549.07 | -450.93 | sell / filled / 직전 완료 봉 목표 비중 0%; 다음 봉 시가 가정 |
| v2 | trend_8_26 + momentum_26 | 9352.17 | -647.83 | sell / filled / 직전 완료 봉 목표 비중 0%; 다음 봉 시가 가정 |
| v2 | trend_8_26 AND breakout_8 | 9181.63 | -818.37 | sell / filled / 직전 완료 봉 목표 비중 0%; 다음 봉 시가 가정 |
| v2 | trend_8_26 + breakout_8 | 9351.36 | -648.64 | sell / filled / 직전 완료 봉 목표 비중 0%; 다음 봉 시가 가정 |
| v2 | trend_8_26 AND reversion_12 | 9729.48 | -270.52 | sell / filled / 직전 완료 봉 목표 비중 0%; 다음 봉 시가 가정 |
| v2 | trend_8_26 + reversion_12 | 9664.34 | -335.66 | sell / filled / 직전 완료 봉 목표 비중 50%; 다음 봉 시가 가정 |
| v2 | trend_8_26 AND volume_26 | 9897.88 | -102.12 | sell / filled / 직전 완료 봉 목표 비중 0%; 다음 봉 시가 가정 |
| v2 | trend_8_26 + volume_26 | 9725.74 | -274.26 | sell / filled / 직전 완료 봉 목표 비중 0%; 다음 봉 시가 가정 |
| v2 | momentum_26 AND breakout_8 | 8947.82 | -1052.18 | 중단: 손실 한도 / buy / partial / 직전 완료 봉 목표 비중 100%; 다음 봉 시가 가정 |
| v2 | momentum_26 + breakout_8 | 8995.36 | -1004.64 | 중단: 손실 한도 / sell / filled / 직전 완료 봉 목표 비중 0%; 다음 봉 시가 가정 |
| v2 | momentum_26 AND reversion_12 | 9730.22 | -269.78 | sell / filled / 직전 완료 봉 목표 비중 0%; 다음 봉 시가 가정 |
| v2 | momentum_26 + reversion_12 | 9442.76 | -557.24 | sell / filled / 직전 완료 봉 목표 비중 50%; 다음 봉 시가 가정 |
| v2 | momentum_26 AND volume_26 | 9724.84 | -275.16 | sell / filled / 직전 완료 봉 목표 비중 0%; 다음 봉 시가 가정 |
| v2 | momentum_26 + volume_26 | 9443.31 | -556.69 | sell / filled / 직전 완료 봉 목표 비중 0%; 다음 봉 시가 가정 |
| v2 | breakout_8 AND reversion_12 | 10000.00 | 0.00 | 대기 /  / 새 신호 대기 |
| v2 | breakout_8 + reversion_12 | 9303.34 | -696.66 | sell / filled / 직전 완료 봉 목표 비중 50%; 다음 봉 시가 가정 |
| v2 | breakout_8 AND volume_26 | 9941.48 | -58.52 | sell / filled / 직전 완료 봉 목표 비중 0%; 다음 봉 시가 가정 |
| v2 | breakout_8 + volume_26 | 9362.03 | -637.97 | sell / filled / 직전 완료 봉 목표 비중 0%; 다음 봉 시가 가정 |
| v2 | reversion_12 AND volume_26 | 9987.18 | -12.82 | sell / filled / 직전 완료 봉 목표 비중 0%; 다음 봉 시가 가정 |
| v2 | reversion_12 + volume_26 | 9696.70 | -303.30 | sell / filled / 직전 완료 봉 목표 비중 50%; 다음 봉 시가 가정 |
| v2 | ema_12_26 | 9635.47 | -364.53 | sell / filled / EMA12 > EMA26; 조건 미충족; EMA12=334.549, EMA26=334.619; 직전 완료 봉 목표를 다음 봉 시가에 모의 적용 |
| v2 | macd_12_26_9 | 9718.13 | -281.87 | sell / filled / MACD > 신호선 그리고 MACD > 0; 조건 미충족; MACD=-0.0706145, signal9=0.000366165; 직전 완료 봉 목표를 다음 봉 시가에 모의 적용 |
| v2 | rsi_14_recovery | 9984.37 | -15.63 | sell / filled / 직전 RSI14 < 30, 현재 RSI14 >= 30 (한 봉 목표); 조건 미충족; RSI14=61.6663, previous_RSI14=57.046; 직전 완료 봉 목표를 다음 봉 시가에 모의 적용 |
| v2 | bollinger_20_reentry | 9861.26 | -138.74 | buy / partial / 직전 종가 < 직전 하단밴드, 현재 하단밴드 <= 종가 <= SMA20 (한 봉 목표); 조건 충족; close=333.275, lower20=332.957, SMA20=334.505, previous_lower20=333.105; 직전 완료 봉 목표를 다음 봉 시가에 모의 적용 |
| v2 | donchian_20 | 9784.95 | -215.05 | sell / filled / 종가 > 현재 봉을 제외한 직전 20봉 최고가; 조건 미충족; close=335.915, prior_high20=336.169; 직전 완료 봉 목표를 다음 봉 시가에 모의 적용 |
| v2 | atr_14_breakout | 9697.17 | -302.83 | sell / filled / 종가 > 직전 종가 + 직전 ATR14 그리고 종가 > EMA26; 조건 미충족; close=335.915, threshold=336.711, prior_ATR14=0.931481, EMA26=334.792; 직전 완료 봉 목표를 다음 봉 시가에 모의 적용 |
| v2 | session_vwap | 9633.10 | -366.90 | sell / filled / 종가 > 뉴욕 거래일별 누적 전형가격 VWAP; 조건 미충족; close=334.455, session_VWAP=334.987, session_volume=800398; 직전 완료 봉 목표를 다음 봉 시가에 모의 적용 |
| v2 | obv_20 | 9923.71 | -76.29 | sell / filled / OBV > OBV의 SMA20 그리고 종가 > EMA26; 조건 미충족; OBV=-2.0016e+07, OBV_SMA20=-2.02591e+07, close=334.455, EMA26=334.767; 직전 완료 봉 목표를 다음 봉 시가에 모의 적용 |
| v2 | stochastic_14_3_recovery | 9571.65 | -428.35 | buy / partial / 직전 %K14 < 20에서 %K14가 %D3 상향 돌파 (한 봉 목표); 조건 충족; K14=24.5463, D3=18.2988, previous_K14=5.92494, previous_D3=25.9572; 직전 완료 봉 목표를 다음 봉 시가에 모의 적용 |
| v2 | mfi_14_recovery | 9931.66 | -68.34 | sell / filled / 직전 MFI14 < 20, 현재 MFI14 >= 20 (한 봉 목표); 조건 미충족; MFI14=30.2719, previous_MFI14=26.8492; 직전 완료 봉 목표를 다음 봉 시가에 모의 적용 |
| v2 | adx_14_trend | 9722.79 | -277.21 | sell / filled / Wilder ADX14 >= 25 그리고 +DI14 > -DI14; 조건 미충족; ADX14=23.9395, plus_DI14=23.2021, minus_DI14=22.594; 직전 완료 봉 목표를 다음 봉 시가에 모의 적용 |
| v2 | aroon_25_trend | 9822.74 | -177.26 | sell / filled / Aroon25 Up > 70 그리고 Down < 30 (동률이면 최신 극값); 조건 미충족; Aroon_up=68, Aroon_down=16; 직전 완료 봉 목표를 다음 봉 시가에 모의 적용 |
| v2 | cci_20_momentum | 9802.89 | -197.11 | sell / filled / CCI20 > 100 (전형가격·평균절대편차); 조건 미충족; CCI20=57.5465; 직전 완료 봉 목표를 다음 봉 시가에 모의 적용 |
| v2 | williams_14_recovery | 9566.51 | -433.49 | buy / partial / 직전 Williams %R14 < -80, 현재 >= -80 (한 봉 목표); 조건 충족; Williams_R14=-75.4537, previous_R14=-94.0751; 직전 완료 봉 목표를 다음 봉 시가에 모의 적용 |
| v2 | cmf_20_accumulation | 9786.81 | -213.19 | buy / partial / Chaikin Money Flow20 > 0.1; 조건 충족; CMF20=0.131084, volume20=2.22061e+06; 직전 완료 봉 목표를 다음 봉 시가에 모의 적용 |
| v2 | chaikin_3_10 | 9750.91 | -249.09 | sell / filled / ADL의 EMA3 - EMA10 > 0 그리고 종가 > EMA26; 조건 미충족; Chaikin3_10=246051, ADL=-9.83788e+06, close=334.455, EMA26=334.767; 직전 완료 봉 목표를 다음 봉 시가에 모의 적용 |
| v2 | roc_10_momentum | 9832.47 | -167.53 | sell / filled / 10봉 ROC > 1% 그리고 종가 > EMA26; 조건 미충족; ROC10_percent=0.964142, close=337.72, EMA26=336.695; 직전 완료 봉 목표를 다음 봉 시가에 모의 적용 |
| v2 | trix_15_trend | 9715.96 | -284.04 | sell / filled / 15봉 삼중 EMA의 1봉 변화율 TRIX > 0 그리고 종가 > EMA26; 조건 미충족; TRIX15_percent=0.0135144, close=337.6, EMA26=338.759; 직전 완료 봉 목표를 다음 봉 시가에 모의 적용 |
| v2 | keltner_20_breakout | 9901.28 | -98.72 | sell / filled / 종가 > EMA20 + 2 x Wilder ATR14; 조건 미충족; close=339.04, upper_Keltner=339.281, EMA20=336.559, ATR14=1.36146; 직전 완료 봉 목표를 다음 봉 시가에 모의 적용 |
| v2 | opening_range_30m | 9846.33 | -153.67 | sell / filled / 뉴욕 09:30·09:45 두 완료 봉 최고가를 10:00 이후 종가가 돌파; 조건 미충족; close=337.72, opening_high=339.035; 직전 완료 봉 목표를 다음 봉 시가에 모의 적용 |

### 같은 기간의 비용·노출 비교 (사후 연구)

| 전략 | 비용 전 | 비용 후 | 100% 보유 | 같은 평균 노출 보유 | 평균 노출 |
|---|---:|---:|---:|---:|---:|
| cash | 0.00% | 0.00% | 0.24% | 0.00% | 0.00% |
| buy_hold | 0.66% | 0.24% | 0.24% | 0.24% | 100.00% |
| trend_8_26 | 0.02% | -4.09% | 0.24% | 0.13% | 55.67% |
| momentum_26 | -4.04% | -12.51% | 0.24% | 0.13% | 53.30% |
| breakout_8 | -3.22% | -18.53% | 0.24% | 0.05% | 20.32% |
| reversion_12 | 7.20% | -8.23% | 0.24% | 0.06% | 23.75% |
| volume_26 | 1.38% | -5.21% | 0.24% | 0.02% | 6.60% |
| trend_8_26 AND momentum_26 | -0.24% | -6.33% | 0.24% | 0.10% | 42.48% |
| trend_8_26 + momentum_26 | -2.02% | -8.20% | 0.24% | 0.13% | 54.49% |
| trend_8_26 AND breakout_8 | -3.01% | -13.41% | 0.24% | 0.03% | 12.66% |
| trend_8_26 + breakout_8 | -1.59% | -11.03% | 0.24% | 0.09% | 38.00% |
| trend_8_26 AND reversion_12 | 2.60% | -4.47% | 0.24% | 0.02% | 8.18% |
| trend_8_26 + reversion_12 | 3.57% | -5.59% | 0.24% | 0.10% | 39.72% |
| trend_8_26 AND volume_26 | 0.71% | -3.03% | 0.24% | 0.01% | 4.22% |
| trend_8_26 + volume_26 | 0.72% | -4.65% | 0.24% | 0.07% | 31.14% |
| momentum_26 AND breakout_8 | -3.19% | -14.65% | 0.24% | 0.03% | 13.19% |
| momentum_26 + breakout_8 | -3.60% | -15.37% | 0.24% | 0.09% | 36.81% |
| momentum_26 AND reversion_12 | 2.63% | -5.24% | 0.24% | 0.02% | 7.39% |
| momentum_26 + reversion_12 | 1.45% | -8.30% | 0.24% | 0.09% | 38.53% |
| momentum_26 AND volume_26 | -0.48% | -3.77% | 0.24% | 0.01% | 3.17% |
| momentum_26 + volume_26 | -1.34% | -8.35% | 0.24% | 0.07% | 29.95% |
| breakout_8 AND reversion_12 | 0.00% | 0.00% | 0.24% | 0.00% | 0.00% |
| breakout_8 + reversion_12 | 1.88% | -12.25% | 0.24% | 0.05% | 22.04% |
| breakout_8 AND volume_26 | 0.48% | -2.02% | 0.24% | 0.00% | 1.58% |
| breakout_8 + volume_26 | -0.93% | -11.19% | 0.24% | 0.03% | 13.46% |
| reversion_12 AND volume_26 | 2.09% | -0.45% | 0.24% | 0.01% | 2.11% |
| reversion_12 + volume_26 | 4.26% | -5.55% | 0.24% | 0.04% | 15.18% |
| ema_12_26 | -1.03% | -4.70% | 0.24% | 0.13% | 52.77% |
| macd_12_26_9 | -0.92% | -5.79% | 0.24% | 0.08% | 33.51% |
| rsi_14_recovery | 0.40% | -0.86% | 0.24% | 0.00% | 0.79% |
| bollinger_20_reentry | 0.62% | -3.52% | 0.24% | 0.01% | 2.64% |
| donchian_20 | -1.80% | -5.44% | 0.24% | 0.01% | 3.43% |
| atr_14_breakout | -1.24% | -8.82% | 0.24% | 0.01% | 5.28% |
| session_vwap | 0.34% | -9.66% | 0.24% | 0.12% | 48.28% |
| obv_20 | -3.47% | -14.90% | 0.24% | 0.07% | 30.34% |
| stochastic_14_3_recovery | -0.15% | -10.48% | 0.24% | 0.02% | 6.86% |
| mfi_14_recovery | 0.12% | -1.13% | 0.24% | 0.00% | 0.79% |
| adx_14_trend | -2.46% | -4.89% | 0.24% | 0.07% | 27.97% |
| aroon_25_trend | -0.75% | -4.43% | 0.24% | 0.05% | 21.90% |
| cci_20_momentum | -3.44% | -11.96% | 0.24% | 0.04% | 17.15% |
| williams_14_recovery | -0.60% | -10.88% | 0.24% | 0.02% | 6.86% |
| cmf_20_accumulation | -2.14% | -11.15% | 0.24% | 0.08% | 34.04% |
| chaikin_3_10 | 0.96% | -8.72% | 0.24% | 0.08% | 34.30% |
| roc_10_momentum | -1.40% | -3.86% | 0.24% | 0.02% | 6.60% |
| trix_15_trend | -1.25% | -8.83% | 0.24% | 0.08% | 35.36% |
| keltner_20_breakout | -1.21% | -4.07% | 0.24% | 0.01% | 4.22% |
| opening_range_30m | -0.23% | -3.93% | 0.24% | 0.04% | 17.41% |

동일 구간·초기 자금, 종료 시 청산 비용 포함. 노출 맞춤은 사후 설명용이며 v2 실제 계좌 성과가 아닙니다.
[낙폭 분해·비용 영향·전체 구간](JPM/comparison.json)

[v1 전체 기록](JPM/accounts.json) · [v2 전체 기록](JPM/accounts-v2.json)

## XOM 계좌

| 모델 | 전략 | 평가액 USD | 손익 USD | 최근 매매·이유 |
|---|---|---:|---:|---|
| v1 | cash | 10000.00 | 0.00 | 대기 /  / 새 신호 대기 |
| v1 | buy_hold | 9913.30 | -86.70 | buy /  / buy_hold: prior completed bar target 100%; next bar open simulation |
| v1 | trend_8_26 | 9707.62 | -292.38 | sell /  / trend_8_26: prior completed bar target 0%; next bar open simulation |
| v1 | momentum_26 | 9812.01 | -187.99 | sell /  / momentum_26: prior completed bar target 0%; next bar open simulation |
| v1 | breakout_8 | 9491.06 | -508.94 | sell /  / breakout_8: prior completed bar target 0%; next bar open simulation |
| v1 | reversion_12 | 9547.52 | -452.48 | buy /  / reversion_12: prior completed bar target 100%; next bar open simulation |
| v1 | volume_26 | 9510.72 | -489.28 | sell /  / volume_26: prior completed bar target 0%; next bar open simulation |
| v1 | trend_8_26 AND momentum_26 | 9682.17 | -317.83 | sell /  / trend_8_26 AND momentum_26: prior completed bar target 0%; next bar open simulation |
| v1 | trend_8_26 + momentum_26 | 9759.82 | -240.18 | sell /  / trend_8_26 + momentum_26: prior completed bar target 0%; next bar open simulation |
| v1 | trend_8_26 AND breakout_8 | 9628.70 | -371.30 | sell /  / trend_8_26 AND breakout_8: prior completed bar target 0%; next bar open simulation |
| v1 | trend_8_26 + breakout_8 | 9618.49 | -381.51 | sell /  / trend_8_26 + breakout_8: prior completed bar target 0%; next bar open simulation |
| v1 | trend_8_26 AND reversion_12 | 9569.59 | -430.41 | sell /  / trend_8_26 AND reversion_12: prior completed bar target 0%; next bar open simulation |
| v1 | trend_8_26 + reversion_12 | 9627.34 | -372.66 | buy /  / trend_8_26 + reversion_12: prior completed bar target 50%; next bar open simulation |
| v1 | trend_8_26 AND volume_26 | 9624.99 | -375.01 | sell /  / trend_8_26 AND volume_26: prior completed bar target 0%; next bar open simulation |
| v1 | trend_8_26 + volume_26 | 9609.08 | -390.92 | sell /  / trend_8_26 + volume_26: prior completed bar target 0%; next bar open simulation |
| v1 | momentum_26 AND breakout_8 | 9724.23 | -275.77 | sell /  / momentum_26 AND breakout_8: prior completed bar target 0%; next bar open simulation |
| v1 | momentum_26 + breakout_8 | 9650.65 | -349.35 | sell /  / momentum_26 + breakout_8: prior completed bar target 0%; next bar open simulation |
| v1 | momentum_26 AND reversion_12 | 9667.08 | -332.92 | sell /  / momentum_26 AND reversion_12: prior completed bar target 0%; next bar open simulation |
| v1 | momentum_26 + reversion_12 | 9678.84 | -321.16 | buy /  / momentum_26 + reversion_12: prior completed bar target 50%; next bar open simulation |
| v1 | momentum_26 AND volume_26 | 9843.02 | -156.98 | sell /  / momentum_26 AND volume_26: prior completed bar target 0%; next bar open simulation |
| v1 | momentum_26 + volume_26 | 9660.41 | -339.59 | sell /  / momentum_26 + volume_26: prior completed bar target 0%; next bar open simulation |
| v1 | breakout_8 AND reversion_12 | 10000.00 | 0.00 | 대기 /  / 새 신호 대기 |
| v1 | breakout_8 + reversion_12 | 9538.23 | -461.77 | buy /  / breakout_8 + reversion_12: prior completed bar target 50%; next bar open simulation |
| v1 | breakout_8 AND volume_26 | 9851.05 | -148.95 | sell /  / breakout_8 AND volume_26: prior completed bar target 0%; next bar open simulation |
| v1 | breakout_8 + volume_26 | 9500.79 | -499.21 | sell /  / breakout_8 + volume_26: prior completed bar target 0%; next bar open simulation |
| v1 | reversion_12 AND volume_26 | 9794.27 | -205.73 | sell /  / reversion_12 AND volume_26: prior completed bar target 0%; next bar open simulation |
| v1 | reversion_12 + volume_26 | 9529.22 | -470.78 | buy /  / reversion_12 + volume_26: prior completed bar target 50%; next bar open simulation |
| v1 | ema_12_26 | 9780.43 | -219.57 | sell /  / EMA12 > EMA26; 조건 미충족; EMA12=177.479, EMA26=177.559 |
| v1 | macd_12_26_9 | 9819.68 | -180.32 | sell /  / MACD > 신호선 그리고 MACD > 0; 조건 미충족; MACD=0.15005, signal9=0.18271 |
| v1 | rsi_14_recovery | 9927.64 | -72.36 | sell /  / 직전 RSI14 < 30, 현재 RSI14 >= 30 (한 봉 목표); 조건 미충족; RSI14=37.639, previous_RSI14=31.1023 |
| v1 | bollinger_20_reentry | 9719.76 | -280.24 | sell /  / 직전 종가 < 직전 하단밴드, 현재 하단밴드 <= 종가 <= SMA20 (한 봉 목표); 조건 미충족; close=175.148, lower20=175.274, SMA20=177.31, previous_lower20=175.639 |
| v1 | donchian_20 | 9665.93 | -334.07 | sell /  / 종가 > 현재 봉을 제외한 직전 20봉 최고가; 조건 미충족; close=178.045, prior_high20=179.205 |
| v1 | atr_14_breakout | 9803.61 | -196.39 | sell /  / 종가 > 직전 종가 + 직전 ATR14 그리고 종가 > EMA26; 조건 미충족; close=178.95, threshold=179.19, prior_ATR14=0.519565, EMA26=177.678 |
| v1 | session_vwap | 9789.16 | -210.84 | sell /  / 종가 > 뉴욕 거래일별 누적 전형가격 VWAP; 조건 미충족; close=178.38, session_VWAP=178.992, session_volume=640287 |
| v1 | obv_20 | 9265.81 | -734.19 | sell /  / OBV > OBV의 SMA20 그리고 종가 > EMA26; 조건 미충족; OBV=2.21458e+07, OBV_SMA20=2.08793e+07, close=177.148, EMA26=177.751 |
| v1 | stochastic_14_3_recovery | 9655.56 | -344.44 | buy /  / 직전 %K14 < 20에서 %K14가 %D3 상향 돌파 (한 봉 목표); 조건 충족; K14=4.66302, D3=2.02546, previous_K14=0.432993, previous_D3=3.70272 |
| v1 | mfi_14_recovery | 10000.00 | 0.00 | 대기 /  / 새 신호 대기 |
| v1 | adx_14_trend | 9999.47 | -0.53 | sell /  / Wilder ADX14 >= 25 그리고 +DI14 > -DI14; 조건 미충족; ADX14=23.8302, plus_DI14=25.6436, minus_DI14=22.6035 |
| v1 | aroon_25_trend | 9589.85 | -410.15 | sell /  / Aroon25 Up > 70 그리고 Down < 30 (동률이면 최신 극값); 조건 미충족; Aroon_up=96, Aroon_down=40 |
| v1 | cci_20_momentum | 9418.76 | -581.24 | sell /  / CCI20 > 100 (전형가격·평균절대편차); 조건 미충족; CCI20=-36.6043 |
| v1 | williams_14_recovery | 9665.88 | -334.12 | sell /  / 직전 Williams %R14 < -80, 현재 >= -80 (한 봉 목표); 조건 미충족; Williams_R14=-12.0205, previous_R14=-62.6593 |
| v1 | cmf_20_accumulation | 9710.54 | -289.46 | sell /  / Chaikin Money Flow20 > 0.1; 조건 미충족; CMF20=0.0640816, volume20=6.12929e+06 |
| v1 | chaikin_3_10 | 9613.68 | -386.32 | sell /  / ADL의 EMA3 - EMA10 > 0 그리고 종가 > EMA26; 조건 미충족; Chaikin3_10=79809.1, ADL=2.85943e+07, close=177.148, EMA26=177.751 |
| v1 | roc_10_momentum | 9848.63 | -151.37 | sell /  / 10봉 ROC > 1% 그리고 종가 > EMA26; 조건 미충족; ROC10_percent=0.417363, close=178.045, EMA26=177.705 |
| v1 | trix_15_trend | 9744.30 | -255.70 | sell /  / 15봉 삼중 EMA의 1봉 변화율 TRIX > 0 그리고 종가 > EMA26; 조건 미충족; TRIX15_percent=0.0153444, close=177.148, EMA26=177.751 |
| v1 | keltner_20_breakout | 9862.17 | -137.83 | sell /  / 종가 > EMA20 + 2 x Wilder ATR14; 조건 미충족; close=178.045, upper_Keltner=178.914, EMA20=177.784, ATR14=0.564804 |
| v1 | opening_range_30m | 9973.39 | -26.61 | sell /  / 뉴욕 09:30·09:45 두 완료 봉 최고가를 10:00 이후 종가가 돌파; 조건 미충족; close=178.045, opening_high=178.105 |
| v2 | cash | 10000.00 | 0.00 | 대기 /  / 새 신호 대기 |
| v2 | buy_hold | 10229.66 | 229.66 | buy / partial / 직전 완료 봉 목표 비중 100%; 다음 봉 시가 가정 |
| v2 | trend_8_26 | 9793.22 | -206.78 | sell / filled / 직전 완료 봉 목표 비중 0%; 다음 봉 시가 가정 |
| v2 | momentum_26 | 9975.42 | -24.58 | sell / filled / 직전 완료 봉 목표 비중 0%; 다음 봉 시가 가정 |
| v2 | breakout_8 | 8988.95 | -1011.05 | 중단: 손실 한도 / sell / filled / 직전 완료 봉 목표 비중 0%; 다음 봉 시가 가정 |
| v2 | reversion_12 | 9362.52 | -637.48 | buy / partial / 직전 완료 봉 목표 비중 100%; 다음 봉 시가 가정 |
| v2 | volume_26 | 9410.08 | -589.92 | sell / filled / 직전 완료 봉 목표 비중 0%; 다음 봉 시가 가정 |
| v2 | trend_8_26 AND momentum_26 | 9772.84 | -227.16 | sell / filled / 직전 완료 봉 목표 비중 0%; 다음 봉 시가 가정 |
| v2 | trend_8_26 + momentum_26 | 9884.07 | -115.93 | sell / filled / 직전 완료 봉 목표 비중 0%; 다음 봉 시가 가정 |
| v2 | trend_8_26 AND breakout_8 | 9084.52 | -915.48 | sell / filled / 직전 완료 봉 목표 비중 0%; 다음 봉 시가 가정 |
| v2 | trend_8_26 + breakout_8 | 9409.67 | -590.33 | sell / filled / 직전 완료 봉 목표 비중 0%; 다음 봉 시가 가정 |
| v2 | trend_8_26 AND reversion_12 | 9406.78 | -593.22 | sell / filled / 직전 완료 봉 목표 비중 0%; 다음 봉 시가 가정 |
| v2 | trend_8_26 + reversion_12 | 9575.61 | -424.39 | buy / filled / 직전 완료 봉 목표 비중 50%; 다음 봉 시가 가정 |
| v2 | trend_8_26 AND volume_26 | 9514.99 | -485.01 | sell / filled / 직전 완료 봉 목표 비중 0%; 다음 봉 시가 가정 |
| v2 | trend_8_26 + volume_26 | 9600.09 | -399.91 | sell / filled / 직전 완료 봉 목표 비중 0%; 다음 봉 시가 가정 |
| v2 | momentum_26 AND breakout_8 | 9193.28 | -806.72 | sell / filled / 직전 완료 봉 목표 비중 0%; 다음 봉 시가 가정 |
| v2 | momentum_26 + breakout_8 | 9457.07 | -542.93 | sell / filled / 직전 완료 봉 목표 비중 0%; 다음 봉 시가 가정 |
| v2 | momentum_26 AND reversion_12 | 9466.29 | -533.71 | sell / filled / 직전 완료 봉 목표 비중 0%; 다음 봉 시가 가정 |
| v2 | momentum_26 + reversion_12 | 9664.18 | -335.82 | buy / filled / 직전 완료 봉 목표 비중 50%; 다음 봉 시가 가정 |
| v2 | momentum_26 AND volume_26 | 9795.76 | -204.24 | sell / filled / 직전 완료 봉 목표 비중 0%; 다음 봉 시가 가정 |
| v2 | momentum_26 + volume_26 | 9709.12 | -290.88 | sell / filled / 직전 완료 봉 목표 비중 0%; 다음 봉 시가 가정 |
| v2 | breakout_8 AND reversion_12 | 10000.00 | 0.00 | 대기 /  / 새 신호 대기 |
| v2 | breakout_8 + reversion_12 | 9180.08 | -819.92 | buy / filled / 직전 완료 봉 목표 비중 50%; 다음 봉 시가 가정 |
| v2 | breakout_8 AND volume_26 | 9817.82 | -182.18 | sell / filled / 직전 완료 봉 목표 비중 0%; 다음 봉 시가 가정 |
| v2 | breakout_8 + volume_26 | 9203.36 | -796.64 | sell / filled / 직전 완료 봉 목표 비중 0%; 다음 봉 시가 가정 |
| v2 | reversion_12 AND volume_26 | 9737.38 | -262.62 | sell / filled / 직전 완료 봉 목표 비중 0%; 다음 봉 시가 가정 |
| v2 | reversion_12 + volume_26 | 9406.12 | -593.88 | buy / filled / 직전 완료 봉 목표 비중 50%; 다음 봉 시가 가정 |
| v2 | ema_12_26 | 9774.56 | -225.44 | sell / filled / EMA12 > EMA26; 조건 미충족; EMA12=177.479, EMA26=177.559; 직전 완료 봉 목표를 다음 봉 시가에 모의 적용 |
| v2 | macd_12_26_9 | 9809.86 | -190.14 | sell / filled / MACD > 신호선 그리고 MACD > 0; 조건 미충족; MACD=0.15005, signal9=0.18271; 직전 완료 봉 목표를 다음 봉 시가에 모의 적용 |
| v2 | rsi_14_recovery | 9923.67 | -76.33 | sell / filled / 직전 RSI14 < 30, 현재 RSI14 >= 30 (한 봉 목표); 조건 미충족; RSI14=37.639, previous_RSI14=31.1023; 직전 완료 봉 목표를 다음 봉 시가에 모의 적용 |
| v2 | bollinger_20_reentry | 9711.99 | -288.01 | sell / filled / 직전 종가 < 직전 하단밴드, 현재 하단밴드 <= 종가 <= SMA20 (한 봉 목표); 조건 미충족; close=175.148, lower20=175.274, SMA20=177.31, previous_lower20=175.639; 직전 완료 봉 목표를 다음 봉 시가에 모의 적용 |
| v2 | donchian_20 | 9654.34 | -345.66 | sell / filled / 종가 > 현재 봉을 제외한 직전 20봉 최고가; 조건 미충족; close=178.045, prior_high20=179.205; 직전 완료 봉 목표를 다음 봉 시가에 모의 적용 |
| v2 | atr_14_breakout | 9793.82 | -206.18 | sell / filled / 종가 > 직전 종가 + 직전 ATR14 그리고 종가 > EMA26; 조건 미충족; close=178.95, threshold=179.19, prior_ATR14=0.519565, EMA26=177.678; 직전 완료 봉 목표를 다음 봉 시가에 모의 적용 |
| v2 | session_vwap | 9775.46 | -224.54 | sell / filled / 종가 > 뉴욕 거래일별 누적 전형가격 VWAP; 조건 미충족; close=178.38, session_VWAP=178.992, session_volume=640287; 직전 완료 봉 목표를 다음 봉 시가에 모의 적용 |
| v2 | obv_20 | 9502.46 | -497.54 | 중단: 손실 한도 / sell / filled / OBV > OBV의 SMA20 그리고 종가 > EMA26; 조건 미충족; OBV=2.24329e+07, OBV_SMA20=2.30895e+07, close=177.005, EMA26=177.393; 직전 완료 봉 목표를 다음 봉 시가에 모의 적용 |
| v2 | stochastic_14_3_recovery | 9643.02 | -356.98 | buy / partial / 직전 %K14 < 20에서 %K14가 %D3 상향 돌파 (한 봉 목표); 조건 충족; K14=4.66302, D3=2.02546, previous_K14=0.432993, previous_D3=3.70272; 직전 완료 봉 목표를 다음 봉 시가에 모의 적용 |
| v2 | mfi_14_recovery | 10000.00 | 0.00 | 대기 /  / 새 신호 대기 |
| v2 | adx_14_trend | 9993.47 | -6.53 | sell / filled / Wilder ADX14 >= 25 그리고 +DI14 > -DI14; 조건 미충족; ADX14=23.8302, plus_DI14=25.6436, minus_DI14=22.6035; 직전 완료 봉 목표를 다음 봉 시가에 모의 적용 |
| v2 | aroon_25_trend | 9582.18 | -417.82 | sell / filled / Aroon25 Up > 70 그리고 Down < 30 (동률이면 최신 극값); 조건 미충족; Aroon_up=96, Aroon_down=40; 직전 완료 봉 목표를 다음 봉 시가에 모의 적용 |
| v2 | cci_20_momentum | 9398.06 | -601.94 | sell / filled / CCI20 > 100 (전형가격·평균절대편차); 조건 미충족; CCI20=-36.6043; 직전 완료 봉 목표를 다음 봉 시가에 모의 적용 |
| v2 | williams_14_recovery | 9654.28 | -345.72 | sell / filled / 직전 Williams %R14 < -80, 현재 >= -80 (한 봉 목표); 조건 미충족; Williams_R14=-12.0205, previous_R14=-62.6593; 직전 완료 봉 목표를 다음 봉 시가에 모의 적용 |
| v2 | cmf_20_accumulation | 9698.90 | -301.10 | sell / filled / Chaikin Money Flow20 > 0.1; 조건 미충족; CMF20=0.0640816, volume20=6.12929e+06; 직전 완료 봉 목표를 다음 봉 시가에 모의 적용 |
| v2 | chaikin_3_10 | 9598.31 | -401.69 | sell / filled / ADL의 EMA3 - EMA10 > 0 그리고 종가 > EMA26; 조건 미충족; Chaikin3_10=79809.1, ADL=2.85943e+07, close=177.148, EMA26=177.751; 직전 완료 봉 목표를 다음 봉 시가에 모의 적용 |
| v2 | roc_10_momentum | 9840.76 | -159.24 | sell / filled / 10봉 ROC > 1% 그리고 종가 > EMA26; 조건 미충족; ROC10_percent=0.417363, close=178.045, EMA26=177.705; 직전 완료 봉 목표를 다음 봉 시가에 모의 적용 |
| v2 | trix_15_trend | 9732.61 | -267.39 | sell / filled / 15봉 삼중 EMA의 1봉 변화율 TRIX > 0 그리고 종가 > EMA26; 조건 미충족; TRIX15_percent=0.0153444, close=177.148, EMA26=177.751; 직전 완료 봉 목표를 다음 봉 시가에 모의 적용 |
| v2 | keltner_20_breakout | 9854.29 | -145.71 | sell / filled / 종가 > EMA20 + 2 x Wilder ATR14; 조건 미충족; close=178.045, upper_Keltner=178.914, EMA20=177.784, ATR14=0.564804; 직전 완료 봉 목표를 다음 봉 시가에 모의 적용 |
| v2 | opening_range_30m | 9969.40 | -30.60 | sell / filled / 뉴욕 09:30·09:45 두 완료 봉 최고가를 10:00 이후 종가가 돌파; 조건 미충족; close=178.045, opening_high=178.105; 직전 완료 봉 목표를 다음 봉 시가에 모의 적용 |

### 같은 기간의 비용·노출 비교 (사후 연구)

| 전략 | 비용 전 | 비용 후 | 100% 보유 | 같은 평균 노출 보유 | 평균 노출 |
|---|---:|---:|---:|---:|---:|
| cash | 0.00% | 0.00% | 6.48% | 0.00% | 0.00% |
| buy_hold | 6.93% | 6.48% | 6.48% | 6.48% | 100.00% |
| trend_8_26 | 1.17% | -3.40% | 6.48% | 4.54% | 70.98% |
| momentum_26 | 1.36% | -4.43% | 6.48% | 4.59% | 71.77% |
| breakout_8 | -0.97% | -18.71% | 6.48% | 1.66% | 26.39% |
| reversion_12 | 2.36% | -7.46% | 6.48% | 1.35% | 21.64% |
| volume_26 | 0.43% | -7.66% | 6.48% | 0.38% | 6.07% |
| trend_8_26 AND momentum_26 | -0.53% | -5.82% | 6.48% | 3.99% | 62.53% |
| trend_8_26 + momentum_26 | 1.27% | -3.71% | 6.48% | 4.57% | 71.37% |
| trend_8_26 AND breakout_8 | -0.80% | -15.79% | 6.48% | 1.32% | 21.11% |
| trend_8_26 + breakout_8 | 0.12% | -11.00% | 6.48% | 3.08% | 48.69% |
| trend_8_26 AND reversion_12 | -0.82% | -6.87% | 6.48% | 0.64% | 10.29% |
| trend_8_26 + reversion_12 | 1.79% | -5.25% | 6.48% | 2.93% | 46.31% |
| trend_8_26 AND volume_26 | -0.39% | -5.68% | 6.48% | 0.25% | 3.96% |
| trend_8_26 + volume_26 | 0.82% | -5.35% | 6.48% | 2.43% | 38.53% |
| momentum_26 AND breakout_8 | -0.72% | -16.43% | 6.48% | 1.44% | 22.96% |
| momentum_26 + breakout_8 | 0.21% | -11.84% | 6.48% | 3.11% | 49.08% |
| momentum_26 AND reversion_12 | -0.06% | -6.95% | 6.48% | 0.61% | 9.76% |
| momentum_26 + reversion_12 | 1.89% | -4.96% | 6.48% | 2.96% | 46.71% |
| momentum_26 AND volume_26 | 0.84% | -3.31% | 6.48% | 0.16% | 2.64% |
| momentum_26 + volume_26 | 0.92% | -5.06% | 6.48% | 2.46% | 38.92% |
| breakout_8 AND reversion_12 | 0.00% | 0.00% | 6.48% | 0.00% | 0.00% |
| breakout_8 + reversion_12 | 0.70% | -12.91% | 6.48% | 1.51% | 24.02% |
| breakout_8 AND volume_26 | -0.10% | -2.18% | 6.48% | 0.08% | 1.32% |
| breakout_8 + volume_26 | -0.26% | -12.63% | 6.48% | 1.01% | 16.24% |
| reversion_12 AND volume_26 | -0.04% | -3.35% | 6.48% | 0.15% | 2.37% |
| reversion_12 + volume_26 | 1.41% | -6.78% | 6.48% | 0.86% | 13.86% |
| ema_12_26 | 0.06% | -3.24% | 6.48% | 4.89% | 76.25% |
| macd_12_26_9 | -1.28% | -7.31% | 6.48% | 2.80% | 44.33% |
| rsi_14_recovery | -0.08% | -1.33% | 6.48% | 0.05% | 0.79% |
| bollinger_20_reentry | -1.67% | -4.92% | 6.48% | 0.13% | 2.11% |
| donchian_20 | -2.09% | -10.73% | 6.48% | 0.59% | 9.50% |
| atr_14_breakout | 0.61% | -7.11% | 6.48% | 0.33% | 5.28% |
| session_vwap | 0.62% | -9.79% | 6.48% | 4.14% | 64.91% |
| obv_20 | -0.99% | -11.60% | 6.48% | 3.13% | 49.34% |
| stochastic_14_3_recovery | 0.05% | -9.54% | 6.48% | 0.39% | 6.33% |
| mfi_14_recovery | -0.31% | -1.97% | 6.48% | 0.07% | 1.06% |
| adx_14_trend | 3.33% | 0.76% | 6.48% | 2.45% | 38.79% |
| aroon_25_trend | -3.63% | -10.27% | 6.48% | 2.14% | 34.04% |
| cci_20_momentum | 1.06% | -8.63% | 6.48% | 1.79% | 28.50% |
| williams_14_recovery | -1.37% | -7.01% | 6.48% | 0.23% | 3.69% |
| cmf_20_accumulation | 1.42% | -5.17% | 6.48% | 3.38% | 53.30% |
| chaikin_3_10 | 0.79% | -8.10% | 6.48% | 3.86% | 60.69% |
| roc_10_momentum | -0.09% | -5.80% | 6.48% | 0.74% | 11.87% |
| trix_15_trend | -0.18% | -6.67% | 6.48% | 4.04% | 63.32% |
| keltner_20_breakout | 0.18% | -5.94% | 6.48% | 1.02% | 16.36% |
| opening_range_30m | -0.31% | -8.34% | 6.48% | 1.79% | 28.50% |

동일 구간·초기 자금, 종료 시 청산 비용 포함. 노출 맞춤은 사후 설명용이며 v2 실제 계좌 성과가 아닙니다.
[낙폭 분해·비용 영향·전체 구간](XOM/comparison.json)

[v1 전체 기록](XOM/accounts.json) · [v2 전체 기록](XOM/accounts-v2.json)

## JNJ 계좌

| 모델 | 전략 | 평가액 USD | 손익 USD | 최근 매매·이유 |
|---|---|---:|---:|---|
| v1 | cash | 10000.00 | 0.00 | 대기 /  / 새 신호 대기 |
| v1 | buy_hold | 10369.24 | 369.24 | buy /  / buy_hold: prior completed bar target 100%; next bar open simulation |
| v1 | trend_8_26 | 10298.19 | 298.19 | buy /  / trend_8_26: prior completed bar target 100%; next bar open simulation |
| v1 | momentum_26 | 9841.08 | -158.92 | buy /  / momentum_26: prior completed bar target 100%; next bar open simulation |
| v1 | breakout_8 | 9614.55 | -385.45 | buy /  / breakout_8: prior completed bar target 100%; next bar open simulation |
| v1 | reversion_12 | 9747.78 | -252.22 | sell /  / reversion_12: prior completed bar target 0%; next bar open simulation |
| v1 | volume_26 | 10040.58 | 40.58 | sell /  / volume_26: prior completed bar target 0%; next bar open simulation |
| v1 | trend_8_26 AND momentum_26 | 9933.14 | -66.86 | buy /  / trend_8_26 AND momentum_26: prior completed bar target 100%; next bar open simulation |
| v1 | trend_8_26 + momentum_26 | 10067.54 | 67.54 | buy /  / trend_8_26 + momentum_26: prior completed bar target 100%; next bar open simulation |
| v1 | trend_8_26 AND breakout_8 | 10010.52 | 10.52 | buy /  / trend_8_26 AND breakout_8: prior completed bar target 100%; next bar open simulation |
| v1 | trend_8_26 + breakout_8 | 9970.75 | -29.25 | buy /  / trend_8_26 + breakout_8: prior completed bar target 100%; next bar open simulation |
| v1 | trend_8_26 AND reversion_12 | 9930.57 | -69.43 | sell /  / trend_8_26 AND reversion_12: prior completed bar target 0%; next bar open simulation |
| v1 | trend_8_26 + reversion_12 | 10019.45 | 19.45 | sell /  / trend_8_26 + reversion_12: prior completed bar target 50%; next bar open simulation |
| v1 | trend_8_26 AND volume_26 | 10134.54 | 134.54 | sell /  / trend_8_26 AND volume_26: prior completed bar target 0%; next bar open simulation |
| v1 | trend_8_26 + volume_26 | 10168.81 | 168.81 | sell /  / trend_8_26 + volume_26: prior completed bar target 50%; next bar open simulation |
| v1 | momentum_26 AND breakout_8 | 9847.59 | -152.41 | buy /  / momentum_26 AND breakout_8: prior completed bar target 100%; next bar open simulation |
| v1 | momentum_26 + breakout_8 | 9727.24 | -272.76 | buy /  / momentum_26 + breakout_8: prior completed bar target 100%; next bar open simulation |
| v1 | momentum_26 AND reversion_12 | 9938.52 | -61.48 | sell /  / momentum_26 AND reversion_12: prior completed bar target 0%; next bar open simulation |
| v1 | momentum_26 + reversion_12 | 9833.39 | -166.61 | sell /  / momentum_26 + reversion_12: prior completed bar target 50%; next bar open simulation |
| v1 | momentum_26 AND volume_26 | 10000.00 | 0.00 | 대기 /  / 새 신호 대기 |
| v1 | momentum_26 + volume_26 | 10000.35 | 0.35 | sell /  / momentum_26 + volume_26: prior completed bar target 50%; next bar open simulation |
| v1 | breakout_8 AND reversion_12 | 10000.00 | 0.00 | 대기 /  / 새 신호 대기 |
| v1 | breakout_8 + reversion_12 | 9680.78 | -319.22 | sell /  / breakout_8 + reversion_12: prior completed bar target 50%; next bar open simulation |
| v1 | breakout_8 AND volume_26 | 10139.49 | 139.49 | sell /  / breakout_8 AND volume_26: prior completed bar target 0%; next bar open simulation |
| v1 | breakout_8 + volume_26 | 9844.85 | -155.15 | sell /  / breakout_8 + volume_26: prior completed bar target 50%; next bar open simulation |
| v1 | reversion_12 AND volume_26 | 9933.02 | -66.98 | sell /  / reversion_12 AND volume_26: prior completed bar target 0%; next bar open simulation |
| v1 | reversion_12 + volume_26 | 9913.08 | -86.92 | sell /  / reversion_12 + volume_26: prior completed bar target 0%; next bar open simulation |
| v1 | ema_12_26 | 9935.68 | -64.32 | buy /  / EMA12 > EMA26; 조건 충족; EMA12=256.701, EMA26=256.629 |
| v1 | macd_12_26_9 | 10055.02 | 55.02 | buy /  / MACD > 신호선 그리고 MACD > 0; 조건 충족; MACD=0.0724674, signal9=-0.175801 |
| v1 | rsi_14_recovery | 9923.04 | -76.96 | sell /  / 직전 RSI14 < 30, 현재 RSI14 >= 30 (한 봉 목표); 조건 미충족; RSI14=40.3665, previous_RSI14=36.2025 |
| v1 | bollinger_20_reentry | 9816.96 | -183.04 | sell /  / 직전 종가 < 직전 하단밴드, 현재 하단밴드 <= 종가 <= SMA20 (한 봉 목표); 조건 미충족; close=255.05, lower20=254.819, SMA20=258.099, previous_lower20=255.312 |
| v1 | donchian_20 | 9888.21 | -111.79 | buy /  / 종가 > 현재 봉을 제외한 직전 20봉 최고가; 조건 충족; close=265.1, prior_high20=264.16 |
| v1 | atr_14_breakout | 9694.66 | -305.34 | sell /  / 종가 > 직전 종가 + 직전 ATR14 그리고 종가 > EMA26; 조건 미충족; close=265.57, threshold=266.103, prior_ATR14=1.00297, EMA26=259.92 |
| v1 | session_vwap | 10012.90 | 12.90 | buy /  / 종가 > 뉴욕 거래일별 누적 전형가격 VWAP; 조건 충족; close=256.05, session_VWAP=255.552, session_volume=3.26826e+06 |
| v1 | obv_20 | 9796.62 | -203.38 | buy /  / OBV > OBV의 SMA20 그리고 종가 > EMA26; 조건 충족; OBV=8.73204e+06, OBV_SMA20=8.54861e+06, close=257.085, EMA26=256.499 |
| v1 | stochastic_14_3_recovery | 9576.18 | -423.82 | sell /  / 직전 %K14 < 20에서 %K14가 %D3 상향 돌파 (한 봉 목표); 조건 미충족; K14=33.4928, D3=23.2217, previous_K14=28.5165, previous_D3=14.8644 |
| v1 | mfi_14_recovery | 9931.49 | -68.51 | sell /  / 직전 MFI14 < 20, 현재 MFI14 >= 20 (한 봉 목표); 조건 미충족; MFI14=35.8262, previous_MFI14=31.0222 |
| v1 | adx_14_trend | 9749.58 | -250.42 | buy /  / Wilder ADX14 >= 25 그리고 +DI14 > -DI14; 조건 충족; ADX14=27.0686, plus_DI14=50.9231, minus_DI14=9.79199 |
| v1 | aroon_25_trend | 10067.21 | 67.21 | buy /  / Aroon25 Up > 70 그리고 Down < 30 (동률이면 최신 극값); 조건 충족; Aroon_up=100, Aroon_down=24 |
| v1 | cci_20_momentum | 10140.92 | 140.92 | buy /  / CCI20 > 100 (전형가격·평균절대편차); 조건 충족; CCI20=114.549 |
| v1 | williams_14_recovery | 9706.89 | -293.11 | sell /  / 직전 Williams %R14 < -80, 현재 >= -80 (한 봉 목표); 조건 미충족; Williams_R14=-66.5072, previous_R14=-71.4835 |
| v1 | cmf_20_accumulation | 10367.25 | 367.25 | buy /  / Chaikin Money Flow20 > 0.1; 조건 충족; CMF20=0.396629, volume20=6.26242e+06 |
| v1 | chaikin_3_10 | 10092.98 | 92.98 | buy /  / ADL의 EMA3 - EMA10 > 0 그리고 종가 > EMA26; 조건 충족; Chaikin3_10=8814.88, ADL=5.01916e+06, close=256.505, EMA26=256.405 |
| v1 | roc_10_momentum | 9810.37 | -189.63 | buy /  / 10봉 ROC > 1% 그리고 종가 > EMA26; 조건 충족; ROC10_percent=2.2132, close=261.63, EMA26=256.999 |
| v1 | trix_15_trend | 9743.00 | -257.00 | buy /  / 15봉 삼중 EMA의 1봉 변화율 TRIX > 0 그리고 종가 > EMA26; 조건 충족; TRIX15_percent=0.00204174, close=262.76, EMA26=257.426 |
| v1 | keltner_20_breakout | 10037.39 | 37.39 | buy /  / 종가 > EMA20 + 2 x Wilder ATR14; 조건 충족; close=261.63, upper_Keltner=258.85, EMA20=257.085, ATR14=0.882261 |
| v1 | opening_range_30m | 10053.30 | 53.30 | buy /  / 뉴욕 09:30·09:45 두 완료 봉 최고가를 10:00 이후 종가가 돌파; 조건 충족; close=263.54, opening_high=263.19 |
| v2 | cash | 10000.00 | 0.00 | 대기 /  / 새 신호 대기 |
| v2 | buy_hold | 10127.23 | 127.23 | 중단: 손실 한도 / buy / partial / 직전 완료 봉 목표 비중 100%; 다음 봉 시가 가정 |
| v2 | trend_8_26 | 10127.23 | 127.23 | 중단: 손실 한도 / buy / partial / 직전 완료 봉 목표 비중 100%; 다음 봉 시가 가정 |
| v2 | momentum_26 | 10127.23 | 127.23 | 중단: 손실 한도 / buy / partial / 직전 완료 봉 목표 비중 100%; 다음 봉 시가 가정 |
| v2 | breakout_8 | 9343.39 | -656.61 | 중단: 손실 한도 / sell / filled / 직전 완료 봉 목표 비중 0%; 다음 봉 시가 가정 |
| v2 | reversion_12 | 9434.41 | -565.59 | sell / filled / 직전 완료 봉 목표 비중 0%; 다음 봉 시가 가정 |
| v2 | volume_26 | 9819.31 | -180.69 | sell / filled / 직전 완료 봉 목표 비중 0%; 다음 봉 시가 가정 |
| v2 | trend_8_26 AND momentum_26 | 10127.23 | 127.23 | 중단: 손실 한도 / buy / partial / 직전 완료 봉 목표 비중 100%; 다음 봉 시가 가정 |
| v2 | trend_8_26 + momentum_26 | 10127.23 | 127.23 | 중단: 손실 한도 / buy / partial / 직전 완료 봉 목표 비중 100%; 다음 봉 시가 가정 |
| v2 | trend_8_26 AND breakout_8 | 9419.39 | -580.61 | 중단: 손실 한도 / sell / filled / 직전 완료 봉 목표 비중 0%; 다음 봉 시가 가정 |
| v2 | trend_8_26 + breakout_8 | 9527.50 | -472.50 | buy / partial / 직전 완료 봉 목표 비중 100%; 다음 봉 시가 가정 |
| v2 | trend_8_26 AND reversion_12 | 9900.89 | -99.11 | sell / filled / 직전 완료 봉 목표 비중 0%; 다음 봉 시가 가정 |
| v2 | trend_8_26 + reversion_12 | 9732.92 | -267.08 | 중단: 손실 한도 / sell / filled / 직전 완료 봉 목표 비중 0%; 다음 봉 시가 가정 |
| v2 | trend_8_26 AND volume_26 | 9997.51 | -2.49 | sell / filled / 직전 완료 봉 목표 비중 0%; 다음 봉 시가 가정 |
| v2 | trend_8_26 + volume_26 | 10041.40 | 41.40 | 중단: 손실 한도 / buy / filled / 직전 완료 봉 목표 비중 50%; 다음 봉 시가 가정 |
| v2 | momentum_26 AND breakout_8 | 9443.90 | -556.10 | buy / partial / 직전 완료 봉 목표 비중 100%; 다음 봉 시가 가정 |
| v2 | momentum_26 + breakout_8 | 9285.15 | -714.85 | buy / partial / 직전 완료 봉 목표 비중 100%; 다음 봉 시가 가정 |
| v2 | momentum_26 AND reversion_12 | 9871.83 | -128.17 | sell / filled / 직전 완료 봉 목표 비중 0%; 다음 봉 시가 가정 |
| v2 | momentum_26 + reversion_12 | 9732.92 | -267.08 | 중단: 손실 한도 / sell / filled / 직전 완료 봉 목표 비중 0%; 다음 봉 시가 가정 |
| v2 | momentum_26 AND volume_26 | 9920.93 | -79.07 | sell / filled / 직전 완료 봉 목표 비중 0%; 다음 봉 시가 가정 |
| v2 | momentum_26 + volume_26 | 10041.40 | 41.40 | 중단: 손실 한도 / buy / filled / 직전 완료 봉 목표 비중 50%; 다음 봉 시가 가정 |
| v2 | breakout_8 AND reversion_12 | 10000.00 | 0.00 | 대기 /  / 새 신호 대기 |
| v2 | breakout_8 + reversion_12 | 9257.11 | -742.89 | sell / filled / 직전 완료 봉 목표 비중 50%; 다음 봉 시가 가정 |
| v2 | breakout_8 AND volume_26 | 9949.08 | -50.92 | sell / filled / 직전 완료 봉 목표 비중 0%; 다음 봉 시가 가정 |
| v2 | breakout_8 + volume_26 | 9444.06 | -555.94 | sell / filled / 직전 완료 봉 목표 비중 50%; 다음 봉 시가 가정 |
| v2 | reversion_12 AND volume_26 | 9816.09 | -183.91 | sell / filled / 직전 완료 봉 목표 비중 0%; 다음 봉 시가 가정 |
| v2 | reversion_12 + volume_26 | 9665.84 | -334.16 | sell / filled / 직전 완료 봉 목표 비중 0%; 다음 봉 시가 가정 |
| v2 | ema_12_26 | 9928.73 | -71.27 | buy / partial / EMA12 > EMA26; 조건 충족; EMA12=256.701, EMA26=256.629; 직전 완료 봉 목표를 다음 봉 시가에 모의 적용 |
| v2 | macd_12_26_9 | 10047.98 | 47.98 | buy / partial / MACD > 신호선 그리고 MACD > 0; 조건 충족; MACD=0.0724674, signal9=-0.175801; 직전 완료 봉 목표를 다음 봉 시가에 모의 적용 |
| v2 | rsi_14_recovery | 9919.07 | -80.93 | sell / filled / 직전 RSI14 < 30, 현재 RSI14 >= 30 (한 봉 목표); 조건 미충족; RSI14=40.3665, previous_RSI14=36.2025; 직전 완료 봉 목표를 다음 봉 시가에 모의 적용 |
| v2 | bollinger_20_reentry | 9811.07 | -188.93 | sell / filled / 직전 종가 < 직전 하단밴드, 현재 하단밴드 <= 종가 <= SMA20 (한 봉 목표); 조건 미충족; close=255.05, lower20=254.819, SMA20=258.099, previous_lower20=255.312; 직전 완료 봉 목표를 다음 봉 시가에 모의 적용 |
| v2 | donchian_20 | 9879.31 | -120.69 | buy / partial / 종가 > 현재 봉을 제외한 직전 20봉 최고가; 조건 충족; close=265.1, prior_high20=264.16; 직전 완료 봉 목표를 다음 봉 시가에 모의 적용 |
| v2 | atr_14_breakout | 9683.04 | -316.96 | sell / filled / 종가 > 직전 종가 + 직전 ATR14 그리고 종가 > EMA26; 조건 미충족; close=265.57, threshold=266.103, prior_ATR14=1.00297, EMA26=259.92; 직전 완료 봉 목표를 다음 봉 시가에 모의 적용 |
| v2 | session_vwap | 9993.90 | -6.10 | buy / partial / 종가 > 뉴욕 거래일별 누적 전형가격 VWAP; 조건 충족; close=256.05, session_VWAP=255.552, session_volume=3.26826e+06; 직전 완료 봉 목표를 다음 봉 시가에 모의 적용 |
| v2 | obv_20 | 9778.02 | -221.98 | buy / partial / OBV > OBV의 SMA20 그리고 종가 > EMA26; 조건 충족; OBV=8.59102e+06, OBV_SMA20=8.40759e+06, close=257.085, EMA26=256.499; 직전 완료 봉 목표를 다음 봉 시가에 모의 적용 |
| v2 | stochastic_14_3_recovery | 9560.87 | -439.13 | sell / filled / 직전 %K14 < 20에서 %K14가 %D3 상향 돌파 (한 봉 목표); 조건 미충족; K14=33.4928, D3=23.2217, previous_K14=28.5165, previous_D3=14.8644; 직전 완료 봉 목표를 다음 봉 시가에 모의 적용 |
| v2 | mfi_14_recovery | 9925.53 | -74.47 | sell / filled / 직전 MFI14 < 20, 현재 MFI14 >= 20 (한 봉 목표); 조건 미충족; MFI14=35.8262, previous_MFI14=31.0222; 직전 완료 봉 목표를 다음 봉 시가에 모의 적용 |
| v2 | adx_14_trend | 9740.81 | -259.19 | buy / partial / Wilder ADX14 >= 25 그리고 +DI14 > -DI14; 조건 충족; ADX14=27.0686, plus_DI14=50.9231, minus_DI14=9.79199; 직전 완료 봉 목표를 다음 봉 시가에 모의 적용 |
| v2 | aroon_25_trend | 10062.17 | 62.17 | buy / partial / Aroon25 Up > 70 그리고 Down < 30 (동률이면 최신 극값); 조건 충족; Aroon_up=100, Aroon_down=24; 직전 완료 봉 목표를 다음 봉 시가에 모의 적용 |
| v2 | cci_20_momentum | 10133.82 | 133.82 | buy / partial / CCI20 > 100 (전형가격·평균절대편차); 조건 충족; CCI20=114.549; 직전 완료 봉 목표를 다음 봉 시가에 모의 적용 |
| v2 | williams_14_recovery | 9697.19 | -302.81 | sell / filled / 직전 Williams %R14 < -80, 현재 >= -80 (한 봉 목표); 조건 미충족; Williams_R14=-66.5072, previous_R14=-71.4835; 직전 완료 봉 목표를 다음 봉 시가에 모의 적용 |
| v2 | cmf_20_accumulation | 10362.07 | 362.07 | buy / partial / Chaikin Money Flow20 > 0.1; 조건 충족; CMF20=0.396629, volume20=6.26242e+06; 직전 완료 봉 목표를 다음 봉 시가에 모의 적용 |
| v2 | chaikin_3_10 | 10083.90 | 83.90 | buy / partial / ADL의 EMA3 - EMA10 > 0 그리고 종가 > EMA26; 조건 충족; Chaikin3_10=8814.88, ADL=4.70768e+06, close=256.505, EMA26=256.405; 직전 완료 봉 목표를 다음 봉 시가에 모의 적용 |
| v2 | roc_10_momentum | 9801.54 | -198.46 | buy / partial / 10봉 ROC > 1% 그리고 종가 > EMA26; 조건 충족; ROC10_percent=2.2132, close=261.63, EMA26=256.999; 직전 완료 봉 목표를 다음 봉 시가에 모의 적용 |
| v2 | trix_15_trend | 9736.18 | -263.82 | buy / partial / 15봉 삼중 EMA의 1봉 변화율 TRIX > 0 그리고 종가 > EMA26; 조건 충족; TRIX15_percent=0.00204174, close=262.76, EMA26=257.426; 직전 완료 봉 목표를 다음 봉 시가에 모의 적용 |
| v2 | keltner_20_breakout | 10034.38 | 34.38 | buy / partial / 종가 > EMA20 + 2 x Wilder ATR14; 조건 충족; close=261.63, upper_Keltner=258.85, EMA20=257.085, ATR14=0.882261; 직전 완료 봉 목표를 다음 봉 시가에 모의 적용 |
| v2 | opening_range_30m | 10052.30 | 52.30 | buy / partial / 뉴욕 09:30·09:45 두 완료 봉 최고가를 10:00 이후 종가가 돌파; 조건 충족; close=263.54, opening_high=263.19; 직전 완료 봉 목표를 다음 봉 시가에 모의 적용 |

### 같은 기간의 비용·노출 비교 (사후 연구)

| 전략 | 비용 전 | 비용 후 | 100% 보유 | 같은 평균 노출 보유 | 평균 노출 |
|---|---:|---:|---:|---:|---:|
| cash | 0.00% | 0.00% | 1.98% | 0.00% | 0.00% |
| buy_hold | 2.41% | 1.98% | 1.98% | 1.98% | 100.00% |
| trend_8_26 | 5.99% | 3.35% | 1.98% | 1.02% | 51.19% |
| momentum_26 | 0.55% | -2.77% | 1.98% | 0.97% | 48.55% |
| breakout_8 | 2.03% | -16.60% | 1.98% | 0.47% | 23.75% |
| reversion_12 | -4.65% | -12.34% | 1.98% | 0.52% | 26.12% |
| volume_26 | 1.99% | -4.64% | 1.98% | 0.12% | 6.07% |
| trend_8_26 AND momentum_26 | 2.23% | -0.73% | 1.98% | 0.86% | 43.01% |
| trend_8_26 + momentum_26 | 3.25% | 0.25% | 1.98% | 0.99% | 49.87% |
| trend_8_26 AND breakout_8 | 3.27% | -9.72% | 1.98% | 0.33% | 16.62% |
| trend_8_26 + breakout_8 | 4.02% | -6.94% | 1.98% | 0.75% | 37.47% |
| trend_8_26 AND reversion_12 | 1.37% | -1.98% | 1.98% | 0.12% | 5.80% |
| trend_8_26 + reversion_12 | 0.57% | -4.60% | 1.98% | 0.77% | 38.66% |
| trend_8_26 AND volume_26 | 3.25% | 0.26% | 1.98% | 0.04% | 2.11% |
| trend_8_26 + volume_26 | 4.01% | -0.50% | 1.98% | 0.57% | 28.63% |
| momentum_26 AND breakout_8 | 2.27% | -9.46% | 1.98% | 0.30% | 14.78% |
| momentum_26 + breakout_8 | 1.32% | -9.74% | 1.98% | 0.72% | 36.15% |
| momentum_26 AND reversion_12 | -0.27% | -3.16% | 1.98% | 0.13% | 6.33% |
| momentum_26 + reversion_12 | -2.06% | -7.09% | 1.98% | 0.74% | 37.34% |
| momentum_26 AND volume_26 | 0.14% | -0.70% | 1.98% | 0.01% | 0.53% |
| momentum_26 + volume_26 | 1.30% | -2.47% | 1.98% | 0.55% | 27.31% |
| breakout_8 AND reversion_12 | 0.00% | 0.00% | 1.98% | 0.00% | 0.00% |
| breakout_8 + reversion_12 | -1.35% | -14.14% | 1.98% | 0.50% | 24.94% |
| breakout_8 AND volume_26 | 1.33% | 0.06% | 1.98% | 0.02% | 1.06% |
| breakout_8 + volume_26 | 2.02% | -9.88% | 1.98% | 0.30% | 14.92% |
| reversion_12 AND volume_26 | -1.19% | -3.65% | 1.98% | 0.04% | 2.11% |
| reversion_12 + volume_26 | -1.37% | -7.99% | 1.98% | 0.32% | 16.10% |
| ema_12_26 | 0.83% | -2.10% | 1.98% | 0.98% | 49.34% |
| macd_12_26_9 | 7.83% | 4.27% | 1.98% | 0.64% | 31.93% |
| rsi_14_recovery | -1.35% | -6.20% | 1.98% | 0.06% | 3.17% |
| bollinger_20_reentry | -1.28% | -5.34% | 1.98% | 0.05% | 2.64% |
| donchian_20 | 1.76% | -6.83% | 1.98% | 0.17% | 8.44% |
| atr_14_breakout | 0.97% | -5.99% | 1.98% | 0.11% | 5.54% |
| session_vwap | 7.06% | -1.57% | 1.98% | 1.08% | 54.09% |
| obv_20 | -2.70% | -12.77% | 1.98% | 0.77% | 38.52% |
| stochastic_14_3_recovery | -0.70% | -11.72% | 1.98% | 0.15% | 7.39% |
| mfi_14_recovery | 0.84% | -1.67% | 1.98% | 0.03% | 1.58% |
| adx_14_trend | -2.74% | -7.90% | 1.98% | 0.77% | 38.52% |
| aroon_25_trend | 5.24% | 0.91% | 1.98% | 0.65% | 32.45% |
| cci_20_momentum | 4.09% | -2.27% | 1.98% | 0.47% | 23.48% |
| williams_14_recovery | -2.20% | -9.32% | 1.98% | 0.10% | 4.75% |
| cmf_20_accumulation | 7.39% | 2.54% | 1.98% | 0.75% | 37.47% |
| chaikin_3_10 | -0.07% | -5.38% | 1.98% | 0.83% | 41.42% |
| roc_10_momentum | -1.40% | -8.58% | 1.98% | 0.40% | 19.79% |
| trix_15_trend | -0.62% | -3.50% | 1.98% | 0.75% | 37.73% |
| keltner_20_breakout | 1.63% | -2.55% | 1.98% | 0.28% | 13.98% |
| opening_range_30m | 1.53% | -2.65% | 1.98% | 0.55% | 27.44% |

동일 구간·초기 자금, 종료 시 청산 비용 포함. 노출 맞춤은 사후 설명용이며 v2 실제 계좌 성과가 아닙니다.
[낙폭 분해·비용 영향·전체 구간](JNJ/comparison.json)

[v1 전체 기록](JNJ/accounts.json) · [v2 전체 기록](JNJ/accounts-v2.json)

## CAT 계좌

| 모델 | 전략 | 평가액 USD | 손익 USD | 최근 매매·이유 |
|---|---|---:|---:|---|
| v1 | cash | 10000.00 | 0.00 | 대기 /  / 새 신호 대기 |
| v1 | buy_hold | 9482.63 | -517.37 | buy /  / buy_hold: prior completed bar target 100%; next bar open simulation |
| v1 | trend_8_26 | 9570.52 | -429.48 | sell /  / trend_8_26: prior completed bar target 0%; next bar open simulation |
| v1 | momentum_26 | 9290.58 | -709.42 | sell /  / momentum_26: prior completed bar target 0%; next bar open simulation |
| v1 | breakout_8 | 9544.96 | -455.04 | sell /  / breakout_8: prior completed bar target 0%; next bar open simulation |
| v1 | reversion_12 | 9707.18 | -292.82 | buy /  / reversion_12: prior completed bar target 100%; next bar open simulation |
| v1 | volume_26 | 9683.18 | -316.82 | sell /  / volume_26: prior completed bar target 0%; next bar open simulation |
| v1 | trend_8_26 AND momentum_26 | 9471.21 | -528.79 | sell /  / trend_8_26 AND momentum_26: prior completed bar target 0%; next bar open simulation |
| v1 | trend_8_26 + momentum_26 | 9430.55 | -569.45 | sell /  / trend_8_26 + momentum_26: prior completed bar target 0%; next bar open simulation |
| v1 | trend_8_26 AND breakout_8 | 9747.92 | -252.08 | sell /  / trend_8_26 AND breakout_8: prior completed bar target 0%; next bar open simulation |
| v1 | trend_8_26 + breakout_8 | 9559.68 | -440.32 | sell /  / trend_8_26 + breakout_8: prior completed bar target 0%; next bar open simulation |
| v1 | trend_8_26 AND reversion_12 | 9919.62 | -80.38 | sell /  / trend_8_26 AND reversion_12: prior completed bar target 0%; next bar open simulation |
| v1 | trend_8_26 + reversion_12 | 9699.04 | -300.96 | buy /  / trend_8_26 + reversion_12: prior completed bar target 50%; next bar open simulation |
| v1 | trend_8_26 AND volume_26 | 9965.69 | -34.31 | sell /  / trend_8_26 AND volume_26: prior completed bar target 0%; next bar open simulation |
| v1 | trend_8_26 + volume_26 | 9667.13 | -332.87 | sell /  / trend_8_26 + volume_26: prior completed bar target 0%; next bar open simulation |
| v1 | momentum_26 AND breakout_8 | 9615.85 | -384.15 | sell /  / momentum_26 AND breakout_8: prior completed bar target 0%; next bar open simulation |
| v1 | momentum_26 + breakout_8 | 9417.88 | -582.12 | sell /  / momentum_26 + breakout_8: prior completed bar target 0%; next bar open simulation |
| v1 | momentum_26 AND reversion_12 | 9878.81 | -121.19 | sell /  / momentum_26 AND reversion_12: prior completed bar target 0%; next bar open simulation |
| v1 | momentum_26 + reversion_12 | 9517.11 | -482.89 | buy /  / momentum_26 + reversion_12: prior completed bar target 50%; next bar open simulation |
| v1 | momentum_26 AND volume_26 | 9894.55 | -105.45 | sell /  / momentum_26 AND volume_26: prior completed bar target 0%; next bar open simulation |
| v1 | momentum_26 + volume_26 | 9504.77 | -495.23 | sell /  / momentum_26 + volume_26: prior completed bar target 0%; next bar open simulation |
| v1 | breakout_8 AND reversion_12 | 10000.00 | 0.00 | 대기 /  / 새 신호 대기 |
| v1 | breakout_8 + reversion_12 | 9626.38 | -373.62 | buy /  / breakout_8 + reversion_12: prior completed bar target 50%; next bar open simulation |
| v1 | breakout_8 AND volume_26 | 9894.55 | -105.45 | sell /  / breakout_8 AND volume_26: prior completed bar target 0%; next bar open simulation |
| v1 | breakout_8 + volume_26 | 9614.01 | -385.99 | sell /  / breakout_8 + volume_26: prior completed bar target 0%; next bar open simulation |
| v1 | reversion_12 AND volume_26 | 9810.19 | -189.81 | sell /  / reversion_12 AND volume_26: prior completed bar target 0%; next bar open simulation |
| v1 | reversion_12 + volume_26 | 9695.61 | -304.39 | sell /  / reversion_12 + volume_26: prior completed bar target 50%; next bar open simulation |
| v1 | ema_12_26 | 9597.59 | -402.41 | sell /  / EMA12 > EMA26; 조건 미충족; EMA12=734.57, EMA26=734.673 |
| v1 | macd_12_26_9 | 9988.51 | -11.49 | sell /  / MACD > 신호선 그리고 MACD > 0; 조건 미충족; MACD=2.92675, signal9=3.02629 |
| v1 | rsi_14_recovery | 9999.22 | -0.78 | sell /  / 직전 RSI14 < 30, 현재 RSI14 >= 30 (한 봉 목표); 조건 미충족; RSI14=43.621, previous_RSI14=38.5787 |
| v1 | bollinger_20_reentry | 9693.48 | -306.52 | sell /  / 직전 종가 < 직전 하단밴드, 현재 하단밴드 <= 종가 <= SMA20 (한 봉 목표); 조건 미충족; close=698.04, lower20=693.892, SMA20=727.609, previous_lower20=698.501 |
| v1 | donchian_20 | 9943.28 | -56.72 | sell /  / 종가 > 현재 봉을 제외한 직전 20봉 최고가; 조건 미충족; close=735.35, prior_high20=745 |
| v1 | atr_14_breakout | 9768.31 | -231.69 | sell /  / 종가 > 직전 종가 + 직전 ATR14 그리고 종가 > EMA26; 조건 미충족; close=735.35, threshold=737.263, prior_ATR14=4.10289, EMA26=727.331 |
| v1 | session_vwap | 9256.88 | -743.12 | sell /  / 종가 > 뉴욕 거래일별 누적 전형가격 VWAP; 조건 미충족; close=711.18, session_VWAP=714.637, session_volume=326559 |
| v1 | obv_20 | 9541.23 | -458.77 | sell /  / OBV > OBV의 SMA20 그리고 종가 > EMA26; 조건 미충족; OBV=-4.81948e+06, OBV_SMA20=-4.73979e+06, close=711.18, EMA26=734.673 |
| v1 | stochastic_14_3_recovery | 9770.81 | -229.19 | sell /  / 직전 %K14 < 20에서 %K14가 %D3 상향 돌파 (한 봉 목표); 조건 미충족; K14=0.622844, D3=3.92968, previous_K14=8.58265, previous_D3=4.55061 |
| v1 | mfi_14_recovery | 10068.63 | 68.63 | sell /  / 직전 MFI14 < 20, 현재 MFI14 >= 20 (한 봉 목표); 조건 미충족; MFI14=32.7313, previous_MFI14=24.1736 |
| v1 | adx_14_trend | 9614.13 | -385.87 | sell /  / Wilder ADX14 >= 25 그리고 +DI14 > -DI14; 조건 미충족; ADX14=37.6898, plus_DI14=16.8278, minus_DI14=52.0976 |
| v1 | aroon_25_trend | 9979.61 | -20.39 | sell /  / Aroon25 Up > 70 그리고 Down < 30 (동률이면 최신 극값); 조건 미충족; Aroon_up=68, Aroon_down=20 |
| v1 | cci_20_momentum | 9862.85 | -137.15 | sell /  / CCI20 > 100 (전형가격·평균절대편차); 조건 미충족; CCI20=99.2123 |
| v1 | williams_14_recovery | 10007.06 | 7.06 | sell /  / 직전 Williams %R14 < -80, 현재 >= -80 (한 봉 목표); 조건 미충족; Williams_R14=-40.3504, previous_R14=-56.1644 |
| v1 | cmf_20_accumulation | 9458.11 | -541.89 | sell /  / Chaikin Money Flow20 > 0.1; 조건 미충족; CMF20=0.0105743, volume20=1.36134e+06 |
| v1 | chaikin_3_10 | 9240.53 | -759.47 | sell /  / ADL의 EMA3 - EMA10 > 0 그리고 종가 > EMA26; 조건 미충족; Chaikin3_10=-27551.7, ADL=-5.11151e+06, close=711.18, EMA26=734.673 |
| v1 | roc_10_momentum | 9896.73 | -103.27 | sell /  / 10봉 ROC > 1% 그리고 종가 > EMA26; 조건 미충족; ROC10_percent=0.883016, close=741.47, EMA26=734.681 |
| v1 | trix_15_trend | 9340.52 | -659.48 | sell /  / 15봉 삼중 EMA의 1봉 변화율 TRIX > 0 그리고 종가 > EMA26; 조건 미충족; TRIX15_percent=0.0460682, close=711.18, EMA26=734.673 |
| v1 | keltner_20_breakout | 10000.00 | 0.00 | 대기 /  / 새 신호 대기 |
| v1 | opening_range_30m | 10162.22 | 162.22 | sell /  / 뉴욕 09:30·09:45 두 완료 봉 최고가를 10:00 이후 종가가 돌파; 자료 부족·변동폭 또는 거래량 없음: 대기; close=733.16 |
| v2 | cash | 10000.00 | 0.00 | 대기 /  / 새 신호 대기 |
| v2 | buy_hold | 8720.94 | -1279.06 | 중단: 손실 한도 / buy / partial / 직전 완료 봉 목표 비중 100%; 다음 봉 시가 가정 |
| v2 | trend_8_26 | 9331.63 | -668.37 | 중단: 손실 한도 / buy / partial / 직전 완료 봉 목표 비중 100%; 다음 봉 시가 가정 |
| v2 | momentum_26 | 9135.22 | -864.78 | 중단: 손실 한도 / buy / partial / 직전 완료 봉 목표 비중 100%; 다음 봉 시가 가정 |
| v2 | breakout_8 | 9357.29 | -642.71 | sell / filled / 직전 완료 봉 목표 비중 0%; 다음 봉 시가 가정 |
| v2 | reversion_12 | 8599.15 | -1400.85 | 중단: 손실 한도 / buy / partial / 직전 완료 봉 목표 비중 100%; 다음 봉 시가 가정 |
| v2 | volume_26 | 8845.07 | -1154.93 | 중단: 손실 한도 / buy / partial / 직전 완료 봉 목표 비중 100%; 다음 봉 시가 가정 |
| v2 | trend_8_26 AND momentum_26 | 9345.40 | -654.60 | 중단: 손실 한도 / buy / partial / 직전 완료 봉 목표 비중 100%; 다음 봉 시가 가정 |
| v2 | trend_8_26 + momentum_26 | 9233.91 | -766.09 | 중단: 손실 한도 / buy / partial / 직전 완료 봉 목표 비중 100%; 다음 봉 시가 가정 |
| v2 | trend_8_26 AND breakout_8 | 9655.84 | -344.16 | sell / filled / 직전 완료 봉 목표 비중 0%; 다음 봉 시가 가정 |
| v2 | trend_8_26 + breakout_8 | 9426.02 | -573.98 | sell / filled / 직전 완료 봉 목표 비중 0%; 다음 봉 시가 가정 |
| v2 | trend_8_26 AND reversion_12 | 9728.39 | -271.61 | sell / filled / 직전 완료 봉 목표 비중 0%; 다음 봉 시가 가정 |
| v2 | trend_8_26 + reversion_12 | 9324.73 | -675.27 | buy / filled / 직전 완료 봉 목표 비중 50%; 다음 봉 시가 가정 |
| v2 | trend_8_26 AND volume_26 | 9999.01 | -0.99 | sell / filled / 직전 완료 봉 목표 비중 0%; 다음 봉 시가 가정 |
| v2 | trend_8_26 + volume_26 | 9303.04 | -696.96 | 중단: 손실 한도 / sell / filled / 직전 완료 봉 목표 비중 0%; 다음 봉 시가 가정 |
| v2 | momentum_26 AND breakout_8 | 9576.90 | -423.10 | sell / filled / 직전 완료 봉 목표 비중 0%; 다음 봉 시가 가정 |
| v2 | momentum_26 + breakout_8 | 9325.28 | -674.72 | sell / filled / 직전 완료 봉 목표 비중 0%; 다음 봉 시가 가정 |
| v2 | momentum_26 AND reversion_12 | 9745.30 | -254.70 | sell / filled / 직전 완료 봉 목표 비중 0%; 다음 봉 시가 가정 |
| v2 | momentum_26 + reversion_12 | 9186.55 | -813.45 | buy / filled / 직전 완료 봉 목표 비중 50%; 다음 봉 시가 가정 |
| v2 | momentum_26 AND volume_26 | 9936.85 | -63.15 | sell / filled / 직전 완료 봉 목표 비중 0%; 다음 봉 시가 가정 |
| v2 | momentum_26 + volume_26 | 9203.76 | -796.24 | 중단: 손실 한도 / sell / filled / 직전 완료 봉 목표 비중 0%; 다음 봉 시가 가정 |
| v2 | breakout_8 AND reversion_12 | 10000.00 | 0.00 | 대기 /  / 새 신호 대기 |
| v2 | breakout_8 + reversion_12 | 9610.18 | -389.82 | 중단: 손실 한도 / sell / filled / 직전 완료 봉 목표 비중 0%; 다음 봉 시가 가정 |
| v2 | breakout_8 AND volume_26 | 9887.31 | -112.69 | sell / filled / 직전 완료 봉 목표 비중 0%; 다음 봉 시가 가정 |
| v2 | breakout_8 + volume_26 | 9216.53 | -783.47 | sell / filled / 직전 완료 봉 목표 비중 0%; 다음 봉 시가 가정 |
| v2 | reversion_12 AND volume_26 | 8783.89 | -1216.11 | 중단: 손실 한도 / buy / partial / 직전 완료 봉 목표 비중 100%; 다음 봉 시가 가정 |
| v2 | reversion_12 + volume_26 | 9159.80 | -840.20 | 중단: 손실 한도 / sell / filled / 직전 완료 봉 목표 비중 50%; 다음 봉 시가 가정 |
| v2 | ema_12_26 | 9432.78 | -567.22 | 중단: 손실 한도 / buy / partial / EMA12 > EMA26; 조건 충족; EMA12=726.261, EMA26=726.172; 직전 완료 봉 목표를 다음 봉 시가에 모의 적용 |
| v2 | macd_12_26_9 | 9984.52 | -15.48 | sell / filled / MACD > 신호선 그리고 MACD > 0; 조건 미충족; MACD=2.92675, signal9=3.02629; 직전 완료 봉 목표를 다음 봉 시가에 모의 적용 |
| v2 | rsi_14_recovery | 9995.22 | -4.78 | sell / filled / 직전 RSI14 < 30, 현재 RSI14 >= 30 (한 봉 목표); 조건 미충족; RSI14=43.621, previous_RSI14=38.5787; 직전 완료 봉 목표를 다음 봉 시가에 모의 적용 |
| v2 | bollinger_20_reentry | 9685.73 | -314.27 | sell / filled / 직전 종가 < 직전 하단밴드, 현재 하단밴드 <= 종가 <= SMA20 (한 봉 목표); 조건 미충족; close=698.04, lower20=693.892, SMA20=727.609, previous_lower20=698.501; 직전 완료 봉 목표를 다음 봉 시가에 모의 적용 |
| v2 | donchian_20 | 9939.30 | -60.70 | sell / filled / 종가 > 현재 봉을 제외한 직전 20봉 최고가; 조건 미충족; close=735.35, prior_high20=745; 직전 완료 봉 목표를 다음 봉 시가에 모의 적용 |
| v2 | atr_14_breakout | 9758.55 | -241.45 | sell / filled / 종가 > 직전 종가 + 직전 ATR14 그리고 종가 > EMA26; 조건 미충족; close=735.35, threshold=737.263, prior_ATR14=4.10289, EMA26=727.331; 직전 완료 봉 목표를 다음 봉 시가에 모의 적용 |
| v2 | session_vwap | 9083.37 | -916.63 | 중단: 손실 한도 / buy / partial / 종가 > 뉴욕 거래일별 누적 전형가격 VWAP; 조건 충족; close=734.98, session_VWAP=734.093, session_volume=764353; 직전 완료 봉 목표를 다음 봉 시가에 모의 적용 |
| v2 | obv_20 | 9369.89 | -630.11 | 중단: 손실 한도 / buy / partial / OBV > OBV의 SMA20 그리고 종가 > EMA26; 조건 충족; OBV=-5.0567e+06, OBV_SMA20=-6.30537e+06, close=733.16, EMA26=726.69; 직전 완료 봉 목표를 다음 봉 시가에 모의 적용 |
| v2 | stochastic_14_3_recovery | 9757.14 | -242.86 | sell / filled / 직전 %K14 < 20에서 %K14가 %D3 상향 돌파 (한 봉 목표); 조건 미충족; K14=0.622844, D3=3.92968, previous_K14=8.58265, previous_D3=4.55061; 직전 완료 봉 목표를 다음 봉 시가에 모의 적용 |
| v2 | mfi_14_recovery | 10064.61 | 64.61 | sell / filled / 직전 MFI14 < 20, 현재 MFI14 >= 20 (한 봉 목표); 조건 미충족; MFI14=32.7313, previous_MFI14=24.1736; 직전 완료 봉 목표를 다음 봉 시가에 모의 적용 |
| v2 | adx_14_trend | 9450.93 | -549.07 | 중단: 손실 한도 / buy / partial / Wilder ADX14 >= 25 그리고 +DI14 > -DI14; 조건 충족; ADX14=25.4031, plus_DI14=35.2628, minus_DI14=13.9603; 직전 완료 봉 목표를 다음 봉 시가에 모의 적용 |
| v2 | aroon_25_trend | 9973.62 | -26.38 | sell / filled / Aroon25 Up > 70 그리고 Down < 30 (동률이면 최신 극값); 조건 미충족; Aroon_up=68, Aroon_down=20; 직전 완료 봉 목표를 다음 봉 시가에 모의 적용 |
| v2 | cci_20_momentum | 9854.97 | -145.03 | sell / filled / CCI20 > 100 (전형가격·평균절대편차); 조건 미충족; CCI20=99.2123; 직전 완료 봉 목표를 다음 봉 시가에 모의 적용 |
| v2 | williams_14_recovery | 9999.06 | -0.94 | sell / filled / 직전 Williams %R14 < -80, 현재 >= -80 (한 봉 목표); 조건 미충족; Williams_R14=-40.3504, previous_R14=-56.1644; 직전 완료 봉 목표를 다음 봉 시가에 모의 적용 |
| v2 | cmf_20_accumulation | 9290.12 | -709.88 | 중단: 손실 한도 / buy / partial / Chaikin Money Flow20 > 0.1; 조건 충족; CMF20=0.145111, volume20=965726; 직전 완료 봉 목표를 다음 봉 시가에 모의 적용 |
| v2 | chaikin_3_10 | 9184.42 | -815.58 | 중단: 손실 한도 / buy / partial / ADL의 EMA3 - EMA10 > 0 그리고 종가 > EMA26; 조건 충족; Chaikin3_10=293683, ADL=-4.91156e+06, close=739.58, EMA26=736.187; 직전 완료 봉 목표를 다음 봉 시가에 모의 적용 |
| v2 | roc_10_momentum | 9888.81 | -111.19 | sell / filled / 10봉 ROC > 1% 그리고 종가 > EMA26; 조건 미충족; ROC10_percent=0.883016, close=741.47, EMA26=734.681; 직전 완료 봉 목표를 다음 봉 시가에 모의 적용 |
| v2 | trix_15_trend | 9193.67 | -806.33 | 중단: 손실 한도 / buy / partial / 15봉 삼중 EMA의 1봉 변화율 TRIX > 0 그리고 종가 > EMA26; 조건 충족; TRIX15_percent=0.0196284, close=739.58, EMA26=736.187; 직전 완료 봉 목표를 다음 봉 시가에 모의 적용 |
| v2 | keltner_20_breakout | 10000.00 | 0.00 | 대기 /  / 새 신호 대기 |
| v2 | opening_range_30m | 10158.15 | 158.15 | sell / filled / 뉴욕 09:30·09:45 두 완료 봉 최고가를 10:00 이후 종가가 돌파; 자료 부족·변동폭 또는 거래량 없음: 대기; close=733.16; 직전 완료 봉 목표를 다음 봉 시가에 모의 적용 |

### 같은 기간의 비용·노출 비교 (사후 연구)

| 전략 | 비용 전 | 비용 후 | 100% 보유 | 같은 평균 노출 보유 | 평균 노출 |
|---|---:|---:|---:|---:|---:|
| cash | 0.00% | 0.00% | -15.62% | -0.00% | 0.00% |
| buy_hold | -15.26% | -15.62% | -15.62% | -15.62% | 100.00% |
| trend_8_26 | -2.15% | -5.78% | -15.62% | -7.63% | 47.49% |
| momentum_26 | -5.67% | -9.93% | -15.62% | -7.30% | 45.38% |
| breakout_8 | -2.56% | -14.45% | -15.62% | -2.50% | 15.30% |
| reversion_12 | -4.74% | -17.07% | -15.62% | -4.42% | 27.18% |
| volume_26 | -2.47% | -10.70% | -15.62% | -1.43% | 8.71% |
| trend_8_26 AND momentum_26 | -1.56% | -4.81% | -15.62% | -6.51% | 40.37% |
| trend_8_26 + momentum_26 | -3.90% | -7.86% | -15.62% | -7.47% | 46.44% |
| trend_8_26 AND breakout_8 | -1.08% | -7.90% | -15.62% | -1.43% | 8.71% |
| trend_8_26 + breakout_8 | -2.30% | -9.99% | -15.62% | -5.09% | 31.40% |
| trend_8_26 AND reversion_12 | 0.96% | -5.20% | -15.62% | -0.91% | 5.54% |
| trend_8_26 + reversion_12 | -3.36% | -10.62% | -15.62% | -6.04% | 37.34% |
| trend_8_26 AND volume_26 | 2.90% | 1.18% | -15.62% | -0.26% | 1.58% |
| trend_8_26 + volume_26 | -2.24% | -7.65% | -15.62% | -4.56% | 28.10% |
| momentum_26 AND breakout_8 | -1.82% | -9.35% | -15.62% | -1.47% | 8.97% |
| momentum_26 + breakout_8 | -4.08% | -12.19% | -15.62% | -4.92% | 30.35% |
| momentum_26 AND reversion_12 | -2.85% | -8.78% | -15.62% | -1.04% | 6.33% |
| momentum_26 + reversion_12 | -5.14% | -13.36% | -15.62% | -5.87% | 36.29% |
| momentum_26 AND volume_26 | 2.69% | 0.55% | -15.62% | -0.26% | 1.58% |
| momentum_26 + volume_26 | -4.02% | -9.71% | -15.62% | -4.40% | 27.05% |
| breakout_8 AND reversion_12 | 0.00% | 0.00% | -15.62% | -0.00% | 0.00% |
| breakout_8 + reversion_12 | -3.59% | -15.04% | -15.62% | -3.46% | 21.25% |
| breakout_8 AND volume_26 | 0.55% | -1.13% | -15.62% | -0.17% | 1.06% |
| breakout_8 + volume_26 | -2.48% | -12.03% | -15.62% | -1.97% | 12.01% |
| reversion_12 AND volume_26 | -1.80% | -7.02% | -15.62% | -0.91% | 5.54% |
| reversion_12 + volume_26 | -3.57% | -13.57% | -15.62% | -2.93% | 17.95% |
| ema_12_26 | -2.40% | -4.03% | -15.62% | -7.01% | 43.54% |
| macd_12_26_9 | 3.46% | 0.88% | -15.62% | -4.42% | 27.18% |
| rsi_14_recovery | 0.45% | -5.28% | -15.62% | -0.61% | 3.69% |
| bollinger_20_reentry | -0.39% | -5.68% | -15.62% | -0.56% | 3.43% |
| donchian_20 | -0.65% | -3.93% | -15.62% | -0.56% | 3.43% |
| atr_14_breakout | -1.18% | -6.04% | -15.62% | -0.56% | 3.43% |
| session_vwap | -0.49% | -12.27% | -15.62% | -7.80% | 48.55% |
| obv_20 | -4.17% | -13.00% | -15.62% | -4.04% | 24.80% |
| stochastic_14_3_recovery | -1.54% | -11.36% | -15.62% | -1.08% | 6.60% |
| mfi_14_recovery | 2.16% | -0.38% | -15.62% | -0.26% | 1.58% |
| adx_14_trend | -5.42% | -7.77% | -15.62% | -2.07% | 12.66% |
| aroon_25_trend | 0.17% | -3.54% | -15.62% | -1.90% | 11.61% |
| cci_20_momentum | -3.28% | -8.04% | -15.62% | -2.42% | 14.78% |
| williams_14_recovery | 0.42% | -6.50% | -15.62% | -0.74% | 4.49% |
| cmf_20_accumulation | -6.74% | -13.53% | -15.62% | -3.23% | 19.79% |
| chaikin_3_10 | -6.34% | -14.96% | -15.62% | -5.22% | 32.19% |
| roc_10_momentum | -1.46% | -7.08% | -15.62% | -1.99% | 12.14% |
| trix_15_trend | -3.56% | -7.53% | -15.62% | -5.72% | 35.36% |
| keltner_20_breakout | -2.06% | -3.70% | -15.62% | -0.30% | 1.85% |
| opening_range_30m | 7.87% | 3.43% | -15.62% | -3.82% | 23.48% |

동일 구간·초기 자금, 종료 시 청산 비용 포함. 노출 맞춤은 사후 설명용이며 v2 실제 계좌 성과가 아닙니다.
[낙폭 분해·비용 영향·전체 구간](CAT/comparison.json)

[v1 전체 기록](CAT/accounts.json) · [v2 전체 기록](CAT/accounts-v2.json)

## WMT 계좌

| 모델 | 전략 | 평가액 USD | 손익 USD | 최근 매매·이유 |
|---|---|---:|---:|---|
| v1 | cash | 10000.00 | 0.00 | 대기 /  / 새 신호 대기 |
| v1 | buy_hold | 10140.84 | 140.84 | buy /  / buy_hold: prior completed bar target 100%; next bar open simulation |
| v1 | trend_8_26 | 9799.88 | -200.12 | buy /  / trend_8_26: prior completed bar target 100%; next bar open simulation |
| v1 | momentum_26 | 9915.94 | -84.06 | buy /  / momentum_26: prior completed bar target 100%; next bar open simulation |
| v1 | breakout_8 | 9531.79 | -468.21 | sell /  / breakout_8: prior completed bar target 0%; next bar open simulation |
| v1 | reversion_12 | 9573.71 | -426.29 | sell /  / reversion_12: prior completed bar target 0%; next bar open simulation |
| v1 | volume_26 | 9775.35 | -224.65 | sell /  / volume_26: prior completed bar target 0%; next bar open simulation |
| v1 | trend_8_26 AND momentum_26 | 9881.66 | -118.34 | buy /  / trend_8_26 AND momentum_26: prior completed bar target 100%; next bar open simulation |
| v1 | trend_8_26 + momentum_26 | 9857.76 | -142.24 | buy /  / trend_8_26 + momentum_26: prior completed bar target 100%; next bar open simulation |
| v1 | trend_8_26 AND breakout_8 | 9797.07 | -202.93 | sell /  / trend_8_26 AND breakout_8: prior completed bar target 0%; next bar open simulation |
| v1 | trend_8_26 + breakout_8 | 9684.40 | -315.60 | sell /  / trend_8_26 + breakout_8: prior completed bar target 50%; next bar open simulation |
| v1 | trend_8_26 AND reversion_12 | 9741.18 | -258.82 | sell /  / trend_8_26 AND reversion_12: prior completed bar target 0%; next bar open simulation |
| v1 | trend_8_26 + reversion_12 | 9725.12 | -274.88 | buy /  / trend_8_26 + reversion_12: prior completed bar target 50%; next bar open simulation |
| v1 | trend_8_26 AND volume_26 | 9837.96 | -162.04 | sell /  / trend_8_26 AND volume_26: prior completed bar target 0%; next bar open simulation |
| v1 | trend_8_26 + volume_26 | 9788.09 | -211.91 | buy /  / trend_8_26 + volume_26: prior completed bar target 50%; next bar open simulation |
| v1 | momentum_26 AND breakout_8 | 9707.53 | -292.47 | sell /  / momentum_26 AND breakout_8: prior completed bar target 0%; next bar open simulation |
| v1 | momentum_26 + breakout_8 | 9780.83 | -219.17 | sell /  / momentum_26 + breakout_8: prior completed bar target 50%; next bar open simulation |
| v1 | momentum_26 AND reversion_12 | 9935.88 | -64.12 | sell /  / momentum_26 AND reversion_12: prior completed bar target 0%; next bar open simulation |
| v1 | momentum_26 + reversion_12 | 9841.23 | -158.77 | buy /  / momentum_26 + reversion_12: prior completed bar target 50%; next bar open simulation |
| v1 | momentum_26 AND volume_26 | 9853.50 | -146.50 | sell /  / momentum_26 AND volume_26: prior completed bar target 0%; next bar open simulation |
| v1 | momentum_26 + volume_26 | 9885.29 | -114.71 | buy /  / momentum_26 + volume_26: prior completed bar target 50%; next bar open simulation |
| v1 | breakout_8 AND reversion_12 | 10000.00 | 0.00 | 대기 /  / 새 신호 대기 |
| v1 | breakout_8 + reversion_12 | 9590.83 | -409.17 | sell /  / breakout_8 + reversion_12: prior completed bar target 0%; next bar open simulation |
| v1 | breakout_8 AND volume_26 | 9797.95 | -202.05 | sell /  / breakout_8 AND volume_26: prior completed bar target 0%; next bar open simulation |
| v1 | breakout_8 + volume_26 | 9653.07 | -346.93 | sell /  / breakout_8 + volume_26: prior completed bar target 0%; next bar open simulation |
| v1 | reversion_12 AND volume_26 | 9911.53 | -88.47 | sell /  / reversion_12 AND volume_26: prior completed bar target 0%; next bar open simulation |
| v1 | reversion_12 + volume_26 | 9732.36 | -267.64 | sell /  / reversion_12 + volume_26: prior completed bar target 0%; next bar open simulation |
| v1 | ema_12_26 | 10020.23 | 20.23 | buy /  / EMA12 > EMA26; 조건 충족; EMA12=117.957, EMA26=117.935 |
| v1 | macd_12_26_9 | 10100.02 | 100.02 | buy /  / MACD > 신호선 그리고 MACD > 0; 조건 충족; MACD=0.0217894, signal9=-0.0690006 |
| v1 | rsi_14_recovery | 9973.19 | -26.81 | sell /  / 직전 RSI14 < 30, 현재 RSI14 >= 30 (한 봉 목표); 조건 미충족; RSI14=46.7246, previous_RSI14=43.1348 |
| v1 | bollinger_20_reentry | 9975.54 | -24.46 | sell /  / 직전 종가 < 직전 하단밴드, 현재 하단밴드 <= 종가 <= SMA20 (한 봉 목표); 조건 미충족; close=117.73, lower20=117.465, SMA20=117.829, previous_lower20=117.475 |
| v1 | donchian_20 | 9863.66 | -136.34 | sell /  / 종가 > 현재 봉을 제외한 직전 20봉 최고가; 조건 미충족; close=119.95, prior_high20=120.08 |
| v1 | atr_14_breakout | 9811.78 | -188.22 | sell /  / 종가 > 직전 종가 + 직전 ATR14 그리고 종가 > EMA26; 조건 미충족; close=120.03, threshold=120.128, prior_ATR14=0.443028, EMA26=118.335 |
| v1 | session_vwap | 9616.87 | -383.13 | buy /  / 종가 > 뉴욕 거래일별 누적 전형가격 VWAP; 조건 충족; close=118.96, session_VWAP=118.576, session_volume=4.484e+06 |
| v1 | obv_20 | 9972.84 | -27.16 | buy /  / OBV > OBV의 SMA20 그리고 종가 > EMA26; 조건 충족; OBV=1.42093e+07, OBV_SMA20=1.04391e+07, close=118.41, EMA26=117.87 |
| v1 | stochastic_14_3_recovery | 9463.72 | -536.28 | sell /  / 직전 %K14 < 20에서 %K14가 %D3 상향 돌파 (한 봉 목표); 조건 미충족; K14=38.3112, D3=17.7755, previous_K14=8.66597, previous_D3=7.09962 |
| v1 | mfi_14_recovery | 9969.08 | -30.92 | sell /  / 직전 MFI14 < 20, 현재 MFI14 >= 20 (한 봉 목표); 조건 미충족; MFI14=57.3162, previous_MFI14=36.5877 |
| v1 | adx_14_trend | 10108.49 | 108.49 | buy /  / Wilder ADX14 >= 25 그리고 +DI14 > -DI14; 조건 충족; ADX14=32.9742, plus_DI14=41.4463, minus_DI14=15.2475 |
| v1 | aroon_25_trend | 9954.43 | -45.57 | sell /  / Aroon25 Up > 70 그리고 Down < 30 (동률이면 최신 극값); 조건 미충족; Aroon_up=84, Aroon_down=76 |
| v1 | cci_20_momentum | 9805.36 | -194.64 | buy /  / CCI20 > 100 (전형가격·평균절대편차); 조건 충족; CCI20=227.859 |
| v1 | williams_14_recovery | 9739.33 | -260.67 | sell /  / 직전 Williams %R14 < -80, 현재 >= -80 (한 봉 목표); 조건 미충족; Williams_R14=-50.649, previous_R14=-61.6888 |
| v1 | cmf_20_accumulation | 9738.99 | -261.01 | buy /  / Chaikin Money Flow20 > 0.1; 조건 충족; CMF20=0.134813, volume20=1.25189e+07 |
| v1 | chaikin_3_10 | 9729.99 | -270.01 | buy /  / ADL의 EMA3 - EMA10 > 0 그리고 종가 > EMA26; 조건 충족; Chaikin3_10=239030, ADL=8.86177e+06, close=118.96, EMA26=118.011 |
| v1 | roc_10_momentum | 10071.37 | 71.37 | buy /  / 10봉 ROC > 1% 그리고 종가 > EMA26; 조건 충족; ROC10_percent=1.0791, close=118.96, EMA26=118.011 |
| v1 | trix_15_trend | 9717.49 | -282.51 | buy /  / 15봉 삼중 EMA의 1봉 변화율 TRIX > 0 그리고 종가 > EMA26; 조건 충족; TRIX15_percent=0.00531527, close=119.685, EMA26=118.199 |
| v1 | keltner_20_breakout | 10006.88 | 6.88 | buy /  / 종가 > EMA20 + 2 x Wilder ATR14; 조건 충족; close=118.96, upper_Keltner=118.84, EMA20=118.021, ATR14=0.409337 |
| v1 | opening_range_30m | 9794.75 | -205.25 | buy /  / 뉴욕 09:30·09:45 두 완료 봉 최고가를 10:00 이후 종가가 돌파; 조건 충족; close=119.685, opening_high=119.42 |
| v2 | cash | 10000.00 | 0.00 | 대기 /  / 새 신호 대기 |
| v2 | buy_hold | 10744.12 | 744.12 | buy / partial / 직전 완료 봉 목표 비중 100%; 다음 봉 시가 가정 |
| v2 | trend_8_26 | 10193.11 | 193.11 | buy / partial / 직전 완료 봉 목표 비중 100%; 다음 봉 시가 가정 |
| v2 | momentum_26 | 10318.71 | 318.71 | buy / partial / 직전 완료 봉 목표 비중 100%; 다음 봉 시가 가정 |
| v2 | breakout_8 | 9477.22 | -522.78 | sell / filled / 직전 완료 봉 목표 비중 0%; 다음 봉 시가 가정 |
| v2 | reversion_12 | 9466.17 | -533.83 | sell / filled / 직전 완료 봉 목표 비중 0%; 다음 봉 시가 가정 |
| v2 | volume_26 | 9727.78 | -272.22 | sell / filled / 직전 완료 봉 목표 비중 0%; 다음 봉 시가 가정 |
| v2 | trend_8_26 AND momentum_26 | 10278.17 | 278.17 | buy / partial / 직전 완료 봉 목표 비중 100%; 다음 봉 시가 가정 |
| v2 | trend_8_26 + momentum_26 | 10255.69 | 255.69 | buy / partial / 직전 완료 봉 목표 비중 100%; 다음 봉 시가 가정 |
| v2 | trend_8_26 AND breakout_8 | 9873.94 | -126.06 | sell / filled / 직전 완료 봉 목표 비중 0%; 다음 봉 시가 가정 |
| v2 | trend_8_26 + breakout_8 | 9849.84 | -150.16 | sell / filled / 직전 완료 봉 목표 비중 50%; 다음 봉 시가 가정 |
| v2 | trend_8_26 AND reversion_12 | 9545.32 | -454.68 | sell / filled / 직전 완료 봉 목표 비중 0%; 다음 봉 시가 가정 |
| v2 | trend_8_26 + reversion_12 | 9865.80 | -134.20 | buy / filled / 직전 완료 봉 목표 비중 50%; 다음 봉 시가 가정 |
| v2 | trend_8_26 AND volume_26 | 9784.10 | -215.90 | sell / filled / 직전 완료 봉 목표 비중 0%; 다음 봉 시가 가정 |
| v2 | trend_8_26 + volume_26 | 9959.62 | -40.38 | buy / filled / 직전 완료 봉 목표 비중 50%; 다음 봉 시가 가정 |
| v2 | momentum_26 AND breakout_8 | 9659.68 | -340.32 | sell / filled / 직전 완료 봉 목표 비중 0%; 다음 봉 시가 가정 |
| v2 | momentum_26 + breakout_8 | 9952.27 | -47.73 | sell / filled / 직전 완료 봉 목표 비중 50%; 다음 봉 시가 가정 |
| v2 | momentum_26 AND reversion_12 | 9759.91 | -240.09 | sell / filled / 직전 완료 봉 목표 비중 0%; 다음 봉 시가 가정 |
| v2 | momentum_26 + reversion_12 | 10031.05 | 31.05 | buy / filled / 직전 완료 봉 목표 비중 50%; 다음 봉 시가 가정 |
| v2 | momentum_26 AND volume_26 | 9760.78 | -239.22 | sell / filled / 직전 완료 봉 목표 비중 0%; 다음 봉 시가 가정 |
| v2 | momentum_26 + volume_26 | 10062.97 | 62.97 | buy / filled / 직전 완료 봉 목표 비중 50%; 다음 봉 시가 가정 |
| v2 | breakout_8 AND reversion_12 | 10000.00 | 0.00 | 대기 /  / 새 신호 대기 |
| v2 | breakout_8 + reversion_12 | 9532.44 | -467.56 | sell / filled / 직전 완료 봉 목표 비중 0%; 다음 봉 시가 가정 |
| v2 | breakout_8 AND volume_26 | 9741.39 | -258.61 | sell / filled / 직전 완료 봉 목표 비중 0%; 다음 봉 시가 가정 |
| v2 | breakout_8 + volume_26 | 9603.26 | -396.74 | sell / filled / 직전 완료 봉 목표 비중 0%; 다음 봉 시가 가정 |
| v2 | reversion_12 AND volume_26 | 9917.25 | -82.75 | sell / filled / 직전 완료 봉 목표 비중 0%; 다음 봉 시가 가정 |
| v2 | reversion_12 + volume_26 | 9656.74 | -343.26 | sell / filled / 직전 완료 봉 목표 비중 0%; 다음 봉 시가 가정 |
| v2 | ema_12_26 | 10015.23 | 15.23 | buy / partial / EMA12 > EMA26; 조건 충족; EMA12=117.957, EMA26=117.935; 직전 완료 봉 목표를 다음 봉 시가에 모의 적용 |
| v2 | macd_12_26_9 | 10094.97 | 94.97 | buy / partial / MACD > 신호선 그리고 MACD > 0; 조건 충족; MACD=0.0217894, signal9=-0.0690006; 직전 완료 봉 목표를 다음 봉 시가에 모의 적용 |
| v2 | rsi_14_recovery | 9971.19 | -28.81 | sell / filled / 직전 RSI14 < 30, 현재 RSI14 >= 30 (한 봉 목표); 조건 미충족; RSI14=46.7246, previous_RSI14=43.1348; 직전 완료 봉 목표를 다음 봉 시가에 모의 적용 |
| v2 | bollinger_20_reentry | 9967.56 | -32.44 | sell / filled / 직전 종가 < 직전 하단밴드, 현재 하단밴드 <= 종가 <= SMA20 (한 봉 목표); 조건 미충족; close=117.73, lower20=117.465, SMA20=117.829, previous_lower20=117.475; 직전 완료 봉 목표를 다음 봉 시가에 모의 적용 |
| v2 | donchian_20 | 9857.75 | -142.25 | sell / filled / 종가 > 현재 봉을 제외한 직전 20봉 최고가; 조건 미충족; close=119.95, prior_high20=120.08; 직전 완료 봉 목표를 다음 봉 시가에 모의 적용 |
| v2 | atr_14_breakout | 9801.98 | -198.02 | sell / filled / 종가 > 직전 종가 + 직전 ATR14 그리고 종가 > EMA26; 조건 미충족; close=120.03, threshold=120.128, prior_ATR14=0.443028, EMA26=118.335; 직전 완료 봉 목표를 다음 봉 시가에 모의 적용 |
| v2 | session_vwap | 9596.70 | -403.30 | buy / partial / 종가 > 뉴욕 거래일별 누적 전형가격 VWAP; 조건 충족; close=118.96, session_VWAP=118.576, session_volume=4.484e+06; 직전 완료 봉 목표를 다음 봉 시가에 모의 적용 |
| v2 | obv_20 | 9961.87 | -38.13 | buy / partial / OBV > OBV의 SMA20 그리고 종가 > EMA26; 조건 충족; OBV=1.42093e+07, OBV_SMA20=1.04391e+07, close=118.41, EMA26=117.87; 직전 완료 봉 목표를 다음 봉 시가에 모의 적용 |
| v2 | stochastic_14_3_recovery | 9839.86 | -160.14 | 중단: 손실 한도 / buy / partial / 직전 %K14 < 20에서 %K14가 %D3 상향 돌파 (한 봉 목표); 조건 충족; K14=25.6758, D3=22.4971, previous_K14=12.8379, previous_D3=25.8704; 직전 완료 봉 목표를 다음 봉 시가에 모의 적용 |
| v2 | mfi_14_recovery | 9961.11 | -38.89 | sell / filled / 직전 MFI14 < 20, 현재 MFI14 >= 20 (한 봉 목표); 조건 미충족; MFI14=57.3162, previous_MFI14=36.5877; 직전 완료 봉 목표를 다음 봉 시가에 모의 적용 |
| v2 | adx_14_trend | 10105.46 | 105.46 | buy / partial / Wilder ADX14 >= 25 그리고 +DI14 > -DI14; 조건 충족; ADX14=32.9742, plus_DI14=41.4463, minus_DI14=15.2475; 직전 완료 봉 목표를 다음 봉 시가에 모의 적용 |
| v2 | aroon_25_trend | 9948.46 | -51.54 | sell / filled / Aroon25 Up > 70 그리고 Down < 30 (동률이면 최신 극값); 조건 미충족; Aroon_up=84, Aroon_down=76; 직전 완료 봉 목표를 다음 봉 시가에 모의 적용 |
| v2 | cci_20_momentum | 9796.54 | -203.46 | buy / partial / CCI20 > 100 (전형가격·평균절대편차); 조건 충족; CCI20=227.859; 직전 완료 봉 목표를 다음 봉 시가에 모의 적용 |
| v2 | williams_14_recovery | 9725.71 | -274.29 | sell / filled / 직전 Williams %R14 < -80, 현재 >= -80 (한 봉 목표); 조건 미충족; Williams_R14=-50.649, previous_R14=-61.6888; 직전 완료 봉 목표를 다음 봉 시가에 모의 적용 |
| v2 | cmf_20_accumulation | 9726.34 | -273.66 | buy / partial / Chaikin Money Flow20 > 0.1; 조건 충족; CMF20=0.134813, volume20=1.25189e+07; 직전 완료 봉 목표를 다음 봉 시가에 모의 적용 |
| v2 | chaikin_3_10 | 9711.53 | -288.47 | buy / partial / ADL의 EMA3 - EMA10 > 0 그리고 종가 > EMA26; 조건 충족; Chaikin3_10=239030, ADL=8.86177e+06, close=118.96, EMA26=118.011; 직전 완료 봉 목표를 다음 봉 시가에 모의 적용 |
| v2 | roc_10_momentum | 10070.36 | 70.36 | buy / partial / 10봉 ROC > 1% 그리고 종가 > EMA26; 조건 충족; ROC10_percent=1.0791, close=118.96, EMA26=118.011; 직전 완료 봉 목표를 다음 봉 시가에 모의 적용 |
| v2 | trix_15_trend | 9704.86 | -295.14 | buy / partial / 15봉 삼중 EMA의 1봉 변화율 TRIX > 0 그리고 종가 > EMA26; 조건 충족; TRIX15_percent=0.00531527, close=119.685, EMA26=118.199; 직전 완료 봉 목표를 다음 봉 시가에 모의 적용 |
| v2 | keltner_20_breakout | 10003.88 | 3.88 | buy / partial / 종가 > EMA20 + 2 x Wilder ATR14; 조건 충족; close=118.96, upper_Keltner=118.84, EMA20=118.021, ATR14=0.409337; 직전 완료 봉 목표를 다음 봉 시가에 모의 적용 |
| v2 | opening_range_30m | 9785.94 | -214.06 | buy / partial / 뉴욕 09:30·09:45 두 완료 봉 최고가를 10:00 이후 종가가 돌파; 조건 충족; close=119.685, opening_high=119.42; 직전 완료 봉 목표를 다음 봉 시가에 모의 적용 |

### 같은 기간의 비용·노출 비교 (사후 연구)

| 전략 | 비용 전 | 비용 후 | 100% 보유 | 같은 평균 노출 보유 | 평균 노출 |
|---|---:|---:|---:|---:|---:|
| cash | 0.00% | 0.00% | 13.90% | 0.00% | 0.00% |
| buy_hold | 14.38% | 13.90% | 13.90% | 13.90% | 100.00% |
| trend_8_26 | 9.47% | 5.41% | 13.90% | 9.48% | 69.66% |
| momentum_26 | 11.96% | 6.01% | 13.90% | 9.85% | 72.30% |
| breakout_8 | 6.42% | -10.41% | 13.90% | 3.45% | 26.12% |
| reversion_12 | 4.08% | -7.08% | 13.90% | 2.46% | 18.73% |
| volume_26 | 2.19% | -4.05% | 13.90% | 0.79% | 6.07% |
| trend_8_26 AND momentum_26 | 9.64% | 4.69% | 13.90% | 8.69% | 64.12% |
| trend_8_26 + momentum_26 | 10.71% | 5.71% | 13.90% | 9.67% | 70.98% |
| trend_8_26 AND breakout_8 | 6.88% | -6.56% | 13.90% | 2.85% | 21.64% |
| trend_8_26 + breakout_8 | 7.95% | -2.61% | 13.90% | 6.42% | 47.90% |
| trend_8_26 AND reversion_12 | 0.15% | -5.97% | 13.90% | 0.96% | 7.39% |
| trend_8_26 + reversion_12 | 6.78% | -0.39% | 13.90% | 5.91% | 44.20% |
| trend_8_26 AND volume_26 | 0.24% | -2.26% | 13.90% | 0.27% | 2.11% |
| trend_8_26 + volume_26 | 5.81% | 1.01% | 13.90% | 5.04% | 37.87% |
| momentum_26 AND breakout_8 | 6.72% | -8.26% | 13.90% | 3.16% | 24.01% |
| momentum_26 + breakout_8 | 9.17% | -1.92% | 13.90% | 6.60% | 49.21% |
| momentum_26 AND reversion_12 | 1.65% | -4.16% | 13.90% | 0.96% | 7.39% |
| momentum_26 + reversion_12 | 7.99% | 1.80% | 13.90% | 6.09% | 45.52% |
| momentum_26 AND volume_26 | 1.51% | -3.07% | 13.90% | 0.41% | 3.17% |
| momentum_26 + volume_26 | 7.01% | 1.30% | 13.90% | 5.22% | 39.19% |
| breakout_8 AND reversion_12 | 0.00% | 0.00% | 13.90% | 0.00% | 0.00% |
| breakout_8 + reversion_12 | 5.27% | -7.99% | 13.90% | 2.95% | 22.44% |
| breakout_8 AND volume_26 | 0.64% | -2.68% | 13.90% | 0.31% | 2.37% |
| breakout_8 + volume_26 | 4.31% | -7.08% | 13.90% | 2.11% | 16.10% |
| reversion_12 AND volume_26 | 0.01% | -2.48% | 13.90% | 0.24% | 1.85% |
| reversion_12 + volume_26 | 3.14% | -4.78% | 13.90% | 1.62% | 12.41% |
| ema_12_26 | 12.70% | 10.82% | 13.90% | 10.19% | 74.67% |
| macd_12_26_9 | 10.13% | 5.60% | 13.90% | 5.06% | 37.99% |
| rsi_14_recovery | 0.20% | -0.64% | 13.90% | 0.07% | 0.53% |
| bollinger_20_reentry | 2.64% | -0.34% | 13.90% | 0.24% | 1.85% |
| donchian_20 | 4.69% | -7.70% | 13.90% | 1.76% | 13.46% |
| atr_14_breakout | -0.69% | -10.96% | 13.90% | 1.03% | 7.92% |
| session_vwap | 8.81% | -2.85% | 13.90% | 7.87% | 58.31% |
| obv_20 | 12.20% | 4.03% | 13.90% | 7.83% | 58.05% |
| stochastic_14_3_recovery | 0.13% | -8.71% | 13.90% | 0.76% | 5.80% |
| mfi_14_recovery | 1.30% | -0.39% | 13.90% | 0.14% | 1.06% |
| adx_14_trend | 10.22% | 7.47% | 13.90% | 7.02% | 52.24% |
| aroon_25_trend | 7.51% | 2.23% | 13.90% | 4.30% | 32.45% |
| cci_20_momentum | 7.30% | -1.75% | 13.90% | 4.45% | 33.51% |
| williams_14_recovery | 0.89% | -7.63% | 13.90% | 0.72% | 5.54% |
| cmf_20_accumulation | 9.25% | -0.39% | 13.90% | 5.38% | 40.37% |
| chaikin_3_10 | 10.58% | 0.82% | 13.90% | 7.21% | 53.56% |
| roc_10_momentum | 0.62% | -4.32% | 13.90% | 2.00% | 15.30% |
| trix_15_trend | 11.30% | 6.72% | 13.90% | 8.95% | 65.96% |
| keltner_20_breakout | 7.56% | 0.57% | 13.90% | 3.70% | 27.97% |
| opening_range_30m | 9.88% | 3.17% | 13.90% | 5.13% | 38.52% |

동일 구간·초기 자금, 종료 시 청산 비용 포함. 노출 맞춤은 사후 설명용이며 v2 실제 계좌 성과가 아닙니다.
[낙폭 분해·비용 영향·전체 구간](WMT/comparison.json)

[v1 전체 기록](WMT/accounts.json) · [v2 전체 기록](WMT/accounts-v2.json)
