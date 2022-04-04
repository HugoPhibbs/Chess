from __future__ import annotations
from abc import ABC, abstractmethod
from typing import TYPE_CHECKING

from src.game_logic.mid_level.moves.castle import Castle
from src.game_logic.mid_level.moves.standardmove import StandardMove

if TYPE_CHECKING:
    from src.game_logic.mid_level.support.board import Board
    from src.game_logic.mid_level.moves.move import Move
    from src.game_logic.pieces import Piece


class MoveFinder(ABC):
    """
    Class to support finding the moves that a piece can do at a given point in a game of chess
    """

    def __init__(self, board: 'Board', piece: 'Piece' = None):
        """
        Constructor for a MoveFinder

        :param piece: Piece to be found moves for
        :param board: Board object for a game of chess
        """
        self.piece = piece
        self.board = board

    def moves(self, ignore_friendly_check: bool = False) -> list:
        """
        Return a list of legal moves that the piece belonging to this MoveFinder can do

        :param ignore_friendly_check: bool for if the executing of any move may cause a friendly check should be filtered out
        this is really to check if a piece controls another square or not. Default False
        :return: list as described
        """
        return self.__filter_illegal_moves(self._possible_moves(), ignore_friendly_check)

    def can_attack_coords(self, coords : tuple[int, int]) -> bool:
        """
        Finds out if the Piece that this MoveFinder finds moves for can attack the given coordinates on a chessboard

        :param coords: coordinates on a chessboard
        :return: bool as described
        """
        all_moves = self.moves(ignore_friendly_check=True)
        for move in all_moves:
            if move.type() == "STANDARD" and move.can_capture and move.dest.coords == coords:
                return True
        return False

    @abstractmethod
    def _possible_moves(self) -> list['Move']:
        """
        Finds the possible moves for the piece belonging to this MoveFinder

        These moves are not checked to be legal yet, i.e. if they cause a friendly check!

        Effectively acts like a wrapper function to _create_standard_moves for pieces that don't do any special moves
        eg a knight or bishop

        :return: list of move objects that can be readily executed
        """
        pass

    @staticmethod
    def __filter_illegal_moves(moves: list, ignore_friendly_check=False):
        """
        Filters a list of moves, so only the legal ones remain

        :param moves: List of moves
        :return: list of filtered moves
        """
        filtered_moves = []
        for move in moves:
            if move.is_legal(ignore_friendly_check):
                filtered_moves.append(move)
        return filtered_moves

    def _create_standard_moves(self, dest_coords_list : list[tuple[int, int]], can_capture: bool = True):
        """
        Creates a list of standard move objects based on the inputted destination coordinates

        Standard moves are not checked to be legal before returning. This is to let all checking of legal moves to be done
        in one place!

        Made dest_coords_list a parameter so this method can be called with differing destination coords and their requirements
        Mainly aimed at pawns, who can only attack on diagonals. So these dest coords should be treated differently!

        Assumes that any capturing of pieces is at the destination coordinates. Special case of this is
        en-passant, so this is handled separately.

        :param dest_coords_list: list of destination coordinates for StandardMove objects to be created from
        :param can_capture: bool for if created StandardMoves can capture another piece. Default is True. Mainly aimed at pawns
        who cannot attack in a forward direction!
        :return: list of standard moves
        """
        moves = []
        for dest_coords in dest_coords_list:
            moves.append(self._move_init("STANDARD")(self.board, self.piece.coords, dest_coords, capture_coords=None))
        return moves

    def filter_dest_coords(self, dest_coords: list[tuple[int, int]], attack_only: bool = False,
                           vacant_only: bool = False) -> list[tuple[int, int]]:
        """
        Filters destination coordinates for intended standard moves that this piece may do

        Optional parameters of vacant only and attack only are added to support en passant capturing.

        :param dest_coords:
        :param attack_only: if only dest coordinates that result in an attack should be accepted
        :param vacant_only: if only dest coordinates that move into empty space should be accepted
        :return:
        """
        filtered_coords = []
        assert not (attack_only and vacant_only), "Destination coordinates can not be filtered for both vacant and " \
                                                  "hostile positions! "
        for coords in dest_coords:
            if self._should_add_dest_coords(coords, attack_only, vacant_only):
                filtered_coords.append(coords)
        return filtered_coords

    def _should_add_dest_coords(self, dest_coords: tuple[int, int], attack_only: bool = False,
                                vacant_only: bool = False) -> bool:
        """
        Finds out if a given destination coords should be a candidate for a possible move that a piece can do

        :param dest_coords:
        :param attack_only:
        :param vacant_only:
        :return:
        """
        if self.board.coords_in_board(dest_coords):
            coords_position = self.board.get_position(dest_coords)
            if attack_only:
                return coords_position.is_hostile(self.piece.colour)
            elif vacant_only:
                return coords_position.is_vacant
            else:
                return coords_position.is_vacant or coords_position.is_hostile(self.piece.colour)
        return False

    @staticmethod
    def _move_init(type: str) -> callable:
        """
        Returns constructor for a given move type.

        This is used to minimise coupling between implementing classes and other parts of the project.

        :param type: str for move type, either "CASTLE" or "STANDARD"
        :return: callable move initializer
        """
        assert type in ["CASTLE", "STANDARD"]
        if type == "STANDARD":
            return StandardMove
        else:
            return Castle
