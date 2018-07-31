
import numpy as np


def compute_pi(segments: int) -> np.double:
    polygon_edge_length_squared = np.double(2.0)  # type: np.double
    polygon_sides = 2  # type: int
    for _ in range(segments):  # type: int
        polygon_edge_length_squared = -np.sqrt(1 - polygon_edge_length_squared / 4) * 2 + 2
        polygon_sides *= 2
    return np.sqrt(polygon_edge_length_squared) * polygon_sides
