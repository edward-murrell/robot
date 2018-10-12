from robot import Aim, Board


def get_place_and_move_scenarios():
    """
    List of valid commands.

    Calling report after all the commands should match the 'report' key.

    :return: List contain scenarios, consisting of commands and a final 'report' location/
    """
    return [
        (
            "Robot can report it's location after being placed on a single square board.",
            Board(1, 1),
            [
                ('place', {'x': 0, 'y': 0, 'direction': Aim.NORTH})
            ],
            '0,0,NORTH'
        ),
        (
            'Robot moves North after given valid movement command.',
            Board(8, 8),
            [
                ('place', {'x': 2, 'y': 2, 'direction': Aim.NORTH}),
                ('move', {})
            ],
            '2,3,NORTH'
        ),
        (
            'Robot moves South after given valid movement command.',
            Board(8, 8),
            [
                ('place', {'x': 2, 'y': 2, 'direction': Aim.SOUTH}),
                ('move', {})
            ],
            '2,1,SOUTH'
        ),
        (
            'Robot moves East after given valid movement command.',
            Board(8, 8),
            [
                ('place', {'x': 2, 'y': 4, 'direction': Aim.EAST}),
                ('move', {})
            ],
            '3,4,EAST'
        ),
        (
            'Robot moves West after given valid movement command.',
            Board(8, 8),
            [
                ('place', {'x': 7, 'y': 0, 'direction': Aim.WEST}),
                ('move', {})
            ],
            '6,0,WEST'
        ),
        (
            'Robot turns right from North to East',
            Board(5, 5),
            [
                ('place', {'x': 2, 'y': 2, 'direction': Aim.NORTH}),
                ('turn_right', {})
            ],
            '2,2,EAST',
        ),
        (
            'Robot turns left from North to West',
            Board(5, 5),
            [
                ('place', {'x': 2, 'y': 2, 'direction': Aim.NORTH}),
                ('turn_left', {})
            ],
            '2,2,WEST',
        ),
        (
            'Robot turns left three times from North to East',
            Board(5, 5),
            [
                ('place', {'x': 2, 'y': 2, 'direction': Aim.NORTH}),
                ('turn_left', {}),
                ('turn_left', {}),
                ('turn_left', {})
            ],
            '2,2,EAST',
        ),
        (
            'Robot turns left three times from North to West',
            Board(5, 5),
            [
                ('place', {'x': 2, 'y': 2, 'direction': Aim.NORTH}),
                ('turn_left', {}),
                ('turn_left', {}),
                ('turn_left', {})
            ],
            '2,2,EAST',
        ),
        (
            'Robot turns left three times and then right to go from North to South',
            Board(5, 5),
            [
                ('place', {'x': 2, 'y': 2, 'direction': Aim.NORTH}),
                ('turn_left', {}),
                ('turn_left', {}),
                ('turn_left', {}),
                ('turn_right', {})
            ],
            '2,2,SOUTH',
        ),
        (
            '3x3 board. Robot starts in centre, turns to south, circuits the board, returns to top.',
            Board(3, 3),
            [
                ('place', {'x': 1, 'y': 1, 'direction': Aim.EAST}),
                ('turn_right', {}),
                ('move', {}),  # After command, will be at bottom of board.
                ('turn_left', {}),  # Turn east.
                ('move', {}),  # Bottom right corner.
                ('turn_left', {}),
                ('move', {}),
                ('move', {}),  # Now at top right
                ('turn_left', {}),
                ('move', {}),
                ('move', {}),  # Now at top left.
                ('turn_left', {}),
                ('move', {}),
                ('move', {}),  # Now at bottom left.
                ('turn_left', {}),
                ('move', {}),
                ('turn_right', {}),
                ('turn_right', {}),
                ('turn_right', {}),
                ('move', {}),
                ('move', {}),
            ],
            '1,2,NORTH',
        ),
        (
            '1x1 board. Robot tries to walk off the edge in all directions.',
            Board(1, 1),
            [
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
                ('turn_left', {}),  # Back to North
                ('move', {}),
                ('move', {}),
                ('move', {}),
            ],
            '0,0,NORTH',
        ),
        (
            "Robot never gets placed. Make sure commands don't crash the program.",
            Board(1, 1),
            [
                ('place', {'x': 3, 'y': 3, 'direction': Aim.SOUTH}),
                ('move', {}),
                ('turn_left', {}),  # Back to North
                ('turn_right', {}),  # Turn to the West.
            ],
            None
        ),
        (
            '1x4 board. Robot tries to walk off the corners. Moves from South to North',
            Board(1, 4),
            [
                ('place', {'x': 0, 'y': 3, 'direction': Aim.EAST}),
                ('move', {}),
                ('turn_right', {}),  # Turn South
                ('move', {}),
                ('move', {}),
                ('move', {}),
                ('turn_left', {}),  # Turn East
                ('move', {}),  # Edge of board
                ('turn_left', {}),  # Turn North
            ],
            '0,0,NORTH'
        )
    ]


def get_bad_place_scenarios():
    """
    List of placement values that should not produce a valid placement.

    Calling report after all these tests should produce "Not on the board yet!" error.

    :return: List contain scenarios, consisting of commands that do not make a valid placement.
    """
    return [
        (
            'No placement yet.',
            Board(5, 5),
            []
        ),
        (
            'No placement yet.',
            Board(1, 1),
            [
                ('place', {'x': 5, 'y': 5, 'direction': Aim.SOUTH})
            ]
        ),
        (
            'Single placement, X too high.',
            Board(1, 1),
            [
                ('place', {'x': 0, 'y': 1, 'direction': Aim.NORTH})
            ]
        ),
        (
            'Single placement, Y too high.',
            Board(1, 1),
            [
                ('place', {'x': 1, 'y': 0, 'direction': Aim.NORTH})
            ]
        ),
        (
            'Single placement, X too low.',
            Board(3, 3),
            [
                ('place', {'x': -4, 'y': 0, 'direction': Aim.EAST})
            ]
        ),
        (
            'Single placement, Y too low.',
            Board(3, 3),
            [
                ('place', {'x': 1, 'y': -2, 'direction': Aim.WEST})
            ]
        ),
        (
            'Place multiple times invalid location. Do not place.',
            Board(16, 16),
            [
                ('place', {'x': -1, 'y': 4, 'direction': Aim.NORTH}),
                ('place', {'x': 3, 'y': 17, 'direction': Aim.EAST}),
                ('place', {'x': 7, 'y': 999999, 'direction': Aim.WEST}),
                ('place', {'x': 20, 'y': 17, 'direction': Aim.SOUTH})
            ]
        )
    ]
