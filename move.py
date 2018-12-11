

class Move:
    tile = None
    piece = None

    def __init__(self, tile, piece):
        self.tile = tile
        self.piece = piece

    def __eq__(self, other):
        return self.tile.__eq__(other.tile)

    def __hash__(self):
        return self.tile.__hash__()

    def __str__(self):
        top = "none"
        right = "none"
        left = "none"

        if self.piece.top is not None:
            top = self.piece.top
        if self.piece.left is not None:
            left = self.piece.left
        if self.piece.right is not None:
            right = self.piece.right

        return str(self.tile.x) + "," + str(self.tile.y) + " " + top + ":" + left + ":" + right