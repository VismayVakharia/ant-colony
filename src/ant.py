import numpy as np

from .pheromone import Pheromone, PheromoneType
from .physical_object import PhysicalObject


class Ant(PhysicalObject):
    def __init__(self, x: float = 0.0, y: float = 0.0, angle: float = 0.0, speed: float = 10):
        super().__init__(x, y, angle)
        self._speed = speed
        self._carrying_food: bool = False
        self._pheromone_drop_delay: float = 1
        self._time_since_last_drop: float = 0

    def drop_pheromone(self, dt: float):
        self._time_since_last_drop += dt
        if self._time_since_last_drop > self._pheromone_drop_delay:
            self._time_since_last_drop = 0
            pheromone_type = PheromoneType.FOOD if self._carrying_food else PheromoneType.HOME
            return Pheromone(pheromone_type, self.x, self.y)
        return None

    @property
    def speed(self) -> float:
        return self._speed

    def update(self, dt):
        self._angle += np.random.normal(0, 5)
        self._position += self.direction * self._speed * dt
