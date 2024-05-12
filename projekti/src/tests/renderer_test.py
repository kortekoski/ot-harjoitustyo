import unittest
from unittest.mock import MagicMock
import pygame
from engine.renderer import Renderer
from levels.level import Level

class TestRenderer(unittest.TestCase):
    def setUp(self):
        pygame.init()
        level1 = Level([
            [5, 4, 6, 8],
            [1, 1, 1, 1],
            [0, 0, 0, 0]
        ], 50)
        display = pygame.display.set_mode((100, 100))
        center = (50, 50)
        self.renderer = Renderer(display, center, level1)
        self.renderer._render_text = MagicMock()

    def tearDown(self):
        pygame.quit()
    
    def test_fail_screen_renders_correct_texts(self):
        self.renderer.render(3, 3, True, False)
        self.renderer._render_text.assert_any_call("FAILED")
        self.renderer._render_text.assert_any_call("Press R to restart level, ESC to go to menu", 20, self.renderer._center_x, self.renderer._center_y + 20)

    def test_success_screen_renders_correct_texts(self):
        self.renderer.render(3, 3, False, True)
        self.renderer._render_text.assert_any_call("SUCCESS!!")
        self.renderer._render_text.assert_any_call("Press ENTER to return to menu", 25, self.renderer._center_x, self.renderer._center_y + 20)
