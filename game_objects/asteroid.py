from game_objects.circleshape import CircleShape
from constants import LINE_WIDTH, ASTEROID_MIN_RADIUS
from debug.logger import log_event
import pygame
import random

class Asteroid(CircleShape):
    def __init__(self, x, y, radius):
        super().__init__(x, y, radius)
    
    def draw(self, screen):
        pygame.draw.circle(screen, "white", self.position, self.radius, LINE_WIDTH)
    
    def update(self, dt):
        self.rect.center = self.position
        self.position += self.velocity * dt

    #Astroid splitting
    def split(self):
        #Kill the current asteroid and check if it's splittable
        self.kill()
        if self.radius == ASTEROID_MIN_RADIUS:
            return

        log_event("asteroid_split")

        #Create split asteroids
        angle = random.uniform(20, 50)
        new_asteroid_vel = self.velocity.rotate(angle)
        new_asteroid_vel2 = self.velocity.rotate(-angle)
        new_radius = self.radius - ASTEROID_MIN_RADIUS

        asteroid1 = Asteroid(self.position[0], self.position[1], new_radius)
        asteroid2 = Asteroid(self.position[0], self.position[1], new_radius)

        asteroid1.velocity = new_asteroid_vel * 1.2
        asteroid2.velocity = new_asteroid_vel2 * 1.2