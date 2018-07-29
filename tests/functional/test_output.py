import subprocess
from unittest import TestCase


class TestOutput(TestCase):
    def test_example_one(self):
        """
        Test the first example given by the requirements document
        """
        expected = b"0,1,NORTH\n"

        completed = subprocess.run(["python3.6", "robot.py", "--file", "tests/provided/example1.txt"],
                                   stdout=subprocess.PIPE)

        self.assertEqual(0, completed.returncode)
        self.assertEqual(expected, completed.stdout)

    def test_example_two(self):
        expected = b"0,0,WEST\n"

        completed = subprocess.run(["python3.6", "robot.py", "--file", "tests/provided/example2.txt"],
                                   stdout=subprocess.PIPE)

        self.assertEqual(0, completed.returncode)
        self.assertEqual(expected, completed.stdout)

    def test_example_three(self):
        """
        Test the first example given by the requirements document
        """
        expected = b"3,3,NORTH\n"

        completed = subprocess.run(["python3.6", "robot.py", "--file", "tests/provided/example3.txt"],
                                   stdout=subprocess.PIPE)

        self.assertEqual(0, completed.returncode)
        self.assertEqual(expected, completed.stdout)

    def test_complex(self):
        """
        Test a complex contrived example.
        """
        expected = b"2,2,EAST\n4,4,SOUTH\n4,0,SOUTH\n"

        completed = subprocess.run(["python3.6", "robot.py", "--file", "tests/provided/complex.txt"],
                                   stdout=subprocess.PIPE)

        self.assertEqual(0, completed.returncode)
        self.assertEqual(expected, completed.stdout)
