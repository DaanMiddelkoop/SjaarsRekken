

class Piece:
    top = None
    left = None
    right = None
    placed = False

    def __init__(self, top, left, right):
        self.top = top
        self.left = left
        self.right = right

    def __eq__(self, other):
        return self.top == other.top and self.left == other.left and self.right == other.right

