import pygame
from utility import screen, blip_sound

class Button:
    def __init__(self, rect, img, hover_img, on_click):
        self.rect = rect
        self.passive_img = img
        self.hover_img = hover_img
        self.on_click = on_click
        self.img = img
        self.loc = None
        self.passive_loc = (self.rect.x, self.rect.y)
        self.hover_loc = (self.rect.centerx - self.hover_img.get_width() / 2, self.rect.centery - self.hover_img.get_height() / 2)

    def draw(self):
        screen.blit(self.img, self.loc)

    def update(self):
        self.check_input()
        self.draw()

    def check_input(self):
        if self.rect.collidepoint(pygame.mouse.get_pos()):
            self.img = self.hover_img
            self.loc = self.hover_loc
            if pygame.mouse.get_pressed()[0]:
                pygame.mixer.Sound.play(blip_sound)
                self.on_click()
        else:
            self.img = self.passive_img
            self.loc = self.passive_loc