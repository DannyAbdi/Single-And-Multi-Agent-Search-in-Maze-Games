from collections import deque


class BFS:
    """
    Initializes a BFS (Breadth-First Search) solver object.
    """

    def __init__(self):
        self.visited = set()
        self.queue = deque()
        self.parent = {}  # Dictionary to store parent relationships for path reconstruction
        self.path = []  # List to store the final path

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
    Performs Breadth-First Search on the maze to find a path from the start to the goal.

    :param maze: The maze grid.
    :param start: The starting position.
    :param goal: The goal position.
    :return: True if a path is found, False otherwise.
    """

    def bfs(self, maze, start, goal):
        self.visited.clear()
        self.queue.clear()
        self.parent.clear()  # Clear parent dictionary
        self.path.clear()  # Clear path

        self.queue.append(start)
        self.visited.add(start)

        while self.queue:
            current = self.queue.popleft()

            if current == goal:
                self.construct_path(start, goal)
                return True  # Goal found

            for neighbour in self.get_neighbours(maze, current[0], current[1]):
                if neighbour not in self.visited:
                    self.queue.append(neighbour)
                    self.visited.add(neighbour)
                    self.parent[neighbour] = current

        return False  # Goal not reached

    """
    Constructs the path from the start to the goal using the parent dictionary.

    :param start: The starting position.
    :param goal: The goal position.
    """

    def construct_path(self, start, goal):
        current = goal
        while current != start:
            self.path.append(current)
            current = self.parent[current]

        self.path.append(start)

    """
    Returns the reconstructed path from start to goal.

    :return: The path as a list of positions.
    """

    def get_path(self):
        return list(reversed(self.path))
