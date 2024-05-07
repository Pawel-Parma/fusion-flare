from abc import ABC, abstractmethod

from ..camera import CameraInterface


class Sceneable(ABC):
    def __init__(self, app, name, parent):
        self.app = app
        self.name = name
        self.parent = parent

        self.camera = camera = app.camera
        self.camera_state = CameraInterface(app, (0, 0, 10), -90, 0, camera.fov, camera.near, camera.far)

        self.create_children()
        self.check_attributes()

    def use_camera(self):
        self.camera.use_vars_from(self.camera_state)

    def unuse_camera(self):
        self.camera_state.use_vars_from(self.camera)

    @abstractmethod
    def add_child(self, child):
        pass

    @abstractmethod
    def create_children(self):
        pass

    def check_attributes(self):
        if not hasattr(self, 'children'):
            raise AttributeError(f"Subclasses of Sceneable must define 'self.children'")

    @abstractmethod
    def update(self):
        pass

    @abstractmethod
    def render(self):
        pass
