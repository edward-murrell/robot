from robot import Parser
from unittest import TestCase


class TestParser(TestCase):
    """
    Tests for turning textual commands into a parsed command.
    """

    def test_creation(self):
        """
        First test for creating parser.
        """
        parser = Parser()
