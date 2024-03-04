from typing import override

import pygame as pg
import src

from src.renderers import Renderer
from src.camera import SpectatorPlayer, PhysicsPlayer
from src.light import Light, CameraFollowingLight

from .scenes import *
from .config import *
from .maze import Maze


class Game(src.GraphicsEngine):
    def __init__(self):
        self.optional_shaders_dir = None
        super().__init__(APP_NAME, WINDOW_SIZE, TEXTURES_DIR_PATH, FONTS_DIR_PATH, icon_path=ICON_PATH)
        self.key_binds = KeyBinds()
        # maze
        self.maze = Maze()
        # light
        self.light = CameraFollowingLight(self, Light(position=(0, 0, 0), specular=0))
        # players
        self.physics_player = PhysicsPlayer(self, position=(0, 0, 0), far=CAMERA_FAR)
        self.spectator_player = SpectatorPlayer(self, far=CAMERA_FAR)
        self.current_camera = CameraType.PHYSICS
        self.camera = self.physics_player
        self.always_update_camera = False
        # scenes
        self.maze_renderer = Renderer(self, MazeScene(self))
        self.main_menu_renderer = Renderer(self, MainMenuScene(self))
        self.esc_menu_renderer = Renderer(self, EscMenuScene(self))
        self.end_game_menu_renderer = Renderer(self, EndGameMenuScene(self))
        self.settings_menu_renderer = Renderer(self, SettingsMenuScene(self))
        self.history_menu_renderer = Renderer(self, HistoryMenuScene(self))
        self.render_debug = False
        self.debug_info_renderer = Renderer(self, DebugInfoScene(self))
        self.game_scene = GameScene.MAIN_MENU
        self.renderer = self.main_menu_renderer
        self.renderer.scene.use()
        #
        self.settings_menu_came_from = GameScene.MAIN_MENU

    def set_renderer(self, scene_renderer):
        self.renderer.scene.un_use()
        self.renderer = scene_renderer
        self.renderer.scene.use()

    def play(self, new_maze=False):
        self.game_scene = GameScene.GAME
        self.set_renderer(self.maze_renderer)
        if new_maze:
            self.maze.new(MAZE_WIDTH, MAZE_LENGTH)
            self.maze_renderer.scene.new_maze()
            self.camera.set_position(self.maze.start_in_map_coords)

    def main_menu(self):
        self.game_scene = GameScene.MAIN_MENU
        self.set_renderer(self.main_menu_renderer)

    def esc_menu(self):
        self.game_scene = GameScene.ESC_MENU
        self.set_renderer(self.esc_menu_renderer)

    def end_game_menu(self):
        self.game_scene = GameScene.END_GAME_MENU
        self.set_renderer(self.end_game_menu_renderer)

    def settings_menu(self, came_from):
        self.settings_menu_came_from = came_from
        self.game_scene = GameScene.SETTINGS_MENU
        self.set_renderer(self.settings_menu_renderer)

    def exit_settings_menu(self):
        match self.settings_menu_came_from:
            case GameScene.MAIN_MENU:
                self.main_menu()

            case GameScene.ESC_MENU:
                self.esc_menu()

    def history_menu(self):
        self.game_scene = GameScene.HISTORY_MENU
        self.set_renderer(self.history_menu_renderer)

    def handle_events(self):
        for event in pg.event.get():
            if event.type == pg.QUIT:
                self.quit()

            # Continue if no keys pressed
            if event.type != pg.KEYDOWN:
                continue

            key = event.key
            if key == self.key_binds.esc_menu:
                match self.game_scene:
                    case GameScene.GAME:
                        self.esc_menu()

                    case GameScene.ESC_MENU:
                        self.play()

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
        match self.game_scene:
            case GameScene.GAME:
                self.render_game()

            case GameScene.MAIN_MENU:
                self.render_main_menu()

            case GameScene.ESC_MENU:
                self.render_esc_menu()

            case GameScene.END_GAME_MENU:
                self.render_end_game_menu()

            case GameScene.SETTINGS_MENU:
                self.render_settings_menu()

            case GameScene.HISTORY_MENU:
                self.render_history_menu()

        if self.render_debug:
            self.render_debug_info()

        if self.always_update_camera:
            self.camera.update()

        self.light.update()
        super().render()

    def render_game(self):
        # background color
        self.ctx.clear(*SKY_COLOR)
        # render scene
        self.maze_renderer.render()
        # update camera
        self.camera.update()
        # check win
        temp = self.camera.position.xyz
        temp.x = round(temp.x)
        temp.y = round(temp.y)
        temp.z = round(temp.z)
        if self.maze.end_in_map_coords == temp:
            self.end_game_menu()

    def render_main_menu(self):
        # background color
        self.ctx.clear(*MENU_COLOR)
        # render scene
        self.main_menu_renderer.render()

    def render_esc_menu(self):
        # background color
        self.ctx.clear(*MENU_COLOR)
        # render scene
        self.esc_menu_renderer.render()

    def render_end_game_menu(self):
        # background color
        self.ctx.clear(*MENU_COLOR)
        # render scene
        self.end_game_menu_renderer.render()

    def render_settings_menu(self):
        # background color
        self.ctx.clear(*MENU_COLOR)
        # render scene
        self.settings_menu_renderer.render()

    def render_history_menu(self):
        # background color
        self.ctx.clear(*MENU_COLOR)
        # render scene
        self.history_menu_renderer.render()

    def render_debug_info(self):
        self.debug_info_renderer.render()

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
