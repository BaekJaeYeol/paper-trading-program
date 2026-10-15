# 모의투자 운영 현황

최근 확인: 2026-10-15T17:52:00.562525+00:00 (UTC)
다음 15분 확인 목표 (세션 실행 중에만 적용): 2026-10-15T18:07:00+00:00 (UTC, 실행 지연 가능)

실제 주문 없음. v1 기존 계좌와 v2 새 계좌의 시작일이 다르므로 수익률을 직접 우열 비교하지 마세요.
v2는 다음 봉 시가에 비용·스프레드·직전 거래량 제한을 적용한 가상 체결입니다. 미체결 잔량은 만료됩니다.

| 종목 | 상태 | 최근 성공 UTC | 마지막 완료 봉 UTC | 이번 새 봉 |
|---|---|---|---|---|
| SPY | updated | 2026-10-15T17:52:00.562525+00:00 | 2026-10-15T17:30:00+00:00 | 1 |
| QQQ | updated | 2026-10-15T17:52:00.562525+00:00 | 2026-10-15T17:30:00+00:00 | 1 |
| IWM | updated | 2026-10-15T17:52:00.562525+00:00 | 2026-10-15T17:30:00+00:00 | 1 |
| DIA | updated | 2026-10-15T17:52:00.562525+00:00 | 2026-10-15T17:30:00+00:00 | 1 |
| MSFT | updated | 2026-10-15T17:52:00.562525+00:00 | 2026-10-15T17:30:00+00:00 | 1 |
| JPM | updated | 2026-10-15T17:52:00.562525+00:00 | 2026-10-15T17:30:00+00:00 | 1 |
| XOM | updated | 2026-10-15T17:52:00.562525+00:00 | 2026-10-15T17:30:00+00:00 | 1 |
| JNJ | updated | 2026-10-15T17:52:00.562525+00:00 | 2026-10-15T17:30:00+00:00 | 1 |
| CAT | updated | 2026-10-15T17:52:00.562525+00:00 | 2026-10-15T17:30:00+00:00 | 1 |
| WMT | updated | 2026-10-15T17:52:00.562525+00:00 | 2026-10-15T17:30:00+00:00 | 1 |

이번 실행 소요: 67.56초
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
| v1 | buy_hold | 9994.67 | -5.33 | buy /  / buy_hold: prior completed bar target 100%; next bar open simulation |
| v1 | trend_8_26 | 9993.60 | -6.40 | buy /  / trend_8_26: prior completed bar target 100%; next bar open simulation |
| v1 | momentum_26 | 9951.80 | -48.20 | buy /  / momentum_26: prior completed bar target 100%; next bar open simulation |
| v1 | breakout_8 | 10000.00 | 0.00 | 대기 /  / 새 신호 대기 |
| v1 | reversion_12 | 10000.00 | 0.00 | 대기 /  / 새 신호 대기 |
| v1 | volume_26 | 9949.83 | -50.17 | sell /  / volume_26: prior completed bar target 0%; next bar open simulation |
| v1 | trend_8_26 AND momentum_26 | 9951.80 | -48.20 | buy /  / trend_8_26 AND momentum_26: prior completed bar target 100%; next bar open simulation |
| v1 | trend_8_26 + momentum_26 | 9972.67 | -27.33 | buy /  / trend_8_26 + momentum_26: prior completed bar target 100%; next bar open simulation |
| v1 | trend_8_26 AND breakout_8 | 10000.00 | 0.00 | 대기 /  / 새 신호 대기 |
| v1 | trend_8_26 + breakout_8 | 9996.77 | -3.23 | sell /  / trend_8_26 + breakout_8: prior completed bar target 50%; next bar open simulation |
| v1 | trend_8_26 AND reversion_12 | 10000.00 | 0.00 | 대기 /  / 새 신호 대기 |
| v1 | trend_8_26 + reversion_12 | 9996.77 | -3.23 | sell /  / trend_8_26 + reversion_12: prior completed bar target 50%; next bar open simulation |
| v1 | trend_8_26 AND volume_26 | 9949.83 | -50.17 | sell /  / trend_8_26 AND volume_26: prior completed bar target 0%; next bar open simulation |
| v1 | trend_8_26 + volume_26 | 9971.68 | -28.32 | sell /  / trend_8_26 + volume_26: prior completed bar target 50%; next bar open simulation |
| v1 | momentum_26 AND breakout_8 | 10000.00 | 0.00 | 대기 /  / 새 신호 대기 |
| v1 | momentum_26 + breakout_8 | 9975.83 | -24.17 | sell /  / momentum_26 + breakout_8: prior completed bar target 50%; next bar open simulation |
| v1 | momentum_26 AND reversion_12 | 10000.00 | 0.00 | 대기 /  / 새 신호 대기 |
| v1 | momentum_26 + reversion_12 | 9975.83 | -24.17 | sell /  / momentum_26 + reversion_12: prior completed bar target 50%; next bar open simulation |
| v1 | momentum_26 AND volume_26 | 10000.00 | 0.00 | 대기 /  / 새 신호 대기 |
| v1 | momentum_26 + volume_26 | 9970.70 | -29.30 | sell /  / momentum_26 + volume_26: prior completed bar target 50%; next bar open simulation |
| v1 | breakout_8 AND reversion_12 | 10000.00 | 0.00 | 대기 /  / 새 신호 대기 |
| v1 | breakout_8 + reversion_12 | 10000.00 | 0.00 | 대기 /  / 새 신호 대기 |
| v1 | breakout_8 AND volume_26 | 10000.00 | 0.00 | 대기 /  / 새 신호 대기 |
| v1 | breakout_8 + volume_26 | 9974.87 | -25.13 | sell /  / breakout_8 + volume_26: prior completed bar target 0%; next bar open simulation |
| v1 | reversion_12 AND volume_26 | 10000.00 | 0.00 | 대기 /  / 새 신호 대기 |
| v1 | reversion_12 + volume_26 | 9974.87 | -25.13 | sell /  / reversion_12 + volume_26: prior completed bar target 0%; next bar open simulation |
| v2 | cash | 10000.00 | 0.00 | 대기 /  / 새 신호 대기 |
| v2 | buy_hold | 9885.11 | -114.89 | buy / partial / 직전 완료 봉 목표 비중 100%; 다음 봉 시가 가정 |
| v2 | trend_8_26 | 9840.93 | -159.07 | buy / partial / 직전 완료 봉 목표 비중 100%; 다음 봉 시가 가정 |
| v2 | momentum_26 | 9811.39 | -188.61 | buy / partial / 직전 완료 봉 목표 비중 100%; 다음 봉 시가 가정 |
| v2 | breakout_8 | 9684.78 | -315.22 | sell / filled / 직전 완료 봉 목표 비중 0%; 다음 봉 시가 가정 |
| v2 | reversion_12 | 9535.84 | -464.16 | sell / filled / 직전 완료 봉 목표 비중 0%; 다음 봉 시가 가정 |
| v2 | volume_26 | 9441.45 | -558.55 | sell / filled / 직전 완료 봉 목표 비중 0%; 다음 봉 시가 가정 |
| v2 | trend_8_26 AND momentum_26 | 9818.08 | -181.92 | buy / partial / 직전 완료 봉 목표 비중 100%; 다음 봉 시가 가정 |
| v2 | trend_8_26 + momentum_26 | 9826.17 | -173.83 | buy / partial / 직전 완료 봉 목표 비중 100%; 다음 봉 시가 가정 |
| v2 | trend_8_26 AND breakout_8 | 9913.42 | -86.58 | sell / filled / 직전 완료 봉 목표 비중 0%; 다음 봉 시가 가정 |
| v2 | trend_8_26 + breakout_8 | 9762.40 | -237.60 | sell / filled / 직전 완료 봉 목표 비중 50%; 다음 봉 시가 가정 |
| v2 | trend_8_26 AND reversion_12 | 9896.11 | -103.89 | sell / filled / 직전 완료 봉 목표 비중 0%; 다음 봉 시가 가정 |
| v2 | trend_8_26 + reversion_12 | 9686.89 | -313.11 | sell / filled / 직전 완료 봉 목표 비중 50%; 다음 봉 시가 가정 |
| v2 | trend_8_26 AND volume_26 | 9845.91 | -154.09 | sell / filled / 직전 완료 봉 목표 비중 0%; 다음 봉 시가 가정 |
| v2 | trend_8_26 + volume_26 | 9659.17 | -340.83 | sell / filled / 직전 완료 봉 목표 비중 50%; 다음 봉 시가 가정 |
| v2 | momentum_26 AND breakout_8 | 9871.37 | -128.63 | sell / filled / 직전 완료 봉 목표 비중 0%; 다음 봉 시가 가정 |
| v2 | momentum_26 + breakout_8 | 9747.77 | -252.23 | sell / filled / 직전 완료 봉 목표 비중 50%; 다음 봉 시가 가정 |
| v2 | momentum_26 AND reversion_12 | 9963.21 | -36.79 | sell / filled / 직전 완료 봉 목표 비중 0%; 다음 봉 시가 가정 |
| v2 | momentum_26 + reversion_12 | 9692.69 | -307.31 | sell / filled / 직전 완료 봉 목표 비중 50%; 다음 봉 시가 가정 |
| v2 | momentum_26 AND volume_26 | 9917.25 | -82.75 | sell / filled / 직전 완료 봉 목표 비중 0%; 다음 봉 시가 가정 |
| v2 | momentum_26 + volume_26 | 9685.23 | -314.77 | sell / filled / 직전 완료 봉 목표 비중 50%; 다음 봉 시가 가정 |
| v2 | breakout_8 AND reversion_12 | 10000.00 | 0.00 | 대기 /  / 새 신호 대기 |
| v2 | breakout_8 + reversion_12 | 9650.09 | -349.91 | sell / filled / 직전 완료 봉 목표 비중 0%; 다음 봉 시가 가정 |
| v2 | breakout_8 AND volume_26 | 9933.18 | -66.82 | sell / filled / 직전 완료 봉 목표 비중 0%; 다음 봉 시가 가정 |
| v2 | breakout_8 + volume_26 | 9602.28 | -397.72 | sell / filled / 직전 완료 봉 목표 비중 0%; 다음 봉 시가 가정 |
| v2 | reversion_12 AND volume_26 | 9743.33 | -256.67 | sell / filled / 직전 완료 봉 목표 비중 0%; 다음 봉 시가 가정 |
| v2 | reversion_12 + volume_26 | 9568.30 | -431.70 | sell / filled / 직전 완료 봉 목표 비중 0%; 다음 봉 시가 가정 |

### 같은 기간의 비용·노출 비교 (사후 연구)

| 전략 | 비용 전 | 비용 후 | 100% 보유 | 같은 평균 노출 보유 | 평균 노출 |
|---|---:|---:|---:|---:|---:|
| cash | 0.00% | 0.00% | -0.07% | -0.00% | 0.00% |
| buy_hold | 0.35% | -0.07% | -0.07% | -0.07% | 100.00% |
| trend_8_26 | 1.60% | -1.76% | -0.07% | -0.04% | 49.34% |
| momentum_26 | -0.45% | -4.94% | -0.07% | -0.04% | 48.82% |
| breakout_8 | -0.74% | -15.74% | -0.07% | -0.02% | 22.05% |
| reversion_12 | -1.86% | -12.74% | -0.07% | -0.02% | 27.82% |
| volume_26 | -0.54% | -9.32% | -0.07% | -0.01% | 8.66% |
| trend_8_26 AND momentum_26 | 0.88% | -2.86% | -0.07% | -0.03% | 42.52% |
| trend_8_26 + momentum_26 | 0.57% | -3.16% | -0.07% | -0.04% | 49.08% |
| trend_8_26 AND breakout_8 | -0.06% | -10.40% | -0.07% | -0.01% | 13.12% |
| trend_8_26 + breakout_8 | 0.42% | -9.02% | -0.07% | -0.03% | 35.70% |
| trend_8_26 AND reversion_12 | 0.10% | -4.01% | -0.07% | -0.00% | 6.04% |
| trend_8_26 + reversion_12 | -0.14% | -7.23% | -0.07% | -0.03% | 38.59% |
| trend_8_26 AND volume_26 | -0.17% | -4.27% | -0.07% | -0.00% | 3.94% |
| trend_8_26 + volume_26 | 0.53% | -5.62% | -0.07% | -0.02% | 29.01% |
| momentum_26 AND breakout_8 | 0.24% | -10.13% | -0.07% | -0.01% | 14.17% |
| momentum_26 + breakout_8 | -0.59% | -10.50% | -0.07% | -0.03% | 35.44% |
| momentum_26 AND reversion_12 | -0.88% | -5.75% | -0.07% | -0.00% | 6.82% |
| momentum_26 + reversion_12 | -1.15% | -8.36% | -0.07% | -0.03% | 38.33% |
| momentum_26 AND volume_26 | -0.22% | -3.11% | -0.07% | -0.00% | 2.10% |
| momentum_26 + volume_26 | -0.49% | -5.98% | -0.07% | -0.02% | 28.74% |
| breakout_8 AND reversion_12 | 0.00% | 0.00% | -0.07% | -0.00% | 0.00% |
| breakout_8 + reversion_12 | -1.30% | -13.72% | -0.07% | -0.02% | 24.94% |
| breakout_8 AND volume_26 | 0.05% | -1.61% | -0.07% | -0.00% | 1.31% |
| breakout_8 + volume_26 | -0.64% | -11.67% | -0.07% | -0.01% | 15.36% |
| reversion_12 AND volume_26 | -0.67% | -4.76% | -0.07% | -0.00% | 3.94% |
| reversion_12 + volume_26 | -1.20% | -10.68% | -0.07% | -0.01% | 18.25% |

동일 구간·초기 자금, 종료 시 청산 비용 포함. 노출 맞춤은 사후 설명용이며 v2 실제 계좌 성과가 아닙니다.
[낙폭 분해·비용 영향·전체 구간](SPY/comparison.json)

[v1 전체 기록](SPY/accounts.json) · [v2 전체 기록](SPY/accounts-v2.json)

## QQQ 계좌

| 모델 | 전략 | 평가액 USD | 손익 USD | 최근 매매·이유 |
|---|---|---:|---:|---|
| v1 | cash | 10000.00 | 0.00 | 대기 /  / 새 신호 대기 |
| v1 | buy_hold | 10003.31 | 3.31 | buy /  / buy_hold: prior completed bar target 100%; next bar open simulation |
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
| v2 | buy_hold | 9668.07 | -331.93 | buy / partial / 직전 완료 봉 목표 비중 100%; 다음 봉 시가 가정 |
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
| cash | 0.00% | 0.00% | -2.64% | -0.00% | 0.00% |
| buy_hold | -2.23% | -2.64% | -2.64% | -2.64% | 100.00% |
| trend_8_26 | 0.01% | -3.30% | -2.64% | -1.27% | 48.03% |
| momentum_26 | -1.39% | -5.44% | -2.64% | -1.13% | 42.78% |
| breakout_8 | -1.69% | -16.89% | -2.64% | -0.46% | 17.59% |
| reversion_12 | -0.86% | -12.96% | -2.64% | -0.70% | 26.51% |
| volume_26 | -1.07% | -13.51% | -2.64% | -0.37% | 14.17% |
| trend_8_26 AND momentum_26 | -0.42% | -3.71% | -2.64% | -1.01% | 38.32% |
| trend_8_26 + momentum_26 | -0.69% | -4.17% | -2.64% | -1.20% | 45.41% |
| trend_8_26 AND breakout_8 | -0.58% | -10.12% | -2.64% | -0.28% | 10.76% |
| trend_8_26 + breakout_8 | -0.84% | -9.98% | -2.64% | -0.87% | 32.81% |
| trend_8_26 AND reversion_12 | 0.42% | -5.31% | -2.64% | -0.16% | 6.04% |
| trend_8_26 + reversion_12 | -0.42% | -7.68% | -2.64% | -0.98% | 37.28% |
| trend_8_26 AND volume_26 | -0.71% | -5.59% | -2.64% | -0.11% | 4.20% |
| trend_8_26 + volume_26 | -0.53% | -8.36% | -2.64% | -0.82% | 31.11% |
| momentum_26 AND breakout_8 | -0.74% | -9.88% | -2.64% | -0.29% | 11.02% |
| momentum_26 + breakout_8 | -1.53% | -11.17% | -2.64% | -0.80% | 30.19% |
| momentum_26 AND reversion_12 | -0.02% | -5.73% | -2.64% | -0.12% | 4.72% |
| momentum_26 + reversion_12 | -1.11% | -8.71% | -2.64% | -0.91% | 34.65% |
| momentum_26 AND volume_26 | -0.30% | -4.40% | -2.64% | -0.09% | 3.41% |
| momentum_26 + volume_26 | -1.22% | -9.38% | -2.64% | -0.75% | 28.48% |
| breakout_8 AND reversion_12 | 0.00% | 0.00% | -2.64% | -0.00% | 0.00% |
| breakout_8 + reversion_12 | -1.27% | -14.06% | -2.64% | -0.58% | 22.06% |
| breakout_8 AND volume_26 | 0.04% | -2.04% | -2.64% | -0.03% | 1.31% |
| breakout_8 + volume_26 | -1.38% | -13.97% | -2.64% | -0.42% | 15.89% |
| reversion_12 AND volume_26 | -1.25% | -8.44% | -2.64% | -0.23% | 8.66% |
| reversion_12 + volume_26 | -0.96% | -12.88% | -2.64% | -0.54% | 20.35% |

동일 구간·초기 자금, 종료 시 청산 비용 포함. 노출 맞춤은 사후 설명용이며 v2 실제 계좌 성과가 아닙니다.
[낙폭 분해·비용 영향·전체 구간](QQQ/comparison.json)

[v1 전체 기록](QQQ/accounts.json) · [v2 전체 기록](QQQ/accounts-v2.json)

## IWM 계좌

| 모델 | 전략 | 평가액 USD | 손익 USD | 최근 매매·이유 |
|---|---|---:|---:|---|
| v1 | cash | 10000.00 | 0.00 | 대기 /  / 새 신호 대기 |
| v1 | buy_hold | 9973.12 | -26.88 | buy /  / buy_hold: prior completed bar target 100%; next bar open simulation |
| v1 | trend_8_26 | 9973.12 | -26.88 | buy /  / trend_8_26: prior completed bar target 100%; next bar open simulation |
| v1 | momentum_26 | 9973.12 | -26.88 | buy /  / momentum_26: prior completed bar target 100%; next bar open simulation |
| v1 | breakout_8 | 10000.00 | 0.00 | 대기 /  / 새 신호 대기 |
| v1 | reversion_12 | 10000.00 | 0.00 | 대기 /  / 새 신호 대기 |
| v1 | volume_26 | 10000.00 | 0.00 | 대기 /  / 새 신호 대기 |
| v1 | trend_8_26 AND momentum_26 | 9973.12 | -26.88 | buy /  / trend_8_26 AND momentum_26: prior completed bar target 100%; next bar open simulation |
| v1 | trend_8_26 + momentum_26 | 9973.12 | -26.88 | buy /  / trend_8_26 + momentum_26: prior completed bar target 100%; next bar open simulation |
| v1 | trend_8_26 AND breakout_8 | 10000.00 | 0.00 | 대기 /  / 새 신호 대기 |
| v1 | trend_8_26 + breakout_8 | 9986.52 | -13.48 | sell /  / trend_8_26 + breakout_8: prior completed bar target 50%; next bar open simulation |
| v1 | trend_8_26 AND reversion_12 | 10000.00 | 0.00 | 대기 /  / 새 신호 대기 |
| v1 | trend_8_26 + reversion_12 | 9986.52 | -13.48 | sell /  / trend_8_26 + reversion_12: prior completed bar target 50%; next bar open simulation |
| v1 | trend_8_26 AND volume_26 | 10000.00 | 0.00 | 대기 /  / 새 신호 대기 |
| v1 | trend_8_26 + volume_26 | 9986.52 | -13.48 | sell /  / trend_8_26 + volume_26: prior completed bar target 50%; next bar open simulation |
| v1 | momentum_26 AND breakout_8 | 10000.00 | 0.00 | 대기 /  / 새 신호 대기 |
| v1 | momentum_26 + breakout_8 | 9986.52 | -13.48 | sell /  / momentum_26 + breakout_8: prior completed bar target 50%; next bar open simulation |
| v1 | momentum_26 AND reversion_12 | 10000.00 | 0.00 | 대기 /  / 새 신호 대기 |
| v1 | momentum_26 + reversion_12 | 9986.52 | -13.48 | sell /  / momentum_26 + reversion_12: prior completed bar target 50%; next bar open simulation |
| v1 | momentum_26 AND volume_26 | 10000.00 | 0.00 | 대기 /  / 새 신호 대기 |
| v1 | momentum_26 + volume_26 | 9986.52 | -13.48 | sell /  / momentum_26 + volume_26: prior completed bar target 50%; next bar open simulation |
| v1 | breakout_8 AND reversion_12 | 10000.00 | 0.00 | 대기 /  / 새 신호 대기 |
| v1 | breakout_8 + reversion_12 | 10000.00 | 0.00 | 대기 /  / 새 신호 대기 |
| v1 | breakout_8 AND volume_26 | 10000.00 | 0.00 | 대기 /  / 새 신호 대기 |
| v1 | breakout_8 + volume_26 | 10000.00 | 0.00 | 대기 /  / 새 신호 대기 |
| v1 | reversion_12 AND volume_26 | 10000.00 | 0.00 | 대기 /  / 새 신호 대기 |
| v1 | reversion_12 + volume_26 | 10000.00 | 0.00 | 대기 /  / 새 신호 대기 |
| v2 | cash | 10000.00 | 0.00 | 대기 /  / 새 신호 대기 |
| v2 | buy_hold | 9808.12 | -191.88 | buy / partial / 직전 완료 봉 목표 비중 100%; 다음 봉 시가 가정 |
| v2 | trend_8_26 | 9785.66 | -214.34 | buy / partial / 직전 완료 봉 목표 비중 100%; 다음 봉 시가 가정 |
| v2 | momentum_26 | 9786.66 | -213.34 | buy / partial / 직전 완료 봉 목표 비중 100%; 다음 봉 시가 가정 |
| v2 | breakout_8 | 9666.31 | -333.69 | sell / filled / 직전 완료 봉 목표 비중 0%; 다음 봉 시가 가정 |
| v2 | reversion_12 | 9538.67 | -461.33 | sell / filled / 직전 완료 봉 목표 비중 0%; 다음 봉 시가 가정 |
| v2 | volume_26 | 9513.36 | -486.64 | sell / filled / 직전 완료 봉 목표 비중 0%; 다음 봉 시가 가정 |
| v2 | trend_8_26 AND momentum_26 | 9937.55 | -62.45 | buy / partial / 직전 완료 봉 목표 비중 100%; 다음 봉 시가 가정 |
| v2 | trend_8_26 + momentum_26 | 9806.87 | -193.13 | buy / partial / 직전 완료 봉 목표 비중 100%; 다음 봉 시가 가정 |
| v2 | trend_8_26 AND breakout_8 | 9962.82 | -37.18 | sell / filled / 직전 완료 봉 목표 비중 0%; 다음 봉 시가 가정 |
| v2 | trend_8_26 + breakout_8 | 9746.34 | -253.66 | sell / filled / 직전 완료 봉 목표 비중 50%; 다음 봉 시가 가정 |
| v2 | trend_8_26 AND reversion_12 | 9881.82 | -118.18 | sell / filled / 직전 완료 봉 목표 비중 0%; 다음 봉 시가 가정 |
| v2 | trend_8_26 + reversion_12 | 9661.23 | -338.77 | sell / filled / 직전 완료 봉 목표 비중 50%; 다음 봉 시가 가정 |
| v2 | trend_8_26 AND volume_26 | 9862.83 | -137.17 | sell / filled / 직전 완료 봉 목표 비중 0%; 다음 봉 시가 가정 |
| v2 | trend_8_26 + volume_26 | 9668.84 | -331.16 | sell / filled / 직전 완료 봉 목표 비중 50%; 다음 봉 시가 가정 |
| v2 | momentum_26 AND breakout_8 | 9854.44 | -145.56 | sell / filled / 직전 완료 봉 목표 비중 0%; 다음 봉 시가 가정 |
| v2 | momentum_26 + breakout_8 | 9726.28 | -273.72 | sell / filled / 직전 완료 봉 목표 비중 50%; 다음 봉 시가 가정 |
| v2 | momentum_26 AND reversion_12 | 9960.59 | -39.41 | sell / filled / 직전 완료 봉 목표 비중 0%; 다음 봉 시가 가정 |
| v2 | momentum_26 + reversion_12 | 9681.82 | -318.18 | sell / filled / 직전 완료 봉 목표 비중 50%; 다음 봉 시가 가정 |
| v2 | momentum_26 AND volume_26 | 9897.79 | -102.21 | sell / filled / 직전 완료 봉 목표 비중 0%; 다음 봉 시가 가정 |
| v2 | momentum_26 + volume_26 | 9648.85 | -351.15 | sell / filled / 직전 완료 봉 목표 비중 50%; 다음 봉 시가 가정 |
| v2 | breakout_8 AND reversion_12 | 10000.00 | 0.00 | 대기 /  / 새 신호 대기 |
| v2 | breakout_8 + reversion_12 | 9642.35 | -357.65 | sell / filled / 직전 완료 봉 목표 비중 0%; 다음 봉 시가 가정 |
| v2 | breakout_8 AND volume_26 | 9746.03 | -253.97 | sell / filled / 직전 완료 봉 목표 비중 0%; 다음 봉 시가 가정 |
| v2 | breakout_8 + volume_26 | 9609.68 | -390.32 | sell / filled / 직전 완료 봉 목표 비중 0%; 다음 봉 시가 가정 |
| v2 | reversion_12 AND volume_26 | 9740.75 | -259.25 | sell / filled / 직전 완료 봉 목표 비중 0%; 다음 봉 시가 가정 |
| v2 | reversion_12 + volume_26 | 9545.82 | -454.18 | sell / filled / 직전 완료 봉 목표 비중 0%; 다음 봉 시가 가정 |

### 같은 기간의 비용·노출 비교 (사후 연구)

| 전략 | 비용 전 | 비용 후 | 100% 보유 | 같은 평균 노출 보유 | 평균 노출 |
|---|---:|---:|---:|---:|---:|
| cash | 0.00% | 0.00% | -3.47% | -0.00% | 0.00% |
| buy_hold | -3.06% | -3.47% | -3.47% | -3.47% | 100.00% |
| trend_8_26 | -2.49% | -6.50% | -3.47% | -1.57% | 44.88% |
| momentum_26 | -2.94% | -8.48% | -3.47% | -1.40% | 40.16% |
| breakout_8 | -0.83% | -13.67% | -3.47% | -0.64% | 18.37% |
| reversion_12 | -2.15% | -14.82% | -3.47% | -1.05% | 29.92% |
| volume_26 | -2.34% | -9.45% | -3.47% | -0.30% | 8.66% |
| trend_8_26 AND momentum_26 | -2.60% | -7.00% | -3.47% | -1.21% | 34.65% |
| trend_8_26 + momentum_26 | -2.71% | -7.10% | -3.47% | -1.49% | 42.52% |
| trend_8_26 AND breakout_8 | -0.70% | -7.93% | -3.47% | -0.35% | 9.97% |
| trend_8_26 + breakout_8 | -1.66% | -9.97% | -3.47% | -1.11% | 31.63% |
| trend_8_26 AND reversion_12 | -0.12% | -5.03% | -3.47% | -0.21% | 6.04% |
| trend_8_26 + reversion_12 | -2.31% | -10.58% | -3.47% | -1.31% | 37.41% |
| trend_8_26 AND volume_26 | -1.05% | -4.72% | -3.47% | -0.13% | 3.67% |
| trend_8_26 + volume_26 | -2.41% | -7.80% | -3.47% | -0.94% | 26.77% |
| momentum_26 AND breakout_8 | -0.10% | -7.37% | -3.47% | -0.34% | 9.71% |
| momentum_26 + breakout_8 | -1.89% | -11.11% | -3.47% | -1.03% | 29.27% |
| momentum_26 AND reversion_12 | -0.05% | -3.76% | -3.47% | -0.12% | 3.41% |
| momentum_26 + reversion_12 | -2.54% | -10.60% | -3.47% | -1.23% | 35.05% |
| momentum_26 AND volume_26 | -1.34% | -4.20% | -3.47% | -0.07% | 2.10% |
| momentum_26 + volume_26 | -2.64% | -8.59% | -3.47% | -0.86% | 24.41% |
| breakout_8 AND reversion_12 | 0.00% | 0.00% | -3.47% | -0.00% | 0.00% |
| breakout_8 + reversion_12 | -1.49% | -13.53% | -3.47% | -0.85% | 24.16% |
| breakout_8 AND volume_26 | -1.33% | -4.19% | -3.47% | -0.08% | 2.36% |
| breakout_8 + volume_26 | -1.59% | -11.40% | -3.47% | -0.47% | 13.52% |
| reversion_12 AND volume_26 | -0.38% | -4.47% | -3.47% | -0.16% | 4.46% |
| reversion_12 + volume_26 | -2.24% | -11.63% | -3.47% | -0.68% | 19.30% |

동일 구간·초기 자금, 종료 시 청산 비용 포함. 노출 맞춤은 사후 설명용이며 v2 실제 계좌 성과가 아닙니다.
[낙폭 분해·비용 영향·전체 구간](IWM/comparison.json)

[v1 전체 기록](IWM/accounts.json) · [v2 전체 기록](IWM/accounts-v2.json)

## DIA 계좌

| 모델 | 전략 | 평가액 USD | 손익 USD | 최근 매매·이유 |
|---|---|---:|---:|---|
| v1 | cash | 10000.00 | 0.00 | 대기 /  / 새 신호 대기 |
| v1 | buy_hold | 9981.75 | -18.25 | buy /  / buy_hold: prior completed bar target 100%; next bar open simulation |
| v1 | trend_8_26 | 9981.75 | -18.25 | buy /  / trend_8_26: prior completed bar target 100%; next bar open simulation |
| v1 | momentum_26 | 9981.75 | -18.25 | buy /  / momentum_26: prior completed bar target 100%; next bar open simulation |
| v1 | breakout_8 | 10000.00 | 0.00 | 대기 /  / 새 신호 대기 |
| v1 | reversion_12 | 10000.00 | 0.00 | 대기 /  / 새 신호 대기 |
| v1 | volume_26 | 10000.00 | 0.00 | 대기 /  / 새 신호 대기 |
| v1 | trend_8_26 AND momentum_26 | 9981.75 | -18.25 | buy /  / trend_8_26 AND momentum_26: prior completed bar target 100%; next bar open simulation |
| v1 | trend_8_26 + momentum_26 | 9981.75 | -18.25 | buy /  / trend_8_26 + momentum_26: prior completed bar target 100%; next bar open simulation |
| v1 | trend_8_26 AND breakout_8 | 10000.00 | 0.00 | 대기 /  / 새 신호 대기 |
| v1 | trend_8_26 + breakout_8 | 9990.83 | -9.17 | sell /  / trend_8_26 + breakout_8: prior completed bar target 50%; next bar open simulation |
| v1 | trend_8_26 AND reversion_12 | 10000.00 | 0.00 | 대기 /  / 새 신호 대기 |
| v1 | trend_8_26 + reversion_12 | 9990.83 | -9.17 | sell /  / trend_8_26 + reversion_12: prior completed bar target 50%; next bar open simulation |
| v1 | trend_8_26 AND volume_26 | 10000.00 | 0.00 | 대기 /  / 새 신호 대기 |
| v1 | trend_8_26 + volume_26 | 9990.83 | -9.17 | sell /  / trend_8_26 + volume_26: prior completed bar target 50%; next bar open simulation |
| v1 | momentum_26 AND breakout_8 | 10000.00 | 0.00 | 대기 /  / 새 신호 대기 |
| v1 | momentum_26 + breakout_8 | 9990.83 | -9.17 | sell /  / momentum_26 + breakout_8: prior completed bar target 50%; next bar open simulation |
| v1 | momentum_26 AND reversion_12 | 10000.00 | 0.00 | 대기 /  / 새 신호 대기 |
| v1 | momentum_26 + reversion_12 | 9990.83 | -9.17 | sell /  / momentum_26 + reversion_12: prior completed bar target 50%; next bar open simulation |
| v1 | momentum_26 AND volume_26 | 10000.00 | 0.00 | 대기 /  / 새 신호 대기 |
| v1 | momentum_26 + volume_26 | 9990.83 | -9.17 | sell /  / momentum_26 + volume_26: prior completed bar target 50%; next bar open simulation |
| v1 | breakout_8 AND reversion_12 | 10000.00 | 0.00 | 대기 /  / 새 신호 대기 |
| v1 | breakout_8 + reversion_12 | 10000.00 | 0.00 | 대기 /  / 새 신호 대기 |
| v1 | breakout_8 AND volume_26 | 10000.00 | 0.00 | 대기 /  / 새 신호 대기 |
| v1 | breakout_8 + volume_26 | 10000.00 | 0.00 | 대기 /  / 새 신호 대기 |
| v1 | reversion_12 AND volume_26 | 10000.00 | 0.00 | 대기 /  / 새 신호 대기 |
| v1 | reversion_12 + volume_26 | 10000.00 | 0.00 | 대기 /  / 새 신호 대기 |
| v2 | cash | 10000.00 | 0.00 | 대기 /  / 새 신호 대기 |
| v2 | buy_hold | 10065.02 | 65.02 | buy / partial / 직전 완료 봉 목표 비중 100%; 다음 봉 시가 가정 |
| v2 | trend_8_26 | 9877.45 | -122.55 | buy / partial / 직전 완료 봉 목표 비중 100%; 다음 봉 시가 가정 |
| v2 | momentum_26 | 9986.05 | -13.95 | buy / partial / 직전 완료 봉 목표 비중 100%; 다음 봉 시가 가정 |
| v2 | breakout_8 | 9626.51 | -373.49 | sell / filled / 직전 완료 봉 목표 비중 0%; 다음 봉 시가 가정 |
| v2 | reversion_12 | 9698.03 | -301.97 | sell / filled / 직전 완료 봉 목표 비중 0%; 다음 봉 시가 가정 |
| v2 | volume_26 | 9718.21 | -281.79 | sell / filled / 직전 완료 봉 목표 비중 0%; 다음 봉 시가 가정 |
| v2 | trend_8_26 AND momentum_26 | 9981.42 | -18.58 | buy / partial / 직전 완료 봉 목표 비중 100%; 다음 봉 시가 가정 |
| v2 | trend_8_26 + momentum_26 | 9931.67 | -68.33 | buy / partial / 직전 완료 봉 목표 비중 100%; 다음 봉 시가 가정 |
| v2 | trend_8_26 AND breakout_8 | 9789.40 | -210.60 | sell / filled / 직전 완료 봉 목표 비중 0%; 다음 봉 시가 가정 |
| v2 | trend_8_26 + breakout_8 | 9751.18 | -248.82 | sell / filled / 직전 완료 봉 목표 비중 50%; 다음 봉 시가 가정 |
| v2 | trend_8_26 AND reversion_12 | 9810.77 | -189.23 | sell / filled / 직전 완료 봉 목표 비중 0%; 다음 봉 시가 가정 |
| v2 | trend_8_26 + reversion_12 | 9787.10 | -212.90 | sell / filled / 직전 완료 봉 목표 비중 50%; 다음 봉 시가 가정 |
| v2 | trend_8_26 AND volume_26 | 9858.88 | -141.12 | sell / filled / 직전 완료 봉 목표 비중 0%; 다음 봉 시가 가정 |
| v2 | trend_8_26 + volume_26 | 9818.07 | -181.93 | sell / filled / 직전 완료 봉 목표 비중 50%; 다음 봉 시가 가정 |
| v2 | momentum_26 AND breakout_8 | 9778.26 | -221.74 | sell / filled / 직전 완료 봉 목표 비중 0%; 다음 봉 시가 가정 |
| v2 | momentum_26 + breakout_8 | 9804.71 | -195.29 | sell / filled / 직전 완료 봉 목표 비중 50%; 다음 봉 시가 가정 |
| v2 | momentum_26 AND reversion_12 | 9955.97 | -44.03 | sell / filled / 직전 완료 봉 목표 비중 0%; 다음 봉 시가 가정 |
| v2 | momentum_26 + reversion_12 | 9840.83 | -159.17 | sell / filled / 직전 완료 봉 목표 비중 50%; 다음 봉 시가 가정 |
| v2 | momentum_26 AND volume_26 | 9791.42 | -208.58 | sell / filled / 직전 완료 봉 목표 비중 0%; 다음 봉 시가 가정 |
| v2 | momentum_26 + volume_26 | 9892.78 | -107.22 | sell / filled / 직전 완료 봉 목표 비중 50%; 다음 봉 시가 가정 |
| v2 | breakout_8 AND reversion_12 | 10000.00 | 0.00 | 대기 /  / 새 신호 대기 |
| v2 | breakout_8 + reversion_12 | 9661.83 | -338.17 | sell / filled / 직전 완료 봉 목표 비중 0%; 다음 봉 시가 가정 |
| v2 | breakout_8 AND volume_26 | 9796.56 | -203.44 | sell / filled / 직전 완료 봉 목표 비중 0%; 다음 봉 시가 가정 |
| v2 | breakout_8 + volume_26 | 9672.16 | -327.84 | sell / filled / 직전 완료 봉 목표 비중 0%; 다음 봉 시가 가정 |
| v2 | reversion_12 AND volume_26 | 10000.00 | 0.00 | 대기 /  / 새 신호 대기 |
| v2 | reversion_12 + volume_26 | 9707.85 | -292.15 | sell / filled / 직전 완료 봉 목표 비중 0%; 다음 봉 시가 가정 |

### 같은 기간의 비용·노출 비교 (사후 연구)

| 전략 | 비용 전 | 비용 후 | 100% 보유 | 같은 평균 노출 보유 | 평균 노출 |
|---|---:|---:|---:|---:|---:|
| cash | 0.00% | 0.00% | 0.91% | 0.00% | 0.00% |
| buy_hold | 1.34% | 0.91% | 0.91% | 0.91% | 100.00% |
| trend_8_26 | 1.65% | -2.94% | 0.91% | 0.51% | 56.17% |
| momentum_26 | 0.19% | -3.94% | 0.91% | 0.48% | 52.23% |
| breakout_8 | 0.14% | -16.40% | 0.91% | 0.21% | 23.36% |
| reversion_12 | -1.36% | -9.30% | 0.91% | 0.23% | 24.67% |
| volume_26 | -0.82% | -11.45% | 0.91% | 0.11% | 11.55% |
| trend_8_26 AND momentum_26 | 1.66% | -2.52% | 0.91% | 0.42% | 46.46% |
| trend_8_26 + momentum_26 | 0.92% | -3.44% | 0.91% | 0.49% | 54.20% |
| trend_8_26 AND breakout_8 | 0.71% | -10.84% | 0.91% | 0.14% | 15.22% |
| trend_8_26 + breakout_8 | 0.90% | -9.73% | 0.91% | 0.36% | 39.77% |
| trend_8_26 AND reversion_12 | 0.37% | -4.56% | 0.91% | 0.06% | 6.30% |
| trend_8_26 + reversion_12 | 0.14% | -5.79% | 0.91% | 0.37% | 40.42% |
| trend_8_26 AND volume_26 | 0.73% | -5.02% | 0.91% | 0.05% | 5.77% |
| trend_8_26 + volume_26 | 0.41% | -7.10% | 0.91% | 0.31% | 33.86% |
| momentum_26 AND breakout_8 | -0.09% | -11.17% | 0.91% | 0.14% | 15.49% |
| momentum_26 + breakout_8 | 0.17% | -10.20% | 0.91% | 0.35% | 37.80% |
| momentum_26 AND reversion_12 | -0.18% | -3.88% | 0.91% | 0.05% | 5.77% |
| momentum_26 + reversion_12 | -0.58% | -5.88% | 0.91% | 0.35% | 38.46% |
| momentum_26 AND volume_26 | -0.36% | -6.05% | 0.91% | 0.05% | 4.99% |
| momentum_26 + volume_26 | -0.31% | -7.00% | 0.91% | 0.29% | 31.89% |
| breakout_8 AND reversion_12 | 0.00% | 0.00% | 0.91% | 0.00% | 0.00% |
| breakout_8 + reversion_12 | -0.61% | -12.57% | 0.91% | 0.22% | 24.02% |
| breakout_8 AND volume_26 | -0.82% | -4.90% | 0.91% | 0.03% | 3.41% |
| breakout_8 + volume_26 | -0.34% | -13.06% | 0.91% | 0.16% | 17.46% |
| reversion_12 AND volume_26 | -0.20% | -5.11% | 0.91% | 0.04% | 3.94% |
| reversion_12 + volume_26 | -1.09% | -10.39% | 0.91% | 0.17% | 18.12% |

동일 구간·초기 자금, 종료 시 청산 비용 포함. 노출 맞춤은 사후 설명용이며 v2 실제 계좌 성과가 아닙니다.
[낙폭 분해·비용 영향·전체 구간](DIA/comparison.json)

[v1 전체 기록](DIA/accounts.json) · [v2 전체 기록](DIA/accounts-v2.json)

## MSFT 계좌

| 모델 | 전략 | 평가액 USD | 손익 USD | 최근 매매·이유 |
|---|---|---:|---:|---|
| v1 | cash | 10000.00 | 0.00 | 대기 /  / 새 신호 대기 |
| v1 | buy_hold | 10032.50 | 32.50 | buy /  / buy_hold: prior completed bar target 100%; next bar open simulation |
| v1 | trend_8_26 | 10032.50 | 32.50 | buy /  / trend_8_26: prior completed bar target 100%; next bar open simulation |
| v1 | momentum_26 | 10034.56 | 34.56 | buy /  / momentum_26: prior completed bar target 100%; next bar open simulation |
| v1 | breakout_8 | 9966.64 | -33.36 | sell /  / breakout_8: prior completed bar target 0%; next bar open simulation |
| v1 | reversion_12 | 10000.00 | 0.00 | 대기 /  / 새 신호 대기 |
| v1 | volume_26 | 9997.72 | -2.28 | sell /  / volume_26: prior completed bar target 0%; next bar open simulation |
| v1 | trend_8_26 AND momentum_26 | 10034.56 | 34.56 | buy /  / trend_8_26 AND momentum_26: prior completed bar target 100%; next bar open simulation |
| v1 | trend_8_26 + momentum_26 | 10033.53 | 33.53 | buy /  / trend_8_26 + momentum_26: prior completed bar target 100%; next bar open simulation |
| v1 | trend_8_26 AND breakout_8 | 9966.64 | -33.36 | sell /  / trend_8_26 AND breakout_8: prior completed bar target 0%; next bar open simulation |
| v1 | trend_8_26 + breakout_8 | 9999.50 | -0.50 | buy /  / trend_8_26 + breakout_8: prior completed bar target 50%; next bar open simulation |
| v1 | trend_8_26 AND reversion_12 | 10000.00 | 0.00 | 대기 /  / 새 신호 대기 |
| v1 | trend_8_26 + reversion_12 | 10016.19 | 16.19 | buy /  / trend_8_26 + reversion_12: prior completed bar target 50%; next bar open simulation |
| v1 | trend_8_26 AND volume_26 | 9997.72 | -2.28 | sell /  / trend_8_26 AND volume_26: prior completed bar target 0%; next bar open simulation |
| v1 | trend_8_26 + volume_26 | 10015.08 | 15.08 | buy /  / trend_8_26 + volume_26: prior completed bar target 50%; next bar open simulation |
| v1 | momentum_26 AND breakout_8 | 9966.64 | -33.36 | sell /  / momentum_26 AND breakout_8: prior completed bar target 0%; next bar open simulation |
| v1 | momentum_26 + breakout_8 | 10000.54 | 0.54 | buy /  / momentum_26 + breakout_8: prior completed bar target 50%; next bar open simulation |
| v1 | momentum_26 AND reversion_12 | 10000.00 | 0.00 | 대기 /  / 새 신호 대기 |
| v1 | momentum_26 + reversion_12 | 10017.23 | 17.23 | buy /  / momentum_26 + reversion_12: prior completed bar target 50%; next bar open simulation |
| v1 | momentum_26 AND volume_26 | 9997.72 | -2.28 | sell /  / momentum_26 AND volume_26: prior completed bar target 0%; next bar open simulation |
| v1 | momentum_26 + volume_26 | 10016.11 | 16.11 | buy /  / momentum_26 + volume_26: prior completed bar target 50%; next bar open simulation |
| v1 | breakout_8 AND reversion_12 | 10000.00 | 0.00 | 대기 /  / 새 신호 대기 |
| v1 | breakout_8 + reversion_12 | 9983.29 | -16.71 | sell /  / breakout_8 + reversion_12: prior completed bar target 0%; next bar open simulation |
| v1 | breakout_8 AND volume_26 | 10000.00 | 0.00 | 대기 /  / 새 신호 대기 |
| v1 | breakout_8 + volume_26 | 10002.13 | 2.13 | sell /  / breakout_8 + volume_26: prior completed bar target 0%; next bar open simulation |
| v1 | reversion_12 AND volume_26 | 10000.00 | 0.00 | 대기 /  / 새 신호 대기 |
| v1 | reversion_12 + volume_26 | 9998.84 | -1.16 | sell /  / reversion_12 + volume_26: prior completed bar target 0%; next bar open simulation |
| v2 | cash | 10000.00 | 0.00 | 대기 /  / 새 신호 대기 |
| v2 | buy_hold | 10017.24 | 17.24 | buy / partial / 직전 완료 봉 목표 비중 100%; 다음 봉 시가 가정 |
| v2 | trend_8_26 | 9899.65 | -100.35 | buy / partial / 직전 완료 봉 목표 비중 100%; 다음 봉 시가 가정 |
| v2 | momentum_26 | 10011.32 | 11.32 | buy / partial / 직전 완료 봉 목표 비중 100%; 다음 봉 시가 가정 |
| v2 | breakout_8 | 9889.00 | -111.00 | sell / filled / 직전 완료 봉 목표 비중 0%; 다음 봉 시가 가정 |
| v2 | reversion_12 | 9618.62 | -381.38 | sell / filled / 직전 완료 봉 목표 비중 0%; 다음 봉 시가 가정 |
| v2 | volume_26 | 9734.37 | -265.63 | sell / filled / 직전 완료 봉 목표 비중 0%; 다음 봉 시가 가정 |
| v2 | trend_8_26 AND momentum_26 | 9860.18 | -139.82 | buy / partial / 직전 완료 봉 목표 비중 100%; 다음 봉 시가 가정 |
| v2 | trend_8_26 + momentum_26 | 9955.59 | -44.41 | buy / partial / 직전 완료 봉 목표 비중 100%; 다음 봉 시가 가정 |
| v2 | trend_8_26 AND breakout_8 | 9727.35 | -272.65 | sell / filled / 직전 완료 봉 목표 비중 0%; 다음 봉 시가 가정 |
| v2 | trend_8_26 + breakout_8 | 9915.29 | -84.71 | buy / filled / 직전 완료 봉 목표 비중 50%; 다음 봉 시가 가정 |
| v2 | trend_8_26 AND reversion_12 | 9900.10 | -99.90 | sell / filled / 직전 완료 봉 목표 비중 0%; 다음 봉 시가 가정 |
| v2 | trend_8_26 + reversion_12 | 9757.80 | -242.20 | buy / filled / 직전 완료 봉 목표 비중 50%; 다음 봉 시가 가정 |
| v2 | trend_8_26 AND volume_26 | 9995.72 | -4.28 | sell / filled / 직전 완료 봉 목표 비중 0%; 다음 봉 시가 가정 |
| v2 | trend_8_26 + volume_26 | 9837.07 | -162.93 | buy / filled / 직전 완료 봉 목표 비중 50%; 다음 봉 시가 가정 |
| v2 | momentum_26 AND breakout_8 | 9883.86 | -116.14 | sell / filled / 직전 완료 봉 목표 비중 0%; 다음 봉 시가 가정 |
| v2 | momentum_26 + breakout_8 | 9950.00 | -50.00 | buy / filled / 직전 완료 봉 목표 비중 50%; 다음 봉 시가 가정 |
| v2 | momentum_26 AND reversion_12 | 9826.88 | -173.12 | sell / filled / 직전 완료 봉 목표 비중 0%; 다음 봉 시가 가정 |
| v2 | momentum_26 + reversion_12 | 9812.80 | -187.20 | buy / filled / 직전 완료 봉 목표 비중 50%; 다음 봉 시가 가정 |
| v2 | momentum_26 AND volume_26 | 9917.94 | -82.06 | sell / filled / 직전 완료 봉 목표 비중 0%; 다음 봉 시가 가정 |
| v2 | momentum_26 + volume_26 | 9892.54 | -107.46 | buy / filled / 직전 완료 봉 목표 비중 50%; 다음 봉 시가 가정 |
| v2 | breakout_8 AND reversion_12 | 10000.00 | 0.00 | 대기 /  / 새 신호 대기 |
| v2 | breakout_8 + reversion_12 | 9773.22 | -226.78 | sell / filled / 직전 완료 봉 목표 비중 0%; 다음 봉 시가 가정 |
| v2 | breakout_8 AND volume_26 | 9938.59 | -61.41 | sell / filled / 직전 완료 봉 목표 비중 0%; 다음 봉 시가 가정 |
| v2 | breakout_8 + volume_26 | 9832.12 | -167.88 | sell / filled / 직전 완료 봉 목표 비중 0%; 다음 봉 시가 가정 |
| v2 | reversion_12 AND volume_26 | 9762.04 | -237.96 | sell / filled / 직전 완료 봉 목표 비중 0%; 다음 봉 시가 가정 |
| v2 | reversion_12 + volume_26 | 9676.20 | -323.80 | sell / filled / 직전 완료 봉 목표 비중 0%; 다음 봉 시가 가정 |

### 같은 기간의 비용·노출 비교 (사후 연구)

| 전략 | 비용 전 | 비용 후 | 100% 보유 | 같은 평균 노출 보유 | 평균 노출 |
|---|---:|---:|---:|---:|---:|
| cash | 0.00% | 0.00% | 7.76% | 0.00% | 0.00% |
| buy_hold | 8.21% | 7.76% | 7.76% | 7.76% | 100.00% |
| trend_8_26 | 2.97% | -0.85% | 7.76% | 4.53% | 59.58% |
| momentum_26 | 1.37% | -4.42% | 7.76% | 4.53% | 59.58% |
| breakout_8 | 4.76% | -9.94% | 7.76% | 1.57% | 21.00% |
| reversion_12 | -4.05% | -12.52% | 7.76% | 1.74% | 23.36% |
| volume_26 | 5.29% | -3.19% | 7.76% | 0.60% | 8.14% |
| trend_8_26 AND momentum_26 | -0.04% | -5.75% | 7.76% | 4.06% | 53.54% |
| trend_8_26 + momentum_26 | 2.19% | -2.63% | 7.76% | 4.53% | 59.58% |
| trend_8_26 AND breakout_8 | 0.36% | -10.02% | 7.76% | 1.03% | 13.91% |
| trend_8_26 + breakout_8 | 3.89% | -5.08% | 7.76% | 3.03% | 40.29% |
| trend_8_26 AND reversion_12 | -3.39% | -8.52% | 7.76% | 0.52% | 7.09% |
| trend_8_26 + reversion_12 | -0.57% | -6.47% | 7.76% | 3.12% | 41.47% |
| trend_8_26 AND volume_26 | 6.34% | 3.26% | 7.76% | 0.19% | 2.62% |
| trend_8_26 + volume_26 | 4.14% | -1.20% | 7.76% | 2.54% | 33.86% |
| momentum_26 AND breakout_8 | 2.30% | -8.67% | 7.76% | 1.05% | 14.17% |
| momentum_26 + breakout_8 | 3.07% | -6.62% | 7.76% | 3.03% | 40.29% |
| momentum_26 AND reversion_12 | -2.74% | -8.67% | 7.76% | 0.60% | 8.14% |
| momentum_26 + reversion_12 | -1.35% | -8.17% | 7.76% | 3.12% | 41.47% |
| momentum_26 AND volume_26 | 1.86% | -1.92% | 7.76% | 0.23% | 3.15% |
| momentum_26 + volume_26 | 3.34% | -2.37% | 7.76% | 2.54% | 33.86% |
| breakout_8 AND reversion_12 | 0.00% | 0.00% | 7.76% | 0.00% | 0.00% |
| breakout_8 + reversion_12 | 0.29% | -10.67% | 7.76% | 1.66% | 22.19% |
| breakout_8 AND volume_26 | 2.07% | -0.47% | 7.76% | 0.14% | 1.84% |
| breakout_8 + volume_26 | 5.05% | -5.43% | 7.76% | 1.08% | 14.57% |
| reversion_12 AND volume_26 | -2.27% | -5.89% | 7.76% | 0.25% | 3.41% |
| reversion_12 + volume_26 | 0.54% | -7.76% | 7.76% | 1.17% | 15.75% |

동일 구간·초기 자금, 종료 시 청산 비용 포함. 노출 맞춤은 사후 설명용이며 v2 실제 계좌 성과가 아닙니다.
[낙폭 분해·비용 영향·전체 구간](MSFT/comparison.json)

[v1 전체 기록](MSFT/accounts.json) · [v2 전체 기록](MSFT/accounts-v2.json)

## JPM 계좌

| 모델 | 전략 | 평가액 USD | 손익 USD | 최근 매매·이유 |
|---|---|---:|---:|---|
| v1 | cash | 10000.00 | 0.00 | 대기 /  / 새 신호 대기 |
| v1 | buy_hold | 9986.75 | -13.25 | buy /  / buy_hold: prior completed bar target 100%; next bar open simulation |
| v1 | trend_8_26 | 9955.01 | -44.99 | sell /  / trend_8_26: prior completed bar target 0%; next bar open simulation |
| v1 | momentum_26 | 9852.47 | -147.53 | buy /  / momentum_26: prior completed bar target 100%; next bar open simulation |
| v1 | breakout_8 | 9956.81 | -43.19 | sell /  / breakout_8: prior completed bar target 0%; next bar open simulation |
| v1 | reversion_12 | 9950.66 | -49.34 | sell /  / reversion_12: prior completed bar target 0%; next bar open simulation |
| v1 | volume_26 | 10000.00 | 0.00 | 대기 /  / 새 신호 대기 |
| v1 | trend_8_26 AND momentum_26 | 9930.31 | -69.69 | sell /  / trend_8_26 AND momentum_26: prior completed bar target 0%; next bar open simulation |
| v1 | trend_8_26 + momentum_26 | 9903.56 | -96.44 | sell /  / trend_8_26 + momentum_26: prior completed bar target 50%; next bar open simulation |
| v1 | trend_8_26 AND breakout_8 | 10000.00 | 0.00 | 대기 /  / 새 신호 대기 |
| v1 | trend_8_26 + breakout_8 | 9955.88 | -44.12 | sell /  / trend_8_26 + breakout_8: prior completed bar target 0%; next bar open simulation |
| v1 | trend_8_26 AND reversion_12 | 10000.00 | 0.00 | 대기 /  / 새 신호 대기 |
| v1 | trend_8_26 + reversion_12 | 9992.68 | -7.32 | sell /  / trend_8_26 + reversion_12: prior completed bar target 0%; next bar open simulation |
| v1 | trend_8_26 AND volume_26 | 10000.00 | 0.00 | 대기 /  / 새 신호 대기 |
| v1 | trend_8_26 + volume_26 | 9977.48 | -22.52 | sell /  / trend_8_26 + volume_26: prior completed bar target 0%; next bar open simulation |
| v1 | momentum_26 AND breakout_8 | 9956.81 | -43.19 | sell /  / momentum_26 AND breakout_8: prior completed bar target 0%; next bar open simulation |
| v1 | momentum_26 + breakout_8 | 9904.48 | -95.52 | sell /  / momentum_26 + breakout_8: prior completed bar target 50%; next bar open simulation |
| v1 | momentum_26 AND reversion_12 | 10000.00 | 0.00 | 대기 /  / 새 신호 대기 |
| v1 | momentum_26 + reversion_12 | 9960.98 | -39.02 | buy /  / momentum_26 + reversion_12: prior completed bar target 50%; next bar open simulation |
| v1 | momentum_26 AND volume_26 | 10000.00 | 0.00 | 대기 /  / 새 신호 대기 |
| v1 | momentum_26 + volume_26 | 9925.91 | -74.09 | sell /  / momentum_26 + volume_26: prior completed bar target 50%; next bar open simulation |
| v1 | breakout_8 AND reversion_12 | 10000.00 | 0.00 | 대기 /  / 새 신호 대기 |
| v1 | breakout_8 + reversion_12 | 9973.63 | -26.37 | sell /  / breakout_8 + reversion_12: prior completed bar target 0%; next bar open simulation |
| v1 | breakout_8 AND volume_26 | 10000.00 | 0.00 | 대기 /  / 새 신호 대기 |
| v1 | breakout_8 + volume_26 | 9978.36 | -21.64 | sell /  / breakout_8 + volume_26: prior completed bar target 0%; next bar open simulation |
| v1 | reversion_12 AND volume_26 | 10000.00 | 0.00 | 대기 /  / 새 신호 대기 |
| v1 | reversion_12 + volume_26 | 9975.27 | -24.73 | sell /  / reversion_12 + volume_26: prior completed bar target 0%; next bar open simulation |
| v2 | cash | 10000.00 | 0.00 | 대기 /  / 새 신호 대기 |
| v2 | buy_hold | 9982.32 | -17.68 | buy / partial / 직전 완료 봉 목표 비중 100%; 다음 봉 시가 가정 |
| v2 | trend_8_26 | 9868.13 | -131.87 | sell / filled / 직전 완료 봉 목표 비중 0%; 다음 봉 시가 가정 |
| v2 | momentum_26 | 9407.39 | -592.61 | buy / partial / 직전 완료 봉 목표 비중 100%; 다음 봉 시가 가정 |
| v2 | breakout_8 | 9383.42 | -616.58 | sell / filled / 직전 완료 봉 목표 비중 0%; 다음 봉 시가 가정 |
| v2 | reversion_12 | 9991.97 | -8.03 | sell / filled / 직전 완료 봉 목표 비중 0%; 다음 봉 시가 가정 |
| v2 | volume_26 | 9826.70 | -173.30 | sell / filled / 직전 완료 봉 목표 비중 0%; 다음 봉 시가 가정 |
| v2 | trend_8_26 AND momentum_26 | 9865.61 | -134.39 | sell / filled / 직전 완료 봉 목표 비중 0%; 다음 봉 시가 가정 |
| v2 | trend_8_26 + momentum_26 | 9635.50 | -364.50 | sell / filled / 직전 완료 봉 목표 비중 50%; 다음 봉 시가 가정 |
| v2 | trend_8_26 AND breakout_8 | 9420.50 | -579.50 | sell / filled / 직전 완료 봉 목표 비중 0%; 다음 봉 시가 가정 |
| v2 | trend_8_26 + breakout_8 | 9623.31 | -376.69 | sell / filled / 직전 완료 봉 목표 비중 0%; 다음 봉 시가 가정 |
| v2 | trend_8_26 AND reversion_12 | 9981.61 | -18.39 | sell / filled / 직전 완료 봉 목표 비중 0%; 다음 봉 시가 가정 |
| v2 | trend_8_26 + reversion_12 | 9971.73 | -28.27 | sell / filled / 직전 완료 봉 목표 비중 0%; 다음 봉 시가 가정 |
| v2 | trend_8_26 AND volume_26 | 9800.30 | -199.70 | sell / filled / 직전 완료 봉 목표 비중 0%; 다음 봉 시가 가정 |
| v2 | trend_8_26 + volume_26 | 9847.91 | -152.09 | sell / filled / 직전 완료 봉 목표 비중 0%; 다음 봉 시가 가정 |
| v2 | momentum_26 AND breakout_8 | 9364.66 | -635.34 | sell / filled / 직전 완료 봉 목표 비중 0%; 다음 봉 시가 가정 |
| v2 | momentum_26 + breakout_8 | 9416.35 | -583.65 | sell / filled / 직전 완료 봉 목표 비중 50%; 다음 봉 시가 가정 |
| v2 | momentum_26 AND reversion_12 | 9950.76 | -49.24 | sell / filled / 직전 완료 봉 목표 비중 0%; 다음 봉 시가 가정 |
| v2 | momentum_26 + reversion_12 | 9818.64 | -181.36 | buy / filled / 직전 완료 봉 목표 비중 50%; 다음 봉 시가 가정 |
| v2 | momentum_26 AND volume_26 | 9800.30 | -199.70 | sell / filled / 직전 완료 봉 목표 비중 0%; 다음 봉 시가 가정 |
| v2 | momentum_26 + volume_26 | 9676.46 | -323.54 | sell / filled / 직전 완료 봉 목표 비중 50%; 다음 봉 시가 가정 |
| v2 | breakout_8 AND reversion_12 | 10000.00 | 0.00 | 대기 /  / 새 신호 대기 |
| v2 | breakout_8 + reversion_12 | 9723.93 | -276.07 | sell / filled / 직전 완료 봉 목표 비중 0%; 다음 봉 시가 가정 |
| v2 | breakout_8 AND volume_26 | 9893.34 | -106.66 | sell / filled / 직전 완료 봉 목표 비중 0%; 다음 봉 시가 가정 |
| v2 | breakout_8 + volume_26 | 9622.85 | -377.15 | sell / filled / 직전 완료 봉 목표 비중 0%; 다음 봉 시가 가정 |
| v2 | reversion_12 AND volume_26 | 10051.38 | 51.38 | sell / filled / 직전 완료 봉 목표 비중 0%; 다음 봉 시가 가정 |
| v2 | reversion_12 + volume_26 | 9930.12 | -69.88 | sell / filled / 직전 완료 봉 목표 비중 0%; 다음 봉 시가 가정 |

### 같은 기간의 비용·노출 비교 (사후 연구)

| 전략 | 비용 전 | 비용 후 | 100% 보유 | 같은 평균 노출 보유 | 평균 노출 |
|---|---:|---:|---:|---:|---:|
| cash | 0.00% | 0.00% | -2.28% | -0.00% | 0.00% |
| buy_hold | -1.86% | -2.28% | -2.28% | -2.28% | 100.00% |
| trend_8_26 | -0.55% | -3.84% | -2.28% | -1.23% | 53.28% |
| momentum_26 | -3.00% | -9.30% | -2.28% | -1.09% | 47.24% |
| breakout_8 | -4.16% | -18.64% | -2.28% | -0.45% | 19.42% |
| reversion_12 | 4.63% | -9.67% | -2.28% | -0.61% | 26.51% |
| volume_26 | -0.72% | -6.78% | -2.28% | -0.16% | 6.82% |
| trend_8_26 AND momentum_26 | -0.08% | -4.19% | -2.28% | -0.98% | 42.26% |
| trend_8_26 + momentum_26 | -1.77% | -6.60% | -2.28% | -1.16% | 50.27% |
| trend_8_26 AND breakout_8 | -4.20% | -14.11% | -2.28% | -0.28% | 12.07% |
| trend_8_26 + breakout_8 | -2.36% | -11.35% | -2.28% | -0.84% | 36.36% |
| trend_8_26 AND reversion_12 | 2.82% | -3.46% | -2.28% | -0.15% | 6.56% |
| trend_8_26 + reversion_12 | 2.02% | -6.22% | -2.28% | -0.92% | 39.90% |
| trend_8_26 AND volume_26 | -1.19% | -5.26% | -2.28% | -0.10% | 4.20% |
| trend_8_26 + volume_26 | -0.62% | -5.32% | -2.28% | -0.70% | 30.06% |
| momentum_26 AND breakout_8 | -3.05% | -13.08% | -2.28% | -0.27% | 11.81% |
| momentum_26 + breakout_8 | -3.56% | -13.90% | -2.28% | -0.77% | 33.34% |
| momentum_26 AND reversion_12 | 2.89% | -3.80% | -2.28% | -0.13% | 5.51% |
| momentum_26 + reversion_12 | 0.77% | -7.95% | -2.28% | -0.85% | 36.88% |
| momentum_26 AND volume_26 | -0.41% | -3.30% | -2.28% | -0.07% | 2.89% |
| momentum_26 + volume_26 | -1.85% | -7.46% | -2.28% | -0.63% | 27.04% |
| breakout_8 AND reversion_12 | 0.00% | 0.00% | -2.28% | -0.00% | 0.00% |
| breakout_8 + reversion_12 | 0.16% | -12.82% | -2.28% | -0.53% | 22.97% |
| breakout_8 AND volume_26 | -1.13% | -2.78% | -2.28% | -0.02% | 1.05% |
| breakout_8 + volume_26 | -2.44% | -11.81% | -2.28% | -0.31% | 13.13% |
| reversion_12 AND volume_26 | 1.25% | -2.10% | -2.28% | -0.08% | 3.41% |
| reversion_12 + volume_26 | 1.93% | -7.47% | -2.28% | -0.39% | 16.67% |

동일 구간·초기 자금, 종료 시 청산 비용 포함. 노출 맞춤은 사후 설명용이며 v2 실제 계좌 성과가 아닙니다.
[낙폭 분해·비용 영향·전체 구간](JPM/comparison.json)

[v1 전체 기록](JPM/accounts.json) · [v2 전체 기록](JPM/accounts-v2.json)

## XOM 계좌

| 모델 | 전략 | 평가액 USD | 손익 USD | 최근 매매·이유 |
|---|---|---:|---:|---|
| v1 | cash | 10000.00 | 0.00 | 대기 /  / 새 신호 대기 |
| v1 | buy_hold | 9935.62 | -64.38 | buy /  / buy_hold: prior completed bar target 100%; next bar open simulation |
| v1 | trend_8_26 | 10000.00 | 0.00 | 대기 /  / 새 신호 대기 |
| v1 | momentum_26 | 10000.00 | 0.00 | 대기 /  / 새 신호 대기 |
| v1 | breakout_8 | 10000.00 | 0.00 | 대기 /  / 새 신호 대기 |
| v1 | reversion_12 | 9926.56 | -73.44 | buy /  / reversion_12: prior completed bar target 100%; next bar open simulation |
| v1 | volume_26 | 10000.00 | 0.00 | 대기 /  / 새 신호 대기 |
| v1 | trend_8_26 AND momentum_26 | 10000.00 | 0.00 | 대기 /  / 새 신호 대기 |
| v1 | trend_8_26 + momentum_26 | 10000.00 | 0.00 | 대기 /  / 새 신호 대기 |
| v1 | trend_8_26 AND breakout_8 | 10000.00 | 0.00 | 대기 /  / 새 신호 대기 |
| v1 | trend_8_26 + breakout_8 | 10000.00 | 0.00 | 대기 /  / 새 신호 대기 |
| v1 | trend_8_26 AND reversion_12 | 10000.00 | 0.00 | 대기 /  / 새 신호 대기 |
| v1 | trend_8_26 + reversion_12 | 9963.17 | -36.83 | buy /  / trend_8_26 + reversion_12: prior completed bar target 50%; next bar open simulation |
| v1 | trend_8_26 AND volume_26 | 10000.00 | 0.00 | 대기 /  / 새 신호 대기 |
| v1 | trend_8_26 + volume_26 | 10000.00 | 0.00 | 대기 /  / 새 신호 대기 |
| v1 | momentum_26 AND breakout_8 | 10000.00 | 0.00 | 대기 /  / 새 신호 대기 |
| v1 | momentum_26 + breakout_8 | 10000.00 | 0.00 | 대기 /  / 새 신호 대기 |
| v1 | momentum_26 AND reversion_12 | 10000.00 | 0.00 | 대기 /  / 새 신호 대기 |
| v1 | momentum_26 + reversion_12 | 9963.17 | -36.83 | buy /  / momentum_26 + reversion_12: prior completed bar target 50%; next bar open simulation |
| v1 | momentum_26 AND volume_26 | 10000.00 | 0.00 | 대기 /  / 새 신호 대기 |
| v1 | momentum_26 + volume_26 | 10000.00 | 0.00 | 대기 /  / 새 신호 대기 |
| v1 | breakout_8 AND reversion_12 | 10000.00 | 0.00 | 대기 /  / 새 신호 대기 |
| v1 | breakout_8 + reversion_12 | 9963.17 | -36.83 | buy /  / breakout_8 + reversion_12: prior completed bar target 50%; next bar open simulation |
| v1 | breakout_8 AND volume_26 | 10000.00 | 0.00 | 대기 /  / 새 신호 대기 |
| v1 | breakout_8 + volume_26 | 10000.00 | 0.00 | 대기 /  / 새 신호 대기 |
| v1 | reversion_12 AND volume_26 | 10000.00 | 0.00 | 대기 /  / 새 신호 대기 |
| v1 | reversion_12 + volume_26 | 9963.17 | -36.83 | buy /  / reversion_12 + volume_26: prior completed bar target 50%; next bar open simulation |
| v2 | cash | 10000.00 | 0.00 | 대기 /  / 새 신호 대기 |
| v2 | buy_hold | 10183.85 | 183.85 | buy / partial / 직전 완료 봉 목표 비중 100%; 다음 봉 시가 가정 |
| v2 | trend_8_26 | 10096.25 | 96.25 | sell / filled / 직전 완료 봉 목표 비중 0%; 다음 봉 시가 가정 |
| v2 | momentum_26 | 10172.64 | 172.64 | sell / filled / 직전 완료 봉 목표 비중 0%; 다음 봉 시가 가정 |
| v2 | breakout_8 | 9471.02 | -528.98 | sell / filled / 직전 완료 봉 목표 비중 0%; 다음 봉 시가 가정 |
| v2 | reversion_12 | 9756.99 | -243.01 | buy / partial / 직전 완료 봉 목표 비중 100%; 다음 봉 시가 가정 |
| v2 | volume_26 | 9908.04 | -91.96 | sell / filled / 직전 완료 봉 목표 비중 0%; 다음 봉 시가 가정 |
| v2 | trend_8_26 AND momentum_26 | 10103.74 | 103.74 | sell / filled / 직전 완료 봉 목표 비중 0%; 다음 봉 시가 가정 |
| v2 | trend_8_26 + momentum_26 | 10134.41 | 134.41 | sell / filled / 직전 완료 봉 목표 비중 0%; 다음 봉 시가 가정 |
| v2 | trend_8_26 AND breakout_8 | 9453.73 | -546.27 | sell / filled / 직전 완료 봉 목표 비중 0%; 다음 봉 시가 가정 |
| v2 | trend_8_26 + breakout_8 | 9799.57 | -200.43 | sell / filled / 직전 완료 봉 목표 비중 0%; 다음 봉 시가 가정 |
| v2 | trend_8_26 AND reversion_12 | 9839.70 | -160.30 | sell / filled / 직전 완료 봉 목표 비중 0%; 다음 봉 시가 가정 |
| v2 | trend_8_26 + reversion_12 | 9925.11 | -74.89 | buy / filled / 직전 완료 봉 목표 비중 50%; 다음 봉 시가 가정 |
| v2 | trend_8_26 AND volume_26 | 9895.61 | -104.39 | sell / filled / 직전 완료 봉 목표 비중 0%; 다음 봉 시가 가정 |
| v2 | trend_8_26 + volume_26 | 10001.66 | 1.66 | sell / filled / 직전 완료 봉 목표 비중 0%; 다음 봉 시가 가정 |
| v2 | momentum_26 AND breakout_8 | 9471.02 | -528.98 | sell / filled / 직전 완료 봉 목표 비중 0%; 다음 봉 시가 가정 |
| v2 | momentum_26 + breakout_8 | 9816.10 | -183.90 | sell / filled / 직전 완료 봉 목표 비중 0%; 다음 봉 시가 가정 |
| v2 | momentum_26 AND reversion_12 | 9800.13 | -199.87 | sell / filled / 직전 완료 봉 목표 비중 0%; 다음 봉 시가 가정 |
| v2 | momentum_26 + reversion_12 | 9962.62 | -37.38 | buy / filled / 직전 완료 봉 목표 비중 50%; 다음 봉 시가 가정 |
| v2 | momentum_26 AND volume_26 | 9957.96 | -42.04 | sell / filled / 직전 완료 봉 목표 비중 0%; 다음 봉 시가 가정 |
| v2 | momentum_26 + volume_26 | 10060.52 | 60.52 | sell / filled / 직전 완료 봉 목표 비중 0%; 다음 봉 시가 가정 |
| v2 | breakout_8 AND reversion_12 | 10000.00 | 0.00 | 대기 /  / 새 신호 대기 |
| v2 | breakout_8 + reversion_12 | 9612.71 | -387.29 | buy / filled / 직전 완료 봉 목표 비중 50%; 다음 봉 시가 가정 |
| v2 | breakout_8 AND volume_26 | 9970.25 | -29.75 | sell / filled / 직전 완료 봉 목표 비중 0%; 다음 봉 시가 가정 |
| v2 | breakout_8 + volume_26 | 9707.34 | -292.66 | sell / filled / 직전 완료 봉 목표 비중 0%; 다음 봉 시가 가정 |
| v2 | reversion_12 AND volume_26 | 9949.87 | -50.13 | sell / filled / 직전 완료 봉 목표 비중 0%; 다음 봉 시가 가정 |
| v2 | reversion_12 + volume_26 | 9832.08 | -167.92 | buy / filled / 직전 완료 봉 목표 비중 50%; 다음 봉 시가 가정 |

### 같은 기간의 비용·노출 비교 (사후 연구)

| 전략 | 비용 전 | 비용 후 | 100% 보유 | 같은 평균 노출 보유 | 평균 노출 |
|---|---:|---:|---:|---:|---:|
| cash | 0.00% | 0.00% | 8.46% | 0.00% | 0.00% |
| buy_hold | 8.92% | 8.46% | 8.46% | 8.46% | 100.00% |
| trend_8_26 | 1.00% | -3.16% | 8.46% | 5.23% | 62.73% |
| momentum_26 | 0.32% | -6.99% | 8.46% | 5.73% | 68.50% |
| breakout_8 | -3.59% | -20.53% | 8.46% | 1.88% | 22.83% |
| reversion_12 | 5.70% | -5.24% | 8.46% | 1.79% | 21.78% |
| volume_26 | 4.95% | -2.69% | 8.46% | 0.41% | 4.99% |
| trend_8_26 AND momentum_26 | -0.45% | -4.95% | 8.46% | 4.79% | 57.48% |
| trend_8_26 + momentum_26 | 0.67% | -4.88% | 8.46% | 5.48% | 65.62% |
| trend_8_26 AND breakout_8 | -1.20% | -14.70% | 8.46% | 1.46% | 17.85% |
| trend_8_26 + breakout_8 | -1.30% | -12.07% | 8.46% | 3.54% | 42.79% |
| trend_8_26 AND reversion_12 | 1.89% | -3.93% | 8.46% | 0.67% | 8.14% |
| trend_8_26 + reversion_12 | 3.35% | -4.00% | 8.46% | 3.50% | 42.26% |
| trend_8_26 AND volume_26 | 2.54% | -1.67% | 8.46% | 0.21% | 2.62% |
| trend_8_26 + volume_26 | 2.97% | -2.52% | 8.46% | 2.80% | 33.86% |
| momentum_26 AND breakout_8 | -3.06% | -18.40% | 8.46% | 1.68% | 20.47% |
| momentum_26 + breakout_8 | -1.63% | -14.01% | 8.46% | 3.79% | 45.68% |
| momentum_26 AND reversion_12 | 2.27% | -4.38% | 8.46% | 0.73% | 8.92% |
| momentum_26 + reversion_12 | 3.00% | -4.52% | 8.46% | 3.74% | 45.15% |
| momentum_26 AND volume_26 | 2.42% | -1.79% | 8.46% | 0.21% | 2.62% |
| momentum_26 + volume_26 | 2.63% | -3.45% | 8.46% | 3.04% | 36.75% |
| breakout_8 AND reversion_12 | 0.00% | 0.00% | 8.46% | 0.00% | 0.00% |
| breakout_8 + reversion_12 | 0.97% | -12.85% | 8.46% | 1.83% | 22.32% |
| breakout_8 AND volume_26 | 0.60% | -0.66% | 8.46% | 0.06% | 0.79% |
| breakout_8 + volume_26 | 0.60% | -10.94% | 8.46% | 1.14% | 13.92% |
| reversion_12 AND volume_26 | 1.84% | -1.11% | 8.46% | 0.15% | 1.84% |
| reversion_12 + volume_26 | 5.34% | -3.37% | 8.46% | 1.10% | 13.39% |

동일 구간·초기 자금, 종료 시 청산 비용 포함. 노출 맞춤은 사후 설명용이며 v2 실제 계좌 성과가 아닙니다.
[낙폭 분해·비용 영향·전체 구간](XOM/comparison.json)

[v1 전체 기록](XOM/accounts.json) · [v2 전체 기록](XOM/accounts-v2.json)

## JNJ 계좌

| 모델 | 전략 | 평가액 USD | 손익 USD | 최근 매매·이유 |
|---|---|---:|---:|---|
| v1 | cash | 10000.00 | 0.00 | 대기 /  / 새 신호 대기 |
| v1 | buy_hold | 9817.02 | -182.98 | buy /  / buy_hold: prior completed bar target 100%; next bar open simulation |
| v1 | trend_8_26 | 9817.02 | -182.98 | buy /  / trend_8_26: prior completed bar target 100%; next bar open simulation |
| v1 | momentum_26 | 9817.02 | -182.98 | buy /  / momentum_26: prior completed bar target 100%; next bar open simulation |
| v1 | breakout_8 | 10000.00 | 0.00 | 대기 /  / 새 신호 대기 |
| v1 | reversion_12 | 9867.37 | -132.63 | buy /  / reversion_12: prior completed bar target 100%; next bar open simulation |
| v1 | volume_26 | 10000.00 | 0.00 | 대기 /  / 새 신호 대기 |
| v1 | trend_8_26 AND momentum_26 | 9817.02 | -182.98 | buy /  / trend_8_26 AND momentum_26: prior completed bar target 100%; next bar open simulation |
| v1 | trend_8_26 + momentum_26 | 9817.02 | -182.98 | buy /  / trend_8_26 + momentum_26: prior completed bar target 100%; next bar open simulation |
| v1 | trend_8_26 AND breakout_8 | 10000.00 | 0.00 | 대기 /  / 새 신호 대기 |
| v1 | trend_8_26 + breakout_8 | 9908.09 | -91.91 | buy /  / trend_8_26 + breakout_8: prior completed bar target 50%; next bar open simulation |
| v1 | trend_8_26 AND reversion_12 | 9867.37 | -132.63 | buy /  / trend_8_26 AND reversion_12: prior completed bar target 100%; next bar open simulation |
| v1 | trend_8_26 + reversion_12 | 9842.18 | -157.82 | buy /  / trend_8_26 + reversion_12: prior completed bar target 100%; next bar open simulation |
| v1 | trend_8_26 AND volume_26 | 10000.00 | 0.00 | 대기 /  / 새 신호 대기 |
| v1 | trend_8_26 + volume_26 | 9908.09 | -91.91 | buy /  / trend_8_26 + volume_26: prior completed bar target 50%; next bar open simulation |
| v1 | momentum_26 AND breakout_8 | 10000.00 | 0.00 | 대기 /  / 새 신호 대기 |
| v1 | momentum_26 + breakout_8 | 9908.09 | -91.91 | buy /  / momentum_26 + breakout_8: prior completed bar target 50%; next bar open simulation |
| v1 | momentum_26 AND reversion_12 | 9867.37 | -132.63 | buy /  / momentum_26 AND reversion_12: prior completed bar target 100%; next bar open simulation |
| v1 | momentum_26 + reversion_12 | 9842.18 | -157.82 | buy /  / momentum_26 + reversion_12: prior completed bar target 100%; next bar open simulation |
| v1 | momentum_26 AND volume_26 | 10000.00 | 0.00 | 대기 /  / 새 신호 대기 |
| v1 | momentum_26 + volume_26 | 9908.09 | -91.91 | buy /  / momentum_26 + volume_26: prior completed bar target 50%; next bar open simulation |
| v1 | breakout_8 AND reversion_12 | 10000.00 | 0.00 | 대기 /  / 새 신호 대기 |
| v1 | breakout_8 + reversion_12 | 9933.45 | -66.55 | buy /  / breakout_8 + reversion_12: prior completed bar target 50%; next bar open simulation |
| v1 | breakout_8 AND volume_26 | 10000.00 | 0.00 | 대기 /  / 새 신호 대기 |
| v1 | breakout_8 + volume_26 | 10000.00 | 0.00 | 대기 /  / 새 신호 대기 |
| v1 | reversion_12 AND volume_26 | 10000.00 | 0.00 | 대기 /  / 새 신호 대기 |
| v1 | reversion_12 + volume_26 | 9933.45 | -66.55 | buy /  / reversion_12 + volume_26: prior completed bar target 50%; next bar open simulation |
| v2 | cash | 10000.00 | 0.00 | 대기 /  / 새 신호 대기 |
| v2 | buy_hold | 9706.10 | -293.90 | 중단: 손실 한도 / buy / partial / 직전 완료 봉 목표 비중 100%; 다음 봉 시가 가정 |
| v2 | trend_8_26 | 9706.10 | -293.90 | 중단: 손실 한도 / buy / partial / 직전 완료 봉 목표 비중 100%; 다음 봉 시가 가정 |
| v2 | momentum_26 | 9706.10 | -293.90 | 중단: 손실 한도 / buy / partial / 직전 완료 봉 목표 비중 100%; 다음 봉 시가 가정 |
| v2 | breakout_8 | 9343.39 | -656.61 | 중단: 손실 한도 / sell / filled / 직전 완료 봉 목표 비중 0%; 다음 봉 시가 가정 |
| v2 | reversion_12 | 9755.38 | -244.62 | buy / partial / 직전 완료 봉 목표 비중 100%; 다음 봉 시가 가정 |
| v2 | volume_26 | 9791.36 | -208.64 | sell / filled / 직전 완료 봉 목표 비중 0%; 다음 봉 시가 가정 |
| v2 | trend_8_26 AND momentum_26 | 9706.10 | -293.90 | 중단: 손실 한도 / buy / partial / 직전 완료 봉 목표 비중 100%; 다음 봉 시가 가정 |
| v2 | trend_8_26 + momentum_26 | 9706.10 | -293.90 | 중단: 손실 한도 / buy / partial / 직전 완료 봉 목표 비중 100%; 다음 봉 시가 가정 |
| v2 | trend_8_26 AND breakout_8 | 9419.39 | -580.61 | 중단: 손실 한도 / sell / filled / 직전 완료 봉 목표 비중 0%; 다음 봉 시가 가정 |
| v2 | trend_8_26 + breakout_8 | 9579.95 | -420.05 | buy / filled / 직전 완료 봉 목표 비중 50%; 다음 봉 시가 가정 |
| v2 | trend_8_26 AND reversion_12 | 9999.27 | -0.73 | buy / partial / 직전 완료 봉 목표 비중 100%; 다음 봉 시가 가정 |
| v2 | trend_8_26 + reversion_12 | 9732.92 | -267.08 | 중단: 손실 한도 / sell / filled / 직전 완료 봉 목표 비중 0%; 다음 봉 시가 가정 |
| v2 | trend_8_26 AND volume_26 | 9870.71 | -129.29 | sell / filled / 직전 완료 봉 목표 비중 0%; 다음 봉 시가 가정 |
| v2 | trend_8_26 + volume_26 | 9825.91 | -174.09 | 중단: 손실 한도 / buy / filled / 직전 완료 봉 목표 비중 50%; 다음 봉 시가 가정 |
| v2 | momentum_26 AND breakout_8 | 9598.70 | -401.30 | sell / filled / 직전 완료 봉 목표 비중 0%; 다음 봉 시가 가정 |
| v2 | momentum_26 + breakout_8 | 9582.33 | -417.67 | buy / filled / 직전 완료 봉 목표 비중 50%; 다음 봉 시가 가정 |
| v2 | momentum_26 AND reversion_12 | 9999.27 | -0.73 | buy / partial / 직전 완료 봉 목표 비중 100%; 다음 봉 시가 가정 |
| v2 | momentum_26 + reversion_12 | 9732.92 | -267.08 | 중단: 손실 한도 / sell / filled / 직전 완료 봉 목표 비중 0%; 다음 봉 시가 가정 |
| v2 | momentum_26 AND volume_26 | 9920.93 | -79.07 | sell / filled / 직전 완료 봉 목표 비중 0%; 다음 봉 시가 가정 |
| v2 | momentum_26 + volume_26 | 9825.91 | -174.09 | 중단: 손실 한도 / buy / filled / 직전 완료 봉 목표 비중 50%; 다음 봉 시가 가정 |
| v2 | breakout_8 AND reversion_12 | 10000.00 | 0.00 | 대기 /  / 새 신호 대기 |
| v2 | breakout_8 + reversion_12 | 9613.32 | -386.68 | buy / filled / 직전 완료 봉 목표 비중 50%; 다음 봉 시가 가정 |
| v2 | breakout_8 AND volume_26 | 9814.17 | -185.83 | sell / filled / 직전 완료 봉 목표 비중 0%; 다음 봉 시가 가정 |
| v2 | breakout_8 + volume_26 | 9610.69 | -389.31 | sell / filled / 직전 완료 봉 목표 비중 0%; 다음 봉 시가 가정 |
| v2 | reversion_12 AND volume_26 | 9886.24 | -113.76 | sell / filled / 직전 완료 봉 목표 비중 0%; 다음 봉 시가 가정 |
| v2 | reversion_12 + volume_26 | 9794.19 | -205.81 | buy / filled / 직전 완료 봉 목표 비중 50%; 다음 봉 시가 가정 |

### 같은 기간의 비용·노출 비교 (사후 연구)

| 전략 | 비용 전 | 비용 후 | 100% 보유 | 같은 평균 노출 보유 | 평균 노출 |
|---|---:|---:|---:|---:|---:|
| cash | 0.00% | 0.00% | -6.74% | -0.00% | 0.00% |
| buy_hold | -6.35% | -6.74% | -6.74% | -6.74% | 100.00% |
| trend_8_26 | 2.50% | 0.37% | -6.74% | -3.28% | 47.51% |
| momentum_26 | 0.06% | -3.65% | -6.74% | -3.23% | 46.72% |
| breakout_8 | -0.27% | -16.75% | -6.74% | -1.47% | 21.00% |
| reversion_12 | -7.56% | -16.77% | -6.74% | -2.10% | 30.18% |
| volume_26 | -1.33% | -8.13% | -6.74% | -0.48% | 6.82% |
| trend_8_26 AND momentum_26 | 2.35% | -0.61% | -6.74% | -3.02% | 43.57% |
| trend_8_26 + momentum_26 | 1.28% | -1.66% | -6.74% | -3.26% | 47.11% |
| trend_8_26 AND breakout_8 | 0.78% | -11.52% | -6.74% | -1.07% | 15.22% |
| trend_8_26 + breakout_8 | 1.13% | -8.37% | -6.74% | -2.38% | 34.26% |
| trend_8_26 AND reversion_12 | 0.70% | -2.63% | -6.74% | -0.39% | 5.51% |
| trend_8_26 + reversion_12 | -2.62% | -8.21% | -6.74% | -2.69% | 38.85% |
| trend_8_26 AND volume_26 | 1.59% | -0.53% | -6.74% | -0.11% | 1.57% |
| trend_8_26 + volume_26 | 0.60% | -3.56% | -6.74% | -1.89% | 27.17% |
| momentum_26 AND breakout_8 | 2.20% | -9.52% | -6.74% | -1.01% | 14.44% |
| momentum_26 + breakout_8 | -0.08% | -10.23% | -6.74% | -2.35% | 33.87% |
| momentum_26 AND reversion_12 | -0.89% | -4.57% | -6.74% | -0.44% | 6.30% |
| momentum_26 + reversion_12 | -3.79% | -9.88% | -6.74% | -2.67% | 38.46% |
| momentum_26 AND volume_26 | 0.88% | -1.21% | -6.74% | -0.11% | 1.57% |
| momentum_26 + volume_26 | -0.61% | -5.31% | -6.74% | -1.87% | 26.77% |
| breakout_8 AND reversion_12 | 0.00% | 0.00% | -6.74% | -0.00% | 0.00% |
| breakout_8 + reversion_12 | -3.96% | -16.24% | -6.74% | -1.79% | 25.60% |
| breakout_8 AND volume_26 | -0.11% | -2.19% | -6.74% | -0.11% | 1.57% |
| breakout_8 + volume_26 | -0.79% | -11.81% | -6.74% | -0.98% | 13.92% |
| reversion_12 AND volume_26 | -2.65% | -5.47% | -6.74% | -0.20% | 2.89% |
| reversion_12 + volume_26 | -4.48% | -11.82% | -6.74% | -1.30% | 18.51% |

동일 구간·초기 자금, 종료 시 청산 비용 포함. 노출 맞춤은 사후 설명용이며 v2 실제 계좌 성과가 아닙니다.
[낙폭 분해·비용 영향·전체 구간](JNJ/comparison.json)

[v1 전체 기록](JNJ/accounts.json) · [v2 전체 기록](JNJ/accounts-v2.json)

## CAT 계좌

| 모델 | 전략 | 평가액 USD | 손익 USD | 최근 매매·이유 |
|---|---|---:|---:|---|
| v1 | cash | 10000.00 | 0.00 | 대기 /  / 새 신호 대기 |
| v1 | buy_hold | 9962.80 | -37.20 | buy /  / buy_hold: prior completed bar target 100%; next bar open simulation |
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
| v2 | buy_hold | 9108.01 | -891.99 | 중단: 손실 한도 / buy / partial / 직전 완료 봉 목표 비중 100%; 다음 봉 시가 가정 |
| v2 | trend_8_26 | 9941.61 | -58.39 | sell / filled / 직전 완료 봉 목표 비중 0%; 다음 봉 시가 가정 |
| v2 | momentum_26 | 10014.59 | 14.59 | sell / filled / 직전 완료 봉 목표 비중 0%; 다음 봉 시가 가정 |
| v2 | breakout_8 | 9806.46 | -193.54 | sell / filled / 직전 완료 봉 목표 비중 0%; 다음 봉 시가 가정 |
| v2 | reversion_12 | 8980.82 | -1019.18 | 중단: 손실 한도 / buy / partial / 직전 완료 봉 목표 비중 100%; 다음 봉 시가 가정 |
| v2 | volume_26 | 9237.66 | -762.34 | 중단: 손실 한도 / buy / partial / 직전 완료 봉 목표 비중 100%; 다음 봉 시가 가정 |
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
| v2 | reversion_12 AND volume_26 | 9173.76 | -826.24 | 중단: 손실 한도 / buy / partial / 직전 완료 봉 목표 비중 100%; 다음 봉 시가 가정 |
| v2 | reversion_12 + volume_26 | 9352.73 | -647.27 | 중단: 손실 한도 / sell / filled / 직전 완료 봉 목표 비중 50%; 다음 봉 시가 가정 |

### 같은 기간의 비용·노출 비교 (사후 연구)

| 전략 | 비용 전 | 비용 후 | 100% 보유 | 같은 평균 노출 보유 | 평균 노출 |
|---|---:|---:|---:|---:|---:|
| cash | 0.00% | 0.00% | -11.11% | -0.00% | 0.00% |
| buy_hold | -10.73% | -11.11% | -11.11% | -11.11% | 100.00% |
| trend_8_26 | -1.35% | -4.61% | -11.11% | -5.80% | 51.97% |
| momentum_26 | -4.02% | -9.50% | -11.11% | -5.71% | 51.18% |
| breakout_8 | -3.57% | -16.40% | -11.11% | -1.67% | 14.96% |
| reversion_12 | -4.23% | -15.21% | -11.11% | -2.85% | 25.46% |
| volume_26 | -2.55% | -10.03% | -11.11% | -0.94% | 8.40% |
| trend_8_26 AND momentum_26 | -1.32% | -5.77% | -11.11% | -5.07% | 45.41% |
| trend_8_26 + momentum_26 | -2.67% | -7.07% | -11.11% | -5.76% | 51.58% |
| trend_8_26 AND breakout_8 | -1.46% | -9.02% | -11.11% | -0.88% | 7.87% |
| trend_8_26 + breakout_8 | -2.43% | -10.49% | -11.11% | -3.74% | 33.47% |
| trend_8_26 AND reversion_12 | 0.78% | -5.38% | -11.11% | -0.79% | 7.09% |
| trend_8_26 + reversion_12 | -2.74% | -9.47% | -11.11% | -4.33% | 38.72% |
| trend_8_26 AND volume_26 | 2.63% | -0.76% | -11.11% | -0.32% | 2.89% |
| trend_8_26 + volume_26 | -1.90% | -7.14% | -11.11% | -3.38% | 30.19% |
| momentum_26 AND breakout_8 | -2.95% | -11.51% | -11.11% | -1.03% | 9.19% |
| momentum_26 + breakout_8 | -3.75% | -12.99% | -11.11% | -3.70% | 33.08% |
| momentum_26 AND reversion_12 | -3.04% | -8.96% | -11.11% | -0.65% | 5.77% |
| momentum_26 + reversion_12 | -4.07% | -11.46% | -11.11% | -4.28% | 38.33% |
| momentum_26 AND volume_26 | 1.58% | -0.53% | -11.11% | -0.18% | 1.57% |
| momentum_26 + volume_26 | -3.23% | -8.78% | -11.11% | -3.33% | 29.79% |
| breakout_8 AND reversion_12 | 0.00% | 0.00% | -11.11% | -0.00% | 0.00% |
| breakout_8 + reversion_12 | -3.85% | -14.90% | -11.11% | -2.26% | 20.22% |
| breakout_8 AND volume_26 | 0.78% | -0.48% | -11.11% | -0.09% | 0.79% |
| breakout_8 + volume_26 | -3.03% | -12.53% | -11.11% | -1.31% | 11.69% |
| reversion_12 AND volume_26 | -1.25% | -5.71% | -11.11% | -0.59% | 5.25% |
| reversion_12 + volume_26 | -3.36% | -11.91% | -11.11% | -1.90% | 16.93% |

동일 구간·초기 자금, 종료 시 청산 비용 포함. 노출 맞춤은 사후 설명용이며 v2 실제 계좌 성과가 아닙니다.
[낙폭 분해·비용 영향·전체 구간](CAT/comparison.json)

[v1 전체 기록](CAT/accounts.json) · [v2 전체 기록](CAT/accounts-v2.json)

## WMT 계좌

| 모델 | 전략 | 평가액 USD | 손익 USD | 최근 매매·이유 |
|---|---|---:|---:|---|
| v1 | cash | 10000.00 | 0.00 | 대기 /  / 새 신호 대기 |
| v1 | buy_hold | 9906.81 | -93.19 | buy /  / buy_hold: prior completed bar target 100%; next bar open simulation |
| v1 | trend_8_26 | 9906.81 | -93.19 | buy /  / trend_8_26: prior completed bar target 100%; next bar open simulation |
| v1 | momentum_26 | 9906.81 | -93.19 | buy /  / momentum_26: prior completed bar target 100%; next bar open simulation |
| v1 | breakout_8 | 10000.00 | 0.00 | 대기 /  / 새 신호 대기 |
| v1 | reversion_12 | 9930.96 | -69.04 | buy /  / reversion_12: prior completed bar target 100%; next bar open simulation |
| v1 | volume_26 | 10000.00 | 0.00 | 대기 /  / 새 신호 대기 |
| v1 | trend_8_26 AND momentum_26 | 9906.81 | -93.19 | buy /  / trend_8_26 AND momentum_26: prior completed bar target 100%; next bar open simulation |
| v1 | trend_8_26 + momentum_26 | 9906.81 | -93.19 | buy /  / trend_8_26 + momentum_26: prior completed bar target 100%; next bar open simulation |
| v1 | trend_8_26 AND breakout_8 | 10000.00 | 0.00 | 대기 /  / 새 신호 대기 |
| v1 | trend_8_26 + breakout_8 | 9953.25 | -46.75 | buy /  / trend_8_26 + breakout_8: prior completed bar target 50%; next bar open simulation |
| v1 | trend_8_26 AND reversion_12 | 9930.96 | -69.04 | buy /  / trend_8_26 AND reversion_12: prior completed bar target 100%; next bar open simulation |
| v1 | trend_8_26 + reversion_12 | 9918.86 | -81.14 | buy /  / trend_8_26 + reversion_12: prior completed bar target 100%; next bar open simulation |
| v1 | trend_8_26 AND volume_26 | 10000.00 | 0.00 | 대기 /  / 새 신호 대기 |
| v1 | trend_8_26 + volume_26 | 9953.25 | -46.75 | buy /  / trend_8_26 + volume_26: prior completed bar target 50%; next bar open simulation |
| v1 | momentum_26 AND breakout_8 | 10000.00 | 0.00 | 대기 /  / 새 신호 대기 |
| v1 | momentum_26 + breakout_8 | 9953.25 | -46.75 | buy /  / momentum_26 + breakout_8: prior completed bar target 50%; next bar open simulation |
| v1 | momentum_26 AND reversion_12 | 9930.96 | -69.04 | buy /  / momentum_26 AND reversion_12: prior completed bar target 100%; next bar open simulation |
| v1 | momentum_26 + reversion_12 | 9918.86 | -81.14 | buy /  / momentum_26 + reversion_12: prior completed bar target 100%; next bar open simulation |
| v1 | momentum_26 AND volume_26 | 10000.00 | 0.00 | 대기 /  / 새 신호 대기 |
| v1 | momentum_26 + volume_26 | 9953.25 | -46.75 | buy /  / momentum_26 + volume_26: prior completed bar target 50%; next bar open simulation |
| v1 | breakout_8 AND reversion_12 | 10000.00 | 0.00 | 대기 /  / 새 신호 대기 |
| v1 | breakout_8 + reversion_12 | 9965.38 | -34.62 | buy /  / breakout_8 + reversion_12: prior completed bar target 50%; next bar open simulation |
| v1 | breakout_8 AND volume_26 | 10000.00 | 0.00 | 대기 /  / 새 신호 대기 |
| v1 | breakout_8 + volume_26 | 10000.00 | 0.00 | 대기 /  / 새 신호 대기 |
| v1 | reversion_12 AND volume_26 | 10000.00 | 0.00 | 대기 /  / 새 신호 대기 |
| v1 | reversion_12 + volume_26 | 9965.38 | -34.62 | buy /  / reversion_12 + volume_26: prior completed bar target 50%; next bar open simulation |
| v2 | cash | 10000.00 | 0.00 | 대기 /  / 새 신호 대기 |
| v2 | buy_hold | 10595.23 | 595.23 | buy / partial / 직전 완료 봉 목표 비중 100%; 다음 봉 시가 가정 |
| v2 | trend_8_26 | 10451.06 | 451.06 | buy / partial / 직전 완료 봉 목표 비중 100%; 다음 봉 시가 가정 |
| v2 | momentum_26 | 10421.08 | 421.08 | buy / partial / 직전 완료 봉 목표 비중 100%; 다음 봉 시가 가정 |
| v2 | breakout_8 | 9964.65 | -35.35 | sell / filled / 직전 완료 봉 목표 비중 0%; 다음 봉 시가 가정 |
| v2 | reversion_12 | 9950.08 | -49.92 | buy / partial / 직전 완료 봉 목표 비중 100%; 다음 봉 시가 가정 |
| v2 | volume_26 | 9965.28 | -34.72 | sell / filled / 직전 완료 봉 목표 비중 0%; 다음 봉 시가 가정 |
| v2 | trend_8_26 AND momentum_26 | 10451.06 | 451.06 | buy / partial / 직전 완료 봉 목표 비중 100%; 다음 봉 시가 가정 |
| v2 | trend_8_26 + momentum_26 | 10436.05 | 436.05 | buy / partial / 직전 완료 봉 목표 비중 100%; 다음 봉 시가 가정 |
| v2 | trend_8_26 AND breakout_8 | 10088.55 | 88.55 | sell / filled / 직전 완료 봉 목표 비중 0%; 다음 봉 시가 가정 |
| v2 | trend_8_26 + breakout_8 | 10205.39 | 205.39 | buy / filled / 직전 완료 봉 목표 비중 50%; 다음 봉 시가 가정 |
| v2 | trend_8_26 AND reversion_12 | 9859.50 | -140.50 | buy / partial / 직전 완료 봉 목표 비중 100%; 다음 봉 시가 가정 |
| v2 | trend_8_26 + reversion_12 | 10199.00 | 199.00 | buy / partial / 직전 완료 봉 목표 비중 100%; 다음 봉 시가 가정 |
| v2 | trend_8_26 AND volume_26 | 9949.23 | -50.77 | sell / filled / 직전 완료 봉 목표 비중 0%; 다음 봉 시가 가정 |
| v2 | trend_8_26 + volume_26 | 10206.76 | 206.76 | buy / filled / 직전 완료 봉 목표 비중 50%; 다음 봉 시가 가정 |
| v2 | momentum_26 AND breakout_8 | 9964.65 | -35.35 | sell / filled / 직전 완료 봉 목표 비중 0%; 다음 봉 시가 가정 |
| v2 | momentum_26 + breakout_8 | 10190.78 | 190.78 | buy / filled / 직전 완료 봉 목표 비중 50%; 다음 봉 시가 가정 |
| v2 | momentum_26 AND reversion_12 | 9869.09 | -130.91 | buy / partial / 직전 완료 봉 목표 비중 100%; 다음 봉 시가 가정 |
| v2 | momentum_26 + reversion_12 | 10227.24 | 227.24 | buy / partial / 직전 완료 봉 목표 비중 100%; 다음 봉 시가 가정 |
| v2 | momentum_26 AND volume_26 | 9913.82 | -86.18 | sell / filled / 직전 완료 봉 목표 비중 0%; 다음 봉 시가 가정 |
| v2 | momentum_26 + volume_26 | 10192.21 | 192.21 | buy / filled / 직전 완료 봉 목표 비중 50%; 다음 봉 시가 가정 |
| v2 | breakout_8 AND reversion_12 | 10000.00 | 0.00 | 대기 /  / 새 신호 대기 |
| v2 | breakout_8 + reversion_12 | 9979.54 | -20.46 | buy / filled / 직전 완료 봉 목표 비중 50%; 다음 봉 시가 가정 |
| v2 | breakout_8 AND volume_26 | 9950.23 | -49.77 | sell / filled / 직전 완료 봉 목표 비중 0%; 다음 봉 시가 가정 |
| v2 | breakout_8 + volume_26 | 9966.35 | -33.65 | sell / filled / 직전 완료 봉 목표 비중 0%; 다음 봉 시가 가정 |
| v2 | reversion_12 AND volume_26 | 10009.78 | 9.78 | sell / filled / 직전 완료 봉 목표 비중 0%; 다음 봉 시가 가정 |
| v2 | reversion_12 + volume_26 | 9957.66 | -42.34 | buy / filled / 직전 완료 봉 목표 비중 50%; 다음 봉 시가 가정 |

### 같은 기간의 비용·노출 비교 (사후 연구)

| 전략 | 비용 전 | 비용 후 | 100% 보유 | 같은 평균 노출 보유 | 평균 노출 |
|---|---:|---:|---:|---:|---:|
| cash | 0.00% | 0.00% | 10.09% | 0.00% | 0.00% |
| buy_hold | 10.56% | 10.09% | 10.09% | 10.09% | 100.00% |
| trend_8_26 | 9.54% | 6.81% | 10.09% | 6.78% | 67.45% |
| momentum_26 | 6.75% | 2.79% | 10.09% | 6.72% | 66.93% |
| breakout_8 | 5.52% | -11.92% | 10.09% | 2.67% | 26.77% |
| reversion_12 | 3.06% | -6.43% | 10.09% | 1.67% | 16.80% |
| volume_26 | -0.17% | -5.87% | 10.09% | 0.60% | 6.04% |
| trend_8_26 AND momentum_26 | 9.06% | 5.02% | 10.09% | 6.19% | 61.68% |
| trend_8_26 + momentum_26 | 8.14% | 4.79% | 10.09% | 6.75% | 67.19% |
| trend_8_26 AND breakout_8 | 6.92% | -6.91% | 10.09% | 2.23% | 22.31% |
| trend_8_26 + breakout_8 | 7.52% | -2.79% | 10.09% | 4.72% | 47.12% |
| trend_8_26 AND reversion_12 | 0.31% | -4.62% | 10.09% | 0.60% | 6.04% |
| trend_8_26 + reversion_12 | 6.29% | 0.19% | 10.09% | 4.22% | 42.13% |
| trend_8_26 AND volume_26 | 1.13% | -1.39% | 10.09% | 0.21% | 2.10% |
| trend_8_26 + volume_26 | 4.61% | 0.71% | 10.09% | 3.68% | 36.75% |
| momentum_26 AND breakout_8 | 5.58% | -8.47% | 10.09% | 2.33% | 23.36% |
| momentum_26 + breakout_8 | 6.15% | -4.63% | 10.09% | 4.69% | 46.86% |
| momentum_26 AND reversion_12 | 0.27% | -4.66% | 10.09% | 0.57% | 5.77% |
| momentum_26 + reversion_12 | 4.93% | -0.04% | 10.09% | 4.19% | 41.87% |
| momentum_26 AND volume_26 | 0.44% | -3.69% | 10.09% | 0.29% | 2.89% |
| momentum_26 + volume_26 | 3.27% | -1.62% | 10.09% | 3.65% | 36.49% |
| breakout_8 AND reversion_12 | 0.00% | 0.00% | 10.09% | 0.00% | 0.00% |
| breakout_8 + reversion_12 | 4.31% | -8.83% | 10.09% | 2.17% | 21.79% |
| breakout_8 AND volume_26 | 0.91% | -1.19% | 10.09% | 0.16% | 1.57% |
| breakout_8 + volume_26 | 2.67% | -8.16% | 10.09% | 1.64% | 16.41% |
| reversion_12 AND volume_26 | -0.11% | -3.00% | 10.09% | 0.29% | 2.89% |
| reversion_12 + volume_26 | 1.44% | -5.95% | 10.09% | 1.14% | 11.42% |

동일 구간·초기 자금, 종료 시 청산 비용 포함. 노출 맞춤은 사후 설명용이며 v2 실제 계좌 성과가 아닙니다.
[낙폭 분해·비용 영향·전체 구간](WMT/comparison.json)

[v1 전체 기록](WMT/accounts.json) · [v2 전체 기록](WMT/accounts-v2.json)
