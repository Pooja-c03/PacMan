import pygame
import sys
import random
import math

pygame.init()

BLUE = (0, 0, 255)
BLACK = (0, 0, 0)
RED = (255, 0 ,0)
YELLOW = (255, 255, 0)
ORANGE = (255, 165, 0)
CYAN = (0, 255, 255)
WHITE = (255, 255, 255)
PINK = (255, 192, 203)

screen_width = 600
screen_height = 650
cell_size = 40

grid_width = 15
grid_height = 15


play = 0
game_over = 1

game_state = play 

screen = pygame.display.set_mode((screen_width, screen_height))
pygame.display.set_caption("Pac-Man")

font = pygame.font.Font(None, 36)

pacman = {'x':1, 'y':1, 'direction':3, 'mouth_open':False}

ghosts =[
    {'x':1, 'y':13, 'color':RED},
    {'x':13, 'y':1, 'color':PINK},
    {'x':13, 'y':13, 'color':CYAN},
    {'x':11, 'y':11, 'color':ORANGE},
]

score = 0

clock = pygame.tme.Clock()
running = True

pacman_move_delay = 150
ghost_move_delay = 300
mouth_delay = 600
last_pacman_move = 0
last_ghost_move = 0
last_mouth_time = 0