import pygame
import time

class Board:
    def __init__(self, x, y, sprite : dict, screen):
        self.x = x
        self.y = y
        self.sprite = sprite
        self.screen = screen
        self.image = self.sprite
        self.animation_time = 0
        self.index = 0
        self.coins = []
        self.updated = True
        self.score = [0, 0]
        self.grid = [[None] * 6 for _ in range(6)]

    def animate(self, dt):
        self.animation_time += dt
        if self.animation_time >= 200:
            self.index = (self.index + 1) % 7
            self.animation_time = 0

    def draw(self):
        frame_width = self.image.get_width() / 7
        frame_height = self.image.get_height()
        frame_rect = pygame.Rect(self.index * frame_width, 0, frame_width, frame_height)
        self.screen.blit(self.image, (self.x ,self.y), frame_rect)
    """
    The packing functions pack the coins in one direction, and then places the new coin at the end. 
    """
    def pack_down(self, coin):
        empty_space = 0
        for row in range(5, -1, -1):
            if (self.grid[row][coin.col] == None):
                empty_space += 1 
            else:
                c = self.grid[row][coin.col]
                self.grid[row][coin.col] = None
                self.grid[(row + empty_space)][coin.col] = c
                c.move(row + empty_space, coin.col)
        landing_row = empty_space - 1
        self.grid[landing_row][coin.col] = coin
        coin.move(landing_row, coin.col)

    def pack_up(self, coin):
        empty_space = 0
        for row in range(0, 6, 1):
            if (self.grid[row][coin.col] == None):
                empty_space += 1
            else:
                c = self.grid[row][coin.col]
                self.grid[row][coin.col] = None
                self.grid[(row - empty_space)][coin.col] = c
                c.move(row - empty_space, coin.col)
        landing_row = 6 - empty_space
        self.grid[landing_row][coin.col] = coin
        coin.move(landing_row, coin.col)

    def pack_right(self, coin):
        empty_space = 0
        for col in range(5, -1, -1):
            if (self.grid[coin.row][col] == None):
                empty_space += 1
            else:
                c = self.grid[coin.row][col]
                self.grid[coin.row][col] = None
                self.grid[coin.row][col + empty_space] = c
                c.move(coin.row, col + empty_space)
        landing_col = empty_space - 1
        self.grid[coin.row][landing_col] = coin
        coin.move(coin.row, landing_col)

    def pack_left(self, coin):
        empty_space = 0
        for col in range(0, 6, 1):
            if (self.grid[coin.row][col] == None):
                empty_space += 1
            else:
                c = self.grid[coin.row][col]
                self.grid[coin.row][col] = None
                self.grid[coin.row][col - empty_space] = c
                c.move(coin.row, col - empty_space)
        landing_col = 6 - empty_space
        self.grid[coin.row][landing_col] = coin
        coin.move(coin.row, landing_col)
    """
    Adds a new coing to the board and packs coins in the right direction. And after a new move has been made the board checks for 4 in a row
    """
    def add_coin(self, coin, direction):
        self.coins.append(coin)
        match direction:
            case "DOWN":
                self.pack_down(coin)
            case "UP":
                self.pack_up(coin)
            case "RIGHT":
                self.pack_right(coin)
            case "LEFT":
                self.pack_left(coin)
        self.check_game_over()

    def update(self, dt):
        self.animate(dt)
        self.draw()
        for coin in self.coins:
            coin.update()

    
    """
    Returns the true if a row or column is full, depending on direction
    """
    def is_full(self, row, col, direction):
        if (direction == "UP" or direction == "DOWN"):
                return all(row[col] is not None for row in self.grid)

        else:
            return all(self.grid[row])
        
    def check_rows(self):
        previous = None
        count = 1
        for row in self.grid:
            for coin in row:
                if (coin is None):
                    previous = None
                elif (coin.team == previous):
                    count += 1
                else:
                    count = 1
                    previous = coin.team
                if (count == 4):
                    self.score[coin.team] += 1
                    count = 1
   
    def check_cols(self):
        previous = None
        count = 1
        for column in range(0, 6, 1):
            for tile in range(0, 6, 1):
                coin = self.grid[tile][column]
                if (coin is None):
                    previous = None
                elif (coin.team == previous):
                    count += 1
                else:
                    count = 1
                    previous = coin.team
                if (count == 4):
                    self.score[coin.team] += 1
                    count = 1
    
    def check_diagonals(self):
        n = 6
        m = 6
        previous = None
        count = 1
        for line in range(4, 9):
            start_column = max(0, line - n)
            nbr_elements = min(line, m - start_column, n)
            for j in range(nbr_elements):
                row = min(n, line) - j - 1
                col = start_column + j
                coin = self.grid[row][col]
                if (coin == None):
                    previous = None
                elif (coin.team == previous):
                    count += 1
                else:
                    count = 1
                    previous = coin.team
                if (count == 4):
                    self.score[coin.team] += 1
                    count = 1

        previous = None
        count = 1
        for line in range(4, 9):
            start_column =(n-1) + min(0, line - n, n - line)
            nbr_elements = min(line, start_column + 1, n)
            for j in range(nbr_elements):
                row = min(n, line) - j - 1
                col = start_column - j
                coin = self.grid[row][col]
                if (coin == None):
                    previous = None
                elif (coin.team == previous):
                    count += 1
                else:
                    count = 1
                    previous = coin.team
                if (count == 4):
                    self.score[coin.team] += 1
                    count = 1

    def check_game_over(self):
        self.check_rows()
        self.check_cols()
        self.check_diagonals()
        if (self.score[0] > self.score[1]):
            print("Green wins!")
        elif(self.score[1] > self.score[0]):
            print("Red wins!")