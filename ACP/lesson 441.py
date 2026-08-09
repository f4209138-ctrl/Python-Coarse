import pygame
import random

pygame.init()
screen = pygame.display.set_mode((800, 600))
clock = pygame.time.Clock()

player = pygame.Rect(400, 300, 40, 40)
enemies = [pygame.Rect(random.randint(0, 760), random.randint(0, 560), 40, 40) for _ in range(7)]
score = 0

running = True
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

    keys = pygame.key.get_pressed()
    if keys[pygame.K_LEFT]: player.x -= 5
    if keys[pygame.K_RIGHT]: player.x += 5
    if keys[pygame.K_UP]: player.y -= 5
    if keys[pygame.K_DOWN]: player.y += 5

    for enemy in enemies[:]:
        if player.colliderect(enemy):
            score += 1
            enemies.remove(enemy)
            enemies.append(pygame.Rect(random.randint(0, 760), random.randint(0, 560), 40, 40))

    screen.fill((0, 0, 0))
    pygame.draw.rect(screen, (0, 255, 0), player)
    for enemy in enemies:
        pygame.draw.rect(screen, (255, 0, 0), enemy)

    pygame.display.flip()
    clock.tick(60)

pygame.quit()