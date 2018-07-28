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

    def report(self):
        if self.__placed:
            return f"{self.__locX},{self.__locY},{self.__face.value}"
        else:
            return "Not on the board yet!"
