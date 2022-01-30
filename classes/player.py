class Player:
    """
    Represents a Player in a game of chess
    """

    def __init__(self, name_: str, pieces_: list, colour_ : str):
        self.name = name_
        self.pieces = pieces_
        self.colour = colour_

    @property
    def colour(self):
        return self.__colour

    @colour.setter
    def colour(self, val):
        assert val in ["WHITE", "BLACK"]
        self.__colour = val

    @property
    def opponent_score(self):
        """
        Returns the score of the opponent player to this player,

        ie the value of the pieces that the opponent has captured

        :return: int as described
        """
        count = 0
        for piece in self.pieces:
            if piece.is_captured():
                count += piece.value
        return count
