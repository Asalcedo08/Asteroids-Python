from game_objects.entity import Entity
from constants import LINE_WIDTH, ASTEROID_MIN_RADIUS
from debug.logger import log_event
import pygame
import random

class Asteroid(Entity):
    def __init__(self, x, y, radius):
        super().__init__(x, y)
        self.radius = radius
        self.image = pygame.Surface((self.radius * 2, self.radius * 2), pygame.SRCALPHA)
        pygame.draw.circle(self.image, "white", (self.radius, self.radius), self.radius, LINE_WIDTH)
        self.rect = self.image.get_rect(center=self.position)
        self.mask = pygame.mask.from_surface(self.image)
    
    def draw(self, screen):
        screen.blit(self.image, self.rect)
    
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