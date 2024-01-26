import pygame as pg
import moderngl as gl


class Texture:
    def __init__(self, app):
        self.app = app
        self.ctx = app.ctx
        self.textures = {"test": self.get_texture("../textures/test.png"),  # TODO: add NONE texture
                         "0": self.get_texture("../textures/img.png"),
                         "1": self.get_texture("../textures/img_1.png"),

                         "depth_texture": self.get_depth_texture()}

    def deinit(self):
        [texture.release() for texture in self.textures.values()]

    def get_texture(self, path):  # TODO: add texture.fill((255, 0, 255, 255)), color etc.
        texture = pg.image.load(path)
        texture = texture.convert()
        texture = pg.transform.flip(texture, flip_x=False, flip_y=True)
        texture = self.ctx.texture(size=texture.get_size(), components=3,
                                   data=pg.image.tostring(texture, "RGB"))
        # mipmaps
        texture.filter = (gl.LINEAR_MIPMAP_LINEAR, gl.LINEAR)
        texture.build_mipmaps()
        # anisotropic filtering
        texture.anisotropy = 32

        return texture

    def get_depth_texture(self):
        depth_texture = self.ctx.depth_texture(self.app.WIN_SIZE)
        depth_texture.repeat_x = False
        depth_texture.repeat_y = False
        return depth_texture

    def __getitem__(self, texture_id):
        if texture_id not in self.textures:
            self.textures[texture_id] = self.get_texture(texture_id)

        return self.textures[texture_id]
