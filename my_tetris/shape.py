import pygame
import time
from block import Block
from utilities import WHITE_BLOCK, GRID_UNIT, FALL_SPEED, V_SPEED, H_SPEED, SPACE_BAR, LEFT, RIGHT, DOWN


class Shape(pygame.sprite.Sprite):
    def __init__(self):
        self.blocks = []
        letter_surface = pygame.Surface((15, 60), pygame.SRCALPHA, 32)
        self.letter_surface = letter_surface.convert_alpha()
        self.last_location = self.letter_surface.get_rect()
        self.x_pos = 195
        self.y_pos = 30
        self.angle = 0
        self.rect = pygame.Rect(self.x_pos, self.y_pos, 15, 60)
        self.rect = pygame.Rect(self.x_pos, self.y_pos, 15, 60)
        self._make_I()
        self.sprite_group = pygame.sprite.Group(self.blocks)

    def fall(self):
        self.last_location = self.letter_surface.get_rect()
        if self.y_pos + FALL_SPEED < 585:
            self.y_pos += FALL_SPEED
            self.update_blocks(y=self.y_pos)

    def update(self, key):
        x = self.x_pos
        y = self.y_pos
        self.last_location = self.letter_surface.get_rect()
        self.rect = pygame.Rect(self.x_pos, self.y_pos, 15, 60) if self.angle == 0 else pygame.Rect(self.x_pos, self.y_pos, 60, 15)

        if key == SPACE_BAR:
            new_surface = pygame.transform.rotate(
                self.letter_surface, 90)
            self.letter_surface = new_surface
            if self.angle == 0:
                self.angle = 1
            else:
                self.angle = 0
            self.update_blocks()
        elif key == LEFT:
            self.x_pos -= H_SPEED
            self.update_blocks()
        elif key == RIGHT:
            if x + H_SPEED <= 400:
                self.x_pos += H_SPEED
                self.update_blocks()
        elif key == DOWN:
            if y + V_SPEED <= 580:
                self.y_pos += V_SPEED
                self.update_blocks()

    def update_blocks(self):
        letter_surface_top_left = self.rect.topleft
        for i, block in enumerate(self.blocks):
            if self.angle == 0:
                block.y = (i * GRID_UNIT) + letter_surface_top_left[1]
                block.x = letter_surface_top_left[0]
            else:
                block.x = (i * GRID_UNIT) + letter_surface_top_left[0]
                block.y = letter_surface_top_left[1]

    def _make_I(self):
        incrementer = 0
        letter_surface_rect_top = self.letter_surface.get_rect().top

        for block in range(4):
            new_block = Block(WHITE_BLOCK)
            new_block.x = self.x_pos
            new_block.y = self.y_pos + incrementer
            self.blocks.append(new_block)

            self.letter_surface.blit(
                new_block.image, (0, letter_surface_rect_top + incrementer))
            incrementer += 15
