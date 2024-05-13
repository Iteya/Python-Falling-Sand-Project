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
grid = [[False for _ in range(grid_width)] for _ in range(grid_height)]


def Square(left, top, width, height):
    grid_x = left // width
    grid_y = top // height

    if grid_y < len(grid) and grid_x < len(grid[0]) and grid[grid_y][grid_x]:
        return None

    pygame.draw.rect(screen, "red", (left, top, width, height), 2)

    if grid_y < len(grid) and grid_x < len(grid[0]):
        grid[grid_y][grid_x] = True

    new_top = top + height
    if new_top < screen_height:
        return (left, new_top)
    else:
        return None


while running:

    # poll for events
    # pygame.QUIT event means the user clicked X to close your window
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
        if event.type == pygame.MOUSEBUTTONDOWN:
                if event.button == 1:
                    mouse_x, mouse_y = pygame.mouse.get_pos()
                    squares.append((mouse_x, mouse_y))

    screen.fill("black")

    updated_squares = []
    for (x, y) in squares:
        updated_position = Square(x, y, 5, 5)
        if updated_position is not None:
            updated_squares.append(updated_position)

    squares = updated_squares

    # flip() the display to put your work on screen
    pygame.display.flip()

    clock.tick(60)  # limits FPS to 60

pygame.quit()