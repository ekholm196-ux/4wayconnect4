import json
from utility import menu_img, screen, return_img, returnhover_img, set_state, sfx
from slider import Slider
from button import Button
import pygame

class Settings:
    def __init__(self):
        with open('game/settings.json', 'r') as file:
            settings = json.load(file)
        self.master_volume = settings.get('master_volume')
        self.music = settings.get('music')
        self.sound_effects = settings.get('sound_effects')
        self.fullscreen = settings.get('fullscreen')
        self.frame_rate_cap = settings.get('frame_rate_cap')
        self.background = menu_img
        self.interactables = []
        self.return_button = Button(pygame.Rect((12, 12), (return_img.get_width(), return_img.get_height())),
                                 return_img, returnhover_img, self.return_menu)
        self.interactables.append(self.return_button)
        self.mv_slider = Slider((screen.get_width() / 2 - 100, 30), self.master_volume, self.change_mv, "MASTER VOLUME")
        self.interactables.append(self.mv_slider)
        self.sfx_slider = Slider((screen.get_width() / 2 - 100, 60), self.sound_effects, self.change_sfx, "SOUND EFFECTS")
        self.interactables.append(self.sfx_slider)
        self.music_sider = Slider((screen.get_width() / 2 - 100, 90), self.music, self.change_music, "MUSIC VOLUME")
        self.interactables.append(self.music_sider)

    def draw(self):
        screen.blit(self.background, (0, 0))

    def update(self):
        self.draw()
        for interactable in self.interactables:
            interactable.update()

    def return_menu(self):
        self.save_settings()
        set_state('MENU')


    def change_sfx(self, volume):
        self.sound_effects = volume
        for sound in sfx:
            sound.set_volume(self.master_volume*volume)

    def change_mv(self, volume):
        self.master_volume = volume
        for sound in sfx:
            sound.set_volume(self.master_volume*self.sound_effects)
        pygame.mixer.music.set_volume(self.master_volume*self.music)

    def change_music(self, volume):
        self.music = volume
        pygame.mixer.music.set_volume(self.master_volume*self.music)

    def save_settings(self):
        with open('game/settings.json', 'r') as file:
            settings = json.load(file)
        settings["master_volume"] = self.master_volume
        settings['music'] = self.music
        settings['sound_effects'] = self.sound_effects

        with open('game/settings.json', "w") as file:
            json.dump(settings, file, indent=4)
