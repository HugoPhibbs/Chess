import unittest

from src import Setup, Piece, King, Queen


class TestSetup(unittest.TestCase):

    def setUp(self) -> None:
        self.setup = Setup({'white_name':'Hugo', 'black_name': 'Tom'})

    def test_fill_colour(self):
        pass

    def test_fill_positions(self):
        fill_positions = self.setup._Setup__fill_positions

        # Test normally
        pieces = Setup._Setup__create_pieces("WHITE")['bottom_row']
        fill_positions(0, pieces) # Test runs with no errors

        # Test with list of pieces with wrong length
        pieces = [King('WHITE')]
        self.assertRaises(AssertionError, fill_positions, 0, pieces)

    def test_create_pieces(self):
        create_pieces = Setup._Setup__create_pieces

        # Test with white pieces
        pieces = create_pieces('WHITE')
        self.assertEqual(pieces['bottom_row'][0].type, 'ROOK')
        self.assertEqual(pieces['bottom_row'][4].type, 'KING')

        # Test with black pieces
        pieces = create_pieces('BLACK')
        self.assertEqual(pieces['bottom_row'][0].type, 'ROOK')
        self.assertEqual(pieces['bottom_row'][4].type, 'KING')

    def test_colour_for_rows(self):
        colour_for_rows = Setup._Setup__colour_for_rows

        # Test normally
        self.assertEqual((0, 1), colour_for_rows('WHITE'))
        self.assertEqual((7, 6), colour_for_rows('BLACK'))

        # Check raises value error
        self.assertRaises(ValueError, colour_for_rows, 'white')

    def test_fill_board(self):
        # Test normally
        pieces_dict = self.setup._Setup__fill_board()
        self.assertEqual(list(pieces_dict.keys()), ['white_pieces', 'black_pieces'])

    def test_create_board(self):
        # Test normally
        board = Setup._Setup__create_board()
        self.assertEqual(board.get_position((4, 3)).coords, (4, 3))

    def test_create_players(self):
        create_players = Setup._Setup__create_players
        # Test normally
        names = {'white_name':'Hugo', 'black_name': 'Tom'}
        pieces = {'white_pieces':[King(colour="WHITE"), Queen(colour="WHITE")], 'black_pieces' : [King(colour="BLACK"), Queen(colour="BLACK")]}
        players = create_players(names, pieces)
        self.assertEqual(players['white_player'].name, names['white_name'])


if __name__ == '__main__':
    unittest.main()
