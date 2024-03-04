from typing import override

from ..i_dont_know_how_to_call_that_package import Color

from .base import BaseModel


class Plane2d(BaseModel):
    def __init__(self, app, texture_id, position, size=(1, 1), rotation=(0, 0, 0), color=Color()):
        super().__init__(app, "plane2d", texture_id, (*size, 0), position, rotation, color)

    @override
    def update(self):
        super().update()
