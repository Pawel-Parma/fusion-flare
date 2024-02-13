from models import *


class EscMenu:
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
        play_button = add(Button(app, (0, -0.5, 0), "img_2", hover_texture, scale=(1.5, 0.5)))
        play_button.on_click(app.play)
        # settings
        settings_button = add(Button(app, (0, -2, 0), "black", hover_texture, scale=(1.5, 0.5)))
        # exit
        exit_button = add(Button(app, (0, -3.5, 0), "img", hover_texture, scale=(1.5, 0.5)))
        exit_button.on_click(app.main_menu)
        # bind buttons
        play_button.set_chosen()
        play_button.down_button(settings_button)

        settings_button.up_button(play_button)
        settings_button.down_button(exit_button)

        exit_button.up_button(settings_button)

    def update(self):
        pass
