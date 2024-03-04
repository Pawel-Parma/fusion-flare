import glm


class CameraInterface:
    default_up = glm.vec3(0, 1, 0)
    default_right = glm.vec3(1, 0, 0)
    default_front = glm.vec3(0, 0, -1)

    def __init__(self, app, position, yaw, pitch, fov, near, far):
        self.app = app

        self.position = glm.vec3(position)
        self.yaw = glm.radians(yaw)
        self.pitch = glm.radians(pitch)

        self.fov = fov
        self.near = near
        self.far = far

        self.up = glm.vec3(0, 1, 0)
        self.right = glm.vec3(1, 0, 0)
        self.front = glm.vec3(0, 0, -1)

        self.m_view = glm.lookAt(self.position, self.position + self.front, self.up)
        self.m_proj = glm.perspective(glm.radians(fov), app.window_size[0] / app.window_size[1], near, far)

    def use_vars_from(self, camera):
        self.position = camera.position
        self.yaw = camera.yaw
        self.pitch = camera.pitch
        self.fov = camera.fov
        self.near = camera.near
        self.far = camera.far
        self.up = camera.up
        self.right = camera.right
        self.front = camera.front
        self.m_view = camera.m_view
        self.m_proj = camera.m_proj


class Camera(CameraInterface):
    def __init__(self, app, speed, mouse_sensitivity, fov, near, far, pitch_min, pitch_max, position, yaw, pitch):
        super().__init__(app, position, yaw, pitch, fov, near, far)
        self.speed = speed
        self.mouse_sensitivity = mouse_sensitivity
        self.pitch_max = pitch_max
        self.pitch_min = pitch_min

    def set_position(self, position):
        self.position = glm.vec3(position)

    def update_vectors(self):
        self.front.x = glm.cos(self.yaw) * glm.cos(self.pitch)
        self.front.y = glm.sin(self.pitch)
        self.front.z = glm.sin(self.yaw) * glm.cos(self.pitch)

        self.front = glm.normalize(self.front)
        self.right = glm.normalize(glm.cross(self.front, glm.vec3(0, 1, 0)))
        self.up = glm.normalize(glm.cross(self.right, self.front))

    def update_view_matrix(self):
        self.m_view = glm.lookAt(self.position, self.position + self.front, self.up)

    def rotate_yaw(self, delta_x):
        self.yaw += delta_x

    def rotate_pitch(self, delta_y):
        self.pitch -= delta_y
        self.pitch = glm.clamp(self.pitch, glm.radians(self.pitch_min), glm.radians(self.pitch_max))

    def if_move_up(self, velocity):
        return self.__class__.default_up * velocity

    def move_up(self, velocity):
        self.position += self.if_move_up(velocity)

    def if_move_down(self, velocity):
        return - self.__class__.default_up * velocity

    def move_down(self, velocity):
        self.position += self.if_move_down(velocity)

    def if_move_forward(self, velocity):
        move_vector = glm.vec3(0, 0, 0)
        pi = glm.pi()
        if abs(self.yaw % (pi * 2)) <= pi / 2:
            move_vector -= self.__class__.default_front + (self.right - self.front) * glm.cos(self.yaw)

        if pi / 2 < abs(self.yaw % (pi * 2)) <= pi:
            move_vector -= self.__class__.default_right + (self.right - self.front) * glm.sin(self.yaw)

        if pi < abs(self.yaw % (pi * 2)) <= pi * 3 / 2:
            move_vector += self.__class__.default_front + (self.right - self.front) * glm.cos(self.yaw)

        if pi * 3 / 2 < abs(self.yaw % (pi * 2)):
            move_vector += self.__class__.default_right + (self.right - self.front) * glm.sin(self.yaw)

        move_vector.y = 0
        return glm.normalize(move_vector) * velocity

    def move_forward(self, velocity):
        self.position += self.if_move_forward(velocity)

    def if_move_backward(self, velocity):
        return self.if_move_forward(-velocity)

    def move_backward(self, velocity):
        self.position += self.if_move_backward(velocity)

    def if_move_right(self, velocity):
        return self.right * velocity

    def move_right(self, velocity):
        self.position += self.if_move_right(velocity)

    def if_move_left(self, velocity):
        return - self.right * velocity

    def move_left(self, velocity):
        self.position += self.if_move_left(velocity)

    def update(self):
        self.update_vectors()
        self.update_view_matrix()
