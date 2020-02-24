import pygame
from utilities import load_image, GRID_UNIT


class Block(pygame.sprite.Sprite):

    # Constructor. Pass in the color of the block,
    # and its x and y position
    def __init__(self, color, width=GRID_UNIT, height=GRID_UNIT):
        # Call the parent class (Sprite) constructor
        pygame.sprite.Sprite.__init__(self)

        # Create an image of the block, and fill it with a color.
        # This could also be an image loaded from the disk.
        self.image = load_image(color, (width, height))
        self.x = 0
        self.y = 0
        self.width = width
        self.height = height
        # Fetch the rectangle object that has the dimensions of the image
        # Update the position of this object by setting the values of rect.x and rect.y
        self.rect = pygame.Rect((self.x, self.y), (GRID_UNIT, GRID_UNIT))
        self.rect.x = self.x
        self.rect.y = self.y

        


