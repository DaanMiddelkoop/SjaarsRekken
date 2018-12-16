import random
from piece import Piece

default_pieces = [
    Piece("RED", "RED", "RED", 6),
    Piece("BLUE", "BLUE", "BLUE", 6),
    Piece("GREEN", "GREEN", "GREEN", 6),
    Piece("YELLOW", "YELLOW", "YELLOW", 6),
    Piece("PURPLE", "PURPLE", "PURPLE", 6),

    Piece("RED", "RED", "YELLOW", 5),
    Piece("RED", "RED", "PURPLE", 5),
    Piece("BLUE", "BLUE", "RED", 5),
    Piece("BLUE", "BLUE", "PURPLE", 5),
    Piece("GREEN", "GREEN", "RED", 5),
    Piece("GREEN", "GREEN", "BLUE", 5),
    Piece("YELLOW", "YELLOW", "GREEN", 5),
    Piece("YELLOW", "YELLOW", "BLUE", 5),
    Piece("PURPLE", "PURPLE", "YELLOW", 5),
    Piece("PURPLE", "PURPLE", "GREEN", 5),

    Piece("RED", "RED", "BLUE", 4),
    Piece("RED", "RED", "GREEN", 4),
    Piece("BLUE", "BLUE", "GREEN", 4),
    Piece("BLUE", "BLUE", "YELLOW", 4),
    Piece("GREEN", "GREEN", "YELLOW", 4),
    Piece("GREEN", "GREEN", "PURPLE", 4),
    Piece("YELLOW", "YELLOW", "RED", 4),
    Piece("YELLOW", "YELLOW", "PURPLE", 4),
    Piece("PURPLE", "PURPLE", "RED", 4),
    Piece("PURPLE", "PURPLE", "BLUE", 4),

    Piece("YELLOW", "BLUE", "PURPLE", 3),
    Piece("RED", "GREEN", "YELLOW", 3),
    Piece("BLUE", "GREEN", "PURPLE", 3),
    Piece("GREEN", "RED", "BLUE", 3),

    Piece("BLUE", "RED", "PURPLE", 2),
    Piece("YELLOW", "PURPLE", "RED", 2),
    Piece("YELLOW", "PURPLE", "GREEN", 2),

    Piece("GREEN", "RED", "PURPLE", 1),
    Piece("BLUE", "YELLOW", "GREEN", 1),
    Piece("RED", "YELLOW", "BLUE", 1),

    Piece(None, None, None, 1)
]


class Bank:
    pieces = None

    def __init__(self, pieces=None):
        if pieces is None:
            self.pieces = default_pieces

    def get_piece(self):
        if len(self.pieces) > 0:
            choice = random.randint(0, len(self.pieces) - 1)
            return self.pieces.pop(choice)
        return None

    def get_pieces(self):
        return self.pieces
