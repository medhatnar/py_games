import os
import time
import pygame

# Constants

# sizes
GRID_UNIT = 20
BASE_WIDTH = 600
BASE_HEIGHT = 600
# SPEEDS
V_SPEED = 20
H_SPEED = 10
# TIME
WAIT_TIME = -0.05
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
    print(time_now - begin, WAIT_TIME)
    return time_now - begin > WAIT_TIME
