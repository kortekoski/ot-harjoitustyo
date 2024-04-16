import pygame


class Renderer:
    def __init__(self, display, level):
        self._display = display
        self._level = level

    def render(self):
        self._level.all_sprites.draw(self._display)

        pygame.display.update()

    def render_text(self, text):
        font = pygame.font.Font(None, 32)
        text = font.render(text, True, (255, 255, 255))
        text_rect = text.get_rect()
        text_rect.center = self._level.get_center()
        self._display.blit(text, text_rect)
        pygame.display.update()
