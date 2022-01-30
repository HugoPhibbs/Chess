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

    def valid_moves_limited(self, piece : LimitedPiece) -> list:
        """
        Return a list of the valid moves that can be done for a limited range piece

        :param piece: LimitedRange piece to be found the valid moves for
        :return: list as described
        """
        possible_moves = piece.moves()
        valid_moves = []
        for move in possible_moves:
            if self.move_is_valid(move, piece):
                valid_moves.append(move)
        return valid_moves

    def valid_moves_ranged(self, piece : RangedPiece):
        pass

    def knight_moves(self, pos):
        row = pos[0]
        col = pos[1]
        possible_moves = [(row - 2, col + 1),
                          (row - 1, col + 2),
                          (row - 2, col - 1),
                          (row - 1, col - 2),
                          (row + 1, col - 2),
                          (row + 2, col - 1),
                          (row + 2, col + 1),
                          (row + 1, col + 2)]

        return self.valid_moves(possible_moves)

    def valid_moves(self, possible_moves, piece):
        valid_moves = []
        for move in possible_moves:
            if self.move_is_valid(move, piece):
                valid_moves.append(move)

    def move_is_valid(self, move: tuple, piece: Piece):
        ## Need to check if piece blocks check
        if Board.__is_outside_board(move):
            return False
        if self.pos_empty(move):
            return True
        if not self.pos_friendly(move, piece.colour):
            return True

    def pos_friendly(self, pos, colour):
        return self.board_mat[pos[0]][pos[1]].colour == colour

    def pos_empty(self, pos):
        return self.board_mat[pos[0]][pos[1]] == None

    def __dfs_moves(self, pos: tuple, piece: Piece, direction: str, lim: int = None):
        """
        Completes a dfs for the specified direction for a given piece at a particular position.

        Returns all moves that are valid in this direction,

        For example, find the moves that a bishop at B4 can move in the north-east direction

        :param pos: tuple describing the current position of a piece
        :param piece: Piece that will be found valid moves for
        :param direction: str for the direction that is wished to travel
        :param lim: the max number of places that a piece can move, useful for when finding moves for a kind, default 8
        :return: list of tuples containing the possible moves that can be done for a particular direction
        """
        if lim is None:
            lim = 8
        adjust_pos = Board.__determine_adjust_move_func(direction)
        moves = []
        move = adjust_pos(pos)
        i = 0
        while self.move_is_valid(move, piece) and i < lim:
            moves.append(move)
            move = adjust_pos(move)
            i += 1
        return move

    @staticmethod
    def __determine_adjust_move_func(direction: str) -> callable:
        """
        Determines the function to adjust position that should be used when doing a dfs in a particular direction

        :param direction: str for the direction as described
        :return: callable function that can be used to increment the position of a possible move by a piece
        """
        if direction == "N":
            adjust_pos = Board.__adjust_move_func(1, 0)
        elif direction == "S":
            adjust_pos = Board.__adjust_move_func(-1, 0)
        elif direction == "E":
            adjust_pos = Board.__adjust_move_func(0, 1)
        elif direction == "W":
            adjust_pos = Board.__adjust_move_func(0, -1)
        elif direction == "NE":
            adjust_pos = Board.__adjust_move_func(1, 1)
        elif direction == "SE":
            adjust_pos = Board.__adjust_move_func(-1, 1)
        elif direction == "SW":
            adjust_pos = Board.__adjust_move_func(-1, -1)
        elif direction == "NW":
            adjust_pos = Board.__adjust_move_func(-1, 1)
        else:
            raise Exception('Direction is not valid, must be in ["N", "S", "W", "E", "NE", "SE", "SW", "NW"]')
        return adjust_pos

    @staticmethod
    def __adjust_move_func(row_incr: int, col_incr: int) -> callable:
        """
        Provides an anonymous function that is used to increment a move to the next possible one during a dfs to find
        possible moves

        A move is simply a tuple, (row, col) specifying a possible position that a piece could move

        row_incr and col_incr must be one of -1, 1 or 0

        :param row_incr: increment for how the row of a position should be updated
        :param col_incr: increment for how the col of a position should be updated
        :return: lambda function as described
        """
        acceptable_directions = [1, -1, 0]
        assert row_incr in acceptable_directions and col_incr in acceptable_directions
        return lambda pos: (pos[0] + row_incr, pos[1] + col_incr)

    @staticmethod
    def __is_outside_board(pos: tuple) -> bool:
        """
        Determines if a position is outside the board

        :param pos: tuple for the position of a piece on the board
        :return: bool as described
        """
        return 0 <= pos[0] <= 7 and 0 <= pos[1] <= 7

    def __pawn_can_move(self, pos):
        pass



    def __find_moves(self, directions: list, pos: tuple, piece: any, lim: int = None) -> list:
        """
        Finds the moves that can be done for a list of directions for a particular piece at a particular position

        :param directions: list of strings for the directions that this piece can travel
        :param pos: tuple describing the position of the inputted piece
        :param piece: Piece object to be found moves for
        :param lim int for the number of places that a piece can move, useful for kings
        :return: list of tuples for the valid moves that a piece can do
        """
        moves = []
        for direction in directions:
        for direction in directions:
            moves.append(self.__dfs_moves(pos, piece, direction, lim))
        return moves

    def __king_moves(self, pos: tuple, piece: Piece) -> list:
        """
        Returns a list of the possible moves that a king can do for a particular direction

        :param pos: tuple for the position of the king
        :param piece: Piece object for the king
        :return: list as described
        """
        return self.__find_moves(Board.__diag_directions() + Board.__straight_directions(), pos, piece, lim=1)

    def pieces_see_each_other(self, piece_1, piece_2):
        """
        If two pieces are at a straight or diagonal direction to each other, it finds if two pieces can see each other
        :param piece_1:
        :param piece_2:
        :return:
        """
        direction_between = self.__king_to_piece_direction(piece_2, piece_1)
        if direction_between is None:
            return False
        else:
            curr_row = piece_2.pos[0] + direction_between[0]
            curr_col = piece_2.pos[1] + direction_between[1]
            curr_piece =  self.get_piece_at_pos(row=curr_row,col=curr_col)
            while curr_piece is None and not self.__is_outside_board((curr_row, curr_col)):
                curr_row += direction_between[0]
                curr_col += direction_between[1]
                curr_piece = self.get_piece_at_pos(row=curr_row, col=curr_col)
            return curr_piece == piece_1

    def get_piece_at_pos(self, pos: tuple = None, row: int = None, col:int = None):
        """
        Finds the piece at a given position on the chess board. None if there is no piece on this position

        Pos can only be specified if both row and col are None, and vice versa. Otherwise an exception is thrown
        This gives flexibility.

        :param pos: tuple for the position on a board, default None
        :param row: int for the row of a position on the board, default None
        :param col: int for the col of a position on the board, default None.
        :return:
        """
        if pos is not None and (row is None and col is None):
            assert isinstance(pos, tuple) and isinstance(pos[0], int) and isinstance(pos[1], int)
            return self.board_mat[pos[0], pos[1]]
        elif pos is None and (row is not None and col is not None):
            assert isinstance(row, int) and isinstance(col, int)
            return self.board_mat[row][col]
        raise Exception("If pos is specified, row and col must be None. If pos is None, then row and col must be "
                        "specified!")

    def __king_to_piece_direction(self, king : King, piece : Piece) -> tuple:
        """
        Finds the direction between a king and a piece.

        We assume that if two pieces can't possibly have a line of sight with each other, (not strictly in range) then they have a
        direction between them. Otherwise, if they don't have a line of sight between, then there is no direction between them

        :param king: King object
        :param piece: Piece object
        :return: tuple for the direction between the king and the piece, None if there is no line between the king and piece,
        this is expressed as (row direction, col direction)
        """
        direction_dict = {
            '('
        }
        row_diff = king.pos[0] - piece.pos[0]
        col_diff = king.pos[1] - piece.pos[1]
        if not Board.pieces_share_direction(row_diff, col_diff):
            return None
        direction = (row_diff // abs(row_diff), col_diff // abs(col_diff))
        return direction

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






