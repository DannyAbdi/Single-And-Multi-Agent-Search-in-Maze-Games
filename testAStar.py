import unittest
from aStar import AStar


class TestAStar(unittest.TestCase):
    def setUp(self):
        self.maze = [
            [1, 0, 0, 0],
            [0, 1, 1, 0],
            [0, 0, 0, 1],
            [1, 0, 0, 0]
        ]
        self.a_star_solver = AStar(self.maze)

    def test_heuristic1(self):
        current_position = (1, 1)
        visited_corners = set()
        heuristic_result = self.a_star_solver.heuristic1(current_position, self.a_star_solver.corners, visited_corners)
        self.assertEqual(heuristic_result, 3)

        current_position = (2, 2)
        visited_corners = set()
        heuristic_result = self.a_star_solver.heuristic1(current_position, self.a_star_solver.corners, visited_corners)
        self.assertEqual(heuristic_result, ...)

    def test_heuristic2(self):
        current_position = (1, 1)
        visited_corners = set()
        heuristic_result = self.a_star_solver.heuristic2(current_position, self.a_star_solver.corners, visited_corners)
        self.assertEqual(heuristic_result, ...)

        current_position = (2, 2)
        visited_corners = set()
        heuristic_result = self.a_star_solver.heuristic2(current_position, self.a_star_solver.corners, visited_corners)
        self.assertEqual(heuristic_result, ...)

    def test_all_corners_visited(self):
        corners = {(1, 1), (2, 2), (3, 3)}
        visited_corners = {(1, 1), (2, 2)}
        result = self.a_star_solver.all_corners_visited(corners, visited_corners)
        self.assertFalse(result)

    def test_find_goal_position(self):
        maze_with_goal = ...
        goal_position = self.a_star_solver.find_goal_position(maze_with_goal)
        self.assertIsNotNone(goal_position)

        maze_without_goal = ...
        goal_position = self.a_star_solver.find_goal_position(maze_without_goal)
        self.assertIsNone(goal_position)

    def test_find_shortest_path_with_valid_heuristic(self):
        def valid_heuristic(current, corners, visited_corners):
            return 0

        path = self.a_star_solver.find_shortest_path(valid_heuristic)
        self.assertIsNotNone(path)

    def test_find_shortest_path_with_invalid_heuristic(self):
        def invalid_heuristic(current, corners, visited_corners):
            return None

        path = self.a_star_solver.find_shortest_path(invalid_heuristic)
        self.assertIsNone(path)


if __name__ == '__main__':
    unittest.main()
