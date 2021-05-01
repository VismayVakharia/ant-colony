import numpy as np


class Ant:
    def __init__(self, x: float = 0.0, y: float = 0.0, angle: float = 0.0, speed: float = 10):
        self._position = np.array([x, y])
        self._angle = angle
        self._speed = speed

    @property
    def position(self):
        return self._position

    @property
    def x(self):
        return self._position[0]

    @property
    def y(self):
        return self._position[1]

    @property
    def angle(self):
        return self._angle

    @angle.setter
    def angle(self, angle: float):
        self._angle = angle

    @property
    def direction(self):
        angle = np.deg2rad(self._angle)
        return np.array([np.cos(angle), np.sin(angle)])

    @property
    def speed(self):
        return self._speed

    def update(self):
        self._angle += np.random.normal(0, 1)
        self._position += self.direction * self._speed
