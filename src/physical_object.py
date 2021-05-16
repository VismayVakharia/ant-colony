import numpy as np


class PhysicalObject:
    def __init__(self, x: float = 0.0, y: float = 0.0, angle: float = 0.0):
        self._position = np.array([x, y])
        self._angle = angle

    @property
    def position(self) -> np.ndarray:
        return self._position

    @property
    def x(self) -> float:
        return self._position[0]

    @x.setter
    def x(self, value: float):
        self._position[0] = value

    @property
    def y(self) -> float:
        return self._position[1]

    @y.setter
    def y(self, value: float):
        self._position[1] = value

    @property
    def angle(self) -> float:
        return self._angle

    @angle.setter
    def angle(self, angle: float):
        self._angle = angle

    @property
    def direction(self) -> np.ndarray:
        angle = np.deg2rad(self._angle)
        return np.array([np.cos(angle), np.sin(angle)])
