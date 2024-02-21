# from typing import override

import glm

from ..config import *

from .base import BaseModel
from .char import Char


class Text(BaseModel):  # TODO: add color, make text rotation, not char rotation
    def __init__(self, app, text, font, position, rotation=(0, 0, 0), scale=(1, 1), alpha=1.0, qualtiy=(96, 96)):
        self.real_position = glm.vec3(*position)
        pos = glm.vec3(*position)
        pos.x -= (self.get_text_len(text) - 1) * scale[0]
        super().__init__(app, "plane2d", "none", pos, rotation, (*scale, 0), alpha)
        self.rotation_in_deg = glm.vec3(rotation)
        self.alpha_in_float = alpha

        self.text = text
        self.font = font
        self.quality = qualtiy
        self.chars = self.get_chars()

    def get_chars(self):
        tmp = []
        special_char = []
        special_char_started = False
        for char in self.text:
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

            pos = self.position + 2 * self.scale * glm.vec3(len(tmp), 0, 0)
            tmp.append(Char(self.app, char, self.font, self.quality, pos,  self.rotation_in_deg, self.scale,
                            self.alpha_in_float))

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
        self.position = self.real_position.xyz
        self.position.x -= (self.get_text_len(text) - 1) * self.scale[0]
        self.text = text
        self.chars = self.get_chars()

    # @override
    def render(self):
        for char in self.chars:
            char.render()

    # @override
    def update(self):
        pass
