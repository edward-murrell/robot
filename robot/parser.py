from robot import Robot


class Parser:
    def __init__(self, robot: Robot):
        self.__robot = robot

    def read(self, line: str):
        if line == 'MOVE':
            self.__robot.move()
        elif line == 'LEFT':
            self.__robot.turn_left()
        elif line == 'RIGHT':
            self.__robot.turn_right()
        elif line == 'REPORT':
            return self.__robot.report()
