from src.game_logic.pieces.limitedpiece import LimitedPiece
from typing import TYPE_CHECKING

if TYPE_CHECKING:
    from src.game_logic.mid_level.moves import Move
    from src.game_logic.mid_level.support.board import Board

class King(LimitedPiece):

    def __init__(self, colour, move_finder : 'MoveFinder', value=0, king=None):
        """
        Constructor for a King piece, all constructor arguments are passed to Piece

        """
        super().__init__(colour, move_finder, value, king)
        self.king = self

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
        return "King"

    def str_abr(self):
        return "KG"

    def is_in_check(self, board) -> bool:
        """
        Finds out if this king Piece is in Check or not

        :param board: Board object being used for a chess game
        :return: bool for if this King is in check or not
        """
        return self.in_knight_check(board) or self.in_check_all_directions(board)

