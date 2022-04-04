from __future__ import annotations
from src.game_logic.mid_level.moves.move import Move
from typing import TYPE_CHECKING

if TYPE_CHECKING:
    from src.game_logic.mid_level.support.board import Board
    from src.game_logic.pieces.king import King
    from src.game_logic.pieces import Rook


class Castle(Move):
    """
    Class to support castling

    This class simply a king and a rook as in castling.

    The instructions on which coordinates to move the king and rook to are provided my KingMoveFinder
    """
    __side: str = ""

    def __init__(self, board: 'Board', king: 'King', rook: 'Rook', king_dest_coords: tuple, rook_dest_coords: tuple):
        """
        Constructor for a Castle Move

        :param board: Board object for a game of chess
        :param king: King object to be moved by this Castling
        :param rook : Rook involved in this castling
        """
        super().__init__(board, [rook, king], can_capture=False)
        assert king.colour == rook.colour, "Rook and king must be same colour in castling!"
        assert rook is not None, "Rook cannot be None!"
        self.king = king
        self.rook = rook
        self.king_dest_coords = king_dest_coords
        self.rook_dest_coords = rook_dest_coords
        self.king_source_coords = king.coords
        self.rook_source_coords = rook.coords

    def __repr__(self) -> str:
        return "{colour} king with {rook}".format(colour=self.king.colour, rook=self.rook)

    def _move_pieces(self) -> None:
        self.rook.swap_position(self.board.get_position(self.rook_dest_coords))
        self.king.swap_position(self.board.get_position(self.king_dest_coords))

    def length(self) -> int:
        """
        Finds the length of this castling move.

        By convention, this just returns 0
        :return:
        """
        return 0

    def type(self) -> str:
        return "CASTLE"

    def _reverse_moving_pieces(self) -> None:
        self.rook.swap_position(self.board.get_position(self.rook_source_coords))
        self.king.swap_position(self.board.get_position(self.king_source_coords))
