import glm

from ..i_dont_know_how_to_call_that_package import Color

from .base import BaseModel


class Char(BaseModel):
    def __init__(self, app, font, quality, char, position, size=(1, 1), rotation=(0, 0, 0), color=Color()):
        super().__init__(app, "plane2d", "none", position, (*size, 0), rotation, color)

        self.font_name = font
        self.quality = quality
        self.font = app.font_manager[(font, quality)]
        self.char = char
        self.texture = self.font[self.char]

        self.char_size = glm.vec3(*self.texture.size, 0)
        self.size *= glm.vec3(*self.char_size) / 100
        self.update_m_model()

    def update(self):
        super().update()
