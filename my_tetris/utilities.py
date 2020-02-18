import os
import time
import pygame

# Constants

# SIZES
GRID_UNIT = 15
BASE_WIDTH = 600
BASE_HEIGHT = 600
GRID_SIDE_LEFT = pygame.Rect((0, 0, 10, 600)).inflate(25,0)
GRID_SIDE_RIGHT = pygame.Rect((395, 0, 10, 600)).inflate(-10,0)
GRID_SIDE_BOTTOM = pygame.Rect((0, 600, 400, 10)).inflate(0, -5)
GRID_SIDES = [GRID_SIDE_LEFT, GRID_SIDE_RIGHT, GRID_SIDE_BOTTOM]
# SPEEDS
FALL_SPEED = 10
V_SPEED = 20
H_SPEED = 10
# TIME
WAIT_TIME = -0.05
# STANCES
VERTICAL = 'vert'
SIDE = 'side'
# KEYS
SPACE_BAR = 32
LEFT = 276
RIGHT = 275
DOWN = 274
# COLORS
BLACK = 0, 0, 0
WHITE = 255, 255, 255

# Utility methods


def load_image(name, size, color_key=-1):
    ext = "jpg" if name == 'big-galaxy' else "png"
    file_path = os.path.join('assets', f"{name}.{ext}")
    try:
        image = pygame.image.load(file_path)
        image = pygame.transform.scale(image, size)
    except pygame.error as message:
        print('cannot load image', name)
        raise SystemExit(message)
    image = image.convert()
    image.set_colorkey(color_key)

    return image


def past_time(time_now):
    begin = time.time()
    return time_now - begin > WAIT_TIME
