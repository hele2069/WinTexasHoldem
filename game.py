import random
from card import Card
from player import Player 

class TexasHoldem:

    def __init__(self, player_count, players = []):
        self.players = players 
        self.board = None 
        self.state = None 

        # init players 
        if not players: 
            for i in range(1, player_count+1):
                player = Player(name='player '+str(i))
                self.players.append(player)

        # generate deck 
        deck = []
        suit = ['s','c','h','d']
        val = ['2','3','4','5','6','7','8','9','10','J','Q','K','A']
        for i in suit:
            for j in val:
                temp = Card(val=j, suit=i)
                deck.append(temp)
        random.shuffle(deck)
        self.deck = deck 

    def preflop(self):
        for i in self.players:
            i.hand1 = self.deck.pop()
        for i in self.players:
            i.hand2 = self.deck.pop()
        self.state = 'preflop'
    
    def flop(self):
        self.deck.pop() # burn 1
        self.board = [self.deck.pop() for __ in range(3)]
        self.state = 'flop'

    def turn(self):
        self.deck.pop() # burn 2
        out = self.deck.pop()
        self.board.append(out)
        self.state = 'turn'

    def river(self):
        self.deck.pop() # burn 3
        out = self.deck.pop()
        self.board.append(out)
        self.state = 'river'