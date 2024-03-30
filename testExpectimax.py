import unittest
from expectimax import Expectimax


class TestExpectimax(unittest.TestCase):

    def test_valid_scenario(self):
        maze = [[0, 0, 0],
                [0, 1, 0],
                [0, 0, 0]]
        expectimax_solver = Expectimax(maze)
        player_position = (0, 0)
        enemy_position = (2, 2)
        depth = 3
        maximizing_player = True
        result = expectimax_solver.expectimax(player_position, enemy_position, depth, maximizing_player)
        self.assertIsNotNone(result)

    def test_invalid_scenario_negative_depth(self):
        maze = [[0, 0, 0],
                [0, 1, 0],
                [0, 0, 0]]
        expectimax_solver = Expectimax(maze)
        player_position = (0, 0)
        enemy_position = (2, 2)
        depth = -1
        maximizing_player = True
        with self.assertRaises(ValueError):
            expectimax_solver.expectimax(player_position, enemy_position, depth, maximizing_player)

    def test_no_valid_moves(self):
        maze = [[1, 1, 1],
                [1, 1, 1],
                [1, 1, 1]]
        expectimax_solver = Expectimax(maze)
        player_position = (0, 0)
        enemy_position = (2, 2)
        depth = 3
        maximizing_player = True
        result = expectimax_solver.expectimax(player_position, enemy_position, depth, maximizing_player)
        self.assertEqual(result, 0)

    def test_game_over(self):
        maze = [[0, 0, 0],
                [0, 0, 0],
                [0, 0, 0]]
        expectimax_solver = Expectimax(maze)
        player_position = (0, 0)
        enemy_position = (2, 2)
        depth = 3
        maximizing_player = True
        result = expectimax_solver.expectimax(player_position, enemy_position, depth, maximizing_player)
        self.assertEqual(result, 0)

    def test_max_depth(self):
        maze = [[0, 0, 0],
                [0, 0, 0],
                [0, 0, 0]]
        expectimax_solver = Expectimax(maze)
        player_position = (0, 0)
        enemy_position = (2, 2)
        depth = 10
        maximizing_player = True
        result = expectimax_solver.expectimax(player_position, enemy_position, depth, maximizing_player)
        self.assertIsNotNone(result)


if __name__ == '__main__':
    unittest.main()
