import pygame
from constants import *
class Info:
    def __init__(self, image_src, type,text,x,y):
        img = pygame.image.load(image_src)
        img = pygame.transform.scale(img, (WINDOW_WIDTH/6, WINDOW_HEIGHT/6))
        self.img = img
        self.image_rect = img.get_rect()
        self.image_rect.x = x
        self.image_rect.y = y
        self.type = type
        self.text_array = self.from_text_to_array(text) #array of text
        self.text_color = black

    def from_text_to_array(self,text):
        """
        the function get text and break it into sentences that fits the screen, in
        case the text too long to for one line
        :param text: string
            text to show on screen
        :return: list of sentences
        """
        text_array = []
        text_to_edit = text
        if len(text) > 20:
            while not (len(text_to_edit) <= 0):
                if len(text_to_edit) < LINE_MAX_LENGTH:
                    text_array.append(text_to_edit)
                    text_to_edit = ""
                else:
                    temp = text_to_edit[0: LINE_MAX_LENGTH]
                    text_to_edit = text_to_edit[LINE_MAX_LENGTH:]
                    while not (temp[-1] == ' ') and not (temp[-1] == ','):
                        text_to_edit = temp[-1] + text_to_edit
                        temp_len = int(len(temp))
                        temp = temp[0: temp_len - 1]
                    text_array.append(temp)
        else:
            text_array.append(text)
        return text_array


    def display_content(self):
        """
        Display background and text on screen

        :return:None
        """
        # pygame.draw.rect(SCREEN, self.background_color,
        #                  pygame.Rect(POST_X_POS,
        #                              POST_Y_POS,
        #                              POST_WIDTH,
        #                              POST_HEIGHT))
        for i in range(0, len(self.text_array)):
            text_font = pygame.font.SysFont('chalkduster.ttf',
                                            TEXT_POST_FONT_SIZE, bold=False)
            text_to_display = text_font.render(self.text_array[i],
                                               True, self.text_color)
            text_pos = [self.image_rect.x-10 ,self.image_rect.y+i*LINE_SPACE+self.image_rect.height+10]
            SCREEN.blit(text_to_display, text_pos)
    def show_img(self):
        SCREEN.blit(self.img, (self.image_rect.x,self.image_rect.y))
    def blit_info(self):
        self.show_img()
        self.display_content()






