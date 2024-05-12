import pygame

BLACK = (0, 0, 0)
WHITE = (255, 255, 255)


class Renderer:
    """Controls the display window and draws sprites on it.

    Attributes:
        display: 
    """

    def __init__(self, display, center, level=None):
        """Generates a new Renderer instance.

        Args:
            display: A pygame display which contains all graphical elements of the game.
            center: The coordinates for the center of the display as a tuple.
            level: The level that should be rendered on screen. Defaults to None.
        """
        self._display = display
        self._level = level
        self._center_x = center[0]
        self._center_y = center[1]
        self._screen_width = display.get_size()[0]
        self._screen_heigth = display.get_size()[1]

    def set_level(self, level):
        """Sets the level to be rendered.

        Args:
            level: The level to be rendered.
        """
        self._level = level

    def render(self, coins, stars, failed, success):
        """Draws the sprites of the currently chosen level.

        If the player beats or fails a level, suitable texts are rendered.

        Args:
            coins: The amount of coins collected.
            stars: The amount of stars collected.
            failed: If the player has failed.
            success: If the player has succeeded.
        """
        self._level.all_sprites.draw(self._display)
        self._render_info_texts(coins, stars)

        if failed:
            self._render_text("FAILED")
            self._render_text("Press R to restart level, ESC to go to menu",
                              20, self._center_x, self._center_y+20)

        if success:
            self._render_text("SUCCESS!!")
            self._render_text("Press ENTER to return to menu",
                              25, self._center_x, self._center_y+20)

        pygame.display.update()

    def render_introscreen(self):
        """Renders the intro screen.
        """
        self._render_text("GAME", 100)
        self._render_text("Press ENTER to start or ESC to quit",
                          32, self._center_x, self._center_y + 50)
        pygame.display.update()

    def render_menu(self, chosen_level, level_info):
        """Renders the menu.

        Args:
            chosen_level: The currently chosen level number.
            level_info: Max number of collectibles found in the level.
        """
        self._display.fill((0, 0, 0))
        self._render_text("CHOOSE LEVEL", 75, self._center_x, 50)
        self._render_text(str(chosen_level), 100)
        self._render_collectibles(level_info)
        self._render_text("Press <- and -> to browse, ENTER to select, BACKSPACE to save menu",
                          20, self._center_x, self._center_y + 100)
        pygame.display.update()

    def render_slotscreen(self, slot=1):
        self._display.fill((0, 0, 0))
        self._render_text("CHOOSE SAVE SLOT", 65, self._center_x, 50)
        self._render_text(str(slot), 100)
        self._render_text("Press <- and -> to browse, ENTER to select, DEL to clear slot",
                          20, self._center_x, self._center_y + 100)
        pygame.display.update()

    def render_delete_slotscreen(self, slot):
        self._display.fill((0, 0, 0))
        self._render_text(
            f"Clear save data from slot {slot}?", 50, self._center_x, self._center_y)
        self._render_text("ENTER to confirm, BACKSPACE to cancel",
                          20, self._center_x, self._center_y + 100)
        pygame.display.update()

    def render_pause(self):
        """Renders the pause window.
        """
        pause_screen = pygame.Rect(
            0, 0, self._screen_width/2, self._screen_heigth/3)
        pause_screen.center = (self._center_x, self._center_y)
        pygame.draw.rect(self._display, BLACK, pause_screen)
        self._render_text("GAME PAUSED")
        self._render_text("Return to menu with ESC", 20,
                          self._center_x, self._center_y+30)

        pygame.display.update()

    def _render_info_texts(self, coins, stars):
        self._render_text(f"Coins: {coins}", 20, 25, 25)
        self._render_text(f"Stars: {stars}", 20, 25, 45)

    def _render_text(self, text, size=32, x=0, y=0):
        font = pygame.font.Font(None, size)
        text = font.render(text, True, WHITE)
        text_rect = text.get_rect()

        if x == 0 and y == 0:
            text_rect.center = (self._center_x, self._center_y)
        else:
            text_rect.center = (x, y)
        self._display.blit(text, text_rect)

    def _render_collectibles(self, level_info):
        max_coins = level_info[0]
        max_stars = level_info[1]

        if len(level_info) > 2:
            coins_collected = level_info[2]
            stars_collected = level_info[3]
        else:
            coins_collected = 0
            stars_collected = 0

        self._render_text(
            f"Coins: {coins_collected}/{max_coins}", 30, self._center_x, self._center_y+50)
        self._render_text(
            f"Stars: {stars_collected}/{max_stars}", 30, self._center_x, self._center_y+70)
