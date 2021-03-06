#!/usr/share/env python3.8

import numpy as np

from src.simulation import Simulation

WIDTH = 720
HEIGHT = 480
BLACK_COLOR = (0, 0, 0, 1)
WHITE_COLOR = (1, 1, 1, 1)

np.random.seed(0)


if __name__ == "__main__":
    sim = Simulation(
        width=WIDTH,
        height=HEIGHT,
        bg_color=WHITE_COLOR,
        recording_abspath="",
    )
    sim.run()
