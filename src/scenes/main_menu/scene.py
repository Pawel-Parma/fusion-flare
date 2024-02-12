from models import *


class MainMenuScene:
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

        # game name
        """
        add(Text(app, "Maze", (0, 0.5, 0), scale=(0.5, 0.5, 0.5)))  # TEXT DOESN'T EXIST YET
        """

        # buttons
        hover_texture = "white"
        # play
        play_button = add(Button(app, (0, -0.5, 0), "img_2", hover_texture, scale=(1.5, 0.5)))
        play_button.on_click(lambda: app.play(new_maze=True))
        # history
        history_button = add(Button(app, (0, -2, 0), "black", hover_texture, scale=(1.5, 0.5)))
        # settings
        settings_button = add(Button(app, (0, -3.5, 0), "black", hover_texture, scale=(1.5, 0.5)))
        # exit
        exit_button = add(Button(app, (6, -3.5, 0), "img", hover_texture, scale=(1.5, 0.5), is_dynamic=True))
        exit_button.on_click(app.quit)

        play_button.set_chosen()
        play_button.right_button(exit_button)
        play_button.down_button(history_button)

        history_button.up_button(play_button)
        history_button.right_button(exit_button)
        history_button.down_button(settings_button)

        settings_button.up_button(history_button)
        settings_button.right_button(exit_button)

    def update(self):
        pass
