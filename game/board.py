import pygame

class Board:
    def __init__(self, x, y, sprite, screen):
        self.x = x
        self.y = y
        self.image = sprite
        self.screen = screen

    def draw(self):
        self.screen.blit(self.image, (self.x ,self.y))


    def update(self):
        self.draw()