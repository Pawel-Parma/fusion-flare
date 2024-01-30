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
        return obj

    def load(self):
        app = self.app
        add = self.add_object

        b1 = add(Button(app, position=(0, 0, 0), hover_color=(125, 125, 125), color=(255, 0, 0)))
        b2 = add(Button(app, position=(0, -4, 0), hover_color=(125, 125, 125), color=(0, 255, 0)))
        b1.set_chosen()
        # b1.down_button(b2)
        # b2.up_button(b1)

        # b3 = add(Button(app, position=(-1, -7, 2), color=(125, 125, 125), hover_color=(0, 255, 0)))
        # b4 = add(Button(app, position=(-1, -10, 2), color=(125, 125, 125), hover_color=(0, 255, 0)))
        # b5 = add(Button(app, position=(-1, -13, 2), color=(125, 125, 125), hover_color=(0, 255, 0)))

        add(Cube(app, "white", position=(0, -2, 0), rotation=(0, 0, 0), scale=(1, 1, 1)))

    def update(self):
        pass
