from card import Card
from hand import Hand

def build_deck():
    deck = []
    for i in range(1,5):
        for j in range(1,14):
            card = Card(j,i)
            deck.append(card)
    return deck

def main():
    # h = Hand([Card(1,2), Card(2,2), Card(2,3), Card(5,1), Card(11,4)])
    # h2 = Hand([Card(1,3), Card(2,4), Card(2,4), Card(5,2), Card(12,1)])

    # a = [h, h2]

    # a.sort()
    # print(a[0])
    # hand = Hand([Card(1,1), Card(2,1), Card(3,1), Card(4,1), Card(5,1)])
    # other = Hand([Card(11,2), Card(11,1), Card(11,3), Card(3,2), Card(3,1)])
    # print(hand.value)
    # print(other.value)
    hand = Hand([Card(11,3), Card(11,1), Card(11,2), Card(11,4), Card(5,1)])
    other = Hand([Card(9,2), Card(9,1), Card(9,3), Card(3,4), Card(3,2)])
    print(hand.handRank - other.handRank)
    print(hand.handRank)
    print(other.handRank)

if __name__ == "__main__":
    main()
