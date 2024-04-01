from typing import override

import glm

from ..misc import Color


class Light:
    def __init__(self, position, direction=(0, 0, 0), color=Color(), ambient=0.1, diffuse=0.8, specular=1.0):
        self.position = glm.vec3(position)
        self.color = glm.vec3(color)
        self.direction = glm.vec3(direction)

        self.intensities = (ambient, diffuse, specular)
        self.ambient = ambient * self.color
        self.diffuse = diffuse * self.color
        self.specular = specular * self.color

        self.m_view_light = self.get_m_view()

    def get_m_view(self):
        return glm.lookAt(self.position, self.direction, glm.vec3(0, 1, 0))

    @property
    def can_change_position(self):
        return False

    def update(self):
        pass


class CameraFollowingLight(Light):
    def __init__(self, app, position, direction=(0, 0, 0), color=Color(), ambient=0.1, diffuse=0.8, specular=1.0):
        super().__init__(position, direction, color, ambient, diffuse, specular)
        self.app = app

    @property
    @override
    def can_change_position(self):
        return True

    @override
    def update(self):
        self.position.xyz = self.app.camera.position.xyz
