# 모의투자 운영 현황

최근 확인: 2026-10-15T16:37:00.608660+00:00 (UTC)
다음 15분 확인 목표 (세션 실행 중에만 적용): 2026-10-15T16:52:00+00:00 (UTC, 실행 지연 가능)

실제 주문 없음. v1 기존 계좌와 v2 새 계좌의 시작일이 다르므로 수익률을 직접 우열 비교하지 마세요.
v2는 다음 봉 시가에 비용·스프레드·직전 거래량 제한을 적용한 가상 체결입니다. 미체결 잔량은 만료됩니다.

| 종목 | 상태 | 최근 성공 UTC | 마지막 완료 봉 UTC | 이번 새 봉 |
|---|---|---|---|---|
| SPY | updated | 2026-10-15T16:37:00.608660+00:00 | 2026-10-15T16:15:00+00:00 | 1 |
| QQQ | updated | 2026-10-15T16:37:00.608660+00:00 | 2026-10-15T16:15:00+00:00 | 1 |
| IWM | updated | 2026-10-15T16:37:00.608660+00:00 | 2026-10-15T16:15:00+00:00 | 1 |
| DIA | updated | 2026-10-15T16:37:00.608660+00:00 | 2026-10-15T16:15:00+00:00 | 1 |
| MSFT | updated | 2026-10-15T16:37:00.608660+00:00 | 2026-10-15T16:15:00+00:00 | 1 |
| JPM | updated | 2026-10-15T16:37:00.608660+00:00 | 2026-10-15T16:15:00+00:00 | 1 |
| XOM | updated | 2026-10-15T16:37:00.608660+00:00 | 2026-10-15T16:15:00+00:00 | 1 |
| JNJ | updated | 2026-10-15T16:37:00.608660+00:00 | 2026-10-15T16:15:00+00:00 | 1 |
| CAT | updated | 2026-10-15T16:37:00.608660+00:00 | 2026-10-15T16:15:00+00:00 | 1 |
| WMT | updated | 2026-10-15T16:37:00.608660+00:00 | 2026-10-15T16:15:00+00:00 | 1 |

이번 실행 소요: 67.65초
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
| v1 | buy_hold | 9967.33 | -32.67 | buy /  / buy_hold: prior completed bar target 100%; next bar open simulation |
| v1 | trend_8_26 | 9966.27 | -33.73 | buy /  / trend_8_26: prior completed bar target 100%; next bar open simulation |
| v1 | momentum_26 | 9976.53 | -23.47 | buy /  / momentum_26: prior completed bar target 100%; next bar open simulation |
| v1 | breakout_8 | 10000.00 | 0.00 | 대기 /  / 새 신호 대기 |
| v1 | reversion_12 | 10000.00 | 0.00 | 대기 /  / 새 신호 대기 |
| v1 | volume_26 | 9949.83 | -50.17 | sell /  / volume_26: prior completed bar target 0%; next bar open simulation |
| v1 | trend_8_26 AND momentum_26 | 9976.53 | -23.47 | buy /  / trend_8_26 AND momentum_26: prior completed bar target 100%; next bar open simulation |
| v1 | trend_8_26 + momentum_26 | 9971.39 | -28.61 | buy /  / trend_8_26 + momentum_26: prior completed bar target 100%; next bar open simulation |
| v1 | trend_8_26 AND breakout_8 | 10000.00 | 0.00 | 대기 /  / 새 신호 대기 |
| v1 | trend_8_26 + breakout_8 | 9983.10 | -16.90 | sell /  / trend_8_26 + breakout_8: prior completed bar target 50%; next bar open simulation |
| v1 | trend_8_26 AND reversion_12 | 10000.00 | 0.00 | 대기 /  / 새 신호 대기 |
| v1 | trend_8_26 + reversion_12 | 9983.10 | -16.90 | sell /  / trend_8_26 + reversion_12: prior completed bar target 50%; next bar open simulation |
| v1 | trend_8_26 AND volume_26 | 9949.83 | -50.17 | sell /  / trend_8_26 AND volume_26: prior completed bar target 0%; next bar open simulation |
| v1 | trend_8_26 + volume_26 | 9958.05 | -41.95 | sell /  / trend_8_26 + volume_26: prior completed bar target 50%; next bar open simulation |
| v1 | momentum_26 AND breakout_8 | 10000.00 | 0.00 | 대기 /  / 새 신호 대기 |
| v1 | momentum_26 + breakout_8 | 9988.24 | -11.76 | buy /  / momentum_26 + breakout_8: prior completed bar target 50%; next bar open simulation |
| v1 | momentum_26 AND reversion_12 | 10000.00 | 0.00 | 대기 /  / 새 신호 대기 |
| v1 | momentum_26 + reversion_12 | 9988.24 | -11.76 | buy /  / momentum_26 + reversion_12: prior completed bar target 50%; next bar open simulation |
| v1 | momentum_26 AND volume_26 | 10000.00 | 0.00 | 대기 /  / 새 신호 대기 |
| v1 | momentum_26 + volume_26 | 9983.10 | -16.90 | sell /  / momentum_26 + volume_26: prior completed bar target 50%; next bar open simulation |
| v1 | breakout_8 AND reversion_12 | 10000.00 | 0.00 | 대기 /  / 새 신호 대기 |
| v1 | breakout_8 + reversion_12 | 10000.00 | 0.00 | 대기 /  / 새 신호 대기 |
| v1 | breakout_8 AND volume_26 | 10000.00 | 0.00 | 대기 /  / 새 신호 대기 |
| v1 | breakout_8 + volume_26 | 9974.87 | -25.13 | sell /  / breakout_8 + volume_26: prior completed bar target 0%; next bar open simulation |
| v1 | reversion_12 AND volume_26 | 10000.00 | 0.00 | 대기 /  / 새 신호 대기 |
| v1 | reversion_12 + volume_26 | 9974.87 | -25.13 | sell /  / reversion_12 + volume_26: prior completed bar target 0%; next bar open simulation |
| v2 | cash | 10000.00 | 0.00 | 대기 /  / 새 신호 대기 |
| v2 | buy_hold | 9858.07 | -141.93 | buy / partial / 직전 완료 봉 목표 비중 100%; 다음 봉 시가 가정 |
| v2 | trend_8_26 | 9814.02 | -185.98 | buy / partial / 직전 완료 봉 목표 비중 100%; 다음 봉 시가 가정 |
| v2 | momentum_26 | 9837.74 | -162.26 | buy / partial / 직전 완료 봉 목표 비중 100%; 다음 봉 시가 가정 |
| v2 | breakout_8 | 9684.78 | -315.22 | sell / filled / 직전 완료 봉 목표 비중 0%; 다음 봉 시가 가정 |
| v2 | reversion_12 | 9535.84 | -464.16 | sell / filled / 직전 완료 봉 목표 비중 0%; 다음 봉 시가 가정 |
| v2 | volume_26 | 9441.45 | -558.55 | sell / filled / 직전 완료 봉 목표 비중 0%; 다음 봉 시가 가정 |
| v2 | trend_8_26 AND momentum_26 | 9844.45 | -155.55 | buy / partial / 직전 완료 봉 목표 비중 100%; 다음 봉 시가 가정 |
| v2 | trend_8_26 + momentum_26 | 9825.89 | -174.11 | buy / partial / 직전 완료 봉 목표 비중 100%; 다음 봉 시가 가정 |
| v2 | trend_8_26 AND breakout_8 | 9913.42 | -86.58 | sell / filled / 직전 완료 봉 목표 비중 0%; 다음 봉 시가 가정 |
| v2 | trend_8_26 + breakout_8 | 9749.04 | -250.96 | sell / filled / 직전 완료 봉 목표 비중 50%; 다음 봉 시가 가정 |
| v2 | trend_8_26 AND reversion_12 | 9896.11 | -103.89 | sell / filled / 직전 완료 봉 목표 비중 0%; 다음 봉 시가 가정 |
| v2 | trend_8_26 + reversion_12 | 9673.64 | -326.36 | sell / filled / 직전 완료 봉 목표 비중 50%; 다음 봉 시가 가정 |
| v2 | trend_8_26 AND volume_26 | 9845.91 | -154.09 | sell / filled / 직전 완료 봉 목표 비중 0%; 다음 봉 시가 가정 |
| v2 | trend_8_26 + volume_26 | 9645.97 | -354.03 | sell / filled / 직전 완료 봉 목표 비중 50%; 다음 봉 시가 가정 |
| v2 | momentum_26 AND breakout_8 | 9871.37 | -128.63 | sell / filled / 직전 완료 봉 목표 비중 0%; 다음 봉 시가 가정 |
| v2 | momentum_26 + breakout_8 | 9760.88 | -239.12 | buy / filled / 직전 완료 봉 목표 비중 50%; 다음 봉 시가 가정 |
| v2 | momentum_26 AND reversion_12 | 9963.21 | -36.79 | sell / filled / 직전 완료 봉 목표 비중 0%; 다음 봉 시가 가정 |
| v2 | momentum_26 + reversion_12 | 9705.72 | -294.28 | buy / filled / 직전 완료 봉 목표 비중 50%; 다음 봉 시가 가정 |
| v2 | momentum_26 AND volume_26 | 9917.25 | -82.75 | sell / filled / 직전 완료 봉 목표 비중 0%; 다음 봉 시가 가정 |
| v2 | momentum_26 + volume_26 | 9698.24 | -301.76 | sell / filled / 직전 완료 봉 목표 비중 50%; 다음 봉 시가 가정 |
| v2 | breakout_8 AND reversion_12 | 10000.00 | 0.00 | 대기 /  / 새 신호 대기 |
| v2 | breakout_8 + reversion_12 | 9650.09 | -349.91 | sell / filled / 직전 완료 봉 목표 비중 0%; 다음 봉 시가 가정 |
| v2 | breakout_8 AND volume_26 | 9933.18 | -66.82 | sell / filled / 직전 완료 봉 목표 비중 0%; 다음 봉 시가 가정 |
| v2 | breakout_8 + volume_26 | 9602.28 | -397.72 | sell / filled / 직전 완료 봉 목표 비중 0%; 다음 봉 시가 가정 |
| v2 | reversion_12 AND volume_26 | 9743.33 | -256.67 | sell / filled / 직전 완료 봉 목표 비중 0%; 다음 봉 시가 가정 |
| v2 | reversion_12 + volume_26 | 9568.30 | -431.70 | sell / filled / 직전 완료 봉 목표 비중 0%; 다음 봉 시가 가정 |

### 같은 기간의 비용·노출 비교 (사후 연구)

| 전략 | 비용 전 | 비용 후 | 100% 보유 | 같은 평균 노출 보유 | 평균 노출 |
|---|---:|---:|---:|---:|---:|
| cash | 0.00% | 0.00% | -0.24% | -0.00% | 0.00% |
| buy_hold | 0.18% | -0.24% | -0.24% | -0.24% | 100.00% |
| trend_8_26 | 1.43% | -1.92% | -0.24% | -0.12% | 49.21% |
| momentum_26 | -0.44% | -4.94% | -0.24% | -0.11% | 48.68% |
| breakout_8 | -0.74% | -15.74% | -0.24% | -0.05% | 22.11% |
| reversion_12 | -1.86% | -12.74% | -0.24% | -0.07% | 27.89% |
| volume_26 | -0.54% | -9.32% | -0.24% | -0.02% | 8.68% |
| trend_8_26 AND momentum_26 | 0.89% | -2.85% | -0.24% | -0.10% | 42.37% |
| trend_8_26 + momentum_26 | 0.49% | -3.24% | -0.24% | -0.12% | 48.95% |
| trend_8_26 AND breakout_8 | -0.06% | -10.40% | -0.24% | -0.03% | 13.16% |
| trend_8_26 + breakout_8 | 0.34% | -9.09% | -0.24% | -0.08% | 35.66% |
| trend_8_26 AND reversion_12 | 0.10% | -4.01% | -0.24% | -0.01% | 6.05% |
| trend_8_26 + reversion_12 | -0.22% | -7.30% | -0.24% | -0.09% | 38.56% |
| trend_8_26 AND volume_26 | -0.17% | -4.27% | -0.24% | -0.01% | 3.95% |
| trend_8_26 + volume_26 | 0.44% | -5.70% | -0.24% | -0.07% | 28.95% |
| momentum_26 AND breakout_8 | 0.24% | -10.13% | -0.24% | -0.03% | 14.21% |
| momentum_26 + breakout_8 | -0.59% | -10.50% | -0.24% | -0.08% | 35.40% |
| momentum_26 AND reversion_12 | -0.88% | -5.75% | -0.24% | -0.02% | 6.84% |
| momentum_26 + reversion_12 | -1.15% | -8.36% | -0.24% | -0.09% | 38.29% |
| momentum_26 AND volume_26 | -0.22% | -3.11% | -0.24% | -0.00% | 2.11% |
| momentum_26 + volume_26 | -0.49% | -5.78% | -0.24% | -0.07% | 28.69% |
| breakout_8 AND reversion_12 | 0.00% | 0.00% | -0.24% | -0.00% | 0.00% |
| breakout_8 + reversion_12 | -1.30% | -13.72% | -0.24% | -0.06% | 25.01% |
| breakout_8 AND volume_26 | 0.05% | -1.61% | -0.24% | -0.00% | 1.32% |
| breakout_8 + volume_26 | -0.64% | -11.67% | -0.24% | -0.04% | 15.40% |
| reversion_12 AND volume_26 | -0.67% | -4.76% | -0.24% | -0.01% | 3.95% |
| reversion_12 + volume_26 | -1.20% | -10.68% | -0.24% | -0.04% | 18.30% |

동일 구간·초기 자금, 종료 시 청산 비용 포함. 노출 맞춤은 사후 설명용이며 v2 실제 계좌 성과가 아닙니다.
[낙폭 분해·비용 영향·전체 구간](SPY/comparison.json)

[v1 전체 기록](SPY/accounts.json) · [v2 전체 기록](SPY/accounts-v2.json)

## QQQ 계좌

| 모델 | 전략 | 평가액 USD | 손익 USD | 최근 매매·이유 |
|---|---|---:|---:|---|
| v1 | cash | 10000.00 | 0.00 | 대기 /  / 새 신호 대기 |
| v1 | buy_hold | 9955.79 | -44.21 | buy /  / buy_hold: prior completed bar target 100%; next bar open simulation |
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
| v2 | buy_hold | 9622.14 | -377.86 | buy / partial / 직전 완료 봉 목표 비중 100%; 다음 봉 시가 가정 |
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
| cash | 0.00% | 0.00% | -2.92% | -0.00% | 0.00% |
| buy_hold | -2.51% | -2.92% | -2.92% | -2.92% | 100.00% |
| trend_8_26 | 0.19% | -3.12% | -2.92% | -1.44% | 49.21% |
| momentum_26 | -1.28% | -6.13% | -2.92% | -1.27% | 43.68% |
| breakout_8 | -1.69% | -16.89% | -2.92% | -0.51% | 17.63% |
| reversion_12 | -0.86% | -12.96% | -2.92% | -0.78% | 26.58% |
| volume_26 | -1.07% | -13.51% | -2.92% | -0.41% | 14.21% |
| trend_8_26 AND momentum_26 | -0.32% | -4.42% | -2.92% | -1.14% | 39.21% |
| trend_8_26 + momentum_26 | -0.54% | -4.44% | -2.92% | -1.36% | 46.45% |
| trend_8_26 AND breakout_8 | -0.58% | -10.12% | -2.92% | -0.31% | 10.79% |
| trend_8_26 + breakout_8 | -0.75% | -9.89% | -2.92% | -0.97% | 33.43% |
| trend_8_26 AND reversion_12 | 0.42% | -5.31% | -2.92% | -0.18% | 6.05% |
| trend_8_26 + reversion_12 | -0.32% | -7.60% | -2.92% | -1.11% | 37.90% |
| trend_8_26 AND volume_26 | -0.71% | -5.59% | -2.92% | -0.12% | 4.21% |
| trend_8_26 + volume_26 | -0.44% | -8.28% | -2.92% | -0.93% | 31.72% |
| momentum_26 AND breakout_8 | -0.74% | -9.88% | -2.92% | -0.32% | 11.05% |
| momentum_26 + breakout_8 | -1.48% | -11.49% | -2.92% | -0.89% | 30.66% |
| momentum_26 AND reversion_12 | -0.02% | -5.73% | -2.92% | -0.14% | 4.74% |
| momentum_26 + reversion_12 | -1.06% | -9.05% | -2.92% | -1.02% | 35.14% |
| momentum_26 AND volume_26 | -0.30% | -4.40% | -2.92% | -0.10% | 3.42% |
| momentum_26 + volume_26 | -1.17% | -9.72% | -2.92% | -0.84% | 28.95% |
| breakout_8 AND reversion_12 | 0.00% | 0.00% | -2.92% | -0.00% | 0.00% |
| breakout_8 + reversion_12 | -1.27% | -14.06% | -2.92% | -0.64% | 22.11% |
| breakout_8 AND volume_26 | 0.04% | -2.04% | -2.92% | -0.04% | 1.32% |
| breakout_8 + volume_26 | -1.38% | -13.97% | -2.92% | -0.46% | 15.93% |
| reversion_12 AND volume_26 | -1.25% | -8.44% | -2.92% | -0.25% | 8.68% |
| reversion_12 + volume_26 | -0.96% | -12.88% | -2.92% | -0.59% | 20.40% |

동일 구간·초기 자금, 종료 시 청산 비용 포함. 노출 맞춤은 사후 설명용이며 v2 실제 계좌 성과가 아닙니다.
[낙폭 분해·비용 영향·전체 구간](QQQ/comparison.json)

[v1 전체 기록](QQQ/accounts.json) · [v2 전체 기록](QQQ/accounts-v2.json)

## IWM 계좌

| 모델 | 전략 | 평가액 USD | 손익 USD | 최근 매매·이유 |
|---|---|---:|---:|---|
| v1 | cash | 10000.00 | 0.00 | 대기 /  / 새 신호 대기 |
| v1 | buy_hold | 9947.23 | -52.77 | buy /  / buy_hold: prior completed bar target 100%; next bar open simulation |
| v1 | trend_8_26 | 9947.23 | -52.77 | buy /  / trend_8_26: prior completed bar target 100%; next bar open simulation |
| v1 | momentum_26 | 9947.23 | -52.77 | buy /  / momentum_26: prior completed bar target 100%; next bar open simulation |
| v1 | breakout_8 | 10000.00 | 0.00 | 대기 /  / 새 신호 대기 |
| v1 | reversion_12 | 10000.00 | 0.00 | 대기 /  / 새 신호 대기 |
| v1 | volume_26 | 10000.00 | 0.00 | 대기 /  / 새 신호 대기 |
| v1 | trend_8_26 AND momentum_26 | 9947.23 | -52.77 | buy /  / trend_8_26 AND momentum_26: prior completed bar target 100%; next bar open simulation |
| v1 | trend_8_26 + momentum_26 | 9947.23 | -52.77 | buy /  / trend_8_26 + momentum_26: prior completed bar target 100%; next bar open simulation |
| v1 | trend_8_26 AND breakout_8 | 10000.00 | 0.00 | 대기 /  / 새 신호 대기 |
| v1 | trend_8_26 + breakout_8 | 9973.55 | -26.45 | buy /  / trend_8_26 + breakout_8: prior completed bar target 50%; next bar open simulation |
| v1 | trend_8_26 AND reversion_12 | 10000.00 | 0.00 | 대기 /  / 새 신호 대기 |
| v1 | trend_8_26 + reversion_12 | 9973.55 | -26.45 | buy /  / trend_8_26 + reversion_12: prior completed bar target 50%; next bar open simulation |
| v1 | trend_8_26 AND volume_26 | 10000.00 | 0.00 | 대기 /  / 새 신호 대기 |
| v1 | trend_8_26 + volume_26 | 9973.55 | -26.45 | buy /  / trend_8_26 + volume_26: prior completed bar target 50%; next bar open simulation |
| v1 | momentum_26 AND breakout_8 | 10000.00 | 0.00 | 대기 /  / 새 신호 대기 |
| v1 | momentum_26 + breakout_8 | 9973.55 | -26.45 | buy /  / momentum_26 + breakout_8: prior completed bar target 50%; next bar open simulation |
| v1 | momentum_26 AND reversion_12 | 10000.00 | 0.00 | 대기 /  / 새 신호 대기 |
| v1 | momentum_26 + reversion_12 | 9973.55 | -26.45 | buy /  / momentum_26 + reversion_12: prior completed bar target 50%; next bar open simulation |
| v1 | momentum_26 AND volume_26 | 10000.00 | 0.00 | 대기 /  / 새 신호 대기 |
| v1 | momentum_26 + volume_26 | 9973.55 | -26.45 | buy /  / momentum_26 + volume_26: prior completed bar target 50%; next bar open simulation |
| v1 | breakout_8 AND reversion_12 | 10000.00 | 0.00 | 대기 /  / 새 신호 대기 |
| v1 | breakout_8 + reversion_12 | 10000.00 | 0.00 | 대기 /  / 새 신호 대기 |
| v1 | breakout_8 AND volume_26 | 10000.00 | 0.00 | 대기 /  / 새 신호 대기 |
| v1 | breakout_8 + volume_26 | 10000.00 | 0.00 | 대기 /  / 새 신호 대기 |
| v1 | reversion_12 AND volume_26 | 10000.00 | 0.00 | 대기 /  / 새 신호 대기 |
| v1 | reversion_12 + volume_26 | 10000.00 | 0.00 | 대기 /  / 새 신호 대기 |
| v2 | cash | 10000.00 | 0.00 | 대기 /  / 새 신호 대기 |
| v2 | buy_hold | 9782.66 | -217.34 | buy / partial / 직전 완료 봉 목표 비중 100%; 다음 봉 시가 가정 |
| v2 | trend_8_26 | 9760.26 | -239.74 | buy / partial / 직전 완료 봉 목표 비중 100%; 다음 봉 시가 가정 |
| v2 | momentum_26 | 9761.26 | -238.74 | buy / partial / 직전 완료 봉 목표 비중 100%; 다음 봉 시가 가정 |
| v2 | breakout_8 | 9666.31 | -333.69 | sell / filled / 직전 완료 봉 목표 비중 0%; 다음 봉 시가 가정 |
| v2 | reversion_12 | 9538.67 | -461.33 | sell / filled / 직전 완료 봉 목표 비중 0%; 다음 봉 시가 가정 |
| v2 | volume_26 | 9513.36 | -486.64 | sell / filled / 직전 완료 봉 목표 비중 0%; 다음 봉 시가 가정 |
| v2 | trend_8_26 AND momentum_26 | 9911.75 | -88.25 | buy / partial / 직전 완료 봉 목표 비중 100%; 다음 봉 시가 가정 |
| v2 | trend_8_26 + momentum_26 | 9781.41 | -218.59 | buy / partial / 직전 완료 봉 목표 비중 100%; 다음 봉 시가 가정 |
| v2 | trend_8_26 AND breakout_8 | 9962.82 | -37.18 | sell / filled / 직전 완료 봉 목표 비중 0%; 다음 봉 시가 가정 |
| v2 | trend_8_26 + breakout_8 | 9733.69 | -266.31 | buy / filled / 직전 완료 봉 목표 비중 50%; 다음 봉 시가 가정 |
| v2 | trend_8_26 AND reversion_12 | 9881.82 | -118.18 | sell / filled / 직전 완료 봉 목표 비중 0%; 다음 봉 시가 가정 |
| v2 | trend_8_26 + reversion_12 | 9648.69 | -351.31 | buy / filled / 직전 완료 봉 목표 비중 50%; 다음 봉 시가 가정 |
| v2 | trend_8_26 AND volume_26 | 9862.83 | -137.17 | sell / filled / 직전 완료 봉 목표 비중 0%; 다음 봉 시가 가정 |
| v2 | trend_8_26 + volume_26 | 9656.29 | -343.71 | buy / filled / 직전 완료 봉 목표 비중 50%; 다음 봉 시가 가정 |
| v2 | momentum_26 AND breakout_8 | 9854.44 | -145.56 | sell / filled / 직전 완료 봉 목표 비중 0%; 다음 봉 시가 가정 |
| v2 | momentum_26 + breakout_8 | 9713.65 | -286.35 | buy / filled / 직전 완료 봉 목표 비중 50%; 다음 봉 시가 가정 |
| v2 | momentum_26 AND reversion_12 | 9960.59 | -39.41 | sell / filled / 직전 완료 봉 목표 비중 0%; 다음 봉 시가 가정 |
| v2 | momentum_26 + reversion_12 | 9669.26 | -330.74 | buy / filled / 직전 완료 봉 목표 비중 50%; 다음 봉 시가 가정 |
| v2 | momentum_26 AND volume_26 | 9897.79 | -102.21 | sell / filled / 직전 완료 봉 목표 비중 0%; 다음 봉 시가 가정 |
| v2 | momentum_26 + volume_26 | 9636.33 | -363.67 | buy / filled / 직전 완료 봉 목표 비중 50%; 다음 봉 시가 가정 |
| v2 | breakout_8 AND reversion_12 | 10000.00 | 0.00 | 대기 /  / 새 신호 대기 |
| v2 | breakout_8 + reversion_12 | 9642.35 | -357.65 | sell / filled / 직전 완료 봉 목표 비중 0%; 다음 봉 시가 가정 |
| v2 | breakout_8 AND volume_26 | 9746.03 | -253.97 | sell / filled / 직전 완료 봉 목표 비중 0%; 다음 봉 시가 가정 |
| v2 | breakout_8 + volume_26 | 9609.68 | -390.32 | sell / filled / 직전 완료 봉 목표 비중 0%; 다음 봉 시가 가정 |
| v2 | reversion_12 AND volume_26 | 9740.75 | -259.25 | sell / filled / 직전 완료 봉 목표 비중 0%; 다음 봉 시가 가정 |
| v2 | reversion_12 + volume_26 | 9545.82 | -454.18 | sell / filled / 직전 완료 봉 목표 비중 0%; 다음 봉 시가 가정 |

### 같은 기간의 비용·노출 비교 (사후 연구)

| 전략 | 비용 전 | 비용 후 | 100% 보유 | 같은 평균 노출 보유 | 평균 노출 |
|---|---:|---:|---:|---:|---:|
| cash | 0.00% | 0.00% | -3.52% | -0.00% | 0.00% |
| buy_hold | -3.12% | -3.52% | -3.52% | -3.52% | 100.00% |
| trend_8_26 | -2.55% | -6.56% | -3.52% | -1.59% | 44.74% |
| momentum_26 | -3.19% | -8.72% | -3.52% | -1.38% | 38.95% |
| breakout_8 | -1.01% | -14.18% | -3.52% | -0.66% | 18.68% |
| reversion_12 | -2.15% | -14.82% | -3.52% | -1.07% | 30.00% |
| volume_26 | -2.34% | -9.45% | -3.52% | -0.31% | 8.68% |
| trend_8_26 AND momentum_26 | -2.85% | -7.24% | -3.52% | -1.19% | 33.42% |
| trend_8_26 + momentum_26 | -2.87% | -7.25% | -3.52% | -1.48% | 41.84% |
| trend_8_26 AND breakout_8 | -0.88% | -8.48% | -3.52% | -0.37% | 10.26% |
| trend_8_26 + breakout_8 | -1.77% | -10.26% | -3.52% | -1.13% | 31.72% |
| trend_8_26 AND reversion_12 | -0.12% | -5.03% | -3.52% | -0.22% | 6.05% |
| trend_8_26 + reversion_12 | -2.34% | -10.60% | -3.52% | -1.33% | 37.37% |
| trend_8_26 AND volume_26 | -1.05% | -4.72% | -3.52% | -0.13% | 3.68% |
| trend_8_26 + volume_26 | -2.44% | -7.82% | -3.52% | -0.95% | 26.71% |
| momentum_26 AND breakout_8 | -0.10% | -7.37% | -3.52% | -0.35% | 9.74% |
| momentum_26 + breakout_8 | -2.10% | -11.49% | -3.52% | -1.02% | 28.82% |
| momentum_26 AND reversion_12 | -0.05% | -3.76% | -3.52% | -0.12% | 3.42% |
| momentum_26 + reversion_12 | -2.67% | -10.71% | -3.52% | -1.22% | 34.48% |
| momentum_26 AND volume_26 | -1.34% | -4.20% | -3.52% | -0.08% | 2.11% |
| momentum_26 + volume_26 | -2.76% | -8.71% | -3.52% | -0.85% | 23.82% |
| breakout_8 AND reversion_12 | 0.00% | 0.00% | -3.52% | -0.00% | 0.00% |
| breakout_8 + reversion_12 | -1.58% | -13.79% | -3.52% | -0.87% | 24.35% |
| breakout_8 AND volume_26 | -1.33% | -4.19% | -3.52% | -0.08% | 2.37% |
| breakout_8 + volume_26 | -1.67% | -11.66% | -3.52% | -0.49% | 13.69% |
| reversion_12 AND volume_26 | -0.38% | -4.47% | -3.52% | -0.16% | 4.47% |
| reversion_12 + volume_26 | -2.24% | -11.63% | -3.52% | -0.69% | 19.35% |

동일 구간·초기 자금, 종료 시 청산 비용 포함. 노출 맞춤은 사후 설명용이며 v2 실제 계좌 성과가 아닙니다.
[낙폭 분해·비용 영향·전체 구간](IWM/comparison.json)

[v1 전체 기록](IWM/accounts.json) · [v2 전체 기록](IWM/accounts-v2.json)

## DIA 계좌

| 모델 | 전략 | 평가액 USD | 손익 USD | 최근 매매·이유 |
|---|---|---:|---:|---|
| v1 | cash | 10000.00 | 0.00 | 대기 /  / 새 신호 대기 |
| v1 | buy_hold | 9966.42 | -33.58 | buy /  / buy_hold: prior completed bar target 100%; next bar open simulation |
| v1 | trend_8_26 | 9966.42 | -33.58 | buy /  / trend_8_26: prior completed bar target 100%; next bar open simulation |
| v1 | momentum_26 | 9966.42 | -33.58 | buy /  / momentum_26: prior completed bar target 100%; next bar open simulation |
| v1 | breakout_8 | 10000.00 | 0.00 | 대기 /  / 새 신호 대기 |
| v1 | reversion_12 | 10000.00 | 0.00 | 대기 /  / 새 신호 대기 |
| v1 | volume_26 | 10000.00 | 0.00 | 대기 /  / 새 신호 대기 |
| v1 | trend_8_26 AND momentum_26 | 9966.42 | -33.58 | buy /  / trend_8_26 AND momentum_26: prior completed bar target 100%; next bar open simulation |
| v1 | trend_8_26 + momentum_26 | 9966.42 | -33.58 | buy /  / trend_8_26 + momentum_26: prior completed bar target 100%; next bar open simulation |
| v1 | trend_8_26 AND breakout_8 | 10000.00 | 0.00 | 대기 /  / 새 신호 대기 |
| v1 | trend_8_26 + breakout_8 | 9983.17 | -16.83 | buy /  / trend_8_26 + breakout_8: prior completed bar target 50%; next bar open simulation |
| v1 | trend_8_26 AND reversion_12 | 10000.00 | 0.00 | 대기 /  / 새 신호 대기 |
| v1 | trend_8_26 + reversion_12 | 9983.17 | -16.83 | buy /  / trend_8_26 + reversion_12: prior completed bar target 50%; next bar open simulation |
| v1 | trend_8_26 AND volume_26 | 10000.00 | 0.00 | 대기 /  / 새 신호 대기 |
| v1 | trend_8_26 + volume_26 | 9983.17 | -16.83 | buy /  / trend_8_26 + volume_26: prior completed bar target 50%; next bar open simulation |
| v1 | momentum_26 AND breakout_8 | 10000.00 | 0.00 | 대기 /  / 새 신호 대기 |
| v1 | momentum_26 + breakout_8 | 9983.17 | -16.83 | buy /  / momentum_26 + breakout_8: prior completed bar target 50%; next bar open simulation |
| v1 | momentum_26 AND reversion_12 | 10000.00 | 0.00 | 대기 /  / 새 신호 대기 |
| v1 | momentum_26 + reversion_12 | 9983.17 | -16.83 | buy /  / momentum_26 + reversion_12: prior completed bar target 50%; next bar open simulation |
| v1 | momentum_26 AND volume_26 | 10000.00 | 0.00 | 대기 /  / 새 신호 대기 |
| v1 | momentum_26 + volume_26 | 9983.17 | -16.83 | buy /  / momentum_26 + volume_26: prior completed bar target 50%; next bar open simulation |
| v1 | breakout_8 AND reversion_12 | 10000.00 | 0.00 | 대기 /  / 새 신호 대기 |
| v1 | breakout_8 + reversion_12 | 10000.00 | 0.00 | 대기 /  / 새 신호 대기 |
| v1 | breakout_8 AND volume_26 | 10000.00 | 0.00 | 대기 /  / 새 신호 대기 |
| v1 | breakout_8 + volume_26 | 10000.00 | 0.00 | 대기 /  / 새 신호 대기 |
| v1 | reversion_12 AND volume_26 | 10000.00 | 0.00 | 대기 /  / 새 신호 대기 |
| v1 | reversion_12 + volume_26 | 10000.00 | 0.00 | 대기 /  / 새 신호 대기 |
| v2 | cash | 10000.00 | 0.00 | 대기 /  / 새 신호 대기 |
| v2 | buy_hold | 10049.56 | 49.56 | buy / partial / 직전 완료 봉 목표 비중 100%; 다음 봉 시가 가정 |
| v2 | trend_8_26 | 9862.28 | -137.72 | buy / partial / 직전 완료 봉 목표 비중 100%; 다음 봉 시가 가정 |
| v2 | momentum_26 | 9970.71 | -29.29 | buy / partial / 직전 완료 봉 목표 비중 100%; 다음 봉 시가 가정 |
| v2 | breakout_8 | 9626.51 | -373.49 | sell / filled / 직전 완료 봉 목표 비중 0%; 다음 봉 시가 가정 |
| v2 | reversion_12 | 9698.03 | -301.97 | sell / filled / 직전 완료 봉 목표 비중 0%; 다음 봉 시가 가정 |
| v2 | volume_26 | 9718.21 | -281.79 | sell / filled / 직전 완료 봉 목표 비중 0%; 다음 봉 시가 가정 |
| v2 | trend_8_26 AND momentum_26 | 9966.09 | -33.91 | buy / partial / 직전 완료 봉 목표 비중 100%; 다음 봉 시가 가정 |
| v2 | trend_8_26 + momentum_26 | 9916.41 | -83.59 | buy / partial / 직전 완료 봉 목표 비중 100%; 다음 봉 시가 가정 |
| v2 | trend_8_26 AND breakout_8 | 9789.40 | -210.60 | sell / filled / 직전 완료 봉 목표 비중 0%; 다음 봉 시가 가정 |
| v2 | trend_8_26 + breakout_8 | 9743.70 | -256.30 | buy / filled / 직전 완료 봉 목표 비중 50%; 다음 봉 시가 가정 |
| v2 | trend_8_26 AND reversion_12 | 9810.77 | -189.23 | sell / filled / 직전 완료 봉 목표 비중 0%; 다음 봉 시가 가정 |
| v2 | trend_8_26 + reversion_12 | 9779.59 | -220.41 | buy / filled / 직전 완료 봉 목표 비중 50%; 다음 봉 시가 가정 |
| v2 | trend_8_26 AND volume_26 | 9858.88 | -141.12 | sell / filled / 직전 완료 봉 목표 비중 0%; 다음 봉 시가 가정 |
| v2 | trend_8_26 + volume_26 | 9810.54 | -189.46 | buy / filled / 직전 완료 봉 목표 비중 50%; 다음 봉 시가 가정 |
| v2 | momentum_26 AND breakout_8 | 9778.26 | -221.74 | sell / filled / 직전 완료 봉 목표 비중 0%; 다음 봉 시가 가정 |
| v2 | momentum_26 + breakout_8 | 9797.19 | -202.81 | buy / filled / 직전 완료 봉 목표 비중 50%; 다음 봉 시가 가정 |
| v2 | momentum_26 AND reversion_12 | 9955.97 | -44.03 | sell / filled / 직전 완료 봉 목표 비중 0%; 다음 봉 시가 가정 |
| v2 | momentum_26 + reversion_12 | 9833.28 | -166.72 | buy / filled / 직전 완료 봉 목표 비중 50%; 다음 봉 시가 가정 |
| v2 | momentum_26 AND volume_26 | 9791.42 | -208.58 | sell / filled / 직전 완료 봉 목표 비중 0%; 다음 봉 시가 가정 |
| v2 | momentum_26 + volume_26 | 9885.20 | -114.80 | buy / filled / 직전 완료 봉 목표 비중 50%; 다음 봉 시가 가정 |
| v2 | breakout_8 AND reversion_12 | 10000.00 | 0.00 | 대기 /  / 새 신호 대기 |
| v2 | breakout_8 + reversion_12 | 9661.83 | -338.17 | sell / filled / 직전 완료 봉 목표 비중 0%; 다음 봉 시가 가정 |
| v2 | breakout_8 AND volume_26 | 9796.56 | -203.44 | sell / filled / 직전 완료 봉 목표 비중 0%; 다음 봉 시가 가정 |
| v2 | breakout_8 + volume_26 | 9672.16 | -327.84 | sell / filled / 직전 완료 봉 목표 비중 0%; 다음 봉 시가 가정 |
| v2 | reversion_12 AND volume_26 | 10000.00 | 0.00 | 대기 /  / 새 신호 대기 |
| v2 | reversion_12 + volume_26 | 9707.85 | -292.15 | sell / filled / 직전 완료 봉 목표 비중 0%; 다음 봉 시가 가정 |

### 같은 기간의 비용·노출 비교 (사후 연구)

| 전략 | 비용 전 | 비용 후 | 100% 보유 | 같은 평균 노출 보유 | 평균 노출 |
|---|---:|---:|---:|---:|---:|
| cash | 0.00% | 0.00% | 0.97% | 0.00% | 0.00% |
| buy_hold | 1.40% | 0.97% | 0.97% | 0.97% | 100.00% |
| trend_8_26 | 1.71% | -2.88% | 0.97% | 0.55% | 56.05% |
| momentum_26 | 0.03% | -4.08% | 0.97% | 0.50% | 51.05% |
| breakout_8 | 0.14% | -16.40% | 0.97% | 0.23% | 23.42% |
| reversion_12 | -1.36% | -9.30% | 0.97% | 0.24% | 24.74% |
| volume_26 | -0.82% | -11.45% | 0.97% | 0.11% | 11.58% |
| trend_8_26 AND momentum_26 | 1.50% | -2.67% | 0.97% | 0.44% | 45.26% |
| trend_8_26 + momentum_26 | 0.87% | -3.48% | 0.97% | 0.52% | 53.55% |
| trend_8_26 AND breakout_8 | 0.71% | -10.84% | 0.97% | 0.15% | 15.26% |
| trend_8_26 + breakout_8 | 0.93% | -9.71% | 0.97% | 0.39% | 39.74% |
| trend_8_26 AND reversion_12 | 0.37% | -4.56% | 0.97% | 0.06% | 6.32% |
| trend_8_26 + reversion_12 | 0.17% | -5.76% | 0.97% | 0.39% | 40.40% |
| trend_8_26 AND volume_26 | 0.73% | -5.02% | 0.97% | 0.06% | 5.79% |
| trend_8_26 + volume_26 | 0.44% | -7.08% | 0.97% | 0.33% | 33.82% |
| momentum_26 AND breakout_8 | -0.09% | -11.17% | 0.97% | 0.15% | 15.53% |
| momentum_26 + breakout_8 | 0.09% | -10.27% | 0.97% | 0.36% | 37.24% |
| momentum_26 AND reversion_12 | -0.18% | -3.88% | 0.97% | 0.06% | 5.79% |
| momentum_26 + reversion_12 | -0.66% | -5.95% | 0.97% | 0.37% | 37.90% |
| momentum_26 AND volume_26 | -0.36% | -6.05% | 0.97% | 0.05% | 5.00% |
| momentum_26 + volume_26 | -0.39% | -7.07% | 0.97% | 0.30% | 31.32% |
| breakout_8 AND reversion_12 | 0.00% | 0.00% | 0.97% | 0.00% | 0.00% |
| breakout_8 + reversion_12 | -0.61% | -12.57% | 0.97% | 0.23% | 24.09% |
| breakout_8 AND volume_26 | -0.82% | -4.90% | 0.97% | 0.03% | 3.42% |
| breakout_8 + volume_26 | -0.34% | -13.06% | 0.97% | 0.17% | 17.51% |
| reversion_12 AND volume_26 | -0.20% | -5.11% | 0.97% | 0.04% | 3.95% |
| reversion_12 + volume_26 | -1.09% | -10.39% | 0.97% | 0.18% | 18.16% |

동일 구간·초기 자금, 종료 시 청산 비용 포함. 노출 맞춤은 사후 설명용이며 v2 실제 계좌 성과가 아닙니다.
[낙폭 분해·비용 영향·전체 구간](DIA/comparison.json)

[v1 전체 기록](DIA/accounts.json) · [v2 전체 기록](DIA/accounts-v2.json)

## MSFT 계좌

| 모델 | 전략 | 평가액 USD | 손익 USD | 최근 매매·이유 |
|---|---|---:|---:|---|
| v1 | cash | 10000.00 | 0.00 | 대기 /  / 새 신호 대기 |
| v1 | buy_hold | 10021.90 | 21.90 | buy /  / buy_hold: prior completed bar target 100%; next bar open simulation |
| v1 | trend_8_26 | 10021.90 | 21.90 | buy /  / trend_8_26: prior completed bar target 100%; next bar open simulation |
| v1 | momentum_26 | 10023.96 | 23.96 | buy /  / momentum_26: prior completed bar target 100%; next bar open simulation |
| v1 | breakout_8 | 9986.22 | -13.78 | buy /  / breakout_8: prior completed bar target 100%; next bar open simulation |
| v1 | reversion_12 | 10000.00 | 0.00 | 대기 /  / 새 신호 대기 |
| v1 | volume_26 | 9997.72 | -2.28 | sell /  / volume_26: prior completed bar target 0%; next bar open simulation |
| v1 | trend_8_26 AND momentum_26 | 10023.96 | 23.96 | buy /  / trend_8_26 AND momentum_26: prior completed bar target 100%; next bar open simulation |
| v1 | trend_8_26 + momentum_26 | 10022.93 | 22.93 | buy /  / trend_8_26 + momentum_26: prior completed bar target 100%; next bar open simulation |
| v1 | trend_8_26 AND breakout_8 | 9986.22 | -13.78 | buy /  / trend_8_26 AND breakout_8: prior completed bar target 100%; next bar open simulation |
| v1 | trend_8_26 + breakout_8 | 10004.03 | 4.03 | buy /  / trend_8_26 + breakout_8: prior completed bar target 100%; next bar open simulation |
| v1 | trend_8_26 AND reversion_12 | 10000.00 | 0.00 | 대기 /  / 새 신호 대기 |
| v1 | trend_8_26 + reversion_12 | 10010.91 | 10.91 | sell /  / trend_8_26 + reversion_12: prior completed bar target 50%; next bar open simulation |
| v1 | trend_8_26 AND volume_26 | 9997.72 | -2.28 | sell /  / trend_8_26 AND volume_26: prior completed bar target 0%; next bar open simulation |
| v1 | trend_8_26 + volume_26 | 10009.81 | 9.81 | sell /  / trend_8_26 + volume_26: prior completed bar target 50%; next bar open simulation |
| v1 | momentum_26 AND breakout_8 | 9986.22 | -13.78 | buy /  / momentum_26 AND breakout_8: prior completed bar target 100%; next bar open simulation |
| v1 | momentum_26 + breakout_8 | 10005.07 | 5.07 | buy /  / momentum_26 + breakout_8: prior completed bar target 100%; next bar open simulation |
| v1 | momentum_26 AND reversion_12 | 10000.00 | 0.00 | 대기 /  / 새 신호 대기 |
| v1 | momentum_26 + reversion_12 | 10011.95 | 11.95 | sell /  / momentum_26 + reversion_12: prior completed bar target 50%; next bar open simulation |
| v1 | momentum_26 AND volume_26 | 9997.72 | -2.28 | sell /  / momentum_26 AND volume_26: prior completed bar target 0%; next bar open simulation |
| v1 | momentum_26 + volume_26 | 10010.84 | 10.84 | sell /  / momentum_26 + volume_26: prior completed bar target 50%; next bar open simulation |
| v1 | breakout_8 AND reversion_12 | 10000.00 | 0.00 | 대기 /  / 새 신호 대기 |
| v1 | breakout_8 + reversion_12 | 9993.10 | -6.90 | buy /  / breakout_8 + reversion_12: prior completed bar target 50%; next bar open simulation |
| v1 | breakout_8 AND volume_26 | 10000.00 | 0.00 | 대기 /  / 새 신호 대기 |
| v1 | breakout_8 + volume_26 | 10011.95 | 11.95 | sell /  / breakout_8 + volume_26: prior completed bar target 50%; next bar open simulation |
| v1 | reversion_12 AND volume_26 | 10000.00 | 0.00 | 대기 /  / 새 신호 대기 |
| v1 | reversion_12 + volume_26 | 9998.84 | -1.16 | sell /  / reversion_12 + volume_26: prior completed bar target 0%; next bar open simulation |
| v2 | cash | 10000.00 | 0.00 | 대기 /  / 새 신호 대기 |
| v2 | buy_hold | 10006.66 | 6.66 | buy / partial / 직전 완료 봉 목표 비중 100%; 다음 봉 시가 가정 |
| v2 | trend_8_26 | 9889.19 | -110.81 | buy / partial / 직전 완료 봉 목표 비중 100%; 다음 봉 시가 가정 |
| v2 | momentum_26 | 10000.75 | 0.75 | buy / partial / 직전 완료 봉 목표 비중 100%; 다음 봉 시가 가정 |
| v2 | breakout_8 | 9909.42 | -90.58 | buy / partial / 직전 완료 봉 목표 비중 100%; 다음 봉 시가 가정 |
| v2 | reversion_12 | 9618.62 | -381.38 | sell / filled / 직전 완료 봉 목표 비중 0%; 다음 봉 시가 가정 |
| v2 | volume_26 | 9734.37 | -265.63 | sell / filled / 직전 완료 봉 목표 비중 0%; 다음 봉 시가 가정 |
| v2 | trend_8_26 AND momentum_26 | 9849.76 | -150.24 | buy / partial / 직전 완료 봉 목표 비중 100%; 다음 봉 시가 가정 |
| v2 | trend_8_26 + momentum_26 | 9945.08 | -54.92 | buy / partial / 직전 완료 봉 목표 비중 100%; 다음 봉 시가 가정 |
| v2 | trend_8_26 AND breakout_8 | 9747.43 | -252.57 | buy / partial / 직전 완료 봉 목표 비중 100%; 다음 봉 시가 가정 |
| v2 | trend_8_26 + breakout_8 | 9920.28 | -79.72 | buy / partial / 직전 완료 봉 목표 비중 100%; 다음 봉 시가 가정 |
| v2 | trend_8_26 AND reversion_12 | 9900.10 | -99.90 | sell / filled / 직전 완료 봉 목표 비중 0%; 다음 봉 시가 가정 |
| v2 | trend_8_26 + reversion_12 | 9752.65 | -247.35 | sell / filled / 직전 완료 봉 목표 비중 50%; 다음 봉 시가 가정 |
| v2 | trend_8_26 AND volume_26 | 9995.72 | -4.28 | sell / filled / 직전 완료 봉 목표 비중 0%; 다음 봉 시가 가정 |
| v2 | trend_8_26 + volume_26 | 9831.90 | -168.10 | sell / filled / 직전 완료 봉 목표 비중 50%; 다음 봉 시가 가정 |
| v2 | momentum_26 AND breakout_8 | 9904.27 | -95.73 | buy / partial / 직전 완료 봉 목표 비중 100%; 다음 봉 시가 가정 |
| v2 | momentum_26 + breakout_8 | 9955.01 | -44.99 | buy / partial / 직전 완료 봉 목표 비중 100%; 다음 봉 시가 가정 |
| v2 | momentum_26 AND reversion_12 | 9826.88 | -173.12 | sell / filled / 직전 완료 봉 목표 비중 0%; 다음 봉 시가 가정 |
| v2 | momentum_26 + reversion_12 | 9807.63 | -192.37 | sell / filled / 직전 완료 봉 목표 비중 50%; 다음 봉 시가 가정 |
| v2 | momentum_26 AND volume_26 | 9917.94 | -82.06 | sell / filled / 직전 완료 봉 목표 비중 0%; 다음 봉 시가 가정 |
| v2 | momentum_26 + volume_26 | 9887.33 | -112.67 | sell / filled / 직전 완료 봉 목표 비중 50%; 다음 봉 시가 가정 |
| v2 | breakout_8 AND reversion_12 | 10000.00 | 0.00 | 대기 /  / 새 신호 대기 |
| v2 | breakout_8 + reversion_12 | 9783.31 | -216.69 | buy / filled / 직전 완료 봉 목표 비중 50%; 다음 봉 시가 가정 |
| v2 | breakout_8 AND volume_26 | 9938.59 | -61.41 | sell / filled / 직전 완료 봉 목표 비중 0%; 다음 봉 시가 가정 |
| v2 | breakout_8 + volume_26 | 9842.26 | -157.74 | sell / filled / 직전 완료 봉 목표 비중 50%; 다음 봉 시가 가정 |
| v2 | reversion_12 AND volume_26 | 9762.04 | -237.96 | sell / filled / 직전 완료 봉 목표 비중 0%; 다음 봉 시가 가정 |
| v2 | reversion_12 + volume_26 | 9676.20 | -323.80 | sell / filled / 직전 완료 봉 목표 비중 0%; 다음 봉 시가 가정 |

### 같은 기간의 비용·노출 비교 (사후 연구)

| 전략 | 비용 전 | 비용 후 | 100% 보유 | 같은 평균 노출 보유 | 평균 노출 |
|---|---:|---:|---:|---:|---:|
| cash | 0.00% | 0.00% | 8.03% | 0.00% | 0.00% |
| buy_hold | 8.48% | 8.03% | 8.03% | 8.03% | 100.00% |
| trend_8_26 | 3.23% | -0.60% | 8.03% | 4.67% | 59.47% |
| momentum_26 | 1.27% | -4.52% | 8.03% | 4.59% | 58.42% |
| breakout_8 | 4.75% | -10.32% | 8.03% | 1.64% | 21.32% |
| reversion_12 | -4.05% | -12.52% | 8.03% | 1.81% | 23.42% |
| volume_26 | 5.29% | -3.19% | 8.03% | 0.62% | 8.16% |
| trend_8_26 AND momentum_26 | -0.14% | -5.84% | 8.03% | 4.10% | 52.37% |
| trend_8_26 + momentum_26 | 2.26% | -2.56% | 8.03% | 4.63% | 58.95% |
| trend_8_26 AND breakout_8 | 0.35% | -10.41% | 8.03% | 1.09% | 14.21% |
| trend_8_26 + breakout_8 | 4.02% | -5.17% | 8.03% | 3.14% | 40.40% |
| trend_8_26 AND reversion_12 | -3.39% | -8.52% | 8.03% | 0.54% | 7.11% |
| trend_8_26 + reversion_12 | -0.45% | -6.35% | 8.03% | 3.23% | 41.45% |
| trend_8_26 AND volume_26 | 6.34% | 3.26% | 8.03% | 0.20% | 2.63% |
| trend_8_26 + volume_26 | 4.28% | -1.08% | 8.03% | 2.62% | 33.82% |
| momentum_26 AND breakout_8 | 2.29% | -8.67% | 8.03% | 1.05% | 13.68% |
| momentum_26 + breakout_8 | 3.01% | -6.87% | 8.03% | 3.10% | 39.87% |
| momentum_26 AND reversion_12 | -2.74% | -8.67% | 8.03% | 0.62% | 8.16% |
| momentum_26 + reversion_12 | -1.40% | -8.22% | 8.03% | 3.19% | 40.93% |
| momentum_26 AND volume_26 | 1.86% | -1.92% | 8.03% | 0.24% | 3.16% |
| momentum_26 + volume_26 | 3.29% | -2.42% | 8.03% | 2.58% | 33.29% |
| breakout_8 AND reversion_12 | 0.00% | 0.00% | 8.03% | 0.00% | 0.00% |
| breakout_8 + reversion_12 | 0.28% | -10.86% | 8.03% | 1.72% | 22.38% |
| breakout_8 AND volume_26 | 2.07% | -0.47% | 8.03% | 0.14% | 1.84% |
| breakout_8 + volume_26 | 5.04% | -5.63% | 8.03% | 1.13% | 14.74% |
| reversion_12 AND volume_26 | -2.27% | -5.89% | 8.03% | 0.26% | 3.42% |
| reversion_12 + volume_26 | 0.54% | -7.76% | 8.03% | 1.21% | 15.79% |

동일 구간·초기 자금, 종료 시 청산 비용 포함. 노출 맞춤은 사후 설명용이며 v2 실제 계좌 성과가 아닙니다.
[낙폭 분해·비용 영향·전체 구간](MSFT/comparison.json)

[v1 전체 기록](MSFT/accounts.json) · [v2 전체 기록](MSFT/accounts-v2.json)

## JPM 계좌

| 모델 | 전략 | 평가액 USD | 손익 USD | 최근 매매·이유 |
|---|---|---:|---:|---|
| v1 | cash | 10000.00 | 0.00 | 대기 /  / 새 신호 대기 |
| v1 | buy_hold | 9972.79 | -27.21 | buy /  / buy_hold: prior completed bar target 100%; next bar open simulation |
| v1 | trend_8_26 | 9985.49 | -14.51 | buy /  / trend_8_26: prior completed bar target 100%; next bar open simulation |
| v1 | momentum_26 | 9945.63 | -54.37 | sell /  / momentum_26: prior completed bar target 0%; next bar open simulation |
| v1 | breakout_8 | 10000.00 | 0.00 | 대기 /  / 새 신호 대기 |
| v1 | reversion_12 | 9961.87 | -38.13 | sell /  / reversion_12: prior completed bar target 0%; next bar open simulation |
| v1 | volume_26 | 10000.00 | 0.00 | 대기 /  / 새 신호 대기 |
| v1 | trend_8_26 AND momentum_26 | 10000.00 | 0.00 | 대기 /  / 새 신호 대기 |
| v1 | trend_8_26 + momentum_26 | 9965.50 | -34.50 | sell /  / trend_8_26 + momentum_26: prior completed bar target 50%; next bar open simulation |
| v1 | trend_8_26 AND breakout_8 | 10000.00 | 0.00 | 대기 /  / 새 신호 대기 |
| v1 | trend_8_26 + breakout_8 | 9992.72 | -7.28 | sell /  / trend_8_26 + breakout_8: prior completed bar target 50%; next bar open simulation |
| v1 | trend_8_26 AND reversion_12 | 10000.00 | 0.00 | 대기 /  / 새 신호 대기 |
| v1 | trend_8_26 + reversion_12 | 9993.61 | -6.39 | buy /  / trend_8_26 + reversion_12: prior completed bar target 50%; next bar open simulation |
| v1 | trend_8_26 AND volume_26 | 10000.00 | 0.00 | 대기 /  / 새 신호 대기 |
| v1 | trend_8_26 + volume_26 | 9992.72 | -7.28 | sell /  / trend_8_26 + volume_26: prior completed bar target 50%; next bar open simulation |
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
| v2 | buy_hold | 9968.36 | -31.64 | buy / partial / 직전 완료 봉 목표 비중 100%; 다음 봉 시가 가정 |
| v2 | trend_8_26 | 9899.34 | -100.66 | buy / partial / 직전 완료 봉 목표 비중 100%; 다음 봉 시가 가정 |
| v2 | momentum_26 | 9499.19 | -500.81 | sell / filled / 직전 완료 봉 목표 비중 0%; 다음 봉 시가 가정 |
| v2 | breakout_8 | 9426.01 | -573.99 | sell / filled / 직전 완료 봉 목표 비중 0%; 다음 봉 시가 가정 |
| v2 | reversion_12 | 10005.24 | 5.24 | sell / filled / 직전 완료 봉 목표 비중 0%; 다음 봉 시가 가정 |
| v2 | volume_26 | 9826.70 | -173.30 | sell / filled / 직전 완료 봉 목표 비중 0%; 다음 봉 시가 가정 |
| v2 | trend_8_26 AND momentum_26 | 9936.83 | -63.17 | sell / filled / 직전 완료 봉 목표 비중 0%; 다음 봉 시가 가정 |
| v2 | trend_8_26 + momentum_26 | 9697.71 | -302.29 | sell / filled / 직전 완료 봉 목표 비중 50%; 다음 봉 시가 가정 |
| v2 | trend_8_26 AND breakout_8 | 9420.50 | -579.50 | sell / filled / 직전 완료 봉 목표 비중 0%; 다음 봉 시가 가정 |
| v2 | trend_8_26 + breakout_8 | 9660.36 | -339.64 | sell / filled / 직전 완료 봉 목표 비중 50%; 다음 봉 시가 가정 |
| v2 | trend_8_26 AND reversion_12 | 9981.61 | -18.39 | sell / filled / 직전 완료 봉 목표 비중 0%; 다음 봉 시가 가정 |
| v2 | trend_8_26 + reversion_12 | 9973.16 | -26.84 | buy / filled / 직전 완료 봉 목표 비중 50%; 다음 봉 시가 가정 |
| v2 | trend_8_26 AND volume_26 | 9800.30 | -199.70 | sell / filled / 직전 완료 봉 목표 비중 0%; 다음 봉 시가 가정 |
| v2 | trend_8_26 + volume_26 | 9863.45 | -136.55 | sell / filled / 직전 완료 봉 목표 비중 50%; 다음 봉 시가 가정 |
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
| cash | 0.00% | 0.00% | -1.44% | -0.00% | 0.00% |
| buy_hold | -1.03% | -1.44% | -1.44% | -1.44% | 100.00% |
| trend_8_26 | 0.54% | -2.78% | -1.44% | -0.78% | 53.95% |
| momentum_26 | -1.88% | -7.48% | -1.44% | -0.68% | 46.84% |
| breakout_8 | -3.35% | -17.61% | -1.44% | -0.28% | 19.47% |
| reversion_12 | 4.33% | -9.55% | -1.44% | -0.38% | 26.32% |
| volume_26 | -0.72% | -6.78% | -1.44% | -0.10% | 6.84% |
| trend_8_26 AND momentum_26 | 1.03% | -2.71% | -1.44% | -0.62% | 42.37% |
| trend_8_26 + momentum_26 | -0.67% | -5.15% | -1.44% | -0.73% | 50.40% |
| trend_8_26 AND breakout_8 | -3.43% | -13.42% | -1.44% | -0.18% | 12.37% |
| trend_8_26 + breakout_8 | -1.41% | -10.30% | -1.44% | -0.53% | 36.72% |
| trend_8_26 AND reversion_12 | 2.82% | -3.46% | -1.44% | -0.10% | 6.58% |
| trend_8_26 + reversion_12 | 2.44% | -5.84% | -1.44% | -0.58% | 40.14% |
| trend_8_26 AND volume_26 | -1.19% | -5.26% | -1.44% | -0.06% | 4.21% |
| trend_8_26 + volume_26 | -0.08% | -4.80% | -1.44% | -0.44% | 30.40% |
| momentum_26 AND breakout_8 | -2.23% | -11.98% | -1.44% | -0.17% | 11.84% |
| momentum_26 + breakout_8 | -2.60% | -12.49% | -1.44% | -0.48% | 33.16% |
| momentum_26 AND reversion_12 | 2.89% | -3.80% | -1.44% | -0.08% | 5.53% |
| momentum_26 + reversion_12 | 1.20% | -7.36% | -1.44% | -0.53% | 36.58% |
| momentum_26 AND volume_26 | -0.41% | -3.30% | -1.44% | -0.04% | 2.89% |
| momentum_26 + volume_26 | -1.28% | -6.54% | -1.44% | -0.39% | 26.85% |
| breakout_8 AND reversion_12 | 0.00% | 0.00% | -1.44% | -0.00% | 0.00% |
| breakout_8 + reversion_12 | 0.44% | -12.40% | -1.44% | -0.33% | 22.90% |
| breakout_8 AND volume_26 | -1.13% | -2.78% | -1.44% | -0.02% | 1.05% |
| breakout_8 + volume_26 | -2.03% | -11.25% | -1.44% | -0.19% | 13.16% |
| reversion_12 AND volume_26 | 1.25% | -2.10% | -1.44% | -0.05% | 3.42% |
| reversion_12 + volume_26 | 1.78% | -7.41% | -1.44% | -0.24% | 16.58% |

동일 구간·초기 자금, 종료 시 청산 비용 포함. 노출 맞춤은 사후 설명용이며 v2 실제 계좌 성과가 아닙니다.
[낙폭 분해·비용 영향·전체 구간](JPM/comparison.json)

[v1 전체 기록](JPM/accounts.json) · [v2 전체 기록](JPM/accounts-v2.json)

## XOM 계좌

| 모델 | 전략 | 평가액 USD | 손익 USD | 최근 매매·이유 |
|---|---|---:|---:|---|
| v1 | cash | 10000.00 | 0.00 | 대기 /  / 새 신호 대기 |
| v1 | buy_hold | 9967.51 | -32.49 | buy /  / buy_hold: prior completed bar target 100%; next bar open simulation |
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
| v2 | buy_hold | 10216.53 | 216.53 | buy / partial / 직전 완료 봉 목표 비중 100%; 다음 봉 시가 가정 |
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
| cash | 0.00% | 0.00% | 7.91% | 0.00% | 0.00% |
| buy_hold | 8.37% | 7.91% | 7.91% | 7.91% | 100.00% |
| trend_8_26 | 1.00% | -3.16% | 7.91% | 4.93% | 62.89% |
| momentum_26 | -0.51% | -7.75% | 7.91% | 5.47% | 69.74% |
| breakout_8 | -3.59% | -20.53% | 7.91% | 1.77% | 22.89% |
| reversion_12 | 6.17% | -4.41% | 7.91% | 1.65% | 21.32% |
| volume_26 | 4.95% | -2.69% | 7.91% | 0.39% | 5.00% |
| trend_8_26 AND momentum_26 | -0.45% | -4.95% | 7.91% | 4.51% | 57.63% |
| trend_8_26 + momentum_26 | 0.25% | -5.28% | 7.91% | 5.20% | 66.32% |
| trend_8_26 AND breakout_8 | -1.20% | -14.70% | 7.91% | 1.38% | 17.89% |
| trend_8_26 + breakout_8 | -1.30% | -12.07% | 7.91% | 3.34% | 42.90% |
| trend_8_26 AND reversion_12 | 1.89% | -3.93% | 7.91% | 0.63% | 8.16% |
| trend_8_26 + reversion_12 | 3.58% | -3.58% | 7.91% | 3.28% | 42.11% |
| trend_8_26 AND volume_26 | 2.54% | -1.67% | 7.91% | 0.20% | 2.63% |
| trend_8_26 + volume_26 | 2.97% | -2.52% | 7.91% | 2.64% | 33.95% |
| momentum_26 AND breakout_8 | -3.06% | -18.40% | 7.91% | 1.59% | 20.53% |
| momentum_26 + breakout_8 | -2.03% | -14.36% | 7.91% | 3.61% | 46.32% |
| momentum_26 AND reversion_12 | 2.64% | -4.43% | 7.91% | 0.71% | 9.21% |
| momentum_26 + reversion_12 | 2.81% | -4.50% | 7.91% | 3.55% | 45.53% |
| momentum_26 AND volume_26 | 2.42% | -1.79% | 7.91% | 0.20% | 2.63% |
| momentum_26 + volume_26 | 2.21% | -3.85% | 7.91% | 2.91% | 37.37% |
| breakout_8 AND reversion_12 | 0.00% | 0.00% | 7.91% | 0.00% | 0.00% |
| breakout_8 + reversion_12 | 1.19% | -12.48% | 7.91% | 1.71% | 22.11% |
| breakout_8 AND volume_26 | 0.60% | -0.66% | 7.91% | 0.06% | 0.79% |
| breakout_8 + volume_26 | 0.60% | -10.94% | 7.91% | 1.08% | 13.96% |
| reversion_12 AND volume_26 | 1.84% | -1.11% | 7.91% | 0.14% | 1.84% |
| reversion_12 + volume_26 | 5.57% | -2.95% | 7.91% | 1.02% | 13.16% |

동일 구간·초기 자금, 종료 시 청산 비용 포함. 노출 맞춤은 사후 설명용이며 v2 실제 계좌 성과가 아닙니다.
[낙폭 분해·비용 영향·전체 구간](XOM/comparison.json)

[v1 전체 기록](XOM/accounts.json) · [v2 전체 기록](XOM/accounts-v2.json)

## JNJ 계좌

| 모델 | 전략 | 평가액 USD | 손익 USD | 최근 매매·이유 |
|---|---|---:|---:|---|
| v1 | cash | 10000.00 | 0.00 | 대기 /  / 새 신호 대기 |
| v1 | buy_hold | 9930.26 | -69.74 | buy /  / buy_hold: prior completed bar target 100%; next bar open simulation |
| v1 | trend_8_26 | 9930.26 | -69.74 | buy /  / trend_8_26: prior completed bar target 100%; next bar open simulation |
| v1 | momentum_26 | 9930.26 | -69.74 | buy /  / momentum_26: prior completed bar target 100%; next bar open simulation |
| v1 | breakout_8 | 10000.00 | 0.00 | 대기 /  / 새 신호 대기 |
| v1 | reversion_12 | 10000.00 | 0.00 | 대기 /  / 새 신호 대기 |
| v1 | volume_26 | 10000.00 | 0.00 | 대기 /  / 새 신호 대기 |
| v1 | trend_8_26 AND momentum_26 | 9930.26 | -69.74 | buy /  / trend_8_26 AND momentum_26: prior completed bar target 100%; next bar open simulation |
| v1 | trend_8_26 + momentum_26 | 9930.26 | -69.74 | buy /  / trend_8_26 + momentum_26: prior completed bar target 100%; next bar open simulation |
| v1 | trend_8_26 AND breakout_8 | 10000.00 | 0.00 | 대기 /  / 새 신호 대기 |
| v1 | trend_8_26 + breakout_8 | 9965.07 | -34.93 | buy /  / trend_8_26 + breakout_8: prior completed bar target 50%; next bar open simulation |
| v1 | trend_8_26 AND reversion_12 | 10000.00 | 0.00 | 대기 /  / 새 신호 대기 |
| v1 | trend_8_26 + reversion_12 | 9965.07 | -34.93 | buy /  / trend_8_26 + reversion_12: prior completed bar target 50%; next bar open simulation |
| v1 | trend_8_26 AND volume_26 | 10000.00 | 0.00 | 대기 /  / 새 신호 대기 |
| v1 | trend_8_26 + volume_26 | 9965.07 | -34.93 | buy /  / trend_8_26 + volume_26: prior completed bar target 50%; next bar open simulation |
| v1 | momentum_26 AND breakout_8 | 10000.00 | 0.00 | 대기 /  / 새 신호 대기 |
| v1 | momentum_26 + breakout_8 | 9965.07 | -34.93 | buy /  / momentum_26 + breakout_8: prior completed bar target 50%; next bar open simulation |
| v1 | momentum_26 AND reversion_12 | 10000.00 | 0.00 | 대기 /  / 새 신호 대기 |
| v1 | momentum_26 + reversion_12 | 9965.07 | -34.93 | buy /  / momentum_26 + reversion_12: prior completed bar target 50%; next bar open simulation |
| v1 | momentum_26 AND volume_26 | 10000.00 | 0.00 | 대기 /  / 새 신호 대기 |
| v1 | momentum_26 + volume_26 | 9965.07 | -34.93 | buy /  / momentum_26 + volume_26: prior completed bar target 50%; next bar open simulation |
| v1 | breakout_8 AND reversion_12 | 10000.00 | 0.00 | 대기 /  / 새 신호 대기 |
| v1 | breakout_8 + reversion_12 | 10000.00 | 0.00 | 대기 /  / 새 신호 대기 |
| v1 | breakout_8 AND volume_26 | 10000.00 | 0.00 | 대기 /  / 새 신호 대기 |
| v1 | breakout_8 + volume_26 | 10000.00 | 0.00 | 대기 /  / 새 신호 대기 |
| v1 | reversion_12 AND volume_26 | 10000.00 | 0.00 | 대기 /  / 새 신호 대기 |
| v1 | reversion_12 + volume_26 | 10000.00 | 0.00 | 대기 /  / 새 신호 대기 |
| v2 | cash | 10000.00 | 0.00 | 대기 /  / 새 신호 대기 |
| v2 | buy_hold | 9818.06 | -181.94 | 중단: 손실 한도 / buy / partial / 직전 완료 봉 목표 비중 100%; 다음 봉 시가 가정 |
| v2 | trend_8_26 | 9818.06 | -181.94 | 중단: 손실 한도 / buy / partial / 직전 완료 봉 목표 비중 100%; 다음 봉 시가 가정 |
| v2 | momentum_26 | 9818.06 | -181.94 | 중단: 손실 한도 / buy / partial / 직전 완료 봉 목표 비중 100%; 다음 봉 시가 가정 |
| v2 | breakout_8 | 9343.39 | -656.61 | 중단: 손실 한도 / sell / filled / 직전 완료 봉 목표 비중 0%; 다음 봉 시가 가정 |
| v2 | reversion_12 | 9887.49 | -112.51 | sell / filled / 직전 완료 봉 목표 비중 0%; 다음 봉 시가 가정 |
| v2 | volume_26 | 9791.36 | -208.64 | sell / filled / 직전 완료 봉 목표 비중 0%; 다음 봉 시가 가정 |
| v2 | trend_8_26 AND momentum_26 | 9818.06 | -181.94 | 중단: 손실 한도 / buy / partial / 직전 완료 봉 목표 비중 100%; 다음 봉 시가 가정 |
| v2 | trend_8_26 + momentum_26 | 9818.06 | -181.94 | 중단: 손실 한도 / buy / partial / 직전 완료 봉 목표 비중 100%; 다음 봉 시가 가정 |
| v2 | trend_8_26 AND breakout_8 | 9419.39 | -580.61 | 중단: 손실 한도 / sell / filled / 직전 완료 봉 목표 비중 0%; 다음 봉 시가 가정 |
| v2 | trend_8_26 + breakout_8 | 9635.05 | -364.95 | buy / filled / 직전 완료 봉 목표 비중 50%; 다음 봉 시가 가정 |
| v2 | trend_8_26 AND reversion_12 | 10134.68 | 134.68 | sell / filled / 직전 완료 봉 목표 비중 0%; 다음 봉 시가 가정 |
| v2 | trend_8_26 + reversion_12 | 9732.92 | -267.08 | 중단: 손실 한도 / sell / filled / 직전 완료 봉 목표 비중 0%; 다음 봉 시가 가정 |
| v2 | trend_8_26 AND volume_26 | 9870.71 | -129.29 | sell / filled / 직전 완료 봉 목표 비중 0%; 다음 봉 시가 가정 |
| v2 | trend_8_26 + volume_26 | 9883.20 | -116.80 | 중단: 손실 한도 / buy / filled / 직전 완료 봉 목표 비중 50%; 다음 봉 시가 가정 |
| v2 | momentum_26 AND breakout_8 | 9598.70 | -401.30 | sell / filled / 직전 완료 봉 목표 비중 0%; 다음 봉 시가 가정 |
| v2 | momentum_26 + breakout_8 | 9637.44 | -362.56 | buy / filled / 직전 완료 봉 목표 비중 50%; 다음 봉 시가 가정 |
| v2 | momentum_26 AND reversion_12 | 10134.68 | 134.68 | sell / filled / 직전 완료 봉 목표 비중 0%; 다음 봉 시가 가정 |
| v2 | momentum_26 + reversion_12 | 9732.92 | -267.08 | 중단: 손실 한도 / sell / filled / 직전 완료 봉 목표 비중 0%; 다음 봉 시가 가정 |
| v2 | momentum_26 AND volume_26 | 9920.93 | -79.07 | sell / filled / 직전 완료 봉 목표 비중 0%; 다음 봉 시가 가정 |
| v2 | momentum_26 + volume_26 | 9883.20 | -116.80 | 중단: 손실 한도 / buy / filled / 직전 완료 봉 목표 비중 50%; 다음 봉 시가 가정 |
| v2 | breakout_8 AND reversion_12 | 10000.00 | 0.00 | 대기 /  / 새 신호 대기 |
| v2 | breakout_8 + reversion_12 | 9678.21 | -321.79 | sell / filled / 직전 완료 봉 목표 비중 0%; 다음 봉 시가 가정 |
| v2 | breakout_8 AND volume_26 | 9814.17 | -185.83 | sell / filled / 직전 완료 봉 목표 비중 0%; 다음 봉 시가 가정 |
| v2 | breakout_8 + volume_26 | 9610.69 | -389.31 | sell / filled / 직전 완료 봉 목표 비중 0%; 다음 봉 시가 가정 |
| v2 | reversion_12 AND volume_26 | 9886.24 | -113.76 | sell / filled / 직전 완료 봉 목표 비중 0%; 다음 봉 시가 가정 |
| v2 | reversion_12 + volume_26 | 9860.31 | -139.69 | sell / filled / 직전 완료 봉 목표 비중 0%; 다음 봉 시가 가정 |

### 같은 기간의 비용·노출 비교 (사후 연구)

| 전략 | 비용 전 | 비용 후 | 100% 보유 | 같은 평균 노출 보유 | 평균 노출 |
|---|---:|---:|---:|---:|---:|
| cash | 0.00% | 0.00% | -5.46% | -0.00% | 0.00% |
| buy_hold | -5.06% | -5.46% | -5.46% | -5.46% | 100.00% |
| trend_8_26 | 3.91% | 1.32% | -5.46% | -2.65% | 47.37% |
| momentum_26 | 1.43% | -2.33% | -5.46% | -2.60% | 46.58% |
| breakout_8 | -0.32% | -17.14% | -5.46% | -1.20% | 21.32% |
| reversion_12 | -6.50% | -15.47% | -5.46% | -1.63% | 28.95% |
| volume_26 | -1.33% | -8.13% | -5.46% | -0.39% | 6.84% |
| trend_8_26 AND momentum_26 | 3.76% | 0.33% | -5.46% | -2.43% | 43.42% |
| trend_8_26 + momentum_26 | 2.67% | -0.52% | -5.46% | -2.63% | 46.98% |
| trend_8_26 AND breakout_8 | 0.73% | -11.94% | -5.46% | -0.88% | 15.53% |
| trend_8_26 + breakout_8 | 1.80% | -8.16% | -5.46% | -1.93% | 34.35% |
| trend_8_26 AND reversion_12 | 1.85% | -1.10% | -5.46% | -0.24% | 4.21% |
| trend_8_26 + reversion_12 | -1.40% | -6.86% | -5.46% | -2.14% | 38.16% |
| trend_8_26 AND volume_26 | 1.59% | -0.53% | -5.46% | -0.09% | 1.58% |
| trend_8_26 + volume_26 | 1.29% | -2.90% | -5.46% | -1.53% | 27.11% |
| momentum_26 AND breakout_8 | 2.15% | -9.94% | -5.46% | -0.84% | 14.74% |
| momentum_26 + breakout_8 | 0.58% | -9.83% | -5.46% | -1.91% | 33.95% |
| momentum_26 AND reversion_12 | 0.24% | -3.07% | -5.46% | -0.28% | 5.00% |
| momentum_26 + reversion_12 | -2.58% | -8.56% | -5.46% | -2.12% | 37.77% |
| momentum_26 AND volume_26 | 0.88% | -1.21% | -5.46% | -0.09% | 1.58% |
| momentum_26 + volume_26 | 0.07% | -4.66% | -5.46% | -1.51% | 26.71% |
| breakout_8 AND reversion_12 | 0.00% | 0.00% | -5.46% | -0.00% | 0.00% |
| breakout_8 + reversion_12 | -3.44% | -15.78% | -5.46% | -1.42% | 25.14% |
| breakout_8 AND volume_26 | -0.11% | -2.19% | -5.46% | -0.09% | 1.58% |
| breakout_8 + volume_26 | -0.82% | -12.02% | -5.46% | -0.80% | 14.09% |
| reversion_12 AND volume_26 | -2.65% | -5.47% | -5.46% | -0.16% | 2.89% |
| reversion_12 + volume_26 | -3.94% | -11.13% | -5.46% | -1.01% | 17.90% |

동일 구간·초기 자금, 종료 시 청산 비용 포함. 노출 맞춤은 사후 설명용이며 v2 실제 계좌 성과가 아닙니다.
[낙폭 분해·비용 영향·전체 구간](JNJ/comparison.json)

[v1 전체 기록](JNJ/accounts.json) · [v2 전체 기록](JNJ/accounts-v2.json)

## CAT 계좌

| 모델 | 전략 | 평가액 USD | 손익 USD | 최근 매매·이유 |
|---|---|---:|---:|---|
| v1 | cash | 10000.00 | 0.00 | 대기 /  / 새 신호 대기 |
| v1 | buy_hold | 9955.35 | -44.65 | buy /  / buy_hold: prior completed bar target 100%; next bar open simulation |
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
| v2 | buy_hold | 9101.20 | -898.80 | 중단: 손실 한도 / buy / partial / 직전 완료 봉 목표 비중 100%; 다음 봉 시가 가정 |
| v2 | trend_8_26 | 9941.61 | -58.39 | sell / filled / 직전 완료 봉 목표 비중 0%; 다음 봉 시가 가정 |
| v2 | momentum_26 | 10014.59 | 14.59 | sell / filled / 직전 완료 봉 목표 비중 0%; 다음 봉 시가 가정 |
| v2 | breakout_8 | 9806.46 | -193.54 | sell / filled / 직전 완료 봉 목표 비중 0%; 다음 봉 시가 가정 |
| v2 | reversion_12 | 8974.10 | -1025.90 | 중단: 손실 한도 / buy / partial / 직전 완료 봉 목표 비중 100%; 다음 봉 시가 가정 |
| v2 | volume_26 | 9230.75 | -769.25 | 중단: 손실 한도 / buy / partial / 직전 완료 봉 목표 비중 100%; 다음 봉 시가 가정 |
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
| v2 | reversion_12 AND volume_26 | 9166.90 | -833.10 | 중단: 손실 한도 / buy / partial / 직전 완료 봉 목표 비중 100%; 다음 봉 시가 가정 |
| v2 | reversion_12 + volume_26 | 9349.33 | -650.67 | 중단: 손실 한도 / sell / filled / 직전 완료 봉 목표 비중 50%; 다음 봉 시가 가정 |

### 같은 기간의 비용·노출 비교 (사후 연구)

| 전략 | 비용 전 | 비용 후 | 100% 보유 | 같은 평균 노출 보유 | 평균 노출 |
|---|---:|---:|---:|---:|---:|
| cash | 0.00% | 0.00% | -9.79% | -0.00% | 0.00% |
| buy_hold | -9.41% | -9.79% | -9.79% | -9.79% | 100.00% |
| trend_8_26 | 0.19% | -3.12% | -9.79% | -5.19% | 53.16% |
| momentum_26 | -4.02% | -9.50% | -9.79% | -5.01% | 51.32% |
| breakout_8 | -3.57% | -16.40% | -9.79% | -1.46% | 15.00% |
| reversion_12 | -4.23% | -15.21% | -9.79% | -2.49% | 25.53% |
| volume_26 | -2.55% | -10.03% | -9.79% | -0.82% | 8.42% |
| trend_8_26 AND momentum_26 | -1.32% | -5.77% | -9.79% | -4.44% | 45.53% |
| trend_8_26 + momentum_26 | -1.92% | -6.35% | -9.79% | -5.10% | 52.24% |
| trend_8_26 AND breakout_8 | -1.46% | -9.02% | -9.79% | -0.77% | 7.89% |
| trend_8_26 + breakout_8 | -1.67% | -9.79% | -9.79% | -3.32% | 34.08% |
| trend_8_26 AND reversion_12 | 0.78% | -5.38% | -9.79% | -0.69% | 7.11% |
| trend_8_26 + reversion_12 | -1.98% | -8.77% | -9.79% | -3.84% | 39.35% |
| trend_8_26 AND volume_26 | 2.63% | -0.76% | -9.79% | -0.28% | 2.89% |
| trend_8_26 + volume_26 | -1.13% | -6.41% | -9.79% | -3.00% | 30.79% |
| momentum_26 AND breakout_8 | -2.95% | -11.51% | -9.79% | -0.90% | 9.21% |
| momentum_26 + breakout_8 | -3.75% | -12.99% | -9.79% | -3.23% | 33.16% |
| momentum_26 AND reversion_12 | -3.04% | -8.96% | -9.79% | -0.56% | 5.79% |
| momentum_26 + reversion_12 | -4.07% | -11.46% | -9.79% | -3.75% | 38.43% |
| momentum_26 AND volume_26 | 1.58% | -0.53% | -9.79% | -0.15% | 1.58% |
| momentum_26 + volume_26 | -3.23% | -8.78% | -9.79% | -2.91% | 29.87% |
| breakout_8 AND reversion_12 | 0.00% | 0.00% | -9.79% | -0.00% | 0.00% |
| breakout_8 + reversion_12 | -3.85% | -14.90% | -9.79% | -1.97% | 20.27% |
| breakout_8 AND volume_26 | 0.78% | -0.48% | -9.79% | -0.08% | 0.79% |
| breakout_8 + volume_26 | -3.03% | -12.53% | -9.79% | -1.14% | 11.72% |
| reversion_12 AND volume_26 | -1.25% | -5.71% | -9.79% | -0.51% | 5.26% |
| reversion_12 + volume_26 | -3.36% | -11.91% | -9.79% | -1.65% | 16.98% |

동일 구간·초기 자금, 종료 시 청산 비용 포함. 노출 맞춤은 사후 설명용이며 v2 실제 계좌 성과가 아닙니다.
[낙폭 분해·비용 영향·전체 구간](CAT/comparison.json)

[v1 전체 기록](CAT/accounts.json) · [v2 전체 기록](CAT/accounts-v2.json)

## WMT 계좌

| 모델 | 전략 | 평가액 USD | 손익 USD | 최근 매매·이유 |
|---|---|---:|---:|---|
| v1 | cash | 10000.00 | 0.00 | 대기 /  / 새 신호 대기 |
| v1 | buy_hold | 9950.32 | -49.68 | buy /  / buy_hold: prior completed bar target 100%; next bar open simulation |
| v1 | trend_8_26 | 9950.32 | -49.68 | buy /  / trend_8_26: prior completed bar target 100%; next bar open simulation |
| v1 | momentum_26 | 9950.32 | -49.68 | buy /  / momentum_26: prior completed bar target 100%; next bar open simulation |
| v1 | breakout_8 | 10000.00 | 0.00 | 대기 /  / 새 신호 대기 |
| v1 | reversion_12 | 10000.00 | 0.00 | 대기 /  / 새 신호 대기 |
| v1 | volume_26 | 10000.00 | 0.00 | 대기 /  / 새 신호 대기 |
| v1 | trend_8_26 AND momentum_26 | 9950.32 | -49.68 | buy /  / trend_8_26 AND momentum_26: prior completed bar target 100%; next bar open simulation |
| v1 | trend_8_26 + momentum_26 | 9950.32 | -49.68 | buy /  / trend_8_26 + momentum_26: prior completed bar target 100%; next bar open simulation |
| v1 | trend_8_26 AND breakout_8 | 10000.00 | 0.00 | 대기 /  / 새 신호 대기 |
| v1 | trend_8_26 + breakout_8 | 9975.10 | -24.90 | buy /  / trend_8_26 + breakout_8: prior completed bar target 50%; next bar open simulation |
| v1 | trend_8_26 AND reversion_12 | 10000.00 | 0.00 | 대기 /  / 새 신호 대기 |
| v1 | trend_8_26 + reversion_12 | 9975.10 | -24.90 | buy /  / trend_8_26 + reversion_12: prior completed bar target 50%; next bar open simulation |
| v1 | trend_8_26 AND volume_26 | 10000.00 | 0.00 | 대기 /  / 새 신호 대기 |
| v1 | trend_8_26 + volume_26 | 9975.10 | -24.90 | buy /  / trend_8_26 + volume_26: prior completed bar target 50%; next bar open simulation |
| v1 | momentum_26 AND breakout_8 | 10000.00 | 0.00 | 대기 /  / 새 신호 대기 |
| v1 | momentum_26 + breakout_8 | 9975.10 | -24.90 | buy /  / momentum_26 + breakout_8: prior completed bar target 50%; next bar open simulation |
| v1 | momentum_26 AND reversion_12 | 10000.00 | 0.00 | 대기 /  / 새 신호 대기 |
| v1 | momentum_26 + reversion_12 | 9975.10 | -24.90 | buy /  / momentum_26 + reversion_12: prior completed bar target 50%; next bar open simulation |
| v1 | momentum_26 AND volume_26 | 10000.00 | 0.00 | 대기 /  / 새 신호 대기 |
| v1 | momentum_26 + volume_26 | 9975.10 | -24.90 | buy /  / momentum_26 + volume_26: prior completed bar target 50%; next bar open simulation |
| v1 | breakout_8 AND reversion_12 | 10000.00 | 0.00 | 대기 /  / 새 신호 대기 |
| v1 | breakout_8 + reversion_12 | 10000.00 | 0.00 | 대기 /  / 새 신호 대기 |
| v1 | breakout_8 AND volume_26 | 10000.00 | 0.00 | 대기 /  / 새 신호 대기 |
| v1 | breakout_8 + volume_26 | 10000.00 | 0.00 | 대기 /  / 새 신호 대기 |
| v1 | reversion_12 AND volume_26 | 10000.00 | 0.00 | 대기 /  / 새 신호 대기 |
| v1 | reversion_12 + volume_26 | 10000.00 | 0.00 | 대기 /  / 새 신호 대기 |
| v2 | cash | 10000.00 | 0.00 | 대기 /  / 새 신호 대기 |
| v2 | buy_hold | 10641.77 | 641.77 | buy / partial / 직전 완료 봉 목표 비중 100%; 다음 봉 시가 가정 |
| v2 | trend_8_26 | 10496.96 | 496.96 | buy / partial / 직전 완료 봉 목표 비중 100%; 다음 봉 시가 가정 |
| v2 | momentum_26 | 10466.86 | 466.86 | buy / partial / 직전 완료 봉 목표 비중 100%; 다음 봉 시가 가정 |
| v2 | breakout_8 | 9964.65 | -35.35 | sell / filled / 직전 완료 봉 목표 비중 0%; 다음 봉 시가 가정 |
| v2 | reversion_12 | 10022.26 | 22.26 | sell / filled / 직전 완료 봉 목표 비중 0%; 다음 봉 시가 가정 |
| v2 | volume_26 | 9965.28 | -34.72 | sell / filled / 직전 완료 봉 목표 비중 0%; 다음 봉 시가 가정 |
| v2 | trend_8_26 AND momentum_26 | 10496.96 | 496.96 | buy / partial / 직전 완료 봉 목표 비중 100%; 다음 봉 시가 가정 |
| v2 | trend_8_26 + momentum_26 | 10481.89 | 481.89 | buy / partial / 직전 완료 봉 목표 비중 100%; 다음 봉 시가 가정 |
| v2 | trend_8_26 AND breakout_8 | 10088.55 | 88.55 | sell / filled / 직전 완료 봉 목표 비중 0%; 다음 봉 시가 가정 |
| v2 | trend_8_26 + breakout_8 | 10227.80 | 227.80 | buy / filled / 직전 완료 봉 목표 비중 50%; 다음 봉 시가 가정 |
| v2 | trend_8_26 AND reversion_12 | 9931.03 | -68.97 | sell / filled / 직전 완료 봉 목표 비중 0%; 다음 봉 시가 가정 |
| v2 | trend_8_26 + reversion_12 | 10258.37 | 258.37 | buy / filled / 직전 완료 봉 목표 비중 50%; 다음 봉 시가 가정 |
| v2 | trend_8_26 AND volume_26 | 9949.23 | -50.77 | sell / filled / 직전 완료 봉 목표 비중 0%; 다음 봉 시가 가정 |
| v2 | trend_8_26 + volume_26 | 10229.17 | 229.17 | buy / filled / 직전 완료 봉 목표 비중 50%; 다음 봉 시가 가정 |
| v2 | momentum_26 AND breakout_8 | 9964.65 | -35.35 | sell / filled / 직전 완료 봉 목표 비중 0%; 다음 봉 시가 가정 |
| v2 | momentum_26 + breakout_8 | 10213.15 | 213.15 | buy / filled / 직전 완료 봉 목표 비중 50%; 다음 봉 시가 가정 |
| v2 | momentum_26 AND reversion_12 | 9940.68 | -59.32 | sell / filled / 직전 완료 봉 목표 비중 0%; 다음 봉 시가 가정 |
| v2 | momentum_26 + reversion_12 | 10286.78 | 286.78 | buy / filled / 직전 완료 봉 목표 비중 50%; 다음 봉 시가 가정 |
| v2 | momentum_26 AND volume_26 | 9913.82 | -86.18 | sell / filled / 직전 완료 봉 목표 비중 0%; 다음 봉 시가 가정 |
| v2 | momentum_26 + volume_26 | 10214.59 | 214.59 | buy / filled / 직전 완료 봉 목표 비중 50%; 다음 봉 시가 가정 |
| v2 | breakout_8 AND reversion_12 | 10000.00 | 0.00 | 대기 /  / 새 신호 대기 |
| v2 | breakout_8 + reversion_12 | 10015.72 | 15.72 | sell / filled / 직전 완료 봉 목표 비중 0%; 다음 봉 시가 가정 |
| v2 | breakout_8 AND volume_26 | 9950.23 | -49.77 | sell / filled / 직전 완료 봉 목표 비중 0%; 다음 봉 시가 가정 |
| v2 | breakout_8 + volume_26 | 9966.35 | -33.65 | sell / filled / 직전 완료 봉 목표 비중 0%; 다음 봉 시가 가정 |
| v2 | reversion_12 AND volume_26 | 10009.78 | 9.78 | sell / filled / 직전 완료 봉 목표 비중 0%; 다음 봉 시가 가정 |
| v2 | reversion_12 + volume_26 | 9993.76 | -6.24 | sell / filled / 직전 완료 봉 목표 비중 0%; 다음 봉 시가 가정 |

### 같은 기간의 비용·노출 비교 (사후 연구)

| 전략 | 비용 전 | 비용 후 | 100% 보유 | 같은 평균 노출 보유 | 평균 노출 |
|---|---:|---:|---:|---:|---:|
| cash | 0.00% | 0.00% | 9.43% | 0.00% | 0.00% |
| buy_hold | 9.89% | 9.43% | 9.43% | 9.43% | 100.00% |
| trend_8_26 | 10.02% | 7.28% | 9.43% | 6.25% | 66.32% |
| momentum_26 | 7.22% | 3.24% | 9.43% | 6.20% | 65.79% |
| breakout_8 | 5.52% | -11.92% | 9.43% | 2.53% | 26.84% |
| reversion_12 | 2.08% | -6.53% | 9.43% | 1.63% | 17.37% |
| volume_26 | -0.17% | -5.87% | 9.43% | 0.57% | 6.05% |
| trend_8_26 AND momentum_26 | 9.54% | 5.48% | 9.43% | 5.70% | 60.53% |
| trend_8_26 + momentum_26 | 8.62% | 5.25% | 9.43% | 6.22% | 66.05% |
| trend_8_26 AND breakout_8 | 6.92% | -6.91% | 9.43% | 2.10% | 22.37% |
| trend_8_26 + breakout_8 | 7.76% | -2.57% | 9.43% | 4.39% | 46.59% |
| trend_8_26 AND reversion_12 | 0.40% | -3.73% | 9.43% | 0.52% | 5.53% |
| trend_8_26 + reversion_12 | 6.02% | 0.36% | 9.43% | 3.94% | 41.85% |
| trend_8_26 AND volume_26 | 1.13% | -1.39% | 9.43% | 0.20% | 2.11% |
| trend_8_26 + volume_26 | 4.84% | 0.93% | 9.43% | 3.41% | 36.19% |
| momentum_26 AND breakout_8 | 5.58% | -8.47% | 9.43% | 2.20% | 23.42% |
| momentum_26 + breakout_8 | 6.38% | -4.42% | 9.43% | 4.36% | 46.32% |
| momentum_26 AND reversion_12 | 0.36% | -3.77% | 9.43% | 0.49% | 5.26% |
| momentum_26 + reversion_12 | 4.66% | 0.12% | 9.43% | 3.91% | 41.58% |
| momentum_26 AND volume_26 | 0.44% | -3.69% | 9.43% | 0.27% | 2.89% |
| momentum_26 + volume_26 | 3.50% | -1.40% | 9.43% | 3.38% | 35.92% |
| breakout_8 AND reversion_12 | 0.00% | 0.00% | 9.43% | 0.00% | 0.00% |
| breakout_8 + reversion_12 | 3.82% | -8.88% | 9.43% | 2.08% | 22.11% |
| breakout_8 AND volume_26 | 0.91% | -1.19% | 9.43% | 0.15% | 1.58% |
| breakout_8 + volume_26 | 2.67% | -8.16% | 9.43% | 1.55% | 16.45% |
| reversion_12 AND volume_26 | -0.11% | -3.00% | 9.43% | 0.27% | 2.89% |
| reversion_12 + volume_26 | 0.96% | -6.00% | 9.43% | 1.10% | 11.71% |

동일 구간·초기 자금, 종료 시 청산 비용 포함. 노출 맞춤은 사후 설명용이며 v2 실제 계좌 성과가 아닙니다.
[낙폭 분해·비용 영향·전체 구간](WMT/comparison.json)

[v1 전체 기록](WMT/accounts.json) · [v2 전체 기록](WMT/accounts-v2.json)
