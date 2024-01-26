from vao import VAO
from texture import Texture


class Mesh:
    def __init__(self, app):
        self.app = app
        self.vao = VAO(app.ctx)
        self.texture = Texture(app)

    def deinit(self):
        self.vao.deinit()
        self.texture.deinit()
