import abc


class BaseScene(abc.ABC):
    def __init__(self, app, name, parent=None):
        self.app = app
        self.name = name
        self.parent = parent

        self.objects = []
        self.create_objects()

    def add_object(self, obj):
        self.objects.append(obj)
        return obj

    @abc.abstractmethod
    def create_objects(self):
        pass

    def update(self):
        pass
