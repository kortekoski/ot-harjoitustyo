import unittest
from levels.level import Level


class TestMovement(unittest.TestCase):
    def setUp(self):
        LEVEL_MAP = [[0, 0, 0, 0, 0],
                     [0, 1, 4, 0, 0]]
        CELL_SIZE = 50

        self.test_level = Level(LEVEL_MAP, CELL_SIZE)

    def test_can_move_left_and_right(self):
        starting_position = self.test_level.player.get_position()

        self.assertEqual(starting_position, (100, 50))

        self.test_level.move_player(50, 0)
        new_position = self.test_level.player.get_position()

        self.assertEqual(new_position, (150, 50))

        self.test_level.move_player(-50, 0)

        self.assertEqual(starting_position, (100, 50))

    def test_player_cannot_pass_platform_horizontally(self):
        starting_position = self.test_level.player.get_position()
        self.test_level.move_player(-50, 0)
        new_position = self.test_level.player.get_position()
        self.assertEqual(starting_position, new_position)
