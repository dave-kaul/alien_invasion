import pygame

class Ship():
    """A class to manage the ship"""
    def __init__(self, ai_game):
        """Initialize the ship and its starting position"""
        self.screen = ai_game.screen
        self.screen_rect = ai_game.screen.get_rect()

        # Load the ship image and get its rect
        self.image = pygame.image.load('media/ship.png')
        # Scale the ship as needed
        self.image = pygame.transform.scale(self.image, (self.image.get_width() * 1, self.image.get_height() * 1))
        self.rect = self.image.get_rect()

        # Start each new ship at the bottom center of the screen
        self.rect.midbottom = self.screen_rect.midbottom
    
    def blitme(self):
        """Draw the ship at its current location"""
        self.screen.blit(self.image, self.rect)