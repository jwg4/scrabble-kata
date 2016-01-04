import unittest

from scrabble import Board, score_word

class TestScoreWord(unittest.TestCase):
    def setUp(self):
        self.board = Board()


