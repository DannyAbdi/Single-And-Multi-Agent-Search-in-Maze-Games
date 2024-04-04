import unittest
from collections import deque
from bfs import BFS


class TestBFS(unittest.TestCase):
    def setUp(self):
        self.bfs_solver = BFS()

    def test_init(self):
        bfs = BFS()
        self.assertEqual(len(bfs.visited), 0)
        self.assertIsInstance(bfs.queue, deque)
        self.assertEqual(len(bfs.parent), 0)
        self.assertEqual(len(bfs.path), 0)

    def test_get_neighbours(self):
        bfs = BFS()
        maze = [
            [0, 0, 0],
            [0, 1, 0],
            [0, 0, 0]
        ]
        neighbours = bfs.get_neighbours(maze, 1, 1)
        expected_neighbours = [(0, 1), (1, 0), (1, 2), (2, 1)]
        self.assertEqual(neighbours, expected_neighbours)

        maze = [
            [1, 1, 1],
            [1, 1, 1],
            [1, 1, 1]
        ]
        neighbours = bfs.get_neighbours(maze, 1, 1)
        self.assertEqual(neighbours, [])

    def test_bfs_path_found(self):
        maze = [
            [0, 0, 0],
            [1, 1, 0],
            [0, 0, 0]
        ]
        start = (0, 0)
        goal = (2, 2)
        self.assertTrue(self.bfs_solver.bfs(maze, start, goal))

    def test_bfs_no_path(self):
        maze = [
            [0, 1, 0],
            [1, 1, 0],
            [0, 1, 0]
        ]
        start = (0, 0)
        goal = (2, 2)
        self.assertFalse(self.bfs_solver.bfs(maze, start, goal))

    def test_bfs_empty_maze(self):
        maze = []
        start = (0, 0)
        goal = (2, 2)
        self.assertFalse(self.bfs_solver.bfs(maze, start, goal))

    def test_bfs_unreachable_goal(self):
        maze = [
            [0, 0, 0],
            [1, 1, 0],
            [0, 0, 1]
        ]
        start = (0, 0)
        goal = (2, 2)
        self.assertFalse(self.bfs_solver.bfs(maze, start, goal))

    def test_bfs_unreachable_start(self):
        maze = [
            [1, 0, 0],
            [1, 1, 0],
            [0, 0, 0]
        ]
        start = (0, 0)
        goal = (2, 2)
        self.assertFalse(self.bfs_solver.bfs(maze, start, goal))

    def test_bfs_single_cell_maze(self):
        maze = [[0]]
        start = (0, 0)
        goal = (0, 0)
        self.assertTrue(self.bfs_solver.bfs(maze, start, goal))

    def test_construct_path(self):
        start = (0, 0)
        goal = (2, 2)
        parent = {
            (1, 1): (0, 1),
            (1, 2): (1, 1),
            (2, 2): (1, 2),
            (0, 1): (0, 0)
        }
        self.bfs_solver.parent = parent
        self.bfs_solver.construct_path(start, goal)
        expected_path = [(0, 0), (0, 1), (1, 1), (1, 2), (2, 2)]
        self.assertEqual(self.bfs_solver.path, expected_path)

    def test_get_path(self):
        self.bfs_solver.path = [(0, 0), (0, 1), (1, 1), (1, 2), (2, 2)]
        expected_path = [(2, 2), (1, 2), (1, 1), (0, 1), (0, 0)]
        self.assertEqual(self.bfs_solver.get_path(), expected_path)


if __name__ == "__main__":
    unittest.main()
