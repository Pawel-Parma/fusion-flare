from config import *


class MenuSceneRenderer:
    def __init__(self, app):
        self.app = app
        self.ctx = app.ctx
        self.mesh = app.mesh
        self.scene = app.menu_scene

    def main_render(self):
        for obj in self.scene.no_shadow_objects:
            obj.render()

    def render(self):
        self.scene.update()
        self.main_render()
