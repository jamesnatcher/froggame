import pygame

from pygame.locals import (
    K_UP,
    K_DOWN,
    K_LEFT,
    K_RIGHT,
    K_ESCAPE,
    KEYDOWN,
)

# Constants for the game
SCREEN_WIDTH = 900
SCREEN_HEIGHT = 900

class Player(pygame.sprite.Sprite):
    def __init__(self):
        # Call the parent class (Sprite) constructor
        pygame.sprite.Sprite.__init__(self)

        # Set entity properties
        self.width = 75
        self.height = 75
        self.speed = 75
        self.surf = pygame.Surface([self.width, self.height])
        self.surf.fill((255, 255, 255))

        # Set up the entity's position
        self.rect = self.surf.get_rect()
        self.rect[0] = ((SCREEN_HEIGHT/self.width)/2) * self.width
        self.rect[1] = ((SCREEN_HEIGHT/self.height)/2) * self.height

    # Handles user inputs for the Player entity
    def handleKeys(self, pressed_keys):
        position = self.rect
        if pressed_keys[K_UP]:
            self.rect.move_ip(0, -self.speed)
            if (position[1] < 0):
                position[1] %= SCREEN_HEIGHT
        if pressed_keys[K_DOWN]:
            self.rect.move_ip(0, self.speed)
            if (position[1] + self.height > SCREEN_HEIGHT):
                position[1] = 0
        if pressed_keys[K_LEFT]:
            self.rect.move_ip(-self.speed, 0)
            if (position[0] < 0):
                position[0] %= SCREEN_WIDTH
        if pressed_keys[K_RIGHT]:
            self.rect.move_ip(self.speed, 0)
            if (position[0] + self.width > SCREEN_WIDTH):
                position[0] = 0

# Set up pygame
pygame.init()
screen = pygame.display.set_mode((SCREEN_WIDTH,SCREEN_HEIGHT))
clock = pygame.time.Clock()

# Initialize entities
player = Player()
background = pygame.image.load("lilypads.png")
background = pygame.transform.scale(background, (SCREEN_WIDTH+100, SCREEN_HEIGHT+100))

# Game loop
running = True
while running:
    # Process player inputs.
    for event in pygame.event.get():
        if event.type == KEYDOWN:
            if event.key == K_ESCAPE:
                running = False
        elif event.type == pygame.QUIT:
            pygame.quit()
            raise SystemExit

    # Do logical updates here.
    
    # Handle player input 
    pressed_keys = pygame.key.get_pressed()
    player.handleKeys(pressed_keys)

    # Render the graphics here.

    # Display background
    screen.fill("purple")  # Fill the display with a solid color
    screen.blit(background, (-90, -100))

    # Draw entities
    screen.blit(player.surf, player.rect)

    pygame.display.flip()  # Refresh on-screen display
    clock.tick(24)         # wait until next frame (at 60 FPS)