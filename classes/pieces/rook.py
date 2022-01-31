from classes.pieces.piece import Piece
from classes.pieces.rangedpiece import RangedPiece


class Rook(RangedPiece):
    """
    Represents a rook piece in a game of chess
    """

    def __init__(self, *args):
        """
        Constructor for a Rook piece, all constructor arguments are passed to Piece

        :param args: parameters for the parent constructor of a Piece object
        """
        super().__init__(*args)

    def move_directions(self) -> list:
        """
        See RangedPiece.move_directions()
        :return:
        """
        return self.straight_directions

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
        return "R"
