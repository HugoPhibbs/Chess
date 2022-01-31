from classes.move import Move
from classes.pieces.limitedpiece import LimitedPiece
from classes.position import Position


class Knight(LimitedPiece):
    """
    Represents a Knight piece on a chessboard
    """

    def __init__(self, *args):
        """
        Constructor for a knight piece, all constructor arguments are passed to Piece

        :param args: parameters for the parent constructor of a Piece object
        """
        super().__init__(*args)

    @property
    def type(self):
        """
        Returns the type of this Piece, overrides type() from Piece

        :return: string describing the type of piece that this knight piece is
        """
        return "KNIGHT"

    def __repr__(self) -> str:
        """
        Returns a string representation of itself

        :return: str as described
        """
        return "KT"

    def moves(self, board) -> list:
        """
        Finds the possible moves that can be done by this Knight

        Checks that any moves are inside the chessboard and nothing else, proper checking to see if move puts king in check
        etc should be done by Board class later

        :param board: Board object for the current chess game
        :return: list containing tuples of coords for possible moves that this knight can do
        """
        return Move.filter_moves(Knight.attack_coords(self.position.coords), self, board)

    @staticmethod
    def attack_coords(coords):
        """
        Returns a list of the possible coordinates that a knight could attack from inputted coordinates. Can also be
        used to find the possible coordinates of attacking knights from given coordinates

        Static so it can be used by king to check if it is being checked by a knight

        :param coords: tuple integer pair of coordinates on a chess board
        :return: list of coordinates as described
        """
        row = coords[0]
        col = coords[1]
        possible_move_coords = [(row - 2, col + 1),
                          (row - 1, col + 2),
                          (row - 2, col - 1),
                          (row - 1, col - 2),
                          (row + 1, col - 2),
                          (row + 2, col - 1),
                          (row + 2, col + 1),
                          (row + 1, col + 2)]
        coords_inside_board = []
        for coords in possible_move_coords:
            if Position.coords_in_board(coords):
                coords_inside_board.append(coords)
        return coords_inside_board



