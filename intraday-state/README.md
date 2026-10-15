# 모의투자 운영 현황

최근 확인: 2026-10-15T19:22:00.581638+00:00 (UTC)
다음 15분 확인 목표 (세션 실행 중에만 적용): 2026-10-15T19:37:00+00:00 (UTC, 실행 지연 가능)

실제 주문 없음. v1 기존 계좌와 v2 새 계좌의 시작일이 다르므로 수익률을 직접 우열 비교하지 마세요.
v2는 다음 봉 시가에 비용·스프레드·직전 거래량 제한을 적용한 가상 체결입니다. 미체결 잔량은 만료됩니다.

| 종목 | 상태 | 최근 성공 UTC | 마지막 완료 봉 UTC | 이번 새 봉 |
|---|---|---|---|---|
| SPY | updated | 2026-10-15T19:22:00.581638+00:00 | 2026-10-15T19:00:00+00:00 | 1 |
| QQQ | updated | 2026-10-15T19:22:00.581638+00:00 | 2026-10-15T19:00:00+00:00 | 1 |
| IWM | updated | 2026-10-15T19:22:00.581638+00:00 | 2026-10-15T19:00:00+00:00 | 1 |
| DIA | updated | 2026-10-15T19:22:00.581638+00:00 | 2026-10-15T19:00:00+00:00 | 1 |
| MSFT | updated | 2026-10-15T19:22:00.581638+00:00 | 2026-10-15T19:00:00+00:00 | 1 |
| JPM | updated | 2026-10-15T19:22:00.581638+00:00 | 2026-10-15T19:00:00+00:00 | 1 |
| XOM | updated | 2026-10-15T19:22:00.581638+00:00 | 2026-10-15T19:00:00+00:00 | 1 |
| JNJ | updated | 2026-10-15T19:22:00.581638+00:00 | 2026-10-15T19:00:00+00:00 | 1 |
| CAT | updated | 2026-10-15T19:22:00.581638+00:00 | 2026-10-15T19:00:00+00:00 | 1 |
| WMT | updated | 2026-10-15T19:22:00.581638+00:00 | 2026-10-15T19:00:00+00:00 | 1 |

이번 실행 소요: 68.03초
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
| v1 | buy_hold | 10006.14 | 6.14 | buy /  / buy_hold: prior completed bar target 100%; next bar open simulation |
| v1 | trend_8_26 | 10005.06 | 5.06 | buy /  / trend_8_26: prior completed bar target 100%; next bar open simulation |
| v1 | momentum_26 | 9963.21 | -36.79 | buy /  / momentum_26: prior completed bar target 100%; next bar open simulation |
| v1 | breakout_8 | 9958.01 | -41.99 | sell /  / breakout_8: prior completed bar target 0%; next bar open simulation |
| v1 | reversion_12 | 10000.00 | 0.00 | 대기 /  / 새 신호 대기 |
| v1 | volume_26 | 9949.83 | -50.17 | sell /  / volume_26: prior completed bar target 0%; next bar open simulation |
| v1 | trend_8_26 AND momentum_26 | 9963.21 | -36.79 | buy /  / trend_8_26 AND momentum_26: prior completed bar target 100%; next bar open simulation |
| v1 | trend_8_26 + momentum_26 | 9984.11 | -15.89 | buy /  / trend_8_26 + momentum_26: prior completed bar target 100%; next bar open simulation |
| v1 | trend_8_26 AND breakout_8 | 9958.01 | -41.99 | sell /  / trend_8_26 AND breakout_8: prior completed bar target 0%; next bar open simulation |
| v1 | trend_8_26 + breakout_8 | 9981.49 | -18.51 | sell /  / trend_8_26 + breakout_8: prior completed bar target 50%; next bar open simulation |
| v1 | trend_8_26 AND reversion_12 | 10000.00 | 0.00 | 대기 /  / 새 신호 대기 |
| v1 | trend_8_26 + reversion_12 | 10002.49 | 2.49 | sell /  / trend_8_26 + reversion_12: prior completed bar target 50%; next bar open simulation |
| v1 | trend_8_26 AND volume_26 | 9949.83 | -50.17 | sell /  / trend_8_26 AND volume_26: prior completed bar target 0%; next bar open simulation |
| v1 | trend_8_26 + volume_26 | 9977.39 | -22.61 | sell /  / trend_8_26 + volume_26: prior completed bar target 50%; next bar open simulation |
| v1 | momentum_26 AND breakout_8 | 9958.01 | -41.99 | sell /  / momentum_26 AND breakout_8: prior completed bar target 0%; next bar open simulation |
| v1 | momentum_26 + breakout_8 | 9960.58 | -39.42 | sell /  / momentum_26 + breakout_8: prior completed bar target 50%; next bar open simulation |
| v1 | momentum_26 AND reversion_12 | 10000.00 | 0.00 | 대기 /  / 새 신호 대기 |
| v1 | momentum_26 + reversion_12 | 9981.53 | -18.47 | sell /  / momentum_26 + reversion_12: prior completed bar target 50%; next bar open simulation |
| v1 | momentum_26 AND volume_26 | 10000.00 | 0.00 | 대기 /  / 새 신호 대기 |
| v1 | momentum_26 + volume_26 | 9976.40 | -23.60 | sell /  / momentum_26 + volume_26: prior completed bar target 50%; next bar open simulation |
| v1 | breakout_8 AND reversion_12 | 10000.00 | 0.00 | 대기 /  / 새 신호 대기 |
| v1 | breakout_8 + reversion_12 | 9978.96 | -21.04 | sell /  / breakout_8 + reversion_12: prior completed bar target 0%; next bar open simulation |
| v1 | breakout_8 AND volume_26 | 10000.00 | 0.00 | 대기 /  / 새 신호 대기 |
| v1 | breakout_8 + volume_26 | 9953.88 | -46.12 | sell /  / breakout_8 + volume_26: prior completed bar target 0%; next bar open simulation |
| v1 | reversion_12 AND volume_26 | 10000.00 | 0.00 | 대기 /  / 새 신호 대기 |
| v1 | reversion_12 + volume_26 | 9974.87 | -25.13 | sell /  / reversion_12 + volume_26: prior completed bar target 0%; next bar open simulation |
| v2 | cash | 10000.00 | 0.00 | 대기 /  / 새 신호 대기 |
| v2 | buy_hold | 9896.45 | -103.55 | buy / partial / 직전 완료 봉 목표 비중 100%; 다음 봉 시가 가정 |
| v2 | trend_8_26 | 9852.22 | -147.78 | buy / partial / 직전 완료 봉 목표 비중 100%; 다음 봉 시가 가정 |
| v2 | momentum_26 | 9822.65 | -177.35 | buy / partial / 직전 완료 봉 목표 비중 100%; 다음 봉 시가 가정 |
| v2 | breakout_8 | 9642.19 | -357.81 | sell / filled / 직전 완료 봉 목표 비중 0%; 다음 봉 시가 가정 |
| v2 | reversion_12 | 9535.84 | -464.16 | sell / filled / 직전 완료 봉 목표 비중 0%; 다음 봉 시가 가정 |
| v2 | volume_26 | 9441.45 | -558.55 | sell / filled / 직전 완료 봉 목표 비중 0%; 다음 봉 시가 가정 |
| v2 | trend_8_26 AND momentum_26 | 9829.34 | -170.66 | buy / partial / 직전 완료 봉 목표 비중 100%; 다음 봉 시가 가정 |
| v2 | trend_8_26 + momentum_26 | 9837.44 | -162.56 | buy / partial / 직전 완료 봉 목표 비중 100%; 다음 봉 시가 가정 |
| v2 | trend_8_26 AND breakout_8 | 9869.82 | -130.18 | sell / filled / 직전 완료 봉 목표 비중 0%; 다음 봉 시가 가정 |
| v2 | trend_8_26 + breakout_8 | 9746.50 | -253.50 | sell / filled / 직전 완료 봉 목표 비중 50%; 다음 봉 시가 가정 |
| v2 | trend_8_26 AND reversion_12 | 9896.11 | -103.89 | sell / filled / 직전 완료 봉 목표 비중 0%; 다음 봉 시가 가정 |
| v2 | trend_8_26 + reversion_12 | 9692.43 | -307.57 | sell / filled / 직전 완료 봉 목표 비중 50%; 다음 봉 시가 가정 |
| v2 | trend_8_26 AND volume_26 | 9845.91 | -154.09 | sell / filled / 직전 완료 봉 목표 비중 0%; 다음 봉 시가 가정 |
| v2 | trend_8_26 + volume_26 | 9664.70 | -335.30 | sell / filled / 직전 완료 봉 목표 비중 50%; 다음 봉 시가 가정 |
| v2 | momentum_26 AND breakout_8 | 9827.95 | -172.05 | sell / filled / 직전 완료 봉 목표 비중 0%; 다음 봉 시가 가정 |
| v2 | momentum_26 + breakout_8 | 9731.90 | -268.10 | sell / filled / 직전 완료 봉 목표 비중 50%; 다음 봉 시가 가정 |
| v2 | momentum_26 AND reversion_12 | 9963.21 | -36.79 | sell / filled / 직전 완료 봉 목표 비중 0%; 다음 봉 시가 가정 |
| v2 | momentum_26 + reversion_12 | 9698.23 | -301.77 | sell / filled / 직전 완료 봉 목표 비중 50%; 다음 봉 시가 가정 |
| v2 | momentum_26 AND volume_26 | 9917.25 | -82.75 | sell / filled / 직전 완료 봉 목표 비중 0%; 다음 봉 시가 가정 |
| v2 | momentum_26 + volume_26 | 9690.77 | -309.23 | sell / filled / 직전 완료 봉 목표 비중 50%; 다음 봉 시가 가정 |
| v2 | breakout_8 AND reversion_12 | 10000.00 | 0.00 | 대기 /  / 새 신호 대기 |
| v2 | breakout_8 + reversion_12 | 9628.83 | -371.17 | sell / filled / 직전 완료 봉 목표 비중 0%; 다음 봉 시가 가정 |
| v2 | breakout_8 AND volume_26 | 9933.18 | -66.82 | sell / filled / 직전 완료 봉 목표 비중 0%; 다음 봉 시가 가정 |
| v2 | breakout_8 + volume_26 | 9581.12 | -418.88 | sell / filled / 직전 완료 봉 목표 비중 0%; 다음 봉 시가 가정 |
| v2 | reversion_12 AND volume_26 | 9743.33 | -256.67 | sell / filled / 직전 완료 봉 목표 비중 0%; 다음 봉 시가 가정 |
| v2 | reversion_12 + volume_26 | 9568.30 | -431.70 | sell / filled / 직전 완료 봉 목표 비중 0%; 다음 봉 시가 가정 |

### 같은 기간의 비용·노출 비교 (사후 연구)

| 전략 | 비용 전 | 비용 후 | 100% 보유 | 같은 평균 노출 보유 | 평균 노출 |
|---|---:|---:|---:|---:|---:|
| cash | 0.00% | 0.00% | 0.22% | 0.00% | 0.00% |
| buy_hold | 0.64% | 0.22% | 0.22% | 0.22% | 100.00% |
| trend_8_26 | 1.90% | -1.47% | 0.22% | 0.11% | 49.61% |
| momentum_26 | -0.06% | -4.57% | 0.22% | 0.11% | 49.35% |
| breakout_8 | -0.43% | -15.47% | 0.22% | 0.05% | 21.67% |
| reversion_12 | -1.86% | -12.74% | 0.22% | 0.06% | 27.68% |
| volume_26 | -0.60% | -8.99% | 0.22% | 0.02% | 8.09% |
| trend_8_26 AND momentum_26 | 1.27% | -2.48% | 0.22% | 0.10% | 43.08% |
| trend_8_26 + momentum_26 | 0.91% | -2.83% | 0.22% | 0.11% | 49.48% |
| trend_8_26 AND breakout_8 | 0.26% | -10.12% | 0.22% | 0.03% | 12.79% |
| trend_8_26 + breakout_8 | 0.73% | -8.74% | 0.22% | 0.08% | 35.65% |
| trend_8_26 AND reversion_12 | 0.10% | -4.01% | 0.22% | 0.01% | 6.01% |
| trend_8_26 + reversion_12 | 0.01% | -7.09% | 0.22% | 0.09% | 38.65% |
| trend_8_26 AND volume_26 | -0.23% | -3.93% | 0.22% | 0.01% | 3.39% |
| trend_8_26 + volume_26 | 0.64% | -5.31% | 0.22% | 0.06% | 28.86% |
| momentum_26 AND breakout_8 | 0.56% | -9.84% | 0.22% | 0.03% | 13.84% |
| momentum_26 + breakout_8 | -0.24% | -10.19% | 0.22% | 0.08% | 35.52% |
| momentum_26 AND reversion_12 | -0.88% | -5.75% | 0.22% | 0.01% | 6.79% |
| momentum_26 + reversion_12 | -0.96% | -8.18% | 0.22% | 0.09% | 38.52% |
| momentum_26 AND volume_26 | -0.18% | -2.67% | 0.22% | 0.00% | 1.83% |
| momentum_26 + volume_26 | -0.33% | -5.63% | 0.22% | 0.06% | 28.72% |
| breakout_8 AND reversion_12 | 0.00% | 0.00% | 0.22% | 0.00% | 0.00% |
| breakout_8 + reversion_12 | -1.14% | -13.59% | 0.22% | 0.05% | 24.68% |
| breakout_8 AND volume_26 | 0.09% | -1.17% | 0.22% | 0.00% | 1.04% |
| breakout_8 + volume_26 | -0.51% | -11.37% | 0.22% | 0.03% | 14.89% |
| reversion_12 AND volume_26 | -0.67% | -4.76% | 0.22% | 0.01% | 3.92% |
| reversion_12 + volume_26 | -1.23% | -10.52% | 0.22% | 0.04% | 17.89% |

동일 구간·초기 자금, 종료 시 청산 비용 포함. 노출 맞춤은 사후 설명용이며 v2 실제 계좌 성과가 아닙니다.
[낙폭 분해·비용 영향·전체 구간](SPY/comparison.json)

[v1 전체 기록](SPY/accounts.json) · [v2 전체 기록](SPY/accounts-v2.json)

## QQQ 계좌

| 모델 | 전략 | 평가액 USD | 손익 USD | 최근 매매·이유 |
|---|---|---:|---:|---|
| v1 | cash | 10000.00 | 0.00 | 대기 /  / 새 신호 대기 |
| v1 | buy_hold | 10022.86 | 22.86 | buy /  / buy_hold: prior completed bar target 100%; next bar open simulation |
| v1 | trend_8_26 | 10032.97 | 32.97 | buy /  / trend_8_26: prior completed bar target 100%; next bar open simulation |
| v1 | momentum_26 | 10000.00 | 0.00 | 대기 /  / 새 신호 대기 |
| v1 | breakout_8 | 9956.10 | -43.90 | sell /  / breakout_8: prior completed bar target 0%; next bar open simulation |
| v1 | reversion_12 | 10000.00 | 0.00 | 대기 /  / 새 신호 대기 |
| v1 | volume_26 | 9962.28 | -37.72 | sell /  / volume_26: prior completed bar target 0%; next bar open simulation |
| v1 | trend_8_26 AND momentum_26 | 10000.00 | 0.00 | 대기 /  / 새 신호 대기 |
| v1 | trend_8_26 + momentum_26 | 10016.46 | 16.46 | sell /  / trend_8_26 + momentum_26: prior completed bar target 50%; next bar open simulation |
| v1 | trend_8_26 AND breakout_8 | 10000.00 | 0.00 | 대기 /  / 새 신호 대기 |
| v1 | trend_8_26 + breakout_8 | 9994.43 | -5.57 | sell /  / trend_8_26 + breakout_8: prior completed bar target 50%; next bar open simulation |
| v1 | trend_8_26 AND reversion_12 | 10000.00 | 0.00 | 대기 /  / 새 신호 대기 |
| v1 | trend_8_26 + reversion_12 | 10016.46 | 16.46 | sell /  / trend_8_26 + reversion_12: prior completed bar target 50%; next bar open simulation |
| v1 | trend_8_26 AND volume_26 | 10000.00 | 0.00 | 대기 /  / 새 신호 대기 |
| v1 | trend_8_26 + volume_26 | 9997.54 | -2.46 | sell /  / trend_8_26 + volume_26: prior completed bar target 50%; next bar open simulation |
| v1 | momentum_26 AND breakout_8 | 10000.00 | 0.00 | 대기 /  / 새 신호 대기 |
| v1 | momentum_26 + breakout_8 | 9978.01 | -21.99 | sell /  / momentum_26 + breakout_8: prior completed bar target 0%; next bar open simulation |
| v1 | momentum_26 AND reversion_12 | 10000.00 | 0.00 | 대기 /  / 새 신호 대기 |
| v1 | momentum_26 + reversion_12 | 10000.00 | 0.00 | 대기 /  / 새 신호 대기 |
| v1 | momentum_26 AND volume_26 | 10000.00 | 0.00 | 대기 /  / 새 신호 대기 |
| v1 | momentum_26 + volume_26 | 9981.11 | -18.89 | sell /  / momentum_26 + volume_26: prior completed bar target 0%; next bar open simulation |
| v1 | breakout_8 AND reversion_12 | 10000.00 | 0.00 | 대기 /  / 새 신호 대기 |
| v1 | breakout_8 + reversion_12 | 9978.01 | -21.99 | sell /  / breakout_8 + reversion_12: prior completed bar target 0%; next bar open simulation |
| v1 | breakout_8 AND volume_26 | 10000.00 | 0.00 | 대기 /  / 새 신호 대기 |
| v1 | breakout_8 + volume_26 | 9959.16 | -40.84 | sell /  / breakout_8 + volume_26: prior completed bar target 0%; next bar open simulation |
| v1 | reversion_12 AND volume_26 | 10000.00 | 0.00 | 대기 /  / 새 신호 대기 |
| v1 | reversion_12 + volume_26 | 9981.11 | -18.89 | sell /  / reversion_12 + volume_26: prior completed bar target 0%; next bar open simulation |
| v2 | cash | 10000.00 | 0.00 | 대기 /  / 새 신호 대기 |
| v2 | buy_hold | 9686.97 | -313.03 | buy / partial / 직전 완료 봉 목표 비중 100%; 다음 봉 시가 가정 |
| v2 | trend_8_26 | 9813.06 | -186.94 | buy / partial / 직전 완료 봉 목표 비중 100%; 다음 봉 시가 가정 |
| v2 | momentum_26 | 9936.83 | -63.17 | sell / filled / 직전 완료 봉 목표 비중 0%; 다음 봉 시가 가정 |
| v2 | breakout_8 | 9741.06 | -258.94 | sell / filled / 직전 완료 봉 목표 비중 0%; 다음 봉 시가 가정 |
| v2 | reversion_12 | 9515.83 | -484.17 | sell / filled / 직전 완료 봉 목표 비중 0%; 다음 봉 시가 가정 |
| v2 | volume_26 | 9565.80 | -434.20 | 중단: 손실 한도 / sell / filled / 직전 완료 봉 목표 비중 0%; 다음 봉 시가 가정 |
| v2 | trend_8_26 AND momentum_26 | 9936.83 | -63.17 | sell / filled / 직전 완료 봉 목표 비중 0%; 다음 봉 시가 가정 |
| v2 | trend_8_26 + momentum_26 | 9874.76 | -125.24 | sell / filled / 직전 완료 봉 목표 비중 50%; 다음 봉 시가 가정 |
| v2 | trend_8_26 AND breakout_8 | 9968.70 | -31.30 | sell / filled / 직전 완료 봉 목표 비중 0%; 다음 봉 시가 가정 |
| v2 | trend_8_26 + breakout_8 | 9776.92 | -223.08 | sell / filled / 직전 완료 봉 목표 비중 50%; 다음 봉 시가 가정 |
| v2 | trend_8_26 AND reversion_12 | 9861.14 | -138.86 | sell / filled / 직전 완료 봉 목표 비중 0%; 다음 봉 시가 가정 |
| v2 | trend_8_26 + reversion_12 | 9663.01 | -336.99 | sell / filled / 직전 완료 봉 목표 비중 50%; 다음 봉 시가 가정 |
| v2 | trend_8_26 AND volume_26 | 9840.10 | -159.90 | sell / filled / 직전 완료 봉 목표 비중 0%; 다음 봉 시가 가정 |
| v2 | trend_8_26 + volume_26 | 9607.71 | -392.29 | sell / filled / 직전 완료 봉 목표 비중 50%; 다음 봉 시가 가정 |
| v2 | momentum_26 AND breakout_8 | 10000.00 | 0.00 | 대기 /  / 새 신호 대기 |
| v2 | momentum_26 + breakout_8 | 9838.38 | -161.62 | sell / filled / 직전 완료 봉 목표 비중 0%; 다음 봉 시가 가정 |
| v2 | momentum_26 AND reversion_12 | 10000.00 | 0.00 | 대기 /  / 새 신호 대기 |
| v2 | momentum_26 + reversion_12 | 9744.19 | -255.81 | sell / filled / 직전 완료 봉 목표 비중 0%; 다음 봉 시가 가정 |
| v2 | momentum_26 AND volume_26 | 9936.83 | -63.17 | sell / filled / 직전 완료 봉 목표 비중 0%; 다음 봉 시가 가정 |
| v2 | momentum_26 + volume_26 | 9668.12 | -331.88 | sell / filled / 직전 완료 봉 목표 비중 0%; 다음 봉 시가 가정 |
| v2 | breakout_8 AND reversion_12 | 10000.00 | 0.00 | 대기 /  / 새 신호 대기 |
| v2 | breakout_8 + reversion_12 | 9688.33 | -311.67 | sell / filled / 직전 완료 봉 목표 비중 0%; 다음 봉 시가 가정 |
| v2 | breakout_8 AND volume_26 | 9947.98 | -52.02 | sell / filled / 직전 완료 봉 목표 비중 0%; 다음 봉 시가 가정 |
| v2 | breakout_8 + volume_26 | 9612.73 | -387.27 | sell / filled / 직전 완료 봉 목표 비중 0%; 다음 봉 시가 가정 |
| v2 | reversion_12 AND volume_26 | 9547.64 | -452.36 | 중단: 손실 한도 / sell / filled / 직전 완료 봉 목표 비중 0%; 다음 봉 시가 가정 |
| v2 | reversion_12 + volume_26 | 9481.14 | -518.86 | sell / filled / 직전 완료 봉 목표 비중 0%; 다음 봉 시가 가정 |

### 같은 기간의 비용·노출 비교 (사후 연구)

| 전략 | 비용 전 | 비용 후 | 100% 보유 | 같은 평균 노출 보유 | 평균 노출 |
|---|---:|---:|---:|---:|---:|
| cash | 0.00% | 0.00% | -2.18% | -0.00% | 0.00% |
| buy_hold | -1.77% | -2.18% | -2.18% | -2.18% | 100.00% |
| trend_8_26 | 0.82% | -2.92% | -2.18% | -1.03% | 47.52% |
| momentum_26 | -0.92% | -5.00% | -2.18% | -0.91% | 41.78% |
| breakout_8 | -1.29% | -16.56% | -2.18% | -0.37% | 17.23% |
| reversion_12 | -0.86% | -12.96% | -2.18% | -0.57% | 26.37% |
| volume_26 | -1.07% | -13.51% | -2.18% | -0.31% | 14.10% |
| trend_8_26 AND momentum_26 | 0.05% | -3.26% | -2.18% | -0.81% | 37.34% |
| trend_8_26 + momentum_26 | -0.05% | -3.76% | -2.18% | -0.97% | 44.65% |
| trend_8_26 AND breakout_8 | -0.14% | -9.34% | -2.18% | -0.22% | 10.18% |
| trend_8_26 + breakout_8 | -0.24% | -9.62% | -2.18% | -0.70% | 32.38% |
| trend_8_26 AND reversion_12 | 0.42% | -5.31% | -2.18% | -0.13% | 6.01% |
| trend_8_26 + reversion_12 | -0.01% | -7.50% | -2.18% | -0.80% | 36.95% |
| trend_8_26 AND volume_26 | -0.71% | -5.59% | -2.18% | -0.09% | 4.18% |
| trend_8_26 + volume_26 | -0.13% | -8.18% | -2.18% | -0.67% | 30.81% |
| momentum_26 AND breakout_8 | -0.30% | -9.10% | -2.18% | -0.23% | 10.44% |
| momentum_26 + breakout_8 | -1.10% | -10.78% | -2.18% | -0.64% | 29.51% |
| momentum_26 AND reversion_12 | -0.02% | -5.73% | -2.18% | -0.10% | 4.70% |
| momentum_26 + reversion_12 | -0.88% | -8.50% | -2.18% | -0.74% | 34.08% |
| momentum_26 AND volume_26 | -0.30% | -4.40% | -2.18% | -0.07% | 3.39% |
| momentum_26 + volume_26 | -0.99% | -9.17% | -2.18% | -0.61% | 27.94% |
| breakout_8 AND reversion_12 | 0.00% | 0.00% | -2.18% | -0.00% | 0.00% |
| breakout_8 + reversion_12 | -1.07% | -13.89% | -2.18% | -0.47% | 21.81% |
| breakout_8 AND volume_26 | 0.04% | -2.04% | -2.18% | -0.03% | 1.31% |
| breakout_8 + volume_26 | -1.18% | -13.80% | -2.18% | -0.34% | 15.67% |
| reversion_12 AND volume_26 | -1.25% | -8.44% | -2.18% | -0.19% | 8.62% |
| reversion_12 + volume_26 | -0.96% | -12.88% | -2.18% | -0.44% | 20.24% |

동일 구간·초기 자금, 종료 시 청산 비용 포함. 노출 맞춤은 사후 설명용이며 v2 실제 계좌 성과가 아닙니다.
[낙폭 분해·비용 영향·전체 구간](QQQ/comparison.json)

[v1 전체 기록](QQQ/accounts.json) · [v2 전체 기록](QQQ/accounts-v2.json)

## IWM 계좌

| 모델 | 전략 | 평가액 USD | 손익 USD | 최근 매매·이유 |
|---|---|---:|---:|---|
| v1 | cash | 10000.00 | 0.00 | 대기 /  / 새 신호 대기 |
| v1 | buy_hold | 9998.25 | -1.75 | buy /  / buy_hold: prior completed bar target 100%; next bar open simulation |
| v1 | trend_8_26 | 9998.25 | -1.75 | buy /  / trend_8_26: prior completed bar target 100%; next bar open simulation |
| v1 | momentum_26 | 9998.25 | -1.75 | buy /  / momentum_26: prior completed bar target 100%; next bar open simulation |
| v1 | breakout_8 | 9952.80 | -47.20 | sell /  / breakout_8: prior completed bar target 0%; next bar open simulation |
| v1 | reversion_12 | 10000.00 | 0.00 | 대기 /  / 새 신호 대기 |
| v1 | volume_26 | 10000.00 | 0.00 | 대기 /  / 새 신호 대기 |
| v1 | trend_8_26 AND momentum_26 | 9998.25 | -1.75 | buy /  / trend_8_26 AND momentum_26: prior completed bar target 100%; next bar open simulation |
| v1 | trend_8_26 + momentum_26 | 9998.25 | -1.75 | buy /  / trend_8_26 + momentum_26: prior completed bar target 100%; next bar open simulation |
| v1 | trend_8_26 AND breakout_8 | 9952.80 | -47.20 | sell /  / trend_8_26 AND breakout_8: prior completed bar target 0%; next bar open simulation |
| v1 | trend_8_26 + breakout_8 | 9975.47 | -24.53 | sell /  / trend_8_26 + breakout_8: prior completed bar target 50%; next bar open simulation |
| v1 | trend_8_26 AND reversion_12 | 10000.00 | 0.00 | 대기 /  / 새 신호 대기 |
| v1 | trend_8_26 + reversion_12 | 9999.08 | -0.92 | sell /  / trend_8_26 + reversion_12: prior completed bar target 50%; next bar open simulation |
| v1 | trend_8_26 AND volume_26 | 10000.00 | 0.00 | 대기 /  / 새 신호 대기 |
| v1 | trend_8_26 + volume_26 | 9999.08 | -0.92 | sell /  / trend_8_26 + volume_26: prior completed bar target 50%; next bar open simulation |
| v1 | momentum_26 AND breakout_8 | 9952.80 | -47.20 | sell /  / momentum_26 AND breakout_8: prior completed bar target 0%; next bar open simulation |
| v1 | momentum_26 + breakout_8 | 9975.47 | -24.53 | sell /  / momentum_26 + breakout_8: prior completed bar target 50%; next bar open simulation |
| v1 | momentum_26 AND reversion_12 | 10000.00 | 0.00 | 대기 /  / 새 신호 대기 |
| v1 | momentum_26 + reversion_12 | 9999.08 | -0.92 | sell /  / momentum_26 + reversion_12: prior completed bar target 50%; next bar open simulation |
| v1 | momentum_26 AND volume_26 | 10000.00 | 0.00 | 대기 /  / 새 신호 대기 |
| v1 | momentum_26 + volume_26 | 9999.08 | -0.92 | sell /  / momentum_26 + volume_26: prior completed bar target 50%; next bar open simulation |
| v1 | breakout_8 AND reversion_12 | 10000.00 | 0.00 | 대기 /  / 새 신호 대기 |
| v1 | breakout_8 + reversion_12 | 9976.36 | -23.64 | sell /  / breakout_8 + reversion_12: prior completed bar target 0%; next bar open simulation |
| v1 | breakout_8 AND volume_26 | 10000.00 | 0.00 | 대기 /  / 새 신호 대기 |
| v1 | breakout_8 + volume_26 | 9976.36 | -23.64 | sell /  / breakout_8 + volume_26: prior completed bar target 0%; next bar open simulation |
| v1 | reversion_12 AND volume_26 | 10000.00 | 0.00 | 대기 /  / 새 신호 대기 |
| v1 | reversion_12 + volume_26 | 10000.00 | 0.00 | 대기 /  / 새 신호 대기 |
| v2 | cash | 10000.00 | 0.00 | 대기 /  / 새 신호 대기 |
| v2 | buy_hold | 9832.83 | -167.17 | buy / partial / 직전 완료 봉 목표 비중 100%; 다음 봉 시가 가정 |
| v2 | trend_8_26 | 9810.31 | -189.69 | buy / partial / 직전 완료 봉 목표 비중 100%; 다음 봉 시가 가정 |
| v2 | momentum_26 | 9811.32 | -188.68 | buy / partial / 직전 완료 봉 목표 비중 100%; 다음 봉 시가 가정 |
| v2 | breakout_8 | 9618.76 | -381.24 | sell / filled / 직전 완료 봉 목표 비중 0%; 다음 봉 시가 가정 |
| v2 | reversion_12 | 9538.67 | -461.33 | sell / filled / 직전 완료 봉 목표 비중 0%; 다음 봉 시가 가정 |
| v2 | volume_26 | 9513.36 | -486.64 | sell / filled / 직전 완료 봉 목표 비중 0%; 다음 봉 시가 가정 |
| v2 | trend_8_26 AND momentum_26 | 9962.58 | -37.42 | buy / partial / 직전 완료 봉 목표 비중 100%; 다음 봉 시가 가정 |
| v2 | trend_8_26 + momentum_26 | 9831.57 | -168.43 | buy / partial / 직전 완료 봉 목표 비중 100%; 다음 봉 시가 가정 |
| v2 | trend_8_26 AND breakout_8 | 9913.81 | -86.19 | sell / filled / 직전 완료 봉 목표 비중 0%; 다음 봉 시가 가정 |
| v2 | trend_8_26 + breakout_8 | 9734.59 | -265.41 | sell / filled / 직전 완료 봉 목표 비중 50%; 다음 봉 시가 가정 |
| v2 | trend_8_26 AND reversion_12 | 9881.82 | -118.18 | sell / filled / 직전 완료 봉 목표 비중 0%; 다음 봉 시가 가정 |
| v2 | trend_8_26 + reversion_12 | 9673.39 | -326.61 | sell / filled / 직전 완료 봉 목표 비중 50%; 다음 봉 시가 가정 |
| v2 | trend_8_26 AND volume_26 | 9862.83 | -137.17 | sell / filled / 직전 완료 봉 목표 비중 0%; 다음 봉 시가 가정 |
| v2 | trend_8_26 + volume_26 | 9681.00 | -319.00 | sell / filled / 직전 완료 봉 목표 비중 50%; 다음 봉 시가 가정 |
| v2 | momentum_26 AND breakout_8 | 9805.96 | -194.04 | sell / filled / 직전 완료 봉 목표 비중 0%; 다음 봉 시가 가정 |
| v2 | momentum_26 + breakout_8 | 9714.55 | -285.45 | sell / filled / 직전 완료 봉 목표 비중 50%; 다음 봉 시가 가정 |
| v2 | momentum_26 AND reversion_12 | 9960.59 | -39.41 | sell / filled / 직전 완료 봉 목표 비중 0%; 다음 봉 시가 가정 |
| v2 | momentum_26 + reversion_12 | 9694.00 | -306.00 | sell / filled / 직전 완료 봉 목표 비중 50%; 다음 봉 시가 가정 |
| v2 | momentum_26 AND volume_26 | 9897.79 | -102.21 | sell / filled / 직전 완료 봉 목표 비중 0%; 다음 봉 시가 가정 |
| v2 | momentum_26 + volume_26 | 9660.99 | -339.01 | sell / filled / 직전 완료 봉 목표 비중 50%; 다음 봉 시가 가정 |
| v2 | breakout_8 AND reversion_12 | 10000.00 | 0.00 | 대기 /  / 새 신호 대기 |
| v2 | breakout_8 + reversion_12 | 9618.59 | -381.41 | sell / filled / 직전 완료 봉 목표 비중 0%; 다음 봉 시가 가정 |
| v2 | breakout_8 AND volume_26 | 9746.03 | -253.97 | sell / filled / 직전 완료 봉 목표 비중 0%; 다음 봉 시가 가정 |
| v2 | breakout_8 + volume_26 | 9586.00 | -414.00 | sell / filled / 직전 완료 봉 목표 비중 0%; 다음 봉 시가 가정 |
| v2 | reversion_12 AND volume_26 | 9740.75 | -259.25 | sell / filled / 직전 완료 봉 목표 비중 0%; 다음 봉 시가 가정 |
| v2 | reversion_12 + volume_26 | 9545.82 | -454.18 | sell / filled / 직전 완료 봉 목표 비중 0%; 다음 봉 시가 가정 |

### 같은 기간의 비용·노출 비교 (사후 연구)

| 전략 | 비용 전 | 비용 후 | 100% 보유 | 같은 평균 노출 보유 | 평균 노출 |
|---|---:|---:|---:|---:|---:|
| cash | 0.00% | 0.00% | -2.72% | -0.00% | 0.00% |
| buy_hold | -2.31% | -2.72% | -2.72% | -2.72% | 100.00% |
| trend_8_26 | -1.74% | -5.78% | -2.72% | -1.24% | 45.17% |
| momentum_26 | -2.32% | -7.90% | -2.72% | -1.11% | 40.73% |
| breakout_8 | -0.88% | -13.71% | -2.72% | -0.51% | 18.54% |
| reversion_12 | -2.12% | -14.79% | -2.72% | -0.81% | 29.50% |
| volume_26 | -2.31% | -9.05% | -2.72% | -0.23% | 8.36% |
| trend_8_26 AND momentum_26 | -1.98% | -6.41% | -2.72% | -0.97% | 35.25% |
| trend_8_26 + momentum_26 | -2.03% | -6.45% | -2.72% | -1.18% | 42.95% |
| trend_8_26 AND breakout_8 | -0.75% | -7.98% | -2.72% | -0.28% | 10.18% |
| trend_8_26 + breakout_8 | -1.30% | -9.64% | -2.72% | -0.87% | 31.86% |
| trend_8_26 AND reversion_12 | -0.09% | -5.00% | -2.72% | -0.16% | 5.74% |
| trend_8_26 + reversion_12 | -1.92% | -10.21% | -2.72% | -1.02% | 37.34% |
| trend_8_26 AND volume_26 | -1.03% | -4.30% | -2.72% | -0.09% | 3.39% |
| trend_8_26 + volume_26 | -2.02% | -7.24% | -2.72% | -0.73% | 26.77% |
| momentum_26 AND breakout_8 | -0.14% | -7.42% | -2.72% | -0.27% | 9.92% |
| momentum_26 + breakout_8 | -1.60% | -10.85% | -2.72% | -0.81% | 29.64% |
| momentum_26 AND reversion_12 | -0.02% | -3.73% | -2.72% | -0.09% | 3.13% |
| momentum_26 + reversion_12 | -2.22% | -10.30% | -2.72% | -0.96% | 35.12% |
| momentum_26 AND volume_26 | -1.32% | -3.77% | -2.72% | -0.05% | 1.83% |
| momentum_26 + volume_26 | -2.31% | -8.10% | -2.72% | -0.67% | 24.55% |
| breakout_8 AND reversion_12 | 0.00% | 0.00% | -2.72% | -0.00% | 0.00% |
| breakout_8 + reversion_12 | -1.50% | -13.54% | -2.72% | -0.66% | 24.03% |
| breakout_8 AND volume_26 | -1.30% | -3.76% | -2.72% | -0.06% | 2.09% |
| breakout_8 + volume_26 | -1.60% | -11.23% | -2.72% | -0.37% | 13.45% |
| reversion_12 AND volume_26 | -0.38% | -4.47% | -2.72% | -0.12% | 4.44% |
| reversion_12 + volume_26 | -2.21% | -11.41% | -2.72% | -0.52% | 18.94% |

동일 구간·초기 자금, 종료 시 청산 비용 포함. 노출 맞춤은 사후 설명용이며 v2 실제 계좌 성과가 아닙니다.
[낙폭 분해·비용 영향·전체 구간](IWM/comparison.json)

[v1 전체 기록](IWM/accounts.json) · [v2 전체 기록](IWM/accounts-v2.json)

## DIA 계좌

| 모델 | 전략 | 평가액 USD | 손익 USD | 최근 매매·이유 |
|---|---|---:|---:|---|
| v1 | cash | 10000.00 | 0.00 | 대기 /  / 새 신호 대기 |
| v1 | buy_hold | 9995.46 | -4.54 | buy /  / buy_hold: prior completed bar target 100%; next bar open simulation |
| v1 | trend_8_26 | 9995.46 | -4.54 | buy /  / trend_8_26: prior completed bar target 100%; next bar open simulation |
| v1 | momentum_26 | 9995.46 | -4.54 | buy /  / momentum_26: prior completed bar target 100%; next bar open simulation |
| v1 | breakout_8 | 9958.65 | -41.35 | sell /  / breakout_8: prior completed bar target 0%; next bar open simulation |
| v1 | reversion_12 | 10000.00 | 0.00 | 대기 /  / 새 신호 대기 |
| v1 | volume_26 | 10000.00 | 0.00 | 대기 /  / 새 신호 대기 |
| v1 | trend_8_26 AND momentum_26 | 9995.46 | -4.54 | buy /  / trend_8_26 AND momentum_26: prior completed bar target 100%; next bar open simulation |
| v1 | trend_8_26 + momentum_26 | 9995.46 | -4.54 | buy /  / trend_8_26 + momentum_26: prior completed bar target 100%; next bar open simulation |
| v1 | trend_8_26 AND breakout_8 | 9958.65 | -41.35 | sell /  / trend_8_26 AND breakout_8: prior completed bar target 0%; next bar open simulation |
| v1 | trend_8_26 + breakout_8 | 9977.00 | -23.00 | sell /  / trend_8_26 + breakout_8: prior completed bar target 50%; next bar open simulation |
| v1 | trend_8_26 AND reversion_12 | 10000.00 | 0.00 | 대기 /  / 새 신호 대기 |
| v1 | trend_8_26 + reversion_12 | 9997.68 | -2.32 | sell /  / trend_8_26 + reversion_12: prior completed bar target 50%; next bar open simulation |
| v1 | trend_8_26 AND volume_26 | 10000.00 | 0.00 | 대기 /  / 새 신호 대기 |
| v1 | trend_8_26 + volume_26 | 9997.68 | -2.32 | sell /  / trend_8_26 + volume_26: prior completed bar target 50%; next bar open simulation |
| v1 | momentum_26 AND breakout_8 | 9958.65 | -41.35 | sell /  / momentum_26 AND breakout_8: prior completed bar target 0%; next bar open simulation |
| v1 | momentum_26 + breakout_8 | 9977.00 | -23.00 | sell /  / momentum_26 + breakout_8: prior completed bar target 50%; next bar open simulation |
| v1 | momentum_26 AND reversion_12 | 10000.00 | 0.00 | 대기 /  / 새 신호 대기 |
| v1 | momentum_26 + reversion_12 | 9997.68 | -2.32 | sell /  / momentum_26 + reversion_12: prior completed bar target 50%; next bar open simulation |
| v1 | momentum_26 AND volume_26 | 10000.00 | 0.00 | 대기 /  / 새 신호 대기 |
| v1 | momentum_26 + volume_26 | 9997.68 | -2.32 | sell /  / momentum_26 + volume_26: prior completed bar target 50%; next bar open simulation |
| v1 | breakout_8 AND reversion_12 | 10000.00 | 0.00 | 대기 /  / 새 신호 대기 |
| v1 | breakout_8 + reversion_12 | 9979.28 | -20.72 | sell /  / breakout_8 + reversion_12: prior completed bar target 0%; next bar open simulation |
| v1 | breakout_8 AND volume_26 | 10000.00 | 0.00 | 대기 /  / 새 신호 대기 |
| v1 | breakout_8 + volume_26 | 9979.28 | -20.72 | sell /  / breakout_8 + volume_26: prior completed bar target 0%; next bar open simulation |
| v1 | reversion_12 AND volume_26 | 10000.00 | 0.00 | 대기 /  / 새 신호 대기 |
| v1 | reversion_12 + volume_26 | 10000.00 | 0.00 | 대기 /  / 새 신호 대기 |
| v2 | cash | 10000.00 | 0.00 | 대기 /  / 새 신호 대기 |
| v2 | buy_hold | 10078.84 | 78.84 | buy / partial / 직전 완료 봉 목표 비중 100%; 다음 봉 시가 가정 |
| v2 | trend_8_26 | 9891.01 | -108.99 | buy / partial / 직전 완료 봉 목표 비중 100%; 다음 봉 시가 가정 |
| v2 | momentum_26 | 9999.76 | -0.24 | buy / partial / 직전 완료 봉 목표 비중 100%; 다음 봉 시가 가정 |
| v2 | breakout_8 | 9584.78 | -415.22 | sell / filled / 직전 완료 봉 목표 비중 0%; 다음 봉 시가 가정 |
| v2 | reversion_12 | 9698.03 | -301.97 | sell / filled / 직전 완료 봉 목표 비중 0%; 다음 봉 시가 가정 |
| v2 | volume_26 | 9718.21 | -281.79 | sell / filled / 직전 완료 봉 목표 비중 0%; 다음 봉 시가 가정 |
| v2 | trend_8_26 AND momentum_26 | 9995.12 | -4.88 | buy / partial / 직전 완료 봉 목표 비중 100%; 다음 봉 시가 가정 |
| v2 | trend_8_26 + momentum_26 | 9945.30 | -54.70 | buy / partial / 직전 완료 봉 목표 비중 100%; 다음 봉 시가 가정 |
| v2 | trend_8_26 AND breakout_8 | 9746.97 | -253.03 | sell / filled / 직전 완료 봉 목표 비중 0%; 다음 봉 시가 가정 |
| v2 | trend_8_26 + breakout_8 | 9736.71 | -263.29 | sell / filled / 직전 완료 봉 목표 비중 50%; 다음 봉 시가 가정 |
| v2 | trend_8_26 AND reversion_12 | 9810.77 | -189.23 | sell / filled / 직전 완료 봉 목표 비중 0%; 다음 봉 시가 가정 |
| v2 | trend_8_26 + reversion_12 | 9793.80 | -206.20 | sell / filled / 직전 완료 봉 목표 비중 50%; 다음 봉 시가 가정 |
| v2 | trend_8_26 AND volume_26 | 9858.88 | -141.12 | sell / filled / 직전 완료 봉 목표 비중 0%; 다음 봉 시가 가정 |
| v2 | trend_8_26 + volume_26 | 9824.80 | -175.20 | sell / filled / 직전 완료 봉 목표 비중 50%; 다음 봉 시가 가정 |
| v2 | momentum_26 AND breakout_8 | 9735.87 | -264.13 | sell / filled / 직전 완료 봉 목표 비중 0%; 다음 봉 시가 가정 |
| v2 | momentum_26 + breakout_8 | 9790.15 | -209.85 | sell / filled / 직전 완료 봉 목표 비중 50%; 다음 봉 시가 가정 |
| v2 | momentum_26 AND reversion_12 | 9955.97 | -44.03 | sell / filled / 직전 완료 봉 목표 비중 0%; 다음 봉 시가 가정 |
| v2 | momentum_26 + reversion_12 | 9847.57 | -152.43 | sell / filled / 직전 완료 봉 목표 비중 50%; 다음 봉 시가 가정 |
| v2 | momentum_26 AND volume_26 | 9791.42 | -208.58 | sell / filled / 직전 완료 봉 목표 비중 0%; 다음 봉 시가 가정 |
| v2 | momentum_26 + volume_26 | 9899.56 | -100.44 | sell / filled / 직전 완료 봉 목표 비중 50%; 다음 봉 시가 가정 |
| v2 | breakout_8 AND reversion_12 | 10000.00 | 0.00 | 대기 /  / 새 신호 대기 |
| v2 | breakout_8 + reversion_12 | 9640.85 | -359.15 | sell / filled / 직전 완료 봉 목표 비중 0%; 다음 봉 시가 가정 |
| v2 | breakout_8 AND volume_26 | 9796.56 | -203.44 | sell / filled / 직전 완료 봉 목표 비중 0%; 다음 봉 시가 가정 |
| v2 | breakout_8 + volume_26 | 9651.15 | -348.85 | sell / filled / 직전 완료 봉 목표 비중 0%; 다음 봉 시가 가정 |
| v2 | reversion_12 AND volume_26 | 10000.00 | 0.00 | 대기 /  / 새 신호 대기 |
| v2 | reversion_12 + volume_26 | 9707.85 | -292.15 | sell / filled / 직전 완료 봉 목표 비중 0%; 다음 봉 시가 가정 |

### 같은 기간의 비용·노출 비교 (사후 연구)

| 전략 | 비용 전 | 비용 후 | 100% 보유 | 같은 평균 노출 보유 | 평균 노출 |
|---|---:|---:|---:|---:|---:|
| cash | 0.00% | 0.00% | 1.02% | 0.00% | 0.00% |
| buy_hold | 1.44% | 1.02% | 1.02% | 1.02% | 100.00% |
| trend_8_26 | 1.76% | -2.83% | 1.02% | 0.58% | 56.40% |
| momentum_26 | 0.42% | -3.71% | 1.02% | 0.54% | 52.74% |
| breakout_8 | 0.08% | -16.45% | 1.02% | 0.24% | 23.24% |
| reversion_12 | -1.36% | -9.30% | 1.02% | 0.25% | 24.54% |
| volume_26 | -0.99% | -11.24% | 1.02% | 0.11% | 10.97% |
| trend_8_26 AND momentum_26 | 1.90% | -2.29% | 1.02% | 0.48% | 47.00% |
| trend_8_26 + momentum_26 | 1.09% | -3.27% | 1.02% | 0.56% | 54.57% |
| trend_8_26 AND breakout_8 | 0.65% | -10.89% | 1.02% | 0.15% | 15.14% |
| trend_8_26 + breakout_8 | 0.92% | -9.71% | 1.02% | 0.41% | 39.82% |
| trend_8_26 AND reversion_12 | 0.37% | -4.56% | 1.02% | 0.06% | 6.27% |
| trend_8_26 + reversion_12 | 0.19% | -5.74% | 1.02% | 0.41% | 40.47% |
| trend_8_26 AND volume_26 | 0.56% | -4.78% | 1.02% | 0.05% | 5.22% |
| trend_8_26 + volume_26 | 0.38% | -6.94% | 1.02% | 0.34% | 33.69% |
| momentum_26 AND breakout_8 | -0.15% | -11.23% | 1.02% | 0.16% | 15.40% |
| momentum_26 + breakout_8 | 0.26% | -10.12% | 1.02% | 0.39% | 38.00% |
| momentum_26 AND reversion_12 | -0.18% | -3.88% | 1.02% | 0.06% | 5.74% |
| momentum_26 + reversion_12 | -0.47% | -5.77% | 1.02% | 0.39% | 38.65% |
| momentum_26 AND volume_26 | -0.40% | -5.70% | 1.02% | 0.05% | 4.70% |
| momentum_26 + volume_26 | -0.28% | -6.77% | 1.02% | 0.33% | 31.86% |
| breakout_8 AND reversion_12 | 0.00% | 0.00% | 1.02% | 0.00% | 0.00% |
| breakout_8 + reversion_12 | -0.64% | -12.60% | 1.02% | 0.24% | 23.90% |
| breakout_8 AND volume_26 | -0.87% | -4.55% | 1.02% | 0.03% | 3.13% |
| breakout_8 + volume_26 | -0.45% | -12.98% | 1.02% | 0.17% | 17.11% |
| reversion_12 AND volume_26 | -0.20% | -5.11% | 1.02% | 0.04% | 3.92% |
| reversion_12 + volume_26 | -1.17% | -10.28% | 1.02% | 0.18% | 17.76% |

동일 구간·초기 자금, 종료 시 청산 비용 포함. 노출 맞춤은 사후 설명용이며 v2 실제 계좌 성과가 아닙니다.
[낙폭 분해·비용 영향·전체 구간](DIA/comparison.json)

[v1 전체 기록](DIA/accounts.json) · [v2 전체 기록](DIA/accounts-v2.json)

## MSFT 계좌

| 모델 | 전략 | 평가액 USD | 손익 USD | 최근 매매·이유 |
|---|---|---:|---:|---|
| v1 | cash | 10000.00 | 0.00 | 대기 /  / 새 신호 대기 |
| v1 | buy_hold | 10039.59 | 39.59 | buy /  / buy_hold: prior completed bar target 100%; next bar open simulation |
| v1 | trend_8_26 | 10039.59 | 39.59 | buy /  / trend_8_26: prior completed bar target 100%; next bar open simulation |
| v1 | momentum_26 | 10041.64 | 41.64 | buy /  / momentum_26: prior completed bar target 100%; next bar open simulation |
| v1 | breakout_8 | 9946.94 | -53.06 | buy /  / breakout_8: prior completed bar target 100%; next bar open simulation |
| v1 | reversion_12 | 10000.00 | 0.00 | 대기 /  / 새 신호 대기 |
| v1 | volume_26 | 9952.64 | -47.36 | sell /  / volume_26: prior completed bar target 0%; next bar open simulation |
| v1 | trend_8_26 AND momentum_26 | 10041.64 | 41.64 | buy /  / trend_8_26 AND momentum_26: prior completed bar target 100%; next bar open simulation |
| v1 | trend_8_26 + momentum_26 | 10040.61 | 40.61 | buy /  / trend_8_26 + momentum_26: prior completed bar target 100%; next bar open simulation |
| v1 | trend_8_26 AND breakout_8 | 9946.94 | -53.06 | buy /  / trend_8_26 AND breakout_8: prior completed bar target 100%; next bar open simulation |
| v1 | trend_8_26 + breakout_8 | 9993.13 | -6.87 | buy /  / trend_8_26 + breakout_8: prior completed bar target 100%; next bar open simulation |
| v1 | trend_8_26 AND reversion_12 | 10000.00 | 0.00 | 대기 /  / 새 신호 대기 |
| v1 | trend_8_26 + reversion_12 | 10019.70 | 19.70 | sell /  / trend_8_26 + reversion_12: prior completed bar target 50%; next bar open simulation |
| v1 | trend_8_26 AND volume_26 | 9952.64 | -47.36 | sell /  / trend_8_26 AND volume_26: prior completed bar target 0%; next bar open simulation |
| v1 | trend_8_26 + volume_26 | 9996.01 | -3.99 | sell /  / trend_8_26 + volume_26: prior completed bar target 50%; next bar open simulation |
| v1 | momentum_26 AND breakout_8 | 9946.94 | -53.06 | buy /  / momentum_26 AND breakout_8: prior completed bar target 100%; next bar open simulation |
| v1 | momentum_26 + breakout_8 | 9994.17 | -5.83 | buy /  / momentum_26 + breakout_8: prior completed bar target 100%; next bar open simulation |
| v1 | momentum_26 AND reversion_12 | 10000.00 | 0.00 | 대기 /  / 새 신호 대기 |
| v1 | momentum_26 + reversion_12 | 10020.74 | 20.74 | sell /  / momentum_26 + reversion_12: prior completed bar target 50%; next bar open simulation |
| v1 | momentum_26 AND volume_26 | 9952.64 | -47.36 | sell /  / momentum_26 AND volume_26: prior completed bar target 0%; next bar open simulation |
| v1 | momentum_26 + volume_26 | 9997.03 | -2.97 | sell /  / momentum_26 + volume_26: prior completed bar target 50%; next bar open simulation |
| v1 | breakout_8 AND reversion_12 | 10000.00 | 0.00 | 대기 /  / 새 신호 대기 |
| v1 | breakout_8 + reversion_12 | 9973.41 | -26.59 | buy /  / breakout_8 + reversion_12: prior completed bar target 50%; next bar open simulation |
| v1 | breakout_8 AND volume_26 | 10000.00 | 0.00 | 대기 /  / 새 신호 대기 |
| v1 | breakout_8 + volume_26 | 9969.66 | -30.34 | buy /  / breakout_8 + volume_26: prior completed bar target 50%; next bar open simulation |
| v1 | reversion_12 AND volume_26 | 10000.00 | 0.00 | 대기 /  / 새 신호 대기 |
| v1 | reversion_12 + volume_26 | 9976.25 | -23.75 | sell /  / reversion_12 + volume_26: prior completed bar target 0%; next bar open simulation |
| v2 | cash | 10000.00 | 0.00 | 대기 /  / 새 신호 대기 |
| v2 | buy_hold | 10024.31 | 24.31 | buy / partial / 직전 완료 봉 목표 비중 100%; 다음 봉 시가 가정 |
| v2 | trend_8_26 | 9906.64 | -93.36 | buy / partial / 직전 완료 봉 목표 비중 100%; 다음 봉 시가 가정 |
| v2 | momentum_26 | 10018.39 | 18.39 | buy / partial / 직전 완료 봉 목표 비중 100%; 다음 봉 시가 가정 |
| v2 | breakout_8 | 9868.47 | -131.53 | buy / partial / 직전 완료 봉 목표 비중 100%; 다음 봉 시가 가정 |
| v2 | reversion_12 | 9618.62 | -381.38 | sell / filled / 직전 완료 봉 목표 비중 0%; 다음 봉 시가 가정 |
| v2 | volume_26 | 9688.55 | -311.45 | sell / filled / 직전 완료 봉 목표 비중 0%; 다음 봉 시가 가정 |
| v2 | trend_8_26 AND momentum_26 | 9867.14 | -132.86 | buy / partial / 직전 완료 봉 목표 비중 100%; 다음 봉 시가 가정 |
| v2 | trend_8_26 + momentum_26 | 9962.62 | -37.38 | buy / partial / 직전 완료 봉 목표 비중 100%; 다음 봉 시가 가정 |
| v2 | trend_8_26 AND breakout_8 | 9707.15 | -292.85 | buy / partial / 직전 완료 봉 목표 비중 100%; 다음 봉 시가 가정 |
| v2 | trend_8_26 + breakout_8 | 9908.48 | -91.52 | buy / partial / 직전 완료 봉 목표 비중 100%; 다음 봉 시가 가정 |
| v2 | trend_8_26 AND reversion_12 | 9900.10 | -99.90 | sell / filled / 직전 완료 봉 목표 비중 0%; 다음 봉 시가 가정 |
| v2 | trend_8_26 + reversion_12 | 9761.21 | -238.79 | sell / filled / 직전 완료 봉 목표 비중 50%; 다음 봉 시가 가정 |
| v2 | trend_8_26 AND volume_26 | 9948.66 | -51.34 | sell / filled / 직전 완료 봉 목표 비중 0%; 다음 봉 시가 가정 |
| v2 | trend_8_26 + volume_26 | 9817.36 | -182.64 | sell / filled / 직전 완료 봉 목표 비중 50%; 다음 봉 시가 가정 |
| v2 | momentum_26 AND breakout_8 | 9863.34 | -136.66 | buy / partial / 직전 완료 봉 목표 비중 100%; 다음 봉 시가 가정 |
| v2 | momentum_26 + breakout_8 | 9943.17 | -56.83 | buy / partial / 직전 완료 봉 목표 비중 100%; 다음 봉 시가 가정 |
| v2 | momentum_26 AND reversion_12 | 9826.88 | -173.12 | sell / filled / 직전 완료 봉 목표 비중 0%; 다음 봉 시가 가정 |
| v2 | momentum_26 + reversion_12 | 9816.24 | -183.76 | sell / filled / 직전 완료 봉 목표 비중 50%; 다음 봉 시가 가정 |
| v2 | momentum_26 AND volume_26 | 9871.26 | -128.74 | sell / filled / 직전 완료 봉 목표 비중 0%; 다음 봉 시가 가정 |
| v2 | momentum_26 + volume_26 | 9872.71 | -127.29 | sell / filled / 직전 완료 봉 목표 비중 50%; 다음 봉 시가 가정 |
| v2 | breakout_8 AND reversion_12 | 10000.00 | 0.00 | 대기 /  / 새 신호 대기 |
| v2 | breakout_8 + reversion_12 | 9763.06 | -236.94 | buy / filled / 직전 완료 봉 목표 비중 50%; 다음 봉 시가 가정 |
| v2 | breakout_8 AND volume_26 | 9938.59 | -61.41 | sell / filled / 직전 완료 봉 목표 비중 0%; 다음 봉 시가 가정 |
| v2 | breakout_8 + volume_26 | 9798.73 | -201.27 | buy / filled / 직전 완료 봉 목표 비중 50%; 다음 봉 시가 가정 |
| v2 | reversion_12 AND volume_26 | 9762.04 | -237.96 | sell / filled / 직전 완료 봉 목표 비중 0%; 다음 봉 시가 가정 |
| v2 | reversion_12 + volume_26 | 9653.37 | -346.63 | sell / filled / 직전 완료 봉 목표 비중 0%; 다음 봉 시가 가정 |

### 같은 기간의 비용·노출 비교 (사후 연구)

| 전략 | 비용 전 | 비용 후 | 100% 보유 | 같은 평균 노출 보유 | 평균 노출 |
|---|---:|---:|---:|---:|---:|
| cash | 0.00% | 0.00% | 4.66% | 0.00% | 0.00% |
| buy_hold | 5.10% | 4.66% | 4.66% | 4.66% | 100.00% |
| trend_8_26 | 0.01% | -3.70% | 4.66% | 2.76% | 59.79% |
| momentum_26 | 1.15% | -4.63% | 4.66% | 2.78% | 60.05% |
| breakout_8 | 5.15% | -9.60% | 4.66% | 0.95% | 20.63% |
| reversion_12 | -4.05% | -12.52% | 4.66% | 1.07% | 23.24% |
| volume_26 | 2.43% | -5.82% | 4.66% | 0.37% | 8.09% |
| trend_8_26 AND momentum_26 | -0.26% | -5.95% | 4.66% | 2.50% | 54.05% |
| trend_8_26 + momentum_26 | 0.59% | -4.15% | 4.66% | 2.77% | 59.92% |
| trend_8_26 AND breakout_8 | 0.74% | -9.69% | 4.66% | 0.62% | 13.58% |
| trend_8_26 + breakout_8 | 2.57% | -6.29% | 4.66% | 1.85% | 40.21% |
| trend_8_26 AND reversion_12 | -3.39% | -8.52% | 4.66% | 0.32% | 7.05% |
| trend_8_26 + reversion_12 | -2.02% | -7.83% | 4.66% | 1.91% | 41.52% |
| trend_8_26 AND volume_26 | 3.46% | 0.46% | 4.66% | 0.12% | 2.61% |
| trend_8_26 + volume_26 | 1.23% | -3.96% | 4.66% | 1.56% | 33.95% |
| momentum_26 AND breakout_8 | 2.68% | -8.33% | 4.66% | 0.63% | 13.84% |
| momentum_26 + breakout_8 | 3.15% | -6.55% | 4.66% | 1.86% | 40.35% |
| momentum_26 AND reversion_12 | -2.74% | -8.67% | 4.66% | 0.37% | 8.09% |
| momentum_26 + reversion_12 | -1.46% | -8.27% | 4.66% | 1.92% | 41.65% |
| momentum_26 AND volume_26 | 1.80% | -2.38% | 4.66% | 0.16% | 3.39% |
| momentum_26 + volume_26 | 1.81% | -4.02% | 4.66% | 1.57% | 34.08% |
| breakout_8 AND reversion_12 | 0.00% | 0.00% | 4.66% | 0.00% | 0.00% |
| breakout_8 + reversion_12 | 0.47% | -10.50% | 4.66% | 1.01% | 21.94% |
| breakout_8 AND volume_26 | 2.07% | -0.47% | 4.66% | 0.08% | 1.83% |
| breakout_8 + volume_26 | 3.80% | -6.75% | 4.66% | 0.66% | 14.37% |
| reversion_12 AND volume_26 | -2.27% | -5.89% | 4.66% | 0.16% | 3.39% |
| reversion_12 + volume_26 | -0.84% | -9.03% | 4.66% | 0.72% | 15.67% |

동일 구간·초기 자금, 종료 시 청산 비용 포함. 노출 맞춤은 사후 설명용이며 v2 실제 계좌 성과가 아닙니다.
[낙폭 분해·비용 영향·전체 구간](MSFT/comparison.json)

[v1 전체 기록](MSFT/accounts.json) · [v2 전체 기록](MSFT/accounts-v2.json)

## JPM 계좌

| 모델 | 전략 | 평가액 USD | 손익 USD | 최근 매매·이유 |
|---|---|---:|---:|---|
| v1 | cash | 10000.00 | 0.00 | 대기 /  / 새 신호 대기 |
| v1 | buy_hold | 10009.30 | 9.30 | buy /  / buy_hold: prior completed bar target 100%; next bar open simulation |
| v1 | trend_8_26 | 9938.16 | -61.84 | buy /  / trend_8_26: prior completed bar target 100%; next bar open simulation |
| v1 | momentum_26 | 9817.04 | -182.96 | sell /  / momentum_26: prior completed bar target 0%; next bar open simulation |
| v1 | breakout_8 | 9956.81 | -43.19 | sell /  / breakout_8: prior completed bar target 0%; next bar open simulation |
| v1 | reversion_12 | 9950.66 | -49.34 | sell /  / reversion_12: prior completed bar target 0%; next bar open simulation |
| v1 | volume_26 | 10000.00 | 0.00 | 대기 /  / 새 신호 대기 |
| v1 | trend_8_26 AND momentum_26 | 9895.11 | -104.89 | sell /  / trend_8_26 AND momentum_26: prior completed bar target 0%; next bar open simulation |
| v1 | trend_8_26 + momentum_26 | 9897.15 | -102.85 | sell /  / trend_8_26 + momentum_26: prior completed bar target 50%; next bar open simulation |
| v1 | trend_8_26 AND breakout_8 | 10000.00 | 0.00 | 대기 /  / 새 신호 대기 |
| v1 | trend_8_26 + breakout_8 | 9947.47 | -52.53 | buy /  / trend_8_26 + breakout_8: prior completed bar target 50%; next bar open simulation |
| v1 | trend_8_26 AND reversion_12 | 10000.00 | 0.00 | 대기 /  / 새 신호 대기 |
| v1 | trend_8_26 + reversion_12 | 9984.23 | -15.77 | buy /  / trend_8_26 + reversion_12: prior completed bar target 50%; next bar open simulation |
| v1 | trend_8_26 AND volume_26 | 10000.00 | 0.00 | 대기 /  / 새 신호 대기 |
| v1 | trend_8_26 + volume_26 | 9969.04 | -30.96 | buy /  / trend_8_26 + volume_26: prior completed bar target 50%; next bar open simulation |
| v1 | momentum_26 AND breakout_8 | 9956.81 | -43.19 | sell /  / momentum_26 AND breakout_8: prior completed bar target 0%; next bar open simulation |
| v1 | momentum_26 + breakout_8 | 9886.64 | -113.36 | sell /  / momentum_26 + breakout_8: prior completed bar target 0%; next bar open simulation |
| v1 | momentum_26 AND reversion_12 | 10000.00 | 0.00 | 대기 /  / 새 신호 대기 |
| v1 | momentum_26 + reversion_12 | 9943.05 | -56.95 | sell /  / momentum_26 + reversion_12: prior completed bar target 0%; next bar open simulation |
| v1 | momentum_26 AND volume_26 | 10000.00 | 0.00 | 대기 /  / 새 신호 대기 |
| v1 | momentum_26 + volume_26 | 9908.04 | -91.96 | sell /  / momentum_26 + volume_26: prior completed bar target 0%; next bar open simulation |
| v1 | breakout_8 AND reversion_12 | 10000.00 | 0.00 | 대기 /  / 새 신호 대기 |
| v1 | breakout_8 + reversion_12 | 9973.63 | -26.37 | sell /  / breakout_8 + reversion_12: prior completed bar target 0%; next bar open simulation |
| v1 | breakout_8 AND volume_26 | 10000.00 | 0.00 | 대기 /  / 새 신호 대기 |
| v1 | breakout_8 + volume_26 | 9978.36 | -21.64 | sell /  / breakout_8 + volume_26: prior completed bar target 0%; next bar open simulation |
| v1 | reversion_12 AND volume_26 | 10000.00 | 0.00 | 대기 /  / 새 신호 대기 |
| v1 | reversion_12 + volume_26 | 9975.27 | -24.73 | sell /  / reversion_12 + volume_26: prior completed bar target 0%; next bar open simulation |
| v2 | cash | 10000.00 | 0.00 | 대기 /  / 새 신호 대기 |
| v2 | buy_hold | 10004.85 | 4.85 | buy / partial / 직전 완료 봉 목표 비중 100%; 다음 봉 시가 가정 |
| v2 | trend_8_26 | 9848.48 | -151.52 | buy / partial / 직전 완료 봉 목표 비중 100%; 다음 봉 시가 가정 |
| v2 | momentum_26 | 9372.62 | -627.38 | sell / filled / 직전 완료 봉 목표 비중 0%; 다음 봉 시가 가정 |
| v2 | breakout_8 | 9383.42 | -616.58 | sell / filled / 직전 완료 봉 목표 비중 0%; 다음 봉 시가 가정 |
| v2 | reversion_12 | 9991.97 | -8.03 | sell / filled / 직전 완료 봉 목표 비중 0%; 다음 봉 시가 가정 |
| v2 | volume_26 | 9826.70 | -173.30 | sell / filled / 직전 완료 봉 목표 비중 0%; 다음 봉 시가 가정 |
| v2 | trend_8_26 AND momentum_26 | 9828.67 | -171.33 | sell / filled / 직전 완료 봉 목표 비중 0%; 다음 봉 시가 가정 |
| v2 | trend_8_26 + momentum_26 | 9628.31 | -371.69 | sell / filled / 직전 완료 봉 목표 비중 50%; 다음 봉 시가 가정 |
| v2 | trend_8_26 AND breakout_8 | 9420.50 | -579.50 | sell / filled / 직전 완료 봉 목표 비중 0%; 다음 봉 시가 가정 |
| v2 | trend_8_26 + breakout_8 | 9613.73 | -386.27 | buy / filled / 직전 완료 봉 목표 비중 50%; 다음 봉 시가 가정 |
| v2 | trend_8_26 AND reversion_12 | 9981.61 | -18.39 | sell / filled / 직전 완료 봉 목표 비중 0%; 다음 봉 시가 가정 |
| v2 | trend_8_26 + reversion_12 | 9961.80 | -38.20 | buy / filled / 직전 완료 봉 목표 비중 50%; 다음 봉 시가 가정 |
| v2 | trend_8_26 AND volume_26 | 9800.30 | -199.70 | sell / filled / 직전 완료 봉 목표 비중 0%; 다음 봉 시가 가정 |
| v2 | trend_8_26 + volume_26 | 9838.10 | -161.90 | buy / filled / 직전 완료 봉 목표 비중 50%; 다음 봉 시가 가정 |
| v2 | momentum_26 AND breakout_8 | 9364.66 | -635.34 | sell / filled / 직전 완료 봉 목표 비중 0%; 다음 봉 시가 가정 |
| v2 | momentum_26 + breakout_8 | 9398.92 | -601.08 | sell / filled / 직전 완료 봉 목표 비중 0%; 다음 봉 시가 가정 |
| v2 | momentum_26 AND reversion_12 | 9950.76 | -49.24 | sell / filled / 직전 완료 봉 목표 비중 0%; 다음 봉 시가 가정 |
| v2 | momentum_26 + reversion_12 | 9800.47 | -199.53 | sell / filled / 직전 완료 봉 목표 비중 0%; 다음 봉 시가 가정 |
| v2 | momentum_26 AND volume_26 | 9800.30 | -199.70 | sell / filled / 직전 완료 봉 목표 비중 0%; 다음 봉 시가 가정 |
| v2 | momentum_26 + volume_26 | 9658.56 | -341.44 | sell / filled / 직전 완료 봉 목표 비중 0%; 다음 봉 시가 가정 |
| v2 | breakout_8 AND reversion_12 | 10000.00 | 0.00 | 대기 /  / 새 신호 대기 |
| v2 | breakout_8 + reversion_12 | 9723.93 | -276.07 | sell / filled / 직전 완료 봉 목표 비중 0%; 다음 봉 시가 가정 |
| v2 | breakout_8 AND volume_26 | 9893.34 | -106.66 | sell / filled / 직전 완료 봉 목표 비중 0%; 다음 봉 시가 가정 |
| v2 | breakout_8 + volume_26 | 9622.85 | -377.15 | sell / filled / 직전 완료 봉 목표 비중 0%; 다음 봉 시가 가정 |
| v2 | reversion_12 AND volume_26 | 10051.38 | 51.38 | sell / filled / 직전 완료 봉 목표 비중 0%; 다음 봉 시가 가정 |
| v2 | reversion_12 + volume_26 | 9930.12 | -69.88 | sell / filled / 직전 완료 봉 목표 비중 0%; 다음 봉 시가 가정 |

### 같은 기간의 비용·노출 비교 (사후 연구)

| 전략 | 비용 전 | 비용 후 | 100% 보유 | 같은 평균 노출 보유 | 평균 노출 |
|---|---:|---:|---:|---:|---:|
| cash | 0.00% | 0.00% | -1.78% | -0.00% | 0.00% |
| buy_hold | -1.37% | -1.78% | -1.78% | -1.78% | 100.00% |
| trend_8_26 | 0.16% | -3.96% | -1.78% | -0.95% | 52.74% |
| momentum_26 | -2.88% | -9.19% | -1.78% | -0.85% | 47.26% |
| breakout_8 | -3.72% | -17.92% | -1.78% | -0.34% | 18.80% |
| reversion_12 | 4.63% | -9.67% | -1.78% | -0.48% | 26.37% |
| volume_26 | -0.86% | -6.52% | -1.78% | -0.12% | 6.53% |
| trend_8_26 AND momentum_26 | 0.25% | -4.28% | -1.78% | -0.75% | 41.51% |
| trend_8_26 + momentum_26 | -1.36% | -6.41% | -1.78% | -0.90% | 50.00% |
| trend_8_26 AND breakout_8 | -3.76% | -13.36% | -1.78% | -0.21% | 11.49% |
| trend_8_26 + breakout_8 | -1.79% | -11.02% | -1.78% | -0.65% | 35.78% |
| trend_8_26 AND reversion_12 | 2.82% | -3.46% | -1.78% | -0.12% | 6.53% |
| trend_8_26 + reversion_12 | 2.39% | -6.28% | -1.78% | -0.71% | 39.56% |
| trend_8_26 AND volume_26 | -1.33% | -4.99% | -1.78% | -0.07% | 3.92% |
| trend_8_26 + volume_26 | -0.34% | -5.25% | -1.78% | -0.54% | 29.64% |
| momentum_26 AND breakout_8 | -2.61% | -12.31% | -1.78% | -0.20% | 11.23% |
| momentum_26 + breakout_8 | -3.28% | -13.47% | -1.78% | -0.60% | 33.04% |
| momentum_26 AND reversion_12 | 2.89% | -3.80% | -1.78% | -0.10% | 5.48% |
| momentum_26 + reversion_12 | 0.83% | -7.90% | -1.78% | -0.66% | 36.82% |
| momentum_26 AND volume_26 | -0.55% | -3.02% | -1.78% | -0.05% | 2.61% |
| momentum_26 + volume_26 | -1.85% | -7.28% | -1.78% | -0.49% | 26.90% |
| breakout_8 AND reversion_12 | 0.00% | 0.00% | -1.78% | -0.00% | 0.00% |
| breakout_8 + reversion_12 | 0.39% | -12.44% | -1.78% | -0.41% | 22.59% |
| breakout_8 AND volume_26 | -1.26% | -2.50% | -1.78% | -0.01% | 0.78% |
| breakout_8 + volume_26 | -2.29% | -11.30% | -1.78% | -0.23% | 12.67% |
| reversion_12 AND volume_26 | 1.25% | -2.10% | -1.78% | -0.06% | 3.39% |
| reversion_12 + volume_26 | 1.86% | -7.34% | -1.78% | -0.30% | 16.45% |

동일 구간·초기 자금, 종료 시 청산 비용 포함. 노출 맞춤은 사후 설명용이며 v2 실제 계좌 성과가 아닙니다.
[낙폭 분해·비용 영향·전체 구간](JPM/comparison.json)

[v1 전체 기록](JPM/accounts.json) · [v2 전체 기록](JPM/accounts-v2.json)

## XOM 계좌

| 모델 | 전략 | 평가액 USD | 손익 USD | 최근 매매·이유 |
|---|---|---:|---:|---|
| v1 | cash | 10000.00 | 0.00 | 대기 /  / 새 신호 대기 |
| v1 | buy_hold | 9925.95 | -74.05 | buy /  / buy_hold: prior completed bar target 100%; next bar open simulation |
| v1 | trend_8_26 | 10000.00 | 0.00 | 대기 /  / 새 신호 대기 |
| v1 | momentum_26 | 10000.00 | 0.00 | 대기 /  / 새 신호 대기 |
| v1 | breakout_8 | 10000.00 | 0.00 | 대기 /  / 새 신호 대기 |
| v1 | reversion_12 | 9909.33 | -90.67 | sell /  / reversion_12: prior completed bar target 0%; next bar open simulation |
| v1 | volume_26 | 10000.00 | 0.00 | 대기 /  / 새 신호 대기 |
| v1 | trend_8_26 AND momentum_26 | 10000.00 | 0.00 | 대기 /  / 새 신호 대기 |
| v1 | trend_8_26 + momentum_26 | 10000.00 | 0.00 | 대기 /  / 새 신호 대기 |
| v1 | trend_8_26 AND breakout_8 | 10000.00 | 0.00 | 대기 /  / 새 신호 대기 |
| v1 | trend_8_26 + breakout_8 | 10000.00 | 0.00 | 대기 /  / 새 신호 대기 |
| v1 | trend_8_26 AND reversion_12 | 10000.00 | 0.00 | 대기 /  / 새 신호 대기 |
| v1 | trend_8_26 + reversion_12 | 9954.50 | -45.50 | sell /  / trend_8_26 + reversion_12: prior completed bar target 0%; next bar open simulation |
| v1 | trend_8_26 AND volume_26 | 10000.00 | 0.00 | 대기 /  / 새 신호 대기 |
| v1 | trend_8_26 + volume_26 | 10000.00 | 0.00 | 대기 /  / 새 신호 대기 |
| v1 | momentum_26 AND breakout_8 | 10000.00 | 0.00 | 대기 /  / 새 신호 대기 |
| v1 | momentum_26 + breakout_8 | 10000.00 | 0.00 | 대기 /  / 새 신호 대기 |
| v1 | momentum_26 AND reversion_12 | 10000.00 | 0.00 | 대기 /  / 새 신호 대기 |
| v1 | momentum_26 + reversion_12 | 9954.50 | -45.50 | sell /  / momentum_26 + reversion_12: prior completed bar target 0%; next bar open simulation |
| v1 | momentum_26 AND volume_26 | 10000.00 | 0.00 | 대기 /  / 새 신호 대기 |
| v1 | momentum_26 + volume_26 | 10000.00 | 0.00 | 대기 /  / 새 신호 대기 |
| v1 | breakout_8 AND reversion_12 | 10000.00 | 0.00 | 대기 /  / 새 신호 대기 |
| v1 | breakout_8 + reversion_12 | 9954.50 | -45.50 | sell /  / breakout_8 + reversion_12: prior completed bar target 0%; next bar open simulation |
| v1 | breakout_8 AND volume_26 | 10000.00 | 0.00 | 대기 /  / 새 신호 대기 |
| v1 | breakout_8 + volume_26 | 10000.00 | 0.00 | 대기 /  / 새 신호 대기 |
| v1 | reversion_12 AND volume_26 | 10000.00 | 0.00 | 대기 /  / 새 신호 대기 |
| v1 | reversion_12 + volume_26 | 9954.50 | -45.50 | sell /  / reversion_12 + volume_26: prior completed bar target 0%; next bar open simulation |
| v2 | cash | 10000.00 | 0.00 | 대기 /  / 새 신호 대기 |
| v2 | buy_hold | 10173.93 | 173.93 | buy / partial / 직전 완료 봉 목표 비중 100%; 다음 봉 시가 가정 |
| v2 | trend_8_26 | 10096.25 | 96.25 | sell / filled / 직전 완료 봉 목표 비중 0%; 다음 봉 시가 가정 |
| v2 | momentum_26 | 10172.64 | 172.64 | sell / filled / 직전 완료 봉 목표 비중 0%; 다음 봉 시가 가정 |
| v2 | breakout_8 | 9471.02 | -528.98 | sell / filled / 직전 완료 봉 목표 비중 0%; 다음 봉 시가 가정 |
| v2 | reversion_12 | 9737.14 | -262.86 | sell / filled / 직전 완료 봉 목표 비중 0%; 다음 봉 시가 가정 |
| v2 | volume_26 | 9908.04 | -91.96 | sell / filled / 직전 완료 봉 목표 비중 0%; 다음 봉 시가 가정 |
| v2 | trend_8_26 AND momentum_26 | 10103.74 | 103.74 | sell / filled / 직전 완료 봉 목표 비중 0%; 다음 봉 시가 가정 |
| v2 | trend_8_26 + momentum_26 | 10134.41 | 134.41 | sell / filled / 직전 완료 봉 목표 비중 0%; 다음 봉 시가 가정 |
| v2 | trend_8_26 AND breakout_8 | 9453.73 | -546.27 | sell / filled / 직전 완료 봉 목표 비중 0%; 다음 봉 시가 가정 |
| v2 | trend_8_26 + breakout_8 | 9799.57 | -200.43 | sell / filled / 직전 완료 봉 목표 비중 0%; 다음 봉 시가 가정 |
| v2 | trend_8_26 AND reversion_12 | 9839.70 | -160.30 | sell / filled / 직전 완료 봉 목표 비중 0%; 다음 봉 시가 가정 |
| v2 | trend_8_26 + reversion_12 | 9914.98 | -85.02 | sell / filled / 직전 완료 봉 목표 비중 0%; 다음 봉 시가 가정 |
| v2 | trend_8_26 AND volume_26 | 9895.61 | -104.39 | sell / filled / 직전 완료 봉 목표 비중 0%; 다음 봉 시가 가정 |
| v2 | trend_8_26 + volume_26 | 10001.66 | 1.66 | sell / filled / 직전 완료 봉 목표 비중 0%; 다음 봉 시가 가정 |
| v2 | momentum_26 AND breakout_8 | 9471.02 | -528.98 | sell / filled / 직전 완료 봉 목표 비중 0%; 다음 봉 시가 가정 |
| v2 | momentum_26 + breakout_8 | 9816.10 | -183.90 | sell / filled / 직전 완료 봉 목표 비중 0%; 다음 봉 시가 가정 |
| v2 | momentum_26 AND reversion_12 | 9800.13 | -199.87 | sell / filled / 직전 완료 봉 목표 비중 0%; 다음 봉 시가 가정 |
| v2 | momentum_26 + reversion_12 | 9952.45 | -47.55 | sell / filled / 직전 완료 봉 목표 비중 0%; 다음 봉 시가 가정 |
| v2 | momentum_26 AND volume_26 | 9957.96 | -42.04 | sell / filled / 직전 완료 봉 목표 비중 0%; 다음 봉 시가 가정 |
| v2 | momentum_26 + volume_26 | 10060.52 | 60.52 | sell / filled / 직전 완료 봉 목표 비중 0%; 다음 봉 시가 가정 |
| v2 | breakout_8 AND reversion_12 | 10000.00 | 0.00 | 대기 /  / 새 신호 대기 |
| v2 | breakout_8 + reversion_12 | 9602.90 | -397.10 | sell / filled / 직전 완료 봉 목표 비중 0%; 다음 봉 시가 가정 |
| v2 | breakout_8 AND volume_26 | 9970.25 | -29.75 | sell / filled / 직전 완료 봉 목표 비중 0%; 다음 봉 시가 가정 |
| v2 | breakout_8 + volume_26 | 9707.34 | -292.66 | sell / filled / 직전 완료 봉 목표 비중 0%; 다음 봉 시가 가정 |
| v2 | reversion_12 AND volume_26 | 9949.87 | -50.13 | sell / filled / 직전 완료 봉 목표 비중 0%; 다음 봉 시가 가정 |
| v2 | reversion_12 + volume_26 | 9822.04 | -177.96 | sell / filled / 직전 완료 봉 목표 비중 0%; 다음 봉 시가 가정 |

### 같은 기간의 비용·노출 비교 (사후 연구)

| 전략 | 비용 전 | 비용 후 | 100% 보유 | 같은 평균 노출 보유 | 평균 노출 |
|---|---:|---:|---:|---:|---:|
| cash | 0.00% | 0.00% | 7.86% | 0.00% | 0.00% |
| buy_hold | 8.31% | 7.86% | 7.86% | 7.86% | 100.00% |
| trend_8_26 | 1.00% | -3.16% | 7.86% | 4.84% | 62.40% |
| momentum_26 | 0.22% | -6.69% | 7.86% | 5.28% | 67.89% |
| breakout_8 | -3.59% | -20.53% | 7.86% | 1.74% | 22.72% |
| reversion_12 | 5.77% | -5.57% | 7.86% | 1.64% | 21.41% |
| volume_26 | 4.51% | -2.69% | 7.86% | 0.34% | 4.44% |
| trend_8_26 AND momentum_26 | -0.45% | -4.95% | 7.86% | 4.43% | 57.18% |
| trend_8_26 + momentum_26 | 0.62% | -4.73% | 7.86% | 5.06% | 65.15% |
| trend_8_26 AND breakout_8 | -1.20% | -14.70% | 7.86% | 1.36% | 17.75% |
| trend_8_26 + breakout_8 | -1.30% | -12.07% | 7.86% | 3.28% | 42.57% |
| trend_8_26 AND reversion_12 | 1.89% | -3.93% | 7.86% | 0.62% | 8.09% |
| trend_8_26 + reversion_12 | 3.38% | -4.17% | 7.86% | 3.23% | 41.91% |
| trend_8_26 AND volume_26 | 2.54% | -1.67% | 7.86% | 0.20% | 2.61% |
| trend_8_26 + volume_26 | 2.76% | -2.52% | 7.86% | 2.57% | 33.42% |
| momentum_26 AND breakout_8 | -3.06% | -18.40% | 7.86% | 1.56% | 20.37% |
| momentum_26 + breakout_8 | -1.68% | -13.87% | 7.86% | 3.50% | 45.31% |
| momentum_26 AND reversion_12 | 2.27% | -4.38% | 7.86% | 0.68% | 8.88% |
| momentum_26 + reversion_12 | 2.98% | -4.74% | 7.86% | 3.44% | 44.65% |
| momentum_26 AND volume_26 | 2.32% | -1.47% | 7.86% | 0.18% | 2.35% |
| momentum_26 + volume_26 | 2.37% | -3.29% | 7.86% | 2.78% | 36.17% |
| breakout_8 AND reversion_12 | 0.00% | 0.00% | 7.86% | 0.00% | 0.00% |
| breakout_8 + reversion_12 | 1.00% | -13.01% | 7.86% | 1.69% | 22.07% |
| breakout_8 AND volume_26 | 0.60% | -0.66% | 7.86% | 0.06% | 0.78% |
| breakout_8 + volume_26 | 0.39% | -10.94% | 7.86% | 1.04% | 13.58% |
| reversion_12 AND volume_26 | 1.52% | -1.00% | 7.86% | 0.12% | 1.57% |
| reversion_12 + volume_26 | 5.15% | -3.53% | 7.86% | 0.99% | 12.93% |

동일 구간·초기 자금, 종료 시 청산 비용 포함. 노출 맞춤은 사후 설명용이며 v2 실제 계좌 성과가 아닙니다.
[낙폭 분해·비용 영향·전체 구간](XOM/comparison.json)

[v1 전체 기록](XOM/accounts.json) · [v2 전체 기록](XOM/accounts-v2.json)

## JNJ 계좌

| 모델 | 전략 | 평가액 USD | 손익 USD | 최근 매매·이유 |
|---|---|---:|---:|---|
| v1 | cash | 10000.00 | 0.00 | 대기 /  / 새 신호 대기 |
| v1 | buy_hold | 9771.69 | -228.31 | buy /  / buy_hold: prior completed bar target 100%; next bar open simulation |
| v1 | trend_8_26 | 9797.20 | -202.80 | sell /  / trend_8_26: prior completed bar target 0%; next bar open simulation |
| v1 | momentum_26 | 9758.70 | -241.30 | sell /  / momentum_26: prior completed bar target 0%; next bar open simulation |
| v1 | breakout_8 | 10000.00 | 0.00 | 대기 /  / 새 신호 대기 |
| v1 | reversion_12 | 9821.81 | -178.19 | buy /  / reversion_12: prior completed bar target 100%; next bar open simulation |
| v1 | volume_26 | 10000.00 | 0.00 | 대기 /  / 새 신호 대기 |
| v1 | trend_8_26 AND momentum_26 | 9797.20 | -202.80 | sell /  / trend_8_26 AND momentum_26: prior completed bar target 0%; next bar open simulation |
| v1 | trend_8_26 + momentum_26 | 9777.93 | -222.07 | sell /  / trend_8_26 + momentum_26: prior completed bar target 0%; next bar open simulation |
| v1 | trend_8_26 AND breakout_8 | 10000.00 | 0.00 | 대기 /  / 새 신호 대기 |
| v1 | trend_8_26 + breakout_8 | 9898.11 | -101.89 | sell /  / trend_8_26 + breakout_8: prior completed bar target 0%; next bar open simulation |
| v1 | trend_8_26 AND reversion_12 | 9847.46 | -152.54 | sell /  / trend_8_26 AND reversion_12: prior completed bar target 0%; next bar open simulation |
| v1 | trend_8_26 + reversion_12 | 9809.50 | -190.50 | buy /  / trend_8_26 + reversion_12: prior completed bar target 50%; next bar open simulation |
| v1 | trend_8_26 AND volume_26 | 10000.00 | 0.00 | 대기 /  / 새 신호 대기 |
| v1 | trend_8_26 + volume_26 | 9898.11 | -101.89 | sell /  / trend_8_26 + volume_26: prior completed bar target 0%; next bar open simulation |
| v1 | momentum_26 AND breakout_8 | 10000.00 | 0.00 | 대기 /  / 새 신호 대기 |
| v1 | momentum_26 + breakout_8 | 9878.59 | -121.41 | sell /  / momentum_26 + breakout_8: prior completed bar target 0%; next bar open simulation |
| v1 | momentum_26 AND reversion_12 | 9808.75 | -191.25 | sell /  / momentum_26 AND reversion_12: prior completed bar target 0%; next bar open simulation |
| v1 | momentum_26 + reversion_12 | 9790.22 | -209.78 | buy /  / momentum_26 + reversion_12: prior completed bar target 50%; next bar open simulation |
| v1 | momentum_26 AND volume_26 | 10000.00 | 0.00 | 대기 /  / 새 신호 대기 |
| v1 | momentum_26 + volume_26 | 9878.59 | -121.41 | sell /  / momentum_26 + volume_26: prior completed bar target 0%; next bar open simulation |
| v1 | breakout_8 AND reversion_12 | 10000.00 | 0.00 | 대기 /  / 새 신호 대기 |
| v1 | breakout_8 + reversion_12 | 9910.45 | -89.55 | buy /  / breakout_8 + reversion_12: prior completed bar target 50%; next bar open simulation |
| v1 | breakout_8 AND volume_26 | 10000.00 | 0.00 | 대기 /  / 새 신호 대기 |
| v1 | breakout_8 + volume_26 | 10000.00 | 0.00 | 대기 /  / 새 신호 대기 |
| v1 | reversion_12 AND volume_26 | 10000.00 | 0.00 | 대기 /  / 새 신호 대기 |
| v1 | reversion_12 + volume_26 | 9910.45 | -89.55 | buy /  / reversion_12 + volume_26: prior completed bar target 50%; next bar open simulation |
| v2 | cash | 10000.00 | 0.00 | 대기 /  / 새 신호 대기 |
| v2 | buy_hold | 9661.28 | -338.72 | 중단: 손실 한도 / buy / partial / 직전 완료 봉 목표 비중 100%; 다음 봉 시가 가정 |
| v2 | trend_8_26 | 9661.28 | -338.72 | 중단: 손실 한도 / buy / partial / 직전 완료 봉 목표 비중 100%; 다음 봉 시가 가정 |
| v2 | momentum_26 | 9661.28 | -338.72 | 중단: 손실 한도 / buy / partial / 직전 완료 봉 목표 비중 100%; 다음 봉 시가 가정 |
| v2 | breakout_8 | 9343.39 | -656.61 | 중단: 손실 한도 / sell / filled / 직전 완료 봉 목표 비중 0%; 다음 봉 시가 가정 |
| v2 | reversion_12 | 9710.33 | -289.67 | buy / partial / 직전 완료 봉 목표 비중 100%; 다음 봉 시가 가정 |
| v2 | volume_26 | 9791.36 | -208.64 | sell / filled / 직전 완료 봉 목표 비중 0%; 다음 봉 시가 가정 |
| v2 | trend_8_26 AND momentum_26 | 9661.28 | -338.72 | 중단: 손실 한도 / buy / partial / 직전 완료 봉 목표 비중 100%; 다음 봉 시가 가정 |
| v2 | trend_8_26 + momentum_26 | 9661.28 | -338.72 | 중단: 손실 한도 / buy / partial / 직전 완료 봉 목표 비중 100%; 다음 봉 시가 가정 |
| v2 | trend_8_26 AND breakout_8 | 9419.39 | -580.61 | 중단: 손실 한도 / sell / filled / 직전 완료 봉 목표 비중 0%; 다음 봉 시가 가정 |
| v2 | trend_8_26 + breakout_8 | 9569.82 | -430.18 | sell / filled / 직전 완료 봉 목표 비중 0%; 다음 봉 시가 가정 |
| v2 | trend_8_26 AND reversion_12 | 9978.08 | -21.92 | sell / filled / 직전 완료 봉 목표 비중 0%; 다음 봉 시가 가정 |
| v2 | trend_8_26 + reversion_12 | 9732.92 | -267.08 | 중단: 손실 한도 / sell / filled / 직전 완료 봉 목표 비중 0%; 다음 봉 시가 가정 |
| v2 | trend_8_26 AND volume_26 | 9870.71 | -129.29 | sell / filled / 직전 완료 봉 목표 비중 0%; 다음 봉 시가 가정 |
| v2 | trend_8_26 + volume_26 | 9802.98 | -197.02 | 중단: 손실 한도 / buy / filled / 직전 완료 봉 목표 비중 50%; 다음 봉 시가 가정 |
| v2 | momentum_26 AND breakout_8 | 9598.70 | -401.30 | sell / filled / 직전 완료 봉 목표 비중 0%; 다음 봉 시가 가정 |
| v2 | momentum_26 + breakout_8 | 9553.32 | -446.68 | sell / filled / 직전 완료 봉 목표 비중 0%; 다음 봉 시가 가정 |
| v2 | momentum_26 AND reversion_12 | 9938.87 | -61.13 | sell / filled / 직전 완료 봉 목표 비중 0%; 다음 봉 시가 가정 |
| v2 | momentum_26 + reversion_12 | 9732.92 | -267.08 | 중단: 손실 한도 / sell / filled / 직전 완료 봉 목표 비중 0%; 다음 봉 시가 가정 |
| v2 | momentum_26 AND volume_26 | 9920.93 | -79.07 | sell / filled / 직전 완료 봉 목표 비중 0%; 다음 봉 시가 가정 |
| v2 | momentum_26 + volume_26 | 9802.98 | -197.02 | 중단: 손실 한도 / buy / filled / 직전 완료 봉 목표 비중 50%; 다음 봉 시가 가정 |
| v2 | breakout_8 AND reversion_12 | 10000.00 | 0.00 | 대기 /  / 새 신호 대기 |
| v2 | breakout_8 + reversion_12 | 9591.06 | -408.94 | buy / filled / 직전 완료 봉 목표 비중 50%; 다음 봉 시가 가정 |
| v2 | breakout_8 AND volume_26 | 9814.17 | -185.83 | sell / filled / 직전 완료 봉 목표 비중 0%; 다음 봉 시가 가정 |
| v2 | breakout_8 + volume_26 | 9610.69 | -389.31 | sell / filled / 직전 완료 봉 목표 비중 0%; 다음 봉 시가 가정 |
| v2 | reversion_12 AND volume_26 | 9886.24 | -113.76 | sell / filled / 직전 완료 봉 목표 비중 0%; 다음 봉 시가 가정 |
| v2 | reversion_12 + volume_26 | 9771.52 | -228.48 | buy / filled / 직전 완료 봉 목표 비중 50%; 다음 봉 시가 가정 |

### 같은 기간의 비용·노출 비교 (사후 연구)

| 전략 | 비용 전 | 비용 후 | 100% 보유 | 같은 평균 노출 보유 | 평균 노출 |
|---|---:|---:|---:|---:|---:|
| cash | 0.00% | 0.00% | -6.59% | -0.00% | 0.00% |
| buy_hold | -6.20% | -6.59% | -6.59% | -6.59% | 100.00% |
| trend_8_26 | 2.50% | 0.37% | -6.59% | -3.18% | 47.26% |
| momentum_26 | 0.35% | -2.97% | -6.59% | -3.16% | 47.00% |
| breakout_8 | -0.27% | -16.75% | -6.59% | -1.42% | 20.89% |
| reversion_12 | -7.41% | -16.64% | -6.59% | -2.07% | 30.55% |
| volume_26 | -0.65% | -7.11% | -6.59% | -0.45% | 6.53% |
| trend_8_26 AND momentum_26 | 2.35% | -0.62% | -6.59% | -2.92% | 43.34% |
| trend_8_26 + momentum_26 | 1.42% | -1.31% | -6.59% | -3.17% | 47.13% |
| trend_8_26 AND breakout_8 | 0.78% | -11.52% | -6.59% | -1.03% | 15.14% |
| trend_8_26 + breakout_8 | 1.13% | -8.38% | -6.59% | -2.31% | 34.08% |
| trend_8_26 AND reversion_12 | 0.69% | -2.63% | -6.59% | -0.38% | 5.48% |
| trend_8_26 + reversion_12 | -2.55% | -8.14% | -6.59% | -2.63% | 38.91% |
| trend_8_26 AND volume_26 | 1.59% | -0.53% | -6.59% | -0.11% | 1.57% |
| trend_8_26 + volume_26 | 0.94% | -3.02% | -6.59% | -1.83% | 26.90% |
| momentum_26 AND breakout_8 | 2.20% | -9.52% | -6.59% | -0.98% | 14.36% |
| momentum_26 + breakout_8 | 0.07% | -9.91% | -6.59% | -2.30% | 33.95% |
| momentum_26 AND reversion_12 | -0.60% | -3.89% | -6.59% | -0.46% | 6.79% |
| momentum_26 + reversion_12 | -3.58% | -9.49% | -6.59% | -2.62% | 38.78% |
| momentum_26 AND volume_26 | 1.57% | -0.12% | -6.59% | -0.09% | 1.31% |
| momentum_26 + volume_26 | -0.12% | -4.45% | -6.59% | -1.82% | 26.77% |
| breakout_8 AND reversion_12 | 0.00% | 0.00% | -6.59% | -0.00% | 0.00% |
| breakout_8 + reversion_12 | -3.88% | -16.17% | -6.59% | -1.75% | 25.73% |
| breakout_8 AND volume_26 | -0.11% | -2.19% | -6.59% | -0.11% | 1.57% |
| breakout_8 + volume_26 | -0.45% | -11.32% | -6.59% | -0.94% | 13.71% |
| reversion_12 AND volume_26 | -1.99% | -4.42% | -6.59% | -0.18% | 2.61% |
| reversion_12 + volume_26 | -4.07% | -11.26% | -6.59% | -1.26% | 18.54% |

동일 구간·초기 자금, 종료 시 청산 비용 포함. 노출 맞춤은 사후 설명용이며 v2 실제 계좌 성과가 아닙니다.
[낙폭 분해·비용 영향·전체 구간](JNJ/comparison.json)

[v1 전체 기록](JNJ/accounts.json) · [v2 전체 기록](JNJ/accounts-v2.json)

## CAT 계좌

| 모델 | 전략 | 평가액 USD | 손익 USD | 최근 매매·이유 |
|---|---|---:|---:|---|
| v1 | cash | 10000.00 | 0.00 | 대기 /  / 새 신호 대기 |
| v1 | buy_hold | 10055.63 | 55.63 | buy /  / buy_hold: prior completed bar target 100%; next bar open simulation |
| v1 | trend_8_26 | 10000.00 | 0.00 | 대기 /  / 새 신호 대기 |
| v1 | momentum_26 | 10000.00 | 0.00 | 대기 /  / 새 신호 대기 |
| v1 | breakout_8 | 10054.81 | 54.81 | buy /  / breakout_8: prior completed bar target 100%; next bar open simulation |
| v1 | reversion_12 | 9995.30 | -4.70 | sell /  / reversion_12: prior completed bar target 0%; next bar open simulation |
| v1 | volume_26 | 9965.26 | -34.74 | sell /  / volume_26: prior completed bar target 0%; next bar open simulation |
| v1 | trend_8_26 AND momentum_26 | 10000.00 | 0.00 | 대기 /  / 새 신호 대기 |
| v1 | trend_8_26 + momentum_26 | 10000.00 | 0.00 | 대기 /  / 새 신호 대기 |
| v1 | trend_8_26 AND breakout_8 | 10000.00 | 0.00 | 대기 /  / 새 신호 대기 |
| v1 | trend_8_26 + breakout_8 | 10027.46 | 27.46 | buy /  / trend_8_26 + breakout_8: prior completed bar target 50%; next bar open simulation |
| v1 | trend_8_26 AND reversion_12 | 10000.00 | 0.00 | 대기 /  / 새 신호 대기 |
| v1 | trend_8_26 + reversion_12 | 9997.64 | -2.36 | sell /  / trend_8_26 + reversion_12: prior completed bar target 0%; next bar open simulation |
| v1 | trend_8_26 AND volume_26 | 10000.00 | 0.00 | 대기 /  / 새 신호 대기 |
| v1 | trend_8_26 + volume_26 | 9982.60 | -17.40 | sell /  / trend_8_26 + volume_26: prior completed bar target 0%; next bar open simulation |
| v1 | momentum_26 AND breakout_8 | 10000.00 | 0.00 | 대기 /  / 새 신호 대기 |
| v1 | momentum_26 + breakout_8 | 10027.46 | 27.46 | buy /  / momentum_26 + breakout_8: prior completed bar target 50%; next bar open simulation |
| v1 | momentum_26 AND reversion_12 | 10000.00 | 0.00 | 대기 /  / 새 신호 대기 |
| v1 | momentum_26 + reversion_12 | 9997.64 | -2.36 | sell /  / momentum_26 + reversion_12: prior completed bar target 0%; next bar open simulation |
| v1 | momentum_26 AND volume_26 | 10000.00 | 0.00 | 대기 /  / 새 신호 대기 |
| v1 | momentum_26 + volume_26 | 9982.60 | -17.40 | sell /  / momentum_26 + volume_26: prior completed bar target 0%; next bar open simulation |
| v1 | breakout_8 AND reversion_12 | 10000.00 | 0.00 | 대기 /  / 새 신호 대기 |
| v1 | breakout_8 + reversion_12 | 10025.09 | 25.09 | buy /  / breakout_8 + reversion_12: prior completed bar target 50%; next bar open simulation |
| v1 | breakout_8 AND volume_26 | 10000.00 | 0.00 | 대기 /  / 새 신호 대기 |
| v1 | breakout_8 + volume_26 | 10010.01 | 10.01 | buy /  / breakout_8 + volume_26: prior completed bar target 50%; next bar open simulation |
| v1 | reversion_12 AND volume_26 | 10000.00 | 0.00 | 대기 /  / 새 신호 대기 |
| v1 | reversion_12 + volume_26 | 9980.24 | -19.76 | sell /  / reversion_12 + volume_26: prior completed bar target 0%; next bar open simulation |
| v2 | cash | 10000.00 | 0.00 | 대기 /  / 새 신호 대기 |
| v2 | buy_hold | 9192.88 | -807.12 | 중단: 손실 한도 / buy / partial / 직전 완료 봉 목표 비중 100%; 다음 봉 시가 가정 |
| v2 | trend_8_26 | 9941.61 | -58.39 | sell / filled / 직전 완료 봉 목표 비중 0%; 다음 봉 시가 가정 |
| v2 | momentum_26 | 10014.59 | 14.59 | sell / filled / 직전 완료 봉 목표 비중 0%; 다음 봉 시가 가정 |
| v2 | breakout_8 | 9859.22 | -140.78 | buy / partial / 직전 완료 봉 목표 비중 100%; 다음 봉 시가 가정 |
| v2 | reversion_12 | 9064.50 | -935.50 | 중단: 손실 한도 / buy / partial / 직전 완료 봉 목표 비중 100%; 다음 봉 시가 가정 |
| v2 | volume_26 | 9323.73 | -676.27 | 중단: 손실 한도 / buy / partial / 직전 완료 봉 목표 비중 100%; 다음 봉 시가 가정 |
| v2 | trend_8_26 AND momentum_26 | 10043.59 | 43.59 | sell / filled / 직전 완료 봉 목표 비중 0%; 다음 봉 시가 가정 |
| v2 | trend_8_26 + momentum_26 | 9978.08 | -21.92 | sell / filled / 직전 완료 봉 목표 비중 0%; 다음 봉 시가 가정 |
| v2 | trend_8_26 AND breakout_8 | 9976.12 | -23.88 | sell / filled / 직전 완료 봉 목표 비중 0%; 다음 봉 시가 가정 |
| v2 | trend_8_26 + breakout_8 | 9900.53 | -99.47 | buy / filled / 직전 완료 봉 목표 비중 50%; 다음 봉 시가 가정 |
| v2 | trend_8_26 AND reversion_12 | 9815.07 | -184.93 | sell / filled / 직전 완료 봉 목표 비중 0%; 다음 봉 시가 가정 |
| v2 | trend_8_26 + reversion_12 | 9633.42 | -366.58 | sell / filled / 직전 완료 봉 목표 비중 0%; 다음 봉 시가 가정 |
| v2 | trend_8_26 AND volume_26 | 10035.44 | 35.44 | sell / filled / 직전 완료 봉 목표 비중 0%; 다음 봉 시가 가정 |
| v2 | trend_8_26 + volume_26 | 9641.27 | -358.73 | sell / filled / 직전 완료 봉 목표 비중 0%; 다음 봉 시가 가정 |
| v2 | momentum_26 AND breakout_8 | 9977.43 | -22.57 | sell / filled / 직전 완료 봉 목표 비중 0%; 다음 봉 시가 가정 |
| v2 | momentum_26 + breakout_8 | 9936.78 | -63.22 | buy / filled / 직전 완료 봉 목표 비중 50%; 다음 봉 시가 가정 |
| v2 | momentum_26 AND reversion_12 | 9874.73 | -125.27 | sell / filled / 직전 완료 봉 목표 비중 0%; 다음 봉 시가 가정 |
| v2 | momentum_26 + reversion_12 | 9668.67 | -331.33 | sell / filled / 직전 완료 봉 목표 비중 0%; 다음 봉 시가 가정 |
| v2 | momentum_26 AND volume_26 | 10048.78 | 48.78 | sell / filled / 직전 완료 봉 목표 비중 0%; 다음 봉 시가 가정 |
| v2 | momentum_26 + volume_26 | 9696.91 | -303.09 | sell / filled / 직전 완료 봉 목표 비중 0%; 다음 봉 시가 가정 |
| v2 | breakout_8 AND reversion_12 | 10000.00 | 0.00 | 대기 /  / 새 신호 대기 |
| v2 | breakout_8 + reversion_12 | 9610.18 | -389.82 | 중단: 손실 한도 / sell / filled / 직전 완료 봉 목표 비중 0%; 다음 봉 시가 가정 |
| v2 | breakout_8 AND volume_26 | 9998.69 | -1.31 | sell / filled / 직전 완료 봉 목표 비중 0%; 다음 봉 시가 가정 |
| v2 | breakout_8 + volume_26 | 9621.53 | -378.47 | buy / filled / 직전 완료 봉 목표 비중 50%; 다음 봉 시가 가정 |
| v2 | reversion_12 AND volume_26 | 9259.23 | -740.77 | 중단: 손실 한도 / buy / partial / 직전 완료 봉 목표 비중 100%; 다음 봉 시가 가정 |
| v2 | reversion_12 + volume_26 | 9395.03 | -604.97 | 중단: 손실 한도 / sell / filled / 직전 완료 봉 목표 비중 50%; 다음 봉 시가 가정 |

### 같은 기간의 비용·노출 비교 (사후 연구)

| 전략 | 비용 전 | 비용 후 | 100% 보유 | 같은 평균 노출 보유 | 평균 노출 |
|---|---:|---:|---:|---:|---:|
| cash | 0.00% | 0.00% | -9.80% | -0.00% | 0.00% |
| buy_hold | -9.42% | -9.80% | -9.80% | -9.80% | 100.00% |
| trend_8_26 | -0.82% | -4.10% | -9.80% | -4.98% | 50.65% |
| momentum_26 | -3.11% | -8.65% | -9.80% | -4.93% | 50.13% |
| breakout_8 | -3.10% | -16.00% | -9.80% | -1.41% | 14.36% |
| reversion_12 | -3.89% | -15.27% | -9.80% | -2.52% | 25.59% |
| volume_26 | -2.95% | -10.02% | -9.80% | -0.80% | 8.09% |
| trend_8_26 AND momentum_26 | -0.39% | -4.88% | -9.80% | -4.37% | 44.39% |
| trend_8_26 + momentum_26 | -1.96% | -6.39% | -9.80% | -4.96% | 50.39% |
| trend_8_26 AND breakout_8 | -1.72% | -8.87% | -9.80% | -0.69% | 7.05% |
| trend_8_26 + breakout_8 | -1.93% | -10.03% | -9.80% | -3.20% | 32.51% |
| trend_8_26 AND reversion_12 | 0.78% | -5.38% | -9.80% | -0.69% | 7.05% |
| trend_8_26 + reversion_12 | -2.31% | -9.27% | -9.80% | -3.75% | 38.12% |
| trend_8_26 AND volume_26 | 2.22% | -0.75% | -9.80% | -0.26% | 2.61% |
| trend_8_26 + volume_26 | -1.84% | -6.89% | -9.80% | -2.89% | 29.38% |
| momentum_26 AND breakout_8 | -2.81% | -11.01% | -9.80% | -0.85% | 8.62% |
| momentum_26 + breakout_8 | -3.07% | -12.37% | -9.80% | -3.17% | 32.25% |
| momentum_26 AND reversion_12 | -3.04% | -8.96% | -9.80% | -0.57% | 5.74% |
| momentum_26 + reversion_12 | -3.45% | -11.07% | -9.80% | -3.73% | 37.86% |
| momentum_26 AND volume_26 | 1.58% | -0.53% | -9.80% | -0.15% | 1.57% |
| momentum_26 + volume_26 | -2.97% | -8.54% | -9.80% | -2.87% | 29.12% |
| breakout_8 AND reversion_12 | 0.00% | 0.00% | -9.80% | -0.00% | 0.00% |
| breakout_8 + reversion_12 | -3.45% | -14.73% | -9.80% | -1.97% | 19.98% |
| breakout_8 AND volume_26 | 0.37% | -0.47% | -9.80% | -0.05% | 0.52% |
| breakout_8 + volume_26 | -2.99% | -12.31% | -9.80% | -1.11% | 11.23% |
| reversion_12 AND volume_26 | -1.25% | -5.71% | -9.80% | -0.51% | 5.22% |
| reversion_12 + volume_26 | -3.39% | -11.93% | -9.80% | -1.66% | 16.85% |

동일 구간·초기 자금, 종료 시 청산 비용 포함. 노출 맞춤은 사후 설명용이며 v2 실제 계좌 성과가 아닙니다.
[낙폭 분해·비용 영향·전체 구간](CAT/comparison.json)

[v1 전체 기록](CAT/accounts.json) · [v2 전체 기록](CAT/accounts-v2.json)

## WMT 계좌

| 모델 | 전략 | 평가액 USD | 손익 USD | 최근 매매·이유 |
|---|---|---:|---:|---|
| v1 | cash | 10000.00 | 0.00 | 대기 /  / 새 신호 대기 |
| v1 | buy_hold | 9883.04 | -116.96 | buy /  / buy_hold: prior completed bar target 100%; next bar open simulation |
| v1 | trend_8_26 | 9869.47 | -130.53 | sell /  / trend_8_26: prior completed bar target 0%; next bar open simulation |
| v1 | momentum_26 | 9883.04 | -116.96 | buy /  / momentum_26: prior completed bar target 100%; next bar open simulation |
| v1 | breakout_8 | 10000.00 | 0.00 | 대기 /  / 새 신호 대기 |
| v1 | reversion_12 | 9896.39 | -103.61 | buy /  / reversion_12: prior completed bar target 100%; next bar open simulation |
| v1 | volume_26 | 10000.00 | 0.00 | 대기 /  / 새 신호 대기 |
| v1 | trend_8_26 AND momentum_26 | 9869.47 | -130.53 | sell /  / trend_8_26 AND momentum_26: prior completed bar target 0%; next bar open simulation |
| v1 | trend_8_26 + momentum_26 | 9876.25 | -123.75 | sell /  / trend_8_26 + momentum_26: prior completed bar target 50%; next bar open simulation |
| v1 | trend_8_26 AND breakout_8 | 10000.00 | 0.00 | 대기 /  / 새 신호 대기 |
| v1 | trend_8_26 + breakout_8 | 9934.46 | -65.54 | sell /  / trend_8_26 + breakout_8: prior completed bar target 0%; next bar open simulation |
| v1 | trend_8_26 AND reversion_12 | 9882.79 | -117.21 | sell /  / trend_8_26 AND reversion_12: prior completed bar target 0%; next bar open simulation |
| v1 | trend_8_26 + reversion_12 | 9882.89 | -117.11 | sell /  / trend_8_26 + reversion_12: prior completed bar target 50%; next bar open simulation |
| v1 | trend_8_26 AND volume_26 | 10000.00 | 0.00 | 대기 /  / 새 신호 대기 |
| v1 | trend_8_26 + volume_26 | 9934.46 | -65.54 | sell /  / trend_8_26 + volume_26: prior completed bar target 0%; next bar open simulation |
| v1 | momentum_26 AND breakout_8 | 10000.00 | 0.00 | 대기 /  / 새 신호 대기 |
| v1 | momentum_26 + breakout_8 | 9941.28 | -58.72 | buy /  / momentum_26 + breakout_8: prior completed bar target 50%; next bar open simulation |
| v1 | momentum_26 AND reversion_12 | 9896.39 | -103.61 | buy /  / momentum_26 AND reversion_12: prior completed bar target 100%; next bar open simulation |
| v1 | momentum_26 + reversion_12 | 9889.69 | -110.31 | buy /  / momentum_26 + reversion_12: prior completed bar target 100%; next bar open simulation |
| v1 | momentum_26 AND volume_26 | 10000.00 | 0.00 | 대기 /  / 새 신호 대기 |
| v1 | momentum_26 + volume_26 | 9941.28 | -58.72 | buy /  / momentum_26 + volume_26: prior completed bar target 50%; next bar open simulation |
| v1 | breakout_8 AND reversion_12 | 10000.00 | 0.00 | 대기 /  / 새 신호 대기 |
| v1 | breakout_8 + reversion_12 | 9947.99 | -52.01 | sell /  / breakout_8 + reversion_12: prior completed bar target 50%; next bar open simulation |
| v1 | breakout_8 AND volume_26 | 10000.00 | 0.00 | 대기 /  / 새 신호 대기 |
| v1 | breakout_8 + volume_26 | 10000.00 | 0.00 | 대기 /  / 새 신호 대기 |
| v1 | reversion_12 AND volume_26 | 10000.00 | 0.00 | 대기 /  / 새 신호 대기 |
| v1 | reversion_12 + volume_26 | 9947.99 | -52.01 | sell /  / reversion_12 + volume_26: prior completed bar target 50%; next bar open simulation |
| v2 | cash | 10000.00 | 0.00 | 대기 /  / 새 신호 대기 |
| v2 | buy_hold | 10569.81 | 569.81 | buy / partial / 직전 완료 봉 목표 비중 100%; 다음 봉 시가 가정 |
| v2 | trend_8_26 | 10410.62 | 410.62 | sell / filled / 직전 완료 봉 목표 비중 0%; 다음 봉 시가 가정 |
| v2 | momentum_26 | 10396.08 | 396.08 | buy / partial / 직전 완료 봉 목표 비중 100%; 다음 봉 시가 가정 |
| v2 | breakout_8 | 9964.65 | -35.35 | sell / filled / 직전 완료 봉 목표 비중 0%; 다음 봉 시가 가정 |
| v2 | reversion_12 | 9913.46 | -86.54 | buy / partial / 직전 완료 봉 목표 비중 100%; 다음 봉 시가 가정 |
| v2 | volume_26 | 9965.28 | -34.72 | sell / filled / 직전 완료 봉 목표 비중 0%; 다음 봉 시가 가정 |
| v2 | trend_8_26 AND momentum_26 | 10410.62 | 410.62 | sell / filled / 직전 완료 봉 목표 비중 0%; 다음 봉 시가 가정 |
| v2 | trend_8_26 + momentum_26 | 10403.34 | 403.34 | sell / filled / 직전 완료 봉 목표 비중 50%; 다음 봉 시가 가정 |
| v2 | trend_8_26 AND breakout_8 | 10088.55 | 88.55 | sell / filled / 직전 완료 봉 목표 비중 0%; 다음 봉 시가 가정 |
| v2 | trend_8_26 + breakout_8 | 10185.61 | 185.61 | sell / filled / 직전 완료 봉 목표 비중 0%; 다음 봉 시가 가정 |
| v2 | trend_8_26 AND reversion_12 | 9808.74 | -191.26 | sell / filled / 직전 완료 봉 목표 비중 0%; 다음 봉 시가 가정 |
| v2 | trend_8_26 + reversion_12 | 10160.50 | 160.50 | sell / filled / 직전 완료 봉 목표 비중 50%; 다음 봉 시가 가정 |
| v2 | trend_8_26 AND volume_26 | 9949.23 | -50.77 | sell / filled / 직전 완료 봉 목표 비중 0%; 다음 봉 시가 가정 |
| v2 | trend_8_26 + volume_26 | 10186.98 | 186.98 | sell / filled / 직전 완료 봉 목표 비중 0%; 다음 봉 시가 가정 |
| v2 | momentum_26 AND breakout_8 | 9964.65 | -35.35 | sell / filled / 직전 완료 봉 목표 비중 0%; 다음 봉 시가 가정 |
| v2 | momentum_26 + breakout_8 | 10178.52 | 178.52 | buy / filled / 직전 완료 봉 목표 비중 50%; 다음 봉 시가 가정 |
| v2 | momentum_26 AND reversion_12 | 9832.77 | -167.23 | buy / partial / 직전 완료 봉 목표 비중 100%; 다음 봉 시가 가정 |
| v2 | momentum_26 + reversion_12 | 10196.14 | 196.14 | buy / partial / 직전 완료 봉 목표 비중 100%; 다음 봉 시가 가정 |
| v2 | momentum_26 AND volume_26 | 9913.82 | -86.18 | sell / filled / 직전 완료 봉 목표 비중 0%; 다음 봉 시가 가정 |
| v2 | momentum_26 + volume_26 | 10179.95 | 179.95 | buy / filled / 직전 완료 봉 목표 비중 50%; 다음 봉 시가 가정 |
| v2 | breakout_8 AND reversion_12 | 10000.00 | 0.00 | 대기 /  / 새 신호 대기 |
| v2 | breakout_8 + reversion_12 | 9961.13 | -38.87 | sell / filled / 직전 완료 봉 목표 비중 50%; 다음 봉 시가 가정 |
| v2 | breakout_8 AND volume_26 | 9950.23 | -49.77 | sell / filled / 직전 완료 봉 목표 비중 0%; 다음 봉 시가 가정 |
| v2 | breakout_8 + volume_26 | 9966.35 | -33.65 | sell / filled / 직전 완료 봉 목표 비중 0%; 다음 봉 시가 가정 |
| v2 | reversion_12 AND volume_26 | 10009.78 | 9.78 | sell / filled / 직전 완료 봉 목표 비중 0%; 다음 봉 시가 가정 |
| v2 | reversion_12 + volume_26 | 9939.28 | -60.72 | sell / filled / 직전 완료 봉 목표 비중 50%; 다음 봉 시가 가정 |

### 같은 기간의 비용·노출 비교 (사후 연구)

| 전략 | 비용 전 | 비용 후 | 100% 보유 | 같은 평균 노출 보유 | 평균 노출 |
|---|---:|---:|---:|---:|---:|
| cash | 0.00% | 0.00% | 9.58% | 0.00% | 0.00% |
| buy_hold | 10.04% | 9.58% | 9.58% | 9.58% | 100.00% |
| trend_8_26 | 9.34% | 6.62% | 9.58% | 6.53% | 68.41% |
| momentum_26 | 6.49% | 2.54% | 9.58% | 6.50% | 68.15% |
| breakout_8 | 5.52% | -11.92% | 9.58% | 2.53% | 26.63% |
| reversion_12 | 2.88% | -6.99% | 9.58% | 1.58% | 16.71% |
| volume_26 | -0.57% | -5.85% | 9.58% | 0.52% | 5.48% |
| trend_8_26 AND momentum_26 | 8.87% | 4.83% | 9.58% | 5.97% | 62.66% |
| trend_8_26 + momentum_26 | 7.92% | 4.57% | 9.58% | 6.51% | 68.28% |
| trend_8_26 AND breakout_8 | 6.92% | -6.91% | 9.58% | 2.10% | 22.19% |
| trend_8_26 + breakout_8 | 7.43% | -2.87% | 9.58% | 4.52% | 47.53% |
| trend_8_26 AND reversion_12 | 0.42% | -4.91% | 9.58% | 0.64% | 6.79% |
| trend_8_26 + reversion_12 | 6.10% | -0.20% | 9.58% | 4.05% | 42.56% |
| trend_8_26 AND volume_26 | 1.13% | -1.39% | 9.58% | 0.20% | 2.09% |
| trend_8_26 + volume_26 | 4.31% | 0.62% | 9.58% | 3.51% | 36.95% |
| momentum_26 AND breakout_8 | 5.58% | -8.47% | 9.58% | 2.20% | 23.24% |
| momentum_26 + breakout_8 | 6.02% | -4.75% | 9.58% | 4.51% | 47.40% |
| momentum_26 AND reversion_12 | 0.32% | -5.01% | 9.58% | 0.64% | 6.79% |
| momentum_26 + reversion_12 | 4.71% | -0.46% | 9.58% | 4.03% | 42.43% |
| momentum_26 AND volume_26 | 0.44% | -3.69% | 9.58% | 0.27% | 2.87% |
| momentum_26 + volume_26 | 2.94% | -1.73% | 9.58% | 3.50% | 36.82% |
| breakout_8 AND reversion_12 | 0.00% | 0.00% | 9.58% | 0.00% | 0.00% |
| breakout_8 + reversion_12 | 4.22% | -9.10% | 9.58% | 2.05% | 21.68% |
| breakout_8 AND volume_26 | 0.91% | -1.19% | 9.58% | 0.15% | 1.57% |
| breakout_8 + volume_26 | 2.46% | -8.15% | 9.58% | 1.52% | 16.06% |
| reversion_12 AND volume_26 | -0.51% | -2.99% | 9.58% | 0.22% | 2.35% |
| reversion_12 + volume_26 | 1.15% | -6.23% | 9.58% | 1.05% | 11.10% |

동일 구간·초기 자금, 종료 시 청산 비용 포함. 노출 맞춤은 사후 설명용이며 v2 실제 계좌 성과가 아닙니다.
[낙폭 분해·비용 영향·전체 구간](WMT/comparison.json)

[v1 전체 기록](WMT/accounts.json) · [v2 전체 기록](WMT/accounts-v2.json)
