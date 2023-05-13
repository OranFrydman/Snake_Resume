"""
Snake Eater
Made with PyGame
"""

import pygame, sys, time, random

from collectable import Collectable
from constants import *
from info import Info
from Button import Button

# Window size


# Checks for errors encountered
check_errors = pygame.init()
# pygame.init() example output -> (6, 0)
# second number in tuple gives number of errors
if check_errors[1] > 0:
    print(f'[!] Had {check_errors[1]} errors when initialising game, exiting...')
    sys.exit(-1)
else:
    print('[+] Game successfully initialised')

# Initialise game window
pygame.display.set_caption('Oran Frydman Resume - Snake')
game_window = SCREEN

# FPS (frames per second) controller
fps_controller = pygame.time.Clock()

# Game variables
snake_pos = [100, 50]
snake_body = [[100, 50], [100 - 10, 50], [100 - (2 * 10), 50]]

food_pos = [random.randrange(1, (WINDOW_WIDTH // 10)) * 10, random.randrange(1, (WINDOW_HEIGHT // 10)) * 10]
food_spawn = True
index = random.randrange(1, INDEX_IMG)
collect_object = Collectable(index)
direction = 'RIGHT'
change_to = direction
score = 0
#objects declarations:
jobs1 = Info('Images/BTG2.png',"job","Process Automation Supply Chain 2020-2022 ",40,50)
jobs2 = Info('Images/Nitzanim.jpg',"job","Python Instructor 2023",265,50)
jobs3 = Info('Images/BGU.png',"job","ERP course assistant 2023 ",470,50)
jobs4 = Info('Images/Collplant.jpg',"job","Lab assistant 2013 ",40,200)
jobs5 = Info('Images/Givaty.png',"job","Commander - Sergeant 2014-2017",265,200)
jobs6 = Info('Images/iClimbg.png',"job","Climbing instructor 2018",470,200)

jobs = [jobs1,jobs2,jobs3,jobs4,jobs5,jobs6]

# Game Over
def game_over():
    pass
    # my_font = pygame.font.SysFont('times new roman', 90)
    # game_over_surface = my_font.render('YOU DIED', True, red)
    # game_over_rect = game_over_surface.get_rect()
    # game_over_rect.midtop = (WINDOW_WIDTH / 2, WINDOW_HEIGHT / 4)
    # game_window.fill(black)
    # game_window.blit(game_over_surface, game_over_rect)
    # show_score(0, red, 'times', 20)
    # pygame.display.flip()
    # time.sleep(3)
    # pygame.quit()
    # sys.exit()

def init_header(text):
    font = pygame.font.Font(None, 36)
    header = font.render(text, True, black)
    text_rect = header.get_rect()
    text_rect.center = (WINDOW_WIDTH // 2, 50)
    header_and_rect = [header,text_rect]
    return header_and_rect
def show_info(collision_type):

    back_button = Button("Images/Back.jpg",WINDOW_WIDTH/2,WINDOW_HEIGHT*0.8)
    flag= True
    while flag:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()
            if event.type == pygame.MOUSEBUTTONDOWN:
                # Get the position (x,y) of the mouse press
                pos = event.pos
                if back_button.mouse_in_button(pos):
                    flag= False
        SCREEN.fill(white)
        if collision_type == 1:
            header_n_rect = init_header("Education")
        if collision_type==2:
            header_n_rect = init_header("Work Experience")
            for j in jobs:
                j.blit_info()
        if collision_type == 3:
            header_n_rect = init_header("Hobbies")
        if collision_type == 4:
            header_n_rect = init_header("About me")
        SCREEN.blit(header_n_rect[0], header_n_rect[1])
        back_button.blit()
        pygame.display.update()
# Score
def show_score(choice, color, font, size):
    score_font = pygame.font.SysFont(font, size)
    score_surface = score_font.render('Score : ' + str(score), True, color)
    score_rect = score_surface.get_rect()
    if choice == 1:
        score_rect.midtop = (WINDOW_WIDTH / 10, 15)
    else:
        score_rect.midtop = (WINDOW_WIDTH / 2, WINDOW_HEIGHT / 1.25)
    game_window.blit(score_surface, score_rect)
    # pygame.display.flip()


# Main logic
while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()
        # Whenever a key is pressed down
        elif event.type == pygame.KEYDOWN:
            # W -> Up; S -> Down; A -> Left; D -> Right
            if event.key == pygame.K_UP or event.key == ord('w'):
                change_to = 'UP'
            if event.key == pygame.K_DOWN or event.key == ord('s'):
                change_to = 'DOWN'
            if event.key == pygame.K_LEFT or event.key == ord('a'):
                change_to = 'LEFT'
            if event.key == pygame.K_RIGHT or event.key == ord('d'):
                change_to = 'RIGHT'
            # Esc -> Create event to quit the game
            if event.key == pygame.K_ESCAPE:
                pygame.event.post(pygame.event.Event(pygame.QUIT))

    # Making sure the snake cannot move in the opposite direction instantaneously
    if change_to == 'UP' and direction != 'DOWN':
        direction = 'UP'
    if change_to == 'DOWN' and direction != 'UP':
        direction = 'DOWN'
    if change_to == 'LEFT' and direction != 'RIGHT':
        direction = 'LEFT'
    if change_to == 'RIGHT' and direction != 'LEFT':
        direction = 'RIGHT'

    # Moving the snake
    if direction == 'UP':
        snake_pos[1] -= 10
    if direction == 'DOWN':
        snake_pos[1] += 10
    if direction == 'LEFT':
        snake_pos[0] -= 10
    if direction == 'RIGHT':
        snake_pos[0] += 10

    # Snake body growing mechanism
    snake_body.insert(0, list(snake_pos))
    collision_type = collect_object.bump(snake_pos)
    if collision_type>0:  ##collision
        show_info(collision_type)
        score += 1
        collect_object.OnScreen = False
        food_spawn = False
        index = random.randrange(1, INDEX_IMG)
        collect_object = Collectable(index)
    else:
        snake_body.pop()

    # Spawning food on the screen
    if not collect_object.OnScreen:
        collect_object.run_new_collectable()
    #     food_pos = [random.randrange(1, (WINDOW_WIDTH // 10)) * 10, random.randrange(1, (WINDOW_HEIGHT // 10)) * 10]
    # food_spawn = True
    collect_object.OnScreen = True

    # GFX
    game_window.blit(BACKGROUND, (0, 0))
    for pos in snake_body:
        # Snake body
        # .draw.rect(play_surface, color, xy-coordinate)
        # xy-coordinate -> .Rect(x, y, size_x, size_y)
        pygame.draw.rect(game_window, black, pygame.Rect(pos[0], pos[1], 10, 10))

    # Snake food

    collect_object.blit()
    # pygame.draw.rect(game_window, white, pygame.Rect(food_pos[0], food_pos[1], 10, 10))

    # Game Over conditions
    # Getting out of bounds
    if snake_pos[0] < 0 or snake_pos[0] > WINDOW_WIDTH - 10:
        snake_pos = [100, 50]
        snake_body = [[100, 50], [100 - 10, 50], [100 - (2 * 10), 50]]
        score = 0
        game_over()
    if snake_pos[1] < 0 or snake_pos[1] > WINDOW_HEIGHT - 10:
        snake_pos = [100, 50]
        snake_body = [[100, 50], [100 - 10, 50], [100 - (2 * 10), 50]]
        score = 0
        game_over()
    # Touching the snake body
    for block in snake_body[1:]:
        if snake_pos[0] == block[0] and snake_pos[1] == block[1]:
            snake_pos = [100, 50]
            snake_body = [[100, 50], [100 - 10, 50], [100 - (2 * 10), 50]]
            score = 0
            game_over()

    show_score(1, black, 'consolas', 20)
    # Refresh game screen
    pygame.display.update()
    # Refresh rate
    fps_controller.tick(difficulty)


