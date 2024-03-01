import os
import os.path as op

import glm


def traverse_dir(path: str) -> list[str]:
    items = []
    to_check = list(os.listdir(path))

    while to_check:
        item = to_check.pop(0)
        item_dir = op.join(path, item)
        if op.isfile(item_dir):
            items.append(item_dir)

        else:
            items += traverse_dir(item_dir)

    return items


class Color(glm.vec4):
    def __init__(self, r: float, g: float, b: float, a: float = 0.0):
        super().__init__(r, g, b, a)
        self /= 255
