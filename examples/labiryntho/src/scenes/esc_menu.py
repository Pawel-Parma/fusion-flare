from typing import override

from src.models import *
from src.scenes import BaseScene

from ..config import *

from .common import *


class EscMenuScene(BaseScene):
    @override
    def create_objects(self):
        app = self.app
        add = self.add_object

        # name
        add(Text(app, "comic-sans", "Game menu", (-0.5, 3, 0), size=(0.5, 0.6), color=Color(60, 160, 220)))
        # buttons
        # play
        play_button = add(Button(app, "white", "white", (0, -0.5, 0), size=(1.5, 0.5), default_color=light_green,
                          hover_color=green))
        add(Text(app, "comic-sans", "Resume", (-0.36, -0.5, 0.01), size=(0.25, 0.4)))
        # settings
        settings_button = add(Button(app, "black", "white", (0, -2, 0), size=(1.5, 0.5), hover_color=yellow))
        add(Text(app, "comic-sans", "Settings", (0, -2, 0.01), size=(0.23, 0.4)))
        # exit
        exit_button = add(Button(app, "white", "white", (0, -3.5, 0), size=(1.5, 0.5), default_color=light_red,
                          hover_color=red))
        add(Text(app, "comic-sans", "Exit", (-0.36, -3.5, 0.01), size=(0.5, 0.4)))
        
        # bind buttons
        play_button.on_click(app.play)
        play_button.set_chosen()
        play_button.down_button(settings_button)

        settings_button.on_click(lambda: app.settings_menu(came_from=GameScene.ESC_MENU))
        settings_button.up_button(play_button)
        settings_button.down_button(exit_button)
        
        exit_button.on_click(app.main_menu)
        exit_button.up_button(settings_button)
