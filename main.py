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

grid = [
    [1,1,1,1,1,1,1,1,1,1,1,1,1,1,1],
    [1,0,0,0,0,0,0,1,0,0,0,0,0,0,1],
    [1,0,1,1,0,1,0,1,0,1,0,1,1,0,1],
    [1,0,0,0,0,0,0,0,0,0,0,0,0,0,1],
    [1,0,1,1,0,1,1,1,1,1,0,1,1,0,1],
    [1,0,0,0,0,0,0,1,0,0,0,0,0,0,1],
    [1,1,1,1,0,1,0,1,0,1,0,1,1,1,1],
    [1,1,1,1,0,1,0,0,0,1,0,1,1,1,1],
    [1,1,1,1,0,1,0,1,0,1,0,1,1,1,1],
    [1,0,0,0,0,0,0,1,0,0,0,0,0,0,1],
    [1,0,1,1,0,1,1,1,1,1,0,1,1,0,1],
    [1,0,0,0,0,0,0,0,0,0,0,0,0,0,1],
    [1,0,1,1,0,1,0,1,0,1,0,1,1,0,1],
    [1,0,0,0,0,0,0,1,0,0,0,0,0,0,1],
    [1,1,1,1,1,1,1,1,1,1,1,1,1,1,1]
]

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

def move_pacman():
    global score
    dx, dy =[(1,0),(0,1),(-1,0),(0,-1)][pacman['direction']]
    new_x, new_y = pacman['x']+dx, pacman['y']+dy
    if grid[new_x][new_y]!=1:
        pacman['x'],pacman['y'] = new_x, new_y
        if grid[new_y][new_x]==0:
            grid[new_y][new_x] = 2
            score += 10

def move_ghost(ghost):
    directions = [(1,0),(0,1),(-1,0),(0,-1)]
    random.shuffle(directions)
    for dx, dy in directions:
        new_x, new_y = ghost['x']+dx, ghost['y']+dy
        if 0 <= new_x < grid_width and 0 <= new_y < grid_height and grid[new_x][new_y] != 1:
            ghost['x'], ghost['y'] = new_x, new_y
            break