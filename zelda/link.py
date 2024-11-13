import pygame

class Link():

    # Zelda sound library https://zeldaarchive.org/zelda-sounds/

    """A class to manage Link"""
    def __init__(self, zelda_game):
        """Initialize Link and his starting position"""
        self.screen = zelda_game.screen
        self.screen_rect = zelda_game.screen.get_rect()

        # Load Link image and get its rect
        self.original_image = pygame.image.load('media/link.png')
        # Scale the image down
        self.original_image = pygame.transform.scale(self.original_image, (self.original_image.get_width() // 6, self.original_image.get_height() // 6))
        self.image = self.original_image
        self.rect = self.image.get_rect()

        # Position Link on the ground and in the middle of the background
        #self.rect.x = 715
        #self.rect.y = 100s
        # Start each new Link at the bottom center of the screen
        #self.rect.midbottom = self.screen_rect.midbottom
        self.rect.centerx = self.screen_rect.centerx
        self.rect.bottom = self.screen_rect.bottom - 80
        # Movement flag; start with Link that's not moving.
        self.moving_right = False
        self.moving_left = False
        self.moving_up = False
        self.moving_down = False

        self.is_jumping = False
        self.vertical_velocity = 0 #Jump Speed
        self.gravity = 1 # Gravity effect

        # Load jump sound
        self.jump_sound = pygame.mixer.Sound("media/link_jump.wav")
        self.jump_sound.set_volume(1)



    def update(self):
        # Test if jumping
        if self.is_jumping:
            self.rect.y += self.vertical_velocity
            self.vertical_velocity += self.gravity # Gravity to bring Link Down

            # Check to see if Link has landed(Hits bottom of the screen)
            if self.rect.bottom >= self.screen_rect.bottom - 80:
                self.rect.bottom =  self.screen_rect.bottom - 80
                self.is_jumping = False # Stop Jumping
                self.vertical_velocity = 0 #Reset Vertical velocity


        # Movement in other directions (Left or)
        if self.moving_right:
            self.image = pygame.transform.flip(self.original_image,1,0)
            self.rect.x += 9
        elif self.moving_left:
            self.image = pygame.transform.flip(self.original_image,0,0)
            self.rect.x -= 9


    def handle_keydown(self, event):
        if event.key == pygame.K_a:
            self.moving_left = True
        elif event.key == pygame.K_d:
            self.moving_right = True
        elif event.key == pygame.K_SPACE:
            self.jump() # Trigger jump on spacebar

    def handle_keyup(self,event):
        """ Handle Keyup events to reset movement flags"""
        if event.key == pygame.K_UP:
            self.moving_up = False
        elif event.key == pygame.K_DOWN:
            self.moving_down = False
        elif event.key == pygame.K_a:
            self.moving_left = False
        elif event.key == pygame.K_d:
            self.moving_right = False

    def jump(self):
        """ Make Link jump by setting initial vertical velocity"""
        if not self.is_jumping:
            
            self.is_jumping = True
            self.vertical_velocity = -15 # Initial jump velocity (Negative to move up)
            self.jump_sound.play()


    def blitme(self):
        """Draw Link at his current location"""
        self.screen.blit(self.image, self.rect)