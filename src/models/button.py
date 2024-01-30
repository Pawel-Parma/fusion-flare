import numpy as np
import pygame as pg

from .base import BaseModel


class Button(BaseModel):
    def __init__(self, app, position, color, hover_color, rotation=(0, 0, 0), scale=(1, 1, 1)):
        super().__init__(app, "button", "none", position, rotation, scale)
        self.color = np.array(np.array(color) / 255, dtype="f4")
        self.hover_color = np.array(np.array(hover_color) / 255, dtype="f4")
        self.func_on_click = lambda: None
        self.on_init()

    def on_init(self):
        self.program["m_proj"].write(self.app.camera.m_proj)
        self.program["color"].write(self.color)

    def change_to_hover_color(self):
        self.program["color"].write(self.hover_color)

    def change_to_normal_color(self):
        self.program["color"].write(self.color)

    def is_chosen(self):
        return False

    @staticmethod
    def is_clicked():
        keys = pg.key.get_pressed()
        if keys[pg.K_ENTER] or keys[pg.K_RETURN] or keys[pg.K_SPACE]:
            return True

        return False

    def on_click(self, func):
        self.func_on_click = func

    def update(self):
        if self.is_chosen():
            self.change_to_hover_color()
            if self.is_clicked():
                self.func_on_click()

        else:
            self.change_to_normal_color()

    def render(self):
        self.program["m_model"].write(self.m_model)
        self.program["m_view"].write(self.app.camera.m_view)
        super().render()
        self.update()
