from typing import override

import glm

from ..config import *

from .base import BaseModel
from .char import Char


# TODO: text rendering is really bad
class Text(BaseModel):
    def __init__(self, app, font, text, position, rotation=(0, 0, 0), scale=(1, 1), color=(255, 255, 255), alpha=255,
                 qualtiy=(96, 96)):
        self.real_position = glm.vec3(*position)
        pos = glm.vec3(*position)
        pos.x -= (self.get_text_len(text) - 1) * scale[0]
        super().__init__(app, "plane2d", "none", pos, rotation, (*scale, 0), color, alpha)
        self.rotation_in_deg = glm.vec3(rotation)

        self.text = text
        self.font = font
        self.quality = qualtiy
        self.chars = self.get_chars()

    def get_chars(self):
        tmp = []
        special_char = []
        special_char_started = False
        prev_char = ""
        prev_scale = glm.vec3(0, 0, 0)
        for i, char in enumerate(self.text):
            if char == "`":
                special_char.append(char)
                if special_char_started:
                    special_char_started = False
                    char = FONT_BINDS["".join(special_char)]
                    special_char.clear()

                else:
                    special_char_started = True
                    continue

            elif special_char_started:
                special_char += char
                continue

            pos = self.position
            pos.x += self.scale.x * 1.5
            if {"W", "M"} & {prev_char.upper(), char.upper()} or char.upper() == char:
                pos.x += prev_scale.x

            if {"I", "L"} & {char.upper(), prev_char.upper()}:
                pos.x -= prev_scale.x / 2 - 0.1

            char = Char(self.app, self.font, char, self.quality, pos, self.rotation_in_deg, self.scale)
            char.color = self.color
            prev_char = char.char
            prev_scale = char.scale
            tmp.append(char)

        return tmp

    @staticmethod
    def get_text_len(text):
        len_text = 0
        special_char_started = False
        for char in text:
            if char == "`":
                if special_char_started:
                    special_char_started = False
                    len_text += 1

                else:
                    special_char_started = True

            elif not special_char_started:
                len_text += 1

        return len_text

    def set_text(self, text):
        self.new_position()
        self.text = text
        self.chars = self.get_chars()

    def new_position(self):
        self.position = self.real_position.xyz
        self.position.x -= (self.get_text_len(self.text) - 1) * self.scale[0]

    def set_position(self, position):
        self.real_position = glm.vec3(*position)
        self.new_position()
        for char in self.chars:
            char.position = self.position
            char.m_model = char.get_model_matrix()

    @override
    def render(self):
        for char in self.chars:
            char.render()

    @override
    def update(self):
        pass
