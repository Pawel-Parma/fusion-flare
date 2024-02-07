import time

import numpy as np
import pygame as pg

from .base import BaseModel

from config import *


class Button(BaseModel):
    def __init__(self, app, position, default_texture, hover_texture, delay_time=0.15, rotation=(0, 0, 0),
                 scale=(1, 1, 1)):
        super().__init__(app, "button", "none", position, rotation, scale)
        self.func_on_click = lambda: None
        self.button_up: Button | None = None
        self.button_down: Button | None = None
        self.button_left: Button | None = None
        self.button_right: Button | None = None
        self.is_chosen = False
        self.delay_time = delay_time
        self.default_texture = self.app.mesh.texture[default_texture]
        self.hover_texture = self.app.mesh.texture[hover_texture]
        self.last_switch_time = time.time()
        self.on_init()

    def on_init(self):
        # texture
        self.program["u_texture_0"] = 0
        self.use_correct_texture()
        self.texture.use(location=0)
        # mvp
        self.program["m_proj"].write(self.app.camera.m_proj)
        self.program["m_view"].write(self.app.camera.m_view)
        self.program["m_model"].write(self.m_model)

    def use_correct_texture(self):
        self.texture = self.hover_texture if self.is_chosen else self.default_texture

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

    def set_not_chosen(self, current_time=None):
        self.is_chosen = False
        if current_time is not None:
            self.last_switch_time = current_time

    def listen_for_change(self):
        current_time = time.time()
        if current_time - self.last_switch_time < self.delay_time:
            return

        keys = pg.key.get_pressed()
        if keys[pg.K_w]:
            if self.button_up:
                self.set_not_chosen(current_time)
                self.button_up.set_chosen()

        elif keys[pg.K_s]:
            if self.button_down:
                self.set_not_chosen(current_time)
                self.button_down.set_chosen()

        elif keys[pg.K_a]:
            if self.button_left:
                self.set_not_chosen(current_time)
                self.button_left.set_chosen()

        elif keys[pg.K_d]:
            if self.button_right:
                self.set_not_chosen(current_time)
                self.button_right.set_chosen()

    def on_click(self, func):
        self.func_on_click = func

    def update(self):
        if self.is_chosen:
            self.listen_for_change()

        else:
            self.last_switch_time = time.time()

        if self.is_clicked():
            self.func_on_click()

        self.use_correct_texture()
        self.texture.use(location=0)
        self.program["m_model"].write(self.m_model)
        self.program["m_view"].write(self.app.camera.m_view)
