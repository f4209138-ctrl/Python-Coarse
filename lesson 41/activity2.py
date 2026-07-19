import pygame
pygame.init()
SCREEN_WIDTH, SCREEN_HEIGHT = 500, 500
screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
pygame.display.set_caption("Penguin Window")
background = pygame.image.load('background.png').convert()
background = pygame.transform.scale(background, (SCREEN_WIDTH, SCREEN_HEIGHT))
penguin = pygame.image.load('penguin.png').convert_alpha()
penguin = pygame.transform.scale(penguin, (200, 200))
penguin_rect = penguin.get_rect(center=(SCREEN_WIDTH // 2, SCREEN_HEIGHT // 2))
font = pygame.font.Font(None, 30)
def draw_text_multiline(text, font, color, surface, x, y):
    words = text.split(' ')
    lines = []
    current_line = []
    for word in words:
        test_line = ' '.join(current_line + [word])
        if font.size(test_line)[0] < SCREEN_WIDTH - 20:
            current_line.append(word)
        else:
            lines.append(' '.join(current_line))
            current_line = [word]
    lines.append(' '.join(current_line))
    for i, line in enumerate(lines):
        text_surface = font.render(line, True, color)
        text_rect = text_surface.get_rect(center=(x, y + i * 30))
        surface.blit(text_surface, text_rect)
def game_loop():
    clock = pygame.time.Clock()
    running = True
    long_text = "hi everyone my name is Cody! used by codingal as a tutor runs on a model from google."
    while running:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False
        screen.blit(background, (0, 0))
        screen.blit(penguin, penguin_rect)
        draw_text_multiline(long_text, font, (0, 0, 0), screen, SCREEN_WIDTH // 2, 50)
        pygame.display.flip()
        clock.tick(30)
    pygame.quit()
if __name__ == '__main__':
    game_loop()