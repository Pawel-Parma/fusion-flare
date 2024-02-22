# from typing import override

from ...models import *

from ..scene import BaseScene


class EndGameMenu(BaseScene):
    def __init__(self, app):
        super().__init__(app)

    # @override
    def create_objects(self):
        app = self.app
        add = self.add_object

        # buttons
        hover_texture = "white"
        # play
        new_game_button = add(Button(app, (-6, -0.5, 0), "bronze_panel", hover_texture, scale=(1.5, 0.5)))
        new_game_button.on_click(lambda: app.play(new_maze=True))
        # replay
        replay_button = add(Button(app, (-6, -2, 0), "bronze_panel", hover_texture, scale=(1.5, 0.5)))
        replay_button.on_click(app.play)
        # exit
        exit_button = add(Button(app, (-6, -3.5, 0), "wooden_box", hover_texture, scale=(1.5, 0.5)))
        exit_button.on_click(app.main_menu)

        # bind buttons
        new_game_button.set_chosen()
        new_game_button.down_button(replay_button)

        replay_button.up_button(new_game_button)
        replay_button.down_button(exit_button)

        exit_button.up_button(replay_button)
