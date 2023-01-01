from player import Player 
import random 
from card import Card
from game import TexasHoldem

def summary(game: TexasHoldem) -> None:
    # print(self.deck)
    print('---------- BOARD ----------\n')
    print([str(i) for i in game.board])
    print('\n')

    for i in game.players:   
        print('----- {} ----- \n'.format(i.name.upper()))
        print([str(i.hand1), str(i.hand2)])
        print('Win Rate: '+str(i.win_rate)+'\n')

def value_greater(card1: Card, card2: Card) -> bool: 
    val = ['2','3','4','5','6','7','8','9','10','J','Q','K','A']
    if val.index(card1.val) > val.index(card2.val):
        return True 
    elif val.index(card1.val) == val.index(card2.val):
        return None 
    else: 
        return False 

# combines board and player hand 
def generate_hand(game: TexasHoldem, player: Player):
    temp = game.board.copy()
    temp.append(player.hand1)
    temp.append(player.hand2)
    return temp 

# handles J, Q, K, A in sorting 
def to_number(card: Card) -> int:
    FACE_CARDS = {'J': 11, 'Q': 12, 'K': 13, 'A': 14}
    if card.val.isnumeric():
        return int(card.val)
    else:
        return FACE_CARDS[card.val]

def detect_high_card(game: TexasHoldem, player: Player) -> list:
    temp = generate_hand(game, player)
    temp.sort(key=to_number, reverse=True)
    hand = temp[0:5]
    return True, hand 

def detect_pair(game: TexasHoldem, player: Player) -> list: 
    temp = generate_hand(game, player)
    temp.sort(key=to_number, reverse=True)
    found = False
    hand = [None, None, None, None, None]
    for i in range(len(temp)-1):
        if temp[i].val == temp[i+1].val:
            card1 = temp.pop(i)
            card2 = temp.pop(i)
            hand = [card1, card2, temp[0], temp[1], temp[2]]
            found = True
            break
    return found, hand 

def detect_two_pair(game: TexasHoldem, player: Player) -> list: 
    pair_cnt = 0
    hand = []
    found = False 
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
        found = True 
    else: 
        hand = [None, None, None, None, None]
    return found, hand  

def detect_three_of_a_kind(game: TexasHoldem, player: Player) -> list: 
    hand = [None, None, None, None, None]
    found = False 
    temp = generate_hand(game, player)
    temp.sort(key=to_number, reverse=True)
    for i in range(len(temp)-2):
        if temp[i].val == temp[i+2].val:
            card1 = temp.pop(i)
            card2 = temp.pop(i)
            card3 = temp.pop(i)
            hand = [card1, card2, card3, temp[0], temp[1]]
            found = True 
            break     
    return found, hand  

def detect_straight(game: TexasHoldem, player: Player) -> list: 
    hand = [None, None, None, None, None]
    found = False
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
            if i + 4 < len(seq) and seq[i] - seq[i+4] == 4:
                hand = [straight[seq[i]][0],straight[seq[i+1]][0],straight[seq[i+2]][0],straight[seq[i+3]][0],straight[seq[i+4]][0]]
                found = True 
                break
    return found, hand  

def detect_flush(game: TexasHoldem, player: Player) -> list: 
    hand = [None, None, None, None, None]
    found = False 
    temp = generate_hand(game, player)
    temp.sort(key=lambda x:(x.suit,to_number(x)), reverse=True)
    for i in range(3): 
        if i + 4 < len(temp) and temp[i].suit == temp[i+4].suit:
            hand = temp[i:i+5]
            found = True 
            break
    return found, hand  

def detect_full_house(game: TexasHoldem, player: Player) -> list: 
    hand = [None, None, None, None, None]
    found = False 
    temp = generate_hand(game, player)
    temp.sort(key=to_number, reverse=True)
    # find triple
    for i in range(len(temp)-2):
        if temp[i].val == temp[i+2].val:
            card1 = temp.pop(i)
            card2 = temp.pop(i)
            card3 = temp.pop(i)
            hand = [card1, card2, card3]     
            break
        elif i == len(temp)-3:
            break 
    # find pair 
    if len(hand) == 3: 
        for i in range(len(temp)-1):
            if temp[i].val == temp[i+1].val:
                hand.append(temp.pop(i))
                hand.append(temp.pop(i))
                found = True 
                break
            elif i == len(temp)-2:
                hand = [None, None, None, None, None]
    return found, hand 

def detect_four_of_a_kind(game: TexasHoldem, player: Player) -> list: 
    hand = [None, None, None, None, None]
    found = False 
    temp = generate_hand(game, player)
    temp.sort(key=to_number, reverse=True)
    for i in range(len(temp)-3):
        if temp[i].val == temp[i+3].val:
            card1 = temp.pop(i)
            card2 = temp.pop(i)
            card3 = temp.pop(i)
            card4 = temp.pop(i)
            hand = [card1, card2, card3, card4, temp[0]]
            found = True 
            break     
    return found, hand 

def detect_straight_flush(game: TexasHoldem, player: Player) -> list: 
    hand = [None, None, None, None, None]
    found = False 
    temp = generate_hand(game, player)
    suit_dict = {'h':[], 's':[], 'd':[], 'c':[]} 
    for card in temp: 
        suit_dict[card.suit].append(card)
    for value in suit_dict.values():
        if len(value) >= 5: 
            flush = list(value.copy())
            flush.sort(key=to_number, reverse=True)
            for i in range(3):
                if i + 4 < len(flush) and to_number(flush[i]) - to_number(flush[i+4]) == 4:
                    hand = flush[i:i+5]
                    found = True 
                    break 
            break 
    return found, hand  

def detect_royal_flush(game: TexasHoldem, player: Player) -> list: 
    hand = [None, None, None, None, None]
    found = False 
    temp = generate_hand(game, player)
    suit_dict = {'h':[], 's':[], 'd':[], 'c':[]} 
    for card in temp: 
        suit_dict[card.suit].append(card)
    for value in suit_dict.values():
        if len(value) >= 5: 
            flush = list(value.copy())
            flush.sort(key=to_number, reverse=True)
            for i in range(3):
                if i + 4 < len(flush) and to_number(flush[i])-to_number(flush[i+4])==4 and flush[i].val=='A':
                    hand = flush[i:i+5]
                    found = True 
                    break 
            break 
    return found, hand 

def win(player1, player2) -> Player: 
    return 
