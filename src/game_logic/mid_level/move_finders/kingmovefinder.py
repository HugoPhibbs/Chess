from __future__ import annotations
from typing import TYPE_CHECKING

if TYPE_CHECKING:
    from src.game_logic.pieces import Piece
    from src.game_logic.mid_level.support.board import Board

from src.game_logic.mid_level.move_finders.movefinder import MoveFinder


class KingMoveFinder(MoveFinder):
    """
    Class to help find moves that a king piece can do.
    """

    def __init__(self, board: 'Board', king: 'Piece' = None):
        """
        Constructor for a KingMoveFinder

        :param king: Piece object for the king to find moves for
        :param board: Board object for this game of chess
        """
        super().__init__(piece=king, board=board)
        assert king is None or king.type == "KING", "King Piece must be type king! Or be None"

    def _possible_moves(self) -> list['Move']:
        return self._create_standard_moves() + self.__castle_moves()

    def _dest_coords_list(self) -> list[tuple[int, int]]:
        """
        Finds the possible destination coords that a king can move in a standard move.

        Are filtered by MoveFinder.filter_dest_coords

        :return:
        """
        curr_coords = self.piece.coords
        return self.filter_dest_coords([
            (curr_coords[0] + 1, curr_coords[1] + 1),
            (curr_coords[0] + 1, curr_coords[1] - 1),
            (curr_coords[0] + 1, curr_coords[1]),
            (curr_coords[0] - 1, curr_coords[1] + 1),
            (curr_coords[0] - 1, curr_coords[1] - 1),
            (curr_coords[0] - 1, curr_coords[1]),
            (curr_coords[0], curr_coords[1] + 1),
            (curr_coords[0], curr_coords[1] - 1),
        ])

    @staticmethod
    def castling_sides():
        """
        The sides that a castling can be done on

        :return: list of strings as described
        """
        return ['king-side', 'queen-side']

    def __castle_moves(self) -> list['Castle']:
        """
        Finds the castling moves that this King can do

        Are not checked to be illegal before returning

        :return: list of Castle Moves that a king can do, if any exist
        """
        moves = []
        if not self.piece.has_moved:
            for side in self.castling_sides():
                if self.__can_castle(side):
                    moves.append(self._move_init("Castle")(self.board, self.piece, self.__castle_get_rook(side), self.__castle_king_travel_to_coords(side), self.__castle_rook_travel_to_coords(side)))
        return moves

    def __can_castle(self, side: str) -> bool:
        """
        Finds out if castling can occur for a given side

        :param side: side of a castling
        :return: bool as described
        """
        return self.__castle_traveling_positions_are_empty(side) and self.__king_can_castle(side) and self.__rook_can_castle(
            side)

    def __king_can_castle(self, side: str) -> bool:
        """
        Finds out if the king involved in this castle can castle

        :param side: str for the side of castling
        :return: bool as described
        """
        # King must not have moved and cannot have moved into check
        return not self.piece.has_moved and not self._castle_causes_check(side) and not self.piece.is_in_check(self.board)

    def _castle_causes_check(self, side : str) -> bool:
        """
        Finds out if the king involved in this castling moves into check or travels along a square that is controlled by
        another piece during this castling

        :param side: str for the side of castling
        :return: bool as described
        """
        king_move_coords = self.__castle_king_move_coords(side)
        return len(self.piece.filter_standard_moves(king_move_coords, self.board)) == len(king_move_coords)

    def __castle_king_move_coords(self, side: str) -> list[tuple[int, int]]:
        """
        Finds the coordinates that the king will have to move through and onto in order to complete this castling.

        This is necessary, since a king cannot move through a square that is controlled by another piece

        :param side: str for the side of castling
        :return: list of tuples as described
        """
        return [self.__castle_king_travel_to_coords(side), self.__castle_king_travel_thru_coords(side)]

    def __castle_king_travel_thru_coords(self, side: str) -> tuple[int, int]:
        """
        Coordinates that a king will need to travel through in order to complete castling

        :param side: str for the side of castling
        :return: coordinate tuple as described
        """
        return self.piece.coords[0], self.piece.coords[1] + self.__castle_col_travel_sign(side) * 1

    def __castle_king_travel_to_coords(self, side: str) -> tuple[int, int]:
        """
        Coordinates that a king will travel to complete this castling

        :param side: str for the side of castling
        :return: coordinate tuple as described
        """
        return self.piece.coords[0], self.piece.coords[1] + self.__castle_col_travel_sign(side) * 2

    def __castle_col_travel_sign(self, side):
        """
        The sign for the change in column entries for a king under going castling

        :param side: str for the side of castling
        :return: int for sign as described
        """
        if side == "queen-side":
            return -1
        return +1

    def __castle_traveling_positions_are_empty(self, side : str) -> bool:
        """
        Finds out if the positions that the rook and king will have to travel to and through are empty

        :param side: str for the side of castling
        :return: bool as described
        """
        for coords in self.__castle_traveling_coords(side):
            if not self.board.get_position(coords).is_vacant:
                return False
        return True

    def __castle_traveling_coords(self, side : str) -> list[tuple[int, int]]:
        """
        Finds all the coordinates that the pieces involved in this castling will have to travel to and onto to complete
        the castling

        :param side: str for the side of castling
        :return:
        """
        coords = self.__castle_king_move_coords()
        if side == "queen-side":
            coords.append((self.piece.coords[0], self.piece.coords[1] - 3))
        return coords

    def __rook_can_castle(self, side: str) -> bool:
        """
        Finds out the piece occupying the rook position for a castling can castle

        :param side: str for the side of castling
        :return bool as described
        """
        piece = self.__castle_get_rook(side)
        if piece is None:
            return False
        return piece.type == "ROOK" and not piece.has_moved

    def __castle_rook_travel_to_coords(self, side : str) -> tuple[int, int]:
        """
        Finds the coordinates that a rook will have to travel to when castling.

        These are the same coordinates that a king travels through when completing castling

        :param side: str for the side of castling
        :return: coordinate tuple as described
        """
        return self.__castle_king_travel_thru_coords(side)

    def __castle_get_rook(self, side: str) -> 'Piece' | None:
        """
        Gets the piece that occupies the rook position for a given castling side

        :param side: str for side of castling
        :return: Piece object or None, if there is no piece occupying the rook's position
        """
        rook_coords = self.__castle_get_rook_coords(side)
        assert self.board.coords_are_valid(rook_coords)
        return self.board.get_position(rook_coords).piece

    def __castle_get_rook_coords(self, side: str) -> tuple[int, int]:
        """
        Finds the coordinates where a rook should be for a castling on a given side

        :param side: str for the side of castling
        :return: coordinate tuple as described
        """
        if side == 'queen-side':
            return self.piece.coords[0], self.piece.coords[1] - 4
        return self.piece.coords[0], self.piece.coords[1] + 3
