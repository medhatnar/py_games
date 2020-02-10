import pygame
import time
from block import Block
from utilities import V_SPEED, H_SPEED, SPACE_BAR, LEFT, RIGHT, DOWN


class Shape(pygame.sprite.Sprite):
    def __init__(self, letter):
        self.blocks = None
        letter_surface = pygame.Surface((20, 80), pygame.SRCALPHA, 32)
        self.letter_surface = letter_surface.convert_alpha()
        self.x_pos = 200
        self.y_pos = 100
        self.last_location = None

        if letter == 'I':
            self.blocks = self._make_I()

    def update(self, key):
        self.last_location = self.letter_surface.get_rect()

        if key == SPACE_BAR:
            self.letter_surface = pygame.transform.rotate(
                self.letter_surface, 90)
        elif key == LEFT:
            self.x_pos -= H_SPEED

    def _make_I(self):
        block_list = []
        incrementer = 0
        letter_surface_rect_top = self.letter_surface.get_rect().top

        for block in range(4):
            new_block = Block()
            self.letter_surface.blit(
                new_block.image, (0, letter_surface_rect_top + incrementer))
            incrementer += 20

        return pygame.sprite.RenderPlain(block_list)
