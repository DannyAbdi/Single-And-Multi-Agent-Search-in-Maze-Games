import heapq


class Dijkstra:
    """
    Initializes a Dijkstra object.

    :param maze: The maze used for navigation and solving.
    """
    def __init__(self, maze):
        self.maze = maze

    """
    Calculates the cost of moving from one cell to another based on the cell type.

    :param cell_type: The type of cell (0 for empty, 1 for wall, 2 for goal, etc.).
    :return: The cost of moving to the cell.
    """
    def calculate_cost(self, cell):
        if cell == 0:
            return 1
        elif cell == 2:
            return 100
        elif cell == 3:
            return 1
        else:
            return float('inf')

    """
    Finds the shortest path from the player's current position to a specific location using Dijkstra's algorithm.

    :param start_position: The (row, column) position of the start.
    :param goal_position: The (row, column) position of the goal.
    :return: The shortest path from the start position to the goal position.
    """
    def find_shortest_path(self, start_position, goal_position):
        frontier = [(0, start_position)]
        came_from = {}
        cost_so_far = {}
        came_from[start_position] = None
        cost_so_far[start_position] = 0

        while frontier:
            current_cost, current = heapq.heappop(frontier)

            if current == goal_position:
                break

            for next in self.get_neighbors(current):
                new_cost = cost_so_far[current] + self.calculate_cost(self.maze.current_level[next[0]][next[1]])
                if next not in cost_so_far or new_cost < cost_so_far[next]:
                    cost_so_far[next] = new_cost
                    priority = new_cost
                    heapq.heappush(frontier, (priority, next))
                    came_from[next] = current

        current = goal_position
        path = []
        while current != start_position:
            path.append(current)
            current = came_from[current]
        path.append(start_position)
        path.reverse()
        return path

    """
    Gets the valid neighboring cells of a given cell.

    :param cell: The (row, column) position of the cell.
    :return: A list of valid neighboring cells.
    """
    def get_neighbors(self, cell):
        neighbors = []
        for dx, dy in [(1, 0), (-1, 0), (0, 1), (0, -1)]:
            x, y = cell[1] + dx, cell[0] + dy
            if 0 <= x < len(self.maze.current_level[0]) and 0 <= y < len(self.maze.current_level):
                neighbors.append((y, x))
        return neighbors