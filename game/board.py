import pygame
import time

class Board:
    def __init__(self, x, y, sprite : dict, screen):
        self.x = x
        self.y = y
        self.sprite = sprite
        self.screen = screen
        self.image = self.sprite
        self.animation_time = 0
        self.index = 0
        self.coins = []
        self.updated = True
        self.grid = [[None] * 6 for _ in range(6)]

    def animate(self, dt):
        self.animation_time += dt
        if self.animation_time >= 200:
            self.index = (self.index + 1) % 7
            self.animation_time = 0

    def draw(self):
        frame_width = self.image.get_width() / 7
        frame_height = self.image.get_height()
        frame_rect = pygame.Rect(self.index * frame_width, 0, frame_width, frame_height)
        self.screen.blit(self.image, (self.x ,self.y), frame_rect)



    def update(self, dt):
        self.animate(dt)
        self.draw()
        for coin in self.coins:
            coin.update()
        self.updated = True

    def add_coin(self, coin, row, col):
        self.coins.append(coin)
        self.updated = False
    
    """Returns the true if a row or column is full, depending on direction"""
    def is_full(self, row, col, direction):
        if (direction == "UP" or direction == "DOWN"):
                return all(row[col] is not None for row in self.grid)

        else:
            return all(self.grid[row])
