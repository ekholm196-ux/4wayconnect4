import pygame

class Input:
    def __init__(self, image, screen):
        self.team = 1
        self.image = image
        self.screen = screen
        self.x = 0
        self.y = 0

    def draw(self, x, y):
        self.screen.blit(self.image, (x, y))

    def update(self):
        self.x, self.y = pygame.mouse.get_pos()
        self.x -= self.image.width/2
        self.y -= self.image.height/2
        self.draw(self.x, self.y)