import pygame
import random

class Heart:
    """ Define the Heart class"""
    def __init__(self, screen):
        self.screen = screen
        self.image = pygame.image.load("media/heart.png")
        self.image = pygame.transform.scale(self.image, (60,60))
        self.rect = self.image.get_rect()

        self.rect.x = random.randint(0, self.screen.get_width() - self.rect.width)
        #self.rect.y = random.randint(300, self.screen.get_height() - 350)
        self.rect.y = random.randint(350, 450)

    
    def blitme(self):
        self.screen.blit(self.image, self.rect)