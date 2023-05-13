import pygame
from constants import *
class Button:
    """
    A class used to represent an Button on the screen
    """
    def __init__(self,image_src, x, y):
        """
        Constructor

        :param x_pos: int
            Position of the top left corner of the button in X axis
        :param y_pos: int
            Position of the top left corner of the button in Y axis
        :param width: int
            Width of button in pixels
        :param height: int
            Height of button in pixels
        """
        img = pygame.image.load(image_src)
        img = pygame.transform.scale(img, (WINDOW_WIDTH/6, WINDOW_HEIGHT/6))
        self.img = img
        self.image_rect = img.get_rect()

        self.width = self.image_rect.width
        self.height = self.image_rect.height
        self.image_rect.x = x - self.width/2
        self.image_rect.y = y

    def blit(self):
        SCREEN.blit(self.img, (self.image_rect.x,self.image_rect.y))


    def mouse_in_button(self, mouse_pos):
        """
        The function get button and mouse press position on screen and return True
        if mouse click on button
        :param button: Button object
            button on screen
        :param mouse_pos: tuple
            the x and y position of the mouse cursor
        :return: boolean
            True if mouse click on button, else False
        """
        if self.image_rect.x + self.width > mouse_pos[0] > self.image_rect.x and \
                self.image_rect.y < mouse_pos[1] < self.image_rect.y + self.height:
            return True