from config import *
from dfs import *
from bfs import *
from dijkstra import *


class PlayerController:
    """
    Initializes a PlayerController object.

    :param player: The player controlled by this controller.
    :param maze: The maze used for navigation and solving.
    """
    def __init__(self, player, maze):
        self.player = player
        self.maze = maze
        self.dfs_solver = DFS()
        self.bfs_solver = BFS()
        self.dijkstra_solver = None

    """
    Moves the player in the specified direction based on keyboard input.

    :param direction: A dictionary representing the keys pressed.
    """
    def move_player(self, direction):
        new_x = self.player.x
        new_y = self.player.y

        if direction[pygame.K_UP]:
            new_y -= TILE_SIZE
        elif direction[pygame.K_DOWN]:
            new_y += TILE_SIZE
        elif direction[pygame.K_LEFT]:
            new_x -= TILE_SIZE
        elif direction[pygame.K_RIGHT]:
            new_x += TILE_SIZE

        if self.check_collision(new_x, new_y):
            self.player.x = new_x
            self.player.y = new_y

    """
    Checks if the player will collide with walls at the specified position.

    :param x: The x-coordinate of the potential position.
    :param y: The y-coordinate of the potential position.
    :return: True if collision is detected, False otherwise.
    """
    def check_collision(self, x, y):
        row = y // TILE_SIZE
        column = x // TILE_SIZE
        return self.maze.current_level[row][column] != 1

    """Resets the player's position to the starting point."""
    def reset_player_position(self):
        self.player.x = TILE_SIZE
        self.player.y = TILE_SIZE

    """
    Sets the DFS solver used by the controller.

    :param dfs_solver: The DFS solver object.
    """
    def set_dfs_solver(self, dfs_solver):
        self.dfs_solver = dfs_solver

    """
    Sets the BFS solver used by the controller.

    :param bfs_solver: The BFS solver object.
    """
    def set_bfs_solver(self, bfs_solver):
        self.bfs_solver = bfs_solver

    """
    Sets the Dijkstra solver used by the controller.

    :param dijkstra_solver: The Dijkstra solver object.
    """
    def set_dijkstra_solver(self, dijkstra_solver):
        self.dijkstra_solver = dijkstra_solver

    """
    Moves the player towards the goal using DFS.
    """
    def move_to_goal_dfs(self):
        start_position = (self.player.y // TILE_SIZE, self.player.x // TILE_SIZE)
        goal_position = self.find_goal_position()

        if goal_position:
            if self.dfs_solver.dfs(self.maze.current_level, start_position, goal_position):
                path = self.dfs_solver.get_path()
                self.follow_path(path)

    """
    Moves the player towards the goal using BFS pathfinding.
    """
    def move_to_goal_bfs(self):
        start_position = (self.player.y // TILE_SIZE, self.player.x // TILE_SIZE)
        goal_position = self.find_goal_position()

        if goal_position:
            if self.bfs_solver.bfs(self.maze.current_level, start_position, goal_position):
                path = self.bfs_solver.get_path()
                self.follow_path(path)

    """
    Moves the player towards the goal using Dijkstra's algorithm.
    """
    def move_to_goal_dijkstra(self):
        if self.dijkstra_solver is not None:
            start_position = (self.player.y // TILE_SIZE, self.player.x // TILE_SIZE)
            goal_position = self.find_goal_position()

            if goal_position:
                path = self.dijkstra_solver.find_shortest_path(start_position, goal_position)
                if path:
                    self.follow_path(path)

    """
    Moves the player along the specified path.

    :param path: The path to follow.
    """
    def follow_path(self, path):
        for position in path:
            goal_y, goal_x = position
            target_y, target_x = goal_y * TILE_SIZE, goal_x * TILE_SIZE

            while self.player.x != target_x or self.player.y != target_y:
                direction_x = 1 if target_x > self.player.x else -1 if target_x < self.player.x else 0
                direction_y = 1 if target_y > self.player.y else -1 if target_y < self.player.y else 0

                new_x, new_y = self.player.x + direction_x * TILE_SIZE, self.player.y + direction_y * TILE_SIZE

                if self.maze.current_level[new_y // TILE_SIZE][new_x // TILE_SIZE] != 1:
                    # Draw the path on the screen
                    self.maze.draw()
                    self.draw_path(path)

                    # Move the player
                    self.player.x, self.player.y = new_x, new_y

                    pygame.display.flip()
                    pygame.time.delay(100)  # Introduce a delay for visualization

    """
    Draws the path on the screen for visualization.

    :param path: The path to draw.
    """
    def draw_path(self, path):
        for position in path:
            pygame.draw.rect(
                screen,
                (0, 255, 0),  # Green color for the path
                (position[1] * TILE_SIZE, position[0] * TILE_SIZE, TILE_SIZE, TILE_SIZE),
            )

    """
    Finds the position of the goal in the maze.

    :return: The (row, column) position of the goal or None if not found.
    """
    def find_goal_position(self):
        for i in range(len(self.maze.current_level)):
            for j in range(len(self.maze.current_level[0])):
                if self.maze.current_level[i][j] == 3:
                    return i, j
        return None
