import pygame

from copy import deepcopy
from moveTracker import MoveTracker
from piece import Piece
from move import Move
import random

colors = ["red", "blue", "yellow"]

class Board:
    tiles = None
    top = None
    move_tracker = None

    def __init__(self):
        self.tiles = []
        self.top = Tile(12, 0, 0, 0, self.tiles)
        self.move_tracker = MoveTracker()
        self.first_move = True

    def do_move(self, move):
        if self.first_move or self.move_tracker.is_available(move):
            self.first_move = False

            move.tile.piece = move.piece
            move.tile.piece.placed = True
            self.move_tracker.do_move(move)
            print("piece set in move", move.tile.piece)
            return True
        else:
            return False

    def do_move_xy(self, x, y, top, left, right):
        for tile_move in self.tiles:
            if tile_move.x == x and tile_move.y == y:
                print(tile_move.top, tile_move.left, tile_move.right)
                return self.do_move(Move(tile_move, Piece(top, left, right)))

    def generate_move(self):
        moves = list(self.move_tracker.get_possible_moves())
        if len(moves) > 0:
            move = moves[0]
            move.piece = deepcopy(move.piece)
            if move.piece.left is None:
                move.piece.left = random.choice(colors)

            if move.piece.right is None:
                move.piece.right = random.choice(colors)

            if move.piece.top is None:
                move.piece.top = random.choice(colors)


            self.do_move(move)
            print("AI played move " + str(move.tile.x) + ", " + str(move.tile.y) + ": " + move.piece.top + move.piece.left + move.piece.right)
            return True
        return False

    def draw(self, screen):
        for tile in self.tiles:
            scale = 20
            if tile.piece is not None:
                tile.draw(screen)






class Tile:
    top = None  # top/bot
    right = None  # right
    left = None  # left
    x = None
    y = None
    piece = Piece(None, None, None)

    def __init__(self, counter, cloning, x, y, tiles, top=None, left=None, right=None):
        self.x = x
        self.y = y

        self.top = top
        self.left = left
        self.right = right
        tiles.append(self)

        if counter > 0:
            if cloning == 0:
                self.top = Tile(counter - 1, 1, x, y + 1, tiles, top=self)
            elif cloning == 1:
                self.left = Tile(counter - 1, 0, x - 1, y, tiles, right=self)
                self.right = Tile(counter - 1, 2, x + 1, y, tiles, left=self)
            elif cloning == 2:
                self.top = Tile(counter - 1, 3, x, y + 1, tiles, top=self)
            elif cloning == 3:
                try:
                    self.left = self.top.left.left.top.right
                except AttributeError:
                    pass

                try:
                    self.top.left.left.top.right.right = self
                except AttributeError:
                    pass
                self.right = Tile(counter - 1, 2, x + 1, y, tiles, left=self)

    def __hash__(self):
        return (self.x * 1000) + self.y

    def draw(self, screen):
        scale = 50
        scale2 = 30
        if self.y % 2 == self.x % 2:
            pygame.draw.line(screen, (255, 255, 255),
                             (self.x * scale - scale2 + 300, self.y * scale + 100),
                             (self.x * scale + 300, self.y * scale - scale2 + 100), 10)
            if self.piece.left is not None:
                pygame.draw.line(screen, self.convert_colors(self.piece.left),
                                 (self.x * scale - scale2 + 300, self.y * scale + 100),
                                 (self.x * scale + 300, self.y * scale - scale2 + 100), 10)
            pygame.draw.line(screen, (255, 255, 255),
                             (self.x * scale + scale2 + 300, self.y * scale + 100),
                             (self.x * scale + 300, self.y * scale - scale2 + 100), 10)
            if self.piece.right is not None:
                pygame.draw.line(screen, self.convert_colors(self.piece.right),
                                 (self.x * scale + scale2 + 300, self.y * scale + 100),
                                 (self.x * scale + 300, self.y * scale - scale2 + 100), 10)
            pygame.draw.line(screen, (255, 255, 255),
                             (self.x * scale - scale2 + 300, self.y * scale + 100),
                             (self.x * scale + scale2 + 300, self.y * scale + 100), 10)
            if self.piece.top is not None:
                pygame.draw.line(screen, self.convert_colors(self.piece.top),
                                 (self.x * scale - scale2 + 300, self.y * scale + 100),
                                 (self.x * scale + scale2 + 300, self.y * scale + 100), 10)
        else:
            pygame.draw.line(screen, (255, 255, 255),
                             (self.x * scale - scale2 + 300, self.y * scale - scale2 + 100),
                             (self.x * scale + 300, self.y * scale + 100), 10)
            if self.piece.left is not None:
                pygame.draw.line(screen, self.convert_colors(self.piece.left),
                                 (self.x * scale - scale2 + 300, self.y * scale - scale2 + 100),
                                 (self.x * scale + 300, self.y * scale + 100), 10)
            pygame.draw.line(screen, (255, 255, 255),
                             (self.x * scale + scale2 + 300, self.y * scale - scale2 + 100),
                             (self.x * scale + 300, self.y * scale + 100), 10)
            if self.piece.right is not None:
                pygame.draw.line(screen, self.convert_colors(self.piece.right),
                                 (self.x * scale + scale2 + 300, self.y * scale - scale2 + 100),
                                 (self.x * scale + 300, self.y * scale + 100), 10)
            pygame.draw.line(screen, (255, 255, 255),
                             (self.x * scale - scale2 + 300, self.y * scale - scale2 + 100),
                             (self.x * scale + scale2 + 300, self.y * scale - scale2 + 100), 10)
            if self.piece.top is not None:
                pygame.draw.line(screen, self.convert_colors(self.piece.top),
                                 (self.x * scale - scale2 + 300, self.y * scale - scale2 + 100),
                                 (self.x * scale + scale2 + 300, self.y * scale - scale2 + 100), 10)
                #pygame.draw.rect(screen, self.convert_colors(self.piece.left),
                #                 (self.x * scale - scale2 + 300, self.y * scale, scale2, scale2))
        #     if self.piece.right is not None:
        #         pygame.draw.rect(screen, self.convert_colors(self.piece.right),
        #                          (self.x * scale + 300, self.y * scale, scale2, scale2))
        #     if self.piece.top is not None:
        #         pygame.draw.rect(screen, self.convert_colors(self.piece.top),
        #                          (self.x * scale - scale2 // 2 + 300, self.y * scale + scale2, scale2, scale2))
        # else:
        #     if self.piece.left is not None:
        #         pygame.draw.rect(screen, self.convert_colors(self.piece.left),
        #                          (self.x * scale - scale2 + 300, self.y * scale + scale2, scale2, scale2))
        #     if self.piece.right is not None:
        #         pygame.draw.rect(screen, self.convert_colors(self.piece.right),
        #                          (self.x * scale + 300, self.y * scale + scale2, scale2, scale2))
        #     if self.piece.top is not None:
        #         pygame.draw.rect(screen, self.convert_colors(self.piece.top),
        #                          (self.x * scale - scale2 // 2 + 300, self.y * scale, scale2, scale2))

    def convert_colors(self, color):
        if color == "red":
            return (255, 0, 0)

        if color == "blue":
            return (0, 0, 255)

        if color == "yellow":
            return (255, 255, 0)

        return (255, 255, 255)