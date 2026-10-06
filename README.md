# 모의매매 프로그램

Python 3.11+ 기반으로 실행 가능한 **Alpaca 모의매매 MVP**입니다. 실계좌 URL과 실거래 기능은 포함하지 않습니다. 라이브 API 키를 넣어도 실거래 서버로 연결되지 않습니다. 전략의 수익성은 검증되지 않았습니다.

## 구현 범위

- 지정한 미국주식 목록의 일봉 수집, 페이지네이션, 전일 거래일 확인
- 거래량 급증 + 제한된 상승률 스크리닝
- 시세 시간, 스프레드, 가격 갭 검사
- 정수 주식 수량 계산, 종목 비중/개수/전일 대비 계좌 손실 제한
- limit 진입 + bracket 익절/손절 모의주문
- SQLite 주문 의도 기록과 일정한 client_order_id를 통한 재실행 방지
- 단일 종목 CSV 백테스트, 합성 데이터 데모, 단위/가짜 브로커 테스트
- GitHub Actions CI, Docker 실행

## Windows 실행

PowerShell에서 압축을 해제한 프로젝트 폴더로 이동합니다.

```powershell
py -3.12 -m venv .venv
.\.venv\Scripts\Activate.ps1
python -m pip install -e .
python -m unittest discover -s tests -v
stockbot demo
```

데모는 키 없이 동작합니다. `examples/demo.csv`는 **합성 데이터**이며 실제 주가나 성과 자료가 아닙니다.

Alpaca에서 Paper Trading 계정을 생성하고 모의 API 키를 발급받은 뒤:

```powershell
$env:APCA_API_KEY_ID = '모의_API_KEY'
$env:APCA_API_SECRET_KEY = '모의_SECRET_KEY'
stockbot scan
stockbot paper --execute-paper
stockbot run --execute-paper --interval 300
```

`scan`은 데이터 조회와 주문 계획만 출력합니다. `paper`는 한 번, `run`은 5분마다 반복하며 **모의주문**을 제출합니다. 미국 정규장 밖에서는 신규 주문하지 않습니다. PC/서버가 켜져 있어야 반복 실행됩니다. `.env.example`은 참고용이며 자동으로 읽지 않습니다. 키를 GitHub나 채팅에 올리지 마세요.

Linux/macOS에서는 `python3 -m venv .venv`, `source .venv/bin/activate`를 사용하고 환경변수는 `export`로 설정합니다.

## 전략 정의

완료된 직전 미국 거래일의 일봉에서 판단합니다.

1. 해당 거래일 거래량 / 그 이전 30거래일 평균 거래량 ≥ 3.
2. 해당 종가 / 21거래일 전 종가 − 1 ≤ 0.03. 하락폭 하한은 없습니다.
3. 다음 거래일 정규장에 최신 ask 기준 limit 주문을 계획합니다.
4. 전일 종가 대비 갭 3%, 스프레드 0.5%, quote 나이 120초 조건을 통과해야 합니다.
5. 최대 종목 비중 5%, 최대 5종목, 전일 계좌 equity 대비 손실 2%에서 신규 진입 중단.
6. 전일 종가 기준 손절 5%, 익절 15%. 실제 체결가 기준 비율과 다를 수 있습니다.

손절 가격은 체결 보장이 아니며 급격한 갭에서 손실이 커질 수 있습니다. 일일 손실 제한은 신규 진입만 중단하고 기존 포지션을 청산하지 않습니다. 계좌 입출금도 equity 비교에 영향을 줍니다. 전용 모의계좌 사용을 전제로 합니다.

설정은 `config.json`에서 수정합니다. 기본 목록은 7개 예시 종목으로 미국 전체시장 탐색이 아닙니다. 기본 `iex`는 단일 거래소 거래량으로 시장 전체 거래량이 아닙니다. 전체 시장 스크리닝에는 데이터 사용권을 확인하고 `sip`로 변경하세요. 분할 조정 데이터를 사용하지만 종목 목록의 생존 편향과 과거 유니버스 변화는 처리하지 않습니다.

## 중단 / 장애 복구

```powershell
New-Item -ItemType File -Path state/STOP -Force
```

STOP 파일은 **신규 주문 중단**용입니다. 이미 제출한 주문 취소나 포지션 청산은 Alpaca 대시보드에서 처리하세요. 재개는 파일을 삭제합니다. Ctrl+C는 반복 프로세스를 종료합니다.

주문 요청 전에 의도를 저장합니다. 요청 타임아웃/오류는 `unknown`으로 남기고 자동 재전송하지 않습니다. 계정 대시보드에서 해당 `client_order_id`와 실제 주문을 확인해야 합니다. pending/unknown은 자동 복구하지 않으며 안전하게 해당 신호를 건너뜁니다. 상태 파일 삭제는 중복 제출 위험이 있으므로 하지 마세요. 상태 디렉터리를 공유하는 한 프로세스만 실행하세요. 디렉터리 잠금으로 동시 실행을 거부합니다. 비정상 프로세스 종료 후 `state/cycle.lock`이 남으면 실행 중인 프로세스가 없는지 확인한 후 그 빈 디렉터리만 삭제하세요.

## 백테스트

```powershell
stockbot backtest --csv examples/demo.csv
```

CSV 열: `date,open,high,low,close,volume`. 날짜 오름차순, 하루 한 행, 동일한 가격 조정 기준을 사용하세요. 다음 봉 시가 진입, 기본 수수료 0.1%와 슬리피지 0.1%를 적용합니다. 한 봉에서 손절/익절이 동시에 닿으면 손절 우선으로 계산합니다. 마지막 미청산 포지션은 종가 평가합니다.

이 백테스트는 단일 종목 일봉 모델로, 실제 limit 미체결, 부분 체결, bracket 활성화 지연, 다중 종목 자금 경합을 재현하지 않습니다. 모의매매 성과와 동일하지 않습니다.

## 구조와 확장

| 파일 | 역할 |
|---|---|
| `core.py` | 스크리닝, 수량, 백테스트 |
| `broker.py` | Alpaca 모의 REST API 및 데이터 |
| `cli.py` | 캘린더, 계좌/주문 검사, 실행, 상태 |
| `tests/test_bot.py` | 전략/주문 안전성 검증 |

OpenBB, NautilusTrader, Backtrader, CCXT, Freqtrade 코드를 복사하거나 의존성으로 넣지 않았습니다. 첫 실행 가능한 미국주식 모의주문 흐름을 독립적으로 구현했습니다. 다음 단계의 연결 지점은 다음과 같습니다.

- OpenBB: 데이터 공급자 인터페이스로 펀더멘털/IR 자료 추가.
- 15가지 투자 분석: 출처·발표시점·검증 상태를 가진 별도 리서치 보고서. 현재 AI 점수/자동 판단은 구현하지 않았습니다.
- NautilusTrader: 이벤트 기반 체결 시뮬레이션 및 브로커별 주문 어댑터. 현재 연결하지 않았습니다.
- 한국 증권사 미국주식 주문: 별도 모의 API 어댑터 필요. 한국 거주자의 Alpaca 실계좌 개설 가능 여부를 전제하지 않습니다.

## GitHub 저장소

저장소: https://github.com/BaekJaeYeol/paper-trading-program

```powershell
git clone https://github.com/BaekJaeYeol/paper-trading-program.git
cd paper-trading-program
```

설치와 실행은 위의 Windows 실행 안내를 따르세요.

## 공식 API 참고

- https://docs.alpaca.markets/us/docs/working-with-orders
- https://docs.alpaca.markets/us/reference/stockbars
- https://docs.alpaca.markets/us/docs/market-data-faq
- https://docs.alpaca.markets/us/reference/getorderbyclientorderid

## v0.2 추가: 복구 코어와 토스 읽기 전용 연결

`recovery.py`는 브로커 공통 실행 코어이며 기존 `stockbot run`에는 아직 연결되지 않았습니다. 영구 주문 의도 예약, 누적 부분 체결량 갱신, 요청 불확실 시 신규 진입 차단, 재시작 시 브로커 스냅샷 동기화, STOP 및 봇 주문 취소 요청을 구현합니다. 취소 요청 성공을 최종 취소로 간주하지 않습니다. 테스트는 가짜 브로커를 사용합니다.

토스 공식 명세에서 clientOrderId 멱등성 보장 기간은 10분입니다. 조회 목록에는 clientOrderId가 포함되지 않으므로 응답 유실 시 주문 ID 없이 완전한 자동 대조를 보장할 수 없습니다. 주문 속성/시간만으로 추측해 연결하거나 재전송하지 않습니다. unknown 주문은 수동 대조가 필요합니다.

토스 실주문과 실주문 취소는 **차단**되어 있습니다. `TossReadOnly`는 실계좌 정보를 조회하지만 돈을 움직이지 않습니다. 토스 계좌 테스트를 위해 Alpaca 반복 실행을 종료할 필요는 없으나, 별도의 프로젝트 폴더 PowerShell 창에서 다음을 실행하세요:

```powershell
$env:TOSS_CLIENT_ID = '토스_client_id'
$env:TOSS_CLIENT_SECRET = '토스_client_secret'
.\.venv\Scripts\python.exe -m stockbot.toss
```

여러 계좌가 있으면 `TOSS_ACCOUNT_SEQ`를 본인이 선택한 값으로 설정해야 합니다. 공식 WTS 설정 > Open API에서 자격증명과 허용 IP를 관리하세요. Alpaca API 키와 다릅니다. 토큰 재발급 시 같은 client의 이전 토큰이 무효화되므로 한 client를 여러 프로그램에서 공유하지 마세요.

출력은 연결 상태, 보유종목 수와 API 범위 내 미체결 주문 수만 포함합니다. 토스 API 계좌 통신은 사용자 키 없이 검증하지 못했습니다. API가 조회하지 못하는 주문 종류와 조건주문을 포함한 전체 계좌 위험, 손절/익절 보호, 신호 연결, 주문 실행 경로는 후속 구현·검증 대상입니다.

공식 명세: https://openapi.tossinvest.com/openapi-docs/latest/openapi.json
개발자 안내: https://developers.tossinvest.com/docs
