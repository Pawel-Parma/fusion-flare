import numpy as np

from .cube import CubeVBO
from .button import ButtonVBO


class VBO:
    def __init__(self, ctx):
        self.vbos = {"cube": CubeVBO(ctx),
                     "button": ButtonVBO(ctx)}

    def __getitem__(self, name):
        if name not in self.vbos:
            raise KeyError(f"VBO {name} not found")

        return self.vbos[name]
