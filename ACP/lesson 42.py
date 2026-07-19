import pygame

def main():
    pygame.init()
    
    screen_width, screen_height = 640, 480
    screen = pygame.display.set_mode((screen_width, screen_height))
    pygame.display.set_caption("My first game screen")
    
    BACKGROUND_COLOR = (0, 0, 0)
    RECT_COLOR = (0, 150, 255)
    TEXT_COLOR = (255, 255, 255)
    
    rect_width, rect_height = 150, 100
    rect_x = (screen_width // 2) - (rect_width // 2)
    rect_y = (screen_height // 2) - (rect_height // 2)
    
    font = pygame.font.SysFont("Arial", 24)
    text_surface = font.render("Welcome to my first game screen!", True, TEXT_COLOR)
    text_rect = text_surface.get_rect(center=(screen_width // 2, 50))
    
    clock = pygame.time.Clock()
    running = True
    
    while running:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False
                
        screen.fill(BACKGROUND_COLOR)
        
        pygame.draw.rect(screen, RECT_COLOR, pygame.Rect(rect_x, rect_y, rect_width, rect_height))
        screen.blit(text_surface, text_rect)
        
        pygame.display.flip()
        clock.tick(60)
        
    pygame.quit()

if __name__ == "__main__":
    main()