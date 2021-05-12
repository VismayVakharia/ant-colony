from pathlib import Path
from typing import Tuple

import pyglet

from .environment import Environment
from .generic_sprite import GenericSprite
from .ui import BaseWindow

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

        self.environment = Environment(width, height)

        self.batch = pyglet.graphics.Batch()
        self.ant_sprites = []
        for ant in self.environment.ants:
            self.ant_sprites.append(
                GenericSprite(ant, images_dir=ASSETS["ant"], scale=0.5, anchor=(75, 75), batch=self.batch)
            )

    def actual_draw(self):
        self.batch.draw()

    def actual_update(self, dt):
        self.environment.update(dt)
        for sprite in self.ant_sprites:
            sprite.render()
