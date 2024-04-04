import unittest
from unittest.mock import Mock

import pygame

from maze import Maze


class TestMaze(unittest.TestCase):
    def test_num_rows(self):
        initial_level = [
            [0, 0, 0],
            [0, 0, 0],
            [0, 0, 0]
        ]
        maze = Maze(initial_level)
        self.assertEqual(maze.num_rows(), 3)

    def test_num_columns(self):
        initial_level = [
            [0, 0, 0, 0],
            [0, 0, 0, 0],
            [0, 0, 0, 0]
        ]
        maze = Maze(initial_level)
        self.assertEqual(maze.num_columns(), 4)

    def test_getitem(self):
        initial_level = [
            [0, 0, 0],
            [0, 0, 0],
            [0, 0, 0]
        ]
        maze = Maze(initial_level)
        self.assertEqual(maze[0], [0, 0, 0])
        self.assertEqual(maze[1], [0, 0, 0])
        self.assertEqual(maze[2], [0, 0, 0])

    def test_set_level(self):
        initial_level = [
            [0, 0, 0],
            [0, 0, 0],
            [0, 0, 0]
        ]
        maze = Maze(initial_level)
        new_level = [
            [1, 1, 1],
            [1, 1, 1],
            [1, 1, 1]
        ]
        maze.set_level(new_level)
        self.assertEqual(maze.current_level, new_level)

    def test_update_screen_size(self):
        initial_level = [
            [0, 0, 0],
            [0, 0, 0],
            [0, 0, 0]
        ]
        maze = Maze(initial_level)
        pygame.display.set_mode((800, 600))
        maze.update_screen_size()
        self.assertEqual(pygame.display.get_surface().get_size(), (3 * 32, 3 * 32))

    def test_draw(self):
        initial_level = [
            [0, 0, 0],
            [0, 1, 0],
            [0, 0, 0]
        ]
        maze = Maze(initial_level)
        tiles = {0: Mock(), 1: Mock()}
        maze.tiles = tiles

        maze.draw()

        expected_calls = [
            ((tiles[0], (0, 0)),),
            ((tiles[0], (32, 0)),),
            ((tiles[0], (64, 0)),),
            ((tiles[0], (0, 32)),),
            ((tiles[1], (32, 32)),),
            ((tiles[0], (64, 32)),),
            ((tiles[0], (0, 64)),),
            ((tiles[0], (32, 64)),),
            ((tiles[0], (64, 64)),),
        ]
        self.assertEqual(self.mock_screen.blit.call_args_list, expected_calls)


if __name__ == "__main__":
    unittest.main()
