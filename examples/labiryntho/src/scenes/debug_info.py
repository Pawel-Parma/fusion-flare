from typing import override

import glm

from src.models import *
from src.sceneable import BaseScene


class DebugInfoScene(BaseScene):
    def get_fps(self):
        return f"{self.app.clock.get_fps():.0f}"

    def get_position(self):
        pos = self.app.camera.position
        return f"{pos.x:.0f}, {pos.y:.0f}, {pos.z:.0f}"

    @override
    def create_children(self):
        add = self.add_child
        app = self.app

        self.position_text_pos_relative = glm.vec3(0, 0.04, -0.13)
        self.position_text = add(Text(app, "comic-sans", f"XYZ: {self.get_position()}", self.position_text_pos_relative,
                                      size=(0.002, 0.002)))
        self.fps_text_pos_relative = glm.vec3(0, 0.03, -0.13)
        self.fps_text = add(Text(app, "comic-sans", f"FPS: {self.get_fps()}", self.fps_text_pos_relative,
                                 size=(0.002, 0.002)))

    @override
    def update(self):
        camera_position = self.app.camera.position

        self.position_text.set_position(camera_position + self.position_text_pos_relative)
        self.position_text.text = f"XYZ: {self.get_position()}"

        self.fps_text.set_position(camera_position + self.fps_text_pos_relative)
        self.fps_text.text = f"FPS: {self.get_fps()}"
