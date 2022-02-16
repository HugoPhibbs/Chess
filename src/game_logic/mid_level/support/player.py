from __future__ import annotations
from typing import TYPE_CHECKING

if TYPE_CHECKING:
    from src.game_logic.pieces.piece import Piece
    from src.game_logic.pieces.king import King
    from src.game_logic.mid_level.moves.move import Move
    from src.game_logic.mid_level.support.board import Board


class Player:
    """
    Represents a Player in a game of chess
    """

    __moves: list['Move'] = []
    __king: 'King' = None

    def __init__(self, name: str, pieces: list['Piece' | 'King'], colour: str):
        """
        Constructor for a player Object

        :param name: str for the name of this player
        :param pieces: list of Piece objects that this player owns
        :param colour: str for the colour of pieces that this player has
        """
        self.name = name
        self.pieces = pieces
        self.colour = colour
        self.__set_king()

    def __set_king(self) -> None:
        """
        Sets the king for this Player

        :return: None
        """
        for piece in self.pieces:
            if piece.type == 'KING':
                assert piece.colour == self.colour
                self.__king = piece

    def is_in_check(self, board: 'Board') -> bool:
        """
        Finds out if this player is in check

        :param board: Board object for this current game of chess
        :return: bool as described
        """
        return self.__king.is_in_check(board)

    def is_checkmated(self, board: 'Board') -> bool:
        """
        Finds out if this Player has been checkmated or not

        :param board: Board object for this current game of chess
        :return: bool as described
        """
        if self.is_in_check(board):
            for piece in self.pieces:
                if piece.num_moves(board) > 0:
                    return False
            return True
        return False

    @property
    def king(self):
        return self.__king

    @property
    def colour(self) -> str:
        """
        The colour of pieces that this player has

        :return: str for the colour of pieces that this player has
        """
        return self.__colour

    @property
    def moves(self):
        return self.__moves

    def add_move(self, move: 'Move') -> None:
        """
        Adds a move that was completed by this player

        :param move:
        :return:
        """
        for piece in move.pieces:
            assert piece.colour == self.colour
        self.__moves.append(move)

    @property
    def most_recent_move(self) -> Move:
        """
        Self explanatory

        :return: Move object
        """
        return self.moves[-1]

    @colour.setter
    def colour(self, val: str) -> None:
        """
        Set the value of the colour of pieces that this player controls

        :param val: str for the colour of pieces as described
        :return: None
        """
        assert val in ["WHITE", "BLACK"]
        self.__colour = val

    @property
    def opponent_score(self) -> int:
        """
        Returns the score of the opponent player to this player,

        ie the value of the pieces that the opponent has captured

        :return: int as described
        """
        count = 0
        for piece in self.pieces:
            if piece.is_captured:
                count += piece.value
        return count
