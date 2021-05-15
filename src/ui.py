from pathlib import Path
from typing import Tuple

import pyglet
import pyglet.gl as gl


class BaseWindow(pyglet.window.Window):
    def __init__(
        self,
        width: int,
        height: int,
        bg_color: Tuple[float, float, float, float],
        recording_abspath: str = "",
    ):

        config = pyglet.gl.Config(sample_buffers=1, samples=4)
        super().__init__(width, height, config=config)
        gl.glClearColor(*bg_color)

        self.is_paused = False
        self.recording = False
        if recording_abspath:
            self.recording = True
            self.recording_path = Path(recording_abspath)
            self.ensure_recording_path()
            self.frame_count = 0

    def ensure_recording_path(self):
        self.recording_path.mkdir(parents=True, exist_ok=True)

    def actual_draw(self):
        raise NotImplementedError("actual_draw method must be implemented in sub-classes")

    def on_draw(self):
        self.clear()

        self.actual_draw()

        if self.recording:
            self.record()

    def record(self):
        file_path = str(self.recording_path / f"{self.frame_count}.png")
        pyglet.image.get_buffer_manager().get_color_buffer().save(file_path)
        self.frame_count += 1

    def on_key_release(self, symbol, modifiers):
        if symbol == pyglet.window.key.SPACE:
            self.is_paused = not self.is_paused

    def update(self, dt):
        if not self.is_paused:
            self.actual_update(dt)

    def actual_update(self, dt):
        raise NotImplementedError("update method must be implemented in sub-classes")

    def run(self):
        pyglet.clock.schedule_interval(self.update, 1 / 50)
        pyglet.app.run()
