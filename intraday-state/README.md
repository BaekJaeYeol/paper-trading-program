# 모의투자 운영 현황

최근 확인: 2026-10-15T16:52:00.576665+00:00 (UTC)
다음 15분 확인 목표 (세션 실행 중에만 적용): 2026-10-15T17:07:00+00:00 (UTC, 실행 지연 가능)

실제 주문 없음. v1 기존 계좌와 v2 새 계좌의 시작일이 다르므로 수익률을 직접 우열 비교하지 마세요.
v2는 다음 봉 시가에 비용·스프레드·직전 거래량 제한을 적용한 가상 체결입니다. 미체결 잔량은 만료됩니다.

| 종목 | 상태 | 최근 성공 UTC | 마지막 완료 봉 UTC | 이번 새 봉 |
|---|---|---|---|---|
| SPY | updated | 2026-10-15T16:52:00.576665+00:00 | 2026-10-15T16:30:00+00:00 | 1 |
| QQQ | updated | 2026-10-15T16:52:00.576665+00:00 | 2026-10-15T16:30:00+00:00 | 1 |
| IWM | updated | 2026-10-15T16:52:00.576665+00:00 | 2026-10-15T16:30:00+00:00 | 1 |
| DIA | updated | 2026-10-15T16:52:00.576665+00:00 | 2026-10-15T16:30:00+00:00 | 1 |
| MSFT | updated | 2026-10-15T16:52:00.576665+00:00 | 2026-10-15T16:30:00+00:00 | 1 |
| JPM | updated | 2026-10-15T16:52:00.576665+00:00 | 2026-10-15T16:30:00+00:00 | 1 |
| XOM | updated | 2026-10-15T16:52:00.576665+00:00 | 2026-10-15T16:30:00+00:00 | 1 |
| JNJ | updated | 2026-10-15T16:52:00.576665+00:00 | 2026-10-15T16:30:00+00:00 | 1 |
| CAT | updated | 2026-10-15T16:52:00.576665+00:00 | 2026-10-15T16:30:00+00:00 | 1 |
| WMT | updated | 2026-10-15T16:52:00.576665+00:00 | 2026-10-15T16:30:00+00:00 | 1 |

이번 실행 소요: 67.47초
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
| v1 | buy_hold | 9977.05 | -22.95 | buy /  / buy_hold: prior completed bar target 100%; next bar open simulation |
| v1 | trend_8_26 | 9975.98 | -24.02 | buy /  / trend_8_26: prior completed bar target 100%; next bar open simulation |
| v1 | momentum_26 | 9956.59 | -43.41 | sell /  / momentum_26: prior completed bar target 0%; next bar open simulation |
| v1 | breakout_8 | 10000.00 | 0.00 | 대기 /  / 새 신호 대기 |
| v1 | reversion_12 | 10000.00 | 0.00 | 대기 /  / 새 신호 대기 |
| v1 | volume_26 | 9949.83 | -50.17 | sell /  / volume_26: prior completed bar target 0%; next bar open simulation |
| v1 | trend_8_26 AND momentum_26 | 9956.59 | -43.41 | sell /  / trend_8_26 AND momentum_26: prior completed bar target 0%; next bar open simulation |
| v1 | trend_8_26 + momentum_26 | 9966.28 | -33.72 | sell /  / trend_8_26 + momentum_26: prior completed bar target 50%; next bar open simulation |
| v1 | trend_8_26 AND breakout_8 | 10000.00 | 0.00 | 대기 /  / 새 신호 대기 |
| v1 | trend_8_26 + breakout_8 | 9987.96 | -12.04 | buy /  / trend_8_26 + breakout_8: prior completed bar target 50%; next bar open simulation |
| v1 | trend_8_26 AND reversion_12 | 10000.00 | 0.00 | 대기 /  / 새 신호 대기 |
| v1 | trend_8_26 + reversion_12 | 9987.96 | -12.04 | buy /  / trend_8_26 + reversion_12: prior completed bar target 50%; next bar open simulation |
| v1 | trend_8_26 AND volume_26 | 9949.83 | -50.17 | sell /  / trend_8_26 AND volume_26: prior completed bar target 0%; next bar open simulation |
| v1 | trend_8_26 + volume_26 | 9962.90 | -37.10 | sell /  / trend_8_26 + volume_26: prior completed bar target 50%; next bar open simulation |
| v1 | momentum_26 AND breakout_8 | 10000.00 | 0.00 | 대기 /  / 새 신호 대기 |
| v1 | momentum_26 + breakout_8 | 9978.25 | -21.75 | sell /  / momentum_26 + breakout_8: prior completed bar target 0%; next bar open simulation |
| v1 | momentum_26 AND reversion_12 | 10000.00 | 0.00 | 대기 /  / 새 신호 대기 |
| v1 | momentum_26 + reversion_12 | 9978.25 | -21.75 | sell /  / momentum_26 + reversion_12: prior completed bar target 0%; next bar open simulation |
| v1 | momentum_26 AND volume_26 | 10000.00 | 0.00 | 대기 /  / 새 신호 대기 |
| v1 | momentum_26 + volume_26 | 9973.12 | -26.88 | sell /  / momentum_26 + volume_26: prior completed bar target 0%; next bar open simulation |
| v1 | breakout_8 AND reversion_12 | 10000.00 | 0.00 | 대기 /  / 새 신호 대기 |
| v1 | breakout_8 + reversion_12 | 10000.00 | 0.00 | 대기 /  / 새 신호 대기 |
| v1 | breakout_8 AND volume_26 | 10000.00 | 0.00 | 대기 /  / 새 신호 대기 |
| v1 | breakout_8 + volume_26 | 9974.87 | -25.13 | sell /  / breakout_8 + volume_26: prior completed bar target 0%; next bar open simulation |
| v1 | reversion_12 AND volume_26 | 10000.00 | 0.00 | 대기 /  / 새 신호 대기 |
| v1 | reversion_12 + volume_26 | 9974.87 | -25.13 | sell /  / reversion_12 + volume_26: prior completed bar target 0%; next bar open simulation |
| v2 | cash | 10000.00 | 0.00 | 대기 /  / 새 신호 대기 |
| v2 | buy_hold | 9867.68 | -132.32 | buy / partial / 직전 완료 봉 목표 비중 100%; 다음 봉 시가 가정 |
| v2 | trend_8_26 | 9823.59 | -176.41 | buy / partial / 직전 완료 봉 목표 비중 100%; 다음 봉 시가 가정 |
| v2 | momentum_26 | 9817.10 | -182.90 | sell / filled / 직전 완료 봉 목표 비중 0%; 다음 봉 시가 가정 |
| v2 | breakout_8 | 9684.78 | -315.22 | sell / filled / 직전 완료 봉 목표 비중 0%; 다음 봉 시가 가정 |
| v2 | reversion_12 | 9535.84 | -464.16 | sell / filled / 직전 완료 봉 목표 비중 0%; 다음 봉 시가 가정 |
| v2 | volume_26 | 9441.45 | -558.55 | sell / filled / 직전 완료 봉 목표 비중 0%; 다음 봉 시가 가정 |
| v2 | trend_8_26 AND momentum_26 | 9823.79 | -176.21 | sell / filled / 직전 완료 봉 목표 비중 0%; 다음 봉 시가 가정 |
| v2 | trend_8_26 + momentum_26 | 9820.36 | -179.64 | sell / filled / 직전 완료 봉 목표 비중 50%; 다음 봉 시가 가정 |
| v2 | trend_8_26 AND breakout_8 | 9913.42 | -86.58 | sell / filled / 직전 완료 봉 목표 비중 0%; 다음 봉 시가 가정 |
| v2 | trend_8_26 + breakout_8 | 9753.79 | -246.21 | buy / filled / 직전 완료 봉 목표 비중 50%; 다음 봉 시가 가정 |
| v2 | trend_8_26 AND reversion_12 | 9896.11 | -103.89 | sell / filled / 직전 완료 봉 목표 비중 0%; 다음 봉 시가 가정 |
| v2 | trend_8_26 + reversion_12 | 9678.35 | -321.65 | buy / filled / 직전 완료 봉 목표 비중 50%; 다음 봉 시가 가정 |
| v2 | trend_8_26 AND volume_26 | 9845.91 | -154.09 | sell / filled / 직전 완료 봉 목표 비중 0%; 다음 봉 시가 가정 |
| v2 | trend_8_26 + volume_26 | 9650.66 | -349.34 | sell / filled / 직전 완료 봉 목표 비중 50%; 다음 봉 시가 가정 |
| v2 | momentum_26 AND breakout_8 | 9871.37 | -128.63 | sell / filled / 직전 완료 봉 목표 비중 0%; 다음 봉 시가 가정 |
| v2 | momentum_26 + breakout_8 | 9750.62 | -249.38 | sell / filled / 직전 완료 봉 목표 비중 0%; 다음 봉 시가 가정 |
| v2 | momentum_26 AND reversion_12 | 9963.21 | -36.79 | sell / filled / 직전 완료 봉 목표 비중 0%; 다음 봉 시가 가정 |
| v2 | momentum_26 + reversion_12 | 9695.53 | -304.47 | sell / filled / 직전 완료 봉 목표 비중 0%; 다음 봉 시가 가정 |
| v2 | momentum_26 AND volume_26 | 9917.25 | -82.75 | sell / filled / 직전 완료 봉 목표 비중 0%; 다음 봉 시가 가정 |
| v2 | momentum_26 + volume_26 | 9688.07 | -311.93 | sell / filled / 직전 완료 봉 목표 비중 0%; 다음 봉 시가 가정 |
| v2 | breakout_8 AND reversion_12 | 10000.00 | 0.00 | 대기 /  / 새 신호 대기 |
| v2 | breakout_8 + reversion_12 | 9650.09 | -349.91 | sell / filled / 직전 완료 봉 목표 비중 0%; 다음 봉 시가 가정 |
| v2 | breakout_8 AND volume_26 | 9933.18 | -66.82 | sell / filled / 직전 완료 봉 목표 비중 0%; 다음 봉 시가 가정 |
| v2 | breakout_8 + volume_26 | 9602.28 | -397.72 | sell / filled / 직전 완료 봉 목표 비중 0%; 다음 봉 시가 가정 |
| v2 | reversion_12 AND volume_26 | 9743.33 | -256.67 | sell / filled / 직전 완료 봉 목표 비중 0%; 다음 봉 시가 가정 |
| v2 | reversion_12 + volume_26 | 9568.30 | -431.70 | sell / filled / 직전 완료 봉 목표 비중 0%; 다음 봉 시가 가정 |

### 같은 기간의 비용·노출 비교 (사후 연구)

| 전략 | 비용 전 | 비용 후 | 100% 보유 | 같은 평균 노출 보유 | 평균 노출 |
|---|---:|---:|---:|---:|---:|
| cash | 0.00% | 0.00% | -0.06% | -0.00% | 0.00% |
| buy_hold | 0.36% | -0.06% | -0.06% | -0.06% | 100.00% |
| trend_8_26 | 1.61% | -1.75% | -0.06% | -0.03% | 49.21% |
| momentum_26 | -0.44% | -4.94% | -0.06% | -0.03% | 48.68% |
| breakout_8 | -0.74% | -15.74% | -0.06% | -0.01% | 22.11% |
| reversion_12 | -1.86% | -12.74% | -0.06% | -0.02% | 27.89% |
| volume_26 | -0.54% | -9.32% | -0.06% | -0.01% | 8.68% |
| trend_8_26 AND momentum_26 | 0.89% | -2.85% | -0.06% | -0.02% | 42.37% |
| trend_8_26 + momentum_26 | 0.58% | -3.15% | -0.06% | -0.03% | 48.95% |
| trend_8_26 AND breakout_8 | -0.06% | -10.40% | -0.06% | -0.01% | 13.16% |
| trend_8_26 + breakout_8 | 0.43% | -9.01% | -0.06% | -0.02% | 35.66% |
| trend_8_26 AND reversion_12 | 0.10% | -4.01% | -0.06% | -0.00% | 6.05% |
| trend_8_26 + reversion_12 | -0.13% | -7.22% | -0.06% | -0.02% | 38.56% |
| trend_8_26 AND volume_26 | -0.17% | -4.27% | -0.06% | -0.00% | 3.95% |
| trend_8_26 + volume_26 | 0.53% | -5.61% | -0.06% | -0.02% | 28.95% |
| momentum_26 AND breakout_8 | 0.24% | -10.13% | -0.06% | -0.01% | 14.21% |
| momentum_26 + breakout_8 | -0.59% | -10.50% | -0.06% | -0.02% | 35.40% |
| momentum_26 AND reversion_12 | -0.88% | -5.75% | -0.06% | -0.00% | 6.84% |
| momentum_26 + reversion_12 | -1.15% | -8.36% | -0.06% | -0.02% | 38.29% |
| momentum_26 AND volume_26 | -0.22% | -3.11% | -0.06% | -0.00% | 2.11% |
| momentum_26 + volume_26 | -0.49% | -5.78% | -0.06% | -0.02% | 28.69% |
| breakout_8 AND reversion_12 | 0.00% | 0.00% | -0.06% | -0.00% | 0.00% |
| breakout_8 + reversion_12 | -1.30% | -13.72% | -0.06% | -0.01% | 25.01% |
| breakout_8 AND volume_26 | 0.05% | -1.61% | -0.06% | -0.00% | 1.32% |
| breakout_8 + volume_26 | -0.64% | -11.67% | -0.06% | -0.01% | 15.40% |
| reversion_12 AND volume_26 | -0.67% | -4.76% | -0.06% | -0.00% | 3.95% |
| reversion_12 + volume_26 | -1.20% | -10.68% | -0.06% | -0.01% | 18.30% |

동일 구간·초기 자금, 종료 시 청산 비용 포함. 노출 맞춤은 사후 설명용이며 v2 실제 계좌 성과가 아닙니다.
[낙폭 분해·비용 영향·전체 구간](SPY/comparison.json)

[v1 전체 기록](SPY/accounts.json) · [v2 전체 기록](SPY/accounts-v2.json)

## QQQ 계좌

| 모델 | 전략 | 평가액 USD | 손익 USD | 최근 매매·이유 |
|---|---|---:|---:|---|
| v1 | cash | 10000.00 | 0.00 | 대기 /  / 새 신호 대기 |
| v1 | buy_hold | 9971.77 | -28.23 | buy /  / buy_hold: prior completed bar target 100%; next bar open simulation |
| v1 | trend_8_26 | 10000.00 | 0.00 | 대기 /  / 새 신호 대기 |
| v1 | momentum_26 | 10000.00 | 0.00 | 대기 /  / 새 신호 대기 |
| v1 | breakout_8 | 10000.00 | 0.00 | 대기 /  / 새 신호 대기 |
| v1 | reversion_12 | 10000.00 | 0.00 | 대기 /  / 새 신호 대기 |
| v1 | volume_26 | 9962.28 | -37.72 | sell /  / volume_26: prior completed bar target 0%; next bar open simulation |
| v1 | trend_8_26 AND momentum_26 | 10000.00 | 0.00 | 대기 /  / 새 신호 대기 |
| v1 | trend_8_26 + momentum_26 | 10000.00 | 0.00 | 대기 /  / 새 신호 대기 |
| v1 | trend_8_26 AND breakout_8 | 10000.00 | 0.00 | 대기 /  / 새 신호 대기 |
| v1 | trend_8_26 + breakout_8 | 10000.00 | 0.00 | 대기 /  / 새 신호 대기 |
| v1 | trend_8_26 AND reversion_12 | 10000.00 | 0.00 | 대기 /  / 새 신호 대기 |
| v1 | trend_8_26 + reversion_12 | 10000.00 | 0.00 | 대기 /  / 새 신호 대기 |
| v1 | trend_8_26 AND volume_26 | 10000.00 | 0.00 | 대기 /  / 새 신호 대기 |
| v1 | trend_8_26 + volume_26 | 9981.11 | -18.89 | sell /  / trend_8_26 + volume_26: prior completed bar target 0%; next bar open simulation |
| v1 | momentum_26 AND breakout_8 | 10000.00 | 0.00 | 대기 /  / 새 신호 대기 |
| v1 | momentum_26 + breakout_8 | 10000.00 | 0.00 | 대기 /  / 새 신호 대기 |
| v1 | momentum_26 AND reversion_12 | 10000.00 | 0.00 | 대기 /  / 새 신호 대기 |
| v1 | momentum_26 + reversion_12 | 10000.00 | 0.00 | 대기 /  / 새 신호 대기 |
| v1 | momentum_26 AND volume_26 | 10000.00 | 0.00 | 대기 /  / 새 신호 대기 |
| v1 | momentum_26 + volume_26 | 9981.11 | -18.89 | sell /  / momentum_26 + volume_26: prior completed bar target 0%; next bar open simulation |
| v1 | breakout_8 AND reversion_12 | 10000.00 | 0.00 | 대기 /  / 새 신호 대기 |
| v1 | breakout_8 + reversion_12 | 10000.00 | 0.00 | 대기 /  / 새 신호 대기 |
| v1 | breakout_8 AND volume_26 | 10000.00 | 0.00 | 대기 /  / 새 신호 대기 |
| v1 | breakout_8 + volume_26 | 9981.11 | -18.89 | sell /  / breakout_8 + volume_26: prior completed bar target 0%; next bar open simulation |
| v1 | reversion_12 AND volume_26 | 10000.00 | 0.00 | 대기 /  / 새 신호 대기 |
| v1 | reversion_12 + volume_26 | 9981.11 | -18.89 | sell /  / reversion_12 + volume_26: prior completed bar target 0%; next bar open simulation |
| v2 | cash | 10000.00 | 0.00 | 대기 /  / 새 신호 대기 |
| v2 | buy_hold | 9637.59 | -362.41 | buy / partial / 직전 완료 봉 목표 비중 100%; 다음 봉 시가 가정 |
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
| v2 | trend_8_26 + volume_26 | 9592.41 | -407.59 | sell / filled / 직전 완료 봉 목표 비중 0%; 다음 봉 시가 가정 |
| v2 | momentum_26 AND breakout_8 | 10000.00 | 0.00 | 대기 /  / 새 신호 대기 |
| v2 | momentum_26 + breakout_8 | 9861.05 | -138.95 | sell / filled / 직전 완료 봉 목표 비중 0%; 다음 봉 시가 가정 |
| v2 | momentum_26 AND reversion_12 | 10000.00 | 0.00 | 대기 /  / 새 신호 대기 |
| v2 | momentum_26 + reversion_12 | 9744.19 | -255.81 | sell / filled / 직전 완료 봉 목표 비중 0%; 다음 봉 시가 가정 |
| v2 | momentum_26 AND volume_26 | 9936.83 | -63.17 | sell / filled / 직전 완료 봉 목표 비중 0%; 다음 봉 시가 가정 |
| v2 | momentum_26 + volume_26 | 9668.12 | -331.88 | sell / filled / 직전 완료 봉 목표 비중 0%; 다음 봉 시가 가정 |
| v2 | breakout_8 AND reversion_12 | 10000.00 | 0.00 | 대기 /  / 새 신호 대기 |
| v2 | breakout_8 + reversion_12 | 9710.65 | -289.35 | sell / filled / 직전 완료 봉 목표 비중 0%; 다음 봉 시가 가정 |
| v2 | breakout_8 AND volume_26 | 9947.98 | -52.02 | sell / filled / 직전 완료 봉 목표 비중 0%; 다음 봉 시가 가정 |
| v2 | breakout_8 + volume_26 | 9634.88 | -365.12 | sell / filled / 직전 완료 봉 목표 비중 0%; 다음 봉 시가 가정 |
| v2 | reversion_12 AND volume_26 | 9547.64 | -452.36 | 중단: 손실 한도 / sell / filled / 직전 완료 봉 목표 비중 0%; 다음 봉 시가 가정 |
| v2 | reversion_12 + volume_26 | 9481.14 | -518.86 | sell / filled / 직전 완료 봉 목표 비중 0%; 다음 봉 시가 가정 |

### 같은 기간의 비용·노출 비교 (사후 연구)

| 전략 | 비용 전 | 비용 후 | 100% 보유 | 같은 평균 노출 보유 | 평균 노출 |
|---|---:|---:|---:|---:|---:|
| cash | 0.00% | 0.00% | -2.61% | -0.00% | 0.00% |
| buy_hold | -2.20% | -2.61% | -2.61% | -2.61% | 100.00% |
| trend_8_26 | 0.35% | -2.96% | -2.61% | -1.27% | 48.95% |
| momentum_26 | -1.12% | -5.59% | -2.61% | -1.13% | 43.42% |
| breakout_8 | -1.69% | -16.89% | -2.61% | -0.46% | 17.63% |
| reversion_12 | -0.86% | -12.96% | -2.61% | -0.69% | 26.58% |
| volume_26 | -1.07% | -13.51% | -2.61% | -0.37% | 14.21% |
| trend_8_26 AND momentum_26 | -0.15% | -3.86% | -2.61% | -1.01% | 38.95% |
| trend_8_26 + momentum_26 | -0.38% | -4.08% | -2.61% | -1.20% | 46.19% |
| trend_8_26 AND breakout_8 | -0.58% | -10.12% | -2.61% | -0.28% | 10.79% |
| trend_8_26 + breakout_8 | -0.67% | -9.82% | -2.61% | -0.87% | 33.30% |
| trend_8_26 AND reversion_12 | 0.42% | -5.31% | -2.61% | -0.16% | 6.05% |
| trend_8_26 + reversion_12 | -0.24% | -7.52% | -2.61% | -0.98% | 37.77% |
| trend_8_26 AND volume_26 | -0.71% | -5.59% | -2.61% | -0.11% | 4.21% |
| trend_8_26 + volume_26 | -0.36% | -8.20% | -2.61% | -0.82% | 31.58% |
| momentum_26 AND breakout_8 | -0.74% | -9.88% | -2.61% | -0.29% | 11.05% |
| momentum_26 + breakout_8 | -1.40% | -11.23% | -2.61% | -0.79% | 30.53% |
| momentum_26 AND reversion_12 | -0.02% | -5.73% | -2.61% | -0.12% | 4.74% |
| momentum_26 + reversion_12 | -0.98% | -8.78% | -2.61% | -0.91% | 35.01% |
| momentum_26 AND volume_26 | -0.30% | -4.40% | -2.61% | -0.09% | 3.42% |
| momentum_26 + volume_26 | -1.09% | -9.45% | -2.61% | -0.75% | 28.82% |
| breakout_8 AND reversion_12 | 0.00% | 0.00% | -2.61% | -0.00% | 0.00% |
| breakout_8 + reversion_12 | -1.27% | -14.06% | -2.61% | -0.57% | 22.11% |
| breakout_8 AND volume_26 | 0.04% | -2.04% | -2.61% | -0.03% | 1.32% |
| breakout_8 + volume_26 | -1.38% | -13.97% | -2.61% | -0.41% | 15.93% |
| reversion_12 AND volume_26 | -1.25% | -8.44% | -2.61% | -0.23% | 8.68% |
| reversion_12 + volume_26 | -0.96% | -12.88% | -2.61% | -0.53% | 20.40% |

동일 구간·초기 자금, 종료 시 청산 비용 포함. 노출 맞춤은 사후 설명용이며 v2 실제 계좌 성과가 아닙니다.
[낙폭 분해·비용 영향·전체 구간](QQQ/comparison.json)

[v1 전체 기록](QQQ/accounts.json) · [v2 전체 기록](QQQ/accounts-v2.json)

## IWM 계좌

| 모델 | 전략 | 평가액 USD | 손익 USD | 최근 매매·이유 |
|---|---|---:|---:|---|
| v1 | cash | 10000.00 | 0.00 | 대기 /  / 새 신호 대기 |
| v1 | buy_hold | 9959.26 | -40.74 | buy /  / buy_hold: prior completed bar target 100%; next bar open simulation |
| v1 | trend_8_26 | 9959.26 | -40.74 | buy /  / trend_8_26: prior completed bar target 100%; next bar open simulation |
| v1 | momentum_26 | 9959.26 | -40.74 | buy /  / momentum_26: prior completed bar target 100%; next bar open simulation |
| v1 | breakout_8 | 10000.00 | 0.00 | 대기 /  / 새 신호 대기 |
| v1 | reversion_12 | 10000.00 | 0.00 | 대기 /  / 새 신호 대기 |
| v1 | volume_26 | 10000.00 | 0.00 | 대기 /  / 새 신호 대기 |
| v1 | trend_8_26 AND momentum_26 | 9959.26 | -40.74 | buy /  / trend_8_26 AND momentum_26: prior completed bar target 100%; next bar open simulation |
| v1 | trend_8_26 + momentum_26 | 9959.26 | -40.74 | buy /  / trend_8_26 + momentum_26: prior completed bar target 100%; next bar open simulation |
| v1 | trend_8_26 AND breakout_8 | 10000.00 | 0.00 | 대기 /  / 새 신호 대기 |
| v1 | trend_8_26 + breakout_8 | 9979.58 | -20.42 | buy /  / trend_8_26 + breakout_8: prior completed bar target 50%; next bar open simulation |
| v1 | trend_8_26 AND reversion_12 | 10000.00 | 0.00 | 대기 /  / 새 신호 대기 |
| v1 | trend_8_26 + reversion_12 | 9979.58 | -20.42 | buy /  / trend_8_26 + reversion_12: prior completed bar target 50%; next bar open simulation |
| v1 | trend_8_26 AND volume_26 | 10000.00 | 0.00 | 대기 /  / 새 신호 대기 |
| v1 | trend_8_26 + volume_26 | 9979.58 | -20.42 | buy /  / trend_8_26 + volume_26: prior completed bar target 50%; next bar open simulation |
| v1 | momentum_26 AND breakout_8 | 10000.00 | 0.00 | 대기 /  / 새 신호 대기 |
| v1 | momentum_26 + breakout_8 | 9979.58 | -20.42 | buy /  / momentum_26 + breakout_8: prior completed bar target 50%; next bar open simulation |
| v1 | momentum_26 AND reversion_12 | 10000.00 | 0.00 | 대기 /  / 새 신호 대기 |
| v1 | momentum_26 + reversion_12 | 9979.58 | -20.42 | buy /  / momentum_26 + reversion_12: prior completed bar target 50%; next bar open simulation |
| v1 | momentum_26 AND volume_26 | 10000.00 | 0.00 | 대기 /  / 새 신호 대기 |
| v1 | momentum_26 + volume_26 | 9979.58 | -20.42 | buy /  / momentum_26 + volume_26: prior completed bar target 50%; next bar open simulation |
| v1 | breakout_8 AND reversion_12 | 10000.00 | 0.00 | 대기 /  / 새 신호 대기 |
| v1 | breakout_8 + reversion_12 | 10000.00 | 0.00 | 대기 /  / 새 신호 대기 |
| v1 | breakout_8 AND volume_26 | 10000.00 | 0.00 | 대기 /  / 새 신호 대기 |
| v1 | breakout_8 + volume_26 | 10000.00 | 0.00 | 대기 /  / 새 신호 대기 |
| v1 | reversion_12 AND volume_26 | 10000.00 | 0.00 | 대기 /  / 새 신호 대기 |
| v1 | reversion_12 + volume_26 | 10000.00 | 0.00 | 대기 /  / 새 신호 대기 |
| v2 | cash | 10000.00 | 0.00 | 대기 /  / 새 신호 대기 |
| v2 | buy_hold | 9794.48 | -205.52 | buy / partial / 직전 완료 봉 목표 비중 100%; 다음 봉 시가 가정 |
| v2 | trend_8_26 | 9772.05 | -227.95 | buy / partial / 직전 완료 봉 목표 비중 100%; 다음 봉 시가 가정 |
| v2 | momentum_26 | 9773.05 | -226.95 | buy / partial / 직전 완료 봉 목표 비중 100%; 다음 봉 시가 가정 |
| v2 | breakout_8 | 9666.31 | -333.69 | sell / filled / 직전 완료 봉 목표 비중 0%; 다음 봉 시가 가정 |
| v2 | reversion_12 | 9538.67 | -461.33 | sell / filled / 직전 완료 봉 목표 비중 0%; 다음 봉 시가 가정 |
| v2 | volume_26 | 9513.36 | -486.64 | sell / filled / 직전 완료 봉 목표 비중 0%; 다음 봉 시가 가정 |
| v2 | trend_8_26 AND momentum_26 | 9923.73 | -76.27 | buy / partial / 직전 완료 봉 목표 비중 100%; 다음 봉 시가 가정 |
| v2 | trend_8_26 + momentum_26 | 9793.23 | -206.77 | buy / partial / 직전 완료 봉 목표 비중 100%; 다음 봉 시가 가정 |
| v2 | trend_8_26 AND breakout_8 | 9962.82 | -37.18 | sell / filled / 직전 완료 봉 목표 비중 0%; 다음 봉 시가 가정 |
| v2 | trend_8_26 + breakout_8 | 9739.57 | -260.43 | buy / filled / 직전 완료 봉 목표 비중 50%; 다음 봉 시가 가정 |
| v2 | trend_8_26 AND reversion_12 | 9881.82 | -118.18 | sell / filled / 직전 완료 봉 목표 비중 0%; 다음 봉 시가 가정 |
| v2 | trend_8_26 + reversion_12 | 9654.52 | -345.48 | buy / filled / 직전 완료 봉 목표 비중 50%; 다음 봉 시가 가정 |
| v2 | trend_8_26 AND volume_26 | 9862.83 | -137.17 | sell / filled / 직전 완료 봉 목표 비중 0%; 다음 봉 시가 가정 |
| v2 | trend_8_26 + volume_26 | 9662.12 | -337.88 | buy / filled / 직전 완료 봉 목표 비중 50%; 다음 봉 시가 가정 |
| v2 | momentum_26 AND breakout_8 | 9854.44 | -145.56 | sell / filled / 직전 완료 봉 목표 비중 0%; 다음 봉 시가 가정 |
| v2 | momentum_26 + breakout_8 | 9719.52 | -280.48 | buy / filled / 직전 완료 봉 목표 비중 50%; 다음 봉 시가 가정 |
| v2 | momentum_26 AND reversion_12 | 9960.59 | -39.41 | sell / filled / 직전 완료 봉 목표 비중 0%; 다음 봉 시가 가정 |
| v2 | momentum_26 + reversion_12 | 9675.10 | -324.90 | buy / filled / 직전 완료 봉 목표 비중 50%; 다음 봉 시가 가정 |
| v2 | momentum_26 AND volume_26 | 9897.79 | -102.21 | sell / filled / 직전 완료 봉 목표 비중 0%; 다음 봉 시가 가정 |
| v2 | momentum_26 + volume_26 | 9642.15 | -357.85 | buy / filled / 직전 완료 봉 목표 비중 50%; 다음 봉 시가 가정 |
| v2 | breakout_8 AND reversion_12 | 10000.00 | 0.00 | 대기 /  / 새 신호 대기 |
| v2 | breakout_8 + reversion_12 | 9642.35 | -357.65 | sell / filled / 직전 완료 봉 목표 비중 0%; 다음 봉 시가 가정 |
| v2 | breakout_8 AND volume_26 | 9746.03 | -253.97 | sell / filled / 직전 완료 봉 목표 비중 0%; 다음 봉 시가 가정 |
| v2 | breakout_8 + volume_26 | 9609.68 | -390.32 | sell / filled / 직전 완료 봉 목표 비중 0%; 다음 봉 시가 가정 |
| v2 | reversion_12 AND volume_26 | 9740.75 | -259.25 | sell / filled / 직전 완료 봉 목표 비중 0%; 다음 봉 시가 가정 |
| v2 | reversion_12 + volume_26 | 9545.82 | -454.18 | sell / filled / 직전 완료 봉 목표 비중 0%; 다음 봉 시가 가정 |

### 같은 기간의 비용·노출 비교 (사후 연구)

| 전략 | 비용 전 | 비용 후 | 100% 보유 | 같은 평균 노출 보유 | 평균 노출 |
|---|---:|---:|---:|---:|---:|
| cash | 0.00% | 0.00% | -3.24% | -0.00% | 0.00% |
| buy_hold | -2.83% | -3.24% | -3.24% | -3.24% | 100.00% |
| trend_8_26 | -2.26% | -6.28% | -3.24% | -1.46% | 44.74% |
| momentum_26 | -3.08% | -8.61% | -3.24% | -1.28% | 39.21% |
| breakout_8 | -0.83% | -13.67% | -3.24% | -0.60% | 18.42% |
| reversion_12 | -2.15% | -14.82% | -3.24% | -0.98% | 30.00% |
| volume_26 | -2.34% | -9.45% | -3.24% | -0.28% | 8.68% |
| trend_8_26 AND momentum_26 | -2.74% | -7.13% | -3.24% | -1.10% | 33.68% |
| trend_8_26 + momentum_26 | -2.66% | -7.06% | -3.24% | -1.37% | 41.98% |
| trend_8_26 AND breakout_8 | -0.70% | -7.93% | -3.24% | -0.33% | 10.00% |
| trend_8_26 + breakout_8 | -1.54% | -9.86% | -3.24% | -1.03% | 31.58% |
| trend_8_26 AND reversion_12 | -0.12% | -5.03% | -3.24% | -0.20% | 6.05% |
| trend_8_26 + reversion_12 | -2.20% | -10.47% | -3.24% | -1.22% | 37.37% |
| trend_8_26 AND volume_26 | -1.05% | -4.72% | -3.24% | -0.12% | 3.68% |
| trend_8_26 + volume_26 | -2.29% | -7.69% | -3.24% | -0.87% | 26.71% |
| momentum_26 AND breakout_8 | -0.10% | -7.37% | -3.24% | -0.32% | 9.74% |
| momentum_26 + breakout_8 | -1.96% | -11.18% | -3.24% | -0.94% | 28.82% |
| momentum_26 AND reversion_12 | -0.05% | -3.76% | -3.24% | -0.11% | 3.42% |
| momentum_26 + reversion_12 | -2.61% | -10.66% | -3.24% | -1.13% | 34.61% |
| momentum_26 AND volume_26 | -1.34% | -4.20% | -3.24% | -0.07% | 2.11% |
| momentum_26 + volume_26 | -2.70% | -8.65% | -3.24% | -0.78% | 23.95% |
| breakout_8 AND reversion_12 | 0.00% | 0.00% | -3.24% | -0.00% | 0.00% |
| breakout_8 + reversion_12 | -1.49% | -13.53% | -3.24% | -0.79% | 24.22% |
| breakout_8 AND volume_26 | -1.33% | -4.19% | -3.24% | -0.08% | 2.37% |
| breakout_8 + volume_26 | -1.59% | -11.40% | -3.24% | -0.44% | 13.56% |
| reversion_12 AND volume_26 | -0.38% | -4.47% | -3.24% | -0.15% | 4.47% |
| reversion_12 + volume_26 | -2.24% | -11.63% | -3.24% | -0.63% | 19.35% |

동일 구간·초기 자금, 종료 시 청산 비용 포함. 노출 맞춤은 사후 설명용이며 v2 실제 계좌 성과가 아닙니다.
[낙폭 분해·비용 영향·전체 구간](IWM/comparison.json)

[v1 전체 기록](IWM/accounts.json) · [v2 전체 기록](IWM/accounts-v2.json)

## DIA 계좌

| 모델 | 전략 | 평가액 USD | 손익 USD | 최근 매매·이유 |
|---|---|---:|---:|---|
| v1 | cash | 10000.00 | 0.00 | 대기 /  / 새 신호 대기 |
| v1 | buy_hold | 9969.87 | -30.13 | buy /  / buy_hold: prior completed bar target 100%; next bar open simulation |
| v1 | trend_8_26 | 9969.87 | -30.13 | buy /  / trend_8_26: prior completed bar target 100%; next bar open simulation |
| v1 | momentum_26 | 9969.87 | -30.13 | buy /  / momentum_26: prior completed bar target 100%; next bar open simulation |
| v1 | breakout_8 | 10000.00 | 0.00 | 대기 /  / 새 신호 대기 |
| v1 | reversion_12 | 10000.00 | 0.00 | 대기 /  / 새 신호 대기 |
| v1 | volume_26 | 10000.00 | 0.00 | 대기 /  / 새 신호 대기 |
| v1 | trend_8_26 AND momentum_26 | 9969.87 | -30.13 | buy /  / trend_8_26 AND momentum_26: prior completed bar target 100%; next bar open simulation |
| v1 | trend_8_26 + momentum_26 | 9969.87 | -30.13 | buy /  / trend_8_26 + momentum_26: prior completed bar target 100%; next bar open simulation |
| v1 | trend_8_26 AND breakout_8 | 10000.00 | 0.00 | 대기 /  / 새 신호 대기 |
| v1 | trend_8_26 + breakout_8 | 9984.89 | -15.11 | sell /  / trend_8_26 + breakout_8: prior completed bar target 50%; next bar open simulation |
| v1 | trend_8_26 AND reversion_12 | 10000.00 | 0.00 | 대기 /  / 새 신호 대기 |
| v1 | trend_8_26 + reversion_12 | 9984.89 | -15.11 | sell /  / trend_8_26 + reversion_12: prior completed bar target 50%; next bar open simulation |
| v1 | trend_8_26 AND volume_26 | 10000.00 | 0.00 | 대기 /  / 새 신호 대기 |
| v1 | trend_8_26 + volume_26 | 9984.89 | -15.11 | sell /  / trend_8_26 + volume_26: prior completed bar target 50%; next bar open simulation |
| v1 | momentum_26 AND breakout_8 | 10000.00 | 0.00 | 대기 /  / 새 신호 대기 |
| v1 | momentum_26 + breakout_8 | 9984.89 | -15.11 | sell /  / momentum_26 + breakout_8: prior completed bar target 50%; next bar open simulation |
| v1 | momentum_26 AND reversion_12 | 10000.00 | 0.00 | 대기 /  / 새 신호 대기 |
| v1 | momentum_26 + reversion_12 | 9984.89 | -15.11 | sell /  / momentum_26 + reversion_12: prior completed bar target 50%; next bar open simulation |
| v1 | momentum_26 AND volume_26 | 10000.00 | 0.00 | 대기 /  / 새 신호 대기 |
| v1 | momentum_26 + volume_26 | 9984.89 | -15.11 | sell /  / momentum_26 + volume_26: prior completed bar target 50%; next bar open simulation |
| v1 | breakout_8 AND reversion_12 | 10000.00 | 0.00 | 대기 /  / 새 신호 대기 |
| v1 | breakout_8 + reversion_12 | 10000.00 | 0.00 | 대기 /  / 새 신호 대기 |
| v1 | breakout_8 AND volume_26 | 10000.00 | 0.00 | 대기 /  / 새 신호 대기 |
| v1 | breakout_8 + volume_26 | 10000.00 | 0.00 | 대기 /  / 새 신호 대기 |
| v1 | reversion_12 AND volume_26 | 10000.00 | 0.00 | 대기 /  / 새 신호 대기 |
| v1 | reversion_12 + volume_26 | 10000.00 | 0.00 | 대기 /  / 새 신호 대기 |
| v2 | cash | 10000.00 | 0.00 | 대기 /  / 새 신호 대기 |
| v2 | buy_hold | 10053.04 | 53.04 | buy / partial / 직전 완료 봉 목표 비중 100%; 다음 봉 시가 가정 |
| v2 | trend_8_26 | 9865.69 | -134.31 | buy / partial / 직전 완료 봉 목표 비중 100%; 다음 봉 시가 가정 |
| v2 | momentum_26 | 9974.16 | -25.84 | buy / partial / 직전 완료 봉 목표 비중 100%; 다음 봉 시가 가정 |
| v2 | breakout_8 | 9626.51 | -373.49 | sell / filled / 직전 완료 봉 목표 비중 0%; 다음 봉 시가 가정 |
| v2 | reversion_12 | 9698.03 | -301.97 | sell / filled / 직전 완료 봉 목표 비중 0%; 다음 봉 시가 가정 |
| v2 | volume_26 | 9718.21 | -281.79 | sell / filled / 직전 완료 봉 목표 비중 0%; 다음 봉 시가 가정 |
| v2 | trend_8_26 AND momentum_26 | 9969.54 | -30.46 | buy / partial / 직전 완료 봉 목표 비중 100%; 다음 봉 시가 가정 |
| v2 | trend_8_26 + momentum_26 | 9919.85 | -80.15 | buy / partial / 직전 완료 봉 목표 비중 100%; 다음 봉 시가 가정 |
| v2 | trend_8_26 AND breakout_8 | 9789.40 | -210.60 | sell / filled / 직전 완료 봉 목표 비중 0%; 다음 봉 시가 가정 |
| v2 | trend_8_26 + breakout_8 | 9745.38 | -254.62 | sell / filled / 직전 완료 봉 목표 비중 50%; 다음 봉 시가 가정 |
| v2 | trend_8_26 AND reversion_12 | 9810.77 | -189.23 | sell / filled / 직전 완료 봉 목표 비중 0%; 다음 봉 시가 가정 |
| v2 | trend_8_26 + reversion_12 | 9781.28 | -218.72 | sell / filled / 직전 완료 봉 목표 비중 50%; 다음 봉 시가 가정 |
| v2 | trend_8_26 AND volume_26 | 9858.88 | -141.12 | sell / filled / 직전 완료 봉 목표 비중 0%; 다음 봉 시가 가정 |
| v2 | trend_8_26 + volume_26 | 9812.23 | -187.77 | sell / filled / 직전 완료 봉 목표 비중 50%; 다음 봉 시가 가정 |
| v2 | momentum_26 AND breakout_8 | 9778.26 | -221.74 | sell / filled / 직전 완료 봉 목표 비중 0%; 다음 봉 시가 가정 |
| v2 | momentum_26 + breakout_8 | 9798.88 | -201.12 | sell / filled / 직전 완료 봉 목표 비중 50%; 다음 봉 시가 가정 |
| v2 | momentum_26 AND reversion_12 | 9955.97 | -44.03 | sell / filled / 직전 완료 봉 목표 비중 0%; 다음 봉 시가 가정 |
| v2 | momentum_26 + reversion_12 | 9834.98 | -165.02 | sell / filled / 직전 완료 봉 목표 비중 50%; 다음 봉 시가 가정 |
| v2 | momentum_26 AND volume_26 | 9791.42 | -208.58 | sell / filled / 직전 완료 봉 목표 비중 0%; 다음 봉 시가 가정 |
| v2 | momentum_26 + volume_26 | 9886.90 | -113.10 | sell / filled / 직전 완료 봉 목표 비중 50%; 다음 봉 시가 가정 |
| v2 | breakout_8 AND reversion_12 | 10000.00 | 0.00 | 대기 /  / 새 신호 대기 |
| v2 | breakout_8 + reversion_12 | 9661.83 | -338.17 | sell / filled / 직전 완료 봉 목표 비중 0%; 다음 봉 시가 가정 |
| v2 | breakout_8 AND volume_26 | 9796.56 | -203.44 | sell / filled / 직전 완료 봉 목표 비중 0%; 다음 봉 시가 가정 |
| v2 | breakout_8 + volume_26 | 9672.16 | -327.84 | sell / filled / 직전 완료 봉 목표 비중 0%; 다음 봉 시가 가정 |
| v2 | reversion_12 AND volume_26 | 10000.00 | 0.00 | 대기 /  / 새 신호 대기 |
| v2 | reversion_12 + volume_26 | 9707.85 | -292.15 | sell / filled / 직전 완료 봉 목표 비중 0%; 다음 봉 시가 가정 |

### 같은 기간의 비용·노출 비교 (사후 연구)

| 전략 | 비용 전 | 비용 후 | 100% 보유 | 같은 평균 노출 보유 | 평균 노출 |
|---|---:|---:|---:|---:|---:|
| cash | 0.00% | 0.00% | 1.08% | 0.00% | 0.00% |
| buy_hold | 1.51% | 1.08% | 1.08% | 1.08% | 100.00% |
| trend_8_26 | 1.82% | -2.77% | 1.08% | 0.61% | 56.05% |
| momentum_26 | 0.07% | -4.05% | 1.08% | 0.56% | 51.32% |
| breakout_8 | 0.14% | -16.40% | 1.08% | 0.25% | 23.42% |
| reversion_12 | -1.36% | -9.30% | 1.08% | 0.27% | 24.74% |
| volume_26 | -0.82% | -11.45% | 1.08% | 0.13% | 11.58% |
| trend_8_26 AND momentum_26 | 1.54% | -2.64% | 1.08% | 0.49% | 45.53% |
| trend_8_26 + momentum_26 | 0.95% | -3.41% | 1.08% | 0.58% | 53.69% |
| trend_8_26 AND breakout_8 | 0.71% | -10.84% | 1.08% | 0.17% | 15.26% |
| trend_8_26 + breakout_8 | 0.98% | -9.66% | 1.08% | 0.43% | 39.74% |
| trend_8_26 AND reversion_12 | 0.37% | -4.56% | 1.08% | 0.07% | 6.32% |
| trend_8_26 + reversion_12 | 0.23% | -5.71% | 1.08% | 0.44% | 40.40% |
| trend_8_26 AND volume_26 | 0.73% | -5.02% | 1.08% | 0.06% | 5.79% |
| trend_8_26 + volume_26 | 0.50% | -7.03% | 1.08% | 0.37% | 33.82% |
| momentum_26 AND breakout_8 | -0.09% | -11.17% | 1.08% | 0.17% | 15.53% |
| momentum_26 + breakout_8 | 0.11% | -10.25% | 1.08% | 0.40% | 37.37% |
| momentum_26 AND reversion_12 | -0.18% | -3.88% | 1.08% | 0.06% | 5.79% |
| momentum_26 + reversion_12 | -0.64% | -5.93% | 1.08% | 0.41% | 38.03% |
| momentum_26 AND volume_26 | -0.36% | -6.05% | 1.08% | 0.05% | 5.00% |
| momentum_26 + volume_26 | -0.37% | -7.05% | 1.08% | 0.34% | 31.45% |
| breakout_8 AND reversion_12 | 0.00% | 0.00% | 1.08% | 0.00% | 0.00% |
| breakout_8 + reversion_12 | -0.61% | -12.57% | 1.08% | 0.26% | 24.09% |
| breakout_8 AND volume_26 | -0.82% | -4.90% | 1.08% | 0.04% | 3.42% |
| breakout_8 + volume_26 | -0.34% | -13.06% | 1.08% | 0.19% | 17.51% |
| reversion_12 AND volume_26 | -0.20% | -5.11% | 1.08% | 0.04% | 3.95% |
| reversion_12 + volume_26 | -1.09% | -10.39% | 1.08% | 0.20% | 18.16% |

동일 구간·초기 자금, 종료 시 청산 비용 포함. 노출 맞춤은 사후 설명용이며 v2 실제 계좌 성과가 아닙니다.
[낙폭 분해·비용 영향·전체 구간](DIA/comparison.json)

[v1 전체 기록](DIA/accounts.json) · [v2 전체 기록](DIA/accounts-v2.json)

## MSFT 계좌

| 모델 | 전략 | 평가액 USD | 손익 USD | 최근 매매·이유 |
|---|---|---:|---:|---|
| v1 | cash | 10000.00 | 0.00 | 대기 /  / 새 신호 대기 |
| v1 | buy_hold | 10033.90 | 33.90 | buy /  / buy_hold: prior completed bar target 100%; next bar open simulation |
| v1 | trend_8_26 | 10033.90 | 33.90 | buy /  / trend_8_26: prior completed bar target 100%; next bar open simulation |
| v1 | momentum_26 | 10035.95 | 35.95 | buy /  / momentum_26: prior completed bar target 100%; next bar open simulation |
| v1 | breakout_8 | 9998.17 | -1.83 | buy /  / breakout_8: prior completed bar target 100%; next bar open simulation |
| v1 | reversion_12 | 10000.00 | 0.00 | 대기 /  / 새 신호 대기 |
| v1 | volume_26 | 9997.72 | -2.28 | sell /  / volume_26: prior completed bar target 0%; next bar open simulation |
| v1 | trend_8_26 AND momentum_26 | 10035.95 | 35.95 | buy /  / trend_8_26 AND momentum_26: prior completed bar target 100%; next bar open simulation |
| v1 | trend_8_26 + momentum_26 | 10034.92 | 34.92 | buy /  / trend_8_26 + momentum_26: prior completed bar target 100%; next bar open simulation |
| v1 | trend_8_26 AND breakout_8 | 9998.17 | -1.83 | buy /  / trend_8_26 AND breakout_8: prior completed bar target 100%; next bar open simulation |
| v1 | trend_8_26 + breakout_8 | 10016.00 | 16.00 | buy /  / trend_8_26 + breakout_8: prior completed bar target 100%; next bar open simulation |
| v1 | trend_8_26 AND reversion_12 | 10000.00 | 0.00 | 대기 /  / 새 신호 대기 |
| v1 | trend_8_26 + reversion_12 | 10016.90 | 16.90 | sell /  / trend_8_26 + reversion_12: prior completed bar target 50%; next bar open simulation |
| v1 | trend_8_26 AND volume_26 | 9997.72 | -2.28 | sell /  / trend_8_26 AND volume_26: prior completed bar target 0%; next bar open simulation |
| v1 | trend_8_26 + volume_26 | 10015.79 | 15.79 | sell /  / trend_8_26 + volume_26: prior completed bar target 50%; next bar open simulation |
| v1 | momentum_26 AND breakout_8 | 9998.17 | -1.83 | buy /  / momentum_26 AND breakout_8: prior completed bar target 100%; next bar open simulation |
| v1 | momentum_26 + breakout_8 | 10017.04 | 17.04 | buy /  / momentum_26 + breakout_8: prior completed bar target 100%; next bar open simulation |
| v1 | momentum_26 AND reversion_12 | 10000.00 | 0.00 | 대기 /  / 새 신호 대기 |
| v1 | momentum_26 + reversion_12 | 10017.93 | 17.93 | sell /  / momentum_26 + reversion_12: prior completed bar target 50%; next bar open simulation |
| v1 | momentum_26 AND volume_26 | 9997.72 | -2.28 | sell /  / momentum_26 AND volume_26: prior completed bar target 0%; next bar open simulation |
| v1 | momentum_26 + volume_26 | 10016.81 | 16.81 | sell /  / momentum_26 + volume_26: prior completed bar target 50%; next bar open simulation |
| v1 | breakout_8 AND reversion_12 | 10000.00 | 0.00 | 대기 /  / 새 신호 대기 |
| v1 | breakout_8 + reversion_12 | 9999.06 | -0.94 | sell /  / breakout_8 + reversion_12: prior completed bar target 50%; next bar open simulation |
| v1 | breakout_8 AND volume_26 | 10000.00 | 0.00 | 대기 /  / 새 신호 대기 |
| v1 | breakout_8 + volume_26 | 10017.93 | 17.93 | sell /  / breakout_8 + volume_26: prior completed bar target 50%; next bar open simulation |
| v1 | reversion_12 AND volume_26 | 10000.00 | 0.00 | 대기 /  / 새 신호 대기 |
| v1 | reversion_12 + volume_26 | 9998.84 | -1.16 | sell /  / reversion_12 + volume_26: prior completed bar target 0%; next bar open simulation |
| v2 | cash | 10000.00 | 0.00 | 대기 /  / 새 신호 대기 |
| v2 | buy_hold | 10018.63 | 18.63 | buy / partial / 직전 완료 봉 목표 비중 100%; 다음 봉 시가 가정 |
| v2 | trend_8_26 | 9901.03 | -98.97 | buy / partial / 직전 완료 봉 목표 비중 100%; 다음 봉 시가 가정 |
| v2 | momentum_26 | 10012.71 | 12.71 | buy / partial / 직전 완료 봉 목표 비중 100%; 다음 봉 시가 가정 |
| v2 | breakout_8 | 9921.27 | -78.73 | buy / partial / 직전 완료 봉 목표 비중 100%; 다음 봉 시가 가정 |
| v2 | reversion_12 | 9618.62 | -381.38 | sell / filled / 직전 완료 봉 목표 비중 0%; 다음 봉 시가 가정 |
| v2 | volume_26 | 9734.37 | -265.63 | sell / filled / 직전 완료 봉 목표 비중 0%; 다음 봉 시가 가정 |
| v2 | trend_8_26 AND momentum_26 | 9861.55 | -138.45 | buy / partial / 직전 완료 봉 목표 비중 100%; 다음 봉 시가 가정 |
| v2 | trend_8_26 + momentum_26 | 9956.98 | -43.02 | buy / partial / 직전 완료 봉 목표 비중 100%; 다음 봉 시가 가정 |
| v2 | trend_8_26 AND breakout_8 | 9759.10 | -240.90 | buy / partial / 직전 완료 봉 목표 비중 100%; 다음 봉 시가 가정 |
| v2 | trend_8_26 + breakout_8 | 9932.15 | -67.85 | buy / partial / 직전 완료 봉 목표 비중 100%; 다음 봉 시가 가정 |
| v2 | trend_8_26 AND reversion_12 | 9900.10 | -99.90 | sell / filled / 직전 완료 봉 목표 비중 0%; 다음 봉 시가 가정 |
| v2 | trend_8_26 + reversion_12 | 9758.49 | -241.51 | sell / filled / 직전 완료 봉 목표 비중 50%; 다음 봉 시가 가정 |
| v2 | trend_8_26 AND volume_26 | 9995.72 | -4.28 | sell / filled / 직전 완료 봉 목표 비중 0%; 다음 봉 시가 가정 |
| v2 | trend_8_26 + volume_26 | 9837.77 | -162.23 | sell / filled / 직전 완료 봉 목표 비중 50%; 다음 봉 시가 가정 |
| v2 | momentum_26 AND breakout_8 | 9916.12 | -83.88 | buy / partial / 직전 완료 봉 목표 비중 100%; 다음 봉 시가 가정 |
| v2 | momentum_26 + breakout_8 | 9966.92 | -33.08 | buy / partial / 직전 완료 봉 목표 비중 100%; 다음 봉 시가 가정 |
| v2 | momentum_26 AND reversion_12 | 9826.88 | -173.12 | sell / filled / 직전 완료 봉 목표 비중 0%; 다음 봉 시가 가정 |
| v2 | momentum_26 + reversion_12 | 9813.49 | -186.51 | sell / filled / 직전 완료 봉 목표 비중 50%; 다음 봉 시가 가정 |
| v2 | momentum_26 AND volume_26 | 9917.94 | -82.06 | sell / filled / 직전 완료 봉 목표 비중 0%; 다음 봉 시가 가정 |
| v2 | momentum_26 + volume_26 | 9893.23 | -106.77 | sell / filled / 직전 완료 봉 목표 비중 50%; 다음 봉 시가 가정 |
| v2 | breakout_8 AND reversion_12 | 10000.00 | 0.00 | 대기 /  / 새 신호 대기 |
| v2 | breakout_8 + reversion_12 | 9789.15 | -210.85 | sell / filled / 직전 완료 봉 목표 비중 50%; 다음 봉 시가 가정 |
| v2 | breakout_8 AND volume_26 | 9938.59 | -61.41 | sell / filled / 직전 완료 봉 목표 비중 0%; 다음 봉 시가 가정 |
| v2 | breakout_8 + volume_26 | 9848.14 | -151.86 | sell / filled / 직전 완료 봉 목표 비중 50%; 다음 봉 시가 가정 |
| v2 | reversion_12 AND volume_26 | 9762.04 | -237.96 | sell / filled / 직전 완료 봉 목표 비중 0%; 다음 봉 시가 가정 |
| v2 | reversion_12 + volume_26 | 9676.20 | -323.80 | sell / filled / 직전 완료 봉 목표 비중 0%; 다음 봉 시가 가정 |

### 같은 기간의 비용·노출 비교 (사후 연구)

| 전략 | 비용 전 | 비용 후 | 100% 보유 | 같은 평균 노출 보유 | 평균 노출 |
|---|---:|---:|---:|---:|---:|
| cash | 0.00% | 0.00% | 8.13% | 0.00% | 0.00% |
| buy_hold | 8.58% | 8.13% | 8.13% | 8.13% | 100.00% |
| trend_8_26 | 3.32% | -0.51% | 8.13% | 4.73% | 59.47% |
| momentum_26 | 1.39% | -4.40% | 8.13% | 4.67% | 58.68% |
| breakout_8 | 4.85% | -10.24% | 8.13% | 1.66% | 21.32% |
| reversion_12 | -4.05% | -12.52% | 8.13% | 1.83% | 23.42% |
| volume_26 | 5.29% | -3.19% | 8.13% | 0.63% | 8.16% |
| trend_8_26 AND momentum_26 | -0.02% | -5.73% | 8.13% | 4.17% | 52.63% |
| trend_8_26 + momentum_26 | 2.37% | -2.45% | 8.13% | 4.70% | 59.08% |
| trend_8_26 AND breakout_8 | 0.44% | -10.32% | 8.13% | 1.10% | 14.21% |
| trend_8_26 + breakout_8 | 4.11% | -5.08% | 8.13% | 3.18% | 40.40% |
| trend_8_26 AND reversion_12 | -3.39% | -8.52% | 8.13% | 0.55% | 7.11% |
| trend_8_26 + reversion_12 | -0.40% | -6.31% | 8.13% | 3.27% | 41.45% |
| trend_8_26 AND volume_26 | 6.34% | 3.26% | 8.13% | 0.20% | 2.63% |
| trend_8_26 + volume_26 | 4.32% | -1.03% | 8.13% | 2.65% | 33.82% |
| momentum_26 AND breakout_8 | 2.41% | -8.57% | 8.13% | 1.08% | 13.95% |
| momentum_26 + breakout_8 | 3.12% | -6.78% | 8.13% | 3.15% | 40.01% |
| momentum_26 AND reversion_12 | -2.74% | -8.67% | 8.13% | 0.63% | 8.16% |
| momentum_26 + reversion_12 | -1.35% | -8.17% | 8.13% | 3.24% | 41.06% |
| momentum_26 AND volume_26 | 1.86% | -1.92% | 8.13% | 0.24% | 3.16% |
| momentum_26 + volume_26 | 3.35% | -2.36% | 8.13% | 2.62% | 33.42% |
| breakout_8 AND reversion_12 | 0.00% | 0.00% | 8.13% | 0.00% | 0.00% |
| breakout_8 + reversion_12 | 0.33% | -10.82% | 8.13% | 1.75% | 22.38% |
| breakout_8 AND volume_26 | 2.07% | -0.47% | 8.13% | 0.14% | 1.84% |
| breakout_8 + volume_26 | 5.09% | -5.59% | 8.13% | 1.15% | 14.74% |
| reversion_12 AND volume_26 | -2.27% | -5.89% | 8.13% | 0.26% | 3.42% |
| reversion_12 + volume_26 | 0.54% | -7.76% | 8.13% | 1.23% | 15.79% |

동일 구간·초기 자금, 종료 시 청산 비용 포함. 노출 맞춤은 사후 설명용이며 v2 실제 계좌 성과가 아닙니다.
[낙폭 분해·비용 영향·전체 구간](MSFT/comparison.json)

[v1 전체 기록](MSFT/accounts.json) · [v2 전체 기록](MSFT/accounts-v2.json)

## JPM 계좌

| 모델 | 전략 | 평가액 USD | 손익 USD | 최근 매매·이유 |
|---|---|---:|---:|---|
| v1 | cash | 10000.00 | 0.00 | 대기 /  / 새 신호 대기 |
| v1 | buy_hold | 9990.93 | -9.07 | buy /  / buy_hold: prior completed bar target 100%; next bar open simulation |
| v1 | trend_8_26 | 10003.65 | 3.65 | buy /  / trend_8_26: prior completed bar target 100%; next bar open simulation |
| v1 | momentum_26 | 9945.63 | -54.37 | sell /  / momentum_26: prior completed bar target 0%; next bar open simulation |
| v1 | breakout_8 | 10000.00 | 0.00 | 대기 /  / 새 신호 대기 |
| v1 | reversion_12 | 9961.87 | -38.13 | sell /  / reversion_12: prior completed bar target 0%; next bar open simulation |
| v1 | volume_26 | 10000.00 | 0.00 | 대기 /  / 새 신호 대기 |
| v1 | trend_8_26 AND momentum_26 | 10000.00 | 0.00 | 대기 /  / 새 신호 대기 |
| v1 | trend_8_26 + momentum_26 | 9974.56 | -25.44 | sell /  / trend_8_26 + momentum_26: prior completed bar target 50%; next bar open simulation |
| v1 | trend_8_26 AND breakout_8 | 10000.00 | 0.00 | 대기 /  / 새 신호 대기 |
| v1 | trend_8_26 + breakout_8 | 10001.80 | 1.80 | sell /  / trend_8_26 + breakout_8: prior completed bar target 50%; next bar open simulation |
| v1 | trend_8_26 AND reversion_12 | 10000.00 | 0.00 | 대기 /  / 새 신호 대기 |
| v1 | trend_8_26 + reversion_12 | 10002.70 | 2.70 | sell /  / trend_8_26 + reversion_12: prior completed bar target 50%; next bar open simulation |
| v1 | trend_8_26 AND volume_26 | 10000.00 | 0.00 | 대기 /  / 새 신호 대기 |
| v1 | trend_8_26 + volume_26 | 10001.80 | 1.80 | sell /  / trend_8_26 + volume_26: prior completed bar target 50%; next bar open simulation |
| v1 | momentum_26 AND breakout_8 | 10000.00 | 0.00 | 대기 /  / 새 신호 대기 |
| v1 | momentum_26 + breakout_8 | 9972.76 | -27.24 | sell /  / momentum_26 + breakout_8: prior completed bar target 0%; next bar open simulation |
| v1 | momentum_26 AND reversion_12 | 10000.00 | 0.00 | 대기 /  / 새 신호 대기 |
| v1 | momentum_26 + reversion_12 | 9973.65 | -26.35 | sell /  / momentum_26 + reversion_12: prior completed bar target 0%; next bar open simulation |
| v1 | momentum_26 AND volume_26 | 10000.00 | 0.00 | 대기 /  / 새 신호 대기 |
| v1 | momentum_26 + volume_26 | 9972.76 | -27.24 | sell /  / momentum_26 + volume_26: prior completed bar target 0%; next bar open simulation |
| v1 | breakout_8 AND reversion_12 | 10000.00 | 0.00 | 대기 /  / 새 신호 대기 |
| v1 | breakout_8 + reversion_12 | 9980.90 | -19.10 | sell /  / breakout_8 + reversion_12: prior completed bar target 0%; next bar open simulation |
| v1 | breakout_8 AND volume_26 | 10000.00 | 0.00 | 대기 /  / 새 신호 대기 |
| v1 | breakout_8 + volume_26 | 10000.00 | 0.00 | 대기 /  / 새 신호 대기 |
| v1 | reversion_12 AND volume_26 | 10000.00 | 0.00 | 대기 /  / 새 신호 대기 |
| v1 | reversion_12 + volume_26 | 9980.90 | -19.10 | sell /  / reversion_12 + volume_26: prior completed bar target 0%; next bar open simulation |
| v2 | cash | 10000.00 | 0.00 | 대기 /  / 새 신호 대기 |
| v2 | buy_hold | 9986.50 | -13.50 | buy / partial / 직전 완료 봉 목표 비중 100%; 다음 봉 시가 가정 |
| v2 | trend_8_26 | 9917.35 | -82.65 | buy / partial / 직전 완료 봉 목표 비중 100%; 다음 봉 시가 가정 |
| v2 | momentum_26 | 9499.19 | -500.81 | sell / filled / 직전 완료 봉 목표 비중 0%; 다음 봉 시가 가정 |
| v2 | breakout_8 | 9426.01 | -573.99 | sell / filled / 직전 완료 봉 목표 비중 0%; 다음 봉 시가 가정 |
| v2 | reversion_12 | 10005.24 | 5.24 | sell / filled / 직전 완료 봉 목표 비중 0%; 다음 봉 시가 가정 |
| v2 | volume_26 | 9826.70 | -173.30 | sell / filled / 직전 완료 봉 목표 비중 0%; 다음 봉 시가 가정 |
| v2 | trend_8_26 AND momentum_26 | 9936.83 | -63.17 | sell / filled / 직전 완료 봉 목표 비중 0%; 다음 봉 시가 가정 |
| v2 | trend_8_26 + momentum_26 | 9706.52 | -293.48 | sell / filled / 직전 완료 봉 목표 비중 50%; 다음 봉 시가 가정 |
| v2 | trend_8_26 AND breakout_8 | 9420.50 | -579.50 | sell / filled / 직전 완료 봉 목표 비중 0%; 다음 봉 시가 가정 |
| v2 | trend_8_26 + breakout_8 | 9669.14 | -330.86 | sell / filled / 직전 완료 봉 목표 비중 50%; 다음 봉 시가 가정 |
| v2 | trend_8_26 AND reversion_12 | 9981.61 | -18.39 | sell / filled / 직전 완료 봉 목표 비중 0%; 다음 봉 시가 가정 |
| v2 | trend_8_26 + reversion_12 | 9982.22 | -17.78 | sell / filled / 직전 완료 봉 목표 비중 50%; 다음 봉 시가 가정 |
| v2 | trend_8_26 AND volume_26 | 9800.30 | -199.70 | sell / filled / 직전 완료 봉 목표 비중 0%; 다음 봉 시가 가정 |
| v2 | trend_8_26 + volume_26 | 9872.41 | -127.59 | sell / filled / 직전 완료 봉 목표 비중 50%; 다음 봉 시가 가정 |
| v2 | momentum_26 AND breakout_8 | 9407.17 | -592.83 | sell / filled / 직전 완료 봉 목표 비중 0%; 다음 봉 시가 가정 |
| v2 | momentum_26 + breakout_8 | 9483.63 | -516.37 | sell / filled / 직전 완료 봉 목표 비중 0%; 다음 봉 시가 가정 |
| v2 | momentum_26 AND reversion_12 | 9950.76 | -49.24 | sell / filled / 직전 완료 봉 목표 비중 0%; 다음 봉 시가 가정 |
| v2 | momentum_26 + reversion_12 | 9831.62 | -168.38 | sell / filled / 직전 완료 봉 목표 비중 0%; 다음 봉 시가 가정 |
| v2 | momentum_26 AND volume_26 | 9800.30 | -199.70 | sell / filled / 직전 완료 봉 목표 비중 0%; 다음 봉 시가 가정 |
| v2 | momentum_26 + volume_26 | 9723.60 | -276.40 | sell / filled / 직전 완료 봉 목표 비중 0%; 다음 봉 시가 가정 |
| v2 | breakout_8 AND reversion_12 | 10000.00 | 0.00 | 대기 /  / 새 신호 대기 |
| v2 | breakout_8 + reversion_12 | 9731.99 | -268.01 | sell / filled / 직전 완료 봉 목표 비중 0%; 다음 봉 시가 가정 |
| v2 | breakout_8 AND volume_26 | 9893.34 | -106.66 | sell / filled / 직전 완료 봉 목표 비중 0%; 다음 봉 시가 가정 |
| v2 | breakout_8 + volume_26 | 9644.69 | -355.31 | sell / filled / 직전 완료 봉 목표 비중 0%; 다음 봉 시가 가정 |
| v2 | reversion_12 AND volume_26 | 10051.38 | 51.38 | sell / filled / 직전 완료 봉 목표 비중 0%; 다음 봉 시가 가정 |
| v2 | reversion_12 + volume_26 | 9936.72 | -63.28 | sell / filled / 직전 완료 봉 목표 비중 0%; 다음 봉 시가 가정 |

### 같은 기간의 비용·노출 비교 (사후 연구)

| 전략 | 비용 전 | 비용 후 | 100% 보유 | 같은 평균 노출 보유 | 평균 노출 |
|---|---:|---:|---:|---:|---:|
| cash | 0.00% | 0.00% | -1.29% | -0.00% | 0.00% |
| buy_hold | -0.87% | -1.29% | -1.29% | -1.29% | 100.00% |
| trend_8_26 | 0.70% | -2.62% | -1.29% | -0.70% | 53.95% |
| momentum_26 | -1.88% | -7.48% | -1.29% | -0.61% | 46.84% |
| breakout_8 | -3.35% | -17.61% | -1.29% | -0.25% | 19.47% |
| reversion_12 | 4.33% | -9.55% | -1.29% | -0.34% | 26.32% |
| volume_26 | -0.72% | -6.78% | -1.29% | -0.09% | 6.84% |
| trend_8_26 AND momentum_26 | 1.03% | -2.71% | -1.29% | -0.55% | 42.37% |
| trend_8_26 + momentum_26 | -0.59% | -5.08% | -1.29% | -0.65% | 50.40% |
| trend_8_26 AND breakout_8 | -3.43% | -13.42% | -1.29% | -0.16% | 12.37% |
| trend_8_26 + breakout_8 | -1.33% | -10.23% | -1.29% | -0.48% | 36.72% |
| trend_8_26 AND reversion_12 | 2.82% | -3.46% | -1.29% | -0.09% | 6.58% |
| trend_8_26 + reversion_12 | 2.52% | -5.76% | -1.29% | -0.52% | 40.14% |
| trend_8_26 AND volume_26 | -1.19% | -5.26% | -1.29% | -0.05% | 4.21% |
| trend_8_26 + volume_26 | 0.00% | -4.72% | -1.29% | -0.39% | 30.40% |
| momentum_26 AND breakout_8 | -2.23% | -11.98% | -1.29% | -0.15% | 11.84% |
| momentum_26 + breakout_8 | -2.60% | -12.49% | -1.29% | -0.43% | 33.16% |
| momentum_26 AND reversion_12 | 2.89% | -3.80% | -1.29% | -0.07% | 5.53% |
| momentum_26 + reversion_12 | 1.20% | -7.36% | -1.29% | -0.47% | 36.58% |
| momentum_26 AND volume_26 | -0.41% | -3.30% | -1.29% | -0.04% | 2.89% |
| momentum_26 + volume_26 | -1.28% | -6.54% | -1.29% | -0.35% | 26.85% |
| breakout_8 AND reversion_12 | 0.00% | 0.00% | -1.29% | -0.00% | 0.00% |
| breakout_8 + reversion_12 | 0.44% | -12.40% | -1.29% | -0.30% | 22.90% |
| breakout_8 AND volume_26 | -1.13% | -2.78% | -1.29% | -0.01% | 1.05% |
| breakout_8 + volume_26 | -2.03% | -11.25% | -1.29% | -0.17% | 13.16% |
| reversion_12 AND volume_26 | 1.25% | -2.10% | -1.29% | -0.04% | 3.42% |
| reversion_12 + volume_26 | 1.78% | -7.41% | -1.29% | -0.22% | 16.58% |

동일 구간·초기 자금, 종료 시 청산 비용 포함. 노출 맞춤은 사후 설명용이며 v2 실제 계좌 성과가 아닙니다.
[낙폭 분해·비용 영향·전체 구간](JPM/comparison.json)

[v1 전체 기록](JPM/accounts.json) · [v2 전체 기록](JPM/accounts-v2.json)

## XOM 계좌

| 모델 | 전략 | 평가액 USD | 손익 USD | 최근 매매·이유 |
|---|---|---:|---:|---|
| v1 | cash | 10000.00 | 0.00 | 대기 /  / 새 신호 대기 |
| v1 | buy_hold | 9948.72 | -51.28 | buy /  / buy_hold: prior completed bar target 100%; next bar open simulation |
| v1 | trend_8_26 | 10000.00 | 0.00 | 대기 /  / 새 신호 대기 |
| v1 | momentum_26 | 10000.00 | 0.00 | 대기 /  / 새 신호 대기 |
| v1 | breakout_8 | 10000.00 | 0.00 | 대기 /  / 새 신호 대기 |
| v1 | reversion_12 | 9994.58 | -5.42 | sell /  / reversion_12: prior completed bar target 0%; next bar open simulation |
| v1 | volume_26 | 10000.00 | 0.00 | 대기 /  / 새 신호 대기 |
| v1 | trend_8_26 AND momentum_26 | 10000.00 | 0.00 | 대기 /  / 새 신호 대기 |
| v1 | trend_8_26 + momentum_26 | 10000.00 | 0.00 | 대기 /  / 새 신호 대기 |
| v1 | trend_8_26 AND breakout_8 | 10000.00 | 0.00 | 대기 /  / 새 신호 대기 |
| v1 | trend_8_26 + breakout_8 | 10000.00 | 0.00 | 대기 /  / 새 신호 대기 |
| v1 | trend_8_26 AND reversion_12 | 10000.00 | 0.00 | 대기 /  / 새 신호 대기 |
| v1 | trend_8_26 + reversion_12 | 9997.28 | -2.72 | sell /  / trend_8_26 + reversion_12: prior completed bar target 0%; next bar open simulation |
| v1 | trend_8_26 AND volume_26 | 10000.00 | 0.00 | 대기 /  / 새 신호 대기 |
| v1 | trend_8_26 + volume_26 | 10000.00 | 0.00 | 대기 /  / 새 신호 대기 |
| v1 | momentum_26 AND breakout_8 | 10000.00 | 0.00 | 대기 /  / 새 신호 대기 |
| v1 | momentum_26 + breakout_8 | 10000.00 | 0.00 | 대기 /  / 새 신호 대기 |
| v1 | momentum_26 AND reversion_12 | 10000.00 | 0.00 | 대기 /  / 새 신호 대기 |
| v1 | momentum_26 + reversion_12 | 9997.28 | -2.72 | sell /  / momentum_26 + reversion_12: prior completed bar target 0%; next bar open simulation |
| v1 | momentum_26 AND volume_26 | 10000.00 | 0.00 | 대기 /  / 새 신호 대기 |
| v1 | momentum_26 + volume_26 | 10000.00 | 0.00 | 대기 /  / 새 신호 대기 |
| v1 | breakout_8 AND reversion_12 | 10000.00 | 0.00 | 대기 /  / 새 신호 대기 |
| v1 | breakout_8 + reversion_12 | 9997.28 | -2.72 | sell /  / breakout_8 + reversion_12: prior completed bar target 0%; next bar open simulation |
| v1 | breakout_8 AND volume_26 | 10000.00 | 0.00 | 대기 /  / 새 신호 대기 |
| v1 | breakout_8 + volume_26 | 10000.00 | 0.00 | 대기 /  / 새 신호 대기 |
| v1 | reversion_12 AND volume_26 | 10000.00 | 0.00 | 대기 /  / 새 신호 대기 |
| v1 | reversion_12 + volume_26 | 9997.28 | -2.72 | sell /  / reversion_12 + volume_26: prior completed bar target 0%; next bar open simulation |
| v2 | cash | 10000.00 | 0.00 | 대기 /  / 새 신호 대기 |
| v2 | buy_hold | 10197.28 | 197.28 | buy / partial / 직전 완료 봉 목표 비중 100%; 다음 봉 시가 가정 |
| v2 | trend_8_26 | 10096.25 | 96.25 | sell / filled / 직전 완료 봉 목표 비중 0%; 다음 봉 시가 가정 |
| v2 | momentum_26 | 10172.64 | 172.64 | sell / filled / 직전 완료 봉 목표 비중 0%; 다음 봉 시가 가정 |
| v2 | breakout_8 | 9471.02 | -528.98 | sell / filled / 직전 완료 봉 목표 비중 0%; 다음 봉 시가 가정 |
| v2 | reversion_12 | 9826.80 | -173.20 | sell / filled / 직전 완료 봉 목표 비중 0%; 다음 봉 시가 가정 |
| v2 | volume_26 | 9908.04 | -91.96 | sell / filled / 직전 완료 봉 목표 비중 0%; 다음 봉 시가 가정 |
| v2 | trend_8_26 AND momentum_26 | 10103.74 | 103.74 | sell / filled / 직전 완료 봉 목표 비중 0%; 다음 봉 시가 가정 |
| v2 | trend_8_26 + momentum_26 | 10134.41 | 134.41 | sell / filled / 직전 완료 봉 목표 비중 0%; 다음 봉 시가 가정 |
| v2 | trend_8_26 AND breakout_8 | 9453.73 | -546.27 | sell / filled / 직전 완료 봉 목표 비중 0%; 다음 봉 시가 가정 |
| v2 | trend_8_26 + breakout_8 | 9799.57 | -200.43 | sell / filled / 직전 완료 봉 목표 비중 0%; 다음 봉 시가 가정 |
| v2 | trend_8_26 AND reversion_12 | 9839.70 | -160.30 | sell / filled / 직전 완료 봉 목표 비중 0%; 다음 봉 시가 가정 |
| v2 | trend_8_26 + reversion_12 | 9960.60 | -39.40 | sell / filled / 직전 완료 봉 목표 비중 0%; 다음 봉 시가 가정 |
| v2 | trend_8_26 AND volume_26 | 9895.61 | -104.39 | sell / filled / 직전 완료 봉 목표 비중 0%; 다음 봉 시가 가정 |
| v2 | trend_8_26 + volume_26 | 10001.66 | 1.66 | sell / filled / 직전 완료 봉 목표 비중 0%; 다음 봉 시가 가정 |
| v2 | momentum_26 AND breakout_8 | 9471.02 | -528.98 | sell / filled / 직전 완료 봉 목표 비중 0%; 다음 봉 시가 가정 |
| v2 | momentum_26 + breakout_8 | 9816.10 | -183.90 | sell / filled / 직전 완료 봉 목표 비중 0%; 다음 봉 시가 가정 |
| v2 | momentum_26 AND reversion_12 | 9800.13 | -199.87 | sell / filled / 직전 완료 봉 목표 비중 0%; 다음 봉 시가 가정 |
| v2 | momentum_26 + reversion_12 | 9998.24 | -1.76 | sell / filled / 직전 완료 봉 목표 비중 0%; 다음 봉 시가 가정 |
| v2 | momentum_26 AND volume_26 | 9957.96 | -42.04 | sell / filled / 직전 완료 봉 목표 비중 0%; 다음 봉 시가 가정 |
| v2 | momentum_26 + volume_26 | 10060.52 | 60.52 | sell / filled / 직전 완료 봉 목표 비중 0%; 다음 봉 시가 가정 |
| v2 | breakout_8 AND reversion_12 | 10000.00 | 0.00 | 대기 /  / 새 신호 대기 |
| v2 | breakout_8 + reversion_12 | 9647.08 | -352.92 | sell / filled / 직전 완료 봉 목표 비중 0%; 다음 봉 시가 가정 |
| v2 | breakout_8 AND volume_26 | 9970.25 | -29.75 | sell / filled / 직전 완료 봉 목표 비중 0%; 다음 봉 시가 가정 |
| v2 | breakout_8 + volume_26 | 9707.34 | -292.66 | sell / filled / 직전 완료 봉 목표 비중 0%; 다음 봉 시가 가정 |
| v2 | reversion_12 AND volume_26 | 9949.87 | -50.13 | sell / filled / 직전 완료 봉 목표 비중 0%; 다음 봉 시가 가정 |
| v2 | reversion_12 + volume_26 | 9867.23 | -132.77 | sell / filled / 직전 완료 봉 목표 비중 0%; 다음 봉 시가 가정 |

### 같은 기간의 비용·노출 비교 (사후 연구)

| 전략 | 비용 전 | 비용 후 | 100% 보유 | 같은 평균 노출 보유 | 평균 노출 |
|---|---:|---:|---:|---:|---:|
| cash | 0.00% | 0.00% | 7.32% | 0.00% | 0.00% |
| buy_hold | 7.77% | 7.32% | 7.32% | 7.32% | 100.00% |
| trend_8_26 | 1.00% | -3.16% | 7.32% | 4.56% | 62.89% |
| momentum_26 | -0.87% | -8.09% | 7.32% | 5.05% | 69.47% |
| breakout_8 | -3.59% | -20.53% | 7.32% | 1.64% | 22.89% |
| reversion_12 | 5.79% | -4.36% | 7.32% | 1.51% | 21.05% |
| volume_26 | 4.95% | -2.69% | 7.32% | 0.36% | 5.00% |
| trend_8_26 AND momentum_26 | -0.45% | -4.95% | 7.32% | 4.17% | 57.63% |
| trend_8_26 + momentum_26 | 0.07% | -5.45% | 7.32% | 4.80% | 66.19% |
| trend_8_26 AND breakout_8 | -1.20% | -14.70% | 7.32% | 1.28% | 17.89% |
| trend_8_26 + breakout_8 | -1.30% | -12.07% | 7.32% | 3.10% | 42.90% |
| trend_8_26 AND reversion_12 | 1.89% | -3.93% | 7.32% | 0.58% | 8.16% |
| trend_8_26 + reversion_12 | 3.39% | -3.56% | 7.32% | 3.03% | 41.98% |
| trend_8_26 AND volume_26 | 2.54% | -1.67% | 7.32% | 0.19% | 2.63% |
| trend_8_26 + volume_26 | 2.97% | -2.52% | 7.32% | 2.44% | 33.95% |
| momentum_26 AND breakout_8 | -3.06% | -18.40% | 7.32% | 1.47% | 20.53% |
| momentum_26 + breakout_8 | -2.21% | -14.52% | 7.32% | 3.34% | 46.19% |
| momentum_26 AND reversion_12 | 2.27% | -4.38% | 7.32% | 0.64% | 8.95% |
| momentum_26 + reversion_12 | 2.43% | -4.65% | 7.32% | 3.27% | 45.27% |
| momentum_26 AND volume_26 | 2.42% | -1.79% | 7.32% | 0.19% | 2.63% |
| momentum_26 + volume_26 | 2.02% | -4.02% | 7.32% | 2.68% | 37.24% |
| breakout_8 AND reversion_12 | 0.00% | 0.00% | 7.32% | 0.00% | 0.00% |
| breakout_8 + reversion_12 | 1.01% | -12.45% | 7.32% | 1.58% | 21.98% |
| breakout_8 AND volume_26 | 0.60% | -0.66% | 7.32% | 0.06% | 0.79% |
| breakout_8 + volume_26 | 0.60% | -10.94% | 7.32% | 1.00% | 13.96% |
| reversion_12 AND volume_26 | 1.84% | -1.11% | 7.32% | 0.13% | 1.84% |
| reversion_12 + volume_26 | 5.38% | -2.92% | 7.32% | 0.93% | 13.03% |

동일 구간·초기 자금, 종료 시 청산 비용 포함. 노출 맞춤은 사후 설명용이며 v2 실제 계좌 성과가 아닙니다.
[낙폭 분해·비용 영향·전체 구간](XOM/comparison.json)

[v1 전체 기록](XOM/accounts.json) · [v2 전체 기록](XOM/accounts-v2.json)

## JNJ 계좌

| 모델 | 전략 | 평가액 USD | 손익 USD | 최근 매매·이유 |
|---|---|---:|---:|---|
| v1 | cash | 10000.00 | 0.00 | 대기 /  / 새 신호 대기 |
| v1 | buy_hold | 9895.73 | -104.27 | buy /  / buy_hold: prior completed bar target 100%; next bar open simulation |
| v1 | trend_8_26 | 9895.73 | -104.27 | buy /  / trend_8_26: prior completed bar target 100%; next bar open simulation |
| v1 | momentum_26 | 9895.73 | -104.27 | buy /  / momentum_26: prior completed bar target 100%; next bar open simulation |
| v1 | breakout_8 | 10000.00 | 0.00 | 대기 /  / 새 신호 대기 |
| v1 | reversion_12 | 9946.48 | -53.52 | buy /  / reversion_12: prior completed bar target 100%; next bar open simulation |
| v1 | volume_26 | 10000.00 | 0.00 | 대기 /  / 새 신호 대기 |
| v1 | trend_8_26 AND momentum_26 | 9895.73 | -104.27 | buy /  / trend_8_26 AND momentum_26: prior completed bar target 100%; next bar open simulation |
| v1 | trend_8_26 + momentum_26 | 9895.73 | -104.27 | buy /  / trend_8_26 + momentum_26: prior completed bar target 100%; next bar open simulation |
| v1 | trend_8_26 AND breakout_8 | 10000.00 | 0.00 | 대기 /  / 새 신호 대기 |
| v1 | trend_8_26 + breakout_8 | 9947.74 | -52.26 | sell /  / trend_8_26 + breakout_8: prior completed bar target 50%; next bar open simulation |
| v1 | trend_8_26 AND reversion_12 | 9946.48 | -53.52 | buy /  / trend_8_26 AND reversion_12: prior completed bar target 100%; next bar open simulation |
| v1 | trend_8_26 + reversion_12 | 9921.09 | -78.91 | buy /  / trend_8_26 + reversion_12: prior completed bar target 100%; next bar open simulation |
| v1 | trend_8_26 AND volume_26 | 10000.00 | 0.00 | 대기 /  / 새 신호 대기 |
| v1 | trend_8_26 + volume_26 | 9947.74 | -52.26 | sell /  / trend_8_26 + volume_26: prior completed bar target 50%; next bar open simulation |
| v1 | momentum_26 AND breakout_8 | 10000.00 | 0.00 | 대기 /  / 새 신호 대기 |
| v1 | momentum_26 + breakout_8 | 9947.74 | -52.26 | sell /  / momentum_26 + breakout_8: prior completed bar target 50%; next bar open simulation |
| v1 | momentum_26 AND reversion_12 | 9946.48 | -53.52 | buy /  / momentum_26 AND reversion_12: prior completed bar target 100%; next bar open simulation |
| v1 | momentum_26 + reversion_12 | 9921.09 | -78.91 | buy /  / momentum_26 + reversion_12: prior completed bar target 100%; next bar open simulation |
| v1 | momentum_26 AND volume_26 | 10000.00 | 0.00 | 대기 /  / 새 신호 대기 |
| v1 | momentum_26 + volume_26 | 9947.74 | -52.26 | sell /  / momentum_26 + volume_26: prior completed bar target 50%; next bar open simulation |
| v1 | breakout_8 AND reversion_12 | 10000.00 | 0.00 | 대기 /  / 새 신호 대기 |
| v1 | breakout_8 + reversion_12 | 9973.19 | -26.81 | buy /  / breakout_8 + reversion_12: prior completed bar target 50%; next bar open simulation |
| v1 | breakout_8 AND volume_26 | 10000.00 | 0.00 | 대기 /  / 새 신호 대기 |
| v1 | breakout_8 + volume_26 | 10000.00 | 0.00 | 대기 /  / 새 신호 대기 |
| v1 | reversion_12 AND volume_26 | 10000.00 | 0.00 | 대기 /  / 새 신호 대기 |
| v1 | reversion_12 + volume_26 | 9973.19 | -26.81 | buy /  / reversion_12 + volume_26: prior completed bar target 50%; next bar open simulation |
| v2 | cash | 10000.00 | 0.00 | 대기 /  / 새 신호 대기 |
| v2 | buy_hold | 9783.91 | -216.09 | 중단: 손실 한도 / buy / partial / 직전 완료 봉 목표 비중 100%; 다음 봉 시가 가정 |
| v2 | trend_8_26 | 9783.91 | -216.09 | 중단: 손실 한도 / buy / partial / 직전 완료 봉 목표 비중 100%; 다음 봉 시가 가정 |
| v2 | momentum_26 | 9783.91 | -216.09 | 중단: 손실 한도 / buy / partial / 직전 완료 봉 목표 비중 100%; 다음 봉 시가 가정 |
| v2 | breakout_8 | 9343.39 | -656.61 | 중단: 손실 한도 / sell / filled / 직전 완료 봉 목표 비중 0%; 다음 봉 시가 가정 |
| v2 | reversion_12 | 9833.59 | -166.41 | buy / partial / 직전 완료 봉 목표 비중 100%; 다음 봉 시가 가정 |
| v2 | volume_26 | 9791.36 | -208.64 | sell / filled / 직전 완료 봉 목표 비중 0%; 다음 봉 시가 가정 |
| v2 | trend_8_26 AND momentum_26 | 9783.91 | -216.09 | 중단: 손실 한도 / buy / partial / 직전 완료 봉 목표 비중 100%; 다음 봉 시가 가정 |
| v2 | trend_8_26 + momentum_26 | 9783.91 | -216.09 | 중단: 손실 한도 / buy / partial / 직전 완료 봉 목표 비중 100%; 다음 봉 시가 가정 |
| v2 | trend_8_26 AND breakout_8 | 9419.39 | -580.61 | 중단: 손실 한도 / sell / filled / 직전 완료 봉 목표 비중 0%; 다음 봉 시가 가정 |
| v2 | trend_8_26 + breakout_8 | 9618.28 | -381.72 | sell / filled / 직전 완료 봉 목표 비중 50%; 다음 봉 시가 가정 |
| v2 | trend_8_26 AND reversion_12 | 10079.44 | 79.44 | buy / partial / 직전 완료 봉 목표 비중 100%; 다음 봉 시가 가정 |
| v2 | trend_8_26 + reversion_12 | 9732.92 | -267.08 | 중단: 손실 한도 / sell / filled / 직전 완료 봉 목표 비중 0%; 다음 봉 시가 가정 |
| v2 | trend_8_26 AND volume_26 | 9870.71 | -129.29 | sell / filled / 직전 완료 봉 목표 비중 0%; 다음 봉 시가 가정 |
| v2 | trend_8_26 + volume_26 | 9865.73 | -134.27 | 중단: 손실 한도 / buy / filled / 직전 완료 봉 목표 비중 50%; 다음 봉 시가 가정 |
| v2 | momentum_26 AND breakout_8 | 9598.70 | -401.30 | sell / filled / 직전 완료 봉 목표 비중 0%; 다음 봉 시가 가정 |
| v2 | momentum_26 + breakout_8 | 9620.67 | -379.33 | sell / filled / 직전 완료 봉 목표 비중 50%; 다음 봉 시가 가정 |
| v2 | momentum_26 AND reversion_12 | 10079.44 | 79.44 | buy / partial / 직전 완료 봉 목표 비중 100%; 다음 봉 시가 가정 |
| v2 | momentum_26 + reversion_12 | 9732.92 | -267.08 | 중단: 손실 한도 / sell / filled / 직전 완료 봉 목표 비중 0%; 다음 봉 시가 가정 |
| v2 | momentum_26 AND volume_26 | 9920.93 | -79.07 | sell / filled / 직전 완료 봉 목표 비중 0%; 다음 봉 시가 가정 |
| v2 | momentum_26 + volume_26 | 9865.73 | -134.27 | 중단: 손실 한도 / buy / filled / 직전 완료 봉 목표 비중 50%; 다음 봉 시가 가정 |
| v2 | breakout_8 AND reversion_12 | 10000.00 | 0.00 | 대기 /  / 새 신호 대기 |
| v2 | breakout_8 + reversion_12 | 9651.77 | -348.23 | buy / filled / 직전 완료 봉 목표 비중 50%; 다음 봉 시가 가정 |
| v2 | breakout_8 AND volume_26 | 9814.17 | -185.83 | sell / filled / 직전 완료 봉 목표 비중 0%; 다음 봉 시가 가정 |
| v2 | breakout_8 + volume_26 | 9610.69 | -389.31 | sell / filled / 직전 완료 봉 목표 비중 0%; 다음 봉 시가 가정 |
| v2 | reversion_12 AND volume_26 | 9886.24 | -113.76 | sell / filled / 직전 완료 봉 목표 비중 0%; 다음 봉 시가 가정 |
| v2 | reversion_12 + volume_26 | 9833.38 | -166.62 | buy / filled / 직전 완료 봉 목표 비중 50%; 다음 봉 시가 가정 |

### 같은 기간의 비용·노출 비교 (사후 연구)

| 전략 | 비용 전 | 비용 후 | 100% 보유 | 같은 평균 노출 보유 | 평균 노출 |
|---|---:|---:|---:|---:|---:|
| cash | 0.00% | 0.00% | -6.05% | -0.00% | 0.00% |
| buy_hold | -5.65% | -6.05% | -6.05% | -6.05% | 100.00% |
| trend_8_26 | 3.26% | 0.69% | -6.05% | -2.94% | 47.37% |
| momentum_26 | 0.80% | -2.93% | -6.05% | -2.89% | 46.58% |
| breakout_8 | -0.32% | -17.14% | -6.05% | -1.34% | 21.32% |
| reversion_12 | -6.82% | -16.11% | -6.05% | -1.83% | 29.21% |
| volume_26 | -1.33% | -8.13% | -6.05% | -0.43% | 6.84% |
| trend_8_26 AND momentum_26 | 3.12% | -0.29% | -6.05% | -2.70% | 43.42% |
| trend_8_26 + momentum_26 | 2.03% | -1.13% | -6.05% | -2.91% | 46.98% |
| trend_8_26 AND breakout_8 | 0.73% | -11.94% | -6.05% | -0.98% | 15.53% |
| trend_8_26 + breakout_8 | 1.48% | -8.44% | -6.05% | -2.14% | 34.35% |
| trend_8_26 AND reversion_12 | 1.50% | -1.85% | -6.05% | -0.28% | 4.47% |
| trend_8_26 + reversion_12 | -1.87% | -7.50% | -6.05% | -2.38% | 38.29% |
| trend_8_26 AND volume_26 | 1.59% | -0.53% | -6.05% | -0.10% | 1.58% |
| trend_8_26 + volume_26 | 0.97% | -3.20% | -6.05% | -1.70% | 27.11% |
| momentum_26 AND breakout_8 | 2.15% | -9.94% | -6.05% | -0.93% | 14.74% |
| momentum_26 + breakout_8 | 0.27% | -10.11% | -6.05% | -2.12% | 33.95% |
| momentum_26 AND reversion_12 | -0.09% | -3.80% | -6.05% | -0.33% | 5.26% |
| momentum_26 + reversion_12 | -3.05% | -9.18% | -6.05% | -2.36% | 37.90% |
| momentum_26 AND volume_26 | 0.88% | -1.21% | -6.05% | -0.10% | 1.58% |
| momentum_26 + volume_26 | -0.24% | -4.96% | -6.05% | -1.67% | 26.71% |
| breakout_8 AND reversion_12 | 0.00% | 0.00% | -6.05% | -0.00% | 0.00% |
| breakout_8 + reversion_12 | -3.60% | -16.10% | -6.05% | -1.58% | 25.27% |
| breakout_8 AND volume_26 | -0.11% | -2.19% | -6.05% | -0.10% | 1.58% |
| breakout_8 + volume_26 | -0.82% | -12.02% | -6.05% | -0.89% | 14.09% |
| reversion_12 AND volume_26 | -2.65% | -5.47% | -6.05% | -0.18% | 2.89% |
| reversion_12 + volume_26 | -4.10% | -11.47% | -6.05% | -1.13% | 18.03% |

동일 구간·초기 자금, 종료 시 청산 비용 포함. 노출 맞춤은 사후 설명용이며 v2 실제 계좌 성과가 아닙니다.
[낙폭 분해·비용 영향·전체 구간](JNJ/comparison.json)

[v1 전체 기록](JNJ/accounts.json) · [v2 전체 기록](JNJ/accounts-v2.json)

## CAT 계좌

| 모델 | 전략 | 평가액 USD | 손익 USD | 최근 매매·이유 |
|---|---|---:|---:|---|
| v1 | cash | 10000.00 | 0.00 | 대기 /  / 새 신호 대기 |
| v1 | buy_hold | 9943.39 | -56.61 | buy /  / buy_hold: prior completed bar target 100%; next bar open simulation |
| v1 | trend_8_26 | 10000.00 | 0.00 | 대기 /  / 새 신호 대기 |
| v1 | momentum_26 | 10000.00 | 0.00 | 대기 /  / 새 신호 대기 |
| v1 | breakout_8 | 10000.00 | 0.00 | 대기 /  / 새 신호 대기 |
| v1 | reversion_12 | 10000.00 | 0.00 | 대기 /  / 새 신호 대기 |
| v1 | volume_26 | 9965.26 | -34.74 | sell /  / volume_26: prior completed bar target 0%; next bar open simulation |
| v1 | trend_8_26 AND momentum_26 | 10000.00 | 0.00 | 대기 /  / 새 신호 대기 |
| v1 | trend_8_26 + momentum_26 | 10000.00 | 0.00 | 대기 /  / 새 신호 대기 |
| v1 | trend_8_26 AND breakout_8 | 10000.00 | 0.00 | 대기 /  / 새 신호 대기 |
| v1 | trend_8_26 + breakout_8 | 10000.00 | 0.00 | 대기 /  / 새 신호 대기 |
| v1 | trend_8_26 AND reversion_12 | 10000.00 | 0.00 | 대기 /  / 새 신호 대기 |
| v1 | trend_8_26 + reversion_12 | 10000.00 | 0.00 | 대기 /  / 새 신호 대기 |
| v1 | trend_8_26 AND volume_26 | 10000.00 | 0.00 | 대기 /  / 새 신호 대기 |
| v1 | trend_8_26 + volume_26 | 9982.60 | -17.40 | sell /  / trend_8_26 + volume_26: prior completed bar target 0%; next bar open simulation |
| v1 | momentum_26 AND breakout_8 | 10000.00 | 0.00 | 대기 /  / 새 신호 대기 |
| v1 | momentum_26 + breakout_8 | 10000.00 | 0.00 | 대기 /  / 새 신호 대기 |
| v1 | momentum_26 AND reversion_12 | 10000.00 | 0.00 | 대기 /  / 새 신호 대기 |
| v1 | momentum_26 + reversion_12 | 10000.00 | 0.00 | 대기 /  / 새 신호 대기 |
| v1 | momentum_26 AND volume_26 | 10000.00 | 0.00 | 대기 /  / 새 신호 대기 |
| v1 | momentum_26 + volume_26 | 9982.60 | -17.40 | sell /  / momentum_26 + volume_26: prior completed bar target 0%; next bar open simulation |
| v1 | breakout_8 AND reversion_12 | 10000.00 | 0.00 | 대기 /  / 새 신호 대기 |
| v1 | breakout_8 + reversion_12 | 10000.00 | 0.00 | 대기 /  / 새 신호 대기 |
| v1 | breakout_8 AND volume_26 | 10000.00 | 0.00 | 대기 /  / 새 신호 대기 |
| v1 | breakout_8 + volume_26 | 9982.60 | -17.40 | sell /  / breakout_8 + volume_26: prior completed bar target 0%; next bar open simulation |
| v1 | reversion_12 AND volume_26 | 10000.00 | 0.00 | 대기 /  / 새 신호 대기 |
| v1 | reversion_12 + volume_26 | 9982.60 | -17.40 | sell /  / reversion_12 + volume_26: prior completed bar target 0%; next bar open simulation |
| v2 | cash | 10000.00 | 0.00 | 대기 /  / 새 신호 대기 |
| v2 | buy_hold | 9090.27 | -909.73 | 중단: 손실 한도 / buy / partial / 직전 완료 봉 목표 비중 100%; 다음 봉 시가 가정 |
| v2 | trend_8_26 | 9941.61 | -58.39 | sell / filled / 직전 완료 봉 목표 비중 0%; 다음 봉 시가 가정 |
| v2 | momentum_26 | 10014.59 | 14.59 | sell / filled / 직전 완료 봉 목표 비중 0%; 다음 봉 시가 가정 |
| v2 | breakout_8 | 9806.46 | -193.54 | sell / filled / 직전 완료 봉 목표 비중 0%; 다음 봉 시가 가정 |
| v2 | reversion_12 | 8963.32 | -1036.68 | 중단: 손실 한도 / buy / partial / 직전 완료 봉 목표 비중 100%; 다음 봉 시가 가정 |
| v2 | volume_26 | 9219.66 | -780.34 | 중단: 손실 한도 / buy / partial / 직전 완료 봉 목표 비중 100%; 다음 봉 시가 가정 |
| v2 | trend_8_26 AND momentum_26 | 10043.59 | 43.59 | sell / filled / 직전 완료 봉 목표 비중 0%; 다음 봉 시가 가정 |
| v2 | trend_8_26 + momentum_26 | 9978.08 | -21.92 | sell / filled / 직전 완료 봉 목표 비중 0%; 다음 봉 시가 가정 |
| v2 | trend_8_26 AND breakout_8 | 9976.12 | -23.88 | sell / filled / 직전 완료 봉 목표 비중 0%; 다음 봉 시가 가정 |
| v2 | trend_8_26 + breakout_8 | 9873.91 | -126.09 | sell / filled / 직전 완료 봉 목표 비중 0%; 다음 봉 시가 가정 |
| v2 | trend_8_26 AND reversion_12 | 9815.07 | -184.93 | sell / filled / 직전 완료 봉 목표 비중 0%; 다음 봉 시가 가정 |
| v2 | trend_8_26 + reversion_12 | 9636.65 | -363.35 | sell / filled / 직전 완료 봉 목표 비중 0%; 다음 봉 시가 가정 |
| v2 | trend_8_26 AND volume_26 | 10035.44 | 35.44 | sell / filled / 직전 완료 봉 목표 비중 0%; 다음 봉 시가 가정 |
| v2 | trend_8_26 + volume_26 | 9641.27 | -358.73 | sell / filled / 직전 완료 봉 목표 비중 0%; 다음 봉 시가 가정 |
| v2 | momentum_26 AND breakout_8 | 9977.43 | -22.57 | sell / filled / 직전 완료 봉 목표 비중 0%; 다음 봉 시가 가정 |
| v2 | momentum_26 + breakout_8 | 9910.06 | -89.94 | sell / filled / 직전 완료 봉 목표 비중 0%; 다음 봉 시가 가정 |
| v2 | momentum_26 AND reversion_12 | 9874.73 | -125.27 | sell / filled / 직전 완료 봉 목표 비중 0%; 다음 봉 시가 가정 |
| v2 | momentum_26 + reversion_12 | 9671.92 | -328.08 | sell / filled / 직전 완료 봉 목표 비중 0%; 다음 봉 시가 가정 |
| v2 | momentum_26 AND volume_26 | 10048.78 | 48.78 | sell / filled / 직전 완료 봉 목표 비중 0%; 다음 봉 시가 가정 |
| v2 | momentum_26 + volume_26 | 9696.91 | -303.09 | sell / filled / 직전 완료 봉 목표 비중 0%; 다음 봉 시가 가정 |
| v2 | breakout_8 AND reversion_12 | 10000.00 | 0.00 | 대기 /  / 새 신호 대기 |
| v2 | breakout_8 + reversion_12 | 9610.18 | -389.82 | 중단: 손실 한도 / sell / filled / 직전 완료 봉 목표 비중 0%; 다음 봉 시가 가정 |
| v2 | breakout_8 AND volume_26 | 9998.69 | -1.31 | sell / filled / 직전 완료 봉 목표 비중 0%; 다음 봉 시가 가정 |
| v2 | breakout_8 + volume_26 | 9595.66 | -404.34 | sell / filled / 직전 완료 봉 목표 비중 0%; 다음 봉 시가 가정 |
| v2 | reversion_12 AND volume_26 | 9155.88 | -844.12 | 중단: 손실 한도 / buy / partial / 직전 완료 봉 목표 비중 100%; 다음 봉 시가 가정 |
| v2 | reversion_12 + volume_26 | 9343.88 | -656.12 | 중단: 손실 한도 / sell / filled / 직전 완료 봉 목표 비중 50%; 다음 봉 시가 가정 |

### 같은 기간의 비용·노출 비교 (사후 연구)

| 전략 | 비용 전 | 비용 후 | 100% 보유 | 같은 평균 노출 보유 | 평균 노출 |
|---|---:|---:|---:|---:|---:|
| cash | 0.00% | 0.00% | -9.82% | -0.00% | 0.00% |
| buy_hold | -9.44% | -9.82% | -9.82% | -9.82% | 100.00% |
| trend_8_26 | 0.27% | -3.04% | -9.82% | -5.18% | 52.89% |
| momentum_26 | -4.02% | -9.50% | -9.82% | -5.02% | 51.32% |
| breakout_8 | -3.57% | -16.40% | -9.82% | -1.46% | 15.00% |
| reversion_12 | -4.23% | -15.21% | -9.82% | -2.49% | 25.53% |
| volume_26 | -2.55% | -10.03% | -9.82% | -0.82% | 8.42% |
| trend_8_26 AND momentum_26 | -1.32% | -5.77% | -9.82% | -4.45% | 45.53% |
| trend_8_26 + momentum_26 | -1.88% | -6.31% | -9.82% | -5.10% | 52.11% |
| trend_8_26 AND breakout_8 | -1.46% | -9.02% | -9.82% | -0.77% | 7.89% |
| trend_8_26 + breakout_8 | -1.63% | -9.75% | -9.82% | -3.32% | 33.95% |
| trend_8_26 AND reversion_12 | 0.78% | -5.38% | -9.82% | -0.69% | 7.11% |
| trend_8_26 + reversion_12 | -1.94% | -8.73% | -9.82% | -3.84% | 39.22% |
| trend_8_26 AND volume_26 | 2.63% | -0.76% | -9.82% | -0.28% | 2.89% |
| trend_8_26 + volume_26 | -1.09% | -6.37% | -9.82% | -3.00% | 30.66% |
| momentum_26 AND breakout_8 | -2.95% | -11.51% | -9.82% | -0.90% | 9.21% |
| momentum_26 + breakout_8 | -3.75% | -12.99% | -9.82% | -3.24% | 33.16% |
| momentum_26 AND reversion_12 | -3.04% | -8.96% | -9.82% | -0.56% | 5.79% |
| momentum_26 + reversion_12 | -4.07% | -11.46% | -9.82% | -3.76% | 38.43% |
| momentum_26 AND volume_26 | 1.58% | -0.53% | -9.82% | -0.15% | 1.58% |
| momentum_26 + volume_26 | -3.23% | -8.78% | -9.82% | -2.92% | 29.87% |
| breakout_8 AND reversion_12 | 0.00% | 0.00% | -9.82% | -0.00% | 0.00% |
| breakout_8 + reversion_12 | -3.85% | -14.90% | -9.82% | -1.98% | 20.27% |
| breakout_8 AND volume_26 | 0.78% | -0.48% | -9.82% | -0.08% | 0.79% |
| breakout_8 + volume_26 | -3.03% | -12.53% | -9.82% | -1.14% | 11.72% |
| reversion_12 AND volume_26 | -1.25% | -5.71% | -9.82% | -0.51% | 5.26% |
| reversion_12 + volume_26 | -3.36% | -11.91% | -9.82% | -1.66% | 16.98% |

동일 구간·초기 자금, 종료 시 청산 비용 포함. 노출 맞춤은 사후 설명용이며 v2 실제 계좌 성과가 아닙니다.
[낙폭 분해·비용 영향·전체 구간](CAT/comparison.json)

[v1 전체 기록](CAT/accounts.json) · [v2 전체 기록](CAT/accounts-v2.json)

## WMT 계좌

| 모델 | 전략 | 평가액 USD | 손익 USD | 최근 매매·이유 |
|---|---|---:|---:|---|
| v1 | cash | 10000.00 | 0.00 | 대기 /  / 새 신호 대기 |
| v1 | buy_hold | 9944.46 | -55.54 | buy /  / buy_hold: prior completed bar target 100%; next bar open simulation |
| v1 | trend_8_26 | 9944.46 | -55.54 | buy /  / trend_8_26: prior completed bar target 100%; next bar open simulation |
| v1 | momentum_26 | 9944.46 | -55.54 | buy /  / momentum_26: prior completed bar target 100%; next bar open simulation |
| v1 | breakout_8 | 10000.00 | 0.00 | 대기 /  / 새 신호 대기 |
| v1 | reversion_12 | 10000.00 | 0.00 | 대기 /  / 새 신호 대기 |
| v1 | volume_26 | 10000.00 | 0.00 | 대기 /  / 새 신호 대기 |
| v1 | trend_8_26 AND momentum_26 | 9944.46 | -55.54 | buy /  / trend_8_26 AND momentum_26: prior completed bar target 100%; next bar open simulation |
| v1 | trend_8_26 + momentum_26 | 9944.46 | -55.54 | buy /  / trend_8_26 + momentum_26: prior completed bar target 100%; next bar open simulation |
| v1 | trend_8_26 AND breakout_8 | 10000.00 | 0.00 | 대기 /  / 새 신호 대기 |
| v1 | trend_8_26 + breakout_8 | 9972.16 | -27.84 | sell /  / trend_8_26 + breakout_8: prior completed bar target 50%; next bar open simulation |
| v1 | trend_8_26 AND reversion_12 | 10000.00 | 0.00 | 대기 /  / 새 신호 대기 |
| v1 | trend_8_26 + reversion_12 | 9972.16 | -27.84 | sell /  / trend_8_26 + reversion_12: prior completed bar target 50%; next bar open simulation |
| v1 | trend_8_26 AND volume_26 | 10000.00 | 0.00 | 대기 /  / 새 신호 대기 |
| v1 | trend_8_26 + volume_26 | 9972.16 | -27.84 | sell /  / trend_8_26 + volume_26: prior completed bar target 50%; next bar open simulation |
| v1 | momentum_26 AND breakout_8 | 10000.00 | 0.00 | 대기 /  / 새 신호 대기 |
| v1 | momentum_26 + breakout_8 | 9972.16 | -27.84 | sell /  / momentum_26 + breakout_8: prior completed bar target 50%; next bar open simulation |
| v1 | momentum_26 AND reversion_12 | 10000.00 | 0.00 | 대기 /  / 새 신호 대기 |
| v1 | momentum_26 + reversion_12 | 9972.16 | -27.84 | sell /  / momentum_26 + reversion_12: prior completed bar target 50%; next bar open simulation |
| v1 | momentum_26 AND volume_26 | 10000.00 | 0.00 | 대기 /  / 새 신호 대기 |
| v1 | momentum_26 + volume_26 | 9972.16 | -27.84 | sell /  / momentum_26 + volume_26: prior completed bar target 50%; next bar open simulation |
| v1 | breakout_8 AND reversion_12 | 10000.00 | 0.00 | 대기 /  / 새 신호 대기 |
| v1 | breakout_8 + reversion_12 | 10000.00 | 0.00 | 대기 /  / 새 신호 대기 |
| v1 | breakout_8 AND volume_26 | 10000.00 | 0.00 | 대기 /  / 새 신호 대기 |
| v1 | breakout_8 + volume_26 | 10000.00 | 0.00 | 대기 /  / 새 신호 대기 |
| v1 | reversion_12 AND volume_26 | 10000.00 | 0.00 | 대기 /  / 새 신호 대기 |
| v1 | reversion_12 + volume_26 | 10000.00 | 0.00 | 대기 /  / 새 신호 대기 |
| v2 | cash | 10000.00 | 0.00 | 대기 /  / 새 신호 대기 |
| v2 | buy_hold | 10635.50 | 635.50 | buy / partial / 직전 완료 봉 목표 비중 100%; 다음 봉 시가 가정 |
| v2 | trend_8_26 | 10490.78 | 490.78 | buy / partial / 직전 완료 봉 목표 비중 100%; 다음 봉 시가 가정 |
| v2 | momentum_26 | 10460.69 | 460.69 | buy / partial / 직전 완료 봉 목표 비중 100%; 다음 봉 시가 가정 |
| v2 | breakout_8 | 9964.65 | -35.35 | sell / filled / 직전 완료 봉 목표 비중 0%; 다음 봉 시가 가정 |
| v2 | reversion_12 | 10022.26 | 22.26 | sell / filled / 직전 완료 봉 목표 비중 0%; 다음 봉 시가 가정 |
| v2 | volume_26 | 9965.28 | -34.72 | sell / filled / 직전 완료 봉 목표 비중 0%; 다음 봉 시가 가정 |
| v2 | trend_8_26 AND momentum_26 | 10490.78 | 490.78 | buy / partial / 직전 완료 봉 목표 비중 100%; 다음 봉 시가 가정 |
| v2 | trend_8_26 + momentum_26 | 10475.72 | 475.72 | buy / partial / 직전 완료 봉 목표 비중 100%; 다음 봉 시가 가정 |
| v2 | trend_8_26 AND breakout_8 | 10088.55 | 88.55 | sell / filled / 직전 완료 봉 목표 비중 0%; 다음 봉 시가 가정 |
| v2 | trend_8_26 + breakout_8 | 10224.78 | 224.78 | sell / filled / 직전 완료 봉 목표 비중 50%; 다음 봉 시가 가정 |
| v2 | trend_8_26 AND reversion_12 | 9931.03 | -68.97 | sell / filled / 직전 완료 봉 목표 비중 0%; 다음 봉 시가 가정 |
| v2 | trend_8_26 + reversion_12 | 10255.35 | 255.35 | sell / filled / 직전 완료 봉 목표 비중 50%; 다음 봉 시가 가정 |
| v2 | trend_8_26 AND volume_26 | 9949.23 | -50.77 | sell / filled / 직전 완료 봉 목표 비중 0%; 다음 봉 시가 가정 |
| v2 | trend_8_26 + volume_26 | 10226.16 | 226.16 | sell / filled / 직전 완료 봉 목표 비중 50%; 다음 봉 시가 가정 |
| v2 | momentum_26 AND breakout_8 | 9964.65 | -35.35 | sell / filled / 직전 완료 봉 목표 비중 0%; 다음 봉 시가 가정 |
| v2 | momentum_26 + breakout_8 | 10210.14 | 210.14 | sell / filled / 직전 완료 봉 목표 비중 50%; 다음 봉 시가 가정 |
| v2 | momentum_26 AND reversion_12 | 9940.68 | -59.32 | sell / filled / 직전 완료 봉 목표 비중 0%; 다음 봉 시가 가정 |
| v2 | momentum_26 + reversion_12 | 10283.74 | 283.74 | sell / filled / 직전 완료 봉 목표 비중 50%; 다음 봉 시가 가정 |
| v2 | momentum_26 AND volume_26 | 9913.82 | -86.18 | sell / filled / 직전 완료 봉 목표 비중 0%; 다음 봉 시가 가정 |
| v2 | momentum_26 + volume_26 | 10211.58 | 211.58 | sell / filled / 직전 완료 봉 목표 비중 50%; 다음 봉 시가 가정 |
| v2 | breakout_8 AND reversion_12 | 10000.00 | 0.00 | 대기 /  / 새 신호 대기 |
| v2 | breakout_8 + reversion_12 | 10015.72 | 15.72 | sell / filled / 직전 완료 봉 목표 비중 0%; 다음 봉 시가 가정 |
| v2 | breakout_8 AND volume_26 | 9950.23 | -49.77 | sell / filled / 직전 완료 봉 목표 비중 0%; 다음 봉 시가 가정 |
| v2 | breakout_8 + volume_26 | 9966.35 | -33.65 | sell / filled / 직전 완료 봉 목표 비중 0%; 다음 봉 시가 가정 |
| v2 | reversion_12 AND volume_26 | 10009.78 | 9.78 | sell / filled / 직전 완료 봉 목표 비중 0%; 다음 봉 시가 가정 |
| v2 | reversion_12 + volume_26 | 9993.76 | -6.24 | sell / filled / 직전 완료 봉 목표 비중 0%; 다음 봉 시가 가정 |

### 같은 기간의 비용·노출 비교 (사후 연구)

| 전략 | 비용 전 | 비용 후 | 100% 보유 | 같은 평균 노출 보유 | 평균 노출 |
|---|---:|---:|---:|---:|---:|
| cash | 0.00% | 0.00% | 9.25% | 0.00% | 0.00% |
| buy_hold | 9.71% | 9.25% | 9.25% | 9.25% | 100.00% |
| trend_8_26 | 9.95% | 7.22% | 9.25% | 6.16% | 66.58% |
| momentum_26 | 7.16% | 3.18% | 9.25% | 6.11% | 66.05% |
| breakout_8 | 5.52% | -11.92% | 9.25% | 2.48% | 26.84% |
| reversion_12 | 1.98% | -6.63% | 9.25% | 1.58% | 17.11% |
| volume_26 | -0.17% | -5.87% | 9.25% | 0.56% | 6.05% |
| trend_8_26 AND momentum_26 | 9.48% | 5.42% | 9.25% | 5.62% | 60.79% |
| trend_8_26 + momentum_26 | 8.55% | 5.19% | 9.25% | 6.13% | 66.32% |
| trend_8_26 AND breakout_8 | 6.92% | -6.91% | 9.25% | 2.07% | 22.37% |
| trend_8_26 + breakout_8 | 7.73% | -2.60% | 9.25% | 4.32% | 46.72% |
| trend_8_26 AND reversion_12 | 0.40% | -3.73% | 9.25% | 0.51% | 5.53% |
| trend_8_26 + reversion_12 | 5.93% | 0.28% | 9.25% | 3.87% | 41.85% |
| trend_8_26 AND volume_26 | 1.13% | -1.39% | 9.25% | 0.19% | 2.11% |
| trend_8_26 + volume_26 | 4.81% | 0.90% | 9.25% | 3.36% | 36.32% |
| momentum_26 AND breakout_8 | 5.58% | -8.47% | 9.25% | 2.16% | 23.42% |
| momentum_26 + breakout_8 | 6.35% | -4.45% | 9.25% | 4.29% | 46.45% |
| momentum_26 AND reversion_12 | 0.36% | -3.77% | 9.25% | 0.49% | 5.26% |
| momentum_26 + reversion_12 | 4.58% | 0.04% | 9.25% | 3.84% | 41.58% |
| momentum_26 AND volume_26 | 0.44% | -3.69% | 9.25% | 0.27% | 2.89% |
| momentum_26 + volume_26 | 3.47% | -1.43% | 9.25% | 3.33% | 36.06% |
| breakout_8 AND reversion_12 | 0.00% | 0.00% | 9.25% | 0.00% | 0.00% |
| breakout_8 + reversion_12 | 3.77% | -8.92% | 9.25% | 2.03% | 21.98% |
| breakout_8 AND volume_26 | 0.91% | -1.19% | 9.25% | 0.15% | 1.58% |
| breakout_8 + volume_26 | 2.67% | -8.16% | 9.25% | 1.52% | 16.45% |
| reversion_12 AND volume_26 | -0.11% | -3.00% | 9.25% | 0.27% | 2.89% |
| reversion_12 + volume_26 | 0.91% | -6.05% | 9.25% | 1.07% | 11.58% |

동일 구간·초기 자금, 종료 시 청산 비용 포함. 노출 맞춤은 사후 설명용이며 v2 실제 계좌 성과가 아닙니다.
[낙폭 분해·비용 영향·전체 구간](WMT/comparison.json)

[v1 전체 기록](WMT/accounts.json) · [v2 전체 기록](WMT/accounts-v2.json)
