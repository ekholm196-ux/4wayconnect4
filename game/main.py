
import pygame
import os
import sys
import time
from board import Board
from input import Input
from win import Win
from utility import screen, resource_path, particles, get_state

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
win = Win()
board = Board(win)
input = Input(board)
while running:
    gameClock.tick(280)
    state = get_state()
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
    if state == 'MENU':
        pass

    elif state == 'GAME':
        board.update(dt)
        particles.update(dt)
        input.update()

    elif state == 'END':
        win.update(dt)
        particles.update(dt)
        
    pygame.display.flip()
    now = time.time()
    dt = (now - last_time) * 1000
    last_time = now
pygame.quit()      
