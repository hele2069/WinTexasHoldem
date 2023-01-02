from game import TexasHoldem
from util import *
from card import Card
import argparse
from copy import deepcopy

# Parameters
parser = argparse.ArgumentParser()
parser.add_argument('--seed', default=1, type=int)
parser.add_argument('--num_iteration', default=1000, type=int)
parser.add_argument('--num_players', default=3, type=int)
args = parser.parse_args()

# Initiate Game 
game = TexasHoldem(player_count=args.num_players)
game.preflop()

def simulate_helper(game: TexasHoldem) -> list:
    temp = deepcopy(game)
    random.shuffle(temp.deck)
    if temp.state == 'preflop':
        temp.flop()
        temp.turn()
        temp.river() 
    elif temp.state == 'flop':
        temp.turn()
        temp.river() 
    elif temp.state == 'turn':
        temp.river()
    return win(temp)

# Monte Carlo Simulation 
for __ in range(args.num_iteration):
    players_update, winners = simulate_helper(game)
    game.players = players_update

# Simulation Summary 
## Overall Win Rate
print('\n')
print('----- SUMMARY ----- \n')
for i in game.players: 
    win_rate = i.wins/args.num_iteration
    print('{}: {} (Win Rate: {})'.format(i.name.upper(), [str(i.hand1), str(i.hand2)], win_rate))
print('Tie Rate: ' + str(game.players[0].ties/args.num_iteration)+'\n')

## Hand Win Rate Breakdown 
print('----- HAND WIN RATE ----- \n')
for i in game.players: 
    print('{}: '.format(i.name.upper()))
    for key in i.win_stats.keys():
        # for calculating win rate with a given hand 
        if i.win_stats[key] != 0 and i.draw_stats[key] != 0:
            rate = round(i.win_stats[key]/i.draw_stats[key], 5)
        else:
            rate = 0
        print('{}: {}'.format(key, rate))
    print('\n')

## Hand Draw Rate Breakdown 
print('----- HAND DRAW RATE ----- \n')
for i in game.players: 
    print('{}: '.format(i.name.upper()))
    for key in i.win_stats.keys():
        if key != 'high_card':
            rate = round(i.draw_stats[key]/args.num_iteration, 5)
            print('{}: {}'.format(key, rate))
    print('\n')


