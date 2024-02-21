from .base import BaseModel


class Char(BaseModel):
    def __init__(self, app, char, font, quality, position, rotation=(0, 0, 0), scale=(1, 1), alpha=1.0):
        super().__init__(app, "plane2d", "none", position, rotation, (*scale, 0), alpha)
        self.char = char
        self.font_name = font
        self.quality = quality
        self.font = app.font_manager[(font, quality)]

        self.on_init()

    def on_init(self):
        # texture
        self.texture = self.font[self.char]
        self.program["u_texture_0"] = 0
        self.texture.use(location=0)
        # mvp
        self.program["m_model"].write(self.m_model)
        # alpha
        self.program["alpha"].write(self.alpha)

    def update(self):
        super().update()
        self.texture.use(location=0)
        self.program["m_model"].write(self.m_model)
