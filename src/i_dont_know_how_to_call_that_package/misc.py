import os
import os.path as op


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
