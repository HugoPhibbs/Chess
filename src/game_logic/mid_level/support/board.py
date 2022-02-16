from __future__ import annotations
from typing import TYPE_CHECKING

if TYPE_CHECKING:
    from src.game_logic.mid_level.support.position import Position


class Board:
    """
    Class to represent a Board object in a game of chess
    """

    __board_mat : list = None

    def __init__(self, board_mat: list):
        """
        Initializer for a  Board Object

        :param board_mat: matrix containing Position objects representing the actual board in a chess game
        """
        self.__set_board_mat(board_mat)

    def get_position(self, coords: tuple) -> Position:
        """
        Returns the Position object that is located at a coordinate pair for this Board

        :param coords: tuple for the coordinates of a position on this board, must be valid as per Position.coords_is_valid(val)
        :return: Position object as described
        """
        assert self.coords_are_valid(coords), "These coordinates are not valid!"
        return self.board_mat[coords[0]][coords[1]]

    def add_position(self, position: 'Position') -> None:
        """
        Adds a position object to this chessboard according to the coordinates of the inputted position object

        :param position: Position object to be added
        :return: Noneg
        """
        self.board_mat[position.coords[0]][position.coords[1]] = position

    @property
    def board_mat(self):
        return self.__board_mat

    def __set_board_mat(self, val):
        self.__board_mat = val

    @staticmethod
    def coords_are_valid(coords: tuple[int, int]) -> bool:
        """
        Checks if an inputted coordinate pair are valid or not

        :param coords: coordinate tuple pair
        :return: bool if inputted coords are valid or not
        """
        return Board.__coords_are_coords(coords) and Board.coords_in_board(coords)

    @staticmethod
    def coords_in_board(coords: tuple[int, int]) -> bool:
        """
        Finds out if a integer coordinate pair are on a chess board or not

        :param coords: tuple of length 2 with integer values to be checked
        :return: bool if the inputted coords are in the board or not
        """
        assert Board.__coords_are_coords(coords), "These coords are not a 2d tuple integer pair!"
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

    def get_row(self, row) -> list[Position]:
        """
        Returns a list of the Positon objects for a particular row

        :param row: int for the row to be returned
        :return: list of Position objects as described
        """
        return self.board_mat[row]
