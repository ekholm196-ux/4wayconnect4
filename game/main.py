
import pygame
import os
import sys
import time
from board import Board
from input import Input
from win import Win
from utility import resource_path, particles, get_state
from menu import Menu

#Setting up pygame
pygame.init()
pygame.mixer.init()
pygame.display.set_caption('4WayConnect4')
pygame.mouse.set_visible(True)
screen_width = 480
screen_height = 270
gameClock = pygame.time.Clock()
font = pygame.font.Font(resource_path('game/fonts/ARCADECLASSIC.TTF'), 16)
#gameloop booleans
running = True

#for starting delta time
dt = 0

#main game loop
menu = Menu()
win = Win()
board = Board(win)
input = Input(board)
while running:
    dt = gameClock.tick(280)
    state = get_state()
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
    if state == 'MENU':
        menu.update()

    elif state == 'GAME':
        board.update(dt)
        particles.update(dt)
        input.update()

    elif state == 'END':
        win.update(dt)
        particles.update(dt)

    pygame.display.flip()
pygame.quit()      
