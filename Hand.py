from handrank import HandRank

class Hand:
    def __init__(self, cards):
        cards.sort(key=lambda x: x.rank, reverse=True)
        self.cards = cards
        self.suits =  self.organise_suits()
        self.fourOfKindValue = 0
        self.tripsValue = 0
        self.pairValue = 0
        self.secondPairValue = 0
        self.highCardValue = 0
        self.handRank = self.evaluate()

    def organise_suits(self):
        cards = self.cards
        suits = []
        hearths = []
        diamonds = []
        clubs = []
        spades = []
        for card in cards:
            if card.suit == 1:
                hearths.append(card)
            elif card.suit == 2:
                diamonds.append(card)
            elif card.suit == 3:
                clubs.append(card)
            elif card.suit == 4:
                spades.append(card)
        suits.append(hearths)
        suits.append(diamonds)
        suits.append(clubs)
        suits.append(spades)
        return suits

    def __eq__(self, obj):
        return self.compare(obj) == 0

    def __lt__(self, obj):
        return int(self.compare(obj)) < 0

    def compare(self, obj):
        if self.handRank != obj.handRank:
            return self.handRank - obj.handRank
        if self.handRank == HandRank.straightFlush:
            return self.highCardValue - obj.highCardValue 
        if self.handRank == HandRank.fourOfKind:
            if self.fourOfKindValue == obj.fourOfKindValue:
                return self.highCardValue - obj.highCardValue
            return self.fourOfKindValue - obj.fourOfKindValue
        if self.handRank == HandRank.fullHouse:
            if self.tripsValue == obj.tripsValue:
                return self.pairValue - obj.pairValue
            return self.tripsValue - obj.tripsValue
        if self.handRank == HandRank.flush or self.handRank == HandRank.straight:
            return self.highCardValue - obj.highCardValue
        if self.handRank == HandRank.threeOfKind:
            if self.tripsValue == obj.tripsValue:
                return compare_high_cards(obj)
            return self.tripsValue - obj.tripsValue
        if self.handRank == HandRank.twoPair:
            if self.pairValue == obj.pairValue:
                if self.secondPairValue == obj.secondPairValue:
                    return compare_high_cards(obj)
                return self.secondPairValue - obj.secondPairValue
            return self.pairValue - obj.pairValue
        if self.handRank == HandRank.pair:
            if self.pairValue == obj.pairValue:
                return compare_high_cards(obj)
            return self.pairValue - obj.pairValue

        return compare_high_cards(obj)
    
    def compare_high_cards(self, obj):
        l = max(len(self.cards), len(obj.cards))
        for i in range(l):
            if self.cards[i].rank != obj.cards[i].rank:
                return self.cards[i].rank - obj.cards[i].rank
        return 0

    def evaluate(self):
        if self.check_straight_flush():
            return HandRank.straightFlush
        elif self.check_four_of_kind():
            return HandRank.fourOfKind
        elif self.check_fullhouse():
            return HandRank.fullHouse
        elif self.check_flush():
            return HandRank.flush
        elif self.check_straight():
            return HandRank.straight
        elif self.check_three_of_kind():
            return HandRank.threeOfKind
        elif self.check_two_pair():
            return HandRank.twoPair
        elif self.check_pair():
            return HandRank.pair
        else: return HandRank.highCard
    
    def check_straight_flush(self):
        for suit in self.suits:
            if len(suit) >= 5:
                high_card = is_straight(suit)
                if high_card != 0:
                    self.highCardValue = high_card
                    return True
        return False
    
    def check_four_of_kind(self):
        count = 1
        for i in range(1, len(self.cards)):
            if self.cards[i].rank == self.cards[i-1].rank:
                count += 1
                if count == 4:
                    self.fourOfKindValue = self.cards[i].rank if self.cards[i].rank != 1 else 14
                    return True
            else: count = 1
        return False
    
    def check_fullhouse(self):
        trips = 0
        pair = 0
        for i in range(1, len(self.cards)):
            if self.cards[i].rank == self.cards[i-1].rank:
                if trips == 0 and pair == 0:
                    pair = self.cards[i].rank
                elif trips == 0:
                    trips = self.cards[i].rank
                    if pair == self.cards[i].rank:
                        pair = 0
                elif pair == 0:
                    pair = self.cards[i].rank

                if trips != 0 and pair != 0:
                    self.tripsValue = trips
                    self.pairValue = pair
                    return True
                    
        return False

    def check_flush(self):
        for suit in self.suits:
            if len(suit) >= 5:
                return True
        return False
    
    def check_straight(self):
        return is_straight(self.cards)
    
    def check_three_of_kind(self):
        for i in range(1, len(self.cards)):
            if self.cards[i].rank == self.cards[i-1].rank and i+1 < len(self.cards) and self.cards[i+1].rank == self.cards[i].rank:
                return self.cards[i].rank
        return 0
    
    def check_two_pair(self):
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


def is_straight(cards):
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
                return 14
        else:
            count = 0
    return 0 
