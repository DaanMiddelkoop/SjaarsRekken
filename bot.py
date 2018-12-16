import random
from copy import deepcopy

colors = ["BLUE", "RED", "GREEN", "PURPLE", "YELLOW"]


def generate_move(board, hand):
    moves = list(board.move_tracker.get_possible_moves())
    for move in moves:
        pieces_in_hand = hand.get_pieces()
        try:
            index = pieces_in_hand.index(move.piece)
            move.piece = pieces_in_hand[index]
            score = board.do_move(move)
            print("AI played move " + str(move.tile.x) + ", " + str(move.tile.y) + move.piece.__str__())
            return move.tile.x, move.tile.y, move.tile.piece.top, move.tile.piece.left, move.tile.piece.right, score, index
        except ValueError:
            continue
    return None


def minimax(board, hands, playerindex, depth, move):
    pass
