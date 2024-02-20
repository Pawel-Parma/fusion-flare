import os
import os.path as op

from .font import Font

from ..config import *


class FontManager:
    def __init__(self, app):
        self.app = app
        self.font_list = set(op.splitext(font)[0] for font in os.listdir(FONTS_DIR))
        self.fonts = {("comic-sans", (96, 96)): Font(app, "comic-sans", (96, 96))}

    def __getitem__(self, full_name: tuple[str, tuple[int, int]]):
        if full_name[0] not in self.font_list:
            raise Exception(f"Font ({full_name[0]}) not found")

        if full_name not in self.fonts:
            self.fonts[full_name] = Font(self.app, *full_name)

        return self.fonts[full_name]
