import pygame


class Renderer:
    def __init__(self, display, center, level=None):
        self._display = display
        self._level = level
        self._center_x = center[0]
        self._center_y = center[1]

    def set_level(self, level):
        self._level = level

    def render(self, coins, stars, failed, success):
        self._level.all_sprites.draw(self._display)
        self._render_info_texts(coins, stars)

        if failed:
            self._render_text("FAILED, press R to restart")

        if success:
            self._render_text("SUCCESS!!")
            self._render_text("Press ENTER to return to menu",
                              25, self._center_x, self._center_y+20)

        pygame.display.update()

    def render_introscreen(self):
        self._render_text("GAME", 100)
        self._render_text("Press ENTER to start or ESC to quit",
                          32, self._center_x, self._center_y + 50)
        pygame.display.update()

    def render_menu(self, chosen_level=0):
        self._display.fill((0, 0, 0))
        self._render_text("CHOOSE LEVEL", 75, self._center_x, 50)
        self._render_text(str(chosen_level), 100)
        self._render_text("Press <- and -> to browse, ENTER to select",
                          20, self._center_x, self._center_y + 100)
        pygame.display.update()

    def _render_info_texts(self, coins, stars):
        self._render_text(f"Coins: {coins}", 20, 25, 25)
        self._render_text(f"Stars: {stars}", 20, 25, 45)

    def _render_text(self, text, size=32, x=0, y=0):
        font = pygame.font.Font(None, size)
        text = font.render(text, True, (255, 255, 255))
        text_rect = text.get_rect()

        if x == 0 and y == 0:
            text_rect.center = (self._center_x, self._center_y)
        else:
            text_rect.center = (x, y)
        self._display.blit(text, text_rect)
