from typing import override

import pygame as pg

from src.sceneable import Dimension

from ...config import *

from .scenes import *


class MazeDimension(Dimension):
    def __init__(self, app, name, parent):
        self.maze = app.maze
        super().__init__(app, name, parent)

    @override
    def create_children(self):
        add = self.add_child
        app = self.app

        add(MazeScene(app, MazeScenes.MAZE, self)).new_maze()

        self.add_child_to_render(MazeScenes.MAZE)

    def play(self, new_maze=False):
        self.app.set_dimension(self)
        if new_maze:
            self.maze.new(MAZE_LENGTH, MAZE_WIDTH)
            self.children[MazeScenes.MAZE].new_maze()  # noqa
            self.app.camera.set_position(self.maze.start_in_map_coords)

    @override
    def handle_event(self, event):
        if event.type != pg.KEYDOWN:
            return

        key = event.key
        if key == self.app.key_binds.esc_menu and MazeScenes.MAZE in self.app.dimension.children_to_render.keys():
            self.app.menus_dimension.esc_menu()

    @override
    def update(self):
        self.app.ctx.clear(*SKY_COLOR)

        camera = self.app.camera
        camera.update()

        temp = camera.position.xyz
        temp.x = round(temp.x)
        temp.y = round(temp.y)
        temp.z = round(temp.z)
        if self.maze.end_in_map_coords == temp:
            self.app.menus_dimension.end_game_menu()
