from robot import Board, Robot
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
