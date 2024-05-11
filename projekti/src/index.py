import os
import pygame
import json

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

    with open("./src/assets/maps.json", "r") as file:
        read_file = json.load(file)

    level_maps = []
    for key in read_file:
        level_maps.append(read_file[key])

    height = len(level_maps[1])
    screen_height = height * CELL_SIZE
    screen_width = 10 * CELL_SIZE
    screen_center = (screen_width / 2, screen_height / 2)
    screen = pygame.display.set_mode((screen_width, screen_height))

    pygame.display.set_caption("Game")

    event_queue = EventQueue()
    renderer = Renderer(screen, screen_center)
    clock = Clock()
    database_service = DatabaseService()

    # Initialize the database if it doesn't exist yet
    current_directory = os.path.dirname(os.path.abspath(__file__))
    database_directory = os.path.join(current_directory, "database")
    database_file_path = os.path.join(database_directory, "save.db")
    if not os.path.exists(database_file_path):
        database_service.initialize()

    game_loop = GameLoop(level_maps, renderer, event_queue,
                         clock, database_service, CELL_SIZE)

    game_loop.start()


if __name__ == "__main__":
    main()
