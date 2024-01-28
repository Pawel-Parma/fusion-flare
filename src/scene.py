from models import *


class Scene:
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

        n, s = len(self.maze), 2
        for x in range(-n, n, s):
            for z in range(-n, n, s):
                if self.maze[int((x + n) / s)][int((z + n) / s)] == ".":
                    add(Cube(app, texture_id="img", position=(x, -s, z)))

        for x in range(-n, n, s):
            for z in range(-n, n, s):
                if self.maze[int((x + n) / s)][int((z + n) / s)] == "#":
                    add(Cube(app, texture_id="img_1", position=(x, -s + 2, z)))

        for y in range(0, n, s):
            add(Cube(app, texture_id="img_1", position=(0, y + 3, 0)))

    def update(self):
        pass
