from config import *

from .scene import EndGameMenu


class EndGameMenuSceneRenderer:
    def __init__(self, app):
        self.app = app
        self.scene = EndGameMenu(app)
        self.ctx = app.ctx
        self.mesh = app.mesh
        # depth buffer
        self.depth_texture = self.app.mesh.texture['depth_texture']
        self.depth_fbo = self.ctx.framebuffer(depth_attachment=self.depth_texture)

    def shadow_render(self):
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
