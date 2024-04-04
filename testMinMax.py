import unittest
from minmax import MinMax


class TestMinMax(unittest.TestCase):

    def test_get_valid_moves_middle(self):
        maze = [[0, 0, 0],
                [0, 1, 0],
                [0, 0, 0]]
        minmax = MinMax(maze)
        player_position = (1, 1)
        valid_moves = minmax.get_valid_moves(player_position)
        expected_moves = [(0, 1), (2, 1), (1, 0), (1, 2)]
        self.assertEqual(valid_moves, expected_moves)

    def test_get_valid_moves_corner(self):
        maze = [[0, 1, 0],
                [1, 1, 0],
                [0, 0, 0]]
        minmax = MinMax(maze)
        player_position = (0, 0)
        valid_moves = minmax.get_valid_moves(player_position)
        expected_moves = [(1, 0), (0, 1)]
        self.assertEqual(valid_moves, expected_moves)

    def test_valid_move(self):
        maze = [[0, 0, 0],
                [0, 1, 0],
                [0, 0, 0]]
        minmax = MinMax(maze)
        valid_position = (1, 0)
        self.assertTrue(minmax.is_valid_move(valid_position))

    def test_invalid_move_wall(self):
        maze = [[0, 1, 0],
                [1, 1, 0],
                [0, 0, 0]]
        minmax = MinMax(maze)
        wall_position = (0, 1)
        self.assertFalse(minmax.is_valid_move(wall_position))

    def test_invalid_move_outside(self):
        maze = [[0, 0, 0],
                [0, 1, 0],
                [0, 0, 0]]
        minmax = MinMax(maze)
        outside_position = (3, 0)
        self.assertFalse(minmax.is_valid_move(outside_position))

    def test_minmax(self):
        maze = [[0, 0, 0],
                [0, 1, 0],
                [0, 0, 0]]
        minmax = MinMax(maze)
        player_position = (0, 0)
        enemy_position = (2, 2)
        depth = 3
        alpha = float('-inf')
        beta = float('inf')
        maximizing_player = True
        result = minmax.minmax(player_position, enemy_position, depth, alpha, beta, maximizing_player)
        self.assertIsInstance(result, int)

        maze = [[0, 0, 0],
                [0, 1, 0],
                [0, 0, 0]]
        player_position = (0, 0)
        enemy_position = (2, 2)
        depth = 1

        result = minmax.minmax(player_position, enemy_position, depth, float('-inf'), float('inf'), maximizing_player)
        print("Result:", result)

    def test_evaluate(self):
        maze = [[0, 0, 0],
                [0, 1, 0],
                [0, 0, 0]]
        minmax_object = MinMax(maze)
        print("Testing the evaluate method...")

        player_position = (1, 1)
        enemy_position = (1, 1)
        evaluation_result = minmax_object.evaluate(player_position, enemy_position)
        print("Evaluation result when player and enemy are at the same position:", evaluation_result)

        player_position = (2, 2)
        enemy_position = (1, 1)
        evaluation_result = minmax_object.evaluate(player_position, enemy_position)
        print("Evaluation result when player is closer to the goal than the enemy:", evaluation_result)

        player_position = (1, 1)
        enemy_position = (2, 2)
        evaluation_result = minmax_object.evaluate(player_position, enemy_position)
        print("Evaluation result when enemy is closer to the goal than the player:", evaluation_result)

    def test_game_over(self):
        maze = [[0, 0, 0],
                [0, 1, 0],
                [0, 0, 0]]
        minmax_object = MinMax(maze)
        print("Testing the game_over method...")

        game_over_result = minmax_object.game_over()
        print("Game over result when the game is not over:", game_over_result)

        game_over_result = minmax_object.game_over()
        print("Game over result when the game is over:", game_over_result)


if __name__ == '__main__':
    unittest.main()
