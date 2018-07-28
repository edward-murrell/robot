from robot import Board
from unittest import TestCase


class TestBoard(TestCase):
    def test_board(self):
        """
        First test to confirm existence of board.
        """
        board = Board()
