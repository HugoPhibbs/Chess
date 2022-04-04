from src.game_logic.pieces.limitedpiece import LimitedPiece
from typing import TYPE_CHECKING

if TYPE_CHECKING:
    from src.game_logic.mid_level.move_finders.movefinder import MoveFinder

class King(LimitedPiece):
    """
    Class to represent a King piece in a game of chess
    """

    __king: 'King' = None

    def __init__(self, colour : str, move_finder : 'MoveFinder', value=0, king=None):
        """
        Constructor for a King piece, all constructor arguments are passed to Piece

        :param colour: string for the colour of this King
        :param move_finder: MoveFinder object that finds moves for this King
        :param value: int for the value of this king
        :param king: King object that is the king of this king
        """
        super().__init__(colour, move_finder, value, king)
        self.king = self

    @property
    def king(self) -> 'King':
        """
        The King object that is king to this king

        :return: 'King' object as described
        """
        return self.__king

    @king.setter
    def king(self, king) -> None:
        """
        Sets the king object for this King. This must be either None or this king itself

        :param king: King object as described
        :return: None
        """
        assert king is None or king == self, "King attribute for this king must be either None or this King itself!"
        self.__king = king

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
        ## TODO fix this bellow
        return self.in_knight_check(board) or self.in_check_all_directions(board)

