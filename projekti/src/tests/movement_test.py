import unittest
from levels.level import Level


class TestMovement(unittest.TestCase):
    def setUp(self):
        LEVEL_MAP = [[0, 0, 0, 0, 0, 0, 0, 0],
                     [0, 1, 4, 0, 2, 0, 0, 0],
                     [1, 1, 1, 1, 1, 1, 0, 0]]
        CELL_SIZE = 50

        self.test_level = Level(LEVEL_MAP, CELL_SIZE)
        self.starting_position = self.test_level.player.get_position()

    def test_can_move_left_and_right(self):

        self.assertEqual(self.starting_position, (100, 50))

        self.test_level.move_player(50, 0)
        new_position = self.test_level.player.get_position()

        self.assertEqual(new_position, (150, 50))

        self.test_level.move_player(-50, 0)

        self.assertEqual(self.starting_position, (100, 50))

    def test_player_cannot_pass_platform_horizontally(self):
        self.test_level.move_player(-50, 0)
        new_position = self.test_level.player.get_position()
        self.assertEqual(self.starting_position, new_position)

    def test_player_cannot_pass_platform_vertically(self):
        self.test_level.move_player(0, 50)
        new_position = self.test_level.player.get_position()
        self.assertEqual(self.starting_position, new_position)

    def test_player_cannot_pass_obstacle_horizontally(self):
        self.test_level.move_player(50, 0)
        possible_position = self.test_level.player.get_position()
        self.test_level.move_player(50, 0)
        new_position = self.test_level.player.get_position()
        self.assertEqual(possible_position, new_position)

    def test_player_cannot_pass_obstacle_vertically(self):
        self.test_level.move_player(0, -50)
        self.test_level.move_player(100, 0)
        possible_position = self.test_level.player.get_position()
        self.test_level.move_player(0, 50)
        new_position = self.test_level.player.get_position()
        self.assertEqual(possible_position, new_position)
