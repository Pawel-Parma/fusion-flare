class SceneRenderer:  # TODO: look at it and change to better
    def __init__(self, app):
        self.app = app
        self.ctx = app.ctx
        self.camera = app.camera
        self.camera_following_light = app.camera_following_light
        self.mesh = app.mesh
        self.scene = app.scene
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
        self.camera.update()
        self.camera_following_light.update()
        self.scene.update()
        self.render_shadow()
        self.main_render()
