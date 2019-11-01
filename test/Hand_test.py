import unittest
from Evaluator import evaluate, HandRank
from Card import Card

class TestEvaluatorMethods(unittest.TestCase):
    def test_stragithflush(self):
        hand = ([Card(1,1), Card(2,1), Card(3,1), Card(4,1), Card(5,1)])
        other = ([Card(1,2), Card(2,2), Card(3,2), Card(4,2), Card(5,2)])
        self.assertEqual(hand, other)
    def test_flush(self):
        self.assertEqual(evaluate([Card(6,2), Card(9,3), Card(5,2), Card(13,2), Card(6,3), Card(7,2), Card(8,2)]), (HandRank.flush, 13))
    def test_straight(self):
        self.assertEqual(evaluate([Card(1,2), Card(2,3), Card(3,2), Card(4,3), Card(5,4)]), (HandRank.straight, 5))
        self.assertEqual(evaluate([Card(6,2), Card(9,3), Card(5,2), Card(13,2), Card(6,3), Card(7,3), Card(8,4)]), (HandRank.straight, 9))
        self.assertEqual(evaluate([Card(11,2), Card(10,3), Card(12,2), Card(13,3), Card(1,4)]), (HandRank.straight, 1))
    def test_two_pair(self):
        self.assertEqual(evaluate([Card(1,2), Card(1,3), Card(2,2), Card(3,3), Card(2,4)]), (HandRank.twoPair, 1))
    def test_pair(self):
        self.assertEqual(evaluate([Card(1,2), Card(1,3)]), (HandRank.pair, 1))
    def test_highcard(self):
        self.assertEqual(evaluate([Card(1,2), Card(11,3), Card(2,2), Card(3,3), Card(12,4)]), (HandRank.highCard, 12))


if __name__ == "__main__":
    unittest.main()

