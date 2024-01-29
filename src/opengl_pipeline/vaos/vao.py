from opengl_pipeline.vbos import VBO
from opengl_pipeline.shader_programs import ShaderProgram


class VAO:
    def __init__(self, ctx):
        self.ctx = ctx
        self.vbo = VBO(ctx)
        self.program = ShaderProgram(ctx)
        self.vaos = {"cube": self.get_vao(program=self.program["default"], vbo=self.vbo["cube"]),
                     "shadow_cube": self.get_vao(program=self.program["shadow_map"], vbo=self.vbo["cube"]),
                     "button": self.get_vao(program=self.program["button"], vbo=self.vbo["button"])}

    def get_vao(self, program, vbo):
        vao = self.ctx.vertex_array(program, [(vbo.vbo, vbo.format, *vbo.attributes)], skip_errors=True)
        return vao

    def __getitem__(self, item):
        if item not in self.vaos:
            raise KeyError(f"VAO {item} not found")

        return self.vaos[item]