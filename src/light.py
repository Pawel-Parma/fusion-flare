import glm


class PhongLight:
    def __init__(self, position=(3, 3, -3), color=(1, 1, 1)):
        self.position = glm.vec3(position)
        self.color = glm.vec3(color)
        self.direction = glm.vec3(0, 0, 0)
        # intensities
        self.Ia = 0.1 * self.color  # ambient
        self.Id = 0.8 * self.color  # diffuse
        self.Is = 1.0 * self.color  # specular
        # view matrix
        self.m_view_light = self.get_view_matrix()

    def get_view_matrix(self):
        return glm.lookAt(self.position, self.direction, glm.vec3(0, 1, 0))


class CameraFollowingLight:
    def __init__(self, app, light):
        self.app = app
        self.light = light

    def update(self):
        self.light.position = self.app.camera.position
        self.light.m_view_light = self.light.get_view_matrix()
