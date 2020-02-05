import os
import sys
import pygame

from utilities import load_image, base_width, base_height, black, white
from shape import Shape


def main(base_width, base_height):
    pygame.init()
    screen = pygame.display.set_mode((base_width, base_height))
    pygame.display.set_caption('Q-Tetris')

    background = pygame.Surface(screen.get_size())
    background = background.convert()

    image = load_image('big-galaxy', (base_width, base_height))

    background.blit(image, (0, 0))
    screen.blit(background, image.get_rect())

    grid_size = base_width, base_height = base_width - base_width/3, base_height + 10
    grid = pygame.Rect((4, -15), grid_size)

    screen.blit(background, image.get_rect())
    pygame.draw.rect(screen, white, grid, 10)

    i_shape = Shape('I')
    i_shape.blocks.draw(screen)
    while 1:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                sys.exit()

            if event.type == pygame.KEYDOWN and event.key == 32:
                i_shape.blocks.update()

        i_shape.blocks.draw(screen)
        pygame.display.flip()


if __name__ == "__main__":
    main(base_width, base_height)
