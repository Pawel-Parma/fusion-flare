from typing import override

from src.dimensions import Dimension

from ...config import *

from .scenes import *


class DefaultDimension(Dimension):
    @override
    def create_scenes(self):
        add = self.add_scene
        app = self.app

        add(DefaultScene(app, DefaultScenes.DEFAULT, self))

        self.scene_to_render = DefaultScenes.DEFAULT

    @override
    def update(self):
        self.app.ctx.clear(*SKY_COLOR)
        self.app.camera.update()
