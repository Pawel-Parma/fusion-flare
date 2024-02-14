from ..renderer import BaseRenderer

from .scene import EndGameMenu


class EndGameMenuSceneRenderer(BaseRenderer):
    def __init__(self, app):
        super().__init__(app)

    def create_scene(self):
        return EndGameMenu(self.app)
