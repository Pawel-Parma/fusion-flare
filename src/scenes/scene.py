import abc

from ..camera import CameraInterface


class BaseScene(abc.ABC):
    def __init__(self, app):
        self.app = app
        self.camera_values = CameraInterface(app, position=(0, 0, 10), yaw=-90, pitch=0)
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

    def use(self):
        self.app.camera.use_vars_from(self.camera_values)

    def un_use(self):
        self.camera_values.use_vars_from(self.app.camera)

    def update(self):
        pass
