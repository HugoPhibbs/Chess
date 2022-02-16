from src.game_logic.top_level.setup import Setup
from src.game_logic.mid_level.moves.move import Move


class Game:
    __curr_player: 'Player' = None  # Player whose turn it currently is

    def __init__(self, setup: Setup):
        self.white_player = setup.players['white_player']
        self.black_player = setup.players['black_player']
        self.board = setup.board

    def start_game(self):
        pass

    def next_turn(self):
        pass

    def curr_player_in_check(self, board: 'Board') -> bool:
        """
        Finds out if the current player who has their turn is in check

        :param board: Board object for this current game of chess
        :return:
        """
        return self.__curr_player.is_in_check(board)

    def next_player(self) -> 'Player':
        """
        Finds the player whose turn it is next

        :return: Player object as described
        """
        if self.__curr_player == 'WHITE':
            return self.black_player
        return self.white_player

    def switch_curr_player(self, board: 'Board') -> None:
        """
        Switches the current player who has their turn for this game

        :param board: Board object for this current game of chess
        :return: None
        """
        assert not self.__curr_player.is_in_check(board)
        if self.__curr_player.colour == 'WHITE':
            self.__curr_player = self.black_player
        else:
            self.__curr_player = self.white_player

    def player_in_checkmate(self, board: 'Board') -> bool:
        """
        Finds out if the current player is in checkmate or not
        :param board: Board object for this current game of chess
        :return: bool as described
        """
        return self.__curr_player.is_checkmated(board)

    def game_state(self) -> str:
        pass

    def moves_for_coords(self, coords: tuple[int, int]) -> list['Move']:
        pass

    def execute_move(self, moves: list['Move'], destination: str):
        pass
