from dataclasses import dataclass
from enum import IntEnum


class PheromoneType(IntEnum):
    HOME = 0
    FOOD = 1


@dataclass
class Pheromone:
    pheromone_type: PheromoneType
    x: float
    y: float
