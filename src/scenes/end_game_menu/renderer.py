from config import *


class EndGameMenuSceneRenderer:
    def __init__(self, app):
        self.app = app
        self.ctx = app.ctx
        self.mesh = app.mesh
        self.scene = app.end_game_menu_scene

    def main_render(self):
        for obj in self.scene.no_shadow_objects:
            obj.render()

    def render(self):
        self.main_render()
