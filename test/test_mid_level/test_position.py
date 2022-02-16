import unittest

from src.game_logic.top_level.setup import Setup
from src.game_logic.top_level.game import Game

class TestPosition(unittest.TestCase):

    def setUp(self) -> None:
        self.setup = Setup({'white_name':'Hugo', 'black_name': 'Tom'})
        self.board = Game(self.setup).board
        self.position1 = self.board.get_position((0, 0))
        self.position2 = self.board.get_position((3, 0))
        self.position3 = self.board.get_position((0, 7))

    def test_is_vacant(self):
        # Test with a non empty position
        self.assertFalse(self.position1.is_vacant)

        # Test with an empty position
        self.assertTrue(self.position2.is_vacant)

    def test_is_hostile(self):
        # Test with a non empty position, with enemy piece
        self.assertTrue(self.position1.is_hostile(colour="BLACK"))

        # Test with a position containing a friendly piece
        self.assertFalse(self.position1.is_hostile(colour="WHITE"))

        # Test with an empty position
        self.assertFalse(self.position2.is_hostile(colour = "BLACK"))
        self.assertFalse(self.position2.is_hostile(colour="WHITE"))

        # Test with None input
        self.assertFalse(self.position2.is_hostile(None))

    def test_row_str(self):
        self.assertEqual(self.position1._Position__row_str(), "1")
        self.assertEqual(self.position3._Position__row_str(), "1")

    def test_repr(self):
        self.assertEqual(self.position1.__repr__(), "A1")
        self.assertEqual(self.position3.__repr__(), "H1")

    def test_col_str(self):
        self.assertEqual(self.position1._Position__col_str(), "A")
        self.assertEqual(self.position3._Position__col_str(), "H")

    def test_is_friendly(self):
        # Test with a non empty position, with enemy piece
        self.assertFalse(self.position1.is_friendly(colour="BLACK"))

        # Test with a position containing a friendly piece
        self.assertTrue(self.position1.is_friendly(colour="WHITE"))

        # Test with an empty position
        self.assertFalse(self.position2.is_friendly("BLACK"))
        self.assertFalse(self.position2.is_friendly("WHITE"))

        # Test with None input
        self.assertFalse(self.position2.is_friendly(None))

    def test_has_piece_type(self):
        # Test with a non empty position
        self.assertTrue(self.position1.has_piece_type("ROOK"))
        self.assertFalse(self.position1.has_piece_type("KNIGHT"))

        # Test with an empty position
        self.assertFalse(self.position2.has_piece_type("QUEEN"))

        # Test with None input
        self.assertFalse(self.position2.has_piece_type(None))


if __name__ == '__main__':
    unittest.main()
