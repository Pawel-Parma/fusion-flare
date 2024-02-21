import time

# from typing import override

import numpy as np
import pygame as pg

from .base import BaseModel


class Button(BaseModel):
    last_press_time = time.time()

    def __init__(self, app, position, default_texture, hover_texture,
                 change_delay_time=0.15, sequent_press_delay_time=0.3,
                 rotation=(0, 0, 0), scale=(1, 1), is_dynamic=False, alpha=1.0):
        super().__init__(app, "plane2d", "none", position, rotation, (*scale, 0), alpha)
        self.default_texture = self.app.mesh.texture[default_texture]
        self.hover_texture = self.app.mesh.texture[hover_texture]

        self.change_delay_time = change_delay_time
        self.last_change_time = time.time()
        self.press_delay_time = sequent_press_delay_time

        self.is_dynamic = is_dynamic

        self.is_chosen = False
        self.func_on_click = lambda: None
        self.button_up = [None, False]
        self.button_down = [None, False]
        self.button_left = [None, False]
        self.button_right = [None, False]

        self.on_init()

    def on_init(self):
        # texture
        self.program["u_texture_0"] = 0
        self.set_correct_texture()
        self.texture.use(location=0)
        # mvp
        self.program["m_proj"].write(self.app.camera.m_proj)
        self.program["m_view"].write(self.app.camera.m_view)
        self.program["m_model"].write(self.m_model)

    def set_correct_texture(self):
        self.texture = self.hover_texture if self.is_chosen else self.default_texture

    def set_chosen(self, button_and_id=None):
        self.is_chosen = True

        if not (self.is_dynamic and button_and_id):
            return

        button = button_and_id[0]
        match button_and_id[1]:
            case "up":
                if not (self.button_down[0] and self.button_down[1]):
                    self.button_down[0] = button

            case "down":
                if not (self.button_up[0] and self.button_up[1]):
                    self.button_up[0] = button

            case "left":
                if not (self.button_right[0] and self.button_right[1]):
                    self.button_right[0] = button

            case "right":
                if not (self.button_left[0] and self.button_left[1]):
                    self.button_left[0] = button

    def set_not_chosen(self, current_time=None):
        self.is_chosen = False
        if current_time is not None:
            self.last_change_time = current_time

    def on_click(self, func):
        self.func_on_click = func

    def up_button(self, button):
        self.button_up = [button, True]

    def down_button(self, button):
        self.button_down = [button, True]

    def left_button(self, button):
        self.button_left = [button, True]

    def right_button(self, button):
        self.button_right = [button, True]

    def is_clicked(self):
        current_time = time.time()
        if current_time - self.last_press_time < self.press_delay_time:
            return False

        if self.is_chosen:
            keys = pg.key.get_pressed()
            if keys[self.app.key_binds.button_press[0]] or keys[self.app.key_binds.button_press[1]]:
                Button.last_press_time = current_time
                return True

        return False

    def listen_for_change(self):
        current_time = time.time()
        if current_time - self.last_change_time < self.change_delay_time:
            return

        key_binds = self.app.key_binds
        keys = pg.key.get_pressed()
        if keys[key_binds.button_up[0]] or keys[key_binds.button_up[1]]:
            if self.button_up[0]:
                self.set_not_chosen(current_time)
                self.button_up[0].set_chosen(button_and_id=(self, "up"))

        elif keys[key_binds.button_down[0]] or keys[key_binds.button_down[1]]:
            if self.button_down[0]:
                self.set_not_chosen(current_time)
                self.button_down[0].set_chosen(button_and_id=(self, "down"))

        elif keys[key_binds.button_left[0]] or keys[key_binds.button_left[1]]:
            if self.button_left[0]:
                self.set_not_chosen(current_time)
                self.button_left[0].set_chosen(button_and_id=(self, "left"))

        elif keys[key_binds.button_right[0]] or keys[key_binds.button_right[1]]:
            if self.button_right[0]:
                self.set_not_chosen(current_time)
                self.button_right[0].set_chosen(button_and_id=(self, "right"))

    # @override
    def update(self):
        super().update()
        if self.is_chosen:
            self.listen_for_change()

        else:
            self.last_change_time = time.time()

        if self.is_clicked():
            self.func_on_click()

        self.set_correct_texture()
        self.texture.use(location=0)
        self.program["m_model"].write(self.m_model)
        self.program["m_view"].write(self.app.camera.m_view)
