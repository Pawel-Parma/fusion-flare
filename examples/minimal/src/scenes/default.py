from typing import override

import glm

from src.models import *
from src.sceneable import BaseScene
from src.misc import Color

from ..config import SKY_COLOR


class Test(GroupModel):
    @override
    def create_children(self):
        self.add_child(Cube(self.app, "test", (2, 0, 0), rotation=(0, 0, 0)))
        self.add_child(Cube(self.app, "test", (-2, 0, 0)))

    def update(self):
        rads = glm.radians(0.01)

        self.children[0].rotation_rad.y += rads
        self.children[1].rotation_rad.y += rads

        self.update_children_attrs()
        self.update_children_m_model()


class DefaultScene(BaseScene):
    @override
    def create_children(self):
        add = self.add_child
        app = self.app

        add(Cube(app, "test", (0, 0, -5)))
        add(Cube(app, "black", (0, 0, -2.5)))
        add(Cube(app, "white", (0, 0, 2.5)))
        add(Cube(app, "white", (0, 0, 5), color=Color(255, 0, 0)))
        add(Cube(app, "white", (0, 0, 0), color=Color(0, 255, 0, 0.5)))

        add(Test(app, (0, 2, 0), (1, 1, 1), (0, 0, 0)))

    @override
    def update(self):
        self.app.ctx.clear(*SKY_COLOR)
        self.app.camera.update()
