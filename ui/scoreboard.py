import pygame

from constants import SCOREBOARD_TEXT_SIZE, SCOREBOARD_TEXT_OFFSET, LINE_WIDTH, SCOREBOARD_LIFE_CONTAINER_OFFSET, \
    SCOREBOARD_BOMB_CONTAINER_OFFSET


class Scoreboard:
    def __init__(self, x, y, width, height):
        self.y = y
        self.width = width
        self.board = pygame.Rect((x, y), (width, height))
        self.font = pygame.font.SysFont('Arial', SCOREBOARD_TEXT_SIZE)
        self.score = 0
        self.life_containers = [pygame.Rect((x + 125, y + SCOREBOARD_LIFE_CONTAINER_OFFSET), (75, SCOREBOARD_TEXT_SIZE)),
             pygame.Rect((x + 210, y + SCOREBOARD_LIFE_CONTAINER_OFFSET), (75, SCOREBOARD_TEXT_SIZE)),
             pygame.Rect((x + 295, y + SCOREBOARD_LIFE_CONTAINER_OFFSET), (75, SCOREBOARD_TEXT_SIZE)),
             pygame.Rect((x + 380, y + SCOREBOARD_LIFE_CONTAINER_OFFSET), (75, SCOREBOARD_TEXT_SIZE)),
             pygame.Rect((x + 465, y + SCOREBOARD_LIFE_CONTAINER_OFFSET), (75, SCOREBOARD_TEXT_SIZE))]

        self.bomb_container_center_and_radius = [
            ((715, self.y + SCOREBOARD_BOMB_CONTAINER_OFFSET), 15),
            ((755, self.y + SCOREBOARD_BOMB_CONTAINER_OFFSET), 15),
            ((795, self.y + SCOREBOARD_BOMB_CONTAINER_OFFSET), 15)]

    def draw(self, screen, player):
        pygame.draw.rect(screen, (128, 128, 128), self.board)
        score_string = self.font.render("Score: " + str(self.score), True, "black")
        screen.blit(score_string, (self.width - 150, self.y + SCOREBOARD_TEXT_OFFSET))
        lives_string = self.font.render("Lives:", True, "black")
        screen.blit(lives_string, (self.width - 1250, self.y + SCOREBOARD_TEXT_OFFSET))
        bombs_string = self.font.render("Bombs:", True, "black")
        screen.blit(bombs_string, (self.width - 700, self.y + SCOREBOARD_TEXT_OFFSET))

        #Life container creation
        for i in range(0, player.max_lives):
            if i < player.lives:
                pygame.draw.rect(screen, (26, 255, 0), self.life_containers[i])
            else:
                pygame.draw.rect(screen, (26, 255, 0), self.life_containers[i], LINE_WIDTH)

        #Bomb container creation
        for i in range(0, player.max_bombs):
            if i < player.bombs:
                pygame.draw.circle(screen,
                                    (255, 0, 0),
                                    self.bomb_container_center_and_radius[i][0],
                                    self.bomb_container_center_and_radius[i][1])
            else:
                pygame.draw.circle(screen,
                                    (255, 0, 0),
                                    self.bomb_container_center_and_radius[i][0],
                                    self.bomb_container_center_and_radius[i][1],
                                    LINE_WIDTH)
