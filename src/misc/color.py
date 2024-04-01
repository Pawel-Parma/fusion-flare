import glm


class Color(glm.vec4):
    def __init__(self, r: float = 255, g: float = 255, b: float = 255, a: float = 1):
        super().__init__(r / 255, g / 255, b / 255, a)

    def r(self):
        return self.x

    def g(self):
        return self.y

    def b(self):
        return self.z

    def a(self):
        return self.w

    def rgb(self):
        return self.x, self.y, self.z