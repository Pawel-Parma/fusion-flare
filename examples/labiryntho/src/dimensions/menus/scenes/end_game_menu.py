from typing import override

from src.models import *
from src.sceneable import BaseScene

from ....scenes.common import *


class EndGameMenuScene(BaseScene):
    @override
    def create_children(self):
        add = self.add_child
        app = self.app

        play_again_button = add(Button(app, "white", "white", (-6, -2, 0), size=(1.5, 0.5), default_color=light_green,
                                       hover_color=green))
        add(Text(app, "comic-sans", "Play again", (-6 - 0.05, -2, 0.01), size=(0.16, 0.37)))

        exit_button = add(Button(app, "white", "white", (-6, -3.5, 0), size=(1.5, 0.5), default_color=light_red,
                                 hover_color=red))
        add(Text(app, "comic-sans", "Exit", (-6 - 0.36, -3.5, 0.01), size=(0.5, 0.4)))

        play_again_button.on_click(lambda: app.maze_dimension.play(new_maze=True))
        play_again_button.set_chosen()
        play_again_button.down_button(exit_button)

        exit_button.on_click(self.parent.main_menu)
        exit_button.up_button(play_again_button)
