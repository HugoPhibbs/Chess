from __future__ import annotations
from typing import TYPE_CHECKING
if TYPE_CHECKING:
    from src.game_logic.mid_level.moves.standardmove import StandardMove
    from src.game_logic.mid_level.support.board import Board
    from src.game_logic.pieces import Piece
    from src.game_logic.pieces import Pawn

from src.game_logic.mid_level.move_finders.movefinder import MoveFinder


class PawnMoveFinder(MoveFinder):
    """
    Finds the moves that can be completed by a Pawn
    """

    def __init__(self, board: 'Board', pawn: 'Piece' | 'Pawn' = None):
        """
        Constructor for a pawn move finder

        :param pawn: Pawn piece to find the moves for
        :param board: Board object for this game of chess
        """
        super().__init__(board, pawn)
        assert pawn is None or pawn.type == "PAWN", "Only pawns or None objects should be used in PawnMoveFinder!"

    def _possible_moves(self) -> list['Move']:
        return self._create_standard_moves(self.__forward_coords(), can_capture=False) + self._create_standard_moves(self.__attack_coords()) + self.__en_passant_moves()

    def __forward_coords(self) -> list[tuple[int, int]]:
        """
        Finds the destination coords of possible moves forward that this pawn can do.
        :return: list of coords
        """
        return self.filter_dest_coords([self.__single_forward_coords(), self.__double_forward_coords()],
                                       vacant_only=True)

    def __attack_coords(self) -> list[tuple[int, int]]:
        """
        Finds the destination coords of possible attack coords that a pawn can do
        :return: list of coords
        """
        return self.filter_dest_coords([self.__right_attack_coords(), self.__left_attack_coords()], attack_only=True)

    def __can_double_move(self, board: 'Board') -> bool:
        """
        Finds if this Pawn can do a double forward move on a chessboard

        Needs a clear line of sight to dest coords

        :param board: Board object for a game of chess
        :return: bool as described
        """
        return not self.piece.has_moved and board.get_position(self.__single_forward_coords()).is_vacant

    def __single_forward_coords(self) -> tuple:
        """
        Finds the coordinates directly in-front of a pawn, as if it was doing a forward advancement on the chessboard,

        Depending on what colour a pawn is, the 'forward' bearing varie

        :return: tuple of length 2 containing integers with the coordinates in front of a pawn, not necessarily
        inside a chessboard
        """
        return self.piece.position.row + self.__forward_row_coef(), self.piece.position.col

    def __double_forward_coords(self) -> tuple:
        """
        Returns the coordinates that are 2 steps forward infront of this pawn

        Considers the colour of this pawn in making calculations

        :return: tuple of length 2 containing integers of the coordinates 2 steps infront of this pawn on the chess board
        """
        one_forward = self.__single_forward_coords()
        return one_forward[0] + self.__forward_row_coef(), one_forward[1]

    def __forward_row_coef(self) -> int:
        """
        Finds the coefficient that should be multiplied to any positive increment of the row of a Pawn, corresponding to
        forward movement on the chess board

        For example, Black pawns use -1 and White use +1

        :return: integer for the coefficient as described
        """
        if self.piece.colour == "BLACK":
            return -1
        return +1

    def __left_attack_coords(self) -> tuple:
        """
        Finds the coordinates for an attack from this pawn to the right

        :return: tuple of coordinates as described
        """
        forward_coords = self.__single_forward_coords()
        return forward_coords[0], forward_coords[1] - 1

    def __right_attack_coords(self) -> tuple:
        """
        Finds the coordinates for an attack from this pawn to the right

        :return: tuple of coordinates as described
        """
        forward_coords = self.__single_forward_coords()
        return forward_coords[0], forward_coords[1] + 1

    def __en_passant_moves(self) -> list['StandardMove']:
        """
        Finds the potential en passant moves that this Pawn can do.

        Since an en passant is a special case of a capture, this is done seperately here

        :return: list of standard move objects
        """
        moves = []

        def add_en_passant_move(dest_coords, capture_coords):
            if self._should_add_dest_coords(dest_coords, vacant_only=True):
                moves.append(self._move_init("STANDARD")(self.board, self.piece.coords, dest_coords, capture_coords))

        add_en_passant_move(self.__left_attack_coords(), self.__en_passant_capture_coords_left())
        add_en_passant_move(self.__right_attack_coords(), self.__en_passant_capture_coords_right())
        return moves

    def __en_passant_coords(self) -> list[tuple[int, int]]:
        """
        Returns destination coordinates of en passant moves that can be done

        :return: list of coords as described
        """
        coords_list = [self.__en_passant_capture_coords_left(), self.__en_passant_capture_coords_right()]
        return self.filter_dest_coords(
            [coords for coords in coords_list if self.__can_en_passant(coords)], vacant_only=True)

    def __en_passant_capture_coords_left(self) -> tuple:
        """
        Finds capture coords of an en-passant captures on the left, given that they can be done

        :return: tuple
        """
        return self.piece.coords[0], self.piece.coords[1] - 1

    def __en_passant_capture_coords_right(self) -> tuple:
        """
        Finds capture coords of an en-passant captures, given that they can be done

        :return: tuple
        """
        return self.piece.coords[0], self.piece.coords[1] + 1

    def __can_en_passant(self, capture_coords):
        """
        Finds if an en passant move can be done for the given capture coordinates of the enpassant

        Ignores possibility of causing a friendly check
        :return: bool as described
        """
        capture = self.board.get_position(capture_coords).piece
        return capture is not None and capture.type == 'PAWN' and capture.just_double_moved
