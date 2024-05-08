from abc import ABC
from typing import TypeVar, override

from .sceneable import Sceneable

T = TypeVar('T')


class Dimension(Sceneable, ABC):
    def __init__(self, app, name, parent):
        self.children: dict[T, Sceneable] = {}
        self.children_to_render: dict[T, Sceneable] = {}
        super().__init__(app, name, parent)

    @override
    def add_child(self, scene: Sceneable):
        self.children[scene.name] = scene
        return scene

    def add_child_to_render(self, scene_name: T):
        self.children_to_render[scene_name] = self.children[scene_name]

    def clear(self):
        self.children_to_render.clear()

    def handle_event(self, event):
        pass

    @override
    def update(self):
        pass

    @override
    def render(self):
        self.update()
        for scene in self.children_to_render.values():
            scene.render()
