import enum

import pygame as pg


class GameScene(enum.Enum):
    MAIN_MENU = 0
    GAME = 1
    ESC_MENU = 2
    END_GAME_MENU = 3
    SETTINGS_MENU = 4
    HISTORY_MENU = 5


class CameraType(enum.Enum):
    SPECTATOR = 0
    PHYSICS = 1


class KeyBinds:
    def __init__(self):
        self.change_camera = pg.K_F1
        self.free_camera = pg.K_F2
        self.show_debug = pg.K_F3
        self.tab = pg.K_TAB

        self.button_up = (pg.K_w, pg.K_UP)
        self.button_down = (pg.K_s, pg.K_DOWN)
        self.button_left = (pg.K_a, pg.K_LEFT)
        self.button_right = (pg.K_d, pg.K_RIGHT)
        self.button_press = (pg.K_RETURN, pg.K_SPACE)
        self.esc_menu = pg.K_ESCAPE

        self.camera_up = pg.K_SPACE
        self.camera_down = pg.K_LSHIFT
        self.camera_forward = pg.K_w
        self.camera_backward = pg.K_s
        self.camera_left = pg.K_a
        self.camera_right = pg.K_d

    def reset_movement_keys(self):
        self.camera_forward = pg.K_w
        self.camera_backward = pg.K_s
        self.camera_left = pg.K_a
        self.camera_right = pg.K_d
        self.camera_up = pg.K_SPACE
        self.camera_down = pg.K_LSHIFT
