from .base import BaseModel


class Button(BaseModel):
    def __init__(self, app, texture_id, position, rotation=(0, 0, 0), scale=(1, 1, 1)):
        super().__init__(app, "button", texture_id, position, rotation, scale)
        self.on_init()

    def on_init(self):
        ...

    def is_clicked(self):
        ...

    def on_click(self, func):
        ...

    def update(self):
        ...

    def render(self):
        ...
