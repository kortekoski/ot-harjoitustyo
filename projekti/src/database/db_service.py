import os
import sqlite3


class DatabaseService:
    """Saves progress in the game.

    Attributes:
        connection: The connection to the sqlite3 database.
        cursor: Handles database commands.
    """

    def __init__(self, db_filename):
        """Creates a new database service instance.

        The first two lines ensures that the database file is created
        in this directory.
        """
        current_directory = os.path.dirname(os.path.abspath(__file__))
        database_file_path = os.path.join(current_directory, db_filename)

        connection = sqlite3.connect(database_file_path)
        self.connection = connection
        self.cursor = connection.cursor()

    def _execute_sql(self, sql):
        self.cursor.execute(sql)
        self.connection.commit()

    def initialize(self):
        """Initializes the database tables."""
        sql = [
            """CREATE TABLE IF NOT EXISTS Levels(
            id INTEGER PRIMARY KEY, 
            coins INTEGER, 
            stars INTEGER
        )""",
            """CREATE TABLE IF NOT EXISTS Slots(
            id INTEGER PRIMARY KEY, 
            current_level INTEGER REFERENCES Levels
        )""",
            """CREATE TABLE IF NOT EXISTS SlotsLevels(
            slot_id INTEGER REFERENCES Slots,
            level_id INTEGER REFERENCES Levels,
            coins_collected INTEGER,
            stars_collected INTEGER
        )"""
        ]

        for s in sql:
            self.cursor.execute(s)

        self.connection.commit()

        slots = self._get_slots()
        if not slots:
            insert_sql = ["""INSERT INTO Levels VALUES(0, 1, 1), (1, 0, 0), (2, 1, 1),
                             (3, 1, 1), (4, 2, 2), (5, 2, 2)""",
                          "INSERT INTO Slots VALUES(1, 0), (2, 0), (3, 0)"]
            for s in insert_sql:
                self.cursor.execute(s)

        self.connection.commit()

    def reset(self):
        """Drops all tables and re-initalizes the database.
        """
        sql = ["DROP TABLE SlotsLevels",
               "DROP TABLE Slots",
               "DROP TABLE Levels"]

        for s in sql:
            self._execute_sql(s)

        self.initialize()

    def progress_slot(self, slot_id, new_level):
        """Changes the current level on the save slot if the parameter is bigger.

        Args:
            slot_id: Id of the save slot.
            new_level: The level that could be unlocked.
        """
        current_level = self._get_slot_by_id(slot_id)[1]
        if new_level > current_level:
            sql = f"UPDATE Slots SET current_level={new_level} WHERE id={slot_id}"
            self._execute_sql(sql)

    def clear_slot(self, slot_id):
        """Clears a save slot of all progress.

        Args:
            slot_id: ID of the slot that should be cleared.
        """
        sql = f"DELETE FROM SlotsLevels WHERE slot_id={slot_id}"
        self._execute_sql(sql)
        sql = f"UPDATE Slots SET current_level=0 WHERE id={slot_id}"
        self._execute_sql(sql)

    def _get_slots(self):
        sql = "SELECT * FROM Slots"
        response = self.cursor.execute(sql)
        return response.fetchall()

    def get(self):
        sql = "SELECT * FROM Slots"
        response = self.cursor.execute(sql)
        return response.fetchall()

    def _get_levels(self):
        sql = "SELECT * FROM Levels"
        response = self.cursor.execute(sql)
        return response.fetchall()

    def _get_slot_by_id(self, slot_id):
        sql = f"SELECT * FROM Slots WHERE id={slot_id}"
        response = self.cursor.execute(sql)
        return response.fetchone()

    def max_level(self, slot_id):
        """Determines the maximum unlocked level in the save.

        Args:
            slot_id: ID for the desired save slot.

        Returns:
            integer: Maximum unlocked level id.
        """
        sql = f"SELECT current_level FROM Slots WHERE id={slot_id}"
        response = self.cursor.execute(sql)
        level_id = response.fetchone()
        return level_id[0]

    def level_info(self, slot_id, level_id):
        """Returns the max coins and stars in the level + the amount collected on the save."""
        sql = f"""SELECT Levels.coins, Levels.stars,
             SlotsLevels.coins_collected, SlotsLevels.stars_collected 
            FROM Levels LEFT JOIN SlotsLevels ON Levels.id = SlotsLevels.level_id
            WHERE SlotsLevels.slot_id={slot_id} AND SlotsLevels.level_id={level_id}"""
        response = self.cursor.execute(sql)
        result = response.fetchone()

        if result is not None:
            return result

        sql2 = f"SELECT coins, stars FROM Levels WHERE id={level_id}"
        response2 = self.cursor.execute(sql2)
        result2 = response2.fetchone()

        return result2

    def get_slotslevels_by_id(self, slot_id, level_id):
        sql = f"SELECT * FROM SlotsLevels WHERE slot_id={slot_id} AND level_id={level_id}"
        response = self.cursor.execute(sql)
        return response.fetchone()

    def update_stats(self, slot_id, level_id, coins, stars):
        """Updates the collected coins and stars in the level on the save slot.

        If no row is found with the slot and level ids, a new row is added.
        If a row is found, it's updated if the new values are larger than the saved ones.
        """
        if not self.get_slotslevels_by_id(slot_id, level_id):
            sql = f"INSERT INTO SlotsLevels VALUES({slot_id}, {level_id}, {coins}, {stars})"
            self._execute_sql(sql)
        else:
            old_stats = self.get_slotslevels_by_id(slot_id, level_id)
            if coins > old_stats[2] and stars > old_stats[3]:
                sql = f"""UPDATE SlotsLevels
                    SET coins_collected={coins}, stars_collected={stars}
                    WHERE slot_id={slot_id} AND level_id={level_id}
                """
                self._execute_sql(sql)
            elif coins > old_stats[2] and stars <= old_stats[3]:
                sql = f"""UPDATE SlotsLevels
                    SET coins_collected={coins}
                    WHERE slot_id={slot_id} AND level_id={level_id}
                """
                self._execute_sql(sql)
            elif coins <= old_stats[2] and stars > old_stats[3]:
                sql = f"""UPDATE SlotsLevels
                    SET stars_collected={stars}
                    WHERE slot_id={slot_id} AND level_id={level_id}
                """
                self._execute_sql(sql)
                