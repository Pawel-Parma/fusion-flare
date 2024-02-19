import pygame as pg
import glm

from ..config import *


class CameraInterface:
    default_up = glm.vec3(0, 1, 0)
    default_right = glm.vec3(1, 0, 0)
    default_front = glm.vec3(0, 0, -1)

    def __init__(self, position, yaw, pitch):
        self.position = glm.vec3(position)
        self.yaw = glm.radians(yaw)
        self.pitch = glm.radians(pitch)
        
        self.up = glm.vec3(0, 1, 0)
        self.right = glm.vec3(1, 0, 0)
        self.front = glm.vec3(0, 0, -1)

        self.m_view = glm.lookAt(self.position, self.position + self.front, self.up)
        self.m_proj = glm.perspective(glm.radians(CAMERA_FOV), WINDOW_WIDTH / WINDOW_HEIGHT, CAMERA_NEAR, CAMERA_FAR)

    def use_vars_from(self, camera):
        self.position = camera.position
        self.yaw = camera.yaw
        self.pitch = camera.pitch
        self.up = camera.up
        self.right = camera.right
        self.front = camera.front
        self.m_view = camera.m_view
        self.m_proj = camera.m_proj


class Camera(CameraInterface):
    def __init__(self, position, yaw, pitch):
        super().__init__(position, yaw, pitch)

    def set_position(self, position):
        self.position = glm.vec3(position)

    def update_vectors(self):
        self.front.x = glm.cos(self.yaw) * glm.cos(self.pitch)
        self.front.y = glm.sin(self.pitch)
        self.front.z = glm.sin(self.yaw) * glm.cos(self.pitch)

        self.front = glm.normalize(self.front)
        self.right = glm.normalize(glm.cross(self.front, glm.vec3(0, 1, 0)))
        self.up = glm.normalize(glm.cross(self.right, self.front))

    def update_view_matirx(self):
        self.m_view = glm.lookAt(self.position, self.position + self.front, self.up)

    def rotate_yaw(self, delta_x):
        self.yaw += delta_x

    def rotate_pitch(self, delta_y):
        self.pitch -= delta_y
        self.pitch = glm.clamp(self.pitch, glm.radians(CAMERA_PITCH_MIN), glm.radians(CAMERA_PITCH_MAX))

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

        if abs(self.yaw % (PI * 2)) <= PI / 2:
            move_vector -= self.__class__.default_front + (self.right - self.front) * glm.cos(self.yaw)

        if PI / 2 < abs(self.yaw % (PI * 2)) <= PI:
            move_vector -= self.__class__.default_right + (self.right - self.front) * glm.sin(self.yaw)

        if PI < abs(self.yaw % (PI * 2)) <= PI * 3 / 2:
            move_vector += self.__class__.default_front + (self.right - self.front) * glm.cos(self.yaw)

        if PI * 3 / 2 < abs(self.yaw % (PI * 2)):
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
        self.update_view_matirx()
