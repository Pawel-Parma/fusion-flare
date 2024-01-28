import os
import os.path as op

import pygame as pg
import moderngl as gl

from common import *


class Texture:
    def __init__(self, app):
        self.app = app
        self.ctx = app.ctx

        self.textures = {"none": self.get_texture(),
                         "blue": self.get_texture(color=(0, 23, 255)),
                         "img": self.get_texture("img", color=(255, 0, 0)),
                         "img_1": self.get_texture("img_1", color=(23, 140, 60)),
                         "light_gray": self.get_texture(color=(123, 123, 123)),
                         # TODO: add outline none and outline transformation
                         "depth_texture": self.get_depth_texture()}

        self.textures_list = {t[:t.rfind(".")] for t in os.listdir(TEXTURES_DIR) if op.isfile(op.join(TEXTURES_DIR, t))}
        self.textures_list.update(set(self.textures))

    def deinit(self):
        [texture.release() for texture in self.textures.values()]

    def get_texture(self, name="none", extension=".png", color=None):
        texture = pg.image.load(op.join(TEXTURES_DIR, name + extension))
        texture = texture.convert()
        texture = pg.transform.flip(texture, flip_x=False, flip_y=True)
        if color:
            texture.fill(color, special_flags=pg.BLEND_MULT)

        texture = self.ctx.texture(size=texture.get_size(), components=3,
                                   data=pg.image.tostring(texture, "RGB"))
        # mipmaps
        texture.filter = (gl.LINEAR_MIPMAP_LINEAR, gl.LINEAR)
        texture.build_mipmaps()
        # anisotropic filtering
        texture.anisotropy = 32

        return texture

    def get_depth_texture(self):
        depth_texture = self.ctx.depth_texture(WINDOW_SIZE)
        depth_texture.repeat_x = False
        depth_texture.repeat_y = False
        return depth_texture

    def __getitem__(self, texture_id, **kwargs):
        if texture_id not in self.textures_list:
            raise KeyError(f"Texture {texture_id} not found")

        if texture_id not in self.textures:
            self.textures[texture_id] = self.get_texture(texture_id, **kwargs)

        return self.textures[texture_id]
