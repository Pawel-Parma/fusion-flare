import glm


class PhongLight:  # TODO: add light that moves with player
    def __init__(self, position, direction=(0, 0, 0), color=(1, 1, 1), intensities=(0.1, 0.8, 1.0)):
        self.position = glm.vec3(position)
        self.color = glm.vec3(color)
        self.direction = glm.vec3(direction)
        # intensities
        self.Ia = intensities[0] * self.color  # ambient
        self.Id = intensities[1] * self.color  # diffuse
        self.Is = intensities[2] * self.color  # specular
        # view matrix
        self.m_view_light = self.get_view_matrix()

    def get_view_matrix(self):
        return glm.lookAt(self.position, self.direction, glm.vec3(0, 1, 0))
