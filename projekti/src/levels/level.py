import pygame
from sprites.player import Player
from sprites.platform import Platform
from sprites.background import Background


class Level:
    def __init__(self, level_map, cell_size):
        self.cell_size = cell_size
        self.level_map = level_map
        self.player = None
        self.platforms = pygame.sprite.Group()
        self.backgrounds = pygame.sprite.Group()
        self.g = 5

        self.all_sprites = pygame.sprite.Group()

        self._initialize_sprites(self.level_map)

    def get_center(self):
        normalized_x = len(self.level_map[0]) * self.cell_size
        normalized_y = len(self.level_map) * self.cell_size

        return (normalized_x / 2, normalized_y / 2)

    def _initialize_sprites(self, level_map):
        height = len(level_map)
        width = len(level_map[0])

        for y in range(height):
            for x in range(width):
                cell = level_map[y][x]
                normalized_x = x * self.cell_size
                normalized_y = y * self.cell_size

                if cell == 0:
                    self.backgrounds.add(Background(
                        (normalized_x, normalized_y)))
                elif cell == 1:
                    self.platforms.add(Platform((normalized_x, normalized_y)))
                elif cell == 4:
                    self.player = Player((normalized_x, normalized_y))
                    self.backgrounds.add(Background(
                        (normalized_x, normalized_y)))

        self.all_sprites.add(
            self.backgrounds,
            self.platforms,
            self.player
        )

    def restart_level(self):
        self._initialize_sprites(self.level_map)

    def move_player(self, dx=0, dy=0):
        if not self._player_can_move(dx, dy):
            return

        self.player.rect.move_ip(dx, dy)

    def _player_can_move(self, x=0, y=0):
        self.player.rect.move_ip(x, y)

        colliding_platforms = pygame.sprite.spritecollide(
            self.player, self.platforms, False)

        can_move = not colliding_platforms

        self.player.rect.move_ip(-x, -y)
        return can_move

    def _get_colliding_platform(self, x=0, y=0):
        self.player.rect.move_ip(x, y)

        colliding_platform = pygame.sprite.spritecollide(
            self.player, self.platforms, False)[0]
        
        return colliding_platform

    def jump_player(self):
        if self._player_can_move(0, -self.player.jump_velocity):
            self.player.rect.y -= self.player.jump_velocity
        else:
            colliding_platform = self._get_colliding_platform(
                0, -self.player.jump_velocity)
            if colliding_platform.rect.y < self.player.rect.y:
                self.player.rect.top = colliding_platform.rect.bottom
            else:
                self.player.rect.bottom = colliding_platform.rect.top

        self.player.jump_velocity -= self.player.jump_gravity

        if self.player.jump_velocity < -self.player.jump_height:
            self.player.jumping = False
            self.player.sprint_jumping = False
            self.player.jump_velocity = self.player.jump_height

    def gravity(self):
        if self._player_can_move(0, self.g):
            self.player.rect.y += self.g
        else:
            print("COLLISION")
            colliding_platform = self._get_colliding_platform(
                0, self.g)
            self.player.rect.bottom = colliding_platform.rect.top

    def player_fallen(self):
        if self.player.rect.y > len(self.level_map) * self.cell_size:
            return True
        return False

    def player_succeeded(self):
        if self.player.rect.x > len(self.level_map[0]) * self.cell_size:
            return True
        return False
    