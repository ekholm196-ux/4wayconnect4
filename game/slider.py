from utility import slider_img, bar_img, screen, font
import pygame

class Slider:
    def __init__(self, loc, gauge_start, action, title):
        self.slider_img = slider_img
        self.bar_img = bar_img
        self.loc = loc
        self.slider_x = self.loc[0] + self.bar_img.get_width()*gauge_start
        self.slider_y = self.loc[1] - self.slider_img.get_height() / 2 + self.bar_img.get_height() / 2
        self.rect = pygame.Rect(self.slider_x - self.slider_img.get_width() / 2, self.slider_y, self.slider_img.get_width(), self.slider_img.get_height())
        self.value = gauge_start
        self.prev_pos = self.slider_x
        self.sliding = False
        self.action = action
        self.title = title

    def update(self):
         self.check_input()
         self.draw()

    def draw(self):
        screen.blit(self.bar_img, self.loc)
        screen.blit(self.slider_img, (self.slider_x - self.slider_img.get_width() / 2, self.slider_y))
        screen.blit(font.render(str(round(self.value*100)), False, (98, 190, 196)), (self.loc[0] + self.bar_img.get_width() + 4, self.loc[1] - self.bar_img.get_height() / 2))
        screen.blit(font.render(self.title, False, (98, 190, 196)), (self.loc[0], self.loc[1] - 18))
        

    def check_input(self):
        pos = pygame.mouse.get_pos()
        if pygame.mouse.get_pressed()[0] and self.rect.collidepoint(pos) and not self.sliding:
            self.prev_pos = pos[0]
            self.sliding = True
            pygame.mouse.set_visible(False)
        
        elif pygame.mouse.get_pressed()[0] and self.sliding:
            self.slider_x += pos[0] - self.prev_pos
            if self.slider_x <= self.loc[0]:
                self.slider_x = self.loc[0]
            elif self.slider_x >= self.loc[0] + self.bar_img.get_width():
                self.slider_x = self.loc[0] + self.bar_img.get_width()
            self.value = (self.slider_x - self.loc[0]) / self.bar_img.get_width()
            self.rect.x = self.slider_x - self.slider_img.get_width() / 2
            self.prev_pos = pos[0]
        elif not pygame.mouse.get_pressed()[0] and self.sliding:
            self.sliding = False
            pygame.mouse.set_visible(True)
            self.action(self.get_value())

    def get_value(self):
         return self.value