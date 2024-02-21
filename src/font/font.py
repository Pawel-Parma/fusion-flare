import string

from io import BytesIO

import freetype as ft
import numpy as np
import pygame as pg
import moderngl as gl
import glm

from ..config import *


def flip(buffer, width, height):
    new_buffer = np.zeros((width * height), dtype=np.ubyte)
    for i in range(height):
        new_buffer[i * width: (i + 1) * width] = buffer[height - i - 1]

    return new_buffer


class Font:
    def __init__(self, app, name, size):
        self.app = app
        self.ctx = app.ctx

        self.name = name
        self.size = size

        # noinspection PyTypeChecker
        self.face = ft.Face(f"{FONTS_DIR}/{name}.ttf")
        self.face.set_char_size(size[0] * size[1])
        self.glyphs = {}
        self.load_glyphs(string.printable)

    def load_glyphs(self, text):
        for char in text:
            if char in self.glyphs:
                continue

            elif char == " ":
                self.glyphs[char] = self.get_texture(np.zeros((1, 1), dtype=np.ubyte), (1, 1))
                continue

            self.face.load_char(char)
            bitmap = self.face.glyph.bitmap
            size = bitmap.width, bitmap.rows
            buffer = np.array(bitmap.buffer, dtype=np.ubyte).reshape(*size[::-1])
            buffer = flip(buffer, *size)

            self.glyphs[char] = self.get_texture(buffer, size)

    def get_texture(self, buffer, size):
        texture = self.ctx.texture(size=size, components=1,
                                   data=buffer.tobytes(), )
        texture.swizzle = "RRR"  # TODO: Check what it does (Added by copilot, most likely wrong but interesting)
        # mipmaps
        texture.filter = (gl.LINEAR_MIPMAP_LINEAR, gl.LINEAR)
        texture.build_mipmaps()
        # anisotropic filtering
        texture.anisotropy = 16

        return texture

    def __getitem__(self, char):
        if char not in self.glyphs:
            self.load_glyphs(char)

        return self.glyphs[char]
