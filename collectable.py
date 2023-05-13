import sys

import pygame
import random
from constants import *
class Collectable:
    def __init__(self, type):
        self.type = type
        self.width = IMG_SIZE
        self.height = IMG_SIZE
        image_src = self.get_image()
        item = pygame.image.load(image_src)
        item = pygame.transform.scale(item, (self.width , self.height))
        self.item = item
        self.image_rect = item.get_rect()
        self.image_rect.x = random.randrange(1, (WINDOW_WIDTH // 10)) * 9
        self.image_rect.y = random.randrange(1, (WINDOW_HEIGHT // 10)) * 9
        self.OnScreen = True
    def blit(self):
        SCREEN.blit(self.item, (self.image_rect.x,self.image_rect.y))

    def get_image(self):
        if self.type==1:
            return BLUE_EDU_IMG
        elif self.type == 2:
            return WORK_IMG
        elif self.type == 3:
            return ROCK_IMG
        elif self.type == 4:
            return GLOBE_IMG
    def bump(self,snake_pos):
        if self.image_rect.collidepoint(snake_pos[0], snake_pos[1]):
        # if snake_pos[0] >= self.x_pos and snake_pos[0] <= self.x_pos+IMG_SIZE and snake_pos[1] >= self.y_pos and snake_pos[1] <= self.y_pos+IMG_SIZE:
            return self.type
        return 0
    def run_new_collectable(self):
        self.image_rect.x = random.randrange(1, (WINDOW_WIDTH // 10)) * 10
        self.image_rect.y = random.randrange(1, (WINDOW_HEIGHT // 10)) * 10

