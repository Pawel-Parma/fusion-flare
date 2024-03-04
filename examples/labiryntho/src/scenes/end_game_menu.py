from typing import override

from src.models import *
from src.i_dont_know_how_to_call_that_package import Color
from src.scenes import BaseScene


class EndGameMenuScene(BaseScene):
    def __init__(self, app):
        super().__init__(app)

    @override
    def create_objects(self):
        app = self.app
        add = self.add_object

        # buttons
        hover_texture = "white"
        # play again
        play_again_button = add(
            Button(app, "white", hover_texture, (-6, -2, 0), size=(1.5, 0.5), default_color=Color(0, 125, 0),
                   hover_color=Color(0, 255, 0)))
        add(Text(app, "comic-sans", "Play again", (-6 - 0.05, -2, 0.01), size=(0.16, 0.37)))
        play_again_button.on_click(lambda: app.play(new_maze=True))
        # exit
        exit_button = add(
            Button(app, "white", hover_texture, (-6, -3.5, 0), size=(1.5, 0.5), default_color=Color(125, 0, 0),
                   hover_color=Color(255, 0, 0)))
        add(Text(app, "comic-sans", "Exit", (-6 - 0.36, -3.5, 0.01), size=(0.5, 0.4)))
        exit_button.on_click(app.main_menu)

        # bind buttons
        play_again_button.set_chosen()
        play_again_button.down_button(exit_button)

        exit_button.up_button(play_again_button)
