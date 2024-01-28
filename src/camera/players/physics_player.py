import pygame as pg
import glm

from config import *
from .spectator_player import SpectatorPlayer


class PhysicsPlayer(SpectatorPlayer):
    def __init__(self, app, position, yaw=0, pitch=0):
        super().__init__(app, position, yaw, pitch)
        self.maze = self.app.maze

    # TODO: Add physics (real velocity, acceleration, etc.)
    def keyboard_control(self):
        velocity = CAMERA_SPEED * self.app.delta_time
        keys = pg.key.get_pressed()

        if keys[pg.K_w]:
            self.move_forward(velocity)

        if keys[pg.K_s]:
            self.move_backward(velocity)

        if keys[pg.K_a]:
            self.move_left(velocity)

        if keys[pg.K_d]:
            self.move_right(velocity)

    def update(self):
        self.keyboard_control()
        self.mouse_control()
        self.update_vectors()
        self.update_view_matirx()
