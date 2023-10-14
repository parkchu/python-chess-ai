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

## Django
- codespace 로 웹 서버 띄우기 가능
- ui 는 html 로 구현

## Pieces
- [x] 자기가 움직일 수 있는 범위인가

## Board
- [x] 기물 배치
- [ ] 기물 이동

### 기물 배치
- [x] 체스 룰에 맞게 기물을 배치
- [x] 비어 있는 칸은 NonePiece 를 배치

### 기물 이동
- [x] 움직일 기물과 움직일 위치의 좌표를 입력 받아 이동
- [x] 움직일 기물이 NonePiece 면 안됨
- [ ] 움직일 기물이 움직일 위치로 이동할 수 있는 범위여야함
- [ ] 움직일 기물이 이동하는 거리는 NonePiece 여야함
- [ ] 움직일 기물이 움직일 위치에 같은팀 기물이 있으면 안됨

## Screen
- [x] Board 를 사용자가 볼수 있게 출력
- [x] 움직일 기물과 움직일 위치의 좌표를 사용자로 부터 입력 받음

## UI
- [x] 기물의 기본적인 움직임 요청 구현
- [x] 기물을 선택하면 해당 기물이 움직일 수 있는 위치 표시
- [x] 움직일 수 없는 위치일 경우 이동 요청 보내지 않음
- [ ] 캐슬링 요청 구현
- [ ] 폰 프로모션 요청 구현
- [ ] Response 로 Board 를 받으면 그거에 맞게 화면 그리기
- [ ] 게임 끝날 경우
- [ ] 차례에 맞는 기물만 움직일 수 있다.

## Test
- [X] 테스트 코드 실행시 src/main 디렉토리에 접근하지 못함
- [X] 임시로 아래 코드를 모든 테스트 파일에 작성하여 해결함
``` 
import sys
sys.path.append("./src/main/chess")
```
- [X] 추후 리펙토링 필요
- `PYTHONPATH` 환경변수를 추가하여 해결
