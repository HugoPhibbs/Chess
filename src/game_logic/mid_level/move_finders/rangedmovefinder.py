from __future__ import annotations
from typing import TYPE_CHECKING

if TYPE_CHECKING:
    from src.game_logic.pieces import Piece
    from src.game_logic.pieces import RangedPiece
    from src.game_logic.mid_level.support.board import Board
    from src.game_logic.helpers import TraverseHelper
    from src.game_logic.mid_level.moves import Move

from src.game_logic.mid_level.move_finders.movefinder import MoveFinder


class RangedMoveFinder(MoveFinder):
    """
    Finds the moves that a Ranged Piece can do in a game of chess
    """

    def __init__(self, ranged_piece: 'Piece' | 'RangedPiece', board: 'Board', traverse_helper : 'TraverseHelper'):
        super().__init__(piece=ranged_piece, board=board)
        assert ranged_piece.type in ['BISHOP', 'QUEEN', 'ROOK'], "Inputted piece type must be a ranged piece!"
        self.traverse_helper = traverse_helper

    def _possible_moves(self) -> list['Move']:
        return self._create_standard_moves(self._dest_coords_list())

    def _dest_coords_list(self) -> list[tuple[int, int]]:
        move_coords = []
        for bearing in self.piece.bearings():
            move_coords += self.__dfs_coords(bearing)
        return self.filter_dest_coords(move_coords)

    def __dfs_coords(self, bearing: 'str') -> list[tuple]:
        """
        Completes a dfs for the specified Traverse for a piece at a particular position.
        Returns all moves that are valid in the bearing of this Traverse

        For example, find the moves that a bishop at B4 can move in the north-east bearing

        :param bearing: str for the bearing of this dfs on a chessboard
        :return: list of tuples containing the possible moves that can be done for a particular bearing
        """
        assert bearing in self.piece.bearings(), "This bearing is not in the known bearings of this Ranged Piece!"
        move_coords: list[tuple] = []
        traverse_coords: tuple = self.traverse_helper.next_coords(self.piece.coords, bearing)
        while self.board.coords_in_board(traverse_coords):
            if self.board.get_position(traverse_coords).is_friendly(self.piece.colour):  # Friendly pieces block moves
                break
            move_coords.append(traverse_coords)
            traverse_coords = self.traverse_helper.next_coords(traverse_coords, bearing)
        return move_coords

