import unittest

from src.game_logic.pieces import Bishop, Rook, Queen
from test import test_game


class TestRangedPiece(unittest.TestCase):

    def setUp(self) -> None:
        self.board = test_game.board
        self.bishop1 = self.board.get_position((0, 2)).piece
        self.queen1 = self.board.get_position((0, 3)).piece
        self.rook1 = self.board.get_position((0, 0)).piece

    def test_moves(self):
        pass

    def test_dfs_coords(self):
        # Test with a blocked piece
        self.assertEqual([], self.bishop1._RangedPiece__dfs_coords("NE", self.board))
        self.assertEqual([], self.queen1._RangedPiece__dfs_coords("NE", self.board))
        self.assertEqual([], self.rook1._RangedPiece__dfs_coords("N", self.board))

        # Test raises assertion error with wrong inputted bearing
        self.assertRaises(AssertionError, self.bishop1._RangedPiece__dfs_coords, "N", self.board)

        # Test with a piece that is not blocked!
        queen_pawn = self.board.get_position((1, 3)).piece
        queen_pawn.swap_position(self.board.get_position(3, 3))


    def test_move_coords(self):
        # Test with a piece that is blocked by other pieces
        self.assertEqual([], self.bishop1._RangedPiece__move_coords(self.board))
        pass

if __name__ == '__main__':
    unittest.main()
