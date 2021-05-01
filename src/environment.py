#!/usr/share/env python3.8

from src.ant import Ant


class Environment:
    def __init__(self):
        self.ants = []
        self.ants.append(Ant(angle=45, speed=1.0))

    def update(self):
        for ant in self.ants:
            ant.update()
