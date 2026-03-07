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

    #moves the coin to a new row and column, not on the board but for knowing where to draw

    def move(self, row, col):
        self.row = row
        self.col = col
    

    #Draws coin at the desired place
    def draw(self):
        x = scalar * (173 + self.col * 24)
        y = scalar * (68  + self.row * 24)
        self.screen.blit(self.image, (x, y))

    
    #Updates that should happen in each frame
    def update(self):
        self.draw()
    