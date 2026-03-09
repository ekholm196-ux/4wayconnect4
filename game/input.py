import pygame
from utility import resource_path
from coin import Coin
import time

class Input:
    def __init__(self, images, screen, board):
        self.team = 0
        self.images = images
        self.image = self.images[self.team]
        self.screen = screen
        self.x = 0
        self.y = 0
        self.width = self.image.get_width()
        self.height = self.image.get_height()
        self.board = board
        self.placement_points = []

        """
        Making the placement points for coins, using rectangles so that collision with the cursor can be checked.
        They are stored in a list, as tuples, so that each rectangle has a correspongding row, column and direction of travel.
        """
        for row in range(0, 6, 1):
            for col in range(0, 6, 1):
                if (row == 0):
                    coordinates = (173 + 24*col, 30)
                    self.placement_points.append(((pygame.Rect(coordinates, (self.image.get_width(), self.image.get_height()))), row, col, "DOWN"))
                elif (row == 5):
                    coordinates = (173 +24*col, self.screen.get_height() - 30 - self.image.get_height())
                    self.placement_points.append(((pygame.Rect(coordinates, (self.image.get_width(), self.image.get_height()))), row, col, "UP"))
                if (col == 0):
                    coordinates = (135, 68 + 24*row)
                    self.placement_points.append(((pygame.Rect(coordinates, (self.image.get_width(), self.image.get_height()))), row, col, "RIGHT"))
                elif (col == 5):
                    coordinates = (self.screen.get_width() - 135 - self.image.get_width(), 68 + 24*row)
                    self.placement_points.append(((pygame.Rect(coordinates, (self.image.get_width(), self.image.get_height()))), row, col, "LEFT"))

    #draws a coin over the cursor location
    def draw(self, x, y):
        if (self.image != None):
            self.screen.blit(self.image, (x, y))

    #updates things that should be updates every frame
    def update(self):
        self.placement()
        self.draw(self.x, self.y)
    
    #Finds the mouse position, snaps onto placement points if collding with them, and allows you to place a coin if the row/col is not full.
    def placement(self):
        self.x, self.y = pygame.mouse.get_pos()
        self.x -= self.width/2
        self.y -= self.height/2
        for placement in self.placement_points:
            if (placement[0].collidepoint((pygame.mouse.get_pos())) and self.board.updated):
                self.x = placement[0].x
                self.y = placement[0].y
                if (pygame.mouse.get_pressed()[0] and self.board.is_full(placement[1], placement[2], placement[3]) == False):
                    coin = Coin(self.screen, self.image, placement[1], placement[2], (placement[0].x, placement[0].y), self.team, self.board)
                    self.board.add_coin(coin, placement[3])
                    self.team = (self.team + 1) % 2
                    self.image = self.images[self.team]
                    time.sleep(0.1)