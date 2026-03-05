import pygame
from utility import scalar

class Coin:
    def __init__(self, screen, image, row, column, destination, team, direction, board):
        self.row = row
        self.col = column
        self.team = team
        self.direction = direction
        self.board = board
        self.destination = destination
        self.screen = screen
        self.image = image

    def play_coin(self, direction):
        empty_space = 0
        match direction:
            case "DOWN":
                for row in range(5, -1, -1):
                    if (self.board.grid[row][self.col] == None):
                        empty_space += 1 
                    else:
                        c = self.board.grid[row][self.col]
                        self.board.grid[row][self.col] = None
                        self.board.grid[(row + empty_space)][self.col] = c
                        c.move(row + empty_space, self.col)
                self.board.grid[self.row + empty_space - 1][self.col] = self
                self.move(row + empty_space -1, self.col)
            case "UP":
                for row in range(0, 6, 1):
                    if (self.board.grid[row][self.col] == None):
                        empty_space += 1
                    else:
                        c = self.board.grid[row][self.col]
                        self.board.grid[row][self.col] = None
                        self.board.grid[(row - empty_space)][self.col] = c
                        c.move(row - empty_space, self.col)
                self.board.grid[self.row - empty_space + 1][self.col] = self
                self.move(row - empty_space + 1, self.col)
            case "RIGHT":
                for col in range(5, -1, -1):
                    if (self.board.grid[self.row][col] == None):
                        empty_space += 1
                    else:
                        c = self.board.grid[self.row][col]
                        self.board.grid[self.row][col] = None
                        self.board.grid[self.row][col + empty_space] = c
                        c.move(self.row, col + empty_space)
                self.board.grid[self.row][col + empty_space - 1] = self
                self.move(self.row, col + empty_space - 1)
            case "LEFT":
                for col in range(0, 6, 1):
                    if (self.board.grid[self.row][col] == None):
                        empty_space += 1
                    else:
                        c = self.board.grid[self.row][col]
                        self.board.grid[self.row][col] = None
                        self.board.grid[self.row][col - empty_space] = c
                        c.move(self.row, col - empty_space)
                self.board.grid[self.row][col - empty_space + 1] = self
                self.move(self.row, col - empty_space + 1)
        print(self.board.grid)

    def move(self, row, col):
        self.row = row
        self.col = col
    
    def draw(self):
        x = scalar * (173 + self.col * 24)
        y = scalar * (68  + self.row * 24)
        self.screen.blit(self.image, (x, y))

    def update(self):
        self.draw()