from scenes.renderer import BaseRenderer

from .scene import MazeScene


class MazeSceneRenderer(BaseRenderer):
    def __init__(self, app):
        super().__init__(app)

    def create_scene(self):
        return MazeScene(self.app)
