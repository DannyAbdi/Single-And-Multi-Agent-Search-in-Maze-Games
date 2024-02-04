import heapq


class AStar:
    def __init__(self, maze):
        self.maze = maze
        self.start = (1, 1)
        self.corners = set()
        self.directions = [(-1, 0), (1, 0), (0, -1), (0, 1)]

        for i in range(maze.num_rows()):
            for j in range(maze.num_columns()):
                if maze[i][j] == 3 or maze[i][j] == 4:
                    self.corners.add((i, j))

    def heuristic1(self, current, corners, visited_corners):
        remaining_corners = sum(1 for corner in corners if corner not in visited_corners)
        first_corner = next(iter(corners))  # Get the first corner from the set
        return abs(current[0] - first_corner[0]) + abs(current[1] - first_corner[1]) + remaining_corners

    def heuristic2(self, current, corners, visited_corners):
        remaining_corners = sum(1 for corner in corners if corner not in visited_corners)
        return ((current[0] - corners[0][0]) ** 2 + (current[1] - corners[0][1]) ** 2) ** 0.5 + remaining_corners

    def all_corners_visited(self, corners, visited_corners):
        return all(corner in visited_corners for corner in corners)

    def find_goal_position(self, maze):
        for i in range(maze.num_rows()):
            for j in range(len(self.maze[0])):
                if self.maze[i][j] == 3:
                    return (i, j)
        return None

    def find_shortest_path(self, heuristic):
        start = (1, 1)
        goal = None

        visited = set()
        frontier = [(0, start, [])]  # Priority queue: (total_cost, current_node, path)
        heapq.heapify(frontier)

        while frontier:
            total_cost, current, path = heapq.heappop(frontier)
            if self.maze[current[0]][current[1]] == 3:
                goal = current
                break
            if current not in visited:
                visited.add(current)
                for dx, dy in self.directions:
                    x, y = current[0] + dx, current[1] + dy
                    if 0 <= x < self.maze.num_rows() and 0 <= y < self.maze.num_columns() and self.maze[x][y] != 1:
                        new_cost = total_cost + 1
                        heapq.heappush(frontier,
                                       (new_cost + heuristic((x, y), self.corners, visited), (x, y), path + [current]))

        if goal:
            return path + [goal]
        else:
            return None
