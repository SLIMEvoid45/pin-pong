import pygame
backsetpoint = (0, 0)
windowres = (700, 500)
spriteres = (20, 20)
x1 = 20
y1 = 20
x2 = 20
y2 = 20
#создай окно игры
pygame.init()
#задай фон сцены
window = pygame.display.set_mode(windowres)
#создай 2 спрайта и размести их на сцене
spriteload1 = pygame.image.load('sprite1.png')
sparitemain1 = pygame.transform.scale(spriteload1, spriteres)
spriteload2 = pygame.image.load('sprite2.png')
sparitemain2 = pygame.transform.scale(spriteload2, spriteres)
backgroundload1 = pygame.image.load('background.jpg')
backgroundmain1 = pygame.transform.scale(backgroundload1, windowres)
backgroundload2 = pygame.image.load('background1.png')
backgroundmain2 = pygame.transform.scale(backgroundload2, windowres)
speed=0.5*10
gamequit = True
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
            