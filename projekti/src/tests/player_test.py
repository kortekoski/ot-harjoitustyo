import unittest
from sprites.player import Player


class TestPlayer(unittest.TestCase):
    def setUp(self):
        self.player = Player((50, 50))

    def test_is_jumping_returns_false_when_not_jumping(self):
        is_jumping = self.player.is_jumping()
        self.assertEqual(False, is_jumping)

    def test_is_jumping_returns_true_when_jumping(self):
        self.player.jumping = True
        is_jumping = self.player.is_jumping()
        self.assertEqual(True, is_jumping)

    def test_reset_jumping_resets_jumping(self):
        self.player.jumping = True
        self.player.reset_jumping()
        self.assertEqual(False, self.player.jumping)

    def test_reset_jumping_resets_jumping_height(self):
        self.player.jump_height = 1000
        self.player.reset_jumping()
        self.assertEqual(14, self.player.jump_height)

    def test_reset_jumping_resets_jumping_velocity(self):
        self.player.jump_velocity = 1000
        self.player.reset_jumping()
        self.assertEqual(self.player.jump_height, self.player.jump_velocity)
