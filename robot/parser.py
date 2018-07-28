from robot import Robot, Aim


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
        elif line == 'PLACE 3,4,NORTH':
            return self.__robot.place(3, 4, Aim.NORTH)
