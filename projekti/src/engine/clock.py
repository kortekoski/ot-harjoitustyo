import pygame


class Clock:
    def __init__(self):
        self._clock = pygame.time.Clock()

    def tick(self, fps):
        dt = self._clock.tick(fps)
        return dt

    def get_ticks(self):
        return pygame.time.get_ticks()
