from scenes.renderer import BaseRenderer

from .scene import MainMenu


class MainMenuSceneRenderer(BaseRenderer):
    def __init__(self, app):
        super().__init__(app)

    def create_scene(self):
        return MainMenu(self.app)
