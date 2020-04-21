
import random
import unittest
from repository.computer import computerBoard
from repository.user import userBoard

class Game:
    def __init__(self, cBoard, uBoard):
        self._computerBoard = cBoard
        self._userBoard = uBoard
    
    @property
    def computerBoard(self):
        return self._computerBoard
    
    @property
    def userBoard(self):
        return self._userBoard
    
    def humanMove(self,x,y):
        '''
        Marks the human's move
        Input : x - the line of the point to hit
                y - the column
        '''
        self._computerBoard._revealed[x][y] = True
        if self._computerBoard._data[x][y] == 0:
            print("user - miss")
        else:
            print("user - hit")
    
    def computerRandomMove(self):
        '''
        The computer makes a random move
        '''
        ok = False
        while ok == False:
            x = random.randint(0,7)
            y = random.randint(0,7)
            if self._userBoard._revealed[x][y] == False:
                ok = True
                
        self._userBoard._revealed[x][y] = True
        if self._userBoard._data[x][y] == 0:
            print("computer - miss")
        else:
            print("computer - hit")
    
    def computerSearchHit(self):
        '''
        Search for a point that have already been hit
        Returns one of the point's neighbourhoods (tuple)
        Returns none if there aren't any
        '''
        
        for x in range(0,8):
            for y in range(0,8):
                if self._userBoard._revealed[x][y] == True and self._userBoard._data[x][y] != 0:
                    #search for a neighbour to hit
                    neigh = [(x,y-1),(x-1,y),(x+1,y), (x,y+1)]
                    i = 0
                    while i<len(neigh):
                        loc = neigh[i]
                        
                        if loc[0] not in range(0,8):
                            neigh.pop(i)
                            continue
                        if loc[1] not in range(0,8):
                            neigh.pop(i)
                            continue
                        i += 1
                    
                    random.shuffle(neigh)
                    for point in neigh:
                        if self._userBoard._revealed[point[0]][point[1]] == False:
                            return point
        return None
    
    def computerMove(self):
        '''
        Makes the computer's move
        The move will be random if there are not any points the computer searched to hit
        '''
        point = self.computerSearchHit()
        if point != None:
            self._userBoard._revealed[point[0]][point[1]] = True
            if self._userBoard._data[point[0]][point[1]] == 0:
                print("computer - miss")
            else:
                print("computer - hit")
        else:
            self.computerRandomMove()
            
            
            
class gameTest(unittest.TestCase):
    
    def setUp(self):
        self._computerBoard = computerBoard(8)
        self._userBoard = userBoard(8)
        self._userBoard.markBattleship([[0,0],[0,1],[0,2],[0,3]])
        self._userBoard.markCruiser([[1,0],[1,1],[1,2]])
        self._userBoard.markDestroyer([[2,3],[3,3]])
        self._game = Game(self._computerBoard, self._userBoard)
    
    def testComputerMoves(self):
        self.assertEqual(self._game.computerSearchHit(), None)
        self._userBoard._revealed[5][5] = True 
        self.assertEqual(self._game.computerSearchHit(), None)
        self._userBoard._revealed[0][0] = True 
        self.assertIsNotNone(self._game.computerSearchHit())
        self.assertIn(self._game.computerSearchHit(), [(0,1),(1,0)])
    