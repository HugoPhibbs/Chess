from __future__ import annotations
from abc import ABC, abstractmethod
from typing import TYPE_CHECKING

if TYPE_CHECKING:
    from src.game_logic.mid_level.support.position import Position
    from src.game_logic.mid_level.support.board import Board
    from src.game_logic.mid_level.moves.move import Move
    from src.game_logic.pieces.king import King
    from src.game_logic.mid_level.move_finders.movefinder import MoveFinder


class Piece(ABC):
    """
    Class to represent a piece in chess

    Attributes
        is_captured: if a piece is captured or not
        value: value of this piece in a game of chess, useful for scoring
        #TODO
    """

    __is_captured = False
    __has_moved : bool = False
    _completed_moves : list['Move'] =  False

    def __init__(self, colour: str, move_finder : 'MoveFinder', value: int = 0, king: 'King' | None = None, position: 'Position' = None):
        """
        Constructor for a Piece object,

        :param colour: colour for this piece
        :param value : value of this piece, default 0
        :param king: king of this piece in a game of chess
        """
        super().__init__()
        self.colour = colour
        self.move_finder = move_finder
        self.value = value
        self.king = king
        self.position = position
        move_finder.piece = self

    def post_move_updates(self, move : 'Move') -> None:
        """
        Updates the state of this Piece once a move has been completed for this piece

        :param move: Move object that has just been executed
        :return: None
        """
        self._completed_moves.append(move)
        if not self.has_moved:
            self.has_moved = True

    def num_moves(self, board : 'Board') -> int:
        """
        Finds the number of moves that this piece can (legally do)

        :param board: Board object for current game of chess
        :return: int
        """
        return len(self.moves(board))

    @property
    def position(self):
        return self.__position

    @position.setter
    def position(self, val : Position) -> None:
        self.__position = val

    @property
    def curr_coords(self) -> tuple[int, int]:
        """
        Returns the current coordinates of this piece

        :return: tuple with 2 integers specifying the position of this piece on the chessboard
        """
        assert self.position is not None, "The position attribute for this piece is None!"
        return self.position.coords

    def piece_is_opponents(self, piece) -> bool:
        """
        Finds if an inputted piece belongs to the opponent

        :param piece: Piece object to be checked
        :return: bool if piece belongs to opponent or not
        """
        return piece.colour != self.colour

    @staticmethod
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
    def colour(self, val) -> None:
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
    @abstractmethod
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

    @abstractmethod
    def str_abr(self) -> str:
        """
        Return a abbreviated string desbrining the type of this piece
        :return: str as described
        """
        pass

    @property
    def value(self) -> int:
        """
        Returns the value of this Piece, for scoring

        :return: int as described
        """
        return self.__value

    @value.setter
    def value(self, val) -> None:
        assert Piece.value_is_valid(val)
        self.__value = val

    def moves(self, ignore_friendly_check=False) -> list['Move']:
        """
         Method to find the moves that this piece can do on a board at a particular state of a chess game

        :param ignore_friendly_check bool for if any returned moves should ignore the prospect of putting a friendly king in check
        :return: list containing coordinate tuples of the possible coordinates on a chessboard that this piece can do
        """
        return self.move_finder.moves(ignore_friendly_check)

    def can_attack_coords(self, coords : tuple[int, int]) -> bool:
        """
        Finds if this Piece can attack a pair of coordinates on a chessboard

        :param coords: coords on a chessboard
        :return: bool as described
        """
        return self.move_finder.can_attack_coords(coords)

    def swap_position(self, position : 'Position') -> None:
        """
        Swaps the position object for this Piece. Also changes the piece attribute of the inputted position to this Piece

        :param position: Position object
        :return: None
        """
        assert position is not None, "Inputted position cannot be None!, see Piece.reset_position() instead!"
        if self.position is not None:
            self.position.piece = None
        self.position = position
        position.piece = self

    def reset_position(self) -> None:
        """
        Resets the position attribute of this piece.

        Updates piece object on the position end too
        :return:
        """
        self.position.piece = None
        self.position = None

    def change_position(self, new_coords : tuple[int, int], board : 'Board') -> None:
        """
        Changes the position object of this Piece to the Position object occupying the inputted coordinates

        :param new_coords: tuple for coordinates on a chessboard
        :param board: Board object for a game of chess
        :return: None
        """
        assert board.coords_are_valid(new_coords)
        self.swap_position(board.get_position(new_coords))

    @property
    def coords(self) -> tuple[int, int]:
        return self.position.coords

    @property
    def has_moved(self) -> bool:
        return self.__has_moved

    @has_moved.setter
    def has_moved(self, val) -> None:
        assert isinstance(val, bool)
        self.has_moved = val