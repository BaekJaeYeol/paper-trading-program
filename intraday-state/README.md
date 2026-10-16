# 모의투자 운영 현황

[PC·서버 장애 진단과 복구 방법](https://github.com/BaekJaeYeol/paper-trading-program/blob/main/investment-lab/docs/failure-recovery.md)

이번 실행 복구: {}

완료 봉 확인 주기: 기록 9/15회 · 기록 없는 예정 6회 · 아직 판정 전 11회 · 주의: 예약 시작 지연 또는 실행·저장 누락을 확인하세요.

[주기 판정 기준](https://github.com/BaekJaeYeol/paper-trading-program/blob/main/investment-lab/docs/session-coverage.md)

최근 확인: 2026-10-16T17:37:00.376302+00:00 (UTC)
다음 15분 확인 목표 (세션 실행 중에만 적용): 2026-10-16T17:52:00+00:00 (UTC, 실행 지연 가능)

실제 주문 없음. v1 기존 계좌와 v2 새 계좌의 시작일이 다르므로 수익률을 직접 우열 비교하지 마세요.
v2는 다음 봉 시가에 비용·스프레드·직전 거래량 제한을 적용한 가상 체결입니다. 미체결 잔량은 만료됩니다.

| 종목 | 상태 | 최근 성공 UTC | 마지막 완료 봉 UTC | 이번 새 봉 |
|---|---|---|---|---|
| SPY | updated | 2026-10-16T17:37:00.376302+00:00 | 2026-10-16T17:15:00+00:00 | 1 |
| QQQ | updated | 2026-10-16T17:37:00.376302+00:00 | 2026-10-16T17:15:00+00:00 | 1 |
| IWM | updated | 2026-10-16T17:37:00.376302+00:00 | 2026-10-16T17:15:00+00:00 | 1 |
| DIA | updated | 2026-10-16T17:37:00.376302+00:00 | 2026-10-16T17:15:00+00:00 | 1 |
| MSFT | updated | 2026-10-16T17:37:00.376302+00:00 | 2026-10-16T17:15:00+00:00 | 1 |
| JPM | updated | 2026-10-16T17:37:00.376302+00:00 | 2026-10-16T17:15:00+00:00 | 1 |
| XOM | updated | 2026-10-16T17:37:00.376302+00:00 | 2026-10-16T17:15:00+00:00 | 1 |
| JNJ | updated | 2026-10-16T17:37:00.376302+00:00 | 2026-10-16T17:15:00+00:00 | 1 |
| CAT | updated | 2026-10-16T17:37:00.376302+00:00 | 2026-10-16T17:15:00+00:00 | 1 |
| WMT | updated | 2026-10-16T17:37:00.376302+00:00 | 2026-10-16T17:15:00+00:00 | 1 |

이번 실행 소요: 43.55초
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
| v1 | buy_hold | 9862.19 | -137.81 | buy /  / buy_hold: prior completed bar target 100%; next bar open simulation |
| v1 | trend_8_26 | 9902.75 | -97.25 | sell /  / trend_8_26: prior completed bar target 0%; next bar open simulation |
| v1 | momentum_26 | 9916.54 | -83.46 | sell /  / momentum_26: prior completed bar target 0%; next bar open simulation |
| v1 | breakout_8 | 10000.00 | 0.00 | 대기 /  / 새 신호 대기 |
| v1 | reversion_12 | 9905.49 | -94.51 | buy /  / reversion_12: prior completed bar target 100%; next bar open simulation |
| v1 | volume_26 | 9925.86 | -74.14 | sell /  / volume_26: prior completed bar target 0%; next bar open simulation |
| v1 | trend_8_26 AND momentum_26 | 9916.54 | -83.46 | sell /  / trend_8_26 AND momentum_26: prior completed bar target 0%; next bar open simulation |
| v1 | trend_8_26 + momentum_26 | 9909.65 | -90.35 | sell /  / trend_8_26 + momentum_26: prior completed bar target 0%; next bar open simulation |
| v1 | trend_8_26 AND breakout_8 | 10000.00 | 0.00 | 대기 /  / 새 신호 대기 |
| v1 | trend_8_26 + breakout_8 | 9951.22 | -48.78 | sell /  / trend_8_26 + breakout_8: prior completed bar target 0%; next bar open simulation |
| v1 | trend_8_26 AND reversion_12 | 9946.23 | -53.77 | sell /  / trend_8_26 AND reversion_12: prior completed bar target 0%; next bar open simulation |
| v1 | trend_8_26 + reversion_12 | 9904.07 | -95.93 | buy /  / trend_8_26 + reversion_12: prior completed bar target 50%; next bar open simulation |
| v1 | trend_8_26 AND volume_26 | 9925.86 | -74.14 | sell /  / trend_8_26 AND volume_26: prior completed bar target 0%; next bar open simulation |
| v1 | trend_8_26 + volume_26 | 9914.27 | -85.73 | sell /  / trend_8_26 + volume_26: prior completed bar target 0%; next bar open simulation |
| v1 | momentum_26 AND breakout_8 | 10000.00 | 0.00 | 대기 /  / 새 신호 대기 |
| v1 | momentum_26 + breakout_8 | 9958.17 | -41.83 | sell /  / momentum_26 + breakout_8: prior completed bar target 0%; next bar open simulation |
| v1 | momentum_26 AND reversion_12 | 10000.00 | 0.00 | 대기 /  / 새 신호 대기 |
| v1 | momentum_26 + reversion_12 | 9930.79 | -69.21 | buy /  / momentum_26 + reversion_12: prior completed bar target 50%; next bar open simulation |
| v1 | momentum_26 AND volume_26 | 9939.68 | -60.32 | sell /  / momentum_26 AND volume_26: prior completed bar target 0%; next bar open simulation |
| v1 | momentum_26 + volume_26 | 9921.17 | -78.83 | sell /  / momentum_26 + volume_26: prior completed bar target 0%; next bar open simulation |
| v1 | breakout_8 AND reversion_12 | 10000.00 | 0.00 | 대기 /  / 새 신호 대기 |
| v1 | breakout_8 + reversion_12 | 9952.59 | -47.41 | buy /  / breakout_8 + reversion_12: prior completed bar target 50%; next bar open simulation |
| v1 | breakout_8 AND volume_26 | 10000.00 | 0.00 | 대기 /  / 새 신호 대기 |
| v1 | breakout_8 + volume_26 | 9962.84 | -37.16 | sell /  / breakout_8 + volume_26: prior completed bar target 0%; next bar open simulation |
| v1 | reversion_12 AND volume_26 | 9946.23 | -53.77 | sell /  / reversion_12 AND volume_26: prior completed bar target 0%; next bar open simulation |
| v1 | reversion_12 + volume_26 | 9915.64 | -84.36 | buy /  / reversion_12 + volume_26: prior completed bar target 50%; next bar open simulation |
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
| v2 | buy_hold | 9791.06 | -208.94 | buy / partial / 직전 완료 봉 목표 비중 100%; 다음 봉 시가 가정 |
| v2 | trend_8_26 | 9786.41 | -213.59 | sell / filled / 직전 완료 봉 목표 비중 0%; 다음 봉 시가 가정 |
| v2 | momentum_26 | 9770.62 | -229.38 | sell / filled / 직전 완료 봉 목표 비중 0%; 다음 봉 시가 가정 |
| v2 | breakout_8 | 9598.61 | -401.39 | sell / filled / 직전 완료 봉 목표 비중 0%; 다음 봉 시가 가정 |
| v2 | reversion_12 | 9444.77 | -555.23 | buy / partial / 직전 완료 봉 목표 비중 100%; 다음 봉 시가 가정 |
| v2 | volume_26 | 9369.58 | -630.42 | sell / filled / 직전 완료 봉 목표 비중 0%; 다음 봉 시가 가정 |
| v2 | trend_8_26 AND momentum_26 | 9777.28 | -222.72 | sell / filled / 직전 완료 봉 목표 비중 0%; 다음 봉 시가 가정 |
| v2 | trend_8_26 + momentum_26 | 9778.53 | -221.47 | sell / filled / 직전 완료 봉 목표 비중 0%; 다음 봉 시가 가정 |
| v2 | trend_8_26 AND breakout_8 | 9825.21 | -174.79 | sell / filled / 직전 완료 봉 목표 비중 0%; 다음 봉 시가 가정 |
| v2 | trend_8_26 + breakout_8 | 9691.90 | -308.10 | sell / filled / 직전 완료 봉 목표 비중 0%; 다음 봉 시가 가정 |
| v2 | trend_8_26 AND reversion_12 | 9840.93 | -159.07 | sell / filled / 직전 완료 봉 목표 비중 0%; 다음 봉 시가 가정 |
| v2 | trend_8_26 + reversion_12 | 9613.71 | -386.29 | buy / filled / 직전 완료 봉 목표 비중 50%; 다음 봉 시가 가정 |
| v2 | trend_8_26 AND volume_26 | 9770.95 | -229.05 | sell / filled / 직전 완료 봉 목표 비중 0%; 다음 봉 시가 가정 |
| v2 | trend_8_26 + volume_26 | 9595.60 | -404.40 | sell / filled / 직전 완료 봉 목표 비중 0%; 다음 봉 시가 가정 |
| v2 | momentum_26 AND breakout_8 | 9783.53 | -216.47 | sell / filled / 직전 완료 봉 목표 비중 0%; 다음 봉 시가 가정 |
| v2 | momentum_26 + breakout_8 | 9684.14 | -315.86 | sell / filled / 직전 완료 봉 목표 비중 0%; 다음 봉 시가 가정 |
| v2 | momentum_26 AND reversion_12 | 9963.21 | -36.79 | sell / filled / 직전 완료 봉 목표 비중 0%; 다음 봉 시가 가정 |
| v2 | momentum_26 + reversion_12 | 9646.38 | -353.62 | buy / filled / 직전 완료 봉 목표 비중 50%; 다음 봉 시가 가정 |
| v2 | momentum_26 AND volume_26 | 9855.46 | -144.54 | sell / filled / 직전 완료 봉 목표 비중 0%; 다음 봉 시가 가정 |
| v2 | momentum_26 + volume_26 | 9628.18 | -371.82 | sell / filled / 직전 완료 봉 목표 비중 0%; 다음 봉 시가 가정 |
| v2 | breakout_8 AND reversion_12 | 10000.00 | 0.00 | 대기 /  / 새 신호 대기 |
| v2 | breakout_8 + reversion_12 | 9560.99 | -439.01 | buy / filled / 직전 완료 봉 목표 비중 50%; 다음 봉 시가 가정 |
| v2 | breakout_8 AND volume_26 | 9933.18 | -66.82 | sell / filled / 직전 완료 봉 목표 비중 0%; 다음 봉 시가 가정 |
| v2 | breakout_8 + volume_26 | 9522.95 | -477.05 | sell / filled / 직전 완료 봉 목표 비중 0%; 다음 봉 시가 가정 |
| v2 | reversion_12 AND volume_26 | 9689.01 | -310.99 | sell / filled / 직전 완료 봉 목표 비중 0%; 다음 봉 시가 가정 |
| v2 | reversion_12 + volume_26 | 9486.16 | -513.84 | buy / filled / 직전 완료 봉 목표 비중 50%; 다음 봉 시가 가정 |
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
| cash | 0.00% | 0.00% | -1.33% | -0.00% | 0.00% |
| buy_hold | -0.92% | -1.33% | -1.33% | -1.33% | 100.00% |
| trend_8_26 | 0.93% | -2.41% | -1.33% | -0.63% | 47.51% |
| momentum_26 | -0.87% | -5.35% | -1.33% | -0.62% | 46.72% |
| breakout_8 | -0.61% | -15.63% | -1.33% | -0.28% | 21.26% |
| reversion_12 | -2.75% | -13.17% | -1.33% | -0.40% | 29.66% |
| volume_26 | -0.94% | -9.69% | -1.33% | -0.12% | 8.92% |
| trend_8_26 AND momentum_26 | 0.45% | -3.27% | -1.33% | -0.54% | 40.42% |
| trend_8_26 + momentum_26 | 0.03% | -3.68% | -1.33% | -0.63% | 47.11% |
| trend_8_26 AND breakout_8 | 0.07% | -10.28% | -1.33% | -0.16% | 12.34% |
| trend_8_26 + breakout_8 | 0.16% | -9.26% | -1.33% | -0.46% | 34.39% |
| trend_8_26 AND reversion_12 | -0.20% | -3.90% | -1.33% | -0.08% | 6.04% |
| trend_8_26 + reversion_12 | -0.92% | -7.76% | -1.33% | -0.51% | 38.59% |
| trend_8_26 AND volume_26 | -0.57% | -4.66% | -1.33% | -0.06% | 4.20% |
| trend_8_26 + volume_26 | -0.01% | -6.12% | -1.33% | -0.38% | 28.22% |
| momentum_26 AND breakout_8 | 0.37% | -10.01% | -1.33% | -0.18% | 13.39% |
| momentum_26 + breakout_8 | -0.74% | -10.64% | -1.33% | -0.45% | 34.00% |
| momentum_26 AND reversion_12 | -1.04% | -5.11% | -1.33% | -0.08% | 6.30% |
| momentum_26 + reversion_12 | -1.81% | -8.59% | -1.33% | -0.51% | 38.19% |
| momentum_26 AND volume_26 | -0.39% | -3.27% | -1.33% | -0.03% | 2.10% |
| momentum_26 + volume_26 | -0.90% | -6.37% | -1.33% | -0.37% | 27.83% |
| breakout_8 AND reversion_12 | 0.00% | 0.00% | -1.33% | -0.00% | 0.00% |
| breakout_8 + reversion_12 | -1.68% | -13.88% | -1.33% | -0.34% | 25.47% |
| breakout_8 AND volume_26 | 0.09% | -1.17% | -1.33% | -0.01% | 1.05% |
| breakout_8 + volume_26 | -0.78% | -11.80% | -1.33% | -0.20% | 15.10% |
| reversion_12 AND volume_26 | -0.81% | -5.29% | -1.33% | -0.06% | 4.46% |
| reversion_12 + volume_26 | -1.85% | -11.08% | -1.33% | -0.26% | 19.30% |
| ema_12_26 | -0.67% | -3.95% | -1.33% | -0.64% | 48.29% |
| macd_12_26_9 | 0.47% | -3.66% | -1.33% | -0.39% | 28.87% |
| rsi_14_recovery | -0.33% | -3.62% | -1.33% | -0.03% | 2.10% |
| bollinger_20_reentry | -1.04% | -7.47% | -1.33% | -0.06% | 4.20% |
| donchian_20 | 0.11% | -6.79% | -1.33% | -0.09% | 6.56% |
| atr_14_breakout | -0.04% | -5.35% | -1.33% | -0.05% | 3.94% |
| session_vwap | 1.16% | -8.92% | -1.33% | -0.67% | 49.87% |
| obv_20 | -0.84% | -9.22% | -1.33% | -0.49% | 37.01% |
| stochastic_14_3_recovery | -1.05% | -15.65% | -1.33% | -0.13% | 9.97% |
| mfi_14_recovery | -0.01% | -2.50% | -1.33% | -0.02% | 1.57% |
| adx_14_trend | -0.10% | -3.81% | -1.33% | -0.37% | 27.82% |
| aroon_25_trend | 0.72% | -2.20% | -1.33% | -0.35% | 26.25% |
| cci_20_momentum | -0.18% | -7.84% | -1.33% | -0.28% | 21.00% |
| williams_14_recovery | -0.94% | -11.18% | -1.33% | -0.09% | 6.82% |
| cmf_20_accumulation | 1.68% | -2.50% | -1.33% | -0.61% | 45.67% |
| chaikin_3_10 | 1.26% | -5.32% | -1.33% | -0.52% | 39.11% |
| roc_10_momentum | -0.06% | -0.48% | -1.33% | -0.01% | 0.79% |
| trix_15_trend | -0.57% | -3.45% | -1.33% | -0.48% | 36.22% |
| keltner_20_breakout | 0.09% | -3.62% | -1.33% | -0.14% | 10.76% |
| opening_range_30m | -0.36% | -6.44% | -1.33% | -0.40% | 30.18% |

동일 구간·초기 자금, 종료 시 청산 비용 포함. 노출 맞춤은 사후 설명용이며 v2 실제 계좌 성과가 아닙니다.
[낙폭 분해·비용 영향·전체 구간](SPY/comparison.json)

[v1 전체 기록](SPY/accounts.json) · [v2 전체 기록](SPY/accounts-v2.json)

## QQQ 계좌

| 모델 | 전략 | 평가액 USD | 손익 USD | 최근 매매·이유 |
|---|---|---:|---:|---|
| v1 | cash | 10000.00 | 0.00 | 대기 /  / 새 신호 대기 |
| v1 | buy_hold | 9802.76 | -197.24 | buy /  / buy_hold: prior completed bar target 100%; next bar open simulation |
| v1 | trend_8_26 | 9922.86 | -77.14 | sell /  / trend_8_26: prior completed bar target 0%; next bar open simulation |
| v1 | momentum_26 | 9935.02 | -64.98 | sell /  / momentum_26: prior completed bar target 0%; next bar open simulation |
| v1 | breakout_8 | 10000.00 | 0.00 | 대기 /  / 새 신호 대기 |
| v1 | reversion_12 | 9823.71 | -176.29 | buy /  / reversion_12: prior completed bar target 100%; next bar open simulation |
| v1 | volume_26 | 9944.75 | -55.25 | sell /  / volume_26: prior completed bar target 0%; next bar open simulation |
| v1 | trend_8_26 AND momentum_26 | 9951.96 | -48.04 | sell /  / trend_8_26 AND momentum_26: prior completed bar target 0%; next bar open simulation |
| v1 | trend_8_26 + momentum_26 | 9928.92 | -71.08 | sell /  / trend_8_26 + momentum_26: prior completed bar target 0%; next bar open simulation |
| v1 | trend_8_26 AND breakout_8 | 10000.00 | 0.00 | 대기 /  / 새 신호 대기 |
| v1 | trend_8_26 + breakout_8 | 9961.32 | -38.68 | sell /  / trend_8_26 + breakout_8: prior completed bar target 0%; next bar open simulation |
| v1 | trend_8_26 AND reversion_12 | 9951.96 | -48.04 | sell /  / trend_8_26 AND reversion_12: prior completed bar target 0%; next bar open simulation |
| v1 | trend_8_26 + reversion_12 | 9873.08 | -126.92 | buy /  / trend_8_26 + reversion_12: prior completed bar target 50%; next bar open simulation |
| v1 | trend_8_26 AND volume_26 | 10000.00 | 0.00 | 대기 /  / 새 신호 대기 |
| v1 | trend_8_26 + volume_26 | 9933.75 | -66.25 | sell /  / trend_8_26 + volume_26: prior completed bar target 0%; next bar open simulation |
| v1 | momentum_26 AND breakout_8 | 10000.00 | 0.00 | 대기 /  / 새 신호 대기 |
| v1 | momentum_26 + breakout_8 | 9967.44 | -32.56 | sell /  / momentum_26 + breakout_8: prior completed bar target 0%; next bar open simulation |
| v1 | momentum_26 AND reversion_12 | 9951.96 | -48.04 | sell /  / momentum_26 AND reversion_12: prior completed bar target 0%; next bar open simulation |
| v1 | momentum_26 + reversion_12 | 9879.15 | -120.85 | buy /  / momentum_26 + reversion_12: prior completed bar target 50%; next bar open simulation |
| v1 | momentum_26 AND volume_26 | 10000.00 | 0.00 | 대기 /  / 새 신호 대기 |
| v1 | momentum_26 + volume_26 | 9939.85 | -60.15 | sell /  / momentum_26 + volume_26: prior completed bar target 0%; next bar open simulation |
| v1 | breakout_8 AND reversion_12 | 10000.00 | 0.00 | 대기 /  / 새 신호 대기 |
| v1 | breakout_8 + reversion_12 | 9911.37 | -88.63 | buy /  / breakout_8 + reversion_12: prior completed bar target 50%; next bar open simulation |
| v1 | breakout_8 AND volume_26 | 10000.00 | 0.00 | 대기 /  / 새 신호 대기 |
| v1 | breakout_8 + volume_26 | 9972.32 | -27.68 | sell /  / breakout_8 + volume_26: prior completed bar target 0%; next bar open simulation |
| v1 | reversion_12 AND volume_26 | 9950.23 | -49.77 | sell /  / reversion_12 AND volume_26: prior completed bar target 0%; next bar open simulation |
| v1 | reversion_12 + volume_26 | 9903.78 | -96.22 | buy /  / reversion_12 + volume_26: prior completed bar target 50%; next bar open simulation |
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
| v2 | buy_hold | 9485.90 | -514.10 | buy / partial / 직전 완료 봉 목표 비중 100%; 다음 봉 시가 가정 |
| v2 | trend_8_26 | 9726.12 | -273.88 | sell / filled / 직전 완료 봉 목표 비중 0%; 다음 봉 시가 가정 |
| v2 | momentum_26 | 9831.49 | -168.51 | sell / filled / 직전 완료 봉 목표 비중 0%; 다음 봉 시가 가정 |
| v2 | breakout_8 | 9669.86 | -330.14 | sell / filled / 직전 완료 봉 목표 비중 0%; 다음 봉 시가 가정 |
| v2 | reversion_12 | 9343.41 | -656.59 | buy / partial / 직전 완료 봉 목표 비중 100%; 다음 봉 시가 가정 |
| v2 | volume_26 | 9565.80 | -434.20 | 중단: 손실 한도 / sell / filled / 직전 완료 봉 목표 비중 0%; 다음 봉 시가 가정 |
| v2 | trend_8_26 AND momentum_26 | 9848.25 | -151.75 | sell / filled / 직전 완료 봉 목표 비중 0%; 다음 봉 시가 가정 |
| v2 | trend_8_26 + momentum_26 | 9778.69 | -221.31 | sell / filled / 직전 완료 봉 목표 비중 0%; 다음 봉 시가 가정 |
| v2 | trend_8_26 AND breakout_8 | 9895.83 | -104.17 | sell / filled / 직전 완료 봉 목표 비중 0%; 다음 봉 시가 가정 |
| v2 | trend_8_26 + breakout_8 | 9697.89 | -302.11 | sell / filled / 직전 완료 봉 목표 비중 0%; 다음 봉 시가 가정 |
| v2 | trend_8_26 AND reversion_12 | 9811.80 | -188.20 | sell / filled / 직전 완료 봉 목표 비중 0%; 다음 봉 시가 가정 |
| v2 | trend_8_26 + reversion_12 | 9532.47 | -467.53 | buy / filled / 직전 완료 봉 목표 비중 50%; 다음 봉 시가 가정 |
| v2 | trend_8_26 AND volume_26 | 9840.10 | -159.90 | sell / filled / 직전 완료 봉 목표 비중 0%; 다음 봉 시가 가정 |
| v2 | trend_8_26 + volume_26 | 9537.59 | -462.41 | sell / filled / 직전 완료 봉 목표 비중 0%; 다음 봉 시가 가정 |
| v2 | momentum_26 AND breakout_8 | 9960.69 | -39.31 | sell / filled / 직전 완료 봉 목표 비중 0%; 다음 봉 시가 가정 |
| v2 | momentum_26 + breakout_8 | 9750.28 | -249.72 | sell / filled / 직전 완료 봉 목표 비중 0%; 다음 봉 시가 가정 |
| v2 | momentum_26 AND reversion_12 | 9949.97 | -50.03 | sell / filled / 직전 완료 봉 목표 비중 0%; 다음 봉 시가 가정 |
| v2 | momentum_26 + reversion_12 | 9604.11 | -395.89 | buy / filled / 직전 완료 봉 목표 비중 50%; 다음 봉 시가 가정 |
| v2 | momentum_26 AND volume_26 | 9936.83 | -63.17 | sell / filled / 직전 완료 봉 목표 비중 0%; 다음 봉 시가 가정 |
| v2 | momentum_26 + volume_26 | 9589.12 | -410.88 | sell / filled / 직전 완료 봉 목표 비중 0%; 다음 봉 시가 가정 |
| v2 | breakout_8 AND reversion_12 | 10000.00 | 0.00 | 대기 /  / 새 신호 대기 |
| v2 | breakout_8 + reversion_12 | 9564.92 | -435.08 | buy / filled / 직전 완료 봉 목표 비중 50%; 다음 봉 시가 가정 |
| v2 | breakout_8 AND volume_26 | 9947.98 | -52.02 | sell / filled / 직전 완료 봉 목표 비중 0%; 다음 봉 시가 가정 |
| v2 | breakout_8 + volume_26 | 9550.09 | -449.91 | sell / filled / 직전 완료 봉 목표 비중 0%; 다음 봉 시가 가정 |
| v2 | reversion_12 AND volume_26 | 9547.64 | -452.36 | 중단: 손실 한도 / sell / filled / 직전 완료 봉 목표 비중 0%; 다음 봉 시가 가정 |
| v2 | reversion_12 + volume_26 | 9387.56 | -612.44 | buy / filled / 직전 완료 봉 목표 비중 50%; 다음 봉 시가 가정 |
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
| cash | 0.00% | 0.00% | -4.68% | -0.00% | 0.00% |
| buy_hold | -4.28% | -4.68% | -4.68% | -4.68% | 100.00% |
| trend_8_26 | -0.36% | -4.06% | -4.68% | -2.08% | 44.36% |
| momentum_26 | -1.63% | -6.47% | -4.68% | -1.79% | 38.06% |
| breakout_8 | -1.46% | -16.35% | -4.68% | -0.83% | 17.59% |
| reversion_12 | -1.81% | -14.16% | -4.68% | -1.37% | 29.13% |
| volume_26 | -1.23% | -14.01% | -4.68% | -0.70% | 14.96% |
| trend_8_26 AND momentum_26 | -0.50% | -4.60% | -4.68% | -1.56% | 33.33% |
| trend_8_26 + momentum_26 | -1.00% | -5.07% | -4.68% | -1.93% | 41.21% |
| trend_8_26 AND breakout_8 | -0.32% | -9.11% | -4.68% | -0.49% | 10.50% |
| trend_8_26 + breakout_8 | -0.91% | -10.04% | -4.68% | -1.45% | 30.98% |
| trend_8_26 AND reversion_12 | 0.15% | -5.17% | -4.68% | -0.31% | 6.56% |
| trend_8_26 + reversion_12 | -1.08% | -8.68% | -4.68% | -1.72% | 36.75% |
| trend_8_26 AND volume_26 | -0.71% | -5.59% | -4.68% | -0.20% | 4.20% |
| trend_8_26 + volume_26 | -0.79% | -8.98% | -4.68% | -1.39% | 29.66% |
| momentum_26 AND breakout_8 | -0.13% | -8.56% | -4.68% | -0.48% | 10.24% |
| momentum_26 + breakout_8 | -1.54% | -11.36% | -4.68% | -1.31% | 27.83% |
| momentum_26 AND reversion_12 | -0.29% | -5.59% | -4.68% | -0.25% | 5.25% |
| momentum_26 + reversion_12 | -1.72% | -9.84% | -4.68% | -1.58% | 33.60% |
| momentum_26 AND volume_26 | -0.30% | -4.40% | -4.68% | -0.16% | 3.41% |
| momentum_26 + volume_26 | -1.42% | -10.14% | -4.68% | -1.24% | 26.51% |
| breakout_8 AND reversion_12 | 0.00% | 0.00% | -4.68% | -0.00% | 0.00% |
| breakout_8 + reversion_12 | -1.63% | -14.38% | -4.68% | -1.10% | 23.37% |
| breakout_8 AND volume_26 | 0.04% | -2.04% | -4.68% | -0.06% | 1.31% |
| breakout_8 + volume_26 | -1.34% | -13.94% | -4.68% | -0.76% | 16.28% |
| reversion_12 AND volume_26 | -1.34% | -8.91% | -4.68% | -0.43% | 9.19% |
| reversion_12 + volume_26 | -1.51% | -13.55% | -4.68% | -1.04% | 22.05% |
| ema_12_26 | 0.17% | -1.91% | -4.68% | -1.68% | 35.70% |
| macd_12_26_9 | 1.49% | -1.86% | -4.68% | -0.95% | 20.21% |
| rsi_14_recovery | -0.50% | -4.99% | -4.68% | -0.14% | 2.89% |
| bollinger_20_reentry | -0.40% | -6.48% | -4.68% | -0.18% | 3.94% |
| donchian_20 | 0.28% | -4.24% | -4.68% | -0.22% | 4.72% |
| atr_14_breakout | -0.26% | -4.76% | -4.68% | -0.15% | 3.15% |
| session_vwap | -1.31% | -12.62% | -4.68% | -2.39% | 50.92% |
| obv_20 | -1.88% | -10.91% | -4.68% | -1.27% | 27.03% |
| stochastic_14_3_recovery | -0.50% | -11.91% | -4.68% | -0.36% | 7.61% |
| mfi_14_recovery | -0.16% | -1.82% | -4.68% | -0.05% | 1.05% |
| adx_14_trend | -0.71% | -3.59% | -4.68% | -0.88% | 18.64% |
| aroon_25_trend | 1.40% | -1.95% | -4.68% | -0.92% | 19.69% |
| cci_20_momentum | -0.85% | -5.72% | -4.68% | -0.70% | 14.96% |
| williams_14_recovery | -0.68% | -10.95% | -4.68% | -0.32% | 6.82% |
| cmf_20_accumulation | -2.08% | -9.97% | -4.68% | -1.48% | 31.50% |
| chaikin_3_10 | -3.04% | -11.22% | -4.68% | -1.59% | 33.86% |
| roc_10_momentum | -0.31% | -1.56% | -4.68% | -0.10% | 2.10% |
| trix_15_trend | 0.04% | -1.62% | -4.68% | -1.39% | 29.66% |
| keltner_20_breakout | -0.73% | -4.81% | -4.68% | -0.35% | 7.35% |
| opening_range_30m | -0.35% | -6.04% | -4.68% | -1.02% | 21.78% |

동일 구간·초기 자금, 종료 시 청산 비용 포함. 노출 맞춤은 사후 설명용이며 v2 실제 계좌 성과가 아닙니다.
[낙폭 분해·비용 영향·전체 구간](QQQ/comparison.json)

[v1 전체 기록](QQQ/accounts.json) · [v2 전체 기록](QQQ/accounts-v2.json)

## IWM 계좌

| 모델 | 전략 | 평가액 USD | 손익 USD | 최근 매매·이유 |
|---|---|---:|---:|---|
| v1 | cash | 10000.00 | 0.00 | 대기 /  / 새 신호 대기 |
| v1 | buy_hold | 9806.89 | -193.11 | buy /  / buy_hold: prior completed bar target 100%; next bar open simulation |
| v1 | trend_8_26 | 9838.25 | -161.75 | sell /  / trend_8_26: prior completed bar target 0%; next bar open simulation |
| v1 | momentum_26 | 9895.73 | -104.27 | sell /  / momentum_26: prior completed bar target 0%; next bar open simulation |
| v1 | breakout_8 | 9929.38 | -70.62 | sell /  / breakout_8: prior completed bar target 0%; next bar open simulation |
| v1 | reversion_12 | 9870.66 | -129.34 | buy /  / reversion_12: prior completed bar target 100%; next bar open simulation |
| v1 | volume_26 | 9935.98 | -64.02 | sell /  / volume_26: prior completed bar target 0%; next bar open simulation |
| v1 | trend_8_26 AND momentum_26 | 9895.73 | -104.27 | sell /  / trend_8_26 AND momentum_26: prior completed bar target 0%; next bar open simulation |
| v1 | trend_8_26 + momentum_26 | 9866.97 | -133.03 | sell /  / trend_8_26 + momentum_26: prior completed bar target 0%; next bar open simulation |
| v1 | trend_8_26 AND breakout_8 | 9929.38 | -70.62 | sell /  / trend_8_26 AND breakout_8: prior completed bar target 0%; next bar open simulation |
| v1 | trend_8_26 + breakout_8 | 9883.72 | -116.28 | sell /  / trend_8_26 + breakout_8: prior completed bar target 0%; next bar open simulation |
| v1 | trend_8_26 AND reversion_12 | 9902.23 | -97.77 | sell /  / trend_8_26 AND reversion_12: prior completed bar target 0%; next bar open simulation |
| v1 | trend_8_26 + reversion_12 | 9854.39 | -145.61 | buy /  / trend_8_26 + reversion_12: prior completed bar target 50%; next bar open simulation |
| v1 | trend_8_26 AND volume_26 | 9935.98 | -64.02 | sell /  / trend_8_26 AND volume_26: prior completed bar target 0%; next bar open simulation |
| v1 | trend_8_26 + volume_26 | 9886.95 | -113.05 | sell /  / trend_8_26 + volume_26: prior completed bar target 0%; next bar open simulation |
| v1 | momentum_26 AND breakout_8 | 9929.38 | -70.62 | sell /  / momentum_26 AND breakout_8: prior completed bar target 0%; next bar open simulation |
| v1 | momentum_26 + breakout_8 | 9912.56 | -87.44 | sell /  / momentum_26 + breakout_8: prior completed bar target 0%; next bar open simulation |
| v1 | momentum_26 AND reversion_12 | 10000.00 | 0.00 | 대기 /  / 새 신호 대기 |
| v1 | momentum_26 + reversion_12 | 9902.90 | -97.10 | buy /  / momentum_26 + reversion_12: prior completed bar target 50%; next bar open simulation |
| v1 | momentum_26 AND volume_26 | 10000.00 | 0.00 | 대기 /  / 새 신호 대기 |
| v1 | momentum_26 + volume_26 | 9915.81 | -84.19 | sell /  / momentum_26 + volume_26: prior completed bar target 0%; next bar open simulation |
| v1 | breakout_8 AND reversion_12 | 10000.00 | 0.00 | 대기 /  / 새 신호 대기 |
| v1 | breakout_8 + reversion_12 | 9899.92 | -100.08 | buy /  / breakout_8 + reversion_12: prior completed bar target 50%; next bar open simulation |
| v1 | breakout_8 AND volume_26 | 10000.00 | 0.00 | 대기 /  / 새 신호 대기 |
| v1 | breakout_8 + volume_26 | 9932.66 | -67.34 | sell /  / breakout_8 + volume_26: prior completed bar target 0%; next bar open simulation |
| v1 | reversion_12 AND volume_26 | 9935.98 | -64.02 | sell /  / reversion_12 AND volume_26: prior completed bar target 0%; next bar open simulation |
| v1 | reversion_12 + volume_26 | 9903.23 | -96.77 | buy /  / reversion_12 + volume_26: prior completed bar target 50%; next bar open simulation |
| v1 | ema_12_26 | 9838.25 | -161.75 | sell /  / EMA12 > EMA26; 조건 미충족; EMA12=273.669, EMA26=273.722 |
| v1 | macd_12_26_9 | 9916.70 | -83.30 | sell /  / MACD > 신호선 그리고 MACD > 0; 조건 미충족; MACD=0.425881, signal9=0.461272 |
| v1 | rsi_14_recovery | 10000.00 | 0.00 | 대기 /  / 새 신호 대기 |
| v1 | bollinger_20_reentry | 9947.64 | -52.36 | sell /  / 직전 종가 < 직전 하단밴드, 현재 하단밴드 <= 종가 <= SMA20 (한 봉 목표); 조건 미충족; close=271.86, lower20=271.804, SMA20=273.875, previous_lower20=272.119 |
| v1 | donchian_20 | 9929.38 | -70.62 | sell /  / 종가 > 현재 봉을 제외한 직전 20봉 최고가; 조건 미충족; close=274.88, prior_high20=275.91 |
| v1 | atr_14_breakout | 9929.38 | -70.62 | sell /  / 종가 > 직전 종가 + 직전 ATR14 그리고 종가 > EMA26; 조건 미충족; close=274.88, threshold=276.257, prior_ATR14=0.526844, EMA26=273.855 |
| v1 | session_vwap | 9937.31 | -62.69 | sell /  / 종가 > 뉴욕 거래일별 누적 전형가격 VWAP; 조건 미충족; close=274.88, session_VWAP=275.422, session_volume=2.52313e+06 |
| v1 | obv_20 | 9928.63 | -71.37 | sell /  / OBV > OBV의 SMA20 그리고 종가 > EMA26; 조건 미충족; OBV=-4.10489e+07, OBV_SMA20=-4.0926e+07, close=274.64, EMA26=273.913 |
| v1 | stochastic_14_3_recovery | 9880.91 | -119.09 | sell /  / 직전 %K14 < 20에서 %K14가 %D3 상향 돌파 (한 봉 목표); 조건 미충족; K14=2.62635, D3=4.00006, previous_K14=7.36227, previous_D3=3.53101 |
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
| v2 | buy_hold | 9702.03 | -297.97 | buy / partial / 직전 완료 봉 목표 비중 100%; 다음 봉 시가 가정 |
| v2 | trend_8_26 | 9709.80 | -290.20 | sell / filled / 직전 완료 봉 목표 비중 0%; 다음 봉 시가 가정 |
| v2 | momentum_26 | 9767.53 | -232.47 | sell / filled / 직전 완료 봉 목표 비중 0%; 다음 봉 시가 가정 |
| v2 | breakout_8 | 9547.89 | -452.11 | sell / filled / 직전 완료 봉 목표 비중 0%; 다음 봉 시가 가정 |
| v2 | reversion_12 | 9414.35 | -585.65 | buy / partial / 직전 완료 봉 목표 비중 100%; 다음 봉 시가 가정 |
| v2 | volume_26 | 9450.57 | -549.43 | sell / filled / 직전 완료 봉 목표 비중 0%; 다음 봉 시가 가정 |
| v2 | trend_8_26 AND momentum_26 | 9918.12 | -81.88 | sell / filled / 직전 완료 봉 목표 비중 0%; 다음 봉 시가 가정 |
| v2 | trend_8_26 + momentum_26 | 9759.25 | -240.75 | sell / filled / 직전 완료 봉 목표 비중 0%; 다음 봉 시가 가정 |
| v2 | trend_8_26 AND breakout_8 | 9840.76 | -159.24 | sell / filled / 직전 완료 봉 목표 비중 0%; 다음 봉 시가 가정 |
| v2 | trend_8_26 + breakout_8 | 9648.89 | -351.11 | sell / filled / 직전 완료 봉 목표 비중 0%; 다음 봉 시가 가정 |
| v2 | trend_8_26 AND reversion_12 | 9783.25 | -216.75 | sell / filled / 직전 완료 봉 목표 비중 0%; 다음 봉 시가 가정 |
| v2 | trend_8_26 + reversion_12 | 9560.73 | -439.27 | buy / filled / 직전 완료 봉 목표 비중 50%; 다음 봉 시가 가정 |
| v2 | trend_8_26 AND volume_26 | 9797.73 | -202.27 | sell / filled / 직전 완료 봉 목표 비중 0%; 다음 봉 시가 가정 |
| v2 | trend_8_26 + volume_26 | 9599.39 | -400.61 | sell / filled / 직전 완료 봉 목표 비중 0%; 다음 봉 시가 가정 |
| v2 | momentum_26 AND breakout_8 | 9733.71 | -266.29 | sell / filled / 직전 완료 봉 목표 비중 0%; 다음 봉 시가 가정 |
| v2 | momentum_26 + breakout_8 | 9657.13 | -342.87 | sell / filled / 직전 완료 봉 목표 비중 0%; 다음 봉 시가 가정 |
| v2 | momentum_26 AND reversion_12 | 9960.59 | -39.41 | sell / filled / 직전 완료 봉 목표 비중 0%; 다음 봉 시가 가정 |
| v2 | momentum_26 + reversion_12 | 9629.23 | -370.77 | buy / filled / 직전 완료 봉 목표 비중 50%; 다음 봉 시가 가정 |
| v2 | momentum_26 AND volume_26 | 9897.79 | -102.21 | sell / filled / 직전 완료 봉 목표 비중 0%; 다음 봉 시가 가정 |
| v2 | momentum_26 + volume_26 | 9607.50 | -392.50 | sell / filled / 직전 완료 봉 목표 비중 0%; 다음 봉 시가 가정 |
| v2 | breakout_8 AND reversion_12 | 10000.00 | 0.00 | 대기 /  / 새 신호 대기 |
| v2 | breakout_8 + reversion_12 | 9520.35 | -479.65 | buy / filled / 직전 완료 봉 목표 비중 50%; 다음 봉 시가 가정 |
| v2 | breakout_8 AND volume_26 | 9746.03 | -253.97 | sell / filled / 직전 완료 봉 목표 비중 0%; 다음 봉 시가 가정 |
| v2 | breakout_8 + volume_26 | 9519.00 | -481.00 | sell / filled / 직전 완료 봉 목표 비중 0%; 다음 봉 시가 가정 |
| v2 | reversion_12 AND volume_26 | 9676.46 | -323.54 | sell / filled / 직전 완료 봉 목표 비중 0%; 다음 봉 시가 가정 |
| v2 | reversion_12 + volume_26 | 9452.02 | -547.98 | buy / filled / 직전 완료 봉 목표 비중 50%; 다음 봉 시가 가정 |
| v2 | ema_12_26 | 9836.29 | -163.71 | sell / filled / EMA12 > EMA26; 조건 미충족; EMA12=273.669, EMA26=273.722; 직전 완료 봉 목표를 다음 봉 시가에 모의 적용 |
| v2 | macd_12_26_9 | 9914.72 | -85.28 | sell / filled / MACD > 신호선 그리고 MACD > 0; 조건 미충족; MACD=0.425881, signal9=0.461272; 직전 완료 봉 목표를 다음 봉 시가에 모의 적용 |
| v2 | rsi_14_recovery | 10000.00 | 0.00 | 대기 /  / 새 신호 대기 |
| v2 | bollinger_20_reentry | 9945.65 | -54.35 | sell / filled / 직전 종가 < 직전 하단밴드, 현재 하단밴드 <= 종가 <= SMA20 (한 봉 목표); 조건 미충족; close=271.86, lower20=271.804, SMA20=273.875, previous_lower20=272.119; 직전 완료 봉 목표를 다음 봉 시가에 모의 적용 |
| v2 | donchian_20 | 9927.39 | -72.61 | sell / filled / 종가 > 현재 봉을 제외한 직전 20봉 최고가; 조건 미충족; close=274.88, prior_high20=275.91; 직전 완료 봉 목표를 다음 봉 시가에 모의 적용 |
| v2 | atr_14_breakout | 9927.39 | -72.61 | sell / filled / 종가 > 직전 종가 + 직전 ATR14 그리고 종가 > EMA26; 조건 미충족; close=274.88, threshold=276.257, prior_ATR14=0.526844, EMA26=273.855; 직전 완료 봉 목표를 다음 봉 시가에 모의 적용 |
| v2 | session_vwap | 9935.32 | -64.68 | sell / filled / 종가 > 뉴욕 거래일별 누적 전형가격 VWAP; 조건 미충족; close=274.88, session_VWAP=275.422, session_volume=2.52313e+06; 직전 완료 봉 목표를 다음 봉 시가에 모의 적용 |
| v2 | obv_20 | 9926.64 | -73.36 | sell / filled / OBV > OBV의 SMA20 그리고 종가 > EMA26; 조건 미충족; OBV=-4.10489e+07, OBV_SMA20=-4.0926e+07, close=274.64, EMA26=273.913; 직전 완료 봉 목표를 다음 봉 시가에 모의 적용 |
| v2 | stochastic_14_3_recovery | 9876.96 | -123.04 | sell / filled / 직전 %K14 < 20에서 %K14가 %D3 상향 돌파 (한 봉 목표); 조건 미충족; K14=2.62635, D3=4.00006, previous_K14=7.36227, previous_D3=3.53101; 직전 완료 봉 목표를 다음 봉 시가에 모의 적용 |
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
| cash | 0.00% | 0.00% | -4.55% | -0.00% | 0.00% |
| buy_hold | -4.15% | -4.55% | -4.55% | -4.55% | 100.00% |
| trend_8_26 | -2.31% | -5.93% | -4.55% | -2.01% | 43.83% |
| momentum_26 | -3.10% | -8.63% | -4.55% | -1.75% | 38.06% |
| breakout_8 | -0.95% | -13.77% | -4.55% | -0.87% | 18.90% |
| reversion_12 | -3.25% | -15.77% | -4.55% | -1.45% | 31.50% |
| volume_26 | -2.55% | -9.65% | -4.55% | -0.40% | 8.66% |
| trend_8_26 AND momentum_26 | -1.98% | -6.01% | -4.55% | -1.52% | 33.07% |
| trend_8_26 + momentum_26 | -2.70% | -6.90% | -4.55% | -1.88% | 40.95% |
| trend_8_26 AND breakout_8 | -0.45% | -7.70% | -4.55% | -0.50% | 10.76% |
| trend_8_26 + breakout_8 | -1.62% | -9.75% | -4.55% | -1.44% | 31.37% |
| trend_8_26 AND reversion_12 | -0.73% | -5.61% | -4.55% | -0.28% | 6.04% |
| trend_8_26 + reversion_12 | -2.77% | -10.81% | -4.55% | -1.73% | 37.67% |
| trend_8_26 AND volume_26 | -1.26% | -4.93% | -4.55% | -0.17% | 3.67% |
| trend_8_26 + volume_26 | -2.42% | -7.62% | -4.55% | -1.21% | 26.25% |
| momentum_26 AND breakout_8 | -0.21% | -7.48% | -4.55% | -0.47% | 10.24% |
| momentum_26 + breakout_8 | -2.02% | -11.24% | -4.55% | -1.31% | 28.48% |
| momentum_26 AND reversion_12 | -0.08% | -3.38% | -4.55% | -0.12% | 2.62% |
| momentum_26 + reversion_12 | -3.17% | -10.98% | -4.55% | -1.60% | 34.78% |
| momentum_26 AND volume_26 | -1.32% | -3.77% | -4.55% | -0.09% | 1.84% |
| momentum_26 + volume_26 | -2.82% | -8.76% | -4.55% | -1.08% | 23.36% |
| breakout_8 AND reversion_12 | 0.00% | 0.00% | -4.55% | -0.00% | 0.00% |
| breakout_8 + reversion_12 | -2.10% | -14.07% | -4.55% | -1.16% | 25.21% |
| breakout_8 AND volume_26 | -1.30% | -3.76% | -4.55% | -0.10% | 2.10% |
| breakout_8 + volume_26 | -1.75% | -11.55% | -4.55% | -0.64% | 13.79% |
| reversion_12 AND volume_26 | -0.62% | -5.10% | -4.55% | -0.22% | 4.72% |
| reversion_12 + volume_26 | -2.90% | -12.22% | -4.55% | -0.93% | 20.08% |
| ema_12_26 | -0.71% | -3.18% | -4.55% | -1.95% | 42.52% |
| macd_12_26_9 | 1.88% | -0.23% | -4.55% | -1.23% | 26.77% |
| rsi_14_recovery | -0.28% | -4.78% | -4.55% | -0.13% | 2.89% |
| bollinger_20_reentry | -0.37% | -5.27% | -4.55% | -0.15% | 3.15% |
| donchian_20 | -0.20% | -5.10% | -4.55% | -0.25% | 5.51% |
| atr_14_breakout | -1.87% | -8.25% | -4.55% | -0.19% | 4.20% |
| session_vwap | -1.68% | -11.48% | -4.55% | -1.94% | 42.26% |
| obv_20 | -0.31% | -4.41% | -4.55% | -1.70% | 37.01% |
| stochastic_14_3_recovery | -1.26% | -14.40% | -4.55% | -0.41% | 8.92% |
| mfi_14_recovery | 0.22% | -3.50% | -4.55% | -0.11% | 2.36% |
| adx_14_trend | -0.58% | -4.27% | -4.55% | -1.45% | 31.50% |
| aroon_25_trend | -1.70% | -4.95% | -4.55% | -0.94% | 20.47% |
| cci_20_momentum | -1.95% | -7.93% | -4.55% | -0.80% | 17.32% |
| williams_14_recovery | -0.74% | -10.26% | -4.55% | -0.29% | 6.30% |
| cmf_20_accumulation | -2.49% | -8.82% | -4.55% | -0.82% | 17.85% |
| chaikin_3_10 | -3.14% | -9.82% | -4.55% | -1.45% | 31.50% |
| roc_10_momentum | -0.63% | -1.87% | -4.55% | -0.15% | 3.15% |
| trix_15_trend | -0.41% | -3.70% | -4.55% | -1.45% | 31.50% |
| keltner_20_breakout | -0.91% | -4.18% | -4.55% | -0.24% | 5.25% |
| opening_range_30m | 1.50% | -3.49% | -4.55% | -1.11% | 24.15% |

동일 구간·초기 자금, 종료 시 청산 비용 포함. 노출 맞춤은 사후 설명용이며 v2 실제 계좌 성과가 아닙니다.
[낙폭 분해·비용 영향·전체 구간](IWM/comparison.json)

[v1 전체 기록](IWM/accounts.json) · [v2 전체 기록](IWM/accounts-v2.json)

## DIA 계좌

| 모델 | 전략 | 평가액 USD | 손익 USD | 최근 매매·이유 |
|---|---|---:|---:|---|
| v1 | cash | 10000.00 | 0.00 | 대기 /  / 새 신호 대기 |
| v1 | buy_hold | 9901.20 | -98.80 | buy /  / buy_hold: prior completed bar target 100%; next bar open simulation |
| v1 | trend_8_26 | 9904.27 | -95.73 | sell /  / trend_8_26: prior completed bar target 0%; next bar open simulation |
| v1 | momentum_26 | 9909.03 | -90.97 | sell /  / momentum_26: prior completed bar target 0%; next bar open simulation |
| v1 | breakout_8 | 9940.12 | -59.88 | sell /  / breakout_8: prior completed bar target 0%; next bar open simulation |
| v1 | reversion_12 | 9932.93 | -67.07 | buy /  / reversion_12: prior completed bar target 100%; next bar open simulation |
| v1 | volume_26 | 9928.60 | -71.40 | buy /  / volume_26: prior completed bar target 100%; next bar open simulation |
| v1 | trend_8_26 AND momentum_26 | 9909.03 | -90.97 | sell /  / trend_8_26 AND momentum_26: prior completed bar target 0%; next bar open simulation |
| v1 | trend_8_26 + momentum_26 | 9906.65 | -93.35 | sell /  / trend_8_26 + momentum_26: prior completed bar target 0%; next bar open simulation |
| v1 | trend_8_26 AND breakout_8 | 9940.12 | -59.88 | sell /  / trend_8_26 AND breakout_8: prior completed bar target 0%; next bar open simulation |
| v1 | trend_8_26 + breakout_8 | 9922.18 | -77.82 | sell /  / trend_8_26 + breakout_8: prior completed bar target 0%; next bar open simulation |
| v1 | trend_8_26 AND reversion_12 | 9936.00 | -64.00 | sell /  / trend_8_26 AND reversion_12: prior completed bar target 0%; next bar open simulation |
| v1 | trend_8_26 + reversion_12 | 9918.54 | -81.46 | buy /  / trend_8_26 + reversion_12: prior completed bar target 50%; next bar open simulation |
| v1 | trend_8_26 AND volume_26 | 9943.10 | -56.90 | sell /  / trend_8_26 AND volume_26: prior completed bar target 0%; next bar open simulation |
| v1 | trend_8_26 + volume_26 | 9916.37 | -83.63 | buy /  / trend_8_26 + volume_26: prior completed bar target 50%; next bar open simulation |
| v1 | momentum_26 AND breakout_8 | 9940.12 | -59.88 | sell /  / momentum_26 AND breakout_8: prior completed bar target 0%; next bar open simulation |
| v1 | momentum_26 + breakout_8 | 9924.57 | -75.43 | sell /  / momentum_26 + breakout_8: prior completed bar target 0%; next bar open simulation |
| v1 | momentum_26 AND reversion_12 | 9940.78 | -59.22 | sell /  / momentum_26 AND reversion_12: prior completed bar target 0%; next bar open simulation |
| v1 | momentum_26 + reversion_12 | 9920.92 | -79.08 | buy /  / momentum_26 + reversion_12: prior completed bar target 50%; next bar open simulation |
| v1 | momentum_26 AND volume_26 | 9943.10 | -56.90 | sell /  / momentum_26 AND volume_26: prior completed bar target 0%; next bar open simulation |
| v1 | momentum_26 + volume_26 | 9918.76 | -81.24 | buy /  / momentum_26 + volume_26: prior completed bar target 50%; next bar open simulation |
| v1 | breakout_8 AND reversion_12 | 10000.00 | 0.00 | 대기 /  / 새 신호 대기 |
| v1 | breakout_8 + reversion_12 | 9936.49 | -63.51 | buy /  / breakout_8 + reversion_12: prior completed bar target 50%; next bar open simulation |
| v1 | breakout_8 AND volume_26 | 10000.00 | 0.00 | 대기 /  / 새 신호 대기 |
| v1 | breakout_8 + volume_26 | 9934.34 | -65.66 | buy /  / breakout_8 + volume_26: prior completed bar target 50%; next bar open simulation |
| v1 | reversion_12 AND volume_26 | 9985.42 | -14.58 | buy /  / reversion_12 AND volume_26: prior completed bar target 100%; next bar open simulation |
| v1 | reversion_12 + volume_26 | 9950.61 | -49.39 | buy /  / reversion_12 + volume_26: prior completed bar target 100%; next bar open simulation |
| v1 | ema_12_26 | 9876.07 | -123.93 | sell /  / EMA12 > EMA26; 조건 미충족; EMA12=520.874, EMA26=520.918 |
| v1 | macd_12_26_9 | 9941.64 | -58.36 | sell /  / MACD > 신호선 그리고 MACD > 0; 조건 미충족; MACD=1.23542, signal9=1.25143 |
| v1 | rsi_14_recovery | 10000.00 | 0.00 | 대기 /  / 새 신호 대기 |
| v1 | bollinger_20_reentry | 10000.00 | 0.00 | 대기 /  / 새 신호 대기 |
| v1 | donchian_20 | 9940.12 | -59.88 | sell /  / 종가 > 현재 봉을 제외한 직전 20봉 최고가; 조건 미충족; close=522.89, prior_high20=525.09 |
| v1 | atr_14_breakout | 9972.44 | -27.56 | sell /  / 종가 > 직전 종가 + 직전 ATR14 그리고 종가 > EMA26; 조건 미충족; close=524.65, threshold=524.777, prior_ATR14=0.84688, EMA26=520.429 |
| v1 | session_vwap | 9960.84 | -39.16 | sell /  / 종가 > 뉴욕 거래일별 누적 전형가격 VWAP; 조건 미충족; close=522.89, session_VWAP=523.72, session_volume=975370 |
| v1 | obv_20 | 9924.53 | -75.47 | sell /  / OBV > OBV의 SMA20 그리고 종가 > EMA26; 조건 미충족; OBV=-5.35236e+06, OBV_SMA20=-5.09617e+06, close=522.08, EMA26=521.373 |
| v1 | stochastic_14_3_recovery | 9931.73 | -68.27 | sell /  / 직전 %K14 < 20에서 %K14가 %D3 상향 돌파 (한 봉 목표); 조건 미충족; K14=2.62089, D3=5.57899, previous_K14=8.02172, previous_D3=4.77963 |
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
| v2 | buy_hold | 10023.86 | 23.86 | buy / partial / 직전 완료 봉 목표 비중 100%; 다음 봉 시가 가정 |
| v2 | trend_8_26 | 9839.12 | -160.88 | sell / filled / 직전 완료 봉 목표 비중 0%; 다음 봉 시가 가정 |
| v2 | momentum_26 | 9952.08 | -47.92 | sell / filled / 직전 완료 봉 목표 비중 0%; 다음 봉 시가 가정 |
| v2 | breakout_8 | 9466.63 | -533.37 | sell / filled / 직전 완료 봉 목표 비중 0%; 다음 봉 시가 가정 |
| v2 | reversion_12 | 9632.01 | -367.99 | buy / partial / 직전 완료 봉 목표 비중 100%; 다음 봉 시가 가정 |
| v2 | volume_26 | 9645.93 | -354.07 | buy / partial / 직전 완료 봉 목표 비중 100%; 다음 봉 시가 가정 |
| v2 | trend_8_26 AND momentum_26 | 9947.46 | -52.54 | sell / filled / 직전 완료 봉 목표 비중 0%; 다음 봉 시가 가정 |
| v2 | trend_8_26 + momentum_26 | 9895.51 | -104.49 | sell / filled / 직전 완료 봉 목표 비중 0%; 다음 봉 시가 가정 |
| v2 | trend_8_26 AND breakout_8 | 9626.81 | -373.19 | sell / filled / 직전 완료 봉 목표 비중 0%; 다음 봉 시가 가정 |
| v2 | trend_8_26 + breakout_8 | 9651.15 | -348.85 | sell / filled / 직전 완료 봉 목표 비중 0%; 다음 봉 시가 가정 |
| v2 | trend_8_26 AND reversion_12 | 9746.03 | -253.97 | sell / filled / 직전 완료 봉 목표 비중 0%; 다음 봉 시가 가정 |
| v2 | trend_8_26 + reversion_12 | 9734.72 | -265.28 | buy / filled / 직전 완료 봉 목표 비중 50%; 다음 봉 시가 가정 |
| v2 | trend_8_26 AND volume_26 | 9800.82 | -199.18 | sell / filled / 직전 완료 봉 목표 비중 0%; 다음 봉 시가 가정 |
| v2 | trend_8_26 + volume_26 | 9762.42 | -237.58 | buy / filled / 직전 완료 봉 목표 비중 50%; 다음 봉 시가 가정 |
| v2 | momentum_26 AND breakout_8 | 9615.85 | -384.15 | sell / filled / 직전 완료 봉 목표 비중 0%; 다음 봉 시가 가정 |
| v2 | momentum_26 + breakout_8 | 9706.46 | -293.54 | sell / filled / 직전 완료 봉 목표 비중 0%; 다음 봉 시가 가정 |
| v2 | momentum_26 AND reversion_12 | 9895.03 | -104.97 | sell / filled / 직전 완료 봉 목표 비중 0%; 다음 봉 시가 가정 |
| v2 | momentum_26 + reversion_12 | 9790.51 | -209.49 | buy / filled / 직전 완료 봉 목표 비중 50%; 다음 봉 시가 가정 |
| v2 | momentum_26 AND volume_26 | 9733.77 | -266.23 | sell / filled / 직전 완료 봉 목표 비중 0%; 다음 봉 시가 가정 |
| v2 | momentum_26 + volume_26 | 9839.08 | -160.92 | buy / filled / 직전 완료 봉 목표 비중 50%; 다음 봉 시가 가정 |
| v2 | breakout_8 AND reversion_12 | 10000.00 | 0.00 | 대기 /  / 새 신호 대기 |
| v2 | breakout_8 + reversion_12 | 9548.51 | -451.49 | buy / filled / 직전 완료 봉 목표 비중 50%; 다음 봉 시가 가정 |
| v2 | breakout_8 AND volume_26 | 9796.56 | -203.44 | sell / filled / 직전 완료 봉 목표 비중 0%; 다음 봉 시가 가정 |
| v2 | breakout_8 + volume_26 | 9555.69 | -444.31 | buy / filled / 직전 완료 봉 목표 비중 50%; 다음 봉 시가 가정 |
| v2 | reversion_12 AND volume_26 | 9984.42 | -15.58 | buy / partial / 직전 완료 봉 목표 비중 100%; 다음 봉 시가 가정 |
| v2 | reversion_12 + volume_26 | 9658.94 | -341.06 | buy / partial / 직전 완료 봉 목표 비중 100%; 다음 봉 시가 가정 |
| v2 | ema_12_26 | 9874.10 | -125.90 | sell / filled / EMA12 > EMA26; 조건 미충족; EMA12=520.874, EMA26=520.918; 직전 완료 봉 목표를 다음 봉 시가에 모의 적용 |
| v2 | macd_12_26_9 | 9939.65 | -60.35 | sell / filled / MACD > 신호선 그리고 MACD > 0; 조건 미충족; MACD=1.23542, signal9=1.25143; 직전 완료 봉 목표를 다음 봉 시가에 모의 적용 |
| v2 | rsi_14_recovery | 10000.00 | 0.00 | 대기 /  / 새 신호 대기 |
| v2 | bollinger_20_reentry | 10000.00 | 0.00 | 대기 /  / 새 신호 대기 |
| v2 | donchian_20 | 9938.13 | -61.87 | sell / filled / 종가 > 현재 봉을 제외한 직전 20봉 최고가; 조건 미충족; close=522.89, prior_high20=525.09; 직전 완료 봉 목표를 다음 봉 시가에 모의 적용 |
| v2 | atr_14_breakout | 9970.44 | -29.56 | sell / filled / 종가 > 직전 종가 + 직전 ATR14 그리고 종가 > EMA26; 조건 미충족; close=524.65, threshold=524.777, prior_ATR14=0.84688, EMA26=520.429; 직전 완료 봉 목표를 다음 봉 시가에 모의 적용 |
| v2 | session_vwap | 9958.85 | -41.15 | sell / filled / 종가 > 뉴욕 거래일별 누적 전형가격 VWAP; 조건 미충족; close=522.89, session_VWAP=523.72, session_volume=975370; 직전 완료 봉 목표를 다음 봉 시가에 모의 적용 |
| v2 | obv_20 | 9922.55 | -77.45 | sell / filled / OBV > OBV의 SMA20 그리고 종가 > EMA26; 조건 미충족; OBV=-5.35236e+06, OBV_SMA20=-5.09617e+06, close=522.08, EMA26=521.373; 직전 완료 봉 목표를 다음 봉 시가에 모의 적용 |
| v2 | stochastic_14_3_recovery | 9929.74 | -70.26 | sell / filled / 직전 %K14 < 20에서 %K14가 %D3 상향 돌파 (한 봉 목표); 조건 미충족; K14=2.62089, D3=5.57899, previous_K14=8.02172, previous_D3=4.77963; 직전 완료 봉 목표를 다음 봉 시가에 모의 적용 |
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
| cash | 0.00% | 0.00% | -0.16% | -0.00% | 0.00% |
| buy_hold | 0.26% | -0.16% | -0.16% | -0.16% | 100.00% |
| trend_8_26 | 0.80% | -3.75% | -0.16% | -0.09% | 55.64% |
| momentum_26 | -0.48% | -4.57% | -0.16% | -0.08% | 51.71% |
| breakout_8 | -0.04% | -16.90% | -0.16% | -0.04% | 23.36% |
| reversion_12 | -1.82% | -10.11% | -0.16% | -0.04% | 26.25% |
| volume_26 | -1.02% | -11.63% | -0.16% | -0.02% | 11.29% |
| trend_8_26 AND momentum_26 | 0.99% | -3.17% | -0.16% | -0.07% | 45.93% |
| trend_8_26 + momentum_26 | 0.17% | -4.16% | -0.16% | -0.09% | 53.68% |
| trend_8_26 AND breakout_8 | 0.53% | -11.37% | -0.16% | -0.02% | 15.22% |
| trend_8_26 + breakout_8 | 0.39% | -10.38% | -0.16% | -0.06% | 39.51% |
| trend_8_26 AND reversion_12 | 0.13% | -5.19% | -0.16% | -0.01% | 7.35% |
| trend_8_26 + reversion_12 | -0.51% | -6.60% | -0.16% | -0.07% | 40.95% |
| trend_8_26 AND volume_26 | 0.48% | -4.86% | -0.16% | -0.01% | 5.25% |
| trend_8_26 + volume_26 | -0.11% | -7.59% | -0.16% | -0.05% | 33.47% |
| momentum_26 AND breakout_8 | -0.27% | -11.70% | -0.16% | -0.03% | 15.49% |
| momentum_26 + breakout_8 | -0.25% | -10.76% | -0.16% | -0.06% | 37.54% |
| momentum_26 AND reversion_12 | -0.37% | -4.47% | -0.16% | -0.01% | 6.56% |
| momentum_26 + reversion_12 | -1.15% | -6.61% | -0.16% | -0.06% | 38.98% |
| momentum_26 AND volume_26 | -0.49% | -5.77% | -0.16% | -0.01% | 4.72% |
| momentum_26 + volume_26 | -0.75% | -7.40% | -0.16% | -0.05% | 31.50% |
| breakout_8 AND reversion_12 | 0.00% | 0.00% | -0.16% | -0.00% | 0.00% |
| breakout_8 + reversion_12 | -0.93% | -13.22% | -0.16% | -0.04% | 24.81% |
| breakout_8 AND volume_26 | -0.87% | -4.55% | -0.16% | -0.01% | 3.15% |
| breakout_8 + volume_26 | -0.53% | -13.59% | -0.16% | -0.03% | 17.33% |
| reversion_12 AND volume_26 | -0.15% | -5.45% | -0.16% | -0.01% | 4.20% |
| reversion_12 + volume_26 | -1.42% | -10.69% | -0.16% | -0.03% | 18.77% |
| ema_12_26 | -0.57% | -3.04% | -0.16% | -0.08% | 50.66% |
| macd_12_26_9 | 1.65% | -1.30% | -0.16% | -0.04% | 27.56% |
| rsi_14_recovery | 0.01% | -2.07% | -0.16% | -0.00% | 1.31% |
| bollinger_20_reentry | -0.25% | -5.16% | -0.16% | -0.01% | 3.15% |
| donchian_20 | 0.36% | -5.77% | -0.16% | -0.01% | 8.14% |
| atr_14_breakout | -1.05% | -8.25% | -0.16% | -0.01% | 5.51% |
| session_vwap | 1.03% | -6.72% | -0.16% | -0.08% | 49.34% |
| obv_20 | -0.10% | -8.53% | -0.16% | -0.07% | 43.04% |
| stochastic_14_3_recovery | 0.50% | -11.77% | -0.16% | -0.01% | 8.14% |
| mfi_14_recovery | -0.06% | -2.95% | -0.16% | -0.00% | 1.84% |
| adx_14_trend | -0.70% | -5.19% | -0.16% | -0.06% | 36.22% |
| aroon_25_trend | 0.77% | -2.56% | -0.16% | -0.04% | 25.98% |
| cci_20_momentum | 0.66% | -5.09% | -0.16% | -0.04% | 23.88% |
| williams_14_recovery | 1.01% | -6.74% | -0.16% | -0.01% | 4.99% |
| cmf_20_accumulation | 0.58% | -6.35% | -0.16% | -0.05% | 30.45% |
| chaikin_3_10 | 1.10% | -8.59% | -0.16% | -0.07% | 41.73% |
| roc_10_momentum | 0.15% | -0.27% | -0.16% | -0.00% | 1.31% |
| trix_15_trend | -0.33% | -4.03% | -0.16% | -0.07% | 42.52% |
| keltner_20_breakout | 0.33% | -5.79% | -0.16% | -0.03% | 16.80% |
| opening_range_30m | 0.81% | -5.34% | -0.16% | -0.03% | 21.00% |

동일 구간·초기 자금, 종료 시 청산 비용 포함. 노출 맞춤은 사후 설명용이며 v2 실제 계좌 성과가 아닙니다.
[낙폭 분해·비용 영향·전체 구간](DIA/comparison.json)

[v1 전체 기록](DIA/accounts.json) · [v2 전체 기록](DIA/accounts-v2.json)

## MSFT 계좌

| 모델 | 전략 | 평가액 USD | 손익 USD | 최근 매매·이유 |
|---|---|---:|---:|---|
| v1 | cash | 10000.00 | 0.00 | 대기 /  / 새 신호 대기 |
| v1 | buy_hold | 9698.19 | -301.81 | buy /  / buy_hold: prior completed bar target 100%; next bar open simulation |
| v1 | trend_8_26 | 9853.68 | -146.32 | sell /  / trend_8_26: prior completed bar target 0%; next bar open simulation |
| v1 | momentum_26 | 9839.32 | -160.68 | sell /  / momentum_26: prior completed bar target 0%; next bar open simulation |
| v1 | breakout_8 | 10000.00 | 0.00 | 대기 /  / 새 신호 대기 |
| v1 | reversion_12 | 9766.96 | -233.04 | buy /  / reversion_12: prior completed bar target 100%; next bar open simulation |
| v1 | volume_26 | 9938.00 | -62.00 | sell /  / volume_26: prior completed bar target 0%; next bar open simulation |
| v1 | trend_8_26 AND momentum_26 | 9853.68 | -146.32 | sell /  / trend_8_26 AND momentum_26: prior completed bar target 0%; next bar open simulation |
| v1 | trend_8_26 + momentum_26 | 9846.52 | -153.48 | sell /  / trend_8_26 + momentum_26: prior completed bar target 0%; next bar open simulation |
| v1 | trend_8_26 AND breakout_8 | 10000.00 | 0.00 | 대기 /  / 새 신호 대기 |
| v1 | trend_8_26 + breakout_8 | 9926.58 | -73.42 | sell /  / trend_8_26 + breakout_8: prior completed bar target 0%; next bar open simulation |
| v1 | trend_8_26 AND reversion_12 | 9923.56 | -76.44 | sell /  / trend_8_26 AND reversion_12: prior completed bar target 0%; next bar open simulation |
| v1 | trend_8_26 + reversion_12 | 9810.20 | -189.80 | buy /  / trend_8_26 + reversion_12: prior completed bar target 50%; next bar open simulation |
| v1 | trend_8_26 AND volume_26 | 10000.00 | 0.00 | 대기 /  / 새 신호 대기 |
| v1 | trend_8_26 + volume_26 | 9895.73 | -104.27 | sell /  / trend_8_26 + volume_26: prior completed bar target 0%; next bar open simulation |
| v1 | momentum_26 AND breakout_8 | 10000.00 | 0.00 | 대기 /  / 새 신호 대기 |
| v1 | momentum_26 + breakout_8 | 9919.33 | -80.67 | sell /  / momentum_26 + breakout_8: prior completed bar target 0%; next bar open simulation |
| v1 | momentum_26 AND reversion_12 | 9909.10 | -90.90 | sell /  / momentum_26 AND reversion_12: prior completed bar target 0%; next bar open simulation |
| v1 | momentum_26 + reversion_12 | 9803.05 | -196.95 | buy /  / momentum_26 + reversion_12: prior completed bar target 50%; next bar open simulation |
| v1 | momentum_26 AND volume_26 | 10000.00 | 0.00 | 대기 /  / 새 신호 대기 |
| v1 | momentum_26 + volume_26 | 9888.51 | -111.49 | sell /  / momentum_26 + volume_26: prior completed bar target 0%; next bar open simulation |
| v1 | breakout_8 AND reversion_12 | 10000.00 | 0.00 | 대기 /  / 새 신호 대기 |
| v1 | breakout_8 + reversion_12 | 9882.74 | -117.26 | buy /  / breakout_8 + reversion_12: prior completed bar target 50%; next bar open simulation |
| v1 | breakout_8 AND volume_26 | 10000.00 | 0.00 | 대기 /  / 새 신호 대기 |
| v1 | breakout_8 + volume_26 | 9968.93 | -31.07 | sell /  / breakout_8 + volume_26: prior completed bar target 0%; next bar open simulation |
| v1 | reversion_12 AND volume_26 | 9938.00 | -62.00 | sell /  / reversion_12 AND volume_26: prior completed bar target 0%; next bar open simulation |
| v1 | reversion_12 + volume_26 | 9852.06 | -147.94 | buy /  / reversion_12 + volume_26: prior completed bar target 50%; next bar open simulation |
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
| v2 | buy_hold | 9751.10 | -248.90 | buy / partial / 직전 완료 봉 목표 비중 100%; 다음 봉 시가 가정 |
| v2 | trend_8_26 | 9790.17 | -209.83 | sell / filled / 직전 완료 봉 목표 비중 0%; 다음 봉 시가 가정 |
| v2 | momentum_26 | 9886.18 | -113.82 | sell / filled / 직전 완료 봉 목표 비중 0%; 다음 봉 시가 가정 |
| v2 | breakout_8 | 9799.48 | -200.52 | sell / filled / 직전 완료 봉 목표 비중 0%; 다음 봉 시가 가정 |
| v2 | reversion_12 | 9393.53 | -606.47 | buy / partial / 직전 완료 봉 목표 비중 100%; 다음 봉 시가 가정 |
| v2 | volume_26 | 9626.55 | -373.45 | sell / filled / 직전 완료 봉 목표 비중 0%; 다음 봉 시가 가정 |
| v2 | trend_8_26 AND momentum_26 | 9751.13 | -248.87 | sell / filled / 직전 완료 봉 목표 비중 0%; 다음 봉 시가 가정 |
| v2 | trend_8_26 + momentum_26 | 9838.34 | -161.66 | sell / filled / 직전 완료 봉 목표 비중 0%; 다음 봉 시가 가정 |
| v2 | trend_8_26 AND breakout_8 | 9639.29 | -360.71 | sell / filled / 직전 완료 봉 목표 비중 0%; 다음 봉 시가 가정 |
| v2 | trend_8_26 + breakout_8 | 9815.63 | -184.37 | sell / filled / 직전 완료 봉 목표 비중 0%; 다음 봉 시가 가정 |
| v2 | trend_8_26 AND reversion_12 | 9822.46 | -177.54 | sell / filled / 직전 완료 봉 목표 비중 0%; 다음 봉 시가 가정 |
| v2 | trend_8_26 + reversion_12 | 9589.45 | -410.55 | buy / filled / 직전 완료 봉 목표 비중 50%; 다음 봉 시가 가정 |
| v2 | trend_8_26 AND volume_26 | 9948.66 | -51.34 | sell / filled / 직전 완료 봉 목표 비중 0%; 다음 봉 시가 가정 |
| v2 | trend_8_26 + volume_26 | 9728.21 | -271.79 | sell / filled / 직전 완료 봉 목표 비중 0%; 다음 봉 시가 가정 |
| v2 | momentum_26 AND breakout_8 | 9794.38 | -205.62 | sell / filled / 직전 완료 봉 목표 비중 0%; 다음 봉 시가 가정 |
| v2 | momentum_26 + breakout_8 | 9842.81 | -157.19 | sell / filled / 직전 완료 봉 목표 비중 0%; 다음 봉 시가 가정 |
| v2 | momentum_26 AND reversion_12 | 9735.61 | -264.39 | sell / filled / 직전 완료 봉 목표 비중 0%; 다음 봉 시가 가정 |
| v2 | momentum_26 + reversion_12 | 9636.48 | -363.52 | buy / filled / 직전 완료 봉 목표 비중 50%; 다음 봉 시가 가정 |
| v2 | momentum_26 AND volume_26 | 9871.26 | -128.74 | sell / filled / 직전 완료 봉 목표 비중 0%; 다음 봉 시가 가정 |
| v2 | momentum_26 + volume_26 | 9775.92 | -224.08 | sell / filled / 직전 완료 봉 목표 비중 0%; 다음 봉 시가 가정 |
| v2 | breakout_8 AND reversion_12 | 10000.00 | 0.00 | 대기 /  / 새 신호 대기 |
| v2 | breakout_8 + reversion_12 | 9614.27 | -385.73 | buy / filled / 직전 완료 봉 목표 비중 50%; 다음 봉 시가 가정 |
| v2 | breakout_8 AND volume_26 | 9938.59 | -61.41 | sell / filled / 직전 완료 봉 목표 비중 0%; 다음 봉 시가 가정 |
| v2 | breakout_8 + volume_26 | 9733.07 | -266.93 | sell / filled / 직전 완료 봉 목표 비중 0%; 다음 봉 시가 가정 |
| v2 | reversion_12 AND volume_26 | 9699.57 | -300.43 | sell / filled / 직전 완료 봉 목표 비중 0%; 다음 봉 시가 가정 |
| v2 | reversion_12 + volume_26 | 9509.13 | -490.87 | buy / filled / 직전 완료 봉 목표 비중 50%; 다음 봉 시가 가정 |
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
| cash | 0.00% | 0.00% | 1.46% | 0.00% | 0.00% |
| buy_hold | 1.89% | 1.46% | 1.46% | 1.46% | 100.00% |
| trend_8_26 | -1.30% | -4.96% | 1.46% | 0.82% | 56.43% |
| momentum_26 | -0.31% | -6.01% | 1.46% | 0.83% | 57.22% |
| breakout_8 | 5.09% | -8.89% | 1.46% | 0.28% | 19.69% |
| reversion_12 | -6.07% | -14.72% | 1.46% | 0.39% | 26.77% |
| volume_26 | 2.21% | -6.42% | 1.46% | 0.12% | 8.66% |
| trend_8_26 AND momentum_26 | -1.56% | -7.18% | 1.46% | 0.73% | 50.66% |
| trend_8_26 + momentum_26 | -0.80% | -5.47% | 1.46% | 0.82% | 56.83% |
| trend_8_26 AND breakout_8 | 0.68% | -8.98% | 1.46% | 0.18% | 12.60% |
| trend_8_26 + breakout_8 | 1.87% | -6.54% | 1.46% | 0.55% | 38.06% |
| trend_8_26 AND reversion_12 | -3.72% | -9.22% | 1.46% | 0.11% | 7.35% |
| trend_8_26 + reversion_12 | -3.69% | -9.59% | 1.46% | 0.60% | 41.61% |
| trend_8_26 AND volume_26 | 3.46% | 0.46% | 1.46% | 0.04% | 2.62% |
| trend_8_26 + volume_26 | 0.46% | -4.90% | 1.46% | 0.47% | 32.55% |
| momentum_26 AND breakout_8 | 2.61% | -7.61% | 1.46% | 0.18% | 12.86% |
| momentum_26 + breakout_8 | 2.37% | -6.87% | 1.46% | 0.56% | 38.46% |
| momentum_26 AND reversion_12 | -3.21% | -9.50% | 1.46% | 0.13% | 8.92% |
| momentum_26 + reversion_12 | -3.21% | -10.09% | 1.46% | 0.61% | 42.00% |
| momentum_26 AND volume_26 | 1.80% | -2.38% | 1.46% | 0.05% | 3.41% |
| momentum_26 + volume_26 | 0.96% | -5.02% | 1.46% | 0.48% | 32.94% |
| breakout_8 AND reversion_12 | 0.00% | 0.00% | 1.46% | 0.00% | 0.00% |
| breakout_8 + reversion_12 | -0.62% | -11.29% | 1.46% | 0.33% | 23.24% |
| breakout_8 AND volume_26 | 2.07% | -0.47% | 1.46% | 0.03% | 1.84% |
| breakout_8 + volume_26 | 3.65% | -6.69% | 1.46% | 0.20% | 14.18% |
| reversion_12 AND volume_26 | -2.48% | -6.49% | 1.46% | 0.06% | 3.94% |
| reversion_12 + volume_26 | -2.00% | -10.47% | 1.46% | 0.26% | 17.72% |
| ema_12_26 | -0.71% | -4.39% | 1.46% | 0.87% | 60.10% |
| macd_12_26_9 | 0.71% | -4.24% | 1.46% | 0.47% | 32.81% |
| rsi_14_recovery | -0.46% | -1.71% | 1.46% | 0.01% | 0.79% |
| bollinger_20_reentry | -0.52% | -3.81% | 1.46% | 0.03% | 2.10% |
| donchian_20 | 1.84% | -3.17% | 1.46% | 0.06% | 4.46% |
| atr_14_breakout | 1.50% | -3.89% | 1.46% | 0.05% | 3.67% |
| session_vwap | 2.82% | -5.07% | 1.46% | 0.66% | 45.41% |
| obv_20 | 4.17% | -4.62% | 1.46% | 0.74% | 51.18% |
| stochastic_14_3_recovery | -0.68% | -10.95% | 1.46% | 0.10% | 6.82% |
| mfi_14_recovery | 1.04% | -1.88% | 1.46% | 0.03% | 1.84% |
| adx_14_trend | 1.30% | -1.64% | 1.46% | 0.63% | 43.83% |
| aroon_25_trend | 0.23% | -4.29% | 1.46% | 0.29% | 20.47% |
| cci_20_momentum | 2.74% | -3.54% | 1.46% | 0.29% | 20.47% |
| williams_14_recovery | -0.28% | -9.09% | 1.46% | 0.08% | 5.77% |
| cmf_20_accumulation | 0.57% | -5.18% | 1.46% | 0.52% | 35.70% |
| chaikin_3_10 | 3.42% | -4.51% | 1.46% | 0.65% | 44.62% |
| roc_10_momentum | -0.20% | -4.30% | 1.46% | 0.20% | 14.17% |
| trix_15_trend | -1.57% | -5.62% | 1.46% | 0.67% | 46.19% |
| keltner_20_breakout | 1.12% | -3.85% | 1.46% | 0.19% | 13.39% |
| opening_range_30m | -2.08% | -6.89% | 1.46% | 0.34% | 23.62% |

동일 구간·초기 자금, 종료 시 청산 비용 포함. 노출 맞춤은 사후 설명용이며 v2 실제 계좌 성과가 아닙니다.
[낙폭 분해·비용 영향·전체 구간](MSFT/comparison.json)

[v1 전체 기록](MSFT/accounts.json) · [v2 전체 기록](MSFT/accounts-v2.json)

## JPM 계좌

| 모델 | 전략 | 평가액 USD | 손익 USD | 최근 매매·이유 |
|---|---|---:|---:|---|
| v1 | cash | 10000.00 | 0.00 | 대기 /  / 새 신호 대기 |
| v1 | buy_hold | 9939.07 | -60.93 | buy /  / buy_hold: prior completed bar target 100%; next bar open simulation |
| v1 | trend_8_26 | 9939.07 | -60.93 | buy /  / trend_8_26: prior completed bar target 100%; next bar open simulation |
| v1 | momentum_26 | 9939.07 | -60.93 | buy /  / momentum_26: prior completed bar target 100%; next bar open simulation |
| v1 | breakout_8 | 9915.55 | -84.45 | sell /  / breakout_8: prior completed bar target 0%; next bar open simulation |
| v1 | reversion_12 | 9925.64 | -74.36 | buy /  / reversion_12: prior completed bar target 100%; next bar open simulation |
| v1 | volume_26 | 10035.68 | 35.68 | sell /  / volume_26: prior completed bar target 0%; next bar open simulation |
| v1 | trend_8_26 AND momentum_26 | 9939.07 | -60.93 | buy /  / trend_8_26 AND momentum_26: prior completed bar target 100%; next bar open simulation |
| v1 | trend_8_26 + momentum_26 | 9939.07 | -60.93 | buy /  / trend_8_26 + momentum_26: prior completed bar target 100%; next bar open simulation |
| v1 | trend_8_26 AND breakout_8 | 9915.55 | -84.45 | sell /  / trend_8_26 AND breakout_8: prior completed bar target 0%; next bar open simulation |
| v1 | trend_8_26 + breakout_8 | 9927.38 | -72.62 | buy /  / trend_8_26 + breakout_8: prior completed bar target 50%; next bar open simulation |
| v1 | trend_8_26 AND reversion_12 | 9925.64 | -74.36 | buy /  / trend_8_26 AND reversion_12: prior completed bar target 100%; next bar open simulation |
| v1 | trend_8_26 + reversion_12 | 9932.36 | -67.64 | buy /  / trend_8_26 + reversion_12: prior completed bar target 100%; next bar open simulation |
| v1 | trend_8_26 AND volume_26 | 10035.68 | 35.68 | sell /  / trend_8_26 AND volume_26: prior completed bar target 0%; next bar open simulation |
| v1 | trend_8_26 + volume_26 | 9987.21 | -12.79 | buy /  / trend_8_26 + volume_26: prior completed bar target 50%; next bar open simulation |
| v1 | momentum_26 AND breakout_8 | 9915.55 | -84.45 | sell /  / momentum_26 AND breakout_8: prior completed bar target 0%; next bar open simulation |
| v1 | momentum_26 + breakout_8 | 9927.38 | -72.62 | buy /  / momentum_26 + breakout_8: prior completed bar target 50%; next bar open simulation |
| v1 | momentum_26 AND reversion_12 | 9925.64 | -74.36 | buy /  / momentum_26 AND reversion_12: prior completed bar target 100%; next bar open simulation |
| v1 | momentum_26 + reversion_12 | 9932.36 | -67.64 | buy /  / momentum_26 + reversion_12: prior completed bar target 100%; next bar open simulation |
| v1 | momentum_26 AND volume_26 | 10035.68 | 35.68 | sell /  / momentum_26 AND volume_26: prior completed bar target 0%; next bar open simulation |
| v1 | momentum_26 + volume_26 | 9987.21 | -12.79 | buy /  / momentum_26 + volume_26: prior completed bar target 50%; next bar open simulation |
| v1 | breakout_8 AND reversion_12 | 10000.00 | 0.00 | 대기 /  / 새 신호 대기 |
| v1 | breakout_8 + reversion_12 | 9920.63 | -79.37 | buy /  / breakout_8 + reversion_12: prior completed bar target 50%; next bar open simulation |
| v1 | breakout_8 AND volume_26 | 10035.68 | 35.68 | sell /  / breakout_8 AND volume_26: prior completed bar target 0%; next bar open simulation |
| v1 | breakout_8 + volume_26 | 9975.44 | -24.56 | sell /  / breakout_8 + volume_26: prior completed bar target 0%; next bar open simulation |
| v1 | reversion_12 AND volume_26 | 10000.00 | 0.00 | 대기 /  / 새 신호 대기 |
| v1 | reversion_12 + volume_26 | 9980.54 | -19.46 | buy /  / reversion_12 + volume_26: prior completed bar target 50%; next bar open simulation |
| v1 | ema_12_26 | 9939.07 | -60.93 | buy /  / EMA12 > EMA26; 조건 충족; EMA12=334.708, EMA26=334.451 |
| v1 | macd_12_26_9 | 9973.56 | -26.44 | sell /  / MACD > 신호선 그리고 MACD > 0; 조건 미충족; MACD=1.87003, signal9=1.96381 |
| v1 | rsi_14_recovery | 10000.00 | 0.00 | 대기 /  / 새 신호 대기 |
| v1 | bollinger_20_reentry | 10000.00 | 0.00 | 대기 /  / 새 신호 대기 |
| v1 | donchian_20 | 9872.30 | -127.70 | sell /  / 종가 > 현재 봉을 제외한 직전 20봉 최고가; 조건 미충족; close=343.037, prior_high20=344.4 |
| v1 | atr_14_breakout | 9886.92 | -113.08 | sell /  / 종가 > 직전 종가 + 직전 ATR14 그리고 종가 > EMA26; 조건 미충족; close=342.515, threshold=344.598, prior_ATR14=1.50332, EMA26=336.975 |
| v1 | session_vwap | 9936.81 | -63.19 | sell /  / 종가 > 뉴욕 거래일별 누적 전형가격 VWAP; 조건 미충족; close=342, session_VWAP=342.233, session_volume=3.25898e+06 |
| v1 | obv_20 | 10007.55 | 7.55 | sell /  / OBV > OBV의 SMA20 그리고 종가 > EMA26; 조건 미충족; OBV=-1.38544e+07, OBV_SMA20=-1.10099e+07, close=341.625, EMA26=338.807 |
| v1 | stochastic_14_3_recovery | 10000.00 | 0.00 | 대기 /  / 새 신호 대기 |
| v1 | mfi_14_recovery | 10000.00 | 0.00 | 대기 /  / 새 신호 대기 |
| v1 | adx_14_trend | 9806.96 | -193.04 | sell /  / Wilder ADX14 >= 25 그리고 +DI14 > -DI14; 조건 미충족; ADX14=30.1815, plus_DI14=27.5695, minus_DI14=29.9812 |
| v1 | aroon_25_trend | 9824.71 | -175.29 | sell /  / Aroon25 Up > 70 그리고 Down < 30 (동률이면 최신 극값); 조건 미충족; Aroon_up=68, Aroon_down=16 |
| v1 | cci_20_momentum | 10050.62 | 50.62 | sell /  / CCI20 > 100 (전형가격·평균절대편차); 조건 미충족; CCI20=93.5627 |
| v1 | williams_14_recovery | 10000.00 | 0.00 | 대기 /  / 새 신호 대기 |
| v1 | cmf_20_accumulation | 9932.16 | -67.84 | sell /  / Chaikin Money Flow20 > 0.1; 조건 미충족; CMF20=-0.14511, volume20=9.3038e+06 |
| v1 | chaikin_3_10 | 10007.55 | 7.55 | sell /  / ADL의 EMA3 - EMA10 > 0 그리고 종가 > EMA26; 조건 미충족; Chaikin3_10=-655976, ADL=-7.91325e+06, close=341.625, EMA26=338.807 |
| v1 | roc_10_momentum | 9913.84 | -86.16 | sell /  / 10봉 ROC > 1% 그리고 종가 > EMA26; 조건 미충족; ROC10_percent=-0.490038, close=340.901, EMA26=338.962 |
| v1 | trix_15_trend | 9923.45 | -76.55 | sell /  / 15봉 삼중 EMA의 1봉 변화율 TRIX > 0 그리고 종가 > EMA26; 조건 미충족; TRIX15_percent=0.0809094, close=339.06, EMA26=339.114 |
| v1 | keltner_20_breakout | 9946.99 | -53.01 | sell /  / 종가 > EMA20 + 2 x Wilder ATR14; 조건 미충족; close=342, upper_Keltner=342.276, EMA20=339.397, ATR14=1.43933 |
| v1 | opening_range_30m | 9927.81 | -72.19 | sell /  / 뉴욕 09:30·09:45 두 완료 봉 최고가를 10:00 이후 종가가 돌파; 조건 미충족; close=343.037, opening_high=343.75 |
| v2 | cash | 10000.00 | 0.00 | 대기 /  / 새 신호 대기 |
| v2 | buy_hold | 10105.15 | 105.15 | buy / partial / 직전 완료 봉 목표 비중 100%; 다음 봉 시가 가정 |
| v2 | trend_8_26 | 9947.21 | -52.79 | buy / partial / 직전 완료 봉 목표 비중 100%; 다음 봉 시가 가정 |
| v2 | momentum_26 | 9446.74 | -553.26 | buy / partial / 직전 완료 봉 목표 비중 100%; 다음 봉 시가 가정 |
| v2 | breakout_8 | 9251.20 | -748.80 | sell / filled / 직전 완료 봉 목표 비중 0%; 다음 봉 시가 가정 |
| v2 | reversion_12 | 9916.68 | -83.32 | buy / partial / 직전 완료 봉 목표 비중 100%; 다음 봉 시가 가정 |
| v2 | volume_26 | 9859.79 | -140.21 | sell / filled / 직전 완료 봉 목표 비중 0%; 다음 봉 시가 가정 |
| v2 | trend_8_26 AND momentum_26 | 9906.39 | -93.61 | buy / partial / 직전 완료 봉 목표 비중 100%; 다음 봉 시가 가정 |
| v2 | trend_8_26 + momentum_26 | 9714.66 | -285.34 | buy / partial / 직전 완료 봉 목표 비중 100%; 다음 봉 시가 가정 |
| v2 | trend_8_26 AND breakout_8 | 9287.76 | -712.24 | sell / filled / 직전 완료 봉 목표 비중 0%; 다음 봉 시가 가정 |
| v2 | trend_8_26 + breakout_8 | 9594.03 | -405.97 | buy / filled / 직전 완료 봉 목표 비중 50%; 다음 봉 시가 가정 |
| v2 | trend_8_26 AND reversion_12 | 9906.40 | -93.60 | buy / partial / 직전 완료 봉 목표 비중 100%; 다음 봉 시가 가정 |
| v2 | trend_8_26 + reversion_12 | 9973.97 | -26.03 | buy / partial / 직전 완료 봉 목표 비중 100%; 다음 봉 시가 가정 |
| v2 | trend_8_26 AND volume_26 | 9833.30 | -166.70 | sell / filled / 직전 완료 봉 목표 비중 0%; 다음 봉 시가 가정 |
| v2 | trend_8_26 + volume_26 | 9904.20 | -95.80 | buy / filled / 직전 완료 봉 목표 비중 50%; 다음 봉 시가 가정 |
| v2 | momentum_26 AND breakout_8 | 9232.70 | -767.30 | sell / filled / 직전 완료 봉 목표 비중 0%; 다음 봉 시가 가정 |
| v2 | momentum_26 + breakout_8 | 9369.79 | -630.21 | buy / filled / 직전 완료 봉 목표 비중 50%; 다음 봉 시가 가정 |
| v2 | momentum_26 AND reversion_12 | 9875.78 | -124.22 | buy / partial / 직전 완료 봉 목표 비중 100%; 다음 봉 시가 가정 |
| v2 | momentum_26 + reversion_12 | 9802.16 | -197.84 | buy / partial / 직전 완료 봉 목표 비중 100%; 다음 봉 시가 가정 |
| v2 | momentum_26 AND volume_26 | 9833.30 | -166.70 | sell / filled / 직전 완료 봉 목표 비중 0%; 다음 봉 시가 가정 |
| v2 | momentum_26 + volume_26 | 9713.26 | -286.74 | buy / filled / 직전 완료 봉 목표 비중 50%; 다음 봉 시가 가정 |
| v2 | breakout_8 AND reversion_12 | 10000.00 | 0.00 | 대기 /  / 새 신호 대기 |
| v2 | breakout_8 + reversion_12 | 9618.75 | -381.25 | buy / filled / 직전 완료 봉 목표 비중 50%; 다음 봉 시가 가정 |
| v2 | breakout_8 AND volume_26 | 9926.66 | -73.34 | sell / filled / 직전 완료 봉 목표 비중 0%; 다음 봉 시가 가정 |
| v2 | breakout_8 + volume_26 | 9570.88 | -429.12 | sell / filled / 직전 완료 봉 목표 비중 0%; 다음 봉 시가 가정 |
| v2 | reversion_12 AND volume_26 | 10051.38 | 51.38 | sell / filled / 직전 완료 봉 목표 비중 0%; 다음 봉 시가 가정 |
| v2 | reversion_12 + volume_26 | 9909.30 | -90.70 | buy / filled / 직전 완료 봉 목표 비중 50%; 다음 봉 시가 가정 |
| v2 | ema_12_26 | 9938.08 | -61.92 | buy / partial / EMA12 > EMA26; 조건 충족; EMA12=334.708, EMA26=334.451; 직전 완료 봉 목표를 다음 봉 시가에 모의 적용 |
| v2 | macd_12_26_9 | 9971.56 | -28.44 | sell / filled / MACD > 신호선 그리고 MACD > 0; 조건 미충족; MACD=1.87003, signal9=1.96381; 직전 완료 봉 목표를 다음 봉 시가에 모의 적용 |
| v2 | rsi_14_recovery | 10000.00 | 0.00 | 대기 /  / 새 신호 대기 |
| v2 | bollinger_20_reentry | 10000.00 | 0.00 | 대기 /  / 새 신호 대기 |
| v2 | donchian_20 | 9868.35 | -131.65 | sell / filled / 종가 > 현재 봉을 제외한 직전 20봉 최고가; 조건 미충족; close=343.037, prior_high20=344.4; 직전 완료 봉 목표를 다음 봉 시가에 모의 적용 |
| v2 | atr_14_breakout | 9882.97 | -117.03 | sell / filled / 종가 > 직전 종가 + 직전 ATR14 그리고 종가 > EMA26; 조건 미충족; close=342.515, threshold=344.598, prior_ATR14=1.50332, EMA26=336.975; 직전 완료 봉 목표를 다음 봉 시가에 모의 적용 |
| v2 | session_vwap | 9932.83 | -67.17 | sell / filled / 종가 > 뉴욕 거래일별 누적 전형가격 VWAP; 조건 미충족; close=342, session_VWAP=342.233, session_volume=3.25898e+06; 직전 완료 봉 목표를 다음 봉 시가에 모의 적용 |
| v2 | obv_20 | 10005.55 | 5.55 | sell / filled / OBV > OBV의 SMA20 그리고 종가 > EMA26; 조건 미충족; OBV=-1.38544e+07, OBV_SMA20=-1.10099e+07, close=341.625, EMA26=338.807; 직전 완료 봉 목표를 다음 봉 시가에 모의 적용 |
| v2 | stochastic_14_3_recovery | 10000.00 | 0.00 | 대기 /  / 새 신호 대기 |
| v2 | mfi_14_recovery | 10000.00 | 0.00 | 대기 /  / 새 신호 대기 |
| v2 | adx_14_trend | 9805.00 | -195.00 | sell / filled / Wilder ADX14 >= 25 그리고 +DI14 > -DI14; 조건 미충족; ADX14=30.1815, plus_DI14=27.5695, minus_DI14=29.9812; 직전 완료 봉 목표를 다음 봉 시가에 모의 적용 |
| v2 | aroon_25_trend | 9822.74 | -177.26 | sell / filled / Aroon25 Up > 70 그리고 Down < 30 (동률이면 최신 극값); 조건 미충족; Aroon_up=68, Aroon_down=16; 직전 완료 봉 목표를 다음 봉 시가에 모의 적용 |
| v2 | cci_20_momentum | 10048.61 | 48.61 | sell / filled / CCI20 > 100 (전형가격·평균절대편차); 조건 미충족; CCI20=93.5627; 직전 완료 봉 목표를 다음 봉 시가에 모의 적용 |
| v2 | williams_14_recovery | 10000.00 | 0.00 | 대기 /  / 새 신호 대기 |
| v2 | cmf_20_accumulation | 9930.17 | -69.83 | sell / filled / Chaikin Money Flow20 > 0.1; 조건 미충족; CMF20=-0.14511, volume20=9.3038e+06; 직전 완료 봉 목표를 다음 봉 시가에 모의 적용 |
| v2 | chaikin_3_10 | 10005.55 | 5.55 | sell / filled / ADL의 EMA3 - EMA10 > 0 그리고 종가 > EMA26; 조건 미충족; Chaikin3_10=-655976, ADL=-7.91325e+06, close=341.625, EMA26=338.807; 직전 완료 봉 목표를 다음 봉 시가에 모의 적용 |
| v2 | roc_10_momentum | 9911.86 | -88.14 | sell / filled / 10봉 ROC > 1% 그리고 종가 > EMA26; 조건 미충족; ROC10_percent=-0.490038, close=340.901, EMA26=338.962; 직전 완료 봉 목표를 다음 봉 시가에 모의 적용 |
| v2 | trix_15_trend | 9921.47 | -78.53 | sell / filled / 15봉 삼중 EMA의 1봉 변화율 TRIX > 0 그리고 종가 > EMA26; 조건 미충족; TRIX15_percent=0.0809094, close=339.06, EMA26=339.114; 직전 완료 봉 목표를 다음 봉 시가에 모의 적용 |
| v2 | keltner_20_breakout | 9945.00 | -55.00 | sell / filled / 종가 > EMA20 + 2 x Wilder ATR14; 조건 미충족; close=342, upper_Keltner=342.276, EMA20=339.397, ATR14=1.43933; 직전 완료 봉 목표를 다음 봉 시가에 모의 적용 |
| v2 | opening_range_30m | 9925.82 | -74.18 | sell / filled / 뉴욕 09:30·09:45 두 완료 봉 최고가를 10:00 이후 종가가 돌파; 조건 미충족; close=343.037, opening_high=343.75; 직전 완료 봉 목표를 다음 봉 시가에 모의 적용 |

### 같은 기간의 비용·노출 비교 (사후 연구)

| 전략 | 비용 전 | 비용 후 | 100% 보유 | 같은 평균 노출 보유 | 평균 노출 |
|---|---:|---:|---:|---:|---:|
| cash | 0.00% | 0.00% | -1.60% | -0.00% | 0.00% |
| buy_hold | -1.19% | -1.60% | -1.60% | -1.60% | 100.00% |
| trend_8_26 | 0.34% | -3.79% | -1.60% | -0.85% | 52.49% |
| momentum_26 | -2.70% | -9.41% | -1.60% | -0.76% | 46.98% |
| breakout_8 | -3.71% | -18.60% | -1.60% | -0.33% | 19.95% |
| reversion_12 | 4.06% | -10.54% | -1.60% | -0.45% | 27.56% |
| volume_26 | -0.11% | -6.20% | -1.60% | -0.11% | 6.82% |
| trend_8_26 AND momentum_26 | 0.43% | -4.50% | -1.60% | -0.67% | 41.21% |
| trend_8_26 + momentum_26 | -1.18% | -6.44% | -1.60% | -0.81% | 49.74% |
| trend_8_26 AND breakout_8 | -3.76% | -14.07% | -1.60% | -0.21% | 12.60% |
| trend_8_26 + breakout_8 | -1.69% | -11.31% | -1.60% | -0.59% | 36.23% |
| trend_8_26 AND reversion_12 | 2.26% | -4.38% | -1.60% | -0.13% | 7.61% |
| trend_8_26 + reversion_12 | 2.21% | -6.64% | -1.60% | -0.65% | 40.03% |
| trend_8_26 AND volume_26 | -0.58% | -4.67% | -1.60% | -0.07% | 4.20% |
| trend_8_26 + volume_26 | 0.14% | -5.00% | -1.60% | -0.48% | 29.66% |
| momentum_26 AND breakout_8 | -2.60% | -13.04% | -1.60% | -0.20% | 12.34% |
| momentum_26 + breakout_8 | -3.19% | -13.93% | -1.60% | -0.55% | 33.47% |
| momentum_26 AND reversion_12 | 2.32% | -4.73% | -1.60% | -0.11% | 6.56% |
| momentum_26 + reversion_12 | 0.65% | -8.45% | -1.60% | -0.61% | 37.28% |
| momentum_26 AND volume_26 | 0.21% | -2.70% | -1.60% | -0.05% | 2.89% |
| momentum_26 + volume_26 | -1.39% | -7.23% | -1.60% | -0.44% | 26.91% |
| breakout_8 AND reversion_12 | 0.00% | 0.00% | -1.60% | -0.00% | 0.00% |
| breakout_8 + reversion_12 | 0.12% | -13.22% | -1.60% | -0.39% | 23.76% |
| breakout_8 AND volume_26 | -0.51% | -2.17% | -1.60% | -0.02% | 1.05% |
| breakout_8 + volume_26 | -1.91% | -11.52% | -1.60% | -0.22% | 13.39% |
| reversion_12 AND volume_26 | 1.25% | -2.10% | -1.60% | -0.06% | 3.41% |
| reversion_12 + volume_26 | 1.97% | -7.63% | -1.60% | -0.28% | 17.20% |
| ema_12_26 | -0.00% | -3.31% | -1.60% | -0.79% | 48.82% |
| macd_12_26_9 | 0.83% | -3.32% | -1.60% | -0.51% | 30.97% |
| rsi_14_recovery | 0.14% | -2.35% | -1.60% | -0.03% | 1.57% |
| bollinger_20_reentry | 0.44% | -5.30% | -1.60% | -0.06% | 3.67% |
| donchian_20 | -1.79% | -4.63% | -1.60% | -0.05% | 2.89% |
| atr_14_breakout | -1.13% | -7.55% | -1.60% | -0.07% | 4.46% |
| session_vwap | 0.74% | -8.92% | -1.60% | -0.78% | 47.77% |
| obv_20 | -4.05% | -15.05% | -1.60% | -0.50% | 30.71% |
| stochastic_14_3_recovery | -1.86% | -12.75% | -1.60% | -0.12% | 7.35% |
| mfi_14_recovery | 0.16% | -1.50% | -1.60% | -0.02% | 1.05% |
| adx_14_trend | -3.41% | -6.60% | -1.60% | -0.45% | 27.82% |
| aroon_25_trend | -1.62% | -6.06% | -1.60% | -0.38% | 23.10% |
| cci_20_momentum | -2.59% | -10.44% | -1.60% | -0.25% | 15.22% |
| williams_14_recovery | -2.54% | -12.98% | -1.60% | -0.12% | 7.09% |
| cmf_20_accumulation | -3.20% | -11.74% | -1.60% | -0.55% | 33.86% |
| chaikin_3_10 | 1.28% | -7.27% | -1.60% | -0.54% | 33.33% |
| roc_10_momentum | -0.98% | -3.45% | -1.60% | -0.13% | 7.87% |
| trix_15_trend | -0.99% | -7.81% | -1.60% | -0.57% | 34.65% |
| keltner_20_breakout | -1.19% | -3.65% | -1.60% | -0.06% | 3.94% |
| opening_range_30m | -0.41% | -4.11% | -1.60% | -0.28% | 17.32% |

동일 구간·초기 자금, 종료 시 청산 비용 포함. 노출 맞춤은 사후 설명용이며 v2 실제 계좌 성과가 아닙니다.
[낙폭 분해·비용 영향·전체 구간](JPM/comparison.json)

[v1 전체 기록](JPM/accounts.json) · [v2 전체 기록](JPM/accounts-v2.json)

## XOM 계좌

| 모델 | 전략 | 평가액 USD | 손익 USD | 최근 매매·이유 |
|---|---|---:|---:|---|
| v1 | cash | 10000.00 | 0.00 | 대기 /  / 새 신호 대기 |
| v1 | buy_hold | 10070.23 | 70.23 | buy /  / buy_hold: prior completed bar target 100%; next bar open simulation |
| v1 | trend_8_26 | 10131.36 | 131.36 | buy /  / trend_8_26: prior completed bar target 100%; next bar open simulation |
| v1 | momentum_26 | 10097.98 | 97.98 | buy /  / momentum_26: prior completed bar target 100%; next bar open simulation |
| v1 | breakout_8 | 9899.56 | -100.44 | buy /  / breakout_8: prior completed bar target 100%; next bar open simulation |
| v1 | reversion_12 | 10000.00 | 0.00 | 대기 /  / 새 신호 대기 |
| v1 | volume_26 | 9889.56 | -110.44 | sell /  / volume_26: prior completed bar target 0%; next bar open simulation |
| v1 | trend_8_26 AND momentum_26 | 10131.36 | 131.36 | buy /  / trend_8_26 AND momentum_26: prior completed bar target 100%; next bar open simulation |
| v1 | trend_8_26 + momentum_26 | 10114.64 | 114.64 | buy /  / trend_8_26 + momentum_26: prior completed bar target 100%; next bar open simulation |
| v1 | trend_8_26 AND breakout_8 | 10021.76 | 21.76 | buy /  / trend_8_26 AND breakout_8: prior completed bar target 100%; next bar open simulation |
| v1 | trend_8_26 + breakout_8 | 10034.85 | 34.85 | buy /  / trend_8_26 + breakout_8: prior completed bar target 100%; next bar open simulation |
| v1 | trend_8_26 AND reversion_12 | 10000.00 | 0.00 | 대기 /  / 새 신호 대기 |
| v1 | trend_8_26 + reversion_12 | 10065.43 | 65.43 | sell /  / trend_8_26 + reversion_12: prior completed bar target 50%; next bar open simulation |
| v1 | trend_8_26 AND volume_26 | 9985.49 | -14.51 | sell /  / trend_8_26 AND volume_26: prior completed bar target 0%; next bar open simulation |
| v1 | trend_8_26 + volume_26 | 10009.69 | 9.69 | sell /  / trend_8_26 + volume_26: prior completed bar target 50%; next bar open simulation |
| v1 | momentum_26 AND breakout_8 | 9948.86 | -51.14 | buy /  / momentum_26 AND breakout_8: prior completed bar target 100%; next bar open simulation |
| v1 | momentum_26 + breakout_8 | 9998.30 | -1.70 | buy /  / momentum_26 + breakout_8: prior completed bar target 100%; next bar open simulation |
| v1 | momentum_26 AND reversion_12 | 10000.00 | 0.00 | 대기 /  / 새 신호 대기 |
| v1 | momentum_26 + reversion_12 | 10048.83 | 48.83 | sell /  / momentum_26 + reversion_12: prior completed bar target 50%; next bar open simulation |
| v1 | momentum_26 AND volume_26 | 9985.49 | -14.51 | sell /  / momentum_26 AND volume_26: prior completed bar target 0%; next bar open simulation |
| v1 | momentum_26 + volume_26 | 9993.18 | -6.82 | sell /  / momentum_26 + volume_26: prior completed bar target 50%; next bar open simulation |
| v1 | breakout_8 AND reversion_12 | 10000.00 | 0.00 | 대기 /  / 새 신호 대기 |
| v1 | breakout_8 + reversion_12 | 9949.61 | -50.39 | sell /  / breakout_8 + reversion_12: prior completed bar target 50%; next bar open simulation |
| v1 | breakout_8 AND volume_26 | 9950.44 | -49.56 | sell /  / breakout_8 AND volume_26: prior completed bar target 0%; next bar open simulation |
| v1 | breakout_8 + volume_26 | 9894.50 | -105.50 | sell /  / breakout_8 + volume_26: prior completed bar target 50%; next bar open simulation |
| v1 | reversion_12 AND volume_26 | 10000.00 | 0.00 | 대기 /  / 새 신호 대기 |
| v1 | reversion_12 + volume_26 | 9944.60 | -55.40 | sell /  / reversion_12 + volume_26: prior completed bar target 0%; next bar open simulation |
| v1 | ema_12_26 | 10128.48 | 128.48 | buy /  / EMA12 > EMA26; 조건 충족; EMA12=175.145, EMA26=175.141 |
| v1 | macd_12_26_9 | 10128.48 | 128.48 | buy /  / MACD > 신호선 그리고 MACD > 0; 조건 충족; MACD=0.00418876, signal9=-0.17046 |
| v1 | rsi_14_recovery | 10000.00 | 0.00 | 대기 /  / 새 신호 대기 |
| v1 | bollinger_20_reentry | 9913.52 | -86.48 | sell /  / 직전 종가 < 직전 하단밴드, 현재 하단밴드 <= 종가 <= SMA20 (한 봉 목표); 조건 미충족; close=175.71, lower20=173.907, SMA20=174.743, previous_lower20=173.977 |
| v1 | donchian_20 | 9950.44 | -49.56 | sell /  / 종가 > 현재 봉을 제외한 직전 20봉 최고가; 조건 미충족; close=175.56, prior_high20=177.365 |
| v1 | atr_14_breakout | 9864.96 | -135.04 | sell /  / 종가 > 직전 종가 + 직전 ATR14 그리고 종가 > EMA26; 조건 미충족; close=177.19, threshold=177.748, prior_ATR14=0.663113, EMA26=175.734 |
| v1 | session_vwap | 10029.16 | 29.16 | buy /  / 종가 > 뉴욕 거래일별 누적 전형가격 VWAP; 조건 충족; close=176.25, session_VWAP=175.945, session_volume=7.74672e+06 |
| v1 | obv_20 | 9970.37 | -29.63 | sell /  / OBV > OBV의 SMA20 그리고 종가 > EMA26; 조건 미충족; OBV=1.88162e+07, OBV_SMA20=2.13258e+07, close=175.84, EMA26=175.361 |
| v1 | stochastic_14_3_recovery | 10000.00 | 0.00 | 대기 /  / 새 신호 대기 |
| v1 | mfi_14_recovery | 10000.00 | 0.00 | 대기 /  / 새 신호 대기 |
| v1 | adx_14_trend | 10107.08 | 107.08 | buy /  / Wilder ADX14 >= 25 그리고 +DI14 > -DI14; 조건 충족; ADX14=25.0494, plus_DI14=28.5472, minus_DI14=15.0232 |
| v1 | aroon_25_trend | 10000.00 | 0.00 | 대기 /  / 새 신호 대기 |
| v1 | cci_20_momentum | 9961.90 | -38.10 | buy /  / CCI20 > 100 (전형가격·평균절대편차); 조건 충족; CCI20=102.776 |
| v1 | williams_14_recovery | 9913.52 | -86.48 | sell /  / 직전 Williams %R14 < -80, 현재 >= -80 (한 봉 목표); 조건 미충족; Williams_R14=-43.9575, previous_R14=-33.1215 |
| v1 | cmf_20_accumulation | 10000.00 | 0.00 | 대기 /  / 새 신호 대기 |
| v1 | chaikin_3_10 | 10000.00 | 0.00 | 대기 /  / 새 신호 대기 |
| v1 | roc_10_momentum | 10003.81 | 3.81 | buy /  / 10봉 ROC > 1% 그리고 종가 > EMA26; 조건 충족; ROC10_percent=1.10566, close=177.4, EMA26=175.858 |
| v1 | trix_15_trend | 10081.36 | 81.36 | buy /  / 15봉 삼중 EMA의 1봉 변화율 TRIX > 0 그리고 종가 > EMA26; 조건 충족; TRIX15_percent=0.00176833, close=176.25, EMA26=175.427 |
| v1 | keltner_20_breakout | 10034.69 | 34.69 | buy /  / 종가 > EMA20 + 2 x Wilder ATR14; 조건 충족; close=177.085, upper_Keltner=177.035, EMA20=175.709, ATR14=0.663113 |
| v1 | opening_range_30m | 10019.98 | 19.98 | buy /  / 뉴욕 09:30·09:45 두 완료 봉 최고가를 10:00 이후 종가가 돌파; 조건 충족; close=177.4, opening_high=177.365 |
| v2 | cash | 10000.00 | 0.00 | 대기 /  / 새 신호 대기 |
| v2 | buy_hold | 10391.59 | 391.59 | buy / partial / 직전 완료 봉 목표 비중 100%; 다음 봉 시가 가정 |
| v2 | trend_8_26 | 10227.86 | 227.86 | buy / partial / 직전 완료 봉 목표 비중 100%; 다음 봉 시가 가정 |
| v2 | momentum_26 | 10271.28 | 271.28 | buy / partial / 직전 완료 봉 목표 비중 100%; 다음 봉 시가 가정 |
| v2 | breakout_8 | 9369.33 | -630.67 | buy / partial / 직전 완료 봉 목표 비중 100%; 다음 봉 시가 가정 |
| v2 | reversion_12 | 9815.06 | -184.94 | sell / filled / 직전 완료 봉 목표 비중 0%; 다음 봉 시가 가정 |
| v2 | volume_26 | 9794.70 | -205.30 | sell / filled / 직전 완료 봉 목표 비중 0%; 다음 봉 시가 가정 |
| v2 | trend_8_26 AND momentum_26 | 10235.44 | 235.44 | buy / partial / 직전 완료 봉 목표 비중 100%; 다음 봉 시가 가정 |
| v2 | trend_8_26 + momentum_26 | 10249.56 | 249.56 | buy / partial / 직전 완료 봉 목표 비중 100%; 다음 봉 시가 가정 |
| v2 | trend_8_26 AND breakout_8 | 9471.46 | -528.54 | buy / partial / 직전 완료 봉 목표 비중 100%; 다음 봉 시가 가정 |
| v2 | trend_8_26 + breakout_8 | 9830.77 | -169.23 | buy / partial / 직전 완료 봉 목표 비중 100%; 다음 봉 시가 가정 |
| v2 | trend_8_26 AND reversion_12 | 9839.70 | -160.30 | sell / filled / 직전 완료 봉 목표 비중 0%; 다음 봉 시가 가정 |
| v2 | trend_8_26 + reversion_12 | 10019.39 | 19.39 | sell / filled / 직전 완료 봉 목표 비중 50%; 다음 봉 시가 가정 |
| v2 | trend_8_26 AND volume_26 | 9879.28 | -120.72 | sell / filled / 직전 완료 봉 목표 비중 0%; 다음 봉 시가 가정 |
| v2 | trend_8_26 + volume_26 | 10008.84 | 8.84 | sell / filled / 직전 완료 봉 목표 비중 50%; 다음 봉 시가 가정 |
| v2 | momentum_26 AND breakout_8 | 9417.88 | -582.12 | buy / partial / 직전 완료 봉 목표 비중 100%; 다음 봉 시가 가정 |
| v2 | momentum_26 + breakout_8 | 9810.51 | -189.49 | buy / partial / 직전 완료 봉 목표 비중 100%; 다음 봉 시가 가정 |
| v2 | momentum_26 AND reversion_12 | 9800.13 | -199.87 | sell / filled / 직전 완료 봉 목표 비중 0%; 다음 봉 시가 가정 |
| v2 | momentum_26 + reversion_12 | 10040.67 | 40.67 | sell / filled / 직전 완료 봉 목표 비중 50%; 다음 봉 시가 가정 |
| v2 | momentum_26 AND volume_26 | 9941.52 | -58.48 | sell / filled / 직전 완료 봉 목표 비중 0%; 다음 봉 시가 가정 |
| v2 | momentum_26 + volume_26 | 10051.14 | 51.14 | sell / filled / 직전 완료 봉 목표 비중 50%; 다음 봉 시가 가정 |
| v2 | breakout_8 AND reversion_12 | 10000.00 | 0.00 | 대기 /  / 새 신호 대기 |
| v2 | breakout_8 + reversion_12 | 9589.47 | -410.53 | sell / filled / 직전 완료 봉 목표 비중 50%; 다음 봉 시가 가정 |
| v2 | breakout_8 AND volume_26 | 9918.86 | -81.14 | sell / filled / 직전 완료 봉 목표 비중 0%; 다음 봉 시가 가정 |
| v2 | breakout_8 + volume_26 | 9599.64 | -400.36 | sell / filled / 직전 완료 봉 목표 비중 50%; 다음 봉 시가 가정 |
| v2 | reversion_12 AND volume_26 | 9949.87 | -50.13 | sell / filled / 직전 완료 봉 목표 비중 0%; 다음 봉 시가 가정 |
| v2 | reversion_12 + volume_26 | 9825.48 | -174.52 | sell / filled / 직전 완료 봉 목표 비중 0%; 다음 봉 시가 가정 |
| v2 | ema_12_26 | 10127.46 | 127.46 | buy / partial / EMA12 > EMA26; 조건 충족; EMA12=175.145, EMA26=175.141; 직전 완료 봉 목표를 다음 봉 시가에 모의 적용 |
| v2 | macd_12_26_9 | 10127.46 | 127.46 | buy / partial / MACD > 신호선 그리고 MACD > 0; 조건 충족; MACD=0.00418876, signal9=-0.17046; 직전 완료 봉 목표를 다음 봉 시가에 모의 적용 |
| v2 | rsi_14_recovery | 10000.00 | 0.00 | 대기 /  / 새 신호 대기 |
| v2 | bollinger_20_reentry | 9911.54 | -88.46 | sell / filled / 직전 종가 < 직전 하단밴드, 현재 하단밴드 <= 종가 <= SMA20 (한 봉 목표); 조건 미충족; close=175.71, lower20=173.907, SMA20=174.743, previous_lower20=173.977; 직전 완료 봉 목표를 다음 봉 시가에 모의 적용 |
| v2 | donchian_20 | 9948.45 | -51.55 | sell / filled / 종가 > 현재 봉을 제외한 직전 20봉 최고가; 조건 미충족; close=175.56, prior_high20=177.365; 직전 완료 봉 목표를 다음 봉 시가에 모의 적용 |
| v2 | atr_14_breakout | 9859.04 | -140.96 | sell / filled / 종가 > 직전 종가 + 직전 ATR14 그리고 종가 > EMA26; 조건 미충족; close=177.19, threshold=177.748, prior_ATR14=0.663113, EMA26=175.734; 직전 완료 봉 목표를 다음 봉 시가에 모의 적용 |
| v2 | session_vwap | 10026.15 | 26.15 | buy / partial / 종가 > 뉴욕 거래일별 누적 전형가격 VWAP; 조건 충족; close=176.25, session_VWAP=175.945, session_volume=7.74672e+06; 직전 완료 봉 목표를 다음 봉 시가에 모의 적용 |
| v2 | obv_20 | 9968.37 | -31.63 | sell / filled / OBV > OBV의 SMA20 그리고 종가 > EMA26; 조건 미충족; OBV=1.88162e+07, OBV_SMA20=2.13258e+07, close=175.84, EMA26=175.361; 직전 완료 봉 목표를 다음 봉 시가에 모의 적용 |
| v2 | stochastic_14_3_recovery | 10000.00 | 0.00 | 대기 /  / 새 신호 대기 |
| v2 | mfi_14_recovery | 10000.00 | 0.00 | 대기 /  / 새 신호 대기 |
| v2 | adx_14_trend | 10106.07 | 106.07 | buy / partial / Wilder ADX14 >= 25 그리고 +DI14 > -DI14; 조건 충족; ADX14=25.0494, plus_DI14=28.5472, minus_DI14=15.0232; 직전 완료 봉 목표를 다음 봉 시가에 모의 적용 |
| v2 | aroon_25_trend | 10000.00 | 0.00 | 대기 /  / 새 신호 대기 |
| v2 | cci_20_momentum | 9956.92 | -43.08 | buy / partial / CCI20 > 100 (전형가격·평균절대편차); 조건 충족; CCI20=102.776; 직전 완료 봉 목표를 다음 봉 시가에 모의 적용 |
| v2 | williams_14_recovery | 9911.54 | -88.46 | sell / filled / 직전 Williams %R14 < -80, 현재 >= -80 (한 봉 목표); 조건 미충족; Williams_R14=-43.9575, previous_R14=-33.1215; 직전 완료 봉 목표를 다음 봉 시가에 모의 적용 |
| v2 | cmf_20_accumulation | 10000.00 | 0.00 | 대기 /  / 새 신호 대기 |
| v2 | chaikin_3_10 | 10000.00 | 0.00 | 대기 /  / 새 신호 대기 |
| v2 | roc_10_momentum | 10000.81 | 0.81 | buy / partial / 10봉 ROC > 1% 그리고 종가 > EMA26; 조건 충족; ROC10_percent=1.10566, close=177.4, EMA26=175.858; 직전 완료 봉 목표를 다음 봉 시가에 모의 적용 |
| v2 | trix_15_trend | 10080.36 | 80.36 | buy / partial / 15봉 삼중 EMA의 1봉 변화율 TRIX > 0 그리고 종가 > EMA26; 조건 충족; TRIX15_percent=0.00176833, close=176.25, EMA26=175.427; 직전 완료 봉 목표를 다음 봉 시가에 모의 적용 |
| v2 | keltner_20_breakout | 10033.69 | 33.69 | buy / partial / 종가 > EMA20 + 2 x Wilder ATR14; 조건 충족; close=177.085, upper_Keltner=177.035, EMA20=175.709, ATR14=0.663113; 직전 완료 봉 목표를 다음 봉 시가에 모의 적용 |
| v2 | opening_range_30m | 10018.98 | 18.98 | buy / partial / 뉴욕 09:30·09:45 두 완료 봉 최고가를 10:00 이후 종가가 돌파; 조건 충족; close=177.4, opening_high=177.365; 직전 완료 봉 목표를 다음 봉 시가에 모의 적용 |

### 같은 기간의 비용·노출 비교 (사후 연구)

| 전략 | 비용 전 | 비용 후 | 100% 보유 | 같은 평균 노출 보유 | 평균 노출 |
|---|---:|---:|---:|---:|---:|
| cash | 0.00% | 0.00% | 10.43% | 0.00% | 0.00% |
| buy_hold | 10.90% | 10.43% | 10.43% | 10.43% | 100.00% |
| trend_8_26 | 2.53% | -2.10% | 10.43% | 6.78% | 65.88% |
| momentum_26 | 1.40% | -5.98% | 10.43% | 7.39% | 71.65% |
| breakout_8 | -2.48% | -20.28% | 10.43% | 2.44% | 24.15% |
| reversion_12 | 7.01% | -3.65% | 10.43% | 2.09% | 20.73% |
| volume_26 | 4.19% | -3.80% | 10.43% | 0.53% | 5.25% |
| trend_8_26 AND momentum_26 | 1.06% | -3.91% | 10.43% | 6.22% | 60.63% |
| trend_8_26 + momentum_26 | 1.97% | -3.85% | 10.43% | 7.08% | 68.77% |
| trend_8_26 AND breakout_8 | -0.38% | -14.72% | 10.43% | 1.96% | 19.42% |
| trend_8_26 + breakout_8 | 0.02% | -11.27% | 10.43% | 4.59% | 45.02% |
| trend_8_26 AND reversion_12 | 1.89% | -3.93% | 10.43% | 0.82% | 8.14% |
| trend_8_26 + reversion_12 | 4.78% | -2.67% | 10.43% | 4.41% | 43.31% |
| trend_8_26 AND volume_26 | 2.80% | -1.84% | 10.43% | 0.29% | 2.89% |
| trend_8_26 + volume_26 | 3.38% | -2.55% | 10.43% | 3.61% | 35.57% |
| momentum_26 AND breakout_8 | -2.59% | -19.03% | 10.43% | 2.25% | 22.31% |
| momentum_26 + breakout_8 | -0.53% | -13.41% | 10.43% | 4.89% | 47.91% |
| momentum_26 AND reversion_12 | 2.27% | -4.38% | 10.43% | 0.90% | 8.92% |
| momentum_26 + reversion_12 | 4.20% | -3.41% | 10.43% | 4.71% | 46.20% |
| momentum_26 AND volume_26 | 2.58% | -1.64% | 10.43% | 0.26% | 2.62% |
| momentum_26 + volume_26 | 2.81% | -3.49% | 10.43% | 3.91% | 38.46% |
| breakout_8 AND reversion_12 | 0.00% | 0.00% | 10.43% | 0.00% | 0.00% |
| breakout_8 + reversion_12 | 2.18% | -12.18% | 10.43% | 2.27% | 22.45% |
| breakout_8 AND volume_26 | 0.51% | -1.17% | 10.43% | 0.11% | 1.05% |
| breakout_8 + volume_26 | 0.81% | -11.32% | 10.43% | 1.48% | 14.71% |
| reversion_12 AND volume_26 | 1.52% | -1.00% | 10.43% | 0.16% | 1.57% |
| reversion_12 + volume_26 | 5.61% | -2.91% | 10.43% | 1.31% | 13.00% |
| ema_12_26 | 1.01% | -2.32% | 10.43% | 7.78% | 75.33% |
| macd_12_26_9 | -0.10% | -5.80% | 10.43% | 4.20% | 41.21% |
| rsi_14_recovery | -0.15% | -0.57% | 10.43% | 0.03% | 0.26% |
| bollinger_20_reentry | -0.87% | -3.75% | 10.43% | 0.18% | 1.84% |
| donchian_20 | -1.09% | -9.82% | 10.43% | 0.90% | 8.92% |
| atr_14_breakout | -1.27% | -10.74% | 10.43% | 0.66% | 6.56% |
| session_vwap | 0.22% | -11.65% | 10.43% | 6.78% | 65.88% |
| obv_20 | 2.12% | -5.32% | 10.43% | 4.33% | 42.52% |
| stochastic_14_3_recovery | 1.55% | -6.63% | 10.43% | 0.53% | 5.25% |
| mfi_14_recovery | -0.31% | -1.97% | 10.43% | 0.11% | 1.05% |
| adx_14_trend | 2.12% | -0.84% | 10.43% | 4.41% | 43.31% |
| aroon_25_trend | -1.78% | -7.78% | 10.43% | 3.09% | 30.45% |
| cci_20_momentum | 3.70% | -4.25% | 10.43% | 2.82% | 27.82% |
| williams_14_recovery | 0.08% | -5.24% | 10.43% | 0.34% | 3.41% |
| cmf_20_accumulation | 2.13% | -6.10% | 10.43% | 5.15% | 50.39% |
| chaikin_3_10 | -1.00% | -9.36% | 10.43% | 5.65% | 55.12% |
| roc_10_momentum | 0.45% | -5.69% | 10.43% | 1.45% | 14.44% |
| trix_15_trend | -1.64% | -8.80% | 10.43% | 6.47% | 62.99% |
| keltner_20_breakout | -0.31% | -7.18% | 10.43% | 1.61% | 16.01% |
| opening_range_30m | 0.04% | -9.55% | 10.43% | 3.68% | 36.22% |

동일 구간·초기 자금, 종료 시 청산 비용 포함. 노출 맞춤은 사후 설명용이며 v2 실제 계좌 성과가 아닙니다.
[낙폭 분해·비용 영향·전체 구간](XOM/comparison.json)

[v1 전체 기록](XOM/accounts.json) · [v2 전체 기록](XOM/accounts-v2.json)

## JNJ 계좌

| 모델 | 전략 | 평가액 USD | 손익 USD | 최근 매매·이유 |
|---|---|---:|---:|---|
| v1 | cash | 10000.00 | 0.00 | 대기 /  / 새 신호 대기 |
| v1 | buy_hold | 9963.43 | -36.57 | buy /  / buy_hold: prior completed bar target 100%; next bar open simulation |
| v1 | trend_8_26 | 9917.63 | -82.37 | buy /  / trend_8_26: prior completed bar target 100%; next bar open simulation |
| v1 | momentum_26 | 10000.00 | 0.00 | 대기 /  / 새 신호 대기 |
| v1 | breakout_8 | 9822.10 | -177.90 | sell /  / breakout_8: prior completed bar target 0%; next bar open simulation |
| v1 | reversion_12 | 9992.01 | -7.99 | sell /  / reversion_12: prior completed bar target 0%; next bar open simulation |
| v1 | volume_26 | 9935.63 | -64.37 | sell /  / volume_26: prior completed bar target 0%; next bar open simulation |
| v1 | trend_8_26 AND momentum_26 | 10000.00 | 0.00 | 대기 /  / 새 신호 대기 |
| v1 | trend_8_26 + momentum_26 | 9958.68 | -41.32 | sell /  / trend_8_26 + momentum_26: prior completed bar target 50%; next bar open simulation |
| v1 | trend_8_26 AND breakout_8 | 9937.40 | -62.60 | sell /  / trend_8_26 AND breakout_8: prior completed bar target 0%; next bar open simulation |
| v1 | trend_8_26 + breakout_8 | 9869.71 | -130.29 | sell /  / trend_8_26 + breakout_8: prior completed bar target 50%; next bar open simulation |
| v1 | trend_8_26 AND reversion_12 | 9992.01 | -7.99 | sell /  / trend_8_26 AND reversion_12: prior completed bar target 0%; next bar open simulation |
| v1 | trend_8_26 + reversion_12 | 9954.73 | -45.27 | sell /  / trend_8_26 + reversion_12: prior completed bar target 50%; next bar open simulation |
| v1 | trend_8_26 AND volume_26 | 9935.63 | -64.37 | sell /  / trend_8_26 AND volume_26: prior completed bar target 0%; next bar open simulation |
| v1 | trend_8_26 + volume_26 | 9926.62 | -73.38 | sell /  / trend_8_26 + volume_26: prior completed bar target 50%; next bar open simulation |
| v1 | momentum_26 AND breakout_8 | 10000.00 | 0.00 | 대기 /  / 새 신호 대기 |
| v1 | momentum_26 + breakout_8 | 9910.61 | -89.39 | sell /  / momentum_26 + breakout_8: prior completed bar target 0%; next bar open simulation |
| v1 | momentum_26 AND reversion_12 | 10000.00 | 0.00 | 대기 /  / 새 신호 대기 |
| v1 | momentum_26 + reversion_12 | 9995.98 | -4.02 | sell /  / momentum_26 + reversion_12: prior completed bar target 0%; next bar open simulation |
| v1 | momentum_26 AND volume_26 | 10000.00 | 0.00 | 대기 /  / 새 신호 대기 |
| v1 | momentum_26 + volume_26 | 9967.75 | -32.25 | sell /  / momentum_26 + volume_26: prior completed bar target 0%; next bar open simulation |
| v1 | breakout_8 AND reversion_12 | 10000.00 | 0.00 | 대기 /  / 새 신호 대기 |
| v1 | breakout_8 + reversion_12 | 9906.63 | -93.37 | sell /  / breakout_8 + reversion_12: prior completed bar target 0%; next bar open simulation |
| v1 | breakout_8 AND volume_26 | 10000.00 | 0.00 | 대기 /  / 새 신호 대기 |
| v1 | breakout_8 + volume_26 | 9878.65 | -121.35 | sell /  / breakout_8 + volume_26: prior completed bar target 0%; next bar open simulation |
| v1 | reversion_12 AND volume_26 | 10000.00 | 0.00 | 대기 /  / 새 신호 대기 |
| v1 | reversion_12 + volume_26 | 9963.74 | -36.26 | sell /  / reversion_12 + volume_26: prior completed bar target 0%; next bar open simulation |
| v1 | ema_12_26 | 9888.89 | -111.11 | sell /  / EMA12 > EMA26; 조건 미충족; EMA12=255.389, EMA26=255.395 |
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
| v1 | aroon_25_trend | 9981.79 | -18.21 | buy /  / Aroon25 Up > 70 그리고 Down < 30 (동률이면 최신 극값); 조건 충족; Aroon_up=80, Aroon_down=28 |
| v1 | cci_20_momentum | 9935.63 | -64.37 | sell /  / CCI20 > 100 (전형가격·평균절대편차); 조건 미충족; CCI20=62.9489 |
| v1 | williams_14_recovery | 9927.65 | -72.35 | sell /  / 직전 Williams %R14 < -80, 현재 >= -80 (한 봉 목표); 조건 미충족; Williams_R14=-39.8495, previous_R14=-25.2395 |
| v1 | cmf_20_accumulation | 10000.00 | 0.00 | 대기 /  / 새 신호 대기 |
| v1 | chaikin_3_10 | 10000.00 | 0.00 | 대기 /  / 새 신호 대기 |
| v1 | roc_10_momentum | 9816.66 | -183.34 | sell /  / 10봉 ROC > 1% 그리고 종가 > EMA26; 조건 미충족; ROC10_percent=-0.398319, close=255.08, EMA26=255.591 |
| v1 | trix_15_trend | 9889.12 | -110.88 | sell /  / 15봉 삼중 EMA의 1봉 변화율 TRIX > 0 그리고 종가 > EMA26; 조건 미충족; TRIX15_percent=0.00718077, close=255.08, EMA26=255.591 |
| v1 | keltner_20_breakout | 10000.00 | 0.00 | 대기 /  / 새 신호 대기 |
| v1 | opening_range_30m | 10000.00 | 0.00 | 대기 /  / 새 신호 대기 |
| v2 | cash | 10000.00 | 0.00 | 대기 /  / 새 신호 대기 |
| v2 | buy_hold | 9730.89 | -269.11 | 중단: 손실 한도 / buy / partial / 직전 완료 봉 목표 비중 100%; 다음 봉 시가 가정 |
| v2 | trend_8_26 | 9730.89 | -269.11 | 중단: 손실 한도 / buy / partial / 직전 완료 봉 목표 비중 100%; 다음 봉 시가 가정 |
| v2 | momentum_26 | 9730.89 | -269.11 | 중단: 손실 한도 / buy / partial / 직전 완료 봉 목표 비중 100%; 다음 봉 시가 가정 |
| v2 | breakout_8 | 9343.39 | -656.61 | 중단: 손실 한도 / sell / filled / 직전 완료 봉 목표 비중 0%; 다음 봉 시가 가정 |
| v2 | reversion_12 | 9680.46 | -319.54 | sell / filled / 직전 완료 봉 목표 비중 0%; 다음 봉 시가 가정 |
| v2 | volume_26 | 9726.38 | -273.62 | sell / filled / 직전 완료 봉 목표 비중 0%; 다음 봉 시가 가정 |
| v2 | trend_8_26 AND momentum_26 | 9730.89 | -269.11 | 중단: 손실 한도 / buy / partial / 직전 완료 봉 목표 비중 100%; 다음 봉 시가 가정 |
| v2 | trend_8_26 + momentum_26 | 9730.89 | -269.11 | 중단: 손실 한도 / buy / partial / 직전 완료 봉 목표 비중 100%; 다음 봉 시가 가정 |
| v2 | trend_8_26 AND breakout_8 | 9419.39 | -580.61 | 중단: 손실 한도 / sell / filled / 직전 완료 봉 목표 비중 0%; 다음 봉 시가 가정 |
| v2 | trend_8_26 + breakout_8 | 9441.82 | -558.18 | sell / filled / 직전 완료 봉 목표 비중 50%; 다음 봉 시가 가정 |
| v2 | trend_8_26 AND reversion_12 | 9968.12 | -31.88 | sell / filled / 직전 완료 봉 목표 비중 0%; 다음 봉 시가 가정 |
| v2 | trend_8_26 + reversion_12 | 9732.92 | -267.08 | 중단: 손실 한도 / sell / filled / 직전 완료 봉 목표 비중 0%; 다음 봉 시가 가정 |
| v2 | trend_8_26 AND volume_26 | 9805.21 | -194.79 | sell / filled / 직전 완료 봉 목표 비중 0%; 다음 봉 시가 가정 |
| v2 | trend_8_26 + volume_26 | 9838.60 | -161.40 | 중단: 손실 한도 / buy / filled / 직전 완료 봉 목표 비중 50%; 다음 봉 시가 가정 |
| v2 | momentum_26 AND breakout_8 | 9598.70 | -401.30 | sell / filled / 직전 완료 봉 목표 비중 0%; 다음 봉 시가 가정 |
| v2 | momentum_26 + breakout_8 | 9472.51 | -527.49 | sell / filled / 직전 완료 봉 목표 비중 0%; 다음 봉 시가 가정 |
| v2 | momentum_26 AND reversion_12 | 9938.87 | -61.13 | sell / filled / 직전 완료 봉 목표 비중 0%; 다음 봉 시가 가정 |
| v2 | momentum_26 + reversion_12 | 9732.92 | -267.08 | 중단: 손실 한도 / sell / filled / 직전 완료 봉 목표 비중 0%; 다음 봉 시가 가정 |
| v2 | momentum_26 AND volume_26 | 9920.93 | -79.07 | sell / filled / 직전 완료 봉 목표 비중 0%; 다음 봉 시가 가정 |
| v2 | momentum_26 + volume_26 | 9838.60 | -161.40 | 중단: 손실 한도 / buy / filled / 직전 완료 봉 목표 비중 50%; 다음 봉 시가 가정 |
| v2 | breakout_8 AND reversion_12 | 10000.00 | 0.00 | 대기 /  / 새 신호 대기 |
| v2 | breakout_8 + reversion_12 | 9487.81 | -512.19 | sell / filled / 직전 완료 봉 목표 비중 0%; 다음 봉 시가 가정 |
| v2 | breakout_8 AND volume_26 | 9814.17 | -185.83 | sell / filled / 직전 완료 봉 목표 비중 0%; 다음 봉 시가 가정 |
| v2 | breakout_8 + volume_26 | 9490.26 | -509.74 | sell / filled / 직전 완료 봉 목표 비중 0%; 다음 봉 시가 가정 |
| v2 | reversion_12 AND volume_26 | 9886.24 | -113.76 | sell / filled / 직전 완료 봉 목표 비중 0%; 다음 봉 시가 가정 |
| v2 | reversion_12 + volume_26 | 9724.01 | -275.99 | sell / filled / 직전 완료 봉 목표 비중 0%; 다음 봉 시가 가정 |
| v2 | ema_12_26 | 9886.91 | -113.09 | sell / filled / EMA12 > EMA26; 조건 미충족; EMA12=255.389, EMA26=255.395; 직전 완료 봉 목표를 다음 봉 시가에 모의 적용 |
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
| v2 | aroon_25_trend | 9980.79 | -19.21 | buy / partial / Aroon25 Up > 70 그리고 Down < 30 (동률이면 최신 극값); 조건 충족; Aroon_up=80, Aroon_down=28; 직전 완료 봉 목표를 다음 봉 시가에 모의 적용 |
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
| cash | 0.00% | 0.00% | -6.29% | -0.00% | 0.00% |
| buy_hold | -5.90% | -6.29% | -6.29% | -6.29% | 100.00% |
| trend_8_26 | 1.68% | -0.85% | -6.29% | -3.20% | 49.61% |
| momentum_26 | 0.96% | -2.38% | -6.29% | -3.06% | 47.51% |
| breakout_8 | -0.91% | -17.98% | -6.29% | -1.35% | 20.73% |
| reversion_12 | -7.49% | -16.01% | -6.29% | -1.98% | 30.45% |
| volume_26 | -0.78% | -7.23% | -6.29% | -0.43% | 6.56% |
| trend_8_26 AND momentum_26 | 2.35% | -0.62% | -6.29% | -2.82% | 43.57% |
| trend_8_26 + momentum_26 | 1.33% | -1.61% | -6.29% | -3.13% | 48.56% |
| trend_8_26 AND breakout_8 | 0.55% | -12.09% | -6.29% | -1.01% | 15.49% |
| trend_8_26 + breakout_8 | 0.40% | -9.80% | -6.29% | -2.28% | 35.18% |
| trend_8_26 AND reversion_12 | 1.02% | -2.73% | -6.29% | -0.41% | 6.30% |
| trend_8_26 + reversion_12 | -2.98% | -8.35% | -6.29% | -2.59% | 40.03% |
| trend_8_26 AND volume_26 | 1.34% | -1.19% | -6.29% | -0.12% | 1.84% |
| trend_8_26 + volume_26 | 0.48% | -3.88% | -6.29% | -1.83% | 28.09% |
| momentum_26 AND breakout_8 | 2.20% | -9.52% | -6.29% | -0.95% | 14.44% |
| momentum_26 + breakout_8 | 0.05% | -10.31% | -6.29% | -2.22% | 34.13% |
| momentum_26 AND reversion_12 | -0.60% | -3.89% | -6.29% | -0.45% | 6.82% |
| momentum_26 + reversion_12 | -3.32% | -8.87% | -6.29% | -2.52% | 38.98% |
| momentum_26 AND volume_26 | 1.57% | -0.12% | -6.29% | -0.09% | 1.31% |
| momentum_26 + volume_26 | 0.12% | -4.22% | -6.29% | -1.76% | 27.04% |
| breakout_8 AND reversion_12 | 0.00% | 0.00% | -6.29% | -0.00% | 0.00% |
| breakout_8 + reversion_12 | -4.24% | -16.48% | -6.29% | -1.67% | 25.60% |
| breakout_8 AND volume_26 | 0.00% | -1.66% | -6.29% | -0.09% | 1.31% |
| breakout_8 + volume_26 | -0.84% | -12.04% | -6.29% | -0.90% | 13.66% |
| reversion_12 AND volume_26 | -1.99% | -4.42% | -6.29% | -0.17% | 2.62% |
| reversion_12 + volume_26 | -4.18% | -10.98% | -6.29% | -1.21% | 18.51% |
| ema_12_26 | -0.87% | -2.93% | -6.29% | -2.90% | 44.88% |
| macd_12_26_9 | 5.17% | 2.55% | -6.29% | -1.90% | 29.13% |
| rsi_14_recovery | -1.69% | -6.92% | -6.29% | -0.22% | 3.41% |
| bollinger_20_reentry | -0.55% | -4.64% | -6.29% | -0.17% | 2.62% |
| donchian_20 | 1.17% | -6.59% | -6.29% | -0.48% | 7.35% |
| atr_14_breakout | 1.31% | -4.88% | -6.29% | -0.31% | 4.72% |
| session_vwap | 1.29% | -6.48% | -6.29% | -3.11% | 48.29% |
| obv_20 | -6.18% | -14.10% | -6.29% | -2.18% | 33.60% |
| stochastic_14_3_recovery | -1.40% | -13.80% | -6.29% | -0.55% | 8.40% |
| mfi_14_recovery | 0.33% | -0.93% | -6.29% | -0.05% | 0.79% |
| adx_14_trend | -2.56% | -7.35% | -6.29% | -2.03% | 31.23% |
| aroon_25_trend | 3.88% | -0.81% | -6.29% | -1.85% | 28.35% |
| cci_20_momentum | 0.94% | -6.01% | -6.29% | -1.56% | 23.88% |
| williams_14_recovery | -2.03% | -10.30% | -6.29% | -0.36% | 5.51% |
| cmf_20_accumulation | 2.08% | -2.12% | -6.29% | -1.90% | 29.13% |
| chaikin_3_10 | -3.59% | -7.94% | -6.29% | -2.25% | 34.65% |
| roc_10_momentum | -2.21% | -8.56% | -6.29% | -0.98% | 14.96% |
| trix_15_trend | -1.60% | -4.46% | -6.29% | -2.20% | 33.86% |
| keltner_20_breakout | 0.76% | -2.97% | -6.29% | -0.62% | 9.45% |
| opening_range_30m | 0.41% | -3.72% | -6.29% | -1.71% | 26.25% |

동일 구간·초기 자금, 종료 시 청산 비용 포함. 노출 맞춤은 사후 설명용이며 v2 실제 계좌 성과가 아닙니다.
[낙폭 분해·비용 영향·전체 구간](JNJ/comparison.json)

[v1 전체 기록](JNJ/accounts.json) · [v2 전체 기록](JNJ/accounts-v2.json)

## CAT 계좌

| 모델 | 전략 | 평가액 USD | 손익 USD | 최근 매매·이유 |
|---|---|---:|---:|---|
| v1 | cash | 10000.00 | 0.00 | 대기 /  / 새 신호 대기 |
| v1 | buy_hold | 9992.67 | -7.33 | buy /  / buy_hold: prior completed bar target 100%; next bar open simulation |
| v1 | trend_8_26 | 9992.67 | -7.33 | buy /  / trend_8_26: prior completed bar target 100%; next bar open simulation |
| v1 | momentum_26 | 9912.42 | -87.58 | buy /  / momentum_26: prior completed bar target 100%; next bar open simulation |
| v1 | breakout_8 | 9950.83 | -49.17 | sell /  / breakout_8: prior completed bar target 0%; next bar open simulation |
| v1 | reversion_12 | 9942.33 | -57.67 | buy /  / reversion_12: prior completed bar target 100%; next bar open simulation |
| v1 | volume_26 | 10000.00 | 0.00 | 대기 /  / 새 신호 대기 |
| v1 | trend_8_26 AND momentum_26 | 9912.42 | -87.58 | buy /  / trend_8_26 AND momentum_26: prior completed bar target 100%; next bar open simulation |
| v1 | trend_8_26 + momentum_26 | 9952.63 | -47.37 | buy /  / trend_8_26 + momentum_26: prior completed bar target 100%; next bar open simulation |
| v1 | trend_8_26 AND breakout_8 | 9950.83 | -49.17 | sell /  / trend_8_26 AND breakout_8: prior completed bar target 0%; next bar open simulation |
| v1 | trend_8_26 + breakout_8 | 9971.88 | -28.12 | buy /  / trend_8_26 + breakout_8: prior completed bar target 50%; next bar open simulation |
| v1 | trend_8_26 AND reversion_12 | 9942.33 | -57.67 | buy /  / trend_8_26 AND reversion_12: prior completed bar target 100%; next bar open simulation |
| v1 | trend_8_26 + reversion_12 | 9967.53 | -32.47 | buy /  / trend_8_26 + reversion_12: prior completed bar target 100%; next bar open simulation |
| v1 | trend_8_26 AND volume_26 | 10000.00 | 0.00 | 대기 /  / 새 신호 대기 |
| v1 | trend_8_26 + volume_26 | 9996.38 | -3.62 | buy /  / trend_8_26 + volume_26: prior completed bar target 50%; next bar open simulation |
| v1 | momentum_26 AND breakout_8 | 9950.83 | -49.17 | sell /  / momentum_26 AND breakout_8: prior completed bar target 0%; next bar open simulation |
| v1 | momentum_26 + breakout_8 | 9931.60 | -68.40 | buy /  / momentum_26 + breakout_8: prior completed bar target 50%; next bar open simulation |
| v1 | momentum_26 AND reversion_12 | 9942.33 | -57.67 | buy /  / momentum_26 AND reversion_12: prior completed bar target 100%; next bar open simulation |
| v1 | momentum_26 + reversion_12 | 9927.35 | -72.65 | buy /  / momentum_26 + reversion_12: prior completed bar target 100%; next bar open simulation |
| v1 | momentum_26 AND volume_26 | 10000.00 | 0.00 | 대기 /  / 새 신호 대기 |
| v1 | momentum_26 + volume_26 | 9956.08 | -43.92 | buy /  / momentum_26 + volume_26: prior completed bar target 50%; next bar open simulation |
| v1 | breakout_8 AND reversion_12 | 10000.00 | 0.00 | 대기 /  / 새 신호 대기 |
| v1 | breakout_8 + reversion_12 | 9946.53 | -53.47 | buy /  / breakout_8 + reversion_12: prior completed bar target 50%; next bar open simulation |
| v1 | breakout_8 AND volume_26 | 10000.00 | 0.00 | 대기 /  / 새 신호 대기 |
| v1 | breakout_8 + volume_26 | 9975.37 | -24.63 | sell /  / breakout_8 + volume_26: prior completed bar target 0%; next bar open simulation |
| v1 | reversion_12 AND volume_26 | 10000.00 | 0.00 | 대기 /  / 새 신호 대기 |
| v1 | reversion_12 + volume_26 | 9971.09 | -28.91 | buy /  / reversion_12 + volume_26: prior completed bar target 50%; next bar open simulation |
| v1 | ema_12_26 | 9912.42 | -87.58 | buy /  / EMA12 > EMA26; 조건 충족; EMA12=733.716, EMA26=733.7 |
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
| v1 | chaikin_3_10 | 9758.62 | -241.38 | sell /  / ADL의 EMA3 - EMA10 > 0 그리고 종가 > EMA26; 조건 미충족; Chaikin3_10=12269.7, ADL=-5.59334e+06, close=735.29, EMA26=735.965 |
| v1 | roc_10_momentum | 9963.13 | -36.87 | sell /  / 10봉 ROC > 1% 그리고 종가 > EMA26; 조건 미충족; ROC10_percent=-0.134597, close=734.53, EMA26=735.486 |
| v1 | trix_15_trend | 9768.45 | -231.55 | sell /  / 15봉 삼중 EMA의 1봉 변화율 TRIX > 0 그리고 종가 > EMA26; 조건 미충족; TRIX15_percent=0.0210282, close=735.29, EMA26=735.965 |
| v1 | keltner_20_breakout | 10000.00 | 0.00 | 대기 /  / 새 신호 대기 |
| v1 | opening_range_30m | 10040.71 | 40.71 | sell /  / 뉴욕 09:30·09:45 두 완료 봉 최고가를 10:00 이후 종가가 돌파; 자료 부족·변동폭 또는 거래량 없음: 대기; close=740.21 |
| v2 | cash | 10000.00 | 0.00 | 대기 /  / 새 신호 대기 |
| v2 | buy_hold | 9190.01 | -809.99 | 중단: 손실 한도 / buy / partial / 직전 완료 봉 목표 비중 100%; 다음 봉 시가 가정 |
| v2 | trend_8_26 | 9916.45 | -83.55 | buy / partial / 직전 완료 봉 목표 비중 100%; 다음 봉 시가 가정 |
| v2 | momentum_26 | 9925.89 | -74.11 | buy / partial / 직전 완료 봉 목표 비중 100%; 다음 봉 시가 가정 |
| v2 | breakout_8 | 9772.76 | -227.24 | sell / filled / 직전 완료 봉 목표 비중 0%; 다음 봉 시가 가정 |
| v2 | reversion_12 | 9061.66 | -938.34 | 중단: 손실 한도 / buy / partial / 직전 완료 봉 목표 비중 100%; 다음 봉 시가 가정 |
| v2 | volume_26 | 9320.82 | -679.18 | 중단: 손실 한도 / buy / partial / 직전 완료 봉 목표 비중 100%; 다음 봉 시가 가정 |
| v2 | trend_8_26 AND momentum_26 | 9954.63 | -45.37 | buy / partial / 직전 완료 봉 목표 비중 100%; 다음 봉 시가 가정 |
| v2 | trend_8_26 + momentum_26 | 9921.34 | -78.66 | buy / partial / 직전 완료 봉 목표 비중 100%; 다음 봉 시가 가정 |
| v2 | trend_8_26 AND breakout_8 | 9866.70 | -133.30 | sell / filled / 직전 완료 봉 목표 비중 0%; 다음 봉 시가 가정 |
| v2 | trend_8_26 + breakout_8 | 9844.77 | -155.23 | buy / filled / 직전 완료 봉 목표 비중 50%; 다음 봉 시가 가정 |
| v2 | trend_8_26 AND reversion_12 | 9753.60 | -246.40 | buy / partial / 직전 완료 봉 목표 비중 100%; 다음 봉 시가 가정 |
| v2 | trend_8_26 + reversion_12 | 9591.07 | -408.93 | buy / partial / 직전 완료 봉 목표 비중 100%; 다음 봉 시가 가정 |
| v2 | trend_8_26 AND volume_26 | 10035.44 | 35.44 | sell / filled / 직전 완료 봉 목표 비중 0%; 다음 봉 시가 가정 |
| v2 | trend_8_26 + volume_26 | 9629.07 | -370.93 | buy / filled / 직전 완료 봉 목표 비중 50%; 다음 봉 시가 가정 |
| v2 | momentum_26 AND breakout_8 | 9926.39 | -73.61 | sell / filled / 직전 완료 봉 목표 비중 0%; 다음 봉 시가 가정 |
| v2 | momentum_26 + breakout_8 | 9849.21 | -150.79 | buy / filled / 직전 완료 봉 목표 비중 50%; 다음 봉 시가 가정 |
| v2 | momentum_26 AND reversion_12 | 9812.88 | -187.12 | buy / partial / 직전 완료 봉 목표 비중 100%; 다음 봉 시가 가정 |
| v2 | momentum_26 + reversion_12 | 9595.55 | -404.45 | buy / partial / 직전 완료 봉 목표 비중 100%; 다음 봉 시가 가정 |
| v2 | momentum_26 AND volume_26 | 10048.78 | 48.78 | sell / filled / 직전 완료 봉 목표 비중 0%; 다음 봉 시가 가정 |
| v2 | momentum_26 + volume_26 | 9653.83 | -346.17 | buy / filled / 직전 완료 봉 목표 비중 50%; 다음 봉 시가 가정 |
| v2 | breakout_8 AND reversion_12 | 10000.00 | 0.00 | 대기 /  / 새 신호 대기 |
| v2 | breakout_8 + reversion_12 | 9610.18 | -389.82 | 중단: 손실 한도 / sell / filled / 직전 완료 봉 목표 비중 0%; 다음 봉 시가 가정 |
| v2 | breakout_8 AND volume_26 | 9998.69 | -1.31 | sell / filled / 직전 완료 봉 목표 비중 0%; 다음 봉 시가 가정 |
| v2 | breakout_8 + volume_26 | 9579.25 | -420.75 | sell / filled / 직전 완료 봉 목표 비중 0%; 다음 봉 시가 가정 |
| v2 | reversion_12 AND volume_26 | 9256.34 | -743.66 | 중단: 손실 한도 / buy / partial / 직전 완료 봉 목표 비중 100%; 다음 봉 시가 가정 |
| v2 | reversion_12 + volume_26 | 9393.59 | -606.41 | 중단: 손실 한도 / sell / filled / 직전 완료 봉 목표 비중 50%; 다음 봉 시가 가정 |
| v2 | ema_12_26 | 9911.43 | -88.57 | buy / partial / EMA12 > EMA26; 조건 충족; EMA12=733.716, EMA26=733.7; 직전 완료 봉 목표를 다음 봉 시가에 모의 적용 |
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
| v2 | chaikin_3_10 | 9752.77 | -247.23 | sell / filled / ADL의 EMA3 - EMA10 > 0 그리고 종가 > EMA26; 조건 미충족; Chaikin3_10=12269.7, ADL=-5.59334e+06, close=735.29, EMA26=735.965; 직전 완료 봉 목표를 다음 봉 시가에 모의 적용 |
| v2 | roc_10_momentum | 9961.14 | -38.86 | sell / filled / 10봉 ROC > 1% 그리고 종가 > EMA26; 조건 미충족; ROC10_percent=-0.134597, close=734.53, EMA26=735.486; 직전 완료 봉 목표를 다음 봉 시가에 모의 적용 |
| v2 | trix_15_trend | 9762.59 | -237.41 | sell / filled / 15봉 삼중 EMA의 1봉 변화율 TRIX > 0 그리고 종가 > EMA26; 조건 미충족; TRIX15_percent=0.0210282, close=735.29, EMA26=735.965; 직전 완료 봉 목표를 다음 봉 시가에 모의 적용 |
| v2 | keltner_20_breakout | 10000.00 | 0.00 | 대기 /  / 새 신호 대기 |
| v2 | opening_range_30m | 10038.70 | 38.70 | sell / filled / 뉴욕 09:30·09:45 두 완료 봉 최고가를 10:00 이후 종가가 돌파; 자료 부족·변동폭 또는 거래량 없음: 대기; close=740.21; 직전 완료 봉 목표를 다음 봉 시가에 모의 적용 |

### 같은 기간의 비용·노출 비교 (사후 연구)

| 전략 | 비용 전 | 비용 후 | 100% 보유 | 같은 평균 노출 보유 | 평균 노출 |
|---|---:|---:|---:|---:|---:|
| cash | 0.00% | 0.00% | -10.77% | -0.00% | 0.00% |
| buy_hold | -10.39% | -10.77% | -10.77% | -10.77% | 100.00% |
| trend_8_26 | -1.89% | -5.53% | -10.77% | -5.48% | 50.39% |
| momentum_26 | -4.77% | -10.58% | -10.77% | -5.31% | 48.82% |
| breakout_8 | -3.13% | -15.67% | -10.77% | -1.64% | 14.96% |
| reversion_12 | -3.49% | -15.98% | -10.77% | -2.90% | 26.51% |
| volume_26 | -2.95% | -10.02% | -10.77% | -0.89% | 8.14% |
| trend_8_26 AND momentum_26 | -2.09% | -6.90% | -10.77% | -4.69% | 43.04% |
| trend_8_26 + momentum_26 | -3.32% | -8.08% | -10.77% | -5.40% | 49.61% |
| trend_8_26 AND breakout_8 | -1.76% | -8.91% | -10.77% | -0.84% | 7.61% |
| trend_8_26 + breakout_8 | -2.48% | -10.53% | -10.77% | -3.57% | 32.68% |
| trend_8_26 AND reversion_12 | 1.20% | -6.17% | -10.77% | -0.86% | 7.87% |
| trend_8_26 + reversion_12 | -2.63% | -10.32% | -10.77% | -4.20% | 38.46% |
| trend_8_26 AND volume_26 | 2.22% | -0.75% | -10.77% | -0.29% | 2.62% |
| trend_8_26 + volume_26 | -2.37% | -7.58% | -10.77% | -3.20% | 29.27% |
| momentum_26 AND breakout_8 | -2.68% | -10.53% | -10.77% | -0.92% | 8.40% |
| momentum_26 + breakout_8 | -3.91% | -13.13% | -10.77% | -3.48% | 31.90% |
| momentum_26 AND reversion_12 | -2.63% | -9.72% | -10.77% | -0.72% | 6.56% |
| momentum_26 + reversion_12 | -4.08% | -12.39% | -10.77% | -4.11% | 37.67% |
| momentum_26 AND volume_26 | 1.58% | -0.53% | -10.77% | -0.17% | 1.57% |
| momentum_26 + volume_26 | -3.80% | -9.52% | -10.77% | -3.11% | 28.48% |
| breakout_8 AND reversion_12 | 0.00% | 0.00% | -10.77% | -0.00% | 0.00% |
| breakout_8 + reversion_12 | -3.26% | -14.92% | -10.77% | -2.27% | 20.74% |
| breakout_8 AND volume_26 | 0.37% | -0.47% | -10.77% | -0.06% | 0.52% |
| breakout_8 + volume_26 | -3.01% | -12.14% | -10.77% | -1.27% | 11.55% |
| reversion_12 AND volume_26 | -1.25% | -5.71% | -10.77% | -0.58% | 5.25% |
| reversion_12 + volume_26 | -3.18% | -12.30% | -10.77% | -1.90% | 17.33% |
| ema_12_26 | -1.34% | -3.39% | -10.77% | -5.46% | 50.13% |
| macd_12_26_9 | -0.77% | -4.85% | -10.77% | -3.38% | 30.97% |
| rsi_14_recovery | -0.96% | -6.22% | -10.77% | -0.37% | 3.41% |
| bollinger_20_reentry | 1.35% | -4.43% | -10.77% | -0.40% | 3.67% |
| donchian_20 | -2.30% | -7.11% | -10.77% | -0.58% | 5.25% |
| atr_14_breakout | -2.42% | -9.14% | -10.77% | -0.52% | 4.72% |
| session_vwap | -0.44% | -12.23% | -10.77% | -4.98% | 45.67% |
| obv_20 | -4.26% | -14.52% | -10.77% | -2.90% | 26.51% |
| stochastic_14_3_recovery | -3.21% | -13.22% | -10.77% | -0.75% | 6.82% |
| mfi_14_recovery | 0.45% | -1.63% | -10.77% | -0.14% | 1.31% |
| adx_14_trend | -3.13% | -5.93% | -10.77% | -1.04% | 9.45% |
| aroon_25_trend | -2.12% | -6.14% | -10.77% | -1.61% | 14.70% |
| cci_20_momentum | -5.69% | -11.82% | -10.77% | -1.78% | 16.27% |
| williams_14_recovery | -1.60% | -10.66% | -10.77% | -0.66% | 6.04% |
| cmf_20_accumulation | -5.93% | -12.41% | -10.77% | -1.93% | 17.59% |
| chaikin_3_10 | -6.49% | -15.46% | -10.77% | -3.81% | 34.91% |
| roc_10_momentum | -1.82% | -7.81% | -10.77% | -1.47% | 13.39% |
| trix_15_trend | -1.56% | -6.39% | -10.77% | -4.27% | 39.11% |
| keltner_20_breakout | -3.35% | -6.15% | -10.77% | -0.32% | 2.89% |
| opening_range_30m | 4.95% | -0.21% | -10.77% | -2.24% | 20.47% |

동일 구간·초기 자금, 종료 시 청산 비용 포함. 노출 맞춤은 사후 설명용이며 v2 실제 계좌 성과가 아닙니다.
[낙폭 분해·비용 영향·전체 구간](CAT/comparison.json)

[v1 전체 기록](CAT/accounts.json) · [v2 전체 기록](CAT/accounts-v2.json)

## WMT 계좌

| 모델 | 전략 | 평가액 USD | 손익 USD | 최근 매매·이유 |
|---|---|---:|---:|---|
| v1 | cash | 10000.00 | 0.00 | 대기 /  / 새 신호 대기 |
| v1 | buy_hold | 10037.89 | 37.89 | buy /  / buy_hold: prior completed bar target 100%; next bar open simulation |
| v1 | trend_8_26 | 9984.23 | -15.77 | buy /  / trend_8_26: prior completed bar target 100%; next bar open simulation |
| v1 | momentum_26 | 9995.46 | -4.54 | sell /  / momentum_26: prior completed bar target 0%; next bar open simulation |
| v1 | breakout_8 | 9953.51 | -46.49 | sell /  / breakout_8: prior completed bar target 0%; next bar open simulation |
| v1 | reversion_12 | 10043.97 | 43.97 | sell /  / reversion_12: prior completed bar target 0%; next bar open simulation |
| v1 | volume_26 | 9979.72 | -20.28 | sell /  / volume_26: prior completed bar target 0%; next bar open simulation |
| v1 | trend_8_26 AND momentum_26 | 9951.70 | -48.30 | sell /  / trend_8_26 AND momentum_26: prior completed bar target 0%; next bar open simulation |
| v1 | trend_8_26 + momentum_26 | 9989.90 | -10.10 | sell /  / trend_8_26 + momentum_26: prior completed bar target 50%; next bar open simulation |
| v1 | trend_8_26 AND breakout_8 | 10000.00 | 0.00 | 대기 /  / 새 신호 대기 |
| v1 | trend_8_26 + breakout_8 | 9968.82 | -31.18 | buy /  / trend_8_26 + breakout_8: prior completed bar target 50%; next bar open simulation |
| v1 | trend_8_26 AND reversion_12 | 10000.00 | 0.00 | 대기 /  / 새 신호 대기 |
| v1 | trend_8_26 + reversion_12 | 10014.08 | 14.08 | buy /  / trend_8_26 + reversion_12: prior completed bar target 50%; next bar open simulation |
| v1 | trend_8_26 AND volume_26 | 10000.00 | 0.00 | 대기 /  / 새 신호 대기 |
| v1 | trend_8_26 + volume_26 | 9981.91 | -18.09 | buy /  / trend_8_26 + volume_26: prior completed bar target 50%; next bar open simulation |
| v1 | momentum_26 AND breakout_8 | 10000.00 | 0.00 | 대기 /  / 새 신호 대기 |
| v1 | momentum_26 + breakout_8 | 9994.50 | -5.50 | sell /  / momentum_26 + breakout_8: prior completed bar target 0%; next bar open simulation |
| v1 | momentum_26 AND reversion_12 | 10043.97 | 43.97 | sell /  / momentum_26 AND reversion_12: prior completed bar target 0%; next bar open simulation |
| v1 | momentum_26 + reversion_12 | 10019.67 | 19.67 | sell /  / momentum_26 + reversion_12: prior completed bar target 0%; next bar open simulation |
| v1 | momentum_26 AND volume_26 | 10000.00 | 0.00 | 대기 /  / 새 신호 대기 |
| v1 | momentum_26 + volume_26 | 10007.62 | 7.62 | sell /  / momentum_26 + volume_26: prior completed bar target 0%; next bar open simulation |
| v1 | breakout_8 AND reversion_12 | 10000.00 | 0.00 | 대기 /  / 새 신호 대기 |
| v1 | breakout_8 + reversion_12 | 10018.74 | 18.74 | sell /  / breakout_8 + reversion_12: prior completed bar target 0%; next bar open simulation |
| v1 | breakout_8 AND volume_26 | 9979.72 | -20.28 | sell /  / breakout_8 AND volume_26: prior completed bar target 0%; next bar open simulation |
| v1 | breakout_8 + volume_26 | 9966.61 | -33.39 | sell /  / breakout_8 + volume_26: prior completed bar target 0%; next bar open simulation |
| v1 | reversion_12 AND volume_26 | 10000.00 | 0.00 | 대기 /  / 새 신호 대기 |
| v1 | reversion_12 + volume_26 | 10031.90 | 31.90 | sell /  / reversion_12 + volume_26: prior completed bar target 0%; next bar open simulation |
| v1 | ema_12_26 | 10037.89 | 37.89 | buy /  / EMA12 > EMA26; 조건 충족; EMA12=118.245, EMA26=118.045 |
| v1 | macd_12_26_9 | 10000.00 | 0.00 | 대기 /  / 새 신호 대기 |
| v1 | rsi_14_recovery | 10000.00 | 0.00 | 대기 /  / 새 신호 대기 |
| v1 | bollinger_20_reentry | 10000.00 | 0.00 | 대기 /  / 새 신호 대기 |
| v1 | donchian_20 | 10000.00 | 0.00 | 대기 /  / 새 신호 대기 |
| v1 | atr_14_breakout | 9979.72 | -20.28 | sell /  / 종가 > 직전 종가 + 직전 ATR14 그리고 종가 > EMA26; 조건 미충족; close=119.375, threshold=119.607, prior_ATR14=0.486823, EMA26=118.217 |
| v1 | session_vwap | 9839.22 | -160.78 | sell /  / 종가 > 뉴욕 거래일별 누적 전형가격 VWAP; 조건 미충족; close=118.745, session_VWAP=118.899, session_volume=6.77102e+06 |
| v1 | obv_20 | 9958.82 | -41.18 | sell /  / OBV > OBV의 SMA20 그리고 종가 > EMA26; 조건 미충족; OBV=1.92333e+07, OBV_SMA20=1.94364e+07, close=118.615, EMA26=118.507 |
| v1 | stochastic_14_3_recovery | 9979.72 | -20.28 | sell /  / 직전 %K14 < 20에서 %K14가 %D3 상향 돌파 (한 봉 목표); 조건 미충족; K14=93.8952, D3=60.8222, previous_K14=82.4242, previous_D3=34.5012 |
| v1 | mfi_14_recovery | 10000.00 | 0.00 | 대기 /  / 새 신호 대기 |
| v1 | adx_14_trend | 9991.69 | -8.31 | sell /  / Wilder ADX14 >= 25 그리고 +DI14 > -DI14; 조건 미충족; ADX14=24.5142, plus_DI14=24.7537, minus_DI14=21.6519 |
| v1 | aroon_25_trend | 10000.00 | 0.00 | 대기 /  / 새 신호 대기 |
| v1 | cci_20_momentum | 9932.96 | -67.04 | sell /  / CCI20 > 100 (전형가격·평균절대편차); 조건 미충족; CCI20=99.1325 |
| v1 | williams_14_recovery | 9979.72 | -20.28 | sell /  / 직전 Williams %R14 < -80, 현재 >= -80 (한 봉 목표); 조건 미충족; Williams_R14=-6.10484, previous_R14=-17.5758 |
| v1 | cmf_20_accumulation | 10000.00 | 0.00 | 대기 /  / 새 신호 대기 |
| v1 | chaikin_3_10 | 9814.25 | -185.75 | buy /  / ADL의 EMA3 - EMA10 > 0 그리고 종가 > EMA26; 조건 충족; Chaikin3_10=85268.3, ADL=1.95276e+07, close=118.535, EMA26=118.469 |
| v1 | roc_10_momentum | 10000.00 | 0.00 | 대기 /  / 새 신호 대기 |
| v1 | trix_15_trend | 9903.86 | -96.14 | buy /  / 15봉 삼중 EMA의 1봉 변화율 TRIX > 0 그리고 종가 > EMA26; 조건 충족; TRIX15_percent=0.026499, close=118.535, EMA26=118.469 |
| v1 | keltner_20_breakout | 10000.00 | 0.00 | 대기 /  / 새 신호 대기 |
| v1 | opening_range_30m | 10000.00 | 0.00 | 대기 /  / 새 신호 대기 |
| v2 | cash | 10000.00 | 0.00 | 대기 /  / 새 신호 대기 |
| v2 | buy_hold | 10635.05 | 635.05 | buy / partial / 직전 완료 봉 목표 비중 100%; 다음 봉 시가 가정 |
| v2 | trend_8_26 | 10393.17 | 393.17 | buy / partial / 직전 완료 봉 목표 비중 100%; 다음 봉 시가 가정 |
| v2 | momentum_26 | 10412.91 | 412.91 | sell / filled / 직전 완료 봉 목표 비중 0%; 다음 봉 시가 가정 |
| v2 | breakout_8 | 9916.34 | -83.66 | sell / filled / 직전 완료 봉 목표 비중 0%; 다음 봉 시가 가정 |
| v2 | reversion_12 | 9953.01 | -46.99 | sell / filled / 직전 완료 봉 목표 비중 0%; 다음 봉 시가 가정 |
| v2 | volume_26 | 9943.08 | -56.92 | sell / filled / 직전 완료 봉 목표 비중 0%; 다음 봉 시가 가정 |
| v2 | trend_8_26 AND momentum_26 | 10358.27 | 358.27 | sell / filled / 직전 완료 봉 목표 비중 0%; 다음 봉 시가 가정 |
| v2 | trend_8_26 + momentum_26 | 10403.04 | 403.04 | sell / filled / 직전 완료 봉 목표 비중 50%; 다음 봉 시가 가정 |
| v2 | trend_8_26 AND breakout_8 | 10088.55 | 88.55 | sell / filled / 직전 완료 봉 목표 비중 0%; 다음 봉 시가 가정 |
| v2 | trend_8_26 + breakout_8 | 10152.33 | 152.33 | buy / filled / 직전 완료 봉 목표 비중 50%; 다음 봉 시가 가정 |
| v2 | trend_8_26 AND reversion_12 | 9808.74 | -191.26 | sell / filled / 직전 완료 봉 목표 비중 0%; 다음 봉 시가 가정 |
| v2 | trend_8_26 + reversion_12 | 10172.18 | 172.18 | buy / filled / 직전 완료 봉 목표 비중 50%; 다음 봉 시가 가정 |
| v2 | trend_8_26 AND volume_26 | 9949.23 | -50.77 | sell / filled / 직전 완료 봉 목표 비중 0%; 다음 봉 시가 가정 |
| v2 | trend_8_26 + volume_26 | 10167.03 | 167.03 | buy / filled / 직전 완료 봉 목표 비중 50%; 다음 봉 시가 가정 |
| v2 | momentum_26 AND breakout_8 | 9964.65 | -35.35 | sell / filled / 직전 완료 봉 목표 비중 0%; 다음 봉 시가 가정 |
| v2 | momentum_26 + breakout_8 | 10183.42 | 183.42 | sell / filled / 직전 완료 봉 목표 비중 0%; 다음 봉 시가 가정 |
| v2 | momentum_26 AND reversion_12 | 9872.00 | -128.00 | sell / filled / 직전 완료 봉 목표 비중 0%; 다음 봉 시가 가정 |
| v2 | momentum_26 + reversion_12 | 10224.72 | 224.72 | sell / filled / 직전 완료 봉 목표 비중 0%; 다음 봉 시가 가정 |
| v2 | momentum_26 AND volume_26 | 9913.82 | -86.18 | sell / filled / 직전 완료 봉 목표 비중 0%; 다음 봉 시가 가정 |
| v2 | momentum_26 + volume_26 | 10198.23 | 198.23 | sell / filled / 직전 완료 봉 목표 비중 0%; 다음 봉 시가 가정 |
| v2 | breakout_8 AND reversion_12 | 10000.00 | 0.00 | 대기 /  / 새 신호 대기 |
| v2 | breakout_8 + reversion_12 | 9977.73 | -22.27 | sell / filled / 직전 완료 봉 목표 비중 0%; 다음 봉 시가 가정 |
| v2 | breakout_8 AND volume_26 | 9928.06 | -71.94 | sell / filled / 직전 완료 봉 목표 비중 0%; 다음 봉 시가 가정 |
| v2 | breakout_8 + volume_26 | 9931.09 | -68.91 | sell / filled / 직전 완료 봉 목표 비중 0%; 다음 봉 시가 가정 |
| v2 | reversion_12 AND volume_26 | 10009.78 | 9.78 | sell / filled / 직전 완료 봉 목표 비중 0%; 다음 봉 시가 가정 |
| v2 | reversion_12 + volume_26 | 9968.93 | -31.07 | sell / filled / 직전 완료 봉 목표 비중 0%; 다음 봉 시가 가정 |
| v2 | ema_12_26 | 10036.89 | 36.89 | buy / partial / EMA12 > EMA26; 조건 충족; EMA12=118.245, EMA26=118.045; 직전 완료 봉 목표를 다음 봉 시가에 모의 적용 |
| v2 | macd_12_26_9 | 10000.00 | 0.00 | 대기 /  / 새 신호 대기 |
| v2 | rsi_14_recovery | 10000.00 | 0.00 | 대기 /  / 새 신호 대기 |
| v2 | bollinger_20_reentry | 10000.00 | 0.00 | 대기 /  / 새 신호 대기 |
| v2 | donchian_20 | 10000.00 | 0.00 | 대기 /  / 새 신호 대기 |
| v2 | atr_14_breakout | 9977.72 | -22.28 | sell / filled / 종가 > 직전 종가 + 직전 ATR14 그리고 종가 > EMA26; 조건 미충족; close=119.375, threshold=119.607, prior_ATR14=0.486823, EMA26=118.217; 직전 완료 봉 목표를 다음 봉 시가에 모의 적용 |
| v2 | session_vwap | 9835.28 | -164.72 | sell / filled / 종가 > 뉴욕 거래일별 누적 전형가격 VWAP; 조건 미충족; close=118.745, session_VWAP=118.899, session_volume=6.77102e+06; 직전 완료 봉 목표를 다음 봉 시가에 모의 적용 |
| v2 | obv_20 | 9956.83 | -43.17 | sell / filled / OBV > OBV의 SMA20 그리고 종가 > EMA26; 조건 미충족; OBV=1.92333e+07, OBV_SMA20=1.94364e+07, close=118.615, EMA26=118.507; 직전 완료 봉 목표를 다음 봉 시가에 모의 적용 |
| v2 | stochastic_14_3_recovery | 9977.72 | -22.28 | sell / filled / 직전 %K14 < 20에서 %K14가 %D3 상향 돌파 (한 봉 목표); 조건 미충족; K14=93.8952, D3=60.8222, previous_K14=82.4242, previous_D3=34.5012; 직전 완료 봉 목표를 다음 봉 시가에 모의 적용 |
| v2 | mfi_14_recovery | 10000.00 | 0.00 | 대기 /  / 새 신호 대기 |
| v2 | adx_14_trend | 9989.70 | -10.30 | sell / filled / Wilder ADX14 >= 25 그리고 +DI14 > -DI14; 조건 미충족; ADX14=24.5142, plus_DI14=24.7537, minus_DI14=21.6519; 직전 완료 봉 목표를 다음 봉 시가에 모의 적용 |
| v2 | aroon_25_trend | 10000.00 | 0.00 | 대기 /  / 새 신호 대기 |
| v2 | cci_20_momentum | 9930.98 | -69.02 | sell / filled / CCI20 > 100 (전형가격·평균절대편차); 조건 미충족; CCI20=99.1325; 직전 완료 봉 목표를 다음 봉 시가에 모의 적용 |
| v2 | williams_14_recovery | 9977.72 | -22.28 | sell / filled / 직전 Williams %R14 < -80, 현재 >= -80 (한 봉 목표); 조건 미충족; Williams_R14=-6.10484, previous_R14=-17.5758; 직전 완료 봉 목표를 다음 봉 시가에 모의 적용 |
| v2 | cmf_20_accumulation | 10000.00 | 0.00 | 대기 /  / 새 신호 대기 |
| v2 | chaikin_3_10 | 9809.34 | -190.66 | buy / partial / ADL의 EMA3 - EMA10 > 0 그리고 종가 > EMA26; 조건 충족; Chaikin3_10=85268.3, ADL=1.95276e+07, close=118.535, EMA26=118.469; 직전 완료 봉 목표를 다음 봉 시가에 모의 적용 |
| v2 | roc_10_momentum | 10000.00 | 0.00 | 대기 /  / 새 신호 대기 |
| v2 | trix_15_trend | 9900.89 | -99.11 | buy / partial / 15봉 삼중 EMA의 1봉 변화율 TRIX > 0 그리고 종가 > EMA26; 조건 충족; TRIX15_percent=0.026499, close=118.535, EMA26=118.469; 직전 완료 봉 목표를 다음 봉 시가에 모의 적용 |
| v2 | keltner_20_breakout | 10000.00 | 0.00 | 대기 /  / 새 신호 대기 |
| v2 | opening_range_30m | 10000.00 | 0.00 | 대기 /  / 새 신호 대기 |

### 같은 기간의 비용·노출 비교 (사후 연구)

| 전략 | 비용 전 | 비용 후 | 100% 보유 | 같은 평균 노출 보유 | 평균 노출 |
|---|---:|---:|---:|---:|---:|
| cash | 0.00% | 0.00% | 9.50% | 0.00% | 0.00% |
| buy_hold | 9.96% | 9.50% | 9.50% | 9.50% | 100.00% |
| trend_8_26 | 9.24% | 6.07% | 9.50% | 6.58% | 69.55% |
| momentum_26 | 7.34% | 2.92% | 9.50% | 6.61% | 69.82% |
| breakout_8 | 5.45% | -11.60% | 9.50% | 2.50% | 26.51% |
| reversion_12 | 4.02% | -5.96% | 9.50% | 1.58% | 16.80% |
| volume_26 | -0.20% | -5.50% | 9.50% | 0.52% | 5.51% |
| trend_8_26 AND momentum_26 | 8.78% | 4.30% | 9.50% | 5.98% | 63.25% |
| trend_8_26 + momentum_26 | 8.29% | 4.49% | 9.50% | 6.59% | 69.69% |
| trend_8_26 AND breakout_8 | 6.92% | -6.91% | 9.50% | 2.10% | 22.31% |
| trend_8_26 + breakout_8 | 7.34% | -3.16% | 9.50% | 4.53% | 48.04% |
| trend_8_26 AND reversion_12 | 0.42% | -4.91% | 9.50% | 0.64% | 6.82% |
| trend_8_26 + reversion_12 | 6.63% | 0.10% | 9.50% | 4.07% | 43.18% |
| trend_8_26 AND volume_26 | 1.13% | -1.39% | 9.50% | 0.20% | 2.10% |
| trend_8_26 + volume_26 | 4.45% | 0.55% | 9.50% | 3.54% | 37.54% |
| momentum_26 AND breakout_8 | 5.58% | -8.47% | 9.50% | 2.20% | 23.36% |
| momentum_26 + breakout_8 | 6.41% | -4.20% | 9.50% | 4.55% | 48.17% |
| momentum_26 AND reversion_12 | 1.36% | -4.43% | 9.50% | 0.71% | 7.61% |
| momentum_26 + reversion_12 | 5.71% | 0.27% | 9.50% | 4.09% | 43.31% |
| momentum_26 AND volume_26 | 0.44% | -3.69% | 9.50% | 0.27% | 2.89% |
| momentum_26 + volume_26 | 3.54% | -1.16% | 9.50% | 3.55% | 37.67% |
| breakout_8 AND reversion_12 | 0.00% | 0.00% | 9.50% | 0.00% | 0.00% |
| breakout_8 + reversion_12 | 4.76% | -8.24% | 9.50% | 2.04% | 21.66% |
| breakout_8 AND volume_26 | 1.29% | -0.82% | 9.50% | 0.15% | 1.57% |
| breakout_8 + volume_26 | 2.62% | -7.82% | 9.50% | 1.51% | 16.02% |
| reversion_12 AND volume_26 | -0.51% | -2.99% | 9.50% | 0.22% | 2.36% |
| reversion_12 + volume_26 | 1.90% | -5.33% | 9.50% | 1.05% | 11.16% |
| ema_12_26 | 9.28% | 7.91% | 9.50% | 6.61% | 69.82% |
| macd_12_26_9 | 8.10% | 4.53% | 9.50% | 3.39% | 35.96% |
| rsi_14_recovery | -0.68% | -2.74% | 9.50% | 0.12% | 1.31% |
| bollinger_20_reentry | 0.93% | -2.41% | 9.50% | 0.20% | 2.10% |
| donchian_20 | 4.64% | -8.52% | 9.50% | 1.33% | 14.17% |
| atr_14_breakout | -0.51% | -10.81% | 9.50% | 0.76% | 8.14% |
| session_vwap | 7.03% | -3.24% | 9.50% | 5.61% | 59.32% |
| obv_20 | 8.16% | 0.28% | 9.50% | 5.28% | 55.91% |
| stochastic_14_3_recovery | 1.43% | -9.06% | 9.50% | 0.64% | 6.82% |
| mfi_14_recovery | 0.02% | -0.81% | 9.50% | 0.05% | 0.52% |
| adx_14_trend | 8.84% | 6.13% | 9.50% | 4.78% | 50.66% |
| aroon_25_trend | 6.70% | 1.88% | 9.50% | 2.99% | 31.76% |
| cci_20_momentum | 7.75% | -0.52% | 9.50% | 3.12% | 33.07% |
| williams_14_recovery | 0.23% | -8.61% | 9.50% | 0.54% | 5.77% |
| cmf_20_accumulation | 9.25% | 1.30% | 9.50% | 3.56% | 37.80% |
| chaikin_3_10 | 5.65% | -2.05% | 9.50% | 5.08% | 53.81% |
| roc_10_momentum | -0.29% | -5.58% | 9.50% | 1.46% | 15.49% |
| trix_15_trend | 8.21% | 5.52% | 9.50% | 6.21% | 65.62% |
| keltner_20_breakout | 6.87% | -0.08% | 9.50% | 2.59% | 27.56% |
| opening_range_30m | 10.32% | 4.89% | 9.50% | 3.34% | 35.43% |

동일 구간·초기 자금, 종료 시 청산 비용 포함. 노출 맞춤은 사후 설명용이며 v2 실제 계좌 성과가 아닙니다.
[낙폭 분해·비용 영향·전체 구간](WMT/comparison.json)

[v1 전체 기록](WMT/accounts.json) · [v2 전체 기록](WMT/accounts-v2.json)
