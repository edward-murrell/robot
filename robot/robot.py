from robot import Aim, Board


class Robot:
    def __init__(self, board: Board):
        self.__board = board
        self.__locX = None
        self.__locY = None
        self.__face = None
        self.__placed = False

    def place(self, x: int, y: int, direction: Aim):
        if x >= self.__board.width:
            return
        if y >= self.__board.height:
            return
        if x < 0:
            return
        if y < 0:
            return

        self.__locX = x
        self.__locY = y
        self.__face = direction
        self.__placed = True

    def turn_left(self):
        self.__face = Aim((self.__face - 1) % 4)

    def turn_right(self):
        self.__face = Aim((self.__face + 1) % 4)

    def move(self):
        if self.__face == Aim.NORTH and self.__locY + 1 < self.__board.height:
            self.__locY += 1
        elif self.__face == Aim.SOUTH and self.__locY - 1 >= 0:
            self.__locY -= 1
        if self.__face == Aim.EAST and self.__locX + 1 < self.__board.width:
            self.__locX += 1
        elif self.__face == Aim.WEST and (self.__locX - 1) >= 0:
            self.__locX -= 1

    def report(self):
        if self.__placed:
            return f"{self.__locX},{self.__locY},{self.__face.name}"
        else:
            return None
