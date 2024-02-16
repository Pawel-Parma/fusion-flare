import os

from .font import Font

from ..config import *


class FontManager:
    def __init__(self):
        self.font_list = set(os.listdir(FONTS_DIR))
        self.fonts = {("comic-sans", (46, 64)): Font("comic-sans", (48, 64))}

    def __getitem__(self, name, size):
        if name not in self.font_list:
            raise Exception(f"Font {name} not found")

        full_name = (name, size)
        if full_name not in fonts:
            self.fonts[full_name] = Font(*full_name)

        return self.fonts[full_name]


font_manager = FontManager()
