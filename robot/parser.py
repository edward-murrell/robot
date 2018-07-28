from robot import Robot, Aim


class Parser:
    """
    Parse lines into robot commands.
    """

    def __init__(self, robot: Robot):
        """
        Wrap a parser around a robot object.

        :param robot: Constructed Robot object.
        """
        self.__robot = robot
        self.__map = {
            'NORTH': Aim.NORTH,
            'SOUTH': Aim.SOUTH,
            'EAST': Aim.EAST,
            'WEST': Aim.WEST
        }

    def read(self, line: str):
        """
        Parse an input line.

        This method assumes that lines of a file have been stripped of newlines.

        :param line:
        :return: None, or str if returned by REPORT commands.
        """
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
        """
        Call robot.place() with parameters if the parameters are valid.

        This method assumes that the first six characters are 'PLACE '.

        :param line: A line in the format 'PLACE X,Y,DIRECTION', where X & Y are positive integers, and DIRECTION is one
         one of NORTH, SOUTH, EAST, WEST.
        """
        parameters = line[6:].split(',')
        if len(parameters) != 3:
            return
        if parameters[0].isdigit() and parameters[1].isdigit() and parameters[2] in self.__map:
            x = int(parameters[0])
            y = int(parameters[1])
            facing = self.__map[parameters[2]]
            self.__robot.place(x, y, facing)
