from math import hypot
import numpy as np

def distance_to_value(x1, y1, x2=None, y2=None, out_min=None, out_max=None, in_min=15, in_max=200):
    if x2 is not None and y2 is not None:
        length = hypot(x2 - x1, y2 - y1)
    else:
        length = x1  # x1 is length if x2/y2 not given

    if out_min is not None and out_max is not None:
        return np.interp(length, [in_min, in_max], [out_min, out_max])
    return length
