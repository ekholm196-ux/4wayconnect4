import pygame
import random
import math
from utility import particles

class Particle(pygame.sprite.Sprite):
    def __init__(self, x, y, screen):
        pygame.sprite.Sprite.__init__(self)
        self.screen = screen
        self.float_x = x
        self.float_y = y
        self.rect = pygame.Rect(self.float_x, self.float_y, 2, 2)
        self.animation_time = 0
        self.angle = math.radians(random.randint(0, 360))
        self.momentum_tot = 0.05
        self.momentum_x = math.sin(self.angle) * self.momentum_tot
        self.momentum_y = self.momentum_tot * math.cos(self.angle)
        particles.add(self)
        
    #moves/animates the particle
    def animate(self, dt):
        self.animation_time += 1
        self.float_x += self.momentum_x*dt
        self.float_y += self.momentum_y*dt
        self.rect.x = self.float_x
        self.rect.y = self.float_y
        if self.animation_time > 100:
            self.kill()

    #draws the particle
    def draw(self):
        pygame.draw.rect(self.screen, [255, 127, 0], self.rect)
    
    #updates the particle for each frame
    def update(self, dt):
        self.animate(dt)
        self.draw()