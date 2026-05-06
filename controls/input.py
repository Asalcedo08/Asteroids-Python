import sys
from controls.keybinds import Keybinds
import pygame


class Input:
    def __init__(self):
        #Creates a dictionary for mapping action enums to keys
        self.keybinds = {
            Keybinds.MOVE_FORWARD: pygame.K_w,
            Keybinds.MOVE_BACKWARD: pygame.K_s,
            Keybinds.ROTATE_LEFT: pygame.K_a,
            Keybinds.ROTATE_RIGHT: pygame.K_d,
            Keybinds.SHOOT: pygame.K_SPACE,
            Keybinds.BOMB: pygame.K_LSHIFT,
            Keybinds.PAUSE: pygame.K_ESCAPE,
        }

    def input_action(self, player, dt):
        keys = pygame.key.get_pressed()
        # Checks for input and applies the effect
        if keys[self.keybinds[Keybinds.ROTATE_LEFT]]:
            player.rotate(-dt)
        if keys[self.keybinds[Keybinds.ROTATE_RIGHT]]:
            player.rotate(dt)
        if keys[self.keybinds[Keybinds.MOVE_FORWARD]]:
            player.move(dt)
        if keys[self.keybinds[Keybinds.MOVE_BACKWARD]]:
            player.move(-dt)
        if keys[self.keybinds[Keybinds.SHOOT]]:
            player.shoot()

        #Checks for exit and keybinds that only trigger one time per press (no hold)
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                sys.exit()
            if event.type == pygame.KEYDOWN:
                if event.key == self.keybinds[Keybinds.BOMB]:
                    player.bomb()
                if event.key == self.keybinds[Keybinds.PAUSE]:
                    pass
