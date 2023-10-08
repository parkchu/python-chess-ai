from board.Board import Board
from screen.Screen import Screen

def run():
    board = Board()
    Screen.showBoard(board)
    currentPosition, targetPosition = Screen.inputMovePostions("움직일 기물의 좌표와 움직일 위치를 입력해주세요. (ex: xy xy)\n")
    board.move(currentPosition, targetPosition)
    Screen.showBoard(board)

run()
