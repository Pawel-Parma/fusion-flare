from config import *
from models import *


class GameScene:
    def __init__(self, app):
        self.app = app
        self.maze = app.maze
        self.shadow_objects = []
        self.no_shadow_objects = []
        self.load()

    def add_object(self, obj):
        if obj.is_shadowy():
            self.shadow_objects.append(obj)

        else:
            self.no_shadow_objects.append(obj)

    def load(self):
        app = self.app
        add = self.add_object

        s = 2
        add(Cube(app, texture_id="white", position=(-1, -s, -1), scale=(MAZE_WIDTH, 1, MAZE_LENGHT)))
        for x in range(-MAZE_WIDTH, MAZE_WIDTH, s):
            for z in range(-MAZE_LENGHT, MAZE_LENGHT, s):
                if self.maze[int((x + MAZE_WIDTH) / s)][int((z + MAZE_LENGHT) / s)] == "#":
                    add(Cube(app, texture_id="img", position=(x, -s + 2, z)))

                elif self.maze[int((x + MAZE_WIDTH) / s)][int((z + MAZE_LENGHT) / s)] == "s":
                    print(x, z)
                    for y in range(2, 6, s):
                        add(Cube(app, texture_id="img_2", position=(x, -s + y, z)))

                elif self.maze[int((x + MAZE_WIDTH) / s)][int((z + MAZE_LENGHT) / s)] == "e":
                    for y in range(2, 6, s):
                        add(Cube(app, texture_id="img_1", position=(x, -s + y, z)))

    def update(self):
        pass
