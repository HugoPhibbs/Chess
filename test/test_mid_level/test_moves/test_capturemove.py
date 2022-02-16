import unittest

from src.game_logic.mid_level import CaptureMove


class TestCaptureMove(unittest.TestCase):

    def setUp(self) -> None:
        from test import game
        self.board = game.board
        self.move1 = CaptureMove(self.board, (1, 0), (2, 0))
        self.move2 = CaptureMove(self.board, (1, 1), (7, 7))
        self.move3 = CaptureMove(self.board, (1, 0), (1, 1))
        self.move4 = CaptureMove(self.board, (7, 0), (3, 4))

    def test_execute(self):
        # Test normally
        self.assertEqual(None, self.move1.execute(False, True))
        self.assertTrue(self.board.get_position((1,0)).is_vacant)
        self.assertFalse(self.board.get_position((2, 0)).is_vacant)
        self.assertEqual(self.board.get_position((2, 0)).piece, self.move1.piece)
        self.assertTrue(self.move1.executed)

        # Test with a move that has already been executed
        self.assertRaises(AssertionError, self.move1.execute)

        # Test with a move that captures another piece
        self.assertEqual(self.board.get_position((7, 7)).piece, self.move2.execute(False, True))
        self.assertTrue(self.board.get_position((1, 1)).is_vacant)
        self.assertEqual(self.board.get_position((7, 7)).piece, self.move2.piece)

    def test_reverse(self):
        # Test normally
        self.move2.execute(False, True)
        self.assertEqual(self.move2.capture, self.move2._Move__reverse())
        self.assertEqual(self.move2.dest_pos.piece, self.move2.capture)
        self.assertEqual(self.move2.source_pos.piece, self.move2.piece)
        self.assertFalse(self.move2.executed)

        # Test with a move that hasn't been executed yet
        self.assertRaises(AssertionError, self.move1._Move__reverse)

    def test_dest_is_friendly_blocked(self):
        # Test normally
        self.assertTrue(self.move3._CaptureMove__dest_is_friendly_blocked())

        # Test with an empty destination
        self.assertFalse(self.move1._CaptureMove__dest_is_friendly_blocked())

        # Test with destination containing an enemy
        self.assertFalse(self.move2._CaptureMove__dest_is_friendly_blocked())




    def test_is_legal(self):
        pass

    def test_causes_friendly_check(self):
        pass

if __name__ == '__main__':
    unittest.main()
