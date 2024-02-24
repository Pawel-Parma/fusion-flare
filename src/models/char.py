import glm

from .base import BaseModel


class Char(BaseModel):
    def __init__(self, app, char, font, quality, position, rotation=(0, 0, 0), scale=(1, 1), color=(255, 255, 255),
                 alpha=255):
        super().__init__(app, "plane2d", "none", position, rotation, (*scale, 0), color, alpha)
        self.char = char
        self.font_name = font
        self.quality = quality
        self.font = app.font_manager[(font, quality)]
        self.texture = self.font[self.char]
        self.size = glm.vec3(*self.texture.size, 0)
        self.scale *= glm.vec3(*self.size) / 100
        self.m_model = self.get_model_matrix()

        self.on_init()

    def on_init(self):
        # texture
        self.program["u_texture_0"] = 0

    def update(self):
        super().update()
        self.texture.use(location=0)
        self.program["m_model"].write(self.m_model)
