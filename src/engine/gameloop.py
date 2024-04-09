import pygame

class GameLoop:
    def __init__(self, level, renderer, event_queue, clock, cell_size):
        self._level = level
        self._renderer = renderer
        self._event_queue = event_queue
        self._clock = clock
        self._cell_size = cell_size
        self.dt = 0

    def start(self):
        while True:
            if self._handle_events() == False:
                break
            
            self._handle_player_movement()
            self._gravity()

            self._render()

            self.dt = self._clock.tick(60) / 1000


    def _handle_player_movement(self):
        keys = pygame.key.get_pressed()
        if keys[pygame.K_LSHIFT] and not self._level.player.jumping:
            self._level.player.set_ms(600)
    
        if self._level.player.sprint_jumping:
            self._level.player.set_ms(600)

        if keys[pygame.K_LEFT]:
            self._level.move_player(-self._level.player.move_speed * self.dt)
        if keys[pygame.K_RIGHT]:
            self._level.move_player(self._level.player.move_speed * self.dt)
        if keys[pygame.K_UP]:
            self._level.move_player(0, -self._level.player.move_speed * self.dt)
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

    def _gravity(self):
        if not self._level.player.is_jumping():
            self._level.move_player(0, 2)

    def _handle_events(self):
        for event in self._event_queue.get():
            if event.type == pygame.KEYDOWN:
                # pause menu, restart level etc will be here
                pass
            elif event.type == pygame.QUIT:
                return False
            
    def _render(self):
        self._renderer.render()