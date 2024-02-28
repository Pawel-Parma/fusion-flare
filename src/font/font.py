import freetype as ft
import numpy as np
import moderngl as gl


def flip_fold_array(array, width, height):
    out_array = np.zeros(array.size, dtype=array.dtype)
    for i in range(height):
        out_array[i * width: (i + 1) * width] = array[height - i - 1]

    return out_array


def grayscale_to_rgba(array):
    new_shape = array.shape + (4,)
    out_array = np.ones(new_shape, dtype=array.dtype)

    for i in range(3):
        out_array[..., i] = array

    out_array[..., 3] = np.where(array == 255, 255, 0)

    return out_array


class Font:
    def __init__(self, app, name, size):
        self.app = app
        self.ctx = app.ctx

        self.name = name
        self.size = size

        self.face = ft.Face(f"{self.app.fonts_dir_path}/{name}.ttf")
        self.face.set_char_size(size[0] * size[1])
        self.glyphs = {}

    def load_glyphs(self, text):
        for char in text:
            if char in self.glyphs:
                continue

            elif char == " ":
                self.glyphs[char] = self.get_texture(np.zeros((1, 4), dtype=np.ubyte), (1, 1))
                continue

            self.face.load_char(char)

            bitmap = self.face.glyph.bitmap
            size = bitmap.width, bitmap.rows
            buffer = np.array(bitmap.buffer, dtype=np.ubyte).reshape(*size[::-1])
            buffer = flip_fold_array(buffer, *size)
            buffer = grayscale_to_rgba(buffer)

            self.glyphs[char] = self.get_texture(buffer, size)

    def get_texture(self, buffer, size):
        texture = self.ctx.texture(size=size, components=4, data=buffer.tobytes())
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
