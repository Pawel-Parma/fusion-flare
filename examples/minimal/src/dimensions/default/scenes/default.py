from typing import override

from src.models import *
from src.scenes import BaseScene
from src.misc import Color


class DefaultScene(BaseScene):
    @override
    def create_objects(self):
        add = self.add_object
        app = self.app

        add(Cube(app, "test", (0, 0, -4)))
        add(Cube(app, "black", (0, 0, -2)))
        add(Cube(app, "white", (0, 0, 4), color=Color(255, 0, 0)))
        add(Cube(app, "white", (0, 0, 2)))
        add(Cube(app, "white", (0, 0, 0), color=Color(0, 255, 0, 0.5)))