import pygame

class Keeper():


    def __init__(self, c_settings, screen):
        """Initialize the ship and set its starting position."""
        self.screen = screen
        self.c_settings = c_settings

        #Load the ship image and get its rect.
        self.image = pygame.image.load('images/keeper.bmp')
        self.rect = self.image.get_rect()
        self.screen_rect = screen.get_rect()

        # Start each new rocket in the middle of the screen.
        self.rect.centerx = self.screen_rect.centerx
        self.rect.bottom = self.screen_rect.bottom


        # Store a deciaml value for the ship's center.
        self.center = float(self.rect.centerx)
        self.centery = float(self.rect.centery)

        # Movement flag
        self.moving_right = False
        self.moving_left = False


    def update(self):
        """Update the keeper's position based on the movement flag."""
        # Update the ship's center value, not the rect
        if self.moving_right and self.rect.right < self.screen_rect.right:
            self.center +=self.c_settings.keeper_speed_factor
        if self.moving_left and self.rect.left > 0:
            self.center -= self.c_settings.keeper_speed_factor

        #Update rect objrct from self.center.
        self.rect.centerx = self.center

    def blitme(self):
        """Draw the keeper at its current location."""
        self.screen.blit(self.image, self.rect)
