from player import Player 
import random 
from card import Card

def generate_deck() -> list:
    deck = []
    suit = ['s','c','h','d']
    val = ['2','3','4','5','6','7','8','9','10','J','Q','K','A']
    for i in suit:
        for j in val:
            temp = Card(val=j, suit=i)
            deck.append(temp)
    random.shuffle(deck)
    return deck 

def summary(game) -> None:
    # print('---------- Deck ---------- \n')
    # print(self.deck)

    print('---------- FLOP ----------')
    print([str(i) for i in game.flop_cards])

    print('---------- TURN ----------')
    print(game.turn_cards)

    print('---------- RIVER ---------')
    print(game.river_cards)

    for i in game.players:   
        print('----- {} ----- \n'.format(i.name.upper()))
        print([str(i.hand1), str(i.hand2)])
        print('Win Rate: '+str(i.win_rate)+'\n')

def compare_greater(card1, card2) -> bool: 
    val = ['2','3','4','5','6','7','8','9','10','J','Q','K','A']
    if val.index(card1.val) > val.index(card2.val):
        return True 
    elif val.index(card1.val) == val.index(card2.val):
        return None 
    else: 
        return False 

def detect_high_card(): 
    return 

def detect_pair(): 
    return 

def detect_two_pair(): 
    return 

def detect_three_of_a_kind(): 
    return 

def detect_straight(): 
    return 

def detect_flush(): 
    return 

def detect_full_house(): 
    return 

def detect_four_of_a_kind(): 
    return 

def detect_straight_flush(): 
    return 

def detect_royal_flush(): 
    return 

def win(player1, player2) -> Player: 
    return 
