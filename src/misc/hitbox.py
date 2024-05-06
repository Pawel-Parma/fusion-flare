class HitBox:
    def __init__(self, position, size, rotation):
        self.position = position
        self.size = size
        self.rotation = rotation

        # self.vertices = self.get_vertices()
        # self.surfaces = self.get_surfaces()

    def get_vertices(self):
        pass

    def get_surfaces(self):
        pass

    def update(self, position, size, rotation):
        if (self.position, self.size, self.rotation) == (position, size, rotation):
            return

        # self.vertices = self.get_vertices()
        # self.surfaces = self.get_surfaces()
