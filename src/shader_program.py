class ShaderProgram:
    def __init__(self, ctx):
        self.ctx = ctx
        self.programs = {}
        # TODO: implement programs_list (reads available programs and checks if program exists)
        self.programs_list = {"default", }
        self.programs["default"] = self.get_program("default")

    def deinit(self):
        [program.release() for program in self.programs.values()]

    def get_program(self, name):
        with open(f"../shaders/{name}.vert", "r") as file:  # TODO: add path to constants
            vertex_shader = file.read()

        with open(f"../shaders/{name}.frag", "r") as file:  # TODO: make shaders/name/name(.frag | .vert)
            fragment_shader = file.read()

        program = self.ctx.program(vertex_shader=vertex_shader, fragment_shader=fragment_shader)
        return program

    def __getitem__(self, name):
        if name not in self.programs_list:
            raise KeyError(f"Program {name} not found")

        if name not in self.programs:
            return self.get_program(name)

        return self.programs[name]
