from random import choice



class game:

    def __init__(self, repo):
        self._board = repo


    def showBoard(self):
        print(self._board)

    def finished(self):
        if self._board.getFreePoints() == []:
            return True
        return False

    def humanMove(self,x,y):
        self._board.mark(x,y,'X')

    def computerMove(self):
        points = self._board.getFreePoints()
        p = choice(points)
        self._board.mark(p[0],p[1],'O')


