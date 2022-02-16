from __future__ import annotations
from typing import TYPE_CHECKING

if TYPE_CHECKING:
    from src.game_logic.mid_level.support.board import Board
    from src.game_logic.pieces.king import King
    from src.game_logic.helpers import BearingHelper
    from src.game_logic.helpers import TraverseHelper

from src.game_logic.mid_level.move_finders.knightmovefinder import KnightMoveFinder

#TODO intergrate this with the rest of the project!

class Check:
    """
    Class to find if a king is in check
    """

    def __init__(self, king: 'King', board: 'Board', bearing_helper: 'BearingHelper',
                 traverse_helper: 'TraverseHelper'):
        self.king = king
        self.board = board
        self.bearing_helper = bearing_helper
        self.traverse_helper = traverse_helper

    def king_in_check(self):
        pass

    def in_check_all_directions(self):
        """
        Determines if a king is in check considering all the directions that legally exist on a chessboard

        For example, North, East, South-West etc

        :return: bool if a King is in Check or not
        """
        all_bearings = self.bearing_helper.all_bearings()
        for bearing in all_bearings:
            if self.in_check_traverse(bearing):
                return True
        return False

    def in_check_traverse(self, bearing: str) -> bool:
        """
        Finds out if this king is in check for a given bearing across the chessboard.

        Does a DFS on coordinates from the position of this king, and finds if any pieces it encounters can attack this King

        :param bearing: str for traveling in a specified bearing across the chessboard
        :return: bool if this king is in check via the bearing of the inputted traverse
        """
        traverse_coords = self.traverse_helper.next_coords(self.king.coords, bearing)
        while self.board.coords_are_valid(traverse_coords):
            pos = self.board.get_position(traverse_coords)
            if pos.is_hostile(self.king.colour):
                if pos.piece.can_move_to_coords(self.king.coords, self.board, True):
                    return True
                break  # Blocks any enemy pieces from attacking this king in this bearing
            elif pos.is_friendly(self.king.colour):
                # Friendly piece in this position, blocks any attacks from enemy on this bearing
                return False
            traverse_coords = self.traverse_helper.next_coords(traverse_coords, bearing)
        return False

    def in_knight_check(self) -> bool:
        """
        Determines if a King object is in check by an enemy knight

        :return: bool if this king is in check by a knight
        """
        knight_coords = self.king.move_finder.filter_dest_coords(KnightMoveFinder.knight_move_coords(self.king.coords),
                                                                 attack_only=True)
        for coord in knight_coords:
            pos_at_coords = self.board.get_position(coord)
            if pos_at_coords.piece.type == "KNIGHT":
                return True
        return False
