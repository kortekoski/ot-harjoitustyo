import pygame


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

        self.dt = 0

    def start(self):
        while True:
            self._render_introscreen()

            if self._check_start() is True:
                break

        while True:
            if self._handle_events() is False:
                break

            if not self._failed and not self._success:
                self._handle_player_movement()
                self._gravity()

                self._check_success()
                self._check_fail()

                self._render()

                self.dt = self._clock.tick(60) / 1000
            else:
                self._render()

            self._handle_fist()
            self._collect()

    def _check_success(self):
        if self._level.player_succeeded():
            self._success = True

    def _check_fail(self):
        if self._level.player_fallen():
            self._failed = True

    def _set_sprintspeed(self, keys):
        if keys[pygame.K_LSHIFT] and not self._level.player.jumping:
            self._level.player.set_ms(600)

        if self._level.player.sprint_jumping:
            self._level.player.set_ms(600)

    def _handle_player_movement(self):
        keys = pygame.key.get_pressed()
        self._set_sprintspeed(keys)

        self._move_player(keys)

        if not self._level.player.sprint_jumping:
            self._level.player.set_ms(300)

        if keys[pygame.K_SPACE]:
            self._level.player.jumping = True

        if keys[pygame.K_SPACE] and keys[pygame.K_LSHIFT]:
            self._level.player.sprint_jumping = True

        if self._level.player.jumping:
            self._level.jump_player()

        if self._level.fist:
            self._level.set_fist()

    def _move_player(self, keys):
        if keys[pygame.K_LEFT]:
            self._level.move_player(-self._level.player.move_speed * self.dt)
        if keys[pygame.K_RIGHT]:
            self._level.move_player(self._level.player.move_speed * self.dt)

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
