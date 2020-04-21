'''
Created on Dec 29, 2018

@author: hp840
'''
from texttable import Texttable
from domain.ship import Ship
import unittest

class userBoard:
    
    def __init__(self, size):
        self._size = size
        self._data = []
        self._revealed = []
        
        for i in range(self.size):
            self._data.append([0]*self.size)
            self._revealed.append([False]*self.size)
        
    
    def markBattleship(self, battleshipList):
        '''
        Marks the battleship on the user's board
        Input - battleshipList - the list of all points of the battleship
        '''
        for i in battleshipList:
            self._setShip(i[0],i[1],"B")
    
    def markCruiser(self, cruiserList):
        '''
        Marks the cruiser on the user's board
        Input - cruiserList - the list of all points of the cruiser
        '''
        for i in cruiserList:
            self._setShip(i[0],i[1],"C")
            
    def markDestroyer(self, destroyerList):
        '''
        Marks the destroyer on the user's board
        Input - destroyerList - the list of all points of the destroyer
        '''
        for i in destroyerList:
            self._setShip(i[0],i[1],"D")
    
    @property
    def size(self):
        return self._size   
    
    def finished(self):
        '''
        Returns True if the game is finished (the computer won, because all user's ships were destroyed), and False otherwise
        '''
        finish = True
        for x in range(0,8):
            for y in range(0,8):
                if self._revealed[x][y] == False and self._data[x][y]!=0:
                    finish = False
        return finish
    
    def _setShip(self,x,y,symbol):
        '''
        Sets a point of a ship
        Input : x - the line of the point
                y - the column of the point
                symbol - the symbol of the ship to be put on the board
        '''
        self._data[x][y] = symbol
    
    def shipOverlap(self, ship):
        '''
        Verifies if a ship overlaps with another ship already existent on the board
        '''
        lst = ship.getAllPoints() 
        for point in lst:
            if self._data[point[0]][point[1]] != 0:
                return True #it overlaps
        return False
    
    def __str__(self):
        t = Texttable()
        
        #Build row header
        res = [' ','A']
        i = self.size-1
        while i>0:
            res.append(chr(ord(res[-1]) + 1)) #We put the letters A,B,C,... on the first row as a header, this appears only at printing the table
            i -=1
        t.header(res)
        
        for i in range(self.size):
            res = []
            for j in range(self.size):
                if self._revealed[i][j] == True:
                    res.append(self._data[i][j])
                else:
                    res.append("?")
            t.add_row( [i+1] + res)  
        return t.draw()

    
    def str(self):
        t = Texttable()
        
        #Build row header
        res = [' ','A']
        i = self.size-1
        while i>0:
            res.append(chr(ord(res[-1]) + 1))
            i -=1
        t.header(res)
        
        for i in range(self.size):
            t.add_row( [i+1] + self._data[i])
        return t.draw()
    
    
class testUserBoard(unittest.TestCase):
    
    def setUp(self):
        self.board = userBoard(8)
        self.board.markBattleship([[0,0],[0,1],[0,2],[0,3]])
        self.board.markCruiser([[1,0],[1,1],[1,2]])
        self.board.markDestroyer([[2,3],[3,3]])
        
    def testData(self):
        self.assertEqual(self.board._data,[["B","B","B","B",0,0,0,0],["C","C","C",0,0,0,0,0],[0,0,0,"D",0,0,0,0],[0,0,0,"D",0,0,0,0],[0,0,0,0,0,0,0,0],[0,0,0,0,0,0,0,0],[0,0,0,0,0,0,0,0],[0,0,0,0,0,0,0,0]])
        
    def testFinished(self):
        self.assertEqual(self.board.finished(),False)
        self.board._revealed[0][0] = True
        self.board._revealed[0][1] = True
        self.assertEqual(self.board.finished(),False)
        self.board._revealed[0][2] = True
        self.board._revealed[0][3] = True
        self.assertEqual(self.board.finished(),False)
        self.board._revealed[1][0] = True
        self.board._revealed[1][1] = True
        self.assertEqual(self.board.finished(),False)
        self.board._revealed[1][2] = True
        self.board._revealed[2][3] = True
        self.board._revealed[3][3] = True
        self.assertEqual(self.board.finished(),True)
        
        
    def testShipOverlap(self):
        ship = Ship(2, [0,0],[0,1])
        self.assertEqual(self.board.shipOverlap(ship), True)
        ship2 = Ship(3, [0,3],[0,5])
        self.assertEqual(self.board.shipOverlap(ship2), True)
        ship3 = Ship(4, [5,0],[5,3])
        self.assertEqual(self.board.shipOverlap(ship3), False)
