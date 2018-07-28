from robot import Robot


class Parser:
    def __init__(self, robot: Robot):
        self.__robot = robot

    def read(self, line: str):
        self.__robot.move()
