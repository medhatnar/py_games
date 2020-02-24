import pygame
from block import Block
from utilities import FALL_SPEED, V_SPEED, H_SPEED, GRID_UNIT,  SPACE_BAR, LEFT, RIGHT, DOWN, LIGHT_PINK_BLOCK


class T_Shape(pygame.sprite.Sprite):
    def __init__(self):
        self.blocks = []
        self.letter_surface = pygame.Surface(
            (45, 30), pygame.SRCALPHA, 32).convert_alpha()
        self.last_location = self.letter_surface.get_rect()
        self.x_pos = 225
        self.y_pos = 90
        self.angle = 0
        self.rect = pygame.Rect(self.x_pos, self.y_pos, 45, 30)

        self._make_T()
        self.sprite_group = pygame.sprite.Group(self.blocks)

    def update(self, key):
        x = self.x_pos
        y = self.y_pos
        self.last_location = self.letter_surface.get_rect()
        self.rect = pygame.Rect(self.x_pos, self.y_pos, 45, 30) if self.angle == 0 else pygame.Rect(
            self.x_pos, self.y_pos, 30, 45)

        if key == SPACE_BAR:
            new_surface = pygame.transform.rotate(
                self.letter_surface, 90)
            self.letter_surface = new_surface
            if self.angle != 3:
                self.angle = self.angle + 1
            else:
                self.angle = 0
            self.update_blocks()
        elif key == LEFT:
            self.x_pos -= H_SPEED
        elif key == RIGHT:
            if x + H_SPEED <= 400:
                self.x_pos += H_SPEED
        elif key == DOWN:
            if y + V_SPEED <= 580:
                self.y_pos += V_SPEED

    def update_blocks(self):
        letter_surface_top_left = self.rect.topleft

        for i, block in enumerate(self.blocks):
            if self.angle == 0:
                if i == 3:
                    block.x = GRID_UNIT + letter_surface_top_left[0]
                    block.y = letter_surface_top_left[1]
                else:
                    block.x = (GRID_UNIT * i) + letter_surface_top_left[0]
                    block.y = GRID_UNIT + letter_surface_top_left[1]
            elif self.angle == 1:
                if i == 3:
                    block.x = letter_surface_top_left[0]
                    block.y = GRID_UNIT + letter_surface_top_left[1]
                else:
                    block.x = GRID_UNIT + letter_surface_top_left[0]
                    block.y = (GRID_UNIT * i) + letter_surface_top_left[1]
            elif self.angle == 2:
                if i == 3:
                    block.x = GRID_UNIT + letter_surface_top_left[0]
                    block.y = GRID_UNIT + letter_surface_top_left[1]
                else:
                    block.x = (GRID_UNIT * i) + letter_surface_top_left[0]
                    block.y = letter_surface_top_left[1]
            elif self.angle == 3:
                if i == 3:
                    block.x = GRID_UNIT + letter_surface_top_left[0]
                    block.y = GRID_UNIT + letter_surface_top_left[1]
                else:
                    block.x = letter_surface_top_left[0]
                    block.y = (GRID_UNIT * i) + letter_surface_top_left[1]
            print('x', block.x, 'y', block.y)

    def _make_T(self):
        incrementer = 0
        letter_surface_rect_pos = self.letter_surface.get_rect()

        for block in range(4):
            new_block = Block(LIGHT_PINK_BLOCK)
            self.blocks.append(new_block)

            if block == 0:
                self.letter_surface.blit(
                    new_block.image, (15, 0))
            if block == 1:
                self.letter_surface.blit(
                    new_block.image, (15, 15)
                )
            if block == 2:
                self.letter_surface.blit(
                    new_block.image, (0, 15)
                )
            if block == 3:
                self.letter_surface.blit(
                    new_block.image, (30, 15)
                )
