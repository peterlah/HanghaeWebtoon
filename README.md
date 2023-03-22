# Sailing-Article-10
항해 10조 토이프로젝트

조원 : 김보슬님, 나상우님, 전우상님

# 파이썬 venv 만들기 및 활성화
# 만들기
python -m venv venv

# 활성화
source venv/Scripts/activate

# 비활성화
deactivate

# UnicodeDecodeError: 'cp949' codec can't decode byte 0xeb in position 16: illegal multibyte sequence
set PYTHONUTF8=1
# 설정후 새로운 터미널창 오픈 -> 또는 환경 변수 등록

# pip update
python.exe -m pip install --upgrade pip

# requests 패키지 -> web에 GET, POST 요청 위해 사용
pip install requests

# flask 설치 -> 웹 개발 용도
pip install flask

# bs4 패키지 -> 웹크롤링 패키지
pip install bs4

# pymongo, dnspython 패키지 -> MongoDB 사용을 위한 패키지
pip install pymongo dnspython

# 패키지 삭제
pip uninstall requests

** 파이썬 파일 생성시 import 하는 모듈명과 동일한 이름을 사용하면 문제 발생

