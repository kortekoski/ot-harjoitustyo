import pygame


class Clock:
    """Controls the refresh rate of the game.

    Attributes:
        clock: A pygame Clock object for tracking time.
    """

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
        """Returns the time elapsed since the game was started, in milliseconds.

        Returns:
            int: Time since the game was started.
        """
        return pygame.time.get_ticks()
