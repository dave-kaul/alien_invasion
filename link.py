import pygame

class Link():
    """A class to manage Link"""
    def __init__(self, ai_game):
        """Initialize Link and his starting position"""
        self.screen = ai_game.screen
        self.screen_rect = ai_game.screen.get_rect()

        # Load Link image and get its rect
        self.image = pygame.image.load('media/link.png')
        # Scale the image down by 5
        self.image = pygame.transform.scale(self.image, (self.image.get_width() // 5, self.image.get_height() // 5))
        self.rect = self.image.get_rect()

        # Position Link on the ground and in the middle of the background
        self.rect.x = 600
        self.rect.y = 450
    
    def blitme(self):
        """Draw Link at his current location"""
        self.screen.blit(self.image, self.rect)