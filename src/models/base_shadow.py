import abc

from typing import override

import glm

from .base import BaseModel


class BaseShadowModel(BaseModel, abc.ABC):
    def __init__(self, app, vao_name, texture_id, position, size, rotation, color):
        self.depth_texture = app.mesh.texture["depth_texture"]
        self.shadow_vao = app.mesh.vao["shadow_cube"]
        self.shadow_program = self.shadow_vao.program
        super().__init__(app, vao_name, texture_id, position, size, rotation, color)

    @override
    def on_init(self):
        super().on_init()

        self.program["u_resolution"].write(glm.vec2(self.app.window_size))

        self.program["shadowMap"] = 1
        self.depth_texture.use(location=1)

        self.shadow_program["m_proj"].write(self.app.camera.m_proj)
        self.shadow_program["m_view_light"].write(self.app.light.m_view_light)

        self.program["m_view_light"].write(self.app.light.m_view_light)

    @property
    @override
    def is_shadowy(self):
        return True

    def shadow_update(self):
        self.shadow_program["m_model"].write(self.m_model)
        if self.app.light.can_change_position:
            self.shadow_program["m_proj"].write(self.app.camera.m_proj)
            self.shadow_program["m_view_light"].write(self.app.light.m_view_light)

    def render_shadow(self):
        self.shadow_update()
        self.shadow_vao.render()
