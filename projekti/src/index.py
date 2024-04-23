import pygame

from levels.level import Level

from engine.clock import Clock
from engine.eventqueue import EventQueue
from engine.gameloop import GameLoop
from engine.renderer import Renderer

LEVEL_MAP = [[0, 0, 0, 0, 0, 5, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
             [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
             [0, 0, 0, 0, 1, 1, 0, 0, 0, 0, 0, 0, 6, 0, 0, 0],
             [0, 1, 4, 0, 0, 0, 0, 0, 2, 0, 0, 0, 2, 0, 0, 0],
             [0, 1, 1, 1, 0, 1, 1, 1, 1, 0, 1, 1, 1, 1, 1, 1]]

LEVEL_MAP_2 = [[0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 8],
               [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0,
                   0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 8],
               [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0,
                   0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 8],
               [0, 0, 0, 0, 4, 0, 0, 0, 0, 0, 0, 0, 0, 0,
                   0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 8],
               [1, 1, 1, 1, 1, 1, 1, 1, 0, 1, 1, 0, 1, 1, 0, 1, 1, 1, 0, 0, 1, 1, 1, 0, 0, 1, 1]]

CELL_SIZE = 50


def main():
    pygame.init()
    pygame.mixer.init()

    height = len(LEVEL_MAP_2)
    width = len(LEVEL_MAP_2[0])
    screen_height = height * CELL_SIZE
    screen_width = 10 * CELL_SIZE
    screen_scroll_threshold = screen_width / 2
    screen_center = (screen_width / 2, screen_height / 2)
    screen = pygame.display.set_mode((screen_width, screen_height))

    pygame.display.set_caption("Game")

    level = Level(LEVEL_MAP_2, CELL_SIZE, screen_scroll_threshold)
    event_queue = EventQueue()
    renderer = Renderer(screen, level, screen_center)
    clock = Clock()
    game_loop = GameLoop(level, renderer, event_queue, clock, CELL_SIZE)

    game_loop.start()


if __name__ == "__main__":
    main()
