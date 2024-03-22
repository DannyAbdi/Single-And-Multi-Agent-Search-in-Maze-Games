import unittest
from dfs import DFS


class TestDFS(unittest.TestCase):
    def test_init(self):
        dfs = DFS()
        self.assertEqual(dfs.visited, set())
        self.assertEqual(dfs.path, [])

    def test_get_neighbours(self):
        maze = [
            [0, 0, 0, 1],
            [1, 1, 0, 0],
            [0, 1, 0, 1],
            [0, 0, 0, 0]
        ]
        dfs = DFS()

        self.assertEqual(dfs.get_neighbours(maze, 0, 0), [(0, 1), (1, 0)])
        self.assertEqual(dfs.get_neighbours(maze, 1, 1), [(1, 2), (2, 1)])
        self.assertEqual(dfs.get_neighbours(maze, 2, 2), [(2, 1), (3, 2)])

    def test_dfs(self):
        maze = [
            [0, 0, 0, 1],
            [1, 1, 0, 0],
            [0, 1, 0, 1],
            [0, 0, 0, 0]
        ]
        dfs = DFS()

        start = (0, 0)
        goal = (3, 3)
        self.assertTrue(dfs.dfs(maze, start, goal))

        start = (0, 0)
        goal = (2, 2)
        self.assertFalse(dfs.dfs(maze, start, goal))

    def test__dfs(self):
        maze = [
            [0, 0, 0, 1],
            [1, 1, 0, 0],
            [0, 1, 0, 1],
            [0, 0, 0, 0]
        ]
        dfs = DFS()

        start = (0, 0)
        goal = (3, 3)
        self.assertTrue(dfs._dfs(maze, start, goal))

        start = (0, 0)
        goal = (2, 2)
        self.assertFalse(dfs._dfs(maze, start, goal))

    def test_get_path(self):
        maze = [
            [0, 0, 0, 1],
            [1, 1, 0, 0],
            [0, 1, 0, 1],
            [0, 0, 0, 0]
        ]
        dfs = DFS()

        start = (0, 0)
        goal = (3, 3)
        dfs._dfs(maze, start, goal)
        expected_path = [(0, 0), (0, 1), (1, 1), (2, 1), (3, 1), (3, 2), (3, 3)]
        self.assertEqual(dfs.get_path(), expected_path)

        start = (0, 0)
        goal = (2, 2)  
        dfs._dfs(maze, start, goal)
        self.assertEqual(dfs.get_path(), [])


if __name__ == "__main__":
    unittest.main()
