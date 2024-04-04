import unittest
from dijkstra import Dijkstra


class TestDijkstra(unittest.TestCase):
    def setUp(self):
        self.dijkstra_solver = Dijkstra(None)

    def test_calculate_cost_empty(self):
        cell_type = 0
        cost = self.dijkstra_solver.calculate_cost(cell_type)
        self.assertEqual(cost, 1)

    def test_calculate_cost_wall(self):
        cell_type = 1
        cost = self.dijkstra_solver.calculate_cost(cell_type)
        self.assertEqual(cost, float('inf'))

    def test_calculate_cost_goal(self):
        cell_type = 2
        cost = self.dijkstra_solver.calculate_cost(cell_type)
        self.assertEqual(cost, 100)

    def test_calculate_cost_start(self):
        cell_type = 3
        cost = self.dijkstra_solver.calculate_cost(cell_type)
        self.assertEqual(cost, 1)

    def test_find_shortest_path_simple(self):

        start_position = (0, 0)
        goal_position = (3, 3)
        path = self.dijkstra_solver.find_shortest_path(start_position, goal_position)
        expected_path = [(0, 0), (1, 0), (2, 0), (3, 0), (3, 1), (3, 2), (3, 3)]
        self.assertEqual(path, expected_path)

    def test_find_shortest_path_blocked_goal(self):

        start_position = (0, 0)
        goal_position = (3, 3)
        path = self.dijkstra_solver.find_shortest_path(start_position, goal_position)
        expected_path = []
        self.assertEqual(path, expected_path)

    def test_find_shortest_path_complex(self):

        start_position = (0, 0)
        goal_position = (4, 4)
        path = self.dijkstra_solver.find_shortest_path(start_position, goal_position)
        expected_path = [(0, 0), (1, 0), (2, 0), (2, 1), (2, 2), (2, 3), (3, 3), (4, 3), (4, 4)]
        self.assertEqual(path, expected_path)

    def test_get_neighbors_middle(self):
        maze = Dijkstra([
            [0, 0, 0, 1],
            [1, 1, 0, 0],
            [0, 1, 0, 1],
            [0, 0, 0, 0]
        ])
        cell = (1, 1)
        neighbors = maze.get_neighbors(cell)
        expected_neighbors = [(0, 1), (2, 1), (1, 0), (1, 2)]
        self.assertEqual(neighbors, expected_neighbors)

    def test_get_neighbors_corner(self):
        maze = Dijkstra([
            [0, 0, 0, 1],
            [1, 1, 0, 0],
            [0, 1, 0, 1],
            [0, 0, 0, 0]
        ])
        cell = (0, 0)
        neighbors = maze.get_neighbors(cell)
        expected_neighbors = [(1, 0), (0, 1)]
        self.assertEqual(neighbors, expected_neighbors)


if __name__ == "__main__":
    unittest.main()
