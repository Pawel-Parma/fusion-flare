class Renderer:
    def __init__(self, app, scene):
        self.app = app
        self.ctx = app.ctx
        self.mesh = app.mesh
        self.scene = scene

        self.depth_texture = self.mesh.texture['depth_texture']
        self.depth_fbo = self.ctx.framebuffer(depth_attachment=self.depth_texture)

    def shadow_render(self):
        self.depth_fbo.clear()
        self.depth_fbo.use()
        for obj in self.scene.shadow_objects:
            if obj.is_seen_by_camera():
                obj.render_shadow()

    def main_render(self):
        self.ctx.screen.use()
        for obj in (self.scene.no_shadow_objects + self.scene.shadow_objects):
            if obj.is_seen_by_camera():
                obj.render()

    def render(self):
        self.scene.update()
        if not self.app.disable_shadow_render:
            self.shadow_render()

        self.main_render()
