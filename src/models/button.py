import numpy as np
import pygame as pg

from .base import BaseModel


class Button(BaseModel):
    def __init__(self, app, position, color, hover_color, rotation=(0, 0, 0), scale=(1, 1, 1)):
        super().__init__(app, "button", "none", position, rotation, scale)
        self.color = np.array(np.array(color) / 255, dtype="f4")
        self.hover_color = np.array(np.array(hover_color) / 255, dtype="f4")
        self.func_on_click = lambda: None
        self.button_up: Button | None = None
        self.button_down: Button | None = None
        self.button_left: Button | None = None
        self.button_right: Button | None = None
        self.is_chosen = False
        self.on_init()

    def on_init(self):
        self.program["m_proj"].write(self.app.camera.m_proj)
        self.program["color"].write(self.hover_color if self.is_chosen else self.color)

    def up_button(self, button):
        self.button_up = button

    def down_button(self, button):
        self.button_down = button

    def left_button(self, button):
        self.button_left = button

    def right_button(self, button):
        self.button_right = button

    def is_clicked(self):
        if self.is_chosen:
            keys = pg.key.get_pressed()
            if keys[pg.K_RETURN] or keys[pg.K_SPACE]:
                return True

        return False

    def set_chosen(self):
        self.is_chosen = True
        self.program["color"].write(self.hover_color)

    def set_not_chosen(self):
        self.is_chosen = False
        self.program["color"].write(self.color)

    def listen_for_change(self):
        keys = pg.key.get_pressed()
        if keys[pg.K_w]:
            if self.button_up:
                self.set_not_chosen()
                self.button_up.set_chosen()

        elif keys[pg.K_s]:
            if self.button_down:
                self.set_not_chosen()
                self.button_down.set_chosen()

        elif keys[pg.K_a]:
            if self.button_left:
                self.set_not_chosen()
                self.button_left.set_chosen()

        elif keys[pg.K_d]:
            if self.button_right:
                self.set_not_chosen()
                self.button_right.set_chosen()

    def on_click(self, func):
        self.func_on_click = func

    def update(self):
        self.listen_for_change()
        if self.is_clicked():
            self.func_on_click()

        self.program["m_model"].write(self.m_model)
        self.program["m_view"].write(self.app.camera.m_view)
        self.program["color"].write(self.hover_color if self.is_chosen else self.color)
