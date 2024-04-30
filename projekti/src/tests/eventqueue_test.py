import unittest
import pygame
from engine.eventqueue import EventQueue


class TestEventQueue(unittest.TestCase):
    def setUp(self):
        pygame.init()
        self.eventqueue = EventQueue()

    def test_events_are_returned(self):
        self.assertIsNotNone(self.eventqueue.get())
