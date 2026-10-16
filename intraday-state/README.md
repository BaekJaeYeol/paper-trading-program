# 모의투자 운영 현황

[PC·서버 장애 진단과 복구 방법](https://github.com/BaekJaeYeol/paper-trading-program/blob/main/investment-lab/docs/failure-recovery.md)

이번 실행 복구: {}

완료 봉 확인 주기: 기록 0/6회 · 기록 없는 예정 6회 · 아직 판정 전 20회 · 주의: 예약 시작 지연 또는 실행·저장 누락을 확인하세요.

[주기 판정 기준](https://github.com/BaekJaeYeol/paper-trading-program/blob/main/investment-lab/docs/session-coverage.md)

최근 확인: 2026-10-16T15:22:00.386566+00:00 (UTC)
다음 15분 확인 목표 (세션 실행 중에만 적용): 2026-10-16T15:37:00+00:00 (UTC, 실행 지연 가능)

실제 주문 없음. v1 기존 계좌와 v2 새 계좌의 시작일이 다르므로 수익률을 직접 우열 비교하지 마세요.
v2는 다음 봉 시가에 비용·스프레드·직전 거래량 제한을 적용한 가상 체결입니다. 미체결 잔량은 만료됩니다.

| 종목 | 상태 | 최근 성공 UTC | 마지막 완료 봉 UTC | 이번 새 봉 |
|---|---|---|---|---|
| SPY | updated | 2026-10-16T15:22:00.386566+00:00 | 2026-10-16T15:00:00+00:00 | 1 |
| QQQ | updated | 2026-10-16T15:22:00.386566+00:00 | 2026-10-16T15:00:00+00:00 | 1 |
| IWM | updated | 2026-10-16T15:22:00.386566+00:00 | 2026-10-16T15:00:00+00:00 | 1 |
| DIA | updated | 2026-10-16T15:22:00.386566+00:00 | 2026-10-16T15:00:00+00:00 | 1 |
| MSFT | updated | 2026-10-16T15:22:00.386566+00:00 | 2026-10-16T15:00:00+00:00 | 1 |
| JPM | updated | 2026-10-16T15:22:00.386566+00:00 | 2026-10-16T15:00:00+00:00 | 1 |
| XOM | updated | 2026-10-16T15:22:00.386566+00:00 | 2026-10-16T15:00:00+00:00 | 1 |
| JNJ | updated | 2026-10-16T15:22:00.386566+00:00 | 2026-10-16T15:00:00+00:00 | 1 |
| CAT | updated | 2026-10-16T15:22:00.386566+00:00 | 2026-10-16T15:00:00+00:00 | 1 |
| WMT | updated | 2026-10-16T15:22:00.386566+00:00 | 2026-10-16T15:00:00+00:00 | 1 |

이번 실행 소요: 43.36초
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
| v1 | buy_hold | 9936.34 | -63.66 | buy /  / buy_hold: prior completed bar target 100%; next bar open simulation |
| v1 | trend_8_26 | 9936.34 | -63.66 | buy /  / trend_8_26: prior completed bar target 100%; next bar open simulation |
| v1 | momentum_26 | 9936.34 | -63.66 | buy /  / momentum_26: prior completed bar target 100%; next bar open simulation |
| v1 | breakout_8 | 10000.00 | 0.00 | 대기 /  / 새 신호 대기 |
| v1 | reversion_12 | 10000.00 | 0.00 | 대기 /  / 새 신호 대기 |
| v1 | volume_26 | 9959.52 | -40.48 | buy /  / volume_26: prior completed bar target 100%; next bar open simulation |
| v1 | trend_8_26 AND momentum_26 | 9936.34 | -63.66 | buy /  / trend_8_26 AND momentum_26: prior completed bar target 100%; next bar open simulation |
| v1 | trend_8_26 + momentum_26 | 9936.34 | -63.66 | buy /  / trend_8_26 + momentum_26: prior completed bar target 100%; next bar open simulation |
| v1 | trend_8_26 AND breakout_8 | 10000.00 | 0.00 | 대기 /  / 새 신호 대기 |
| v1 | trend_8_26 + breakout_8 | 9968.09 | -31.91 | buy /  / trend_8_26 + breakout_8: prior completed bar target 50%; next bar open simulation |
| v1 | trend_8_26 AND reversion_12 | 10000.00 | 0.00 | 대기 /  / 새 신호 대기 |
| v1 | trend_8_26 + reversion_12 | 9968.09 | -31.91 | buy /  / trend_8_26 + reversion_12: prior completed bar target 50%; next bar open simulation |
| v1 | trend_8_26 AND volume_26 | 9959.52 | -40.48 | buy /  / trend_8_26 AND volume_26: prior completed bar target 100%; next bar open simulation |
| v1 | trend_8_26 + volume_26 | 9947.89 | -52.11 | buy /  / trend_8_26 + volume_26: prior completed bar target 100%; next bar open simulation |
| v1 | momentum_26 AND breakout_8 | 10000.00 | 0.00 | 대기 /  / 새 신호 대기 |
| v1 | momentum_26 + breakout_8 | 9968.09 | -31.91 | buy /  / momentum_26 + breakout_8: prior completed bar target 50%; next bar open simulation |
| v1 | momentum_26 AND reversion_12 | 10000.00 | 0.00 | 대기 /  / 새 신호 대기 |
| v1 | momentum_26 + reversion_12 | 9968.09 | -31.91 | buy /  / momentum_26 + reversion_12: prior completed bar target 50%; next bar open simulation |
| v1 | momentum_26 AND volume_26 | 9959.52 | -40.48 | buy /  / momentum_26 AND volume_26: prior completed bar target 100%; next bar open simulation |
| v1 | momentum_26 + volume_26 | 9947.89 | -52.11 | buy /  / momentum_26 + volume_26: prior completed bar target 100%; next bar open simulation |
| v1 | breakout_8 AND reversion_12 | 10000.00 | 0.00 | 대기 /  / 새 신호 대기 |
| v1 | breakout_8 + reversion_12 | 10000.00 | 0.00 | 대기 /  / 새 신호 대기 |
| v1 | breakout_8 AND volume_26 | 10000.00 | 0.00 | 대기 /  / 새 신호 대기 |
| v1 | breakout_8 + volume_26 | 9979.72 | -20.28 | buy /  / breakout_8 + volume_26: prior completed bar target 50%; next bar open simulation |
| v1 | reversion_12 AND volume_26 | 10000.00 | 0.00 | 대기 /  / 새 신호 대기 |
| v1 | reversion_12 + volume_26 | 9979.72 | -20.28 | buy /  / reversion_12 + volume_26: prior completed bar target 50%; next bar open simulation |
| v1 | ema_12_26 | 9936.34 | -63.66 | buy /  / EMA12 > EMA26; 조건 충족; EMA12=771.059, EMA26=770.546 |
| v1 | macd_12_26_9 | 9936.34 | -63.66 | buy /  / MACD > 신호선 그리고 MACD > 0; 조건 충족; MACD=0.512991, signal9=0.254322 |
| v1 | rsi_14_recovery | 10000.00 | 0.00 | 대기 /  / 새 신호 대기 |
| v1 | bollinger_20_reentry | 10000.00 | 0.00 | 대기 /  / 새 신호 대기 |
| v1 | donchian_20 | 10000.00 | 0.00 | 대기 /  / 새 신호 대기 |
| v1 | atr_14_breakout | 10000.00 | 0.00 | 대기 /  / 새 신호 대기 |
| v1 | session_vwap | 9891.58 | -108.42 | sell /  / 종가 > 뉴욕 거래일별 누적 전형가격 VWAP; 조건 미충족; close=771.41, session_VWAP=771.735, session_volume=1.75958e+07 |
| v1 | obv_20 | 9931.74 | -68.26 | sell /  / OBV > OBV의 SMA20 그리고 종가 > EMA26; 조건 미충족; OBV=-708839, OBV_SMA20=2.15302e+06, close=771.03, EMA26=770.746 |
| v1 | stochastic_14_3_recovery | 10000.00 | 0.00 | 대기 /  / 새 신호 대기 |
| v1 | mfi_14_recovery | 10000.00 | 0.00 | 대기 /  / 새 신호 대기 |
| v1 | adx_14_trend | 10000.00 | 0.00 | 대기 /  / 새 신호 대기 |
| v1 | aroon_25_trend | 9936.34 | -63.66 | buy /  / Aroon25 Up > 70 그리고 Down < 30 (동률이면 최신 극값); 조건 충족; Aroon_up=92, Aroon_down=4 |
| v1 | cci_20_momentum | 9936.89 | -63.11 | sell /  / CCI20 > 100 (전형가격·평균절대편차); 조건 미충족; CCI20=66.0792 |
| v1 | williams_14_recovery | 10000.00 | 0.00 | 대기 /  / 새 신호 대기 |
| v1 | cmf_20_accumulation | 9929.81 | -70.19 | sell /  / Chaikin Money Flow20 > 0.1; 조건 미충족; CMF20=-0.158867, volume20=2.42577e+07 |
| v1 | chaikin_3_10 | 9946.30 | -53.70 | sell /  / ADL의 EMA3 - EMA10 > 0 그리고 종가 > EMA26; 조건 미충족; Chaikin3_10=-174742, ADL=3.14745e+07, close=772.2, EMA26=770.668 |
| v1 | roc_10_momentum | 10000.00 | 0.00 | 대기 /  / 새 신호 대기 |
| v1 | trix_15_trend | 9936.34 | -63.66 | buy /  / 15봉 삼중 EMA의 1봉 변화율 TRIX > 0 그리고 종가 > EMA26; 조건 충족; TRIX15_percent=0.00577763, close=771.74, EMA26=770.546 |
| v1 | keltner_20_breakout | 10000.00 | 0.00 | 대기 /  / 새 신호 대기 |
| v1 | opening_range_30m | 9946.30 | -53.70 | sell /  / 뉴욕 09:30·09:45 두 완료 봉 최고가를 10:00 이후 종가가 돌파; 자료 부족·변동폭 또는 거래량 없음: 대기; close=772.2 |
| v2 | cash | 10000.00 | 0.00 | 대기 /  / 새 신호 대기 |
| v2 | buy_hold | 9864.67 | -135.33 | buy / partial / 직전 완료 봉 목표 비중 100%; 다음 봉 시가 가정 |
| v2 | trend_8_26 | 9820.59 | -179.41 | buy / partial / 직전 완료 봉 목표 비중 100%; 다음 봉 시가 가정 |
| v2 | momentum_26 | 9791.11 | -208.89 | buy / partial / 직전 완료 봉 목표 비중 100%; 다음 봉 시가 가정 |
| v2 | breakout_8 | 9598.61 | -401.39 | sell / filled / 직전 완료 봉 목표 비중 0%; 다음 봉 시가 가정 |
| v2 | reversion_12 | 9535.84 | -464.16 | sell / filled / 직전 완료 봉 목표 비중 0%; 다음 봉 시가 가정 |
| v2 | volume_26 | 9402.30 | -597.70 | buy / partial / 직전 완료 봉 목표 비중 100%; 다음 봉 시가 가정 |
| v2 | trend_8_26 AND momentum_26 | 9797.78 | -202.22 | buy / partial / 직전 완료 봉 목표 비중 100%; 다음 봉 시가 가정 |
| v2 | trend_8_26 + momentum_26 | 9805.85 | -194.15 | buy / partial / 직전 완료 봉 목표 비중 100%; 다음 봉 시가 가정 |
| v2 | trend_8_26 AND breakout_8 | 9825.21 | -174.79 | sell / filled / 직전 완료 봉 목표 비중 0%; 다음 봉 시가 가정 |
| v2 | trend_8_26 + breakout_8 | 9708.82 | -291.18 | buy / filled / 직전 완료 봉 목표 비중 50%; 다음 봉 시가 가정 |
| v2 | trend_8_26 AND reversion_12 | 9896.11 | -103.89 | sell / filled / 직전 완료 봉 목표 비중 0%; 다음 봉 시가 가정 |
| v2 | trend_8_26 + reversion_12 | 9676.83 | -323.17 | buy / filled / 직전 완료 봉 목표 비중 50%; 다음 봉 시가 가정 |
| v2 | trend_8_26 AND volume_26 | 9805.08 | -194.92 | buy / partial / 직전 완료 봉 목표 비중 100%; 다음 봉 시가 가정 |
| v2 | trend_8_26 + volume_26 | 9629.11 | -370.89 | buy / partial / 직전 완료 봉 목표 비중 100%; 다음 봉 시가 가정 |
| v2 | momentum_26 AND breakout_8 | 9783.53 | -216.47 | sell / filled / 직전 완료 봉 목표 비중 0%; 다음 봉 시가 가정 |
| v2 | momentum_26 + breakout_8 | 9694.27 | -305.73 | buy / filled / 직전 완료 봉 목표 비중 50%; 다음 봉 시가 가정 |
| v2 | momentum_26 AND reversion_12 | 9963.21 | -36.79 | sell / filled / 직전 완료 봉 목표 비중 0%; 다음 봉 시가 가정 |
| v2 | momentum_26 + reversion_12 | 9682.62 | -317.38 | buy / filled / 직전 완료 봉 목표 비중 50%; 다음 봉 시가 가정 |
| v2 | momentum_26 AND volume_26 | 9876.12 | -123.88 | buy / partial / 직전 완료 봉 목표 비중 100%; 다음 봉 시가 가정 |
| v2 | momentum_26 + volume_26 | 9655.08 | -344.92 | buy / partial / 직전 완료 봉 목표 비중 100%; 다음 봉 시가 가정 |
| v2 | breakout_8 AND reversion_12 | 10000.00 | 0.00 | 대기 /  / 새 신호 대기 |
| v2 | breakout_8 + reversion_12 | 9607.02 | -392.98 | sell / filled / 직전 완료 봉 목표 비중 0%; 다음 봉 시가 가정 |
| v2 | breakout_8 AND volume_26 | 9933.18 | -66.82 | sell / filled / 직전 완료 봉 목표 비중 0%; 다음 봉 시가 가정 |
| v2 | breakout_8 + volume_26 | 9539.56 | -460.44 | buy / filled / 직전 완료 봉 목표 비중 50%; 다음 봉 시가 가정 |
| v2 | reversion_12 AND volume_26 | 9743.33 | -256.67 | sell / filled / 직전 완료 봉 목표 비중 0%; 다음 봉 시가 가정 |
| v2 | reversion_12 + volume_26 | 9548.42 | -451.58 | buy / filled / 직전 완료 봉 목표 비중 50%; 다음 봉 시가 가정 |
| v2 | ema_12_26 | 9935.35 | -64.65 | buy / partial / EMA12 > EMA26; 조건 충족; EMA12=771.059, EMA26=770.546; 직전 완료 봉 목표를 다음 봉 시가에 모의 적용 |
| v2 | macd_12_26_9 | 9935.35 | -64.65 | buy / partial / MACD > 신호선 그리고 MACD > 0; 조건 충족; MACD=0.512991, signal9=0.254322; 직전 완료 봉 목표를 다음 봉 시가에 모의 적용 |
| v2 | rsi_14_recovery | 10000.00 | 0.00 | 대기 /  / 새 신호 대기 |
| v2 | bollinger_20_reentry | 10000.00 | 0.00 | 대기 /  / 새 신호 대기 |
| v2 | donchian_20 | 10000.00 | 0.00 | 대기 /  / 새 신호 대기 |
| v2 | atr_14_breakout | 10000.00 | 0.00 | 대기 /  / 새 신호 대기 |
| v2 | session_vwap | 9887.63 | -112.37 | sell / filled / 종가 > 뉴욕 거래일별 누적 전형가격 VWAP; 조건 미충족; close=771.41, session_VWAP=771.735, session_volume=1.75958e+07; 직전 완료 봉 목표를 다음 봉 시가에 모의 적용 |
| v2 | obv_20 | 9929.76 | -70.24 | sell / filled / OBV > OBV의 SMA20 그리고 종가 > EMA26; 조건 미충족; OBV=-708839, OBV_SMA20=2.15302e+06, close=771.03, EMA26=770.746; 직전 완료 봉 목표를 다음 봉 시가에 모의 적용 |
| v2 | stochastic_14_3_recovery | 10000.00 | 0.00 | 대기 /  / 새 신호 대기 |
| v2 | mfi_14_recovery | 10000.00 | 0.00 | 대기 /  / 새 신호 대기 |
| v2 | adx_14_trend | 10000.00 | 0.00 | 대기 /  / 새 신호 대기 |
| v2 | aroon_25_trend | 9935.35 | -64.65 | buy / partial / Aroon25 Up > 70 그리고 Down < 30 (동률이면 최신 극값); 조건 충족; Aroon_up=92, Aroon_down=4; 직전 완료 봉 목표를 다음 봉 시가에 모의 적용 |
| v2 | cci_20_momentum | 9934.91 | -65.09 | sell / filled / CCI20 > 100 (전형가격·평균절대편차); 조건 미충족; CCI20=66.0792; 직전 완료 봉 목표를 다음 봉 시가에 모의 적용 |
| v2 | williams_14_recovery | 10000.00 | 0.00 | 대기 /  / 새 신호 대기 |
| v2 | cmf_20_accumulation | 9927.82 | -72.18 | sell / filled / Chaikin Money Flow20 > 0.1; 조건 미충족; CMF20=-0.158867, volume20=2.42577e+07; 직전 완료 봉 목표를 다음 봉 시가에 모의 적용 |
| v2 | chaikin_3_10 | 9944.31 | -55.69 | sell / filled / ADL의 EMA3 - EMA10 > 0 그리고 종가 > EMA26; 조건 미충족; Chaikin3_10=-174742, ADL=3.14745e+07, close=772.2, EMA26=770.668; 직전 완료 봉 목표를 다음 봉 시가에 모의 적용 |
| v2 | roc_10_momentum | 10000.00 | 0.00 | 대기 /  / 새 신호 대기 |
| v2 | trix_15_trend | 9935.35 | -64.65 | buy / partial / 15봉 삼중 EMA의 1봉 변화율 TRIX > 0 그리고 종가 > EMA26; 조건 충족; TRIX15_percent=0.00577763, close=771.74, EMA26=770.546; 직전 완료 봉 목표를 다음 봉 시가에 모의 적용 |
| v2 | keltner_20_breakout | 10000.00 | 0.00 | 대기 /  / 새 신호 대기 |
| v2 | opening_range_30m | 9944.31 | -55.69 | sell / filled / 뉴욕 09:30·09:45 두 완료 봉 최고가를 10:00 이후 종가가 돌파; 자료 부족·변동폭 또는 거래량 없음: 대기; close=772.2; 직전 완료 봉 목표를 다음 봉 시가에 모의 적용 |

### 같은 기간의 비용·노출 비교 (사후 연구)

| 전략 | 비용 전 | 비용 후 | 100% 보유 | 같은 평균 노출 보유 | 평균 노출 |
|---|---:|---:|---:|---:|---:|
| cash | 0.00% | 0.00% | -0.58% | -0.00% | 0.00% |
| buy_hold | -0.16% | -0.58% | -0.58% | -0.58% | 100.00% |
| trend_8_26 | 1.08% | -2.26% | -0.58% | -0.28% | 49.08% |
| momentum_26 | -0.86% | -5.33% | -0.58% | -0.28% | 48.81% |
| breakout_8 | -0.61% | -15.63% | -0.58% | -0.12% | 21.37% |
| reversion_12 | -1.86% | -12.74% | -0.58% | -0.16% | 27.97% |
| volume_26 | -0.81% | -9.56% | -0.58% | -0.05% | 8.44% |
| trend_8_26 AND momentum_26 | 0.47% | -3.26% | -0.58% | -0.24% | 42.48% |
| trend_8_26 + momentum_26 | 0.11% | -3.60% | -0.58% | -0.28% | 48.95% |
| trend_8_26 AND breakout_8 | 0.07% | -10.28% | -0.58% | -0.07% | 12.40% |
| trend_8_26 + breakout_8 | 0.24% | -9.19% | -0.58% | -0.20% | 35.23% |
| trend_8_26 AND reversion_12 | 0.10% | -4.01% | -0.58% | -0.03% | 6.07% |
| trend_8_26 + reversion_12 | -0.39% | -7.46% | -0.58% | -0.22% | 38.53% |
| trend_8_26 AND volume_26 | -0.43% | -4.53% | -0.58% | -0.02% | 3.69% |
| trend_8_26 + volume_26 | 0.14% | -5.98% | -0.58% | -0.17% | 28.76% |
| momentum_26 AND breakout_8 | 0.37% | -10.01% | -0.58% | -0.08% | 13.46% |
| momentum_26 + breakout_8 | -0.73% | -10.63% | -0.58% | -0.20% | 35.10% |
| momentum_26 AND reversion_12 | -0.88% | -5.75% | -0.58% | -0.04% | 6.86% |
| momentum_26 + reversion_12 | -1.35% | -8.55% | -0.58% | -0.22% | 38.40% |
| momentum_26 AND volume_26 | -0.39% | -3.27% | -0.58% | -0.01% | 2.11% |
| momentum_26 + volume_26 | -0.83% | -6.30% | -0.58% | -0.17% | 28.63% |
| breakout_8 AND reversion_12 | 0.00% | 0.00% | -0.58% | -0.00% | 0.00% |
| breakout_8 + reversion_12 | -1.23% | -13.67% | -0.58% | -0.14% | 24.68% |
| breakout_8 AND volume_26 | 0.09% | -1.17% | -0.58% | -0.01% | 1.06% |
| breakout_8 + volume_26 | -0.71% | -11.73% | -0.58% | -0.09% | 14.92% |
| reversion_12 AND volume_26 | -0.67% | -4.76% | -0.58% | -0.02% | 3.96% |
| reversion_12 + volume_26 | -1.33% | -10.80% | -0.58% | -0.10% | 18.21% |
| ema_12_26 | -0.52% | -3.81% | -0.58% | -0.29% | 49.87% |
| macd_12_26_9 | 0.42% | -4.11% | -0.58% | -0.17% | 30.08% |
| rsi_14_recovery | -0.33% | -3.62% | -0.58% | -0.01% | 2.11% |
| bollinger_20_reentry | -0.82% | -6.49% | -0.58% | -0.02% | 3.69% |
| donchian_20 | 0.11% | -6.79% | -0.58% | -0.04% | 6.60% |
| atr_14_breakout | -0.04% | -5.35% | -0.58% | -0.02% | 3.96% |
| session_vwap | 1.18% | -8.91% | -0.58% | -0.30% | 51.98% |
| obv_20 | -0.83% | -9.20% | -0.58% | -0.23% | 39.05% |
| stochastic_14_3_recovery | -0.99% | -15.24% | -0.58% | -0.06% | 9.76% |
| mfi_14_recovery | -0.01% | -2.50% | -0.58% | -0.01% | 1.58% |
| adx_14_trend | -0.10% | -3.81% | -0.58% | -0.16% | 27.97% |
| aroon_25_trend | 0.91% | -2.42% | -0.58% | -0.15% | 26.39% |
| cci_20_momentum | -0.18% | -7.84% | -0.58% | -0.12% | 21.11% |
| williams_14_recovery | -0.88% | -10.76% | -0.58% | -0.04% | 6.60% |
| cmf_20_accumulation | 1.72% | -2.46% | -0.58% | -0.27% | 47.23% |
| chaikin_3_10 | 1.27% | -5.31% | -0.58% | -0.24% | 41.16% |
| roc_10_momentum | -0.06% | -0.48% | -0.58% | -0.00% | 0.79% |
| trix_15_trend | -0.55% | -3.43% | -0.58% | -0.22% | 38.26% |
| keltner_20_breakout | 0.09% | -3.62% | -0.58% | -0.06% | 10.82% |
| opening_range_30m | -0.35% | -6.43% | -0.58% | -0.19% | 32.19% |

동일 구간·초기 자금, 종료 시 청산 비용 포함. 노출 맞춤은 사후 설명용이며 v2 실제 계좌 성과가 아닙니다.
[낙폭 분해·비용 영향·전체 구간](SPY/comparison.json)

[v1 전체 기록](SPY/accounts.json) · [v2 전체 기록](SPY/accounts-v2.json)

## QQQ 계좌

| 모델 | 전략 | 평가액 USD | 손익 USD | 최근 매매·이유 |
|---|---|---:|---:|---|
| v1 | cash | 10000.00 | 0.00 | 대기 /  / 새 신호 대기 |
| v1 | buy_hold | 9877.94 | -122.06 | buy /  / buy_hold: prior completed bar target 100%; next bar open simulation |
| v1 | trend_8_26 | 9922.86 | -77.14 | sell /  / trend_8_26: prior completed bar target 0%; next bar open simulation |
| v1 | momentum_26 | 9935.02 | -64.98 | sell /  / momentum_26: prior completed bar target 0%; next bar open simulation |
| v1 | breakout_8 | 10000.00 | 0.00 | 대기 /  / 새 신호 대기 |
| v1 | reversion_12 | 9951.96 | -48.04 | sell /  / reversion_12: prior completed bar target 0%; next bar open simulation |
| v1 | volume_26 | 10000.00 | 0.00 | 대기 /  / 새 신호 대기 |
| v1 | trend_8_26 AND momentum_26 | 9951.96 | -48.04 | sell /  / trend_8_26 AND momentum_26: prior completed bar target 0%; next bar open simulation |
| v1 | trend_8_26 + momentum_26 | 9928.92 | -71.08 | sell /  / trend_8_26 + momentum_26: prior completed bar target 0%; next bar open simulation |
| v1 | trend_8_26 AND breakout_8 | 10000.00 | 0.00 | 대기 /  / 새 신호 대기 |
| v1 | trend_8_26 + breakout_8 | 9961.32 | -38.68 | sell /  / trend_8_26 + breakout_8: prior completed bar target 0%; next bar open simulation |
| v1 | trend_8_26 AND reversion_12 | 9951.96 | -48.04 | sell /  / trend_8_26 AND reversion_12: prior completed bar target 0%; next bar open simulation |
| v1 | trend_8_26 + reversion_12 | 9937.38 | -62.62 | sell /  / trend_8_26 + reversion_12: prior completed bar target 0%; next bar open simulation |
| v1 | trend_8_26 AND volume_26 | 10000.00 | 0.00 | 대기 /  / 새 신호 대기 |
| v1 | trend_8_26 + volume_26 | 9961.32 | -38.68 | sell /  / trend_8_26 + volume_26: prior completed bar target 0%; next bar open simulation |
| v1 | momentum_26 AND breakout_8 | 10000.00 | 0.00 | 대기 /  / 새 신호 대기 |
| v1 | momentum_26 + breakout_8 | 9967.44 | -32.56 | sell /  / momentum_26 + breakout_8: prior completed bar target 0%; next bar open simulation |
| v1 | momentum_26 AND reversion_12 | 9951.96 | -48.04 | sell /  / momentum_26 AND reversion_12: prior completed bar target 0%; next bar open simulation |
| v1 | momentum_26 + reversion_12 | 9943.49 | -56.51 | sell /  / momentum_26 + reversion_12: prior completed bar target 0%; next bar open simulation |
| v1 | momentum_26 AND volume_26 | 10000.00 | 0.00 | 대기 /  / 새 신호 대기 |
| v1 | momentum_26 + volume_26 | 9967.44 | -32.56 | sell /  / momentum_26 + volume_26: prior completed bar target 0%; next bar open simulation |
| v1 | breakout_8 AND reversion_12 | 10000.00 | 0.00 | 대기 /  / 새 신호 대기 |
| v1 | breakout_8 + reversion_12 | 9975.92 | -24.08 | sell /  / breakout_8 + reversion_12: prior completed bar target 0%; next bar open simulation |
| v1 | breakout_8 AND volume_26 | 10000.00 | 0.00 | 대기 /  / 새 신호 대기 |
| v1 | breakout_8 + volume_26 | 10000.00 | 0.00 | 대기 /  / 새 신호 대기 |
| v1 | reversion_12 AND volume_26 | 10000.00 | 0.00 | 대기 /  / 새 신호 대기 |
| v1 | reversion_12 + volume_26 | 9975.92 | -24.08 | sell /  / reversion_12 + volume_26: prior completed bar target 0%; next bar open simulation |
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
| v2 | buy_hold | 9558.65 | -441.35 | buy / partial / 직전 완료 봉 목표 비중 100%; 다음 봉 시가 가정 |
| v2 | trend_8_26 | 9726.12 | -273.88 | sell / filled / 직전 완료 봉 목표 비중 0%; 다음 봉 시가 가정 |
| v2 | momentum_26 | 9831.49 | -168.51 | sell / filled / 직전 완료 봉 목표 비중 0%; 다음 봉 시가 가정 |
| v2 | breakout_8 | 9669.86 | -330.14 | sell / filled / 직전 완료 봉 목표 비중 0%; 다음 봉 시가 가정 |
| v2 | reversion_12 | 9468.22 | -531.78 | sell / filled / 직전 완료 봉 목표 비중 0%; 다음 봉 시가 가정 |
| v2 | volume_26 | 9565.80 | -434.20 | 중단: 손실 한도 / sell / filled / 직전 완료 봉 목표 비중 0%; 다음 봉 시가 가정 |
| v2 | trend_8_26 AND momentum_26 | 9848.25 | -151.75 | sell / filled / 직전 완료 봉 목표 비중 0%; 다음 봉 시가 가정 |
| v2 | trend_8_26 + momentum_26 | 9778.69 | -221.31 | sell / filled / 직전 완료 봉 목표 비중 0%; 다음 봉 시가 가정 |
| v2 | trend_8_26 AND breakout_8 | 9895.83 | -104.17 | sell / filled / 직전 완료 봉 목표 비중 0%; 다음 봉 시가 가정 |
| v2 | trend_8_26 + breakout_8 | 9697.89 | -302.11 | sell / filled / 직전 완료 봉 목표 비중 0%; 다음 봉 시가 가정 |
| v2 | trend_8_26 AND reversion_12 | 9811.80 | -188.20 | sell / filled / 직전 완료 봉 목표 비중 0%; 다음 봉 시가 가정 |
| v2 | trend_8_26 + reversion_12 | 9596.00 | -404.00 | sell / filled / 직전 완료 봉 목표 비중 0%; 다음 봉 시가 가정 |
| v2 | trend_8_26 AND volume_26 | 9840.10 | -159.90 | sell / filled / 직전 완료 봉 목표 비중 0%; 다음 봉 시가 가정 |
| v2 | trend_8_26 + volume_26 | 9565.02 | -434.98 | sell / filled / 직전 완료 봉 목표 비중 0%; 다음 봉 시가 가정 |
| v2 | momentum_26 AND breakout_8 | 9960.69 | -39.31 | sell / filled / 직전 완료 봉 목표 비중 0%; 다음 봉 시가 가정 |
| v2 | momentum_26 + breakout_8 | 9750.28 | -249.72 | sell / filled / 직전 완료 봉 목표 비중 0%; 다음 봉 시가 가정 |
| v2 | momentum_26 AND reversion_12 | 9949.97 | -50.03 | sell / filled / 직전 완료 봉 목표 비중 0%; 다음 봉 시가 가정 |
| v2 | momentum_26 + reversion_12 | 9668.11 | -331.89 | sell / filled / 직전 완료 봉 목표 비중 0%; 다음 봉 시가 가정 |
| v2 | momentum_26 AND volume_26 | 9936.83 | -63.17 | sell / filled / 직전 완료 봉 목표 비중 0%; 다음 봉 시가 가정 |
| v2 | momentum_26 + volume_26 | 9616.70 | -383.30 | sell / filled / 직전 완료 봉 목표 비중 0%; 다음 봉 시가 가정 |
| v2 | breakout_8 AND reversion_12 | 10000.00 | 0.00 | 대기 /  / 새 신호 대기 |
| v2 | breakout_8 + reversion_12 | 9628.66 | -371.34 | sell / filled / 직전 완료 봉 목표 비중 0%; 다음 봉 시가 가정 |
| v2 | breakout_8 AND volume_26 | 9947.98 | -52.02 | sell / filled / 직전 완료 봉 목표 비중 0%; 다음 봉 시가 가정 |
| v2 | breakout_8 + volume_26 | 9577.55 | -422.45 | sell / filled / 직전 완료 봉 목표 비중 0%; 다음 봉 시가 가정 |
| v2 | reversion_12 AND volume_26 | 9547.64 | -452.36 | 중단: 손실 한도 / sell / filled / 직전 완료 봉 목표 비중 0%; 다음 봉 시가 가정 |
| v2 | reversion_12 + volume_26 | 9457.36 | -542.64 | sell / filled / 직전 완료 봉 목표 비중 0%; 다음 봉 시가 가정 |
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
| cash | 0.00% | 0.00% | -4.02% | -0.00% | 0.00% |
| buy_hold | -3.62% | -4.02% | -4.02% | -4.02% | 100.00% |
| trend_8_26 | -0.44% | -4.13% | -4.02% | -1.87% | 46.44% |
| momentum_26 | -1.71% | -6.54% | -4.02% | -1.62% | 40.11% |
| breakout_8 | -1.58% | -16.80% | -4.02% | -0.72% | 17.94% |
| reversion_12 | -0.94% | -13.39% | -4.02% | -1.12% | 27.70% |
| volume_26 | -1.07% | -13.51% | -4.02% | -0.57% | 14.25% |
| trend_8_26 AND momentum_26 | -0.58% | -4.67% | -4.02% | -1.43% | 35.36% |
| trend_8_26 + momentum_26 | -1.07% | -5.14% | -4.02% | -1.74% | 43.27% |
| trend_8_26 AND breakout_8 | -0.43% | -9.60% | -4.02% | -0.44% | 10.82% |
| trend_8_26 + breakout_8 | -1.00% | -10.31% | -4.02% | -1.30% | 32.20% |
| trend_8_26 AND reversion_12 | 0.34% | -5.79% | -4.02% | -0.29% | 7.12% |
| trend_8_26 + reversion_12 | -0.68% | -8.31% | -4.02% | -1.49% | 37.08% |
| trend_8_26 AND volume_26 | -0.71% | -5.59% | -4.02% | -0.17% | 4.22% |
| trend_8_26 + volume_26 | -0.75% | -8.76% | -4.02% | -1.22% | 30.35% |
| momentum_26 AND breakout_8 | -0.25% | -9.05% | -4.02% | -0.43% | 10.55% |
| momentum_26 + breakout_8 | -1.64% | -11.63% | -4.02% | -1.17% | 29.03% |
| momentum_26 AND reversion_12 | -0.10% | -6.20% | -4.02% | -0.23% | 5.80% |
| momentum_26 + reversion_12 | -1.32% | -9.47% | -4.02% | -1.37% | 33.91% |
| momentum_26 AND volume_26 | -0.30% | -4.40% | -4.02% | -0.14% | 3.43% |
| momentum_26 + volume_26 | -1.39% | -9.91% | -4.02% | -1.10% | 27.18% |
| breakout_8 AND reversion_12 | 0.00% | 0.00% | -4.02% | -0.00% | 0.00% |
| breakout_8 + reversion_12 | -1.25% | -14.23% | -4.02% | -0.92% | 22.83% |
| breakout_8 AND volume_26 | 0.04% | -2.04% | -4.02% | -0.05% | 1.32% |
| breakout_8 + volume_26 | -1.32% | -13.92% | -4.02% | -0.65% | 16.10% |
| reversion_12 AND volume_26 | -1.25% | -8.44% | -4.02% | -0.35% | 8.71% |
| reversion_12 + volume_26 | -1.00% | -13.10% | -4.02% | -0.85% | 20.98% |
| ema_12_26 | 0.10% | -1.98% | -4.02% | -1.52% | 37.73% |
| macd_12_26_9 | 1.43% | -2.34% | -4.02% | -0.84% | 20.84% |
| rsi_14_recovery | -0.50% | -4.99% | -4.02% | -0.12% | 2.90% |
| bollinger_20_reentry | -0.19% | -5.89% | -4.02% | -0.15% | 3.69% |
| donchian_20 | 0.28% | -4.24% | -4.02% | -0.19% | 4.75% |
| atr_14_breakout | -0.26% | -4.76% | -4.02% | -0.13% | 3.17% |
| session_vwap | -1.38% | -12.69% | -4.02% | -2.14% | 53.03% |
| obv_20 | -1.88% | -10.91% | -4.02% | -1.10% | 27.18% |
| stochastic_14_3_recovery | -0.24% | -10.93% | -4.02% | -0.29% | 7.12% |
| mfi_14_recovery | -0.16% | -1.82% | -4.02% | -0.04% | 1.06% |
| adx_14_trend | -0.71% | -3.59% | -4.02% | -0.76% | 18.73% |
| aroon_25_trend | 1.33% | -2.43% | -4.02% | -0.82% | 20.32% |
| cci_20_momentum | -0.85% | -5.72% | -4.02% | -0.61% | 15.04% |
| williams_14_recovery | -0.68% | -10.95% | -4.02% | -0.28% | 6.86% |
| cmf_20_accumulation | -2.09% | -10.35% | -4.02% | -1.31% | 32.45% |
| chaikin_3_10 | -3.11% | -11.29% | -4.02% | -1.45% | 35.88% |
| roc_10_momentum | -0.31% | -1.56% | -4.02% | -0.09% | 2.11% |
| trix_15_trend | -0.03% | -1.69% | -4.02% | -1.28% | 31.66% |
| keltner_20_breakout | -0.73% | -4.81% | -4.02% | -0.30% | 7.39% |
| opening_range_30m | -0.35% | -6.04% | -4.02% | -0.88% | 21.90% |

동일 구간·초기 자금, 종료 시 청산 비용 포함. 노출 맞춤은 사후 설명용이며 v2 실제 계좌 성과가 아닙니다.
[낙폭 분해·비용 영향·전체 구간](QQQ/comparison.json)

[v1 전체 기록](QQQ/accounts.json) · [v2 전체 기록](QQQ/accounts-v2.json)

## IWM 계좌

| 모델 | 전략 | 평가액 USD | 손익 USD | 최근 매매·이유 |
|---|---|---:|---:|---|
| v1 | cash | 10000.00 | 0.00 | 대기 /  / 새 신호 대기 |
| v1 | buy_hold | 9915.55 | -84.45 | buy /  / buy_hold: prior completed bar target 100%; next bar open simulation |
| v1 | trend_8_26 | 9915.55 | -84.45 | buy /  / trend_8_26: prior completed bar target 100%; next bar open simulation |
| v1 | momentum_26 | 9915.55 | -84.45 | buy /  / momentum_26: prior completed bar target 100%; next bar open simulation |
| v1 | breakout_8 | 9929.38 | -70.62 | sell /  / breakout_8: prior completed bar target 0%; next bar open simulation |
| v1 | reversion_12 | 10000.00 | 0.00 | 대기 /  / 새 신호 대기 |
| v1 | volume_26 | 10000.00 | 0.00 | 대기 /  / 새 신호 대기 |
| v1 | trend_8_26 AND momentum_26 | 9915.55 | -84.45 | buy /  / trend_8_26 AND momentum_26: prior completed bar target 100%; next bar open simulation |
| v1 | trend_8_26 + momentum_26 | 9915.55 | -84.45 | buy /  / trend_8_26 + momentum_26: prior completed bar target 100%; next bar open simulation |
| v1 | trend_8_26 AND breakout_8 | 9929.38 | -70.62 | sell /  / trend_8_26 AND breakout_8: prior completed bar target 0%; next bar open simulation |
| v1 | trend_8_26 + breakout_8 | 9922.47 | -77.53 | buy /  / trend_8_26 + breakout_8: prior completed bar target 50%; next bar open simulation |
| v1 | trend_8_26 AND reversion_12 | 10000.00 | 0.00 | 대기 /  / 새 신호 대기 |
| v1 | trend_8_26 + reversion_12 | 9957.66 | -42.34 | buy /  / trend_8_26 + reversion_12: prior completed bar target 50%; next bar open simulation |
| v1 | trend_8_26 AND volume_26 | 10000.00 | 0.00 | 대기 /  / 새 신호 대기 |
| v1 | trend_8_26 + volume_26 | 9957.66 | -42.34 | buy /  / trend_8_26 + volume_26: prior completed bar target 50%; next bar open simulation |
| v1 | momentum_26 AND breakout_8 | 9929.38 | -70.62 | sell /  / momentum_26 AND breakout_8: prior completed bar target 0%; next bar open simulation |
| v1 | momentum_26 + breakout_8 | 9922.47 | -77.53 | buy /  / momentum_26 + breakout_8: prior completed bar target 50%; next bar open simulation |
| v1 | momentum_26 AND reversion_12 | 10000.00 | 0.00 | 대기 /  / 새 신호 대기 |
| v1 | momentum_26 + reversion_12 | 9957.66 | -42.34 | buy /  / momentum_26 + reversion_12: prior completed bar target 50%; next bar open simulation |
| v1 | momentum_26 AND volume_26 | 10000.00 | 0.00 | 대기 /  / 새 신호 대기 |
| v1 | momentum_26 + volume_26 | 9957.66 | -42.34 | buy /  / momentum_26 + volume_26: prior completed bar target 50%; next bar open simulation |
| v1 | breakout_8 AND reversion_12 | 10000.00 | 0.00 | 대기 /  / 새 신호 대기 |
| v1 | breakout_8 + reversion_12 | 9964.62 | -35.38 | sell /  / breakout_8 + reversion_12: prior completed bar target 0%; next bar open simulation |
| v1 | breakout_8 AND volume_26 | 10000.00 | 0.00 | 대기 /  / 새 신호 대기 |
| v1 | breakout_8 + volume_26 | 9964.62 | -35.38 | sell /  / breakout_8 + volume_26: prior completed bar target 0%; next bar open simulation |
| v1 | reversion_12 AND volume_26 | 10000.00 | 0.00 | 대기 /  / 새 신호 대기 |
| v1 | reversion_12 + volume_26 | 10000.00 | 0.00 | 대기 /  / 새 신호 대기 |
| v1 | ema_12_26 | 9915.55 | -84.45 | buy /  / EMA12 > EMA26; 조건 충족; EMA12=274.113, EMA26=273.616 |
| v1 | macd_12_26_9 | 9916.70 | -83.30 | sell /  / MACD > 신호선 그리고 MACD > 0; 조건 미충족; MACD=0.425881, signal9=0.461272 |
| v1 | rsi_14_recovery | 10000.00 | 0.00 | 대기 /  / 새 신호 대기 |
| v1 | bollinger_20_reentry | 10000.00 | 0.00 | 대기 /  / 새 신호 대기 |
| v1 | donchian_20 | 9929.38 | -70.62 | sell /  / 종가 > 현재 봉을 제외한 직전 20봉 최고가; 조건 미충족; close=274.88, prior_high20=275.91 |
| v1 | atr_14_breakout | 9929.38 | -70.62 | sell /  / 종가 > 직전 종가 + 직전 ATR14 그리고 종가 > EMA26; 조건 미충족; close=274.88, threshold=276.257, prior_ATR14=0.526844, EMA26=273.855 |
| v1 | session_vwap | 9937.31 | -62.69 | sell /  / 종가 > 뉴욕 거래일별 누적 전형가격 VWAP; 조건 미충족; close=274.88, session_VWAP=275.422, session_volume=2.52313e+06 |
| v1 | obv_20 | 9928.63 | -71.37 | sell /  / OBV > OBV의 SMA20 그리고 종가 > EMA26; 조건 미충족; OBV=-4.10489e+07, OBV_SMA20=-4.0926e+07, close=274.64, EMA26=273.913 |
| v1 | stochastic_14_3_recovery | 10000.00 | 0.00 | 대기 /  / 새 신호 대기 |
| v1 | mfi_14_recovery | 10000.00 | 0.00 | 대기 /  / 새 신호 대기 |
| v1 | adx_14_trend | 9915.55 | -84.45 | buy /  / Wilder ADX14 >= 25 그리고 +DI14 > -DI14; 조건 충족; ADX14=29.1522, plus_DI14=35.2594, minus_DI14=12.8051 |
| v1 | aroon_25_trend | 9915.55 | -84.45 | buy /  / Aroon25 Up > 70 그리고 Down < 30 (동률이면 최신 극값); 조건 충족; Aroon_up=100, Aroon_down=4 |
| v1 | cci_20_momentum | 9928.63 | -71.37 | sell /  / CCI20 > 100 (전형가격·평균절대편차); 조건 미충족; CCI20=90.0513 |
| v1 | williams_14_recovery | 10000.00 | 0.00 | 대기 /  / 새 신호 대기 |
| v1 | cmf_20_accumulation | 9843.27 | -156.73 | sell /  / Chaikin Money Flow20 > 0.1; 조건 미충족; CMF20=0.0663812, volume20=1.58199e+07 |
| v1 | chaikin_3_10 | 9916.70 | -83.30 | sell /  / ADL의 EMA3 - EMA10 > 0 그리고 종가 > EMA26; 조건 미충족; Chaikin3_10=-335917, ADL=-5.92841e+07, close=274.31, EMA26=274.011 |
| v1 | roc_10_momentum | 10000.00 | 0.00 | 대기 /  / 새 신호 대기 |
| v1 | trix_15_trend | 9915.55 | -84.45 | buy /  / 15봉 삼중 EMA의 1봉 변화율 TRIX > 0 그리고 종가 > EMA26; 조건 충족; TRIX15_percent=0.020718, close=275.03, EMA26=273.616 |
| v1 | keltner_20_breakout | 9937.31 | -62.69 | sell /  / 종가 > EMA20 + 2 x Wilder ATR14; 조건 미충족; close=274.88, upper_Keltner=275.161, EMA20=274.044, ATR14=0.558498 |
| v1 | opening_range_30m | 9968.03 | -31.97 | sell /  / 뉴욕 09:30·09:45 두 완료 봉 최고가를 10:00 이후 종가가 돌파; 자료 부족·변동폭 또는 거래량 없음: 대기; close=275.73 |
| v2 | cash | 10000.00 | 0.00 | 대기 /  / 새 신호 대기 |
| v2 | buy_hold | 9809.53 | -190.47 | buy / partial / 직전 완료 봉 목표 비중 100%; 다음 봉 시가 가정 |
| v2 | trend_8_26 | 9787.07 | -212.93 | buy / partial / 직전 완료 봉 목표 비중 100%; 다음 봉 시가 가정 |
| v2 | momentum_26 | 9788.08 | -211.92 | buy / partial / 직전 완료 봉 목표 비중 100%; 다음 봉 시가 가정 |
| v2 | breakout_8 | 9547.89 | -452.11 | sell / filled / 직전 완료 봉 목표 비중 0%; 다음 봉 시가 가정 |
| v2 | reversion_12 | 9538.67 | -461.33 | sell / filled / 직전 완료 봉 목표 비중 0%; 다음 봉 시가 가정 |
| v2 | volume_26 | 9513.36 | -486.64 | sell / filled / 직전 완료 봉 목표 비중 0%; 다음 봉 시가 가정 |
| v2 | trend_8_26 AND momentum_26 | 9938.98 | -61.02 | buy / partial / 직전 완료 봉 목표 비중 100%; 다음 봉 시가 가정 |
| v2 | trend_8_26 + momentum_26 | 9808.28 | -191.72 | buy / partial / 직전 완료 봉 목표 비중 100%; 다음 봉 시가 가정 |
| v2 | trend_8_26 AND breakout_8 | 9840.76 | -159.24 | sell / filled / 직전 완료 봉 목표 비중 0%; 다음 봉 시가 가정 |
| v2 | trend_8_26 + breakout_8 | 9687.20 | -312.80 | buy / filled / 직전 완료 봉 목표 비중 50%; 다음 봉 시가 가정 |
| v2 | trend_8_26 AND reversion_12 | 9881.82 | -118.18 | sell / filled / 직전 완료 봉 목표 비중 0%; 다음 봉 시가 가정 |
| v2 | trend_8_26 + reversion_12 | 9661.89 | -338.11 | buy / filled / 직전 완료 봉 목표 비중 50%; 다음 봉 시가 가정 |
| v2 | trend_8_26 AND volume_26 | 9862.83 | -137.17 | sell / filled / 직전 완료 봉 목표 비중 0%; 다음 봉 시가 가정 |
| v2 | trend_8_26 + volume_26 | 9669.49 | -330.51 | buy / filled / 직전 완료 봉 목표 비중 50%; 다음 봉 시가 가정 |
| v2 | momentum_26 AND breakout_8 | 9733.71 | -266.29 | sell / filled / 직전 완료 봉 목표 비중 0%; 다음 봉 시가 가정 |
| v2 | momentum_26 + breakout_8 | 9667.26 | -332.74 | buy / filled / 직전 완료 봉 목표 비중 50%; 다음 봉 시가 가정 |
| v2 | momentum_26 AND reversion_12 | 9960.59 | -39.41 | sell / filled / 직전 완료 봉 목표 비중 0%; 다음 봉 시가 가정 |
| v2 | momentum_26 + reversion_12 | 9682.47 | -317.53 | buy / filled / 직전 완료 봉 목표 비중 50%; 다음 봉 시가 가정 |
| v2 | momentum_26 AND volume_26 | 9897.79 | -102.21 | sell / filled / 직전 완료 봉 목표 비중 0%; 다음 봉 시가 가정 |
| v2 | momentum_26 + volume_26 | 9649.50 | -350.50 | buy / filled / 직전 완료 봉 목표 비중 50%; 다음 봉 시가 가정 |
| v2 | breakout_8 AND reversion_12 | 10000.00 | 0.00 | 대기 /  / 새 신호 대기 |
| v2 | breakout_8 + reversion_12 | 9583.04 | -416.96 | sell / filled / 직전 완료 봉 목표 비중 0%; 다음 봉 시가 가정 |
| v2 | breakout_8 AND volume_26 | 9746.03 | -253.97 | sell / filled / 직전 완료 봉 목표 비중 0%; 다음 봉 시가 가정 |
| v2 | breakout_8 + volume_26 | 9550.58 | -449.42 | sell / filled / 직전 완료 봉 목표 비중 0%; 다음 봉 시가 가정 |
| v2 | reversion_12 AND volume_26 | 9740.75 | -259.25 | sell / filled / 직전 완료 봉 목표 비중 0%; 다음 봉 시가 가정 |
| v2 | reversion_12 + volume_26 | 9545.82 | -454.18 | sell / filled / 직전 완료 봉 목표 비중 0%; 다음 봉 시가 가정 |
| v2 | ema_12_26 | 9914.56 | -85.44 | buy / partial / EMA12 > EMA26; 조건 충족; EMA12=274.113, EMA26=273.616; 직전 완료 봉 목표를 다음 봉 시가에 모의 적용 |
| v2 | macd_12_26_9 | 9914.72 | -85.28 | sell / filled / MACD > 신호선 그리고 MACD > 0; 조건 미충족; MACD=0.425881, signal9=0.461272; 직전 완료 봉 목표를 다음 봉 시가에 모의 적용 |
| v2 | rsi_14_recovery | 10000.00 | 0.00 | 대기 /  / 새 신호 대기 |
| v2 | bollinger_20_reentry | 10000.00 | 0.00 | 대기 /  / 새 신호 대기 |
| v2 | donchian_20 | 9927.39 | -72.61 | sell / filled / 종가 > 현재 봉을 제외한 직전 20봉 최고가; 조건 미충족; close=274.88, prior_high20=275.91; 직전 완료 봉 목표를 다음 봉 시가에 모의 적용 |
| v2 | atr_14_breakout | 9927.39 | -72.61 | sell / filled / 종가 > 직전 종가 + 직전 ATR14 그리고 종가 > EMA26; 조건 미충족; close=274.88, threshold=276.257, prior_ATR14=0.526844, EMA26=273.855; 직전 완료 봉 목표를 다음 봉 시가에 모의 적용 |
| v2 | session_vwap | 9935.32 | -64.68 | sell / filled / 종가 > 뉴욕 거래일별 누적 전형가격 VWAP; 조건 미충족; close=274.88, session_VWAP=275.422, session_volume=2.52313e+06; 직전 완료 봉 목표를 다음 봉 시가에 모의 적용 |
| v2 | obv_20 | 9926.64 | -73.36 | sell / filled / OBV > OBV의 SMA20 그리고 종가 > EMA26; 조건 미충족; OBV=-4.10489e+07, OBV_SMA20=-4.0926e+07, close=274.64, EMA26=273.913; 직전 완료 봉 목표를 다음 봉 시가에 모의 적용 |
| v2 | stochastic_14_3_recovery | 10000.00 | 0.00 | 대기 /  / 새 신호 대기 |
| v2 | mfi_14_recovery | 10000.00 | 0.00 | 대기 /  / 새 신호 대기 |
| v2 | adx_14_trend | 9914.56 | -85.44 | buy / partial / Wilder ADX14 >= 25 그리고 +DI14 > -DI14; 조건 충족; ADX14=29.1522, plus_DI14=35.2594, minus_DI14=12.8051; 직전 완료 봉 목표를 다음 봉 시가에 모의 적용 |
| v2 | aroon_25_trend | 9914.56 | -85.44 | buy / partial / Aroon25 Up > 70 그리고 Down < 30 (동률이면 최신 극값); 조건 충족; Aroon_up=100, Aroon_down=4; 직전 완료 봉 목표를 다음 봉 시가에 모의 적용 |
| v2 | cci_20_momentum | 9926.64 | -73.36 | sell / filled / CCI20 > 100 (전형가격·평균절대편차); 조건 미충족; CCI20=90.0513; 직전 완료 봉 목표를 다음 봉 시가에 모의 적용 |
| v2 | williams_14_recovery | 10000.00 | 0.00 | 대기 /  / 새 신호 대기 |
| v2 | cmf_20_accumulation | 9837.36 | -162.64 | sell / filled / Chaikin Money Flow20 > 0.1; 조건 미충족; CMF20=0.0663812, volume20=1.58199e+07; 직전 완료 봉 목표를 다음 봉 시가에 모의 적용 |
| v2 | chaikin_3_10 | 9914.72 | -85.28 | sell / filled / ADL의 EMA3 - EMA10 > 0 그리고 종가 > EMA26; 조건 미충족; Chaikin3_10=-335917, ADL=-5.92841e+07, close=274.31, EMA26=274.011; 직전 완료 봉 목표를 다음 봉 시가에 모의 적용 |
| v2 | roc_10_momentum | 10000.00 | 0.00 | 대기 /  / 새 신호 대기 |
| v2 | trix_15_trend | 9914.56 | -85.44 | buy / partial / 15봉 삼중 EMA의 1봉 변화율 TRIX > 0 그리고 종가 > EMA26; 조건 충족; TRIX15_percent=0.020718, close=275.03, EMA26=273.616; 직전 완료 봉 목표를 다음 봉 시가에 모의 적용 |
| v2 | keltner_20_breakout | 9935.32 | -64.68 | sell / filled / 종가 > EMA20 + 2 x Wilder ATR14; 조건 미충족; close=274.88, upper_Keltner=275.161, EMA20=274.044, ATR14=0.558498; 직전 완료 봉 목표를 다음 봉 시가에 모의 적용 |
| v2 | opening_range_30m | 9966.04 | -33.96 | sell / filled / 뉴욕 09:30·09:45 두 완료 봉 최고가를 10:00 이후 종가가 돌파; 자료 부족·변동폭 또는 거래량 없음: 대기; close=275.73; 직전 완료 봉 목표를 다음 봉 시가에 모의 적용 |

### 같은 기간의 비용·노출 비교 (사후 연구)

| 전략 | 비용 전 | 비용 후 | 100% 보유 | 같은 평균 노출 보유 | 평균 노출 |
|---|---:|---:|---:|---:|---:|
| cash | 0.00% | 0.00% | -3.34% | -0.00% | 0.00% |
| buy_hold | -2.93% | -3.34% | -3.34% | -3.34% | 100.00% |
| trend_8_26 | -1.58% | -5.23% | -3.34% | -1.52% | 45.12% |
| momentum_26 | -2.94% | -8.49% | -3.34% | -1.35% | 40.11% |
| breakout_8 | -1.07% | -14.24% | -3.34% | -0.65% | 19.26% |
| reversion_12 | -2.18% | -14.48% | -3.34% | -0.99% | 29.29% |
| volume_26 | -2.31% | -9.05% | -3.34% | -0.29% | 8.44% |
| trend_8_26 AND momentum_26 | -1.83% | -5.86% | -3.34% | -1.18% | 35.09% |
| trend_8_26 + momentum_26 | -2.26% | -6.48% | -3.34% | -1.43% | 42.61% |
| trend_8_26 AND breakout_8 | -0.58% | -8.20% | -3.34% | -0.37% | 11.08% |
| trend_8_26 + breakout_8 | -1.32% | -9.66% | -3.34% | -1.09% | 32.20% |
| trend_8_26 AND reversion_12 | -0.15% | -4.66% | -3.34% | -0.18% | 5.28% |
| trend_8_26 + reversion_12 | -1.87% | -9.79% | -3.34% | -1.25% | 37.21% |
| trend_8_26 AND volume_26 | -1.03% | -4.30% | -3.34% | -0.12% | 3.43% |
| trend_8_26 + volume_26 | -1.94% | -6.97% | -3.34% | -0.90% | 26.78% |
| momentum_26 AND breakout_8 | -0.34% | -7.98% | -3.34% | -0.36% | 10.55% |
| momentum_26 + breakout_8 | -2.01% | -11.41% | -3.34% | -1.00% | 29.69% |
| momentum_26 AND reversion_12 | -0.08% | -3.38% | -3.34% | -0.09% | 2.64% |
| momentum_26 + reversion_12 | -2.55% | -10.42% | -3.34% | -1.17% | 34.70% |
| momentum_26 AND volume_26 | -1.32% | -3.77% | -3.34% | -0.06% | 1.85% |
| momentum_26 + volume_26 | -2.62% | -8.39% | -3.34% | -0.82% | 24.28% |
| breakout_8 AND reversion_12 | 0.00% | 0.00% | -3.34% | -0.00% | 0.00% |
| breakout_8 + reversion_12 | -1.62% | -13.65% | -3.34% | -0.82% | 24.28% |
| breakout_8 AND volume_26 | -1.30% | -3.76% | -3.34% | -0.07% | 2.11% |
| breakout_8 + volume_26 | -1.69% | -11.50% | -3.34% | -0.47% | 13.86% |
| reversion_12 AND volume_26 | -0.38% | -4.47% | -3.34% | -0.15% | 4.49% |
| reversion_12 + volume_26 | -2.24% | -11.25% | -3.34% | -0.64% | 18.87% |
| ema_12_26 | 0.03% | -2.46% | -3.34% | -1.47% | 43.80% |
| macd_12_26_9 | 1.78% | -1.16% | -3.34% | -0.93% | 27.70% |
| rsi_14_recovery | -0.28% | -4.78% | -3.34% | -0.10% | 2.90% |
| bollinger_20_reentry | -0.25% | -4.75% | -3.34% | -0.10% | 2.90% |
| donchian_20 | -0.20% | -5.10% | -3.34% | -0.19% | 5.54% |
| atr_14_breakout | -1.87% | -8.25% | -3.34% | -0.14% | 4.22% |
| session_vwap | -1.53% | -11.34% | -3.34% | -1.49% | 44.33% |
| obv_20 | -0.44% | -4.93% | -3.34% | -1.26% | 37.47% |
| stochastic_14_3_recovery | -0.87% | -13.34% | -3.34% | -0.29% | 8.44% |
| mfi_14_recovery | 0.22% | -3.50% | -3.34% | -0.08% | 2.37% |
| adx_14_trend | -0.39% | -4.08% | -3.34% | -1.06% | 31.40% |
| aroon_25_trend | -1.37% | -4.63% | -3.34% | -0.68% | 20.05% |
| cci_20_momentum | -1.95% | -7.93% | -3.34% | -0.59% | 17.41% |
| williams_14_recovery | -0.74% | -10.26% | -3.34% | -0.21% | 6.33% |
| cmf_20_accumulation | -2.35% | -8.70% | -3.34% | -0.64% | 19.00% |
| chaikin_3_10 | -2.99% | -9.68% | -3.34% | -1.13% | 33.51% |
| roc_10_momentum | -0.63% | -1.87% | -3.34% | -0.11% | 3.17% |
| trix_15_trend | -0.25% | -3.54% | -3.34% | -1.13% | 33.51% |
| keltner_20_breakout | -0.91% | -4.18% | -3.34% | -0.18% | 5.28% |
| opening_range_30m | 1.50% | -3.49% | -3.34% | -0.82% | 24.27% |

동일 구간·초기 자금, 종료 시 청산 비용 포함. 노출 맞춤은 사후 설명용이며 v2 실제 계좌 성과가 아닙니다.
[낙폭 분해·비용 영향·전체 구간](IWM/comparison.json)

[v1 전체 기록](IWM/accounts.json) · [v2 전체 기록](IWM/accounts-v2.json)

## DIA 계좌

| 모델 | 전략 | 평가액 USD | 손익 USD | 최근 매매·이유 |
|---|---|---:|---:|---|
| v1 | cash | 10000.00 | 0.00 | 대기 /  / 새 신호 대기 |
| v1 | buy_hold | 9982.89 | -17.11 | buy /  / buy_hold: prior completed bar target 100%; next bar open simulation |
| v1 | trend_8_26 | 9982.89 | -17.11 | buy /  / trend_8_26: prior completed bar target 100%; next bar open simulation |
| v1 | momentum_26 | 9982.89 | -17.11 | buy /  / momentum_26: prior completed bar target 100%; next bar open simulation |
| v1 | breakout_8 | 9940.12 | -59.88 | sell /  / breakout_8: prior completed bar target 0%; next bar open simulation |
| v1 | reversion_12 | 10000.00 | 0.00 | 대기 /  / 새 신호 대기 |
| v1 | volume_26 | 10000.00 | 0.00 | 대기 /  / 새 신호 대기 |
| v1 | trend_8_26 AND momentum_26 | 9982.89 | -17.11 | buy /  / trend_8_26 AND momentum_26: prior completed bar target 100%; next bar open simulation |
| v1 | trend_8_26 + momentum_26 | 9982.89 | -17.11 | buy /  / trend_8_26 + momentum_26: prior completed bar target 100%; next bar open simulation |
| v1 | trend_8_26 AND breakout_8 | 9940.12 | -59.88 | sell /  / trend_8_26 AND breakout_8: prior completed bar target 0%; next bar open simulation |
| v1 | trend_8_26 + breakout_8 | 9961.50 | -38.50 | sell /  / trend_8_26 + breakout_8: prior completed bar target 50%; next bar open simulation |
| v1 | trend_8_26 AND reversion_12 | 10000.00 | 0.00 | 대기 /  / 새 신호 대기 |
| v1 | trend_8_26 + reversion_12 | 9991.41 | -8.59 | sell /  / trend_8_26 + reversion_12: prior completed bar target 50%; next bar open simulation |
| v1 | trend_8_26 AND volume_26 | 10000.00 | 0.00 | 대기 /  / 새 신호 대기 |
| v1 | trend_8_26 + volume_26 | 9991.41 | -8.59 | sell /  / trend_8_26 + volume_26: prior completed bar target 50%; next bar open simulation |
| v1 | momentum_26 AND breakout_8 | 9940.12 | -59.88 | sell /  / momentum_26 AND breakout_8: prior completed bar target 0%; next bar open simulation |
| v1 | momentum_26 + breakout_8 | 9961.50 | -38.50 | sell /  / momentum_26 + breakout_8: prior completed bar target 50%; next bar open simulation |
| v1 | momentum_26 AND reversion_12 | 10000.00 | 0.00 | 대기 /  / 새 신호 대기 |
| v1 | momentum_26 + reversion_12 | 9991.41 | -8.59 | sell /  / momentum_26 + reversion_12: prior completed bar target 50%; next bar open simulation |
| v1 | momentum_26 AND volume_26 | 10000.00 | 0.00 | 대기 /  / 새 신호 대기 |
| v1 | momentum_26 + volume_26 | 9991.41 | -8.59 | sell /  / momentum_26 + volume_26: prior completed bar target 50%; next bar open simulation |
| v1 | breakout_8 AND reversion_12 | 10000.00 | 0.00 | 대기 /  / 새 신호 대기 |
| v1 | breakout_8 + reversion_12 | 9970.03 | -29.97 | sell /  / breakout_8 + reversion_12: prior completed bar target 0%; next bar open simulation |
| v1 | breakout_8 AND volume_26 | 10000.00 | 0.00 | 대기 /  / 새 신호 대기 |
| v1 | breakout_8 + volume_26 | 9970.03 | -29.97 | sell /  / breakout_8 + volume_26: prior completed bar target 0%; next bar open simulation |
| v1 | reversion_12 AND volume_26 | 10000.00 | 0.00 | 대기 /  / 새 신호 대기 |
| v1 | reversion_12 + volume_26 | 10000.00 | 0.00 | 대기 /  / 새 신호 대기 |
| v1 | ema_12_26 | 9982.89 | -17.11 | buy /  / EMA12 > EMA26; 조건 충족; EMA12=520.818, EMA26=519.784 |
| v1 | macd_12_26_9 | 9962.13 | -37.87 | buy /  / MACD > 신호선 그리고 MACD > 0; 조건 충족; MACD=1.20578, signal9=1.11304 |
| v1 | rsi_14_recovery | 10000.00 | 0.00 | 대기 /  / 새 신호 대기 |
| v1 | bollinger_20_reentry | 10000.00 | 0.00 | 대기 /  / 새 신호 대기 |
| v1 | donchian_20 | 9940.12 | -59.88 | sell /  / 종가 > 현재 봉을 제외한 직전 20봉 최고가; 조건 미충족; close=522.89, prior_high20=525.09 |
| v1 | atr_14_breakout | 9972.44 | -27.56 | sell /  / 종가 > 직전 종가 + 직전 ATR14 그리고 종가 > EMA26; 조건 미충족; close=524.65, threshold=524.777, prior_ATR14=0.84688, EMA26=520.429 |
| v1 | session_vwap | 9960.84 | -39.16 | sell /  / 종가 > 뉴욕 거래일별 누적 전형가격 VWAP; 조건 미충족; close=522.89, session_VWAP=523.72, session_volume=975370 |
| v1 | obv_20 | 9962.13 | -37.87 | buy /  / OBV > OBV의 SMA20 그리고 종가 > EMA26; 조건 충족; OBV=-4.80658e+06, OBV_SMA20=-5.3038e+06, close=523.93, EMA26=520.091 |
| v1 | stochastic_14_3_recovery | 10000.00 | 0.00 | 대기 /  / 새 신호 대기 |
| v1 | mfi_14_recovery | 10000.00 | 0.00 | 대기 /  / 새 신호 대기 |
| v1 | adx_14_trend | 9982.89 | -17.11 | buy /  / Wilder ADX14 >= 25 그리고 +DI14 > -DI14; 조건 충족; ADX14=38.0858, plus_DI14=35.3559, minus_DI14=16.277 |
| v1 | aroon_25_trend | 9982.89 | -17.11 | buy /  / Aroon25 Up > 70 그리고 Down < 30 (동률이면 최신 극값); 조건 충족; Aroon_up=92, Aroon_down=4 |
| v1 | cci_20_momentum | 9954.56 | -45.44 | sell /  / CCI20 > 100 (전형가격·평균절대편차); 조건 미충족; CCI20=83.6046 |
| v1 | williams_14_recovery | 10000.00 | 0.00 | 대기 /  / 새 신호 대기 |
| v1 | cmf_20_accumulation | 9927.80 | -72.20 | sell /  / Chaikin Money Flow20 > 0.1; 조건 미충족; CMF20=0.0502896, volume20=2.48879e+06 |
| v1 | chaikin_3_10 | 9962.13 | -37.87 | buy /  / ADL의 EMA3 - EMA10 > 0 그리고 종가 > EMA26; 조건 충족; Chaikin3_10=75087, ADL=-1.47605e+07, close=523.93, EMA26=520.091 |
| v1 | roc_10_momentum | 10000.00 | 0.00 | 대기 /  / 새 신호 대기 |
| v1 | trix_15_trend | 9982.89 | -17.11 | buy /  / 15봉 삼중 EMA의 1봉 변화율 TRIX > 0 그리고 종가 > EMA26; 조건 충족; TRIX15_percent=0.0323703, close=521.24, EMA26=519.784 |
| v1 | keltner_20_breakout | 9940.12 | -59.88 | sell /  / 종가 > EMA20 + 2 x Wilder ATR14; 조건 미충족; close=522.89, upper_Keltner=523.089, EMA20=521.145, ATR14=0.971947 |
| v1 | opening_range_30m | 9980.84 | -19.16 | sell /  / 뉴욕 09:30·09:45 두 완료 봉 최고가를 10:00 이후 종가가 돌파; 자료 부족·변동폭 또는 거래량 없음: 대기; close=523.93 |
| v2 | cash | 10000.00 | 0.00 | 대기 /  / 새 신호 대기 |
| v2 | buy_hold | 10106.57 | 106.57 | buy / partial / 직전 완료 봉 목표 비중 100%; 다음 봉 시가 가정 |
| v2 | trend_8_26 | 9918.22 | -81.78 | buy / partial / 직전 완료 봉 목표 비중 100%; 다음 봉 시가 가정 |
| v2 | momentum_26 | 10027.27 | 27.27 | buy / partial / 직전 완료 봉 목표 비중 100%; 다음 봉 시가 가정 |
| v2 | breakout_8 | 9466.63 | -533.37 | sell / filled / 직전 완료 봉 목표 비중 0%; 다음 봉 시가 가정 |
| v2 | reversion_12 | 9698.03 | -301.97 | sell / filled / 직전 완료 봉 목표 비중 0%; 다음 봉 시가 가정 |
| v2 | volume_26 | 9718.21 | -281.79 | sell / filled / 직전 완료 봉 목표 비중 0%; 다음 봉 시가 가정 |
| v2 | trend_8_26 AND momentum_26 | 10022.62 | 22.62 | buy / partial / 직전 완료 봉 목표 비중 100%; 다음 봉 시가 가정 |
| v2 | trend_8_26 + momentum_26 | 9972.66 | -27.34 | buy / partial / 직전 완료 봉 목표 비중 100%; 다음 봉 시가 가정 |
| v2 | trend_8_26 AND breakout_8 | 9626.81 | -373.19 | sell / filled / 직전 완료 봉 목표 비중 0%; 다음 봉 시가 가정 |
| v2 | trend_8_26 + breakout_8 | 9689.88 | -310.12 | sell / filled / 직전 완료 봉 목표 비중 50%; 다음 봉 시가 가정 |
| v2 | trend_8_26 AND reversion_12 | 9810.77 | -189.23 | sell / filled / 직전 완료 봉 목표 비중 0%; 다음 봉 시가 가정 |
| v2 | trend_8_26 + reversion_12 | 9807.22 | -192.78 | sell / filled / 직전 완료 봉 목표 비중 50%; 다음 봉 시가 가정 |
| v2 | trend_8_26 AND volume_26 | 9858.88 | -141.12 | sell / filled / 직전 완료 봉 목표 비중 0%; 다음 봉 시가 가정 |
| v2 | trend_8_26 + volume_26 | 9838.26 | -161.74 | sell / filled / 직전 완료 봉 목표 비중 50%; 다음 봉 시가 가정 |
| v2 | momentum_26 AND breakout_8 | 9615.85 | -384.15 | sell / filled / 직전 완료 봉 목표 비중 0%; 다음 봉 시가 가정 |
| v2 | momentum_26 + breakout_8 | 9743.07 | -256.93 | sell / filled / 직전 완료 봉 목표 비중 50%; 다음 봉 시가 가정 |
| v2 | momentum_26 AND reversion_12 | 9955.97 | -44.03 | sell / filled / 직전 완료 봉 목표 비중 0%; 다음 봉 시가 가정 |
| v2 | momentum_26 + reversion_12 | 9861.06 | -138.94 | sell / filled / 직전 완료 봉 목표 비중 50%; 다음 봉 시가 가정 |
| v2 | momentum_26 AND volume_26 | 9791.42 | -208.58 | sell / filled / 직전 완료 봉 목표 비중 0%; 다음 봉 시가 가정 |
| v2 | momentum_26 + volume_26 | 9913.13 | -86.87 | sell / filled / 직전 완료 봉 목표 비중 50%; 다음 봉 시가 가정 |
| v2 | breakout_8 AND reversion_12 | 10000.00 | 0.00 | 대기 /  / 새 신호 대기 |
| v2 | breakout_8 + reversion_12 | 9581.22 | -418.78 | sell / filled / 직전 완료 봉 목표 비중 0%; 다음 봉 시가 가정 |
| v2 | breakout_8 AND volume_26 | 9796.56 | -203.44 | sell / filled / 직전 완료 봉 목표 비중 0%; 다음 봉 시가 가정 |
| v2 | breakout_8 + volume_26 | 9591.45 | -408.55 | sell / filled / 직전 완료 봉 목표 비중 0%; 다음 봉 시가 가정 |
| v2 | reversion_12 AND volume_26 | 10000.00 | 0.00 | 대기 /  / 새 신호 대기 |
| v2 | reversion_12 + volume_26 | 9707.85 | -292.15 | sell / filled / 직전 완료 봉 목표 비중 0%; 다음 봉 시가 가정 |
| v2 | ema_12_26 | 9981.90 | -18.10 | buy / partial / EMA12 > EMA26; 조건 충족; EMA12=520.818, EMA26=519.784; 직전 완료 봉 목표를 다음 봉 시가에 모의 적용 |
| v2 | macd_12_26_9 | 9961.13 | -38.87 | buy / partial / MACD > 신호선 그리고 MACD > 0; 조건 충족; MACD=1.20578, signal9=1.11304; 직전 완료 봉 목표를 다음 봉 시가에 모의 적용 |
| v2 | rsi_14_recovery | 10000.00 | 0.00 | 대기 /  / 새 신호 대기 |
| v2 | bollinger_20_reentry | 10000.00 | 0.00 | 대기 /  / 새 신호 대기 |
| v2 | donchian_20 | 9938.13 | -61.87 | sell / filled / 종가 > 현재 봉을 제외한 직전 20봉 최고가; 조건 미충족; close=522.89, prior_high20=525.09; 직전 완료 봉 목표를 다음 봉 시가에 모의 적용 |
| v2 | atr_14_breakout | 9970.44 | -29.56 | sell / filled / 종가 > 직전 종가 + 직전 ATR14 그리고 종가 > EMA26; 조건 미충족; close=524.65, threshold=524.777, prior_ATR14=0.84688, EMA26=520.429; 직전 완료 봉 목표를 다음 봉 시가에 모의 적용 |
| v2 | session_vwap | 9958.85 | -41.15 | sell / filled / 종가 > 뉴욕 거래일별 누적 전형가격 VWAP; 조건 미충족; close=522.89, session_VWAP=523.72, session_volume=975370; 직전 완료 봉 목표를 다음 봉 시가에 모의 적용 |
| v2 | obv_20 | 9961.13 | -38.87 | buy / partial / OBV > OBV의 SMA20 그리고 종가 > EMA26; 조건 충족; OBV=-4.80658e+06, OBV_SMA20=-5.3038e+06, close=523.93, EMA26=520.091; 직전 완료 봉 목표를 다음 봉 시가에 모의 적용 |
| v2 | stochastic_14_3_recovery | 10000.00 | 0.00 | 대기 /  / 새 신호 대기 |
| v2 | mfi_14_recovery | 10000.00 | 0.00 | 대기 /  / 새 신호 대기 |
| v2 | adx_14_trend | 9981.90 | -18.10 | buy / partial / Wilder ADX14 >= 25 그리고 +DI14 > -DI14; 조건 충족; ADX14=38.0858, plus_DI14=35.3559, minus_DI14=16.277; 직전 완료 봉 목표를 다음 봉 시가에 모의 적용 |
| v2 | aroon_25_trend | 9981.90 | -18.10 | buy / partial / Aroon25 Up > 70 그리고 Down < 30 (동률이면 최신 극값); 조건 충족; Aroon_up=92, Aroon_down=4; 직전 완료 봉 목표를 다음 봉 시가에 모의 적용 |
| v2 | cci_20_momentum | 9952.57 | -47.43 | sell / filled / CCI20 > 100 (전형가격·평균절대편차); 조건 미충족; CCI20=83.6046; 직전 완료 봉 목표를 다음 봉 시가에 모의 적용 |
| v2 | williams_14_recovery | 10000.00 | 0.00 | 대기 /  / 새 신호 대기 |
| v2 | cmf_20_accumulation | 9925.82 | -74.18 | sell / filled / Chaikin Money Flow20 > 0.1; 조건 미충족; CMF20=0.0502896, volume20=2.48879e+06; 직전 완료 봉 목표를 다음 봉 시가에 모의 적용 |
| v2 | chaikin_3_10 | 9961.13 | -38.87 | buy / partial / ADL의 EMA3 - EMA10 > 0 그리고 종가 > EMA26; 조건 충족; Chaikin3_10=75087, ADL=-1.47605e+07, close=523.93, EMA26=520.091; 직전 완료 봉 목표를 다음 봉 시가에 모의 적용 |
| v2 | roc_10_momentum | 10000.00 | 0.00 | 대기 /  / 새 신호 대기 |
| v2 | trix_15_trend | 9981.90 | -18.10 | buy / partial / 15봉 삼중 EMA의 1봉 변화율 TRIX > 0 그리고 종가 > EMA26; 조건 충족; TRIX15_percent=0.0323703, close=521.24, EMA26=519.784; 직전 완료 봉 목표를 다음 봉 시가에 모의 적용 |
| v2 | keltner_20_breakout | 9938.13 | -61.87 | sell / filled / 종가 > EMA20 + 2 x Wilder ATR14; 조건 미충족; close=522.89, upper_Keltner=523.089, EMA20=521.145, ATR14=0.971947; 직전 완료 봉 목표를 다음 봉 시가에 모의 적용 |
| v2 | opening_range_30m | 9978.85 | -21.15 | sell / filled / 뉴욕 09:30·09:45 두 완료 봉 최고가를 10:00 이후 종가가 돌파; 자료 부족·변동폭 또는 거래량 없음: 대기; close=523.93; 직전 완료 봉 목표를 다음 봉 시가에 모의 적용 |

### 같은 기간의 비용·노출 비교 (사후 연구)

| 전략 | 비용 전 | 비용 후 | 100% 보유 | 같은 평균 노출 보유 | 평균 노출 |
|---|---:|---:|---:|---:|---:|
| cash | 0.00% | 0.00% | 0.75% | 0.00% | 0.00% |
| buy_hold | 1.17% | 0.75% | 0.75% | 0.75% | 100.00% |
| trend_8_26 | 1.49% | -3.09% | 0.75% | 0.42% | 55.94% |
| momentum_26 | 0.15% | -3.97% | 0.75% | 0.39% | 52.24% |
| breakout_8 | -0.13% | -17.33% | 0.75% | 0.18% | 23.75% |
| reversion_12 | -1.36% | -9.30% | 0.75% | 0.19% | 24.80% |
| volume_26 | -0.91% | -10.78% | 0.75% | 0.08% | 10.82% |
| trend_8_26 AND momentum_26 | 1.62% | -2.55% | 0.75% | 0.35% | 46.44% |
| trend_8_26 + momentum_26 | 0.82% | -3.53% | 0.75% | 0.41% | 54.09% |
| trend_8_26 AND breakout_8 | 0.44% | -11.82% | 0.75% | 0.12% | 15.57% |
| trend_8_26 + breakout_8 | 0.68% | -10.30% | 0.75% | 0.30% | 39.85% |
| trend_8_26 AND reversion_12 | 0.37% | -4.56% | 0.75% | 0.05% | 6.33% |
| trend_8_26 + reversion_12 | 0.06% | -5.86% | 0.75% | 0.30% | 40.37% |
| trend_8_26 AND volume_26 | 0.65% | -4.30% | 0.75% | 0.04% | 5.01% |
| trend_8_26 + volume_26 | 0.29% | -6.83% | 0.75% | 0.25% | 33.38% |
| momentum_26 AND breakout_8 | -0.36% | -12.15% | 0.75% | 0.12% | 15.83% |
| momentum_26 + breakout_8 | 0.02% | -10.71% | 0.75% | 0.29% | 38.00% |
| momentum_26 AND reversion_12 | -0.18% | -3.88% | 0.75% | 0.04% | 5.80% |
| momentum_26 + reversion_12 | -0.60% | -5.89% | 0.75% | 0.29% | 38.53% |
| momentum_26 AND volume_26 | -0.32% | -5.22% | 0.75% | 0.03% | 4.49% |
| momentum_26 + volume_26 | -0.37% | -6.66% | 0.75% | 0.24% | 31.53% |
| breakout_8 AND reversion_12 | 0.00% | 0.00% | 0.75% | 0.00% | 0.00% |
| breakout_8 + reversion_12 | -0.74% | -13.06% | 0.75% | 0.18% | 24.28% |
| breakout_8 AND volume_26 | -0.87% | -4.55% | 0.75% | 0.02% | 3.17% |
| breakout_8 + volume_26 | -0.51% | -13.40% | 0.75% | 0.13% | 17.29% |
| reversion_12 AND volume_26 | -0.20% | -5.11% | 0.75% | 0.03% | 3.96% |
| reversion_12 + volume_26 | -1.13% | -10.05% | 0.75% | 0.13% | 17.82% |
| ema_12_26 | 0.39% | -2.10% | 0.75% | 0.38% | 50.66% |
| macd_12_26_9 | 1.62% | -1.74% | 0.75% | 0.22% | 29.29% |
| rsi_14_recovery | 0.01% | -2.07% | 0.75% | 0.01% | 1.32% |
| bollinger_20_reentry | -0.25% | -5.16% | 0.75% | 0.02% | 3.17% |
| donchian_20 | 0.36% | -5.77% | 0.75% | 0.06% | 8.18% |
| atr_14_breakout | -1.05% | -8.25% | 0.75% | 0.04% | 5.54% |
| session_vwap | 1.12% | -6.64% | 0.75% | 0.39% | 51.45% |
| obv_20 | 0.17% | -8.29% | 0.75% | 0.34% | 44.59% |
| stochastic_14_3_recovery | 0.79% | -11.14% | 0.75% | 0.06% | 7.92% |
| mfi_14_recovery | -0.06% | -2.95% | 0.75% | 0.01% | 1.85% |
| adx_14_trend | -0.21% | -4.31% | 0.75% | 0.28% | 36.94% |
| aroon_25_trend | 1.15% | -2.60% | 0.75% | 0.19% | 25.59% |
| cci_20_momentum | 0.66% | -5.09% | 0.75% | 0.18% | 24.01% |
| williams_14_recovery | 1.01% | -6.74% | 0.75% | 0.04% | 5.01% |
| cmf_20_accumulation | 0.67% | -6.27% | 0.75% | 0.24% | 32.45% |
| chaikin_3_10 | 1.35% | -8.37% | 0.75% | 0.33% | 43.54% |
| roc_10_momentum | 0.15% | -0.27% | 0.75% | 0.01% | 1.32% |
| trix_15_trend | 0.10% | -3.61% | 0.75% | 0.33% | 43.80% |
| keltner_20_breakout | 0.33% | -5.79% | 0.75% | 0.13% | 16.89% |
| opening_range_30m | 0.90% | -5.26% | 0.75% | 0.17% | 22.96% |

동일 구간·초기 자금, 종료 시 청산 비용 포함. 노출 맞춤은 사후 설명용이며 v2 실제 계좌 성과가 아닙니다.
[낙폭 분해·비용 영향·전체 구간](DIA/comparison.json)

[v1 전체 기록](DIA/accounts.json) · [v2 전체 기록](DIA/accounts-v2.json)

## MSFT 계좌

| 모델 | 전략 | 평가액 USD | 손익 USD | 최근 매매·이유 |
|---|---|---:|---:|---|
| v1 | cash | 10000.00 | 0.00 | 대기 /  / 새 신호 대기 |
| v1 | buy_hold | 9818.08 | -181.92 | buy /  / buy_hold: prior completed bar target 100%; next bar open simulation |
| v1 | trend_8_26 | 9853.68 | -146.32 | sell /  / trend_8_26: prior completed bar target 0%; next bar open simulation |
| v1 | momentum_26 | 9839.32 | -160.68 | sell /  / momentum_26: prior completed bar target 0%; next bar open simulation |
| v1 | breakout_8 | 10000.00 | 0.00 | 대기 /  / 새 신호 대기 |
| v1 | reversion_12 | 9887.71 | -112.29 | buy /  / reversion_12: prior completed bar target 100%; next bar open simulation |
| v1 | volume_26 | 10000.00 | 0.00 | 대기 /  / 새 신호 대기 |
| v1 | trend_8_26 AND momentum_26 | 9853.68 | -146.32 | sell /  / trend_8_26 AND momentum_26: prior completed bar target 0%; next bar open simulation |
| v1 | trend_8_26 + momentum_26 | 9846.52 | -153.48 | sell /  / trend_8_26 + momentum_26: prior completed bar target 0%; next bar open simulation |
| v1 | trend_8_26 AND breakout_8 | 10000.00 | 0.00 | 대기 /  / 새 신호 대기 |
| v1 | trend_8_26 + breakout_8 | 9926.58 | -73.42 | sell /  / trend_8_26 + breakout_8: prior completed bar target 0%; next bar open simulation |
| v1 | trend_8_26 AND reversion_12 | 9923.56 | -76.44 | sell /  / trend_8_26 AND reversion_12: prior completed bar target 0%; next bar open simulation |
| v1 | trend_8_26 + reversion_12 | 9870.69 | -129.31 | buy /  / trend_8_26 + reversion_12: prior completed bar target 50%; next bar open simulation |
| v1 | trend_8_26 AND volume_26 | 10000.00 | 0.00 | 대기 /  / 새 신호 대기 |
| v1 | trend_8_26 + volume_26 | 9926.58 | -73.42 | sell /  / trend_8_26 + volume_26: prior completed bar target 0%; next bar open simulation |
| v1 | momentum_26 AND breakout_8 | 10000.00 | 0.00 | 대기 /  / 새 신호 대기 |
| v1 | momentum_26 + breakout_8 | 9919.33 | -80.67 | sell /  / momentum_26 + breakout_8: prior completed bar target 0%; next bar open simulation |
| v1 | momentum_26 AND reversion_12 | 9909.10 | -90.90 | sell /  / momentum_26 AND reversion_12: prior completed bar target 0%; next bar open simulation |
| v1 | momentum_26 + reversion_12 | 9863.48 | -136.52 | sell /  / momentum_26 + reversion_12: prior completed bar target 50%; next bar open simulation |
| v1 | momentum_26 AND volume_26 | 10000.00 | 0.00 | 대기 /  / 새 신호 대기 |
| v1 | momentum_26 + volume_26 | 9919.33 | -80.67 | sell /  / momentum_26 + volume_26: prior completed bar target 0%; next bar open simulation |
| v1 | breakout_8 AND reversion_12 | 10000.00 | 0.00 | 대기 /  / 새 신호 대기 |
| v1 | breakout_8 + reversion_12 | 9943.67 | -56.33 | buy /  / breakout_8 + reversion_12: prior completed bar target 50%; next bar open simulation |
| v1 | breakout_8 AND volume_26 | 10000.00 | 0.00 | 대기 /  / 새 신호 대기 |
| v1 | breakout_8 + volume_26 | 10000.00 | 0.00 | 대기 /  / 새 신호 대기 |
| v1 | reversion_12 AND volume_26 | 10000.00 | 0.00 | 대기 /  / 새 신호 대기 |
| v1 | reversion_12 + volume_26 | 9943.67 | -56.33 | buy /  / reversion_12 + volume_26: prior completed bar target 50%; next bar open simulation |
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
| v1 | cmf_20_accumulation | 9818.08 | -181.92 | buy /  / Chaikin Money Flow20 > 0.1; 조건 충족; CMF20=0.49076, volume20=5.29606e+07 |
| v1 | chaikin_3_10 | 9889.94 | -110.06 | sell /  / ADL의 EMA3 - EMA10 > 0 그리고 종가 > EMA26; 조건 미충족; Chaikin3_10=3.90601e+06, ADL=1.2345e+08, close=537.34, EMA26=538.834 |
| v1 | roc_10_momentum | 10000.00 | 0.00 | 대기 /  / 새 신호 대기 |
| v1 | trix_15_trend | 9889.94 | -110.06 | sell /  / 15봉 삼중 EMA의 1봉 변화율 TRIX > 0 그리고 종가 > EMA26; 조건 미충족; TRIX15_percent=0.0221169, close=537.34, EMA26=538.834 |
| v1 | keltner_20_breakout | 10000.00 | 0.00 | 대기 /  / 새 신호 대기 |
| v1 | opening_range_30m | 9889.94 | -110.06 | sell /  / 뉴욕 09:30·09:45 두 완료 봉 최고가를 10:00 이후 종가가 돌파; 자료 부족·변동폭 또는 거래량 없음: 대기; close=537.34 |
| v2 | cash | 10000.00 | 0.00 | 대기 /  / 새 신호 대기 |
| v2 | buy_hold | 9871.65 | -128.35 | buy / partial / 직전 완료 봉 목표 비중 100%; 다음 봉 시가 가정 |
| v2 | trend_8_26 | 9790.17 | -209.83 | sell / filled / 직전 완료 봉 목표 비중 0%; 다음 봉 시가 가정 |
| v2 | momentum_26 | 9886.18 | -113.82 | sell / filled / 직전 완료 봉 목표 비중 0%; 다음 봉 시가 가정 |
| v2 | breakout_8 | 9799.48 | -200.52 | sell / filled / 직전 완료 봉 목표 비중 0%; 다음 봉 시가 가정 |
| v2 | reversion_12 | 9509.66 | -490.34 | buy / partial / 직전 완료 봉 목표 비중 100%; 다음 봉 시가 가정 |
| v2 | volume_26 | 9688.55 | -311.45 | sell / filled / 직전 완료 봉 목표 비중 0%; 다음 봉 시가 가정 |
| v2 | trend_8_26 AND momentum_26 | 9751.13 | -248.87 | sell / filled / 직전 완료 봉 목표 비중 0%; 다음 봉 시가 가정 |
| v2 | trend_8_26 + momentum_26 | 9838.34 | -161.66 | sell / filled / 직전 완료 봉 목표 비중 0%; 다음 봉 시가 가정 |
| v2 | trend_8_26 AND breakout_8 | 9639.29 | -360.71 | sell / filled / 직전 완료 봉 목표 비중 0%; 다음 봉 시가 가정 |
| v2 | trend_8_26 + breakout_8 | 9815.63 | -184.37 | sell / filled / 직전 완료 봉 목표 비중 0%; 다음 봉 시가 가정 |
| v2 | trend_8_26 AND reversion_12 | 9822.46 | -177.54 | sell / filled / 직전 완료 봉 목표 비중 0%; 다음 봉 시가 가정 |
| v2 | trend_8_26 + reversion_12 | 9648.58 | -351.42 | buy / filled / 직전 완료 봉 목표 비중 50%; 다음 봉 시가 가정 |
| v2 | trend_8_26 AND volume_26 | 9948.66 | -51.34 | sell / filled / 직전 완료 봉 목표 비중 0%; 다음 봉 시가 가정 |
| v2 | trend_8_26 + volume_26 | 9759.51 | -240.49 | sell / filled / 직전 완료 봉 목표 비중 0%; 다음 봉 시가 가정 |
| v2 | momentum_26 AND breakout_8 | 9794.38 | -205.62 | sell / filled / 직전 완료 봉 목표 비중 0%; 다음 봉 시가 가정 |
| v2 | momentum_26 + breakout_8 | 9842.81 | -157.19 | sell / filled / 직전 완료 봉 목표 비중 0%; 다음 봉 시가 가정 |
| v2 | momentum_26 AND reversion_12 | 9735.61 | -264.39 | sell / filled / 직전 완료 봉 목표 비중 0%; 다음 봉 시가 가정 |
| v2 | momentum_26 + reversion_12 | 9695.89 | -304.11 | sell / filled / 직전 완료 봉 목표 비중 50%; 다음 봉 시가 가정 |
| v2 | momentum_26 AND volume_26 | 9871.26 | -128.74 | sell / filled / 직전 완료 봉 목표 비중 0%; 다음 봉 시가 가정 |
| v2 | momentum_26 + volume_26 | 9807.37 | -192.63 | sell / filled / 직전 완료 봉 목표 비중 0%; 다음 봉 시가 가정 |
| v2 | breakout_8 AND reversion_12 | 10000.00 | 0.00 | 대기 /  / 새 신호 대기 |
| v2 | breakout_8 + reversion_12 | 9673.55 | -326.45 | buy / filled / 직전 완료 봉 목표 비중 50%; 다음 봉 시가 가정 |
| v2 | breakout_8 AND volume_26 | 9938.59 | -61.41 | sell / filled / 직전 완료 봉 목표 비중 0%; 다음 봉 시가 가정 |
| v2 | breakout_8 + volume_26 | 9764.39 | -235.61 | sell / filled / 직전 완료 봉 목표 비중 0%; 다음 봉 시가 가정 |
| v2 | reversion_12 AND volume_26 | 9762.04 | -237.96 | sell / filled / 직전 완료 봉 목표 비중 0%; 다음 봉 시가 가정 |
| v2 | reversion_12 + volume_26 | 9598.52 | -401.48 | buy / filled / 직전 완료 봉 목표 비중 50%; 다음 봉 시가 가정 |
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
| v2 | cmf_20_accumulation | 9817.10 | -182.90 | buy / partial / Chaikin Money Flow20 > 0.1; 조건 충족; CMF20=0.49076, volume20=5.29606e+07; 직전 완료 봉 목표를 다음 봉 시가에 모의 적용 |
| v2 | chaikin_3_10 | 9887.97 | -112.03 | sell / filled / ADL의 EMA3 - EMA10 > 0 그리고 종가 > EMA26; 조건 미충족; Chaikin3_10=3.90601e+06, ADL=1.2345e+08, close=537.34, EMA26=538.834; 직전 완료 봉 목표를 다음 봉 시가에 모의 적용 |
| v2 | roc_10_momentum | 10000.00 | 0.00 | 대기 /  / 새 신호 대기 |
| v2 | trix_15_trend | 9887.97 | -112.03 | sell / filled / 15봉 삼중 EMA의 1봉 변화율 TRIX > 0 그리고 종가 > EMA26; 조건 미충족; TRIX15_percent=0.0221169, close=537.34, EMA26=538.834; 직전 완료 봉 목표를 다음 봉 시가에 모의 적용 |
| v2 | keltner_20_breakout | 10000.00 | 0.00 | 대기 /  / 새 신호 대기 |
| v2 | opening_range_30m | 9887.97 | -112.03 | sell / filled / 뉴욕 09:30·09:45 두 완료 봉 최고가를 10:00 이후 종가가 돌파; 자료 부족·변동폭 또는 거래량 없음: 대기; close=537.34; 직전 완료 봉 목표를 다음 봉 시가에 모의 적용 |

### 같은 기간의 비용·노출 비교 (사후 연구)

| 전략 | 비용 전 | 비용 후 | 100% 보유 | 같은 평균 노출 보유 | 평균 노출 |
|---|---:|---:|---:|---:|---:|
| cash | 0.00% | 0.00% | 2.35% | 0.00% | 0.00% |
| buy_hold | 2.78% | 2.35% | 2.35% | 2.35% | 100.00% |
| trend_8_26 | -1.64% | -5.29% | 2.35% | 1.37% | 58.58% |
| momentum_26 | -0.67% | -6.34% | 2.35% | 1.39% | 59.37% |
| breakout_8 | 5.08% | -9.28% | 2.35% | 0.47% | 20.32% |
| reversion_12 | -4.94% | -13.69% | 2.35% | 0.58% | 25.07% |
| volume_26 | 2.43% | -5.82% | 2.35% | 0.19% | 8.18% |
| trend_8_26 AND momentum_26 | -1.90% | -7.51% | 2.35% | 1.23% | 52.77% |
| trend_8_26 + momentum_26 | -1.15% | -5.80% | 2.35% | 1.38% | 58.97% |
| trend_8_26 AND breakout_8 | 0.67% | -9.36% | 2.35% | 0.31% | 13.19% |
| trend_8_26 + breakout_8 | 1.68% | -6.91% | 2.35% | 0.92% | 39.45% |
| trend_8_26 AND reversion_12 | -3.74% | -9.24% | 2.35% | 0.18% | 7.92% |
| trend_8_26 + reversion_12 | -3.29% | -9.21% | 2.35% | 0.98% | 41.82% |
| trend_8_26 AND volume_26 | 3.46% | 0.46% | 2.35% | 0.06% | 2.64% |
| trend_8_26 + volume_26 | 0.39% | -4.76% | 2.35% | 0.78% | 33.38% |
| momentum_26 AND breakout_8 | 2.61% | -8.01% | 2.35% | 0.31% | 13.46% |
| momentum_26 + breakout_8 | 2.18% | -7.23% | 2.35% | 0.93% | 39.85% |
| momentum_26 AND reversion_12 | -3.23% | -9.52% | 2.35% | 0.22% | 9.50% |
| momentum_26 + reversion_12 | -2.80% | -9.71% | 2.35% | 0.99% | 42.22% |
| momentum_26 AND volume_26 | 1.80% | -2.38% | 2.35% | 0.08% | 3.43% |
| momentum_26 + volume_26 | 0.89% | -4.88% | 2.35% | 0.79% | 33.78% |
| breakout_8 AND reversion_12 | 0.00% | 0.00% | 2.35% | 0.00% | 0.00% |
| breakout_8 + reversion_12 | -0.03% | -10.95% | 2.35% | 0.53% | 22.70% |
| breakout_8 AND volume_26 | 2.07% | -0.47% | 2.35% | 0.04% | 1.85% |
| breakout_8 + volume_26 | 3.76% | -6.59% | 2.35% | 0.33% | 14.25% |
| reversion_12 AND volume_26 | -2.27% | -5.89% | 2.35% | 0.08% | 3.43% |
| reversion_12 + volume_26 | -1.30% | -9.64% | 2.35% | 0.39% | 16.63% |
| ema_12_26 | -1.06% | -4.73% | 2.35% | 1.46% | 62.27% |
| macd_12_26_9 | 0.71% | -4.24% | 2.35% | 0.77% | 32.98% |
| rsi_14_recovery | -0.46% | -1.71% | 2.35% | 0.02% | 0.79% |
| bollinger_20_reentry | -0.45% | -3.34% | 2.35% | 0.04% | 1.85% |
| donchian_20 | 1.84% | -3.17% | 2.35% | 0.10% | 4.49% |
| atr_14_breakout | 1.50% | -3.89% | 2.35% | 0.09% | 3.69% |
| session_vwap | 2.45% | -5.40% | 2.35% | 1.11% | 47.49% |
| obv_20 | 3.85% | -5.71% | 2.35% | 1.22% | 52.24% |
| stochastic_14_3_recovery | -0.11% | -9.68% | 2.35% | 0.15% | 6.33% |
| mfi_14_recovery | 1.04% | -1.88% | 2.35% | 0.04% | 1.85% |
| adx_14_trend | 0.94% | -1.98% | 2.35% | 1.07% | 45.91% |
| aroon_25_trend | -0.07% | -4.98% | 2.35% | 0.50% | 21.64% |
| cci_20_momentum | 2.74% | -3.93% | 2.35% | 0.48% | 20.84% |
| williams_14_recovery | -0.28% | -9.09% | 2.35% | 0.13% | 5.80% |
| cmf_20_accumulation | 0.61% | -5.54% | 2.35% | 0.86% | 36.68% |
| chaikin_3_10 | 3.11% | -5.20% | 2.35% | 1.07% | 45.91% |
| roc_10_momentum | -0.20% | -4.30% | 2.35% | 0.33% | 14.25% |
| trix_15_trend | -1.92% | -5.95% | 2.35% | 1.13% | 48.28% |
| keltner_20_breakout | 1.16% | -4.22% | 2.35% | 0.32% | 13.72% |
| opening_range_30m | -2.37% | -7.56% | 2.35% | 0.58% | 24.80% |

동일 구간·초기 자금, 종료 시 청산 비용 포함. 노출 맞춤은 사후 설명용이며 v2 실제 계좌 성과가 아닙니다.
[낙폭 분해·비용 영향·전체 구간](MSFT/comparison.json)

[v1 전체 기록](MSFT/accounts.json) · [v2 전체 기록](MSFT/accounts-v2.json)

## JPM 계좌

| 모델 | 전략 | 평가액 USD | 손익 USD | 최근 매매·이유 |
|---|---|---:|---:|---|
| v1 | cash | 10000.00 | 0.00 | 대기 /  / 새 신호 대기 |
| v1 | buy_hold | 10102.46 | 102.46 | buy /  / buy_hold: prior completed bar target 100%; next bar open simulation |
| v1 | trend_8_26 | 10102.46 | 102.46 | buy /  / trend_8_26: prior completed bar target 100%; next bar open simulation |
| v1 | momentum_26 | 10102.46 | 102.46 | buy /  / momentum_26: prior completed bar target 100%; next bar open simulation |
| v1 | breakout_8 | 9966.69 | -33.31 | buy /  / breakout_8: prior completed bar target 100%; next bar open simulation |
| v1 | reversion_12 | 10000.00 | 0.00 | 대기 /  / 새 신호 대기 |
| v1 | volume_26 | 10035.68 | 35.68 | sell /  / volume_26: prior completed bar target 0%; next bar open simulation |
| v1 | trend_8_26 AND momentum_26 | 10102.46 | 102.46 | buy /  / trend_8_26 AND momentum_26: prior completed bar target 100%; next bar open simulation |
| v1 | trend_8_26 + momentum_26 | 10102.46 | 102.46 | buy /  / trend_8_26 + momentum_26: prior completed bar target 100%; next bar open simulation |
| v1 | trend_8_26 AND breakout_8 | 9966.69 | -33.31 | buy /  / trend_8_26 AND breakout_8: prior completed bar target 100%; next bar open simulation |
| v1 | trend_8_26 + breakout_8 | 10034.45 | 34.45 | buy /  / trend_8_26 + breakout_8: prior completed bar target 100%; next bar open simulation |
| v1 | trend_8_26 AND reversion_12 | 10000.00 | 0.00 | 대기 /  / 새 신호 대기 |
| v1 | trend_8_26 + reversion_12 | 10051.14 | 51.14 | sell /  / trend_8_26 + reversion_12: prior completed bar target 50%; next bar open simulation |
| v1 | trend_8_26 AND volume_26 | 10035.68 | 35.68 | sell /  / trend_8_26 AND volume_26: prior completed bar target 0%; next bar open simulation |
| v1 | trend_8_26 + volume_26 | 10069.01 | 69.01 | sell /  / trend_8_26 + volume_26: prior completed bar target 50%; next bar open simulation |
| v1 | momentum_26 AND breakout_8 | 9966.69 | -33.31 | buy /  / momentum_26 AND breakout_8: prior completed bar target 100%; next bar open simulation |
| v1 | momentum_26 + breakout_8 | 10034.45 | 34.45 | buy /  / momentum_26 + breakout_8: prior completed bar target 100%; next bar open simulation |
| v1 | momentum_26 AND reversion_12 | 10000.00 | 0.00 | 대기 /  / 새 신호 대기 |
| v1 | momentum_26 + reversion_12 | 10051.14 | 51.14 | sell /  / momentum_26 + reversion_12: prior completed bar target 50%; next bar open simulation |
| v1 | momentum_26 AND volume_26 | 10035.68 | 35.68 | sell /  / momentum_26 AND volume_26: prior completed bar target 0%; next bar open simulation |
| v1 | momentum_26 + volume_26 | 10069.01 | 69.01 | sell /  / momentum_26 + volume_26: prior completed bar target 50%; next bar open simulation |
| v1 | breakout_8 AND reversion_12 | 10000.00 | 0.00 | 대기 /  / 새 신호 대기 |
| v1 | breakout_8 + reversion_12 | 9983.38 | -16.62 | buy /  / breakout_8 + reversion_12: prior completed bar target 50%; next bar open simulation |
| v1 | breakout_8 AND volume_26 | 10035.68 | 35.68 | sell /  / breakout_8 AND volume_26: prior completed bar target 0%; next bar open simulation |
| v1 | breakout_8 + volume_26 | 10001.12 | 1.12 | buy /  / breakout_8 + volume_26: prior completed bar target 50%; next bar open simulation |
| v1 | reversion_12 AND volume_26 | 10000.00 | 0.00 | 대기 /  / 새 신호 대기 |
| v1 | reversion_12 + volume_26 | 10017.88 | 17.88 | sell /  / reversion_12 + volume_26: prior completed bar target 0%; next bar open simulation |
| v1 | ema_12_26 | 10102.46 | 102.46 | buy /  / EMA12 > EMA26; 조건 충족; EMA12=334.708, EMA26=334.451 |
| v1 | macd_12_26_9 | 10102.46 | 102.46 | buy /  / MACD > 신호선 그리고 MACD > 0; 조건 충족; MACD=0.256679, signal9=0.133159 |
| v1 | rsi_14_recovery | 10000.00 | 0.00 | 대기 /  / 새 신호 대기 |
| v1 | bollinger_20_reentry | 10000.00 | 0.00 | 대기 /  / 새 신호 대기 |
| v1 | donchian_20 | 9944.08 | -55.92 | sell /  / 종가 > 현재 봉을 제외한 직전 20봉 최고가; 조건 미충족; close=341.92, prior_high20=343.75 |
| v1 | atr_14_breakout | 9886.92 | -113.08 | sell /  / 종가 > 직전 종가 + 직전 ATR14 그리고 종가 > EMA26; 조건 미충족; close=342.515, threshold=344.598, prior_ATR14=1.50332, EMA26=336.975 |
| v1 | session_vwap | 10016.09 | 16.09 | buy /  / 종가 > 뉴욕 거래일별 누적 전형가격 VWAP; 조건 충족; close=343.095, session_VWAP=341.805, session_volume=2.19743e+06 |
| v1 | obv_20 | 10102.46 | 102.46 | buy /  / OBV > OBV의 SMA20 그리고 종가 > EMA26; 조건 충족; OBV=-1.09065e+07, OBV_SMA20=-1.16181e+07, close=335.52, EMA26=334.451 |
| v1 | stochastic_14_3_recovery | 10000.00 | 0.00 | 대기 /  / 새 신호 대기 |
| v1 | mfi_14_recovery | 10000.00 | 0.00 | 대기 /  / 새 신호 대기 |
| v1 | adx_14_trend | 10008.24 | 8.24 | buy /  / Wilder ADX14 >= 25 그리고 +DI14 > -DI14; 조건 충족; ADX14=26.8739, plus_DI14=46.4083, minus_DI14=10.993 |
| v1 | aroon_25_trend | 10026.36 | 26.36 | buy /  / Aroon25 Up > 70 그리고 Down < 30 (동률이면 최신 극값); 조건 충족; Aroon_up=100, Aroon_down=4 |
| v1 | cci_20_momentum | 10102.46 | 102.46 | buy /  / CCI20 > 100 (전형가격·평균절대편차); 조건 충족; CCI20=154.189 |
| v1 | williams_14_recovery | 10000.00 | 0.00 | 대기 /  / 새 신호 대기 |
| v1 | cmf_20_accumulation | 10026.36 | 26.36 | buy /  / Chaikin Money Flow20 > 0.1; 조건 충족; CMF20=0.219142, volume20=5.48047e+06 |
| v1 | chaikin_3_10 | 10102.46 | 102.46 | buy /  / ADL의 EMA3 - EMA10 > 0 그리고 종가 > EMA26; 조건 충족; Chaikin3_10=213543, ADL=-5.96061e+06, close=335.52, EMA26=334.451 |
| v1 | roc_10_momentum | 10026.36 | 26.36 | buy /  / 10봉 ROC > 1% 그리고 종가 > EMA26; 조건 충족; ROC10_percent=2.4431, close=342.58, EMA26=335.053 |
| v1 | trix_15_trend | 10102.46 | 102.46 | buy /  / 15봉 삼중 EMA의 1봉 변화율 TRIX > 0 그리고 종가 > EMA26; 조건 충족; TRIX15_percent=0.00554135, close=335.52, EMA26=334.451 |
| v1 | keltner_20_breakout | 10026.36 | 26.36 | buy /  / 종가 > EMA20 + 2 x Wilder ATR14; 조건 충족; close=342.58, upper_Keltner=338.352, EMA20=335.297, ATR14=1.5272 |
| v1 | opening_range_30m | 10000.00 | 0.00 | 대기 /  / 새 신호 대기 |
| v2 | cash | 10000.00 | 0.00 | 대기 /  / 새 신호 대기 |
| v2 | buy_hold | 10271.27 | 271.27 | buy / partial / 직전 완료 봉 목표 비중 100%; 다음 봉 시가 가정 |
| v2 | trend_8_26 | 10110.73 | 110.73 | buy / partial / 직전 완료 봉 목표 비중 100%; 다음 봉 시가 가정 |
| v2 | momentum_26 | 9602.03 | -397.97 | buy / partial / 직전 완료 봉 목표 비중 100%; 다음 봉 시가 가정 |
| v2 | breakout_8 | 9299.84 | -700.16 | buy / partial / 직전 완료 봉 목표 비중 100%; 다음 봉 시가 가정 |
| v2 | reversion_12 | 9991.97 | -8.03 | sell / filled / 직전 완료 봉 목표 비중 0%; 다음 봉 시가 가정 |
| v2 | volume_26 | 9859.79 | -140.21 | sell / filled / 직전 완료 봉 목표 비중 0%; 다음 봉 시가 가정 |
| v2 | trend_8_26 AND momentum_26 | 10069.24 | 69.24 | buy / partial / 직전 완료 봉 목표 비중 100%; 다음 봉 시가 가정 |
| v2 | trend_8_26 + momentum_26 | 9874.36 | -125.64 | buy / partial / 직전 완료 봉 목표 비중 100%; 다음 봉 시가 가정 |
| v2 | trend_8_26 AND breakout_8 | 9336.60 | -663.40 | buy / partial / 직전 완료 봉 목표 비중 100%; 다음 봉 시가 가정 |
| v2 | trend_8_26 + breakout_8 | 9697.99 | -302.01 | buy / partial / 직전 완료 봉 목표 비중 100%; 다음 봉 시가 가정 |
| v2 | trend_8_26 AND reversion_12 | 9981.61 | -18.39 | sell / filled / 직전 완료 봉 목표 비중 0%; 다음 봉 시가 가정 |
| v2 | trend_8_26 + reversion_12 | 10093.75 | 93.75 | sell / filled / 직전 완료 봉 목표 비중 50%; 다음 봉 시가 가정 |
| v2 | trend_8_26 AND volume_26 | 9833.30 | -166.70 | sell / filled / 직전 완료 봉 목표 비중 0%; 다음 봉 시가 가정 |
| v2 | trend_8_26 + volume_26 | 9985.32 | -14.68 | sell / filled / 직전 완료 봉 목표 비중 50%; 다음 봉 시가 가정 |
| v2 | momentum_26 AND breakout_8 | 9281.25 | -718.75 | buy / partial / 직전 완료 봉 목표 비중 100%; 다음 봉 시가 가정 |
| v2 | momentum_26 + breakout_8 | 9471.32 | -528.68 | buy / partial / 직전 완료 봉 목표 비중 100%; 다음 봉 시가 가정 |
| v2 | momentum_26 AND reversion_12 | 9950.76 | -49.24 | sell / filled / 직전 완료 봉 목표 비중 0%; 다음 봉 시가 가정 |
| v2 | momentum_26 + reversion_12 | 9919.88 | -80.12 | sell / filled / 직전 완료 봉 목표 비중 50%; 다음 봉 시가 가정 |
| v2 | momentum_26 AND volume_26 | 9833.30 | -166.70 | sell / filled / 직전 완료 봉 목표 비중 0%; 다음 봉 시가 가정 |
| v2 | momentum_26 + volume_26 | 9792.81 | -207.19 | sell / filled / 직전 완료 봉 목표 비중 50%; 다음 봉 시가 가정 |
| v2 | breakout_8 AND reversion_12 | 10000.00 | 0.00 | 대기 /  / 새 신호 대기 |
| v2 | breakout_8 + reversion_12 | 9680.56 | -319.44 | buy / filled / 직전 완료 봉 목표 비중 50%; 다음 봉 시가 가정 |
| v2 | breakout_8 AND volume_26 | 9926.66 | -73.34 | sell / filled / 직전 완료 봉 목표 비중 0%; 다음 봉 시가 가정 |
| v2 | breakout_8 + volume_26 | 9596.00 | -404.00 | buy / filled / 직전 완료 봉 목표 비중 50%; 다음 봉 시가 가정 |
| v2 | reversion_12 AND volume_26 | 10051.38 | 51.38 | sell / filled / 직전 완료 봉 목표 비중 0%; 다음 봉 시가 가정 |
| v2 | reversion_12 + volume_26 | 9946.87 | -53.13 | sell / filled / 직전 완료 봉 목표 비중 0%; 다음 봉 시가 가정 |
| v2 | ema_12_26 | 10101.45 | 101.45 | buy / partial / EMA12 > EMA26; 조건 충족; EMA12=334.708, EMA26=334.451; 직전 완료 봉 목표를 다음 봉 시가에 모의 적용 |
| v2 | macd_12_26_9 | 10101.45 | 101.45 | buy / partial / MACD > 신호선 그리고 MACD > 0; 조건 충족; MACD=0.256679, signal9=0.133159; 직전 완료 봉 목표를 다음 봉 시가에 모의 적용 |
| v2 | rsi_14_recovery | 10000.00 | 0.00 | 대기 /  / 새 신호 대기 |
| v2 | bollinger_20_reentry | 10000.00 | 0.00 | 대기 /  / 새 신호 대기 |
| v2 | donchian_20 | 9942.09 | -57.91 | sell / filled / 종가 > 현재 봉을 제외한 직전 20봉 최고가; 조건 미충족; close=341.92, prior_high20=343.75; 직전 완료 봉 목표를 다음 봉 시가에 모의 적용 |
| v2 | atr_14_breakout | 9882.97 | -117.03 | sell / filled / 종가 > 직전 종가 + 직전 ATR14 그리고 종가 > EMA26; 조건 미충족; close=342.515, threshold=344.598, prior_ATR14=1.50332, EMA26=336.975; 직전 완료 봉 목표를 다음 봉 시가에 모의 적용 |
| v2 | session_vwap | 10013.09 | 13.09 | buy / partial / 종가 > 뉴욕 거래일별 누적 전형가격 VWAP; 조건 충족; close=343.095, session_VWAP=341.805, session_volume=2.19743e+06; 직전 완료 봉 목표를 다음 봉 시가에 모의 적용 |
| v2 | obv_20 | 10101.45 | 101.45 | buy / partial / OBV > OBV의 SMA20 그리고 종가 > EMA26; 조건 충족; OBV=-1.09065e+07, OBV_SMA20=-1.16181e+07, close=335.52, EMA26=334.451; 직전 완료 봉 목표를 다음 봉 시가에 모의 적용 |
| v2 | stochastic_14_3_recovery | 10000.00 | 0.00 | 대기 /  / 새 신호 대기 |
| v2 | mfi_14_recovery | 10000.00 | 0.00 | 대기 /  / 새 신호 대기 |
| v2 | adx_14_trend | 10007.24 | 7.24 | buy / partial / Wilder ADX14 >= 25 그리고 +DI14 > -DI14; 조건 충족; ADX14=26.8739, plus_DI14=46.4083, minus_DI14=10.993; 직전 완료 봉 목표를 다음 봉 시가에 모의 적용 |
| v2 | aroon_25_trend | 10025.36 | 25.36 | buy / partial / Aroon25 Up > 70 그리고 Down < 30 (동률이면 최신 극값); 조건 충족; Aroon_up=100, Aroon_down=4; 직전 완료 봉 목표를 다음 봉 시가에 모의 적용 |
| v2 | cci_20_momentum | 10101.45 | 101.45 | buy / partial / CCI20 > 100 (전형가격·평균절대편차); 조건 충족; CCI20=154.189; 직전 완료 봉 목표를 다음 봉 시가에 모의 적용 |
| v2 | williams_14_recovery | 10000.00 | 0.00 | 대기 /  / 새 신호 대기 |
| v2 | cmf_20_accumulation | 10025.36 | 25.36 | buy / partial / Chaikin Money Flow20 > 0.1; 조건 충족; CMF20=0.219142, volume20=5.48047e+06; 직전 완료 봉 목표를 다음 봉 시가에 모의 적용 |
| v2 | chaikin_3_10 | 10101.45 | 101.45 | buy / partial / ADL의 EMA3 - EMA10 > 0 그리고 종가 > EMA26; 조건 충족; Chaikin3_10=213543, ADL=-5.96061e+06, close=335.52, EMA26=334.451; 직전 완료 봉 목표를 다음 봉 시가에 모의 적용 |
| v2 | roc_10_momentum | 10025.36 | 25.36 | buy / partial / 10봉 ROC > 1% 그리고 종가 > EMA26; 조건 충족; ROC10_percent=2.4431, close=342.58, EMA26=335.053; 직전 완료 봉 목표를 다음 봉 시가에 모의 적용 |
| v2 | trix_15_trend | 10101.45 | 101.45 | buy / partial / 15봉 삼중 EMA의 1봉 변화율 TRIX > 0 그리고 종가 > EMA26; 조건 충족; TRIX15_percent=0.00554135, close=335.52, EMA26=334.451; 직전 완료 봉 목표를 다음 봉 시가에 모의 적용 |
| v2 | keltner_20_breakout | 10025.36 | 25.36 | buy / partial / 종가 > EMA20 + 2 x Wilder ATR14; 조건 충족; close=342.58, upper_Keltner=338.352, EMA20=335.297, ATR14=1.5272; 직전 완료 봉 목표를 다음 봉 시가에 모의 적용 |
| v2 | opening_range_30m | 10000.00 | 0.00 | 대기 /  / 새 신호 대기 |

### 같은 기간의 비용·노출 비교 (사후 연구)

| 전략 | 비용 전 | 비용 후 | 100% 보유 | 같은 평균 노출 보유 | 평균 노출 |
|---|---:|---:|---:|---:|---:|
| cash | 0.00% | 0.00% | 0.30% | 0.00% | 0.00% |
| buy_hold | 0.72% | 0.30% | 0.30% | 0.30% | 100.00% |
| trend_8_26 | 2.28% | -1.93% | 0.30% | 0.16% | 52.24% |
| momentum_26 | -0.83% | -7.66% | 0.30% | 0.14% | 46.70% |
| breakout_8 | -3.48% | -18.75% | 0.30% | 0.06% | 20.05% |
| reversion_12 | 4.63% | -9.67% | 0.30% | 0.08% | 26.65% |
| volume_26 | -0.11% | -6.20% | 0.30% | 0.02% | 6.86% |
| trend_8_26 AND momentum_26 | 2.37% | -2.66% | 0.30% | 0.12% | 40.90% |
| trend_8_26 + momentum_26 | 0.72% | -4.63% | 0.30% | 0.15% | 49.48% |
| trend_8_26 AND breakout_8 | -3.52% | -14.23% | 0.30% | 0.04% | 12.66% |
| trend_8_26 + breakout_8 | -0.63% | -10.53% | 0.30% | 0.11% | 36.15% |
| trend_8_26 AND reversion_12 | 2.82% | -3.46% | 0.30% | 0.02% | 6.60% |
| trend_8_26 + reversion_12 | 3.47% | -5.29% | 0.30% | 0.12% | 39.45% |
| trend_8_26 AND volume_26 | -0.58% | -4.67% | 0.30% | 0.01% | 4.22% |
| trend_8_26 + volume_26 | 1.10% | -4.08% | 0.30% | 0.09% | 29.55% |
| momentum_26 AND breakout_8 | -2.36% | -13.20% | 0.30% | 0.04% | 12.40% |
| momentum_26 + breakout_8 | -2.14% | -13.18% | 0.30% | 0.10% | 33.38% |
| momentum_26 AND reversion_12 | 2.89% | -3.80% | 0.30% | 0.02% | 5.54% |
| momentum_26 + reversion_12 | 1.89% | -7.12% | 0.30% | 0.11% | 36.68% |
| momentum_26 AND volume_26 | 0.21% | -2.70% | 0.30% | 0.01% | 2.90% |
| momentum_26 + volume_26 | -0.44% | -6.34% | 0.30% | 0.08% | 26.79% |
| breakout_8 AND reversion_12 | 0.00% | 0.00% | 0.30% | 0.00% | 0.00% |
| breakout_8 + reversion_12 | 0.52% | -12.88% | 0.30% | 0.07% | 23.36% |
| breakout_8 AND volume_26 | -0.51% | -2.17% | 0.30% | 0.00% | 1.06% |
| breakout_8 + volume_26 | -1.79% | -11.59% | 0.30% | 0.04% | 13.46% |
| reversion_12 AND volume_26 | 1.25% | -2.10% | 0.30% | 0.01% | 3.43% |
| reversion_12 + volume_26 | 2.25% | -7.18% | 0.30% | 0.05% | 16.76% |
| ema_12_26 | 1.93% | -1.44% | 0.30% | 0.15% | 48.55% |
| macd_12_26_9 | 1.95% | -2.66% | 0.30% | 0.09% | 30.08% |
| rsi_14_recovery | 0.14% | -2.35% | 0.30% | 0.00% | 1.58% |
| bollinger_20_reentry | 0.44% | -5.30% | 0.30% | 0.01% | 3.69% |
| donchian_20 | -1.47% | -3.92% | 0.30% | 0.01% | 2.64% |
| atr_14_breakout | -1.13% | -7.55% | 0.30% | 0.01% | 4.49% |
| session_vwap | 1.62% | -8.12% | 0.30% | 0.15% | 49.34% |
| obv_20 | -3.24% | -14.70% | 0.30% | 0.10% | 31.66% |
| stochastic_14_3_recovery | -1.86% | -12.75% | 0.30% | 0.02% | 7.39% |
| mfi_14_recovery | 0.16% | -1.50% | 0.30% | 0.00% | 1.06% |
| adx_14_trend | -1.35% | -4.61% | 0.30% | 0.08% | 27.70% |
| aroon_25_trend | 0.22% | -4.71% | 0.30% | 0.06% | 21.37% |
| cci_20_momentum | -2.29% | -10.16% | 0.30% | 0.05% | 15.04% |
| williams_14_recovery | -2.54% | -12.98% | 0.30% | 0.02% | 7.12% |
| cmf_20_accumulation | -2.21% | -10.84% | 0.30% | 0.11% | 35.09% |
| chaikin_3_10 | 2.32% | -6.32% | 0.30% | 0.10% | 34.56% |
| roc_10_momentum | -0.06% | -2.55% | 0.30% | 0.02% | 6.86% |
| trix_15_trend | 0.88% | -6.07% | 0.30% | 0.11% | 34.83% |
| keltner_20_breakout | -0.60% | -3.08% | 0.30% | 0.01% | 3.43% |
| opening_range_30m | -0.01% | -3.72% | 0.30% | 0.06% | 18.47% |

동일 구간·초기 자금, 종료 시 청산 비용 포함. 노출 맞춤은 사후 설명용이며 v2 실제 계좌 성과가 아닙니다.
[낙폭 분해·비용 영향·전체 구간](JPM/comparison.json)

[v1 전체 기록](JPM/accounts.json) · [v2 전체 기록](JPM/accounts-v2.json)

## XOM 계좌

| 모델 | 전략 | 평가액 USD | 손익 USD | 최근 매매·이유 |
|---|---|---:|---:|---|
| v1 | cash | 10000.00 | 0.00 | 대기 /  / 새 신호 대기 |
| v1 | buy_hold | 9952.60 | -47.40 | buy /  / buy_hold: prior completed bar target 100%; next bar open simulation |
| v1 | trend_8_26 | 10013.03 | 13.03 | buy /  / trend_8_26: prior completed bar target 100%; next bar open simulation |
| v1 | momentum_26 | 9980.03 | -19.97 | buy /  / momentum_26: prior completed bar target 100%; next bar open simulation |
| v1 | breakout_8 | 9844.91 | -155.09 | buy /  / breakout_8: prior completed bar target 100%; next bar open simulation |
| v1 | reversion_12 | 10000.00 | 0.00 | 대기 /  / 새 신호 대기 |
| v1 | volume_26 | 9903.93 | -96.07 | sell /  / volume_26: prior completed bar target 0%; next bar open simulation |
| v1 | trend_8_26 AND momentum_26 | 10013.03 | 13.03 | buy /  / trend_8_26 AND momentum_26: prior completed bar target 100%; next bar open simulation |
| v1 | trend_8_26 + momentum_26 | 9996.50 | -3.50 | buy /  / trend_8_26 + momentum_26: prior completed bar target 100%; next bar open simulation |
| v1 | trend_8_26 AND breakout_8 | 9966.44 | -33.56 | buy /  / trend_8_26 AND breakout_8: prior completed bar target 100%; next bar open simulation |
| v1 | trend_8_26 + breakout_8 | 9948.49 | -51.51 | buy /  / trend_8_26 + breakout_8: prior completed bar target 100%; next bar open simulation |
| v1 | trend_8_26 AND reversion_12 | 10000.00 | 0.00 | 대기 /  / 새 신호 대기 |
| v1 | trend_8_26 + reversion_12 | 10006.49 | 6.49 | sell /  / trend_8_26 + reversion_12: prior completed bar target 50%; next bar open simulation |
| v1 | trend_8_26 AND volume_26 | 10000.00 | 0.00 | 대기 /  / 새 신호 대기 |
| v1 | trend_8_26 + volume_26 | 9958.29 | -41.71 | sell /  / trend_8_26 + volume_26: prior completed bar target 50%; next bar open simulation |
| v1 | momentum_26 AND breakout_8 | 9893.94 | -106.06 | buy /  / momentum_26 AND breakout_8: prior completed bar target 100%; next bar open simulation |
| v1 | momentum_26 + breakout_8 | 9912.26 | -87.74 | buy /  / momentum_26 + breakout_8: prior completed bar target 100%; next bar open simulation |
| v1 | momentum_26 AND reversion_12 | 10000.00 | 0.00 | 대기 /  / 새 신호 대기 |
| v1 | momentum_26 + reversion_12 | 9989.99 | -10.01 | sell /  / momentum_26 + reversion_12: prior completed bar target 50%; next bar open simulation |
| v1 | momentum_26 AND volume_26 | 10000.00 | 0.00 | 대기 /  / 새 신호 대기 |
| v1 | momentum_26 + volume_26 | 9941.87 | -58.13 | sell /  / momentum_26 + volume_26: prior completed bar target 50%; next bar open simulation |
| v1 | breakout_8 AND reversion_12 | 10000.00 | 0.00 | 대기 /  / 새 신호 대기 |
| v1 | breakout_8 + reversion_12 | 9922.11 | -77.89 | buy /  / breakout_8 + reversion_12: prior completed bar target 50%; next bar open simulation |
| v1 | breakout_8 AND volume_26 | 9950.44 | -49.56 | sell /  / breakout_8 AND volume_26: prior completed bar target 0%; next bar open simulation |
| v1 | breakout_8 + volume_26 | 9874.33 | -125.67 | buy /  / breakout_8 + volume_26: prior completed bar target 50%; next bar open simulation |
| v1 | reversion_12 AND volume_26 | 10000.00 | 0.00 | 대기 /  / 새 신호 대기 |
| v1 | reversion_12 + volume_26 | 9951.83 | -48.17 | sell /  / reversion_12 + volume_26: prior completed bar target 0%; next bar open simulation |
| v1 | ema_12_26 | 10010.17 | 10.17 | buy /  / EMA12 > EMA26; 조건 충족; EMA12=175.145, EMA26=175.141 |
| v1 | macd_12_26_9 | 10010.17 | 10.17 | buy /  / MACD > 신호선 그리고 MACD > 0; 조건 충족; MACD=0.00418876, signal9=-0.17046 |
| v1 | rsi_14_recovery | 10000.00 | 0.00 | 대기 /  / 새 신호 대기 |
| v1 | bollinger_20_reentry | 9913.52 | -86.48 | sell /  / 직전 종가 < 직전 하단밴드, 현재 하단밴드 <= 종가 <= SMA20 (한 봉 목표); 조건 미충족; close=175.71, lower20=173.907, SMA20=174.743, previous_lower20=173.977 |
| v1 | donchian_20 | 9950.44 | -49.56 | sell /  / 종가 > 현재 봉을 제외한 직전 20봉 최고가; 조건 미충족; close=175.56, prior_high20=177.365 |
| v1 | atr_14_breakout | 9917.05 | -82.95 | buy /  / 종가 > 직전 종가 + 직전 ATR14 그리고 종가 > EMA26; 조건 충족; close=176.252, threshold=176.178, prior_ATR14=0.717416, EMA26=175.223 |
| v1 | session_vwap | 9966.44 | -33.56 | buy /  / 종가 > 뉴욕 거래일별 누적 전형가격 VWAP; 조건 충족; close=176.252, session_VWAP=176.004, session_volume=3.15024e+06 |
| v1 | obv_20 | 9999.35 | -0.65 | buy /  / OBV > OBV의 SMA20 그리고 종가 > EMA26; 조건 충족; OBV=2.28535e+07, OBV_SMA20=2.0753e+07, close=175.71, EMA26=174.973 |
| v1 | stochastic_14_3_recovery | 10000.00 | 0.00 | 대기 /  / 새 신호 대기 |
| v1 | mfi_14_recovery | 10000.00 | 0.00 | 대기 /  / 새 신호 대기 |
| v1 | adx_14_trend | 10000.00 | 0.00 | 대기 /  / 새 신호 대기 |
| v1 | aroon_25_trend | 10000.00 | 0.00 | 대기 /  / 새 신호 대기 |
| v1 | cci_20_momentum | 9915.92 | -84.08 | buy /  / CCI20 > 100 (전형가격·평균절대편차); 조건 충족; CCI20=126.554 |
| v1 | williams_14_recovery | 9913.52 | -86.48 | sell /  / 직전 Williams %R14 < -80, 현재 >= -80 (한 봉 목표); 조건 미충족; Williams_R14=-43.9575, previous_R14=-33.1215 |
| v1 | cmf_20_accumulation | 10000.00 | 0.00 | 대기 /  / 새 신호 대기 |
| v1 | chaikin_3_10 | 10000.00 | 0.00 | 대기 /  / 새 신호 대기 |
| v1 | roc_10_momentum | 10000.00 | 0.00 | 대기 /  / 새 신호 대기 |
| v1 | trix_15_trend | 10000.00 | 0.00 | 대기 /  / 새 신호 대기 |
| v1 | keltner_20_breakout | 10000.00 | 0.00 | 대기 /  / 새 신호 대기 |
| v1 | opening_range_30m | 10000.00 | 0.00 | 대기 /  / 새 신호 대기 |
| v2 | cash | 10000.00 | 0.00 | 대기 /  / 새 신호 대기 |
| v2 | buy_hold | 10270.22 | 270.22 | buy / partial / 직전 완료 봉 목표 비중 100%; 다음 봉 시가 가정 |
| v2 | trend_8_26 | 10108.40 | 108.40 | buy / partial / 직전 완료 봉 목표 비중 100%; 다음 봉 시가 가정 |
| v2 | momentum_26 | 10151.31 | 151.31 | buy / partial / 직전 완료 봉 목표 비중 100%; 다음 봉 시가 가정 |
| v2 | breakout_8 | 9319.47 | -680.53 | buy / partial / 직전 완료 봉 목표 비중 100%; 다음 봉 시가 가정 |
| v2 | reversion_12 | 9815.06 | -184.94 | sell / filled / 직전 완료 봉 목표 비중 0%; 다음 봉 시가 가정 |
| v2 | volume_26 | 9810.89 | -189.11 | sell / filled / 직전 완료 봉 목표 비중 0%; 다음 봉 시가 가정 |
| v2 | trend_8_26 AND momentum_26 | 10115.89 | 115.89 | buy / partial / 직전 완료 봉 목표 비중 100%; 다음 봉 시가 가정 |
| v2 | trend_8_26 + momentum_26 | 10129.84 | 129.84 | buy / partial / 직전 완료 봉 목표 비중 100%; 다음 봉 시가 가정 |
| v2 | trend_8_26 AND breakout_8 | 9421.06 | -578.94 | buy / partial / 직전 완료 봉 목표 비중 100%; 다음 봉 시가 가정 |
| v2 | trend_8_26 + breakout_8 | 9747.15 | -252.85 | buy / partial / 직전 완료 봉 목표 비중 100%; 다음 봉 시가 가정 |
| v2 | trend_8_26 AND reversion_12 | 9839.70 | -160.30 | sell / filled / 직전 완료 봉 목표 비중 0%; 다음 봉 시가 가정 |
| v2 | trend_8_26 + reversion_12 | 9960.72 | -39.28 | sell / filled / 직전 완료 봉 목표 비중 50%; 다음 봉 시가 가정 |
| v2 | trend_8_26 AND volume_26 | 9895.61 | -104.39 | sell / filled / 직전 완료 봉 목표 비중 0%; 다음 봉 시가 가정 |
| v2 | trend_8_26 + volume_26 | 9958.45 | -41.55 | sell / filled / 직전 완료 봉 목표 비중 50%; 다음 봉 시가 가정 |
| v2 | momentum_26 AND breakout_8 | 9367.76 | -632.24 | buy / partial / 직전 완료 봉 목표 비중 100%; 다음 봉 시가 가정 |
| v2 | momentum_26 + breakout_8 | 9727.06 | -272.94 | buy / partial / 직전 완료 봉 목표 비중 100%; 다음 봉 시가 가정 |
| v2 | momentum_26 AND reversion_12 | 9800.13 | -199.87 | sell / filled / 직전 완료 봉 목표 비중 0%; 다음 봉 시가 가정 |
| v2 | momentum_26 + reversion_12 | 9981.87 | -18.13 | sell / filled / 직전 완료 봉 목표 비중 50%; 다음 봉 시가 가정 |
| v2 | momentum_26 AND volume_26 | 9957.96 | -42.04 | sell / filled / 직전 완료 봉 목표 비중 0%; 다음 봉 시가 가정 |
| v2 | momentum_26 + volume_26 | 10000.53 | 0.53 | sell / filled / 직전 완료 봉 목표 비중 50%; 다음 봉 시가 가정 |
| v2 | breakout_8 AND reversion_12 | 10000.00 | 0.00 | 대기 /  / 새 신호 대기 |
| v2 | breakout_8 + reversion_12 | 9563.92 | -436.08 | buy / filled / 직전 완료 봉 목표 비중 50%; 다음 봉 시가 가정 |
| v2 | breakout_8 AND volume_26 | 9918.86 | -81.14 | sell / filled / 직전 완료 봉 목표 비중 0%; 다음 봉 시가 가정 |
| v2 | breakout_8 + volume_26 | 9581.99 | -418.01 | buy / filled / 직전 완료 봉 목표 비중 50%; 다음 봉 시가 가정 |
| v2 | reversion_12 AND volume_26 | 9949.87 | -50.13 | sell / filled / 직전 완료 봉 목표 비중 0%; 다음 봉 시가 가정 |
| v2 | reversion_12 + volume_26 | 9833.62 | -166.38 | sell / filled / 직전 완료 봉 목표 비중 0%; 다음 봉 시가 가정 |
| v2 | ema_12_26 | 10009.17 | 9.17 | buy / partial / EMA12 > EMA26; 조건 충족; EMA12=175.145, EMA26=175.141; 직전 완료 봉 목표를 다음 봉 시가에 모의 적용 |
| v2 | macd_12_26_9 | 10009.17 | 9.17 | buy / partial / MACD > 신호선 그리고 MACD > 0; 조건 충족; MACD=0.00418876, signal9=-0.17046; 직전 완료 봉 목표를 다음 봉 시가에 모의 적용 |
| v2 | rsi_14_recovery | 10000.00 | 0.00 | 대기 /  / 새 신호 대기 |
| v2 | bollinger_20_reentry | 9911.54 | -88.46 | sell / filled / 직전 종가 < 직전 하단밴드, 현재 하단밴드 <= 종가 <= SMA20 (한 봉 목표); 조건 미충족; close=175.71, lower20=173.907, SMA20=174.743, previous_lower20=173.977; 직전 완료 봉 목표를 다음 봉 시가에 모의 적용 |
| v2 | donchian_20 | 9948.45 | -51.55 | sell / filled / 종가 > 현재 봉을 제외한 직전 20봉 최고가; 조건 미충족; close=175.56, prior_high20=177.365; 직전 완료 봉 목표를 다음 봉 시가에 모의 적용 |
| v2 | atr_14_breakout | 9914.07 | -85.93 | buy / partial / 종가 > 직전 종가 + 직전 ATR14 그리고 종가 > EMA26; 조건 충족; close=176.252, threshold=176.178, prior_ATR14=0.717416, EMA26=175.223; 직전 완료 봉 목표를 다음 봉 시가에 모의 적용 |
| v2 | session_vwap | 9965.44 | -34.56 | buy / partial / 종가 > 뉴욕 거래일별 누적 전형가격 VWAP; 조건 충족; close=176.252, session_VWAP=176.004, session_volume=3.15024e+06; 직전 완료 봉 목표를 다음 봉 시가에 모의 적용 |
| v2 | obv_20 | 9998.35 | -1.65 | buy / partial / OBV > OBV의 SMA20 그리고 종가 > EMA26; 조건 충족; OBV=2.28535e+07, OBV_SMA20=2.0753e+07, close=175.71, EMA26=174.973; 직전 완료 봉 목표를 다음 봉 시가에 모의 적용 |
| v2 | stochastic_14_3_recovery | 10000.00 | 0.00 | 대기 /  / 새 신호 대기 |
| v2 | mfi_14_recovery | 10000.00 | 0.00 | 대기 /  / 새 신호 대기 |
| v2 | adx_14_trend | 10000.00 | 0.00 | 대기 /  / 새 신호 대기 |
| v2 | aroon_25_trend | 10000.00 | 0.00 | 대기 /  / 새 신호 대기 |
| v2 | cci_20_momentum | 9912.94 | -87.06 | buy / partial / CCI20 > 100 (전형가격·평균절대편차); 조건 충족; CCI20=126.554; 직전 완료 봉 목표를 다음 봉 시가에 모의 적용 |
| v2 | williams_14_recovery | 9911.54 | -88.46 | sell / filled / 직전 Williams %R14 < -80, 현재 >= -80 (한 봉 목표); 조건 미충족; Williams_R14=-43.9575, previous_R14=-33.1215; 직전 완료 봉 목표를 다음 봉 시가에 모의 적용 |
| v2 | cmf_20_accumulation | 10000.00 | 0.00 | 대기 /  / 새 신호 대기 |
| v2 | chaikin_3_10 | 10000.00 | 0.00 | 대기 /  / 새 신호 대기 |
| v2 | roc_10_momentum | 10000.00 | 0.00 | 대기 /  / 새 신호 대기 |
| v2 | trix_15_trend | 10000.00 | 0.00 | 대기 /  / 새 신호 대기 |
| v2 | keltner_20_breakout | 10000.00 | 0.00 | 대기 /  / 새 신호 대기 |
| v2 | opening_range_30m | 10000.00 | 0.00 | 대기 /  / 새 신호 대기 |

### 같은 기간의 비용·노출 비교 (사후 연구)

| 전략 | 비용 전 | 비용 후 | 100% 보유 | 같은 평균 노출 보유 | 평균 노출 |
|---|---:|---:|---:|---:|---:|
| cash | 0.00% | 0.00% | 9.43% | 0.00% | 0.00% |
| buy_hold | 9.89% | 9.43% | 9.43% | 9.43% | 100.00% |
| trend_8_26 | 1.33% | -3.24% | 9.43% | 5.93% | 63.85% |
| momentum_26 | 0.22% | -7.08% | 9.43% | 6.49% | 69.66% |
| breakout_8 | -3.45% | -21.08% | 9.43% | 2.14% | 23.48% |
| reversion_12 | 7.01% | -3.65% | 9.43% | 1.90% | 20.84% |
| volume_26 | 3.92% | -3.64% | 9.43% | 0.45% | 5.01% |
| trend_8_26 AND momentum_26 | -0.13% | -5.03% | 9.43% | 5.43% | 58.58% |
| trend_8_26 + momentum_26 | 0.78% | -4.97% | 9.43% | 6.21% | 66.76% |
| trend_8_26 AND breakout_8 | -1.33% | -15.18% | 9.43% | 1.66% | 18.21% |
| trend_8_26 + breakout_8 | -1.06% | -12.23% | 9.43% | 4.02% | 43.67% |
| trend_8_26 AND reversion_12 | 1.89% | -3.93% | 9.43% | 0.74% | 8.18% |
| trend_8_26 + reversion_12 | 4.16% | -3.24% | 9.43% | 3.90% | 42.35% |
| trend_8_26 AND volume_26 | 2.54% | -1.67% | 9.43% | 0.24% | 2.64% |
| trend_8_26 + volume_26 | 2.64% | -3.04% | 9.43% | 3.16% | 34.44% |
| momentum_26 AND breakout_8 | -3.52% | -19.46% | 9.43% | 1.93% | 21.11% |
| momentum_26 + breakout_8 | -1.61% | -14.35% | 9.43% | 4.30% | 46.58% |
| momentum_26 AND reversion_12 | 2.27% | -4.38% | 9.43% | 0.81% | 8.97% |
| momentum_26 + reversion_12 | 3.59% | -3.98% | 9.43% | 4.17% | 45.26% |
| momentum_26 AND volume_26 | 2.32% | -1.47% | 9.43% | 0.21% | 2.37% |
| momentum_26 + volume_26 | 2.08% | -3.97% | 9.43% | 3.43% | 37.34% |
| breakout_8 AND reversion_12 | 0.00% | 0.00% | 9.43% | 0.00% | 0.00% |
| breakout_8 + reversion_12 | 1.67% | -12.62% | 9.43% | 2.02% | 22.17% |
| breakout_8 AND volume_26 | 0.51% | -1.17% | 9.43% | 0.10% | 1.06% |
| breakout_8 + volume_26 | 0.18% | -11.69% | 9.43% | 1.30% | 14.26% |
| reversion_12 AND volume_26 | 1.52% | -1.00% | 9.43% | 0.14% | 1.58% |
| reversion_12 + volume_26 | 5.47% | -2.83% | 9.43% | 1.18% | 12.93% |
| ema_12_26 | -0.17% | -3.47% | 9.43% | 6.84% | 73.35% |
| macd_12_26_9 | -1.26% | -6.90% | 9.43% | 3.59% | 39.05% |
| rsi_14_recovery | -0.15% | -0.57% | 9.43% | 0.02% | 0.26% |
| bollinger_20_reentry | -0.87% | -3.75% | 9.43% | 0.17% | 1.85% |
| donchian_20 | -1.09% | -9.82% | 9.43% | 0.81% | 8.97% |
| atr_14_breakout | -1.34% | -10.43% | 9.43% | 0.57% | 6.33% |
| session_vwap | -0.98% | -12.70% | 9.43% | 6.03% | 64.91% |
| obv_20 | 2.21% | -5.23% | 9.43% | 3.89% | 42.22% |
| stochastic_14_3_recovery | 1.60% | -6.97% | 9.43% | 0.50% | 5.54% |
| mfi_14_recovery | -0.31% | -1.97% | 9.43% | 0.10% | 1.06% |
| adx_14_trend | 0.84% | -1.67% | 9.43% | 3.84% | 41.69% |
| aroon_25_trend | -1.78% | -7.78% | 9.43% | 2.80% | 30.61% |
| cci_20_momentum | 2.81% | -4.68% | 9.43% | 2.41% | 26.39% |
| williams_14_recovery | 0.13% | -5.59% | 9.43% | 0.33% | 3.69% |
| cmf_20_accumulation | 2.09% | -6.53% | 9.43% | 4.75% | 51.45% |
| chaikin_3_10 | -1.00% | -9.36% | 9.43% | 5.13% | 55.41% |
| roc_10_momentum | -0.19% | -5.50% | 9.43% | 1.22% | 13.46% |
| trix_15_trend | -2.63% | -9.34% | 9.43% | 5.73% | 61.74% |
| keltner_20_breakout | -0.86% | -7.30% | 9.43% | 1.37% | 15.04% |
| opening_range_30m | -0.36% | -9.53% | 9.43% | 3.29% | 35.88% |

동일 구간·초기 자금, 종료 시 청산 비용 포함. 노출 맞춤은 사후 설명용이며 v2 실제 계좌 성과가 아닙니다.
[낙폭 분해·비용 영향·전체 구간](XOM/comparison.json)

[v1 전체 기록](XOM/accounts.json) · [v2 전체 기록](XOM/accounts-v2.json)

## JNJ 계좌

| 모델 | 전략 | 평가액 USD | 손익 USD | 최근 매매·이유 |
|---|---|---:|---:|---|
| v1 | cash | 10000.00 | 0.00 | 대기 /  / 새 신호 대기 |
| v1 | buy_hold | 10025.73 | 25.73 | buy /  / buy_hold: prior completed bar target 100%; next bar open simulation |
| v1 | trend_8_26 | 9979.64 | -20.36 | buy /  / trend_8_26: prior completed bar target 100%; next bar open simulation |
| v1 | momentum_26 | 10000.00 | 0.00 | 대기 /  / 새 신호 대기 |
| v1 | breakout_8 | 9883.97 | -116.03 | sell /  / breakout_8: prior completed bar target 0%; next bar open simulation |
| v1 | reversion_12 | 10000.00 | 0.00 | 대기 /  / 새 신호 대기 |
| v1 | volume_26 | 10000.00 | 0.00 | 대기 /  / 새 신호 대기 |
| v1 | trend_8_26 AND momentum_26 | 10000.00 | 0.00 | 대기 /  / 새 신호 대기 |
| v1 | trend_8_26 + momentum_26 | 9989.80 | -10.20 | buy /  / trend_8_26 + momentum_26: prior completed bar target 50%; next bar open simulation |
| v1 | trend_8_26 AND breakout_8 | 10000.00 | 0.00 | 대기 /  / 새 신호 대기 |
| v1 | trend_8_26 + breakout_8 | 9931.65 | -68.35 | buy /  / trend_8_26 + breakout_8: prior completed bar target 50%; next bar open simulation |
| v1 | trend_8_26 AND reversion_12 | 10000.00 | 0.00 | 대기 /  / 새 신호 대기 |
| v1 | trend_8_26 + reversion_12 | 9989.80 | -10.20 | buy /  / trend_8_26 + reversion_12: prior completed bar target 50%; next bar open simulation |
| v1 | trend_8_26 AND volume_26 | 10000.00 | 0.00 | 대기 /  / 새 신호 대기 |
| v1 | trend_8_26 + volume_26 | 9989.80 | -10.20 | buy /  / trend_8_26 + volume_26: prior completed bar target 50%; next bar open simulation |
| v1 | momentum_26 AND breakout_8 | 10000.00 | 0.00 | 대기 /  / 새 신호 대기 |
| v1 | momentum_26 + breakout_8 | 9941.79 | -58.21 | sell /  / momentum_26 + breakout_8: prior completed bar target 0%; next bar open simulation |
| v1 | momentum_26 AND reversion_12 | 10000.00 | 0.00 | 대기 /  / 새 신호 대기 |
| v1 | momentum_26 + reversion_12 | 10000.00 | 0.00 | 대기 /  / 새 신호 대기 |
| v1 | momentum_26 AND volume_26 | 10000.00 | 0.00 | 대기 /  / 새 신호 대기 |
| v1 | momentum_26 + volume_26 | 10000.00 | 0.00 | 대기 /  / 새 신호 대기 |
| v1 | breakout_8 AND reversion_12 | 10000.00 | 0.00 | 대기 /  / 새 신호 대기 |
| v1 | breakout_8 + reversion_12 | 9941.79 | -58.21 | sell /  / breakout_8 + reversion_12: prior completed bar target 0%; next bar open simulation |
| v1 | breakout_8 AND volume_26 | 10000.00 | 0.00 | 대기 /  / 새 신호 대기 |
| v1 | breakout_8 + volume_26 | 9941.79 | -58.21 | sell /  / breakout_8 + volume_26: prior completed bar target 0%; next bar open simulation |
| v1 | reversion_12 AND volume_26 | 10000.00 | 0.00 | 대기 /  / 새 신호 대기 |
| v1 | reversion_12 + volume_26 | 10000.00 | 0.00 | 대기 /  / 새 신호 대기 |
| v1 | ema_12_26 | 9979.06 | -20.94 | buy /  / EMA12 > EMA26; 조건 충족; EMA12=255.218, EMA26=255.146 |
| v1 | macd_12_26_9 | 9979.06 | -20.94 | buy /  / MACD > 신호선 그리고 MACD > 0; 조건 충족; MACD=0.0719144, signal9=-0.171173 |
| v1 | rsi_14_recovery | 10000.00 | 0.00 | 대기 /  / 새 신호 대기 |
| v1 | bollinger_20_reentry | 10000.00 | 0.00 | 대기 /  / 새 신호 대기 |
| v1 | donchian_20 | 10000.00 | 0.00 | 대기 /  / 새 신호 대기 |
| v1 | atr_14_breakout | 9883.97 | -116.03 | sell /  / 종가 > 직전 종가 + 직전 ATR14 그리고 종가 > EMA26; 조건 미충족; close=256.72, threshold=258.136, prior_ATR14=1.3158, EMA26=255.146 |
| v1 | session_vwap | 9902.81 | -97.19 | buy /  / 종가 > 뉴욕 거래일별 누적 전형가격 VWAP; 조건 충족; close=256.82, session_VWAP=255.918, session_volume=1.26831e+06 |
| v1 | obv_20 | 10000.00 | 0.00 | 대기 /  / 새 신호 대기 |
| v1 | stochastic_14_3_recovery | 9927.65 | -72.35 | sell /  / 직전 %K14 < 20에서 %K14가 %D3 상향 돌파 (한 봉 목표); 조건 미충족; K14=60.1505, D3=50.3645, previous_K14=74.7605, previous_D3=37.7141 |
| v1 | mfi_14_recovery | 10000.00 | 0.00 | 대기 /  / 새 신호 대기 |
| v1 | adx_14_trend | 9887.44 | -112.56 | sell /  / Wilder ADX14 >= 25 그리고 +DI14 > -DI14; 조건 미충족; ADX14=24.931, plus_DI14=25.9947, minus_DI14=16.1195 |
| v1 | aroon_25_trend | 10000.00 | 0.00 | 대기 /  / 새 신호 대기 |
| v1 | cci_20_momentum | 10000.00 | 0.00 | 대기 /  / 새 신호 대기 |
| v1 | williams_14_recovery | 9927.65 | -72.35 | sell /  / 직전 Williams %R14 < -80, 현재 >= -80 (한 봉 목표); 조건 미충족; Williams_R14=-39.8495, previous_R14=-25.2395 |
| v1 | cmf_20_accumulation | 10000.00 | 0.00 | 대기 /  / 새 신호 대기 |
| v1 | chaikin_3_10 | 10000.00 | 0.00 | 대기 /  / 새 신호 대기 |
| v1 | roc_10_momentum | 9974.98 | -25.02 | buy /  / 10봉 ROC > 1% 그리고 종가 > EMA26; 조건 충족; ROC10_percent=1.26173, close=256.82, EMA26=255.02 |
| v1 | trix_15_trend | 10000.00 | 0.00 | 대기 /  / 새 신호 대기 |
| v1 | keltner_20_breakout | 10000.00 | 0.00 | 대기 /  / 새 신호 대기 |
| v1 | opening_range_30m | 10000.00 | 0.00 | 대기 /  / 새 신호 대기 |
| v2 | cash | 10000.00 | 0.00 | 대기 /  / 새 신호 대기 |
| v2 | buy_hold | 9791.74 | -208.26 | 중단: 손실 한도 / buy / partial / 직전 완료 봉 목표 비중 100%; 다음 봉 시가 가정 |
| v2 | trend_8_26 | 9791.74 | -208.26 | 중단: 손실 한도 / buy / partial / 직전 완료 봉 목표 비중 100%; 다음 봉 시가 가정 |
| v2 | momentum_26 | 9791.74 | -208.26 | 중단: 손실 한도 / buy / partial / 직전 완료 봉 목표 비중 100%; 다음 봉 시가 가정 |
| v2 | breakout_8 | 9343.39 | -656.61 | 중단: 손실 한도 / sell / filled / 직전 완료 봉 목표 비중 0%; 다음 봉 시가 가정 |
| v2 | reversion_12 | 9690.14 | -309.86 | sell / filled / 직전 완료 봉 목표 비중 0%; 다음 봉 시가 가정 |
| v2 | volume_26 | 9791.36 | -208.64 | sell / filled / 직전 완료 봉 목표 비중 0%; 다음 봉 시가 가정 |
| v2 | trend_8_26 AND momentum_26 | 9791.74 | -208.26 | 중단: 손실 한도 / buy / partial / 직전 완료 봉 목표 비중 100%; 다음 봉 시가 가정 |
| v2 | trend_8_26 + momentum_26 | 9791.74 | -208.26 | 중단: 손실 한도 / buy / partial / 직전 완료 봉 목표 비중 100%; 다음 봉 시가 가정 |
| v2 | trend_8_26 AND breakout_8 | 9419.39 | -580.61 | 중단: 손실 한도 / sell / filled / 직전 완료 봉 목표 비중 0%; 다음 봉 시가 가정 |
| v2 | trend_8_26 + breakout_8 | 9502.03 | -497.97 | buy / filled / 직전 완료 봉 목표 비중 50%; 다음 봉 시가 가정 |
| v2 | trend_8_26 AND reversion_12 | 9978.08 | -21.92 | sell / filled / 직전 완료 봉 목표 비중 0%; 다음 봉 시가 가정 |
| v2 | trend_8_26 + reversion_12 | 9732.92 | -267.08 | 중단: 손실 한도 / sell / filled / 직전 완료 봉 목표 비중 0%; 다음 봉 시가 가정 |
| v2 | trend_8_26 AND volume_26 | 9870.71 | -129.29 | sell / filled / 직전 완료 봉 목표 비중 0%; 다음 봉 시가 가정 |
| v2 | trend_8_26 + volume_26 | 9869.73 | -130.27 | 중단: 손실 한도 / buy / filled / 직전 완료 봉 목표 비중 50%; 다음 봉 시가 가정 |
| v2 | momentum_26 AND breakout_8 | 9598.70 | -401.30 | sell / filled / 직전 완료 봉 목표 비중 0%; 다음 봉 시가 가정 |
| v2 | momentum_26 + breakout_8 | 9503.27 | -496.73 | sell / filled / 직전 완료 봉 목표 비중 0%; 다음 봉 시가 가정 |
| v2 | momentum_26 AND reversion_12 | 9938.87 | -61.13 | sell / filled / 직전 완료 봉 목표 비중 0%; 다음 봉 시가 가정 |
| v2 | momentum_26 + reversion_12 | 9732.92 | -267.08 | 중단: 손실 한도 / sell / filled / 직전 완료 봉 목표 비중 0%; 다음 봉 시가 가정 |
| v2 | momentum_26 AND volume_26 | 9920.93 | -79.07 | sell / filled / 직전 완료 봉 목표 비중 0%; 다음 봉 시가 가정 |
| v2 | momentum_26 + volume_26 | 9869.73 | -130.27 | 중단: 손실 한도 / buy / filled / 직전 완료 봉 목표 비중 50%; 다음 봉 시가 가정 |
| v2 | breakout_8 AND reversion_12 | 10000.00 | 0.00 | 대기 /  / 새 신호 대기 |
| v2 | breakout_8 + reversion_12 | 9523.40 | -476.60 | sell / filled / 직전 완료 봉 목표 비중 0%; 다음 봉 시가 가정 |
| v2 | breakout_8 AND volume_26 | 9814.17 | -185.83 | sell / filled / 직전 완료 봉 목표 비중 0%; 다음 봉 시가 가정 |
| v2 | breakout_8 + volume_26 | 9552.83 | -447.17 | sell / filled / 직전 완료 봉 목표 비중 0%; 다음 봉 시가 가정 |
| v2 | reversion_12 AND volume_26 | 9886.24 | -113.76 | sell / filled / 직전 완료 봉 목표 비중 0%; 다음 봉 시가 가정 |
| v2 | reversion_12 + volume_26 | 9761.35 | -238.65 | sell / filled / 직전 완료 봉 목표 비중 0%; 다음 봉 시가 가정 |
| v2 | ema_12_26 | 9978.06 | -21.94 | buy / partial / EMA12 > EMA26; 조건 충족; EMA12=255.218, EMA26=255.146; 직전 완료 봉 목표를 다음 봉 시가에 모의 적용 |
| v2 | macd_12_26_9 | 9978.06 | -21.94 | buy / partial / MACD > 신호선 그리고 MACD > 0; 조건 충족; MACD=0.0719144, signal9=-0.171173; 직전 완료 봉 목표를 다음 봉 시가에 모의 적용 |
| v2 | rsi_14_recovery | 10000.00 | 0.00 | 대기 /  / 새 신호 대기 |
| v2 | bollinger_20_reentry | 10000.00 | 0.00 | 대기 /  / 새 신호 대기 |
| v2 | donchian_20 | 10000.00 | 0.00 | 대기 /  / 새 신호 대기 |
| v2 | atr_14_breakout | 9880.02 | -119.98 | sell / filled / 종가 > 직전 종가 + 직전 ATR14 그리고 종가 > EMA26; 조건 미충족; close=256.72, threshold=258.136, prior_ATR14=1.3158, EMA26=255.146; 직전 완료 봉 목표를 다음 봉 시가에 모의 적용 |
| v2 | session_vwap | 9899.84 | -100.16 | buy / partial / 종가 > 뉴욕 거래일별 누적 전형가격 VWAP; 조건 충족; close=256.82, session_VWAP=255.918, session_volume=1.26831e+06; 직전 완료 봉 목표를 다음 봉 시가에 모의 적용 |
| v2 | obv_20 | 10000.00 | 0.00 | 대기 /  / 새 신호 대기 |
| v2 | stochastic_14_3_recovery | 9925.66 | -74.34 | sell / filled / 직전 %K14 < 20에서 %K14가 %D3 상향 돌파 (한 봉 목표); 조건 미충족; K14=60.1505, D3=50.3645, previous_K14=74.7605, previous_D3=37.7141; 직전 완료 봉 목표를 다음 봉 시가에 모의 적용 |
| v2 | mfi_14_recovery | 10000.00 | 0.00 | 대기 /  / 새 신호 대기 |
| v2 | adx_14_trend | 9883.48 | -116.52 | sell / filled / Wilder ADX14 >= 25 그리고 +DI14 > -DI14; 조건 미충족; ADX14=24.931, plus_DI14=25.9947, minus_DI14=16.1195; 직전 완료 봉 목표를 다음 봉 시가에 모의 적용 |
| v2 | aroon_25_trend | 10000.00 | 0.00 | 대기 /  / 새 신호 대기 |
| v2 | cci_20_momentum | 10000.00 | 0.00 | 대기 /  / 새 신호 대기 |
| v2 | williams_14_recovery | 9925.66 | -74.34 | sell / filled / 직전 Williams %R14 < -80, 현재 >= -80 (한 봉 목표); 조건 미충족; Williams_R14=-39.8495, previous_R14=-25.2395; 직전 완료 봉 목표를 다음 봉 시가에 모의 적용 |
| v2 | cmf_20_accumulation | 10000.00 | 0.00 | 대기 /  / 새 신호 대기 |
| v2 | chaikin_3_10 | 10000.00 | 0.00 | 대기 /  / 새 신호 대기 |
| v2 | roc_10_momentum | 9973.98 | -26.02 | buy / partial / 10봉 ROC > 1% 그리고 종가 > EMA26; 조건 충족; ROC10_percent=1.26173, close=256.82, EMA26=255.02; 직전 완료 봉 목표를 다음 봉 시가에 모의 적용 |
| v2 | trix_15_trend | 10000.00 | 0.00 | 대기 /  / 새 신호 대기 |
| v2 | keltner_20_breakout | 10000.00 | 0.00 | 대기 /  / 새 신호 대기 |
| v2 | opening_range_30m | 10000.00 | 0.00 | 대기 /  / 새 신호 대기 |

### 같은 기간의 비용·노출 비교 (사후 연구)

| 전략 | 비용 전 | 비용 후 | 100% 보유 | 같은 평균 노출 보유 | 평균 노출 |
|---|---:|---:|---:|---:|---:|
| cash | 0.00% | 0.00% | -5.49% | -0.00% | 0.00% |
| buy_hold | -5.09% | -5.49% | -5.49% | -5.49% | 100.00% |
| trend_8_26 | 2.49% | -0.06% | -5.49% | -2.70% | 48.02% |
| momentum_26 | 0.96% | -2.38% | -5.49% | -2.68% | 47.76% |
| breakout_8 | -0.63% | -17.75% | -5.49% | -1.23% | 21.64% |
| reversion_12 | -7.78% | -15.92% | -5.49% | -1.69% | 29.82% |
| volume_26 | -0.65% | -7.11% | -5.49% | -0.38% | 6.60% |
| trend_8_26 AND momentum_26 | 2.35% | -0.62% | -5.49% | -2.47% | 43.80% |
| trend_8_26 + momentum_26 | 1.73% | -1.22% | -5.49% | -2.69% | 47.89% |
| trend_8_26 AND breakout_8 | 0.78% | -11.52% | -5.49% | -0.87% | 15.30% |
| trend_8_26 + breakout_8 | 0.94% | -9.12% | -5.49% | -1.97% | 34.84% |
| trend_8_26 AND reversion_12 | 0.69% | -2.63% | -5.49% | -0.32% | 5.54% |
| trend_8_26 + reversion_12 | -2.75% | -7.94% | -5.49% | -2.20% | 38.92% |
| trend_8_26 AND volume_26 | 1.59% | -0.53% | -5.49% | -0.09% | 1.58% |
| trend_8_26 + volume_26 | 0.94% | -3.23% | -5.49% | -1.55% | 27.31% |
| momentum_26 AND breakout_8 | 2.20% | -9.52% | -5.49% | -0.83% | 14.51% |
| momentum_26 + breakout_8 | 0.19% | -10.18% | -5.49% | -1.96% | 34.70% |
| momentum_26 AND reversion_12 | -0.60% | -3.89% | -5.49% | -0.39% | 6.86% |
| momentum_26 + reversion_12 | -3.48% | -8.82% | -5.49% | -2.19% | 38.79% |
| momentum_26 AND volume_26 | 1.57% | -0.12% | -5.49% | -0.08% | 1.32% |
| momentum_26 + volume_26 | 0.18% | -4.16% | -5.49% | -1.54% | 27.18% |
| breakout_8 AND reversion_12 | 0.00% | 0.00% | -5.49% | -0.00% | 0.00% |
| breakout_8 + reversion_12 | -4.26% | -16.32% | -5.49% | -1.46% | 25.73% |
| breakout_8 AND volume_26 | -0.11% | -2.19% | -5.49% | -0.09% | 1.58% |
| breakout_8 + volume_26 | -0.63% | -11.85% | -5.49% | -0.81% | 14.12% |
| reversion_12 AND volume_26 | -1.99% | -4.42% | -5.49% | -0.15% | 2.64% |
| reversion_12 + volume_26 | -4.27% | -10.88% | -5.49% | -1.04% | 18.21% |
| ema_12_26 | 0.00% | -2.07% | -5.49% | -2.47% | 43.80% |
| macd_12_26_9 | 6.36% | 3.72% | -5.49% | -1.62% | 28.50% |
| rsi_14_recovery | -1.69% | -6.92% | -5.49% | -0.20% | 3.43% |
| bollinger_20_reentry | -0.55% | -4.64% | -5.49% | -0.15% | 2.64% |
| donchian_20 | 1.17% | -6.59% | -5.49% | -0.42% | 7.39% |
| atr_14_breakout | 1.31% | -4.88% | -5.49% | -0.27% | 4.75% |
| session_vwap | 2.04% | -5.39% | -5.49% | -2.80% | 49.87% |
| obv_20 | -5.39% | -13.02% | -5.49% | -1.94% | 34.30% |
| stochastic_14_3_recovery | -1.40% | -13.80% | -5.49% | -0.48% | 8.44% |
| mfi_14_recovery | 0.33% | -0.93% | -5.49% | -0.05% | 0.79% |
| adx_14_trend | -2.32% | -6.73% | -5.49% | -1.76% | 31.13% |
| aroon_25_trend | 3.86% | -0.41% | -5.49% | -1.60% | 28.23% |
| cci_20_momentum | 1.10% | -5.87% | -5.49% | -1.39% | 24.54% |
| williams_14_recovery | -2.03% | -10.30% | -5.49% | -0.32% | 5.54% |
| cmf_20_accumulation | 2.16% | -2.04% | -5.49% | -1.73% | 30.61% |
| chaikin_3_10 | -3.37% | -7.73% | -5.49% | -2.06% | 36.41% |
| roc_10_momentum | -1.23% | -7.26% | -5.49% | -0.81% | 14.25% |
| trix_15_trend | -0.90% | -3.36% | -5.49% | -1.90% | 33.51% |
| keltner_20_breakout | 0.76% | -2.97% | -5.49% | -0.54% | 9.50% |
| opening_range_30m | 0.41% | -3.72% | -5.49% | -1.50% | 26.39% |

동일 구간·초기 자금, 종료 시 청산 비용 포함. 노출 맞춤은 사후 설명용이며 v2 실제 계좌 성과가 아닙니다.
[낙폭 분해·비용 영향·전체 구간](JNJ/comparison.json)

[v1 전체 기록](JNJ/accounts.json) · [v2 전체 기록](JNJ/accounts-v2.json)

## CAT 계좌

| 모델 | 전략 | 평가액 USD | 손익 USD | 최근 매매·이유 |
|---|---|---:|---:|---|
| v1 | cash | 10000.00 | 0.00 | 대기 /  / 새 신호 대기 |
| v1 | buy_hold | 9982.34 | -17.66 | buy /  / buy_hold: prior completed bar target 100%; next bar open simulation |
| v1 | trend_8_26 | 9982.34 | -17.66 | buy /  / trend_8_26: prior completed bar target 100%; next bar open simulation |
| v1 | momentum_26 | 9902.18 | -97.82 | buy /  / momentum_26: prior completed bar target 100%; next bar open simulation |
| v1 | breakout_8 | 9950.83 | -49.17 | sell /  / breakout_8: prior completed bar target 0%; next bar open simulation |
| v1 | reversion_12 | 10000.00 | 0.00 | 대기 /  / 새 신호 대기 |
| v1 | volume_26 | 10000.00 | 0.00 | 대기 /  / 새 신호 대기 |
| v1 | trend_8_26 AND momentum_26 | 9902.18 | -97.82 | buy /  / trend_8_26 AND momentum_26: prior completed bar target 100%; next bar open simulation |
| v1 | trend_8_26 + momentum_26 | 9942.34 | -57.66 | buy /  / trend_8_26 + momentum_26: prior completed bar target 100%; next bar open simulation |
| v1 | trend_8_26 AND breakout_8 | 9950.83 | -49.17 | sell /  / trend_8_26 AND breakout_8: prior completed bar target 0%; next bar open simulation |
| v1 | trend_8_26 + breakout_8 | 9966.78 | -33.22 | sell /  / trend_8_26 + breakout_8: prior completed bar target 50%; next bar open simulation |
| v1 | trend_8_26 AND reversion_12 | 10000.00 | 0.00 | 대기 /  / 새 신호 대기 |
| v1 | trend_8_26 + reversion_12 | 9991.26 | -8.74 | sell /  / trend_8_26 + reversion_12: prior completed bar target 50%; next bar open simulation |
| v1 | trend_8_26 AND volume_26 | 10000.00 | 0.00 | 대기 /  / 새 신호 대기 |
| v1 | trend_8_26 + volume_26 | 9991.26 | -8.74 | sell /  / trend_8_26 + volume_26: prior completed bar target 50%; next bar open simulation |
| v1 | momentum_26 AND breakout_8 | 9950.83 | -49.17 | sell /  / momentum_26 AND breakout_8: prior completed bar target 0%; next bar open simulation |
| v1 | momentum_26 + breakout_8 | 9926.52 | -73.48 | sell /  / momentum_26 + breakout_8: prior completed bar target 50%; next bar open simulation |
| v1 | momentum_26 AND reversion_12 | 10000.00 | 0.00 | 대기 /  / 새 신호 대기 |
| v1 | momentum_26 + reversion_12 | 9950.99 | -49.01 | sell /  / momentum_26 + reversion_12: prior completed bar target 50%; next bar open simulation |
| v1 | momentum_26 AND volume_26 | 10000.00 | 0.00 | 대기 /  / 새 신호 대기 |
| v1 | momentum_26 + volume_26 | 9950.99 | -49.01 | sell /  / momentum_26 + volume_26: prior completed bar target 50%; next bar open simulation |
| v1 | breakout_8 AND reversion_12 | 10000.00 | 0.00 | 대기 /  / 새 신호 대기 |
| v1 | breakout_8 + reversion_12 | 9975.37 | -24.63 | sell /  / breakout_8 + reversion_12: prior completed bar target 0%; next bar open simulation |
| v1 | breakout_8 AND volume_26 | 10000.00 | 0.00 | 대기 /  / 새 신호 대기 |
| v1 | breakout_8 + volume_26 | 9975.37 | -24.63 | sell /  / breakout_8 + volume_26: prior completed bar target 0%; next bar open simulation |
| v1 | reversion_12 AND volume_26 | 10000.00 | 0.00 | 대기 /  / 새 신호 대기 |
| v1 | reversion_12 + volume_26 | 10000.00 | 0.00 | 대기 /  / 새 신호 대기 |
| v1 | ema_12_26 | 9902.18 | -97.82 | buy /  / EMA12 > EMA26; 조건 충족; EMA12=733.716, EMA26=733.7 |
| v1 | macd_12_26_9 | 9902.18 | -97.82 | buy /  / MACD > 신호선 그리고 MACD > 0; 조건 충족; MACD=0.0155601, signal9=-2.12997 |
| v1 | rsi_14_recovery | 10000.00 | 0.00 | 대기 /  / 새 신호 대기 |
| v1 | bollinger_20_reentry | 10000.00 | 0.00 | 대기 /  / 새 신호 대기 |
| v1 | donchian_20 | 9950.83 | -49.17 | sell /  / 종가 > 현재 봉을 제외한 직전 20봉 최고가; 조건 미충족; close=739.81, prior_high20=742.28 |
| v1 | atr_14_breakout | 9950.83 | -49.17 | sell /  / 종가 > 직전 종가 + 직전 ATR14 그리고 종가 > EMA26; 조건 미충족; close=739.81, threshold=744.805, prior_ATR14=4.59507, EMA26=734.153 |
| v1 | session_vwap | 9982.34 | -17.66 | buy /  / 종가 > 뉴욕 거래일별 누적 전형가격 VWAP; 조건 충족; close=735.5, session_VWAP=726.49, session_volume=5.46536e+06 |
| v1 | obv_20 | 9982.34 | -17.66 | buy /  / OBV > OBV의 SMA20 그리고 종가 > EMA26; 조건 충족; OBV=-4.52114e+06, OBV_SMA20=-4.56599e+06, close=735.5, EMA26=733.18 |
| v1 | stochastic_14_3_recovery | 10000.00 | 0.00 | 대기 /  / 새 신호 대기 |
| v1 | mfi_14_recovery | 10000.00 | 0.00 | 대기 /  / 새 신호 대기 |
| v1 | adx_14_trend | 10000.00 | 0.00 | 대기 /  / 새 신호 대기 |
| v1 | aroon_25_trend | 10031.15 | 31.15 | sell /  / Aroon25 Up > 70 그리고 Down < 30 (동률이면 최신 극값); 조건 미충족; Aroon_up=88, Aroon_down=48 |
| v1 | cci_20_momentum | 10024.78 | 24.78 | sell /  / CCI20 > 100 (전형가격·평균절대편차); 조건 미충족; CCI20=98.8062 |
| v1 | williams_14_recovery | 10000.00 | 0.00 | 대기 /  / 새 신호 대기 |
| v1 | cmf_20_accumulation | 9911.38 | -88.62 | buy /  / Chaikin Money Flow20 > 0.1; 조건 충족; CMF20=0.173065, volume20=2.14066e+06 |
| v1 | chaikin_3_10 | 9902.18 | -97.82 | buy /  / ADL의 EMA3 - EMA10 > 0 그리고 종가 > EMA26; 조건 충족; Chaikin3_10=13207, ADL=-5.59769e+06, close=740.21, EMA26=733.7 |
| v1 | roc_10_momentum | 9982.34 | -17.66 | buy /  / 10봉 ROC > 1% 그리고 종가 > EMA26; 조건 충족; ROC10_percent=1.18659, close=735.5, EMA26=733.18 |
| v1 | trix_15_trend | 9911.62 | -88.38 | buy /  / 15봉 삼중 EMA의 1봉 변화율 TRIX > 0 그리고 종가 > EMA26; 조건 충족; TRIX15_percent=0.00288214, close=739.67, EMA26=735.563 |
| v1 | keltner_20_breakout | 10000.00 | 0.00 | 대기 /  / 새 신호 대기 |
| v1 | opening_range_30m | 10040.71 | 40.71 | sell /  / 뉴욕 09:30·09:45 두 완료 봉 최고가를 10:00 이후 종가가 돌파; 자료 부족·변동폭 또는 거래량 없음: 대기; close=740.21 |
| v2 | cash | 10000.00 | 0.00 | 대기 /  / 새 신호 대기 |
| v2 | buy_hold | 9180.51 | -819.49 | 중단: 손실 한도 / buy / partial / 직전 완료 봉 목표 비중 100%; 다음 봉 시가 가정 |
| v2 | trend_8_26 | 9906.20 | -93.80 | buy / partial / 직전 완료 봉 목표 비중 100%; 다음 봉 시가 가정 |
| v2 | momentum_26 | 9915.63 | -84.37 | buy / partial / 직전 완료 봉 목표 비중 100%; 다음 봉 시가 가정 |
| v2 | breakout_8 | 9772.76 | -227.24 | sell / filled / 직전 완료 봉 목표 비중 0%; 다음 봉 시가 가정 |
| v2 | reversion_12 | 9052.30 | -947.70 | 중단: 손실 한도 / buy / partial / 직전 완료 봉 목표 비중 100%; 다음 봉 시가 가정 |
| v2 | volume_26 | 9311.18 | -688.82 | 중단: 손실 한도 / buy / partial / 직전 완료 봉 목표 비중 100%; 다음 봉 시가 가정 |
| v2 | trend_8_26 AND momentum_26 | 9944.34 | -55.66 | buy / partial / 직전 완료 봉 목표 비중 100%; 다음 봉 시가 가정 |
| v2 | trend_8_26 + momentum_26 | 9911.08 | -88.92 | buy / partial / 직전 완료 봉 목표 비중 100%; 다음 봉 시가 가정 |
| v2 | trend_8_26 AND breakout_8 | 9866.70 | -133.30 | sell / filled / 직전 완료 봉 목표 비중 0%; 다음 봉 시가 가정 |
| v2 | trend_8_26 + breakout_8 | 9839.74 | -160.26 | sell / filled / 직전 완료 봉 목표 비중 50%; 다음 봉 시가 가정 |
| v2 | trend_8_26 AND reversion_12 | 9815.07 | -184.93 | sell / filled / 직전 완료 봉 목표 비중 0%; 다음 봉 시가 가정 |
| v2 | trend_8_26 + reversion_12 | 9616.31 | -383.69 | sell / filled / 직전 완료 봉 목표 비중 50%; 다음 봉 시가 가정 |
| v2 | trend_8_26 AND volume_26 | 10035.44 | 35.44 | sell / filled / 직전 완료 봉 목표 비중 0%; 다음 봉 시가 가정 |
| v2 | trend_8_26 + volume_26 | 9624.15 | -375.85 | sell / filled / 직전 완료 봉 목표 비중 50%; 다음 봉 시가 가정 |
| v2 | momentum_26 AND breakout_8 | 9926.39 | -73.61 | sell / filled / 직전 완료 봉 목표 비중 0%; 다음 봉 시가 가정 |
| v2 | momentum_26 + breakout_8 | 9844.18 | -155.82 | sell / filled / 직전 완료 봉 목표 비중 50%; 다음 봉 시가 가정 |
| v2 | momentum_26 AND reversion_12 | 9874.73 | -125.27 | sell / filled / 직전 완료 봉 목표 비중 0%; 다음 봉 시가 가정 |
| v2 | momentum_26 + reversion_12 | 9620.80 | -379.20 | sell / filled / 직전 완료 봉 목표 비중 50%; 다음 봉 시가 가정 |
| v2 | momentum_26 AND volume_26 | 10048.78 | 48.78 | sell / filled / 직전 완료 봉 목표 비중 0%; 다음 봉 시가 가정 |
| v2 | momentum_26 + volume_26 | 9648.90 | -351.10 | sell / filled / 직전 완료 봉 목표 비중 50%; 다음 봉 시가 가정 |
| v2 | breakout_8 AND reversion_12 | 10000.00 | 0.00 | 대기 /  / 새 신호 대기 |
| v2 | breakout_8 + reversion_12 | 9610.18 | -389.82 | 중단: 손실 한도 / sell / filled / 직전 완료 봉 목표 비중 0%; 다음 봉 시가 가정 |
| v2 | breakout_8 AND volume_26 | 9998.69 | -1.31 | sell / filled / 직전 완료 봉 목표 비중 0%; 다음 봉 시가 가정 |
| v2 | breakout_8 + volume_26 | 9579.25 | -420.75 | sell / filled / 직전 완료 봉 목표 비중 0%; 다음 봉 시가 가정 |
| v2 | reversion_12 AND volume_26 | 9246.77 | -753.23 | 중단: 손실 한도 / buy / partial / 직전 완료 봉 목표 비중 100%; 다음 봉 시가 가정 |
| v2 | reversion_12 + volume_26 | 9388.86 | -611.14 | 중단: 손실 한도 / sell / filled / 직전 완료 봉 목표 비중 50%; 다음 봉 시가 가정 |
| v2 | ema_12_26 | 9901.19 | -98.81 | buy / partial / EMA12 > EMA26; 조건 충족; EMA12=733.716, EMA26=733.7; 직전 완료 봉 목표를 다음 봉 시가에 모의 적용 |
| v2 | macd_12_26_9 | 9901.19 | -98.81 | buy / partial / MACD > 신호선 그리고 MACD > 0; 조건 충족; MACD=0.0155601, signal9=-2.12997; 직전 완료 봉 목표를 다음 봉 시가에 모의 적용 |
| v2 | rsi_14_recovery | 10000.00 | 0.00 | 대기 /  / 새 신호 대기 |
| v2 | bollinger_20_reentry | 10000.00 | 0.00 | 대기 /  / 새 신호 대기 |
| v2 | donchian_20 | 9948.84 | -51.16 | sell / filled / 종가 > 현재 봉을 제외한 직전 20봉 최고가; 조건 미충족; close=739.81, prior_high20=742.28; 직전 완료 봉 목표를 다음 봉 시가에 모의 적용 |
| v2 | atr_14_breakout | 9948.84 | -51.16 | sell / filled / 종가 > 직전 종가 + 직전 ATR14 그리고 종가 > EMA26; 조건 미충족; close=739.81, threshold=744.805, prior_ATR14=4.59507, EMA26=734.153; 직전 완료 봉 목표를 다음 봉 시가에 모의 적용 |
| v2 | session_vwap | 9981.34 | -18.66 | buy / partial / 종가 > 뉴욕 거래일별 누적 전형가격 VWAP; 조건 충족; close=735.5, session_VWAP=726.49, session_volume=5.46536e+06; 직전 완료 봉 목표를 다음 봉 시가에 모의 적용 |
| v2 | obv_20 | 9981.34 | -18.66 | buy / partial / OBV > OBV의 SMA20 그리고 종가 > EMA26; 조건 충족; OBV=-4.52114e+06, OBV_SMA20=-4.56599e+06, close=735.5, EMA26=733.18; 직전 완료 봉 목표를 다음 봉 시가에 모의 적용 |
| v2 | stochastic_14_3_recovery | 10000.00 | 0.00 | 대기 /  / 새 신호 대기 |
| v2 | mfi_14_recovery | 10000.00 | 0.00 | 대기 /  / 새 신호 대기 |
| v2 | adx_14_trend | 10000.00 | 0.00 | 대기 /  / 새 신호 대기 |
| v2 | aroon_25_trend | 10029.14 | 29.14 | sell / filled / Aroon25 Up > 70 그리고 Down < 30 (동률이면 최신 극값); 조건 미충족; Aroon_up=88, Aroon_down=48; 직전 완료 봉 목표를 다음 봉 시가에 모의 적용 |
| v2 | cci_20_momentum | 10022.77 | 22.77 | sell / filled / CCI20 > 100 (전형가격·평균절대편차); 조건 미충족; CCI20=98.8062; 직전 완료 봉 목표를 다음 봉 시가에 모의 적용 |
| v2 | williams_14_recovery | 10000.00 | 0.00 | 대기 /  / 새 신호 대기 |
| v2 | cmf_20_accumulation | 9910.39 | -89.61 | buy / partial / Chaikin Money Flow20 > 0.1; 조건 충족; CMF20=0.173065, volume20=2.14066e+06; 직전 완료 봉 목표를 다음 봉 시가에 모의 적용 |
| v2 | chaikin_3_10 | 9901.19 | -98.81 | buy / partial / ADL의 EMA3 - EMA10 > 0 그리고 종가 > EMA26; 조건 충족; Chaikin3_10=13207, ADL=-5.59769e+06, close=740.21, EMA26=733.7; 직전 완료 봉 목표를 다음 봉 시가에 모의 적용 |
| v2 | roc_10_momentum | 9981.34 | -18.66 | buy / partial / 10봉 ROC > 1% 그리고 종가 > EMA26; 조건 충족; ROC10_percent=1.18659, close=735.5, EMA26=733.18; 직전 완료 봉 목표를 다음 봉 시가에 모의 적용 |
| v2 | trix_15_trend | 9910.63 | -89.37 | buy / partial / 15봉 삼중 EMA의 1봉 변화율 TRIX > 0 그리고 종가 > EMA26; 조건 충족; TRIX15_percent=0.00288214, close=739.67, EMA26=735.563; 직전 완료 봉 목표를 다음 봉 시가에 모의 적용 |
| v2 | keltner_20_breakout | 10000.00 | 0.00 | 대기 /  / 새 신호 대기 |
| v2 | opening_range_30m | 10038.70 | 38.70 | sell / filled / 뉴욕 09:30·09:45 두 완료 봉 최고가를 10:00 이후 종가가 돌파; 자료 부족·변동폭 또는 거래량 없음: 대기; close=740.21; 직전 완료 봉 목표를 다음 봉 시가에 모의 적용 |

### 같은 기간의 비용·노출 비교 (사후 연구)

| 전략 | 비용 전 | 비용 후 | 100% 보유 | 같은 평균 노출 보유 | 평균 노출 |
|---|---:|---:|---:|---:|---:|
| cash | 0.00% | 0.00% | -10.40% | -0.00% | 0.00% |
| buy_hold | -10.02% | -10.40% | -10.40% | -10.40% | 100.00% |
| trend_8_26 | -1.49% | -5.15% | -10.40% | -5.25% | 50.13% |
| momentum_26 | -4.38% | -10.22% | -10.40% | -5.09% | 48.55% |
| breakout_8 | -3.26% | -16.13% | -10.40% | -1.61% | 15.30% |
| reversion_12 | -3.89% | -15.27% | -10.40% | -2.72% | 25.86% |
| volume_26 | -2.95% | -10.02% | -10.40% | -0.86% | 8.18% |
| trend_8_26 AND momentum_26 | -1.69% | -6.52% | -10.40% | -4.48% | 42.74% |
| trend_8_26 + momentum_26 | -2.93% | -7.70% | -10.40% | -5.17% | 49.34% |
| trend_8_26 AND breakout_8 | -1.89% | -9.42% | -10.40% | -0.83% | 7.92% |
| trend_8_26 + breakout_8 | -2.34% | -10.60% | -10.40% | -3.44% | 32.72% |
| trend_8_26 AND reversion_12 | 0.78% | -5.38% | -10.40% | -0.75% | 7.12% |
| trend_8_26 + reversion_12 | -2.64% | -9.76% | -10.40% | -3.99% | 38.00% |
| trend_8_26 AND volume_26 | 2.22% | -0.75% | -10.40% | -0.28% | 2.64% |
| trend_8_26 + volume_26 | -2.17% | -7.39% | -10.40% | -3.06% | 29.16% |
| momentum_26 AND breakout_8 | -2.81% | -11.02% | -10.40% | -0.92% | 8.71% |
| momentum_26 + breakout_8 | -3.78% | -13.20% | -10.40% | -3.35% | 31.93% |
| momentum_26 AND reversion_12 | -3.04% | -8.96% | -10.40% | -0.61% | 5.80% |
| momentum_26 + reversion_12 | -4.08% | -11.84% | -10.40% | -3.90% | 37.21% |
| momentum_26 AND volume_26 | 1.58% | -0.53% | -10.40% | -0.17% | 1.58% |
| momentum_26 + volume_26 | -3.61% | -9.33% | -10.40% | -2.98% | 28.37% |
| breakout_8 AND reversion_12 | 0.00% | 0.00% | -10.40% | -0.00% | 0.00% |
| breakout_8 + reversion_12 | -3.53% | -14.80% | -10.40% | -2.17% | 20.59% |
| breakout_8 AND volume_26 | 0.37% | -0.47% | -10.40% | -0.06% | 0.53% |
| breakout_8 + volume_26 | -3.07% | -12.38% | -10.40% | -1.24% | 11.75% |
| reversion_12 AND volume_26 | -1.25% | -5.71% | -10.40% | -0.56% | 5.28% |
| reversion_12 + volume_26 | -3.39% | -11.93% | -10.40% | -1.79% | 17.02% |
| ema_12_26 | -0.93% | -2.99% | -10.40% | -5.22% | 49.87% |
| macd_12_26_9 | -0.99% | -5.06% | -10.40% | -3.10% | 29.55% |
| rsi_14_recovery | -0.96% | -6.22% | -10.40% | -0.36% | 3.43% |
| bollinger_20_reentry | 1.35% | -4.43% | -10.40% | -0.39% | 3.69% |
| donchian_20 | -2.30% | -7.11% | -10.40% | -0.56% | 5.28% |
| atr_14_breakout | -2.42% | -9.14% | -10.40% | -0.50% | 4.75% |
| session_vwap | -0.16% | -11.98% | -10.40% | -4.89% | 46.70% |
| obv_20 | -3.81% | -14.12% | -10.40% | -2.91% | 27.70% |
| stochastic_14_3_recovery | -3.21% | -13.22% | -10.40% | -0.72% | 6.86% |
| mfi_14_recovery | 0.45% | -1.63% | -10.40% | -0.14% | 1.32% |
| adx_14_trend | -3.13% | -5.93% | -10.40% | -1.00% | 9.50% |
| aroon_25_trend | -1.87% | -6.31% | -10.40% | -1.58% | 15.04% |
| cci_20_momentum | -5.69% | -11.82% | -10.40% | -1.72% | 16.36% |
| williams_14_recovery | -1.60% | -10.66% | -10.40% | -0.64% | 6.07% |
| cmf_20_accumulation | -5.74% | -12.60% | -10.40% | -1.89% | 17.94% |
| chaikin_3_10 | -5.58% | -13.92% | -10.40% | -3.77% | 35.88% |
| roc_10_momentum | -1.82% | -7.82% | -10.40% | -1.42% | 13.46% |
| trix_15_trend | -0.60% | -4.69% | -10.40% | -4.18% | 39.84% |
| keltner_20_breakout | -3.35% | -6.15% | -10.40% | -0.31% | 2.90% |
| opening_range_30m | 4.95% | -0.21% | -10.40% | -2.16% | 20.58% |

동일 구간·초기 자금, 종료 시 청산 비용 포함. 노출 맞춤은 사후 설명용이며 v2 실제 계좌 성과가 아닙니다.
[낙폭 분해·비용 영향·전체 구간](CAT/comparison.json)

[v1 전체 기록](CAT/accounts.json) · [v2 전체 기록](CAT/accounts-v2.json)

## WMT 계좌

| 모델 | 전략 | 평가액 USD | 손익 USD | 최근 매매·이유 |
|---|---|---:|---:|---|
| v1 | cash | 10000.00 | 0.00 | 대기 /  / 새 신호 대기 |
| v1 | buy_hold | 10050.57 | 50.57 | buy /  / buy_hold: prior completed bar target 100%; next bar open simulation |
| v1 | trend_8_26 | 9996.83 | -3.17 | buy /  / trend_8_26: prior completed bar target 100%; next bar open simulation |
| v1 | momentum_26 | 10043.97 | 43.97 | sell /  / momentum_26: prior completed bar target 0%; next bar open simulation |
| v1 | breakout_8 | 9953.51 | -46.49 | sell /  / breakout_8: prior completed bar target 0%; next bar open simulation |
| v1 | reversion_12 | 10043.97 | 43.97 | sell /  / reversion_12: prior completed bar target 0%; next bar open simulation |
| v1 | volume_26 | 9979.72 | -20.28 | sell /  / volume_26: prior completed bar target 0%; next bar open simulation |
| v1 | trend_8_26 AND momentum_26 | 10000.00 | 0.00 | 대기 /  / 새 신호 대기 |
| v1 | trend_8_26 + momentum_26 | 10020.44 | 20.44 | buy /  / trend_8_26 + momentum_26: prior completed bar target 50%; next bar open simulation |
| v1 | trend_8_26 AND breakout_8 | 10000.00 | 0.00 | 대기 /  / 새 신호 대기 |
| v1 | trend_8_26 + breakout_8 | 9975.15 | -24.85 | buy /  / trend_8_26 + breakout_8: prior completed bar target 50%; next bar open simulation |
| v1 | trend_8_26 AND reversion_12 | 10000.00 | 0.00 | 대기 /  / 새 신호 대기 |
| v1 | trend_8_26 + reversion_12 | 10020.44 | 20.44 | buy /  / trend_8_26 + reversion_12: prior completed bar target 50%; next bar open simulation |
| v1 | trend_8_26 AND volume_26 | 10000.00 | 0.00 | 대기 /  / 새 신호 대기 |
| v1 | trend_8_26 + volume_26 | 9988.25 | -11.75 | buy /  / trend_8_26 + volume_26: prior completed bar target 50%; next bar open simulation |
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
| v1 | ema_12_26 | 10050.57 | 50.57 | buy /  / EMA12 > EMA26; 조건 충족; EMA12=118.245, EMA26=118.045 |
| v1 | macd_12_26_9 | 10000.00 | 0.00 | 대기 /  / 새 신호 대기 |
| v1 | rsi_14_recovery | 10000.00 | 0.00 | 대기 /  / 새 신호 대기 |
| v1 | bollinger_20_reentry | 10000.00 | 0.00 | 대기 /  / 새 신호 대기 |
| v1 | donchian_20 | 10000.00 | 0.00 | 대기 /  / 새 신호 대기 |
| v1 | atr_14_breakout | 9979.72 | -20.28 | sell /  / 종가 > 직전 종가 + 직전 ATR14 그리고 종가 > EMA26; 조건 미충족; close=119.375, threshold=119.607, prior_ATR14=0.486823, EMA26=118.217 |
| v1 | session_vwap | 9899.04 | -100.96 | sell /  / 종가 > 뉴욕 거래일별 누적 전형가격 VWAP; 조건 미충족; close=118.42, session_VWAP=118.955, session_volume=5.04706e+06 |
| v1 | obv_20 | 10000.00 | 0.00 | 대기 /  / 새 신호 대기 |
| v1 | stochastic_14_3_recovery | 9979.72 | -20.28 | sell /  / 직전 %K14 < 20에서 %K14가 %D3 상향 돌파 (한 봉 목표); 조건 미충족; K14=93.8952, D3=60.8222, previous_K14=82.4242, previous_D3=34.5012 |
| v1 | mfi_14_recovery | 10000.00 | 0.00 | 대기 /  / 새 신호 대기 |
| v1 | adx_14_trend | 10050.57 | 50.57 | buy /  / Wilder ADX14 >= 25 그리고 +DI14 > -DI14; 조건 충족; ADX14=29.9186, plus_DI14=22.635, minus_DI14=22.4078 |
| v1 | aroon_25_trend | 10000.00 | 0.00 | 대기 /  / 새 신호 대기 |
| v1 | cci_20_momentum | 9932.96 | -67.04 | sell /  / CCI20 > 100 (전형가격·평균절대편차); 조건 미충족; CCI20=99.1325 |
| v1 | williams_14_recovery | 9979.72 | -20.28 | sell /  / 직전 Williams %R14 < -80, 현재 >= -80 (한 봉 목표); 조건 미충족; Williams_R14=-6.10484, previous_R14=-17.5758 |
| v1 | cmf_20_accumulation | 10000.00 | 0.00 | 대기 /  / 새 신호 대기 |
| v1 | chaikin_3_10 | 9876.44 | -123.56 | buy /  / ADL의 EMA3 - EMA10 > 0 그리고 종가 > EMA26; 조건 충족; Chaikin3_10=175820, ADL=1.95122e+07, close=118.735, EMA26=118.371 |
| v1 | roc_10_momentum | 10000.00 | 0.00 | 대기 /  / 새 신호 대기 |
| v1 | trix_15_trend | 9966.62 | -33.38 | buy /  / 15봉 삼중 EMA의 1봉 변화율 TRIX > 0 그리고 종가 > EMA26; 조건 충족; TRIX15_percent=0.0496307, close=119.12, EMA26=118.125 |
| v1 | keltner_20_breakout | 10000.00 | 0.00 | 대기 /  / 새 신호 대기 |
| v1 | opening_range_30m | 10000.00 | 0.00 | 대기 /  / 새 신호 대기 |
| v2 | cash | 10000.00 | 0.00 | 대기 /  / 새 신호 대기 |
| v2 | buy_hold | 10648.48 | 648.48 | buy / partial / 직전 완료 봉 목표 비중 100%; 다음 봉 시가 가정 |
| v2 | trend_8_26 | 10406.29 | 406.29 | buy / partial / 직전 완료 봉 목표 비중 100%; 다음 봉 시가 가정 |
| v2 | momentum_26 | 10465.54 | 465.54 | sell / filled / 직전 완료 봉 목표 비중 0%; 다음 봉 시가 가정 |
| v2 | breakout_8 | 9916.34 | -83.66 | sell / filled / 직전 완료 봉 목표 비중 0%; 다음 봉 시가 가정 |
| v2 | reversion_12 | 9953.01 | -46.99 | sell / filled / 직전 완료 봉 목표 비중 0%; 다음 봉 시가 가정 |
| v2 | volume_26 | 9943.08 | -56.92 | sell / filled / 직전 완료 봉 목표 비중 0%; 다음 봉 시가 가정 |
| v2 | trend_8_26 AND momentum_26 | 10410.62 | 410.62 | sell / filled / 직전 완료 봉 목표 비중 0%; 다음 봉 시가 가정 |
| v2 | trend_8_26 + momentum_26 | 10435.89 | 435.89 | buy / filled / 직전 완료 봉 목표 비중 50%; 다음 봉 시가 가정 |
| v2 | trend_8_26 AND breakout_8 | 10088.55 | 88.55 | sell / filled / 직전 완료 봉 목표 비중 0%; 다음 봉 시가 가정 |
| v2 | trend_8_26 + breakout_8 | 10158.78 | 158.78 | buy / filled / 직전 완료 봉 목표 비중 50%; 다음 봉 시가 가정 |
| v2 | trend_8_26 AND reversion_12 | 9808.74 | -191.26 | sell / filled / 직전 완료 봉 목표 비중 0%; 다음 봉 시가 가정 |
| v2 | trend_8_26 + reversion_12 | 10178.64 | 178.64 | buy / filled / 직전 완료 봉 목표 비중 50%; 다음 봉 시가 가정 |
| v2 | trend_8_26 AND volume_26 | 9949.23 | -50.77 | sell / filled / 직전 완료 봉 목표 비중 0%; 다음 봉 시가 가정 |
| v2 | trend_8_26 + volume_26 | 10173.49 | 173.49 | buy / filled / 직전 완료 봉 목표 비중 50%; 다음 봉 시가 가정 |
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
| v2 | ema_12_26 | 10049.56 | 49.56 | buy / partial / EMA12 > EMA26; 조건 충족; EMA12=118.245, EMA26=118.045; 직전 완료 봉 목표를 다음 봉 시가에 모의 적용 |
| v2 | macd_12_26_9 | 10000.00 | 0.00 | 대기 /  / 새 신호 대기 |
| v2 | rsi_14_recovery | 10000.00 | 0.00 | 대기 /  / 새 신호 대기 |
| v2 | bollinger_20_reentry | 10000.00 | 0.00 | 대기 /  / 새 신호 대기 |
| v2 | donchian_20 | 10000.00 | 0.00 | 대기 /  / 새 신호 대기 |
| v2 | atr_14_breakout | 9977.72 | -22.28 | sell / filled / 종가 > 직전 종가 + 직전 ATR14 그리고 종가 > EMA26; 조건 미충족; close=119.375, threshold=119.607, prior_ATR14=0.486823, EMA26=118.217; 직전 완료 봉 목표를 다음 봉 시가에 모의 적용 |
| v2 | session_vwap | 9897.06 | -102.94 | sell / filled / 종가 > 뉴욕 거래일별 누적 전형가격 VWAP; 조건 미충족; close=118.42, session_VWAP=118.955, session_volume=5.04706e+06; 직전 완료 봉 목표를 다음 봉 시가에 모의 적용 |
| v2 | obv_20 | 10000.00 | 0.00 | 대기 /  / 새 신호 대기 |
| v2 | stochastic_14_3_recovery | 9977.72 | -22.28 | sell / filled / 직전 %K14 < 20에서 %K14가 %D3 상향 돌파 (한 봉 목표); 조건 미충족; K14=93.8952, D3=60.8222, previous_K14=82.4242, previous_D3=34.5012; 직전 완료 봉 목표를 다음 봉 시가에 모의 적용 |
| v2 | mfi_14_recovery | 10000.00 | 0.00 | 대기 /  / 새 신호 대기 |
| v2 | adx_14_trend | 10049.56 | 49.56 | buy / partial / Wilder ADX14 >= 25 그리고 +DI14 > -DI14; 조건 충족; ADX14=29.9186, plus_DI14=22.635, minus_DI14=22.4078; 직전 완료 봉 목표를 다음 봉 시가에 모의 적용 |
| v2 | aroon_25_trend | 10000.00 | 0.00 | 대기 /  / 새 신호 대기 |
| v2 | cci_20_momentum | 9930.98 | -69.02 | sell / filled / CCI20 > 100 (전형가격·평균절대편차); 조건 미충족; CCI20=99.1325; 직전 완료 봉 목표를 다음 봉 시가에 모의 적용 |
| v2 | williams_14_recovery | 9977.72 | -22.28 | sell / filled / 직전 Williams %R14 < -80, 현재 >= -80 (한 봉 목표); 조건 미충족; Williams_R14=-6.10484, previous_R14=-17.5758; 직전 완료 봉 목표를 다음 봉 시가에 모의 적용 |
| v2 | cmf_20_accumulation | 10000.00 | 0.00 | 대기 /  / 새 신호 대기 |
| v2 | chaikin_3_10 | 9873.48 | -126.52 | buy / partial / ADL의 EMA3 - EMA10 > 0 그리고 종가 > EMA26; 조건 충족; Chaikin3_10=175820, ADL=1.95122e+07, close=118.735, EMA26=118.371; 직전 완료 봉 목표를 다음 봉 시가에 모의 적용 |
| v2 | roc_10_momentum | 10000.00 | 0.00 | 대기 /  / 새 신호 대기 |
| v2 | trix_15_trend | 9965.62 | -34.38 | buy / partial / 15봉 삼중 EMA의 1봉 변화율 TRIX > 0 그리고 종가 > EMA26; 조건 충족; TRIX15_percent=0.0496307, close=119.12, EMA26=118.125; 직전 완료 봉 목표를 다음 봉 시가에 모의 적용 |
| v2 | keltner_20_breakout | 10000.00 | 0.00 | 대기 /  / 새 신호 대기 |
| v2 | opening_range_30m | 10000.00 | 0.00 | 대기 /  / 새 신호 대기 |

### 같은 기간의 비용·노출 비교 (사후 연구)

| 전략 | 비용 전 | 비용 후 | 100% 보유 | 같은 평균 노출 보유 | 평균 노출 |
|---|---:|---:|---:|---:|---:|
| cash | 0.00% | 0.00% | 9.79% | 0.00% | 0.00% |
| buy_hold | 10.25% | 9.79% | 9.79% | 9.79% | 100.00% |
| trend_8_26 | 9.53% | 6.35% | 9.79% | 6.77% | 69.39% |
| momentum_26 | 7.43% | 3.45% | 9.79% | 6.82% | 69.92% |
| breakout_8 | 5.45% | -11.60% | 9.79% | 2.59% | 26.65% |
| reversion_12 | 4.02% | -5.96% | 9.79% | 1.64% | 16.89% |
| volume_26 | -0.20% | -5.50% | 9.79% | 0.54% | 5.54% |
| trend_8_26 AND momentum_26 | 8.87% | 4.83% | 9.79% | 6.17% | 63.32% |
| trend_8_26 + momentum_26 | 8.48% | 4.90% | 9.79% | 6.80% | 69.66% |
| trend_8_26 AND breakout_8 | 6.92% | -6.91% | 9.79% | 2.18% | 22.43% |
| trend_8_26 + breakout_8 | 7.49% | -3.03% | 9.79% | 4.67% | 48.03% |
| trend_8_26 AND reversion_12 | 0.42% | -4.91% | 9.79% | 0.66% | 6.86% |
| trend_8_26 + reversion_12 | 6.77% | 0.23% | 9.79% | 4.20% | 43.14% |
| trend_8_26 AND volume_26 | 1.13% | -1.39% | 9.79% | 0.20% | 2.11% |
| trend_8_26 + volume_26 | 4.59% | 0.69% | 9.79% | 3.64% | 37.47% |
| momentum_26 AND breakout_8 | 5.58% | -8.47% | 9.79% | 2.28% | 23.48% |
| momentum_26 + breakout_8 | 6.45% | -3.96% | 9.79% | 4.70% | 48.29% |
| momentum_26 AND reversion_12 | 1.36% | -4.43% | 9.79% | 0.74% | 7.65% |
| momentum_26 + reversion_12 | 5.75% | 0.53% | 9.79% | 4.22% | 43.41% |
| momentum_26 AND volume_26 | 0.44% | -3.69% | 9.79% | 0.28% | 2.90% |
| momentum_26 + volume_26 | 3.58% | -0.91% | 9.79% | 3.67% | 37.73% |
| breakout_8 AND reversion_12 | 0.00% | 0.00% | 9.79% | 0.00% | 0.00% |
| breakout_8 + reversion_12 | 4.76% | -8.24% | 9.79% | 2.11% | 21.78% |
| breakout_8 AND volume_26 | 1.29% | -0.82% | 9.79% | 0.15% | 1.58% |
| breakout_8 + volume_26 | 2.62% | -7.82% | 9.79% | 1.56% | 16.10% |
| reversion_12 AND volume_26 | -0.51% | -2.99% | 9.79% | 0.23% | 2.37% |
| reversion_12 + volume_26 | 1.90% | -5.33% | 9.79% | 1.09% | 11.22% |
| ema_12_26 | 9.42% | 8.05% | 9.79% | 6.61% | 67.81% |
| macd_12_26_9 | 8.10% | 4.53% | 9.79% | 3.51% | 36.15% |
| rsi_14_recovery | -0.68% | -2.74% | 9.79% | 0.13% | 1.32% |
| bollinger_20_reentry | 0.93% | -2.41% | 9.79% | 0.20% | 2.11% |
| donchian_20 | 4.64% | -8.52% | 9.79% | 1.38% | 14.25% |
| atr_14_breakout | -0.51% | -10.81% | 9.79% | 0.79% | 8.18% |
| session_vwap | 7.40% | -2.49% | 9.79% | 5.97% | 61.21% |
| obv_20 | 8.04% | -0.24% | 9.79% | 5.53% | 56.73% |
| stochastic_14_3_recovery | 1.43% | -9.06% | 9.79% | 0.66% | 6.86% |
| mfi_14_recovery | 0.02% | -0.81% | 9.79% | 0.05% | 0.53% |
| adx_14_trend | 9.26% | 6.54% | 9.79% | 4.88% | 50.13% |
| aroon_25_trend | 6.70% | 1.88% | 9.79% | 3.10% | 31.93% |
| cci_20_momentum | 7.67% | -1.01% | 9.79% | 3.28% | 33.77% |
| williams_14_recovery | 0.23% | -8.61% | 9.79% | 0.56% | 5.80% |
| cmf_20_accumulation | 9.49% | 1.51% | 9.79% | 3.82% | 39.31% |
| chaikin_3_10 | 5.76% | -2.35% | 9.79% | 5.16% | 53.03% |
| roc_10_momentum | -0.29% | -5.58% | 9.79% | 1.51% | 15.57% |
| trix_15_trend | 8.46% | 6.20% | 9.79% | 6.22% | 63.85% |
| keltner_20_breakout | 6.87% | -0.08% | 9.79% | 2.69% | 27.70% |
| opening_range_30m | 10.47% | 5.04% | 9.79% | 3.64% | 37.47% |

동일 구간·초기 자금, 종료 시 청산 비용 포함. 노출 맞춤은 사후 설명용이며 v2 실제 계좌 성과가 아닙니다.
[낙폭 분해·비용 영향·전체 구간](WMT/comparison.json)

[v1 전체 기록](WMT/accounts.json) · [v2 전체 기록](WMT/accounts-v2.json)
