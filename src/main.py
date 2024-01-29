import os.path as op

import pygame as pg
import moderngl as gl

from config import *
from camera import SpectatorPlayer, PhysicsPlayer
from light import Light, CameraFollowingLight
from opengl_pipeline import Mesh
from scene import GameScene, GameSceneRenderer, MenuScene, MenuSceneRenderer
from maze import Maze

# GAME
# TODO: Make faster by utilising chunks and not rendering everything at once
# TODO: add f3 debug screen

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
# Make coin power-ups [has compass, shows where to go, speed boost, etc.]
# Custom music and sound
# Add shop
# Custom textures [for player to load]
# Allow 3D with stairs [another hard one]
# enemies)
# Make custom map generator and creator [might be hard]


class GraphicsEngine:
    def __init__(self) -> None:
        self.run: bool = True
        self.show = ToShow.GAME
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
        pg.display.set_caption("Labiryntho")
        pg.display.set_icon(pg.image.load(op.join(IMAGES_DIR, "logo.png")))
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
        # self.camera = PhysicsPlayer(self, position=(0, 0, 0))
        self.camera = SpectatorPlayer(self)
        # mesh
        self.mesh = Mesh(self)
        # game scene
        self.game_scene = GameScene(self)
        self.game_scene_renderer = GameSceneRenderer(self)
        # menu scene
        self.menu_scene = MenuScene(self)
        self.menu_scene_renderer = MenuSceneRenderer(self)

    def get_time(self) -> float:
        self.time = pg.time.get_ticks() * 0.001
        return self.time

    def handle_events(self) -> None:
        for event in pg.event.get():
            if event.type == pg.QUIT:
                pg.quit()
                self.run = False

            # FOR TESTING
            if event.type == pg.KEYDOWN:
                if event.key == pg.K_TAB:
                    if self.show == ToShow.GAME:
                        self.show = ToShow.MAIN_MENU

                    elif self.show == ToShow.MAIN_MENU:
                        self.show = ToShow.GAME

    def render(self):
        # background color
        self.ctx.clear(*SKY_COLOR)
        # render scene
        self.game_scene_renderer.render()

    def render_game(self):
        self.render()
        self.camera.update()
        self.light.update()

    def render_menu(self):
        # red=0.0, green=0.0, blue=0.0, alpha=0.0, depth=1.0, viewport=None, color=None
        self.ctx.clear(0.23, 0.23, 0.23, alpha=-100.5, depth=1, viewport=None)
        self.menu_scene_renderer.render()

    def mainloop(self) -> None:
        while self.run:
            pg.display.set_caption(f"Labiryntho | FPS: {self.clock.get_fps():.2f}")
            self.delta_time = self.clock.tick()  # FPS

            match self.show:
                case ToShow.GAME:
                    self.render_game()

                case ToShow.MAIN_MENU:
                    self.render_menu()

            # swap buffers
            pg.display.flip()

            self.handle_events()
            self.get_time()

        print()


if __name__ == "__main__":
    app = GraphicsEngine()
    app.mainloop()
