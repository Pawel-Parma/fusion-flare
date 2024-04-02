from typing import override

from src.models import *
from src.scenes import BaseScene

from ....config import *
from ....scenes.common import *

from .types import *


class MainMenuScene(BaseScene):
    @override
    def create_objects(self):
        app = self.app
        add = self.add_object

        # name
        add(Text(app, "comic-sans", APP_NAME, (0.36, 3, 0), size=(0.5, 0.6), color=dodger_blue))
        # buttons
        # play
        play_button = add(Button(app, "white", "white", (0, -0.5, 0), size=(1.5, 0.5), default_color=light_green,
                                 hover_color=green))
        add(Text(app, "comic-sans", "Play", (-0.36, -0.5, 0.01), size=(0.5, 0.4)))
        # history
        history_button = add(Button(app, "black", "white", (0, -2, 0), size=(1.5, 0.5), hover_color=yellow))
        add(Text(app, "comic-sans", "History", (0, -2, 0.01), size=(0.25, 0.4)))
        # settings
        settings_button = add(Button(app, "black", "white", (0, -3.5, 0), size=(1.5, 0.5), hover_color=yellow))
        add(Text(app, "comic-sans", "Settings", (0, -3.5, 0.01), size=(0.23, 0.4)))
        # exit
        exit_button = add(Button(app, "white", "white", (6, -3.5, 0), size=(1.5, 0.5), default_color=light_red,
                                 hover_color=red, is_dynamic=True))
        add(Text(app, "comic-sans", "Exit", (6 - 0.36, -3.5, 0.01), size=(0.5, 0.4)))

        # bind buttons
        play_button.set_chosen()
        play_button.on_click(lambda: app.maze_dimension.play(new_maze=True))
        play_button.right_button(exit_button)
        play_button.down_button(history_button)

        history_button.on_click(self.parent.history_menu)
        history_button.up_button(play_button)
        history_button.right_button(exit_button)
        history_button.down_button(settings_button)

        settings_button.on_click(lambda: self.parent.settings_menu(came_from=MenusScenes.MAIN))
        settings_button.up_button(history_button)
        settings_button.right_button(exit_button)

        exit_button.on_click(app.quit)
