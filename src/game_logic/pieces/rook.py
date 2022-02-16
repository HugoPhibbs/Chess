from src.game_logic.pieces.rangedpiece import RangedPiece
from typing import TYPE_CHECKING

if TYPE_CHECKING:
    pass


class Rook(RangedPiece):
    """
    Represents a rook piece in a game of chess
    """

    is_castleable : bool = False

    def __init__(self, colour, value=0, king=None):
        """
        Constructor for a Rook piece, all constructor arguments are passed to Piece

        :param args: parameters for the parent constructor of a Piece object
        """
        super().__init__(colour, value, king)

    @property
    def type(self):
        """
        Returns the type of this Piece, overrides type() from Piece

        :return: string describing the type of piece that this Rook piece is
        """
        return "ROOK"

    def __repr__(self) -> str:
        """
        Returns a string representation of itself

        :return: str as described
        """
        return "Rook"

    def str_abr(self) -> str:
        return "R"

    def bearings(self) -> list[str]:
        return self.bearing_helper.straight_bearings()
