import pygame
from board import Board


screen = pygame.display.set_mode((1280, 720))
board = Board()

board.do_move_xy(0, 0, "RED", "RED", "RED")
while True:
    move = board.generate_move()
    if move is None:
        break

    board.draw(screen)
    pygame.display.flip()

print("Done")

while True:
    pass