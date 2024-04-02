from typing import override

from src.dimensions import Dimension

from ...config import *

from .scenes import *


class MazeDimension(Dimension):
    def __init__(self, app, name):
        self.maze = app.maze
        super().__init__(app, name)

    @override
    def create_scenes(self):
        add = self.add_scene
        app = self.app

        add(MazeScene(app, MazeScenes.MAZE, self)).new_maze()

        self.scene_to_render = MazeScenes.MAZE

    def play(self, new_maze=False):
        self.app.set_dimension(self)
        if new_maze:
            self.maze.new(MAZE_LENGTH, MAZE_WIDTH)
            self.scenes[MazeScenes.MAZE].new_maze()
            self.app.camera.set_position(self.maze.start_in_map_coords)

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
