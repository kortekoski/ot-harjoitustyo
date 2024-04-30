import pygame


class EventQueue:
    """This class gets the pygame events needed for interacting with the game.
    """

    def get(self):
        """Gets interaction events from pygame.

        Returns:
            event: A pygame event.
        """
        return pygame.event.get()
