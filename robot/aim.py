from enum import Enum


class Aim(Enum):
    """
    Directional class.

    Used to enforce that only a canonical compass direction can be used.
    """
    North = "NORTH"
    South = "SOUTH"
    East = "EAST"
    West = "WEST"
