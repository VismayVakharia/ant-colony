#!/usr/share/env python3.8
from typing import Tuple

import numpy as np

from .ant import Ant
from .food import FoodParticle
from .physical_object import PhysicalObject


class Environment:
    def __init__(self, width: int, height: int, num_ants: int = 10, num_food_particles: int = 50):
        self.width = width
        self.height = height

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
        if not (0 < obj.x < self.width):
            obj.angle = 180 - obj.angle
        elif not (0 < obj.y < self.height):
            obj.angle = -obj.angle

    def update(self, dt):
        for ant in self.ants:
            ant.update(dt)
            self.enforce_bounds(ant)
