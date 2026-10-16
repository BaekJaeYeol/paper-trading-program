# 모의투자 운영 현황

[PC·서버 장애 진단과 복구 방법](https://github.com/BaekJaeYeol/paper-trading-program/blob/main/investment-lab/docs/failure-recovery.md)

이번 실행 복구: {}

완료 봉 확인 주기: 기록 3/9회 · 기록 없는 예정 6회 · 아직 판정 전 17회 · 주의: 예약 시작 지연 또는 실행·저장 누락을 확인하세요.

[주기 판정 기준](https://github.com/BaekJaeYeol/paper-trading-program/blob/main/investment-lab/docs/session-coverage.md)

최근 확인: 2026-10-16T16:07:00.377662+00:00 (UTC)
다음 15분 확인 목표 (세션 실행 중에만 적용): 2026-10-16T16:22:00+00:00 (UTC, 실행 지연 가능)

실제 주문 없음. v1 기존 계좌와 v2 새 계좌의 시작일이 다르므로 수익률을 직접 우열 비교하지 마세요.
v2는 다음 봉 시가에 비용·스프레드·직전 거래량 제한을 적용한 가상 체결입니다. 미체결 잔량은 만료됩니다.

| 종목 | 상태 | 최근 성공 UTC | 마지막 완료 봉 UTC | 이번 새 봉 |
|---|---|---|---|---|
| SPY | updated | 2026-10-16T16:07:00.377662+00:00 | 2026-10-16T15:45:00+00:00 | 1 |
| QQQ | updated | 2026-10-16T16:07:00.377662+00:00 | 2026-10-16T15:45:00+00:00 | 1 |
| IWM | updated | 2026-10-16T16:07:00.377662+00:00 | 2026-10-16T15:45:00+00:00 | 1 |
| DIA | updated | 2026-10-16T16:07:00.377662+00:00 | 2026-10-16T15:45:00+00:00 | 1 |
| MSFT | updated | 2026-10-16T16:07:00.377662+00:00 | 2026-10-16T15:45:00+00:00 | 1 |
| JPM | updated | 2026-10-16T16:07:00.377662+00:00 | 2026-10-16T15:45:00+00:00 | 1 |
| XOM | updated | 2026-10-16T16:07:00.377662+00:00 | 2026-10-16T15:45:00+00:00 | 1 |
| JNJ | updated | 2026-10-16T16:07:00.377662+00:00 | 2026-10-16T15:45:00+00:00 | 1 |
| CAT | updated | 2026-10-16T16:07:00.377662+00:00 | 2026-10-16T15:45:00+00:00 | 1 |
| WMT | updated | 2026-10-16T16:07:00.377662+00:00 | 2026-10-16T15:45:00+00:00 | 1 |

이번 실행 소요: 43.21초
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
| v1 | buy_hold | 9906.07 | -93.93 | buy /  / buy_hold: prior completed bar target 100%; next bar open simulation |
| v1 | trend_8_26 | 9902.75 | -97.25 | sell /  / trend_8_26: prior completed bar target 0%; next bar open simulation |
| v1 | momentum_26 | 9916.54 | -83.46 | sell /  / momentum_26: prior completed bar target 0%; next bar open simulation |
| v1 | breakout_8 | 10000.00 | 0.00 | 대기 /  / 새 신호 대기 |
| v1 | reversion_12 | 9949.57 | -50.43 | buy /  / reversion_12: prior completed bar target 100%; next bar open simulation |
| v1 | volume_26 | 9925.86 | -74.14 | sell /  / volume_26: prior completed bar target 0%; next bar open simulation |
| v1 | trend_8_26 AND momentum_26 | 9916.54 | -83.46 | sell /  / trend_8_26 AND momentum_26: prior completed bar target 0%; next bar open simulation |
| v1 | trend_8_26 + momentum_26 | 9909.65 | -90.35 | sell /  / trend_8_26 + momentum_26: prior completed bar target 0%; next bar open simulation |
| v1 | trend_8_26 AND breakout_8 | 10000.00 | 0.00 | 대기 /  / 새 신호 대기 |
| v1 | trend_8_26 + breakout_8 | 9951.22 | -48.78 | sell /  / trend_8_26 + breakout_8: prior completed bar target 0%; next bar open simulation |
| v1 | trend_8_26 AND reversion_12 | 9946.23 | -53.77 | sell /  / trend_8_26 AND reversion_12: prior completed bar target 0%; next bar open simulation |
| v1 | trend_8_26 + reversion_12 | 9926.10 | -73.90 | sell /  / trend_8_26 + reversion_12: prior completed bar target 50%; next bar open simulation |
| v1 | trend_8_26 AND volume_26 | 9925.86 | -74.14 | sell /  / trend_8_26 AND volume_26: prior completed bar target 0%; next bar open simulation |
| v1 | trend_8_26 + volume_26 | 9914.27 | -85.73 | sell /  / trend_8_26 + volume_26: prior completed bar target 0%; next bar open simulation |
| v1 | momentum_26 AND breakout_8 | 10000.00 | 0.00 | 대기 /  / 새 신호 대기 |
| v1 | momentum_26 + breakout_8 | 9958.17 | -41.83 | sell /  / momentum_26 + breakout_8: prior completed bar target 0%; next bar open simulation |
| v1 | momentum_26 AND reversion_12 | 10000.00 | 0.00 | 대기 /  / 새 신호 대기 |
| v1 | momentum_26 + reversion_12 | 9952.88 | -47.12 | sell /  / momentum_26 + reversion_12: prior completed bar target 50%; next bar open simulation |
| v1 | momentum_26 AND volume_26 | 9939.68 | -60.32 | sell /  / momentum_26 AND volume_26: prior completed bar target 0%; next bar open simulation |
| v1 | momentum_26 + volume_26 | 9921.17 | -78.83 | sell /  / momentum_26 + volume_26: prior completed bar target 0%; next bar open simulation |
| v1 | breakout_8 AND reversion_12 | 10000.00 | 0.00 | 대기 /  / 새 신호 대기 |
| v1 | breakout_8 + reversion_12 | 9974.73 | -25.27 | sell /  / breakout_8 + reversion_12: prior completed bar target 50%; next bar open simulation |
| v1 | breakout_8 AND volume_26 | 10000.00 | 0.00 | 대기 /  / 새 신호 대기 |
| v1 | breakout_8 + volume_26 | 9962.84 | -37.16 | sell /  / breakout_8 + volume_26: prior completed bar target 0%; next bar open simulation |
| v1 | reversion_12 AND volume_26 | 9946.23 | -53.77 | sell /  / reversion_12 AND volume_26: prior completed bar target 0%; next bar open simulation |
| v1 | reversion_12 + volume_26 | 9937.69 | -62.31 | sell /  / reversion_12 + volume_26: prior completed bar target 50%; next bar open simulation |
| v1 | ema_12_26 | 9902.75 | -97.25 | sell /  / EMA12 > EMA26; 조건 미충족; EMA12=770.416, EMA26=770.512 |
| v1 | macd_12_26_9 | 9916.54 | -83.46 | sell /  / MACD > 신호선 그리고 MACD > 0; 조건 미충족; MACD=0.273669, signal9=0.379179 |
| v1 | rsi_14_recovery | 10000.00 | 0.00 | 대기 /  / 새 신호 대기 |
| v1 | bollinger_20_reentry | 9963.42 | -36.58 | buy /  / 직전 종가 < 직전 하단밴드, 현재 하단밴드 <= 종가 <= SMA20 (한 봉 목표); 조건 충족; close=768.74, lower20=768.649, SMA20=770.87, previous_lower20=768.926 |
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
| v2 | buy_hold | 9834.62 | -165.38 | buy / partial / 직전 완료 봉 목표 비중 100%; 다음 봉 시가 가정 |
| v2 | trend_8_26 | 9786.41 | -213.59 | sell / filled / 직전 완료 봉 목표 비중 0%; 다음 봉 시가 가정 |
| v2 | momentum_26 | 9770.62 | -229.38 | sell / filled / 직전 완료 봉 목표 비중 0%; 다음 봉 시가 가정 |
| v2 | breakout_8 | 9598.61 | -401.39 | sell / filled / 직전 완료 봉 목표 비중 0%; 다음 봉 시가 가정 |
| v2 | reversion_12 | 9486.80 | -513.20 | buy / partial / 직전 완료 봉 목표 비중 100%; 다음 봉 시가 가정 |
| v2 | volume_26 | 9369.58 | -630.42 | sell / filled / 직전 완료 봉 목표 비중 0%; 다음 봉 시가 가정 |
| v2 | trend_8_26 AND momentum_26 | 9777.28 | -222.72 | sell / filled / 직전 완료 봉 목표 비중 0%; 다음 봉 시가 가정 |
| v2 | trend_8_26 + momentum_26 | 9778.53 | -221.47 | sell / filled / 직전 완료 봉 목표 비중 0%; 다음 봉 시가 가정 |
| v2 | trend_8_26 AND breakout_8 | 9825.21 | -174.79 | sell / filled / 직전 완료 봉 목표 비중 0%; 다음 봉 시가 가정 |
| v2 | trend_8_26 + breakout_8 | 9691.90 | -308.10 | sell / filled / 직전 완료 봉 목표 비중 0%; 다음 봉 시가 가정 |
| v2 | trend_8_26 AND reversion_12 | 9840.93 | -159.07 | sell / filled / 직전 완료 봉 목표 비중 0%; 다음 봉 시가 가정 |
| v2 | trend_8_26 + reversion_12 | 9635.10 | -364.90 | sell / filled / 직전 완료 봉 목표 비중 50%; 다음 봉 시가 가정 |
| v2 | trend_8_26 AND volume_26 | 9770.95 | -229.05 | sell / filled / 직전 완료 봉 목표 비중 0%; 다음 봉 시가 가정 |
| v2 | trend_8_26 + volume_26 | 9595.60 | -404.40 | sell / filled / 직전 완료 봉 목표 비중 0%; 다음 봉 시가 가정 |
| v2 | momentum_26 AND breakout_8 | 9783.53 | -216.47 | sell / filled / 직전 완료 봉 목표 비중 0%; 다음 봉 시가 가정 |
| v2 | momentum_26 + breakout_8 | 9684.14 | -315.86 | sell / filled / 직전 완료 봉 목표 비중 0%; 다음 봉 시가 가정 |
| v2 | momentum_26 AND reversion_12 | 9963.21 | -36.79 | sell / filled / 직전 완료 봉 목표 비중 0%; 다음 봉 시가 가정 |
| v2 | momentum_26 + reversion_12 | 9667.85 | -332.15 | sell / filled / 직전 완료 봉 목표 비중 50%; 다음 봉 시가 가정 |
| v2 | momentum_26 AND volume_26 | 9855.46 | -144.54 | sell / filled / 직전 완료 봉 목표 비중 0%; 다음 봉 시가 가정 |
| v2 | momentum_26 + volume_26 | 9628.18 | -371.82 | sell / filled / 직전 완료 봉 목표 비중 0%; 다음 봉 시가 가정 |
| v2 | breakout_8 AND reversion_12 | 10000.00 | 0.00 | 대기 /  / 새 신호 대기 |
| v2 | breakout_8 + reversion_12 | 9582.27 | -417.73 | sell / filled / 직전 완료 봉 목표 비중 50%; 다음 봉 시가 가정 |
| v2 | breakout_8 AND volume_26 | 9933.18 | -66.82 | sell / filled / 직전 완료 봉 목표 비중 0%; 다음 봉 시가 가정 |
| v2 | breakout_8 + volume_26 | 9522.95 | -477.05 | sell / filled / 직전 완료 봉 목표 비중 0%; 다음 봉 시가 가정 |
| v2 | reversion_12 AND volume_26 | 9689.01 | -310.99 | sell / filled / 직전 완료 봉 목표 비중 0%; 다음 봉 시가 가정 |
| v2 | reversion_12 + volume_26 | 9507.26 | -492.74 | sell / filled / 직전 완료 봉 목표 비중 50%; 다음 봉 시가 가정 |
| v2 | ema_12_26 | 9900.77 | -99.23 | sell / filled / EMA12 > EMA26; 조건 미충족; EMA12=770.416, EMA26=770.512; 직전 완료 봉 목표를 다음 봉 시가에 모의 적용 |
| v2 | macd_12_26_9 | 9914.56 | -85.44 | sell / filled / MACD > 신호선 그리고 MACD > 0; 조건 미충족; MACD=0.273669, signal9=0.379179; 직전 완료 봉 목표를 다음 봉 시가에 모의 적용 |
| v2 | rsi_14_recovery | 10000.00 | 0.00 | 대기 /  / 새 신호 대기 |
| v2 | bollinger_20_reentry | 9962.43 | -37.57 | buy / partial / 직전 종가 < 직전 하단밴드, 현재 하단밴드 <= 종가 <= SMA20 (한 봉 목표); 조건 충족; close=768.74, lower20=768.649, SMA20=770.87, previous_lower20=768.926; 직전 완료 봉 목표를 다음 봉 시가에 모의 적용 |
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
| cash | 0.00% | 0.00% | -0.86% | -0.00% | 0.00% |
| buy_hold | -0.44% | -0.86% | -0.86% | -0.86% | 100.00% |
| trend_8_26 | 0.97% | -2.37% | -0.86% | -0.42% | 48.95% |
| momentum_26 | -0.83% | -5.31% | -0.86% | -0.41% | 48.16% |
| breakout_8 | -0.61% | -15.63% | -0.86% | -0.18% | 21.32% |
| reversion_12 | -2.15% | -13.38% | -0.86% | -0.25% | 28.68% |
| volume_26 | -0.94% | -9.69% | -0.86% | -0.08% | 8.95% |
| trend_8_26 AND momentum_26 | 0.49% | -3.24% | -0.86% | -0.36% | 41.84% |
| trend_8_26 + momentum_26 | 0.06% | -3.65% | -0.86% | -0.42% | 48.55% |
| trend_8_26 AND breakout_8 | 0.07% | -10.28% | -0.86% | -0.11% | 12.37% |
| trend_8_26 + breakout_8 | 0.18% | -9.24% | -0.86% | -0.30% | 35.14% |
| trend_8_26 AND reversion_12 | -0.04% | -4.55% | -0.86% | -0.06% | 6.58% |
| trend_8_26 + reversion_12 | -0.60% | -7.85% | -0.86% | -0.33% | 38.82% |
| trend_8_26 AND volume_26 | -0.57% | -4.66% | -0.86% | -0.04% | 4.21% |
| trend_8_26 + volume_26 | 0.01% | -6.10% | -0.86% | -0.25% | 28.95% |
| momentum_26 AND breakout_8 | 0.37% | -10.01% | -0.86% | -0.12% | 13.42% |
| momentum_26 + breakout_8 | -0.72% | -10.62% | -0.86% | -0.30% | 34.74% |
| momentum_26 AND reversion_12 | -0.88% | -5.75% | -0.86% | -0.06% | 6.84% |
| momentum_26 + reversion_12 | -1.49% | -8.68% | -0.86% | -0.33% | 38.43% |
| momentum_26 AND volume_26 | -0.39% | -3.27% | -0.86% | -0.02% | 2.11% |
| momentum_26 + volume_26 | -0.89% | -6.36% | -0.86% | -0.25% | 28.56% |
| breakout_8 AND reversion_12 | 0.00% | 0.00% | -0.86% | -0.00% | 0.00% |
| breakout_8 + reversion_12 | -1.38% | -13.98% | -0.86% | -0.21% | 25.01% |
| breakout_8 AND volume_26 | 0.09% | -1.17% | -0.86% | -0.01% | 1.05% |
| breakout_8 + volume_26 | -0.78% | -11.80% | -0.86% | -0.13% | 15.14% |
| reversion_12 AND volume_26 | -0.81% | -5.29% | -0.86% | -0.04% | 4.47% |
| reversion_12 + volume_26 | -1.55% | -11.18% | -0.86% | -0.16% | 18.82% |
| ema_12_26 | -0.64% | -3.92% | -0.86% | -0.43% | 49.74% |
| macd_12_26_9 | 0.44% | -4.09% | -0.86% | -0.25% | 29.47% |
| rsi_14_recovery | -0.33% | -3.62% | -0.86% | -0.02% | 2.11% |
| bollinger_20_reentry | -0.99% | -7.03% | -0.86% | -0.03% | 3.95% |
| donchian_20 | 0.11% | -6.79% | -0.86% | -0.06% | 6.58% |
| atr_14_breakout | -0.04% | -5.35% | -0.86% | -0.03% | 3.95% |
| session_vwap | 1.20% | -8.89% | -0.86% | -0.44% | 51.32% |
| obv_20 | -0.81% | -9.18% | -0.86% | -0.33% | 38.42% |
| stochastic_14_3_recovery | -0.99% | -15.24% | -0.86% | -0.08% | 9.74% |
| mfi_14_recovery | -0.01% | -2.50% | -0.86% | -0.01% | 1.58% |
| adx_14_trend | -0.10% | -3.81% | -0.86% | -0.24% | 27.89% |
| aroon_25_trend | 0.72% | -2.20% | -0.86% | -0.23% | 26.32% |
| cci_20_momentum | -0.18% | -7.84% | -0.86% | -0.18% | 21.05% |
| williams_14_recovery | -0.88% | -10.76% | -0.86% | -0.06% | 6.58% |
| cmf_20_accumulation | 1.72% | -2.46% | -0.86% | -0.40% | 47.11% |
| chaikin_3_10 | 1.29% | -5.29% | -0.86% | -0.35% | 40.53% |
| roc_10_momentum | -0.06% | -0.48% | -0.86% | -0.01% | 0.79% |
| trix_15_trend | -0.53% | -3.41% | -0.86% | -0.32% | 37.63% |
| keltner_20_breakout | 0.09% | -3.62% | -0.86% | -0.09% | 10.79% |
| opening_range_30m | -0.32% | -6.41% | -0.86% | -0.27% | 31.58% |

동일 구간·초기 자금, 종료 시 청산 비용 포함. 노출 맞춤은 사후 설명용이며 v2 실제 계좌 성과가 아닙니다.
[낙폭 분해·비용 영향·전체 구간](SPY/comparison.json)

[v1 전체 기록](SPY/accounts.json) · [v2 전체 기록](SPY/accounts-v2.json)

## QQQ 계좌

| 모델 | 전략 | 평가액 USD | 손익 USD | 최근 매매·이유 |
|---|---|---:|---:|---|
| v1 | cash | 10000.00 | 0.00 | 대기 /  / 새 신호 대기 |
| v1 | buy_hold | 9858.41 | -141.59 | buy /  / buy_hold: prior completed bar target 100%; next bar open simulation |
| v1 | trend_8_26 | 9922.86 | -77.14 | sell /  / trend_8_26: prior completed bar target 0%; next bar open simulation |
| v1 | momentum_26 | 9935.02 | -64.98 | sell /  / momentum_26: prior completed bar target 0%; next bar open simulation |
| v1 | breakout_8 | 10000.00 | 0.00 | 대기 /  / 새 신호 대기 |
| v1 | reversion_12 | 9913.62 | -86.38 | buy /  / reversion_12: prior completed bar target 100%; next bar open simulation |
| v1 | volume_26 | 9959.46 | -40.54 | buy /  / volume_26: prior completed bar target 100%; next bar open simulation |
| v1 | trend_8_26 AND momentum_26 | 9951.96 | -48.04 | sell /  / trend_8_26 AND momentum_26: prior completed bar target 0%; next bar open simulation |
| v1 | trend_8_26 + momentum_26 | 9928.92 | -71.08 | sell /  / trend_8_26 + momentum_26: prior completed bar target 0%; next bar open simulation |
| v1 | trend_8_26 AND breakout_8 | 10000.00 | 0.00 | 대기 /  / 새 신호 대기 |
| v1 | trend_8_26 + breakout_8 | 9961.32 | -38.68 | sell /  / trend_8_26 + breakout_8: prior completed bar target 0%; next bar open simulation |
| v1 | trend_8_26 AND reversion_12 | 9951.96 | -48.04 | sell /  / trend_8_26 AND reversion_12: prior completed bar target 0%; next bar open simulation |
| v1 | trend_8_26 + reversion_12 | 9918.20 | -81.80 | sell /  / trend_8_26 + reversion_12: prior completed bar target 50%; next bar open simulation |
| v1 | trend_8_26 AND volume_26 | 10000.00 | 0.00 | 대기 /  / 새 신호 대기 |
| v1 | trend_8_26 + volume_26 | 9941.09 | -58.91 | buy /  / trend_8_26 + volume_26: prior completed bar target 50%; next bar open simulation |
| v1 | momentum_26 AND breakout_8 | 10000.00 | 0.00 | 대기 /  / 새 신호 대기 |
| v1 | momentum_26 + breakout_8 | 9967.44 | -32.56 | sell /  / momentum_26 + breakout_8: prior completed bar target 0%; next bar open simulation |
| v1 | momentum_26 AND reversion_12 | 9951.96 | -48.04 | sell /  / momentum_26 AND reversion_12: prior completed bar target 0%; next bar open simulation |
| v1 | momentum_26 + reversion_12 | 9924.29 | -75.71 | sell /  / momentum_26 + reversion_12: prior completed bar target 50%; next bar open simulation |
| v1 | momentum_26 AND volume_26 | 10000.00 | 0.00 | 대기 /  / 새 신호 대기 |
| v1 | momentum_26 + volume_26 | 9947.19 | -52.81 | buy /  / momentum_26 + volume_26: prior completed bar target 50%; next bar open simulation |
| v1 | breakout_8 AND reversion_12 | 10000.00 | 0.00 | 대기 /  / 새 신호 대기 |
| v1 | breakout_8 + reversion_12 | 9956.66 | -43.34 | sell /  / breakout_8 + reversion_12: prior completed bar target 50%; next bar open simulation |
| v1 | breakout_8 AND volume_26 | 10000.00 | 0.00 | 대기 /  / 새 신호 대기 |
| v1 | breakout_8 + volume_26 | 9979.69 | -20.31 | buy /  / breakout_8 + volume_26: prior completed bar target 50%; next bar open simulation |
| v1 | reversion_12 AND volume_26 | 9959.46 | -40.54 | buy /  / reversion_12 AND volume_26: prior completed bar target 100%; next bar open simulation |
| v1 | reversion_12 + volume_26 | 9936.47 | -63.53 | buy /  / reversion_12 + volume_26: prior completed bar target 100%; next bar open simulation |
| v1 | ema_12_26 | 9930.96 | -69.04 | sell /  / EMA12 > EMA26; 조건 미충족; EMA12=725.847, EMA26=725.955 |
| v1 | macd_12_26_9 | 9930.96 | -69.04 | sell /  / MACD > 신호선 그리고 MACD > 0; 조건 미충족; MACD=-0.108239, signal9=-0.536871 |
| v1 | rsi_14_recovery | 10000.00 | 0.00 | 대기 /  / 새 신호 대기 |
| v1 | bollinger_20_reentry | 9902.52 | -97.48 | buy /  / 직전 종가 < 직전 하단밴드, 현재 하단밴드 <= 종가 <= SMA20 (한 봉 목표); 조건 충족; close=718.09, lower20=716.805, SMA20=723.53, previous_lower20=717.595 |
| v1 | donchian_20 | 10000.00 | 0.00 | 대기 /  / 새 신호 대기 |
| v1 | atr_14_breakout | 10000.00 | 0.00 | 대기 /  / 새 신호 대기 |
| v1 | session_vwap | 9874.48 | -125.52 | sell /  / 종가 > 뉴욕 거래일별 누적 전형가격 VWAP; 조건 미충족; close=721.534, session_VWAP=721.817, session_volume=9.25052e+07 |
| v1 | obv_20 | 9930.96 | -69.04 | sell /  / OBV > OBV의 SMA20 그리고 종가 > EMA26; 조건 미충족; OBV=7.37006e+07, OBV_SMA20=7.17868e+07, close=723.36, EMA26=725.955 |
| v1 | stochastic_14_3_recovery | 9846.21 | -153.79 | buy /  / 직전 %K14 < 20에서 %K14가 %D3 상향 돌파 (한 봉 목표); 조건 충족; K14=13.3561, D3=8.97849, previous_K14=6.77598, previous_D3=10.6129 |
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
| v2 | buy_hold | 9539.74 | -460.26 | buy / partial / 직전 완료 봉 목표 비중 100%; 다음 봉 시가 가정 |
| v2 | trend_8_26 | 9726.12 | -273.88 | sell / filled / 직전 완료 봉 목표 비중 0%; 다음 봉 시가 가정 |
| v2 | momentum_26 | 9831.49 | -168.51 | sell / filled / 직전 완료 봉 목표 비중 0%; 다음 봉 시가 가정 |
| v2 | breakout_8 | 9669.86 | -330.14 | sell / filled / 직전 완료 봉 목표 비중 0%; 다음 봉 시가 가정 |
| v2 | reversion_12 | 9430.80 | -569.20 | buy / partial / 직전 완료 봉 목표 비중 100%; 다음 봉 시가 가정 |
| v2 | volume_26 | 9565.80 | -434.20 | 중단: 손실 한도 / sell / filled / 직전 완료 봉 목표 비중 0%; 다음 봉 시가 가정 |
| v2 | trend_8_26 AND momentum_26 | 9848.25 | -151.75 | sell / filled / 직전 완료 봉 목표 비중 0%; 다음 봉 시가 가정 |
| v2 | trend_8_26 + momentum_26 | 9778.69 | -221.31 | sell / filled / 직전 완료 봉 목표 비중 0%; 다음 봉 시가 가정 |
| v2 | trend_8_26 AND breakout_8 | 9895.83 | -104.17 | sell / filled / 직전 완료 봉 목표 비중 0%; 다음 봉 시가 가정 |
| v2 | trend_8_26 + breakout_8 | 9697.89 | -302.11 | sell / filled / 직전 완료 봉 목표 비중 0%; 다음 봉 시가 가정 |
| v2 | trend_8_26 AND reversion_12 | 9811.80 | -188.20 | sell / filled / 직전 완료 봉 목표 비중 0%; 다음 봉 시가 가정 |
| v2 | trend_8_26 + reversion_12 | 9576.99 | -423.01 | sell / filled / 직전 완료 봉 목표 비중 50%; 다음 봉 시가 가정 |
| v2 | trend_8_26 AND volume_26 | 9840.10 | -159.90 | sell / filled / 직전 완료 봉 목표 비중 0%; 다음 봉 시가 가정 |
| v2 | trend_8_26 + volume_26 | 9545.12 | -454.88 | buy / filled / 직전 완료 봉 목표 비중 50%; 다음 봉 시가 가정 |
| v2 | momentum_26 AND breakout_8 | 9960.69 | -39.31 | sell / filled / 직전 완료 봉 목표 비중 0%; 다음 봉 시가 가정 |
| v2 | momentum_26 + breakout_8 | 9750.28 | -249.72 | sell / filled / 직전 완료 봉 목표 비중 0%; 다음 봉 시가 가정 |
| v2 | momentum_26 AND reversion_12 | 9949.97 | -50.03 | sell / filled / 직전 완료 봉 목표 비중 0%; 다음 봉 시가 가정 |
| v2 | momentum_26 + reversion_12 | 9648.96 | -351.04 | sell / filled / 직전 완료 봉 목표 비중 50%; 다음 봉 시가 가정 |
| v2 | momentum_26 AND volume_26 | 9936.83 | -63.17 | sell / filled / 직전 완료 봉 목표 비중 0%; 다음 봉 시가 가정 |
| v2 | momentum_26 + volume_26 | 9596.68 | -403.32 | buy / filled / 직전 완료 봉 목표 비중 50%; 다음 봉 시가 가정 |
| v2 | breakout_8 AND reversion_12 | 10000.00 | 0.00 | 대기 /  / 새 신호 대기 |
| v2 | breakout_8 + reversion_12 | 9609.59 | -390.41 | sell / filled / 직전 완료 봉 목표 비중 50%; 다음 봉 시가 가정 |
| v2 | breakout_8 AND volume_26 | 9947.98 | -52.02 | sell / filled / 직전 완료 봉 목표 비중 0%; 다음 봉 시가 가정 |
| v2 | breakout_8 + volume_26 | 9557.62 | -442.38 | buy / filled / 직전 완료 봉 목표 비중 50%; 다음 봉 시가 가정 |
| v2 | reversion_12 AND volume_26 | 9547.64 | -452.36 | 중단: 손실 한도 / sell / filled / 직전 완료 봉 목표 비중 0%; 다음 봉 시가 가정 |
| v2 | reversion_12 + volume_26 | 9419.02 | -580.98 | buy / partial / 직전 완료 봉 목표 비중 100%; 다음 봉 시가 가정 |
| v2 | ema_12_26 | 9928.97 | -71.03 | sell / filled / EMA12 > EMA26; 조건 미충족; EMA12=725.847, EMA26=725.955; 직전 완료 봉 목표를 다음 봉 시가에 모의 적용 |
| v2 | macd_12_26_9 | 9928.97 | -71.03 | sell / filled / MACD > 신호선 그리고 MACD > 0; 조건 미충족; MACD=-0.108239, signal9=-0.536871; 직전 완료 봉 목표를 다음 봉 시가에 모의 적용 |
| v2 | rsi_14_recovery | 10000.00 | 0.00 | 대기 /  / 새 신호 대기 |
| v2 | bollinger_20_reentry | 9899.55 | -100.45 | buy / partial / 직전 종가 < 직전 하단밴드, 현재 하단밴드 <= 종가 <= SMA20 (한 봉 목표); 조건 충족; close=718.09, lower20=716.805, SMA20=723.53, previous_lower20=717.595; 직전 완료 봉 목표를 다음 봉 시가에 모의 적용 |
| v2 | donchian_20 | 10000.00 | 0.00 | 대기 /  / 새 신호 대기 |
| v2 | atr_14_breakout | 10000.00 | 0.00 | 대기 /  / 새 신호 대기 |
| v2 | session_vwap | 9870.53 | -129.47 | sell / filled / 종가 > 뉴욕 거래일별 누적 전형가격 VWAP; 조건 미충족; close=721.534, session_VWAP=721.817, session_volume=9.25052e+07; 직전 완료 봉 목표를 다음 봉 시가에 모의 적용 |
| v2 | obv_20 | 9928.97 | -71.03 | sell / filled / OBV > OBV의 SMA20 그리고 종가 > EMA26; 조건 미충족; OBV=7.37006e+07, OBV_SMA20=7.17868e+07, close=723.36, EMA26=725.955; 직전 완료 봉 목표를 다음 봉 시가에 모의 적용 |
| v2 | stochastic_14_3_recovery | 9841.29 | -158.71 | buy / partial / 직전 %K14 < 20에서 %K14가 %D3 상향 돌파 (한 봉 목표); 조건 충족; K14=13.3561, D3=8.97849, previous_K14=6.77598, previous_D3=10.6129; 직전 완료 봉 목표를 다음 봉 시가에 모의 적용 |
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
| cash | 0.00% | 0.00% | -4.15% | -0.00% | 0.00% |
| buy_hold | -3.75% | -4.15% | -4.15% | -4.15% | 100.00% |
| trend_8_26 | -0.37% | -4.07% | -4.15% | -1.90% | 45.79% |
| momentum_26 | -1.64% | -6.48% | -4.15% | -1.64% | 39.47% |
| breakout_8 | -1.46% | -16.35% | -4.15% | -0.73% | 17.63% |
| reversion_12 | -1.12% | -13.92% | -4.15% | -1.18% | 28.42% |
| volume_26 | -1.28% | -14.05% | -4.15% | -0.60% | 14.47% |
| trend_8_26 AND momentum_26 | -0.51% | -4.60% | -4.15% | -1.44% | 34.74% |
| trend_8_26 + momentum_26 | -1.00% | -5.08% | -4.15% | -1.77% | 42.63% |
| trend_8_26 AND breakout_8 | -0.32% | -9.11% | -4.15% | -0.44% | 10.53% |
| trend_8_26 + breakout_8 | -0.91% | -10.04% | -4.15% | -1.32% | 31.72% |
| trend_8_26 AND reversion_12 | 0.34% | -5.79% | -4.15% | -0.30% | 7.11% |
| trend_8_26 + reversion_12 | -0.74% | -8.56% | -4.15% | -1.54% | 37.11% |
| trend_8_26 AND volume_26 | -0.71% | -5.59% | -4.15% | -0.18% | 4.21% |
| trend_8_26 + volume_26 | -0.82% | -9.01% | -4.15% | -1.25% | 30.14% |
| momentum_26 AND breakout_8 | -0.13% | -8.56% | -4.15% | -0.43% | 10.26% |
| momentum_26 + breakout_8 | -1.55% | -11.37% | -4.15% | -1.19% | 28.56% |
| momentum_26 AND reversion_12 | -0.10% | -6.20% | -4.15% | -0.24% | 5.79% |
| momentum_26 + reversion_12 | -1.38% | -9.71% | -4.15% | -1.41% | 33.95% |
| momentum_26 AND volume_26 | -0.30% | -4.40% | -4.15% | -0.14% | 3.42% |
| momentum_26 + volume_26 | -1.45% | -10.16% | -4.15% | -1.12% | 26.98% |
| breakout_8 AND reversion_12 | 0.00% | 0.00% | -4.15% | -0.00% | 0.00% |
| breakout_8 + reversion_12 | -1.29% | -14.26% | -4.15% | -0.96% | 23.04% |
| breakout_8 AND volume_26 | 0.04% | -2.04% | -4.15% | -0.05% | 1.32% |
| breakout_8 + volume_26 | -1.37% | -13.96% | -4.15% | -0.67% | 16.06% |
| reversion_12 AND volume_26 | -1.45% | -9.01% | -4.15% | -0.37% | 8.95% |
| reversion_12 + volume_26 | -1.20% | -13.63% | -4.15% | -0.89% | 21.45% |
| ema_12_26 | 0.16% | -1.92% | -4.15% | -1.54% | 37.11% |
| macd_12_26_9 | 1.49% | -1.86% | -4.15% | -0.84% | 20.26% |
| rsi_14_recovery | -0.50% | -4.99% | -4.15% | -0.12% | 2.89% |
| bollinger_20_reentry | -0.40% | -6.48% | -4.15% | -0.16% | 3.95% |
| donchian_20 | 0.28% | -4.24% | -4.15% | -0.20% | 4.74% |
| atr_14_breakout | -0.26% | -4.76% | -4.15% | -0.13% | 3.16% |
| session_vwap | -1.31% | -12.63% | -4.15% | -2.18% | 52.37% |
| obv_20 | -1.88% | -10.91% | -4.15% | -1.13% | 27.11% |
| stochastic_14_3_recovery | -0.44% | -11.49% | -4.15% | -0.31% | 7.37% |
| mfi_14_recovery | -0.16% | -1.82% | -4.15% | -0.04% | 1.05% |
| adx_14_trend | -0.71% | -3.59% | -4.15% | -0.78% | 18.68% |
| aroon_25_trend | 1.40% | -1.95% | -4.15% | -0.82% | 19.74% |
| cci_20_momentum | -0.85% | -5.72% | -4.15% | -0.62% | 15.00% |
| williams_14_recovery | -0.68% | -10.95% | -4.15% | -0.28% | 6.84% |
| cmf_20_accumulation | -2.09% | -10.35% | -4.15% | -1.35% | 32.37% |
| chaikin_3_10 | -3.05% | -11.23% | -4.15% | -1.47% | 35.26% |
| roc_10_momentum | -0.31% | -1.56% | -4.15% | -0.09% | 2.11% |
| trix_15_trend | 0.04% | -1.63% | -4.15% | -1.29% | 31.05% |
| keltner_20_breakout | -0.73% | -4.81% | -4.15% | -0.31% | 7.37% |
| opening_range_30m | -0.35% | -6.04% | -4.15% | -0.91% | 21.84% |

동일 구간·초기 자금, 종료 시 청산 비용 포함. 노출 맞춤은 사후 설명용이며 v2 실제 계좌 성과가 아닙니다.
[낙폭 분해·비용 영향·전체 구간](QQQ/comparison.json)

[v1 전체 기록](QQQ/accounts.json) · [v2 전체 기록](QQQ/accounts-v2.json)

## IWM 계좌

| 모델 | 전략 | 평가액 USD | 손익 USD | 최근 매매·이유 |
|---|---|---:|---:|---|
| v1 | cash | 10000.00 | 0.00 | 대기 /  / 새 신호 대기 |
| v1 | buy_hold | 9857.60 | -142.40 | buy /  / buy_hold: prior completed bar target 100%; next bar open simulation |
| v1 | trend_8_26 | 9857.60 | -142.40 | buy /  / trend_8_26: prior completed bar target 100%; next bar open simulation |
| v1 | momentum_26 | 9895.73 | -104.27 | sell /  / momentum_26: prior completed bar target 0%; next bar open simulation |
| v1 | breakout_8 | 9929.38 | -70.62 | sell /  / breakout_8: prior completed bar target 0%; next bar open simulation |
| v1 | reversion_12 | 9921.70 | -78.30 | buy /  / reversion_12: prior completed bar target 100%; next bar open simulation |
| v1 | volume_26 | 9955.52 | -44.48 | buy /  / volume_26: prior completed bar target 100%; next bar open simulation |
| v1 | trend_8_26 AND momentum_26 | 9895.73 | -104.27 | sell /  / trend_8_26 AND momentum_26: prior completed bar target 0%; next bar open simulation |
| v1 | trend_8_26 + momentum_26 | 9876.65 | -123.35 | buy /  / trend_8_26 + momentum_26: prior completed bar target 50%; next bar open simulation |
| v1 | trend_8_26 AND breakout_8 | 9929.38 | -70.62 | sell /  / trend_8_26 AND breakout_8: prior completed bar target 0%; next bar open simulation |
| v1 | trend_8_26 + breakout_8 | 9893.42 | -106.58 | buy /  / trend_8_26 + breakout_8: prior completed bar target 50%; next bar open simulation |
| v1 | trend_8_26 AND reversion_12 | 9921.70 | -78.30 | buy /  / trend_8_26 AND reversion_12: prior completed bar target 100%; next bar open simulation |
| v1 | trend_8_26 + reversion_12 | 9889.56 | -110.44 | buy /  / trend_8_26 + reversion_12: prior completed bar target 100%; next bar open simulation |
| v1 | trend_8_26 AND volume_26 | 9955.52 | -44.48 | buy /  / trend_8_26 AND volume_26: prior completed bar target 100%; next bar open simulation |
| v1 | trend_8_26 + volume_26 | 9906.39 | -93.61 | buy /  / trend_8_26 + volume_26: prior completed bar target 100%; next bar open simulation |
| v1 | momentum_26 AND breakout_8 | 9929.38 | -70.62 | sell /  / momentum_26 AND breakout_8: prior completed bar target 0%; next bar open simulation |
| v1 | momentum_26 + breakout_8 | 9912.56 | -87.44 | sell /  / momentum_26 + breakout_8: prior completed bar target 0%; next bar open simulation |
| v1 | momentum_26 AND reversion_12 | 10000.00 | 0.00 | 대기 /  / 새 신호 대기 |
| v1 | momentum_26 + reversion_12 | 9928.50 | -71.50 | buy /  / momentum_26 + reversion_12: prior completed bar target 50%; next bar open simulation |
| v1 | momentum_26 AND volume_26 | 10000.00 | 0.00 | 대기 /  / 새 신호 대기 |
| v1 | momentum_26 + volume_26 | 9925.55 | -74.45 | buy /  / momentum_26 + volume_26: prior completed bar target 50%; next bar open simulation |
| v1 | breakout_8 AND reversion_12 | 10000.00 | 0.00 | 대기 /  / 새 신호 대기 |
| v1 | breakout_8 + reversion_12 | 9925.51 | -74.49 | buy /  / breakout_8 + reversion_12: prior completed bar target 50%; next bar open simulation |
| v1 | breakout_8 AND volume_26 | 10000.00 | 0.00 | 대기 /  / 새 신호 대기 |
| v1 | breakout_8 + volume_26 | 9942.41 | -57.59 | buy /  / breakout_8 + volume_26: prior completed bar target 50%; next bar open simulation |
| v1 | reversion_12 AND volume_26 | 9955.52 | -44.48 | buy /  / reversion_12 AND volume_26: prior completed bar target 100%; next bar open simulation |
| v1 | reversion_12 + volume_26 | 9938.58 | -61.42 | buy /  / reversion_12 + volume_26: prior completed bar target 100%; next bar open simulation |
| v1 | ema_12_26 | 9857.60 | -142.40 | buy /  / EMA12 > EMA26; 조건 충족; EMA12=274.113, EMA26=273.616 |
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
| v1 | aroon_25_trend | 9862.11 | -137.89 | sell /  / Aroon25 Up > 70 그리고 Down < 30 (동률이면 최신 극값); 조건 미충족; Aroon_up=68, Aroon_down=100 |
| v1 | cci_20_momentum | 9928.63 | -71.37 | sell /  / CCI20 > 100 (전형가격·평균절대편차); 조건 미충족; CCI20=90.0513 |
| v1 | williams_14_recovery | 10000.00 | 0.00 | 대기 /  / 새 신호 대기 |
| v1 | cmf_20_accumulation | 9843.27 | -156.73 | sell /  / Chaikin Money Flow20 > 0.1; 조건 미충족; CMF20=0.0663812, volume20=1.58199e+07 |
| v1 | chaikin_3_10 | 9916.70 | -83.30 | sell /  / ADL의 EMA3 - EMA10 > 0 그리고 종가 > EMA26; 조건 미충족; Chaikin3_10=-335917, ADL=-5.92841e+07, close=274.31, EMA26=274.011 |
| v1 | roc_10_momentum | 10000.00 | 0.00 | 대기 /  / 새 신호 대기 |
| v1 | trix_15_trend | 9895.73 | -104.27 | sell /  / 15봉 삼중 EMA의 1봉 변화율 TRIX > 0 그리고 종가 > EMA26; 조건 미충족; TRIX15_percent=0.0257204, close=273.74, EMA26=273.991 |
| v1 | keltner_20_breakout | 9937.31 | -62.69 | sell /  / 종가 > EMA20 + 2 x Wilder ATR14; 조건 미충족; close=274.88, upper_Keltner=275.161, EMA20=274.044, ATR14=0.558498 |
| v1 | opening_range_30m | 9968.03 | -31.97 | sell /  / 뉴욕 09:30·09:45 두 완료 봉 최고가를 10:00 이후 종가가 돌파; 자료 부족·변동폭 또는 거래량 없음: 대기; close=275.73 |
| v2 | cash | 10000.00 | 0.00 | 대기 /  / 새 신호 대기 |
| v2 | buy_hold | 9752.20 | -247.80 | buy / partial / 직전 완료 봉 목표 비중 100%; 다음 봉 시가 가정 |
| v2 | trend_8_26 | 9729.87 | -270.13 | buy / partial / 직전 완료 봉 목표 비중 100%; 다음 봉 시가 가정 |
| v2 | momentum_26 | 9767.53 | -232.47 | sell / filled / 직전 완료 봉 목표 비중 0%; 다음 봉 시가 가정 |
| v2 | breakout_8 | 9547.89 | -452.11 | sell / filled / 직전 완료 봉 목표 비중 0%; 다음 봉 시가 가정 |
| v2 | reversion_12 | 9463.04 | -536.96 | buy / partial / 직전 완료 봉 목표 비중 100%; 다음 봉 시가 가정 |
| v2 | volume_26 | 9470.10 | -529.90 | buy / partial / 직전 완료 봉 목표 비중 100%; 다음 봉 시가 가정 |
| v2 | trend_8_26 AND momentum_26 | 9918.12 | -81.88 | sell / filled / 직전 완료 봉 목표 비중 0%; 다음 봉 시가 가정 |
| v2 | trend_8_26 + momentum_26 | 9769.31 | -230.69 | buy / filled / 직전 완료 봉 목표 비중 50%; 다음 봉 시가 가정 |
| v2 | trend_8_26 AND breakout_8 | 9840.76 | -159.24 | sell / filled / 직전 완료 봉 목표 비중 0%; 다음 봉 시가 가정 |
| v2 | trend_8_26 + breakout_8 | 9658.84 | -341.16 | buy / filled / 직전 완료 봉 목표 비중 50%; 다음 봉 시가 가정 |
| v2 | trend_8_26 AND reversion_12 | 9803.47 | -196.53 | buy / partial / 직전 완료 봉 목표 비중 100%; 다음 봉 시가 가정 |
| v2 | trend_8_26 + reversion_12 | 9595.33 | -404.67 | buy / partial / 직전 완료 봉 목표 비중 100%; 다음 봉 시가 가정 |
| v2 | trend_8_26 AND volume_26 | 9817.98 | -182.02 | buy / partial / 직전 완료 봉 목표 비중 100%; 다음 봉 시가 가정 |
| v2 | trend_8_26 + volume_26 | 9619.23 | -380.77 | buy / partial / 직전 완료 봉 목표 비중 100%; 다음 봉 시가 가정 |
| v2 | momentum_26 AND breakout_8 | 9733.71 | -266.29 | sell / filled / 직전 완료 봉 목표 비중 0%; 다음 봉 시가 가정 |
| v2 | momentum_26 + breakout_8 | 9657.13 | -342.87 | sell / filled / 직전 완료 봉 목표 비중 0%; 다음 봉 시가 가정 |
| v2 | momentum_26 AND reversion_12 | 9960.59 | -39.41 | sell / filled / 직전 완료 봉 목표 비중 0%; 다음 봉 시가 가정 |
| v2 | momentum_26 + reversion_12 | 9654.12 | -345.88 | buy / filled / 직전 완료 봉 목표 비중 50%; 다음 봉 시가 가정 |
| v2 | momentum_26 AND volume_26 | 9897.79 | -102.21 | sell / filled / 직전 완료 봉 목표 비중 0%; 다음 봉 시가 가정 |
| v2 | momentum_26 + volume_26 | 9617.42 | -382.58 | buy / filled / 직전 완료 봉 목표 비중 50%; 다음 봉 시가 가정 |
| v2 | breakout_8 AND reversion_12 | 10000.00 | 0.00 | 대기 /  / 새 신호 대기 |
| v2 | breakout_8 + reversion_12 | 9544.96 | -455.04 | buy / filled / 직전 완료 봉 목표 비중 50%; 다음 봉 시가 가정 |
| v2 | breakout_8 AND volume_26 | 9746.03 | -253.97 | sell / filled / 직전 완료 봉 목표 비중 0%; 다음 봉 시가 가정 |
| v2 | breakout_8 + volume_26 | 9528.82 | -471.18 | buy / filled / 직전 완료 봉 목표 비중 50%; 다음 봉 시가 가정 |
| v2 | reversion_12 AND volume_26 | 9696.46 | -303.54 | buy / partial / 직전 완료 봉 목표 비중 100%; 다음 봉 시가 가정 |
| v2 | reversion_12 + volume_26 | 9486.24 | -513.76 | buy / partial / 직전 완료 봉 목표 비중 100%; 다음 봉 시가 가정 |
| v2 | ema_12_26 | 9856.61 | -143.39 | buy / partial / EMA12 > EMA26; 조건 충족; EMA12=274.113, EMA26=273.616; 직전 완료 봉 목표를 다음 봉 시가에 모의 적용 |
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
| v2 | aroon_25_trend | 9860.14 | -139.86 | sell / filled / Aroon25 Up > 70 그리고 Down < 30 (동률이면 최신 극값); 조건 미충족; Aroon_up=68, Aroon_down=100; 직전 완료 봉 목표를 다음 봉 시가에 모의 적용 |
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
| cash | 0.00% | 0.00% | -3.93% | -0.00% | 0.00% |
| buy_hold | -3.52% | -3.93% | -3.93% | -3.93% | 100.00% |
| trend_8_26 | -2.19% | -5.81% | -3.93% | -1.79% | 45.26% |
| momentum_26 | -2.97% | -8.51% | -3.93% | -1.57% | 39.47% |
| breakout_8 | -1.07% | -14.24% | -3.93% | -0.76% | 19.21% |
| reversion_12 | -2.75% | -15.34% | -3.93% | -1.19% | 30.00% |
| volume_26 | -2.55% | -9.65% | -3.93% | -0.35% | 8.68% |
| trend_8_26 AND momentum_26 | -1.85% | -5.89% | -3.93% | -1.37% | 34.47% |
| trend_8_26 + momentum_26 | -2.57% | -6.78% | -3.93% | -1.68% | 42.37% |
| trend_8_26 AND breakout_8 | -0.58% | -8.20% | -3.93% | -0.44% | 11.05% |
| trend_8_26 + breakout_8 | -1.62% | -9.93% | -3.93% | -1.28% | 32.24% |
| trend_8_26 AND reversion_12 | -0.73% | -5.61% | -3.93% | -0.24% | 6.05% |
| trend_8_26 + reversion_12 | -2.46% | -10.52% | -3.93% | -1.49% | 37.64% |
| trend_8_26 AND volume_26 | -1.27% | -4.93% | -3.93% | -0.15% | 3.68% |
| trend_8_26 + volume_26 | -2.36% | -7.56% | -3.93% | -1.07% | 26.98% |
| momentum_26 AND breakout_8 | -0.34% | -7.98% | -3.93% | -0.42% | 10.53% |
| momentum_26 + breakout_8 | -2.02% | -11.42% | -3.93% | -1.17% | 29.35% |
| momentum_26 AND reversion_12 | -0.08% | -3.38% | -3.93% | -0.10% | 2.63% |
| momentum_26 + reversion_12 | -2.85% | -10.69% | -3.93% | -1.38% | 34.74% |
| momentum_26 AND volume_26 | -1.32% | -3.77% | -3.93% | -0.07% | 1.84% |
| momentum_26 + volume_26 | -2.76% | -8.70% | -3.93% | -0.96% | 24.08% |
| breakout_8 AND reversion_12 | 0.00% | 0.00% | -3.93% | -0.00% | 0.00% |
| breakout_8 + reversion_12 | -1.91% | -14.08% | -3.93% | -0.98% | 24.61% |
| breakout_8 AND volume_26 | -1.30% | -3.76% | -3.93% | -0.08% | 2.11% |
| breakout_8 + volume_26 | -1.81% | -11.79% | -3.93% | -0.56% | 13.95% |
| reversion_12 AND volume_26 | -0.62% | -5.11% | -3.93% | -0.19% | 4.74% |
| reversion_12 + volume_26 | -2.65% | -11.99% | -3.93% | -0.77% | 19.35% |
| ema_12_26 | -0.59% | -3.06% | -3.93% | -1.74% | 43.95% |
| macd_12_26_9 | 1.76% | -0.78% | -3.93% | -1.08% | 27.11% |
| rsi_14_recovery | -0.28% | -4.78% | -3.93% | -0.12% | 2.89% |
| bollinger_20_reentry | -0.25% | -4.75% | -3.93% | -0.12% | 2.89% |
| donchian_20 | -0.20% | -5.10% | -3.93% | -0.22% | 5.53% |
| atr_14_breakout | -1.87% | -8.25% | -3.93% | -0.17% | 4.21% |
| session_vwap | -1.55% | -11.37% | -3.93% | -1.73% | 43.68% |
| obv_20 | -0.44% | -4.93% | -3.93% | -1.48% | 37.37% |
| stochastic_14_3_recovery | -0.87% | -13.34% | -3.93% | -0.34% | 8.42% |
| mfi_14_recovery | 0.22% | -3.50% | -3.93% | -0.09% | 2.37% |
| adx_14_trend | -0.58% | -4.27% | -3.93% | -1.25% | 31.58% |
| aroon_25_trend | -1.70% | -4.95% | -3.93% | -0.82% | 20.53% |
| cci_20_momentum | -1.95% | -7.93% | -3.93% | -0.69% | 17.37% |
| williams_14_recovery | -0.74% | -10.26% | -3.93% | -0.25% | 6.32% |
| cmf_20_accumulation | -2.35% | -8.70% | -3.93% | -0.75% | 18.95% |
| chaikin_3_10 | -3.02% | -9.70% | -3.93% | -1.31% | 32.89% |
| roc_10_momentum | -0.63% | -1.87% | -3.93% | -0.13% | 3.16% |
| trix_15_trend | -0.27% | -3.57% | -3.93% | -1.31% | 32.89% |
| keltner_20_breakout | -0.91% | -4.18% | -3.93% | -0.21% | 5.26% |
| opening_range_30m | 1.50% | -3.49% | -3.93% | -0.96% | 24.21% |

동일 구간·초기 자금, 종료 시 청산 비용 포함. 노출 맞춤은 사후 설명용이며 v2 실제 계좌 성과가 아닙니다.
[낙폭 분해·비용 영향·전체 구간](IWM/comparison.json)

[v1 전체 기록](IWM/accounts.json) · [v2 전체 기록](IWM/accounts-v2.json)

## DIA 계좌

| 모델 | 전략 | 평가액 USD | 손익 USD | 최근 매매·이유 |
|---|---|---:|---:|---|
| v1 | cash | 10000.00 | 0.00 | 대기 /  / 새 신호 대기 |
| v1 | buy_hold | 9949.30 | -50.70 | buy /  / buy_hold: prior completed bar target 100%; next bar open simulation |
| v1 | trend_8_26 | 9949.30 | -50.70 | buy /  / trend_8_26: prior completed bar target 100%; next bar open simulation |
| v1 | momentum_26 | 9949.30 | -50.70 | buy /  / momentum_26: prior completed bar target 100%; next bar open simulation |
| v1 | breakout_8 | 9940.12 | -59.88 | sell /  / breakout_8: prior completed bar target 0%; next bar open simulation |
| v1 | reversion_12 | 10000.00 | 0.00 | 대기 /  / 새 신호 대기 |
| v1 | volume_26 | 9964.16 | -35.84 | buy /  / volume_26: prior completed bar target 100%; next bar open simulation |
| v1 | trend_8_26 AND momentum_26 | 9949.30 | -50.70 | buy /  / trend_8_26 AND momentum_26: prior completed bar target 100%; next bar open simulation |
| v1 | trend_8_26 + momentum_26 | 9949.30 | -50.70 | buy /  / trend_8_26 + momentum_26: prior completed bar target 100%; next bar open simulation |
| v1 | trend_8_26 AND breakout_8 | 9940.12 | -59.88 | sell /  / trend_8_26 AND breakout_8: prior completed bar target 0%; next bar open simulation |
| v1 | trend_8_26 + breakout_8 | 9944.72 | -55.28 | buy /  / trend_8_26 + breakout_8: prior completed bar target 50%; next bar open simulation |
| v1 | trend_8_26 AND reversion_12 | 10000.00 | 0.00 | 대기 /  / 새 신호 대기 |
| v1 | trend_8_26 + reversion_12 | 9974.58 | -25.42 | buy /  / trend_8_26 + reversion_12: prior completed bar target 50%; next bar open simulation |
| v1 | trend_8_26 AND volume_26 | 9964.16 | -35.84 | buy /  / trend_8_26 AND volume_26: prior completed bar target 100%; next bar open simulation |
| v1 | trend_8_26 + volume_26 | 9956.69 | -43.31 | buy /  / trend_8_26 + volume_26: prior completed bar target 100%; next bar open simulation |
| v1 | momentum_26 AND breakout_8 | 9940.12 | -59.88 | sell /  / momentum_26 AND breakout_8: prior completed bar target 0%; next bar open simulation |
| v1 | momentum_26 + breakout_8 | 9944.72 | -55.28 | buy /  / momentum_26 + breakout_8: prior completed bar target 50%; next bar open simulation |
| v1 | momentum_26 AND reversion_12 | 10000.00 | 0.00 | 대기 /  / 새 신호 대기 |
| v1 | momentum_26 + reversion_12 | 9974.58 | -25.42 | buy /  / momentum_26 + reversion_12: prior completed bar target 50%; next bar open simulation |
| v1 | momentum_26 AND volume_26 | 9964.16 | -35.84 | buy /  / momentum_26 AND volume_26: prior completed bar target 100%; next bar open simulation |
| v1 | momentum_26 + volume_26 | 9956.69 | -43.31 | buy /  / momentum_26 + volume_26: prior completed bar target 100%; next bar open simulation |
| v1 | breakout_8 AND reversion_12 | 10000.00 | 0.00 | 대기 /  / 새 신호 대기 |
| v1 | breakout_8 + reversion_12 | 9970.03 | -29.97 | sell /  / breakout_8 + reversion_12: prior completed bar target 0%; next bar open simulation |
| v1 | breakout_8 AND volume_26 | 10000.00 | 0.00 | 대기 /  / 새 신호 대기 |
| v1 | breakout_8 + volume_26 | 9952.13 | -47.87 | buy /  / breakout_8 + volume_26: prior completed bar target 50%; next bar open simulation |
| v1 | reversion_12 AND volume_26 | 10000.00 | 0.00 | 대기 /  / 새 신호 대기 |
| v1 | reversion_12 + volume_26 | 9982.05 | -17.95 | buy /  / reversion_12 + volume_26: prior completed bar target 50%; next bar open simulation |
| v1 | ema_12_26 | 9949.30 | -50.70 | buy /  / EMA12 > EMA26; 조건 충족; EMA12=520.818, EMA26=519.784 |
| v1 | macd_12_26_9 | 9941.64 | -58.36 | sell /  / MACD > 신호선 그리고 MACD > 0; 조건 미충족; MACD=1.23542, signal9=1.25143 |
| v1 | rsi_14_recovery | 10000.00 | 0.00 | 대기 /  / 새 신호 대기 |
| v1 | bollinger_20_reentry | 10000.00 | 0.00 | 대기 /  / 새 신호 대기 |
| v1 | donchian_20 | 9940.12 | -59.88 | sell /  / 종가 > 현재 봉을 제외한 직전 20봉 최고가; 조건 미충족; close=522.89, prior_high20=525.09 |
| v1 | atr_14_breakout | 9972.44 | -27.56 | sell /  / 종가 > 직전 종가 + 직전 ATR14 그리고 종가 > EMA26; 조건 미충족; close=524.65, threshold=524.777, prior_ATR14=0.84688, EMA26=520.429 |
| v1 | session_vwap | 9960.84 | -39.16 | sell /  / 종가 > 뉴욕 거래일별 누적 전형가격 VWAP; 조건 미충족; close=522.89, session_VWAP=523.72, session_volume=975370 |
| v1 | obv_20 | 9924.53 | -75.47 | sell /  / OBV > OBV의 SMA20 그리고 종가 > EMA26; 조건 미충족; OBV=-5.35236e+06, OBV_SMA20=-5.09617e+06, close=522.08, EMA26=521.373 |
| v1 | stochastic_14_3_recovery | 10000.00 | 0.00 | 대기 /  / 새 신호 대기 |
| v1 | mfi_14_recovery | 10000.00 | 0.00 | 대기 /  / 새 신호 대기 |
| v1 | adx_14_trend | 9949.30 | -50.70 | buy /  / Wilder ADX14 >= 25 그리고 +DI14 > -DI14; 조건 충족; ADX14=38.0858, plus_DI14=35.3559, minus_DI14=16.277 |
| v1 | aroon_25_trend | 9949.30 | -50.70 | buy /  / Aroon25 Up > 70 그리고 Down < 30 (동률이면 최신 극값); 조건 충족; Aroon_up=92, Aroon_down=4 |
| v1 | cci_20_momentum | 9954.56 | -45.44 | sell /  / CCI20 > 100 (전형가격·평균절대편차); 조건 미충족; CCI20=83.6046 |
| v1 | williams_14_recovery | 10000.00 | 0.00 | 대기 /  / 새 신호 대기 |
| v1 | cmf_20_accumulation | 9927.80 | -72.20 | sell /  / Chaikin Money Flow20 > 0.1; 조건 미충족; CMF20=0.0502896, volume20=2.48879e+06 |
| v1 | chaikin_3_10 | 9926.34 | -73.66 | sell /  / ADL의 EMA3 - EMA10 > 0 그리고 종가 > EMA26; 조건 미충족; Chaikin3_10=-14655, ADL=-1.49709e+07, close=522.196, EMA26=521.317 |
| v1 | roc_10_momentum | 10000.00 | 0.00 | 대기 /  / 새 신호 대기 |
| v1 | trix_15_trend | 9949.30 | -50.70 | buy /  / 15봉 삼중 EMA의 1봉 변화율 TRIX > 0 그리고 종가 > EMA26; 조건 충족; TRIX15_percent=0.0323703, close=521.24, EMA26=519.784 |
| v1 | keltner_20_breakout | 9940.12 | -59.88 | sell /  / 종가 > EMA20 + 2 x Wilder ATR14; 조건 미충족; close=522.89, upper_Keltner=523.089, EMA20=521.145, ATR14=0.971947 |
| v1 | opening_range_30m | 9980.84 | -19.16 | sell /  / 뉴욕 09:30·09:45 두 완료 봉 최고가를 10:00 이후 종가가 돌파; 자료 부족·변동폭 또는 거래량 없음: 대기; close=523.93 |
| v2 | cash | 10000.00 | 0.00 | 대기 /  / 새 신호 대기 |
| v2 | buy_hold | 10072.56 | 72.56 | buy / partial / 직전 완료 봉 목표 비중 100%; 다음 봉 시가 가정 |
| v2 | trend_8_26 | 9884.84 | -115.16 | buy / partial / 직전 완료 봉 목표 비중 100%; 다음 봉 시가 가정 |
| v2 | momentum_26 | 9993.53 | -6.47 | buy / partial / 직전 완료 봉 목표 비중 100%; 다음 봉 시가 가정 |
| v2 | breakout_8 | 9466.63 | -533.37 | sell / filled / 직전 완료 봉 목표 비중 0%; 다음 봉 시가 가정 |
| v2 | reversion_12 | 9698.03 | -301.97 | sell / filled / 직전 완료 봉 목표 비중 0%; 다음 봉 시가 가정 |
| v2 | volume_26 | 9682.41 | -317.59 | buy / partial / 직전 완료 봉 목표 비중 100%; 다음 봉 시가 가정 |
| v2 | trend_8_26 AND momentum_26 | 9988.89 | -11.11 | buy / partial / 직전 완료 봉 목표 비중 100%; 다음 봉 시가 가정 |
| v2 | trend_8_26 + momentum_26 | 9939.10 | -60.90 | buy / partial / 직전 완료 봉 목표 비중 100%; 다음 봉 시가 가정 |
| v2 | trend_8_26 AND breakout_8 | 9626.81 | -373.19 | sell / filled / 직전 완료 봉 목표 비중 0%; 다음 봉 시가 가정 |
| v2 | trend_8_26 + breakout_8 | 9673.56 | -326.44 | buy / filled / 직전 완료 봉 목표 비중 50%; 다음 봉 시가 가정 |
| v2 | trend_8_26 AND reversion_12 | 9810.77 | -189.23 | sell / filled / 직전 완료 봉 목표 비중 0%; 다음 봉 시가 가정 |
| v2 | trend_8_26 + reversion_12 | 9790.70 | -209.30 | buy / filled / 직전 완료 봉 목표 비중 50%; 다음 봉 시가 가정 |
| v2 | trend_8_26 AND volume_26 | 9822.57 | -177.43 | buy / partial / 직전 완료 봉 목표 비중 100%; 다음 봉 시가 가정 |
| v2 | trend_8_26 + volume_26 | 9803.59 | -196.41 | buy / partial / 직전 완료 봉 목표 비중 100%; 다음 봉 시가 가정 |
| v2 | momentum_26 AND breakout_8 | 9615.85 | -384.15 | sell / filled / 직전 완료 봉 목표 비중 0%; 다음 봉 시가 가정 |
| v2 | momentum_26 + breakout_8 | 9726.66 | -273.34 | buy / filled / 직전 완료 봉 목표 비중 50%; 다음 봉 시가 가정 |
| v2 | momentum_26 AND reversion_12 | 9955.97 | -44.03 | sell / filled / 직전 완료 봉 목표 비중 0%; 다음 봉 시가 가정 |
| v2 | momentum_26 + reversion_12 | 9844.45 | -155.55 | buy / filled / 직전 완료 봉 목표 비중 50%; 다음 봉 시가 가정 |
| v2 | momentum_26 AND volume_26 | 9755.36 | -244.64 | buy / partial / 직전 완료 봉 목표 비중 100%; 다음 봉 시가 가정 |
| v2 | momentum_26 + volume_26 | 9878.19 | -121.81 | buy / partial / 직전 완료 봉 목표 비중 100%; 다음 봉 시가 가정 |
| v2 | breakout_8 AND reversion_12 | 10000.00 | 0.00 | 대기 /  / 새 신호 대기 |
| v2 | breakout_8 + reversion_12 | 9581.22 | -418.78 | sell / filled / 직전 완료 봉 목표 비중 0%; 다음 봉 시가 가정 |
| v2 | breakout_8 AND volume_26 | 9796.56 | -203.44 | sell / filled / 직전 완료 봉 목표 비중 0%; 다음 봉 시가 가정 |
| v2 | breakout_8 + volume_26 | 9573.75 | -426.25 | buy / filled / 직전 완료 봉 목표 비중 50%; 다음 봉 시가 가정 |
| v2 | reversion_12 AND volume_26 | 10000.00 | 0.00 | 대기 /  / 새 신호 대기 |
| v2 | reversion_12 + volume_26 | 9689.93 | -310.07 | buy / filled / 직전 완료 봉 목표 비중 50%; 다음 봉 시가 가정 |
| v2 | ema_12_26 | 9948.31 | -51.69 | buy / partial / EMA12 > EMA26; 조건 충족; EMA12=520.818, EMA26=519.784; 직전 완료 봉 목표를 다음 봉 시가에 모의 적용 |
| v2 | macd_12_26_9 | 9939.65 | -60.35 | sell / filled / MACD > 신호선 그리고 MACD > 0; 조건 미충족; MACD=1.23542, signal9=1.25143; 직전 완료 봉 목표를 다음 봉 시가에 모의 적용 |
| v2 | rsi_14_recovery | 10000.00 | 0.00 | 대기 /  / 새 신호 대기 |
| v2 | bollinger_20_reentry | 10000.00 | 0.00 | 대기 /  / 새 신호 대기 |
| v2 | donchian_20 | 9938.13 | -61.87 | sell / filled / 종가 > 현재 봉을 제외한 직전 20봉 최고가; 조건 미충족; close=522.89, prior_high20=525.09; 직전 완료 봉 목표를 다음 봉 시가에 모의 적용 |
| v2 | atr_14_breakout | 9970.44 | -29.56 | sell / filled / 종가 > 직전 종가 + 직전 ATR14 그리고 종가 > EMA26; 조건 미충족; close=524.65, threshold=524.777, prior_ATR14=0.84688, EMA26=520.429; 직전 완료 봉 목표를 다음 봉 시가에 모의 적용 |
| v2 | session_vwap | 9958.85 | -41.15 | sell / filled / 종가 > 뉴욕 거래일별 누적 전형가격 VWAP; 조건 미충족; close=522.89, session_VWAP=523.72, session_volume=975370; 직전 완료 봉 목표를 다음 봉 시가에 모의 적용 |
| v2 | obv_20 | 9922.55 | -77.45 | sell / filled / OBV > OBV의 SMA20 그리고 종가 > EMA26; 조건 미충족; OBV=-5.35236e+06, OBV_SMA20=-5.09617e+06, close=522.08, EMA26=521.373; 직전 완료 봉 목표를 다음 봉 시가에 모의 적용 |
| v2 | stochastic_14_3_recovery | 10000.00 | 0.00 | 대기 /  / 새 신호 대기 |
| v2 | mfi_14_recovery | 10000.00 | 0.00 | 대기 /  / 새 신호 대기 |
| v2 | adx_14_trend | 9948.31 | -51.69 | buy / partial / Wilder ADX14 >= 25 그리고 +DI14 > -DI14; 조건 충족; ADX14=38.0858, plus_DI14=35.3559, minus_DI14=16.277; 직전 완료 봉 목표를 다음 봉 시가에 모의 적용 |
| v2 | aroon_25_trend | 9948.31 | -51.69 | buy / partial / Aroon25 Up > 70 그리고 Down < 30 (동률이면 최신 극값); 조건 충족; Aroon_up=92, Aroon_down=4; 직전 완료 봉 목표를 다음 봉 시가에 모의 적용 |
| v2 | cci_20_momentum | 9952.57 | -47.43 | sell / filled / CCI20 > 100 (전형가격·평균절대편차); 조건 미충족; CCI20=83.6046; 직전 완료 봉 목표를 다음 봉 시가에 모의 적용 |
| v2 | williams_14_recovery | 10000.00 | 0.00 | 대기 /  / 새 신호 대기 |
| v2 | cmf_20_accumulation | 9925.82 | -74.18 | sell / filled / Chaikin Money Flow20 > 0.1; 조건 미충족; CMF20=0.0502896, volume20=2.48879e+06; 직전 완료 봉 목표를 다음 봉 시가에 모의 적용 |
| v2 | chaikin_3_10 | 9924.35 | -75.65 | sell / filled / ADL의 EMA3 - EMA10 > 0 그리고 종가 > EMA26; 조건 미충족; Chaikin3_10=-14655, ADL=-1.49709e+07, close=522.196, EMA26=521.317; 직전 완료 봉 목표를 다음 봉 시가에 모의 적용 |
| v2 | roc_10_momentum | 10000.00 | 0.00 | 대기 /  / 새 신호 대기 |
| v2 | trix_15_trend | 9948.31 | -51.69 | buy / partial / 15봉 삼중 EMA의 1봉 변화율 TRIX > 0 그리고 종가 > EMA26; 조건 충족; TRIX15_percent=0.0323703, close=521.24, EMA26=519.784; 직전 완료 봉 목표를 다음 봉 시가에 모의 적용 |
| v2 | keltner_20_breakout | 9938.13 | -61.87 | sell / filled / 종가 > EMA20 + 2 x Wilder ATR14; 조건 미충족; close=522.89, upper_Keltner=523.089, EMA20=521.145, ATR14=0.971947; 직전 완료 봉 목표를 다음 봉 시가에 모의 적용 |
| v2 | opening_range_30m | 9978.85 | -21.15 | sell / filled / 뉴욕 09:30·09:45 두 완료 봉 최고가를 10:00 이후 종가가 돌파; 자료 부족·변동폭 또는 거래량 없음: 대기; close=523.93; 직전 완료 봉 목표를 다음 봉 시가에 모의 적용 |

### 같은 기간의 비용·노출 비교 (사후 연구)

| 전략 | 비용 전 | 비용 후 | 100% 보유 | 같은 평균 노출 보유 | 평균 노출 |
|---|---:|---:|---:|---:|---:|
| cash | 0.00% | 0.00% | 0.40% | 0.00% | 0.00% |
| buy_hold | 0.83% | 0.40% | 0.40% | 0.40% | 100.00% |
| trend_8_26 | 1.14% | -3.43% | 0.40% | 0.23% | 56.05% |
| momentum_26 | -0.19% | -4.30% | 0.40% | 0.21% | 52.37% |
| breakout_8 | -0.13% | -17.33% | 0.40% | 0.10% | 23.68% |
| reversion_12 | -1.36% | -9.30% | 0.40% | 0.10% | 24.74% |
| volume_26 | -1.06% | -11.30% | 0.40% | 0.04% | 11.05% |
| trend_8_26 AND momentum_26 | 1.28% | -2.89% | 0.40% | 0.19% | 46.58% |
| trend_8_26 + momentum_26 | 0.48% | -3.86% | 0.40% | 0.22% | 54.21% |
| trend_8_26 AND breakout_8 | 0.44% | -11.82% | 0.40% | 0.06% | 15.53% |
| trend_8_26 + breakout_8 | 0.51% | -10.46% | 0.40% | 0.16% | 39.88% |
| trend_8_26 AND reversion_12 | 0.37% | -4.56% | 0.40% | 0.03% | 6.32% |
| trend_8_26 + reversion_12 | -0.11% | -6.03% | 0.40% | 0.16% | 40.40% |
| trend_8_26 AND volume_26 | 0.49% | -4.85% | 0.40% | 0.02% | 5.26% |
| trend_8_26 + volume_26 | 0.04% | -7.26% | 0.40% | 0.14% | 33.56% |
| momentum_26 AND breakout_8 | -0.36% | -12.15% | 0.40% | 0.06% | 15.79% |
| momentum_26 + breakout_8 | -0.15% | -10.86% | 0.40% | 0.15% | 38.03% |
| momentum_26 AND reversion_12 | -0.18% | -3.88% | 0.40% | 0.02% | 5.79% |
| momentum_26 + reversion_12 | -0.77% | -6.05% | 0.40% | 0.16% | 38.56% |
| momentum_26 AND volume_26 | -0.47% | -5.76% | 0.40% | 0.02% | 4.74% |
| momentum_26 + volume_26 | -0.62% | -7.09% | 0.40% | 0.13% | 31.71% |
| breakout_8 AND reversion_12 | 0.00% | 0.00% | 0.40% | 0.00% | 0.00% |
| breakout_8 + reversion_12 | -0.74% | -13.06% | 0.40% | 0.10% | 24.22% |
| breakout_8 AND volume_26 | -0.87% | -4.55% | 0.40% | 0.01% | 3.16% |
| breakout_8 + volume_26 | -0.59% | -13.65% | 0.40% | 0.07% | 17.38% |
| reversion_12 AND volume_26 | -0.20% | -5.11% | 0.40% | 0.02% | 3.95% |
| reversion_12 + volume_26 | -1.21% | -10.31% | 0.40% | 0.07% | 17.90% |
| ema_12_26 | 0.05% | -2.44% | 0.40% | 0.21% | 50.79% |
| macd_12_26_9 | 1.61% | -1.75% | 0.40% | 0.12% | 28.68% |
| rsi_14_recovery | 0.01% | -2.07% | 0.40% | 0.01% | 1.32% |
| bollinger_20_reentry | -0.25% | -5.16% | 0.40% | 0.01% | 3.16% |
| donchian_20 | 0.36% | -5.77% | 0.40% | 0.03% | 8.16% |
| atr_14_breakout | -1.05% | -8.25% | 0.40% | 0.02% | 5.53% |
| session_vwap | 1.11% | -6.64% | 0.40% | 0.21% | 50.79% |
| obv_20 | -0.02% | -8.46% | 0.40% | 0.18% | 44.47% |
| stochastic_14_3_recovery | 0.79% | -11.14% | 0.40% | 0.03% | 7.89% |
| mfi_14_recovery | -0.06% | -2.95% | 0.40% | 0.01% | 1.84% |
| adx_14_trend | -0.55% | -4.64% | 0.40% | 0.15% | 37.11% |
| aroon_25_trend | 0.79% | -2.54% | 0.40% | 0.11% | 26.05% |
| cci_20_momentum | 0.66% | -5.09% | 0.40% | 0.10% | 23.95% |
| williams_14_recovery | 1.01% | -6.74% | 0.40% | 0.02% | 5.00% |
| cmf_20_accumulation | 0.66% | -6.28% | 0.40% | 0.13% | 31.84% |
| chaikin_3_10 | 1.18% | -8.52% | 0.40% | 0.17% | 43.16% |
| roc_10_momentum | 0.15% | -0.27% | 0.40% | 0.01% | 1.32% |
| trix_15_trend | -0.24% | -3.94% | 0.40% | 0.18% | 43.95% |
| keltner_20_breakout | 0.33% | -5.79% | 0.40% | 0.07% | 16.84% |
| opening_range_30m | 0.89% | -5.27% | 0.40% | 0.09% | 22.37% |

동일 구간·초기 자금, 종료 시 청산 비용 포함. 노출 맞춤은 사후 설명용이며 v2 실제 계좌 성과가 아닙니다.
[낙폭 분해·비용 영향·전체 구간](DIA/comparison.json)

[v1 전체 기록](DIA/accounts.json) · [v2 전체 기록](DIA/accounts-v2.json)

## MSFT 계좌

| 모델 | 전략 | 평가액 USD | 손익 USD | 최근 매매·이유 |
|---|---|---:|---:|---|
| v1 | cash | 10000.00 | 0.00 | 대기 /  / 새 신호 대기 |
| v1 | buy_hold | 9746.70 | -253.30 | buy /  / buy_hold: prior completed bar target 100%; next bar open simulation |
| v1 | trend_8_26 | 9853.68 | -146.32 | sell /  / trend_8_26: prior completed bar target 0%; next bar open simulation |
| v1 | momentum_26 | 9839.32 | -160.68 | sell /  / momentum_26: prior completed bar target 0%; next bar open simulation |
| v1 | breakout_8 | 10000.00 | 0.00 | 대기 /  / 새 신호 대기 |
| v1 | reversion_12 | 9815.82 | -184.18 | buy /  / reversion_12: prior completed bar target 100%; next bar open simulation |
| v1 | volume_26 | 9938.00 | -62.00 | sell /  / volume_26: prior completed bar target 0%; next bar open simulation |
| v1 | trend_8_26 AND momentum_26 | 9853.68 | -146.32 | sell /  / trend_8_26 AND momentum_26: prior completed bar target 0%; next bar open simulation |
| v1 | trend_8_26 + momentum_26 | 9846.52 | -153.48 | sell /  / trend_8_26 + momentum_26: prior completed bar target 0%; next bar open simulation |
| v1 | trend_8_26 AND breakout_8 | 10000.00 | 0.00 | 대기 /  / 새 신호 대기 |
| v1 | trend_8_26 + breakout_8 | 9926.58 | -73.42 | sell /  / trend_8_26 + breakout_8: prior completed bar target 0%; next bar open simulation |
| v1 | trend_8_26 AND reversion_12 | 9923.56 | -76.44 | sell /  / trend_8_26 AND reversion_12: prior completed bar target 0%; next bar open simulation |
| v1 | trend_8_26 + reversion_12 | 9834.74 | -165.26 | sell /  / trend_8_26 + reversion_12: prior completed bar target 50%; next bar open simulation |
| v1 | trend_8_26 AND volume_26 | 10000.00 | 0.00 | 대기 /  / 새 신호 대기 |
| v1 | trend_8_26 + volume_26 | 9895.73 | -104.27 | sell /  / trend_8_26 + volume_26: prior completed bar target 0%; next bar open simulation |
| v1 | momentum_26 AND breakout_8 | 10000.00 | 0.00 | 대기 /  / 새 신호 대기 |
| v1 | momentum_26 + breakout_8 | 9919.33 | -80.67 | sell /  / momentum_26 + breakout_8: prior completed bar target 0%; next bar open simulation |
| v1 | momentum_26 AND reversion_12 | 9909.10 | -90.90 | sell /  / momentum_26 AND reversion_12: prior completed bar target 0%; next bar open simulation |
| v1 | momentum_26 + reversion_12 | 9827.57 | -172.43 | sell /  / momentum_26 + reversion_12: prior completed bar target 50%; next bar open simulation |
| v1 | momentum_26 AND volume_26 | 10000.00 | 0.00 | 대기 /  / 새 신호 대기 |
| v1 | momentum_26 + volume_26 | 9888.51 | -111.49 | sell /  / momentum_26 + volume_26: prior completed bar target 0%; next bar open simulation |
| v1 | breakout_8 AND reversion_12 | 10000.00 | 0.00 | 대기 /  / 새 신호 대기 |
| v1 | breakout_8 + reversion_12 | 9907.46 | -92.54 | sell /  / breakout_8 + reversion_12: prior completed bar target 50%; next bar open simulation |
| v1 | breakout_8 AND volume_26 | 10000.00 | 0.00 | 대기 /  / 새 신호 대기 |
| v1 | breakout_8 + volume_26 | 9968.93 | -31.07 | sell /  / breakout_8 + volume_26: prior completed bar target 0%; next bar open simulation |
| v1 | reversion_12 AND volume_26 | 9938.00 | -62.00 | sell /  / reversion_12 AND volume_26: prior completed bar target 0%; next bar open simulation |
| v1 | reversion_12 + volume_26 | 9876.69 | -123.31 | sell /  / reversion_12 + volume_26: prior completed bar target 50%; next bar open simulation |
| v1 | ema_12_26 | 9853.68 | -146.32 | sell /  / EMA12 > EMA26; 조건 미충족; EMA12=538.192, EMA26=538.342 |
| v1 | macd_12_26_9 | 9889.94 | -110.06 | sell /  / MACD > 신호선 그리고 MACD > 0; 조건 미충족; MACD=0.536125, signal9=0.712825 |
| v1 | rsi_14_recovery | 10000.00 | 0.00 | 대기 /  / 새 신호 대기 |
| v1 | bollinger_20_reentry | 9931.47 | -68.53 | sell /  / 직전 종가 < 직전 하단밴드, 현재 하단밴드 <= 종가 <= SMA20 (한 봉 목표); 조건 미충족; close=534.48, lower20=535.11, SMA20=538.768, previous_lower20=535.929 |
| v1 | donchian_20 | 10000.00 | 0.00 | 대기 /  / 새 신호 대기 |
| v1 | atr_14_breakout | 10000.00 | 0.00 | 대기 /  / 새 신호 대기 |
| v1 | session_vwap | 9889.94 | -110.06 | sell /  / 종가 > 뉴욕 거래일별 누적 전형가격 VWAP; 조건 미충족; close=537.34, session_VWAP=538.663, session_volume=3.36828e+06 |
| v1 | obv_20 | 9889.94 | -110.06 | sell /  / OBV > OBV의 SMA20 그리고 종가 > EMA26; 조건 미충족; OBV=1.44955e+08, OBV_SMA20=1.34631e+08, close=537.34, EMA26=538.834 |
| v1 | stochastic_14_3_recovery | 9861.43 | -138.57 | buy /  / 직전 %K14 < 20에서 %K14가 %D3 상향 돌파 (한 봉 목표); 조건 충족; K14=6.59071, D3=4.39686, previous_K14=1.73165, previous_D3=3.92762 |
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
| v2 | buy_hold | 9799.88 | -200.12 | buy / partial / 직전 완료 봉 목표 비중 100%; 다음 봉 시가 가정 |
| v2 | trend_8_26 | 9790.17 | -209.83 | sell / filled / 직전 완료 봉 목표 비중 0%; 다음 봉 시가 가정 |
| v2 | momentum_26 | 9886.18 | -113.82 | sell / filled / 직전 완료 봉 목표 비중 0%; 다음 봉 시가 가정 |
| v2 | breakout_8 | 9799.48 | -200.52 | sell / filled / 직전 완료 봉 목표 비중 0%; 다음 봉 시가 가정 |
| v2 | reversion_12 | 9440.52 | -559.48 | buy / partial / 직전 완료 봉 목표 비중 100%; 다음 봉 시가 가정 |
| v2 | volume_26 | 9626.55 | -373.45 | sell / filled / 직전 완료 봉 목표 비중 0%; 다음 봉 시가 가정 |
| v2 | trend_8_26 AND momentum_26 | 9751.13 | -248.87 | sell / filled / 직전 완료 봉 목표 비중 0%; 다음 봉 시가 가정 |
| v2 | trend_8_26 + momentum_26 | 9838.34 | -161.66 | sell / filled / 직전 완료 봉 목표 비중 0%; 다음 봉 시가 가정 |
| v2 | trend_8_26 AND breakout_8 | 9639.29 | -360.71 | sell / filled / 직전 완료 봉 목표 비중 0%; 다음 봉 시가 가정 |
| v2 | trend_8_26 + breakout_8 | 9815.63 | -184.37 | sell / filled / 직전 완료 봉 목표 비중 0%; 다음 봉 시가 가정 |
| v2 | trend_8_26 AND reversion_12 | 9822.46 | -177.54 | sell / filled / 직전 완료 봉 목표 비중 0%; 다음 봉 시가 가정 |
| v2 | trend_8_26 + reversion_12 | 9613.44 | -386.56 | sell / filled / 직전 완료 봉 목표 비중 50%; 다음 봉 시가 가정 |
| v2 | trend_8_26 AND volume_26 | 9948.66 | -51.34 | sell / filled / 직전 완료 봉 목표 비중 0%; 다음 봉 시가 가정 |
| v2 | trend_8_26 + volume_26 | 9728.21 | -271.79 | sell / filled / 직전 완료 봉 목표 비중 0%; 다음 봉 시가 가정 |
| v2 | momentum_26 AND breakout_8 | 9794.38 | -205.62 | sell / filled / 직전 완료 봉 목표 비중 0%; 다음 봉 시가 가정 |
| v2 | momentum_26 + breakout_8 | 9842.81 | -157.19 | sell / filled / 직전 완료 봉 목표 비중 0%; 다음 봉 시가 가정 |
| v2 | momentum_26 AND reversion_12 | 9735.61 | -264.39 | sell / filled / 직전 완료 봉 목표 비중 0%; 다음 봉 시가 가정 |
| v2 | momentum_26 + reversion_12 | 9660.59 | -339.41 | sell / filled / 직전 완료 봉 목표 비중 50%; 다음 봉 시가 가정 |
| v2 | momentum_26 AND volume_26 | 9871.26 | -128.74 | sell / filled / 직전 완료 봉 목표 비중 0%; 다음 봉 시가 가정 |
| v2 | momentum_26 + volume_26 | 9775.92 | -224.08 | sell / filled / 직전 완료 봉 목표 비중 0%; 다음 봉 시가 가정 |
| v2 | breakout_8 AND reversion_12 | 10000.00 | 0.00 | 대기 /  / 새 신호 대기 |
| v2 | breakout_8 + reversion_12 | 9638.33 | -361.67 | sell / filled / 직전 완료 봉 목표 비중 50%; 다음 봉 시가 가정 |
| v2 | breakout_8 AND volume_26 | 9938.59 | -61.41 | sell / filled / 직전 완료 봉 목표 비중 0%; 다음 봉 시가 가정 |
| v2 | breakout_8 + volume_26 | 9733.07 | -266.93 | sell / filled / 직전 완료 봉 목표 비중 0%; 다음 봉 시가 가정 |
| v2 | reversion_12 AND volume_26 | 9699.57 | -300.43 | sell / filled / 직전 완료 봉 목표 비중 0%; 다음 봉 시가 가정 |
| v2 | reversion_12 + volume_26 | 9532.91 | -467.09 | sell / filled / 직전 완료 봉 목표 비중 50%; 다음 봉 시가 가정 |
| v2 | ema_12_26 | 9851.71 | -148.29 | sell / filled / EMA12 > EMA26; 조건 미충족; EMA12=538.192, EMA26=538.342; 직전 완료 봉 목표를 다음 봉 시가에 모의 적용 |
| v2 | macd_12_26_9 | 9887.97 | -112.03 | sell / filled / MACD > 신호선 그리고 MACD > 0; 조건 미충족; MACD=0.536125, signal9=0.712825; 직전 완료 봉 목표를 다음 봉 시가에 모의 적용 |
| v2 | rsi_14_recovery | 10000.00 | 0.00 | 대기 /  / 새 신호 대기 |
| v2 | bollinger_20_reentry | 9929.48 | -70.52 | sell / filled / 직전 종가 < 직전 하단밴드, 현재 하단밴드 <= 종가 <= SMA20 (한 봉 목표); 조건 미충족; close=534.48, lower20=535.11, SMA20=538.768, previous_lower20=535.929; 직전 완료 봉 목표를 다음 봉 시가에 모의 적용 |
| v2 | donchian_20 | 10000.00 | 0.00 | 대기 /  / 새 신호 대기 |
| v2 | atr_14_breakout | 10000.00 | 0.00 | 대기 /  / 새 신호 대기 |
| v2 | session_vwap | 9887.97 | -112.03 | sell / filled / 종가 > 뉴욕 거래일별 누적 전형가격 VWAP; 조건 미충족; close=537.34, session_VWAP=538.663, session_volume=3.36828e+06; 직전 완료 봉 목표를 다음 봉 시가에 모의 적용 |
| v2 | obv_20 | 9887.97 | -112.03 | sell / filled / OBV > OBV의 SMA20 그리고 종가 > EMA26; 조건 미충족; OBV=1.44955e+08, OBV_SMA20=1.34631e+08, close=537.34, EMA26=538.834; 직전 완료 봉 목표를 다음 봉 시가에 모의 적용 |
| v2 | stochastic_14_3_recovery | 9858.47 | -141.53 | buy / partial / 직전 %K14 < 20에서 %K14가 %D3 상향 돌파 (한 봉 목표); 조건 충족; K14=6.59071, D3=4.39686, previous_K14=1.73165, previous_D3=3.92762; 직전 완료 봉 목표를 다음 봉 시가에 모의 적용 |
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
| cash | 0.00% | 0.00% | 1.62% | 0.00% | 0.00% |
| buy_hold | 2.04% | 1.62% | 1.62% | 1.62% | 100.00% |
| trend_8_26 | -1.64% | -5.29% | 1.62% | 0.93% | 57.89% |
| momentum_26 | -0.66% | -6.33% | 1.62% | 0.94% | 58.68% |
| breakout_8 | 5.09% | -8.89% | 1.62% | 0.32% | 19.74% |
| reversion_12 | -5.63% | -14.32% | 1.62% | 0.41% | 25.79% |
| volume_26 | 2.21% | -6.42% | 1.62% | 0.14% | 8.68% |
| trend_8_26 AND momentum_26 | -1.90% | -7.50% | 1.62% | 0.84% | 52.11% |
| trend_8_26 + momentum_26 | -1.14% | -5.80% | 1.62% | 0.94% | 58.29% |
| trend_8_26 AND breakout_8 | 0.68% | -8.98% | 1.62% | 0.20% | 12.63% |
| trend_8_26 + breakout_8 | 1.69% | -6.71% | 1.62% | 0.62% | 38.82% |
| trend_8_26 AND reversion_12 | -3.74% | -9.24% | 1.62% | 0.13% | 7.89% |
| trend_8_26 + reversion_12 | -3.64% | -9.54% | 1.62% | 0.67% | 41.85% |
| trend_8_26 AND volume_26 | 3.46% | 0.46% | 1.62% | 0.04% | 2.63% |
| trend_8_26 + volume_26 | 0.29% | -5.06% | 1.62% | 0.53% | 33.29% |
| momentum_26 AND breakout_8 | 2.61% | -7.61% | 1.62% | 0.21% | 12.89% |
| momentum_26 + breakout_8 | 2.19% | -7.03% | 1.62% | 0.63% | 39.22% |
| momentum_26 AND reversion_12 | -3.23% | -9.52% | 1.62% | 0.15% | 9.47% |
| momentum_26 + reversion_12 | -3.15% | -10.04% | 1.62% | 0.68% | 42.24% |
| momentum_26 AND volume_26 | 1.80% | -2.38% | 1.62% | 0.05% | 3.42% |
| momentum_26 + volume_26 | 0.78% | -5.19% | 1.62% | 0.54% | 33.69% |
| breakout_8 AND reversion_12 | 0.00% | 0.00% | 1.62% | 0.00% | 0.00% |
| breakout_8 + reversion_12 | -0.39% | -11.08% | 1.62% | 0.36% | 22.77% |
| breakout_8 AND volume_26 | 2.07% | -0.47% | 1.62% | 0.03% | 1.84% |
| breakout_8 + volume_26 | 3.65% | -6.69% | 1.62% | 0.23% | 14.22% |
| reversion_12 AND volume_26 | -2.48% | -6.49% | 1.62% | 0.06% | 3.95% |
| reversion_12 + volume_26 | -1.77% | -10.26% | 1.62% | 0.28% | 17.24% |
| ema_12_26 | -1.05% | -4.72% | 1.62% | 0.99% | 61.58% |
| macd_12_26_9 | 0.71% | -4.24% | 1.62% | 0.53% | 32.89% |
| rsi_14_recovery | -0.46% | -1.71% | 1.62% | 0.01% | 0.79% |
| bollinger_20_reentry | -0.45% | -3.34% | 1.62% | 0.03% | 1.84% |
| donchian_20 | 1.84% | -3.17% | 1.62% | 0.07% | 4.47% |
| atr_14_breakout | 1.50% | -3.89% | 1.62% | 0.06% | 3.68% |
| session_vwap | 2.46% | -5.40% | 1.62% | 0.75% | 46.84% |
| obv_20 | 3.86% | -5.31% | 1.62% | 0.83% | 51.58% |
| stochastic_14_3_recovery | -0.61% | -10.52% | 1.62% | 0.10% | 6.58% |
| mfi_14_recovery | 1.04% | -1.88% | 1.62% | 0.03% | 1.84% |
| adx_14_trend | 0.95% | -1.98% | 1.62% | 0.73% | 45.26% |
| aroon_25_trend | -0.06% | -4.97% | 1.62% | 0.34% | 21.05% |
| cci_20_momentum | 2.74% | -3.93% | 1.62% | 0.33% | 20.79% |
| williams_14_recovery | -0.28% | -9.09% | 1.62% | 0.09% | 5.79% |
| cmf_20_accumulation | 0.27% | -5.85% | 1.62% | 0.58% | 36.32% |
| chaikin_3_10 | 3.12% | -5.19% | 1.62% | 0.73% | 45.26% |
| roc_10_momentum | -0.20% | -4.30% | 1.62% | 0.23% | 14.21% |
| trix_15_trend | -1.91% | -5.94% | 1.62% | 0.76% | 47.63% |
| keltner_20_breakout | 1.12% | -3.85% | 1.62% | 0.21% | 13.42% |
| opening_range_30m | -2.37% | -7.56% | 1.62% | 0.39% | 24.21% |

동일 구간·초기 자금, 종료 시 청산 비용 포함. 노출 맞춤은 사후 설명용이며 v2 실제 계좌 성과가 아닙니다.
[낙폭 분해·비용 영향·전체 구간](MSFT/comparison.json)

[v1 전체 기록](MSFT/accounts.json) · [v2 전체 기록](MSFT/accounts-v2.json)

## JPM 계좌

| 모델 | 전략 | 평가액 USD | 손익 USD | 최근 매매·이유 |
|---|---|---:|---:|---|
| v1 | cash | 10000.00 | 0.00 | 대기 /  / 새 신호 대기 |
| v1 | buy_hold | 10030.09 | 30.09 | buy /  / buy_hold: prior completed bar target 100%; next bar open simulation |
| v1 | trend_8_26 | 10030.09 | 30.09 | buy /  / trend_8_26: prior completed bar target 100%; next bar open simulation |
| v1 | momentum_26 | 10030.09 | 30.09 | buy /  / momentum_26: prior completed bar target 100%; next bar open simulation |
| v1 | breakout_8 | 9915.55 | -84.45 | sell /  / breakout_8: prior completed bar target 0%; next bar open simulation |
| v1 | reversion_12 | 10000.00 | 0.00 | 대기 /  / 새 신호 대기 |
| v1 | volume_26 | 10035.68 | 35.68 | sell /  / volume_26: prior completed bar target 0%; next bar open simulation |
| v1 | trend_8_26 AND momentum_26 | 10030.09 | 30.09 | buy /  / trend_8_26 AND momentum_26: prior completed bar target 100%; next bar open simulation |
| v1 | trend_8_26 + momentum_26 | 10030.09 | 30.09 | buy /  / trend_8_26 + momentum_26: prior completed bar target 100%; next bar open simulation |
| v1 | trend_8_26 AND breakout_8 | 9915.55 | -84.45 | sell /  / trend_8_26 AND breakout_8: prior completed bar target 0%; next bar open simulation |
| v1 | trend_8_26 + breakout_8 | 9972.75 | -27.25 | buy /  / trend_8_26 + breakout_8: prior completed bar target 50%; next bar open simulation |
| v1 | trend_8_26 AND reversion_12 | 10000.00 | 0.00 | 대기 /  / 새 신호 대기 |
| v1 | trend_8_26 + reversion_12 | 10015.05 | 15.05 | buy /  / trend_8_26 + reversion_12: prior completed bar target 50%; next bar open simulation |
| v1 | trend_8_26 AND volume_26 | 10035.68 | 35.68 | sell /  / trend_8_26 AND volume_26: prior completed bar target 0%; next bar open simulation |
| v1 | trend_8_26 + volume_26 | 10032.86 | 32.86 | buy /  / trend_8_26 + volume_26: prior completed bar target 50%; next bar open simulation |
| v1 | momentum_26 AND breakout_8 | 9915.55 | -84.45 | sell /  / momentum_26 AND breakout_8: prior completed bar target 0%; next bar open simulation |
| v1 | momentum_26 + breakout_8 | 9972.75 | -27.25 | buy /  / momentum_26 + breakout_8: prior completed bar target 50%; next bar open simulation |
| v1 | momentum_26 AND reversion_12 | 10000.00 | 0.00 | 대기 /  / 새 신호 대기 |
| v1 | momentum_26 + reversion_12 | 10015.05 | 15.05 | buy /  / momentum_26 + reversion_12: prior completed bar target 50%; next bar open simulation |
| v1 | momentum_26 AND volume_26 | 10035.68 | 35.68 | sell /  / momentum_26 AND volume_26: prior completed bar target 0%; next bar open simulation |
| v1 | momentum_26 + volume_26 | 10032.86 | 32.86 | buy /  / momentum_26 + volume_26: prior completed bar target 50%; next bar open simulation |
| v1 | breakout_8 AND reversion_12 | 10000.00 | 0.00 | 대기 /  / 새 신호 대기 |
| v1 | breakout_8 + reversion_12 | 9957.75 | -42.25 | sell /  / breakout_8 + reversion_12: prior completed bar target 0%; next bar open simulation |
| v1 | breakout_8 AND volume_26 | 10035.68 | 35.68 | sell /  / breakout_8 AND volume_26: prior completed bar target 0%; next bar open simulation |
| v1 | breakout_8 + volume_26 | 9975.44 | -24.56 | sell /  / breakout_8 + volume_26: prior completed bar target 0%; next bar open simulation |
| v1 | reversion_12 AND volume_26 | 10000.00 | 0.00 | 대기 /  / 새 신호 대기 |
| v1 | reversion_12 + volume_26 | 10017.88 | 17.88 | sell /  / reversion_12 + volume_26: prior completed bar target 0%; next bar open simulation |
| v1 | ema_12_26 | 10030.09 | 30.09 | buy /  / EMA12 > EMA26; 조건 충족; EMA12=334.708, EMA26=334.451 |
| v1 | macd_12_26_9 | 10030.09 | 30.09 | buy /  / MACD > 신호선 그리고 MACD > 0; 조건 충족; MACD=0.256679, signal9=0.133159 |
| v1 | rsi_14_recovery | 10000.00 | 0.00 | 대기 /  / 새 신호 대기 |
| v1 | bollinger_20_reentry | 10000.00 | 0.00 | 대기 /  / 새 신호 대기 |
| v1 | donchian_20 | 9872.30 | -127.70 | sell /  / 종가 > 현재 봉을 제외한 직전 20봉 최고가; 조건 미충족; close=343.037, prior_high20=344.4 |
| v1 | atr_14_breakout | 9886.92 | -113.08 | sell /  / 종가 > 직전 종가 + 직전 ATR14 그리고 종가 > EMA26; 조건 미충족; close=342.515, threshold=344.598, prior_ATR14=1.50332, EMA26=336.975 |
| v1 | session_vwap | 9936.81 | -63.19 | sell /  / 종가 > 뉴욕 거래일별 누적 전형가격 VWAP; 조건 미충족; close=342, session_VWAP=342.233, session_volume=3.25898e+06 |
| v1 | obv_20 | 10030.09 | 30.09 | buy /  / OBV > OBV의 SMA20 그리고 종가 > EMA26; 조건 충족; OBV=-1.09065e+07, OBV_SMA20=-1.16181e+07, close=335.52, EMA26=334.451 |
| v1 | stochastic_14_3_recovery | 10000.00 | 0.00 | 대기 /  / 새 신호 대기 |
| v1 | mfi_14_recovery | 10000.00 | 0.00 | 대기 /  / 새 신호 대기 |
| v1 | adx_14_trend | 9936.55 | -63.45 | buy /  / Wilder ADX14 >= 25 그리고 +DI14 > -DI14; 조건 충족; ADX14=26.8739, plus_DI14=46.4083, minus_DI14=10.993 |
| v1 | aroon_25_trend | 9954.53 | -45.47 | buy /  / Aroon25 Up > 70 그리고 Down < 30 (동률이면 최신 극값); 조건 충족; Aroon_up=100, Aroon_down=4 |
| v1 | cci_20_momentum | 10050.62 | 50.62 | sell /  / CCI20 > 100 (전형가격·평균절대편차); 조건 미충족; CCI20=93.5627 |
| v1 | williams_14_recovery | 10000.00 | 0.00 | 대기 /  / 새 신호 대기 |
| v1 | cmf_20_accumulation | 9954.53 | -45.47 | buy /  / Chaikin Money Flow20 > 0.1; 조건 충족; CMF20=0.219142, volume20=5.48047e+06 |
| v1 | chaikin_3_10 | 10030.09 | 30.09 | buy /  / ADL의 EMA3 - EMA10 > 0 그리고 종가 > EMA26; 조건 충족; Chaikin3_10=213543, ADL=-5.96061e+06, close=335.52, EMA26=334.451 |
| v1 | roc_10_momentum | 9954.53 | -45.47 | buy /  / 10봉 ROC > 1% 그리고 종가 > EMA26; 조건 충족; ROC10_percent=2.4431, close=342.58, EMA26=335.053 |
| v1 | trix_15_trend | 10030.09 | 30.09 | buy /  / 15봉 삼중 EMA의 1봉 변화율 TRIX > 0 그리고 종가 > EMA26; 조건 충족; TRIX15_percent=0.00554135, close=335.52, EMA26=334.451 |
| v1 | keltner_20_breakout | 9946.99 | -53.01 | sell /  / 종가 > EMA20 + 2 x Wilder ATR14; 조건 미충족; close=342, upper_Keltner=342.276, EMA20=339.397, ATR14=1.43933 |
| v1 | opening_range_30m | 9927.81 | -72.19 | sell /  / 뉴욕 09:30·09:45 두 완료 봉 최고가를 10:00 이후 종가가 돌파; 조건 미충족; close=343.037, opening_high=343.75 |
| v2 | cash | 10000.00 | 0.00 | 대기 /  / 새 신호 대기 |
| v2 | buy_hold | 10197.69 | 197.69 | buy / partial / 직전 완료 봉 목표 비중 100%; 다음 봉 시가 가정 |
| v2 | trend_8_26 | 10038.30 | 38.30 | buy / partial / 직전 완료 봉 목표 비중 100%; 다음 봉 시가 가정 |
| v2 | momentum_26 | 9533.24 | -466.76 | buy / partial / 직전 완료 봉 목표 비중 100%; 다음 봉 시가 가정 |
| v2 | breakout_8 | 9251.20 | -748.80 | sell / filled / 직전 완료 봉 목표 비중 0%; 다음 봉 시가 가정 |
| v2 | reversion_12 | 9991.97 | -8.03 | sell / filled / 직전 완료 봉 목표 비중 0%; 다음 봉 시가 가정 |
| v2 | volume_26 | 9859.79 | -140.21 | sell / filled / 직전 완료 봉 목표 비중 0%; 다음 봉 시가 가정 |
| v2 | trend_8_26 AND momentum_26 | 9997.11 | -2.89 | buy / partial / 직전 완료 봉 목표 비중 100%; 다음 봉 시가 가정 |
| v2 | trend_8_26 + momentum_26 | 9803.62 | -196.38 | buy / partial / 직전 완료 봉 목표 비중 100%; 다음 봉 시가 가정 |
| v2 | trend_8_26 AND breakout_8 | 9287.76 | -712.24 | sell / filled / 직전 완료 봉 목표 비중 0%; 다음 봉 시가 가정 |
| v2 | trend_8_26 + breakout_8 | 9637.88 | -362.12 | buy / filled / 직전 완료 봉 목표 비중 50%; 다음 봉 시가 가정 |
| v2 | trend_8_26 AND reversion_12 | 9981.61 | -18.39 | sell / filled / 직전 완료 봉 목표 비중 0%; 다음 봉 시가 가정 |
| v2 | trend_8_26 + reversion_12 | 10057.51 | 57.51 | buy / filled / 직전 완료 봉 목표 비중 50%; 다음 봉 시가 가정 |
| v2 | trend_8_26 AND volume_26 | 9833.30 | -166.70 | sell / filled / 직전 완료 봉 목표 비중 0%; 다음 봉 시가 가정 |
| v2 | trend_8_26 + volume_26 | 9949.47 | -50.53 | buy / filled / 직전 완료 봉 목표 비중 50%; 다음 봉 시가 가정 |
| v2 | momentum_26 AND breakout_8 | 9232.70 | -767.30 | sell / filled / 직전 완료 봉 목표 비중 0%; 다음 봉 시가 가정 |
| v2 | momentum_26 + breakout_8 | 9412.62 | -587.38 | buy / filled / 직전 완료 봉 목표 비중 50%; 다음 봉 시가 가정 |
| v2 | momentum_26 AND reversion_12 | 9950.76 | -49.24 | sell / filled / 직전 완료 봉 목표 비중 0%; 다음 봉 시가 가정 |
| v2 | momentum_26 + reversion_12 | 9884.26 | -115.74 | buy / filled / 직전 완료 봉 목표 비중 50%; 다음 봉 시가 가정 |
| v2 | momentum_26 AND volume_26 | 9833.30 | -166.70 | sell / filled / 직전 완료 봉 목표 비중 0%; 다음 봉 시가 가정 |
| v2 | momentum_26 + volume_26 | 9757.66 | -242.34 | buy / filled / 직전 완료 봉 목표 비중 50%; 다음 봉 시가 가정 |
| v2 | breakout_8 AND reversion_12 | 10000.00 | 0.00 | 대기 /  / 새 신호 대기 |
| v2 | breakout_8 + reversion_12 | 9655.22 | -344.78 | sell / filled / 직전 완료 봉 목표 비중 0%; 다음 봉 시가 가정 |
| v2 | breakout_8 AND volume_26 | 9926.66 | -73.34 | sell / filled / 직전 완료 봉 목표 비중 0%; 다음 봉 시가 가정 |
| v2 | breakout_8 + volume_26 | 9570.88 | -429.12 | sell / filled / 직전 완료 봉 목표 비중 0%; 다음 봉 시가 가정 |
| v2 | reversion_12 AND volume_26 | 10051.38 | 51.38 | sell / filled / 직전 완료 봉 목표 비중 0%; 다음 봉 시가 가정 |
| v2 | reversion_12 + volume_26 | 9946.87 | -53.13 | sell / filled / 직전 완료 봉 목표 비중 0%; 다음 봉 시가 가정 |
| v2 | ema_12_26 | 10029.09 | 29.09 | buy / partial / EMA12 > EMA26; 조건 충족; EMA12=334.708, EMA26=334.451; 직전 완료 봉 목표를 다음 봉 시가에 모의 적용 |
| v2 | macd_12_26_9 | 10029.09 | 29.09 | buy / partial / MACD > 신호선 그리고 MACD > 0; 조건 충족; MACD=0.256679, signal9=0.133159; 직전 완료 봉 목표를 다음 봉 시가에 모의 적용 |
| v2 | rsi_14_recovery | 10000.00 | 0.00 | 대기 /  / 새 신호 대기 |
| v2 | bollinger_20_reentry | 10000.00 | 0.00 | 대기 /  / 새 신호 대기 |
| v2 | donchian_20 | 9868.35 | -131.65 | sell / filled / 종가 > 현재 봉을 제외한 직전 20봉 최고가; 조건 미충족; close=343.037, prior_high20=344.4; 직전 완료 봉 목표를 다음 봉 시가에 모의 적용 |
| v2 | atr_14_breakout | 9882.97 | -117.03 | sell / filled / 종가 > 직전 종가 + 직전 ATR14 그리고 종가 > EMA26; 조건 미충족; close=342.515, threshold=344.598, prior_ATR14=1.50332, EMA26=336.975; 직전 완료 봉 목표를 다음 봉 시가에 모의 적용 |
| v2 | session_vwap | 9932.83 | -67.17 | sell / filled / 종가 > 뉴욕 거래일별 누적 전형가격 VWAP; 조건 미충족; close=342, session_VWAP=342.233, session_volume=3.25898e+06; 직전 완료 봉 목표를 다음 봉 시가에 모의 적용 |
| v2 | obv_20 | 10029.09 | 29.09 | buy / partial / OBV > OBV의 SMA20 그리고 종가 > EMA26; 조건 충족; OBV=-1.09065e+07, OBV_SMA20=-1.16181e+07, close=335.52, EMA26=334.451; 직전 완료 봉 목표를 다음 봉 시가에 모의 적용 |
| v2 | stochastic_14_3_recovery | 10000.00 | 0.00 | 대기 /  / 새 신호 대기 |
| v2 | mfi_14_recovery | 10000.00 | 0.00 | 대기 /  / 새 신호 대기 |
| v2 | adx_14_trend | 9935.55 | -64.45 | buy / partial / Wilder ADX14 >= 25 그리고 +DI14 > -DI14; 조건 충족; ADX14=26.8739, plus_DI14=46.4083, minus_DI14=10.993; 직전 완료 봉 목표를 다음 봉 시가에 모의 적용 |
| v2 | aroon_25_trend | 9953.54 | -46.46 | buy / partial / Aroon25 Up > 70 그리고 Down < 30 (동률이면 최신 극값); 조건 충족; Aroon_up=100, Aroon_down=4; 직전 완료 봉 목표를 다음 봉 시가에 모의 적용 |
| v2 | cci_20_momentum | 10048.61 | 48.61 | sell / filled / CCI20 > 100 (전형가격·평균절대편차); 조건 미충족; CCI20=93.5627; 직전 완료 봉 목표를 다음 봉 시가에 모의 적용 |
| v2 | williams_14_recovery | 10000.00 | 0.00 | 대기 /  / 새 신호 대기 |
| v2 | cmf_20_accumulation | 9953.54 | -46.46 | buy / partial / Chaikin Money Flow20 > 0.1; 조건 충족; CMF20=0.219142, volume20=5.48047e+06; 직전 완료 봉 목표를 다음 봉 시가에 모의 적용 |
| v2 | chaikin_3_10 | 10029.09 | 29.09 | buy / partial / ADL의 EMA3 - EMA10 > 0 그리고 종가 > EMA26; 조건 충족; Chaikin3_10=213543, ADL=-5.96061e+06, close=335.52, EMA26=334.451; 직전 완료 봉 목표를 다음 봉 시가에 모의 적용 |
| v2 | roc_10_momentum | 9953.54 | -46.46 | buy / partial / 10봉 ROC > 1% 그리고 종가 > EMA26; 조건 충족; ROC10_percent=2.4431, close=342.58, EMA26=335.053; 직전 완료 봉 목표를 다음 봉 시가에 모의 적용 |
| v2 | trix_15_trend | 10029.09 | 29.09 | buy / partial / 15봉 삼중 EMA의 1봉 변화율 TRIX > 0 그리고 종가 > EMA26; 조건 충족; TRIX15_percent=0.00554135, close=335.52, EMA26=334.451; 직전 완료 봉 목표를 다음 봉 시가에 모의 적용 |
| v2 | keltner_20_breakout | 9945.00 | -55.00 | sell / filled / 종가 > EMA20 + 2 x Wilder ATR14; 조건 미충족; close=342, upper_Keltner=342.276, EMA20=339.397, ATR14=1.43933; 직전 완료 봉 목표를 다음 봉 시가에 모의 적용 |
| v2 | opening_range_30m | 9925.82 | -74.18 | sell / filled / 뉴욕 09:30·09:45 두 완료 봉 최고가를 10:00 이후 종가가 돌파; 조건 미충족; close=343.037, opening_high=343.75; 직전 완료 봉 목표를 다음 봉 시가에 모의 적용 |

### 같은 기간의 비용·노출 비교 (사후 연구)

| 전략 | 비용 전 | 비용 후 | 100% 보유 | 같은 평균 노출 보유 | 평균 노출 |
|---|---:|---:|---:|---:|---:|
| cash | 0.00% | 0.00% | -0.32% | -0.00% | 0.00% |
| buy_hold | 0.10% | -0.32% | -0.32% | -0.32% | 100.00% |
| trend_8_26 | 1.65% | -2.53% | -0.32% | -0.17% | 52.37% |
| momentum_26 | -1.43% | -8.23% | -0.32% | -0.15% | 46.84% |
| breakout_8 | -3.78% | -19.00% | -0.32% | -0.07% | 20.26% |
| reversion_12 | 4.63% | -9.67% | -0.32% | -0.09% | 26.58% |
| volume_26 | -0.11% | -6.20% | -0.32% | -0.02% | 6.84% |
| trend_8_26 AND momentum_26 | 1.74% | -3.26% | -0.32% | -0.13% | 41.05% |
| trend_8_26 + momentum_26 | 0.10% | -5.22% | -0.32% | -0.16% | 49.61% |
| trend_8_26 AND breakout_8 | -3.83% | -14.50% | -0.32% | -0.04% | 12.89% |
| trend_8_26 + breakout_8 | -1.09% | -10.95% | -0.32% | -0.12% | 36.32% |
| trend_8_26 AND reversion_12 | 2.82% | -3.46% | -0.32% | -0.02% | 6.58% |
| trend_8_26 + reversion_12 | 3.15% | -5.58% | -0.32% | -0.13% | 39.48% |
| trend_8_26 AND volume_26 | -0.58% | -4.67% | -0.32% | -0.01% | 4.21% |
| trend_8_26 + volume_26 | 0.79% | -4.38% | -0.32% | -0.10% | 29.61% |
| momentum_26 AND breakout_8 | -2.67% | -13.47% | -0.32% | -0.04% | 12.63% |
| momentum_26 + breakout_8 | -2.59% | -13.58% | -0.32% | -0.11% | 33.56% |
| momentum_26 AND reversion_12 | 2.89% | -3.80% | -0.32% | -0.02% | 5.53% |
| momentum_26 + reversion_12 | 1.58% | -7.41% | -0.32% | -0.12% | 36.72% |
| momentum_26 AND volume_26 | 0.21% | -2.70% | -0.32% | -0.01% | 2.89% |
| momentum_26 + volume_26 | -0.75% | -6.63% | -0.32% | -0.09% | 26.85% |
| breakout_8 AND reversion_12 | 0.00% | 0.00% | -0.32% | -0.00% | 0.00% |
| breakout_8 + reversion_12 | 0.36% | -13.02% | -0.32% | -0.08% | 23.43% |
| breakout_8 AND volume_26 | -0.51% | -2.17% | -0.32% | -0.00% | 1.05% |
| breakout_8 + volume_26 | -1.95% | -11.73% | -0.32% | -0.04% | 13.56% |
| reversion_12 AND volume_26 | 1.25% | -2.10% | -0.32% | -0.01% | 3.42% |
| reversion_12 + volume_26 | 2.25% | -7.18% | -0.32% | -0.05% | 16.72% |
| ema_12_26 | 1.30% | -2.05% | -0.32% | -0.16% | 48.68% |
| macd_12_26_9 | 1.20% | -2.96% | -0.32% | -0.10% | 30.53% |
| rsi_14_recovery | 0.14% | -2.35% | -0.32% | -0.01% | 1.58% |
| bollinger_20_reentry | 0.44% | -5.30% | -0.32% | -0.01% | 3.68% |
| donchian_20 | -1.79% | -4.63% | -0.32% | -0.01% | 2.89% |
| atr_14_breakout | -1.13% | -7.55% | -0.32% | -0.01% | 4.47% |
| session_vwap | 1.13% | -8.57% | -0.32% | -0.16% | 49.21% |
| obv_20 | -3.83% | -14.86% | -0.32% | -0.10% | 31.84% |
| stochastic_14_3_recovery | -1.86% | -12.75% | -0.32% | -0.02% | 7.37% |
| mfi_14_recovery | 0.16% | -1.50% | -0.32% | -0.00% | 1.05% |
| adx_14_trend | -1.95% | -5.19% | -0.32% | -0.09% | 27.89% |
| aroon_25_trend | -0.52% | -5.01% | -0.32% | -0.07% | 21.84% |
| cci_20_momentum | -2.59% | -10.44% | -0.32% | -0.05% | 15.26% |
| williams_14_recovery | -2.54% | -12.98% | -0.32% | -0.02% | 7.11% |
| cmf_20_accumulation | -2.80% | -11.38% | -0.32% | -0.11% | 35.26% |
| chaikin_3_10 | 1.69% | -6.89% | -0.32% | -0.11% | 34.74% |
| roc_10_momentum | -0.78% | -3.25% | -0.32% | -0.02% | 7.63% |
| trix_15_trend | 0.26% | -6.65% | -0.32% | -0.11% | 35.00% |
| keltner_20_breakout | -1.19% | -3.65% | -0.32% | -0.01% | 3.95% |
| opening_range_30m | -0.21% | -3.91% | -0.32% | -0.06% | 18.42% |

동일 구간·초기 자금, 종료 시 청산 비용 포함. 노출 맞춤은 사후 설명용이며 v2 실제 계좌 성과가 아닙니다.
[낙폭 분해·비용 영향·전체 구간](JPM/comparison.json)

[v1 전체 기록](JPM/accounts.json) · [v2 전체 기록](JPM/accounts-v2.json)

## XOM 계좌

| 모델 | 전략 | 평가액 USD | 손익 USD | 최근 매매·이유 |
|---|---|---:|---:|---|
| v1 | cash | 10000.00 | 0.00 | 대기 /  / 새 신호 대기 |
| v1 | buy_hold | 9966.74 | -33.26 | buy /  / buy_hold: prior completed bar target 100%; next bar open simulation |
| v1 | trend_8_26 | 10027.25 | 27.25 | buy /  / trend_8_26: prior completed bar target 100%; next bar open simulation |
| v1 | momentum_26 | 9994.21 | -5.79 | buy /  / momentum_26: prior completed bar target 100%; next bar open simulation |
| v1 | breakout_8 | 9826.90 | -173.10 | sell /  / breakout_8: prior completed bar target 0%; next bar open simulation |
| v1 | reversion_12 | 10000.00 | 0.00 | 대기 /  / 새 신호 대기 |
| v1 | volume_26 | 9907.12 | -92.88 | buy /  / volume_26: prior completed bar target 100%; next bar open simulation |
| v1 | trend_8_26 AND momentum_26 | 10027.25 | 27.25 | buy /  / trend_8_26 AND momentum_26: prior completed bar target 100%; next bar open simulation |
| v1 | trend_8_26 + momentum_26 | 10010.70 | 10.70 | buy /  / trend_8_26 + momentum_26: prior completed bar target 100%; next bar open simulation |
| v1 | trend_8_26 AND breakout_8 | 9948.21 | -51.79 | sell /  / trend_8_26 AND breakout_8: prior completed bar target 0%; next bar open simulation |
| v1 | trend_8_26 + breakout_8 | 9946.45 | -53.55 | buy /  / trend_8_26 + breakout_8: prior completed bar target 50%; next bar open simulation |
| v1 | trend_8_26 AND reversion_12 | 10000.00 | 0.00 | 대기 /  / 새 신호 대기 |
| v1 | trend_8_26 + reversion_12 | 10013.59 | 13.59 | buy /  / trend_8_26 + reversion_12: prior completed bar target 50%; next bar open simulation |
| v1 | trend_8_26 AND volume_26 | 10003.22 | 3.22 | buy /  / trend_8_26 AND volume_26: prior completed bar target 100%; next bar open simulation |
| v1 | trend_8_26 + volume_26 | 9966.96 | -33.04 | buy /  / trend_8_26 + volume_26: prior completed bar target 100%; next bar open simulation |
| v1 | momentum_26 AND breakout_8 | 9875.85 | -124.15 | sell /  / momentum_26 AND breakout_8: prior completed bar target 0%; next bar open simulation |
| v1 | momentum_26 + breakout_8 | 9910.23 | -89.77 | buy /  / momentum_26 + breakout_8: prior completed bar target 50%; next bar open simulation |
| v1 | momentum_26 AND reversion_12 | 10000.00 | 0.00 | 대기 /  / 새 신호 대기 |
| v1 | momentum_26 + reversion_12 | 9997.08 | -2.92 | buy /  / momentum_26 + reversion_12: prior completed bar target 50%; next bar open simulation |
| v1 | momentum_26 AND volume_26 | 10003.22 | 3.22 | buy /  / momentum_26 AND volume_26: prior completed bar target 100%; next bar open simulation |
| v1 | momentum_26 + volume_26 | 9950.53 | -49.47 | buy /  / momentum_26 + volume_26: prior completed bar target 100%; next bar open simulation |
| v1 | breakout_8 AND reversion_12 | 10000.00 | 0.00 | 대기 /  / 새 신호 대기 |
| v1 | breakout_8 + reversion_12 | 9913.03 | -86.97 | sell /  / breakout_8 + reversion_12: prior completed bar target 0%; next bar open simulation |
| v1 | breakout_8 AND volume_26 | 9950.44 | -49.56 | sell /  / breakout_8 AND volume_26: prior completed bar target 0%; next bar open simulation |
| v1 | breakout_8 + volume_26 | 9866.89 | -133.11 | buy /  / breakout_8 + volume_26: prior completed bar target 50%; next bar open simulation |
| v1 | reversion_12 AND volume_26 | 10000.00 | 0.00 | 대기 /  / 새 신호 대기 |
| v1 | reversion_12 + volume_26 | 9953.44 | -46.56 | buy /  / reversion_12 + volume_26: prior completed bar target 50%; next bar open simulation |
| v1 | ema_12_26 | 10024.39 | 24.39 | buy /  / EMA12 > EMA26; 조건 충족; EMA12=175.145, EMA26=175.141 |
| v1 | macd_12_26_9 | 10024.39 | 24.39 | buy /  / MACD > 신호선 그리고 MACD > 0; 조건 충족; MACD=0.00418876, signal9=-0.17046 |
| v1 | rsi_14_recovery | 10000.00 | 0.00 | 대기 /  / 새 신호 대기 |
| v1 | bollinger_20_reentry | 9913.52 | -86.48 | sell /  / 직전 종가 < 직전 하단밴드, 현재 하단밴드 <= 종가 <= SMA20 (한 봉 목표); 조건 미충족; close=175.71, lower20=173.907, SMA20=174.743, previous_lower20=173.977 |
| v1 | donchian_20 | 9950.44 | -49.56 | sell /  / 종가 > 현재 봉을 제외한 직전 20봉 최고가; 조건 미충족; close=175.56, prior_high20=177.365 |
| v1 | atr_14_breakout | 9898.91 | -101.09 | sell /  / 종가 > 직전 종가 + 직전 ATR14 그리고 종가 > EMA26; 조건 미충족; close=176, threshold=176.983, prior_ATR14=0.731315, EMA26=175.281 |
| v1 | session_vwap | 9948.21 | -51.79 | sell /  / 종가 > 뉴욕 거래일별 누적 전형가격 VWAP; 조건 미충족; close=176, session_VWAP=176.01, session_volume=3.42523e+06 |
| v1 | obv_20 | 9970.37 | -29.63 | sell /  / OBV > OBV의 SMA20 그리고 종가 > EMA26; 조건 미충족; OBV=1.88162e+07, OBV_SMA20=2.13258e+07, close=175.84, EMA26=175.361 |
| v1 | stochastic_14_3_recovery | 10000.00 | 0.00 | 대기 /  / 새 신호 대기 |
| v1 | mfi_14_recovery | 10000.00 | 0.00 | 대기 /  / 새 신호 대기 |
| v1 | adx_14_trend | 10003.22 | 3.22 | buy /  / Wilder ADX14 >= 25 그리고 +DI14 > -DI14; 조건 충족; ADX14=25.0494, plus_DI14=28.5472, minus_DI14=15.0232 |
| v1 | aroon_25_trend | 10000.00 | 0.00 | 대기 /  / 새 신호 대기 |
| v1 | cci_20_momentum | 9888.78 | -111.22 | sell /  / CCI20 > 100 (전형가격·평균절대편차); 조건 미충족; CCI20=92.2568 |
| v1 | williams_14_recovery | 9913.52 | -86.48 | sell /  / 직전 Williams %R14 < -80, 현재 >= -80 (한 봉 목표); 조건 미충족; Williams_R14=-43.9575, previous_R14=-33.1215 |
| v1 | cmf_20_accumulation | 10000.00 | 0.00 | 대기 /  / 새 신호 대기 |
| v1 | chaikin_3_10 | 10000.00 | 0.00 | 대기 /  / 새 신호 대기 |
| v1 | roc_10_momentum | 10001.59 | 1.59 | buy /  / 10봉 ROC > 1% 그리고 종가 > EMA26; 조건 충족; ROC10_percent=1.09227, close=175.85, EMA26=175.323 |
| v1 | trix_15_trend | 10000.00 | 0.00 | 대기 /  / 새 신호 대기 |
| v1 | keltner_20_breakout | 10000.00 | 0.00 | 대기 /  / 새 신호 대기 |
| v1 | opening_range_30m | 10000.00 | 0.00 | 대기 /  / 새 신호 대기 |
| v2 | cash | 10000.00 | 0.00 | 대기 /  / 새 신호 대기 |
| v2 | buy_hold | 10284.81 | 284.81 | buy / partial / 직전 완료 봉 목표 비중 100%; 다음 봉 시가 가정 |
| v2 | trend_8_26 | 10122.75 | 122.75 | buy / partial / 직전 완료 봉 목표 비중 100%; 다음 봉 시가 가정 |
| v2 | momentum_26 | 10165.73 | 165.73 | buy / partial / 직전 완료 봉 목표 비중 100%; 다음 봉 시가 가정 |
| v2 | breakout_8 | 9301.50 | -698.50 | sell / filled / 직전 완료 봉 목표 비중 0%; 다음 봉 시가 가정 |
| v2 | reversion_12 | 9815.06 | -184.94 | sell / filled / 직전 완료 봉 목표 비중 0%; 다음 봉 시가 가정 |
| v2 | volume_26 | 9813.07 | -186.93 | buy / partial / 직전 완료 봉 목표 비중 100%; 다음 봉 시가 가정 |
| v2 | trend_8_26 AND momentum_26 | 10130.26 | 130.26 | buy / partial / 직전 완료 봉 목표 비중 100%; 다음 봉 시가 가정 |
| v2 | trend_8_26 + momentum_26 | 10144.23 | 144.23 | buy / partial / 직전 완료 봉 목표 비중 100%; 다음 봉 시가 가정 |
| v2 | trend_8_26 AND breakout_8 | 9402.89 | -597.11 | sell / filled / 직전 완료 봉 목표 비중 0%; 다음 봉 시가 가정 |
| v2 | trend_8_26 + breakout_8 | 9744.66 | -255.34 | buy / filled / 직전 완료 봉 목표 비중 50%; 다음 봉 시가 가정 |
| v2 | trend_8_26 AND reversion_12 | 9839.70 | -160.30 | sell / filled / 직전 완료 봉 목표 비중 0%; 다음 봉 시가 가정 |
| v2 | trend_8_26 + reversion_12 | 9967.79 | -32.21 | buy / filled / 직전 완료 봉 목표 비중 50%; 다음 봉 시가 가정 |
| v2 | trend_8_26 AND volume_26 | 9897.81 | -102.19 | buy / partial / 직전 완료 봉 목표 비중 100%; 다음 봉 시가 가정 |
| v2 | trend_8_26 + volume_26 | 9966.62 | -33.38 | buy / partial / 직전 완료 봉 목표 비중 100%; 다음 봉 시가 가정 |
| v2 | momentum_26 AND breakout_8 | 9349.69 | -650.31 | sell / filled / 직전 완료 봉 목표 비중 0%; 다음 봉 시가 가정 |
| v2 | momentum_26 + breakout_8 | 9724.58 | -275.42 | buy / filled / 직전 완료 봉 목표 비중 50%; 다음 봉 시가 가정 |
| v2 | momentum_26 AND reversion_12 | 9800.13 | -199.87 | sell / filled / 직전 완료 봉 목표 비중 0%; 다음 봉 시가 가정 |
| v2 | momentum_26 + reversion_12 | 9988.96 | -11.04 | buy / filled / 직전 완료 봉 목표 비중 50%; 다음 봉 시가 가정 |
| v2 | momentum_26 AND volume_26 | 9960.17 | -39.83 | buy / partial / 직전 완료 봉 목표 비중 100%; 다음 봉 시가 가정 |
| v2 | momentum_26 + volume_26 | 10008.74 | 8.74 | buy / partial / 직전 완료 봉 목표 비중 100%; 다음 봉 시가 가정 |
| v2 | breakout_8 AND reversion_12 | 10000.00 | 0.00 | 대기 /  / 새 신호 대기 |
| v2 | breakout_8 + reversion_12 | 9554.70 | -445.30 | sell / filled / 직전 완료 봉 목표 비중 0%; 다음 봉 시가 가정 |
| v2 | breakout_8 AND volume_26 | 9918.86 | -81.14 | sell / filled / 직전 완료 봉 목표 비중 0%; 다음 봉 시가 가정 |
| v2 | breakout_8 + volume_26 | 9573.81 | -426.19 | buy / filled / 직전 완료 봉 목표 비중 50%; 다음 봉 시가 가정 |
| v2 | reversion_12 AND volume_26 | 9949.87 | -50.13 | sell / filled / 직전 완료 봉 목표 비중 0%; 다음 봉 시가 가정 |
| v2 | reversion_12 + volume_26 | 9834.71 | -165.29 | buy / filled / 직전 완료 봉 목표 비중 50%; 다음 봉 시가 가정 |
| v2 | ema_12_26 | 10023.39 | 23.39 | buy / partial / EMA12 > EMA26; 조건 충족; EMA12=175.145, EMA26=175.141; 직전 완료 봉 목표를 다음 봉 시가에 모의 적용 |
| v2 | macd_12_26_9 | 10023.39 | 23.39 | buy / partial / MACD > 신호선 그리고 MACD > 0; 조건 충족; MACD=0.00418876, signal9=-0.17046; 직전 완료 봉 목표를 다음 봉 시가에 모의 적용 |
| v2 | rsi_14_recovery | 10000.00 | 0.00 | 대기 /  / 새 신호 대기 |
| v2 | bollinger_20_reentry | 9911.54 | -88.46 | sell / filled / 직전 종가 < 직전 하단밴드, 현재 하단밴드 <= 종가 <= SMA20 (한 봉 목표); 조건 미충족; close=175.71, lower20=173.907, SMA20=174.743, previous_lower20=173.977; 직전 완료 봉 목표를 다음 봉 시가에 모의 적용 |
| v2 | donchian_20 | 9948.45 | -51.55 | sell / filled / 종가 > 현재 봉을 제외한 직전 20봉 최고가; 조건 미충족; close=175.56, prior_high20=177.365; 직전 완료 봉 목표를 다음 봉 시가에 모의 적용 |
| v2 | atr_14_breakout | 9894.95 | -105.05 | sell / filled / 종가 > 직전 종가 + 직전 ATR14 그리고 종가 > EMA26; 조건 미충족; close=176, threshold=176.983, prior_ATR14=0.731315, EMA26=175.281; 직전 완료 봉 목표를 다음 봉 시가에 모의 적용 |
| v2 | session_vwap | 9946.22 | -53.78 | sell / filled / 종가 > 뉴욕 거래일별 누적 전형가격 VWAP; 조건 미충족; close=176, session_VWAP=176.01, session_volume=3.42523e+06; 직전 완료 봉 목표를 다음 봉 시가에 모의 적용 |
| v2 | obv_20 | 9968.37 | -31.63 | sell / filled / OBV > OBV의 SMA20 그리고 종가 > EMA26; 조건 미충족; OBV=1.88162e+07, OBV_SMA20=2.13258e+07, close=175.84, EMA26=175.361; 직전 완료 봉 목표를 다음 봉 시가에 모의 적용 |
| v2 | stochastic_14_3_recovery | 10000.00 | 0.00 | 대기 /  / 새 신호 대기 |
| v2 | mfi_14_recovery | 10000.00 | 0.00 | 대기 /  / 새 신호 대기 |
| v2 | adx_14_trend | 10002.22 | 2.22 | buy / partial / Wilder ADX14 >= 25 그리고 +DI14 > -DI14; 조건 충족; ADX14=25.0494, plus_DI14=28.5472, minus_DI14=15.0232; 직전 완료 봉 목표를 다음 봉 시가에 모의 적용 |
| v2 | aroon_25_trend | 10000.00 | 0.00 | 대기 /  / 새 신호 대기 |
| v2 | cci_20_momentum | 9884.83 | -115.17 | sell / filled / CCI20 > 100 (전형가격·평균절대편차); 조건 미충족; CCI20=92.2568; 직전 완료 봉 목표를 다음 봉 시가에 모의 적용 |
| v2 | williams_14_recovery | 9911.54 | -88.46 | sell / filled / 직전 Williams %R14 < -80, 현재 >= -80 (한 봉 목표); 조건 미충족; Williams_R14=-43.9575, previous_R14=-33.1215; 직전 완료 봉 목표를 다음 봉 시가에 모의 적용 |
| v2 | cmf_20_accumulation | 10000.00 | 0.00 | 대기 /  / 새 신호 대기 |
| v2 | chaikin_3_10 | 10000.00 | 0.00 | 대기 /  / 새 신호 대기 |
| v2 | roc_10_momentum | 10000.59 | 0.59 | buy / partial / 10봉 ROC > 1% 그리고 종가 > EMA26; 조건 충족; ROC10_percent=1.09227, close=175.85, EMA26=175.323; 직전 완료 봉 목표를 다음 봉 시가에 모의 적용 |
| v2 | trix_15_trend | 10000.00 | 0.00 | 대기 /  / 새 신호 대기 |
| v2 | keltner_20_breakout | 10000.00 | 0.00 | 대기 /  / 새 신호 대기 |
| v2 | opening_range_30m | 10000.00 | 0.00 | 대기 /  / 새 신호 대기 |

### 같은 기간의 비용·노출 비교 (사후 연구)

| 전략 | 비용 전 | 비용 후 | 100% 보유 | 같은 평균 노출 보유 | 평균 노출 |
|---|---:|---:|---:|---:|---:|
| cash | 0.00% | 0.00% | 9.39% | 0.00% | 0.00% |
| buy_hold | 9.85% | 9.39% | 9.39% | 9.39% | 100.00% |
| trend_8_26 | 1.48% | -3.11% | 9.39% | 5.97% | 64.47% |
| momentum_26 | 0.36% | -6.95% | 9.39% | 6.52% | 70.26% |
| breakout_8 | -3.43% | -21.06% | 9.39% | 2.13% | 23.42% |
| reversion_12 | 7.01% | -3.65% | 9.39% | 1.89% | 20.79% |
| volume_26 | 4.17% | -3.82% | 9.39% | 0.48% | 5.26% |
| trend_8_26 AND momentum_26 | 0.02% | -4.90% | 9.39% | 5.47% | 59.21% |
| trend_8_26 + momentum_26 | 0.93% | -4.84% | 9.39% | 6.24% | 67.37% |
| trend_8_26 AND breakout_8 | -1.31% | -15.16% | 9.39% | 1.65% | 18.16% |
| trend_8_26 + breakout_8 | -0.98% | -12.16% | 9.39% | 4.03% | 43.95% |
| trend_8_26 AND reversion_12 | 1.89% | -3.93% | 9.39% | 0.74% | 8.16% |
| trend_8_26 + reversion_12 | 4.24% | -3.17% | 9.39% | 3.91% | 42.64% |
| trend_8_26 AND volume_26 | 2.78% | -1.86% | 9.39% | 0.26% | 2.89% |
| trend_8_26 + volume_26 | 2.83% | -3.06% | 9.39% | 3.19% | 34.87% |
| momentum_26 AND breakout_8 | -3.50% | -19.44% | 9.39% | 1.91% | 21.05% |
| momentum_26 + breakout_8 | -1.53% | -14.28% | 9.39% | 4.31% | 46.85% |
| momentum_26 AND reversion_12 | 2.27% | -4.38% | 9.39% | 0.81% | 8.95% |
| momentum_26 + reversion_12 | 3.66% | -3.91% | 9.39% | 4.18% | 45.53% |
| momentum_26 AND volume_26 | 2.56% | -1.66% | 9.39% | 0.24% | 2.63% |
| momentum_26 + volume_26 | 2.27% | -3.99% | 9.39% | 3.46% | 37.77% |
| breakout_8 AND reversion_12 | 0.00% | 0.00% | 9.39% | 0.00% | 0.00% |
| breakout_8 + reversion_12 | 1.67% | -12.61% | 9.39% | 2.01% | 22.12% |
| breakout_8 AND volume_26 | 0.51% | -1.17% | 9.39% | 0.09% | 1.05% |
| breakout_8 + volume_26 | 0.31% | -11.76% | 9.39% | 1.30% | 14.35% |
| reversion_12 AND volume_26 | 1.52% | -1.00% | 9.39% | 0.14% | 1.58% |
| reversion_12 + volume_26 | 5.60% | -2.92% | 9.39% | 1.18% | 13.03% |
| ema_12_26 | -0.03% | -3.33% | 9.39% | 6.87% | 73.95% |
| macd_12_26_9 | -1.12% | -6.77% | 9.39% | 3.64% | 39.74% |
| rsi_14_recovery | -0.15% | -0.57% | 9.39% | 0.02% | 0.26% |
| bollinger_20_reentry | -0.87% | -3.75% | 9.39% | 0.17% | 1.84% |
| donchian_20 | -1.09% | -9.82% | 9.39% | 0.81% | 8.95% |
| atr_14_breakout | -1.33% | -10.41% | 9.39% | 0.57% | 6.32% |
| session_vwap | -0.96% | -12.69% | 9.39% | 5.99% | 64.74% |
| obv_20 | 2.12% | -5.32% | 9.39% | 3.91% | 42.63% |
| stochastic_14_3_recovery | 1.55% | -6.63% | 9.39% | 0.48% | 5.26% |
| mfi_14_recovery | -0.31% | -1.97% | 9.39% | 0.09% | 1.05% |
| adx_14_trend | 1.07% | -1.86% | 9.39% | 3.84% | 41.84% |
| aroon_25_trend | -1.78% | -7.78% | 9.39% | 2.79% | 30.53% |
| cci_20_momentum | 2.73% | -4.75% | 9.39% | 2.42% | 26.58% |
| williams_14_recovery | 0.08% | -5.24% | 9.39% | 0.31% | 3.42% |
| cmf_20_accumulation | 2.09% | -6.53% | 9.39% | 4.72% | 51.32% |
| chaikin_3_10 | -1.00% | -9.36% | 9.39% | 5.10% | 55.26% |
| roc_10_momentum | 0.02% | -5.69% | 9.39% | 1.26% | 13.95% |
| trix_15_trend | -2.63% | -9.34% | 9.39% | 5.69% | 61.58% |
| keltner_20_breakout | -0.86% | -7.30% | 9.39% | 1.36% | 15.00% |
| opening_range_30m | -0.36% | -9.53% | 9.39% | 3.27% | 35.79% |

동일 구간·초기 자금, 종료 시 청산 비용 포함. 노출 맞춤은 사후 설명용이며 v2 실제 계좌 성과가 아닙니다.
[낙폭 분해·비용 영향·전체 구간](XOM/comparison.json)

[v1 전체 기록](XOM/accounts.json) · [v2 전체 기록](XOM/accounts-v2.json)

## JNJ 계좌

| 모델 | 전략 | 평가액 USD | 손익 USD | 최근 매매·이유 |
|---|---|---:|---:|---|
| v1 | cash | 10000.00 | 0.00 | 대기 /  / 새 신호 대기 |
| v1 | buy_hold | 10010.49 | 10.49 | buy /  / buy_hold: prior completed bar target 100%; next bar open simulation |
| v1 | trend_8_26 | 9964.48 | -35.52 | buy /  / trend_8_26: prior completed bar target 100%; next bar open simulation |
| v1 | momentum_26 | 10000.00 | 0.00 | 대기 /  / 새 신호 대기 |
| v1 | breakout_8 | 9842.15 | -157.85 | buy /  / breakout_8: prior completed bar target 100%; next bar open simulation |
| v1 | reversion_12 | 10000.00 | 0.00 | 대기 /  / 새 신호 대기 |
| v1 | volume_26 | 9935.63 | -64.37 | sell /  / volume_26: prior completed bar target 0%; next bar open simulation |
| v1 | trend_8_26 AND momentum_26 | 10000.00 | 0.00 | 대기 /  / 새 신호 대기 |
| v1 | trend_8_26 + momentum_26 | 9982.20 | -17.80 | sell /  / trend_8_26 + momentum_26: prior completed bar target 50%; next bar open simulation |
| v1 | trend_8_26 AND breakout_8 | 9957.69 | -42.31 | buy /  / trend_8_26 AND breakout_8: prior completed bar target 100%; next bar open simulation |
| v1 | trend_8_26 + breakout_8 | 9903.11 | -96.89 | buy /  / trend_8_26 + breakout_8: prior completed bar target 100%; next bar open simulation |
| v1 | trend_8_26 AND reversion_12 | 10000.00 | 0.00 | 대기 /  / 새 신호 대기 |
| v1 | trend_8_26 + reversion_12 | 9982.20 | -17.80 | sell /  / trend_8_26 + reversion_12: prior completed bar target 50%; next bar open simulation |
| v1 | trend_8_26 AND volume_26 | 9935.63 | -64.37 | sell /  / trend_8_26 AND volume_26: prior completed bar target 0%; next bar open simulation |
| v1 | trend_8_26 + volume_26 | 9950.05 | -49.95 | sell /  / trend_8_26 + volume_26: prior completed bar target 50%; next bar open simulation |
| v1 | momentum_26 AND breakout_8 | 10000.00 | 0.00 | 대기 /  / 새 신호 대기 |
| v1 | momentum_26 + breakout_8 | 9920.72 | -79.28 | buy /  / momentum_26 + breakout_8: prior completed bar target 50%; next bar open simulation |
| v1 | momentum_26 AND reversion_12 | 10000.00 | 0.00 | 대기 /  / 새 신호 대기 |
| v1 | momentum_26 + reversion_12 | 10000.00 | 0.00 | 대기 /  / 새 신호 대기 |
| v1 | momentum_26 AND volume_26 | 10000.00 | 0.00 | 대기 /  / 새 신호 대기 |
| v1 | momentum_26 + volume_26 | 9967.75 | -32.25 | sell /  / momentum_26 + volume_26: prior completed bar target 0%; next bar open simulation |
| v1 | breakout_8 AND reversion_12 | 10000.00 | 0.00 | 대기 /  / 새 신호 대기 |
| v1 | breakout_8 + reversion_12 | 9920.72 | -79.28 | buy /  / breakout_8 + reversion_12: prior completed bar target 50%; next bar open simulation |
| v1 | breakout_8 AND volume_26 | 10000.00 | 0.00 | 대기 /  / 새 신호 대기 |
| v1 | breakout_8 + volume_26 | 9888.72 | -111.28 | buy /  / breakout_8 + volume_26: prior completed bar target 50%; next bar open simulation |
| v1 | reversion_12 AND volume_26 | 10000.00 | 0.00 | 대기 /  / 새 신호 대기 |
| v1 | reversion_12 + volume_26 | 9967.75 | -32.25 | sell /  / reversion_12 + volume_26: prior completed bar target 0%; next bar open simulation |
| v1 | ema_12_26 | 9963.90 | -36.10 | buy /  / EMA12 > EMA26; 조건 충족; EMA12=255.218, EMA26=255.146 |
| v1 | macd_12_26_9 | 9963.90 | -36.10 | buy /  / MACD > 신호선 그리고 MACD > 0; 조건 충족; MACD=0.0719144, signal9=-0.171173 |
| v1 | rsi_14_recovery | 10000.00 | 0.00 | 대기 /  / 새 신호 대기 |
| v1 | bollinger_20_reentry | 10000.00 | 0.00 | 대기 /  / 새 신호 대기 |
| v1 | donchian_20 | 10000.00 | 0.00 | 대기 /  / 새 신호 대기 |
| v1 | atr_14_breakout | 9883.97 | -116.03 | sell /  / 종가 > 직전 종가 + 직전 ATR14 그리고 종가 > EMA26; 조건 미충족; close=256.72, threshold=258.136, prior_ATR14=1.3158, EMA26=255.146 |
| v1 | session_vwap | 9813.21 | -186.79 | buy /  / 종가 > 뉴욕 거래일별 누적 전형가격 VWAP; 조건 충족; close=256.88, session_VWAP=256.481, session_volume=3.84566e+06 |
| v1 | obv_20 | 9968.75 | -31.25 | buy /  / OBV > OBV의 SMA20 그리고 종가 > EMA26; 조건 충족; OBV=6.12774e+06, OBV_SMA20=4.45241e+06, close=256.69, EMA26=255.435 |
| v1 | stochastic_14_3_recovery | 9927.65 | -72.35 | sell /  / 직전 %K14 < 20에서 %K14가 %D3 상향 돌파 (한 봉 목표); 조건 미충족; K14=60.1505, D3=50.3645, previous_K14=74.7605, previous_D3=37.7141 |
| v1 | mfi_14_recovery | 10000.00 | 0.00 | 대기 /  / 새 신호 대기 |
| v1 | adx_14_trend | 9823.79 | -176.21 | sell /  / Wilder ADX14 >= 25 그리고 +DI14 > -DI14; 조건 미충족; ADX14=24.7842, plus_DI14=27.3963, minus_DI14=19.1477 |
| v1 | aroon_25_trend | 10000.00 | 0.00 | 대기 /  / 새 신호 대기 |
| v1 | cci_20_momentum | 9935.63 | -64.37 | sell /  / CCI20 > 100 (전형가격·평균절대편차); 조건 미충족; CCI20=62.9489 |
| v1 | williams_14_recovery | 9927.65 | -72.35 | sell /  / 직전 Williams %R14 < -80, 현재 >= -80 (한 봉 목표); 조건 미충족; Williams_R14=-39.8495, previous_R14=-25.2395 |
| v1 | cmf_20_accumulation | 10000.00 | 0.00 | 대기 /  / 새 신호 대기 |
| v1 | chaikin_3_10 | 10000.00 | 0.00 | 대기 /  / 새 신호 대기 |
| v1 | roc_10_momentum | 9884.73 | -115.27 | buy /  / 10봉 ROC > 1% 그리고 종가 > EMA26; 조건 충족; ROC10_percent=1.25744, close=256.88, EMA26=255.578 |
| v1 | trix_15_trend | 9957.69 | -42.31 | buy /  / 15봉 삼중 EMA의 1봉 변화율 TRIX > 0 그리고 종가 > EMA26; 조건 충족; TRIX15_percent=0.00301911, close=256.88, EMA26=255.578 |
| v1 | keltner_20_breakout | 10000.00 | 0.00 | 대기 /  / 새 신호 대기 |
| v1 | opening_range_30m | 10000.00 | 0.00 | 대기 /  / 새 신호 대기 |
| v2 | cash | 10000.00 | 0.00 | 대기 /  / 새 신호 대기 |
| v2 | buy_hold | 9776.86 | -223.14 | 중단: 손실 한도 / buy / partial / 직전 완료 봉 목표 비중 100%; 다음 봉 시가 가정 |
| v2 | trend_8_26 | 9776.86 | -223.14 | 중단: 손실 한도 / buy / partial / 직전 완료 봉 목표 비중 100%; 다음 봉 시가 가정 |
| v2 | momentum_26 | 9776.86 | -223.14 | 중단: 손실 한도 / buy / partial / 직전 완료 봉 목표 비중 100%; 다음 봉 시가 가정 |
| v2 | breakout_8 | 9343.39 | -656.61 | 중단: 손실 한도 / sell / filled / 직전 완료 봉 목표 비중 0%; 다음 봉 시가 가정 |
| v2 | reversion_12 | 9690.14 | -309.86 | sell / filled / 직전 완료 봉 목표 비중 0%; 다음 봉 시가 가정 |
| v2 | volume_26 | 9726.38 | -273.62 | sell / filled / 직전 완료 봉 목표 비중 0%; 다음 봉 시가 가정 |
| v2 | trend_8_26 AND momentum_26 | 9776.86 | -223.14 | 중단: 손실 한도 / buy / partial / 직전 완료 봉 목표 비중 100%; 다음 봉 시가 가정 |
| v2 | trend_8_26 + momentum_26 | 9776.86 | -223.14 | 중단: 손실 한도 / buy / partial / 직전 완료 봉 목표 비중 100%; 다음 봉 시가 가정 |
| v2 | trend_8_26 AND breakout_8 | 9419.39 | -580.61 | 중단: 손실 한도 / sell / filled / 직전 완료 봉 목표 비중 0%; 다음 봉 시가 가정 |
| v2 | trend_8_26 + breakout_8 | 9474.25 | -525.75 | buy / partial / 직전 완료 봉 목표 비중 100%; 다음 봉 시가 가정 |
| v2 | trend_8_26 AND reversion_12 | 9978.08 | -21.92 | sell / filled / 직전 완료 봉 목표 비중 0%; 다음 봉 시가 가정 |
| v2 | trend_8_26 + reversion_12 | 9732.92 | -267.08 | 중단: 손실 한도 / sell / filled / 직전 완료 봉 목표 비중 0%; 다음 봉 시가 가정 |
| v2 | trend_8_26 AND volume_26 | 9805.21 | -194.79 | sell / filled / 직전 완료 봉 목표 비중 0%; 다음 봉 시가 가정 |
| v2 | trend_8_26 + volume_26 | 9862.12 | -137.88 | 중단: 손실 한도 / buy / filled / 직전 완료 봉 목표 비중 50%; 다음 봉 시가 가정 |
| v2 | momentum_26 AND breakout_8 | 9598.70 | -401.30 | sell / filled / 직전 완료 봉 목표 비중 0%; 다음 봉 시가 가정 |
| v2 | momentum_26 + breakout_8 | 9482.65 | -517.35 | buy / filled / 직전 완료 봉 목표 비중 50%; 다음 봉 시가 가정 |
| v2 | momentum_26 AND reversion_12 | 9938.87 | -61.13 | sell / filled / 직전 완료 봉 목표 비중 0%; 다음 봉 시가 가정 |
| v2 | momentum_26 + reversion_12 | 9732.92 | -267.08 | 중단: 손실 한도 / sell / filled / 직전 완료 봉 목표 비중 0%; 다음 봉 시가 가정 |
| v2 | momentum_26 AND volume_26 | 9920.93 | -79.07 | sell / filled / 직전 완료 봉 목표 비중 0%; 다음 봉 시가 가정 |
| v2 | momentum_26 + volume_26 | 9862.12 | -137.88 | 중단: 손실 한도 / buy / filled / 직전 완료 봉 목표 비중 50%; 다음 봉 시가 가정 |
| v2 | breakout_8 AND reversion_12 | 10000.00 | 0.00 | 대기 /  / 새 신호 대기 |
| v2 | breakout_8 + reversion_12 | 9502.73 | -497.27 | buy / filled / 직전 완료 봉 목표 비중 50%; 다음 봉 시가 가정 |
| v2 | breakout_8 AND volume_26 | 9814.17 | -185.83 | sell / filled / 직전 완료 봉 목표 비중 0%; 다음 봉 시가 가정 |
| v2 | breakout_8 + volume_26 | 9500.41 | -499.59 | buy / filled / 직전 완료 봉 목표 비중 50%; 다음 봉 시가 가정 |
| v2 | reversion_12 AND volume_26 | 9886.24 | -113.76 | sell / filled / 직전 완료 봉 목표 비중 0%; 다음 봉 시가 가정 |
| v2 | reversion_12 + volume_26 | 9728.89 | -271.11 | sell / filled / 직전 완료 봉 목표 비중 0%; 다음 봉 시가 가정 |
| v2 | ema_12_26 | 9962.90 | -37.10 | buy / partial / EMA12 > EMA26; 조건 충족; EMA12=255.218, EMA26=255.146; 직전 완료 봉 목표를 다음 봉 시가에 모의 적용 |
| v2 | macd_12_26_9 | 9962.90 | -37.10 | buy / partial / MACD > 신호선 그리고 MACD > 0; 조건 충족; MACD=0.0719144, signal9=-0.171173; 직전 완료 봉 목표를 다음 봉 시가에 모의 적용 |
| v2 | rsi_14_recovery | 10000.00 | 0.00 | 대기 /  / 새 신호 대기 |
| v2 | bollinger_20_reentry | 10000.00 | 0.00 | 대기 /  / 새 신호 대기 |
| v2 | donchian_20 | 10000.00 | 0.00 | 대기 /  / 새 신호 대기 |
| v2 | atr_14_breakout | 9880.02 | -119.98 | sell / filled / 종가 > 직전 종가 + 직전 ATR14 그리고 종가 > EMA26; 조건 미충족; close=256.72, threshold=258.136, prior_ATR14=1.3158, EMA26=255.146; 직전 완료 봉 목표를 다음 봉 시가에 모의 적용 |
| v2 | session_vwap | 9808.30 | -191.70 | buy / partial / 종가 > 뉴욕 거래일별 누적 전형가격 VWAP; 조건 충족; close=256.88, session_VWAP=256.481, session_volume=3.84566e+06; 직전 완료 봉 목표를 다음 봉 시가에 모의 적용 |
| v2 | obv_20 | 9967.75 | -32.25 | buy / partial / OBV > OBV의 SMA20 그리고 종가 > EMA26; 조건 충족; OBV=6.12774e+06, OBV_SMA20=4.45241e+06, close=256.69, EMA26=255.435; 직전 완료 봉 목표를 다음 봉 시가에 모의 적용 |
| v2 | stochastic_14_3_recovery | 9925.66 | -74.34 | sell / filled / 직전 %K14 < 20에서 %K14가 %D3 상향 돌파 (한 봉 목표); 조건 미충족; K14=60.1505, D3=50.3645, previous_K14=74.7605, previous_D3=37.7141; 직전 완료 봉 목표를 다음 봉 시가에 모의 적용 |
| v2 | mfi_14_recovery | 10000.00 | 0.00 | 대기 /  / 새 신호 대기 |
| v2 | adx_14_trend | 9817.90 | -182.10 | sell / filled / Wilder ADX14 >= 25 그리고 +DI14 > -DI14; 조건 미충족; ADX14=24.7842, plus_DI14=27.3963, minus_DI14=19.1477; 직전 완료 봉 목표를 다음 봉 시가에 모의 적용 |
| v2 | aroon_25_trend | 10000.00 | 0.00 | 대기 /  / 새 신호 대기 |
| v2 | cci_20_momentum | 9933.64 | -66.36 | sell / filled / CCI20 > 100 (전형가격·평균절대편차); 조건 미충족; CCI20=62.9489; 직전 완료 봉 목표를 다음 봉 시가에 모의 적용 |
| v2 | williams_14_recovery | 9925.66 | -74.34 | sell / filled / 직전 Williams %R14 < -80, 현재 >= -80 (한 봉 목표); 조건 미충족; Williams_R14=-39.8495, previous_R14=-25.2395; 직전 완료 봉 목표를 다음 봉 시가에 모의 적용 |
| v2 | cmf_20_accumulation | 10000.00 | 0.00 | 대기 /  / 새 신호 대기 |
| v2 | chaikin_3_10 | 10000.00 | 0.00 | 대기 /  / 새 신호 대기 |
| v2 | roc_10_momentum | 9881.76 | -118.24 | buy / partial / 10봉 ROC > 1% 그리고 종가 > EMA26; 조건 충족; ROC10_percent=1.25744, close=256.88, EMA26=255.578; 직전 완료 봉 목표를 다음 봉 시가에 모의 적용 |
| v2 | trix_15_trend | 9956.70 | -43.30 | buy / partial / 15봉 삼중 EMA의 1봉 변화율 TRIX > 0 그리고 종가 > EMA26; 조건 충족; TRIX15_percent=0.00301911, close=256.88, EMA26=255.578; 직전 완료 봉 목표를 다음 봉 시가에 모의 적용 |
| v2 | keltner_20_breakout | 10000.00 | 0.00 | 대기 /  / 새 신호 대기 |
| v2 | opening_range_30m | 10000.00 | 0.00 | 대기 /  / 새 신호 대기 |

### 같은 기간의 비용·노출 비교 (사후 연구)

| 전략 | 비용 전 | 비용 후 | 100% 보유 | 같은 평균 노출 보유 | 평균 노출 |
|---|---:|---:|---:|---:|---:|
| cash | 0.00% | 0.00% | -5.78% | -0.00% | 0.00% |
| buy_hold | -5.38% | -5.78% | -5.78% | -5.78% | 100.00% |
| trend_8_26 | 2.34% | -0.21% | -5.78% | -2.88% | 48.68% |
| momentum_26 | 0.96% | -2.38% | -5.78% | -2.82% | 47.63% |
| breakout_8 | -1.00% | -18.39% | -5.78% | -1.29% | 21.58% |
| reversion_12 | -7.78% | -15.92% | -5.78% | -1.77% | 29.74% |
| volume_26 | -0.90% | -7.73% | -5.78% | -0.41% | 6.84% |
| trend_8_26 AND momentum_26 | 2.35% | -0.62% | -5.78% | -2.59% | 43.68% |
| trend_8_26 + momentum_26 | 1.65% | -1.30% | -5.78% | -2.85% | 48.16% |
| trend_8_26 AND breakout_8 | 0.56% | -12.09% | -5.78% | -0.93% | 15.53% |
| trend_8_26 + breakout_8 | 0.68% | -9.55% | -5.78% | -2.09% | 35.14% |
| trend_8_26 AND reversion_12 | 0.69% | -2.63% | -5.78% | -0.33% | 5.53% |
| trend_8_26 + reversion_12 | -2.82% | -8.01% | -5.78% | -2.33% | 39.21% |
| trend_8_26 AND volume_26 | 1.34% | -1.19% | -5.78% | -0.11% | 1.84% |
| trend_8_26 + volume_26 | 0.74% | -3.62% | -5.78% | -1.66% | 27.77% |
| momentum_26 AND breakout_8 | 2.20% | -9.52% | -5.78% | -0.87% | 14.47% |
| momentum_26 + breakout_8 | 0.00% | -10.54% | -5.78% | -2.06% | 34.61% |
| momentum_26 AND reversion_12 | -0.60% | -3.89% | -5.78% | -0.41% | 6.84% |
| momentum_26 + reversion_12 | -3.48% | -8.82% | -5.78% | -2.30% | 38.69% |
| momentum_26 AND volume_26 | 1.57% | -0.12% | -5.78% | -0.08% | 1.32% |
| momentum_26 + volume_26 | 0.06% | -4.48% | -5.78% | -1.63% | 27.24% |
| breakout_8 AND reversion_12 | 0.00% | 0.00% | -5.78% | -0.00% | 0.00% |
| breakout_8 + reversion_12 | -4.43% | -16.65% | -5.78% | -1.53% | 25.67% |
| breakout_8 AND volume_26 | -0.11% | -2.19% | -5.78% | -0.10% | 1.58% |
| breakout_8 + volume_26 | -0.94% | -12.49% | -5.78% | -0.85% | 14.22% |
| reversion_12 AND volume_26 | -1.99% | -4.42% | -5.78% | -0.16% | 2.63% |
| reversion_12 + volume_26 | -4.39% | -11.18% | -5.78% | -1.10% | 18.29% |
| ema_12_26 | -0.15% | -2.22% | -5.78% | -2.64% | 44.47% |
| macd_12_26_9 | 6.20% | 3.56% | -5.78% | -1.74% | 29.21% |
| rsi_14_recovery | -1.69% | -6.92% | -5.78% | -0.21% | 3.42% |
| bollinger_20_reentry | -0.55% | -4.64% | -5.78% | -0.16% | 2.63% |
| donchian_20 | 1.17% | -6.59% | -5.78% | -0.44% | 7.37% |
| atr_14_breakout | 1.31% | -4.88% | -5.78% | -0.29% | 4.74% |
| session_vwap | 1.37% | -6.40% | -5.78% | -2.94% | 49.74% |
| obv_20 | -5.64% | -13.61% | -5.78% | -2.07% | 34.74% |
| stochastic_14_3_recovery | -1.40% | -13.80% | -5.78% | -0.51% | 8.42% |
| mfi_14_recovery | 0.33% | -0.93% | -5.78% | -0.05% | 0.79% |
| adx_14_trend | -2.56% | -7.35% | -5.78% | -1.87% | 31.32% |
| aroon_25_trend | 3.86% | -0.41% | -5.78% | -1.68% | 28.16% |
| cci_20_momentum | 0.85% | -6.49% | -5.78% | -1.48% | 24.74% |
| williams_14_recovery | -2.03% | -10.30% | -5.78% | -0.33% | 5.53% |
| cmf_20_accumulation | 2.16% | -2.04% | -5.78% | -1.82% | 30.53% |
| chaikin_3_10 | -3.52% | -7.87% | -5.78% | -2.14% | 36.05% |
| roc_10_momentum | -1.73% | -8.11% | -5.78% | -0.89% | 14.74% |
| trix_15_trend | -1.12% | -3.98% | -5.78% | -2.01% | 33.68% |
| keltner_20_breakout | 0.76% | -2.97% | -5.78% | -0.57% | 9.47% |
| opening_range_30m | 0.41% | -3.72% | -5.78% | -1.57% | 26.32% |

동일 구간·초기 자금, 종료 시 청산 비용 포함. 노출 맞춤은 사후 설명용이며 v2 실제 계좌 성과가 아닙니다.
[낙폭 분해·비용 영향·전체 구간](JNJ/comparison.json)

[v1 전체 기록](JNJ/accounts.json) · [v2 전체 기록](JNJ/accounts-v2.json)

## CAT 계좌

| 모델 | 전략 | 평가액 USD | 손익 USD | 최근 매매·이유 |
|---|---|---:|---:|---|
| v1 | cash | 10000.00 | 0.00 | 대기 /  / 새 신호 대기 |
| v1 | buy_hold | 10037.45 | 37.45 | buy /  / buy_hold: prior completed bar target 100%; next bar open simulation |
| v1 | trend_8_26 | 10037.45 | 37.45 | buy /  / trend_8_26: prior completed bar target 100%; next bar open simulation |
| v1 | momentum_26 | 9956.84 | -43.16 | buy /  / momentum_26: prior completed bar target 100%; next bar open simulation |
| v1 | breakout_8 | 9950.83 | -49.17 | sell /  / breakout_8: prior completed bar target 0%; next bar open simulation |
| v1 | reversion_12 | 9997.26 | -2.74 | sell /  / reversion_12: prior completed bar target 0%; next bar open simulation |
| v1 | volume_26 | 10000.00 | 0.00 | 대기 /  / 새 신호 대기 |
| v1 | trend_8_26 AND momentum_26 | 9956.84 | -43.16 | buy /  / trend_8_26 AND momentum_26: prior completed bar target 100%; next bar open simulation |
| v1 | trend_8_26 + momentum_26 | 9997.23 | -2.77 | buy /  / trend_8_26 + momentum_26: prior completed bar target 100%; next bar open simulation |
| v1 | trend_8_26 AND breakout_8 | 9950.83 | -49.17 | sell /  / trend_8_26 AND breakout_8: prior completed bar target 0%; next bar open simulation |
| v1 | trend_8_26 + breakout_8 | 9994.21 | -5.79 | sell /  / trend_8_26 + breakout_8: prior completed bar target 50%; next bar open simulation |
| v1 | trend_8_26 AND reversion_12 | 9997.26 | -2.74 | sell /  / trend_8_26 AND reversion_12: prior completed bar target 0%; next bar open simulation |
| v1 | trend_8_26 + reversion_12 | 10017.42 | 17.42 | sell /  / trend_8_26 + reversion_12: prior completed bar target 50%; next bar open simulation |
| v1 | trend_8_26 AND volume_26 | 10000.00 | 0.00 | 대기 /  / 새 신호 대기 |
| v1 | trend_8_26 + volume_26 | 10018.76 | 18.76 | sell /  / trend_8_26 + volume_26: prior completed bar target 50%; next bar open simulation |
| v1 | momentum_26 AND breakout_8 | 9950.83 | -49.17 | sell /  / momentum_26 AND breakout_8: prior completed bar target 0%; next bar open simulation |
| v1 | momentum_26 + breakout_8 | 9953.84 | -46.16 | sell /  / momentum_26 + breakout_8: prior completed bar target 50%; next bar open simulation |
| v1 | momentum_26 AND reversion_12 | 9997.26 | -2.74 | sell /  / momentum_26 AND reversion_12: prior completed bar target 0%; next bar open simulation |
| v1 | momentum_26 + reversion_12 | 9977.04 | -22.96 | sell /  / momentum_26 + reversion_12: prior completed bar target 50%; next bar open simulation |
| v1 | momentum_26 AND volume_26 | 10000.00 | 0.00 | 대기 /  / 새 신호 대기 |
| v1 | momentum_26 + volume_26 | 9978.38 | -21.62 | sell /  / momentum_26 + volume_26: prior completed bar target 50%; next bar open simulation |
| v1 | breakout_8 AND reversion_12 | 10000.00 | 0.00 | 대기 /  / 새 신호 대기 |
| v1 | breakout_8 + reversion_12 | 9974.00 | -26.00 | sell /  / breakout_8 + reversion_12: prior completed bar target 0%; next bar open simulation |
| v1 | breakout_8 AND volume_26 | 10000.00 | 0.00 | 대기 /  / 새 신호 대기 |
| v1 | breakout_8 + volume_26 | 9975.37 | -24.63 | sell /  / breakout_8 + volume_26: prior completed bar target 0%; next bar open simulation |
| v1 | reversion_12 AND volume_26 | 10000.00 | 0.00 | 대기 /  / 새 신호 대기 |
| v1 | reversion_12 + volume_26 | 9998.63 | -1.37 | sell /  / reversion_12 + volume_26: prior completed bar target 0%; next bar open simulation |
| v1 | ema_12_26 | 9956.84 | -43.16 | buy /  / EMA12 > EMA26; 조건 충족; EMA12=733.716, EMA26=733.7 |
| v1 | macd_12_26_9 | 9956.84 | -43.16 | buy /  / MACD > 신호선 그리고 MACD > 0; 조건 충족; MACD=0.0155601, signal9=-2.12997 |
| v1 | rsi_14_recovery | 10000.00 | 0.00 | 대기 /  / 새 신호 대기 |
| v1 | bollinger_20_reentry | 10000.00 | 0.00 | 대기 /  / 새 신호 대기 |
| v1 | donchian_20 | 9950.83 | -49.17 | sell /  / 종가 > 현재 봉을 제외한 직전 20봉 최고가; 조건 미충족; close=739.81, prior_high20=742.28 |
| v1 | atr_14_breakout | 9950.83 | -49.17 | sell /  / 종가 > 직전 종가 + 직전 ATR14 그리고 종가 > EMA26; 조건 미충족; close=739.81, threshold=744.805, prior_ATR14=4.59507, EMA26=734.153 |
| v1 | session_vwap | 9963.13 | -36.87 | sell /  / 종가 > 뉴욕 거래일별 누적 전형가격 VWAP; 조건 미충족; close=734.53, session_VWAP=738.361, session_volume=651546 |
| v1 | obv_20 | 9946.59 | -53.41 | buy /  / OBV > OBV의 SMA20 그리고 종가 > EMA26; 조건 충족; OBV=-4.34663e+06, OBV_SMA20=-4.46778e+06, close=737.51, EMA26=735.635 |
| v1 | stochastic_14_3_recovery | 10000.00 | 0.00 | 대기 /  / 새 신호 대기 |
| v1 | mfi_14_recovery | 10000.00 | 0.00 | 대기 /  / 새 신호 대기 |
| v1 | adx_14_trend | 10000.00 | 0.00 | 대기 /  / 새 신호 대기 |
| v1 | aroon_25_trend | 10031.15 | 31.15 | sell /  / Aroon25 Up > 70 그리고 Down < 30 (동률이면 최신 극값); 조건 미충족; Aroon_up=88, Aroon_down=48 |
| v1 | cci_20_momentum | 10024.78 | 24.78 | sell /  / CCI20 > 100 (전형가격·평균절대편차); 조건 미충족; CCI20=98.8062 |
| v1 | williams_14_recovery | 10000.00 | 0.00 | 대기 /  / 새 신호 대기 |
| v1 | cmf_20_accumulation | 9966.09 | -33.91 | buy /  / Chaikin Money Flow20 > 0.1; 조건 충족; CMF20=0.173065, volume20=2.14066e+06 |
| v1 | chaikin_3_10 | 9866.71 | -133.29 | buy /  / ADL의 EMA3 - EMA10 > 0 그리고 종가 > EMA26; 조건 충족; Chaikin3_10=108.363, ADL=-5.61683e+06, close=737.51, EMA26=735.635 |
| v1 | roc_10_momentum | 9963.13 | -36.87 | sell /  / 10봉 ROC > 1% 그리고 종가 > EMA26; 조건 미충족; ROC10_percent=-0.134597, close=734.53, EMA26=735.486 |
| v1 | trix_15_trend | 9876.12 | -123.88 | buy /  / 15봉 삼중 EMA의 1봉 변화율 TRIX > 0 그리고 종가 > EMA26; 조건 충족; TRIX15_percent=0.0151548, close=737.51, EMA26=735.635 |
| v1 | keltner_20_breakout | 10000.00 | 0.00 | 대기 /  / 새 신호 대기 |
| v1 | opening_range_30m | 10040.71 | 40.71 | sell /  / 뉴욕 09:30·09:45 두 완료 봉 최고가를 10:00 이후 종가가 돌파; 자료 부족·변동폭 또는 거래량 없음: 대기; close=740.21 |
| v2 | cash | 10000.00 | 0.00 | 대기 /  / 새 신호 대기 |
| v2 | buy_hold | 9231.19 | -768.81 | 중단: 손실 한도 / buy / partial / 직전 완료 봉 목표 비중 100%; 다음 봉 시가 가정 |
| v2 | trend_8_26 | 9960.89 | -39.11 | buy / partial / 직전 완료 봉 목표 비중 100%; 다음 봉 시가 가정 |
| v2 | momentum_26 | 9970.37 | -29.63 | buy / partial / 직전 완료 봉 목표 비중 100%; 다음 봉 시가 가정 |
| v2 | breakout_8 | 9772.76 | -227.24 | sell / filled / 직전 완료 봉 목표 비중 0%; 다음 봉 시가 가정 |
| v2 | reversion_12 | 9102.27 | -897.73 | 중단: 손실 한도 / buy / partial / 직전 완료 봉 목표 비중 100%; 다음 봉 시가 가정 |
| v2 | volume_26 | 9362.59 | -637.41 | 중단: 손실 한도 / buy / partial / 직전 완료 봉 목표 비중 100%; 다음 봉 시가 가정 |
| v2 | trend_8_26 AND momentum_26 | 9999.24 | -0.76 | buy / partial / 직전 완료 봉 목표 비중 100%; 다음 봉 시가 가정 |
| v2 | trend_8_26 + momentum_26 | 9965.80 | -34.20 | buy / partial / 직전 완료 봉 목표 비중 100%; 다음 봉 시가 가정 |
| v2 | trend_8_26 AND breakout_8 | 9866.70 | -133.30 | sell / filled / 직전 완료 봉 목표 비중 0%; 다음 봉 시가 가정 |
| v2 | trend_8_26 + breakout_8 | 9866.82 | -133.18 | sell / filled / 직전 완료 봉 목표 비중 50%; 다음 봉 시가 가정 |
| v2 | trend_8_26 AND reversion_12 | 9810.43 | -189.57 | sell / filled / 직전 완료 봉 목표 비중 0%; 다음 봉 시가 가정 |
| v2 | trend_8_26 + reversion_12 | 9640.52 | -359.48 | sell / filled / 직전 완료 봉 목표 비중 50%; 다음 봉 시가 가정 |
| v2 | trend_8_26 AND volume_26 | 10035.44 | 35.44 | sell / filled / 직전 완료 봉 목표 비중 0%; 다음 봉 시가 가정 |
| v2 | trend_8_26 + volume_26 | 9650.63 | -349.37 | sell / filled / 직전 완료 봉 목표 비중 50%; 다음 봉 시가 가정 |
| v2 | momentum_26 AND breakout_8 | 9926.39 | -73.61 | sell / filled / 직전 완료 봉 목표 비중 0%; 다음 봉 시가 가정 |
| v2 | momentum_26 + breakout_8 | 9871.27 | -128.73 | sell / filled / 직전 완료 봉 목표 비중 50%; 다음 봉 시가 가정 |
| v2 | momentum_26 AND reversion_12 | 9870.05 | -129.95 | sell / filled / 직전 완료 봉 목표 비중 0%; 다음 봉 시가 가정 |
| v2 | momentum_26 + reversion_12 | 9645.02 | -354.98 | sell / filled / 직전 완료 봉 목표 비중 50%; 다음 봉 시가 가정 |
| v2 | momentum_26 AND volume_26 | 10048.78 | 48.78 | sell / filled / 직전 완료 봉 목표 비중 0%; 다음 봉 시가 가정 |
| v2 | momentum_26 + volume_26 | 9675.46 | -324.54 | sell / filled / 직전 완료 봉 목표 비중 50%; 다음 봉 시가 가정 |
| v2 | breakout_8 AND reversion_12 | 10000.00 | 0.00 | 대기 /  / 새 신호 대기 |
| v2 | breakout_8 + reversion_12 | 9610.18 | -389.82 | 중단: 손실 한도 / sell / filled / 직전 완료 봉 목표 비중 0%; 다음 봉 시가 가정 |
| v2 | breakout_8 AND volume_26 | 9998.69 | -1.31 | sell / filled / 직전 완료 봉 목표 비중 0%; 다음 봉 시가 가정 |
| v2 | breakout_8 + volume_26 | 9579.25 | -420.75 | sell / filled / 직전 완료 봉 목표 비중 0%; 다음 봉 시가 가정 |
| v2 | reversion_12 AND volume_26 | 9297.82 | -702.18 | 중단: 손실 한도 / buy / partial / 직전 완료 봉 목표 비중 100%; 다음 봉 시가 가정 |
| v2 | reversion_12 + volume_26 | 9414.12 | -585.88 | 중단: 손실 한도 / sell / filled / 직전 완료 봉 목표 비중 50%; 다음 봉 시가 가정 |
| v2 | ema_12_26 | 9955.85 | -44.15 | buy / partial / EMA12 > EMA26; 조건 충족; EMA12=733.716, EMA26=733.7; 직전 완료 봉 목표를 다음 봉 시가에 모의 적용 |
| v2 | macd_12_26_9 | 9955.85 | -44.15 | buy / partial / MACD > 신호선 그리고 MACD > 0; 조건 충족; MACD=0.0155601, signal9=-2.12997; 직전 완료 봉 목표를 다음 봉 시가에 모의 적용 |
| v2 | rsi_14_recovery | 10000.00 | 0.00 | 대기 /  / 새 신호 대기 |
| v2 | bollinger_20_reentry | 10000.00 | 0.00 | 대기 /  / 새 신호 대기 |
| v2 | donchian_20 | 9948.84 | -51.16 | sell / filled / 종가 > 현재 봉을 제외한 직전 20봉 최고가; 조건 미충족; close=739.81, prior_high20=742.28; 직전 완료 봉 목표를 다음 봉 시가에 모의 적용 |
| v2 | atr_14_breakout | 9948.84 | -51.16 | sell / filled / 종가 > 직전 종가 + 직전 ATR14 그리고 종가 > EMA26; 조건 미충족; close=739.81, threshold=744.805, prior_ATR14=4.59507, EMA26=734.153; 직전 완료 봉 목표를 다음 봉 시가에 모의 적용 |
| v2 | session_vwap | 9961.14 | -38.86 | sell / filled / 종가 > 뉴욕 거래일별 누적 전형가격 VWAP; 조건 미충족; close=734.53, session_VWAP=738.361, session_volume=651546; 직전 완료 봉 목표를 다음 봉 시가에 모의 적용 |
| v2 | obv_20 | 9943.61 | -56.39 | buy / partial / OBV > OBV의 SMA20 그리고 종가 > EMA26; 조건 충족; OBV=-4.34663e+06, OBV_SMA20=-4.46778e+06, close=737.51, EMA26=735.635; 직전 완료 봉 목표를 다음 봉 시가에 모의 적용 |
| v2 | stochastic_14_3_recovery | 10000.00 | 0.00 | 대기 /  / 새 신호 대기 |
| v2 | mfi_14_recovery | 10000.00 | 0.00 | 대기 /  / 새 신호 대기 |
| v2 | adx_14_trend | 10000.00 | 0.00 | 대기 /  / 새 신호 대기 |
| v2 | aroon_25_trend | 10029.14 | 29.14 | sell / filled / Aroon25 Up > 70 그리고 Down < 30 (동률이면 최신 극값); 조건 미충족; Aroon_up=88, Aroon_down=48; 직전 완료 봉 목표를 다음 봉 시가에 모의 적용 |
| v2 | cci_20_momentum | 10022.77 | 22.77 | sell / filled / CCI20 > 100 (전형가격·평균절대편차); 조건 미충족; CCI20=98.8062; 직전 완료 봉 목표를 다음 봉 시가에 모의 적용 |
| v2 | williams_14_recovery | 10000.00 | 0.00 | 대기 /  / 새 신호 대기 |
| v2 | cmf_20_accumulation | 9965.10 | -34.90 | buy / partial / Chaikin Money Flow20 > 0.1; 조건 충족; CMF20=0.173065, volume20=2.14066e+06; 직전 완료 봉 목표를 다음 봉 시가에 모의 적용 |
| v2 | chaikin_3_10 | 9863.75 | -136.25 | buy / partial / ADL의 EMA3 - EMA10 > 0 그리고 종가 > EMA26; 조건 충족; Chaikin3_10=108.363, ADL=-5.61683e+06, close=737.51, EMA26=735.635; 직전 완료 봉 목표를 다음 봉 시가에 모의 적용 |
| v2 | roc_10_momentum | 9961.14 | -38.86 | sell / filled / 10봉 ROC > 1% 그리고 종가 > EMA26; 조건 미충족; ROC10_percent=-0.134597, close=734.53, EMA26=735.486; 직전 완료 봉 목표를 다음 봉 시가에 모의 적용 |
| v2 | trix_15_trend | 9873.16 | -126.84 | buy / partial / 15봉 삼중 EMA의 1봉 변화율 TRIX > 0 그리고 종가 > EMA26; 조건 충족; TRIX15_percent=0.0151548, close=737.51, EMA26=735.635; 직전 완료 봉 목표를 다음 봉 시가에 모의 적용 |
| v2 | keltner_20_breakout | 10000.00 | 0.00 | 대기 /  / 새 신호 대기 |
| v2 | opening_range_30m | 10038.70 | 38.70 | sell / filled / 뉴욕 09:30·09:45 두 완료 봉 최고가를 10:00 이후 종가가 돌파; 자료 부족·변동폭 또는 거래량 없음: 대기; close=740.21; 직전 완료 봉 목표를 다음 봉 시가에 모의 적용 |

### 같은 기간의 비용·노출 비교 (사후 연구)

| 전략 | 비용 전 | 비용 후 | 100% 보유 | 같은 평균 노출 보유 | 평균 노출 |
|---|---:|---:|---:|---:|---:|
| cash | 0.00% | 0.00% | -10.01% | -0.00% | 0.00% |
| buy_hold | -9.63% | -10.01% | -10.01% | -10.01% | 100.00% |
| trend_8_26 | -1.07% | -4.74% | -10.01% | -5.07% | 50.26% |
| momentum_26 | -3.96% | -9.83% | -10.01% | -4.92% | 48.68% |
| breakout_8 | -3.26% | -16.13% | -10.01% | -1.55% | 15.26% |
| reversion_12 | -3.54% | -15.31% | -10.01% | -2.64% | 26.05% |
| volume_26 | -2.95% | -10.02% | -10.01% | -0.83% | 8.16% |
| trend_8_26 AND momentum_26 | -1.26% | -6.11% | -10.01% | -4.34% | 42.89% |
| trend_8_26 + momentum_26 | -2.51% | -7.30% | -10.01% | -5.00% | 49.48% |
| trend_8_26 AND breakout_8 | -1.89% | -9.42% | -10.01% | -0.80% | 7.89% |
| trend_8_26 + breakout_8 | -2.13% | -10.40% | -10.01% | -3.32% | 32.77% |
| trend_8_26 AND reversion_12 | 1.15% | -5.42% | -10.01% | -0.75% | 7.37% |
| trend_8_26 + reversion_12 | -2.25% | -9.59% | -10.01% | -3.86% | 38.16% |
| trend_8_26 AND volume_26 | 2.22% | -0.75% | -10.01% | -0.27% | 2.63% |
| trend_8_26 + volume_26 | -1.96% | -7.20% | -10.01% | -2.96% | 29.21% |
| momentum_26 AND breakout_8 | -2.81% | -11.02% | -10.01% | -0.88% | 8.68% |
| momentum_26 + breakout_8 | -3.57% | -13.01% | -10.01% | -3.24% | 31.98% |
| momentum_26 AND reversion_12 | -2.68% | -9.01% | -10.01% | -0.61% | 6.05% |
| momentum_26 + reversion_12 | -3.70% | -11.67% | -10.01% | -3.78% | 37.37% |
| momentum_26 AND volume_26 | 1.58% | -0.53% | -10.01% | -0.16% | 1.58% |
| momentum_26 + volume_26 | -3.40% | -9.14% | -10.01% | -2.88% | 28.42% |
| breakout_8 AND reversion_12 | 0.00% | 0.00% | -10.01% | -0.00% | 0.00% |
| breakout_8 + reversion_12 | -3.35% | -14.82% | -10.01% | -2.10% | 20.67% |
| breakout_8 AND volume_26 | 0.37% | -0.47% | -10.01% | -0.05% | 0.53% |
| breakout_8 + volume_26 | -3.07% | -12.38% | -10.01% | -1.19% | 11.72% |
| reversion_12 AND volume_26 | -1.25% | -5.71% | -10.01% | -0.53% | 5.26% |
| reversion_12 + volume_26 | -3.21% | -11.95% | -10.01% | -1.74% | 17.11% |
| ema_12_26 | -0.51% | -2.57% | -10.01% | -5.05% | 50.00% |
| macd_12_26_9 | -0.45% | -4.54% | -10.01% | -3.06% | 30.26% |
| rsi_14_recovery | -0.96% | -6.22% | -10.01% | -0.35% | 3.42% |
| bollinger_20_reentry | 1.35% | -4.43% | -10.01% | -0.37% | 3.68% |
| donchian_20 | -2.30% | -7.11% | -10.01% | -0.53% | 5.26% |
| atr_14_breakout | -2.42% | -9.14% | -10.01% | -0.48% | 4.74% |
| session_vwap | -0.03% | -11.49% | -10.01% | -4.68% | 46.32% |
| obv_20 | -3.89% | -14.55% | -10.01% | -2.77% | 27.37% |
| stochastic_14_3_recovery | -3.21% | -13.22% | -10.01% | -0.70% | 6.84% |
| mfi_14_recovery | 0.45% | -1.63% | -10.01% | -0.13% | 1.32% |
| adx_14_trend | -3.13% | -5.93% | -10.01% | -0.96% | 9.47% |
| aroon_25_trend | -2.12% | -6.14% | -10.01% | -1.50% | 14.74% |
| cci_20_momentum | -5.69% | -11.82% | -10.01% | -1.66% | 16.32% |
| williams_14_recovery | -1.60% | -10.66% | -10.01% | -0.61% | 6.05% |
| cmf_20_accumulation | -5.33% | -12.22% | -10.01% | -1.84% | 18.16% |
| chaikin_3_10 | -5.66% | -14.34% | -10.01% | -3.59% | 35.53% |
| roc_10_momentum | -1.82% | -7.81% | -10.01% | -1.36% | 13.42% |
| trix_15_trend | -0.68% | -5.16% | -10.01% | -3.99% | 39.47% |
| keltner_20_breakout | -3.35% | -6.15% | -10.01% | -0.29% | 2.89% |
| opening_range_30m | 4.95% | -0.21% | -10.01% | -2.08% | 20.53% |

동일 구간·초기 자금, 종료 시 청산 비용 포함. 노출 맞춤은 사후 설명용이며 v2 실제 계좌 성과가 아닙니다.
[낙폭 분해·비용 영향·전체 구간](CAT/comparison.json)

[v1 전체 기록](CAT/accounts.json) · [v2 전체 기록](CAT/accounts-v2.json)

## WMT 계좌

| 모델 | 전략 | 평가액 USD | 손익 USD | 최근 매매·이유 |
|---|---|---:|---:|---|
| v1 | cash | 10000.00 | 0.00 | 대기 /  / 새 신호 대기 |
| v1 | buy_hold | 10012.55 | 12.55 | buy /  / buy_hold: prior completed bar target 100%; next bar open simulation |
| v1 | trend_8_26 | 9959.02 | -40.98 | buy /  / trend_8_26: prior completed bar target 100%; next bar open simulation |
| v1 | momentum_26 | 10043.97 | 43.97 | sell /  / momentum_26: prior completed bar target 0%; next bar open simulation |
| v1 | breakout_8 | 9953.51 | -46.49 | sell /  / breakout_8: prior completed bar target 0%; next bar open simulation |
| v1 | reversion_12 | 10043.97 | 43.97 | sell /  / reversion_12: prior completed bar target 0%; next bar open simulation |
| v1 | volume_26 | 9979.72 | -20.28 | sell /  / volume_26: prior completed bar target 0%; next bar open simulation |
| v1 | trend_8_26 AND momentum_26 | 10000.00 | 0.00 | 대기 /  / 새 신호 대기 |
| v1 | trend_8_26 + momentum_26 | 10001.45 | 1.45 | sell /  / trend_8_26 + momentum_26: prior completed bar target 50%; next bar open simulation |
| v1 | trend_8_26 AND breakout_8 | 10000.00 | 0.00 | 대기 /  / 새 신호 대기 |
| v1 | trend_8_26 + breakout_8 | 9956.25 | -43.75 | sell /  / trend_8_26 + breakout_8: prior completed bar target 50%; next bar open simulation |
| v1 | trend_8_26 AND reversion_12 | 10000.00 | 0.00 | 대기 /  / 새 신호 대기 |
| v1 | trend_8_26 + reversion_12 | 10001.45 | 1.45 | sell /  / trend_8_26 + reversion_12: prior completed bar target 50%; next bar open simulation |
| v1 | trend_8_26 AND volume_26 | 10000.00 | 0.00 | 대기 /  / 새 신호 대기 |
| v1 | trend_8_26 + volume_26 | 9969.33 | -30.67 | sell /  / trend_8_26 + volume_26: prior completed bar target 50%; next bar open simulation |
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
| v1 | ema_12_26 | 10012.55 | 12.55 | buy /  / EMA12 > EMA26; 조건 충족; EMA12=118.245, EMA26=118.045 |
| v1 | macd_12_26_9 | 10000.00 | 0.00 | 대기 /  / 새 신호 대기 |
| v1 | rsi_14_recovery | 10000.00 | 0.00 | 대기 /  / 새 신호 대기 |
| v1 | bollinger_20_reentry | 10000.00 | 0.00 | 대기 /  / 새 신호 대기 |
| v1 | donchian_20 | 10000.00 | 0.00 | 대기 /  / 새 신호 대기 |
| v1 | atr_14_breakout | 9979.72 | -20.28 | sell /  / 종가 > 직전 종가 + 직전 ATR14 그리고 종가 > EMA26; 조건 미충족; close=119.375, threshold=119.607, prior_ATR14=0.486823, EMA26=118.217 |
| v1 | session_vwap | 9839.22 | -160.78 | sell /  / 종가 > 뉴욕 거래일별 누적 전형가격 VWAP; 조건 미충족; close=118.745, session_VWAP=118.899, session_volume=6.77102e+06 |
| v1 | obv_20 | 10000.00 | 0.00 | 대기 /  / 새 신호 대기 |
| v1 | stochastic_14_3_recovery | 9979.72 | -20.28 | sell /  / 직전 %K14 < 20에서 %K14가 %D3 상향 돌파 (한 봉 목표); 조건 미충족; K14=93.8952, D3=60.8222, previous_K14=82.4242, previous_D3=34.5012 |
| v1 | mfi_14_recovery | 10000.00 | 0.00 | 대기 /  / 새 신호 대기 |
| v1 | adx_14_trend | 10012.55 | 12.55 | buy /  / Wilder ADX14 >= 25 그리고 +DI14 > -DI14; 조건 충족; ADX14=29.9186, plus_DI14=22.635, minus_DI14=22.4078 |
| v1 | aroon_25_trend | 10000.00 | 0.00 | 대기 /  / 새 신호 대기 |
| v1 | cci_20_momentum | 9932.96 | -67.04 | sell /  / CCI20 > 100 (전형가격·평균절대편차); 조건 미충족; CCI20=99.1325 |
| v1 | williams_14_recovery | 9979.72 | -20.28 | sell /  / 직전 Williams %R14 < -80, 현재 >= -80 (한 봉 목표); 조건 미충족; Williams_R14=-6.10484, previous_R14=-17.5758 |
| v1 | cmf_20_accumulation | 10000.00 | 0.00 | 대기 /  / 새 신호 대기 |
| v1 | chaikin_3_10 | 9839.08 | -160.92 | buy /  / ADL의 EMA3 - EMA10 > 0 그리고 종가 > EMA26; 조건 충족; Chaikin3_10=175820, ADL=1.95122e+07, close=118.735, EMA26=118.371 |
| v1 | roc_10_momentum | 10000.00 | 0.00 | 대기 /  / 새 신호 대기 |
| v1 | trix_15_trend | 9928.92 | -71.08 | buy /  / 15봉 삼중 EMA의 1봉 변화율 TRIX > 0 그리고 종가 > EMA26; 조건 충족; TRIX15_percent=0.0496307, close=119.12, EMA26=118.125 |
| v1 | keltner_20_breakout | 10000.00 | 0.00 | 대기 /  / 새 신호 대기 |
| v1 | opening_range_30m | 10000.00 | 0.00 | 대기 /  / 새 신호 대기 |
| v2 | cash | 10000.00 | 0.00 | 대기 /  / 새 신호 대기 |
| v2 | buy_hold | 10608.20 | 608.20 | buy / partial / 직전 완료 봉 목표 비중 100%; 다음 봉 시가 가정 |
| v2 | trend_8_26 | 10366.93 | 366.93 | buy / partial / 직전 완료 봉 목표 비중 100%; 다음 봉 시가 가정 |
| v2 | momentum_26 | 10465.54 | 465.54 | sell / filled / 직전 완료 봉 목표 비중 0%; 다음 봉 시가 가정 |
| v2 | breakout_8 | 9916.34 | -83.66 | sell / filled / 직전 완료 봉 목표 비중 0%; 다음 봉 시가 가정 |
| v2 | reversion_12 | 9953.01 | -46.99 | sell / filled / 직전 완료 봉 목표 비중 0%; 다음 봉 시가 가정 |
| v2 | volume_26 | 9943.08 | -56.92 | sell / filled / 직전 완료 봉 목표 비중 0%; 다음 봉 시가 가정 |
| v2 | trend_8_26 AND momentum_26 | 10410.62 | 410.62 | sell / filled / 직전 완료 봉 목표 비중 0%; 다음 봉 시가 가정 |
| v2 | trend_8_26 + momentum_26 | 10416.11 | 416.11 | sell / filled / 직전 완료 봉 목표 비중 50%; 다음 봉 시가 가정 |
| v2 | trend_8_26 AND breakout_8 | 10088.55 | 88.55 | sell / filled / 직전 완료 봉 목표 비중 0%; 다음 봉 시가 가정 |
| v2 | trend_8_26 + breakout_8 | 10139.53 | 139.53 | sell / filled / 직전 완료 봉 목표 비중 50%; 다음 봉 시가 가정 |
| v2 | trend_8_26 AND reversion_12 | 9808.74 | -191.26 | sell / filled / 직전 완료 봉 목표 비중 0%; 다음 봉 시가 가정 |
| v2 | trend_8_26 + reversion_12 | 10159.35 | 159.35 | sell / filled / 직전 완료 봉 목표 비중 50%; 다음 봉 시가 가정 |
| v2 | trend_8_26 AND volume_26 | 9949.23 | -50.77 | sell / filled / 직전 완료 봉 목표 비중 0%; 다음 봉 시가 가정 |
| v2 | trend_8_26 + volume_26 | 10154.21 | 154.21 | sell / filled / 직전 완료 봉 목표 비중 50%; 다음 봉 시가 가정 |
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
| v2 | ema_12_26 | 10011.55 | 11.55 | buy / partial / EMA12 > EMA26; 조건 충족; EMA12=118.245, EMA26=118.045; 직전 완료 봉 목표를 다음 봉 시가에 모의 적용 |
| v2 | macd_12_26_9 | 10000.00 | 0.00 | 대기 /  / 새 신호 대기 |
| v2 | rsi_14_recovery | 10000.00 | 0.00 | 대기 /  / 새 신호 대기 |
| v2 | bollinger_20_reentry | 10000.00 | 0.00 | 대기 /  / 새 신호 대기 |
| v2 | donchian_20 | 10000.00 | 0.00 | 대기 /  / 새 신호 대기 |
| v2 | atr_14_breakout | 9977.72 | -22.28 | sell / filled / 종가 > 직전 종가 + 직전 ATR14 그리고 종가 > EMA26; 조건 미충족; close=119.375, threshold=119.607, prior_ATR14=0.486823, EMA26=118.217; 직전 완료 봉 목표를 다음 봉 시가에 모의 적용 |
| v2 | session_vwap | 9835.28 | -164.72 | sell / filled / 종가 > 뉴욕 거래일별 누적 전형가격 VWAP; 조건 미충족; close=118.745, session_VWAP=118.899, session_volume=6.77102e+06; 직전 완료 봉 목표를 다음 봉 시가에 모의 적용 |
| v2 | obv_20 | 10000.00 | 0.00 | 대기 /  / 새 신호 대기 |
| v2 | stochastic_14_3_recovery | 9977.72 | -22.28 | sell / filled / 직전 %K14 < 20에서 %K14가 %D3 상향 돌파 (한 봉 목표); 조건 미충족; K14=93.8952, D3=60.8222, previous_K14=82.4242, previous_D3=34.5012; 직전 완료 봉 목표를 다음 봉 시가에 모의 적용 |
| v2 | mfi_14_recovery | 10000.00 | 0.00 | 대기 /  / 새 신호 대기 |
| v2 | adx_14_trend | 10011.55 | 11.55 | buy / partial / Wilder ADX14 >= 25 그리고 +DI14 > -DI14; 조건 충족; ADX14=29.9186, plus_DI14=22.635, minus_DI14=22.4078; 직전 완료 봉 목표를 다음 봉 시가에 모의 적용 |
| v2 | aroon_25_trend | 10000.00 | 0.00 | 대기 /  / 새 신호 대기 |
| v2 | cci_20_momentum | 9930.98 | -69.02 | sell / filled / CCI20 > 100 (전형가격·평균절대편차); 조건 미충족; CCI20=99.1325; 직전 완료 봉 목표를 다음 봉 시가에 모의 적용 |
| v2 | williams_14_recovery | 9977.72 | -22.28 | sell / filled / 직전 Williams %R14 < -80, 현재 >= -80 (한 봉 목표); 조건 미충족; Williams_R14=-6.10484, previous_R14=-17.5758; 직전 완료 봉 목표를 다음 봉 시가에 모의 적용 |
| v2 | cmf_20_accumulation | 10000.00 | 0.00 | 대기 /  / 새 신호 대기 |
| v2 | chaikin_3_10 | 9836.13 | -163.87 | buy / partial / ADL의 EMA3 - EMA10 > 0 그리고 종가 > EMA26; 조건 충족; Chaikin3_10=175820, ADL=1.95122e+07, close=118.735, EMA26=118.371; 직전 완료 봉 목표를 다음 봉 시가에 모의 적용 |
| v2 | roc_10_momentum | 10000.00 | 0.00 | 대기 /  / 새 신호 대기 |
| v2 | trix_15_trend | 9927.93 | -72.07 | buy / partial / 15봉 삼중 EMA의 1봉 변화율 TRIX > 0 그리고 종가 > EMA26; 조건 충족; TRIX15_percent=0.0496307, close=119.12, EMA26=118.125; 직전 완료 봉 목표를 다음 봉 시가에 모의 적용 |
| v2 | keltner_20_breakout | 10000.00 | 0.00 | 대기 /  / 새 신호 대기 |
| v2 | opening_range_30m | 10000.00 | 0.00 | 대기 /  / 새 신호 대기 |

### 같은 기간의 비용·노출 비교 (사후 연구)

| 전략 | 비용 전 | 비용 후 | 100% 보유 | 같은 평균 노출 보유 | 평균 노출 |
|---|---:|---:|---:|---:|---:|
| cash | 0.00% | 0.00% | 9.45% | 0.00% | 0.00% |
| buy_hold | 9.91% | 9.45% | 9.45% | 9.45% | 100.00% |
| trend_8_26 | 9.19% | 6.03% | 9.45% | 6.54% | 69.47% |
| momentum_26 | 7.43% | 3.45% | 9.45% | 6.57% | 69.74% |
| breakout_8 | 5.45% | -11.60% | 9.45% | 2.49% | 26.58% |
| reversion_12 | 4.02% | -5.96% | 9.45% | 1.58% | 16.84% |
| volume_26 | -0.20% | -5.50% | 9.45% | 0.52% | 5.53% |
| trend_8_26 AND momentum_26 | 8.87% | 4.83% | 9.45% | 5.94% | 63.16% |
| trend_8_26 + momentum_26 | 8.32% | 4.74% | 9.45% | 6.56% | 69.61% |
| trend_8_26 AND breakout_8 | 6.92% | -6.91% | 9.45% | 2.09% | 22.37% |
| trend_8_26 + breakout_8 | 7.32% | -3.17% | 9.45% | 4.51% | 48.03% |
| trend_8_26 AND reversion_12 | 0.42% | -4.91% | 9.45% | 0.64% | 6.84% |
| trend_8_26 + reversion_12 | 6.61% | 0.08% | 9.45% | 4.05% | 43.16% |
| trend_8_26 AND volume_26 | 1.13% | -1.39% | 9.45% | 0.20% | 2.11% |
| trend_8_26 + volume_26 | 4.43% | 0.53% | 9.45% | 3.52% | 37.50% |
| momentum_26 AND breakout_8 | 5.58% | -8.47% | 9.45% | 2.19% | 23.42% |
| momentum_26 + breakout_8 | 6.45% | -3.96% | 9.45% | 4.52% | 48.16% |
| momentum_26 AND reversion_12 | 1.36% | -4.43% | 9.45% | 0.71% | 7.63% |
| momentum_26 + reversion_12 | 5.75% | 0.53% | 9.45% | 4.06% | 43.29% |
| momentum_26 AND volume_26 | 0.44% | -3.69% | 9.45% | 0.27% | 2.89% |
| momentum_26 + volume_26 | 3.58% | -0.91% | 9.45% | 3.53% | 37.63% |
| breakout_8 AND reversion_12 | 0.00% | 0.00% | 9.45% | 0.00% | 0.00% |
| breakout_8 + reversion_12 | 4.76% | -8.24% | 9.45% | 2.03% | 21.72% |
| breakout_8 AND volume_26 | 1.29% | -0.82% | 9.45% | 0.15% | 1.58% |
| breakout_8 + volume_26 | 2.62% | -7.82% | 9.45% | 1.50% | 16.06% |
| reversion_12 AND volume_26 | -0.51% | -2.99% | 9.45% | 0.22% | 2.37% |
| reversion_12 + volume_26 | 1.90% | -5.33% | 9.45% | 1.05% | 11.19% |
| ema_12_26 | 9.01% | 7.64% | 9.45% | 6.44% | 68.42% |
| macd_12_26_9 | 8.10% | 4.53% | 9.45% | 3.38% | 36.05% |
| rsi_14_recovery | -0.68% | -2.74% | 9.45% | 0.12% | 1.32% |
| bollinger_20_reentry | 0.93% | -2.41% | 9.45% | 0.20% | 2.11% |
| donchian_20 | 4.64% | -8.52% | 9.45% | 1.33% | 14.21% |
| atr_14_breakout | -0.51% | -10.81% | 9.45% | 0.76% | 8.16% |
| session_vwap | 7.25% | -3.03% | 9.45% | 5.72% | 60.79% |
| obv_20 | 8.12% | 0.25% | 9.45% | 5.27% | 56.05% |
| stochastic_14_3_recovery | 1.43% | -9.06% | 9.45% | 0.64% | 6.84% |
| mfi_14_recovery | 0.02% | -0.81% | 9.45% | 0.05% | 0.53% |
| adx_14_trend | 8.85% | 6.14% | 9.45% | 4.77% | 50.79% |
| aroon_25_trend | 6.70% | 1.88% | 9.45% | 2.98% | 31.84% |
| cci_20_momentum | 7.75% | -0.52% | 9.45% | 3.11% | 33.16% |
| williams_14_recovery | 0.23% | -8.61% | 9.45% | 0.54% | 5.79% |
| cmf_20_accumulation | 9.49% | 1.51% | 9.45% | 3.68% | 39.21% |
| chaikin_3_10 | 5.44% | -2.23% | 9.45% | 5.00% | 53.16% |
| roc_10_momentum | -0.29% | -5.58% | 9.45% | 1.45% | 15.53% |
| trix_15_trend | 8.05% | 5.80% | 9.45% | 6.07% | 64.47% |
| keltner_20_breakout | 6.87% | -0.08% | 9.45% | 2.59% | 27.63% |
| opening_range_30m | 10.55% | 5.12% | 9.45% | 3.46% | 36.84% |

동일 구간·초기 자금, 종료 시 청산 비용 포함. 노출 맞춤은 사후 설명용이며 v2 실제 계좌 성과가 아닙니다.
[낙폭 분해·비용 영향·전체 구간](WMT/comparison.json)

[v1 전체 기록](WMT/accounts.json) · [v2 전체 기록](WMT/accounts-v2.json)
