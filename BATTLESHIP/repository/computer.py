'''
Created on Dec 29, 2018

@author: hp840
'''

from texttable import Texttable
import random
import unittest

class computerBoard:
    
    def __init__(self, size):
        self._size = size
        self._data = []
        self._revealed = []
        
        for i in range(self.size):
            self._data.append([0]*self.size)
            self._revealed.append([False]*self.size)
        
        self._setShip(2,"D")
        self._setShip(3,"C")
        self._setShip(4,"B")
        
    @property
    def size(self):
        return self._size   
    
    def _setShip(self, dimension, symbol):
        '''
        Sets a random ship
        Input: dimension - the dimension of the ship
               symbol - the symbol to be placed on the board
        '''
        valid = False
        while valid == False:
            x = random.randint(0,7)
            y = random.randint(0,7)
            o = random.randint(0,1)
            if o == 0:
                orientation = "vertical"
            else:
                orientation = "horizontal"
            
            valid = self._validate(dimension, x, y, orientation)
        
        self._placeShip(dimension, x,y, orientation,symbol)
    
    def _validate(self, dim,x,y,orientation):
        '''
        Validates a ship
        Input : dim - the dimension of the ship
                x - the line of the head
                y - the column of the head
                orientation - vertical or horizontal (the way the ship is oriented)
        Output : True or False
        '''
        if orientation == "vertical" and x+dim > self.size:
            return False
        elif orientation == "horizontal" and y+dim > self.size:
            return False
        else:
            if orientation == "vertical":
                for i in range(dim):
                    if self._data[x+i][y]!=0:
                        return False
            elif orientation == "horizontal":
                for i in range(dim):
                    if self._data[x][y+i]!=0:
                        return False
        return True
    
    def _placeShip(self,dim,x,y,orientation, symbol):
        '''
        Places a ship on the board
        Input : dim - the dimension of the ship
                x - the line of the head
                y - the column of the head
                orientation - vertical or horizontal (the way the ship is oriented)
                symbol - the symbol of the ship to be put on the board
        '''
        if orientation == "vertical":
                for i in range(dim):
                    self._data[x+i][y] = symbol
        elif orientation == "horizontal":
                for i in range(dim):
                    self._data[x][y+i] = symbol
  
    def finished(self):
        '''
        Returns True if the game is finished (the user won, because all computer's ships were destroyed), and False otherwise
        '''
        finish = True
        for x in range(0,8):
            for y in range(0,8):
                if self._revealed[x][y] == False and self._data[x][y]!=0:
                    finish = False
        return finish
    
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
    
    
class testComputerUnit(unittest.TestCase):
    
    def test(self):
        
        cb = computerBoard(8)
        self.assertEqual(cb.size, 8)
        self.assertEqual(cb._validate(2, 0, 0, "vertical"), True)
        self.assertEqual(cb._validate(2, 0, 0, "horizontal"), True)
        self.assertEqual(cb._validate(4, 0, 5, "horizontal"), False)
        self.assertEqual(cb._validate(2, 7, 0, "vertical"), False)
        
        self.assertEqual(cb.finished(), False)
        for i in range(0,8):
            for j in range(0,8):
                cb._revealed[i][j] = True
        self.assertEqual(cb.finished(), True)
