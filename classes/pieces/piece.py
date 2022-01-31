from abc import ABC, abstractmethod

from classes.move import Move
from classes.position import Position


class Piece(ABC):
    """
    Class to represent a piece in chess

    Attributes
        is_captured: if a piece is captured or not
        position: position of piece on chessboard, None if it is not on a chessboard (aka not active or captured)
        value: value of this piece in a game of chess, useful for scoring
    """

    __is_captured = False
    __position = None

    def __init__(self, colour_: str, value, position: Position):
        """
        Constructor for a Piece object,

        :param colour_: colour for this piece
        :param value : value of this piece
        :param position : Position object of this piece
        """
        self.colour = colour_
        self.value = value
        self.position = position

    def piece_is_opponents(self, piece) -> bool:
        """
        Finds if an inputted piece belongs to the opponent

        :param piece: Piece object to be checked
        :return: bool if piece belongs to opponent or not
        """
        return piece.colour != self.colour

    def value_is_valid(val) -> bool:
        """
        Finds if the value for a piece is valid or not.

        Must be an integer greater than or equal to zero

        :param val: value of piece to be checked
        :return: bool if inputted value is valid or not
        """
        return isinstance(val, int) and val >= 0

    @staticmethod
    def colour_is_valid(val) -> bool:
        """
        Checks if an inputed colour value is valid or not

        :param val: value to be checked if it is a valid colour or not
        :return: bool as described
        """
        return val in ['WHITE', 'BLACK']

    @property
    def colour(self) -> str:
        """
        Getter for the colour of this Piece

        :return: str as described
        """
        return self.__colour

    @colour.setter
    def colour(self, val) -> bool:
        """
        Setter for the colour attribute of this Piece object

        value must be valid before being set

        :param val: value to be set
        :return: None
        """
        if Piece.colour_is_valid(val):
            self.__colour = val

    @property
    def is_captured(self) -> bool:
        """
        Getter for if this piece is captured or not by an opponent's piece

        :return: bool as described
        """
        return self.__is_captured

    @is_captured.setter
    def is_captured(self, val) -> None:
        """
        Setter for if a this piece is captured or not

        Value must be boolean

        :param val: value to be set
        :return: None
        """
        assert isinstance(val, bool)
        self.__is_captured = val

    @property
    def position(self):
        """"""
        return self.__position

    @position.setter
    def position(self, val):
        self.__position = val

    @abstractmethod
    @property
    def type(self) -> str:
        """
        Abstract method to return the string for the type of this Piece

        :return: str as described
        """
        pass

    @abstractmethod
    def __repr__(self) -> str:
        """
        Abstract method for the string representation of this Piece

        :return: str as described
        """
        pass

    @property
    def value(self) -> int:
        """
        Returns the value of this Piece, for scoring

        :return: int as described
        """
        return self.value

    @value.setter
    def value(self, val):
        assert Piece.value_is_valid(val)
        self.__value = val

    @property
    def move_distance_lim(self):
        return 8

    @abstractmethod
    def moves(self, board, ignore_friendly_check=False) -> list[Move]:
        """
        Abstract method to find the moves that this piece can do on a board at a particular state of a chess game

        :param board: Board object for a game of chess
        :param ignore_friendly_check bool for if any returned moves should ignore the prospect of putting a friendly king in check
        :return: list containing coordinate tuples of the possible coordinates on a chessboard that this piece can do
        """
        pass
        # TODO need way by pass checking that a move puts friendly king in check, unnecessary for checking if
        #  a piece is checking another piece

    @abstractmethod
    def can_move_to_coords(self, coords: tuple, board) -> bool:
        """
        Finds out if this Piece object can move to a given coordinate pair given that there is nothing in the way
        between them.

        Ignores fact that such move may put a friendly king into check

        :param coords: tuple containing two integers specifying the row and column of coordinates on a chessboard
        :return: bool if this Piece can move to inputted coords as described
        """
        for move in self.moves(board, ignore_friendly_check=True):
            if move.dest.coords == coords:
                return True
        return False

    def friendly_king_in_check(self) -> bool:
        """
        Finds out if the king belonging to the same player as this Piece is in check

        :return: bool as described
        """
        pass
