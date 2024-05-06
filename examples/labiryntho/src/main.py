from typing import override

import pygame as pg

from src import GraphicsEngine
from src.renderers import Renderer
from src.camera import SpectatorPlayer, PhysicsPlayer
from src.light import CameraFollowingLight

from .scenes import *
from .dimensions import *
from .config import *
from .maze import Maze


class Game(GraphicsEngine):
    def __init__(self):
        super().__init__(APP_NAME, WINDOW_SIZE, TEXTURES_DIR_PATH, FONTS_DIR_PATH, icon_path=ICON_PATH)
        self.key_binds = KeyBinds()

        self.maze = Maze()

        self.light = CameraFollowingLight(self, position=(0, 0, 0), specular=0)

        self.physics_player = PhysicsPlayer(self, position=(0, 0, 0), far=CAMERA_FAR)
        self.spectator_player = SpectatorPlayer(self, far=CAMERA_FAR)
        self.current_camera = CameraType.PHYSICS
        self.camera = self.physics_player
        self.always_update_camera = False

        self.maze_dimension = MazeDimension(self, GameDimension.MAZE)
        self.menus_dimension = MenusDimension(self, GameDimension.MENUS)
        self.dimension = self.menus_dimension
        self.menus_dimension.use()

        self.debug_info_renderer = Renderer(self, DebugInfoScene(self, "main_debug_info"))
        self.render_debug = False

    def set_dimension(self, dimension):
        self.dimension.un_use()
        self.dimension = dimension
        self.dimension.use()

    def handle_events(self):
        for event in pg.event.get():
            if event.type == pg.QUIT:
                self.quit()

            self.dimension.handle_events(event)

            if event.type != pg.KEYDOWN:
                continue

            key = event.key
            if key == self.key_binds.change_camera:
                match self.current_camera:
                    case CameraType.PHYSICS:
                        self.current_camera = CameraType.SPECTATOR
                        self.spectator_player.use_vars_from(self.camera)
                        self.camera = self.spectator_player

                    case CameraType.SPECTATOR:
                        self.current_camera = CameraType.PHYSICS
                        self.physics_player.use_vars_from(self.camera)
                        self.camera = self.physics_player

            if key == self.key_binds.free_camera:
                self.always_update_camera = not self.always_update_camera

            if key == self.key_binds.show_debug:
                self.render_debug = not self.render_debug

    @override
    def render(self):
        self.dimension.render_one()

        if self.render_debug:
            self.debug_info_renderer.render()

        if self.always_update_camera:
            self.camera.update()

        self.light.update()
        super().render()

    @override
    def on_tick_exception(self, e):
        if f"{e}" == "video system not initialized":
            return

        log(f"Exception occurred while ticking: ({e})", level=LogLevel.ERROR)
        super().on_tick_exception(e)

    @override
    def mainloop(self):
        log("App start", level=LogLevel.INFO)
        super().mainloop()
        log("App quit\n", level=LogLevel.INFO)


if __name__ == "__main__":
    game = Game()
    game.mainloop()
