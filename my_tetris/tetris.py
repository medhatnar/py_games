import os
import sys
import pygame

from utilities import load_image, base_width, base_height, black, white
from shape import Shape

pygame.init()


class Tetris:
    def __init__(self, width=base_width, height=base_height):
        self.screen = pygame.display.set_mode((width, height))
        pygame.display.set_caption('Q-Tetris')

        background = pygame.Surface(self.screen.get_size())
        self.background = background.convert()

        self.image = load_image('big-galaxy', (width, height))

        self.background.blit(self.image, (0, 0))
        self.screen.blit(self.background, self.image.get_rect())

        grid_size = width, height = width - width/3, height + 10
        self.grid = pygame.Rect((4, -15), grid_size)


while 1:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            sys.exit()

    tetris = Tetris()
    tetris.screen.blit(tetris.background, tetris.image.get_rect())
    pygame.draw.rect(tetris.screen, white, tetris.grid, 10)

    i_shape = Shape('I')
    # pygame.transform.rotate(i_shape.letter, 180)
    i_shape.blocks.draw(tetris.screen)

    # for i, sprite in enumerate(i_shape.blocks):
    #     print(i, sprite)
    #     new_sprite = pygame.transform.rotate(sprite.image, 180)
    #     tetris.screen.blit(new_sprite, (200, 300))

    pygame.display.flip()
