import os
import os.path as op

from config import *


class ShaderProgram:
    def __init__(self, ctx):
        self.ctx = ctx
        self.programs_list = {shader for shader in os.listdir(SHADERS_DIR) if op.isdir(op.join(SHADERS_DIR, shader))}
        self.programs = {"default": self.get_program("default"),
                         "shadow_map": self.get_program("shadow_map"),
                         "button": self.get_program("button")}

    def get_program(self, name):
        with open(op.join(SHADERS_DIR, f"{name}/{name}.vert"), "r") as file:
            vertex_shader = file.read()

        with open(op.join(SHADERS_DIR, f"{name}/{name}.frag"), "r") as file:
            fragment_shader = file.read()

        program = self.ctx.program(vertex_shader=vertex_shader, fragment_shader=fragment_shader)
        return program

    def __getitem__(self, name):
        if name not in self.programs_list:
            raise KeyError(f"Program {name} not found")

        if name not in self.programs:
            return self.get_program(name)

        return self.programs[name]
