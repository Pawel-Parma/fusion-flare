import sys
# =================================
import pygame as pg
import moderngl as gl
# =================================
from src.common import *


class App:
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
        pg.display.set_mode(size=(WIDTH, HEIGHT), flags=(pg.DOUBLEBUF | pg.OPENGL))
        pg.display.set_caption("Labiryntho")
        self.context = gl.create_context()

        # get fps clock
        self.clock = pg.time.Clock()

    def handle_events(self) -> None:
        for event in pg.event.get():
            if event.type == pg.QUIT:
                self.run = False

    def mainloop(self) -> None:
        while self.run:
            self.handle_events()

            pg.display.flip()
            self.clock.tick(FPS)

        pg.quit()


def main() -> None:
    app = App()
    app.mainloop()


if __name__ == "__main__":
    main()
