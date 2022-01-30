from classes.pieces.limitedpiece import LimitedPiece

class Knight(LimitedPiece):

    def __init__(self, *args):
        """
        Constructor for a knight piece, all constructor arguments are passed to Piece

        :param args: parameters for the parent constructor of a Piece object
        """
        super().__init__(*args)

    @property
    def type(self):
        """
        Returns the type of this Piece, overrides type() from Piece

        :return: string describing the type of piece that this knight piece is
        """
        return "KNIGHT"

    def __repr__(self) -> str:
        """
        Returns a string representation of itself

        :return: str as described
        """
        return "KT"

    @property
    def value(self) -> int:
        return 3

    @staticmethod
    def moves(pos):
        return