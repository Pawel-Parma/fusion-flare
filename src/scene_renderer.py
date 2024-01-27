class SceneRenderer:
    def __init__(self, app):
        self.app = app
        self.ctx = app.ctx
        self.camera = app.camera
        self.mesh = app.mesh
        self.scene = app.scene
        self.light = app.light
        # depth buffer
        self.depth_texture = self.mesh.texture['depth_texture']
        self.depth_fbo = self.ctx.framebuffer(depth_attachment=self.depth_texture)

    def deinit(self):
        self.depth_fbo.release()

    def render_shadow(self):
        self.depth_fbo.clear()
        self.depth_fbo.use()
        for obj in self.scene.objects:
            obj.render_shadow()

    def main_render(self):
        self.app.ctx.screen.use()
        for obj in self.scene.objects:
            obj.render()

    def render(self):
        self.light.update()
        # self.render_shadow() TODO: fix shadows
        self.camera.update()
        self.scene.update()
        self.main_render()
