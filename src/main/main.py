from board.board import Board

def run():
    board = Board()
    showBoard(board)
    currentPosition, targetPosition = inputMovePostions("움직일 기물의 좌표와 움직일 위치를 입력해주세요. (ex: xy xy)\n")
    board.move(currentPosition, targetPosition)
    showBoard(board)

def showBoard(board):
    for index, pieces in enumerate(board.getBoard()):
        print("{0}| ".format(7 - index) + " ".join(pieces))
    print("   ---------------")
    print("   0 1 2 3 4 5 6 7")

def inputMovePostions(message):
    try:
        currentPosition, targetPosition = input(message).split(" ")
        return toPosition(currentPosition), toPosition(targetPosition)

    except:
        print("")
        print("좌표는 (0, 0) 부터 (7, 7) 까지 있습니다.")
        return inputMovePostions("다시 입력해주세요. (ex: xy xy)\n")
    
def toPosition(positionString):
    if (len(positionString) != 2):
         raise Exception()
    x = int(positionString[0]) 
    y = int(positionString[1])
    if (0 <= x < 8 and 0 <= y < 8):
        return (x, y)
    raise Exception()

run()
