from src.game_logic.pieces.limitedpiece import LimitedPiece
from typing import TYPE_CHECKING

if TYPE_CHECKING:
    from src.game_logic.mid_level.moves.move import Move
    from src.game_logic.mid_level.support.board import Board
    from src.game_logic.mid_level.move_finders.movefinder import MoveFinder


class Knight(LimitedPiece):
    """
    Represents a Knight piece on a chessboard
    """

    def __init__(self, colour: str, move_finder : 'MoveFinder', value: int = 0, king=None):
        """
        Constructor for a knight piece, all constructor arguments are passed to Piece

        :param args: parameters for the parent constructor of a Piece object
        """
        super().__init__(colour, move_finder, value, king)

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
        return "Knight"

    def str_abr(self) -> str:
        return "KT"