import pygame
import time
from board import Board
from hand import Hand
from bank import Bank
from bot import generate_move


def wait_key():
    while True:
        for event in pygame.event.get():
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_SPACE:
                    return

pygame.init()
screen = pygame.display.set_mode((1280, 720))
board = Board()
bank = Bank()
hand1 = Hand(bank)
hand2 = Hand(bank)

scores = [0, 0]


# Do first move

piece = hand2.get_pieces()[0]
score = board.do_move_xy(1, 3, piece.top, piece.left, piece.right)

print("hand2 has: ", hand2.__str__())
hand2.remove_piece(0)
hand2.add_piece(bank.get_piece())
scores[1] += score


def do_move(b, h):
    move = generate_move(b, h)
    if move is None:
        return None
    _, _, _, _, _, s, i = move
    h.remove_piece(i)
    h.add_piece(bank.get_piece())
    return s

while True:
    # Handle player 1
    print("hand1 has: ", hand1.__str__())
    score = do_move(board, hand1)
    if score is None:
        break
    scores[0] += score

    # Handle board drawing
    board.draw(screen)
    pygame.display.flip()
    time.sleep(0.01)
    wait_key()

    # Handle player 2
    print("hand2 has: ", hand2.__str__())
    score = do_move(board, hand2)
    if score is None:
        break
    scores[1] += score

    # Handle board drawing
    board.draw(screen)
    pygame.display.flip()
    time.sleep(0.01)
    wait_key()

print("Done")
print(scores)
while True:
    pass
