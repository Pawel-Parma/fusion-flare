import pygame as pg
import moderngl as gl


class Texture:
    def __init__(self, ctx):
        self.ctx = ctx
        self.textures = {"test": self.get_texture("../textures/test.png"),  # TODO: add NONE texture
                         "0": self.get_texture("../textures/img.png")}

    def deinit(self):
        [texture.release() for texture in self.textures.values()]

    def get_texture(self, path):  # TODO: add texture.fill((255, 0, 255, 255))
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

    def __getitem__(self, texture_id):
        if texture_id not in self.textures:
            self.textures[texture_id] = self.get_texture(texture_id)

        return self.textures[texture_id]
