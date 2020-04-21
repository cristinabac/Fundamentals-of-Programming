
from controller.gameController import *
from domain.ship import *
from repository.computer import *
from repository.user import *
from ui.ui import *

cb = computerBoard(8)
#ub = userBoard(8,[[0,0],[0,1],[0,2],[0,3]], [[3,4],[3,5],[3,6]], [[5,0],[6,0]])
ub = userBoard(8)
game = Game(cb, ub)
ui = Ui(game)
ui.start()