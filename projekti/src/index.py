import pygame
from sprites.player import Player
from sprites.platform import Platform

from levels.level import Level

from engine.clock import Clock
from engine.eventqueue import EventQueue
from engine.gameloop import GameLoop
from engine.renderer import Renderer

LEVEL_MAP = [[0, 0, 0, 0, 0, 0],
             [0, 0, 0, 0, 0, 0],
             [0, 0, 0, 0, 1, 1],
             [0, 1, 4, 0, 0, 0],
             [0, 1, 1, 1, 0, 0]]

CELL_SIZE = 50 

def main():
    height = len(LEVEL_MAP)
    width = len(LEVEL_MAP[0])
    screen_height = height * CELL_SIZE
    screen_width = width * CELL_SIZE
    screen = pygame.display.set_mode((screen_width, screen_height))

    pygame.display.set_caption("Game")

    level = Level(LEVEL_MAP, CELL_SIZE)
    event_queue = EventQueue()
    renderer = Renderer(screen, level)
    clock = Clock()
    game_loop = GameLoop(level, renderer, event_queue, clock, CELL_SIZE)

    pygame.init()
    game_loop.start()

if __name__ == "__main__":
    main()