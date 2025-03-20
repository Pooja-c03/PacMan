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

def draw_pacman():
    x = pacman['x'] * cell_size + cell_size // 2
    y = pacman['y'] * cell_size + cell_size // 2 + 50

    mouth_opening = 45 if pacman['mouth_open'] else 0

    pygame.draw.circle(screen, YELLOW, (x, y), cell_size // 2)


    if pacman['direction'] == 0:
        start_angle = 360 - mouth_opening / 2
        end_angle = mouth_opening / 2
    elif pacman['direction'] == 3:
        start_angle = 90 - mouth_opening / 2
        end_angle = 90 + mouth_opening / 2
    elif pacman['direction'] == 2:
        start_angle = 180 - mouth_opening / 2
        end_angle = 180 + mouth_opening / 2
    else:
        start_angle = 270 - mouth_opening / 2
        end_angle = 270 + mouth_opening / 2
        
    pygame.draw.arc(screen, BLACK,
                (x - cell_size // 2, y - cell_size // 2, cell_size, cell_size),
                math.radians(start_angle), math.radians(end_angle), cell_size // 2)
    
    mouth_line_end_x = x + math.cos(math.radians(start_angle)) * cell_size // 2
    mouth_line_end_y = y - math.sin(math.radians(start_angle)) * cell_size // 2
    pygame.draw.line(screen, BLACK, (x, y), (mouth_line_end_x, mouth_line_end_y), 2)

    mouth_line_end_x = x + math.cos(math.radians(end_angle)) * cell_size // 2
    mouth_line_end_y = y - math.sin(math.radians(end_angle)) * cell_size // 2
    pygame.draw.line(screen, BLACK, (x, y), (mouth_line_end_x, mouth_line_end_y), 2)

def draw_ghost(ghost):
    x = ghost['x'] * cell_size + cell_size // 2
    y = ghost['y'] * cell_size + cell_size // 2 + 50
    pygame.draw.circle(screen, ghost['color'], (x, y), cell_size // 2)