from controller.controller import game
from repository.repository import repo

r = repo()
g = game(r)

print(g._sen)
print(g._bad_sen)

g.swap(0,1,0,2)

print(g._sen)
print(g._bad_sen)
