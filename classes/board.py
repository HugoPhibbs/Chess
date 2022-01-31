from classes.move import Move
from classes.pieces.king import King
from classes.pieces.limitedpiece import LimitedPiece
from classes.pieces.piece import Piece
from classes.pieces.rangedpiece import RangedPiece
from classes.position import Position


class Board:
    """
    Class to represent a Board object in a game of chess
    """

    def __init__(self, board_mat_: list):
        """
        Initializer for a  Board Object

        :param board_mat_: matrix containing Position objects representing the actual board in a chess game
        """
        self.board_mat = board_mat_

    def valid_moves(self, coords):
        """
        Finds the valid moves that can be done by a piece at a given position

        :param coords: tuple of coordinates on a chess board, aka position
        :return: list of valid moves that can be done for this position, None if there is no Piece object in this position
        """
        piece: any = self.board_mat[coords[0]][coords[1]].piece
        if piece is None:
            return None
        elif isinstance(piece, RangedPiece):
            return self.valid_moves_ranged(piece)
        elif isinstance(piece, LimitedPiece):
            return self.valid_moves_limited(piece)

    def coords_friendly(self, coords, colour) -> bool:
        """
        Finds if a pair of coordinates on a chess board are occupied by a friendly piece

        :param coords: tuple of length two containing integers for coordinates on a chessboard
        :param colour: colour of a piece that will be considered friendly to another piece
        :return: bool if a pair of coords is friendly as described
        """
        return self.board_mat[coords[0]][coords[1]].colour == colour
    @staticmethod
    def __determine_adjust_coord_func(direction: str) -> callable:
        """
        Determines the function to adjust position that should be used when doing a dfs in a particular direction

        :param direction: str for the direction as described
        :return: callable function that can be used to increment the position of a possible move by a piece
        """
        if direction == "N":
            adjust_pos = RangedPiece.__adjust_move_func(1, 0)
        elif direction == "S":
            adjust_pos = RangedPiece.__adjust_move_func(-1, 0)
        elif direction == "E":
            adjust_pos = RangedPiece.__adjust_move_func(0, 1)
        elif direction == "W":
            adjust_pos = RangedPiece.__adjust_move_func(0, -1)
        elif direction == "NE":
            adjust_pos = RangedPiece.__adjust_move_func(1, 1)
        elif direction == "SE":
            adjust_pos = RangedPiece.__adjust_move_func(-1, 1)
        elif direction == "SW":
            adjust_pos = RangedPiece.__adjust_move_func(-1, -1)
        elif direction == "NW":
            adjust_pos = RangedPiece.__adjust_move_func(-1, 1)
        else:
            raise Exception('Direction is not valid, must be in ["N", "S", "W", "E", "NE", "SE", "SW", "NW"]')
        return adjust_pos

    @staticmethod
    def pieces_share_direction(row_diff : int, col_diff : int) -> bool:
        """
        Finds if two pieces are diagonal or straight to each other, or not

        :param row_diff: difference in row coordinates between two pieces
        :param col_diff: difference in column coordinates between two pieces
        :return: boolean true if they are on a straight or diagonal direction to each other, otherwise false
        """
        return (row_diff + col_diff) % row_diff == 0 or (row_diff + col_diff) % col_diff == 0

    def get_pos_obj_at_coords(self, coords) -> Position:
        """
        Returns the Position object that is located at a coordinate pair for this Board

        :param coords: tuple for the coordinates of a position on this board, must be valid as per Position.coords_is_valid(val)
        :return: Position object as described
        """
        assert Position.coords_is_valid(coords)
        return self.board_mat[coords[0]][coords[1]]

    def coords_vacant(self, coords) -> bool:
        """
        Finds if the Position object located at a pair of coordinates is vacant or not

        :param coords: tuple pair of coordinates if they are vacant or not
        :return: bool as described
        """
        return self.get_pos_obj_at_coords(coords).is_vacant












