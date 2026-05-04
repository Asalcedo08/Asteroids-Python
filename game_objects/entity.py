import pygame

# Base class for game objects
class Entity(pygame.sprite.Sprite):
    def __init__(self, x, y):
        # we will be using this later
        if hasattr(self, "containers"):
            super().__init__(self.containers)
        else:
            super().__init__()

        self.position = pygame.Vector2(x, y)
        self.velocity = pygame.Vector2(0, 0)

        #Set by children
        self.rect = None
        self.image = None
        self.mask = None

    def draw(self, screen):
        # must override
        pass

    def update(self, dt):
        # must override
        pass