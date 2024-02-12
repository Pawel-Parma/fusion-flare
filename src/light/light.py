import glm


class Light:
    def __init__(self, position, direction=(0, 0, 0), color=(1, 1, 1), ambient=0.1, diffuse=0.8, specular=1.0):
        self.position = glm.vec3(position)
        self.color = glm.vec3(color)
        self.direction = glm.vec3(direction)
        # intensities
        self.intensities = (ambient, diffuse, specular)
        self.Ia = ambient * self.color  # ambient
        self.Id = diffuse * self.color  # diffuse
        self.Is = specular * self.color  # specular
        # view matrix
        self.m_view_light = self.get_view_matrix()

    def get_view_matrix(self):
        return glm.lookAt(self.position, self.direction, glm.vec3(0, 1, 0))

    @staticmethod
    def can_change_position():
        return False

    def update(self):
        pass


class CameraFollowingLight(Light):
    def __init__(self, app, light):
        super().__init__(light.position, light.direction, light.color, *light.intensities)
        self.app = app

    @staticmethod
    def can_change_position():
        return True

    def update(self):
        self.position.xz = self.app.camera.position.xz
        self.position.y = 1
