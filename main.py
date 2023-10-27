import pygame
import math
from mazes import small_maze

pygame.init()

TILE_SIZE = 64
WIDTH = TILE_SIZE * 10
HEIGHT = TILE_SIZE * 8
screen = pygame.display.set_mode([WIDTH, HEIGHT])
timer = pygame.time.Clock()
FPS = 30
font = pygame.font.Font('HalloweenSlimePersonalUse-4B80D.otf', 20)
level = small_maze
player = pygame.Rect(64, 64, 64, 64)

tiles = [pygame.image.load('blank.png'), pygame.image.load('wall.png'), pygame.image.load('goal.png')]

direction = pygame.key.get_pressed()


def draw_maze():
    for row in range(len(small_maze)):
        for column in range(len(small_maze[row])):
            x = column * TILE_SIZE
            y = row * TILE_SIZE
            tile = tiles[small_maze[row][column]]
            screen.blit(tile, (x, y))


def draw_player():
    pygame.draw.rect(screen, 'white', player)


def move_player():
    if direction[pygame.K_UP]:
        player.move_ip(0, -64)
    if direction[pygame.K_DOWN]:
        player.move_ip(0, 64)
    if direction[pygame.K_LEFT]:
        player.move_ip(-64, 0)
    if direction[pygame.K_RIGHT]:
        player.move_ip(64, 0)


run = True
while run:
    timer.tick(FPS)
    screen.fill('black')
    draw_maze()
    draw_player()
    direction = pygame.key.get_pressed()
    move_player()

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            run = False

    pygame.display.flip()
pygame.quit()
