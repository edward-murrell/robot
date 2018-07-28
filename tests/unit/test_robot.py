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
        robot.place(5, 5, Aim.South)
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

    def get_bad_place_scenarios(self):
        """
        List of placement values that should not produce a valid placement.

        Calling report after all these tests should produce "Not on the board yet!" error.

        :return: List contain scenarios, consisting of commands that do not make a valid placement.
        """
        return [
            {
                'label': 'Single board, X too high.',
                'board': Board(1, 1),
                'commands': [
                    ('place', {'x': 0, 'y': 1, 'direction': Aim.North})
                ]
            },
            {
                'label': 'Single board, Y too high.',
                'board': Board(1, 1),
                'commands': [
                    ('place', {'x': 1, 'y': 0, 'direction': Aim.North})
                ]
            }
        ]

    def test_bad_place_values(self):
        """
        Worker method for get_bad_place_scenarios
        """
        expected = "Not on the board yet!"
        for scenario in self.get_bad_place_scenarios():

            label, board, commands = scenario['label'], scenario['board'], scenario['commands']
            robot = Robot(board)
            for command, args in commands:
                robot.__getattribute__(command)(**args)
            actual = robot.report()
            self.assertEqual(expected, actual)
