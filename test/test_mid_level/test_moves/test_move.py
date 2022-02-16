import unittest


class TestMove(unittest.TestCase):

    def setUp(self) -> None:
        pass

    def test_something(self):
        self.assertEqual(True, False)  # add assertion here

    def test_causes_friendly_check(self):
        # Test normally
        self.move4.execute(False) # Move rook to pin pawn infront of king
        self.assertTrue(Move((2, 4), (5, 6), self.board)._Move__causes_friendly_check())

        # Test with moves that don't cause check
        self.assertFalse(self.move1._Move__causes_friendly_check())
        self.assertFalse(self.move3._Move__causes_friendly_check())
        self.assertFalse(self.move2._Move__causes_friendly_check())


if __name__ == '__main__':
    unittest.main()
