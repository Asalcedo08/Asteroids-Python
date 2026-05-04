import pygame
from game_objects.circleshape import CircleShape
from constants import LINE_WIDTH
from debug.logger import log_event

class Bomb(CircleShape):
    #Nested class for bomb explosion objects
    class Explosion(CircleShape):
        def __init__(self, x, y, radius):
            super().__init__(x, y, radius)

    def __init__(self, x, y, radius, explosion_radius):
        super().__init__(x, y, radius)
        self.explosion_radius = explosion_radius

    def draw(self, screen):
        pygame.draw.circle(screen, "red", self.position, self.radius, LINE_WIDTH)
    
        
    def update(self, dt):
        self.rect.center = self.position
        self.position += self.velocity * dt
    
    def explode(self, asteroids):
        #Create the explosion
        explosion = self.Explosion(self.position[0], self.position[1], self.explosion_radius)
        hit_asteroids = pygame.sprite.spritecollide(explosion, asteroids, False, pygame.sprite.collide_circle)
        #Check if each asteroid is affected by explosion and split
        for hit_asteroid in hit_asteroids:
            log_event("asteroid_hit_with_explosion")
            hit_asteroid.split()

