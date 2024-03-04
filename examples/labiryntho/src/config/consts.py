from src.i_dont_know_how_to_call_that_package import Color


LOGGER_NAME: str = "base_logger"
LOGS_DIR: str = "examples/labiryntho/logs"

APP_NAME: str = "Labiryntho"
ICON_PATH: str = "examples/labiryntho/textures/logo.png"

WINDOW_WIDTH: int = 1200
WINDOW_HEIGHT: int = 700
WINDOW_SIZE = (WINDOW_WIDTH, WINDOW_HEIGHT)
MAZE_WIDTH = 50
MAZE_LENGTH = 30

SKY_COLOR: Color = Color(90, 208, 255)
MENU_COLOR: Color = Color(70, 70, 70)

TEXTURES_DIR_PATH: str = "examples/labiryntho/textures"
FONTS_DIR_PATH: str = "examples/labiryntho/fonts"

CAMERA_FOV: float = 50  # deg
CAMERA_NEAR: float = 0.1
CAMERA_FAR: float = 80
CAMERA_SPEED: float = 0.01
MOUSE_SENSITIVITY: float = 0.002
CAMERA_PITCH_MAX: float = 89
CAMERA_PITCH_MIN: float = -89
