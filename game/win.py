from utility import state, redwin_img, greenwin_img, screen, set_state, explosion_sound
from particle import Particle
import random
import pygame

class Win:
    def __init__(self):
        self.image = None
        self.signx = (screen.get_width() - greenwin_img.get_width()) / 2
        self.signy = 0 - greenwin_img.get_height()
        self.momentum_y = 1
        self.animation_time = 0

    def set_winner(self, winner):
        if winner == 0:
            self.image = greenwin_img
        else:
            self.image = redwin_img

    def move_sign(self, dt):
        if self.signy <= (screen.get_height() - self.image.get_height()) / 2:
            self.signy += self.momentum_y*dt

    def draw_sign(self):
        screen.fill((20, 27, 34))
        screen.blit(self.image, (self.signx, self.signy))

    def update(self, dt):
        self.animation_time += dt
        self.move_sign(dt)
        self.draw_sign()
        if self.animation_time >= 3000:
            self.animation_time = 0
            pygame.mouse.set_visible(True)
            set_state('MENU')