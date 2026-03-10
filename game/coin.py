import pygame

class Coin:
    def __init__(self, screen, image, row, column, destination, team, board, direction):
        self.row = row
        self.col = column
        self.team = team
        self.board = board
        self.destination = destination
        self.screen = screen
        self.image = image        
        self.rect = self.image.get_rect()
        self.float_x = destination[0]
        self.float_y = destination[1]
        self.rect.x = destination[0]
        self.rect.y = destination[1]
        self.animation_ended = False
        self.collision_count = 0

        #initial momentum when coin is played
        self.momentum_x = 0
        self.momentum_y = 0
        self.directions = (0, 0)
        match direction:
            case "UP": 
                self.momentum_y = -0.5
            case "DOWN":
                self.momentum_y = 0.5
            case "RIGHT":
                self.momentum_x = 0.5
            case "LEFT":
                self.momentum_x = -0.5


    #moves the coin to a new row and column, not on the board but for knowing where to draw

    def move(self, row, col):
        self.row = row
        self.col = col
        self.distance_desired_x = abs(self.rect.x - (173 + self.col * 24))
        self.distance_desired_y = abs(self.rect.y - (68  + self.row * 24))

    def animate(self, dt):
        self.float_x += self.momentum_x*dt
        self.float_y += self.momentum_y*dt
        self.rect.x = self.float_x
        self.rect.y = self.float_y
        self.distance_desired_x -= abs(self.momentum_x*dt)
        self.distance_desired_y -= abs(self.momentum_y*dt)
        if (self.distance_desired_x <= 0 and self.distance_desired_y <= 0):
            self.momentum_x = 0
            self.momentum_y = 0
            self.rect.x = 173 + self.col * 24
            self.rect.y = 68  + self.row * 24
            self.float_x = self.rect.x
            self.float_y = self.rect.y
            self.animation_ended = True
        if (self.momentum_x or self.momentum_y):
            self.check_collision()

    #Draws coin at the desired place
    def draw(self):
        self.screen.blit(self.image, self.rect)
    
    #checks for the incoming collision of any coin this coin will push
    def check_collision(self):
        dx = (self.momentum_x > 0) - (self.momentum_x < 0)
        dy = (self.momentum_y > 0) - (self.momentum_y < 0)
        check_row = self.row + dy
        check_col = self.col + dx

        if not (0 <= check_row < 6 and 0 <= check_col < 6):
            return

        neighbour_coin = self.board.grid[check_row][check_col]
        if neighbour_coin and self.rect.colliderect(neighbour_coin.rect) and not neighbour_coin.momentum_y and not neighbour_coin.momentum_x:
            self.collision_count += 1
            neighbour_coin.momentum_y = self.momentum_y
            neighbour_coin.momentum_x = self.momentum_x
            self.momentum_y /= 2
            self.momentum_x /= 2
    
    #Updates that should happen in each frame
    def update(self, dt):
        if self.momentum_x or self.momentum_y:
            self.animation_ended = False
            self.animate(dt)
        self.draw()
    