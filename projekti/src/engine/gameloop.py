import pygame


class GameLoop:
    def __init__(self, level, renderer, event_queue, clock, cell_size):
        self._level = level
        self._renderer = renderer
        self._event_queue = event_queue
        self._clock = clock
        self._cell_size = cell_size

        self._failed = False
        self._success = False

        self.dt = 0

    def start(self):
        while True:
            if self._handle_events() is False:
                break

            if not self._failed:
                self._handle_player_movement()
                self._gravity()

                self._check_success()
                self._check_fail()

                self._render()

                self.dt = self._clock.tick(60) / 1000
            elif self._success:
                self._render_success()
            else:
                self._render_fail()

            self._handle_fist()

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

        if keys[pygame.K_LEFT]:
            self._level.move_player(-self._level.player.move_speed * self.dt)
        if keys[pygame.K_RIGHT]:
            self._level.move_player(self._level.player.move_speed * self.dt)
        if keys[pygame.K_UP]:
            self._level.move_player(
                0, -self._level.player.move_speed * self.dt)
        if keys[pygame.K_DOWN]:
            self._level.move_player(0, self._level.player.move_speed * self.dt)

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

    def _gravity(self):
        self._level.gravity()

    def _handle_events(self):
        for event in self._event_queue.get():
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_r:
                    self._level.restart_level()
                    self._failed = False
                    self._success = False
                    return None
                if event.key == pygame.K_z:
                    self._level.player_attack()
                    return None
                return None
            if event.type == pygame.QUIT:
                return False
        return None

    def _render(self):
        self._renderer.render()

    def _render_fail(self):
        self._renderer.render_text("FAILED, press R to restart")

    def _render_success(self):
        self._renderer.render_text("SUCCESS!!")

    def _handle_fist(self):
        self._level.handle_fist()