from typing import override

from ..misc import Color

from .base import BaseModel


class Plane2d(BaseModel):
    def __init__(self, app, texture_id, position, size=(1, 1), rotation=(0, 0, 0), color=Color()):
        super().__init__(app, "plane2d", texture_id, position, (*size, 0), rotation, color)

    @override
    def update(self):
        super().update()
