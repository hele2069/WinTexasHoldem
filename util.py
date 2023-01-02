from player import Player 
import random 
from card import Card
from game import TexasHoldem
from copy import deepcopy

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
    suit_dict = {'h':[], 's':[], 'd':[], 'c':[]} 
    for card in temp:
        suit_dict[card.suit].append(card)
    for value in suit_dict.values():
        if len(value) >= 5:     
            value = list(value)
            value.sort(key=to_number, reverse=True)
            found = True
            hand = value[0:5]
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

def win(game: TexasHoldem): 
    for player in game.players: 
        if detect_high_card(game, player)[0]:
            player.best_hand = detect_high_card(game, player)[1]
            player.draw_stats['high_card'] += 1
            player.best_hand_score = 1
        if detect_pair(game, player)[0]:
            player.best_hand = detect_pair(game, player)[1]
            player.draw_stats['pair'] += 1
            player.best_hand_score = 2
        if detect_two_pair(game, player)[0]:
            player.best_hand = detect_two_pair(game, player)[1]
            player.draw_stats['two_pair'] += 1
            player.best_hand_score = 3
        if detect_three_of_a_kind(game, player)[0]:
            player.best_hand = detect_three_of_a_kind(game, player)[1]
            player.draw_stats['three_of_a_kind'] += 1
            player.best_hand_score = 4
        if detect_straight(game, player)[0]:
            player.best_hand = detect_straight(game, player)[1]
            player.draw_stats['straight'] += 1
            player.best_hand_score = 5
        if detect_flush(game, player)[0]:
            player.best_hand = detect_flush(game, player)[1]
            player.draw_stats['flush'] += 1
            player.best_hand_score = 6
        if detect_full_house(game, player)[0]:
            player.best_hand = detect_full_house(game, player)[1]
            player.draw_stats['full_house'] += 1
            player.best_hand_score = 7
        if detect_four_of_a_kind(game, player)[0]:
            player.best_hand = detect_four_of_a_kind(game, player)[1]
            player.draw_stats['four_of_a_kind'] += 1
            player.best_hand_score = 8
        if detect_straight_flush(game, player)[0]:
            player.best_hand = detect_straight_flush(game, player)[1]
            player.draw_stats['straight_flush'] += 1
            player.best_hand_score = 9
        if detect_royal_flush(game, player)[0]:
            player.best_hand = detect_royal_flush(game, player)[1]
            player.draw_stats['royal_flush'] += 1
            player.best_hand_score = 10 
    hand_assembly = {}
    for player in game.players: 
        if player.best_hand_score not in hand_assembly.keys():
            hand_assembly[player.best_hand_score] = [player]
        else:
            hand_assembly[player.best_hand_score].append(player)

    hand_type = max(list(hand_assembly.keys()))
    player_assembly = hand_assembly[hand_type]
    hand_dict = {1:'high_card',2:'pair',3:'two_pair',4:'three_of_a_kind',5:'straight',6:'flush',
                 7:'full_house',8:'four_of_a_kind',9:'straight_flush',10:'royal_flush'}
    # no tie 
    if len(player_assembly) == 1:
        player_assembly[0].win_stats[hand_dict[hand_type]] += 1
        player_assembly[0].wins += 1
        return game.players, player_assembly
    # tie 
    else: 
        if hand_type == 1: 
            player_assembly = tie_breaker(player_assembly, 0, 5)
        elif hand_type == 2: 
            player_assembly = tie_breaker(player_assembly, 0, 1)
            if len(player_assembly) != 1:
                player_assembly = tie_breaker(player_assembly, 2, 5)
        elif hand_type == 3: 
            player_assembly = tie_breaker(player_assembly, 0, 1)
            if len(player_assembly) != 1:
                player_assembly = tie_breaker(player_assembly, 2, 3)
                if len(player_assembly) != 1:
                    player_assembly = tie_breaker(player_assembly, 4, 5)
        elif hand_type == 4:
            player_assembly = tie_breaker(player_assembly, 0, 1)
            if len(player_assembly) != 1:
                player_assembly = tie_breaker(player_assembly, 3, 5)
        elif hand_type == 5:
            player_assembly = tie_breaker(player_assembly, 0, 1)
        elif hand_type == 6:
            player_assembly = tie_breaker(player_assembly, 0, 5)
        elif hand_type == 7:
            player_assembly = tie_breaker(player_assembly, 0, 1)
            if len(player_assembly) != 1:
                player_assembly = tie_breaker(player_assembly, 3, 4)
        elif hand_type == 8:
            player_assembly = tie_breaker(player_assembly, 0, 1)
            if len(player_assembly) != 1:
                player_assembly = tie_breaker(player_assembly, 4, 5)
        elif hand_type == 9:
            player_assembly = tie_breaker(player_assembly, 0, 1)
        elif hand_type == 10:
            player_assembly = player_assembly
        # all ties 
        if len(player_assembly) == len(game.players):
            for player in player_assembly:
                player.ties += 1
        # some ties (split pot)
        else: 
            for player in player_assembly:
                player.win_stats[hand_dict[hand_type]] += 1
                player.wins += 1
        return game.players, player_assembly

def tie_breaker(player_assembly: list, start: int, end: int):
    for i in range(start, end):
        compare = [to_number(hand.best_hand[i]) for hand in player_assembly]
        highest_kicker = max(compare)
        if compare.count(highest_kicker) == 1: 
            return [player_assembly[compare.index(highest_kicker)]]
        else:
            index = 0 
            while index < len(compare):
                card = compare[index]
                if card != highest_kicker:
                    compare.pop(index)
                    player_assembly.pop(index)
                else: 
                    index += 1
            return player_assembly