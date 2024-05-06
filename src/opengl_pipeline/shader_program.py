import os

from ..config import *


class ShaderProgram:
    def __init__(self, app):
        self.app = app
        self.ctx = app.ctx
        self.programs_list = set(os.listdir(SHADERS_DIR))
        self.programs = {"default": self.get_program("default"),
                         "plane2d": self.get_program("plane2d")}

    def get_program(self, name):
        program_name = f"{SHADERS_DIR}/{name}/{name}"
        with open(f"{program_name}.vert", "r") as file:
            vertex_shader = file.read()

        with open(f"{program_name}.frag", "r") as file:
            fragment_shader = file.read()

        program = self.ctx.program(vertex_shader=vertex_shader, fragment_shader=fragment_shader)
        return program

    def __getitem__(self, name):
        if name not in self.programs_list:
            raise KeyError(f"Program ({name}) not found")

        if name not in self.programs:
            self.programs[name] = self.get_program(name)
            self.programs_list.add(name)

        return self.programs[name]
