import pygame as pg
import moderngl as gl

from camera import SpectatorPlayer, PhysicsPlayer
from light import *
from mesh import Mesh
from scene import Scene
from scene_renderer import SceneRenderer

from maze import *
from common import *

# GAME
# TODO: Make faster by utilising chunks and not rendering everything at once
# TODO: Add icon
# TODO: ask before quiting game
# TODO: add f3 debug screen
# TODO: show time, coins and score when playing

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

# TODO: Make maze generation

# TODO: Make end screen
# Time
# Score
# Coins
# Name
# Play-through [shows correct path with green]

# Play again [shows play screen and same setting]
# Main menu

# TODO: Make database

# IF TIME
# TODO: Make coin power-ups [has compass, shows where to go, speed boost, etc.]
# TODO: Custom music and sound
# TODO: Add shop
# TODO: Custom textures [for player to load]
# TODO: Allow 3D with stairs [another hard one]
# TODO: enemies)
# TODO: Make custom map generator [might be hard]


class GraphicsEngine:  # TODO: clean up the project structure
    def __init__(self) -> None:
        self.run: bool = True
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
        self.maze = maze.generate_maze(MAZE_WIDTH, MAZE_LENGHT)
        # light
        self.light = CameraFollowingLight(self, Light(position=(0, 1, 0), specular=0))
        # player
        # self.camera = PhysicsPlayer(self)
        self.camera = SpectatorPlayer(self)
        # mesh
        self.mesh = Mesh(self)
        # scene
        self.scene = Scene(self)
        # scene renderer
        self.scene_renderer = SceneRenderer(self)

    def get_time(self) -> float:
        self.time = pg.time.get_ticks() / 1000
        return self.time

    def handle_events(self) -> None:
        for event in pg.event.get():
            if event.type == pg.QUIT:
                self.mesh.deinit()
                self.scene_renderer.deinit()
                pg.quit()
                self.run = False

    def render(self):
        # background color
        # TODO: add to consts.py and look for other to add
        self.ctx.clear(*glm.normalize(glm.vec3(90, 208, 255)))  # 0.08, 0.16, 0.18
        # render scene
        self.scene_renderer.render()
        # swap buffers
        pg.display.flip()

    def mainloop(self) -> None:
        while self.run:
            # print(f"\rFPS: {self.clock.get_fps():.2f}", end="")
            pg.display.set_caption(f"Labiryntho | FPS: {self.clock.get_fps():.2f}")
            self.delta_time = self.clock.tick()  # FPS

            self.render()
            self.handle_events()

            self.get_time()

        print()


if __name__ == "__main__":
    app = GraphicsEngine()
    app.mainloop()
