from typing import Tuple

import pyglet

from .physical_object import PhysicalObject


class GenericShape:
    def __init__(
        self,
        obj: PhysicalObject,
        shape: str,
        color: Tuple[int, int, int] = (0, 0, 0),
        batch: pyglet.graphics.Batch = None,
        group: pyglet.graphics.Group = None,
        **kwargs
    ) -> None:
        self._obj = obj
        str_pyglet_shape_mapping = {
            "circle": pyglet.shapes.Circle,
            "rectangle": pyglet.shapes.Rectangle,
        }

        if shape == "circle" and "radius" not in kwargs:
            raise Exception("Mandatory argument 'radius' not given")
        if shape == "rectangle" and "width" not in kwargs and "height" not in kwargs:
            raise Exception("Mandatory argument 'height' and 'width' not given")

        self._shape = str_pyglet_shape_mapping[shape](
            x=self._obj.x, y=self._obj.y, color=color, batch=batch, group=group, **kwargs
        )

    def refresh(self):
        self._shape.x = self._obj.x
        self._shape.y = self._obj.y
        self._shape.rotation = -self._obj.angle
