from typing import override

import pygame as pg

from src import GraphicsEngine
from src.camera import SpectatorPlayer
from src.light import CameraFollowingLight

from .dimensions import *
from .config import *


class Game(GraphicsEngine):
    def __init__(self):
        super().__init__(APP_NAME, WINDOW_SIZE, TEXTURES_DIR_PATH, FONTS_DIR_PATH)
        self.key_binds = KeyBinds()

        self.light = CameraFollowingLight(self, position=(0, 0, 0), specular=0)

        self.camera = SpectatorPlayer(self, far=CAMERA_FAR, position=(-10, 0, 0))

        self.dimension = DefaultDimension(self, DefaultDimensions.DEFAULT, None)

    def handle_events(self):
        for event in pg.event.get():
            if event.type == pg.QUIT:
                self.quit()

    @override
    def render(self):
        self.dimension.render()

        self.light.update()
        super().render()


if __name__ == "__main__":
    game = Game()
    game.mainloop()
