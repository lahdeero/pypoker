import unittest
from card import Card
from hand import Hand
from handrank import HandRank

class TestHand(unittest.TestCase):
    def test_stragith_flush_eq(self):
        hand = Hand([Card(1,1), Card(2,1), Card(3,1), Card(4,1), Card(5,1)])
        other = Hand([Card(1,2), Card(2,2), Card(3,2), Card(4,2), Card(5,2)])
        self.assertEqual(hand, other, msg="suit should not matter when comparing straight flushes")

    def test_stragith_flush_lt(self):
        hand = Hand([Card(1,1), Card(2,1), Card(3,1), Card(4,1), Card(5,1)])
        other = Hand([Card(10,2), Card(11,2), Card(12,2), Card(13,2), Card(1,2)])
        self.assertLess(hand, other, msg="wheel straigth flush should be lesser than royal straight flush")

    def test_straight_flush_beats_four_of_kind(self):
        hand = Hand([Card(1,1), Card(2,1), Card(3,1), Card(4,1), Card(5,1)])
        other = Hand([Card(11,2), Card(11,1), Card(11,3), Card(11,4), Card(5,2)])
        self.assertGreater(hand, other, msg="straight flush should beat four of kind")

    def test_four_of_kind_eq(self):
        hand = Hand([Card(11,3), Card(11,1), Card(11,2), Card(11,4), Card(5,1)])
        other = Hand([Card(11,2), Card(11,1), Card(11,3), Card(11,4), Card(5,2)])
        self.assertEqual(hand, other, msg="suit should not matter when comparing four of kinds")

    def test_four_of_kind_lt(self):
        hand = Hand([Card(11,3), Card(11,1), Card(11,2), Card(11,4), Card(5,1)])
        other = Hand([Card(1,2), Card(1,1), Card(1,3), Card(1,4), Card(2,2)])
        self.assertLess(hand, other, msg="four jacks should be less than four aces")

    def test_four_of_kind_beats_full_house(self):
        hand = Hand([Card(9,2), Card(9,1), Card(9,3), Card(3,4), Card(3,2)])
        other = Hand([Card(11,3), Card(11,1), Card(11,2), Card(11,4), Card(5,1)])
        self.assertLess(hand, other, msg="full house should be less than four of kind")

    def test_full_house_eq(self):
        hand = Hand([Card(9,2), Card(9,1), Card(9,3), Card(3,4), Card(3,2)])
        other = Hand([Card(9,1), Card(9,2), Card(9,3), Card(3,1), Card(3,3)])
        self.assertEqual(hand, other, msg="suit should not matter when comparing full houses")

    def test_full_house_lt(self):
        hand = Hand([Card(8,2), Card(8,1), Card(8,3), Card(3,4), Card(3,2)])
        other = Hand([Card(9,1), Card(9,2), Card(9,3), Card(3,1), Card(3,3)])
        self.assertLess(hand, other, msg="eights full should be less than nines full")

    def test_flush(self):
        h = Hand([Card(6,2), Card(9,3), Card(5,2), Card(13,2), Card(6,3), Card(7,2), Card(8,2)])
        self.assertEqual(h.handRank, HandRank.flush)

    # def test_straight(self):
    #     self.assertEqual(evaluate([Card(1,2), Card(2,3), Card(3,2), Card(4,3), Card(5,4)]), (HandRank.straight, 5))
    #     self.assertEqual(evaluate([Card(6,2), Card(9,3), Card(5,2), Card(13,2), Card(6,3), Card(7,3), Card(8,4)]), (HandRank.straight, 9))
    #     self.assertEqual(evaluate([Card(11,2), Card(10,3), Card(12,2), Card(13,3), Card(1,4)]), (HandRank.straight, 1))
    # def test_two_pair(self):
    #     self.assertEqual(evaluate([Card(1,2), Card(1,3), Card(2,2), Card(3,3), Card(2,4)]), (HandRank.twoPair, 1))
    # def test_pair(self):
    #     self.assertEqual(evaluate([Card(1,2), Card(1,3)]), (HandRank.pair, 1))
    # def test_highcard(self):
    #     self.assertEqual(evaluate([Card(1,2), Card(11,3), Card(2,2), Card(3,3), Card(12,4)]), (HandRank.highCard, 12))


if __name__ == "__main__":
    unittest.main()

