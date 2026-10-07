# 한국 모의투자 연결 (1단계)

요구사항: 미국과 한국 주식을 모두 사용하되, 한국은 모의투자부터 연결한다.

이 버전은 미국 Alpaca 모의매매와 한국투자증권 KIS 국내주식 모의계좌 인증·잔고·보유종목 조회를 제공합니다. 한국 자동주문, 후보조회, 미체결 주문조회, 한국 백테스트는 아직 제공하지 않습니다. 한국 시장에서 해당 버튼을 누르면 안내를 표시하며 미국 주문을 실행하지 않습니다.

## 준비

1. https://apiportal.koreainvestment.com 에서 한국투자증권 Open API 이용 절차와 모의투자 신청을 확인합니다.
2. KIS 국내주식 모의투자 계좌와 모의투자용 App Key / App Secret을 준비합니다. Alpaca 키는 사용할 수 없습니다.
3. 모의계좌 번호 앞 8자리와 뒤 2자리(계좌상품코드)를 준비합니다.

## 실행

1. ZIP을 새 폴더에 모두 추출합니다. 최초 setup-gui.bat, 이후 start-gui.bat를 실행합니다.
2. 우측 상단에서 `한국 · KIS`를 선택합니다.
3. `API 연결`에서 네 항목을 입력하고 `연결 확인`을 누릅니다.
4. 총 자산·예수금은 원화로, 보유종목은 국내 종목코드로 표시됩니다.
5. `계좌 새로고침`으로 갱신합니다. 매수 가능 금액·전일 손익은 별도 조회 미구현이므로 `미조회`입니다. 미체결 주문은 조회하지 않았으므로 빈 표를 무주문으로 해석하지 마세요.
6. 미국 시장으로 돌아가면 기존 Alpaca 모의매매를 사용할 수 있습니다. 처리 중·미국 자동매매 실행 중에는 시장을 변경할 수 없습니다.

키·계좌·접근토큰은 파일에 저장하지 않습니다. KIS 토큰은 실행 중 재사용하며 만료 전에 갱신합니다. 전체 잔고 연속조회가 실패하면 부분 잔고를 표시하지 않습니다. KIS 실전 서버나 주문 API는 이 연결에서 호출하지 않습니다.

## 검증 범위

기존 테스트와 추가 테스트 26개 통과. KIS 응답을 대체한 인증·토큰 재사용·잔고 연속조회·오류·시장별 라우팅 검증입니다. 사용자 KIS 키가 없으므로 실제 모의서버 인증과 Windows에서 새 시장 선택 UI 조작은 아직 검증하지 않았습니다. docs/windows-gui-verification.md의 Windows 검증은 이전 미국 GUI 버전에 대한 기록입니다.

## 공식 참고 자료

- https://github.com/koreainvestment/open-trading-api
- https://github.com/koreainvestment/open-trading-api/blob/main/kis_devlp.yaml
- https://github.com/koreainvestment/open-trading-api/blob/main/examples_user/kis_auth.py
- https://github.com/koreainvestment/open-trading-api/blob/main/examples_llm/domestic_stock/inquire_balance/inquire_balance.py
