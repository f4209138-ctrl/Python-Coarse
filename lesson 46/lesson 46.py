import pygame
import sys

# Initialize all pygame modules
if pygame.init()[1] > 0:
    print("Warning: Some pygame modules failed to initialize")

# Set screen dimensions
WIDTH, HEIGHT = 800, 600

try:
    # Set the display mode
    screen = pygame.display.set_mode((WIDTH, HEIGHT))
    pygame.display.set_caption("Background Image")
except pygame.error as e:
    print(f"Error setting display mode: {e}")
    print("Ensure you are running this in an environment that supports graphical windows.")
    sys.exit(1)

# Load and scale background image
try:
    # Ensure 'background.png' exists in the same directory as the script
    background = pygame.image.load('background.png').convert()
    background = pygame.transform.scale(background, (WIDTH, HEIGHT))
except FileNotFoundError:
    print("Error: 'background.png' not found. Please ensure the image file exists.")
    # Create a solid color background as fallback
    background = pygame.Surface((WIDTH, HEIGHT))
    background.fill((0, 0, 0)) # Black background

clock = pygame.time.Clock()
running = True

while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

    # Draw the background first
    screen.blit(background, (0, 0))

    # Draw other game elements here...

    pygame.display.flip()
    clock.tick(60)

pygame.quit()
sys.exit()   