import pygame as pg
import moderngl as gl

from .config import *
from .camera import SpectatorPlayer, PhysicsPlayer
from .light import Light, CameraFollowingLight
from .opengl_pipeline import Mesh
from .scenes import *
from .maze import Maze
from .font import FontManager


# GAME
# TODO: add debug screen (F3)

# TODO: Make main menu
# Play
# History [ranking, score, time, number of missed tiles]
# Settings [controls, graphics, credits]
# Exit

# TODO: Make escape menu
# Resume
# Settings
# Exit

# TODO: Make end screen
# Score
# Time
# Name
# Play-through [shows correct path with green]

# Play again [shows play screen and same setting]
# Main menu

# TODO: Make database

# TODO: FINISHING TOUCHES
# Show time while playing
# More textures

# If time
# Custom music and sound
# Make coins, power-ups [compass, shows where to go, speed boost, etc.]
# Allow true 3D with stairs


class GraphicsEngine:
    def __init__(self):
        self.running: bool = True
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
        self.ctx.enable(flags=(gl.DEPTH_TEST | gl.BLEND))
        self.ctx.gc_mode = "auto"
        # get fps clock
        self.clock = pg.time.Clock()
        self.time = 0
        self.delta_time = 0
        # maze
        self.maze = Maze()
        # light
        self.light = CameraFollowingLight(self, Light(position=(0, 0, 0), specular=0))
        # fonts
        self.font_manager = FontManager(self)
        # players
        self.physics_player = PhysicsPlayer(self, position=(0, 0, 0))
        self.spectator_player = SpectatorPlayer(self)
        self.current_camera = CameraType.PHYSICS
        self.camera = self.physics_player
        self.always_update_camera = False
        # mesh
        self.mesh = Mesh(self)
        # scenes
        self.maze_renderer = Renderer(self, MazeScene(self))
        self.main_menu_renderer = Renderer(self, MainMenuScene(self))
        self.esc_menu_renderer = Renderer(self, EscMenuScene(self))
        self.end_game_menu_renderer = Renderer(self, EndGameMenuScene(self))
        self.settings_menu_renderer = Renderer(self, SettingsMenuScene(self))
        self.history_menu_renderer = Renderer(self, HistoryMenuScene(self))
        self.game_scene = GameScene.MAIN_MENU
        self.renderer = self.main_menu_renderer
        self.renderer.scene.use()
        #
        self.settings_menu_came_from = GameScene.MAIN_MENU

    def get_time(self):
        self.time = pg.time.get_ticks() * 0.001

    def set_renderer(self, scene_renderer):
        self.renderer.scene.un_use()
        self.renderer = scene_renderer
        self.renderer.scene.use()

    def play(self, new_maze=False):
        self.game_scene = GameScene.GAME
        self.set_renderer(self.maze_renderer)
        if new_maze:
            self.maze.new(MAZE_WIDTH, MAZE_LENGHT)
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

    def quit(self):
        pg.quit()
        self.running = False

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
                match self.game_scene:
                    case GameScene.GAME:
                        self.esc_menu()

                    case GameScene.ESC_MENU:
                        self.play()

            # CHEAT CODES
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

        if self.always_update_camera:
            self.camera.update()

        self.light.update()
        # swap buffers
        pg.display.flip()

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
        self.ctx.clear(*MENU_COLOR, alpha=0.5)
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

    def tick(self):
        log(f"FPS: {self.clock.get_fps():.2f}")
        self.delta_time = self.clock.tick()  # FPS
        self.render()
        self.handle_events()
        self.get_time()

    def mainloop(self):
        log("App start", level=LogLevel.INFO)
        try:
            while self.running:
                self.tick()

        except Exception as e:
            log(f"Occurred while ticking ({e})", level=LogLevel.ERROR)

        log("App quit\n", level=LogLevel.INFO)


if __name__ == "__main__":
    app = GraphicsEngine()
    app.mainloop()
