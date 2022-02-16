import unittest

from src.game_logic.mid_level.support.board import Board
from test import test_game


class TestBoard(unittest.TestCase):
    """
    Test case for Board object
    """

    def setUp(self):
        self.board = test_game.board

    def test_get_position(self):
        # Test with valid coords
        expected = self.board.board_mat[0][0]
        actual = self.board.get_position((0, 0))
        self.assertEqual(expected, actual)

        # Test with invalid coords
        self.assertRaises(AssertionError, self.board.get_position, (-1, '1'))

    def test_get_row(self):
        pass  # TODO

    def test_coords_in_board(self):
        # Test edge cases, in board
        coords_in_board = lambda coords: Board._Board__coords_in_board(coords)
        self.assertTrue(coords_in_board((0, 0)))
        self.assertTrue(coords_in_board((0, 7)))
        self.assertTrue(coords_in_board((7, 7)))
        self.assertTrue(coords_in_board((7, 0)))

        # Test with edge cases, outside board
        self.assertFalse(coords_in_board((-1, 2)))
        self.assertFalse(coords_in_board((-1, 0)))
        self.assertFalse(coords_in_board((-1, -1)))

        # Test with None input
        self.assertRaises(AssertionError, coords_in_board, None)

        # Test with coords not on edge
        self.assertTrue(coords_in_board((3, 3)))

        # Test with string input
        self.assertRaises(AssertionError, coords_in_board, "str")

    def test_coords_are_coords(self):
        coords_are_coords = Board._Board__coords_are_coords

        # Test with None input
        self.assertFalse(coords_are_coords(None))

        # Test with string input
        self.assertFalse(coords_are_coords("str"))

        # Test with invalid tuple input
        self.assertFalse(coords_are_coords((5, "str")))
        self.assertFalse(coords_are_coords((5)))
        self.assertFalse(coords_are_coords((5, "str", Board([]))))
        self.assertFalse(coords_are_coords((5, -1.3)))

        # Test with valid tuple input
        self.assertTrue(coords_are_coords((1, 1)))

    def test_coords_are_valid(self):
        # Test with None input
        self.assertFalse(Board.coords_are_valid(None))

        # Test with valid input
        self.assertTrue(Board.coords_are_valid((1, 1)))
        self.assertTrue(Board.coords_are_valid((0, 0)))
        self.assertTrue(Board.coords_are_valid((0, 3)))
        self.assertTrue(Board.coords_are_valid((1, 2)))

        # Test with str input
        self.assertFalse(Board.coords_are_valid("str"))


if __name__ == '__main__':
    unittest.main()
