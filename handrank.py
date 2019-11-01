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
