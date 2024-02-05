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
        buttons = []
        colors = [(255, 0, 0), (0, 255, 0), (0, 0, 255), (0, 255, 255), (255, 0, 255), (255, 255, 0), (255, 165, 0),
                  (128, 0, 128), (255, 105, 180)]

        for i in range(-1, 2):
            for j in range(-1, 2):
                color = colors[(i * 3 + j + 4) % len(colors)]
                button = add(Button(app, position=(4 * i, 4 * j, 0), hover_color=(155, 155, 155),
                                    color=color))
                buttons.append(button)

        buttons[0].right_button(buttons[1])
        buttons[0].down_button(buttons[3])

        buttons[1].left_button(buttons[0])
        buttons[1].right_button(buttons[2])
        buttons[1].down_button(buttons[4])

        buttons[2].left_button(buttons[1])
        buttons[2].down_button(buttons[5])

        buttons[3].up_button(buttons[0])
        buttons[3].right_button(buttons[4])
        buttons[3].down_button(buttons[6])

        buttons[4].up_button(buttons[1])
        buttons[4].left_button(buttons[3])
        buttons[4].right_button(buttons[5])
        buttons[4].down_button(buttons[7])
        buttons[4].set_chosen()

        buttons[5].up_button(buttons[2])
        buttons[5].left_button(buttons[4])
        buttons[5].down_button(buttons[8])

        buttons[6].up_button(buttons[3])
        buttons[6].right_button(buttons[7])

        buttons[7].up_button(buttons[4])
        buttons[7].left_button(buttons[6])
        buttons[7].right_button(buttons[8])

        buttons[8].up_button(buttons[5])
        buttons[8].left_button(buttons[7])

        for i in range(-2, 2):
            for j in range(-3, 4):
                add(Cube(app, "white", position=(2 * j, 2 + 4 * i, 0), rotation=(0, 0, 0), scale=(1, 1, 1)))

        for i in range(-2, 2):
            for j in range(-1, 2):
                add(Cube(app, "white", position=(2 + 4 * i, 4 * j, 0), rotation=(0, 0, 0), scale=(1, 1, 1)))

    def update(self):
        pass
