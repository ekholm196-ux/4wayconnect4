
import pygame
import os
import sys
import time
from board import Board
from input import Input
from utility import screen, resource_path, particles

#Setting up pygame
pygame.init()
pygame.mixer.init()
pygame.display.set_caption('4WayConnect4')
pygame.mouse.set_visible(False)
screen_width = 480
screen_height = 270
screen = pygame.display.set_mode((screen_width, 270), pygame.SCALED)
gameClock = pygame.time.Clock()
font = pygame.font.Font(resource_path('game/fonts/ARCADECLASSIC.TTF'), 16)
#gameloop booleans
running = True
match_in_progress = False

#for starting delta time
dt = 0
last_time = time.time()

#main game loop
board = Board(132, 27)
input = Input(board)
while running:
    gameClock.tick()
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

    screen.fill((30, 30, 30))
    #FPS-text
    fps = gameClock.get_fps()
    fps_text = font.render(f"FPS {fps:.0f}", False, (98, 190, 196))
    screen.blit(fps_text, (10, 10))
    board.update(dt)
    particles.update(dt)
    input.update()
    pygame.display.flip()
    now = time.time()
    dt = (now - last_time) * 1000
    last_time = now
pygame.quit()      
