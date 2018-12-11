from move import Move
from piece import Piece


class MoveTracker:
    available_moves = None

    def __init__(self):
        self.available_moves = set()

    def do_move(self, move):
        print("move to discard: ", move)
        print("moves before discard")
        for x in self.available_moves:
            print(x)
        self.available_moves.discard(move)

        print("after:")
        for x in self.available_moves:
            print(x)
        print("end")
        if move.tile.left is not None and not move.tile.left.piece.placed:
            self.available_moves.add(Move(move.tile.left, collect_possible_pieces(move.tile.left)))

        if move.tile.right is not None and not move.tile.right.piece.placed:
            self.available_moves.add(Move(move.tile.right, collect_possible_pieces(move.tile.right)))

        if move.tile.top is not None and not move.tile.top.piece.placed:
            self.available_moves.add(Move(move.tile.top, collect_possible_pieces(move.tile.top)))

    def is_available(self, move):
        for x in self.available_moves:
            if x.tile == move.tile:
                if x.piece.top is None or x.piece.top == move.piece.top:
                    if x.piece.left is None or x.piece.left == move.piece.left:
                        if x.piece.right is None or x.piece.right == move.piece.right:
                            return True
        return False


    def get_possible_moves(self):
        return self.available_moves


def collect_possible_pieces(tile):
    left = None
    right = None
    top = None

    if tile.left is not None and tile.left.piece is not None:
        left = tile.left.piece.right

    if tile.right is not None and tile.right.piece is not None:
        right = tile.right.piece.left

    if tile.top is not None and tile.top.piece is not None:
        top = tile.top.piece.top
    return Piece(top, left, right)


