# from typing import override

from src.models import *

from src.scenes import BaseScene


class EndGameMenuScene(BaseScene):
    def __init__(self, app):
        super().__init__(app)

    # @override
    def create_objects(self):
        app = self.app
        add = self.add_object

        # buttons
        hover_texture = "white"
        # play again
        play_again_button = add(Button(app, (-6, -2, 0), "white", hover_texture, scale=(1.5, 0.5),
                                       default_color=(0, 125, 0), hover_color=(0, 255, 0)))
        play_again_button.on_click(lambda: app.play(new_maze=True))
        # exit
        exit_button = add(Button(app, (-6, -3.5, 0), "white", hover_texture, scale=(1.5, 0.5),
                                 default_color=(125, 0, 0), hover_color=(255, 0, 0)))
        exit_button.on_click(app.main_menu)

        # bind buttons
        play_again_button.set_chosen()
        play_again_button.down_button(exit_button)

        exit_button.up_button(play_again_button)
