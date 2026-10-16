# 모의투자 운영 현황

[PC·서버 장애 진단과 복구 방법](https://github.com/BaekJaeYeol/paper-trading-program/blob/main/investment-lab/docs/failure-recovery.md)

이번 실행 복구: {}

완료 봉 확인 주기: 기록 11/17회 · 기록 없는 예정 6회 · 아직 판정 전 9회 · 주의: 예약 시작 지연 또는 실행·저장 누락을 확인하세요.

[주기 판정 기준](https://github.com/BaekJaeYeol/paper-trading-program/blob/main/investment-lab/docs/session-coverage.md)

최근 확인: 2026-10-16T18:07:00.370239+00:00 (UTC)
다음 15분 확인 목표 (세션 실행 중에만 적용): 2026-10-16T18:22:00+00:00 (UTC, 실행 지연 가능)

실제 주문 없음. v1 기존 계좌와 v2 새 계좌의 시작일이 다르므로 수익률을 직접 우열 비교하지 마세요.
v2는 다음 봉 시가에 비용·스프레드·직전 거래량 제한을 적용한 가상 체결입니다. 미체결 잔량은 만료됩니다.

| 종목 | 상태 | 최근 성공 UTC | 마지막 완료 봉 UTC | 이번 새 봉 |
|---|---|---|---|---|
| SPY | updated | 2026-10-16T18:07:00.370239+00:00 | 2026-10-16T17:45:00+00:00 | 1 |
| QQQ | updated | 2026-10-16T18:07:00.370239+00:00 | 2026-10-16T17:45:00+00:00 | 1 |
| IWM | updated | 2026-10-16T18:07:00.370239+00:00 | 2026-10-16T17:45:00+00:00 | 1 |
| DIA | updated | 2026-10-16T18:07:00.370239+00:00 | 2026-10-16T17:45:00+00:00 | 1 |
| MSFT | updated | 2026-10-16T18:07:00.370239+00:00 | 2026-10-16T17:45:00+00:00 | 1 |
| JPM | updated | 2026-10-16T18:07:00.370239+00:00 | 2026-10-16T17:45:00+00:00 | 1 |
| XOM | updated | 2026-10-16T18:07:00.370239+00:00 | 2026-10-16T17:45:00+00:00 | 1 |
| JNJ | updated | 2026-10-16T18:07:00.370239+00:00 | 2026-10-16T17:45:00+00:00 | 1 |
| CAT | updated | 2026-10-16T18:07:00.370239+00:00 | 2026-10-16T17:45:00+00:00 | 1 |
| WMT | updated | 2026-10-16T18:07:00.370239+00:00 | 2026-10-16T17:45:00+00:00 | 1 |

이번 실행 소요: 43.76초
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
| v1 | buy_hold | 9852.90 | -147.10 | buy /  / buy_hold: prior completed bar target 100%; next bar open simulation |
| v1 | trend_8_26 | 9902.75 | -97.25 | sell /  / trend_8_26: prior completed bar target 0%; next bar open simulation |
| v1 | momentum_26 | 9916.54 | -83.46 | sell /  / momentum_26: prior completed bar target 0%; next bar open simulation |
| v1 | breakout_8 | 10000.00 | 0.00 | 대기 /  / 새 신호 대기 |
| v1 | reversion_12 | 9900.05 | -99.95 | sell /  / reversion_12: prior completed bar target 0%; next bar open simulation |
| v1 | volume_26 | 9925.86 | -74.14 | sell /  / volume_26: prior completed bar target 0%; next bar open simulation |
| v1 | trend_8_26 AND momentum_26 | 9916.54 | -83.46 | sell /  / trend_8_26 AND momentum_26: prior completed bar target 0%; next bar open simulation |
| v1 | trend_8_26 + momentum_26 | 9909.65 | -90.35 | sell /  / trend_8_26 + momentum_26: prior completed bar target 0%; next bar open simulation |
| v1 | trend_8_26 AND breakout_8 | 10000.00 | 0.00 | 대기 /  / 새 신호 대기 |
| v1 | trend_8_26 + breakout_8 | 9951.22 | -48.78 | sell /  / trend_8_26 + breakout_8: prior completed bar target 0%; next bar open simulation |
| v1 | trend_8_26 AND reversion_12 | 9946.23 | -53.77 | sell /  / trend_8_26 AND reversion_12: prior completed bar target 0%; next bar open simulation |
| v1 | trend_8_26 + reversion_12 | 9901.35 | -98.65 | sell /  / trend_8_26 + reversion_12: prior completed bar target 0%; next bar open simulation |
| v1 | trend_8_26 AND volume_26 | 9925.86 | -74.14 | sell /  / trend_8_26 AND volume_26: prior completed bar target 0%; next bar open simulation |
| v1 | trend_8_26 + volume_26 | 9914.27 | -85.73 | sell /  / trend_8_26 + volume_26: prior completed bar target 0%; next bar open simulation |
| v1 | momentum_26 AND breakout_8 | 10000.00 | 0.00 | 대기 /  / 새 신호 대기 |
| v1 | momentum_26 + breakout_8 | 9958.17 | -41.83 | sell /  / momentum_26 + breakout_8: prior completed bar target 0%; next bar open simulation |
| v1 | momentum_26 AND reversion_12 | 10000.00 | 0.00 | 대기 /  / 새 신호 대기 |
| v1 | momentum_26 + reversion_12 | 9928.06 | -71.94 | sell /  / momentum_26 + reversion_12: prior completed bar target 0%; next bar open simulation |
| v1 | momentum_26 AND volume_26 | 9939.68 | -60.32 | sell /  / momentum_26 AND volume_26: prior completed bar target 0%; next bar open simulation |
| v1 | momentum_26 + volume_26 | 9921.17 | -78.83 | sell /  / momentum_26 + volume_26: prior completed bar target 0%; next bar open simulation |
| v1 | breakout_8 AND reversion_12 | 10000.00 | 0.00 | 대기 /  / 새 신호 대기 |
| v1 | breakout_8 + reversion_12 | 9949.86 | -50.14 | sell /  / breakout_8 + reversion_12: prior completed bar target 0%; next bar open simulation |
| v1 | breakout_8 AND volume_26 | 10000.00 | 0.00 | 대기 /  / 새 신호 대기 |
| v1 | breakout_8 + volume_26 | 9962.84 | -37.16 | sell /  / breakout_8 + volume_26: prior completed bar target 0%; next bar open simulation |
| v1 | reversion_12 AND volume_26 | 9946.23 | -53.77 | sell /  / reversion_12 AND volume_26: prior completed bar target 0%; next bar open simulation |
| v1 | reversion_12 + volume_26 | 9912.91 | -87.09 | sell /  / reversion_12 + volume_26: prior completed bar target 0%; next bar open simulation |
| v1 | ema_12_26 | 9902.75 | -97.25 | sell /  / EMA12 > EMA26; 조건 미충족; EMA12=770.416, EMA26=770.512 |
| v1 | macd_12_26_9 | 9916.54 | -83.46 | sell /  / MACD > 신호선 그리고 MACD > 0; 조건 미충족; MACD=0.273669, signal9=0.379179 |
| v1 | rsi_14_recovery | 9956.16 | -43.84 | buy /  / 직전 RSI14 < 30, 현재 RSI14 >= 30 (한 봉 목표); 조건 충족; RSI14=33.2374, previous_RSI14=25.4013 |
| v1 | bollinger_20_reentry | 9855.13 | -144.87 | buy /  / 직전 종가 < 직전 하단밴드, 현재 하단밴드 <= 종가 <= SMA20 (한 봉 목표); 조건 충족; close=765.21, lower20=763.636, SMA20=769.073, previous_lower20=764.119 |
| v1 | donchian_20 | 10000.00 | 0.00 | 대기 /  / 새 신호 대기 |
| v1 | atr_14_breakout | 10000.00 | 0.00 | 대기 /  / 새 신호 대기 |
| v1 | session_vwap | 9891.58 | -108.42 | sell /  / 종가 > 뉴욕 거래일별 누적 전형가격 VWAP; 조건 미충족; close=771.41, session_VWAP=771.735, session_volume=1.75958e+07 |
| v1 | obv_20 | 9931.74 | -68.26 | sell /  / OBV > OBV의 SMA20 그리고 종가 > EMA26; 조건 미충족; OBV=-708839, OBV_SMA20=2.15302e+06, close=771.03, EMA26=770.746 |
| v1 | stochastic_14_3_recovery | 9929.04 | -70.96 | sell /  / 직전 %K14 < 20에서 %K14가 %D3 상향 돌파 (한 봉 목표); 조건 미충족; K14=26.1953, D3=15.1045, previous_K14=15.2388, previous_D3=9.09199 |
| v1 | mfi_14_recovery | 10000.00 | 0.00 | 대기 /  / 새 신호 대기 |
| v1 | adx_14_trend | 10000.00 | 0.00 | 대기 /  / 새 신호 대기 |
| v1 | aroon_25_trend | 9902.37 | -97.63 | sell /  / Aroon25 Up > 70 그리고 Down < 30 (동률이면 최신 극값); 조건 미충족; Aroon_up=72, Aroon_down=100 |
| v1 | cci_20_momentum | 9936.89 | -63.11 | sell /  / CCI20 > 100 (전형가격·평균절대편차); 조건 미충족; CCI20=66.0792 |
| v1 | williams_14_recovery | 9910.87 | -89.13 | buy /  / 직전 Williams %R14 < -80, 현재 >= -80 (한 봉 목표); 조건 충족; Williams_R14=-73.8047, previous_R14=-84.7612 |
| v1 | cmf_20_accumulation | 9929.81 | -70.19 | sell /  / Chaikin Money Flow20 > 0.1; 조건 미충족; CMF20=-0.158867, volume20=2.42577e+07 |
| v1 | chaikin_3_10 | 9946.30 | -53.70 | sell /  / ADL의 EMA3 - EMA10 > 0 그리고 종가 > EMA26; 조건 미충족; Chaikin3_10=-174742, ADL=3.14745e+07, close=772.2, EMA26=770.668 |
| v1 | roc_10_momentum | 10000.00 | 0.00 | 대기 /  / 새 신호 대기 |
| v1 | trix_15_trend | 9916.54 | -83.46 | sell /  / 15봉 삼중 EMA의 1봉 변화율 TRIX > 0 그리고 종가 > EMA26; 조건 미충족; TRIX15_percent=0.00866315, close=769.855, EMA26=770.806 |
| v1 | keltner_20_breakout | 10000.00 | 0.00 | 대기 /  / 새 신호 대기 |
| v1 | opening_range_30m | 9946.30 | -53.70 | sell /  / 뉴욕 09:30·09:45 두 완료 봉 최고가를 10:00 이후 종가가 돌파; 자료 부족·변동폭 또는 거래량 없음: 대기; close=772.2 |
| v2 | cash | 10000.00 | 0.00 | 대기 /  / 새 신호 대기 |
| v2 | buy_hold | 9781.83 | -218.17 | buy / partial / 직전 완료 봉 목표 비중 100%; 다음 봉 시가 가정 |
| v2 | trend_8_26 | 9786.41 | -213.59 | sell / filled / 직전 완료 봉 목표 비중 0%; 다음 봉 시가 가정 |
| v2 | momentum_26 | 9770.62 | -229.38 | sell / filled / 직전 완료 봉 목표 비중 0%; 다음 봉 시가 가정 |
| v2 | breakout_8 | 9598.61 | -401.39 | sell / filled / 직전 완료 봉 목표 비중 0%; 다음 봉 시가 가정 |
| v2 | reversion_12 | 9438.64 | -561.36 | sell / filled / 직전 완료 봉 목표 비중 0%; 다음 봉 시가 가정 |
| v2 | volume_26 | 9369.58 | -630.42 | sell / filled / 직전 완료 봉 목표 비중 0%; 다음 봉 시가 가정 |
| v2 | trend_8_26 AND momentum_26 | 9777.28 | -222.72 | sell / filled / 직전 완료 봉 목표 비중 0%; 다음 봉 시가 가정 |
| v2 | trend_8_26 + momentum_26 | 9778.53 | -221.47 | sell / filled / 직전 완료 봉 목표 비중 0%; 다음 봉 시가 가정 |
| v2 | trend_8_26 AND breakout_8 | 9825.21 | -174.79 | sell / filled / 직전 완료 봉 목표 비중 0%; 다음 봉 시가 가정 |
| v2 | trend_8_26 + breakout_8 | 9691.90 | -308.10 | sell / filled / 직전 완료 봉 목표 비중 0%; 다음 봉 시가 가정 |
| v2 | trend_8_26 AND reversion_12 | 9840.93 | -159.07 | sell / filled / 직전 완료 봉 목표 비중 0%; 다음 봉 시가 가정 |
| v2 | trend_8_26 + reversion_12 | 9610.59 | -389.41 | sell / filled / 직전 완료 봉 목표 비중 0%; 다음 봉 시가 가정 |
| v2 | trend_8_26 AND volume_26 | 9770.95 | -229.05 | sell / filled / 직전 완료 봉 목표 비중 0%; 다음 봉 시가 가정 |
| v2 | trend_8_26 + volume_26 | 9595.60 | -404.40 | sell / filled / 직전 완료 봉 목표 비중 0%; 다음 봉 시가 가정 |
| v2 | momentum_26 AND breakout_8 | 9783.53 | -216.47 | sell / filled / 직전 완료 봉 목표 비중 0%; 다음 봉 시가 가정 |
| v2 | momentum_26 + breakout_8 | 9684.14 | -315.86 | sell / filled / 직전 완료 봉 목표 비중 0%; 다음 봉 시가 가정 |
| v2 | momentum_26 AND reversion_12 | 9963.21 | -36.79 | sell / filled / 직전 완료 봉 목표 비중 0%; 다음 봉 시가 가정 |
| v2 | momentum_26 + reversion_12 | 9643.25 | -356.75 | sell / filled / 직전 완료 봉 목표 비중 0%; 다음 봉 시가 가정 |
| v2 | momentum_26 AND volume_26 | 9855.46 | -144.54 | sell / filled / 직전 완료 봉 목표 비중 0%; 다음 봉 시가 가정 |
| v2 | momentum_26 + volume_26 | 9628.18 | -371.82 | sell / filled / 직전 완료 봉 목표 비중 0%; 다음 봉 시가 가정 |
| v2 | breakout_8 AND reversion_12 | 10000.00 | 0.00 | 대기 /  / 새 신호 대기 |
| v2 | breakout_8 + reversion_12 | 9557.89 | -442.11 | sell / filled / 직전 완료 봉 목표 비중 0%; 다음 봉 시가 가정 |
| v2 | breakout_8 AND volume_26 | 9933.18 | -66.82 | sell / filled / 직전 완료 봉 목표 비중 0%; 다음 봉 시가 가정 |
| v2 | breakout_8 + volume_26 | 9522.95 | -477.05 | sell / filled / 직전 완료 봉 목표 비중 0%; 다음 봉 시가 가정 |
| v2 | reversion_12 AND volume_26 | 9689.01 | -310.99 | sell / filled / 직전 완료 봉 목표 비중 0%; 다음 봉 시가 가정 |
| v2 | reversion_12 + volume_26 | 9483.08 | -516.92 | sell / filled / 직전 완료 봉 목표 비중 0%; 다음 봉 시가 가정 |
| v2 | ema_12_26 | 9900.77 | -99.23 | sell / filled / EMA12 > EMA26; 조건 미충족; EMA12=770.416, EMA26=770.512; 직전 완료 봉 목표를 다음 봉 시가에 모의 적용 |
| v2 | macd_12_26_9 | 9914.56 | -85.44 | sell / filled / MACD > 신호선 그리고 MACD > 0; 조건 미충족; MACD=0.273669, signal9=0.379179; 직전 완료 봉 목표를 다음 봉 시가에 모의 적용 |
| v2 | rsi_14_recovery | 9955.17 | -44.83 | buy / partial / 직전 RSI14 < 30, 현재 RSI14 >= 30 (한 봉 목표); 조건 충족; RSI14=33.2374, previous_RSI14=25.4013; 직전 완료 봉 목표를 다음 봉 시가에 모의 적용 |
| v2 | bollinger_20_reentry | 9850.20 | -149.80 | buy / partial / 직전 종가 < 직전 하단밴드, 현재 하단밴드 <= 종가 <= SMA20 (한 봉 목표); 조건 충족; close=765.21, lower20=763.636, SMA20=769.073, previous_lower20=764.119; 직전 완료 봉 목표를 다음 봉 시가에 모의 적용 |
| v2 | donchian_20 | 10000.00 | 0.00 | 대기 /  / 새 신호 대기 |
| v2 | atr_14_breakout | 10000.00 | 0.00 | 대기 /  / 새 신호 대기 |
| v2 | session_vwap | 9887.63 | -112.37 | sell / filled / 종가 > 뉴욕 거래일별 누적 전형가격 VWAP; 조건 미충족; close=771.41, session_VWAP=771.735, session_volume=1.75958e+07; 직전 완료 봉 목표를 다음 봉 시가에 모의 적용 |
| v2 | obv_20 | 9929.76 | -70.24 | sell / filled / OBV > OBV의 SMA20 그리고 종가 > EMA26; 조건 미충족; OBV=-708839, OBV_SMA20=2.15302e+06, close=771.03, EMA26=770.746; 직전 완료 봉 목표를 다음 봉 시가에 모의 적용 |
| v2 | stochastic_14_3_recovery | 9925.07 | -74.93 | sell / filled / 직전 %K14 < 20에서 %K14가 %D3 상향 돌파 (한 봉 목표); 조건 미충족; K14=26.1953, D3=15.1045, previous_K14=15.2388, previous_D3=9.09199; 직전 완료 봉 목표를 다음 봉 시가에 모의 적용 |
| v2 | mfi_14_recovery | 10000.00 | 0.00 | 대기 /  / 새 신호 대기 |
| v2 | adx_14_trend | 10000.00 | 0.00 | 대기 /  / 새 신호 대기 |
| v2 | aroon_25_trend | 9900.39 | -99.61 | sell / filled / Aroon25 Up > 70 그리고 Down < 30 (동률이면 최신 극값); 조건 미충족; Aroon_up=72, Aroon_down=100; 직전 완료 봉 목표를 다음 봉 시가에 모의 적용 |
| v2 | cci_20_momentum | 9934.91 | -65.09 | sell / filled / CCI20 > 100 (전형가격·평균절대편차); 조건 미충족; CCI20=66.0792; 직전 완료 봉 목표를 다음 봉 시가에 모의 적용 |
| v2 | williams_14_recovery | 9907.89 | -92.11 | buy / partial / 직전 Williams %R14 < -80, 현재 >= -80 (한 봉 목표); 조건 충족; Williams_R14=-73.8047, previous_R14=-84.7612; 직전 완료 봉 목표를 다음 봉 시가에 모의 적용 |
| v2 | cmf_20_accumulation | 9927.82 | -72.18 | sell / filled / Chaikin Money Flow20 > 0.1; 조건 미충족; CMF20=-0.158867, volume20=2.42577e+07; 직전 완료 봉 목표를 다음 봉 시가에 모의 적용 |
| v2 | chaikin_3_10 | 9944.31 | -55.69 | sell / filled / ADL의 EMA3 - EMA10 > 0 그리고 종가 > EMA26; 조건 미충족; Chaikin3_10=-174742, ADL=3.14745e+07, close=772.2, EMA26=770.668; 직전 완료 봉 목표를 다음 봉 시가에 모의 적용 |
| v2 | roc_10_momentum | 10000.00 | 0.00 | 대기 /  / 새 신호 대기 |
| v2 | trix_15_trend | 9914.56 | -85.44 | sell / filled / 15봉 삼중 EMA의 1봉 변화율 TRIX > 0 그리고 종가 > EMA26; 조건 미충족; TRIX15_percent=0.00866315, close=769.855, EMA26=770.806; 직전 완료 봉 목표를 다음 봉 시가에 모의 적용 |
| v2 | keltner_20_breakout | 10000.00 | 0.00 | 대기 /  / 새 신호 대기 |
| v2 | opening_range_30m | 9944.31 | -55.69 | sell / filled / 뉴욕 09:30·09:45 두 완료 봉 최고가를 10:00 이후 종가가 돌파; 자료 부족·변동폭 또는 거래량 없음: 대기; close=772.2; 직전 완료 봉 목표를 다음 봉 시가에 모의 적용 |

### 같은 기간의 비용·노출 비교 (사후 연구)

| 전략 | 비용 전 | 비용 후 | 100% 보유 | 같은 평균 노출 보유 | 평균 노출 |
|---|---:|---:|---:|---:|---:|
| cash | 0.00% | 0.00% | -1.06% | -0.00% | 0.00% |
| buy_hold | -0.65% | -1.06% | -1.06% | -1.06% | 100.00% |
| trend_8_26 | 1.30% | -2.05% | -1.06% | -0.50% | 47.12% |
| momentum_26 | -0.50% | -5.00% | -1.06% | -0.49% | 46.34% |
| breakout_8 | -0.61% | -15.63% | -1.06% | -0.22% | 21.20% |
| reversion_12 | -2.60% | -13.05% | -1.06% | -0.32% | 29.84% |
| volume_26 | -0.94% | -9.69% | -1.06% | -0.09% | 8.90% |
| trend_8_26 AND momentum_26 | 0.82% | -2.92% | -1.06% | -0.42% | 40.05% |
| trend_8_26 + momentum_26 | 0.40% | -3.33% | -1.06% | -0.50% | 46.73% |
| trend_8_26 AND breakout_8 | 0.07% | -10.28% | -1.06% | -0.13% | 12.30% |
| trend_8_26 + breakout_8 | 0.34% | -9.09% | -1.06% | -0.36% | 34.17% |
| trend_8_26 AND reversion_12 | -0.20% | -3.90% | -1.06% | -0.06% | 6.02% |
| trend_8_26 + reversion_12 | -0.67% | -7.52% | -1.06% | -0.41% | 38.49% |
| trend_8_26 AND volume_26 | -0.57% | -4.66% | -1.06% | -0.04% | 4.19% |
| trend_8_26 + volume_26 | 0.18% | -5.95% | -1.06% | -0.30% | 28.01% |
| momentum_26 AND breakout_8 | 0.37% | -10.01% | -1.06% | -0.14% | 13.35% |
| momentum_26 + breakout_8 | -0.56% | -10.47% | -1.06% | -0.36% | 33.78% |
| momentum_26 AND reversion_12 | -1.04% | -5.11% | -1.06% | -0.07% | 6.28% |
| momentum_26 + reversion_12 | -1.56% | -8.35% | -1.06% | -0.40% | 38.09% |
| momentum_26 AND volume_26 | -0.39% | -3.27% | -1.06% | -0.02% | 2.09% |
| momentum_26 + volume_26 | -0.72% | -6.20% | -1.06% | -0.29% | 27.62% |
| breakout_8 AND reversion_12 | 0.00% | 0.00% | -1.06% | -0.00% | 0.00% |
| breakout_8 + reversion_12 | -1.61% | -13.82% | -1.06% | -0.27% | 25.53% |
| breakout_8 AND volume_26 | 0.09% | -1.17% | -1.06% | -0.01% | 1.05% |
| breakout_8 + volume_26 | -0.78% | -11.80% | -1.06% | -0.16% | 15.06% |
| reversion_12 AND volume_26 | -0.81% | -5.29% | -1.06% | -0.05% | 4.45% |
| reversion_12 + volume_26 | -1.78% | -11.02% | -1.06% | -0.21% | 19.38% |
| ema_12_26 | -0.31% | -3.60% | -1.06% | -0.51% | 47.91% |
| macd_12_26_9 | 0.47% | -3.66% | -1.06% | -0.31% | 28.80% |
| rsi_14_recovery | -0.57% | -4.26% | -1.06% | -0.02% | 2.36% |
| bollinger_20_reentry | -1.28% | -8.08% | -1.06% | -0.05% | 4.45% |
| donchian_20 | 0.11% | -6.79% | -1.06% | -0.07% | 6.54% |
| atr_14_breakout | -0.04% | -5.35% | -1.06% | -0.04% | 3.93% |
| session_vwap | 1.54% | -8.58% | -1.06% | -0.52% | 49.48% |
| obv_20 | -0.48% | -8.88% | -1.06% | -0.39% | 36.65% |
| stochastic_14_3_recovery | -0.91% | -15.88% | -1.06% | -0.11% | 10.21% |
| mfi_14_recovery | -0.01% | -2.50% | -1.06% | -0.02% | 1.57% |
| adx_14_trend | -0.10% | -3.81% | -1.06% | -0.29% | 27.75% |
| aroon_25_trend | 0.72% | -2.20% | -1.06% | -0.28% | 26.18% |
| cci_20_momentum | -0.18% | -7.84% | -1.06% | -0.22% | 20.94% |
| williams_14_recovery | -1.17% | -11.77% | -1.06% | -0.07% | 7.07% |
| cmf_20_accumulation | 2.06% | -1.73% | -1.06% | -0.48% | 45.29% |
| chaikin_3_10 | 1.63% | -4.57% | -1.06% | -0.41% | 38.74% |
| roc_10_momentum | -0.06% | -0.48% | -1.06% | -0.01% | 0.79% |
| trix_15_trend | -0.20% | -3.09% | -1.06% | -0.38% | 35.86% |
| keltner_20_breakout | 0.09% | -3.62% | -1.06% | -0.11% | 10.73% |
| opening_range_30m | 0.01% | -6.10% | -1.06% | -0.32% | 29.84% |

동일 구간·초기 자금, 종료 시 청산 비용 포함. 노출 맞춤은 사후 설명용이며 v2 실제 계좌 성과가 아닙니다.
[낙폭 분해·비용 영향·전체 구간](SPY/comparison.json)

[v1 전체 기록](SPY/accounts.json) · [v2 전체 기록](SPY/accounts-v2.json)

## QQQ 계좌

| 모델 | 전략 | 평가액 USD | 손익 USD | 최근 매매·이유 |
|---|---|---:|---:|---|
| v1 | cash | 10000.00 | 0.00 | 대기 /  / 새 신호 대기 |
| v1 | buy_hold | 9789.76 | -210.24 | buy /  / buy_hold: prior completed bar target 100%; next bar open simulation |
| v1 | trend_8_26 | 9922.86 | -77.14 | sell /  / trend_8_26: prior completed bar target 0%; next bar open simulation |
| v1 | momentum_26 | 9935.02 | -64.98 | sell /  / momentum_26: prior completed bar target 0%; next bar open simulation |
| v1 | breakout_8 | 10000.00 | 0.00 | 대기 /  / 새 신호 대기 |
| v1 | reversion_12 | 9810.69 | -189.31 | buy /  / reversion_12: prior completed bar target 100%; next bar open simulation |
| v1 | volume_26 | 9944.75 | -55.25 | sell /  / volume_26: prior completed bar target 0%; next bar open simulation |
| v1 | trend_8_26 AND momentum_26 | 9951.96 | -48.04 | sell /  / trend_8_26 AND momentum_26: prior completed bar target 0%; next bar open simulation |
| v1 | trend_8_26 + momentum_26 | 9928.92 | -71.08 | sell /  / trend_8_26 + momentum_26: prior completed bar target 0%; next bar open simulation |
| v1 | trend_8_26 AND breakout_8 | 10000.00 | 0.00 | 대기 /  / 새 신호 대기 |
| v1 | trend_8_26 + breakout_8 | 9961.32 | -38.68 | sell /  / trend_8_26 + breakout_8: prior completed bar target 0%; next bar open simulation |
| v1 | trend_8_26 AND reversion_12 | 9951.96 | -48.04 | sell /  / trend_8_26 AND reversion_12: prior completed bar target 0%; next bar open simulation |
| v1 | trend_8_26 + reversion_12 | 9866.54 | -133.46 | sell /  / trend_8_26 + reversion_12: prior completed bar target 50%; next bar open simulation |
| v1 | trend_8_26 AND volume_26 | 10000.00 | 0.00 | 대기 /  / 새 신호 대기 |
| v1 | trend_8_26 + volume_26 | 9933.75 | -66.25 | sell /  / trend_8_26 + volume_26: prior completed bar target 0%; next bar open simulation |
| v1 | momentum_26 AND breakout_8 | 10000.00 | 0.00 | 대기 /  / 새 신호 대기 |
| v1 | momentum_26 + breakout_8 | 9967.44 | -32.56 | sell /  / momentum_26 + breakout_8: prior completed bar target 0%; next bar open simulation |
| v1 | momentum_26 AND reversion_12 | 9951.96 | -48.04 | sell /  / momentum_26 AND reversion_12: prior completed bar target 0%; next bar open simulation |
| v1 | momentum_26 + reversion_12 | 9872.60 | -127.40 | sell /  / momentum_26 + reversion_12: prior completed bar target 50%; next bar open simulation |
| v1 | momentum_26 AND volume_26 | 10000.00 | 0.00 | 대기 /  / 새 신호 대기 |
| v1 | momentum_26 + volume_26 | 9939.85 | -60.15 | sell /  / momentum_26 + volume_26: prior completed bar target 0%; next bar open simulation |
| v1 | breakout_8 AND reversion_12 | 10000.00 | 0.00 | 대기 /  / 새 신호 대기 |
| v1 | breakout_8 + reversion_12 | 9904.80 | -95.20 | sell /  / breakout_8 + reversion_12: prior completed bar target 50%; next bar open simulation |
| v1 | breakout_8 AND volume_26 | 10000.00 | 0.00 | 대기 /  / 새 신호 대기 |
| v1 | breakout_8 + volume_26 | 9972.32 | -27.68 | sell /  / breakout_8 + volume_26: prior completed bar target 0%; next bar open simulation |
| v1 | reversion_12 AND volume_26 | 9950.23 | -49.77 | sell /  / reversion_12 AND volume_26: prior completed bar target 0%; next bar open simulation |
| v1 | reversion_12 + volume_26 | 9897.22 | -102.78 | sell /  / reversion_12 + volume_26: prior completed bar target 50%; next bar open simulation |
| v1 | ema_12_26 | 9930.96 | -69.04 | sell /  / EMA12 > EMA26; 조건 미충족; EMA12=725.847, EMA26=725.955 |
| v1 | macd_12_26_9 | 9930.96 | -69.04 | sell /  / MACD > 신호선 그리고 MACD > 0; 조건 미충족; MACD=-0.108239, signal9=-0.536871 |
| v1 | rsi_14_recovery | 9952.62 | -47.38 | buy /  / 직전 RSI14 < 30, 현재 RSI14 >= 30 (한 봉 목표); 조건 충족; RSI14=31.5147, previous_RSI14=27.3561 |
| v1 | bollinger_20_reentry | 9882.24 | -117.76 | sell /  / 직전 종가 < 직전 하단밴드, 현재 하단밴드 <= 종가 <= SMA20 (한 봉 목표); 조건 미충족; close=716.64, lower20=715.793, SMA20=723.132, previous_lower20=716.805 |
| v1 | donchian_20 | 10000.00 | 0.00 | 대기 /  / 새 신호 대기 |
| v1 | atr_14_breakout | 10000.00 | 0.00 | 대기 /  / 새 신호 대기 |
| v1 | session_vwap | 9874.48 | -125.52 | sell /  / 종가 > 뉴욕 거래일별 누적 전형가격 VWAP; 조건 미충족; close=721.534, session_VWAP=721.817, session_volume=9.25052e+07 |
| v1 | obv_20 | 9930.96 | -69.04 | sell /  / OBV > OBV의 SMA20 그리고 종가 > EMA26; 조건 미충족; OBV=7.37006e+07, OBV_SMA20=7.17868e+07, close=723.36, EMA26=725.955 |
| v1 | stochastic_14_3_recovery | 9756.33 | -243.67 | sell /  / 직전 %K14 < 20에서 %K14가 %D3 상향 돌파 (한 봉 목표); 조건 미충족; K14=20.5089, D3=12.4422, previous_K14=12.599, previous_D3=7.73047 |
| v1 | mfi_14_recovery | 10000.00 | 0.00 | 대기 /  / 새 신호 대기 |
| v1 | adx_14_trend | 9930.96 | -69.04 | sell /  / Wilder ADX14 >= 25 그리고 +DI14 > -DI14; 조건 미충족; ADX14=26.4264, plus_DI14=23.7408, minus_DI14=36.7914 |
| v1 | aroon_25_trend | 9922.86 | -77.14 | sell /  / Aroon25 Up > 70 그리고 Down < 30 (동률이면 최신 극값); 조건 미충족; Aroon_up=80, Aroon_down=92 |
| v1 | cci_20_momentum | 9930.96 | -69.04 | sell /  / CCI20 > 100 (전형가격·평균절대편차); 조건 미충족; CCI20=-76.1363 |
| v1 | williams_14_recovery | 9896.02 | -103.98 | buy /  / 직전 Williams %R14 < -80, 현재 >= -80 (한 봉 목표); 조건 충족; Williams_R14=-79.4911, previous_R14=-87.401 |
| v1 | cmf_20_accumulation | 9818.03 | -181.97 | sell /  / Chaikin Money Flow20 > 0.1; 조건 미충족; CMF20=0.0659721, volume20=2.62879e+08 |
| v1 | chaikin_3_10 | 9930.96 | -69.04 | sell /  / ADL의 EMA3 - EMA10 > 0 그리고 종가 > EMA26; 조건 미충족; Chaikin3_10=1.68527e+06, ADL=1.75875e+08, close=723.36, EMA26=725.955 |
| v1 | roc_10_momentum | 10000.00 | 0.00 | 대기 /  / 새 신호 대기 |
| v1 | trix_15_trend | 10000.00 | 0.00 | 대기 /  / 새 신호 대기 |
| v1 | keltner_20_breakout | 10000.00 | 0.00 | 대기 /  / 새 신호 대기 |
| v1 | opening_range_30m | 9930.96 | -69.04 | sell /  / 뉴욕 09:30·09:45 두 완료 봉 최고가를 10:00 이후 종가가 돌파; 자료 부족·변동폭 또는 거래량 없음: 대기; close=723.36 |
| v2 | cash | 10000.00 | 0.00 | 대기 /  / 새 신호 대기 |
| v2 | buy_hold | 9473.32 | -526.68 | buy / partial / 직전 완료 봉 목표 비중 100%; 다음 봉 시가 가정 |
| v2 | trend_8_26 | 9726.12 | -273.88 | sell / filled / 직전 완료 봉 목표 비중 0%; 다음 봉 시가 가정 |
| v2 | momentum_26 | 9831.49 | -168.51 | sell / filled / 직전 완료 봉 목표 비중 0%; 다음 봉 시가 가정 |
| v2 | breakout_8 | 9669.86 | -330.14 | sell / filled / 직전 완료 봉 목표 비중 0%; 다음 봉 시가 가정 |
| v2 | reversion_12 | 9331.02 | -668.98 | buy / partial / 직전 완료 봉 목표 비중 100%; 다음 봉 시가 가정 |
| v2 | volume_26 | 9565.80 | -434.20 | 중단: 손실 한도 / sell / filled / 직전 완료 봉 목표 비중 0%; 다음 봉 시가 가정 |
| v2 | trend_8_26 AND momentum_26 | 9848.25 | -151.75 | sell / filled / 직전 완료 봉 목표 비중 0%; 다음 봉 시가 가정 |
| v2 | trend_8_26 + momentum_26 | 9778.69 | -221.31 | sell / filled / 직전 완료 봉 목표 비중 0%; 다음 봉 시가 가정 |
| v2 | trend_8_26 AND breakout_8 | 9895.83 | -104.17 | sell / filled / 직전 완료 봉 목표 비중 0%; 다음 봉 시가 가정 |
| v2 | trend_8_26 + breakout_8 | 9697.89 | -302.11 | sell / filled / 직전 완료 봉 목표 비중 0%; 다음 봉 시가 가정 |
| v2 | trend_8_26 AND reversion_12 | 9811.80 | -188.20 | sell / filled / 직전 완료 봉 목표 비중 0%; 다음 봉 시가 가정 |
| v2 | trend_8_26 + reversion_12 | 9526.15 | -473.85 | sell / filled / 직전 완료 봉 목표 비중 50%; 다음 봉 시가 가정 |
| v2 | trend_8_26 AND volume_26 | 9840.10 | -159.90 | sell / filled / 직전 완료 봉 목표 비중 0%; 다음 봉 시가 가정 |
| v2 | trend_8_26 + volume_26 | 9537.59 | -462.41 | sell / filled / 직전 완료 봉 목표 비중 0%; 다음 봉 시가 가정 |
| v2 | momentum_26 AND breakout_8 | 9960.69 | -39.31 | sell / filled / 직전 완료 봉 목표 비중 0%; 다음 봉 시가 가정 |
| v2 | momentum_26 + breakout_8 | 9750.28 | -249.72 | sell / filled / 직전 완료 봉 목표 비중 0%; 다음 봉 시가 가정 |
| v2 | momentum_26 AND reversion_12 | 9949.97 | -50.03 | sell / filled / 직전 완료 봉 목표 비중 0%; 다음 봉 시가 가정 |
| v2 | momentum_26 + reversion_12 | 9597.74 | -402.26 | sell / filled / 직전 완료 봉 목표 비중 50%; 다음 봉 시가 가정 |
| v2 | momentum_26 AND volume_26 | 9936.83 | -63.17 | sell / filled / 직전 완료 봉 목표 비중 0%; 다음 봉 시가 가정 |
| v2 | momentum_26 + volume_26 | 9589.12 | -410.88 | sell / filled / 직전 완료 봉 목표 비중 0%; 다음 봉 시가 가정 |
| v2 | breakout_8 AND reversion_12 | 10000.00 | 0.00 | 대기 /  / 새 신호 대기 |
| v2 | breakout_8 + reversion_12 | 9558.58 | -441.42 | sell / filled / 직전 완료 봉 목표 비중 50%; 다음 봉 시가 가정 |
| v2 | breakout_8 AND volume_26 | 9947.98 | -52.02 | sell / filled / 직전 완료 봉 목표 비중 0%; 다음 봉 시가 가정 |
| v2 | breakout_8 + volume_26 | 9550.09 | -449.91 | sell / filled / 직전 완료 봉 목표 비중 0%; 다음 봉 시가 가정 |
| v2 | reversion_12 AND volume_26 | 9547.64 | -452.36 | 중단: 손실 한도 / sell / filled / 직전 완료 봉 목표 비중 0%; 다음 봉 시가 가정 |
| v2 | reversion_12 + volume_26 | 9381.33 | -618.67 | sell / filled / 직전 완료 봉 목표 비중 50%; 다음 봉 시가 가정 |
| v2 | ema_12_26 | 9928.97 | -71.03 | sell / filled / EMA12 > EMA26; 조건 미충족; EMA12=725.847, EMA26=725.955; 직전 완료 봉 목표를 다음 봉 시가에 모의 적용 |
| v2 | macd_12_26_9 | 9928.97 | -71.03 | sell / filled / MACD > 신호선 그리고 MACD > 0; 조건 미충족; MACD=-0.108239, signal9=-0.536871; 직전 완료 봉 목표를 다음 봉 시가에 모의 적용 |
| v2 | rsi_14_recovery | 9951.63 | -48.37 | buy / partial / 직전 RSI14 < 30, 현재 RSI14 >= 30 (한 봉 목표); 조건 충족; RSI14=31.5147, previous_RSI14=27.3561; 직전 완료 봉 목표를 다음 봉 시가에 모의 적용 |
| v2 | bollinger_20_reentry | 9878.29 | -121.71 | sell / filled / 직전 종가 < 직전 하단밴드, 현재 하단밴드 <= 종가 <= SMA20 (한 봉 목표); 조건 미충족; close=716.64, lower20=715.793, SMA20=723.132, previous_lower20=716.805; 직전 완료 봉 목표를 다음 봉 시가에 모의 적용 |
| v2 | donchian_20 | 10000.00 | 0.00 | 대기 /  / 새 신호 대기 |
| v2 | atr_14_breakout | 10000.00 | 0.00 | 대기 /  / 새 신호 대기 |
| v2 | session_vwap | 9870.53 | -129.47 | sell / filled / 종가 > 뉴욕 거래일별 누적 전형가격 VWAP; 조건 미충족; close=721.534, session_VWAP=721.817, session_volume=9.25052e+07; 직전 완료 봉 목표를 다음 봉 시가에 모의 적용 |
| v2 | obv_20 | 9928.97 | -71.03 | sell / filled / OBV > OBV의 SMA20 그리고 종가 > EMA26; 조건 미충족; OBV=7.37006e+07, OBV_SMA20=7.17868e+07, close=723.36, EMA26=725.955; 직전 완료 봉 목표를 다음 봉 시가에 모의 적용 |
| v2 | stochastic_14_3_recovery | 9746.57 | -253.43 | sell / filled / 직전 %K14 < 20에서 %K14가 %D3 상향 돌파 (한 봉 목표); 조건 미충족; K14=20.5089, D3=12.4422, previous_K14=12.599, previous_D3=7.73047; 직전 완료 봉 목표를 다음 봉 시가에 모의 적용 |
| v2 | mfi_14_recovery | 10000.00 | 0.00 | 대기 /  / 새 신호 대기 |
| v2 | adx_14_trend | 9928.97 | -71.03 | sell / filled / Wilder ADX14 >= 25 그리고 +DI14 > -DI14; 조건 미충족; ADX14=26.4264, plus_DI14=23.7408, minus_DI14=36.7914; 직전 완료 봉 목표를 다음 봉 시가에 모의 적용 |
| v2 | aroon_25_trend | 9920.88 | -79.12 | sell / filled / Aroon25 Up > 70 그리고 Down < 30 (동률이면 최신 극값); 조건 미충족; Aroon_up=80, Aroon_down=92; 직전 완료 봉 목표를 다음 봉 시가에 모의 적용 |
| v2 | cci_20_momentum | 9928.97 | -71.03 | sell / filled / CCI20 > 100 (전형가격·평균절대편차); 조건 미충족; CCI20=-76.1363; 직전 완료 봉 목표를 다음 봉 시가에 모의 적용 |
| v2 | williams_14_recovery | 9893.05 | -106.95 | buy / partial / 직전 Williams %R14 < -80, 현재 >= -80 (한 봉 목표); 조건 충족; Williams_R14=-79.4911, previous_R14=-87.401; 직전 완료 봉 목표를 다음 봉 시가에 모의 적용 |
| v2 | cmf_20_accumulation | 9812.14 | -187.86 | sell / filled / Chaikin Money Flow20 > 0.1; 조건 미충족; CMF20=0.0659721, volume20=2.62879e+08; 직전 완료 봉 목표를 다음 봉 시가에 모의 적용 |
| v2 | chaikin_3_10 | 9928.97 | -71.03 | sell / filled / ADL의 EMA3 - EMA10 > 0 그리고 종가 > EMA26; 조건 미충족; Chaikin3_10=1.68527e+06, ADL=1.75875e+08, close=723.36, EMA26=725.955; 직전 완료 봉 목표를 다음 봉 시가에 모의 적용 |
| v2 | roc_10_momentum | 10000.00 | 0.00 | 대기 /  / 새 신호 대기 |
| v2 | trix_15_trend | 10000.00 | 0.00 | 대기 /  / 새 신호 대기 |
| v2 | keltner_20_breakout | 10000.00 | 0.00 | 대기 /  / 새 신호 대기 |
| v2 | opening_range_30m | 9928.97 | -71.03 | sell / filled / 뉴욕 09:30·09:45 두 완료 봉 최고가를 10:00 이후 종가가 돌파; 자료 부족·변동폭 또는 거래량 없음: 대기; close=723.36; 직전 완료 봉 목표를 다음 봉 시가에 모의 적용 |

### 같은 기간의 비용·노출 비교 (사후 연구)

| 전략 | 비용 전 | 비용 후 | 100% 보유 | 같은 평균 노출 보유 | 평균 노출 |
|---|---:|---:|---:|---:|---:|
| cash | 0.00% | 0.00% | -4.29% | -0.00% | 0.00% |
| buy_hold | -3.89% | -4.29% | -4.29% | -4.29% | 100.00% |
| trend_8_26 | 0.18% | -3.54% | -4.29% | -1.89% | 43.98% |
| momentum_26 | -1.10% | -5.96% | -4.29% | -1.62% | 37.70% |
| breakout_8 | -1.46% | -16.35% | -4.29% | -0.75% | 17.54% |
| reversion_12 | -1.94% | -14.27% | -4.29% | -1.27% | 29.58% |
| volume_26 | -1.23% | -14.01% | -4.29% | -0.64% | 14.92% |
| trend_8_26 AND momentum_26 | 0.04% | -4.08% | -4.29% | -1.41% | 32.98% |
| trend_8_26 + momentum_26 | -0.46% | -4.56% | -4.29% | -1.75% | 40.84% |
| trend_8_26 AND breakout_8 | -0.32% | -9.11% | -4.29% | -0.45% | 10.47% |
| trend_8_26 + breakout_8 | -0.64% | -9.80% | -4.29% | -1.32% | 30.77% |
| trend_8_26 AND reversion_12 | 0.15% | -5.17% | -4.29% | -0.28% | 6.54% |
| trend_8_26 + reversion_12 | -0.88% | -8.50% | -4.29% | -1.58% | 36.79% |
| trend_8_26 AND volume_26 | -0.71% | -5.59% | -4.29% | -0.18% | 4.19% |
| trend_8_26 + volume_26 | -0.52% | -8.74% | -4.29% | -1.26% | 29.46% |
| momentum_26 AND breakout_8 | -0.13% | -8.56% | -4.29% | -0.44% | 10.21% |
| momentum_26 + breakout_8 | -1.28% | -11.12% | -4.29% | -1.18% | 27.62% |
| momentum_26 AND reversion_12 | -0.29% | -5.59% | -4.29% | -0.22% | 5.24% |
| momentum_26 + reversion_12 | -1.51% | -9.65% | -4.29% | -1.44% | 33.64% |
| momentum_26 AND volume_26 | -0.30% | -4.40% | -4.29% | -0.15% | 3.40% |
| momentum_26 + volume_26 | -1.16% | -9.89% | -4.29% | -1.13% | 26.31% |
| breakout_8 AND reversion_12 | 0.00% | 0.00% | -4.29% | -0.00% | 0.00% |
| breakout_8 + reversion_12 | -1.69% | -14.44% | -4.29% | -1.01% | 23.57% |
| breakout_8 AND volume_26 | 0.04% | -2.04% | -4.29% | -0.06% | 1.31% |
| breakout_8 + volume_26 | -1.34% | -13.94% | -4.29% | -0.70% | 16.24% |
| reversion_12 AND volume_26 | -1.34% | -8.91% | -4.29% | -0.39% | 9.16% |
| reversion_12 + volume_26 | -1.58% | -13.60% | -4.29% | -0.95% | 22.26% |
| ema_12_26 | 0.71% | -1.38% | -4.29% | -1.52% | 35.34% |
| macd_12_26_9 | 1.49% | -1.86% | -4.29% | -0.86% | 20.16% |
| rsi_14_recovery | -0.78% | -5.65% | -4.29% | -0.13% | 3.14% |
| bollinger_20_reentry | -0.40% | -6.48% | -4.29% | -0.17% | 3.93% |
| donchian_20 | 0.28% | -4.24% | -4.29% | -0.20% | 4.71% |
| atr_14_breakout | -0.26% | -4.76% | -4.29% | -0.13% | 3.14% |
| session_vwap | -0.77% | -12.15% | -4.29% | -2.17% | 50.52% |
| obv_20 | -1.35% | -10.05% | -4.29% | -1.14% | 26.70% |
| stochastic_14_3_recovery | -0.36% | -12.15% | -4.29% | -0.34% | 7.85% |
| mfi_14_recovery | -0.16% | -1.82% | -4.29% | -0.04% | 1.05% |
| adx_14_trend | -0.71% | -3.59% | -4.29% | -0.80% | 18.59% |
| aroon_25_trend | 1.40% | -1.95% | -4.29% | -0.84% | 19.63% |
| cci_20_momentum | -0.85% | -5.72% | -4.29% | -0.64% | 14.92% |
| williams_14_recovery | -0.95% | -11.57% | -4.29% | -0.30% | 7.07% |
| cmf_20_accumulation | -1.55% | -9.10% | -4.29% | -1.34% | 31.15% |
| chaikin_3_10 | -2.51% | -10.37% | -4.29% | -1.44% | 33.51% |
| roc_10_momentum | -0.31% | -1.56% | -4.29% | -0.09% | 2.09% |
| trix_15_trend | 0.59% | -1.09% | -4.29% | -1.26% | 29.32% |
| keltner_20_breakout | -0.73% | -4.81% | -4.29% | -0.31% | 7.33% |
| opening_range_30m | -0.35% | -6.04% | -4.29% | -0.93% | 21.73% |

동일 구간·초기 자금, 종료 시 청산 비용 포함. 노출 맞춤은 사후 설명용이며 v2 실제 계좌 성과가 아닙니다.
[낙폭 분해·비용 영향·전체 구간](QQQ/comparison.json)

[v1 전체 기록](QQQ/accounts.json) · [v2 전체 기록](QQQ/accounts-v2.json)

## IWM 계좌

| 모델 | 전략 | 평가액 USD | 손익 USD | 최근 매매·이유 |
|---|---|---:|---:|---|
| v1 | cash | 10000.00 | 0.00 | 대기 /  / 새 신호 대기 |
| v1 | buy_hold | 9791.49 | -208.51 | buy /  / buy_hold: prior completed bar target 100%; next bar open simulation |
| v1 | trend_8_26 | 9838.25 | -161.75 | sell /  / trend_8_26: prior completed bar target 0%; next bar open simulation |
| v1 | momentum_26 | 9895.73 | -104.27 | sell /  / momentum_26: prior completed bar target 0%; next bar open simulation |
| v1 | breakout_8 | 9929.38 | -70.62 | sell /  / breakout_8: prior completed bar target 0%; next bar open simulation |
| v1 | reversion_12 | 9867.30 | -132.70 | sell /  / reversion_12: prior completed bar target 0%; next bar open simulation |
| v1 | volume_26 | 9935.98 | -64.02 | sell /  / volume_26: prior completed bar target 0%; next bar open simulation |
| v1 | trend_8_26 AND momentum_26 | 9895.73 | -104.27 | sell /  / trend_8_26 AND momentum_26: prior completed bar target 0%; next bar open simulation |
| v1 | trend_8_26 + momentum_26 | 9866.97 | -133.03 | sell /  / trend_8_26 + momentum_26: prior completed bar target 0%; next bar open simulation |
| v1 | trend_8_26 AND breakout_8 | 9929.38 | -70.62 | sell /  / trend_8_26 AND breakout_8: prior completed bar target 0%; next bar open simulation |
| v1 | trend_8_26 + breakout_8 | 9883.72 | -116.28 | sell /  / trend_8_26 + breakout_8: prior completed bar target 0%; next bar open simulation |
| v1 | trend_8_26 AND reversion_12 | 9902.23 | -97.77 | sell /  / trend_8_26 AND reversion_12: prior completed bar target 0%; next bar open simulation |
| v1 | trend_8_26 + reversion_12 | 9852.71 | -147.29 | sell /  / trend_8_26 + reversion_12: prior completed bar target 0%; next bar open simulation |
| v1 | trend_8_26 AND volume_26 | 9935.98 | -64.02 | sell /  / trend_8_26 AND volume_26: prior completed bar target 0%; next bar open simulation |
| v1 | trend_8_26 + volume_26 | 9886.95 | -113.05 | sell /  / trend_8_26 + volume_26: prior completed bar target 0%; next bar open simulation |
| v1 | momentum_26 AND breakout_8 | 9929.38 | -70.62 | sell /  / momentum_26 AND breakout_8: prior completed bar target 0%; next bar open simulation |
| v1 | momentum_26 + breakout_8 | 9912.56 | -87.44 | sell /  / momentum_26 + breakout_8: prior completed bar target 0%; next bar open simulation |
| v1 | momentum_26 AND reversion_12 | 10000.00 | 0.00 | 대기 /  / 새 신호 대기 |
| v1 | momentum_26 + reversion_12 | 9901.22 | -98.78 | sell /  / momentum_26 + reversion_12: prior completed bar target 0%; next bar open simulation |
| v1 | momentum_26 AND volume_26 | 10000.00 | 0.00 | 대기 /  / 새 신호 대기 |
| v1 | momentum_26 + volume_26 | 9915.81 | -84.19 | sell /  / momentum_26 + volume_26: prior completed bar target 0%; next bar open simulation |
| v1 | breakout_8 AND reversion_12 | 10000.00 | 0.00 | 대기 /  / 새 신호 대기 |
| v1 | breakout_8 + reversion_12 | 9898.24 | -101.76 | sell /  / breakout_8 + reversion_12: prior completed bar target 0%; next bar open simulation |
| v1 | breakout_8 AND volume_26 | 10000.00 | 0.00 | 대기 /  / 새 신호 대기 |
| v1 | breakout_8 + volume_26 | 9932.66 | -67.34 | sell /  / breakout_8 + volume_26: prior completed bar target 0%; next bar open simulation |
| v1 | reversion_12 AND volume_26 | 9935.98 | -64.02 | sell /  / reversion_12 AND volume_26: prior completed bar target 0%; next bar open simulation |
| v1 | reversion_12 + volume_26 | 9901.54 | -98.46 | sell /  / reversion_12 + volume_26: prior completed bar target 0%; next bar open simulation |
| v1 | ema_12_26 | 9838.25 | -161.75 | sell /  / EMA12 > EMA26; 조건 미충족; EMA12=273.669, EMA26=273.722 |
| v1 | macd_12_26_9 | 9916.70 | -83.30 | sell /  / MACD > 신호선 그리고 MACD > 0; 조건 미충족; MACD=0.425881, signal9=0.461272 |
| v1 | rsi_14_recovery | 9947.83 | -52.17 | buy /  / 직전 RSI14 < 30, 현재 RSI14 >= 30 (한 봉 목표); 조건 충족; RSI14=32.5191, previous_RSI14=25.4828 |
| v1 | bollinger_20_reentry | 9924.03 | -75.97 | sell /  / 직전 종가 < 직전 하단밴드, 현재 하단밴드 <= 종가 <= SMA20 (한 봉 목표); 조건 미충족; close=271.19, lower20=270.018, SMA20=273.224, previous_lower20=270.283 |
| v1 | donchian_20 | 9929.38 | -70.62 | sell /  / 종가 > 현재 봉을 제외한 직전 20봉 최고가; 조건 미충족; close=274.88, prior_high20=275.91 |
| v1 | atr_14_breakout | 9929.38 | -70.62 | sell /  / 종가 > 직전 종가 + 직전 ATR14 그리고 종가 > EMA26; 조건 미충족; close=274.88, threshold=276.257, prior_ATR14=0.526844, EMA26=273.855 |
| v1 | session_vwap | 9937.31 | -62.69 | sell /  / 종가 > 뉴욕 거래일별 누적 전형가격 VWAP; 조건 미충족; close=274.88, session_VWAP=275.422, session_volume=2.52313e+06 |
| v1 | obv_20 | 9928.63 | -71.37 | sell /  / OBV > OBV의 SMA20 그리고 종가 > EMA26; 조건 미충족; OBV=-4.10489e+07, OBV_SMA20=-4.0926e+07, close=274.64, EMA26=273.913 |
| v1 | stochastic_14_3_recovery | 9857.46 | -142.54 | sell /  / 직전 %K14 < 20에서 %K14가 %D3 상향 돌파 (한 봉 목표); 조건 미충족; K14=19.3547, D3=10.3979, previous_K14=9.21269, previous_D3=6.40044 |
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
| v2 | buy_hold | 9686.80 | -313.20 | buy / partial / 직전 완료 봉 목표 비중 100%; 다음 봉 시가 가정 |
| v2 | trend_8_26 | 9709.80 | -290.20 | sell / filled / 직전 완료 봉 목표 비중 0%; 다음 봉 시가 가정 |
| v2 | momentum_26 | 9767.53 | -232.47 | sell / filled / 직전 완료 봉 목표 비중 0%; 다음 봉 시가 가정 |
| v2 | breakout_8 | 9547.89 | -452.11 | sell / filled / 직전 완료 봉 목표 비중 0%; 다음 봉 시가 가정 |
| v2 | reversion_12 | 9410.21 | -589.79 | sell / filled / 직전 완료 봉 목표 비중 0%; 다음 봉 시가 가정 |
| v2 | volume_26 | 9450.57 | -549.43 | sell / filled / 직전 완료 봉 목표 비중 0%; 다음 봉 시가 가정 |
| v2 | trend_8_26 AND momentum_26 | 9918.12 | -81.88 | sell / filled / 직전 완료 봉 목표 비중 0%; 다음 봉 시가 가정 |
| v2 | trend_8_26 + momentum_26 | 9759.25 | -240.75 | sell / filled / 직전 완료 봉 목표 비중 0%; 다음 봉 시가 가정 |
| v2 | trend_8_26 AND breakout_8 | 9840.76 | -159.24 | sell / filled / 직전 완료 봉 목표 비중 0%; 다음 봉 시가 가정 |
| v2 | trend_8_26 + breakout_8 | 9648.89 | -351.11 | sell / filled / 직전 완료 봉 목표 비중 0%; 다음 봉 시가 가정 |
| v2 | trend_8_26 AND reversion_12 | 9783.25 | -216.75 | sell / filled / 직전 완료 봉 목표 비중 0%; 다음 봉 시가 가정 |
| v2 | trend_8_26 + reversion_12 | 9558.62 | -441.38 | sell / filled / 직전 완료 봉 목표 비중 0%; 다음 봉 시가 가정 |
| v2 | trend_8_26 AND volume_26 | 9797.73 | -202.27 | sell / filled / 직전 완료 봉 목표 비중 0%; 다음 봉 시가 가정 |
| v2 | trend_8_26 + volume_26 | 9599.39 | -400.61 | sell / filled / 직전 완료 봉 목표 비중 0%; 다음 봉 시가 가정 |
| v2 | momentum_26 AND breakout_8 | 9733.71 | -266.29 | sell / filled / 직전 완료 봉 목표 비중 0%; 다음 봉 시가 가정 |
| v2 | momentum_26 + breakout_8 | 9657.13 | -342.87 | sell / filled / 직전 완료 봉 목표 비중 0%; 다음 봉 시가 가정 |
| v2 | momentum_26 AND reversion_12 | 9960.59 | -39.41 | sell / filled / 직전 완료 봉 목표 비중 0%; 다음 봉 시가 가정 |
| v2 | momentum_26 + reversion_12 | 9627.11 | -372.89 | sell / filled / 직전 완료 봉 목표 비중 0%; 다음 봉 시가 가정 |
| v2 | momentum_26 AND volume_26 | 9897.79 | -102.21 | sell / filled / 직전 완료 봉 목표 비중 0%; 다음 봉 시가 가정 |
| v2 | momentum_26 + volume_26 | 9607.50 | -392.50 | sell / filled / 직전 완료 봉 목표 비중 0%; 다음 봉 시가 가정 |
| v2 | breakout_8 AND reversion_12 | 10000.00 | 0.00 | 대기 /  / 새 신호 대기 |
| v2 | breakout_8 + reversion_12 | 9518.25 | -481.75 | sell / filled / 직전 완료 봉 목표 비중 0%; 다음 봉 시가 가정 |
| v2 | breakout_8 AND volume_26 | 9746.03 | -253.97 | sell / filled / 직전 완료 봉 목표 비중 0%; 다음 봉 시가 가정 |
| v2 | breakout_8 + volume_26 | 9519.00 | -481.00 | sell / filled / 직전 완료 봉 목표 비중 0%; 다음 봉 시가 가정 |
| v2 | reversion_12 AND volume_26 | 9676.46 | -323.54 | sell / filled / 직전 완료 봉 목표 비중 0%; 다음 봉 시가 가정 |
| v2 | reversion_12 + volume_26 | 9449.94 | -550.06 | sell / filled / 직전 완료 봉 목표 비중 0%; 다음 봉 시가 가정 |
| v2 | ema_12_26 | 9836.29 | -163.71 | sell / filled / EMA12 > EMA26; 조건 미충족; EMA12=273.669, EMA26=273.722; 직전 완료 봉 목표를 다음 봉 시가에 모의 적용 |
| v2 | macd_12_26_9 | 9914.72 | -85.28 | sell / filled / MACD > 신호선 그리고 MACD > 0; 조건 미충족; MACD=0.425881, signal9=0.461272; 직전 완료 봉 목표를 다음 봉 시가에 모의 적용 |
| v2 | rsi_14_recovery | 9946.84 | -53.16 | buy / partial / 직전 RSI14 < 30, 현재 RSI14 >= 30 (한 봉 목표); 조건 충족; RSI14=32.5191, previous_RSI14=25.4828; 직전 완료 봉 목표를 다음 봉 시가에 모의 적용 |
| v2 | bollinger_20_reentry | 9920.06 | -79.94 | sell / filled / 직전 종가 < 직전 하단밴드, 현재 하단밴드 <= 종가 <= SMA20 (한 봉 목표); 조건 미충족; close=271.19, lower20=270.018, SMA20=273.224, previous_lower20=270.283; 직전 완료 봉 목표를 다음 봉 시가에 모의 적용 |
| v2 | donchian_20 | 9927.39 | -72.61 | sell / filled / 종가 > 현재 봉을 제외한 직전 20봉 최고가; 조건 미충족; close=274.88, prior_high20=275.91; 직전 완료 봉 목표를 다음 봉 시가에 모의 적용 |
| v2 | atr_14_breakout | 9927.39 | -72.61 | sell / filled / 종가 > 직전 종가 + 직전 ATR14 그리고 종가 > EMA26; 조건 미충족; close=274.88, threshold=276.257, prior_ATR14=0.526844, EMA26=273.855; 직전 완료 봉 목표를 다음 봉 시가에 모의 적용 |
| v2 | session_vwap | 9935.32 | -64.68 | sell / filled / 종가 > 뉴욕 거래일별 누적 전형가격 VWAP; 조건 미충족; close=274.88, session_VWAP=275.422, session_volume=2.52313e+06; 직전 완료 봉 목표를 다음 봉 시가에 모의 적용 |
| v2 | obv_20 | 9926.64 | -73.36 | sell / filled / OBV > OBV의 SMA20 그리고 종가 > EMA26; 조건 미충족; OBV=-4.10489e+07, OBV_SMA20=-4.0926e+07, close=274.64, EMA26=273.913; 직전 완료 봉 목표를 다음 봉 시가에 모의 적용 |
| v2 | stochastic_14_3_recovery | 9851.55 | -148.45 | sell / filled / 직전 %K14 < 20에서 %K14가 %D3 상향 돌파 (한 봉 목표); 조건 미충족; K14=19.3547, D3=10.3979, previous_K14=9.21269, previous_D3=6.40044; 직전 완료 봉 목표를 다음 봉 시가에 모의 적용 |
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
| cash | 0.00% | 0.00% | -3.98% | -0.00% | 0.00% |
| buy_hold | -3.57% | -3.98% | -3.98% | -3.98% | 100.00% |
| trend_8_26 | -1.57% | -5.22% | -3.98% | -1.74% | 43.46% |
| momentum_26 | -2.36% | -7.94% | -3.98% | -1.51% | 37.70% |
| breakout_8 | -0.95% | -13.77% | -3.98% | -0.76% | 18.85% |
| reversion_12 | -3.09% | -15.63% | -3.98% | -1.27% | 31.68% |
| volume_26 | -2.55% | -9.65% | -3.98% | -0.35% | 8.64% |
| trend_8_26 AND momentum_26 | -1.24% | -5.30% | -3.98% | -1.31% | 32.72% |
| trend_8_26 + momentum_26 | -1.96% | -6.19% | -3.98% | -1.62% | 40.58% |
| trend_8_26 AND breakout_8 | -0.45% | -7.70% | -3.98% | -0.43% | 10.73% |
| trend_8_26 + breakout_8 | -1.25% | -9.41% | -3.98% | -1.25% | 31.16% |
| trend_8_26 AND reversion_12 | -0.73% | -5.61% | -3.98% | -0.24% | 6.02% |
| trend_8_26 + reversion_12 | -2.32% | -10.40% | -3.98% | -1.50% | 37.57% |
| trend_8_26 AND volume_26 | -1.26% | -4.93% | -3.98% | -0.15% | 3.66% |
| trend_8_26 + volume_26 | -2.05% | -7.27% | -3.98% | -1.04% | 26.05% |
| momentum_26 AND breakout_8 | -0.21% | -7.48% | -3.98% | -0.41% | 10.21% |
| momentum_26 + breakout_8 | -1.65% | -10.90% | -3.98% | -1.13% | 28.28% |
| momentum_26 AND reversion_12 | -0.08% | -3.38% | -3.98% | -0.11% | 2.62% |
| momentum_26 + reversion_12 | -2.72% | -10.57% | -3.98% | -1.39% | 34.69% |
| momentum_26 AND volume_26 | -1.32% | -3.77% | -3.98% | -0.07% | 1.83% |
| momentum_26 + volume_26 | -2.45% | -8.42% | -3.98% | -0.93% | 23.17% |
| breakout_8 AND reversion_12 | 0.00% | 0.00% | -3.98% | -0.00% | 0.00% |
| breakout_8 + reversion_12 | -2.02% | -14.00% | -3.98% | -1.01% | 25.27% |
| breakout_8 AND volume_26 | -1.30% | -3.76% | -3.98% | -0.08% | 2.09% |
| breakout_8 + volume_26 | -1.75% | -11.55% | -3.98% | -0.55% | 13.75% |
| reversion_12 AND volume_26 | -0.62% | -5.10% | -3.98% | -0.19% | 4.71% |
| reversion_12 + volume_26 | -2.82% | -12.15% | -3.98% | -0.81% | 20.16% |
| ema_12_26 | 0.04% | -2.45% | -3.98% | -1.69% | 42.15% |
| macd_12_26_9 | 1.88% | -0.23% | -3.98% | -1.07% | 26.70% |
| rsi_14_recovery | -0.60% | -5.49% | -3.98% | -0.13% | 3.14% |
| bollinger_20_reentry | -0.21% | -5.51% | -3.98% | -0.14% | 3.40% |
| donchian_20 | -0.20% | -5.10% | -3.98% | -0.22% | 5.50% |
| atr_14_breakout | -1.87% | -8.25% | -3.98% | -0.17% | 4.19% |
| session_vwap | -0.94% | -10.44% | -3.98% | -1.68% | 41.88% |
| obv_20 | 0.44% | -3.28% | -3.98% | -1.47% | 36.65% |
| stochastic_14_3_recovery | -1.10% | -14.62% | -3.98% | -0.37% | 9.16% |
| mfi_14_recovery | 0.22% | -3.50% | -3.98% | -0.09% | 2.36% |
| adx_14_trend | -0.58% | -4.27% | -3.98% | -1.26% | 31.41% |
| aroon_25_trend | -1.70% | -4.95% | -3.98% | -0.82% | 20.42% |
| cci_20_momentum | -1.95% | -7.93% | -3.98% | -0.69% | 17.28% |
| williams_14_recovery | -0.74% | -10.26% | -3.98% | -0.25% | 6.28% |
| cmf_20_accumulation | -1.75% | -7.75% | -3.98% | -0.70% | 17.54% |
| chaikin_3_10 | -2.41% | -8.75% | -3.98% | -1.25% | 31.15% |
| roc_10_momentum | -0.63% | -1.87% | -3.98% | -0.13% | 3.14% |
| trix_15_trend | 0.35% | -2.56% | -3.98% | -1.25% | 31.15% |
| keltner_20_breakout | -0.91% | -4.18% | -3.98% | -0.21% | 5.24% |
| opening_range_30m | 1.50% | -3.49% | -3.98% | -0.97% | 24.08% |

동일 구간·초기 자금, 종료 시 청산 비용 포함. 노출 맞춤은 사후 설명용이며 v2 실제 계좌 성과가 아닙니다.
[낙폭 분해·비용 영향·전체 구간](IWM/comparison.json)

[v1 전체 기록](IWM/accounts.json) · [v2 전체 기록](IWM/accounts-v2.json)

## DIA 계좌

| 모델 | 전략 | 평가액 USD | 손익 USD | 최근 매매·이유 |
|---|---|---:|---:|---|
| v1 | cash | 10000.00 | 0.00 | 대기 /  / 새 신호 대기 |
| v1 | buy_hold | 9898.34 | -101.66 | buy /  / buy_hold: prior completed bar target 100%; next bar open simulation |
| v1 | trend_8_26 | 9904.27 | -95.73 | sell /  / trend_8_26: prior completed bar target 0%; next bar open simulation |
| v1 | momentum_26 | 9909.03 | -90.97 | sell /  / momentum_26: prior completed bar target 0%; next bar open simulation |
| v1 | breakout_8 | 9940.12 | -59.88 | sell /  / breakout_8: prior completed bar target 0%; next bar open simulation |
| v1 | reversion_12 | 9931.61 | -68.39 | sell /  / reversion_12: prior completed bar target 0%; next bar open simulation |
| v1 | volume_26 | 9908.95 | -91.05 | sell /  / volume_26: prior completed bar target 0%; next bar open simulation |
| v1 | trend_8_26 AND momentum_26 | 9909.03 | -90.97 | sell /  / trend_8_26 AND momentum_26: prior completed bar target 0%; next bar open simulation |
| v1 | trend_8_26 + momentum_26 | 9906.65 | -93.35 | sell /  / trend_8_26 + momentum_26: prior completed bar target 0%; next bar open simulation |
| v1 | trend_8_26 AND breakout_8 | 9940.12 | -59.88 | sell /  / trend_8_26 AND breakout_8: prior completed bar target 0%; next bar open simulation |
| v1 | trend_8_26 + breakout_8 | 9922.18 | -77.82 | sell /  / trend_8_26 + breakout_8: prior completed bar target 0%; next bar open simulation |
| v1 | trend_8_26 AND reversion_12 | 9936.00 | -64.00 | sell /  / trend_8_26 AND reversion_12: prior completed bar target 0%; next bar open simulation |
| v1 | trend_8_26 + reversion_12 | 9917.88 | -82.12 | sell /  / trend_8_26 + reversion_12: prior completed bar target 0%; next bar open simulation |
| v1 | trend_8_26 AND volume_26 | 9943.10 | -56.90 | sell /  / trend_8_26 AND volume_26: prior completed bar target 0%; next bar open simulation |
| v1 | trend_8_26 + volume_26 | 9906.54 | -93.46 | sell /  / trend_8_26 + volume_26: prior completed bar target 0%; next bar open simulation |
| v1 | momentum_26 AND breakout_8 | 9940.12 | -59.88 | sell /  / momentum_26 AND breakout_8: prior completed bar target 0%; next bar open simulation |
| v1 | momentum_26 + breakout_8 | 9924.57 | -75.43 | sell /  / momentum_26 + breakout_8: prior completed bar target 0%; next bar open simulation |
| v1 | momentum_26 AND reversion_12 | 9940.78 | -59.22 | sell /  / momentum_26 AND reversion_12: prior completed bar target 0%; next bar open simulation |
| v1 | momentum_26 + reversion_12 | 9920.26 | -79.74 | sell /  / momentum_26 + reversion_12: prior completed bar target 0%; next bar open simulation |
| v1 | momentum_26 AND volume_26 | 9943.10 | -56.90 | sell /  / momentum_26 AND volume_26: prior completed bar target 0%; next bar open simulation |
| v1 | momentum_26 + volume_26 | 9908.93 | -91.07 | sell /  / momentum_26 + volume_26: prior completed bar target 0%; next bar open simulation |
| v1 | breakout_8 AND reversion_12 | 10000.00 | 0.00 | 대기 /  / 새 신호 대기 |
| v1 | breakout_8 + reversion_12 | 9935.83 | -64.17 | sell /  / breakout_8 + reversion_12: prior completed bar target 0%; next bar open simulation |
| v1 | breakout_8 AND volume_26 | 10000.00 | 0.00 | 대기 /  / 새 신호 대기 |
| v1 | breakout_8 + volume_26 | 9924.50 | -75.50 | sell /  / breakout_8 + volume_26: prior completed bar target 0%; next bar open simulation |
| v1 | reversion_12 AND volume_26 | 9965.65 | -34.35 | sell /  / reversion_12 AND volume_26: prior completed bar target 0%; next bar open simulation |
| v1 | reversion_12 + volume_26 | 9940.10 | -59.90 | sell /  / reversion_12 + volume_26: prior completed bar target 0%; next bar open simulation |
| v1 | ema_12_26 | 9876.07 | -123.93 | sell /  / EMA12 > EMA26; 조건 미충족; EMA12=520.874, EMA26=520.918 |
| v1 | macd_12_26_9 | 9941.64 | -58.36 | sell /  / MACD > 신호선 그리고 MACD > 0; 조건 미충족; MACD=1.23542, signal9=1.25143 |
| v1 | rsi_14_recovery | 10000.00 | 0.00 | 대기 /  / 새 신호 대기 |
| v1 | bollinger_20_reentry | 9978.51 | -21.49 | sell /  / 직전 종가 < 직전 하단밴드, 현재 하단밴드 <= 종가 <= SMA20 (한 봉 목표); 조건 미충족; close=519.823, lower20=518.355, SMA20=521.612, previous_lower20=518.548 |
| v1 | donchian_20 | 9940.12 | -59.88 | sell /  / 종가 > 현재 봉을 제외한 직전 20봉 최고가; 조건 미충족; close=522.89, prior_high20=525.09 |
| v1 | atr_14_breakout | 9972.44 | -27.56 | sell /  / 종가 > 직전 종가 + 직전 ATR14 그리고 종가 > EMA26; 조건 미충족; close=524.65, threshold=524.777, prior_ATR14=0.84688, EMA26=520.429 |
| v1 | session_vwap | 9960.84 | -39.16 | sell /  / 종가 > 뉴욕 거래일별 누적 전형가격 VWAP; 조건 미충족; close=522.89, session_VWAP=523.72, session_volume=975370 |
| v1 | obv_20 | 9924.53 | -75.47 | sell /  / OBV > OBV의 SMA20 그리고 종가 > EMA26; 조건 미충족; OBV=-5.35236e+06, OBV_SMA20=-5.09617e+06, close=522.08, EMA26=521.373 |
| v1 | stochastic_14_3_recovery | 9910.39 | -89.61 | sell /  / 직전 %K14 < 20에서 %K14가 %D3 상향 돌파 (한 봉 목표); 조건 미충족; K14=34.5537, D3=16.5437, previous_K14=12.4567, previous_D3=7.69976 |
| v1 | mfi_14_recovery | 10000.00 | 0.00 | 대기 /  / 새 신호 대기 |
| v1 | adx_14_trend | 9882.74 | -117.26 | sell /  / Wilder ADX14 >= 25 그리고 +DI14 > -DI14; 조건 미충족; ADX14=30.2264, plus_DI14=23.4608, minus_DI14=27.9688 |
| v1 | aroon_25_trend | 9928.27 | -71.73 | sell /  / Aroon25 Up > 70 그리고 Down < 30 (동률이면 최신 극값); 조건 미충족; Aroon_up=68, Aroon_down=4 |
| v1 | cci_20_momentum | 9954.56 | -45.44 | sell /  / CCI20 > 100 (전형가격·평균절대편차); 조건 미충족; CCI20=83.6046 |
| v1 | williams_14_recovery | 9958.52 | -41.48 | buy /  / 직전 Williams %R14 < -80, 현재 >= -80 (한 봉 목표); 조건 충족; Williams_R14=-65.4463, previous_R14=-87.5433 |
| v1 | cmf_20_accumulation | 9927.80 | -72.20 | sell /  / Chaikin Money Flow20 > 0.1; 조건 미충족; CMF20=0.0502896, volume20=2.48879e+06 |
| v1 | chaikin_3_10 | 9926.34 | -73.66 | sell /  / ADL의 EMA3 - EMA10 > 0 그리고 종가 > EMA26; 조건 미충족; Chaikin3_10=-14655, ADL=-1.49709e+07, close=522.196, EMA26=521.317 |
| v1 | roc_10_momentum | 10000.00 | 0.00 | 대기 /  / 새 신호 대기 |
| v1 | trix_15_trend | 9928.27 | -71.73 | sell /  / 15봉 삼중 EMA의 1봉 변화율 TRIX > 0 그리고 종가 > EMA26; 조건 미충족; TRIX15_percent=0.0322153, close=521.26, EMA26=521.365 |
| v1 | keltner_20_breakout | 9940.12 | -59.88 | sell /  / 종가 > EMA20 + 2 x Wilder ATR14; 조건 미충족; close=522.89, upper_Keltner=523.089, EMA20=521.145, ATR14=0.971947 |
| v1 | opening_range_30m | 9980.84 | -19.16 | sell /  / 뉴욕 09:30·09:45 두 완료 봉 최고가를 10:00 이후 종가가 돌파; 자료 부족·변동폭 또는 거래량 없음: 대기; close=523.93 |
| v2 | cash | 10000.00 | 0.00 | 대기 /  / 새 신호 대기 |
| v2 | buy_hold | 10020.97 | 20.97 | buy / partial / 직전 완료 봉 목표 비중 100%; 다음 봉 시가 가정 |
| v2 | trend_8_26 | 9839.12 | -160.88 | sell / filled / 직전 완료 봉 목표 비중 0%; 다음 봉 시가 가정 |
| v2 | momentum_26 | 9952.08 | -47.92 | sell / filled / 직전 완료 봉 목표 비중 0%; 다음 봉 시가 가정 |
| v2 | breakout_8 | 9466.63 | -533.37 | sell / filled / 직전 완료 봉 목표 비중 0%; 다음 봉 시가 가정 |
| v2 | reversion_12 | 9629.77 | -370.23 | sell / filled / 직전 완료 봉 목표 비중 0%; 다음 봉 시가 가정 |
| v2 | volume_26 | 9625.87 | -374.13 | sell / filled / 직전 완료 봉 목표 비중 0%; 다음 봉 시가 가정 |
| v2 | trend_8_26 AND momentum_26 | 9947.46 | -52.54 | sell / filled / 직전 완료 봉 목표 비중 0%; 다음 봉 시가 가정 |
| v2 | trend_8_26 + momentum_26 | 9895.51 | -104.49 | sell / filled / 직전 완료 봉 목표 비중 0%; 다음 봉 시가 가정 |
| v2 | trend_8_26 AND breakout_8 | 9626.81 | -373.19 | sell / filled / 직전 완료 봉 목표 비중 0%; 다음 봉 시가 가정 |
| v2 | trend_8_26 + breakout_8 | 9651.15 | -348.85 | sell / filled / 직전 완료 봉 목표 비중 0%; 다음 봉 시가 가정 |
| v2 | trend_8_26 AND reversion_12 | 9746.03 | -253.97 | sell / filled / 직전 완료 봉 목표 비중 0%; 다음 봉 시가 가정 |
| v2 | trend_8_26 + reversion_12 | 9733.59 | -266.41 | sell / filled / 직전 완료 봉 목표 비중 0%; 다음 봉 시가 가정 |
| v2 | trend_8_26 AND volume_26 | 9800.82 | -199.18 | sell / filled / 직전 완료 봉 목표 비중 0%; 다음 봉 시가 가정 |
| v2 | trend_8_26 + volume_26 | 9752.26 | -247.74 | sell / filled / 직전 완료 봉 목표 비중 0%; 다음 봉 시가 가정 |
| v2 | momentum_26 AND breakout_8 | 9615.85 | -384.15 | sell / filled / 직전 완료 봉 목표 비중 0%; 다음 봉 시가 가정 |
| v2 | momentum_26 + breakout_8 | 9706.46 | -293.54 | sell / filled / 직전 완료 봉 목표 비중 0%; 다음 봉 시가 가정 |
| v2 | momentum_26 AND reversion_12 | 9895.03 | -104.97 | sell / filled / 직전 완료 봉 목표 비중 0%; 다음 봉 시가 가정 |
| v2 | momentum_26 + reversion_12 | 9789.37 | -210.63 | sell / filled / 직전 완료 봉 목표 비중 0%; 다음 봉 시가 가정 |
| v2 | momentum_26 AND volume_26 | 9733.77 | -266.23 | sell / filled / 직전 완료 봉 목표 비중 0%; 다음 봉 시가 가정 |
| v2 | momentum_26 + volume_26 | 9828.84 | -171.16 | sell / filled / 직전 완료 봉 목표 비중 0%; 다음 봉 시가 가정 |
| v2 | breakout_8 AND reversion_12 | 10000.00 | 0.00 | 대기 /  / 새 신호 대기 |
| v2 | breakout_8 + reversion_12 | 9547.40 | -452.60 | sell / filled / 직전 완료 봉 목표 비중 0%; 다음 봉 시가 가정 |
| v2 | breakout_8 AND volume_26 | 9796.56 | -203.44 | sell / filled / 직전 완료 봉 목표 비중 0%; 다음 봉 시가 가정 |
| v2 | breakout_8 + volume_26 | 9545.74 | -454.26 | sell / filled / 직전 완료 봉 목표 비중 0%; 다음 봉 시가 가정 |
| v2 | reversion_12 AND volume_26 | 9963.66 | -36.34 | sell / filled / 직전 완료 봉 목표 비중 0%; 다음 봉 시가 가정 |
| v2 | reversion_12 + volume_26 | 9647.77 | -352.23 | sell / filled / 직전 완료 봉 목표 비중 0%; 다음 봉 시가 가정 |
| v2 | ema_12_26 | 9874.10 | -125.90 | sell / filled / EMA12 > EMA26; 조건 미충족; EMA12=520.874, EMA26=520.918; 직전 완료 봉 목표를 다음 봉 시가에 모의 적용 |
| v2 | macd_12_26_9 | 9939.65 | -60.35 | sell / filled / MACD > 신호선 그리고 MACD > 0; 조건 미충족; MACD=1.23542, signal9=1.25143; 직전 완료 봉 목표를 다음 봉 시가에 모의 적용 |
| v2 | rsi_14_recovery | 10000.00 | 0.00 | 대기 /  / 새 신호 대기 |
| v2 | bollinger_20_reentry | 9976.52 | -23.48 | sell / filled / 직전 종가 < 직전 하단밴드, 현재 하단밴드 <= 종가 <= SMA20 (한 봉 목표); 조건 미충족; close=519.823, lower20=518.355, SMA20=521.612, previous_lower20=518.548; 직전 완료 봉 목표를 다음 봉 시가에 모의 적용 |
| v2 | donchian_20 | 9938.13 | -61.87 | sell / filled / 종가 > 현재 봉을 제외한 직전 20봉 최고가; 조건 미충족; close=522.89, prior_high20=525.09; 직전 완료 봉 목표를 다음 봉 시가에 모의 적용 |
| v2 | atr_14_breakout | 9970.44 | -29.56 | sell / filled / 종가 > 직전 종가 + 직전 ATR14 그리고 종가 > EMA26; 조건 미충족; close=524.65, threshold=524.777, prior_ATR14=0.84688, EMA26=520.429; 직전 완료 봉 목표를 다음 봉 시가에 모의 적용 |
| v2 | session_vwap | 9958.85 | -41.15 | sell / filled / 종가 > 뉴욕 거래일별 누적 전형가격 VWAP; 조건 미충족; close=522.89, session_VWAP=523.72, session_volume=975370; 직전 완료 봉 목표를 다음 봉 시가에 모의 적용 |
| v2 | obv_20 | 9922.55 | -77.45 | sell / filled / OBV > OBV의 SMA20 그리고 종가 > EMA26; 조건 미충족; OBV=-5.35236e+06, OBV_SMA20=-5.09617e+06, close=522.08, EMA26=521.373; 직전 완료 봉 목표를 다음 봉 시가에 모의 적용 |
| v2 | stochastic_14_3_recovery | 9906.42 | -93.58 | sell / filled / 직전 %K14 < 20에서 %K14가 %D3 상향 돌파 (한 봉 목표); 조건 미충족; K14=34.5537, D3=16.5437, previous_K14=12.4567, previous_D3=7.69976; 직전 완료 봉 목표를 다음 봉 시가에 모의 적용 |
| v2 | mfi_14_recovery | 10000.00 | 0.00 | 대기 /  / 새 신호 대기 |
| v2 | adx_14_trend | 9878.79 | -121.21 | sell / filled / Wilder ADX14 >= 25 그리고 +DI14 > -DI14; 조건 미충족; ADX14=30.2264, plus_DI14=23.4608, minus_DI14=27.9688; 직전 완료 봉 목표를 다음 봉 시가에 모의 적용 |
| v2 | aroon_25_trend | 9926.28 | -73.72 | sell / filled / Aroon25 Up > 70 그리고 Down < 30 (동률이면 최신 극값); 조건 미충족; Aroon_up=68, Aroon_down=4; 직전 완료 봉 목표를 다음 봉 시가에 모의 적용 |
| v2 | cci_20_momentum | 9952.57 | -47.43 | sell / filled / CCI20 > 100 (전형가격·평균절대편차); 조건 미충족; CCI20=83.6046; 직전 완료 봉 목표를 다음 봉 시가에 모의 적용 |
| v2 | williams_14_recovery | 9957.53 | -42.47 | buy / partial / 직전 Williams %R14 < -80, 현재 >= -80 (한 봉 목표); 조건 충족; Williams_R14=-65.4463, previous_R14=-87.5433; 직전 완료 봉 목표를 다음 봉 시가에 모의 적용 |
| v2 | cmf_20_accumulation | 9925.82 | -74.18 | sell / filled / Chaikin Money Flow20 > 0.1; 조건 미충족; CMF20=0.0502896, volume20=2.48879e+06; 직전 완료 봉 목표를 다음 봉 시가에 모의 적용 |
| v2 | chaikin_3_10 | 9924.35 | -75.65 | sell / filled / ADL의 EMA3 - EMA10 > 0 그리고 종가 > EMA26; 조건 미충족; Chaikin3_10=-14655, ADL=-1.49709e+07, close=522.196, EMA26=521.317; 직전 완료 봉 목표를 다음 봉 시가에 모의 적용 |
| v2 | roc_10_momentum | 10000.00 | 0.00 | 대기 /  / 새 신호 대기 |
| v2 | trix_15_trend | 9926.28 | -73.72 | sell / filled / 15봉 삼중 EMA의 1봉 변화율 TRIX > 0 그리고 종가 > EMA26; 조건 미충족; TRIX15_percent=0.0322153, close=521.26, EMA26=521.365; 직전 완료 봉 목표를 다음 봉 시가에 모의 적용 |
| v2 | keltner_20_breakout | 9938.13 | -61.87 | sell / filled / 종가 > EMA20 + 2 x Wilder ATR14; 조건 미충족; close=522.89, upper_Keltner=523.089, EMA20=521.145, ATR14=0.971947; 직전 완료 봉 목표를 다음 봉 시가에 모의 적용 |
| v2 | opening_range_30m | 9978.85 | -21.15 | sell / filled / 뉴욕 09:30·09:45 두 완료 봉 최고가를 10:00 이후 종가가 돌파; 자료 부족·변동폭 또는 거래량 없음: 대기; close=523.93; 직전 완료 봉 목표를 다음 봉 시가에 모의 적용 |

### 같은 기간의 비용·노출 비교 (사후 연구)

| 전략 | 비용 전 | 비용 후 | 100% 보유 | 같은 평균 노출 보유 | 평균 노출 |
|---|---:|---:|---:|---:|---:|
| cash | 0.00% | 0.00% | 0.41% | 0.00% | 0.00% |
| buy_hold | 0.84% | 0.41% | 0.41% | 0.41% | 100.00% |
| trend_8_26 | 1.41% | -3.17% | 0.41% | 0.23% | 55.24% |
| momentum_26 | 0.13% | -3.99% | 0.41% | 0.21% | 51.31% |
| breakout_8 | 0.57% | -16.40% | 0.41% | 0.10% | 23.04% |
| reversion_12 | -1.64% | -9.94% | 0.41% | 0.11% | 26.44% |
| volume_26 | -1.02% | -11.63% | 0.41% | 0.05% | 11.26% |
| trend_8_26 AND momentum_26 | 1.60% | -2.58% | 0.41% | 0.19% | 45.55% |
| trend_8_26 + momentum_26 | 0.77% | -3.58% | 0.41% | 0.22% | 53.27% |
| trend_8_26 AND breakout_8 | 1.14% | -10.84% | 0.41% | 0.06% | 14.92% |
| trend_8_26 + breakout_8 | 0.99% | -9.84% | 0.41% | 0.16% | 39.14% |
| trend_8_26 AND reversion_12 | 0.13% | -5.19% | 0.41% | 0.03% | 7.33% |
| trend_8_26 + reversion_12 | -0.12% | -6.23% | 0.41% | 0.17% | 40.84% |
| trend_8_26 AND volume_26 | 0.48% | -4.86% | 0.41% | 0.02% | 5.24% |
| trend_8_26 + volume_26 | 0.19% | -7.31% | 0.41% | 0.14% | 33.25% |
| momentum_26 AND breakout_8 | 0.34% | -11.17% | 0.41% | 0.06% | 15.18% |
| momentum_26 + breakout_8 | 0.35% | -10.22% | 0.41% | 0.15% | 37.18% |
| momentum_26 AND reversion_12 | -0.37% | -4.47% | 0.41% | 0.03% | 6.54% |
| momentum_26 + reversion_12 | -0.75% | -6.24% | 0.41% | 0.16% | 38.88% |
| momentum_26 AND volume_26 | -0.49% | -5.77% | 0.41% | 0.02% | 4.71% |
| momentum_26 + volume_26 | -0.44% | -7.12% | 0.41% | 0.13% | 31.29% |
| breakout_8 AND reversion_12 | 0.00% | 0.00% | 0.41% | 0.00% | 0.00% |
| breakout_8 + reversion_12 | -0.54% | -12.88% | 0.41% | 0.10% | 24.75% |
| breakout_8 AND volume_26 | -0.87% | -4.55% | 0.41% | 0.01% | 3.14% |
| breakout_8 + volume_26 | -0.23% | -13.33% | 0.41% | 0.07% | 17.15% |
| reversion_12 AND volume_26 | -0.15% | -5.45% | 0.41% | 0.02% | 4.19% |
| reversion_12 + volume_26 | -1.33% | -10.61% | 0.41% | 0.08% | 18.85% |
| ema_12_26 | 0.03% | -2.46% | 0.41% | 0.21% | 50.26% |
| macd_12_26_9 | 1.65% | -1.30% | 0.41% | 0.11% | 27.49% |
| rsi_14_recovery | 0.01% | -2.07% | 0.41% | 0.01% | 1.31% |
| bollinger_20_reentry | -0.07% | -5.38% | 0.41% | 0.01% | 3.40% |
| donchian_20 | 0.36% | -5.77% | 0.41% | 0.03% | 8.12% |
| atr_14_breakout | -1.05% | -8.25% | 0.41% | 0.02% | 5.50% |
| session_vwap | 1.64% | -6.15% | 0.41% | 0.20% | 48.95% |
| obv_20 | 0.51% | -7.98% | 0.41% | 0.18% | 42.67% |
| stochastic_14_3_recovery | 0.69% | -11.98% | 0.41% | 0.03% | 8.38% |
| mfi_14_recovery | -0.06% | -2.95% | 0.41% | 0.01% | 1.83% |
| adx_14_trend | -0.10% | -4.61% | 0.41% | 0.15% | 35.86% |
| aroon_25_trend | 0.77% | -2.56% | 0.41% | 0.11% | 25.92% |
| cci_20_momentum | 0.66% | -5.09% | 0.41% | 0.10% | 23.82% |
| williams_14_recovery | 0.79% | -7.33% | 0.41% | 0.02% | 5.24% |
| cmf_20_accumulation | 1.19% | -5.79% | 0.41% | 0.12% | 30.10% |
| chaikin_3_10 | 1.71% | -8.04% | 0.41% | 0.17% | 41.36% |
| roc_10_momentum | 0.15% | -0.27% | 0.41% | 0.01% | 1.31% |
| trix_15_trend | 0.27% | -3.45% | 0.41% | 0.17% | 42.15% |
| keltner_20_breakout | 0.33% | -5.79% | 0.41% | 0.07% | 16.75% |
| opening_range_30m | 1.42% | -4.77% | 0.41% | 0.09% | 20.68% |

동일 구간·초기 자금, 종료 시 청산 비용 포함. 노출 맞춤은 사후 설명용이며 v2 실제 계좌 성과가 아닙니다.
[낙폭 분해·비용 영향·전체 구간](DIA/comparison.json)

[v1 전체 기록](DIA/accounts.json) · [v2 전체 기록](DIA/accounts-v2.json)

## MSFT 계좌

| 모델 | 전략 | 평가액 USD | 손익 USD | 최근 매매·이유 |
|---|---|---:|---:|---|
| v1 | cash | 10000.00 | 0.00 | 대기 /  / 새 신호 대기 |
| v1 | buy_hold | 9720.32 | -279.68 | buy /  / buy_hold: prior completed bar target 100%; next bar open simulation |
| v1 | trend_8_26 | 9853.68 | -146.32 | sell /  / trend_8_26: prior completed bar target 0%; next bar open simulation |
| v1 | momentum_26 | 9839.32 | -160.68 | sell /  / momentum_26: prior completed bar target 0%; next bar open simulation |
| v1 | breakout_8 | 10000.00 | 0.00 | 대기 /  / 새 신호 대기 |
| v1 | reversion_12 | 9784.89 | -215.11 | sell /  / reversion_12: prior completed bar target 0%; next bar open simulation |
| v1 | volume_26 | 9938.00 | -62.00 | sell /  / volume_26: prior completed bar target 0%; next bar open simulation |
| v1 | trend_8_26 AND momentum_26 | 9853.68 | -146.32 | sell /  / trend_8_26 AND momentum_26: prior completed bar target 0%; next bar open simulation |
| v1 | trend_8_26 + momentum_26 | 9846.52 | -153.48 | sell /  / trend_8_26 + momentum_26: prior completed bar target 0%; next bar open simulation |
| v1 | trend_8_26 AND breakout_8 | 10000.00 | 0.00 | 대기 /  / 새 신호 대기 |
| v1 | trend_8_26 + breakout_8 | 9926.58 | -73.42 | sell /  / trend_8_26 + breakout_8: prior completed bar target 0%; next bar open simulation |
| v1 | trend_8_26 AND reversion_12 | 9923.56 | -76.44 | sell /  / trend_8_26 AND reversion_12: prior completed bar target 0%; next bar open simulation |
| v1 | trend_8_26 + reversion_12 | 9819.20 | -180.80 | sell /  / trend_8_26 + reversion_12: prior completed bar target 0%; next bar open simulation |
| v1 | trend_8_26 AND volume_26 | 10000.00 | 0.00 | 대기 /  / 새 신호 대기 |
| v1 | trend_8_26 + volume_26 | 9895.73 | -104.27 | sell /  / trend_8_26 + volume_26: prior completed bar target 0%; next bar open simulation |
| v1 | momentum_26 AND breakout_8 | 10000.00 | 0.00 | 대기 /  / 새 신호 대기 |
| v1 | momentum_26 + breakout_8 | 9919.33 | -80.67 | sell /  / momentum_26 + breakout_8: prior completed bar target 0%; next bar open simulation |
| v1 | momentum_26 AND reversion_12 | 9909.10 | -90.90 | sell /  / momentum_26 AND reversion_12: prior completed bar target 0%; next bar open simulation |
| v1 | momentum_26 + reversion_12 | 9812.04 | -187.96 | sell /  / momentum_26 + reversion_12: prior completed bar target 0%; next bar open simulation |
| v1 | momentum_26 AND volume_26 | 10000.00 | 0.00 | 대기 /  / 새 신호 대기 |
| v1 | momentum_26 + volume_26 | 9888.51 | -111.49 | sell /  / momentum_26 + volume_26: prior completed bar target 0%; next bar open simulation |
| v1 | breakout_8 AND reversion_12 | 10000.00 | 0.00 | 대기 /  / 새 신호 대기 |
| v1 | breakout_8 + reversion_12 | 9891.81 | -108.19 | sell /  / breakout_8 + reversion_12: prior completed bar target 0%; next bar open simulation |
| v1 | breakout_8 AND volume_26 | 10000.00 | 0.00 | 대기 /  / 새 신호 대기 |
| v1 | breakout_8 + volume_26 | 9968.93 | -31.07 | sell /  / breakout_8 + volume_26: prior completed bar target 0%; next bar open simulation |
| v1 | reversion_12 AND volume_26 | 9938.00 | -62.00 | sell /  / reversion_12 AND volume_26: prior completed bar target 0%; next bar open simulation |
| v1 | reversion_12 + volume_26 | 9861.10 | -138.90 | sell /  / reversion_12 + volume_26: prior completed bar target 0%; next bar open simulation |
| v1 | ema_12_26 | 9853.68 | -146.32 | sell /  / EMA12 > EMA26; 조건 미충족; EMA12=538.192, EMA26=538.342 |
| v1 | macd_12_26_9 | 9889.94 | -110.06 | sell /  / MACD > 신호선 그리고 MACD > 0; 조건 미충족; MACD=0.536125, signal9=0.712825 |
| v1 | rsi_14_recovery | 9964.52 | -35.48 | buy /  / 직전 RSI14 < 30, 현재 RSI14 >= 30 (한 봉 목표); 조건 충족; RSI14=33.2992, previous_RSI14=22.8346 |
| v1 | bollinger_20_reentry | 9885.00 | -115.00 | sell /  / 직전 종가 < 직전 하단밴드, 현재 하단밴드 <= 종가 <= SMA20 (한 봉 목표); 조건 미충족; close=529.125, lower20=527.516, SMA20=535.918, previous_lower20=528.497 |
| v1 | donchian_20 | 10000.00 | 0.00 | 대기 /  / 새 신호 대기 |
| v1 | atr_14_breakout | 10000.00 | 0.00 | 대기 /  / 새 신호 대기 |
| v1 | session_vwap | 9889.94 | -110.06 | sell /  / 종가 > 뉴욕 거래일별 누적 전형가격 VWAP; 조건 미충족; close=537.34, session_VWAP=538.663, session_volume=3.36828e+06 |
| v1 | obv_20 | 9889.94 | -110.06 | sell /  / OBV > OBV의 SMA20 그리고 종가 > EMA26; 조건 미충족; OBV=1.44955e+08, OBV_SMA20=1.34631e+08, close=537.34, EMA26=538.834 |
| v1 | stochastic_14_3_recovery | 9792.37 | -207.63 | sell /  / 직전 %K14 < 20에서 %K14가 %D3 상향 돌파 (한 봉 목표); 조건 미충족; K14=25.4855, D3=14.0848, previous_K14=10.0077, previous_D3=7.52857 |
| v1 | mfi_14_recovery | 10000.00 | 0.00 | 대기 /  / 새 신호 대기 |
| v1 | adx_14_trend | 9889.94 | -110.06 | sell /  / Wilder ADX14 >= 25 그리고 +DI14 > -DI14; 조건 미충족; ADX14=30.6145, plus_DI14=15.7198, minus_DI14=27.4451 |
| v1 | aroon_25_trend | 9867.67 | -132.33 | sell /  / Aroon25 Up > 70 그리고 Down < 30 (동률이면 최신 극값); 조건 미충족; Aroon_up=84, Aroon_down=100 |
| v1 | cci_20_momentum | 10000.00 | 0.00 | 대기 /  / 새 신호 대기 |
| v1 | williams_14_recovery | 9896.23 | -103.77 | buy /  / 직전 Williams %R14 < -80, 현재 >= -80 (한 봉 목표); 조건 충족; Williams_R14=-74.5145, previous_R14=-89.9923 |
| v1 | cmf_20_accumulation | 9765.23 | -234.77 | sell /  / Chaikin Money Flow20 > 0.1; 조건 미충족; CMF20=-0.0001648, volume20=6.0129e+07 |
| v1 | chaikin_3_10 | 9889.94 | -110.06 | sell /  / ADL의 EMA3 - EMA10 > 0 그리고 종가 > EMA26; 조건 미충족; Chaikin3_10=3.90601e+06, ADL=1.2345e+08, close=537.34, EMA26=538.834 |
| v1 | roc_10_momentum | 10000.00 | 0.00 | 대기 /  / 새 신호 대기 |
| v1 | trix_15_trend | 9889.94 | -110.06 | sell /  / 15봉 삼중 EMA의 1봉 변화율 TRIX > 0 그리고 종가 > EMA26; 조건 미충족; TRIX15_percent=0.0221169, close=537.34, EMA26=538.834 |
| v1 | keltner_20_breakout | 10000.00 | 0.00 | 대기 /  / 새 신호 대기 |
| v1 | opening_range_30m | 9889.94 | -110.06 | sell /  / 뉴욕 09:30·09:45 두 완료 봉 최고가를 10:00 이후 종가가 돌파; 자료 부족·변동폭 또는 거래량 없음: 대기; close=537.34 |
| v2 | cash | 10000.00 | 0.00 | 대기 /  / 새 신호 대기 |
| v2 | buy_hold | 9773.36 | -226.64 | buy / partial / 직전 완료 봉 목표 비중 100%; 다음 봉 시가 가정 |
| v2 | trend_8_26 | 9790.17 | -209.83 | sell / filled / 직전 완료 봉 목표 비중 0%; 다음 봉 시가 가정 |
| v2 | momentum_26 | 9886.18 | -113.82 | sell / filled / 직전 완료 봉 목표 비중 0%; 다음 봉 시가 가정 |
| v2 | breakout_8 | 9799.48 | -200.52 | sell / filled / 직전 완료 봉 목표 비중 0%; 다음 봉 시가 가정 |
| v2 | reversion_12 | 9409.83 | -590.17 | sell / filled / 직전 완료 봉 목표 비중 0%; 다음 봉 시가 가정 |
| v2 | volume_26 | 9626.55 | -373.45 | sell / filled / 직전 완료 봉 목표 비중 0%; 다음 봉 시가 가정 |
| v2 | trend_8_26 AND momentum_26 | 9751.13 | -248.87 | sell / filled / 직전 완료 봉 목표 비중 0%; 다음 봉 시가 가정 |
| v2 | trend_8_26 + momentum_26 | 9838.34 | -161.66 | sell / filled / 직전 완료 봉 목표 비중 0%; 다음 봉 시가 가정 |
| v2 | trend_8_26 AND breakout_8 | 9639.29 | -360.71 | sell / filled / 직전 완료 봉 목표 비중 0%; 다음 봉 시가 가정 |
| v2 | trend_8_26 + breakout_8 | 9815.63 | -184.37 | sell / filled / 직전 완료 봉 목표 비중 0%; 다음 봉 시가 가정 |
| v2 | trend_8_26 AND reversion_12 | 9822.46 | -177.54 | sell / filled / 직전 완료 봉 목표 비중 0%; 다음 봉 시가 가정 |
| v2 | trend_8_26 + reversion_12 | 9597.76 | -402.24 | sell / filled / 직전 완료 봉 목표 비중 0%; 다음 봉 시가 가정 |
| v2 | trend_8_26 AND volume_26 | 9948.66 | -51.34 | sell / filled / 직전 완료 봉 목표 비중 0%; 다음 봉 시가 가정 |
| v2 | trend_8_26 + volume_26 | 9728.21 | -271.79 | sell / filled / 직전 완료 봉 목표 비중 0%; 다음 봉 시가 가정 |
| v2 | momentum_26 AND breakout_8 | 9794.38 | -205.62 | sell / filled / 직전 완료 봉 목표 비중 0%; 다음 봉 시가 가정 |
| v2 | momentum_26 + breakout_8 | 9842.81 | -157.19 | sell / filled / 직전 완료 봉 목표 비중 0%; 다음 봉 시가 가정 |
| v2 | momentum_26 AND reversion_12 | 9735.61 | -264.39 | sell / filled / 직전 완료 봉 목표 비중 0%; 다음 봉 시가 가정 |
| v2 | momentum_26 + reversion_12 | 9644.83 | -355.17 | sell / filled / 직전 완료 봉 목표 비중 0%; 다음 봉 시가 가정 |
| v2 | momentum_26 AND volume_26 | 9871.26 | -128.74 | sell / filled / 직전 완료 봉 목표 비중 0%; 다음 봉 시가 가정 |
| v2 | momentum_26 + volume_26 | 9775.92 | -224.08 | sell / filled / 직전 완료 봉 목표 비중 0%; 다음 봉 시가 가정 |
| v2 | breakout_8 AND reversion_12 | 10000.00 | 0.00 | 대기 /  / 새 신호 대기 |
| v2 | breakout_8 + reversion_12 | 9622.61 | -377.39 | sell / filled / 직전 완료 봉 목표 비중 0%; 다음 봉 시가 가정 |
| v2 | breakout_8 AND volume_26 | 9938.59 | -61.41 | sell / filled / 직전 완료 봉 목표 비중 0%; 다음 봉 시가 가정 |
| v2 | breakout_8 + volume_26 | 9733.07 | -266.93 | sell / filled / 직전 완료 봉 목표 비중 0%; 다음 봉 시가 가정 |
| v2 | reversion_12 AND volume_26 | 9699.57 | -300.43 | sell / filled / 직전 완료 봉 목표 비중 0%; 다음 봉 시가 가정 |
| v2 | reversion_12 + volume_26 | 9517.37 | -482.63 | sell / filled / 직전 완료 봉 목표 비중 0%; 다음 봉 시가 가정 |
| v2 | ema_12_26 | 9851.71 | -148.29 | sell / filled / EMA12 > EMA26; 조건 미충족; EMA12=538.192, EMA26=538.342; 직전 완료 봉 목표를 다음 봉 시가에 모의 적용 |
| v2 | macd_12_26_9 | 9887.97 | -112.03 | sell / filled / MACD > 신호선 그리고 MACD > 0; 조건 미충족; MACD=0.536125, signal9=0.712825; 직전 완료 봉 목표를 다음 봉 시가에 모의 적용 |
| v2 | rsi_14_recovery | 9963.53 | -36.47 | buy / partial / 직전 RSI14 < 30, 현재 RSI14 >= 30 (한 봉 목표); 조건 충족; RSI14=33.2992, previous_RSI14=22.8346; 직전 완료 봉 목표를 다음 봉 시가에 모의 적용 |
| v2 | bollinger_20_reentry | 9881.05 | -118.95 | sell / filled / 직전 종가 < 직전 하단밴드, 현재 하단밴드 <= 종가 <= SMA20 (한 봉 목표); 조건 미충족; close=529.125, lower20=527.516, SMA20=535.918, previous_lower20=528.497; 직전 완료 봉 목표를 다음 봉 시가에 모의 적용 |
| v2 | donchian_20 | 10000.00 | 0.00 | 대기 /  / 새 신호 대기 |
| v2 | atr_14_breakout | 10000.00 | 0.00 | 대기 /  / 새 신호 대기 |
| v2 | session_vwap | 9887.97 | -112.03 | sell / filled / 종가 > 뉴욕 거래일별 누적 전형가격 VWAP; 조건 미충족; close=537.34, session_VWAP=538.663, session_volume=3.36828e+06; 직전 완료 봉 목표를 다음 봉 시가에 모의 적용 |
| v2 | obv_20 | 9887.97 | -112.03 | sell / filled / OBV > OBV의 SMA20 그리고 종가 > EMA26; 조건 미충족; OBV=1.44955e+08, OBV_SMA20=1.34631e+08, close=537.34, EMA26=538.834; 직전 완료 봉 목표를 다음 봉 시가에 모의 적용 |
| v2 | stochastic_14_3_recovery | 9784.54 | -215.46 | sell / filled / 직전 %K14 < 20에서 %K14가 %D3 상향 돌파 (한 봉 목표); 조건 미충족; K14=25.4855, D3=14.0848, previous_K14=10.0077, previous_D3=7.52857; 직전 완료 봉 목표를 다음 봉 시가에 모의 적용 |
| v2 | mfi_14_recovery | 10000.00 | 0.00 | 대기 /  / 새 신호 대기 |
| v2 | adx_14_trend | 9887.97 | -112.03 | sell / filled / Wilder ADX14 >= 25 그리고 +DI14 > -DI14; 조건 미충족; ADX14=30.6145, plus_DI14=15.7198, minus_DI14=27.4451; 직전 완료 봉 목표를 다음 봉 시가에 모의 적용 |
| v2 | aroon_25_trend | 9865.70 | -134.30 | sell / filled / Aroon25 Up > 70 그리고 Down < 30 (동률이면 최신 극값); 조건 미충족; Aroon_up=84, Aroon_down=100; 직전 완료 봉 목표를 다음 봉 시가에 모의 적용 |
| v2 | cci_20_momentum | 10000.00 | 0.00 | 대기 /  / 새 신호 대기 |
| v2 | williams_14_recovery | 9893.27 | -106.73 | buy / partial / 직전 Williams %R14 < -80, 현재 >= -80 (한 봉 목표); 조건 충족; Williams_R14=-74.5145, previous_R14=-89.9923; 직전 완료 봉 목표를 다음 봉 시가에 모의 적용 |
| v2 | cmf_20_accumulation | 9763.27 | -236.73 | sell / filled / Chaikin Money Flow20 > 0.1; 조건 미충족; CMF20=-0.0001648, volume20=6.0129e+07; 직전 완료 봉 목표를 다음 봉 시가에 모의 적용 |
| v2 | chaikin_3_10 | 9887.97 | -112.03 | sell / filled / ADL의 EMA3 - EMA10 > 0 그리고 종가 > EMA26; 조건 미충족; Chaikin3_10=3.90601e+06, ADL=1.2345e+08, close=537.34, EMA26=538.834; 직전 완료 봉 목표를 다음 봉 시가에 모의 적용 |
| v2 | roc_10_momentum | 10000.00 | 0.00 | 대기 /  / 새 신호 대기 |
| v2 | trix_15_trend | 9887.97 | -112.03 | sell / filled / 15봉 삼중 EMA의 1봉 변화율 TRIX > 0 그리고 종가 > EMA26; 조건 미충족; TRIX15_percent=0.0221169, close=537.34, EMA26=538.834; 직전 완료 봉 목표를 다음 봉 시가에 모의 적용 |
| v2 | keltner_20_breakout | 10000.00 | 0.00 | 대기 /  / 새 신호 대기 |
| v2 | opening_range_30m | 9887.97 | -112.03 | sell / filled / 뉴욕 09:30·09:45 두 완료 봉 최고가를 10:00 이후 종가가 돌파; 자료 부족·변동폭 또는 거래량 없음: 대기; close=537.34; 직전 완료 봉 목표를 다음 봉 시가에 모의 적용 |

### 같은 기간의 비용·노출 비교 (사후 연구)

| 전략 | 비용 전 | 비용 후 | 100% 보유 | 같은 평균 노출 보유 | 평균 노출 |
|---|---:|---:|---:|---:|---:|
| cash | 0.00% | 0.00% | 3.83% | 0.00% | 0.00% |
| buy_hold | 4.26% | 3.83% | 3.83% | 3.83% | 100.00% |
| trend_8_26 | 0.78% | -2.96% | 3.83% | 2.11% | 56.02% |
| momentum_26 | 1.78% | -4.03% | 3.83% | 2.14% | 56.81% |
| breakout_8 | 5.09% | -8.89% | 3.83% | 0.73% | 19.63% |
| reversion_12 | -3.73% | -12.23% | 3.83% | 0.99% | 26.70% |
| volume_26 | 2.21% | -6.42% | 3.83% | 0.32% | 8.64% |
| trend_8_26 AND momentum_26 | 0.51% | -5.23% | 3.83% | 1.89% | 50.26% |
| trend_8_26 + momentum_26 | 1.28% | -3.49% | 3.83% | 2.12% | 56.42% |
| trend_8_26 AND breakout_8 | 0.68% | -8.98% | 3.83% | 0.46% | 12.57% |
| trend_8_26 + breakout_8 | 2.93% | -5.57% | 3.83% | 1.41% | 37.83% |
| trend_8_26 AND reversion_12 | -1.70% | -6.92% | 3.83% | 0.26% | 7.07% |
| trend_8_26 + reversion_12 | -1.49% | -7.33% | 3.83% | 1.55% | 41.37% |
| trend_8_26 AND volume_26 | 3.46% | 0.46% | 3.83% | 0.10% | 2.62% |
| trend_8_26 + volume_26 | 1.50% | -3.91% | 3.83% | 1.20% | 32.33% |
| momentum_26 AND breakout_8 | 2.61% | -7.61% | 3.83% | 0.47% | 12.83% |
| momentum_26 + breakout_8 | 3.43% | -5.90% | 3.83% | 1.43% | 38.23% |
| momentum_26 AND reversion_12 | -1.18% | -7.21% | 3.83% | 0.32% | 8.64% |
| momentum_26 + reversion_12 | -0.99% | -7.84% | 3.83% | 1.56% | 41.76% |
| momentum_26 AND volume_26 | 1.80% | -2.38% | 3.83% | 0.13% | 3.40% |
| momentum_26 + volume_26 | 2.01% | -4.03% | 3.83% | 1.22% | 32.73% |
| breakout_8 AND reversion_12 | 0.00% | 0.00% | 3.83% | 0.00% | 0.00% |
| breakout_8 + reversion_12 | 0.60% | -10.01% | 3.83% | 0.86% | 23.17% |
| breakout_8 AND volume_26 | 2.07% | -0.47% | 3.83% | 0.07% | 1.83% |
| breakout_8 + volume_26 | 3.65% | -6.69% | 3.83% | 0.52% | 14.14% |
| reversion_12 AND volume_26 | -2.48% | -6.49% | 3.83% | 0.14% | 3.93% |
| reversion_12 + volume_26 | -0.79% | -9.18% | 3.83% | 0.65% | 17.68% |
| ema_12_26 | 1.38% | -2.38% | 3.83% | 2.25% | 59.69% |
| macd_12_26_9 | 0.71% | -4.24% | 3.83% | 1.22% | 32.72% |
| rsi_14_recovery | -0.61% | -2.27% | 3.83% | 0.04% | 1.05% |
| bollinger_20_reentry | -0.52% | -3.81% | 3.83% | 0.08% | 2.09% |
| donchian_20 | 1.84% | -3.17% | 3.83% | 0.16% | 4.45% |
| atr_14_breakout | 1.50% | -3.89% | 3.83% | 0.13% | 3.66% |
| session_vwap | 4.97% | -3.08% | 3.83% | 1.69% | 45.03% |
| obv_20 | 4.17% | -4.62% | 3.83% | 1.92% | 51.05% |
| stochastic_14_3_recovery | -0.32% | -11.00% | 3.83% | 0.26% | 7.07% |
| mfi_14_recovery | 1.04% | -1.88% | 3.83% | 0.07% | 1.83% |
| adx_14_trend | 3.42% | 0.43% | 3.83% | 1.63% | 43.46% |
| aroon_25_trend | 0.23% | -4.29% | 3.83% | 0.76% | 20.42% |
| cci_20_momentum | 2.74% | -3.54% | 3.83% | 0.76% | 20.42% |
| williams_14_recovery | -0.44% | -9.61% | 3.83% | 0.22% | 6.02% |
| cmf_20_accumulation | 0.57% | -5.18% | 3.83% | 1.33% | 35.60% |
| chaikin_3_10 | 3.42% | -4.51% | 3.83% | 1.67% | 44.50% |
| roc_10_momentum | -0.20% | -4.30% | 3.83% | 0.52% | 14.14% |
| trix_15_trend | 0.50% | -3.64% | 3.83% | 1.72% | 45.81% |
| keltner_20_breakout | 1.12% | -3.85% | 3.83% | 0.49% | 13.35% |
| opening_range_30m | -2.08% | -6.89% | 3.83% | 0.87% | 23.56% |

동일 구간·초기 자금, 종료 시 청산 비용 포함. 노출 맞춤은 사후 설명용이며 v2 실제 계좌 성과가 아닙니다.
[낙폭 분해·비용 영향·전체 구간](MSFT/comparison.json)

[v1 전체 기록](MSFT/accounts.json) · [v2 전체 기록](MSFT/accounts-v2.json)

## JPM 계좌

| 모델 | 전략 | 평가액 USD | 손익 USD | 최근 매매·이유 |
|---|---|---:|---:|---|
| v1 | cash | 10000.00 | 0.00 | 대기 /  / 새 신호 대기 |
| v1 | buy_hold | 9924.83 | -75.17 | buy /  / buy_hold: prior completed bar target 100%; next bar open simulation |
| v1 | trend_8_26 | 9924.83 | -75.17 | buy /  / trend_8_26: prior completed bar target 100%; next bar open simulation |
| v1 | momentum_26 | 9924.83 | -75.17 | buy /  / momentum_26: prior completed bar target 100%; next bar open simulation |
| v1 | breakout_8 | 9915.55 | -84.45 | sell /  / breakout_8: prior completed bar target 0%; next bar open simulation |
| v1 | reversion_12 | 9919.55 | -80.45 | sell /  / reversion_12: prior completed bar target 0%; next bar open simulation |
| v1 | volume_26 | 10035.68 | 35.68 | sell /  / volume_26: prior completed bar target 0%; next bar open simulation |
| v1 | trend_8_26 AND momentum_26 | 9924.83 | -75.17 | buy /  / trend_8_26 AND momentum_26: prior completed bar target 100%; next bar open simulation |
| v1 | trend_8_26 + momentum_26 | 9924.83 | -75.17 | buy /  / trend_8_26 + momentum_26: prior completed bar target 100%; next bar open simulation |
| v1 | trend_8_26 AND breakout_8 | 9915.55 | -84.45 | sell /  / trend_8_26 AND breakout_8: prior completed bar target 0%; next bar open simulation |
| v1 | trend_8_26 + breakout_8 | 9920.26 | -79.74 | sell /  / trend_8_26 + breakout_8: prior completed bar target 50%; next bar open simulation |
| v1 | trend_8_26 AND reversion_12 | 9919.55 | -80.45 | sell /  / trend_8_26 AND reversion_12: prior completed bar target 0%; next bar open simulation |
| v1 | trend_8_26 + reversion_12 | 9922.20 | -77.80 | sell /  / trend_8_26 + reversion_12: prior completed bar target 50%; next bar open simulation |
| v1 | trend_8_26 AND volume_26 | 10035.68 | 35.68 | sell /  / trend_8_26 AND volume_26: prior completed bar target 0%; next bar open simulation |
| v1 | trend_8_26 + volume_26 | 9980.05 | -19.95 | sell /  / trend_8_26 + volume_26: prior completed bar target 50%; next bar open simulation |
| v1 | momentum_26 AND breakout_8 | 9915.55 | -84.45 | sell /  / momentum_26 AND breakout_8: prior completed bar target 0%; next bar open simulation |
| v1 | momentum_26 + breakout_8 | 9920.26 | -79.74 | sell /  / momentum_26 + breakout_8: prior completed bar target 50%; next bar open simulation |
| v1 | momentum_26 AND reversion_12 | 9919.55 | -80.45 | sell /  / momentum_26 AND reversion_12: prior completed bar target 0%; next bar open simulation |
| v1 | momentum_26 + reversion_12 | 9922.20 | -77.80 | sell /  / momentum_26 + reversion_12: prior completed bar target 50%; next bar open simulation |
| v1 | momentum_26 AND volume_26 | 10035.68 | 35.68 | sell /  / momentum_26 AND volume_26: prior completed bar target 0%; next bar open simulation |
| v1 | momentum_26 + volume_26 | 9980.05 | -19.95 | sell /  / momentum_26 + volume_26: prior completed bar target 50%; next bar open simulation |
| v1 | breakout_8 AND reversion_12 | 10000.00 | 0.00 | 대기 /  / 새 신호 대기 |
| v1 | breakout_8 + reversion_12 | 9917.58 | -82.42 | sell /  / breakout_8 + reversion_12: prior completed bar target 0%; next bar open simulation |
| v1 | breakout_8 AND volume_26 | 10035.68 | 35.68 | sell /  / breakout_8 AND volume_26: prior completed bar target 0%; next bar open simulation |
| v1 | breakout_8 + volume_26 | 9975.44 | -24.56 | sell /  / breakout_8 + volume_26: prior completed bar target 0%; next bar open simulation |
| v1 | reversion_12 AND volume_26 | 10000.00 | 0.00 | 대기 /  / 새 신호 대기 |
| v1 | reversion_12 + volume_26 | 9977.46 | -22.54 | sell /  / reversion_12 + volume_26: prior completed bar target 0%; next bar open simulation |
| v1 | ema_12_26 | 9924.83 | -75.17 | buy /  / EMA12 > EMA26; 조건 충족; EMA12=334.708, EMA26=334.451 |
| v1 | macd_12_26_9 | 9973.56 | -26.44 | sell /  / MACD > 신호선 그리고 MACD > 0; 조건 미충족; MACD=1.87003, signal9=1.96381 |
| v1 | rsi_14_recovery | 10000.00 | 0.00 | 대기 /  / 새 신호 대기 |
| v1 | bollinger_20_reentry | 10000.00 | 0.00 | 대기 /  / 새 신호 대기 |
| v1 | donchian_20 | 9872.30 | -127.70 | sell /  / 종가 > 현재 봉을 제외한 직전 20봉 최고가; 조건 미충족; close=343.037, prior_high20=344.4 |
| v1 | atr_14_breakout | 9886.92 | -113.08 | sell /  / 종가 > 직전 종가 + 직전 ATR14 그리고 종가 > EMA26; 조건 미충족; close=342.515, threshold=344.598, prior_ATR14=1.50332, EMA26=336.975 |
| v1 | session_vwap | 9936.81 | -63.19 | sell /  / 종가 > 뉴욕 거래일별 누적 전형가격 VWAP; 조건 미충족; close=342, session_VWAP=342.233, session_volume=3.25898e+06 |
| v1 | obv_20 | 10007.55 | 7.55 | sell /  / OBV > OBV의 SMA20 그리고 종가 > EMA26; 조건 미충족; OBV=-1.38544e+07, OBV_SMA20=-1.10099e+07, close=341.625, EMA26=338.807 |
| v1 | stochastic_14_3_recovery | 9973.76 | -26.24 | sell /  / 직전 %K14 < 20에서 %K14가 %D3 상향 돌파 (한 봉 목표); 조건 미충족; K14=21.5845, D3=12.4907, previous_K14=14.6076, previous_D3=9.68611 |
| v1 | mfi_14_recovery | 10000.00 | 0.00 | 대기 /  / 새 신호 대기 |
| v1 | adx_14_trend | 9806.96 | -193.04 | sell /  / Wilder ADX14 >= 25 그리고 +DI14 > -DI14; 조건 미충족; ADX14=30.1815, plus_DI14=27.5695, minus_DI14=29.9812 |
| v1 | aroon_25_trend | 9824.71 | -175.29 | sell /  / Aroon25 Up > 70 그리고 Down < 30 (동률이면 최신 극값); 조건 미충족; Aroon_up=68, Aroon_down=16 |
| v1 | cci_20_momentum | 10050.62 | 50.62 | sell /  / CCI20 > 100 (전형가격·평균절대편차); 조건 미충족; CCI20=93.5627 |
| v1 | williams_14_recovery | 9951.92 | -48.08 | buy /  / 직전 Williams %R14 < -80, 현재 >= -80 (한 봉 목표); 조건 충족; Williams_R14=-78.4155, previous_R14=-85.3924 |
| v1 | cmf_20_accumulation | 9932.16 | -67.84 | sell /  / Chaikin Money Flow20 > 0.1; 조건 미충족; CMF20=-0.14511, volume20=9.3038e+06 |
| v1 | chaikin_3_10 | 10007.55 | 7.55 | sell /  / ADL의 EMA3 - EMA10 > 0 그리고 종가 > EMA26; 조건 미충족; Chaikin3_10=-655976, ADL=-7.91325e+06, close=341.625, EMA26=338.807 |
| v1 | roc_10_momentum | 9913.84 | -86.16 | sell /  / 10봉 ROC > 1% 그리고 종가 > EMA26; 조건 미충족; ROC10_percent=-0.490038, close=340.901, EMA26=338.962 |
| v1 | trix_15_trend | 9875.74 | -124.26 | buy /  / 15봉 삼중 EMA의 1봉 변화율 TRIX > 0 그리고 종가 > EMA26; 조건 충족; TRIX15_percent=0.0635068, close=339.005, EMA26=338.985 |
| v1 | keltner_20_breakout | 9946.99 | -53.01 | sell /  / 종가 > EMA20 + 2 x Wilder ATR14; 조건 미충족; close=342, upper_Keltner=342.276, EMA20=339.397, ATR14=1.43933 |
| v1 | opening_range_30m | 9927.81 | -72.19 | sell /  / 뉴욕 09:30·09:45 두 완료 봉 최고가를 10:00 이후 종가가 돌파; 조건 미충족; close=343.037, opening_high=343.75 |
| v2 | cash | 10000.00 | 0.00 | 대기 /  / 새 신호 대기 |
| v2 | buy_hold | 10090.67 | 90.67 | buy / partial / 직전 완료 봉 목표 비중 100%; 다음 봉 시가 가정 |
| v2 | trend_8_26 | 9932.96 | -67.04 | buy / partial / 직전 완료 봉 목표 비중 100%; 다음 봉 시가 가정 |
| v2 | momentum_26 | 9433.20 | -566.80 | buy / partial / 직전 완료 봉 목표 비중 100%; 다음 봉 시가 가정 |
| v2 | breakout_8 | 9251.20 | -748.80 | sell / filled / 직전 완료 봉 목표 비중 0%; 다음 봉 시가 가정 |
| v2 | reversion_12 | 9909.61 | -90.39 | sell / filled / 직전 완료 봉 목표 비중 0%; 다음 봉 시가 가정 |
| v2 | volume_26 | 9859.79 | -140.21 | sell / filled / 직전 완료 봉 목표 비중 0%; 다음 봉 시가 가정 |
| v2 | trend_8_26 AND momentum_26 | 9892.20 | -107.80 | buy / partial / 직전 완료 봉 목표 비중 100%; 다음 봉 시가 가정 |
| v2 | trend_8_26 + momentum_26 | 9700.74 | -299.26 | buy / partial / 직전 완료 봉 목표 비중 100%; 다음 봉 시가 가정 |
| v2 | trend_8_26 AND breakout_8 | 9287.76 | -712.24 | sell / filled / 직전 완료 봉 목표 비중 0%; 다음 봉 시가 가정 |
| v2 | trend_8_26 + breakout_8 | 9587.15 | -412.85 | sell / filled / 직전 완료 봉 목표 비중 50%; 다음 봉 시가 가정 |
| v2 | trend_8_26 AND reversion_12 | 9899.33 | -100.67 | sell / filled / 직전 완료 봉 목표 비중 0%; 다음 봉 시가 가정 |
| v2 | trend_8_26 + reversion_12 | 9963.27 | -36.73 | sell / filled / 직전 완료 봉 목표 비중 50%; 다음 봉 시가 가정 |
| v2 | trend_8_26 AND volume_26 | 9833.30 | -166.70 | sell / filled / 직전 완료 봉 목표 비중 0%; 다음 봉 시가 가정 |
| v2 | trend_8_26 + volume_26 | 9897.09 | -102.91 | sell / filled / 직전 완료 봉 목표 비중 50%; 다음 봉 시가 가정 |
| v2 | momentum_26 AND breakout_8 | 9232.70 | -767.30 | sell / filled / 직전 완료 봉 목표 비중 0%; 다음 봉 시가 가정 |
| v2 | momentum_26 + breakout_8 | 9363.07 | -636.93 | sell / filled / 직전 완료 봉 목표 비중 50%; 다음 봉 시가 가정 |
| v2 | momentum_26 AND reversion_12 | 9868.73 | -131.27 | sell / filled / 직전 완료 봉 목표 비중 0%; 다음 봉 시가 가정 |
| v2 | momentum_26 + reversion_12 | 9791.64 | -208.36 | sell / filled / 직전 완료 봉 목표 비중 50%; 다음 봉 시가 가정 |
| v2 | momentum_26 AND volume_26 | 9833.30 | -166.70 | sell / filled / 직전 완료 봉 목표 비중 0%; 다음 봉 시가 가정 |
| v2 | momentum_26 + volume_26 | 9706.29 | -293.71 | sell / filled / 직전 완료 봉 목표 비중 50%; 다음 봉 시가 가정 |
| v2 | breakout_8 AND reversion_12 | 10000.00 | 0.00 | 대기 /  / 새 신호 대기 |
| v2 | breakout_8 + reversion_12 | 9615.31 | -384.69 | sell / filled / 직전 완료 봉 목표 비중 0%; 다음 봉 시가 가정 |
| v2 | breakout_8 AND volume_26 | 9926.66 | -73.34 | sell / filled / 직전 완료 봉 목표 비중 0%; 다음 봉 시가 가정 |
| v2 | breakout_8 + volume_26 | 9570.88 | -429.12 | sell / filled / 직전 완료 봉 목표 비중 0%; 다음 봉 시가 가정 |
| v2 | reversion_12 AND volume_26 | 10051.38 | 51.38 | sell / filled / 직전 완료 봉 목표 비중 0%; 다음 봉 시가 가정 |
| v2 | reversion_12 + volume_26 | 9905.75 | -94.25 | sell / filled / 직전 완료 봉 목표 비중 0%; 다음 봉 시가 가정 |
| v2 | ema_12_26 | 9923.84 | -76.16 | buy / partial / EMA12 > EMA26; 조건 충족; EMA12=334.708, EMA26=334.451; 직전 완료 봉 목표를 다음 봉 시가에 모의 적용 |
| v2 | macd_12_26_9 | 9971.56 | -28.44 | sell / filled / MACD > 신호선 그리고 MACD > 0; 조건 미충족; MACD=1.87003, signal9=1.96381; 직전 완료 봉 목표를 다음 봉 시가에 모의 적용 |
| v2 | rsi_14_recovery | 10000.00 | 0.00 | 대기 /  / 새 신호 대기 |
| v2 | bollinger_20_reentry | 10000.00 | 0.00 | 대기 /  / 새 신호 대기 |
| v2 | donchian_20 | 9868.35 | -131.65 | sell / filled / 종가 > 현재 봉을 제외한 직전 20봉 최고가; 조건 미충족; close=343.037, prior_high20=344.4; 직전 완료 봉 목표를 다음 봉 시가에 모의 적용 |
| v2 | atr_14_breakout | 9882.97 | -117.03 | sell / filled / 종가 > 직전 종가 + 직전 ATR14 그리고 종가 > EMA26; 조건 미충족; close=342.515, threshold=344.598, prior_ATR14=1.50332, EMA26=336.975; 직전 완료 봉 목표를 다음 봉 시가에 모의 적용 |
| v2 | session_vwap | 9932.83 | -67.17 | sell / filled / 종가 > 뉴욕 거래일별 누적 전형가격 VWAP; 조건 미충족; close=342, session_VWAP=342.233, session_volume=3.25898e+06; 직전 완료 봉 목표를 다음 봉 시가에 모의 적용 |
| v2 | obv_20 | 10005.55 | 5.55 | sell / filled / OBV > OBV의 SMA20 그리고 종가 > EMA26; 조건 미충족; OBV=-1.38544e+07, OBV_SMA20=-1.10099e+07, close=341.625, EMA26=338.807; 직전 완료 봉 목표를 다음 봉 시가에 모의 적용 |
| v2 | stochastic_14_3_recovery | 9971.77 | -28.23 | sell / filled / 직전 %K14 < 20에서 %K14가 %D3 상향 돌파 (한 봉 목표); 조건 미충족; K14=21.5845, D3=12.4907, previous_K14=14.6076, previous_D3=9.68611; 직전 완료 봉 목표를 다음 봉 시가에 모의 적용 |
| v2 | mfi_14_recovery | 10000.00 | 0.00 | 대기 /  / 새 신호 대기 |
| v2 | adx_14_trend | 9805.00 | -195.00 | sell / filled / Wilder ADX14 >= 25 그리고 +DI14 > -DI14; 조건 미충족; ADX14=30.1815, plus_DI14=27.5695, minus_DI14=29.9812; 직전 완료 봉 목표를 다음 봉 시가에 모의 적용 |
| v2 | aroon_25_trend | 9822.74 | -177.26 | sell / filled / Aroon25 Up > 70 그리고 Down < 30 (동률이면 최신 극값); 조건 미충족; Aroon_up=68, Aroon_down=16; 직전 완료 봉 목표를 다음 봉 시가에 모의 적용 |
| v2 | cci_20_momentum | 10048.61 | 48.61 | sell / filled / CCI20 > 100 (전형가격·평균절대편차); 조건 미충족; CCI20=93.5627; 직전 완료 봉 목표를 다음 봉 시가에 모의 적용 |
| v2 | williams_14_recovery | 9950.92 | -49.08 | buy / partial / 직전 Williams %R14 < -80, 현재 >= -80 (한 봉 목표); 조건 충족; Williams_R14=-78.4155, previous_R14=-85.3924; 직전 완료 봉 목표를 다음 봉 시가에 모의 적용 |
| v2 | cmf_20_accumulation | 9930.17 | -69.83 | sell / filled / Chaikin Money Flow20 > 0.1; 조건 미충족; CMF20=-0.14511, volume20=9.3038e+06; 직전 완료 봉 목표를 다음 봉 시가에 모의 적용 |
| v2 | chaikin_3_10 | 10005.55 | 5.55 | sell / filled / ADL의 EMA3 - EMA10 > 0 그리고 종가 > EMA26; 조건 미충족; Chaikin3_10=-655976, ADL=-7.91325e+06, close=341.625, EMA26=338.807; 직전 완료 봉 목표를 다음 봉 시가에 모의 적용 |
| v2 | roc_10_momentum | 9911.86 | -88.14 | sell / filled / 10봉 ROC > 1% 그리고 종가 > EMA26; 조건 미충족; ROC10_percent=-0.490038, close=340.901, EMA26=338.962; 직전 완료 봉 목표를 다음 봉 시가에 모의 적용 |
| v2 | trix_15_trend | 9872.78 | -127.22 | buy / partial / 15봉 삼중 EMA의 1봉 변화율 TRIX > 0 그리고 종가 > EMA26; 조건 충족; TRIX15_percent=0.0635068, close=339.005, EMA26=338.985; 직전 완료 봉 목표를 다음 봉 시가에 모의 적용 |
| v2 | keltner_20_breakout | 9945.00 | -55.00 | sell / filled / 종가 > EMA20 + 2 x Wilder ATR14; 조건 미충족; close=342, upper_Keltner=342.276, EMA20=339.397, ATR14=1.43933; 직전 완료 봉 목표를 다음 봉 시가에 모의 적용 |
| v2 | opening_range_30m | 9925.82 | -74.18 | sell / filled / 뉴욕 09:30·09:45 두 완료 봉 최고가를 10:00 이후 종가가 돌파; 조건 미충족; close=343.037, opening_high=343.75; 직전 완료 봉 목표를 다음 봉 시가에 모의 적용 |

### 같은 기간의 비용·노출 비교 (사후 연구)

| 전략 | 비용 전 | 비용 후 | 100% 보유 | 같은 평균 노출 보유 | 평균 노출 |
|---|---:|---:|---:|---:|---:|
| cash | 0.00% | 0.00% | -1.52% | -0.00% | 0.00% |
| buy_hold | -1.11% | -1.52% | -1.52% | -1.52% | 100.00% |
| trend_8_26 | 0.42% | -3.71% | -1.52% | -0.81% | 52.62% |
| momentum_26 | -2.63% | -9.34% | -1.52% | -0.73% | 47.12% |
| breakout_8 | -3.50% | -18.42% | -1.52% | -0.31% | 19.63% |
| reversion_12 | 4.21% | -10.41% | -1.52% | -0.43% | 27.75% |
| volume_26 | -0.11% | -6.20% | -1.52% | -0.11% | 6.81% |
| trend_8_26 AND momentum_26 | 0.51% | -4.43% | -1.52% | -0.64% | 41.36% |
| trend_8_26 + momentum_26 | -1.11% | -6.36% | -1.52% | -0.77% | 49.87% |
| trend_8_26 AND breakout_8 | -3.54% | -13.88% | -1.52% | -0.19% | 12.30% |
| trend_8_26 + breakout_8 | -1.54% | -11.17% | -1.52% | -0.56% | 36.13% |
| trend_8_26 AND reversion_12 | 2.40% | -4.25% | -1.52% | -0.12% | 7.85% |
| trend_8_26 + reversion_12 | 2.32% | -6.54% | -1.52% | -0.62% | 40.19% |
| trend_8_26 AND volume_26 | -0.58% | -4.67% | -1.52% | -0.07% | 4.19% |
| trend_8_26 + volume_26 | 0.18% | -4.96% | -1.52% | -0.46% | 29.72% |
| momentum_26 AND breakout_8 | -2.38% | -12.85% | -1.52% | -0.19% | 12.04% |
| momentum_26 + breakout_8 | -3.04% | -13.80% | -1.52% | -0.52% | 33.38% |
| momentum_26 AND reversion_12 | 2.47% | -4.59% | -1.52% | -0.11% | 6.81% |
| momentum_26 + reversion_12 | 0.76% | -8.35% | -1.52% | -0.58% | 37.44% |
| momentum_26 AND volume_26 | 0.21% | -2.70% | -1.52% | -0.05% | 2.88% |
| momentum_26 + volume_26 | -1.35% | -7.19% | -1.52% | -0.42% | 26.97% |
| breakout_8 AND reversion_12 | 0.00% | 0.00% | -1.52% | -0.00% | 0.00% |
| breakout_8 + reversion_12 | 0.30% | -13.07% | -1.52% | -0.37% | 23.70% |
| breakout_8 AND volume_26 | -0.51% | -2.17% | -1.52% | -0.02% | 1.05% |
| breakout_8 + volume_26 | -1.80% | -11.42% | -1.52% | -0.21% | 13.23% |
| reversion_12 AND volume_26 | 1.25% | -2.10% | -1.52% | -0.05% | 3.40% |
| reversion_12 + volume_26 | 2.04% | -7.56% | -1.52% | -0.27% | 17.28% |
| ema_12_26 | 0.08% | -3.23% | -1.52% | -0.76% | 48.95% |
| macd_12_26_9 | 0.83% | -3.32% | -1.52% | -0.48% | 30.89% |
| rsi_14_recovery | 0.14% | -2.35% | -1.52% | -0.02% | 1.57% |
| bollinger_20_reentry | 0.44% | -5.30% | -1.52% | -0.06% | 3.66% |
| donchian_20 | -1.79% | -4.63% | -1.52% | -0.05% | 2.88% |
| atr_14_breakout | -1.13% | -7.55% | -1.52% | -0.07% | 4.45% |
| session_vwap | 0.96% | -8.72% | -1.52% | -0.73% | 47.38% |
| obv_20 | -3.84% | -14.87% | -1.52% | -0.47% | 30.37% |
| stochastic_14_3_recovery | -1.73% | -13.00% | -1.52% | -0.12% | 7.59% |
| mfi_14_recovery | 0.16% | -1.50% | -1.52% | -0.02% | 1.05% |
| adx_14_trend | -3.19% | -6.39% | -1.52% | -0.43% | 27.49% |
| aroon_25_trend | -1.62% | -6.06% | -1.52% | -0.36% | 23.04% |
| cci_20_momentum | -2.59% | -10.44% | -1.52% | -0.24% | 15.18% |
| williams_14_recovery | -2.81% | -13.59% | -1.52% | -0.11% | 7.33% |
| cmf_20_accumulation | -2.99% | -11.55% | -1.52% | -0.52% | 33.51% |
| chaikin_3_10 | 1.50% | -7.07% | -1.52% | -0.51% | 32.98% |
| roc_10_momentum | -0.98% | -3.45% | -1.52% | -0.12% | 7.85% |
| trix_15_trend | -1.05% | -8.25% | -1.52% | -0.54% | 34.55% |
| keltner_20_breakout | -1.19% | -3.65% | -1.52% | -0.06% | 3.93% |
| opening_range_30m | -0.19% | -3.89% | -1.52% | -0.27% | 17.02% |

동일 구간·초기 자금, 종료 시 청산 비용 포함. 노출 맞춤은 사후 설명용이며 v2 실제 계좌 성과가 아닙니다.
[낙폭 분해·비용 영향·전체 구간](JPM/comparison.json)

[v1 전체 기록](JPM/accounts.json) · [v2 전체 기록](JPM/accounts-v2.json)

## XOM 계좌

| 모델 | 전략 | 평가액 USD | 손익 USD | 최근 매매·이유 |
|---|---|---:|---:|---|
| v1 | cash | 10000.00 | 0.00 | 대기 /  / 새 신호 대기 |
| v1 | buy_hold | 10067.40 | 67.40 | buy /  / buy_hold: prior completed bar target 100%; next bar open simulation |
| v1 | trend_8_26 | 10128.52 | 128.52 | buy /  / trend_8_26: prior completed bar target 100%; next bar open simulation |
| v1 | momentum_26 | 10095.14 | 95.14 | buy /  / momentum_26: prior completed bar target 100%; next bar open simulation |
| v1 | breakout_8 | 9873.67 | -126.33 | sell /  / breakout_8: prior completed bar target 0%; next bar open simulation |
| v1 | reversion_12 | 10000.00 | 0.00 | 대기 /  / 새 신호 대기 |
| v1 | volume_26 | 9889.56 | -110.44 | sell /  / volume_26: prior completed bar target 0%; next bar open simulation |
| v1 | trend_8_26 AND momentum_26 | 10128.52 | 128.52 | buy /  / trend_8_26 AND momentum_26: prior completed bar target 100%; next bar open simulation |
| v1 | trend_8_26 + momentum_26 | 10111.80 | 111.80 | buy /  / trend_8_26 + momentum_26: prior completed bar target 100%; next bar open simulation |
| v1 | trend_8_26 AND breakout_8 | 9995.55 | -4.45 | sell /  / trend_8_26 AND breakout_8: prior completed bar target 0%; next bar open simulation |
| v1 | trend_8_26 + breakout_8 | 10020.31 | 20.31 | sell /  / trend_8_26 + breakout_8: prior completed bar target 50%; next bar open simulation |
| v1 | trend_8_26 AND reversion_12 | 10000.00 | 0.00 | 대기 /  / 새 신호 대기 |
| v1 | trend_8_26 + reversion_12 | 10064.00 | 64.00 | buy /  / trend_8_26 + reversion_12: prior completed bar target 50%; next bar open simulation |
| v1 | trend_8_26 AND volume_26 | 9985.49 | -14.51 | sell /  / trend_8_26 AND volume_26: prior completed bar target 0%; next bar open simulation |
| v1 | trend_8_26 + volume_26 | 10008.26 | 8.26 | buy /  / trend_8_26 + volume_26: prior completed bar target 50%; next bar open simulation |
| v1 | momentum_26 AND breakout_8 | 9922.84 | -77.16 | sell /  / momentum_26 AND breakout_8: prior completed bar target 0%; next bar open simulation |
| v1 | momentum_26 + breakout_8 | 9983.82 | -16.18 | sell /  / momentum_26 + breakout_8: prior completed bar target 50%; next bar open simulation |
| v1 | momentum_26 AND reversion_12 | 10000.00 | 0.00 | 대기 /  / 새 신호 대기 |
| v1 | momentum_26 + reversion_12 | 10047.40 | 47.40 | buy /  / momentum_26 + reversion_12: prior completed bar target 50%; next bar open simulation |
| v1 | momentum_26 AND volume_26 | 9985.49 | -14.51 | sell /  / momentum_26 AND volume_26: prior completed bar target 0%; next bar open simulation |
| v1 | momentum_26 + volume_26 | 9991.76 | -8.24 | buy /  / momentum_26 + volume_26: prior completed bar target 50%; next bar open simulation |
| v1 | breakout_8 AND reversion_12 | 10000.00 | 0.00 | 대기 /  / 새 신호 대기 |
| v1 | breakout_8 + reversion_12 | 9936.58 | -63.42 | sell /  / breakout_8 + reversion_12: prior completed bar target 0%; next bar open simulation |
| v1 | breakout_8 AND volume_26 | 9950.44 | -49.56 | sell /  / breakout_8 AND volume_26: prior completed bar target 0%; next bar open simulation |
| v1 | breakout_8 + volume_26 | 9881.54 | -118.46 | sell /  / breakout_8 + volume_26: prior completed bar target 0%; next bar open simulation |
| v1 | reversion_12 AND volume_26 | 10000.00 | 0.00 | 대기 /  / 새 신호 대기 |
| v1 | reversion_12 + volume_26 | 9944.60 | -55.40 | sell /  / reversion_12 + volume_26: prior completed bar target 0%; next bar open simulation |
| v1 | ema_12_26 | 10125.63 | 125.63 | buy /  / EMA12 > EMA26; 조건 충족; EMA12=175.145, EMA26=175.141 |
| v1 | macd_12_26_9 | 10125.63 | 125.63 | buy /  / MACD > 신호선 그리고 MACD > 0; 조건 충족; MACD=0.00418876, signal9=-0.17046 |
| v1 | rsi_14_recovery | 10000.00 | 0.00 | 대기 /  / 새 신호 대기 |
| v1 | bollinger_20_reentry | 9913.52 | -86.48 | sell /  / 직전 종가 < 직전 하단밴드, 현재 하단밴드 <= 종가 <= SMA20 (한 봉 목표); 조건 미충족; close=175.71, lower20=173.907, SMA20=174.743, previous_lower20=173.977 |
| v1 | donchian_20 | 9906.82 | -93.18 | sell /  / 종가 > 현재 봉을 제외한 직전 20봉 최고가; 조건 미충족; close=177.975, prior_high20=178.18 |
| v1 | atr_14_breakout | 9864.96 | -135.04 | sell /  / 종가 > 직전 종가 + 직전 ATR14 그리고 종가 > EMA26; 조건 미충족; close=177.19, threshold=177.748, prior_ATR14=0.663113, EMA26=175.734 |
| v1 | session_vwap | 10026.34 | 26.34 | buy /  / 종가 > 뉴욕 거래일별 누적 전형가격 VWAP; 조건 충족; close=176.25, session_VWAP=175.945, session_volume=7.74672e+06 |
| v1 | obv_20 | 9970.37 | -29.63 | sell /  / OBV > OBV의 SMA20 그리고 종가 > EMA26; 조건 미충족; OBV=1.88162e+07, OBV_SMA20=2.13258e+07, close=175.84, EMA26=175.361 |
| v1 | stochastic_14_3_recovery | 10000.00 | 0.00 | 대기 /  / 새 신호 대기 |
| v1 | mfi_14_recovery | 10000.00 | 0.00 | 대기 /  / 새 신호 대기 |
| v1 | adx_14_trend | 10104.25 | 104.25 | buy /  / Wilder ADX14 >= 25 그리고 +DI14 > -DI14; 조건 충족; ADX14=25.0494, plus_DI14=28.5472, minus_DI14=15.0232 |
| v1 | aroon_25_trend | 9983.39 | -16.61 | buy /  / Aroon25 Up > 70 그리고 Down < 30 (동률이면 최신 극값); 조건 충족; Aroon_up=100, Aroon_down=28 |
| v1 | cci_20_momentum | 9959.10 | -40.90 | buy /  / CCI20 > 100 (전형가격·평균절대편차); 조건 충족; CCI20=102.776 |
| v1 | williams_14_recovery | 9913.52 | -86.48 | sell /  / 직전 Williams %R14 < -80, 현재 >= -80 (한 봉 목표); 조건 미충족; Williams_R14=-43.9575, previous_R14=-33.1215 |
| v1 | cmf_20_accumulation | 10000.00 | 0.00 | 대기 /  / 새 신호 대기 |
| v1 | chaikin_3_10 | 9979.47 | -20.53 | buy /  / ADL의 EMA3 - EMA10 > 0 그리고 종가 > EMA26; 조건 충족; Chaikin3_10=43082.7, ADL=2.817e+07, close=178.08, EMA26=176.138 |
| v1 | roc_10_momentum | 10001.00 | 1.00 | buy /  / 10봉 ROC > 1% 그리고 종가 > EMA26; 조건 충족; ROC10_percent=1.10566, close=177.4, EMA26=175.858 |
| v1 | trix_15_trend | 10078.53 | 78.53 | buy /  / 15봉 삼중 EMA의 1봉 변화율 TRIX > 0 그리고 종가 > EMA26; 조건 충족; TRIX15_percent=0.00176833, close=176.25, EMA26=175.427 |
| v1 | keltner_20_breakout | 10031.87 | 31.87 | buy /  / 종가 > EMA20 + 2 x Wilder ATR14; 조건 충족; close=177.085, upper_Keltner=177.035, EMA20=175.709, ATR14=0.663113 |
| v1 | opening_range_30m | 10017.17 | 17.17 | buy /  / 뉴욕 09:30·09:45 두 완료 봉 최고가를 10:00 이후 종가가 돌파; 조건 충족; close=177.4, opening_high=177.365 |
| v2 | cash | 10000.00 | 0.00 | 대기 /  / 새 신호 대기 |
| v2 | buy_hold | 10388.67 | 388.67 | buy / partial / 직전 완료 봉 목표 비중 100%; 다음 봉 시가 가정 |
| v2 | trend_8_26 | 10224.99 | 224.99 | buy / partial / 직전 완료 봉 목표 비중 100%; 다음 봉 시가 가정 |
| v2 | momentum_26 | 10268.40 | 268.40 | buy / partial / 직전 완료 봉 목표 비중 100%; 다음 봉 시가 가정 |
| v2 | breakout_8 | 9343.89 | -656.11 | sell / filled / 직전 완료 봉 목표 비중 0%; 다음 봉 시가 가정 |
| v2 | reversion_12 | 9815.06 | -184.94 | sell / filled / 직전 완료 봉 목표 비중 0%; 다음 봉 시가 가정 |
| v2 | volume_26 | 9794.70 | -205.30 | sell / filled / 직전 완료 봉 목표 비중 0%; 다음 봉 시가 가정 |
| v2 | trend_8_26 AND momentum_26 | 10232.57 | 232.57 | buy / partial / 직전 완료 봉 목표 비중 100%; 다음 봉 시가 가정 |
| v2 | trend_8_26 + momentum_26 | 10246.68 | 246.68 | buy / partial / 직전 완료 봉 목표 비중 100%; 다음 봉 시가 가정 |
| v2 | trend_8_26 AND breakout_8 | 9445.74 | -554.26 | sell / filled / 직전 완료 봉 목표 비중 0%; 다음 봉 시가 가정 |
| v2 | trend_8_26 + breakout_8 | 9816.04 | -183.96 | sell / filled / 직전 완료 봉 목표 비중 50%; 다음 봉 시가 가정 |
| v2 | trend_8_26 AND reversion_12 | 9839.70 | -160.30 | sell / filled / 직전 완료 봉 목표 비중 0%; 다음 봉 시가 가정 |
| v2 | trend_8_26 + reversion_12 | 10017.96 | 17.96 | buy / filled / 직전 완료 봉 목표 비중 50%; 다음 봉 시가 가정 |
| v2 | trend_8_26 AND volume_26 | 9879.28 | -120.72 | sell / filled / 직전 완료 봉 목표 비중 0%; 다음 봉 시가 가정 |
| v2 | trend_8_26 + volume_26 | 10007.42 | 7.42 | buy / filled / 직전 완료 봉 목표 비중 50%; 다음 봉 시가 가정 |
| v2 | momentum_26 AND breakout_8 | 9392.31 | -607.69 | sell / filled / 직전 완료 봉 목표 비중 0%; 다음 봉 시가 가정 |
| v2 | momentum_26 + breakout_8 | 9795.82 | -204.18 | sell / filled / 직전 완료 봉 목표 비중 50%; 다음 봉 시가 가정 |
| v2 | momentum_26 AND reversion_12 | 9800.13 | -199.87 | sell / filled / 직전 완료 봉 목표 비중 0%; 다음 봉 시가 가정 |
| v2 | momentum_26 + reversion_12 | 10039.24 | 39.24 | buy / filled / 직전 완료 봉 목표 비중 50%; 다음 봉 시가 가정 |
| v2 | momentum_26 AND volume_26 | 9941.52 | -58.48 | sell / filled / 직전 완료 봉 목표 비중 0%; 다음 봉 시가 가정 |
| v2 | momentum_26 + volume_26 | 10049.71 | 49.71 | buy / filled / 직전 완료 봉 목표 비중 50%; 다음 봉 시가 가정 |
| v2 | breakout_8 AND reversion_12 | 10000.00 | 0.00 | 대기 /  / 새 신호 대기 |
| v2 | breakout_8 + reversion_12 | 9576.43 | -423.57 | sell / filled / 직전 완료 봉 목표 비중 0%; 다음 봉 시가 가정 |
| v2 | breakout_8 AND volume_26 | 9918.86 | -81.14 | sell / filled / 직전 완료 봉 목표 비중 0%; 다음 봉 시가 가정 |
| v2 | breakout_8 + volume_26 | 9586.59 | -413.41 | sell / filled / 직전 완료 봉 목표 비중 0%; 다음 봉 시가 가정 |
| v2 | reversion_12 AND volume_26 | 9949.87 | -50.13 | sell / filled / 직전 완료 봉 목표 비중 0%; 다음 봉 시가 가정 |
| v2 | reversion_12 + volume_26 | 9825.48 | -174.52 | sell / filled / 직전 완료 봉 목표 비중 0%; 다음 봉 시가 가정 |
| v2 | ema_12_26 | 10124.62 | 124.62 | buy / partial / EMA12 > EMA26; 조건 충족; EMA12=175.145, EMA26=175.141; 직전 완료 봉 목표를 다음 봉 시가에 모의 적용 |
| v2 | macd_12_26_9 | 10124.62 | 124.62 | buy / partial / MACD > 신호선 그리고 MACD > 0; 조건 충족; MACD=0.00418876, signal9=-0.17046; 직전 완료 봉 목표를 다음 봉 시가에 모의 적용 |
| v2 | rsi_14_recovery | 10000.00 | 0.00 | 대기 /  / 새 신호 대기 |
| v2 | bollinger_20_reentry | 9911.54 | -88.46 | sell / filled / 직전 종가 < 직전 하단밴드, 현재 하단밴드 <= 종가 <= SMA20 (한 봉 목표); 조건 미충족; close=175.71, lower20=173.907, SMA20=174.743, previous_lower20=173.977; 직전 완료 봉 목표를 다음 봉 시가에 모의 적용 |
| v2 | donchian_20 | 9902.86 | -97.14 | sell / filled / 종가 > 현재 봉을 제외한 직전 20봉 최고가; 조건 미충족; close=177.975, prior_high20=178.18; 직전 완료 봉 목표를 다음 봉 시가에 모의 적용 |
| v2 | atr_14_breakout | 9859.04 | -140.96 | sell / filled / 종가 > 직전 종가 + 직전 ATR14 그리고 종가 > EMA26; 조건 미충족; close=177.19, threshold=177.748, prior_ATR14=0.663113, EMA26=175.734; 직전 완료 봉 목표를 다음 봉 시가에 모의 적용 |
| v2 | session_vwap | 10023.33 | 23.33 | buy / partial / 종가 > 뉴욕 거래일별 누적 전형가격 VWAP; 조건 충족; close=176.25, session_VWAP=175.945, session_volume=7.74672e+06; 직전 완료 봉 목표를 다음 봉 시가에 모의 적용 |
| v2 | obv_20 | 9968.37 | -31.63 | sell / filled / OBV > OBV의 SMA20 그리고 종가 > EMA26; 조건 미충족; OBV=1.88162e+07, OBV_SMA20=2.13258e+07, close=175.84, EMA26=175.361; 직전 완료 봉 목표를 다음 봉 시가에 모의 적용 |
| v2 | stochastic_14_3_recovery | 10000.00 | 0.00 | 대기 /  / 새 신호 대기 |
| v2 | mfi_14_recovery | 10000.00 | 0.00 | 대기 /  / 새 신호 대기 |
| v2 | adx_14_trend | 10103.24 | 103.24 | buy / partial / Wilder ADX14 >= 25 그리고 +DI14 > -DI14; 조건 충족; ADX14=25.0494, plus_DI14=28.5472, minus_DI14=15.0232; 직전 완료 봉 목표를 다음 봉 시가에 모의 적용 |
| v2 | aroon_25_trend | 9982.40 | -17.60 | buy / partial / Aroon25 Up > 70 그리고 Down < 30 (동률이면 최신 극값); 조건 충족; Aroon_up=100, Aroon_down=28; 직전 완료 봉 목표를 다음 봉 시가에 모의 적용 |
| v2 | cci_20_momentum | 9954.12 | -45.88 | buy / partial / CCI20 > 100 (전형가격·평균절대편차); 조건 충족; CCI20=102.776; 직전 완료 봉 목표를 다음 봉 시가에 모의 적용 |
| v2 | williams_14_recovery | 9911.54 | -88.46 | sell / filled / 직전 Williams %R14 < -80, 현재 >= -80 (한 봉 목표); 조건 미충족; Williams_R14=-43.9575, previous_R14=-33.1215; 직전 완료 봉 목표를 다음 봉 시가에 모의 적용 |
| v2 | cmf_20_accumulation | 10000.00 | 0.00 | 대기 /  / 새 신호 대기 |
| v2 | chaikin_3_10 | 9978.47 | -21.53 | buy / partial / ADL의 EMA3 - EMA10 > 0 그리고 종가 > EMA26; 조건 충족; Chaikin3_10=43082.7, ADL=2.817e+07, close=178.08, EMA26=176.138; 직전 완료 봉 목표를 다음 봉 시가에 모의 적용 |
| v2 | roc_10_momentum | 9998.01 | -1.99 | buy / partial / 10봉 ROC > 1% 그리고 종가 > EMA26; 조건 충족; ROC10_percent=1.10566, close=177.4, EMA26=175.858; 직전 완료 봉 목표를 다음 봉 시가에 모의 적용 |
| v2 | trix_15_trend | 10077.53 | 77.53 | buy / partial / 15봉 삼중 EMA의 1봉 변화율 TRIX > 0 그리고 종가 > EMA26; 조건 충족; TRIX15_percent=0.00176833, close=176.25, EMA26=175.427; 직전 완료 봉 목표를 다음 봉 시가에 모의 적용 |
| v2 | keltner_20_breakout | 10030.87 | 30.87 | buy / partial / 종가 > EMA20 + 2 x Wilder ATR14; 조건 충족; close=177.085, upper_Keltner=177.035, EMA20=175.709, ATR14=0.663113; 직전 완료 봉 목표를 다음 봉 시가에 모의 적용 |
| v2 | opening_range_30m | 10016.17 | 16.17 | buy / partial / 뉴욕 09:30·09:45 두 완료 봉 최고가를 10:00 이후 종가가 돌파; 조건 충족; close=177.4, opening_high=177.365; 직전 완료 봉 목표를 다음 봉 시가에 모의 적용 |

### 같은 기간의 비용·노출 비교 (사후 연구)

| 전략 | 비용 전 | 비용 후 | 100% 보유 | 같은 평균 노출 보유 | 평균 노출 |
|---|---:|---:|---:|---:|---:|
| cash | 0.00% | 0.00% | 9.10% | 0.00% | 0.00% |
| buy_hold | 9.56% | 9.10% | 9.10% | 9.10% | 100.00% |
| trend_8_26 | 2.50% | -2.13% | 9.10% | 5.97% | 66.23% |
| momentum_26 | 1.37% | -6.01% | 9.10% | 6.50% | 71.99% |
| breakout_8 | -2.54% | -20.33% | 9.10% | 2.17% | 24.35% |
| reversion_12 | 7.01% | -3.65% | 9.10% | 1.84% | 20.68% |
| volume_26 | 4.19% | -3.80% | 9.10% | 0.46% | 5.24% |
| trend_8_26 AND momentum_26 | 1.03% | -3.94% | 9.10% | 5.49% | 60.99% |
| trend_8_26 + momentum_26 | 1.95% | -3.88% | 9.10% | 6.23% | 69.11% |
| trend_8_26 AND breakout_8 | -0.45% | -14.77% | 9.10% | 1.74% | 19.63% |
| trend_8_26 + breakout_8 | -0.02% | -11.31% | 9.10% | 4.06% | 45.30% |
| trend_8_26 AND reversion_12 | 1.89% | -3.93% | 9.10% | 0.72% | 8.12% |
| trend_8_26 + reversion_12 | 4.76% | -2.69% | 9.10% | 3.89% | 43.46% |
| trend_8_26 AND volume_26 | 2.80% | -1.84% | 9.10% | 0.25% | 2.88% |
| trend_8_26 + volume_26 | 3.36% | -2.56% | 9.10% | 3.19% | 35.74% |
| momentum_26 AND breakout_8 | -2.65% | -19.08% | 9.10% | 2.00% | 22.51% |
| momentum_26 + breakout_8 | -0.58% | -13.45% | 9.10% | 4.32% | 48.17% |
| momentum_26 AND reversion_12 | 2.27% | -4.38% | 9.10% | 0.79% | 8.90% |
| momentum_26 + reversion_12 | 4.19% | -3.43% | 9.10% | 4.15% | 46.34% |
| momentum_26 AND volume_26 | 2.58% | -1.64% | 9.10% | 0.23% | 2.62% |
| momentum_26 + volume_26 | 2.80% | -3.50% | 9.10% | 3.45% | 38.62% |
| breakout_8 AND reversion_12 | 0.00% | 0.00% | 9.10% | 0.00% | 0.00% |
| breakout_8 + reversion_12 | 2.15% | -12.21% | 9.10% | 2.00% | 22.52% |
| breakout_8 AND volume_26 | 0.51% | -1.17% | 9.10% | 0.09% | 1.05% |
| breakout_8 + volume_26 | 0.78% | -11.34% | 9.10% | 1.31% | 14.80% |
| reversion_12 AND volume_26 | 1.52% | -1.00% | 9.10% | 0.14% | 1.57% |
| reversion_12 + volume_26 | 5.61% | -2.91% | 9.10% | 1.15% | 12.96% |
| ema_12_26 | 0.98% | -2.35% | 9.10% | 6.84% | 75.65% |
| macd_12_26_9 | -0.12% | -5.83% | 9.10% | 3.72% | 41.62% |
| rsi_14_recovery | -0.15% | -0.57% | 9.10% | 0.02% | 0.26% |
| bollinger_20_reentry | -0.87% | -3.75% | 9.10% | 0.16% | 1.83% |
| donchian_20 | -1.13% | -10.23% | 9.10% | 0.81% | 9.16% |
| atr_14_breakout | -1.27% | -10.74% | 9.10% | 0.58% | 6.54% |
| session_vwap | 0.19% | -11.67% | 9.10% | 5.97% | 66.23% |
| obv_20 | 2.12% | -5.32% | 9.10% | 3.79% | 42.41% |
| stochastic_14_3_recovery | 1.55% | -6.63% | 9.10% | 0.46% | 5.24% |
| mfi_14_recovery | -0.31% | -1.97% | 9.10% | 0.09% | 1.05% |
| adx_14_trend | 2.09% | -0.87% | 9.10% | 3.91% | 43.72% |
| aroon_25_trend | -1.75% | -8.14% | 9.10% | 2.73% | 30.63% |
| cci_20_momentum | 3.67% | -4.28% | 9.10% | 2.52% | 28.27% |
| williams_14_recovery | 0.08% | -5.24% | 9.10% | 0.30% | 3.40% |
| cmf_20_accumulation | 0.92% | -6.82% | 9.10% | 4.48% | 50.00% |
| chaikin_3_10 | -1.01% | -9.74% | 9.10% | 4.99% | 55.50% |
| roc_10_momentum | 0.42% | -5.71% | 9.10% | 1.32% | 14.92% |
| trix_15_trend | -1.67% | -8.83% | 9.10% | 5.70% | 63.35% |
| keltner_20_breakout | -0.34% | -7.21% | 9.10% | 1.46% | 16.49% |
| opening_range_30m | 0.02% | -9.57% | 9.10% | 3.27% | 36.65% |

동일 구간·초기 자금, 종료 시 청산 비용 포함. 노출 맞춤은 사후 설명용이며 v2 실제 계좌 성과가 아닙니다.
[낙폭 분해·비용 영향·전체 구간](XOM/comparison.json)

[v1 전체 기록](XOM/accounts.json) · [v2 전체 기록](XOM/accounts-v2.json)

## JNJ 계좌

| 모델 | 전략 | 평가액 USD | 손익 USD | 최근 매매·이유 |
|---|---|---:|---:|---|
| v1 | cash | 10000.00 | 0.00 | 대기 /  / 새 신호 대기 |
| v1 | buy_hold | 9965.77 | -34.23 | buy /  / buy_hold: prior completed bar target 100%; next bar open simulation |
| v1 | trend_8_26 | 9919.96 | -80.04 | buy /  / trend_8_26: prior completed bar target 100%; next bar open simulation |
| v1 | momentum_26 | 9966.94 | -33.06 | buy /  / momentum_26: prior completed bar target 100%; next bar open simulation |
| v1 | breakout_8 | 9822.10 | -177.90 | sell /  / breakout_8: prior completed bar target 0%; next bar open simulation |
| v1 | reversion_12 | 9992.01 | -7.99 | sell /  / reversion_12: prior completed bar target 0%; next bar open simulation |
| v1 | volume_26 | 9935.63 | -64.37 | sell /  / volume_26: prior completed bar target 0%; next bar open simulation |
| v1 | trend_8_26 AND momentum_26 | 9966.94 | -33.06 | buy /  / trend_8_26 AND momentum_26: prior completed bar target 100%; next bar open simulation |
| v1 | trend_8_26 + momentum_26 | 9943.39 | -56.61 | buy /  / trend_8_26 + momentum_26: prior completed bar target 100%; next bar open simulation |
| v1 | trend_8_26 AND breakout_8 | 9937.40 | -62.60 | sell /  / trend_8_26 AND breakout_8: prior completed bar target 0%; next bar open simulation |
| v1 | trend_8_26 + breakout_8 | 9870.87 | -129.13 | sell /  / trend_8_26 + breakout_8: prior completed bar target 50%; next bar open simulation |
| v1 | trend_8_26 AND reversion_12 | 9992.01 | -7.99 | sell /  / trend_8_26 AND reversion_12: prior completed bar target 0%; next bar open simulation |
| v1 | trend_8_26 + reversion_12 | 9955.88 | -44.12 | sell /  / trend_8_26 + reversion_12: prior completed bar target 50%; next bar open simulation |
| v1 | trend_8_26 AND volume_26 | 9935.63 | -64.37 | sell /  / trend_8_26 AND volume_26: prior completed bar target 0%; next bar open simulation |
| v1 | trend_8_26 + volume_26 | 9927.78 | -72.22 | sell /  / trend_8_26 + volume_26: prior completed bar target 50%; next bar open simulation |
| v1 | momentum_26 AND breakout_8 | 10000.00 | 0.00 | 대기 /  / 새 신호 대기 |
| v1 | momentum_26 + breakout_8 | 9894.19 | -105.81 | buy /  / momentum_26 + breakout_8: prior completed bar target 50%; next bar open simulation |
| v1 | momentum_26 AND reversion_12 | 10000.00 | 0.00 | 대기 /  / 새 신호 대기 |
| v1 | momentum_26 + reversion_12 | 9979.42 | -20.58 | buy /  / momentum_26 + reversion_12: prior completed bar target 50%; next bar open simulation |
| v1 | momentum_26 AND volume_26 | 10000.00 | 0.00 | 대기 /  / 새 신호 대기 |
| v1 | momentum_26 + volume_26 | 9951.24 | -48.76 | buy /  / momentum_26 + volume_26: prior completed bar target 50%; next bar open simulation |
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
| v1 | obv_20 | 9867.37 | -132.63 | buy /  / OBV > OBV의 SMA20 그리고 종가 > EMA26; 조건 충족; OBV=5.80642e+06, OBV_SMA20=5.15384e+06, close=255.59, EMA26=255.372 |
| v1 | stochastic_14_3_recovery | 9927.65 | -72.35 | sell /  / 직전 %K14 < 20에서 %K14가 %D3 상향 돌파 (한 봉 목표); 조건 미충족; K14=60.1505, D3=50.3645, previous_K14=74.7605, previous_D3=37.7141 |
| v1 | mfi_14_recovery | 10000.00 | 0.00 | 대기 /  / 새 신호 대기 |
| v1 | adx_14_trend | 9823.79 | -176.21 | sell /  / Wilder ADX14 >= 25 그리고 +DI14 > -DI14; 조건 미충족; ADX14=24.7842, plus_DI14=27.3963, minus_DI14=19.1477 |
| v1 | aroon_25_trend | 9984.14 | -15.86 | buy /  / Aroon25 Up > 70 그리고 Down < 30 (동률이면 최신 극값); 조건 충족; Aroon_up=80, Aroon_down=28 |
| v1 | cci_20_momentum | 9935.63 | -64.37 | sell /  / CCI20 > 100 (전형가격·평균절대편차); 조건 미충족; CCI20=62.9489 |
| v1 | williams_14_recovery | 9927.65 | -72.35 | sell /  / 직전 Williams %R14 < -80, 현재 >= -80 (한 봉 목표); 조건 미충족; Williams_R14=-39.8495, previous_R14=-25.2395 |
| v1 | cmf_20_accumulation | 10000.00 | 0.00 | 대기 /  / 새 신호 대기 |
| v1 | chaikin_3_10 | 10000.00 | 0.00 | 대기 /  / 새 신호 대기 |
| v1 | roc_10_momentum | 9816.66 | -183.34 | sell /  / 10봉 ROC > 1% 그리고 종가 > EMA26; 조건 미충족; ROC10_percent=-0.398319, close=255.08, EMA26=255.591 |
| v1 | trix_15_trend | 9856.43 | -143.57 | buy /  / 15봉 삼중 EMA의 1봉 변화율 TRIX > 0 그리고 종가 > EMA26; 조건 충족; TRIX15_percent=0.00148267, close=255.59, EMA26=255.372 |
| v1 | keltner_20_breakout | 10000.00 | 0.00 | 대기 /  / 새 신호 대기 |
| v1 | opening_range_30m | 10000.00 | 0.00 | 대기 /  / 새 신호 대기 |
| v2 | cash | 10000.00 | 0.00 | 대기 /  / 새 신호 대기 |
| v2 | buy_hold | 9733.18 | -266.82 | 중단: 손실 한도 / buy / partial / 직전 완료 봉 목표 비중 100%; 다음 봉 시가 가정 |
| v2 | trend_8_26 | 9733.18 | -266.82 | 중단: 손실 한도 / buy / partial / 직전 완료 봉 목표 비중 100%; 다음 봉 시가 가정 |
| v2 | momentum_26 | 9733.18 | -266.82 | 중단: 손실 한도 / buy / partial / 직전 완료 봉 목표 비중 100%; 다음 봉 시가 가정 |
| v2 | breakout_8 | 9343.39 | -656.61 | 중단: 손실 한도 / sell / filled / 직전 완료 봉 목표 비중 0%; 다음 봉 시가 가정 |
| v2 | reversion_12 | 9680.46 | -319.54 | sell / filled / 직전 완료 봉 목표 비중 0%; 다음 봉 시가 가정 |
| v2 | volume_26 | 9726.38 | -273.62 | sell / filled / 직전 완료 봉 목표 비중 0%; 다음 봉 시가 가정 |
| v2 | trend_8_26 AND momentum_26 | 9733.18 | -266.82 | 중단: 손실 한도 / buy / partial / 직전 완료 봉 목표 비중 100%; 다음 봉 시가 가정 |
| v2 | trend_8_26 + momentum_26 | 9733.18 | -266.82 | 중단: 손실 한도 / buy / partial / 직전 완료 봉 목표 비중 100%; 다음 봉 시가 가정 |
| v2 | trend_8_26 AND breakout_8 | 9419.39 | -580.61 | 중단: 손실 한도 / sell / filled / 직전 완료 봉 목표 비중 0%; 다음 봉 시가 가정 |
| v2 | trend_8_26 + breakout_8 | 9442.93 | -557.07 | sell / filled / 직전 완료 봉 목표 비중 50%; 다음 봉 시가 가정 |
| v2 | trend_8_26 AND reversion_12 | 9968.12 | -31.88 | sell / filled / 직전 완료 봉 목표 비중 0%; 다음 봉 시가 가정 |
| v2 | trend_8_26 + reversion_12 | 9732.92 | -267.08 | 중단: 손실 한도 / sell / filled / 직전 완료 봉 목표 비중 0%; 다음 봉 시가 가정 |
| v2 | trend_8_26 AND volume_26 | 9805.21 | -194.79 | sell / filled / 직전 완료 봉 목표 비중 0%; 다음 봉 시가 가정 |
| v2 | trend_8_26 + volume_26 | 9839.77 | -160.23 | 중단: 손실 한도 / buy / filled / 직전 완료 봉 목표 비중 50%; 다음 봉 시가 가정 |
| v2 | momentum_26 AND breakout_8 | 9598.70 | -401.30 | sell / filled / 직전 완료 봉 목표 비중 0%; 다음 봉 시가 가정 |
| v2 | momentum_26 + breakout_8 | 9456.35 | -543.65 | buy / filled / 직전 완료 봉 목표 비중 50%; 다음 봉 시가 가정 |
| v2 | momentum_26 AND reversion_12 | 9938.87 | -61.13 | sell / filled / 직전 완료 봉 목표 비중 0%; 다음 봉 시가 가정 |
| v2 | momentum_26 + reversion_12 | 9732.92 | -267.08 | 중단: 손실 한도 / sell / filled / 직전 완료 봉 목표 비중 0%; 다음 봉 시가 가정 |
| v2 | momentum_26 AND volume_26 | 9920.93 | -79.07 | sell / filled / 직전 완료 봉 목표 비중 0%; 다음 봉 시가 가정 |
| v2 | momentum_26 + volume_26 | 9839.77 | -160.23 | 중단: 손실 한도 / buy / filled / 직전 완료 봉 목표 비중 50%; 다음 봉 시가 가정 |
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
| v2 | obv_20 | 9864.42 | -135.58 | buy / partial / OBV > OBV의 SMA20 그리고 종가 > EMA26; 조건 충족; OBV=5.80642e+06, OBV_SMA20=5.15384e+06, close=255.59, EMA26=255.372; 직전 완료 봉 목표를 다음 봉 시가에 모의 적용 |
| v2 | stochastic_14_3_recovery | 9925.66 | -74.34 | sell / filled / 직전 %K14 < 20에서 %K14가 %D3 상향 돌파 (한 봉 목표); 조건 미충족; K14=60.1505, D3=50.3645, previous_K14=74.7605, previous_D3=37.7141; 직전 완료 봉 목표를 다음 봉 시가에 모의 적용 |
| v2 | mfi_14_recovery | 10000.00 | 0.00 | 대기 /  / 새 신호 대기 |
| v2 | adx_14_trend | 9817.90 | -182.10 | sell / filled / Wilder ADX14 >= 25 그리고 +DI14 > -DI14; 조건 미충족; ADX14=24.7842, plus_DI14=27.3963, minus_DI14=19.1477; 직전 완료 봉 목표를 다음 봉 시가에 모의 적용 |
| v2 | aroon_25_trend | 9983.14 | -16.86 | buy / partial / Aroon25 Up > 70 그리고 Down < 30 (동률이면 최신 극값); 조건 충족; Aroon_up=80, Aroon_down=28; 직전 완료 봉 목표를 다음 봉 시가에 모의 적용 |
| v2 | cci_20_momentum | 9933.64 | -66.36 | sell / filled / CCI20 > 100 (전형가격·평균절대편차); 조건 미충족; CCI20=62.9489; 직전 완료 봉 목표를 다음 봉 시가에 모의 적용 |
| v2 | williams_14_recovery | 9925.66 | -74.34 | sell / filled / 직전 Williams %R14 < -80, 현재 >= -80 (한 봉 목표); 조건 미충족; Williams_R14=-39.8495, previous_R14=-25.2395; 직전 완료 봉 목표를 다음 봉 시가에 모의 적용 |
| v2 | cmf_20_accumulation | 10000.00 | 0.00 | 대기 /  / 새 신호 대기 |
| v2 | chaikin_3_10 | 10000.00 | 0.00 | 대기 /  / 새 신호 대기 |
| v2 | roc_10_momentum | 9812.74 | -187.26 | sell / filled / 10봉 ROC > 1% 그리고 종가 > EMA26; 조건 미충족; ROC10_percent=-0.398319, close=255.08, EMA26=255.591; 직전 완료 봉 목표를 다음 봉 시가에 모의 적용 |
| v2 | trix_15_trend | 9853.47 | -146.53 | buy / partial / 15봉 삼중 EMA의 1봉 변화율 TRIX > 0 그리고 종가 > EMA26; 조건 충족; TRIX15_percent=0.00148267, close=255.59, EMA26=255.372; 직전 완료 봉 목표를 다음 봉 시가에 모의 적용 |
| v2 | keltner_20_breakout | 10000.00 | 0.00 | 대기 /  / 새 신호 대기 |
| v2 | opening_range_30m | 10000.00 | 0.00 | 대기 /  / 새 신호 대기 |

### 같은 기간의 비용·노출 비교 (사후 연구)

| 전략 | 비용 전 | 비용 후 | 100% 보유 | 같은 평균 노출 보유 | 평균 노출 |
|---|---:|---:|---:|---:|---:|
| cash | 0.00% | 0.00% | -5.95% | -0.00% | 0.00% |
| buy_hold | -5.56% | -5.95% | -5.95% | -5.95% | 100.00% |
| trend_8_26 | 2.05% | -0.49% | -5.95% | -3.03% | 49.74% |
| momentum_26 | 0.83% | -2.91% | -5.95% | -2.90% | 47.64% |
| breakout_8 | -0.58% | -17.70% | -5.95% | -1.26% | 20.42% |
| reversion_12 | -7.49% | -16.01% | -5.95% | -1.87% | 30.37% |
| volume_26 | -0.78% | -7.23% | -5.95% | -0.41% | 6.54% |
| trend_8_26 AND momentum_26 | 2.22% | -1.16% | -5.95% | -2.67% | 43.72% |
| trend_8_26 + momentum_26 | 1.44% | -1.71% | -5.95% | -2.97% | 48.69% |
| trend_8_26 AND breakout_8 | 0.89% | -11.80% | -5.95% | -0.94% | 15.18% |
| trend_8_26 + breakout_8 | 0.75% | -9.48% | -5.95% | -2.15% | 35.09% |
| trend_8_26 AND reversion_12 | 1.02% | -2.73% | -5.95% | -0.39% | 6.28% |
| trend_8_26 + reversion_12 | -2.80% | -8.18% | -5.95% | -2.45% | 40.06% |
| trend_8_26 AND volume_26 | 1.34% | -1.19% | -5.95% | -0.11% | 1.83% |
| trend_8_26 + volume_26 | 0.66% | -3.70% | -5.95% | -1.73% | 28.14% |
| momentum_26 AND breakout_8 | 2.20% | -9.52% | -5.95% | -0.89% | 14.40% |
| momentum_26 + breakout_8 | 0.15% | -10.41% | -5.95% | -2.09% | 34.04% |
| momentum_26 AND reversion_12 | -0.60% | -3.89% | -5.95% | -0.42% | 6.81% |
| momentum_26 + reversion_12 | -3.39% | -9.12% | -5.95% | -2.39% | 39.01% |
| momentum_26 AND volume_26 | 1.57% | -0.12% | -5.95% | -0.08% | 1.31% |
| momentum_26 + volume_26 | 0.05% | -4.49% | -5.95% | -1.67% | 27.10% |
| breakout_8 AND reversion_12 | 0.00% | 0.00% | -5.95% | -0.00% | 0.00% |
| breakout_8 + reversion_12 | -4.08% | -16.34% | -5.95% | -1.56% | 25.40% |
| breakout_8 AND volume_26 | 0.00% | -1.66% | -5.95% | -0.08% | 1.31% |
| breakout_8 + volume_26 | -0.67% | -11.89% | -5.95% | -0.83% | 13.49% |
| reversion_12 AND volume_26 | -1.99% | -4.42% | -5.95% | -0.16% | 2.62% |
| reversion_12 + volume_26 | -4.18% | -10.98% | -5.95% | -1.14% | 18.46% |
| ema_12_26 | -0.54% | -2.60% | -5.95% | -2.72% | 44.50% |
| macd_12_26_9 | 5.52% | 2.90% | -5.95% | -1.77% | 28.80% |
| rsi_14_recovery | -1.69% | -6.92% | -5.95% | -0.21% | 3.40% |
| bollinger_20_reentry | -0.55% | -4.64% | -5.95% | -0.16% | 2.62% |
| donchian_20 | 1.17% | -6.59% | -5.95% | -0.45% | 7.33% |
| atr_14_breakout | 1.31% | -4.88% | -5.95% | -0.29% | 4.71% |
| session_vwap | 1.63% | -6.17% | -5.95% | -2.92% | 47.91% |
| obv_20 | -5.98% | -14.28% | -5.95% | -2.06% | 33.51% |
| stochastic_14_3_recovery | -1.40% | -13.80% | -5.95% | -0.52% | 8.38% |
| mfi_14_recovery | 0.33% | -0.93% | -5.95% | -0.05% | 0.79% |
| adx_14_trend | -2.56% | -7.35% | -5.95% | -1.91% | 31.15% |
| aroon_25_trend | 3.90% | -0.79% | -5.95% | -1.77% | 28.80% |
| cci_20_momentum | 1.28% | -5.70% | -5.95% | -1.45% | 23.56% |
| williams_14_recovery | -2.03% | -10.30% | -5.95% | -0.34% | 5.50% |
| cmf_20_accumulation | 2.42% | -1.37% | -5.95% | -1.77% | 28.80% |
| chaikin_3_10 | -3.27% | -7.24% | -5.95% | -2.10% | 34.29% |
| roc_10_momentum | -2.21% | -8.56% | -5.95% | -0.92% | 14.92% |
| trix_15_trend | -1.73% | -4.98% | -5.95% | -2.09% | 34.03% |
| keltner_20_breakout | 0.76% | -2.97% | -5.95% | -0.58% | 9.42% |
| opening_range_30m | 0.41% | -3.72% | -5.95% | -1.61% | 26.18% |

동일 구간·초기 자금, 종료 시 청산 비용 포함. 노출 맞춤은 사후 설명용이며 v2 실제 계좌 성과가 아닙니다.
[낙폭 분해·비용 영향·전체 구간](JNJ/comparison.json)

[v1 전체 기록](JNJ/accounts.json) · [v2 전체 기록](JNJ/accounts-v2.json)

## CAT 계좌

| 모델 | 전략 | 평가액 USD | 손익 USD | 최근 매매·이유 |
|---|---|---:|---:|---|
| v1 | cash | 10000.00 | 0.00 | 대기 /  / 새 신호 대기 |
| v1 | buy_hold | 9987.71 | -12.29 | buy /  / buy_hold: prior completed bar target 100%; next bar open simulation |
| v1 | trend_8_26 | 9987.71 | -12.29 | buy /  / trend_8_26: prior completed bar target 100%; next bar open simulation |
| v1 | momentum_26 | 9907.50 | -92.50 | buy /  / momentum_26: prior completed bar target 100%; next bar open simulation |
| v1 | breakout_8 | 9871.06 | -128.94 | buy /  / breakout_8: prior completed bar target 100%; next bar open simulation |
| v1 | reversion_12 | 9928.06 | -71.94 | sell /  / reversion_12: prior completed bar target 0%; next bar open simulation |
| v1 | volume_26 | 10000.00 | 0.00 | 대기 /  / 새 신호 대기 |
| v1 | trend_8_26 AND momentum_26 | 9907.50 | -92.50 | buy /  / trend_8_26 AND momentum_26: prior completed bar target 100%; next bar open simulation |
| v1 | trend_8_26 + momentum_26 | 9947.69 | -52.31 | buy /  / trend_8_26 + momentum_26: prior completed bar target 100%; next bar open simulation |
| v1 | trend_8_26 AND breakout_8 | 9871.06 | -128.94 | buy /  / trend_8_26 AND breakout_8: prior completed bar target 100%; next bar open simulation |
| v1 | trend_8_26 + breakout_8 | 9929.42 | -70.58 | buy /  / trend_8_26 + breakout_8: prior completed bar target 100%; next bar open simulation |
| v1 | trend_8_26 AND reversion_12 | 9928.06 | -71.94 | sell /  / trend_8_26 AND reversion_12: prior completed bar target 0%; next bar open simulation |
| v1 | trend_8_26 + reversion_12 | 9957.97 | -42.03 | sell /  / trend_8_26 + reversion_12: prior completed bar target 50%; next bar open simulation |
| v1 | trend_8_26 AND volume_26 | 10000.00 | 0.00 | 대기 /  / 새 신호 대기 |
| v1 | trend_8_26 + volume_26 | 9993.94 | -6.06 | sell /  / trend_8_26 + volume_26: prior completed bar target 50%; next bar open simulation |
| v1 | momentum_26 AND breakout_8 | 9871.06 | -128.94 | buy /  / momentum_26 AND breakout_8: prior completed bar target 100%; next bar open simulation |
| v1 | momentum_26 + breakout_8 | 9889.31 | -110.69 | buy /  / momentum_26 + breakout_8: prior completed bar target 100%; next bar open simulation |
| v1 | momentum_26 AND reversion_12 | 9928.06 | -71.94 | sell /  / momentum_26 AND reversion_12: prior completed bar target 0%; next bar open simulation |
| v1 | momentum_26 + reversion_12 | 9917.83 | -82.17 | sell /  / momentum_26 + reversion_12: prior completed bar target 50%; next bar open simulation |
| v1 | momentum_26 AND volume_26 | 10000.00 | 0.00 | 대기 /  / 새 신호 대기 |
| v1 | momentum_26 + volume_26 | 9953.66 | -46.34 | sell /  / momentum_26 + volume_26: prior completed bar target 50%; next bar open simulation |
| v1 | breakout_8 AND reversion_12 | 10000.00 | 0.00 | 대기 /  / 새 신호 대기 |
| v1 | breakout_8 + reversion_12 | 9899.46 | -100.54 | buy /  / breakout_8 + reversion_12: prior completed bar target 50%; next bar open simulation |
| v1 | breakout_8 AND volume_26 | 10000.00 | 0.00 | 대기 /  / 새 신호 대기 |
| v1 | breakout_8 + volume_26 | 9935.30 | -64.70 | buy /  / breakout_8 + volume_26: prior completed bar target 50%; next bar open simulation |
| v1 | reversion_12 AND volume_26 | 10000.00 | 0.00 | 대기 /  / 새 신호 대기 |
| v1 | reversion_12 + volume_26 | 9963.92 | -36.08 | sell /  / reversion_12 + volume_26: prior completed bar target 0%; next bar open simulation |
| v1 | ema_12_26 | 9907.50 | -92.50 | buy /  / EMA12 > EMA26; 조건 충족; EMA12=733.716, EMA26=733.7 |
| v1 | macd_12_26_9 | 9904.18 | -95.82 | sell /  / MACD > 신호선 그리고 MACD > 0; 조건 미충족; MACD=0.746548, signal9=0.752293 |
| v1 | rsi_14_recovery | 10000.00 | 0.00 | 대기 /  / 새 신호 대기 |
| v1 | bollinger_20_reentry | 10000.00 | 0.00 | 대기 /  / 새 신호 대기 |
| v1 | donchian_20 | 9950.83 | -49.17 | sell /  / 종가 > 현재 봉을 제외한 직전 20봉 최고가; 조건 미충족; close=739.81, prior_high20=742.28 |
| v1 | atr_14_breakout | 9871.06 | -128.94 | buy /  / 종가 > 직전 종가 + 직전 ATR14 그리고 종가 > EMA26; 조건 충족; close=739.58, threshold=739.056, prior_ATR14=3.76595, EMA26=736.187 |
| v1 | session_vwap | 9835.67 | -164.33 | buy /  / 종가 > 뉴욕 거래일별 누적 전형가격 VWAP; 조건 충족; close=739.58, session_VWAP=736.206, session_volume=2.76847e+06 |
| v1 | obv_20 | 9835.99 | -164.01 | buy /  / OBV > OBV의 SMA20 그리고 종가 > EMA26; 조건 충족; OBV=-3.06051e+06, OBV_SMA20=-4.26e+06, close=739.58, EMA26=736.187 |
| v1 | stochastic_14_3_recovery | 10000.00 | 0.00 | 대기 /  / 새 신호 대기 |
| v1 | mfi_14_recovery | 10000.00 | 0.00 | 대기 /  / 새 신호 대기 |
| v1 | adx_14_trend | 10000.00 | 0.00 | 대기 /  / 새 신호 대기 |
| v1 | aroon_25_trend | 10031.15 | 31.15 | sell /  / Aroon25 Up > 70 그리고 Down < 30 (동률이면 최신 극값); 조건 미충족; Aroon_up=88, Aroon_down=48 |
| v1 | cci_20_momentum | 10024.78 | 24.78 | sell /  / CCI20 > 100 (전형가격·평균절대편차); 조건 미충족; CCI20=98.8062 |
| v1 | williams_14_recovery | 10000.00 | 0.00 | 대기 /  / 새 신호 대기 |
| v1 | cmf_20_accumulation | 9876.25 | -123.75 | buy /  / Chaikin Money Flow20 > 0.1; 조건 충족; CMF20=0.191828, volume20=3.33969e+06 |
| v1 | chaikin_3_10 | 9680.39 | -319.61 | buy /  / ADL의 EMA3 - EMA10 > 0 그리고 종가 > EMA26; 조건 충족; Chaikin3_10=293683, ADL=-4.91156e+06, close=739.58, EMA26=736.187 |
| v1 | roc_10_momentum | 9963.13 | -36.87 | sell /  / 10봉 ROC > 1% 그리고 종가 > EMA26; 조건 미충족; ROC10_percent=-0.134597, close=734.53, EMA26=735.486 |
| v1 | trix_15_trend | 9690.14 | -309.86 | buy /  / 15봉 삼중 EMA의 1봉 변화율 TRIX > 0 그리고 종가 > EMA26; 조건 충족; TRIX15_percent=0.0196284, close=739.58, EMA26=736.187 |
| v1 | keltner_20_breakout | 10000.00 | 0.00 | 대기 /  / 새 신호 대기 |
| v1 | opening_range_30m | 10040.71 | 40.71 | sell /  / 뉴욕 09:30·09:45 두 완료 봉 최고가를 10:00 이후 종가가 돌파; 자료 부족·변동폭 또는 거래량 없음: 대기; close=740.21 |
| v2 | cash | 10000.00 | 0.00 | 대기 /  / 새 신호 대기 |
| v2 | buy_hold | 9185.44 | -814.56 | 중단: 손실 한도 / buy / partial / 직전 완료 봉 목표 비중 100%; 다음 봉 시가 가정 |
| v2 | trend_8_26 | 9911.53 | -88.47 | buy / partial / 직전 완료 봉 목표 비중 100%; 다음 봉 시가 가정 |
| v2 | momentum_26 | 9920.96 | -79.04 | buy / partial / 직전 완료 봉 목표 비중 100%; 다음 봉 시가 가정 |
| v2 | breakout_8 | 9693.45 | -306.55 | buy / partial / 직전 완료 봉 목표 비중 100%; 다음 봉 시가 가정 |
| v2 | reversion_12 | 9057.16 | -942.84 | 중단: 손실 한도 / buy / partial / 직전 완료 봉 목표 비중 100%; 다음 봉 시가 가정 |
| v2 | volume_26 | 9316.19 | -683.81 | 중단: 손실 한도 / buy / partial / 직전 완료 봉 목표 비중 100%; 다음 봉 시가 가정 |
| v2 | trend_8_26 AND momentum_26 | 9949.69 | -50.31 | buy / partial / 직전 완료 봉 목표 비중 100%; 다음 봉 시가 가정 |
| v2 | trend_8_26 + momentum_26 | 9916.41 | -83.59 | buy / partial / 직전 완료 봉 목표 비중 100%; 다음 봉 시가 가정 |
| v2 | trend_8_26 AND breakout_8 | 9786.62 | -213.38 | buy / partial / 직전 완료 봉 목표 비중 100%; 다음 봉 시가 가정 |
| v2 | trend_8_26 + breakout_8 | 9802.36 | -197.64 | buy / partial / 직전 완료 봉 목표 비중 100%; 다음 봉 시가 가정 |
| v2 | trend_8_26 AND reversion_12 | 9738.62 | -261.38 | sell / filled / 직전 완료 봉 목표 비중 0%; 다음 봉 시가 가정 |
| v2 | trend_8_26 + reversion_12 | 9581.39 | -418.61 | sell / filled / 직전 완료 봉 목표 비중 50%; 다음 봉 시가 가정 |
| v2 | trend_8_26 AND volume_26 | 10035.44 | 35.44 | sell / filled / 직전 완료 봉 목표 비중 0%; 다음 봉 시가 가정 |
| v2 | trend_8_26 + volume_26 | 9626.72 | -373.28 | sell / filled / 직전 완료 봉 목표 비중 50%; 다음 봉 시가 가정 |
| v2 | momentum_26 AND breakout_8 | 9845.83 | -154.17 | buy / partial / 직전 완료 봉 목표 비중 100%; 다음 봉 시가 가정 |
| v2 | momentum_26 + breakout_8 | 9806.78 | -193.22 | buy / partial / 직전 완료 봉 목표 비중 100%; 다음 봉 시가 가정 |
| v2 | momentum_26 AND reversion_12 | 9797.81 | -202.19 | sell / filled / 직전 완료 봉 목표 비중 0%; 다음 봉 시가 가정 |
| v2 | momentum_26 + reversion_12 | 9585.86 | -414.14 | sell / filled / 직전 완료 봉 목표 비중 50%; 다음 봉 시가 가정 |
| v2 | momentum_26 AND volume_26 | 10048.78 | 48.78 | sell / filled / 직전 완료 봉 목표 비중 0%; 다음 봉 시가 가정 |
| v2 | momentum_26 + volume_26 | 9651.48 | -348.52 | sell / filled / 직전 완료 봉 목표 비중 50%; 다음 봉 시가 가정 |
| v2 | breakout_8 AND reversion_12 | 10000.00 | 0.00 | 대기 /  / 새 신호 대기 |
| v2 | breakout_8 + reversion_12 | 9610.18 | -389.82 | 중단: 손실 한도 / sell / filled / 직전 완료 봉 목표 비중 0%; 다음 봉 시가 가정 |
| v2 | breakout_8 AND volume_26 | 9998.69 | -1.31 | sell / filled / 직전 완료 봉 목표 비중 0%; 다음 봉 시가 가정 |
| v2 | breakout_8 + volume_26 | 9540.29 | -459.71 | buy / filled / 직전 완료 봉 목표 비중 50%; 다음 봉 시가 가정 |
| v2 | reversion_12 AND volume_26 | 9251.74 | -748.26 | 중단: 손실 한도 / buy / partial / 직전 완료 봉 목표 비중 100%; 다음 봉 시가 가정 |
| v2 | reversion_12 + volume_26 | 9391.32 | -608.68 | 중단: 손실 한도 / sell / filled / 직전 완료 봉 목표 비중 50%; 다음 봉 시가 가정 |
| v2 | ema_12_26 | 9906.51 | -93.49 | buy / partial / EMA12 > EMA26; 조건 충족; EMA12=733.716, EMA26=733.7; 직전 완료 봉 목표를 다음 봉 시가에 모의 적용 |
| v2 | macd_12_26_9 | 9902.20 | -97.80 | sell / filled / MACD > 신호선 그리고 MACD > 0; 조건 미충족; MACD=0.746548, signal9=0.752293; 직전 완료 봉 목표를 다음 봉 시가에 모의 적용 |
| v2 | rsi_14_recovery | 10000.00 | 0.00 | 대기 /  / 새 신호 대기 |
| v2 | bollinger_20_reentry | 10000.00 | 0.00 | 대기 /  / 새 신호 대기 |
| v2 | donchian_20 | 9948.84 | -51.16 | sell / filled / 종가 > 현재 봉을 제외한 직전 20봉 최고가; 조건 미충족; close=739.81, prior_high20=742.28; 직전 완료 봉 목표를 다음 봉 시가에 모의 적용 |
| v2 | atr_14_breakout | 9868.10 | -131.90 | buy / partial / 종가 > 직전 종가 + 직전 ATR14 그리고 종가 > EMA26; 조건 충족; close=739.58, threshold=739.056, prior_ATR14=3.76595, EMA26=736.187; 직전 완료 봉 목표를 다음 봉 시가에 모의 적용 |
| v2 | session_vwap | 9830.76 | -169.24 | buy / partial / 종가 > 뉴욕 거래일별 누적 전형가격 VWAP; 조건 충족; close=739.58, session_VWAP=736.206, session_volume=2.76847e+06; 직전 완료 봉 목표를 다음 봉 시가에 모의 적용 |
| v2 | obv_20 | 9831.07 | -168.93 | buy / partial / OBV > OBV의 SMA20 그리고 종가 > EMA26; 조건 충족; OBV=-3.06051e+06, OBV_SMA20=-4.26e+06, close=739.58, EMA26=736.187; 직전 완료 봉 목표를 다음 봉 시가에 모의 적용 |
| v2 | stochastic_14_3_recovery | 10000.00 | 0.00 | 대기 /  / 새 신호 대기 |
| v2 | mfi_14_recovery | 10000.00 | 0.00 | 대기 /  / 새 신호 대기 |
| v2 | adx_14_trend | 10000.00 | 0.00 | 대기 /  / 새 신호 대기 |
| v2 | aroon_25_trend | 10029.14 | 29.14 | sell / filled / Aroon25 Up > 70 그리고 Down < 30 (동률이면 최신 극값); 조건 미충족; Aroon_up=88, Aroon_down=48; 직전 완료 봉 목표를 다음 봉 시가에 모의 적용 |
| v2 | cci_20_momentum | 10022.77 | 22.77 | sell / filled / CCI20 > 100 (전형가격·평균절대편차); 조건 미충족; CCI20=98.8062; 직전 완료 봉 목표를 다음 봉 시가에 모의 적용 |
| v2 | williams_14_recovery | 10000.00 | 0.00 | 대기 /  / 새 신호 대기 |
| v2 | cmf_20_accumulation | 9873.29 | -126.71 | buy / partial / Chaikin Money Flow20 > 0.1; 조건 충족; CMF20=0.191828, volume20=3.33969e+06; 직전 완료 봉 목표를 다음 봉 시가에 모의 적용 |
| v2 | chaikin_3_10 | 9673.61 | -326.39 | 중단: 손실 한도 / buy / partial / ADL의 EMA3 - EMA10 > 0 그리고 종가 > EMA26; 조건 충족; Chaikin3_10=293683, ADL=-4.91156e+06, close=739.58, EMA26=736.187; 직전 완료 봉 목표를 다음 봉 시가에 모의 적용 |
| v2 | roc_10_momentum | 9961.14 | -38.86 | sell / filled / 10봉 ROC > 1% 그리고 종가 > EMA26; 조건 미충족; ROC10_percent=-0.134597, close=734.53, EMA26=735.486; 직전 완료 봉 목표를 다음 봉 시가에 모의 적용 |
| v2 | trix_15_trend | 9683.36 | -316.64 | 중단: 손실 한도 / buy / partial / 15봉 삼중 EMA의 1봉 변화율 TRIX > 0 그리고 종가 > EMA26; 조건 충족; TRIX15_percent=0.0196284, close=739.58, EMA26=736.187; 직전 완료 봉 목표를 다음 봉 시가에 모의 적용 |
| v2 | keltner_20_breakout | 10000.00 | 0.00 | 대기 /  / 새 신호 대기 |
| v2 | opening_range_30m | 10038.70 | 38.70 | sell / filled / 뉴욕 09:30·09:45 두 완료 봉 최고가를 10:00 이후 종가가 돌파; 자료 부족·변동폭 또는 거래량 없음: 대기; close=740.21; 직전 완료 봉 목표를 다음 봉 시가에 모의 적용 |

### 같은 기간의 비용·노출 비교 (사후 연구)

| 전략 | 비용 전 | 비용 후 | 100% 보유 | 같은 평균 노출 보유 | 평균 노출 |
|---|---:|---:|---:|---:|---:|
| cash | 0.00% | 0.00% | -10.86% | -0.00% | 0.00% |
| buy_hold | -10.49% | -10.86% | -10.86% | -10.86% | 100.00% |
| trend_8_26 | -2.00% | -5.64% | -10.86% | -5.55% | 50.52% |
| momentum_26 | -4.87% | -10.68% | -10.86% | -5.38% | 48.95% |
| breakout_8 | -3.78% | -16.58% | -10.86% | -1.65% | 14.92% |
| reversion_12 | -3.43% | -15.93% | -10.86% | -2.92% | 26.44% |
| volume_26 | -2.95% | -10.02% | -10.86% | -0.90% | 8.12% |
| trend_8_26 AND momentum_26 | -2.20% | -7.00% | -10.86% | -4.75% | 43.19% |
| trend_8_26 + momentum_26 | -3.43% | -8.18% | -10.86% | -5.47% | 49.74% |
| trend_8_26 AND breakout_8 | -2.41% | -9.90% | -10.86% | -0.84% | 7.59% |
| trend_8_26 + breakout_8 | -2.86% | -11.07% | -10.86% | -3.61% | 32.73% |
| trend_8_26 AND reversion_12 | 1.26% | -6.11% | -10.86% | -0.87% | 7.85% |
| trend_8_26 + reversion_12 | -2.66% | -10.35% | -10.86% | -4.24% | 38.49% |
| trend_8_26 AND volume_26 | 2.22% | -0.75% | -10.86% | -0.29% | 2.62% |
| trend_8_26 + volume_26 | -2.42% | -7.63% | -10.86% | -3.24% | 29.32% |
| momentum_26 AND breakout_8 | -3.33% | -11.49% | -10.86% | -0.93% | 8.38% |
| momentum_26 + breakout_8 | -4.29% | -13.65% | -10.86% | -3.52% | 31.94% |
| momentum_26 AND reversion_12 | -2.58% | -9.67% | -10.86% | -0.73% | 6.54% |
| momentum_26 + reversion_12 | -4.10% | -12.41% | -10.86% | -4.15% | 37.70% |
| momentum_26 AND volume_26 | 1.58% | -0.53% | -10.86% | -0.17% | 1.57% |
| momentum_26 + volume_26 | -3.86% | -9.57% | -10.86% | -3.15% | 28.54% |
| breakout_8 AND reversion_12 | 0.00% | 0.00% | -10.86% | -0.00% | 0.00% |
| breakout_8 + reversion_12 | -3.55% | -15.35% | -10.86% | -2.29% | 20.69% |
| breakout_8 AND volume_26 | 0.37% | -0.47% | -10.86% | -0.06% | 0.52% |
| breakout_8 + volume_26 | -3.33% | -12.62% | -10.86% | -1.28% | 11.52% |
| reversion_12 AND volume_26 | -1.25% | -5.71% | -10.86% | -0.58% | 5.24% |
| reversion_12 + volume_26 | -3.16% | -12.28% | -10.86% | -1.91% | 17.28% |
| ema_12_26 | -1.45% | -3.50% | -10.86% | -5.52% | 50.26% |
| macd_12_26_9 | -0.77% | -4.85% | -10.86% | -3.41% | 30.89% |
| rsi_14_recovery | -0.96% | -6.22% | -10.86% | -0.38% | 3.40% |
| bollinger_20_reentry | 1.35% | -4.43% | -10.86% | -0.41% | 3.66% |
| donchian_20 | -2.30% | -7.11% | -10.86% | -0.58% | 5.24% |
| atr_14_breakout | -3.01% | -10.07% | -10.86% | -0.55% | 4.97% |
| session_vwap | -1.10% | -13.18% | -10.86% | -5.01% | 45.55% |
| obv_20 | -4.90% | -15.45% | -10.86% | -2.92% | 26.44% |
| stochastic_14_3_recovery | -3.21% | -13.22% | -10.86% | -0.75% | 6.81% |
| mfi_14_recovery | 0.45% | -1.63% | -10.86% | -0.15% | 1.31% |
| adx_14_trend | -3.13% | -5.93% | -10.86% | -1.04% | 9.42% |
| aroon_25_trend | -2.12% | -6.14% | -10.86% | -1.62% | 14.66% |
| cci_20_momentum | -5.75% | -11.87% | -10.86% | -1.77% | 15.97% |
| williams_14_recovery | -1.60% | -10.66% | -10.86% | -0.67% | 6.02% |
| cmf_20_accumulation | -6.09% | -12.93% | -10.86% | -1.97% | 17.80% |
| chaikin_3_10 | -7.12% | -16.37% | -10.86% | -3.84% | 34.82% |
| roc_10_momentum | -1.82% | -7.81% | -10.86% | -1.48% | 13.35% |
| trix_15_trend | -2.21% | -7.41% | -10.86% | -4.30% | 39.01% |
| keltner_20_breakout | -3.35% | -6.15% | -10.86% | -0.32% | 2.88% |
| opening_range_30m | 4.95% | -0.21% | -10.86% | -2.26% | 20.42% |

동일 구간·초기 자금, 종료 시 청산 비용 포함. 노출 맞춤은 사후 설명용이며 v2 실제 계좌 성과가 아닙니다.
[낙폭 분해·비용 영향·전체 구간](CAT/comparison.json)

[v1 전체 기록](CAT/accounts.json) · [v2 전체 기록](CAT/accounts-v2.json)

## WMT 계좌

| 모델 | 전략 | 평가액 USD | 손익 USD | 최근 매매·이유 |
|---|---|---:|---:|---|
| v1 | cash | 10000.00 | 0.00 | 대기 /  / 새 신호 대기 |
| v1 | buy_hold | 10026.91 | 26.91 | buy /  / buy_hold: prior completed bar target 100%; next bar open simulation |
| v1 | trend_8_26 | 9973.31 | -26.69 | buy /  / trend_8_26: prior completed bar target 100%; next bar open simulation |
| v1 | momentum_26 | 9965.42 | -34.58 | buy /  / momentum_26: prior completed bar target 100%; next bar open simulation |
| v1 | breakout_8 | 9923.60 | -76.40 | buy /  / breakout_8: prior completed bar target 100%; next bar open simulation |
| v1 | reversion_12 | 10043.97 | 43.97 | sell /  / reversion_12: prior completed bar target 0%; next bar open simulation |
| v1 | volume_26 | 9979.72 | -20.28 | sell /  / volume_26: prior completed bar target 0%; next bar open simulation |
| v1 | trend_8_26 AND momentum_26 | 9921.79 | -78.21 | buy /  / trend_8_26 AND momentum_26: prior completed bar target 100%; next bar open simulation |
| v1 | trend_8_26 + momentum_26 | 9969.44 | -30.56 | buy /  / trend_8_26 + momentum_26: prior completed bar target 100%; next bar open simulation |
| v1 | trend_8_26 AND breakout_8 | 9969.95 | -30.05 | buy /  / trend_8_26 AND breakout_8: prior completed bar target 100%; next bar open simulation |
| v1 | trend_8_26 + breakout_8 | 9948.40 | -51.60 | buy /  / trend_8_26 + breakout_8: prior completed bar target 100%; next bar open simulation |
| v1 | trend_8_26 AND reversion_12 | 10000.00 | 0.00 | 대기 /  / 새 신호 대기 |
| v1 | trend_8_26 + reversion_12 | 10008.60 | 8.60 | sell /  / trend_8_26 + reversion_12: prior completed bar target 50%; next bar open simulation |
| v1 | trend_8_26 AND volume_26 | 10000.00 | 0.00 | 대기 /  / 새 신호 대기 |
| v1 | trend_8_26 + volume_26 | 9976.45 | -23.55 | sell /  / trend_8_26 + volume_26: prior completed bar target 50%; next bar open simulation |
| v1 | momentum_26 AND breakout_8 | 9969.95 | -30.05 | buy /  / momentum_26 AND breakout_8: prior completed bar target 100%; next bar open simulation |
| v1 | momentum_26 + breakout_8 | 9964.46 | -35.54 | buy /  / momentum_26 + breakout_8: prior completed bar target 100%; next bar open simulation |
| v1 | momentum_26 AND reversion_12 | 10043.97 | 43.97 | sell /  / momentum_26 AND reversion_12: prior completed bar target 0%; next bar open simulation |
| v1 | momentum_26 + reversion_12 | 10004.59 | 4.59 | sell /  / momentum_26 + reversion_12: prior completed bar target 50%; next bar open simulation |
| v1 | momentum_26 AND volume_26 | 10000.00 | 0.00 | 대기 /  / 새 신호 대기 |
| v1 | momentum_26 + volume_26 | 9992.57 | -7.43 | sell /  / momentum_26 + volume_26: prior completed bar target 50%; next bar open simulation |
| v1 | breakout_8 AND reversion_12 | 10000.00 | 0.00 | 대기 /  / 새 신호 대기 |
| v1 | breakout_8 + reversion_12 | 10003.67 | 3.67 | sell /  / breakout_8 + reversion_12: prior completed bar target 50%; next bar open simulation |
| v1 | breakout_8 AND volume_26 | 9979.72 | -20.28 | sell /  / breakout_8 AND volume_26: prior completed bar target 0%; next bar open simulation |
| v1 | breakout_8 + volume_26 | 9951.62 | -48.38 | sell /  / breakout_8 + volume_26: prior completed bar target 50%; next bar open simulation |
| v1 | reversion_12 AND volume_26 | 10000.00 | 0.00 | 대기 /  / 새 신호 대기 |
| v1 | reversion_12 + volume_26 | 10031.90 | 31.90 | sell /  / reversion_12 + volume_26: prior completed bar target 0%; next bar open simulation |
| v1 | ema_12_26 | 10026.91 | 26.91 | buy /  / EMA12 > EMA26; 조건 충족; EMA12=118.245, EMA26=118.045 |
| v1 | macd_12_26_9 | 10000.00 | 0.00 | 대기 /  / 새 신호 대기 |
| v1 | rsi_14_recovery | 10000.00 | 0.00 | 대기 /  / 새 신호 대기 |
| v1 | bollinger_20_reentry | 10000.00 | 0.00 | 대기 /  / 새 신호 대기 |
| v1 | donchian_20 | 10000.00 | 0.00 | 대기 /  / 새 신호 대기 |
| v1 | atr_14_breakout | 9979.72 | -20.28 | sell /  / 종가 > 직전 종가 + 직전 ATR14 그리고 종가 > EMA26; 조건 미충족; close=119.375, threshold=119.607, prior_ATR14=0.486823, EMA26=118.217 |
| v1 | session_vwap | 9809.65 | -190.35 | buy /  / 종가 > 뉴욕 거래일별 누적 전형가격 VWAP; 조건 충족; close=118.83, session_VWAP=118.814, session_volume=1.00902e+07 |
| v1 | obv_20 | 9928.89 | -71.11 | buy /  / OBV > OBV의 SMA20 그리고 종가 > EMA26; 조건 충족; OBV=1.98141e+07, OBV_SMA20=1.94121e+07, close=118.83, EMA26=118.531 |
| v1 | stochastic_14_3_recovery | 9979.72 | -20.28 | sell /  / 직전 %K14 < 20에서 %K14가 %D3 상향 돌파 (한 봉 목표); 조건 미충족; K14=93.8952, D3=60.8222, previous_K14=82.4242, previous_D3=34.5012 |
| v1 | mfi_14_recovery | 10000.00 | 0.00 | 대기 /  / 새 신호 대기 |
| v1 | adx_14_trend | 9991.69 | -8.31 | sell /  / Wilder ADX14 >= 25 그리고 +DI14 > -DI14; 조건 미충족; ADX14=24.5142, plus_DI14=24.7537, minus_DI14=21.6519 |
| v1 | aroon_25_trend | 10000.00 | 0.00 | 대기 /  / 새 신호 대기 |
| v1 | cci_20_momentum | 9932.96 | -67.04 | sell /  / CCI20 > 100 (전형가격·평균절대편차); 조건 미충족; CCI20=99.1325 |
| v1 | williams_14_recovery | 9979.72 | -20.28 | sell /  / 직전 Williams %R14 < -80, 현재 >= -80 (한 봉 목표); 조건 미충족; Williams_R14=-6.10484, previous_R14=-17.5758 |
| v1 | cmf_20_accumulation | 10000.00 | 0.00 | 대기 /  / 새 신호 대기 |
| v1 | chaikin_3_10 | 9803.51 | -196.49 | buy /  / ADL의 EMA3 - EMA10 > 0 그리고 종가 > EMA26; 조건 충족; Chaikin3_10=85268.3, ADL=1.95276e+07, close=118.535, EMA26=118.469 |
| v1 | roc_10_momentum | 10000.00 | 0.00 | 대기 /  / 새 신호 대기 |
| v1 | trix_15_trend | 9893.03 | -106.97 | buy /  / 15봉 삼중 EMA의 1봉 변화율 TRIX > 0 그리고 종가 > EMA26; 조건 충족; TRIX15_percent=0.026499, close=118.535, EMA26=118.469 |
| v1 | keltner_20_breakout | 10000.00 | 0.00 | 대기 /  / 새 신호 대기 |
| v1 | opening_range_30m | 10000.00 | 0.00 | 대기 /  / 새 신호 대기 |
| v2 | cash | 10000.00 | 0.00 | 대기 /  / 새 신호 대기 |
| v2 | buy_hold | 10623.42 | 623.42 | buy / partial / 직전 완료 봉 목표 비중 100%; 다음 봉 시가 가정 |
| v2 | trend_8_26 | 10381.80 | 381.80 | buy / partial / 직전 완료 봉 목표 비중 100%; 다음 봉 시가 가정 |
| v2 | momentum_26 | 10380.58 | 380.58 | buy / partial / 직전 완료 봉 목표 비중 100%; 다음 봉 시가 가정 |
| v2 | breakout_8 | 9885.55 | -114.45 | buy / partial / 직전 완료 봉 목표 비중 100%; 다음 봉 시가 가정 |
| v2 | reversion_12 | 9953.01 | -46.99 | sell / filled / 직전 완료 봉 목표 비중 0%; 다음 봉 시가 가정 |
| v2 | volume_26 | 9943.08 | -56.92 | sell / filled / 직전 완료 봉 목표 비중 0%; 다음 봉 시가 가정 |
| v2 | trend_8_26 AND momentum_26 | 10326.11 | 326.11 | buy / partial / 직전 완료 봉 목표 비중 100%; 다음 봉 시가 가정 |
| v2 | trend_8_26 + momentum_26 | 10381.22 | 381.22 | buy / partial / 직전 완료 봉 목표 비중 100%; 다음 봉 시가 가정 |
| v2 | trend_8_26 AND breakout_8 | 10057.23 | 57.23 | buy / partial / 직전 완료 봉 목표 비중 100%; 다음 봉 시가 가정 |
| v2 | trend_8_26 + breakout_8 | 10131.02 | 131.02 | buy / partial / 직전 완료 봉 목표 비중 100%; 다음 봉 시가 가정 |
| v2 | trend_8_26 AND reversion_12 | 9808.74 | -191.26 | sell / filled / 직전 완료 봉 목표 비중 0%; 다음 봉 시가 가정 |
| v2 | trend_8_26 + reversion_12 | 10166.61 | 166.61 | sell / filled / 직전 완료 봉 목표 비중 50%; 다음 봉 시가 가정 |
| v2 | trend_8_26 AND volume_26 | 9949.23 | -50.77 | sell / filled / 직전 완료 봉 목표 비중 0%; 다음 봉 시가 가정 |
| v2 | trend_8_26 + volume_26 | 10161.46 | 161.46 | sell / filled / 직전 완료 봉 목표 비중 50%; 다음 봉 시가 가정 |
| v2 | momentum_26 AND breakout_8 | 9933.71 | -66.29 | buy / partial / 직전 완료 봉 목표 비중 100%; 다음 봉 시가 가정 |
| v2 | momentum_26 + breakout_8 | 10151.81 | 151.81 | buy / partial / 직전 완료 봉 목표 비중 100%; 다음 봉 시가 가정 |
| v2 | momentum_26 AND reversion_12 | 9872.00 | -128.00 | sell / filled / 직전 완료 봉 목표 비중 0%; 다음 봉 시가 가정 |
| v2 | momentum_26 + reversion_12 | 10208.82 | 208.82 | sell / filled / 직전 완료 봉 목표 비중 50%; 다음 봉 시가 가정 |
| v2 | momentum_26 AND volume_26 | 9913.82 | -86.18 | sell / filled / 직전 완료 봉 목표 비중 0%; 다음 봉 시가 가정 |
| v2 | momentum_26 + volume_26 | 10182.38 | 182.38 | sell / filled / 직전 완료 봉 목표 비중 50%; 다음 봉 시가 가정 |
| v2 | breakout_8 AND reversion_12 | 10000.00 | 0.00 | 대기 /  / 새 신호 대기 |
| v2 | breakout_8 + reversion_12 | 9962.22 | -37.78 | sell / filled / 직전 완료 봉 목표 비중 50%; 다음 봉 시가 가정 |
| v2 | breakout_8 AND volume_26 | 9928.06 | -71.94 | sell / filled / 직전 완료 봉 목표 비중 0%; 다음 봉 시가 가정 |
| v2 | breakout_8 + volume_26 | 9915.65 | -84.35 | sell / filled / 직전 완료 봉 목표 비중 50%; 다음 봉 시가 가정 |
| v2 | reversion_12 AND volume_26 | 10009.78 | 9.78 | sell / filled / 직전 완료 봉 목표 비중 0%; 다음 봉 시가 가정 |
| v2 | reversion_12 + volume_26 | 9968.93 | -31.07 | sell / filled / 직전 완료 봉 목표 비중 0%; 다음 봉 시가 가정 |
| v2 | ema_12_26 | 10025.91 | 25.91 | buy / partial / EMA12 > EMA26; 조건 충족; EMA12=118.245, EMA26=118.045; 직전 완료 봉 목표를 다음 봉 시가에 모의 적용 |
| v2 | macd_12_26_9 | 10000.00 | 0.00 | 대기 /  / 새 신호 대기 |
| v2 | rsi_14_recovery | 10000.00 | 0.00 | 대기 /  / 새 신호 대기 |
| v2 | bollinger_20_reentry | 10000.00 | 0.00 | 대기 /  / 새 신호 대기 |
| v2 | donchian_20 | 10000.00 | 0.00 | 대기 /  / 새 신호 대기 |
| v2 | atr_14_breakout | 9977.72 | -22.28 | sell / filled / 종가 > 직전 종가 + 직전 ATR14 그리고 종가 > EMA26; 조건 미충족; close=119.375, threshold=119.607, prior_ATR14=0.486823, EMA26=118.217; 직전 완료 봉 목표를 다음 봉 시가에 모의 적용 |
| v2 | session_vwap | 9804.75 | -195.25 | buy / partial / 종가 > 뉴욕 거래일별 누적 전형가격 VWAP; 조건 충족; close=118.83, session_VWAP=118.814, session_volume=1.00902e+07; 직전 완료 봉 목표를 다음 봉 시가에 모의 적용 |
| v2 | obv_20 | 9925.92 | -74.08 | buy / partial / OBV > OBV의 SMA20 그리고 종가 > EMA26; 조건 충족; OBV=1.98141e+07, OBV_SMA20=1.94121e+07, close=118.83, EMA26=118.531; 직전 완료 봉 목표를 다음 봉 시가에 모의 적용 |
| v2 | stochastic_14_3_recovery | 9977.72 | -22.28 | sell / filled / 직전 %K14 < 20에서 %K14가 %D3 상향 돌파 (한 봉 목표); 조건 미충족; K14=93.8952, D3=60.8222, previous_K14=82.4242, previous_D3=34.5012; 직전 완료 봉 목표를 다음 봉 시가에 모의 적용 |
| v2 | mfi_14_recovery | 10000.00 | 0.00 | 대기 /  / 새 신호 대기 |
| v2 | adx_14_trend | 9989.70 | -10.30 | sell / filled / Wilder ADX14 >= 25 그리고 +DI14 > -DI14; 조건 미충족; ADX14=24.5142, plus_DI14=24.7537, minus_DI14=21.6519; 직전 완료 봉 목표를 다음 봉 시가에 모의 적용 |
| v2 | aroon_25_trend | 10000.00 | 0.00 | 대기 /  / 새 신호 대기 |
| v2 | cci_20_momentum | 9930.98 | -69.02 | sell / filled / CCI20 > 100 (전형가격·평균절대편차); 조건 미충족; CCI20=99.1325; 직전 완료 봉 목표를 다음 봉 시가에 모의 적용 |
| v2 | williams_14_recovery | 9977.72 | -22.28 | sell / filled / 직전 Williams %R14 < -80, 현재 >= -80 (한 봉 목표); 조건 미충족; Williams_R14=-6.10484, previous_R14=-17.5758; 직전 완료 봉 목표를 다음 봉 시가에 모의 적용 |
| v2 | cmf_20_accumulation | 10000.00 | 0.00 | 대기 /  / 새 신호 대기 |
| v2 | chaikin_3_10 | 9798.61 | -201.39 | buy / partial / ADL의 EMA3 - EMA10 > 0 그리고 종가 > EMA26; 조건 충족; Chaikin3_10=85268.3, ADL=1.95276e+07, close=118.535, EMA26=118.469; 직전 완료 봉 목표를 다음 봉 시가에 모의 적용 |
| v2 | roc_10_momentum | 10000.00 | 0.00 | 대기 /  / 새 신호 대기 |
| v2 | trix_15_trend | 9890.06 | -109.94 | buy / partial / 15봉 삼중 EMA의 1봉 변화율 TRIX > 0 그리고 종가 > EMA26; 조건 충족; TRIX15_percent=0.026499, close=118.535, EMA26=118.469; 직전 완료 봉 목표를 다음 봉 시가에 모의 적용 |
| v2 | keltner_20_breakout | 10000.00 | 0.00 | 대기 /  / 새 신호 대기 |
| v2 | opening_range_30m | 10000.00 | 0.00 | 대기 /  / 새 신호 대기 |

### 같은 기간의 비용·노출 비교 (사후 연구)

| 전략 | 비용 전 | 비용 후 | 100% 보유 | 같은 평균 노출 보유 | 평균 노출 |
|---|---:|---:|---:|---:|---:|
| cash | 0.00% | 0.00% | 9.55% | 0.00% | 0.00% |
| buy_hold | 10.01% | 9.55% | 9.55% | 9.55% | 100.00% |
| trend_8_26 | 9.29% | 6.12% | 9.55% | 6.62% | 69.63% |
| momentum_26 | 7.40% | 2.55% | 9.55% | 6.65% | 69.90% |
| breakout_8 | 5.51% | -11.55% | 9.55% | 2.52% | 26.70% |
| reversion_12 | 4.02% | -5.96% | 9.55% | 1.58% | 16.75% |
| volume_26 | -0.20% | -5.50% | 9.55% | 0.52% | 5.50% |
| trend_8_26 AND momentum_26 | 8.84% | 3.92% | 9.55% | 6.02% | 63.35% |
| trend_8_26 + momentum_26 | 8.35% | 4.33% | 9.55% | 6.63% | 69.77% |
| trend_8_26 AND breakout_8 | 6.98% | -6.86% | 9.55% | 2.13% | 22.51% |
| trend_8_26 + breakout_8 | 7.40% | -3.11% | 9.55% | 4.57% | 48.17% |
| trend_8_26 AND reversion_12 | 0.42% | -4.91% | 9.55% | 0.64% | 6.81% |
| trend_8_26 + reversion_12 | 6.66% | 0.12% | 9.55% | 4.09% | 43.20% |
| trend_8_26 AND volume_26 | 1.13% | -1.39% | 9.55% | 0.20% | 2.09% |
| trend_8_26 + volume_26 | 4.48% | 0.58% | 9.55% | 3.56% | 37.57% |
| momentum_26 AND breakout_8 | 5.64% | -8.42% | 9.55% | 2.23% | 23.56% |
| momentum_26 + breakout_8 | 6.47% | -4.35% | 9.55% | 4.58% | 48.30% |
| momentum_26 AND reversion_12 | 1.36% | -4.43% | 9.55% | 0.72% | 7.59% |
| momentum_26 + reversion_12 | 5.74% | 0.09% | 9.55% | 4.10% | 43.33% |
| momentum_26 AND volume_26 | 0.44% | -3.69% | 9.55% | 0.27% | 2.88% |
| momentum_26 + volume_26 | 3.57% | -1.33% | 9.55% | 3.57% | 37.70% |
| breakout_8 AND reversion_12 | 0.00% | 0.00% | 9.55% | 0.00% | 0.00% |
| breakout_8 + reversion_12 | 4.79% | -8.21% | 9.55% | 2.05% | 21.74% |
| breakout_8 AND volume_26 | 1.29% | -0.82% | 9.55% | 0.15% | 1.57% |
| breakout_8 + volume_26 | 2.65% | -7.99% | 9.55% | 1.52% | 16.11% |
| reversion_12 AND volume_26 | -0.51% | -2.99% | 9.55% | 0.22% | 2.36% |
| reversion_12 + volume_26 | 1.90% | -5.33% | 9.55% | 1.05% | 11.13% |
| ema_12_26 | 9.16% | 7.79% | 9.55% | 6.67% | 70.16% |
| macd_12_26_9 | 8.10% | 4.53% | 9.55% | 3.39% | 35.86% |
| rsi_14_recovery | -0.68% | -2.74% | 9.55% | 0.12% | 1.31% |
| bollinger_20_reentry | 0.93% | -2.41% | 9.55% | 0.20% | 2.09% |
| donchian_20 | 4.80% | -7.99% | 9.55% | 1.31% | 13.87% |
| atr_14_breakout | -0.36% | -10.29% | 9.55% | 0.74% | 7.85% |
| session_vwap | 7.09% | -3.59% | 9.55% | 5.64% | 59.42% |
| obv_20 | 8.22% | 0.34% | 9.55% | 5.32% | 56.02% |
| stochastic_14_3_recovery | 1.43% | -9.06% | 9.55% | 0.64% | 6.81% |
| mfi_14_recovery | 0.02% | -0.81% | 9.55% | 0.05% | 0.52% |
| adx_14_trend | 8.84% | 6.13% | 9.55% | 4.79% | 50.52% |
| aroon_25_trend | 6.87% | 2.04% | 9.55% | 2.97% | 31.41% |
| cci_20_momentum | 7.75% | -0.52% | 9.55% | 3.12% | 32.98% |
| williams_14_recovery | 0.23% | -8.61% | 9.55% | 0.54% | 5.76% |
| cmf_20_accumulation | 9.42% | 1.46% | 9.55% | 3.54% | 37.43% |
| chaikin_3_10 | 5.70% | -2.00% | 9.55% | 5.12% | 53.93% |
| roc_10_momentum | -0.29% | -5.58% | 9.55% | 1.46% | 15.45% |
| trix_15_trend | 8.09% | 5.40% | 9.55% | 6.27% | 65.97% |
| keltner_20_breakout | 6.87% | -0.08% | 9.55% | 2.60% | 27.49% |
| opening_range_30m | 10.49% | 5.06% | 9.55% | 3.32% | 35.08% |

동일 구간·초기 자금, 종료 시 청산 비용 포함. 노출 맞춤은 사후 설명용이며 v2 실제 계좌 성과가 아닙니다.
[낙폭 분해·비용 영향·전체 구간](WMT/comparison.json)

[v1 전체 기록](WMT/accounts.json) · [v2 전체 기록](WMT/accounts-v2.json)
