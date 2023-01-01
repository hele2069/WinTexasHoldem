from player import Player 
import random 
from card import Card
from game import TexasHoldem

# combines board and player hand 
def generate_hand(game, player):
    temp = game.board.copy()
    temp.append(player.hand1)
    temp.append(player.hand2)
    return temp 

# handles J, Q, K, A in sorting 
def to_number(card):
    FACE_CARDS = {'J': 11, 'Q': 12, 'K': 13, 'A': 14}
    if card.val.isnumeric():
        return int(card.val)
    else:
        return FACE_CARDS[card.val]

def detect_high_card(game):
    output = []
    for player in game.players: 
        if game.state != 'preflop':
            temp = generate_hand(game, player)
            temp.sort(key=to_number, reverse=True)
            output.append(temp[0:5])
        else: 
            output.append([player.hand1, player.hand2])        
    return output 

def detect_pair(game): 
    output = []
    for player in game.players: 
        if game.state != 'preflop':
            temp = generate_hand(game, player)
            temp.sort(key=to_number, reverse=True)
            for i in range(len(temp)-1):
                if temp[i].val == temp[i+1].val:
                    card1 = temp.pop(i)
                    card2 = temp.pop(i)
                    output.append([card1, card2, temp[0], temp[1], temp[2]])
                    break
                elif i == len(temp)-2:
                    output.append([None, None, None, None, None])
        else: 
            if player.hand1.val == player.hand2.val:
                output.append([player.hand1, player.hand2, None, None, None])
            else: 
                output.append([None, None, None, None, None])
    return output 

def detect_two_pair(game): 
    output = []
    for player in game.players: 
        if game.state != 'preflop':
            pair_cnt = 0
            hand = []
            temp = generate_hand(game, player)
            temp.sort(key=to_number, reverse=True)
            # first pair 
            for i in range(len(temp)-1):
                if temp[i].val == temp[i+1].val:
                    hand.append(temp.pop(i))
                    hand.append(temp.pop(i))
                    pair_cnt += 1
                    break
            # second pair 
            for i in range(len(temp)-1):
                if temp[i].val == temp[i+1].val:
                    hand.append(temp.pop(i))
                    hand.append(temp.pop(i))
                    pair_cnt += 1
                    break
            if pair_cnt == 2 and len(hand) == 4:
                hand.append(temp[0])
                output.append(hand)
            else: 
                output.append([None, None, None, None, None])
        else: 
            output.append([None, None, None, None, None])
    return output 

def detect_three_of_a_kind(game): 
    output = []
    for player in game.players: 
        hand = [None, None, None, None, None]
        if game.state != 'preflop':
            temp = generate_hand(game, player)
            temp.sort(key=to_number, reverse=True)
            for i in range(len(temp)-2):
                if temp[i].val == temp[i+2].val:
                    card1 = temp.pop(i)
                    card2 = temp.pop(i)
                    card3 = temp.pop(i)
                    hand = [card1, card2, card3, temp[0], temp[1]]
                    break     
                elif i == len(temp)-3:
                    break
        output.append(hand)
    return output 

def detect_straight(game): 
    output = []
    for player in game.players: 
        hand = [None, None, None, None, None]
        if game.state != 'preflop':
            temp = generate_hand(game, player)
            straight = {}
            for card in temp:
                if card.val not in straight.keys(): 
                    straight[to_number(card)] = [card]
                else:
                    straight[card.val].append(card)
            if len(straight.keys()) >= 5:
                seq = list(straight.keys())
                seq.sort(reverse=True) 
                for i in range(3):
                    if i + 4 < len(seq):
                        if seq[i] - seq[i+4] == 4:
                            hand = [straight[seq[i]][0],straight[seq[i+1]][0],straight[seq[i+2]][0],straight[seq[i+3]][0],straight[seq[i+4]][0]]
                            break
        output.append(hand)
    return output 

def detect_flush(game): 
    output = []
    for player in game.players: 
        hand = [None, None, None, None, None]
        if game.state != 'preflop':
            temp = generate_hand(game, player)
            temp.sort(key=lambda x:(x.suit,to_number(x)), reverse=True)
            for i in range(3): 
                if i + 4 < len(temp) and temp[i].suit == temp[i+4].suit:
                    hand = temp[i:i+5]
        output.append(hand)
    return output 

def detect_full_house(game): 
    output = []
    for player in game.players: 
        hand = [None, None, None, None, None]
        if game.state != 'preflop':
            temp = generate_hand(game, player)
            temp.sort(key=to_number, reverse=True)
            for i in range(len(temp)-2):
                if temp[i].val == temp[i+2].val:
                    card1 = temp.pop(i)
                    card2 = temp.pop(i)
                    card3 = temp.pop(i)
                    hand = [card1, card2, card3]     
                    break
                elif i == len(temp)-3:
                    break 
            if len(hand) == 3: 
                for i in range(len(temp)-1):
                    if temp[i].val == temp[i+1].val:
                        hand.append(temp.pop(i))
                        hand.append(temp.pop(i))
                        break
                    elif i == len(temp)-2:
                        hand = [None, None, None, None, None]
        output.append(hand)
    return output 

def detect_four_of_a_kind(game): 
    output = []
    for player in game.players: 
        hand = [None, None, None, None, None]
        if game.state != 'preflop':
            temp = generate_hand(game, player)
            temp.sort(key=to_number, reverse=True)
            for i in range(len(temp)-3):
                if temp[i].val == temp[i+3].val:
                    card1 = temp.pop(i)
                    card2 = temp.pop(i)
                    card3 = temp.pop(i)
                    card4 = temp.pop(i)
                    hand = [card1, card2, card3, card4, temp[0]]
                    break     
                elif i == len(temp)-4:
                    break
        output.append(hand)
    return output 

def detect_straight_flush(game): 
    output = []
    for player in game.players: 
        hand = [None, None, None, None, None]
        if game.state != 'preflop':
            switch = False
            temp = generate_hand(game, player)
            suit_dict = {'h':[], 's':[], 'd':[], 'c':[]} 
            for card in temp: 
                suit_dict[card.suit].append(card)
            for key, value in suit_dict.items():
                if len(value) >= 5: 
                    hand = value 
                    switch = True 
                    break 
            if not switch: 
                hand = [None, None, None, None, None] 
            else: 
                hand.sort(key=to_number, reverse=True)
                for i in range(3):
                    if i + 4 < len(hand) and to_number(hand[i]) - to_number(hand[i+4]) == 4:
                        hand = hand[i:i+5]
                        break 
                    if i == len(hand)-4:
                        hand = [None, None, None, None, None]
        output.append(hand)
    return output 

def detect_royal_flush(game: TexasHoldem): 
    output = []
    hand = [None, None, None, None, None]
    for player in game.players:
        if game.state != 'preflop':
            temp = generate_deck(game, player)
            for i in range
