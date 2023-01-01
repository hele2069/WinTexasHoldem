from game import TexasHoldem
from util import *
from card import Card

game = TexasHoldem(player_count=1)
game.players[0].hand1 = Card(val='K',suit='c')
game.players[0].hand2 = Card(val='K',suit='s')

card1 = Card(val='9',suit='s')
card2 = Card(val='K',suit='s')
card3 = Card(val='Q',suit='s')
card4 = Card(val='J',suit='s')
card5 = Card(val='10',suit='s')

game.board = [card1, card2, card3, card4, card5]
game.state = 'river'

print(detect_royal_flush(game, game.players[0])[0], [str(i) for i in detect_royal_flush(game, game.players[0])[1]])

summary(game)


