import os
import unittest
import pygame
from database.db_service import DatabaseService


class TestDatabaseService(unittest.TestCase):
    def setUp(self):
        self.db_service = DatabaseService("test.db")

        self.db_service.initialize()
        self.db_service.reset()

    def test_get_slots(self):
        slots = self.db_service.get()
        self.assertEqual([(1, 0), (2, 0), (3, 0)], slots)

    def test_slot_progresses(self):
        self.db_service.progress_slot(1, 1)
        self.db_service.progress_slot(2, 2)

        slots = self.db_service._get_slots()

        self.assertEqual([(1, 1), (2, 2), (3, 0)], slots)

    def test_save_slot_clear(self):
        self.db_service.progress_slot(1, 1)
        self.db_service.clear_slot(1)

        slot_1 = self.db_service._get_slot_by_id(1)

        self.assertEqual((1, 0), slot_1)

    def test_correct_max_level(self):
        self.db_service.progress_slot(1, 2)
        max = self.db_service.max_level(1)

        self.assertEqual(2, max)

    def test_coins_and_stars_in_level_info_correct(self):
        info = self.db_service.level_info(1, 2)
        self.assertEqual((1, 1), info)

    def test_progress_in_level_info_correct(self):
        sql = "INSERT INTO SlotsLevels VALUES(1, 0, 1, 1)"
        self.db_service._execute_sql(sql)
        info = self.db_service.level_info(1, 0)
        self.assertEqual((1, 1, 1, 1), info)

    def test_getting_slotslevels_row_by_id(self):
        sql = "INSERT INTO SlotsLevels VALUES(1, 0, 1, 1)"
        self.db_service._execute_sql(sql)
        row = self.db_service.get_slotslevels_by_id(1, 0)
        self.assertEqual((1, 0, 1, 1), row)

    def test_updating_level_stats_on_first_attempt(self):
        self.db_service.update_stats(1, 0, 1, 1)
        row = self.db_service.get_slotslevels_by_id(1, 0)
        self.assertEqual((1, 0, 1, 1), row)

    def test_updating_level_stats_on_another_attempt(self):
        self.db_service.update_stats(1, 0, 0, 0)
        row = self.db_service.get_slotslevels_by_id(1, 0)
        self.assertEqual((1, 0, 0, 0), row)

        self.db_service.update_stats(1, 0, 1, 0)
        row = self.db_service.get_slotslevels_by_id(1, 0)
        self.assertEqual((1, 0, 1, 0), row)

        self.db_service.update_stats(1, 0, 0, 1)
        row = self.db_service.get_slotslevels_by_id(1, 0)
        self.assertEqual((1, 0, 1, 1), row)

        self.db_service.update_stats(1, 0, 0, 2)
        row = self.db_service.get_slotslevels_by_id(1, 0)
        self.assertEqual((1, 0, 1, 2), row)

        self.db_service.update_stats(1, 0, 3, 3)
        row = self.db_service.get_slotslevels_by_id(1, 0)
        self.assertEqual((1, 0, 3, 3), row)
