import random


class game:

    def __init__(self,board):
        self._board = board


    def computerMove(self):
        ok = True
        while ok == True:
            x = random.randint(0,5)
            y = random.randint(0,5)
            if self._board.isPointFree(x,y) == True:
                ok = False
        z = random.randint(0,2)
        if z == 0:
            self._board.mark(x,y,'O')
            print("AI:(" + str(x+1) + "," + str(y+1) + ",O)" )
        else:
            self._board.mark(x, y, 'X')
            print("AI:(" + str(x + 1) + "," + str(y + 1) + ",X)")

    def humanMove(self,x,y, symbol):
        self._board.mark(x, y, symbol)
        print("AI:(" + str(x + 1) + "," + str(y + 1) + "," + symbol + ")")


    def finished(self):
        if self._board.finish_computerWin() == True:
            return True
        if self._board.finish_humanWin() == True:
            return None
        return False


    def showBoard(self):
        print(self._board)