# Python-Chess

## Pieces
- 움직일 수 있는 위치

## Board
- 기물 배치
- 기물 이동

## Test
- 테스트 코드 실행시 src/main 디렉토리에 접근하지 못함
- 임시로 아래 코드를 모든 테스트 파일에 작성하여 해결함
``` 
import sys
sys.path.append("./src/main")
```
- 추후 리펙토링 필요