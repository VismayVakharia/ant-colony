import numpy as np

from .physical_object import PhysicalObject


class Ant(PhysicalObject):
    def __init__(self, x: float = 0.0, y: float = 0.0, angle: float = 0.0, speed: float = 10):
        super().__init__(x, y, angle)
        self._speed = speed

    @property
    def speed(self) -> float:
        return self._speed

    def update(self):
        self._angle += np.random.normal(0, 1)
        self._position += self.direction * self._speed
