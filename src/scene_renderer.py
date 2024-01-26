class SceneRenderer:  # TODO: look at it and change to better
    def __init__(self, app):
        self.app = app
        self.ctx = app.ctx
        self.camera = app.camera
        self.mesh = app.mesh
        self.scene = app.scene
        # depth buffer
        # self.depth_texture = self.mesh.texture.textures['depth_texture']
        # self.depth_fbo = self.ctx.framebuffer(depth_attachment=self.depth_texture)

    def deinit(self):
        ...

    def main_render(self):
        self.app.ctx.screen.use()
        for obj in self.scene.objects:
            obj.render()

    def render(self):
        self.camera.update()
        self.scene.update()
        self.main_render()
