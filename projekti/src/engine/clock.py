import pygame


class Clock:
    def __init__(self):
        self._clock = pygame.time.Clock()

    def tick(self, fps):
        """
        Computes how many milliseconds have passed
        since the previous call.

        Args:
            fps: Frames per second, i.e. how often the screen should be "refreshed".

        Returns:
            The amount of milliseconds since the previous call.
        """
        delta_time = self._clock.tick_busy_loop(fps)
        return delta_time

    def get_ticks(self):
        return pygame.time.get_ticks()
