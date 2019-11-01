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


def evaluate(cards):
    cards.sort(key=lambda x: x.rank, reverse=True)
    print(cards)

    highCard = check_straightflush(cards)
    if highCard > 0:
        return (HandRank.straightFlush, highCard)
    highCard = check_four_of_kind(cards)
    if highCard > 0:
        return (HandRank.fourOfKind, highCard)
    highCard = check_fullhouse(cards)
    if highCard > 0:
        return (HandRank.fullHouse, highCard)
    highCard = check_flush(cards)
    if highCard > 0:
        return (HandRank.flush, highCard)
    highCard = check_straight(cards)
    if highCard > 0:
        return (HandRank.straight, highCard)
    highCard = check_three_of_kind(cards)
    if highCard > 0:
        return (HandRank.threeOfKind, highCard)
    highCard = check_two_pair(cards)
    if highCard > 0:
        return (HandRank.twoPair, highCard)
    highCard = check_pair(cards)
    if highCard > 0:
        return (HandRank.pair, highCard)
    return (HandRank.highCard, cards[0].rank)

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

def check_pair(cards):
    for i in range(1, len(cards)):
        if cards[i].rank == cards[i-1].rank:
            return cards[i].rank
    return 0


