from config import *


class Player:
    """
    Initialises a Player object with a specified position.

    :param x: The x-coordinate of the player's position.
    :param y: The y-coordinate of the player's position
    """
    def __init__(self, x, y):
        self.x = x
        self.y = y

    """
    Draws the player on the game screen using Pygame.

    This method utilizes the Pygame library to draw a white rectangle representing the player
    at the specified (x, y) coordinates with the size of TILE_SIZE.
    """
    def draw(self):
        pygame.draw.rect(screen, 'white', (self.x, self.y, TILE_SIZE, TILE_SIZE))
