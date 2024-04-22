import os
import pygame

dirname = os.path.dirname(__file__)


class Player(pygame.sprite.Sprite):
    def __init__(self, position):
        super().__init__()

        self.image = pygame.image.load(
            os.path.join(dirname, "..", "assets", "dude.png")
        )

        self.rect = self.image.get_rect()

        self.rect.x = position[0]
        self.rect.y = position[1]

        self.move_speed = 300

        self.jumping = False
        self.sprint_jumping = False
        self.jump_height = 10
        self.jump_velocity = self.jump_height
        self.jump_gravity = 1

    def set_ms(self, x):
        self.move_speed = x

    def get_position(self):
        return (self.rect.x, self.rect.y)

    def is_jumping(self):
        if self.jumping or self.sprint_jumping:
            return True

        return False

    def reset_jumping(self):
        self.jumping = False
        self.sprint_jumping = False
        self.jump_height = 20
        self.jump_velocity = self.jump_height
