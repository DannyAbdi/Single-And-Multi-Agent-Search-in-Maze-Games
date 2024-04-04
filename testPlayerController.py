import unittest
from unittest.mock import Mock

import pygame

from config import TILE_SIZE
from player import Player
from playerController import PlayerController  # Import the PlayerController class


class TestPlayerController(unittest.TestCase):
    def setUp(self):
        self.player_mock = Mock()
        self.maze_mock = Mock()
        self.player_controller = PlayerController(self.player_mock, self.maze_mock)

    def test_move_player_up(self):
        direction = {pygame.K_UP: True, pygame.K_DOWN: False, pygame.K_LEFT: False, pygame.K_RIGHT: False}
        self.player_controller.move_player(direction)
        self.assertEqual(self.player_mock.y, self.player_mock.y - TILE_SIZE)

    def test_move_player_down(self):
        direction = {pygame.K_UP: False, pygame.K_DOWN: True, pygame.K_LEFT: False, pygame.K_RIGHT: False}
        self.player_controller.move_player(direction)
        self.assertEqual(self.player_mock.y, self.player_mock.y + TILE_SIZE)

    def test_move_player_left(self):
        direction = {pygame.K_UP: False, pygame.K_DOWN: False, pygame.K_LEFT: True, pygame.K_RIGHT: False}
        self.player_controller.move_player(direction)
        self.assertEqual(self.player_mock.x, self.player_mock.x - TILE_SIZE)

    def test_move_player_right(self):
        direction = {pygame.K_UP: False, pygame.K_DOWN: False, pygame.K_LEFT: False, pygame.K_RIGHT: True}
        self.player_controller.move_player(direction)
        self.assertEqual(self.player_mock.x, self.player_mock.x + TILE_SIZE)

    def test_valid_position_within_maze(self):
        position = (1, 1)
        self.assertTrue(self.player_controller.is_valid_position(position))

    def test_position_outside_maze_bounds(self):
        position = (-1, 1)
        self.assertFalse(self.player_controller.is_valid_position(position))
        position = (10, 5)
        self.assertFalse(self.player_controller.is_valid_position(position))
        position = (1, 10)
        self.assertFalse(self.player_controller.is_valid_position(position))

    def test_position_collides_with_wall(self):
        self.player_controller.maze = Mock(current_level=[[0, 0, 0],
                                                          [0, 1, 0],
                                                          [0, 0, 0]])
        position = (1, 1)
        self.assertFalse(self.player_controller.is_valid_position(position))
        position = (0, 1)
        self.assertTrue(self.player_controller.is_valid_position(position))

    def test_collision_with_wall(self):
        self.player_controller.maze = [[0, 0, 0],
                                       [0, 1, 0],
                                       [0, 0, 0]]
        x, y = 50, 50
        self.assertTrue(self.player_controller.check_collision(x, y))

    def test_no_collision_with_wall(self):
        self.player_controller.maze = [[0, 0, 0],
                                       [0, 0, 0],
                                       [0, 0, 0]]
        x, y = 50, 50
        self.assertFalse(self.player_controller.check_collision(x, y))

    def test_reset_player_position(self):
        initial_x, initial_y = 100, 100
        self.player_controller.player = Player(initial_x, initial_y)
        self.player_controller.reset_player_position()
        self.assertEqual(self.player_controller.player.x, TILE_SIZE)
        self.assertEqual(self.player_controller.player.y, TILE_SIZE)

    def test_set_dfs_solver(self):
        dfs_solver_mock = Mock()
        self.player_controller.set_dfs_solver(dfs_solver_mock)
        self.assertEqual(self.player_controller.dfs_solver, dfs_solver_mock)

    def test_set_bfs_solver(self):
        bfs_solver_mock = Mock()
        self.player_controller.set_bfs_solver(bfs_solver_mock)
        self.assertEqual(self.player_controller.bfs_solver, bfs_solver_mock)

    def test_set_dijkstra_solver(self):
        dijkstra_solver_mock = Mock()
        self.player_controller.set_dijkstra_solver(dijkstra_solver_mock)
        self.assertEqual(self.player_controller.dijkstra_solver, dijkstra_solver_mock)

    def test_set_astar_solver(self):
        astar_solver_mock = Mock()
        self.player_controller.set_astar_solver(astar_solver_mock)
        self.assertEqual(self.player_controller.astar_solver, astar_solver_mock)

    def test_move_to_goal_dfs(self):
        dfs_solver_mock = Mock()
        dfs_solver_mock.dfs.return_value = True
        dfs_solver_mock.get_path.return_value = [(1, 1), (1, 2), (1, 3)]

        self.player_controller.set_dfs_solver(dfs_solver_mock)
        self.player_controller.maze = Mock()
        self.player_controller.maze.current_level = [
            [0, 0, 0, 0],
            [0, 0, 3, 0],
            [0, 0, 0, 0],
        ]

        self.player_controller.player.x = TILE_SIZE
        self.player_controller.player.y = TILE_SIZE
        self.player_controller.move_to_goal_dfs()

        expected_path = [(1 * TILE_SIZE, 1 * TILE_SIZE), (1 * TILE_SIZE, 2 * TILE_SIZE), (1 * TILE_SIZE, 3 * TILE_SIZE)]
        self.assertEqual(
            [(self.player_controller.player.x, self.player_controller.player.y) for _ in range(len(expected_path))],
            expected_path)

    def test_move_to_goal_bfs(self):
        bfs_solver_mock = Mock()
        bfs_solver_mock.bfs.return_value = True
        bfs_solver_mock.get_path.return_value = [(1, 1), (1, 2), (1, 3)]

        self.player_controller.set_bfs_solver(bfs_solver_mock)
        self.player_controller.maze = Mock()
        self.player_controller.maze.current_level = [
            [0, 0, 0, 0],
            [0, 0, 3, 0],
            [0, 0, 0, 0],
        ]

        self.player_controller.player.x = TILE_SIZE
        self.player_controller.player.y = TILE_SIZE
        self.player_controller.move_to_goal_bfs()

        expected_path = [(1 * TILE_SIZE, 1 * TILE_SIZE), (1 * TILE_SIZE, 2 * TILE_SIZE), (1 * TILE_SIZE, 3 * TILE_SIZE)]
        self.assertEqual(
            [(self.player_controller.player.x, self.player_controller.player.y) for _ in range(len(expected_path))],
            expected_path)

    def test_move_to_goal_dijkstra(self):
        dijkstra_solver_mock = Mock()
        dijkstra_solver_mock.find_shortest_path.return_value = [(1, 1), (1, 2), (1, 3)]  # Simulate a path

        self.player_controller.set_dijkstra_solver(dijkstra_solver_mock)
        self.player_controller.maze = Mock()
        self.player_controller.maze.current_level = [
            [0, 0, 0, 0],
            [0, 0, 3, 0],
            [0, 0, 0, 0],
        ]

        self.player_controller.player.x = TILE_SIZE
        self.player_controller.player.y = TILE_SIZE
        self.player_controller.move_to_goal_dijkstra()

        expected_path = [(1 * TILE_SIZE, 1 * TILE_SIZE), (1 * TILE_SIZE, 2 * TILE_SIZE), (1 * TILE_SIZE, 3 * TILE_SIZE)]
        self.assertEqual(
            [(self.player_controller.player.x, self.player_controller.player.y) for _ in range(len(expected_path))],
            expected_path)

    def test_move_to_goal_astar(self):
        astar_solver_mock = Mock()
        astar_solver_mock.find_goal_position.return_value = (2, 2)  # Simulate a goal position
        astar_solver_mock.find_shortest_path.return_value = [(1, 1), (1, 2), (1, 3)]  # Simulate a path

        self.player_controller.set_astar_solver(astar_solver_mock)
        self.player_controller.maze = Mock()
        self.player_controller.maze.current_level = [
            [0, 0, 0, 0],
            [0, 0, 3, 0],
            [0, 0, 0, 0],
        ]

        self.player_controller.player.x = TILE_SIZE
        self.player_controller.player.y = TILE_SIZE
        self.player_controller.move_to_goal_astar()

        expected_path = [(1 * TILE_SIZE, 1 * TILE_SIZE), (1 * TILE_SIZE, 2 * TILE_SIZE), (1 * TILE_SIZE, 3 * TILE_SIZE)]
        self.assertEqual(
            [(self.player_controller.player.x, self.player_controller.player.y) for _ in range(len(expected_path))],
            expected_path)

    def test_follow_path(self):
        player_mock = Mock()
        self.player_controller.player = player_mock
        maze_mock = Mock()
        self.player_controller.maze = maze_mock
        path = [(0, 0), (0, 1), (0, 2)]
        self.player_controller.follow_path(path)
        expected_positions = [(0, 0), (0, 1), (0, 2)]
        self.assertEqual([(args[0], args[1]) for args in player_mock.x.call_args_list], expected_positions)

    def test_draw_path(self):
        screen_mock = Mock()
        self.player_controller.screen = screen_mock
        path = [(0, 0), (0, 1), (1, 1)]
        self.player_controller.draw_path(path)

        expected_calls = [
            ((screen_mock,), {'color': (0, 255, 0), 'rect': (0, 0, TILE_SIZE, TILE_SIZE)}),
            ((screen_mock,), {'color': (0, 255, 0), 'rect': (TILE_SIZE, 0, TILE_SIZE, TILE_SIZE)}),
            ((screen_mock,), {'color': (0, 255, 0), 'rect': (TILE_SIZE, TILE_SIZE, TILE_SIZE, TILE_SIZE)})
        ]

        self.assertEqual(screen_mock.mock_calls,
                         [unittest.mock.call.draw.rect(*args, **kwargs) for args, kwargs in expected_calls])

    def test_find_goal_position(self):
        mock_maze = Mock()
        mock_maze.current_level = [
            [0, 0, 0],
            [0, 0, 0],
            [0, 0, 3]
        ]

        self.player_controller.maze = mock_maze
        goal_position = self.player_controller.find_goal_position()
        expected_goal_position = (2, 2)
        self.assertEqual(goal_position, expected_goal_position)


if __name__ == "__main__":
    unittest.main()
