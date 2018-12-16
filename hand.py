from collections import deque


class Hand:
    score = None
    pieces = None

    def __init__(self, bank, score=0):
        self.score = score
        self.pieces = deque()
        for _ in range(4):
            self.pieces.append(bank.get_piece())

    def add_piece(self, piece):
        if piece is not None:
            self.pieces.append(piece)

    def remove_piece(self, piece):
        li = list(self.pieces)
        li.pop(piece)
        self.pieces = deque(li)

    def get_pieces(self):
        return list(self.pieces)

    def __str__(self):
        result = ""
        for x in self.pieces:
            result += x.__str__() + ", "
        return result
