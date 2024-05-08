# Example file showing a basic pygame "game loop"
import pygame, random

# pygame setup
pygame.init()
screen = pygame.display.set_mode((1280, 720))
clock = pygame.time.Clock()
running = True
dt = 0

player_pos = pygame.Rect(10, 10, 5, 5)

while running:
    # poll for events
    # pygame.QUIT event means the user clicked X to close your window
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

    # fill the screen with a color to wipe away anything from last frame
    screen.fill("black")

    # pygame.draw.rect(screen, "Red", player_pos, 10)
    pygame.draw.rect(screen, "red", player_pos, 10)
    if player_pos.top < screen.get_height() - 10:
        player_pos.top += 1
    
    # flip() the display to put your work on screen
    pygame.display.flip()

    clock.tick(60)  # limits FPS to 60

pygame.quit()