import unittest

from src.game_logic.top_level.game import Game

#TODO refactor private methods!


class TestPawn(unittest.TestCase):

    def setUp(self) -> None:
        self.board = Game().board
        self.pawn1 = self.board.get_position((1, 0)).piece
        self.knight2 = self.board.get_position((0, 1)).piece
        self.pawn2 = self.board.get_position((1, 3)).piece
        self.enemy_queen = self.board.get_position((7, 3)).piece
        self.enemy_rook1 = self.board.get_position((0, 7)).piece

    def test_attack_is_valid(self):
        pass

    def test_moves(self):
        pass

    def test_attack_coords(self):
        # Test with no pieces in attack range
        self.assertEqual(self.pawn1._Pawn__attack_coords(self.board), [])

        # Test with enemy directly in front
        self.enemy_queen.position.piece = None
        self.enemy_queen.position = self.board.get_position((2, 0))
        self.enemy_queen.position.piece = self.enemy_queen
        self.assertEqual(self.pawn1._Pawn__attack_coords(self.board), [])

        # Test with enemy to left
        self.enemy_rook1.position.piece = None
        self.enemy_rook1.position = self.board.get_position((2, 2)) #TODO
        self.enemy_rook1.position.piece = self.enemy_rook1
        self.assertEqual(self.pawn2._Pawn__attack_coords(self.board), [(2, 2)])

        # Test with enemy to right

    def test_forward_row_coef(self):
        # Test with a white pawn
        self.assertEqual(self.pawn1._Pawn__forward_row_coef(), 1)

        # Test with a black pawn
        self.assertEqual(self.board.get_position((6, 0)).piece._Pawn__forward_row_coef(), -1)

    def test_forward_coords(self):
        # Test on baseline
        actual = sorted(self.pawn1._Pawn__forward_coords(self.board))
        expected = sorted([(self.pawn1.position.coords[0] + 2, self.pawn1.position.coords[1]),
                    (self.pawn1.position.coords[0] + 1, self.pawn1.position.coords[1])])
        self.assertEqual(actual, expected)

        # Test with a friendly piece blocking it
        self.knight2.position.piece = None
        self.knight2.position = self.board.get_position((2, 0))
        self.knight2.position.piece = self.knight2
        actual = sorted(self.pawn1._Pawn__forward_coords(self.board))
        expected = []
        self.assertEqual(actual, expected)

        # Test with an enemy piece blocking pawn
        self.enemy_queen.position.piece = None
        self.enemy_queen.position = self.board.get_position((2, 3))
        self.enemy_queen.position.piece = self.enemy_queen
        actual = sorted(self.pawn2._Pawn__forward_coords(self.board))
        expected = []
        self.assertEqual(actual, expected)

        # Test with an enemy piece blocking a double move
        self.enemy_queen.position.piece = None
        self.enemy_queen.position = self.board.get_position((3, 3))
        self.enemy_queen.position.piece = self.enemy_queen
        actual = sorted(self.pawn2._Pawn__forward_coords(self.board))
        expected = [(2, 3)]
        self.assertEqual(actual, expected)

        # Test with a friendly piece blocking a double move
        self.knight2.position.piece = None
        self.knight2.position = self.board.get_position((3, 0))
        self.knight2.position.piece = self.knight2
        actual = sorted(self.pawn1._Pawn__forward_coords(self.board))
        expected = [(2, 0)]
        self.assertEqual(actual, expected)



if __name__ == '__main__':
    unittest.main()
