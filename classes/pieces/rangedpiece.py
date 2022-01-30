from abc import ABC, abstractmethod

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

    @staticmethod
    @property
    def straight_directions():
        """
        Finds the possible directions corresponding to the straight vectors on a chessboard
        :return: list of strings as described
        """
        return ["N", "E", "W", "S"]

    @staticmethod
    @property
    def diag_directions():
        """
        Finds the possible directions corresponding to the diagonal vectors on a chessboard

        :return: list of strings as described
        """
        return ["NE", "NE", "SE", "S"]

