from src.game_logic.mid_level.move_finders.kingmovefinder import KingMoveFinder
from src.game_logic.mid_level.move_finders.knightmovefinder import KnightMoveFinder
from src.game_logic.mid_level.move_finders.pawnmovefinder import PawnMoveFinder
from src.game_logic.mid_level.move_finders.rangedmovefinder import RangedMoveFinder
from src.game_logic.mid_level.support.position import Position
from src.game_logic.mid_level.support.board import Board
from src.game_logic.mid_level.support.player import Player
from src.game_logic.pieces import *
from src.game_logic.helpers import CoordsHelper, TraverseHelper, BearingHelper


class Setup:
    """
    Sets up a game of chess, organising and creating all necessary objects
    """

    coords_helper: 'CoordsHelper' = CoordsHelper

    def __init__(self, player_names: dict):
        """
        Creates an instance of a setup class

        :param player_names: dict containing the two names for the players of this game of chess, should have keys
        'white_name' and 'black_name'
        """
        self.board = self.__create_board()
        self.players = self.__create_players(player_names, self.__fill_board())

    @staticmethod
    def __create_players(names: dict, pieces: dict) -> dict:
        """
        Creates two Player objects for two players playing in a game of chess

        :param names: dict containing the two names for the players of this game of chess, should have keys
        'white_name' and 'black_name'
        :param pieces: dict for the pieces to be assigned to each player, should have keys for "white_pieces" and "black_pieces"
        :return: dict containing two player objects as described, has keys "white_player", "black_player"
        """
        return {"white_player": Player(names['white_name'], pieces['white_pieces'], "WHITE"),
                "black_player": Player(names['black_name'], pieces['black_pieces'], "BLACK")}

    def __create_board(self) -> Board:
        """
        Creates a board for a game of chess

        :return: Board object
        """
        board_mat = [[None] * 8 for i in range(8)]
        for row in range(8):
            for col in range(8):
                pos = Position((row, col), self.coords_helper)
                board_mat[row][col] = pos
        return Board(board_mat)

    def __fill_board(self) -> dict:
        """
        Fills a board for a game of chess with pieces

        :return: dict containing the pieces that were created, has keys for each colour, "white_pieces" and "black_pieces"
        """
        return {"white_pieces": self.__fill_colour("WHITE"),
                "black_pieces": self.__fill_colour("BLACK")}

    @staticmethod
    def __colour_for_rows(colour: str) -> tuple[int, int]:
        """
        Finds the rows that pieces occupy for a particular colour

        :param colour: str for colour of pieces
        :return: tuple[int, int] for the rows occupied by coloured pieces
        """
        if colour == 'WHITE':
            return 0, 1
        elif colour == 'BLACK':
            return 7, 6
        raise ValueError("Colour must be either 'WHITE' or 'BLACK'")

    def __fill_colour(self, colour: str) -> list:
        """
        Fills a chess board with pieces for a particular colour, returns a list of the pieces created

        :param colour: str for colour of pieces
        :param rows: rows on a chess board that pieces of the inputted colour occupy at the start of the game
        :return: None
        """
        pieces = self.__create_pieces(colour)
        rows = self.__colour_for_rows(colour)
        self.__fill_positions(rows[0], pieces['bottom_row'])
        self.__fill_positions(rows[1], pieces['pawns'])
        return pieces['bottom_row'] + pieces['pawns']

    def __fill_positions(self, row: int, pieces: list['Piece']) -> None:
        """
        Fills a row on a chessboard with pieces
        :param row: int for the row to be filled
        :param pieces: Piece objects to be inserted
        :return: None
        """
        cols = len(self.board.board_mat[row])
        assert cols == len(pieces)
        for i in range(cols):
            pieces[i].swap_position(self.board.get_position((row, i)))

    def __create_pieces(self, colour: str) -> dict[str:list]:
        """
        Creates chess piece objects for a particular colour

        :param colour: str for colour
        :return: dict of length 2 containing the pieces entered, one entry is 'bottom_row' and the other is 'pawns'
        """
        king_move_finder = KingMoveFinder(self.board)
        traverse_helper = TraverseHelper()
        bearing_helper = BearingHelper()
        king = King(colour, king=None, move_finder=king_move_finder)
        king.king = king
        bottom_row = [Rook(colour, king=king, move_finder=RangedMoveFinder(self.board, traverse_helper),
                           bearing_helper=bearing_helper),
                      Knight(colour, king=king, move_finder=KnightMoveFinder(self.board)),
                      Bishop(colour, king=king, move_finder=RangedMoveFinder(self.board, traverse_helper),
                             bearing_helper=bearing_helper),
                      Queen(colour, king=king, move_finder=RangedMoveFinder(self.board, traverse_helper),
                            bearing_helper=bearing_helper),
                      king,
                      Bishop(colour, king=king, move_finder=RangedMoveFinder(self.board, traverse_helper),
                             bearing_helper=bearing_helper),
                      Knight(colour, king=king, move_finder=KnightMoveFinder(self.board)),
                      Rook(colour, king=king, move_finder=RangedMoveFinder(self.board, traverse_helper),
                           bearing_helper=bearing_helper), ]
        pawns = []
        for i in range(8):
            pawns.append(Pawn(colour, king=king, move_finder = PawnMoveFinder(self.board)))
        return {"bottom_row": bottom_row, "pawns": pawns}
