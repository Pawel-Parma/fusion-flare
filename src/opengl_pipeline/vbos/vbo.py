import abc

import numpy as np


class VBO:
    def __init__(self, ctx):
        self.vbos = {"cube": CubeVBO(ctx),
                     "button": ButtonVBO(ctx)}

    def __getitem__(self, name):
        if name not in self.vbos:
            raise KeyError(f"VBO {name} not found")

        return self.vbos[name]


class BaseVBO:
    def __init__(self, ctx):
        self.ctx = ctx
        self.vbo = self.get_vbo()
        self.format: str | None = None
        self.attributes: list | None = None

    @abc.abstractmethod
    def get_vertex_data(self):
        pass

    @staticmethod
    def get_data(vertices, indices):
        data = [vertices[ind] for triangle in indices for ind in triangle]
        return np.array(data, dtype="f4")

    def get_vbo(self):
        vertex_data = self.get_vertex_data()
        vbo = self.ctx.buffer(vertex_data)
        return vbo


class CubeVBO(BaseVBO):
    def __init__(self, ctx):
        super().__init__(ctx)
        self.format = "2f 3f 3f"
        self.attributes = ["in_textcoord_0", "in_normal", "in_position"]

    def get_vertex_data(self):
        vertices = [(-1, -1, 1), (1, -1, 1), (1, 1, 1), (-1, 1, 1),
                    (-1, 1, -1), (-1, -1, -1), (1, -1, -1), (1, 1, -1)]

        indices = [(0, 2, 3), (0, 1, 2),
                   (1, 7, 2), (1, 6, 7),
                   (6, 5, 4), (4, 7, 6),
                   (3, 4, 5), (3, 5, 0),
                   (3, 7, 4), (3, 2, 7),
                   (0, 6, 1), (0, 5, 6)]
        vertex_data = self.get_data(vertices, indices)

        texture_coord_vertices = [(0, 0), (1, 0), (1, 1), (0, 1)]
        texture_coord_indices = [(0, 2, 3), (0, 1, 2),
                                 (0, 2, 3), (0, 1, 2),
                                 (0, 1, 2), (2, 3, 0),
                                 (2, 3, 0), (2, 0, 1),
                                 (0, 2, 3), (0, 1, 2),
                                 (3, 1, 2), (3, 0, 1)]
        texture_coord_data = self.get_data(texture_coord_vertices, texture_coord_indices)

        normals = [(0, 0, 1) * 6,
                   (1, 0, 0) * 6,
                   (0, 0, -1) * 6,
                   (-1, 0, 0) * 6,
                   (0, 1, 0) * 6,
                   (0, -1, 0) * 6]
        normals = np.array(normals, dtype="f4").reshape(36, 3)

        vertex_data = np.hstack((normals, vertex_data))
        vertex_data = np.hstack((texture_coord_data, vertex_data))
        return vertex_data


class ButtonVBO(BaseVBO):
    def __init__(self, ctx):
        super().__init__(ctx)
        self.format = "2f 2f"
        self.attributes = ["in_textcoord_0", "in_position"]

    def get_vertex_data(self):
        vertices = [(0, 0), (1, 0), (1, 1), (0, 1)]
        indices = [(0, 2, 3), (0, 1, 2)]
        vertex_data = self.get_data(vertices, indices)

        texture_coord_vertices = [(0, 0), (1, 0), (1, 1), (0, 1)]
        texture_coord_indices = [(0, 2, 3), (0, 1, 2)]
        texture_coord_data = self.get_data(texture_coord_vertices, texture_coord_indices)

        vertex_data = np.hstack((texture_coord_data, vertex_data))
        return vertex_data
