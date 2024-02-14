# from typing import override

from .base import BaseVBO


class ButtonVBO(BaseVBO):
    def __init__(self, ctx):
        super().__init__(ctx)
        self.format = "3f"
        self.attributes = ["in_position"]

    # @override
    def get_vertex_data(self):
        vertices = [(-1, -1, 0), (1, -1, 0), (1, 1, 0), (-1, 1, 0)]
        indices = [(0, 1, 2), (2, 3, 0)]
        vertex_data = self.get_data(vertices, indices)

        return vertex_data
