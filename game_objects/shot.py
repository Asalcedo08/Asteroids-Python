import pygame
from game_objects.entity import Entity
from constants import LINE_WIDTH

class Shot(Entity):
    def __init__(self, x, y, radius):
        super().__init__(x, y)
        self.radius = radius
        self.image = pygame.Surface((self.radius * 2, self.radius * 2), pygame.SRCALPHA)
        pygame.draw.circle(self.image, "yellow", (self.radius, self.radius), self.radius, LINE_WIDTH)
        self.rect = self.image.get_rect(center=self.position)
        self.mask = pygame.mask.from_surface(self.image)


    def draw(self, screen):
        screen.blit(self.image, self.rect)
    
    def update(self, dt):
        self.rect.center = self.position
        self.position += self.velocity * dt