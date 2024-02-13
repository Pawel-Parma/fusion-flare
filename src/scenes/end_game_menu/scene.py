from models import *


class EndGameMenu:
    def __init__(self, app):
        self.app = app
        self.shadow_objects = []
        self.no_shadow_objects = []
        self.load()

    def add_object(self, obj):
        if obj.is_shadowy:
            self.shadow_objects.append(obj)

        else:
            self.no_shadow_objects.append(obj)

        return obj

    def load(self):
        app = self.app
        add = self.add_object

        # buttons
        hover_texture = "white"
        # play
        new_game_button = add(Button(app, (-6, -0.5, 0), "img_2", hover_texture, scale=(1.5, 0.5)))
        new_game_button.on_click(lambda: app.play(new_maze=True))
        # replay
        replay_button = add(Button(app, (-6, -2, 0), "img_2", hover_texture, scale=(1.5, 0.5)))
        replay_button.on_click(app.play)
        # exit
        exit_button = add(Button(app, (-6, -3.5, 0), "img", hover_texture, scale=(1.5, 0.5)))
        exit_button.on_click(app.main_menu)

        # bind buttons
        new_game_button.set_chosen()
        new_game_button.down_button(replay_button)

        replay_button.up_button(new_game_button)
        replay_button.down_button(exit_button)

        exit_button.up_button(replay_button)

    def update(self):
        pass
