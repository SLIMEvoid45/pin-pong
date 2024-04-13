#
from pygame import *
from random import *
pygame.init()

win1 = 700
win2 = 500
window = display.set_mode((win1, win2))
display.set_caption("ping pon")
background = transform.scale(image.load("BACK.png"), (700, 500))
clock = time.Clock()
FPS = 120
lost = 0
score = 0
game = True
finish = False

class GameSprite(sprite.Sprite):
    def __init__(self, player_image, player_x, player_y, player_speed):
        super().__init__()
        self.image = transform.scale(image.load(player_image), (65, 65))
        self.speed = player_speed
        self.rect = self.image.get_rect()
        self.rect.x = player_x
        self.rect.y = player_y
    def reset(self):
        window.blit(self.image, (self.rect.x, self.rect.y))

class Player(GameSprite):
    def update(self):
        keys_pressed = key.get_pressed()
        if keys_pressed[K_a] and self.rect.x > 5:
            self.rect.x -= self.speed
        if keys_pressed[K_d] and self.rect.x < 595:
            self.rect.x += self.speed
while gamequit:
    window.blit(backgroundmain2, (0, 0))
    window.blit(sparitemain1, (x1, y1))
    window.blit(sparitemain2, (x2, y2))
    pygame.display.update()
    if y1 < 470:
        y1 += speed 
    if pygame.key.get_pressed()[pygame.K_RIGHT] and x1 < 670:
        
        x1 += speed
        print(x1)
    if pygame.key.get_pressed()[pygame.K_LEFT] and x1 > 5:
        x1 -= speed
        print(x1)
    if pygame.key.get_pressed()[pygame.K_UP] and y1 > 5:
        y1 -= speed
        print(y1)
    if pygame.key.get_pressed()[pygame.K_DOWN] and y1 < 470:
        y1 += speed
        print(y1)

    if pygame.key.get_pressed()[pygame.K_d] and x2 < 650:
        x2 += speed
        print(x2)
    if pygame.key.get_pressed()[pygame.K_a] and x2 > 5:
        x2 -= speed
        print(x2)
    if pygame.key.get_pressed()[pygame.K_w] and y2 > 5:
        y2 -= speed
        print(y2)
    if pygame.key.get_pressed()[pygame.K_s] and y2 < 470:
        y2 += speed
        print(y2)

    for w in pygame.event.get():
        if w.type == pygame.QUIT:
            gamequit = False