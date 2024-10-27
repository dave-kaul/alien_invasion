import sys
import os
import pygame

os.chdir("D:/OneDrive/Albright/CSC141/alien_invasion")

class BlueSky:
    """ Overall class to manage game assets and behavior."""

    def __init__(self):
        """Initialize the game and create game resourceas."""
        pygame.init()
        self.clock = pygame.time.Clock()
        self.screen = pygame.display.set_mode((1455,625))
        pygame.display.set_caption("Legend of Zelda")

        # Set to a light blue
        self.bg_color = (50,125,255)

    def run_game(self):
        """ Start the main loop for the game """
        while True:
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    sys.exit()
                    
            self.screen.fill(self.bg_color)

            # Make the most recently drawn screen available
            pygame.display.flip()
            self.clock.tick(60)
            

if __name__ == '__main__':
    ai = BlueSky()
    ai.run_game()


   