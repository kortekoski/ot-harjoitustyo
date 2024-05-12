import unittest
import pygame
from levels.level import Level


class TestLevel(unittest.TestCase):
    def setUp(self):
        TEST_LEVEL_MAP = [[0, 0, 0, 0, 0],
                          [5, 6, 8, 9, 4]]
        CELL_SIZE = 50

        self.level = Level(TEST_LEVEL_MAP, CELL_SIZE)

        TEST_MAP_2 = [[0, 4, 2]]
        CELL_SIZE_2 = 50

        self.level2 = Level(TEST_MAP_2, CELL_SIZE_2)

        TEST_MAP_3 = [[1, 1, 1],[0, 4, 0], [1, 1, 1]]
        self.level3 = Level(TEST_MAP_3, 50)

    def test_sprites_are_movable(self):
        coin = self.level.coins.sprites()[0]
        starting_position_y = coin.rect.y
        self.level.move_sprite(coin, 0, 50)
        self.assertEqual(starting_position_y+50, coin.rect.y)

    def test_restart_resets_sprite_positions(self):
        coin = self.level.coins.sprites()[0]
        starting_position_y = coin.rect.y
        self.level.move_sprite(coin, 0, 50)
        self.level.restart_level()
        coin = self.level.coins.sprites()[0]
        end_position_y = coin.rect.y
        self.assertEqual(starting_position_y, end_position_y)

    def test_nuke_kills_all(self):
        self.level.nuke()
        counter = 0
        for sprite in self.level.all_sprites:
            counter += 1

        self.assertEqual(0, counter)

    def test_scroll_moves_sprites(self):
        starting_points = []

        for sprite in self.level.np_sprites:
            starting_points.append(sprite.rect.x)

        self.level.set_speed(50)
        self.level.scroll_level(1)

        ending_points = []
        for sprite in self.level.np_sprites:
            ending_points.append(sprite.rect.x)

        for i in range(0, len(starting_points)):
            self.assertEqual(ending_points[i], starting_points[i]-50)

    def test_scrolled_obstacle_pushes_player_back(self):
        starting_x = self.level2.player.rect.x
        self.level2.set_speed(50)
        self.level2.scroll_level(1)
        self.assertEqual(self.level2.player.rect.x, starting_x-50)

    def test_player_collects_collectables_when_hit(self):
        while self.level.player.rect.x > 0:
            self.level.move_player(-50)
            self.level.collect()
        self.assertEqual(0, len(self.level.coins.sprites()))

    def test_player_gravity_pulls_down(self):
        self.level.move_player(0, -50)
        position1 = self.level.player.rect.y
        self.level.gravity()
        position2 = self.level.player.rect.y
        self.assertGreater(position2, position1)

    def test_player_gravity_doesnt_pull_below_object(self):
        self.level3.move_player(0, +10)
        position1 = self.level3.player.rect.y
        self.level3.gravity()
        position2 = self.level3.player.rect.y
        self.assertEqual(position2, position1)

    def test_no_jumping_below_object(self):
        position1 = self.level3.player.rect.y
        self.level3.jump_player(True)
        position2 = self.level3.player.rect.y
        self.assertEqual(position2, position1)