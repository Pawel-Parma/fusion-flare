import glm
import pygame as pg
from common import *


class Camera:  # TODO: change to better
    def __init__(self, app, position, yaw=-90, pitch=0):
        self.app = app
        self.aspect_ratio = WINDOW_WIDTH / WINDOW_HEIGHT
        self.position = glm.vec3(position)
        self.up = glm.vec3(0, 1, 0)
        self.right = glm.vec3(1, 0, 0)
        self.forward = glm.vec3(0, 0, -1)
        self.yaw = yaw
        self.pitch = pitch
        # view matrix
        self.m_view = self.get_view_matrix()
        # projection matrix
        self.m_proj = self.get_projection_matrix()

    def rotate(self):
        rel_x, rel_y = pg.mouse.get_rel()
        self.yaw += rel_x * MOUSE_SENSITIVITY
        self.pitch -= rel_y * MOUSE_SENSITIVITY
        self.pitch = max(-89, min(89, self.pitch))

    def update_camera_vectors(self):
        yaw, pitch = glm.radians(self.yaw), glm.radians(self.pitch)

        self.forward.x = glm.cos(yaw) * glm.cos(pitch)
        self.forward.y = glm.sin(pitch)
        self.forward.z = glm.sin(yaw) * glm.cos(pitch)

        self.forward = glm.normalize(self.forward)
        self.right = glm.normalize(glm.cross(self.forward, glm.vec3(0, 1, 0)))
        self.up = glm.normalize(glm.cross(self.right, self.forward))

    def update(self):
        self.move()
        self.rotate()
        self.update_camera_vectors()
        self.m_view = self.get_view_matrix()

    def move(self):  # TODO: Add physics, better movement
        velocity = CAMERA_SPEED * self.app.delta_time
        keys = pg.key.get_pressed()
        if keys[pg.K_w]:
            self.position += self.forward * velocity

        if keys[pg.K_s]:
            self.position -= self.forward * velocity

        if keys[pg.K_a]:
            self.position -= self.right * velocity

        if keys[pg.K_d]:
            self.position += self.right * velocity

        if keys[pg.K_SPACE]:
            self.position += self.up * velocity

        if keys[pg.K_LSHIFT]:
            self.position -= self.up * velocity

    def get_view_matrix(self):
        return glm.lookAt(self.position, self.position + self.forward, self.up)  # + self.forward, self.up) TODO: fix

    def get_projection_matrix(self):
        return glm.perspective(glm.radians(CAMERA_FOV), self.aspect_ratio, CAMERA_NEAR, CAMERA_FAR)
