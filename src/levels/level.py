import pygame
from sprites.player import Player
from sprites.platform import Platform
from sprites.background import Background

class Level:
    def __init__(self, level_map, cell_size):
        self.cell_size = cell_size
        self.player = None
        self.platforms = pygame.sprite.Group()
        self.backgrounds = pygame.sprite.Group()

        self.all_sprites = pygame.sprite.Group()

        self._initialize_sprites(level_map)

    def _initialize_sprites(self, level_map):
        height = len(level_map)
        width = len(level_map[0])

        for y in range(height):
            for x in range(width):
                cell = level_map[y][x]
                normalized_x = x * self.cell_size
                normalized_y = y * self.cell_size

                if cell == 0:
                    self.backgrounds.add(Background((normalized_x, normalized_y)))
                elif cell == 1:
                    self.platforms.add(Platform((normalized_x, normalized_y)))
                elif cell == 4:
                    self.player = Player((normalized_x, normalized_y))
                    self.backgrounds.add(Background((normalized_x, normalized_y)))
        
        self.all_sprites.add(
            self.backgrounds,
            self.platforms,
            self.player
        )

    def move_player(self, dx=0, dy=0):
        if not self._player_can_move(dx, dy):
            return
        
        self.player.rect.move_ip(dx, dy)

    def _player_can_move(self, x=0, y=0):
        self.player.rect.move_ip(x, y)

        colliding_platforms = pygame.sprite.spritecollide(self.player, self.platforms, False)
        can_move = not colliding_platforms

        self.player.rect.move_ip(-x, -y)
        return can_move
    
    def _check_jump(self, y):
        x = self.rect.x
        self.player.rect.move_ip(x, y)
    
    def jump_player(self):
        # y-koordista vähennetään velocity -> kun velocity on alle nollan, y-koord lisäänty eli pallo putoaa
        # velocitystyä vähennetään gravity
        # loppuu kun velocity on pienempi kuin -korkeus (eli lähtöpiste on saavutettu)

        if self._player_can_move(0, -self.player.jump_velocity):
            self.player.rect.y -= self.player.jump_velocity
        else:
            print("COLLIDING")
        
        self.player.jump_velocity -= self.player.jump_gravity
        
        if self.player.jump_velocity < -self.player.jump_height:
            
            self.player.jumping = False
            self.player.sprint_jumping = False
            self.player.jump_velocity = self.player.jump_height