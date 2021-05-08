from enum import IntEnum
from dataclasses import dataclass


class PheromoneType(IntEnum):
    HOME = 0
    FOOD = 1


@dataclass
class Pheromone:
    pheromone_type: PheromoneType
    x: float
    y: float
