from classes.board import Board
from classes.move import Move
from classes.pieces.knight import Knight
from classes.pieces.piece import Piece
from classes.pieces.rangedpiece import RangedPiece
from classes.position import Position


class King(Piece, RangedPiece):

    def move_directions(self) -> list:
        pass

    def __init__(self, *args):
        """
        Constructor for a King piece, all constructor arguments are passed to Piece

        :param args: parameters for the parent constructor of a Piece object
        """
        super().__init__(*args)

    @property
    def type(self):
        """
        Returns the type of this Piece, overrides type() from Piece

        :return: string describing the type of piece that this King piece is
        """
        return "KING"

    def __repr__(self) -> str:
        """
        Returns a string representation of itself

        :return: str as described
        """
        return "K"

    def is_in_check(self, board) -> bool:
        """
        Finds out if this king Piece is in Check or not

        :param board: Board object being used for a chess game
        :return: bool for if this King is in check or not
        """
        return self.in_knight_check(board) or self.in_check_all_directions(board)

    def in_check_all_directions(self, board):
        """
        Determines if this king is in check considering all the directions that legally exist on a chessboard

        For example, North, East, South-West etc

        :param board: Board object for a game of chess
        :return: bool if a King is in Check or not
        """
        possible_directions = RangedPiece.diag_directions + RangedPiece.straight_directions
        for direction in possible_directions:
            if self.in_check_direction(direction.board):
                return True
        return False

    def in_check_direction(self, direction: str, board: Board) -> bool:
        """
        Finds out if this king is in check for a given direction.

        Does a DFS on coordinates from the position of this king, and finds if any pieces it encounters can attack this King

        :param direction: str for the direction to be checked as described
        :param board: Board object belonging to a game of chess
        :return: bool if this king is in check via the inputted direction
        """
        adjust_coords = Move.determine_adjust_coords_func(direction)
        curr_coords = adjust_coords(self.position.coords)
        while Position.coords_in_board(curr_coords):
            pos = board.get_pos_obj_at_coords(curr_coords)
            if pos.is_hostile(self.colour):
                if pos.piece.can_move_to_coords(self.position.coords):
                    return True
                break  # Blocks any enemy pieces from attacking this king in this direction
            elif pos.is_friendly(self.colour):
                # Friendly piece in this position, blocks any attacks from enemy on this direction
                return False
            curr_coords = adjust_coords(curr_coords)
        return False

    def in_knight_check(self, board) -> bool:
        """
        Determines if this King object is in check by an enemy knight

        :param board: Board object belonging to the chess game being played
        :return: bool if this king is in check by a knight
        """
        knight_coords = Knight.attack_coords(self.position.coords)
        for coord in knight_coords:
            pos_at_coords: Position = board.get_pos_obj_at_coords(coord)
            if pos_at_coords.is_hostile(self.colour) and pos_at_coords.piece.type == "KNIGHT":
                return True
        return False
