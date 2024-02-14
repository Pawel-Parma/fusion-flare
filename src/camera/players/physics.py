import pygame as pg
import glm

# from typing import override

from ...config import *

from .spectator import SpectatorPlayer


class PhysicsPlayer(SpectatorPlayer):
    def __init__(self, app, position, yaw=0, pitch=0):
        super().__init__(app, position, yaw, pitch)
        self.maze = self.app.maze

    # TODO: Add physics (real velocity, acceleration, etc.)
    # @override
    def keyboard_control(self):
        velocity = CAMERA_SPEED * self.app.delta_time
        keys = pg.key.get_pressed()

        if keys[self.key_binds.camera_forward]:
            self.move_forward(velocity)

        if keys[self.key_binds.camera_backward]:
            self.move_backward(velocity)

        if keys[self.key_binds.camera_left]:
            self.move_left(velocity)

        if keys[self.key_binds.camera_right]:
            self.move_right(velocity)
