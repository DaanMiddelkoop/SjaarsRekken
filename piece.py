

class Piece:
    top = None
    left = None
    right = None
    score = None
    placed = False

    def __init__(self, top, left, right, score=None):
        self.top = top
        self.left = left
        self.right = right
        self.score = score

    def __eq__(self, other):
        return (self.top == other.top or self.top is None or other.top is None) and \
               (self.left == other.left or self.left is None or other.left is None) and \
               (self.right == other.right or self.right is None or other.right is None)

    def __str__(self):
        stop = "None"
        sleft = "None"
        sright = "None"

        if self.top is not None:
            stop = self.top

        if self.left is not None:
            sleft = self.left

        if self.right is not None:
            sright = self.right
        return stop + sleft + sright

