import pygame
import os
import sys
import time
from utility import resource_path
from board import Board
from input import Input

#Setting up pygame
pygame.init()
pygame.mixer.init()
pygame.display.set_caption('4WayConnect4')
screen_width = 480
screen_height = 270
screen = pygame.display.set_mode((screen_width, screen_height), pygame.SCALED)
gameClock = pygame.time.Clock()
font = pygame.font.SysFont("consolas", 24)

#gameloop booleans
running = True
match_in_progress = False

#for starting delta time
dt = 0
last_time = time.time()

#loading sprites
redcoin_img = pygame.image.load(resource_path('game/sprites/redcoin-sheet.png')).convert_alpha()
greencoin_img = pygame.image.load(resource_path('game/sprites/greencoin-sheet.png')).convert_alpha()
board_spritesheet = pygame.image.load(resource_path('game/sprites/board-sheet.png')).convert_alpha()


#main game loop
board = Board(132, 27, board_spritesheet, screen)
input = Input(greencoin_img, screen)
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

    screen.fill((30, 30, 30))

    #FPS-text
    fps = gameClock.get_fps()
    fps_text = font.render(f"FPS: {fps:.0f}", True, (255, 255, 255))
    screen.blit(fps_text, (10, 10))
    board.update(dt)
    input.update()
    pygame.display.flip()

    now = time.time()
    dt = (now - last_time) * 1000
    last_time = now

    gameClock.tick()

pygame.quit()      