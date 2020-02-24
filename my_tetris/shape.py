import pygame
import time
import copy
from block import Block
from utilities import WHITE_BLOCK, GRID_UNIT, FALL_SPEED, V_SPEED, H_SPEED, SPACE_BAR, LEFT, RIGHT, DOWN


class Shape(pygame.sprite.Sprite):
    def __init__(self):
        self.blocks = []
        letter_surface = pygame.Surface((15, 60), pygame.SRCALPHA, 32)
        self.letter_surface = letter_surface.convert_alpha()
        self.last_location = self.letter_surface.get_rect()
        self.x_pos = 195
        self.y_pos = 15
        self.angle = 0
        self.rect = pygame.Rect(self.x_pos, self.y_pos, 15, 60)
        self._make_I()
        self.sprite_group = pygame.sprite.Group(self.blocks)

    def fall(self):
        self.last_location = self.letter_surface.get_rect()
        if self.y_pos + FALL_SPEED < 585:
            self.y_pos += FALL_SPEED
            self.update_blocks(y=self.y_pos)

    def update(self, key, matrix):
        x = self.x_pos
        y = self.y_pos
        self.last_location = self.letter_surface.get_rect()
        width_and_height = (15, 60) if self.angle == 0 else (60, 15)

        if key == SPACE_BAR:
            new_surface = pygame.transform.rotate(
                self.letter_surface, 90)
            self.letter_surface = new_surface
            if self.angle == 0:
                self.angle = 1
            else:
                self.angle = 0
            self.update_blocks(width_and_height)
        elif key == LEFT:
            if not self.collision_detection(matrix, -H_SPEED, width_and_height):
                self.x_pos += -H_SPEED
                self.update_blocks(width_and_height)
        elif key == RIGHT:
            if not self.collision_detection(matrix, H_SPEED, width_and_height):
                self.x_pos += H_SPEED
                self.update_blocks(width_and_height)
        elif key == DOWN:
            if not self.collision_detection(matrix, V_SPEED, width_and_height):
                self.y_pos += V_SPEED
                self.update_blocks(width_and_height)

    def future_locations(self, blocks, direction, width_and_height):
        if direction == H_SPEED or direction == -H_SPEED:
            updated_surface_rect = pygame.Rect(
                (self.x_pos + direction, self.y_pos), width_and_height)
            letter_surface_top_left = updated_surface_rect.topleft

            for i, block in enumerate(blocks):
                if self.angle == 0:
                    block.y = (i * direction) + letter_surface_top_left[1]
                    block.x = letter_surface_top_left[0]
                else:
                    block.x = (i * direction) + letter_surface_top_left[0]
                    block.y = letter_surface_top_left[1]
                block.rect = pygame.Rect(
                    (block.x, block.y), (GRID_UNIT, GRID_UNIT))
        return blocks

    def collision_detection(self, matrix, direction, width_and_height):
        t = [matrix[6][16], matrix[7][16], matrix[7][15], matrix[7][17]]
        new_locations = self.future_locations(
            self.blocks.copy(), direction, width_and_height)

        for block in new_locations:
            for curr in t:
                if(block.x < curr['grid_square'].x + curr['grid_square'].width and block.x + block.width > curr['grid_square'].x and block.y < curr['grid_square'].y + curr['grid_square'].height and block.y + block.height > curr['grid_square'].y):
                    print('(block1 x axis)', block.x, '< (block2 combined x axis and width)', curr['grid_square'].x + curr['grid_square'].width)
                    print('----')
                    print('and vice versa: ', block.x + block.width, '>', curr['grid_square'].x)
                    print('======================================================================')
                    print('(block1 y axis)', block.y, '< (block2 combined y axis and height)', curr['grid_square'].y + curr['grid_square'].height)
                    print('----')
                    print('and vice versa', block.y + block.height, ' > ', curr['grid_square'].y)
                    return True
                else:
                    print('block1 x axis:', block.x, 'is less than combined block2 x axis:', curr['grid_square'].x, 'and block2 width:', curr['grid_square'].width)
                    print('----')
                    print('block1 x axis:', block.x, 'is greater than combined block1 width:', block.width, 'and block2 x axis:',curr['grid_square'].x)
                    print('======================================================================')
                    print('block1 y axis:', block.y, 'is less than block2 y axis:',curr['grid_square'].y, 'and block2 height:', curr['grid_square'].height)
                    print('----')
                    print('block1 y axis:', block.y, 'is greter than block1 height:', block.height, 'and block2 y axis:', curr['grid_square'].y)
                    print('======================================================================')

        return False

    def update_blocks(self, width_and_height):
        rect = pygame.Rect((self.x_pos, self.y_pos), width_and_height)
        letter_surface_top_left = rect.topleft
        for i, block in enumerate(self.blocks):
            if self.angle == 0:
                block.y = (i * GRID_UNIT) + letter_surface_top_left[1]
                block.x = letter_surface_top_left[0]
            else:
                block.x = (i * GRID_UNIT) + letter_surface_top_left[0]
                block.y = letter_surface_top_left[1]
            block.rect = pygame.Rect(
                (block.x, block.y), (GRID_UNIT, GRID_UNIT))

    def _make_I(self):
        incrementer = 0

        for block in range(4):
            new_block = Block(WHITE_BLOCK)
            new_block.x = self.x_pos
            new_block.y = self.y_pos + incrementer
            self.blocks.append(new_block)

            self.letter_surface.blit(
                new_block.image, (0, incrementer))
            incrementer += 15
