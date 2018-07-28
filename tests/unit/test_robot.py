from robot import Board, Robot, Aim
from unittest import TestCase


class TestRobot(TestCase):
    """
    Tests for a robot object to receive commands and issue reports.
    """

    def test_robot_report_empty(self):
        """
        Reports before the board is placed
        """
        expected = "Not on the board yet!"

        robot = Robot(Board(5, 5))
        actual = robot.report()

        self.assertEqual(expected, actual)

    def test_bad_place_report(self):
        """
        Robot will error when placement is invalid.
        """
        expected = "Not on the board yet!"

        robot = Robot(Board(1, 1))
        robot.place(5, 5)
        actual = robot.report()

        self.assertEqual(expected, actual)

    def test_place_report(self):
        """
        Robot can report it's location after being placed on a single square board.
        """
        expected = '0,0,NORTH'

        robot = Robot(Board(1, 1))
        robot.place(0, 0, Aim.North)
        actual = robot.report()

        self.assertEqual(expected, actual)
