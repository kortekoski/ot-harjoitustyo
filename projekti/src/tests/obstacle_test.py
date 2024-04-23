import unittest
import pygame
from sprites.obstacle import Obstacle


class TestObstacle(unittest.TestCase):
    def setUp(self):
        self.obstacle = Obstacle((50, 50))
        self.obstacles = pygame.sprite.Group()

    def test_obstacle_dies_when_killed(self):
        self.obstacles.add(self.obstacle)
        self.obstacle.destroy()
        self.assertNotIn(self.obstacle, self.obstacles)
