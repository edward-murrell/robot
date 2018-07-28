from enum import IntEnum


class Aim(IntEnum):
    """
    Directional class.

    Used to enforce that only a canonical compass direction can be used.
    """
    NORTH = 0
    SOUTH = 2
    EAST = 1
    WEST = 3
