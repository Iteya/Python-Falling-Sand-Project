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

grid_width = screen.get_width() // 5
grid_height = screen.get_height() // 5
grid = [[0 for _ in range(grid_height)] for _ in range(grid_width + 1)]
width = len(grid)
height = len(grid[1])


def Sand(x, y):
    if grid[x][y + 1] == 0:
        grid[x][y] = 0
        return (x, y + 1)
    if grid[x + 1][y + 1] == 0:
        grid[x][y] = 0
        return (x + 1, y + 1)
    if grid[x - 1][y + 1] == 0:
        grid[x][y] = 0
        return (x - 1, y + 1)
    return (x, y)

def Water(x, y):
    if grid[x][y + 1] != 0:
        dir = random.choice([-1, 1])
        if grid[x + dir][y + 1] == 0:
            grid[x][y] = 0
            return (x + dir, y + 1)
        elif grid[x + dir][y] == 0:
            grid[x][y] = 0
            return (x + dir, y)
    elif grid[x][y + 1] == 0:
        if grid[x][y + 2] == 0:
            grid[x][y] = 0
            return (x, y + 2)
        grid[x][y] = 0
        return (x, y + 1)
    return (x, y)

def MoveSquare(x, y):
    try:
        if grid[x][y] == 1:
            return(Sand(x, y))
        elif grid[x][y] == 2:
            return(Water(x, y))
        else:
            grid[x][y] = 0
            return (x, y)
    except:
        return(x, y)

def DrawSquare(col, left, top, width, height):
    pygame.draw.rect(screen, col, (left, top, width, height), 5)


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
        squares.append(((mouse_x // 5), (mouse_y // 5)))
        type.append(random.randint(2, 2))
        grid[(mouse_x // 5)][(mouse_y // 5)] = 1
    
    
    screen.fill("black")

    for i, (x, y) in enumerate(squares):
        squares[i] = MoveSquare(x, y)
        

    for a, (x, y) in enumerate(squares):
        grid[x][y] = type[a]
        if type[a] == -1:
            DrawSquare("gray", x * 5, y * 5, 5, 5)
        if type[a] == 1:
            DrawSquare("red", x * 5, y * 5, 5, 5)
        if type[a] == 2:
            DrawSquare("blue", x * 5, y * 5, 5, 5)

    # flip() the display to put your work on screen
    pygame.display.flip()

    clock.tick(60)  # limits FPS to 60

pygame.quit()