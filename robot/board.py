class Board:
    """
    Immutable board class.

    Interrogate for height and width by attribute. These properties cannot be changed once created.
    """

    def __init__(self, width: int, height: int):
        self.width = width
        self.height = height
