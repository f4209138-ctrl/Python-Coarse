import pygame

pygame.init()

WHITE = pygame.Color('white')
RED = pygame.Color('red')
BLUE = pygame.Color('blue')

SCREEN_WIDTH = 500
SCREEN_HEIGHT = 400

class PlayerSprite(pygame.sprite.Sprite):
    def __init__(self, color, width, height, controls):
        super().__init__()
        self.image = pygame.Surface([width, height])
        self.image.fill(color)
        self.rect = self.image.get_rect()
        self.speed = 5
        self.controls = controls

    def update(self):
        keys = pygame.key.get_pressed()

        if keys[self.controls['left']]:
            self.rect.x -= self.speed
        if keys[self.controls['right']]:
            self.rect.x += self.speed
        if keys[self.controls['up']]:
            self.rect.y -= self.speed
        if keys[self.controls['down']]:
            self.rect.y += self.speed

        if self.rect.left < 0:
            self.rect.left = 0
        if self.rect.right > SCREEN_WIDTH:
            self.rect.right = SCREEN_WIDTH
        if self.rect.top < 0:
            self.rect.top = 0
        if self.rect.bottom > SCREEN_HEIGHT:
            self.rect.bottom = SCREEN_HEIGHT

screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
pygame.display.set_caption("Two Player Sprite Game")

all_sprites_list = pygame.sprite.Group()

controls_arrows = {
    'left': pygame.K_LEFT, 
    'right': pygame.K_RIGHT, 
    'up': pygame.K_UP, 
    'down': pygame.K_DOWN
}
player1 = PlayerSprite(RED, 40, 40, controls_arrows)
player1.rect.x = 100
player1.rect.y = 100
all_sprites_list.add(player1)

controls_wasd = {
    'left': pygame.K_a, 
    'right': pygame.K_d, 
    'up': pygame.K_w, 
    'down': pygame.K_s
}
player2 = PlayerSprite(BLUE, 40, 40, controls_wasd)
player2.rect.x = 300
player2.rect.y = 200
all_sprites_list.add(player2)

exit_game = False
clock = pygame.time.Clock()

while not exit_game:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            exit_game = True

    all_sprites_list.update()
    screen.fill(WHITE)
    all_sprites_list.draw(screen)
    pygame.display.flip()
    clock.tick(60)

pygame.quit()