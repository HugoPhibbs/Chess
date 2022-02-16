from __future__ import annotations


class CoordsHelper:
    """
    Helper class to help with coordinates in a chess game
    """

    @staticmethod
    def add(first: tuple, second: tuple):
        """
        Adds two coordinates together.

        Coordinates are treated as position vectors

        :param first: tuple
        :param second: tuple
        :return: a new tuple of first and second added together
        """
        return first[0] + second[0], first[1] + second[1]

    @staticmethod
    def coords_are_valid(coords: tuple[int, int]) -> bool:
        """
        Checks if an inputted coordinate pair are valid or not

        :param coords: coordinate tuple pair
        :return: bool if inputted coords are valid or not
        """
        return CoordsHelper.__coords_are_coords(coords) and CoordsHelper.__coords_in_board(coords)

    @staticmethod
    def __coords_in_board(coords: tuple[int, int]) -> bool:
        """
        Finds out if a integer coordinate pair are on a chess board or not

        :param coords: tuple of length 2 with integer values to be checked
        :return: bool if the inputted coords are in the board or not
        """
        assert CoordsHelper.__coords_are_coords(coords), "These coords are not a 2d tuple integer pair!"
        return 0 <= coords[0] <= 7 and 0 <= coords[1] <= 7

    @staticmethod
    def __coords_are_coords(coords: tuple[int, int]) -> bool:
        """
        Checks if inputted coords are a 2d coordinate pair containing integers

        :param coords: tuple coordinate pair to be checked
        :return: bool if the inputted coords are valid or not
        """
        return coords is not None and isinstance(coords, tuple) \
               and len(coords) == 2 \
               and isinstance(coords[0], int) and isinstance(coords[1], int)


class BearingHelper:
    """
    Utility class to help with bearings on a chessboard
    """

    @staticmethod
    def diag_bearings() -> list[str]:
        """
        Return a list of possible diagonal bearing that a traverse can travel in

        :return: list of strings as described
        """
        return ["NE", "NW", "SE", "SW"]

    @staticmethod
    def straight_bearings() -> list[str]:
        """
        Return a list of possible straight bearing that a traverse can travel in

        :return: list of strings as described
        """
        return ["N", "E", "W", "S"]

    @staticmethod
    def all_bearings():
        """
        Return a list of possible straight bearing that a traverse can travel in

        :return: list of strings as described
        """
        return BearingHelper.diag_bearings() + BearingHelper.straight_bearings()


class TraverseHelper:
    """
    Class to help traverse across a chess board
    """

    def __init__(self):
        """
        Constructor for a Traverser object
        """
        pass

    def next_coords(self, coords: tuple, bearing: str):
        """
        Return the next coordinates in the direction of an inputted bearing

        :param coords: tuple for coordinates
        :param bearing: str for the bearing to travel in
        :return: a new pair of coordinates in the bearing specified
        """
        adjust_coords = self.__determine_adjust_coords_func(bearing)
        return adjust_coords(coords)

    def __determine_adjust_coords_func(self, bearing: str) -> callable:
        """
        Determines the function to adjust position that should be used when doing a dfs in a particular bearing

        :param bearing: str for the bearing as described
        :return: callable function that can be used to increment the position of a possible move by a piece
        """
        if bearing == "N":
            adjust_coords = self.__next_coords_func(1, 0)
        elif bearing == "S":
            adjust_coords = self.__next_coords_func(-1, 0)
        elif bearing == "E":
            adjust_coords = self.__next_coords_func(0, 1)
        elif bearing == "W":
            adjust_coords = self.__next_coords_func(0, -1)
        elif bearing == "NE":
            adjust_coords = self.__next_coords_func(1, 1)
        elif bearing == "SE":
            adjust_coords = self.__next_coords_func(-1, 1)
        elif bearing == "SW":
            adjust_coords = self.__next_coords_func(-1, -1)
        elif bearing == "NW":
            adjust_coords = self.__next_coords_func(-1, 1)
        else:
            raise Exception('Bearing is not valid, must be in {0}}'.format(bearing_helper.__all_bearings()))
        return adjust_coords

    def __next_coords_func(self, row_incr: int, col_incr: int) -> callable:
        """
        Provides an anonymous function that is used to increment a coordinate to the next possible one during a dfs to find
        possible coordinate destination for moves or other pieces

        A move is simply a tuple, (row, col) specifying a possible position that a piece could move
        row_incr and col_incr must be one of -1, 1 or 0

        :param row_incr: increment for how the row of a position should be updated
        :param col_incr: increment for how the col of a position should be updated
        :return: lambda function as described
        """
        # TODO does this even belong here??
        acceptable_increments = [1, -1, 0]
        assert row_incr in acceptable_increments and col_incr in acceptable_increments
        return lambda coords: CoordsHelper.add(coords, (row_incr, col_incr))

