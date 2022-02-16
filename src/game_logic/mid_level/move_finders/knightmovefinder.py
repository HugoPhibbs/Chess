from __future__ import annotations
from typing import TYPE_CHECKING

if TYPE_CHECKING:
    from src.game_logic.pieces import Piece, Knight
    from src.game_logic.mid_level import Move, Board

from src.game_logic.mid_level.move_finders.movefinder import MoveFinder


class KnightMoveFinder(MoveFinder):
    """
    Finds the moves that a knight can during a game of chess
    """

    def __init__(self, knight: 'Piece' | 'Knight', board: 'Board'):
        """
        Creates a KnightMoveFinder object
        :param knight: Knight object to find the moves for
        :param board: Board object for this game of chess
        """
        super().__init__(knight, board)

    def _possible_moves(self) -> list['Move']:
        return self._create_standard_moves(self._dest_coords_list())

    def _dest_coords_list(self) -> list[tuple[int, int]]:
        return self.filter_dest_coords(self.knight_move_coords(self.piece.coords))

    @staticmethod
    def knight_move_coords(coords: tuple[int, int]) -> list[tuple[int, int]]:
        """
        Finds the possible coordinates that a knight could move to (or attack from), given inputted coordinates

        Implemented with coords as an input so to help to see if a king is in check via a knight, hence also why it is static

        :param coords: coords to find the move coordinates of a knight (or attack from)
        :return: list of tuples as described
        """
        row = coords[0]
        col = coords[1]
        return [(row - 2, col + 1),
                (row - 1, col + 2),
                (row - 2, col - 1),
                (row - 1, col - 2),
                (row + 1, col - 2),
                (row + 2, col - 1),
                (row + 2, col + 1),
                (row + 1, col + 2)]
