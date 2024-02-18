import abc
import struct

# from typing import override

import glm

from ..config import *


class HitBox:
    def __init__(self, position, scale, rotation):
        self.position = position
        self.scale = scale
        self.rotation = rotation

        self.vertices = self.get_vertices()
        self.surfaces = self.get_surfaces()

    def get_vertices(self):
        ...

    def get_surfaces(self):
        ...

    def update(self, position, scale, rotation):
        if (self.position, self.scale, self.rotation) == (position, scale, rotation):
            return

        self.vertices = self.get_vertices()
        self.surfaces = self.get_surfaces()


class BaseModel(abc.ABC):
    def __init__(self, app, vao_name, texture_id, position, rotation=(0, 0, 0), scale=(1, 1, 1), alpha=1.0):
        self.app = app

        self.vao = app.mesh.vao[vao_name]
        self.program = self.vao.program
        self.texture_id = texture_id
        self.position = position
        self.rotation = glm.vec3(*[glm.radians(rot) for rot in rotation])
        self.scale = glm.vec3(scale)
        self.alpha = struct.pack('f', alpha)

        self.hit_box = HitBox(position, self.scale, self.rotation)
        self.m_model = self.get_model_matrix()

    def get_model_matrix(self):
        m_model = glm.mat4()
        # translate
        m_model = glm.translate(m_model, self.position)
        # rotate
        m_model = glm.rotate(m_model, self.rotation.x, glm.vec3(1, 0, 0))
        m_model = glm.rotate(m_model, self.rotation.y, glm.vec3(0, 1, 0))
        m_model = glm.rotate(m_model, self.rotation.z, glm.vec3(0, 0, 1))
        # scale
        m_model = glm.scale(m_model, self.scale)
        return m_model

    def render(self):
        self.update()
        self.vao.render()

    def is_seen_by_camera(self):  # TODO: implement real culling
        return True

    @abc.abstractmethod
    def update(self):
        self.hit_box.update(self.position, self.scale, self.rotation)
        self.program["alpha"].write(self.alpha)

    @property
    def is_shadowy(self):
        return False


class BaseShadowModel(BaseModel, abc.ABC):
    def __init__(self, app, vao_name, texture_id, position, rotation=(0, 0, 0), scale=(1, 1, 1), alpha=1.0):
        super().__init__(app, vao_name, texture_id, position, rotation, scale, alpha)
        self.on_init()

    def on_init(self):
        # resolution
        self.program["u_resolution"].write(glm.vec2(WINDOW_SIZE))
        # depth texture
        self.depth_texture = self.app.mesh.texture["depth_texture"]
        self.program["shadowMap"] = 1
        self.depth_texture.use(location=1)
        # shadow
        self.shadow_vao = self.app.mesh.vao["shadow_cube"]
        self.shadow_program = self.shadow_vao.program
        self.shadow_program["m_proj"].write(self.app.camera.m_proj)
        self.shadow_program["m_view_light"].write(self.app.light.m_view_light)
        self.shadow_program["m_model"].write(self.m_model)
        # light (shadow)
        self.program["m_view_light"].write(self.app.light.m_view_light)

    def update_shadow(self):
        self.shadow_program["m_model"].write(self.m_model)
        if self.app.light.can_change_position:
            self.shadow_program["m_proj"].write(self.app.camera.m_proj)
            self.shadow_program["m_view_light"].write(self.app.light.m_view_light)

    def render_shadow(self):
        self.update_shadow()
        self.shadow_vao.render()

    @property
    # @override
    def is_shadowy(self):
        return True
