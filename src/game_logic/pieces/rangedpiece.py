from __future__ import annotations
from abc import abstractmethod
from src.game_logic.pieces.piece import Piece
from typing import TYPE_CHECKING

if TYPE_CHECKING:
    from src.game_logic.mid_level.support.board import Board
    from src.game_logic.mid_level.moves.move import Move
    from src.game_logic.pieces.king import King
    from src.game_logic.mid_level.support.position import Position
    from src.game_logic.helpers import BearingHelper
    from src.game_logic.mid_level.move_finders.movefinder import MoveFinder


class RangedPiece(Piece):
    """
    For Types of pieces that have range that is only limited by other pieces and the board itself.
    Namely, this includes rook, bishops and queen pieces
    """

    def __init__(self, colour: str, move_finder: 'MoveFinder', bearing_helper : 'BearingHelper', value : int =0, king: 'King' | None = None, position: 'Position' | None = None):
        """
        Constructor for a RangedPiece object

        :param colour: str for the colour of this ranged piece
        :param value: int for the value of this piece in a game of chess
        :param king: King object that this piece is on the same side on, default None
        :param position: Position object that this piece currently occupies, default None
        """
        super().__init__(colour, move_finder,  value, king, position)
        self.bearing_helper = bearing_helper

    @abstractmethod
    def bearings(self):
        """
        The bearings that this RangedPiece can travel in
        :return: str of bearings as described
        """
        pass