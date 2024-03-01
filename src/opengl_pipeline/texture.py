import os
import os.path as op

import pygame as pg
import moderngl as gl

from ..config import *


class Texture:
    def __init__(self, app):
        self.app = app
        self.ctx = app.ctx

        self.textures = {"depth_texture": self.get_depth_texture()}

        textures_path_list = set(traverse_dir(app.textures_dir_path))
        self.textures_paths = {op.splitext(op.basename(t))[0]: t for t in textures_path_list}

        self.textures_list = set(self.textures_paths.keys())
        self.textures_list.update(self.textures)

    def get_texture(self, name="none", color=None):
        texture = pg.image.load(f"{self.textures_paths[name]}").convert_alpha()
        texture = pg.transform.flip(texture, flip_x=False, flip_y=True)
        if color:
            texture.fill(color, special_flags=pg.BLEND_MULT)

        texture = self.ctx.texture(size=texture.get_size(), components=4,
                                   data=pg.image.tostring(texture, "RGBA"))
        # mipmaps
        texture.filter = (gl.LINEAR_MIPMAP_LINEAR, gl.LINEAR)
        texture.build_mipmaps()
        # anisotropic filtering
        texture.anisotropy = 32

        return texture

    def get_depth_texture(self):
        depth_texture = self.ctx.depth_texture(self.app.window_size)
        depth_texture.repeat_x = False
        depth_texture.repeat_y = False
        return depth_texture

    def __getitem__(self, texture_id):
        if texture_id not in self.textures_list:
            raise KeyError(f"Texture ({texture_id}) not found")

        if texture_id not in self.textures:
            self.textures[texture_id] = self.get_texture(texture_id)

        return self.textures[texture_id]
