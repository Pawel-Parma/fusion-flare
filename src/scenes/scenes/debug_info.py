import time

# from typing import override

import glm

from ...models import *

from ..scene import BaseScene


class DebugInfoScene(BaseScene):
    def __init__(self, app):
        super().__init__(app)
        self.last_fps_update = time.time()

    def get_fps(self):
        return f"{self.app.clock.get_fps():.0f}"

    def get_position(self):
        pos = self.app.camera.position
        return f"{pos.x:.0f}, {pos.y:.0f}, {pos.z:.0f}"

    # @override
    def create_objects(self):
        add = self.add_object
        app = self.app

        self.position_text_pos_relative = glm.vec3(0, 0.04, -0.13)
        self.position_text = add(Text(app, "comic-sans", f"XYZ: {self.get_position()}", self.position_text_pos_relative,
                                      scale=(0.002, 0.002)))
        self.fps_text_pos_relative = glm.vec3(0, 0.03, -0.13)
        self.fps_text = add(Text(app, "comic-sans", f"FPS: {self.get_fps()}", self.fps_text_pos_relative,
                                 scale=(0.002, 0.002)))

    # @override
    def update(self):
        super().update()
        camera_position = self.app.camera.position

        self.position_text.set_position(camera_position + self.position_text_pos_relative)
        self.position_text.set_text(f"XYZ: {self.get_position()}")

        self.fps_text.set_position(camera_position + self.fps_text_pos_relative)
        self.fps_text.set_text(f"FPS: {self.get_fps()}")
