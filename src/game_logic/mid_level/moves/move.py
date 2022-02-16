from __future__ import annotations
from typing import TYPE_CHECKING
from abc import ABC, abstractmethod

if TYPE_CHECKING:
    from src.game_logic.mid_level.support.board import Board
    from src.game_logic.pieces.piece import Piece


class Move(ABC):
    """
    Class to represent a Move on a chessboard

    Attributes:
        can_capture: Bool for if this Move can capture another piece or not. This is mainly aimed at pawns, which can't
        capture pieces on a forward move.
    """

    __executed: bool = False

    def __init__(self, board: 'Board', pieces: list['Piece']):
        """
        Constructor for a Move object

        :param board: Board object for a game of chess
        :param pieces: list of pieces that are moved as part of this move. Used as list, since in castling two pieces move
        """
        self.board = board
        self.pieces = pieces

    @property
    def executed(self) -> bool:
        """
        Find out if this Move as been executed or not

        :return: bool as described
        """
        return self.__executed

    def execute(self, check_legal: bool = True, ignore_friendly_check: bool = False, is_test: bool = False) -> None:
        """
        Executes this move.

        :param check_legal: bool check if this move is legal or not before executing, default True
        :param ignore_friendly_check: bool for if this Move should be checked to cause a friendly check before execution,
        useful for checking if an opposing king is under attack. Only needs to be specified if check_legal is True
        :param is_test: bool for if this move is being executed to test if this move causes a friendly check
        :return: None
        """
        self.pre_execute_checks(check_legal, ignore_friendly_check)
        self._move_pieces()
        self.__post_execute_updates(is_test)

    def __post_execute_updates(self, is_test: bool = False) -> None:
        """
        Handles updating the state a chess game once the movement of pieces has been executed

        :param is_test bool for if the move was executed in order to test if it causes a friendly check
        :return: None
        """
        self.__executed = True
        if not is_test:
            for piece in self.pieces:
                piece.post_move_updates(self)

    @abstractmethod
    def _move_pieces(self) -> None:
        """
        Handles actually the piece(s) involved in this move, and any capturing that may need to be done

        :return: None
        """
        pass

    def pre_execute_checks(self, check_legal, ignore_friendly_check) -> None:
        """
        Checks if a move can be executed before executing, raises an error if not.

        Intended to be called just before a move is executed
        :param check_legal: bool for if this move should be checked if it is legal or not
        :param ignore_friendly_check: bool for if this move should be checked to cause a friendly check
        :return: None
        """
        if check_legal:
            assert self.is_legal(ignore_friendly_check), "Move is not legal!"
        assert self.executed is False, "Move has already been executed!"

    def _reverse(self) -> None:
        """
        Reverses this move

        :return: None
        """
        self.__pre_reverse_checks()
        self._reverse_moving_pieces()
        self.__post_reverse_updates()

    def __post_reverse_updates(self) -> None:
        """
        Handles updating the state a chess game once the movement of pieces has been reversed

        :return: None
        """
        self.__executed = False
        for piece in self.pieces:
            piece.has_moved = True

    def __pre_reverse_checks(self):
        """
        Checks if this move can be reversed

        Throws an error if not
        :return:
        """
        assert self.executed is True, "Move hasn't been executed yet!"

    @abstractmethod
    def _reverse_moving_pieces(self) -> None:
        """
        Reverses any moving of pieces on the chessboard that this Move may have done, and any capturing that may
        have occurred

        :return: None
        """
        pass

    def is_legal(self, ignore_friendly_check: bool = False) -> bool:
        """
        Finds out if this move is legal or not.

        Intended to be overridden and called again by classes implementing the move class

        :param: ignore_friendly_check: bool for if it should be checked if this move causes a friendly check. Useful for
        checking if the opposing king is under attack.
        :return: bool as described
        """
        if not ignore_friendly_check:
            return self.__causes_friendly_check()
        return True

    def __causes_friendly_check(self) -> bool:
        """
        Finds out if this move causes a friendly check or not

        :return: bool if this Move causes a friendly check or not
        """
        self.execute(check_legal=False, is_test=True)
        if self.pieces[0].king.is_in_check(self.board):
            self._reverse()
            return False
        self._reverse()
        return True

    @abstractmethod
    def length(self) -> int:
        """
        Length of this move.

        :return: length of this move, rounded to the nearest integer
        """
        pass

    @abstractmethod
    def type(self) -> str:
        """
        Type of move this is, implemented to avoid isinstance()
        :return:
        """
        pass


