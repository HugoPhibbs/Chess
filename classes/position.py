from classes.pieces.piece import Piece


class Position:
    """
    Represents a Position on a chessboard
    """

    def __init__(self, coords, piece: Piece = None):
        """
        Constructor for a Position object

        :param coords: tuple for the coordinates of this position on a chess board. Expressed as a number pair, each
        number from 0-7, useful for indexing the board matrix
        :param piece Piece object that this position contains, leave empty if no piece present
        """
        self.coords = coords
        self.piece = piece

    def __repr__(self) -> str:
        """
        Returns a string representation of this position

        :return: string as described
        """
        return self.col_str() + self.row_str()

    @staticmethod
    def coords_is_valid(val):
        """
        Finds if an inputted value is valid to be integer coordinate pair for this position

        Must be a tuple of length 2, contain only integers, and both integers must be between 0 and 7 (inclusive)
        :param val:
        :return: bool if the inputted value is a valid coordinate pair or not
        """
        if not isinstance(val, tuple) or len(val) != 2:
            return False
        if not isinstance(val[0], int) or not isinstance(val[1], int):
            return False
        return Position.coords_in_board(val)

    @staticmethod
    def coords_in_board(coords) -> bool:
        """
        Finds out if a integer coordinate pair are on a chess board or not

        :param coords: tuple of length 2 with integer values to be checked
        :return: bool if the inputted coords are in the board or not
        """
        return 0 <= coords[0] <= 7 and 0 <= coords[1] <= 8

    def col_str(self) -> str:
        """
        Returns a string representation of the col of this position, as in an actual game of chess

        For example the first column is mapped to 'A', second to 'B' and so forth

        :return: str character as described
        """
        return chr(self.col + 65)

    def row_str(self) -> str:
        """
        Returns a string representation of this row of this position, as in an actual game of chess

        For example, the first row 0 is mapped to 1, 1 to 2 and so forth

        :return: str character as described
        """
        return str(self.row + 1)

    @property
    def piece(self) -> Piece:
        return self.__piece

    @piece.setter
    def piece(self, val) -> None:
        assert isinstance(val, val)
        self.__piece = val

    @property
    def coords(self):
        return self.__coords

    @coords.setter
    def coords(self, val):
        if Position.coords_is_valid(val):
            self.__coords = val
        else:
            raise Exception("Inputted value for new coords for this position are not valid!")

    @property
    def row(self) -> int:
        return self.coords[0]

    @property
    def col(self) -> int:
        return self.coords[1]

    @property
    def is_vacant(self) -> bool:
        """
        Finds if this position is vacant or not, ie if it contains a piece or not

        :return: bool as described
        """
        return self.piece is not None

    def is_hostile(self, colour : str):
        """
        Finds out if this position is occupied by a piece that has a colour that is opposite to the inputted piece

        By convention, an vacant position is not considered hostile, nor is it considered friendly

        :param colour: str for the colour of a Piece object to be checked if this Position contains an hostile piece to it
        :return: bool if this position is occupied by a enemy piece as described
        """
        if self.is_vacant:
            return False
        return self.piece.colour != colour

    def is_friendly(self, colour):
        """
        Finds out if this position is occupied by a piece that is considered friendly to another piece

        By convention, if this position is vacant, it is not considered friendly, nor hostile

        :param colour: str for the colour of a piece that will be considered to be friendly to the colour of the piece
        on this board, if one exists
        :return: bool true if there is a piece on this position that has the same colour as inputted colour, otherwise false,
        see note above
        """
        if self.is_vacant:
            return False
        return self.piece.colour == colour

    def has_piece_type(self, piece_type: str) -> bool:
        """
        Finds out if this Position has a piece of a given type.

        False if this position contains no Piece, or not the right type

        :param piece_type: str for the type of piece as described
        :return: bool as described
        """
        if self.is_vacant:
            return False
        return self.piece.type == piece_type

    def replace_piece(self, new_piece:Piece = None) -> Piece:
        """
        Replaces the piece that is on this board with a new piece

        :param new_piece Piece object that will be placed on this position, default None
        :return: Piece that has been replaced, None if there was no piece already on this position
        """
        assert new_piece is None or isinstance(new_piece, Piece)
        piece = self.piece
        self.piece = new_piece
        return piece
