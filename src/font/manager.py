import os
import os.path as op

from .font import Font


class FontManager:
    def __init__(self, app):
        self.app = app
        self.available_fonts = set(op.splitext(font)[0] for font in os.listdir(app.fonts_dir_path))
        self.loaded_fonts = {}

    def __getitem__(self, full_name: tuple[str, tuple[int, int]]):
        if full_name[0] not in self.available_fonts:
            raise Exception(f"Font ({full_name[0]}) not found")

        if full_name not in self.loaded_fonts:
            self.loaded_fonts[full_name] = Font(self.app, *full_name)

        return self.loaded_fonts[full_name]
