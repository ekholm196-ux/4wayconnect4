import sys
import os
import pygame

def resource_path(relative_path):
    """" Get absolute path to resource, this is in case of converting to exe with PyInstaller """
    try:
    # PyInstaller creates a temp folder and stores path in _MEIPASS
        base_path = sys._MEIPASS
    except Exception:
        base_path = os.path.abspath(".")

    return os.path.join(base_path, relative_path)

#Setting up pygame
pygame.init()
pygame.mixer.init()
pygame.display.set_caption('4WayConnect4')
pygame.mouse.set_visible(False)
screen_width = 480
screen_height = 270
screen = pygame.display.set_mode((screen_width, 270), pygame.SCALED)
gameClock = pygame.time.Clock()
#gameClock.tick(60)
font = pygame.font.SysFont("consolas", 24)

layers = pygame.sprite.LayeredUpdates()
particles = pygame.sprite.Group()

#load all sounds and images
redcoin_img = pygame.image.load(resource_path('game/sprites/redcoin-sheet.png')).convert_alpha()
greencoin_img = pygame.image.load(resource_path('game/sprites/greencoin-sheet.png')).convert_alpha()
board_spritesheet = pygame.image.load(resource_path('game/sprites/board-sheet.png')).convert_alpha()
grid_img = pygame.image.load(resource_path('game/sprites/grid-sheet.png')).convert_alpha()
play_sound = pygame.mixer.Sound(resource_path('game/sounds/play_coin.wav'))
collision_sound = pygame.mixer.Sound(resource_path('game/sounds/collision.wav'))
play_sound.set_volume(0.1)
collision_sound.set_volume(0.05)