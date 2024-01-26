import random


def generate_maze(width: int, height: int):
    return [[random.choice(("#", ".")) for _ in range(width)] for _ in range(height)]

