import glm


WINDOW_WIDTH: int = 1200
WINDOW_HEIGHT: int = 700
WINDOW_SIZE = (WINDOW_WIDTH, WINDOW_HEIGHT)
MAZE_WIDTH = 80
MAZE_LENGHT = 80
FPS: int = 60

PI = glm.pi()

SHADERS_DIR: str = "../shaders/"
TEXTURES_DIR: str = "../textures/"

CAMERA_FOV: float = 50  # deg
CAMERA_NEAR: float = 0.1
CAMERA_FAR: float = 100
CAMERA_SPEED: float = 0.01
MOUSE_SENSITIVITY: float = 0.002
CAMERA_PITCH_MAX: float = 89
CAMERA_PITCH_MIN: float = -89

del glm
