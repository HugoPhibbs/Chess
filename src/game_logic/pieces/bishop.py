from src.game_logic.pieces.rangedpiece import RangedPiece

class Bishop(RangedPiece):
    """
    Represents a bishop piece in a game of chess
    """

    def __init__(self, colour, value=0, king=None):
        """
        Constructor for a Bishop piece, all constructor arguments are passed to Piece

        """
        super().__init__(colour, value, king)

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
        return "Bishop"

    def str_abr(self) -> str:
        return "B"

    def bearings(self) -> list[str]:
        return self.bearing_helper.diag_bearings()
