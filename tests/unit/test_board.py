from robot import Board
from unittest import TestCase


class TestBoard(TestCase):
    """
    Test that board is an immutable class with height and width parameters.
    """

    def test_board_properties(self):
        """
        Confirm that a board has a height and width available as properties.
        """
        board = Board(height=45, width=16)
        self.assertEqual(45, board.height)
        self.assertEqual(16, board.width)
