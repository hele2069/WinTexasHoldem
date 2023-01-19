## Overview
This project uses **Monte Carlo Simulation** to predict players' win rates given their hands on a game of Texas Holdem. 

## Prerequisites 
The codebase is written using Python 3.8.8 with a virtual environment attached. Feel free to execute the code without this since it only utilizes basic Python packages such as random.

## How To Use
To clone and run this application, you'll need [Git](https://git-scm.com) installed on your computer. From your command line:

```bash
# Clone this repository
$ git clone https://github.com/hele2069/WinTexasHoldem

# Go into the repository
$ cd WinTexasHoldem

# Activate Virtual Environment (if needed)
$ conda activate myenv

# Run the code
$ python run.py
```

## Sample Output
```bash 
----- SETTINGS ----- 

Number of Players: 3
Number of Simulations: 1000

----- SUMMARY ----- 

PLAYER 1: ['5h', '2s'] (Win Rate: 0.186)
PLAYER 2: ['Jd', 'Qs'] (Win Rate: 0.429)
PLAYER 3: ['As', '2d'] (Win Rate: 0.394)
Tie Rate: 0.003

----- HAND WIN RATE ----- 

PLAYER 1: 
high_card: 0
pair: 0.04194
two_pair: 0.29614
three_of_a_kind: 0.3617
straight: 0.86047
flush: 0.84211
full_house: 0.875
four_of_a_kind: 1.0
straight_flush: 0
royal_flush: 0

PLAYER 2: 
high_card: 0
pair: 0.18653
two_pair: 0.61628
three_of_a_kind: 0.52113
straight: 0.88406
flush: 0.75
full_house: 0.86364
four_of_a_kind: 0
straight_flush: 0
royal_flush: 0

PLAYER 3: 
high_card: 0.016
pair: 0.23056
two_pair: 0.65532
three_of_a_kind: 0.55556
straight: 0.69231
flush: 0.75
full_house: 0.8
four_of_a_kind: 1.0
straight_flush: 0
royal_flush: 0


----- HAND DRAW RATE ----- 

PLAYER 1: 
pair: 0.763
two_pair: 0.233
three_of_a_kind: 0.047
straight: 0.043
flush: 0.019
full_house: 0.016
four_of_a_kind: 0.001
straight_flush: 0.0
royal_flush: 0.0

PLAYER 2: 
pair: 0.772
two_pair: 0.258
three_of_a_kind: 0.071
straight: 0.069
flush: 0.012
full_house: 0.022
four_of_a_kind: 0.0
straight_flush: 0.0
royal_flush: 0.0

PLAYER 3: 
pair: 0.746
two_pair: 0.235
three_of_a_kind: 0.045
straight: 0.013
flush: 0.012
full_house: 0.01
four_of_a_kind: 0.001
straight_flush: 0.0
royal_flush: 0.0
```
