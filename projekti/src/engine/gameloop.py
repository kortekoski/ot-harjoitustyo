import os
import pygame

dirname = os.path.dirname(__file__)


class GameLoop:
    def __init__(self, level, renderer, event_queue, clock, cell_size):
        self._level = level
        self._renderer = renderer
        self._event_queue = event_queue
        self._clock = clock
        self._cell_size = cell_size

        # These could be moved to a class called "State" or something
        self._failed = False
        self._success = False
        self._coins = 0
        self._stars = 0

    def start(self):
        while True:
            if self._check_start():
                break

            self._render_introscreen()
            self._clock.tick(60)

        pygame.mixer.music.load(os.path.join(
            dirname, "..", "assets", "test_track.mp3"))
        pygame.mixer.music.play(-1)

        while True:
            if self._handle_events() is False:
                break

            if not self._failed and not self._success:
                self._gravity()
                self._handle_player_movement()
                self._scroll_level()

                self._check_success()
                self._check_fail()

                self._render()

                self._clock.tick(60)
            else:
                self._render()
                self._clock.tick(60)

            self._handle_fist()
            self._collect()

    def _check_success(self):
        if self._level.player_succeeded():
            self._success = True

    def _check_fail(self):
        if self._level.player_dead():
            self._failed = True

    def _handle_player_movement(self):
        keys = pygame.key.get_pressed()

        self._level.player_movement()

        if keys[pygame.K_SPACE]:
            self._level.player.jumping = True

        if self._level.player.jumping:
            self._level.jump_player()

        if self._level.fist:
            self._level.set_fist()

    def _scroll_level(self):
        self._level.scroll_level()

    def _gravity(self):
        self._level.gravity()

    def _reset_values(self):
        self._failed = False
        self._success = False
        self._coins = 0
        self._stars = 0

    def _handle_events(self):
        for event in self._event_queue.get():
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_r:
                    self._level.restart_level()
                    self._reset_values()
                    pygame.mixer.music.play(-1)
                    return None
                if event.key == pygame.K_z:
                    self._level.player_attack()
                    return None
                if event.key == pygame.K_ESCAPE:
                    pygame.quit()
                return None
            if event.type == pygame.QUIT:
                return False
        return None

    def _render(self):
        self._renderer.render(self._coins, self._stars,
                              self._failed, self._success)

    def _render_introscreen(self):
        self._renderer.render_introscreen()

    def _handle_fist(self):
        self._level.handle_fist()

    def _collect(self):
        collected = self._level.collect()

        if collected == "Coin":
            self._coins += 1
        elif collected == "Star":
            self._stars += 1

    def _check_start(self):
        for event in self._event_queue.get():
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_RETURN:
                    return True
                if event.key == pygame.K_ESCAPE:
                    pygame.quit()
                    exit()
