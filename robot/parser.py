from robot import Robot, Aim


class Parser:
    def __init__(self, robot: Robot):
        self.__robot = robot
        self.__map = {
            'NORTH': Aim.NORTH,
            'SOUTH': Aim.SOUTH,
            'EAST': Aim.EAST,
            'WEST': Aim.WEST
        }

    def read(self, line: str):
        if line == 'MOVE':
            self.__robot.move()
        elif line == 'LEFT':
            self.__robot.turn_left()
        elif line == 'RIGHT':
            self.__robot.turn_right()
        elif line == 'REPORT':
            return self.__robot.report()
        elif line[:6] == 'PLACE ':
            self.__place(line)

    def __place(self, line: str):
        parameters = line[6:].split(',')
        if len(parameters) != 3:
            return
        if parameters[0].isdigit() and parameters[1].isdigit() and parameters[2] in self.__map:
            x = int(parameters[0])
            y = int(parameters[1])
            facing = self.__map[parameters[2]]
            self.__robot.place(x, y, facing)
