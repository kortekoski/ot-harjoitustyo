import unittest
from sprites.fist import Fist


class TestFist(unittest.TestCase):
    def setUp(self):
        self.fist = Fist((50, 50))

    def test_fist_exist(self):
        self.assertEqual((50, 50), (self.fist.rect.x, self.fist.rect.y))
    
    def test_fist_alive(self):
        self.assertEqual(9, self.fist.get_lifetime())

    def test_fist_lifetime_ticks_down(self):
        starting_lifetime = self.fist.get_lifetime()
        self.fist.tick()
        ending_lifetime = self.fist.get_lifetime()
        self.assertEqual(ending_lifetime, starting_lifetime-1)

    def test_fist_move(self):
        self.fist.set_coordinates(100, 100)
        self.assertEqual((100, 100), (self.fist.rect.x, self.fist.rect.y))