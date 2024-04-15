import pygame
import sys
import random
import time


pygame.init()


c = pygame.time.Clock()

#CONFIG
width = 1900
height = 1000
screen = pygame.display.set_mode((width, height))
pygame.display.set_caption("Ping Pon")
ball = pygame.Rect(width / 2 - 15, height / 2 - 15, 30, 30, )
player1 = pygame.Rect(width - 20, height / 2 - 70, 10, 140)
player2 = pygame.Rect(10, height / 2 - 70, 10, 140)
ball_speedx = 8 * random.choice((1, -1))
ball_speedy = 8 * random.choice((1, -1))
player1_speed = 0
player2_speed = 8
player1_score = 0
player2_score = 0
#CONFIG END

def ball_movement():
    global ball_speedx, ball_speedy, player1_score, player2_score
    ball.x += ball_speedx
    ball.y += ball_speedy


    if ball.top <= 0 or ball.bottom >= height:
        ball_speedy *= -1
    if ball.left <= 0:
        player1_score += 1
        ball_restart()
    if ball.right >= width:
        player2_score += 1
        ball_restart()

    if ball.colliderect(player1) or ball.colliderect(player2):
        ball_speedx *= -1


def player1_movement():
    global player1_speed
    player1.y += player1_speed
    if player1.top <= 0:
        player1.top = 0
    if player1.bottom >= height:
        player1.bottom = height


def player2_movement():
    global player2_speed
    if player2.top < ball.y:
        player2.top += player2_speed
    if player2.bottom > ball.y:
        player2.bottom -= player2_speed
    if player2.top <= 0:
        player2_top = 0
    if player2.bottom >= height:
        player2.bottom = height


def ball_restart():
    global ball_speedx, ball_speedy
    ball.center = (width / 2, height / 2)
    ball_speedy *= random.choice((1, -1))
    ball_speedx *= random.choice((1, -1))


font = pygame.font.SysFont("calibri", 25)

while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_DOWN:
                player1_speed += 8
            if event.key == pygame.K_UP:
                player1_speed -= 8
        if event.type == pygame.KEYUP:
            if event.key == pygame.K_DOWN:
                player1_speed -= 8
            if event.key == pygame.K_UP:
                player1_speed += 8

    ball_movement()
    player1_movement()
    player2_movement()

    if ball.x < 0:
        player1_score += 1
    elif ball.x > width:
        player2_score += 1


    screen.fill((0, 0, 0))
    pygame.draw.rect(screen, (220, 220, 220), player1)
    pygame.draw.rect(screen, (220, 220, 220), player2)
    pygame.draw.ellipse(screen, (220, 220, 220), ball)
    if player1_score == 15:
        pygame.quit()
        sys.exit()
    if player2_score == 15:
        pygame.quit()
        sys.exit()

    player1_text = font.render("Score P1:" + str(player1_score), False, (255, 255, 255))
    screen.blit(player1_text, [600, 50])
    player2_text = font.render("Score P2:" + str(player2_score), False, (255, 255, 255))
    screen.blit(player2_text, [300, 50])


    pygame.display.update()


    c.tick(60)
