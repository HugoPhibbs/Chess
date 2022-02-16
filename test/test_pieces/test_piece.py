import unittest

from src.game_logic.pieces import Piece

from test import test_game

class TestPiece(unittest.TestCase):

    def setUp(self) -> None:
        self.board = test_game.board
        self.pawn1 = self.board.get_position((1, 0)).piece

    def test_coords(self):
        # Check with non None position
        pass
        # Check with None position
        pass

    def test_value_is_valid(self):
        # Test with positive integer input
        self.assertTrue(Piece.value_is_valid(1))

        # Test with float input
        self.assertFalse(Piece.value_is_valid(1.4))

        # Test with 0
        self.assertTrue(Piece.value_is_valid(0))

        # Test with negative input
        self.assertFalse(Piece.value_is_valid(-1))

        # Test with None
        self.assertFalse(Piece.value_is_valid(None))

        # Test with a string
        self.assertFalse(Piece.value_is_valid("Str"))

    def test_colour_is_valid(self):
        # Test normally
        self.assertTrue(Piece.colour_is_valid("WHITE"))
        self.assertTrue(Piece.colour_is_valid("BLACK"))

        # Test with none input
        self.assertFalse(Piece.colour_is_valid(None))

    def test_can_move_to_coords(self):
        # Test with coordinates that a pawn can move to
        self.assertTrue(self.pawn1.can_move_to_coords((2, 0), self.board))

        # Test with a pawn that is out of range of some coordinates
        self.assertFalse(self.pawn1.can_move_to_coords((4, 0), self.board))





if __name__ == '__main__':
    unittest.main()
