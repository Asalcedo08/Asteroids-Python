import pygame
from constants import SCREEN_WIDTH, SCREEN_HEIGHT
from logger import log_state
from player import Player

def main():
    pygame.init()
    print(f"Starting Asteroids with pygame version: {pygame.version.ver}")
    print(f"Screen width: {SCREEN_WIDTH}")
    print(f"Screen height: {SCREEN_HEIGHT}")

    # Screen and clock setup
    clock = pygame.time.Clock()
    dt = 0
    screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))

    #Create groups
    updatable = pygame.sprite.Group()
    drawable = pygame.sprite.Group()

    #Player creation
    Player.containers = (updatable, drawable)
    player = Player(SCREEN_WIDTH / 2, SCREEN_HEIGHT / 2)

    #Game loop
    while True:
        #Logging
        log_state()
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                return
            
        #Updating
        dt = clock.tick(60) / 1000
        updatable.update(dt)

        #Rendering
        screen.fill("black")
        for drawing in drawable:
            drawing.draw(screen)
        pygame.display.flip()
        

    


if __name__ == "__main__":
    main()
