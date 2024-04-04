import unittest
from unittest.mock import Mock, patch
from config import TILE_SIZE
from player import Player


class TestPlayer(unittest.TestCase):
    @patch('pygame.draw.rect')
    def test_draw(self, mock_rect):
        # Mock the screen surface
        screen_surface_mock = Mock()
        player = Player(10, 20)
        player.draw(screen_surface_mock)
        mock_rect.assert_called_once_with(screen_surface_mock, 'white', (10, 20, TILE_SIZE, TILE_SIZE))


if __name__ == "__main__":
    unittest.main()
