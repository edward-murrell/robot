from robot import Parser


class FileToFileRunner:
    """
    Program runner. Takes a parser w/h robot, reads a file, and sends results to the outfile.
    """

    def __init__(self, infile, outfile, parser: Parser):
        """

        :param infile: Open input file handle.
        :param outfile: Open output file handle.
        :param parser: Populated Parser object.
        """
        self.__input_file = infile
        self.__output_file = outfile
        self.__parser = parser

    def run(self):
        """
        Run instructions from infile.
        """
        line = self.__input_file.readline()
        while line:
            line = line.rstrip()
            output = self.__parser.read(line)
            if output:
                self.__output_file.write(output)
            line = self.__input_file.readline()