from pathlib import Path
from typing import Tuple

import pyglet

from .environment import Environment
from .generic_shape import GenericShape
from .generic_sprite import GenericSprite
from .pheromone import PheromoneType
from .ui import BaseWindow
from .utils import SingleChannelImage, get_image_data

ASSET_DIR = Path(__file__).parent.parent / "assets"
ASSETS = {"ant": str(ASSET_DIR / "ant")}


class Simulation(BaseWindow):  # pylint: disable=too-many-ancestors, abstract-method
    def __init__(
        self,
        width: int,
        height: int,
        bg_color: Tuple[float, float, float, float],
        recording_abspath: str = "",
    ):
        super().__init__(
            width=width,
            height=height,
            bg_color=bg_color,
            recording_abspath=recording_abspath,
        )
        self.fps = pyglet.window.FPSDisplay(self)

        self.environment = Environment(width, height)

        self.batch = pyglet.graphics.Batch()
        self.back_ground = pyglet.graphics.OrderedGroup(0)
        self.fore_ground = pyglet.graphics.OrderedGroup(1)

        self.pheromone_map = None

        self.ant_sprites = []
        for ant in self.environment.ants:
            self.ant_sprites.append(
                GenericSprite(
                    ant, images_dir=ASSETS["ant"], scale=0.5, anchor=(75, 75), batch=self.batch, group=self.fore_ground
                )
            )

        self.food_sprites = []
        for food_particle in self.environment.food_particles:
            self.food_sprites.append(
                GenericShape(food_particle, "circle", radius=2, batch=self.batch, group=self.fore_ground)
            )

    def actual_draw(self):
        if self.pheromone_map:
            self.pheromone_map.blit(0, 0)
        self.batch.draw()
        self.fps.draw()

    def actual_update(self, dt):
        self.environment.update(dt)

        channels = []
        for pheromone_type in PheromoneType:
            channel = SingleChannelImage(self.environment.pheromone_trackers[pheromone_type].get_data())
            channels.append(channel.get_matrix_data(pheromone_type))

        self.pheromone_map = get_image_data(sum(channels))

        for sprite in self.ant_sprites + self.food_sprites:
            sprite.refresh()
