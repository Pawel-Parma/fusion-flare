import os
import os.path as op

from .font import Font


class FontManager:
    def __init__(self, app):
        self.app = app
        self.font_list = set(op.splitext(font)[0] for font in os.listdir(app.fonts_dir_path))
        self.fonts = {}

    def __getitem__(self, full_name: tuple[str, tuple[int, int]]):
        if full_name[0] not in self.font_list:
            raise Exception(f"Font ({full_name[0]}) not found")

        if full_name not in self.fonts:
            self.fonts[full_name] = Font(self.app, *full_name)

        return self.fonts[full_name]
