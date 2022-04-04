from __future__ import annotations

from src.game_logic.pieces.piece import Piece
from typing import TYPE_CHECKING

if TYPE_CHECKING:
    from src.game_logic.mid_level.support.position import Position
    from src.game_logic.mid_level.move_finders.movefinder import MoveFinder
    from src.game_logic.pieces.king import King

class LimitedPiece(Piece):
    """
    Class to represent pieces that have limited range, specifically knights and pawn,
    other pieces, on the other hand, their range is limited by the board itself or by other pieces
    """

    def __init__(self, colour: str, move_finder : 'MoveFinder', value: int=0, king : 'King' | None =None, position: 'Position' | None = None):
        super().__init__(colour, move_finder, value, king, position)