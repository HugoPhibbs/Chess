from abc import ABC, abstractmethod

from classes.pieces.piece import Piece


class LimitedPiece(ABC, Piece):
    """
    Class to represent pieces that have limited range, specifically knights and pawn,
    other pieces, on the other hand, their range is limited by the board itself or by other pieces
    """

    @staticmethod
    @abstractmethod
    def moves(*args):
        """
        Abstract static method to return the possible moves that can be done by a limited range piece. This is intended to
        provide moves that can then be checked if they are valid or not

        Ignores the size of the board, valid checking is done by Board class

        :param args any arguments that may be needed for the implemenation of this method=
        :return:
        """
        pass