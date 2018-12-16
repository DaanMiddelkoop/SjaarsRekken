import pygame
import time
from board import Board
from hand import Hand
from bank import Bank
from bot import generate_move, minimax


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


def do_move(current_player, first_move):
    move = generate_move(board, [hand1, hand2], current_player, first_move)
    if move is None:
        return None
    _, _, _, _, _, s, i = move
    [hand1, hand2][current_player].remove_piece(i)
    [hand1, hand2][current_player].add_piece(bank.get_piece())
    return s


# Handle player 2
print("hand2 has: ", hand2.__str__())
score = do_move(1, True)
scores[1] += score

while True:
    minimax(board, [hand1, hand2], 0, 0, 0)
    # Handle player 1
    print("hand1 has: ", hand1.__str__())
    score = do_move(0, False)
    if score is None:
        break
    scores[0] += score

    # Handle board drawing
    board.draw(screen)
    pygame.display.flip()
    time.sleep(0.01)

    # Handle player 2
    print("hand2 has: ", hand2.__str__())
    score = do_move(1, False)
    if score is None:
        break
    scores[1] += score

    # Handle board drawing
    board.draw(screen)
    pygame.display.flip()
    time.sleep(0.01)

print("Done")
print(scores)
while True:
    pass
