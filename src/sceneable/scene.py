from abc import ABC

from .sceneable import Sceneable
from ..models import BaseModel


class BaseScene(Sceneable, ABC):
    def __init__(self, app, name, parent):
        self.children: list[BaseModel] = []
        super().__init__(app, name, parent)

    def add_child(self, child: BaseModel) -> BaseModel:
        self.children.append(child)
        return child

    def update(self):
        pass

    def render(self):
        self.update()
        for child in self.children:
            child.update()
            child.render()
