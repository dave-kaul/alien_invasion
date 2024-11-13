import pygame

class Background():
    """Initalize the background and its starting position"""
    def __init__(self, link_game):
        """Initialize Link and his starting position"""
        self.screen = link_game.screen
        self.screen_rect = link_game.screen.get_rect()

        # Load the background image and get its rect
        self.image = pygame.image.load('media/background_forest.png')
        self.rect = self.image.get_rect()

        # Starting position offset
        self.offset_x = 0
        self.offset_y = 0

        # center the background image to the screen
        self.rect.center = self.screen_rect.center

    def update(self, link):
        """ Update the background based on Links's movement"""
        if link.moving_left:
            self.offset_x -= 3
        elif link.moving_right:
            self.offset_x += 3

        if self.rect.x > 650:
            self.rect.x = 0
    def blitme(self):
        """Draw the background at its current location"""
        self.screen.blit(self.image, (self.rect.x + self.offset_x, 0))