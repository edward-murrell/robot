import subprocess
from unittest import TestCase


class TestOutput(TestCase):
    def test_example_one(self):
        expected = "0,1,NORTH"

        completed = subprocess.run(["python3.6", "robot.py", "--file", "tests/provided/example1.txt"])

        self.assertEqual(0, completed.returncode)

