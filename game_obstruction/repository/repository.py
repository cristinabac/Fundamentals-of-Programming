from texttable import Texttable


class repo:

    def __init__(self):
        self._data = []
        for i in range (0,6):
            lst = []
            for j in range(0,6):
                lst.append(' ')
            self._data.append(lst)

    def isPointInside(self,x,y):
        if x not in [0,1,2,3,4,5] or y not in [0,1,2,3,4,5]:
            return False
        return True

    def isPointFree(self,x,y):
        if self._data[x][y] == ' ':
            return True
        return False

    def getFreePoints(self):
        res = []
        for i in range(0,6):
            for j in range(0,6):
                if self._data[i][j] == ' ':
                    res.append([i,j])
        return res


    def getNeighbours(self,x,y):
        lst = [[x+1,y],[x+1,y+1],[x+1,y-1],[x-1,y],[x-1,y-1],[x-1,y+1],[x,y-1],[x,y+1]]
        res = []
        for p in lst:
            if self.isPointInside(p[0],p[1]) == True:
                res.append(p)
        return res

    def mark(self,x,y,symbol):
        self._data[x][y] = symbol
        res = self.getNeighbours(x,y)
        for p in res:
            self._data[p[0]][p[1]] = '-'

    def __str__(self):

        board = Texttable()
        for i in range(0,6):
            lst = []
            for j in range(0,6):
                lst.append(self._data[i][j])
            board.add_row(lst)

        return board.draw()