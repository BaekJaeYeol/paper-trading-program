# Windows 인증정보 저장 및 앱 내 업데이트 (v0.4.0)

## 사용 방법

이 버전은 처음 한 번 ZIP을 받아 압축을 푼다. 앞으로 같은 폴더의 `TossTrading.cmd`를
더블클릭해 실행한다. Python 3.11 이상과 기존 Windows tzdata 설치를 사용한다.
처음 실행이 안 되면 기존처럼 `python -m pip install -e .`를 실행한다.
기존 프로젝트의 config/state를 덮어쓰거나 옮기지 않는다. 기존 폴더를 삭제하지 않는다.
바탕화면에 TossTrading.cmd의 바로가기를 만들어도 된다.

`API 보안 저장·삭제`에서 ID/Secret을 입력해 저장하거나, 인증정보를 입력했던
PowerShell에서 `python start_toss.py`로 열어 `현재 PowerShell 값 저장`을 누른다.
저장은 계좌 연결 검사가 아니므로 이후 `토스 연결·새로고침`으로 계좌를 확인한다.
저장 성공 후 PowerShell을 닫아도 동일 Windows 사용자/PC의 다음 실행에서 불러온다.
저장된 완전한 인증 묶음이 환경변수보다 우선하며 서로 다른 출처의 ID/Secret을 섞지 않는다.

`업데이트 확인` → 새 버전이 있으면 버전을 확인하고 설치 → 창을 닫고
`TossTrading.cmd`로 재실행한다. 직접 `python -m stockbot.toss_gui`로 실행하면
그 폴더의 원본 코드가 선택되므로 관리형 업데이트가 적용되지 않는다.
`이전 버전 복구`도 다음 실행부터 적용된다. 최신 버전 확인은 버튼을 눌렀을 때만 수행한다.
현재 버전이 이미 최신이면 설치하지 않는다. 미래 버전을 아직 배포하지 않았으면 업데이트가 없다.

## 저장 방식과 제한

ctypes로 Windows CredWriteW/CredReadW/CredDeleteW를 사용한다. Generic credential 하나에
ID/Secret/계좌 선택 값을 묶어 저장하며 CRED_PERSIST_LOCAL_MACHINE(동일 사용자·이 PC의
이후 로그온 세션)을 사용한다. 설정 파일·로그·GitHub·업데이트 요청에는 비밀키를 넣지 않는다.
저장 내용을 화면에 다시 채워 넣지 않고 입력은 마스킹한다. 삭제 시 앱 내 환경변수도 지운다.
원래 부모 PowerShell 환경변수는 앱에서 삭제할 수 없으므로 해당 창을 닫아야 한다.
같은 Windows 사용자로 실행되는 다른 프로그램이나 침해된 PC로부터의 보호를 보장하지 않는다.
Python의 임시 문자열 메모리가 모두 즉시 지워진다는 보장도 없다.

업데이트는 고정 저장소 BaekJaeYeol/paper-trading-program의 main/desktop-channel.json만
확인한다. 메타데이터는 테스트 완료된 불변 커밋과 버전을 가리켜야 한다. 실행 모드는
`schema=1`, `python=3.11+`, `mode=toss-read-only`만 허용한다.
커밋에 고정한 src/stockbot의 평면 Python 파일만 받고 크기·이름·중복·Git blob SHA를
검사한 뒤 AST 문법을 검사한다. 다운로드 중 코드를 실행하지 않는다. HTTPS GitHub 원본을
신뢰하며 별도 독립 코드 서명은 없다. 미래 의존성/폴더/실거래 모드 변경은 이 채널에서
자동 지원하지 않는다. 배포 담당자는 호환되는 의존성을 유지해야 한다.

설치는 LOCALAPPDATA/BaekJaeYeolStockbot/versions/<commit>/src에 준비하고 원자적인
current.json 포인터로 다음 실행 버전을 선택한다. 이전 실행 버전 포인터를 보관한다.
파일 잠금은 프로세스 종료 시 OS가 해제하며, 다운로드·디스크·포인터 쓰기 실패 시
기존 활성 포인터는 유지된다. 준비된 고아 버전은 재검증 후 재시도할 수 있다.
현재/이전 코드 폴더와 Windows 인증 저장소는 서로 분리되어 업데이트/복구 시 키가 유지된다.
현재 프로세스의 코드를 실행 중 덮어쓰지 않는다. 네트워크는 최대 4개 병렬·파일별 20초 제한, 전체는
요청 전후 120초 예산 검사이며 진행 중 요청을 120초 정각에 강제 중단하지는 않는다.
창을 닫아 설치가 중단되면 아직 전환하지 않은 버전은 활성화되지 않는다.

안정 실행기는 새 GUI의 0.5초 이벤트 루프 신호를 최대 30초 기다린다. 시작 실패 시
이전 버전으로 한 번 복구·재실행한다. 이 신호는 계좌 API나 모든 기능의 정상 동작을
검증하지 않는다. 창이 열린 뒤 런타임 문제가 나면 수동 복구를 사용한다.
실행기 파일 자체는 자동 업데이트하지 않으므로 보관하고, 프로토콜 변경 시 별도 배포가 필요하다.
업데이트/복구가 매매를 시작하지 않으며 실제 주문·취소는 계속 차단한다.

## 배포 절차

1. updater.VERSION과 pyproject 버전을 올리고 호환성/오프라인/Windows 테스트를 실행한다.
2. 기능 PR의 정확한 head에서 tests와 Windows GUI verification 성공을 확인하고 병합한다.
3. main의 desktop-channel.json을 그 테스트 완료 커밋 SHA와 새 버전으로 갱신하는 별도 PR을 만든다.
4. 채널 스키마·해당 커밋 파일 다운로드 검증 후 채널 PR을 병합한다.
5. 사용자는 앱의 업데이트 확인으로 배포된 버전을 받는다. 단순 main 변경이 자동 배포되는 것은 아니다.

Figma 쓰기 한도 때문에 실제 Figma 파일은 제작하지 않았다. 기존 조회 창의 보조 버튼과
인증정보 모달, 업데이트 버전 확인 대화상자, 진행·실패·재실행 안내로 흐름을 구성했다.
테스트는 fixture 기반 업데이트 손상·실패·복구 및 새 프로세스 시작을 검사한다.
Windows CI에서는 실제 Credential Manager 저장/교체/새 Python 프로세스 조회/삭제를
일회성 테스트 항목으로 검증하고 정리하며, 실제 Tk 창에서 마스킹·저장·삭제·업데이트
취소/설치/실패 표시를 검사한다. 사용자 PC의 실제 API 재접속 및 미래 버전 운용은 별도 검증이다.

공식 근거:
https://learn.microsoft.com/en-us/windows/win32/api/wincred/nf-wincred-credwritew
https://learn.microsoft.com/en-us/windows/win32/api/wincred/ns-wincred-credentialw
https://docs.github.com/en/rest/repos/contents
