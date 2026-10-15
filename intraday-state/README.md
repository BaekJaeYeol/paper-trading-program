# 모의투자 운영 현황

최근 확인: 2026-10-15T15:52:00.663804+00:00 (UTC)
다음 15분 확인 목표 (세션 실행 중에만 적용): 2026-10-15T16:07:00+00:00 (UTC, 실행 지연 가능)

실제 주문 없음. v1 기존 계좌와 v2 새 계좌의 시작일이 다르므로 수익률을 직접 우열 비교하지 마세요.
v2는 다음 봉 시가에 비용·스프레드·직전 거래량 제한을 적용한 가상 체결입니다. 미체결 잔량은 만료됩니다.

| 종목 | 상태 | 최근 성공 UTC | 마지막 완료 봉 UTC | 이번 새 봉 |
|---|---|---|---|---|
| SPY | updated | 2026-10-15T15:52:00.663804+00:00 | 2026-10-15T15:30:00+00:00 | 1 |
| QQQ | updated | 2026-10-15T15:52:00.663804+00:00 | 2026-10-15T15:30:00+00:00 | 1 |
| IWM | updated | 2026-10-15T15:52:00.663804+00:00 | 2026-10-15T15:30:00+00:00 | 1 |
| DIA | updated | 2026-10-15T15:52:00.663804+00:00 | 2026-10-15T15:30:00+00:00 | 1 |
| MSFT | updated | 2026-10-15T15:52:00.663804+00:00 | 2026-10-15T15:30:00+00:00 | 1 |
| JPM | updated | 2026-10-15T15:52:00.663804+00:00 | 2026-10-15T15:30:00+00:00 | 1 |
| XOM | updated | 2026-10-15T15:52:00.663804+00:00 | 2026-10-15T15:30:00+00:00 | 1 |
| JNJ | updated | 2026-10-15T15:52:00.663804+00:00 | 2026-10-15T15:30:00+00:00 | 1 |
| CAT | updated | 2026-10-15T15:52:00.663804+00:00 | 2026-10-15T15:30:00+00:00 | 1 |
| WMT | updated | 2026-10-15T15:52:00.663804+00:00 | 2026-10-15T15:30:00+00:00 | 1 |

이번 실행 소요: 66.99초
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
| v1 | buy_hold | 9974.41 | -25.59 | buy /  / buy_hold: prior completed bar target 100%; next bar open simulation |
| v1 | trend_8_26 | 10000.00 | 0.00 | 대기 /  / 새 신호 대기 |
| v1 | momentum_26 | 10000.00 | 0.00 | 대기 /  / 새 신호 대기 |
| v1 | breakout_8 | 10000.00 | 0.00 | 대기 /  / 새 신호 대기 |
| v1 | reversion_12 | 10000.00 | 0.00 | 대기 /  / 새 신호 대기 |
| v1 | volume_26 | 10000.00 | 0.00 | 대기 /  / 새 신호 대기 |
| v1 | trend_8_26 AND momentum_26 | 10000.00 | 0.00 | 대기 /  / 새 신호 대기 |
| v1 | trend_8_26 + momentum_26 | 10000.00 | 0.00 | 대기 /  / 새 신호 대기 |
| v1 | trend_8_26 AND breakout_8 | 10000.00 | 0.00 | 대기 /  / 새 신호 대기 |
| v1 | trend_8_26 + breakout_8 | 10000.00 | 0.00 | 대기 /  / 새 신호 대기 |
| v1 | trend_8_26 AND reversion_12 | 10000.00 | 0.00 | 대기 /  / 새 신호 대기 |
| v1 | trend_8_26 + reversion_12 | 10000.00 | 0.00 | 대기 /  / 새 신호 대기 |
| v1 | trend_8_26 AND volume_26 | 10000.00 | 0.00 | 대기 /  / 새 신호 대기 |
| v1 | trend_8_26 + volume_26 | 10000.00 | 0.00 | 대기 /  / 새 신호 대기 |
| v1 | momentum_26 AND breakout_8 | 10000.00 | 0.00 | 대기 /  / 새 신호 대기 |
| v1 | momentum_26 + breakout_8 | 10000.00 | 0.00 | 대기 /  / 새 신호 대기 |
| v1 | momentum_26 AND reversion_12 | 10000.00 | 0.00 | 대기 /  / 새 신호 대기 |
| v1 | momentum_26 + reversion_12 | 10000.00 | 0.00 | 대기 /  / 새 신호 대기 |
| v1 | momentum_26 AND volume_26 | 10000.00 | 0.00 | 대기 /  / 새 신호 대기 |
| v1 | momentum_26 + volume_26 | 10000.00 | 0.00 | 대기 /  / 새 신호 대기 |
| v1 | breakout_8 AND reversion_12 | 10000.00 | 0.00 | 대기 /  / 새 신호 대기 |
| v1 | breakout_8 + reversion_12 | 10000.00 | 0.00 | 대기 /  / 새 신호 대기 |
| v1 | breakout_8 AND volume_26 | 10000.00 | 0.00 | 대기 /  / 새 신호 대기 |
| v1 | breakout_8 + volume_26 | 10000.00 | 0.00 | 대기 /  / 새 신호 대기 |
| v1 | reversion_12 AND volume_26 | 10000.00 | 0.00 | 대기 /  / 새 신호 대기 |
| v1 | reversion_12 + volume_26 | 10000.00 | 0.00 | 대기 /  / 새 신호 대기 |
| v2 | cash | 10000.00 | 0.00 | 대기 /  / 새 신호 대기 |
| v2 | buy_hold | 9865.07 | -134.93 | buy / partial / 직전 완료 봉 목표 비중 100%; 다음 봉 시가 가정 |
| v2 | trend_8_26 | 9848.22 | -151.78 | sell / filled / 직전 완료 봉 목표 비중 0%; 다음 봉 시가 가정 |
| v2 | momentum_26 | 9861.87 | -138.13 | sell / filled / 직전 완료 봉 목표 비중 0%; 다음 봉 시가 가정 |
| v2 | breakout_8 | 9684.78 | -315.22 | sell / filled / 직전 완료 봉 목표 비중 0%; 다음 봉 시가 가정 |
| v2 | reversion_12 | 9535.84 | -464.16 | sell / filled / 직전 완료 봉 목표 비중 0%; 다음 봉 시가 가정 |
| v2 | volume_26 | 9490.95 | -509.05 | sell / filled / 직전 완료 봉 목표 비중 0%; 다음 봉 시가 가정 |
| v2 | trend_8_26 AND momentum_26 | 9868.60 | -131.40 | sell / filled / 직전 완료 봉 목표 비중 0%; 다음 봉 시가 가정 |
| v2 | trend_8_26 + momentum_26 | 9855.07 | -144.93 | sell / filled / 직전 완료 봉 목표 비중 0%; 다음 봉 시가 가정 |
| v2 | trend_8_26 AND breakout_8 | 9913.42 | -86.58 | sell / filled / 직전 완료 봉 목표 비중 0%; 다음 봉 시가 가정 |
| v2 | trend_8_26 + breakout_8 | 9766.04 | -233.96 | sell / filled / 직전 완료 봉 목표 비중 0%; 다음 봉 시가 가정 |
| v2 | trend_8_26 AND reversion_12 | 9896.11 | -103.89 | sell / filled / 직전 완료 봉 목표 비중 0%; 다음 봉 시가 가정 |
| v2 | trend_8_26 + reversion_12 | 9690.51 | -309.49 | sell / filled / 직전 완료 봉 목표 비중 0%; 다음 봉 시가 가정 |
| v2 | trend_8_26 AND volume_26 | 9897.53 | -102.47 | sell / filled / 직전 완료 봉 목표 비중 0%; 다음 봉 시가 가정 |
| v2 | trend_8_26 + volume_26 | 9688.05 | -311.95 | sell / filled / 직전 완료 봉 목표 비중 0%; 다음 봉 시가 가정 |
| v2 | momentum_26 AND breakout_8 | 9871.37 | -128.63 | sell / filled / 직전 완료 봉 목표 비중 0%; 다음 봉 시가 가정 |
| v2 | momentum_26 + breakout_8 | 9772.86 | -227.14 | sell / filled / 직전 완료 봉 목표 비중 0%; 다음 봉 시가 가정 |
| v2 | momentum_26 AND reversion_12 | 9963.21 | -36.79 | sell / filled / 직전 완료 봉 목표 비중 0%; 다음 봉 시가 가정 |
| v2 | momentum_26 + reversion_12 | 9717.64 | -282.36 | sell / filled / 직전 완료 봉 목표 비중 0%; 다음 봉 시가 가정 |
| v2 | momentum_26 AND volume_26 | 9917.25 | -82.75 | sell / filled / 직전 완료 봉 목표 비중 0%; 다음 봉 시가 가정 |
| v2 | momentum_26 + volume_26 | 9715.15 | -284.85 | sell / filled / 직전 완료 봉 목표 비중 0%; 다음 봉 시가 가정 |
| v2 | breakout_8 AND reversion_12 | 10000.00 | 0.00 | 대기 /  / 새 신호 대기 |
| v2 | breakout_8 + reversion_12 | 9650.09 | -349.91 | sell / filled / 직전 완료 봉 목표 비중 0%; 다음 봉 시가 가정 |
| v2 | breakout_8 AND volume_26 | 9933.18 | -66.82 | sell / filled / 직전 완료 봉 목표 비중 0%; 다음 봉 시가 가정 |
| v2 | breakout_8 + volume_26 | 9627.44 | -372.56 | sell / filled / 직전 완료 봉 목표 비중 0%; 다음 봉 시가 가정 |
| v2 | reversion_12 AND volume_26 | 9743.33 | -256.67 | sell / filled / 직전 완료 봉 목표 비중 0%; 다음 봉 시가 가정 |
| v2 | reversion_12 + volume_26 | 9593.37 | -406.63 | sell / filled / 직전 완료 봉 목표 비중 0%; 다음 봉 시가 가정 |

### 같은 기간의 비용·노출 비교 (사후 연구)

| 전략 | 비용 전 | 비용 후 | 100% 보유 | 같은 평균 노출 보유 | 평균 노출 |
|---|---:|---:|---:|---:|---:|
| cash | 0.00% | 0.00% | -0.12% | -0.00% | 0.00% |
| buy_hold | 0.30% | -0.12% | -0.12% | -0.12% | 100.00% |
| trend_8_26 | 1.61% | -1.33% | -0.12% | -0.06% | 49.34% |
| momentum_26 | -0.41% | -4.50% | -0.12% | -0.06% | 48.55% |
| breakout_8 | -0.74% | -15.74% | -0.12% | -0.03% | 22.16% |
| reversion_12 | -1.86% | -12.74% | -0.12% | -0.03% | 27.97% |
| volume_26 | -0.44% | -8.84% | -0.12% | -0.01% | 8.44% |
| trend_8_26 AND momentum_26 | 0.92% | -2.41% | -0.12% | -0.05% | 42.22% |
| trend_8_26 + momentum_26 | 0.60% | -2.72% | -0.12% | -0.06% | 48.95% |
| trend_8_26 AND breakout_8 | -0.06% | -10.40% | -0.12% | -0.02% | 13.19% |
| trend_8_26 + breakout_8 | 0.43% | -8.82% | -0.12% | -0.04% | 35.76% |
| trend_8_26 AND reversion_12 | 0.10% | -4.01% | -0.12% | -0.01% | 6.07% |
| trend_8_26 + reversion_12 | -0.13% | -7.03% | -0.12% | -0.05% | 38.66% |
| trend_8_26 AND volume_26 | -0.07% | -3.77% | -0.12% | -0.00% | 3.69% |
| trend_8_26 + volume_26 | 0.59% | -5.17% | -0.12% | -0.04% | 28.90% |
| momentum_26 AND breakout_8 | 0.24% | -10.13% | -0.12% | -0.02% | 14.25% |
| momentum_26 + breakout_8 | -0.57% | -10.30% | -0.12% | -0.04% | 35.36% |
| momentum_26 AND reversion_12 | -0.88% | -5.75% | -0.12% | -0.01% | 6.86% |
| momentum_26 + reversion_12 | -1.13% | -8.15% | -0.12% | -0.05% | 38.26% |
| momentum_26 AND volume_26 | -0.22% | -3.11% | -0.12% | -0.00% | 2.11% |
| momentum_26 + volume_26 | -0.42% | -5.52% | -0.12% | -0.03% | 28.50% |
| breakout_8 AND reversion_12 | 0.00% | 0.00% | -0.12% | -0.00% | 0.00% |
| breakout_8 + reversion_12 | -1.30% | -13.72% | -0.12% | -0.03% | 25.07% |
| breakout_8 AND volume_26 | 0.05% | -1.61% | -0.12% | -0.00% | 1.32% |
| breakout_8 + volume_26 | -0.59% | -11.44% | -0.12% | -0.02% | 15.31% |
| reversion_12 AND volume_26 | -0.67% | -4.76% | -0.12% | -0.00% | 3.96% |
| reversion_12 + volume_26 | -1.15% | -10.45% | -0.12% | -0.02% | 18.21% |

동일 구간·초기 자금, 종료 시 청산 비용 포함. 노출 맞춤은 사후 설명용이며 v2 실제 계좌 성과가 아닙니다.
[낙폭 분해·비용 영향·전체 구간](SPY/comparison.json)

[v1 전체 기록](SPY/accounts.json) · [v2 전체 기록](SPY/accounts-v2.json)

## QQQ 계좌

| 모델 | 전략 | 평가액 USD | 손익 USD | 최근 매매·이유 |
|---|---|---:|---:|---|
| v1 | cash | 10000.00 | 0.00 | 대기 /  / 새 신호 대기 |
| v1 | buy_hold | 9969.29 | -30.71 | buy /  / buy_hold: prior completed bar target 100%; next bar open simulation |
| v1 | trend_8_26 | 10000.00 | 0.00 | 대기 /  / 새 신호 대기 |
| v1 | momentum_26 | 10000.00 | 0.00 | 대기 /  / 새 신호 대기 |
| v1 | breakout_8 | 10000.00 | 0.00 | 대기 /  / 새 신호 대기 |
| v1 | reversion_12 | 10000.00 | 0.00 | 대기 /  / 새 신호 대기 |
| v1 | volume_26 | 10000.00 | 0.00 | 대기 /  / 새 신호 대기 |
| v1 | trend_8_26 AND momentum_26 | 10000.00 | 0.00 | 대기 /  / 새 신호 대기 |
| v1 | trend_8_26 + momentum_26 | 10000.00 | 0.00 | 대기 /  / 새 신호 대기 |
| v1 | trend_8_26 AND breakout_8 | 10000.00 | 0.00 | 대기 /  / 새 신호 대기 |
| v1 | trend_8_26 + breakout_8 | 10000.00 | 0.00 | 대기 /  / 새 신호 대기 |
| v1 | trend_8_26 AND reversion_12 | 10000.00 | 0.00 | 대기 /  / 새 신호 대기 |
| v1 | trend_8_26 + reversion_12 | 10000.00 | 0.00 | 대기 /  / 새 신호 대기 |
| v1 | trend_8_26 AND volume_26 | 10000.00 | 0.00 | 대기 /  / 새 신호 대기 |
| v1 | trend_8_26 + volume_26 | 10000.00 | 0.00 | 대기 /  / 새 신호 대기 |
| v1 | momentum_26 AND breakout_8 | 10000.00 | 0.00 | 대기 /  / 새 신호 대기 |
| v1 | momentum_26 + breakout_8 | 10000.00 | 0.00 | 대기 /  / 새 신호 대기 |
| v1 | momentum_26 AND reversion_12 | 10000.00 | 0.00 | 대기 /  / 새 신호 대기 |
| v1 | momentum_26 + reversion_12 | 10000.00 | 0.00 | 대기 /  / 새 신호 대기 |
| v1 | momentum_26 AND volume_26 | 10000.00 | 0.00 | 대기 /  / 새 신호 대기 |
| v1 | momentum_26 + volume_26 | 10000.00 | 0.00 | 대기 /  / 새 신호 대기 |
| v1 | breakout_8 AND reversion_12 | 10000.00 | 0.00 | 대기 /  / 새 신호 대기 |
| v1 | breakout_8 + reversion_12 | 10000.00 | 0.00 | 대기 /  / 새 신호 대기 |
| v1 | breakout_8 AND volume_26 | 10000.00 | 0.00 | 대기 /  / 새 신호 대기 |
| v1 | breakout_8 + volume_26 | 10000.00 | 0.00 | 대기 /  / 새 신호 대기 |
| v1 | reversion_12 AND volume_26 | 10000.00 | 0.00 | 대기 /  / 새 신호 대기 |
| v1 | reversion_12 + volume_26 | 10000.00 | 0.00 | 대기 /  / 새 신호 대기 |
| v2 | cash | 10000.00 | 0.00 | 대기 /  / 새 신호 대기 |
| v2 | buy_hold | 9635.19 | -364.81 | buy / partial / 직전 완료 봉 목표 비중 100%; 다음 봉 시가 가정 |
| v2 | trend_8_26 | 9781.79 | -218.21 | sell / filled / 직전 완료 봉 목표 비중 0%; 다음 봉 시가 가정 |
| v2 | momentum_26 | 9936.83 | -63.17 | sell / filled / 직전 완료 봉 목표 비중 0%; 다음 봉 시가 가정 |
| v2 | breakout_8 | 9785.97 | -214.03 | sell / filled / 직전 완료 봉 목표 비중 0%; 다음 봉 시가 가정 |
| v2 | reversion_12 | 9515.83 | -484.17 | sell / filled / 직전 완료 봉 목표 비중 0%; 다음 봉 시가 가정 |
| v2 | volume_26 | 9565.80 | -434.20 | 중단: 손실 한도 / sell / filled / 직전 완료 봉 목표 비중 0%; 다음 봉 시가 가정 |
| v2 | trend_8_26 AND momentum_26 | 9936.83 | -63.17 | sell / filled / 직전 완료 봉 목표 비중 0%; 다음 봉 시가 가정 |
| v2 | trend_8_26 + momentum_26 | 9859.04 | -140.96 | sell / filled / 직전 완료 봉 목표 비중 0%; 다음 봉 시가 가정 |
| v2 | trend_8_26 AND breakout_8 | 9968.70 | -31.30 | sell / filled / 직전 완료 봉 목표 비중 0%; 다음 봉 시가 가정 |
| v2 | trend_8_26 + breakout_8 | 9783.85 | -216.15 | sell / filled / 직전 완료 봉 목표 비중 0%; 다음 봉 시가 가정 |
| v2 | trend_8_26 AND reversion_12 | 9861.14 | -138.86 | sell / filled / 직전 완료 봉 목표 비중 0%; 다음 봉 시가 가정 |
| v2 | trend_8_26 + reversion_12 | 9647.62 | -352.38 | sell / filled / 직전 완료 봉 목표 비중 0%; 다음 봉 시가 가정 |
| v2 | trend_8_26 AND volume_26 | 9840.10 | -159.90 | sell / filled / 직전 완료 봉 목표 비중 0%; 다음 봉 시가 가정 |
| v2 | trend_8_26 + volume_26 | 9611.52 | -388.48 | sell / filled / 직전 완료 봉 목표 비중 0%; 다음 봉 시가 가정 |
| v2 | momentum_26 AND breakout_8 | 10000.00 | 0.00 | 대기 /  / 새 신호 대기 |
| v2 | momentum_26 + breakout_8 | 9861.05 | -138.95 | sell / filled / 직전 완료 봉 목표 비중 0%; 다음 봉 시가 가정 |
| v2 | momentum_26 AND reversion_12 | 10000.00 | 0.00 | 대기 /  / 새 신호 대기 |
| v2 | momentum_26 + reversion_12 | 9744.19 | -255.81 | sell / filled / 직전 완료 봉 목표 비중 0%; 다음 봉 시가 가정 |
| v2 | momentum_26 AND volume_26 | 9936.83 | -63.17 | sell / filled / 직전 완료 봉 목표 비중 0%; 다음 봉 시가 가정 |
| v2 | momentum_26 + volume_26 | 9687.39 | -312.61 | sell / filled / 직전 완료 봉 목표 비중 0%; 다음 봉 시가 가정 |
| v2 | breakout_8 AND reversion_12 | 10000.00 | 0.00 | 대기 /  / 새 신호 대기 |
| v2 | breakout_8 + reversion_12 | 9710.65 | -289.35 | sell / filled / 직전 완료 봉 목표 비중 0%; 다음 봉 시가 가정 |
| v2 | breakout_8 AND volume_26 | 9947.98 | -52.02 | sell / filled / 직전 완료 봉 목표 비중 0%; 다음 봉 시가 가정 |
| v2 | breakout_8 + volume_26 | 9654.08 | -345.92 | sell / filled / 직전 완료 봉 목표 비중 0%; 다음 봉 시가 가정 |
| v2 | reversion_12 AND volume_26 | 9547.64 | -452.36 | 중단: 손실 한도 / sell / filled / 직전 완료 봉 목표 비중 0%; 다음 봉 시가 가정 |
| v2 | reversion_12 + volume_26 | 9500.03 | -499.97 | sell / filled / 직전 완료 봉 목표 비중 0%; 다음 봉 시가 가정 |

### 같은 기간의 비용·노출 비교 (사후 연구)

| 전략 | 비용 전 | 비용 후 | 100% 보유 | 같은 평균 노출 보유 | 평균 노출 |
|---|---:|---:|---:|---:|---:|
| cash | 0.00% | 0.00% | -2.67% | -0.00% | 0.00% |
| buy_hold | -2.27% | -2.67% | -2.67% | -2.67% | 100.00% |
| trend_8_26 | 0.31% | -3.00% | -2.67% | -1.33% | 49.87% |
| momentum_26 | -1.28% | -6.13% | -2.67% | -1.17% | 43.80% |
| breakout_8 | -1.69% | -16.89% | -2.67% | -0.47% | 17.68% |
| reversion_12 | -0.86% | -12.96% | -2.67% | -0.71% | 26.65% |
| volume_26 | -1.10% | -13.17% | -2.67% | -0.37% | 13.72% |
| trend_8_26 AND momentum_26 | -0.32% | -4.42% | -2.67% | -1.05% | 39.31% |
| trend_8_26 + momentum_26 | -0.48% | -4.38% | -2.67% | -1.25% | 46.84% |
| trend_8_26 AND breakout_8 | -0.58% | -10.12% | -2.67% | -0.29% | 10.82% |
| trend_8_26 + breakout_8 | -0.69% | -9.84% | -2.67% | -0.90% | 33.78% |
| trend_8_26 AND reversion_12 | 0.42% | -5.31% | -2.67% | -0.16% | 6.07% |
| trend_8_26 + reversion_12 | -0.27% | -7.54% | -2.67% | -1.02% | 38.26% |
| trend_8_26 AND volume_26 | -0.71% | -5.59% | -2.67% | -0.11% | 4.22% |
| trend_8_26 + volume_26 | -0.39% | -8.04% | -2.67% | -0.85% | 31.80% |
| momentum_26 AND breakout_8 | -0.74% | -9.88% | -2.67% | -0.30% | 11.08% |
| momentum_26 + breakout_8 | -1.48% | -11.49% | -2.67% | -0.82% | 30.75% |
| momentum_26 AND reversion_12 | -0.02% | -5.73% | -2.67% | -0.13% | 4.75% |
| momentum_26 + reversion_12 | -1.06% | -9.05% | -2.67% | -0.94% | 35.23% |
| momentum_26 AND volume_26 | -0.30% | -4.40% | -2.67% | -0.09% | 3.43% |
| momentum_26 + volume_26 | -1.18% | -9.54% | -2.67% | -0.77% | 28.77% |
| breakout_8 AND reversion_12 | 0.00% | 0.00% | -2.67% | -0.00% | 0.00% |
| breakout_8 + reversion_12 | -1.27% | -14.06% | -2.67% | -0.59% | 22.17% |
| breakout_8 AND volume_26 | 0.04% | -2.04% | -2.67% | -0.04% | 1.32% |
| breakout_8 + volume_26 | -1.39% | -13.80% | -2.67% | -0.42% | 15.71% |
| reversion_12 AND volume_26 | -1.25% | -8.44% | -2.67% | -0.23% | 8.71% |
| reversion_12 + volume_26 | -0.97% | -12.70% | -2.67% | -0.54% | 20.19% |

동일 구간·초기 자금, 종료 시 청산 비용 포함. 노출 맞춤은 사후 설명용이며 v2 실제 계좌 성과가 아닙니다.
[낙폭 분해·비용 영향·전체 구간](QQQ/comparison.json)

[v1 전체 기록](QQQ/accounts.json) · [v2 전체 기록](QQQ/accounts-v2.json)

## IWM 계좌

| 모델 | 전략 | 평가액 USD | 손익 USD | 최근 매매·이유 |
|---|---|---:|---:|---|
| v1 | cash | 10000.00 | 0.00 | 대기 /  / 새 신호 대기 |
| v1 | buy_hold | 9968.37 | -31.63 | buy /  / buy_hold: prior completed bar target 100%; next bar open simulation |
| v1 | trend_8_26 | 9968.37 | -31.63 | buy /  / trend_8_26: prior completed bar target 100%; next bar open simulation |
| v1 | momentum_26 | 9968.37 | -31.63 | buy /  / momentum_26: prior completed bar target 100%; next bar open simulation |
| v1 | breakout_8 | 10000.00 | 0.00 | 대기 /  / 새 신호 대기 |
| v1 | reversion_12 | 10000.00 | 0.00 | 대기 /  / 새 신호 대기 |
| v1 | volume_26 | 10000.00 | 0.00 | 대기 /  / 새 신호 대기 |
| v1 | trend_8_26 AND momentum_26 | 9968.37 | -31.63 | buy /  / trend_8_26 AND momentum_26: prior completed bar target 100%; next bar open simulation |
| v1 | trend_8_26 + momentum_26 | 9968.37 | -31.63 | buy /  / trend_8_26 + momentum_26: prior completed bar target 100%; next bar open simulation |
| v1 | trend_8_26 AND breakout_8 | 10000.00 | 0.00 | 대기 /  / 새 신호 대기 |
| v1 | trend_8_26 + breakout_8 | 9984.15 | -15.85 | buy /  / trend_8_26 + breakout_8: prior completed bar target 50%; next bar open simulation |
| v1 | trend_8_26 AND reversion_12 | 10000.00 | 0.00 | 대기 /  / 새 신호 대기 |
| v1 | trend_8_26 + reversion_12 | 9984.15 | -15.85 | buy /  / trend_8_26 + reversion_12: prior completed bar target 50%; next bar open simulation |
| v1 | trend_8_26 AND volume_26 | 10000.00 | 0.00 | 대기 /  / 새 신호 대기 |
| v1 | trend_8_26 + volume_26 | 9984.15 | -15.85 | buy /  / trend_8_26 + volume_26: prior completed bar target 50%; next bar open simulation |
| v1 | momentum_26 AND breakout_8 | 10000.00 | 0.00 | 대기 /  / 새 신호 대기 |
| v1 | momentum_26 + breakout_8 | 9984.15 | -15.85 | buy /  / momentum_26 + breakout_8: prior completed bar target 50%; next bar open simulation |
| v1 | momentum_26 AND reversion_12 | 10000.00 | 0.00 | 대기 /  / 새 신호 대기 |
| v1 | momentum_26 + reversion_12 | 9984.15 | -15.85 | buy /  / momentum_26 + reversion_12: prior completed bar target 50%; next bar open simulation |
| v1 | momentum_26 AND volume_26 | 10000.00 | 0.00 | 대기 /  / 새 신호 대기 |
| v1 | momentum_26 + volume_26 | 9984.15 | -15.85 | buy /  / momentum_26 + volume_26: prior completed bar target 50%; next bar open simulation |
| v1 | breakout_8 AND reversion_12 | 10000.00 | 0.00 | 대기 /  / 새 신호 대기 |
| v1 | breakout_8 + reversion_12 | 10000.00 | 0.00 | 대기 /  / 새 신호 대기 |
| v1 | breakout_8 AND volume_26 | 10000.00 | 0.00 | 대기 /  / 새 신호 대기 |
| v1 | breakout_8 + volume_26 | 10000.00 | 0.00 | 대기 /  / 새 신호 대기 |
| v1 | reversion_12 AND volume_26 | 10000.00 | 0.00 | 대기 /  / 새 신호 대기 |
| v1 | reversion_12 + volume_26 | 10000.00 | 0.00 | 대기 /  / 새 신호 대기 |
| v2 | cash | 10000.00 | 0.00 | 대기 /  / 새 신호 대기 |
| v2 | buy_hold | 9803.44 | -196.56 | buy / partial / 직전 완료 봉 목표 비중 100%; 다음 봉 시가 가정 |
| v2 | trend_8_26 | 9781.00 | -219.00 | buy / partial / 직전 완료 봉 목표 비중 100%; 다음 봉 시가 가정 |
| v2 | momentum_26 | 9782.00 | -218.00 | buy / partial / 직전 완료 봉 목표 비중 100%; 다음 봉 시가 가정 |
| v2 | breakout_8 | 9666.31 | -333.69 | sell / filled / 직전 완료 봉 목표 비중 0%; 다음 봉 시가 가정 |
| v2 | reversion_12 | 9538.67 | -461.33 | sell / filled / 직전 완료 봉 목표 비중 0%; 다음 봉 시가 가정 |
| v2 | volume_26 | 9513.36 | -486.64 | sell / filled / 직전 완료 봉 목표 비중 0%; 다음 봉 시가 가정 |
| v2 | trend_8_26 AND momentum_26 | 9932.81 | -67.19 | buy / partial / 직전 완료 봉 목표 비중 100%; 다음 봉 시가 가정 |
| v2 | trend_8_26 + momentum_26 | 9802.20 | -197.80 | buy / partial / 직전 완료 봉 목표 비중 100%; 다음 봉 시가 가정 |
| v2 | trend_8_26 AND breakout_8 | 9962.82 | -37.18 | sell / filled / 직전 완료 봉 목표 비중 0%; 다음 봉 시가 가정 |
| v2 | trend_8_26 + breakout_8 | 9744.04 | -255.96 | sell / filled / 직전 완료 봉 목표 비중 50%; 다음 봉 시가 가정 |
| v2 | trend_8_26 AND reversion_12 | 9881.82 | -118.18 | sell / filled / 직전 완료 봉 목표 비중 0%; 다음 봉 시가 가정 |
| v2 | trend_8_26 + reversion_12 | 9658.95 | -341.05 | buy / filled / 직전 완료 봉 목표 비중 50%; 다음 봉 시가 가정 |
| v2 | trend_8_26 AND volume_26 | 9862.83 | -137.17 | sell / filled / 직전 완료 봉 목표 비중 0%; 다음 봉 시가 가정 |
| v2 | trend_8_26 + volume_26 | 9666.56 | -333.44 | buy / filled / 직전 완료 봉 목표 비중 50%; 다음 봉 시가 가정 |
| v2 | momentum_26 AND breakout_8 | 9854.44 | -145.56 | sell / filled / 직전 완료 봉 목표 비중 0%; 다음 봉 시가 가정 |
| v2 | momentum_26 + breakout_8 | 9723.98 | -276.02 | sell / filled / 직전 완료 봉 목표 비중 50%; 다음 봉 시가 가정 |
| v2 | momentum_26 AND reversion_12 | 9960.59 | -39.41 | sell / filled / 직전 완료 봉 목표 비중 0%; 다음 봉 시가 가정 |
| v2 | momentum_26 + reversion_12 | 9679.54 | -320.46 | buy / filled / 직전 완료 봉 목표 비중 50%; 다음 봉 시가 가정 |
| v2 | momentum_26 AND volume_26 | 9897.79 | -102.21 | sell / filled / 직전 완료 봉 목표 비중 0%; 다음 봉 시가 가정 |
| v2 | momentum_26 + volume_26 | 9646.57 | -353.43 | buy / filled / 직전 완료 봉 목표 비중 50%; 다음 봉 시가 가정 |
| v2 | breakout_8 AND reversion_12 | 10000.00 | 0.00 | 대기 /  / 새 신호 대기 |
| v2 | breakout_8 + reversion_12 | 9642.35 | -357.65 | sell / filled / 직전 완료 봉 목표 비중 0%; 다음 봉 시가 가정 |
| v2 | breakout_8 AND volume_26 | 9746.03 | -253.97 | sell / filled / 직전 완료 봉 목표 비중 0%; 다음 봉 시가 가정 |
| v2 | breakout_8 + volume_26 | 9609.68 | -390.32 | sell / filled / 직전 완료 봉 목표 비중 0%; 다음 봉 시가 가정 |
| v2 | reversion_12 AND volume_26 | 9740.75 | -259.25 | sell / filled / 직전 완료 봉 목표 비중 0%; 다음 봉 시가 가정 |
| v2 | reversion_12 + volume_26 | 9545.82 | -454.18 | sell / filled / 직전 완료 봉 목표 비중 0%; 다음 봉 시가 가정 |

### 같은 기간의 비용·노출 비교 (사후 연구)

| 전략 | 비용 전 | 비용 후 | 100% 보유 | 같은 평균 노출 보유 | 평균 노출 |
|---|---:|---:|---:|---:|---:|
| cash | 0.00% | 0.00% | -3.30% | -0.00% | 0.00% |
| buy_hold | -2.90% | -3.30% | -3.30% | -3.30% | 100.00% |
| trend_8_26 | -2.33% | -6.35% | -3.30% | -1.48% | 44.59% |
| momentum_26 | -2.99% | -8.53% | -3.30% | -1.27% | 38.26% |
| breakout_8 | -1.05% | -14.57% | -3.30% | -0.63% | 19.00% |
| reversion_12 | -2.15% | -14.82% | -3.30% | -1.00% | 30.08% |
| volume_26 | -2.34% | -9.45% | -3.30% | -0.29% | 8.71% |
| trend_8_26 AND momentum_26 | -2.65% | -7.04% | -3.30% | -1.09% | 32.72% |
| trend_8_26 + momentum_26 | -2.65% | -7.05% | -3.30% | -1.38% | 41.43% |
| trend_8_26 AND breakout_8 | -0.92% | -8.90% | -3.30% | -0.35% | 10.55% |
| trend_8_26 + breakout_8 | -1.68% | -10.36% | -3.30% | -1.06% | 31.80% |
| trend_8_26 AND reversion_12 | -0.12% | -5.03% | -3.30% | -0.20% | 6.07% |
| trend_8_26 + reversion_12 | -2.23% | -10.50% | -3.30% | -1.24% | 37.34% |
| trend_8_26 AND volume_26 | -1.05% | -4.72% | -3.30% | -0.12% | 3.69% |
| trend_8_26 + volume_26 | -2.32% | -7.72% | -3.30% | -0.89% | 26.65% |
| momentum_26 AND breakout_8 | -0.10% | -7.37% | -3.30% | -0.33% | 9.76% |
| momentum_26 + breakout_8 | -2.02% | -11.60% | -3.30% | -0.95% | 28.63% |
| momentum_26 AND reversion_12 | -0.05% | -3.76% | -3.30% | -0.11% | 3.43% |
| momentum_26 + reversion_12 | -2.56% | -10.62% | -3.30% | -1.14% | 34.17% |
| momentum_26 AND volume_26 | -1.34% | -4.20% | -3.30% | -0.07% | 2.11% |
| momentum_26 + volume_26 | -2.66% | -8.61% | -3.30% | -0.78% | 23.49% |
| breakout_8 AND reversion_12 | 0.00% | 0.00% | -3.30% | -0.00% | 0.00% |
| breakout_8 + reversion_12 | -1.60% | -13.99% | -3.30% | -0.82% | 24.55% |
| breakout_8 AND volume_26 | -1.33% | -4.19% | -3.30% | -0.08% | 2.37% |
| breakout_8 + volume_26 | -1.69% | -11.87% | -3.30% | -0.46% | 13.86% |
| reversion_12 AND volume_26 | -0.38% | -4.47% | -3.30% | -0.15% | 4.49% |
| reversion_12 + volume_26 | -2.24% | -11.63% | -3.30% | -0.65% | 19.40% |

동일 구간·초기 자금, 종료 시 청산 비용 포함. 노출 맞춤은 사후 설명용이며 v2 실제 계좌 성과가 아닙니다.
[낙폭 분해·비용 영향·전체 구간](IWM/comparison.json)

[v1 전체 기록](IWM/accounts.json) · [v2 전체 기록](IWM/accounts-v2.json)

## DIA 계좌

| 모델 | 전략 | 평가액 USD | 손익 USD | 최근 매매·이유 |
|---|---|---:|---:|---|
| v1 | cash | 10000.00 | 0.00 | 대기 /  / 새 신호 대기 |
| v1 | buy_hold | 9971.60 | -28.40 | buy /  / buy_hold: prior completed bar target 100%; next bar open simulation |
| v1 | trend_8_26 | 9971.60 | -28.40 | buy /  / trend_8_26: prior completed bar target 100%; next bar open simulation |
| v1 | momentum_26 | 9971.60 | -28.40 | buy /  / momentum_26: prior completed bar target 100%; next bar open simulation |
| v1 | breakout_8 | 10000.00 | 0.00 | 대기 /  / 새 신호 대기 |
| v1 | reversion_12 | 10000.00 | 0.00 | 대기 /  / 새 신호 대기 |
| v1 | volume_26 | 10000.00 | 0.00 | 대기 /  / 새 신호 대기 |
| v1 | trend_8_26 AND momentum_26 | 9971.60 | -28.40 | buy /  / trend_8_26 AND momentum_26: prior completed bar target 100%; next bar open simulation |
| v1 | trend_8_26 + momentum_26 | 9971.60 | -28.40 | buy /  / trend_8_26 + momentum_26: prior completed bar target 100%; next bar open simulation |
| v1 | trend_8_26 AND breakout_8 | 10000.00 | 0.00 | 대기 /  / 새 신호 대기 |
| v1 | trend_8_26 + breakout_8 | 9985.77 | -14.23 | buy /  / trend_8_26 + breakout_8: prior completed bar target 50%; next bar open simulation |
| v1 | trend_8_26 AND reversion_12 | 10000.00 | 0.00 | 대기 /  / 새 신호 대기 |
| v1 | trend_8_26 + reversion_12 | 9985.77 | -14.23 | buy /  / trend_8_26 + reversion_12: prior completed bar target 50%; next bar open simulation |
| v1 | trend_8_26 AND volume_26 | 10000.00 | 0.00 | 대기 /  / 새 신호 대기 |
| v1 | trend_8_26 + volume_26 | 9985.77 | -14.23 | buy /  / trend_8_26 + volume_26: prior completed bar target 50%; next bar open simulation |
| v1 | momentum_26 AND breakout_8 | 10000.00 | 0.00 | 대기 /  / 새 신호 대기 |
| v1 | momentum_26 + breakout_8 | 9985.77 | -14.23 | buy /  / momentum_26 + breakout_8: prior completed bar target 50%; next bar open simulation |
| v1 | momentum_26 AND reversion_12 | 10000.00 | 0.00 | 대기 /  / 새 신호 대기 |
| v1 | momentum_26 + reversion_12 | 9985.77 | -14.23 | buy /  / momentum_26 + reversion_12: prior completed bar target 50%; next bar open simulation |
| v1 | momentum_26 AND volume_26 | 10000.00 | 0.00 | 대기 /  / 새 신호 대기 |
| v1 | momentum_26 + volume_26 | 9985.77 | -14.23 | buy /  / momentum_26 + volume_26: prior completed bar target 50%; next bar open simulation |
| v1 | breakout_8 AND reversion_12 | 10000.00 | 0.00 | 대기 /  / 새 신호 대기 |
| v1 | breakout_8 + reversion_12 | 10000.00 | 0.00 | 대기 /  / 새 신호 대기 |
| v1 | breakout_8 AND volume_26 | 10000.00 | 0.00 | 대기 /  / 새 신호 대기 |
| v1 | breakout_8 + volume_26 | 10000.00 | 0.00 | 대기 /  / 새 신호 대기 |
| v1 | reversion_12 AND volume_26 | 10000.00 | 0.00 | 대기 /  / 새 신호 대기 |
| v1 | reversion_12 + volume_26 | 10000.00 | 0.00 | 대기 /  / 새 신호 대기 |
| v2 | cash | 10000.00 | 0.00 | 대기 /  / 새 신호 대기 |
| v2 | buy_hold | 10054.78 | 54.78 | buy / partial / 직전 완료 봉 목표 비중 100%; 다음 봉 시가 가정 |
| v2 | trend_8_26 | 9867.40 | -132.60 | buy / partial / 직전 완료 봉 목표 비중 100%; 다음 봉 시가 가정 |
| v2 | momentum_26 | 9975.89 | -24.11 | buy / partial / 직전 완료 봉 목표 비중 100%; 다음 봉 시가 가정 |
| v2 | breakout_8 | 9626.51 | -373.49 | sell / filled / 직전 완료 봉 목표 비중 0%; 다음 봉 시가 가정 |
| v2 | reversion_12 | 9698.03 | -301.97 | sell / filled / 직전 완료 봉 목표 비중 0%; 다음 봉 시가 가정 |
| v2 | volume_26 | 9718.21 | -281.79 | sell / filled / 직전 완료 봉 목표 비중 0%; 다음 봉 시가 가정 |
| v2 | trend_8_26 AND momentum_26 | 9971.26 | -28.74 | buy / partial / 직전 완료 봉 목표 비중 100%; 다음 봉 시가 가정 |
| v2 | trend_8_26 + momentum_26 | 9921.56 | -78.44 | buy / partial / 직전 완료 봉 목표 비중 100%; 다음 봉 시가 가정 |
| v2 | trend_8_26 AND breakout_8 | 9789.40 | -210.60 | sell / filled / 직전 완료 봉 목표 비중 0%; 다음 봉 시가 가정 |
| v2 | trend_8_26 + breakout_8 | 9746.24 | -253.76 | sell / filled / 직전 완료 봉 목표 비중 50%; 다음 봉 시가 가정 |
| v2 | trend_8_26 AND reversion_12 | 9810.77 | -189.23 | sell / filled / 직전 완료 봉 목표 비중 0%; 다음 봉 시가 가정 |
| v2 | trend_8_26 + reversion_12 | 9782.14 | -217.86 | buy / filled / 직전 완료 봉 목표 비중 50%; 다음 봉 시가 가정 |
| v2 | trend_8_26 AND volume_26 | 9858.88 | -141.12 | sell / filled / 직전 완료 봉 목표 비중 0%; 다음 봉 시가 가정 |
| v2 | trend_8_26 + volume_26 | 9813.10 | -186.90 | buy / filled / 직전 완료 봉 목표 비중 50%; 다음 봉 시가 가정 |
| v2 | momentum_26 AND breakout_8 | 9778.26 | -221.74 | sell / filled / 직전 완료 봉 목표 비중 0%; 다음 봉 시가 가정 |
| v2 | momentum_26 + breakout_8 | 9799.74 | -200.26 | sell / filled / 직전 완료 봉 목표 비중 50%; 다음 봉 시가 가정 |
| v2 | momentum_26 AND reversion_12 | 9955.97 | -44.03 | sell / filled / 직전 완료 봉 목표 비중 0%; 다음 봉 시가 가정 |
| v2 | momentum_26 + reversion_12 | 9835.84 | -164.16 | buy / filled / 직전 완료 봉 목표 비중 50%; 다음 봉 시가 가정 |
| v2 | momentum_26 AND volume_26 | 9791.42 | -208.58 | sell / filled / 직전 완료 봉 목표 비중 0%; 다음 봉 시가 가정 |
| v2 | momentum_26 + volume_26 | 9887.77 | -112.23 | buy / filled / 직전 완료 봉 목표 비중 50%; 다음 봉 시가 가정 |
| v2 | breakout_8 AND reversion_12 | 10000.00 | 0.00 | 대기 /  / 새 신호 대기 |
| v2 | breakout_8 + reversion_12 | 9661.83 | -338.17 | sell / filled / 직전 완료 봉 목표 비중 0%; 다음 봉 시가 가정 |
| v2 | breakout_8 AND volume_26 | 9796.56 | -203.44 | sell / filled / 직전 완료 봉 목표 비중 0%; 다음 봉 시가 가정 |
| v2 | breakout_8 + volume_26 | 9672.16 | -327.84 | sell / filled / 직전 완료 봉 목표 비중 0%; 다음 봉 시가 가정 |
| v2 | reversion_12 AND volume_26 | 10000.00 | 0.00 | 대기 /  / 새 신호 대기 |
| v2 | reversion_12 + volume_26 | 9707.85 | -292.15 | sell / filled / 직전 완료 봉 목표 비중 0%; 다음 봉 시가 가정 |

### 같은 기간의 비용·노출 비교 (사후 연구)

| 전략 | 비용 전 | 비용 후 | 100% 보유 | 같은 평균 노출 보유 | 평균 노출 |
|---|---:|---:|---:|---:|---:|
| cash | 0.00% | 0.00% | 0.96% | 0.00% | 0.00% |
| buy_hold | 1.39% | 0.96% | 0.96% | 0.96% | 100.00% |
| trend_8_26 | 1.70% | -2.89% | 0.96% | 0.54% | 55.94% |
| momentum_26 | 0.08% | -4.03% | 0.96% | 0.49% | 50.40% |
| breakout_8 | 0.14% | -16.40% | 0.96% | 0.23% | 23.48% |
| reversion_12 | -1.36% | -9.30% | 0.96% | 0.24% | 24.80% |
| volume_26 | -0.82% | -11.45% | 0.96% | 0.11% | 11.61% |
| trend_8_26 AND momentum_26 | 1.56% | -2.62% | 0.96% | 0.43% | 44.59% |
| trend_8_26 + momentum_26 | 0.89% | -3.46% | 0.96% | 0.51% | 53.17% |
| trend_8_26 AND breakout_8 | 0.71% | -10.84% | 0.96% | 0.15% | 15.30% |
| trend_8_26 + breakout_8 | 0.92% | -9.71% | 0.96% | 0.38% | 39.72% |
| trend_8_26 AND reversion_12 | 0.37% | -4.56% | 0.96% | 0.06% | 6.33% |
| trend_8_26 + reversion_12 | 0.17% | -5.76% | 0.96% | 0.39% | 40.37% |
| trend_8_26 AND volume_26 | 0.73% | -5.02% | 0.96% | 0.06% | 5.80% |
| trend_8_26 + volume_26 | 0.44% | -7.08% | 0.96% | 0.33% | 33.78% |
| momentum_26 AND breakout_8 | -0.09% | -11.17% | 0.96% | 0.15% | 15.57% |
| momentum_26 + breakout_8 | 0.12% | -10.24% | 0.96% | 0.36% | 36.95% |
| momentum_26 AND reversion_12 | -0.18% | -3.88% | 0.96% | 0.06% | 5.80% |
| momentum_26 + reversion_12 | -0.63% | -5.92% | 0.96% | 0.36% | 37.60% |
| momentum_26 AND volume_26 | -0.36% | -6.05% | 0.96% | 0.05% | 5.01% |
| momentum_26 + volume_26 | -0.37% | -7.04% | 0.96% | 0.30% | 31.01% |
| breakout_8 AND reversion_12 | 0.00% | 0.00% | 0.96% | 0.00% | 0.00% |
| breakout_8 + reversion_12 | -0.61% | -12.57% | 0.96% | 0.23% | 24.15% |
| breakout_8 AND volume_26 | -0.82% | -4.90% | 0.96% | 0.03% | 3.43% |
| breakout_8 + volume_26 | -0.34% | -13.06% | 0.96% | 0.17% | 17.55% |
| reversion_12 AND volume_26 | -0.20% | -5.11% | 0.96% | 0.04% | 3.96% |
| reversion_12 + volume_26 | -1.09% | -10.39% | 0.96% | 0.18% | 18.21% |

동일 구간·초기 자금, 종료 시 청산 비용 포함. 노출 맞춤은 사후 설명용이며 v2 실제 계좌 성과가 아닙니다.
[낙폭 분해·비용 영향·전체 구간](DIA/comparison.json)

[v1 전체 기록](DIA/accounts.json) · [v2 전체 기록](DIA/accounts-v2.json)

## MSFT 계좌

| 모델 | 전략 | 평가액 USD | 손익 USD | 최근 매매·이유 |
|---|---|---:|---:|---|
| v1 | cash | 10000.00 | 0.00 | 대기 /  / 새 신호 대기 |
| v1 | buy_hold | 9978.17 | -21.83 | buy /  / buy_hold: prior completed bar target 100%; next bar open simulation |
| v1 | trend_8_26 | 9978.17 | -21.83 | buy /  / trend_8_26: prior completed bar target 100%; next bar open simulation |
| v1 | momentum_26 | 10000.00 | 0.00 | 대기 /  / 새 신호 대기 |
| v1 | breakout_8 | 10000.00 | 0.00 | 대기 /  / 새 신호 대기 |
| v1 | reversion_12 | 10000.00 | 0.00 | 대기 /  / 새 신호 대기 |
| v1 | volume_26 | 10000.00 | 0.00 | 대기 /  / 새 신호 대기 |
| v1 | trend_8_26 AND momentum_26 | 10000.00 | 0.00 | 대기 /  / 새 신호 대기 |
| v1 | trend_8_26 + momentum_26 | 9989.06 | -10.94 | buy /  / trend_8_26 + momentum_26: prior completed bar target 50%; next bar open simulation |
| v1 | trend_8_26 AND breakout_8 | 10000.00 | 0.00 | 대기 /  / 새 신호 대기 |
| v1 | trend_8_26 + breakout_8 | 9989.06 | -10.94 | buy /  / trend_8_26 + breakout_8: prior completed bar target 50%; next bar open simulation |
| v1 | trend_8_26 AND reversion_12 | 10000.00 | 0.00 | 대기 /  / 새 신호 대기 |
| v1 | trend_8_26 + reversion_12 | 9989.06 | -10.94 | buy /  / trend_8_26 + reversion_12: prior completed bar target 50%; next bar open simulation |
| v1 | trend_8_26 AND volume_26 | 10000.00 | 0.00 | 대기 /  / 새 신호 대기 |
| v1 | trend_8_26 + volume_26 | 9989.06 | -10.94 | buy /  / trend_8_26 + volume_26: prior completed bar target 50%; next bar open simulation |
| v1 | momentum_26 AND breakout_8 | 10000.00 | 0.00 | 대기 /  / 새 신호 대기 |
| v1 | momentum_26 + breakout_8 | 10000.00 | 0.00 | 대기 /  / 새 신호 대기 |
| v1 | momentum_26 AND reversion_12 | 10000.00 | 0.00 | 대기 /  / 새 신호 대기 |
| v1 | momentum_26 + reversion_12 | 10000.00 | 0.00 | 대기 /  / 새 신호 대기 |
| v1 | momentum_26 AND volume_26 | 10000.00 | 0.00 | 대기 /  / 새 신호 대기 |
| v1 | momentum_26 + volume_26 | 10000.00 | 0.00 | 대기 /  / 새 신호 대기 |
| v1 | breakout_8 AND reversion_12 | 10000.00 | 0.00 | 대기 /  / 새 신호 대기 |
| v1 | breakout_8 + reversion_12 | 10000.00 | 0.00 | 대기 /  / 새 신호 대기 |
| v1 | breakout_8 AND volume_26 | 10000.00 | 0.00 | 대기 /  / 새 신호 대기 |
| v1 | breakout_8 + volume_26 | 10000.00 | 0.00 | 대기 /  / 새 신호 대기 |
| v1 | reversion_12 AND volume_26 | 10000.00 | 0.00 | 대기 /  / 새 신호 대기 |
| v1 | reversion_12 + volume_26 | 10000.00 | 0.00 | 대기 /  / 새 신호 대기 |
| v2 | cash | 10000.00 | 0.00 | 대기 /  / 새 신호 대기 |
| v2 | buy_hold | 9962.99 | -37.01 | buy / partial / 직전 완료 봉 목표 비중 100%; 다음 봉 시가 가정 |
| v2 | trend_8_26 | 9846.04 | -153.96 | buy / partial / 직전 완료 봉 목표 비중 100%; 다음 봉 시가 가정 |
| v2 | momentum_26 | 9977.84 | -22.16 | sell / filled / 직전 완료 봉 목표 비중 0%; 다음 봉 시가 가정 |
| v2 | breakout_8 | 9924.08 | -75.92 | sell / filled / 직전 완료 봉 목표 비중 0%; 다음 봉 시가 가정 |
| v2 | reversion_12 | 9618.62 | -381.38 | sell / filled / 직전 완료 봉 목표 비중 0%; 다음 봉 시가 가정 |
| v2 | volume_26 | 9738.54 | -261.46 | sell / filled / 직전 완료 봉 목표 비중 0%; 다음 봉 시가 가정 |
| v2 | trend_8_26 AND momentum_26 | 9827.20 | -172.80 | sell / filled / 직전 완료 봉 목표 비중 0%; 다음 봉 시가 가정 |
| v2 | trend_8_26 + momentum_26 | 9911.97 | -88.03 | sell / filled / 직전 완료 봉 목표 비중 50%; 다음 봉 시가 가정 |
| v2 | trend_8_26 AND breakout_8 | 9761.86 | -238.14 | sell / filled / 직전 완료 봉 목표 비중 0%; 다음 봉 시가 가정 |
| v2 | trend_8_26 + breakout_8 | 9905.93 | -94.07 | sell / filled / 직전 완료 봉 목표 비중 50%; 다음 봉 시가 가정 |
| v2 | trend_8_26 AND reversion_12 | 9900.10 | -99.90 | sell / filled / 직전 완료 봉 목표 비중 0%; 다음 봉 시가 가정 |
| v2 | trend_8_26 + reversion_12 | 9731.36 | -268.64 | buy / filled / 직전 완료 봉 목표 비중 50%; 다음 봉 시가 가정 |
| v2 | trend_8_26 AND volume_26 | 10000.00 | 0.00 | 대기 /  / 새 신호 대기 |
| v2 | trend_8_26 + volume_26 | 9812.51 | -187.49 | buy / filled / 직전 완료 봉 목표 비중 50%; 다음 봉 시가 가정 |
| v2 | momentum_26 AND breakout_8 | 9918.93 | -81.07 | sell / filled / 직전 완료 봉 목표 비중 0%; 다음 봉 시가 가정 |
| v2 | momentum_26 + breakout_8 | 9950.96 | -49.04 | sell / filled / 직전 완료 봉 목표 비중 0%; 다음 봉 시가 가정 |
| v2 | momentum_26 AND reversion_12 | 9826.88 | -173.12 | sell / filled / 직전 완료 봉 목표 비중 0%; 다음 봉 시가 가정 |
| v2 | momentum_26 + reversion_12 | 9796.42 | -203.58 | sell / filled / 직전 완료 봉 목표 비중 0%; 다음 봉 시가 가정 |
| v2 | momentum_26 AND volume_26 | 9922.19 | -77.81 | sell / filled / 직전 완료 봉 목표 비중 0%; 다음 봉 시가 가정 |
| v2 | momentum_26 + volume_26 | 9878.11 | -121.89 | sell / filled / 직전 완료 봉 목표 비중 0%; 다음 봉 시가 가정 |
| v2 | breakout_8 AND reversion_12 | 10000.00 | 0.00 | 대기 /  / 새 신호 대기 |
| v2 | breakout_8 + reversion_12 | 9790.56 | -209.44 | sell / filled / 직전 완료 봉 목표 비중 0%; 다음 봉 시가 가정 |
| v2 | breakout_8 AND volume_26 | 9938.59 | -61.41 | sell / filled / 직전 완료 봉 목표 비중 0%; 다음 봉 시가 가정 |
| v2 | breakout_8 + volume_26 | 9831.01 | -168.99 | sell / filled / 직전 완료 봉 목표 비중 0%; 다음 봉 시가 가정 |
| v2 | reversion_12 AND volume_26 | 9762.04 | -237.96 | sell / filled / 직전 완료 봉 목표 비중 0%; 다음 봉 시가 가정 |
| v2 | reversion_12 + volume_26 | 9678.29 | -321.71 | sell / filled / 직전 완료 봉 목표 비중 0%; 다음 봉 시가 가정 |

### 같은 기간의 비용·노출 비교 (사후 연구)

| 전략 | 비용 전 | 비용 후 | 100% 보유 | 같은 평균 노출 보유 | 평균 노출 |
|---|---:|---:|---:|---:|---:|
| cash | 0.00% | 0.00% | 7.73% | 0.00% | 0.00% |
| buy_hold | 8.19% | 7.73% | 7.73% | 7.73% | 100.00% |
| trend_8_26 | 2.82% | -1.00% | 7.73% | 4.47% | 59.10% |
| momentum_26 | 0.82% | -4.54% | 7.73% | 4.37% | 57.78% |
| breakout_8 | 4.86% | -9.86% | 7.73% | 1.60% | 21.64% |
| reversion_12 | -4.05% | -12.52% | 7.73% | 1.74% | 23.48% |
| volume_26 | 4.89% | -3.15% | 7.73% | 0.56% | 7.65% |
| trend_8_26 AND momentum_26 | -0.58% | -5.86% | 7.73% | 3.90% | 51.72% |
| trend_8_26 + momentum_26 | 1.83% | -2.76% | 7.73% | 4.42% | 58.45% |
| trend_8_26 AND breakout_8 | 0.33% | -10.05% | 7.73% | 1.05% | 14.25% |
| trend_8_26 + breakout_8 | 3.86% | -5.11% | 7.73% | 3.02% | 40.38% |
| trend_8_26 AND reversion_12 | -3.39% | -8.52% | 7.73% | 0.52% | 7.12% |
| trend_8_26 + reversion_12 | -0.65% | -6.54% | 7.73% | 3.09% | 41.30% |
| trend_8_26 AND volume_26 | 5.94% | 3.30% | 7.73% | 0.15% | 2.11% |
| trend_8_26 + volume_26 | 3.87% | -1.25% | 7.73% | 2.49% | 33.38% |
| momentum_26 AND breakout_8 | 2.23% | -8.35% | 7.73% | 0.99% | 13.46% |
| momentum_26 + breakout_8 | 2.84% | -6.64% | 7.73% | 2.97% | 39.72% |
| momentum_26 AND reversion_12 | -2.74% | -8.67% | 7.73% | 0.60% | 8.18% |
| momentum_26 + reversion_12 | -1.62% | -8.23% | 7.73% | 3.04% | 40.64% |
| momentum_26 AND volume_26 | 1.47% | -1.88% | 7.73% | 0.19% | 2.64% |
| momentum_26 + volume_26 | 2.87% | -2.41% | 7.73% | 2.44% | 32.72% |
| breakout_8 AND reversion_12 | 0.00% | 0.00% | 7.73% | 0.00% | 0.00% |
| breakout_8 + reversion_12 | 0.33% | -10.63% | 7.73% | 1.67% | 22.57% |
| breakout_8 AND volume_26 | 2.07% | -0.47% | 7.73% | 0.14% | 1.85% |
| breakout_8 + volume_26 | 4.90% | -5.56% | 7.73% | 1.08% | 14.65% |
| reversion_12 AND volume_26 | -2.27% | -5.89% | 7.73% | 0.25% | 3.43% |
| reversion_12 + volume_26 | 0.35% | -7.74% | 7.73% | 1.15% | 15.57% |

동일 구간·초기 자금, 종료 시 청산 비용 포함. 노출 맞춤은 사후 설명용이며 v2 실제 계좌 성과가 아닙니다.
[낙폭 분해·비용 영향·전체 구간](MSFT/comparison.json)

[v1 전체 기록](MSFT/accounts.json) · [v2 전체 기록](MSFT/accounts-v2.json)

## JPM 계좌

| 모델 | 전략 | 평가액 USD | 손익 USD | 최근 매매·이유 |
|---|---|---:|---:|---|
| v1 | cash | 10000.00 | 0.00 | 대기 /  / 새 신호 대기 |
| v1 | buy_hold | 9965.55 | -34.45 | buy /  / buy_hold: prior completed bar target 100%; next bar open simulation |
| v1 | trend_8_26 | 10000.00 | 0.00 | 대기 /  / 새 신호 대기 |
| v1 | momentum_26 | 9965.55 | -34.45 | buy /  / momentum_26: prior completed bar target 100%; next bar open simulation |
| v1 | breakout_8 | 10000.00 | 0.00 | 대기 /  / 새 신호 대기 |
| v1 | reversion_12 | 10000.00 | 0.00 | 대기 /  / 새 신호 대기 |
| v1 | volume_26 | 10000.00 | 0.00 | 대기 /  / 새 신호 대기 |
| v1 | trend_8_26 AND momentum_26 | 10000.00 | 0.00 | 대기 /  / 새 신호 대기 |
| v1 | trend_8_26 + momentum_26 | 9982.74 | -17.26 | buy /  / trend_8_26 + momentum_26: prior completed bar target 50%; next bar open simulation |
| v1 | trend_8_26 AND breakout_8 | 10000.00 | 0.00 | 대기 /  / 새 신호 대기 |
| v1 | trend_8_26 + breakout_8 | 10000.00 | 0.00 | 대기 /  / 새 신호 대기 |
| v1 | trend_8_26 AND reversion_12 | 10000.00 | 0.00 | 대기 /  / 새 신호 대기 |
| v1 | trend_8_26 + reversion_12 | 10000.00 | 0.00 | 대기 /  / 새 신호 대기 |
| v1 | trend_8_26 AND volume_26 | 10000.00 | 0.00 | 대기 /  / 새 신호 대기 |
| v1 | trend_8_26 + volume_26 | 10000.00 | 0.00 | 대기 /  / 새 신호 대기 |
| v1 | momentum_26 AND breakout_8 | 10000.00 | 0.00 | 대기 /  / 새 신호 대기 |
| v1 | momentum_26 + breakout_8 | 9982.74 | -17.26 | buy /  / momentum_26 + breakout_8: prior completed bar target 50%; next bar open simulation |
| v1 | momentum_26 AND reversion_12 | 10000.00 | 0.00 | 대기 /  / 새 신호 대기 |
| v1 | momentum_26 + reversion_12 | 9982.74 | -17.26 | buy /  / momentum_26 + reversion_12: prior completed bar target 50%; next bar open simulation |
| v1 | momentum_26 AND volume_26 | 10000.00 | 0.00 | 대기 /  / 새 신호 대기 |
| v1 | momentum_26 + volume_26 | 9982.74 | -17.26 | buy /  / momentum_26 + volume_26: prior completed bar target 50%; next bar open simulation |
| v1 | breakout_8 AND reversion_12 | 10000.00 | 0.00 | 대기 /  / 새 신호 대기 |
| v1 | breakout_8 + reversion_12 | 10000.00 | 0.00 | 대기 /  / 새 신호 대기 |
| v1 | breakout_8 AND volume_26 | 10000.00 | 0.00 | 대기 /  / 새 신호 대기 |
| v1 | breakout_8 + volume_26 | 10000.00 | 0.00 | 대기 /  / 새 신호 대기 |
| v1 | reversion_12 AND volume_26 | 10000.00 | 0.00 | 대기 /  / 새 신호 대기 |
| v1 | reversion_12 + volume_26 | 10000.00 | 0.00 | 대기 /  / 새 신호 대기 |
| v2 | cash | 10000.00 | 0.00 | 대기 /  / 새 신호 대기 |
| v2 | buy_hold | 9961.12 | -38.88 | buy / partial / 직전 완료 봉 목표 비중 100%; 다음 봉 시가 가정 |
| v2 | trend_8_26 | 9914.72 | -85.28 | sell / filled / 직전 완료 봉 목표 비중 0%; 다음 봉 시가 가정 |
| v2 | momentum_26 | 9519.16 | -480.84 | buy / partial / 직전 완료 봉 목표 비중 100%; 다음 봉 시가 가정 |
| v2 | breakout_8 | 9426.01 | -573.99 | sell / filled / 직전 완료 봉 목표 비중 0%; 다음 봉 시가 가정 |
| v2 | reversion_12 | 10045.54 | 45.54 | sell / filled / 직전 완료 봉 목표 비중 0%; 다음 봉 시가 가정 |
| v2 | volume_26 | 9826.70 | -173.30 | sell / filled / 직전 완료 봉 목표 비중 0%; 다음 봉 시가 가정 |
| v2 | trend_8_26 AND momentum_26 | 9936.83 | -63.17 | sell / filled / 직전 완료 봉 목표 비중 0%; 다음 봉 시가 가정 |
| v2 | trend_8_26 + momentum_26 | 9715.46 | -284.54 | sell / filled / 직전 완료 봉 목표 비중 50%; 다음 봉 시가 가정 |
| v2 | trend_8_26 AND breakout_8 | 9420.50 | -579.50 | sell / filled / 직전 완료 봉 목표 비중 0%; 다음 봉 시가 가정 |
| v2 | trend_8_26 + breakout_8 | 9667.89 | -332.11 | sell / filled / 직전 완료 봉 목표 비중 0%; 다음 봉 시가 가정 |
| v2 | trend_8_26 AND reversion_12 | 9981.61 | -18.39 | sell / filled / 직전 완료 봉 목표 비중 0%; 다음 봉 시가 가정 |
| v2 | trend_8_26 + reversion_12 | 9980.03 | -19.97 | sell / filled / 직전 완료 봉 목표 비중 0%; 다음 봉 시가 가정 |
| v2 | trend_8_26 AND volume_26 | 9800.30 | -199.70 | sell / filled / 직전 완료 봉 목표 비중 0%; 다음 봉 시가 가정 |
| v2 | trend_8_26 + volume_26 | 9871.13 | -128.87 | sell / filled / 직전 완료 봉 목표 비중 0%; 다음 봉 시가 가정 |
| v2 | momentum_26 AND breakout_8 | 9407.17 | -592.83 | sell / filled / 직전 완료 봉 목표 비중 0%; 다음 봉 시가 가정 |
| v2 | momentum_26 + breakout_8 | 9493.59 | -506.41 | buy / filled / 직전 완료 봉 목표 비중 50%; 다음 봉 시가 가정 |
| v2 | momentum_26 AND reversion_12 | 9950.76 | -49.24 | sell / filled / 직전 완료 봉 목표 비중 0%; 다음 봉 시가 가정 |
| v2 | momentum_26 + reversion_12 | 9841.07 | -158.93 | buy / filled / 직전 완료 봉 목표 비중 50%; 다음 봉 시가 가정 |
| v2 | momentum_26 AND volume_26 | 9800.30 | -199.70 | sell / filled / 직전 완료 봉 목표 비중 0%; 다음 봉 시가 가정 |
| v2 | momentum_26 + volume_26 | 9733.81 | -266.19 | buy / filled / 직전 완료 봉 목표 비중 50%; 다음 봉 시가 가정 |
| v2 | breakout_8 AND reversion_12 | 10000.00 | 0.00 | 대기 /  / 새 신호 대기 |
| v2 | breakout_8 + reversion_12 | 9751.59 | -248.41 | sell / filled / 직전 완료 봉 목표 비중 0%; 다음 봉 시가 가정 |
| v2 | breakout_8 AND volume_26 | 9893.34 | -106.66 | sell / filled / 직전 완료 봉 목표 비중 0%; 다음 봉 시가 가정 |
| v2 | breakout_8 + volume_26 | 9644.69 | -355.31 | sell / filled / 직전 완료 봉 목표 비중 0%; 다음 봉 시가 가정 |
| v2 | reversion_12 AND volume_26 | 10051.38 | 51.38 | sell / filled / 직전 완료 봉 목표 비중 0%; 다음 봉 시가 가정 |
| v2 | reversion_12 + volume_26 | 9956.73 | -43.27 | sell / filled / 직전 완료 봉 목표 비중 0%; 다음 봉 시가 가정 |

### 같은 기간의 비용·노출 비교 (사후 연구)

| 전략 | 비용 전 | 비용 후 | 100% 보유 | 같은 평균 노출 보유 | 평균 노출 |
|---|---:|---:|---:|---:|---:|
| cash | 0.00% | 0.00% | -1.50% | -0.00% | 0.00% |
| buy_hold | -1.09% | -1.50% | -1.50% | -1.50% | 100.00% |
| trend_8_26 | 0.50% | -2.41% | -1.50% | -0.82% | 54.09% |
| momentum_26 | -1.88% | -7.48% | -1.50% | -0.71% | 46.97% |
| breakout_8 | -3.35% | -17.61% | -1.50% | -0.30% | 19.53% |
| reversion_12 | 4.31% | -9.19% | -1.50% | -0.40% | 26.12% |
| volume_26 | -0.72% | -6.78% | -1.50% | -0.10% | 6.86% |
| trend_8_26 AND momentum_26 | 1.03% | -2.71% | -1.50% | -0.64% | 42.48% |
| trend_8_26 + momentum_26 | -0.69% | -4.97% | -1.50% | -0.76% | 50.53% |
| trend_8_26 AND breakout_8 | -3.43% | -13.42% | -1.50% | -0.19% | 12.40% |
| trend_8_26 + breakout_8 | -1.43% | -10.13% | -1.50% | -0.56% | 36.81% |
| trend_8_26 AND reversion_12 | 2.82% | -3.46% | -1.50% | -0.10% | 6.60% |
| trend_8_26 + reversion_12 | 2.41% | -5.67% | -1.50% | -0.61% | 40.11% |
| trend_8_26 AND volume_26 | -1.19% | -5.26% | -1.50% | -0.06% | 4.22% |
| trend_8_26 + volume_26 | -0.10% | -4.62% | -1.50% | -0.46% | 30.48% |
| momentum_26 AND breakout_8 | -2.23% | -11.98% | -1.50% | -0.18% | 11.87% |
| momentum_26 + breakout_8 | -2.60% | -12.49% | -1.50% | -0.50% | 33.25% |
| momentum_26 AND reversion_12 | 2.89% | -3.80% | -1.50% | -0.08% | 5.54% |
| momentum_26 + reversion_12 | 1.19% | -7.37% | -1.50% | -0.55% | 36.55% |
| momentum_26 AND volume_26 | -0.41% | -3.30% | -1.50% | -0.04% | 2.90% |
| momentum_26 + volume_26 | -1.28% | -6.54% | -1.50% | -0.41% | 26.92% |
| breakout_8 AND reversion_12 | 0.00% | 0.00% | -1.50% | -0.00% | 0.00% |
| breakout_8 + reversion_12 | 0.43% | -12.22% | -1.50% | -0.35% | 22.83% |
| breakout_8 AND volume_26 | -1.13% | -2.78% | -1.50% | -0.02% | 1.06% |
| breakout_8 + volume_26 | -2.03% | -11.25% | -1.50% | -0.20% | 13.20% |
| reversion_12 AND volume_26 | 1.25% | -2.10% | -1.50% | -0.05% | 3.43% |
| reversion_12 + volume_26 | 1.78% | -7.22% | -1.50% | -0.25% | 16.50% |

동일 구간·초기 자금, 종료 시 청산 비용 포함. 노출 맞춤은 사후 설명용이며 v2 실제 계좌 성과가 아닙니다.
[낙폭 분해·비용 영향·전체 구간](JPM/comparison.json)

[v1 전체 기록](JPM/accounts.json) · [v2 전체 기록](JPM/accounts-v2.json)

## XOM 계좌

| 모델 | 전략 | 평가액 USD | 손익 USD | 최근 매매·이유 |
|---|---|---:|---:|---|
| v1 | cash | 10000.00 | 0.00 | 대기 /  / 새 신호 대기 |
| v1 | buy_hold | 9962.95 | -37.05 | buy /  / buy_hold: prior completed bar target 100%; next bar open simulation |
| v1 | trend_8_26 | 10000.00 | 0.00 | 대기 /  / 새 신호 대기 |
| v1 | momentum_26 | 10000.00 | 0.00 | 대기 /  / 새 신호 대기 |
| v1 | breakout_8 | 10000.00 | 0.00 | 대기 /  / 새 신호 대기 |
| v1 | reversion_12 | 10000.00 | 0.00 | 대기 /  / 새 신호 대기 |
| v1 | volume_26 | 10000.00 | 0.00 | 대기 /  / 새 신호 대기 |
| v1 | trend_8_26 AND momentum_26 | 10000.00 | 0.00 | 대기 /  / 새 신호 대기 |
| v1 | trend_8_26 + momentum_26 | 10000.00 | 0.00 | 대기 /  / 새 신호 대기 |
| v1 | trend_8_26 AND breakout_8 | 10000.00 | 0.00 | 대기 /  / 새 신호 대기 |
| v1 | trend_8_26 + breakout_8 | 10000.00 | 0.00 | 대기 /  / 새 신호 대기 |
| v1 | trend_8_26 AND reversion_12 | 10000.00 | 0.00 | 대기 /  / 새 신호 대기 |
| v1 | trend_8_26 + reversion_12 | 10000.00 | 0.00 | 대기 /  / 새 신호 대기 |
| v1 | trend_8_26 AND volume_26 | 10000.00 | 0.00 | 대기 /  / 새 신호 대기 |
| v1 | trend_8_26 + volume_26 | 10000.00 | 0.00 | 대기 /  / 새 신호 대기 |
| v1 | momentum_26 AND breakout_8 | 10000.00 | 0.00 | 대기 /  / 새 신호 대기 |
| v1 | momentum_26 + breakout_8 | 10000.00 | 0.00 | 대기 /  / 새 신호 대기 |
| v1 | momentum_26 AND reversion_12 | 10000.00 | 0.00 | 대기 /  / 새 신호 대기 |
| v1 | momentum_26 + reversion_12 | 10000.00 | 0.00 | 대기 /  / 새 신호 대기 |
| v1 | momentum_26 AND volume_26 | 10000.00 | 0.00 | 대기 /  / 새 신호 대기 |
| v1 | momentum_26 + volume_26 | 10000.00 | 0.00 | 대기 /  / 새 신호 대기 |
| v1 | breakout_8 AND reversion_12 | 10000.00 | 0.00 | 대기 /  / 새 신호 대기 |
| v1 | breakout_8 + reversion_12 | 10000.00 | 0.00 | 대기 /  / 새 신호 대기 |
| v1 | breakout_8 AND volume_26 | 10000.00 | 0.00 | 대기 /  / 새 신호 대기 |
| v1 | breakout_8 + volume_26 | 10000.00 | 0.00 | 대기 /  / 새 신호 대기 |
| v1 | reversion_12 AND volume_26 | 10000.00 | 0.00 | 대기 /  / 새 신호 대기 |
| v1 | reversion_12 + volume_26 | 10000.00 | 0.00 | 대기 /  / 새 신호 대기 |
| v2 | cash | 10000.00 | 0.00 | 대기 /  / 새 신호 대기 |
| v2 | buy_hold | 10211.86 | 211.86 | buy / partial / 직전 완료 봉 목표 비중 100%; 다음 봉 시가 가정 |
| v2 | trend_8_26 | 10096.25 | 96.25 | sell / filled / 직전 완료 봉 목표 비중 0%; 다음 봉 시가 가정 |
| v2 | momentum_26 | 10172.64 | 172.64 | sell / filled / 직전 완료 봉 목표 비중 0%; 다음 봉 시가 가정 |
| v2 | breakout_8 | 9471.02 | -528.98 | sell / filled / 직전 완료 봉 목표 비중 0%; 다음 봉 시가 가정 |
| v2 | reversion_12 | 9834.10 | -165.90 | sell / filled / 직전 완료 봉 목표 비중 0%; 다음 봉 시가 가정 |
| v2 | volume_26 | 9908.04 | -91.96 | sell / filled / 직전 완료 봉 목표 비중 0%; 다음 봉 시가 가정 |
| v2 | trend_8_26 AND momentum_26 | 10103.74 | 103.74 | sell / filled / 직전 완료 봉 목표 비중 0%; 다음 봉 시가 가정 |
| v2 | trend_8_26 + momentum_26 | 10134.41 | 134.41 | sell / filled / 직전 완료 봉 목표 비중 0%; 다음 봉 시가 가정 |
| v2 | trend_8_26 AND breakout_8 | 9453.73 | -546.27 | sell / filled / 직전 완료 봉 목표 비중 0%; 다음 봉 시가 가정 |
| v2 | trend_8_26 + breakout_8 | 9799.57 | -200.43 | sell / filled / 직전 완료 봉 목표 비중 0%; 다음 봉 시가 가정 |
| v2 | trend_8_26 AND reversion_12 | 9839.70 | -160.30 | sell / filled / 직전 완료 봉 목표 비중 0%; 다음 봉 시가 가정 |
| v2 | trend_8_26 + reversion_12 | 9964.30 | -35.70 | sell / filled / 직전 완료 봉 목표 비중 0%; 다음 봉 시가 가정 |
| v2 | trend_8_26 AND volume_26 | 9895.61 | -104.39 | sell / filled / 직전 완료 봉 목표 비중 0%; 다음 봉 시가 가정 |
| v2 | trend_8_26 + volume_26 | 10001.66 | 1.66 | sell / filled / 직전 완료 봉 목표 비중 0%; 다음 봉 시가 가정 |
| v2 | momentum_26 AND breakout_8 | 9471.02 | -528.98 | sell / filled / 직전 완료 봉 목표 비중 0%; 다음 봉 시가 가정 |
| v2 | momentum_26 + breakout_8 | 9816.10 | -183.90 | sell / filled / 직전 완료 봉 목표 비중 0%; 다음 봉 시가 가정 |
| v2 | momentum_26 AND reversion_12 | 9800.13 | -199.87 | sell / filled / 직전 완료 봉 목표 비중 0%; 다음 봉 시가 가정 |
| v2 | momentum_26 + reversion_12 | 10001.96 | 1.96 | sell / filled / 직전 완료 봉 목표 비중 0%; 다음 봉 시가 가정 |
| v2 | momentum_26 AND volume_26 | 9957.96 | -42.04 | sell / filled / 직전 완료 봉 목표 비중 0%; 다음 봉 시가 가정 |
| v2 | momentum_26 + volume_26 | 10060.52 | 60.52 | sell / filled / 직전 완료 봉 목표 비중 0%; 다음 봉 시가 가정 |
| v2 | breakout_8 AND reversion_12 | 10000.00 | 0.00 | 대기 /  / 새 신호 대기 |
| v2 | breakout_8 + reversion_12 | 9650.66 | -349.34 | sell / filled / 직전 완료 봉 목표 비중 0%; 다음 봉 시가 가정 |
| v2 | breakout_8 AND volume_26 | 9970.25 | -29.75 | sell / filled / 직전 완료 봉 목표 비중 0%; 다음 봉 시가 가정 |
| v2 | breakout_8 + volume_26 | 9707.34 | -292.66 | sell / filled / 직전 완료 봉 목표 비중 0%; 다음 봉 시가 가정 |
| v2 | reversion_12 AND volume_26 | 9949.87 | -50.13 | sell / filled / 직전 완료 봉 목표 비중 0%; 다음 봉 시가 가정 |
| v2 | reversion_12 + volume_26 | 9870.90 | -129.10 | sell / filled / 직전 완료 봉 목표 비중 0%; 다음 봉 시가 가정 |

### 같은 기간의 비용·노출 비교 (사후 연구)

| 전략 | 비용 전 | 비용 후 | 100% 보유 | 같은 평균 노출 보유 | 평균 노출 |
|---|---:|---:|---:|---:|---:|
| cash | 0.00% | 0.00% | 7.65% | 0.00% | 0.00% |
| buy_hold | 8.10% | 7.65% | 7.65% | 7.65% | 100.00% |
| trend_8_26 | 1.00% | -3.16% | 7.65% | 4.78% | 63.06% |
| momentum_26 | -0.71% | -7.94% | 7.65% | 5.35% | 70.45% |
| breakout_8 | -3.59% | -20.53% | 7.65% | 1.72% | 22.96% |
| reversion_12 | 5.59% | -4.53% | 7.65% | 1.62% | 21.64% |
| volume_26 | 4.95% | -2.69% | 7.65% | 0.37% | 5.01% |
| trend_8_26 AND momentum_26 | -0.45% | -4.95% | 7.65% | 4.37% | 57.78% |
| trend_8_26 + momentum_26 | 0.15% | -5.37% | 7.65% | 5.06% | 66.76% |
| trend_8_26 AND breakout_8 | -1.20% | -14.70% | 7.65% | 1.34% | 17.94% |
| trend_8_26 + breakout_8 | -1.30% | -12.07% | 7.65% | 3.24% | 43.02% |
| trend_8_26 AND reversion_12 | 1.89% | -3.93% | 7.65% | 0.61% | 8.18% |
| trend_8_26 + reversion_12 | 3.29% | -3.64% | 7.65% | 3.19% | 42.35% |
| trend_8_26 AND volume_26 | 2.54% | -1.67% | 7.65% | 0.20% | 2.64% |
| trend_8_26 + volume_26 | 2.97% | -2.52% | 7.65% | 2.56% | 34.04% |
| momentum_26 AND breakout_8 | -3.06% | -18.40% | 7.65% | 1.54% | 20.58% |
| momentum_26 + breakout_8 | -2.13% | -14.45% | 7.65% | 3.52% | 46.71% |
| momentum_26 AND reversion_12 | 2.43% | -4.63% | 7.65% | 0.73% | 9.76% |
| momentum_26 + reversion_12 | 2.42% | -4.66% | 7.65% | 3.47% | 46.05% |
| momentum_26 AND volume_26 | 2.42% | -1.79% | 7.65% | 0.20% | 2.64% |
| momentum_26 + volume_26 | 2.11% | -3.95% | 7.65% | 2.84% | 37.73% |
| breakout_8 AND reversion_12 | 0.00% | 0.00% | 7.65% | 0.00% | 0.00% |
| breakout_8 + reversion_12 | 0.91% | -12.53% | 7.65% | 1.67% | 22.30% |
| breakout_8 AND volume_26 | 0.60% | -0.66% | 7.65% | 0.06% | 0.79% |
| breakout_8 + volume_26 | 0.60% | -10.94% | 7.65% | 1.05% | 13.99% |
| reversion_12 AND volume_26 | 1.84% | -1.11% | 7.65% | 0.14% | 1.85% |
| reversion_12 + volume_26 | 5.28% | -3.01% | 7.65% | 1.00% | 13.33% |

동일 구간·초기 자금, 종료 시 청산 비용 포함. 노출 맞춤은 사후 설명용이며 v2 실제 계좌 성과가 아닙니다.
[낙폭 분해·비용 영향·전체 구간](XOM/comparison.json)

[v1 전체 기록](XOM/accounts.json) · [v2 전체 기록](XOM/accounts-v2.json)

## JNJ 계좌

| 모델 | 전략 | 평가액 USD | 손익 USD | 최근 매매·이유 |
|---|---|---:|---:|---|
| v1 | cash | 10000.00 | 0.00 | 대기 /  / 새 신호 대기 |
| v1 | buy_hold | 9994.69 | -5.31 | buy /  / buy_hold: prior completed bar target 100%; next bar open simulation |
| v1 | trend_8_26 | 9994.69 | -5.31 | buy /  / trend_8_26: prior completed bar target 100%; next bar open simulation |
| v1 | momentum_26 | 9994.69 | -5.31 | buy /  / momentum_26: prior completed bar target 100%; next bar open simulation |
| v1 | breakout_8 | 10000.00 | 0.00 | 대기 /  / 새 신호 대기 |
| v1 | reversion_12 | 10000.00 | 0.00 | 대기 /  / 새 신호 대기 |
| v1 | volume_26 | 10000.00 | 0.00 | 대기 /  / 새 신호 대기 |
| v1 | trend_8_26 AND momentum_26 | 9994.69 | -5.31 | buy /  / trend_8_26 AND momentum_26: prior completed bar target 100%; next bar open simulation |
| v1 | trend_8_26 + momentum_26 | 9994.69 | -5.31 | buy /  / trend_8_26 + momentum_26: prior completed bar target 100%; next bar open simulation |
| v1 | trend_8_26 AND breakout_8 | 10000.00 | 0.00 | 대기 /  / 새 신호 대기 |
| v1 | trend_8_26 + breakout_8 | 9997.34 | -2.66 | buy /  / trend_8_26 + breakout_8: prior completed bar target 50%; next bar open simulation |
| v1 | trend_8_26 AND reversion_12 | 10000.00 | 0.00 | 대기 /  / 새 신호 대기 |
| v1 | trend_8_26 + reversion_12 | 9997.34 | -2.66 | buy /  / trend_8_26 + reversion_12: prior completed bar target 50%; next bar open simulation |
| v1 | trend_8_26 AND volume_26 | 10000.00 | 0.00 | 대기 /  / 새 신호 대기 |
| v1 | trend_8_26 + volume_26 | 9997.34 | -2.66 | buy /  / trend_8_26 + volume_26: prior completed bar target 50%; next bar open simulation |
| v1 | momentum_26 AND breakout_8 | 10000.00 | 0.00 | 대기 /  / 새 신호 대기 |
| v1 | momentum_26 + breakout_8 | 9997.34 | -2.66 | buy /  / momentum_26 + breakout_8: prior completed bar target 50%; next bar open simulation |
| v1 | momentum_26 AND reversion_12 | 10000.00 | 0.00 | 대기 /  / 새 신호 대기 |
| v1 | momentum_26 + reversion_12 | 9997.34 | -2.66 | buy /  / momentum_26 + reversion_12: prior completed bar target 50%; next bar open simulation |
| v1 | momentum_26 AND volume_26 | 10000.00 | 0.00 | 대기 /  / 새 신호 대기 |
| v1 | momentum_26 + volume_26 | 9997.34 | -2.66 | buy /  / momentum_26 + volume_26: prior completed bar target 50%; next bar open simulation |
| v1 | breakout_8 AND reversion_12 | 10000.00 | 0.00 | 대기 /  / 새 신호 대기 |
| v1 | breakout_8 + reversion_12 | 10000.00 | 0.00 | 대기 /  / 새 신호 대기 |
| v1 | breakout_8 AND volume_26 | 10000.00 | 0.00 | 대기 /  / 새 신호 대기 |
| v1 | breakout_8 + volume_26 | 10000.00 | 0.00 | 대기 /  / 새 신호 대기 |
| v1 | reversion_12 AND volume_26 | 10000.00 | 0.00 | 대기 /  / 새 신호 대기 |
| v1 | reversion_12 + volume_26 | 10000.00 | 0.00 | 대기 /  / 새 신호 대기 |
| v2 | cash | 10000.00 | 0.00 | 대기 /  / 새 신호 대기 |
| v2 | buy_hold | 9881.76 | -118.24 | 중단: 손실 한도 / buy / partial / 직전 완료 봉 목표 비중 100%; 다음 봉 시가 가정 |
| v2 | trend_8_26 | 9881.76 | -118.24 | 중단: 손실 한도 / buy / partial / 직전 완료 봉 목표 비중 100%; 다음 봉 시가 가정 |
| v2 | momentum_26 | 9881.76 | -118.24 | 중단: 손실 한도 / buy / partial / 직전 완료 봉 목표 비중 100%; 다음 봉 시가 가정 |
| v2 | breakout_8 | 9343.39 | -656.61 | 중단: 손실 한도 / sell / filled / 직전 완료 봉 목표 비중 0%; 다음 봉 시가 가정 |
| v2 | reversion_12 | 9887.49 | -112.51 | sell / filled / 직전 완료 봉 목표 비중 0%; 다음 봉 시가 가정 |
| v2 | volume_26 | 9791.36 | -208.64 | sell / filled / 직전 완료 봉 목표 비중 0%; 다음 봉 시가 가정 |
| v2 | trend_8_26 AND momentum_26 | 9881.76 | -118.24 | 중단: 손실 한도 / buy / partial / 직전 완료 봉 목표 비중 100%; 다음 봉 시가 가정 |
| v2 | trend_8_26 + momentum_26 | 9881.76 | -118.24 | 중단: 손실 한도 / buy / partial / 직전 완료 봉 목표 비중 100%; 다음 봉 시가 가정 |
| v2 | trend_8_26 AND breakout_8 | 9419.39 | -580.61 | 중단: 손실 한도 / sell / filled / 직전 완료 봉 목표 비중 0%; 다음 봉 시가 가정 |
| v2 | trend_8_26 + breakout_8 | 9666.24 | -333.76 | sell / filled / 직전 완료 봉 목표 비중 50%; 다음 봉 시가 가정 |
| v2 | trend_8_26 AND reversion_12 | 10134.68 | 134.68 | sell / filled / 직전 완료 봉 목표 비중 0%; 다음 봉 시가 가정 |
| v2 | trend_8_26 + reversion_12 | 9732.92 | -267.08 | 중단: 손실 한도 / sell / filled / 직전 완료 봉 목표 비중 0%; 다음 봉 시가 가정 |
| v2 | trend_8_26 AND volume_26 | 9870.71 | -129.29 | sell / filled / 직전 완료 봉 목표 비중 0%; 다음 봉 시가 가정 |
| v2 | trend_8_26 + volume_26 | 9915.80 | -84.20 | 중단: 손실 한도 / buy / filled / 직전 완료 봉 목표 비중 50%; 다음 봉 시가 가정 |
| v2 | momentum_26 AND breakout_8 | 9598.70 | -401.30 | sell / filled / 직전 완료 봉 목표 비중 0%; 다음 봉 시가 가정 |
| v2 | momentum_26 + breakout_8 | 9668.64 | -331.36 | sell / filled / 직전 완료 봉 목표 비중 50%; 다음 봉 시가 가정 |
| v2 | momentum_26 AND reversion_12 | 10134.68 | 134.68 | sell / filled / 직전 완료 봉 목표 비중 0%; 다음 봉 시가 가정 |
| v2 | momentum_26 + reversion_12 | 9732.92 | -267.08 | 중단: 손실 한도 / sell / filled / 직전 완료 봉 목표 비중 0%; 다음 봉 시가 가정 |
| v2 | momentum_26 AND volume_26 | 9920.93 | -79.07 | sell / filled / 직전 완료 봉 목표 비중 0%; 다음 봉 시가 가정 |
| v2 | momentum_26 + volume_26 | 9915.80 | -84.20 | 중단: 손실 한도 / buy / filled / 직전 완료 봉 목표 비중 50%; 다음 봉 시가 가정 |
| v2 | breakout_8 AND reversion_12 | 10000.00 | 0.00 | 대기 /  / 새 신호 대기 |
| v2 | breakout_8 + reversion_12 | 9678.21 | -321.79 | sell / filled / 직전 완료 봉 목표 비중 0%; 다음 봉 시가 가정 |
| v2 | breakout_8 AND volume_26 | 9814.17 | -185.83 | sell / filled / 직전 완료 봉 목표 비중 0%; 다음 봉 시가 가정 |
| v2 | breakout_8 + volume_26 | 9610.69 | -389.31 | sell / filled / 직전 완료 봉 목표 비중 0%; 다음 봉 시가 가정 |
| v2 | reversion_12 AND volume_26 | 9886.24 | -113.76 | sell / filled / 직전 완료 봉 목표 비중 0%; 다음 봉 시가 가정 |
| v2 | reversion_12 + volume_26 | 9860.31 | -139.69 | sell / filled / 직전 완료 봉 목표 비중 0%; 다음 봉 시가 가정 |

### 같은 기간의 비용·노출 비교 (사후 연구)

| 전략 | 비용 전 | 비용 후 | 100% 보유 | 같은 평균 노출 보유 | 평균 노출 |
|---|---:|---:|---:|---:|---:|
| cash | 0.00% | 0.00% | -5.19% | -0.00% | 0.00% |
| buy_hold | -4.79% | -5.19% | -5.19% | -5.19% | 100.00% |
| trend_8_26 | 4.20% | 1.61% | -5.19% | -2.51% | 47.23% |
| momentum_26 | 1.72% | -2.05% | -5.19% | -2.47% | 46.44% |
| breakout_8 | -0.45% | -17.59% | -5.19% | -1.17% | 21.64% |
| reversion_12 | -6.50% | -15.47% | -5.19% | -1.56% | 29.02% |
| volume_26 | -1.33% | -8.13% | -5.19% | -0.37% | 6.86% |
| trend_8_26 AND momentum_26 | 4.05% | 0.61% | -5.19% | -2.31% | 43.27% |
| trend_8_26 + momentum_26 | 2.96% | -0.23% | -5.19% | -2.49% | 46.84% |
| trend_8_26 AND breakout_8 | 0.60% | -12.42% | -5.19% | -0.86% | 15.83% |
| trend_8_26 + breakout_8 | 1.88% | -8.28% | -5.19% | -1.84% | 34.44% |
| trend_8_26 AND reversion_12 | 1.85% | -1.10% | -5.19% | -0.23% | 4.22% |
| trend_8_26 + reversion_12 | -1.26% | -6.73% | -5.19% | -2.04% | 38.13% |
| trend_8_26 AND volume_26 | 1.59% | -0.53% | -5.19% | -0.09% | 1.58% |
| trend_8_26 + volume_26 | 1.43% | -2.76% | -5.19% | -1.45% | 27.05% |
| momentum_26 AND breakout_8 | 2.02% | -10.44% | -5.19% | -0.81% | 15.04% |
| momentum_26 + breakout_8 | 0.66% | -9.95% | -5.19% | -1.82% | 34.04% |
| momentum_26 AND reversion_12 | 0.24% | -3.07% | -5.19% | -0.27% | 5.01% |
| momentum_26 + reversion_12 | -2.45% | -8.43% | -5.19% | -2.02% | 37.74% |
| momentum_26 AND volume_26 | 0.88% | -1.21% | -5.19% | -0.09% | 1.58% |
| momentum_26 + volume_26 | 0.22% | -4.53% | -5.19% | -1.43% | 26.65% |
| breakout_8 AND reversion_12 | 0.00% | 0.00% | -5.19% | -0.00% | 0.00% |
| breakout_8 + reversion_12 | -3.50% | -16.01% | -5.19% | -1.36% | 25.34% |
| breakout_8 AND volume_26 | -0.11% | -2.19% | -5.19% | -0.09% | 1.58% |
| breakout_8 + volume_26 | -0.88% | -12.26% | -5.19% | -0.77% | 14.26% |
| reversion_12 AND volume_26 | -2.65% | -5.47% | -5.19% | -0.16% | 2.90% |
| reversion_12 + volume_26 | -3.94% | -11.13% | -5.19% | -0.97% | 17.95% |

동일 구간·초기 자금, 종료 시 청산 비용 포함. 노출 맞춤은 사후 설명용이며 v2 실제 계좌 성과가 아닙니다.
[낙폭 분해·비용 영향·전체 구간](JNJ/comparison.json)

[v1 전체 기록](JNJ/accounts.json) · [v2 전체 기록](JNJ/accounts-v2.json)

## CAT 계좌

| 모델 | 전략 | 평가액 USD | 손익 USD | 최근 매매·이유 |
|---|---|---:|---:|---|
| v1 | cash | 10000.00 | 0.00 | 대기 /  / 새 신호 대기 |
| v1 | buy_hold | 9983.72 | -16.28 | buy /  / buy_hold: prior completed bar target 100%; next bar open simulation |
| v1 | trend_8_26 | 10000.00 | 0.00 | 대기 /  / 새 신호 대기 |
| v1 | momentum_26 | 10000.00 | 0.00 | 대기 /  / 새 신호 대기 |
| v1 | breakout_8 | 10000.00 | 0.00 | 대기 /  / 새 신호 대기 |
| v1 | reversion_12 | 10000.00 | 0.00 | 대기 /  / 새 신호 대기 |
| v1 | volume_26 | 9983.72 | -16.28 | buy /  / volume_26: prior completed bar target 100%; next bar open simulation |
| v1 | trend_8_26 AND momentum_26 | 10000.00 | 0.00 | 대기 /  / 새 신호 대기 |
| v1 | trend_8_26 + momentum_26 | 10000.00 | 0.00 | 대기 /  / 새 신호 대기 |
| v1 | trend_8_26 AND breakout_8 | 10000.00 | 0.00 | 대기 /  / 새 신호 대기 |
| v1 | trend_8_26 + breakout_8 | 10000.00 | 0.00 | 대기 /  / 새 신호 대기 |
| v1 | trend_8_26 AND reversion_12 | 10000.00 | 0.00 | 대기 /  / 새 신호 대기 |
| v1 | trend_8_26 + reversion_12 | 10000.00 | 0.00 | 대기 /  / 새 신호 대기 |
| v1 | trend_8_26 AND volume_26 | 10000.00 | 0.00 | 대기 /  / 새 신호 대기 |
| v1 | trend_8_26 + volume_26 | 9991.84 | -8.16 | buy /  / trend_8_26 + volume_26: prior completed bar target 50%; next bar open simulation |
| v1 | momentum_26 AND breakout_8 | 10000.00 | 0.00 | 대기 /  / 새 신호 대기 |
| v1 | momentum_26 + breakout_8 | 10000.00 | 0.00 | 대기 /  / 새 신호 대기 |
| v1 | momentum_26 AND reversion_12 | 10000.00 | 0.00 | 대기 /  / 새 신호 대기 |
| v1 | momentum_26 + reversion_12 | 10000.00 | 0.00 | 대기 /  / 새 신호 대기 |
| v1 | momentum_26 AND volume_26 | 10000.00 | 0.00 | 대기 /  / 새 신호 대기 |
| v1 | momentum_26 + volume_26 | 9991.84 | -8.16 | buy /  / momentum_26 + volume_26: prior completed bar target 50%; next bar open simulation |
| v1 | breakout_8 AND reversion_12 | 10000.00 | 0.00 | 대기 /  / 새 신호 대기 |
| v1 | breakout_8 + reversion_12 | 10000.00 | 0.00 | 대기 /  / 새 신호 대기 |
| v1 | breakout_8 AND volume_26 | 10000.00 | 0.00 | 대기 /  / 새 신호 대기 |
| v1 | breakout_8 + volume_26 | 9991.84 | -8.16 | buy /  / breakout_8 + volume_26: prior completed bar target 50%; next bar open simulation |
| v1 | reversion_12 AND volume_26 | 10000.00 | 0.00 | 대기 /  / 새 신호 대기 |
| v1 | reversion_12 + volume_26 | 9991.84 | -8.16 | buy /  / reversion_12 + volume_26: prior completed bar target 50%; next bar open simulation |
| v2 | cash | 10000.00 | 0.00 | 대기 /  / 새 신호 대기 |
| v2 | buy_hold | 9127.14 | -872.86 | 중단: 손실 한도 / buy / partial / 직전 완료 봉 목표 비중 100%; 다음 봉 시가 가정 |
| v2 | trend_8_26 | 9941.61 | -58.39 | sell / filled / 직전 완료 봉 목표 비중 0%; 다음 봉 시가 가정 |
| v2 | momentum_26 | 10014.59 | 14.59 | sell / filled / 직전 완료 봉 목표 비중 0%; 다음 봉 시가 가정 |
| v2 | breakout_8 | 9806.46 | -193.54 | sell / filled / 직전 완료 봉 목표 비중 0%; 다음 봉 시가 가정 |
| v2 | reversion_12 | 8999.67 | -1000.33 | 중단: 손실 한도 / buy / partial / 직전 완료 봉 목표 비중 100%; 다음 봉 시가 가정 |
| v2 | volume_26 | 9257.05 | -742.95 | 중단: 손실 한도 / buy / partial / 직전 완료 봉 목표 비중 100%; 다음 봉 시가 가정 |
| v2 | trend_8_26 AND momentum_26 | 10043.59 | 43.59 | sell / filled / 직전 완료 봉 목표 비중 0%; 다음 봉 시가 가정 |
| v2 | trend_8_26 + momentum_26 | 9978.08 | -21.92 | sell / filled / 직전 완료 봉 목표 비중 0%; 다음 봉 시가 가정 |
| v2 | trend_8_26 AND breakout_8 | 9976.12 | -23.88 | sell / filled / 직전 완료 봉 목표 비중 0%; 다음 봉 시가 가정 |
| v2 | trend_8_26 + breakout_8 | 9873.91 | -126.09 | sell / filled / 직전 완료 봉 목표 비중 0%; 다음 봉 시가 가정 |
| v2 | trend_8_26 AND reversion_12 | 9815.07 | -184.93 | sell / filled / 직전 완료 봉 목표 비중 0%; 다음 봉 시가 가정 |
| v2 | trend_8_26 + reversion_12 | 9636.65 | -363.35 | sell / filled / 직전 완료 봉 목표 비중 0%; 다음 봉 시가 가정 |
| v2 | trend_8_26 AND volume_26 | 10035.44 | 35.44 | sell / filled / 직전 완료 봉 목표 비중 0%; 다음 봉 시가 가정 |
| v2 | trend_8_26 + volume_26 | 9650.68 | -349.32 | buy / filled / 직전 완료 봉 목표 비중 50%; 다음 봉 시가 가정 |
| v2 | momentum_26 AND breakout_8 | 9977.43 | -22.57 | sell / filled / 직전 완료 봉 목표 비중 0%; 다음 봉 시가 가정 |
| v2 | momentum_26 + breakout_8 | 9910.06 | -89.94 | sell / filled / 직전 완료 봉 목표 비중 0%; 다음 봉 시가 가정 |
| v2 | momentum_26 AND reversion_12 | 9874.73 | -125.27 | sell / filled / 직전 완료 봉 목표 비중 0%; 다음 봉 시가 가정 |
| v2 | momentum_26 + reversion_12 | 9671.92 | -328.08 | sell / filled / 직전 완료 봉 목표 비중 0%; 다음 봉 시가 가정 |
| v2 | momentum_26 AND volume_26 | 10048.78 | 48.78 | sell / filled / 직전 완료 봉 목표 비중 0%; 다음 봉 시가 가정 |
| v2 | momentum_26 + volume_26 | 9706.38 | -293.62 | buy / filled / 직전 완료 봉 목표 비중 50%; 다음 봉 시가 가정 |
| v2 | breakout_8 AND reversion_12 | 10000.00 | 0.00 | 대기 /  / 새 신호 대기 |
| v2 | breakout_8 + reversion_12 | 9610.18 | -389.82 | 중단: 손실 한도 / sell / filled / 직전 완료 봉 목표 비중 0%; 다음 봉 시가 가정 |
| v2 | breakout_8 AND volume_26 | 9998.69 | -1.31 | sell / filled / 직전 완료 봉 목표 비중 0%; 다음 봉 시가 가정 |
| v2 | breakout_8 + volume_26 | 9605.03 | -394.97 | buy / filled / 직전 완료 봉 목표 비중 50%; 다음 봉 시가 가정 |
| v2 | reversion_12 AND volume_26 | 9193.02 | -806.98 | 중단: 손실 한도 / buy / partial / 직전 완료 봉 목표 비중 100%; 다음 봉 시가 가정 |
| v2 | reversion_12 + volume_26 | 9362.26 | -637.74 | 중단: 손실 한도 / sell / filled / 직전 완료 봉 목표 비중 50%; 다음 봉 시가 가정 |

### 같은 기간의 비용·노출 비교 (사후 연구)

| 전략 | 비용 전 | 비용 후 | 100% 보유 | 같은 평균 노출 보유 | 평균 노출 |
|---|---:|---:|---:|---:|---:|
| cash | 0.00% | 0.00% | -9.63% | -0.00% | 0.00% |
| buy_hold | -9.25% | -9.63% | -9.63% | -9.63% | 100.00% |
| trend_8_26 | 0.08% | -3.23% | -9.63% | -5.17% | 53.83% |
| momentum_26 | -4.02% | -9.50% | -9.63% | -4.94% | 51.45% |
| breakout_8 | -3.57% | -16.40% | -9.63% | -1.44% | 15.04% |
| reversion_12 | -4.23% | -15.21% | -9.63% | -2.45% | 25.59% |
| volume_26 | -2.57% | -10.04% | -9.63% | -0.81% | 8.44% |
| trend_8_26 AND momentum_26 | -1.32% | -5.77% | -9.63% | -4.38% | 45.65% |
| trend_8_26 + momentum_26 | -1.97% | -6.40% | -9.63% | -5.05% | 52.64% |
| trend_8_26 AND breakout_8 | -1.46% | -9.02% | -9.63% | -0.76% | 7.92% |
| trend_8_26 + breakout_8 | -1.72% | -9.84% | -9.63% | -3.30% | 34.44% |
| trend_8_26 AND reversion_12 | 0.78% | -5.38% | -9.63% | -0.68% | 7.12% |
| trend_8_26 + reversion_12 | -2.03% | -8.82% | -9.63% | -3.81% | 39.71% |
| trend_8_26 AND volume_26 | 2.63% | -0.76% | -9.63% | -0.28% | 2.90% |
| trend_8_26 + volume_26 | -1.19% | -6.47% | -9.63% | -2.99% | 31.14% |
| momentum_26 AND breakout_8 | -2.95% | -11.51% | -9.63% | -0.88% | 9.23% |
| momentum_26 + breakout_8 | -3.75% | -12.99% | -9.63% | -3.19% | 33.25% |
| momentum_26 AND reversion_12 | -3.04% | -8.96% | -9.63% | -0.56% | 5.80% |
| momentum_26 + reversion_12 | -4.07% | -11.46% | -9.63% | -3.70% | 38.53% |
| momentum_26 AND volume_26 | 1.58% | -0.53% | -9.63% | -0.15% | 1.58% |
| momentum_26 + volume_26 | -3.23% | -8.79% | -9.63% | -2.87% | 29.95% |
| breakout_8 AND reversion_12 | 0.00% | 0.00% | -9.63% | -0.00% | 0.00% |
| breakout_8 + reversion_12 | -3.85% | -14.90% | -9.63% | -1.95% | 20.32% |
| breakout_8 AND volume_26 | 0.78% | -0.48% | -9.63% | -0.08% | 0.79% |
| breakout_8 + volume_26 | -3.04% | -12.53% | -9.63% | -1.12% | 11.75% |
| reversion_12 AND volume_26 | -1.25% | -5.71% | -9.63% | -0.50% | 5.28% |
| reversion_12 + volume_26 | -3.37% | -11.92% | -9.63% | -1.63% | 17.02% |

동일 구간·초기 자금, 종료 시 청산 비용 포함. 노출 맞춤은 사후 설명용이며 v2 실제 계좌 성과가 아닙니다.
[낙폭 분해·비용 영향·전체 구간](CAT/comparison.json)

[v1 전체 기록](CAT/accounts.json) · [v2 전체 기록](CAT/accounts-v2.json)

## WMT 계좌

| 모델 | 전략 | 평가액 USD | 손익 USD | 최근 매매·이유 |
|---|---|---:|---:|---|
| v1 | cash | 10000.00 | 0.00 | 대기 /  / 새 신호 대기 |
| v1 | buy_hold | 9979.20 | -20.80 | buy /  / buy_hold: prior completed bar target 100%; next bar open simulation |
| v1 | trend_8_26 | 9979.20 | -20.80 | buy /  / trend_8_26: prior completed bar target 100%; next bar open simulation |
| v1 | momentum_26 | 9979.20 | -20.80 | buy /  / momentum_26: prior completed bar target 100%; next bar open simulation |
| v1 | breakout_8 | 10000.00 | 0.00 | 대기 /  / 새 신호 대기 |
| v1 | reversion_12 | 10000.00 | 0.00 | 대기 /  / 새 신호 대기 |
| v1 | volume_26 | 10000.00 | 0.00 | 대기 /  / 새 신호 대기 |
| v1 | trend_8_26 AND momentum_26 | 9979.20 | -20.80 | buy /  / trend_8_26 AND momentum_26: prior completed bar target 100%; next bar open simulation |
| v1 | trend_8_26 + momentum_26 | 9979.20 | -20.80 | buy /  / trend_8_26 + momentum_26: prior completed bar target 100%; next bar open simulation |
| v1 | trend_8_26 AND breakout_8 | 10000.00 | 0.00 | 대기 /  / 새 신호 대기 |
| v1 | trend_8_26 + breakout_8 | 9989.58 | -10.42 | buy /  / trend_8_26 + breakout_8: prior completed bar target 50%; next bar open simulation |
| v1 | trend_8_26 AND reversion_12 | 10000.00 | 0.00 | 대기 /  / 새 신호 대기 |
| v1 | trend_8_26 + reversion_12 | 9989.58 | -10.42 | buy /  / trend_8_26 + reversion_12: prior completed bar target 50%; next bar open simulation |
| v1 | trend_8_26 AND volume_26 | 10000.00 | 0.00 | 대기 /  / 새 신호 대기 |
| v1 | trend_8_26 + volume_26 | 9989.58 | -10.42 | buy /  / trend_8_26 + volume_26: prior completed bar target 50%; next bar open simulation |
| v1 | momentum_26 AND breakout_8 | 10000.00 | 0.00 | 대기 /  / 새 신호 대기 |
| v1 | momentum_26 + breakout_8 | 9989.58 | -10.42 | buy /  / momentum_26 + breakout_8: prior completed bar target 50%; next bar open simulation |
| v1 | momentum_26 AND reversion_12 | 10000.00 | 0.00 | 대기 /  / 새 신호 대기 |
| v1 | momentum_26 + reversion_12 | 9989.58 | -10.42 | buy /  / momentum_26 + reversion_12: prior completed bar target 50%; next bar open simulation |
| v1 | momentum_26 AND volume_26 | 10000.00 | 0.00 | 대기 /  / 새 신호 대기 |
| v1 | momentum_26 + volume_26 | 9989.58 | -10.42 | buy /  / momentum_26 + volume_26: prior completed bar target 50%; next bar open simulation |
| v1 | breakout_8 AND reversion_12 | 10000.00 | 0.00 | 대기 /  / 새 신호 대기 |
| v1 | breakout_8 + reversion_12 | 10000.00 | 0.00 | 대기 /  / 새 신호 대기 |
| v1 | breakout_8 AND volume_26 | 10000.00 | 0.00 | 대기 /  / 새 신호 대기 |
| v1 | breakout_8 + volume_26 | 10000.00 | 0.00 | 대기 /  / 새 신호 대기 |
| v1 | reversion_12 AND volume_26 | 10000.00 | 0.00 | 대기 /  / 새 신호 대기 |
| v1 | reversion_12 + volume_26 | 10000.00 | 0.00 | 대기 /  / 새 신호 대기 |
| v2 | cash | 10000.00 | 0.00 | 대기 /  / 새 신호 대기 |
| v2 | buy_hold | 10672.65 | 672.65 | buy / partial / 직전 완료 봉 목표 비중 100%; 다음 봉 시가 가정 |
| v2 | trend_8_26 | 10527.43 | 527.43 | buy / partial / 직전 완료 봉 목표 비중 100%; 다음 봉 시가 가정 |
| v2 | momentum_26 | 10497.23 | 497.23 | buy / partial / 직전 완료 봉 목표 비중 100%; 다음 봉 시가 가정 |
| v2 | breakout_8 | 9964.65 | -35.35 | sell / filled / 직전 완료 봉 목표 비중 0%; 다음 봉 시가 가정 |
| v2 | reversion_12 | 10022.26 | 22.26 | sell / filled / 직전 완료 봉 목표 비중 0%; 다음 봉 시가 가정 |
| v2 | volume_26 | 9965.28 | -34.72 | sell / filled / 직전 완료 봉 목표 비중 0%; 다음 봉 시가 가정 |
| v2 | trend_8_26 AND momentum_26 | 10527.43 | 527.43 | buy / partial / 직전 완료 봉 목표 비중 100%; 다음 봉 시가 가정 |
| v2 | trend_8_26 + momentum_26 | 10512.31 | 512.31 | buy / partial / 직전 완료 봉 목표 비중 100%; 다음 봉 시가 가정 |
| v2 | trend_8_26 AND breakout_8 | 10088.55 | 88.55 | sell / filled / 직전 완료 봉 목표 비중 0%; 다음 봉 시가 가정 |
| v2 | trend_8_26 + breakout_8 | 10242.63 | 242.63 | sell / filled / 직전 완료 봉 목표 비중 50%; 다음 봉 시가 가정 |
| v2 | trend_8_26 AND reversion_12 | 9931.03 | -68.97 | sell / filled / 직전 완료 봉 목표 비중 0%; 다음 봉 시가 가정 |
| v2 | trend_8_26 + reversion_12 | 10273.25 | 273.25 | sell / filled / 직전 완료 봉 목표 비중 50%; 다음 봉 시가 가정 |
| v2 | trend_8_26 AND volume_26 | 9949.23 | -50.77 | sell / filled / 직전 완료 봉 목표 비중 0%; 다음 봉 시가 가정 |
| v2 | trend_8_26 + volume_26 | 10244.01 | 244.01 | sell / filled / 직전 완료 봉 목표 비중 50%; 다음 봉 시가 가정 |
| v2 | momentum_26 AND breakout_8 | 9964.65 | -35.35 | sell / filled / 직전 완료 봉 목표 비중 0%; 다음 봉 시가 가정 |
| v2 | momentum_26 + breakout_8 | 10227.96 | 227.96 | sell / filled / 직전 완료 봉 목표 비중 50%; 다음 봉 시가 가정 |
| v2 | momentum_26 AND reversion_12 | 9940.68 | -59.32 | sell / filled / 직전 완료 봉 목표 비중 0%; 다음 봉 시가 가정 |
| v2 | momentum_26 + reversion_12 | 10301.70 | 301.70 | sell / filled / 직전 완료 봉 목표 비중 50%; 다음 봉 시가 가정 |
| v2 | momentum_26 AND volume_26 | 9913.82 | -86.18 | sell / filled / 직전 완료 봉 목표 비중 0%; 다음 봉 시가 가정 |
| v2 | momentum_26 + volume_26 | 10229.40 | 229.40 | sell / filled / 직전 완료 봉 목표 비중 50%; 다음 봉 시가 가정 |
| v2 | breakout_8 AND reversion_12 | 10000.00 | 0.00 | 대기 /  / 새 신호 대기 |
| v2 | breakout_8 + reversion_12 | 10015.72 | 15.72 | sell / filled / 직전 완료 봉 목표 비중 0%; 다음 봉 시가 가정 |
| v2 | breakout_8 AND volume_26 | 9950.23 | -49.77 | sell / filled / 직전 완료 봉 목표 비중 0%; 다음 봉 시가 가정 |
| v2 | breakout_8 + volume_26 | 9966.35 | -33.65 | sell / filled / 직전 완료 봉 목표 비중 0%; 다음 봉 시가 가정 |
| v2 | reversion_12 AND volume_26 | 10009.78 | 9.78 | sell / filled / 직전 완료 봉 목표 비중 0%; 다음 봉 시가 가정 |
| v2 | reversion_12 + volume_26 | 9993.76 | -6.24 | sell / filled / 직전 완료 봉 목표 비중 0%; 다음 봉 시가 가정 |

### 같은 기간의 비용·노출 비교 (사후 연구)

| 전략 | 비용 전 | 비용 후 | 100% 보유 | 같은 평균 노출 보유 | 평균 노출 |
|---|---:|---:|---:|---:|---:|
| cash | 0.00% | 0.00% | 9.23% | 0.00% | 0.00% |
| buy_hold | 9.69% | 9.23% | 9.23% | 9.23% | 100.00% |
| trend_8_26 | 10.34% | 7.59% | 9.23% | 6.07% | 65.70% |
| momentum_26 | 7.53% | 3.54% | 9.23% | 6.02% | 65.17% |
| breakout_8 | 5.52% | -11.92% | 9.23% | 2.49% | 26.91% |
| reversion_12 | 2.08% | -6.53% | 9.23% | 1.61% | 17.41% |
| volume_26 | -0.17% | -5.87% | 9.23% | 0.56% | 6.07% |
| trend_8_26 AND momentum_26 | 9.86% | 5.78% | 9.23% | 5.53% | 59.89% |
| trend_8_26 + momentum_26 | 8.93% | 5.55% | 9.23% | 6.04% | 65.44% |
| trend_8_26 AND breakout_8 | 6.92% | -6.91% | 9.23% | 2.07% | 22.43% |
| trend_8_26 + breakout_8 | 7.92% | -2.43% | 9.23% | 4.28% | 46.31% |
| trend_8_26 AND reversion_12 | 0.40% | -3.73% | 9.23% | 0.51% | 5.54% |
| trend_8_26 + reversion_12 | 6.17% | 0.50% | 9.23% | 3.84% | 41.56% |
| trend_8_26 AND volume_26 | 1.13% | -1.39% | 9.23% | 0.20% | 2.11% |
| trend_8_26 + volume_26 | 4.99% | 1.07% | 9.23% | 3.32% | 35.89% |
| momentum_26 AND breakout_8 | 5.58% | -8.47% | 9.23% | 2.17% | 23.48% |
| momentum_26 + breakout_8 | 6.54% | -4.29% | 9.23% | 4.25% | 46.05% |
| momentum_26 AND reversion_12 | 0.36% | -3.77% | 9.23% | 0.49% | 5.28% |
| momentum_26 + reversion_12 | 4.82% | 0.27% | 9.23% | 3.82% | 41.30% |
| momentum_26 AND volume_26 | 0.44% | -3.69% | 9.23% | 0.27% | 2.90% |
| momentum_26 + volume_26 | 3.65% | -1.26% | 9.23% | 3.29% | 35.62% |
| breakout_8 AND reversion_12 | 0.00% | 0.00% | 9.23% | 0.00% | 0.00% |
| breakout_8 + reversion_12 | 3.82% | -8.88% | 9.23% | 2.05% | 22.17% |
| breakout_8 AND volume_26 | 0.91% | -1.19% | 9.23% | 0.15% | 1.58% |
| breakout_8 + volume_26 | 2.67% | -8.16% | 9.23% | 1.53% | 16.50% |
| reversion_12 AND volume_26 | -0.11% | -3.00% | 9.23% | 0.27% | 2.90% |
| reversion_12 + volume_26 | 0.96% | -6.00% | 9.23% | 1.09% | 11.75% |

동일 구간·초기 자금, 종료 시 청산 비용 포함. 노출 맞춤은 사후 설명용이며 v2 실제 계좌 성과가 아닙니다.
[낙폭 분해·비용 영향·전체 구간](WMT/comparison.json)

[v1 전체 기록](WMT/accounts.json) · [v2 전체 기록](WMT/accounts-v2.json)
