import pygame
from utility import collision_sound
from particle import Particle

class Coin:
    def __init__(self, screen, image, row, column, destination, team, board, direction):
        self.row = row
        self.col = column
        self.team = team
        self.board = board
        self.destination = destination
        self.screen = screen
        self.sound = collision_sound
        self.image = image        
        self.rect = self.image.get_rect()
        self.float_x = destination[0]
        self.float_y = destination[1]
        self.rect.x = destination[0]
        self.rect.y = destination[1]
        self.animation_ended = False
        """
        This variable is for the animation to be played if this is the coin being played and it collies, so we get a visual effect only 
        the played coin collides. It is briefly true in the add_coin function in board to allow the coin being played to trigger a 
        particle effect upon collision.
        """
        self.being_played = True

        #initial momentum when coin is played
        self.momentum_x = 0
        self.momentum_y = 0
        match direction:
            case "UP": 
                self.momentum_y = -0.5
                self.collision_point = [7, 0]
            case "DOWN":
                self.momentum_y = 0.5
                self.collision_point = [7, 14]
            case "RIGHT":
                self.momentum_x = 0.5
                self.collision_point = [14, 7]
            case "LEFT":
                self.momentum_x = -0.5
                self.collision_point = [0, 7]

    #moves the coin to a new row and column, not on the board but for knowing where to draw

    def move(self, row, col):
        self.row = row
        self.col = col
        self.distance_desired_x = abs(self.rect.x - (173 + self.col * 24))
        self.distance_desired_y = abs(self.rect.y - (68  + self.row * 24))

    """
    This function moves the sprite of the coin to the board position of the coin if they are not aligned, based off of the coins own 
    momentum. It also importantly sets the being_played attribute to False, since when a coin stops for the first time it means it 
    can no longer be the coin being in play, thus we do not want to initiate the particle effect if it collides.
    """
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
            self.being_played = False
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
            if self.being_played:
                x = self.rect.x 
                pygame.mixer.Sound.play(collision_sound)
                for i in range(60):
                    particle = Particle(self.rect.x + self.collision_point[0], self.rect.y + self.collision_point[1], self.screen)
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
    