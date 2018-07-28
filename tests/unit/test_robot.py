from robot import Board, Robot, Aim
from unittest import TestCase


class TestRobot(TestCase):
    """
    Tests for a robot object to receive commands and issue reports.
    """

    def test_place_report(self):
        """
        Robot can report it's location after being placed on a single square board.
        """
        expected = '0,0,NORTH'

        robot = Robot(Board(1, 1))
        robot.place(0, 0, Aim.North)
        actual = robot.report()

        self.assertEqual(expected, actual)

    @staticmethod
    def get_bad_place_scenarios():
        """
        List of placement values that should not produce a valid placement.

        Calling report after all these tests should produce "Not on the board yet!" error.

        :return: List contain scenarios, consisting of commands that do not make a valid placement.
        """
        return [
            {
                'label': 'No placement yet.',
                'board': Board(5, 5),
                'commands': []
            },
            {
                'label': 'No placement yet.',
                'board': Board(1, 1),
                'commands': [
                    ('place', {'x': 5, 'y': 5, 'direction': Aim.South})
                ]
            },
            {
                'label': 'Single placement, X too high.',
                'board': Board(1, 1),
                'commands': [
                    ('place', {'x': 0, 'y': 1, 'direction': Aim.North})
                ]
            },
            {
                'label': 'Single placement, Y too high.',
                'board': Board(1, 1),
                'commands': [
                    ('place', {'x': 1, 'y': 0, 'direction': Aim.North})
                ]
            },
            {
                'label': 'Single placement, X too low.',
                'board': Board(3, 3),
                'commands': [
                    ('place', {'x': -4, 'y': 0, 'direction': Aim.East})
                ]
            },
            {
                'label': 'Single placement, Y too low.',
                'board': Board(3, 3),
                'commands': [
                    ('place', {'x': 1, 'y': -2, 'direction': Aim.West})
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
            self.assertEqual(expected, actual, f"Failed on scenario: {label}")
