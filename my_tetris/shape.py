import pygame
import time
import copy
from block import Block
from utilities import WHITE_BLOCK, GRID_UNIT, FALL_SPEED, V_SPEED, H_SPEED, SPACE_BAR, LEFT, RIGHT, DOWN


class Shape(pygame.sprite.Sprite):
    def __init__(self):
        self.blocks = []
        letter_surface = pygame.Surface((15, 60), pygame.SRCALPHA, 32)
        self.letter_surface = letter_surface.convert_alpha( )
        self.last_location = self.letter_surface.get_rect()
        self.x_pos = 195
        self.y_pos = 60
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
            new_rect = pygame.Rect((self.x_pos + -H_SPEED, self.y_pos), width_and_height)
            print('nu left', new_rect.x, new_rect.y)
            if not self.collision_detection(matrix, -H_SPEED, width_and_height):
                self.x_pos += -H_SPEED
                self.update_blocks(width_and_height)
        elif key == RIGHT:
            new_rect = pygame.Rect((self.x_pos + H_SPEED, self.y_pos), width_and_height)
            print('nuuu right', new_rect.x, new_rect.y)
            if not self.collision_detection(matrix, H_SPEED, width_and_height):
                self.x_pos += H_SPEED
                self.update_blocks(width_and_height)

        elif key == DOWN:
            if y + V_SPEED <= 580:
                self.y_pos += V_SPEED
                self.update_blocks(width_and_height)

    def future_locations(self, blocks, direction, width_and_height):
        updated_surface_rect = pygame.Rect((self.x_pos + direction, self.y_pos), width_and_height)
        letter_surface_top_left = updated_surface_rect.topleft
        for i, block in enumerate(blocks):
            if self.angle == 0:
                block.y = (i * GRID_UNIT) + letter_surface_top_left[1]
                block.x = letter_surface_top_left[0]
            else:
                block.x = (i * GRID_UNIT) + letter_surface_top_left[0]
                block.y = letter_surface_top_left[1]
            block.rect = pygame.Rect(
                (block.x, block.y), (GRID_UNIT, GRID_UNIT))
        
        return blocks

    def collision_detection(self, matrix, direction, width_and_height):
        new_locations = self.future_locations(self.blocks.copy(), direction, width_and_height)
        for i, row in enumerate(matrix):
            for j, column in enumerate(row):

                curr_rect = matrix[i][j]
                hitbox = curr_rect['grid_square']
                for i, block in enumerate(new_locations):
    
                    if hitbox.colliderect(block.rect) and curr_rect['has_block']:
                        print(i, 'block rect', block.rect,  'hitbox',hitbox)
                        return True

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
        letter_surface_rect_top = self.rect.topleft
        print('make top left', letter_surface_rect_top)

        for block in range(4):
            new_block = Block(WHITE_BLOCK)
            new_block.x = self.x_pos
            new_block.y = self.y_pos + incrementer
            self.blocks.append(new_block)

            self.letter_surface.blit(
                new_block.image, (0, incrementer))
            incrementer += 15
