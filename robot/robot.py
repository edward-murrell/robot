from typing import Optional
from robot import Aim, Board


class Robot:
    """
    Robot class that moves around the board one square at a time in compass directions (North, South, East, West).
    """

    def __init__(self, board: Board):
        """
        Create a robot on the defined board.

        :param board: Board object that the robot sits on.
        """
        self.__board = board
        self.__locX = None
        self.__locY = None
        self.__face = None
        self.__placed = False

    def place(self, x: int, y: int, direction: Aim):
        """
        Attempt to place the robot on the board.

        Locations start at zero, in the South-West corner.
         ie; On a 5x3 board, the South West corner is x=0,y=0, and the North-East corner is x=2,y=4.

        The robot can be placed at any time. If the location is invalid, the robot will not be moved placed.
          No error messages are generated on an invalid placing.

        :param x: Horizontal location (West to East), starting at zero.
        :param y: Vertical location (South to North), starting at zero.
        :param direction: Compass direction, set by the Aim class.
        """
        if not self.__check_location(x, y):
            return

        self.__locX = x
        self.__locY = y
        self.__face = direction
        self.__placed = True

    def turn_left(self):
        """
        Turn the robot left 90 degrees.
        ie; If the robot is pointing East, it will turn North.

        No error message is generated if the robot is not yet placed.
        """
        if self.__placed:
            self.__face = Aim((self.__face - 1) % 4)

    def turn_right(self):
        """
        Turn the robot right 90 degrees.
        ie; If the robot is pointing South, it will turn West.

        No error message is generated if the robot is not yet placed.
        """
        if self.__placed:
            self.__face = Aim((self.__face + 1) % 4)

    def move(self):
        """
        Move the robot one square in the direction it is facing.

        If the robot is not yet placed, or is on the edge of the board, nothing will happen.
        """
        if not self.__placed:
            return
        if self.__face == Aim.NORTH and self.__check_location(self.__locX, self.__locY + 1):
            self.__locY += 1
        elif self.__face == Aim.SOUTH and self.__check_location(self.__locX, self.__locY - 1):
            self.__locY -= 1
        elif self.__face == Aim.EAST and self.__check_location(self.__locX + 1, self.__locY):
            self.__locX += 1
        elif self.__face == Aim.WEST and self.__check_location(self.__locX - 1, self.__locY):
            self.__locX -= 1

    def report(self) -> Optional[str]:
        """
        Get the location of the robot as a string.

        The format is "X,Y,DIRECTION", where X is the West to East location, starting at zero, Y is the South to North
         location, starting at zero, and the direction is an all upper case direction of NORTH, SOUTH, EAST, or WEST.

        If the robot is not yet placed, a None will be returned.

        :return: Optional string describing location and direction.
        """
        if self.__placed:
            return f"{self.__locX},{self.__locY},{self.__face.name}"
        else:
            return None

    def __check_location(self, x: int, y: int) -> bool:
        """
        Check if the given location is valid.

        Method will check if supplied location is in the bounds of the board. This method does not move the robot.

        :param x: Requested horizontal location (West to East), starting at zero.
        :param y: Requested vertical location (South to North), starting at zero.
        :return: True if the location is valid on the board, false if it is not.
        """
        if x >= self.__board.width:
            return False
        if y >= self.__board.height:
            return False
        if x < 0:
            return False
        if y < 0:
            return False
        return True
