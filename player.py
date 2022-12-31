
class Player:
    def __init__(self, name) -> None:
        self.name = name 
        self.hand1 = None 
        self.hand2 = None
        self.stats = {'high_card':'','pair':'','two_pair':'','three_of_a_kind':'','straight':'',
                      'flush':'','full_house':'','four_of_a_kind':'','straight_flush':'','royal_flush':''}
        self.win_rate = 0