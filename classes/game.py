from classes.pieces.piece import Piece


class Game:

    def start(self):
        pass

    def create_board(self):
        q_w = Piece("QUEEN", "WHITE")
        q_b = Piece("QUEEN", "BLACK")

        k_w = Piece("KING", "WHITE")
        k_b = Piece("KING", "BLACK")

        r_w_1 = Piece("ROOK", "WHITE")
        r_w_2 = Piece("ROOK", "WHITE")
        r_b_1 = Piece("ROOK", "BLACK")
        r_b_2 = Piece("ROOK", "BLACK")

        b_w_1 = Piece("BISHOP", "WHITE")
        b_w_2 = Piece("BISHOP", "WHITE")
        b_b_1 = Piece("BISHOP", "BLACK")
        b_b_2 = Piece("BISHOP", "BLACK")

        k_w_1 = Piece("KNIGHT", "WHITE")
        k_w_2 = Piece("KNIGHT", "WHITE")
        k_b_1 = Piece("KNIGHT", "BLACK")
        k_b_2 = Piece("KNIGHT", "BLACK")

        p_w_1 = Piece("PAWN", "WHITE")
        p_w_2 = Piece("PAWN", "WHITE")
        p_w_3 = Piece("PAWN", "WHITE")
        p_w_4 = Piece("PAWN", "WHITE")
        p_w_5 = Piece("PAWN", "WHITE")
        p_w_6 = Piece("PAWN", "WHITE")
        p_w_7 = Piece("PAWN", "WHITE")
        p_w_8 = Piece("PAWN", "WHITE")

        p_b_1 = Piece("PAWN", "BLACK")
        p_b_2 = Piece("PAWN", "BLACK")
        p_b_3 = Piece("PAWN", "BLACK")
        p_b_4 = Piece("PAWN", "BLACK")
        p_b_5 = Piece("PAWN", "BLACK")
        p_b_6 = Piece("PAWN", "BLACK")
        p_b_7 = Piece("PAWN", "BLACK")
        p_b_8 = Piece("PAWN", "BLACK")

        board_mat = [[None] * 8 for i in range(8)]
        board_mat[0] = [r_w_1, k_w_1, b_w_1, q_w, k_w, b_w_2, k_w_2, r_w_1]
        board_mat[1] = [p_w_1, p_w_2, p_w_3, p_w_4, p_w_5, p_w_6, p_w_7, p_w_8]
        board_mat[7] = [r_b_1, k_b_1, b_b_1, q_b, k_b, b_b_2, k_b_2, r_b_1]
        board_mat[6] = [p_b_1, p_b_2, p_b_3, p_b_4, p_b_5, p_b_6, p_b_7, p_b_8]