import pygame
from utility import scalar

class Coin:
    def __init__(self, screen, image, row, column, destination, team, board):
        self.row = row
        self.col = column
        self.team = team
        self.board = board
        self.destination = destination
        self.screen = screen
        self.image = image

    def move(self, row, col):
        self.row = row
        self.col = col
    
    def draw(self):
        x = scalar * (173 + self.col * 24)
        y = scalar * (68  + self.row * 24)
        self.screen.blit(self.image, (x, y))

    def update(self):
        self.draw()
    