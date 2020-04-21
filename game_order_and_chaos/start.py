from controller.controller import game
from repository.repository import board
from ui.ui import UI

b = board()
g = game(b)
ui = UI(g)

ui.start()