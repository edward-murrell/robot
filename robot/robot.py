from robot import Aim, Board


class Robot:
    def __init__(self, board: Board):
        self.__board = board
        self.__locX = None
        self.__locY = None
        self.__face = None
        self.__placed = False

    def place(self, x: int, y: int, direction: Aim):
        if not self.__check_location(x, y):
            return None

        self.__locX = x
        self.__locY = y
        self.__face = direction
        self.__placed = True

    def turn_left(self):
        self.__face = Aim((self.__face - 1) % 4)

    def turn_right(self):
        self.__face = Aim((self.__face + 1) % 4)

    def move(self):
        if self.__face == Aim.NORTH and self.__check_location(self.__locX, self.__locY + 1):
            self.__locY += 1
        elif self.__face == Aim.SOUTH and self.__check_location(self.__locX, self.__locY - 1):
            self.__locY -= 1
        elif self.__face == Aim.EAST and self.__check_location(self.__locX + 1, self.__locY):
            self.__locX += 1
        elif self.__face == Aim.WEST and self.__check_location(self.__locX - 1, self.__locY):
            self.__locX -= 1

    def report(self):
        if self.__placed:
            return f"{self.__locX},{self.__locY},{self.__face.name}"
        else:
            return None

    def __check_location(self, x: int, y: int) -> bool:
        if x >= self.__board.width:
            return False
        if y >= self.__board.height:
            return False
        if x < 0:
            return False
        if y < 0:
            return False
        return True
