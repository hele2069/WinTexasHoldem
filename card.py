
class Card:
    def __init__(self, val, suit) -> None:
        self.val = val 
        self.suit = suit 
    
    def __str__(self) -> str:
        return str(self.val)+str(self.suit)