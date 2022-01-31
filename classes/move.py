from classes.board import Board
from classes.pieces.piece import Piece
from classes.position import Position
from __future__ import annotations


class Move:
    """
    Class to assist with moves in a game of chess.

    Represents a possible move that could be completed in a game of chess
    """

    __executed: bool = False

    def __init__(self, piece, source: Position, dest: Position, capture: Piece = None):
        """
        Initializer for a Move object

        Assumes that the inputted piece object can actually move to the destination. This should be checked before
        the creation of this object.

        :param piece: Piece object that is being moved on the chess board by this move
        :param source: Position object where the piece object starts this move
        :param dest: Position object where the piece object finishes this move
        :param capture: Any Piece object that is captured by inputted piece by this move
        """
        self.piece = piece
        self.source = source
        self.dest = dest
        self.capture = capture

    def __repr__(self):
        """
        Returns a string representation of this move
        :return:
        """
        pass

    @property
    def capture(self) -> Piece:
        return self.__capture

    @capture.setter
    def capture(self, val) -> None:
        assert isinstance(val, Piece)
        self.__capture = val

    @staticmethod
    def determine_adjust_coords_func(direction: str) -> callable:
        """
        Determines the function to adjust position that should be used when doing a dfs in a particular direction

        :param direction: str for the direction as described
        :return: callable function that can be used to increment the position of a possible move by a piece
        """
        if direction == "N":
            adjust_pos = RangedPiece.__adjust_coords_func(1, 0)
        elif direction == "S":
            adjust_pos = RangedPiece.__adjust_coords_func(-1, 0)
        elif direction == "E":
            adjust_pos = RangedPiece.__adjust_coords_func(0, 1)
        elif direction == "W":
            adjust_pos = RangedPiece.__adjust_coords_func(0, -1)
        elif direction == "NE":
            adjust_pos = RangedPiece.__adjust_coords_func(1, 1)
        elif direction == "SE":
            adjust_pos = RangedPiece.__adjust_coords_func(-1, 1)
        elif direction == "SW":
            adjust_pos = RangedPiece.__adjust_coords_func(-1, -1)
        elif direction == "NW":
            adjust_pos = RangedPiece.__adjust_coords_func(-1, 1)
        else:
            raise Exception('Direction is not valid, must be in ["N", "S", "W", "E", "NE", "SE", "SW", "NW"]')
        return adjust_pos

    @property
    def executed(self) -> bool:
        return self.__executed

    @executed.setter
    def executed(self, val) -> None:
        assert isinstance(val, bool)
        self.__executed = val

    @property
    def piece(self) -> Piece:
        return self.__piece

    @piece.setter
    def piece(self, val) -> None:
        assert val is not None and isinstance(val, Piece)
        self.__piece = val

    def execute(self) -> Piece:
        """
        Executes this move.

        :return: Any Pieces that were captured by this Move
        """
        assert self.executed is False, "Move has already been executed!"
        self.source.replace_piece()
        self.dest.replace_piece(self.piece)
        self.executed = True
        return self.capture

    def reverse(self) -> Piece:
        """
        Reverses the execution of this move

        :return: Any Piece object that was previously captured by this Move
        """
        assert self.executed is True, "Move hasn't been executed yet!"
        self.dest.replace_piece(self.capture)
        self.source.replace_piece(self.piece)
        self.executed = False
        return self.capture

    def __is_legal(self) -> bool:
        """
        Finds out if this move is legal or not.

        :return: bool as described
        """
        if not (self.dest.is_vacant or self.dest.is_hostile(self.piece.colour)):
            return False
        self.execute()
        if self.piece.friendly_king_in_check():
            self.reverse()
            return False
        self.reverse()
        return True

    @staticmethod
    def filter_move(dest_coord: tuple, piece: Piece, board: Board) -> Move | None:
        """
        Finds out if a move with inputted destination coords, for a particular piece can be created.

        If it can, returns a new Move initialized with necessary values, otherwise returns None

        Assumes that the inputted piece has the capability to move to the destination coordinates in the first place.
        For example, don't input destination coords on the other side of the board for a knight that you know cannot
        get there in the first place!

        :param dest_coord: tuple integer pair of prosepctive oordinates on a chessboard to be checked as a valid destination for the piece
        :param piece: Piece object that could be moved to the destination coordinates
        :param board : Board object for this game of chess
        :return: A Move object if it can be created, otherwise None
        """
        if Position.coords_in_board(dest_coord):
            dest_position = board.get_pos_obj_at_coords(dest_coord)
            move = Move(piece, piece.position, dest_position, dest_position.piece)
            if move.__is_legal():
                return move
        return None

    @staticmethod
    def filter_moves(dest_coords: list, piece: Piece, board: Board) -> list:
        """
        Filters a list of destination coordinates for a piece on a chessboard. Returns a list of Move objects that can
        are legally possible for the piece to move to the destination coordinates.

        Main logic is in Move.filter_move(dest_coord: tuple, piece: Piece, board: Board)

        :param dest_coords: list of tuple integer pair of prospective coordinate destinations on a chessboard for an inputted piece
        :param piece: Piece object that will prospectively move to coords in dest_coords
        :param board: Board object for this chess game
        :return: list of moves that can be completed given inputs
        """
        moves = []
        for dest_coord in dest_coords:
            move = Move.filter_move(dest_coord, piece, board)
            if move is not None:
                moves.append(move)
        return moves
