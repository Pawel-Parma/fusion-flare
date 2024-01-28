import abc

import numpy as np
import moderngl as mgl
import glm

from config import *
from .base import BaseShadowModel


class Cube(BaseShadowModel):
    def __init__(self, app, texture_id, position, rotation=(0, 0, 0), scale=(1, 1, 1)):
        super().__init__(app, "cube", texture_id, position, rotation, scale)
        self.on_init()

    def on_init(self):
        super().on_init()
        # texture
        self.texture = self.app.mesh.texture[self.texture_id]
        self.program["u_texture_0"] = 0
        self.texture.use(location=0)
        # mvp
        self.program["m_proj"].write(self.camera.m_proj)
        self.program["m_view"].write(self.camera.m_view)
        self.program["m_model"].write(self.m_model)
        # light
        self.program["light.position"].write(self.app.light.position)
        self.program["light.Ia"].write(self.app.light.Ia)
        self.program["light.Id"].write(self.app.light.Id)
        self.program["light.Is"].write(self.app.light.Is)

    def update_light(self):
        if self.app.light.can_change_position():
            self.program["light.position"].write(self.app.light.position)

    def update(self):
        self.texture.use(location=0)
        self.program["camPos"].write(self.camera.position)
        self.program["m_view"].write(self.camera.m_view)
        self.program["m_model"].write(self.m_model)

        self.update_light()