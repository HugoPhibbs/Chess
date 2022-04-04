from __future__ import annotations

from src.game_logic.pieces.rangedpiece import RangedPiece
from typing import TYPE_CHECKING

if TYPE_CHECKING:
    from src.game_logic.pieces.king import King
    from src.game_logic.mid_level.support.position import Position
    from src.game_logic.mid_level.move_finders.movefinder import MoveFinder
    from src.game_logic.helpers import BearingHelper


class Queen(RangedPiece):
    """
    Represents a chess piece on a chessboard
    """

    def __init__(self, colour: str, move_finder : 'MoveFinder', bearing_helper : 'BearingHelper', value: int = 0, king: 'King' | None = None, position: 'Position' | None = None):
        """
        Constructor for a queen piece, all constructor arguments are passed to Piece

        """
        super().__init__(colour, move_finder, bearing_helper, value, king, position)

    @property
    def type(self) -> str:
        """
        Returns the type of this Piece, overrides type() from Piece

        :return: string describing the type of piece that this Queen piece is
        """
        return "QUEEN"

    def __repr__(self) -> str:
        """
        Returns a string representation of itself

        :return: str as described
        """
        return "Queen"

    def str_abr(self) -> str:
        return "Q"

    def bearings(self) -> list:
        return self.bearing_helper.all_bearings()
