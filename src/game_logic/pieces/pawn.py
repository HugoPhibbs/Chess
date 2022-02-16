from src.game_logic.pieces.limitedpiece import LimitedPiece
from typing import TYPE_CHECKING

if TYPE_CHECKING:
    from src.game_logic.mid_level.support.position import Position
    from src.game_logic.mid_level.support.board import Board
    from src.game_logic.mid_level.moves.move import Move
    from src.game_logic.pieces.king import King


class Pawn(LimitedPiece):
    """
    Represents a pawn piece in a game of chess
    """

    def __init__(self, colour: str, value: int = 0, king: 'King' = None, position: 'Position' = None):
        """
        Constructor for a Pawn piece, all constructor arguments are passed to Piece

        """
        super().__init__(colour, value, king, position)

    @property
    def type(self):
        """
        Returns the type of this Piece, overrides type() from Piece

        :return: string describing the type of piece that this Pawn piece is
        """
        return "PAWN"

    def __repr__(self) -> str:
        """
        Returns a string representation of itself

        :return: str as described
        """
        return "Pawn"

    def str_abr(self) -> str:
        return "P"

    def post_move_updates(self, move : 'Move') -> None:
        raise NotImplemented

    @property
    def just_double_moved(self) -> bool:
        """
        If this pawn has just double moved, and is the most recent move from this pawn's player

        :return: bool as described
        """
        most_recent_move = self.player.most_recent_move
        return most_recent_move.pieces[0] == self and most_recent_move.length == 2

    @property
    def player(self) -> 'Player':
        return self.__player

    @player.setter
    def player(self, player: 'Player') -> None:
        """"""
        self.__player = player

    def __has_moved(self) -> bool:
        """
        Finds if this Pawn has moved or not

        :return: bool if this Pawn has moved or not
        """
        return not ((self.colour == 'WHITE' and self.position.row == 1) or (
                self.colour == 'BLACK' and self.position.row == 7))


