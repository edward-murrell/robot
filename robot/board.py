class Board:
    """
    Immutable board class.

    Interrogate for height and width by attribute. These properties cannot be changed once created.
    """

    def __init__(self, width: int, height: int):
        """
        Create a board object.

        Height and width cannot be changed after board creation.

        :param width: Width of board in squares.
        :param height: Height of board in squares.
        """
        self.__dict__['width'] = width
        self.__dict__['height'] = height

    def __setattr__(self, key, value):
        """
        Throw errors when setting height or width.

        All other properties are ignored.

        :param key: 'height' or 'width'
        :param value: Ignored.
        """
        if key in ('width', 'height'):
            raise ValueError(f'Board {key} cannot be changed after creation.')
