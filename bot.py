import random
from copy import deepcopy
from move import Move
import random

colors = ["BLUE", "RED", "GREEN", "PURPLE", "YELLOW"]


def fits(side1, side2):
    return side1 is None or side1 == side2 or side2 is None


def generate_permutations(piece):
    top = piece.top
    left = piece.left
    right = piece.right

    p0 = deepcopy(piece)
    p1 = deepcopy(piece)
    p2 = deepcopy(piece)
    p3 = deepcopy(piece)
    p4 = deepcopy(piece)
    p5 = deepcopy(piece)

    p1.top = left
    p1.left = right
    p1.right = top

    p2.top = right
    p2.left = top
    p2.right = left

    p3.left = right
    p3.right = left

    p4.top = left
    p4.left = top

    p5.top = right
    p5.right = top

    return [p0, p1, p2, p3, p4, p5]


def generate_move(board, hands, player_index, first_turn):
    hand = hands[player_index % len(hands)]

    if first_turn:
        tile = board.get_xy(0, 4)
        piece = hand.get_pieces()[0]
        move = Move(tile, piece)
        score = board.do_move(move)
        return 0, 4, piece.top, piece.left, piece.right, score, 0

    # Do a next move

    moves = minimax(board, hands, player_index, 0, player_index)
    # if len(moves) > 0:
    #     move, index = random.choice(moves)
    if moves is not None:
        move, index = moves
        score = board.do_move(move)
        return move.tile.x, move.tile.y, move.tile.piece.top, move.tile.piece.left, move.tile.piece.right, score, index

    # moves = list(board.move_tracker.get_possible_moves())
    # for move in moves:
    #     for index in range(0, len(hand.get_pieces())):
    #         for perm in generate_permutations(hand.get_pieces()[index]):
    #             if fits(move.piece, perm):
    #                 move.piece = perm
    #                 score = board.do_move(move)
    #                 print("AI played move " + str(move.tile.x) + ", " + str(move.tile.y) + move.piece.__str__())
    #                 return move.tile.x, move.tile.y, move.tile.piece.top, move.tile.piece.left, move.tile.piece.right, score, index
    return None


def minimax(board, hands, player_index, depth, own_index):
    hand = hands[player_index % len(hands)]

    # Collect all possible moves
    heighest_score = -100

    moves = []
    best_move = None
    possible_positions = list(board.move_tracker.get_possible_moves())
    for move in possible_positions:
        for index in range(0, len(hand.get_pieces())):
            for perm in generate_permutations(hand.get_pieces()[index]):
                if fits(move.piece, perm):
                    if board.calc_score(Move(move.tile, perm)) > heighest_score:
                        moves.append((Move(move.tile, perm), index))

                        heighest_score = board.calc_score(Move(move.tile, perm))
                        best_move = (Move(move.tile, perm), index)

    print("possible moves:", len(moves))
    return best_move

