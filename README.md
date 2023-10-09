# Python-Chess

## Django
- codespace 로 웹 서버 띄우기 가능
- ui 는 html 로 구현

### 변경사항 생겼을시
```
python manage.py migrate
python runserver
```

## Pieces
- [ ] 자기가 움직일 수 있는 범위인가

## Board
- [x] 기물 배치
- [ ] 기물 이동

### 기물 배치
- [x] 체스 룰에 맞게 기물을 배치
- [x] 비어 있는 칸은 NonePiece 를 배치

### 기물 이동
- [x] 움직일 기물과 움직일 위치의 좌표를 입력 받아 이동
- [ ] 움직일 기물이 NonePiece 면 안됨
- [ ] 움직일 기물이 움직일 위치로 이동할 수 있는 범위여야함
- [ ] 움직일 기물이 이동하는 거리는 NonePiece 여야함
- [ ] 움직일 기물이 움직일 위치에 같은팀 기물이 있으면 안됨

## Screen
- [x] Board 를 사용자가 볼수 있게 출력
- [x] 움직일 기물과 움직일 위치의 좌표를 사용자로 부터 입력 받음

## Test
- [X] 테스트 코드 실행시 src/main 디렉토리에 접근하지 못함
- [X] 임시로 아래 코드를 모든 테스트 파일에 작성하여 해결함
``` 
import sys
sys.path.append("./src/main/chess")
```
- [X] 추후 리펙토링 필요
- `PYTHONPATH` 환경변수를 추가하여 해결
