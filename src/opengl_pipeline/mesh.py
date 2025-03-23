from .vao import VAO
from .texture import Texture


class Mesh:
    def __init__(self, app):
        self.app = app
        self.vao = VAO(app)
        self.texture = Texture(app)
