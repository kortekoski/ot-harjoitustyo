import pygame


class Renderer:
    def __init__(self, display, level):
        self._display = display
        self._level = level

    def render(self, coins, stars, failed, success):
        self._level.all_sprites.draw(self._display)
        self._render_info_texts(coins, stars)

        if failed:
            self._render_text("FAILED, press R to restart")
        
        if success:
            self._render_text("SUCCESS!!")

        pygame.display.update()

    def _render_info_texts(self, coins, stars):
        self._render_text(f"Coins: {coins}", 20, 25, 25)
        self._render_text(f"Stars: {stars}", 20, 25, 45)

    def _render_text(self, text, size=32, x=0, y=0):
        font = pygame.font.Font(None, size)
        text = font.render(text, True, (255, 255, 255))
        text_rect = text.get_rect()

        if x == 0 and y == 0:
            text_rect.center = self._level.get_center()
        else:
            text_rect.left = x
            text_rect.bottom = y
        self._display.blit(text, text_rect)
        