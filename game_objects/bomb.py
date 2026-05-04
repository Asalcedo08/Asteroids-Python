import pygame
from game_objects.entity import Entity
from constants import LINE_WIDTH
from debug.logger import log_event

class Bomb(Entity):
    #Nested class for bomb explosion objects
    class Explosion(Entity):
        def __init__(self, x, y, radius):
            super().__init__(x, y)
            self.radius = radius
            self.image = pygame.Surface((radius * 2, radius * 2), pygame.SRCALPHA)
            pygame.draw.circle(self.image, "white", (radius, radius), radius)
            self.rect = self.image.get_rect(center=self.position)
            self.mask = pygame.mask.from_surface(self.image)

    def __init__(self, x, y, radius, explosion_radius):
        super().__init__(x, y)
        self.explosion_radius = explosion_radius
        self.radius = radius
        self.image = pygame.Surface((self.radius * 2, self.radius * 2), pygame.SRCALPHA)
        pygame.draw.circle(self.image, "red", (self.radius, self.radius), self.radius, LINE_WIDTH)
        self.rect = self.image.get_rect(center=self.position)
        self.mask = pygame.mask.from_surface(self.image)

    def draw(self, screen):
        screen.blit(self.image, self.rect)
    
        
    def update(self, dt):
        self.rect.center = self.position
        self.position += self.velocity * dt
    
    def explode(self, asteroids):
        #Create the explosion
        explosion = self.Explosion(self.position[0], self.position[1], self.explosion_radius)
        hit_asteroids = pygame.sprite.spritecollide(explosion, asteroids, False, pygame.sprite.collide_mask)
        #Check if each asteroid is affected by explosion and split
        for hit_asteroid in hit_asteroids:
            log_event("asteroid_hit_with_explosion")
            hit_asteroid.split()

