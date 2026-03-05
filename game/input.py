import pygame
from utility import scalar

class Input:
    def __init__(self, image, screen, board):
        self.team = 1
        self.image = image
        self.screen = screen
        self.x = 0
        self.y = 0
        self.board = board
        self.placement_points = []

        """
        Making the placement points for coins, using rectangles so that collision with the cursor can be checked,
        using scalar
        """
        for row in range(0, 6, 1):
            for col in range(0, 6, 1):
                if (row == 0):
                    coordinates = (173*scalar + 24*scalar*col, 30*scalar)
                    self.placement_points.append(((pygame.Rect(coordinates, (self.image.get_width(), self.image.get_height()))), row, col, "top"))
                elif (row == 5):
                    coordinates = (173*scalar +24*scalar*col, self.screen.get_height() - 30*scalar - self.image.get_height())
                    self.placement_points.append(((pygame.Rect(coordinates, (self.image.get_width(), self.image.get_height()))), row, col, "bottom"))
                if (col == 0):
                    coordinates = (135*scalar, 68*scalar + 24*scalar*row)
                    self.placement_points.append(((pygame.Rect(coordinates, (self.image.get_width(), self.image.get_height()))), row, col, "left"))
                elif (col == 5):
                    coordinates = (self.screen.get_width() - 135*scalar - self.image.get_width(), 68*scalar + 24*scalar*row)
                    self.placement_points.append(((pygame.Rect(coordinates, (self.image.get_width(), self.image.get_height()))), row, col, "right"))


    def draw(self, x, y):
        self.screen.blit(self.image, (x, y))

    def update(self):
        self.placement()
        self.draw(self.x, self.y)
    
    def placement(self):
        self.x, self.y = pygame.mouse.get_pos()
        self.x -= self.image.width/2
        self.y -= self.image.height/2
        for placement in self.placement_points:
            if (placement[0].collidepoint((pygame.mouse.get_pos()))):
                self.x = placement[0].x
                self.y = placement[0].y
