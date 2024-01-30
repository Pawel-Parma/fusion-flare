from .base import BaseModel


class Button(BaseModel):
    def __init__(self, app, texture_id, position, rotation=(0, 0, 0), scale=(1, 1, 1)):
        super().__init__(app, "button", texture_id, position, rotation, scale)
        self.func_on_click = lambda: None
        self.on_init()

    def on_init(self):
        self.program["m_proj"].write(self.app.camera.m_proj)

    def change_to_hover_texture(self):
        ...

    def is_hover(self):
        return False

    def is_clicked(self):
        return False

    def on_click(self, func):
        self.func_on_click = func

    def update(self):
        if self.is_hover():
            self.change_to_hover_texture()
            if is_clicked():
                self.func_on_click()

    def render(self):
        self.program["m_model"].write(self.m_model)
        self.program["m_view"].write(self.app.camera.m_view)
        super().render()
        self.update()
