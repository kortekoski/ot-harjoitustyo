import os
import pygame

dirname = os.path.dirname(__file__)

class Star(pygame.sprite.Sprite):
    def __init__(self, position):
        super().__init__()

        self.image = pygame.image.load(
            os.path.join(dirname, "..", "assets", "star.png")
        )

        self.rect = self.image.get_rect()

        self.rect.x = position[0]
        self.rect.y = position[1]

    def collect(self):
        self.kill()