import numpy as np

from .cube import CubeVBO
from .button import Plane2dVBO


class VBO:
    def __init__(self, ctx):
        self.vbos = {"cube": CubeVBO(ctx),
                     "plane2d": Plane2dVBO(ctx)}

    def __getitem__(self, name):
        if name not in self.vbos:
            raise KeyError(f"VBO {name} not found")

        return self.vbos[name]
