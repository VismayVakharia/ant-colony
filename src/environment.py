#!/usr/share/env python3.8
from typing import Tuple

import numpy as np

from .ant import Ant
from .food import FoodParticle
from .pheromone import PheromoneType
from .pheromone_tracker import SingleTypePheromoneTracker
from .physical_object import PhysicalObject


class Environment:
    def __init__(self, width: int, height: int, num_ants: int = 10, num_food_particles: int = 50):
        self.width = width
        self.height = height

        self.pheromone_trackers = {
            pheromone_type: SingleTypePheromoneTracker(width, height, pheromone_type)
            for pheromone_type in PheromoneType
        }

        self.food_particles = []
        for _ in range(num_food_particles):
            self.food_particles.append(FoodParticle(*self.random_position()))

        self.ants = []
        for _ in range(num_ants):
            self.ants.append(Ant(x=self.width / 2, y=self.height / 2, angle=np.random.randint(-180, 180), speed=50.0))

    def random_position(self) -> Tuple[int, int]:
        x = np.random.randint(0, self.width)
        y = np.random.randint(0, self.height)
        return x, y

    def enforce_bounds(self, obj: PhysicalObject):
        if not (0 < obj.x < self.width - 1):
            obj.angle = 180 - obj.angle
            obj.x = 0 if obj.x < 0 else self.width - 1
        elif not (0 < obj.y < self.height - 1):
            obj.angle = -obj.angle
            obj.y = 0 if obj.y < 0 else self.height - 1

    def update(self, dt):
        for ant in self.ants:
            ant.update(dt)
            self.enforce_bounds(ant)
            if (pheromone := ant.drop_pheromone(dt)) is not None:
                self.pheromone_trackers[pheromone.pheromone_type].add_pheromone(pheromone)
