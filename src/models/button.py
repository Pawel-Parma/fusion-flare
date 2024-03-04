import time

from typing import override

import pygame as pg

from ..misc import Color

from .base import BaseModel


class NighbourButton:
    def __init__(self, button, is_set):
        self.button = button
        self.is_set = is_set


class Button(BaseModel):
    last_press_time = time.time()

    # TODO: add text to button
    def __init__(self, app, default_texture, hover_texture, position, size=(1, 1), rotation=(0, 0, 0),
                 default_color=Color(), hover_color=Color(), change_delay_time=0.15, sequent_press_delay_time=0.3,
                 is_dynamic=False):
        super().__init__(app, "plane2d", "none", position, (*size, 0), rotation, Color())

        self.default_texture = self.app.mesh.texture[default_texture]
        self.default_color = default_color
        self.hover_texture = self.app.mesh.texture[hover_texture]
        self.hover_color = hover_color

        self.change_delay_time = change_delay_time
        self.last_change_time = time.time()
        self.press_delay_time = sequent_press_delay_time

        self.is_dynamic = is_dynamic

        self.is_chosen = False
        self.func_on_click = lambda: None

        self._up_button = NighbourButton(None, False)
        self._down_button = NighbourButton(None, False)
        self._left_button = NighbourButton(None, False)
        self._right_button = NighbourButton(None, False)
        self.buttons = {"up": self._up_button,
                        "down": self._down_button,
                        "left": self._left_button,
                        "right": self._right_button}

    def set_correct_texture_and_color(self):
        self.texture = self.hover_texture if self.is_chosen else self.default_texture
        self.color = self.hover_color if self.is_chosen else self.default_color

    def set_chosen(self, button_and_id=None):
        self.is_chosen = True

        if not (self.is_dynamic and button_and_id):
            return

        button = button_and_id[0]
        nighbour_button = self.buttons[button_and_id[1]]
        if not (nighbour_button.button and nighbour_button.is_set):
            nighbour_button.button = button

    def set_not_chosen(self, current_time=None):
        self.is_chosen = False
        if current_time is not None:
            self.last_change_time = current_time

    def on_click(self, func):
        self.func_on_click = func

    @staticmethod
    def set_button(which, to):
        which.button = to
        which.is_set = True

    def up_button(self, button):
        self.set_button(self._up_button, button)

    def down_button(self, button):
        self.set_button(self._down_button, button)

    def left_button(self, button):
        self.set_button(self._left_button, button)

    def right_button(self, button):
        self.set_button(self._right_button, button)

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
            if button := self._up_button.button:
                self.set_not_chosen(current_time)
                button.set_chosen(button_and_id=(self, "down"))

        elif keys[key_binds.button_down[0]] or keys[key_binds.button_down[1]]:
            if button := self._down_button.button:
                self.set_not_chosen(current_time)
                button.set_chosen(button_and_id=(self, "up"))

        elif keys[key_binds.button_left[0]] or keys[key_binds.button_left[1]]:
            if button := self._left_button.button:
                self.set_not_chosen(current_time)
                button.set_chosen(button_and_id=(self, "right"))

        elif keys[key_binds.button_right[0]] or keys[key_binds.button_right[1]]:
            if button := self._right_button.button:
                self.set_not_chosen(current_time)
                button.set_chosen(button_and_id=(self, "left"))

    @override
    def update(self):
        super().update()
        self.set_correct_texture_and_color()
        if self.is_chosen:
            self.listen_for_change()

        else:
            self.last_change_time = time.time()

        if self.is_clicked():
            self.func_on_click()
