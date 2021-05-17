import numpy as np
import pyglet


class AnchoredMatrix:
    def __init__(self, start_row: int, start_col: int, data: np.ndarray):
        self._start_row = start_row
        self._start_col = start_col
        self._data = data

    @property
    def num_rows(self) -> int:
        return self._data.shape[0]

    @property
    def num_cols(self) -> int:
        return self._data.shape[1]


class SingleChannelImage:
    def __init__(self, im_data: np.ndarray):
        self._data = im_data

    def get_matrix_data(self, channel: int) -> np.ndarray:
        assert channel in [0, 1, 2], f"channel {channel} must be 0, 1, 2"
        width, height = self._data.shape
        image = np.zeros((width, height, 3), dtype="uint8")
        max_data = np.max(self._data)
        if max_data > 0:
            data = 255 * self._data / max_data
        else:
            data = self._data
        image[:, :, channel] = data
        return image


def get_image_data(image: np.ndarray) -> pyglet.image.ImageData:
    height, width, num_channels = image.shape
    image = image.ravel()
    image_texture = image.tobytes()

    return pyglet.image.ImageData(width, height, "RGB", image_texture, pitch=-1 * width * num_channels)
