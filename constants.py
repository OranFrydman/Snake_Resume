import pygame

WINDOW_WIDTH = 720
WINDOW_HEIGHT = 480
SCREEN = pygame.display.set_mode((WINDOW_WIDTH, WINDOW_HEIGHT))
# Difficulty settings
# Easy      ->  10
# Medium    ->  25
# Hard      ->  40
# Harder    ->  60
# Impossible->  120

difficulty = 25

black = pygame.Color(0, 0, 0)
white = pygame.Color(255, 255, 255)
red = pygame.Color(255, 0, 0)
green = pygame.Color(0, 255, 0)
blue = pygame.Color(0, 0, 255)

# images Paths
IMG_SIZE = 30
BLUE_EDU_IMG = 'Images/BlueEdu.png'
ROCK_IMG = 'Images/RockClimb.png'
WORK_IMG = 'Images/Work.png'
GLOBE_IMG = 'Images/Globe.png'
INDEX_IMG = 5
BACKGROUND = pygame.image.load('Images/background.jpg')
BACKGROUND = pygame.transform.scale(BACKGROUND, (WINDOW_WIDTH, WINDOW_HEIGHT))

TEXT_POST_FONT_SIZE=25
LINE_MAX_LENGTH= 25
LINE_SPACE = 15