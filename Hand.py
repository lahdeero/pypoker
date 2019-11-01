from enum import IntEnum

class HandRank(IntEnum):
    straightFlush = 8
    fourOfKind = 7
    fullHouse = 6
    flush = 5
    straight = 4
    threeOfKind = 3
    twoPair = 2
    pair = 1
    highCard = 0

class Hand:
    def __init__(self, cards):
        cards.sort(key=lambda x: x.rank, reverse=True)
        self.cards = cards
        self.pairValue = 0
        self.highCardValue = 0
        self.value = self.evaluate()

    def __eq__(self, other):
        if self.value != other.value: return False
        else: 
            if self.value == straightFlush:
                return self.highCardValue == other.highCardValue

    def __lt__(self, other):
        return self.value > other.value

    def evaluate(self):
        print(self.cards)
    
        if self.check_pair():
            return HandRank.pair
        else: return handRank.highCard
    
    def check_straightflush(cards):
        return 0
    
    def check_four_of_kind(cards):
        return 0
    
    def check_fullhouse(cards):
        return 0
    
    def check_flush(cards):
        arr = [0,0,0,0,0]
        for i in range(0, len(cards)):
            arr[cards[i].suit] += 1
    
        for i, item in enumerate(arr):
            if item is 5:
                for card in cards:
                    if card.suit is i:
                        return card.rank
        return 0
    
    def check_straight(cards):
        count = 0 
        for i in range(1, len(cards)):
            if cards[i].rank is cards[i-1].rank:
                continue
            if cards[i].rank + 1 is int(cards[i-1].rank):
                count += 1
                if count == 4:
                    if cards[i].rank is 1:
                        return 5
                    return cards[i-5].rank
                elif count == 3 and cards[i].rank is 10 and cards[len(cards)-1].rank is 1:
                    return 1
            else:
                count = 0
        return 0
    
    def check_three_of_kind(cards):
        for i in range(1, len(cards)):
            if cards[i].rank == cards[i-1].rank and i+1 < len(cards) and cards[i+1].rank == cards[i].rank:
                return cards[i].rank
        return 0
    
    def check_two_pair(cards):
        pair = 0
        first_pair_rank = 0
        for i in range(1, len(cards)):
            if cards[i].rank == cards[i-1].rank:
                if pair is 0:
                    pair = 1
                    first_pair_rank = cards[i].rank
                elif pair is 1 and cards[i].rank is not first_pair_rank:
                    return first_pair_rank if cards[i].rank != 1 else 1
        return 0
    
    def check_pair(self):
        for i in range(1, len(self.cards)):
            if self.cards[i].rank == self.cards[i-1].rank:
                return self.cards[i].rank
        return 0


