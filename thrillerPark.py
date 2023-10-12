import pygame
import math
from mazes import small_maze

pygame.init()

WIDTH = 1000
HEIGHT = 1000
screen = pygame.display.set_mode([WIDTH, HEIGHT])
timer = pygame.time.Clock()
fps = 60
font = pygame.font.Font('HalloweenSlimePersonalUse-4B80D.otf', 20)
level = small_maze


def draw_maze(level):
    num1 = (HEIGHT // 30)
    num2 = (WIDTH // 30)
    for i in range(len(level)):
        for j in range(len(level[i])):
            if level[i][j] == 1:
                pygame.draw.line(screen, 'purple', (j * num2 + (0.5 * num2), i * num1),
                                 (j * num2 + (0.5 * num2), i * num1 + num1), 3)
            if level[i][j] == 2:
                pygame.draw.line(screen, 'purple', (j * num2, i * num1 + (0.5 * num1)),
                                 (j * num2 + num2, i * num1 + (0.5 * num1)), 3)
            if level[i][j] == 3:
                pygame.draw.arc(screen, 'purple',
                                [(j * num2 - (num2 * 0.4)) - 2, (i * num1 + (0.5 * num1)), num2, num1],
                                0, math.pi / 2, 3)
            if level[i][j] == 4:
                pygame.draw.arc(screen, 'purple',
                                [(j * num2 + (num2 * 0.5)), (i * num1 + (0.5 * num1)), num2, num1], math.pi / 2,
                                math.pi, 3)
            if level[i][j] == 5:
                pygame.draw.arc(screen, 'purple', [(j * num2 + (num2 * 0.5)), (i * num1 - (0.4 * num1)), num2, num1],
                                math.pi,
                                3 * math.pi / 2, 3)
            if level[i][j] == 6:
                pygame.draw.arc(screen, 'purple',
                                [(j * num2 - (num2 * 0.4)) - 2, (i * num1 - (0.4 * num1)), num2, num1], 3 * math.pi / 2,
                                2 * math.pi, 3)


run = True
while run:
    timer.tick(fps)
    screen.fill('black')
    draw_maze(level)

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            run = False

    pygame.display.flip()
pygame.quit()
