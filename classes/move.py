class Move:
    """
    Represents a completed move in a game of chess
    """

    def __init__(self, piece_, source_, dest_, capture_=None):
        self.piece = piece_
        self.source = source_
        self.dest = dest_
        self.capture = capture_

    def __repr__(self):


