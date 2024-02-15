import random
from config import *

"""
Class representing an enemy agent in the game.
"""
class Enemy:
    """
    Initialise the Enemy object.

    :param maze (Maze): The maze object representing the game environment.
    :param x (int): The x-coordinate of the enemy's position.
    :param y (int): The y-coordinate of the enemy's position.
    """
    def __init__(self, maze):
        self.maze = maze
        self.x, self.y = self.reset_position()

    """
    Reset the position of the enemy to a valid starting position in the maze.

    :return: tuple: A tuple containing the x and y coordinates of the enemy's position.
    """
    def reset_position(self):
        while True:
            num_rows = self.maze.num_rows()
            num_cols = self.maze.num_columns()

            random_row = random.randint(0, num_rows - 1)

            start_col = num_cols - 2

            self.x = start_col * TILE_SIZE
            self.y = random_row * TILE_SIZE

            if self.maze[random_row][start_col] != 1:
                return self.x, self.y

    """
    Draw the enemy on the screen.

    :param screen: The Pygame screen surface to draw on.
    """
    def draw(self, screen):
        pygame.draw.rect(screen, 'blue', (self.x, self.y, TILE_SIZE, TILE_SIZE))
