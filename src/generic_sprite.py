import os
from typing import Tuple

import pyglet

from .physical_object import PhysicalObject


class GenericSprite(pyglet.sprite.Sprite):
    def __init__(
        self,
        obj: PhysicalObject,
        images_dir: str,
        scale: float = 1.0,
        anchor: Tuple[int, int] = (0, 0),
        batch: pyglet.graphics.Batch = None,
        group: pyglet.graphics.Group = None,
    ):
        self._obj = obj
        animation = self.load_animation(images_dir, anchor)
        super().__init__(animation, x=obj.x, y=obj.y, batch=batch, group=group)
        self.scale = scale
        self.render()

    def render(self):
        super().update(x=self._obj.x, y=self._obj.y, rotation=-self._obj.angle)

    @staticmethod
    def load_animation(
        images_dir: str, anchor: Tuple[int, int] = (0, 0), duration: float = 0.1
    ) -> pyglet.image.Animation:
        images = []
        pyglet.resource.path = [images_dir]
        pyglet.resource.reindex()
        for filename in sorted(os.listdir(images_dir)):
            image = pyglet.resource.image(filename)
            image.anchor_x, image.anchor_y = anchor
            images.append(image)
        return pyglet.image.Animation.from_image_sequence(images, duration=duration, loop=True)
