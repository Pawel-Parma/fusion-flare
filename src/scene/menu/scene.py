from config import *
from models import *


class MenuScene:
    def __init__(self, app):
        self.app = app
        self.maze = app.maze
        self.no_shadow_objects = []
        self.load()

    def add_object(self, obj):
        self.no_shadow_objects.append(obj)

    def load(self):
        app = self.app
        add = self.add_object

        add(Button(app, "none", position=(-1, -1, 0), rotation=(73, 43, 0)))
        add(Cube(app, "black", position=(-1, -2, 0), rotation=(73, 43, 0)))
        add(Button(app, "none", position=(-1, -3, 0), rotation=(73, 43, 0)))
        add(Cube(app, "white", position=(-1, -4, 0), rotation=(73, 43, 0)))
        add(Button(app, "none", position=(-1, -5, 0), rotation=(73, 43, 0)))

    def update(self):
        pass
