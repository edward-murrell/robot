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

    def test_immutable_height(self):
        """
        Board height properties are immutable.
        """
        board = Board(width=1, height=22)
        with self.assertRaises(ValueError) as exc:
            board.height = 8
            self.assertEqual("Board height cannot be changed after creation.", str(exc))

    def test_immutable_width(self):
        """
        Board width properties are immutable.
        """
        board = Board(width=4, height=4)
        with self.assertRaises(ValueError) as exc:
            board.width = 0
            self.assertEqual("Board width cannot be changed after creation.", str(exc))
