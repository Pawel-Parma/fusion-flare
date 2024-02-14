# from typing import override

import numpy as np

from .base import BaseVBO


class Plane2dVBO(BaseVBO):
    def __init__(self, ctx):
        super().__init__(ctx)
        self.format = "2f 3f"
        self.attributes = ["in_textcoord_0", "in_position"]

    # @override
    def get_vertex_data(self):
        vertices = [(-1, -1, 0), (1, -1, 0), (1, 1, 0), (-1, 1, 0)]
        indices = [(0, 1, 2), (2, 3, 0)]
        vertex_data = self.get_data(vertices, indices)

        texture_coord_vertices = [(0, 0), (1, 0), (1, 1), (0, 1)]
        texture_coord_indices = [(0, 1, 2), (2, 3, 0)]
        texture_coord_data = self.get_data(texture_coord_vertices, texture_coord_indices)

        vertex_data = np.hstack((texture_coord_data, vertex_data))
        return vertex_data
