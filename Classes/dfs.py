
class DFS:
    """
    Initializes a DFS (Depth-First Search) solver object.
    """
    def __init__(self):
        self.visited = set()
        self.path = []

    """
    Returns a list of valid neighbours for a given cell in the maze.

    :param maze: The maze grid.
    :param i: The row index of the current cell.
    :param j: The column index of the current cell.
    :return: A list of valid neighbours.
    """
    def get_neighbours(self, maze, i, j):
        neighbours = []
        directions = [(0, 1), (1, 0), (0, -1), (-1, 0)]

        for direction in directions:
            ni, nj = i + direction[0], j + direction[1]
            if 0 <= ni < len(maze) and 0 <= nj < len(maze[0]) and maze[ni][nj] != 1:
                neighbours.append((ni, nj))

        return neighbours

    """
    Performs Depth-First Search on the maze to find a path from the start to the goal.

    :param maze: The maze grid.
    :param start: The starting position.
    :param goal: The goal position.
    :return: True if a path is found, False otherwise.
    """
    def dfs(self, maze, start, goal):
        self.visited.clear()
        self.path.clear()
        return self._dfs(maze, start, goal)

    """
    Recursive helper function for DFS.

    :param maze: The maze grid.
    :param current: The current position.
    :param goal: The goal position.
    :return: True if a path is found, False otherwise.
    """
    def _dfs(self, maze, current, goal):
        if current == goal:
            self.path.append(current)
            return True

        self.visited.add(current)

        for neighbour in self.get_neighbours(maze, current[0], current[1]):
            if neighbour not in self.visited and self._dfs(maze, neighbour, goal):
                self.path.append(current)
                return True

        return False

    """
    Returns the reconstructed path from start to goal.

    :return: The path as a list of positions.
    """
    def get_path(self):
        return list(reversed(self.path))
