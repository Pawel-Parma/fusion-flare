class Renderer:
    def __init__(self, app, scene):
        self.app = app
        self.ctx = app.ctx
        self.mesh = app.mesh
        self.scene = scene

    def render(self):
        self.scene.update()

        for obj in self.scene.objects:
            if obj.is_seen_by_camera():
                obj.render()
