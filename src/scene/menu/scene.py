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

        add(Button(app, "img", (0, 0, 0), scale=(0.5, 0.5, 0.5)))

    def update(self):
        pass
