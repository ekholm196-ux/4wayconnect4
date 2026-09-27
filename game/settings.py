import json
from utility import menu_img, screen
from slider import Slider

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
        self.mv_slider = Slider((50, 50), self.master_volume)

    def draw(self):
        screen.blit(self.background, (0, 0))

    def update(self):
        self.draw()
        self.mv_slider.update()
