import pygame
from block import Block


class Shape(pygame.sprite.Sprite):
    def __init__(self, letter):
        pygame.sprite.Sprite.__init__(self)
        self.speeds = [10, 20, 30]
        self.blocks = None
        self.location = (100,200)
        self.rotate_point = None
        # self.hsp = 0
        # self.vsp = 0
        # self.forceVerticalSpeedInterval = 10
        # self.h_speed = 10
        # self.v_speed = 5
        # self.angle_state = None
        # self.h_pos = None
        # self.v_pos = None

        if letter == 'I':
            self.blocks = self._make_I()

        # keys = pygame.key.get_pressed()
        # millisecs = pygame.time.get_ticks()

        # if self.forceVerticalSpeedInterval:
        #     self.vsp = 20

        # if millisecs % 500 == 0:
        #    if not keys[pygame.K_LEFT] and keys[pygame.K_RIGHT]:
        #     if keys[pygame.K_LEFT]:
        #         self.hsp = -self.h_speed
        #     else:
        #         self.hsp = self.h_speed

        #     if keys[pygame.K_DOWN]:
        #         self.vsp += self.v_speed
            # move()
            # hpos += hsp
            # vpos += vsp
            # vsp, hsp = 0;
    def flip_shape(self):
       all_sprites = self.blocks
       new_sprites = []
       for i, sprite in enumerate(all_sprites):
           pygame.transform.rotate(sprite.image, 180)
           new_sprites.append(sprite)

    def _make_I(self):
        block_list = []
        incrementer = 0
        for block in range(4):
            new_block = Block(location=(200, 100 + incrementer)
            if block == 1
            block_list.append()
            incrementer += 20

        return pygame.sprite.Group(block_list)
