import pygame
import sys
import random

pygame.init()
WIDTH, HEIGHT = 800, 600
screen = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("Pet Food Collection")

try:
    background = pygame.transform.scale(pygame.image.load("background.png"), (WIDTH, HEIGHT))
except:
    background = pygame.Surface((WIDTH, HEIGHT))
    background.fill((50, 150, 50))

class Pet(pygame.sprite.Sprite):
    def __init__(self):
        super().__init__()
        try:
            self.image = pygame.image.load("pet.png").convert_alpha()
        except:
            self.image = pygame.Surface((40, 40))
            self.image.fill((0, 0, 255))
        self.rect = self.image.get_rect(center=(WIDTH // 2, HEIGHT // 2))
        self.speed = 5

    def update(self, keys):
        if keys[pygame.K_LEFT]:
            self.rect.x -= self.speed
        if keys[pygame.K_RIGHT]:
            self.rect.x += self.speed
        if keys[pygame.K_UP]:
            self.rect.y -= self.speed
        if keys[pygame.K_DOWN]:
            self.rect.y += self.speed
        
        self.rect.clamp_ip(screen.get_rect())

class Food(pygame.sprite.Sprite):
    def __init__(self, x, y):
        super().__init__()
        try:
            self.image = pygame.image.load("food.png").convert_alpha()
        except:
            self.image = pygame.Surface((20, 20))
            self.image.fill((255, 100, 0))
        self.rect = self.image.get_rect(center=(x, y))

pet = Pet()
all_sprites = pygame.sprite.Group()
foods = pygame.sprite.Group()

all_sprites.add(pet)

for _ in range(10):
    x = random.randint(50, WIDTH - 50)
    y = random.randint(50, HEIGHT - 50)
    food = Food(x, y)
    all_sprites.add(food)
    foods.add(food)

font = pygame.font.SysFont("impact", 54)
clock = pygame.time.Clock()
running = True
completed = False

while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

    if not completed:
        keys = pygame.key.get_pressed()
        pet.update(keys)
        
        pygame.sprite.spritecollide(pet, foods, True)
        
        if len(foods) == 0:
            completed = True

    screen.blit(background, (0, 0))
    all_sprites.draw(screen)

    if completed:
        text = font.render("COMPLETED!", True, (255, 255, 255))
        text_rect = text.get_rect(center=(WIDTH // 2, HEIGHT // 2))
        screen.blit(text, text_rect)

    pygame.display.flip()
    clock.tick(60)

pygame.quit()
sys.exit()