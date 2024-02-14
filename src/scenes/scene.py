import abc


class BaseScene(abc.ABC):
    def __init__(self, app):
        self.app = app
        self.shadow_objects = []
        self.no_shadow_objects = []
        self.create_objects()

    def add_object(self, obj):
        if obj.is_shadowy:
            self.shadow_objects.append(obj)

        else:
            self.no_shadow_objects.append(obj)

        return obj

    @abc.abstractmethod
    def create_objects(self):
        pass

    def update(self):
        pass
