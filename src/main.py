import pygame as pg
import moderngl as gl

from config import *
from camera import SpectatorPlayer
from light import Light, CameraFollowingLight
from opengl_pipeline import Mesh
from scene import Scene
from scene_renderer import SceneRenderer
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

# IF TIME
# TODO: Make coin power-ups [has compass, shows where to go, speed boost, etc.]
# TODO: Custom music and sound
# TODO: Add shop
# TODO: Custom textures [for player to load]
# TODO: Allow 3D with stairs [another hard one]
# TODO: enemies)
# TODO: Make custom map generator [might be hard]


class GraphicsEngine:
    # TODO: clean up the project structure
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
        # TODO: Add icon
        # TODO: ask before quiting game
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
        # scene
        self.scene = Scene(self)
        # scene renderer
        self.scene_renderer = SceneRenderer(self)

    def get_time(self) -> float:
        self.time = pg.time.get_ticks() * 0.001
        return self.time

    def handle_events(self) -> None:
        for event in pg.event.get():
            if event.type == pg.QUIT:
                pg.quit()
                self.run = False

    def render(self):
        # background color
        self.ctx.clear(*BUFFER_COLOR)
        # render scene
        self.scene_renderer.render()
        # swap buffers
        pg.display.flip()

    def render_game(self):
        self.render()
        self.camera.update()
        self.light.update()

    def render_menu(self):
        ...

    def mainloop(self) -> None:
        while self.run:
            pg.display.set_caption(f"Labiryntho | FPS: {self.clock.get_fps():.2f}")
            self.delta_time = self.clock.tick()  # FPS

            match self.show:
                case ToShow.GAME:
                    self.render_game()

                case ToShow.MENU:
                    self.render_menu()

            self.handle_events()
            self.get_time()

        print()


if __name__ == "__main__":
    app = GraphicsEngine()
    app.mainloop()
