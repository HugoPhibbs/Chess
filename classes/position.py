class Position:
    """
    Represents a Position on a chessboard
    """

    def __init__(self, coords, piece=None):
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
    def coords(self):
        return self.__coords

    @coords.setter
    def coords(self, val):
        if Position.coords_is_valid(val):
            self.__coords = val
        else:
            raise Exception("Inputted value for new coords for this position are not valid!")

    @property
    def row(self):
        return self.coords[0]

    def col(self):
        return self.coords[1]

    @property
    def is_vacant(self) -> bool:
        """
        Finds if this position is vacant or not, ie if it contains a piece or not

        :return: bool as described
        """
        return self.piece is not None

    def is_hostile(self, colour):
        """
        Finds out if this position is occupied by a piece that has a colour that is opposite to the inputted piece

        :param colour: colour of a Piece object to be checked if this Position contains an hostile piece to it
        :return: bool if this position is occupied by a enemy piece as described
        """
        if self.piece is None:
            return False
        return self.piece.colour != colour
