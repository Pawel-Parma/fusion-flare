from opengl_pipeline.vaos import VAO
from opengl_pipeline.textures import Texture


class Mesh:
    def __init__(self, app):
        self.app = app
        self.vao = VAO(app.ctx)
        self.texture = Texture(app)
