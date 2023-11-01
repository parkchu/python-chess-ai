from chess.board.Position import Position

class Screen:

    def showBoard(board):
        for index, pieces in enumerate(board.getBoard()):
            print("{0}| ".format(8 - index) + " ".join(pieces))
        print("   ---------------")
        print("   a b c d e f g h")


    def inputMovePostions(message):
        try:
            currentPosition, targetPosition = input(message).split(" ")
            print("")
            return Screen.checkPosition(currentPosition), Screen.checkPosition(targetPosition)

        except:
            print("")
            print("좌표는 a1 부터 h8 까지 있습니다.")
            return Screen.inputMovePostions("다시 입력해주세요. (ex: xy xy)\n")
        
        
    def checkPosition(positionString):
        if (len(positionString) != 2):
            raise Exception()
        file = positionString[0]
        rank = positionString[1]
        if ('a' <= file <= 'h' and '1' <= rank <= '8'):
            return Position(file, rank)
        raise Exception()
    