import pygame
import random
import math
from utility import particles

class Particle(pygame.sprite.Sprite):
    def __init__(self, x, y, momentum_x, momentum_y, screen):
        pygame.sprite.Sprite.__init__(self)
        self.screen = screen
        self.float_x = x
        self.float_y = y
        self.rect = pygame.Rect(self.float_x, self.float_y, 2, 2)
        self.vertical = False
        """
        based on the direction of the coin whom creates said collision particle effect, decide which direction(opposite) this particle 
        should travel, as well as a random angle in the other axis.
        """
        self.lifetime = 0
        self.lifetime_limit = random.randint(240, 320)
        self.angle = math.radians(random.randint(0, 360))
        if momentum_y:
            self.momentum_tot = -momentum_y/10
            self.momentum_x = math.sin(self.angle) * self.momentum_tot
            self.momentum_y = self.momentum_tot * math.cos(self.angle)
            self.vertical = True
        else:
            self.momentum_tot = -momentum_x/10
        self.momentum_x = math.sin(self.angle) * self.momentum_tot
        self.momentum_y = self.momentum_tot * math.cos(self.angle)
        particles.add(self)
        
    #moves/animates the particle
    def animate(self, dt):
        self.lifetime += 1
        self.float_x += self.momentum_x*dt
        self.float_y += self.momentum_y*dt
        self.rect.x = self.float_x
        self.rect.y = self.float_y
        print(self.float_x, self.float_y, self.momentum_x, self.momentum_y)
        if self.lifetime > self.lifetime_limit:
            self.kill()

    #draws the particle
    def draw(self):
        pygame.draw.rect(self.screen, [255, 127, 0], self.rect)
    
    #updates the particle for each frame
    def update(self, dt):
        self.animate(dt)
        self.draw()