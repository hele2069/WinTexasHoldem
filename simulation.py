from game import TexasHoldem
from util import *

game = TexasHoldem(player_count=5)
game.preflop()
game.flop()
game.turn()
game.river()

for i in detect_straight_flush(game):
    print([str(j) for j in i])

summary(game)


