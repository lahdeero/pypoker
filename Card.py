class Card:
    def __init__(self, rank, suit):
        self.rank = rank
        self.suit = suit

    def __str__(self):
        return self.represent()
    
    def __repr__(self):
        return self.represent()

    def represent(self):
        if self.suit == 1:
            return str(self.rank) + "♠"  
        elif self.suit == 2:
            return str(self.rank) + "♥"
        elif self.suit == 3:
            return str(self.rank) + "♦"
        elif self.suit == 4:
            return str(self.rank) + "♣"
        return "unknown card"
        

