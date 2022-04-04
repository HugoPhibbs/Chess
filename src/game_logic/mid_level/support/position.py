from __future__ import annotations

from typing import TYPE_CHECKING

if TYPE_CHECKING:
    from src.game_logic.pieces.piece import Piece
    from src.game_logic.helpers import CoordsHelper


class Position:
    """
    Represents a Position on a chessboard
    """

    __piece: 'Piece' = None

    def __init__(self, coords: tuple[int, int], coords_helper : 'CoordsHelper', piece: 'Piece' = None):
        """
        Constructor for a Position object

        :param coords: tuple for the coordinates of this position on a chess board. Expressed as a number pair, each
        number from 0-7, useful for indexing the board matrix
        :param coords_helper: CoordsHelper object to help with dealing with coordinates
        :param piece: Piece object that this position contains, leave empty if no piece present
        """
        self.coords_helper = coords_helper
        self.__set_coords(coords)
        self.piece = piece
    
    def __repr__(self) -> str:
        """
        Returns a string representation of this position

        :return: string as described
        """
        return self.__col_str() + self.__row_str()

    def __col_str(self) -> str:
        """
        Returns a string representation of the col of this position, as in an actual game of chess

        For example the first column is mapped to 'A', second to 'B' and so forth

        :return: str character as described
        """
        return chr(self.col + 65)

    def __row_str(self) -> str:
        """
        Returns a string representation of this row of this position, as in an actual game of chess

        For example, the first row 0 is mapped to 1, 1 to 2 and so forth

        :return: str character as described
        """
        return str(self.row + 1)

    @property
    def piece(self) -> 'Piece' | None:
        """
        The piece that currently occupies this position, None if there is nothing there

        :return: Piece object or None as described
        """
        return self.__piece

    @piece.setter
    def piece(self, val: 'Piece') -> None:
        """
        Sets which piece currently occupies this position

        :param val: Piece object to be set
        :return: None
        """
        self.__piece = val

    @property
    def coords(self) -> tuple[int, int]:
        """
        The coordinates that this position occupies

        :return: tuple of integers for the coordinates of this position
        """
        return self.__coords

    def __set_coords(self, val: tuple[int, int]):
        """
        Checks then sets the coordinates of this position

        :param val: tuple of integers to be checked if valid, then set as the coordinates of this position
        :return: None
        """
        assert self.coords_helper.coords_are_valid(val), "Inputted value for new coords for this position are not valid!, " \
                                                    "see Board.coords_are_valid(coords)"
        self.__coords = val

    @property
    def row(self) -> int:
        """
        The row that this Position is on

        :return: int as described
        """
        return self.coords[0]

    @property
    def col(self) -> int:
        """
        The col that this Position is on

        :return: int as described
        """
        return self.coords[1]

    @property
    def is_vacant(self) -> bool:
        """
        Finds if this position is vacant or not, ie if it contains a piece or not

        :return: bool as described
        """
        return self.piece is None

    def is_hostile(self, colour: str) -> bool:
        """
        Finds out if this position is occupied by a piece that has a colour that is opposite to the inputted piece

        By convention, an vacant position is not considered hostile, nor is it considered friendly

        :param colour: str for the colour of a Piece object to be checked if this Position contains an hostile piece to it
        :return: bool if this position is occupied by a enemy piece as described
        """
        if self.is_vacant:
            return False
        return self.piece.colour != colour

    def is_friendly(self, colour: str) -> bool:
        """
        Finds out if this position is occupied by a piece that is considered friendly to another piece

        By convention, if this position is vacant, it is not considered friendly, nor hostile

        :param colour: str for the colour of a piece that will be considered to be friendly to the colour of the piece
        on this board, if one exists
        :return: bool true if there is a piece on this position that has the same colour as inputted colour, otherwise false,
        see note above
        """
        if self.is_vacant:
            return False
        return self.piece.colour == colour

    def has_piece_type(self, piece_type: str) -> bool:
        """
        Finds out if this Position has a piece of a given type.

        False if this position contains no Piece, or not the right type

        :param piece_type: str for the type of piece as described
        :return: bool as described
        """
        if self.is_vacant:
            return False
        return self.piece.type == piece_type
