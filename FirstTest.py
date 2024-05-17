# Example file showing a basic pygame "game loop"
import pygame, random

# pygame setup
pygame.init()
screen_width = 720
screen_height = 1280
screen = pygame.display.set_mode((screen_height, screen_width))
clock = pygame.time.Clock()
running = True
dt = 0
squares = []


type = []
mouse_pressed = False

grid_width = screen.get_width() // 50
grid_height = screen.get_height() // 50
grid = [[0 for _ in range(grid_height)] for _ in range(grid_width + 1)]
width = len(grid)
height = len(grid[1])

def Sand(x, y):
    if grid[x][y + 1] == 0:
        grid[x][y] = 0
        grid[x][y + 1] = 1
        return
    if grid[x][y + 1] == 2:
        grid[x][y] = 2
        grid[x][y + 1] = 1
        return
    if grid[x + 1][y + 1] == 0:
        grid[x][y] = 0
        grid[x + 1][y + 1] = 1
        return
    if grid[x - 1][y + 1] == 0:
        grid[x][y] = 0
        grid[x - 1][y + 1] = 1
        return
    
    return

def Water(x, y):
    if grid[x][y + 1] == 1:
        grid[x][y] = 1
        grid[x][y + 1] = 2
        return
    
    if grid[x][y + 1] != 0:
        dir = random.choice([-1, 1])
        if grid[x + dir][y + 1] == 0:
            grid[x][y] = 0
            grid[x + dir][y + 1] = 2
            return
        elif grid[x + dir][y] == 0:
            grid[x][y] = 0
            grid[x + dir][y] = 2
            return
    elif grid[x][y + 1] == 0:
        grid[x][y] = 0
        grid[x][y + 1] = 2
        return
    
    return

def DrawSquare(col, left, top, width, height):
    pygame.draw.rect(screen, col, (left, top, width, height), 50)

for _ in range(width):
    grid[_][height - 1] = -1
    type.append(-1)
    squares.append((_, height - 1))
    grid[_][0] = -1
    type.append(-1)
    squares.append((_, 0))

for _ in range(height):
    grid[width - 1][_] = -1
    type.append(-1)
    squares.append((width - 1, _))
    grid[0][_] = -1
    type.append(-1)
    squares.append((0, _))


while running:
    # poll for events
    # pygame.QUIT event means the user clicked X to close your window
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
        if event.type == pygame.MOUSEBUTTONDOWN:
            mouse_pressed = True
        if event.type == pygame.MOUSEBUTTONUP:
            mouse_pressed = False

    if mouse_pressed:
        mouse_x, mouse_y = pygame.mouse.get_pos()
        try:
            if grid[mouse_x // 50][mouse_y // 50] == 0:
                grid[(mouse_x // 50)][(mouse_y // 50)] = random.randint(1, 2)
        except:
            print("Out of bounds")
    
    
    screen.fill("black")
        

    for a in range(width):
        for b in range(height):
            #Move Phase
            if grid[a][b] == 1:
                Sand(a, b)
            elif grid[a][b] == 2:
                Water(a, b)

    for a in range(width):
        for b in range(height):
            #Draw Phase
            if grid[a][b] == -1:
                DrawSquare("gray", a * 50, b * 50, 50, 50)
            elif grid[a][b] == 1:
                DrawSquare("red", a * 50, b * 50, 50, 50)
            elif grid[a][b] == 2:
                DrawSquare("blue", a * 50, b * 50, 50, 50)
        
    # flip() the display to put your work on screen
    pygame.display.flip()

    clock.tick(10)  # limits FPS to 60

pygame.quit()