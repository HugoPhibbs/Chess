from classes.pieces.piece import Piece
from classes.pieces.rangedpiece import RangedPiece


class Queen(Piece, RangedPiece):

    def move_directions(self) -> list:
        return self.straight_directions + self.diag_directions

    def __init__(self, *args):
        """
        Constructor for a queen piece, all constructor arguments are passed to Piece

        :param args: parameters for the parent constructor of a Piece object
        """
        super().__init__(*args)

    @property
    def type(self):
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
        return "Q"

    @property
    def value(self) -> int:
        return 9

