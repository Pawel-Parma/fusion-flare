import pygame as pg

from typing import override

from ..camera import Camera


class SpectatorPlayer(Camera):
    def __init__(self, app, speed=0.01, mouse_sensitivity=0.002, fov=50, near=0.1, far=80, pitch_min=-89, pitch_max=89,
                 position=(0, 0, 0), yaw=0, pitch=0):
        super().__init__(app, speed, mouse_sensitivity, fov, near, far, pitch_min, pitch_max, position, yaw, pitch)
        self.key_binds = app.key_binds

    def keyboard_control(self):
        velocity = self.speed * self.app.delta_time
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

        self.rotate_yaw(delta_x * self.mouse_sensitivity)
        if delta_y:
            self.rotate_pitch(delta_y * self.mouse_sensitivity)

    @override
    def update(self):
        self.keyboard_control()
        self.mouse_control()
        super().update()
