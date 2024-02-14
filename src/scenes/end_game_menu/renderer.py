# from typing import override

from ..renderer import BaseRenderer

from .scene import EndGameMenu


class EndGameMenuSceneRenderer(BaseRenderer):
    def __init__(self, app):
        super().__init__(app)

    # @override
    def create_scene(self):
        return EndGameMenu(self.app)
