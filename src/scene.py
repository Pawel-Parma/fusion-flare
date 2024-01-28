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
        # for x in range(-n, n, s):
        #     for z in range(-n, n, s):
        #         if self.maze[int((x + n) / s)][int((z + n) / s)] == ".":
        #             add(Cube(app, texture_id="img", position=(x, -s, z)))
        add(Cube(app, texture_id="light_gray", position=(-1, -s, -1), scale=(n, 1, n)))

        for x in range(-n, n, s):
            for z in range(-n, n, s):
                print(x, z)
                if self.maze[int((x + n) / s)][int((z + n) / s)] == "#":
                    add(Cube(app, texture_id="img_1", position=(x, -s + 2, z)))

    def update(self):
        pass
