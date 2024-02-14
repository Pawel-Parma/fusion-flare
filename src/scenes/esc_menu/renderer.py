from ..renderer import BaseRenderer

from .scene import EscMenu


class EscMenuSceneRenderer(BaseRenderer):
    def __init__(self, app):
        super().__init__(app)

    def create_scene(self):
        return EscMenu(self.app)
