import json
import pygame

from engine.clock import Clock
from engine.eventqueue import EventQueue
from engine.gameloop import GameLoop
from engine.renderer import Renderer
from database.db_service import DatabaseService

CELL_SIZE = 50

def main():
    pygame.init()
    pygame.mixer.init()
    pygame.mixer.music.set_volume(0.4)

    with open("./src/assets/maps.json", "r", encoding="utf-8") as file:
        read_file = json.load(file)

    level_maps = [read_file[key] for key in read_file]

    height = len(level_maps[1])
    screen_height = height * CELL_SIZE
    screen_width = 10 * CELL_SIZE
    screen_center = (screen_width / 2, screen_height / 2)
    screen = pygame.display.set_mode((screen_width, screen_height))

    pygame.display.set_caption("Game")

    event_queue = EventQueue()
    renderer = Renderer(screen, screen_center)
    clock = Clock()
    database_service = DatabaseService("save.db")
    database_service.initialize()

    game_loop = GameLoop(level_maps, renderer, event_queue,
                         clock, database_service, CELL_SIZE)

    game_loop.start()


if __name__ == "__main__":
    main()
