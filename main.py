import pygame
from constants import SCREEN_WIDTH, SCREEN_HEIGHT, SCOREBOARD_POS_X, SCOREBOARD_POS_Y, SCOREBOARD_WIDTH, \
    SCOREBOARD_HEIGHT, ASTEROID_MAX_RADIUS, ASTEROID_MIN_RADIUS
from controls.input import Input
from debug.logger import log_state
from game_objects.player import Player
from game_objects.asteroid import Asteroid
from game_objects.asteroidfield import AsteroidField
from debug.logger import log_event
from game_objects.shot import Shot
from game_objects.bomb import Bomb
import sys

from ui.scoreboard import Scoreboard


def main():
    #Starting game
    pygame.init()
    print(f"Starting Asteroids with pygame version: {pygame.version.ver}")
    print(f"Screen width: {SCREEN_WIDTH}")
    print(f"Screen height: {SCREEN_HEIGHT}")

    # Screen and clock setup
    clock = pygame.time.Clock()
    dt = 0
    screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
    pygame.display.set_caption("Asteroids")

    # Create scoreboard
    scoreboard = Scoreboard(SCOREBOARD_POS_X, SCOREBOARD_POS_Y, SCOREBOARD_WIDTH, SCOREBOARD_HEIGHT)

    game_input = Input()

    #Create groups
    updatable = pygame.sprite.Group()
    drawable = pygame.sprite.Group()
    asteroids = pygame.sprite.Group()
    shots = pygame.sprite.Group()
    bombs = pygame.sprite.Group()

    #Player and asteroid creation
    Player.containers = (updatable, drawable)
    player = Player(SCREEN_WIDTH / 2, SCREEN_HEIGHT / 2, game_input)
    Asteroid.containers = (asteroids, updatable, drawable)
    AsteroidField.containers = updatable
    AsteroidField()

    #Sets shot, bomb, scoreboard containers
    Shot.containers = (shots, drawable, updatable)
    Bomb.containers = (bombs, drawable, updatable)

    #Game loop
    while True:
        #Logging
        log_state()
            
        #Updating
        dt = clock.tick(60) / 1000
        updatable.update(dt)

        #Check for player collision
        if pygame.sprite.spritecollide(player, asteroids, True, pygame.sprite.collide_mask):
            # End game if player collides
            player.lives -= 1
            if player.lives == 0:
                print("Game over!")
                sys.exit()

        #Check for shots hitting asteroids
        shot_hits = pygame.sprite.groupcollide(shots, asteroids, True, False, pygame.sprite.collide_mask)
        # Split asteroid if shot collides
        for shot, hit_asteroids in shot_hits.items():
            for asteroid in hit_asteroids:
                log_event("asteroid_shot")
                asteroid.split()
                scoreboard.score += 1

        # Check for bombs hitting asteroids
        bomb_hits = pygame.sprite.groupcollide(bombs, asteroids, True, True, pygame.sprite.collide_mask)
        # Bomb asteroid if bomb collides
        for bomb, hit_asteroids in bomb_hits.items():
            for asteroid in hit_asteroids:
                log_event("asteroid_bombed")

                #Calculate asteroid point worth
                asteroid_points = None
                if asteroid.radius == ASTEROID_MAX_RADIUS:
                    asteroid_points = 7
                elif asteroid.radius == ASTEROID_MIN_RADIUS:
                    asteroid_points = 1
                else:
                    asteroid_points = 3

                #Add points of all hit asteroids to score
                scoreboard.score += asteroid_points + bomb.explode(asteroids)

        #Rendering
        screen.fill("black")
        for drawing in drawable:
            drawing.draw(screen)

        scoreboard.draw(screen, player)
        pygame.display.flip()
        

    


if __name__ == "__main__":
    main()
