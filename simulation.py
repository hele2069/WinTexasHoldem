from game import TexasHoldem
from util import summary

game = TexasHoldem(player_count=5)
game.preflop()
game.flop()
game.turn()
game.river()
summary(game)


