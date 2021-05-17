#!/usr/share/env python3.8
from typing import List

import numpy as np

from .pheromone import Pheromone, PheromoneType

PHEROMONE_INTENSITY = 1


class SingleTypePheromoneTracker:
    def __init__(self, width, height, pheromone_type: PheromoneType):
        self._width = width
        self._height = height
        self._pheromone_type = pheromone_type
        self._tracker = np.zeros((height, width))

    def get_data(self) -> np.ndarray:
        return self._tracker

    def add_pheromone(self, pheromone: Pheromone):
        x = int(pheromone.x)
        y = int(pheromone.y)
        self._tracker[self._height - y - 1, x] += PHEROMONE_INTENSITY

    def add_pheromones(self, pheromones: List[Pheromone]):
        for pheromone in pheromones:
            self.add_pheromone(pheromone)

    def get_point_intensity(self, x: int, y: int) -> float:
        return self._tracker[self._height - y - 1, x]

    def get_intensity(self, mask: np.ndarray) -> np.ndarray:
        return np.matmul(self._tracker, mask)

    # def update(self):
    #     ...
