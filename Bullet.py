import pygame

from pygame.sprite import Sprite

class Bullet(Sprite):
    """class for bullets"""

    def __init__(self, ai_game):
        """creat a bullet at the spaceship"""
        super().__init__()
        self.screen = ai_game.screen
        self.settings = ai_game.settings
        self.color = self.settings.bullet_color


        # create a bullet rect at (0, 0), then set it to the right place
        self.rect = pygame.Rect(0, 0, self.settings.bullet_width,
                    self.settings.bullet_height)
        self.rect.midtop = ai_game.ship.rect.midtop

        # store bullet coordinate by float
        self.y = float(self.rect.y)

    def update(self):
            """move bullets upwards"""
            # update its coordination by float
            self.y -= self.settings.bullet_speed
            # update rect's coordination
            self.rect.y = self.y

    def draw_bullet(self):
        """draw bullets on the screen"""
        pygame.draw.rect(self.screen, self.color, self.rect)
