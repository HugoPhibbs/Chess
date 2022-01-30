from classes.pieces.piece import Piece
from classes.pieces.rangedpiece import RangedPiece


class King(Piece, RangedPiece):

    def move_directions(self) -> list:
        pass

    def __init__(self, *args):
        """
        Constructor for a King piece, all constructor arguments are passed to Piece

        :param args: parameters for the parent constructor of a Piece object
        """
        super().__init__(*args)

    @property
    def type(self):
        """
        Returns the type of this Piece, overrides type() from Piece

        :return: string describing the type of piece that this King piece is
        """
        return "KING"

    def __repr__(self) -> str:
        """
        Returns a string representation of itself

        :return: str as described
        """
        return "K"

    def value(self) -> int:
        return 0

    def move_distance_lim(self):
        return 1
