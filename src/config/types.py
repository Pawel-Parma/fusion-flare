import enum


class ToShow(enum.Enum):
    MAIN_MENU = 0
    GAME = 1
    ESC_MENU = 2
    END_GAME_MENU = 3


class CameraType(enum.Enum):
    SPECTATOR = 0
    PHYSICS = 1


del enum
