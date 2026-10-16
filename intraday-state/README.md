# 모의투자 운영 현황

[PC·서버 장애 진단과 복구 방법](https://github.com/BaekJaeYeol/paper-trading-program/blob/main/investment-lab/docs/failure-recovery.md)

이번 실행 복구: {}

완료 봉 확인 주기: 기록 7/13회 · 기록 없는 예정 6회 · 아직 판정 전 13회 · 주의: 예약 시작 지연 또는 실행·저장 누락을 확인하세요.

[주기 판정 기준](https://github.com/BaekJaeYeol/paper-trading-program/blob/main/investment-lab/docs/session-coverage.md)

최근 확인: 2026-10-16T17:07:00.349711+00:00 (UTC)
다음 15분 확인 목표 (세션 실행 중에만 적용): 2026-10-16T17:22:00+00:00 (UTC, 실행 지연 가능)

실제 주문 없음. v1 기존 계좌와 v2 새 계좌의 시작일이 다르므로 수익률을 직접 우열 비교하지 마세요.
v2는 다음 봉 시가에 비용·스프레드·직전 거래량 제한을 적용한 가상 체결입니다. 미체결 잔량은 만료됩니다.

| 종목 | 상태 | 최근 성공 UTC | 마지막 완료 봉 UTC | 이번 새 봉 |
|---|---|---|---|---|
| SPY | updated | 2026-10-16T17:07:00.349711+00:00 | 2026-10-16T16:45:00+00:00 | 1 |
| QQQ | updated | 2026-10-16T17:07:00.349711+00:00 | 2026-10-16T16:45:00+00:00 | 1 |
| IWM | updated | 2026-10-16T17:07:00.349711+00:00 | 2026-10-16T16:45:00+00:00 | 1 |
| DIA | updated | 2026-10-16T17:07:00.349711+00:00 | 2026-10-16T16:45:00+00:00 | 1 |
| MSFT | updated | 2026-10-16T17:07:00.349711+00:00 | 2026-10-16T16:45:00+00:00 | 1 |
| JPM | updated | 2026-10-16T17:07:00.349711+00:00 | 2026-10-16T16:45:00+00:00 | 1 |
| XOM | updated | 2026-10-16T17:07:00.349711+00:00 | 2026-10-16T16:45:00+00:00 | 1 |
| JNJ | updated | 2026-10-16T17:07:00.349711+00:00 | 2026-10-16T16:45:00+00:00 | 1 |
| CAT | updated | 2026-10-16T17:07:00.349711+00:00 | 2026-10-16T16:45:00+00:00 | 1 |
| WMT | updated | 2026-10-16T17:07:00.349711+00:00 | 2026-10-16T16:45:00+00:00 | 1 |

이번 실행 소요: 43.43초
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
| v1 | buy_hold | 9890.07 | -109.93 | buy /  / buy_hold: prior completed bar target 100%; next bar open simulation |
| v1 | trend_8_26 | 9902.75 | -97.25 | sell /  / trend_8_26: prior completed bar target 0%; next bar open simulation |
| v1 | momentum_26 | 9916.54 | -83.46 | sell /  / momentum_26: prior completed bar target 0%; next bar open simulation |
| v1 | breakout_8 | 10000.00 | 0.00 | 대기 /  / 새 신호 대기 |
| v1 | reversion_12 | 9933.49 | -66.51 | buy /  / reversion_12: prior completed bar target 100%; next bar open simulation |
| v1 | volume_26 | 9925.86 | -74.14 | sell /  / volume_26: prior completed bar target 0%; next bar open simulation |
| v1 | trend_8_26 AND momentum_26 | 9916.54 | -83.46 | sell /  / trend_8_26 AND momentum_26: prior completed bar target 0%; next bar open simulation |
| v1 | trend_8_26 + momentum_26 | 9909.65 | -90.35 | sell /  / trend_8_26 + momentum_26: prior completed bar target 0%; next bar open simulation |
| v1 | trend_8_26 AND breakout_8 | 10000.00 | 0.00 | 대기 /  / 새 신호 대기 |
| v1 | trend_8_26 + breakout_8 | 9951.22 | -48.78 | sell /  / trend_8_26 + breakout_8: prior completed bar target 0%; next bar open simulation |
| v1 | trend_8_26 AND reversion_12 | 9946.23 | -53.77 | sell /  / trend_8_26 AND reversion_12: prior completed bar target 0%; next bar open simulation |
| v1 | trend_8_26 + reversion_12 | 9918.06 | -81.94 | buy /  / trend_8_26 + reversion_12: prior completed bar target 50%; next bar open simulation |
| v1 | trend_8_26 AND volume_26 | 9925.86 | -74.14 | sell /  / trend_8_26 AND volume_26: prior completed bar target 0%; next bar open simulation |
| v1 | trend_8_26 + volume_26 | 9914.27 | -85.73 | sell /  / trend_8_26 + volume_26: prior completed bar target 0%; next bar open simulation |
| v1 | momentum_26 AND breakout_8 | 10000.00 | 0.00 | 대기 /  / 새 신호 대기 |
| v1 | momentum_26 + breakout_8 | 9958.17 | -41.83 | sell /  / momentum_26 + breakout_8: prior completed bar target 0%; next bar open simulation |
| v1 | momentum_26 AND reversion_12 | 10000.00 | 0.00 | 대기 /  / 새 신호 대기 |
| v1 | momentum_26 + reversion_12 | 9944.82 | -55.18 | buy /  / momentum_26 + reversion_12: prior completed bar target 50%; next bar open simulation |
| v1 | momentum_26 AND volume_26 | 9939.68 | -60.32 | sell /  / momentum_26 AND volume_26: prior completed bar target 0%; next bar open simulation |
| v1 | momentum_26 + volume_26 | 9921.17 | -78.83 | sell /  / momentum_26 + volume_26: prior completed bar target 0%; next bar open simulation |
| v1 | breakout_8 AND reversion_12 | 10000.00 | 0.00 | 대기 /  / 새 신호 대기 |
| v1 | breakout_8 + reversion_12 | 9966.65 | -33.35 | buy /  / breakout_8 + reversion_12: prior completed bar target 50%; next bar open simulation |
| v1 | breakout_8 AND volume_26 | 10000.00 | 0.00 | 대기 /  / 새 신호 대기 |
| v1 | breakout_8 + volume_26 | 9962.84 | -37.16 | sell /  / breakout_8 + volume_26: prior completed bar target 0%; next bar open simulation |
| v1 | reversion_12 AND volume_26 | 9946.23 | -53.77 | sell /  / reversion_12 AND volume_26: prior completed bar target 0%; next bar open simulation |
| v1 | reversion_12 + volume_26 | 9929.65 | -70.35 | buy /  / reversion_12 + volume_26: prior completed bar target 50%; next bar open simulation |
| v1 | ema_12_26 | 9902.75 | -97.25 | sell /  / EMA12 > EMA26; 조건 미충족; EMA12=770.416, EMA26=770.512 |
| v1 | macd_12_26_9 | 9916.54 | -83.46 | sell /  / MACD > 신호선 그리고 MACD > 0; 조건 미충족; MACD=0.273669, signal9=0.379179 |
| v1 | rsi_14_recovery | 10000.00 | 0.00 | 대기 /  / 새 신호 대기 |
| v1 | bollinger_20_reentry | 9898.52 | -101.48 | sell /  / 직전 종가 < 직전 하단밴드, 현재 하단밴드 <= 종가 <= SMA20 (한 봉 목표); 조건 미충족; close=767.51, lower20=767.203, SMA20=770.361, previous_lower20=767.656 |
| v1 | donchian_20 | 10000.00 | 0.00 | 대기 /  / 새 신호 대기 |
| v1 | atr_14_breakout | 10000.00 | 0.00 | 대기 /  / 새 신호 대기 |
| v1 | session_vwap | 9891.58 | -108.42 | sell /  / 종가 > 뉴욕 거래일별 누적 전형가격 VWAP; 조건 미충족; close=771.41, session_VWAP=771.735, session_volume=1.75958e+07 |
| v1 | obv_20 | 9931.74 | -68.26 | sell /  / OBV > OBV의 SMA20 그리고 종가 > EMA26; 조건 미충족; OBV=-708839, OBV_SMA20=2.15302e+06, close=771.03, EMA26=770.746 |
| v1 | stochastic_14_3_recovery | 9954.50 | -45.50 | sell /  / 직전 %K14 < 20에서 %K14가 %D3 상향 돌파 (한 봉 목표); 조건 미충족; K14=13.943, D3=11.5022, previous_K14=20.3896, previous_D3=8.88861 |
| v1 | mfi_14_recovery | 10000.00 | 0.00 | 대기 /  / 새 신호 대기 |
| v1 | adx_14_trend | 10000.00 | 0.00 | 대기 /  / 새 신호 대기 |
| v1 | aroon_25_trend | 9902.37 | -97.63 | sell /  / Aroon25 Up > 70 그리고 Down < 30 (동률이면 최신 극값); 조건 미충족; Aroon_up=72, Aroon_down=100 |
| v1 | cci_20_momentum | 9936.89 | -63.11 | sell /  / CCI20 > 100 (전형가격·평균절대편차); 조건 미충족; CCI20=66.0792 |
| v1 | williams_14_recovery | 9954.50 | -45.50 | sell /  / 직전 Williams %R14 < -80, 현재 >= -80 (한 봉 목표); 조건 미충족; Williams_R14=-86.057, previous_R14=-79.6104 |
| v1 | cmf_20_accumulation | 9929.81 | -70.19 | sell /  / Chaikin Money Flow20 > 0.1; 조건 미충족; CMF20=-0.158867, volume20=2.42577e+07 |
| v1 | chaikin_3_10 | 9946.30 | -53.70 | sell /  / ADL의 EMA3 - EMA10 > 0 그리고 종가 > EMA26; 조건 미충족; Chaikin3_10=-174742, ADL=3.14745e+07, close=772.2, EMA26=770.668 |
| v1 | roc_10_momentum | 10000.00 | 0.00 | 대기 /  / 새 신호 대기 |
| v1 | trix_15_trend | 9916.54 | -83.46 | sell /  / 15봉 삼중 EMA의 1봉 변화율 TRIX > 0 그리고 종가 > EMA26; 조건 미충족; TRIX15_percent=0.00866315, close=769.855, EMA26=770.806 |
| v1 | keltner_20_breakout | 10000.00 | 0.00 | 대기 /  / 새 신호 대기 |
| v1 | opening_range_30m | 9946.30 | -53.70 | sell /  / 뉴욕 09:30·09:45 두 완료 봉 최고가를 10:00 이후 종가가 돌파; 자료 부족·변동폭 또는 거래량 없음: 대기; close=772.2 |
| v2 | cash | 10000.00 | 0.00 | 대기 /  / 새 신호 대기 |
| v2 | buy_hold | 9818.73 | -181.27 | buy / partial / 직전 완료 봉 목표 비중 100%; 다음 봉 시가 가정 |
| v2 | trend_8_26 | 9786.41 | -213.59 | sell / filled / 직전 완료 봉 목표 비중 0%; 다음 봉 시가 가정 |
| v2 | momentum_26 | 9770.62 | -229.38 | sell / filled / 직전 완료 봉 목표 비중 0%; 다음 봉 시가 가정 |
| v2 | breakout_8 | 9598.61 | -401.39 | sell / filled / 직전 완료 봉 목표 비중 0%; 다음 봉 시가 가정 |
| v2 | reversion_12 | 9471.47 | -528.53 | buy / partial / 직전 완료 봉 목표 비중 100%; 다음 봉 시가 가정 |
| v2 | volume_26 | 9369.58 | -630.42 | sell / filled / 직전 완료 봉 목표 비중 0%; 다음 봉 시가 가정 |
| v2 | trend_8_26 AND momentum_26 | 9777.28 | -222.72 | sell / filled / 직전 완료 봉 목표 비중 0%; 다음 봉 시가 가정 |
| v2 | trend_8_26 + momentum_26 | 9778.53 | -221.47 | sell / filled / 직전 완료 봉 목표 비중 0%; 다음 봉 시가 가정 |
| v2 | trend_8_26 AND breakout_8 | 9825.21 | -174.79 | sell / filled / 직전 완료 봉 목표 비중 0%; 다음 봉 시가 가정 |
| v2 | trend_8_26 + breakout_8 | 9691.90 | -308.10 | sell / filled / 직전 완료 봉 목표 비중 0%; 다음 봉 시가 가정 |
| v2 | trend_8_26 AND reversion_12 | 9840.93 | -159.07 | sell / filled / 직전 완료 봉 목표 비중 0%; 다음 봉 시가 가정 |
| v2 | trend_8_26 + reversion_12 | 9627.30 | -372.70 | buy / filled / 직전 완료 봉 목표 비중 50%; 다음 봉 시가 가정 |
| v2 | trend_8_26 AND volume_26 | 9770.95 | -229.05 | sell / filled / 직전 완료 봉 목표 비중 0%; 다음 봉 시가 가정 |
| v2 | trend_8_26 + volume_26 | 9595.60 | -404.40 | sell / filled / 직전 완료 봉 목표 비중 0%; 다음 봉 시가 가정 |
| v2 | momentum_26 AND breakout_8 | 9783.53 | -216.47 | sell / filled / 직전 완료 봉 목표 비중 0%; 다음 봉 시가 가정 |
| v2 | momentum_26 + breakout_8 | 9684.14 | -315.86 | sell / filled / 직전 완료 봉 목표 비중 0%; 다음 봉 시가 가정 |
| v2 | momentum_26 AND reversion_12 | 9963.21 | -36.79 | sell / filled / 직전 완료 봉 목표 비중 0%; 다음 봉 시가 가정 |
| v2 | momentum_26 + reversion_12 | 9660.02 | -339.98 | buy / filled / 직전 완료 봉 목표 비중 50%; 다음 봉 시가 가정 |
| v2 | momentum_26 AND volume_26 | 9855.46 | -144.54 | sell / filled / 직전 완료 봉 목표 비중 0%; 다음 봉 시가 가정 |
| v2 | momentum_26 + volume_26 | 9628.18 | -371.82 | sell / filled / 직전 완료 봉 목표 비중 0%; 다음 봉 시가 가정 |
| v2 | breakout_8 AND reversion_12 | 10000.00 | 0.00 | 대기 /  / 새 신호 대기 |
| v2 | breakout_8 + reversion_12 | 9574.51 | -425.49 | buy / filled / 직전 완료 봉 목표 비중 50%; 다음 봉 시가 가정 |
| v2 | breakout_8 AND volume_26 | 9933.18 | -66.82 | sell / filled / 직전 완료 봉 목표 비중 0%; 다음 봉 시가 가정 |
| v2 | breakout_8 + volume_26 | 9522.95 | -477.05 | sell / filled / 직전 완료 봉 목표 비중 0%; 다음 봉 시가 가정 |
| v2 | reversion_12 AND volume_26 | 9689.01 | -310.99 | sell / filled / 직전 완료 봉 목표 비중 0%; 다음 봉 시가 가정 |
| v2 | reversion_12 + volume_26 | 9499.56 | -500.44 | buy / filled / 직전 완료 봉 목표 비중 50%; 다음 봉 시가 가정 |
| v2 | ema_12_26 | 9900.77 | -99.23 | sell / filled / EMA12 > EMA26; 조건 미충족; EMA12=770.416, EMA26=770.512; 직전 완료 봉 목표를 다음 봉 시가에 모의 적용 |
| v2 | macd_12_26_9 | 9914.56 | -85.44 | sell / filled / MACD > 신호선 그리고 MACD > 0; 조건 미충족; MACD=0.273669, signal9=0.379179; 직전 완료 봉 목표를 다음 봉 시가에 모의 적용 |
| v2 | rsi_14_recovery | 10000.00 | 0.00 | 대기 /  / 새 신호 대기 |
| v2 | bollinger_20_reentry | 9894.56 | -105.44 | sell / filled / 직전 종가 < 직전 하단밴드, 현재 하단밴드 <= 종가 <= SMA20 (한 봉 목표); 조건 미충족; close=767.51, lower20=767.203, SMA20=770.361, previous_lower20=767.656; 직전 완료 봉 목표를 다음 봉 시가에 모의 적용 |
| v2 | donchian_20 | 10000.00 | 0.00 | 대기 /  / 새 신호 대기 |
| v2 | atr_14_breakout | 10000.00 | 0.00 | 대기 /  / 새 신호 대기 |
| v2 | session_vwap | 9887.63 | -112.37 | sell / filled / 종가 > 뉴욕 거래일별 누적 전형가격 VWAP; 조건 미충족; close=771.41, session_VWAP=771.735, session_volume=1.75958e+07; 직전 완료 봉 목표를 다음 봉 시가에 모의 적용 |
| v2 | obv_20 | 9929.76 | -70.24 | sell / filled / OBV > OBV의 SMA20 그리고 종가 > EMA26; 조건 미충족; OBV=-708839, OBV_SMA20=2.15302e+06, close=771.03, EMA26=770.746; 직전 완료 봉 목표를 다음 봉 시가에 모의 적용 |
| v2 | stochastic_14_3_recovery | 9952.51 | -47.49 | sell / filled / 직전 %K14 < 20에서 %K14가 %D3 상향 돌파 (한 봉 목표); 조건 미충족; K14=13.943, D3=11.5022, previous_K14=20.3896, previous_D3=8.88861; 직전 완료 봉 목표를 다음 봉 시가에 모의 적용 |
| v2 | mfi_14_recovery | 10000.00 | 0.00 | 대기 /  / 새 신호 대기 |
| v2 | adx_14_trend | 10000.00 | 0.00 | 대기 /  / 새 신호 대기 |
| v2 | aroon_25_trend | 9900.39 | -99.61 | sell / filled / Aroon25 Up > 70 그리고 Down < 30 (동률이면 최신 극값); 조건 미충족; Aroon_up=72, Aroon_down=100; 직전 완료 봉 목표를 다음 봉 시가에 모의 적용 |
| v2 | cci_20_momentum | 9934.91 | -65.09 | sell / filled / CCI20 > 100 (전형가격·평균절대편차); 조건 미충족; CCI20=66.0792; 직전 완료 봉 목표를 다음 봉 시가에 모의 적용 |
| v2 | williams_14_recovery | 9952.51 | -47.49 | sell / filled / 직전 Williams %R14 < -80, 현재 >= -80 (한 봉 목표); 조건 미충족; Williams_R14=-86.057, previous_R14=-79.6104; 직전 완료 봉 목표를 다음 봉 시가에 모의 적용 |
| v2 | cmf_20_accumulation | 9927.82 | -72.18 | sell / filled / Chaikin Money Flow20 > 0.1; 조건 미충족; CMF20=-0.158867, volume20=2.42577e+07; 직전 완료 봉 목표를 다음 봉 시가에 모의 적용 |
| v2 | chaikin_3_10 | 9944.31 | -55.69 | sell / filled / ADL의 EMA3 - EMA10 > 0 그리고 종가 > EMA26; 조건 미충족; Chaikin3_10=-174742, ADL=3.14745e+07, close=772.2, EMA26=770.668; 직전 완료 봉 목표를 다음 봉 시가에 모의 적용 |
| v2 | roc_10_momentum | 10000.00 | 0.00 | 대기 /  / 새 신호 대기 |
| v2 | trix_15_trend | 9914.56 | -85.44 | sell / filled / 15봉 삼중 EMA의 1봉 변화율 TRIX > 0 그리고 종가 > EMA26; 조건 미충족; TRIX15_percent=0.00866315, close=769.855, EMA26=770.806; 직전 완료 봉 목표를 다음 봉 시가에 모의 적용 |
| v2 | keltner_20_breakout | 10000.00 | 0.00 | 대기 /  / 새 신호 대기 |
| v2 | opening_range_30m | 9944.31 | -55.69 | sell / filled / 뉴욕 09:30·09:45 두 완료 봉 최고가를 10:00 이후 종가가 돌파; 자료 부족·변동폭 또는 거래량 없음: 대기; close=772.2; 직전 완료 봉 목표를 다음 봉 시가에 모의 적용 |

### 같은 기간의 비용·노출 비교 (사후 연구)

| 전략 | 비용 전 | 비용 후 | 100% 보유 | 같은 평균 노출 보유 | 평균 노출 |
|---|---:|---:|---:|---:|---:|
| cash | 0.00% | 0.00% | -1.04% | -0.00% | 0.00% |
| buy_hold | -0.63% | -1.04% | -1.04% | -1.04% | 100.00% |
| trend_8_26 | 0.94% | -2.39% | -1.04% | -0.50% | 48.03% |
| momentum_26 | -0.86% | -5.33% | -1.04% | -0.49% | 47.24% |
| breakout_8 | -0.61% | -15.63% | -1.04% | -0.22% | 21.26% |
| reversion_12 | -2.36% | -13.20% | -1.04% | -0.31% | 29.40% |
| volume_26 | -0.94% | -9.69% | -1.04% | -0.09% | 8.92% |
| trend_8_26 AND momentum_26 | 0.47% | -3.26% | -1.04% | -0.43% | 40.94% |
| trend_8_26 + momentum_26 | 0.04% | -3.67% | -1.04% | -0.50% | 47.64% |
| trend_8_26 AND breakout_8 | 0.07% | -10.28% | -1.04% | -0.13% | 12.34% |
| trend_8_26 + breakout_8 | 0.17% | -9.25% | -1.04% | -0.36% | 34.65% |
| trend_8_26 AND reversion_12 | -0.09% | -4.20% | -1.04% | -0.07% | 6.30% |
| trend_8_26 + reversion_12 | -0.72% | -7.77% | -1.04% | -0.40% | 38.72% |
| trend_8_26 AND volume_26 | -0.57% | -4.66% | -1.04% | -0.04% | 4.20% |
| trend_8_26 + volume_26 | -0.00% | -6.11% | -1.04% | -0.30% | 28.48% |
| momentum_26 AND breakout_8 | 0.37% | -10.01% | -1.04% | -0.14% | 13.39% |
| momentum_26 + breakout_8 | -0.73% | -10.63% | -1.04% | -0.36% | 34.26% |
| momentum_26 AND reversion_12 | -0.93% | -5.40% | -1.04% | -0.07% | 6.56% |
| momentum_26 + reversion_12 | -1.61% | -8.59% | -1.04% | -0.40% | 38.33% |
| momentum_26 AND volume_26 | -0.39% | -3.27% | -1.04% | -0.02% | 2.10% |
| momentum_26 + volume_26 | -0.90% | -6.37% | -1.04% | -0.29% | 28.09% |
| breakout_8 AND reversion_12 | 0.00% | 0.00% | -1.04% | -0.00% | 0.00% |
| breakout_8 + reversion_12 | -1.49% | -13.89% | -1.04% | -0.26% | 25.34% |
| breakout_8 AND volume_26 | 0.09% | -1.17% | -1.04% | -0.01% | 1.05% |
| breakout_8 + volume_26 | -0.78% | -11.80% | -1.04% | -0.16% | 15.10% |
| reversion_12 AND volume_26 | -0.81% | -5.29% | -1.04% | -0.05% | 4.46% |
| reversion_12 + volume_26 | -1.65% | -11.09% | -1.04% | -0.20% | 19.17% |
| ema_12_26 | -0.66% | -3.94% | -1.04% | -0.51% | 48.82% |
| macd_12_26_9 | 0.47% | -3.66% | -1.04% | -0.30% | 28.87% |
| rsi_14_recovery | -0.33% | -3.62% | -1.04% | -0.02% | 2.10% |
| bollinger_20_reentry | -1.04% | -7.47% | -1.04% | -0.04% | 4.20% |
| donchian_20 | 0.11% | -6.79% | -1.04% | -0.07% | 6.56% |
| atr_14_breakout | -0.04% | -5.35% | -1.04% | -0.04% | 3.94% |
| session_vwap | 1.18% | -8.91% | -1.04% | -0.53% | 50.39% |
| obv_20 | -0.83% | -9.20% | -1.04% | -0.39% | 37.53% |
| stochastic_14_3_recovery | -1.05% | -15.65% | -1.04% | -0.10% | 9.97% |
| mfi_14_recovery | -0.01% | -2.50% | -1.04% | -0.02% | 1.57% |
| adx_14_trend | -0.10% | -3.81% | -1.04% | -0.29% | 27.82% |
| aroon_25_trend | 0.72% | -2.20% | -1.04% | -0.27% | 26.25% |
| cci_20_momentum | -0.18% | -7.84% | -1.04% | -0.22% | 21.00% |
| williams_14_recovery | -0.94% | -11.18% | -1.04% | -0.07% | 6.82% |
| cmf_20_accumulation | 1.70% | -2.49% | -1.04% | -0.48% | 46.19% |
| chaikin_3_10 | 1.27% | -5.31% | -1.04% | -0.41% | 39.63% |
| roc_10_momentum | -0.06% | -0.48% | -1.04% | -0.01% | 0.79% |
| trix_15_trend | -0.56% | -3.44% | -1.04% | -0.38% | 36.75% |
| keltner_20_breakout | 0.09% | -3.62% | -1.04% | -0.11% | 10.76% |
| opening_range_30m | -0.35% | -6.43% | -1.04% | -0.32% | 30.71% |

동일 구간·초기 자금, 종료 시 청산 비용 포함. 노출 맞춤은 사후 설명용이며 v2 실제 계좌 성과가 아닙니다.
[낙폭 분해·비용 영향·전체 구간](SPY/comparison.json)

[v1 전체 기록](SPY/accounts.json) · [v2 전체 기록](SPY/accounts-v2.json)

## QQQ 계좌

| 모델 | 전략 | 평가액 USD | 손익 USD | 최근 매매·이유 |
|---|---|---:|---:|---|
| v1 | cash | 10000.00 | 0.00 | 대기 /  / 새 신호 대기 |
| v1 | buy_hold | 9842.86 | -157.14 | buy /  / buy_hold: prior completed bar target 100%; next bar open simulation |
| v1 | trend_8_26 | 9922.86 | -77.14 | sell /  / trend_8_26: prior completed bar target 0%; next bar open simulation |
| v1 | momentum_26 | 9935.02 | -64.98 | sell /  / momentum_26: prior completed bar target 0%; next bar open simulation |
| v1 | breakout_8 | 10000.00 | 0.00 | 대기 /  / 새 신호 대기 |
| v1 | reversion_12 | 9863.90 | -136.10 | buy /  / reversion_12: prior completed bar target 100%; next bar open simulation |
| v1 | volume_26 | 9944.75 | -55.25 | sell /  / volume_26: prior completed bar target 0%; next bar open simulation |
| v1 | trend_8_26 AND momentum_26 | 9951.96 | -48.04 | sell /  / trend_8_26 AND momentum_26: prior completed bar target 0%; next bar open simulation |
| v1 | trend_8_26 + momentum_26 | 9928.92 | -71.08 | sell /  / trend_8_26 + momentum_26: prior completed bar target 0%; next bar open simulation |
| v1 | trend_8_26 AND breakout_8 | 10000.00 | 0.00 | 대기 /  / 새 신호 대기 |
| v1 | trend_8_26 + breakout_8 | 9961.32 | -38.68 | sell /  / trend_8_26 + breakout_8: prior completed bar target 0%; next bar open simulation |
| v1 | trend_8_26 AND reversion_12 | 9951.96 | -48.04 | sell /  / trend_8_26 AND reversion_12: prior completed bar target 0%; next bar open simulation |
| v1 | trend_8_26 + reversion_12 | 9893.26 | -106.74 | sell /  / trend_8_26 + reversion_12: prior completed bar target 50%; next bar open simulation |
| v1 | trend_8_26 AND volume_26 | 10000.00 | 0.00 | 대기 /  / 새 신호 대기 |
| v1 | trend_8_26 + volume_26 | 9933.75 | -66.25 | sell /  / trend_8_26 + volume_26: prior completed bar target 0%; next bar open simulation |
| v1 | momentum_26 AND breakout_8 | 10000.00 | 0.00 | 대기 /  / 새 신호 대기 |
| v1 | momentum_26 + breakout_8 | 9967.44 | -32.56 | sell /  / momentum_26 + breakout_8: prior completed bar target 0%; next bar open simulation |
| v1 | momentum_26 AND reversion_12 | 9951.96 | -48.04 | sell /  / momentum_26 AND reversion_12: prior completed bar target 0%; next bar open simulation |
| v1 | momentum_26 + reversion_12 | 9899.35 | -100.65 | sell /  / momentum_26 + reversion_12: prior completed bar target 50%; next bar open simulation |
| v1 | momentum_26 AND volume_26 | 10000.00 | 0.00 | 대기 /  / 새 신호 대기 |
| v1 | momentum_26 + volume_26 | 9939.85 | -60.15 | sell /  / momentum_26 + volume_26: prior completed bar target 0%; next bar open simulation |
| v1 | breakout_8 AND reversion_12 | 10000.00 | 0.00 | 대기 /  / 새 신호 대기 |
| v1 | breakout_8 + reversion_12 | 9931.63 | -68.37 | sell /  / breakout_8 + reversion_12: prior completed bar target 50%; next bar open simulation |
| v1 | breakout_8 AND volume_26 | 10000.00 | 0.00 | 대기 /  / 새 신호 대기 |
| v1 | breakout_8 + volume_26 | 9972.32 | -27.68 | sell /  / breakout_8 + volume_26: prior completed bar target 0%; next bar open simulation |
| v1 | reversion_12 AND volume_26 | 9950.23 | -49.77 | sell /  / reversion_12 AND volume_26: prior completed bar target 0%; next bar open simulation |
| v1 | reversion_12 + volume_26 | 9924.02 | -75.98 | buy /  / reversion_12 + volume_26: prior completed bar target 50%; next bar open simulation |
| v1 | ema_12_26 | 9930.96 | -69.04 | sell /  / EMA12 > EMA26; 조건 미충족; EMA12=725.847, EMA26=725.955 |
| v1 | macd_12_26_9 | 9930.96 | -69.04 | sell /  / MACD > 신호선 그리고 MACD > 0; 조건 미충족; MACD=-0.108239, signal9=-0.536871 |
| v1 | rsi_14_recovery | 10000.00 | 0.00 | 대기 /  / 새 신호 대기 |
| v1 | bollinger_20_reentry | 9882.24 | -117.76 | sell /  / 직전 종가 < 직전 하단밴드, 현재 하단밴드 <= 종가 <= SMA20 (한 봉 목표); 조건 미충족; close=716.64, lower20=715.793, SMA20=723.132, previous_lower20=716.805 |
| v1 | donchian_20 | 10000.00 | 0.00 | 대기 /  / 새 신호 대기 |
| v1 | atr_14_breakout | 10000.00 | 0.00 | 대기 /  / 새 신호 대기 |
| v1 | session_vwap | 9874.48 | -125.52 | sell /  / 종가 > 뉴욕 거래일별 누적 전형가격 VWAP; 조건 미충족; close=721.534, session_VWAP=721.817, session_volume=9.25052e+07 |
| v1 | obv_20 | 9930.96 | -69.04 | sell /  / OBV > OBV의 SMA20 그리고 종가 > EMA26; 조건 미충족; OBV=7.37006e+07, OBV_SMA20=7.17868e+07, close=723.36, EMA26=725.955 |
| v1 | stochastic_14_3_recovery | 9781.43 | -218.57 | sell /  / 직전 %K14 < 20에서 %K14가 %D3 상향 돌파 (한 봉 목표); 조건 미충족; K14=10.9793, D3=9.03051, previous_K14=13.8351, previous_D3=9.82277 |
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
| v2 | buy_hold | 9524.70 | -475.30 | buy / partial / 직전 완료 봉 목표 비중 100%; 다음 봉 시가 가정 |
| v2 | trend_8_26 | 9726.12 | -273.88 | sell / filled / 직전 완료 봉 목표 비중 0%; 다음 봉 시가 가정 |
| v2 | momentum_26 | 9831.49 | -168.51 | sell / filled / 직전 완료 봉 목표 비중 0%; 다음 봉 시가 가정 |
| v2 | breakout_8 | 9669.86 | -330.14 | sell / filled / 직전 완료 봉 목표 비중 0%; 다음 봉 시가 가정 |
| v2 | reversion_12 | 9381.63 | -618.37 | buy / partial / 직전 완료 봉 목표 비중 100%; 다음 봉 시가 가정 |
| v2 | volume_26 | 9565.80 | -434.20 | 중단: 손실 한도 / sell / filled / 직전 완료 봉 목표 비중 0%; 다음 봉 시가 가정 |
| v2 | trend_8_26 AND momentum_26 | 9848.25 | -151.75 | sell / filled / 직전 완료 봉 목표 비중 0%; 다음 봉 시가 가정 |
| v2 | trend_8_26 + momentum_26 | 9778.69 | -221.31 | sell / filled / 직전 완료 봉 목표 비중 0%; 다음 봉 시가 가정 |
| v2 | trend_8_26 AND breakout_8 | 9895.83 | -104.17 | sell / filled / 직전 완료 봉 목표 비중 0%; 다음 봉 시가 가정 |
| v2 | trend_8_26 + breakout_8 | 9697.89 | -302.11 | sell / filled / 직전 완료 봉 목표 비중 0%; 다음 봉 시가 가정 |
| v2 | trend_8_26 AND reversion_12 | 9811.80 | -188.20 | sell / filled / 직전 완료 봉 목표 비중 0%; 다음 봉 시가 가정 |
| v2 | trend_8_26 + reversion_12 | 9551.96 | -448.04 | sell / filled / 직전 완료 봉 목표 비중 50%; 다음 봉 시가 가정 |
| v2 | trend_8_26 AND volume_26 | 9840.10 | -159.90 | sell / filled / 직전 완료 봉 목표 비중 0%; 다음 봉 시가 가정 |
| v2 | trend_8_26 + volume_26 | 9537.59 | -462.41 | sell / filled / 직전 완료 봉 목표 비중 0%; 다음 봉 시가 가정 |
| v2 | momentum_26 AND breakout_8 | 9960.69 | -39.31 | sell / filled / 직전 완료 봉 목표 비중 0%; 다음 봉 시가 가정 |
| v2 | momentum_26 + breakout_8 | 9750.28 | -249.72 | sell / filled / 직전 완료 봉 목표 비중 0%; 다음 봉 시가 가정 |
| v2 | momentum_26 AND reversion_12 | 9949.97 | -50.03 | sell / filled / 직전 완료 봉 목표 비중 0%; 다음 봉 시가 가정 |
| v2 | momentum_26 + reversion_12 | 9623.74 | -376.26 | sell / filled / 직전 완료 봉 목표 비중 50%; 다음 봉 시가 가정 |
| v2 | momentum_26 AND volume_26 | 9936.83 | -63.17 | sell / filled / 직전 완료 봉 목표 비중 0%; 다음 봉 시가 가정 |
| v2 | momentum_26 + volume_26 | 9589.12 | -410.88 | sell / filled / 직전 완료 봉 목표 비중 0%; 다음 봉 시가 가정 |
| v2 | breakout_8 AND reversion_12 | 10000.00 | 0.00 | 대기 /  / 새 신호 대기 |
| v2 | breakout_8 + reversion_12 | 9584.47 | -415.53 | sell / filled / 직전 완료 봉 목표 비중 50%; 다음 봉 시가 가정 |
| v2 | breakout_8 AND volume_26 | 9947.98 | -52.02 | sell / filled / 직전 완료 봉 목표 비중 0%; 다음 봉 시가 가정 |
| v2 | breakout_8 + volume_26 | 9550.09 | -449.91 | sell / filled / 직전 완료 봉 목표 비중 0%; 다음 봉 시가 가정 |
| v2 | reversion_12 AND volume_26 | 9547.64 | -452.36 | 중단: 손실 한도 / sell / filled / 직전 완료 봉 목표 비중 0%; 다음 봉 시가 가정 |
| v2 | reversion_12 + volume_26 | 9406.75 | -593.25 | buy / filled / 직전 완료 봉 목표 비중 50%; 다음 봉 시가 가정 |
| v2 | ema_12_26 | 9928.97 | -71.03 | sell / filled / EMA12 > EMA26; 조건 미충족; EMA12=725.847, EMA26=725.955; 직전 완료 봉 목표를 다음 봉 시가에 모의 적용 |
| v2 | macd_12_26_9 | 9928.97 | -71.03 | sell / filled / MACD > 신호선 그리고 MACD > 0; 조건 미충족; MACD=-0.108239, signal9=-0.536871; 직전 완료 봉 목표를 다음 봉 시가에 모의 적용 |
| v2 | rsi_14_recovery | 10000.00 | 0.00 | 대기 /  / 새 신호 대기 |
| v2 | bollinger_20_reentry | 9878.29 | -121.71 | sell / filled / 직전 종가 < 직전 하단밴드, 현재 하단밴드 <= 종가 <= SMA20 (한 봉 목표); 조건 미충족; close=716.64, lower20=715.793, SMA20=723.132, previous_lower20=716.805; 직전 완료 봉 목표를 다음 봉 시가에 모의 적용 |
| v2 | donchian_20 | 10000.00 | 0.00 | 대기 /  / 새 신호 대기 |
| v2 | atr_14_breakout | 10000.00 | 0.00 | 대기 /  / 새 신호 대기 |
| v2 | session_vwap | 9870.53 | -129.47 | sell / filled / 종가 > 뉴욕 거래일별 누적 전형가격 VWAP; 조건 미충족; close=721.534, session_VWAP=721.817, session_volume=9.25052e+07; 직전 완료 봉 목표를 다음 봉 시가에 모의 적용 |
| v2 | obv_20 | 9928.97 | -71.03 | sell / filled / OBV > OBV의 SMA20 그리고 종가 > EMA26; 조건 미충족; OBV=7.37006e+07, OBV_SMA20=7.17868e+07, close=723.36, EMA26=725.955; 직전 완료 봉 목표를 다음 봉 시가에 모의 적용 |
| v2 | stochastic_14_3_recovery | 9773.61 | -226.39 | sell / filled / 직전 %K14 < 20에서 %K14가 %D3 상향 돌파 (한 봉 목표); 조건 미충족; K14=10.9793, D3=9.03051, previous_K14=13.8351, previous_D3=9.82277; 직전 완료 봉 목표를 다음 봉 시가에 모의 적용 |
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
| cash | 0.00% | 0.00% | -4.32% | -0.00% | 0.00% |
| buy_hold | -3.92% | -4.32% | -4.32% | -4.32% | 100.00% |
| trend_8_26 | -0.39% | -4.09% | -4.32% | -1.94% | 44.88% |
| momentum_26 | -1.66% | -6.49% | -4.32% | -1.67% | 38.58% |
| breakout_8 | -1.46% | -16.35% | -4.32% | -0.76% | 17.59% |
| reversion_12 | -1.31% | -14.08% | -4.32% | -1.25% | 28.87% |
| volume_26 | -1.23% | -14.01% | -4.32% | -0.65% | 14.96% |
| trend_8_26 AND momentum_26 | -0.53% | -4.62% | -4.32% | -1.47% | 33.86% |
| trend_8_26 + momentum_26 | -1.02% | -5.10% | -4.32% | -1.81% | 41.73% |
| trend_8_26 AND breakout_8 | -0.32% | -9.11% | -4.32% | -0.45% | 10.50% |
| trend_8_26 + breakout_8 | -0.92% | -10.05% | -4.32% | -1.35% | 31.24% |
| trend_8_26 AND reversion_12 | 0.25% | -5.48% | -4.32% | -0.30% | 6.82% |
| trend_8_26 + reversion_12 | -0.84% | -8.66% | -4.32% | -1.60% | 36.88% |
| trend_8_26 AND volume_26 | -0.71% | -5.59% | -4.32% | -0.18% | 4.20% |
| trend_8_26 + volume_26 | -0.80% | -9.00% | -4.32% | -1.30% | 29.93% |
| momentum_26 AND breakout_8 | -0.13% | -8.56% | -4.32% | -0.44% | 10.24% |
| momentum_26 + breakout_8 | -1.56% | -11.37% | -4.32% | -1.22% | 28.09% |
| momentum_26 AND reversion_12 | -0.19% | -5.89% | -4.32% | -0.24% | 5.51% |
| momentum_26 + reversion_12 | -1.48% | -9.81% | -4.32% | -1.46% | 33.73% |
| momentum_26 AND volume_26 | -0.30% | -4.40% | -4.32% | -0.15% | 3.41% |
| momentum_26 + volume_26 | -1.44% | -10.15% | -4.32% | -1.16% | 26.78% |
| breakout_8 AND reversion_12 | 0.00% | 0.00% | -4.32% | -0.00% | 0.00% |
| breakout_8 + reversion_12 | -1.38% | -14.34% | -4.32% | -1.01% | 23.24% |
| breakout_8 AND volume_26 | 0.04% | -2.04% | -4.32% | -0.06% | 1.31% |
| breakout_8 + volume_26 | -1.34% | -13.94% | -4.32% | -0.71% | 16.28% |
| reversion_12 AND volume_26 | -1.34% | -8.91% | -4.32% | -0.40% | 9.19% |
| reversion_12 + volume_26 | -1.27% | -13.51% | -4.32% | -0.95% | 21.92% |
| ema_12_26 | 0.14% | -1.94% | -4.32% | -1.57% | 36.22% |
| macd_12_26_9 | 1.49% | -1.86% | -4.32% | -0.88% | 20.21% |
| rsi_14_recovery | -0.50% | -4.99% | -4.32% | -0.13% | 2.89% |
| bollinger_20_reentry | -0.40% | -6.48% | -4.32% | -0.17% | 3.94% |
| donchian_20 | 0.28% | -4.24% | -4.32% | -0.20% | 4.72% |
| atr_14_breakout | -0.26% | -4.76% | -4.32% | -0.14% | 3.15% |
| session_vwap | -1.33% | -12.65% | -4.32% | -2.23% | 51.44% |
| obv_20 | -1.88% | -10.91% | -4.32% | -1.17% | 27.03% |
| stochastic_14_3_recovery | -0.50% | -11.91% | -4.32% | -0.33% | 7.61% |
| mfi_14_recovery | -0.16% | -1.82% | -4.32% | -0.05% | 1.05% |
| adx_14_trend | -0.71% | -3.59% | -4.32% | -0.81% | 18.64% |
| aroon_25_trend | 1.40% | -1.95% | -4.32% | -0.85% | 19.69% |
| cci_20_momentum | -0.85% | -5.72% | -4.32% | -0.65% | 14.96% |
| williams_14_recovery | -0.68% | -10.95% | -4.32% | -0.30% | 6.82% |
| cmf_20_accumulation | -2.11% | -9.99% | -4.32% | -1.39% | 32.02% |
| chaikin_3_10 | -3.06% | -11.25% | -4.32% | -1.49% | 34.38% |
| roc_10_momentum | -0.31% | -1.56% | -4.32% | -0.09% | 2.10% |
| trix_15_trend | 0.02% | -1.65% | -4.32% | -1.31% | 30.18% |
| keltner_20_breakout | -0.73% | -4.81% | -4.32% | -0.32% | 7.35% |
| opening_range_30m | -0.35% | -6.04% | -4.32% | -0.94% | 21.78% |

동일 구간·초기 자금, 종료 시 청산 비용 포함. 노출 맞춤은 사후 설명용이며 v2 실제 계좌 성과가 아닙니다.
[낙폭 분해·비용 영향·전체 구간](QQQ/comparison.json)

[v1 전체 기록](QQQ/accounts.json) · [v2 전체 기록](QQQ/accounts-v2.json)

## IWM 계좌

| 모델 | 전략 | 평가액 USD | 손익 USD | 최근 매매·이유 |
|---|---|---:|---:|---|
| v1 | cash | 10000.00 | 0.00 | 대기 /  / 새 신호 대기 |
| v1 | buy_hold | 9830.07 | -169.93 | buy /  / buy_hold: prior completed bar target 100%; next bar open simulation |
| v1 | trend_8_26 | 9838.25 | -161.75 | sell /  / trend_8_26: prior completed bar target 0%; next bar open simulation |
| v1 | momentum_26 | 9895.73 | -104.27 | sell /  / momentum_26: prior completed bar target 0%; next bar open simulation |
| v1 | breakout_8 | 9929.38 | -70.62 | sell /  / breakout_8: prior completed bar target 0%; next bar open simulation |
| v1 | reversion_12 | 9893.99 | -106.01 | buy /  / reversion_12: prior completed bar target 100%; next bar open simulation |
| v1 | volume_26 | 9935.98 | -64.02 | sell /  / volume_26: prior completed bar target 0%; next bar open simulation |
| v1 | trend_8_26 AND momentum_26 | 9895.73 | -104.27 | sell /  / trend_8_26 AND momentum_26: prior completed bar target 0%; next bar open simulation |
| v1 | trend_8_26 + momentum_26 | 9866.97 | -133.03 | sell /  / trend_8_26 + momentum_26: prior completed bar target 0%; next bar open simulation |
| v1 | trend_8_26 AND breakout_8 | 9929.38 | -70.62 | sell /  / trend_8_26 AND breakout_8: prior completed bar target 0%; next bar open simulation |
| v1 | trend_8_26 + breakout_8 | 9883.72 | -116.28 | sell /  / trend_8_26 + breakout_8: prior completed bar target 0%; next bar open simulation |
| v1 | trend_8_26 AND reversion_12 | 9902.23 | -97.77 | sell /  / trend_8_26 AND reversion_12: prior completed bar target 0%; next bar open simulation |
| v1 | trend_8_26 + reversion_12 | 9866.04 | -133.96 | buy /  / trend_8_26 + reversion_12: prior completed bar target 50%; next bar open simulation |
| v1 | trend_8_26 AND volume_26 | 9935.98 | -64.02 | sell /  / trend_8_26 AND volume_26: prior completed bar target 0%; next bar open simulation |
| v1 | trend_8_26 + volume_26 | 9886.95 | -113.05 | sell /  / trend_8_26 + volume_26: prior completed bar target 0%; next bar open simulation |
| v1 | momentum_26 AND breakout_8 | 9929.38 | -70.62 | sell /  / momentum_26 AND breakout_8: prior completed bar target 0%; next bar open simulation |
| v1 | momentum_26 + breakout_8 | 9912.56 | -87.44 | sell /  / momentum_26 + breakout_8: prior completed bar target 0%; next bar open simulation |
| v1 | momentum_26 AND reversion_12 | 10000.00 | 0.00 | 대기 /  / 새 신호 대기 |
| v1 | momentum_26 + reversion_12 | 9914.61 | -85.39 | buy /  / momentum_26 + reversion_12: prior completed bar target 50%; next bar open simulation |
| v1 | momentum_26 AND volume_26 | 10000.00 | 0.00 | 대기 /  / 새 신호 대기 |
| v1 | momentum_26 + volume_26 | 9915.81 | -84.19 | sell /  / momentum_26 + volume_26: prior completed bar target 0%; next bar open simulation |
| v1 | breakout_8 AND reversion_12 | 10000.00 | 0.00 | 대기 /  / 새 신호 대기 |
| v1 | breakout_8 + reversion_12 | 9911.62 | -88.38 | buy /  / breakout_8 + reversion_12: prior completed bar target 50%; next bar open simulation |
| v1 | breakout_8 AND volume_26 | 10000.00 | 0.00 | 대기 /  / 새 신호 대기 |
| v1 | breakout_8 + volume_26 | 9932.66 | -67.34 | sell /  / breakout_8 + volume_26: prior completed bar target 0%; next bar open simulation |
| v1 | reversion_12 AND volume_26 | 9935.98 | -64.02 | sell /  / reversion_12 AND volume_26: prior completed bar target 0%; next bar open simulation |
| v1 | reversion_12 + volume_26 | 9914.93 | -85.07 | buy /  / reversion_12 + volume_26: prior completed bar target 50%; next bar open simulation |
| v1 | ema_12_26 | 9838.25 | -161.75 | sell /  / EMA12 > EMA26; 조건 미충족; EMA12=273.669, EMA26=273.722 |
| v1 | macd_12_26_9 | 9916.70 | -83.30 | sell /  / MACD > 신호선 그리고 MACD > 0; 조건 미충족; MACD=0.425881, signal9=0.461272 |
| v1 | rsi_14_recovery | 10000.00 | 0.00 | 대기 /  / 새 신호 대기 |
| v1 | bollinger_20_reentry | 9947.64 | -52.36 | sell /  / 직전 종가 < 직전 하단밴드, 현재 하단밴드 <= 종가 <= SMA20 (한 봉 목표); 조건 미충족; close=271.86, lower20=271.804, SMA20=273.875, previous_lower20=272.119 |
| v1 | donchian_20 | 9929.38 | -70.62 | sell /  / 종가 > 현재 봉을 제외한 직전 20봉 최고가; 조건 미충족; close=274.88, prior_high20=275.91 |
| v1 | atr_14_breakout | 9929.38 | -70.62 | sell /  / 종가 > 직전 종가 + 직전 ATR14 그리고 종가 > EMA26; 조건 미충족; close=274.88, threshold=276.257, prior_ATR14=0.526844, EMA26=273.855 |
| v1 | session_vwap | 9937.31 | -62.69 | sell /  / 종가 > 뉴욕 거래일별 누적 전형가격 VWAP; 조건 미충족; close=274.88, session_VWAP=275.422, session_volume=2.52313e+06 |
| v1 | obv_20 | 9928.63 | -71.37 | sell /  / OBV > OBV의 SMA20 그리고 종가 > EMA26; 조건 미충족; OBV=-4.10489e+07, OBV_SMA20=-4.0926e+07, close=274.64, EMA26=273.913 |
| v1 | stochastic_14_3_recovery | 9947.64 | -52.36 | sell /  / 직전 %K14 < 20에서 %K14가 %D3 상향 돌파 (한 봉 목표); 조건 미충족; K14=1.21921, D3=3.49587, previous_K14=9.2684, previous_D3=3.30205 |
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
| v2 | buy_hold | 9724.96 | -275.04 | buy / partial / 직전 완료 봉 목표 비중 100%; 다음 봉 시가 가정 |
| v2 | trend_8_26 | 9709.80 | -290.20 | sell / filled / 직전 완료 봉 목표 비중 0%; 다음 봉 시가 가정 |
| v2 | momentum_26 | 9767.53 | -232.47 | sell / filled / 직전 완료 봉 목표 비중 0%; 다음 봉 시가 가정 |
| v2 | breakout_8 | 9547.89 | -452.11 | sell / filled / 직전 완료 봉 목표 비중 0%; 다음 봉 시가 가정 |
| v2 | reversion_12 | 9436.61 | -563.39 | buy / partial / 직전 완료 봉 목표 비중 100%; 다음 봉 시가 가정 |
| v2 | volume_26 | 9450.57 | -549.43 | sell / filled / 직전 완료 봉 목표 비중 0%; 다음 봉 시가 가정 |
| v2 | trend_8_26 AND momentum_26 | 9918.12 | -81.88 | sell / filled / 직전 완료 봉 목표 비중 0%; 다음 봉 시가 가정 |
| v2 | trend_8_26 + momentum_26 | 9759.25 | -240.75 | sell / filled / 직전 완료 봉 목표 비중 0%; 다음 봉 시가 가정 |
| v2 | trend_8_26 AND breakout_8 | 9840.76 | -159.24 | sell / filled / 직전 완료 봉 목표 비중 0%; 다음 봉 시가 가정 |
| v2 | trend_8_26 + breakout_8 | 9648.89 | -351.11 | sell / filled / 직전 완료 봉 목표 비중 0%; 다음 봉 시가 가정 |
| v2 | trend_8_26 AND reversion_12 | 9783.25 | -216.75 | sell / filled / 직전 완료 봉 목표 비중 0%; 다음 봉 시가 가정 |
| v2 | trend_8_26 + reversion_12 | 9572.03 | -427.97 | buy / filled / 직전 완료 봉 목표 비중 50%; 다음 봉 시가 가정 |
| v2 | trend_8_26 AND volume_26 | 9797.73 | -202.27 | sell / filled / 직전 완료 봉 목표 비중 0%; 다음 봉 시가 가정 |
| v2 | trend_8_26 + volume_26 | 9599.39 | -400.61 | sell / filled / 직전 완료 봉 목표 비중 0%; 다음 봉 시가 가정 |
| v2 | momentum_26 AND breakout_8 | 9733.71 | -266.29 | sell / filled / 직전 완료 봉 목표 비중 0%; 다음 봉 시가 가정 |
| v2 | momentum_26 + breakout_8 | 9657.13 | -342.87 | sell / filled / 직전 완료 봉 목표 비중 0%; 다음 봉 시가 가정 |
| v2 | momentum_26 AND reversion_12 | 9960.59 | -39.41 | sell / filled / 직전 완료 봉 목표 비중 0%; 다음 봉 시가 가정 |
| v2 | momentum_26 + reversion_12 | 9640.61 | -359.39 | buy / filled / 직전 완료 봉 목표 비중 50%; 다음 봉 시가 가정 |
| v2 | momentum_26 AND volume_26 | 9897.79 | -102.21 | sell / filled / 직전 완료 봉 목표 비중 0%; 다음 봉 시가 가정 |
| v2 | momentum_26 + volume_26 | 9607.50 | -392.50 | sell / filled / 직전 완료 봉 목표 비중 0%; 다음 봉 시가 가정 |
| v2 | breakout_8 AND reversion_12 | 10000.00 | 0.00 | 대기 /  / 새 신호 대기 |
| v2 | breakout_8 + reversion_12 | 9531.60 | -468.40 | buy / filled / 직전 완료 봉 목표 비중 50%; 다음 봉 시가 가정 |
| v2 | breakout_8 AND volume_26 | 9746.03 | -253.97 | sell / filled / 직전 완료 봉 목표 비중 0%; 다음 봉 시가 가정 |
| v2 | breakout_8 + volume_26 | 9519.00 | -481.00 | sell / filled / 직전 완료 봉 목표 비중 0%; 다음 봉 시가 가정 |
| v2 | reversion_12 AND volume_26 | 9676.46 | -323.54 | sell / filled / 직전 완료 봉 목표 비중 0%; 다음 봉 시가 가정 |
| v2 | reversion_12 + volume_26 | 9463.19 | -536.81 | buy / filled / 직전 완료 봉 목표 비중 50%; 다음 봉 시가 가정 |
| v2 | ema_12_26 | 9836.29 | -163.71 | sell / filled / EMA12 > EMA26; 조건 미충족; EMA12=273.669, EMA26=273.722; 직전 완료 봉 목표를 다음 봉 시가에 모의 적용 |
| v2 | macd_12_26_9 | 9914.72 | -85.28 | sell / filled / MACD > 신호선 그리고 MACD > 0; 조건 미충족; MACD=0.425881, signal9=0.461272; 직전 완료 봉 목표를 다음 봉 시가에 모의 적용 |
| v2 | rsi_14_recovery | 10000.00 | 0.00 | 대기 /  / 새 신호 대기 |
| v2 | bollinger_20_reentry | 9945.65 | -54.35 | sell / filled / 직전 종가 < 직전 하단밴드, 현재 하단밴드 <= 종가 <= SMA20 (한 봉 목표); 조건 미충족; close=271.86, lower20=271.804, SMA20=273.875, previous_lower20=272.119; 직전 완료 봉 목표를 다음 봉 시가에 모의 적용 |
| v2 | donchian_20 | 9927.39 | -72.61 | sell / filled / 종가 > 현재 봉을 제외한 직전 20봉 최고가; 조건 미충족; close=274.88, prior_high20=275.91; 직전 완료 봉 목표를 다음 봉 시가에 모의 적용 |
| v2 | atr_14_breakout | 9927.39 | -72.61 | sell / filled / 종가 > 직전 종가 + 직전 ATR14 그리고 종가 > EMA26; 조건 미충족; close=274.88, threshold=276.257, prior_ATR14=0.526844, EMA26=273.855; 직전 완료 봉 목표를 다음 봉 시가에 모의 적용 |
| v2 | session_vwap | 9935.32 | -64.68 | sell / filled / 종가 > 뉴욕 거래일별 누적 전형가격 VWAP; 조건 미충족; close=274.88, session_VWAP=275.422, session_volume=2.52313e+06; 직전 완료 봉 목표를 다음 봉 시가에 모의 적용 |
| v2 | obv_20 | 9926.64 | -73.36 | sell / filled / OBV > OBV의 SMA20 그리고 종가 > EMA26; 조건 미충족; OBV=-4.10489e+07, OBV_SMA20=-4.0926e+07, close=274.64, EMA26=273.913; 직전 완료 봉 목표를 다음 봉 시가에 모의 적용 |
| v2 | stochastic_14_3_recovery | 9945.65 | -54.35 | sell / filled / 직전 %K14 < 20에서 %K14가 %D3 상향 돌파 (한 봉 목표); 조건 미충족; K14=1.21921, D3=3.49587, previous_K14=9.2684, previous_D3=3.30205; 직전 완료 봉 목표를 다음 봉 시가에 모의 적용 |
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
| cash | 0.00% | 0.00% | -4.33% | -0.00% | 0.00% |
| buy_hold | -3.93% | -4.33% | -4.33% | -4.33% | 100.00% |
| trend_8_26 | -2.32% | -5.94% | -4.33% | -1.94% | 44.36% |
| momentum_26 | -3.11% | -8.64% | -4.33% | -1.69% | 38.58% |
| breakout_8 | -1.07% | -14.24% | -4.33% | -0.84% | 19.16% |
| reversion_12 | -3.02% | -15.57% | -4.33% | -1.36% | 30.97% |
| volume_26 | -2.55% | -9.65% | -4.33% | -0.38% | 8.66% |
| trend_8_26 AND momentum_26 | -1.99% | -6.02% | -4.33% | -1.47% | 33.60% |
| trend_8_26 + momentum_26 | -2.71% | -6.91% | -4.33% | -1.82% | 41.47% |
| trend_8_26 AND breakout_8 | -0.58% | -8.20% | -4.33% | -0.49% | 11.02% |
| trend_8_26 + breakout_8 | -1.69% | -10.00% | -4.33% | -1.39% | 31.76% |
| trend_8_26 AND reversion_12 | -0.73% | -5.61% | -4.33% | -0.27% | 6.04% |
| trend_8_26 + reversion_12 | -2.66% | -10.71% | -4.33% | -1.65% | 37.67% |
| trend_8_26 AND volume_26 | -1.26% | -4.93% | -4.33% | -0.16% | 3.67% |
| trend_8_26 + volume_26 | -2.43% | -7.62% | -4.33% | -1.16% | 26.51% |
| momentum_26 AND breakout_8 | -0.34% | -7.98% | -4.33% | -0.46% | 10.50% |
| momentum_26 + breakout_8 | -2.09% | -11.48% | -4.33% | -1.27% | 28.88% |
| momentum_26 AND reversion_12 | -0.08% | -3.38% | -4.33% | -0.12% | 2.62% |
| momentum_26 + reversion_12 | -3.06% | -10.88% | -4.33% | -1.52% | 34.78% |
| momentum_26 AND volume_26 | -1.32% | -3.77% | -4.33% | -0.08% | 1.84% |
| momentum_26 + volume_26 | -2.82% | -8.77% | -4.33% | -1.04% | 23.63% |
| breakout_8 AND reversion_12 | 0.00% | 0.00% | -4.33% | -0.00% | 0.00% |
| breakout_8 + reversion_12 | -2.05% | -14.20% | -4.33% | -1.10% | 25.07% |
| breakout_8 AND volume_26 | -1.30% | -3.76% | -4.33% | -0.09% | 2.10% |
| breakout_8 + volume_26 | -1.81% | -11.79% | -4.33% | -0.61% | 13.92% |
| reversion_12 AND volume_26 | -0.62% | -5.10% | -4.33% | -0.21% | 4.72% |
| reversion_12 + volume_26 | -2.78% | -12.11% | -4.33% | -0.87% | 19.82% |
| ema_12_26 | -0.72% | -3.19% | -4.33% | -1.88% | 43.04% |
| macd_12_26_9 | 1.76% | -0.78% | -4.33% | -1.19% | 27.03% |
| rsi_14_recovery | -0.28% | -4.78% | -4.33% | -0.13% | 2.89% |
| bollinger_20_reentry | -0.37% | -5.27% | -4.33% | -0.14% | 3.15% |
| donchian_20 | -0.20% | -5.10% | -4.33% | -0.24% | 5.51% |
| atr_14_breakout | -1.87% | -8.25% | -4.33% | -0.19% | 4.20% |
| session_vwap | -1.69% | -11.49% | -4.33% | -1.87% | 42.78% |
| obv_20 | -0.44% | -4.93% | -4.33% | -1.63% | 37.27% |
| stochastic_14_3_recovery | -0.99% | -13.81% | -4.33% | -0.38% | 8.66% |
| mfi_14_recovery | 0.22% | -3.50% | -4.33% | -0.10% | 2.36% |
| adx_14_trend | -0.58% | -4.27% | -4.33% | -1.38% | 31.50% |
| aroon_25_trend | -1.70% | -4.95% | -4.33% | -0.90% | 20.47% |
| cci_20_momentum | -1.95% | -7.93% | -4.33% | -0.76% | 17.32% |
| williams_14_recovery | -0.74% | -10.26% | -4.33% | -0.28% | 6.30% |
| cmf_20_accumulation | -2.50% | -8.83% | -4.33% | -0.81% | 18.37% |
| chaikin_3_10 | -3.15% | -9.83% | -4.33% | -1.40% | 32.02% |
| roc_10_momentum | -0.63% | -1.87% | -4.33% | -0.14% | 3.15% |
| trix_15_trend | -0.42% | -3.71% | -4.33% | -1.40% | 32.02% |
| keltner_20_breakout | -0.91% | -4.18% | -4.33% | -0.23% | 5.25% |
| opening_range_30m | 1.50% | -3.49% | -4.33% | -1.06% | 24.15% |

동일 구간·초기 자금, 종료 시 청산 비용 포함. 노출 맞춤은 사후 설명용이며 v2 실제 계좌 성과가 아닙니다.
[낙폭 분해·비용 영향·전체 구간](IWM/comparison.json)

[v1 전체 기록](IWM/accounts.json) · [v2 전체 기록](IWM/accounts-v2.json)

## DIA 계좌

| 모델 | 전략 | 평가액 USD | 손익 USD | 최근 매매·이유 |
|---|---|---:|---:|---|
| v1 | cash | 10000.00 | 0.00 | 대기 /  / 새 신호 대기 |
| v1 | buy_hold | 9923.91 | -76.09 | buy /  / buy_hold: prior completed bar target 100%; next bar open simulation |
| v1 | trend_8_26 | 9923.91 | -76.09 | buy /  / trend_8_26: prior completed bar target 100%; next bar open simulation |
| v1 | momentum_26 | 9909.03 | -90.97 | sell /  / momentum_26: prior completed bar target 0%; next bar open simulation |
| v1 | breakout_8 | 9940.12 | -59.88 | sell /  / breakout_8: prior completed bar target 0%; next bar open simulation |
| v1 | reversion_12 | 9955.71 | -44.29 | buy /  / reversion_12: prior completed bar target 100%; next bar open simulation |
| v1 | volume_26 | 9943.10 | -56.90 | sell /  / volume_26: prior completed bar target 0%; next bar open simulation |
| v1 | trend_8_26 AND momentum_26 | 9909.03 | -90.97 | sell /  / trend_8_26 AND momentum_26: prior completed bar target 0%; next bar open simulation |
| v1 | trend_8_26 + momentum_26 | 9916.47 | -83.53 | sell /  / trend_8_26 + momentum_26: prior completed bar target 50%; next bar open simulation |
| v1 | trend_8_26 AND breakout_8 | 9940.12 | -59.88 | sell /  / trend_8_26 AND breakout_8: prior completed bar target 0%; next bar open simulation |
| v1 | trend_8_26 + breakout_8 | 9932.01 | -67.99 | buy /  / trend_8_26 + breakout_8: prior completed bar target 50%; next bar open simulation |
| v1 | trend_8_26 AND reversion_12 | 9955.71 | -44.29 | buy /  / trend_8_26 AND reversion_12: prior completed bar target 100%; next bar open simulation |
| v1 | trend_8_26 + reversion_12 | 9939.75 | -60.25 | buy /  / trend_8_26 + reversion_12: prior completed bar target 100%; next bar open simulation |
| v1 | trend_8_26 AND volume_26 | 9943.10 | -56.90 | sell /  / trend_8_26 AND volume_26: prior completed bar target 0%; next bar open simulation |
| v1 | trend_8_26 + volume_26 | 9933.45 | -66.55 | buy /  / trend_8_26 + volume_26: prior completed bar target 50%; next bar open simulation |
| v1 | momentum_26 AND breakout_8 | 9940.12 | -59.88 | sell /  / momentum_26 AND breakout_8: prior completed bar target 0%; next bar open simulation |
| v1 | momentum_26 + breakout_8 | 9924.57 | -75.43 | sell /  / momentum_26 + breakout_8: prior completed bar target 0%; next bar open simulation |
| v1 | momentum_26 AND reversion_12 | 9940.78 | -59.22 | sell /  / momentum_26 AND reversion_12: prior completed bar target 0%; next bar open simulation |
| v1 | momentum_26 + reversion_12 | 9932.30 | -67.70 | sell /  / momentum_26 + reversion_12: prior completed bar target 50%; next bar open simulation |
| v1 | momentum_26 AND volume_26 | 9943.10 | -56.90 | sell /  / momentum_26 AND volume_26: prior completed bar target 0%; next bar open simulation |
| v1 | momentum_26 + volume_26 | 9926.01 | -73.99 | sell /  / momentum_26 + volume_26: prior completed bar target 0%; next bar open simulation |
| v1 | breakout_8 AND reversion_12 | 10000.00 | 0.00 | 대기 /  / 새 신호 대기 |
| v1 | breakout_8 + reversion_12 | 9947.89 | -52.11 | buy /  / breakout_8 + reversion_12: prior completed bar target 50%; next bar open simulation |
| v1 | breakout_8 AND volume_26 | 10000.00 | 0.00 | 대기 /  / 새 신호 대기 |
| v1 | breakout_8 + volume_26 | 9941.60 | -58.40 | sell /  / breakout_8 + volume_26: prior completed bar target 0%; next bar open simulation |
| v1 | reversion_12 AND volume_26 | 10000.00 | 0.00 | 대기 /  / 새 신호 대기 |
| v1 | reversion_12 + volume_26 | 9969.29 | -30.71 | buy /  / reversion_12 + volume_26: prior completed bar target 50%; next bar open simulation |
| v1 | ema_12_26 | 9923.91 | -76.09 | buy /  / EMA12 > EMA26; 조건 충족; EMA12=520.818, EMA26=519.784 |
| v1 | macd_12_26_9 | 9941.64 | -58.36 | sell /  / MACD > 신호선 그리고 MACD > 0; 조건 미충족; MACD=1.23542, signal9=1.25143 |
| v1 | rsi_14_recovery | 10000.00 | 0.00 | 대기 /  / 새 신호 대기 |
| v1 | bollinger_20_reentry | 10000.00 | 0.00 | 대기 /  / 새 신호 대기 |
| v1 | donchian_20 | 9940.12 | -59.88 | sell /  / 종가 > 현재 봉을 제외한 직전 20봉 최고가; 조건 미충족; close=522.89, prior_high20=525.09 |
| v1 | atr_14_breakout | 9972.44 | -27.56 | sell /  / 종가 > 직전 종가 + 직전 ATR14 그리고 종가 > EMA26; 조건 미충족; close=524.65, threshold=524.777, prior_ATR14=0.84688, EMA26=520.429 |
| v1 | session_vwap | 9960.84 | -39.16 | sell /  / 종가 > 뉴욕 거래일별 누적 전형가격 VWAP; 조건 미충족; close=522.89, session_VWAP=523.72, session_volume=975370 |
| v1 | obv_20 | 9924.53 | -75.47 | sell /  / OBV > OBV의 SMA20 그리고 종가 > EMA26; 조건 미충족; OBV=-5.35236e+06, OBV_SMA20=-5.09617e+06, close=522.08, EMA26=521.373 |
| v1 | stochastic_14_3_recovery | 10000.00 | 0.00 | 대기 /  / 새 신호 대기 |
| v1 | mfi_14_recovery | 10000.00 | 0.00 | 대기 /  / 새 신호 대기 |
| v1 | adx_14_trend | 9882.74 | -117.26 | sell /  / Wilder ADX14 >= 25 그리고 +DI14 > -DI14; 조건 미충족; ADX14=30.2264, plus_DI14=23.4608, minus_DI14=27.9688 |
| v1 | aroon_25_trend | 9928.27 | -71.73 | sell /  / Aroon25 Up > 70 그리고 Down < 30 (동률이면 최신 극값); 조건 미충족; Aroon_up=68, Aroon_down=4 |
| v1 | cci_20_momentum | 9954.56 | -45.44 | sell /  / CCI20 > 100 (전형가격·평균절대편차); 조건 미충족; CCI20=83.6046 |
| v1 | williams_14_recovery | 10000.00 | 0.00 | 대기 /  / 새 신호 대기 |
| v1 | cmf_20_accumulation | 9927.80 | -72.20 | sell /  / Chaikin Money Flow20 > 0.1; 조건 미충족; CMF20=0.0502896, volume20=2.48879e+06 |
| v1 | chaikin_3_10 | 9926.34 | -73.66 | sell /  / ADL의 EMA3 - EMA10 > 0 그리고 종가 > EMA26; 조건 미충족; Chaikin3_10=-14655, ADL=-1.49709e+07, close=522.196, EMA26=521.317 |
| v1 | roc_10_momentum | 10000.00 | 0.00 | 대기 /  / 새 신호 대기 |
| v1 | trix_15_trend | 9928.27 | -71.73 | sell /  / 15봉 삼중 EMA의 1봉 변화율 TRIX > 0 그리고 종가 > EMA26; 조건 미충족; TRIX15_percent=0.0322153, close=521.26, EMA26=521.365 |
| v1 | keltner_20_breakout | 9940.12 | -59.88 | sell /  / 종가 > EMA20 + 2 x Wilder ATR14; 조건 미충족; close=522.89, upper_Keltner=523.089, EMA20=521.145, ATR14=0.971947 |
| v1 | opening_range_30m | 9980.84 | -19.16 | sell /  / 뉴욕 09:30·09:45 두 완료 봉 최고가를 10:00 이후 종가가 돌파; 자료 부족·변동폭 또는 거래량 없음: 대기; close=523.93 |
| v2 | cash | 10000.00 | 0.00 | 대기 /  / 새 신호 대기 |
| v2 | buy_hold | 10046.86 | 46.86 | buy / partial / 직전 완료 봉 목표 비중 100%; 다음 봉 시가 가정 |
| v2 | trend_8_26 | 9859.62 | -140.38 | buy / partial / 직전 완료 봉 목표 비중 100%; 다음 봉 시가 가정 |
| v2 | momentum_26 | 9952.08 | -47.92 | sell / filled / 직전 완료 봉 목표 비중 0%; 다음 봉 시가 가정 |
| v2 | breakout_8 | 9466.63 | -533.37 | sell / filled / 직전 완료 봉 목표 비중 0%; 다음 봉 시가 가정 |
| v2 | reversion_12 | 9654.11 | -345.89 | buy / partial / 직전 완료 봉 목표 비중 100%; 다음 봉 시가 가정 |
| v2 | volume_26 | 9660.98 | -339.02 | sell / filled / 직전 완료 봉 목표 비중 0%; 다음 봉 시가 가정 |
| v2 | trend_8_26 AND momentum_26 | 9947.46 | -52.54 | sell / filled / 직전 완료 봉 목표 비중 0%; 다음 봉 시가 가정 |
| v2 | trend_8_26 + momentum_26 | 9905.81 | -94.19 | sell / filled / 직전 완료 봉 목표 비중 50%; 다음 봉 시가 가정 |
| v2 | trend_8_26 AND breakout_8 | 9626.81 | -373.19 | sell / filled / 직전 완료 봉 목표 비중 0%; 다음 봉 시가 가정 |
| v2 | trend_8_26 + breakout_8 | 9661.19 | -338.81 | buy / filled / 직전 완료 봉 목표 비중 50%; 다음 봉 시가 가정 |
| v2 | trend_8_26 AND reversion_12 | 9766.34 | -233.66 | buy / partial / 직전 완료 봉 목표 비중 100%; 다음 봉 시가 가정 |
| v2 | trend_8_26 + reversion_12 | 9756.04 | -243.96 | buy / partial / 직전 완료 봉 목표 비중 100%; 다음 봉 시가 가정 |
| v2 | trend_8_26 AND volume_26 | 9800.82 | -199.18 | sell / filled / 직전 완료 봉 목표 비중 0%; 다음 봉 시가 가정 |
| v2 | trend_8_26 + volume_26 | 9780.21 | -219.79 | buy / filled / 직전 완료 봉 목표 비중 50%; 다음 봉 시가 가정 |
| v2 | momentum_26 AND breakout_8 | 9615.85 | -384.15 | sell / filled / 직전 완료 봉 목표 비중 0%; 다음 봉 시가 가정 |
| v2 | momentum_26 + breakout_8 | 9706.46 | -293.54 | sell / filled / 직전 완료 봉 목표 비중 0%; 다음 봉 시가 가정 |
| v2 | momentum_26 AND reversion_12 | 9895.03 | -104.97 | sell / filled / 직전 완료 봉 목표 비중 0%; 다음 봉 시가 가정 |
| v2 | momentum_26 + reversion_12 | 9801.75 | -198.25 | sell / filled / 직전 완료 봉 목표 비중 50%; 다음 봉 시가 가정 |
| v2 | momentum_26 AND volume_26 | 9733.77 | -266.23 | sell / filled / 직전 완료 봉 목표 비중 0%; 다음 봉 시가 가정 |
| v2 | momentum_26 + volume_26 | 9846.77 | -153.23 | sell / filled / 직전 완료 봉 목표 비중 0%; 다음 봉 시가 가정 |
| v2 | breakout_8 AND reversion_12 | 10000.00 | 0.00 | 대기 /  / 새 신호 대기 |
| v2 | breakout_8 + reversion_12 | 9559.46 | -440.54 | buy / filled / 직전 완료 봉 목표 비중 50%; 다음 봉 시가 가정 |
| v2 | breakout_8 AND volume_26 | 9796.56 | -203.44 | sell / filled / 직전 완료 봉 목표 비중 0%; 다음 봉 시가 가정 |
| v2 | breakout_8 + volume_26 | 9563.15 | -436.85 | sell / filled / 직전 완료 봉 목표 비중 0%; 다음 봉 시가 가정 |
| v2 | reversion_12 AND volume_26 | 10000.00 | 0.00 | 대기 /  / 새 신호 대기 |
| v2 | reversion_12 + volume_26 | 9677.55 | -322.45 | buy / filled / 직전 완료 봉 목표 비중 50%; 다음 봉 시가 가정 |
| v2 | ema_12_26 | 9922.92 | -77.08 | buy / partial / EMA12 > EMA26; 조건 충족; EMA12=520.818, EMA26=519.784; 직전 완료 봉 목표를 다음 봉 시가에 모의 적용 |
| v2 | macd_12_26_9 | 9939.65 | -60.35 | sell / filled / MACD > 신호선 그리고 MACD > 0; 조건 미충족; MACD=1.23542, signal9=1.25143; 직전 완료 봉 목표를 다음 봉 시가에 모의 적용 |
| v2 | rsi_14_recovery | 10000.00 | 0.00 | 대기 /  / 새 신호 대기 |
| v2 | bollinger_20_reentry | 10000.00 | 0.00 | 대기 /  / 새 신호 대기 |
| v2 | donchian_20 | 9938.13 | -61.87 | sell / filled / 종가 > 현재 봉을 제외한 직전 20봉 최고가; 조건 미충족; close=522.89, prior_high20=525.09; 직전 완료 봉 목표를 다음 봉 시가에 모의 적용 |
| v2 | atr_14_breakout | 9970.44 | -29.56 | sell / filled / 종가 > 직전 종가 + 직전 ATR14 그리고 종가 > EMA26; 조건 미충족; close=524.65, threshold=524.777, prior_ATR14=0.84688, EMA26=520.429; 직전 완료 봉 목표를 다음 봉 시가에 모의 적용 |
| v2 | session_vwap | 9958.85 | -41.15 | sell / filled / 종가 > 뉴욕 거래일별 누적 전형가격 VWAP; 조건 미충족; close=522.89, session_VWAP=523.72, session_volume=975370; 직전 완료 봉 목표를 다음 봉 시가에 모의 적용 |
| v2 | obv_20 | 9922.55 | -77.45 | sell / filled / OBV > OBV의 SMA20 그리고 종가 > EMA26; 조건 미충족; OBV=-5.35236e+06, OBV_SMA20=-5.09617e+06, close=522.08, EMA26=521.373; 직전 완료 봉 목표를 다음 봉 시가에 모의 적용 |
| v2 | stochastic_14_3_recovery | 10000.00 | 0.00 | 대기 /  / 새 신호 대기 |
| v2 | mfi_14_recovery | 10000.00 | 0.00 | 대기 /  / 새 신호 대기 |
| v2 | adx_14_trend | 9878.79 | -121.21 | sell / filled / Wilder ADX14 >= 25 그리고 +DI14 > -DI14; 조건 미충족; ADX14=30.2264, plus_DI14=23.4608, minus_DI14=27.9688; 직전 완료 봉 목표를 다음 봉 시가에 모의 적용 |
| v2 | aroon_25_trend | 9926.28 | -73.72 | sell / filled / Aroon25 Up > 70 그리고 Down < 30 (동률이면 최신 극값); 조건 미충족; Aroon_up=68, Aroon_down=4; 직전 완료 봉 목표를 다음 봉 시가에 모의 적용 |
| v2 | cci_20_momentum | 9952.57 | -47.43 | sell / filled / CCI20 > 100 (전형가격·평균절대편차); 조건 미충족; CCI20=83.6046; 직전 완료 봉 목표를 다음 봉 시가에 모의 적용 |
| v2 | williams_14_recovery | 10000.00 | 0.00 | 대기 /  / 새 신호 대기 |
| v2 | cmf_20_accumulation | 9925.82 | -74.18 | sell / filled / Chaikin Money Flow20 > 0.1; 조건 미충족; CMF20=0.0502896, volume20=2.48879e+06; 직전 완료 봉 목표를 다음 봉 시가에 모의 적용 |
| v2 | chaikin_3_10 | 9924.35 | -75.65 | sell / filled / ADL의 EMA3 - EMA10 > 0 그리고 종가 > EMA26; 조건 미충족; Chaikin3_10=-14655, ADL=-1.49709e+07, close=522.196, EMA26=521.317; 직전 완료 봉 목표를 다음 봉 시가에 모의 적용 |
| v2 | roc_10_momentum | 10000.00 | 0.00 | 대기 /  / 새 신호 대기 |
| v2 | trix_15_trend | 9926.28 | -73.72 | sell / filled / 15봉 삼중 EMA의 1봉 변화율 TRIX > 0 그리고 종가 > EMA26; 조건 미충족; TRIX15_percent=0.0322153, close=521.26, EMA26=521.365; 직전 완료 봉 목표를 다음 봉 시가에 모의 적용 |
| v2 | keltner_20_breakout | 9938.13 | -61.87 | sell / filled / 종가 > EMA20 + 2 x Wilder ATR14; 조건 미충족; close=522.89, upper_Keltner=523.089, EMA20=521.145, ATR14=0.971947; 직전 완료 봉 목표를 다음 봉 시가에 모의 적용 |
| v2 | opening_range_30m | 9978.85 | -21.15 | sell / filled / 뉴욕 09:30·09:45 두 완료 봉 최고가를 10:00 이후 종가가 돌파; 자료 부족·변동폭 또는 거래량 없음: 대기; close=523.93; 직전 완료 봉 목표를 다음 봉 시가에 모의 적용 |

### 같은 기간의 비용·노출 비교 (사후 연구)

| 전략 | 비용 전 | 비용 후 | 100% 보유 | 같은 평균 노출 보유 | 평균 노출 |
|---|---:|---:|---:|---:|---:|
| cash | 0.00% | 0.00% | 0.10% | 0.00% | 0.00% |
| buy_hold | 0.52% | 0.10% | 0.10% | 0.10% | 100.00% |
| trend_8_26 | 0.83% | -3.72% | 0.10% | 0.05% | 56.17% |
| momentum_26 | -0.45% | -4.54% | 0.10% | 0.05% | 52.23% |
| breakout_8 | -0.13% | -17.33% | 0.10% | 0.02% | 23.62% |
| reversion_12 | -1.60% | -9.90% | 0.10% | 0.02% | 25.72% |
| volume_26 | -1.08% | -11.31% | 0.10% | 0.01% | 11.02% |
| trend_8_26 AND momentum_26 | 1.02% | -3.14% | 0.10% | 0.04% | 46.46% |
| trend_8_26 + momentum_26 | 0.19% | -4.13% | 0.10% | 0.05% | 54.20% |
| trend_8_26 AND breakout_8 | 0.44% | -11.82% | 0.10% | 0.01% | 15.49% |
| trend_8_26 + breakout_8 | 0.35% | -10.60% | 0.10% | 0.04% | 39.90% |
| trend_8_26 AND reversion_12 | 0.13% | -5.20% | 0.10% | 0.01% | 7.35% |
| trend_8_26 + reversion_12 | -0.39% | -6.48% | 0.10% | 0.04% | 40.95% |
| trend_8_26 AND volume_26 | 0.48% | -4.86% | 0.10% | 0.01% | 5.25% |
| trend_8_26 + volume_26 | -0.12% | -7.41% | 0.10% | 0.03% | 33.60% |
| momentum_26 AND breakout_8 | -0.36% | -12.15% | 0.10% | 0.02% | 15.75% |
| momentum_26 + breakout_8 | -0.28% | -10.98% | 0.10% | 0.04% | 37.93% |
| momentum_26 AND reversion_12 | -0.37% | -4.47% | 0.10% | 0.01% | 6.56% |
| momentum_26 + reversion_12 | -1.02% | -6.49% | 0.10% | 0.04% | 38.98% |
| momentum_26 AND volume_26 | -0.49% | -5.77% | 0.10% | 0.00% | 4.72% |
| momentum_26 + volume_26 | -0.76% | -7.22% | 0.10% | 0.03% | 31.63% |
| breakout_8 AND reversion_12 | 0.00% | 0.00% | 0.10% | 0.00% | 0.00% |
| breakout_8 + reversion_12 | -0.86% | -13.34% | 0.10% | 0.02% | 24.68% |
| breakout_8 AND volume_26 | -0.87% | -4.55% | 0.10% | 0.00% | 3.15% |
| breakout_8 + volume_26 | -0.60% | -13.66% | 0.10% | 0.02% | 17.33% |
| reversion_12 AND volume_26 | -0.20% | -5.11% | 0.10% | 0.00% | 3.94% |
| reversion_12 + volume_26 | -1.33% | -10.43% | 0.10% | 0.02% | 18.38% |
| ema_12_26 | -0.26% | -2.74% | 0.10% | 0.05% | 50.92% |
| macd_12_26_9 | 1.56% | -1.80% | 0.10% | 0.03% | 27.82% |
| rsi_14_recovery | 0.01% | -2.07% | 0.10% | 0.00% | 1.31% |
| bollinger_20_reentry | -0.25% | -5.16% | 0.10% | 0.00% | 3.15% |
| donchian_20 | 0.36% | -5.77% | 0.10% | 0.01% | 8.14% |
| atr_14_breakout | -1.05% | -8.25% | 0.10% | 0.01% | 5.51% |
| session_vwap | 1.06% | -6.69% | 0.10% | 0.05% | 49.87% |
| obv_20 | -0.07% | -8.51% | 0.10% | 0.04% | 43.57% |
| stochastic_14_3_recovery | 0.79% | -11.14% | 0.10% | 0.01% | 7.87% |
| mfi_14_recovery | -0.06% | -2.95% | 0.10% | 0.00% | 1.84% |
| adx_14_trend | -0.68% | -5.16% | 0.10% | 0.04% | 36.75% |
| aroon_25_trend | 0.77% | -2.56% | 0.10% | 0.03% | 25.98% |
| cci_20_momentum | 0.66% | -5.09% | 0.10% | 0.02% | 23.88% |
| williams_14_recovery | 1.01% | -6.74% | 0.10% | 0.00% | 4.99% |
| cmf_20_accumulation | 0.61% | -6.33% | 0.10% | 0.03% | 30.97% |
| chaikin_3_10 | 1.13% | -8.57% | 0.10% | 0.04% | 42.26% |
| roc_10_momentum | 0.15% | -0.27% | 0.10% | 0.00% | 1.31% |
| trix_15_trend | -0.30% | -4.00% | 0.10% | 0.04% | 43.04% |
| keltner_20_breakout | 0.33% | -5.79% | 0.10% | 0.02% | 16.80% |
| opening_range_30m | 0.84% | -5.32% | 0.10% | 0.02% | 21.52% |

동일 구간·초기 자금, 종료 시 청산 비용 포함. 노출 맞춤은 사후 설명용이며 v2 실제 계좌 성과가 아닙니다.
[낙폭 분해·비용 영향·전체 구간](DIA/comparison.json)

[v1 전체 기록](DIA/accounts.json) · [v2 전체 기록](DIA/accounts-v2.json)

## MSFT 계좌

| 모델 | 전략 | 평가액 USD | 손익 USD | 최근 매매·이유 |
|---|---|---:|---:|---|
| v1 | cash | 10000.00 | 0.00 | 대기 /  / 새 신호 대기 |
| v1 | buy_hold | 9740.52 | -259.48 | buy /  / buy_hold: prior completed bar target 100%; next bar open simulation |
| v1 | trend_8_26 | 9853.68 | -146.32 | sell /  / trend_8_26: prior completed bar target 0%; next bar open simulation |
| v1 | momentum_26 | 9839.32 | -160.68 | sell /  / momentum_26: prior completed bar target 0%; next bar open simulation |
| v1 | breakout_8 | 10000.00 | 0.00 | 대기 /  / 새 신호 대기 |
| v1 | reversion_12 | 9809.59 | -190.41 | buy /  / reversion_12: prior completed bar target 100%; next bar open simulation |
| v1 | volume_26 | 9938.00 | -62.00 | sell /  / volume_26: prior completed bar target 0%; next bar open simulation |
| v1 | trend_8_26 AND momentum_26 | 9853.68 | -146.32 | sell /  / trend_8_26 AND momentum_26: prior completed bar target 0%; next bar open simulation |
| v1 | trend_8_26 + momentum_26 | 9846.52 | -153.48 | sell /  / trend_8_26 + momentum_26: prior completed bar target 0%; next bar open simulation |
| v1 | trend_8_26 AND breakout_8 | 10000.00 | 0.00 | 대기 /  / 새 신호 대기 |
| v1 | trend_8_26 + breakout_8 | 9926.58 | -73.42 | sell /  / trend_8_26 + breakout_8: prior completed bar target 0%; next bar open simulation |
| v1 | trend_8_26 AND reversion_12 | 9923.56 | -76.44 | sell /  / trend_8_26 AND reversion_12: prior completed bar target 0%; next bar open simulation |
| v1 | trend_8_26 + reversion_12 | 9831.59 | -168.41 | buy /  / trend_8_26 + reversion_12: prior completed bar target 50%; next bar open simulation |
| v1 | trend_8_26 AND volume_26 | 10000.00 | 0.00 | 대기 /  / 새 신호 대기 |
| v1 | trend_8_26 + volume_26 | 9895.73 | -104.27 | sell /  / trend_8_26 + volume_26: prior completed bar target 0%; next bar open simulation |
| v1 | momentum_26 AND breakout_8 | 10000.00 | 0.00 | 대기 /  / 새 신호 대기 |
| v1 | momentum_26 + breakout_8 | 9919.33 | -80.67 | sell /  / momentum_26 + breakout_8: prior completed bar target 0%; next bar open simulation |
| v1 | momentum_26 AND reversion_12 | 9909.10 | -90.90 | sell /  / momentum_26 AND reversion_12: prior completed bar target 0%; next bar open simulation |
| v1 | momentum_26 + reversion_12 | 9824.43 | -175.57 | buy /  / momentum_26 + reversion_12: prior completed bar target 50%; next bar open simulation |
| v1 | momentum_26 AND volume_26 | 10000.00 | 0.00 | 대기 /  / 새 신호 대기 |
| v1 | momentum_26 + volume_26 | 9888.51 | -111.49 | sell /  / momentum_26 + volume_26: prior completed bar target 0%; next bar open simulation |
| v1 | breakout_8 AND reversion_12 | 10000.00 | 0.00 | 대기 /  / 새 신호 대기 |
| v1 | breakout_8 + reversion_12 | 9904.29 | -95.71 | buy /  / breakout_8 + reversion_12: prior completed bar target 50%; next bar open simulation |
| v1 | breakout_8 AND volume_26 | 10000.00 | 0.00 | 대기 /  / 새 신호 대기 |
| v1 | breakout_8 + volume_26 | 9968.93 | -31.07 | sell /  / breakout_8 + volume_26: prior completed bar target 0%; next bar open simulation |
| v1 | reversion_12 AND volume_26 | 9938.00 | -62.00 | sell /  / reversion_12 AND volume_26: prior completed bar target 0%; next bar open simulation |
| v1 | reversion_12 + volume_26 | 9873.54 | -126.46 | buy /  / reversion_12 + volume_26: prior completed bar target 50%; next bar open simulation |
| v1 | ema_12_26 | 9853.68 | -146.32 | sell /  / EMA12 > EMA26; 조건 미충족; EMA12=538.192, EMA26=538.342 |
| v1 | macd_12_26_9 | 9889.94 | -110.06 | sell /  / MACD > 신호선 그리고 MACD > 0; 조건 미충족; MACD=0.536125, signal9=0.712825 |
| v1 | rsi_14_recovery | 10000.00 | 0.00 | 대기 /  / 새 신호 대기 |
| v1 | bollinger_20_reentry | 9885.00 | -115.00 | sell /  / 직전 종가 < 직전 하단밴드, 현재 하단밴드 <= 종가 <= SMA20 (한 봉 목표); 조건 미충족; close=529.125, lower20=527.516, SMA20=535.918, previous_lower20=528.497 |
| v1 | donchian_20 | 10000.00 | 0.00 | 대기 /  / 새 신호 대기 |
| v1 | atr_14_breakout | 10000.00 | 0.00 | 대기 /  / 새 신호 대기 |
| v1 | session_vwap | 9889.94 | -110.06 | sell /  / 종가 > 뉴욕 거래일별 누적 전형가격 VWAP; 조건 미충족; close=537.34, session_VWAP=538.663, session_volume=3.36828e+06 |
| v1 | obv_20 | 9889.94 | -110.06 | sell /  / OBV > OBV의 SMA20 그리고 종가 > EMA26; 조건 미충족; OBV=1.44955e+08, OBV_SMA20=1.34631e+08, close=537.34, EMA26=538.834 |
| v1 | stochastic_14_3_recovery | 9795.67 | -204.33 | sell /  / 직전 %K14 < 20에서 %K14가 %D3 상향 돌파 (한 봉 목표); 조건 미충족; K14=9.65793, D3=7.84926, previous_K14=12.2725, previous_D3=6.82685 |
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
| v2 | buy_hold | 9793.67 | -206.33 | buy / partial / 직전 완료 봉 목표 비중 100%; 다음 봉 시가 가정 |
| v2 | trend_8_26 | 9790.17 | -209.83 | sell / filled / 직전 완료 봉 목표 비중 0%; 다음 봉 시가 가정 |
| v2 | momentum_26 | 9886.18 | -113.82 | sell / filled / 직전 완료 봉 목표 비중 0%; 다음 봉 시가 가정 |
| v2 | breakout_8 | 9799.48 | -200.52 | sell / filled / 직전 완료 봉 목표 비중 0%; 다음 봉 시가 가정 |
| v2 | reversion_12 | 9434.53 | -565.47 | buy / partial / 직전 완료 봉 목표 비중 100%; 다음 봉 시가 가정 |
| v2 | volume_26 | 9626.55 | -373.45 | sell / filled / 직전 완료 봉 목표 비중 0%; 다음 봉 시가 가정 |
| v2 | trend_8_26 AND momentum_26 | 9751.13 | -248.87 | sell / filled / 직전 완료 봉 목표 비중 0%; 다음 봉 시가 가정 |
| v2 | trend_8_26 + momentum_26 | 9838.34 | -161.66 | sell / filled / 직전 완료 봉 목표 비중 0%; 다음 봉 시가 가정 |
| v2 | trend_8_26 AND breakout_8 | 9639.29 | -360.71 | sell / filled / 직전 완료 봉 목표 비중 0%; 다음 봉 시가 가정 |
| v2 | trend_8_26 + breakout_8 | 9815.63 | -184.37 | sell / filled / 직전 완료 봉 목표 비중 0%; 다음 봉 시가 가정 |
| v2 | trend_8_26 AND reversion_12 | 9822.46 | -177.54 | sell / filled / 직전 완료 봉 목표 비중 0%; 다음 봉 시가 가정 |
| v2 | trend_8_26 + reversion_12 | 9610.36 | -389.64 | buy / filled / 직전 완료 봉 목표 비중 50%; 다음 봉 시가 가정 |
| v2 | trend_8_26 AND volume_26 | 9948.66 | -51.34 | sell / filled / 직전 완료 봉 목표 비중 0%; 다음 봉 시가 가정 |
| v2 | trend_8_26 + volume_26 | 9728.21 | -271.79 | sell / filled / 직전 완료 봉 목표 비중 0%; 다음 봉 시가 가정 |
| v2 | momentum_26 AND breakout_8 | 9794.38 | -205.62 | sell / filled / 직전 완료 봉 목표 비중 0%; 다음 봉 시가 가정 |
| v2 | momentum_26 + breakout_8 | 9842.81 | -157.19 | sell / filled / 직전 완료 봉 목표 비중 0%; 다음 봉 시가 가정 |
| v2 | momentum_26 AND reversion_12 | 9735.61 | -264.39 | sell / filled / 직전 완료 봉 목표 비중 0%; 다음 봉 시가 가정 |
| v2 | momentum_26 + reversion_12 | 9657.49 | -342.51 | buy / filled / 직전 완료 봉 목표 비중 50%; 다음 봉 시가 가정 |
| v2 | momentum_26 AND volume_26 | 9871.26 | -128.74 | sell / filled / 직전 완료 봉 목표 비중 0%; 다음 봉 시가 가정 |
| v2 | momentum_26 + volume_26 | 9775.92 | -224.08 | sell / filled / 직전 완료 봉 목표 비중 0%; 다음 봉 시가 가정 |
| v2 | breakout_8 AND reversion_12 | 10000.00 | 0.00 | 대기 /  / 새 신호 대기 |
| v2 | breakout_8 + reversion_12 | 9635.24 | -364.76 | buy / filled / 직전 완료 봉 목표 비중 50%; 다음 봉 시가 가정 |
| v2 | breakout_8 AND volume_26 | 9938.59 | -61.41 | sell / filled / 직전 완료 봉 목표 비중 0%; 다음 봉 시가 가정 |
| v2 | breakout_8 + volume_26 | 9733.07 | -266.93 | sell / filled / 직전 완료 봉 목표 비중 0%; 다음 봉 시가 가정 |
| v2 | reversion_12 AND volume_26 | 9699.57 | -300.43 | sell / filled / 직전 완료 봉 목표 비중 0%; 다음 봉 시가 가정 |
| v2 | reversion_12 + volume_26 | 9529.86 | -470.14 | buy / filled / 직전 완료 봉 목표 비중 50%; 다음 봉 시가 가정 |
| v2 | ema_12_26 | 9851.71 | -148.29 | sell / filled / EMA12 > EMA26; 조건 미충족; EMA12=538.192, EMA26=538.342; 직전 완료 봉 목표를 다음 봉 시가에 모의 적용 |
| v2 | macd_12_26_9 | 9887.97 | -112.03 | sell / filled / MACD > 신호선 그리고 MACD > 0; 조건 미충족; MACD=0.536125, signal9=0.712825; 직전 완료 봉 목표를 다음 봉 시가에 모의 적용 |
| v2 | rsi_14_recovery | 10000.00 | 0.00 | 대기 /  / 새 신호 대기 |
| v2 | bollinger_20_reentry | 9881.05 | -118.95 | sell / filled / 직전 종가 < 직전 하단밴드, 현재 하단밴드 <= 종가 <= SMA20 (한 봉 목표); 조건 미충족; close=529.125, lower20=527.516, SMA20=535.918, previous_lower20=528.497; 직전 완료 봉 목표를 다음 봉 시가에 모의 적용 |
| v2 | donchian_20 | 10000.00 | 0.00 | 대기 /  / 새 신호 대기 |
| v2 | atr_14_breakout | 10000.00 | 0.00 | 대기 /  / 새 신호 대기 |
| v2 | session_vwap | 9887.97 | -112.03 | sell / filled / 종가 > 뉴욕 거래일별 누적 전형가격 VWAP; 조건 미충족; close=537.34, session_VWAP=538.663, session_volume=3.36828e+06; 직전 완료 봉 목표를 다음 봉 시가에 모의 적용 |
| v2 | obv_20 | 9887.97 | -112.03 | sell / filled / OBV > OBV의 SMA20 그리고 종가 > EMA26; 조건 미충족; OBV=1.44955e+08, OBV_SMA20=1.34631e+08, close=537.34, EMA26=538.834; 직전 완료 봉 목표를 다음 봉 시가에 모의 적용 |
| v2 | stochastic_14_3_recovery | 9789.80 | -210.20 | sell / filled / 직전 %K14 < 20에서 %K14가 %D3 상향 돌파 (한 봉 목표); 조건 미충족; K14=9.65793, D3=7.84926, previous_K14=12.2725, previous_D3=6.82685; 직전 완료 봉 목표를 다음 봉 시가에 모의 적용 |
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
| cash | 0.00% | 0.00% | 1.88% | 0.00% | 0.00% |
| buy_hold | 2.31% | 1.88% | 1.88% | 1.88% | 100.00% |
| trend_8_26 | -1.32% | -4.98% | 1.88% | 1.06% | 56.96% |
| momentum_26 | -0.34% | -6.03% | 1.88% | 1.08% | 57.74% |
| breakout_8 | 5.09% | -8.89% | 1.88% | 0.36% | 19.69% |
| reversion_12 | -5.69% | -14.37% | 1.88% | 0.50% | 26.77% |
| volume_26 | 2.21% | -6.42% | 1.88% | 0.16% | 8.66% |
| trend_8_26 AND momentum_26 | -1.58% | -7.20% | 1.88% | 0.95% | 51.18% |
| trend_8_26 + momentum_26 | -0.82% | -5.50% | 1.88% | 1.07% | 57.35% |
| trend_8_26 AND breakout_8 | 0.68% | -8.98% | 1.88% | 0.23% | 12.60% |
| trend_8_26 + breakout_8 | 1.85% | -6.56% | 1.88% | 0.71% | 38.33% |
| trend_8_26 AND reversion_12 | -3.74% | -9.24% | 1.88% | 0.15% | 7.87% |
| trend_8_26 + reversion_12 | -3.51% | -9.42% | 1.88% | 0.78% | 41.87% |
| trend_8_26 AND volume_26 | 3.46% | 0.46% | 1.88% | 0.05% | 2.62% |
| trend_8_26 + volume_26 | 0.45% | -4.91% | 1.88% | 0.61% | 32.81% |
| momentum_26 AND breakout_8 | 2.61% | -7.61% | 1.88% | 0.24% | 12.86% |
| momentum_26 + breakout_8 | 2.36% | -6.88% | 1.88% | 0.72% | 38.72% |
| momentum_26 AND reversion_12 | -3.23% | -9.52% | 1.88% | 0.17% | 9.45% |
| momentum_26 + reversion_12 | -3.03% | -9.92% | 1.88% | 0.79% | 42.26% |
| momentum_26 AND volume_26 | 1.80% | -2.38% | 1.88% | 0.06% | 3.41% |
| momentum_26 + volume_26 | 0.94% | -5.03% | 1.88% | 0.62% | 33.21% |
| breakout_8 AND reversion_12 | 0.00% | 0.00% | 1.88% | 0.00% | 0.00% |
| breakout_8 + reversion_12 | -0.42% | -11.11% | 1.88% | 0.43% | 23.24% |
| breakout_8 AND volume_26 | 2.07% | -0.47% | 1.88% | 0.03% | 1.84% |
| breakout_8 + volume_26 | 3.65% | -6.69% | 1.88% | 0.26% | 14.18% |
| reversion_12 AND volume_26 | -2.48% | -6.49% | 1.88% | 0.07% | 3.94% |
| reversion_12 + volume_26 | -1.80% | -10.29% | 1.88% | 0.33% | 17.72% |
| ema_12_26 | -0.73% | -4.41% | 1.88% | 1.13% | 60.63% |
| macd_12_26_9 | 0.71% | -4.24% | 1.88% | 0.61% | 32.81% |
| rsi_14_recovery | -0.46% | -1.71% | 1.88% | 0.01% | 0.79% |
| bollinger_20_reentry | -0.52% | -3.81% | 1.88% | 0.04% | 2.10% |
| donchian_20 | 1.84% | -3.17% | 1.88% | 0.08% | 4.46% |
| atr_14_breakout | 1.50% | -3.89% | 1.88% | 0.07% | 3.67% |
| session_vwap | 2.79% | -5.09% | 1.88% | 0.85% | 45.93% |
| obv_20 | 4.17% | -4.62% | 1.88% | 0.95% | 51.18% |
| stochastic_14_3_recovery | -0.68% | -10.95% | 1.88% | 0.13% | 6.82% |
| mfi_14_recovery | 1.04% | -1.88% | 1.88% | 0.03% | 1.84% |
| adx_14_trend | 1.27% | -1.66% | 1.88% | 0.82% | 44.36% |
| aroon_25_trend | 0.23% | -4.29% | 1.88% | 0.38% | 20.47% |
| cci_20_momentum | 2.74% | -3.54% | 1.88% | 0.38% | 20.47% |
| williams_14_recovery | -0.28% | -9.09% | 1.88% | 0.11% | 5.77% |
| cmf_20_accumulation | 0.57% | -5.18% | 1.88% | 0.66% | 35.70% |
| chaikin_3_10 | 3.42% | -4.51% | 1.88% | 0.83% | 44.62% |
| roc_10_momentum | -0.20% | -4.30% | 1.88% | 0.26% | 14.17% |
| trix_15_trend | -1.60% | -5.64% | 1.88% | 0.87% | 46.72% |
| keltner_20_breakout | 1.12% | -3.85% | 1.88% | 0.25% | 13.39% |
| opening_range_30m | -2.08% | -6.89% | 1.88% | 0.44% | 23.62% |

동일 구간·초기 자금, 종료 시 청산 비용 포함. 노출 맞춤은 사후 설명용이며 v2 실제 계좌 성과가 아닙니다.
[낙폭 분해·비용 영향·전체 구간](MSFT/comparison.json)

[v1 전체 기록](MSFT/accounts.json) · [v2 전체 기록](MSFT/accounts-v2.json)

## JPM 계좌

| 모델 | 전략 | 평가액 USD | 손익 USD | 최근 매매·이유 |
|---|---|---:|---:|---|
| v1 | cash | 10000.00 | 0.00 | 대기 /  / 새 신호 대기 |
| v1 | buy_hold | 9954.78 | -45.22 | buy /  / buy_hold: prior completed bar target 100%; next bar open simulation |
| v1 | trend_8_26 | 9954.78 | -45.22 | buy /  / trend_8_26: prior completed bar target 100%; next bar open simulation |
| v1 | momentum_26 | 9954.78 | -45.22 | buy /  / momentum_26: prior completed bar target 100%; next bar open simulation |
| v1 | breakout_8 | 9915.55 | -84.45 | sell /  / breakout_8: prior completed bar target 0%; next bar open simulation |
| v1 | reversion_12 | 9941.33 | -58.67 | buy /  / reversion_12: prior completed bar target 100%; next bar open simulation |
| v1 | volume_26 | 10035.68 | 35.68 | sell /  / volume_26: prior completed bar target 0%; next bar open simulation |
| v1 | trend_8_26 AND momentum_26 | 9954.78 | -45.22 | buy /  / trend_8_26 AND momentum_26: prior completed bar target 100%; next bar open simulation |
| v1 | trend_8_26 + momentum_26 | 9954.78 | -45.22 | buy /  / trend_8_26 + momentum_26: prior completed bar target 100%; next bar open simulation |
| v1 | trend_8_26 AND breakout_8 | 9915.55 | -84.45 | sell /  / trend_8_26 AND breakout_8: prior completed bar target 0%; next bar open simulation |
| v1 | trend_8_26 + breakout_8 | 9935.23 | -64.77 | buy /  / trend_8_26 + breakout_8: prior completed bar target 50%; next bar open simulation |
| v1 | trend_8_26 AND reversion_12 | 9941.33 | -58.67 | buy /  / trend_8_26 AND reversion_12: prior completed bar target 100%; next bar open simulation |
| v1 | trend_8_26 + reversion_12 | 9948.06 | -51.94 | buy /  / trend_8_26 + reversion_12: prior completed bar target 100%; next bar open simulation |
| v1 | trend_8_26 AND volume_26 | 10035.68 | 35.68 | sell /  / trend_8_26 AND volume_26: prior completed bar target 0%; next bar open simulation |
| v1 | trend_8_26 + volume_26 | 9995.11 | -4.89 | buy /  / trend_8_26 + volume_26: prior completed bar target 50%; next bar open simulation |
| v1 | momentum_26 AND breakout_8 | 9915.55 | -84.45 | sell /  / momentum_26 AND breakout_8: prior completed bar target 0%; next bar open simulation |
| v1 | momentum_26 + breakout_8 | 9935.23 | -64.77 | buy /  / momentum_26 + breakout_8: prior completed bar target 50%; next bar open simulation |
| v1 | momentum_26 AND reversion_12 | 9941.33 | -58.67 | buy /  / momentum_26 AND reversion_12: prior completed bar target 100%; next bar open simulation |
| v1 | momentum_26 + reversion_12 | 9948.06 | -51.94 | buy /  / momentum_26 + reversion_12: prior completed bar target 100%; next bar open simulation |
| v1 | momentum_26 AND volume_26 | 10035.68 | 35.68 | sell /  / momentum_26 AND volume_26: prior completed bar target 0%; next bar open simulation |
| v1 | momentum_26 + volume_26 | 9995.11 | -4.89 | buy /  / momentum_26 + volume_26: prior completed bar target 50%; next bar open simulation |
| v1 | breakout_8 AND reversion_12 | 10000.00 | 0.00 | 대기 /  / 새 신호 대기 |
| v1 | breakout_8 + reversion_12 | 9928.48 | -71.52 | sell /  / breakout_8 + reversion_12: prior completed bar target 50%; next bar open simulation |
| v1 | breakout_8 AND volume_26 | 10035.68 | 35.68 | sell /  / breakout_8 AND volume_26: prior completed bar target 0%; next bar open simulation |
| v1 | breakout_8 + volume_26 | 9975.44 | -24.56 | sell /  / breakout_8 + volume_26: prior completed bar target 0%; next bar open simulation |
| v1 | reversion_12 AND volume_26 | 10000.00 | 0.00 | 대기 /  / 새 신호 대기 |
| v1 | reversion_12 + volume_26 | 9988.43 | -11.57 | sell /  / reversion_12 + volume_26: prior completed bar target 50%; next bar open simulation |
| v1 | ema_12_26 | 9954.78 | -45.22 | buy /  / EMA12 > EMA26; 조건 충족; EMA12=334.708, EMA26=334.451 |
| v1 | macd_12_26_9 | 9973.56 | -26.44 | sell /  / MACD > 신호선 그리고 MACD > 0; 조건 미충족; MACD=1.87003, signal9=1.96381 |
| v1 | rsi_14_recovery | 10000.00 | 0.00 | 대기 /  / 새 신호 대기 |
| v1 | bollinger_20_reentry | 10000.00 | 0.00 | 대기 /  / 새 신호 대기 |
| v1 | donchian_20 | 9872.30 | -127.70 | sell /  / 종가 > 현재 봉을 제외한 직전 20봉 최고가; 조건 미충족; close=343.037, prior_high20=344.4 |
| v1 | atr_14_breakout | 9886.92 | -113.08 | sell /  / 종가 > 직전 종가 + 직전 ATR14 그리고 종가 > EMA26; 조건 미충족; close=342.515, threshold=344.598, prior_ATR14=1.50332, EMA26=336.975 |
| v1 | session_vwap | 9936.81 | -63.19 | sell /  / 종가 > 뉴욕 거래일별 누적 전형가격 VWAP; 조건 미충족; close=342, session_VWAP=342.233, session_volume=3.25898e+06 |
| v1 | obv_20 | 10007.55 | 7.55 | sell /  / OBV > OBV의 SMA20 그리고 종가 > EMA26; 조건 미충족; OBV=-1.38544e+07, OBV_SMA20=-1.10099e+07, close=341.625, EMA26=338.807 |
| v1 | stochastic_14_3_recovery | 10000.00 | 0.00 | 대기 /  / 새 신호 대기 |
| v1 | mfi_14_recovery | 10000.00 | 0.00 | 대기 /  / 새 신호 대기 |
| v1 | adx_14_trend | 9861.94 | -138.06 | buy /  / Wilder ADX14 >= 25 그리고 +DI14 > -DI14; 조건 충족; ADX14=26.8739, plus_DI14=46.4083, minus_DI14=10.993 |
| v1 | aroon_25_trend | 9879.79 | -120.21 | buy /  / Aroon25 Up > 70 그리고 Down < 30 (동률이면 최신 극값); 조건 충족; Aroon_up=100, Aroon_down=4 |
| v1 | cci_20_momentum | 10050.62 | 50.62 | sell /  / CCI20 > 100 (전형가격·평균절대편차); 조건 미충족; CCI20=93.5627 |
| v1 | williams_14_recovery | 10000.00 | 0.00 | 대기 /  / 새 신호 대기 |
| v1 | cmf_20_accumulation | 9932.16 | -67.84 | sell /  / Chaikin Money Flow20 > 0.1; 조건 미충족; CMF20=-0.14511, volume20=9.3038e+06 |
| v1 | chaikin_3_10 | 10007.55 | 7.55 | sell /  / ADL의 EMA3 - EMA10 > 0 그리고 종가 > EMA26; 조건 미충족; Chaikin3_10=-655976, ADL=-7.91325e+06, close=341.625, EMA26=338.807 |
| v1 | roc_10_momentum | 9913.84 | -86.16 | sell /  / 10봉 ROC > 1% 그리고 종가 > EMA26; 조건 미충족; ROC10_percent=-0.490038, close=340.901, EMA26=338.962 |
| v1 | trix_15_trend | 9954.78 | -45.22 | buy /  / 15봉 삼중 EMA의 1봉 변화율 TRIX > 0 그리고 종가 > EMA26; 조건 충족; TRIX15_percent=0.00554135, close=335.52, EMA26=334.451 |
| v1 | keltner_20_breakout | 9946.99 | -53.01 | sell /  / 종가 > EMA20 + 2 x Wilder ATR14; 조건 미충족; close=342, upper_Keltner=342.276, EMA20=339.397, ATR14=1.43933 |
| v1 | opening_range_30m | 9927.81 | -72.19 | sell /  / 뉴욕 09:30·09:45 두 완료 봉 최고가를 10:00 이후 종가가 돌파; 조건 미충족; close=343.037, opening_high=343.75 |
| v2 | cash | 10000.00 | 0.00 | 대기 /  / 새 신호 대기 |
| v2 | buy_hold | 10121.12 | 121.12 | buy / partial / 직전 완료 봉 목표 비중 100%; 다음 봉 시가 가정 |
| v2 | trend_8_26 | 9962.93 | -37.07 | buy / partial / 직전 완료 봉 목표 비중 100%; 다음 봉 시가 가정 |
| v2 | momentum_26 | 9461.66 | -538.34 | buy / partial / 직전 완료 봉 목표 비중 100%; 다음 봉 시가 가정 |
| v2 | breakout_8 | 9251.20 | -748.80 | sell / filled / 직전 완료 봉 목표 비중 0%; 다음 봉 시가 가정 |
| v2 | reversion_12 | 9932.36 | -67.64 | buy / partial / 직전 완료 봉 목표 비중 100%; 다음 봉 시가 가정 |
| v2 | volume_26 | 9859.79 | -140.21 | sell / filled / 직전 완료 봉 목표 비중 0%; 다음 봉 시가 가정 |
| v2 | trend_8_26 AND momentum_26 | 9922.04 | -77.96 | buy / partial / 직전 완료 봉 목표 비중 100%; 다음 봉 시가 가정 |
| v2 | trend_8_26 + momentum_26 | 9730.01 | -269.99 | buy / partial / 직전 완료 봉 목표 비중 100%; 다음 봉 시가 가정 |
| v2 | trend_8_26 AND breakout_8 | 9287.76 | -712.24 | sell / filled / 직전 완료 봉 목표 비중 0%; 다음 봉 시가 가정 |
| v2 | trend_8_26 + breakout_8 | 9601.62 | -398.38 | buy / filled / 직전 완료 봉 목표 비중 50%; 다음 봉 시가 가정 |
| v2 | trend_8_26 AND reversion_12 | 9922.05 | -77.95 | buy / partial / 직전 완료 봉 목표 비중 100%; 다음 봉 시가 가정 |
| v2 | trend_8_26 + reversion_12 | 9989.73 | -10.27 | buy / partial / 직전 완료 봉 목표 비중 100%; 다음 봉 시가 가정 |
| v2 | trend_8_26 AND volume_26 | 9833.30 | -166.70 | sell / filled / 직전 완료 봉 목표 비중 0%; 다음 봉 시가 가정 |
| v2 | trend_8_26 + volume_26 | 9912.03 | -87.97 | buy / filled / 직전 완료 봉 목표 비중 50%; 다음 봉 시가 가정 |
| v2 | momentum_26 AND breakout_8 | 9232.70 | -767.30 | sell / filled / 직전 완료 봉 목표 비중 0%; 다음 봉 시가 가정 |
| v2 | momentum_26 + breakout_8 | 9377.20 | -622.80 | buy / filled / 직전 완료 봉 목표 비중 50%; 다음 봉 시가 가정 |
| v2 | momentum_26 AND reversion_12 | 9891.38 | -108.62 | buy / partial / 직전 완료 봉 목표 비중 100%; 다음 봉 시가 가정 |
| v2 | momentum_26 + reversion_12 | 9817.65 | -182.35 | buy / partial / 직전 완료 봉 목표 비중 100%; 다음 봉 시가 가정 |
| v2 | momentum_26 AND volume_26 | 9833.30 | -166.70 | sell / filled / 직전 완료 봉 목표 비중 0%; 다음 봉 시가 가정 |
| v2 | momentum_26 + volume_26 | 9720.94 | -279.06 | buy / filled / 직전 완료 봉 목표 비중 50%; 다음 봉 시가 가정 |
| v2 | breakout_8 AND reversion_12 | 10000.00 | 0.00 | 대기 /  / 새 신호 대기 |
| v2 | breakout_8 + reversion_12 | 9626.35 | -373.65 | sell / filled / 직전 완료 봉 목표 비중 50%; 다음 봉 시가 가정 |
| v2 | breakout_8 AND volume_26 | 9926.66 | -73.34 | sell / filled / 직전 완료 봉 목표 비중 0%; 다음 봉 시가 가정 |
| v2 | breakout_8 + volume_26 | 9570.88 | -429.12 | sell / filled / 직전 완료 봉 목표 비중 0%; 다음 봉 시가 가정 |
| v2 | reversion_12 AND volume_26 | 10051.38 | 51.38 | sell / filled / 직전 완료 봉 목표 비중 0%; 다음 봉 시가 가정 |
| v2 | reversion_12 + volume_26 | 9917.14 | -82.86 | sell / filled / 직전 완료 봉 목표 비중 50%; 다음 봉 시가 가정 |
| v2 | ema_12_26 | 9953.79 | -46.21 | buy / partial / EMA12 > EMA26; 조건 충족; EMA12=334.708, EMA26=334.451; 직전 완료 봉 목표를 다음 봉 시가에 모의 적용 |
| v2 | macd_12_26_9 | 9971.56 | -28.44 | sell / filled / MACD > 신호선 그리고 MACD > 0; 조건 미충족; MACD=1.87003, signal9=1.96381; 직전 완료 봉 목표를 다음 봉 시가에 모의 적용 |
| v2 | rsi_14_recovery | 10000.00 | 0.00 | 대기 /  / 새 신호 대기 |
| v2 | bollinger_20_reentry | 10000.00 | 0.00 | 대기 /  / 새 신호 대기 |
| v2 | donchian_20 | 9868.35 | -131.65 | sell / filled / 종가 > 현재 봉을 제외한 직전 20봉 최고가; 조건 미충족; close=343.037, prior_high20=344.4; 직전 완료 봉 목표를 다음 봉 시가에 모의 적용 |
| v2 | atr_14_breakout | 9882.97 | -117.03 | sell / filled / 종가 > 직전 종가 + 직전 ATR14 그리고 종가 > EMA26; 조건 미충족; close=342.515, threshold=344.598, prior_ATR14=1.50332, EMA26=336.975; 직전 완료 봉 목표를 다음 봉 시가에 모의 적용 |
| v2 | session_vwap | 9932.83 | -67.17 | sell / filled / 종가 > 뉴욕 거래일별 누적 전형가격 VWAP; 조건 미충족; close=342, session_VWAP=342.233, session_volume=3.25898e+06; 직전 완료 봉 목표를 다음 봉 시가에 모의 적용 |
| v2 | obv_20 | 10005.55 | 5.55 | sell / filled / OBV > OBV의 SMA20 그리고 종가 > EMA26; 조건 미충족; OBV=-1.38544e+07, OBV_SMA20=-1.10099e+07, close=341.625, EMA26=338.807; 직전 완료 봉 목표를 다음 봉 시가에 모의 적용 |
| v2 | stochastic_14_3_recovery | 10000.00 | 0.00 | 대기 /  / 새 신호 대기 |
| v2 | mfi_14_recovery | 10000.00 | 0.00 | 대기 /  / 새 신호 대기 |
| v2 | adx_14_trend | 9860.96 | -139.04 | buy / partial / Wilder ADX14 >= 25 그리고 +DI14 > -DI14; 조건 충족; ADX14=26.8739, plus_DI14=46.4083, minus_DI14=10.993; 직전 완료 봉 목표를 다음 봉 시가에 모의 적용 |
| v2 | aroon_25_trend | 9878.80 | -121.20 | buy / partial / Aroon25 Up > 70 그리고 Down < 30 (동률이면 최신 극값); 조건 충족; Aroon_up=100, Aroon_down=4; 직전 완료 봉 목표를 다음 봉 시가에 모의 적용 |
| v2 | cci_20_momentum | 10048.61 | 48.61 | sell / filled / CCI20 > 100 (전형가격·평균절대편차); 조건 미충족; CCI20=93.5627; 직전 완료 봉 목표를 다음 봉 시가에 모의 적용 |
| v2 | williams_14_recovery | 10000.00 | 0.00 | 대기 /  / 새 신호 대기 |
| v2 | cmf_20_accumulation | 9930.17 | -69.83 | sell / filled / Chaikin Money Flow20 > 0.1; 조건 미충족; CMF20=-0.14511, volume20=9.3038e+06; 직전 완료 봉 목표를 다음 봉 시가에 모의 적용 |
| v2 | chaikin_3_10 | 10005.55 | 5.55 | sell / filled / ADL의 EMA3 - EMA10 > 0 그리고 종가 > EMA26; 조건 미충족; Chaikin3_10=-655976, ADL=-7.91325e+06, close=341.625, EMA26=338.807; 직전 완료 봉 목표를 다음 봉 시가에 모의 적용 |
| v2 | roc_10_momentum | 9911.86 | -88.14 | sell / filled / 10봉 ROC > 1% 그리고 종가 > EMA26; 조건 미충족; ROC10_percent=-0.490038, close=340.901, EMA26=338.962; 직전 완료 봉 목표를 다음 봉 시가에 모의 적용 |
| v2 | trix_15_trend | 9953.79 | -46.21 | buy / partial / 15봉 삼중 EMA의 1봉 변화율 TRIX > 0 그리고 종가 > EMA26; 조건 충족; TRIX15_percent=0.00554135, close=335.52, EMA26=334.451; 직전 완료 봉 목표를 다음 봉 시가에 모의 적용 |
| v2 | keltner_20_breakout | 9945.00 | -55.00 | sell / filled / 종가 > EMA20 + 2 x Wilder ATR14; 조건 미충족; close=342, upper_Keltner=342.276, EMA20=339.397, ATR14=1.43933; 직전 완료 봉 목표를 다음 봉 시가에 모의 적용 |
| v2 | opening_range_30m | 9925.82 | -74.18 | sell / filled / 뉴욕 09:30·09:45 두 완료 봉 최고가를 10:00 이후 종가가 돌파; 조건 미충족; close=343.037, opening_high=343.75; 직전 완료 봉 목표를 다음 봉 시가에 모의 적용 |

### 같은 기간의 비용·노출 비교 (사후 연구)

| 전략 | 비용 전 | 비용 후 | 100% 보유 | 같은 평균 노출 보유 | 평균 노출 |
|---|---:|---:|---:|---:|---:|
| cash | 0.00% | 0.00% | -1.36% | -0.00% | 0.00% |
| buy_hold | -0.95% | -1.36% | -1.36% | -1.36% | 100.00% |
| trend_8_26 | 0.58% | -3.55% | -1.36% | -0.73% | 52.49% |
| momentum_26 | -2.47% | -9.19% | -1.36% | -0.65% | 46.98% |
| breakout_8 | -3.78% | -19.00% | -1.36% | -0.28% | 20.21% |
| reversion_12 | 4.23% | -10.40% | -1.36% | -0.38% | 27.03% |
| volume_26 | -0.11% | -6.20% | -1.36% | -0.10% | 6.82% |
| trend_8_26 AND momentum_26 | 0.67% | -4.27% | -1.36% | -0.57% | 41.21% |
| trend_8_26 + momentum_26 | -0.94% | -6.21% | -1.36% | -0.69% | 49.74% |
| trend_8_26 AND breakout_8 | -3.83% | -14.50% | -1.36% | -0.18% | 12.86% |
| trend_8_26 + breakout_8 | -1.61% | -11.42% | -1.36% | -0.50% | 36.36% |
| trend_8_26 AND reversion_12 | 2.42% | -4.23% | -1.36% | -0.10% | 7.09% |
| trend_8_26 + reversion_12 | 2.41% | -6.45% | -1.36% | -0.55% | 39.77% |
| trend_8_26 AND volume_26 | -0.58% | -4.67% | -1.36% | -0.06% | 4.20% |
| trend_8_26 + volume_26 | 0.26% | -4.88% | -1.36% | -0.41% | 29.66% |
| momentum_26 AND breakout_8 | -2.67% | -13.47% | -1.36% | -0.18% | 12.60% |
| momentum_26 + breakout_8 | -3.10% | -14.04% | -1.36% | -0.47% | 33.60% |
| momentum_26 AND reversion_12 | 2.49% | -4.58% | -1.36% | -0.08% | 6.04% |
| momentum_26 + reversion_12 | 0.85% | -8.27% | -1.36% | -0.51% | 37.01% |
| momentum_26 AND volume_26 | 0.21% | -2.70% | -1.36% | -0.04% | 2.89% |
| momentum_26 + volume_26 | -1.27% | -7.12% | -1.36% | -0.37% | 26.91% |
| breakout_8 AND reversion_12 | 0.00% | 0.00% | -1.36% | -0.00% | 0.00% |
| breakout_8 + reversion_12 | 0.16% | -13.37% | -1.36% | -0.33% | 23.63% |
| breakout_8 AND volume_26 | -0.51% | -2.17% | -1.36% | -0.01% | 1.05% |
| breakout_8 + volume_26 | -1.95% | -11.73% | -1.36% | -0.19% | 13.52% |
| reversion_12 AND volume_26 | 1.25% | -2.10% | -1.36% | -0.05% | 3.41% |
| reversion_12 + volume_26 | 2.05% | -7.55% | -1.36% | -0.24% | 16.93% |
| ema_12_26 | 0.24% | -3.07% | -1.36% | -0.68% | 48.82% |
| macd_12_26_9 | 0.83% | -3.32% | -1.36% | -0.43% | 30.97% |
| rsi_14_recovery | 0.14% | -2.35% | -1.36% | -0.02% | 1.57% |
| bollinger_20_reentry | 0.44% | -5.30% | -1.36% | -0.05% | 3.67% |
| donchian_20 | -1.79% | -4.63% | -1.36% | -0.04% | 2.89% |
| atr_14_breakout | -1.13% | -7.55% | -1.36% | -0.06% | 4.46% |
| session_vwap | 0.82% | -8.84% | -1.36% | -0.67% | 48.29% |
| obv_20 | -3.97% | -14.98% | -1.36% | -0.43% | 31.23% |
| stochastic_14_3_recovery | -1.86% | -12.75% | -1.36% | -0.10% | 7.35% |
| mfi_14_recovery | 0.16% | -1.50% | -1.36% | -0.01% | 1.05% |
| adx_14_trend | -2.98% | -6.19% | -1.36% | -0.39% | 28.08% |
| aroon_25_trend | -1.26% | -5.72% | -1.36% | -0.32% | 22.83% |
| cci_20_momentum | -2.59% | -10.44% | -1.36% | -0.21% | 15.22% |
| williams_14_recovery | -2.54% | -12.98% | -1.36% | -0.10% | 7.09% |
| cmf_20_accumulation | -3.12% | -11.67% | -1.36% | -0.48% | 34.38% |
| chaikin_3_10 | 1.36% | -7.19% | -1.36% | -0.47% | 33.86% |
| roc_10_momentum | -0.98% | -3.45% | -1.36% | -0.11% | 7.87% |
| trix_15_trend | -0.79% | -7.63% | -1.36% | -0.49% | 35.17% |
| keltner_20_breakout | -1.19% | -3.65% | -1.36% | -0.06% | 3.94% |
| opening_range_30m | -0.33% | -4.03% | -1.36% | -0.25% | 17.85% |

동일 구간·초기 자금, 종료 시 청산 비용 포함. 노출 맞춤은 사후 설명용이며 v2 실제 계좌 성과가 아닙니다.
[낙폭 분해·비용 영향·전체 구간](JPM/comparison.json)

[v1 전체 기록](JPM/accounts.json) · [v2 전체 기록](JPM/accounts-v2.json)

## XOM 계좌

| 모델 | 전략 | 평가액 USD | 손익 USD | 최근 매매·이유 |
|---|---|---:|---:|---|
| v1 | cash | 10000.00 | 0.00 | 대기 /  / 새 신호 대기 |
| v1 | buy_hold | 10031.77 | 31.77 | buy /  / buy_hold: prior completed bar target 100%; next bar open simulation |
| v1 | trend_8_26 | 10092.68 | 92.68 | buy /  / trend_8_26: prior completed bar target 100%; next bar open simulation |
| v1 | momentum_26 | 10059.42 | 59.42 | buy /  / momentum_26: prior completed bar target 100%; next bar open simulation |
| v1 | breakout_8 | 9861.76 | -138.24 | buy /  / breakout_8: prior completed bar target 100%; next bar open simulation |
| v1 | reversion_12 | 10000.00 | 0.00 | 대기 /  / 새 신호 대기 |
| v1 | volume_26 | 9889.56 | -110.44 | sell /  / volume_26: prior completed bar target 0%; next bar open simulation |
| v1 | trend_8_26 AND momentum_26 | 10092.68 | 92.68 | buy /  / trend_8_26 AND momentum_26: prior completed bar target 100%; next bar open simulation |
| v1 | trend_8_26 + momentum_26 | 10076.01 | 76.01 | buy /  / trend_8_26 + momentum_26: prior completed bar target 100%; next bar open simulation |
| v1 | trend_8_26 AND breakout_8 | 9983.50 | -16.50 | buy /  / trend_8_26 AND breakout_8: prior completed bar target 100%; next bar open simulation |
| v1 | trend_8_26 + breakout_8 | 9996.53 | -3.47 | buy /  / trend_8_26 + breakout_8: prior completed bar target 100%; next bar open simulation |
| v1 | trend_8_26 AND reversion_12 | 10000.00 | 0.00 | 대기 /  / 새 신호 대기 |
| v1 | trend_8_26 + reversion_12 | 10046.19 | 46.19 | sell /  / trend_8_26 + reversion_12: prior completed bar target 50%; next bar open simulation |
| v1 | trend_8_26 AND volume_26 | 9985.49 | -14.51 | sell /  / trend_8_26 AND volume_26: prior completed bar target 0%; next bar open simulation |
| v1 | trend_8_26 + volume_26 | 9990.55 | -9.45 | sell /  / trend_8_26 + volume_26: prior completed bar target 50%; next bar open simulation |
| v1 | momentum_26 AND breakout_8 | 9910.87 | -89.13 | buy /  / momentum_26 AND breakout_8: prior completed bar target 100%; next bar open simulation |
| v1 | momentum_26 + breakout_8 | 9960.12 | -39.88 | buy /  / momentum_26 + breakout_8: prior completed bar target 100%; next bar open simulation |
| v1 | momentum_26 AND reversion_12 | 10000.00 | 0.00 | 대기 /  / 새 신호 대기 |
| v1 | momentum_26 + reversion_12 | 10029.62 | 29.62 | sell /  / momentum_26 + reversion_12: prior completed bar target 50%; next bar open simulation |
| v1 | momentum_26 AND volume_26 | 9985.49 | -14.51 | sell /  / momentum_26 AND volume_26: prior completed bar target 0%; next bar open simulation |
| v1 | momentum_26 + volume_26 | 9974.08 | -25.92 | sell /  / momentum_26 + volume_26: prior completed bar target 50%; next bar open simulation |
| v1 | breakout_8 AND reversion_12 | 10000.00 | 0.00 | 대기 /  / 새 신호 대기 |
| v1 | breakout_8 + reversion_12 | 9930.59 | -69.41 | sell /  / breakout_8 + reversion_12: prior completed bar target 50%; next bar open simulation |
| v1 | breakout_8 AND volume_26 | 9950.44 | -49.56 | sell /  / breakout_8 AND volume_26: prior completed bar target 0%; next bar open simulation |
| v1 | breakout_8 + volume_26 | 9875.58 | -124.42 | sell /  / breakout_8 + volume_26: prior completed bar target 50%; next bar open simulation |
| v1 | reversion_12 AND volume_26 | 10000.00 | 0.00 | 대기 /  / 새 신호 대기 |
| v1 | reversion_12 + volume_26 | 9944.60 | -55.40 | sell /  / reversion_12 + volume_26: prior completed bar target 0%; next bar open simulation |
| v1 | ema_12_26 | 10089.80 | 89.80 | buy /  / EMA12 > EMA26; 조건 충족; EMA12=175.145, EMA26=175.141 |
| v1 | macd_12_26_9 | 10089.80 | 89.80 | buy /  / MACD > 신호선 그리고 MACD > 0; 조건 충족; MACD=0.00418876, signal9=-0.17046 |
| v1 | rsi_14_recovery | 10000.00 | 0.00 | 대기 /  / 새 신호 대기 |
| v1 | bollinger_20_reentry | 9913.52 | -86.48 | sell /  / 직전 종가 < 직전 하단밴드, 현재 하단밴드 <= 종가 <= SMA20 (한 봉 목표); 조건 미충족; close=175.71, lower20=173.907, SMA20=174.743, previous_lower20=173.977 |
| v1 | donchian_20 | 9950.44 | -49.56 | sell /  / 종가 > 현재 봉을 제외한 직전 20봉 최고가; 조건 미충족; close=175.56, prior_high20=177.365 |
| v1 | atr_14_breakout | 9864.96 | -135.04 | sell /  / 종가 > 직전 종가 + 직전 ATR14 그리고 종가 > EMA26; 조건 미충족; close=177.19, threshold=177.748, prior_ATR14=0.663113, EMA26=175.734 |
| v1 | session_vwap | 9990.86 | -9.14 | buy /  / 종가 > 뉴욕 거래일별 누적 전형가격 VWAP; 조건 충족; close=176.25, session_VWAP=175.945, session_volume=7.74672e+06 |
| v1 | obv_20 | 9970.37 | -29.63 | sell /  / OBV > OBV의 SMA20 그리고 종가 > EMA26; 조건 미충족; OBV=1.88162e+07, OBV_SMA20=2.13258e+07, close=175.84, EMA26=175.361 |
| v1 | stochastic_14_3_recovery | 10000.00 | 0.00 | 대기 /  / 새 신호 대기 |
| v1 | mfi_14_recovery | 10000.00 | 0.00 | 대기 /  / 새 신호 대기 |
| v1 | adx_14_trend | 10068.49 | 68.49 | buy /  / Wilder ADX14 >= 25 그리고 +DI14 > -DI14; 조건 충족; ADX14=25.0494, plus_DI14=28.5472, minus_DI14=15.0232 |
| v1 | aroon_25_trend | 10000.00 | 0.00 | 대기 /  / 새 신호 대기 |
| v1 | cci_20_momentum | 9923.86 | -76.14 | buy /  / CCI20 > 100 (전형가격·평균절대편차); 조건 충족; CCI20=102.776 |
| v1 | williams_14_recovery | 9913.52 | -86.48 | sell /  / 직전 Williams %R14 < -80, 현재 >= -80 (한 봉 목표); 조건 미충족; Williams_R14=-43.9575, previous_R14=-33.1215 |
| v1 | cmf_20_accumulation | 10000.00 | 0.00 | 대기 /  / 새 신호 대기 |
| v1 | chaikin_3_10 | 10000.00 | 0.00 | 대기 /  / 새 신호 대기 |
| v1 | roc_10_momentum | 9983.87 | -16.13 | sell /  / 10봉 ROC > 1% 그리고 종가 > EMA26; 조건 미충족; ROC10_percent=0.916121, close=176.25, EMA26=175.427 |
| v1 | trix_15_trend | 10042.87 | 42.87 | buy /  / 15봉 삼중 EMA의 1봉 변화율 TRIX > 0 그리고 종가 > EMA26; 조건 충족; TRIX15_percent=0.00176833, close=176.25, EMA26=175.427 |
| v1 | keltner_20_breakout | 9996.37 | -3.63 | buy /  / 종가 > EMA20 + 2 x Wilder ATR14; 조건 충족; close=177.085, upper_Keltner=177.035, EMA20=175.709, ATR14=0.663113 |
| v1 | opening_range_30m | 10000.00 | 0.00 | 대기 /  / 새 신호 대기 |
| v2 | cash | 10000.00 | 0.00 | 대기 /  / 새 신호 대기 |
| v2 | buy_hold | 10351.91 | 351.91 | buy / partial / 직전 완료 봉 목표 비중 100%; 다음 봉 시가 가정 |
| v2 | trend_8_26 | 10188.80 | 188.80 | buy / partial / 직전 완료 봉 목표 비중 100%; 다음 봉 시가 가정 |
| v2 | momentum_26 | 10232.06 | 232.06 | buy / partial / 직전 완료 봉 목표 비중 100%; 다음 봉 시가 가정 |
| v2 | breakout_8 | 9333.55 | -666.45 | buy / partial / 직전 완료 봉 목표 비중 100%; 다음 봉 시가 가정 |
| v2 | reversion_12 | 9815.06 | -184.94 | sell / filled / 직전 완료 봉 목표 비중 0%; 다음 봉 시가 가정 |
| v2 | volume_26 | 9794.70 | -205.30 | sell / filled / 직전 완료 봉 목표 비중 0%; 다음 봉 시가 가정 |
| v2 | trend_8_26 AND momentum_26 | 10196.36 | 196.36 | buy / partial / 직전 완료 봉 목표 비중 100%; 다음 봉 시가 가정 |
| v2 | trend_8_26 + momentum_26 | 10210.42 | 210.42 | buy / partial / 직전 완료 봉 목표 비중 100%; 다음 봉 시가 가정 |
| v2 | trend_8_26 AND breakout_8 | 9435.29 | -564.71 | buy / partial / 직전 완료 봉 목표 비중 100%; 다음 봉 시가 가정 |
| v2 | trend_8_26 + breakout_8 | 9793.23 | -206.77 | buy / partial / 직전 완료 봉 목표 비중 100%; 다음 봉 시가 가정 |
| v2 | trend_8_26 AND reversion_12 | 9839.70 | -160.30 | sell / filled / 직전 완료 봉 목표 비중 0%; 다음 봉 시가 가정 |
| v2 | trend_8_26 + reversion_12 | 10000.23 | 0.23 | sell / filled / 직전 완료 봉 목표 비중 50%; 다음 봉 시가 가정 |
| v2 | trend_8_26 AND volume_26 | 9879.28 | -120.72 | sell / filled / 직전 완료 봉 목표 비중 0%; 다음 봉 시가 가정 |
| v2 | trend_8_26 + volume_26 | 9989.71 | -10.29 | sell / filled / 직전 완료 봉 목표 비중 50%; 다음 봉 시가 가정 |
| v2 | momentum_26 AND breakout_8 | 9381.92 | -618.08 | buy / partial / 직전 완료 봉 목표 비중 100%; 다음 봉 시가 가정 |
| v2 | momentum_26 + breakout_8 | 9773.05 | -226.95 | buy / partial / 직전 완료 봉 목표 비중 100%; 다음 봉 시가 가정 |
| v2 | momentum_26 AND reversion_12 | 9800.13 | -199.87 | sell / filled / 직전 완료 봉 목표 비중 0%; 다음 봉 시가 가정 |
| v2 | momentum_26 + reversion_12 | 10021.47 | 21.47 | sell / filled / 직전 완료 봉 목표 비중 50%; 다음 봉 시가 가정 |
| v2 | momentum_26 AND volume_26 | 9941.52 | -58.48 | sell / filled / 직전 완료 봉 목표 비중 0%; 다음 봉 시가 가정 |
| v2 | momentum_26 + volume_26 | 10031.93 | 31.93 | sell / filled / 직전 완료 봉 목표 비중 50%; 다음 봉 시가 가정 |
| v2 | breakout_8 AND reversion_12 | 10000.00 | 0.00 | 대기 /  / 새 신호 대기 |
| v2 | breakout_8 + reversion_12 | 9571.14 | -428.86 | sell / filled / 직전 완료 봉 목표 비중 50%; 다음 봉 시가 가정 |
| v2 | breakout_8 AND volume_26 | 9918.86 | -81.14 | sell / filled / 직전 완료 봉 목표 비중 0%; 다음 봉 시가 가정 |
| v2 | breakout_8 + volume_26 | 9581.29 | -418.71 | sell / filled / 직전 완료 봉 목표 비중 50%; 다음 봉 시가 가정 |
| v2 | reversion_12 AND volume_26 | 9949.87 | -50.13 | sell / filled / 직전 완료 봉 목표 비중 0%; 다음 봉 시가 가정 |
| v2 | reversion_12 + volume_26 | 9825.48 | -174.52 | sell / filled / 직전 완료 봉 목표 비중 0%; 다음 봉 시가 가정 |
| v2 | ema_12_26 | 10088.79 | 88.79 | buy / partial / EMA12 > EMA26; 조건 충족; EMA12=175.145, EMA26=175.141; 직전 완료 봉 목표를 다음 봉 시가에 모의 적용 |
| v2 | macd_12_26_9 | 10088.79 | 88.79 | buy / partial / MACD > 신호선 그리고 MACD > 0; 조건 충족; MACD=0.00418876, signal9=-0.17046; 직전 완료 봉 목표를 다음 봉 시가에 모의 적용 |
| v2 | rsi_14_recovery | 10000.00 | 0.00 | 대기 /  / 새 신호 대기 |
| v2 | bollinger_20_reentry | 9911.54 | -88.46 | sell / filled / 직전 종가 < 직전 하단밴드, 현재 하단밴드 <= 종가 <= SMA20 (한 봉 목표); 조건 미충족; close=175.71, lower20=173.907, SMA20=174.743, previous_lower20=173.977; 직전 완료 봉 목표를 다음 봉 시가에 모의 적용 |
| v2 | donchian_20 | 9948.45 | -51.55 | sell / filled / 종가 > 현재 봉을 제외한 직전 20봉 최고가; 조건 미충족; close=175.56, prior_high20=177.365; 직전 완료 봉 목표를 다음 봉 시가에 모의 적용 |
| v2 | atr_14_breakout | 9859.04 | -140.96 | sell / filled / 종가 > 직전 종가 + 직전 ATR14 그리고 종가 > EMA26; 조건 미충족; close=177.19, threshold=177.748, prior_ATR14=0.663113, EMA26=175.734; 직전 완료 봉 목표를 다음 봉 시가에 모의 적용 |
| v2 | session_vwap | 9987.86 | -12.14 | buy / partial / 종가 > 뉴욕 거래일별 누적 전형가격 VWAP; 조건 충족; close=176.25, session_VWAP=175.945, session_volume=7.74672e+06; 직전 완료 봉 목표를 다음 봉 시가에 모의 적용 |
| v2 | obv_20 | 9968.37 | -31.63 | sell / filled / OBV > OBV의 SMA20 그리고 종가 > EMA26; 조건 미충족; OBV=1.88162e+07, OBV_SMA20=2.13258e+07, close=175.84, EMA26=175.361; 직전 완료 봉 목표를 다음 봉 시가에 모의 적용 |
| v2 | stochastic_14_3_recovery | 10000.00 | 0.00 | 대기 /  / 새 신호 대기 |
| v2 | mfi_14_recovery | 10000.00 | 0.00 | 대기 /  / 새 신호 대기 |
| v2 | adx_14_trend | 10067.48 | 67.48 | buy / partial / Wilder ADX14 >= 25 그리고 +DI14 > -DI14; 조건 충족; ADX14=25.0494, plus_DI14=28.5472, minus_DI14=15.0232; 직전 완료 봉 목표를 다음 봉 시가에 모의 적용 |
| v2 | aroon_25_trend | 10000.00 | 0.00 | 대기 /  / 새 신호 대기 |
| v2 | cci_20_momentum | 9918.90 | -81.10 | buy / partial / CCI20 > 100 (전형가격·평균절대편차); 조건 충족; CCI20=102.776; 직전 완료 봉 목표를 다음 봉 시가에 모의 적용 |
| v2 | williams_14_recovery | 9911.54 | -88.46 | sell / filled / 직전 Williams %R14 < -80, 현재 >= -80 (한 봉 목표); 조건 미충족; Williams_R14=-43.9575, previous_R14=-33.1215; 직전 완료 봉 목표를 다음 봉 시가에 모의 적용 |
| v2 | cmf_20_accumulation | 10000.00 | 0.00 | 대기 /  / 새 신호 대기 |
| v2 | chaikin_3_10 | 10000.00 | 0.00 | 대기 /  / 새 신호 대기 |
| v2 | roc_10_momentum | 9981.87 | -18.13 | sell / filled / 10봉 ROC > 1% 그리고 종가 > EMA26; 조건 미충족; ROC10_percent=0.916121, close=176.25, EMA26=175.427; 직전 완료 봉 목표를 다음 봉 시가에 모의 적용 |
| v2 | trix_15_trend | 10041.87 | 41.87 | buy / partial / 15봉 삼중 EMA의 1봉 변화율 TRIX > 0 그리고 종가 > EMA26; 조건 충족; TRIX15_percent=0.00176833, close=176.25, EMA26=175.427; 직전 완료 봉 목표를 다음 봉 시가에 모의 적용 |
| v2 | keltner_20_breakout | 9995.37 | -4.63 | buy / partial / 종가 > EMA20 + 2 x Wilder ATR14; 조건 충족; close=177.085, upper_Keltner=177.035, EMA20=175.709, ATR14=0.663113; 직전 완료 봉 목표를 다음 봉 시가에 모의 적용 |
| v2 | opening_range_30m | 10000.00 | 0.00 | 대기 /  / 새 신호 대기 |

### 같은 기간의 비용·노출 비교 (사후 연구)

| 전략 | 비용 전 | 비용 후 | 100% 보유 | 같은 평균 노출 보유 | 평균 노출 |
|---|---:|---:|---:|---:|---:|
| cash | 0.00% | 0.00% | 9.94% | 0.00% | 0.00% |
| buy_hold | 10.40% | 9.94% | 9.94% | 9.94% | 100.00% |
| trend_8_26 | 2.14% | -2.47% | 9.94% | 6.40% | 65.35% |
| momentum_26 | 1.02% | -6.34% | 9.94% | 6.99% | 71.13% |
| breakout_8 | -3.02% | -21.06% | 9.94% | 2.30% | 23.88% |
| reversion_12 | 7.01% | -3.65% | 9.94% | 2.00% | 20.73% |
| volume_26 | 4.19% | -3.80% | 9.94% | 0.50% | 5.25% |
| trend_8_26 AND momentum_26 | 0.67% | -4.28% | 9.94% | 5.88% | 60.10% |
| trend_8_26 + momentum_26 | 1.59% | -4.22% | 9.94% | 6.70% | 68.24% |
| trend_8_26 AND breakout_8 | -0.77% | -15.05% | 9.94% | 1.82% | 18.90% |
| trend_8_26 + breakout_8 | -0.45% | -11.87% | 9.94% | 4.34% | 44.63% |
| trend_8_26 AND reversion_12 | 1.89% | -3.93% | 9.94% | 0.78% | 8.14% |
| trend_8_26 + reversion_12 | 4.58% | -2.86% | 9.94% | 4.18% | 43.05% |
| trend_8_26 AND volume_26 | 2.80% | -1.84% | 9.94% | 0.28% | 2.89% |
| trend_8_26 + volume_26 | 3.18% | -2.73% | 9.94% | 3.42% | 35.31% |
| momentum_26 AND breakout_8 | -2.96% | -19.34% | 9.94% | 2.10% | 21.78% |
| momentum_26 + breakout_8 | -1.00% | -14.00% | 9.94% | 4.62% | 47.51% |
| momentum_26 AND reversion_12 | 2.27% | -4.38% | 9.94% | 0.86% | 8.92% |
| momentum_26 + reversion_12 | 4.00% | -3.60% | 9.94% | 4.47% | 45.94% |
| momentum_26 AND volume_26 | 2.58% | -1.64% | 9.94% | 0.25% | 2.62% |
| momentum_26 + volume_26 | 2.62% | -3.67% | 9.94% | 3.70% | 38.19% |
| breakout_8 AND reversion_12 | 0.00% | 0.00% | 9.94% | 0.00% | 0.00% |
| breakout_8 + reversion_12 | 1.89% | -12.61% | 9.94% | 2.15% | 22.32% |
| breakout_8 AND volume_26 | 0.51% | -1.17% | 9.94% | 0.10% | 1.05% |
| breakout_8 + volume_26 | 0.53% | -11.75% | 9.94% | 1.40% | 14.58% |
| reversion_12 AND volume_26 | 1.52% | -1.00% | 9.94% | 0.15% | 1.57% |
| reversion_12 + volume_26 | 5.61% | -2.91% | 9.94% | 1.25% | 13.00% |
| ema_12_26 | 0.63% | -2.70% | 9.94% | 7.36% | 74.80% |
| macd_12_26_9 | -0.48% | -6.16% | 9.94% | 3.95% | 40.68% |
| rsi_14_recovery | -0.15% | -0.57% | 9.94% | 0.03% | 0.26% |
| bollinger_20_reentry | -0.87% | -3.75% | 9.94% | 0.18% | 1.84% |
| donchian_20 | -1.09% | -9.82% | 9.94% | 0.86% | 8.92% |
| atr_14_breakout | -1.27% | -10.74% | 9.94% | 0.63% | 6.56% |
| session_vwap | -0.34% | -12.50% | 9.94% | 6.43% | 65.62% |
| obv_20 | 2.12% | -5.32% | 9.94% | 4.13% | 42.52% |
| stochastic_14_3_recovery | 1.55% | -6.63% | 9.94% | 0.50% | 5.25% |
| mfi_14_recovery | -0.31% | -1.97% | 9.94% | 0.10% | 1.05% |
| adx_14_trend | 1.73% | -1.22% | 9.94% | 4.16% | 42.78% |
| aroon_25_trend | -1.78% | -7.78% | 9.94% | 2.94% | 30.45% |
| cci_20_momentum | 3.31% | -4.62% | 9.94% | 2.63% | 27.30% |
| williams_14_recovery | 0.08% | -5.24% | 9.94% | 0.33% | 3.41% |
| cmf_20_accumulation | 2.06% | -6.17% | 9.94% | 4.96% | 50.92% |
| chaikin_3_10 | -1.00% | -9.36% | 9.94% | 5.38% | 55.12% |
| roc_10_momentum | 0.05% | -5.67% | 9.94% | 1.34% | 13.91% |
| trix_15_trend | -2.01% | -9.15% | 9.94% | 6.11% | 62.47% |
| keltner_20_breakout | -0.69% | -7.54% | 9.94% | 1.49% | 15.49% |
| opening_range_30m | -0.36% | -9.53% | 9.94% | 3.46% | 35.70% |

동일 구간·초기 자금, 종료 시 청산 비용 포함. 노출 맞춤은 사후 설명용이며 v2 실제 계좌 성과가 아닙니다.
[낙폭 분해·비용 영향·전체 구간](XOM/comparison.json)

[v1 전체 기록](XOM/accounts.json) · [v2 전체 기록](XOM/accounts-v2.json)

## JNJ 계좌

| 모델 | 전략 | 평가액 USD | 손익 USD | 최근 매매·이유 |
|---|---|---:|---:|---|
| v1 | cash | 10000.00 | 0.00 | 대기 /  / 새 신호 대기 |
| v1 | buy_hold | 9957.18 | -42.82 | buy /  / buy_hold: prior completed bar target 100%; next bar open simulation |
| v1 | trend_8_26 | 9911.41 | -88.59 | buy /  / trend_8_26: prior completed bar target 100%; next bar open simulation |
| v1 | momentum_26 | 10000.00 | 0.00 | 대기 /  / 새 신호 대기 |
| v1 | breakout_8 | 9822.10 | -177.90 | sell /  / breakout_8: prior completed bar target 0%; next bar open simulation |
| v1 | reversion_12 | 10007.51 | 7.51 | buy /  / reversion_12: prior completed bar target 100%; next bar open simulation |
| v1 | volume_26 | 9935.63 | -64.37 | sell /  / volume_26: prior completed bar target 0%; next bar open simulation |
| v1 | trend_8_26 AND momentum_26 | 10000.00 | 0.00 | 대기 /  / 새 신호 대기 |
| v1 | trend_8_26 + momentum_26 | 9955.57 | -44.43 | sell /  / trend_8_26 + momentum_26: prior completed bar target 50%; next bar open simulation |
| v1 | trend_8_26 AND breakout_8 | 9937.40 | -62.60 | sell /  / trend_8_26 AND breakout_8: prior completed bar target 0%; next bar open simulation |
| v1 | trend_8_26 + breakout_8 | 9866.62 | -133.38 | sell /  / trend_8_26 + breakout_8: prior completed bar target 50%; next bar open simulation |
| v1 | trend_8_26 AND reversion_12 | 10007.51 | 7.51 | buy /  / trend_8_26 AND reversion_12: prior completed bar target 100%; next bar open simulation |
| v1 | trend_8_26 + reversion_12 | 9959.31 | -40.69 | buy /  / trend_8_26 + reversion_12: prior completed bar target 100%; next bar open simulation |
| v1 | trend_8_26 AND volume_26 | 9935.63 | -64.37 | sell /  / trend_8_26 AND volume_26: prior completed bar target 0%; next bar open simulation |
| v1 | trend_8_26 + volume_26 | 9923.51 | -76.49 | sell /  / trend_8_26 + volume_26: prior completed bar target 50%; next bar open simulation |
| v1 | momentum_26 AND breakout_8 | 10000.00 | 0.00 | 대기 /  / 새 신호 대기 |
| v1 | momentum_26 + breakout_8 | 9910.61 | -89.39 | sell /  / momentum_26 + breakout_8: prior completed bar target 0%; next bar open simulation |
| v1 | momentum_26 AND reversion_12 | 10000.00 | 0.00 | 대기 /  / 새 신호 대기 |
| v1 | momentum_26 + reversion_12 | 10003.73 | 3.73 | sell /  / momentum_26 + reversion_12: prior completed bar target 50%; next bar open simulation |
| v1 | momentum_26 AND volume_26 | 10000.00 | 0.00 | 대기 /  / 새 신호 대기 |
| v1 | momentum_26 + volume_26 | 9967.75 | -32.25 | sell /  / momentum_26 + volume_26: prior completed bar target 0%; next bar open simulation |
| v1 | breakout_8 AND reversion_12 | 10000.00 | 0.00 | 대기 /  / 새 신호 대기 |
| v1 | breakout_8 + reversion_12 | 9914.31 | -85.69 | sell /  / breakout_8 + reversion_12: prior completed bar target 50%; next bar open simulation |
| v1 | breakout_8 AND volume_26 | 10000.00 | 0.00 | 대기 /  / 새 신호 대기 |
| v1 | breakout_8 + volume_26 | 9878.65 | -121.35 | sell /  / breakout_8 + volume_26: prior completed bar target 0%; next bar open simulation |
| v1 | reversion_12 AND volume_26 | 10000.00 | 0.00 | 대기 /  / 새 신호 대기 |
| v1 | reversion_12 + volume_26 | 9971.47 | -28.53 | sell /  / reversion_12 + volume_26: prior completed bar target 50%; next bar open simulation |
| v1 | ema_12_26 | 9910.83 | -89.17 | buy /  / EMA12 > EMA26; 조건 충족; EMA12=255.218, EMA26=255.146 |
| v1 | macd_12_26_9 | 9863.86 | -136.14 | sell /  / MACD > 신호선 그리고 MACD > 0; 조건 미충족; MACD=0.118609, signal9=0.188199 |
| v1 | rsi_14_recovery | 10000.00 | 0.00 | 대기 /  / 새 신호 대기 |
| v1 | bollinger_20_reentry | 10000.00 | 0.00 | 대기 /  / 새 신호 대기 |
| v1 | donchian_20 | 10000.00 | 0.00 | 대기 /  / 새 신호 대기 |
| v1 | atr_14_breakout | 9883.97 | -116.03 | sell /  / 종가 > 직전 종가 + 직전 ATR14 그리고 종가 > EMA26; 조건 미충족; close=256.72, threshold=258.136, prior_ATR14=1.3158, EMA26=255.146 |
| v1 | session_vwap | 9793.21 | -206.79 | sell /  / 종가 > 뉴욕 거래일별 누적 전형가격 VWAP; 조건 미충족; close=256.3, session_VWAP=256.491, session_volume=4.03125e+06 |
| v1 | obv_20 | 9900.11 | -99.89 | sell /  / OBV > OBV의 SMA20 그리고 종가 > EMA26; 조건 미충족; OBV=5.71591e+06, OBV_SMA20=4.69003e+06, close=255.08, EMA26=255.591 |
| v1 | stochastic_14_3_recovery | 9927.65 | -72.35 | sell /  / 직전 %K14 < 20에서 %K14가 %D3 상향 돌파 (한 봉 목표); 조건 미충족; K14=60.1505, D3=50.3645, previous_K14=74.7605, previous_D3=37.7141 |
| v1 | mfi_14_recovery | 10000.00 | 0.00 | 대기 /  / 새 신호 대기 |
| v1 | adx_14_trend | 9823.79 | -176.21 | sell /  / Wilder ADX14 >= 25 그리고 +DI14 > -DI14; 조건 미충족; ADX14=24.7842, plus_DI14=27.3963, minus_DI14=19.1477 |
| v1 | aroon_25_trend | 10000.00 | 0.00 | 대기 /  / 새 신호 대기 |
| v1 | cci_20_momentum | 9935.63 | -64.37 | sell /  / CCI20 > 100 (전형가격·평균절대편차); 조건 미충족; CCI20=62.9489 |
| v1 | williams_14_recovery | 9927.65 | -72.35 | sell /  / 직전 Williams %R14 < -80, 현재 >= -80 (한 봉 목표); 조건 미충족; Williams_R14=-39.8495, previous_R14=-25.2395 |
| v1 | cmf_20_accumulation | 10000.00 | 0.00 | 대기 /  / 새 신호 대기 |
| v1 | chaikin_3_10 | 10000.00 | 0.00 | 대기 /  / 새 신호 대기 |
| v1 | roc_10_momentum | 9816.66 | -183.34 | sell /  / 10봉 ROC > 1% 그리고 종가 > EMA26; 조건 미충족; ROC10_percent=-0.398319, close=255.08, EMA26=255.591 |
| v1 | trix_15_trend | 9889.12 | -110.88 | sell /  / 15봉 삼중 EMA의 1봉 변화율 TRIX > 0 그리고 종가 > EMA26; 조건 미충족; TRIX15_percent=0.00718077, close=255.08, EMA26=255.591 |
| v1 | keltner_20_breakout | 10000.00 | 0.00 | 대기 /  / 새 신호 대기 |
| v1 | opening_range_30m | 10000.00 | 0.00 | 대기 /  / 새 신호 대기 |
| v2 | cash | 10000.00 | 0.00 | 대기 /  / 새 신호 대기 |
| v2 | buy_hold | 9724.79 | -275.21 | 중단: 손실 한도 / buy / partial / 직전 완료 봉 목표 비중 100%; 다음 봉 시가 가정 |
| v2 | trend_8_26 | 9724.79 | -275.21 | 중단: 손실 한도 / buy / partial / 직전 완료 봉 목표 비중 100%; 다음 봉 시가 가정 |
| v2 | momentum_26 | 9724.79 | -275.21 | 중단: 손실 한도 / buy / partial / 직전 완료 봉 목표 비중 100%; 다음 봉 시가 가정 |
| v2 | breakout_8 | 9343.39 | -656.61 | 중단: 손실 한도 / sell / filled / 직전 완료 봉 목표 비중 0%; 다음 봉 시가 가정 |
| v2 | reversion_12 | 9696.45 | -303.55 | buy / partial / 직전 완료 봉 목표 비중 100%; 다음 봉 시가 가정 |
| v2 | volume_26 | 9726.38 | -273.62 | sell / filled / 직전 완료 봉 목표 비중 0%; 다음 봉 시가 가정 |
| v2 | trend_8_26 AND momentum_26 | 9724.79 | -275.21 | 중단: 손실 한도 / buy / partial / 직전 완료 봉 목표 비중 100%; 다음 봉 시가 가정 |
| v2 | trend_8_26 + momentum_26 | 9724.79 | -275.21 | 중단: 손실 한도 / buy / partial / 직전 완료 봉 목표 비중 100%; 다음 봉 시가 가정 |
| v2 | trend_8_26 AND breakout_8 | 9419.39 | -580.61 | 중단: 손실 한도 / sell / filled / 직전 완료 봉 목표 비중 0%; 다음 봉 시가 가정 |
| v2 | trend_8_26 + breakout_8 | 9438.87 | -561.13 | sell / filled / 직전 완료 봉 목표 비중 50%; 다음 봉 시가 가정 |
| v2 | trend_8_26 AND reversion_12 | 9984.58 | -15.42 | buy / partial / 직전 완료 봉 목표 비중 100%; 다음 봉 시가 가정 |
| v2 | trend_8_26 + reversion_12 | 9732.92 | -267.08 | 중단: 손실 한도 / sell / filled / 직전 완료 봉 목표 비중 0%; 다음 봉 시가 가정 |
| v2 | trend_8_26 AND volume_26 | 9805.21 | -194.79 | sell / filled / 직전 완료 봉 목표 비중 0%; 다음 봉 시가 가정 |
| v2 | trend_8_26 + volume_26 | 9835.47 | -164.53 | 중단: 손실 한도 / buy / filled / 직전 완료 봉 목표 비중 50%; 다음 봉 시가 가정 |
| v2 | momentum_26 AND breakout_8 | 9598.70 | -401.30 | sell / filled / 직전 완료 봉 목표 비중 0%; 다음 봉 시가 가정 |
| v2 | momentum_26 + breakout_8 | 9472.51 | -527.49 | sell / filled / 직전 완료 봉 목표 비중 0%; 다음 봉 시가 가정 |
| v2 | momentum_26 AND reversion_12 | 9938.87 | -61.13 | sell / filled / 직전 완료 봉 목표 비중 0%; 다음 봉 시가 가정 |
| v2 | momentum_26 + reversion_12 | 9732.92 | -267.08 | 중단: 손실 한도 / sell / filled / 직전 완료 봉 목표 비중 0%; 다음 봉 시가 가정 |
| v2 | momentum_26 AND volume_26 | 9920.93 | -79.07 | sell / filled / 직전 완료 봉 목표 비중 0%; 다음 봉 시가 가정 |
| v2 | momentum_26 + volume_26 | 9835.47 | -164.53 | 중단: 손실 한도 / buy / filled / 직전 완료 봉 목표 비중 50%; 다음 봉 시가 가정 |
| v2 | breakout_8 AND reversion_12 | 10000.00 | 0.00 | 대기 /  / 새 신호 대기 |
| v2 | breakout_8 + reversion_12 | 9495.64 | -504.36 | sell / filled / 직전 완료 봉 목표 비중 50%; 다음 봉 시가 가정 |
| v2 | breakout_8 AND volume_26 | 9814.17 | -185.83 | sell / filled / 직전 완료 봉 목표 비중 0%; 다음 봉 시가 가정 |
| v2 | breakout_8 + volume_26 | 9490.26 | -509.74 | sell / filled / 직전 완료 봉 목표 비중 0%; 다음 봉 시가 가정 |
| v2 | reversion_12 AND volume_26 | 9886.24 | -113.76 | sell / filled / 직전 완료 봉 목표 비중 0%; 다음 봉 시가 가정 |
| v2 | reversion_12 + volume_26 | 9732.04 | -267.96 | sell / filled / 직전 완료 봉 목표 비중 50%; 다음 봉 시가 가정 |
| v2 | ema_12_26 | 9909.84 | -90.16 | buy / partial / EMA12 > EMA26; 조건 충족; EMA12=255.218, EMA26=255.146; 직전 완료 봉 목표를 다음 봉 시가에 모의 적용 |
| v2 | macd_12_26_9 | 9861.89 | -138.11 | sell / filled / MACD > 신호선 그리고 MACD > 0; 조건 미충족; MACD=0.118609, signal9=0.188199; 직전 완료 봉 목표를 다음 봉 시가에 모의 적용 |
| v2 | rsi_14_recovery | 10000.00 | 0.00 | 대기 /  / 새 신호 대기 |
| v2 | bollinger_20_reentry | 10000.00 | 0.00 | 대기 /  / 새 신호 대기 |
| v2 | donchian_20 | 10000.00 | 0.00 | 대기 /  / 새 신호 대기 |
| v2 | atr_14_breakout | 9880.02 | -119.98 | sell / filled / 종가 > 직전 종가 + 직전 ATR14 그리고 종가 > EMA26; 조건 미충족; close=256.72, threshold=258.136, prior_ATR14=1.3158, EMA26=255.146; 직전 완료 봉 목표를 다음 봉 시가에 모의 적용 |
| v2 | session_vwap | 9787.34 | -212.66 | sell / filled / 종가 > 뉴욕 거래일별 누적 전형가격 VWAP; 조건 미충족; close=256.3, session_VWAP=256.491, session_volume=4.03125e+06; 직전 완료 봉 목표를 다음 봉 시가에 모의 적용 |
| v2 | obv_20 | 9898.13 | -101.87 | sell / filled / OBV > OBV의 SMA20 그리고 종가 > EMA26; 조건 미충족; OBV=5.71591e+06, OBV_SMA20=4.69003e+06, close=255.08, EMA26=255.591; 직전 완료 봉 목표를 다음 봉 시가에 모의 적용 |
| v2 | stochastic_14_3_recovery | 9925.66 | -74.34 | sell / filled / 직전 %K14 < 20에서 %K14가 %D3 상향 돌파 (한 봉 목표); 조건 미충족; K14=60.1505, D3=50.3645, previous_K14=74.7605, previous_D3=37.7141; 직전 완료 봉 목표를 다음 봉 시가에 모의 적용 |
| v2 | mfi_14_recovery | 10000.00 | 0.00 | 대기 /  / 새 신호 대기 |
| v2 | adx_14_trend | 9817.90 | -182.10 | sell / filled / Wilder ADX14 >= 25 그리고 +DI14 > -DI14; 조건 미충족; ADX14=24.7842, plus_DI14=27.3963, minus_DI14=19.1477; 직전 완료 봉 목표를 다음 봉 시가에 모의 적용 |
| v2 | aroon_25_trend | 10000.00 | 0.00 | 대기 /  / 새 신호 대기 |
| v2 | cci_20_momentum | 9933.64 | -66.36 | sell / filled / CCI20 > 100 (전형가격·평균절대편차); 조건 미충족; CCI20=62.9489; 직전 완료 봉 목표를 다음 봉 시가에 모의 적용 |
| v2 | williams_14_recovery | 9925.66 | -74.34 | sell / filled / 직전 Williams %R14 < -80, 현재 >= -80 (한 봉 목표); 조건 미충족; Williams_R14=-39.8495, previous_R14=-25.2395; 직전 완료 봉 목표를 다음 봉 시가에 모의 적용 |
| v2 | cmf_20_accumulation | 10000.00 | 0.00 | 대기 /  / 새 신호 대기 |
| v2 | chaikin_3_10 | 10000.00 | 0.00 | 대기 /  / 새 신호 대기 |
| v2 | roc_10_momentum | 9812.74 | -187.26 | sell / filled / 10봉 ROC > 1% 그리고 종가 > EMA26; 조건 미충족; ROC10_percent=-0.398319, close=255.08, EMA26=255.591; 직전 완료 봉 목표를 다음 봉 시가에 모의 적용 |
| v2 | trix_15_trend | 9887.15 | -112.85 | sell / filled / 15봉 삼중 EMA의 1봉 변화율 TRIX > 0 그리고 종가 > EMA26; 조건 미충족; TRIX15_percent=0.00718077, close=255.08, EMA26=255.591; 직전 완료 봉 목표를 다음 봉 시가에 모의 적용 |
| v2 | keltner_20_breakout | 10000.00 | 0.00 | 대기 /  / 새 신호 대기 |
| v2 | opening_range_30m | 10000.00 | 0.00 | 대기 /  / 새 신호 대기 |

### 같은 기간의 비용·노출 비교 (사후 연구)

| 전략 | 비용 전 | 비용 후 | 100% 보유 | 같은 평균 노출 보유 | 평균 노출 |
|---|---:|---:|---:|---:|---:|
| cash | 0.00% | 0.00% | -6.19% | -0.00% | 0.00% |
| buy_hold | -5.80% | -6.19% | -6.19% | -6.19% | 100.00% |
| trend_8_26 | 1.79% | -0.74% | -6.19% | -3.14% | 49.61% |
| momentum_26 | 0.96% | -2.38% | -6.19% | -3.01% | 47.51% |
| breakout_8 | -0.91% | -17.98% | -6.19% | -1.33% | 20.73% |
| reversion_12 | -7.53% | -16.05% | -6.19% | -1.93% | 30.18% |
| volume_26 | -0.78% | -7.23% | -6.19% | -0.42% | 6.56% |
| trend_8_26 AND momentum_26 | 2.35% | -0.62% | -6.19% | -2.77% | 43.57% |
| trend_8_26 + momentum_26 | 1.38% | -1.56% | -6.19% | -3.08% | 48.56% |
| trend_8_26 AND breakout_8 | 0.55% | -12.09% | -6.19% | -1.00% | 15.49% |
| trend_8_26 + breakout_8 | 0.46% | -9.75% | -6.19% | -2.24% | 35.18% |
| trend_8_26 AND reversion_12 | 0.97% | -2.77% | -6.19% | -0.39% | 6.04% |
| trend_8_26 + reversion_12 | -2.95% | -8.32% | -6.19% | -2.54% | 39.90% |
| trend_8_26 AND volume_26 | 1.34% | -1.19% | -6.19% | -0.12% | 1.84% |
| trend_8_26 + volume_26 | 0.53% | -3.83% | -6.19% | -1.80% | 28.09% |
| momentum_26 AND breakout_8 | 2.20% | -9.52% | -6.19% | -0.93% | 14.44% |
| momentum_26 + breakout_8 | 0.05% | -10.31% | -6.19% | -2.18% | 34.13% |
| momentum_26 AND reversion_12 | -0.60% | -3.89% | -6.19% | -0.44% | 6.82% |
| momentum_26 + reversion_12 | -3.35% | -8.89% | -6.19% | -2.47% | 38.85% |
| momentum_26 AND volume_26 | 1.57% | -0.12% | -6.19% | -0.09% | 1.31% |
| momentum_26 + volume_26 | 0.12% | -4.22% | -6.19% | -1.73% | 27.04% |
| breakout_8 AND reversion_12 | 0.00% | 0.00% | -6.19% | -0.00% | 0.00% |
| breakout_8 + reversion_12 | -4.26% | -16.50% | -6.19% | -1.63% | 25.47% |
| breakout_8 AND volume_26 | 0.00% | -1.66% | -6.19% | -0.09% | 1.31% |
| breakout_8 + volume_26 | -0.84% | -12.04% | -6.19% | -0.88% | 13.66% |
| reversion_12 AND volume_26 | -1.99% | -4.42% | -6.19% | -0.17% | 2.62% |
| reversion_12 + volume_26 | -4.20% | -11.00% | -6.19% | -1.18% | 18.38% |
| ema_12_26 | -0.68% | -2.74% | -6.19% | -2.88% | 45.41% |
| macd_12_26_9 | 5.35% | 2.72% | -6.19% | -1.90% | 29.66% |
| rsi_14_recovery | -1.69% | -6.92% | -6.19% | -0.22% | 3.41% |
| bollinger_20_reentry | -0.55% | -4.64% | -6.19% | -0.17% | 2.62% |
| donchian_20 | 1.17% | -6.59% | -6.19% | -0.47% | 7.35% |
| atr_14_breakout | 1.31% | -4.88% | -6.19% | -0.31% | 4.72% |
| session_vwap | 1.46% | -6.32% | -6.19% | -3.09% | 48.82% |
| obv_20 | -6.02% | -13.95% | -6.19% | -2.18% | 34.12% |
| stochastic_14_3_recovery | -1.40% | -13.80% | -6.19% | -0.54% | 8.40% |
| mfi_14_recovery | 0.33% | -0.93% | -6.19% | -0.05% | 0.79% |
| adx_14_trend | -2.56% | -7.35% | -6.19% | -2.00% | 31.23% |
| aroon_25_trend | 3.86% | -0.41% | -6.19% | -1.80% | 28.08% |
| cci_20_momentum | 0.94% | -6.01% | -6.19% | -1.53% | 23.88% |
| williams_14_recovery | -2.03% | -10.30% | -6.19% | -0.36% | 5.51% |
| cmf_20_accumulation | 2.25% | -1.95% | -6.19% | -1.90% | 29.66% |
| chaikin_3_10 | -3.43% | -7.79% | -6.19% | -2.24% | 35.17% |
| roc_10_momentum | -2.21% | -8.56% | -6.19% | -0.96% | 14.96% |
| trix_15_trend | -1.60% | -4.46% | -6.19% | -2.16% | 33.86% |
| keltner_20_breakout | 0.76% | -2.97% | -6.19% | -0.61% | 9.45% |
| opening_range_30m | 0.41% | -3.72% | -6.19% | -1.68% | 26.25% |

동일 구간·초기 자금, 종료 시 청산 비용 포함. 노출 맞춤은 사후 설명용이며 v2 실제 계좌 성과가 아닙니다.
[낙폭 분해·비용 영향·전체 구간](JNJ/comparison.json)

[v1 전체 기록](JNJ/accounts.json) · [v2 전체 기록](JNJ/accounts-v2.json)

## CAT 계좌

| 모델 | 전략 | 평가액 USD | 손익 USD | 최근 매매·이유 |
|---|---|---:|---:|---|
| v1 | cash | 10000.00 | 0.00 | 대기 /  / 새 신호 대기 |
| v1 | buy_hold | 10008.03 | 8.03 | buy /  / buy_hold: prior completed bar target 100%; next bar open simulation |
| v1 | trend_8_26 | 10008.03 | 8.03 | buy /  / trend_8_26: prior completed bar target 100%; next bar open simulation |
| v1 | momentum_26 | 9927.66 | -72.34 | buy /  / momentum_26: prior completed bar target 100%; next bar open simulation |
| v1 | breakout_8 | 9950.83 | -49.17 | sell /  / breakout_8: prior completed bar target 0%; next bar open simulation |
| v1 | reversion_12 | 9964.26 | -35.74 | sell /  / reversion_12: prior completed bar target 0%; next bar open simulation |
| v1 | volume_26 | 10000.00 | 0.00 | 대기 /  / 새 신호 대기 |
| v1 | trend_8_26 AND momentum_26 | 9927.66 | -72.34 | buy /  / trend_8_26 AND momentum_26: prior completed bar target 100%; next bar open simulation |
| v1 | trend_8_26 + momentum_26 | 9967.92 | -32.08 | buy /  / trend_8_26 + momentum_26: prior completed bar target 100%; next bar open simulation |
| v1 | trend_8_26 AND breakout_8 | 9950.83 | -49.17 | sell /  / trend_8_26 AND breakout_8: prior completed bar target 0%; next bar open simulation |
| v1 | trend_8_26 + breakout_8 | 9979.54 | -20.46 | sell /  / trend_8_26 + breakout_8: prior completed bar target 50%; next bar open simulation |
| v1 | trend_8_26 AND reversion_12 | 9964.26 | -35.74 | sell /  / trend_8_26 AND reversion_12: prior completed bar target 0%; next bar open simulation |
| v1 | trend_8_26 + reversion_12 | 9986.19 | -13.81 | sell /  / trend_8_26 + reversion_12: prior completed bar target 50%; next bar open simulation |
| v1 | trend_8_26 AND volume_26 | 10000.00 | 0.00 | 대기 /  / 새 신호 대기 |
| v1 | trend_8_26 + volume_26 | 10004.06 | 4.06 | sell /  / trend_8_26 + volume_26: prior completed bar target 50%; next bar open simulation |
| v1 | momentum_26 AND breakout_8 | 9950.83 | -49.17 | sell /  / momentum_26 AND breakout_8: prior completed bar target 0%; next bar open simulation |
| v1 | momentum_26 + breakout_8 | 9939.23 | -60.77 | sell /  / momentum_26 + breakout_8: prior completed bar target 50%; next bar open simulation |
| v1 | momentum_26 AND reversion_12 | 9964.26 | -35.74 | sell /  / momentum_26 AND reversion_12: prior completed bar target 0%; next bar open simulation |
| v1 | momentum_26 + reversion_12 | 9945.94 | -54.06 | sell /  / momentum_26 + reversion_12: prior completed bar target 50%; next bar open simulation |
| v1 | momentum_26 AND volume_26 | 10000.00 | 0.00 | 대기 /  / 새 신호 대기 |
| v1 | momentum_26 + volume_26 | 9963.73 | -36.27 | sell /  / momentum_26 + volume_26: prior completed bar target 50%; next bar open simulation |
| v1 | breakout_8 AND reversion_12 | 10000.00 | 0.00 | 대기 /  / 새 신호 대기 |
| v1 | breakout_8 + reversion_12 | 9957.50 | -42.50 | sell /  / breakout_8 + reversion_12: prior completed bar target 0%; next bar open simulation |
| v1 | breakout_8 AND volume_26 | 10000.00 | 0.00 | 대기 /  / 새 신호 대기 |
| v1 | breakout_8 + volume_26 | 9975.37 | -24.63 | sell /  / breakout_8 + volume_26: prior completed bar target 0%; next bar open simulation |
| v1 | reversion_12 AND volume_26 | 10000.00 | 0.00 | 대기 /  / 새 신호 대기 |
| v1 | reversion_12 + volume_26 | 9982.09 | -17.91 | sell /  / reversion_12 + volume_26: prior completed bar target 0%; next bar open simulation |
| v1 | ema_12_26 | 9927.66 | -72.34 | buy /  / EMA12 > EMA26; 조건 충족; EMA12=733.716, EMA26=733.7 |
| v1 | macd_12_26_9 | 9904.18 | -95.82 | sell /  / MACD > 신호선 그리고 MACD > 0; 조건 미충족; MACD=0.746548, signal9=0.752293 |
| v1 | rsi_14_recovery | 10000.00 | 0.00 | 대기 /  / 새 신호 대기 |
| v1 | bollinger_20_reentry | 10000.00 | 0.00 | 대기 /  / 새 신호 대기 |
| v1 | donchian_20 | 9950.83 | -49.17 | sell /  / 종가 > 현재 봉을 제외한 직전 20봉 최고가; 조건 미충족; close=739.81, prior_high20=742.28 |
| v1 | atr_14_breakout | 9950.83 | -49.17 | sell /  / 종가 > 직전 종가 + 직전 ATR14 그리고 종가 > EMA26; 조건 미충족; close=739.81, threshold=744.805, prior_ATR14=4.59507, EMA26=734.153 |
| v1 | session_vwap | 9915.16 | -84.84 | sell /  / 종가 > 뉴욕 거래일별 누적 전형가격 VWAP; 조건 미충족; close=737.92, session_VWAP=738.059, session_volume=992163 |
| v1 | obv_20 | 9915.48 | -84.52 | sell /  / OBV > OBV의 SMA20 그리고 종가 > EMA26; 조건 미충족; OBV=-4.43751e+06, OBV_SMA20=-4.40907e+06, close=737.92, EMA26=736.007 |
| v1 | stochastic_14_3_recovery | 10000.00 | 0.00 | 대기 /  / 새 신호 대기 |
| v1 | mfi_14_recovery | 10000.00 | 0.00 | 대기 /  / 새 신호 대기 |
| v1 | adx_14_trend | 10000.00 | 0.00 | 대기 /  / 새 신호 대기 |
| v1 | aroon_25_trend | 10031.15 | 31.15 | sell /  / Aroon25 Up > 70 그리고 Down < 30 (동률이면 최신 극값); 조건 미충족; Aroon_up=88, Aroon_down=48 |
| v1 | cci_20_momentum | 10024.78 | 24.78 | sell /  / CCI20 > 100 (전형가격·평균절대편차); 조건 미충족; CCI20=98.8062 |
| v1 | williams_14_recovery | 10000.00 | 0.00 | 대기 /  / 새 신호 대기 |
| v1 | cmf_20_accumulation | 9906.51 | -93.49 | sell /  / Chaikin Money Flow20 > 0.1; 조건 미충족; CMF20=-0.00238772, volume20=1.90174e+06 |
| v1 | chaikin_3_10 | 9807.72 | -192.28 | sell /  / ADL의 EMA3 - EMA10 > 0 그리고 종가 > EMA26; 조건 미충족; Chaikin3_10=-6402.02, ADL=-5.65083e+06, close=735.68, EMA26=735.983 |
| v1 | roc_10_momentum | 9963.13 | -36.87 | sell /  / 10봉 ROC > 1% 그리고 종가 > EMA26; 조건 미충족; ROC10_percent=-0.134597, close=734.53, EMA26=735.486 |
| v1 | trix_15_trend | 9801.06 | -198.94 | buy /  / 15봉 삼중 EMA의 1봉 변화율 TRIX > 0 그리고 종가 > EMA26; 조건 충족; TRIX15_percent=0.0217542, close=736.045, EMA26=735.987 |
| v1 | keltner_20_breakout | 10000.00 | 0.00 | 대기 /  / 새 신호 대기 |
| v1 | opening_range_30m | 10040.71 | 40.71 | sell /  / 뉴욕 09:30·09:45 두 완료 봉 최고가를 10:00 이후 종가가 돌파; 자료 부족·변동폭 또는 거래량 없음: 대기; close=740.21 |
| v2 | cash | 10000.00 | 0.00 | 대기 /  / 새 신호 대기 |
| v2 | buy_hold | 9204.13 | -795.87 | 중단: 손실 한도 / buy / partial / 직전 완료 봉 목표 비중 100%; 다음 봉 시가 가정 |
| v2 | trend_8_26 | 9931.69 | -68.31 | buy / partial / 직전 완료 봉 목표 비중 100%; 다음 봉 시가 가정 |
| v2 | momentum_26 | 9941.15 | -58.85 | buy / partial / 직전 완료 봉 목표 비중 100%; 다음 봉 시가 가정 |
| v2 | breakout_8 | 9772.76 | -227.24 | sell / filled / 직전 완료 봉 목표 비중 0%; 다음 봉 시가 가정 |
| v2 | reversion_12 | 9075.59 | -924.41 | 중단: 손실 한도 / buy / partial / 직전 완료 봉 목표 비중 100%; 다음 봉 시가 가정 |
| v2 | volume_26 | 9335.14 | -664.86 | 중단: 손실 한도 / buy / partial / 직전 완료 봉 목표 비중 100%; 다음 봉 시가 가정 |
| v2 | trend_8_26 AND momentum_26 | 9969.93 | -30.07 | buy / partial / 직전 완료 봉 목표 비중 100%; 다음 봉 시가 가정 |
| v2 | trend_8_26 + momentum_26 | 9936.58 | -63.42 | buy / partial / 직전 완료 봉 목표 비중 100%; 다음 봉 시가 가정 |
| v2 | trend_8_26 AND breakout_8 | 9866.70 | -133.30 | sell / filled / 직전 완료 봉 목표 비중 0%; 다음 봉 시가 가정 |
| v2 | trend_8_26 + breakout_8 | 9852.33 | -147.67 | sell / filled / 직전 완료 봉 목표 비중 50%; 다음 봉 시가 가정 |
| v2 | trend_8_26 AND reversion_12 | 9776.08 | -223.92 | sell / filled / 직전 완료 봉 목표 비중 0%; 다음 봉 시가 가정 |
| v2 | trend_8_26 + reversion_12 | 9609.51 | -390.49 | sell / filled / 직전 완료 봉 목표 비중 50%; 다음 봉 시가 가정 |
| v2 | trend_8_26 AND volume_26 | 10035.44 | 35.44 | sell / filled / 직전 완료 봉 목표 비중 0%; 다음 봉 시가 가정 |
| v2 | trend_8_26 + volume_26 | 9636.47 | -363.53 | sell / filled / 직전 완료 봉 목표 비중 50%; 다음 봉 시가 가정 |
| v2 | momentum_26 AND breakout_8 | 9926.39 | -73.61 | sell / filled / 직전 완료 봉 목표 비중 0%; 다음 봉 시가 가정 |
| v2 | momentum_26 + breakout_8 | 9856.78 | -143.22 | sell / filled / 직전 완료 봉 목표 비중 50%; 다음 봉 시가 가정 |
| v2 | momentum_26 AND reversion_12 | 9835.50 | -164.50 | sell / filled / 직전 완료 봉 목표 비중 0%; 다음 봉 시가 가정 |
| v2 | momentum_26 + reversion_12 | 9613.99 | -386.01 | sell / filled / 직전 완료 봉 목표 비중 50%; 다음 봉 시가 가정 |
| v2 | momentum_26 AND volume_26 | 10048.78 | 48.78 | sell / filled / 직전 완료 봉 목표 비중 0%; 다음 봉 시가 가정 |
| v2 | momentum_26 + volume_26 | 9661.25 | -338.75 | sell / filled / 직전 완료 봉 목표 비중 50%; 다음 봉 시가 가정 |
| v2 | breakout_8 AND reversion_12 | 10000.00 | 0.00 | 대기 /  / 새 신호 대기 |
| v2 | breakout_8 + reversion_12 | 9610.18 | -389.82 | 중단: 손실 한도 / sell / filled / 직전 완료 봉 목표 비중 0%; 다음 봉 시가 가정 |
| v2 | breakout_8 AND volume_26 | 9998.69 | -1.31 | sell / filled / 직전 완료 봉 목표 비중 0%; 다음 봉 시가 가정 |
| v2 | breakout_8 + volume_26 | 9579.25 | -420.75 | sell / filled / 직전 완료 봉 목표 비중 0%; 다음 봉 시가 가정 |
| v2 | reversion_12 AND volume_26 | 9270.56 | -729.44 | 중단: 손실 한도 / buy / partial / 직전 완료 봉 목표 비중 100%; 다음 봉 시가 가정 |
| v2 | reversion_12 + volume_26 | 9400.63 | -599.37 | 중단: 손실 한도 / sell / filled / 직전 완료 봉 목표 비중 50%; 다음 봉 시가 가정 |
| v2 | ema_12_26 | 9926.66 | -73.34 | buy / partial / EMA12 > EMA26; 조건 충족; EMA12=733.716, EMA26=733.7; 직전 완료 봉 목표를 다음 봉 시가에 모의 적용 |
| v2 | macd_12_26_9 | 9902.20 | -97.80 | sell / filled / MACD > 신호선 그리고 MACD > 0; 조건 미충족; MACD=0.746548, signal9=0.752293; 직전 완료 봉 목표를 다음 봉 시가에 모의 적용 |
| v2 | rsi_14_recovery | 10000.00 | 0.00 | 대기 /  / 새 신호 대기 |
| v2 | bollinger_20_reentry | 10000.00 | 0.00 | 대기 /  / 새 신호 대기 |
| v2 | donchian_20 | 9948.84 | -51.16 | sell / filled / 종가 > 현재 봉을 제외한 직전 20봉 최고가; 조건 미충족; close=739.81, prior_high20=742.28; 직전 완료 봉 목표를 다음 봉 시가에 모의 적용 |
| v2 | atr_14_breakout | 9948.84 | -51.16 | sell / filled / 종가 > 직전 종가 + 직전 ATR14 그리고 종가 > EMA26; 조건 미충족; close=739.81, threshold=744.805, prior_ATR14=4.59507, EMA26=734.153; 직전 완료 봉 목표를 다음 봉 시가에 모의 적용 |
| v2 | session_vwap | 9911.20 | -88.80 | sell / filled / 종가 > 뉴욕 거래일별 누적 전형가격 VWAP; 조건 미충족; close=737.92, session_VWAP=738.059, session_volume=992163; 직전 완료 봉 목표를 다음 봉 시가에 모의 적용 |
| v2 | obv_20 | 9911.52 | -88.48 | sell / filled / OBV > OBV의 SMA20 그리고 종가 > EMA26; 조건 미충족; OBV=-4.43751e+06, OBV_SMA20=-4.40907e+06, close=737.92, EMA26=736.007; 직전 완료 봉 목표를 다음 봉 시가에 모의 적용 |
| v2 | stochastic_14_3_recovery | 10000.00 | 0.00 | 대기 /  / 새 신호 대기 |
| v2 | mfi_14_recovery | 10000.00 | 0.00 | 대기 /  / 새 신호 대기 |
| v2 | adx_14_trend | 10000.00 | 0.00 | 대기 /  / 새 신호 대기 |
| v2 | aroon_25_trend | 10029.14 | 29.14 | sell / filled / Aroon25 Up > 70 그리고 Down < 30 (동률이면 최신 극값); 조건 미충족; Aroon_up=88, Aroon_down=48; 직전 완료 봉 목표를 다음 봉 시가에 모의 적용 |
| v2 | cci_20_momentum | 10022.77 | 22.77 | sell / filled / CCI20 > 100 (전형가격·평균절대편차); 조건 미충족; CCI20=98.8062; 직전 완료 봉 목표를 다음 봉 시가에 모의 적용 |
| v2 | williams_14_recovery | 10000.00 | 0.00 | 대기 /  / 새 신호 대기 |
| v2 | cmf_20_accumulation | 9904.53 | -95.47 | sell / filled / Chaikin Money Flow20 > 0.1; 조건 미충족; CMF20=-0.00238772, volume20=1.90174e+06; 직전 완료 봉 목표를 다음 봉 시가에 모의 적용 |
| v2 | chaikin_3_10 | 9803.80 | -196.20 | sell / filled / ADL의 EMA3 - EMA10 > 0 그리고 종가 > EMA26; 조건 미충족; Chaikin3_10=-6402.02, ADL=-5.65083e+06, close=735.68, EMA26=735.983; 직전 완료 봉 목표를 다음 봉 시가에 모의 적용 |
| v2 | roc_10_momentum | 9961.14 | -38.86 | sell / filled / 10봉 ROC > 1% 그리고 종가 > EMA26; 조건 미충족; ROC10_percent=-0.134597, close=734.53, EMA26=735.486; 직전 완료 봉 목표를 다음 봉 시가에 모의 적용 |
| v2 | trix_15_trend | 9796.16 | -203.84 | buy / partial / 15봉 삼중 EMA의 1봉 변화율 TRIX > 0 그리고 종가 > EMA26; 조건 충족; TRIX15_percent=0.0217542, close=736.045, EMA26=735.987; 직전 완료 봉 목표를 다음 봉 시가에 모의 적용 |
| v2 | keltner_20_breakout | 10000.00 | 0.00 | 대기 /  / 새 신호 대기 |
| v2 | opening_range_30m | 10038.70 | 38.70 | sell / filled / 뉴욕 09:30·09:45 두 완료 봉 최고가를 10:00 이후 종가가 돌파; 자료 부족·변동폭 또는 거래량 없음: 대기; close=740.21; 직전 완료 봉 목표를 다음 봉 시가에 모의 적용 |

### 같은 기간의 비용·노출 비교 (사후 연구)

| 전략 | 비용 전 | 비용 후 | 100% 보유 | 같은 평균 노출 보유 | 평균 노출 |
|---|---:|---:|---:|---:|---:|
| cash | 0.00% | 0.00% | -10.47% | -0.00% | 0.00% |
| buy_hold | -10.09% | -10.47% | -10.47% | -10.47% | 100.00% |
| trend_8_26 | -1.57% | -5.22% | -10.47% | -5.33% | 50.39% |
| momentum_26 | -4.45% | -10.28% | -10.47% | -5.16% | 48.82% |
| breakout_8 | -3.26% | -16.13% | -10.47% | -1.62% | 15.22% |
| reversion_12 | -3.47% | -15.61% | -10.47% | -2.79% | 26.25% |
| volume_26 | -2.95% | -10.02% | -10.47% | -0.87% | 8.14% |
| trend_8_26 AND momentum_26 | -1.76% | -6.59% | -10.47% | -4.56% | 43.04% |
| trend_8_26 + momentum_26 | -3.00% | -7.77% | -10.47% | -5.24% | 49.61% |
| trend_8_26 AND breakout_8 | -1.89% | -9.42% | -10.47% | -0.84% | 7.87% |
| trend_8_26 + breakout_8 | -2.38% | -10.63% | -10.47% | -3.48% | 32.81% |
| trend_8_26 AND reversion_12 | 1.22% | -5.75% | -10.47% | -0.81% | 7.61% |
| trend_8_26 + reversion_12 | -2.46% | -9.97% | -10.47% | -4.06% | 38.33% |
| trend_8_26 AND volume_26 | 2.22% | -0.75% | -10.47% | -0.28% | 2.62% |
| trend_8_26 + volume_26 | -2.21% | -7.43% | -10.47% | -3.11% | 29.27% |
| momentum_26 AND breakout_8 | -2.81% | -11.02% | -10.47% | -0.92% | 8.66% |
| momentum_26 + breakout_8 | -3.82% | -13.23% | -10.47% | -3.40% | 32.03% |
| momentum_26 AND reversion_12 | -2.61% | -9.32% | -10.47% | -0.67% | 6.30% |
| momentum_26 + reversion_12 | -3.91% | -12.05% | -10.47% | -3.98% | 37.54% |
| momentum_26 AND volume_26 | 1.58% | -0.53% | -10.47% | -0.17% | 1.57% |
| momentum_26 + volume_26 | -3.64% | -9.37% | -10.47% | -3.02% | 28.48% |
| breakout_8 AND reversion_12 | 0.00% | 0.00% | -10.47% | -0.00% | 0.00% |
| breakout_8 + reversion_12 | -3.31% | -14.97% | -10.47% | -2.20% | 20.74% |
| breakout_8 AND volume_26 | 0.37% | -0.47% | -10.47% | -0.06% | 0.52% |
| breakout_8 + volume_26 | -3.07% | -12.38% | -10.47% | -1.24% | 11.69% |
| reversion_12 AND volume_26 | -1.25% | -5.71% | -10.47% | -0.56% | 5.25% |
| reversion_12 + volume_26 | -3.17% | -12.11% | -10.47% | -1.83% | 17.20% |
| ema_12_26 | -1.01% | -3.06% | -10.47% | -5.30% | 50.13% |
| macd_12_26_9 | -0.77% | -4.85% | -10.47% | -3.29% | 30.97% |
| rsi_14_recovery | -0.96% | -6.22% | -10.47% | -0.36% | 3.41% |
| bollinger_20_reentry | 1.35% | -4.43% | -10.47% | -0.39% | 3.67% |
| donchian_20 | -2.30% | -7.11% | -10.47% | -0.56% | 5.25% |
| atr_14_breakout | -2.42% | -9.14% | -10.47% | -0.50% | 4.72% |
| session_vwap | -0.26% | -12.07% | -10.47% | -4.89% | 46.19% |
| obv_20 | -4.09% | -14.37% | -10.47% | -2.87% | 27.03% |
| stochastic_14_3_recovery | -3.21% | -13.22% | -10.47% | -0.73% | 6.82% |
| mfi_14_recovery | 0.45% | -1.63% | -10.47% | -0.14% | 1.31% |
| adx_14_trend | -3.13% | -5.93% | -10.47% | -1.01% | 9.45% |
| aroon_25_trend | -2.12% | -6.14% | -10.47% | -1.56% | 14.70% |
| cci_20_momentum | -5.69% | -11.82% | -10.47% | -1.73% | 16.27% |
| williams_14_recovery | -1.60% | -10.66% | -10.47% | -0.64% | 6.04% |
| cmf_20_accumulation | -5.76% | -12.26% | -10.47% | -1.93% | 18.11% |
| chaikin_3_10 | -6.23% | -14.87% | -10.47% | -3.73% | 35.17% |
| roc_10_momentum | -1.82% | -7.81% | -10.47% | -1.42% | 13.39% |
| trix_15_trend | -1.25% | -6.10% | -10.47% | -4.17% | 39.37% |
| keltner_20_breakout | -3.35% | -6.15% | -10.47% | -0.31% | 2.89% |
| opening_range_30m | 4.95% | -0.21% | -10.47% | -2.18% | 20.47% |

동일 구간·초기 자금, 종료 시 청산 비용 포함. 노출 맞춤은 사후 설명용이며 v2 실제 계좌 성과가 아닙니다.
[낙폭 분해·비용 영향·전체 구간](CAT/comparison.json)

[v1 전체 기록](CAT/accounts.json) · [v2 전체 기록](CAT/accounts-v2.json)

## WMT 계좌

| 모델 | 전략 | 평가액 USD | 손익 USD | 최근 매매·이유 |
|---|---|---:|---:|---|
| v1 | cash | 10000.00 | 0.00 | 대기 /  / 새 신호 대기 |
| v1 | buy_hold | 10028.18 | 28.18 | buy /  / buy_hold: prior completed bar target 100%; next bar open simulation |
| v1 | trend_8_26 | 9974.57 | -25.43 | buy /  / trend_8_26: prior completed bar target 100%; next bar open simulation |
| v1 | momentum_26 | 10043.97 | 43.97 | sell /  / momentum_26: prior completed bar target 0%; next bar open simulation |
| v1 | breakout_8 | 9953.51 | -46.49 | sell /  / breakout_8: prior completed bar target 0%; next bar open simulation |
| v1 | reversion_12 | 10043.97 | 43.97 | sell /  / reversion_12: prior completed bar target 0%; next bar open simulation |
| v1 | volume_26 | 9979.72 | -20.28 | sell /  / volume_26: prior completed bar target 0%; next bar open simulation |
| v1 | trend_8_26 AND momentum_26 | 10000.00 | 0.00 | 대기 /  / 새 신호 대기 |
| v1 | trend_8_26 + momentum_26 | 10009.24 | 9.24 | sell /  / trend_8_26 + momentum_26: prior completed bar target 50%; next bar open simulation |
| v1 | trend_8_26 AND breakout_8 | 10000.00 | 0.00 | 대기 /  / 새 신호 대기 |
| v1 | trend_8_26 + breakout_8 | 9964.00 | -36.00 | sell /  / trend_8_26 + breakout_8: prior completed bar target 50%; next bar open simulation |
| v1 | trend_8_26 AND reversion_12 | 10000.00 | 0.00 | 대기 /  / 새 신호 대기 |
| v1 | trend_8_26 + reversion_12 | 10009.24 | 9.24 | sell /  / trend_8_26 + reversion_12: prior completed bar target 50%; next bar open simulation |
| v1 | trend_8_26 AND volume_26 | 10000.00 | 0.00 | 대기 /  / 새 신호 대기 |
| v1 | trend_8_26 + volume_26 | 9977.09 | -22.91 | sell /  / trend_8_26 + volume_26: prior completed bar target 50%; next bar open simulation |
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
| v1 | ema_12_26 | 10028.18 | 28.18 | buy /  / EMA12 > EMA26; 조건 충족; EMA12=118.245, EMA26=118.045 |
| v1 | macd_12_26_9 | 10000.00 | 0.00 | 대기 /  / 새 신호 대기 |
| v1 | rsi_14_recovery | 10000.00 | 0.00 | 대기 /  / 새 신호 대기 |
| v1 | bollinger_20_reentry | 10000.00 | 0.00 | 대기 /  / 새 신호 대기 |
| v1 | donchian_20 | 10000.00 | 0.00 | 대기 /  / 새 신호 대기 |
| v1 | atr_14_breakout | 9979.72 | -20.28 | sell /  / 종가 > 직전 종가 + 직전 ATR14 그리고 종가 > EMA26; 조건 미충족; close=119.375, threshold=119.607, prior_ATR14=0.486823, EMA26=118.217 |
| v1 | session_vwap | 9839.22 | -160.78 | sell /  / 종가 > 뉴욕 거래일별 누적 전형가격 VWAP; 조건 미충족; close=118.745, session_VWAP=118.899, session_volume=6.77102e+06 |
| v1 | obv_20 | 9987.60 | -12.40 | buy /  / OBV > OBV의 SMA20 그리고 종가 > EMA26; 조건 충족; OBV=1.97077e+07, OBV_SMA20=1.95583e+07, close=118.63, EMA26=118.481 |
| v1 | stochastic_14_3_recovery | 9979.72 | -20.28 | sell /  / 직전 %K14 < 20에서 %K14가 %D3 상향 돌파 (한 봉 목표); 조건 미충족; K14=93.8952, D3=60.8222, previous_K14=82.4242, previous_D3=34.5012 |
| v1 | mfi_14_recovery | 10000.00 | 0.00 | 대기 /  / 새 신호 대기 |
| v1 | adx_14_trend | 9991.69 | -8.31 | sell /  / Wilder ADX14 >= 25 그리고 +DI14 > -DI14; 조건 미충족; ADX14=24.5142, plus_DI14=24.7537, minus_DI14=21.6519 |
| v1 | aroon_25_trend | 10000.00 | 0.00 | 대기 /  / 새 신호 대기 |
| v1 | cci_20_momentum | 9932.96 | -67.04 | sell /  / CCI20 > 100 (전형가격·평균절대편차); 조건 미충족; CCI20=99.1325 |
| v1 | williams_14_recovery | 9979.72 | -20.28 | sell /  / 직전 Williams %R14 < -80, 현재 >= -80 (한 봉 목표); 조건 미충족; Williams_R14=-6.10484, previous_R14=-17.5758 |
| v1 | cmf_20_accumulation | 10000.00 | 0.00 | 대기 /  / 새 신호 대기 |
| v1 | chaikin_3_10 | 9804.75 | -195.25 | buy /  / ADL의 EMA3 - EMA10 > 0 그리고 종가 > EMA26; 조건 충족; Chaikin3_10=85268.3, ADL=1.95276e+07, close=118.535, EMA26=118.469 |
| v1 | roc_10_momentum | 10000.00 | 0.00 | 대기 /  / 새 신호 대기 |
| v1 | trix_15_trend | 9894.28 | -105.72 | buy /  / 15봉 삼중 EMA의 1봉 변화율 TRIX > 0 그리고 종가 > EMA26; 조건 충족; TRIX15_percent=0.026499, close=118.535, EMA26=118.469 |
| v1 | keltner_20_breakout | 10000.00 | 0.00 | 대기 /  / 새 신호 대기 |
| v1 | opening_range_30m | 10000.00 | 0.00 | 대기 /  / 새 신호 대기 |
| v2 | cash | 10000.00 | 0.00 | 대기 /  / 새 신호 대기 |
| v2 | buy_hold | 10624.76 | 624.76 | buy / partial / 직전 완료 봉 목표 비중 100%; 다음 봉 시가 가정 |
| v2 | trend_8_26 | 10383.11 | 383.11 | buy / partial / 직전 완료 봉 목표 비중 100%; 다음 봉 시가 가정 |
| v2 | momentum_26 | 10465.54 | 465.54 | sell / filled / 직전 완료 봉 목표 비중 0%; 다음 봉 시가 가정 |
| v2 | breakout_8 | 9916.34 | -83.66 | sell / filled / 직전 완료 봉 목표 비중 0%; 다음 봉 시가 가정 |
| v2 | reversion_12 | 9953.01 | -46.99 | sell / filled / 직전 완료 봉 목표 비중 0%; 다음 봉 시가 가정 |
| v2 | volume_26 | 9943.08 | -56.92 | sell / filled / 직전 완료 봉 목표 비중 0%; 다음 봉 시가 가정 |
| v2 | trend_8_26 AND momentum_26 | 10410.62 | 410.62 | sell / filled / 직전 완료 봉 목표 비중 0%; 다음 봉 시가 가정 |
| v2 | trend_8_26 + momentum_26 | 10424.22 | 424.22 | sell / filled / 직전 완료 봉 목표 비중 50%; 다음 봉 시가 가정 |
| v2 | trend_8_26 AND breakout_8 | 10088.55 | 88.55 | sell / filled / 직전 완료 봉 목표 비중 0%; 다음 봉 시가 가정 |
| v2 | trend_8_26 + breakout_8 | 10147.41 | 147.41 | sell / filled / 직전 완료 봉 목표 비중 50%; 다음 봉 시가 가정 |
| v2 | trend_8_26 AND reversion_12 | 9808.74 | -191.26 | sell / filled / 직전 완료 봉 목표 비중 0%; 다음 봉 시가 가정 |
| v2 | trend_8_26 + reversion_12 | 10167.26 | 167.26 | sell / filled / 직전 완료 봉 목표 비중 50%; 다음 봉 시가 가정 |
| v2 | trend_8_26 AND volume_26 | 9949.23 | -50.77 | sell / filled / 직전 완료 봉 목표 비중 0%; 다음 봉 시가 가정 |
| v2 | trend_8_26 + volume_26 | 10162.11 | 162.11 | sell / filled / 직전 완료 봉 목표 비중 50%; 다음 봉 시가 가정 |
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
| v2 | ema_12_26 | 10027.18 | 27.18 | buy / partial / EMA12 > EMA26; 조건 충족; EMA12=118.245, EMA26=118.045; 직전 완료 봉 목표를 다음 봉 시가에 모의 적용 |
| v2 | macd_12_26_9 | 10000.00 | 0.00 | 대기 /  / 새 신호 대기 |
| v2 | rsi_14_recovery | 10000.00 | 0.00 | 대기 /  / 새 신호 대기 |
| v2 | bollinger_20_reentry | 10000.00 | 0.00 | 대기 /  / 새 신호 대기 |
| v2 | donchian_20 | 10000.00 | 0.00 | 대기 /  / 새 신호 대기 |
| v2 | atr_14_breakout | 9977.72 | -22.28 | sell / filled / 종가 > 직전 종가 + 직전 ATR14 그리고 종가 > EMA26; 조건 미충족; close=119.375, threshold=119.607, prior_ATR14=0.486823, EMA26=118.217; 직전 완료 봉 목표를 다음 봉 시가에 모의 적용 |
| v2 | session_vwap | 9835.28 | -164.72 | sell / filled / 종가 > 뉴욕 거래일별 누적 전형가격 VWAP; 조건 미충족; close=118.745, session_VWAP=118.899, session_volume=6.77102e+06; 직전 완료 봉 목표를 다음 봉 시가에 모의 적용 |
| v2 | obv_20 | 9986.60 | -13.40 | buy / partial / OBV > OBV의 SMA20 그리고 종가 > EMA26; 조건 충족; OBV=1.97077e+07, OBV_SMA20=1.95583e+07, close=118.63, EMA26=118.481; 직전 완료 봉 목표를 다음 봉 시가에 모의 적용 |
| v2 | stochastic_14_3_recovery | 9977.72 | -22.28 | sell / filled / 직전 %K14 < 20에서 %K14가 %D3 상향 돌파 (한 봉 목표); 조건 미충족; K14=93.8952, D3=60.8222, previous_K14=82.4242, previous_D3=34.5012; 직전 완료 봉 목표를 다음 봉 시가에 모의 적용 |
| v2 | mfi_14_recovery | 10000.00 | 0.00 | 대기 /  / 새 신호 대기 |
| v2 | adx_14_trend | 9989.70 | -10.30 | sell / filled / Wilder ADX14 >= 25 그리고 +DI14 > -DI14; 조건 미충족; ADX14=24.5142, plus_DI14=24.7537, minus_DI14=21.6519; 직전 완료 봉 목표를 다음 봉 시가에 모의 적용 |
| v2 | aroon_25_trend | 10000.00 | 0.00 | 대기 /  / 새 신호 대기 |
| v2 | cci_20_momentum | 9930.98 | -69.02 | sell / filled / CCI20 > 100 (전형가격·평균절대편차); 조건 미충족; CCI20=99.1325; 직전 완료 봉 목표를 다음 봉 시가에 모의 적용 |
| v2 | williams_14_recovery | 9977.72 | -22.28 | sell / filled / 직전 Williams %R14 < -80, 현재 >= -80 (한 봉 목표); 조건 미충족; Williams_R14=-6.10484, previous_R14=-17.5758; 직전 완료 봉 목표를 다음 봉 시가에 모의 적용 |
| v2 | cmf_20_accumulation | 10000.00 | 0.00 | 대기 /  / 새 신호 대기 |
| v2 | chaikin_3_10 | 9799.85 | -200.15 | buy / partial / ADL의 EMA3 - EMA10 > 0 그리고 종가 > EMA26; 조건 충족; Chaikin3_10=85268.3, ADL=1.95276e+07, close=118.535, EMA26=118.469; 직전 완료 봉 목표를 다음 봉 시가에 모의 적용 |
| v2 | roc_10_momentum | 10000.00 | 0.00 | 대기 /  / 새 신호 대기 |
| v2 | trix_15_trend | 9891.31 | -108.69 | buy / partial / 15봉 삼중 EMA의 1봉 변화율 TRIX > 0 그리고 종가 > EMA26; 조건 충족; TRIX15_percent=0.026499, close=118.535, EMA26=118.469; 직전 완료 봉 목표를 다음 봉 시가에 모의 적용 |
| v2 | keltner_20_breakout | 10000.00 | 0.00 | 대기 /  / 새 신호 대기 |
| v2 | opening_range_30m | 10000.00 | 0.00 | 대기 /  / 새 신호 대기 |

### 같은 기간의 비용·노출 비교 (사후 연구)

| 전략 | 비용 전 | 비용 후 | 100% 보유 | 같은 평균 노출 보유 | 평균 노출 |
|---|---:|---:|---:|---:|---:|
| cash | 0.00% | 0.00% | 9.59% | 0.00% | 0.00% |
| buy_hold | 10.05% | 9.59% | 9.59% | 9.59% | 100.00% |
| trend_8_26 | 9.33% | 6.17% | 9.59% | 6.65% | 69.55% |
| momentum_26 | 7.43% | 3.45% | 9.59% | 6.65% | 69.55% |
| breakout_8 | 5.45% | -11.60% | 9.59% | 2.52% | 26.51% |
| reversion_12 | 4.02% | -5.96% | 9.59% | 1.59% | 16.80% |
| volume_26 | -0.20% | -5.50% | 9.59% | 0.52% | 5.51% |
| trend_8_26 AND momentum_26 | 8.87% | 4.83% | 9.59% | 6.01% | 62.99% |
| trend_8_26 + momentum_26 | 8.39% | 4.80% | 9.59% | 6.65% | 69.56% |
| trend_8_26 AND breakout_8 | 6.92% | -6.91% | 9.59% | 2.12% | 22.31% |
| trend_8_26 + breakout_8 | 7.39% | -3.11% | 9.59% | 4.58% | 48.04% |
| trend_8_26 AND reversion_12 | 0.42% | -4.91% | 9.59% | 0.65% | 6.82% |
| trend_8_26 + reversion_12 | 6.68% | 0.14% | 9.59% | 4.11% | 43.18% |
| trend_8_26 AND volume_26 | 1.13% | -1.39% | 9.59% | 0.20% | 2.10% |
| trend_8_26 + volume_26 | 4.50% | 0.60% | 9.59% | 3.57% | 37.54% |
| momentum_26 AND breakout_8 | 5.58% | -8.47% | 9.59% | 2.22% | 23.36% |
| momentum_26 + breakout_8 | 6.45% | -3.96% | 9.59% | 4.58% | 48.04% |
| momentum_26 AND reversion_12 | 1.36% | -4.43% | 9.59% | 0.72% | 7.61% |
| momentum_26 + reversion_12 | 5.75% | 0.53% | 9.59% | 4.11% | 43.18% |
| momentum_26 AND volume_26 | 0.44% | -3.69% | 9.59% | 0.27% | 2.89% |
| momentum_26 + volume_26 | 3.58% | -0.91% | 9.59% | 3.57% | 37.54% |
| breakout_8 AND reversion_12 | 0.00% | 0.00% | 9.59% | 0.00% | 0.00% |
| breakout_8 + reversion_12 | 4.76% | -8.24% | 9.59% | 2.06% | 21.66% |
| breakout_8 AND volume_26 | 1.29% | -0.82% | 9.59% | 0.15% | 1.57% |
| breakout_8 + volume_26 | 2.62% | -7.82% | 9.59% | 1.52% | 16.02% |
| reversion_12 AND volume_26 | -0.51% | -2.99% | 9.59% | 0.22% | 2.36% |
| reversion_12 + volume_26 | 1.90% | -5.33% | 9.59% | 1.06% | 11.16% |
| ema_12_26 | 9.18% | 7.81% | 9.59% | 6.62% | 69.29% |
| macd_12_26_9 | 8.10% | 4.53% | 9.59% | 3.42% | 35.96% |
| rsi_14_recovery | -0.68% | -2.74% | 9.59% | 0.12% | 1.31% |
| bollinger_20_reentry | 0.93% | -2.41% | 9.59% | 0.20% | 2.10% |
| donchian_20 | 4.64% | -8.52% | 9.59% | 1.34% | 14.17% |
| atr_14_breakout | -0.51% | -10.81% | 9.59% | 0.77% | 8.14% |
| session_vwap | 7.22% | -3.06% | 9.59% | 5.71% | 59.84% |
| obv_20 | 8.25% | 0.37% | 9.59% | 5.31% | 55.64% |
| stochastic_14_3_recovery | 1.43% | -9.06% | 9.59% | 0.65% | 6.82% |
| mfi_14_recovery | 0.02% | -0.81% | 9.59% | 0.05% | 0.52% |
| adx_14_trend | 8.84% | 6.13% | 9.59% | 4.83% | 50.66% |
| aroon_25_trend | 6.70% | 1.88% | 9.59% | 3.02% | 31.76% |
| cci_20_momentum | 7.75% | -0.52% | 9.59% | 3.14% | 33.07% |
| williams_14_recovery | 0.23% | -8.61% | 9.59% | 0.55% | 5.77% |
| cmf_20_accumulation | 9.45% | 1.48% | 9.59% | 3.65% | 38.32% |
| chaikin_3_10 | 5.54% | -2.14% | 9.59% | 5.08% | 53.28% |
| roc_10_momentum | -0.29% | -5.58% | 9.59% | 1.47% | 15.49% |
| trix_15_trend | 8.10% | 5.41% | 9.59% | 6.22% | 65.09% |
| keltner_20_breakout | 6.87% | -0.08% | 9.59% | 2.62% | 27.56% |
| opening_range_30m | 10.52% | 5.09% | 9.59% | 3.42% | 35.96% |

동일 구간·초기 자금, 종료 시 청산 비용 포함. 노출 맞춤은 사후 설명용이며 v2 실제 계좌 성과가 아닙니다.
[낙폭 분해·비용 영향·전체 구간](WMT/comparison.json)

[v1 전체 기록](WMT/accounts.json) · [v2 전체 기록](WMT/accounts-v2.json)
