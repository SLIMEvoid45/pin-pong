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
while True:
    print('error: (проэкт не доработан)')
    