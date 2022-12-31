import random
# from poker import Card
from player import Player 
from card import Card 
from deck import Deck 
import deck 
from util import generate_deck

class TexasHoldem:

    def __init__(self, player_count, players = [], flop='', turn='', river=''):
        
        self.players = players 
        self.deck = generate_deck() 
        self.flop_cards = flop 
        self.turn_cards = turn 
        self.river_cards = river 
        self.state = ''

        # init players 
        for i in range(1, player_count+1):
            player = Player(name='player '+str(i))
            self.players.append(player)

    def preflop(self):
        for i in self.players:
            i.hand1 = self.deck.pop()
        for i in self.players:
            i.hand2 = self.deck.pop()
        self.state = 'preflop'
    
    def flop(self):
        self.deck.pop() # burn 1
        self.flop_cards = [self.deck.pop() for __ in range(3)]
        self.state = 'flop'

    def turn(self):
        self.deck.pop() # burn 2
        self.turn_cards = self.deck.pop()
        self.state = 'turn'

    def river(self):
        self.deck.pop() # burn 3
        self.river_cards = self.deck.pop()
        self.state = 'river'
    