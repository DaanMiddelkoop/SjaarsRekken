from board import Board
import pygame
import time

def main():

    pygame.init()

    screen = pygame.display.set_mode((1280, 720))

    board = Board()
    board.do_move_xy(0, 0, "red", "red", "red")

    while True:
        p0_score = 0
        p1_score = 0
        # x, y = tuple(map(int, input("Enter move coords\n").split(" ")))
        # top, left, right = tuple(input("Enter top left right color").split(" "))
        # if not (board.do_move_xy(x, y, top, left, right)):
        #     print("thats not a valid move!")
        #     continue
        if not board.generate_move():
            break

        time.sleep(1) 

        board.draw(screen)

        pygame.display.flip()

    while True:
        time.sleep(1)

main()