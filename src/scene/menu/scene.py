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

        add(Button(app, position=(-1, -1, 2), color=(125, 125, 125), hover_color=(255, 255, 255)))
        add(Cube(app, "white", position=(0, 0, 0), rotation=(0, 0, 0), scale=(1, 1, 1)))

    def update(self):
        pass
