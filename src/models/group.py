from typing import override
from abc import ABC, abstractmethod
from sys import stderr

import glm

from ..misc import Color
from .base import BaseModel


class GroupModel(BaseModel, ABC):
    def __init__(self, app, position, size=(1, 1, 1), rotation=(0, 0, 0), color=Color()):  # noqa
        print("This implementation is experimental, "
              "'add_child' and 'update_child_attrs' methods are not fully implemented.", file=stderr)
        self.children: list[BaseModel] = []

        self.app = app
        self.vao = None
        self.program = None
        self.texture_id = None
        self.texture = None
        self.position = glm.vec3(position)
        self.size = glm.vec3(size)
        self.rotation_deg = glm.vec3(rotation)
        self.rotation_rad = glm.vec3(*[glm.radians(rot) for rot in rotation])
        self.color = color

        self.hit_box = None
        self.m_model = None

        self.create_children()

    @override
    def on_init(self):
        pass

    def add_child(self, child: BaseModel) -> BaseModel:
        # TODO: check if correct
        child.position *= self.size / child.size
        child.position += self.position

        rotation_matrix_x = glm.rotate(glm.mat4(1.0), self.rotation_rad.x, glm.vec3(1, 0, 0))
        rotation_matrix_y = glm.rotate(glm.mat4(1.0), self.rotation_rad.y, glm.vec3(0, 1, 0))
        rotation_matrix_z = glm.rotate(glm.mat4(1.0), self.rotation_rad.z, glm.vec3(0, 0, 1))
        rotation_matrix = rotation_matrix_x * rotation_matrix_y * rotation_matrix_z
        child.position = glm.vec3(rotation_matrix * glm.vec4(child.position, 1.0))
        child.rotation_deg += self.rotation_deg
        child.rotation_rad += self.rotation_rad

        child.size *= self.size
        child.color *= self.color
        # til here

        child.update_m_model()

        self.children.append(child)
        return child

    @abstractmethod
    def create_children(self):
        pass

    def update_child_attrs(self, child: BaseModel):  # TODO: make
        pass

    def update_children_attrs(self):
        for child in self.children:
            self.update_child_attrs(child)

    def update_children_m_model(self):
        for child in self.children:
            child.update_m_model()

    def update_children_attrs_and_m_model(self):
        for child in self.children:
            self.update_child_attrs(child)
            child.update_m_model()

    @override
    def get_m_model(self):
        raise NotImplementedError

    @override
    def update_m_model(self):
        raise NotImplementedError

    @override
    def is_seen_by_camera(self):
        raise NotImplementedError

    @override
    def update(self):
        pass

    @override
    def render(self):
        self.update()
        for child in self.children:
            child.update()
            child.render()
