import pygame
pygame.init()
SCREEN_WIDTH, SCREEN_HEIGHT = 500, 500
screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
pygame.display.set_caption("My first game screen")
image = pygame.image.load('image.png').convert_alpha()
image = pygame.transform.scale(image, (300, 300))
image_rect = image.get_rect(center=(SCREEN_WIDTH // 2, SCREEN_HEIGHT // 2))
clock = pygame.time.Clock()
running = True
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
    screen.fill((58, 58, 58))
    screen.blit(image, image_rect)
    pygame.display.flip()
    clock.tick(30)
pygame.quit()