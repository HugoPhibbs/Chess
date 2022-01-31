from abc import ABC, abstractmethod

from classes.board import Board
from classes.move import Move
from classes.pieces.piece import Piece


class RangedPiece(ABC, Piece):
    """
    For Types of pieces that have range that is only limited by other pieces and the board itself.

    Namely, this includes rook, bishops and queen pieces
    """

    @abstractmethod
    def move_directions(self) -> list:
        """
        Finds the directions that this piece can travel in.

        For example, if it were a rook, then the directions would be north, south, east and west

        :return: a list of directions that this piece can travel in, expressed as short string abbreviations
        """
        pass

    @property
    def straight_directions(self):
        """
        Finds the possible directions corresponding to the straight vectors on a chessboard
        :return: list of strings as described
        """
        return ["N", "E", "W", "S"]

    @property
    def diag_directions(self):
        """
        Finds the possible directions corresponding to the diagonal vectors on a chessboard

        :return: list of strings as described
        """
        return ["NE", "NE", "SE", "S"]

    def __dfs_moves(self, direction: str, board : Board) -> list[Move]:
        """
        Completes a dfs for the specified direction for this piece at a particular position.

        Returns all moves that are valid in this direction,

        For example, find the moves that a bishop at B4 can move in the north-east direction

        :param direction: str for the direction that is wished to travel
        :return: list of tuples containing the possible moves that can be done for a particular direction
        """
        # TODO, add support for Move object
        adjust_pos = RangedPiece.__determine_adjust_coord_func(direction)
        moves = []
        move = adjust_pos(self.position.coords)
        while board.move_is_legal(move, self):
            moves.append(move)
            move = adjust_pos(move)
        return moves

    @staticmethod
    def __adjust_coords_func(row_incr: int, col_incr: int) -> callable:
        """
        Provides an anonymous function that is used to increment a coordianate to the next possible one during a dfs to find
        possible coordinate destination for moves

        A move is simply a tuple, (row, col) specifying a possible position that a piece could move

        row_incr and col_incr must be one of -1, 1 or 0

        :param row_incr: increment for how the row of a position should be updated
        :param col_incr: increment for how the col of a position should be updated
        :return: lambda function as described
        """
        acceptable_directions = [1, -1, 0]
        assert row_incr in acceptable_directions and col_incr in acceptable_directions
        return lambda pos: (pos[0] + row_incr, pos[1] + col_incr)

