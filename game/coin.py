import pygame

class Coin:
    def __init__(self, screen, image, row, column, destination, team, board):
        self.row = row
        self.col = column
        self.team = team
        self.board = board
        self.destination = destination
        self.screen = screen
        self.image = image
        self.x = 0
        self.y = 0

    #moves the coin to a new row and column, not on the board but for knowing where to draw

    def move(self, row, col):
        self.row = row
        self.col = col
        
    

    #Draws coin at the desired place
    def draw(self):
        x = (173 + self.col * 24)
        y = (68  + self.row * 24)
        self.screen.blit(self.image, (x, y))
    
    #Updates that should happen in each frame
    def update(self):
        self.draw()
    