import pygame as pg

from typing import override

from .spectator import SpectatorPlayer


class PhysicsPlayer(SpectatorPlayer):
    def __init__(self, app, position, speed=0.01, mouse_sensitivity=0.002, fov=50, near=0.1, far=80, pitch_min=-89,
                 pitch_max=89, yaw=0, pitch=0):
        super().__init__(app, speed, mouse_sensitivity, fov, near, far, pitch_min, pitch_max, position, yaw, pitch)

    # TODO: Add physics (real velocity, acceleration, etc.), implement hit box, add collision detection in BaseModel
    @override
    def keyboard_control(self):
        velocity = self.speed * self.app.delta_time
        keys = pg.key.get_pressed()

        if keys[self.key_binds.camera_forward]:
            self.move_forward(velocity)

        if keys[self.key_binds.camera_backward]:
            self.move_backward(velocity)

        if keys[self.key_binds.camera_left]:
            self.move_left(velocity)

        if keys[self.key_binds.camera_right]:
            self.move_right(velocity)
