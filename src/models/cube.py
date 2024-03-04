from typing import override

from ..i_dont_know_how_to_call_that_package import Color

from .base_shadow import BaseShadowModel


class Cube(BaseShadowModel):
    def __init__(self, app, texture_id, position, rotation=(0, 0, 0), size=(1, 1, 1), color=Color()):
        super().__init__(app, "cube", texture_id, position, size, rotation, color)

    @override
    def on_init(self):
        super().on_init()
        # light
        self.program["light.position"].write(self.app.light.position)
        self.program["light.Ia"].write(self.app.light.Ia)
        self.program["light.Id"].write(self.app.light.Id)
        self.program["light.Is"].write(self.app.light.Is)

    def update_light(self):
        if self.app.light.can_change_position:
            self.program["light.position"].write(self.app.light.position)

    @override
    def update(self):
        super().update()
        self.program["camPos"].write(self.app.camera.position)
        self.update_light()
