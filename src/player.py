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

    def keyboard_control(self):  # TODO: Add physics (real velocity, acceleration, etc.)
        velocity = CAMERA_SPEED * self.app.delta_time

        keys = pg.key.get_pressed()

        if keys[pg.K_SPACE]:
            self.move_up(velocity)

        if keys[pg.K_LSHIFT]:
            self.move_down(velocity)

        if keys[pg.K_w]:
            self.move_forward(velocity)

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
