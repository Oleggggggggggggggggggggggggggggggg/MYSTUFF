import pygame
pygame.init()
x = 400
y = 300
size = 40
screenwidth = 800
screenheight = 600
speed = 0.5
player = pygame.Rect((x, y, size, size))
bulletplace = pygame.Rect((x, y, 1, 1))
screen = pygame.display.set_mode((screenwidth, screenheight))




def move():
    global x
    global y
    bulletplace.centerx = player.centerx = int(x)
    bulletplace.centery = player.centery = int(y)
    
    if x > screenwidth - 20:
        x -= speed
    if x < 20:
        x += speed
    if y > screenheight - 20:
        y -= speed
    if y < 20:
        y += speed

def check_key():
     moved = False
     global x
     global y
     if key[pygame.K_a] == True:
        x -= speed
        moved = True
     if key[pygame.K_w] == True:
         y -= speed
         moved = True
     if key[pygame.K_s] == True:
         y += speed
         moved = True  
     if key[pygame.K_d] == True:
         x += speed
         moved = True
     if moved:
         move()
         
        

run = True
while run:
    screen.fill((0, 0, 0))
    pygame.draw.rect(screen, (0, 255, 0), player)
    pygame.draw.rect(screen, (0, 255, 255), bulletplace)

    key = pygame.key.get_pressed()
    move()

    check_key()
    


    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            run = False
    
    pygame.display.update()

pygame.quit()

