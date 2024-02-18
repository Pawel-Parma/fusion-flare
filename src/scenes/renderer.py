import abc

from ..config import *


class BaseRenderer(abc.ABC):
    def __init__(self, app):
        self.app = app
        self.ctx = app.ctx
        self.mesh = app.mesh
        # scene
        self.scene = self.create_scene()
        # depth buffer
        self.depth_texture = self.mesh.texture['depth_texture']
        self.depth_fbo = self.ctx.framebuffer(depth_attachment=self.depth_texture)

    def shadow_render(self):
        self.depth_fbo.clear()
        self.depth_fbo.use()
        for obj in self.scene.shadow_objects:
            if obj.is_seen_by_camera():
                obj.render_shadow()

    def main_render(self):
        self.app.ctx.screen.use()
        for obj in (self.scene.no_shadow_objects + self.scene.shadow_objects):
            if obj.is_seen_by_camera():
                obj.render()

    def render(self):
        self.scene.update()
        if not DISABLE_SHADOW_RENDER:
            self.shadow_render()

        self.main_render()

    @abc.abstractmethod
    def create_scene(self):
        pass
