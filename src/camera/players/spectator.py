import pygame as pg
import glm

from config import *
from camera.camera import Camera


class SpectatorPlayer(Camera):
    def __init__(self, app, position=(0, 0, 0), yaw=0, pitch=0):
        self.app = app
        self.key_binds = app.key_binds
        super().__init__(position, yaw, pitch)

    def update(self):
        self.keyboard_control()
        self.mouse_control()
        super().update()

    def keyboard_control(self):
        velocity = CAMERA_SPEED * self.app.delta_time
        keys = pg.key.get_pressed()

        if keys[self.key_binds.camera_up]:
            self.move_up(velocity)

        if keys[self.key_binds.camera_down]:
            self.move_down(velocity)

        if keys[self.key_binds.camera_forward]:
            self.move_forward(velocity)

        if keys[self.key_binds.camera_backward]:
            self.move_backward(velocity)

        if keys[self.key_binds.camera_left]:
            self.move_left(velocity)

        if keys[self.key_binds.camera_right]:
            self.move_right(velocity)

    def mouse_control(self):
        delta_x, delta_y = pg.mouse.get_rel()
        if delta_x:
            self.rotate_yaw(delta_x * MOUSE_SENSITIVITY)

        if delta_y:
            self.rotate_pitch(delta_y * MOUSE_SENSITIVITY)
