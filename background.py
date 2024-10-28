import pygame

class Background():
    """A class to manage the ship"""
    def __init__(self, link_game):
        """Initialize the ship and its starting position"""
        self.screen = link_game.screen
        self.screen_rect = link_game.screen.get_rect()

        # Load the background image and get its rect
        self.image = pygame.image.load('media/background_chill.png')
        self.rect = self.image.get_rect()

    def blitme(self):
        """Draw the background at its current location"""
        self.screen.blit(self.image, self.rect)