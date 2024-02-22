# from typing import override

from ...models import *

from ..scene import BaseScene


class EscMenuScene(BaseScene):
    def __init__(self, app):
        super().__init__(app)

    # @override
    def create_objects(self):
        app = self.app
        add = self.add_object

        # buttons
        hover_texture = "white"
        # play
        play_button = add(Button(app, (0, -0.5, 0), "white", hover_texture, scale=(1.5, 0.5),
                                 default_color=(0, 125, 0), hover_color=(0, 255, 0)))
        play_button.on_click(app.play)
        # settings
        settings_button = add(Button(app, (0, -2, 0), "black", hover_texture, scale=(1.5, 0.5),
                                     hover_color=(255, 255, 0)))
        # exit
        exit_button = add(Button(app, (0, -3.5, 0), "white", hover_texture, scale=(1.5, 0.5),
                                 default_color=(125, 0, 0), hover_color=(255, 0, 0)))
        exit_button.on_click(app.main_menu)
        # bind buttons
        play_button.set_chosen()
        play_button.down_button(settings_button)

        settings_button.up_button(play_button)
        settings_button.down_button(exit_button)

        exit_button.up_button(settings_button)
