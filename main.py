import pygame
from constants import *
from player import Player

def main():
    pygame.init()
    screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
    clock = pygame.time.Clock()
    dt = 0
    running = True

    drawables = pygame.sprite.Group()
    updatables = pygame.sprite.Group()

    Player.containers = (drawables, updatables)
    player = Player(SCREEN_WIDTH/2, SCREEN_HEIGHT/2)



    print("Starting asteroids!")
    print(f"Screen width: {SCREEN_WIDTH}")
    print(f"Screen height: {SCREEN_HEIGHT}")
    while running:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False

        keys = pygame.key.get_pressed()
        if keys[pygame.K_q] or keys[pygame.K_ESCAPE]:
            running = False

        screen.fill("black")
        for thing in drawables:
            thing.draw(screen)

        pygame.display.flip()

        dt = clock.tick(60) / 1000

        for thing in updatables:
            thing.update(dt)

if __name__ == "__main__":
    main()
