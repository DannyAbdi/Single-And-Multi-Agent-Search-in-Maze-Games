import unittest
from unittest.mock import Mock
from button import Button


class TestButton(unittest.TestCase):
    def setUp(self):
        pygame = Mock()
        self.mock_screen = pygame.display.set_mode.return_value
        self.mock_player_controller = Mock()
        self.mock_maze = Mock()
        self.mock_image = Mock()
        self.mock_image.get_width.return_value = 100
        self.mock_image.get_height.return_value = 50
        self.button = Button(self.mock_image, 100, 100, 1, None)

    def test_draw(self):
        mock_image = Mock()
        button = Button(mock_image, 100, 100, 1, Mock())

        button.draw()

        expected_calls = [
            ((mock_image, (100, 100)),),
        ]
        self.assertEqual(self.mock_screen.blit.call_args_list, expected_calls)

    def test_handle_mouse_click_when_clicked(self):
        button = Button(Mock(), 100, 100, 1, self.mock_player_controller)

        button.handle_mouse_click((110, 110), self.mock_maze)

        self.mock_maze.set_level.assert_called_once_with(1)
        self.mock_player_controller.reset_player_position.assert_called_once()
        self.assertTrue(button.is_clicked)

    def test_handle_mouse_click_when_not_clicked(self):
        button = Button(Mock(), 100, 100, 1, self.mock_player_controller)

        button.handle_mouse_click((90, 90), self.mock_maze)

        self.assertFalse(self.mock_maze.set_level.called)
        self.assertFalse(self.mock_player_controller.reset_player_position.called)
        self.assertFalse(button.is_clicked)

    def test_check_click_within_boundaries(self):
        result = self.button.check_click((150, 125))
        self.assertTrue(result)

    def test_check_click_outside_boundaries(self):
        result = self.button.check_click((50, 75))
        self.assertFalse(result)


if __name__ == "__main__":
    unittest.main()
