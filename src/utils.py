import numpy as np
import pyglet


class AnchoredMatrix:
    def __init__(self, start_row: int, start_col: int, data: np.array):
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
    def __init__(self, im_data: np.array):
        self._data = im_data

    def get_matrix_data(self, channel: int) -> np.array:
        assert channel in [0, 1, 2], f"channel {channel} must be 0, 1, 2"
        width, height = self._data.shape
        image = np.zeros((width, height, 3))
        image[:, :, channel] = self._data
        return image


def get_image_data(image: np.array) -> pyglet.image.ImageData:
    height, width, num_channels = image.shape
    number_of_bytes = height * width * num_channels
    image *= 255
    image = image.ravel()
    image_texture = (pyglet.gl.GLubyte * number_of_bytes)(*image.astype('uint8'))

    return pyglet.image.ImageData(width, height, 'RGB',
                                  image_texture, pitch=-1 * width * num_channels)
