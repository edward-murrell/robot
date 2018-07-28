from robot import Robot
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

        robot = Robot()
        actual = robot.report()

        self.assertEqual(expected, actual)
