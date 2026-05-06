import pygame
from game_objects.entity import Entity
from constants import LINE_WIDTH, PLAYER_TURN_SPEED, PLAYER_MAX_SPEED, SHOT_RADIUS, PLAYER_SHOOT_SPEED, \
    PLAYER_SHOOT_COOLDOWN_SECONDS, PLAYER_BOMB_COOLDOWN_SECONDS, BOMB_RADIUS, BOMB_EXPLOSION_RADIUS, PLAYER_SIZE, \
    SCREEN_WIDTH, SCREEN_HEIGHT, SCOREBOARD_HEIGHT, PLAYER_ACCELERATION, FRICTION
from game_objects.shot import Shot
from game_objects.bomb import Bomb

class Player(Entity):
    def __init__(self, x, y, game_input):
        super().__init__(x, y)

        self.image = pygame.Surface((PLAYER_SIZE * 3, PLAYER_SIZE * 3), pygame.SRCALPHA)
        self.rect = self.image.get_rect(center=self.position)
        self.mask = pygame.mask.from_surface(self.image)

        self.nose = None

        self.rotation = 0
        self.shot_cooldown = 0
        self.bomb_cooldown = PLAYER_BOMB_COOLDOWN_SECONDS

        self.max_lives = 3
        self.lives = 3
        self.max_bombs = 3
        self.bombs = 1

        self.velocity = pygame.Vector2(0, 0)

        self.game_input = game_input
    
    def triangle(self):
        canvas_center = pygame.Vector2(self.image.get_width() / 2, self.image.get_height() / 2)
        #Create triangle shape for player
        forward = pygame.Vector2(0, 1).rotate(self.rotation)
        right = pygame.Vector2(0, 1).rotate(self.rotation + 90) * PLAYER_SIZE / 1.5
        self.nose = self.position + forward * PLAYER_SIZE
        a = canvas_center + forward * PLAYER_SIZE
        b = canvas_center - forward * PLAYER_SIZE - right
        c = canvas_center - forward * PLAYER_SIZE + right
        return [a, b, c]
    
    def draw(self, screen):
        #Update rect to match current position
        self.rect.center = (self.position.x, self.position.y)
        #Update player image and set mask again
        self.image.fill((0, 0, 0, 0))
        pygame.draw.polygon(self.image, "green", self.triangle(), LINE_WIDTH)
        self.mask = pygame.mask.from_surface(self.image)
        #Copy to screen
        screen.blit(self.image, self.rect)

    def rotate(self, dt):
        self.rotation += PLAYER_TURN_SPEED * dt

    def update(self, dt):
        #Update player timers
        self.shot_cooldown -= dt
        if self.bombs != self.max_bombs:
            self.bomb_cooldown -= dt

        #Adds bomb and resets timer if ready and less than 3 bombs
        if self.bomb_cooldown <= 0 and self.bombs < self.max_bombs:
            self.bombs += 1
            self.bomb_cooldown = PLAYER_BOMB_COOLDOWN_SECONDS

        self.game_input.input_action(self, dt)

        #Slow down using friction
        self.velocity *= FRICTION

        #Cap speed and update position
        if self.velocity.length() > PLAYER_MAX_SPEED:
            self.velocity.scale_to_length(PLAYER_MAX_SPEED)

        self.position += self.velocity * dt




    def move(self, dt):
        # Create rotated vector
        forward = pygame.Vector2(0, 1).rotate(self.rotation)

        # Calculate and add acceleration to velocity
        acceleration = forward * PLAYER_ACCELERATION * dt
        self.velocity += acceleration

        #Move rect attribute
        self.rect.center = self.position

        if self.position[0] < -PLAYER_SIZE:
            self.position[0] = SCREEN_WIDTH + PLAYER_SIZE

        elif self.position[0] > SCREEN_WIDTH + PLAYER_SIZE:
            self.position[0] = -PLAYER_SIZE

        if self.position[1] < -PLAYER_SIZE:
            self.position[1] = SCREEN_HEIGHT - SCOREBOARD_HEIGHT + PLAYER_SIZE

        elif self.position[1] > SCREEN_HEIGHT - SCOREBOARD_HEIGHT + PLAYER_SIZE:
            self.position[1] = -PLAYER_SIZE

    def shoot(self):
        #Check if shot timer is ready
        if self.shot_cooldown <= 0:
            #Reset timer
            self.shot_cooldown = PLAYER_SHOOT_COOLDOWN_SECONDS
            #Create shot and set velocity
            shot = Shot(self.nose.x, self.nose.y, SHOT_RADIUS)
            vector = pygame.Vector2(0, 1)
            vector = vector.rotate(self.rotation)
            vector *= PLAYER_SHOOT_SPEED
            shot.velocity = vector

    def bomb(self):
        #Check if bombs are available and creates
        if self.bombs > 0:
            self.bombs -= 1
            #Create bomb and set velocity
            bomb = Bomb(self.nose.x, self.nose.y, BOMB_RADIUS, BOMB_EXPLOSION_RADIUS)
            vector = pygame.Vector2(0, 1)
            vector = vector.rotate(self.rotation)
            vector *= PLAYER_SHOOT_SPEED
            bomb.velocity = vector
