import unittest
import pygame
from engine.eventqueue import EventQueue
from engine.renderer import Renderer
from engine.clock import Clock
from engine.gameloop import GameLoop
from levels.level import Level
from database.db_service import DatabaseService


def post_key(key):
    the_key = getattr(pygame, key, None)

    pygame.event.post(pygame.event.Event(pygame.KEYDOWN, {'key': the_key}))


class TestGameLoop(unittest.TestCase):
    def setUp(self):
        pygame.init()
        CELL_SIZE = 50
        level_maps = [
            [
                [0, 4, 0, 8],
                [1, 1, 1, 1],
                [0, 0, 0, 0]
            ],
            [
                [0, 4, 0, 8],
                [1, 1, 1, 1],
                [0, 0, 0, 0]
            ],
            [
                [0, 4, 0, 8],
                [1, 1, 1, 1],
                [0, 0, 0, 0]
            ]
        ]
        self.level1 = Level([
            [5, 4, 6, 8],
            [1, 1, 1, 1],
            [0, 0, 0, 0]
        ], 50)
        event_queue = EventQueue()
        screen = pygame.display.set_mode((10, 10))
        screen_center = (5, 5)
        renderer = Renderer(screen, screen_center)
        clock = Clock()
        database_service = DatabaseService()
        self.game_loop = GameLoop(level_maps, renderer, event_queue,
                                  clock, database_service, CELL_SIZE)
        self.game_loop._level = self.level1

    def test_gameloop_exists(self):
        self.assertIsNotNone(self.game_loop)

    def test_level_reset_resets_all_values(self):
        self.game_loop._failed = True
        self.game_loop._success = True
        self.game_loop._coins = 5
        self.game_loop._stars = 5
        self.game_loop._level = self.level1
        self.game_loop._paused = True

        self.game_loop._reset_level()

        values = (self.game_loop._failed, self.game_loop._success,
                  self.game_loop._coins, self.game_loop._stars,
                  self.game_loop._level, self.game_loop._paused)

        self.assertEqual((False, False, 0, 0, None, False), values)

    def test_pause_toggle_works(self):
        paused = self.game_loop._paused
        self.game_loop._toggle_pause()
        self.assertNotEqual(self.game_loop._paused, paused)

    def test_success_checks_are_correct(self):

        should_be_false = self.game_loop._success

        self.game_loop._level.player.rect.move_ip(100, 0)
        self.game_loop._check_success()

        self.assertNotEqual(self.game_loop._success, should_be_false)

    def test_fail_checks_are_correct(self):

        should_be_false = self.game_loop._failed

        self.game_loop._level.player.rect.move_ip(-1000, 0)
        self.game_loop._check_fail()

        self.assertNotEqual(self.game_loop._failed, should_be_false)

    def test_enter_returns_true_in_game(self):
        post_key("K_RETURN")

        self.assertEqual(True, self.game_loop._handle_events())

    def test_escape_returns_false_and_quits(self):
        post_key("K_ESCAPE")
        self.game_loop._toggle_pause()
        false_1 = self.game_loop._handle_events()
        false_2 = self.game_loop._paused

        post_key("K_ESCAPE")
        self.game_loop._failed = True
        self.game_loop._coins = 5
        false_3 = self.game_loop._handle_events()
        zero = self.game_loop._coins

        post_key("K_ESCAPE")
        self.game_loop._handle_events()

        with self.assertRaises(pygame.error):
            pygame.event.get()

        self.assertEqual((False, False, False, 0),
                         (false_1, false_2, false_3, zero))

    def test_coins_and_stars_are_collected(self):
        self.game_loop._level.move_player(-50)
        self.game_loop._collect()
        self.game_loop._level.move_player(100)
        self.game_loop._collect()
        self.game_loop._collect()

        self.assertEqual(
            (1, 1), (self.game_loop._coins, self.game_loop._stars))

    def test_start_checks_returns_correct_values(self):
        post_key("K_RETURN")
        true_1 = self.game_loop._check_start()
        none_1 = self.game_loop._check_start()

        post_key("K_r")
        none_2 = self.game_loop._check_start()

        self.assertEqual((true_1, none_1, none_2), (True, None, None))

    def test_buttons_change_chosen_level_in_menu(self):
        none_1 = self.game_loop._handle_menu_events()
        post_key("K_RETURN")
        true_1 = self.game_loop._handle_menu_events()
        post_key("K_RIGHT")
        self.game_loop._handle_menu_events()
        one = self.game_loop._chosen_level
        post_key("K_LEFT")
        self.game_loop._handle_menu_events()
        zero = self.game_loop._chosen_level

        self.assertEqual((none_1, true_1, one, zero), (None, True, 1, 0))
