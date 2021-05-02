#!/usr/share/env python3.8

import numpy as np

from .ant import Ant
from .physical_object import PhysicalObject


class Environment:
    def __init__(self, width: int, height: int, num_ants: int = 10):
        self.width = width
        self.height = height
        self.ants = []
        for i in range(num_ants):
            self.ants.append(Ant(x=self.width / 2, y=self.height / 2, angle=np.random.randint(-180, 180), speed=50.0))

    def enforce_bounds(self, obj: PhysicalObject):
        if not (0 < obj.x < self.width):
            obj.angle = 180 - obj.angle
        elif not (0 < obj.y < self.height):
            obj.angle = -obj.angle

    def update(self, dt):
        for ant in self.ants:
            ant.update(dt)
            self.enforce_bounds(ant)
