from model import *
import maze

new_maze = maze.generate_maze(80, 80)


class Scene:
    def __init__(self, app):
        self.app = app
        self.objects = []
        self.load()

    def add_object(self, obj):
        self.objects.append(obj)

    def load(self):
        app = self.app
        add = self.add_object

        n, s = 80, 2
        for x in range(-n, n, s):
            for z in range(-n, n, s):
                if new_maze[int((x + n) / s)][int((z + n) / s)] == ".":
                    add(Cube(app, position=(x, -s, z)))

        for x in range(-n, n, s):
            for z in range(-n, n, s):
                if new_maze[int((x + n) / s)][int((z + n) / s)] == "#":
                    add(Cube(app, position=(x, -s + 2, z), texture_id="test"))

    def render(self):
        for obj in self.objects:
            obj.render()
