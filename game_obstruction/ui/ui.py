

class UI:

    def __init__(self, game):
        self._game = game

    def start(self):

        while True:
            self._game.showBoard()
            x = int(input("Enter row"))
            y = int(input("Enter column"))

            self._game.humanMove(x,y)

            if self._game.finished() == True:
                print("YOU WON")
                self._game.showBoard()
                return

            self._game.computerMove()

            if self._game.finished() == True:
                print("YOU LOST")
                self._game.showBoard()
                return