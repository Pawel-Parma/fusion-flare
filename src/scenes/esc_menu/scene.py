# from typing import override

from ...models import *

from ..scene import BaseScene


class EscMenu(BaseScene):
    def __init__(self, app):
        super().__init__(app)

    # @override
    def create_objects(self):
        app = self.app
        add = self.add_object

        # buttons
        hover_texture = "white"
        # play
        play_button = add(Button(app, (0, -0.5, 0), "bronze_panel", hover_texture, scale=(1.5, 0.5)))
        play_button.on_click(app.play)
        # settings
        settings_button = add(Button(app, (0, -2, 0), "black", hover_texture, scale=(1.5, 0.5)))
        # exit
        exit_button = add(Button(app, (0, -3.5, 0), "wooden_box", hover_texture, scale=(1.5, 0.5)))
        exit_button.on_click(app.main_menu)
        # bind buttons
        play_button.set_chosen()
        play_button.down_button(settings_button)

        settings_button.up_button(play_button)
        settings_button.down_button(exit_button)

        exit_button.up_button(settings_button)
