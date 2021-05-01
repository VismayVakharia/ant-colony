from typing import Tuple
from . import ui, environment
import pyglet


class AntSprite:
    def __init__(self, ant, batch: pyglet.graphics.Batch = None):
        self.ant = ant
        image = pyglet.image.load("ant.png")
        self.sprite = pyglet.sprite.Sprite(image, batch=batch)
        self.update()

    def update(self):
        self.sprite.update(x=self.ant.x, y=self.ant.y, rotation=-self.ant.angle)


class Simulation(ui.BaseWindow):
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

        self.environment = environment.Environment()

        self.batch = pyglet.graphics.Batch()
        self.ant_sprites = []
        for ant in self.environment.ants:
            self.ant_sprites.append(AntSprite(ant, batch=self.batch))

    def actual_draw(self):
        self.batch.draw()

    def actual_update(self, dt):
        self.environment.update()
        for sprite in self.ant_sprites:
            sprite.update()
