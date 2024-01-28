import pygame as pg
import glm

from .spectator_player import SpectatorPlayer
from common import *


class PhysicsPlayer(SpectatorPlayer):
    def __init__(self, app, position=(0, 0.2, 0), yaw=0, pitch=0):
        super().__init__(app, position, yaw, pitch)
        self.maze = self.app.maze

    # TODO: Add physics (real velocity, acceleration, etc.)
    def keyboard_control(self):
        velocity = CAMERA_SPEED * self.app.delta_time
        keys = pg.key.get_pressed()

        if keys[pg.K_w]:
            pos = self.position + self.if_move_forward(velocity)
            print(round(pos.z + 4), round(pos.x + 4))
            print(self.maze[round(pos.z + 4)][round(pos.x + 4)])
            if self.maze[round(pos.z + 4)][round(pos.x + 4)] == ".":
                self.position = pos

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
