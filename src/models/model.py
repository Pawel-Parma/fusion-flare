import abc

import numpy as np
import moderngl as mgl
import glm

from .base import BaseModel

from common import *


class BaseShadowModel(BaseModel):
    def __init__(self, app, vao_name, texture_id, position, rotation=(0, 0, 0), scale=(1, 1, 1)):
        super().__init__(app, vao_name, texture_id, position, rotation, scale)
        self.on_init()

    def on_init(self):
        self.program["m_model"].write(self.m_model)

    def update(self):
        self.program["m_model"].write(self.m_model)

    @staticmethod
    def is_shadowy():
        return True


class ExtendedShadowModel(BaseShadowModel):
    pass


class Cube(BaseModel):
    def __init__(self, app, texture_id, position, rotation=(0, 0, 0), scale=(1, 1, 1)):
        super().__init__(app, "cube", texture_id, position, rotation, scale)
        self.on_init()

    def on_init(self):  # TODO: remove shadow from cube and add it to BaseShadowModel
        self.program["m_view_light"].write(self.app.light.m_view_light)
        # resolution
        self.program["u_resolution"].write(glm.vec2(WINDOW_SIZE))
        # depth texture
        self.depth_texture = self.app.mesh.texture["depth_texture"]
        self.program["shadowMap"] = 1
        self.depth_texture.use(location=1)
        # shadow
        self.shadow_vao = self.app.mesh.vao["shadow_cube"]
        self.shadow_program = self.shadow_vao.program
        self.shadow_program["m_proj"].write(self.camera.m_proj)
        self.shadow_program["m_view_light"].write(self.app.light.m_view_light)
        self.shadow_program["m_model"].write(self.m_model)
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
        self.program["light.Is"].write(self.app.light.Id)

    def update_shadow(self):  # TODO: update shadow program
        self.shadow_program["m_model"].write(self.m_model)

    def render_shadow(self):
        self.update_shadow()
        self.shadow_vao.render()

    def update(self):
        self.texture.use(location=0)
        self.program["camPos"].write(self.camera.position)
        self.program["m_view"].write(self.camera.m_view)
        self.program["m_model"].write(self.m_model)

        self.program["light.position"].write(self.app.light.position)
