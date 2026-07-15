import pygame 
import math 
pygame.init()
s_h = 600
s_w = 600
screen = pygame.display.set_mode((s_w, s_h))
tile = pygame.Rect((0, 0, 50, 50))
number = 1

board = []
for i in range(1, 65):
    board.append(i)


def move_vertical(index, piece, direction):
    board[index + 1] = index
    board[index + (direction*8)] = piece

def move_horizontal(index, piece, direction):
    board[index+1] = index
    board[index + direction] = piece

def setup():
    global tile
    global number
    for i in range(len(board)):
       tile = pygame.Rect(((100 + (i%8)*50),(100 + 50 * (math.floor(i/8))), 50, 50))
       pygame.draw.rect(screen, (255, 255, 255), tile)
       number = number + 1


def update():
    screen.fill((0, 0, 0))
    pygame.display.update()
    setup()




run = True
screen.fill((0, 0, 0))
update()
while run:
    

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            run = False
    
    

pygame.quit()



