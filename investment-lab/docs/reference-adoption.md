# 참고 모음 10 적용

사용자가 승인한 Auto-trading-live-references-10.zip을 읽고 현재 10종목 서버 모의투자에 필요한 일부 동작을 독립 구현했다. 원본 프로젝트 전체 도입·코드 복사는 하지 않았다.

## 확인한 근거
- Lumiwealth/lumibot `tests/test_strategy_asset_backup.py`: 저장 후 재시작 상태 보존 검사, Git blob `625e423f2dec2dd08470e975fa8885784aa360d4`.
- Lumiwealth/lumibot `tests/test_stock_split_accounting.py`: 분할 비율·중복 적용·보정 가격의 이중 반영 검사, Git blob `54986931fe609725bcace8ea6618f31183ddabe6`.
- ZIP source-manifest.json의 SHA-256과 동봉 원문을 대조했다. 원본 lumibot 테스트 자체는 실행하지 않았다. 원본 GPL 코드를 복사하거나 의존성으로 추가하지 않았다.

## 적용 동작
v2 계좌를 처리하기 전과 처리한 후에 현금·수량·가격·평가액의 유한성·범위와 `equity = cash + qty * mark`를 확인한다. 비용·체결량 비율과 손실 제한 설정도 확인한다. 실패하면 종목별 임시 처리 결과를 발행하지 않아 원장을 보존한다. 기존 가격 수정·누락 중단 기능은 유지하고 분할이나 가격 보정을 추측해 자동 변경하지 않는다.

최근 200회 실행의 소요 시간·종목별 오류·연속 오류·복구 전환을 operations-history.json에 저장한다. 상태 파일과 README에서 현재 오류·복구를 확인한다. 외부 알림은 발송하지 않는다.

## 범위
서버 가상 체결 계좌 검사이며 증권사 잔고 대조가 아니다. 가격 수정이 계속 발생하면 원인 조사와 명시적 복구가 필요하다. 참고 묶음 전체 545개 소스를 통합하거나 실제 증권사 주문을 추가한 것은 아니다.
