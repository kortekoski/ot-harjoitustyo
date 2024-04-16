import os
import pygame

dirname = os.path.dirname(__file__)


class Fist(pygame.sprite.Sprite):
    def __init__(self, position):
        super().__init__()

        self.image = pygame.image.load(
            os.path.join(dirname, "..", "assets", "fist.png")
        )

        self.rect = self.image.get_rect()

        self.rect.x = position[0]
        self.rect.y = position[1]

        self.lifetime = 9

    def tick(self):
        self.lifetime -= 1

    def get_lifetime(self):
        return self.lifetime

    def set_coordinates(self, x, y):
        self.rect.x = x
        self.rect.y = y
