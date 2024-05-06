import abc

from ..camera import CameraInterface


class Dimension(abc.ABC):
    def __init__(self, app, name):
        self.app = app
        self.name = name

        self.scenes = {}
        self.scene_to_render = None
        self.scenes_to_render = []
        camera = app.camera
        self.camera_values = CameraInterface(app, position=(0, 0, 10), fov=camera.fov, near=camera.near, far=camera.far,
                                             yaw=-90, pitch=0)
        self.create_scenes()

    def add_scene(self, scene):
        self.scenes[scene.name] = scene
        return scene

    def use(self):
        self.app.camera.use_vars_from(self.camera_values)

    def un_use(self):
        self.camera_values.use_vars_from(self.app.camera)

    @abc.abstractmethod
    def create_scenes(self):
        pass

    def render_one(self):
        self.update()
        if not self.scene_to_render:
            return

        self.scenes[self.scene_to_render].render()

    def render_list(self):
        self.update()
        for name in self.scenes_to_render:
            self.scenes[name].render()

    def render_all(self):
        self.update()
        for scene in self.scenes.values():
            scene.render()

    @abc.abstractmethod
    def update(self):
        pass
