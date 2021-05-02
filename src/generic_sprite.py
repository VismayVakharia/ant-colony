import os

import pyglet


class GenericSprite(pyglet.sprite.Sprite):
    def __init__(self, obj, images_dir: str, batch: pyglet.graphics.Batch = None):
        self._obj = obj
        animation = self.load_animation(images_dir)
        super().__init__(animation, x=obj.x, y=obj.y, batch=batch)
        self.update()

    def update(self):
        super().update(x=self._obj.x, y=self._obj.y, rotation=-self._obj.angle)

    def load_animation(self, images_dir: str, duration: float = 0.1):
        images = []
        pyglet.resource.path = [images_dir]
        pyglet.resource.reindex()
        for filename in sorted(os.listdir(images_dir)):
            images.append(pyglet.resource.image(filename))
        return pyglet.image.Animation.from_image_sequence(images, duration=duration, loop=True)
