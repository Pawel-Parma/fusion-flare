import typing

import glm


LOGGER_NAME: str = "base_logger"
LOGS_DIR: str = "examples/labiryntho/logs"

APP_NAME: str = "Labiryntho"
ICON_PATH: str = "examples/labiryntho/textures/logo.png"

WINDOW_WIDTH: int = 1200
WINDOW_HEIGHT: int = 700
WINDOW_SIZE = (WINDOW_WIDTH, WINDOW_HEIGHT)
MAZE_WIDTH = 50
MAZE_LENGHT = 30
FPS: int = 60
DISABLE_SHADOW_RENDER: bool = True  # SHADOWS ARE EXPERIMENTAL AND WILL CAUSE ISSUES


def normalize_color(r, g, b):
    return glm.vec3(r, g, b) / 255


SKY_COLOR: glm.vec3 = normalize_color(90, 208, 255)
MENU_COLOR: glm.vec3 = normalize_color(70, 70, 70)

PI = glm.pi()

FONTS_DIR: str = "fonts/"
SHADERS_DIR: str = "shaders/"
TEXTURES_DIR: str = "textures/"

CAMERA_FOV: float = 50  # deg
CAMERA_NEAR: float = 0.1
CAMERA_FAR: float = 80
CAMERA_SPEED: float = 0.01
MOUSE_SENSITIVITY: float = 0.002
CAMERA_PITCH_MAX: float = 89
CAMERA_PITCH_MIN: float = -89


del typing, glm