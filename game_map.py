from tcod.ecs import Registry

import numpy as np

import tile_types


def generate_game_map(registry: Registry, map_width, map_height, level=1):
    return registry.new_entity(
        components = {
            np.ndarray: np.full((map_width, map_height), fill_value=tile_types.floor, order="F"),
            ("width", int): map_width,
            ("height", int): map_height,
            ("level", int): level
        }
    )