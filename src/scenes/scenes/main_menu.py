# from typing import override

from ...config import *
from ...models import *

from ..scene import BaseScene


class MainMenuScene(BaseScene):
    def __init__(self, app):
        super().__init__(app)

    # @override
    def create_objects(self):
        app = self.app
        add = self.add_object

        # name
        add(Text(app, "comic-sans", APP_NAME, (0, 2, 0), scale=(0.5, 0.6), color=(60, 160, 220)))
        # buttons
        hover_texture = "white"
        # play
        play_button = add(Button(app, (0, -0.5, 0), "white", hover_texture, scale=(1.5, 0.5),
                                 default_color=(0, 125, 0), hover_color=(0, 255, 0)))
        play_button.on_click(lambda: app.play(new_maze=True))
        # history
        history_button = add(Button(app, (0, -2, 0), "black", hover_texture, scale=(1.5, 0.5),
                                    hover_color=(255, 255, 0)))
        # settings
        settings_button = add(Button(app, (0, -3.5, 0), "black", hover_texture, scale=(1.5, 0.5),
                                     hover_color=(255, 255, 0)))
        settings_button.on_click(app.settings_menu)
        # exit
        exit_button = add(Button(app, (6, -3.5, 0), "white", hover_texture, scale=(1.5, 0.5),
                                 default_color=(125, 0, 0), hover_color=(255, 0, 0), is_dynamic=True))
        exit_button.on_click(app.quit)
        # bind buttons
        play_button.set_chosen()
        play_button.right_button(exit_button)
        play_button.down_button(history_button)

        history_button.up_button(play_button)
        history_button.right_button(exit_button)
        history_button.down_button(settings_button)

        settings_button.up_button(history_button)
        settings_button.right_button(exit_button)
