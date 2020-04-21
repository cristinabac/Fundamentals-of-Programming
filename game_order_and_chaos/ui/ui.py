

class UI:

    def __init__(self,game):
        self._game = game

    def start(self):
        print(" Start a new game or load from a file a game?")
        s = input("Enter new/load: ")

        if s == 'load':
            filename = input("Enter file name: ")
            self._game._board.loadFromFile(filename)

        while True:



            self._game.showBoard()

            ok = False
            while ok == False:

                try:
                    x = input("Enter the row")
                    y = input("Enter the column")
                    symbol = input("Enter symbol")
                    x = int(x) -1
                    y = int(y)-1
                    ok = True
                except ValueError as e:
                    print("Invalid coordinates")

            self._game.humanMove(x,y,symbol)

            if self._game.finished() == True:
                print("GAME OVER")
                self._game.showBoard()
                return
            if self._game.finished() == None:
                print("CONGRATS! YOU WON!")
                self._game.showBoard()
                return

            self._game.computerMove()

            if self._game.finished() == True:
                print("GAME OVER")
                self._game.showBoard()
                return
            if self._game.finished() == None:
                print("CONGRATS! YOU WON!")
                self._game.showBoard()
                return