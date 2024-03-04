from .vbos import VBO
from .shader_program import ShaderProgram


class VAO:
    def __init__(self, app):
        self.app = app
        self.ctx = app.ctx

        self.vbo = VBO(self.ctx)
        self.program = ShaderProgram(app)
        self.vaos = {"cube": self.get_vao(program=self.program["default"], vbo=self.vbo["cube"]),
                     "shadow_cube": self.get_vao(program=self.program["shadow_map"], vbo=self.vbo["cube"]),
                     "plane2d": self.get_vao(program=self.program["plane2d"], vbo=self.vbo["plane2d"])}

    def get_vao(self, program, vbo, skip_errors=True):
        vao = self.ctx.vertex_array(program, [(vbo.vbo, vbo.format, *vbo.attributes)], skip_errors=skip_errors)
        return vao

    def __getitem__(self, item):
        if item not in self.vaos:
            raise KeyError(f"VAO ({item}) not found")

        return self.vaos[item]
