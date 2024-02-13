from config import *

from .scene import MainMenu


class MainMenuSceneRenderer:
    def __init__(self, app):
        self.app = app
        self.ctx = app.ctx
        self.mesh = app.mesh
        self.scene = MainMenu(app)
        # depth buffer
        self.depth_texture = self.mesh.texture['depth_texture']
        self.depth_fbo = self.ctx.framebuffer(depth_attachment=self.depth_texture)

    # def create_scene(self):
    #     return MainMenu(self.app)

    def render_shadow(self):
        self.depth_fbo.clear()
        self.depth_fbo.use()
        for obj in self.scene.shadow_objects:
            obj.render_shadow()

    def main_render(self):
        self.app.ctx.screen.use()
        for obj in (self.scene.no_shadow_objects + self.scene.shadow_objects):
            obj.render()

    def render(self):
        self.main_render()
        if not DISABLE_SHADOW_RENDER:
            self.render_shadow()
