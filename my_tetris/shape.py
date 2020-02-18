import pygame
import time
from block import Block
from utilities import GRID_SIDE_LEFT, GRID_SIDE_RIGHT, GRID_SIDE_BOTTOM, FALL_SPEED, V_SPEED, H_SPEED, SPACE_BAR, LEFT, RIGHT, DOWN


class Shape(pygame.sprite.Sprite):
    def __init__(self, letter):
        self.blocks = None
        letter_surface = pygame.Surface((15, 60), pygame.SRCALPHA, 32)
        self.letter_surface = letter_surface.convert_alpha()
        self.last_location = self.letter_surface.get_rect()
        self.x_pos = 200
        self.y_pos = 50
        self.rect = pygame.Rect(self.x_pos, self.y_pos, 60, 60)

        if letter == 'I':
            self.blocks = self._make_I()
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
        self.rect = pygame.Rect(self.x_pos, self.y_pos, 15, 60)

        if key == SPACE_BAR:
            new_surface = pygame.transform.rotate(
                self.letter_surface, 90)
            if new_surface.get_rect().colliderect(GRID_SIDE_LEFT):
                print('left 2', self.rect.x, self.rect.y)
            if new_surface.get_rect().colliderect(GRID_SIDE_RIGHT):
                print('right 2', self.rect.x, self.rect.y)
            if new_surface.get_rect().colliderect(GRID_SIDE_BOTTOM):
                print('bottom 2', self.rect.x, self.rect.y)
            self.letter_surface = new_surface
        elif key == LEFT:
            hitbox = self.rect.inflate(-H_SPEED, 10)
            if hitbox.colliderect(GRID_SIDE_LEFT) != True:
                self.x_pos -= H_SPEED
                self.update_blocks(x=self.x_pos)
        elif key == RIGHT:
            if x + H_SPEED < 400:
                self.x_pos += H_SPEED
                self.update_blocks(x=self.x_pos)
        elif key == DOWN:
            if y + V_SPEED < 600:
                self.y_pos += V_SPEED
                self.update_blocks(y=self.y_pos)
        # if self.rect.inflate(H_SPEED, 0).colliderect(GRID_SIDE_LEFT):
        #     print('left', self.rect.x, self.rect.y)
        # if self.rect.colliderect(GRID_SIDE_RIGHT):
        #     print('right', self.rect.x, self.rect.y)
        # if self.rect.colliderect(GRID_SIDE_BOTTOM):
        #     print('bottom', self.rect.x, self.rect.y)

# left - check top head, side head
# bottom - check top butt, side butt
# right - check top butt, side butt

    def update_blocks(self, x=0, y=0):
        incrementer = 0
        if x:
            for block in self.blocks:
                block.x = x + incrementer
                incrementer += 10
        elif y:
            for block in self.blocks:
                block.y = (y + incrementer)
                incrementer += 15

    def _make_I(self):
        block_list = []
        incrementer = 0
        letter_surface_rect_top = self.letter_surface.get_rect().top

        for block in range(4):
            new_block = Block()
            new_block.x = self.x_pos
            new_block.y = self.y_pos + incrementer
            block_list.append(new_block)
            self.letter_surface.blit(
                new_block.image, (0, letter_surface_rect_top + incrementer))
            incrementer += 15

        return block_list
