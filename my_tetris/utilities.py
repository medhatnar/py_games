import os
import pygame

# constants
grid_unit = 20

base_width = 600
base_height = 600

v_speed = 20
h_speed = 20

black = 0, 0, 0
white = 255, 255, 255

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
