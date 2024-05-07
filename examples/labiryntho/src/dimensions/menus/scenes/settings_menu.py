from typing import override

from src.models import *
from src.sceneable import BaseScene

from ....scenes.common import *


class SettingsMenuScene(BaseScene):
    @override
    def create_children(self):
        add = self.add_child
        app = self.app

        add(Text(app, "comic-sans", "Settings", (0, 3, 0), size=(0.5, 0.6), color=dodger_blue))

        exit_button = add(Button(app, "white", "white", (6, -3.5, 0), size=(1.5, 0.5), default_color=light_red,
                                 hover_color=red))
        add(Text(app, "comic-sans", "Exit", (6 - 0.36, -3.5, 0.01), size=(0.5, 0.4)))

        exit_button.set_chosen()
        exit_button.on_click(self.parent.exit_settings_menu)
