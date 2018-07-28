from robot import Board, Robot, Aim
from unittest import TestCase


class TestRobot(TestCase):
    """
    Tests for a robot object to receive commands and issue reports.
    """

    @staticmethod
    def get_place_and_move_scenarios():
        """
        List of valid commands.

        Calling report after all the commands should match the 'report' key.

        :return: List contain scenarios, consisting of commands and a final 'report' location/
        """
        return [
            {
                'label': "Robot can report it's location after being placed on a single square board.",
                'board': Board(1, 1),
                'commands': [
                    ('place', {'x': 0, 'y': 0, 'direction': Aim.NORTH})
                ],
                'report': '0,0,NORTH'
            },
            {
                'label': 'Robot moves North after given valid movement command.',
                'board': Board(8, 8),
                'commands': [
                    ('place', {'x': 2, 'y': 2, 'direction': Aim.NORTH}),
                    ('move', {})
                ],
                'report': '2,3,NORTH'
            },
            {
                'label': 'Robot moves South after given valid movement command.',
                'board': Board(8, 8),
                'commands': [
                    ('place', {'x': 2, 'y': 2, 'direction': Aim.SOUTH}),
                    ('move', {})
                ],
                'report': '2,1,SOUTH'
            },
            {
                'label': 'Robot moves East after given valid movement command.',
                'board': Board(8, 8),
                'commands': [
                    ('place', {'x': 2, 'y': 4, 'direction': Aim.EAST}),
                    ('move', {})
                ],
                'report': '3,4,EAST'
            },
            {
                'label': 'Robot moves West after given valid movement command.',
                'board': Board(8, 8),
                'commands': [
                    ('place', {'x': 7, 'y': 0, 'direction': Aim.WEST}),
                    ('move', {})
                ],
                'report': '6,0,WEST'
            },
            {
                'label': 'Robot turns right from North to East',
                'board': Board(5, 5),
                'commands': [
                    ('place', {'x': 2, 'y': 2, 'direction': Aim.NORTH}),
                    ('turn_right', {})
                ],
                'report': '2,2,EAST',
            },
            {
                'label': 'Robot turns left from North to West',
                'board': Board(5, 5),
                'commands': [
                    ('place', {'x': 2, 'y': 2, 'direction': Aim.NORTH}),
                    ('turn_left', {})
                ],
                'report': '2,2,WEST',
            },
            {
                'label': 'Robot turns left three times from North to East',
                'board': Board(5, 5),
                'commands': [
                    ('place', {'x': 2, 'y': 2, 'direction': Aim.NORTH}),
                    ('turn_left', {}),
                    ('turn_left', {}),
                    ('turn_left', {})
                ],
                'report': '2,2,EAST',
            },
            {
                'label': 'Robot turns left three times from North to West',
                'board': Board(5, 5),
                'commands': [
                    ('place', {'x': 2, 'y': 2, 'direction': Aim.NORTH}),
                    ('turn_left', {}),
                    ('turn_left', {}),
                    ('turn_left', {})
                ],
                'report': '2,2,EAST',
            },
            {
                'label': 'Robot turns left three times and then right to go from North to South',
                'board': Board(5, 5),
                'commands': [
                    ('place', {'x': 2, 'y': 2, 'direction': Aim.NORTH}),
                    ('turn_left', {}),
                    ('turn_left', {}),
                    ('turn_left', {}),
                    ('turn_right', {})
                ],
                'report': '2,2,SOUTH',
            },
            {
                'label': '3x3 board. Robot starts in centre, turns to south, circuits the board, returns to top.',
                'board': Board(3, 3),
                'commands': [
                    ('place', {'x': 1, 'y': 1, 'direction': Aim.EAST}),
                    ('turn_right', {}),
                    ('move', {}),       # After command, will be at bottom of board.
                    ('turn_left', {}),  # Turn east.
                    ('move', {}),       # Bottom right corner.
                    ('turn_left', {}),
                    ('move', {}),
                    ('move', {}),       # Now at top right
                    ('turn_left', {}),
                    ('move', {}),
                    ('move', {}),       # Now at top left.
                    ('turn_left', {}),
                    ('move', {}),
                    ('move', {}),       # Now at bottom left.
                    ('turn_left', {}),
                    ('move', {}),
                    ('turn_right', {}),
                    ('turn_right', {}),
                    ('turn_right', {}),
                    ('move', {}),
                    ('move', {}),
                ],
                'report': '1,2,NORTH',
            },
            {
                'label': '1x1 board. Robot tries to walk off the edge in all directions.',
                'board': Board(1, 1),
                'commands': [
                    ('place', {'x': 0, 'y': 0, 'direction': Aim.SOUTH}),
                    ('move', {}),
                    ('turn_right', {}),  # Turn to the West.
                    ('move', {}),
                    ('move', {}),
                    ('turn_right', {}),  # North
                    ('move', {}),
                    ('move', {}),
                    ('turn_right', {}),  # East
                    ('move', {}),
                    ('turn_left', {}),   # Back to North
                    ('move', {}),
                    ('move', {}),
                    ('move', {}),
                ],
                'report': '0,0,NORTH',
            },
            {
                'label': "Robot never gets placed. Make sure commands don't crash the program.",
                'board': Board(1, 1),
                'commands': [
                    ('place', {'x': 3, 'y': 3, 'direction': Aim.SOUTH}),
                    ('move', {}),
                    ('turn_left', {}),   # Back to North
                    ('turn_right', {}),  # Turn to the West.
                ],
                'report': None,
            },
            {
                'label': '1x4 board. Robot tries to walk off the corners. Moves from South to North',
                'board': Board(1, 4),
                'commands': [
                    ('place', {'x': 0, 'y': 3, 'direction': Aim.EAST}),
                    ('move', {}),
                    ('turn_right', {}),  # Turn South
                    ('move', {}),
                    ('move', {}),
                    ('move', {}),
                    ('turn_left', {}),  # Turn East
                    ('move', {}),       # Edge of board
                    ('turn_left', {}),  # Turn North
                ],
                'report': '0,0,NORTH',
            },
        ]

    def test_move_scenarios(self):
        """
        Worker method for get_bad_place_scenarios
        """
        for scenario in self.get_place_and_move_scenarios():

            label, board, commands, expected =\
                scenario['label'], scenario['board'], scenario['commands'], scenario['report']

            robot = Robot(board)
            for command, args in commands:
                robot.__getattribute__(command)(**args)

            actual = robot.report()
            self.assertEqual(expected, actual, f"Failed on scenario: {label}")

    def test_invalid_does_not_override(self):
        """
        Robot will not be replaced after place command.
        """
        expected = '2,3,EAST'

        robot = Robot(Board(16, 4))
        robot.place(2, 3, Aim.EAST)
        robot.place(16, 7, Aim.NORTH)
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
                    ('place', {'x': 5, 'y': 5, 'direction': Aim.SOUTH})
                ]
            },
            {
                'label': 'Single placement, X too high.',
                'board': Board(1, 1),
                'commands': [
                    ('place', {'x': 0, 'y': 1, 'direction': Aim.NORTH})
                ]
            },
            {
                'label': 'Single placement, Y too high.',
                'board': Board(1, 1),
                'commands': [
                    ('place', {'x': 1, 'y': 0, 'direction': Aim.NORTH})
                ]
            },
            {
                'label': 'Single placement, X too low.',
                'board': Board(3, 3),
                'commands': [
                    ('place', {'x': -4, 'y': 0, 'direction': Aim.EAST})
                ]
            },
            {
                'label': 'Single placement, Y too low.',
                'board': Board(3, 3),
                'commands': [
                    ('place', {'x': 1, 'y': -2, 'direction': Aim.WEST})
                ]
            },
            {
                'label': 'Place multiple times invalid location. Do not place.',
                'board': Board(16, 16),
                'commands': [
                    ('place', {'x': -1, 'y': 4, 'direction': Aim.NORTH}),
                    ('place', {'x': 3, 'y': 17, 'direction': Aim.EAST}),
                    ('place', {'x': 7, 'y': 999999, 'direction': Aim.WEST}),
                    ('place', {'x': 20, 'y': 17, 'direction': Aim.SOUTH})
                ]
            }
        ]

    def test_bad_place_values(self):
        """
        Worker method for get_bad_place_scenarios
        """
        expected = None
        for scenario in self.get_bad_place_scenarios():

            label, board, commands = scenario['label'], scenario['board'], scenario['commands']
            robot = Robot(board)
            for command, args in commands:
                robot.__getattribute__(command)(**args)
            actual = robot.report()
            self.assertEqual(expected, actual, f"Failed on scenario: {label}")
