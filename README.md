# Python-Chess

## 실행 전 사전 작업
- `/python-chess-ai/src/main` 를 PYTHONPATH 환경변수로 설정해야 합니다.

Linux:
```
export PYTHONPATH='(python-chesss-ai 디렉토리가 위치한 경로)/python-chess-ai/src/main'
```

- 해당 명령어를 통해 `django` 와 `rest_framework` 를 설치해주세요.
```
pip install django
pip install djangorestframework
```

- 다음과 같이 `alias` 를 설정해주면 간편하게 코드를 실행 시킬 수 있어요.
```
alias pyma='python src/main/server/manage.py'
alias pyrun='python src/main/chess/main.py'
alias pytest='python -m unittest -v src/test/*/*/*Test.py'
```

- 서버를 처음 띄울땐 해당 명령어를 입력해주세요.
```
python manage.py makemigrations
python manage.py migrate
python manage.py runserver
```

## 용어 사전
|용어|종류|설명|
|---|---|------|
|Piece|클래스|체스 기물들의 기본이 되는 데이터를 가지는 객체|
|NonePiece|클래스|체스 기물이 없는 위치를 나타내기 위한 객체|
|Board|클래스|체스 기물들이 움직이는 장소|
|Screen|클래스|Board 를 화면에 출력해주거나 기물을 움직이기 위해 입력한 값을 받아오는 객체|
|config|디렉토리|django 에 대해 설정하는 디렉토리|
|home|디렉토리|체스 게임을 할 수 있게 html 을 띄워주는 웹 서버|
|chess_api|디렉토리|체스 게임을 돌리며 데이터를 주고 받는 api 서버|

## Ai
- [x] 랜덤한 기물을 고르고 해당 기물이 갈 수 있는 위치중 하나를 랜덤으로 골라 이동
- [ ] 의미있는 기물을 움직이기
- [ ] 의미있는 위치로 움직이기

## UI
- [ ] UI 코드가 더럽고 중복되는 코드가 많아 리펙토링 필요
- [ ] 흰색과 검은색을 ai 와 player 중 선택할 수 있기
- [ ] ai 로 설정된 색을 undo 할 경우 움직일 위치 재요청 하기

### UI 리펙토링
- [ ] request 요청 보내는 함수만 모아둔 js 파일 만들기
