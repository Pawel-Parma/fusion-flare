from typing import override

import pygame as pg

from src.sceneable import Dimension

from ...config import *

from .scenes import *


class MenusDimension(Dimension):
    def __init__(self, app, name, parent):
        self.settings_menu_came_from = MenusScenes.MAIN
        super().__init__(app, name, parent)

    @override
    def create_children(self):
        add = self.add_child
        app = self.app

        add(MainMenuScene(app, MenusScenes.MAIN, self))
        add(EscMenuScene(app, MenusScenes.ESC, self))
        add(EndGameMenuScene(app, MenusScenes.END_GAME, self))
        add(SettingsMenuScene(app, MenusScenes.SETTINGS, self))
        add(HistoryMenuScene(app, MenusScenes.HISTORY, self))

        self.add_child_to_render(MenusScenes.MAIN)

    def change_scene(self, scene_name):
        self.app.set_dimension(self)
        self.clear()
        self.add_child_to_render(scene_name)

    def main_menu(self):
        self.change_scene(MenusScenes.MAIN)

    def esc_menu(self):
        self.change_scene(MenusScenes.ESC)

    def end_game_menu(self):
        self.change_scene(MenusScenes.END_GAME)

    def settings_menu(self, came_from):
        self.settings_menu_came_from = came_from
        self.change_scene(MenusScenes.SETTINGS)

    def exit_settings_menu(self):
        match self.settings_menu_came_from:
            case MenusScenes.MAIN:
                self.main_menu()

            case MenusScenes.ESC:
                self.esc_menu()

    def history_menu(self):
        self.change_scene(MenusScenes.HISTORY)

    @override
    def handle_event(self, event):
        if event.type != pg.KEYDOWN:
            return

        key = event.key
        if key == self.app.key_binds.esc_menu and MenusScenes.ESC in self.app.dimension.children_to_render:
            self.app.maze_dimension.play()

    @override
    def update(self):
        self.app.ctx.clear(*MENU_COLOR)
