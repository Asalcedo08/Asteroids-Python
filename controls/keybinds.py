from enum import Enum, auto


class Keybinds(Enum):
    #Creating action enums
    MOVE_FORWARD = auto()
    MOVE_BACKWARD = auto()
    ROTATE_LEFT = auto()
    ROTATE_RIGHT = auto()
    SHOOT = auto()
    BOMB = auto()
    PAUSE = auto()
