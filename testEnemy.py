import unittest
from unittest.mock import MagicMock, patch
from enemy import Enemy
from config import TILE_SIZE


class TestEnemy(unittest.TestCase):
    @patch('enemy.random')
    def test_init(self, mock_random):
        mock_maze = MagicMock()

        mock_random.randint.return_value = 2
        mock_maze.num_rows.return_value = 5
        mock_maze.num_columns.return_value = 6
        mock_maze.__getitem__.return_value = 0

        enemy = Enemy(mock_maze)

        self.assertEqual(enemy.x, 2 * 32)
        self.assertEqual(enemy.y, 0)

    @patch('enemy.random')
    def test_reset_position(self, mock_random):
        mock_maze = MagicMock()

        mock_random.randint.return_value = 2
        mock_maze.num_rows.return_value = 5
        mock_maze.num_columns.return_value = 6
        mock_maze.__getitem__.return_value = 0

        enemy = Enemy(mock_maze)
        enemy.reset_position()

        self.assertEqual(enemy.x, 2 * 32)
        self.assertEqual(enemy.y, 0)

    def test_draw(self):
        mock_screen = MagicMock()

        enemy = Enemy(None)
        enemy.draw(mock_screen)
        mock_screen.assert_called_once_with('blue', (enemy.x, enemy.y, enemy.TILE_SIZE, enemy.TILE_SIZE))


if __name__ == "__main__":
    unittest.main()
