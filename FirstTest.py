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

grid_width = screen.get_width() // 50
grid_height = screen.get_height() // 50
grid = [[0 for _ in range(grid_height)] for _ in range(grid_width)]
print(grid[24])


def MoveSquare(x, y):
    try:
        if grid[x][y] == 1:
            print("exists")
            if grid[x][y - 1] == 0:
                print("moved")
                grid[x][y] = 0
                grid[x][y + 1] = 1
                return (x, y + 1)
            else:
                print("Something's below me")
                return (x, y)
        else:
            return(x, y)
    except:
        print("Broken :(")
        return(x, y)

def DrawSquare(left, top, width, height):
    pygame.draw.rect(screen, "red", (left, top, width, height), 2)


while running:
    # poll for events
    # pygame.QUIT event means the user clicked X to close your window
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
        if event.type == pygame.MOUSEBUTTONDOWN:
            if event.button == 1:
                mouse_x, mouse_y = pygame.mouse.get_pos()
                squares.append(((mouse_x // 50) - 1, (mouse_y // 50) - 1))
                grid[(mouse_x // 50) - 1][(mouse_y // 50) -1] = 1
    screen.fill("black")

    #updated_squares = []
    #for (x, y) in squares:
    #    updated_position = Square(x, y, 5, 5)
    #    if updated_position is not None:
    #        updated_squares.append(updated_position)

    #squares = updated_squares
    
    for i, (x, y) in enumerate(squares):
        squares[i] = MoveSquare(x, y)
        DrawSquare(x * 50, y * 50, 50, 50)

    # flip() the display to put your work on screen
    pygame.display.flip()

    clock.tick(60)  # limits FPS to 60

pygame.quit()