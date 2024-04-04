from config import *


class Maze:
    """
    Initializes a Maze object with an initial maze level.

    :param initial_level: The initial maze level.
    """
    def __init__(self, initial_level):
        self.current_level = initial_level
        self.update_screen_size()

    """
    Get the length of the maze, which is the number of rows in the maze.

    :return: The number of rows in the maze.
    """
    def num_rows(self):
        return len(self.current_level)

    """
    Get the number of columns in the maze.

    :return: The number of columns in the maze.
    """
    def num_columns(self):
        return len(self.current_level[0])

    """
    Retrieves the item at the specified index.

    :param index: The index of the item to retrieve.
    :return: The item at the specified index.
    """
    def __getitem__(self, index):
        return self.current_level[index]

    """
    Sets a new maze level and updates the screen size accordingly.

    :param new_level: The new maze level.
    """
    def set_level(self, new_level):
        self.current_level = new_level
        self.update_screen_size()

    """
    Updates the size of the game screen based on the current maze level.
    """
    def update_screen_size(self):
        screen_size = (len(self.current_level[0]) * TILE_SIZE, len(self.current_level) * TILE_SIZE)
        screen = pygame.display.set_mode(screen_size)

    """
    Draws the current maze level on the game screen.
    """
    def draw(self):
        for row in range(len(self.current_level)):
            for column in range(len(self.current_level[row])):
                x = column * TILE_SIZE
                y = row * TILE_SIZE
                tile = tiles[self.current_level[row][column]]
                screen.blit(tile, (x, y))
