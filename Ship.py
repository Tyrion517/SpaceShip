import pygame.image


class Ship:
    """for managing ships"""

    def __init__(self, ai_game):
        """initialize ship and its place"""
        self.screen = ai_game.screen
        self.screen_rect = ai_game.screen.get_rect()
        self.settings = ai_game.settings

        # load ship image and ge its rect
        self.image = pygame.image.load('images/ship.bmp')
        self.rect = self.image.get_rect()

        # place every new ship at the central bottom of the screen
        self.rect.midbottom = self.screen_rect.midbottom

        # store float in ship's attribute x
        self.x = float(self.rect.x)

        # flag of moving
        self.moving_right = False
        self.moving_left = False

    def update(self):
        # move the ship according to flags
        # update the x attribute of Ship instead of Ship.rect
        if self.moving_right and self.rect.right < self.screen_rect.right:
            self.x += 1
        if self.moving_left and self.rect.x > 0:
            self.x -= 1

        # update x of rect by x of ship
        self.rect.x = self.x

    def blitme(self):
        """draw ship at wanted place"""
        self.screen.blit(self.image, self.rect)
