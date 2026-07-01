import random
import time
import pygame
pygame.init()
movesens = 1

def wall_check(thing):
    if thing.centerx > 1200:
        thing.centerx = 0
    if thing.centerx < 0:
        thing.centerx = 1200
    if thing.centery > 600:
        thing.centery = 0
    if thing.centery < 0:
        thing.centery = 600


    


screen_width = 1200
screen_height = 600

screen = pygame.display.set_mode((screen_width, screen_height))
player = pygame.Rect((600, 250, 50, 50))
player2 = pygame.Rect((200, 250, 50, 50))

pygame.display.set_caption("HELLO")
run = True
while run:

    screen.fill((0, 255, 0))
    pygame.draw.rect(screen, (255, 0, 0), player)
    pygame.draw.rect(screen, (0, 0, 255), player2)
    
    key = pygame.key.get_pressed()
    if key[pygame.K_a] == True:
        player.move_ip(-movesens, 0)
        wall_check(player)
    elif key[pygame.K_w] == True:
        player.move_ip(0, -movesens)
        wall_check(player)
    elif key[pygame.K_s] == True:
        player.move_ip(0, movesens)
        wall_check(player)
    elif key[pygame.K_d] == True:
        player.move_ip(movesens, 0)
        wall_check(player)
    
    if key[pygame.K_LEFT] == True:
        player2.move_ip(-movesens, 0)
        wall_check(player2)
    elif key[pygame.K_UP] == True:
        player2.move_ip(0, -movesens)
        wall_check(player2)
    elif key[pygame.K_DOWN] == True:
        player2.move_ip(0, movesens)
        wall_check(player2)
    elif key[pygame.K_RIGHT] == True:
        player2.move_ip(movesens, 0)
        wall_check(player2)
    
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            run = False
    
    pygame.display.update()

pygame.quit()