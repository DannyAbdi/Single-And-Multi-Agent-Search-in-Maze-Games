from config import *


class Button:
    """
    Initializes a Button object with specified attributes.

    :param image: The image representing the button.
    :param x: The x-coordinate of the button's position.
    :param y: The y-coordinate of the button's position.
    :param level: The level associated with the button.
    :param player_controller: The player controller associated with the button.
    """

    def __init__(self, image, x, y, level, player_controller):
        self.image = image
        self.x = x
        self.y = y
        self.level = level
        self.is_clicked = False
        self.player_controller = player_controller

    """
    Draws the button on the game screen.

    This method scales the button's image, positions it, and blits it onto the screen.
    """
    def draw(self):
        width = self.image.get_width()
        height = self.image.get_height()
        scaled_image = pygame.transform.scale(self.image, (int(width * 0.7), int(height * 0.7)))
        image_rect = scaled_image.get_rect()
        image_rect.right = self.x
        image_rect.top = self.y
        screen.blit(scaled_image, image_rect)

    """
    Handles mouse clicks on the button.

    If the button is clicked, it sets the maze level, resets the player position, and updates the 'is_clicked' 
    attribute.

    :param mouse_pos: The current mouse position (x, y).
    :param maze: The maze associated with the button.
    """
    def handle_mouse_click(self, mouse_pos, maze):
        if self.check_click(mouse_pos):
            maze.set_level(self.level)
            self.player_controller.reset_player_position()
            self.is_clicked = True
        else:
            self.is_clicked = False

    """
    Checks if the mouse click is within the button's boundaries.

    :param mouse_pos: The current mouse position (x, y).
    :return: True if the mouse click is within the button's boundaries, False otherwise.
    """
    def check_click(self, mouse_pos):
        x, y = mouse_pos
        return self.x <= x <= self.x + self.image.get_width() and self.y <= y <= self.y + self.image.get_height()

