# Axgate Snort Automation TEST
Github Action의 self-hosted Runner 기능 사용을 위한 사전 환경 구성 작업이 필요함.

1. Github의 Repository로 이동 -> Setting -> Actions-Runners -> New self-hosted runner 추가

    참조 : https://shorturl.at/ajlm7


2. 사용자 PC에서 Powershell 관리자 권한으로 실행 후 Get-ExecutionPolicy로 권한 확인

    -> Restricted 일 경우


     Set-ExecutionPolicy -ExecutionPolicy RemoteSigned 입력 후 A 로 변경 - 이부분은 .bat으로 만들어 수행하게 
5. 파일 명명 규칙이 필요함.
6. pcap path는 C:\Users\AXGATE를 기본으로 하고 폴더 명 정립이 필요함.
