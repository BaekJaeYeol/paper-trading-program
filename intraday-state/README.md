# 모의투자 운영 현황

[PC·서버 장애 진단과 복구 방법](https://github.com/BaekJaeYeol/paper-trading-program/blob/main/investment-lab/docs/failure-recovery.md)

이번 실행 복구: {}

완료 봉 확인 주기: 기록 2/8회 · 기록 없는 예정 6회 · 아직 판정 전 18회 · 주의: 예약 시작 지연 또는 실행·저장 누락을 확인하세요.

[주기 판정 기준](https://github.com/BaekJaeYeol/paper-trading-program/blob/main/investment-lab/docs/session-coverage.md)

최근 확인: 2026-10-16T15:52:00.417305+00:00 (UTC)
다음 15분 확인 목표 (세션 실행 중에만 적용): 2026-10-16T16:07:00+00:00 (UTC, 실행 지연 가능)

실제 주문 없음. v1 기존 계좌와 v2 새 계좌의 시작일이 다르므로 수익률을 직접 우열 비교하지 마세요.
v2는 다음 봉 시가에 비용·스프레드·직전 거래량 제한을 적용한 가상 체결입니다. 미체결 잔량은 만료됩니다.

| 종목 | 상태 | 최근 성공 UTC | 마지막 완료 봉 UTC | 이번 새 봉 |
|---|---|---|---|---|
| SPY | updated | 2026-10-16T15:52:00.417305+00:00 | 2026-10-16T15:30:00+00:00 | 1 |
| QQQ | updated | 2026-10-16T15:52:00.417305+00:00 | 2026-10-16T15:30:00+00:00 | 1 |
| IWM | updated | 2026-10-16T15:52:00.417305+00:00 | 2026-10-16T15:30:00+00:00 | 1 |
| DIA | updated | 2026-10-16T15:52:00.417305+00:00 | 2026-10-16T15:30:00+00:00 | 1 |
| MSFT | updated | 2026-10-16T15:52:00.417305+00:00 | 2026-10-16T15:30:00+00:00 | 1 |
| JPM | updated | 2026-10-16T15:52:00.417305+00:00 | 2026-10-16T15:30:00+00:00 | 1 |
| XOM | updated | 2026-10-16T15:52:00.417305+00:00 | 2026-10-16T15:30:00+00:00 | 1 |
| JNJ | updated | 2026-10-16T15:52:00.417305+00:00 | 2026-10-16T15:30:00+00:00 | 1 |
| CAT | updated | 2026-10-16T15:52:00.417305+00:00 | 2026-10-16T15:30:00+00:00 | 1 |
| WMT | updated | 2026-10-16T15:52:00.417305+00:00 | 2026-10-16T15:30:00+00:00 | 1 |

이번 실행 소요: 43.15초
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
| v1 | buy_hold | 9921.95 | -78.05 | buy /  / buy_hold: prior completed bar target 100%; next bar open simulation |
| v1 | trend_8_26 | 9921.95 | -78.05 | buy /  / trend_8_26: prior completed bar target 100%; next bar open simulation |
| v1 | momentum_26 | 9916.54 | -83.46 | sell /  / momentum_26: prior completed bar target 0%; next bar open simulation |
| v1 | breakout_8 | 10000.00 | 0.00 | 대기 /  / 새 신호 대기 |
| v1 | reversion_12 | 9965.51 | -34.49 | buy /  / reversion_12: prior completed bar target 100%; next bar open simulation |
| v1 | volume_26 | 9945.10 | -54.90 | buy /  / volume_26: prior completed bar target 100%; next bar open simulation |
| v1 | trend_8_26 AND momentum_26 | 9916.54 | -83.46 | sell /  / trend_8_26 AND momentum_26: prior completed bar target 0%; next bar open simulation |
| v1 | trend_8_26 + momentum_26 | 9919.24 | -80.76 | sell /  / trend_8_26 + momentum_26: prior completed bar target 50%; next bar open simulation |
| v1 | trend_8_26 AND breakout_8 | 10000.00 | 0.00 | 대기 /  / 새 신호 대기 |
| v1 | trend_8_26 + breakout_8 | 9960.85 | -39.15 | buy /  / trend_8_26 + breakout_8: prior completed bar target 50%; next bar open simulation |
| v1 | trend_8_26 AND reversion_12 | 9965.51 | -34.49 | buy /  / trend_8_26 AND reversion_12: prior completed bar target 100%; next bar open simulation |
| v1 | trend_8_26 + reversion_12 | 9943.67 | -56.33 | buy /  / trend_8_26 + reversion_12: prior completed bar target 100%; next bar open simulation |
| v1 | trend_8_26 AND volume_26 | 9945.10 | -54.90 | buy /  / trend_8_26 AND volume_26: prior completed bar target 100%; next bar open simulation |
| v1 | trend_8_26 + volume_26 | 9933.49 | -66.51 | buy /  / trend_8_26 + volume_26: prior completed bar target 100%; next bar open simulation |
| v1 | momentum_26 AND breakout_8 | 10000.00 | 0.00 | 대기 /  / 새 신호 대기 |
| v1 | momentum_26 + breakout_8 | 9958.17 | -41.83 | sell /  / momentum_26 + breakout_8: prior completed bar target 0%; next bar open simulation |
| v1 | momentum_26 AND reversion_12 | 10000.00 | 0.00 | 대기 /  / 새 신호 대기 |
| v1 | momentum_26 + reversion_12 | 9960.85 | -39.15 | buy /  / momentum_26 + reversion_12: prior completed bar target 50%; next bar open simulation |
| v1 | momentum_26 AND volume_26 | 9939.68 | -60.32 | sell /  / momentum_26 AND volume_26: prior completed bar target 0%; next bar open simulation |
| v1 | momentum_26 + volume_26 | 9930.78 | -69.22 | sell /  / momentum_26 + volume_26: prior completed bar target 50%; next bar open simulation |
| v1 | breakout_8 AND reversion_12 | 10000.00 | 0.00 | 대기 /  / 새 신호 대기 |
| v1 | breakout_8 + reversion_12 | 9982.72 | -17.28 | sell /  / breakout_8 + reversion_12: prior completed bar target 50%; next bar open simulation |
| v1 | breakout_8 AND volume_26 | 10000.00 | 0.00 | 대기 /  / 새 신호 대기 |
| v1 | breakout_8 + volume_26 | 9972.49 | -27.51 | buy /  / breakout_8 + volume_26: prior completed bar target 50%; next bar open simulation |
| v1 | reversion_12 AND volume_26 | 9965.51 | -34.49 | buy /  / reversion_12 AND volume_26: prior completed bar target 100%; next bar open simulation |
| v1 | reversion_12 + volume_26 | 9955.29 | -44.71 | buy /  / reversion_12 + volume_26: prior completed bar target 100%; next bar open simulation |
| v1 | ema_12_26 | 9921.95 | -78.05 | buy /  / EMA12 > EMA26; 조건 충족; EMA12=771.059, EMA26=770.546 |
| v1 | macd_12_26_9 | 9916.54 | -83.46 | sell /  / MACD > 신호선 그리고 MACD > 0; 조건 미충족; MACD=0.273669, signal9=0.379179 |
| v1 | rsi_14_recovery | 10000.00 | 0.00 | 대기 /  / 새 신호 대기 |
| v1 | bollinger_20_reentry | 10000.00 | 0.00 | 대기 /  / 새 신호 대기 |
| v1 | donchian_20 | 10000.00 | 0.00 | 대기 /  / 새 신호 대기 |
| v1 | atr_14_breakout | 10000.00 | 0.00 | 대기 /  / 새 신호 대기 |
| v1 | session_vwap | 9891.58 | -108.42 | sell /  / 종가 > 뉴욕 거래일별 누적 전형가격 VWAP; 조건 미충족; close=771.41, session_VWAP=771.735, session_volume=1.75958e+07 |
| v1 | obv_20 | 9931.74 | -68.26 | sell /  / OBV > OBV의 SMA20 그리고 종가 > EMA26; 조건 미충족; OBV=-708839, OBV_SMA20=2.15302e+06, close=771.03, EMA26=770.746 |
| v1 | stochastic_14_3_recovery | 10000.00 | 0.00 | 대기 /  / 새 신호 대기 |
| v1 | mfi_14_recovery | 10000.00 | 0.00 | 대기 /  / 새 신호 대기 |
| v1 | adx_14_trend | 10000.00 | 0.00 | 대기 /  / 새 신호 대기 |
| v1 | aroon_25_trend | 9902.37 | -97.63 | sell /  / Aroon25 Up > 70 그리고 Down < 30 (동률이면 최신 극값); 조건 미충족; Aroon_up=72, Aroon_down=100 |
| v1 | cci_20_momentum | 9936.89 | -63.11 | sell /  / CCI20 > 100 (전형가격·평균절대편차); 조건 미충족; CCI20=66.0792 |
| v1 | williams_14_recovery | 10000.00 | 0.00 | 대기 /  / 새 신호 대기 |
| v1 | cmf_20_accumulation | 9929.81 | -70.19 | sell /  / Chaikin Money Flow20 > 0.1; 조건 미충족; CMF20=-0.158867, volume20=2.42577e+07 |
| v1 | chaikin_3_10 | 9946.30 | -53.70 | sell /  / ADL의 EMA3 - EMA10 > 0 그리고 종가 > EMA26; 조건 미충족; Chaikin3_10=-174742, ADL=3.14745e+07, close=772.2, EMA26=770.668 |
| v1 | roc_10_momentum | 10000.00 | 0.00 | 대기 /  / 새 신호 대기 |
| v1 | trix_15_trend | 9916.54 | -83.46 | sell /  / 15봉 삼중 EMA의 1봉 변화율 TRIX > 0 그리고 종가 > EMA26; 조건 미충족; TRIX15_percent=0.00866315, close=769.855, EMA26=770.806 |
| v1 | keltner_20_breakout | 10000.00 | 0.00 | 대기 /  / 새 신호 대기 |
| v1 | opening_range_30m | 9946.30 | -53.70 | sell /  / 뉴욕 09:30·09:45 두 완료 봉 최고가를 10:00 이후 종가가 돌파; 자료 부족·변동폭 또는 거래량 없음: 대기; close=772.2 |
| v2 | cash | 10000.00 | 0.00 | 대기 /  / 새 신호 대기 |
| v2 | buy_hold | 9850.38 | -149.62 | buy / partial / 직전 완료 봉 목표 비중 100%; 다음 봉 시가 가정 |
| v2 | trend_8_26 | 9806.36 | -193.64 | buy / partial / 직전 완료 봉 목표 비중 100%; 다음 봉 시가 가정 |
| v2 | momentum_26 | 9770.62 | -229.38 | sell / filled / 직전 완료 봉 목표 비중 0%; 다음 봉 시가 가정 |
| v2 | breakout_8 | 9598.61 | -401.39 | sell / filled / 직전 완료 봉 목표 비중 0%; 다음 봉 시가 가정 |
| v2 | reversion_12 | 9502.00 | -498.00 | buy / partial / 직전 완료 봉 목표 비중 100%; 다음 봉 시가 가정 |
| v2 | volume_26 | 9388.68 | -611.32 | buy / partial / 직전 완료 봉 목표 비중 100%; 다음 봉 시가 가정 |
| v2 | trend_8_26 AND momentum_26 | 9777.28 | -222.72 | sell / filled / 직전 완료 봉 목표 비중 0%; 다음 봉 시가 가정 |
| v2 | trend_8_26 + momentum_26 | 9788.49 | -211.51 | sell / filled / 직전 완료 봉 목표 비중 50%; 다음 봉 시가 가정 |
| v2 | trend_8_26 AND breakout_8 | 9825.21 | -174.79 | sell / filled / 직전 완료 봉 목표 비중 0%; 다음 봉 시가 가정 |
| v2 | trend_8_26 + breakout_8 | 9701.77 | -298.23 | buy / filled / 직전 완료 봉 목표 비중 50%; 다음 봉 시가 가정 |
| v2 | trend_8_26 AND reversion_12 | 9861.00 | -139.00 | buy / partial / 직전 완료 봉 목표 비중 100%; 다음 봉 시가 가정 |
| v2 | trend_8_26 + reversion_12 | 9652.64 | -347.36 | buy / partial / 직전 완료 봉 목표 비중 100%; 다음 봉 시가 가정 |
| v2 | trend_8_26 AND volume_26 | 9790.88 | -209.12 | buy / partial / 직전 완료 봉 목표 비중 100%; 다음 봉 시가 가정 |
| v2 | trend_8_26 + volume_26 | 9615.16 | -384.84 | buy / partial / 직전 완료 봉 목표 비중 100%; 다음 봉 시가 가정 |
| v2 | momentum_26 AND breakout_8 | 9783.53 | -216.47 | sell / filled / 직전 완료 봉 목표 비중 0%; 다음 봉 시가 가정 |
| v2 | momentum_26 + breakout_8 | 9684.14 | -315.86 | sell / filled / 직전 완료 봉 목표 비중 0%; 다음 봉 시가 가정 |
| v2 | momentum_26 AND reversion_12 | 9963.21 | -36.79 | sell / filled / 직전 완료 봉 목표 비중 0%; 다음 봉 시가 가정 |
| v2 | momentum_26 + reversion_12 | 9675.59 | -324.41 | buy / filled / 직전 완료 봉 목표 비중 50%; 다음 봉 시가 가정 |
| v2 | momentum_26 AND volume_26 | 9855.46 | -144.54 | sell / filled / 직전 완료 봉 목표 비중 0%; 다음 봉 시가 가정 |
| v2 | momentum_26 + volume_26 | 9637.99 | -362.01 | sell / filled / 직전 완료 봉 목표 비중 50%; 다음 봉 시가 가정 |
| v2 | breakout_8 AND reversion_12 | 10000.00 | 0.00 | 대기 /  / 새 신호 대기 |
| v2 | breakout_8 + reversion_12 | 9589.94 | -410.06 | sell / filled / 직전 완료 봉 목표 비중 50%; 다음 봉 시가 가정 |
| v2 | breakout_8 AND volume_26 | 9933.18 | -66.82 | sell / filled / 직전 완료 봉 목표 비중 0%; 다음 봉 시가 가정 |
| v2 | breakout_8 + volume_26 | 9532.64 | -467.36 | buy / filled / 직전 완료 봉 목표 비중 50%; 다음 봉 시가 가정 |
| v2 | reversion_12 AND volume_26 | 9708.76 | -291.24 | buy / partial / 직전 완료 봉 목표 비중 100%; 다음 봉 시가 가정 |
| v2 | reversion_12 + volume_26 | 9524.57 | -475.43 | buy / partial / 직전 완료 봉 목표 비중 100%; 다음 봉 시가 가정 |
| v2 | ema_12_26 | 9920.96 | -79.04 | buy / partial / EMA12 > EMA26; 조건 충족; EMA12=771.059, EMA26=770.546; 직전 완료 봉 목표를 다음 봉 시가에 모의 적용 |
| v2 | macd_12_26_9 | 9914.56 | -85.44 | sell / filled / MACD > 신호선 그리고 MACD > 0; 조건 미충족; MACD=0.273669, signal9=0.379179; 직전 완료 봉 목표를 다음 봉 시가에 모의 적용 |
| v2 | rsi_14_recovery | 10000.00 | 0.00 | 대기 /  / 새 신호 대기 |
| v2 | bollinger_20_reentry | 10000.00 | 0.00 | 대기 /  / 새 신호 대기 |
| v2 | donchian_20 | 10000.00 | 0.00 | 대기 /  / 새 신호 대기 |
| v2 | atr_14_breakout | 10000.00 | 0.00 | 대기 /  / 새 신호 대기 |
| v2 | session_vwap | 9887.63 | -112.37 | sell / filled / 종가 > 뉴욕 거래일별 누적 전형가격 VWAP; 조건 미충족; close=771.41, session_VWAP=771.735, session_volume=1.75958e+07; 직전 완료 봉 목표를 다음 봉 시가에 모의 적용 |
| v2 | obv_20 | 9929.76 | -70.24 | sell / filled / OBV > OBV의 SMA20 그리고 종가 > EMA26; 조건 미충족; OBV=-708839, OBV_SMA20=2.15302e+06, close=771.03, EMA26=770.746; 직전 완료 봉 목표를 다음 봉 시가에 모의 적용 |
| v2 | stochastic_14_3_recovery | 10000.00 | 0.00 | 대기 /  / 새 신호 대기 |
| v2 | mfi_14_recovery | 10000.00 | 0.00 | 대기 /  / 새 신호 대기 |
| v2 | adx_14_trend | 10000.00 | 0.00 | 대기 /  / 새 신호 대기 |
| v2 | aroon_25_trend | 9900.39 | -99.61 | sell / filled / Aroon25 Up > 70 그리고 Down < 30 (동률이면 최신 극값); 조건 미충족; Aroon_up=72, Aroon_down=100; 직전 완료 봉 목표를 다음 봉 시가에 모의 적용 |
| v2 | cci_20_momentum | 9934.91 | -65.09 | sell / filled / CCI20 > 100 (전형가격·평균절대편차); 조건 미충족; CCI20=66.0792; 직전 완료 봉 목표를 다음 봉 시가에 모의 적용 |
| v2 | williams_14_recovery | 10000.00 | 0.00 | 대기 /  / 새 신호 대기 |
| v2 | cmf_20_accumulation | 9927.82 | -72.18 | sell / filled / Chaikin Money Flow20 > 0.1; 조건 미충족; CMF20=-0.158867, volume20=2.42577e+07; 직전 완료 봉 목표를 다음 봉 시가에 모의 적용 |
| v2 | chaikin_3_10 | 9944.31 | -55.69 | sell / filled / ADL의 EMA3 - EMA10 > 0 그리고 종가 > EMA26; 조건 미충족; Chaikin3_10=-174742, ADL=3.14745e+07, close=772.2, EMA26=770.668; 직전 완료 봉 목표를 다음 봉 시가에 모의 적용 |
| v2 | roc_10_momentum | 10000.00 | 0.00 | 대기 /  / 새 신호 대기 |
| v2 | trix_15_trend | 9914.56 | -85.44 | sell / filled / 15봉 삼중 EMA의 1봉 변화율 TRIX > 0 그리고 종가 > EMA26; 조건 미충족; TRIX15_percent=0.00866315, close=769.855, EMA26=770.806; 직전 완료 봉 목표를 다음 봉 시가에 모의 적용 |
| v2 | keltner_20_breakout | 10000.00 | 0.00 | 대기 /  / 새 신호 대기 |
| v2 | opening_range_30m | 9944.31 | -55.69 | sell / filled / 뉴욕 09:30·09:45 두 완료 봉 최고가를 10:00 이후 종가가 돌파; 자료 부족·변동폭 또는 거래량 없음: 대기; close=772.2; 직전 완료 봉 목표를 다음 봉 시가에 모의 적용 |

### 같은 기간의 비용·노출 비교 (사후 연구)

| 전략 | 비용 전 | 비용 후 | 100% 보유 | 같은 평균 노출 보유 | 평균 노출 |
|---|---:|---:|---:|---:|---:|
| cash | 0.00% | 0.00% | -0.70% | -0.00% | 0.00% |
| buy_hold | -0.28% | -0.70% | -0.70% | -0.70% | 100.00% |
| trend_8_26 | 0.96% | -2.38% | -0.70% | -0.34% | 49.08% |
| momentum_26 | -0.83% | -5.31% | -0.70% | -0.34% | 48.28% |
| breakout_8 | -0.61% | -15.63% | -0.70% | -0.15% | 21.37% |
| reversion_12 | -2.00% | -13.24% | -0.70% | -0.20% | 28.50% |
| volume_26 | -0.95% | -9.69% | -0.70% | -0.06% | 8.97% |
| trend_8_26 AND momentum_26 | 0.49% | -3.24% | -0.70% | -0.29% | 41.95% |
| trend_8_26 + momentum_26 | 0.06% | -3.65% | -0.70% | -0.34% | 48.68% |
| trend_8_26 AND breakout_8 | 0.07% | -10.28% | -0.70% | -0.09% | 12.40% |
| trend_8_26 + breakout_8 | 0.17% | -9.24% | -0.70% | -0.25% | 35.23% |
| trend_8_26 AND reversion_12 | -0.04% | -4.56% | -0.70% | -0.05% | 6.60% |
| trend_8_26 + reversion_12 | -0.53% | -7.78% | -0.70% | -0.27% | 38.79% |
| trend_8_26 AND volume_26 | -0.58% | -4.67% | -0.70% | -0.03% | 4.22% |
| trend_8_26 + volume_26 | 0.00% | -6.11% | -0.70% | -0.20% | 29.03% |
| momentum_26 AND breakout_8 | 0.37% | -10.01% | -0.70% | -0.09% | 13.46% |
| momentum_26 + breakout_8 | -0.72% | -10.62% | -0.70% | -0.24% | 34.84% |
| momentum_26 AND reversion_12 | -0.88% | -5.75% | -0.70% | -0.05% | 6.86% |
| momentum_26 + reversion_12 | -1.42% | -8.60% | -0.70% | -0.27% | 38.40% |
| momentum_26 AND volume_26 | -0.39% | -3.27% | -0.70% | -0.01% | 2.11% |
| momentum_26 + volume_26 | -0.89% | -6.36% | -0.70% | -0.20% | 28.63% |
| breakout_8 AND reversion_12 | 0.00% | 0.00% | -0.70% | -0.00% | 0.00% |
| breakout_8 + reversion_12 | -1.30% | -13.91% | -0.70% | -0.17% | 24.94% |
| breakout_8 AND volume_26 | 0.09% | -1.17% | -0.70% | -0.01% | 1.06% |
| breakout_8 + volume_26 | -0.78% | -11.80% | -0.70% | -0.11% | 15.18% |
| reversion_12 AND volume_26 | -0.82% | -5.29% | -0.70% | -0.03% | 4.49% |
| reversion_12 + volume_26 | -1.47% | -11.12% | -0.70% | -0.13% | 18.74% |
| ema_12_26 | -0.64% | -3.93% | -0.70% | -0.35% | 49.87% |
| macd_12_26_9 | 0.44% | -4.09% | -0.70% | -0.21% | 29.55% |
| rsi_14_recovery | -0.33% | -3.62% | -0.70% | -0.01% | 2.11% |
| bollinger_20_reentry | -0.82% | -6.49% | -0.70% | -0.03% | 3.69% |
| donchian_20 | 0.11% | -6.79% | -0.70% | -0.05% | 6.60% |
| atr_14_breakout | -0.04% | -5.35% | -0.70% | -0.03% | 3.96% |
| session_vwap | 1.20% | -8.89% | -0.70% | -0.36% | 51.45% |
| obv_20 | -0.81% | -9.18% | -0.70% | -0.27% | 38.52% |
| stochastic_14_3_recovery | -0.99% | -15.24% | -0.70% | -0.07% | 9.76% |
| mfi_14_recovery | -0.01% | -2.50% | -0.70% | -0.01% | 1.58% |
| adx_14_trend | -0.10% | -3.81% | -0.70% | -0.20% | 27.97% |
| aroon_25_trend | 0.72% | -2.20% | -0.70% | -0.18% | 26.39% |
| cci_20_momentum | -0.18% | -7.84% | -0.70% | -0.15% | 21.11% |
| williams_14_recovery | -0.88% | -10.76% | -0.70% | -0.05% | 6.60% |
| cmf_20_accumulation | 1.72% | -2.46% | -0.70% | -0.33% | 47.23% |
| chaikin_3_10 | 1.29% | -5.29% | -0.70% | -0.28% | 40.63% |
| roc_10_momentum | -0.06% | -0.48% | -0.70% | -0.01% | 0.79% |
| trix_15_trend | -0.53% | -3.41% | -0.70% | -0.26% | 37.73% |
| keltner_20_breakout | 0.09% | -3.62% | -0.70% | -0.08% | 10.82% |
| opening_range_30m | -0.32% | -6.41% | -0.70% | -0.22% | 31.66% |

동일 구간·초기 자금, 종료 시 청산 비용 포함. 노출 맞춤은 사후 설명용이며 v2 실제 계좌 성과가 아닙니다.
[낙폭 분해·비용 영향·전체 구간](SPY/comparison.json)

[v1 전체 기록](SPY/accounts.json) · [v2 전체 기록](SPY/accounts-v2.json)

## QQQ 계좌

| 모델 | 전략 | 평가액 USD | 손익 USD | 최근 매매·이유 |
|---|---|---:|---:|---|
| v1 | cash | 10000.00 | 0.00 | 대기 /  / 새 신호 대기 |
| v1 | buy_hold | 9878.36 | -121.64 | buy /  / buy_hold: prior completed bar target 100%; next bar open simulation |
| v1 | trend_8_26 | 9922.86 | -77.14 | sell /  / trend_8_26: prior completed bar target 0%; next bar open simulation |
| v1 | momentum_26 | 9935.02 | -64.98 | sell /  / momentum_26: prior completed bar target 0%; next bar open simulation |
| v1 | breakout_8 | 10000.00 | 0.00 | 대기 /  / 새 신호 대기 |
| v1 | reversion_12 | 9933.67 | -66.33 | buy /  / reversion_12: prior completed bar target 100%; next bar open simulation |
| v1 | volume_26 | 10000.00 | 0.00 | 대기 /  / 새 신호 대기 |
| v1 | trend_8_26 AND momentum_26 | 9951.96 | -48.04 | sell /  / trend_8_26 AND momentum_26: prior completed bar target 0%; next bar open simulation |
| v1 | trend_8_26 + momentum_26 | 9928.92 | -71.08 | sell /  / trend_8_26 + momentum_26: prior completed bar target 0%; next bar open simulation |
| v1 | trend_8_26 AND breakout_8 | 10000.00 | 0.00 | 대기 /  / 새 신호 대기 |
| v1 | trend_8_26 + breakout_8 | 9961.32 | -38.68 | sell /  / trend_8_26 + breakout_8: prior completed bar target 0%; next bar open simulation |
| v1 | trend_8_26 AND reversion_12 | 9951.96 | -48.04 | sell /  / trend_8_26 AND reversion_12: prior completed bar target 0%; next bar open simulation |
| v1 | trend_8_26 + reversion_12 | 9928.23 | -71.77 | sell /  / trend_8_26 + reversion_12: prior completed bar target 50%; next bar open simulation |
| v1 | trend_8_26 AND volume_26 | 10000.00 | 0.00 | 대기 /  / 새 신호 대기 |
| v1 | trend_8_26 + volume_26 | 9961.32 | -38.68 | sell /  / trend_8_26 + volume_26: prior completed bar target 0%; next bar open simulation |
| v1 | momentum_26 AND breakout_8 | 10000.00 | 0.00 | 대기 /  / 새 신호 대기 |
| v1 | momentum_26 + breakout_8 | 9967.44 | -32.56 | sell /  / momentum_26 + breakout_8: prior completed bar target 0%; next bar open simulation |
| v1 | momentum_26 AND reversion_12 | 9951.96 | -48.04 | sell /  / momentum_26 AND reversion_12: prior completed bar target 0%; next bar open simulation |
| v1 | momentum_26 + reversion_12 | 9934.33 | -65.67 | sell /  / momentum_26 + reversion_12: prior completed bar target 50%; next bar open simulation |
| v1 | momentum_26 AND volume_26 | 10000.00 | 0.00 | 대기 /  / 새 신호 대기 |
| v1 | momentum_26 + volume_26 | 9967.44 | -32.56 | sell /  / momentum_26 + volume_26: prior completed bar target 0%; next bar open simulation |
| v1 | breakout_8 AND reversion_12 | 10000.00 | 0.00 | 대기 /  / 새 신호 대기 |
| v1 | breakout_8 + reversion_12 | 9966.73 | -33.27 | sell /  / breakout_8 + reversion_12: prior completed bar target 50%; next bar open simulation |
| v1 | breakout_8 AND volume_26 | 10000.00 | 0.00 | 대기 /  / 새 신호 대기 |
| v1 | breakout_8 + volume_26 | 10000.00 | 0.00 | 대기 /  / 새 신호 대기 |
| v1 | reversion_12 AND volume_26 | 10000.00 | 0.00 | 대기 /  / 새 신호 대기 |
| v1 | reversion_12 + volume_26 | 9966.73 | -33.27 | sell /  / reversion_12 + volume_26: prior completed bar target 50%; next bar open simulation |
| v1 | ema_12_26 | 9930.96 | -69.04 | sell /  / EMA12 > EMA26; 조건 미충족; EMA12=725.847, EMA26=725.955 |
| v1 | macd_12_26_9 | 9930.96 | -69.04 | sell /  / MACD > 신호선 그리고 MACD > 0; 조건 미충족; MACD=-0.108239, signal9=-0.536871 |
| v1 | rsi_14_recovery | 10000.00 | 0.00 | 대기 /  / 새 신호 대기 |
| v1 | bollinger_20_reentry | 9942.83 | -57.17 | sell /  / 직전 종가 < 직전 하단밴드, 현재 하단밴드 <= 종가 <= SMA20 (한 봉 목표); 조건 미충족; close=720.44, lower20=720.08, SMA20=724.588, previous_lower20=720.727 |
| v1 | donchian_20 | 10000.00 | 0.00 | 대기 /  / 새 신호 대기 |
| v1 | atr_14_breakout | 10000.00 | 0.00 | 대기 /  / 새 신호 대기 |
| v1 | session_vwap | 9874.48 | -125.52 | sell /  / 종가 > 뉴욕 거래일별 누적 전형가격 VWAP; 조건 미충족; close=721.534, session_VWAP=721.817, session_volume=9.25052e+07 |
| v1 | obv_20 | 9930.96 | -69.04 | sell /  / OBV > OBV의 SMA20 그리고 종가 > EMA26; 조건 미충족; OBV=7.37006e+07, OBV_SMA20=7.17868e+07, close=723.36, EMA26=725.955 |
| v1 | stochastic_14_3_recovery | 9886.28 | -113.72 | sell /  / 직전 %K14 < 20에서 %K14가 %D3 상향 돌파 (한 봉 목표); 조건 미충족; K14=18.2594, D3=18.7499, previous_K14=31.056, previous_D3=19.1335 |
| v1 | mfi_14_recovery | 10000.00 | 0.00 | 대기 /  / 새 신호 대기 |
| v1 | adx_14_trend | 9930.96 | -69.04 | sell /  / Wilder ADX14 >= 25 그리고 +DI14 > -DI14; 조건 미충족; ADX14=26.4264, plus_DI14=23.7408, minus_DI14=36.7914 |
| v1 | aroon_25_trend | 9922.86 | -77.14 | sell /  / Aroon25 Up > 70 그리고 Down < 30 (동률이면 최신 극값); 조건 미충족; Aroon_up=80, Aroon_down=92 |
| v1 | cci_20_momentum | 9930.96 | -69.04 | sell /  / CCI20 > 100 (전형가격·평균절대편차); 조건 미충족; CCI20=-76.1363 |
| v1 | williams_14_recovery | 9943.13 | -56.87 | sell /  / 직전 Williams %R14 < -80, 현재 >= -80 (한 봉 목표); 조건 미충족; Williams_R14=-81.7406, previous_R14=-68.944 |
| v1 | cmf_20_accumulation | 9818.03 | -181.97 | sell /  / Chaikin Money Flow20 > 0.1; 조건 미충족; CMF20=0.0659721, volume20=2.62879e+08 |
| v1 | chaikin_3_10 | 9930.96 | -69.04 | sell /  / ADL의 EMA3 - EMA10 > 0 그리고 종가 > EMA26; 조건 미충족; Chaikin3_10=1.68527e+06, ADL=1.75875e+08, close=723.36, EMA26=725.955 |
| v1 | roc_10_momentum | 10000.00 | 0.00 | 대기 /  / 새 신호 대기 |
| v1 | trix_15_trend | 10000.00 | 0.00 | 대기 /  / 새 신호 대기 |
| v1 | keltner_20_breakout | 10000.00 | 0.00 | 대기 /  / 새 신호 대기 |
| v1 | opening_range_30m | 9930.96 | -69.04 | sell /  / 뉴욕 09:30·09:45 두 완료 봉 최고가를 10:00 이후 종가가 돌파; 자료 부족·변동폭 또는 거래량 없음: 대기; close=723.36 |
| v2 | cash | 10000.00 | 0.00 | 대기 /  / 새 신호 대기 |
| v2 | buy_hold | 9559.05 | -440.95 | buy / partial / 직전 완료 봉 목표 비중 100%; 다음 봉 시가 가정 |
| v2 | trend_8_26 | 9726.12 | -273.88 | sell / filled / 직전 완료 봉 목표 비중 0%; 다음 봉 시가 가정 |
| v2 | momentum_26 | 9831.49 | -168.51 | sell / filled / 직전 완료 봉 목표 비중 0%; 다음 봉 시가 가정 |
| v2 | breakout_8 | 9669.86 | -330.14 | sell / filled / 직전 완료 봉 목표 비중 0%; 다음 봉 시가 가정 |
| v2 | reversion_12 | 9449.88 | -550.12 | buy / partial / 직전 완료 봉 목표 비중 100%; 다음 봉 시가 가정 |
| v2 | volume_26 | 9565.80 | -434.20 | 중단: 손실 한도 / sell / filled / 직전 완료 봉 목표 비중 0%; 다음 봉 시가 가정 |
| v2 | trend_8_26 AND momentum_26 | 9848.25 | -151.75 | sell / filled / 직전 완료 봉 목표 비중 0%; 다음 봉 시가 가정 |
| v2 | trend_8_26 + momentum_26 | 9778.69 | -221.31 | sell / filled / 직전 완료 봉 목표 비중 0%; 다음 봉 시가 가정 |
| v2 | trend_8_26 AND breakout_8 | 9895.83 | -104.17 | sell / filled / 직전 완료 봉 목표 비중 0%; 다음 봉 시가 가정 |
| v2 | trend_8_26 + breakout_8 | 9697.89 | -302.11 | sell / filled / 직전 완료 봉 목표 비중 0%; 다음 봉 시가 가정 |
| v2 | trend_8_26 AND reversion_12 | 9811.80 | -188.20 | sell / filled / 직전 완료 봉 목표 비중 0%; 다음 봉 시가 가정 |
| v2 | trend_8_26 + reversion_12 | 9586.68 | -413.32 | sell / filled / 직전 완료 봉 목표 비중 50%; 다음 봉 시가 가정 |
| v2 | trend_8_26 AND volume_26 | 9840.10 | -159.90 | sell / filled / 직전 완료 봉 목표 비중 0%; 다음 봉 시가 가정 |
| v2 | trend_8_26 + volume_26 | 9565.02 | -434.98 | sell / filled / 직전 완료 봉 목표 비중 0%; 다음 봉 시가 가정 |
| v2 | momentum_26 AND breakout_8 | 9960.69 | -39.31 | sell / filled / 직전 완료 봉 목표 비중 0%; 다음 봉 시가 가정 |
| v2 | momentum_26 + breakout_8 | 9750.28 | -249.72 | sell / filled / 직전 완료 봉 목표 비중 0%; 다음 봉 시가 가정 |
| v2 | momentum_26 AND reversion_12 | 9949.97 | -50.03 | sell / filled / 직전 완료 봉 목표 비중 0%; 다음 봉 시가 가정 |
| v2 | momentum_26 + reversion_12 | 9658.72 | -341.28 | sell / filled / 직전 완료 봉 목표 비중 50%; 다음 봉 시가 가정 |
| v2 | momentum_26 AND volume_26 | 9936.83 | -63.17 | sell / filled / 직전 완료 봉 목표 비중 0%; 다음 봉 시가 가정 |
| v2 | momentum_26 + volume_26 | 9616.70 | -383.30 | sell / filled / 직전 완료 봉 목표 비중 0%; 다음 봉 시가 가정 |
| v2 | breakout_8 AND reversion_12 | 10000.00 | 0.00 | 대기 /  / 새 신호 대기 |
| v2 | breakout_8 + reversion_12 | 9619.31 | -380.69 | sell / filled / 직전 완료 봉 목표 비중 50%; 다음 봉 시가 가정 |
| v2 | breakout_8 AND volume_26 | 9947.98 | -52.02 | sell / filled / 직전 완료 봉 목표 비중 0%; 다음 봉 시가 가정 |
| v2 | breakout_8 + volume_26 | 9577.55 | -422.45 | sell / filled / 직전 완료 봉 목표 비중 0%; 다음 봉 시가 가정 |
| v2 | reversion_12 AND volume_26 | 9547.64 | -452.36 | 중단: 손실 한도 / sell / filled / 직전 완료 봉 목표 비중 0%; 다음 봉 시가 가정 |
| v2 | reversion_12 + volume_26 | 9448.17 | -551.83 | sell / filled / 직전 완료 봉 목표 비중 50%; 다음 봉 시가 가정 |
| v2 | ema_12_26 | 9928.97 | -71.03 | sell / filled / EMA12 > EMA26; 조건 미충족; EMA12=725.847, EMA26=725.955; 직전 완료 봉 목표를 다음 봉 시가에 모의 적용 |
| v2 | macd_12_26_9 | 9928.97 | -71.03 | sell / filled / MACD > 신호선 그리고 MACD > 0; 조건 미충족; MACD=-0.108239, signal9=-0.536871; 직전 완료 봉 목표를 다음 봉 시가에 모의 적용 |
| v2 | rsi_14_recovery | 10000.00 | 0.00 | 대기 /  / 새 신호 대기 |
| v2 | bollinger_20_reentry | 9940.84 | -59.16 | sell / filled / 직전 종가 < 직전 하단밴드, 현재 하단밴드 <= 종가 <= SMA20 (한 봉 목표); 조건 미충족; close=720.44, lower20=720.08, SMA20=724.588, previous_lower20=720.727; 직전 완료 봉 목표를 다음 봉 시가에 모의 적용 |
| v2 | donchian_20 | 10000.00 | 0.00 | 대기 /  / 새 신호 대기 |
| v2 | atr_14_breakout | 10000.00 | 0.00 | 대기 /  / 새 신호 대기 |
| v2 | session_vwap | 9870.53 | -129.47 | sell / filled / 종가 > 뉴욕 거래일별 누적 전형가격 VWAP; 조건 미충족; close=721.534, session_VWAP=721.817, session_volume=9.25052e+07; 직전 완료 봉 목표를 다음 봉 시가에 모의 적용 |
| v2 | obv_20 | 9928.97 | -71.03 | sell / filled / OBV > OBV의 SMA20 그리고 종가 > EMA26; 조건 미충족; OBV=7.37006e+07, OBV_SMA20=7.17868e+07, close=723.36, EMA26=725.955; 직전 완료 봉 목표를 다음 봉 시가에 모의 적용 |
| v2 | stochastic_14_3_recovery | 9882.33 | -117.67 | sell / filled / 직전 %K14 < 20에서 %K14가 %D3 상향 돌파 (한 봉 목표); 조건 미충족; K14=18.2594, D3=18.7499, previous_K14=31.056, previous_D3=19.1335; 직전 완료 봉 목표를 다음 봉 시가에 모의 적용 |
| v2 | mfi_14_recovery | 10000.00 | 0.00 | 대기 /  / 새 신호 대기 |
| v2 | adx_14_trend | 9928.97 | -71.03 | sell / filled / Wilder ADX14 >= 25 그리고 +DI14 > -DI14; 조건 미충족; ADX14=26.4264, plus_DI14=23.7408, minus_DI14=36.7914; 직전 완료 봉 목표를 다음 봉 시가에 모의 적용 |
| v2 | aroon_25_trend | 9920.88 | -79.12 | sell / filled / Aroon25 Up > 70 그리고 Down < 30 (동률이면 최신 극값); 조건 미충족; Aroon_up=80, Aroon_down=92; 직전 완료 봉 목표를 다음 봉 시가에 모의 적용 |
| v2 | cci_20_momentum | 9928.97 | -71.03 | sell / filled / CCI20 > 100 (전형가격·평균절대편차); 조건 미충족; CCI20=-76.1363; 직전 완료 봉 목표를 다음 봉 시가에 모의 적용 |
| v2 | williams_14_recovery | 9941.14 | -58.86 | sell / filled / 직전 Williams %R14 < -80, 현재 >= -80 (한 봉 목표); 조건 미충족; Williams_R14=-81.7406, previous_R14=-68.944; 직전 완료 봉 목표를 다음 봉 시가에 모의 적용 |
| v2 | cmf_20_accumulation | 9812.14 | -187.86 | sell / filled / Chaikin Money Flow20 > 0.1; 조건 미충족; CMF20=0.0659721, volume20=2.62879e+08; 직전 완료 봉 목표를 다음 봉 시가에 모의 적용 |
| v2 | chaikin_3_10 | 9928.97 | -71.03 | sell / filled / ADL의 EMA3 - EMA10 > 0 그리고 종가 > EMA26; 조건 미충족; Chaikin3_10=1.68527e+06, ADL=1.75875e+08, close=723.36, EMA26=725.955; 직전 완료 봉 목표를 다음 봉 시가에 모의 적용 |
| v2 | roc_10_momentum | 10000.00 | 0.00 | 대기 /  / 새 신호 대기 |
| v2 | trix_15_trend | 10000.00 | 0.00 | 대기 /  / 새 신호 대기 |
| v2 | keltner_20_breakout | 10000.00 | 0.00 | 대기 /  / 새 신호 대기 |
| v2 | opening_range_30m | 9928.97 | -71.03 | sell / filled / 뉴욕 09:30·09:45 두 완료 봉 최고가를 10:00 이후 종가가 돌파; 자료 부족·변동폭 또는 거래량 없음: 대기; close=723.36; 직전 완료 봉 목표를 다음 봉 시가에 모의 적용 |

### 같은 기간의 비용·노출 비교 (사후 연구)

| 전략 | 비용 전 | 비용 후 | 100% 보유 | 같은 평균 노출 보유 | 평균 노출 |
|---|---:|---:|---:|---:|---:|
| cash | 0.00% | 0.00% | -3.96% | -0.00% | 0.00% |
| buy_hold | -3.55% | -3.96% | -3.96% | -3.96% | 100.00% |
| trend_8_26 | -0.37% | -4.07% | -3.96% | -1.82% | 45.91% |
| momentum_26 | -1.64% | -6.48% | -3.96% | -1.57% | 39.58% |
| breakout_8 | -1.46% | -16.35% | -3.96% | -0.70% | 17.68% |
| reversion_12 | -0.92% | -13.74% | -3.96% | -1.12% | 28.23% |
| volume_26 | -1.07% | -13.51% | -3.96% | -0.57% | 14.25% |
| trend_8_26 AND momentum_26 | -0.51% | -4.60% | -3.96% | -1.38% | 34.83% |
| trend_8_26 + momentum_26 | -1.00% | -5.08% | -3.96% | -1.69% | 42.75% |
| trend_8_26 AND breakout_8 | -0.32% | -9.11% | -3.96% | -0.42% | 10.55% |
| trend_8_26 + breakout_8 | -0.91% | -10.04% | -3.96% | -1.26% | 31.80% |
| trend_8_26 AND reversion_12 | 0.34% | -5.79% | -3.96% | -0.28% | 7.12% |
| trend_8_26 + reversion_12 | -0.64% | -8.47% | -3.96% | -1.47% | 37.08% |
| trend_8_26 AND volume_26 | -0.71% | -5.59% | -3.96% | -0.17% | 4.22% |
| trend_8_26 + volume_26 | -0.72% | -8.73% | -3.96% | -1.19% | 30.08% |
| momentum_26 AND breakout_8 | -0.13% | -8.56% | -3.96% | -0.41% | 10.29% |
| momentum_26 + breakout_8 | -1.55% | -11.37% | -3.96% | -1.14% | 28.63% |
| momentum_26 AND reversion_12 | -0.10% | -6.20% | -3.96% | -0.23% | 5.80% |
| momentum_26 + reversion_12 | -1.28% | -9.62% | -3.96% | -1.34% | 33.91% |
| momentum_26 AND volume_26 | -0.30% | -4.40% | -3.96% | -0.14% | 3.43% |
| momentum_26 + volume_26 | -1.35% | -9.88% | -3.96% | -1.07% | 26.92% |
| breakout_8 AND reversion_12 | 0.00% | 0.00% | -3.96% | -0.00% | 0.00% |
| breakout_8 + reversion_12 | -1.19% | -14.17% | -3.96% | -0.91% | 22.96% |
| breakout_8 AND volume_26 | 0.04% | -2.04% | -3.96% | -0.05% | 1.32% |
| breakout_8 + volume_26 | -1.27% | -13.69% | -3.96% | -0.63% | 15.97% |
| reversion_12 AND volume_26 | -1.25% | -8.44% | -3.96% | -0.35% | 8.71% |
| reversion_12 + volume_26 | -0.99% | -13.27% | -3.96% | -0.84% | 21.25% |
| ema_12_26 | 0.16% | -1.92% | -3.96% | -1.47% | 37.20% |
| macd_12_26_9 | 1.49% | -1.86% | -3.96% | -0.81% | 20.32% |
| rsi_14_recovery | -0.50% | -4.99% | -3.96% | -0.12% | 2.90% |
| bollinger_20_reentry | -0.19% | -5.89% | -3.96% | -0.15% | 3.69% |
| donchian_20 | 0.28% | -4.24% | -3.96% | -0.19% | 4.75% |
| atr_14_breakout | -0.26% | -4.76% | -3.96% | -0.13% | 3.17% |
| session_vwap | -1.31% | -12.63% | -3.96% | -2.08% | 52.51% |
| obv_20 | -1.88% | -10.91% | -3.96% | -1.08% | 27.18% |
| stochastic_14_3_recovery | -0.24% | -10.93% | -3.96% | -0.28% | 7.12% |
| mfi_14_recovery | -0.16% | -1.82% | -3.96% | -0.04% | 1.06% |
| adx_14_trend | -0.71% | -3.59% | -3.96% | -0.74% | 18.73% |
| aroon_25_trend | 1.40% | -1.95% | -3.96% | -0.78% | 19.79% |
| cci_20_momentum | -0.85% | -5.72% | -3.96% | -0.60% | 15.04% |
| williams_14_recovery | -0.68% | -10.95% | -3.96% | -0.27% | 6.86% |
| cmf_20_accumulation | -2.09% | -10.35% | -3.96% | -1.29% | 32.45% |
| chaikin_3_10 | -3.05% | -11.23% | -3.96% | -1.40% | 35.36% |
| roc_10_momentum | -0.31% | -1.56% | -3.96% | -0.08% | 2.11% |
| trix_15_trend | 0.04% | -1.63% | -3.96% | -1.23% | 31.13% |
| keltner_20_breakout | -0.73% | -4.81% | -3.96% | -0.29% | 7.39% |
| opening_range_30m | -0.35% | -6.04% | -3.96% | -0.87% | 21.90% |

동일 구간·초기 자금, 종료 시 청산 비용 포함. 노출 맞춤은 사후 설명용이며 v2 실제 계좌 성과가 아닙니다.
[낙폭 분해·비용 영향·전체 구간](QQQ/comparison.json)

[v1 전체 기록](QQQ/accounts.json) · [v2 전체 기록](QQQ/accounts-v2.json)

## IWM 계좌

| 모델 | 전략 | 평가액 USD | 손익 USD | 최근 매매·이유 |
|---|---|---:|---:|---|
| v1 | cash | 10000.00 | 0.00 | 대기 /  / 새 신호 대기 |
| v1 | buy_hold | 9881.87 | -118.13 | buy /  / buy_hold: prior completed bar target 100%; next bar open simulation |
| v1 | trend_8_26 | 9881.87 | -118.13 | buy /  / trend_8_26: prior completed bar target 100%; next bar open simulation |
| v1 | momentum_26 | 9895.73 | -104.27 | sell /  / momentum_26: prior completed bar target 0%; next bar open simulation |
| v1 | breakout_8 | 9929.38 | -70.62 | sell /  / breakout_8: prior completed bar target 0%; next bar open simulation |
| v1 | reversion_12 | 9946.13 | -53.87 | buy /  / reversion_12: prior completed bar target 100%; next bar open simulation |
| v1 | volume_26 | 10000.00 | 0.00 | 대기 /  / 새 신호 대기 |
| v1 | trend_8_26 AND momentum_26 | 9895.73 | -104.27 | sell /  / trend_8_26 AND momentum_26: prior completed bar target 0%; next bar open simulation |
| v1 | trend_8_26 + momentum_26 | 9888.80 | -111.20 | sell /  / trend_8_26 + momentum_26: prior completed bar target 50%; next bar open simulation |
| v1 | trend_8_26 AND breakout_8 | 9929.38 | -70.62 | sell /  / trend_8_26 AND breakout_8: prior completed bar target 0%; next bar open simulation |
| v1 | trend_8_26 + breakout_8 | 9905.59 | -94.41 | buy /  / trend_8_26 + breakout_8: prior completed bar target 50%; next bar open simulation |
| v1 | trend_8_26 AND reversion_12 | 9946.13 | -53.87 | buy /  / trend_8_26 AND reversion_12: prior completed bar target 100%; next bar open simulation |
| v1 | trend_8_26 + reversion_12 | 9913.91 | -86.09 | buy /  / trend_8_26 + reversion_12: prior completed bar target 100%; next bar open simulation |
| v1 | trend_8_26 AND volume_26 | 10000.00 | 0.00 | 대기 /  / 새 신호 대기 |
| v1 | trend_8_26 + volume_26 | 9940.71 | -59.29 | buy /  / trend_8_26 + volume_26: prior completed bar target 50%; next bar open simulation |
| v1 | momentum_26 AND breakout_8 | 9929.38 | -70.62 | sell /  / momentum_26 AND breakout_8: prior completed bar target 0%; next bar open simulation |
| v1 | momentum_26 + breakout_8 | 9912.56 | -87.44 | sell /  / momentum_26 + breakout_8: prior completed bar target 0%; next bar open simulation |
| v1 | momentum_26 AND reversion_12 | 10000.00 | 0.00 | 대기 /  / 새 신호 대기 |
| v1 | momentum_26 + reversion_12 | 9940.71 | -59.29 | buy /  / momentum_26 + reversion_12: prior completed bar target 50%; next bar open simulation |
| v1 | momentum_26 AND volume_26 | 10000.00 | 0.00 | 대기 /  / 새 신호 대기 |
| v1 | momentum_26 + volume_26 | 9947.71 | -52.29 | sell /  / momentum_26 + volume_26: prior completed bar target 0%; next bar open simulation |
| v1 | breakout_8 AND reversion_12 | 10000.00 | 0.00 | 대기 /  / 새 신호 대기 |
| v1 | breakout_8 + reversion_12 | 9937.72 | -62.28 | sell /  / breakout_8 + reversion_12: prior completed bar target 50%; next bar open simulation |
| v1 | breakout_8 AND volume_26 | 10000.00 | 0.00 | 대기 /  / 새 신호 대기 |
| v1 | breakout_8 + volume_26 | 9964.62 | -35.38 | sell /  / breakout_8 + volume_26: prior completed bar target 0%; next bar open simulation |
| v1 | reversion_12 AND volume_26 | 10000.00 | 0.00 | 대기 /  / 새 신호 대기 |
| v1 | reversion_12 + volume_26 | 9973.01 | -26.99 | sell /  / reversion_12 + volume_26: prior completed bar target 50%; next bar open simulation |
| v1 | ema_12_26 | 9881.87 | -118.13 | buy /  / EMA12 > EMA26; 조건 충족; EMA12=274.113, EMA26=273.616 |
| v1 | macd_12_26_9 | 9916.70 | -83.30 | sell /  / MACD > 신호선 그리고 MACD > 0; 조건 미충족; MACD=0.425881, signal9=0.461272 |
| v1 | rsi_14_recovery | 10000.00 | 0.00 | 대기 /  / 새 신호 대기 |
| v1 | bollinger_20_reentry | 10000.00 | 0.00 | 대기 /  / 새 신호 대기 |
| v1 | donchian_20 | 9929.38 | -70.62 | sell /  / 종가 > 현재 봉을 제외한 직전 20봉 최고가; 조건 미충족; close=274.88, prior_high20=275.91 |
| v1 | atr_14_breakout | 9929.38 | -70.62 | sell /  / 종가 > 직전 종가 + 직전 ATR14 그리고 종가 > EMA26; 조건 미충족; close=274.88, threshold=276.257, prior_ATR14=0.526844, EMA26=273.855 |
| v1 | session_vwap | 9937.31 | -62.69 | sell /  / 종가 > 뉴욕 거래일별 누적 전형가격 VWAP; 조건 미충족; close=274.88, session_VWAP=275.422, session_volume=2.52313e+06 |
| v1 | obv_20 | 9928.63 | -71.37 | sell /  / OBV > OBV의 SMA20 그리고 종가 > EMA26; 조건 미충족; OBV=-4.10489e+07, OBV_SMA20=-4.0926e+07, close=274.64, EMA26=273.913 |
| v1 | stochastic_14_3_recovery | 10000.00 | 0.00 | 대기 /  / 새 신호 대기 |
| v1 | mfi_14_recovery | 10000.00 | 0.00 | 대기 /  / 새 신호 대기 |
| v1 | adx_14_trend | 9876.21 | -123.79 | sell /  / Wilder ADX14 >= 25 그리고 +DI14 > -DI14; 조건 미충족; ADX14=27.8588, plus_DI14=21.3361, minus_DI14=26.336 |
| v1 | aroon_25_trend | 9881.87 | -118.13 | buy /  / Aroon25 Up > 70 그리고 Down < 30 (동률이면 최신 극값); 조건 충족; Aroon_up=100, Aroon_down=4 |
| v1 | cci_20_momentum | 9928.63 | -71.37 | sell /  / CCI20 > 100 (전형가격·평균절대편차); 조건 미충족; CCI20=90.0513 |
| v1 | williams_14_recovery | 10000.00 | 0.00 | 대기 /  / 새 신호 대기 |
| v1 | cmf_20_accumulation | 9843.27 | -156.73 | sell /  / Chaikin Money Flow20 > 0.1; 조건 미충족; CMF20=0.0663812, volume20=1.58199e+07 |
| v1 | chaikin_3_10 | 9916.70 | -83.30 | sell /  / ADL의 EMA3 - EMA10 > 0 그리고 종가 > EMA26; 조건 미충족; Chaikin3_10=-335917, ADL=-5.92841e+07, close=274.31, EMA26=274.011 |
| v1 | roc_10_momentum | 10000.00 | 0.00 | 대기 /  / 새 신호 대기 |
| v1 | trix_15_trend | 9895.73 | -104.27 | sell /  / 15봉 삼중 EMA의 1봉 변화율 TRIX > 0 그리고 종가 > EMA26; 조건 미충족; TRIX15_percent=0.0257204, close=273.74, EMA26=273.991 |
| v1 | keltner_20_breakout | 9937.31 | -62.69 | sell /  / 종가 > EMA20 + 2 x Wilder ATR14; 조건 미충족; close=274.88, upper_Keltner=275.161, EMA20=274.044, ATR14=0.558498 |
| v1 | opening_range_30m | 9968.03 | -31.97 | sell /  / 뉴욕 09:30·09:45 두 완료 봉 최고가를 10:00 이후 종가가 돌파; 자료 부족·변동폭 또는 거래량 없음: 대기; close=275.73 |
| v2 | cash | 10000.00 | 0.00 | 대기 /  / 새 신호 대기 |
| v2 | buy_hold | 9776.21 | -223.79 | buy / partial / 직전 완료 봉 목표 비중 100%; 다음 봉 시가 가정 |
| v2 | trend_8_26 | 9753.82 | -246.18 | buy / partial / 직전 완료 봉 목표 비중 100%; 다음 봉 시가 가정 |
| v2 | momentum_26 | 9767.53 | -232.47 | sell / filled / 직전 완료 봉 목표 비중 0%; 다음 봉 시가 가정 |
| v2 | breakout_8 | 9547.89 | -452.11 | sell / filled / 직전 완료 봉 목표 비중 0%; 다음 봉 시가 가정 |
| v2 | reversion_12 | 9486.33 | -513.67 | buy / partial / 직전 완료 봉 목표 비중 100%; 다음 봉 시가 가정 |
| v2 | volume_26 | 9513.36 | -486.64 | sell / filled / 직전 완료 봉 목표 비중 0%; 다음 봉 시가 가정 |
| v2 | trend_8_26 AND momentum_26 | 9918.12 | -81.88 | sell / filled / 직전 완료 봉 목표 비중 0%; 다음 봉 시가 가정 |
| v2 | trend_8_26 + momentum_26 | 9781.33 | -218.67 | sell / filled / 직전 완료 봉 목표 비중 50%; 다음 봉 시가 가정 |
| v2 | trend_8_26 AND breakout_8 | 9840.76 | -159.24 | sell / filled / 직전 완료 봉 목표 비중 0%; 다음 봉 시가 가정 |
| v2 | trend_8_26 + breakout_8 | 9670.72 | -329.28 | buy / filled / 직전 완료 봉 목표 비중 50%; 다음 봉 시가 가정 |
| v2 | trend_8_26 AND reversion_12 | 9827.60 | -172.40 | buy / partial / 직전 완료 봉 목표 비중 100%; 다음 봉 시가 가정 |
| v2 | trend_8_26 + reversion_12 | 9618.96 | -381.04 | buy / partial / 직전 완료 봉 목표 비중 100%; 다음 봉 시가 가정 |
| v2 | trend_8_26 AND volume_26 | 9862.83 | -137.17 | sell / filled / 직전 완료 봉 목표 비중 0%; 다음 봉 시가 가정 |
| v2 | trend_8_26 + volume_26 | 9653.04 | -346.96 | buy / filled / 직전 완료 봉 목표 비중 50%; 다음 봉 시가 가정 |
| v2 | momentum_26 AND breakout_8 | 9733.71 | -266.29 | sell / filled / 직전 완료 봉 목표 비중 0%; 다음 봉 시가 가정 |
| v2 | momentum_26 + breakout_8 | 9657.13 | -342.87 | sell / filled / 직전 완료 봉 목표 비중 0%; 다음 봉 시가 가정 |
| v2 | momentum_26 AND reversion_12 | 9960.59 | -39.41 | sell / filled / 직전 완료 봉 목표 비중 0%; 다음 봉 시가 가정 |
| v2 | momentum_26 + reversion_12 | 9666.00 | -334.00 | buy / filled / 직전 완료 봉 목표 비중 50%; 다음 봉 시가 가정 |
| v2 | momentum_26 AND volume_26 | 9897.79 | -102.21 | sell / filled / 직전 완료 봉 목표 비중 0%; 다음 봉 시가 가정 |
| v2 | momentum_26 + volume_26 | 9639.38 | -360.62 | sell / filled / 직전 완료 봉 목표 비중 0%; 다음 봉 시가 가정 |
| v2 | breakout_8 AND reversion_12 | 10000.00 | 0.00 | 대기 /  / 새 신호 대기 |
| v2 | breakout_8 + reversion_12 | 9556.70 | -443.30 | sell / filled / 직전 완료 봉 목표 비중 50%; 다음 봉 시가 가정 |
| v2 | breakout_8 AND volume_26 | 9746.03 | -253.97 | sell / filled / 직전 완료 봉 목표 비중 0%; 다음 봉 시가 가정 |
| v2 | breakout_8 + volume_26 | 9550.58 | -449.42 | sell / filled / 직전 완료 봉 목표 비중 0%; 다음 봉 시가 가정 |
| v2 | reversion_12 AND volume_26 | 9740.75 | -259.25 | sell / filled / 직전 완료 봉 목표 비중 0%; 다음 봉 시가 가정 |
| v2 | reversion_12 + volume_26 | 9519.58 | -480.42 | sell / filled / 직전 완료 봉 목표 비중 50%; 다음 봉 시가 가정 |
| v2 | ema_12_26 | 9880.88 | -119.12 | buy / partial / EMA12 > EMA26; 조건 충족; EMA12=274.113, EMA26=273.616; 직전 완료 봉 목표를 다음 봉 시가에 모의 적용 |
| v2 | macd_12_26_9 | 9914.72 | -85.28 | sell / filled / MACD > 신호선 그리고 MACD > 0; 조건 미충족; MACD=0.425881, signal9=0.461272; 직전 완료 봉 목표를 다음 봉 시가에 모의 적용 |
| v2 | rsi_14_recovery | 10000.00 | 0.00 | 대기 /  / 새 신호 대기 |
| v2 | bollinger_20_reentry | 10000.00 | 0.00 | 대기 /  / 새 신호 대기 |
| v2 | donchian_20 | 9927.39 | -72.61 | sell / filled / 종가 > 현재 봉을 제외한 직전 20봉 최고가; 조건 미충족; close=274.88, prior_high20=275.91; 직전 완료 봉 목표를 다음 봉 시가에 모의 적용 |
| v2 | atr_14_breakout | 9927.39 | -72.61 | sell / filled / 종가 > 직전 종가 + 직전 ATR14 그리고 종가 > EMA26; 조건 미충족; close=274.88, threshold=276.257, prior_ATR14=0.526844, EMA26=273.855; 직전 완료 봉 목표를 다음 봉 시가에 모의 적용 |
| v2 | session_vwap | 9935.32 | -64.68 | sell / filled / 종가 > 뉴욕 거래일별 누적 전형가격 VWAP; 조건 미충족; close=274.88, session_VWAP=275.422, session_volume=2.52313e+06; 직전 완료 봉 목표를 다음 봉 시가에 모의 적용 |
| v2 | obv_20 | 9926.64 | -73.36 | sell / filled / OBV > OBV의 SMA20 그리고 종가 > EMA26; 조건 미충족; OBV=-4.10489e+07, OBV_SMA20=-4.0926e+07, close=274.64, EMA26=273.913; 직전 완료 봉 목표를 다음 봉 시가에 모의 적용 |
| v2 | stochastic_14_3_recovery | 10000.00 | 0.00 | 대기 /  / 새 신호 대기 |
| v2 | mfi_14_recovery | 10000.00 | 0.00 | 대기 /  / 새 신호 대기 |
| v2 | adx_14_trend | 9874.24 | -125.76 | sell / filled / Wilder ADX14 >= 25 그리고 +DI14 > -DI14; 조건 미충족; ADX14=27.8588, plus_DI14=21.3361, minus_DI14=26.336; 직전 완료 봉 목표를 다음 봉 시가에 모의 적용 |
| v2 | aroon_25_trend | 9880.88 | -119.12 | buy / partial / Aroon25 Up > 70 그리고 Down < 30 (동률이면 최신 극값); 조건 충족; Aroon_up=100, Aroon_down=4; 직전 완료 봉 목표를 다음 봉 시가에 모의 적용 |
| v2 | cci_20_momentum | 9926.64 | -73.36 | sell / filled / CCI20 > 100 (전형가격·평균절대편차); 조건 미충족; CCI20=90.0513; 직전 완료 봉 목표를 다음 봉 시가에 모의 적용 |
| v2 | williams_14_recovery | 10000.00 | 0.00 | 대기 /  / 새 신호 대기 |
| v2 | cmf_20_accumulation | 9837.36 | -162.64 | sell / filled / Chaikin Money Flow20 > 0.1; 조건 미충족; CMF20=0.0663812, volume20=1.58199e+07; 직전 완료 봉 목표를 다음 봉 시가에 모의 적용 |
| v2 | chaikin_3_10 | 9914.72 | -85.28 | sell / filled / ADL의 EMA3 - EMA10 > 0 그리고 종가 > EMA26; 조건 미충족; Chaikin3_10=-335917, ADL=-5.92841e+07, close=274.31, EMA26=274.011; 직전 완료 봉 목표를 다음 봉 시가에 모의 적용 |
| v2 | roc_10_momentum | 10000.00 | 0.00 | 대기 /  / 새 신호 대기 |
| v2 | trix_15_trend | 9893.75 | -106.25 | sell / filled / 15봉 삼중 EMA의 1봉 변화율 TRIX > 0 그리고 종가 > EMA26; 조건 미충족; TRIX15_percent=0.0257204, close=273.74, EMA26=273.991; 직전 완료 봉 목표를 다음 봉 시가에 모의 적용 |
| v2 | keltner_20_breakout | 9935.32 | -64.68 | sell / filled / 종가 > EMA20 + 2 x Wilder ATR14; 조건 미충족; close=274.88, upper_Keltner=275.161, EMA20=274.044, ATR14=0.558498; 직전 완료 봉 목표를 다음 봉 시가에 모의 적용 |
| v2 | opening_range_30m | 9966.04 | -33.96 | sell / filled / 뉴욕 09:30·09:45 두 완료 봉 최고가를 10:00 이후 종가가 돌파; 자료 부족·변동폭 또는 거래량 없음: 대기; close=275.73; 직전 완료 봉 목표를 다음 봉 시가에 모의 적용 |

### 같은 기간의 비용·노출 비교 (사후 연구)

| 전략 | 비용 전 | 비용 후 | 100% 보유 | 같은 평균 노출 보유 | 평균 노출 |
|---|---:|---:|---:|---:|---:|
| cash | 0.00% | 0.00% | -3.69% | -0.00% | 0.00% |
| buy_hold | -3.29% | -3.69% | -3.69% | -3.69% | 100.00% |
| trend_8_26 | -1.95% | -5.58% | -3.69% | -1.68% | 45.12% |
| momentum_26 | -2.97% | -8.51% | -3.69% | -1.47% | 39.58% |
| breakout_8 | -1.07% | -14.24% | -3.69% | -0.72% | 19.26% |
| reversion_12 | -2.51% | -15.13% | -3.69% | -1.11% | 29.82% |
| volume_26 | -2.31% | -9.05% | -3.69% | -0.32% | 8.44% |
| trend_8_26 AND momentum_26 | -1.85% | -5.89% | -3.69% | -1.29% | 34.56% |
| trend_8_26 + momentum_26 | -2.45% | -6.66% | -3.69% | -1.58% | 42.35% |
| trend_8_26 AND breakout_8 | -0.58% | -8.20% | -3.69% | -0.41% | 11.08% |
| trend_8_26 + breakout_8 | -1.50% | -9.82% | -3.69% | -1.20% | 32.20% |
| trend_8_26 AND reversion_12 | -0.49% | -5.38% | -3.69% | -0.22% | 5.80% |
| trend_8_26 + reversion_12 | -2.22% | -10.30% | -3.69% | -1.40% | 37.47% |
| trend_8_26 AND volume_26 | -1.03% | -4.30% | -3.69% | -0.13% | 3.43% |
| trend_8_26 + volume_26 | -2.12% | -7.14% | -3.69% | -1.00% | 26.78% |
| momentum_26 AND breakout_8 | -0.34% | -7.98% | -3.69% | -0.40% | 10.55% |
| momentum_26 + breakout_8 | -2.02% | -11.42% | -3.69% | -1.10% | 29.43% |
| momentum_26 AND reversion_12 | -0.08% | -3.38% | -3.69% | -0.10% | 2.64% |
| momentum_26 + reversion_12 | -2.73% | -10.59% | -3.69% | -1.29% | 34.70% |
| momentum_26 AND volume_26 | -1.32% | -3.77% | -3.69% | -0.07% | 1.85% |
| momentum_26 + volume_26 | -2.64% | -8.40% | -3.69% | -0.90% | 24.01% |
| breakout_8 AND reversion_12 | 0.00% | 0.00% | -3.69% | -0.00% | 0.00% |
| breakout_8 + reversion_12 | -1.79% | -13.97% | -3.69% | -0.92% | 24.55% |
| breakout_8 AND volume_26 | -1.30% | -3.76% | -3.69% | -0.08% | 2.11% |
| breakout_8 + volume_26 | -1.69% | -11.50% | -3.69% | -0.52% | 13.86% |
| reversion_12 AND volume_26 | -0.38% | -4.47% | -3.69% | -0.17% | 4.49% |
| reversion_12 + volume_26 | -2.41% | -11.59% | -3.69% | -0.72% | 19.14% |
| ema_12_26 | -0.34% | -2.82% | -3.69% | -1.63% | 43.80% |
| macd_12_26_9 | 1.76% | -0.78% | -3.69% | -1.01% | 27.18% |
| rsi_14_recovery | -0.28% | -4.78% | -3.69% | -0.11% | 2.90% |
| bollinger_20_reentry | -0.25% | -4.75% | -3.69% | -0.11% | 2.90% |
| donchian_20 | -0.20% | -5.10% | -3.69% | -0.21% | 5.54% |
| atr_14_breakout | -1.87% | -8.25% | -3.69% | -0.16% | 4.22% |
| session_vwap | -1.55% | -11.37% | -3.69% | -1.63% | 43.80% |
| obv_20 | -0.44% | -4.93% | -3.69% | -1.40% | 37.47% |
| stochastic_14_3_recovery | -0.87% | -13.34% | -3.69% | -0.32% | 8.44% |
| mfi_14_recovery | 0.22% | -3.50% | -3.69% | -0.09% | 2.37% |
| adx_14_trend | -0.58% | -4.27% | -3.69% | -1.18% | 31.66% |
| aroon_25_trend | -1.70% | -4.95% | -3.69% | -0.77% | 20.58% |
| cci_20_momentum | -1.95% | -7.93% | -3.69% | -0.65% | 17.41% |
| williams_14_recovery | -0.74% | -10.26% | -3.69% | -0.24% | 6.33% |
| cmf_20_accumulation | -2.35% | -8.70% | -3.69% | -0.71% | 19.00% |
| chaikin_3_10 | -3.02% | -9.70% | -3.69% | -1.23% | 32.98% |
| roc_10_momentum | -0.63% | -1.87% | -3.69% | -0.12% | 3.17% |
| trix_15_trend | -0.27% | -3.57% | -3.69% | -1.23% | 32.98% |
| keltner_20_breakout | -0.91% | -4.18% | -3.69% | -0.20% | 5.28% |
| opening_range_30m | 1.50% | -3.49% | -3.69% | -0.91% | 24.27% |

동일 구간·초기 자금, 종료 시 청산 비용 포함. 노출 맞춤은 사후 설명용이며 v2 실제 계좌 성과가 아닙니다.
[낙폭 분해·비용 영향·전체 구간](IWM/comparison.json)

[v1 전체 기록](IWM/accounts.json) · [v2 전체 기록](IWM/accounts-v2.json)

## DIA 계좌

| 모델 | 전략 | 평가액 USD | 손익 USD | 최근 매매·이유 |
|---|---|---:|---:|---|
| v1 | cash | 10000.00 | 0.00 | 대기 /  / 새 신호 대기 |
| v1 | buy_hold | 9964.95 | -35.05 | buy /  / buy_hold: prior completed bar target 100%; next bar open simulation |
| v1 | trend_8_26 | 9964.95 | -35.05 | buy /  / trend_8_26: prior completed bar target 100%; next bar open simulation |
| v1 | momentum_26 | 9964.95 | -35.05 | buy /  / momentum_26: prior completed bar target 100%; next bar open simulation |
| v1 | breakout_8 | 9940.12 | -59.88 | sell /  / breakout_8: prior completed bar target 0%; next bar open simulation |
| v1 | reversion_12 | 10000.00 | 0.00 | 대기 /  / 새 신호 대기 |
| v1 | volume_26 | 10000.00 | 0.00 | 대기 /  / 새 신호 대기 |
| v1 | trend_8_26 AND momentum_26 | 9964.95 | -35.05 | buy /  / trend_8_26 AND momentum_26: prior completed bar target 100%; next bar open simulation |
| v1 | trend_8_26 + momentum_26 | 9964.95 | -35.05 | buy /  / trend_8_26 + momentum_26: prior completed bar target 100%; next bar open simulation |
| v1 | trend_8_26 AND breakout_8 | 9940.12 | -59.88 | sell /  / trend_8_26 AND breakout_8: prior completed bar target 0%; next bar open simulation |
| v1 | trend_8_26 + breakout_8 | 9952.53 | -47.47 | buy /  / trend_8_26 + breakout_8: prior completed bar target 50%; next bar open simulation |
| v1 | trend_8_26 AND reversion_12 | 10000.00 | 0.00 | 대기 /  / 새 신호 대기 |
| v1 | trend_8_26 + reversion_12 | 9982.42 | -17.58 | buy /  / trend_8_26 + reversion_12: prior completed bar target 50%; next bar open simulation |
| v1 | trend_8_26 AND volume_26 | 10000.00 | 0.00 | 대기 /  / 새 신호 대기 |
| v1 | trend_8_26 + volume_26 | 9982.42 | -17.58 | buy /  / trend_8_26 + volume_26: prior completed bar target 50%; next bar open simulation |
| v1 | momentum_26 AND breakout_8 | 9940.12 | -59.88 | sell /  / momentum_26 AND breakout_8: prior completed bar target 0%; next bar open simulation |
| v1 | momentum_26 + breakout_8 | 9952.53 | -47.47 | buy /  / momentum_26 + breakout_8: prior completed bar target 50%; next bar open simulation |
| v1 | momentum_26 AND reversion_12 | 10000.00 | 0.00 | 대기 /  / 새 신호 대기 |
| v1 | momentum_26 + reversion_12 | 9982.42 | -17.58 | buy /  / momentum_26 + reversion_12: prior completed bar target 50%; next bar open simulation |
| v1 | momentum_26 AND volume_26 | 10000.00 | 0.00 | 대기 /  / 새 신호 대기 |
| v1 | momentum_26 + volume_26 | 9982.42 | -17.58 | buy /  / momentum_26 + volume_26: prior completed bar target 50%; next bar open simulation |
| v1 | breakout_8 AND reversion_12 | 10000.00 | 0.00 | 대기 /  / 새 신호 대기 |
| v1 | breakout_8 + reversion_12 | 9970.03 | -29.97 | sell /  / breakout_8 + reversion_12: prior completed bar target 0%; next bar open simulation |
| v1 | breakout_8 AND volume_26 | 10000.00 | 0.00 | 대기 /  / 새 신호 대기 |
| v1 | breakout_8 + volume_26 | 9970.03 | -29.97 | sell /  / breakout_8 + volume_26: prior completed bar target 0%; next bar open simulation |
| v1 | reversion_12 AND volume_26 | 10000.00 | 0.00 | 대기 /  / 새 신호 대기 |
| v1 | reversion_12 + volume_26 | 10000.00 | 0.00 | 대기 /  / 새 신호 대기 |
| v1 | ema_12_26 | 9964.95 | -35.05 | buy /  / EMA12 > EMA26; 조건 충족; EMA12=520.818, EMA26=519.784 |
| v1 | macd_12_26_9 | 9941.64 | -58.36 | sell /  / MACD > 신호선 그리고 MACD > 0; 조건 미충족; MACD=1.23542, signal9=1.25143 |
| v1 | rsi_14_recovery | 10000.00 | 0.00 | 대기 /  / 새 신호 대기 |
| v1 | bollinger_20_reentry | 10000.00 | 0.00 | 대기 /  / 새 신호 대기 |
| v1 | donchian_20 | 9940.12 | -59.88 | sell /  / 종가 > 현재 봉을 제외한 직전 20봉 최고가; 조건 미충족; close=522.89, prior_high20=525.09 |
| v1 | atr_14_breakout | 9972.44 | -27.56 | sell /  / 종가 > 직전 종가 + 직전 ATR14 그리고 종가 > EMA26; 조건 미충족; close=524.65, threshold=524.777, prior_ATR14=0.84688, EMA26=520.429 |
| v1 | session_vwap | 9960.84 | -39.16 | sell /  / 종가 > 뉴욕 거래일별 누적 전형가격 VWAP; 조건 미충족; close=522.89, session_VWAP=523.72, session_volume=975370 |
| v1 | obv_20 | 9944.22 | -55.78 | buy /  / OBV > OBV의 SMA20 그리고 종가 > EMA26; 조건 충족; OBV=-4.80658e+06, OBV_SMA20=-5.3038e+06, close=523.93, EMA26=520.091 |
| v1 | stochastic_14_3_recovery | 10000.00 | 0.00 | 대기 /  / 새 신호 대기 |
| v1 | mfi_14_recovery | 10000.00 | 0.00 | 대기 /  / 새 신호 대기 |
| v1 | adx_14_trend | 9964.95 | -35.05 | buy /  / Wilder ADX14 >= 25 그리고 +DI14 > -DI14; 조건 충족; ADX14=38.0858, plus_DI14=35.3559, minus_DI14=16.277 |
| v1 | aroon_25_trend | 9964.95 | -35.05 | buy /  / Aroon25 Up > 70 그리고 Down < 30 (동률이면 최신 극값); 조건 충족; Aroon_up=92, Aroon_down=4 |
| v1 | cci_20_momentum | 9954.56 | -45.44 | sell /  / CCI20 > 100 (전형가격·평균절대편차); 조건 미충족; CCI20=83.6046 |
| v1 | williams_14_recovery | 10000.00 | 0.00 | 대기 /  / 새 신호 대기 |
| v1 | cmf_20_accumulation | 9927.80 | -72.20 | sell /  / Chaikin Money Flow20 > 0.1; 조건 미충족; CMF20=0.0502896, volume20=2.48879e+06 |
| v1 | chaikin_3_10 | 9926.34 | -73.66 | sell /  / ADL의 EMA3 - EMA10 > 0 그리고 종가 > EMA26; 조건 미충족; Chaikin3_10=-14655, ADL=-1.49709e+07, close=522.196, EMA26=521.317 |
| v1 | roc_10_momentum | 10000.00 | 0.00 | 대기 /  / 새 신호 대기 |
| v1 | trix_15_trend | 9964.95 | -35.05 | buy /  / 15봉 삼중 EMA의 1봉 변화율 TRIX > 0 그리고 종가 > EMA26; 조건 충족; TRIX15_percent=0.0323703, close=521.24, EMA26=519.784 |
| v1 | keltner_20_breakout | 9940.12 | -59.88 | sell /  / 종가 > EMA20 + 2 x Wilder ATR14; 조건 미충족; close=522.89, upper_Keltner=523.089, EMA20=521.145, ATR14=0.971947 |
| v1 | opening_range_30m | 9980.84 | -19.16 | sell /  / 뉴욕 09:30·09:45 두 완료 봉 최고가를 10:00 이후 종가가 돌파; 자료 부족·변동폭 또는 거래량 없음: 대기; close=523.93 |
| v2 | cash | 10000.00 | 0.00 | 대기 /  / 새 신호 대기 |
| v2 | buy_hold | 10088.40 | 88.40 | buy / partial / 직전 완료 봉 목표 비중 100%; 다음 봉 시가 가정 |
| v2 | trend_8_26 | 9900.39 | -99.61 | buy / partial / 직전 완료 봉 목표 비중 100%; 다음 봉 시가 가정 |
| v2 | momentum_26 | 10009.25 | 9.25 | buy / partial / 직전 완료 봉 목표 비중 100%; 다음 봉 시가 가정 |
| v2 | breakout_8 | 9466.63 | -533.37 | sell / filled / 직전 완료 봉 목표 비중 0%; 다음 봉 시가 가정 |
| v2 | reversion_12 | 9698.03 | -301.97 | sell / filled / 직전 완료 봉 목표 비중 0%; 다음 봉 시가 가정 |
| v2 | volume_26 | 9718.21 | -281.79 | sell / filled / 직전 완료 봉 목표 비중 0%; 다음 봉 시가 가정 |
| v2 | trend_8_26 AND momentum_26 | 10004.60 | 4.60 | buy / partial / 직전 완료 봉 목표 비중 100%; 다음 봉 시가 가정 |
| v2 | trend_8_26 + momentum_26 | 9954.74 | -45.26 | buy / partial / 직전 완료 봉 목표 비중 100%; 다음 봉 시가 가정 |
| v2 | trend_8_26 AND breakout_8 | 9626.81 | -373.19 | sell / filled / 직전 완료 봉 목표 비중 0%; 다음 봉 시가 가정 |
| v2 | trend_8_26 + breakout_8 | 9681.16 | -318.84 | buy / filled / 직전 완료 봉 목표 비중 50%; 다음 봉 시가 가정 |
| v2 | trend_8_26 AND reversion_12 | 9810.77 | -189.23 | sell / filled / 직전 완료 봉 목표 비중 0%; 다음 봉 시가 가정 |
| v2 | trend_8_26 + reversion_12 | 9798.40 | -201.60 | buy / filled / 직전 완료 봉 목표 비중 50%; 다음 봉 시가 가정 |
| v2 | trend_8_26 AND volume_26 | 9858.88 | -141.12 | sell / filled / 직전 완료 봉 목표 비중 0%; 다음 봉 시가 가정 |
| v2 | trend_8_26 + volume_26 | 9829.41 | -170.59 | buy / filled / 직전 완료 봉 목표 비중 50%; 다음 봉 시가 가정 |
| v2 | momentum_26 AND breakout_8 | 9615.85 | -384.15 | sell / filled / 직전 완료 봉 목표 비중 0%; 다음 봉 시가 가정 |
| v2 | momentum_26 + breakout_8 | 9734.30 | -265.70 | buy / filled / 직전 완료 봉 목표 비중 50%; 다음 봉 시가 가정 |
| v2 | momentum_26 AND reversion_12 | 9955.97 | -44.03 | sell / filled / 직전 완료 봉 목표 비중 0%; 다음 봉 시가 가정 |
| v2 | momentum_26 + reversion_12 | 9852.19 | -147.81 | buy / filled / 직전 완료 봉 목표 비중 50%; 다음 봉 시가 가정 |
| v2 | momentum_26 AND volume_26 | 9791.42 | -208.58 | sell / filled / 직전 완료 봉 목표 비중 0%; 다음 봉 시가 가정 |
| v2 | momentum_26 + volume_26 | 9904.21 | -95.79 | buy / filled / 직전 완료 봉 목표 비중 50%; 다음 봉 시가 가정 |
| v2 | breakout_8 AND reversion_12 | 10000.00 | 0.00 | 대기 /  / 새 신호 대기 |
| v2 | breakout_8 + reversion_12 | 9581.22 | -418.78 | sell / filled / 직전 완료 봉 목표 비중 0%; 다음 봉 시가 가정 |
| v2 | breakout_8 AND volume_26 | 9796.56 | -203.44 | sell / filled / 직전 완료 봉 목표 비중 0%; 다음 봉 시가 가정 |
| v2 | breakout_8 + volume_26 | 9591.45 | -408.55 | sell / filled / 직전 완료 봉 목표 비중 0%; 다음 봉 시가 가정 |
| v2 | reversion_12 AND volume_26 | 10000.00 | 0.00 | 대기 /  / 새 신호 대기 |
| v2 | reversion_12 + volume_26 | 9707.85 | -292.15 | sell / filled / 직전 완료 봉 목표 비중 0%; 다음 봉 시가 가정 |
| v2 | ema_12_26 | 9963.96 | -36.04 | buy / partial / EMA12 > EMA26; 조건 충족; EMA12=520.818, EMA26=519.784; 직전 완료 봉 목표를 다음 봉 시가에 모의 적용 |
| v2 | macd_12_26_9 | 9939.65 | -60.35 | sell / filled / MACD > 신호선 그리고 MACD > 0; 조건 미충족; MACD=1.23542, signal9=1.25143; 직전 완료 봉 목표를 다음 봉 시가에 모의 적용 |
| v2 | rsi_14_recovery | 10000.00 | 0.00 | 대기 /  / 새 신호 대기 |
| v2 | bollinger_20_reentry | 10000.00 | 0.00 | 대기 /  / 새 신호 대기 |
| v2 | donchian_20 | 9938.13 | -61.87 | sell / filled / 종가 > 현재 봉을 제외한 직전 20봉 최고가; 조건 미충족; close=522.89, prior_high20=525.09; 직전 완료 봉 목표를 다음 봉 시가에 모의 적용 |
| v2 | atr_14_breakout | 9970.44 | -29.56 | sell / filled / 종가 > 직전 종가 + 직전 ATR14 그리고 종가 > EMA26; 조건 미충족; close=524.65, threshold=524.777, prior_ATR14=0.84688, EMA26=520.429; 직전 완료 봉 목표를 다음 봉 시가에 모의 적용 |
| v2 | session_vwap | 9958.85 | -41.15 | sell / filled / 종가 > 뉴욕 거래일별 누적 전형가격 VWAP; 조건 미충족; close=522.89, session_VWAP=523.72, session_volume=975370; 직전 완료 봉 목표를 다음 봉 시가에 모의 적용 |
| v2 | obv_20 | 9943.23 | -56.77 | buy / partial / OBV > OBV의 SMA20 그리고 종가 > EMA26; 조건 충족; OBV=-4.80658e+06, OBV_SMA20=-5.3038e+06, close=523.93, EMA26=520.091; 직전 완료 봉 목표를 다음 봉 시가에 모의 적용 |
| v2 | stochastic_14_3_recovery | 10000.00 | 0.00 | 대기 /  / 새 신호 대기 |
| v2 | mfi_14_recovery | 10000.00 | 0.00 | 대기 /  / 새 신호 대기 |
| v2 | adx_14_trend | 9963.96 | -36.04 | buy / partial / Wilder ADX14 >= 25 그리고 +DI14 > -DI14; 조건 충족; ADX14=38.0858, plus_DI14=35.3559, minus_DI14=16.277; 직전 완료 봉 목표를 다음 봉 시가에 모의 적용 |
| v2 | aroon_25_trend | 9963.96 | -36.04 | buy / partial / Aroon25 Up > 70 그리고 Down < 30 (동률이면 최신 극값); 조건 충족; Aroon_up=92, Aroon_down=4; 직전 완료 봉 목표를 다음 봉 시가에 모의 적용 |
| v2 | cci_20_momentum | 9952.57 | -47.43 | sell / filled / CCI20 > 100 (전형가격·평균절대편차); 조건 미충족; CCI20=83.6046; 직전 완료 봉 목표를 다음 봉 시가에 모의 적용 |
| v2 | williams_14_recovery | 10000.00 | 0.00 | 대기 /  / 새 신호 대기 |
| v2 | cmf_20_accumulation | 9925.82 | -74.18 | sell / filled / Chaikin Money Flow20 > 0.1; 조건 미충족; CMF20=0.0502896, volume20=2.48879e+06; 직전 완료 봉 목표를 다음 봉 시가에 모의 적용 |
| v2 | chaikin_3_10 | 9924.35 | -75.65 | sell / filled / ADL의 EMA3 - EMA10 > 0 그리고 종가 > EMA26; 조건 미충족; Chaikin3_10=-14655, ADL=-1.49709e+07, close=522.196, EMA26=521.317; 직전 완료 봉 목표를 다음 봉 시가에 모의 적용 |
| v2 | roc_10_momentum | 10000.00 | 0.00 | 대기 /  / 새 신호 대기 |
| v2 | trix_15_trend | 9963.96 | -36.04 | buy / partial / 15봉 삼중 EMA의 1봉 변화율 TRIX > 0 그리고 종가 > EMA26; 조건 충족; TRIX15_percent=0.0323703, close=521.24, EMA26=519.784; 직전 완료 봉 목표를 다음 봉 시가에 모의 적용 |
| v2 | keltner_20_breakout | 9938.13 | -61.87 | sell / filled / 종가 > EMA20 + 2 x Wilder ATR14; 조건 미충족; close=522.89, upper_Keltner=523.089, EMA20=521.145, ATR14=0.971947; 직전 완료 봉 목표를 다음 봉 시가에 모의 적용 |
| v2 | opening_range_30m | 9978.85 | -21.15 | sell / filled / 뉴욕 09:30·09:45 두 완료 봉 최고가를 10:00 이후 종가가 돌파; 자료 부족·변동폭 또는 거래량 없음: 대기; close=523.93; 직전 완료 봉 목표를 다음 봉 시가에 모의 적용 |

### 같은 기간의 비용·노출 비교 (사후 연구)

| 전략 | 비용 전 | 비용 후 | 100% 보유 | 같은 평균 노출 보유 | 평균 노출 |
|---|---:|---:|---:|---:|---:|
| cash | 0.00% | 0.00% | 0.56% | 0.00% | 0.00% |
| buy_hold | 0.98% | 0.56% | 0.56% | 0.56% | 100.00% |
| trend_8_26 | 1.30% | -3.27% | 0.56% | 0.32% | 55.94% |
| momentum_26 | -0.04% | -4.15% | 0.56% | 0.29% | 52.24% |
| breakout_8 | -0.13% | -17.33% | 0.56% | 0.13% | 23.75% |
| reversion_12 | -1.36% | -9.30% | 0.56% | 0.14% | 24.80% |
| volume_26 | -0.91% | -10.78% | 0.56% | 0.06% | 10.82% |
| trend_8_26 AND momentum_26 | 1.43% | -2.74% | 0.56% | 0.26% | 46.44% |
| trend_8_26 + momentum_26 | 0.63% | -3.71% | 0.56% | 0.30% | 54.09% |
| trend_8_26 AND breakout_8 | 0.44% | -11.82% | 0.56% | 0.09% | 15.57% |
| trend_8_26 + breakout_8 | 0.59% | -10.39% | 0.56% | 0.22% | 39.85% |
| trend_8_26 AND reversion_12 | 0.37% | -4.56% | 0.56% | 0.04% | 6.33% |
| trend_8_26 + reversion_12 | -0.03% | -5.95% | 0.56% | 0.23% | 40.37% |
| trend_8_26 AND volume_26 | 0.65% | -4.30% | 0.56% | 0.03% | 5.01% |
| trend_8_26 + volume_26 | 0.19% | -6.92% | 0.56% | 0.19% | 33.38% |
| momentum_26 AND breakout_8 | -0.36% | -12.15% | 0.56% | 0.09% | 15.83% |
| momentum_26 + breakout_8 | -0.08% | -10.79% | 0.56% | 0.21% | 38.00% |
| momentum_26 AND reversion_12 | -0.18% | -3.88% | 0.56% | 0.03% | 5.80% |
| momentum_26 + reversion_12 | -0.69% | -5.98% | 0.56% | 0.22% | 38.53% |
| momentum_26 AND volume_26 | -0.32% | -5.22% | 0.56% | 0.03% | 4.49% |
| momentum_26 + volume_26 | -0.47% | -6.75% | 0.56% | 0.18% | 31.53% |
| breakout_8 AND reversion_12 | 0.00% | 0.00% | 0.56% | 0.00% | 0.00% |
| breakout_8 + reversion_12 | -0.74% | -13.06% | 0.56% | 0.14% | 24.28% |
| breakout_8 AND volume_26 | -0.87% | -4.55% | 0.56% | 0.02% | 3.17% |
| breakout_8 + volume_26 | -0.51% | -13.40% | 0.56% | 0.10% | 17.29% |
| reversion_12 AND volume_26 | -0.20% | -5.11% | 0.56% | 0.02% | 3.96% |
| reversion_12 + volume_26 | -1.13% | -10.05% | 0.56% | 0.10% | 17.82% |
| ema_12_26 | 0.21% | -2.29% | 0.56% | 0.29% | 50.66% |
| macd_12_26_9 | 1.61% | -1.75% | 0.56% | 0.16% | 28.76% |
| rsi_14_recovery | 0.01% | -2.07% | 0.56% | 0.01% | 1.32% |
| bollinger_20_reentry | -0.25% | -5.16% | 0.56% | 0.02% | 3.17% |
| donchian_20 | 0.36% | -5.77% | 0.56% | 0.05% | 8.18% |
| atr_14_breakout | -1.05% | -8.25% | 0.56% | 0.03% | 5.54% |
| session_vwap | 1.11% | -6.64% | 0.56% | 0.29% | 50.92% |
| obv_20 | -0.02% | -8.46% | 0.56% | 0.25% | 44.59% |
| stochastic_14_3_recovery | 0.79% | -11.14% | 0.56% | 0.04% | 7.92% |
| mfi_14_recovery | -0.06% | -2.95% | 0.56% | 0.01% | 1.85% |
| adx_14_trend | -0.40% | -4.49% | 0.56% | 0.21% | 36.94% |
| aroon_25_trend | 0.94% | -2.39% | 0.56% | 0.15% | 25.86% |
| cci_20_momentum | 0.66% | -5.09% | 0.56% | 0.14% | 24.01% |
| williams_14_recovery | 1.01% | -6.74% | 0.56% | 0.03% | 5.01% |
| cmf_20_accumulation | 0.66% | -6.28% | 0.56% | 0.18% | 31.93% |
| chaikin_3_10 | 1.18% | -8.52% | 0.56% | 0.24% | 43.27% |
| roc_10_momentum | 0.15% | -0.27% | 0.56% | 0.01% | 1.32% |
| trix_15_trend | -0.08% | -3.79% | 0.56% | 0.25% | 43.80% |
| keltner_20_breakout | 0.33% | -5.79% | 0.56% | 0.10% | 16.89% |
| opening_range_30m | 0.89% | -5.27% | 0.56% | 0.13% | 22.43% |

동일 구간·초기 자금, 종료 시 청산 비용 포함. 노출 맞춤은 사후 설명용이며 v2 실제 계좌 성과가 아닙니다.
[낙폭 분해·비용 영향·전체 구간](DIA/comparison.json)

[v1 전체 기록](DIA/accounts.json) · [v2 전체 기록](DIA/accounts-v2.json)

## MSFT 계좌

| 모델 | 전략 | 평가액 USD | 손익 USD | 최근 매매·이유 |
|---|---|---:|---:|---|
| v1 | cash | 10000.00 | 0.00 | 대기 /  / 새 신호 대기 |
| v1 | buy_hold | 9796.78 | -203.22 | buy /  / buy_hold: prior completed bar target 100%; next bar open simulation |
| v1 | trend_8_26 | 9853.68 | -146.32 | sell /  / trend_8_26: prior completed bar target 0%; next bar open simulation |
| v1 | momentum_26 | 9839.32 | -160.68 | sell /  / momentum_26: prior completed bar target 0%; next bar open simulation |
| v1 | breakout_8 | 10000.00 | 0.00 | 대기 /  / 새 신호 대기 |
| v1 | reversion_12 | 9866.25 | -133.75 | buy /  / reversion_12: prior completed bar target 100%; next bar open simulation |
| v1 | volume_26 | 9958.37 | -41.63 | buy /  / volume_26: prior completed bar target 100%; next bar open simulation |
| v1 | trend_8_26 AND momentum_26 | 9853.68 | -146.32 | sell /  / trend_8_26 AND momentum_26: prior completed bar target 0%; next bar open simulation |
| v1 | trend_8_26 + momentum_26 | 9846.52 | -153.48 | sell /  / trend_8_26 + momentum_26: prior completed bar target 0%; next bar open simulation |
| v1 | trend_8_26 AND breakout_8 | 10000.00 | 0.00 | 대기 /  / 새 신호 대기 |
| v1 | trend_8_26 + breakout_8 | 9926.58 | -73.42 | sell /  / trend_8_26 + breakout_8: prior completed bar target 0%; next bar open simulation |
| v1 | trend_8_26 AND reversion_12 | 9923.56 | -76.44 | sell /  / trend_8_26 AND reversion_12: prior completed bar target 0%; next bar open simulation |
| v1 | trend_8_26 + reversion_12 | 9859.95 | -140.05 | buy /  / trend_8_26 + reversion_12: prior completed bar target 50%; next bar open simulation |
| v1 | trend_8_26 AND volume_26 | 10000.00 | 0.00 | 대기 /  / 새 신호 대기 |
| v1 | trend_8_26 + volume_26 | 9905.87 | -94.13 | buy /  / trend_8_26 + volume_26: prior completed bar target 50%; next bar open simulation |
| v1 | momentum_26 AND breakout_8 | 10000.00 | 0.00 | 대기 /  / 새 신호 대기 |
| v1 | momentum_26 + breakout_8 | 9919.33 | -80.67 | sell /  / momentum_26 + breakout_8: prior completed bar target 0%; next bar open simulation |
| v1 | momentum_26 AND reversion_12 | 9909.10 | -90.90 | sell /  / momentum_26 AND reversion_12: prior completed bar target 0%; next bar open simulation |
| v1 | momentum_26 + reversion_12 | 9852.76 | -147.24 | buy /  / momentum_26 + reversion_12: prior completed bar target 50%; next bar open simulation |
| v1 | momentum_26 AND volume_26 | 10000.00 | 0.00 | 대기 /  / 새 신호 대기 |
| v1 | momentum_26 + volume_26 | 9898.65 | -101.35 | buy /  / momentum_26 + volume_26: prior completed bar target 50%; next bar open simulation |
| v1 | breakout_8 AND reversion_12 | 10000.00 | 0.00 | 대기 /  / 새 신호 대기 |
| v1 | breakout_8 + reversion_12 | 9932.86 | -67.14 | buy /  / breakout_8 + reversion_12: prior completed bar target 50%; next bar open simulation |
| v1 | breakout_8 AND volume_26 | 10000.00 | 0.00 | 대기 /  / 새 신호 대기 |
| v1 | breakout_8 + volume_26 | 9979.14 | -20.86 | buy /  / breakout_8 + volume_26: prior completed bar target 50%; next bar open simulation |
| v1 | reversion_12 AND volume_26 | 9958.37 | -41.63 | buy /  / reversion_12 AND volume_26: prior completed bar target 100%; next bar open simulation |
| v1 | reversion_12 + volume_26 | 9912.17 | -87.83 | buy /  / reversion_12 + volume_26: prior completed bar target 100%; next bar open simulation |
| v1 | ema_12_26 | 9853.68 | -146.32 | sell /  / EMA12 > EMA26; 조건 미충족; EMA12=538.192, EMA26=538.342 |
| v1 | macd_12_26_9 | 9889.94 | -110.06 | sell /  / MACD > 신호선 그리고 MACD > 0; 조건 미충족; MACD=0.536125, signal9=0.712825 |
| v1 | rsi_14_recovery | 10000.00 | 0.00 | 대기 /  / 새 신호 대기 |
| v1 | bollinger_20_reentry | 9931.47 | -68.53 | sell /  / 직전 종가 < 직전 하단밴드, 현재 하단밴드 <= 종가 <= SMA20 (한 봉 목표); 조건 미충족; close=534.48, lower20=535.11, SMA20=538.768, previous_lower20=535.929 |
| v1 | donchian_20 | 10000.00 | 0.00 | 대기 /  / 새 신호 대기 |
| v1 | atr_14_breakout | 10000.00 | 0.00 | 대기 /  / 새 신호 대기 |
| v1 | session_vwap | 9889.94 | -110.06 | sell /  / 종가 > 뉴욕 거래일별 누적 전형가격 VWAP; 조건 미충족; close=537.34, session_VWAP=538.663, session_volume=3.36828e+06 |
| v1 | obv_20 | 9889.94 | -110.06 | sell /  / OBV > OBV의 SMA20 그리고 종가 > EMA26; 조건 미충족; OBV=1.44955e+08, OBV_SMA20=1.34631e+08, close=537.34, EMA26=538.834 |
| v1 | stochastic_14_3_recovery | 9931.47 | -68.53 | sell /  / 직전 %K14 < 20에서 %K14가 %D3 상향 돌파 (한 봉 목표); 조건 미충족; K14=5.18301, D3=10.6556, previous_K14=21.3213, previous_D3=15.4681 |
| v1 | mfi_14_recovery | 10000.00 | 0.00 | 대기 /  / 새 신호 대기 |
| v1 | adx_14_trend | 9889.94 | -110.06 | sell /  / Wilder ADX14 >= 25 그리고 +DI14 > -DI14; 조건 미충족; ADX14=30.6145, plus_DI14=15.7198, minus_DI14=27.4451 |
| v1 | aroon_25_trend | 9867.67 | -132.33 | sell /  / Aroon25 Up > 70 그리고 Down < 30 (동률이면 최신 극값); 조건 미충족; Aroon_up=84, Aroon_down=100 |
| v1 | cci_20_momentum | 10000.00 | 0.00 | 대기 /  / 새 신호 대기 |
| v1 | williams_14_recovery | 9931.47 | -68.53 | sell /  / 직전 Williams %R14 < -80, 현재 >= -80 (한 봉 목표); 조건 미충족; Williams_R14=-94.817, previous_R14=-78.6787 |
| v1 | cmf_20_accumulation | 9765.23 | -234.77 | sell /  / Chaikin Money Flow20 > 0.1; 조건 미충족; CMF20=-0.0001648, volume20=6.0129e+07 |
| v1 | chaikin_3_10 | 9889.94 | -110.06 | sell /  / ADL의 EMA3 - EMA10 > 0 그리고 종가 > EMA26; 조건 미충족; Chaikin3_10=3.90601e+06, ADL=1.2345e+08, close=537.34, EMA26=538.834 |
| v1 | roc_10_momentum | 10000.00 | 0.00 | 대기 /  / 새 신호 대기 |
| v1 | trix_15_trend | 9889.94 | -110.06 | sell /  / 15봉 삼중 EMA의 1봉 변화율 TRIX > 0 그리고 종가 > EMA26; 조건 미충족; TRIX15_percent=0.0221169, close=537.34, EMA26=538.834 |
| v1 | keltner_20_breakout | 10000.00 | 0.00 | 대기 /  / 새 신호 대기 |
| v1 | opening_range_30m | 9889.94 | -110.06 | sell /  / 뉴욕 09:30·09:45 두 완료 봉 최고가를 10:00 이후 종가가 돌파; 자료 부족·변동폭 또는 거래량 없음: 대기; close=537.34 |
| v2 | cash | 10000.00 | 0.00 | 대기 /  / 새 신호 대기 |
| v2 | buy_hold | 9850.23 | -149.77 | buy / partial / 직전 완료 봉 목표 비중 100%; 다음 봉 시가 가정 |
| v2 | trend_8_26 | 9790.17 | -209.83 | sell / filled / 직전 완료 봉 목표 비중 0%; 다음 봉 시가 가정 |
| v2 | momentum_26 | 9886.18 | -113.82 | sell / filled / 직전 완료 봉 목표 비중 0%; 다음 봉 시가 가정 |
| v2 | breakout_8 | 9799.48 | -200.52 | sell / filled / 직전 완료 봉 목표 비중 0%; 다음 봉 시가 가정 |
| v2 | reversion_12 | 9489.02 | -510.98 | buy / partial / 직전 완료 봉 목표 비중 100%; 다음 봉 시가 가정 |
| v2 | volume_26 | 9647.26 | -352.74 | buy / partial / 직전 완료 봉 목표 비중 100%; 다음 봉 시가 가정 |
| v2 | trend_8_26 AND momentum_26 | 9751.13 | -248.87 | sell / filled / 직전 완료 봉 목표 비중 0%; 다음 봉 시가 가정 |
| v2 | trend_8_26 + momentum_26 | 9838.34 | -161.66 | sell / filled / 직전 완료 봉 목표 비중 0%; 다음 봉 시가 가정 |
| v2 | trend_8_26 AND breakout_8 | 9639.29 | -360.71 | sell / filled / 직전 완료 봉 목표 비중 0%; 다음 봉 시가 가정 |
| v2 | trend_8_26 + breakout_8 | 9815.63 | -184.37 | sell / filled / 직전 완료 봉 목표 비중 0%; 다음 봉 시가 가정 |
| v2 | trend_8_26 AND reversion_12 | 9822.46 | -177.54 | sell / filled / 직전 완료 봉 목표 비중 0%; 다음 봉 시가 가정 |
| v2 | trend_8_26 + reversion_12 | 9638.08 | -361.92 | buy / filled / 직전 완료 봉 목표 비중 50%; 다음 봉 시가 가정 |
| v2 | trend_8_26 AND volume_26 | 9948.66 | -51.34 | sell / filled / 직전 완료 봉 목표 비중 0%; 다음 봉 시가 가정 |
| v2 | trend_8_26 + volume_26 | 9738.66 | -261.34 | buy / filled / 직전 완료 봉 목표 비중 50%; 다음 봉 시가 가정 |
| v2 | momentum_26 AND breakout_8 | 9794.38 | -205.62 | sell / filled / 직전 완료 봉 목표 비중 0%; 다음 봉 시가 가정 |
| v2 | momentum_26 + breakout_8 | 9842.81 | -157.19 | sell / filled / 직전 완료 봉 목표 비중 0%; 다음 봉 시가 가정 |
| v2 | momentum_26 AND reversion_12 | 9735.61 | -264.39 | sell / filled / 직전 완료 봉 목표 비중 0%; 다음 봉 시가 가정 |
| v2 | momentum_26 + reversion_12 | 9685.35 | -314.65 | buy / filled / 직전 완료 봉 목표 비중 50%; 다음 봉 시가 가정 |
| v2 | momentum_26 AND volume_26 | 9871.26 | -128.74 | sell / filled / 직전 완료 봉 목표 비중 0%; 다음 봉 시가 가정 |
| v2 | momentum_26 + volume_26 | 9786.43 | -213.57 | buy / filled / 직전 완료 봉 목표 비중 50%; 다음 봉 시가 가정 |
| v2 | breakout_8 AND reversion_12 | 10000.00 | 0.00 | 대기 /  / 새 신호 대기 |
| v2 | breakout_8 + reversion_12 | 9663.03 | -336.97 | buy / filled / 직전 완료 봉 목표 비중 50%; 다음 봉 시가 가정 |
| v2 | breakout_8 AND volume_26 | 9938.59 | -61.41 | sell / filled / 직전 완료 봉 목표 비중 0%; 다음 봉 시가 가정 |
| v2 | breakout_8 + volume_26 | 9743.53 | -256.47 | buy / filled / 직전 완료 봉 목표 비중 50%; 다음 봉 시가 가정 |
| v2 | reversion_12 AND volume_26 | 9720.43 | -279.57 | buy / partial / 직전 완료 봉 목표 비중 100%; 다음 봉 시가 가정 |
| v2 | reversion_12 + volume_26 | 9567.63 | -432.37 | buy / partial / 직전 완료 봉 목표 비중 100%; 다음 봉 시가 가정 |
| v2 | ema_12_26 | 9851.71 | -148.29 | sell / filled / EMA12 > EMA26; 조건 미충족; EMA12=538.192, EMA26=538.342; 직전 완료 봉 목표를 다음 봉 시가에 모의 적용 |
| v2 | macd_12_26_9 | 9887.97 | -112.03 | sell / filled / MACD > 신호선 그리고 MACD > 0; 조건 미충족; MACD=0.536125, signal9=0.712825; 직전 완료 봉 목표를 다음 봉 시가에 모의 적용 |
| v2 | rsi_14_recovery | 10000.00 | 0.00 | 대기 /  / 새 신호 대기 |
| v2 | bollinger_20_reentry | 9929.48 | -70.52 | sell / filled / 직전 종가 < 직전 하단밴드, 현재 하단밴드 <= 종가 <= SMA20 (한 봉 목표); 조건 미충족; close=534.48, lower20=535.11, SMA20=538.768, previous_lower20=535.929; 직전 완료 봉 목표를 다음 봉 시가에 모의 적용 |
| v2 | donchian_20 | 10000.00 | 0.00 | 대기 /  / 새 신호 대기 |
| v2 | atr_14_breakout | 10000.00 | 0.00 | 대기 /  / 새 신호 대기 |
| v2 | session_vwap | 9887.97 | -112.03 | sell / filled / 종가 > 뉴욕 거래일별 누적 전형가격 VWAP; 조건 미충족; close=537.34, session_VWAP=538.663, session_volume=3.36828e+06; 직전 완료 봉 목표를 다음 봉 시가에 모의 적용 |
| v2 | obv_20 | 9887.97 | -112.03 | sell / filled / OBV > OBV의 SMA20 그리고 종가 > EMA26; 조건 미충족; OBV=1.44955e+08, OBV_SMA20=1.34631e+08, close=537.34, EMA26=538.834; 직전 완료 봉 목표를 다음 봉 시가에 모의 적용 |
| v2 | stochastic_14_3_recovery | 9929.48 | -70.52 | sell / filled / 직전 %K14 < 20에서 %K14가 %D3 상향 돌파 (한 봉 목표); 조건 미충족; K14=5.18301, D3=10.6556, previous_K14=21.3213, previous_D3=15.4681; 직전 완료 봉 목표를 다음 봉 시가에 모의 적용 |
| v2 | mfi_14_recovery | 10000.00 | 0.00 | 대기 /  / 새 신호 대기 |
| v2 | adx_14_trend | 9887.97 | -112.03 | sell / filled / Wilder ADX14 >= 25 그리고 +DI14 > -DI14; 조건 미충족; ADX14=30.6145, plus_DI14=15.7198, minus_DI14=27.4451; 직전 완료 봉 목표를 다음 봉 시가에 모의 적용 |
| v2 | aroon_25_trend | 9865.70 | -134.30 | sell / filled / Aroon25 Up > 70 그리고 Down < 30 (동률이면 최신 극값); 조건 미충족; Aroon_up=84, Aroon_down=100; 직전 완료 봉 목표를 다음 봉 시가에 모의 적용 |
| v2 | cci_20_momentum | 10000.00 | 0.00 | 대기 /  / 새 신호 대기 |
| v2 | williams_14_recovery | 9929.48 | -70.52 | sell / filled / 직전 Williams %R14 < -80, 현재 >= -80 (한 봉 목표); 조건 미충족; Williams_R14=-94.817, previous_R14=-78.6787; 직전 완료 봉 목표를 다음 봉 시가에 모의 적용 |
| v2 | cmf_20_accumulation | 9763.27 | -236.73 | sell / filled / Chaikin Money Flow20 > 0.1; 조건 미충족; CMF20=-0.0001648, volume20=6.0129e+07; 직전 완료 봉 목표를 다음 봉 시가에 모의 적용 |
| v2 | chaikin_3_10 | 9887.97 | -112.03 | sell / filled / ADL의 EMA3 - EMA10 > 0 그리고 종가 > EMA26; 조건 미충족; Chaikin3_10=3.90601e+06, ADL=1.2345e+08, close=537.34, EMA26=538.834; 직전 완료 봉 목표를 다음 봉 시가에 모의 적용 |
| v2 | roc_10_momentum | 10000.00 | 0.00 | 대기 /  / 새 신호 대기 |
| v2 | trix_15_trend | 9887.97 | -112.03 | sell / filled / 15봉 삼중 EMA의 1봉 변화율 TRIX > 0 그리고 종가 > EMA26; 조건 미충족; TRIX15_percent=0.0221169, close=537.34, EMA26=538.834; 직전 완료 봉 목표를 다음 봉 시가에 모의 적용 |
| v2 | keltner_20_breakout | 10000.00 | 0.00 | 대기 /  / 새 신호 대기 |
| v2 | opening_range_30m | 9887.97 | -112.03 | sell / filled / 뉴욕 09:30·09:45 두 완료 봉 최고가를 10:00 이후 종가가 돌파; 자료 부족·변동폭 또는 거래량 없음: 대기; close=537.34; 직전 완료 봉 목표를 다음 봉 시가에 모의 적용 |

### 같은 기간의 비용·노출 비교 (사후 연구)

| 전략 | 비용 전 | 비용 후 | 100% 보유 | 같은 평균 노출 보유 | 평균 노출 |
|---|---:|---:|---:|---:|---:|
| cash | 0.00% | 0.00% | 2.14% | 0.00% | 0.00% |
| buy_hold | 2.57% | 2.14% | 2.14% | 2.14% | 100.00% |
| trend_8_26 | -1.64% | -5.29% | 2.14% | 1.23% | 58.05% |
| momentum_26 | -0.66% | -6.33% | 2.14% | 1.25% | 58.84% |
| breakout_8 | 5.09% | -8.89% | 2.14% | 0.42% | 19.79% |
| reversion_12 | -5.14% | -13.88% | 2.14% | 0.54% | 25.59% |
| volume_26 | 2.21% | -6.42% | 2.14% | 0.18% | 8.71% |
| trend_8_26 AND momentum_26 | -1.90% | -7.50% | 2.14% | 1.11% | 52.24% |
| trend_8_26 + momentum_26 | -1.14% | -5.80% | 2.14% | 1.24% | 58.45% |
| trend_8_26 AND breakout_8 | 0.68% | -8.98% | 2.14% | 0.27% | 12.66% |
| trend_8_26 + breakout_8 | 1.69% | -6.71% | 2.14% | 0.82% | 38.92% |
| trend_8_26 AND reversion_12 | -3.74% | -9.24% | 2.14% | 0.17% | 7.92% |
| trend_8_26 + reversion_12 | -3.39% | -9.31% | 2.14% | 0.89% | 41.82% |
| trend_8_26 AND volume_26 | 3.46% | 0.46% | 2.14% | 0.06% | 2.64% |
| trend_8_26 + volume_26 | 0.29% | -5.06% | 2.14% | 0.71% | 33.38% |
| momentum_26 AND breakout_8 | 2.61% | -7.61% | 2.14% | 0.27% | 12.93% |
| momentum_26 + breakout_8 | 2.19% | -7.03% | 2.14% | 0.83% | 39.32% |
| momentum_26 AND reversion_12 | -3.23% | -9.52% | 2.14% | 0.20% | 9.50% |
| momentum_26 + reversion_12 | -2.91% | -9.81% | 2.14% | 0.90% | 42.22% |
| momentum_26 AND volume_26 | 1.80% | -2.38% | 2.14% | 0.07% | 3.43% |
| momentum_26 + volume_26 | 0.79% | -5.18% | 2.14% | 0.72% | 33.78% |
| breakout_8 AND reversion_12 | 0.00% | 0.00% | 2.14% | 0.00% | 0.00% |
| breakout_8 + reversion_12 | -0.13% | -10.86% | 2.14% | 0.48% | 22.70% |
| breakout_8 AND volume_26 | 2.07% | -0.47% | 2.14% | 0.04% | 1.85% |
| breakout_8 + volume_26 | 3.65% | -6.68% | 2.14% | 0.30% | 14.25% |
| reversion_12 AND volume_26 | -2.48% | -6.49% | 2.14% | 0.08% | 3.96% |
| reversion_12 + volume_26 | -1.52% | -10.03% | 2.14% | 0.36% | 17.16% |
| ema_12_26 | -1.05% | -4.72% | 2.14% | 1.31% | 61.74% |
| macd_12_26_9 | 0.71% | -4.24% | 2.14% | 0.70% | 32.98% |
| rsi_14_recovery | -0.46% | -1.71% | 2.14% | 0.02% | 0.79% |
| bollinger_20_reentry | -0.45% | -3.34% | 2.14% | 0.04% | 1.85% |
| donchian_20 | 1.84% | -3.17% | 2.14% | 0.09% | 4.49% |
| atr_14_breakout | 1.50% | -3.89% | 2.14% | 0.08% | 3.69% |
| session_vwap | 2.46% | -5.40% | 2.14% | 1.00% | 46.97% |
| obv_20 | 3.86% | -5.31% | 2.14% | 1.10% | 51.72% |
| stochastic_14_3_recovery | -0.11% | -9.68% | 2.14% | 0.13% | 6.33% |
| mfi_14_recovery | 1.04% | -1.88% | 2.14% | 0.04% | 1.85% |
| adx_14_trend | 0.95% | -1.98% | 2.14% | 0.96% | 45.38% |
| aroon_25_trend | -0.06% | -4.97% | 2.14% | 0.45% | 21.11% |
| cci_20_momentum | 2.74% | -3.93% | 2.14% | 0.44% | 20.84% |
| williams_14_recovery | -0.28% | -9.09% | 2.14% | 0.12% | 5.80% |
| cmf_20_accumulation | 0.27% | -5.85% | 2.14% | 0.77% | 36.41% |
| chaikin_3_10 | 3.12% | -5.19% | 2.14% | 0.96% | 45.38% |
| roc_10_momentum | -0.20% | -4.30% | 2.14% | 0.30% | 14.25% |
| trix_15_trend | -1.91% | -5.94% | 2.14% | 1.01% | 47.76% |
| keltner_20_breakout | 1.12% | -3.85% | 2.14% | 0.28% | 13.46% |
| opening_range_30m | -2.37% | -7.56% | 2.14% | 0.51% | 24.27% |

동일 구간·초기 자금, 종료 시 청산 비용 포함. 노출 맞춤은 사후 설명용이며 v2 실제 계좌 성과가 아닙니다.
[낙폭 분해·비용 영향·전체 구간](MSFT/comparison.json)

[v1 전체 기록](MSFT/accounts.json) · [v2 전체 기록](MSFT/accounts-v2.json)

## JPM 계좌

| 모델 | 전략 | 평가액 USD | 손익 USD | 최근 매매·이유 |
|---|---|---:|---:|---|
| v1 | cash | 10000.00 | 0.00 | 대기 /  / 새 신호 대기 |
| v1 | buy_hold | 10041.10 | 41.10 | buy /  / buy_hold: prior completed bar target 100%; next bar open simulation |
| v1 | trend_8_26 | 10041.10 | 41.10 | buy /  / trend_8_26: prior completed bar target 100%; next bar open simulation |
| v1 | momentum_26 | 10041.10 | 41.10 | buy /  / momentum_26: prior completed bar target 100%; next bar open simulation |
| v1 | breakout_8 | 9915.55 | -84.45 | sell /  / breakout_8: prior completed bar target 0%; next bar open simulation |
| v1 | reversion_12 | 10000.00 | 0.00 | 대기 /  / 새 신호 대기 |
| v1 | volume_26 | 10035.68 | 35.68 | sell /  / volume_26: prior completed bar target 0%; next bar open simulation |
| v1 | trend_8_26 AND momentum_26 | 10041.10 | 41.10 | buy /  / trend_8_26 AND momentum_26: prior completed bar target 100%; next bar open simulation |
| v1 | trend_8_26 + momentum_26 | 10041.10 | 41.10 | buy /  / trend_8_26 + momentum_26: prior completed bar target 100%; next bar open simulation |
| v1 | trend_8_26 AND breakout_8 | 9915.55 | -84.45 | sell /  / trend_8_26 AND breakout_8: prior completed bar target 0%; next bar open simulation |
| v1 | trend_8_26 + breakout_8 | 9978.23 | -21.77 | sell /  / trend_8_26 + breakout_8: prior completed bar target 50%; next bar open simulation |
| v1 | trend_8_26 AND reversion_12 | 10000.00 | 0.00 | 대기 /  / 새 신호 대기 |
| v1 | trend_8_26 + reversion_12 | 10020.56 | 20.56 | buy /  / trend_8_26 + reversion_12: prior completed bar target 50%; next bar open simulation |
| v1 | trend_8_26 AND volume_26 | 10035.68 | 35.68 | sell /  / trend_8_26 AND volume_26: prior completed bar target 0%; next bar open simulation |
| v1 | trend_8_26 + volume_26 | 10038.38 | 38.38 | buy /  / trend_8_26 + volume_26: prior completed bar target 50%; next bar open simulation |
| v1 | momentum_26 AND breakout_8 | 9915.55 | -84.45 | sell /  / momentum_26 AND breakout_8: prior completed bar target 0%; next bar open simulation |
| v1 | momentum_26 + breakout_8 | 9978.23 | -21.77 | sell /  / momentum_26 + breakout_8: prior completed bar target 50%; next bar open simulation |
| v1 | momentum_26 AND reversion_12 | 10000.00 | 0.00 | 대기 /  / 새 신호 대기 |
| v1 | momentum_26 + reversion_12 | 10020.56 | 20.56 | buy /  / momentum_26 + reversion_12: prior completed bar target 50%; next bar open simulation |
| v1 | momentum_26 AND volume_26 | 10035.68 | 35.68 | sell /  / momentum_26 AND volume_26: prior completed bar target 0%; next bar open simulation |
| v1 | momentum_26 + volume_26 | 10038.38 | 38.38 | buy /  / momentum_26 + volume_26: prior completed bar target 50%; next bar open simulation |
| v1 | breakout_8 AND reversion_12 | 10000.00 | 0.00 | 대기 /  / 새 신호 대기 |
| v1 | breakout_8 + reversion_12 | 9957.75 | -42.25 | sell /  / breakout_8 + reversion_12: prior completed bar target 0%; next bar open simulation |
| v1 | breakout_8 AND volume_26 | 10035.68 | 35.68 | sell /  / breakout_8 AND volume_26: prior completed bar target 0%; next bar open simulation |
| v1 | breakout_8 + volume_26 | 9975.44 | -24.56 | sell /  / breakout_8 + volume_26: prior completed bar target 0%; next bar open simulation |
| v1 | reversion_12 AND volume_26 | 10000.00 | 0.00 | 대기 /  / 새 신호 대기 |
| v1 | reversion_12 + volume_26 | 10017.88 | 17.88 | sell /  / reversion_12 + volume_26: prior completed bar target 0%; next bar open simulation |
| v1 | ema_12_26 | 10041.10 | 41.10 | buy /  / EMA12 > EMA26; 조건 충족; EMA12=334.708, EMA26=334.451 |
| v1 | macd_12_26_9 | 10041.10 | 41.10 | buy /  / MACD > 신호선 그리고 MACD > 0; 조건 충족; MACD=0.256679, signal9=0.133159 |
| v1 | rsi_14_recovery | 10000.00 | 0.00 | 대기 /  / 새 신호 대기 |
| v1 | bollinger_20_reentry | 10000.00 | 0.00 | 대기 /  / 새 신호 대기 |
| v1 | donchian_20 | 9872.30 | -127.70 | sell /  / 종가 > 현재 봉을 제외한 직전 20봉 최고가; 조건 미충족; close=343.037, prior_high20=344.4 |
| v1 | atr_14_breakout | 9886.92 | -113.08 | sell /  / 종가 > 직전 종가 + 직전 ATR14 그리고 종가 > EMA26; 조건 미충족; close=342.515, threshold=344.598, prior_ATR14=1.50332, EMA26=336.975 |
| v1 | session_vwap | 9955.26 | -44.74 | buy /  / 종가 > 뉴욕 거래일별 누적 전형가격 VWAP; 조건 충족; close=343.095, session_VWAP=341.805, session_volume=2.19743e+06 |
| v1 | obv_20 | 10041.10 | 41.10 | buy /  / OBV > OBV의 SMA20 그리고 종가 > EMA26; 조건 충족; OBV=-1.09065e+07, OBV_SMA20=-1.16181e+07, close=335.52, EMA26=334.451 |
| v1 | stochastic_14_3_recovery | 10000.00 | 0.00 | 대기 /  / 새 신호 대기 |
| v1 | mfi_14_recovery | 10000.00 | 0.00 | 대기 /  / 새 신호 대기 |
| v1 | adx_14_trend | 9947.45 | -52.55 | buy /  / Wilder ADX14 >= 25 그리고 +DI14 > -DI14; 조건 충족; ADX14=26.8739, plus_DI14=46.4083, minus_DI14=10.993 |
| v1 | aroon_25_trend | 9965.46 | -34.54 | buy /  / Aroon25 Up > 70 그리고 Down < 30 (동률이면 최신 극값); 조건 충족; Aroon_up=100, Aroon_down=4 |
| v1 | cci_20_momentum | 10050.62 | 50.62 | sell /  / CCI20 > 100 (전형가격·평균절대편차); 조건 미충족; CCI20=93.5627 |
| v1 | williams_14_recovery | 10000.00 | 0.00 | 대기 /  / 새 신호 대기 |
| v1 | cmf_20_accumulation | 9965.46 | -34.54 | buy /  / Chaikin Money Flow20 > 0.1; 조건 충족; CMF20=0.219142, volume20=5.48047e+06 |
| v1 | chaikin_3_10 | 10041.10 | 41.10 | buy /  / ADL의 EMA3 - EMA10 > 0 그리고 종가 > EMA26; 조건 충족; Chaikin3_10=213543, ADL=-5.96061e+06, close=335.52, EMA26=334.451 |
| v1 | roc_10_momentum | 9965.46 | -34.54 | buy /  / 10봉 ROC > 1% 그리고 종가 > EMA26; 조건 충족; ROC10_percent=2.4431, close=342.58, EMA26=335.053 |
| v1 | trix_15_trend | 10041.10 | 41.10 | buy /  / 15봉 삼중 EMA의 1봉 변화율 TRIX > 0 그리고 종가 > EMA26; 조건 충족; TRIX15_percent=0.00554135, close=335.52, EMA26=334.451 |
| v1 | keltner_20_breakout | 9965.46 | -34.54 | buy /  / 종가 > EMA20 + 2 x Wilder ATR14; 조건 충족; close=342.58, upper_Keltner=338.352, EMA20=335.297, ATR14=1.5272 |
| v1 | opening_range_30m | 9927.81 | -72.19 | sell /  / 뉴욕 09:30·09:45 두 완료 봉 최고가를 10:00 이후 종가가 돌파; 조건 미충족; close=343.037, opening_high=343.75 |
| v2 | cash | 10000.00 | 0.00 | 대기 /  / 새 신호 대기 |
| v2 | buy_hold | 10208.88 | 208.88 | buy / partial / 직전 완료 봉 목표 비중 100%; 다음 봉 시가 가정 |
| v2 | trend_8_26 | 10049.32 | 49.32 | buy / partial / 직전 완료 봉 목표 비중 100%; 다음 봉 시가 가정 |
| v2 | momentum_26 | 9543.71 | -456.29 | buy / partial / 직전 완료 봉 목표 비중 100%; 다음 봉 시가 가정 |
| v2 | breakout_8 | 9251.20 | -748.80 | sell / filled / 직전 완료 봉 목표 비중 0%; 다음 봉 시가 가정 |
| v2 | reversion_12 | 9991.97 | -8.03 | sell / filled / 직전 완료 봉 목표 비중 0%; 다음 봉 시가 가정 |
| v2 | volume_26 | 9859.79 | -140.21 | sell / filled / 직전 완료 봉 목표 비중 0%; 다음 봉 시가 가정 |
| v2 | trend_8_26 AND momentum_26 | 10008.08 | 8.08 | buy / partial / 직전 완료 봉 목표 비중 100%; 다음 봉 시가 가정 |
| v2 | trend_8_26 + momentum_26 | 9814.38 | -185.62 | buy / partial / 직전 완료 봉 목표 비중 100%; 다음 봉 시가 가정 |
| v2 | trend_8_26 AND breakout_8 | 9287.76 | -712.24 | sell / filled / 직전 완료 봉 목표 비중 0%; 다음 봉 시가 가정 |
| v2 | trend_8_26 + breakout_8 | 9643.17 | -356.83 | sell / filled / 직전 완료 봉 목표 비중 50%; 다음 봉 시가 가정 |
| v2 | trend_8_26 AND reversion_12 | 9981.61 | -18.39 | sell / filled / 직전 완료 봉 목표 비중 0%; 다음 봉 시가 가정 |
| v2 | trend_8_26 + reversion_12 | 10063.04 | 63.04 | buy / filled / 직전 완료 봉 목표 비중 50%; 다음 봉 시가 가정 |
| v2 | trend_8_26 AND volume_26 | 9833.30 | -166.70 | sell / filled / 직전 완료 봉 목표 비중 0%; 다음 봉 시가 가정 |
| v2 | trend_8_26 + volume_26 | 9954.94 | -45.06 | buy / filled / 직전 완료 봉 목표 비중 50%; 다음 봉 시가 가정 |
| v2 | momentum_26 AND breakout_8 | 9232.70 | -767.30 | sell / filled / 직전 완료 봉 목표 비중 0%; 다음 봉 시가 가정 |
| v2 | momentum_26 + breakout_8 | 9417.78 | -582.22 | sell / filled / 직전 완료 봉 목표 비중 50%; 다음 봉 시가 가정 |
| v2 | momentum_26 AND reversion_12 | 9950.76 | -49.24 | sell / filled / 직전 완료 봉 목표 비중 0%; 다음 봉 시가 가정 |
| v2 | momentum_26 + reversion_12 | 9889.70 | -110.30 | buy / filled / 직전 완료 봉 목표 비중 50%; 다음 봉 시가 가정 |
| v2 | momentum_26 AND volume_26 | 9833.30 | -166.70 | sell / filled / 직전 완료 봉 목표 비중 0%; 다음 봉 시가 가정 |
| v2 | momentum_26 + volume_26 | 9763.02 | -236.98 | buy / filled / 직전 완료 봉 목표 비중 50%; 다음 봉 시가 가정 |
| v2 | breakout_8 AND reversion_12 | 10000.00 | 0.00 | 대기 /  / 새 신호 대기 |
| v2 | breakout_8 + reversion_12 | 9655.22 | -344.78 | sell / filled / 직전 완료 봉 목표 비중 0%; 다음 봉 시가 가정 |
| v2 | breakout_8 AND volume_26 | 9926.66 | -73.34 | sell / filled / 직전 완료 봉 목표 비중 0%; 다음 봉 시가 가정 |
| v2 | breakout_8 + volume_26 | 9570.88 | -429.12 | sell / filled / 직전 완료 봉 목표 비중 0%; 다음 봉 시가 가정 |
| v2 | reversion_12 AND volume_26 | 10051.38 | 51.38 | sell / filled / 직전 완료 봉 목표 비중 0%; 다음 봉 시가 가정 |
| v2 | reversion_12 + volume_26 | 9946.87 | -53.13 | sell / filled / 직전 완료 봉 목표 비중 0%; 다음 봉 시가 가정 |
| v2 | ema_12_26 | 10040.10 | 40.10 | buy / partial / EMA12 > EMA26; 조건 충족; EMA12=334.708, EMA26=334.451; 직전 완료 봉 목표를 다음 봉 시가에 모의 적용 |
| v2 | macd_12_26_9 | 10040.10 | 40.10 | buy / partial / MACD > 신호선 그리고 MACD > 0; 조건 충족; MACD=0.256679, signal9=0.133159; 직전 완료 봉 목표를 다음 봉 시가에 모의 적용 |
| v2 | rsi_14_recovery | 10000.00 | 0.00 | 대기 /  / 새 신호 대기 |
| v2 | bollinger_20_reentry | 10000.00 | 0.00 | 대기 /  / 새 신호 대기 |
| v2 | donchian_20 | 9868.35 | -131.65 | sell / filled / 종가 > 현재 봉을 제외한 직전 20봉 최고가; 조건 미충족; close=343.037, prior_high20=344.4; 직전 완료 봉 목표를 다음 봉 시가에 모의 적용 |
| v2 | atr_14_breakout | 9882.97 | -117.03 | sell / filled / 종가 > 직전 종가 + 직전 ATR14 그리고 종가 > EMA26; 조건 미충족; close=342.515, threshold=344.598, prior_ATR14=1.50332, EMA26=336.975; 직전 완료 봉 목표를 다음 봉 시가에 모의 적용 |
| v2 | session_vwap | 9952.27 | -47.73 | buy / partial / 종가 > 뉴욕 거래일별 누적 전형가격 VWAP; 조건 충족; close=343.095, session_VWAP=341.805, session_volume=2.19743e+06; 직전 완료 봉 목표를 다음 봉 시가에 모의 적용 |
| v2 | obv_20 | 10040.10 | 40.10 | buy / partial / OBV > OBV의 SMA20 그리고 종가 > EMA26; 조건 충족; OBV=-1.09065e+07, OBV_SMA20=-1.16181e+07, close=335.52, EMA26=334.451; 직전 완료 봉 목표를 다음 봉 시가에 모의 적용 |
| v2 | stochastic_14_3_recovery | 10000.00 | 0.00 | 대기 /  / 새 신호 대기 |
| v2 | mfi_14_recovery | 10000.00 | 0.00 | 대기 /  / 새 신호 대기 |
| v2 | adx_14_trend | 9946.46 | -53.54 | buy / partial / Wilder ADX14 >= 25 그리고 +DI14 > -DI14; 조건 충족; ADX14=26.8739, plus_DI14=46.4083, minus_DI14=10.993; 직전 완료 봉 목표를 다음 봉 시가에 모의 적용 |
| v2 | aroon_25_trend | 9964.46 | -35.54 | buy / partial / Aroon25 Up > 70 그리고 Down < 30 (동률이면 최신 극값); 조건 충족; Aroon_up=100, Aroon_down=4; 직전 완료 봉 목표를 다음 봉 시가에 모의 적용 |
| v2 | cci_20_momentum | 10048.61 | 48.61 | sell / filled / CCI20 > 100 (전형가격·평균절대편차); 조건 미충족; CCI20=93.5627; 직전 완료 봉 목표를 다음 봉 시가에 모의 적용 |
| v2 | williams_14_recovery | 10000.00 | 0.00 | 대기 /  / 새 신호 대기 |
| v2 | cmf_20_accumulation | 9964.46 | -35.54 | buy / partial / Chaikin Money Flow20 > 0.1; 조건 충족; CMF20=0.219142, volume20=5.48047e+06; 직전 완료 봉 목표를 다음 봉 시가에 모의 적용 |
| v2 | chaikin_3_10 | 10040.10 | 40.10 | buy / partial / ADL의 EMA3 - EMA10 > 0 그리고 종가 > EMA26; 조건 충족; Chaikin3_10=213543, ADL=-5.96061e+06, close=335.52, EMA26=334.451; 직전 완료 봉 목표를 다음 봉 시가에 모의 적용 |
| v2 | roc_10_momentum | 9964.46 | -35.54 | buy / partial / 10봉 ROC > 1% 그리고 종가 > EMA26; 조건 충족; ROC10_percent=2.4431, close=342.58, EMA26=335.053; 직전 완료 봉 목표를 다음 봉 시가에 모의 적용 |
| v2 | trix_15_trend | 10040.10 | 40.10 | buy / partial / 15봉 삼중 EMA의 1봉 변화율 TRIX > 0 그리고 종가 > EMA26; 조건 충족; TRIX15_percent=0.00554135, close=335.52, EMA26=334.451; 직전 완료 봉 목표를 다음 봉 시가에 모의 적용 |
| v2 | keltner_20_breakout | 9964.46 | -35.54 | buy / partial / 종가 > EMA20 + 2 x Wilder ATR14; 조건 충족; close=342.58, upper_Keltner=338.352, EMA20=335.297, ATR14=1.5272; 직전 완료 봉 목표를 다음 봉 시가에 모의 적용 |
| v2 | opening_range_30m | 9925.82 | -74.18 | sell / filled / 뉴욕 09:30·09:45 두 완료 봉 최고가를 10:00 이후 종가가 돌파; 조건 미충족; close=343.037, opening_high=343.75; 직전 완료 봉 목표를 다음 봉 시가에 모의 적용 |

### 같은 기간의 비용·노출 비교 (사후 연구)

| 전략 | 비용 전 | 비용 후 | 100% 보유 | 같은 평균 노출 보유 | 평균 노출 |
|---|---:|---:|---:|---:|---:|
| cash | 0.00% | 0.00% | -0.21% | -0.00% | 0.00% |
| buy_hold | 0.21% | -0.21% | -0.21% | -0.21% | 100.00% |
| trend_8_26 | 1.76% | -2.43% | -0.21% | -0.11% | 52.24% |
| momentum_26 | -1.33% | -8.13% | -0.21% | -0.10% | 46.70% |
| breakout_8 | -3.78% | -19.00% | -0.21% | -0.04% | 20.32% |
| reversion_12 | 4.63% | -9.67% | -0.21% | -0.06% | 26.65% |
| volume_26 | -0.11% | -6.20% | -0.21% | -0.01% | 6.86% |
| trend_8_26 AND momentum_26 | 1.85% | -3.15% | -0.21% | -0.09% | 40.90% |
| trend_8_26 + momentum_26 | 0.21% | -5.11% | -0.21% | -0.10% | 49.48% |
| trend_8_26 AND breakout_8 | -3.83% | -14.50% | -0.21% | -0.03% | 12.93% |
| trend_8_26 + breakout_8 | -1.03% | -10.90% | -0.21% | -0.08% | 36.29% |
| trend_8_26 AND reversion_12 | 2.82% | -3.46% | -0.21% | -0.01% | 6.60% |
| trend_8_26 + reversion_12 | 3.21% | -5.53% | -0.21% | -0.08% | 39.45% |
| trend_8_26 AND volume_26 | -0.58% | -4.67% | -0.21% | -0.01% | 4.22% |
| trend_8_26 + volume_26 | 0.84% | -4.33% | -0.21% | -0.06% | 29.55% |
| momentum_26 AND breakout_8 | -2.67% | -13.47% | -0.21% | -0.03% | 12.66% |
| momentum_26 + breakout_8 | -2.54% | -13.54% | -0.21% | -0.07% | 33.52% |
| momentum_26 AND reversion_12 | 2.89% | -3.80% | -0.21% | -0.01% | 5.54% |
| momentum_26 + reversion_12 | 1.64% | -7.36% | -0.21% | -0.08% | 36.68% |
| momentum_26 AND volume_26 | 0.21% | -2.70% | -0.21% | -0.01% | 2.90% |
| momentum_26 + volume_26 | -0.69% | -6.57% | -0.21% | -0.06% | 26.79% |
| breakout_8 AND reversion_12 | 0.00% | 0.00% | -0.21% | -0.00% | 0.00% |
| breakout_8 + reversion_12 | 0.36% | -13.02% | -0.21% | -0.05% | 23.49% |
| breakout_8 AND volume_26 | -0.51% | -2.17% | -0.21% | -0.00% | 1.06% |
| breakout_8 + volume_26 | -1.95% | -11.73% | -0.21% | -0.03% | 13.60% |
| reversion_12 AND volume_26 | 1.25% | -2.10% | -0.21% | -0.01% | 3.43% |
| reversion_12 + volume_26 | 2.25% | -7.18% | -0.21% | -0.04% | 16.76% |
| ema_12_26 | 1.41% | -1.94% | -0.21% | -0.10% | 48.55% |
| macd_12_26_9 | 1.31% | -2.86% | -0.21% | -0.06% | 30.34% |
| rsi_14_recovery | 0.14% | -2.35% | -0.21% | -0.00% | 1.58% |
| bollinger_20_reentry | 0.44% | -5.30% | -0.21% | -0.01% | 3.69% |
| donchian_20 | -1.79% | -4.63% | -0.21% | -0.01% | 2.90% |
| atr_14_breakout | -1.13% | -7.55% | -0.21% | -0.01% | 4.49% |
| session_vwap | 1.11% | -8.58% | -0.21% | -0.10% | 49.34% |
| obv_20 | -3.73% | -14.77% | -0.21% | -0.07% | 31.66% |
| stochastic_14_3_recovery | -1.86% | -12.75% | -0.21% | -0.02% | 7.39% |
| mfi_14_recovery | 0.16% | -1.50% | -0.21% | -0.00% | 1.06% |
| adx_14_trend | -1.85% | -5.09% | -0.21% | -0.06% | 27.70% |
| aroon_25_trend | -0.41% | -4.90% | -0.21% | -0.05% | 21.64% |
| cci_20_momentum | -2.59% | -10.44% | -0.21% | -0.03% | 15.30% |
| williams_14_recovery | -2.54% | -12.98% | -0.21% | -0.02% | 7.12% |
| cmf_20_accumulation | -2.70% | -11.29% | -0.21% | -0.07% | 35.09% |
| chaikin_3_10 | 1.80% | -6.79% | -0.21% | -0.07% | 34.56% |
| roc_10_momentum | -0.67% | -3.14% | -0.21% | -0.02% | 7.39% |
| trix_15_trend | 0.37% | -6.55% | -0.21% | -0.07% | 34.83% |
| keltner_20_breakout | -1.21% | -3.66% | -0.21% | -0.01% | 3.96% |
| opening_range_30m | -0.21% | -3.91% | -0.21% | -0.04% | 18.47% |

동일 구간·초기 자금, 종료 시 청산 비용 포함. 노출 맞춤은 사후 설명용이며 v2 실제 계좌 성과가 아닙니다.
[낙폭 분해·비용 영향·전체 구간](JPM/comparison.json)

[v1 전체 기록](JPM/accounts.json) · [v2 전체 기록](JPM/accounts-v2.json)

## XOM 계좌

| 모델 | 전략 | 평가액 USD | 손익 USD | 최근 매매·이유 |
|---|---|---:|---:|---|
| v1 | cash | 10000.00 | 0.00 | 대기 /  / 새 신호 대기 |
| v1 | buy_hold | 9943.56 | -56.44 | buy /  / buy_hold: prior completed bar target 100%; next bar open simulation |
| v1 | trend_8_26 | 10003.92 | 3.92 | buy /  / trend_8_26: prior completed bar target 100%; next bar open simulation |
| v1 | momentum_26 | 9970.96 | -29.04 | buy /  / momentum_26: prior completed bar target 100%; next bar open simulation |
| v1 | breakout_8 | 9826.90 | -173.10 | sell /  / breakout_8: prior completed bar target 0%; next bar open simulation |
| v1 | reversion_12 | 10000.00 | 0.00 | 대기 /  / 새 신호 대기 |
| v1 | volume_26 | 9903.93 | -96.07 | sell /  / volume_26: prior completed bar target 0%; next bar open simulation |
| v1 | trend_8_26 AND momentum_26 | 10003.92 | 3.92 | buy /  / trend_8_26 AND momentum_26: prior completed bar target 100%; next bar open simulation |
| v1 | trend_8_26 + momentum_26 | 9987.41 | -12.59 | buy /  / trend_8_26 + momentum_26: prior completed bar target 100%; next bar open simulation |
| v1 | trend_8_26 AND breakout_8 | 9948.21 | -51.79 | sell /  / trend_8_26 AND breakout_8: prior completed bar target 0%; next bar open simulation |
| v1 | trend_8_26 + breakout_8 | 9934.87 | -65.13 | sell /  / trend_8_26 + breakout_8: prior completed bar target 50%; next bar open simulation |
| v1 | trend_8_26 AND reversion_12 | 10000.00 | 0.00 | 대기 /  / 새 신호 대기 |
| v1 | trend_8_26 + reversion_12 | 10001.93 | 1.93 | buy /  / trend_8_26 + reversion_12: prior completed bar target 50%; next bar open simulation |
| v1 | trend_8_26 AND volume_26 | 10000.00 | 0.00 | 대기 /  / 새 신호 대기 |
| v1 | trend_8_26 + volume_26 | 9953.76 | -46.24 | buy /  / trend_8_26 + volume_26: prior completed bar target 50%; next bar open simulation |
| v1 | momentum_26 AND breakout_8 | 9875.85 | -124.15 | sell /  / momentum_26 AND breakout_8: prior completed bar target 0%; next bar open simulation |
| v1 | momentum_26 + breakout_8 | 9898.69 | -101.31 | sell /  / momentum_26 + breakout_8: prior completed bar target 50%; next bar open simulation |
| v1 | momentum_26 AND reversion_12 | 10000.00 | 0.00 | 대기 /  / 새 신호 대기 |
| v1 | momentum_26 + reversion_12 | 9985.44 | -14.56 | buy /  / momentum_26 + reversion_12: prior completed bar target 50%; next bar open simulation |
| v1 | momentum_26 AND volume_26 | 10000.00 | 0.00 | 대기 /  / 새 신호 대기 |
| v1 | momentum_26 + volume_26 | 9937.34 | -62.66 | buy /  / momentum_26 + volume_26: prior completed bar target 50%; next bar open simulation |
| v1 | breakout_8 AND reversion_12 | 10000.00 | 0.00 | 대기 /  / 새 신호 대기 |
| v1 | breakout_8 + reversion_12 | 9913.03 | -86.97 | sell /  / breakout_8 + reversion_12: prior completed bar target 0%; next bar open simulation |
| v1 | breakout_8 AND volume_26 | 9950.44 | -49.56 | sell /  / breakout_8 AND volume_26: prior completed bar target 0%; next bar open simulation |
| v1 | breakout_8 + volume_26 | 9865.30 | -134.70 | sell /  / breakout_8 + volume_26: prior completed bar target 0%; next bar open simulation |
| v1 | reversion_12 AND volume_26 | 10000.00 | 0.00 | 대기 /  / 새 신호 대기 |
| v1 | reversion_12 + volume_26 | 9951.83 | -48.17 | sell /  / reversion_12 + volume_26: prior completed bar target 0%; next bar open simulation |
| v1 | ema_12_26 | 10001.07 | 1.07 | buy /  / EMA12 > EMA26; 조건 충족; EMA12=175.145, EMA26=175.141 |
| v1 | macd_12_26_9 | 10001.07 | 1.07 | buy /  / MACD > 신호선 그리고 MACD > 0; 조건 충족; MACD=0.00418876, signal9=-0.17046 |
| v1 | rsi_14_recovery | 10000.00 | 0.00 | 대기 /  / 새 신호 대기 |
| v1 | bollinger_20_reentry | 9913.52 | -86.48 | sell /  / 직전 종가 < 직전 하단밴드, 현재 하단밴드 <= 종가 <= SMA20 (한 봉 목표); 조건 미충족; close=175.71, lower20=173.907, SMA20=174.743, previous_lower20=173.977 |
| v1 | donchian_20 | 9950.44 | -49.56 | sell /  / 종가 > 현재 봉을 제외한 직전 20봉 최고가; 조건 미충족; close=175.56, prior_high20=177.365 |
| v1 | atr_14_breakout | 9898.91 | -101.09 | sell /  / 종가 > 직전 종가 + 직전 ATR14 그리고 종가 > EMA26; 조건 미충족; close=176, threshold=176.983, prior_ATR14=0.731315, EMA26=175.281 |
| v1 | session_vwap | 9948.21 | -51.79 | sell /  / 종가 > 뉴욕 거래일별 누적 전형가격 VWAP; 조건 미충족; close=176, session_VWAP=176.01, session_volume=3.42523e+06 |
| v1 | obv_20 | 9990.26 | -9.74 | buy /  / OBV > OBV의 SMA20 그리고 종가 > EMA26; 조건 충족; OBV=2.28535e+07, OBV_SMA20=2.0753e+07, close=175.71, EMA26=174.973 |
| v1 | stochastic_14_3_recovery | 10000.00 | 0.00 | 대기 /  / 새 신호 대기 |
| v1 | mfi_14_recovery | 10000.00 | 0.00 | 대기 /  / 새 신호 대기 |
| v1 | adx_14_trend | 10000.00 | 0.00 | 대기 /  / 새 신호 대기 |
| v1 | aroon_25_trend | 10000.00 | 0.00 | 대기 /  / 새 신호 대기 |
| v1 | cci_20_momentum | 9888.78 | -111.22 | sell /  / CCI20 > 100 (전형가격·평균절대편차); 조건 미충족; CCI20=92.2568 |
| v1 | williams_14_recovery | 9913.52 | -86.48 | sell /  / 직전 Williams %R14 < -80, 현재 >= -80 (한 봉 목표); 조건 미충족; Williams_R14=-43.9575, previous_R14=-33.1215 |
| v1 | cmf_20_accumulation | 10000.00 | 0.00 | 대기 /  / 새 신호 대기 |
| v1 | chaikin_3_10 | 10000.00 | 0.00 | 대기 /  / 새 신호 대기 |
| v1 | roc_10_momentum | 9978.33 | -21.67 | buy /  / 10봉 ROC > 1% 그리고 종가 > EMA26; 조건 충족; ROC10_percent=1.09227, close=175.85, EMA26=175.323 |
| v1 | trix_15_trend | 10000.00 | 0.00 | 대기 /  / 새 신호 대기 |
| v1 | keltner_20_breakout | 10000.00 | 0.00 | 대기 /  / 새 신호 대기 |
| v1 | opening_range_30m | 10000.00 | 0.00 | 대기 /  / 새 신호 대기 |
| v2 | cash | 10000.00 | 0.00 | 대기 /  / 새 신호 대기 |
| v2 | buy_hold | 10260.88 | 260.88 | buy / partial / 직전 완료 봉 목표 비중 100%; 다음 봉 시가 가정 |
| v2 | trend_8_26 | 10099.21 | 99.21 | buy / partial / 직전 완료 봉 목표 비중 100%; 다음 봉 시가 가정 |
| v2 | momentum_26 | 10142.08 | 142.08 | buy / partial / 직전 완료 봉 목표 비중 100%; 다음 봉 시가 가정 |
| v2 | breakout_8 | 9301.50 | -698.50 | sell / filled / 직전 완료 봉 목표 비중 0%; 다음 봉 시가 가정 |
| v2 | reversion_12 | 9815.06 | -184.94 | sell / filled / 직전 완료 봉 목표 비중 0%; 다음 봉 시가 가정 |
| v2 | volume_26 | 9810.89 | -189.11 | sell / filled / 직전 완료 봉 목표 비중 0%; 다음 봉 시가 가정 |
| v2 | trend_8_26 AND momentum_26 | 10106.69 | 106.69 | buy / partial / 직전 완료 봉 목표 비중 100%; 다음 봉 시가 가정 |
| v2 | trend_8_26 + momentum_26 | 10120.63 | 120.63 | buy / partial / 직전 완료 봉 목표 비중 100%; 다음 봉 시가 가정 |
| v2 | trend_8_26 AND breakout_8 | 9402.89 | -597.11 | sell / filled / 직전 완료 봉 목표 비중 0%; 다음 봉 시가 가정 |
| v2 | trend_8_26 + breakout_8 | 9733.31 | -266.69 | sell / filled / 직전 완료 봉 목표 비중 50%; 다음 봉 시가 가정 |
| v2 | trend_8_26 AND reversion_12 | 9839.70 | -160.30 | sell / filled / 직전 완료 봉 목표 비중 0%; 다음 봉 시가 가정 |
| v2 | trend_8_26 + reversion_12 | 9956.18 | -43.82 | buy / filled / 직전 완료 봉 목표 비중 50%; 다음 봉 시가 가정 |
| v2 | trend_8_26 AND volume_26 | 9895.61 | -104.39 | sell / filled / 직전 완료 봉 목표 비중 0%; 다음 봉 시가 가정 |
| v2 | trend_8_26 + volume_26 | 9953.91 | -46.09 | buy / filled / 직전 완료 봉 목표 비중 50%; 다음 봉 시가 가정 |
| v2 | momentum_26 AND breakout_8 | 9349.69 | -650.31 | sell / filled / 직전 완료 봉 목표 비중 0%; 다음 봉 시가 가정 |
| v2 | momentum_26 + breakout_8 | 9713.26 | -286.74 | sell / filled / 직전 완료 봉 목표 비중 50%; 다음 봉 시가 가정 |
| v2 | momentum_26 AND reversion_12 | 9800.13 | -199.87 | sell / filled / 직전 완료 봉 목표 비중 0%; 다음 봉 시가 가정 |
| v2 | momentum_26 + reversion_12 | 9977.33 | -22.67 | buy / filled / 직전 완료 봉 목표 비중 50%; 다음 봉 시가 가정 |
| v2 | momentum_26 AND volume_26 | 9957.96 | -42.04 | sell / filled / 직전 완료 봉 목표 비중 0%; 다음 봉 시가 가정 |
| v2 | momentum_26 + volume_26 | 9995.98 | -4.02 | buy / filled / 직전 완료 봉 목표 비중 50%; 다음 봉 시가 가정 |
| v2 | breakout_8 AND reversion_12 | 10000.00 | 0.00 | 대기 /  / 새 신호 대기 |
| v2 | breakout_8 + reversion_12 | 9554.70 | -445.30 | sell / filled / 직전 완료 봉 목표 비중 0%; 다음 봉 시가 가정 |
| v2 | breakout_8 AND volume_26 | 9918.86 | -81.14 | sell / filled / 직전 완료 봉 목표 비중 0%; 다음 봉 시가 가정 |
| v2 | breakout_8 + volume_26 | 9572.75 | -427.25 | sell / filled / 직전 완료 봉 목표 비중 0%; 다음 봉 시가 가정 |
| v2 | reversion_12 AND volume_26 | 9949.87 | -50.13 | sell / filled / 직전 완료 봉 목표 비중 0%; 다음 봉 시가 가정 |
| v2 | reversion_12 + volume_26 | 9833.62 | -166.38 | sell / filled / 직전 완료 봉 목표 비중 0%; 다음 봉 시가 가정 |
| v2 | ema_12_26 | 10000.07 | 0.07 | buy / partial / EMA12 > EMA26; 조건 충족; EMA12=175.145, EMA26=175.141; 직전 완료 봉 목표를 다음 봉 시가에 모의 적용 |
| v2 | macd_12_26_9 | 10000.07 | 0.07 | buy / partial / MACD > 신호선 그리고 MACD > 0; 조건 충족; MACD=0.00418876, signal9=-0.17046; 직전 완료 봉 목표를 다음 봉 시가에 모의 적용 |
| v2 | rsi_14_recovery | 10000.00 | 0.00 | 대기 /  / 새 신호 대기 |
| v2 | bollinger_20_reentry | 9911.54 | -88.46 | sell / filled / 직전 종가 < 직전 하단밴드, 현재 하단밴드 <= 종가 <= SMA20 (한 봉 목표); 조건 미충족; close=175.71, lower20=173.907, SMA20=174.743, previous_lower20=173.977; 직전 완료 봉 목표를 다음 봉 시가에 모의 적용 |
| v2 | donchian_20 | 9948.45 | -51.55 | sell / filled / 종가 > 현재 봉을 제외한 직전 20봉 최고가; 조건 미충족; close=175.56, prior_high20=177.365; 직전 완료 봉 목표를 다음 봉 시가에 모의 적용 |
| v2 | atr_14_breakout | 9894.95 | -105.05 | sell / filled / 종가 > 직전 종가 + 직전 ATR14 그리고 종가 > EMA26; 조건 미충족; close=176, threshold=176.983, prior_ATR14=0.731315, EMA26=175.281; 직전 완료 봉 목표를 다음 봉 시가에 모의 적용 |
| v2 | session_vwap | 9946.22 | -53.78 | sell / filled / 종가 > 뉴욕 거래일별 누적 전형가격 VWAP; 조건 미충족; close=176, session_VWAP=176.01, session_volume=3.42523e+06; 직전 완료 봉 목표를 다음 봉 시가에 모의 적용 |
| v2 | obv_20 | 9989.26 | -10.74 | buy / partial / OBV > OBV의 SMA20 그리고 종가 > EMA26; 조건 충족; OBV=2.28535e+07, OBV_SMA20=2.0753e+07, close=175.71, EMA26=174.973; 직전 완료 봉 목표를 다음 봉 시가에 모의 적용 |
| v2 | stochastic_14_3_recovery | 10000.00 | 0.00 | 대기 /  / 새 신호 대기 |
| v2 | mfi_14_recovery | 10000.00 | 0.00 | 대기 /  / 새 신호 대기 |
| v2 | adx_14_trend | 10000.00 | 0.00 | 대기 /  / 새 신호 대기 |
| v2 | aroon_25_trend | 10000.00 | 0.00 | 대기 /  / 새 신호 대기 |
| v2 | cci_20_momentum | 9884.83 | -115.17 | sell / filled / CCI20 > 100 (전형가격·평균절대편차); 조건 미충족; CCI20=92.2568; 직전 완료 봉 목표를 다음 봉 시가에 모의 적용 |
| v2 | williams_14_recovery | 9911.54 | -88.46 | sell / filled / 직전 Williams %R14 < -80, 현재 >= -80 (한 봉 목표); 조건 미충족; Williams_R14=-43.9575, previous_R14=-33.1215; 직전 완료 봉 목표를 다음 봉 시가에 모의 적용 |
| v2 | cmf_20_accumulation | 10000.00 | 0.00 | 대기 /  / 새 신호 대기 |
| v2 | chaikin_3_10 | 10000.00 | 0.00 | 대기 /  / 새 신호 대기 |
| v2 | roc_10_momentum | 9977.33 | -22.67 | buy / partial / 10봉 ROC > 1% 그리고 종가 > EMA26; 조건 충족; ROC10_percent=1.09227, close=175.85, EMA26=175.323; 직전 완료 봉 목표를 다음 봉 시가에 모의 적용 |
| v2 | trix_15_trend | 10000.00 | 0.00 | 대기 /  / 새 신호 대기 |
| v2 | keltner_20_breakout | 10000.00 | 0.00 | 대기 /  / 새 신호 대기 |
| v2 | opening_range_30m | 10000.00 | 0.00 | 대기 /  / 새 신호 대기 |

### 같은 기간의 비용·노출 비교 (사후 연구)

| 전략 | 비용 전 | 비용 후 | 100% 보유 | 같은 평균 노출 보유 | 평균 노출 |
|---|---:|---:|---:|---:|---:|
| cash | 0.00% | 0.00% | 9.14% | 0.00% | 0.00% |
| buy_hold | 9.60% | 9.14% | 9.14% | 9.14% | 100.00% |
| trend_8_26 | 1.24% | -3.33% | 9.14% | 5.80% | 64.38% |
| momentum_26 | 0.13% | -7.16% | 9.14% | 6.34% | 70.18% |
| breakout_8 | -3.43% | -21.06% | 9.14% | 2.08% | 23.48% |
| reversion_12 | 7.01% | -3.65% | 9.14% | 1.84% | 20.84% |
| volume_26 | 3.92% | -3.64% | 9.14% | 0.44% | 5.01% |
| trend_8_26 AND momentum_26 | -0.22% | -5.12% | 9.14% | 5.31% | 59.10% |
| trend_8_26 + momentum_26 | 0.69% | -5.06% | 9.14% | 6.07% | 67.29% |
| trend_8_26 AND breakout_8 | -1.31% | -15.16% | 9.14% | 1.61% | 18.21% |
| trend_8_26 + breakout_8 | -1.10% | -12.26% | 9.14% | 3.92% | 43.94% |
| trend_8_26 AND reversion_12 | 1.89% | -3.93% | 9.14% | 0.72% | 8.18% |
| trend_8_26 + reversion_12 | 4.12% | -3.29% | 9.14% | 3.80% | 42.62% |
| trend_8_26 AND volume_26 | 2.54% | -1.67% | 9.14% | 0.23% | 2.64% |
| trend_8_26 + volume_26 | 2.59% | -3.08% | 9.14% | 3.09% | 34.70% |
| momentum_26 AND breakout_8 | -3.50% | -19.44% | 9.14% | 1.87% | 21.11% |
| momentum_26 + breakout_8 | -1.65% | -14.38% | 9.14% | 4.19% | 46.84% |
| momentum_26 AND reversion_12 | 2.27% | -4.38% | 9.14% | 0.79% | 8.97% |
| momentum_26 + reversion_12 | 3.54% | -4.02% | 9.14% | 4.07% | 45.52% |
| momentum_26 AND volume_26 | 2.32% | -1.47% | 9.14% | 0.21% | 2.37% |
| momentum_26 + volume_26 | 2.03% | -4.02% | 9.14% | 3.35% | 37.60% |
| breakout_8 AND reversion_12 | 0.00% | 0.00% | 9.14% | 0.00% | 0.00% |
| breakout_8 + reversion_12 | 1.67% | -12.61% | 9.14% | 1.96% | 22.17% |
| breakout_8 AND volume_26 | 0.51% | -1.17% | 9.14% | 0.09% | 1.06% |
| breakout_8 + volume_26 | 0.19% | -11.68% | 9.14% | 1.26% | 14.26% |
| reversion_12 AND volume_26 | 1.52% | -1.00% | 9.14% | 0.14% | 1.58% |
| reversion_12 + volume_26 | 5.47% | -2.83% | 9.14% | 1.14% | 12.93% |
| ema_12_26 | -0.26% | -3.55% | 9.14% | 6.68% | 73.88% |
| macd_12_26_9 | -1.35% | -6.99% | 9.14% | 3.53% | 39.58% |
| rsi_14_recovery | -0.15% | -0.57% | 9.14% | 0.02% | 0.26% |
| bollinger_20_reentry | -0.87% | -3.75% | 9.14% | 0.16% | 1.85% |
| donchian_20 | -1.09% | -9.82% | 9.14% | 0.79% | 8.97% |
| atr_14_breakout | -1.33% | -10.41% | 9.14% | 0.56% | 6.33% |
| session_vwap | -0.96% | -12.69% | 9.14% | 5.85% | 64.91% |
| obv_20 | 2.11% | -5.32% | 9.14% | 3.82% | 42.74% |
| stochastic_14_3_recovery | 1.55% | -6.63% | 9.14% | 0.46% | 5.28% |
| mfi_14_recovery | -0.31% | -1.97% | 9.14% | 0.09% | 1.06% |
| adx_14_trend | 0.84% | -1.67% | 9.14% | 3.72% | 41.69% |
| aroon_25_trend | -1.78% | -7.78% | 9.14% | 2.72% | 30.61% |
| cci_20_momentum | 2.73% | -4.75% | 9.14% | 2.36% | 26.65% |
| williams_14_recovery | 0.08% | -5.24% | 9.14% | 0.30% | 3.43% |
| cmf_20_accumulation | 2.09% | -6.53% | 9.14% | 4.61% | 51.45% |
| chaikin_3_10 | -1.00% | -9.36% | 9.14% | 4.97% | 55.41% |
| roc_10_momentum | -0.21% | -5.91% | 9.14% | 1.21% | 13.72% |
| trix_15_trend | -2.63% | -9.34% | 9.14% | 5.55% | 61.74% |
| keltner_20_breakout | -0.86% | -7.30% | 9.14% | 1.33% | 15.04% |
| opening_range_30m | -0.36% | -9.53% | 9.14% | 3.19% | 35.88% |

동일 구간·초기 자금, 종료 시 청산 비용 포함. 노출 맞춤은 사후 설명용이며 v2 실제 계좌 성과가 아닙니다.
[낙폭 분해·비용 영향·전체 구간](XOM/comparison.json)

[v1 전체 기록](XOM/accounts.json) · [v2 전체 기록](XOM/accounts-v2.json)

## JNJ 계좌

| 모델 | 전략 | 평가액 USD | 손익 USD | 최근 매매·이유 |
|---|---|---:|---:|---|
| v1 | cash | 10000.00 | 0.00 | 대기 /  / 새 신호 대기 |
| v1 | buy_hold | 10033.15 | 33.15 | buy /  / buy_hold: prior completed bar target 100%; next bar open simulation |
| v1 | trend_8_26 | 9987.03 | -12.97 | buy /  / trend_8_26: prior completed bar target 100%; next bar open simulation |
| v1 | momentum_26 | 10000.00 | 0.00 | 대기 /  / 새 신호 대기 |
| v1 | breakout_8 | 9883.97 | -116.03 | sell /  / breakout_8: prior completed bar target 0%; next bar open simulation |
| v1 | reversion_12 | 10000.00 | 0.00 | 대기 /  / 새 신호 대기 |
| v1 | volume_26 | 9935.63 | -64.37 | sell /  / volume_26: prior completed bar target 0%; next bar open simulation |
| v1 | trend_8_26 AND momentum_26 | 10000.00 | 0.00 | 대기 /  / 새 신호 대기 |
| v1 | trend_8_26 + momentum_26 | 9993.50 | -6.50 | buy /  / trend_8_26 + momentum_26: prior completed bar target 50%; next bar open simulation |
| v1 | trend_8_26 AND breakout_8 | 10000.00 | 0.00 | 대기 /  / 새 신호 대기 |
| v1 | trend_8_26 + breakout_8 | 9935.33 | -64.67 | buy /  / trend_8_26 + breakout_8: prior completed bar target 50%; next bar open simulation |
| v1 | trend_8_26 AND reversion_12 | 10000.00 | 0.00 | 대기 /  / 새 신호 대기 |
| v1 | trend_8_26 + reversion_12 | 9993.50 | -6.50 | buy /  / trend_8_26 + reversion_12: prior completed bar target 50%; next bar open simulation |
| v1 | trend_8_26 AND volume_26 | 9935.63 | -64.37 | sell /  / trend_8_26 AND volume_26: prior completed bar target 0%; next bar open simulation |
| v1 | trend_8_26 + volume_26 | 9961.33 | -38.67 | sell /  / trend_8_26 + volume_26: prior completed bar target 50%; next bar open simulation |
| v1 | momentum_26 AND breakout_8 | 10000.00 | 0.00 | 대기 /  / 새 신호 대기 |
| v1 | momentum_26 + breakout_8 | 9941.79 | -58.21 | sell /  / momentum_26 + breakout_8: prior completed bar target 0%; next bar open simulation |
| v1 | momentum_26 AND reversion_12 | 10000.00 | 0.00 | 대기 /  / 새 신호 대기 |
| v1 | momentum_26 + reversion_12 | 10000.00 | 0.00 | 대기 /  / 새 신호 대기 |
| v1 | momentum_26 AND volume_26 | 10000.00 | 0.00 | 대기 /  / 새 신호 대기 |
| v1 | momentum_26 + volume_26 | 9967.75 | -32.25 | sell /  / momentum_26 + volume_26: prior completed bar target 0%; next bar open simulation |
| v1 | breakout_8 AND reversion_12 | 10000.00 | 0.00 | 대기 /  / 새 신호 대기 |
| v1 | breakout_8 + reversion_12 | 9941.79 | -58.21 | sell /  / breakout_8 + reversion_12: prior completed bar target 0%; next bar open simulation |
| v1 | breakout_8 AND volume_26 | 10000.00 | 0.00 | 대기 /  / 새 신호 대기 |
| v1 | breakout_8 + volume_26 | 9909.73 | -90.27 | sell /  / breakout_8 + volume_26: prior completed bar target 0%; next bar open simulation |
| v1 | reversion_12 AND volume_26 | 10000.00 | 0.00 | 대기 /  / 새 신호 대기 |
| v1 | reversion_12 + volume_26 | 9967.75 | -32.25 | sell /  / reversion_12 + volume_26: prior completed bar target 0%; next bar open simulation |
| v1 | ema_12_26 | 9986.44 | -13.56 | buy /  / EMA12 > EMA26; 조건 충족; EMA12=255.218, EMA26=255.146 |
| v1 | macd_12_26_9 | 9986.44 | -13.56 | buy /  / MACD > 신호선 그리고 MACD > 0; 조건 충족; MACD=0.0719144, signal9=-0.171173 |
| v1 | rsi_14_recovery | 10000.00 | 0.00 | 대기 /  / 새 신호 대기 |
| v1 | bollinger_20_reentry | 10000.00 | 0.00 | 대기 /  / 새 신호 대기 |
| v1 | donchian_20 | 10000.00 | 0.00 | 대기 /  / 새 신호 대기 |
| v1 | atr_14_breakout | 9883.97 | -116.03 | sell /  / 종가 > 직전 종가 + 직전 ATR14 그리고 종가 > EMA26; 조건 미충족; close=256.72, threshold=258.136, prior_ATR14=1.3158, EMA26=255.146 |
| v1 | session_vwap | 9854.90 | -145.10 | sell /  / 종가 > 뉴욕 거래일별 누적 전형가격 VWAP; 조건 미충족; close=255.96, session_VWAP=256.469, session_volume=3.61081e+06 |
| v1 | obv_20 | 9991.31 | -8.69 | buy /  / OBV > OBV의 SMA20 그리고 종가 > EMA26; 조건 충족; OBV=6.12774e+06, OBV_SMA20=4.45241e+06, close=256.69, EMA26=255.435 |
| v1 | stochastic_14_3_recovery | 9927.65 | -72.35 | sell /  / 직전 %K14 < 20에서 %K14가 %D3 상향 돌파 (한 봉 목표); 조건 미충족; K14=60.1505, D3=50.3645, previous_K14=74.7605, previous_D3=37.7141 |
| v1 | mfi_14_recovery | 10000.00 | 0.00 | 대기 /  / 새 신호 대기 |
| v1 | adx_14_trend | 9823.79 | -176.21 | sell /  / Wilder ADX14 >= 25 그리고 +DI14 > -DI14; 조건 미충족; ADX14=24.7842, plus_DI14=27.3963, minus_DI14=19.1477 |
| v1 | aroon_25_trend | 10000.00 | 0.00 | 대기 /  / 새 신호 대기 |
| v1 | cci_20_momentum | 9935.63 | -64.37 | sell /  / CCI20 > 100 (전형가격·평균절대편차); 조건 미충족; CCI20=62.9489 |
| v1 | williams_14_recovery | 9927.65 | -72.35 | sell /  / 직전 Williams %R14 < -80, 현재 >= -80 (한 봉 목표); 조건 미충족; Williams_R14=-39.8495, previous_R14=-25.2395 |
| v1 | cmf_20_accumulation | 10000.00 | 0.00 | 대기 /  / 새 신호 대기 |
| v1 | chaikin_3_10 | 10000.00 | 0.00 | 대기 /  / 새 신호 대기 |
| v1 | roc_10_momentum | 9926.73 | -73.27 | sell /  / 10봉 ROC > 1% 그리고 종가 > EMA26; 조건 미충족; ROC10_percent=0.735964, close=255.96, EMA26=255.474 |
| v1 | trix_15_trend | 10000.00 | 0.00 | 대기 /  / 새 신호 대기 |
| v1 | keltner_20_breakout | 10000.00 | 0.00 | 대기 /  / 새 신호 대기 |
| v1 | opening_range_30m | 10000.00 | 0.00 | 대기 /  / 새 신호 대기 |
| v2 | cash | 10000.00 | 0.00 | 대기 /  / 새 신호 대기 |
| v2 | buy_hold | 9798.98 | -201.02 | 중단: 손실 한도 / buy / partial / 직전 완료 봉 목표 비중 100%; 다음 봉 시가 가정 |
| v2 | trend_8_26 | 9798.98 | -201.02 | 중단: 손실 한도 / buy / partial / 직전 완료 봉 목표 비중 100%; 다음 봉 시가 가정 |
| v2 | momentum_26 | 9798.98 | -201.02 | 중단: 손실 한도 / buy / partial / 직전 완료 봉 목표 비중 100%; 다음 봉 시가 가정 |
| v2 | breakout_8 | 9343.39 | -656.61 | 중단: 손실 한도 / sell / filled / 직전 완료 봉 목표 비중 0%; 다음 봉 시가 가정 |
| v2 | reversion_12 | 9690.14 | -309.86 | sell / filled / 직전 완료 봉 목표 비중 0%; 다음 봉 시가 가정 |
| v2 | volume_26 | 9726.38 | -273.62 | sell / filled / 직전 완료 봉 목표 비중 0%; 다음 봉 시가 가정 |
| v2 | trend_8_26 AND momentum_26 | 9798.98 | -201.02 | 중단: 손실 한도 / buy / partial / 직전 완료 봉 목표 비중 100%; 다음 봉 시가 가정 |
| v2 | trend_8_26 + momentum_26 | 9798.98 | -201.02 | 중단: 손실 한도 / buy / partial / 직전 완료 봉 목표 비중 100%; 다음 봉 시가 가정 |
| v2 | trend_8_26 AND breakout_8 | 9419.39 | -580.61 | 중단: 손실 한도 / sell / filled / 직전 완료 봉 목표 비중 0%; 다음 봉 시가 가정 |
| v2 | trend_8_26 + breakout_8 | 9505.55 | -494.45 | buy / filled / 직전 완료 봉 목표 비중 50%; 다음 봉 시가 가정 |
| v2 | trend_8_26 AND reversion_12 | 9978.08 | -21.92 | sell / filled / 직전 완료 봉 목표 비중 0%; 다음 봉 시가 가정 |
| v2 | trend_8_26 + reversion_12 | 9732.92 | -267.08 | 중단: 손실 한도 / sell / filled / 직전 완료 봉 목표 비중 0%; 다음 봉 시가 가정 |
| v2 | trend_8_26 AND volume_26 | 9805.21 | -194.79 | sell / filled / 직전 완료 봉 목표 비중 0%; 다음 봉 시가 가정 |
| v2 | trend_8_26 + volume_26 | 9873.44 | -126.56 | 중단: 손실 한도 / buy / filled / 직전 완료 봉 목표 비중 50%; 다음 봉 시가 가정 |
| v2 | momentum_26 AND breakout_8 | 9598.70 | -401.30 | sell / filled / 직전 완료 봉 목표 비중 0%; 다음 봉 시가 가정 |
| v2 | momentum_26 + breakout_8 | 9503.27 | -496.73 | sell / filled / 직전 완료 봉 목표 비중 0%; 다음 봉 시가 가정 |
| v2 | momentum_26 AND reversion_12 | 9938.87 | -61.13 | sell / filled / 직전 완료 봉 목표 비중 0%; 다음 봉 시가 가정 |
| v2 | momentum_26 + reversion_12 | 9732.92 | -267.08 | 중단: 손실 한도 / sell / filled / 직전 완료 봉 목표 비중 0%; 다음 봉 시가 가정 |
| v2 | momentum_26 AND volume_26 | 9920.93 | -79.07 | sell / filled / 직전 완료 봉 목표 비중 0%; 다음 봉 시가 가정 |
| v2 | momentum_26 + volume_26 | 9873.44 | -126.56 | 중단: 손실 한도 / buy / filled / 직전 완료 봉 목표 비중 50%; 다음 봉 시가 가정 |
| v2 | breakout_8 AND reversion_12 | 10000.00 | 0.00 | 대기 /  / 새 신호 대기 |
| v2 | breakout_8 + reversion_12 | 9523.40 | -476.60 | sell / filled / 직전 완료 봉 목표 비중 0%; 다음 봉 시가 가정 |
| v2 | breakout_8 AND volume_26 | 9814.17 | -185.83 | sell / filled / 직전 완료 봉 목표 비중 0%; 다음 봉 시가 가정 |
| v2 | breakout_8 + volume_26 | 9521.07 | -478.93 | sell / filled / 직전 완료 봉 목표 비중 0%; 다음 봉 시가 가정 |
| v2 | reversion_12 AND volume_26 | 9886.24 | -113.76 | sell / filled / 직전 완료 봉 목표 비중 0%; 다음 봉 시가 가정 |
| v2 | reversion_12 + volume_26 | 9728.89 | -271.11 | sell / filled / 직전 완료 봉 목표 비중 0%; 다음 봉 시가 가정 |
| v2 | ema_12_26 | 9985.45 | -14.55 | buy / partial / EMA12 > EMA26; 조건 충족; EMA12=255.218, EMA26=255.146; 직전 완료 봉 목표를 다음 봉 시가에 모의 적용 |
| v2 | macd_12_26_9 | 9985.45 | -14.55 | buy / partial / MACD > 신호선 그리고 MACD > 0; 조건 충족; MACD=0.0719144, signal9=-0.171173; 직전 완료 봉 목표를 다음 봉 시가에 모의 적용 |
| v2 | rsi_14_recovery | 10000.00 | 0.00 | 대기 /  / 새 신호 대기 |
| v2 | bollinger_20_reentry | 10000.00 | 0.00 | 대기 /  / 새 신호 대기 |
| v2 | donchian_20 | 10000.00 | 0.00 | 대기 /  / 새 신호 대기 |
| v2 | atr_14_breakout | 9880.02 | -119.98 | sell / filled / 종가 > 직전 종가 + 직전 ATR14 그리고 종가 > EMA26; 조건 미충족; close=256.72, threshold=258.136, prior_ATR14=1.3158, EMA26=255.146; 직전 완료 봉 목표를 다음 봉 시가에 모의 적용 |
| v2 | session_vwap | 9850.96 | -149.04 | sell / filled / 종가 > 뉴욕 거래일별 누적 전형가격 VWAP; 조건 미충족; close=255.96, session_VWAP=256.469, session_volume=3.61081e+06; 직전 완료 봉 목표를 다음 봉 시가에 모의 적용 |
| v2 | obv_20 | 9990.31 | -9.69 | buy / partial / OBV > OBV의 SMA20 그리고 종가 > EMA26; 조건 충족; OBV=6.12774e+06, OBV_SMA20=4.45241e+06, close=256.69, EMA26=255.435; 직전 완료 봉 목표를 다음 봉 시가에 모의 적용 |
| v2 | stochastic_14_3_recovery | 9925.66 | -74.34 | sell / filled / 직전 %K14 < 20에서 %K14가 %D3 상향 돌파 (한 봉 목표); 조건 미충족; K14=60.1505, D3=50.3645, previous_K14=74.7605, previous_D3=37.7141; 직전 완료 봉 목표를 다음 봉 시가에 모의 적용 |
| v2 | mfi_14_recovery | 10000.00 | 0.00 | 대기 /  / 새 신호 대기 |
| v2 | adx_14_trend | 9817.90 | -182.10 | sell / filled / Wilder ADX14 >= 25 그리고 +DI14 > -DI14; 조건 미충족; ADX14=24.7842, plus_DI14=27.3963, minus_DI14=19.1477; 직전 완료 봉 목표를 다음 봉 시가에 모의 적용 |
| v2 | aroon_25_trend | 10000.00 | 0.00 | 대기 /  / 새 신호 대기 |
| v2 | cci_20_momentum | 9933.64 | -66.36 | sell / filled / CCI20 > 100 (전형가격·평균절대편차); 조건 미충족; CCI20=62.9489; 직전 완료 봉 목표를 다음 봉 시가에 모의 적용 |
| v2 | williams_14_recovery | 9925.66 | -74.34 | sell / filled / 직전 Williams %R14 < -80, 현재 >= -80 (한 봉 목표); 조건 미충족; Williams_R14=-39.8495, previous_R14=-25.2395; 직전 완료 봉 목표를 다음 봉 시가에 모의 적용 |
| v2 | cmf_20_accumulation | 10000.00 | 0.00 | 대기 /  / 새 신호 대기 |
| v2 | chaikin_3_10 | 10000.00 | 0.00 | 대기 /  / 새 신호 대기 |
| v2 | roc_10_momentum | 9924.74 | -75.26 | sell / filled / 10봉 ROC > 1% 그리고 종가 > EMA26; 조건 미충족; ROC10_percent=0.735964, close=255.96, EMA26=255.474; 직전 완료 봉 목표를 다음 봉 시가에 모의 적용 |
| v2 | trix_15_trend | 10000.00 | 0.00 | 대기 /  / 새 신호 대기 |
| v2 | keltner_20_breakout | 10000.00 | 0.00 | 대기 /  / 새 신호 대기 |
| v2 | opening_range_30m | 10000.00 | 0.00 | 대기 /  / 새 신호 대기 |

### 같은 기간의 비용·노출 비교 (사후 연구)

| 전략 | 비용 전 | 비용 후 | 100% 보유 | 같은 평균 노출 보유 | 평균 노출 |
|---|---:|---:|---:|---:|---:|
| cash | 0.00% | 0.00% | -5.56% | -0.00% | 0.00% |
| buy_hold | -5.16% | -5.56% | -5.56% | -5.56% | 100.00% |
| trend_8_26 | 2.57% | 0.02% | -5.56% | -2.77% | 48.55% |
| momentum_26 | 0.96% | -2.38% | -5.56% | -2.72% | 47.76% |
| breakout_8 | -0.78% | -17.87% | -5.56% | -1.23% | 21.37% |
| reversion_12 | -7.78% | -15.92% | -5.56% | -1.71% | 29.82% |
| volume_26 | -0.90% | -7.73% | -5.56% | -0.40% | 6.86% |
| trend_8_26 AND momentum_26 | 2.35% | -0.62% | -5.56% | -2.50% | 43.80% |
| trend_8_26 + momentum_26 | 1.77% | -1.18% | -5.56% | -2.74% | 48.15% |
| trend_8_26 AND breakout_8 | 0.78% | -11.52% | -5.56% | -0.89% | 15.30% |
| trend_8_26 + breakout_8 | 0.91% | -9.15% | -5.56% | -2.00% | 34.97% |
| trend_8_26 AND reversion_12 | 0.69% | -2.63% | -5.56% | -0.32% | 5.54% |
| trend_8_26 + reversion_12 | -2.71% | -7.91% | -5.56% | -2.24% | 39.19% |
| trend_8_26 AND volume_26 | 1.34% | -1.19% | -5.56% | -0.11% | 1.85% |
| trend_8_26 + volume_26 | 0.85% | -3.51% | -5.56% | -1.59% | 27.71% |
| momentum_26 AND breakout_8 | 2.20% | -9.52% | -5.56% | -0.84% | 14.51% |
| momentum_26 + breakout_8 | 0.11% | -10.25% | -5.56% | -1.98% | 34.57% |
| momentum_26 AND reversion_12 | -0.60% | -3.89% | -5.56% | -0.40% | 6.86% |
| momentum_26 + reversion_12 | -3.48% | -8.82% | -5.56% | -2.22% | 38.79% |
| momentum_26 AND volume_26 | 1.57% | -0.12% | -5.56% | -0.08% | 1.32% |
| momentum_26 + volume_26 | 0.06% | -4.48% | -5.56% | -1.57% | 27.31% |
| breakout_8 AND reversion_12 | 0.00% | 0.00% | -5.56% | -0.00% | 0.00% |
| breakout_8 + reversion_12 | -4.33% | -16.38% | -5.56% | -1.47% | 25.60% |
| breakout_8 AND volume_26 | -0.11% | -2.19% | -5.56% | -0.09% | 1.58% |
| breakout_8 + volume_26 | -0.83% | -12.21% | -5.56% | -0.82% | 14.12% |
| reversion_12 AND volume_26 | -1.99% | -4.42% | -5.56% | -0.15% | 2.64% |
| reversion_12 + volume_26 | -4.39% | -11.18% | -5.56% | -1.06% | 18.34% |
| ema_12_26 | 0.08% | -2.00% | -5.56% | -2.53% | 44.33% |
| macd_12_26_9 | 6.44% | 3.79% | -5.56% | -1.67% | 29.02% |
| rsi_14_recovery | -1.69% | -6.92% | -5.56% | -0.20% | 3.43% |
| bollinger_20_reentry | -0.55% | -4.64% | -5.56% | -0.15% | 2.64% |
| donchian_20 | 1.17% | -6.59% | -5.56% | -0.43% | 7.39% |
| atr_14_breakout | 1.31% | -4.88% | -5.56% | -0.28% | 4.75% |
| session_vwap | 1.60% | -5.80% | -5.56% | -2.82% | 49.60% |
| obv_20 | -5.43% | -13.41% | -5.56% | -1.98% | 34.56% |
| stochastic_14_3_recovery | -1.40% | -13.80% | -5.56% | -0.49% | 8.44% |
| mfi_14_recovery | 0.33% | -0.93% | -5.56% | -0.05% | 0.79% |
| adx_14_trend | -2.56% | -7.35% | -5.56% | -1.80% | 31.40% |
| aroon_25_trend | 3.86% | -0.41% | -5.56% | -1.62% | 28.23% |
| cci_20_momentum | 0.85% | -6.49% | -5.56% | -1.43% | 24.80% |
| williams_14_recovery | -2.03% | -10.30% | -5.56% | -0.32% | 5.54% |
| cmf_20_accumulation | 2.16% | -2.04% | -5.56% | -1.76% | 30.61% |
| chaikin_3_10 | -3.52% | -7.87% | -5.56% | -2.07% | 36.15% |
| roc_10_momentum | -1.51% | -7.52% | -5.56% | -0.84% | 14.51% |
| trix_15_trend | -0.90% | -3.36% | -5.56% | -1.92% | 33.51% |
| keltner_20_breakout | 0.76% | -2.97% | -5.56% | -0.55% | 9.50% |
| opening_range_30m | 0.41% | -3.72% | -5.56% | -1.52% | 26.39% |

동일 구간·초기 자금, 종료 시 청산 비용 포함. 노출 맞춤은 사후 설명용이며 v2 실제 계좌 성과가 아닙니다.
[낙폭 분해·비용 영향·전체 구간](JNJ/comparison.json)

[v1 전체 기록](JNJ/accounts.json) · [v2 전체 기록](JNJ/accounts-v2.json)

## CAT 계좌

| 모델 | 전략 | 평가액 USD | 손익 USD | 최근 매매·이유 |
|---|---|---:|---:|---|
| v1 | cash | 10000.00 | 0.00 | 대기 /  / 새 신호 대기 |
| v1 | buy_hold | 10022.84 | 22.84 | buy /  / buy_hold: prior completed bar target 100%; next bar open simulation |
| v1 | trend_8_26 | 10022.84 | 22.84 | buy /  / trend_8_26: prior completed bar target 100%; next bar open simulation |
| v1 | momentum_26 | 9942.35 | -57.65 | buy /  / momentum_26: prior completed bar target 100%; next bar open simulation |
| v1 | breakout_8 | 9950.83 | -49.17 | sell /  / breakout_8: prior completed bar target 0%; next bar open simulation |
| v1 | reversion_12 | 10006.08 | 6.08 | buy /  / reversion_12: prior completed bar target 100%; next bar open simulation |
| v1 | volume_26 | 10000.00 | 0.00 | 대기 /  / 새 신호 대기 |
| v1 | trend_8_26 AND momentum_26 | 9942.35 | -57.65 | buy /  / trend_8_26 AND momentum_26: prior completed bar target 100%; next bar open simulation |
| v1 | trend_8_26 + momentum_26 | 9982.68 | -17.32 | buy /  / trend_8_26 + momentum_26: prior completed bar target 100%; next bar open simulation |
| v1 | trend_8_26 AND breakout_8 | 9950.83 | -49.17 | sell /  / trend_8_26 AND breakout_8: prior completed bar target 0%; next bar open simulation |
| v1 | trend_8_26 + breakout_8 | 9986.95 | -13.05 | sell /  / trend_8_26 + breakout_8: prior completed bar target 50%; next bar open simulation |
| v1 | trend_8_26 AND reversion_12 | 10006.08 | 6.08 | buy /  / trend_8_26 AND reversion_12: prior completed bar target 100%; next bar open simulation |
| v1 | trend_8_26 + reversion_12 | 10014.53 | 14.53 | buy /  / trend_8_26 + reversion_12: prior completed bar target 100%; next bar open simulation |
| v1 | trend_8_26 AND volume_26 | 10000.00 | 0.00 | 대기 /  / 새 신호 대기 |
| v1 | trend_8_26 + volume_26 | 10011.48 | 11.48 | sell /  / trend_8_26 + volume_26: prior completed bar target 50%; next bar open simulation |
| v1 | momentum_26 AND breakout_8 | 9950.83 | -49.17 | sell /  / momentum_26 AND breakout_8: prior completed bar target 0%; next bar open simulation |
| v1 | momentum_26 + breakout_8 | 9946.60 | -53.40 | sell /  / momentum_26 + breakout_8: prior completed bar target 50%; next bar open simulation |
| v1 | momentum_26 AND reversion_12 | 10006.08 | 6.08 | buy /  / momentum_26 AND reversion_12: prior completed bar target 100%; next bar open simulation |
| v1 | momentum_26 + reversion_12 | 9974.16 | -25.84 | buy /  / momentum_26 + reversion_12: prior completed bar target 100%; next bar open simulation |
| v1 | momentum_26 AND volume_26 | 10000.00 | 0.00 | 대기 /  / 새 신호 대기 |
| v1 | momentum_26 + volume_26 | 9971.12 | -28.88 | sell /  / momentum_26 + volume_26: prior completed bar target 50%; next bar open simulation |
| v1 | breakout_8 AND reversion_12 | 10000.00 | 0.00 | 대기 /  / 새 신호 대기 |
| v1 | breakout_8 + reversion_12 | 9978.41 | -21.59 | buy /  / breakout_8 + reversion_12: prior completed bar target 50%; next bar open simulation |
| v1 | breakout_8 AND volume_26 | 10000.00 | 0.00 | 대기 /  / 새 신호 대기 |
| v1 | breakout_8 + volume_26 | 9975.37 | -24.63 | sell /  / breakout_8 + volume_26: prior completed bar target 0%; next bar open simulation |
| v1 | reversion_12 AND volume_26 | 10000.00 | 0.00 | 대기 /  / 새 신호 대기 |
| v1 | reversion_12 + volume_26 | 10003.05 | 3.05 | buy /  / reversion_12 + volume_26: prior completed bar target 50%; next bar open simulation |
| v1 | ema_12_26 | 9942.35 | -57.65 | buy /  / EMA12 > EMA26; 조건 충족; EMA12=733.716, EMA26=733.7 |
| v1 | macd_12_26_9 | 9942.35 | -57.65 | buy /  / MACD > 신호선 그리고 MACD > 0; 조건 충족; MACD=0.0155601, signal9=-2.12997 |
| v1 | rsi_14_recovery | 10000.00 | 0.00 | 대기 /  / 새 신호 대기 |
| v1 | bollinger_20_reentry | 10000.00 | 0.00 | 대기 /  / 새 신호 대기 |
| v1 | donchian_20 | 9950.83 | -49.17 | sell /  / 종가 > 현재 봉을 제외한 직전 20봉 최고가; 조건 미충족; close=739.81, prior_high20=742.28 |
| v1 | atr_14_breakout | 9950.83 | -49.17 | sell /  / 종가 > 직전 종가 + 직전 ATR14 그리고 종가 > EMA26; 조건 미충족; close=739.81, threshold=744.805, prior_ATR14=4.59507, EMA26=734.153 |
| v1 | session_vwap | 9963.13 | -36.87 | sell /  / 종가 > 뉴욕 거래일별 누적 전형가격 VWAP; 조건 미충족; close=734.53, session_VWAP=738.361, session_volume=651546 |
| v1 | obv_20 | 9963.13 | -36.87 | sell /  / OBV > OBV의 SMA20 그리고 종가 > EMA26; 조건 미충족; OBV=-4.44791e+06, OBV_SMA20=-4.51885e+06, close=734.53, EMA26=735.486 |
| v1 | stochastic_14_3_recovery | 10000.00 | 0.00 | 대기 /  / 새 신호 대기 |
| v1 | mfi_14_recovery | 10000.00 | 0.00 | 대기 /  / 새 신호 대기 |
| v1 | adx_14_trend | 10000.00 | 0.00 | 대기 /  / 새 신호 대기 |
| v1 | aroon_25_trend | 10031.15 | 31.15 | sell /  / Aroon25 Up > 70 그리고 Down < 30 (동률이면 최신 극값); 조건 미충족; Aroon_up=88, Aroon_down=48 |
| v1 | cci_20_momentum | 10024.78 | 24.78 | sell /  / CCI20 > 100 (전형가격·평균절대편차); 조건 미충족; CCI20=98.8062 |
| v1 | williams_14_recovery | 10000.00 | 0.00 | 대기 /  / 새 신호 대기 |
| v1 | cmf_20_accumulation | 9951.59 | -48.41 | buy /  / Chaikin Money Flow20 > 0.1; 조건 충족; CMF20=0.173065, volume20=2.14066e+06 |
| v1 | chaikin_3_10 | 9883.12 | -116.88 | sell /  / ADL의 EMA3 - EMA10 > 0 그리고 종가 > EMA26; 조건 미충족; Chaikin3_10=-2197.93, ADL=-5.63919e+06, close=734.53, EMA26=735.486 |
| v1 | roc_10_momentum | 9963.13 | -36.87 | sell /  / 10봉 ROC > 1% 그리고 종가 > EMA26; 조건 미충족; ROC10_percent=-0.134597, close=734.53, EMA26=735.486 |
| v1 | trix_15_trend | 9892.54 | -107.46 | sell /  / 15봉 삼중 EMA의 1봉 변화율 TRIX > 0 그리고 종가 > EMA26; 조건 미충족; TRIX15_percent=0.00822102, close=734.53, EMA26=735.486 |
| v1 | keltner_20_breakout | 10000.00 | 0.00 | 대기 /  / 새 신호 대기 |
| v1 | opening_range_30m | 10040.71 | 40.71 | sell /  / 뉴욕 09:30·09:45 두 완료 봉 최고가를 10:00 이후 종가가 돌파; 자료 부족·변동폭 또는 거래량 없음: 대기; close=740.21 |
| v2 | cash | 10000.00 | 0.00 | 대기 /  / 새 신호 대기 |
| v2 | buy_hold | 9217.75 | -782.25 | 중단: 손실 한도 / buy / partial / 직전 완료 봉 목표 비중 100%; 다음 봉 시가 가정 |
| v2 | trend_8_26 | 9946.39 | -53.61 | buy / partial / 직전 완료 봉 목표 비중 100%; 다음 봉 시가 가정 |
| v2 | momentum_26 | 9955.86 | -44.14 | buy / partial / 직전 완료 봉 목표 비중 100%; 다음 봉 시가 가정 |
| v2 | breakout_8 | 9772.76 | -227.24 | sell / filled / 직전 완료 봉 목표 비중 0%; 다음 봉 시가 가정 |
| v2 | reversion_12 | 9089.02 | -910.98 | 중단: 손실 한도 / buy / partial / 직전 완료 봉 목표 비중 100%; 다음 봉 시가 가정 |
| v2 | volume_26 | 9348.96 | -651.04 | 중단: 손실 한도 / buy / partial / 직전 완료 봉 목표 비중 100%; 다음 봉 시가 가정 |
| v2 | trend_8_26 AND momentum_26 | 9984.69 | -15.31 | buy / partial / 직전 완료 봉 목표 비중 100%; 다음 봉 시가 가정 |
| v2 | trend_8_26 + momentum_26 | 9951.29 | -48.71 | buy / partial / 직전 완료 봉 목표 비중 100%; 다음 봉 시가 가정 |
| v2 | trend_8_26 AND breakout_8 | 9866.70 | -133.30 | sell / filled / 직전 완료 봉 목표 비중 0%; 다음 봉 시가 가정 |
| v2 | trend_8_26 + breakout_8 | 9859.64 | -140.36 | sell / filled / 직전 완료 봉 목표 비중 50%; 다음 봉 시가 가정 |
| v2 | trend_8_26 AND reversion_12 | 9820.06 | -179.94 | buy / partial / 직전 완료 봉 목표 비중 100%; 다음 봉 시가 가정 |
| v2 | trend_8_26 + reversion_12 | 9638.22 | -361.78 | buy / partial / 직전 완료 봉 목표 비중 100%; 다음 봉 시가 가정 |
| v2 | trend_8_26 AND volume_26 | 10035.44 | 35.44 | sell / filled / 직전 완료 봉 목표 비중 0%; 다음 봉 시가 가정 |
| v2 | trend_8_26 + volume_26 | 9643.62 | -356.38 | sell / filled / 직전 완료 봉 목표 비중 50%; 다음 봉 시가 가정 |
| v2 | momentum_26 AND breakout_8 | 9926.39 | -73.61 | sell / filled / 직전 완료 봉 목표 비중 0%; 다음 봉 시가 가정 |
| v2 | momentum_26 + breakout_8 | 9864.09 | -135.91 | sell / filled / 직전 완료 봉 목표 비중 50%; 다음 봉 시가 가정 |
| v2 | momentum_26 AND reversion_12 | 9879.75 | -120.25 | buy / partial / 직전 완료 봉 목표 비중 100%; 다음 봉 시가 가정 |
| v2 | momentum_26 + reversion_12 | 9642.72 | -357.28 | buy / partial / 직전 완료 봉 목표 비중 100%; 다음 봉 시가 가정 |
| v2 | momentum_26 AND volume_26 | 10048.78 | 48.78 | sell / filled / 직전 완료 봉 목표 비중 0%; 다음 봉 시가 가정 |
| v2 | momentum_26 + volume_26 | 9668.42 | -331.58 | sell / filled / 직전 완료 봉 목표 비중 50%; 다음 봉 시가 가정 |
| v2 | breakout_8 AND reversion_12 | 10000.00 | 0.00 | 대기 /  / 새 신호 대기 |
| v2 | breakout_8 + reversion_12 | 9610.18 | -389.82 | 중단: 손실 한도 / sell / filled / 직전 완료 봉 목표 비중 0%; 다음 봉 시가 가정 |
| v2 | breakout_8 AND volume_26 | 9998.69 | -1.31 | sell / filled / 직전 완료 봉 목표 비중 0%; 다음 봉 시가 가정 |
| v2 | breakout_8 + volume_26 | 9579.25 | -420.75 | sell / filled / 직전 완료 봉 목표 비중 0%; 다음 봉 시가 가정 |
| v2 | reversion_12 AND volume_26 | 9284.29 | -715.71 | 중단: 손실 한도 / buy / partial / 직전 완료 봉 목표 비중 100%; 다음 봉 시가 가정 |
| v2 | reversion_12 + volume_26 | 9407.42 | -592.58 | 중단: 손실 한도 / sell / filled / 직전 완료 봉 목표 비중 50%; 다음 봉 시가 가정 |
| v2 | ema_12_26 | 9941.36 | -58.64 | buy / partial / EMA12 > EMA26; 조건 충족; EMA12=733.716, EMA26=733.7; 직전 완료 봉 목표를 다음 봉 시가에 모의 적용 |
| v2 | macd_12_26_9 | 9941.36 | -58.64 | buy / partial / MACD > 신호선 그리고 MACD > 0; 조건 충족; MACD=0.0155601, signal9=-2.12997; 직전 완료 봉 목표를 다음 봉 시가에 모의 적용 |
| v2 | rsi_14_recovery | 10000.00 | 0.00 | 대기 /  / 새 신호 대기 |
| v2 | bollinger_20_reentry | 10000.00 | 0.00 | 대기 /  / 새 신호 대기 |
| v2 | donchian_20 | 9948.84 | -51.16 | sell / filled / 종가 > 현재 봉을 제외한 직전 20봉 최고가; 조건 미충족; close=739.81, prior_high20=742.28; 직전 완료 봉 목표를 다음 봉 시가에 모의 적용 |
| v2 | atr_14_breakout | 9948.84 | -51.16 | sell / filled / 종가 > 직전 종가 + 직전 ATR14 그리고 종가 > EMA26; 조건 미충족; close=739.81, threshold=744.805, prior_ATR14=4.59507, EMA26=734.153; 직전 완료 봉 목표를 다음 봉 시가에 모의 적용 |
| v2 | session_vwap | 9961.14 | -38.86 | sell / filled / 종가 > 뉴욕 거래일별 누적 전형가격 VWAP; 조건 미충족; close=734.53, session_VWAP=738.361, session_volume=651546; 직전 완료 봉 목표를 다음 봉 시가에 모의 적용 |
| v2 | obv_20 | 9961.14 | -38.86 | sell / filled / OBV > OBV의 SMA20 그리고 종가 > EMA26; 조건 미충족; OBV=-4.44791e+06, OBV_SMA20=-4.51885e+06, close=734.53, EMA26=735.486; 직전 완료 봉 목표를 다음 봉 시가에 모의 적용 |
| v2 | stochastic_14_3_recovery | 10000.00 | 0.00 | 대기 /  / 새 신호 대기 |
| v2 | mfi_14_recovery | 10000.00 | 0.00 | 대기 /  / 새 신호 대기 |
| v2 | adx_14_trend | 10000.00 | 0.00 | 대기 /  / 새 신호 대기 |
| v2 | aroon_25_trend | 10029.14 | 29.14 | sell / filled / Aroon25 Up > 70 그리고 Down < 30 (동률이면 최신 극값); 조건 미충족; Aroon_up=88, Aroon_down=48; 직전 완료 봉 목표를 다음 봉 시가에 모의 적용 |
| v2 | cci_20_momentum | 10022.77 | 22.77 | sell / filled / CCI20 > 100 (전형가격·평균절대편차); 조건 미충족; CCI20=98.8062; 직전 완료 봉 목표를 다음 봉 시가에 모의 적용 |
| v2 | williams_14_recovery | 10000.00 | 0.00 | 대기 /  / 새 신호 대기 |
| v2 | cmf_20_accumulation | 9950.59 | -49.41 | buy / partial / Chaikin Money Flow20 > 0.1; 조건 충족; CMF20=0.173065, volume20=2.14066e+06; 직전 완료 봉 목표를 다음 봉 시가에 모의 적용 |
| v2 | chaikin_3_10 | 9881.15 | -118.85 | sell / filled / ADL의 EMA3 - EMA10 > 0 그리고 종가 > EMA26; 조건 미충족; Chaikin3_10=-2197.93, ADL=-5.63919e+06, close=734.53, EMA26=735.486; 직전 완료 봉 목표를 다음 봉 시가에 모의 적용 |
| v2 | roc_10_momentum | 9961.14 | -38.86 | sell / filled / 10봉 ROC > 1% 그리고 종가 > EMA26; 조건 미충족; ROC10_percent=-0.134597, close=734.53, EMA26=735.486; 직전 완료 봉 목표를 다음 봉 시가에 모의 적용 |
| v2 | trix_15_trend | 9890.57 | -109.43 | sell / filled / 15봉 삼중 EMA의 1봉 변화율 TRIX > 0 그리고 종가 > EMA26; 조건 미충족; TRIX15_percent=0.00822102, close=734.53, EMA26=735.486; 직전 완료 봉 목표를 다음 봉 시가에 모의 적용 |
| v2 | keltner_20_breakout | 10000.00 | 0.00 | 대기 /  / 새 신호 대기 |
| v2 | opening_range_30m | 10038.70 | 38.70 | sell / filled / 뉴욕 09:30·09:45 두 완료 봉 최고가를 10:00 이후 종가가 돌파; 자료 부족·변동폭 또는 거래량 없음: 대기; close=740.21; 직전 완료 봉 목표를 다음 봉 시가에 모의 적용 |

### 같은 기간의 비용·노출 비교 (사후 연구)

| 전략 | 비용 전 | 비용 후 | 100% 보유 | 같은 평균 노출 보유 | 평균 노출 |
|---|---:|---:|---:|---:|---:|
| cash | 0.00% | 0.00% | -10.14% | -0.00% | 0.00% |
| buy_hold | -9.77% | -10.14% | -10.14% | -10.14% | 100.00% |
| trend_8_26 | -1.21% | -4.88% | -10.14% | -5.13% | 50.13% |
| momentum_26 | -4.10% | -9.96% | -10.14% | -4.97% | 48.55% |
| breakout_8 | -3.26% | -16.13% | -10.14% | -1.57% | 15.30% |
| reversion_12 | -3.64% | -15.41% | -10.14% | -2.68% | 26.12% |
| volume_26 | -2.95% | -10.02% | -10.14% | -0.84% | 8.18% |
| trend_8_26 AND momentum_26 | -1.41% | -6.25% | -10.14% | -4.38% | 42.74% |
| trend_8_26 + momentum_26 | -2.65% | -7.44% | -10.14% | -5.05% | 49.34% |
| trend_8_26 AND breakout_8 | -1.89% | -9.42% | -10.14% | -0.81% | 7.92% |
| trend_8_26 + breakout_8 | -2.20% | -10.47% | -10.14% | -3.36% | 32.72% |
| trend_8_26 AND reversion_12 | 1.04% | -5.53% | -10.14% | -0.76% | 7.39% |
| trend_8_26 + reversion_12 | -2.37% | -9.70% | -10.14% | -3.91% | 38.13% |
| trend_8_26 AND volume_26 | 2.22% | -0.75% | -10.14% | -0.27% | 2.64% |
| trend_8_26 + volume_26 | -2.03% | -7.26% | -10.14% | -2.99% | 29.16% |
| momentum_26 AND breakout_8 | -2.81% | -11.02% | -10.14% | -0.90% | 8.71% |
| momentum_26 + breakout_8 | -3.64% | -13.07% | -10.14% | -3.27% | 31.93% |
| momentum_26 AND reversion_12 | -2.79% | -9.11% | -10.14% | -0.62% | 6.07% |
| momentum_26 + reversion_12 | -3.82% | -11.79% | -10.14% | -3.83% | 37.34% |
| momentum_26 AND volume_26 | 1.58% | -0.53% | -10.14% | -0.16% | 1.58% |
| momentum_26 + volume_26 | -3.47% | -9.20% | -10.14% | -2.91% | 28.37% |
| breakout_8 AND reversion_12 | 0.00% | 0.00% | -10.14% | -0.00% | 0.00% |
| breakout_8 + reversion_12 | -3.40% | -14.86% | -10.14% | -2.13% | 20.72% |
| breakout_8 AND volume_26 | 0.37% | -0.47% | -10.14% | -0.05% | 0.53% |
| breakout_8 + volume_26 | -3.07% | -12.38% | -10.14% | -1.21% | 11.75% |
| reversion_12 AND volume_26 | -1.25% | -5.71% | -10.14% | -0.54% | 5.28% |
| reversion_12 + volume_26 | -3.26% | -12.00% | -10.14% | -1.76% | 17.16% |
| ema_12_26 | -0.65% | -2.72% | -10.14% | -5.10% | 49.87% |
| macd_12_26_9 | -0.59% | -4.68% | -10.14% | -3.09% | 30.08% |
| rsi_14_recovery | -0.96% | -6.22% | -10.14% | -0.35% | 3.43% |
| bollinger_20_reentry | 1.35% | -4.43% | -10.14% | -0.38% | 3.69% |
| donchian_20 | -2.30% | -7.11% | -10.14% | -0.54% | 5.28% |
| atr_14_breakout | -2.42% | -9.14% | -10.14% | -0.49% | 4.75% |
| session_vwap | -0.03% | -11.49% | -10.14% | -4.75% | 46.44% |
| obv_20 | -3.92% | -14.22% | -10.14% | -2.79% | 27.18% |
| stochastic_14_3_recovery | -3.21% | -13.22% | -10.14% | -0.71% | 6.86% |
| mfi_14_recovery | 0.45% | -1.63% | -10.14% | -0.14% | 1.32% |
| adx_14_trend | -3.13% | -5.93% | -10.14% | -0.98% | 9.50% |
| aroon_25_trend | -2.12% | -6.14% | -10.14% | -1.52% | 14.78% |
| cci_20_momentum | -5.69% | -11.82% | -10.14% | -1.68% | 16.36% |
| williams_14_recovery | -1.60% | -10.66% | -10.14% | -0.62% | 6.07% |
| cmf_20_accumulation | -5.47% | -12.35% | -10.14% | -1.84% | 17.94% |
| chaikin_3_10 | -5.69% | -14.01% | -10.14% | -3.62% | 35.36% |
| roc_10_momentum | -1.82% | -7.81% | -10.14% | -1.38% | 13.46% |
| trix_15_trend | -0.71% | -4.80% | -10.14% | -4.03% | 39.31% |
| keltner_20_breakout | -3.35% | -6.15% | -10.14% | -0.30% | 2.90% |
| opening_range_30m | 4.95% | -0.21% | -10.14% | -2.11% | 20.58% |

동일 구간·초기 자금, 종료 시 청산 비용 포함. 노출 맞춤은 사후 설명용이며 v2 실제 계좌 성과가 아닙니다.
[낙폭 분해·비용 영향·전체 구간](CAT/comparison.json)

[v1 전체 기록](CAT/accounts.json) · [v2 전체 기록](CAT/accounts-v2.json)

## WMT 계좌

| 모델 | 전략 | 평가액 USD | 손익 USD | 최근 매매·이유 |
|---|---|---:|---:|---|
| v1 | cash | 10000.00 | 0.00 | 대기 /  / 새 신호 대기 |
| v1 | buy_hold | 10031.98 | 31.98 | buy /  / buy_hold: prior completed bar target 100%; next bar open simulation |
| v1 | trend_8_26 | 9978.35 | -21.65 | buy /  / trend_8_26: prior completed bar target 100%; next bar open simulation |
| v1 | momentum_26 | 10043.97 | 43.97 | sell /  / momentum_26: prior completed bar target 0%; next bar open simulation |
| v1 | breakout_8 | 9953.51 | -46.49 | sell /  / breakout_8: prior completed bar target 0%; next bar open simulation |
| v1 | reversion_12 | 10043.97 | 43.97 | sell /  / reversion_12: prior completed bar target 0%; next bar open simulation |
| v1 | volume_26 | 9979.72 | -20.28 | sell /  / volume_26: prior completed bar target 0%; next bar open simulation |
| v1 | trend_8_26 AND momentum_26 | 10000.00 | 0.00 | 대기 /  / 새 신호 대기 |
| v1 | trend_8_26 + momentum_26 | 10011.15 | 11.15 | buy /  / trend_8_26 + momentum_26: prior completed bar target 50%; next bar open simulation |
| v1 | trend_8_26 AND breakout_8 | 10000.00 | 0.00 | 대기 /  / 새 신호 대기 |
| v1 | trend_8_26 + breakout_8 | 9965.90 | -34.10 | buy /  / trend_8_26 + breakout_8: prior completed bar target 50%; next bar open simulation |
| v1 | trend_8_26 AND reversion_12 | 10000.00 | 0.00 | 대기 /  / 새 신호 대기 |
| v1 | trend_8_26 + reversion_12 | 10011.15 | 11.15 | buy /  / trend_8_26 + reversion_12: prior completed bar target 50%; next bar open simulation |
| v1 | trend_8_26 AND volume_26 | 10000.00 | 0.00 | 대기 /  / 새 신호 대기 |
| v1 | trend_8_26 + volume_26 | 9978.99 | -21.01 | buy /  / trend_8_26 + volume_26: prior completed bar target 50%; next bar open simulation |
| v1 | momentum_26 AND breakout_8 | 10000.00 | 0.00 | 대기 /  / 새 신호 대기 |
| v1 | momentum_26 + breakout_8 | 10018.74 | 18.74 | sell /  / momentum_26 + breakout_8: prior completed bar target 0%; next bar open simulation |
| v1 | momentum_26 AND reversion_12 | 10043.97 | 43.97 | sell /  / momentum_26 AND reversion_12: prior completed bar target 0%; next bar open simulation |
| v1 | momentum_26 + reversion_12 | 10043.97 | 43.97 | sell /  / momentum_26 + reversion_12: prior completed bar target 0%; next bar open simulation |
| v1 | momentum_26 AND volume_26 | 10000.00 | 0.00 | 대기 /  / 새 신호 대기 |
| v1 | momentum_26 + volume_26 | 10031.90 | 31.90 | sell /  / momentum_26 + volume_26: prior completed bar target 0%; next bar open simulation |
| v1 | breakout_8 AND reversion_12 | 10000.00 | 0.00 | 대기 /  / 새 신호 대기 |
| v1 | breakout_8 + reversion_12 | 10018.74 | 18.74 | sell /  / breakout_8 + reversion_12: prior completed bar target 0%; next bar open simulation |
| v1 | breakout_8 AND volume_26 | 9979.72 | -20.28 | sell /  / breakout_8 AND volume_26: prior completed bar target 0%; next bar open simulation |
| v1 | breakout_8 + volume_26 | 9966.61 | -33.39 | sell /  / breakout_8 + volume_26: prior completed bar target 0%; next bar open simulation |
| v1 | reversion_12 AND volume_26 | 10000.00 | 0.00 | 대기 /  / 새 신호 대기 |
| v1 | reversion_12 + volume_26 | 10031.90 | 31.90 | sell /  / reversion_12 + volume_26: prior completed bar target 0%; next bar open simulation |
| v1 | ema_12_26 | 10031.98 | 31.98 | buy /  / EMA12 > EMA26; 조건 충족; EMA12=118.245, EMA26=118.045 |
| v1 | macd_12_26_9 | 10000.00 | 0.00 | 대기 /  / 새 신호 대기 |
| v1 | rsi_14_recovery | 10000.00 | 0.00 | 대기 /  / 새 신호 대기 |
| v1 | bollinger_20_reentry | 10000.00 | 0.00 | 대기 /  / 새 신호 대기 |
| v1 | donchian_20 | 10000.00 | 0.00 | 대기 /  / 새 신호 대기 |
| v1 | atr_14_breakout | 9979.72 | -20.28 | sell /  / 종가 > 직전 종가 + 직전 ATR14 그리고 종가 > EMA26; 조건 미충족; close=119.375, threshold=119.607, prior_ATR14=0.486823, EMA26=118.217 |
| v1 | session_vwap | 9839.22 | -160.78 | sell /  / 종가 > 뉴욕 거래일별 누적 전형가격 VWAP; 조건 미충족; close=118.745, session_VWAP=118.899, session_volume=6.77102e+06 |
| v1 | obv_20 | 10000.00 | 0.00 | 대기 /  / 새 신호 대기 |
| v1 | stochastic_14_3_recovery | 9979.72 | -20.28 | sell /  / 직전 %K14 < 20에서 %K14가 %D3 상향 돌파 (한 봉 목표); 조건 미충족; K14=93.8952, D3=60.8222, previous_K14=82.4242, previous_D3=34.5012 |
| v1 | mfi_14_recovery | 10000.00 | 0.00 | 대기 /  / 새 신호 대기 |
| v1 | adx_14_trend | 10031.98 | 31.98 | buy /  / Wilder ADX14 >= 25 그리고 +DI14 > -DI14; 조건 충족; ADX14=29.9186, plus_DI14=22.635, minus_DI14=22.4078 |
| v1 | aroon_25_trend | 10000.00 | 0.00 | 대기 /  / 새 신호 대기 |
| v1 | cci_20_momentum | 9932.96 | -67.04 | sell /  / CCI20 > 100 (전형가격·평균절대편차); 조건 미충족; CCI20=99.1325 |
| v1 | williams_14_recovery | 9979.72 | -20.28 | sell /  / 직전 Williams %R14 < -80, 현재 >= -80 (한 봉 목표); 조건 미충족; Williams_R14=-6.10484, previous_R14=-17.5758 |
| v1 | cmf_20_accumulation | 10000.00 | 0.00 | 대기 /  / 새 신호 대기 |
| v1 | chaikin_3_10 | 9858.18 | -141.82 | buy /  / ADL의 EMA3 - EMA10 > 0 그리고 종가 > EMA26; 조건 충족; Chaikin3_10=175820, ADL=1.95122e+07, close=118.735, EMA26=118.371 |
| v1 | roc_10_momentum | 10000.00 | 0.00 | 대기 /  / 새 신호 대기 |
| v1 | trix_15_trend | 9948.19 | -51.81 | buy /  / 15봉 삼중 EMA의 1봉 변화율 TRIX > 0 그리고 종가 > EMA26; 조건 충족; TRIX15_percent=0.0496307, close=119.12, EMA26=118.125 |
| v1 | keltner_20_breakout | 10000.00 | 0.00 | 대기 /  / 새 신호 대기 |
| v1 | opening_range_30m | 10000.00 | 0.00 | 대기 /  / 새 신호 대기 |
| v2 | cash | 10000.00 | 0.00 | 대기 /  / 새 신호 대기 |
| v2 | buy_hold | 10628.79 | 628.79 | buy / partial / 직전 완료 봉 목표 비중 100%; 다음 봉 시가 가정 |
| v2 | trend_8_26 | 10387.05 | 387.05 | buy / partial / 직전 완료 봉 목표 비중 100%; 다음 봉 시가 가정 |
| v2 | momentum_26 | 10465.54 | 465.54 | sell / filled / 직전 완료 봉 목표 비중 0%; 다음 봉 시가 가정 |
| v2 | breakout_8 | 9916.34 | -83.66 | sell / filled / 직전 완료 봉 목표 비중 0%; 다음 봉 시가 가정 |
| v2 | reversion_12 | 9953.01 | -46.99 | sell / filled / 직전 완료 봉 목표 비중 0%; 다음 봉 시가 가정 |
| v2 | volume_26 | 9943.08 | -56.92 | sell / filled / 직전 완료 봉 목표 비중 0%; 다음 봉 시가 가정 |
| v2 | trend_8_26 AND momentum_26 | 10410.62 | 410.62 | sell / filled / 직전 완료 봉 목표 비중 0%; 다음 봉 시가 가정 |
| v2 | trend_8_26 + momentum_26 | 10426.21 | 426.21 | buy / filled / 직전 완료 봉 목표 비중 50%; 다음 봉 시가 가정 |
| v2 | trend_8_26 AND breakout_8 | 10088.55 | 88.55 | sell / filled / 직전 완료 봉 목표 비중 0%; 다음 봉 시가 가정 |
| v2 | trend_8_26 + breakout_8 | 10149.35 | 149.35 | buy / filled / 직전 완료 봉 목표 비중 50%; 다음 봉 시가 가정 |
| v2 | trend_8_26 AND reversion_12 | 9808.74 | -191.26 | sell / filled / 직전 완료 봉 목표 비중 0%; 다음 봉 시가 가정 |
| v2 | trend_8_26 + reversion_12 | 10169.20 | 169.20 | buy / filled / 직전 완료 봉 목표 비중 50%; 다음 봉 시가 가정 |
| v2 | trend_8_26 AND volume_26 | 9949.23 | -50.77 | sell / filled / 직전 완료 봉 목표 비중 0%; 다음 봉 시가 가정 |
| v2 | trend_8_26 + volume_26 | 10164.05 | 164.05 | buy / filled / 직전 완료 봉 목표 비중 50%; 다음 봉 시가 가정 |
| v2 | momentum_26 AND breakout_8 | 9964.65 | -35.35 | sell / filled / 직전 완료 봉 목표 비중 0%; 다음 봉 시가 가정 |
| v2 | momentum_26 + breakout_8 | 10209.15 | 209.15 | sell / filled / 직전 완료 봉 목표 비중 0%; 다음 봉 시가 가정 |
| v2 | momentum_26 AND reversion_12 | 9872.00 | -128.00 | sell / filled / 직전 완료 봉 목표 비중 0%; 다음 봉 시가 가정 |
| v2 | momentum_26 + reversion_12 | 10250.55 | 250.55 | sell / filled / 직전 완료 봉 목표 비중 0%; 다음 봉 시가 가정 |
| v2 | momentum_26 AND volume_26 | 9913.82 | -86.18 | sell / filled / 직전 완료 봉 목표 비중 0%; 다음 봉 시가 가정 |
| v2 | momentum_26 + volume_26 | 10223.99 | 223.99 | sell / filled / 직전 완료 봉 목표 비중 0%; 다음 봉 시가 가정 |
| v2 | breakout_8 AND reversion_12 | 10000.00 | 0.00 | 대기 /  / 새 신호 대기 |
| v2 | breakout_8 + reversion_12 | 9977.73 | -22.27 | sell / filled / 직전 완료 봉 목표 비중 0%; 다음 봉 시가 가정 |
| v2 | breakout_8 AND volume_26 | 9928.06 | -71.94 | sell / filled / 직전 완료 봉 목표 비중 0%; 다음 봉 시가 가정 |
| v2 | breakout_8 + volume_26 | 9931.09 | -68.91 | sell / filled / 직전 완료 봉 목표 비중 0%; 다음 봉 시가 가정 |
| v2 | reversion_12 AND volume_26 | 10009.78 | 9.78 | sell / filled / 직전 완료 봉 목표 비중 0%; 다음 봉 시가 가정 |
| v2 | reversion_12 + volume_26 | 9968.93 | -31.07 | sell / filled / 직전 완료 봉 목표 비중 0%; 다음 봉 시가 가정 |
| v2 | ema_12_26 | 10030.98 | 30.98 | buy / partial / EMA12 > EMA26; 조건 충족; EMA12=118.245, EMA26=118.045; 직전 완료 봉 목표를 다음 봉 시가에 모의 적용 |
| v2 | macd_12_26_9 | 10000.00 | 0.00 | 대기 /  / 새 신호 대기 |
| v2 | rsi_14_recovery | 10000.00 | 0.00 | 대기 /  / 새 신호 대기 |
| v2 | bollinger_20_reentry | 10000.00 | 0.00 | 대기 /  / 새 신호 대기 |
| v2 | donchian_20 | 10000.00 | 0.00 | 대기 /  / 새 신호 대기 |
| v2 | atr_14_breakout | 9977.72 | -22.28 | sell / filled / 종가 > 직전 종가 + 직전 ATR14 그리고 종가 > EMA26; 조건 미충족; close=119.375, threshold=119.607, prior_ATR14=0.486823, EMA26=118.217; 직전 완료 봉 목표를 다음 봉 시가에 모의 적용 |
| v2 | session_vwap | 9835.28 | -164.72 | sell / filled / 종가 > 뉴욕 거래일별 누적 전형가격 VWAP; 조건 미충족; close=118.745, session_VWAP=118.899, session_volume=6.77102e+06; 직전 완료 봉 목표를 다음 봉 시가에 모의 적용 |
| v2 | obv_20 | 10000.00 | 0.00 | 대기 /  / 새 신호 대기 |
| v2 | stochastic_14_3_recovery | 9977.72 | -22.28 | sell / filled / 직전 %K14 < 20에서 %K14가 %D3 상향 돌파 (한 봉 목표); 조건 미충족; K14=93.8952, D3=60.8222, previous_K14=82.4242, previous_D3=34.5012; 직전 완료 봉 목표를 다음 봉 시가에 모의 적용 |
| v2 | mfi_14_recovery | 10000.00 | 0.00 | 대기 /  / 새 신호 대기 |
| v2 | adx_14_trend | 10030.98 | 30.98 | buy / partial / Wilder ADX14 >= 25 그리고 +DI14 > -DI14; 조건 충족; ADX14=29.9186, plus_DI14=22.635, minus_DI14=22.4078; 직전 완료 봉 목표를 다음 봉 시가에 모의 적용 |
| v2 | aroon_25_trend | 10000.00 | 0.00 | 대기 /  / 새 신호 대기 |
| v2 | cci_20_momentum | 9930.98 | -69.02 | sell / filled / CCI20 > 100 (전형가격·평균절대편차); 조건 미충족; CCI20=99.1325; 직전 완료 봉 목표를 다음 봉 시가에 모의 적용 |
| v2 | williams_14_recovery | 9977.72 | -22.28 | sell / filled / 직전 Williams %R14 < -80, 현재 >= -80 (한 봉 목표); 조건 미충족; Williams_R14=-6.10484, previous_R14=-17.5758; 직전 완료 봉 목표를 다음 봉 시가에 모의 적용 |
| v2 | cmf_20_accumulation | 10000.00 | 0.00 | 대기 /  / 새 신호 대기 |
| v2 | chaikin_3_10 | 9855.22 | -144.78 | buy / partial / ADL의 EMA3 - EMA10 > 0 그리고 종가 > EMA26; 조건 충족; Chaikin3_10=175820, ADL=1.95122e+07, close=118.735, EMA26=118.371; 직전 완료 봉 목표를 다음 봉 시가에 모의 적용 |
| v2 | roc_10_momentum | 10000.00 | 0.00 | 대기 /  / 새 신호 대기 |
| v2 | trix_15_trend | 9947.20 | -52.80 | buy / partial / 15봉 삼중 EMA의 1봉 변화율 TRIX > 0 그리고 종가 > EMA26; 조건 충족; TRIX15_percent=0.0496307, close=119.12, EMA26=118.125; 직전 완료 봉 목표를 다음 봉 시가에 모의 적용 |
| v2 | keltner_20_breakout | 10000.00 | 0.00 | 대기 /  / 새 신호 대기 |
| v2 | opening_range_30m | 10000.00 | 0.00 | 대기 /  / 새 신호 대기 |

### 같은 기간의 비용·노출 비교 (사후 연구)

| 전략 | 비용 전 | 비용 후 | 100% 보유 | 같은 평균 노출 보유 | 평균 노출 |
|---|---:|---:|---:|---:|---:|
| cash | 0.00% | 0.00% | 9.66% | 0.00% | 0.00% |
| buy_hold | 10.13% | 9.66% | 9.66% | 9.66% | 100.00% |
| trend_8_26 | 9.41% | 6.24% | 9.66% | 6.68% | 69.39% |
| momentum_26 | 7.43% | 3.45% | 9.66% | 6.73% | 69.92% |
| breakout_8 | 5.45% | -11.60% | 9.66% | 2.55% | 26.65% |
| reversion_12 | 4.02% | -5.96% | 9.66% | 1.62% | 16.89% |
| volume_26 | -0.20% | -5.50% | 9.66% | 0.53% | 5.54% |
| trend_8_26 AND momentum_26 | 8.87% | 4.83% | 9.66% | 6.09% | 63.32% |
| trend_8_26 + momentum_26 | 8.42% | 4.84% | 9.66% | 6.71% | 69.66% |
| trend_8_26 AND breakout_8 | 6.92% | -6.91% | 9.66% | 2.15% | 22.43% |
| trend_8_26 + breakout_8 | 7.43% | -3.08% | 9.66% | 4.61% | 48.03% |
| trend_8_26 AND reversion_12 | 0.42% | -4.91% | 9.66% | 0.66% | 6.86% |
| trend_8_26 + reversion_12 | 6.72% | 0.17% | 9.66% | 4.14% | 43.14% |
| trend_8_26 AND volume_26 | 1.13% | -1.39% | 9.66% | 0.20% | 2.11% |
| trend_8_26 + volume_26 | 4.53% | 0.63% | 9.66% | 3.59% | 37.47% |
| momentum_26 AND breakout_8 | 5.58% | -8.47% | 9.66% | 2.25% | 23.48% |
| momentum_26 + breakout_8 | 6.45% | -3.96% | 9.66% | 4.64% | 48.29% |
| momentum_26 AND reversion_12 | 1.36% | -4.43% | 9.66% | 0.73% | 7.65% |
| momentum_26 + reversion_12 | 5.75% | 0.53% | 9.66% | 4.17% | 43.41% |
| momentum_26 AND volume_26 | 0.44% | -3.69% | 9.66% | 0.28% | 2.90% |
| momentum_26 + volume_26 | 3.58% | -0.91% | 9.66% | 3.62% | 37.73% |
| breakout_8 AND reversion_12 | 0.00% | 0.00% | 9.66% | 0.00% | 0.00% |
| breakout_8 + reversion_12 | 4.76% | -8.24% | 9.66% | 2.08% | 21.78% |
| breakout_8 AND volume_26 | 1.29% | -0.82% | 9.66% | 0.15% | 1.58% |
| breakout_8 + volume_26 | 2.62% | -7.82% | 9.66% | 1.54% | 16.10% |
| reversion_12 AND volume_26 | -0.51% | -2.99% | 9.66% | 0.23% | 2.37% |
| reversion_12 + volume_26 | 1.90% | -5.33% | 9.66% | 1.07% | 11.22% |
| ema_12_26 | 9.22% | 7.85% | 9.66% | 6.58% | 68.34% |
| macd_12_26_9 | 8.10% | 4.53% | 9.66% | 3.47% | 36.15% |
| rsi_14_recovery | -0.68% | -2.74% | 9.66% | 0.13% | 1.32% |
| bollinger_20_reentry | 0.93% | -2.41% | 9.66% | 0.20% | 2.11% |
| donchian_20 | 4.64% | -8.52% | 9.66% | 1.36% | 14.25% |
| atr_14_breakout | -0.51% | -10.81% | 9.66% | 0.78% | 8.18% |
| session_vwap | 7.25% | -3.03% | 9.66% | 5.86% | 60.95% |
| obv_20 | 8.12% | 0.25% | 9.66% | 5.40% | 56.20% |
| stochastic_14_3_recovery | 1.43% | -9.06% | 9.66% | 0.66% | 6.86% |
| mfi_14_recovery | 0.02% | -0.81% | 9.66% | 0.05% | 0.53% |
| adx_14_trend | 9.06% | 6.34% | 9.66% | 4.87% | 50.66% |
| aroon_25_trend | 6.70% | 1.88% | 9.66% | 3.06% | 31.93% |
| cci_20_momentum | 7.75% | -0.52% | 9.66% | 3.19% | 33.25% |
| williams_14_recovery | 0.23% | -8.61% | 9.66% | 0.55% | 5.80% |
| cmf_20_accumulation | 9.49% | 1.51% | 9.66% | 3.77% | 39.31% |
| chaikin_3_10 | 5.65% | -2.05% | 9.66% | 5.10% | 53.03% |
| roc_10_momentum | -0.29% | -5.58% | 9.66% | 1.49% | 15.57% |
| trix_15_trend | 8.26% | 6.01% | 9.66% | 6.20% | 64.38% |
| keltner_20_breakout | 6.87% | -0.08% | 9.66% | 2.65% | 27.70% |
| opening_range_30m | 10.55% | 5.12% | 9.66% | 3.54% | 36.94% |

동일 구간·초기 자금, 종료 시 청산 비용 포함. 노출 맞춤은 사후 설명용이며 v2 실제 계좌 성과가 아닙니다.
[낙폭 분해·비용 영향·전체 구간](WMT/comparison.json)

[v1 전체 기록](WMT/accounts.json) · [v2 전체 기록](WMT/accounts-v2.json)
