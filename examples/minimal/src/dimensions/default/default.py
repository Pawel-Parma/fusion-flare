from typing import override

from src.sceneable import Dimension

from ...config import *

from .scenes import *


class DefaultDimension(Dimension):
    @override
    def create_children(self):
        add = self.add_child
        app = self.app

        add(DefaultScene(app, DefaultScenes.DEFAULT, self))

        self.add_child_to_render(DefaultScenes.DEFAULT)

    @override
    def update(self):
        self.app.ctx.clear(*SKY_COLOR)
        self.app.camera.update()
