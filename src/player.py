import pygame as pg
import glm

from camera import Camera
from common import *


class Player(Camera):
    def __init__(self, app, position=(0, 0, 0), yaw=0, pitch=0):
        self.app = app
        super().__init__(position, yaw, pitch)

    def update(self):
        self.keyboard_control()
        self.mouse_control()
        super().update()

    def keyboard_control(self):  # TODO: Add physics, better movement
        velocity = CAMERA_SPEED * self.app.delta_time

        keys = pg.key.get_pressed()

        if keys[pg.K_SPACE]:
            self.move_up(velocity)

        if keys[pg.K_LSHIFT]:
            self.move_down(velocity)

        if keys[pg.K_w]:
            move_vector = glm.vec3(0, 0, 0)
            if abs(self.yaw % (PI * 2)) <= PI / 2:
                move_vector += glm.vec3(0, 0, 1) + (-self.right + self.front) * glm.cos(self.yaw)

            if PI / 2 < abs(self.yaw % (PI * 2)) <= PI:
                move_vector -= glm.vec3(1, 0, 0) + (self.right - self.front) * glm.sin(self.yaw)

            if PI < abs(self.yaw % (PI * 2)) <= PI * 3 / 2:
                move_vector -= glm.vec3(0, 0, 1) + (-self.right + self.front) * glm.cos(self.yaw)

            if PI * 3 / 2 < abs(self.yaw % (PI * 2)):
                move_vector += glm.vec3(1, 0, 0) + (self.right - self.front) * glm.sin(self.yaw)

            move_vector.y = 0
            self.position += glm.normalize(move_vector) * velocity

        if keys[pg.K_s]:
            self.move_backward(velocity)

        if keys[pg.K_a]:
            self.move_left(velocity)

        if keys[pg.K_d]:
            self.move_right(velocity)

    def mouse_control(self):
        delta_x, delta_y = pg.mouse.get_rel()
        if delta_x:
            self.rotate_yaw(delta_x * MOUSE_SENSITIVITY)

        if delta_y:
            self.rotate_pitch(delta_y * MOUSE_SENSITIVITY)