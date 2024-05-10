import pygame

from engine.clock import Clock
from engine.eventqueue import EventQueue
from engine.gameloop import GameLoop
from engine.renderer import Renderer
from database.db_service import DatabaseService

LEVEL_MAP = [[0, 0, 0, 0, 0, 5, 0, 0, 0, 0, 0, 0, 0, 0, 0, 8],
             [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 8],
             [0, 0, 0, 0, 1, 1, 0, 0, 0, 0, 0, 0, 6, 0, 0, 8],
             [0, 1, 4, 0, 0, 0, 0, 0, 2, 0, 0, 0, 2, 0, 0, 8],
             [0, 1, 1, 1, 0, 1, 1, 1, 1, 0, 1, 1, 1, 1, 1, 1]]

LEVEL_MAP_2 = [[0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 8],
               [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0,
                   0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 8],
               [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0,
                   0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 8],
               [0, 0, 0, 0, 4, 0, 0, 0, 0, 0, 0, 0, 0, 0,
                   0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 8],
               [1, 1, 1, 1, 1, 1, 1, 0, 1, 1, 0, 1, 1, 0, 1, 1, 1, 0, 1, 1, 1, 0, 1, 1, 1, 1, 1]]

LEVEL_MAP_3 = [[0, 0, 0, 0, 0, 5, 0, 0, 0, 0, 0, 0, 0, 0, 0, 8],
               [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 8],
               [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 6, 0, 0, 8],
               [0, 1, 4, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 8],
               [0, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1]]

level_maps = [LEVEL_MAP, LEVEL_MAP_2, LEVEL_MAP_3]
CELL_SIZE = 50


def main():
    pygame.init()
    pygame.mixer.init()
    pygame.mixer.music.set_volume(0.4)

    height = len(LEVEL_MAP_2)
    screen_height = height * CELL_SIZE
    screen_width = 10 * CELL_SIZE
    screen_center = (screen_width / 2, screen_height / 2)
    screen = pygame.display.set_mode((screen_width, screen_height))

    pygame.display.set_caption("Game")

    event_queue = EventQueue()
    renderer = Renderer(screen, screen_center)
    clock = Clock()
    database_service = DatabaseService()
    game_loop = GameLoop(level_maps, renderer, event_queue,
                         clock, database_service, CELL_SIZE)

    game_loop.start()


if __name__ == "__main__":
    main()
