from __future__ import annotations

import math

from src.game_logic.mid_level.moves.move import Move
from typing import TYPE_CHECKING

if TYPE_CHECKING:
    from src.game_logic.mid_level.support.board import Board
    from src.game_logic.pieces.piece import Piece


class StandardMove(Move):
    """
    Represents a move that is standard for a chessboard (not a castling move)

    Just one piece traveling to another place on a chessboard, that may or may not capture another piece

    Attributes:
        Inherited attributes from Move
    """
    __capture : Piece | None =  None

    def __init__(self, board: 'Board', source_coords: tuple[int, int], dest_coords: tuple[int, int], capture_coords=None, can_capture : bool= True):
        """
        Constructor for a standard move

        :param board: Board object for this game of chess
        :param source_coords: coordinates for where this move starts
        :param dest_coords: coordinates for where this move ends
        :param capture_coords: coordinates for the piece that is being captured by this move.
         If left None, these are set to dest_coords. Aimed at supporting en-passant capturing
        :param can_capture: bool for if this Move can capture another piece or not. //TODO why is this necessary?
        """
        super().__init__(board, [board.get_position(source_coords).piece])
        self.source = board.get_position(source_coords)
        self.dest = board.get_position(dest_coords)
        self.piece = self.source.piece
        self.can_capture = can_capture
        self._set_capture(capture_coords)

    @property
    def can_capture(self) -> bool:
        """
        Property for if this standard move can capture a piece or not

        :return bool as described
        """
        return self.__can_capture

    @can_capture.setter
    def can_capture(self, can_capture : bool) -> None:
        """
        Setter for if this StandardMove can capture a piece or nto

        :param can_capture: bool for if this StandardMove an capture another piece or not
        :return: None
        """
        assert isinstance(can_capture, bool)
        self.__can_capture = can_capture

    @property
    def capture(self) -> 'Piece' | None:
        """
        The piece that this StandardMove captures. If it is none, then this move doesn't capture anything

        :return: Piece or None object as described
        """
        return self.__capture

    def _set_capture(self, capture_coords : tuple[int, int]) -> None:
        """
        Sets the capture object for this Move

        :return: None
        """
        if capture_coords is None:
            self.capture_pos = self.dest
        else:
            self.capture_pos = self.board.get_position(capture_coords)
            self.capture_piece = self.capture_pos.piece
            assert self.capture_piece is not None, "Capture coords specified with no piece at coords!"

    def _move_pieces(self) -> None:
        self.capture_pos.piece.reset_position()
        self.piece.swap_position(self.dest)

    def _reverse_moving_pieces(self) -> None:
        self.piece.swap_position(self.source)
        self.capture_piece.swap_position(self.capture_pos)

    def is_legal(self, ignore_friendly_check: bool = False) -> bool:
        """
        Finds out if this move is legal or not.

        Ignores that the dest and source may not have a line of sight to each other, this is assumed, except for knights

        :param: ignore_friendly_check: bool for if it should be checked if this move causes a friendly check. Useful for
        checking if the opposing king is under attack.
        :return: bool as described
        """
        if self.__dest_is_friendly_blocked():
            return False
        return super().is_legal(ignore_friendly_check)

    def __dest_is_friendly_blocked(self) -> bool:
        """
        Finds out if this piece is blocked at the destination by a friendly piece

        :return: bool for if this move's destination is blocked by a friendly piece
        """
        return not (self.dest.is_vacant or self.dest.is_hostile(self.piece.colour))

    def length(self) -> int:
        """
        The length of this move.

        Uses pythagoras's theorem

        :return: int as described
        """
        return int(math.sqrt((self.source.row-self.dest.row)**2+(self.source.col-self.dest.col)**2))

    def type(self) -> str:
        return "STANDARD"

