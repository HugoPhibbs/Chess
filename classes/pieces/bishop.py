from classes.pieces.piece import Piece
from classes.pieces.rangedpiece import RangedPiece


class Bishop(RangedPiece):
    """
    Represents a bishop piece in a game of chess
    """

    def __init__(self, *args):
        """
        Constructor for a Bishop piece, all constructor arguments are passed to Piece

        :param args: parameters for the parent constructor of a Piece object
        """
        super().__init__(*args)

    @property
    def type(self):
        """
        Returns the type of this Piece, overrides type() from Piece

        :return: string describing the type of piece that this Bishop piece is
        """
        return "BISHOP"

    def __repr__(self) -> str:
        """
        Returns a string representation of itself

        :return: str as described
        """
        return "B"

    def move_directions(self):
        """
        Finds the list of directions that this Bishop can travel in.

        Implements RangedPiece.move_directions()

        :return: list of string objects that describe the directions that this piece can travel in
        """
        return self.diag_directions

    @property
    def value(self) -> int:
        """
        Returns value of this piece, for scoring
        :return: int as described
        """
        return 3
