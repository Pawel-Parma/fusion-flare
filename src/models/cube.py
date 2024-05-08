from typing import override

from ..misc import Color

from .base import BaseModel


class Cube(BaseModel):
    def __init__(self, app, texture_id, position, size=(1, 1, 1), rotation=(0, 0, 0), color=Color()):
        super().__init__(app, "cube", texture_id, position, size, rotation, color)

    @override
    def on_init(self):
        super().on_init()

        self.program["light.position"].write(self.app.light.position)
        self.program["light.ambient"].write(self.app.light.ambient)
        self.program["light.diffuse"].write(self.app.light.diffuse)
        self.program["light.specular"].write(self.app.light.specular)

    def update_light(self):
        if self.app.light.can_change_position:
            self.program["light.position"].write(self.app.light.position)

    @override
    def update(self):
        super().update()
        self.program["camPos"].write(self.app.camera.position)
        self.update_light()
