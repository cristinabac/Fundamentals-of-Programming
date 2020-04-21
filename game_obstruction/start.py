from controller.controller import game
from repository.repository import repo
from ui.ui import UI

r = repo()
g = game(r)
ui = UI(g)


ui.start()