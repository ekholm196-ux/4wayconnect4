import pygame
from utility import playbutton_img, settingsbutton_img, set_state, screen, menu_img, settingsbuttonhover_img, playbuttonhover_img, blip_sound

class Menu:
    def __init__(self):
        self.background = None
        self.playbutton = playbutton_img
        self.playbutton_rect = pygame.Rect(((screen.get_width() - self.playbutton.get_width()) / 2, (screen.get_height() / 2 - self.playbutton.get_height() / 2) - 32), (self.playbutton.get_width(), self.playbutton.get_height()))
        self.settingsbutton = settingsbutton_img
        self.settingsbutton_rect = pygame.Rect(((screen.get_width() - self.settingsbutton.get_width()) / 2, (screen.get_height() / 2 - self.settingsbutton.get_height() / 2 + 32)), (self.settingsbutton.get_width(), self.settingsbutton.get_height()))
        self.background = menu_img
        self.loc = (0, 0)

    #checks if the user has pressed any of the buttons in the menu
    def check_input(self):
        self.loc = pygame.mouse.get_pos()
        if self.playbutton_rect.collidepoint(self.loc):
            self.playbutton = playbuttonhover_img
            if pygame.mouse.get_pressed()[0]:
                pygame.mixer.Sound.play(blip_sound)
                pygame.mouse.set_visible(False)
                set_state('GAME')
        elif self.settingsbutton_rect.collidepoint(self.loc):
            self.settingsbutton = settingsbuttonhover_img
            if pygame.mouse.get_pressed()[0]:
                pygame.mixer.Sound.play(blip_sound)
                set_state('SETTINGS')
        else:
            self.settingsbutton = settingsbutton_img
            self.playbutton = playbutton_img
            

    def draw(self):
        screen.blit(self.background, (0, 0))
        screen.blit(self.playbutton, ((screen.get_width() - self.playbutton.get_width()) / 2, (screen.get_height() / 2 - self.playbutton.get_height() / 2) - 32))
        screen.blit(self.settingsbutton, ((screen.get_width() - self.settingsbutton.get_width()) / 2, (screen.get_height() / 2 - self.settingsbutton.get_height() / 2) + 32))

    def update(self):
        self.check_input()
        self.draw()
