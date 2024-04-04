import unittest
from game import Game


class TestGame(unittest.TestCase):

    def setUp(self):
        self.maze = [
            [1, 1, 1, 1, 1],
            [1, 0, 0, 0, 1],
            [1, 0, 1, 0, 1],
            [1, 0, 0, 0, 1],
            [1, 1, 1, 1, 1]
        ]
        self.game = Game(self.maze)

    def test_init(self):
        maze = [
            [1, 1, 1, 1, 1],
            [1, 0, 0, 0, 1],
            [1, 0, 1, 0, 1],
            [1, 0, 0, 0, 1],
            [1, 1, 1, 1, 1]
        ]

        game = Game(maze)

        self.assertEqual(game.maze, maze)
        self.assertEqual(game.player_position, (1, 1))
        self.assertEqual(game.enemy_positions, [(2, 2)])

    def test_get_player_position(self):
        maze = [
            [1, 1, 1, 1, 1],
            [1, 0, 0, 0, 1],
            [1, 0, 1, 0, 1],
            [1, 0, 0, 0, 1],
            [1, 1, 1, 1, 1]
        ]

        game = Game(maze)
        player_position = game.get_player_position()
        self.assertEqual(player_position, (1, 1))

    def test_get_enemy_positions(self):
        enemy_positions = self.game.get_enemy_positions()
        self.assertEqual(enemy_positions, [(2, 2)])

    def test_update_positions(self):
        self.game.update_positions()
        self.assertEqual(self.game.player_position, (1, 1))
        self.assertEqual(self.game.enemy_positions, [(2, 2)])

    def test_check_game_over(self):
        game_over = self.game.check_game_over()
        self.assertFalse(game_over)


if __name__ == "__main__":
    unittest.main()
