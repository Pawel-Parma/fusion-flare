import sys
# =================================
import glfw
# =================================
from OpenGL.GL import *
# =================================
from src.common import *

if not glfw.init():
    LOGGER.error("Failed to initialize glfw")
    sys.exit(-1)


class App:
    def __init__(self) -> None:
        self.window = glfw.create_window(WIDTH, HEIGHT, "Labiryntho", None, None)
        if not self.window:
            glfw.terminate()
            LOGGER.error("Failed to create window")
            sys.exit(-2)

        glfw.set_window_pos(self.window, 100, 100)
        glfw.make_context_current(self.window)

    def mainloop(self) -> None:
        while not glfw.window_should_close(self.window):
            glfw.poll_events()
            glfw.swap_buffers(self.window)

        glfw.terminate()


def main() -> None:
    app = App()
    app.mainloop()


if __name__ == "__main__":
    main()
