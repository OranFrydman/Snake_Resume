import pygame
import random
from Constants import SCREEN


class Item:
    def __init__(self, image_src, type, width, height, speed, x_pos, y_pos):
        item = pygame.image.load(image_src)
        item = pygame.transform.scale(item, (60, 60))
        self.item = item
        self.type = type
        self.width = width
        self.height = height
        self.speed = speed
        self.x_pos = x_pos
        self.y_pos = y_pos

    def blit(self):
        SCREEN.blit(self.item, (self.x_pos, self.y_pos))

    def movement(self):
        pass

    def interaction(self):
        pass
