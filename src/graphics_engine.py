import traceback

import moderngl as gl
import pygame as pg

from .font import FontManager
from .opengl_pipeline import Mesh


class GraphicsEngine:
    def __init__(self, app_name: str, window_size: tuple[int, int], icon_path: str = None, grab_mouse: bool = True,
                 show_mouse: bool = False, context_flags=(gl.DEPTH_TEST | gl.BLEND), fps: int = -1):
        self.app_name = app_name
        self.window_size = window_size
        self.icon_path = icon_path
        self.grab_mouse = grab_mouse
        self.show_mouse = show_mouse
        self.context_flags = context_flags
        self.fps = fps
        # init pygame
        pg.init()
        # set OpenGL version
        pg.display.gl_set_attribute(pg.GL_CONTEXT_MAJOR_VERSION, 3)
        pg.display.gl_set_attribute(pg.GL_CONTEXT_MINOR_VERSION, 3)
        # set OpenGL profile
        pg.display.gl_set_attribute(pg.GL_CONTEXT_PROFILE_MASK, pg.GL_CONTEXT_PROFILE_CORE)
        # create OpenGL context
        pg.display.set_mode(size=window_size, flags=(pg.DOUBLEBUF | pg.OPENGL))
        # window settings
        pg.display.set_caption(app_name)
        if icon_path is not None:
            pg.display.set_icon(pg.image.load(icon_path))

        # mouse settings
        pg.event.set_grab(grab_mouse)
        pg.mouse.set_visible(show_mouse)
        # detect and use existing opengl context
        self.ctx = gl.create_context()
        self.ctx.enable(flags=context_flags)
        self.ctx.gc_mode = "auto"
        # get fps clock
        self.clock = pg.time.Clock()
        self.time = 0
        self.delta_time = 0

        # temporary (for the sake of refactoring)
        self.disable_shadow_render = True  # SHADOWS ARE EXPERIMENTAL AND WILL CAUSE ISSUES

        self.fonts_dir = "examples/labiryntho/fonts/"
        self.shaders_dir = "shaders/"
        self.textures_dir = "examples/labiryntho/textures/"
        #

        # fonts
        self.font_manager = FontManager(self)
        # mesh
        self.mesh = Mesh(self)
        # state
        self.running: bool = True

    def set_time(self):
        self.time = pg.time.get_ticks() * 0.001

    def quit(self):
        pg.quit()
        self.running = False

    def handle_events(self):
        for event in pg.event.get():
            if event.type == pg.QUIT:
                self.quit()
                break

    def render(self):
        # swap buffers
        pg.display.flip()

    def tick(self):
        self.delta_time = self.clock.tick(self.fps)
        self.render()
        self.handle_events()
        self.set_time()

    def on_tick_exception(self, e):
        traceback.print_exception(e)

    def mainloop(self):
        try:
            while self.running:
                self.tick()

        except Exception as e:
            self.on_tick_exception(e)
