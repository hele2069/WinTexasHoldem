
class Player:
    def __init__(self, name) -> None:
        self.name = name 
        self.hand1 = None 
        self.hand2 = None
        self.best_hand = None 
        self.best_hand_score = 0 
        self.wins = 0
        self.ties = 0
        self.win_stats = {'high_card':0,'pair':0,'two_pair':0,'three_of_a_kind':0,'straight':0,'flush':0,
                           'full_house':0,'four_of_a_kind':0,'straight_flush':0,'royal_flush':0}
        self.draw_stats = {'high_card':0,'pair':0,'two_pair':0,'three_of_a_kind':0,'straight':0,'flush':0,
                           'full_house':0,'four_of_a_kind':0,'straight_flush':0,'royal_flush':0}