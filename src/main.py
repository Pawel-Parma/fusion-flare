import sys

import pygame as pg
import moderngl as gl

from model import *
from camera import Camera
from light import *
from mesh import Mesh
from scene import Scene
from scene_renderer import SceneRenderer

from common import *


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
        # light
        self.light = PhongLight(position=(0, 0, 0))
        # camera
        self.camera = Camera(self, position=(0, 0, 3))
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
        self.ctx.clear(0.08, 0.16, 0.18)
        # render scene
        self.scene_renderer.render()
        # swap buffers
        pg.display.flip()

    def mainloop(self) -> None:
        print("Started mainloop\n")

        while self.run:
            print(f"\rFPS: {self.clock.get_fps():.2f}", end="")
            self.delta_time = self.clock.tick(FPS)

            self.render()
            self.handle_events()

            self.get_time()

        print()


if __name__ == "__main__":
    app = GraphicsEngine()
    app.mainloop()
