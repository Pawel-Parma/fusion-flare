import os.path as op

import pygame as pg
import moderngl as gl

from config import *
from camera import SpectatorPlayer, PhysicsPlayer
from light import Light, CameraFollowingLight
from opengl_pipeline import Mesh
from scenes import *
from maze import Maze

# GAME
# TODO: Make faster by utilising chunks and not rendering everything at once, more culling
# TODO: add debug screen (F3)

# TODO: Make main menu and its functionality
# Play button and screen
# Settings button and screen [audio, graphics, controls, credits]
# Exit button
# Shop button [coming soon]
# History button

# TODO: Make escape menu
# Resume
# Save
# Settings
# Exit

# TODO: Make end screen
# Time
# Score
# Coins
# Name
# Play-through [shows correct path with green]

# Play again [shows play screen and same setting]
# Main menu

# TODO: Make database

# FINISHING TOUCHES
# TODO: show time, coins and score when playing

# TODO: IF TIME
# Custom music and sound
# Make coin power-ups [has compass, shows where to go, speed boost, etc.]
# Add shop
# Allow true 3D with stairs
# Enemies
# Make custom map generator


class GraphicsEngine:
    def __init__(self):
        self.run: bool = True
        self.show = ToShow.MAIN_MENU
        self.key_binds = KeyBinds()
        # init pygame
        pg.init()
        # set OpenGL version
        pg.display.gl_set_attribute(pg.GL_CONTEXT_MAJOR_VERSION, 3)
        pg.display.gl_set_attribute(pg.GL_CONTEXT_MINOR_VERSION, 3)
        # set OpenGL profile
        pg.display.gl_set_attribute(pg.GL_CONTEXT_PROFILE_MASK, pg.GL_CONTEXT_PROFILE_CORE)
        # create OpenGL context
        pg.display.set_mode(size=(WINDOW_WIDTH, WINDOW_HEIGHT), flags=(pg.DOUBLEBUF | pg.OPENGL))
        # window settings
        pg.display.set_caption(APP_NAME)
        pg.display.set_icon(pg.image.load(f"{IMAGES_DIR}/{ICON_NAME}"))
        # mouse settings
        pg.event.set_grab(True)
        pg.mouse.set_visible(False)
        # detect and use existing opengl context
        self.ctx = gl.create_context()
        self.ctx.enable(flags=(gl.DEPTH_TEST | gl.CULL_FACE | gl.BLEND))
        self.ctx.gc_mode = "auto"
        # get fps clock
        self.clock = pg.time.Clock()
        self.time = 0
        self.delta_time = 0
        # maze
        self.maze = Maze(MAZE_WIDTH, MAZE_LENGHT)
        # light
        self.light = CameraFollowingLight(self, Light(position=(0, 0, 0), specular=0))
        # player
        self.physics_player = PhysicsPlayer(self, position=self.maze.start_in_map_coords)
        self.spectator_player = SpectatorPlayer(self)
        self.current_camera = CameraType.PHYSICS
        self.camera = self.physics_player
        # mesh
        self.mesh = Mesh(self)
        # game scene
        self.game_scene = GameScene(self)
        self.game_scene_renderer = GameSceneRenderer(self)
        # main menu scene
        self.main_menu_scene = MainMenuScene(self)
        self.main_menu_scene_renderer = MainMenuSceneRenderer(self)
        # esc menu scene
        self.esc_menu_scene = EscMenuScene(self)
        self.esc_menu_scene_renderer = EscMenuSceneRenderer(self)
        # end game menu scene
        self.end_game_menu_scene = EndGameMenuScene(self)
        self.end_game_menu_scene_renderer = EndGameMenuSceneRenderer(self)

    def get_time(self):
        self.time = pg.time.get_ticks() * 0.001

    def swap_camera(self, camera_to_use):
        camera = self.camera
        self.camera = camera_to_use
        self.camera.position = camera.position
        self.camera.yaw = camera.yaw
        self.camera.pitch = camera.pitch
        self.camera.up = camera.up
        self.camera.right = camera.right
        self.camera.front = camera.front
        self.camera.m_view = camera.m_view
        self.camera.m_proj = camera.m_proj

    def quit(self):
        pg.quit()
        self.run = False

    def play(self, new_maze=False):
        if new_maze:
            self.maze.new(MAZE_WIDTH, MAZE_LENGHT)
            self.game_scene.update()

        self.show = ToShow.GAME

    def main_menu(self):
        self.show = ToShow.MAIN_MENU

    def esc_menu(self):
        self.show = ToShow.ESC_MENU

    def end_game_menu(self):
        self.show = ToShow.END_GAME_MENU

    def handle_events(self):
        for event in pg.event.get():
            if event.type == pg.QUIT:
                self.quit()

            # Continue if no keys pressed
            if event.type != pg.KEYDOWN:
                continue

            key = event.key
            # Menus
            if key == self.key_binds.esc_menu:
                match self.show:
                    case ToShow.GAME:
                        self.esc_menu()

                    case ToShow.ESC_MENU:
                        self.play()

            # CHEAT CODES
            if key == self.key_binds.spectator_camera:
                match self.current_camera:
                    case CameraType.PHYSICS:
                        self.current_camera = CameraType.SPECTATOR
                        self.spectator_player.use_vars_from(self.camera)
                        self.camera = self.spectator_player

                    case CameraType.SPECTATOR:
                        self.current_camera = CameraType.PHYSICS
                        self.physics_player.use_vars_from(self.camera)
                        self.camera = self.physics_player

    def render(self):
        match self.show:
            case ToShow.GAME:
                self.render_game()

            case ToShow.MAIN_MENU:
                self.render_main_menu()

            case ToShow.ESC_MENU:
                self.render_esc_menu()

            case ToShow.END_GAME_MENU:
                self.render_end_game_menu()

        self.light.update()
        # swap buffers
        pg.display.flip()

    def render_game(self):
        # background color
        self.ctx.clear(*SKY_COLOR)
        # render scene
        self.game_scene_renderer.render()
        # update camera
        self.camera.update()
        # check win
        temp = self.camera.position.xyz
        temp.x = round(temp.x)
        temp.y = round(temp.y)
        temp.z = round(temp.z)
        if self.maze.end_in_map_coords == temp:
            self.end_game_menu()

    # remove in the future
    # TODO: make the camera position independent of each scene
    def set_camera_where_buttons_are(self):
        self.camera.position.x = 0
        self.camera.position.y = 0
        self.camera.position.z = 10
        self.camera.yaw = 4.72
        self.camera.pitch = 0
        self.camera.update_vectors()
        self.camera.update_view_matirx()

    def render_main_menu(self):
        # background color
        self.ctx.clear(*MENU_COLOR)
        # render scene
        self.main_menu_scene_renderer.render()

        # remove in the future
        self.set_camera_where_buttons_are()

    def render_esc_menu(self):
        # background color
        self.ctx.clear(*MENU_COLOR)
        # render scene
        self.esc_menu_scene_renderer.render()

        # remove in the future
        self.set_camera_where_buttons_are()

    def render_end_game_menu(self):
        # background color
        self.ctx.clear(*MENU_COLOR)
        # render scene
        self.end_game_menu_scene_renderer.render()

        # remove in the future
        self.set_camera_where_buttons_are()

    def mainloop(self):
        while self.run:
            log(f"FPS: {self.clock.get_fps():.2f}")
            self.delta_time = self.clock.tick()  # FPS
            self.render()
            self.handle_events()
            self.get_time()


if __name__ == "__main__":
    app = GraphicsEngine()
    app.mainloop()
