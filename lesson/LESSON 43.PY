import pygame
import random
pygame.init()
SPRITE_COLOR_CHANGE_EVENT=pygame.USEREVENT+1
BACKGROUND_COLOR_CHANGE_EVENT=pygame.USEREVENT+2
BLUE=pygame.Color('blue')
LIGHTBLUE=pygame.Color('lightblue')
DARKBLUE=pygame.Color('darkblue')
YELLOW=pygame.Color('yellow')
MAGENTA=pygame.Color('magenta')
WHITE=pygame.Color('white')
class Sprite(pygame.sprite.Sprite):
    def __init__(self,color,height,width):
        super().__init__()
        self.image=pygame.Surface([width,height])
        self.image.fill(color)
        self.rect=self.image.get_rect()
        self.velocity=[random.choice([-1,1]),random.choice([-1,1])]
    def update(self):
        self.rect.move_ip(self.velocity)
        boundry_hit=False
        if self.rect.left<=0 or self.rect.right>=500:
            self.velocity[0]=-self.velocity[0]
            boundry_hit=True
            if self.rect.left<=0 or self.rect.right>=500:
                self.velocity[0]=-self.velocity[0]
            if self.rect.left<=0 or self.rect.right>=400:
                self.velocity[1]=-self.velocity[1]
            if boundry_hit:
                pygame.event.post(pygame.event.Event(SPRITE_COLOR_CHANGE_EVENT))
                pygame.event.post(pygame.event.Event(BACKGROUND_COLOR_CHANGE_EVENT))
        def change_color():
            self.image.fill(random.choice([YELLOW,MAGENTA,WHITE]))
def change_background_color():
    global bg_color
    bg_color=random.choice([BLUE,LIGHTBLUE,DARKBLUE])

                


