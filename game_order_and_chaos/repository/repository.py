from texttable import Texttable
import unittest

class board:

    def __init__(self):
        self._data = []
        for i in range(0,6):
            lst = []
            for i in range(0,6):
                lst.append(' ')
            self._data.append(lst)

    def inPointInside(self,x,y):
        if x not in [0,1,2,3,4,5] or y not in [0,1,2,3,4,5]:
            return False
        return True

    def mark(self,x,y,symbol):
        self._data[x][y] = symbol

    def isPointFree(self,x,y):
        if self._data[x][y] == ' ':
            return True
        return False

    def finish_computerWin(self):
        contor = 0
        for i in range(0,6):
            for j in range(0,6):
                if self._data[i][j] != ' ':
                    contor += 1
        if contor == 36:
            return True
        return False

    def storeToFile(self, filename):
        f = open(filename,"w")
        for i in range(0,6):
            for j in range(0,6):
                if self._data[i][j] == ' ':
                    f.write('-')
                else:
                    f.write(self._data[i][j])
        f.close()

    def loadFromFile(self, filename):
        f = open(filename,"r")
        line = f.readline().strip()
        c = 0
        for i in range(0,6):
            for j in range(0,6):
                if line[c] == '-':
                    self._data[i][j] = ' '
                else:
                    self._data[i][j] = line[c]
                c += 1
        f.close()

    def finish_humanWin(self):
        #verify lines
        for i in range(0,6):
            str = ''
            for j in range(0,6):
                str = str + self._data[i][j]
            if 'XXXXX' in str or 'OOOOO' in str:
                return True

        #verify columns
        for j in range(0,6):
            str = ''
            for i in range(0,6):
                str = str + self._data[i][j]
            if 'XXXXX' in str or 'OOOOO' in str:
                return True

        #verify diagonals
        #DP
        str = ''
        for i in range(0,6):
            str = str + self._data[i][i]
        if 'XXXXX' in str or 'OOOOO' in str:
            return True

        #DS
        str = ''
        for i in range(0, 6):
            str = str + self._data[i][5-i]
        if 'XXXXX' in str or 'OOOOO' in str:
            return True

        #restul diagonalelor...
        #paralele cu DP
        str = ''
        for i in range(1,6):
            str = str + self._data[i][i-1]
        if 'XXXXX' in str or 'OOOOO' in str:
            return True

        str = ''
        for i in range(0, 5):
            str = str + self._data[i][i + 1]
        if 'XXXXX' in str or 'OOOOO' in str:
            return True


        #paralele cu DS
        str = ''
        for i in range(1, 6):
            str = str + self._data[i][6-i]
        if 'XXXXX' in str or 'OOOOO' in str:
            return True

        str = ''
        for i in range(0, 5):
            str = str + self._data[i][4-i]
        if 'XXXXX' in str or 'OOOOO' in str:
            return True

        return False



    def __str__(self):

        t = Texttable()

        for i in range(0,6):
            lst = []
            for j in range(0,6):
                lst.append(self._data[i][j])
            t.add_row(lst)

        return t.draw()


class testUnit(unittest.TestCase):

    def test(self):

        b = board()
        self.assertEqual(b.finish_humanWin(),False)
        b.mark(0,0,'X')
        b.mark(0, 1, 'X')
        b.mark(0, 2, 'X')
        b.mark(0, 3, 'X')
        b.mark(0, 4, 'X')
        self.assertEqual(b.finish_humanWin(), True)
        b.mark(0, 4, 'O')

        b.mark(1, 0, 'O')
        b.mark(2, 1, 'O')
        b.mark(3, 2, 'O')
        b.mark(4, 3, 'O')
        b.mark(5, 4, 'O')
        self.assertEqual(b.finish_humanWin(), True)


        b2  = board()
        self.assertEqual(b2.finish_humanWin(), False)
        b2.mark(0, 4, 'O')
        b2.mark(1, 3, 'O')
        b2.mark(2, 2, 'O')
        b2.mark(3, 1, 'O')
        b2.mark(4, 0, 'O')
        self.assertEqual(b2.finish_humanWin(), True)

        self.assertEqual(b2.isPointFree(0,4),False)
        self.assertEqual(b2.isPointFree(0, 5), True)