# from typing import override

from ...models import *

from ..scene import BaseScene


class MazeScene(BaseScene):
    def __init__(self, app):
        self.maze = app.maze
        super().__init__(app)
    
    # @override
    def create_objects(self):
        pass

    def create_floor(self):
        app = self.app
        add = self.add_object
        
        maze_width = self.maze.width
        maze_length = self.maze.length

        add(Cube(app, texture_id="white", position=(-1, -2, -1), scale=(maze_width, 1, maze_length)))

    def create_maze(self):
        app = self.app
        add = self.add_object
        
        maze_width = self.maze.width
        maze_length = self.maze.length

        for x in range(-maze_width, maze_width, 2):
            for z in range(-maze_length, maze_length, 2):
                if self.maze[int((x + maze_width) / 2)][int((z + maze_length) / 2)] == "#":
                    add(Cube(app, texture_id="wooden_box", position=(x, 0, z), color=(255, 0, 0)))

                elif self.maze[int((x + maze_width) / 2)][int((z + maze_length) / 2)] == "s":
                    for y in range(2, 6, 2):
                        add(Cube(app, texture_id="bronze_panel", position=(x, -2 + y, z), color=(2, 255, 22)))

                elif self.maze[int((x + maze_width) / 2)][int((z + maze_length) / 2)] == "e":
                    for y in range(2, 6, 2):
                        add(Cube(app, texture_id="steel_panel", position=(x, -2 + y, z), color=(213, 140, 120)))

    def remove_maze_objects(self):
        self.shadow_objects.clear()

    def new_maze(self):
        self.remove_maze_objects()
        # Floor
        self.create_floor()
        # Maze
        self.create_maze()
