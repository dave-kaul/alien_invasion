import sys
import pygame
from settings import Settings
from link import Link
from background import Background
from heart import Heart


# This code is refactored


class Zelda:
    """ Overall class to manage game assets and behavior."""

    def __init__(self):
        """Initialize the game and create game resources."""
        pygame.init()
        self.clock = pygame.time.Clock()

        self.settings = Settings()
        
        self.screen = pygame.display.set_mode((self.settings.screen_width, self.settings.screen_height))
        
        pygame.display.set_caption("Legend of Zelda")
        self.link = Link(self)
        self.background = Background(self)

        pygame.mixer.music.load("media/zelda.mp3")
        pygame.mixer.music.play(-1) # Loop music

        self.hearts = []
        self._create_hearts(18) # Creatre X number of hearts initally
        
    def _create_hearts(self, number):
        for _ in range(number):
            heart = Heart(self.screen)
            self.hearts.append(heart)

    def _check_heart_collection(self):
        """ Check if Link collects any hearts """
        for heart in self.hearts[:]: # Use a copy of the list to avoid issues when removing items
            if self.link.rect.colliderect(heart.rect):
                self.hearts.remove(heart)

                # Increase score here
                print ("Heart Collected")

    def run_game(self):
        """ Start the main loop for the game"""
        while True:
            self._check_events()
            self._check_heart_collection()
            self.link.update()
            self.background.update(self.link)
            self._update_screen()
            self.clock.tick(60)
            # Redraw the screen during each pass through the loop
            
            # Redraw the screen during each pass through the loop
           
            # Make the most recently drawn screen available
                
    def _check_events(self):
        """Respond to keypresses and mouse events."""
        
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                sys.exit()
            elif event.type == pygame.KEYDOWN:
                if event.key == pygame.K_ESCAPE: # If hit ESC key close the window
                    sys.exit()
                else:
                    self.link.handle_keydown(event) # Handle all keydown events in Link


            elif event.type == pygame.KEYUP:
                self.link.handle_keyup(event) # Handle all keyup events in Link as well
          
    def _update_screen(self):
        """Update images on the screen, and flip to the new screen."""
        #self.screen.fill(self.settings.bg_color)
        self.background.blitme()
        self.link.blitme()
        
        # Draw hearts
        for heart in self.hearts:
            heart.blitme()

        # Make the most recently drawn screen available
        pygame.display.flip()

if __name__ == '__main__':
    # Instantiate and run game
    zelda = Zelda()
    zelda.run_game()


   