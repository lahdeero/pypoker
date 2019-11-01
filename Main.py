from Card import Card
from Hand import Hand

def build_deck():
    deck = []
    for i in range(1,5):
        for j in range(1,14):
            card = Card(j,i)
            deck.append(card)
    return deck

def main():
    h = Hand([Card(1,2), Card(2,2), Card(2,3), Card(5,1), Card(11,4)])
    h2 = Hand([Card(1,3), Card(2,4), Card(2,4), Card(5,2), Card(12,1)])

    a = [h, h2]

    a.sort()
    print(a[0])

if __name__ == "__main__":
    main()
