from abc import ABC, abstractmethod

import glm

from ..misc import HitBox


class BaseModel(ABC):
    def __init__(self, app, vao_name, texture_id, position, size, rotation, color):
        self.app = app
        self.vao = app.mesh.vao[vao_name]
        self.program = self.vao.program
        self.texture_id = texture_id
        self.texture = app.mesh.texture[texture_id]
        self.position = glm.vec3(position)
        self.size = glm.vec3(size)
        self.rotation_deg = glm.vec3(rotation)
        self.rotation_rad = glm.vec3(*[glm.radians(rot) for rot in rotation])
        self.color = color

        self.hit_box = HitBox(position, self.size, self.rotation_rad)
        self.m_model = self.get_m_model()

        self.on_init()

    def on_init(self):
        self.program["m_proj"].write(self.app.camera.m_proj)

    def get_m_model(self):
        m_model = glm.mat4()

        m_model = glm.translate(m_model, self.position)

        m_model = glm.rotate(m_model, self.rotation_rad.x, glm.vec3(1, 0, 0))
        m_model = glm.rotate(m_model, self.rotation_rad.y, glm.vec3(0, 1, 0))
        m_model = glm.rotate(m_model, self.rotation_rad.z, glm.vec3(0, 0, 1))

        m_model = glm.scale(m_model, self.size)
        return m_model

    def update_m_model(self):
        self.m_model = self.get_m_model()

    def is_seen_by_camera(self):  # TODO: implement real culling
        if self.size != glm.vec3(1, 1, 1):  # Currently only for small objects
            return True

        center_distance = glm.length(self.position - self.app.camera.position)
        return self.app.camera.far > center_distance > self.app.camera.near

    @abstractmethod
    def update(self):
        self.texture.use()
        self.hit_box.update(self.position, self.size, self.rotation_rad)

        self.program["shift_color"].write(self.color)
        self.program["m_model"].write(self.m_model)
        self.program["m_view"].write(self.app.camera.m_view)

    def render(self):
        self.update()
        if self.is_seen_by_camera():
            self.vao.render()
