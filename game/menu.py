import pygame
from utility import playbutton_img, settingsbutton_img, set_state, screen, menu_img, settingsbuttonhover_img, playbuttonhover_img
from button import Button

class Menu:
    def __init__(self):
        self.background = menu_img
        self.loc = (0, 0)
        self.playbutton = Button(pygame.Rect(((screen.get_width() - playbutton_img.get_width()) / 2, (screen.get_height() / 2 - playbutton_img.get_height() / 2) - 32), (playbutton_img.get_width(), playbutton_img.get_height())),
                                 playbutton_img, playbuttonhover_img, self.start)
        self.settingsbutton = Button(pygame.Rect(((screen.get_width() - settingsbutton_img.get_width()) / 2, (screen.get_height() / 2 - settingsbutton_img.get_height() / 2 + 32)), (settingsbutton_img.get_width(), settingsbutton_img.get_height())),
                                     settingsbutton_img, settingsbuttonhover_img, self.settings)
        self.buttons = [self.playbutton, self.settingsbutton]

    def draw(self):
        screen.blit(self.background, (0, 0))

    def update(self):
        self.draw()
        for button in self.buttons:
            button.update()

    def start(self):
        set_state('GAME')

    def settings(self):
        set_state('SETTINGS')