import unittest


class Ship:
    
    def __init__(self, dimension, head, tail):
        self._dim = dimension
        self._head = head
        self._tail = tail
    
    @property
    def head(self):
        return self._head
    
    @property
    def tail(self):
        return self._tail
    
    def isShapeAlright(self):
        '''
        Verifies if the shape of the ship is alright
        Returns true if it is ok, and false otherwise
        '''
        if self._head[0] != self._tail[0] and self._head[1] != self._tail[1]:
            return False #head and tail are not on the same column or line
        if self._head[0] == self._tail[0] and abs(self._head[1] - self._tail[1]) != self._dim -1 :
            return False 
        if self._head[1] == self._tail[1] and abs(self._head[0] - self._tail[0]) != self._dim -1 :
            return False 
        return True
    
    def isShipInsideBoard(self):
        '''
        Verifies if the ship is inside the board
        Retruns true if it is, and false otherwise
        '''
        if self._head[0] < 0 or self._head[0] > 7 or self._head[1] < 0 or self._head[1] > 7 or self._tail[0] < 0 or self._tail[0] > 7 or self._tail[1] < 0 or self._tail[1] > 7:
            return False
        return True
    
    def getAllPoints(self):
        '''
        Returns a list of all points of a ship - a list of lists
        '''
        lst = []
        if self._head[0] == self._tail[0]:
            
            if self._head[1] < self._tail[1]:
                for i in range(self._head[1], self._tail[1]+1):
                    lst.append([self._head[0], i])
            
            elif self._head[1] > self._tail[1]:
                for i in range(self._tail[1], self._head[1]+1):
                    lst.append([self._head[0],i])
        
        elif self._head[1] == self._tail[1]:
            
            if self._head[0] < self._tail[0]:
                for i in range(self._head[0], self._tail[0]+1):
                    lst.append([i,self._head[1]])
            
            elif self._head[0] > self._tail[0]:
                for i in range(self._tail[0], self._head[0]+1):
                    lst.append([i, self._head[1]])
                    
        return lst
        
class shipTest(unittest.TestCase):
    
    def testShip(self):
        s = Ship(4, [0,0],[0,3])
        self.assertEqual(s.getAllPoints(), [[0,0],[0,1],[0,2],[0,3]])    
        self.assertEqual(s.isShapeAlright(), True)
        self.assertEqual(s.isShipInsideBoard(), True)
        s2 = Ship(3, [0,1],[2,1])
        self.assertEqual(s2.getAllPoints(),[[0,1],[1,1],[2,1]])   
        self.assertEqual(s2.isShapeAlright(), True)
        self.assertEqual(s2.isShipInsideBoard(), True)
        
        s3 = Ship(3, [0,6],[0,8])
        self.assertEqual(s3.isShapeAlright(), True)
        self.assertEqual(s3.isShipInsideBoard(), False)
        