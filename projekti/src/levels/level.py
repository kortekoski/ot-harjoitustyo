import pygame
from sprites.player import Player
from sprites.platform import Platform
from sprites.obstacle import Obstacle
from sprites.background import Background
from sprites.coin import Coin
from sprites.star import Star
from sprites.fist import Fist


class Level:
    def __init__(self, level_map, cell_size):
        self.cell_size = cell_size
        self.level_map = level_map
        self.player = None
        self.fist = None
        self.platforms = pygame.sprite.Group()
        self.obstacles = pygame.sprite.Group()
        self.coins = pygame.sprite.Group()
        self.stars = pygame.sprite.Group()
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
                elif cell == 2:
                    self.backgrounds.add(Background((normalized_x, normalized_y)))
                    self.obstacles.add(Obstacle((normalized_x, normalized_y)))
                elif cell == 4:
                    self.player = Player((normalized_x, normalized_y))
                    self.backgrounds.add(Background(
                        (normalized_x, normalized_y)))
                elif cell == 5:
                    self.backgrounds.add(Background(
                        (normalized_x, normalized_y)))
                    self.coins.add(Coin((normalized_x, normalized_y)))
                elif cell == 6:
                    self.backgrounds.add(Background(
                        (normalized_x, normalized_y)))
                    self.stars.add(Star((normalized_x, normalized_y)))

        self.all_sprites.add(
            self.backgrounds,
            self.platforms,
            self.obstacles,
            self.coins,
            self.stars,
            self.player
        )

    def restart_level(self):
        for sprite in self.all_sprites:
            sprite.kill()

        self._initialize_sprites(self.level_map)

    def move_player(self, dx=0, dy=0):
        if not self._player_can_move(dx, dy):
            return

        self.player.rect.move_ip(dx, dy)

    def _player_can_move(self, x=0, y=0):
        self.player.rect.move_ip(x, y)

        colliding_platforms = pygame.sprite.spritecollide(
            self.player, self.platforms, False)
        
        colliding_obstacles = pygame.sprite.spritecollide(
            self.player, self.obstacles, False
        )

        can_move = not colliding_platforms and not colliding_obstacles

        self.player.rect.move_ip(-x, -y)
        return can_move

    def _get_colliding_platforms(self, x=0, y=0):
        self.player.rect.move_ip(x, y)

        colliding_platform = pygame.sprite.spritecollide(
            self.player, self.platforms, False)
        
        return colliding_platform
    
    def _get_colliding_obstacles(self, x=0, y=0):
        self.player.rect.move_ip(x, y)

        colliding_obstacle = pygame.sprite.spritecollide(
            self.player, self.obstacles, False)
        
        return colliding_obstacle

    def jump_player(self):
        if self._player_can_move(0, -self.player.jump_velocity):
            self.player.rect.y -= self.player.jump_velocity
        else:
            colliding_obstacles = self._get_colliding_obstacles(
                0, -self.player.jump_velocity)
            colliding_platforms = self._get_colliding_platforms(
                0, -self.player.jump_velocity)

            if colliding_obstacles:
                obstacle = colliding_obstacles[0]
                if obstacle.rect.y < self.player.rect.y:
                    self.player.rect.top = obstacle.rect.bottom
                else:
                    self.player.rect.bottom = obstacle.rect.top
            else:
                colliding_platform = colliding_platforms[0]
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
            colliding_obstacles = self._get_colliding_obstacles(
                0, self.g)
            colliding_platforms = self._get_colliding_platforms(
                0, self.g)
            
            if colliding_obstacles:
                obstacle = colliding_obstacles[0]
                self.player.rect.bottom = obstacle.rect.top
            else:
                colliding_platform = colliding_platforms[0]
                self.player.rect.bottom = colliding_platform.rect.top

            self.player.reset_jumping()

    def player_fallen(self):
        if self.player.rect.y > len(self.level_map) * self.cell_size:
            return True
        return False

    def player_succeeded(self):
        if self.player.rect.x > len(self.level_map[0]) * self.cell_size:
            return True
        return False
    
    def player_attack(self):
        x = self.player.rect.x + self.cell_size
        y = self.player.rect.y
        self.fist = Fist((x, y))
        self.all_sprites.add(self.fist)
    
    def handle_fist(self):
        if self.fist:
            if self.fist.get_lifetime() > 0:
                self.fist.tick()
                
                hit_obstacles = pygame.sprite.spritecollide(
                    self.fist, self.obstacles, False
                )

                if hit_obstacles:
                    hitted = hit_obstacles[0]
                    hitted.kill()
            else:
                self.fist.kill()

    def set_fist(self):
        self.fist.set_coordinates(
            self.player.rect.x + self.cell_size, self.player.rect.y
        )
    
    def _collided_sprites(self, moving_object, static_objects):
        hit_objects = pygame.sprite.spritecollide(
            moving_object, static_objects, False
        )

        return hit_objects

    def collect(self):
        coins = self._collided_sprites(self.player, self.coins)
        stars = self._collided_sprites(self.player, self.stars)

        if coins:
            coins[0].kill()
            return "Coin"
        
        if stars:
            stars[0].kill()
            return "Star"
        
        return None