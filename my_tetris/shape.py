import pygame
from block import Block
from utilities import v_speed, h_speed


class Shape(pygame.sprite.Sprite):
    def __init__(self, letter):
        self.blocks = None
        letter_surface = pygame.Surface((20, 80), pygame.SRCALPHA, 32)
        self.letter_surface = letter_surface.convert_alpha()
        self.last_location = None

        if letter == 'I':
            self.blocks = self._make_I()

    def update(self):
        self.last_location = self.letter_surface.get_rect()
        self.letter_surface = pygame.transform.rotate(self.letter_surface, 90)

    def _make_I(self):
        block_list = []
        incrementer = 0
        letter_surface_rect_top = self.letter_surface.get_rect().top

        for block in range(4):
            new_block = Block()
            self.letter_surface.blit(new_block.image, (0, letter_surface_rect_top + incrementer))
            incrementer += 20

        return pygame.sprite.RenderPlain(block_list)
