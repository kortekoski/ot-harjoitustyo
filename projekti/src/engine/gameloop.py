import os
import sys
import pygame

from levels.level import Level

dirname = os.path.dirname(__file__)


class GameLoop:
    """This class contains the logic running the game, i.e. the *game loop*. 

    Attributes:
        level_maps: All the levels in the game.
        level: The level that is currently selected.
        renderer: Controls the display, draws sprites on the screen.
        event_queue: Gets the events (e.g. button presses) from the pygame events.
        clock: Controls the refresh rate of the game.
        cell_size: The size of the cells in the level, in pixels.
        db_service: Handles communication with the database storing saves.
        failed: If the player has failed a level.
        success: If the player has succeeded in a level.
        coins: How many coins have been collected.
        stars: How many stars have been collected.
        slot: The chosen save slot.
        chosen_level: The currently chosen level number in the menu.
        max_level: Biggest unlocked level number.
        dt: Delta time, the time elapsed since the previous tick of the clock.
    """

    def __init__(self, level_maps, renderer, event_queue, clock, db_service, cell_size):
        """Creates a new gameloop instance.

        Args:
            level_maps (list): All the levels in the game.
            renderer (Renderer): Controls the display, draws sprites on the screen.
            event_queue (EventQueue): Gets the events (e.g. button presses) from the pygame events.
            clock (Clock): Controls the refresh rate of the game.
            cell_size (int): The size of the cells in the level, in pixels.
        """
        self._level_maps = level_maps
        self._level = None
        self._renderer = renderer
        self._event_queue = event_queue
        self._clock = clock
        self._cell_size = cell_size
        self._db_service = db_service

        # These could be moved to a class called "State" or something
        self._failed = False
        self._success = False
        self._paused = False
        self._coins = 0
        self._stars = 0
        self._slot = 1
        self._in_slot_menu = True

        self._chosen_level = 0
        self._max_level = 0

        self.dt = 0

    def start(self):
        """Starts and plays the game.

        The three loops are as follows: 1. intro screen, 2. menu, 3. level.
        The menu and level loops are contained in one big loop, 
        since movement occurs between the two views.
        """
        # Intro screen loop
        while True:
            if self._check_start():
                break

            self._render_introscreen()
            self._clock.tick(60)

        # Save slot select loop
        self._save_slot_loop()

        while True:

            # Menu or level select loop
            while True:
                if self._handle_menu_events():
                    break
                level_info = self._db_service.level_info(
                    self._slot, self._chosen_level)
                self._render_menu(self._chosen_level, level_info)
                self.dt = self._clock.tick(60)

            self._level = Level(
                self._level_maps[self._chosen_level], self._cell_size)
            self._renderer.set_level(self._level)

            self._play_music()

            # Level loop
            while True:
                events = self._handle_events()

                if events is False:
                    break

                # Returns to the level select menu if the level is cleared and enter is pressed.
                if events is True and self._success is True:
                    self._update_database()
                    self._reset_level()
                    break

                # The game logic is mostly here: what happens when the level is being played.
                if not self._failed and not self._success:
                    self._main_loop()
                else:
                    self._render()
                    self._clock.tick(60)

                self._handle_fist()
                self._collect()

    def _play_music(self):
        pygame.mixer.music.load(os.path.join(
            dirname, "..", "assets", "test_track.mp3"))
        pygame.mixer.music.play(-1)

    def _main_loop(self):
        if self._paused:
            self._render_pause()
        else:
            self._gravity()
            self._handle_player_movement()
            self._scroll_level(self.dt)

            self._check_success()
            self._check_fail()

            self._render()

        self.dt = self._clock.tick(60)

    def _check_success(self):
        if self._level.player_succeeded():
            self._success = True

    def _check_fail(self):
        if self._level.player_dead():
            self._failed = True

    def _update_database(self):
        """Sends level clear data to the database.
        First the maximum selectable level is increased, if possible.
        The max level is fetched from the database to update it in the game.
        Then the collectible info is stored.
        """
        if self._chosen_level < len(self._level_maps) - 1:
            self._db_service.progress_slot(self._slot, self._chosen_level+1)
            self._max_level = self._db_service.max_level(self._slot)

        self._db_service.update_stats(
            self._slot, self._chosen_level, self._coins, self._stars)

    def _handle_player_movement(self):
        keys = pygame.key.get_pressed()

        self._level.player_movement()

        if keys[pygame.K_SPACE]:
            self._level.player.jumping = True

        if self._level.player.jumping:
            self._level.jump_player(keys[pygame.K_SPACE])

        if self._level.fist:
            self._level.set_fist()

    def _scroll_level(self, delta_time):
        self._level.scroll_level(delta_time)

    def _gravity(self):
        self._level.gravity()

    def _reset_values(self):
        self._failed = False
        self._success = False
        self._coins = 0
        self._stars = 0

    def _reset_level(self):
        self._reset_values()
        pygame.mixer.music.stop()
        self._level.nuke()
        self._level = None
        self._paused = False

    def _handle_menu_events_arrows(self, event):
        if event.key == pygame.K_LEFT:
            if self._chosen_level > 0:
                self._chosen_level -= 1

            if self._in_slot_menu:
                if self._slot > 1:
                    self._slot -= 1

        if event.key == pygame.K_RIGHT:
            if self._chosen_level < self._max_level:
                self._chosen_level += 1
            if self._in_slot_menu:
                if self._slot < 3:
                    self._slot += 1

    def _handle_menu_events(self):
        for event in self._event_queue.get():
            if event.type == pygame.KEYDOWN:
                self._handle_menu_events_arrows(event)
                if event.key == pygame.K_RETURN:
                    return True
                if not self._in_slot_menu and event.key == pygame.K_BACKSPACE:
                    self._save_slot_loop()
                if self._in_slot_menu and event.key == pygame.K_DELETE:
                    self._delete_slot_loop()
                if event.key == pygame.K_ESCAPE:
                    pygame.quit()
                    sys.exit()
            return None
        return None

    def _handle_events(self):
        for event in self._event_queue.get():
            if event.type == pygame.KEYDOWN:
                return self._handle_events_keys(event)
            if event.type == pygame.QUIT:
                return False
        return None

    def _handle_prz(self, event):
        if event.key == pygame.K_p:
            self._toggle_pause()
        if event.key == pygame.K_r:
            self._level.restart_level()
            self._reset_values()
            pygame.mixer.music.play(-1)
        if event.key == pygame.K_z:
            self._level.player_attack()

    def _handle_events_keys(self, event):
        self._handle_prz(event)
        if event.key == pygame.K_ESCAPE:
            if self._paused:
                self._toggle_pause()
                return False
            if self._failed:
                self._reset_level()
                return False

            pygame.quit()
        if event.key == pygame.K_RETURN:
            return True
        return None

    def _render(self):
        self._renderer.render(self._coins, self._stars,
                              self._failed, self._success)

    def _render_introscreen(self):
        self._renderer.render_introscreen()

    def _render_menu(self, chosen_level, level_info):
        self._renderer.render_menu(chosen_level, level_info)

    def _render_slotscreen(self, slot):
        self._renderer.render_slotscreen(slot)

    def _render_pause(self):
        self._renderer.render_pause()

    def _handle_fist(self):
        self._level.handle_fist()

    def _collect(self):
        collected = self._level.collect()

        if collected == "Coin":
            self._coins += 1
        elif collected == "Star":
            self._stars += 1

    def _check_start(self):
        for event in self._event_queue.get():
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_RETURN:
                    return True
                if event.key == pygame.K_ESCAPE:
                    pygame.quit()
                    sys.exit()
                return None
        return None

    def _toggle_pause(self):
        if self._paused:
            self._paused = False
        else:
            self._paused = True

    def _toggle_slot_menu(self):
        if self._in_slot_menu:
            self._in_slot_menu = False
        else:
            self._in_slot_menu = True

    def _save_slot_loop(self):
        self._in_slot_menu = True

        while True:
            if self._handle_menu_events():
                break

            self._render_slotscreen(self._slot)
            self._clock.tick(60)

        self._in_slot_menu = False
        self._max_level = self._db_service.max_level(self._slot)
        self._chosen_level = 0

    def _handle_deletion_events(self):
        for event in self._event_queue.get():
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_RETURN:
                    return True
                if event.key == pygame.K_BACKSPACE:
                    return False
                if event.key == pygame.K_ESCAPE:
                    pygame.quit()
                    sys.exit()
            return None
        return None

    def _delete_slot_loop(self):
        while True:
            returned = self._handle_deletion_events()
            if returned is True:
                self._db_service.clear_slot(self._slot)
                break
            if returned is False:
                break

            self._renderer.render_delete_slotscreen(self._slot)
            self._clock.tick(60)
