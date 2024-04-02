from typing import override

from src.dimensions import Dimension

from ...config import *

from .scenes import *


class MenusDimension(Dimension):
    def __init__(self, app, name):
        super().__init__(app, name)
        self.settings_menu_came_from = MenusScenes.MAIN

    @override
    def create_scenes(self):
        add = self.add_scene
        app = self.app

        add(MainMenuScene(app, MenusScenes.MAIN, self))
        add(EscMenuScene(app, MenusScenes.ESC, self))
        add(EndGameMenuScene(app, MenusScenes.END_GAME, self))
        add(SettingsMenuScene(app, MenusScenes.SETTINGS, self))
        add(HistoryMenuScene(app, MenusScenes.HISTORY, self))

        self.scene_to_render = MenusScenes.MAIN

    def main_menu(self):
        self.app.set_dimension(self)
        self.scene_to_render = MenusScenes.MAIN

    def esc_menu(self):
        self.app.set_dimension(self)
        self.scene_to_render = MenusScenes.ESC

    def end_game_menu(self):
        self.app.set_dimension(self)
        self.scene_to_render = MenusScenes.END_GAME

    def settings_menu(self, came_from):
        self.settings_menu_came_from = came_from
        self.app.set_dimension(self)
        self.scene_to_render = MenusScenes.SETTINGS

    def exit_settings_menu(self):
        match self.settings_menu_came_from:
            case MenusScenes.MAIN:
                self.main_menu()

            case MenusScenes.ESC:
                self.esc_menu()

    def history_menu(self):
        self.app.set_dimension(self)
        self.scene_to_render = MenusScenes.HISTORY

    @override
    def update(self):
        self.app.ctx.clear(*MENU_COLOR)
