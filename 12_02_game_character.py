import sys
import pygame
from settings import Settings
from link import Link

class LinkLegend:
    """ Overall class to manage game assets and behavior."""

    def __init__(self):
        """Initialize the game and create game resourceas."""
        pygame.init()
        self.clock = pygame.time.Clock()
        self.settings = Settings()
        self.screen = pygame.display.set_mode((self.settings.screen_width, self.settings.screen_height))
    
        pygame.display.set_caption("Legend of Zelda")
        self.link = Link(self)
        self.bg_color = (0,0,0)

    def run_game(self):
        """ Start the main loop for the game"""
        while True:
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    sys.exit()

            # Redraw the screen during each pass through the loop
            self.screen.fill(self.settings.bg_color)
            self.link.blitme()

            # Make the most recently drawn screen available
            pygame.display.flip()
            self.clock.tick(60)
            
if __name__ == '__main__':
    ai = LinkLegend()
    ai.run_game()


   