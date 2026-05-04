import pygame
from circleshape import CircleShape
from constants import PLAYER_RADIUS, LINE_WIDTH, PLAYER_TURN_SPEED, PLAYER_SPEED, SHOT_RADIUS, PLAYER_SHOOT_SPEED, PLAYER_SHOOT_COOLDOWN_SECONDS, PLAYER_BOMB_COOLDOWN_SECONDS, BOMB_RADIUS, BOMB_EXPLOSION_RADIUS
from shot import Shot
from bomb import Bomb

class Player(CircleShape):
    def __init__(self, x, y):
        super().__init__(x, y, PLAYER_RADIUS)
        self.rotation = 0
        self.shot_cooldown = 0
        self.bomb_cooldown = 0
    
    # in the Player class
    def triangle(self):
        forward = pygame.Vector2(0, 1).rotate(self.rotation)
        right = pygame.Vector2(0, 1).rotate(self.rotation + 90) * self.radius / 1.5
        a = self.position + forward * self.radius
        b = self.position - forward * self.radius - right
        c = self.position - forward * self.radius + right
        return [a, b, c]
    
    def draw(self, screen):
        pygame.draw.polygon(screen, "white", self.triangle(), LINE_WIDTH)
    
    def rotate(self, dt):
        self.rotation += PLAYER_TURN_SPEED * dt

    def update(self, dt):
        self.shot_cooldown -= dt
        self.bomb_cooldown -= dt
        keys = pygame.key.get_pressed()

        if keys[pygame.K_a]:
            self.rotate(-dt)
        if keys[pygame.K_d]:
            self.rotate(dt)
        if keys[pygame.K_w]:
            self.move(dt)
        if keys[pygame.K_s]:
            self.move(-dt)
        if keys[pygame.K_SPACE]:
            self.shoot()
        if keys[pygame.K_LSHIFT]:
            self.bomb()

    def move(self, dt):
        unit_vector = pygame.Vector2(0, 1)
        rotated_vector = unit_vector.rotate(self.rotation)
        rotated_with_speed_vector = rotated_vector * PLAYER_SPEED * dt
        self.position += rotated_with_speed_vector

    def shoot(self):
        if self.shot_cooldown <= 0:
            self.shot_cooldown = PLAYER_SHOOT_COOLDOWN_SECONDS
            shot = Shot(self.position[0], self.position[1], SHOT_RADIUS)
            vector = pygame.Vector2(0, 1)
            vector = vector.rotate(self.rotation)
            vector *= PLAYER_SHOOT_SPEED
            shot.velocity = vector

    def bomb(self):
        if self.bomb_cooldown <= 0:
            self.bomb_cooldown = PLAYER_BOMB_COOLDOWN_SECONDS
            bomb = Bomb(self.position[0], self.position[1], BOMB_RADIUS, BOMB_EXPLOSION_RADIUS)
            vector = pygame.Vector2(0, 1)
            vector = vector.rotate(self.rotation)
            vector *= PLAYER_SHOOT_SPEED
            bomb.velocity = vector
