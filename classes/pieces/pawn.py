from classes.pieces.limitedpiece import LimitedPiece
from classes.position import Position


class Pawn(LimitedPiece):
    """
    Represents a pawn piece in a game of chess
    """

    def __init__(self, *args):
        """
        Constructor for a Pawn piece, all constructor arguments are passed to Piece

        :param args: parameters for the parent constructor of a Piece object
        """
        super().__init__(*args)

    @property
    def type(self):
        """
        Returns the type of this Piece, overrides type() from Piece

        :return: string describing the type of piece that this Pawn piece is
        """
        return "PAWN"

    def __repr__(self) -> str:
        """
        Returns a string representation of itself

        :return: str as described
        """
        return "P"

    def moves(self, board) -> list:
        """
        Finds any moves that can be done by this Pawn for an inputted board

        NOTE: ignores any valid move requirements as per Board.move_is_valid(move), this is done later

        :param board: Board object for this game of chess
        :return: list of coordinates for any moves that this pawn can do
        """
        return self.forward_moves(board) + self.attack_moves(board)

    def forward_moves(self, board) -> list:
        """
        Finds any possible moves forward that this pawn can do

        Ignores any requirements of valid moves as per Board.move_is_valid(move), this is to be done later

        :param board: Board object for a game of chess
        :return: list of tuples coordinates for any forward moves that can be done
        """
        possible_moves = []
        if self.can_move_forward(board):
            possible_moves.append(self.forward_coords())
        if self.can_double_move(board):
            possible_moves.append(self.double_forward_coords())
        return possible_moves

    def attack_moves(self, board) -> list:
        """
        Finds the coordinates of attacks that can be done by this pawn.

        Uses Pawn.attack_is_valid(attack, board) to check if a attack is valid, please check this for it's limitations

        :param board: Board object representing the board in a current game of chess
        :return: list of coordinate tuples of any attack moves that this pawn can do
        """
        possible_attacks = [self.right_attack_coords(), self.left_attack_coords()]
        for attack in possible_attacks:
            if not Pawn.attack_is_valid(board):
                possible_attacks.remove(attack)
        return possible_attacks

    @staticmethod
    def attack_is_valid(attack, board) -> bool:
        """
        Finds out if an inputted attack is valid for this pawn on an inputted board

        NOTE, doesn't check if an attack moves may put the king into check or any other requirements for valid moves
        as per Board.move_is_valid(move). Only checks if this attack is inside the board, and that the an enemy piece
        occupies the position of the attack.

        :param attack: coordinates of a new position of this pawn given an attack on these coordinates
        :param board: Board object for this game of chess
        :return: bool if the attack is valid or not, as described above
        """
        return Position.coords_in_board(attack) and board.get_pos_obj_at_coords(attack).is_hostile()

    def left_attack_coords(self) -> tuple:
        """
        Finds the coordinates for an attack from this pawn to the right

        :return: tuple of coordinates as described
        """
        forward_coords = self.forward_coords()
        return forward_coords[0], forward_coords[1] - 1

    def right_attack_coords(self) -> tuple:
        """
        Finds the coordinates for an attack from this pawn to the right

        :return: tuple of coordinates as described
        """
        forward_coords = self.forward_coords()
        return forward_coords[0], forward_coords[1] + 1

    def can_double_move(self, board):
        """
        Finds if this Pawn can do a double forward move on a chessboard. As it can do at the start of the game

        Ignores if this move is valid as per Board.move_is_valid(move)

        :return: bool as described
        """
        return not self.has_moved() and board.coords_vacant(self.double_forward_coords()) and self.can_move_forward()

    def has_moved(self):
        """
        Finds if this Pawn has moved or not

        :return: bool if this Pawn has moved or not
        """
        return not ((self.colour == 'WHITE' and self.position.row == 1) or (
                    self.colour == 'BLACK' and self.position.row == 7))

    def double_forward_coords(self) -> tuple:
        """
        Returns the coordinates that are 2 steps forward infront of this pawn

        Considers the colour of this pawn in making calculations

        :return: tuple of length 2 containing integers of the coordinates 2 steps infront of this pawn on the chess board
        """
        one_forward = self.forward_coords()
        return one_forward[0] + self.forward_row_coef(), one_forward[1]

    def forward_coords(self) -> tuple:
        """
        Finds the coordinates directly in-front of this pawn, as if it was doing a forward advancement on the chessboard,

        Depending on what colour this pawn is, the 'forward' direction varies

        :return: tuple of length 2 containing integers with the coordinates in front of this pawn, not necessarily
        inside a chessboard
        """
        return self.position.row + self.forward_row_coef(), self.position.col

    def forward_row_coef(self) -> int:
        """
        Finds the coefficient that should be multiplied to any positive increment of the row of this Pawn, corresponding to
        forward movement on the chess board

        For example, Black pawns use -1 and White use +1

        :return: integer for the coefficient as described
        """
        if self.colour == "BLACK":
            return -1
        return +1

    def can_move_forward(self, board):
        """
        Finds out if this pawn can move directly forward or not (no change in column, ie no lateral movement)

        NOTE: simply checks if the position in-front of this pawn exists and that it is vacant, Does not check if
        any move forward is valid as per Board.move_is_valid(move)

        :param board: Board object to be checked if this pawn can move forward on or not
        :return: bool if this pawn can move forward, please see note above
        """
        forward_coords = self.forward_coords()
        return Position.coords_in_board(forward_coords) and board.coords_vacant(forward_coords)
