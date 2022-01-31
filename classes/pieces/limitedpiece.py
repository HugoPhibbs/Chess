from abc import ABC, abstractmethod

from classes.board import Board
from classes.pieces.piece import Piece


class LimitedPiece(ABC, Piece):
    """
    Class to represent pieces that have limited range, specifically knights and pawn,
    other pieces, on the other hand, their range is limited by the board itself or by other pieces
    """

    def valid_moves_limited(self, board : Board) -> list:
        """
        Return a list of the valid moves that can be done for a limited range piece

        :param board: Board object for a game of chess
        :return: list as described
        """
        possible_moves = self.moves()
        valid_moves = []
        for move in possible_moves:
            if self.move_is_valid(move, piece):
                valid_moves.append(move)
        return valid_moves
