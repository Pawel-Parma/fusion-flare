from config import *
from models import *
from scenes.scene import BaseScene


class MazeScene(BaseScene):
    def __init__(self, app):
        self.maze = app.maze
        super().__init__(app)

    def create_objects(self):
        app = self.app
        add = self.add_object

        # Floor
        add(Cube(app, texture_id="white", position=(-1, -2, -1), scale=(MAZE_WIDTH, 1, MAZE_LENGHT)))
        # Maze
        self.create_maze()

    def create_maze(self):
        app = self.app
        add = self.add_object

        for x in range(-MAZE_WIDTH, MAZE_WIDTH, 2):
            for z in range(-MAZE_LENGHT, MAZE_LENGHT, 2):
                if self.maze[int((x + MAZE_WIDTH) / 2)][int((z + MAZE_LENGHT) / 2)] == "#":
                    add(Cube(app, texture_id="img", position=(x, 0, z)))

                elif self.maze[int((x + MAZE_WIDTH) / 2)][int((z + MAZE_LENGHT) / 2)] == "s":
                    for y in range(2, 6, 2):
                        add(Cube(app, texture_id="img_2", position=(x, -2 + y, z)))

                elif self.maze[int((x + MAZE_WIDTH) / 2)][int((z + MAZE_LENGHT) / 2)] == "e":
                    for y in range(2, 6, 2):
                        add(Cube(app, texture_id="img_1", position=(x, -2 + y, z)))

    def remove_maze_objects(self):
        first_shadow = self.shadow_objects[0]
        self.shadow_objects.clear()
        self.shadow_objects.append(first_shadow)

    def new_maze(self):
        self.remove_maze_objects()
        self.create_maze()
