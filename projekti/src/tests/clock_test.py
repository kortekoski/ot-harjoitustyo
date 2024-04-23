import unittest
from engine.clock import Clock


class TestClock(unittest.TestCase):
    def setUp(self):
        self.clock = Clock()

    def test_tick_returns_delta(self):
        dt = self.clock.tick(60)
        self.assertIsNotNone(dt)

    def test_get_ticks_returns_ticks(self):
        ticks = self.clock.get_ticks()
        self.assertIsNotNone(ticks)
