import abc

import numpy as np
import moderngl as mgl
import glm

from common import *


class BaseModel:
    def __init__(self, app, vao_name, texture_id, position, rotation=(0, 0, 0), scale=(1, 1, 1)):
        self.app = app
        self.position = position
        self.rot = glm.vec3(*[glm.radians(rot) for rot in rotation])
        self.scale = scale
        self.m_model = self.get_model_matrix()
        self.texture_id = texture_id
        self.vao = app.mesh.vao[vao_name]
        self.program = self.vao.program
        self.camera = app.camera

    @abc.abstractmethod
    def update(self):
        pass

    def get_model_matrix(self):
        m_model = glm.mat4()
        # translate
        m_model = glm.translate(m_model, self.position)
        # rotate
        m_model = glm.rotate(m_model, self.rot.x, glm.vec3(1, 0, 0))
        m_model = glm.rotate(m_model, self.rot.y, glm.vec3(0, 1, 0))
        m_model = glm.rotate(m_model, self.rot.z, glm.vec3(0, 0, 1))
        # scale
        m_model = glm.scale(m_model, self.scale)
        return m_model

    def render(self):
        self.update()
        self.vao.render()


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
