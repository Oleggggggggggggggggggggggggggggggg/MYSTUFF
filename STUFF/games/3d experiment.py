import pygame
pygame.init()
grid = []
grid_width = 12
grid_height = 8
grid_depth = 10
block_index = 0
block_size = 1
collided = None
block = None
camerax = 0
cameray = 0
cameraz = 0
camerarothor = 0
camerarotver = 0

def fill_grid():
    for i in range(1, grid_width * grid_height * grid_depth + 1):
        grid.append(i)


def get_grid_index_position(x, y, z):
    block_index = 1
    block_index = block_index + round(x / block_size)
    block_index = block_index + round((y / block_size) * grid_width)
    block_index = block_index + round((z / block_size) * (grid_width * grid_height))
    block = grid[block_index]

def place_block(block, x, y, z):
    get_grid_index_position((x * block_size), (y * block_size), (z * block_size))
    grid[block_index] = block

def check_collision(x, y, z):
    collided = None
    if x < 0 or (x < (grid_width * block_size)) == False:
        return None
    if y < 0 or (y < (grid_height * block_size)) == False:
        return None
    if z < 0 or (z < (grid_depth * block_size)) == False:
        return None
    get_grid_index_position(x, y, z)
    if block > 0:
        collided = 1
    



fill_grid()
place_block(100, 0, 0, 0)
place_block(200, 0, 0, 1)
place_block(300, 2, 1, 0) 

screenwidth = 800
screenheight = 600
run = True
screen = pygame.display.set_mode((screenwidth, screenheight))
while run:
    screen.fill((0, 0, 0))


    for event in pygame.event.get():
       if event.type == pygame.QUIT:
           run = False
    pygame.display.update()

pygame.quit()
print(grid)


