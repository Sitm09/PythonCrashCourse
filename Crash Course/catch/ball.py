import pygame
from pygame.sprite import Sprite

class Ball(Sprite):
    """A class to represent a single ball."""

    def __init__(self, c_settings, screen):
        """Initializes the ball and set its starting position."""
        super(Ball, self).__init__()
        self.screen = screen
        self.c_settings = c_settings

        # Load tha alien image and set its rect attribute.
        self.image = pygame.image.load('images/ball.bmp')
        self.rect = self.image.get_rect()

        # Start each new ball in the middle of the screen.
        self.rect.x = self.screen.centerx
        self.rect.y = self.screen.top

        # Store the ball's exact position.
        self.x = float(self.rect.x)

    def blitme(self):
        """Draw the ball at it's current location."""
        self.screen.blit(self.image, self.rect)


    def update(self):
        """Move the ball down"""
        self.y += self.c_settings.ball_drop_speed
        self.rect.y = self.y
