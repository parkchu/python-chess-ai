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
        x = positionString[0]
        y = positionString[1]
        if ('a' <= x <= 'h' and '1' <= y <= '8'):
            return positionString
        raise Exception()
    