from typing import override

from src.models import *
from src.i_dont_know_how_to_call_that_package import Color
from src.scenes import BaseScene


class HistoryMenuScene(BaseScene):
    def __init__(self, app):
        super().__init__(app)

    @override
    def create_objects(self):
        add = self.add_object
        app = self.app

        # name
        add(Text(app, "comic-sans", "History", (0, 3, 0), size=(0.5, 0.6), color=Color(60, 160, 220)))

        # buttons
        exit_button = add(Button(app, "white", "white", (6, -3.5, 0), size=(1.5, 0.5), default_color=Color(125, 0, 0),
                                 hover_color=Color(255, 0, 0)))
        add(Text(app, "comic-sans", "Exit", (6 - 0.36, -3.5, 0.01), size=(0.5, 0.4)))
        exit_button.on_click(app.main_menu)
        exit_button.set_chosen()
