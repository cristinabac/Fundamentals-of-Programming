'''
Created on Dec 29, 2018

@author: hp840
'''
from controller.gameController import Game
from domain.ship import Ship
from repository.user import userBoard

class Ui:
    def __init__(self, game):
        self._game = game
    
    def encodeLetter(self,y):
        y = y.upper()
        
        if y == "A":
            y = 0
        if y == "B":
            y = 1
        if y == "C":
            y = 2
        if y == "D":
            y = 3
        if y == "E":
            y = 4
        if y == "F":
            y = 5
        if y == "G":
            y = 6
        if y == "H":
            y = 7
        return y
    
    def readPoint(self):
        x = input("Give line: ")
        y = input("Give column: ")
        if x not in ["1","2","3","4","5","6","7","8"]:
            print("Line not valid")
            return None
        if y not in ["A","B","C","D","E","F","G","H","a","b","c","d","e","f","g","h"]:
            print("Column not valid")
            return None
        y = self.encodeLetter(y)
        x = int(x) - 1
        return [x,y]
    
    def readShip(self, dim):
        while True:
            print("Give coords of the head:")
            head = self.readPoint()
            if head != None:
                print("Give coords of the tail:")
                tail = self.readPoint()
                
                while tail == None:
                    print("Give coords of the tail:")
                    tail = self.readPoint()
                
                ship = Ship(dim, head, tail)
                return ship
    
    def readShipAndVerify(self, dim):
        b = self.readShip(dim)
        while b.isShapeAlright() == False or b.isShipInsideBoard()== False:
            if b.isShapeAlright() == False:
                print("The shape of your ship is not alright")
            if b.isShipInsideBoard() == False:
                print("The ship is not inside the board")
            b = self.readShip(dim)
        
        return b
    
    def putPlayerShips(self):
        print("The battleship (dimension 4) :")
        b = self.readShipAndVerify(4)
        battleship_lst = b.getAllPoints()
        self._game.userBoard.markBattleship(battleship_lst)
        
        ok = False
        while ok == False:
            print("The cruiser (dimension 3) :")
            c = self.readShipAndVerify(3)
            cruiser_lst = c.getAllPoints()
            if self._game.userBoard.shipOverlap(c) == True:
                print("The cruiser overlaps with another ship!")
            else:
                ok = True
                self._game.userBoard.markCruiser(cruiser_lst)
        
        ok = False
        while ok == False:
            print("The destroyer (dimension 2) :")
            d = self.readShipAndVerify(2)
            destroyer_lst = d.getAllPoints()
            if self._game.userBoard.shipOverlap(d) == True:
                print("The destroyer overlaps with another ship!")
            else:
                ok = True
                self._game.userBoard.markDestroyer(destroyer_lst)
            
        
    def checkOverlap(self, ship):
        lst = ship.getAllPoints()
        for point in lst:
            if self._game.userBoard._data[point[0]][point[1]] != 0:
                return False
        return True
    
    
    def readMove(self):
        print("Enter move : ")
        while True:
            lst = self.readPoint()
            if lst != None:
                return lst[0],lst[1]
        
    
    def start(self):
        
        b = userBoard(8)
        print(b.str())
        
        print("\n")
        print("It's time to put your ships on your board!")
        print("\n")
        self.putPlayerShips()
        
        cb = self._game.computerBoard
        ub = self._game.userBoard
        
        
        
        playerTurn = True
        
        while cb.finished() == False and ub.finished() == False:

            if playerTurn:
                print("------------COPUTER BOARDS-----------")
                print(cb.str())
                print(cb)
                print("-------------YOUR BOARDS-------------")
                print(ub.str())
                print(ub)
                x,y = self.readMove()
                self._game.humanMove(x,y)
            else:
                #self._game.computerRandomMove()
                self._game.computerMove()
            
            playerTurn = not playerTurn
            
        if cb.finished() == True:
            print("-----------------")
            print("Congratulations!")
            print("You won!")
            print("----------------")
            print("------------COPUTER BOARDS-----------")
            print(cb.str())
            print(cb)
            print("-------------YOUR BOARDS-------------")
            print(ub.str())
            print(ub)
        elif ub.finished() == True:
            print("---------")
            print("GAME OVER")
            print("You lost!")
            print("---------")
            print("------------COPUTER BOARDS-----------")
            print(cb.str())
            print(cb)
            print("-------------YOUR BOARDS-------------")
            print(ub.str())
            print(ub)