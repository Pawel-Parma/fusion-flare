from typing import override

import glm

from ..config import *

from ..misc import Color

from .base import BaseModel
from .char import Char


# TODO: text rendering is really bad
class Text(BaseModel):
    def __init__(self, app, font, text, position, rotation=(0, 0, 0), size=(1, 1), color=Color(), qualtiy=(96, 96)):
        self.real_position = glm.vec3(*position)
        pos = glm.vec3(*position)
        pos.x -= (self.get_text_len(text) - 1) * size[0]
        super().__init__(app, "plane2d", "none", pos, (*size, 0), rotation, color)

        self._text = text
        self.font = font
        self.quality = qualtiy
        self.chars = self.get_chars()

    def get_chars(self):
        tmp = []
        special_char = []
        special_char_started = False
        prev_char = ""
        prev_size = glm.vec3(0, 0, 0)
        for i, char in enumerate(self._text):
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
            pos.x += self.size.x * 1.5
            if {"W", "M"} & {prev_char.upper(), char.upper()} or char.upper() == char:
                pos.x += prev_size.x

            if {"I", "L"} & {char.upper(), prev_char.upper()}:
                pos.x -= prev_size.x / 2 - 0.1

            char = Char(self.app, self.font, self.quality, char, pos, self.size, self.rotation_deg)
            char.color = self.color
            prev_char = char.char
            prev_size = char.size
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

    @property
    def text(self):
        return self._text

    @text.setter
    def text(self, text):
        self.new_position()
        self._text = text
        self.chars = self.get_chars()

    def new_position(self):
        self.position = self.real_position.xyz
        self.position.x -= (self.get_text_len(self._text) - 1) * self.size[0]

    def set_position(self, position):
        self.real_position = glm.vec3(*position)
        self.new_position()
        for char in self.chars:
            char.position = self.position
            char.update_m_model()

    @override
    def render(self):
        for char in self.chars:
            char.render()

    @override
    def update(self):
        pass
