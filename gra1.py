import pygame
import sys
from pygame.locals import *  # udostępnienie nazw metod z locals
import matplotlib.pyplot as plt
import numpy as np
import math
import pandas as pd
import time
import random


snake_speed = 15
# Window size
window_x = 720
window_y = 480
# defining colors
black = pygame.Color(0, 0, 0)
white = pygame.Color(255, 255, 255)
red = pygame.Color(255, 0, 0)
green = pygame.Color(0, 255, 0)
blue = pygame.Color(0, 0, 255)

# inicjacja modułu pygame
pygame.init()

# przygotowanie powierzchni do rysowania, czyli inicjacja okna gry
#OKNOGRY = pygame.display.set_mode((300, 300), 0, 32)
# tytuł okna gry
#pygame.display.set_caption('Projekt 1')

# Initialise game window
pygame.display.set_caption('GeeksforGeeks Snakes')
game_window = pygame.display.set_mode((window_x, window_y))

# FPS (frames per second) controller
fps = pygame.time.Clock()
# defining snake default position
snake_position = [100, 50]
# defining first 4 blocks of snake body
snake_body = [[100, 50],
[90, 50],
[80, 50],
[70, 50]
]
# fruit position
fruit_position = [random.randrange(1, (window_x//10)) * 10,
random.randrange(1, (window_y//10)) * 10]
fruit_spawn = True
# setting default snake direction towards
# right
direction = 'RIGHT'
change_to = direction
# initial score
score = 0
# displaying Score function
def show_score(choice, color, font, size):
    # creating font object score_font
    score_font = pygame.font.SysFont(font, size)
    # create the display surface object
    # score_surface
    score_surface = score_font.render('Score : ' + str(score), True, color)
    # create a rectangular object for the text
    # surface object
    score_rect = score_surface.get_rect()
    # displaying text
    game_window.blit(score_surface, score_rect)

# game over function
def game_over():
    # creating font object my_font
    my_font = pygame.font.SysFont('times new roman', 50)
    # creating a text surface on which text
    # will be drawn
    game_over_surface = my_font.render(
    'Your Score is : ' + str(score), True, red)
    # create a rectangular object for the text
    # surface object
    game_over_rect = game_over_surface.get_rect()
    # setting position of the text
    game_over_rect.midtop = (window_x/2, window_y/4)
    # blit will draw the text on screen
    game_window.blit(game_over_surface, game_over_rect)
    pygame.display.flip()
    # after 2 seconds we will quit the program
    time.sleep(2)
    # deactivating pygame library
    pygame.quit()
    # quit the program
    quit()



#tytul przycisku Inicjaly1
pygame.draw.rect(game_window, (0, 0, 255), [0, 0, 720, 45], 2)
fontButtons =  pygame.font.Font('freesansbold.ttf', 20)
textComputer = u'Inicjaly'
tekst_obr_ButtonComp = fontButtons.render(textComputer, True, (20, 255, 20))
tekst_prost_ButtonComp = tekst_obr_ButtonComp.get_rect()
tekst_prost_ButtonComp.center = (360, 30)
game_window.blit(tekst_obr_ButtonComp, tekst_prost_ButtonComp)

#tytul przycisku Bezier
pygame.draw.rect(game_window, (0, 0, 255), [0, 45, 720, 45], 2)
textComputer = u'Bezier'
tekst_obr_ButtonUser = fontButtons.render(textComputer, True, (20, 255, 20))
tekst_prost_ButtonUser = tekst_obr_ButtonUser.get_rect()
tekst_prost_ButtonUser.center = (360, 70)
game_window.blit(tekst_obr_ButtonUser, tekst_prost_ButtonUser)

#tytul przycisku Gra
pygame.draw.rect(game_window, (0, 0, 255), [0, 90, 720, 45], 2)
textComputer = u'Gra'
tekst_obr_ButtonUser = fontButtons.render(textComputer, True, (20, 255, 20))
tekst_prost_ButtonUser = tekst_obr_ButtonUser.get_rect()
tekst_prost_ButtonUser.center = (360, 110)
game_window.blit(tekst_obr_ButtonUser, tekst_prost_ButtonUser)

def bezier(x, y, nr):
    xs = (x * 0.0005 for x in range(0, 2001))
    xarray = []
    yarray = []
    for t in xs:
        xt = pow(1 - t, 3) * x[0] + 3 * t * pow(1 - t, 2) * x[1] + 3 * pow(t, 2) * (1 - t) * x[2] + pow(t, 3) * x[3]
        yt = pow(1 - t, 3) * y[0] + 3 * t * pow(1 - t, 2) * y[1] + 3 * pow(t, 2) * (1 - t) * y[2] + pow(t, 3) * y[3]
        xarray.append(xt)
        yarray.append(yt)

    plt.subplot(nr)
    plt.plot(xarray, yarray)

def FunkcjaN(wzor_i, k):
    if k == 0 or k == wzor_i:
        return 1
    else:
        return FunkcjaN(wzor_i-1, k-1) + FunkcjaN(wzor_i-1, k)

def Licz_Silnie_Bezier(wzor_o,wzor_p,v):
    return math.pow(v,wzor_p) * math.pow(1-v,wzor_o-wzor_p) * FunkcjaN(wzor_o,wzor_p)

def bezierDzbanek(s1, s2):
    f1 = open(s1, "r")
    Lines = f1.readlines()
    count = 0
    f1.close()

    f2 = open(s2, 'w')
    f2.writelines("a,b,c\n")

    X2 = 0.0
    Y2 = 0.0
    Z2 = 0.0

    tab1 = Lines[count].split(" ")
    Licz_Platy = int(tab1[0])

    pkt = np.zeros((4,4,3))


    for i in range(0, Licz_Platy):
        count=count+1
        for j in range(0, 4):
            for l in range(0, 4):
                count = count + 1
                tab1 = Lines[count].split(" ")
                pkt[j,l,0] = float(tab1[0])
                pkt[j,l,1] = float(tab1[1])
                pkt[j,l,2] = float(tab1[2])
        vs = (x * 0.01 for x in range(0, 101))
        for v in vs:
            ws = (x * 0.01 for x in range(0, 101))
            for w in ws:
                for a in range(0, 4):
                    for b in range(0, 4):
                        X2 = X2+ pkt[a][b][0] * Licz_Silnie_Bezier(3, a, w) * Licz_Silnie_Bezier(3, b, v)
                        Y2 = Y2 + pkt[a][b][1] * Licz_Silnie_Bezier(3, a, w) * Licz_Silnie_Bezier(3, b, v)
                        Z2 = Z2 + pkt[a][b][2] * Licz_Silnie_Bezier(3, a, w) * Licz_Silnie_Bezier(3, b, v)

                caption = str(X2) + "," + str(Y2) + "," + str(Z2) + "\n"
                f2.writelines(caption)
                X2 = 0.0
                Y2 = 0.0
                Z2 = 0.0

    f2.close()

def bezierDzbanki():
    #bezierDzbanek("dzbanek.txt", "WspolrzedneDoModelu3D\\dzbanek_model3d.txt")
    #bezierDzbanek("filizanka.txt", "WspolrzedneDoModelu3D\\filizanka_model3d.txt")
    bezierDzbanek("lyzeczka.txt", "WspolrzedneDoModelu3D\\lyzeczka_model3d.txt")


START_GAME = False
while True:
    if START_GAME is True:
        # Main Function
        while True:
            # handling key events
            for event in pygame.event.get():
                if event.type == pygame.KEYDOWN:
                    if event.key == pygame.K_UP:
                        change_to = 'UP'
                    if event.key == pygame.K_DOWN:
                        change_to = 'DOWN'
                    if event.key == pygame.K_LEFT:
                        change_to = 'LEFT'
                    if event.key == pygame.K_RIGHT:
                        change_to = 'RIGHT'
            # If two keys pressed simultaneously
            # we don't want snake to move into two
            # directions simultaneously
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
                snake_position[1] -= 10
            if direction == 'DOWN':
                snake_position[1] += 10
            if direction == 'LEFT':
                snake_position[0] -= 10
            if direction == 'RIGHT':
                snake_position[0] += 10
            # Snake body growing mechanism
            # if fruits and snakes collide then scores
            # will be incremented by 10
            snake_body.insert(0, list(snake_position))
            if snake_position[0] == fruit_position[0] and snake_position[1] == fruit_position[1]:
                score += 10
                fruit_spawn = False
            else:
                snake_body.pop()
            if not fruit_spawn:
                fruit_position = [random.randrange(1, (window_x // 10)) * 10,
                                  random.randrange(1, (window_y // 10)) * 10]
            fruit_spawn = True
            game_window.fill(black)
            for pos in snake_body:
                pygame.draw.rect(game_window, green,
                                 pygame.Rect(pos[0], pos[1], 10, 10))
            pygame.draw.rect(game_window, white, pygame.Rect(
                fruit_position[0], fruit_position[1], 10, 10))
            # Game Over conditions
            if snake_position[0] < 0 or snake_position[0] > window_x - 10:
                game_over()
            if snake_position[1] < 0 or snake_position[1] > window_y - 10:
                game_over()
            # Touching the snake body
            for block in snake_body[1:]:
                if snake_position[0] == block[0] and snake_position[1] == block[1]:
                    game_over()
            # displaying score countinuously
            show_score(1, white, 'times new roman', 20)
            # Refresh game screen
            pygame.display.update()
            # Frame Per Second /Refresh Rate
            fps.tick(snake_speed)
    else:
        for event in pygame.event.get():
            # przechwyć zamknięcie okna
            if event.type == QUIT:
                pygame.quit()
                sys.exit()

            if event.type == MOUSEBUTTONDOWN:
                if event.button == 1:  # jeżeli naciśnięto 1. przycisk
                    mouseX, mouseY = event.pos
                    if 0 <= mouseX <= 720:
                        if 0 <= mouseY <= 45:
                            bezier([105, 157, 217, 277], [76, 488, 485, 76], 111)
                            bezier([105, 157, 217, 277], [76, 200, 200, 76], 111)
                            bezier([175, 175, 200, 200], [250, 300, 300, 250], 111)
                            bezier([175, 175, 200, 200], [250, 200, 200, 250], 111)

                            bezier([470, 145, 709, 400], [336, 337, 78, 78], 111)
                            bezier([400, 300, 268, 330], [78, 68, 130, 146], 111)
                            bezier([330, 493, 207, 330], [146, 188, 321, 362], 111)
                            bezier([330, 400, 550, 470], [362, 381, 360, 336], 111)

                            plt.show()
                        if 45 < mouseY <= 90:
                            bezierDzbanki()

                            columns = ["a", "b", "c"]
                            # msft = pd.read_csv('WspolrzedneDoModelu3D\\filizanka_model3d.txt', usecols=columns)
                            # msft = pd.read_csv('WspolrzedneDoModelu3D\\dzbanek_model3d.txt', usecols=columns)
                            msft = pd.read_csv('WspolrzedneDoModelu3D\\lyzeczka_model3d.txt', usecols=columns)

                            plt.figure().add_subplot(projection='3d')
                            # columns = list(zip(*msft))
                            # print(msft[:,0])
                            plt.plot(msft.a, msft.b, msft.c)
                            plt.show()
                        if 90 < mouseY <= 135:
                            START_GAME = True
                            TRYB_GRY = 1
    pygame.display.update()
