import pygame
from utilities import load_image, grid_unit


class Block(pygame.sprite.Sprite):

    # Constructor. Pass in the color of the block,
    # and its x and y position
    def __init__(self, width=grid_unit, height=grid_unit, location=(200, 100)):
        # Call the parent class (Sprite) constructor
        pygame.sprite.Sprite.__init__(self)

        # Create an image of the block, and fill it with a color.
        # This could also be an image loaded from the disk.
        self.image = load_image('White_Block', (width, height))

        # Fetch the rectangle object that has the dimensions of the image
        # Update the position of this object by setting the values of rect.x and rect.y
        self.rect = self.image.get_rect()
        # pygame.draw.rect(self.image, red, self.rect.inflate(10, 10), 1)
        self.rect.midtop = location
